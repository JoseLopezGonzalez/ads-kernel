# GATE DE CIERRE INDEPENDIENTE DE F4C

> **Nota de transcripción — la escribe el agente principal, NO los revisores ni el adjudicador.**
>
> ```text
> QUÉ ES ESTE DOCUMENTO   el GATE DE CIERRE de `F4c`: la verificación independiente de si la
>                         arquitectura vigente es SUFICIENTE PARA F5, y la adjudicación
>                         individual de los 43 hallazgos que el gate anterior dejó abiertos.
>                         **No corrige nada.** Sólo verifica y adjudica.
>
> QUÉ VERIFICA            el rango de corrección
>                         `7e99388…0a4b3a0` (OCHO commits) · las decisiones `D71`–`D86` · la
>                         resolución declarada de los 43 hallazgos distintos · que la propia
>                         corrección no haya introducido contradicciones · y la proyección
>                         vigente completa de `11-ARQUITECTURA-INTEGRADA.md`.
>
> QUIÉN JUZGA             TRES agentes con CONTEXTO LIMPIO. Ninguno escribió F4 ni sus
>                         correcciones, ninguno participó en `D16`–`D86` ni en `O1`–`O16`, y
>                         ninguno fue revisor `A`–`F` de los documentos 16 y 17:
>                           REVISOR G      protocolo, estado, transacciones, recuperación,
>                                          Git, tipos y fuentes de verdad
>                           REVISOR H      capacidades, procesos, composición de rutas,
>                                          handoffs, macrocircuitos, documentación, adopción,
>                                          F5/F6, operabilidad y los ocho externos
>                           ADJUDICADOR I  recibió los dos dictámenes YA CERRADOS, verificó
>                                          cada afirmación contra su fichero y su línea, y
>                                          emite el ÚNICO veredicto
>
> CÓMO SE PROTEGIÓ LA     `G` y `H` trabajaron EN PARALELO y no vieron el dictamen del otro
> INDEPENDENCIA           hasta terminar. Comprobado mecánicamente: cada uno menciona al otro
>                         DOS veces, y las cuatro menciones son declaraciones de que no lo
>                         consultó — ninguno cita contenido del otro. `I` los recibió DESPUÉS
>                         de que ambos cerraran, y **no resolvió por mayoría**: corrigió a `G`
>                         en `A2`, corrigió a `H` en `A10` y en `F-08`, reubicó cuatro citas
>                         mal situadas, rechazó dos inferencias y un hallazgo completo.
>
> QUIÉN TRANSCRIBE        el agente principal, que SÍ escribió las correcciones del rango
>                         verificado y por tanto **NO PUEDE CERTIFICAR SU PROPIO TRABAJO**.
>                         Copia los tres textos LITERALMENTE. **No ha suavizado, reinterpretado
>                         ni corregido ningún hallazgo.** Donde el adjudicador cita
>                         `scratchpad/inventario-18.md`, se refiere al inventario que este
>                         documento reproduce entero, aquí abajo.
>
> SOBRE QUÉ ÁRBOL         HEAD `0a4b3a08ee5b0d0f896c82a892ec8ea15383fc05`, rama
>                         `redesign/kernel-2.0`, árbol limpio, VEINTIÚN commits sin publicar.
>
> QUÉ NO SE HA HECHO      NINGÚN hallazgo se ha corregido en esta pasada.
>                         `11-ARQUITECTURA-INTEGRADA.md` NO se ha tocado. Los documentos 15,
>                         16 y 17, las decisiones `D1`–`D86` y las resoluciones `O1`–`O16`
>                         permanecen INTACTOS.
> ```

---

## El veredicto, por delante

> # INSUFICIENTE PARA F5

**`F4c` NO se cierra y sigue ABIERTA. F5 NO queda autorizada.**

Y falla por **dos razones independientes**, cualquiera de las cuales bastaría:

```text
1  LA COBERTURA         CATORCE fuentes obligatorias —3 420 líneas, el 10,9 % del corpus—
   NO CUMPLE            sin ninguna lectura sustantiva. DIEZ de ellas son de las diecinueve
                        que el PRIMER gate ya había omitido una vez. Y el documento 15 —la
                        TERCERA REVISIÓN INDEPENDIENTE, donde vive la causa original de
                        `D64`–`D68`— estaba asignado a los DOS revisores y no lo abrió
                        ninguno: el objeto se juzgó por su propia descripción de la fuente.

2  EL FONDO             de las 43 filas, **DIEZ son FALLIDAS** —entre ellas DOS de severidad
   TAMPOCO CIERRA       BLOQUEANTE original y DOS GRAVES—, y quedan **28 hallazgos
                        consolidados**: 0 bloqueantes, OCHO graves, OCHO medios y DOCE
                        menores. **SEIS de los veintiocho los introdujo o los perpetuó la
                        propia tanda de corrección** — que es la novena, y la segunda que
                        alguien mira.
```

**Lo único que exige una decisión de diseño nueva** en toda la lista de condiciones es el
plano de `estado/cuarentena/<TX>/`, y son cinco líneas. Todo lo demás se cierra propagando
material que el corpus ya tiene escrito.

---

## Inventario del corpus obligatorio

Derivado de los documentos 16 y 17, con su reparto entre `G` y `H`. **56 ficheros, 31 517
líneas.** La columna `revisor` es la asignación; **lo que cada uno leyó de verdad está en la
sección 2 de su dictamen, y la auditoría de esa cobertura, en la sección 4 de la
adjudicación.**

| # | path | SHA-256 (16) | líneas | revisor |
|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | `2b183503df95a1ca` | 101 | G+H |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | `45984236979cedda` | 7827 | G+H |
| 3 | `docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` | `b0e015c118ceb916` | 652 | G+H |
| 4 | `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | `8243034f286160cc` | 1258 | G+H |
| 5 | `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` | `18f876d4cd47a2f7` | 1651 | G+H |
| 6 | `docs/evolucion/ADS-NEXT-OWNER-BRIEF.md` | `e82036724b92bdd6` | 1342 | H |
| 7 | `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | `a88609167dbbea28` | 2164 | H |
| 8 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | `265ddf72008b52c2` | 1342 | G+H |
| 9 | `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | `64d170f5acc15144` | 3344 | H |
| 10 | `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | `48412108f711204f` | 598 | H |
| 11 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | `54333d773a4156e5` | 512 | G+H |
| 12 | `docs/rediseno/a-CAPACIDADES-APROBADA.md` | `10cafb5ceee44f57` | 1133 | G+H |
| 13 | `docs/rediseno/a-ENMIENDA-E1-ENC.md` | `18dae19523b25ed4` | 212 | H |
| 14 | `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | `9d5a23806fc33fc1` | 231 | G |
| 15 | `docs/rediseno/b-RECORRIDO-APROBADA.md` | `f8cb974316e283fa` | 1289 | H |
| 16 | `kernel/operativo/00-INDICE.md` | `fa3affa7b2bebc00` | 140 | H |
| 17 | `kernel/operativo/capacidades/APR/CAPACIDAD.md` | `a870911530909584` | 96 | H |
| 18 | `kernel/operativo/capacidades/ARQ/CAPACIDAD.md` | `6ca11b5f09883e24` | 105 | H |
| 19 | `kernel/operativo/capacidades/CON/CAPACIDAD.md` | `e0f79e6c3a467302` | 108 | H |
| 20 | `kernel/operativo/capacidades/DIS/CAPACIDAD.md` | `06f019010d45771f` | 148 | H |
| 21 | `kernel/operativo/capacidades/DOM/CAPACIDAD.md` | `926c7144cb098caa` | 136 | H |
| 22 | `kernel/operativo/capacidades/DSP/CAPACIDAD.md` | `acb292f882e77d74` | 153 | H |
| 23 | `kernel/operativo/capacidades/ENC/CAPACIDAD.md` | `f71b8e43f6e2d66f` | 175 | H |
| 24 | `kernel/operativo/capacidades/ENT/CAPACIDAD.md` | `91a81d3cf1cbfa61` | 124 | H |
| 25 | `kernel/operativo/capacidades/INV/CAPACIDAD.md` | `47412638e7552da1` | 97 | H |
| 26 | `kernel/operativo/capacidades/PLT/CAPACIDAD.md` | `a5f87977c58ed1d0` | 109 | H |
| 27 | `kernel/operativo/capacidades/PRD/CAPACIDAD.md` | `e83b0e08272e219d` | 106 | H |
| 28 | `kernel/operativo/capacidades/SEG/CAPACIDAD.md` | `19bfd38a7a24b57f` | 136 | H |
| 29 | `kernel/operativo/capacidades/SIS/CAPACIDAD.md` | `02089f36d1244356` | 120 | H |
| 30 | `kernel/operativo/capacidades/USO/CAPACIDAD.md` | `65f144e4a5c756ef` | 95 | H |
| 31 | `kernel/operativo/capacidades/VER/CAPACIDAD.md` | `91a16b482629daf3` | 136 | H |
| 32 | `kernel/operativo/circuitos/DIS-handoffs.md` | `87bb395766164dfd` | 248 | H |
| 33 | `kernel/operativo/circuitos/handoffs-generales.md` | `1902884c33728729` | 246 | H |
| 34 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | `825f15a914c10d6f` | 162 | H |
| 35 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | `3ee58ca4bc47988d` | 540 | H |
| 36 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | `d56bf6b81e0fe4a9` | 151 | H |
| 37 | `kernel/operativo/contratos/C4-MATERIALIZACION.md` | `670289180e59b176` | 171 | H |
| 38 | `kernel/operativo/contratos/C5-HANDOFF.md` | `af6f1a4c4f5def8d` | 116 | H |
| 39 | `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` | `14805a79aeb07f31` | 337 | G |
| 40 | `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | `83f82e2be4756a46` | 251 | G |
| 41 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | `08f4bea44594e026` | 142 | H |
| 42 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | `dd323d1aa2f7ede3` | 353 | H |
| 43 | `kernel/operativo/diseno/02-RUBRICAS.md` | `8aa8fb18426eac21` | 344 | H |
| 44 | `kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md` | `8695161d660b9bc5` | 265 | H |
| 45 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | `5d2f54535c1334c0` | 131 | H |
| 46 | `kernel/operativo/diseno/05-FIDELIDAD.md` | `fdabb29f7592e603` | 130 | H |
| 47 | `kernel/operativo/entrada/00-INDICE.md` | `315b2790cb66bb4c` | 29 | H |
| 48 | `kernel/operativo/entrada/02-CIRCUITO.md` | `e204167c8895bff9` | 146 | H |
| 49 | `kernel/operativo/entrada/03-FORMAS.md` | `cdb3b575f8a28a5a` | 558 | H |
| 50 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | `1716bd3d8b48107d` | 188 | H |
| 51 | `kernel/operativo/entrada/05-ESCENARIOS.md` | `31f2dcece59e2ecb` | 638 | H |
| 52 | `kernel/operativo/esquemas/encuadre.yaml` | `eda2b350ebb75b81` | 80 | G |
| 53 | `kernel/operativo/esquemas/handoff.yaml` | `9ff258d33e88a357` | 18 | G |
| 54 | `kernel/operativo/esquemas/memoria.yaml` | `3425f11da9529e88` | 18 | G |
| 55 | `kernel/operativo/esquemas/proceso.yaml` | `bd391d5acddff134` | 50 | G |
| 56 | `kernel/operativo/recorrido/01-PROCESOS.md` | `98b5cbc836121044` | 565 | H |
| | **TOTAL · 56 ficheros** | | **31517** | |

---

# DICTAMEN DEL REVISOR G

# DICTAMEN DEL REVISOR G — GATE DE CIERRE INDEPENDIENTE DE `F4c`

**Materia:** protocolo transaccional, estado, transacciones, recuperación, Git, tipos y
fuentes de verdad.

---

## 1 · Identidad, procedencia y modo

Soy el **REVISOR G** del gate de cierre independiente de `F4c`.

```text
REPOSITORIO      /home/jose/ads-kernel
RAMA             redesign/kernel-2.0
HEAD             0a4b3a08ee5b0d0f896c82a892ec8ea15383fc05   (verificado con git rev-parse)
ÁRBOL            limpio (git status --porcelain vacío)
RANGO OBJETO     7e99388557323c1e0933ff5f2bd9bc5b2fc5708a..0a4b3a08ee5b0d0f896c82a892ec8ea15383fc05
                 OCHO commits, verificados con git log --oneline
MODO             SÓLO LECTURA. No he modificado ningún fichero, no he hecho ningún commit
                 y no he ejecutado ninguna escritura de git
```

**Qué NO soy.** No escribí `F4`, `F4b` ni `F4c`. No apliqué ninguna de sus correcciones. No
participé en ninguna decisión `D16`–`D86` ni en ninguna resolución `O1`–`O16`. No fui revisor
A, B, C, D, E ni F de los documentos 16 y 17. **No he consultado al REVISOR H, no supongo
nada de lo que diga, y ninguna afirmación de este dictamen depende de él.**

**Qué he tratado como OBJETO y qué como FUENTE.** Objeto: `11-ARQUITECTURA-INTEGRADA.md`,
`CHECKPOINT-ADS-NEXT.md`, `DECISIONES-Y-CONTRADICCIONES.md`, `00-INDICE.md` y los mensajes
de commit del rango. Fuente contrastable: los documentos 15, 16 y 17 —para leer la causa
original de cada hallazgo—, `a-CAPACIDADES-APROBADA.md`, `C6`, `C7` y los esquemas del
kernel. Cada cita que aparece abajo la he abierto en su fichero con `sed`/`grep`. **Ningún
recuento de este dictamen está copiado del documento: todos están derivados.**

---

## 2 · Corpus realmente leído

| path | SHA-256 (16) | líneas | íntegro | qué contrasta |
|---|---|---|---|---|
| `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | `45984236979cedda` | **7826** | **SÍ** | es el objeto. Los seis puntos del encargo, todas mis filas de la matriz y los diez hallazgos nuevos |
| `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | `8243034f286160cc` | 1257 | **parcial** | L1–505 íntegras (nota de transcripción, corpus, dictamen íntegro del REVISOR A con `A1`–`A14`, sus no reproducidos y sus limitaciones) + lectura dirigida de `M-8` (L876–893) y de la adjudicación (L1042–1095, L1200–1260). **NO leí el dictamen del REVISOR B salvo `M-8`** |
| `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` | `18f876d4cd47a2f7` | 1650 | **parcial** | lectura dirigida: `F-03` y `F-12` (L1255–1310), `M-8`/`A11` (L326–336, L785–791, L823–825), clasificación de los doce (L1310–1355) |
| `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | `265ddf72008b52c2` | 1341 | **parcial** | L1150–1290 íntegras: la matriz de cierre de los 43, el recuento derivado y las 30 comprobaciones mecánicas. Más barridos sobre `A1`–`A13`, `M-8`, `F-03`, `F-12`, «único escritor» y `estado/deriva` |
| `docs/evolucion/00-INDICE.md` | `2b183503df95a1ca` | 100 | **SÍ** | `F-12`: el reanclaje de las proyecciones de los documentos 15, 16 y 17 |
| `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | `54333d773a4156e5` | 511 | **parcial** | L225–300 íntegras (`D64`–`D86` y el bloque de `O1`–`O6`). Más el diff completo del rango sobre este fichero |
| `docs/rediseno/a-CAPACIDADES-APROBADA.md` | `10cafb5ceee44f57` | 1132 | **parcial** | `a.9` L660–700 íntegro —los cinco conceptos, `ACTOR ATRIBUIDO`, la tabla de autoridad y ejecutor, el tablero como canal de órdenes—, que es la fuente contra la que verifico `A7` y `A13`. **`a.7` NO leído íntegro**: sólo por barrido de `FRENO 3` |
| `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | `9d5a23806fc33fc1` | 230 | **NO** | sólo barrido sobre `E2.4`/`G29` y `E2.6`. **Declarado: no lo cubrí** |
| `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` | `14805a79aeb07f31` | 336 | **parcial** | `N1`–`N14` (L29–42), frontera y topología (L54–132, L183–188, L283). Verifica `F-03` y la excepción de §6.7 |
| `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | `83f82e2be4756a46` | 250 | **parcial** | cabecera L1–22, tabla de propiedad L80–95, `aplica_a` L170. **Intactidad verificada con `git diff` sobre el rango: vacío** |
| `kernel/operativo/esquemas/memoria.yaml` | `3425f11da9529e88` | 17 | **SÍ** | §3.7: `plano` y `estado` **no** están; `capa` sigue obligatorio. Coherente con «esta fase no toca esquemas» |
| `kernel/operativo/esquemas/proceso.yaml` | `bd391d5acddff134` | 49 | **SÍ** | `F-02`: `capacidad` y `capacidad_productora` son `texto`, no `ref_a` |
| `kernel/operativo/esquemas/handoff.yaml` | `9ff258d33e88a357` | 17 | **SÍ** | contraste con `proceso.yaml`: aquí `de`/`a` sí son `ref_a: capacidad` |
| `kernel/operativo/esquemas/encuadre.yaml` | `eda2b350ebb75b81` | 79 | **SÍ** | `F-04`: `grado_inicial` obligatorio |
| `kernel/operativo/esquemas/` (inventario) | — | 19 `.yaml` | **SÍ** | §3.8: los 19 esquemas vigentes, contados por mí |

**`kernel/operativo/esquemas/evento.yaml` NO EXISTE**, comprobado con `ls`. No lo trato como
omisión de cobertura: el tipo `evento` es nuevo de `F4`, su esquema lo construye F6 y §3.6 es
su contrato.

**Lo que NO cubrí, sin adorno:**

```text
1  El dictamen del REVISOR B del documento 16, salvo `M-8`. No afirmo nada sobre sus
   hallazgos ni sobre su eje.
2  `a-ENMIENDA-E2-MULTIREPO.md` íntegro. Verifiqué `E2.4`/`E2.6` por barrido, no por
   lectura completa: una cita correcta de un tramo no garantiza que otro no diga lo
   contrario.
3  `a.7` íntegro, `b.14` y `b.16` íntegros, `C1`–`C5`, y los validadores línea a línea.
4  Los documentos 12, 13, 14 y 15. **NO he leído `15-TERCERA-REVISION-INDEPENDIENTE-F4C.md`
   íntegro**: verifiqué su contenido a través de las citas del documento 16 y del registro
   de decisiones. Las causas originales de MIS filas de la matriz están todas en los
   documentos 16 y 17, que sí abrí en los tramos que las contienen.
5  Una discrepancia de recuento: el encargo dice que el documento 11 tiene **7827** líneas;
   `wc -l` sobre el árbol en `HEAD` da **7826**. No es un hallazgo: es una diferencia de
   cómo se cuenta la última línea. Lo declaro para que nadie lo lea como que revisé otro
   fichero.
```

---

## 3 · Método y comandos

```bash
git rev-parse HEAD                                            # 0a4b3a0…, anclado
git status --porcelain                                        # vacío: modo lectura
git log --oneline 7e99388..0a4b3a0                            # 8 commits
git diff --stat 7e99388..0a4b3a0                              # 4 ficheros, 1128+/213-
git diff 7e99388..0a4b3a0 -- kernel/operativo/contratos/C7-*  # VACÍO → C7 intacto
git diff --stat 7e99388..0a4b3a0 -- kernel/operativo/esquemas/  # VACÍO
git show 7e99388:docs/evolucion/11-ARQUITECTURA-INTEGRADA.md > /tmp/…/11-base.md

sha256sum <cada fichero del corpus> | cut -c1-16
wc -l <cada fichero del corpus>

# ── recuentos derivados por mí, no copiados ──────────────────────────────────
sed -n '1329,1372p' 11-*.md | sed 's/^| \(`X[0-9]*`\).*/\1/' | grep -c '^`X'   # 42 filas
sed -n '1329,1372p' 11-*.md | sed 's/^| \(`X[0-9]*`\).*/\1/' | sort -u | wc -l # 42 ids
ls kernel/operativo/esquemas/*.yaml | wc -l                                    # 19
# fases, estados del campo y filas del contrato: contados a mano sobre L3375-3377,
# L3716-3721 y la tabla L3801-3807

# ── barridos de predicado, enum y espacio de nombres ─────────────────────────
grep -n 'abierta(tx)' 11-*.md
grep -n 'sin `derivada`\|único terminal\|sin evento `derivada`' 11-*.md
grep -n 'cinco conceptos\|CINCO CONCEPTOS\|CINCO CAMPOS' 11-*.md
grep -n 'estado/tx\|estado/deriva\|estado/cuarentena\|gitignore\|X27' 11-*.md
grep -n 'agotado\|intentos_consumidos\|#observaciones' 11-*.md
grep -n 'estado mixto\|MAIN NUNCA\|no hay estado que perder' 11-*.md /tmp/…/11-base.md
grep -n 'único escritor' 11-*.md DECISIONES-*.md CHECKPOINT-*.md

# ── verificación contra la fuente aprobada ───────────────────────────────────
sed -n '665,700p' docs/rediseno/a-CAPACIDADES-APROBADA.md    # los cinco conceptos, literal
grep -n 'aplica_a' kernel/operativo/contratos/C7-*.md        # L170, «una o más fuentes»

# ── ejecución real (sólo lectura) ────────────────────────────────────────────
for v in kernel/operativo/validadores/*.py; do python3 "$v"; done
python3 -V                                                    # 3.10.12
```

**Ejecución de validadores, resultado.** `ads_lint` **0 errores · 0 avisos**;
`comprobar_contratos` 18/0; `comprobar_negativos` 67 infracciones detectadas · **0 no
detectadas**; `comprobar_recuentos`, `comprobar_referencias`, `comprobar_versiones`,
`comprobar_integridad`, `comprobar_evidencia`, `comprobar_prompts`, `comprobar_packs` todos
en verde. Las dos fallidas —`comprobar_fuentes` (`T159`) y `comprobar_arranque` (`T148`)—
son la limitación de Python 3.10 que el gate ya clasificó como `A14`, **ajena a F4**, y no
las cuento como defecto del entregable.

---

## 4 · Comprobaciones independientes: derivado frente a declarado

| # | qué | lo que el documento DECLARA | lo que YO DERIVÉ | ¿coinciden? |
|---|---|---|---|---|
| 1 | fases transaccionales | **5** (§2.6.1 L560, §3.6 L3716) | **5**: `preparada` `confirmada` `conflicto` `abandonada` `derivada` | **SÍ** |
| 2 | terminales | **2** (§2.6.1 L594–596) | **2**: `derivada` y `abandonada`, mutuamente excluyentes | **SÍ** |
| 3 | transiciones admitidas | 6 filas (L665–672) | **6**: 1 inicial + `preparada`→2 + `conflicto`→2 + `confirmada`→1 | **SÍ** |
| 4 | nodos no terminales sin sucesor en el grafo | **0** (L1993–1997) | **0**. `4b` no es nodo del grafo: es condición material | **SÍ** |
| 5 | estados del campo `fase` | **6** (L3720) | **6**: las cinco más la ausencia | **SÍ** |
| 6 | filas del contrato condicional fase a fase | **7** (L3787) | **7**: 5 fases + `deriva` + `fallo` (L3801–3807) | **SÍ** |
| 7 | valores de `evento.tipo` | **9** (L3713) | **9** | **SÍ** |
| 8 | espacio bruto `tipo`×`fase` | **54** (L3723) | 9 × 6 = **54** | **SÍ** |
| 9 | combinaciones **válidas** | **34** (L3731) | 5×5=25 + 6 + 1 + 1 + 1 = **34** | **SÍ** |
| 10 | combinaciones **prohibidas** | **20** (L3737) | 5 + 5 + 5 + 5 = **20**; 34+20=54, la partición cierra | **SÍ** |
| 11 | los tres regímenes | 5 · 1 · 3 (L3725–3729) | **5 + 1 + 3 = 9**, y los nueve tipos quedan cubiertos sin solape | **SÍ** |
| 12 | valores de `deriva.causa` | **3**, sede única §3.6 (L3806) | **3**, y `tx_afectada` condicional coherente en L3768, L3806 y la capa A | **SÍ** |
| 13 | filas de la tabla adversarial §2.6.7 | **42 filas / 42 ids** (L1397) | **42 / 42**, huecos `X24`, `X29`–`X36`, `X40`–`X46`; ninguna fila repetida | **SÍ** |
| 14 | comprobaciones `X-A`–`X-H` | **8** (L2935) | **8** (L2941–2948) | **SÍ** |
| 15 | ventanas de caída | **17** (L1043) | W1–W11 + W12a + W12b + W13–W16 = **17** | **SÍ** |
| 16 | esquemas vigentes del kernel | **19** (§3.8 L4110) | **19** `.yaml` en `esquemas/`, contados con `ls` | **SÍ** |
| 17 | recuento total §3.8 | 19 + 4 + 2 = **25** | **25** | **SÍ** |
| 18 | presiones normativas vigentes | **11** (§0 L123, §16 L7540, §19 L7768) | **11**: `PN-1`,`2`,`3`,`6`–`13`; `PN-4` retirada, `PN-5` fusionada; 3+1+1 = 5 de la entrega anterior | **SÍ** |
| 19 | los cinco conceptos de `a.9` | §3.6 L3404–3412 los cita bien | **verificado literal** contra `a-CAPACIDADES-APROBADA.md` L671–679 | **SÍ en §3.6** |
| 20 | los cinco conceptos en §2.6.10 regla 1 | «los CINCO conceptos de `a.9`: ordenante · autoridad · escritor_del_comando · ejecutor · **actor_atribuido**» (L2038–2040) | `a.9` L665 pone `ACTOR ATRIBUIDO` en **otra lista**; el quinto concepto es `PROPIETARIO DEL CAMPO` | **NO** — ver `A7` |
| 21 | sedes que CITAN `abierta(tx)` | «§2.5 · §2.6.4 · §2.6.6 · §2.6.8 · §2.6.9 · §2.9 · §7.4. **Las siete REMITEN aquí. Ninguna lo redeclara**» (L621–624) | **7 citas reales**, en §2.5 (L496), **§2.6.5** (L1061), §2.6.6 (L1220), §2.6.8 (L1501), **§2.6.11** (L2313), §2.9 (L2647) y §7.4 (L5253). **§2.6.4 y §2.6.9 NO lo citan**; §2.6.4 lo **redeclara** en L894 | **cifra SÍ, censo NO** |
| 22 | `C7` intacto en el rango | «`C7` no se toca en esta pasada» (L2298) | `git diff` sobre el rango: **vacío**. `aplica_a` L170 conserva «una o más fuentes» | **SÍ** |
| 23 | esquemas intactos en el rango | esta fase no toca esquemas ni contratos | `git diff --stat` sobre `kernel/operativo/esquemas/`: **vacío** | **SÍ** |
| 24 | ficheros tocados por el rango | corrección de los 43 en el documento 11, el registro y el checkpoint | **4**: `11-ARQ`, `CHECKPOINT`, `DECISIONES`, `00-INDICE`. Ni kernel, ni esquemas, ni contratos | **SÍ** |

**Veredicto de esta sección.** **Veintitrés de veinticuatro cuadran**, incluida toda la
aritmética del eje `tipo`×`fase` —34 · 20 · 54— y las tres cifras que el encargo me pidió
desconfiar expresamente: **§3.8 dice 25 y son 25; §3.6 dice cinco fases, seis estados y
siete filas y son cinco, seis y siete; §2.6.7 declara cuarenta y dos filas adversariales y
son cuarenta y dos, con cuarenta y dos identificadores distintos**. Los dos que no cuadran
son `A7` (fila 20) y el censo de sedes de `abierta(tx)` (fila 21), y los trato abajo.

---

## 5 · Los seis puntos del encargo

### 5.1 · `D71` — el predicado `abierta(tx)`

**Derivación desde cero, leyendo §2.6 entero y sin fiarme de cómo lo enuncia §2.6.1.**

Recorrí §2.6.0 a §2.6.11 y derivé el autómata de las cinco fases (L630–661), la tabla de
transiciones (L665–672), la tabla de cardinalidad condicional (L996–1005), las diecisiete
ventanas (L1052–1070), la tabla adversarial (L1329–1372) y las siete secuencias completas
(L1936–1990). El predicado que se sigue de todo eso es:

```text
abierta(tx) ≡ ∃ `preparada` durable con ese `tx`
              ∧ ¬∃ evento de ese `tx` con `fase` ∈ { `derivada`, `abandonada` }
```

**Coincide exactamente con el enunciado de §2.6.1 L611–612.** No he encontrado ninguna
propiedad del protocolo que exija un predicado distinto.

**Fases y transiciones reales.** Cinco fases; seis transiciones; `preparada` sale a dos
(`confirmada`, `conflicto`), `conflicto` sale a dos (`confirmada`, `abandonada`),
`confirmada` sale a una (`derivada`). Ningún nodo no terminal queda sin sucesor. Lo
verifiqué recorriendo la tabla, no leyendo su resumen. **CORRECTO.**

**Terminales.** DOS: `derivada` y `abandonada` (L594–596, L675, L993–994), mutuamente
excluyentes, y toda transacción cerrada tiene exactamente uno. **CORRECTO.**

**El marcador `estado/tx/<TX>.abierta`.** Nace en el paso 2 de §2.6.3 (L798–802), después
del punto de compromiso; se retira **por igual tras los dos terminales** (L688–689, L1004,
L1889–1892); lo reconstruye el arranque desde el diario, y §2.9 L2647 declara la fuente y la
condición —el predicado— con todas las letras. `W14` (L1068) cubre la caída al crearlo y
`W8` (L1061) la caída antes de borrarlo. **CORRECTO y consistente.**

**La regla de commit.** «ADS nunca hace commit de un árbol con una transacción abierta»
(L1252–1253), commit sólo entre transacciones, y el commit se desbloquea en cuanto no queda
marcador **y no hay estado especulativo vivo** (L1839–1842). Un `deriva` sin reparar **no**
impide commitear: impide despachar los items que nombra. **CORRECTO**, y es la corrección
material que `B1` exigía.

**La recuperación.** §2.6.4 clasifica contra la intención durable —una sola desde `D64`— en
tres cajas, con dos preguntas previas (paso 0 y paso 1) que deciden si hay transacción. Las
diecisiete ventanas están cubiertas y el reparto «se completa / se revierte / se escala»
(L1074–1089) es coherente con las tres cajas. **CORRECTO.**

**`abandonada` y `derivada`.** `abandonada` es cierre terminal sin completar, exige el
procedimiento A–E de §2.6.9 (L1691–1723) con restauración verificada byte a byte, y es
**inalcanzable hasta completarlo entero**. `derivada` es cierre completo. **CORRECTO.**

**Ninguna sede vigente afirma que `derivada` es el único terminal — con UNA excepción que sí
es vigente.** Las menciones legítimas, que distingo expresamente y **no** cuento como
defecto, son: L603 y L2305 (notas de corrección que citan lo que sustituyen), L7034
(registro de `D46`), L7143 (registro de `D71`) y `DECISIONES-Y-CONTRADICCIONES.md` L234
(`D65`, revisado por `D84` en su columna «qué revisa»). Todas son texto marcado como
histórico, y `X47` (L1361) declara esa disciplina. **La excepción vigente es
`11-ARQ:3925`**, en la lista normativa del validador semántico del diario:

> `11-ARQ:3925` · «· TERMINALIDAD: exactamente un `derivada` por transacción cerrada, y
> ninguno en las abiertas»

Una transacción cerrada por `abandonada` **tiene cero `derivada`**. Esa regla la declararía
defectuosa. Contradice la tabla de cardinalidad de §2.6.4 (L1000–1002) y el bullet de
L3948–3952 —tres líneas más abajo, en la misma lista— que dice lo correcto. Es un hallazgo
nuevo, `G-3`, y vive en la capa que `D71` designa como evaluadora del predicado (L616–619).

**El censo de siete sedes, verificado por mí.** El documento afirma (L621–624):

> «DÓNDE SE CITA §2.5 (marcador) · §2.6.4 (clasificación) · §2.6.6 (garantías y regla de
> commit) · §2.6.8 (regla de lectura) · §2.6.9 (`conflicto`) · §2.9 (reconstrucción del
> marcador) · §7.4 (paso 2 de `Continúa`). **Las siete REMITEN aquí. Ninguna lo redeclara.**»

`grep -n 'abierta(tx)'` sobre el fichero devuelve, fuera de §2.6.1, **exactamente siete
citas**:

```text
L496   §2.5     tabla de plegado del manifiesto            ✔ nombrada
L1061  §2.6.5   W8                                         ✘ NO nombrada en el censo
L1220  §2.6.6   integridad post-terminal                   ✔ nombrada
L1501  §2.6.8   «el diario es la fuente de reconstrucción» ✔ nombrada
L2313  §2.6.11  la distinción conflicto/deriva             ✘ NO nombrada en el censo
L2647  §2.9     tabla de reconstrucción                    ✔ nombrada
L5253  §7.4     paso 2 de `Continúa`                       ✔ nombrada
```

**La cifra es correcta: son SIETE. El censo no lo es.** Nombra dos secciones que no citan el
predicado —**§2.6.4 y §2.6.9**, verificado con barrido acotado a L831–1038 y L1532–2007,
ninguna de las dos contiene la cadena— y omite las dos que sí lo citan, §2.6.5 y §2.6.11.

**Y §2.6.4 no sólo no remite: redeclara**, con la formulación retirada:

> `11-ARQ:894` · «1  ¿EXISTE UNA TRANSACCIÓN ABIERTA —`preparada` durable y SIN `derivada`—
> QUE DECLARE ESA RUTA, EN ESTA INSTALACIÓN?»

Es **byte a byte idéntica al texto base** (`11-base.md:819`), que es precisamente una de las
sedes que el gate enumeró en su `A2` (documento 16, L209: «**L819** (§2.6.4 paso 1)»).

**Lo que refuta la gravedad de mi propio hallazgo, y lo declaro por delante:** el paso 0 de
§2.6.4 (L883–892) comprueba «¿tiene un terminal durable —`derivada` **o** `abandonada`—?»
**antes** de que se llegue al paso 1, y descarta explícitamente las dos ramas. Con esa
guarda, el paso 1 sólo se evalúa sobre transacciones sin terminal, donde «sin `derivada`» y
«sin ninguno de los dos» son equivalentes. **La función de clasificación es correcta.** El
propio REVISOR A lo dijo en el documento 16 L218 y por eso su requisito 1.2 no exigió tocar
L819. Lo que falla es la **declaración de cierre** —«las siete REMITEN aquí, ninguna lo
redeclara»— y el censo, no el comportamiento.

**Veredicto del punto 1.** El defecto BLOQUEANTE de `A2` está **cerrado**: las tres sedes que
resucitaban el marcador y bloqueaban el commit global —§2.5, `W8` y §2.9— y §7.4 están
corregidas y remiten al predicado. Quedan **dos residuos**: el censo de L621–624 es
incorrecto en dos de sus siete entradas y su afirmación «ninguna lo redeclara» es falsa
(`M-1`); y sobrevive una regla vigente que trata `derivada` como único terminal, en el
validador del diario (`G-3`).

### 5.2 · `D72` — `deriva`, y el marcador de `D78`

**El enum, y su sede única.** §3.6 L3806 declara `causa` **enum cerrado de tres valores** y
se autodeclara «ÉSTA ES SU ÚNICA SEDE». §2.6.11 L2331–2333 lo confirma desde el otro lado:
«EL ENUM LO DECLARA §3.6, Y ES SU ÚNICA SEDE. Son TRES valores. Lo que sigue es su GLOSA
—qué significa cada uno—, no una segunda declaración: si alguna vez difieren, manda §3.6».
**CORRECTO**, y es exactamente lo que `A1` exigía.

**Campos obligatorios por causa, y `tx_afectada`.** §3.6 L3806: `tx_afectada` **obligatorio**
con `posterior-al-cierre` y `abandono-de-transaccion`, **prohibido** con `sin-transaccion`.
Coherente en las otras dos sedes que lo gobiernan: combinaciones prohibidas L3768–3769 («el
enum de tres valores y su condicional viven en §3.6») y la capa A del validador (L3878–3883,
que lo enuncia con los tres valores y la condicional correcta). **Las tres sedes dicen lo
mismo.** El defecto BLOQUEANTE de `A1` —que el esquema derivado literalmente de §3.6
rechazaba el `deriva` que hace emitible `abandonada`— está **cerrado**.

**`deriva` posterior al cierre.** `W12b` (L1066), paso 0 de §2.6.4 (L885–888) y §2.6.6
(L1236–1240) coinciden: `derivada` durable → `deriva` con `causa: posterior-al-cierre`, que
referencia sin reabrir. `X56` (L1370) lo comprueba. **CORRECTO.**

**`deriva` por abandono.** L2341–2346 lo declara y L1720 lo emite dentro del paso E. La
fila `abandonada` de §3.6 (L3804) hace `deriva_emitida` **obligatorio**, y la capa B del
validador comprueba que ese `deriva` exista y nombre las mismas rutas (L3941–3943). `X55`
(L1369) lo comprueba. **CORRECTO y cerrado en las tres capas.**

**`deriva` sin transacción.** Paso 1 de §2.6.4 (L899), §2.6.6 (L1203–1209, L1274–1276),
`X51` (L1365). **CORRECTO.**

**La reparación y `resuelve_deriva`.** §2.6.11 L2386–2396 y §2.6.9 L1796–1800: transacción
NUEVA, `tx` nuevo, `preparada` propia con `hash_previo` = lo observado, y `derivada` con
`resuelve_deriva` = el `id` del `deriva`. §3.6 L3805 lo declara campo de `derivada`.
`X50` (L1364) lo comprueba. **CORRECTO.**

**El predicado `bloqueado_por_deriva`.** L1792–1794, con forma explícita de terminar, y
consumido por la segunda rama de `reconciliacion_pendiente` (L1619). **CORRECTO**, y es la
diferencia real con el estado agotado que `D64` retiró.

**El marcador de `D78`, contra las seis propiedades exigidas.** `estado/deriva/<ID>.abierta`
aparece **una sola vez en todo el documento**, en §2.6.8 L1488–1497.

| propiedad | ¿se cumple? | prueba |
|---|---|---|
| **derivado** | **sí** | L1494–1495: «No gana identidad propia: es RECONSTRUIBLE desde el diario por el mismo predicado» |
| **determinista** | **sí, por construcción** | se deriva de `bloqueado_por_deriva(item)` (L1792–1794), que es una función total sobre el diario |
| **regenerable** | **declarado, y sin sede** | L1494 lo afirma, pero **§2.9 no tiene fila de reconstrucción para él** (tabla L2642–2651: hay fila para `estado/tx/<TX>.abierta` y ninguna para éste), pese a que L618–619 fija que «§2.9 declara desde dónde» |
| **no editable** | **no declarado** | ni §2.6.8 ni ninguna otra sede lo dice, y §1.3 no le da fila: la regla 1 de §1.3 («una fila con autoridad NADIE es derivada, y editarla no es una escritura canónica») **no le alcanza porque no tiene fila** |
| **no es una segunda fuente de verdad** | **sí en la intención, no en el mecanismo** | ver abajo |
| **coherente con el diario** | **parcialmente** | «se crea en el mismo instante que el evento» (L1490), pero el procedimiento E de §2.6.9 (L1718–1722), que enumera el cierre «sólo entonces, y en este orden», **no lo crea** |

**Contra §2.4, contra `I5` y contra §1.3, punto por punto:**

```text
CONTRA §2.4   §2.4 declara «DURABLE Y VERSIONADO: `estado/` SALVO la excepción de ruta
              declarada abajo», y esa excepción nombra EXCLUSIVAMENTE «los marcadores de
              transacción de `estado/tx/`» (L417–418). `estado/deriva/` NO está en ella.
              L1496 afirma que vive «fuera de Git por la excepción de ruta de §2.4» —y esa
              excepción, tal como está escrita, no lo cubre.

CONTRA GIT    `.gitignore` se declara en positivo DOS veces, y las dos sólo para
              `estado/tx/`: L445 («excluye `estado/tx/`») y L1316 («NADA de `estado/tx/`.
              Declarado en positivo»). `X27` (L1356) comprueba «ningún commit contiene un
              fichero bajo `estado/tx/`» — y nada comprueba `estado/deriva/`.

CONTRA §2.3   el árbol de la disposición (L373–408) no lista `estado/deriva/`.

CONTRA §1.3   la matriz de fuentes de verdad (L209–232) no tiene fila para él. Tampoco la
              tiene para `estado/tx/`, y ahí no importa porque §2.4 lo clasifica; aquí
              nada lo clasifica.

CONTRA `I5`   por el criterio VIGENTE de §2.4 —todo `estado/` es durable y versionado salvo
              lo exceptuado— este marcador **viaja a Git**. Y entonces un clon nuevo lo
              recibe y, por el paso 2bis de §2.6.8, declara NO FIABLES las rutas que
              nombra, sin ningún mecanismo que le diga si sigue vigente. Es exactamente la
              patología que la garantía 6 de §2.6.6 (L1113–1121) prohíbe para el otro
              marcador —«el marcador NUNCA es fuente para un clon»— y para la que allí sí
              existe un ramal (`fallo` de publicación) que aquí no existe.
```

**¿Es una segunda verdad editable?** **En la intención declarada, no**: es un caché derivado
del mismo predicado. **En el mecanismo publicado, se comporta como una si acaba versionado**,
porque nada lo excluye de Git, nada lo regenera con sede declarada, nada prohíbe editarlo y
ninguna prueba lo cubre. La diferencia con el marcador de transacción es que aquél tiene las
cinco piezas —clasificación, excepción de ruta, `.gitignore`, fila de reconstrucción en §2.9
y `X27`— y éste no tiene ninguna. **Lo digo como es: no es una segunda verdad por diseño; lo
es por omisión, y la omisión es reparable con cinco líneas.** Es el hallazgo `G-2`.

**Y hay un segundo residuo en la misma sección.** La condición de cierre de `A8` era «un
artefacto derivado equivalente para los `deriva` sin reparar, legible sin herramienta **y
sujeto a la misma disciplina que el marcador**». `D78` añadió el artefacto, pero **la regla
que el lector ejecuta no cambió**: §2.6.8 L1451–1452 y L1456 son **byte a byte idénticas al
texto base** (`11-base.md:1375-1376, 1380`) y siguen diciendo «se comprueban DOS cosas: los
marcadores de `estado/tx/` y **los eventos `deriva` SIN REPARAR del diario**». El coste que
`A8` denunció —recorrer `estado/eventos/` entero, el coste con que §2.2 descarta la
alternativa C— sigue impuesto por la regla normativa. La explicación de por qué existe el
marcador se añadió; la regla que lo haría innecesario, no.

### 5.3 · `D73` y `D69` — completar o revertir

**Reversión especulativa.** §2.6.0 (L519–537) separa estable de especulativo con precisión, y
declara que el conjunto parcial «NO es verdad publicada», «no puede entrar en ningún commit
ordinario» y que revertirlo «es local y no destruye trabajo de nadie: nadie los ha visto
nunca». **CORRECTO, y es una corrección sustantiva bien hecha.**

**Estado publicado.** L1749–1758: se retira «roll-forward only» **como absoluto**; lo
publicado nunca se revierte automáticamente (decisión del Owner + transacción de reparación);
lo especulativo sí. La prohibición de §2.6.6 «sigue entera y no la toca `D69`» (L1708–1709).
**CORRECTO.**

**`b.14`.** §7.4 (L5230–5271) está **reescrito**: el paso 2 tiene las dos ramas, usa el
predicado `abierta(tx)` con su remisión a §2.6.1, y la rama MARCAR declara sus dos salidas
—`confirmada` y `abandonada`, ésta «que RESTAURA lo especulativo local a `revision_base` y lo
verifica byte a byte antes de emitirse»—, cerrando con «**Ninguna de las dos cierra dejando
una mezcla parcial publicable**». El resumen de §16 (L7546–7548) está alineado con el cuerpo
de `PN-7` (L7331–7358). La formulación retirada —«§2.6 elimina el ramal de reversión por
completo»— **no aparece en ninguna sede vigente**: la busqué. **CORRECTO. `A3` cerrado.**

**Restauración byte a byte.** Paso D de §2.6.9 (L1711–1716): comparación byte a byte contra
`revision_base`, comprobación de rutas huérfanas, comprobación de que el conjunto vuelve a
ser el de la base **entero**, y «si una escritura concurrente impide verificarlo,
`abandonada` NO puede emitirse». **CORRECTO.**

**Copia de lo divergente.** Paso A (L1691–1696): se conserva **antes** de tocar nada, y «si no
puede conservarse, NO SE PUEDE ABANDONAR». La copia íntegra vive en el cuerpo del `conflicto`
(§3.6 L3803, campo obligatorio). **CORRECTO.**

**Commit de incidente.** L1725–1741: lleva base restaurada + `preparada` + `conflicto` con
evidencia + `abandonada` con su verificación + `deriva`. **CORRECTO.**

**Ninguna mezcla parcial publicable.** L1785–1786: los desenlaces 1 y 2 la convierten en
estable, el 3 la restaura a la base, el 4 no publica. **CORRECTO en §2.6.9.** Ver la reserva
en el punto 6 y en el hallazgo `M-3`.

**Intención histórica.** Es el punto donde el encargo me pidió mirar con más cuidado, y las
**tres** comprobaciones salen bien:

> `11-ARQ:1735-1741` · «NO LLEVA **ningún FICHERO CANÓNICO en su `hash_posterior_esperado`**.
> Ni uno: todos han vuelto a la base, y por eso el conjunto publicable es la BASE CONSISTENTE
> MÁS EL INCIDENTE, nunca la mezcla parcial. **El evento `preparada` SÍ conserva los suyos**,
> y debe conservarlos: es historia, está en `estado/eventos/`, y sin él no se sabría a qué
> resultado se iba ni desde qué base. Confundir «ningún fichero está en su hash posterior»
> con «ningún hash posterior se conserva» borraría la intención que hace auditable el
> abandono.»

```text
1 · ¿`preparada` CONSERVA su `hash_posterior_esperado`?
    SÍ. L1738-1739 lo dice expresamente, y §3.6 L3801 lo mantiene entre los campos
    OBLIGATORIOS de `preparada`. Las dos sedes son compatibles.

2 · ¿LOS CANÓNICOS RESTAURADOS CASAN CON `hash_previo` / la revisión base?
    SÍ. Paso C (L1703-1709) restaura desde `revision_base` EXACTA, incluidos los que ya
    habían alcanzado su hash posterior; paso D verifica byte a byte; y el commit lleva «el
    estado canónico RESTAURADO A LA BASE — idéntico, byte a byte, al del commit anterior en
    todas las rutas de la transacción» (L1728-1729). La condición 7 de arranque (L555-557)
    ya exigía comprobar que las N rutas existen en `revision_base` con el hash declarado,
    «sin esto, `abandonada` sería inalcanzable».

3 · ¿SE INTERPRETÓ «NO PUBLICAR ESTADO POSTERIOR PARCIAL» COMO BORRAR LOS HASHES DEL EVENTO?
    NO. Es exactamente la confusión que L1740-1741 nombra y prohíbe. Y el sujeto está
    corregido: la afirmación es sobre FICHEROS CANÓNICOS, no sobre CAMPOS DEL EVENTO.
    `A5` está cerrado en su literalidad, y sin efecto colateral sobre §2.3 («los eventos SE
    EMITEN, NO SE EDITAN», L392-393) ni sobre la identidad de §2.8.
```

### 5.4 · Git del repositorio de control

| materia | dónde | veredicto |
|---|---|---|
| rama canónica `main` | L2155–2158 | **declarada**, con su significado distinto del de una source: «estado emitido por el ejecutor único» |
| intención publicada previa | L2231–2262, y condición 4 de arranque L549–551 | **declarada**, con sus siete contenidos y la comprobación de que esté en el último estado aceptado |
| worktree limpio | condición 1 de arranque, L543–545 | **declarada**, con su motivo: un worktree sucio hace indistinguible lo especulativo de lo ajeno |
| único escritor por clon | L1826–1829 | **declarado y ACOTADO**: «UN ÚNICO EJECUTOR DE MUTACIÓN por clon/worktree (`R5`)», y el paralelismo por varios worktrees es «capacidad futura, no garantía actual» |
| CAS | L2204–2207, L2165–2168, L1832–1835 | **declarado** como compare-and-swap sobre revisión, con contador propio que no es el de `a.9` ni el de §2.6.9 |
| rechazo non-fast-forward | L2209–2212 | **declarado**, con evento `fallo`, tope de tres por §7.3 y escalado |
| push | L2042–2045, L2145 | **NO automático**. «Nadie automáticamente»; ninguna política autoriza publicar una recuperación |
| autoridad | L2187–2190 | **el Owner por defecto**, y ADS nunca publica una recuperación por su cuenta |
| recuperación local | §2.6.9 garantía A, L1896–1899 | **exacta**, y la única fuerte para lo abierto |
| reinicio remoto | garantía C, L1908–1917 | **REINICIO SEGURO, no reanudación**, «y no se llama de otra manera» |
| incidentes | L1725–1741, garantía B L1901–1906 | **el incidente entero viaja**, y otra máquina puede iniciar la reparación |
| limitación distribuida declarada | L1920–1931 | **declarada sin disimulo**: se sacrifica la reanudación exacta distribuida, «se paga a sabiendas» y «no se presenta como capacidad de PesquerApp hasta que exista» |
| `PN-11` | L7425–7458 | **registrado**, con qué presiona, qué falta, sede resuelta por `O16`, materia mínima, qué bloquea y condición de reversión |
| `O16` | L7167–7170, `DECISIONES` §2 | **citada** como resolución posterior del Owner que da sede a `PN-11` |
| futuro `C8` | L7443–7448 | **declarado**: derivado de `(g)`, gobierna únicamente el control repo, «`C7` permanece limitado a las sources», y «`C8` no copia la tabla de `C7`» |
| **`C7` intacto** | verificado con `git diff` sobre el rango: **vacío** | **CORRECTO.** Y §2.6.10 L2298 lo declara: «`C7` no se toca en esta pasada». Comprobé además que `C7:170` conserva literalmente `aplica_a: "todo item cuyos paquetes escribieron en una o más fuentes"`, luego la denuncia de §9.5 sigue siendo exacta y la abstención de tocarlo es coherente |

**`D84` — el argumento nuevo, examinado por su corrección y no por su procedencia.**

> `11-ARQ:2160-2170` · «PROTECCIÓN DE LA RAMA — **NO se le aplica `G29`** … Lo que SÍ la
> protege es otra cosa: **el CAS de Git**, que serializa `main` entre máquinas sin acuerdo
> previo —y NO «un único escritor», que es una regla LOCAL por worktree (`R5`) y no dice nada
> de dos máquinas empujando a la vez (`A12`; es `D84`)—, **commits sólo entre transacciones**
> (§2.6.6) y **push bajo autoridad**.»

**El argumento nuevo es correcto**, y lo digo tras comprobarlo por sus dos mitades:

```text
LA MITAD POSITIVA ES CIERTA    una actualización de referencia en Git sólo se acepta si
                               avanza desde la revisión que el remoto tiene, y un `push`
                               non-fast-forward se rechaza. Eso ES un compare-and-swap sobre
                               la referencia, y ES una propiedad ENTRE MÁQUINAS: no depende
                               de ningún acuerdo previo entre ellas. §2.6.10 L2204-2212 lo
                               ejerce correctamente —`fetch`, comprobación de fast-forward
                               sobre la revisión conocida, y `fallo` con las dos revisiones
                               nombradas si el remoto avanzó.

LA MITAD NEGATIVA TAMBIÉN      `R5` se implementa con `.ads/run/lock`, que §2.7 L2409-2412
                               declara operacional a propósito porque «un lock versionado en
                               Git sería un lock que viaja a otra máquina», y §2.7 L2442-2443
                               dice que «`R5` es un requisito del runtime local, no del
                               producto». Un lock que no viaja no puede serializar dos
                               máquinas. La premisa retirada era, en efecto, falsa para el
                               sujeto al que se aplicaba.

LO QUE EL CAS NO DA, Y ESTÁ    el CAS serializa la PUBLICACIÓN; no impide que dos máquinas
DICHO EN OTRA PARTE            trabajen a la vez ni resuelve la bifurcación de la cadena
                               `predecesor`. Eso está declarado —§2.7 L2456-2459, §2.11
                               L2981-2987, §2.6.10 regla 5 L2060-2066— como runtime
                               distribuido abierto, con el comportamiento seguro entretanto:
                               la segunda máquina no publica y escala. El argumento no
                               promete más de lo que el CAS da.
```

**Y la conclusión no se apoya ya en la premisa retirada en ninguna otra sede vigente.**
`grep -n 'único escritor'` sobre el documento 11 devuelve **una sola línea, L2166**, que es
la que la retira. La única aparición restante en el corpus es
`DECISIONES-Y-CONTRADICCIONES.md:234`, en el registro de `D65` — y `D84` (L266 del mismo
fichero) declara expresamente que revisa «**`D65`** en su lista de protecciones». Ese
registro es texto histórico bajo la disciplina declarada «`D16`–`D70` no se reescriben»
(L233 y L7139 del documento 11). **Lo distingo: es mención histórica marcada, no sede
vigente.** `A12` está cerrado.

### 5.5 · Estados y esquemas — derivado, no copiado

Todo lo de esta sección está en la tabla del §4. Lo derivé recorriendo las tablas, no leyendo
los titulares. Resumen de lo que comprobé y no está allí:

**Tipos.** Nueve valores de `tipo`, partidos en tres regímenes que suman nueve sin solape:
cinco siempre transaccionales, uno condicional (`orden`), tres nunca (`sellado`, `deriva`,
`fallo`). La demostración es **tipo a tipo** en la tabla L3502–3512, no un cartesiano
postulado, y los cuatro casos que la prueba obligó a separar (L3516–3575) están argumentados
uno a uno. La frontera que exige `tx` es un solo criterio —más de un fichero, **o** sustituye
contenido previo— aplicado por igual a las cinco cosas que ADS escribe bajo `estado/`
(L3613–3619). `sellado` y `retirada-de-cuerpo` acaban en lados distintos por la única razón
que los separa. **CORRECTO y verificable.**

**Combinaciones válidas y prohibidas.** 34 y 20, verificadas por mí (§4, filas 9 y 10), con
la partición cerrando sobre 54. Y cada prohibición tiene **capa asignada** (L3755–3775):
esquema estructural para lo que es coherencia interna del evento, validador semántico del
diario para lo que exige recorrer el `tx`. **CORRECTO.**

**El contrato de `fallo`.** Semántica cerrada: `operacion` es enum cerrado de cinco valores,
`tx_afectada` es REFERENCIA y no pertenencia, `recuperable` ∈ {`si`,`no`,`requiere-decision`},
`autoridad_requerida` y `accion_siguiente` obligatorios, `referencias[]` con commit/rama/
remoto cuando la operación es Git (L3807, L3818–3851). Con eso `X15` y `X28` **sí son
satisfacibles** contra el contrato, que era el defecto de `G3`/`D66`. **CORRECTO.**

**Identidad de eventos.** `id = EV-H(evento MENOS id)`, `tx = TX-H(cuerpo de preparada MENOS
id, tx, predecesor)`, representación canónica normativa e independiente del formato de
presentación, lista cerrada de campos incluidos y excluidos, y `identidad_v: N` para
versionar el algoritmo (L2493–2553). La consecuencia incómoda está dicha sin rodeos:
«REEMITIR NO ES IDEMPOTENTE POR `id`», y la idempotencia vive sobre `tx` con la regla de
reintento. **CORRECTO.**

**Sellado y lápidas.** Tres niveles de garantía separados —continuidad estructural,
consistencia del compromiso, verificación completa—, con lo que cada uno **no** da dicho
expresamente; fuente de recuperación comprobada **antes** de retirar, con sus cuatro
condiciones; excepción tipada al algoritmo de identidad; y el reconocimiento de que «el
diario FÍSICO no es estrictamente append-only» (L2810–2814). La distinción entre referencia
estructural y dependencia semántica viva es lo que hace la operación alcanzable. **CORRECTO
y bien hecho.**

**`cobertura`.** Sujeto como referencia tipada `(clase, ancla, ruta)`; `aspecto` con tres
namespaces de contrato distinto; `responsables` sólo como desviación —el reparto por defecto
vive en el `contrato-de-aspecto`, una sola sede—; `evaluacion_de_pruebas` prueba a prueba;
`verificacion` partida en `auditor` y `verificador_de_correccion`. Las tres celdas de §5.6
caben en el contrato sin campos de conveniencia. **CORRECTO.**

**`iniciativa`.** Estado **no** es campo: función total con precedencia `Q0`–`Q9`, cuyo
dominio es el estado global de sus items ya calculado por `b.4`. Verifiqué la totalidad
recorriendo los diez estados globales contra las diez cláusulas (L3156–3161) y los ocho casos
frontera (L3165–3174): **no encontré ninguna combinación sin resultado ni ninguna que
produzca dos**. Los dos predicados de obligación están definidos a nivel de iniciativa
(L3082–3096), y por eso `Q9` es computable. **CORRECTO.**

**Y una comprobación que hice porque el encargo la sugiere:** §3.8 declara 25 y son 25,
pero además **el `evento` cuyo esquema no existe está dentro de esos 25 como tipo nuevo**, no
como esquema vigente. `19 + 4 + 2` no cuenta dos veces nada. La cuenta es consistente con que
`evento.yaml` no exista todavía.

### 5.6 · Proporcionalidad — seis piezas, seis funciones

| pieza | qué pregunta responde | ¿editable? | ¿fuente de verdad? | sede |
|---|---|---|---|---|
| **DIARIO** `estado/eventos/` | ¿qué pasó, quién lo ordenó, sobre qué base, quién lo aplicó? | **no**: se emite, con UNA excepción física tipada (la lápida) | **sí**, del CAMBIO | §1.3 L221, §2.5 L465–467 |
| **MARCADOR** `estado/tx/` | ¿hay algo en vuelo, y sobre qué rutas? | derivado, reconstruible | **no**: «un acelerador, no una verdad» | §2.9 L2647 |
| **INTENCIÓN PUBLICADA** | ¿qué trabajo debe hacerse, sobre qué base, con qué autoridad? | canónica, previa y **publicada** | **sí**, de la ORDEN | §2.6.10 L2231–2262 |
| **GIT** | ¿dónde sobrevive esto y cómo se mueve entre máquinas? | historia inmutable | **no**: «DERIVADO … Git NO decide qué se recupera ni cómo: sólo dónde sobrevive» | §2.6.10 L2129–2136 |
| **VISTAS** tableros, dosieres, índices | ¿cómo se lee esto sin cómputo? | derivadas, regenerables | **no**: autoridad «nadie» en §1.3 | §1.3 L230–232 |
| **INCIDENTE** | ¿qué salió mal, con qué evidencia, y quién lo desbloquea? | eventos `fallo` y `deriva` | **no**: reportan, no reparan | §2.6.11 L2355–2372, §3.6 L3846–3851 |

**Las seis funciones son distintas, y lo comprobé por la vía dura: buscando la misma verdad
escrita dos veces.** No la encontré entre estas seis. La regla que las separa está enunciada
y es correcta: «la recuperación es del DIARIO; la publicación es de GIT. No hay dos
mecanismos para el mismo estado de recuperación» (L2129–2131). La intención publicada es lo
único que se solapa con el diario en apariencia, y §2.6.10 L2253–2257 corta el solape con
precisión: «publicar la INTENCIÓN no es publicar la TRANSACCIÓN ABIERTA». **Esto está bien, y
lo digo.**

**Dos reservas, y son mías:**

```text
1  EL MARCADOR DE `D78` es la séptima pieza, y es la única que NO tiene su función separada
   por escrito: no está en §1.3, no está en §2.3, no está clasificada por §2.4 y no tiene
   fila en §2.9. Por el criterio vigente acabaría VERSIONADA, y un caché versionado que
   nadie regenera ES una segunda verdad. Es `G-2`, y es un defecto de `I5` por omisión.

2  `estado/cuarentena/<TX>/` es la OCTAVA, y la introduce esta misma tanda. Es peor que la
   anterior: no sólo carece de plano y de fila, sino que §2.6.10 L2103 la descarta
   expresamente como alternativa **porque «crea una tercera ubicación con su ciclo y su
   plano, que §2.4 no tiene»**. Es `G-1`.
```

---

## 6 · Mis filas de la matriz

Para cada una: causa original, texto anterior (`git show 7e99388:…`), corrección vigente,
decisión aplicable, sede actual, condición de cierre declarada en el checkpoint, y si se
cumple de verdad.

---

**`A1` · BLOQUEANTE · el contrato de `evento` no podía representar el `deriva` que hace
emitible `abandonada` — SUPERADA**

*Causa* (doc 16, L176–195): §3.6 declaraba dos valores de `causa` y prohibía `tx_afectada`
fuera de `posterior-al-cierre`, mientras §2.6.11 declaraba tres y `abandonada` exigía
`deriva_emitida`. Dos sedes editables para el mismo enum.
*Texto anterior*: `11-base.md` L3659 y L3622.
*Decisión*: `D72`. *Sede*: §3.6 L3806, con §2.6.11 L2331–2333 declarándose GLOSA.
*Condición declarada*: «enum de TRES valores con UNA sede, §3.6; §2.6.11 remite».
*¿Se cumple?* **SÍ.** Verifiqué las **tres** sedes que gobiernan el enum —contrato L3806,
combinaciones prohibidas L3768–3769, capa A del validador L3878–3883— y las tres dicen lo
mismo, con la condicional correcta en las tres. §2.6.11 declara su subordinación con la
regla de desempate escrita. **SUPERADA.**

---

**`A2` · BLOQUEANTE · el predicado de «transacción abierta» seguía siendo «sin `derivada`» —
SUPERADA, con reserva sobre su condición declarada**

*Causa* (doc 16, L199–220): siete sedes decidían si una transacción sigue abierta y ninguna
citaba a otra; una `abandonada` satisfacía «sin `derivada`», luego §2.9 resucitaba el
marcador que `abandonada` acababa de retirar y, por la regla de commit, **el control repo
dejaba de commitear para todo el producto, indefinidamente**.
*Texto anterior*: `11-base.md` L449, L986, L1144, L1405, L2185, L2514, L5018.
*Decisión*: `D71`. *Sede*: §2.6.1 L599–625.
*Condición declarada*: «predicado `abierta(tx)` en §2.6.1; las siete sedes remiten».

*¿Se cumple?* **La sustancia, SÍ.** El requisito 1.2 del gate pedía tres cosas concretas y
las tres están hechas: predicado único y nombrado (L611–612); «único terminal» retirado de
L449 → L496, L986 → L1061 y L2514 → L2647; y §7.4 L5018 corregido → L5253. Las siete sedes
operativas remiten al predicado. **El modo de fallo bloqueante está cerrado en su raíz**, y
`W8` lo dice ahora expresamente: «el marcador se retira por igual tras `derivada` y tras
`abandonada`». **SUPERADA.**

*Reserva, declarada:* la condición tal como el propio documento la escribe —«Las siete
REMITEN aquí. **Ninguna lo redeclara**» (L621–624)— **es literalmente falsa**: §2.6.4 L894
redeclara con la formulación retirada, y el censo nombra dos secciones que no citan el
predicado y omite dos que sí. No lo convierto en FALLIDA porque el paso 0 de §2.6.4 hace
inocua esa redeclaración y el gate lo sabía (doc 16 L218). Lo registro como `M-1`.

---

**`A3` · GRAVE · §7.4 declaraba en voz normativa un diseño que `D69` retiró — SUPERADA**

*Causa* (doc 16, L228–246): «§2.6 elimina el ramal de reversión por completo» sobrevivía en
§7.4 y en el resumen de §16, contra §2.6.9 y contra el propio `PN-7` reformulado.
*Texto anterior*: `11-base.md` L5008–5013 y L6876.
*Decisión*: `D73`. *Sede*: §7.4 L5230–5271 y §16 L7546–7548.
*Condición declarada*: «§7.4 paso 2 con las dos ramas; resumen de §16 alineado con `PN-7`».
*¿Se cumple?* **SÍ.** Paso 2 reescrito con las dos ramas y el predicado de `D71`; la rama
MARCAR declara sus dos salidas con la restauración verificada; §16 L7546–7548 dice lo mismo
que el cuerpo de `PN-7` (L7331–7358). Busqué la formulación retirada en todo el fichero y
**no aparece en ninguna sede vigente**. **SUPERADA.**

---

**`A5` · MEDIO · el commit del incidente se declaraba a la vez con y sin los hashes
esperados — SUPERADA**

*Causa* (doc 16, L275–295): «NO LLEVA ningún `hash_posterior_esperado`. Ni uno» chocaba con
que ese campo es obligatorio dentro de `preparada`, y leído literalmente obligaba a despojar
el evento de sus hashes antes de commitear.
*Texto anterior*: `11-base.md` L1639.
*Decisión*: §2.6.9. *Sede*: L1735–1741.
*Condición declarada*: «sujeto corregido: ningún FICHERO en su hash posterior; el evento sí
lo conserva».
*¿Se cumple?* **SÍ, y de forma completa.** El sujeto está corregido, el evento conserva sus
hashes con su motivo escrito, y la confusión se nombra y se prohíbe expresamente. Comprobé
además que no queda efecto colateral: §2.3 L392–393 mantiene «SE EMITEN, NO SE EDITAN» con
su única excepción, y la identidad de §2.8 sigue siendo reproducible. **SUPERADA.**

---

**`A6` · MEDIO · tres sedes declaraban seis fases y ocho filas donde el recuento da cinco y
siete — SUPERADA**

*Causa* (doc 16, L303–317): el título de §2.6.1 mentía en sus dos mitades y el preámbulo del
contrato condicional describía mal la tabla que introduce.
*Texto anterior*: `11-base.md` L513, L3327–3328, L3637–3640.
*Decisión*: `D85`. *Sede*: L560 («cinco fases, dos rutas, dos cierres»), L3465–3474,
L3784–3789.
*Condición declarada*: «5 fases · 6 estados · 7 filas, recalculados tras `D64`».
*¿Se cumple?* **SÍ.** Los tres números los derivé yo (§4, filas 1, 5 y 6) y coinciden. El
título de §2.6.1 dice ahora «cinco fases, dos rutas, **dos cierres**», que es correcto en sus
dos mitades. Barrí «seis fases» sobre el fichero y sólo aparece en notas de corrección
marcadas como históricas. **SUPERADA.**

---

**`A7` · MEDIO · `D66` corrigió los cinco conceptos en §3.6 y no en §2.6.10 — FALLIDA**

*Causa* (doc 16, L321–333): la tercera revisión nombró **«`X39` y la regla 1 de §2.6.10»**
como los dos sitios que convierten la cita falsa en condición de validación. «Uno se
corrigió; el otro no.»
*Texto anterior*: `11-base.md:1916-1918`.
*Corrección vigente*: **NINGUNA.** El texto es **byte a byte idéntico**:

> `11-ARQ:2038-2040` · «1  EL COMMIT LOCAL SE HACE, y emite su evento con los **CINCO
> conceptos de `a.9`**: ordenante · autoridad · escritor_del_comando · ejecutor ·
> **actor_atribuido**. La ausencia de cualquiera de los cinco es un FALLO DEL VALIDADOR, no
> un silencio.»

Contra la fuente aprobada, verificada por mí literal:

> `docs/rediseno/a-CAPACIDADES-APROBADA.md:671-679` · «Cinco conceptos que **NO DEBEN**
> confundirse … PROPIETARIO DEL CAMPO · AUTORIDAD · ORDENANTE · ESCRITOR DEL COMANDO ·
> EJECUTOR DE MUTACIÓN»
>
> `…:665` · «ACTOR ATRIBUIDO       Owner              a quién se imputa el cambio» — **otra
> lista**

*Sede*: §2.6.10 regla 1, L2038–2040.
*Condición declarada en el checkpoint*: «`A7` · `CORREGIDO_EN_F4` · §3.6 · «los cinco CAMPOS
de procedencia» **donde es condición de validación**».
*¿Se cumple?* **NO.** L2040 dice «La ausencia de cualquiera de los cinco es un FALLO DEL
VALIDADOR»: **es** una condición de validación, en el sentido literal de la condición de
cierre declarada. Y el documento demuestra que sabe cómo se escribe bien, porque lo escribió
en las otras cuatro sedes: `X39` (L1360), §2.6.6 (L1214–1215), §2.9 punto 9 (L2915–2916) y la
fila `preparada` de §3.6 (L3801) dicen todas «los cinco **CAMPOS** de procedencia de §3.6 —
no «los cinco conceptos de `a.9`», que incluyen uno derivado». **La única sede que el gate
nombró es la única que no se tocó.** El checkpoint la declara `CORREGIDO_EN_F4`. **FALLIDA.**

---

**`A8` · MEDIO · la única justificación del marcador quedaba anulada por la regla 2bis —
FALLIDA**

*Causa* (doc 16, L337–349): el marcador existe para no reproyectar el diario, y la regla de
lectura de la misma sección obliga a hacer exactamente eso. «O un artefacto derivado
equivalente para los `deriva` sin reparar, legible sin herramienta **y sujeto a la misma
disciplina que el marcador**; o rehacer la justificación del marcador.»
*Texto anterior*: `11-base.md:1375-1376` (regla 1) y L1380 (paso 2bis).
*Corrección vigente*: `D78` añade `estado/deriva/<ID>.abierta` en §2.6.8 L1479–1497.
*Sede*: §2.6.8 L1488–1497, y una única aparición más en todo el corpus (registro `D78`).
*Condición declarada*: «`estado/deriva/<ID>.abierta`, legible sin herramienta».
*¿Se cumple?* **NO, por dos razones independientes.**

```text
1  LA REGLA QUE EL LECTOR EJECUTA NO CAMBIÓ. L1451-1452 y L1456 son BYTE A BYTE idénticas a
   `11-base.md:1375-1376, 1380`: siguen diciendo «se comprueban DOS cosas: los marcadores de
   `estado/tx/` y **los eventos `deriva` SIN REPARAR del diario**». El párrafo explicativo se
   añadió debajo; la NORMA sigue mandando recorrer el diario. Un lector que cumpla §2.6.8 al
   pie de la letra sigue pagando el coste con que §2.2 descarta la alternativa C.

2  EL ARTEFACTO NO ESTÁ «SUJETO A LA MISMA DISCIPLINA QUE EL MARCADOR», que es la mitad
   literal de la condición de cierre. El marcador de transacción tiene CINCO piezas; el de
   `deriva` no tiene NINGUNA:
     · clasificación de plano            §2.4 L433-440  ·  ninguna
     · excepción de ruta que lo nombre   §2.4 L417-418  ·  ninguna: nombra sólo `estado/tx/`
     · `.gitignore` declarado            L445, L1316    ·  ninguna
     · fila de reconstrucción en §2.9    L2647          ·  ninguna
     · fila adversarial (`X27`)          L1356          ·  ninguna
   Y §2.6.9 paso E (L1718-1722), que enumera el cierre «sólo entonces, y en este orden», NO
   lo crea, pese a que L1490 dice «se crea en el mismo instante que el evento».
```

**FALLIDA.** El detalle material y su consecuencia están en el hallazgo `G-2`.

---

**`A9` · MEDIO · el desenlace `4b` no tenía salida material garantizada, y `X58` exigía más
de lo que el análisis sostiene — SUPERADA**

*Causa* (doc 16, L353–365): ambas salidas de `conflicto` dependían de hechos fuera del
control del sistema, ninguna autoridad podía desempatar, y mientras `4b` durase el commit
quedaba bloqueado para todo el producto.
*Texto anterior*: `11-base.md` L1862–1866 y L1296.
*Decisión*: `D79`. *Sede*: §2.6.9 L1956–1976 y `X58` L1372.
*Condición declarada*: «dos actos de autoridad del Owner cierran `4b`; `X58` reformulado».
*¿Se cumple?* **SÍ.** Los dos actos están escritos, nombrados y atribuidos: cuarentena
autorizada, o declaración de irrecuperable con cierre por `abandonada` registrando el
`estado_observado[]` de todas las rutas y excluyendo las divergentes del commit. `X58` está
reformulado y dice ahora lo que el diseño sostiene: «la retención acotada del desenlace `4b`
termina por ACTO DE AUTORIDAD del Owner …, **no por construcción: el grafo no la cierra
sola**». Y L2002–2005 lo repite en el cierre de la sección. **SUPERADA en su condición
declarada** — pero la vía (i), la cuarentena, introduce el problema que registro como `G-1`,
que es un hallazgo nuevo y no una parte de `A9`.

---

**`A12` · MENOR · «un único escritor» se ofrecía como protección de una rama compartida —
SUPERADA**

*Causa* (doc 16, L402–411): el documento declaraba en §2.7 que el lock es local y no viaja, y
en §2.6.10 lo listaba entre las protecciones de una rama compartida.
*Texto anterior*: `11-base.md` L2041–2043 (y su gemela).
*Decisión*: `D84`. *Sede*: §2.6.10 L2160–2170.
*Condición declarada*: «el CAS de Git, no «un único escritor»».
*¿Se cumple?* **SÍ.** `grep -n 'único escritor'` sobre el documento 11 devuelve **una sola
línea, L2166**, que es la que lo retira nombrando el motivo. El argumento sustituto es
técnicamente correcto en sus dos mitades (§5.4 de este dictamen). No queda ninguna sede
vigente que apoye la conclusión en la premisa retirada. La única aparición restante en el
corpus es el registro de `D65`, texto histórico que `D84` declara revisado. **SUPERADA.**

---

**`A13` · MEDIO · la fila `preparada` de §3.6 etiquetaba su lista obligatoria como «los cinco
de `a.9`» — SUPERADA**

*Causa* (doc 16, L415–419): la etiqueta que `D66` acababa de declarar engañosa.
*Texto anterior*: `11-base.md:3654`, «los cinco de `a.9`».
*Decisión*: §3.6. *Sede*: L3801.
*Condición declarada*: «fila `preparada` de §3.6 con los cinco CAMPOS».
*¿Se cumple?* **SÍ**, y con exceso: la fila no sólo usa «los CINCO CAMPOS de procedencia»
sino que enumera los cinco y explica por qué el quinto concepto no es campo. **SUPERADA.**
*Nota:* el mismo remedio no se aplicó a §2.6.10 — ver `A7`.

---

**`M-8` · MEDIO · §19 y §2.9 contaban artefactos que `D64` retiró, y `R1`–`R9` colisionaba
con `R1`–`R8` — SUPERADA**

*Causa* (doc 16, L876–890): cuatro citas contando nueve ventanas retiradas, más la colisión
de espacio de nombres con los ocho requisitos de §2.1.
*Texto anterior*: `11-base.md` L2816 y L7060.
*Decisión*: `D83`. *Sede*: §2.1 L297–314, §2.6.5 L1043, §2.6.7 L1422, §2.6.9 L1536, §2.9
L2950–2952, §19 L7748–7752.
*Condición declarada*: «`RC-1`–`RC-9` renombradas y retiradas del inventario de §19».
*¿Se cumple?* **SÍ, en las dos mitades.** Barrí `RC-` sobre el fichero: **cinco apariciones,
todas como `RC-1`–`RC-9`, ninguna como `R1`–`R9`**. §2.9 L2950–2952 dice ahora «Las nueve
`RC-1`–`RC-9` **ya no existen** … contarlas entre lo escrito y no ejecutado era contar dos
veces algo que ya no está». §19 L7748–7752 dice «**Las nueve ventanas de reconciliación NO se
cuentan: `D64` las retiró**». Y §2.1 declara la prueba única del espacio de nombres.
**SUPERADA.**

---

**`F-03` · MEDIO · `N0`–`N7` introducido sobre un `N1`–`N14` vigente — SUPERADA**

*Causa* (doc 17, L1273–1279): `N5` significaba «una FUENTE es una ubicación física
versionada» en `C6`/`C5` y «la quinta fase de la instalación» en §8.1/§18, y `C5` L76 cita
`C6 N5` **a través de la frontera del contrato**.
*Texto anterior*: `11-base.md` L5090 y L6990, con `N0`–`N7`.
*Decisión*: `D83`. *Sede*: §2.1 L309–310, §8.1 L5489–5531, §18 L7672–7673.
*Condición declarada*: «fases de instalación renombradas a `INS-0`…`INS-7`».
*¿Se cumple?* **SÍ.** Barrí `` `N0` `` a `` `N7` `` sobre el documento 11: las **cinco**
apariciones restantes son todas citas de `C6` (`N4` y `N7` como principios normativos), que
es exactamente lo que `D83` declara intocado. Ninguna fase de instalación se nombra ya con
`N<n>`. Verifiqué que `C6` conserva sus `N1`–`N14` (L29–42) y que el rango **no toca `C6`**.
La elección de renombrar el espacio más nuevo, y no el contrato, es la correcta.
**SUPERADA.**

---

**`F-12` · MENOR · las cifras derivadas del propio documento 16 — SUPERADA**

*Causa* (doc 17, L1305): el documento 16 declara en prosa 29 adjudicados y 13 medios cuando
su propia tabla da 32 y 16; y dice «dieciocho fuentes» cuando su requisito 0.1 enumera
diecinueve.
*Decisión*: índice y checkpoint. *Sede*: `00-INDICE.md` filas de los documentos 16 y 17, y
`CHECKPOINT` L1150–1160.
*Condición declarada*: «los documentos 15, 16 y 17 son inmutables; se reanclan sus
proyecciones».
*¿Se cumple?* **SÍ.** `00-INDICE.md` dice ahora, en la fila del documento 16: «Su recuento en
prosa —29 adjudicados y 13 medios— **es erróneo**: su propia tabla da **32 y 16**, 31
distintos, y el documento 17 lo fija (`F-12`). El documento 16 **no se corrige**: es
histórico e inmutable, y lo que se reancla es esta proyección», y recoge también el
dieciocho/diecinueve. Verifiqué con `git diff` que **los documentos 15, 16 y 17 no fueron
tocados por el rango** (no aparecen en `--stat`), que es la mitad que importa: la disciplina
de inmutabilidad se respetó. **SUPERADA.**

---

**Recuento de mis trece filas: DIEZ SUPERADAS · DOS FALLIDAS (`A7`, `A8`) · UNA SUPERADA CON
RESERVA DECLARADA (`A2`). NINGUNA no aplicable.**

---

## 7 · Hallazgos nuevos

Ninguno de los diez siguientes está entre los 43 del gate. Los ordeno por severidad.

---

### `G-1` · GRAVE · `D79` introduce `estado/cuarentena/<TX>/`, que el propio documento descarta doce páginas después por crear la tercera ubicación que `D50` eliminó

**Fichero y línea.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md:1962-1966` frente a
`:2103`.

> **L1962-1963** (§2.6.9, desenlace `4b`, acto de autoridad (i)): «AUTORIZAR LA CUARENTENA —
> copiar lo divergente fuera del worktree, a **`estado/cuarentena/<TX>/`**, con su hash
> registrado en el `conflicto`. Con eso la preservación deja de ser imposible y el desenlace
> 4 se vuelve alcanzable por el camino normal»
>
> **L2103** (§2.6.10, comparación de alternativas de aislamiento): «| **D** | **cuarentena**
> fuera del estado canónico | aísla lo especulativo sin ramas | **crea una tercera ubicación
> con su ciclo y su plano, que §2.4 no tiene**; y lo que aísla es justo lo que `R1` quiere ver
> | **descartada: reintroduce la tercera categoría que `D50` eliminó** |»

**Es defecto introducido por ESTA tanda**, y lo verifiqué: `grep -in cuarentena` sobre
`11-base.md` devuelve **una sola línea, L1979**, que es la alternativa descartada. En `HEAD`
devuelve cuatro, y las tres nuevas son de `D79`.

**Por qué importa materialmente.** `estado/cuarentena/` no tiene plano en §1.2 ni en §2.4, no
tiene fila en la matriz de §1.3, no aparece en el árbol de §2.3, no está en ninguna
declaración de `.gitignore`, no tiene fila de reconstrucción en §2.9, no tiene ciclo —nadie
dice cuándo se vacía— y ninguna fila adversarial la toca. Por el criterio vigente de §2.4
—«DURABLE Y VERSIONADO: `estado/` SALVO la excepción de ruta declarada abajo», y esa
excepción nombra sólo `estado/tx/`— **la cuarentena es durable y versionada**. Y entonces:

```text
· contiene la COPIA ÍNTEGRA DE CONTENIDO DIVERGENTE, que puede ser trabajo de un tercero
· §2.6.9 L1872-1877 declara expresamente que `SEG` PUEDE BLOQUEAR SU PUBLICACIÓN —«secretos,
  material no publicable»— y que sin forma autorizada de preservar, la transacción NO puede
  abandonarse
· luego el acto (i) del Owner, tal como está escrito, PUBLICA en `main` exactamente el
  material que el acto existe para poder preservar cuando `SEG` prohíbe publicarlo
· y si se decidiera lo contrario —cuarentena operacional, fuera de Git—, entonces la única
  copia de lo divergente NO SOBREVIVE a la pérdida de la máquina, que es justo la garantía
  que `4b`(i) existe para dar
```

**Las dos lecturas posibles son ambas malas, y el documento no elige ninguna.** No es una
errata: es una ubicación de estado sin plano, sin autoridad y sin ciclo, que es el modo de
fallo que `D50` cerró y que §2.6.10 sigue declarando cerrado en la misma pasada que lo
reabre.

---

### `G-2` · GRAVE · el marcador de `D78` no está sujeto a ninguna de las cinco piezas de disciplina que sostienen al marcador de transacción, y por el criterio vigente acabaría versionado

**Fichero y línea.** `11-ARQ:1488-1497`, contra `:417-418`, `:445`, `:373-408`, `:1316`,
`:1356`, `:2642-2651` y `:1718-1722`.

> **L1488-1497** · «`estado/deriva/<ID-DEL-DERIVA>.abierta` declara el `id` del evento, **las
> rutas y los items que bloquea**, y su causa. Se crea en el mismo instante que el evento y
> **se retira cuando el `deriva` se resuelve** … **No gana identidad propia**: es
> RECONSTRUIBLE desde el diario por el mismo predicado, **vive en `estado/` fuera de Git por
> la excepción de ruta de §2.4**, y el paso 4 de §3.1 sigue dando COMPONER.»
>
> **L417-418** (§2.4, la excepción invocada) · «OPERACIONAL Y NO VERSIONADO   `.ads/run/` …
> **Y los marcadores de transacción de `estado/tx/`**, por la excepción de abajo.»

La excepción invocada **no lo cubre**: nombra los marcadores de transacción y su ruta, y sólo
ésos. Las cinco piezas que sostienen al otro marcador —clasificación de plano (L433–440),
excepción de ruta (L417–418), `.gitignore` declarado en positivo (L445, L1316), fila de
reconstrucción en §2.9 (L2647) y fila adversarial `X27` (L1356)— **no existen para éste**. El
árbol de §2.3 (L373–408) no lo lista. §2.6.9 paso E (L1718–1722), que enumera el cierre «sólo
entonces, y en este orden», no lo crea.

**Por qué importa materialmente.** Por el criterio vigente de §2.4, este marcador **viaja a
Git**. Un clon nuevo lo recibe y, por el paso 2bis de §2.6.8, declara NO FIABLES las rutas que
nombra — sin ningún mecanismo que le diga si el `deriva` sigue sin reparar, y sin el ramal de
`fallo` que la garantía 6 de §2.6.6 (L1113–1121) sí da para el marcador de transacción («**El
marcador NUNCA es fuente para un clon**»). Un caché versionado que nadie regenera y que nadie
prohíbe editar **es** una segunda verdad: es el defecto de `I5` que el encargo me pidió
nombrar si aparecía, y aparece — no por diseño, sino por omisión de las cinco líneas que lo
habrían clasificado.

**Lo que refuta parcialmente mi hallazgo, y lo declaro:** la intención está escrita y es
correcta —derivado, reconstruible, sin identidad propia, «un caché legible, igual que el
otro»— y el predicado que lo regenera existe y es determinista (L1792–1794). El defecto es de
propagación, no de concepción. Pero la propagación es exactamente lo que `A8` pedía y lo que
el checkpoint declara hecho.

---

### `G-3` · GRAVE · el validador semántico del diario conserva dos reglas normativas que `D64` retiró, una de ellas con campos que ya no existen

**Fichero y línea.** `11-ARQ:3945-3947` y `:3925`, en la lista de lo que comprueba la capa B.

> **L3945-3947** · «· LA IDENTIDAD DE LA RUTA: **#observaciones = #intentos** en una
> transacción de conflicto CERRADA, y #observaciones = #intentos + 1 en una **AGOTADA** — y en
> la agotada ese `+1` es siempre el `conflicto` con **`agotado: true`**»

Contra la retirada, declarada en la misma sección del documento:

> **L718-722** (§2.6.1) · «`intentos_consumidos`, `intento` y `agotado` **se retiran**: no
> había intentos automáticos que contar, y su tope era el que producía `B1`.»

Y la «ruta AGOTADA» es literalmente el estado sin salida que `D64` elimina en su raíz
(L574–585). **La regla es incomprobable: exige contar un campo que el esquema no tiene y
clasificar una ruta que el autómata no admite.** Es texto base no corregido
(`11-base.md:3797`).

> **L3925** · «· TERMINALIDAD: exactamente un `derivada` por transacción cerrada, y ninguno en
> las abiertas»

**Falso desde `D64`**: una transacción cerrada por `abandonada` tiene **cero** `derivada`.
Contradice la tabla de cardinalidad de §2.6.4 (L1000–1002: `derivada` = **0** en la columna
`abandonada`) y el bullet de L3948–3952 —tres líneas más abajo, en la **misma lista**— que
enuncia lo correcto: «`derivada` y `abandonada` **mutuamente excluyentes**, y toda transacción
cerrada tiene exactamente uno de los dos». Es texto base no corregido (`11-base.md:3777`).

**Por qué importa materialmente.** La capa B es la sede que `D71` designa para evaluar
`abierta(tx)` (L616–619) y la que hace cumplir «ninguna transición sale de un terminal»
(L676–679). Un validador construido literalmente de esta lista **rechazaría toda transacción
abandonada como defectuosa** por la regla de terminalidad, e intentaría comprobar una regla
inconstruible por la de identidad de ruta. Y la primera es una afirmación vigente de que
`derivada` es el único terminal, en la única capa que puede comprobarlo — es decir, el residuo
exacto de `A2` en el sitio donde más cuesta.

---

### `M-1` · MEDIO · el censo de sedes de `abierta(tx)` es incorrecto en dos de sus siete entradas, y su declaración de cierre es falsa

**Fichero y línea.** `11-ARQ:621-624`, contra `:894`.

La cifra siete es **correcta** —la conté—, pero el censo nombra **§2.6.4** y **§2.6.9**, que
no contienen ninguna cita del predicado (verificado con barrido acotado a L831–1038 y
L1532–2007), y omite **§2.6.5** (`W8`, L1061) y **§2.6.11** (L2313), que sí. Y la afirmación
«**Ninguna lo redeclara**» es desmentida por el propio documento:

> `11-ARQ:894` · «1  ¿EXISTE UNA TRANSACCIÓN ABIERTA —`preparada` durable y **SIN
> `derivada`**— QUE DECLARE ESA RUTA, EN ESTA INSTALACIÓN?»

**Por qué importa.** La condición de cierre que el checkpoint publica para `A2` es
literalmente «las siete sedes remiten», y la comprobación mecánica que la tanda declara haber
hecho incluye «**UN predicado `abierta(tx)`**» (`CHECKPOINT` L1290). Un lector que siga el
censo hasta §2.6.4 no encuentra remisión: encuentra la formulación retirada.

**Lo que refuta la gravedad, y lo declaro por delante:** el paso 0 de §2.6.4 (L883–892)
comprueba los DOS terminales antes de llegar al paso 1, luego la función de clasificación es
correcta y no hay defecto de comportamiento. Es un defecto de la declaración de cierre y de
su censo, no del protocolo.

---

### `M-2` · MEDIO · tres sedes vigentes describen el resultado de un abandono como «estado mixto», que `D69` retiró, y la garantía de `main` se apoya en la premisa refutada

**Fichero y línea.** `11-ARQ:2192-2195`, `:1459`, `:2343-2344`.

> **L2192-2195** (§2.6.10) · «MAIN NUNCA CONTIENE ESTADO PARCIAL — porque un commit sólo
> ocurre **sin marcadores abiertos**, y sin marcador toda transacción está cerrada por uno de
> sus dos terminales. **Un abandono deja estado mixto declarado** en su `abandonada` y en su
> `deriva`, no silencioso (§2.6.9).»
>
> **L2343-2344** (§2.6.11, glosa de `abandono-de-transaccion`) · «Una autoridad cerró la
> transacción con `abandonada` sin completarla, y **sus rutas quedaron en un estado mixto
> declarado**.»
>
> **L1459** (§2.6.8, paso 2bis) · «una regla que sólo mirase marcadores dejaría de ver
> exactamente **el estado mixto que el abandono declara**.»

Contra `D69`, que hace `abandonada` **inalcanzable** hasta la restauración verificada byte a
byte:

> **L1728-1730** · «LLEVA · el estado canónico **RESTAURADO A LA BASE — idéntico, byte a
> byte**, al del commit anterior en todas las rutas de la transacción»
>
> **L1680-1686** (la nota de `D69`) · «La redacción anterior hacía que `abandonada` retirase
> el marcador **dejando el conjunto parcial en el worktree**, y con el marcador retirado ese
> conjunto era **publicable**.»

**Por qué importa.** El argumento de L2192–2193 —«sin marcador toda transacción está cerrada,
luego `main` no contiene estado parcial»— **es exactamente la inferencia que `D69` refutó**.
La razón real por la que `main` no contiene estado parcial es la restauración verificada, y
esa razón no se invoca. Además, en la ruta normal de abandono **todas** las rutas quedan
clasificadas `previo`: el enum `{previo, posterior, divergente}` de `estado_observado[]`
(§3.6 L3804) sólo alcanza `posterior` y `divergente` en el acto (ii) del desenlace `4b`, y
eso no está dicho en ninguna parte. F6 construiría un validador sobre un enum cuya
alcanzabilidad depende de un caso que el contrato no nombra.

**Lo que refuta parcialmente mi hallazgo, y lo declaro:** la **conclusión** de L2192 sigue
siendo cierta —los dos terminales dejan el árbol consistente y el desenlace `4b` no publica—.
Lo que falla es su argumento y la glosa de las tres sedes, no la propiedad.

---

### `M-3` · MEDIO · §14 escenario 1 afirma que antes de `INS-3` no hay estado que perder, y esta tanda reescribió esa celda sin corregirla

**Fichero y línea.** `11-ARQ:6801`.

> «| 1 | **proyecto nuevo** | … | **repetir el paso; antes de INS-3 no hay estado que
> perder** |»

Contra `D30` y §8.1, en el mismo documento:

> **L7002** (§15.8, registro de `D30`) · «**`estado/` nace en INS-0**, con su soporte durable
> mínimo … una iniciativa que nace en INS-0 con soporte desde INS-3 vive en el chat entre
> medias, y el apartado 19 de la directiva lo prohíbe»
>
> **L5561** (§8.1) · «### `estado/` nace en INS-0, y no en INS-3»
>
> **L5529-5530** · «REANUDACIÓN **por el checkpoint del paquete de `SIS-001`, desde INS-0**.
> Ningún tramo del recorrido depende del chat»

**Y esta tanda tocó esa celda.** El texto base decía «antes de **N3** no hay estado que
perder» (`11-base.md:6233`); `D83` renombró `N3` → `INS-3` **sin corregir la sustancia**, con
lo que reescribió en texto fresco una afirmación que `D30` retiró.

**Por qué importa.** §14 es la sección que el documento presenta como demostración de que las
piezas encajan. Su escenario 1 declara que la instalación no tiene estado recuperable en sus
tres primeras fases, que es literalmente lo que `D30` corrigió por violar el apartado 19 de la
directiva.

---

### `M-4` · MEDIO · el recuento de extensiones de ficha discrepa entre §5.2 y §17

**Fichero y línea.** `11-ARQ:4475-4477` contra `:7588`.

> **L4475-4477** (§5.2) · «QUÉ TRABAJO GENERA una EXTENSIÓN DE FICHA en F6 … **Son SEIS**, no
> cuatro: las cuatro de las dos dimensiones huérfanas, más `DSP` y `ENC` que el gate final
> añadió» — y L4487, L4492 las nombran, con la remisión «registrada abajo y **en §17**»
> (L4525, L4554)
>
> **L7588** (§17) · «quince capacidades, roles, métodos, prompts | **intactos** … **`+4`
> extensiones de ficha: `ENT`, `ARQ`, `PLT` y `SEG`** |»

§5.2 remite a §17 dos veces, y §17 conserva el recuento anterior a `M-5` y `M-6`. **Por qué
importa:** §17 es la tabla que declara qué le pasa a cada pieza del ADS actual, y es de donde
F6 leería cuántas fichas tiene que extender. Faltarían `DSP` y `ENC`, que son precisamente las
dos que el gate añadió y cuyas condiciones de cierre el checkpoint declara `M-5` y `M-6`
resueltas como `CONTRATO_COMPLETO_PARA_F6`.

*Nota de frontera:* la materia de esta discrepancia es capacidades y fichas, que puede
corresponder a otro revisor. La registro porque es un recuento derivado que no cuadra y lo
comprobé yo, no porque presuma sobre el reparto.

---

### `N-1` · MENOR · la ventana de commit se define sobre `derivada` únicamente

**Fichero y línea.** `11-ARQ:1180-1181`.

> «QUÉ ES UNA VENTANA DE COMMIT — el conjunto de transacciones cuyo evento **`derivada`** NO
> está incluido todavía en ningún commit de Git.»

Una transacción cerrada por `abandonada` no tiene ni tendrá `derivada`, luego **nunca sale de
la ventana** y la comprobación de integridad post-terminal la recorrería indefinidamente.
**Mitigado**, y por eso es MENOR: L1190–1191 dice «Las cerradas por `abandonada` no afirman
ningún resultado: su `deriva` ya declara lo observado, y no se vuelve a emitir», luego la
consecuencia es coste, no fallo. Es otro residuo de partición binaria sobre `derivada`.

---

### `N-2` · MENOR · dos resúmenes conservan «completar, o marcar conflicto» sin la segunda salida

**Fichero y línea.** `11-ARQ:5225-5226` (§7.3) y `:6808` (§14, escenario 8).

> **L5225-5226** · «CAÍDA A MITAD — evento `preparada` de la tx: **completar, o `conflicto`**
> si algún fichero es divergente (§2.6)»
>
> **L6808** · «| 8 | **caída durante escritura** | … | **se completa o se marca conflicto** |»

`conflicto` no es un desenlace: es una observación con dos salidas (§2.6.9). Los dos resúmenes
omiten el abandono con restauración que `D73` llevó a §7.4. **MENOR** porque los dos remiten a
§2.6 y ninguno es sede normativa del desenlace, pero es la formulación que `A3` corrigió,
sobreviviendo dos secciones más allá.

---

### `N-3` · MENOR · `X58` y `X54` describen el grafo con precisión, y lo digo porque es lo contrario de un defecto

No es un hallazgo: es una comprobación que hice esperando encontrar un defecto y **no lo
encontré**. `X54` (L1368) exige que el `conflicto` sobreviva o se reconstruya y que «la
transacción siga teniendo sus DOS salidas disponibles tras el arranque»; `X58` (L1372) separa
lo que el grafo cierra de lo que cierra la autoridad, y lo dice sin adorno. Las dos filas
están bien escritas y son convertibles en prueba sin traducción.

---

## 8 · Hallazgos que intenté y NO pude reproducir

Esta lista es parte del entregable. **Ninguno de los siguientes es un hallazgo.**

| # | qué busqué | resultado | por qué |
|---|---|---|---|
| 1 | que el rango hubiera tocado `C7`, contra su declaración | **NO OCURRIÓ** | `git diff 7e99388..0a4b3a0 -- kernel/operativo/contratos/C7-*` devuelve **vacío**. `C7:170` conserva literal `aplica_a: "todo item cuyos paquetes escribieron en una o más fuentes"` |
| 2 | que el rango hubiera tocado esquemas o kernel | **NO OCURRIÓ** | `--stat` sobre el rango: **cuatro ficheros**, todos en `docs/`. `kernel/` intacto |
| 3 | que los documentos 15, 16 o 17 hubieran sido editados pese a declararse inmutables | **NO OCURRIÓ** | no aparecen en `git diff --stat` del rango |
| 4 | una segunda sede editable para el enum de `deriva.causa` | **NO EXISTE** | §2.6.11 se autodeclara GLOSA con regla de desempate (L2331–2333); las tres sedes coinciden |
| 5 | una autorización de `--force` en alguna ruta | **NO EXISTE** | L2220–2223: «PROHIBIDO. Sin excepción automática … Ninguna recuperación, ningún reintento y ninguna política lo autorizan». Coherente en L2057–2058 y L2287 |
| 6 | una promesa vigente de reanudación distribuida exacta | **NO EXISTE** | L1908–1917 («**NO EXISTE REANUDACIÓN EXACTA** … REINICIO SEGURO, no reanudación») y L2124–2125 («SE SACRIFICA la REANUDACIÓN EXACTA DISTRIBUIDA») |
| 7 | filas duplicadas o ids repetidos en la tabla adversarial | **NO REPRODUCIDO** | mi conteo independiente da **42 filas / 42 ids**, con los huecos que L1397–1403 declara |
| 8 | una cifra de §3.6 o §3.8 que no cuadre | **NO REPRODUCIDO** | 34 · 20 · 54, 5 · 6 · 7 y 19+4+2=25, los ocho recuentos derivados por mí |
| 9 | «un único escritor» sostenido en alguna sede vigente | **NO EXISTE** | una sola aparición en el documento 11 (L2166), y es la que lo retira. La del registro `D65` es histórica y `D84` la declara revisada |
| 10 | una segunda sede editable de prioridad y aparcado | **NO EXISTE** | §1.3 L217, L240–248 y `a.9` L692–697 coinciden: la orden es canal de comandos, `02-control.md` es el campo canónico |
| 11 | demostrar `G-1`, `G-2` o `G-3` **en ejecución** | **NO PUDE** | no existe `esquemas/evento.yaml`, no existe validador del diario y no existe runtime. Los tres son contradicciones **textuales y verificables**, no fallos observados |
| 12 | que `estado/tx/` o `estado/deriva/` estuvieran provisionados en el árbol | **NADA PROVISIONADO** | consistente con «NADA ESTÁ CONSTRUIDO» (§19). No es defecto en una fase de diseño |
| 13 | que `T148`/`T159` fueran defecto del entregable | **NO LO SON** | Python 3.10.12 en este entorno; es `A14`, declarado ajeno a F4 por el gate |

---

## 9 · Limitaciones de mi revisión, sin adorno

```text
1  NADA DE LO QUE REVISÉ ESTÁ CONSTRUIDO. No hay esquema de `evento`, ni validador del
   diario, ni runtime, ni un solo fichero bajo `estado/`. Todos mis hallazgos sobre el
   protocolo son sobre TEXTO. Un contrato contradictorio no es un sistema roto: es un
   sistema que no se puede construir sin decidir cuál de las dos frases vale.

2  NO he leído `15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` íntegro, ni el dictamen del
   REVISOR B del documento 16 salvo `M-8`, ni el documento 17 íntegro. Las causas originales
   de mis trece filas están todas en los tramos que sí abrí, pero no puedo afirmar que otro
   tramo no diga algo que las matice.

3  NO he leído `a-ENMIENDA-E2-MULTIREPO.md` íntegro, ni `a.7`, ni `b.14`, ni `b.16`, ni
   `C1`-`C5`. Verifiqué `a.9` y `C6`/`C7` sólo en los tramos citados. Una cita correcta de
   un tramo no garantiza que otro tramo no la contradiga.

4  MI DERIVACIÓN DEL PREDICADO `abierta(tx)` es una derivación de TEXTO. Coincide con lo
   publicado, y eso es todo lo que afirmo: no he demostrado que ningún otro predicado sea
   imposible, sólo que ninguno del documento lo exige.

5  LA GRAVEDAD DE `G-1` DEPENDE DE UNA LECTURA. Sostengo que por §2.4 la cuarentena queda
   versionada; si alguien argumentara que `estado/cuarentena/` hereda la excepción de ruta
   por analogía, el hallazgo bajaría a MEDIO y seguiría siendo un defecto —porque entonces
   la única copia de lo divergente no sobrevive a la pérdida de la máquina—. Lo que NO
   admite lectura es que §2.6.10 L2103 descarta la cuarentena y §2.6.9 L1962 la autoriza.

6  NO he consultado al REVISOR H, no conozco su materia y ninguna de mis conclusiones
   depende de nada suyo. `M-4` toca fichas de capacidad y puede solapar con otro eje; lo
   registro como observación propia, no como reparto.

7  DOS PRUEBAS del corpus (`T148`, `T159`) no pudieron evaluarse por la versión de Python de
   este entorno. NO afirmo que pasarían en 3.11; afirmo que su fallo aquí no es atribuible
   al entregable.

8  DONDE ESCRIBO «CUADRA», LO CONTÉ. Donde escribo «NO CUADRA», lo conté y difiere. Ningún
   recuento de este dictamen procede de leer un titular del documento.
```

---

## 10 · Lo que está bien, porque un dictamen que sólo lista defectos no es una medida

Afecta a mi recomendación, y por eso lo digo antes de darla.

**`D69` y `D70` siguen siendo las mejores correcciones del expediente**, y esta tanda no las
ha degradado: la separación estable/especulativo, el procedimiento A–E con verificación byte
a byte, los tres niveles de recuperación y la limitación distribuida declarada sin disimulo
son material profesional. **`D71` cierra su bloqueante de verdad**: el marcador ya no
resucita, el commit ya no se bloquea para todo el producto, y el predicado tiene sede. **`D72`
cierra el suyo en las tres capas**, no en una. **`D73` reescribe §7.4 correctamente y alinea
§16.** **`D84` sustituye un argumento falso por uno técnicamente correcto**, que es más
difícil que retirar una frase. **`D83` elige renombrar el espacio más nuevo y no el
contrato**, que es la elección correcta. Y **la aritmética de §3.6 y §3.8 cuadra exactamente**
en los ocho recuentos que derivé sin fiarme de ningún titular — incluidos los tres que el
encargo me pidió desconfiar por nombre.

**El patrón de mis hallazgos es uno solo, y es el mismo que el REVISOR A describió una tanda
atrás**: no encontré ninguna decisión mal tomada. Encontré decisiones bien tomadas cuya
propagación al resto del documento quedó incompleta — y, en `G-1`, una decisión nueva que no
se contrastó contra una alternativa que el propio documento ya había descartado.

---

## 11 · Recomendación de veredicto

# INSUFICIENTE PARA F5

**En mi materia**, y en una frase: **dos de las trece filas que me tocan están declaradas
`CORREGIDO_EN_F4` sin estarlo —`A7` conserva byte a byte la única sede que el gate nombró, y
`A8` no cambió la regla que el lector ejecuta ni sometió su marcador nuevo a ninguna de las
cinco piezas de disciplina que la condición de cierre exigía—, y la tanda introduce un
hallazgo GRAVE propio: `D79` autoriza `estado/cuarentena/<TX>/` doce páginas antes de que el
mismo documento descarte la cuarentena por crear exactamente esa tercera ubicación sin plano
que `D50` eliminó.**

**No soy quien emite el veredicto.** Lo recomiendo, y cada afirmación de arriba lleva su
fichero y su línea para que se verifique una a una.

```text
FILAS DE MI MATERIA        13 · 10 SUPERADAS · 2 FALLIDAS (`A7`, `A8`) · 1 SUPERADA CON
                           RESERVA DECLARADA (`A2`) · 0 no aplicables

HALLAZGOS NUEVOS           10 · 0 BLOQUEANTES · 3 GRAVES (`G-1` `G-2` `G-3`) ·
                           4 MEDIOS (`M-1` `M-2` `M-3` `M-4`) · 2 MENORES (`N-1` `N-2`) ·
                           1 comprobación en positivo (`N-3`)

QUÉ NO BLOQUEA             ninguno de los diez exige una decisión arquitectónica nueva salvo
                           `G-1`, cuya salida es elegir uno de los dos planos para la
                           cuarentena y escribirlo. Los otros nueve se cierran alineando
                           texto con decisiones que el documento ya tomó correctamente.

LO QUE ESTE DICTAMEN NO    que el protocolo funcione. Nada de esto está construido, probado
DEMUESTRA                  ni ejecutado, y escribir el contrato de una prueba no es la
                           prueba.
```

---

# DICTAMEN DEL REVISOR H

# DICTAMEN DEL REVISOR H — GATE DE CIERRE INDEPENDIENTE DE `F4c`

**Materia:** capacidades, procesos, composición de rutas, handoffs, macrocircuitos,
documentación, adopción, F5/F6 y operabilidad.

---

## 1 · Identidad, procedencia y modo

No escribí `F4`, `F4b` ni `F4c`. No apliqué ninguna de sus correcciones. No participé en
ninguna decisión `D16`–`D86` ni en ninguna resolución `O1`–`O16`. No fui revisor `A`, `B`,
`C`, `D`, `E` ni `F` de los documentos 16 y 17. Existe un REVISOR G trabajando en paralelo
sobre otra materia: **no lo he consultado, no he supuesto nada de lo que diga, y ninguna
afirmación de este dictamen depende de él.**

**Modo: SÓLO LECTURA.** No he modificado ningún fichero del repositorio, no he hecho
commits ni ninguna escritura de git. El único fichero que he escrito fuera del repositorio
es una copia de trabajo de la versión anterior del documento 11, extraída con
`git show`, en el directorio temporal de sesión, para poder contrastar el antes y el
después sin tocar el árbol.

```text
repositorio   /home/jose/ads-kernel
rama          redesign/kernel-2.0
HEAD          0a4b3a08ee5b0d0f896c82a892ec8ea15383fc05   (verificado con git rev-parse)
rango         7e99388557323c1e0933ff5f2bd9bc5b2fc5708a..0a4b3a08ee5b0d0f896c82a892ec8ea15383fc05
              8 commits · 4 ficheros · 1128 inserciones · 213 supresiones
```

Los ocho commits del rango, verbatim de `git log --oneline`:

```text
a8e85f9  fix(f4c): nivel 1 — los cuatro bloqueantes, cerrados por su causa
d02f7a1  fix(f4c): nivel 2 — los seis graves, y la coherencia transversal que arrastran
5ede376  fix(f4c): nivel 2 — el ejemplo de §5.6 usa el identificador del area unificada
1526e09  fix(f4c): nivel 3 — los medios que obligarian a F6 a decidir arquitectura
3614e75  fix(f4c): nivel 4 — recuentos, citas, espacios de nombres y lo que es externo
6975b59  docs(f4c): matriz de cierre de los 43, y las cifras del gate reancladas
2f2d220  fix(f4c): §8.0 no repite la formula que el validador de vocabulario prohibe
0a4b3a0  docs(f4c): la matriz de los 43 se reconcilia — un estado primario por hallazgo
```

Sólo cuatro ficheros cambian en todo el rango: `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`,
`docs/evolucion/CHECKPOINT-ADS-NEXT.md`, `docs/evolucion/00-INDICE.md` y
`docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`. **Nada de `kernel/operativo/` cambia**, lo
cual es coherente con lo que la propia tanda declara.

---

## 2 · Corpus realmente leído

SHA-256 (16 primeros) y líneas, calculados sobre el árbol en `HEAD`.

| path | SHA-256 (16) | líneas | íntegro | qué contrasta |
|---|---|---|---|---|
| `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | `45984236979cedda` | 7826 | **NO** — ver §9 | el objeto. §0, §1, §4, §5, §7, §8 completos, §9.1/§9.4/§9.5, §13, §14, §15.2–§15.8, §16, §17, §18, §19 |
| `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | `265ddf72008b52c2` | 1341 | parcial (L1140–1341) | la matriz de cierre de los 43, los cinco estados, los atributos secundarios y la «siguiente acción exacta» |
| `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | `8243034f286160cc` | 1257 | parcial | `B-1`, `B-2`, `G-1`–`G-4`, `M-5`, `M-6`, `M-7`, `m-1`–`m-4` y la tabla de adjudicación |
| `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` | `18f876d4cd47a2f7` | 1650 | parcial | §5 del revisor D (`C5` frente a `B-2`), `E-2`, `E-3`, y el índice de los diez `E-<n>` |
| `docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` | `b0e015c118ceb916` | 651 | **NO LEÍDO** | — |
| `docs/evolucion/00-INDICE.md` | `2b183503df95a1ca` | 100 | parcial (diff del rango) | la reancla de «ONCE presiones» y «CORREGIDA NUEVE VECES» |
| `docs/evolucion/ADS-NEXT-OWNER-BRIEF.md` | `e82036724b92bdd6` | 1341 | parcial | §6.2 (las catorce preguntas del baseline), cabecera y §1 |
| `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | `a88609167dbbea28` | 2163 | parcial | §5.18 (doce obligatorias, trece condicionales) y §5.23 |
| `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | `54333d773a4156e5` | 511 | parcial | `O7`–`O16`, `D74`–`D84`, y la derivación completa de `D1`–`D86` |
| `docs/rediseno/a-CAPACIDADES-APROBADA.md` | `10cafb5ceee44f57` | 1132 | parcial | a.3 (catálogo, estación/servicio/sistema), a.5 (propiedad global, custodia, veto), a.6 (composición y traza), a.7 (FRENO 3 literal) |
| `docs/rediseno/b-RECORRIDO-APROBADA.md` | `f8cb974316e283fa` | 1288 | parcial | b.1 (regla de proceso único), b.10 (cierre), b.16 (las diez rutas, el vocabulario `C-<CAP>`, `AUD`, `DIR`) |
| `docs/rediseno/a-ENMIENDA-E1-ENC.md` | `18dae19523b25ed4` | 211 | **NO LEÍDO** | — |
| `kernel/operativo/00-INDICE.md` | `fa3affa7b2bebc00` | 139 | **SÍ** | el mapa de fuente única; «entregas entre capacidades → `circuitos/`»; quince capacidades; diecinueve esquemas |
| `kernel/operativo/recorrido/01-PROCESOS.md` | `98b5cbc836121044` | 564 | parcial (L1–140, L266–564) + derivación completa por `grep` | los diez procesos, sus propietarios globales, obligatorias y condicionales; `AUD` L410–448 con L419 |
| `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` | `f56e8fe4872e46b5` | 130 | **NO LEÍDO** | — |
| `kernel/operativo/contratos/C1-…` | `825f15a914c10d6f` | 161 | parcial | la regla de subconjunto de autoridad (L118, L125) |
| `kernel/operativo/contratos/C2-…` | `3ee58ca4bc47988d` | 539 | **NO LEÍDO** | — |
| `kernel/operativo/contratos/C3-…` | `d56bf6b81e0fe4a9` | 150 | **NO LEÍDO** | — |
| `kernel/operativo/contratos/C4-…` | `670289180e59b176` | 170 | **NO LEÍDO** | — |
| `kernel/operativo/contratos/C5-HANDOFF.md` | `af6f1a4c4f5def8d` | 115 | **SÍ** | que `C5` no compone rutas; «el trabajo lo compone DSP» |
| `kernel/operativo/contratos/C6-…` | `14805a79aeb07f31` | 336 | **NO LEÍDO** | — |
| `kernel/operativo/contratos/C7-…` | `83f82e2be4756a46` | 250 | parcial (L60–130) | **la tabla de propiedad de cada operación Git, L80–L92** |
| `kernel/operativo/circuitos/00-CIRCUITOS.md` | `a6fe7c38875c0d52` | 240 | parcial | cabecera, `AUD` L157–170, «Handoffs declarados» L232–240 |
| `kernel/operativo/circuitos/DIS-handoffs.md` | `87bb395766164dfd` | 247 | parcial | los ocho `cuando`, `dis-a-ver` L135–140 |
| `kernel/operativo/circuitos/handoffs-generales.md` | `1902884c33728729` | 245 | parcial | los nueve `cuando`, y el par `de`/`a` de las diecisiete instancias |
| `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | `08f4bea44594e026` | 141 | **NO LEÍDO** (sólo L110) | — |
| `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | `dd323d1aa2f7ede3` | 352 | **NO LEÍDO** | — |
| `kernel/operativo/diseno/02-RUBRICAS.md` | `8aa8fb18426eac21` | 343 | **NO LEÍDO** | — |
| `kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md` | `8695161d660b9bc5` | 264 | parcial (L1–60, L250–264) | quién calcula el nivel y dónde se registra — refuta un hallazgo mío |
| `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | `5d2f54535c1334c0` | 130 | **NO LEÍDO** | — |
| `kernel/operativo/diseno/05-FIDELIDAD.md` | `fdabb29f7592e603` | 129 | **NO LEÍDO** | — |
| `kernel/operativo/entrada/00-INDICE.md` | `315b2790cb66bb4c` | 28 | **NO LEÍDO** | — |
| `kernel/operativo/entrada/01-TAXONOMIA.md` | `ff0fec389d47bc37` | 309 | parcial | las **nueve** clases, derivadas por `^id: entrada:` |
| `kernel/operativo/entrada/02-CIRCUITO.md` | `e204167c8895bff9` | 145 | **NO LEÍDO** | — |
| `kernel/operativo/entrada/03-FORMAS.md` | `cdb3b575f8a28a5a` | 557 | parcial | cabecera L3, las **catorce** formas, el algoritmo L536–551 |
| `kernel/operativo/entrada/04-INCERTIDUMBRE-…md` | `1716bd3d8b48107d` | 187 | **NO LEÍDO** | — |
| `kernel/operativo/entrada/05-ESCENARIOS.md` | `31f2dcece59e2ecb` | 637 | parcial | cabecera L5, L178–184, e inventario de `T<n>` |
| `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | `64d170f5acc15144` | 3343 | parcial | cabecera + barrido de «actualización de ADS» (cero mandatos) |
| `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | `48412108f711204f` | 597 | parcial | cabecera, §3 L79, §12 L487, §15 L584–597 |
| `kernel/operativo/esquemas/memoria.yaml` · `handoff.yaml` · `proceso.yaml` | — | — | **SÍ** los tres | el patrón `^memoria:[a-z0-9-]+$`, `ref_a: capacidad` en handoff, `tipo: texto` en proceso |

**LAS QUINCE FICHAS `capacidades/<CAP>/CAPACIDAD.md`** — existencia, `clase`, `metodos`,
`mision` y `autoridad` derivadas por `grep` sobre las quince; **leídas de verdad sólo `PLT`
(L1–40) y `DSP` (L1–50)**. Las trece restantes **NO las leí íntegras**, y lo digo sin
adorno. Sus SHA-16 y líneas:

```text
APR a870911530909584/95   ARQ 6ca11b5f09883e24/104  CON e0f79e6c3a467302/107
DIS 06f019010d45771f/147  DOM 926c7144cb098caa/135  DSP acb292f882e77d74/152
ENC f71b8e43f6e2d66f/174  ENT 91a81d3cf1cbfa61/123  INV 47412638e7552da1/96
PLT a5f87977c58ed1d0/108  PRD e83b0e08272e219d/105  SEG 19bfd38a7a24b57f/135
SIS 02089f36d1244356/119  USO 65f144e4a5c756ef/94   VER 91a16b482629daf3/135
```

---

## 3 · Método y comandos exactos, repetibles

```bash
git rev-parse HEAD
git log --oneline 7e99388..0a4b3a0
git diff --stat 7e99388..0a4b3a0
git show 7e99388:docs/evolucion/11-ARQUITECTURA-INTEGRADA.md > /tmp/.../11-OLD.md

# derivación de los diez procesos y sus propietarios, del corpus y no del texto de F4
grep -n '^## \|^id: proceso:\|propietario_global' kernel/operativo/recorrido/01-PROCESOS.md

# derivación de las quince capacidades y sus clases
ls kernel/operativo/capacidades/
grep -n '^clase:'   kernel/operativo/capacidades/*/CAPACIDAD.md
grep -n '^metodos:' kernel/operativo/capacidades/*/CAPACIDAD.md

# las diecisiete instancias de handoff, enumeradas, y sus pares
grep -h '^de:\|^a:' kernel/operativo/circuitos/*.md | paste - - | sort | uniq -c

# nueve clases de entrada y catorce formas, contadas y no citadas
grep -c '^id: entrada:' kernel/operativo/entrada/01-TAXONOMIA.md
grep -c '^id: forma:'   kernel/operativo/entrada/03-FORMAS.md

# once presiones vigentes, derivadas de sus cabeceras
grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | grep -vc 'RETIRADA\|FUSIONADA'

# doce identificadores documentales, únicos
grep -o 'aspecto:documental/[a-z-]*' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | sort -u

# D1–D86 sin hueco, del registro y no del documento 11
grep -o '^| D[0-9]* ' docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md | tr -d '| ' | sort -V

# los doce ejemplares del patrón `ads:memoria`
grep -rho 'memoria:[a-z0-9-]*' kernel/ docs/ | sort -u
```

---

## 4 · Comprobaciones independientes: derivado frente a declarado

| magnitud | declarado por F4 / el checkpoint | derivado por mí | veredicto |
|---|---|---|---|
| capacidades | quince: `APR ARQ CON DIS DOM DSP ENC ENT INV PLT PRD SEG SIS USO VER` (§18 L7666) | quince directorios, quince `CAPACIDAD.md`, quince `id:` | **COINCIDE** |
| procesos | diez, «ninguno nuevo» (§8.0 L5313, §17 L7589) | `FEA GAP DEF INC INV DEU DEP AUD DIR SIS` | **COINCIDE** |
| propietarios globales | `SIS→SIS`, `INV→INV`, `DEU→ARQ`, `DEP→PLT`, `AUD` derivado (§18 L7684) | idéntico, contra L527/L275/L312/L368/L419 | **COINCIDE** |
| `AUD`: única obligatoria | `INV` (§8.2, §18) | `conclusion-fundada`, `capacidad_productora: INV` (L423–427) | **COINCIDE** |
| `AUD`: propietario a mano | prohibido, `01-PROCESOS.md` L419 | L419 literal: «DERIVADO del encargo … NUNCA se asigna a mano» | **COINCIDE** |
| `DEP`: `SEG` irretirable | `G28`, «nadie» (§18 L7682) | L369–374: `autoridad_de_retirada: nadie: G28 …` | **COINCIDE** |
| `SIS`: condicionales | dos, `ENT` y `APR` (`PN-13`) | dos, exactamente | **COINCIDE** |
| `INV`: condicionales | `CON:experimental`, `PRD`, `ARQ`, `APR` (`PN-13`) | los cuatro, y **ni `DOM` ni `SEG` ni `DIS`** | **COINCIDE — `PN-13` es un hecho, no una opinión** |
| instancias de handoff | diecisiete (§8.0 L5325, §15.7) | diecisiete pares `de`/`a` | **COINCIDE** |
| `SIS`/`PLT` en handoffs | cero instancias (§8.0 L5467) | cero, por enumeración completa | **COINCIDE** |
| clases de entrada | nueve (§5.3 L4527) | nueve `^id: entrada:` | **COINCIDE** |
| formas de conversación | catorce (`F-10`) | catorce `^id: forma:` | **COINCIDE** |
| áreas documentales obligatorias | doce, «literalmente `§5.18`» (§4.3) | doce, verbatim contra `ADS-PENDIENTES` L775–786 | **COINCIDE** |
| identificadores documentales | doce (`D77`) | doce `aspecto:documental/<area>`, todos distintos | **COINCIDE** |
| áreas condicionales | TRECE (§4.3 L4320, L4353, tabla) | trece, verbatim contra `ADS-PENDIENTES` L788–790 | **COINCIDE** |
| preguntas del baseline `A3` | catorce, §6.2 de la directiva | catorce, verbatim contra `ADS-NEXT-OWNER-BRIEF` L435–450 | **COINCIDE** |
| ejemplares de `ads:memoria` | doce (§4.3) | doce `memoria:<slug>` distintos | **COINCIDE** |
| esquemas | diecinueve (§17 L7590) | diecinueve `.yaml` en `esquemas/` | **COINCIDE** |
| presiones normativas vigentes | ONCE (§0, §16, §19, checkpoint) | once (13 cabeceras − `PN-4` − `PN-5`) | **COINCIDE en el total, NO en el texto que lo enumera — ver `H-6`** |
| decisiones | `D1`–`D86` sin hueco | `D1`–`D86` sin hueco en el registro | **COINCIDE** |
| extensiones de ficha | **SEIS** (§5.2 L4476) / **CUATRO** (§16 L7576, §17 L7588) | **dos sedes contra una** | **NO COINCIDE — `H-3`** |
| veces corregido | NUEVE (cabecera L12) | 12 bloques de decisión en §15.8; la aposición de la propia frase enumera 10–11 | **NO COINCIDE — `H-11`** |
| ejecutor del source change | `PLT` (§8.0 L5380, §8.1, §8.2, §8.3, §8.4, §18) | `C7` L83–86: **la capacidad con custodia, ella misma** | **NO COINCIDE — `H-1`** |

---

## 5 · Los once puntos del encargo

### 5.1 · Punto 1 — `D74`, `B-2` y la composición de ruta

**`C5` no compone rutas: CONFIRMADO, y con la fuente delante.**
`C5-HANDOFF.md` L36–38 dice literalmente *«Los handoffs concretos entre capacidades viven
en `circuitos/`, no aquí: **C5 define la forma, no las instancias.**»*, y L59 dice
*«NO VIAJA una tarea. Viaja un ARTEFACTO y su evidencia; **el trabajo lo compone DSP**»*.
La conclusión del NIVEL 0 se sostiene leyendo el contrato entero, que leí íntegro.
Verifiqué además, por enumeración completa de los `cuando`, que **ocho** de las diecisiete
instancias anclan su disparo a un criterio `C-<CAP>` (`DIS-handoffs` L22/L53/L80,
`handoffs-generales` L36/L83/L107/L130/L154). F4 dice «siete»; la octava —`dis-a-con`
L80— formula el criterio en negación (*«o el item no cumple `C-ARQ`»*), y bajo esa lectura
«siete» es correcto. **No es defecto.**

**§8.0 es la sede de composición: CONFIRMADO.** §8.0 L5338 declara `SEDE CANÓNICA` la
tabla de §18 y subordina §8.1–§8.4 a ella. §8.0 L5442 declara el `GATE DE COMPOSICIÓN`,
L5454 el error `composicion-incompleta` con escalado por `b.14.3`, y L5446 la
`ENTRADA Y SALIDA` por capacidad. **Todo está.**

**Ningún tipo canónico nuevo: CONFIRMADO.** §8.0 L5344 declara la composición «un CONJUNTO
DE ITEMS ENLAZADOS agrupados por una `iniciativa`», sin esquema y fuera de §3.8. §17 L7590
mantiene el total en 25 y el rango no lo toca (`git diff` no muestra cambio en §3.8).

**Un proceso por item: CONFIRMADO contra la fuente.** `b.1` L49 dice *«Un item tiene
**exactamente un proceso** en cada momento»*. La cita de §8.0 L5348 es literal.

**Las cuatro vías: CONFIRMADAS una a una contra `01-PROCESOS.md` y `b.16`.**

| macrocircuito · tramo | vía declarada | comprobación mía |
|---|---|---|
| `INS-0`–`INS-5` `SIS` | vía 1 | `propietario_global: "SIS"` L527 ✔ y `a.5`: «Para items de tipo `SIS`, es SIS» ✔ |
| `INS-*` `CON` `VER` | vía 2 | obligatorias `cambio-construido`/`evidencia-suficiente` L537/L545 ✔ |
| `INS-6` `ENT` | vía 3 | condicional «el cambio modifica el runtime» L554 ✔ |
| `INS-*` `APR` | vía 3 | condicional `C-APR` L556 ✔ |
| `INS-1`/`INS-5` `PRD` `ARQ` | vía 4, items `INV` enlazados | `INV` condicionales L288–293: `PRD` «el destino declarado es una decisión de producto», `ARQ` «…técnica» ✔ |
| `INS-5` `DOM` `DIS` `SEG` | **sin vía → `PN-13`** | ni en `SIS` ni en `INV`. **Verificado. Es honesto.** |
| `A2`–`A7` propietario | vía 1, derivado por item | L419 ✔ |
| `A2`–`A7` `INV` | vía 2, única obligatoria | L423–427 ✔ |
| `A2`–`A7` `DOM` `SEG` `DIS` `PRD` `APR` | vía 3 | `AUD` condicionales L429–439 ✔ (con la salvedad `DIS/Reconstruccion`, punto 11) |
| `A8` `ARQ` | vía 1 | `DEU` propietario `ARQ` L312 ✔ |
| `A8` `CON` `VER` | vía 2 | `plan-tecnico`/`cambio-construido`/`evidencia-suficiente` ✔ |
| `A9`–`A10` `SEG` | **sin vía → `PN-13`**, entretanto item `AUD` enlazado | correcto contra `SIS` ✔ |
| `M0`–`M5` | idéntico a `INS` | ✔ |
| `M6`–`M7` | idéntico a `A8` | ✔ |
| `U5b` `PLT` vía 1 · `SEG` `CON` `VER` vía 2 · `DOM:condiciones` `ARQ` `ENT` vía 3 | `DEP` L362–399 | **coincidencia exacta, campo a campo** ✔ |

**Criterios `C-<CAP>`: CONFIRMADOS.** `b.16` L815–830 declara siete (`C-PRD C-DIS C-ARQ
C-DOM C-SEG C-ENT C-USO`) más `C-APR`; §8.0 L5360 los enumera correctamente. La prohibición
de condición vaga existe en `b.16` L813 punto 3 y §8.0 la invoca sin repetir la fórmula
—lo cual es exactamente lo que el commit `2f2d220` corrige, y está bien resuelto.

**Items enlazados y una conclusión por item: CONFIRMADO.** `b.16` L925–929 escribe la regla
dos veces, para `AUD` y para `DIR`, tal como §8.0 L5366 afirma.

**El gate, la evidencia y el error: presentes** (§8.0 L5442–L5459).

**`PLT` como EJECUTOR — AQUÍ ESTÁ EL DEFECTO MAYOR DE MI MATERIA.**
§8.0 L5379–5382 dice: *«`PLT` bajo `C7` es el caso constante: custodia la maquinaria y
**cada source change —rama, commit, push, PR y CI POR FUENTE**—, y no es participante de la
ruta por hacerlo»*. **`C7` dice lo contrario, en la tabla que existe precisamente para
cerrar esa ambigüedad** (`C7` L76–77: *«Sin esta tabla, la responsabilidad se reparte de
forma ambigua entre `PLT`, `ENT`, `DSP` y `CON`, que es exactamente el defecto que este
contrato existe para cerrar»*):

```text
C7 L82  materializar una fuente     la solicita DSP · LA EJECUTA PLT           ← F4 acierta
C7 L83  crear rama o worktree       la solicita la capacidad con custodia · ELLA MISMA
C7 L84  commit                      la capacidad con custodia · ELLA MISMA
C7 L85  push                        la capacidad con custodia · ELLA MISMA
C7 L86  abrir PR                    la capacidad con custodia · ELLA MISMA
C7 L88  merge de una fuente         ENT · ENT
C7 L89  declarar convergencia       ENT · ENT · gate:convergencia-de-fuentes
C7 L92  retirar rama abandonada     PLT · PLT                                  ← F4 acierta
```

De las siete operaciones que F4 atribuye a `PLT`, **`C7` le da dos**. Y no es sólo una
discrepancia con el contrato: **es una contradicción interna de F4**, porque
§1.3 L224 asigna el `integration-set` a `ENT` como autoridad y ejecutor; §7.2 L5203 escribe
*«`ENT` declara convergencia con un INTEGRATION SET»*; y §7.6 L5296 escribe *«`C7` declara
quién pide, ejecuta, bloquea y verifica cada una DE LAS FUENTES. El runtime las ORQUESTA»*.
§8 dice otra cosa que §1.3, §7.2 y §7.6. Detalle agravante: §8.0 L5477 hace viajar
*«DE `PLT` A `VER` el resultado por fuente, con su estado `INTEGRACIÓN PARCIAL`»*, cuando
la convergencia es de `ENT` por `C7` L89.

Y esto **no es un residuo heredado**: comprobé con `git show` que en `7e99388` la fila
`EJECUTOR` existía **sólo** en §8.3 (L5310 del árbol anterior). Esta tanda la generalizó a
§8.0, §8.1, §8.2, §8.4 y a la columna «ejecutor y autoridad» de §18. **El defecto lo
introduce la corrección.** Es `H-1`, GRAVE.

**Consecuencia sobre `B-2`.** El dispositivo `EJECUTOR` es la respuesta de `D74` a la mitad
`PLT` del bloqueante — la que el revisor D del NIVEL 0 añadió como séptima capacidad
(doc 17 §5: *«`PLT` no tiene vehículo para `N0`/`N2`/`N6` por ninguna de las tres vías»*).
Como la atribución es falsa para `INS-6`, `A8`, `M6`–`M7`, esa mitad **queda abierta**. Su
remedio, eso sí, está completamente determinado y no exige decisión de nadie: la capacidad
con custodia es `CON`, que es obligatoria en `SIS`, `DEU` y `DEP`; la convergencia es de
`ENT`. Por eso lo gradúo GRAVE y no BLOQUEANTE.

**`PLT` frente a `a.5`.** Aquí F4 acierta en el principio: `a.5` L328–330 separa
responsabilidad de trabajo (*«No es quien más trabaja: es quien responde»*), y `b.16` L921
lo dice con esas palabras para `INV`. La ficha de `PLT` L3–4 confirma *«no toma custodia de
paquetes de producto (a.3)»*. **`PLT` no es una falsa capacidad de ruta: es ejecutor donde
`C7` L82 y L92 lo dicen, y es participante de pleno derecho por vía 1 en `U5b`, donde
`DEP` L368 le da el propietario global.** Lo que falla es el alcance que F4 le atribuye.

### 5.2 · Punto 2 — `D75`, `A2`–`A7`

Todo comprobado y todo correcto.

- **`proceso:AUD`**: §8.2 L5652 y §18 L7676. `AUD` L410–448 lo admite: su `intencion` es
  «producir una CONCLUSIÓN sobre un objeto ya existente» y su `condicion_de_entrada`
  «necesita saber en qué estado está algo que ya existe». **Encaja.**
- **Items enlazados, una conclusión por item**: `b.16` L925–927 literal. ✔
- **Propietario global derivado POR CONCLUSIÓN**: §18 L7676 y L7684 citan `01-PROCESOS.md`
  L419, que verifiqué palabra por palabra. ✔
- **Las ocho reconstrucciones de `A6`**: §8.2 L5641 enumera *producto, arquitectura,
  dominio, datos, UI/UX, sistema de diseño, seguridad y operación*, ocho, con **seis**
  propietarias (`PRD ARQ DOM DIS SEG ENT`). El reparto cierra: `DOM` toma dominio y datos,
  `DIS` toma UI/UX y sistema de diseño. **Ocho conclusiones, seis capacidades, sin hueco.**
- **`INV` única obligatoria**: L423–427. ✔ Y §8.2 L5663 explica bien qué responde y qué no:
  *«produce la evidencia de CADA item … EJECUTA la auditoría sin responder de la
  conclusión»*, que es `b.16` L921 literal.
- **Ningún proceso inventado**: los diez de `01-PROCESOS.md` son los diez de `b.16` L886–897;
  §18 usa `SIS`, `AUD`, `DEU`, `DEP` y ninguno más. ✔
- **`b.16` L899–931** (`AUD` — el propietario global se deriva del encargo) sostiene el
  conjunto entero. ✔

**`B-1` está cerrado.** Añado que verifiqué el segundo defecto de `B-1`: ni `AUD` ni `DEU`
ni `DEP` aparecen ya en ninguna columna de participantes de §18.

### 5.3 · Punto 3 — `D76` a `D86`, una a una

| | fuente | causa | corrección | coherencia | consecuencia F5/F6 | ¿decisión nueva del Owner encubierta? |
|---|---|---|---|---|---|---|
| `D76` | `G-3` | `INS-7 = O12` invocaba tres condiciones y ninguna fase producía dos | `INS-5` produce baseline y clasificación; el Owner aprueba | **PARCIAL**: §18 —sede canónica— **no lleva el gate ni la salida**. Ver `H-4` | F6 construye `INS-5` sin saber que tiene gate del Owner | **No.** Toma la simetría de `A3`, que `O12` ya resuelve |
| `D77` | `G-4` | doce áreas sin identificador | doce `aspecto:documental/<area>` derivados del patrón `ads:memoria` | **SÍ.** Verifiqué el patrón en `esquemas/memoria.yaml` L7 y los doce ejemplares | F6 construye doce contratos ciertos | **No.** Deriva de un patrón existente |
| `D78` | `A8` | marcador de `deriva` ilegible | `estado/deriva/<ID>.abierta` | materia de G — no la juzgo | — | no observada |
| `D79` | `A9` | `4b` sin autoridad de cierre | acto de autoridad del Owner | materia de G — no la juzgo | — | no observada |
| `D80` | `M-6` | `03-FORMAS` L551 manda al vivero todo finding | clase, forma, rama, sujeto y salida determinados | **SÍ en el contrato.** L551 es literal; nueve clases y catorce formas verificadas | **PARCIAL**: la mitad de su cierre (§17) no se hizo. Ver `H-3` | **No** |
| `D81` | `M-9` | `A3` sin contenido | las catorce preguntas del §6.2 | **SÍ.** Verbatim contra el brief L435–450, sin reordenar | F6 no inventa un gate del Owner | **No.** Transcribe la directiva |
| `D82` | `M-7` | FRENO 3 sin evaluar | N 2 · A 4 · M 2 · U 4, y el freno circuito a circuito | **SÍ en lo material.** `a.7` L549–563 verificado literal. Residuo menor: `H-17` | ninguno necesita excepción | **No**, y lo dice: la cláusula de `a.7` ya responde |
| `D83` | `M-8`≡`A11`, `F-03` | `R<n>` ×2, `N<n>` ×3 | `RC-1`–`RC-9`, `INS-0`…`INS-7` | **PARCIAL**: `D76` y `D82`, del mismo bloque, se escriben en el espacio retirado. Ver `H-7` | — | **No** |
| `D84` | `A12` | CAS frente a escritor único | materia de G — no la juzgo | — | — | no observada |
| `D85` | `A6` | recuentos del eje fase | materia de G — no la juzgo | — | — | no observada |
| `D86` | `F-05` | `C5` sin la disciplina de `C6`/`C7` | excepción nombrada en §15.7; manda `00-CIRCUITOS` | **SÍ.** `kernel/operativo/00-INDICE.md` asigna «entregas entre capacidades» a `circuitos/`, y `00-CIRCUITOS` L237–240 desactiva la obligación. Verificado | F6 crea instancias, sin decidir | **No** |

**Ninguna de las once encubre una elección que sólo el Owner pueda hacer.** Lo comprobé
caso a caso, y el más expuesto —`D76`— tiene el argumento correcto: `O12` decía qué hace
falta, y lo que faltaba era el productor. **Y donde sí había elección del Owner, F4 la
registró en vez de tomarla: `PN-13`, con sus dos salidas escritas y «elegir es del Owner».**
Eso es exactamente lo que había que hacer.

### 5.4 · Punto 4 — Quince capacidades y diez procesos, semánticamente

Derivé las quince y los diez **del corpus**, no de §17 ni de §18: quince directorios con su
`CAPACIDAD.md` y su `id:`, diez bloques `ads:proceso`. Coinciden con lo declarado.

Comprobaciones semánticas, no de recuento:

- **Toda capacidad nombrada en §8 y §18 existe**: `SIS CON VER ENT APR PRD ARQ DOM DIS SEG
  PLT INV ENC USO` en §8; `DSP` aparece en §8.0 L5461 como consumidor de la composición y
  en L5454 como quien para y escala. **Las quince quedan cubiertas.**
- **Todo proceso usado existe**: `SIS`, `AUD`, `DEU`, `DEP`. Los otros seis no se usan, y
  §18 L7690–7706 argumenta por qué. Correcto.
- **Propietarios globales**: los cuatro que §18 fija coinciden con `01-PROCESOS.md`. `AUD`
  es el único derivado y §18 no lo asigna a mano. ✔
- **Autoridad**: `a.5` L338–350 exige que el propietario global esté «en modo trabajo
  propio, nunca en modo consulta». En `A6`, `DOM` y `SEG` son propietarias globales, y
  `a.3` L185–199 admite expresamente los dos modos para cualquier capacidad. **No hay
  defecto**, aunque `DOM` y `SEG` sean «servicios» de clase.
- **Criterios de entrada y gates**: cada proceso declara `condicion_de_entrada`,
  `criterio_de_cierre` y `evidencia_necesaria`; §18 mapea gate por tramo. Comprobado.
- **Handoffs**: ver punto 5.5. **Ninguno de los cuatro macrocircuitos declara handoffs**, y
  ninguna de las diecisiete instancias nombra a `SIS` ni a `PLT`. F4 lo declara y lo remite
  a F6 con el contenido determinado (§8.0 L5470–5482). Es una remisión honesta.
- **Líderes**: §5.2 los declara aspecto a aspecto y `contrato-de-aspecto` (§5.7) los da por
  defecto. Coherente.

**Un hueco semántico que nadie ha registrado.** `b.16` L834–836 declara que `DOM` y `SEG`
participan **DOS veces**: `<CAP>:condiciones ⊳ CON` antes de construir, y
`<CAP>:revisión tras VER` después. `01-PROCESOS.md` **no instancia `:revisión` en ninguno
de los diez procesos** (`grep` sobre el fichero entero: cero apariciones), ni aparece en
`circuitos/`. Consecuencia: en `A8`, `M6`–`M7` y `U5b` —los tres tramos que escriben en las
fuentes del producto— `DOM` y `SEG` aportan condiciones y **nunca revisan lo construido**,
que es la mitad que `b.16` pone por escrito para evitar «los fallos de autorización que se
descubren en revisión». El `GATE DE COMPOSICIÓN` de §8.0 L5442 daría por completa esa
composición, porque comprueba contra los condicionales declarados y no contra `b.16`. Es
`H-5`, GRAVE, y **no está en los 43 ni en ninguna `PN`**.

### 5.5 · Punto 5 — Los catorce campos en los cuatro macrocircuitos

| campo | `N` §8.1 | `A` §8.2 | `M` §8.3 | `U` §8.4 |
|---|---|---|---|---|
| disparador | ✔ L5487 | ✔ L5637 | ✔ L5813 | ✔ L5967 |
| precondiciones | ✔ | ✔ | ✔ | ✔ |
| **proceso** | **implícito** (en `PARTICIPANTES`, «propietaria global de `proceso:SIS`») | ✔ fila `PROCESO DE CADA TRAMO` | ✔ rotulado por tramo | ✔ rotulado por tramo |
| participantes | ✔ con vía | ✔ con vía | ✔ con vía | ✔ con vía |
| LEE | ✔ | ✔ | ✔ | ✔ |
| ESCRIBE | ✔ | ✔ | ✔ | ✔ |
| estado | ✔ | ✔ | ✔ | ✔ |
| **handoffs** | **AUSENTE** | **AUSENTE** | **AUSENTE** | **AUSENTE** |
| evidencia | ✔ | ✔ | ✔ | ✔ |
| gates | ✔ | ✔ | ✔ | ✔ |
| rollback | ✔ | ✔ | ✔ | ✔ |
| reanudación | ✔ | ✔ | ✔ | ✔ |
| certificación | ✔ | ✔ | ✔ | ✔ |
| cierre | ✔ | ✔ | ✔ | ✔ |

**Doce de catorce en los cuatro.** El campo `handoffs` no existe en ninguno, y el propio
checkpoint lo admite sin darse cuenta: su lista de 30 comprobaciones dice
*«los cuatro macrocircuitos con sus **doce** campos»* (`CHECKPOINT` L1281). El contenido de
lo que viajaría entre `SIS`, `PLT` y `VER` sí está declarado en §8.0 L5470–5482 —y eso es
más de lo que había—, pero no está repartido por macrocircuito ni por fase. Es `H-13`,
MENOR: la composición no depende de la instancia, y §8.0 lo argumenta bien.

**Incoherencias de campo contra §18** (que es la sede que manda por §8.0 L5338):

1. `N`, campo `gates`: §8.1 L5521 declara **tres** —`INS-4`, **`INS-5` baseline aprobado por
   el Owner**, `INS-7`—. §18 L7672 declara **uno**: `INS-4` Operativa. Y su columna `salida`
   dice «control repo, topología, especialización y adaptadores», sin baseline ni
   clasificación de desconocidos. §18 manda; **la corrección `D76` se pierde en la sede
   canónica.** Y hay una tercera sede que también la pierde: §14 L6801 declara para el
   escenario 1 «`INS-4` Operativa, `INS-7` = `O12`». La asimetría es visible: el gate `A3`
   de la adopción **sí** está en §18 L7676. Es `H-4`, GRAVE.
2. `N`, campo `reanudación`: §8.1 L5605 declara *««Continúa» funciona desde el primer minuto
   … El recorrido se reanuda desde `INS-0`»*. §14 L6801 declara *«repetir el paso; antes de
   `INS-3` no hay estado que perder»* — que es **textualmente la formulación que §8.1 L5563
   cita como retirada**. Es `H-2`, GRAVE.

### 5.6 · Punto 6 — Documentación y diseño

- **Doce áreas con identificador**: ✔ verificado uno a uno contra `§5.18` L775–786; los doce
  slugs son distintos; el patrón se deriva de `esquemas/memoria.yaml` L7, con doce
  ejemplares reales en el corpus. **`G-4`/`D77` está cerrado y bien cerrado.**
- **`ads:memoria`**: ✔ el esquema existe, con `obligatorios: [id, nombre, capacidad, capa,
  fichero, autoridad, contiene, se_actualiza_cuando, se_consulta_en, caducidad,
  vacio_significa]`. §4.2 reparte cada exigencia contra `§5.19`/`§5.23`, que verifiqué en
  `ADS-PENDIENTES` L796 y L860. El paso de `capa` a condicional y el `plano` nuevo están
  registrados en §17 como ampliación. ✔
- **Mapa documental**: ✔ `M-2` cerrado — §1.3 **L226** tiene la fila, con autoridad
  «**nadie**: se REGENERA». Verificado.
- **`O8`**: ✔ su texto (`DECISIONES` L~294) dice «las doce áreas semánticas del §5.18,
  obligatorias como MATERIA y no como ficheros»; §4.3 lo cumple literalmente y registra la
  precisión del área 1 como `PN-12`. **Correcto y simétrico con `PN-6` y `PN-10`.**
- **Trece o catorce condicionales: TRECE.** Contadas por mí sobre `§5.18` L788–790: UX e
  investigación · dirección visual · sistema de diseño · arquitectura de datos detallada ·
  integraciones · cumplimiento regulatorio · modelo de amenazas avanzado · observabilidad ·
  continuidad · analítica · dispositivos · internacionalización · gobierno de IA = **13**.
  F4 dice TRECE en las tres sedes (L4320, L4353 y la tabla de §4.3). **`M-1` cerrado.**
- **Sistema de diseño y UI/UX**: `DIS` responde de seis aspectos separados (§5.2), lo cual
  es la corrección correcta de `H4`; `A6` los reconstruye como dos conclusiones distintas
  con `DIS` de propietaria. Coherente.
- **Despliegue, entornos, operación, seguridad**: áreas 9 y 10 con identificador; aspectos
  `calidad/ci-cd`, `calidad/despliegue`, `calidad/observabilidad` en `ENT`;
  `calidad/seguridad|privacidad|cumplimiento` en `SEG`. ✔
- **Tecnologías**: área 6 y `calidad/tecnologias`/`calidad/entorno` en `PLT`. ✔
- **Auditoría y recurrencia**: §5.3 y §5.4; la mitad normativa está en `PN-2`/`PN-3`. ✔
- **Un hueco de método**: §5.3 L4517 aplica la regla de `C1` L118 a `DSP` («la autoridad de
  un rol es SUBCONJUNTO de la de su capacidad, luego nombrar a `DSP` aquí exige una
  EXTENSIÓN DE FICHA») y **no la aplica** a §5.3 L4559, donde la campaña —una `iniciativa`
  con su gate— la abre «la capacidad RESPONSABLE del aspecto». `grep` sobre las quince
  fichas: **ninguna menciona `iniciativa` ni `campaña`**. Es `H-10`, MEDIO.

### 5.7 · Punto 7 — Adopción de PesquerApp

Leí `O15` íntegra (`DECISIONES` L346–401), sus nueve puntos.

| exigencia de `O15` | dónde la recoge F4 | ¿se cumple? |
|---|---|---|
| primera adopción REAL, PERMANENTE y COMPLETA | §8.2 nota `O15`, §18 paso 8, §19 | **SÍ**, con esas palabras |
| el control repo **nace definitivo**, no desechable | §8.2: *«no es un montaje que se tira al terminar»* | **SÍ** |
| clones/worktrees protegen las FUENTES, no hacen desechable el control repo | §8.2, punto `A1` | **SÍ**, es `O15` punto 3 literal |
| **BASE COMPLETA ACORDADA, no un MVP** | §8.2 punto 2; §18: *«el paso 8 exige la BASE COMPLETA ACORDADA de los pasos 0 a 7, y no un MVP»* | **SÍ**, y dos veces |
| lo que sólo se demuestra contra producto real se completa DURANTE | §8.2 punto 2 | **SÍ** |
| defectos entran por migración (§8.3) o actualización (§8.4), nunca rehaciendo | §8.2 punto 3 | **SÍ** |
| **NO autoriza iniciar la adopción** | §8.2 *«Esto no autoriza iniciar la adopción»*; §19 *«`O15` no la autoriza ni la programa»*; checkpoint punto 6 *«antes de iniciar PesquerApp: `O15` dice qué será cuando ocurra, no que ocurra ahora»* | **SÍ, en tres sedes** |
| no levanta las condiciones de `O14` | §8.2, explícito | **SÍ** |

**`O15` no queda convertida en MVP, prueba temporal, repo desechable ni instalación
parcial, y no autoriza el inicio actual. Punto 7 SUPERADO sin reserva.** `m-1` también:
la nota al pie reancla la cifra a once **sin reescribir la resolución**, que es exactamente
la disciplina correcta con material en voz del Owner.

### 5.8 · Punto 8 — Presiones normativas, derivadas de los identificadores

`grep '^## \`PN-'` sobre el documento devuelve **trece cabeceras**: `PN-1` … `PN-13`.
`PN-4` lleva `RETIRADA` en su propia cabecera (L7252) y `PN-5` lleva `FUSIONADA en PN-3`
(L7280). **13 − 2 = 11 vigentes**, y son exactamente `PN-1 PN-2 PN-3 PN-6 PN-7 PN-8 PN-9
PN-10 PN-11 PN-12 PN-13`. **Coincide con lo esperado y con lo declarado.**

Retirada y fusionada, comprobadas en su cuerpo y no en el resumen:
- **`PN-4`** — retirada con motivo escrito y **reinstaurable por F5** («F5 PUEDE
  reinstaurarla si el Owner prefiere…»). La retirada está argumentada por dos vías: el
  dominio de la función de iniciativa no son paquetes, y no se persiste. **Correcta.**
- **`PN-5`** — fusionada en `PN-3` porque su materia mínima es idéntica (una fila en `a.11`
  que ajuste `G03`), y `PN-3` la nombra como consecuencia con lo que bloquea escrito allí.
  **Correcta**: contarla aparte presentaría dos enmiendas donde hay una.

**`PN-13`, punto por punto:**

- **Fuente exacta**: `b.16`, filas `SIS` e `INV`. **Verificada contra `01-PROCESOS.md`
  L518–563 y L266–300, y contra `b.16` L896–897.** `SIS` tiene dos condicionales (`ENT`,
  `APR`); `INV` tiene cuatro (`CON:experimental`, `PRD`, `ARQ`, `APR`). **`DOM`, `SEG` y
  `DIS` no figuran en ninguna de las dos, ni como obligatorias ni como condicionales.**
  El hecho es exacto.
- **Contradicción que registra**: `INS-5` es «discovery de producto, dominio y diseño» antes
  del gate `INS-7` «listo para construir», y §8.0 exige vía para toda capacidad de la ruta.
  `AUD` sí las declara pero exige objeto ya existente, que en instalación nueva no lo hay.
  **La contradicción es real.**
- **Por qué no cabe en `PN-8`**: `PN-8` es `VER` ausente de la ruta `AUD` —otra fila, otra
  capacidad, otro remedio (añadir `VER` como condicional de `AUD`, o nombrar otro productor
  del dictamen)—. `PN-13` es `DOM`/`SEG`/`DIS` ausentes de `SIS` e `INV`. **No se solapan
  en fila, ni en capacidad, ni en remedio.** Comprobado leyendo los dos cuerpos: la
  distinción se sostiene.
- **Opciones que deja a F5**: dos, escritas — (a) añadir `DOM:condiciones C-DOM`,
  `SEG:condiciones C-SEG` y `DIS C-DIS` como condicionales de `SIS`, y `DOM`, `SEG`, `DIS`
  como condicionales de `INV`; (b) declarar que el discovery de dominio y diseño de un
  producto nuevo no pertenece a `INS-5` y nombrar dónde pertenece. **«Elegir es del Owner.»
  Correcto: no toma la decisión.**
- **Efecto sobre `INS-5` y `A9`**: declarado en `ALCANCE` y en `BLOQUEA`. Bloquea que
  `INS-5` abra con `DOM` y `DIS` en su ruta, y que `A9` incorpore el dictamen de `SEG` sin
  item `AUD` enlazado. **Consistente con §8.1 y §8.2, que declaran ambas ausencias en su
  sitio.**
- **Ninguna enmienda redactada**: confirmado. §16 abre con *«Aquí no se redacta ninguna
  enmienda»* y `PN-13` sólo enuncia la materia mínima. ✔
- **Defecto**: su campo `ALCANCE` (L7520–7521) **queda cortado a media frase**: *«…ni a
  `A8`, `M6`–`M7` ni `U5b`, que son `DEU` y `DEP` y también»*. Es `H-18`, MENOR — pero está
  en la única presión que esta tanda añade y que va al Owner.
- **Y el defecto de recuento**: §16 L7183 dice *«Las demás vigentes —`PN-6` a `PN-12`— son
  posteriores»*. `PN-13` falta. 3 + 7 = 10, no 11. En la misma frase que `m2` corrigió por
  este mismo motivo. Es `H-6`, MEDIO.

### 5.9 · Punto 9 — `F-08` y F5

La matriz (`CHECKPOINT` L1233) declara:
`| F-08 | MENOR | EXTERNO_CON_PROPIETARIO | el Owner · F5 | no | sí · sin PN | no | no | no | nota de vigencia sobre la materialización multirrepo |`
y §19 L7801 lo desarrolla.

**Determinación expresa:**

1. **Qué trabajo exige.** Una nota de vigencia o de sustitución en
   `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` que reconcilie
   **L597** —*«materialización física multi-repo | **ABIERTA — NO IMPLEMENTAR SIN DISEÑO
   PREVIO**»*, en su §15— con lo que `C6`, `C7` y §10 ya implementan. Verifiqué L597, y
   también L487 (*«NO IMPLEMENTAR TODAVÍA»*, §12). El texto sigue vigente y sigue diciendo
   que está abierta una cuestión que la arquitectura multirrepo aprobada ya cerró.
2. **Por qué pertenece a F5.** El fichero es material **en voz del Owner** (`O10`, `P-07`;
   su cabecera L3: *«Estado: documento de trabajo del Owner»*). Sólo el Owner lo edita, y
   la fase cuya puerta es el Owner es F5. **La asignación de fase es correcta.**
3. **Cuál es su autoridad.** El Owner, y sólo él. Declarado. **Correcto.**
4. **Dónde queda registrado.** En §19 de F4 y en la matriz del checkpoint. **En ningún
   sitio más.**
5. **¿Está cubierto por una `PN` existente?** **No.** Leí las trece cabeceras: `PN-1`
   presiona (a)/(b) vía la sección (g); `PN-2` `b.15.1`; `PN-3` `G03`; `PN-6`, `PN-10`,
   `PN-12` resoluciones del Owner `O12`/`O11`/`O8`; `PN-7` `b.14`; `PN-8` `b.16` fila `AUD`;
   `PN-9` `b.3`; `PN-11` `C7`/`E2.4`; `PN-13` `b.16` filas `SIS`/`INV`. **Ninguna alcanza a
   `ADS-IDEAS-PENDIENTES-MULTIREPO.md`.**
6. **¿Necesita `PN` propia?** Estrictamente, **no**, y el argumento de F4 es correcto: `PN`
   es presión sobre **material normativo aprobado**, y ese fichero se declara a sí mismo
   *«no es una especificación cerrada ni autoriza a implementar»*. Es la misma vara que F4
   aplica bien a `F-09`.
7. **¿Es `requiere_f5` una clasificación incorrecta?** **No lo es.** El trabajo requiere al
   Owner y no es materializable por F6.

**Pero el encargo dice: no permitir trabajo normativo sin vehículo de trazabilidad, y ahí
`F-08` falla.** El registro de entrada de F5 es §16 —«se enumera exactamente qué presiona
qué»— y `F-08` no está en él. La instrucción operativa del checkpoint, punto 4
(*«QUÉ LLEVAR AL OWNER: las **ONCE** presiones de §16»*), **no menciona `F-08`**. Y su
único registro vive en §19 de un documento que §17 L7599 declara **temporal**: *«`docs/evolucion/`
… se retira tras F6»*. Añado la asimetría: `F-07` toca el **mismo directorio**
`docs/owner/*`, y va a **F6** con propietario `SIS`; `F-08` va a **F5** con el Owner solo.
F4 argumenta que son remedios distintos —un campo frente a una nota— y es defendible, pero
el resultado es que de los dos hallazgos sobre el mismo directorio, el que llega a F5 es el
único sin vehículo en el registro de F5.

**Veredicto del punto 9:** clasificación correcta, **trazabilidad FALLIDA**. El remedio es
de una línea: nombrarlo en §16 como entrada de F5 que **no** es presión normativa, o
añadirlo al punto 4 del checkpoint. Es `H-9`, MEDIO.

### 5.10 · Punto 10 — F6

**`M-5`** — `CONTRATO_COMPLETO_PARA_F6`. Contra los ocho requisitos:

```text
contrato completo   PARCIAL. La APERTURA está completa (§5.3 L4517: DSP, sólo mecánicamente,
                    dentro de política O7 vigente, y si no hay política PROPONE y espera).
                    La CAMPAÑA nombra actor (§5.3 L4559) y NO resuelve la mitad que el
                    propio M-5 pedía: si esa apertura cabe en la autoridad de esa ficha
fichero futuro      `kernel/operativo/capacidades/DSP/CAPACIDAD.md`. Nombrado en §5.2
propietario         no nombrado explícitamente. Por el mapa de fuente única es `SIS`
entrada             política O7 vigente + celda vencida. ✔
salida              item AUD con la prioridad que la política fija. ✔
prueba              NO DECLARADA. Ningún `T<n>` se le asigna
dependencia         PN-2 y PN-3, declarada en §5.3. ✔
gate                NO DECLARADO
```

Y **`§17` no lo lleva**, pese a que §5.3 L4522 dice *«registrada abajo y en §17»*.

**`M-6`** — `CONTRATO_COMPLETO_PARA_F6`:

```text
contrato completo   SÍ, y bien: CLASE `entrada:finding-de-auditoria`, FORMA `forma:finding`,
                    RAMA antes de la cláusula de cierre, SUJETO la celda, SALIDA encuadre
                    listo-para-dsp o descarte con motivo (§5.3 L4536-4549)
fichero futuro      `entrada/01-TAXONOMIA.md`, `entrada/03-FORMAS.md`, `capacidades/ENC/`
propietario         `ENC` con `SIS`, deducible
entrada             finding con sujeto, aspecto y evidencia de una celda. ✔
salida              declarada. ✔
prueba              NO DECLARADA
dependencia         ninguna. ✔
gate                NO DECLARADO
```

**Y aquí el defecto es literal.** La condición de cierre que el propio `M-6` escribe
(doc 16 L853) es: *«Añadir `capacidades/ENC/` a la lista de extensiones de ficha de §5.2
**y a §17**»*. F4 lo añadió a §5.2 (L4476, «Son **SEIS**, no cuatro») y **no lo añadió a
§17**, cuya línea L7588 sigue diciendo verbatim lo que `M-6` citó como el defecto:
*«`+4` extensiones de ficha: `ENT`, `ARQ`, `PLT` y `SEG`»*. §16 L7576 tampoco: *«las
**cuatro** extensiones de ficha de §5.2»*. Y §8.2 L5680, escrito en esta misma tanda,
remite al lector a *«§5.2 y §17»*. **Tres sedes vigentes con dos cifras.** Es `H-3`, GRAVE.

**Los once `requiere_f6`.** Derivé la lista de la matriz: `B-2 M-5 M-6 F-01 F-02 F-04 F-05
F-06 F-07 F-10 F-11` = once. ✔ Coincide.

**¿Tendría F6 que elegir arquitectura en alguno?**

- `B-2` — **no**: F5 resuelve `PN-13`, F6 compone. Correcto.
- `M-5`, `M-6` — **no en la arquitectura**; sí quedan sin prueba y sin gate.
- `F-01` — **sí, parcialmente**: la sustitución declarada no alcanza a `b.16` L895 ni a
  `a.6` L495, que llevan la misma cadena. Ver punto 11.
- **`F-02` — SÍ, y es un defecto.** Su remedio declarado (§19 L7795) es tipar `capacidad` y
  `capacidad_productora` como `ref_a: capacidad`. Derivé los valores realmente usados en
  `01-PROCESOS.md`: además de las quince, aparecen `DOM:condiciones`, `SEG:condiciones`,
  `CON:experimental`, `ARQ:diagnostico`, `DIS/Reconstruccion` y `OWNER`. **F4 usa
  `DOM:condiciones` y `SEG:condiciones` como participantes en §8.2, §8.3, §8.4 y §18.**
  Bajo `ref_a: capacidad` estricto, la notación de la propia F4 deja de validar. El
  documento 17 `E-3` **sí** había escrito la salida (*«con sufijo `:` opcional para la
  variante declarada»*) y F4 **no la recoge**. F6 tendría que decidirlo. Es `H-8`, MEDIO.
- `F-04`, `F-06`, `F-07`, `F-10`, `F-11` — **no**: correcciones editoriales con cita
  verificada. `F-05` — **no**: `00-CIRCUITOS` L238 desactiva la obligación.

### 5.11 · Punto 11 — Los ocho externos, y `F-01`

| | propietario | fase | fichero | cambio exacto | condición de cierre | efecto F5/F6 | bloqueo | verificación mía |
|---|---|---|---|---|---|---|---|---|
| `F-01` | `SIS` | F6 | `01-PROCESOS.md` · `00-CIRCUITOS.md` | `DIS/Reconstruccion` → `DIS` | ambas sedes dicen `DIS` | F6 | «SÍ, parcialmente» | L434 y L166 **verificadas**. **La sede está incompleta** — ver abajo |
| `F-02` | `SIS` | F6 | `esquemas/proceso.yaml` | `ref_a: capacidad` | tipado | F6 | no | esquema **verificado**: `tipo: texto`, frente a `handoff.yaml` que sí usa `ref_a` |
| `F-04` | `ENC` con `SIS` | F6 | `05-ESCENARIOS.md` · `T75` | `grado_inicial: alta` | `T75` comprueba | F6 | no | L181–182 **verificadas**: `grado: media` / `grado_inicial: media` |
| `F-06` | `DIS` | F6 | `DIS-handoffs.md` | anclar `cuando` de `dis-a-ver` | anclado | F6 | no | L137 **verificada**: `cuando: "DIS cierra su capa…"`, sin estación |
| `F-07` | `SIS` con el Owner | F6 | `docs/owner/*` · `exclusiones.yaml` | campo `autoridad:` | validador lo comprueba | F6 | no | **verificado**: `grep '^autoridad:' docs/owner/*.md` → vacío |
| `F-08` | el **Owner** | **F5** | `ADS-IDEAS-PENDIENTES-MULTIREPO.md` | nota de vigencia | reconciliada | F5 | no | L597 **verificada**. **Sin vehículo — `H-9`** |
| `F-10` | `ENC` | F6 | `03-FORMAS.md` | retirar «uno por clase» | cabecera cierta | F6 | no | **verificado**: 14 formas, 9 clases. La aposición es falsa y la cifra 14 correcta |
| `F-11` | `SIS` | F6 | `05-ESCENARIOS.md` | enumerar lo que contiene | cabecera cierta | F6 | no | **verificado**: contiene `T75`–`T80` y `T154`–`T157`; la cabecera L5 dice «T75 a T84» |

**«Externo» no significa olvidado**: los ocho tienen propietario, fase, fichero, cambio y
condición de cierre en §19, y siete de las ocho citas las he comprobado en su fichero y su
línea. **Eso está bien hecho**, y lo digo porque un dictamen que sólo lista defectos no es
una medida.

**`F-01` — mi decisión, argumentada.**

Los hechos, verificados:

```text
docs/evolucion/11…md §8.2 y §18       `DIS`  `C-DIS`
kernel/…/recorrido/01-PROCESOS.md L434 `DIS/Reconstruccion`
kernel/…/circuitos/00-CIRCUITOS.md L166 `[DIS/Reconstruccion si C-DIS]`
docs/rediseno/b-RECORRIDO-APROBADA.md L895  `DIS/Reconstrucción `C-DIS``   ← (b), APROBADA
docs/rediseno/a-CAPACIDADES-APROBADA.md L495 `AUD  INV ∥ DOM ∥ SEG ∥ DIS/Reconstrucción`  ← (a), APROBADA
kernel/…/capacidades/DIS/CAPACIDAD.md L47   `DIS/Reconstruccion` es un MÉTODO de DIS
kernel/…/diseno/03-ESCALA-DE-NOVEDAD.md L136 el método de N3, y L253-263 «se calcula … en vez de elegirse»
```

**¿Permite entrar en F5, o invalida la arquitectura?**

**PERMITE ENTRAR EN F5.** Razono por qué, y declaro por delante lo que refuta mi primer
impulso: intenté sostener que `F-01` deja sin resolver la segunda mitad de `E-2` —«declarar
quién calcula las cinco variables y en qué fase»— y **no se sostiene**:
`03-ESCALA-DE-NOVEDAD.md` L251–261 ya lo resuelve, *«Todo paquete de `DIS` declara en su
checkpoint `nivel_de_novedad` … `gate:excelencia-visual` lo comprueba»*. El quién y el
cuándo existen en el kernel; F4 no tenía que escribirlos.

Y el sustituendo no cambia **quién participa**: `DIS/Reconstruccion` denota la capacidad
`DIS` operando por uno de sus seis métodos, y la condición de activación es `C-DIS` en las
dos formulaciones. **El conjunto de participantes de `A2`–`A7` es idéntico bajo las dos
lecturas**, luego la composición que §8.0 y §18 declaran es correcta. Lo que se pierde con
la forma del kernel es que la ruta **predetermina el método**, que es lo que
`03-ESCALA` prohíbe. F4 elige bien.

**Pero `F-01` como está registrado es FALLIDO, y lo digo con la misma firmeza.** Su sede
declarada nombra **dos** ficheros del kernel y **omite `b.16` L895 y `a.6` L495**, que
llevan la misma cadena y son material **APROBADO** que §17 L7585 declara *«intactas. F4 no
las toca»* y que F6 tampoco puede tocar. Si F6 ejecuta `F-01` tal como está escrito, el
kernel dirá `DIS` y su fuente normativa seguirá diciendo `DIS/Reconstrucción`: se cambia el
derivado y se deja la fuente, que es exactamente el modo de fallo que §15.7 registra para
`C7`. Y si la conclusión es que (b) también debe corregirse, entonces hay trabajo normativo
**sin `PN` y sin vehículo**, que es lo que el encargo prohíbe permitir.

**Conclusión de `F-01`:** la discrepancia **no invalida la arquitectura de composición** y
**no impide entrar en F5**; lo que está mal es el registro de su remedio, que como está
escrito **no es ejecutable**. El remedio del remedio cuesta una línea: o se añaden `b.16`
L895 y `a.6` L495 a la sede con la nota de que su corrección es de cita y no de fondo, o se
declara expresamente que `DIS/Reconstruccion` y `DIS` **designan al mismo participante** y
que lo que F6 corrige es la forma del derivado. F4 no dice ni lo uno ni lo otro.

---

## 6 · Mis filas de la matriz

| fila | causa original | texto anterior (`git show 7e99388`) | corrección vigente | decisión | sede actual | condición de cierre declarada | ¿se cumple? | veredicto |
|---|---|---|---|---|---|---|---|---|
| `B-1` | procesos incompatibles en §8.2 y §18 | §18 L6993 asignaba `proceso:INV` a `A2`–`A7`; §8.2 L5208 apoyaba `DOM/SEG/DIS` en `AUD` | `proceso:AUD` en items enlazados, uno por conclusión, propietario derivado | `D75` | §8.2 L5652 · §18 L7676 | las dos sedes coinciden y `AUD` admite los condicionales | **sí**, verificado contra L410–448 | **SUPERADA** |
| `B-2` | participantes sin vehículo | §8.1 L5090 «ARQ DOM DIS SEG según discovery», sin vía | cuatro vías + `PN-13`; ejecutor y autoridad separados | `D74`+`PN-13` | §8.0 L5322–5482 | vía declarada para cada participante | **no del todo**: la mitad `PLT` se cierra con una atribución que `C7` L83–86 y la propia §1.3 L224/§7.2/§7.6 desmienten | **FALLIDA** |
| `G-1` | `U5b` sin `SEG` ni `CON` | §18 L6999 «`ENT`, `VER`» | `SEG` y `CON` obligatorias de `DEP`; `G28` irretirable | `D75` | §18 L7682 · §8.4 | figuran como obligatorias | **sí**, coincidencia exacta con `DEP` L369–392 | **SUPERADA** |
| `G-2` | `ARQ` ausente, `CON` sin nombrar | §18, filas `A8` y `M6`–`M7` | `ARQ` vía 1 por `plan-tecnico`; `cambio-construido` de `CON` | `D75` | §18 L7678/L7679 | ambas presentes | **sí**, contra `DEU` L306–352 | **SUPERADA** |
| `G-3` | `O12` invocado y no satisfacible | §8.1 no producía baseline ni clasificación | `INS-5` los produce; el Owner aprueba | `D76` | §8.1 L5521 y su nota | el gate es satisfacible | **no en la sede canónica**: §18 L7672 no lleva ni el gate `INS-5` ni su salida, y §14 L6801 tampoco. §8.0 L5338 dice que manda §18 | **FALLIDA** |
| `G-4` | doce áreas sin identificador | §4.3 sin ids | doce `aspecto:documental/<area>` | `D77` | §4.3 | doce identificadores distintos, derivados del patrón existente | **sí**, doce derivados y únicos; patrón verificado | **SUPERADA** |
| `A4` | trazabilidad de las correcciones | §15.8 saltaba de `D63` a `D69`; cabecera «CORREGIDO DOS VECES» | bloques `D64`–`D68` y `D71`–`D86`; «nueve veces»; la tercera revisión ya no consta pendiente | §15.8 + cabecera | L7103, L7133, L12 | los bloques existen y la cifra se deriva | **parcialmente**: los bloques ✔ y «pendiente» ✔; la cifra **no** se deriva ni de su propia aposición (10–11) ni de §15.8 (12 bloques) | **FALLIDA** |
| `A10` | resumen al Owner con cifra vieja | «OCHO puntos» frente a «DIEZ» | ONCE, derivadas de §16 | §1 · §16 · §19 | L120, L7536, L7767 | la cifra es una y se deriva | **parcialmente**: el total ✔ en cuatro sedes; §16 L7183 dice «`PN-6` a `PN-12`» → 10 | **FALLIDA** |
| `M-1` | catorce condicionales frente a trece | §4.3 decía CATORCE | TRECE en las tres sedes | §4.3 | L4320, L4353, tabla | trece en todas | **sí**, contadas contra `§5.18` L788–790 | **SUPERADA** |
| `M-2` | §1.3 sin fila de mapa documental | ausente | fila con autoridad «nadie: se regenera» | §1.3 | **L226** | la fila existe | **sí** | **SUPERADA** |
| `M-3` | `U6` con dos gates distintos | §18 fijaba `U6 = O12` | revalidación del nivel vigente, no `O12` | `D75` | §18 L7684 · §8.4 | una sola formulación | **sí**, y con el argumento correcto | **SUPERADA** |
| `M-4` | resumen de `D67` desmentido por §18 | registro decía `proceso:INV` | «corregido por `D75`; el resumen decía `proceso:INV`» y `DEP` para propagar | registro `D67` | `DECISIONES` L236 | el resumen coincide con la tabla | **sí**, leído en el registro | **SUPERADA** |
| `M-5` | `APERTURA` y `CAMPAÑA` sin actor | «el sistema» | `DSP` en apertura; la capacidad líder en campaña; extensión de ficha `DSP` | §5.3 + §5.2 | L4517, L4559, L4476 | actor nombrado **y** declarado si cabe en su ficha | **no del todo**: para `DSP` sí; para la campaña **no se declara**, y ninguna ficha menciona `iniciativa`. Además §17 no lleva la extensión pese a que §5.3 L4522 dice «y en §17» | **FALLIDA** |
| `M-6` | extensión de ficha de `ENC` no registrada | §17 L6915 `+4` | clase, forma, rama, sujeto y salida; `ENC` añadida a §5.2 | `D80` | §5.3 L4536 · §5.2 L4476 | **«añadir `capacidades/ENC/` a §5.2 y a §17»** | **no**: §17 L7588 sigue diciendo `+4` con las mismas cuatro. La mitad literal de su cierre no se hizo | **FALLIDA** |
| `M-7` | FRENO 3 sin evaluar | §8 no decía cuántos items | N 2 · A 4 · M 2 · U 4, y el freno circuito a circuito | `D82` | §8.0 L5406–5436 | ninguno necesita excepción, y se demuestra | **sí**: `a.7` L549–563 verificado literal; los tres argumentos se sostienen | **SUPERADA** |
| `M-9` | `A3` sin contenido | «baseline con evidencia» | las catorce preguntas del §6.2, con grado y evidencia | `D81` | §8.2 L5756 · §15.2 | las catorce, literales y sin reordenar | **sí**, verbatim contra el brief L435–450 | **SUPERADA** |
| `m-1` | `O15` cita ocho presiones | «ocho» | nota al pie que reancla a once **sin tocar `O15`** | nota al pie | §8.2 | la resolución no se reescribe | **sí**, y es la disciplina correcta | **SUPERADA** |
| `m-2` | nota de procedencia separada | insertada tras `O16` | precede a la sección de `O16` | §2 del registro | `DECISIONES` L~297 | la nota va con su tabla | **sí** | **SUPERADA** |
| `m-3` | `calidad/observabilidad` sólo en `ENT` | — | hecho confirmado, juicio no asumido | §5.2 | §5.2 · §19 | ninguna: es preferencia de diseño | hecho verificado en `PLT/CAPACIDAD.md` (`mision` nombra «observabilidad»); F4 registra y no decide | **NO APLICABLE con causa demostrada** |
| `m-4` | `U5a` sin rotular | fila «`U5`–`U6`» | `U5a` y `U5b` como filas propias | `D75` | §18 L7681/L7682 | rotuladas | **sí** | **SUPERADA** |
| `F-01` | `DIS/Reconstruccion` en la ruta | — | §8.2 dice `DIS`; el kernel, no | externo | §19 L7794 | sustitución **exacta** en las sedes nombradas | **no**: la sede omite `b.16` L895 y `a.6` L495, aprobadas e intocables por F4 y F6 | **FALLIDA** |
| `F-02` | `capacidad` sin vocabulario | — | tipar como `ref_a: capacidad` | externo | §19 L7795 | tipado y vocabulario fijados | **no**: el remedio colisiona con `DOM:condiciones`/`SEG:condiciones` que F4 usa, y omite el matiz que `E-3` ya había escrito | **FALLIDA** |
| `F-04` | `grado_inicial` incoherente | — | `grado_inicial: alta` + `T75` | externo | §19 L7796 | comprobado por `T75` | registrado con cita verificada (L181) | **SUPERADA** (como registro) |
| `F-05` | `C5` sin excepción nombrada | — | §15.7 registra la excepción; `00-CIRCUITOS` manda | `D86` | §15.7 · §8.0 | tres condiciones cumplidas | **sí en lo material**; la columna del checkpoint dice «§8.0 declara qué **checkpoint** viaja» y §8.0 declara **qué viaja**, no el `checkpoint:` — `H-16` | **SUPERADA** |
| `F-06` | `dis-a-ver` sin anclaje | — | anclar a una estación del ciclo | externo | §19 L7798 | `cuando` anclado | registrado con cita verificada (L137) | **SUPERADA** (como registro) |
| `F-07` | autoridad del material del Owner sólo en prosa | — | campo `autoridad:` + validador | externo | §19 L7799 | campo presente y comprobado | registrado; ausencia del campo verificada | **SUPERADA** (como registro) |
| `F-08` | `IDEAS` §15 contradice lo implementado | — | nota de vigencia del Owner | externo | §19 L7801 · matriz L1233 | la nota existe | clasificación correcta; **sin vehículo en §16 ni en el punto 4 del checkpoint** | **FALLIDA** |
| `F-09` | principio provisional elevado a norma | «PRINCIPIO» sin calificar | «PROVISIONAL» conservado, con procedencia y con el `grep` sobre las 3 343 líneas | §8.4 | §8.4 L5970 | el calificativo consta | **sí**; el `grep` lo reproduje y da vacío. Cita de sección imprecisa: `H-15` | **SUPERADA** |
| `F-10` | «uno por clase de expresión» | — | retirar la aposición | externo | §19 L7802 | cabecera cierta | registrado; 14 formas y 9 clases verificadas por mí | **SUPERADA** (como registro) |
| `F-11` | «T75 a T84» | — | enumerar lo que contiene | externo | §19 L7803 | cabecera cierta | registrado; contenido real verificado | **SUPERADA** (como registro) |

**Recuento: 20 SUPERADAS · 9 FALLIDAS · 1 NO APLICABLE.**
FALLIDAS: `B-2` `G-3` `A4` `A10` `M-5` `M-6` `F-01` `F-02` `F-08`.

---

## 7 · Hallazgos nuevos

### GRAVE

**`H-1` · `PLT` no ejecuta rama, commit, push ni PR: `C7` se lo da a la capacidad con
custodia, y F4 se contradice a sí misma en tres sedes.**
`11-ARQUITECTURA-INTEGRADA.md` **L5380–5381**: *«`PLT` bajo `C7` es el caso constante:
custodia la maquinaria y **cada source change —rama, commit, push, PR y CI POR FUENTE**—»*.
`C7-GOBIERNO-GIT-MULTI-SOURCE.md` **L83–86**: rama, commit, push y PR los solicita y los
ejecuta **«la capacidad con custodia, ella misma»**; **L88–89** dan merge y convergencia a
`ENT`. `C7` **L76–77** dice que esta tabla existe justamente *«porque la responsabilidad se
reparte de forma ambigua entre `PLT`, `ENT`, `DSP` y `CON`»*. Y F4 se desmiente a sí misma:
§1.3 **L224** da el `integration-set` a `ENT`; §7.2 **L5203** escribe *«`ENT` declara
convergencia con un INTEGRATION SET»*; §7.6 **L5296** remite a `C7` sin más.
**Por qué importa materialmente.** Es el dispositivo con el que `D74` cierra la mitad `PLT`
de `B-2` —la que el revisor D del NIVEL 0 añadió como séptima capacidad—. Si la atribución
es falsa para `INS-6`, `A8`, `M6`–`M7`, esa mitad sigue abierta, y F6 materializaría el
reparto de responsabilidad Git al revés del contrato que §15.7 declara REUTILIZADO. Y no es
herencia: `git show 7e99388` demuestra que la fila `EJECUTOR` existía **sólo** en §8.3, y
que **esta tanda** la generalizó a §8.0, §8.1, §8.2, §8.4 y §18. Se propaga en L5511, L5677,
L5854, L6006, L5477 y en la columna «ejecutor y autoridad» de las diez filas de §18.

**`H-2` · §14 conserva, renombrada, la formulación que §8.1 declara retirada sobre la
reanudación de la instalación.**
§14 **L6801**, escenario 1, columna «cómo se recupera»: *«repetir el paso; **antes de
`INS-3` no hay estado que perder**»*. §8.1 **L5563–5566** la cita como el defecto que
corrige: *«F4 entregada declaraba … «REANUDACIÓN por checkpoint desde INS-3; antes,
repitiendo el paso». **Las dos frases juntas dicen que entre INS-0 y INS-3 la iniciativa no
está persistida**: vive en la conversación. Eso es exactamente lo que el apartado 19 de la
directiva prohíbe»*. En `7e99388` la línea decía «antes de **N3**»; **esta tanda la tocó
para renombrarla a `INS-3` y no vio que el enunciado estaba retirado.**
**Por qué importa.** Es la propiedad de operabilidad central —reanudar sin el chat, `R7`,
`b.14`, apartado 19 de la directiva— y hay dos contratos incompatibles vigentes sobre ella.
Es además exactamente lo que el checkpoint, punto 3, manda comprobar: *«que ninguna
afirmación vieja sobrevive sin marca de histórica»*.

**`H-3` · Las extensiones de ficha son SEIS en §5.2 y CUATRO en §16 y §17 — y §17 es la
sede que el propio texto nombra dos veces.**
§5.2 **L4476**: *«Son **SEIS**, no cuatro: las cuatro de las dos dimensiones huérfanas, más
`DSP` y `ENC` que el gate final añadió»*. §17 **L7588**: *«`+4` extensiones de ficha:
`ENT`, `ARQ`, `PLT` y `SEG`»*. §16 **L7576**: *«las **cuatro** extensiones de ficha de
§5.2»*. Y esta misma tanda añadió §5.3 **L4522** («registrada abajo y **en §17**») y §8.2
**L5680** («está en §5.2 **y §17**»), remitiendo a una sede que no las lleva.
**Por qué importa.** `M-6` escribió su condición de cierre así, textualmente (doc 16 L853):
*«Añadir `capacidades/ENC/` a la lista de extensiones de ficha de §5.2 **y a §17**»*. La
mitad no se hizo, y `M-6` y `M-5` están marcados `CONTRATO_COMPLETO_PARA_F6` con
«arquitectura corregida: sí» en la matriz. F6 que lea §17 —el inventario de migración—
construirá cuatro extensiones y `DSP` seguirá sin autorización para abrir items `AUD`, que
es exactamente el defecto que `M-5` denunció.

**`H-4` · §18, declarada sede canónica, no lleva el gate del Owner de `INS-5` que `D76`
creó, ni su salida.**
§8.0 **L5338**: *«SEDE CANÓNICA la tabla de §18 … si alguna vez difieren, **MANDA §18**»*.
§8.1 **L5521**: *«GATES `INS-4` certificación Operativa · **`INS-5` baseline aprobado por el
Owner** · `INS-7` = O12»*. §18 **L7672**, columna gate: *«`INS-4` Operativa»*, y columna
salida: *«control repo, topología, especialización y adaptadores»* — sin baseline y sin
clasificación de desconocidos críticos. La fila `INS-6`–`INS-7` declara como entrada
«especialización aprobada», no «baseline aprobado». §14 **L6801** repite la omisión.
**Por qué importa.** `G-3` es GRAVE y su cierre consiste precisamente en hacer `O12`
satisfacible. Bajo la regla de conflicto que esta misma tanda escribió, la corrección
pierde. Y la asimetría es visible: el gate `A3` **sí** está en §18 L7676, aunque `D76`
invoque la «simetría exacta con `A3`».

**`H-5` · `b.16` da a `DOM` y a `SEG` una segunda participación —revisar lo construido— que
ningún proceso instancia, y el gate de composición de §8.0 no puede verlo.**
`b-RECORRIDO-APROBADA.md` **L834–836**: *«DOM y SEG participan dos veces … `<CAP>:condiciones
⊳ CON` RESTRICCIONES ANTES de construir · **`<CAP>:revisión` tras VER revisan lo
construido**»*. `grep` sobre `01-PROCESOS.md` (564 líneas) y sobre `circuitos/`: **cero
apariciones de `:revisión`**. Los diez procesos instancian sólo `:condiciones`. F4 compone
`A8`, `M6`–`M7` y `U5b` con `DOM:condiciones` y `SEG:condiciones` y nada más (§8.2, §8.3,
§18 L7678/L7679/L7682).
**Por qué importa.** Los tres tramos donde falta la revisión son los tres que escriben en
las fuentes del producto: la retirada de `A8`, la retirada destructiva de `M6` y la
propagación de dependencia de `U5b`. `a.6` L505 lo dice para las dos mitades: *«DOM y SEG
aportan condiciones antes de construir **y revisan después**»*. El `GATE DE COMPOSICIÓN` de
§8.0 L5442 comprueba contra los condicionales declarados, no contra `b.16`, luego daría por
completa una composición a la que le falta una participación que (b) exige. **No está entre
los 43, no tiene `PN` y no está en los ocho externos.**

### MEDIO

**`H-6` · §16 L7183 enumera «`PN-6` a `PN-12`» y su propio total dice ONCE.**
*«Las demás vigentes —`PN-6` a `PN-12`— son posteriores, y el total está abajo.»*
3 + 7 = 10. `PN-13` falta, y es la que esta tanda añade. Está en la misma frase que `m2`
corrigió por este mismo motivo aritmético.

**`H-7` · `D76` y `D82`, decisiones nuevas de esta tanda, se escriben en el espacio de
nombres que `D83` —de la misma tanda— retira.**
`DECISIONES-Y-CONTRADICCIONES.md` **L258**: *«**`N5`** produce el BASELINE … `N7 = O12`»*.
**L264**: *«no hay items de producto listos antes de `N7`/`A10`»*. **L265** (`D83`): *«se
renombran **las fases**, `INS-0`…`INS-7`»*. `D16`–`D70` conservan su texto por diseño, pero
`D76` y `D82` son de este bloque. En el mismo fichero, `N4` significa el principio `N4` de
`C6` (L78) y un nivel de la escala de novedad (L265). **La prueba que `D83` declara —«ningún
identificador `<PREFIJO><n>` se usa con dos significados distintos en el corpus»— falla hoy
sobre el registro de decisiones.**

**`H-8` · El remedio declarado de `F-02` invalidaría la notación de participantes que la
propia F4 usa.**
§19 **L7795** pide tipar `capacidad` y `capacidad_productora` como `ref_a: capacidad`.
Derivé los valores usados: además de las quince, `DOM:condiciones`, `SEG:condiciones`,
`CON:experimental`, `ARQ:diagnostico`, `DIS/Reconstruccion` y `OWNER`. F4 usa
`DOM:condiciones` y `SEG:condiciones` como participantes en §8.2, §8.3, §8.4 y en §18
L7678/L7679/L7682. El documento 17 `E-3` **ya había escrito la salida** —*«con sufijo `:`
opcional para la variante declarada»*— y F4 no la recoge. F6 tendría que decidir el
vocabulario, que es lo que el nivel 3 de esta tanda dice haber eliminado.

**`H-9` · `F-08` crea trabajo de F5 sin vehículo en el registro de F5.**
El único registro es §19 **L7801** y la fila del checkpoint **L1233**. §16 —el registro de
entrada de F5— no lo menciona; el punto 4 del checkpoint (*«QUÉ LLEVAR AL OWNER: las ONCE
presiones de §16»*) tampoco; y §17 **L7599** declara `docs/evolucion/` temporal, *«se retira
tras F6»*. Detalle: `F-07` toca el mismo directorio `docs/owner/*` y va a F6.

**`H-10` · La regla de `C1` se aplica a `DSP` y no al abridor de campañas.**
§5.3 **L4517–4525** aplica `C1` L118 a `DSP` y crea su extensión de ficha. §5.3 **L4559**
dice que la campaña —*«una `iniciativa` de §3.3 con su gate»*— la abre «la capacidad
RESPONSABLE del aspecto», y no aplica la misma regla. `grep 'iniciativa\|campaña'` sobre las
quince fichas: **cero apariciones**. `M-5` pedía las dos mitades: *«Nombrar el actor de
`APERTURA` y de `CAMPAÑA`, y declarar si esa apertura cabe o no en la autoridad»*.

### MENOR

**`H-11`** · Cabecera **L12**: *«CORREGIDO NUEVE VECES: dos devoluciones independientes, una
devolución técnica, cinco comprobaciones técnicas encadenadas, la TERCERA REVISIÓN
INDEPENDIENTE y el GATE FINAL con su complemento»* → la aposición enumera 10, y §15.8 tiene
**doce** bloques de corrección (`D23`–`D33`, `D34`–`D45`, `D46`–`D51`, `D52`–`D54`,
`D55`–`D57`, `D58`–`D59`, `D60`–`D61`, `D62`, `D63`, `D64`–`D68`, `D69`–`D70`, `D71`–`D86`).
La frase dice *«El recuento se deriva de la lista de abajo y de §15.8»*, y no deriva de
ninguna de las dos. Es el mismo modo de fallo de `F-10`.

**`H-12`** · §8.0 **L5375**: *«hay **DOS** formas de estar presente que NO son participar en
la ruta»* — y los macrocircuitos usan **tres**: `EJECUTOR`, `AUTORIDAD` y `ENCUADRE`
(§8.1 L5515, §8.2 L5678). El registro de `D74` sí dice tres (*«…más el ENCUADRE previo»*).

**`H-13`** · Los cuatro macrocircuitos no declaran campo `handoffs`; el propio checkpoint
**L1281** dice *«los cuatro macrocircuitos con sus **doce** campos»*.

**`H-14`** · §8.0 **L5389–5390** describe la forma de `C5` como *«`id`, `de`, `a`, `cuando`,
`checkpoint`, `comprueba_al_recibir`»*: seis de los **once** obligatorios de
`esquemas/handoff.yaml`, sin decir que la lista es parcial. Faltan `entrega`, `rechaza_si`,
`devolucion`, `evidencia_de_devolucion` y `owner`.

**`H-15`** · §8.4 **L5970** atribuye el principio provisional a *«`ADS-IDEAS-PENDIENTES-MULTIREPO.md`
§15»*. El calificativo «Principio provisional» está en **§3, L79**; §15 (L589) lleva el
principio **sin** el calificativo. La sustancia de `F-09` es correcta; la cita, no.

**`H-16`** · La columna de cierre de `F-05` en el checkpoint **L1230** dice *«§8.0 declara
qué **checkpoint** viaja»*. §8.0 L5470–5478 declara **qué viaja** (source change, dosier,
resultado por fuente); no declara el campo `checkpoint:` de esos handoffs. §19 L7797 sí lo
dice bien: *«El QUÉ viaja ya está declarado»*.

**`H-17`** · §8.0 **L5399** afirma, dentro de la nota de `M-7`, que los cuatro macrocircuitos
*«componen **más de dos items** cada uno»*, y su propia derivación diez líneas después da
**N 2** y **M 2**.

**`H-18`** · `PN-13`, campo `ALCANCE`, **L7521**: la frase termina en *«…que son `DEU` y
`DEP` y también»* y la línea siguiente ya es otro campo. Está truncada, en la única presión
que esta tanda añade.

**`H-19`** · §14 **L6806**, escenario 6: *«quién escribe: **runtime dentro de `O7`** · `ENC`
clasifica»*, cuando §5.3 L4517 ya nombra a `DSP` como actor de la apertura. Es el residuo de
`M-5` en la sede que no se revisó.

---

## 8 · Hallazgos que intenté y NO pude reproducir

| lo que intenté sostener | por qué parecía defecto | qué lo refuta | resultado |
|---|---|---|---|
| `F-01` deja sin cerrar la segunda mitad de `E-2`: nadie declara **quién** calcula las cinco variables de la escala de novedad ni **en qué fase** | F4 sólo dice «el método lo calcula la escala de novedad», y `grep 'escala de novedad'` sobre el documento 11 no encuentra ninguna asignación | `03-ESCALA-DE-NOVEDAD.md` **L251–261**: *«Todo paquete de DIS declara en su checkpoint `nivel_de_novedad` … `gate:excelencia-visual` lo comprueba en su comprobación `nivel-declarado`»*. El quién y el cuándo ya están en el kernel | **NO REPRODUCIDO.** Lo declaro por delante porque refuta mi propio hallazgo |
| `D74` subcuenta el hueco de `B-2`: dice «**cinco** capacidades», el documento 16 dice «las **seis**» y el 17 añade `PLT` como séptima | tres cifras distintas para el mismo hueco | Bajo la resolución de F4 las siete se reparten así: `ENC` sale por `ENCUADRE`, `PLT` por `EJECUTOR`, y quedan `PRD ARQ DOM DIS SEG` = **cinco** sin vía. La cifra es coherente con su propia resolución | **NO REPRODUCIDO como error de recuento.** El defecto real está en el `EJECUTOR`, y es `H-1` |
| §8.0 no puede invocar `b.1` para exigir dos items, porque `b.1` L57 dice que la regla *«**no** limita qué capacidades puede activar una ruta»* | parecía que la premisa de la vía 4 se caía | Lo que limita las capacidades es `b.16`, no `b.1`; §8.0 usa `b.1` sólo para negar que quepan **dos procesos en un item**, que es lo que `b.1` L49 dice literalmente. El razonamiento es correcto | **NO REPRODUCIDO** |
| `DOM` y `SEG` son «servicios» en `a.3` y no podrían ser propietarias globales de los items `AUD` de `A6` | `a.3` L176 los agrupa bajo «se consultan sin tomar custodia» | `a.3` **L185–199**: *«"Estación" y "servicio" describen el modo habitual … Cualquier capacidad opera en dos modos … MODO trabajo propio recibe un paquete hijo sustantivo, CON custodia»*, y `a.5` sólo exige que el propietario global esté en modo trabajo propio | **NO REPRODUCIDO** |
| §8.0 dice «siete de las diecisiete instancias disparan sobre `C-<CAP>`»; yo conté ocho | discrepancia derivada | La octava (`DIS-handoffs` L80) formula el criterio en negación: *«…o el item **no** cumple `C-ARQ`»*. Bajo la lectura de «dispara sobre el criterio», siete es defendible | **NO REPRODUCIDO** |
| El «`PLT` sin vehículo» que el revisor D añadió seguiría abierto en `INS-0` y `INS-2` | `PLT` no es obligatoria ni condicional de `proceso:SIS` | `C7` **L82**: *«materializar una fuente | la solicita `DSP` al despachar | **la ejecuta `PLT`** | la verifica `gate:workspace-conforme`»*, y **L92** para retirar ramas. Ahí `PLT` es ejecutor **con gate propio**, fuera de la ruta, y F4 acierta | **NO REPRODUCIDO para `INS-0`/`INS-2`.** Sí reproducido para `INS-6`, `A8`, `M6`–`M7`: es `H-1` |

---

## 9 · Limitaciones de mi revisión, sin adorno

1. **No leí íntegro el documento 11**, que es el objeto. Leí completos §0, §1, §4, §5, §7,
   §8, §13, §14, §15.2–§15.8, §16, §17, §18 y §19, y parcialmente §3, §6 y §9. **No leí §2
   (el protocolo transaccional, ~2 700 líneas), ni §10, §11 ni §12.** Es materia declarada
   del REVISOR G, y esa división la impuso el encargo; pero significa que **cualquier
   contradicción entre §2/§10/§11/§12 y mi materia se me ha escapado**, y una de mis
   comprobaciones —que la reanudación de `U5b` se apoya en `INTEGRACIÓN PARCIAL`— toca ese
   límite.
2. **No leí `15-TERCERA-REVISION-INDEPENDIENTE-F4C.md`** (651 líneas), pese a estar entre
   las fuentes obligatorias. Mi juicio sobre `D64`–`D68` se apoya sólo en cómo el documento
   11 y el registro de decisiones los describen, no en el juicio original.
3. **No leí `a-ENMIENDA-E1-ENC.md`** (211 líneas). Lo que digo sobre `ENC` —que sus cuatro
   entradas están ancladas al Owner, y la extensión que `M-6` exige— procede de la ficha y
   de las citas de los documentos 16 y 17, no de `E1`.
4. **No leí trece de las quince fichas de capacidad íntegras.** Derivé `clase`, `metodos`,
   `mision` y parte de `autoridad` por `grep`. Si alguna de las trece contiene una
   autorización que refute `H-10` o mi lectura de `M-5`, no la habría visto. Sí comprobé
   con `grep` sobre las quince que **ninguna menciona `iniciativa` ni `campaña`**.
5. **No leí `C2`, `C3`, `C4`, `C6`, `00-OBLIGACIONES-Y-CIERRE.md`, cuatro de los seis
   ficheros de `diseno/`, ni cuatro de los seis de `entrada/`.** De `C7` leí la tabla de
   propiedad y su contexto, no las 250 líneas.
6. **De los documentos 16 y 17 leí los hallazgos de mi materia, no los dictámenes
   completos.** No he verificado la aritmética interna del gate (`F-12`).
7. **Nada de lo que digo está ejecutado.** No corrí validadores, no ejecuté pruebas, no
   probé un solo escenario. Como el propio documento admite, todo esto es contrato
   definido, y mi revisión es lectura contra lectura.
8. **`H-5` es un hallazgo sobre material aprobado ((b) L834–836) que ningún revisor
   anterior tocó.** Puede que exista una lectura en la que `<CAP>:revisión` sea ilustrativo
   y no exigible; no la encontré, pero no leí `b.3` ni `b.5` completos, donde podría estar.

---

## 10 · Recomendación de veredicto

# INSUFICIENTE PARA F5

**En una frase:** en mi materia la tanda cierra bien lo estructural —`B-1`, `G-1`, `G-2`,
`G-4`, `M-7`, `M-9`, `O15` y las cuatro vías de composición resisten abrirse contra
`01-PROCESOS.md`, `b.16`, `a.5`, `a.7` y `C5`—, pero **dos de los cuarenta y tres (`M-5` y
`M-6`) tienen su condición de cierre literalmente incumplida en la sede que ellos mismos
nombran, un GRAVE (`G-3`) se pierde en la sede que esta misma tanda declaró canónica, el
dispositivo con el que `D74` cierra la mitad `PLT` del bloqueante `B-2` contradice la tabla
de propiedad de `C7` y las propias §1.3, §7.2 y §7.6, y §14 conserva —renombrada por esta
tanda— la afirmación sobre la reanudación que §8.1 declara retirada**: son cinco defectos
GRAVES, cuatro de ellos introducidos o dejados pasar por la corrección misma, que es el
octavo encadenamiento consecutivo y la razón por la que estas revisiones se encadenan.

**Lo que sí está bien, y hay que decirlo.** La sede canónica de composición de ruta es una
pieza sólida y necesaria: las cuatro vías se comprueban una a una contra el corpus y
resisten; el gate de composición y el error `composicion-incompleta` son declaraciones
verificables; `PN-13` es un hallazgo real, correctamente derivado de `b.16`, con dos salidas
escritas y sin tomar la decisión del Owner; las doce áreas documentales y sus identificadores
son exactos contra `§5.18`; las catorce preguntas de `A3` son el §6.2 del brief, literales;
el análisis del FRENO 3 circuito a circuito es correcto contra `a.7`; y `O15` se respeta en
sus nueve puntos, incluido el que dice que no autoriza empezar. **Ninguno de mis nueve
FALLIDOS exige una decisión de diseño nueva**: los nueve tienen remedio determinado, y ocho
de ellos caben en menos de una página. Lo que no puede hacerse es darlos por cerrados.

---

# ADJUDICACIÓN DEL ADJUDICADOR I

# ADJUDICACIÓN DEL ADJUDICADOR I — GATE DE CIERRE INDEPENDIENTE DE `F4c`

---

## 1 · Identidad y procedencia

```text
REPOSITORIO      /home/jose/ads-kernel
RAMA             redesign/kernel-2.0
HEAD             0a4b3a08ee5b0d0f896c82a892ec8ea15383fc05   (git rev-parse, verificado)
ÁRBOL            limpio (git status --porcelain vacío)
RANGO OBJETO     7e99388557323c1e0933ff5f2bd9bc5b2fc5708a..0a4b3a08ee5b0d0f896c82a892ec8ea15383fc05
                 OCHO commits, verificados con git log --oneline
MODO             SÓLO LECTURA. No he modificado ningún fichero del repositorio, no he hecho
                 ningún commit y no he ejecutado ninguna escritura de git
```

**Qué NO soy.** No escribí `F4`, `F4b` ni `F4c`. No apliqué ninguna corrección. No participé
en ninguna decisión `D16`–`D86` ni en ninguna resolución `O1`–`O16`. No fui revisor A, B, C,
D, E ni F de los documentos 16 y 17, ni revisor G ni H de éste. **Emito el único veredicto.**

**Cómo he trabajado.** No resuelvo por mayoría ni por autoridad. Cada afirmación material de
`G` y de `H` la he abierto en su fichero y su línea. Corrijo a `G` en cinco puntos, corrijo a
`H` en ocho, rechazo una pieza de `H`, y añado tres hallazgos que ninguno de los dos vio.
Ninguna cifra de esta adjudicación está copiada: todas están derivadas.

---

## 2 · Qué recibí y qué leí

Recibí los dos dictámenes ya cerrados y los leí **enteros**:

- `dictamen-G.md` · 1281 líneas · protocolo, estado, transacciones, recuperación, Git, tipos
  y fuentes de verdad · 13 filas de la matriz · 10 hallazgos nuevos · recomienda
  **INSUFICIENTE PARA F5**.
- `dictamen-H.md` · 962 líneas · capacidades, procesos, composición de rutas, handoffs,
  macrocircuitos, documentación, adopción, F5/F6, externos · 30 filas de la matriz ·
  19 hallazgos nuevos · recomienda **INSUFICIENTE PARA F5**.

**Qué verifiqué yo, por muestreo dirigido a los puntos donde la lectura tenía que morder.**
Cada uno de los siguientes lo abrí en su fichero:

| qué comprobé | dónde | resultado |
|---|---|---|
| la matriz de los 43, derivada por identificadores | `CHECKPOINT` L1185–1245 | **43 ids distintos · un estado primario cada uno · 31·1·2·8·1 = 43** |
| `A7` — el texto vigente frente al texto base | `11-ARQ:2038-2040` vs `11-base:1916-1918` | **byte a byte idéntico** |
| los cinco conceptos, en la fuente aprobada | `a-CAPACIDADES-APROBADA.md:671-679` | **`ACTOR ATRIBUIDO` no está en esa lista**: está en L665, otra |
| `A8` — la regla que el lector ejecuta | `11-ARQ:1450-1453` vs `11-base:1374-1377` | **`diff` vacío: idéntica** |
| `estado/deriva/` en todo el corpus | `grep` sobre `11-ARQ` | **DOS apariciones**: L1488 y el registro `D78` L7150 |
| `estado/cuarentena/` en base y en HEAD | `grep -in` sobre ambos | base **1** (la descartada); HEAD **4**, tres nuevas |
| las dos reglas retiradas del validador | `11-ARQ:3925` y `:3945-3947` | **presentes**, y `11-base:3777`/`:3797` idénticas |
| el censo de `abierta(tx)` | `grep` + límites de sección | **siete citas reales**, dos mal nombradas y dos omitidas |
| la tabla de propiedad de `C7` | `C7:80-92` | **rama · commit · push · PR → «la capacidad con custodia, ella misma»** |
| la fila `EJECUTOR` en base y en HEAD | `git show` + `grep` | base **1** (§8.3 L5310); HEAD **5** (§8.0/§8.1/§8.2/§8.3/§8.4) + §18 |
| §14 escenario 1 en base y en HEAD | `11-base:6233` vs `11-ARQ:6801` | **la tanda tocó la celda**: `N3` → `INS-3`, sustancia intacta |
| las extensiones de ficha | `11-ARQ:4475` · `:7576` · `:7588` | **SEIS · CUATRO · CUATRO** |
| §18, fila `INS-0`–`INS-5`, columnas gate y salida | `11-ARQ:7672` | **sin el gate `INS-5` y sin baseline en la salida** |
| `<CAP>:revisión` | `b.16:834-836` + `grep -rn` sobre `kernel/` | **cero instancias** |
| `D77` en el registro de decisiones | `DECISIONES:259` | **«las CATORCE condicionales»** — hallazgo mío |
| qué filas `D16`–`D70` tocó el rango | `git diff` sobre `DECISIONES` | **`D67`**, en el mismo commit que declara que no se tocan — hallazgo mío |
| los recuentos de §3.6 y §3.8 | conteo propio | **42/42 · 34 · 20 · 54 · 19 · 25**, todos cuadran |
| `D1`–`D86` y `O1`–`O16` | `grep` sobre el registro | **sin hueco, los dos** |
| documentos 15, 16 y 17 | `git diff --name-only` del rango | **no aparecen: intactos** |
| los validadores | ejecución real, sólo lectura | `comprobar_recuentos` **en verde**; `T159` y `T148` **FALLIDAS** |

---

## 3 · Método de verificación — comandos exactos

```bash
git rev-parse HEAD                                       # 0a4b3a0…
git status --porcelain                                   # vacío
git log --oneline 7e99388..0a4b3a0                       # 8 commits
git diff --stat  7e99388..0a4b3a0                        # 4 ficheros · 1128+/213-
git diff --name-only 7e99388..0a4b3a0                    # 00-INDICE · 11-ARQ · CHECKPOINT · DECISIONES

# ── la matriz de 43, DERIVADA por identificadores y no copiada ───────────────
awk 'NR>=1185 && NR<=1245 && /^\| `/' CHECKPOINT-ADS-NEXT.md \
  | sed 's/^| `\([^`]*\)` | \([A-Z]*\) | \*\*`\([A-Z_0-9]*\)`\*\* |.*/\1\t\2\t\3/'
cut -f1 | sort | uniq -d          # vacío  → 43 ids DISTINTOS
cut -f3 | sort | uniq -c          # 31 · 1 · 2 · 8 · 1
cut -f2 | sort | uniq -c          # 4 · 6 · 20 · 13   (13 MENOR distintos; A11 es la 14ª fila)

# ── cobertura: reparto G/H frente al inventario obligatorio ──────────────────
comm -23 <ids de las 43> <ids adjudicados por G y H>     # vacío: 0 sin asignar
comm -12 <lista G> <lista H>                             # vacío: 0 solapes reales

# ── texto vigente contra texto base ──────────────────────────────────────────
git show 7e99388:docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | sed -n '1914,1920p'
diff <(git show 7e99388:…11-ARQ… | sed -n '1374,1377p') <(sed -n '1450,1453p' …11-ARQ…)
git show 7e99388:…11-ARQ… | grep -in 'cuarentena'        # 1 sola línea: la descartada
git show 7e99388:…11-ARQ… | grep -n  'EJECUTOR'          # 5310 y ninguna más en §8

# ── censos, enumeraciones y espacios de nombres ──────────────────────────────
grep -n 'abierta(tx)'                    …11-ARQ…        # 496 1061 1220 1501 2313 2647 5253
grep -n '^### 2\.6\.'                    …11-ARQ…        # límites de sección
grep -n 'CINCO conceptos\|cinco CAMPOS'  …11-ARQ…
grep -n 'estado/deriva\|estado/tx'       …11-ARQ…
grep -on '`N[0-7]`'                      …11-ARQ…        # 5, todas citas de C6
grep -n '^## `PN-'                       …11-ARQ…        # 13 cabeceras; −RETIRADA −FUSIONADA = 11
grep -o 'aspecto:documental/[a-z-]*'     …11-ARQ… | sort -u   # 12
grep -o '^| D[0-9]* ' DECISIONES.md | tr -d '| ' | sort -V     # D1…D86 sin hueco
grep -rn ':revisi' kernel/operativo/                     # vacío
grep -c '^id: forma:'   entrada/03-FORMAS.md             # 14
grep -c '^id: entrada:' entrada/01-TAXONOMIA.md          # 9
ls kernel/operativo/esquemas/*.yaml | wc -l              # 19

# ── ejecución real, sólo lectura ─────────────────────────────────────────────
timeout 25 python3 kernel/operativo/validadores/comprobar_recuentos.py   # 1/0
timeout 25 python3 kernel/operativo/validadores/comprobar_fuentes.py     # T159 FALLIDA
timeout 25 python3 kernel/operativo/validadores/comprobar_arranque.py    # T148 FALLIDA
python3 -V                                                                # 3.10.12
```

---

## 4 · Cobertura del corpus

El inventario obligatorio son **56 fuentes, 31 517 líneas**
(`scratchpad/inventario-18.md`, derivado de los documentos 16 y 17). Punto por punto:

### 4.1 · Cero fuentes sin asignar — **CUMPLE**

Las 56 filas del inventario llevan revisor (`G`, `H` o `G+H`). Y las 43 filas de la matriz
están todas adjudicadas: `comm -23` entre los 43 ids y la unión de las listas de `G` y `H`
devuelve **vacío**.

**Corrijo el encargo en un punto de hecho:** dice que «algunas se solapan». **No se solapa
ninguna.** `comm -12` entre las trece de `G` y las treinta de `H` devuelve **vacío**: 13 + 30
= 43, partición exacta. No hay ninguna discrepancia de adjudicación de fila que resolver por
solape; las discrepancias que resuelvo abajo son de otra clase.

> **Advertencia de espacio de nombres, y es de los dictámenes, no del entregable.** `G` numera
> sus hallazgos nuevos `G-1`, `G-2`, `G-3` — **que son también los identificadores de tres
> filas de la matriz**, adjudicadas por `H`. Renumero todo a `I-nn` para que nadie los
> confunda, y cuando escribo `G-1`, `G-2`, `G-3` sin más me refiero **a las filas de la
> matriz**.

### 4.2 · Cero fuentes declaradas como leídas sin evidencia — **CUMPLE**

Ni `G` ni `H` declaran leída ninguna fuente que no acompañen de cita o de recuento derivado.
Los dos declaran por delante lo que **no** leyeron, con nombre. Esto lo digo en su favor: la
honestidad de las dos secciones de limitaciones es lo que me permite auditar la cobertura.

### 4.3 · Las diecinueve que el primer gate omitió — **NO CUMPLE**

Las diecinueve están enumeradas en el documento 17 L101–130. Contrastadas contra lo que `G` y
`H` declaran haber leído:

```text
CUBIERTAS · 9    DIS-handoffs · handoffs-generales · diseno/03-ESCALA-DE-NOVEDAD ·
                 C1 · C5 (íntegro) · owner/ARQUITECTURA-MULTIREPO · owner/IDEAS-PENDIENTES ·
                 entrada/03-FORMAS · entrada/05-ESCENARIOS

NO CUBIERTAS · 10  diseno/00-SISTEMA-DE-EXCELENCIA  (H: «NO LEÍDO», sólo L110)
                   diseno/01-MEMORIA-DE-DISENO      (H: «NO LEÍDO»)
                   diseno/02-RUBRICAS               (H: «NO LEÍDO»)
                   diseno/04-CICLO-DE-CALIDAD       (H: «NO LEÍDO»)
                   diseno/05-FIDELIDAD              (H: «NO LEÍDO»)
                   C2-AGENTES-Y-MODELOS             (H: «NO LEÍDO»)  539 líneas
                   C3-METODO-EJECUTABLE             (H: «NO LEÍDO»)
                   entrada/00-INDICE                (H: «NO LEÍDO»)
                   entrada/02-CIRCUITO              (H: «NO LEÍDO»)
                   entrada/04-INCERTIDUMBRE         (H: «NO LEÍDO»)
```

**Diez de las diecinueve no están cubiertas.** Son exactamente las que el primer gate omitió
y que el complemento tuvo que leer íntegras para encontrar `E-1`…`E-10`.

### 4.4 · Fuentes obligatorias sin ninguna lectura sustantiva — **NO CUMPLE**

Además de las diez anteriores:

```text
15-TERCERA-REVISION-INDEPENDIENTE-F4C.md   652 líneas   asignada a G+H   NINGUNO LA LEYÓ
   G  «NO he leído `15-…` íntegro: verifiqué su contenido a través de las citas del
       documento 16 y del registro de decisiones»
   H  tabla de corpus, fila 5: «**NO LEÍDO**»
C4-MATERIALIZACION.md                      170 líneas   H: «NO LEÍDO»
a-ENMIENDA-E1-ENC.md                       211 líneas   H: «NO LEÍDO»
a-ENMIENDA-E2-MULTIREPO.md                 230 líneas   G: barrido; «Declarado: no lo cubrí»
```

**El documento 15 está asignado a los dos revisores y no lo abrió ninguno.** Es la TERCERA
REVISIÓN INDEPENDIENTE: la fuente donde vive la causa original de `D64`–`D68`, que es la
decisión de la que cuelgan `A1`, `A2`, `A6`, `A8`, `A9` y las nueve ventanas de `M-8`. `H`
lo declara en su limitación 2: *«Mi juicio sobre `D64`–`D68` se apoya sólo en cómo el
documento 11 y el registro de decisiones los describen, no en el juicio original.»* Es decir:
**el objeto se juzgó por su propia descripción de la fuente.**

**Recuento derivado por mí: catorce fuentes obligatorias, 3 420 líneas, sin ninguna lectura
sustantiva** — el 10,9 % del corpus obligatorio.

A eso se añade que **trece de las quince fichas de capacidad** no se leyeron íntegras: `H`
derivó `clase`, `metodos`, `mision` y parte de `autoridad` por `grep`, y leyó de verdad sólo
`PLT` y `DSP`. `grep` sobre un campo no demuestra que otro campo del mismo fichero no lo
contradiga, y `H` lo dice: *«Si alguna de las trece contiene una autorización que refute
`H-10` o mi lectura de `M-5`, no la habría visto.»*

### 4.5 · Las quince capacidades — **CUBIERTAS, con reserva de método**

Existencia y atributos derivados por `H` con `ls` y `grep` sobre los quince `CAPACIDAD.md`, y
lo reproduje: quince directorios, quince ficheros, quince `id:`. Coincide con §18 L7666–7668.
La cobertura es **de recuento y de atributos**, no de lectura íntegra en trece de ellas.

### 4.6 · Los diez procesos — **CUBIERTOS**

Derivados por `H` de `01-PROCESOS.md` y reproducidos por mí:

```text
grep -n 'propietario_global' kernel/operativo/recorrido/01-PROCESOS.md   → 10 bloques
L35 PRD · L95 PRD · L154 «ARQ cuando C-ARQ … CON en caso contrario» · L202 ENT ·
L275 INV · L312 ARQ · L368 PLT · L419 DERIVADO … NUNCA se asigna a mano ·
L458 «la capacidad PROPIETARIA de la decisión … NUNCA lo elige DSP» · L527 SIS
```

Los cuatro que §18 fija —`SIS`→`SIS`, `INV`→`INV`, `DEU`→`ARQ`, `DEP`→`PLT`— coinciden, y
`AUD` es el único derivado. **Verificado por mí, línea a línea.**

### 4.7 · `C1`–`C7` — **NO CUBIERTOS**

`C1` parcial (`H`) · `C2` **no leído** · `C3` **no leído** · `C4` **no leído** · `C5` íntegro
(`H`) · `C6` parcial (`G`) · `C7` parcial (`G` y `H`, y en `H` es la tabla que sostiene su
hallazgo más fuerte). **Tres de siete contratos sin abrir.**

### 4.8 · Handoffs, circuitos, `diseno/`, `entrada/`, `docs/owner/`, packs, tooling, pruebas

```text
handoffs      CUBIERTOS   17 instancias derivadas por H con `grep -h '^de:\|^a:' | paste`
circuitos     CUBIERTOS   DIS-handoffs y handoffs-generales, parciales; 00-CIRCUITOS abierto
diseno/       NO CUBIERTO 5 de 6 ficheros sin leer
entrada/      PARCIAL     3 de 6 sin leer (00, 02, 04)
docs/owner/   PARCIAL     los dos abiertos por barrido dirigido, con cita verificada
packs/        NO EN EL INVENTARIO OBLIGATORIO. G ejecutó `comprobar_packs`: verde
tooling/      NO EN EL INVENTARIO OBLIGATORIO
pruebas       PARCIAL     G ejecutó los validadores; yo reproduje tres. `T148` y `T159` fallan
```

### 4.9 · `evento.yaml`

Comprobado con `ls`: **no existe**. Conforme al encargo, no lo cuento como hueco. §3.6 es su
contrato, y el recuento de §3.8 —19 + 4 + 2 = 25— es consistente con que no exista todavía:
`evento` está entre los cuatro tipos nuevos, no entre los diecinueve esquemas vigentes.

### 4.10 · Veredicto de la cobertura

**NO CUMPLE.** Catorce fuentes obligatorias sin lectura sustantiva, diez de ellas entre las
diecinueve que el primer gate ya había omitido una vez, y una —el documento 15— asignada a
los dos revisores y leída por ninguno. Por la regla del encargo, **esto basta por sí solo
para el resultado**, y lo consigno antes de entrar en el fondo para que quede claro que el
fondo no lo rescata.

---

## 5 · La matriz de las 43 filas

### 5.1 · La derivación, hecha por mí

Extraje los identificadores de la tabla del checkpoint sin copiar ningún total:

```text
43 filas · 43 ids DISTINTOS (uniq -d vacío)
A11 NO aparece: absorbido en `M-8`          ← comprobado con grep sobre la tabla
A14 NO aparece: declarado ajeno a F4         ← ídem
ESTADO PRIMARIO, exactamente uno por id      ← la extracción falla si hay dos, y no falló

  CORREGIDO_EN_F4            31
  PRESION_LISTA_PARA_F5       1
  CONTRATO_COMPLETO_PARA_F6   2
  EXTERNO_CON_PROPIETARIO     8
  HISTORICO_NO_APLICABLE      1
                            ───
                             43

POR SEVERIDAD   BLOQUEANTE 4 · GRAVE 6 · MEDIO 20 · MENOR 13 distintos
                (`A11` es la 14ª fila MENOR, absorbida: 44 filas · 43 distintos)
```

**Mi derivación coincide exactamente con la cifra publicada.** La reconciliación que el
octavo commit hizo —retirar los estados compuestos de `B-2`, `M-5` y `M-6`, que producían
46— **es correcta y está bien argumentada**. Lo digo porque es la única cifra del entregable
que el encargo me pidió desconfiar por nombre y **resiste**.

### 5.2 · Tabla completa

Leyenda de la columna «antes»: **G**/**H** = quién la adjudicó, seguido de su resultado.
`=` significa que coincido; `≠` que le corrijo.

| id | sev | estado primario declarado | **mi resultado** | prueba | antes |
|---|---|---|---|---|---|
| `A1` | BLOQ | `CORREGIDO_EN_F4` | **SUPERADA** | enum de tres valores con sede única en §3.6 L3806, y las otras dos sedes que lo gobiernan —L3768-3769 y la capa A L3878-3883— dicen lo mismo con la condicional correcta; §2.6.11 L2331-2333 se autodeclara GLOSA con regla de desempate | G SUPERADA `=` |
| `A2` | BLOQ | `CORREGIDO_EN_F4` | **FALLIDA** | la condición publicada es «las siete sedes remiten». **Dos de las siete no citan el predicado** (§2.6.4, §2.6.9, barrido acotado) y **dos que sí lo citan no están en el censo** (§2.6.5 L1061, §2.6.11 L2313); §2.6.4 L894 **redeclara** con la formulación retirada; y `11-ARQ:3925` sigue vigente: «TERMINALIDAD: exactamente un `derivada` por transacción cerrada» — **la afirmación exacta que era la causa de `A2`, en la capa que `D71` L616-619 designa evaluadora del predicado** | G SUPERADA con reserva `≠` |
| `A3` | GRAVE | `CORREGIDO_EN_F4` | **SUPERADA** | §7.4 L5253-5262 reescrito con las dos ramas y el predicado; §16 L7546-7548 alineado con `PN-7`. `grep 'elimina el ramal'` → **dos apariciones, las dos en nota de corrección o en el registro `D73`**; ninguna sede vigente | G SUPERADA `=` |
| `A4` | GRAVE | `CORREGIDO_EN_F4` | **FALLIDA** | la condición incluye literalmente «nueve veces». La cabecera L12 dice «El recuento se deriva de la lista de abajo y de §15.8», y **no deriva de ninguna de las dos**: §15.8 tiene **DOCE** bloques de corrección (`D23`–`D33`, `D34`–`D45`, `D46`–`D51`, `D52`–`D54`, `D55`–`D57`, `D58`–`D59`, `D60`–`D61`, `D62`, `D63`, `D64`–`D68`, `D69`–`D70`, `D71`–`D86`), y la aposición de la propia frase **omite `D69`–`D70`** y dice «cinco comprobaciones técnicas» donde §15.8 rotula hasta la **SEXTA**. Los bloques sí existen y «pendiente» sí se retiró; la cifra no | H FALLIDA `=` |
| `A5` | MEDIO | `CORREGIDO_EN_F4` | **SUPERADA** | L1735-1741: sujeto corregido a FICHEROS CANÓNICOS, `preparada` conserva sus hashes con motivo escrito, la confusión se nombra y se prohíbe; §2.3 L392-393 intacto | G SUPERADA `=` |
| `A6` | MEDIO | `CORREGIDO_EN_F4` | **SUPERADA** | 5 fases · 6 estados · 7 filas, los tres derivados por mí sobre L3714-3722 y la tabla L3801-3807. `grep 'seis fases'` → sólo L575, L3466-3467 (notas de corrección) y el registro `D52`/`D57`, texto `D16`–`D70` | G SUPERADA `=` |
| `A7` | MEDIO | `CORREGIDO_EN_F4` | **FALLIDA** | `11-ARQ:2038-2040` es **byte a byte idéntico** a `11-base:1916-1918`: «los CINCO conceptos de `a.9`: ordenante · autoridad · escritor_del_comando · ejecutor · **actor_atribuido**», y L2040 lo hace **condición de validación**. La fuente aprobada lo desmiente: `a-CAPACIDADES-APROBADA.md:671-679` enumera PROPIETARIO DEL CAMPO · AUTORIDAD · ORDENANTE · ESCRITOR DEL COMANDO · EJECUTOR DE MUTACIÓN, y L665 pone `ACTOR ATRIBUIDO` en **otra** lista. El documento sabe escribirlo bien: L1214, L1360, L2915, L3386 y L3801 lo dicen correctamente. **La única sede que el gate nombró es la única que no se tocó** | G FALLIDA `=` |
| `A8` | MEDIO | `CORREGIDO_EN_F4` | **FALLIDA** | (i) la norma que el lector ejecuta —L1450-1453— es **`diff`-idéntica a `11-base:1374-1377`**: sigue mandando mirar «los eventos `deriva` SIN REPARAR del diario»; el marcador se explica debajo, no se normativiza. (ii) la condición exigía «sujeto a la misma disciplina que el marcador»: el de `estado/tx/` tiene cinco piezas —clasificación §2.4 L433-440, excepción de ruta L417-418, `.gitignore` L445 y L1316, fila de reconstrucción §2.9 L2647, `X27` L1356— y `estado/deriva/` **no tiene ninguna**; §2.6.9 paso E L1718-1722 no lo crea | G FALLIDA `=` |
| `A9` | MEDIO | `CORREGIDO_EN_F4` | **SUPERADA** | L1958-1976: los dos actos de autoridad escritos y atribuidos; `X58` L1372 reformulado a «no por construcción: el grafo no la cierra sola». La cuarentena que la vía (i) introduce es hallazgo nuevo (`I-01`), no parte de `A9` | G SUPERADA `=` |
| `A10` | MEDIO | `CORREGIDO_EN_F4` | **SUPERADA** | la condición es «ONCE puntos de presión, derivados de §16». Derivé: `grep '^## \`PN-'` → **13 cabeceras**, `PN-4` RETIRADA (L7252), `PN-5` FUSIONADA (L7280) → **11**, y el total dice ONCE en **cuatro** sedes: L123, L5742, L7540, L7763. La frase defectuosa de §16 L7184 es un hallazgo aparte (`I-11`), no la condición | H FALLIDA `≠` |
| `A12` | MENOR | `CORREGIDO_EN_F4` | **SUPERADA** | `grep 'único escritor'` sobre `11-ARQ` → **L2166 y nada más**, y es la línea que lo retira. La única aparición restante del corpus es `DECISIONES:234` (`D65`), texto histórico que `D84` (L266) declara revisado. El argumento sustituto —el CAS— es correcto: el lock de `R5` es `.ads/run/lock` y §2.7 L2409-2412 declara que no viaja | G SUPERADA `=` |
| `A13` | MEDIO | `CORREGIDO_EN_F4` | **SUPERADA** | §3.6 L3801 usa «los CINCO CAMPOS de procedencia», los enumera y explica por qué el quinto concepto no es campo | G SUPERADA `=` |
| `B-1` | BLOQ | `CORREGIDO_EN_F4` | **SUPERADA** | `01-PROCESOS.md` L415-440: `proceso:AUD` tiene `INV` como **única obligatoria** (`conclusion-fundada`), condicionales `DOM`·`SEG`·`DIS/Reconstruccion`·`PRD`·`APR`, y `propietario_global: "DERIVADO del encargo … NUNCA se asigna a mano"`. §18 L7676 lo reproduce. Verificado por mí en el kernel | H SUPERADA `=` |
| `B-2` | BLOQ | `PRESION_LISTA_PARA_F5` | **FALLIDA** | la mitad `DOM`/`SEG`/`DIS` está correctamente registrada como `PN-13` y es honesta. **La mitad `PLT` se cierra con el dispositivo `EJECUTOR`, que `C7:83-86` desmiente**: rama, commit, push y PR los ejecuta «la capacidad con custodia, ella misma», no `PLT`. Y F4 se contradice: §1.3 L224 da el `integration-set` a `ENT`; §7.2 L5208 «`ENT` declara convergencia con un INTEGRATION SET»; §7.6 L5292 remite a `C7` «DE LAS FUENTES». Ver `I-04` | H FALLIDA `=` |
| `G-1` | GRAVE | `CORREGIDO_EN_F4` | **SUPERADA** | `01-PROCESOS.md` `proceso:DEP`: `condiciones-de-seguridad` con `capacidad_productora: "SEG"` y `cambio-construido` con `"CON"`, las dos **obligatorias**, con su `autoridad_de_retirada`. Verificado por mí | H SUPERADA `=` |
| `G-2` | GRAVE | `CORREGIDO_EN_F4` | **SUPERADA** | `01-PROCESOS.md` L312: `proceso:DEU` → `propietario_global: "ARQ"`; `cambio-construido` producido por `CON`. §18 L7678-7679 lo reproduce | H SUPERADA `=` |
| `G-3` | GRAVE | `CORREGIDO_EN_F4` | **FALLIDA** | §8.1 L5521 declara el gate «`INS-5` baseline aprobado por el Owner». **§18 L7672, que §8.0 L5338 declara SEDE CANÓNICA con «si alguna vez difieren, MANDA §18», no lo lleva**: su columna gate dice sólo «`INS-4` Operativa» y su columna salida «control repo, topología, especialización y adaptadores», sin baseline ni clasificación de desconocidos. §14 L6801 repite la omisión. Y la asimetría es visible: el gate `A3` **sí** está en §18 L7676 | H FALLIDA `=` |
| `G-4` | GRAVE | `CORREGIDO_EN_F4` | **SUPERADA** | derivé `grep -o 'aspecto:documental/[a-z-]*' | sort -u` → **doce identificadores distintos**, todos dentro del patrón `^memoria:[a-z0-9-]+$` de `esquemas/memoria.yaml` L7. Coinciden uno a uno con las doce obligatorias de `§5.18` L775-786, contadas por mí | H SUPERADA `=` |
| `M-1` | MEDIO | `CORREGIDO_EN_F4` | **SUPERADA** | conté las condicionales de `§5.18` L788-790: **trece**. Las tres sedes de doc 11 dicen TRECE (L4320, L4353, tabla de §4.3). El residuo del registro es hallazgo mío aparte (`I-15`) | H SUPERADA `=` |
| `M-2` | MEDIO | `CORREGIDO_EN_F4` | **SUPERADA** | §1.3 L226 tiene la fila del mapa documental con autoridad «nadie: se regenera» | H SUPERADA `=` |
| `M-3` | MEDIO | `CORREGIDO_EN_F4` | **SUPERADA** | §18 L7684 (`U6`): «**revalidación del nivel VIGENTE**, no `O12`: una actualización no arranca programación», con el argumento escrito. Una sola formulación | H SUPERADA `=` |
| `M-4` | MEDIO | `CORREGIDO_EN_F4` | **SUPERADA** | `DECISIONES` D67 dice ahora «`proceso:AUD` con `INV` de obligatoria (**corregido por `D75`**; el resumen decía `proceso:INV`)» y «**propagar a las fuentes es `proceso:DEP`** — no “propagar y certificar”». La condición se cumple. **Que su ejecución exigiera reescribir una fila `D16`–`D70` es defecto de la declaración, no de esta fila**: es `I-16` | H SUPERADA `=` |
| `M-5` | MEDIO | `CONTRATO_COMPLETO_PARA_F6` | **FALLIDA** | el actor está nombrado (§5.3 L4517 `DSP`; L4559 la capacidad responsable) y la regla de `C1` está aplicada a `DSP` (L4522-4525). Pero el propio texto nuevo dice «registrada abajo **y en §17**» y **§17 L7588 no la lleva**: dice «`+4` extensiones de ficha: `ENT`, `ARQ`, `PLT` y `SEG`». `CONTRATO_COMPLETO_PARA_F6` significa que F6 lo construye sin decidir; F6 que lea §17 —el inventario de migración— **no construye la extensión de `DSP`**, y `DSP` sigue sin autorización para abrir items `AUD`, que es exactamente lo que `M-5` denunció. Añado que la mitad `CAMPAÑA` no declara si abrir una `iniciativa` cabe en la autoridad de esa ficha (`I-14`) | H FALLIDA `=` |
| `M-6` | MEDIO | `CONTRATO_COMPLETO_PARA_F6` | **FALLIDA** | la condición de cierre que `M-6` escribió es literal (doc 16 **L853**): *«Añadir `capacidades/ENC/` a la lista de extensiones de ficha de §5.2 **y a §17**»*. Se hizo en §5.2 L4475-4477 («Son **SEIS**, no cuatro») y **no se hizo en §17 L7588**, que sigue diciendo verbatim lo que `M-6` citó como su cita 5. §16 L7576 tampoco: «las **cuatro** extensiones de ficha de §5.2». **La mitad literal de su cierre no se hizo** | H FALLIDA `=` |
| `M-7` | MEDIO | `CORREGIDO_EN_F4` | **SUPERADA** | §8.0 L5401-5436: items por macrocircuito (N 2 · A 4 · M 2 · U 4) y el freno circuito a circuito, con los tres argumentos —antecedente falso en `N` y `A`, cláusula literal de `a.7` en `M` y `U`—. `a.7` L549-563 verificado. La frase «más de dos items cada uno» del preámbulo es `I-25`, MENOR | H SUPERADA `=` |
| `M-8` | MEDIO | `CORREGIDO_EN_F4` | **SUPERADA** | `grep -c 'RC-'` → **6**, todas como `RC-1`–`RC-9`; ninguna ventana se nombra ya `R<n>`. §2.9 L2950-2952 y §19 L7748-7752 las retiran del inventario | G SUPERADA `=` |
| `M-9` | MEDIO | `CORREGIDO_EN_F4` | **SUPERADA** | las catorce preguntas del §6.2 de la directiva, verbatim y sin reordenar contra `ADS-NEXT-OWNER-BRIEF` L435-450; §15.2 desglosado | H SUPERADA `=` |
| `m-1` | MENOR | `CORREGIDO_EN_F4` | **SUPERADA** | §8.2 L5741-5743: nota al pie que reancla la cifra a once **sin tocar `O15`**. Es la disciplina correcta con material en voz del Owner | H SUPERADA `=` |
| `m-2` | MENOR | `CORREGIDO_EN_F4` | **SUPERADA** | la nota de procedencia está en `DECISIONES` L292-299, **antes** de la tabla y de la sección de `O16` (L315) | H SUPERADA `=` |
| `m-3` | MENOR | `HISTORICO_NO_APLICABLE` | **NO APLICABLE con causa demostrada** | §5.2 L4448 registra el hecho —la misión de `PLT` nombra la observabilidad, verificado en `PLT/CAPACIDAD.md` L3, L13, L98— y declina el juicio: «convertirlo en defecto sería una preferencia de diseño, y esta fase no la toma». El propio documento 16 **L973** lo dice: *«`m-3` es un juicio, no un hecho … dejo el juicio al adjudicador»*. **No lo asumo**: la vía de dos responsables con `lider` existe y es del Owner o de F6 | H NO APLICABLE `=` |
| `m-4` | MENOR | `CORREGIDO_EN_F4` | **SUPERADA** | §18 L7681/L7682: `U5a` y `U5b` son filas propias con proceso, propietario y gate distintos | H SUPERADA `=` |
| `F-01` | MEDIO | `EXTERNO_CON_PROPIETARIO` | **FALLIDA** | la sede del remedio (§19 L7794) nombra `01-PROCESOS.md` y `00-CIRCUITOS.md`. **Omite `b-RECORRIDO-APROBADA.md:895` y `a-CAPACIDADES-APROBADA.md:495`**, que llevan la misma cadena `DIS/Reconstrucción` y que §17 L7585 declara «intactas. F4 no las toca». El propio checkpoint dice que el motivo del remedio es que «la composición de `A2`–`A7` **no es verificable mecánicamente contra la fuente** hasta que F6 los reconcilie» — y **la fuente es (a) y (b)**. Ejecutado tal como está escrito, el remedio no alcanza su fin declarado | H FALLIDA `=` |
| `F-02` | MEDIO | `EXTERNO_CON_PROPIETARIO` | **FALLIDA** | §19 L7795 ordena tipar como `ref_a: capacidad` y «fijar el vocabulario», **sin decir cuál**. Derivé los valores realmente usados en `01-PROCESOS.md`: además de las quince, `DOM:condiciones`, `SEG:condiciones`, `CON:experimental`, `ARQ:diagnostico`, `DIS/Reconstruccion` y `OWNER`. **F4 usa `DOM:condiciones` y `SEG:condiciones` como participantes en §8.2, §8.3, §8.4 y en §18 L7678/L7679/L7682**: bajo `ref_a` estricto, la notación de la propia F4 deja de validar | H FALLIDA `=` |
| `F-03` | MEDIO | `CORREGIDO_EN_F4` | **SUPERADA** | `grep -on '\`N[0-7]\`'` sobre doc 11 → **cinco**: L300 (la nota de `D83`), L5041 (`C6 N7`), L6266, L7004 y L7309 (`C6 N4`). **Las cinco son citas de `C6`**, verificadas contra `C6:32` y `C6:35`. Ninguna fase de instalación se nombra ya con `N<n>` | G SUPERADA `=` |
| `F-04` | MEDIO | `EXTERNO_CON_PROPIETARIO` | **SUPERADA** | registro completo: fichero, cambio, propietario, fase, condición. Cita verificada: `05-ESCENARIOS.md:180-181` dice `grado: media` / `grado_inicial: media` | H SUPERADA `=` |
| `F-05` | MENOR | `CORREGIDO_EN_F4` | **SUPERADA** | §15.7 registra la excepción de `C5`; el mapa de fuente única de `kernel/operativo/00-INDICE.md` asigna «entregas entre capacidades» a `circuitos/` y `00-CIRCUITOS` L238 desactiva la obligación. La columna del checkpoint L1230 es imprecisa: `I-24`, MENOR | H SUPERADA `=` |
| `F-06` | MENOR | `EXTERNO_CON_PROPIETARIO` | **SUPERADA** | cita verificada: `DIS-handoffs.md:137` dice `cuando: "DIS cierra su capa y el item continúa hacia verificación"`, sin estación del ciclo | H SUPERADA `=` |
| `F-07` | MENOR | `EXTERNO_CON_PROPIETARIO` | **SUPERADA** | verificado por mí: `grep -c '^autoridad:' docs/owner/*.md` → **0 y 0** | H SUPERADA `=` |
| `F-08` | MENOR | `EXTERNO_CON_PROPIETARIO` | **SUPERADA** | registro completo en §19 L7801 (fichero, cambio, propietario «el **Owner**: es su documento», fase **F5**) y en la matriz L1233 con el atributo `requiere F5 · sí · sin PN`. Su ausencia de §16 es **correcta**: §16 se autodefine «presiones normativas», y `F-08` no lo es —`IDEAS` se declara «no es una especificación cerrada»—. **Rechazo el argumento de `H`**: §17 **L7597** dice literalmente *«`docs/evolucion/` … **temporal**. Se retira tras F6, **y no antes: F5 y F6 necesitan su trazabilidad**»* — la línea que `H` cita lo refuta. Queda un residuo MENOR: `I-28` | H FALLIDA `≠` |
| `F-09` | MENOR | `CORREGIDO_EN_F4` | **SUPERADA** | §8.4 L5971-5975 conserva «PROVISIONAL» con su procedencia. La cita de sección es imprecisa (`I-23`, MENOR): el calificativo está en `IDEAS` §3 L79, no en §15 | H SUPERADA `=` |
| `F-10` | MENOR | `EXTERNO_CON_PROPIETARIO` | **SUPERADA** | verificado por mí: **14** `^id: forma:` y **9** `^id: entrada:`. La aposición «uno por clase de expresión» de `03-FORMAS.md` L3 es falsa y la cifra 14 correcta, exactamente como el registro declara | H SUPERADA `=` |
| `F-11` | MENOR | `EXTERNO_CON_PROPIETARIO` | **SUPERADA** | verificado: `05-ESCENARIOS.md` L5 dice «las pruebas T75 a T84» y el fichero contiene `T75`–`T80` y `T154`–`T157` | H SUPERADA `=` |
| `F-12` | MENOR | `CORREGIDO_EN_F4` | **SUPERADA** | `git diff --name-only` del rango: los documentos **15, 16 y 17 no aparecen**. La disciplina de inmutabilidad se respetó, y `00-INDICE.md` reancla las proyecciones | G SUPERADA `=` |

### 5.3 · Recuento, derivado de las filas y no al revés

```text
SUPERADAS                32
FALLIDAS                 10   A2 · A4 · A7 · A8 · B-2 · G-3 · M-5 · M-6 · F-01 · F-02
NO APLICABLE con causa    1   m-3
                        ───
                         43
```

**Ninguna fila se declara superada por recuento agregado**: cada una lleva arriba su prueba.

**Por severidad original de las fallidas:** **DOS BLOQUEANTES** (`A2`, `B-2`) · **DOS GRAVES**
(`A4`, `G-3`) · **SEIS MEDIOS** (`A7`, `A8`, `M-5`, `M-6`, `F-01`, `F-02`).

---

## 6 · Discrepancias entre `G` y `H`, resueltas una a una

No hay solape de filas. Las discrepancias materiales son de **severidad sobre el mismo
hecho** —los dos revisores encontraron por separado dos defectos idénticos y los graduaron
distinto— y de **alcance**. Resuelvo cada una con la fuente.

**D-1 · §14 L6801, «antes de `INS-3` no hay estado que perder».** `G` lo gradúa **MEDIO**
(su `M-3`); `H` lo gradúa **GRAVE** (su `H-2`). Los dos lo sitúan bien y la cita es exacta.
**Resuelvo: GRAVE**, y el argumento es del propio documento. §14 se abre (L6796-6797)
declarando su función: *«Son recorridos arquitectónicos, y sirven para una sola cosa:
**demostrar que las piezas encajan sin contradecirse**»*. Una celda de §14 que contradice a
§8.1 no es una imprecisión periférica: **falsifica la función declarada de la sección**. Y
§8.1 L5561-5566 no dice que la frase sea mejorable: la cita como el defecto que corrige —
*«Las dos frases juntas dicen que entre `INS-0` y `INS-3` la iniciativa no está persistida …
Eso es exactamente lo que el apartado 19 de la directiva prohíbe»*—. Añado la prueba que
ninguno de los dos dio del todo: `11-base:6233` decía «antes de **N3**», luego **esta tanda
abrió esa celda, la renombró y no vio lo que decía**.

**D-2 · las extensiones de ficha, SEIS frente a CUATRO.** `G` lo gradúa **MEDIO** (su `M-4`,
que registra «por si corresponde a otro eje»); `H` lo gradúa **GRAVE** (su `H-3`).
**Resuelvo: GRAVE.** La prueba que desempata es la condición de cierre literal de `M-6`
(doc 16 **L853**): *«Añadir `capacidades/ENC/` a la lista de extensiones de ficha de §5.2 **y
a §17**»*. No es una discrepancia de recuento entre dos sedes cualesquiera: **una de las dos
sedes está nombrada en la condición de cierre del hallazgo**, y es la que no se tocó. Y hay
tres sedes vigentes con dos cifras —§5.2 L4475 SEIS, §16 L7576 CUATRO, §17 L7588 `+4`—, con
dos remisiones nuevas de esta misma tanda (§5.3 L4525, §8.2 L5680) apuntando a la que no las
lleva. `G` acertó al registrarlo pese a no ser su eje; su graduación se queda corta.

**D-3 · quién ejecuta las operaciones Git de las fuentes.** No es discrepancia entre `G` y
`H` —es materia de `H`—, pero `G` toca el mismo contrato desde el otro lado y conviene
declarar que **no se contradicen**. `G` verifica que el rango **no toca `C7`** (`git diff`
vacío) y que `C7:170` conserva su `aplica_a`; `H` verifica que **§8.0 le atribuye a `PLT`
cuatro operaciones que `C7:83-86` da a la capacidad con custodia**. Las dos cosas son ciertas
a la vez, y juntas son peores: el contrato está intacto **y** la arquitectura lo contradice.

**D-4 · el reparto de `M-4` (extensiones) como frontera de eje.** `G` lo registra con nota de
frontera; `H` lo registra como propio. **Resuelvo que el hecho es uno solo** y lo consolido en
`I-06`, con crédito a los dos: es la única convergencia independiente del expediente, y por
eso la considero especialmente firme.

**D-5 · cobertura del documento 15.** `G` y `H` no discrepan: **los dos declaran no haberlo
leído**, y está asignado a los dos. No es una discrepancia que resolver, es un hueco que
consignar, y lo consigno en §4.4.

**Cuestiones materiales que NO puedo resolver con la fuente, y que por tanto declaro
INSUFICIENTES y no promedio:**

```text
1  SI `C2`, `C3`, `C4`, `diseno/00`-`02`, `diseno/04`-`05`, `entrada/00`, `entrada/02`,
   `entrada/04`, `E1-ENC` o el documento 15 contienen algo que refute o agrave alguno de los
   hallazgos de abajo. Nadie los abrió, yo tampoco los he leído íntegros, y no voy a
   sustituir una lectura ausente por una presunción en ninguna de las dos direcciones.

2  SI `H-5` (`I-08`) admite una lectura en la que `<CAP>:revisión` sea ilustrativo. El propio
   `H` lo declara: no leyó `b.3` ni `b.5` completos. La evidencia directa es fuerte —`b.16`
   L834-836 y `a.6` L504-505 lo dicen dos veces— pero la refutación posible vive en un tramo
   que nadie abrió.

3  SI `T148` y `T159` fallan por la versión de Python. Reproduje los dos fallos con Python
   3.10.12, y la salida dice `workspace check falla en el proyecto creado (exit 1)`, que
   **no establece** la causa que `G` les atribuye. Es `A14`, fuera de los 43, y por eso no
   cambia el veredicto — pero la atribución de `G` no está demostrada.
```

---

## 7 · Hallazgos consolidados — confirmados, reformulados y rechazados

Numerados `I-nn`. Severidad **adjudicada por mí**, no heredada.

### GRAVES

**`I-01` · GRAVE · `D79` autoriza `estado/cuarentena/<TX>/`, una ubicación de estado sin
plano, sin ciclo y sin fila, que el mismo documento descarta doce páginas después.**
*(procede de `G-1` de `G`; **CONFIRMADO**, con una precisión.)*

> `11-ARQ:1962-1963` · «(i) AUTORIZAR LA CUARENTENA — copiar lo divergente fuera del
> worktree, a **`estado/cuarentena/<TX>/`**, con su hash registrado en el `conflicto`»
>
> `11-ARQ:2103` · «| **D** | **cuarentena** fuera del estado canónico | … | **crea una tercera
> ubicación con su ciclo y su plano, que §2.4 no tiene** … | **descartada: reintroduce la
> tercera categoría que `D50` eliminó** |»

`grep -in cuarentena` sobre `11-base` devuelve **una línea**, L1979, la alternativa
descartada. Sobre `HEAD` devuelve cuatro. **Las tres nuevas son de esta tanda.**

`estado/cuarentena/` no tiene plano en §1.2 ni en §2.4, no tiene fila en §1.3, no está en el
árbol de §2.3 (L373-408, que sí lista `estado/tx/`), no está en ninguna declaración de
`.gitignore`, no tiene fila de reconstrucción en §2.9 y ninguna fila adversarial la toca. Por
el criterio vigente de §2.4 L415-418 —«DURABLE Y VERSIONADO: `estado/` **salvo la excepción de
ruta declarada abajo**», y esa excepción nombra **sólo** `estado/tx/`— **la cuarentena viaja a
Git**. Y entonces el acto (i) publica en `main` exactamente el material que existe para
preservar cuando §2.6.9 L1871-1876 declara que **«`SEG` bloquea su publicación —secretos,
material no publicable—»**. La lectura contraria —cuarentena operacional— deja la única copia
de lo divergente sin sobrevivir a la pérdida de la máquina, que es la garantía que `4b`(i)
existe para dar. **Las dos lecturas son malas y el documento no elige.**

**Precisión que hago a `G`:** la alternativa D de §2.6.10 es un **mecanismo general de
aislamiento**, y el acto (i) es una **preservación puntual bajo autoridad**; no son
literalmente lo mismo, y por eso no lo llamo autocontradicción exacta. **Pero la objeción que
L2103 escribe —«crea una tercera ubicación con su ciclo y su plano, que §2.4 no tiene»— se
aplica palabra por palabra a la ruta nueva**, y eso es lo que sostiene la gravedad. El
hallazgo se mantiene GRAVE por la ubicación sin clasificar, no por la etiqueta.

---

**`I-02` · GRAVE · el marcador de `D78` invoca una excepción de ruta que no lo cubre, y no
tiene ninguna de las cinco piezas de disciplina del marcador que dice imitar.**
*(procede de `G-2` de `G`; **CONFIRMADO** íntegro.)*

> `11-ARQ:1494-1496` · «**No gana identidad propia**: es RECONSTRUIBLE desde el diario por el
> mismo predicado, **vive en `estado/` fuera de Git por la excepción de ruta de §2.4**»
>
> `11-ARQ:417-418` · «OPERACIONAL Y NO VERSIONADO `.ads/run/` … **Y los marcadores de
> transacción de `estado/tx/`**, por la excepción de abajo»

`grep 'estado/deriva'` sobre todo el documento devuelve **dos líneas**: L1488 y el registro
`D78` L7150. Contra las cinco piezas del otro marcador, verificadas por mí una a una:

```text
clasificación de plano          §2.4 L433-440  ·  ninguna
excepción de ruta que lo nombre §2.4 L417-418  ·  ninguna: la excepción nombra `estado/tx/`
`.gitignore` en positivo        L445, L1316    ·  ninguna
fila de reconstrucción en §2.9  L2647          ·  ninguna
fila adversarial                X27, L1356     ·  ninguna
árbol de §2.3                   L373-408       ·  no lo lista
creación en el paso E de §2.6.9 L1718-1722     ·  no lo crea, pese a L1490
```

Por el criterio vigente **viaja a Git**, y entonces un clon nuevo lo recibe y por el paso
`2bis` declara NO FIABLES las rutas que nombra, sin el ramal de `fallo` que la garantía 6
(L1113-1121) sí da para el otro marcador. **Un caché versionado que nadie regenera con sede
declarada y que nadie prohíbe editar es una segunda fuente de verdad**, y `I5` lo prohíbe.
La intención está bien escrita; la propagación —que era literalmente lo que `A8` pedía— no
se hizo.

---

**`I-03` · GRAVE · el validador semántico del diario conserva dos reglas normativas que `D64`
retiró, y una de ellas es la afirmación exacta que causó `A2`.**
*(procede de `G-3` de `G`; **CONFIRMADO**, y sube en importancia porque cierra `A2`.)*

> `11-ARQ:3925` · «· TERMINALIDAD: **exactamente un `derivada` por transacción cerrada**, y
> ninguno en las abiertas»
>
> `11-ARQ:3945-3947` · «· LA IDENTIDAD DE LA RUTA: **#observaciones = #intentos** … y en la
> **AGOTADA** ese `+1` es siempre el `conflicto` con **`agotado: true`**»

Contra el propio documento, en la misma sección y en la misma lista:

- `11-ARQ:993-1002` · «`derivada` y `abandonada` son MUTUAMENTE EXCLUYENTES … ninguna
  transacción cerrada tiene cero», y la tabla da `derivada` = **0** en la columna
  `abandonada`.
- `11-ARQ:3928-3932` · tres líneas más abajo, **en la misma lista**: «`derivada` y
  `abandonada` **mutuamente excluyentes**, y toda transacción cerrada tiene exactamente uno
  de los dos».
- `11-ARQ:718-721` · «`intentos_consumidos`, `intento` y `agotado` **se retiran**».

Las dos líneas son idénticas a `11-base:3777` y `11-base:3797`: **texto no corregido**. Por
qué importa materialmente: la capa B es la sede que `D71` L616-619 designa para **evaluar
`abierta(tx)`**. Un validador construido literalmente de esta lista **rechazaría toda
transacción abandonada** por la regla de terminalidad, e intentaría comprobar una regla
inconstruible por la de identidad de ruta. Es el residuo de `A2` en el único sitio donde el
predicado se ejecuta, y es la razón principal por la que `A2` queda FALLIDA.

---

**`I-04` · GRAVE · `PLT` no ejecuta rama, commit, push ni PR: `C7` se los da a la capacidad
con custodia, y F4 se contradice a sí misma en tres sedes.**
*(procede de `H-1` de `H`; **CONFIRMADO**, con dos citas corregidas y un matiz de
procedencia.)*

> `11-ARQ:5379-5381` · «EJECUTOR … **`PLT` bajo `C7` es el caso constante**: custodia la
> maquinaria y **cada source change —rama, commit, push, PR y CI POR FUENTE**—, y no es
> participante de la ruta por hacerlo»
>
> `C7-GOBIERNO-GIT-MULTI-SOURCE.md:82-92`, leído por mí:
> ```
> materializar una fuente  | DSP al despachar          | PLT              ← F4 acierta
> crear rama o worktree    | la capacidad con custodia | ELLA MISMA
> commit                   | la capacidad con custodia | ELLA MISMA
> push                     | la capacidad con custodia | ELLA MISMA
> abrir PR                 | la capacidad con custodia | ELLA MISMA
> merge de una fuente      | ENT                       | ENT
> declarar convergencia    | ENT                       | ENT
> retirar rama abandonada  | PLT                       | PLT              ← F4 acierta
> ```
> `C7:76-77` · «Sin esta tabla, la responsabilidad se reparte de forma ambigua entre `PLT`,
> `ENT`, `DSP` y `CON`, que es exactamente el defecto que este contrato existe para cerrar.»

De las siete operaciones que F4 atribuye a `PLT`, **`C7` le da dos**. Y no es sólo
divergencia con el contrato: §1.3 **L224** asigna el `integration-set` a `ENT` como autoridad
**y** ejecutor; §7.2 **L5208** escribe «`ENT` declara convergencia con un INTEGRATION SET»; y
§7.6 **L5292** dice «`C7` declara quién pide, ejecuta, bloquea y verifica cada una **DE LAS
FUENTES**». Agrava que §8.0 **L5477** haga viajar «DE `PLT` A `VER` el resultado por fuente,
con su estado `INTEGRACIÓN PARCIAL`», cuando la convergencia es de `ENT` por `C7:89`. Y la
ficha de `PLT` L3-4 dice que **no toma custodia de paquetes de producto**, luego no puede ser
«la capacidad con custodia» de ningún source change de producto.

**Corrijo dos citas de `H`:** sitúa la frase de §7.2 en **L5203** —esa línea es un carácter de
flecha— cuando está en **L5208**; y la de §7.6 en **L5296** —que es «EL CONTROL REPO NO ESTÁ
CUBIERTO»— cuando la frase relevante está en **L5292**. Los hallazgos sobreviven con la
referencia corregida.

**Corrijo el alcance de `H`, que dice «el defecto lo introduce la corrección».** Lo verifiqué:
`git show 7e99388 | grep -n EJECUTOR` devuelve **L5310 y ninguna otra en §8** — la fila
existía ya en §8.3, con el mismo texto «`PLT` para cada source change, bajo `C7`». **La semilla
es heredada.** Lo que esta tanda introduce es (i) la **generalización** a §8.0 L5379, §8.1
L5511, §8.2 L5677, §8.4 L6006 y a la columna «ejecutor y autoridad» de las diez filas de §18,
y (ii) su **promoción a dispositivo de cierre de un BLOQUEANTE**. Eso es lo grave: un error de
detalle heredado se ha convertido en la mitad de la respuesta a `B-2`.

---

**`I-05` · GRAVE · §14 conserva, renombrada por esta tanda, la afirmación sobre la
reanudación que §8.1 declara retirada.** *(convergencia independiente de `M-3` de `G` y `H-2`
de `H`; **CONFIRMADO** y graduado GRAVE — ver D-1.)*

> `11-ARQ:6801`, §14 escenario 1, columna «cómo se recupera» · «repetir el paso; **antes de
> INS-3 no hay estado que perder**»
>
> `11-ARQ:5561-5566`, §8.1 · «### `estado/` nace en INS-0, y no en INS-3 … F4 entregada
> declaraba *«`estado/` nace en INS-3»* y *«REANUDACIÓN por checkpoint desde INS-3; antes,
> repitiendo el paso»*. **Las dos frases juntas dicen que entre INS-0 y INS-3 la iniciativa no
> está persistida**: vive en la conversación. Eso es exactamente lo que el apartado 19 de la
> directiva prohíbe»
>
> `11-base:6233` · «… antes de **N3** no hay estado que perder»

Y §8.1 L5605-5607 declara lo contrario: «**«Continúa» funciona desde el primer minuto** … El
recorrido se reanuda desde INS-0 SIN el chat y SIN el Owner, que es `R7` y `b.14`».

Dos contratos incompatibles vigentes sobre la propiedad de operabilidad central. Y es
exactamente lo que la instrucción 3 del checkpoint manda comprobar: *«que ninguna afirmación
vieja sobrevive sin marca de histórica»*.

---

**`I-06` · GRAVE · las extensiones de ficha son SEIS en §5.2 y CUATRO en §16 y §17, y §17 es
la sede que la condición de cierre de `M-6` nombra.** *(convergencia de `M-4` de `G` y `H-3`
de `H`; **CONFIRMADO** y graduado GRAVE — ver D-2.)*

> `11-ARQ:4475-4477` · «QUÉ TRABAJO GENERA una EXTENSIÓN DE FICHA en F6 … **Son SEIS**, no
> cuatro», y las enumera: `ENT`, `ARQ`, `PLT`, `SEG`, **`DSP`** (`M-5`), **`ENC`** (`M-6`)
>
> `11-ARQ:7588`, §17 · «`+4` extensiones de ficha: `ENT`, `ARQ`, `PLT` y `SEG`»
>
> `11-ARQ:7576`, §16 · «las **cuatro** extensiones de ficha de §5.2»
>
> `16-GATE-FINAL…:853` · «Añadir `capacidades/ENC/` a la lista de extensiones de ficha de
> §5.2 **y a §17**»

Y dos remisiones nuevas de esta tanda apuntan a la sede que no las lleva: §5.3 **L4525**
(«registrada abajo y **en §17**») y §8.2 **L5680** («está en §5.2 **y §17**»). F6 que lea §17
—el inventario de migración— construye cuatro extensiones, `DSP` sigue sin autorización para
abrir items `AUD` y `ENC` sin admitir findings, que son los dos defectos que `M-5` y `M-6`
denunciaron y que la matriz declara `CONTRATO_COMPLETO_PARA_F6`.

---

**`I-07` · GRAVE · §18, declarada sede canónica por esta misma tanda, no lleva el gate del
Owner de `INS-5` que `D76` creó, ni su salida.** *(procede de `H-4`; **CONFIRMADO**.)*

> `11-ARQ:5338` · «SEDE CANÓNICA la tabla de §18 … Los bloques de §8.1–§8.4 son su LECTURA
> narrativa: **si alguna vez difieren, MANDA §18**»
>
> `11-ARQ:5521`, §8.1 · «GATES `INS-4` certificación Operativa · **`INS-5` baseline aprobado
> por el Owner** · `INS-7` = O12»
>
> `11-ARQ:7672`, §18, fila `INS-0`–`INS-5` · columna gate: «`INS-4` Operativa». Columna
> salida: «control repo, topología, especialización y adaptadores»

Sin baseline y sin clasificación de desconocidos críticos, que es **lo que `D76` produce** y
lo que hace satisfacible `INS-7 = O12`. §14 L6801 repite la omisión («INS-4 Operativa, INS-7 =
`O12`»). **Bajo la regla de conflicto que esta misma tanda escribió, la corrección de `G-3`
pierde en la sede que manda.** Y la asimetría es visible y verificada por mí: el gate `A3`
**sí** está en §18 L7676 («`A3` baseline aprobado por el Owner»), y `D76` invoca precisamente
«la misma disposición que `A3`».

---

**`I-08` · GRAVE · `b.16` da a `DOM` y a `SEG` una segunda participación —revisar lo
construido— que ningún proceso instancia, y el gate de composición de §8.0 no puede verla.**
*(procede de `H-5`; **CONFIRMADO**, con la reserva declarada en D-5·2.)*

> `b-RECORRIDO-APROBADA.md:832-836` · «### DOM y SEG participan dos veces, y nunca a la vez
> que CON — `<CAP>:condiciones ⊳ CON` RESTRICCIONES ANTES de construir. Consulta. ·
> **`<CAP>:revisión` tras VER revisan lo construido.** Consulta o gate conjunto.»
>
> `a-CAPACIDADES-APROBADA.md:504-505` · «DOM y SEG aportan **condiciones antes de construir y
> revisan después**, no reciben la primera noticia en paralelo con CON»
>
> `grep -rn ':revisi' kernel/operativo/` → **vacío**, verificado por mí

Los diez procesos instancian sólo `:condiciones`. F4 compone `A8`, `M6`–`M7` y `U5b` con
`DOM:condiciones` y `SEG:condiciones` y nada más (§18 L7678/L7679/L7682) — **los tres tramos
que escriben en las fuentes del producto**. El `GATE DE COMPOSICIÓN` de §8.0 L5442 comprueba
«para CADA capacidad que la fase declara, consta UNA de las cuatro vías» — comprueba contra
los condicionales declarados, **no contra `b.16`**, luego daría por completa una composición
a la que le falta una participación que (b) exige. No está entre los 43, no tiene `PN` y no
está entre los ocho externos. Es la misma clase de defecto que `B-2` —participante sin
vehículo— un nivel más abajo, y la comprobación mecánica que el checkpoint declara en verde
(«vía declarada para cada participante») es exactamente la que debía haberlo encontrado.

### MEDIOS

**`I-09` · MEDIO · el censo de sedes de `abierta(tx)` es falso en dos de sus siete entradas, y
su declaración de cierre es desmentida por el propio documento.** *(de `M-1` de `G`;
**CONFIRMADO**, con el censo verificado por mí.)*

> `11-ARQ:621-624` · «DÓNDE SE CITA §2.5 · **§2.6.4** · §2.6.6 · §2.6.8 · **§2.6.9** · §2.9 ·
> §7.4. **Las siete REMITEN aquí. Ninguna lo redeclara.**»

`grep -n 'abierta(tx)'` fuera de §2.6.1 devuelve **siete**, y las asigné a su sección con los
límites reales (`grep -n '^### 2\.6\.'`):

```text
L496   §2.5      ✔ nombrada        L1061  §2.6.5   ✘ NO nombrada
L1220  §2.6.6    ✔ nombrada        L2313  §2.6.11  ✘ NO nombrada
L1501  §2.6.8    ✔ nombrada        L2647  §2.9     ✔ nombrada
L5253  §7.4      ✔ nombrada
§2.6.4 (L831-1040) y §2.6.9 (L1532-2007): CERO citas del predicado
```

Y §2.6.4 **redeclara**: `11-ARQ:894` · «¿EXISTE UNA TRANSACCIÓN ABIERTA —`preparada` durable y
**SIN `derivada`**—…?», idéntica a `11-base:819`. **La cifra siete es correcta; el censo no.**
Declaro por delante lo que lo mitiga, como hizo `G`: el paso 0 de §2.6.4 (L883-892) comprueba
**los dos** terminales antes del paso 1, luego la función de clasificación es correcta y no
hay defecto de comportamiento. Lo que falla es la declaración de cierre — y ésa es la
condición publicada de `A2`.

---

**`I-10` · MEDIO · tres sedes describen el resultado de un abandono como «estado mixto», y la
garantía de `main` se apoya en la inferencia que `D69` refutó.** *(de `M-2` de `G`;
**CONFIRMADO**.)*

> `11-ARQ:2192-2195` · «MAIN NUNCA CONTIENE ESTADO PARCIAL — porque un commit sólo ocurre
> **sin marcadores abiertos**, y sin marcador toda transacción está cerrada … **Un abandono
> deja estado mixto declarado**»
>
> `11-ARQ:2343-2344` · «sus rutas quedaron en **un estado mixto declarado**»
>
> Contra `11-ARQ:1728-1729` · «LLEVA · el estado canónico **RESTAURADO A LA BASE — idéntico,
> byte a byte**», y `11-ARQ:1680-1684` (nota de `D69`) · «La redacción anterior hacía que
> `abandonada` retirase el marcador **dejando el conjunto parcial en el worktree**, y con el
> marcador retirado ese conjunto era **publicable**»

El argumento «sin marcador ⇒ cerrada ⇒ `main` sin estado parcial» **es literalmente la
inferencia que `D69` refutó**. La razón real es la restauración verificada, y no se invoca.
La **conclusión** sigue siendo cierta —lo digo—; lo que falla es su argumento y la glosa de
las tres sedes.

---

**`I-11` · MEDIO · §16 enumera «`PN-6` a `PN-12`» y su propio total dice ONCE.** *(de `H-6`;
**CONFIRMADO**, con la línea corregida: **L7184**, no L7183.)*

> `11-ARQ:7184` · «De aquellas cinco resultan **TRES vigentes** … Las demás vigentes —**`PN-6`
> a `PN-12`**— son posteriores, y el total está abajo.»

3 + 7 = **10**. Falta `PN-13`, que es **la única que esta tanda añade** y la que el Owner
tiene que decidir. Está en la misma frase que `m2` corrigió por este mismo motivo aritmético,
y §16 es el documento que va al Owner.

---

**`I-12` · MEDIO · `D76`, `D82` y el `D67` reescrito se escriben en el espacio de nombres que
`D83`, del mismo bloque y el mismo commit, retira.** *(de `H-7`; **CONFIRMADO y reforzado**.)*

> `DECISIONES-Y-CONTRADICCIONES.md:257` (`D76`) · «**`N5`** produce el BASELINE y la
> CLASIFICACIÓN DE DESCONOCIDOS CRÍTICOS … `N7 = O12`»
>
> `…:264` (`D82`) · «no hay items de producto listos antes de **`N7`/`A10`**»
>
> `…:265` (`D83`) · «se renombran **las fases**, `INS-0`…`INS-7`»

Refuerzo con lo que `H` no vio: el `D67` que esta tanda **reescribió** también dice «**`N0`
crea el item real `SIS-001`**». Derivé sobre el diff: el texto **nuevo** del registro contiene
**ocho** apariciones de `N0`…`N7` en el sentido de fase. `D16`–`D70` conservan su texto por
diseño y eso excusa a `D65`; **`D76`, `D82` y el `D67` corregido son de este bloque y no tienen
esa excusa**. La prueba que `D83` declara —un identificador, un significado— falla hoy sobre el
registro de decisiones.

---

**`I-13` · MEDIO · el remedio declarado de `F-02` invalidaría la notación de participantes que
la propia F4 usa.** *(de `H-8`; **CONFIRMADO, reformulado a la baja en su consecuencia.**)*

> `11-ARQ:7795` · «fijar el vocabulario del campo `capacidad` y tiparlo, junto con
> `capacidad_productora`, como **`ref_a: capacidad`**»

Derivé los valores reales de `01-PROCESOS.md`: además de las quince, `DOM:condiciones`,
`SEG:condiciones`, `CON:experimental`, `ARQ:diagnostico`, `DIS/Reconstruccion` y `OWNER`. Y
F4 usa `DOM:condiciones` y `SEG:condiciones` **como participantes** en §8.2, §8.3, §8.4 y en
§18 L7678/L7679/L7682. Bajo `ref_a` estricto, §18 deja de validar.

**Reformulo la consecuencia que `H` extrae.** `H` dice que «F6 tendría que decidir el
vocabulario». **No es exacto:** el documento 17, `E-3`, ya lo escribió —*«capacidad de las
quince, **con sufijo `:` opcional para la variante declarada**»*— y el documento 17 es corpus
inmutable y accesible a F6. El defecto es que **§19 no lo recoge**, no que la arquitectura
esté sin decidir. Esto importa para el veredicto: **ningún MEDIO de esta adjudicación exige
arquitectura nueva.**

---

**`I-14` · MEDIO · la regla de `C1` se aplica al abridor de auditorías y no al de campañas, y
ninguna de las quince fichas menciona `iniciativa` ni `campaña`.** *(de `H-10`;
**CONFIRMADO**.)*

`11-ARQ:4522-4525` aplica `C1:118` a `DSP` y crea su extensión de ficha. `11-ARQ:4559-4562`
dice que la campaña —«una `iniciativa` de §3.3 con su gate»— la abre «la capacidad
RESPONSABLE del aspecto», **sin aplicar la misma regla**. Y `C1:118` es taxativa: «la autoridad
de un rol es **SIEMPRE** un subconjunto de la de su capacidad». `grep` sobre las quince fichas:
cero apariciones de `iniciativa` o `campaña`. La condición del gate pedía las **dos** mitades.

---

**`I-15` · MEDIO · el registro de `D77`, escrito por esta tanda, dice «las CATORCE
condicionales» donde `M-1` fijó TRECE.** ***HALLAZGO MÍO — no está en `G` ni en `H`.***

> `DECISIONES-Y-CONTRADICCIONES.md:259` (`D77`, línea **nueva** del rango: `grep -c D77` sobre
> `7e99388` devuelve **0**) · «Las **CATORCE** condicionales **no** reciben identificador aquí»
>
> Contra `11-ARQ:4320` · «las **TRECE** condicionales NO reciben identificador aquí»,
> `11-ARQ:4353` · «las **TRECE** que `§5.18` enumera», y el propio resumen `D77` en
> `11-ARQ:7149` · «Las **TRECE** condicionales NO lo reciben»

Y las conté yo sobre `ADS-PENDIENTES` `§5.18` L788-790: UX e investigación · dirección visual ·
sistema de diseño · arquitectura de datos detallada · integraciones · cumplimiento regulatorio ·
modelo de amenazas avanzado · observabilidad · continuidad · analítica · dispositivos ·
internacionalización · gobierno de IA = **TRECE**.

**Por qué importa.** `M-1` es exactamente el hallazgo «catorce frente a trece», y su condición
de cierre es «TRECE condicionales, en las tres sedes». Las tres sedes del documento 11 se
corrigieron; **la cuarta, escrita de cero en este mismo rango, reintrodujo la cifra
defectuosa** en el registro que es la fuente de trazabilidad de las decisiones. No es
editorial: es un recuento, y el encargo excluye del perdón editorial lo que afecta a
recuentos.

---

**`I-16` · MEDIO · la tanda reescribe una fila `D16`–`D70` en el mismo commit en que declara
que no se reescriben.** ***HALLAZGO MÍO — no está en `G` ni en `H`.***

`git diff 7e99388..0a4b3a0 -- DECISIONES-Y-CONTRADICCIONES.md` tiene **una sola supresión de
fila de decisión: `D67`**, sustituida por una versión nueva. Y en el mismo diff se inserta:

> `DECISIONES-Y-CONTRADICCIONES.md`, bloque `D71`–`D86` · «> **`D16`–`D70` no se reescriben.
> `O15` y `O16` quedan intactas.**»
>
> `11-ARQ:7140`, §15.8 · «**`D16`–`D70` conservan su texto.**»
>
> `CHECKPOINT` L1169 · «DECISIONES `D71`–`D86`. **`D16`–`D70` conservan su texto.**»

`H` adjudicó `M-4` SUPERADA y no vio esto; `G` citó la disciplina («`D16`–`D70` no se
reescriben», L233 y L7139) como sostén de su argumento sobre `D65` **sin comprobar que se
cumpliera**. La reescritura de `D67` era el remedio que `M-4` exigía y está marcada en línea
(«corregido por `D75`; el resumen decía `proceso:INV`»), luego el defecto está en la
**declaración**, no en la edición: **tres sedes afirman una disciplina que el mismo commit
falsifica.** Afecta a la trazabilidad, que es la única función del registro.

### MENORES

`I-17` · **la ventana de commit se define sobre `derivada`.** `11-ARQ:1180-1181`: «el conjunto
de transacciones cuyo evento **`derivada`** NO está incluido todavía en ningún commit». Una
cerrada por `abandonada` nunca sale de la ventana. **Mitigado** por L1189-1191 («Las cerradas
por `abandonada` no afirman ningún resultado»): la consecuencia es coste, no fallo.
*(de `N-1` de `G`; confirmado.)*

`I-18` · **dos resúmenes conservan «completar, o marcar conflicto» sin la segunda salida.**
`11-ARQ:5225-5226` (§7.3) y `:6808` (§14, escenario 8). `conflicto` no es desenlace: es
observación con dos salidas (§2.6.9). Es la formulación que `A3` corrigió, sobreviviendo dos
secciones más allá. *(de `N-2` de `G`; confirmado.)*

`I-19` · **«CORREGIDO NUEVE VECES» no deriva de ninguna de sus dos fuentes declaradas.**
`11-ARQ:12` y su aposición. §15.8 tiene **doce** bloques de corrección, contados por mí; la
aposición **omite `D69`–`D70`** enteramente y dice «cinco comprobaciones técnicas» donde §15.8
rotula hasta la **SEXTA**. La frase afirma «El recuento se deriva de la lista de abajo y de
§15.8». *(de `H-11`; confirmado y reforzado — `H` no vio la omisión de `D69`–`D70` ni la
sexta.)*

`I-20` · **«DOS formas de estar presente» y se usan tres.** `11-ARQ:5375` dice DOS;
§8.1 L5513 y §8.2 L5679 usan `EJECUTOR`, `AUTORIDAD` **y `ENCUADRE`**. El registro de `D74` sí
dice tres. *(de `H-12`; confirmado.)*

`I-21` · **los cuatro macrocircuitos no declaran campo `handoffs`**, y el propio checkpoint
L1281 dice «los cuatro macrocircuitos con sus **doce** campos» donde el encargo pedía catorce.
El contenido de lo que viajaría sí está declarado en §8.0 L5470-5482, y eso es más de lo que
había. *(de `H-13`; confirmado.)*

`I-22` · **§8.0 L5389-5390 describe la forma de `C5` con seis campos de los once obligatorios
de `esquemas/handoff.yaml`** —que verifiqué: `id, de, a, cuando, entrega, comprueba_al_recibir,
rechaza_si, devolucion, evidencia_de_devolucion, owner, checkpoint`— **sin decir que la lista
es parcial**. *(de `H-14`; confirmado.)*

`I-23` · **cita de sección imprecisa en `F-09`.** `11-ARQ:5971-5973` atribuye el calificativo
«principio PROVISIONAL» a `IDEAS` **§15**; está en **§3, L79**. §15 (L589) lleva el principio
sin el calificativo. La sustancia de `F-09` es correcta. *(de `H-15`; confirmado.)*

`I-24` · **la columna de cierre de `F-05` en el checkpoint L1230 dice «§8.0 declara qué
**checkpoint** viaja»**; §8.0 L5470-5478 declara **qué viaja**. §19 L7797 lo dice bien.
*(de `H-16`; confirmado.)*

`I-25` · **«componen más de dos items cada uno» frente a N 2 y M 2.** `11-ARQ:5401-5402`,
dentro de la nota de `M-7`, contra la derivación diez líneas después. **Atenúo respecto de
`H`:** la frase está dentro del bloque `>` que **cita la premisa del hallazgo**, no en la
derivación normativa; el defecto es de la premisa citada. *(de `H-17`; confirmado, atenuado.)*

`I-26` · **`PN-13`, campo `ALCANCE`, está truncado a media frase.** `11-ARQ:7520-7521` ·
«…ni a `A8`, `M6`–`M7` ni `U5b`, que son `DEU` y `DEP` **y también**», y la línea siguiente ya
es otro campo. Está **en la única presión que esta tanda añade y que va al Owner**.
*(de `H-18`; confirmado.)*

`I-27` · **§14 escenario 6 nombra «runtime dentro de `O7`» donde §5.3 L4517 nombra a `DSP`.**
`11-ARQ:6806`. Es el residuo de `M-5` en la sede que no se revisó. *(de `H-19`; confirmado.)*

`I-28` · **la instrucción operativa del checkpoint no nombra el único trabajo de F5 que no es
presión.** `CHECKPOINT` punto 4: «QUÉ LLEVAR AL OWNER: las **ONCE** presiones de §16» — y
`F-08` es F5 y no es presión. **Reformulación a la baja de `H-9`** *(ver §8, corrección a `H`
nº 1)*: el registro **sí existe** (§19 L7801, matriz L1233 con `requiere F5 · sí · sin PN`) y
el punto 5 sí lo cubre («QUÉ VIGILAR: los OCHO hallazgos EXTERNOS de §19»). Queda que un
Owner que siga sólo el punto 4 no lo vería.

### RECHAZADOS

**`H-9` en su formulación y su severidad — RECHAZADO como MEDIO.** `H` sostiene que el
registro de `F-08` es huérfano porque «su único registro vive en §19 de un documento que §17
L7599 declara **temporal**: *«`docs/evolucion/` … se retira tras F6»*». **La línea que `H` cita
lo refuta**, y la abrí:

> `11-ARQ:7597` · «| `docs/evolucion/` | **temporal**. Se retira tras F6, **y no antes: F5 y
> F6 necesitan su trazabilidad** |»

`H` cita media línea y omite la mitad que responde a su objeción. Además, la ausencia de
`F-08` en §16 es **correcta**: §16 se autodefine «presiones normativas» (L7175-7176), `F-08`
no lo es, y el propio `H` lo demuestra en los puntos 5 y 6 de su §5.9. Lo que queda es
`I-28`, MENOR. Y con ello **`F-08` pasa de FALLIDA a SUPERADA**.

**`N-3` de `G` — no es un hallazgo y no lo numero.** Es una comprobación en positivo sobre
`X54` y `X58`. La reproduje y coincido: las dos filas están bien escritas. La consigno en §10
como lo que está bien.

### Recuento de hallazgos

```text
CONFIRMADOS      27   8 GRAVES · 8 MEDIOS · 11 MENORES
  de G             9   (I-01 I-02 I-03 I-09 I-10 + su mitad de I-05 e I-06 + I-17 I-18)
  de H            15
  convergentes     2   I-05 e I-06, hallados por los dos por separado
  MÍOS             2   I-15 e I-16
RECHAZADOS        1   H-9 como MEDIO (sobrevive degradado a MENOR: I-28)
NO NUMERADOS      1   N-3 de G: comprobación en positivo
BLOQUEANTES       0   ninguno de los 28 lo es
```

---

## 8 · Correcciones que hago a `G` y a `H`

**A `G`:**

1. **`A2` no es SUPERADA.** `G` la da por superada con reserva porque el modo de fallo
   bloqueante está cerrado. Lo está —lo verifiqué— pero la condición publicada es «las siete
   sedes remiten», es literalmente falsa en dos de siete, y **el propio `G` demuestra en su
   `G-3` que sobrevive una afirmación vigente de que `derivada` es el único terminal, en la
   capa que `D71` designa evaluadora**. Eso es la causa de `A2`, no un hallazgo colateral.
   **FALLIDA.**
2. **`M-3` de `G` es GRAVE, no MEDIO** (`I-05`, argumento en D-1).
3. **`M-4` de `G` es GRAVE, no MEDIO** (`I-06`, argumento en D-2). Y su nota de frontera era
   innecesaria: el hecho es uno y lo encontraron los dos.
4. **Cita mal situada, corregida.** `G` sitúa la regla no cambiada de §2.6.8 en «L1451-1452 y
   L1456». El bloque `diff`-idéntico a `11-base:1374-1377` es **L1450-1453**, y el `2bis`
   idéntico está en **L1454-1459**. El hallazgo sobrevive con la referencia corregida.
5. **Inferencia no sostenida.** `G` afirma que `T148`/`T159` fallan por «la limitación de
   Python 3.10». Reproduje los dos fallos con Python 3.10.12 y la salida dice `workspace check
   falla en el proyecto creado (exit 1)`, que no establece esa causa. Es `A14`, fuera de los
   43, y no cambia nada — pero la atribución no está demostrada y no la adopto.

**A `H`:**

1. **`H-9` rechazado como MEDIO**, por la mitad de línea omitida (§7, RECHAZADOS). **`F-08`
   pasa a SUPERADA.**
2. **`A10` no es FALLIDA.** Su condición es «ONCE, derivadas de §16», y **derivan**: 13
   cabeceras − `PN-4` − `PN-5` = 11, con el total correcto en cuatro sedes. La frase de §16
   L7184 es un defecto distinto, y lo registro como `I-11`. **SUPERADA.**
3. **Dos citas mal situadas en `H-1`:** §7.2 está en **L5208**, no L5203 (que es un carácter
   de flecha); la frase de §7.6 está en **L5292**, no L5296. Corregidas, el hallazgo se
   mantiene íntegro.
4. **Una línea mal situada en `H-6`:** es **L7184**, no L7183.
5. **Alcance de `H-1` acotado.** «El defecto lo introduce la corrección» es medio cierto:
   `git show 7e99388` demuestra que la fila `EJECUTOR` con «`PLT` para cada source change» ya
   existía en §8.3 L5310. Lo nuevo es la **generalización** a cuatro secciones más y a §18, y
   su promoción a dispositivo de cierre de `B-2`.
6. **Consecuencia de `H-8` reformulada.** F6 **no** tendría que decidir el vocabulario: `E-3`
   del documento 17 ya lo escribió y es corpus inmutable. El defecto es que §19 no lo recoge.
   Esto es material para el veredicto: **ningún MEDIO exige arquitectura nueva.**
7. **`H` dio `M-4` por superada sin ver que su ejecución falsifica la disciplina declarada**
   (`I-16`).
8. **`H` no detectó `I-15`**, la cifra CATORCE en el registro de `D77` — que es el residuo
   directo de un hallazgo de su propio eje (`M-1`).

---

## 9 · `D71`–`D86`, verificadas

Fuente, causa, corrección, coherencia y consecuencia. Comprobé además que **ninguna encubre
una decisión nueva del Owner**: donde la había, se registró como presión en vez de tomarla.

| | causa | ¿la corrección responde a su causa? | coherencia con el corpus | consecuencia F5/F6 | ¿decisión nueva del Owner? |
|---|---|---|---|---|---|
| `D71` | `A2` | **sí**: predicado con sede única, L611-612 | **PARCIAL** — el censo L621-624 y `11-ARQ:3925`. `I-03`, `I-09` | F6 construye el validador sobre una lista con dos reglas incomprobables | **no** |
| `D72` | `A1` | **sí**: enum de tres con sede única §3.6 L3806 | **SÍ** — las tres capas coinciden, verificadas | F6 deriva el esquema de `evento` de §3.6 sin ambigüedad | **no** |
| `D73` | `A3` | **sí**: §7.4 L5253-5262 con las dos ramas | **SÍ** — §16 alineado; la formulación retirada no está vigente | `PN-7` cambia de motivo, no desaparece | **no** |
| `D74` | `B-2` | **la mitad** | **NO** — el `EJECUTOR` contradice `C7:83-86`, §1.3 L224, §7.2 L5208, §7.6 L5292. `I-04` | la mitad `PLT` del bloqueante sigue abierta | **no** |
| `D75` | `B-1`,`G-1`,`G-2`,`M-3`,`m-4` | **sí**, verificado contra `01-PROCESOS.md` | **SÍ** — coincidencia campo a campo en `AUD`, `DEU`, `DEP` | F6 compone sin elegir proceso | **no** |
| `D76` | `G-3` | **sí en §8.1** | **NO** — §18, sede canónica, no lleva el gate ni la salida. `I-07`. Y se escribe en `N<n>`: `I-12` | F6 construye `INS-5` sin saber que tiene gate del Owner | **no**: `O12` decía qué falta; `D76` da el productor |
| `D77` | `G-4` | **sí**: doce ids derivados del patrón, verificados | **PARCIAL** — el registro dice CATORCE condicionales. `I-15` | F6 construye doce contratos ciertos | **no**: deriva de un patrón existente |
| `D78` | `A8` | **no**: la norma no cambió y el artefacto no tiene disciplina. `I-02` | **NO** — §2.4, §2.3, §2.9, `X27` no lo alcanzan | F6 materializaría un caché versionado sin regenerador | **no** |
| `D79` | `A9` | **sí** para `4b`; **introduce `I-01`** | **NO** — §2.6.10 L2103 y §2.4 L415-418 | F6 no sabe en qué plano vive `estado/cuarentena/` | **no**, pero deja al Owner un acto cuyo soporte no está clasificado |
| `D80` | `M-6` | **sí en el contrato**: clase, forma, rama, sujeto, salida | **PARCIAL** — la mitad de su cierre (§17) no se hizo. `I-06` | F6 construye en `entrada/` sin decidir | **no** |
| `D81` | `M-9` | **sí**: las catorce del §6.2, verbatim | **SÍ** — verificado contra el brief L435-450 | F6 no inventa el contenido de un gate del Owner | **no**: transcribe la directiva |
| `D82` | `M-7` | **sí**: N 2 · A 4 · M 2 · U 4 y el freno circuito a circuito | **PARCIAL** — `I-12` (se escribe en `N<n>`) e `I-25` | ninguno necesita excepción | **no**, y lo argumenta: la cláusula de `a.7` ya responde |
| `D83` | `M-8`≡`A11`, `F-03` | **sí en el documento 11**, verificado por mí (6 `RC-`, 5 `N<n>` todas de `C6`) | **NO en el registro**: `I-12` | — | **no**: elige renombrar el espacio más nuevo, que es correcto |
| `D84` | `A12` | **sí**, y el argumento sustituto es técnicamente correcto | **SÍ** — una sola aparición de «único escritor» y es la que lo retira | `PN-11` y el futuro `C8` quedan bien delimitados | **no** |
| `D85` | `A6` | **sí**: 5 · 6 · 7, los tres derivados por mí | **SÍ** — «seis fases» sólo en notas históricas | F6 deriva el enum sin ambigüedad | **no** |
| `D86` | `F-05` | **sí**: excepción nombrada, `00-CIRCUITOS` manda | **SÍ** — `kernel/operativo/00-INDICE.md` lo respalda | F6 crea instancias, sin decidir | **no** |

**Ninguna de las dieciséis encubre una elección que sólo el Owner pueda hacer.** Lo comprobé
caso a caso, y donde sí la había —el ensanchamiento de `b.16`— se registró como `PN-13` con
dos salidas escritas y «elegir es del Owner». **Eso es lo correcto, y lo digo.**

**Intactidad, verificada con `git diff --name-only` sobre el rango:**

```text
FICHEROS TOCADOS · 4    00-INDICE.md · 11-ARQUITECTURA-INTEGRADA.md ·
                        CHECKPOINT-ADS-NEXT.md · DECISIONES-Y-CONTRADICCIONES.md
DOCUMENTOS 15, 16, 17   NO APARECEN → INTACTOS ✔
kernel/, packs/, tooling/  NO APARECEN → INTACTOS ✔   (C7 y los esquemas incluidos)
O15 y O16               NO APARECEN en el diff de DECISIONES → INTACTAS ✔
D1–D86                  sin hueco, derivado por mí ✔
O1–O16                  presentes, derivado por mí ✔
D16–D70                 UNA fila tocada: `D67`. Contra la declaración → `I-16`
```

---

## 10 · Lo que está bien, y recuentos recalculados

**Un dictamen que sólo lista defectos no es una medida, y esto afecta a mi veredicto.**

- **La matriz de los 43 está bien construida.** La reconciliación del octavo commit —retirar
  los estados compuestos que producían 46— es correcta, y mi derivación independiente por
  identificadores da exactamente 31·1·2·8·1 = 43, con `A11` absorbido y `A14` excluido. Es la
  cifra que más veces ha fallado en este expediente y esta vez **resiste**.
- **La aritmética de §3.6 y §3.8 cuadra**, en los ocho recuentos que derivé sin leer ningún
  titular: 5 fases · 6 estados · 7 filas · 9 tipos · 54 · 34 · 20 · 42 filas/42 ids · 19
  esquemas · 25. Incluidas las tres que el encargo me pidió desconfiar por nombre.
- **`D72` cierra su bloqueante en las tres capas**, no en una.
- **`D75` resiste abrir el kernel**: cada vía de cada participante de `AUD`, `DEU` y `DEP`
  coincide campo a campo con `01-PROCESOS.md`. Lo comprobé yo.
- **`D84` sustituye un argumento falso por uno técnicamente correcto**, que es más difícil que
  retirar una frase.
- **`D83` renombra el espacio más nuevo y no el contrato**, que es la elección correcta.
- **`PN-13` es un hallazgo real**, derivado de `b.16` y verificado contra `01-PROCESOS.md`,
  con dos salidas escritas y sin tomar la decisión del Owner.
- **`O15` se respeta en sus nueve puntos**, incluido el que dice que no autoriza empezar, y
  `m-1` la reancla sin reescribirla, que es la disciplina correcta con material en voz del
  Owner.
- **La disciplina de inmutabilidad sobre los documentos 15, 16 y 17 se cumplió**, verificada
  con `git diff`.
- **`X54` y `X58` están bien escritos** y son convertibles en prueba sin traducción.
- **Ninguna capacidad no construida se presenta como existente.** §19 lo declara sin adorno y
  el árbol no tiene nada provisionado bajo `estado/`, coherentemente.

**Recuentos recalculados por mí:**

```text
FILAS DE LA MATRIZ            43 · 43 ids distintos · un estado primario cada uno
  SUPERADAS                   32
  FALLIDAS                    10   2 BLOQ · 2 GRAVES · 6 MEDIOS por severidad original
  NO APLICABLE                 1

HALLAZGOS CONSOLIDADOS        28
  BLOQUEANTES                  0
  GRAVES                       8   I-01 … I-08
  MEDIOS                       8   I-09 … I-16
  MENORES                     12   I-17 … I-28
  de ellos INTRODUCIDOS O
  PERPETUADOS POR EL RANGO     6   I-01 (nuevo) · I-04 (generalizado) · I-05 (celda tocada)
                                   I-06 (mitad no hecha) · I-12 (texto nuevo) · I-15 (texto
                                   nuevo). `I-16` es una declaración nueva falsificada por su
                                   propio commit

CORPUS OBLIGATORIO            56 fuentes · 31 517 líneas
  sin asignar                  0
  SIN LECTURA SUSTANTIVA      14 · 3 420 líneas · 10,9 % del corpus
  de las diecinueve del
  primer gate, NO CUBIERTAS   10 de 19
  fichas de capacidad
  no leídas íntegras          13 de 15

DECISIONES                    D1–D86 sin hueco · O1–O16 presentes · D71–D86 verificadas
                              D16–D70: UNA reescrita (`D67`) contra la declaración
FICHEROS DEL RANGO             4 · ninguno en kernel/, packs/ ni tooling/
VALIDADORES                   comprobar_recuentos EN VERDE · T159 y T148 FALLIDAS (A14)
```

---

## 11 · Respuestas expresas a las cinco preguntas del encargo

**`PN-13` y las once presiones: ¿listas para redactar, sin redactar?** **En sustancia SÍ; en
forma entregable NO.** §16 se abre con «Aquí no se redacta ninguna enmienda» y `PN-13` tiene
fuente exacta, contradicción verificada, materia mínima, dos salidas, condición de reversión y
«elegir es del Owner». Ninguna enmienda está redactada, que es lo correcto. **Pero el
documento que va al Owner tiene dos defectos en esa misma materia**: `I-26` (el campo
`ALCANCE` de `PN-13` truncado a media frase) e `I-11` (§16 L7184 enumera diez donde su propio
total dice once, omitiendo precisamente `PN-13`).

**`M-5`, `M-6` y los once `requiere_f6`: ¿contrato completo, sin que F6 elija arquitectura?**
Derivé los once y coinciden: `B-2 M-5 M-6 F-01 F-02 F-04 F-05 F-06 F-07 F-10 F-11`.
**F6 no tiene que elegir arquitectura en ninguno** — y corrijo aquí a `H`, porque el
vocabulario de `F-02` ya está escrito en `E-3` del documento 17. **Pero `M-5` y `M-6` no
tienen su contrato completo en la sede que F6 lee**: §17 sigue diciendo `+4` (`I-06`), y la
mitad literal del cierre de `M-6` está sin hacer. Y `F-01` no es ejecutable para su fin
declarado.

**`F-08`: ¿vehículo de trazabilidad, o trabajo normativo huérfano?** **Tiene vehículo, y no es
huérfano.** §19 L7801 le da fichero, cambio exacto, propietario («el Owner: es su documento») y
fase (**F5**); la matriz L1233 le da el atributo `requiere F5 · sí · sin PN`; y §17 **L7597**
declara expresamente que `docs/evolucion/` **no se retira antes de F6 porque F5 y F6 necesitan
su trazabilidad**. Su ausencia de §16 es correcta: no es presión normativa. Residuo MENOR:
`I-28`.

**`F-01`: ¿la discrepancia entre §8.2 y `01-PROCESOS.md` permite entrar en F5, o invalida la
arquitectura?** **Permite entrar en F5 y no invalida la arquitectura de composición.**
`DIS/Reconstruccion` denota la capacidad `DIS` operando por uno de sus seis métodos, y la
condición de activación es `C-DIS` en las dos formulaciones: **el conjunto de participantes de
`A2`–`A7` es idéntico bajo las dos lecturas**, y `diseno/03-ESCALA-DE-NOVEDAD.md` L251-261
resuelve quién calcula el método y cuándo. **Lo que está mal es el registro de su remedio**: la
sede nombra `01-PROCESOS.md` y `00-CIRCUITOS.md` y omite `b.16:895` y `a.6:495`, que llevan la
misma cadena, son material APROBADO y que §17 L7585 declara intocable. Ejecutado como está
escrito, el kernel diría `DIS` y su fuente normativa seguiría diciendo `DIS/Reconstrucción`, y
la verificación mecánica «contra la fuente» que el checkpoint invoca como motivo **seguiría
fallando**. Por eso la fila es FALLIDA y la arquitectura no lo es.

**¿Está `B-2` completamente determinado para `PN-13`?** **La mitad `DOM`/`SEG`/`DIS`, sí, y
está bien hecha.** La mitad `PLT`, **no**: se cierra con una atribución que `C7` y tres
secciones de la propia F4 desmienten (`I-04`). El remedio está determinado —la capacidad con
custodia es `CON`, obligatoria en `SIS`, `DEU` y `DEP`; la convergencia es de `ENT` por
`C7:89`— y por eso no es BLOQUEANTE, pero no está hecho.

---

## 12 · Limitaciones de mi adjudicación, sin adorno

```text
1  NO HE LEÍDO EL CORPUS OBLIGATORIO ÍNTEGRO. He verificado por muestreo dirigido, que es lo
   que el encargo pide, pero eso significa que **no puedo certificar que las catorce fuentes
   que nadie abrió no contengan algo que refute o agrave lo de arriba**. En particular el
   documento 15, del que cuelga `D64`.

2  EL PUNTO MÁS DÉBIL DE MI PROPIO JUICIO ES LA SEVERIDAD, NO EL HECHO. Los hechos de `I-01`
   a `I-28` están todos verificados en su fichero y su línea; la frontera entre GRAVE y MEDIO
   la he trazado yo con un criterio —«¿construiría F6 algo distinto de lo que el contrato
   quiere?»— que es defendible y no es el único posible. Si alguien graduara `I-05`, `I-06`
   e `I-08` como MEDIOS, el veredicto NO cambiaría, porque la cobertura y las diez filas
   fallidas ya lo determinan. Lo digo para que se vea que el veredicto no depende de mi
   graduación.

3  `I-01` DEPENDE DE UNA LECTURA. Sostengo que por §2.4 la cuarentena queda versionada. Si
   alguien argumentara que hereda la excepción de ruta por analogía, el hallazgo bajaría a
   MEDIO y seguiría siendo defecto, porque entonces la única copia de lo divergente no
   sobrevive a la máquina. Lo que NO admite lectura es que la ruta no tiene plano, ni ciclo,
   ni fila, ni prueba.

4  NADA DE ESTO ESTÁ CONSTRUIDO. No hay esquema de `evento`, ni validador del diario, ni
   runtime, ni un fichero bajo `estado/`. Todos los hallazgos sobre el protocolo son sobre
   TEXTO. Un contrato contradictorio no es un sistema roto: es un sistema que no se puede
   construir sin decidir cuál de las dos frases vale.

5  NO PUDE EJECUTAR LA BATERÍA COMPLETA DE VALIDADORES: excede el tiempo disponible. Ejecuté
   tres. Los resultados de `G` sobre los demás NO los he reproducido y no los adopto como
   propios.

6  NO HE RESUELTO `I-08` CONTRA `b.3` NI `b.5`, que nadie abrió. La evidencia directa es
   fuerte y la registro como GRAVE, pero la refutación posible vive donde no he mirado. Si
   apareciera, `I-08` caería y el veredicto seguiría en pie por lo demás.

7  DONDE ESCRIBO «VERIFICADO», LO ABRÍ. Donde no pude demostrar una resolución —los tres
   puntos del final de §6— lo he declarado INSUFICIENTE en vez de promediar entre G y H.
```

---

## 13 · VEREDICTO

# INSUFICIENTE PARA F5

---

## 14 · Condición exacta para F5, ordenada por lo que desbloquea

`SUFICIENTE` exige **todas** las condiciones del encargo. Fallan cuatro, y por ese orden:

### Nivel 0 · lo que impide siquiera emitir un juicio de suficiencia

```text
C-0.1  CUBRIR LAS CATORCE FUENTES OBLIGATORIAS QUE NADIE ABRIÓ, empezando por
       `15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` (652 líneas), que está asignada a los DOS
       revisores y no la leyó ninguno, y siguiendo por las DIEZ de las diecinueve que el
       primer gate ya había omitido una vez: `diseno/00`, `01`, `02`, `04`, `05`, `C2`, `C3`,
       `entrada/00`, `02`, `04`. Más `C4` y `a-ENMIENDA-E1-ENC.md`, y `a-ENMIENDA-E2` íntegro.
       DESBLOQUEA: el juicio mismo. Sin esto no hay gate, hay una muestra.

C-0.2  LEER ÍNTEGRAS LAS TRECE FICHAS DE CAPACIDAD que se cubrieron por `grep`, o declarar
       expresamente que la cobertura por atributos basta y por qué.
       DESBLOQUEA: `I-14` y la lectura de `M-5`, que hoy descansan en una ausencia.
```

### Nivel 1 · las ocho GRAVES

```text
C-1.1  `I-03` · retirar `11-ARQ:3925` y `:3945-3947` de la lista de la capa B, o reescribirlas
       sobre los DOS terminales y sin `#intentos` ni `agotado`.
       DESBLOQUEA: `A2`, que hoy es FALLIDA por esto. Es la corrección más barata del lote y
       la que cierra un BLOQUEANTE.

C-1.2  `I-04` · corregir la atribución del `EJECUTOR` en §8.0 L5380, §8.1 L5511, §8.2 L5677,
       §8.4 L6006 y en la columna de §18: `PLT` ejecuta materializar una fuente (`C7:82`) y
       retirar rama abandonada (`C7:92`); rama, commit, push y PR los ejecuta la capacidad con
       custodia; merge y convergencia, `ENT`.
       DESBLOQUEA: `B-2`, el segundo BLOQUEANTE fallido. El remedio no exige decidir nada:
       `C7:80-92` ya dice quién.

C-1.3  `I-07` · llevar a §18, fila `INS-0`–`INS-5`, el gate «`INS-5` baseline aprobado por el
       Owner» y su salida —baseline y clasificación de desconocidos críticos—, con la misma
       forma que la fila `A2`–`A7` ya usa para `A3`.
       DESBLOQUEA: `G-3`, GRAVE.

C-1.4  `I-06` · añadir `DSP` y `ENC` a §17 L7588 y corregir §16 L7576. Son dos ediciones.
       DESBLOQUEA: `M-5` y `M-6`, y con ellas el `CONTRATO_COMPLETO_PARA_F6` de los dos.

C-1.5  `I-05` · corregir §14 L6801: la reanudación es por checkpoint desde `INS-0`, y
       `estado/` nace en `INS-0`. Y revisar el resto de §14 por el mismo motivo (`I-27`).
       DESBLOQUEA: la coherencia de la sección cuya función declarada es demostrar que no hay
       contradicciones.

C-1.6  `I-01` · elegir el plano de `estado/cuarentena/<TX>/` y escribirlo: clasificación en
       §2.4, fila en §2.3, ciclo (cuándo se vacía), `.gitignore` si es operacional, y una fila
       adversarial. Y reconciliarlo con la alternativa D de §2.6.10 y con el bloqueo de `SEG`.
       DESBLOQUEA: el único punto donde F6 tendría que elegir arquitectura. **Es la única
       condición de esta lista que exige una decisión de diseño, y son cinco líneas.**

C-1.7  `I-02` · someter `estado/deriva/<ID>.abierta` a las cinco piezas: nombrarlo en la
       excepción de ruta de §2.4 L417-418, en el `.gitignore` de L445 y L1316, darle fila en
       §2.9 y fila adversarial, listarlo en §2.3, y crearlo en el paso E de §2.6.9. Y cambiar
       la NORMA de §2.6.8 L1450-1453 para que el lector mire el marcador y no el diario.
       DESBLOQUEA: `A8`, y la reclamación de que no hay segundas fuentes de verdad.

C-1.8  `I-08` · o instanciar `<CAP>:revisión` para `DOM` y `SEG` en `DEU` y `DEP`, o registrar
       la ausencia como noveno externo con propietario y fase, o declarar por qué (b) L834-836
       no obliga. Cualquiera de las tres cierra; ninguna la toma esta tanda.
       DESBLOQUEA: la afirmación «vía declarada para cada participante».
```

### Nivel 2 · los ocho MEDIOS

```text
C-2.1  `I-09` · corregir el censo de L621-624: §2.6.5 y §2.6.11 dentro, §2.6.4 y §2.6.9 fuera,
       y retirar «ninguna lo redeclara» o corregir L894.
C-2.2  `I-10` · sustituir el argumento de L2192-2193 por la restauración verificada, y retirar
       «estado mixto» de L2194, L1459 y L2343 salvo para el acto (ii) de `4b`.
C-2.3  `I-11` · «`PN-6` a `PN-13`» en §16 L7184.
C-2.4  `I-12` · `INS-5`, `INS-7`, `INS-0` en `D76`, `D82` y el `D67` corregido del registro.
C-2.5  `I-13` · llevar a §19 L7795 el vocabulario que `E-3` escribió: quince capacidades con
       sufijo `:` opcional para la variante declarada.
C-2.6  `I-14` · declarar si abrir una `iniciativa` de campaña cabe en la autoridad de la ficha
       de la capacidad líder, y si no, registrar su extensión como las otras seis.
C-2.7  `I-15` · TRECE en `DECISIONES:259`.
C-2.8  `I-16` · o reconocer la excepción de `D67` en las tres sedes que declaran que
       `D16`–`D70` conservan su texto, o mover esa corrección fuera del registro.
```

### Nivel 3 · los doce MENORES

```text
C-3.1  `I-26` · completar la frase truncada de `PN-13` ALCANCE. VA AL OWNER: es prioritario
       pese a ser MENOR.
C-3.2  `I-19` · derivar la cifra de la cabecera de §15.8 o retirar la afirmación de que deriva.
C-3.3  `I-17` `I-18` `I-20` `I-21` `I-22` `I-23` `I-24` `I-25` `I-27` `I-28` · ediciones de
       una a tres líneas cada una, sin efecto arquitectónico.
```

### Lo que NO hay que hacer

```text
·  NO redactar ninguna enmienda de `b.16`: es del Owner, y `PN-13` está bien planteada.
·  NO tocar `C7` ni ningún fichero de `kernel/operativo/`: F6, y `PN-11`/`C8` primero.
·  NO tocar los documentos 15, 16 y 17: son inmutables, y esta tanda lo respetó.
·  NO iniciar la adopción de PesquerApp: `O15` dice qué será cuando ocurra, no que ocurra.
·  NO volver a aplicar la corrección quien la recibe sin un gate posterior. Ésta es la novena
   tanda, la segunda que se mira, y las dos veces ha aparecido algo que la corrección
   introdujo. Seis de los veintiocho hallazgos de arriba son de esa clase.
```
