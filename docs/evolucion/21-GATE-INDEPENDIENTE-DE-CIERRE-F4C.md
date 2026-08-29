# GATE INDEPENDIENTE DE CIERRE DE F4c CON MANIFIESTOS VERIFICABLES

> **Veredicto, en una línea:**
> # INSUFICIENTE PARA F5
>
> **`F4c` NO se cierra. Sigue ABIERTA. `F5` NO queda autorizada.**
> **`C-L.5` queda CERTIFICADA por primera vez, y el gate NO falla por cobertura.**

## 1 · Identidad y procedencia

```text
CANDIDATA JUZGADA   review/f4c-post-gate-cobertura-candidate-20260829
COMMIT CANDIDATO    7764cca69c9fbb7c3e89b70efdae7d6990f6c3b6
ÁRBOL DEL CANDIDATO 03116b33bf4d8e996d8eccae51db927f4667ca58
RAMA DEL GATE       gate/f4c-cierre-con-manifiestos-20260829, creada en ese commit
                    exacto, sin upstream
HEAD DURANTE EL GATE 18cbfb57fe2286bb68011a31a8f3d07556d7aea9
ÁRBOL DE ESE HEAD    6e9d662d6cc8ff6e289c391490e70285c8a41e9e
DIFERENCIA           git diff --stat 7764cca..18cbfb5 → 1 fichero · 140 inserciones ·
                     0 supresiones — el manifiesto previo de asignación, y nada más

REVISOR P           material normativo y protocolo transaccional. D105 · `abandonada` ·
                    `deriva` · identidades · `fsync` · W17 · recuperación · marcador ·
                    commit · PN-15 · compatibilidad normativa.   20 fuentes asignadas
REVISOR Q           derivación, kernel operativo y batería. D104 · las cuatro vías
                    tipadas · AUD · DIR · ancla de posición · catálogo estático frente
                    a regla por item · G-15 · G-16 · Git fallando cerrado.
                                                                 31 fuentes asignadas
ADJUDICADOR R       recibió los dos dictámenes YA CERRADOS, cruzó asignación contra
                    lectura, reprodujo él mismo los bloqueantes y emitió el veredicto
                    único.                                        9 fuentes asignadas

INDEPENDENCIA       los tres son agentes NUEVOS con contexto limpio. Ninguno escribió
                    F4, ninguno aplicó D16–D106, ninguno es autor de las correcciones,
                    ninguno fue revisor A–O de las pasadas anteriores.
                    P y Q trabajaron EN PARALELO y no se vieron.
                    R NO resolvió por mayoría: abrió cada afirmación material en su
                    fichero y su línea, reprodujo los hallazgos bloqueantes en copias
                    de /tmp, RECHAZÓ la primera razón de veredicto de P y añadió cuatro
                    hallazgos propios.

EL COORDINADOR      emitió y commiteó el manifiesto previo de asignación ANTES de que
                    existiera ningún revisor, repartió el corpus, verificó por su cuenta
                    las afirmaciones más consecuentes, corrigió a P en un punto de hecho
                    para que R lo adjudicara, transcribió y validó.
                    NO emite suficiencia y NO ha corregido ningún hallazgo.
                    Es el autor material de las tandas anteriores, y por eso su juicio
                    no cuenta aquí.
```

**Una corrección del adjudicador al encargo, y va por delante.** El encargo del gate daba
`03116b33…` como «TREE» junto a `HEAD 18cbfb5…`. Son de commits distintos: `03116b33` es el
árbol del **candidato** `7764cca`; el árbol de ese `HEAD` es `6e9d662`. `R` lo verificó con
`git rev-parse` sobre los dos y lo hizo constar. **Tiene razón, y consta.** El objeto normativo
juzgado es idéntico en los dos: la única diferencia entre ambos commits es el propio manifiesto.

**La declaración de `P` sobre el mismo punto se confirma:** `P` detectó por su cuenta que `HEAD`
no era el commit candidato, comprobó `git diff --stat 7764cca..18cbfb5` y obtuvo el mismo
resultado. `Q` hizo esa comprobación por separado. **Los tres llegaron a ella solos.**

## 2 · El manifiesto previo de asignación

Lo exige `D106`, y existe porque el gate anterior no pudo cerrar su propia regla: su adjudicador
`O` declaró la cláusula más dura de `C-L.5` **NO CERTIFICABLE**, porque ningún revisor había
declarado **qué se le había asignado** y `asignado − leído` no era calculable. Es `O-04`.

```text
FICHERO   docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md
LÍNEAS    140
SHA-256   c843b0c341183859b7f0f07db78cc67eade7ef98c4a96ad3edee23c769d2a976
COMMIT    18cbfb57fe2286bb68011a31a8f3d07556d7aea9   2026-08-29 22:15:07 +0200
          1 fichero · 140 inserciones · 0 supresiones — el commit contiene ESO Y NADA MÁS

ORDEN VERIFICADO POR EL REVISOR P CON `git log`: el commit del manifiesto es ANTERIOR a la
creación de los revisores. No se repartió nada antes de publicarlo, y no se ha modificado
después. No hubo ADDENDUM: ninguno de los tres pidió una fuente fuera de su asignación.
```

**Se transcribe íntegro y literal a continuación.** Es el mismo fichero que está en el árbol
—[`F4C-ASIGNACION-GATE-CIERRE-20260829.md`](verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md)—;
cualquiera puede recalcular su SHA-256 y comparar.

---
### MANIFIESTO PREVIO DE ASIGNACIÓN — GATE INDEPENDIENTE DE CIERRE DE F4c

> **EMITIDO ANTES DE REPARTIR.**
>
> Este documento se escribe y se commitea **antes de crear o contactar a ningún revisor**.
> Una vez commiteado **no se modifica**. Si hiciera falta ampliar una asignación, se publica
> un **ADDENDUM** nuevo con su motivo, commiteado antes de entregar la fuente adicional.

#### 1 · Objeto del reparto

```text
COMMIT CANDIDATO   7764cca69c9fbb7c3e89b70efdae7d6990f6c3b6
TREE SHA           03116b33bf4d8e996d8eccae51db927f4667ca58
REFERENCIA REMOTA  refs/heads/review/f4c-post-gate-cobertura-candidate-20260829
FECHA              2026-08-29
RAMA DEL GATE      gate/f4c-cierre-con-manifiestos-20260829, creada en ese commit exacto,
                   sin upstream
```

#### 2 · Identidad prevista de los revisores

```text
REVISOR P     material normativo y protocolo transaccional.
              Foco: D105 · `abandonada` · `deriva` · identidades · `fsync` · `W17` ·
              recuperación · marcador · commit · `PN-15` · compatibilidad normativa

REVISOR Q     derivación, kernel operativo y batería.
              Foco: D104 · las cuatro vías tipadas · propietaria · obligatoria ·
              condicional · item propio enlazado · `AUD` · `DIR` · ancla de posición ·
              catálogo estático frente a regla por item · `G-15` · `G-16` ·
              Git fallando cerrado · excepción exacta de seis ficheros

ADJUDICADOR R recibe los dos dictámenes YA CERRADOS, cruza asignación contra lectura,
              reproduce él mismo los bloqueantes y emite el veredicto único

INDEPENDENCIA EXIGIDA A LOS TRES — ninguno puede haber escrito F4, haber aplicado
              `D16`–`D106`, ser autor de las correcciones, haber sido revisor `A`–`O`,
              ni haber visto el dictamen del otro antes de cerrar el suyo.
              `P` y `Q` trabajan EN PARALELO y sin verse.
```

#### 3 · Dos rutas del encargo que no existen, y cómo se resuelven

El encargo asigna a `P` dos contratos por títulos que **no existen en el árbol**:
`C1-ESTADOS-Y-TRANSICIONES.md` y `C7-INTEGRACION-DISTRIBUIDA.md`. Los contratos `C1` y `C7`
reales son `C1-EQUIPO-ROL-AGENTE-METODO.md` y `C7-GOBIERNO-GIT-MULTI-SOURCE.md`, **y son
inequívocos por número: hay exactamente uno de cada**. Se asignan esos, y consta aquí en
lugar de resolverse en silencio.

#### 4 · Reparto, fuente a fuente

Ruta · líneas · SHA-256 · a quién se asigna. Todo derivado del árbol `03116b33…`, no copiado.

| ruta | líneas | SHA-256 | asignada a |
|---|---|---|---|
| `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | 2163 | `a88609167dbbea2818b7f2e68cbd4c6fc704cb7e2245ee0a2c873052486fd159` | **P+Q+R** |
| `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | 1257 | `8243034f286160cc89330af95b49f558af0dd16d1b36a37ccbdf02f74a79d185` | **P+Q+R** |
| `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` | 1650 | `18f876d4cd47a2f7cfde15594f98696cfacf750607cd23811dd40ffb36d6c29c` | **P+Q+R** |
| `docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` | 3665 | `1e71366b10d2293802db435de14953771ebd8fc13b426acedd7c0efe21cdb496` | **P+Q+R** |
| `docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md` | 801 | `d7d2e4fa3f878e0c010d979e89affdb63462cc6fdd6628ed885d3a760bde09d1` | **P+Q+R** |
| `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 9280 | `84063c2a344a2d15025b7e2b121d5a973c77dc57b0f1e1119eb13b1ca1ccb474` | **P+Q+R** |
| `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 725 | `3be45994f4d00e82d4a136a2140c738b926a3baee4811e757d523125e4239959` | **P+Q+R** |
| `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 2051 | `76ed2d768cdb4db8d8cce6823e7d34ac834fd0a584409644ea373993bb717e74` | **P+Q+R** |
| `docs/rediseno/a-CAPACIDADES-APROBADA.md` | 1132 | `10cafb5ceee44f576d327ce614c14c86eb7b22ff43c3dfb82918b785eb36fb04` | **P** |
| `docs/rediseno/b-RECORRIDO-APROBADA.md` | 1288 | `f8cb974316e283fa2f16f9ecdd3b94ac19bf4a20cf5816cd155a2449f02719b4` | **P** |
| `docs/rediseno/a-ENMIENDA-E1-ENC.md` | 211 | `18dae19523b25ed4a2370ea9c1d23d68beb578f9365bd54587d2f2821093d4da` | **P** |
| `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | 230 | `9d5a23806fc33fc1d76ba6be9b46ae3499c729c1f11203f80b32550c658ed2eb` | **P** |
| `kernel/KERNEL.md` | 1590 | `aa635dff79e73fe13e271cb115653ebc042dc834d32007c634c8ee1df07e3150` | **P** |
| `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | 161 | `825f15a914c10d6f07f74e62967f93743efcf629a13379acb3947e70e2952ffa` | **P** |
| `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | 539 | `3ee58ca4bc47988d4e6bdd652e2ea5de79ebcf8be79270664c0bd4b4cf391510` | **P** |
| `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | 150 | `d56bf6b81e0fe4a9b3ba811f1adf57748cbae65692db557d15960c8506f84234` | **P** |
| `kernel/operativo/contratos/C4-MATERIALIZACION.md` | 170 | `670289180e59b176743571a22f22047d20792db266b6426c1c91bd2fd3c1ee81` | **P** |
| `kernel/operativo/contratos/C5-HANDOFF.md` | 115 | `af6f1a4c4f5def8da0dcecee8ea57c17516b41bbbd4abe963460c21024cc7b9e` | **P** |
| `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` | 336 | `14805a79aeb07f314a55913864ee7d359ead05a932d59b207b66b6279d3a41e9` | **P** |
| `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | 250 | `83f82e2be4756a4651e61f1883d2a99f1d141954097a6e4176a3482a951fc69c` | **P** |
| `kernel/operativo/recorrido/01-PROCESOS.md` | 564 | `98b5cbc836121044a1b3b38690331325cd730ac71d1f30da69482937c392ee85` | **Q** |
| `kernel/operativo/esquemas/proceso.yaml` | 49 | `bd391d5acddff1342ce307829dfb8494df535dbd1924d44948d1e17176440dcc` | **Q** |
| `kernel/operativo/capacidades/APR/CAPACIDAD.md` | 95 | `a8709115309095849707e2d42290631dca6b3de95d49cc2c3c7ffa4e0546d708` | **Q** |
| `kernel/operativo/capacidades/ARQ/CAPACIDAD.md` | 104 | `6ca11b5f09883e24834f770e61963ae69ca738770ffb1de64f7be0afe4757a47` | **Q** |
| `kernel/operativo/capacidades/CON/CAPACIDAD.md` | 107 | `e0f79e6c3a467302c3d16aa5ee4ccb45583daf146d1676b2b06995419656c5d5` | **Q** |
| `kernel/operativo/capacidades/DIS/CAPACIDAD.md` | 147 | `06f019010d45771fd2a125f9f08f88159b45f15e9f83fd2404c7f2a23f32ad06` | **Q** |
| `kernel/operativo/capacidades/DOM/CAPACIDAD.md` | 135 | `926c7144cb098caaa0b87cdebb5c49b955b74832bc238e66d501ecbb2a635bb3` | **Q** |
| `kernel/operativo/capacidades/DSP/CAPACIDAD.md` | 152 | `acb292f882e77d74693caaab3e392a0d691e988cf875ca4394c59f859ebe7937` | **Q** |
| `kernel/operativo/capacidades/ENC/CAPACIDAD.md` | 174 | `f71b8e43f6e2d66f0801d53ce6e018806d33ef9b5ad5b3300bf1d38fe834d946` | **Q** |
| `kernel/operativo/capacidades/ENT/CAPACIDAD.md` | 123 | `91a81d3cf1cbfa619b7b69553a01810d7074b419fc7e2efb5f8ff2f8f9e7f9ed` | **Q** |
| `kernel/operativo/capacidades/INV/CAPACIDAD.md` | 96 | `47412638e7552da14b7bb89e590aea2f37cc61116c83b902e32952647380ed36` | **Q** |
| `kernel/operativo/capacidades/PLT/CAPACIDAD.md` | 108 | `a5f87977c58ed1d0d4deb3504d664a47fc90382a9790986e5aa277f1dad130d2` | **Q** |
| `kernel/operativo/capacidades/PRD/CAPACIDAD.md` | 105 | `e83b0e08272e219db0c5cc2e17b6d1a95dc4304a9f381d3acfe9c76ff528e3b3` | **Q** |
| `kernel/operativo/capacidades/SEG/CAPACIDAD.md` | 135 | `19bfd38a7a24b57fbec8365327926f7e281092a9e33a06e59355cfda5a5e5a13` | **Q** |
| `kernel/operativo/capacidades/SIS/CAPACIDAD.md` | 119 | `02089f36d124435669b7cf14cf46abd1365a860a4842b739663310b8ceb41628` | **Q** |
| `kernel/operativo/capacidades/USO/CAPACIDAD.md` | 94 | `65f144e4a5c756ef97596a997673d7ad73c194ee6936e616bafd434302ff5d0d` | **Q** |
| `kernel/operativo/capacidades/VER/CAPACIDAD.md` | 135 | `91a16b482629daf3455a3c6963a0568a7a68bcd2bd5553e7540d8c9edbfaf0e2` | **Q** |
| `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 1109 | `c3ed5dffeb281219f5dd7cecf072279c61967d27244804628d5fa2489a745d27` | **Q** |
| `docs/evolucion/verificacion/README.md` | 102 | `a4fb2738cb3112e0baa7c1230bb27c6765c1e1253092f08da76fe8c9fa9ad3c6` | **Q** |
| `docs/evolucion/00-INDICE.md` | 111 | `ed673d814a0e008c8f0eeed1a685c2e3675193effef85a893ab9b210ea6cd8b1` | **Q** |
| `kernel/operativo/entrada/00-INDICE.md` | 28 | `315b2790cb66bb4c2c84272468675c8e77fb5a26b8cc2b95ff56db7ee266ddb1` | **Q** |
| `kernel/operativo/entrada/02-CIRCUITO.md` | 145 | `750d39a29f05e7f2b037f9c246c9869ba80edec493e104e206baadda19c09c70` | **Q** |
| `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | 187 | `1716bd3d8b48107d28a93e4297a6d93c0e6125107c0cc14811f092641e3d0cd2` | **Q** |

#### 5 · Totales derivados

```text
FUENTES OBLIGATORIAS        43     comunes a P, Q y R    8
                                   sólo P                12
                                   sólo Q                23

ASIGNACIONES                59     cada fuente común cuenta TRES —P, Q y R—,
                                   más 12 de P y 23 de Q

FUENTES SIN ASIGNAR          0

LÍNEAS OBLIGATORIAS     31 888     P lee 8 comunes + 12 propias
                                   Q lee 8 comunes + 23 propias
                                   R lee las 8 comunes, y cualquier fuente sobre la que
                                     exista discrepancia material
```

#### 6 · Regla de cierre, declarada por delante

```text
CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA.

Se evalúa cruzando ESTE manifiesto con los MANIFIESTOS DE LECTURA que cada revisor
entrega dentro de su dictamen: `asignadas − leídas íntegramente`. Si ese conjunto no
está vacío, el veredicto sólo puede ser INSUFICIENTE PARA F5, con independencia de los
hallazgos.

Ni un `grep`, ni un resumen previo, ni un índice, ni la asignación misma equivalen a
lectura. Cada revisor recalcula el SHA-256 de cada fuente que declara haber leído, y
aporta dos anclas verificables de regiones separadas.
```

#### 7 · Por qué existe este documento

Lo exige `D106`, y lo exige porque el gate anterior no pudo cerrar su propia regla. Su
adjudicador `O` declaró la cláusula más dura de `C-L.5` **NO CERTIFICABLE**: los tres
revisores habían declarado con honestidad qué leyeron y qué no, y **ninguno declaró qué se
le había asignado**, con lo que `asignado − leído` no era calculable. Es `O-04`.

**Con este manifiesto, esa resta es calculable por primera vez.**

---

## 3 · Manifiestos de lectura y el cruce que el manifiesto existe para hacer

Cada revisor recalculó con `sha256sum` el SHA-256 de cada fuente que declara haber leído y
aportó **dos anclas verificables de regiones separadas** de cada una. Los manifiestos completos
—fuente a fuente, con sus anclas y sus líneas— están dentro de los dictámenes literales de las
secciones 5, 6 y 7. Aquí va el cruce, derivado de ellos.

```text
                   ASIGNADAS   LEÍDAS ÍNTEGRAS   PARCIALES   NO ABIERTAS   ASIGNADAS − LEÍDAS

  REVISOR P            20            20              0            0              ∅
  REVISOR Q            31            31              0            0              ∅
  ADJUDICADOR R         9             9              0            0              ∅
                     ────          ────                                        ────
  ASIGNACIONES         59            59              0            0              ∅

  FUENTES DISTINTAS    43   ·   8 comunes a los tres · 12 sólo P · 23 sólo Q
  LÍNEAS               P 21 592 comunes propias incluidas · Q 25 716 · R 21 732
  SHA-256 RECALCULADOS 59 · los 59 coinciden con el manifiesto previo
```

**Y una comprobación que sólo el adjudicador podía hacer, y que hizo.** `R` no se limitó a
verificar sus nueve: **recalculó `wc -l` y `sha256sum` de las CUARENTA Y TRES filas del
manifiesto contra el árbol**, incluidas las que no le tocaban.

```text
FILAS DEL MANIFIESTO                43
COINCIDEN EN LÍNEAS Y EN SHA-256    43     ← todas, sin una sola discrepancia
FICHEROS AUSENTES DEL ÁRBOL          0
```

> **La regla de cierre de `C-L.5` se cumple, y es la PRIMERA VEZ en el expediente que es
> CALCULABLE.** `R`: «No la presumo en ninguna de las dos direcciones: la calculé.»

**Ninguno de los tres recomienda insuficiencia por cobertura, y los tres lo dicen ANTES del
veredicto, como el encargo manda.** `P`: «El conjunto está vacío. Mi recomendación **NO** es
`INSUFICIENTE PARA F5 POR COBERTURA`.» `Q`: «**NO procede** la recomendación
`INSUFICIENTE PARA F5 POR COBERTURA`, y mi veredicto se emite sobre el fondo.» `R`: «**NO falla
por cobertura.** Es la primera vez que `C-L.5` queda **CERTIFICADA**, y la certifico.»

**Fuentes que algún revisor necesitó y no tenía asignadas: ninguna.** `R` lo declara
expresamente: toda discrepancia material entre `P` y `Q` se resolvió dentro de las ocho comunes,
del código de la batería —asignado a `Q`, abierto por `R` como objeto de reproducción— y de
`01-PROCESOS.md`, abierto igualmente como objeto y nunca como fuente de juicio propio. **No se
pidió ADDENDUM, y por tanto no se emitió ninguno.**

## 4 · Qué comprobó el coordinador por su cuenta, y qué corrigió

El coordinador no juzga. Lo que sí hizo, y consta para que se pueda auditar:

- Emitió y **commiteó el manifiesto previo de asignación solo, antes de que existiera ningún
  revisor**, y no lo tocó después.
- Hizo constar **en el propio manifiesto** que el encargo asignaba dos contratos por títulos
  inexistentes —`C1-ESTADOS-Y-TRANSICIONES.md` y `C7-INTEGRACION-DISTRIBUIDA.md`— y que se
  resolvían por número a `C1-EQUIPO-ROL-AGENTE-METODO.md` y `C7-GOBIERNO-GIT-MULTI-SOURCE.md`,
  **en lugar de resolverlo en silencio**.
- Verificó contra fichero y línea, tras recibir los dictámenes cerrados y antes de entregarlos
  a `R`: `P-01`≡`Q-13`, `P-02`≡`Q-06`, `P-03`, `P-04`, `P-05`≡`Q-08`, `P-06`, `P-08`, `Q-01`,
  `Q-02`, `Q-04`, `Q-05`, `Q-07` y `Q-15`.
- **Reprodujo por su cuenta `Q-04`** —el más serio de la batería— en el árbol real: añadiendo
  bajo `kernel/` un `01-PROCESOS-BIS.md` con una copia íntegra del catálogo de procesos y un
  `C8-SEGUNDA-SEDE.md` que declara por escrito que contradice a `C4`, la batería da **30/30 en
  verde**. Y reprodujo `Q-05`: inyectando `capacidad_productora` dentro de la **prosa** de un
  `criterio_de_satisfaccion`, `FEA part` pasa de `[('DOM',4),('SEG',4)]` a
  `[('DOM',2),('DOM',4),('SEG',4)]`.
- **Corrigió a `P` en un punto de hecho y se lo entregó a `R` para que lo adjudicara**, en vez
  de callarlo o de resolverlo él: la afirmación de `P-08` de que `15-TERCERA-REVISION` lleva
  «tercera pasada consecutiva» sin abrirse **es falsa** — el revisor `N` la leyó íntegra en el
  gate anterior y el adjudicador `O` lo registró, en el documento 20 L372 y L638.

**`R` resolvió esa corrección contra `P`,** confirmó que la premisa de hecho es falsa, y resolvió
además la pregunta que quedaba abierta: **una lectura íntegra hecha en un gate anterior satisface
`C-0.1`, y no hay que rehacerla.** Sus cuatro argumentos están en su §5, y el que decide es que
la lectura de `N` es auditable hoy en un documento que `R` tenía asignado y leyó íntegro.

---

## 5 · Dictamen literal del REVISOR P

> Se transcribe **íntegro y sin cambiar una palabra**. La única alteración es el **nivel de los
> encabezados**, rebajado dos niveles para que anide bajo esta sección. `P` no vio el dictamen de
> `Q` ni ninguna adjudicación antes de cerrar el suyo.

### DICTAMEN DEL REVISOR `P` — GATE INDEPENDIENTE DE CIERRE DE `F4c`

---

#### 1 · Alcance y modo

```text
REPOSITORIO        /home/jose/ads-kernel
RAMA               redesign/kernel-2.0
HEAD AL ABRIR      18cbfb57fe2286bb68011a31a8f3d07556d7aea9
HEAD AL CERRAR     18cbfb57fe2286bb68011a31a8f3d07556d7aea9   (idéntico)
ÁRBOL AL ABRIR     git status --porcelain → VACÍO
ÁRBOL AL CERRAR    git status --porcelain → VACÍO
MODO               SÓLO LECTURA. No he modificado ni un fichero del repositorio, no he
                   creado ninguno, no he hecho commit, no he hecho push y no he ejecutado
                   ninguna escritura de git. El único fichero que escribí vive fuera del
                   repositorio, en el scratchpad de sesión
COMMIT CANDIDATO   7764cca69c9fbb7c3e89b70efdae7d6990f6c3b6
TREE DECLARADO     03116b33bf4d8e996d8eccae51db927f4667ca58
MANIFIESTO         docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md
                   commit 18cbfb5 · 2026-08-29 22:15:07 +0200 · 140 líneas
                   SHA-256 recalculado por mí: c843b0c341183859b7f0f07db78cc67eade7ef98c4a96ad3edee23c769d2a976
                   COINCIDE con el declarado en el encargo
```

**Qué NO soy.** No escribí `F4`, `F4b` ni `F4c`. No apliqué ninguna decisión `D16`–`D106`. No soy autor de ninguna corrección. No fui revisor `A`–`O`. No he visto el dictamen de `Q` y no lo veré.

**Observación procedimental, declarada por delante y no como defecto.** `HEAD` **no es** el commit candidato: la rama ha avanzado un commit sobre el objeto del reparto. Lo verifiqué antes de leer nada:

```
git diff --stat 7764cca..18cbfb5
 .../F4C-ASIGNACION-GATE-CIERRE-20260829.md | 140 +++++++++++++++++++++
 1 file changed, 140 insertions(+)
```

El único cambio es la publicación del propio manifiesto de asignación. **Ninguna fuente asignada difiere del árbol candidato**, y lo confirmo además porque los 20 SHA-256 que recalculé coinciden uno a uno con los que el manifiesto derivó del árbol `03116b33`. Leí, por tanto, el contenido exacto del candidato.

**Modo de trabajo.** Toda cifra de este dictamen está derivada por mí con `grep`, `awk`, `sed`, `wc` o `git`, nunca copiada. Donde escribo «verificado», abrí el fichero en su línea. Donde una sospecha mía se cayó al comprobarla, la escribo igual y digo qué la refutó.

---

#### 2 · Evaluación provisional, y qué cambió

Escribí una evaluación provisional **antes de abrir los documentos 16, 17, 18 y 20**, tras leer sólo el encargo y el manifiesto. La conservo íntegra fuera del repositorio. Sus ocho hipótesis y su sesgo declarado, y qué pasó con cada una:

| # | hipótesis previa | resultado | qué cambió |
|---|---|---|---|
| `H1` | la inversión de `D105` resolverá la circularidad directa, pero **quedará al menos un resto textual de la semántica anterior** en algún validador o ventana | **ACERTADA** | Es `P-02`: la capa B conserva en `11-ARQ:4360` «TODO `abandonada` **DECLARA SU** `deriva`», el verbo de la semántica que `D105` invirtió, cuarenta y seis líneas por encima de la regla que declara la inversión |
| `H2` | la idempotencia de la recuperación es **el punto más frágil**; sospecho una dependencia no determinista en el cuerpo del `deriva` (reloj, orden de escaneo, uuid) | **ACERTADA EN LA CONCLUSIÓN, ERRADA EN LA CAUSA** | No hay reloj ni uuid: el cuerpo es función del `abandonada`, y eso está bien hecho. La fragilidad está donde no la buscaba — en `predecesor`, que sí entra en el `id` y cuya definición canónica **contradice** la que `D105` necesita. Es `P-03`, y es mi hallazgo más grave |
| `H3` | `W17` será consecutiva, sin renumerar `W1`–`W16`, y ninguna ventana previa reclamará ya esa caída | **CONFIRMADA** | Verificado: `W1`–`W16` intactas, `W17` añadida al final, y recorrí las dieciséis: ninguna cubre la caída entre el `abandonada` durable y el `deriva`. La numeración es limpia |
| `H4` | riesgo típico: se declara el `fsync` del fichero y se olvida el del **directorio**, o el marcador se retira antes | **REFUTADA, y lo digo por delante** | `11-ARQ:1239` y `:1871-1878` declaran los dos `fsync` **y el directorio**, y el paso 6 retira el marcador «sólo ahora, y no antes». `D105` hizo exactamente lo que había que hacer aquí |
| `H5` | riesgo: que la prueba posterior de `PN-15` ya pase hoy en verde, lo que la haría vacía | **REFUTADA** | `D106` retira la disyunción. Ejecuté la prueba mentalmente contra `a.11`: `grep 'G2[0-3]'` sobre (a) devuelve **una sola línea** —`a-CAPACIDADES-APROBADA.md:180`, la ficha de `INV`, «freshness (G22+G33)»— que no es fila derogatoria y no está en `a.11`. **La prueba falla hoy, y tiene que fallar** |
| `H6` | riesgo: que `G20`–`G23` hayan sido derogadas de facto sin decirlo | **REFUTADA** | `kernel/KERNEL.md` L640, L682, L692, L748: `G20`, `G21`, `G22`, `G23` presentes e intactas. `a.11` (L1016–1024) no las nombra en ninguna de sus cinco filas. Siguen vigentes, como `PN-15` afirma |
| `H7` | el manifiesto existe; la pregunta abierta es si la cronología de `O16` **fecha** o **inventa** | **RESUELTA A FAVOR** | Fecha, y lo dice. Verifiqué las dos fechas con `git log`: `a713590` = 2026-08-28 10:35:31, `d868bcb` = 2026-08-29 18:05:53. Ambas exactas |
| `H8` | `C-L.5` probablemente SUPERADO si los dos manifiestos existen | **PARCIALMENTE REFUTADA, y es mi hallazgo `P-08`** | La resta `asignado − leído` es calculable por primera vez, y eso es verdad y es mérito. Pero **el universo sobre el que se calcula está elegido, no derivado**, y omite seis fuentes que la condición de nivel 0 vigente nombra por su nombre |

**Sesgo declarado que llevaba, y su suerte.** Entré esperando encontrar «al menos un resto de `deriva_emitida` y al menos una dependencia no determinista». Encontré el primero (`P-02`). El segundo **no existe**: `D105` construye el cuerpo del `deriva` como función pura del `abandonada`, y eso es correcto. Lo digo porque era mi apuesta y perdí.

**Lo que más cambió al leer.** Entré tratando `D105` como el foco y `D106` como formalidad administrativa. Sale al revés: `D105` es la decisión mejor construida del lote —tres alternativas comparadas en tabla antes de elegir, y la elegida es la mínima— y `D106` es la que deja abierto el hueco que decide el veredicto.

---

#### 3 · MANIFIESTO DE LECTURA

Veinte fuentes asignadas. **SHA-256 recalculado por mí sobre el árbol de trabajo, con `sha256sum`.** Los veinte coinciden con el manifiesto de asignación. Las anclas son dos por fuente, de regiones separadas, con su línea.

##### 3.1 · Bloque común (8 fuentes · `P+Q+R`)

| # | ruta · líneas · SHA-256 (recalculado) | cobertura | primera y última sección sustantiva | ancla 1 | ancla 2 |
|---|---|---|---|---|---|
| 1 | `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` · 2163 · `a88609167dbbea2818b7f2e68cbd4c6fc704cb7e2245ee0a2c873052486fd159` | **LEÍDO ÍNTEGRO** | primera `## 1. Por qué existe este documento` (L8) · última `## 31. Registro de cambios de este documento` (L2153) | **L99** · *«obtener aprobación del Owner sobre éxito, riesgos, **timebox** y decisiones fuertes, provisionales o abiertas»* | **L914** · *«Principio aceptado: **Detectar automáticamente; actualizar conscientemente.**»* — la segunda sede de `N-05` |
| 2 | `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` · 1257 · `8243034f286160cc89330af95b49f558af0dd16d1b36a37ccbdf02f74a79d185` | **LEÍDO ÍNTEGRO** | primera `## Corpus obligatorio: inventario y cobertura` (L46) · última `## **INSUFICIENTE PARA F5**` (L1196) | **L853** · *«Añadir `capacidades/ENC/` a la lista de extensiones de ficha de §5.2 **y a §17**»* | **L973** · *«`m-3` es un juicio, no un hecho … dejo el juicio al adjudicador»* |
| 3 | `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` · 1650 · `18f876d4cd47a2f7cfde15594f98696cfacf750607cd23811dd40ffb36d6c29c` | **LEÍDO ÍNTEGRO** | primera `## Inventario de las fuentes del nivel 0` (L41) · última `## ADJUDICACIÓN DEL ADJUDICADOR F` (L1094) | **L101–130** · la enumeración de las diecinueve fuentes que el primer gate omitió | **L116** · la cifra **22** de perfiles de `C2`, contra la **21** de la fila del revisor `E` — el hecho de `N-04` |
| 4 | `docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` · 3665 · `1e71366b10d2293802db435de14953771ebd8fc13b426acedd7c0efe21cdb496` | **LEÍDO ÍNTEGRO** | primera `## El veredicto, por delante` (L55) · última `## 14 · Condición exacta para F5, ordenada por lo que desbloquea` (L3562) | **L2373** · *«`H-5` es un hallazgo sobre material aprobado ((b) L834–836) que ningún revisor anterior tocó»* | **L3566** · `C-0.1` · *«**CUBRIR LAS CATORCE FUENTES OBLIGATORIAS QUE NADIE ABRIÓ**, empezando por `15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` (652 líneas)»* |
| 5 | `docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md` · 801 · `d7d2e4fa3f878e0c010d979e89affdb63462cc6fdd6628ed885d3a760bde09d1` | **LEÍDO ÍNTEGRO** | primera `## 1 · Identidad y procedencia` (L8) · última `## 11 · Ningún hallazgo se ha corregido` (L779) | **L79** · *«`15-TERCERA-REVISION` 651 **← nadie la abrió**»* | **L651** · *«REGLA DE CIERRE … **NO CERTIFICABLE POR MÍ** (`O-04`). No recibí los manifiestos de asignación»* |
| 6 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` · 9280 · `84063c2a344a2d15025b7e2b121d5a973c77dc57b0f1e1119eb13b1ca1ccb474` | **LEÍDO ÍNTEGRO** | primera `# 0 · Resumen ejecutivo` (L92) · última `## C-L.5 · La condición de COBERTURA del próximo gate` (L9213) | **L1128** · *«Se enumeran las **DIECIOCHO**, y el recuento **se deriva de las filas de la tabla, no se escribe**»* | **L8357** · *«Un barrido del documento 11 devuelve **cero** apariciones de «timebox»»* |
| 7 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` · 725 · `3be45994f4d00e82d4a136a2140c738b926a3baee4811e757d523125e4239959` | **LEÍDO ÍNTEGRO** | primera `## 1 · Decisiones tomadas sin consultar` (L11) · última `## 4 · Límites declarados de esta iteración` (L707) | **L346** (`D97`) · *«`G20`, `G21`, `G22` y `G23` … quedan registradas como PRESIONADAS y pendientes de F5, **NO derogadas por F4**»* | **L536** · ADDENDUM DE CRONOLOGÍA · *«la fila `\| O16 \|` entró en el registro el **2026-08-28**, en el commit `a713590`»* |
| 8 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` · 2051 · `76ed2d768cdb4db8d8cce6823e7d34ac834fd0a584409644ea373993bb717e74` | **LEÍDO ÍNTEGRO** | primera `## Estado de las fases` (L1177) · última `## Siguiente acción exacta` (L1978) | **L1141** · *«NADA PROBADO: las **46** filas … **las 9 ventanas RC-1–RC-9 de §2.6.9**, los 11 escenarios negativos … y los 12 escenarios de §14»* | **L2031** · *«QUÉ LLEVAR AL OWNER: las **DOCE** presiones de §16»* |

##### 3.2 · Bloque exclusivo de `P` (12 fuentes)

| # | ruta · líneas · SHA-256 (recalculado) | cobertura | primera y última sección sustantiva | ancla 1 | ancla 2 |
|---|---|---|---|---|---|
| 9 | `docs/rediseno/a-CAPACIDADES-APROBADA.md` · 1132 · `10cafb5ceee44f576d327ce614c14c86eb7b22ff43c3dfb82918b785eb36fb04` | **LEÍDO ÍNTEGRO** | primera `## a.0 — Tres niveles` (L22) · última `## a.12 — Pruebas de conformidad` (L1032) | **L502–503** · *«DOM y SEG aportan **condiciones antes de construir** y revisan después»* | **L1018–1024** · `a.11`, sus **cinco** filas: Derogadas · Sustituidas · Ajustadas · PENDIENTES · Previstas — **ninguna nombra `G20`–`G23`** |
| 10 | `docs/rediseno/b-RECORRIDO-APROBADA.md` · 1288 · `f8cb974316e283fa2f16f9ecdd3b94ac19bf4a20cf5816cd155a2449f02719b4` | **LEÍDO ÍNTEGRO** | primera `## b.1 — Proceso, item, ruta, paquete` (L14) · última `### Barrido de consistencia` (L1275) | **L358** · *«Un `devuelto` sin paquete de corrección deja al item en `en espera` (P7)»* — el hecho de `E5-1` | **L836** · *«`<CAP>:**revisión**`  tras VER  revisan lo construido»* — única aparición normativa, **con tilde** |
| 11 | `docs/rediseno/a-ENMIENDA-E1-ENC.md` · 211 · `18dae19523b25ed4a2370ea9c1d23d68beb578f9365bd54587d2f2821093d4da` | **LEÍDO ÍNTEGRO** | primera `## E1.0 — La decisión` (L25) · última `## E1.4 — Trazabilidad` (L189) | **L30** · *«El trabajo que `ENC` ejecuta es **semántico y conversacional**»* | **L196–197** · *«**siete** MARCAS DE REMISIÓN `[E1]` … cinco recuentos y dos párrafos»* — la cifra de `N-03` |
| 12 | `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` · 230 · `9d5a23806fc33fc1d76ba6be9b46ae3499c729c1f11203f80b32550c658ed2eb` | **LEÍDO ÍNTEGRO** | primera `## E2.0 — La decisión` (L26) · última `## E2.8 — Pruebas de conformidad` (L225) | **L30** · *«ADS PROJECT  !=  REPOSITORIO DE CÓDIGO»* | **L146** · `## E2.4 — a.11: `G29` pasa de «sobrevive» a «revisada»` — la prueba de que **lo no nombrado sobrevive** |
| 13 | `kernel/KERNEL.md` · 1590 · `aa635dff79e73fe13e271cb115653ebc042dc834d32007c634c8ee1df07e3150` | **LEÍDO ÍNTEGRO** | primera `## K-1 — Arquitectura de tres capas` (L10) · última `### G50 — Regla final de separación` (L1586) | **L690** (`G21`) · *«**El gate de salida del Circuito 0 lo fija este documento y NO es negociable por el sistema** (G22)»* | **L692–748** · `G22` con su `#### Timebox` (L694) y `### G23 — Product Baseline` (L748), presentes e intactos |
| 14 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` · 161 · `825f15a914c10d6f07f74e62967f93743efcf629a13379acb3947e70e2952ffa` | **LEÍDO ÍNTEGRO** | primera `## Los siete conceptos` (L7) · última `## Cómo se lee un contrato de rol` (L150) | **L118** · *«REGLA: la autoridad de un rol es **SIEMPRE** un subconjunto de la de su capacidad»* | **L136** · `## Qué NO puede declarar un rol` |
| 15 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` · 539 · `3ee58ca4bc47988d4e6bdd652e2ea5de79ebcf8be79270664c0bd4b4cf391510` | **LEÍDO ÍNTEGRO** | primera `## Los cuatro conceptos, separados` (L7) · última `## Catálogo de perfiles del kernel` (L100) | **L30** · *«La asignación es **determinista y explicable**»* | **L500** · un bloque ```` ```yaml ads:perfil-agente ```` — derivé el censo: `grep -c '^id: perfil:'` = **21** |
| 16 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` · 150 · `d56bf6b81e0fe4a9b3ba811f1adf57748cbae65692db557d15960c8506f84234` | **LEÍDO ÍNTEGRO** | primera `## Los diecisiete elementos del procedimiento` (L7) · última `## Método frente a criterio profesional` (L138) | **L10** · *«`esquemas/metodo.yaml`: los diecisiete de abajo más `id`»* | **L140** · *«Un método no sustituye al juicio: lo **enfoca**»* |
| 17 | `kernel/operativo/contratos/C4-MATERIALIZACION.md` · 170 · `670289180e59b176743571a22f22047d20792db266b6426c1c91bd2fd3c1ee81` | **LEÍDO ÍNTEGRO** | primera `## El algoritmo de materialización` (L8) · última `## Ejemplo completo de materialización` (L134) | **L43** · `## Cuántos agentes por rol` | **L125** · *«PROHIBIDO materializar una capacidad «por si acaso», sin paquete que la necesite (T12)»* |
| 18 | `kernel/operativo/contratos/C5-HANDOFF.md` · 115 · `af6f1a4c4f5def8da0dcecee8ea57c17516b41bbbd4abe963460c21024cc7b9e` | **LEÍDO ÍNTEGRO** | primera `## La regla que evita el rebote infinito` (L17) · última `## Handoff y checkpoint` (L105) | **L36** · *«Todo handoff del sistema se declara con un bloque `ads:handoff` conforme a …»* | **L108** · *«con versiones, `freshness`, y las decisiones del Owner captadas. Si `based_on` cambió, …»* |
| 19 | `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` · 336 · `14805a79aeb07f314a55913864ee7d359ead05a932d59b207b66b6279d3a41e9` | **LEÍDO ÍNTEGRO** | primera `## La relación que sustituye a la anterior` (L14) · última `## Lo que este contrato no autoriza` (L326) | **L30** · *«N2  un ADS Project tiene UN ÚNICO repositorio de control»* | **L330** · la lista de lo que `C6` **no** es: *«servicio Git · servicio de locks · gestor de submodules · tooling de monorepo»* |
| 20 | `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` · 250 · `83f82e2be4756a4651e61f1883d2a99f1d141954097a6e4176a3482a951fc69c` | **LEÍDO ÍNTEGRO** | primera `## Qué se conserva de `G29`, y qué se deroga` (L15) · última `## Lo que este contrato no promete` (L243) | **L84** · *«\| commit \| **la capacidad con custodia** \| ella misma \| — \| `gate` de su capa \| SHA en el checkpoint \|»* | **L246** · *«un commit físico atómico entre varios repositorios. **Git no lo ofrece y ADS no lo finge**»* |

##### 3.3 · Tramos NO abiertos

**Ninguno.** No declaro ningún tramo sin abrir en ninguna de las veinte fuentes. Donde una lectura fue costosa —el documento 11 son 9 280 líneas y el 18 son 3 665— la hice por bloques consecutivos hasta agotar el fichero, y las anclas de arriba proceden de regiones separadas de cada uno precisamente para que eso sea comprobable.

---

#### 4 · El cruce que el encargo exige, dicho antes del veredicto

```text
ASIGNADAS                       20
LEÍDAS ÍNTEGRAMENTE             20
PARCIALMENTE LEÍDAS              0
NO ABIERTAS                      0

ASIGNADAS − LEÍDAS ÍNTEGRAMENTE = ∅        (conjunto vacío)
```

**El conjunto está vacío.** Mi recomendación **NO** es `INSUFICIENTE PARA F5 POR COBERTURA`. La regla de cierre del manifiesto no se dispara sobre mi lote, y el veredicto que doy más abajo se apoya en el fondo, no en la cobertura.

Lo digo aquí, antes del veredicto, como el encargo manda.

---

#### 5 · Juicio de `D105` — el terminal `abandonada` y su `deriva`

**Intenté refutarla punto por punto. Resiste en seis de los ocho extremos, y falla en dos.**

##### 5.1 · Lo que resiste

**(a) Referencia hacia adelante — NO la hay.** `11-ARQ:1868` · *«**NO lleva `deriva_emitida`: ese campo queda PROHIBIDO en esta fase**»*, y `11-ARQ:4216`, la celda de campos PROHIBIDOS del `abandonada` en el contrato de §3.6: *«**`deriva_emitida`, PROHIBIDO desde `D105`**»*. Barrí el corpus: `deriva_emitida` aparece **cinco veces** en `11-ARQ` —L1868, L1883, L1907, L4216, L4303— y **las cinco son la prohibición o la explicación de por qué se prohíbe**. Ninguna aparición obligatoria viva.

**(b) Circularidad indirecta — la busqué y no está.** Mi `H1` predecía que quedaría un campo tipo `sucesor` o `cierre_id`. No queda. `11-ARQ:1914-1915` · *«`id(abandonada) = EV-H(su cuerpo MENOS `id`)`, y su cuerpo **ya no contiene ninguna referencia hacia adelante**»*. La tabla de tres alternativas de `11-ARQ:1893-1896` compara A, B y D antes de elegir, descarta A por la circularidad exacta y elige B con el argumento correcto: *«es la mínima: **no añade ningún evento, ningún tipo y ningún campo al `abandonada`** — sólo mueve una referencia de sitio y le da `fsync`»*. **Esto está bien hecho y hay que decirlo.**

**(c) `fsync` del `deriva` y de su directorio — SÍ.** `11-ARQ:1239` · *«**(5) el evento `deriva` con `causa: abandono-de-transaccion` Y SU DIRECTORIO**, ANTES de retirar el marcador de transacción»*. Y el paso E lo ordena: `11-ARQ:1871-1878`, pasos 1 a 6, con el 4 «`fsync` del fichero del `deriva` **Y DE SU DIRECTORIO**» y el 6 «**sólo ahora, y no antes**, retirar el marcador de transacción». Mi `H4` quedó refutada, y a favor.

**(d) Persistencia del marcador de transacción — SÍ.** `11-ARQ:1153` (`W8`) · *«tras `derivada` se retira sin más; tras `abandonada` se retira **sólo cuando el `deriva` y su marcador son durables**»*. La asimetría está declarada donde se lee, no sólo donde se decide.

**(e) Ventana `W17` — existe, es consecutiva y el recuento se deriva.** `11-ARQ:1163` la declara íntegra, incluida la sub-ventana «o entre el `deriva` y su marcador». `11-ARQ:1128` · *«Se enumeran las **DIECIOCHO**, y el recuento **se deriva de las filas de la tabla, no se escribe**»*. Conté las filas: **dieciocho**. Recorrí `W1`–`W16` una a una: **ninguna reclamaba ya esa caída**. `H3` confirmada.

**(f) Recuperación idempotente, sin eventos duplicados — declarada, y la sede que antes la prohibía está corregida.** `11-ARQ:961` (paso 0 de §2.6.4) · *«· NO existe → **se COMPLETA, y es idempotente** · `W17`»*, contra la formulación anterior que la prohibía. `11-ARQ:1940-1944` cierra el círculo: *«**EL VALIDADOR Y LAS VENTANAS, ALINEADOS** … Antes, la capa B exigía que existiera y el paso 0 prohibía emitirlo: **las dos afirmaciones no podían ser ciertas a la vez**»*.

##### 5.2 · Lo que NO resiste

**(g) Residuo de la semántica anterior — SÍ lo hay.** Es `P-02`.

**(h) La idempotencia depende de una premisa que dos sedes canónicas contradicen.** Es `P-03`, y es lo más grave que traigo.

##### 5.3 · Y la prueba que nadie ejecuta

`D105` crea la decimoctava ventana y **ninguna fila adversarial la alcanza**. Es `P-01`. La tabla de §2.6.7 se autodefine (`11-ARQ:1433`) como *«convertible en pruebas de F6 **sin traducción**»*: si una ventana no tiene fila, F6 no la prueba.

**Veredicto sobre `D105`:** **la decisión es correcta y la mejor construida del lote.** Su ejecución deja tres residuos: uno de redacción (`P-02`), uno de contrato (`P-03`) y uno de cobertura de pruebas (`P-01`). El primero y el tercero son ediciones. El segundo exige elegir entre dos frases que hoy no pueden ser ciertas a la vez.

---

#### 6 · Juicio de `PN-15`

**¿Su prueba posterior falla hoy y sólo pasaría tras F5? SÍ.** Ejecutada mentalmente contra `a.11`:

- La disyunción está retirada. `11-ARQ` §16, `PN-15`, PRUEBA POSTERIOR: *«**La disyunción se retira. La prueba exige UNA sola cosa:** … para cada una de `G20`, `G21`, `G22` y `G23`, **una fila en `a.11`** —o en la enmienda que F5 escriba sobre `a.11`— **que la nombre y diga qué se conserva, se ajusta o se sustituye**»*, y remata: *«**Hoy FALLA, y tiene que fallar**»*.
- Lo comprobé: `grep 'G2[0-3]'` sobre (a) devuelve **exactamente una línea**, `a-CAPACIDADES-APROBADA.md:180`, que es la ficha de `INV` («spikes contra entorno real, freshness (G22+G33)»). **No es fila derogatoria y no está en `a.11`.**
- Leí `a.11` entera (L1016–1024). Sus **cinco** filas —Derogadas, Sustituidas, Ajustadas, PENDIENTES, Previstas— nombran `G11`, `G12`, `K0.9`, `G14`, `G13`, `G34`, `G52`, `G17`, `G08`, `G32`, `G26`, `G24`, `G53`. **Ninguna nombra `G20`, `G21`, `G22` ni `G23`.**

**La prueba es genuina: falla hoy, y sólo una enmienda de F5 sobre `a.11` la haría pasar.** `M-05` queda cerrado.

**¿Siguen vigentes `G20`–`G23` y no derogadas? SÍ, verificado en la fuente.** `kernel/KERNEL.md` L640 (`G20`), L682 (`G21`), L692 (`G22`, con su `#### Timebox` en L694), L748 (`G23`): presentes, íntegras, sin marca de derogación. Y `E2.4` (`a-ENMIENDA-E2-MULTIREPO.md:146`) da la doctrina que lo sostiene: *«`G29` pasa de «sobrevive» a «revisada»»* — lo no nombrado sobrevive, y hubo que **enmendar** (a) para reclasificar una sola regla. `D97` la aplica correctamente.

**¿Contradice algo de `D104`–`D106` a (a), (b), `E1`, `E2`, `KERNEL.md` o los siete contratos?** Los abrí los siete y las cuatro fuentes aprobadas. **No encuentro contradicción material.** `D105` y `D106` operan sobre el protocolo transaccional y sobre el procedimiento del gate, materias que ni (a) ni (b) ni `E1`/`E2` ni `C1`–`C7` gobiernan. `C7:84` mantiene su tabla de propiedad intacta y `git diff` confirma que el rango no la toca. Lo único que roza el límite es `E5-3`, y lo trato como `P-07`.

**Un defecto dentro de `PN-15`, no de su tesis:** su bloque de evidencia se autofalsifica. Es `P-06`.

---

#### 7 · Juicio de `D106`

##### 7.1 · La cronología de `O16` — **fecha, no inventa**

El ADDENDUM (`DECISIONES-Y-CONTRADICCIONES.md` L536–548) hace exactamente tres cosas y declara que no hace ninguna más:

> *«El gate de cobertura derivó del historial que **la fila `| O16 |` entró en el registro el 2026-08-28**, en el commit `a713590`, y que **la procedencia de arriba se añadió el 2026-08-29**, en `d868bcb`, declarando esa misma fecha para la consulta al Owner.»*
>
> *«**Qué NO se hace, y por qué.** No se reescribe `O16` … **no se inventa una cita del 28 que nadie dijo**, y no se retira la fila.»*

**Verifiqué las dos fechas con `git log`, no con el texto:**

```
a713590   2026-08-28 10:35:31 +0200
d868bcb   2026-08-29 18:05:53 +0200
```

Ambas exactas. Y la procedencia original ya separaba con honestidad lo que es cita literal del Owner («ok, confirmamos» — dos palabras) de lo que redactó el sistema. El addendum añade el único dato que faltaba —**desde cuándo** está respaldada— y declara expresamente que entre el 28 y el 29 fue *«una formulación registrada a la espera de confirmación»*. **No inventa ninguna confirmación. `M-07` queda cerrado.**

##### 7.2 · El manifiesto de asignación existía antes del reparto — **SÍ, verificado con `git log`**

```
18cbfb5   2026-08-29 22:15:07 +0200   docs(gate): publicar manifiesto previo de asignación de F4c
git diff --stat 7764cca..18cbfb5  →  1 file changed, 140 insertions(+)
```

Es el **último** commit de la rama y **lo único** que añade sobre el candidato. Fue publicado antes de que se me contactara, y su contenido es inmutable desde entonces. Su cabecera lo declara: *«Este documento se escribe y se commitea **antes de crear o contactar a ningún revisor**»*. **Cumplido, y comprobable.**

##### 7.3 · ¿Es `C-L.5` certificable por primera vez?

**En su cláusula más dura, SÍ — y es un avance real.** La regla que `O` declaró NO CERTIFICABLE (`O-04`) era *«cualquier fuente ASIGNADA pero NO LEÍDA impide la suficiencia»*, incomprobable porque nadie declaraba qué se le había asignado. Con el manifiesto de asignación publicado y este manifiesto de lectura, **`asignado − leído` es calculable**: para mí da `∅`. `O-04` queda cerrado por lo que `O-04` dice.

**Pero `C-L.5` no queda cerrada, y el motivo es `P-08`:** `D106` hizo calculable `asignado − leído` y dejó **sin ninguna restricción** `obligatorio − asignado`. El universo de 43 fuentes está **elegido, no derivado**, y el «FUENTES SIN ASIGNAR 0» que el manifiesto publica es cierto por construcción dentro de un universo que él mismo define.

---

#### 8 · Adjudicación de los hallazgos del documento 20 que caen en mi lote

Mi lote se deriva del `Foco` que el manifiesto declara para `P` (L23–25): *material normativo y protocolo transaccional · `D105` · `abandonada` · `deriva` · identidades · `fsync` · `W17` · recuperación · marcador · commit · `PN-15` · compatibilidad normativa*. Son **trece** de los veintiuno. **Un solo estado cada uno.**

| hallazgo | estado | motivo, con su prueba |
|---|---|---|
| `M-02` · GRAVE · circularidad `abandonada`/`deriva` | **SUPERADO** | `D105` invierte la referencia. `deriva_emitida` PROHIBIDO en `11-ARQ:1868` y `:4216`; `abandonada_id` obligatorio en el `deriva` (`:4218`); los dos `id` construibles por `:1914-1920`. Barrido: cinco apariciones de `deriva_emitida`, las cinco prohibitorias o explicativas. **El defecto que `M-02` denuncia ya no existe.** Los residuos que quedan son míos (`P-02`, `P-03`) y son defectos distintos |
| `M-03` · GRAVE · `fsync` del `deriva`, arranque, exhaustividad de la tabla | **SUPERADO** | Sus tres patas cerradas: `fsync` del fichero **y del directorio** (`:1239`, `:1874`); el arranque **completa** en vez de prohibir (`:961`); la justificación de exhaustividad reescrita y el recuento derivado a **DIECIOCHO** (`:1128`), que conté yo sobre las filas. Residuo aparte: `P-01` |
| `M-05` · MEDIO · la prueba posterior de `PN-15` pasaría en verde hoy | **SUPERADO** | `D106` retira la disyunción. Ejecutada por mí: `grep 'G2[0-3]'` sobre (a) = una línea, la ficha de `INV`; `a.11` no las nombra en ninguna de sus cinco filas. **Falla hoy, como debe** |
| `M-07` · MEDIO · la cronología de `O16` | **SUPERADO** | El addendum reconcilia las dos fechas sin reescribir `O16` ni inventar cita. Las dos fechas verificadas por mí con `git log` sobre `a713590` y `d868bcb`: exactas |
| `M-08` · MENOR · cita incorrecta a `a.6` L504–505 | **SUPERADO** | Conté sobre el fichero: la frase *«DOM y SEG aportan condiciones antes de construir y revisan después»* está en **L502–503**. `11-ARQ:8776` cita ahora `L502–503` y **declara la corrección en línea**; `:8802` la repite bien. No queda ninguna cita a L504–505 |
| `M-09` · MENOR · grafía `revisión`/`revision` | **REGISTRADO PARA F5** | Verificado: `grep -rn ':revisi'` sobre (b) = **una línea, L836, con tilde**; `11-ARQ` usa `revision` sin tilde **17** veces. Registrado como `E5-3` con sede, texto vigente, corrección exacta y prueba posterior, y **F4 no elige**, que es correcto. Objeción sobre el **registro elegido**: `P-07` |
| `M-10` · MENOR · `X58` desordenada | **SUPERADO** | Derivé el orden completo de la tabla de §2.6.7: `… X55 X56 X57 **X58** X59 X60 X61 X62`. Correcto. Y conté **46 filas**, que coincide con la cifra publicada |
| `N-03` · MENOR · `E1.4` declara siete marcas y hay seis | **REGISTRADO PARA F5** | Lo conté yo sobre (a): marcas `[E1` en **L26, L89, L219, L226, L261, L285** = **SEIS**; `E1` L196–197 declara **siete**; y los recuentos de **L269** y **L276** van sin marca. Registrado como `E5-4` con corrección y prueba. Misma objeción de sede que `M-09`: `P-07` |
| `N-04` · MENOR · el documento 17 publica 22 y 21 perfiles de `C2` | **SUPERADO** | Derivé sobre el fichero: `grep -c '^id: perfil:' C2` = **21**. `11-ARQ:9076-9089` reancla la cifra vigente («**Son 21**»), declara que el documento 17 es **histórico e inmutable y no se corrige**, y nombra la causa mecánica (`RECUENTOS-generado.md` no censa los perfiles). Disposición completa y correcta |
| `N-05` · MENOR · el calificativo del principio de `U` difiere entre las dos sedes del Owner | **SUPERADO** | Verifiqué las dos: `ADS-PENDIENTES` **L914** dice «**Principio aceptado:**» con la frase literal «Detectar automáticamente; actualizar conscientemente», e `IDEAS` L79 dice «Principio provisional». `11-ARQ:6682-6692` registra la segunda sede y razona bien: los dos son material de trabajo del Owner, **ninguno es normativo** —`ADS-PENDIENTES` L3–L6 se autodeclara «no es todavía especificación normativa»—, luego el adjetivo no decide el estatus |
| `O-03` · MEDIO · la laguna deja el diario permanentemente inválido | **SUPERADO** | `W17` da la ventana, el paso 0 da la reparación, el `fsync` da la durabilidad y `11-ARQ:1940-1944` declara alineados el validador y las ventanas. **La ruta de reparación existe.** Reserva material, y es mía: `P-03` reabre el mismo modo de fallo por otra vía |
| `O-04` · MENOR · `C-L.5` contiene una condición que su adjudicador no puede verificar | **SUPERADO** | El manifiesto de asignación existe, es previo al reparto (`18cbfb5`, verificado con `git log`), publica ruta · líneas · SHA-256 · asignatario de las 43 fuentes, y este dictamen aporta el manifiesto de lectura. **La resta es calculable por primera vez**, que es exactamente lo que `O-04` pedía |
| `N-04`↔`M-06` — nota | *(véase abajo)* | `M-06` cae en el foco de `Q` («excepción exacta de seis ficheros»), no en el mío |

**Fuera de mi lote — no los adjudico, y digo por qué.** `M-01`, `M-04`, `M-06`, `M-11`, `M-12`, `N-01`, `N-02`, `O-01`, `O-02` pertenecen al foco declarado de `Q`: derivación de `<CAP>:revision`, las cuatro vías tipadas, `AUD`/`DIR`, el ancla de posición, la batería `G-15`/`G-16`, y la excepción exacta del kernel. **No los toco, no los presumo cerrados y no los presumo abiertos.** No he leído `01-PROCESOS.md`, `esquemas/proceso.yaml`, las quince fichas ni la batería, y no voy a sustituir una lectura ausente por una inferencia.

**Recuento de mi lote:** 13 hallazgos · **10 SUPERADOS** · **2 REGISTRADOS PARA F5** · **1 SUPERADO con reserva material declarada** (`O-03`) · 0 FALLIDOS · 0 CONTRATADOS PARA F6 · 0 NO APLICABLES · 0 ABIERTOS.

---

#### 9 · HALLAZGOS

Ocho. Severidad puesta por mí con un criterio que declaro: **GRAVE = F6 construiría algo distinto de lo que el contrato quiere, o una garantía publicada no se sostiene; MEDIO = una afirmación vigente es falsa sin cambiar el comportamiento; MENOR = editorial.**

---

##### `P-01` · **GRAVE** · La única fila adversarial que barre todas las ventanas barre diecisiete de dieciocho, y la que se salta es la que `D105` creó

**Fichero y línea:** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L1479**

> *«\| `X54` \| matar la máquina en cada una de las **diecisiete ventanas** con un `conflicto` vivo \| el `conflicto` sobrevive o se reconstruye desde el diario, **ningún canónico se toca**, y la transacción sigue teniendo sus DOS salidas disponibles tras el arranque \|»*

**Contra**, en el mismo documento:

> `11-ARQ:1128` · *«Se enumeran las **DIECIOCHO**, y el recuento **se deriva de las filas de la tabla, no se escribe**»* — y conté las filas: dieciocho.

**Por qué importa.** La tabla de §2.6.7 se autodefine en **L1433** como *«**Convertible en pruebas de F6 sin traducción.** Cada fila declara qué se prepara, dónde se interrumpe, qué debe observarse y qué diagnóstico exacto debe emitirse»*. `X54` es **la única** fila que barre el conjunto de ventanas. Recorrí las 46 filas: **ninguna otra alcanza `W17`**. `X55` prueba el abandono en su camino feliz y su resultado exigido es «el marcador **se retira**» —correcto sólo *después* de que el `deriva` y su marcador sean durables, que es justo lo que `W17` interrumpe—, y no corta la corriente en ese punto.

Resultado: **la ventana que `D105` añade para cerrar `M-03` y `O-03` no tiene prueba**, y toda la disposición de esos dos hallazgos descansa en que sea alcanzable e idempotente.

**Y es la tercera vez que ocurre por la misma causa.** El propio documento lo registra dos veces: `11-ARQ:1269` · *«**Ninguna de las diecisiete filas de §2.6.7 lo detectaba**… Es `D36`»*, y `11-ARQ:1436` · *«ninguna de las **diecisiete originales** detectaba una caída de máquina»*. Se añade una ventana, no se actualiza la fila que las barre.

*(Aclaro que `L1269` y `L1436` son usos **correctos**: hablan de las diecisiete de entonces. El defecto es sólo `L1479`, que es normativa vigente.)*

**¿Bloquea F5?** **SÍ**, y es la corrección más barata del lote: una palabra.

---

##### `P-02` · **MEDIO** · La capa B conserva el verbo de la semántica que `D105` invirtió, en la lista que `D89` acababa de barrer

**Fichero y línea:** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L4360**

> *«· TODO `abandonada` **DECLARA SU** `deriva`, y ese `deriva` existe en el diario y nombra las mismas rutas e items»*

**Contra**, cuarenta y seis líneas más abajo, en la misma sección, **L4406**, regla 3:

> *«la correspondencia se comprueba **recorriendo el diario en busca del `deriva` que apunta**, no siguiendo un puntero desde el `abandonada`. **Invertido por `D105`**: el sentido anterior exigía al `abandonada` un campo cuyo valor no podía existir cuando se calculaba su propio `id`»*

Y contra **L4303**, la capa A del mismo §3.6: *«**y NO `deriva_emitida`, que `D105` prohíbe en esta fase**»*.

**Por qué importa.** «DECLARAR SU» es exactamente el verbo de lo que se retiró: bajo `D105` el `abandonada` **no declara** nada — el `deriva` lo nombra a él. Un autor de validador que lea la lista de viñetas y no baje hasta la tabla de reasignación implementa el puntero al revés, y ése es el defecto `M-02` reaparecido. Agrava que esta lista **acababa de ser barrida** por `D89` para retirar de ella las dos reglas que causaron `A2` —la corrección está a la vista en **L4342-4348**, «*Corregido por el gate de cierre (`I-03`; es `D89`)*»— y que la propia lista declara en **L4335** que *«ninguna regla de esta lista vuelve a escribir la condición con otras palabras»*.

**Lo que atenúa, y lo digo.** La **sustancia** de la viñeta —que existe exactamente un `deriva` por `abandonada`— es **verdadera** bajo `D105`, y `W17` la hace alcanzable. Por eso no lo gradúo GRAVE: falla el verbo, no el hecho.

**¿Bloquea F5?** No por sí solo. Es una edición de tres palabras.

---

##### `P-03` · **GRAVE** · La idempotencia de `W17` descansa en una regla de `predecesor` que sólo una sede escribe y que las dos sedes canónicas del campo contradicen

**La garantía.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L1163** (`W17`) y **L1935-1938**:

> *«el cuerpo del `deriva` es una función del `abandonada` durable …, luego **dos arranques emiten el MISMO evento direccionado por contenido** y emitirlo dos veces no crea dos»*

**La premisa que la sostiene, escrita en UNA sola sede** — `11-ARQ:1918-1920`, punto 4 del paso E:

> *«`id(deriva) = EV-H(su cuerpo MENOS `id`)`, con **`predecesor` = `id(abandonada)`** y `abandonada_id` = `id(abandonada)`, los dos calculables porque ese evento existe»*

**Las dos sedes que la contradicen:**

> **§2.8, `11-ARQ:2927-2934`** — el contrato de identidad, corregido por esta misma fase:
> *«**`predecesor` VA INCLUIDO** — es parte de la historia … Y POR TANTO, DICHO SIN RODEOS: **REEMITIR NO ES IDEMPOTENTE POR `id`.** Tras una caída, el diario ha crecido y el `predecesor` es otro, luego el id es otro. F4c afirmaba que «emitir dos veces el MISMO evento produce el MISMO fichero» … **Eso sólo es cierto bajo un `predecesor` idéntico**, condición que **la recuperación no garantiza**. La frase se RETIRA.»*
>
> **§3.6, `11-ARQ:3774`** — el contrato del campo, que es la sede que `D72` designa para derivar el esquema de `evento`:
> *«`predecesor`    el evento que **este emisor observó como último**. Forma la cadena verificable»*

**Y la fila del `deriva` en el contrato de §3.6, `11-ARQ:4218`, no lleva la excepción.** Declara `causa`, `afecta[]`, `items[]`, `autoridad`, `tx_afectada` y `abandonada_id` con todo detalle, y **no dice nada de `predecesor`**. Barrí `abandonada_id` en todo el documento: siete apariciones, y **ninguna fuera de §2.6.9 fija `predecesor`**.

**Por qué importa, materialmente.** Si `predecesor` es «el último observado» —que es lo que dice la sede de la que F6 deriva el esquema— entonces dos arranques separados por cualquier otra escritura del diario producen **dos `id` distintos**, luego **dos eventos `deriva`** para el mismo `abandonada`. Y entonces se dispara la regla 3 de la capa B (`11-ARQ:4406`): *«ninguna `abandonada` sin **EXACTAMENTE UN** `deriva` que la referencie por `abandonada_id`»*. Resultado: **el diario queda no conforme por su propio validador** — que es palabra por palabra la consecuencia que `O-03` denunció y que `D105` declara haber eliminado (`11-ARQ:1163`: *«El resultado era un bloqueo perdido en silencio y **un diario permanentemente inválido sin ruta de reparación**»*).

No afirmo que `D105` esté equivocada: §2.6.9 punto 4 la resuelve, y la resuelve bien. Afirmo que **la resolución vive en una sola sede, que §2.8 la niega en términos generales y que §3.6 no la recoge**, y que la sede que F6 lee para construir el esquema es §3.6. **F6 no puede materializar el `evento` sin decidir cuál de las tres frases manda.**

**¿Bloquea F5?** **SÍ.** No exige rediseñar nada: exige llevar a §3.6 —fila del `deriva` y definición del campo— y a §2.8 la excepción que §2.6.9 ya escribió. Pero mientras no esté, la garantía central de `D105` no es derivable de su propio contrato.

---

##### `P-04` · **MEDIO** · El checkpoint cuenta las nueve ventanas retiradas en la misma sede en que declara `M-8` corregido por retirarlas

**Fichero y líneas:** `docs/evolucion/CHECKPOINT-ADS-NEXT.md` **L1141-1144**

> *«· NADA PROBADO: las **46** filas de la tabla adversarial de §2.6.7 …, **las 9 ventanas RC-1–RC-9 de §2.6.9**, los 11 escenarios negativos de §11.5 y los 12 escenarios de §14 están ESCRITOS»*

**Contra `11-ARQ:8670-8674`**, la sede equivalente del objeto:

> *«los doce escenarios de §14, las **CUARENTA Y SEIS** filas …, los **ONCE** escenarios negativos de §11.5 y las **OCHO** comprobaciones `X-A`–`X-H` de §2.9. **Las nueve ventanas de reconciliación NO se cuentan: `D64` las retiró** … **contarlas era inflar el inventario con algo inexistente**»*

**Y contra el propio fichero, `CHECKPOINT` L1641:**

> *«\| `M-8` \| MEDIO \| **`CORREGIDO_EN_F4`** \| D83 \| … \| **`RC-1`–`RC-9` renombradas y retiradas del inventario de §19** \|»*

**Por qué importa.** El checkpoint es el fichero que lee un agente sin contexto. Hace exactamente lo que el documento 11 califica de «inflar el inventario con algo inexistente», **y omite las ocho comprobaciones `X-A`–`X-H` que sí existen**, quinientas líneas por encima de la fila donde declara ese mismo defecto cerrado. Es el modo de fallo que `I-15`, `I-16` y `I-24` describieron una tanda antes: la corrección se aplica en el derivado y no en la sede que la declara cerrada.

**¿Bloquea F5?** No por sí solo. Dos ediciones.

---

##### `P-05` · **GRAVE** · El punto de entrada operativo del checkpoint lleva dos tandas de retraso, sin marca de histórico, y su cifra hacia el Owner es errónea por segunda vez consecutiva

**Fichero y sección:** `docs/evolucion/CHECKPOINT-ADS-NEXT.md` · `## Siguiente acción exacta`, **L1978** al final del fichero.

La cabecera del mismo fichero, **L6**, la designa como el punto de entrada: *«**Basta decir «Continúa»**: la siguiente acción exacta está al final.»* A diferencia de las demás secciones —`## TANDA INTEGRADA … — cerrada, sin publicar` (L1799), `## GATE DE CIERRE INDEPENDIENTE — emitido, y NO superado` (L1755)—, **esta no lleva marca de histórica**.

Su contenido está congelado en la décima tanda:

> **L1980-1982** · *«0  UN GATE INDEPENDIENTE SOBRE ESTA DÉCIMA TANDA — **NO lo encarga esta tanda, y no está encargado**»* — cuando ese gate se encargó, se emitió (documentos 19 y 20) y produjo `D96`–`D106`.
>
> **L2007** · *«1  QUÉ HA CORREGIDO ESTA TANDA … los **28 hallazgos `I-01`–`I-28`**»* — el corpus vigente va por `D106` y por `M`/`N`/`O`.
>
> **L2031-2033** · *«5  QUÉ LLEVAR AL OWNER — las **DOCE** presiones de §16, con `PN-1` bloqueando todo el estado durable y **`PN-14` como la única que esta tanda añade**»*

**La cifra es falsa, y la derivé yo:** `grep -c '^## \`PN-'` sobre el documento 11 da **15** cabeceras; `PN-4` está RETIRADA (L7957) y `PN-5` FUSIONADA (L7985); **15 − 2 = TRECE**. El propio checkpoint lo dice bien dos veces —**L979** «Las **TRECE** presiones normativas vigentes» y **L1233** «**TRECE** presiones normativas vigentes»— y el documento 11 lo confirma en L8486. Y `PN-14` **no** es la última: `PN-15` existe y es la que `D97` añade.

**Y es la segunda vez seguida sobre esta línea exacta.** Dos renglones más abajo, **L2039**, el propio texto lo confiesa: *«**Corregido por `I-28`**: este punto decía «las **ONCE** presiones de §16» y un Owner que siguiera sólo esta línea no habría visto `F-08`»*. Se corrigió de once a doce y volvió a quedarse corta.

**Por qué importa.** Un agente que reanude por donde el fichero le dice que reanude cree que el gate no está encargado, que la última corrección es la décima tanda y que el Owner debe recibir doce presiones. Y es literalmente lo que la instrucción 3 del propio checkpoint manda comprobar: *«que ninguna afirmación vieja sobrevive sin marca de histórica»* — la misma regla con la que `I-05` se graduó GRAVE.

**¿Bloquea F5?** **SÍ.** El registro de entrada de F5 dirige mal al Owner y al agente que reanuda. La corrección es reanclar la sección o marcarla histórica.

---

##### `P-06` · **MEDIO** · El bloque de evidencia de `PN-15` se autofalsifica: su barrido declara ceros que el propio texto que lo contiene destruyó

**Fichero y líneas:** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L8357-8360**

> *«Un barrido del documento 11 devuelve **cero** apariciones de «timebox», «presupuesto máximo», «Owner Decision» y «entregables obligatorios»; y **`G20`, `G21` y `G23` tienen cero apariciones en el documento 11**, en (a), en (b) y en `E2`, mientras **`G22` tiene UNA**, como cita de apoyo.»*

**Lo barrí yo, sobre el mismo fichero:**

```
timebox   en 11-ARQ  →  8   (L8348 L8352 L8357 L8368 L8383 L8407 L8517 L8518)
G20       en 11-ARQ  →  13        G21  →  11
G22       en 11-ARQ  →  17        G23  →  14
```

**Lo que sí es cierto, y lo digo:** en (b) y en `E2` el recuento **es cero** (verificado: `grep -c` devuelve 0 en ambos), y en (a) hay **exactamente una** —L180, la ficha de `INV`— que es lo que la frase describe. La mitad de la afirmación se sostiene.

**Por qué importa.** Las ocho apariciones de «timebox» y las 55 de `G20`–`G23` en el documento 11 **las introdujo el propio bloque de `PN-15` y la fila de §17 que `D97` escribió en el mismo commit**. Es decir: la evidencia de la presión se destruyó al registrarla, y no se reancló. Un lector que rehaga el barrido —que es lo que la frase invita a hacer— obtiene cifras que la desmienten y no puede saber si la presión sigue viva. Cae de lleno en la disciplina que el propio expediente fijó para `I-15`: *«no es editorial: es un recuento, y el encargo excluye del perdón editorial lo que afecta a recuentos»*. Y §16 es el documento que va al Owner.

**Lo que atenúa.** La **tesis** de `PN-15` es correcta y su prueba posterior es genuina (§6). Lo que falla es una frase de evidencia, y su remedio es acotar el barrido a las fuentes donde sigue valiendo.

**¿Bloquea F5?** No por sí solo.

---

##### `P-07` · **MEDIO** · El bloque `E5` justifica no crear una presión con un argumento que su propia fila `E5-3` contradice

**Fichero y líneas:** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L8750-8753** y **L8766-8771**

> *«**No son cambio arquitectónico y no se registran como presión normativa**, precisamente porque el contenido no cambia — crear una `PN` para esto sería inflar el censo que F5 lleva al Owner.»*
>
> *«**Y no se crea una `PN`**: una presión normativa registra que el diseño presiona una NORMA, y **aquí no hay norma presionada** — `P7` y `P9` siguen significando lo que siempre significaron, y las cinco reglas de recomposición siguen diciendo lo mismo en cualquier orden. Lo que hay es **una cita mal puesta y una lista mal numerada**.»*

**El argumento es impecable para `E5-1` y `E5-2`.** No lo es para `E5-3`, y lo dice su propia fila (**L8759**):

> *«corrección exacta: **declarar cuál es la grafía CANÓNICA** … Si la canónica es la de (b), F6 corrige el derivado; **si es la sin tilde, F5 enmienda (b)**. … **Hermano exacto de `F-01`/`PN-14`, que SÍ se registró como presión** sobre la misma clase de discrepancia entre fuente aprobada y derivado.»*

**Por qué importa.** `F-01` fue **reclasificado** de EXTERNO a `PN-14` una tanda antes, y `11-ARQ:8263-8270` da el motivo: *«`F-01` estaba clasificado como EXTERNO de F6 … **La sede estaba incompleta**: la misma cadena aparece en material **APROBADO** que §17 declara intocable por F4 **y por F6**»*. `E5-3` tiene la forma idéntica: la discrepancia vive en (b) L836, material APROBADO, y una de sus dos ramas de remedio **enmienda material aprobado**. La justificación de bloque, escrita sobre una cita mal puesta y una numeración desordenada, se extiende sin más a una fila de otra clase.

**Consecuencia concreta:** el punto 5 del checkpoint dice «QUÉ LLEVAR AL OWNER: las presiones de §16». `E5-3` no está en §16. El único de los cuatro que puede exigir enmendar el material aprobado del Owner es el que no llega al Owner.

**Lo que atenúa, y lo digo:** `E5` **no es** un limbo. Se declara *«checklist verificable de F5, que es la fase con autoridad para editar material aprobado»* y las cuatro filas llevan sede, texto vigente, corrección exacta y prueba posterior. F5 lo verá. Es un defecto de clasificación y de destinatario, no de registro.

**¿Bloquea F5?** No.

---

##### `P-08` · **GRAVE** · `D106` hace calculable `asignado − leído` y deja `obligatorio − asignado` sin ninguna restricción; el manifiesto emitido declara «sin asignar 0» sobre un universo que omite la fuente que el gate anterior marcó «nadie la abrió»

**Fichero y líneas:** `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md` **L128-137**

> *«FUENTES OBLIGATORIAS **43** … **FUENTES SIN ASIGNAR 0** … LÍNEAS OBLIGATORIAS 31 888»*

**Contra el inventario que el gate inmediatamente anterior publicó de su propio corpus obligatorio**, `docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md` **L77-88**:

> ```
> LOTE DE M                          LOTE DE N
>   11-ARQUITECTURA-INTEGRADA 9058     01-PROCESOS.md              564
>   19-GATE-DEFINITIVO        1152     LAS QUINCE FICHAS          1829
>   CHECKPOINT-ADS-NEXT       1898     15-TERCERA-REVISION         651  ← nadie la abrió
>   DECISIONES-Y-CONTRADICC.   677     diseno/00 01 02 04 05      1095
> ```

**Derivé la diferencia yo, con `grep` sobre el manifiesto.** Fuentes que el gate anterior tenía por obligatorias y que este manifiesto **no asigna a nadie**:

```
docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md      651
docs/evolucion/19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md      1152
kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md          141
kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md              352
kernel/operativo/diseno/02-RUBRICAS.md                       343
kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md               130
kernel/operativo/diseno/05-FIDELIDAD.md                      129
                                                            ────
                                                            2898 líneas · SIETE fuentes
```

*(Y `diseno/03-ESCALA-DE-NOVEDAD.md`, 264 líneas, que `PN-14` invoca como sede resolutoria en su L251–261 y de la que cuelga la refutación de `F-01`, tampoco está.)*

**Por qué importa, y por qué es GRAVE.**

1. **`15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` está nombrada la primera en la condición de nivel 0 vigente.** `18-GATE…:3566`, `C-0.1`: *«**CUBRIR LAS CATORCE FUENTES OBLIGATORIAS QUE NADIE ABRIÓ**, empezando por `15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` (652 líneas), que está asignada a los DOS revisores y no la leyó ninguno, y siguiendo por las **DIEZ** de las diecinueve que el primer gate ya había omitido una vez: `diseno/00`, `01`, `02`, `04`, `05`, `C2`, `C3`, `entrada/00`, `02`, `04`»*. El checkpoint la repite en su punto 0 operativo, **L1987**. Ninguna de las dos está derogada. **De las diez, el manifiesto asigna cinco** (`C2`, `C3`, `entrada/00`, `02`, `04`) **y omite las cinco de `diseno/`.** Y omite la que la condición pone en primer lugar.

2. **Es la fuente de la que cuelga `D64`.** El propio adjudicador `I` lo escribió (`18-GATE…:2593-2597`): *«Es la TERCERA REVISIÓN INDEPENDIENTE: la fuente donde vive la causa original de `D64`–`D68`, que es la decisión de la que cuelgan `A1`, `A2`, `A6`, `A8`, `A9` y las nueve ventanas de `M-8`»*. `D64` es exactamente la decisión sobre la que se apoyan `P-04` y la mitad de las correcciones de la capa B que juzgo arriba. **Juzgo `D64` por su propia descripción, otra vez.**

3. **El documento 19 tampoco está**, y es donde viven `C-L.1`–`C-L.13` y `K-01`–`K-11`, de los que salen `PN-15`/`D97` y la propia `C-L.5` que este manifiesto existe para satisfacer.

4. **`D106` no exige que el universo se derive.** Su texto (`11-ARQ:9239-9245`) pide del manifiesto de asignación *«Por cada fuente: ruta · líneas · SHA-256 · a qué revisor se asigna. Y el total, derivado: fuentes obligatorias, asignadas y sin asignar»*. **Deriva los totales sobre un conjunto que él mismo elige.** «Sin asignar 0» es entonces verdadero por construcción y no dice nada: es la misma clase de afirmación que `C-L.5` denuncia dos párrafos antes — *«cobertura asignada del 100 % NO es cobertura leída, y `sin_cubrir.txt` vacío sólo dice que todo fichero tenía un lector»*. Un escalón más arriba, el manifiesto reproduce esa forma.

**Lo que consta a favor, y no lo escondo.** El manifiesto **sí** cumple la lista explícita de «QUÉ HAY QUE LEER ÍNTEGRO» de `C-L.5` —`ADS-PENDIENTES`, 16, 17 y 18, los cuatro, y los cuatro los he leído íntegros—; **sí** es previo al reparto e inmutable; **sí** publica ruta, líneas y SHA-256 derivados del árbol; **sí** resuelve por escrito, en vez de en silencio, las dos rutas de contratos que el encargo nombraba mal (§3 del manifiesto); y **sí** hace calculable por primera vez la resta que `O` no pudo calcular. Es un avance real y `O-04` queda cerrado por lo que `O-04` dice.

**¿Bloquea F5?** **SÍ.** No porque falte cobertura en mi lote —no falta—, sino porque `C-L.5` es una de las condiciones de cierre de `F4c` y **no queda cerrada**: su regla dura es ahora comprobable, y su universo sigue sin serlo. Y la fuente que dos gates consecutivos han marcado como no abierta sigue sin abrirse por tercera vez.

---

##### Recuento de mis hallazgos

```text
TOTAL                    8
  BLOQUEANTES            0
  GRAVES                 4    P-01 · P-03 · P-05 · P-08
  MEDIOS                 4    P-02 · P-04 · P-06 · P-07
  MENORES                0

DE ELLOS, INTRODUCIDOS O PERPETUADOS POR ESTA MISMA TANDA
                         5    P-01 (D105 añade la ventana y no la fila que la barre)
                              P-02 (D89 barre la lista y deja la viñeta)
                              P-03 (D105 fija predecesor en una sede y no en la canónica)
                              P-06 (D97 destruye su propia evidencia al registrarla)
                              P-08 (D106 define la regla y no el universo)

QUE BLOQUEAN F5          4    P-01 · P-03 · P-05 · P-08
```

---

#### 10 · Refutaciones intentadas y su resultado

El encargo pide intentar **refutar**, no confirmar. Estas son las que intenté y **perdí**, escritas porque perderlas es el dato.

| lo que intenté sostener | por qué parecía defecto | qué lo refutó | resultado |
|---|---|---|---|
| El cuerpo del `deriva` dependerá de algo no determinista (reloj, uuid, orden de escaneo), y por eso «el mismo evento» no lo será | era mi hipótesis `H2`, y es el modo de fallo clásico de una recuperación idempotente | `11-ARQ:1163` y `:1935` construyen el cuerpo como **función del `abandonada` durable** —`estado_observado[]`, `autoridad`, `motivo`, `revision_base`—, todos ellos ya escritos. **No hay reloj, no hay uuid, no hay orden de escaneo** | **NO REPRODUCIDO.** El defecto real está en `predecesor`, que es otra cosa: `P-03` |
| Se declara el `fsync` del fichero del `deriva` y se olvida el del **directorio** | es la laguna más frecuente y era mi `H4` | `11-ARQ:1239` · «**Y SU DIRECTORIO**» · y `11-ARQ:1874` · «**`fsync` del fichero del `deriva` Y DE SU DIRECTORIO** — obligatorio desde `D105`» | **NO REPRODUCIDO.** Está bien hecho |
| `W17` deja sin cubrir la sub-ventana «entre el `deriva` y su marcador»: el `deriva` es durable, el marcador no, y nadie lo reconstruye | la columna de observación de `W17` describe el estado como «`abandonada` **sin ningún `deriva`**», que no es el estado de esa sub-caída | La sub-ventana **está nombrada** en la propia condición de `W17` («—o entre el `deriva` y su marcador—»), y §2.9 declara `estado/deriva/<ID>.abierta` **reconstruible desde el diario** por `bloqueado_por_deriva(item)`. Cubierta en la práctica | **NO REPRODUCIDO como laguna.** Queda una inconsistencia de redacción en la columna de observación, demasiado menor para numerarla |
| `PN-15` está mal registrada porque `G22` sí aparece en el corpus, luego el «cero» general es falso | vi apariciones de `G22` por todas partes | El «cero» de `PN-15` está **acotado**: «en el documento 11, en (a), en (b) y en `E2`». En (b) y `E2` es **cero** verificado, y en (a) es **una**, exactamente como dice | **PARCIALMENTE REPRODUCIDO.** La mitad acotada a (a), (b) y `E2` **es correcta**. Lo falso es sólo la mitad sobre el documento 11: es `P-06`, y lo gradúo MEDIO en vez de GRAVE por esto |
| `M-05` sigue vivo: la prueba de `PN-15` pasaría en verde hoy porque `D97` escribió la fila de §17 que la satisfacía | era el hallazgo original, y la corrección podía ser cosmética | La disyunción **se retiró**; el disyunto de §17 ya no cuenta. Ejecuté el disyunto superviviente contra (a): una línea, la ficha de `INV`, no derogatoria, fuera de `a.11` | **NO REPRODUCIDO.** `M-05` está genuinamente cerrado |
| El addendum de `O16` retro-fecha una confirmación que el Owner no dio el 28 | era la sospecha obvia sobre cualquier cronología añadida a posteriori | El addendum **dice lo contrario de lo que sospechaba**: declara expresamente que el 28 la formulación estaba «a la espera de confirmación» y que no se inventa cita del 28. Las dos fechas las verifiqué en `git log`, no en el texto | **NO REPRODUCIDO.** Es de lo mejor del expediente: una corrección que empeora su propia posición para ser exacta |
| La viñeta `L4360` de la capa B es sólo un sinónimo inocuo de la regla 3 | había que darle la vuelta antes de numerarla | La **sustancia** sí coincide; el **verbo** no, y `W17` (`L1163`) identifica esa exigencia de la capa B como parte del defecto que se corrigió | **REPRODUCIDO A LA BAJA.** Por eso `P-02` es MEDIO y no GRAVE |
| El manifiesto de asignación no sirve porque `HEAD` no es el candidato | riesgo procedimental que detecté **antes** de leer nada | `git diff --stat 7764cca..18cbfb5` = 1 fichero, 140 inserciones, el propio manifiesto. Y los 20 SHA-256 coinciden | **NO REPRODUCIDO.** Queda como observación declarada, no como defecto |

---

#### 11 · Proporcionalidad

**Un dictamen que sólo enumera defectos no mide nada.** Esto es lo que en mi materia está bien, verificado por mí y no aceptado de palabra:

- **`D105` es la mejor decisión del lote.** Compara **tres alternativas en tabla** antes de elegir (`11-ARQ:1893-1896`), descarta la que era el defecto con el argumento exacto, y elige la mínima: no añade ningún evento, ningún tipo y ningún campo. Eso es más difícil que retirar una frase.
- **Los dos `fsync` y el orden de seis pasos están completos**, con el directorio incluido y con el marcador retirado en el paso 6 y no antes. Busqué la laguna típica y no está.
- **El recuento de ventanas se deriva de las filas y no se escribe**, y lo comprobé contando: dieciocho. Lo mismo con las 46 filas adversariales y con las trece presiones vigentes. **Tres cifras que el encargo me pidió desconfiar, y las tres resisten.**
- **`PN-15` es una presión bien construida:** fuente exacta, texto vigente citado por línea, contradicción demostrada, cuatro preguntas para el Owner, condición de reversión escrita y `PROPIETARIO: el Owner`. Y no toma la decisión: `11-ARQ:8394` dice por qué —`a.11` es material aprobado y `G21` reserva esa decisión a la constitución—. **F4 se abstiene donde debe abstenerse.**
- **`G20`–`G23` siguen íntegras en `KERNEL.md` y `a.11` no las toca.** Nadie derogó nada de tapadillo. Lo verifiqué en la fuente, no en el registro.
- **El addendum de `O16` es un ejemplo de disciplina:** separa la cita literal de dos palabras del párrafo que redactó el sistema, dice qué alcanza la confirmación y qué no, y declara que no autoriza iniciar F5.
- **El manifiesto de asignación es el primer instrumento del expediente que hace comprobable una regla de cobertura**, y resuelve por escrito —en vez de en silencio— dos rutas que el encargo nombraba mal. `O-04` era real y está cerrado.
- **`C7` está intacto** (`git diff` sobre el rango no lo toca) y `C7:246` sigue diciendo lo que debe decir: *«un commit físico atómico entre varios repositorios. **Git no lo ofrece y ADS no lo finge**»*.
- **Diez de los trece hallazgos de mi lote están genuinamente superados**, y ninguno de mis ocho hallazgos exige una decisión de arquitectura nueva. Los ocho tienen remedio determinado y siete caben en menos de media página.

**Y lo digo con la severidad que corresponde:** de mis cuatro GRAVES, tres (`P-01`, `P-03`, `P-05`) son ediciones que caben en un párrafo cada una. El cuarto (`P-08`) exige emitir un manifiesto adicional, no rediseñar nada.

---

#### 12 · Límites de mi revisión, sin adorno

```text
1  NO HE LEÍDO EL LOTE DE `Q`. No abrí `01-PROCESOS.md`, `esquemas/proceso.yaml`, las
   quince fichas de capacidad, la batería `comprobar-correccion-gate-de-cierre.py`, ni
   `entrada/00`, `02`, `04`. Cualquier contradicción entre esa materia y la mía se me ha
   escapado, y NO adjudico ninguno de los nueve hallazgos de ese lote.

2  NO HE LEÍDO EL DOCUMENTO 15 NI EL 19, PORQUE NO SE ME ASIGNARON. Eso significa que
   `D64`–`D68` los juzgo por cómo el documento 11 y el registro los describen, no por su
   fuente — el defecto exacto que el adjudicador `I` reprochó a `G` y a `H`. Lo declaro
   como límite mío ADEMÁS de denunciarlo como `P-08`, porque las dos cosas son ciertas.

3  NO HE EJECUTADO NADA. No corrí validadores, no ejecuté pruebas, no probé un escenario.
   Toda mi lectura es texto contra texto. Y no hay nada que ejecutar: `11-ARQ:8666` lo
   declara — «NADA ESTÁ CONSTRUIDO: ni una línea de kernel, runtime, tooling, esquema».
   Conforme al encargo, NO cuento eso como insuficiencia.

4  `P-03` DEPENDE DE UNA LECTURA, Y LO DIGO. Sostengo que §3.6 L3774 y §2.6.9 punto 4
   se contradicen sobre el mismo campo. Si alguien argumentara que el punto 4 es una
   especialización legítima que el contrato general admite tácitamente, el hallazgo
   bajaría a MEDIO — y seguiría siendo defecto, porque §2.8 niega en términos GENERALES
   («la recuperación no garantiza») justo la condición de la que depende la garantía de
   `W17`, y una sede canónica no debería negar en general lo que otra afirma en particular
   sin nombrar la excepción.

5  MI SEVERIDAD ES DISCUTIBLE; MIS HECHOS NO. Los ocho están abiertos en su fichero y su
   línea. La frontera GRAVE/MEDIO la trazo con el criterio que declaro al abrir §9. Si
   alguien graduara `P-01` y `P-05` como MEDIOS, mi veredicto NO cambiaría: `P-03` y
   `P-08` lo determinan por sí solos.

6  NO PUEDO CERTIFICAR `C-L.5` ENTERA. Sólo puedo certificar mi mitad: mi asignación es
   conocida, mi lectura es completa y la resta da vacío. Si `Q` no entrega manifiesto de
   lectura, la regla vuelve a ser incomprobable, y eso no está en mi mano.

7  NO HE VISTO EL DICTAMEN DE `Q` Y NO LO VERÉ. Donde nuestras materias se rozan —`E5-3`
   toca la grafía que `Q` juzga en el aparato de derivación— he juzgado sólo la mitad
   normativa, que es la mía, y he dicho cuál es.

8  DONDE ESCRIBO «VERIFICADO», LO ABRÍ. Donde no pude demostrar algo, lo he declarado
   insuficiente en vez de presumirlo en una u otra dirección.
```

---

#### 13 · RECOMENDACIÓN DE VEREDICTO

### INSUFICIENTE PARA F5

**No por cobertura.** Mi conjunto `asignadas − leídas íntegramente` es **vacío**, y lo he dicho antes del veredicto, como el encargo manda. Las veinte fuentes están leídas íntegras y sus veinte SHA-256 recalculados coinciden. El veredicto es de fondo.

**Razones, numeradas, cada una suficiente por sí sola para no cerrar:**

1. **La garantía central de `D105` no es derivable de su propio contrato** (`P-03`). La idempotencia de `W17` exige `predecesor` = `id(abandonada)`, y eso sólo lo escribe §2.6.9 punto 4. La sede que `D72` designa para derivar el esquema —§3.6 L3774— define el campo de otra manera, y §2.8 L2931 **niega en términos generales** que la recuperación garantice esa condición. Bajo la lectura de §3.6, dos arranques emiten dos `deriva`, se viola la regla 3 de la capa B y el diario queda no conforme por su propio validador — que es la consecuencia exacta que `D105` declara haber eliminado. **F6 no puede construir el evento sin decidir cuál de las tres frases manda.**

2. **La ventana que `D105` crea no tiene prueba** (`P-01`). `X54`, la única fila adversarial que barre el conjunto, dice «las **diecisiete** ventanas» cuando §2.6.5 deriva **dieciocho**, y ninguna de las 46 filas alcanza `W17`. La tabla se autodefine convertible en pruebas de F6 «sin traducción»: lo que no tiene fila, no se prueba. Es la tercera vez que este fichero registra el mismo modo de fallo, y las dos anteriores están escritas en él.

3. **`C-L.5` no queda cerrada** (`P-08`). `D106` hizo calculable `asignado − leído` —logro real, y `O-04` cerrado— y dejó `obligatorio − asignado` sin ninguna restricción. El manifiesto declara «FUENTES SIN ASIGNAR 0» sobre un universo elegido que omite **siete fuentes y 2 898 líneas** que el gate anterior tenía por obligatorias, incluidas `15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` —la que su propio inventario marca «← nadie la abrió», la que la condición de nivel 0 vigente nombra en primer lugar, y la fuente de la que cuelga `D64`— y las cinco de `kernel/operativo/diseno/`. **Tercera pasada consecutiva en que esa fuente no se abre.**

4. **El punto de entrada operativo del corpus está dos tandas atrasado y sin marca de histórico** (`P-05`), diciendo que el gate «no está encargado» cuando se emitió, y mandando al Owner **DOCE** presiones donde el recuento derivado da **TRECE** — por segunda vez seguida sobre la misma línea, con la corrección anterior registrada dos renglones más abajo. Es literalmente lo que la instrucción 3 del propio checkpoint manda comprobar.

5. **Cinco de mis ocho hallazgos los introdujo o los perpetuó esta misma tanda de corrección** (`P-01`, `P-02`, `P-03`, `P-06`, `P-08`). Es el mismo patrón que los tres gates anteriores midieron y nombraron —el adjudicador `I` contó seis de veintiocho; el gate de cobertura lo repitió— y es la razón por la que estas revisiones se encadenan. La corrección la vuelve a aplicar quien la recibe.

6. **Y una razón que es de forma, y por eso la pongo la última:** dos afirmaciones de evidencia publicadas se autofalsifican al comprobarlas —el barrido de `PN-15` (`P-06`) y el inventario «NADA PROBADO» del checkpoint (`P-04`)—, y una justificación de bloque se extiende a una fila de otra clase (`P-07`). Ninguna cambia el comportamiento del sistema. Todas erosionan lo único que este expediente tiene: que sus cifras se puedan rehacer.

**Lo que quiero que se lea junto al veredicto.** En mi materia, `F4c` ha hecho un trabajo bueno: `D105` resuelve el bloqueante `M-02` con la alternativa mínima y comparada; los `fsync` y el orden de cierre están completos; `PN-15` es una presión honesta que no toma la decisión del Owner; la cronología de `O16` fecha sin inventar; y el manifiesto de asignación es el primer instrumento del expediente que hace **comprobable** una regla de cobertura. **Diez de los trece hallazgos de mi lote están genuinamente superados y ninguno de mis ocho exige arquitectura nueva.** Lo que no puede hacerse es dar por cerrada una fase cuya garantía de recuperación no se deriva de su propio contrato, cuya ventana nueva no tiene prueba, cuya condición de cobertura sigue midiéndose sobre un universo que ella misma elige, y cuyo punto de entrada dice que el gate no está encargado.

---

```text
git status --porcelain  →  vacío        (comprobado al abrir y al cerrar)
git rev-parse HEAD      →  18cbfb57fe2286bb68011a31a8f3d07556d7aea9   (sin cambios)
```

**REVISOR `P` · dictamen cerrado.**

---

## 6 · Dictamen literal del REVISOR Q

> Se transcribe **íntegro y sin cambiar una palabra**, con los encabezados rebajados dos niveles.
> Se retira únicamente la línea de encabezamiento operativo con que el agente devolvió el
> documento —«Devuelvo el dictamen completo.»—, que no forma parte del dictamen. `Q` no vio el
> dictamen de `P` ni ninguna adjudicación antes de cerrar el suyo.

### DICTAMEN DEL REVISOR `Q`
#### Gate de cierre independiente de `F4c` — lote `Q`

---

#### 0 · Alcance y modo

```text
REVISOR              Q, contexto limpio. No escribí F4, no apliqué D16–D106, no soy autor
                     de ninguna corrección, no soy revisor A–O y no he visto el dictamen de P.
REPOSITORIO          /home/jose/ads-kernel
RAMA                 gate/f4c-cierre-con-manifiestos-20260829
CANDIDATA            7764cca69c9fbb7c3e89b70efdae7d6990f6c3b6
ÁRBOL DE LA CANDIDATA 03116b33bf4d8e996d8eccae51db927f4667ca58
HEAD AL TRABAJAR     18cbfb57fe2286bb68011a31a8f3d07556d7aea9
ÁRBOL DE HEAD        6e9d662d6cc8ff6e289c391490e70285c8a41e9e
DIFERENCIA           git diff --stat 7764cca..HEAD → 1 fichero, 140 inserciones:
                     SÓLO el manifiesto de asignación. El material juzgado es el de la
                     candidata, verificado y no supuesto.
MODO                 SÓLO LECTURA. Ni un fichero del repositorio modificado, ningún commit,
                     ningún push. Todo experimento en /tmp/q-gate/ sobre copias completas.
ÁRBOL AL ABRIR       git status --porcelain → vacío
ÁRBOL AL CERRAR      git status --porcelain → vacío
```

El manifiesto de asignación que gobierna mi cobertura es
`docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md`, 140 líneas,
SHA-256 **recalculado por mí** con `sha256sum`:
`c843b0c341183859b7f0f07db78cc67eade7ef98c4a96ad3edee23c769d2a976` — coincide con el declarado.
Lo leí **primero**, antes que ninguna otra fuente.

---

#### 1 · Evaluación provisional, y qué cambió

Emití una evaluación provisional **antes de abrir los documentos 16, 17, 18 y 20**, y la sellé
en `/tmp/.../scratchpad/EVALUACION-PROVISIONAL-Q.md`, SHA-256
`4fcf8f6f693b3099fe3b6f4bec4a57af475beb0a9507cd3f815365acec640ddc`. Decía, literalmente:

> «Sobre MI lote y sin haber leído 16-20: `D104` y la batería SUPERAN su listón. Los cinco
> defectos son MEDIOS/MENORES y ninguno bloquea F5 por sí solo. **PROVISIONAL: SUFICIENTE PARA
> F5 en lo que toca a `Q`, sujeto a cobertura completa.**»

**Qué se confirmó.** Mi derivación independiente de `<CAP>:revision` —hecha antes de mirar lo
publicado— coincide exactamente con `D104`. Las cuatro refutaciones prescritas fallan hoy. Los
cinco defectos provisionales (`Q-01`…`Q-05`) resistieron toda verificación posterior.

**Qué cambió, y es lo que mueve mi recomendación.** Leer las 8 735 líneas de los documentos
16–20 y las 2 163 de `ADS-PENDIENTES` no me dio ninguna razón nueva contra `D104`: me dio el
**criterio de cierre con el que el gate anterior falló a esta misma cadena**, y al aplicarlo a
la candidata aparecieron **diez hallazgos que la evaluación provisional no tenía**
(`Q-06`…`Q-15`). Concretamente, la razón 5 del documento 20 —«tres sedes vigentes afirman cosas
que el árbol desmiente, y ninguna estaba registrada»— **se reproduce en esta tanda con seis
sedes nuevas**, y la razón 4 —«la única garantía mecánica está refutada»— **se reproduce con dos
árboles defectuosos nuevos**. Mi recomendación provisional era `SUFICIENTE`. **La final no lo
es**, y el motivo del cambio es exactamente ése: no un defecto de `D104`, sino el mismo modo de
fallo que doce tandas llevan encadenando.

**Y publico donde me equivoqué.** Sospeché que la numeración de la tabla adversarial tenía
huecos sin declarar (`X24`, `X29`–`X36`, `X40`–`X46`). **Falso**: están declarados uno a uno en
`11-ARQUITECTURA-INTEGRADA.md` L1514–1519. Retiro la sospecha. También sospeché que la
descripción de `AUD` como «cero o un par, NUNCA los dos» en el checkpoint L301 era una sede
viva: **no lo es**, la clave que la contiene es `last_meaningful_event_anterior`, explícitamente
histórica. Retiro esa mitad; la otra mitad —L1020, en el bloque de condiciones— sí es viva, y es
`Q-14`.

---

#### 2 · MANIFIESTO DE LECTURA DEL REVISOR `Q`

Todos los SHA-256 y todos los recuentos de líneas están **recalculados por mí** con
`sha256sum` y `wc -l`, y **coinciden uno a uno con el manifiesto de asignación**. Ninguna
fuente se ha sustituido por `grep`, índice ni resumen.

##### 2.1 · Las OCHO fuentes comunes

| # | ruta exacta | líneas | SHA-256 (16 primeros) | estado |
|---|---|---|---|---|
| 1 | `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | 2 163 | `a88609167dbbea28` | **LEÍDO ÍNTEGRO** |
| 2 | `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | 1 257 | `8243034f286160cc` | **LEÍDO ÍNTEGRO** |
| 3 | `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` | 1 650 | `18f876d4cd47a2f7` | **LEÍDO ÍNTEGRO** |
| 4 | `docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` | 3 665 | `1e71366b10d22938` | **LEÍDO ÍNTEGRO** |
| 5 | `docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md` | 801 | `d7d2e4fa3f878e0c` | **LEÍDO ÍNTEGRO** |
| 6 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 9 280 | `84063c2a344a2d15` | **LEÍDO ÍNTEGRO** |
| 7 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 725 | `3be45994f4d00e82` | **LEÍDO ÍNTEGRO** |
| 8 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 2 051 | `76ed2d768cdb4db8` | **LEÍDO ÍNTEGRO** |

**1 · `ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md`** — primera sección sustantiva: `## 1. Por
qué existe este documento` (L8). Última: `## 31. Registro de cambios de este documento` (L2153).
Anclas de regiones separadas:
- L6 — «**No es todavía especificación normativa ni autoriza a implementar automáticamente sus propuestas.**»
- L788–790 — la lista condicional de §5.18: «UX e investigación, dirección visual, sistema de diseño, … o gobierno de IA».

Qué confirma: **conté yo mismo los condicionales de §5.18 y son TRECE**, lo que valida `D94`/`M-1`
sin copiar la cifra. Confirma también `N-05` en la mitad que puedo abrir: L914 dice «**Principio
aceptado:**» sobre la frase literal «Detectar automáticamente; actualizar conscientemente», y
L3–L6 declara que el documento no es normativo. **BLOQUE B (§8–§12) y BLOQUE C (§13–§17), leídos
íntegros, CONFIRMAN a F4 y no lo refutan**: la certificación por niveles y la unidad amplia
están planteadas como necesidad con diseño pendiente y decisiones abiertas (§17, doce puntos),
sin ninguna regla que contradiga la arquitectura entregada. Qué limita: nada de este documento
toca `<CAP>:revision` ni la segunda participación de `DOM`/`SEG`; no aporta ni una vía de escape.

**2 · `16-GATE-FINAL-INDEPENDIENTE-F4C.md`** — primera: `## Corpus obligatorio: inventario y
cobertura` (L46). Última: `## **INSUFICIENTE PARA F5**` (L1196). Anclas: L68 «`## DICTAMEN DEL
REVISOR A`» · L986 «`## ADJUDICACIÓN DEL ADJUDICADOR C`». Confirma la procedencia de `A1`–`A13`,
`M-1`–`M-9`, `m-1`–`m-4` y `F-01`–`F-12`, y el reparto A·B·C. Limita: su cobertura fue declarada
incompleta por el gate siguiente, y su texto es inmutable.

**3 · `17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md`** — primera: `## Inventario de las fuentes del
nivel 0` (L41). Última: `## ADJUDICACIÓN DEL ADJUDICADOR F` (L1094). Anclas: L60 (fila de
inventario de `C2`, 539 líneas) · **L116** — «… `539` … **22 bloques `ads:perfil-agente`**».
Contradice al árbol: **derivé la cifra yo mismo, `grep -c '```yaml ads:perfil-agente'` sobre `C2`
devuelve 21**, y los `id:` también 21. Es `N-04`, confirmado por mi cuenta.

**4 · `18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md`** — primera: `## El veredicto, por delante` (L55).
Última: `## 14 · Condición exacta para F5, ordenada por lo que desbloquea` (L3562). Anclas: L57
«`> # INSUFICIENTE PARA F5`» · L3556 «`## 13 · VEREDICTO`». Confirma `I-01`–`I-28`, las diez
filas FALLIDAS y la causa original de `D87`–`D95`. Limita: es inmutable, y su veredicto es
anterior a dos tandas.

**5 · `20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md`** — primera: `## 1 · Identidad y
procedencia` (L8). Última: `## 11 · Ningún hallazgo se ha corregido` (L779). Anclas: **L387** —
«`01-PROCESOS.md` L420–427, `proceso:AUD`, `obligatorias` completas: una sola,
`conclusion-fundada`, `capacidad_productora: "INV"`. **No hay `VER`.**» · **L750** — «**dos árboles
defectuosos distintos pasan 30/30 en verde** (`M-04`)». Es la fuente de los 21 hallazgos que
adjudico en §7. Verifiqué L387 contra el fichero: exacto.

**6 · `11-ARQUITECTURA-INTEGRADA.md`** — primera: `# 0 · Resumen ejecutivo` (L92). Última:
``## `C-L.5` · La condición de COBERTURA del próximo gate`` (L9213). Anclas de regiones muy
separadas: **L4360** — «· TODO `abandonada` DECLARA SU `deriva`, y ese `deriva` existe en el
diario y nombra las mismas rutas e items» · **L8856–8861** — «NORMALIZACIÓN —Y ES TODA LA
INFERENCIA QUE HAY— … `capa_exigida`, `condicion`, `criterio_de_satisfaccion` y
`autoridad_de_retirada` **NO se leen**». La primera **contradice** a `D105` (`Q-06`); la segunda
**es falsa sobre el derivado real** (`Q-05`). Confirma, en cambio, que el bloque contractual de
`D104` (L8771–9014) coincide exactamente con mi derivación independiente.

**7 · `DECISIONES-Y-CONTRADICCIONES.md`** — primera: `## 1 · Decisiones tomadas sin consultar`
(L11). Última: `## 4 · Límites declarados de esta iteración` (L707). Anclas: **L412** — `D105`,
«`deriva_emitida` queda PROHIBIDO en `abandonada`; el `deriva` gana `abandonada_id`» ·
**L527–537** — el «ADDENDUM DE CRONOLOGÍA, registrado por `M-07`», con `2026-08-28` formulación y
`2026-08-29` confirmación del Owner. Confirma `D1`–`D106` sin huecos y `O1`–`O16` intactas —lo
derivé, `G-11b` no me sirve (ver `Q-01`)—, y confirma que `M-07` está resuelto sin reescribir
`O16`.

**8 · `CHECKPOINT-ADS-NEXT.md`** — primera: la cabecera de estado (L8–L60). Última: `## Siguiente
acción exacta` (L1978–2051). Anclas: **L6** — «**Basta decir «Continúa»**: la siguiente acción
exacta está al final.» · **L2031** — «5 QUÉ LLEVAR AL OWNER  las **DOCE** presiones de §16».
Las dos juntas son `Q-08`: el propio documento remite al lector a una sección que está caducada
dos tandas. Confirma, en cambio, que la excepción del kernel es hoy exacta y derivada (SEIS
ficheros = 3 directos + 3 de evidencia), lo que cierra `M-06`.

##### 2.2 · Las VEINTITRÉS fuentes exclusivas

| # | ruta exacta | líneas | SHA-256 (16) | estado |
|---|---|---|---|---|
| 9 | `kernel/operativo/recorrido/01-PROCESOS.md` | 564 | `98b5cbc836121044` | **LEÍDO ÍNTEGRO** |
| 10 | `kernel/operativo/esquemas/proceso.yaml` | 49 | `bd391d5acddff134` | **LEÍDO ÍNTEGRO** |
| 11 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 1 109 | `c3ed5dffeb281219` | **LEÍDO ÍNTEGRO** |
| 12 | `docs/evolucion/verificacion/README.md` | 102 | `a4fb2738cb3112e0` | **LEÍDO ÍNTEGRO** |
| 13 | `docs/evolucion/00-INDICE.md` | 111 | `ed673d814a0e008c` | **LEÍDO ÍNTEGRO** |
| 14 | `kernel/operativo/entrada/00-INDICE.md` | 28 | `315b2790cb66bb4c` | **LEÍDO ÍNTEGRO** |
| 15 | `kernel/operativo/entrada/02-CIRCUITO.md` | 145 | `750d39a29f05e7f2` | **LEÍDO ÍNTEGRO** |
| 16 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | 187 | `1716bd3d8b48107d` | **LEÍDO ÍNTEGRO** |

**9 · `01-PROCESOS.md`** — primera: ``## `FEA` — Capacidad nueva`` (L26). Última: ``## `SIS` —
Evolución del sistema`` (L518). Anclas: **L419** — `proceso:AUD`, `propietario_global: "DERIVADO
del encargo … NUNCA se asigna a mano"` · **L458** — `proceso:DIR`, `propietario_global: "la
capacidad PROPIETARIA de la decisión que se sustituye … NUNCA lo elige DSP"`. Es la fuente de mi
derivación independiente (§5). Confirma el discriminante estructural de `D104` y refuta cualquier
partición por la palabra «DERIVADO».

**10 · `esquemas/proceso.yaml`** — primera: la cabecera del esquema (L1). Última: el bloque de
`condicionales` (L49). Anclas: **L22** — «# Texto y no ref: en DIR y AUD el propietario se DERIVA,
no se asigna (b.16)» · **L23** — `propietario_global: {tipo: texto, min: 3}`. Confirma `N-02` en su
hecho y confirma que `D104` tenía que abandonar el barrido léxico.

**11 · `comprobar-correccion-gate-de-cierre.py`** — primera: la cabecera y `_git()` (L75–L90).
Última: el informe y `sys.exit` (L1101–L1109). Anclas: **L325** — `_VIGILADAS = ("DOM", "SEG")` ·
**L359** — `ancla = "VER" if "VER" in obl else (obl[-1] if obl else None)`. La primera es `Q-09`,
la segunda `Q-02`. Confirma que **no existe ningún literal `_COMPONENTES_CL13`**: los componentes
de `C-L.13` se derivan de su fila de detalle (L624–634).

**12 · `verificacion/README.md`** — primera: `## Por qué estas treinta, y por qué así` (L30).
Última: `## Lo que esta batería NO comprueba, y se dice` (L85). Anclas: **L3–L6** — «comprueba,
sobre el árbol y no sobre lo que el texto afirma de sí mismo…» · **L93–L95** — «NO SUSTITUYE AL
GATE  no juzga si la arquitectura es SUFICIENTE PARA F5». Limita: la propia batería declara que
comprueba «TEXTO contra TEXTO», y esa declaración es correcta y honesta.

**13 · `docs/evolucion/00-INDICE.md`** — primera: `## Los documentos en voz del Owner` (L14).
Última: `## Lo que este trabajo ha corregido de sí mismo` (L106). Anclas: L40 «`## Lo que la
directiva ordena antes de diseñar nada`» · **L110–111** — «el gobierno Git no estaba ausente, y el
hallazgo real es que la línea 2.0 nunca recogió lo que la 1.3.0 ya gobernaba».

**14 · `entrada/00-INDICE.md`** — primera y última: `## Las tres frases que resumen el paso 1`
(L16, es fichero de 28 líneas). Anclas: **L19–L20** — «La expresión literal del Owner se conserva
siempre. La interpretación se añade al lado, nunca encima.» · **L22–L24** — «Ninguna expresión se
convierte en trabajo por sí sola.»

**15 · `entrada/02-CIRCUITO.md`** — primera: `## Los caminos hacia atrás` (L88). Última: `## Qué
garantiza este circuito` (L136). Anclas: L108 «`## Dónde termina cada clase de entrada`» ·
**L139** — «[ ] la expresión literal del Owner sobrevive a todo el recorrido, sin excepción». Es
uno de los tres ficheros directos de la excepción exacta del kernel (`K-09`, commit `d868bcb`),
y lo verifiqué contra `git diff --name-only 05f71b7 -- kernel/`.

**16 · `entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md`** — primera: `## 1 · Escala de incertidumbre —
cinco ejes` (L10). Última: `## 4 · Qué hacer cuando el Owner no contesta` (L149). Anclas: L56
«`## 2 · Tabla de confirmación — cuándo se molesta al Owner`» · **L156–157** — «`estado =
en-conversacion` … `estado_paquete = esperando-owner`  Son dos cosas distintas y por eso son dos
campos».

##### 2.3 · Las QUINCE fichas de capacidad — todas LEÍDAS ÍNTEGRAS

Total derivado por mí: `cat kernel/operativo/capacidades/*/CAPACIDAD.md | wc -l` = **1 829**,
idéntico al manifiesto. Dos anclas por ficha, de regiones separadas (cabecera y bloque
`deriva_de`):

| ficha | líneas | SHA-256 (16) | ancla A (L1–5) | ancla B (`deriva_de`) |
|---|---|---|---|---|
| `APR` | 95 | `a870911530909584` | L3 «**No es un trámite universal.**» | L51 «a.3 · APR: no es trámite universal; se materializa ante señal real» |
| `ARQ` | 104 | `6ca11b5f09883e24` | L3 «es **medir el radio de impacto**» | L55 «b.16 · ARQ es propietario global de DEU y de DEF cuando C-ARQ» |
| `CON` | 107 | `e0f79e6c3a467302` | L3 «**no redecide capas anteriores**» | L51 «b.16 · CON:experimental dentro de INV y de DIR» |
| `DIS` | 147 | `06f019010d45771f` | L3 «la primera capacidad desarrollada hasta nivel operativo» | L87 «b.16 · C-DIS y el papel de DIS en FEA, GAP, DEF y DIR» |
| `DOM` | 135 | `926c7144cb098caa` | L3 «**veto duro sobre la integridad y la recuperabilidad**» | **L51 «b.16 · DOM participa dos veces: condiciones antes de CON, revisión después de VER»** |
| `DSP` | 152 | `acb292f882e77d74` | L3 «**total sobre el orden y la ruta, y ninguna sobre el contenido**» | L68 «a.3 + enmienda E1.1 · DSP: … autoridad sobre orden y ruta, ninguna sobre contenido» |
| `ENC` | 174 | `f71b8e43f6e2d66f` | L3 «`ENC` es la **decimoquinta capacidad base**» | L78 «enmienda E1 · ENC como decimoquinta capacidad base» |
| `ENT` | 123 | `91a81d3cf1cbfa61` | L3 «existe **fuera del entorno de desarrollo**» | L52 «b.16 · ENT es propietario global de INC» |
| `INV` | 96 | `47412638e7552da1` | L3 «**una decisión no puede tomarse todavía**» | L49 «b.16 · INV es propietario global de los items INV» |
| `PLT` | 108 | `a5f87977c58ed1d0` | L3 «**Construye y posee** la maquinaria» | L49 «b.16 · PLT es propietario global de los items DEP» |
| `PRD` | 105 | `e83b0e08272e219d` | L3 «un **resultado definido con criterio de terminado**» | L56 «b.16 · PRD es propietario global de FEA y GAP» |
| `SEG` | 135 | `19bfd38a7a24b57f` | L3 «veto … **no levantable** (a.5, G27)» | **L51 «b.16 · SEG participa dos veces y es obligatoria antes de construir en DEP»** |
| `SIS` | 119 | `02089f36d1244356` | L3 «Trabaja **sobre la fábrica**» | L55 «b.16 · SIS es propietario global de los items SIS» |
| `USO` | 94 | `65f144e4a5c756ef` | L3 «**No equivale al Owner.**» | L50 «b.16 · C-USO y su activación en FEA, GAP, DEF, DEU e INC» |
| `VER` | 135 | `91a16b482629daf3` | L3 «**No emite un sí o un no.**» | L52 «b.16 · VER:decision como paquete obligatorio de todo DIR» |

**Lo que la lectura íntegra de las quince aporta y ningún `grep` habría dado:** `grep -rn 'participa
dos veces'` sobre las quince devuelve **exactamente dos líneas, `DOM` L51 y `SEG` L51**. El conjunto
vigilado por la batería **es derivable del corpus** y está escrito a mano. Es `Q-09`.

---

#### 3 · EL CRUCE: asignadas − leídas íntegramente

```text
ASIGNADAS                 31   8 comunes + 23 exclusivas
LEÍDAS ÍNTEGRAMENTE       31
PARCIALMENTE LEÍDAS        0
NO ABIERTAS                0

ASIGNADAS − LEÍDAS ÍNTEGRAMENTE = ∅   (conjunto vacío)
```

Líneas obligatorias de mi lote, derivadas sumando la columna del manifiesto y verificadas con
`wc -l` fichero a fichero: **8 comunes = 21 592** · **23 exclusivas = 4 124** · **total 25 716**.

**El conjunto está vacío.** Por tanto **NO procede** la recomendación
`INSUFICIENTE PARA F5 POR COBERTURA`, y mi veredicto se emite sobre el fondo.

---

#### 4 · Mi derivación propia de `<CAP>:revision`

Hecha a mano sobre `01-PROCESOS.md` y `esquemas/proceso.yaml` **antes de abrir el bloque
publicado** de `11-ARQUITECTURA-INTEGRADA.md`.

```text
DISCRIMINANTE      propietario_global ∈ {las quince nombres de directorio}, por igualdad
                   exacta de cadena. No por subcadena y no por la palabra «DERIVADO».
ESTÁTICOS  (7)     FEA · GAP · INC · INV · DEU · DEP · SIS
POR ITEM   (3)     DEF ("ARQ cuando C-ARQ…; CON en caso contrario")
                   AUD ("DERIVADO del encargo… NUNCA se asigna a mano", L419)
                   DIR ("la capacidad PROPIETARIA de la decisión que se sustituye", L458)

PARES ESTÁTICOS = 9, repartidos en 5 procesos:
   FEA·DOM  FEA·SEG      DOM:condiciones / SEG:condiciones      vía 4
   GAP·DOM  GAP·SEG      DOM:condiciones / SEG:condiciones      vía 4
   DEU·DOM  DEU·SEG      DOM:condiciones / SEG:condiciones      vía 4
   DEP·DOM               DOM:condiciones                        vía 4
   DEP·SEG               obligatoria `condiciones-de-seguridad`,
                         capacidad_productora: "SEG", desnuda    vía 2
   INC·SEG               SEG:condiciones                        vía 4
   → vías: 1 por la 2, 8 por la 4. NINGUNA por la 1 ni por la 3 hoy.
   INV y SIS son ESTÁTICOS y NO aportan par: no tienen DOM ni SEG por ninguna vía.

ANCLA DE POSICIÓN  obligatoria de VER si la hay; si no, la ÚLTIMA obligatoria.
   tras VER   FEA GAP DEF INC DEU DEP DIR SIS   (8)
   sin VER    INV → `evidencia-producida` (INV)
              AUD → `conclusion-fundada`  (INV)

POR ITEM
   AUD  condicionales DESNUDOS `DOM` (C-DOM) y `SEG` (C-SEG), independientes
        → puede producir ∅ · {DOM} · {SEG} · {DOM,SEG}. Las CUATRO son alcanzables.
   DIR  sin DOM/SEG en condicionales → sólo por vía propietaria, con el item delante.
   DEF  propietario resuelve a ARQ o CON, condicionales sin DOM/SEG → hoy nunca exige par.

NO HAY DÉCIMO PAR ESTÁTICO.
```

Después abrí el bloque publicado (L8771–9014) y **coincide exactamente**: mismos siete estáticos,
mismos tres por item, «CINCO procesos y NUEVE pares», `(DEP, SEG)` por la vía 2 y los otros ocho
por la vía 4, anclas sin `VER` en `INV` y `AUD`, las cuatro combinaciones de `AUD`. La ejecución
de `G-15` sobre el árbol real devuelve lo mismo, y lo reproduje yo con el propio módulo cargado
fuera del repositorio.

**Una sola discrepancia con lo publicado**, y es `Q-11`: L8880–8881 escribe
«`INV` `AUD` → tras su única obligatoria, `conclusion-fundada` de `INV`». La única obligatoria de
`proceso:INV` se llama **`evidencia-producida`**; `conclusion-fundada` es la de `proceso:AUD`.

---

#### 5 · Juicio de `D104` — intenté REFUTARLO, no confirmarlo

Punto por punto, contra el listón que se me fijó:

| exigencia | resultado | evidencia mía |
|---|---|---|
| Las cuatro vías tipadas **operan de verdad** | **SÍ** | `_analizar()` L339–369 emite vía 1/2/3/4 por CAMPO y FORMA; los cuatro fixtures de `G-15` (L437–465) se ejecutan en cada corrida y los reproduje aislados |
| La vía **PROPIETARIA no es decorativa** (cero instancias hoy) | **SÍ** | fixture propio `R1`: `proceso:SIS` con `propietario_global: "SEG"` → `G-15` **FALLA** con «publica CINCO procesos y el catálogo deriva 6; publica NUEVE pares y el catálogo deriva 10» |
| Los **condicionales de `AUD` se evalúan** de verdad | **SÍ** | control positivo `n6`: borrar los dos condicionales desnudos de `AUD` → `G-15` **FALLA** nombrando «fixture VÍA 3: los condicionales desnudos de `AUD` no se derivan» **y** las cuatro combinaciones |
| **`DIR` por la misma regla, sin excepción escrita** | **SÍ** | `G-15` §5 (L505–511) exige `DIR ∈ dinámicos`, `DIR ∉ estáticos`, y dos fixtures de item. Doc 11 L8872: «`DEF` y `DIR` entran por la misma regla que `AUD`, sin excepción escrita para ninguno» |
| **Ningún análisis de texto libre** en el algoritmo | **CASI** | el discriminante es pertenencia a conjunto y la normalización es `split(':')[0].split('/')[0]`. **Pero el troceado es una regex de línea sobre un corte de texto, no YAML**: la prosa de `criterio_de_satisfaccion` sí se lee. Es `Q-05` |
| El **ancla funciona sin `VER`** | **SÍ en la regla, NO en la normalización** | `AUD` e `INV` anclan en su última obligatoria. **Pero `"VER" in obl` compara la cadena cruda**: `VER:dosier` —vía 4 legítima— desplaza el ancla en silencio. Es `Q-02` |
| **No aparece un décimo par estático** | **SÍ** | derivé 9 a mano y mecánicamente, y el fixture negativo de `G-15` (§7) demuestra que quitar la obligatoria `SEG` de `DEP` retira el par |
| Un item `AUD` produce **∅ · {DOM} · {SEG} · {DOM,SEG}** | **SÍ** | las cuatro están en los cinco fixtures de `G-15` (L485–495) y en doc 11 L8951–8954 |
| **F6 no necesita elegir arquitectura** | **SÍ** | el contrato fija vías, normalización, discriminante, ancla, algoritmo, regla por item, dos salidas, casos, contraejemplos y error. No queda ni una decisión de diseño abierta |

**Veredicto sobre `D104`, en una línea: el listón se supera.** Es la primera de las cuatro
formulaciones que no me obliga a elegir nada, y las cuatro causas que la gestaron —`O-01`,
`M-01`, `N-02`, `N-01`— están cerradas con fixture ejecutable, no con prosa. Los defectos que le
encuentro (`Q-02`, `Q-03`, `Q-05`, `Q-10`, `Q-11`, `Q-12`) son de **su comprobación y de su
proyección publicada**, no de su arquitectura.

---

#### 6 · La batería, y las CUATRO refutaciones

Ejecutada sobre el árbol real: **30/30 en verde**, y `git status --porcelain` sigue vacío
después. Reproducida desde `/tmp` sobre copia: 30/30. La raíz se deriva de `__file__` y es
portable — lo verifiqué desde quince directorios distintos.

##### 6.1 · Las cuatro refutaciones prescritas

Cada una en su copia aislada de `/tmp/q-gate/`, sobre el árbol completo. **En las cuatro falla la
comprobación RESPONSABLE, y su diagnóstico DERIVA la causa.**

| # | mutación exacta | comprobación que falla | diagnóstico literal |
|---|---|---|---|
| **R1** | `proceso:SIS` → `propietario_global: "SEG"`: participación PROPIETARIA nueva | **`G-15`** (responsable) + `G-23` (lateral) | «publica CINCO procesos y el catálogo deriva **6**; publica NUEVE pares y el catálogo deriva **10**» |
| **R2** | segunda proyección «SEIS procesos · DIEZ pares» en el bloque de `D104` | **`G-15`, y sólo `G-15`** | «hay **2** proyecciones en el bloque y debe haber UNA: `[('CINCO','NUEVE'), ('SEIS','DIEZ')]`» |
| **R3** | `C-L.12` movida a «CORREGIDAS EN F4c» con los contadores ajustados a 9·1·1·1·1 | **`G-16`, y sólo `G-16`** | «`C-L.12`: el resumen lo pone en «CORREGIDAS EN F4c» y su fila de detalle dice «REGISTRADA PARA F5»» |
| **R4** | `.git` eliminado + fila `D67` reescrita + veredicto del documento 18 volteado a `SUFICIENTE` en tres sedes | **`G-11` `G-21` `G-22` `G-23`** | `G-21/22/23`: «**GIT NO RESPONDE**: no se puede saber qué se tocó» |

Diseño de `R1`, y por qué lo cambié: mi primer intento fue mover el propietario de `DEU` a `DOM`.
Lo descarté antes de ejecutarlo porque `(DEU, DOM)` **ya existe** por la vía 4 y el orden de
escritura del diccionario habría sobreescrito la vía 1 con la 4, dejando el recuento en 9: la
prueba no habría demostrado nada. `proceso:SIS → "SEG"` crea un par genuinamente nuevo.

**En `R3` la comprobación responsable falla SOLA**, sin ningún fallo lateral, que es el caso
más limpio de todos.

##### 6.2 · Controles positivos, para separar detección de casualidad

- **`M-11` está vivo, no es código muerto.** Inyecté un estado compuesto en la matriz del
  checkpoint: `G-16` **FALLA** nombrando `A1`. El código que `M-11` denunció está retirado con
  su motivo escrito (L548–551) y sustituido por detección sobre la línea entera.
- **La vía 3 y la regla por item de `AUD` son código vivo** (`n6`, arriba).
- **La excepción de SEIS ficheros se DERIVA y se contrasta.** `G-23` calcula
  `git diff --name-only 05f71b7 -- kernel/` → 6 ficheros, los clasifica en 3 directos + 3 de
  evidencia derivada y los cruza contra la prosa del checkpoint. Cuando toqué dos fichas de
  capacidad, `G-23` dijo: «el checkpoint publica `('6','3','3')` y Git deriva `(8,5,3)`». Es
  derivación real, no afirmación.
- **No existe ningún literal `_COMPONENTES_CL13`.** Los seis componentes de `C-L.13` salen de su
  fila de detalle (L624–634).
- **Sin código muerto, salvo un residuo.** Barrido AST de las 216 definiciones del fichero: una
  sola sin uso, `ancho` en L1102. Es `Q-15`.
- **Git falla cerrado en `G-11`, `G-21`, `G-22` y `G-23`.** Los cuatro llevan
  `_raw is not None` en su predicado. **`G-11b` no.** Es `Q-01`.

##### 6.3 · Refutaciones NUEVAS, que nadie había planteado

Cinco árboles defectuosos nuevos. **Dos de ellos no producen ni un fallo responsable.**

| # | árbol defectuoso construido | resultado |
|---|---|---|
| `n5` | **dos ficheros NUEVOS y no rastreados bajo `kernel/`**: `recorrido/01-PROCESOS-BIS.md` (copia entera, 564 líneas: segunda sede del catálogo de procesos) y `contratos/C8-SEGUNDA-SEDE.md`, que declara por escrito que contradice a `C4` | **30/30 EN VERDE** |
| `n9` | una línea `capacidad_productora: "DOM"` escrita **dentro de la prosa** de `criterio_de_satisfaccion` de `FEA/intencion-definida` | `G-15` **VERDE**; sólo cae `G-23`, lateral. El derivado sí la lee: `FEA part = [('DOM',2), ('DOM',4), ('SEG',4)]` frente al real `[('DOM',4), ('SEG',4)]` |
| `n2` | `proceso:INC`, obligatoria de `VER` tipada como `"VER:dosier"` (vía 4 legítima) | `G-15` **VERDE**, y el ancla de `INC` se ha movido a `APR`: «anclas sin VER `['AUD','INC','INV']`» |
| `n4` | condicionales de `FEA` de `DOM:condiciones`/`SEG:condiciones` a `DOM`/`SEG` desnudos | `G-15` **VERDE** con vías `[(2,1),(3,2),(4,6)]`, mientras doc 11 L8941 sigue diciendo «los otros ocho por la vía 4» |
| `n8` | borradas las **dos únicas** declaraciones del corpus de la segunda participación (`DOM` L51, `SEG` L51) | `G-15` **VERDE** y sigue afirmando los nueve pares; sólo cae `G-23`, lateral |

**La razón 4 del gate anterior —«dos árboles defectuosos distintos pasan 30/30 en verde»— vuelve
a ser cierta**, con árboles distintos de los que `M-04` usó.

---

#### 7 · Adjudicación de los 21 hallazgos del documento 20

Un solo estado por hallazgo. Sin estados compuestos.

| id | sev. orig. | **estado** | motivo, verificado por mí |
|---|---|---|---|
| `M-01` | GRAVE | **SUPERADO** | Vía 3 implementada y ejercitada: `_analizar` emite `('DOM',3)`/`('SEG',3)` para `AUD`; borrarlos hace **fallar** `G-15` nombrando la vía 3 y las cuatro combinaciones (`n6`) |
| `M-02` | GRAVE | **SUPERADO** | `D105` invierte la referencia: `deriva_emitida` PROHIBIDO en `abandonada` (doc 11 L4216), `abandonada_id` obligatorio en `deriva` (L4218), y la regla 3 del reparto lo declara «**Invertido por `D105`**» (L4406). `id(abandonada)` ya no depende de `id(deriva)`. **Queda un residuo textual: `Q-06`** |
| `M-03` | GRAVE | **SUPERADO** | `fsync` del fichero **y del directorio** del `deriva`, obligatorio y nuevo (L1873); orden exacto de seis pasos (L1901–1902); ventana `W17` (L1163). **Queda `Q-13`, que la deja fuera de `X54`** |
| `M-04` | GRAVE | **SUPERADO** en los dos contraejemplos que nombra | `R1` y `R2` fallan hoy con diagnóstico derivado, y las cuatro refutaciones prescritas también. **La clase NO está cerrada: cinco árboles nuevos (§6.3), dos de ellos sin ningún fallo responsable** |
| `M-05` | MEDIO | **SUPERADO** | `D106`(i) retira la disyunción: la prueba posterior de `PN-15` exige una fila en `a.11`, material APROBADO que sólo `F5` puede escribir. `G-12` lo comprueba |
| `M-06` | MEDIO | **SUPERADO** | La «EXCEPCIÓN EXACTA DEL KERNEL» enumera hoy **SEIS ficheros, 3 directos + 3 derivados**, y `G-23` los deriva de Git y los contrasta. Verificado por mí sobre el árbol real y sobre un árbol mutado |
| `M-07` | MEDIO | **SUPERADO** | `D106`(iii): ADDENDUM DE CRONOLOGÍA en `DECISIONES` L527–537, con `2026-08-28` formulación y `2026-08-29` confirmación. No reescribe `O16` ni crea `O17` |
| `M-08` | MENOR | **SUPERADO** | Doc 11 L8776 corrige a **L502–503** y deja constancia de que la cita anterior decía L504–505 |
| `M-09` | MENOR | **REGISTRADO PARA F5** | `E5-3` en doc 11 L8759, con ruta, ubicación (`b` L836), corrección exacta y prueba. `(b)` es material APROBADO que `F4c` no puede editar |
| `M-10` | MENOR | **SUPERADO** | Derivé el orden de la tabla: `… X56 X57 **X58** X59 X60 X61 X62`. Los huecos de la serie están declarados en L1514–1519 |
| `M-11` | MENOR | **SUPERADO** | El código muerto está retirado con su motivo escrito y sustituido; el sustituto **dispara** y nombra `A1` (control positivo mío) |
| `M-12` | MENOR | **SUPERADO** | `G-21`, `G-22` y `G-23` —los tres que nombra— fallan cerrado con «GIT NO RESPONDE» (`R4`). **Un cuarto, `G-11b`, quedó fuera: es `Q-01`** |
| `N-01` | GRAVE | **SUPERADO** | El ancla tiene dos ramas derivables y ninguna presupone `VER`; `DIR` entra por la misma regla, sin excepción escrita, con dos fixtures ejecutados. **Residuos: `Q-02` y `Q-11`** |
| `N-02` | MEDIO | **SUPERADO** | Discriminante por igualdad de cadena contra `_CAPS = os.listdir(capacidades/)`; el fixture «la capacidad que decida el encargo» cae correctamente en dinámico. No se busca la palabra «DERIVADO» en ninguna parte |
| `N-03` | MENOR | **NO APLICABLE** — con motivo | Cae sobre `E1` y `(a)`, **fuera de mi lote**. No sustituyo una lectura ausente por una presunción. Consta que está registrado como `E5-4` (doc 11 L8760) |
| `N-04` | MENOR | **CONTRATADO PARA F6** | Confirmo el hecho por derivación propia: `C2` tiene **21** bloques `ads:perfil-agente`; el documento 17 L116 dice **22**. El documento 17 es inmutable; el checkpoint reancla a 21 y contrata la derivación a F6 (`C-L.10`). Concurro |
| `N-05` | MENOR | **SUPERADO** | Doc 11 L6682–6695 registra la segunda sede. **Verifiqué mi mitad**: `ADS-PENDIENTES` L914 dice «Principio aceptado», y L3–L6 declara el documento no normativo. Ningún calificativo tiene fuerza de norma |
| `O-01` | MEDIO | **SUPERADO** | La vía 1 está implementada en los dos niveles y su fixture corre en cada corrida; `R1` demuestra que una participación propietaria nueva **hace fallar** `G-15` |
| `O-02` | MENOR | **SUPERADO** | El mensaje de éxito de `G-16` deriva `_resumen` de `_declarado`; la cadena `8+2+1+1+1` ya no está codificada |
| `O-03` | MEDIO | **SUPERADO** | Con `M-03`: el `deriva` es durable antes de retirar el marcador, y el arranque lo **completa** de forma idempotente (`D105`(iv)), luego el diario no queda permanentemente inválido |
| `O-04` | MENOR | **SUPERADO en su causa** | La causa que nombra —ausencia del manifiesto de asignación— está resuelta: existe, está publicado, verifiqué su SHA-256 y su cruce con mis 31 fuentes es exacto. **`C-L.5` sigue abierta por construcción** hasta que se crucen los manifiestos de lectura de todos los revisores, y eso no es mi adjudicación |

```text
RECUENTO DERIVADO DE LAS FILAS DE ARRIBA, no copiado
  SUPERADO                17
  REGISTRADO PARA F5       1   M-09
  CONTRATADO PARA F6       1   N-04
  NO APLICABLE             1   N-03, por lote
  FALLIDO                  0
  ABIERTO                  0
                          ──
                          21
```

Coincide con la partición que el checkpoint publica (17 · 2 · 1 · 1), **con una diferencia que
declaro**: el checkpoint pone `N-03` en «REGISTRADOS PARA F5» y `O-04` en «ABIERTO PARA EL
SIGUIENTE GATE». Yo no puedo juzgar `N-03` —no está en mi lote— y juzgo `O-04` superado **en su
causa**, distinguiéndolo del estado de `C-L.5` como condición.

---

#### 8 · Lo que expresamente NO fundamenta mi juicio

Comprobé, y consta a favor: la ausencia de **runtime**, de **piloto**, de **adaptadores
certificados** y de **PesquerApp** está **bien declarada**, con propietario y fase.

- El checkpoint L1138–1140: «NADA CONSTRUIDO: ni kernel, ni runtime, ni tooling… Las correcciones
  son DISEÑO CORREGIDO, no diseño implementado.»
- L1141–1144: «NADA PROBADO: las **46** filas… los 11 escenarios negativos… **Ninguno ejecutado**.»
- L1161: «ningún adaptador existe, y por tanto ninguno está certificado.»
- `O15` (L1150–1160): PesquerApp será la primera adopción real, y **`O15` NO autoriza iniciar la
  adopción**.
- El `README` de la batería L88–L95 declara sus tres límites, incluido que no ejecuta nada del
  protocolo y que no juzga suficiencia.
- `C-L.10` está **CONTRATADA PARA F6 con cero líneas escritas**, y lo verifiqué.

**Ninguna de estas ausencias entra en mi veredicto.** Están declaradas con honestidad poco
frecuente, y contarlas como insuficiencia sería castigar precisamente la disciplina que el
corpus mantiene.

---

#### 9 · Hallazgos del revisor `Q`

Ninguno corregido: el encargo lo prohíbe y el árbol queda intacto.

---

**`Q-01` · MEDIO · `G-11b` no falla cerrado, y es la única comprobación dependiente de Git que
no lo hace.**
`docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` **L248–L261**.

```python
base = _base_raw.split("\n") if _base_raw is not None else []
...
for n in range(1, 87):
    ob = [l for l in base if l.startswith(f"| D{n} |")]
    ac = [l for l in lineas(DEC) if l.startswith(f"| D{n} |")]
    if ob and ac and ob[0] != ac[0]: difs.append(f"D{n}")
check("G-11b", "`D1`-`D86` conservan su texto (D67 restaurada al de 7e99388)",
      not difs, "ninguna difiere" if not difs else ...)
```

Sin `.git`, `base` queda vacía, `ob` siempre vacío, `difs` vacío, y la comprobación imprime
**`OK G-11b … ninguna difiere`**. Reproducido dos veces sobre copias: en `n1` (`.git` ausente +
`D12`, `D40`, `D80` reescritas) y en `r4` (`.git` ausente + `D67` reescrita). En `r4` la fila que
`G-11` existe para proteger había sido sustituida por `| D67 | FILA REESCRITA POR R4 |` y
`G-11b` declaró que **las ochenta y seis conservan su texto**.

Por qué importa: `M-12` corrigió `G-21`, `G-22` y `G-23`, y `G-11` lleva el guardián en su
predicado (`_base_raw is not None`). `G-11b` es el único que quedó fuera — y es el de mayor
alcance de los cinco. **Y una observación adicional**: `G-11` sí falla, pero su diagnóstico dice
«**DIFIERE**» cuando la causa real es que Git no responde. Falla cerrado sin explicar por qué.

¿Bloquea F5? **No por sí solo.** Debilita la garantía mecánica.

---

**`Q-02` · MEDIO · El ancla de posición no normaliza, y una referencia tipada legítima la
desplaza en silencio.**
Batería **L359**: `ancla = "VER" if "VER" in obl else (obl[-1] if obl else None)`.

`_base()` se aplica a las participaciones (L363–369) pero **no al paso del ancla**. El contrato
declara en `11-ARQUITECTURA-INTEGRADA.md` **L8856–8858**: «la capacidad BASE de un valor es el
segmento anterior al primer `:` … **Y ES TODA LA INFERENCIA QUE HAY**», y la vía 4 admite
expresamente `obligatorias[].capacidad_productora` tipada (L8852–8853).

Demostrado (`n2`): en `proceso:INC`, `capacidad_productora: "VER"` → `"VER:dosier"`. El ancla de
`INC` pasa de `VER` a `APR` —su última obligatoria, `aprendizaje-registrado`—, y `G-15` imprime
**verde**: «anclas sin VER `['AUD','INC','INV']`». El §6 de `G-15` sólo verifica que `AUD` esté en
esa lista y que ningún ancla sea `None`; nunca comprueba el recíproco.

Por qué importa: es el mecanismo exacto de `N-01` reintroducido por la puerta de al lado. `F6`
coloca `<CAP>:revision` **después del ancla**, y una referencia tipada a `VER` —forma que el
propio contrato bendice— la mueve sin que nada lo diga.

¿Bloquea F5? **No.** No obliga a `F6` a decidir arquitectura: la regla está escrita bien; lo que
falla es su implementación de referencia.

---

**`Q-03` · MENOR · La atribución de vía par a par que se publica no se contrasta contra nada.**
`11-ARQUITECTURA-INTEGRADA.md` **L8941**: «con `(DEP, SEG)` por la vía 2 y los otros ocho por la
vía 4».

`G-15` contrasta el **número** de procesos y de pares, y comprueba `_est[("DEP","SEG")] == 2` y
que exista al menos una vía 4. **No contrasta el reparto.** Demostrado (`n4`): convirtiendo los
condicionales de `FEA` a la forma desnuda, el reparto pasa a `[(2,1), (3,2), (4,6)]` y `G-15`
sigue **verde**; sólo cae `G-23`, lateralmente y porque se tocó un fichero del kernel.

¿Bloquea F5? **No.**

---

**`Q-04` · MEDIO · `G-22` y `G-23` son ciegos a las ADICIONES: un árbol con una segunda sede del
catálogo de procesos y un contrato que se declara contradictorio pasa 30/30 en verde.**
Batería **L752**: `_tocados_raw = _git("diff", "--name-only", "05f71b7")`.

`git diff --name-only` lista **modificaciones de ficheros rastreados**. No ve un fichero nuevo.
Demostrado (`n5`): añadí bajo `kernel/`

```
kernel/operativo/recorrido/01-PROCESOS-BIS.md   564 líneas, copia íntegra del catálogo
kernel/operativo/contratos/C8-SEGUNDA-SEDE.md   «redeclara la composición de ruta y
                                                 contradice a C4»
```

`git status --porcelain` los ve (`??`). `G-23` no. Resultado: **30/30 comprobaciones en verde**,
con la prosa del checkpoint —«el kernel operativo SUSTANTIVO no se ha tocado, y la excepción es
exacta y se nombra»— intacta y, formalmente, cierta.

Por qué importa: la **verdad duplicada** es exactamente lo que la disciplina de fuente única
prohíbe y lo que `SIS` existe para detectar. La comprobación que se ofrece como garantía de que
el kernel está intacto no cubre la forma más simple de romperlo.

¿Bloquea F5? **No por sí solo**, pero reabre la clase de `M-04`.

---

**`Q-05` · MEDIO · El derivado SÍ lee la prosa, contra la afirmación literal y absoluta del
contrato.**
`11-ARQUITECTURA-INTEGRADA.md` **L8860–8861**: «`capa_exigida`, `condicion`,
`criterio_de_satisfaccion` y `autoridad_de_retirada` **NO se leen**». `DECISIONES` L411, `D104`(ii),
lo repite con las mismas palabras.

El troceado real (batería L349–356) es una regex de línea sobre un corte de texto:
`re.findall(r"^\s*capacidad_productora:\s*(.+)$", seg_obl, re.M)`. **No hay YAML.** Cualquiera
de esos cuatro escalares de bloque puede inyectar una participación.

Demostrado (`n9`): escribí, dentro de la prosa de `criterio_de_satisfaccion` de
`FEA/intencion-definida`, la línea `capacidad_productora: "DOM"`. Ejecutando el propio
`_analizar()` del fichero:

```
ÁRBOL REAL              FEA part=[('DOM', 4), ('SEG', 4)]
N9 (prosa inyectada)    FEA part=[('DOM', 2), ('DOM', 4), ('SEG', 4)]
```

Se fabrica una participación OBLIGATORIA que no existe. Como la clave colisiona con una ya
presente, el recuento no cambia y **`G-15` queda verde**. En un proceso sin ese par el recuento sí
cambia, y entonces `G-15` falla **acusando a la proyección publicada** —«publica CINCO procesos y
el catálogo deriva 6»— en lugar de nombrar la línea malformada.

Por qué importa: `D98` fue insuficiente por barrido léxico, `D103` también, y `D104` se presenta
como «sin buscar una sola palabra en texto libre». Es cierto para el **criterio**; no lo es para
el **troceado** sobre el que el criterio opera.

¿Bloquea F5? **No.** `F6` tiene la regla; lo que falta es un lector estructurado.

---

**`Q-06` · MEDIO · La capa B conserva la dirección que `D105` invirtió, y es la circularidad de
`M-02`.**
`11-ARQUITECTURA-INTEGRADA.md` **L4360–4361**:

> «· TODO `abandonada` **DECLARA SU** `deriva`, y ese `deriva` existe en el diario y nombra las
> mismas rutas e items»

Contradicho, en la misma sección: **L4216** (`deriva_emitida` es campo **PROHIBIDO** en
`abandonada`, «era la referencia circular de `M-02`, y ahora el `deriva` referencia al
`abandonada` y no al revés»), **L4218** (`abandonada_id` en el `deriva`, «referencia UNILATERAL de
`D105`») y **L4406**, que reescribe la misma regla correctamente y añade: «**Invertido por
`D105`**: el sentido anterior exigía al `abandonada` un campo cuyo valor no podía existir cuando
se calculaba su propio `id`».

Por qué importa: L4360 es un **enunciado de regla de validación** de la capa B. Quien construya la
capa B a partir de esa línea implementa el puntero desde el `abandonada` — que es literalmente el
defecto que hacía **inemitible** el segundo terminal. Es el hallazgo más grave del expediente
reintroducido en la redacción de su propia corrección. Ninguna comprobación cubre este texto.

¿Bloquea F5? **No obliga a `F6` a decidir** —las celdas normativas y el reparto son inequívocos—,
pero es una **contradicción material viva y sin registrar**, que es la razón 5 del gate anterior.

---

**`Q-07` · MEDIO · §16 enumera DOCE presiones donde son TRECE, omite `PN-15`, y es la tercera
recurrencia de la misma frase.**
`11-ARQUITECTURA-INTEGRADA.md` **L7887**:

> «Las demás vigentes —**`PN-6` a `PN-14`**— son posteriores, y el total está abajo.»

Con las tres primeras: 3 + 9 = **DOCE**. El resumen de la misma sección, **L8447**, dice
`VIGENTES · TRECE`; §19 **L8687** dice, bien, «`PN-6` a `PN-15` nuevas»; y las cabeceras `## \`PN-`
derivan quince menos dos marcadas = trece.

Las dos líneas siguientes documentan que esta misma frase ya fue corregida **dos veces**: L7886
«Corregido por `m2`» y L7888–7889 «**Corregido por `I-11`**: decía «`PN-6` a `PN-12`»… y omitía
precisamente `PN-13`, la que va al Owner». Hoy omite **`PN-15`**, que es la que declara que
`G20`–`G23` de `KERNEL.md` siguen PRESIONADAS y **NO derogadas por F4** — otra vez, la que va al
Owner.

Invisible a las dos comprobaciones que existen para esto, y lo verifiqué en el código: `G-13` sólo
lee `^VIGENTES · <numeral>$` (L292); `G-26` c1 exige un numeral pegado a «presiones»/«VIGENTES ·»
(L1043–1047). **Un RANGO no es un numeral**, y ninguno de los dos patrones lo alcanza.

¿Bloquea F5? **No por sí solo.** Es material que llega al Owner con una presión de menos.

---

**`Q-08` · MEDIO · La «Siguiente acción exacta» del checkpoint —la sección a la que el propio
documento remite— está caducada dos tandas, sin marca de histórico, y lleva al Owner DOCE
presiones.**
`docs/evolucion/CHECKPOINT-ADS-NEXT.md` **L1978–2051**, y en particular **L2031**:

> «5  QUÉ LLEVAR AL OWNER            las **DOCE** presiones de §16, con `PN-1` bloqueando todo el…»

La cabecera del propio fichero, **L6**: «**Basta decir «Continúa»**: la siguiente acción exacta
está al final.» Es la única sección `## Siguiente acción exacta` del documento —lo verifiqué
listando todas las cabeceras— y dice, además: «**Ésta es la décima**» (L2010) y «un gate
independiente… **NO lo encarga esta tanda, y no está encargado**» (L1982). Desde entonces han
ocurrido el **GATE DEFINITIVO** (`D96`–`D102`), el **GATE DE COBERTURA Y CIERRE** (documento 20) y
la tanda vigente (`D104`–`D106`).

`grep` sobre L1978–2051: **cero marcas `HISTÓRICO`**. Y la asimetría es del propio corpus: el
bloque de la novena tanda sí lleva «**[HISTÓRICO]** ONCE vigentes en el momento de esta tanda»
(L1559), y el propio checkpoint declara la disciplina en L1570–1577 — «`PRESIONES` decía ONCE
donde hoy son TRECE. **Los dos bloques quedan marcados, y ninguno se borra**». Esa disciplina se
aplicó al bloque anterior y no a éste.

Y es reincidencia exacta: L2039 registra que este mismo punto ya fue corregido una vez —
«**Corregido por `I-28`**: este punto decía «las ONCE presiones de §16» y un Owner que siguiera
sólo esta línea no habría visto `F-08`». Hoy dice DOCE, y un Owner que siguiera sólo esta línea
no vería `PN-15`.

Reproduje la lógica de `G-26` c1 sobre el fichero del checkpoint: la línea L2031 sería marcada
FALLA («dice 12 y las cabeceras de §16 derivan 13»). **`G-26` no escanea el checkpoint**: su
`_sedes()` toma `t11` por defecto.

¿Bloquea F5? **No por sí solo.** Es el punto de entrada declarado del expediente, y es falso.

---

**`Q-09` · MENOR · El conjunto vigilado está escrito a mano, y el corpus lo declara de forma
derivable.**
Batería **L325**: `_VIGILADAS = ("DOM", "SEG")`.

En la línea inmediatamente anterior, `_CAPS` **sí** se deriva (`os.listdir(capacidades/)`), y el
comentario de la propia función presume de que «parte por pertenencia al conjunto de las quince».
Pero el conjunto que define de qué trata la comprobación entera es un literal. Y es derivable:
`grep -rn 'participa dos veces' kernel/operativo/capacidades/*/CAPACIDAD.md` devuelve
**exactamente dos líneas**, `DOM/CAPACIDAD.md:51` y `SEG/CAPACIDAD.md:51`.

Demostrado (`n8`): borradas esas dos líneas —el corpus deja de declarar en ninguna ficha que
`DOM` y `SEG` participen dos veces— `G-15` sigue **verde** afirmando los nueve pares. Sólo cae
`G-23`, lateralmente. `G-24` abre las quince fichas pero sólo comprueba que sean legibles.

Es la misma clase que el propio `G-13` declara haber retirado: «La versión anterior exigía
literalmente 14 cabeceras y 12 vigentes: **dos cifras escritas a mano en la comprobación que
existe para que las cifras no se escriban a mano**» (L277–278).

¿Bloquea F5? **No.**

---

**`Q-10` · MENOR · La regla por item trata como CONDICIONAL toda participación de vía 4, incluidas
las que vienen de `obligatorias`.**
Batería **L387–L392**:

```python
for cap, via in proceso_part:
    if via in (3, 4) and cap in condicionales_activos:
        out.add(cap)
```

La vía 4 se emite desde **las dos** secciones (`obligatorias` y `condicionales`, L365–369), y la
lista `part` no conserva de cuál vino. Verificado con fixture: un proceso dinámico con
`obligatorias[].capacidad_productora: "DOM:condiciones"` da

```
dinamicos: {'FX': [('DOM', 4)]}
_exige_item(propietario="PRD", condicionales activos=∅) -> set()
```

cuando la participación es **obligatoria** y debería exigirse siempre. Hoy es latente: ninguno de
los tres procesos dinámicos (`DEF`, `AUD`, `DIR`) lleva `DOM` ni `SEG` en `obligatorias`. Es la
misma situación que `O-01` denunció para la vía 1 —«no hay instancias hoy»— y que el gate anterior
consideró defecto de contrato, no excusa.

¿Bloquea F5? **No.**

---

**`Q-11` · MENOR · La derivación del ancla publicada atribuye a `proceso:INV` una obligatoria que
ese proceso no tiene.**
`11-ARQUITECTURA-INTEGRADA.md` **L8880–8881**:

> «`INV` `AUD` → tras su única obligatoria, `conclusion-fundada` de `INV`»

Derivado por mí de `01-PROCESOS.md`: la única obligatoria de `proceso:INV` es
**`evidencia-producida`** (`capacidad_productora: "INV"`); `conclusion-fundada` es la de
`proceso:AUD`. La línea nombra un id que en `INV` no existe. `G-15` §6 no contrasta esta lista: sólo
verifica que `AUD` esté entre los sin-`VER` y que ningún ancla sea `None`.

Sin consecuencia operativa hoy —L8956 declara que `INV` pasa vacío—, pero es una sede viva que el
árbol desmiente, de la clase de `M-05`/`M-06`/`M-07`.

¿Bloquea F5? **No.**

---

**`Q-12` · MENOR · «Cinco fixtures» no deriva de nada.**
`11-ARQUITECTURA-INTEGRADA.md` **L8985–8988**: «**cinco fixtures**, uno por vía y uno por proceso
dinámico… propietaria · obligatoria · condicional desnuda · item enlazado tipado · `AUD` con sus
cuatro combinaciones · `DIR` con propietario `DOM` y con propietario ajeno».

Cuatro vías + `AUD` + `DIR` = seis grupos; «uno por proceso dinámico» son tres (`DEF`, `AUD`,
`DIR`) → siete. Lo que `G-15` ejecuta, por su propio mensaje: «fixtures 1/2/3/4, AUD×5, DIR×2 y
negativo», más el del discriminante. **Cinco no sale por ninguna lectura**, en un bloque cuya regla
declarada es «la cifra no se escribe: se deriva». No hay comprobación que la contraste.

¿Bloquea F5? **No.**

---

**`Q-13` · MEDIO · La fila adversarial `X54` prescribe DIECISIETE ventanas y la tabla deriva
DIECIOCHO — falta precisamente `W17`, la que esta tanda creó.**
`11-ARQUITECTURA-INTEGRADA.md` **L1479**:

> «| `X54` | matar la máquina en cada una de las **diecisiete** ventanas con un `conflicto` vivo | …»

Derivado por mí: las filas `W` de §2.6.5 son **18** (`W1`…`W11`, `W12a`, `W12b`, `W13`…`W17`), y la
propia sección lo dice en **L1128**: «Se enumeran las **DIECIOCHO**, y el recuento **se deriva de las
filas de la tabla, no se escribe**». `D105`(v) creó `W17` en esta tanda, para la caída entre el
`abandonada` durable y el `deriva` durable — la ventana de `M-03` y `O-03`.

Por qué importa: `X54` no es prosa descriptiva, es **la especificación de una prueba adversarial**.
Quien la construya desde esa línea ejercitará diecisiete ventanas y saltará una — y la que salta
es exactamente la que esta tanda añadió para cerrar dos GRAVES. Es la única sede con la cifra
vieja, y ninguna comprobación cuenta ventanas: los cuatro patrones de `G-26` 26.b hablan de filas
adversariales, no de ventanas.

¿Bloquea F5? **No por sí solo.** Es una sede viva que el árbol desmiente, y con consecuencia
práctica para `F6`.

---

**`Q-14` · MEDIO · En el registro reanudable, `C-L.3` queda a la vez CORREGIDA por `D103` —con la
regla que `M-01` refutó— y NO CERRADA, y `D104` no aparece en ninguna de las dos.**
`docs/evolucion/CHECKPOINT-ADS-NEXT.md` **L994**, **L1011–1021** y **L1065**.

- L98 y L994: «CORREGIDAS EN F4c **8** … `C-L.3` …»
- L1011–1020, fila de detalle: «`C-L.3` **CERRADA** · `D98` reformuló… y **`D103` la corrigió
  después**… POR ITEM para `AUD`, que exige `DOM:revision`, `SEG:revision` o NINGUNA según su
  propietario derivado — **cero o un par, nunca dos**.»
- L1065: «NO CERRADA  1  `C-L.3`  ← una de las cinco que bloquean»

La frase «**cero o un par, nunca dos**» es precisamente lo que `M-01` refutó y lo que `D104`
sustituyó: `11-ARQUITECTURA-INTEGRADA.md` **L8953** dice «`AUD` propietario `PRD` con `C-DOM` y
`C-SEG` activos → **`{DOM, SEG}`**», y `G-15` lo ejercita en cada corrida. Un `grep` de `C-L.3`
sobre el checkpoint entero devuelve **cero menciones de `D104`**: el registro no dice en ninguna
parte que la condición que toda la tanda existe para cerrar haya vuelto a cerrarse, ni con qué
regla.

`G-16` pasa verde porque comprueba **coherencia entre el resumen y su fila de detalle**, no
vigencia: las dos dicen `CERRADA`, y con eso basta.

Por qué importa: `C-L.3` es la condición de cierre que tres tandas seguidas han intentado cerrar.
En el documento que el sistema declara «registro persistente y reanudable», su estado es
contradictorio y su descripción es la regla derogada.

¿Bloquea F5? **No por sí solo**, y es la más significativa de mis contradicciones sin registrar.

---

**`Q-15` · MENOR · Dos residuos.**
- **Código muerto**, uno solo, encontrado con barrido AST sobre las 216 definiciones del fichero:
  `ancho = max(len(t) for _, t, _, _ in RES)` en la batería **L1102**, calculado y nunca usado.
  Es el único; todo lo demás está vivo, y `M-11` está efectivamente retirado.
- **Errata**, `11-ARQUITECTURA-INTEGRADA.md` **L4350–4351**: «que todo `confirmada` tenga su
  `preparada`, **toda todo** `abandonada` su `conflicto`».

¿Bloquea F5? **No.** Se registran por completitud, porque el listón incluía «no sobrevive código
muerto» y la respuesta honesta es «casi».

---

```text
RECUENTO DE MIS HALLAZGOS, derivado de las quince fichas de arriba
  BLOQUEANTE   0
  GRAVE        0
  MEDIO        8   Q-01 Q-02 Q-04 Q-05 Q-06 Q-07 Q-08 Q-13 Q-14   → son NUEVE
  MENOR        7   Q-03 Q-09 Q-10 Q-11 Q-12 Q-15                  → son SEIS
                  ──
                  15
```

Rectifico el recuento en el propio dictamen, derivándolo otra vez de las filas y no de mi
borrador: **MEDIO 9** (`Q-01` `Q-02` `Q-04` `Q-05` `Q-06` `Q-07` `Q-08` `Q-13` `Q-14`) ·
**MENOR 6** (`Q-03` `Q-09` `Q-10` `Q-11` `Q-12` `Q-15`) · **total 15** · **GRAVE 0** ·
**BLOQUEANTE 0**.

---

#### 10 · Proporcionalidad

Digo primero lo que esta candidata hace bien, porque es mucho y porque el veredicto sería
deshonesto sin ello.

- **`D104` es la primera de las cuatro formulaciones que no deja a `F6` nada que decidir.** Lo
  derivé por mi cuenta antes de leerla y coincidimos exactamente. Las cuatro causas que la
  gestaron están cerradas con fixture ejecutable.
- **Las cuatro refutaciones prescritas fallan hoy, y en tres de los cuatro casos falla la
  comprobación responsable con un diagnóstico que deriva la causa.** `R2` y `R3` fallan solas.
- **`M-11` no era decorativo y ahora dispara**; **la vía 3 y la regla por item de `AUD` son código
  vivo**; **la excepción de seis ficheros del kernel se deriva de Git y se contrasta contra la
  prosa**; **`G-11`, `G-21`, `G-22` y `G-23` fallan cerrado**; **no hay ningún literal
  `_COMPONENTES_CL13`**; **el mensaje de `G-16` deriva su censo**. Seis de los siete puntos del
  listón mecánico, cumplidos.
- **Diecisiete de los veintiún hallazgos del gate anterior están efectivamente superados**, y los
  cuatro restantes están registrados, contratados o fuera de mi lote, con estado único.
- **La cobertura se cerró en mi lote**: 31 fuentes de 31, íntegras, con manifiesto y SHA-256
  recalculados. Y la lectura sirvió: los BLOQUES B y C de `ADS-PENDIENTES` confirman a F4, y `N-05`
  quedó verificado en su mitad abrible.
- **Ninguno de mis quince hallazgos es GRAVE o BLOQUEANTE, y ninguno obliga a `F6` a inventar
  arquitectura.**

Y digo también dónde no llega, sin inflarlo. Mis quince hallazgos son de **dos familias**, y las
dos son exactamente las que el documento 20 usó como razones 4 y 5:

1. **Sedes vigentes que el árbol desmiente, sin registrar: seis.** `Q-06` (la capa B conserva la
   dirección que `D105` invirtió), `Q-07` (doce presiones donde son trece), `Q-08` (el punto de
   entrada del checkpoint, caducado dos tandas), `Q-11` (un ancla que no existe), `Q-13` (`X54`
   prescribe una ventana de menos), `Q-14` (`C-L.3` CORREGIDA y NO CERRADA a la vez, sin `D104`).
   El gate anterior falló a esta cadena con **tres**, todas MEDIO, y declaró que cada una bastaba.
2. **La garantía mecánica, refutada de nuevo: dos árboles defectuosos sin ningún fallo
   responsable.** `Q-04` da 30/30 sobre un árbol con una segunda sede de `01-PROCESOS.md` y un
   `C8` que se declara contradictorio con `C4`. `Q-05` fabrica una participación desde la prosa
   y deja `G-15` verde.

Y hay un dato que no puedo pasar por alto en la proporción: **`Q-07` y `Q-08` son la tercera
recurrencia de la misma frase**, corregida ya por `m2`, por `I-11` y por `I-28`; y las tres veces
lo omitido ha sido **la presión que va al Owner** (`PN-13`, `F-08`, ahora `PN-15`). El adjudicador
`O` lo escribió así: «no falla por concepción. Falla, por duodécima vez, porque una decisión bien
tomada llega a la mitad de los sitios que la invocan». **Eso es exactamente lo que he encontrado
otra vez**, y esta vez en la tanda que venía a cerrarlo.

---

#### 11 · Límites de este dictamen

1. **No he visto el dictamen de `P`**, ni ningún otro. Nada de lo anterior está coordinado.
2. **Mi lote son 31 fuentes de las 43 obligatorias.** No he leído `(a)`, `(b)`, `E1`, `E2`,
   `C1`–`C7`, `KERNEL.md`, `diseno/*`, `circuitos/*`, `docs/owner/*` ni los documentos 12, 13, 14,
   15 y 19. Cuando un hallazgo del gate anterior cae ahí (`N-03`), lo he declarado **NO
   APLICABLE** en vez de presumir.
3. **No he ejecutado nada del protocolo transaccional**, porque no existe: no hay runtime, ni
   esquema de `evento`, ni un fichero bajo `estado/`. Mi juicio sobre §2.6 es de coherencia de
   texto contra texto, igual que el de la batería, y lo digo con sus mismas palabras.
4. **`C-L.5` no la cierro yo.** Publico mi manifiesto de lectura y mi cruce; cerrarla exige el
   cruce de los manifiestos de **todos** los revisores contra el de asignación, y eso corresponde
   al adjudicador.
5. **La derivación de `<CAP>:revision` la hice con el mismo intérprete que la batería.** Coincide
   con mi derivación manual, pero un error compartido entre mi lectura y su código no lo habría
   visto ninguno de los dos.
6. **Todos mis experimentos son copias completas en `/tmp/q-gate/`.** El repositorio no fue
   escrito en ningún momento: `git status --porcelain` vacío al abrir, tras ejecutar la batería, y
   al cerrar.

---

#### 12 · RECOMENDACIÓN DE VEREDICTO

La cobertura de mi lote está completa —`ASIGNADAS − LEÍDAS ÍNTEGRAMENTE = ∅`—, de modo que
**no procede** `INSUFICIENTE PARA F5 POR COBERTURA`. Mi recomendación se emite sobre el fondo.

### INSUFICIENTE PARA F5

**Por cuatro razones numeradas. Ninguna es la ausencia de runtime, de piloto, de adaptadores
certificados o de PesquerApp: comprobé que están bien declaradas y no las cuento.**

**1. La condición «ninguna contradicción material sin registrar» no se cumple, y con más sedes
que la vez anterior.** Encontré **seis sedes vigentes que el árbol desmiente y que nadie ha
registrado**: `Q-06`, `Q-07`, `Q-08`, `Q-11`, `Q-13` y `Q-14`. El gate anterior declaró
INSUFICIENTE con **tres** de esta misma clase y severidad —`M-05`, `M-06`, `M-07`— diciendo que
cada una bastaba por sí sola. Aplico el mismo criterio, y no tengo motivo para rebajarlo en la
tanda que vino a satisfacerlo.

**2. La garantía mecánica del entregable vuelve a estar refutada, con árboles nuevos.** `Q-04`:
un árbol con una **segunda sede completa del catálogo de procesos** y un contrato `C8` que se
declara contradictorio con `C4`, ambos bajo `kernel/`, pasa **30/30 en verde**. `Q-05`: una
participación fabricada desde la prosa de un escalar de bloque deja `G-15` verde y contradice la
afirmación literal y absoluta del contrato de `D104`. Es la razón 4 del documento 20,
reproducible con contraejemplos que `M-04` no usó.

**3. Dos de los defectos son la tercera recurrencia de la misma frase, y las tres veces lo
omitido es lo que va al Owner.** `Q-07` (§16 dice `PN-6` a `PN-14`, doce donde son trece, y omite
`PN-15`) y `Q-08` (la «Siguiente acción exacta» del checkpoint, el punto de entrada que el propio
documento declara, caducada dos tandas y llevando DOCE presiones al Owner). Esa frase ya fue
corregida por `m2`, por `I-11` y por `I-28`. Ninguna de las dos comprobaciones que existen para
esto —`G-13` y `G-26` c1— puede verla, porque son rangos y no numerales, y porque `G-26` no
escanea el checkpoint.

**4. La condición que toda la tanda existe para cerrar no consta cerrada en el registro
reanudable.** `Q-14`: `C-L.3` figura simultáneamente como «CORREGIDA EN F4c» —descrita con la
regla de `D103` que `M-01` refutó, «cero o un par, nunca dos»— y como «NO CERRADA», y `D104` no
aparece en ninguna de las dos. `G-16` pasa verde porque comprueba coherencia interna, no vigencia.

---

**Y lo que quiero que no se lea de menos, porque es la mitad honesta del juicio:**

**`D104` supera su listón.** Lo derivé por mi cuenta antes de leerlo y coincidimos exactamente:
siete estáticos, tres por item, cinco procesos, nueve pares, `(DEP,SEG)` por la obligatoria,
anclas sin `VER` en `AUD` e `INV`, las cuatro combinaciones de `AUD` alcanzables, `DIR` por la
misma regla sin excepción escrita, ningún décimo par. Las cuatro vías operan, la propietaria no es
decorativa —lo probé construyendo un par nuevo—, los condicionales de `AUD` se evalúan contra el
árbol —lo probé borrándolos—, y **`F6` no necesita elegir arquitectura**. Intenté refutarlo por
nueve caminos y no cayó por ninguno. **La cuarta formulación es la buena.**

Lo que falla no es la decisión: es, otra vez, que llega a la mitad de los sitios que la invocan,
y que la comprobación que debía impedirlo tiene aún dos puertas abiertas. **Mis quince hallazgos
son MEDIOS y MENORES, ninguno GRAVE ni BLOQUEANTE, y todos se cierran propagando material que el
corpus ya tiene escrito** — ninguno exige decidir diseño. Con esas seis sedes reconciliadas, con
`G-11b` fallando cerrado, con `G-23` mirando también las adiciones y con un lector estructurado en
lugar de una regex de línea, esta candidata pasa.

Pero no le corresponde pasar a quien la aplica, y hoy, con el criterio que el gate anterior fijó
y que esta tanda vino a satisfacer, **no pasa**.

```text
ÁRBOL AL CERRAR   git status --porcelain  →  vacío
HEAD              18cbfb57fe2286bb68011a31a8f3d07556d7aea9
ÁRBOL             6e9d662d6cc8ff6e289c391490e70285c8a41e9e
EXPERIMENTOS      /tmp/q-gate/{base,n1..n9,q08,r1..r4} — 342 MB, todos fuera del repositorio
FICHEROS DEL REPOSITORIO MODIFICADOS   ninguno
COMMITS · PUSH                          ninguno
```

**`F4c` sigue ABIERTA. `F5` NO queda autorizada por mi parte.**

---

## 7 · Adjudicación literal del ADJUDICADOR R

> Se transcribe **íntegra y sin cambiar una palabra**, con los encabezados rebajados dos niveles.
> Se retira únicamente la línea con que el agente devolvió el documento —«Verification complete.
> Tree clean at open and close, `HEAD` unchanged.»—, que es una comprobación de modo, no parte de
> la adjudicación, y cuyo contenido se verifica de nuevo en la sección 14.
>
> `R` recibió los dos dictámenes **ya cerrados**, junto con las verificaciones del coordinador y
> su corrección a `P`. No resolvió por mayoría.

### DICTAMEN DEL ADJUDICADOR `R`

#### GATE INDEPENDIENTE DE CIERRE DE `F4c`

> ## VEREDICTO: `INSUFICIENTE PARA F5`
>
> **`F4c` sigue ABIERTA. `F5` NO queda autorizada. No se corrige nada.**
>
> Y lo digo por delante: **NO falla por cobertura, NO falla por los cuatro bloqueantes anteriores, y NO falla por `D105`.** Falla por dos condiciones de las siete, y las nombro en §11.

---

#### 1 · Procedencia, modo y método

```text
REPOSITORIO   /home/jose/ads-kernel
RAMA          gate/f4c-cierre-con-manifiestos-20260829
HEAD          18cbfb57fe2286bb68011a31a8f3d07556d7aea9
ÁRBOL DE HEAD 6e9d662d6cc8ff6e289c391490e70285c8a41e9e
COMMIT JUZGADO 7764cca69c9fbb7c3e89b70efdae7d6990f6c3b6
ÁRBOL JUZGADO 03116b33bf4d8e996d8eccae51db927f4667ca58   ← verificado con git rev-parse
MODO          SÓLO LECTURA. `git status --porcelain` VACÍO al abrir y al cerrar.
              HEAD idéntico en los dos extremos. Cero commits, cero escrituras de git.
              Todos los experimentos en copias bajo /tmp, sobre `git archive` del HEAD.
```

**Corrijo al encargo en un punto de hecho, y consta.** El encargo da `03116b33…` como «TREE» junto a `HEAD 18cbfb5…`. Son de commits distintos: `03116b33` es el árbol del **candidato** `7764cca`; el árbol de `HEAD` es `6e9d662`. Lo verifiqué con `git rev-parse` sobre los dos. **La declaración de `P` es correcta y la confirmo:** `HEAD` no es el candidato, y `git diff --stat 7764cca..18cbfb5` da **1 fichero, 140 inserciones**, que es el propio manifiesto. El objeto normativo juzgado es idéntico en los dos.

**Qué NO soy.** No escribí `F4`, `F4b` ni `F4c`. No apliqué `D16`–`D106`. No soy autor de ninguna corrección. No fui revisor `A`–`Q`. Recibí los dos dictámenes ya cerrados.

**Cómo he trabajado.** No resuelvo por mayoría. **Cada afirmación material de `P` y de `Q` que sostiene una conclusión la abrí en su fichero y su línea**, y los hallazgos bloqueantes los reproduje yo mismo en copias de `/tmp`. **Rechazo expresamente lo que no se sostiene**, y el rechazo más consecuente de este dictamen cae sobre la primera razón de veredicto de `P`.

---

#### 2 · Mi manifiesto de lectura

**Nueve fuentes asignadas. Nueve leídas ÍNTEGRAS. 21 732 líneas.** Método: `awk`/`sed` por tramos consecutivos que cubren todas las líneas, sin saltos y sin sustituir lectura por `grep`.

| ruta | líneas | SHA-256 (16) recalculado | lectura |
|---|---|---|---|
| `docs/evolucion/ADS-PENDIENTES-…md` | 2163 | `a88609167dbbea28` | **ÍNTEGRA**, BLOQUES B y C incluidos |
| `docs/evolucion/16-GATE-FINAL-…md` | 1257 | `8243034f286160cc` | **ÍNTEGRA** |
| `docs/evolucion/17-COMPLEMENTO-…md` | 1650 | `18f876d4cd47a2f7` | **ÍNTEGRA** |
| `docs/evolucion/18-GATE-DE-CIERRE-…md` | 3665 | `1e71366b10d22938` | **ÍNTEGRA** |
| `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 9280 | `84063c2a344a2d15` | **ÍNTEGRA** |
| `docs/evolucion/20-GATE-INDEPENDIENTE-…md` | 801 | `d7d2e4fa3f878e0c` | **ÍNTEGRA** |
| `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 725 | `3be45994f4d00e82` | **ÍNTEGRA** |
| `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 2051 | `76ed2d768cdb4db8` | **ÍNTEGRA** |
| `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-…md` | 140 | `c843b0c341183859` | **ÍNTEGRA** |

**Dos anclas por fuente, de regiones separadas:**

- **`ADS-PENDIENTES`** — L169 «*Principio aceptado: ADS debe distribuirse preestructurado*» · L1416 «*Lo que se encuentra una vez se corrige; lo que puede repetirse se convierte… en regla, componente, test, validador, skill o gate*»
- **Doc 16** — L120 «*`awk 'NR>=1244 && NR<=1350'` … → 42 filas*» · L1257 «*El patrón que A describe —«decisiones bien tomadas y aplicadas a la mitad de los sitios que las invocan»*»
- **Doc 17** — L45 «*se cubrieron las diecinueve: cubrir de más cierra la ambigüedad*» · L1638 «*En la tensión entre `C5` L36 y `00-CIRCUITOS` L238 manda `00-CIRCUITOS`*»
- **Doc 18** — L79 «*Lo único que exige una decisión de diseño nueva … es el plano de `estado/cuarentena/<TX>/`, y son cinco líneas*» · L3546 «*NO HE RESUELTO `I-08` CONTRA `b.3` NI `b.5`, que nadie abrió*»
- **Doc 11** — L961–968 (paso 0, la guarda de `W17`) · L9016 «*Los censos escritos a mano, derivados*»
- **Doc 20** — L372 «*Lo que mi cobertura sí cierra: las catorce fuentes del `C-0.1` … incluido el documento 15*» · L777 «*falla porque una decisión bien tomada llega a la mitad de los sitios que la invocan*»
- **`DECISIONES`** — L411 (`D104`, las cuatro vías tipadas) · L534–541 (el addendum de cronología de `O16`)
- **`CHECKPOINT`** — L16–28 (los 21 en cuatro estados) · L1661 «*RECUENTO DERIVADO DE LAS 43 FILAS, no al revés*»
- **Manifiesto** — L121 «*CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA*» · L140 «*Con este manifiesto, esa resta es calculable por primera vez*»

---

#### 3 · El cruce asignación contra lectura, y las pendientes derivadas

**Verifiqué las 43 filas del manifiesto, no sólo las mías.** Recalculé `wc -l` y `sha256sum` de las cuarenta y tres rutas contra el árbol:

```text
FILAS DEL MANIFIESTO                43
COINCIDEN líneas Y SHA-256          43   ← todas, sin una sola discrepancia
FICHEROS AUSENTES DEL ÁRBOL          0
```

**La resta, revisor a revisor:**

| | asignadas | leídas íntegras | **asignadas − leídas** |
|---|---|---|---|
| `P` | 20 (8 comunes + 12) | 20 | **∅** |
| `Q` | 31 (8 comunes + 23) | 31 | **∅** |
| `R` | 8 comunes + el manifiesto = 9 | 9 | **∅** |
| | **43 fuentes · 59 asignaciones** | | **∅** |

> **La regla de cierre de `C-L.5` se cumple, y es la PRIMERA VEZ en el expediente que es CALCULABLE.** No la presumo en ninguna de las dos direcciones: la calculé.

**Fuentes que necesité y NO estaban asignadas: NINGUNA.** Lo digo porque el encargo obliga a declararlo. Toda discrepancia material entre `P` y `Q` se resolvió dentro de las ocho comunes, del código de la batería —que `Q` tenía asignado y yo abrí como objeto para reproducir— y de `01-PROCESOS.md`, abierto igualmente como objeto de reproducción, nunca como fuente de juicio propio. **No pido ADDENDUM.**

---

#### 4 · Qué verifiqué yo y qué acepté

**Verificado por mí, contra fichero y línea o reproducido en `/tmp`:** el árbol y el rango · los 43 SHA-256 del manifiesto · el recuento de ventanas (18 filas `W1`–`W17`) · `X54` L1479 · las 46 filas `X` de §2.6.7 y las 8 de §15.5 · que **ninguna fila `X` menciona `W17`** · §2.6.9 puntos 1–8 y la tabla de tres alternativas de `D105` · §2.6.4 paso 0 completo · la lista de `fsync` con su punto (5) · §2.8 punto 4 · §3.6 filas `abandonada` y `deriva` · la capa B entera y la tabla de las cuatro reglas (L4406) · `CHECKPOINT` L994/L1011/L1065/L1142/L1641/L1911–1942/L1978–2051 · §16 L7887 · §19 L8447/L8687 · el bloque de evidencia de `PN-15` y su PRUEBA POSTERIOR corregida · `D104`–`D106` íntegras · el addendum de `O16` con sus dos fechas en `git log` · **las cuatro refutaciones `R1`–`R4`, reproducidas una a una** · `Q-01`, `Q-02`, `Q-03`, `Q-04`, `Q-05`, `Q-09`, `Q-11`, `Q-12`, `Q-15` reproducidos · el control positivo de `M-11` · las cuatro combinaciones de `AUD` derivadas con el propio código · los recuentos de `timebox`/`G20`–`G23` en doc 11, (a), (b) y `E2` · `grep 'G2[0-3]'` sobre (a) · `git diff --numstat` sobre el registro.

**Aceptado sin verificación independiente, y lo digo:** la lectura íntegra que `P` y `Q` declaran de sus lotes propios —no la rehíce, y sus dos manifiestos son internamente consistentes— · la derivación a ciegas de `<CAP>:revision` que `Q` hizo antes de leer lo publicado · los recuentos de doc 16, 17 y 18 sobre fuentes fuera de mi lote · la reproducción de `A14` por entorno.

**Lo que NO juzgo, por instrucción y porque está bien declarado:** ausencia de runtime, de piloto, de adaptadores certificados y de adopción de PesquerApp. Comprobé que están declaradas con propietario y fase, y **no las uso como motivo de insuficiencia en ninguna de mis razones.**

---

#### 5 · Adjudicación de `P-01`–`P-08`

| id | mi adjudicación | severidad final |
|---|---|---|
| `P-01` | **CONFIRMADO**, con la retórica regraduada | **MEDIO** |
| `P-02` | **CONFIRMADO Y AGRAVADO** | **MEDIO** |
| `P-03` | **RECHAZADO en su tesis bloqueante**, sobrevive un residuo | **MENOR** |
| `P-04` | **CONFIRMADO Y AGRAVADO** | **MEDIO** |
| `P-05` | **CONFIRMADO Y AGRAVADO** | **GRAVE** |
| `P-06` | **CONFIRMADO** | **MEDIO** |
| `P-07` | **CONFIRMADO** | **MENOR** |
| `P-08` | **REGRADUADO**: su premisa de hecho es FALSA; sobrevive su mitad formal | **MENOR** |

##### `P-01` · CONFIRMADO en el hecho · MEDIO

**El hecho es exacto y lo derivé yo.** §2.6.5 L1128 declara «**DIECIOCHO**» y el recuento «se deriva de las filas»; conté las filas: `W1`–`W11` + `W12a` + `W12b` + `W13`–`W17` = **18**. `X54` L1479 dice «matar la máquina en cada una de las **diecisiete** ventanas». Y **ninguna de las 46 filas `X` de §2.6.7 menciona `W17`**: `grep -P '^\| \`X[0-9]+\`' | grep -P 'W1[0-8]'` devuelve **vacío**.

**Regraduo dos cosas de la formulación de `P`:**

1. **«Tercera vez» es inexacto.** L1269 y L1436 documentan **el mismo episodio** —la segunda devolución independiente / `D36`, que encontró que ninguna de las diecisiete originales detectaba una caída de máquina—, en dos sedes. Es la **segunda** vez, no la tercera.
2. **«Lo que no tiene fila, no se prueba» es una inferencia de política, no una necesidad textual.** `W17` está especificada íntegra en L1163 y en §2.6.9 punto 8; F6 puede escribir su prueba desde ahí sin decidir nada.

**Lo que sobrevive, y es lo que cuenta:** una **contradicción material vigente y sin registrar** entre dos sedes del mismo documento, en la tabla que se autodeclara «convertible en pruebas de F6 **sin traducción**», y cuyo efecto es que la ventana creada para cerrar `M-03` y `O-03` queda fuera del escenario que la nombraría. **Corrección: una palabra.**

##### `P-02` ≡ `Q-06` · CONFIRMADO Y AGRAVADO · MEDIO

`11-ARQ:4360`, capa B: «TODO `abandonada` **DECLARA SU** `deriva`». Es el verbo previo a `D105`, que **invirtió la referencia**: §3.6 L4217 declara `deriva_emitida` **PROHIBIDO** en `abandonada`, y L4219 da al `deriva` el `abandonada_id` como «referencia UNILATERAL de `D105`».

**Lo agravo, y es mío.** El defecto no es sólo el verbo. **§2.6.9 L1940–1941 afirma una alineación que la capa B no entrega:** dice que «la capa B exige *exactamente un `deriva` que referencie por `abandonada_id`*», y **la lista de la capa B no dice eso en ninguna línea** — lo dice la **tabla de las cuatro reglas**, en L4406, que sí está correcta y lleva su «**Invertido por `D105`**». Es decir: la sede que §2.6.9 invoca por su nombre («la capa B») contiene el enunciado viejo, y el enunciado nuevo vive en otra tabla 46 líneas más abajo. Quien construya la capa B desde su propia lista implementa el puntero desde el `abandonada` — literalmente el defecto que hacía inemitible el segundo terminal.

Agrava, como señalan los dos revisores, que esa lista **acababa de ser barrida por `D89`** y que declara en L4335–4338 que «ninguna regla de esta lista vuelve a escribir la condición con otras palabras» —aunque esa cláusula está acotada a `abierta(tx)`, y lo digo para no inflar la cita.

##### `P-03` · **RECHAZADO en su tesis bloqueante** · sobrevive un residuo MENOR

**Éste es el rechazo más consecuente de este dictamen, y por eso lo argumento entero.**

`P` sostiene que la idempotencia de `W17` descansa en una regla de **una sola sede** que **dos sedes canónicas contradicen**, que **dos arranques emiten dos `deriva`**, que se **viola la regla 3 de la capa B**, que **el diario queda no conforme por su propio validador**, y que **F6 no puede materializar el evento sin decidir cuál de tres frases manda**. Abrí las cinco sedes y **cuatro de las cinco afirmaciones son falsas**.

**1 · «En una sola sede» es falso.** `predecesor = id(abandonada)` aparece **tres veces** en §2.6.9: L1884 (la nota de `D105`), L1894 (la fila A de la tabla de alternativas, que lo usa como premisa del descarte) y L1918 (el punto 4). Y la regla de unicidad que `P` da por ausente está escrita, con su nombre y su motivo, en **L4406**: «*ninguna `abandonada` sin **EXACTAMENTE UN** `deriva` que la referencie por `abandonada_id`* … **Invertido por `D105`**».

**2 · «Dos arranques emiten dos `deriva`» es falso, y lo desmiente el paso 0.** §2.6.4 L956–968, que `P` cita en otra parte de su dictamen, comprueba **antes de emitir**:

> «· existe un `deriva` con `abandonada_id` = ese `abandonada` → **nada que hacer. NO se emite otro** · **NO existe** → se COMPLETA»

La idempotencia operativa **no descansa en la igualdad de `id`**: descansa en una **guarda de existencia por `abandonada_id`**, que es un tercer mecanismo distinto de `tx` y de `id`. Con esa guarda, dos arranques no pueden producir dos eventos, **cualquiera que sea el `predecesor`**.

**3 · «Se viola la regla 3 de la capa B» y «el diario queda no conforme» son falsos**, por lo mismo: la guarda del paso 0 hace cumplir exactamente la regla de L4406, que es la que `P` cree violada.

**4 · «La fila del `deriva` en §3.6 no menciona `predecesor`: cero apariciones» es cierto pero irrelevante.** `predecesor` es **campo COMÚN a todo evento** (§3.6 L3774, bloque «Campos comunes»), no campo por tipo. **Ninguna** de las siete filas del contrato condicional lo menciona, ni la del `deriva` ni la de `preparada`. Un campo común ausente de una fila de campos específicos no es un silencio: es la estructura de la tabla.

**5 · «F6 no puede materializar sin decidir cuál de tres frases manda» es falso.** §2.6.9 punto 4 es explícito, inequívoco y está en la sede del procedimiento de emisión. F6 materializa desde ahí.

**Qué SÍ sobrevive, y lo registro como residuo MENOR mío.** La **justificación** que el documento escribe tres veces —L961–966, L1163 y L1934–1936: «*el cuerpo del `deriva` es una FUNCIÓN del `abandonada`, luego dos arranques producen el MISMO evento direccionado por contenido*»— es **redundante y sobre-alcanza**. §2.8 L2930–2939 retiró expresamente el razonamiento por identidad de contenido («**REEMITIR NO ES IDEMPOTENTE POR `id`** … la idempotencia vive sobre `tx`, no sobre `id`»), y el `deriva` **no tiene `tx`** (PROHIBIDO, L1911 y L4219). El documento se apoya en una prueba que él mismo retiró, para una propiedad que ya tiene garantizada por otro camino. **Sobra una frase; no falta una decisión.** La corrección es retirar la justificación o declararla excepción de §2.8, y en ningún caso bloquea.

> **Y digo lo que esto significa para el veredicto:** la **primera razón** del veredicto de `P` cae. `D105` no deja el segundo terminal inconstruible; lo deja construible, guardado y verificado.

##### `P-04` · CONFIRMADO Y AGRAVADO · MEDIO

`CHECKPOINT` L1142 cuenta «las **9 ventanas `RC-1`–`RC-9`** de §2.6.9» dentro de NADA PROBADO. `11-ARQ:8672–8674` dice lo contrario con todas las letras: «**Las nueve ventanas de reconciliación NO se cuentan: `D64` las retiró** … contarlas era inflar el inventario con algo inexistente». Y omite las **ocho comprobaciones `X-A`–`X-H`** que doc 11 sí cuenta (`grep 'X-A'` sobre el checkpoint: **2 apariciones**, ninguna en ese inventario).

**Lo agravo con una sede que `P` no cita:** el propio checkpoint, **L1641**, declara `M-8` `CORREGIDO_EN_F4` por `D83` con el motivo «`RC-1`–`RC-9` renombradas y **retiradas del inventario de §19**». El fichero declara aplicada una corrección **y conserva en su propio inventario exactamente lo que esa corrección retiró**, quinientas líneas más arriba.

##### `P-05` ≡ `Q-08` · CONFIRMADO Y AGRAVADO · GRAVE

La sección `## Siguiente acción exacta` (L1978–2051) es la que la cabecera L6 designa como punto de entrada: «**Basta decir «Continúa»**: la siguiente acción exacta está al final». **No lleva marca de histórica** —`grep 'HISTÓRICO'` sobre L1978–2051 devuelve **cero**, mientras el bloque de la novena tanda sí la lleva (L1553, L1559)—, y está congelada **dos tandas atrás**. Confirmo los tres puntos de `P` y **añado dos que ni `P` ni `Q` registran**:

```text
PUNTO 0  «NO lo encarga esta tanda, y no está encargado»   ← el gate se encargó y produjo D96–D106
PUNTO 1  «los 28 hallazgos I-01–I-28»                       ← son los del gate ANTERIOR al anterior
PUNTO 2  «Ésta es la décima»                    ← MÍO. Van dos tandas más
PUNTO 3  «la excepción es exacta y se nombra:»  ← MÍO, y es el más serio: enumera TRES ficheros
         + tres rutas                              (comprobar_negativos.py · .upstream-hash ·
                                                   pruebas/evidencia/*) donde L1911-1942 deriva SEIS
                                                   de Git y los enumera uno a uno. Es `M-06`
                                                   REPRODUCIDO en la sede de entrada, en la misma
                                                   tanda que declara `M-06` corregido
PUNTO 5  «las DOCE presiones de §16»            ← el derivado da TRECE (L979 y L1233 lo dicen bien)
```

**Y es la segunda vez seguida sobre esta misma línea:** L2038–2040 registra «**Corregido por `I-28`**: este punto decía «las ONCE presiones de §16»».

**Por qué lo gradúo GRAVE y no MEDIO.** No es un recuento cualquiera en un fichero cualquiera. Es **el único punto del corpus que se autodesigna como entrada para un agente sin contexto**, contiene **cinco afirmaciones falsas simultáneas**, una de ellas es un defecto que esta misma tanda declara corregido, y su línea de presiones va **al Owner**. Un agente que ejecute «Continúa» sobre este fichero encarga un gate ya encargado, corrige 28 hallazgos ya corregidos y lleva al Owner doce presiones de trece.

##### `P-06` · CONFIRMADO · MEDIO

`11-ARQ:8357–8360`. Los recuentos, derivados por mí:

```text
                doc 11   (a)   (b)   E2
timebox            8      1     0     0
G20               13      0     0     0
G21               11      0     0     0
G22               17      1     0     0     ← el bloque dice «UNA», y en (a) ES una
G23               14      0     0     0
```

**La parte acotada del enunciado es EXACTA** —en (a), (b) y `E2` la afirmación se cumple al pie de la letra—; **la parte sobre «el documento 11» es falsa**. Y confirmo la causa que `P` señala: de las 55 apariciones de `G20`/`G21`/`G23` en doc 11, **17 están dentro del propio bloque de `PN-15`**, una en §17 y una en §19 — todas escritas por `D97` en el mismo commit. **La evidencia se destruyó al registrarla.** MEDIO es la graduación correcta, porque el argumento que sostiene la presión —que el material APROBADO no deroga `G20`–`G23`— sobrevive intacto.

##### `P-07` · CONFIRMADO · MENOR

El bloque `E5` justifica no crear presión con «aquí **no hay norma presionada**… una cita mal puesta y una lista mal numerada». Impecable para `E5-1` y `E5-2`. **No lo es para `E5-3`**, cuya propia fila dice «si es la sin tilde, **F5 enmienda (b)**» y «**Hermano exacto de `F-01`/`PN-14`, que SÍ se registró como presión**» — y `F-01` fue reclasificado a `PN-14` **una tanda antes por esa forma exacta**. Consecuencia: el único de los cuatro que puede exigir enmendar material aprobado es el que no llega al Owner. Correcto, y MENOR.

##### `P-08` · REGRADUADO · MENOR · **su premisa de hecho es FALSA**

**Resuelvo la corrección que el coordinador me plantea, y va antes que nada.**

`P` afirma «**tercera pasada consecutiva** en que esa fuente no se abre» sobre `15-TERCERA-REVISION`. **Es falso, y lo verifiqué en la fuente:** doc 20 **L372** — «*Lo que mi cobertura sí cierra: las **catorce fuentes** del `C-0.1` del documento 18 —incluido **el documento 15**—*» — y **L638** — «*La condición `C-0.1` del documento 18 **queda cubierta por el lote de `N`***». El revisor `N` la leyó **íntegra** y el adjudicador `O` lo registró.

**Y ahora la pregunta que se me deja a mí: ¿satisface `C-0.1` una lectura hecha en un gate anterior, o cada gate debe rehacerla?**

**RESUELVO: la lectura en un gate anterior SATISFACE `C-0.1`, y no hay que rehacerla.** Cuatro razones, y la tercera es la que decide:

1. **`C-0.1` está redactada como condición de ESTADO DEL CORPUS, no como obligación por pasada.** Su literal es «CUBRIR LAS CATORCE FUENTES OBLIGATORIAS **QUE NADIE ABRIÓ**» (doc 18 L3569). El sujeto de la condición es «fuentes que nadie abrió». Una vez `N` las abrió, esas fuentes dejaron de pertenecer al conjunto que la condición describe. **La condición no se incumple: se agota.**
2. **Su efecto declarado es «DESBLOQUEA: el juicio mismo. Sin esto no hay gate, hay una muestra.»** Lo que la condición protege es que el expediente haya sido leído **al menos una vez por alguien independiente** — no que cada pasada repita el corpus entero.
3. **La lectura se hizo en las condiciones que la propia condición exige, y su producto es auditable HOY.** `N` era revisor nuevo con contexto limpio, declaró lectura íntegra con manifiesto, `O` la registró, y **el documento 20 —donde consta— está en MI lote y lo he leído íntegro**. No estoy presumiendo una lectura ajena: estoy leyendo su resultado.
4. **La lectura contraria haría la condición insatisfacible en la práctica** y convertiría cada gate en una relectura de 31 517 líneas, que es precisamente el coste que la disciplina de manifiestos existe para acotar.

**Consecuencia:** cae la mitad de hecho de `P-08`. Las siete fuentes que `P` nombra —doc 15, doc 19, y las cinco de `diseno/`— **no son fuentes sin abrir**: doc 15 y `diseno/00`–`05` las leyó `N`; doc 19 lo leyó `M` (doc 20 L78, su lote, 1152 líneas).

**Qué SÍ sobrevive, y lo confirmo:** `D106` (`11-ARQ:9252`) pide «*el total, derivado: fuentes obligatorias, asignadas y sin asignar*» **sin fijar de dónde sale «obligatorias»**. El universo del manifiesto es **elegido**, no derivado, y por tanto «FUENTES SIN ASIGNAR **0**» es verdadero por construcción. Es un defecto formal real, de la misma familia que `C-L.5` denuncia un escalón más arriba, y **la corrección es una frase**: fijar la sede de la que se deriva «obligatorias». **MENOR, y NO bloquea**, porque la regla que `C-L.5` sí exige —`asignado − leído = ∅`— es hoy calculable y la he calculado.

---

#### 6 · Adjudicación de `Q-01`–`Q-15`

**Reproduje nueve de los quince por mi cuenta.** Confirmo los quince; regraduo uno.

| id | mi adjudicación | severidad | reproducido por mí |
|---|---|---|---|
| `Q-01` | **CONFIRMADO** | MEDIO | **sí** — `G-11b` da OK «ninguna difiere» con `D12`/`D40`/`D80` reescritas y sin `.git` |
| `Q-02` | **CONFIRMADO** | MEDIO | **sí** — `capacidad_productora: "VER:dosier"` en `INC` → anclas sin VER `['AUD','INC','INV']`, G-15 VERDE |
| `Q-03` | **CONFIRMADO** | MENOR | **sí** — `DOM`/`SEG` desnudos en `FEA` → vías `[(2,1),(3,2),(4,6)]`, G-15 VERDE |
| `Q-04` | **CONFIRMADO** | MEDIO | **sí** — `01-PROCESOS-BIS.md` + `C8-SEGUNDA-SEDE.md` → **30/30 EN VERDE** |
| `Q-05` | **CONFIRMADO** | MEDIO | **sí** — `FEA part` pasa a `[('DOM',2),('DOM',4),('SEG',4)]` |
| `Q-06` | ≡ `P-02` | MEDIO | sí |
| `Q-07` | **CONFIRMADO** | MEDIO | sí — §16 L7887 «`PN-6` a `PN-14`» = DOCE; L8447 dice TRECE; L8687 dice bien «`PN-6` a `PN-15`» |
| `Q-08` | ≡ `P-05` | GRAVE | sí |
| `Q-09` | **CONFIRMADO** | MENOR | **sí** — `grep 'participa dos veces'` sobre las quince fichas → **exactamente dos líneas**, `DOM:51` y `SEG:51` |
| `Q-10` | **CONFIRMADO como latente** | MENOR | sí, por código: `_exige_item` trata `via in (3,4)` como condicional sin conservar la sección de origen. Hoy **ninguna** vía 4 procede de `obligatorias` |
| `Q-11` | **CONFIRMADO** | MENOR | **sí** — la obligatoria de `INV` es `evidencia-producida`; `conclusion-fundada` es la de `AUD`. L8880 se la atribuye a las dos |
| `Q-12` | **CONFIRMADO** | MENOR | sí — L8985 dice «cinco fixtures» y enumera cuatro vías + `AUD` + `DIR` = seis grupos; los dinámicos son **tres** |
| `Q-13` | ≡ `P-01` | MEDIO | sí |
| `Q-14` | **CONFIRMADO** | MEDIO | sí — `grep 'C-L\.3'` sobre el checkpoint: L46, L98, L284, L994, L1011, L1065. **`D104` no aparece en ninguna** |
| `Q-15` | **CONFIRMADO** | MENOR | **sí** — `ancho` (L1102) se calcula y las dos `f`-strings usan anchos fijos: código muerto. Errata «toda / todo `abandonada` su `conflicto`» en L4350–4351 |

**Dos precisiones que hago a `Q`:**

- **`Q-14` es más grave de lo que `Q` lo presenta, y menos de lo que parece.** El bloque L991–1054 está separado temporalmente del de L1058–1069 («ESTADO TRAS EL GATE…»), así que la doble asignación no es un descuido de `G-16`. **Pero el bloque anterior no lleva marca histórica y describe `C-L.3` con la regla de `D103` que `M-01` refutó** («cero o un par, **nunca dos**»), y **`D104` no aparece en ninguna de las seis sedes de `C-L.3`**. En el registro reanudable, la condición que bloquea el paso a F5 se describe con la formulación que dos gates han declarado insuficiente. MEDIO, confirmado.
- **`Q-04` no falsifica la prosa del checkpoint.** El checkpoint describe `git diff --name-only 05f71b7..HEAD`, que es sobre ficheros **rastreados y modificados**; una adición no rastreada cae fuera de esa afirmación. Lo que sí falsifica `Q-04` es el **título** de `G-22`/`G-23` —«lo normativo **intacto**»— y la promesa que un lector deriva de un 30/30. Es exactamente la clase que el propio corpus condena en L4409–4413: «*una promesa así es peor que no tenerla, porque nadie construye después el mecanismo que sí lo haría*».

---

#### 7 · Mis propios hallazgos

**`R-01` · MENOR · el residuo de `P-03`.** La justificación de idempotencia de `W17` por contenido (L961–966, L1163, L1934–1936) invoca un razonamiento que §2.8 L2930–2939 **retiró expresamente**, para una propiedad que la guarda del paso 0 y la regla 3 de L4406 ya garantizan. Sobra una frase. **No bloquea.**

**`R-02` · MEDIO · `M-06` reproducido en la sede de entrada, en la tanda que lo declara corregido.** `CHECKPOINT` L2023–2029 dice «la excepción es exacta y se nombra» y enumera **TRES** ficheros, donde L1911–1942 —corregido en `7764cca`, «*derivar la excepción exacta del kernel*»— deriva **SEIS** de Git y los enumera uno a uno. La corrección alcanzó una sede del mismo fichero y no la otra. Es el patrón que `O` nombró, en el fichero que existe para no repetirlo.

**`R-03` · MEDIO · §2.6.9 L1940–1941 invoca la capa B por su nombre y la capa B no dice lo que se le atribuye.** Detallado en `P-02`. Lo separo porque el remedio no es el mismo: `P-02` se cierra corrigiendo un verbo en L4360; `R-03` se cierra decidiendo si la lista de la capa B o la tabla de las cuatro reglas es la sede, y haciendo que la otra remita.

**`R-04` · MENOR · la sub-ventana del marcador que `W17` nombra queda fuera de su propia condición de detección.** L1163 declara que `W17` cubre «*—o entre el `deriva` y su marcador—*», y su condición de detección es «*`abandonada` presente **sin ningún `deriva`** … y el marcador de transacción todavía puesto*». Con el `deriva` ya emitido y su marcador ausente, la condición es falsa. El caso **está cubierto** —por §2.9, por `X60` y por el reparto de §2.6.9 punto 7, que lo asigna a `W8`—, y por eso `P` perdió correctamente esta refutación; lo que sobra es la frase que se lo atribuye a `W17`.

---

#### 8 · Discrepancias entre `P` y `Q`, resueltas contra la fuente

| # | discrepancia | resolución |
|---|---|---|
| **D-1** | **`N-04`: `P` lo declara SUPERADO; `Q`, CONTRATADO PARA F6.** | **Resuelvo a favor de `Q`.** Abrí las tres sedes: doc 17 L116 dice **22** y L521 dice **21**; el recuento real es **21** (`grep -c '^id: perfil:'` sobre `C2`); `RECUENTOS-generado.md` **sigue sin contar perfiles** (`grep 'perfil'` → vacío). El corpus reancla la cifra a 21 en `11-ARQ:9078–9086` y contrata su derivación como **CONTRATO 1bis, propietario `PLT`, fase F6, dentro de `C-L.10`**. Cero líneas escritas. **CONTRATADO PARA F6.** El checkpoint L21–23 dice lo mismo, y coincide. |
| **D-2** | **`O-04`: `P` lo declara SUPERADO; `Q` lo distingue —«SUPERADO en su causa»— del estado de `C-L.5` como condición.** | **Resuelvo con la precisión de `Q` y el resultado de `P`.** La causa de `O-04` era que `asignado − leído` no fuera calculable. **Hoy lo es, y lo he calculado: ∅.** `O-04` **SUPERADO**, y con él **`C-L.5` queda CERTIFICADA** — cosa que `O` no pudo hacer y que este gate sí puede. |
| **D-3** | **`P-03` frente al silencio de `Q`.** `P` funda su primera razón de veredicto en él; `Q` no lo encuentra pese a tener la batería y el kernel. | **Resuelvo contra `P`.** Reproduje el paso 0, la tabla de alternativas y la regla 3 de L4406. Que `Q` no lo hallara no es evidencia; que las cinco sedes lo desmientan, sí. **Ver §5.** |
| **D-4** | **`P-08`: `P` cuenta siete fuentes sin abrir; `Q` no registra laguna de cobertura.** | **Resuelvo contra `P` en el hecho y a favor de los dos en el resultado.** Las siete fueron leídas íntegras en el gate anterior (doc 20 L78–79, L372, L638). Sobrevive sólo la mitad formal de `D106`. **Ninguno de los dos falla por cobertura, y yo tampoco.** |
| **D-5** | **`M-04`: `Q` lo pone entre los 17 SUPERADOS; `P` no lo adjudica.** | **Resuelvo contra los dos, y es mi única discrepancia con el corpus.** Ver §9. |
| **D-6** | **Severidad de `P-05`≡`Q-08`.** `P` GRAVE; `Q` MEDIO. | **GRAVE**, por los dos puntos que ninguno de los dos vio —el punto 2 y, sobre todo, el punto 3, que reproduce `M-06`— y porque es la sede de entrada. |

**No hay ninguna discrepancia material irresoluble entre `P` y `Q`.** Las seis se resuelven abriendo la fuente. Y consta un dato del método: **`P` y `Q` convergieron de forma independiente en `P-01`≡`Q-13` y `P-02`≡`Q-06` y `P-05`≡`Q-08`**, desde lotes disjuntos y sin verse.

---

#### 9 · Adjudicación de los 21 hallazgos del documento 20

**Un solo estado cada uno. Sin estados compuestos.**

| id | **estado** | motivo verificado |
|---|---|---|
| `M-01` | **SUPERADO** | `D104` deriva la vía CONDICIONAL de `AUD`. Derivé con el propio código las **cuatro combinaciones**: `∅` · `{DOM}` · `{SEG}` · **`{DOM,SEG}`** — exactamente lo que `D103` («cero o un par, nunca dos») no podía |
| `M-02` | **SUPERADO** | `deriva_emitida` **PROHIBIDO** en `abandonada` (§3.6 L4217, §2.6.9 L1868); el `deriva` gana `abandonada_id` unilateral. La circularidad no existe. Tres alternativas comparadas en tabla y elegida la mínima |
| `M-03` | **SUPERADO** | `fsync` obligatorio punto **(5)**: «el evento `deriva` … **Y SU DIRECTORIO**, ANTES de retirar el marcador» (L1239). `W17` añadida y el recuento pasa a 18, derivado |
| `M-04` | **FALLIDO** | **Mi única discrepancia con el corpus y con `Q`, y la argumento.** Sus **cuatro refutaciones nombradas están cerradas** —las reproduje: `R1` 28/30, `R2` 29/30, `R3` 29/30, `R4` 26/30—. Pero `M-04` no es una lista de cuatro fixtures: es la **proposición** «*se puede construir un árbol defectuoso que pase 30/30 en verde*». **Esa proposición sigue siendo verdadera, y la demostré yo:** con `01-PROCESOS-BIS.md` (copia íntegra del catálogo, segunda sede de la misma verdad) y `C8-SEGUNDA-SEDE.md` (que declara **por escrito** que contradice a `C4`) bajo `kernel/`, la batería da **30/30 EN VERDE** (`Q-04`). Y `G-11b` declara intactas las ochenta y seis filas con tres reescritas (`Q-01`). Cerrar las cuatro instancias no cierra el hallazgo |
| `M-05` | **SUPERADO** | `D106` retira la disyunción. La prueba **falla hoy y tiene que fallar**: `grep 'G2[0-3]'` sobre (a) devuelve **una línea**, la ficha de `INV`, no una fila derogatoria. Lo ejecuté |
| `M-06` | **SUPERADO** | `CHECKPOINT` L1911–1942: **seis** ficheros derivados de `git diff --name-only 05f71b7..HEAD -- kernel/`, enumerados uno a uno, y `G-23` los contrasta contra la prosa. *(El residuo en L2023 es `R-02`, hallazgo nuevo, no `M-06` vivo)* |
| `M-07` | **SUPERADO** | ADDENDUM DE CRONOLOGÍA. Verifiqué las dos fechas en `git log`: `a713590` = **2026-08-28**, `d868bcb` = **2026-08-29**. El addendum **empeora su propia posición para ser exacto**: declara que entre el 28 y el 29 `O16` fue «una formulación registrada **a la espera de confirmación**». No reescribe `O16`, no inventa cita, no crea `O17` |
| `M-08` | **SUPERADO** | La frase está en `a.6` **L502–503** (la conté sobre el fichero); doc 11 L8776 cita ahora L502–503 con su nota «**corregido por `M-08`**» |
| `M-09` | **REGISTRADO PARA F5** | Grafía `revisión`/`revision` en material APROBADO que F4c no puede editar. Va a la checklist `E5-3`. Coinciden `P`, `Q` y el checkpoint |
| `M-10` | **SUPERADO** | Orden derivado por mí: `… X56 X57 **X58** X59 X60 X61 X62` |
| `M-11` | **SUPERADO** | La línea muerta se **retiró** (L540–543 lo documenta) y la sustituye una detección sobre la **línea entera** (L650–651). **Control positivo reproducido:** inyecté un estado compuesto y `G-16` falla con «*matriz: estados COMPUESTOS `['A1']`*» |
| `M-12` | **SUPERADO** | **Reproducido:** sin `.git`, `G-21`, `G-22` y `G-23` fallan CERRADO con «GIT NO RESPONDE: no se puede saber qué se tocó». `_git()` devuelve `None` si `returncode != 0` |
| `N-01` | **SUPERADO** | El **ancla ya no presupone `VER`**: derivé con el propio código que la de `AUD` es su única obligatoria (`INV`), no `VER`. Y **`DIR` entra por la misma regla sin excepción escrita**: los dinámicos derivados son `['AUD','DEF','DIR']` |
| `N-02` | **SUPERADO** | El discriminante es `pg in _CAPS` (L349) — **igualdad de cadena contra un conjunto derivado de los directorios**, no búsqueda de la palabra «DERIVADO» en prosa libre |
| `N-03` | **REGISTRADO PARA F5** | Marcas `[E1]` en material APROBADO. Va a `E5-4`. *(`P` lo declara fuera de su lote; el checkpoint y `Q` coinciden conmigo)* |
| `N-04` | **CONTRATADO PARA F6** | Ver **D-1**. Cifra reanclada a 21 en sede vigente; derivarla es CONTRATO 1bis, propietario `PLT`, fase F6, dentro de `C-L.10`. **Cero líneas escritas**, y `RECUENTOS-generado.md` sigue sin contar perfiles |
| `N-05` | **SUPERADO** | §8.4 L6584–6595 conserva el calificativo «**PROVISIONAL**», cita la procedencia correcta —`IDEAS` §3, no §15— y L6682–6696 registra la **segunda sede** de `ADS-PENDIENTES` L914–916 con su análisis. La sustancia de `F-09` sigue cierta y consta |
| `O-01` | **SUPERADO** | **Reproducido (`R1`):** `proceso:SIS` con `propietario_global: "SEG"` hace **fallar `G-15`** — «*publica CINCO procesos y el catálogo deriva 6; publica NUEVE pares y deriva 10*». La vía propietaria **no es decorativa** |
| `O-02` | **SUPERADO** | `_COMPONENTES_CL13` **retirado** (0 apariciones); los componentes se derivan de la fila de detalle (L625–626); el mensaje de éxito se **deriva** (L659–668) y el 30/30 real imprime «C-L.13 MIXTA con **6 componentes derivados**» |
| `O-03` | **SUPERADO** | El paso 0 **completa** el `deriva` ausente en vez de prohibirlo (L956–974), y L4406 exige «exactamente UN `deriva` que la referencie por `abandonada_id`». Las dos afirmaciones que no podían ser ciertas a la vez ya lo son |
| `O-04` | **SUPERADO** | Los **DOS manifiestos existen**: el de asignación, commiteado antes de repartir y verificado por mí fila a fila; y los tres de lectura. **`asignado − leído` es calculable y lo he calculado: ∅** |

```text
RECUENTO DERIVADO DE LAS FILAS DE ARRIBA, no copiado

  SUPERADO                17   M-01 M-02 M-03 M-05 M-06 M-07 M-08 M-10 M-11 M-12
                               N-01 N-02 N-05 · O-01 O-02 O-03 O-04
  FALLIDO                  1   M-04
  REGISTRADO PARA F5       2   M-09 · N-03
  CONTRATADO PARA F6       1   N-04
  ABIERTO                  0
  NO APLICABLE             0
                          ──
                          21   los veintiún ids, cada uno EXACTAMENTE UNA VEZ
```

---

#### 10 · Las cuatro refutaciones prescritas, reproducidas por mí

**Modo:** `git archive HEAD | tar -x` en `/tmp`, `.git` copiado, una copia limpia por refutación. **El repositorio no se tocó.**

```text
BASELINE                                                            30/30 EN VERDE

R1  proceso:SIS → propietario_global "SEG"              28/30   FALLA G-15 (+G-23 lateral)
    G-15: «publica CINCO procesos y el catálogo deriva 6;
           publica NUEVE pares y deriva 10»

R2  segunda proyección «SEIS procesos y DIEZ pares»     29/30   FALLA G-15, y SÓLO G-15
    G-15: «hay 2 proyecciones en el bloque y debe haber UNA:
           [('CINCO','NUEVE'), ('SEIS','DIEZ')]»

R3  C-L.12 movida a CORREGIDAS, contadores ajustados    29/30   FALLA G-16, y SÓLO G-16
    G-16: «C-L.12: el resumen lo pone en «CORREGIDAS EN F4c»
           y su fila de detalle dice «REGISTRADA PARA F5»»

R4  .git ausente + D67 reescrita + doc 18 volteado       26/30   FALLAN G-11 G-21 G-22 G-23
    G-21/22/23: «GIT NO RESPONDE: no se puede saber qué se tocó»
```

> **Las cuatro refutan.** **NO hay falsos verdes en `R1`–`R4`.** Y en `R2` y `R3` **falla la responsable SOLA**, que es lo que distingue una comprobación de un ruido. La coincidencia con lo que `Q` publicó es exacta, mensaje a mensaje.

**Y las tres que sí son falsos verdes, fuera de `R1`–`R4`, reproducidas igualmente:**

```text
Q-01  D12/D40/D80 reescritas, sin .git    G-11b → OK «ninguna difiere»       30/30 salvo los 4 de R4
Q-04  01-PROCESOS-BIS.md + C8-SEGUNDA-SEDE.md bajo kernel/                   30/30 EN VERDE
Q-05  capacidad_productora inyectada en la prosa de criterio_de_satisfaccion
      FEA part: [('DOM',4),('SEG',4)] → [('DOM',2),('DOM',4),('SEG',4)]      G-15 VERDE
Q-02  capacidad_productora: "VER:dosier" en INC (vía 4 legítima)
      anclas sin VER: ['AUD','INV'] → ['AUD','INC','INV']                    G-15 VERDE
Q-03  DOM/SEG desnudos en FEA: vías [(2,1),(4,8)] → [(2,1),(3,2),(4,6)]      G-15 VERDE
```

---

#### 11 · Las siete condiciones de suficiencia, una a una

| # | condición | resultado |
|---|---|---|
| 1 | `asignadas − leídas = ∅` | **SE CUMPLE.** 43 fuentes, 59 asignaciones, 43 SHA-256 verificados, ∅ en los tres revisores |
| 2 | `C-L.5` **certificada** | **SE CUMPLE, y es la primera vez.** Quién · qué íntegro · dos manifiestos · resta calculable · declaración de cobertura real · el adjudicador no corrige |
| 3 | `D104`–`D106` **superan el intento adversarial** | **NO SE CUMPLE** |
| 4 | los cuatro bloqueantes del gate anterior **superados** | **SE CUMPLE.** `M-01`, `M-02`, `M-03`, `N-01`: los cuatro SUPERADOS, verificados por mí uno a uno |
| 5 | ningún pendiente de F5/F6 **exige inventar arquitectura** | **SE CUMPLE.** Recorrí los veintiún hallazgos, las trece condiciones y las trece presiones: **ninguno** exige decidir diseño. Todo se cierra propagando material ya escrito, o es decisión del Owner correctamente registrada y no tomada |
| 6 | **ninguna contradicción material vigente sin registrar** | **NO SE CUMPLE** |
| 7 | la batería **no ofrece falsos verdes en `R1`–`R4`** | **SE CUMPLE.** Las cuatro refutan, y en dos falla la responsable sola |

##### Por qué falla la condición 3

`D104` **es una buena decisión y lo digo primero**: las cuatro vías operan, la propietaria no es decorativa (`R1`), el discriminante es estructural, las cuatro combinaciones de `AUD` se derivan, `DIR` entra por la misma regla sin excepción escrita, y **no hay décimo par**. Reproduje todo eso.

**Pero dos de sus cuatro pilares declarados son falsables contra el árbol, y los falsé yo:**

- **Pilar (ii) — «`capa_exigida`, `condicion`, `criterio_de_satisfaccion` y `autoridad_de_retirada` NO se leen».** Es **falso del troceado sobre el que opera**. El troceado real es un `re.findall` sobre un **segmento de texto** delimitado por `find("obligatorias:")` y `find("condicionales:")`, no un parseo YAML. Una línea dentro de un block scalar de `criterio_de_satisfaccion` **entra en la derivación**: `FEA part` pasó a `[('DOM',2),('DOM',4),('SEG',4)]`. La afirmación es absoluta y el mecanismo no la sostiene.
- **Pilar (iv) — el ANCLA DE POSICIÓN.** `ancla = "VER" if "VER" in obl else obl[-1]` compara la **cadena cruda**; `_base()` se aplica a las participaciones y **no al ancla**, contra la propia declaración de `D104` de que la normalización a la capacidad BASE «**ES TODA LA INFERENCIA QUE HAY**». Un `capacidad_productora: "VER:dosier"` —vía 4 **legítima** por el propio contrato— desplaza silenciosamente el ancla de un proceso y `G-15` imprime **verde**.

**`D105` supera el intento adversarial**, y con holgura: intenté tumbarlo por el camino de `P-03` y **no cayó**. `D106` supera el suyo: su prueba de `PN-15` falla hoy, y lo comprobé ejecutándola. **La condición 3 falla por `D104`, y por sus pilares (ii) y (iv), no por su arquitectura.**

##### Por qué falla la condición 6

**Siete contradicciones materiales, VIGENTES y SIN REGISTRAR.** No es una discutible: son siete, verificadas contra fichero y línea, y **tres de ellas son la segunda o tercera recurrencia de la misma frase**:

```text
1  X54 dice «diecisiete» · §2.6.5 dice DIECIOCHO y lo deriva de 18 filas     P-01 ≡ Q-13
2  capa B L4360 «DECLARA SU deriva» · D105 lo invirtió, y L4406 lo dice bien  P-02 ≡ Q-06
   — y §2.6.9 L1941 invoca la capa B para una regla que la capa B no escribe  R-03
3  CHECKPOINT L1142 cuenta 9 ventanas RC-1–RC-9 · 11-ARQ:8672 dice que NO
   se cuentan · y el propio L1641 declara M-8 corregido POR RETIRARLAS       P-04
4  «Siguiente acción exacta»: CINCO afirmaciones falsas, sin marca de
   histórica, en la sede que se autodesigna punto de entrada — y una de
   ellas reproduce M-06 en la tanda que declara M-06 corregido      P-05 ≡ Q-08 + R-02
5  PN-15 declara «cero apariciones de G20/G21/G23 en el documento 11»
   y hay 13 · 11 · 14, introducidas por el propio bloque que lo niega        P-06
6  §16 L7887 «PN-6 a PN-14» = DOCE · L8447 dice TRECE · L8687 dice bien
   «PN-6 a PN-15» — y omite justo la presión que va al Owner                 Q-07
7  C-L.3 descrita en el registro reanudable con la regla de D103 que M-01
   refutó, y D104 no aparece en NINGUNA de sus seis sedes                    Q-14
```

**Y lo que las hace decisivas no es su número: es su forma.** `Q-07` es la **tercera** vez que se corrige esa frase (`m2`, luego `I-11`, y falla otra vez). `P-05` es la **segunda** seguida sobre esa línea (`I-28` la corrigió de ONCE a DOCE, y hoy son TRECE). `P-01` es la **segunda** sobre la tabla adversarial. Y en `Q-07`, en `P-05` y en `P-06`, **lo omitido o falseado es precisamente lo que va al Owner**.

**Ninguna de las siete es invisible por accidente.** `G-13` y `G-26` exigen un **numeral** y **un RANGO no es un numeral**; `G-26` toma `t11` por defecto y **no escanea el checkpoint**; `G-16` comprueba coherencia entre resumen y detalle, **no vigencia**. Las comprobaciones están bien construidas y estas siete caen exactamente por sus junturas.

---

#### 12 · Cifras derivadas

```text
CORPUS LEÍDO POR MÍ           9 fuentes · 21 732 líneas · 9 SHA-256 recalculados
MANIFIESTO VERIFICADO         43 filas · 43 coinciden en líneas Y SHA-256 · 0 ausentes
ASIGNACIONES                  59 · asignadas − leídas = ∅ en P, en Q y en R
DIFERENCIA CANDIDATO..HEAD    1 fichero · 140 inserciones · 0 supresiones
REGISTRO 652ab8e..HEAD        169 inserciones · 0 SUPRESIONES  → D1–D103 y O1–O16 intactas
DECISIONES                    D1–D106, serie continua, huecos [] repetidas []
PRESIONES                     15 cabeceras − PN-4 RETIRADA − PN-5 FUSIONADA = 13 vigentes
VENTANAS DE CAÍDA             18 filas (W1–W11, W12a, W12b, W13–W17) · prosa dice DIECIOCHO
TABLA ADVERSARIAL             46 filas / 46 ids en §2.6.7 (+ 8 de X1–X8 en §15.5, otra serie)
FILAS X QUE MENCIONAN W17     0
MATRIZ DE LOS 43              43 filas / 43 ids · 31·2·2·7·1 = 43
CATÁLOGO <CAP>:revision       5 procesos · 9 pares · vías [(2,1),(4,8)] · dinámicos AUD DEF DIR
BATERÍA, ÁRBOL REAL           30/30 en verde
REFUTACIONES R1–R4            28/30 · 29/30 · 29/30 · 26/30   ← las cuatro refutan
FALSOS VERDES FUERA DE R1–R4  3   Q-01 · Q-04 (30/30 con catálogo duplicado) · Q-05
HALLAZGOS DEL DOC 20          21 · SUPERADO 17 · FALLIDO 1 · F5 2 · F6 1 · ABIERTO 0 · N/A 0
HALLAZGOS DE ESTE GATE        P 8 · Q 15 · R 4 propios · 3 solapes (P-01≡Q-13, P-02≡Q-06,
                              P-05≡Q-08)  →  24 distintos
  BLOQUEANTE 0 · GRAVE 1 (P-05) · MEDIO 12 · MENOR 11
RECHAZADOS POR MÍ             1 completo (P-03 en su tesis) + 1 premisa de hecho (P-08)
```

---

#### 13 · Proporcionalidad

**Ninguno de los veinticuatro hallazgos exige rediseñar arquitectura, y lo comprobé uno a uno.**

`P-01` es **una palabra**. `P-02` y `R-03`, un verbo y una remisión. `P-04`, dos líneas. `P-05`, reescribir una sección de 73 líneas contra el estado que el propio fichero ya publica bien 800 líneas más arriba. `P-06`, acotar el sujeto de una frase. `Q-07`, un identificador. `Q-14`, marcar un bloque como histórico y nombrar `D104`. `Q-01`, **añadir cinco caracteres**: `_base_raw is not None and`. `Q-02`, envolver el ancla en `_base()`. `Q-05`, trocear por bloque en vez de por segmento. `Q-04`, comparar contra el árbol y no sólo contra `git diff`. `P-08`, fijar la sede de «obligatorias».

**Y en la otra dirección, porque también hay que decirlo.** **No he contado como insuficiencia** la ausencia de runtime, de piloto, de adaptadores certificados ni de adopción de PesquerApp. Verifiqué que están declaradas con propietario y fase, que `J-11` y `C-L.10` declaran cero implementación **y la tienen de verdad**, y que `O15` no autoriza iniciar nada. Eso es lo que F4 debe entregar, y lo entrega.

---

#### 14 · Límites de esta adjudicación

```text
1  NO he leído el corpus obligatorio ÍNTEGRO. Leí íntegras las NUEVE que se me
   asignaron —21 732 líneas—, y verifiqué por reproducción dirigida todo lo demás.
   NO puedo certificar que las fuentes fuera de mi lote no contengan algo que
   refute o agrave lo de arriba; me apoyo, DECLARÁNDOLO, en los manifiestos de
   lectura de P y de Q, que no rehíce.

2  MI RECHAZO DE `P-03` DEPENDE DE UNA LECTURA, y la declaro: sostengo que
   §2.6.9 punto 4 es lex specialis sobre §3.6 para este evento, y que la guarda
   del paso 0 hace la cuestión irrelevante para la idempotencia. Lo que NO admite
   lectura, y es lo que decide, es que el paso 0 comprueba la existencia ANTES
   de emitir, y que L4406 escribe la regla de unicidad que P da por ausente.

3  MI ADJUDICACIÓN DE `M-04` COMO FALLIDO ES LA MÁS DISCUTIBLE DE LAS 21, y me
   aparto de Q y del checkpoint. Si alguien sostiene que un hallazgo se cierra
   cerrando sus instancias nombradas y no su proposición, `M-04` sería SUPERADO
   y `Q-04` un hallazgo nuevo. **El veredicto NO cambiaría**: las condiciones 3 y 6
   lo determinan por otra vía, y Q-04 seguiría siendo un falso verde reproducido.

4  MI RESOLUCIÓN SOBRE `C-0.1` —que la lectura en un gate anterior la satisface—
   es una decisión de criterio, no un hecho. La tomo con los cuatro argumentos
   de §5 y asumo su consecuencia: si se resolviera al revés, el veredicto seguiría
   siendo INSUFICIENTE, y además por cobertura.

5  NADA DE ESTO ESTÁ CONSTRUIDO. No hay esquema de `evento`, ni validador del
   diario, ni runtime, ni un fichero bajo `estado/`. Todos los hallazgos sobre el
   protocolo son sobre TEXTO. Un contrato contradictorio no es un sistema roto.

6  DONDE ESCRIBO «reproducido», LO EJECUTÉ en /tmp y pego su salida. Donde escribo
   «verificado», abrí el fichero en su línea. Donde acepté algo, lo digo en §4.

7  MI PUNTO MÁS DÉBIL ES LA SEVERIDAD, NO EL HECHO. Los veinticuatro hallazgos
   están abiertos en su fichero y su línea o reproducidos. Si alguien graduara
   `P-05` como MEDIO, el veredicto NO cambiaría: la condición 6 falla con las otras
   seis contradicciones, y la 3 falla por su cuenta.
```

---

#### 15 · VEREDICTO

### `INSUFICIENTE PARA F5`

**`F4c` NO se cierra. Sigue ABIERTA. `F5` NO queda autorizada. No se ha corregido nada.**

**Cuatro razones numeradas. Las dos primeras son, cada una, condición de suficiencia incumplida; las dos últimas explican por qué no son formalismos.**

1. **La condición 6 no se cumple: quedan SIETE contradicciones materiales vigentes y sin registrar.** No una marginal: siete, verificadas contra fichero y línea, entre ellas la sección que el checkpoint designa como **punto de entrada** y que contiene cinco afirmaciones falsas a la vez. **Tres son segunda o tercera recurrencia de la misma frase**, y en tres de ellas lo omitido es exactamente lo que va al Owner.

2. **La condición 3 no se cumple: `D104` no supera íntegro el intento adversarial.** Su arquitectura resiste —lo digo sin reservas—, pero **dos de sus cuatro pilares declarados son falsables contra el árbol y los falsé yo**: la afirmación absoluta de que los campos de prosa «NO se leen» es falsa del troceado real (`Q-05`), y el ancla de posición **no normaliza**, contra la propia declaración de `D104` de que la normalización «ES TODA LA INFERENCIA QUE HAY» (`Q-02`). Las dos pasan en verde.

3. **La única garantía mecánica sigue produciendo falsos verdes, y esta vez el contraejemplo es peor que los anteriores.** Reproduje `30/30 EN VERDE` sobre un árbol que contiene una **copia íntegra del catálogo de procesos** y un contrato que **declara por escrito que contradice a `C4`**. La verdad duplicada es precisamente lo que la disciplina de fuente única prohíbe, y es la razón de ser de `I5`. Y `G-11b` —el de mayor alcance de los que dependen de Git, ochenta y seis filas— **es el único que no falla cerrado**.

4. **Y la razón de método, que es la que impide cerrar aquí.** De los veinticuatro hallazgos de esta pasada, **la mayoría los introdujo o los dejó pasar esta misma tanda**, y tres son la enésima reaparición de una frase ya corregida. `P-05` punto 3 lo enseña en su forma más pura: **la tanda que declara `M-06` corregido reproduce `M-06` en la sede de entrada del mismo fichero**. Cerrar aquí sería premiar exactamente el patrón que doce tandas han perseguido — «una decisión bien tomada llega a la mitad de los sitios que la invocan».

**Lo que expresamente NO fundamenta este veredicto:**

- **NO falla por cobertura.** Es la primera vez que `C-L.5` queda **CERTIFICADA**, y la certifico.
- **NO falla por los cuatro bloqueantes del gate anterior.** `M-01`, `M-02`, `M-03` y `N-01` están **los cuatro SUPERADOS**, verificados por mí uno a uno.
- **NO falla por `D105`**, que resiste el ataque más duro que se le hizo.
- **NO falla porque nada esté construido.** Ninguna de mis cuatro razones es la ausencia de runtime, piloto, adaptadores o PesquerApp.
- **NO falla porque quede arquitectura por inventar.** Ninguno de los veinticuatro hallazgos exige decidir diseño.

---

#### 16 · Qué consta a favor, y no es cortesía

- **`D105` es la mejor decisión que este expediente ha producido.** Tres alternativas comparadas **en tabla**, con las tres preguntas que importan —identidad construible, cadena verificable, bloqueo persistente— y elegida la mínima, con el motivo escrito de por qué las otras dos se descartan. Cierra `M-02`, `M-03` y `O-03` de una vez, **sobrevivió a mi ataque** y no añade ni un evento, ni un tipo, ni un campo.
- **Los cuatro bloqueantes del gate anterior están cerrados de verdad**, y con mecanismo, no con prosa: la vía propietaria **hace fallar** `G-15` (lo ejecuté), las cuatro combinaciones de `AUD` se derivan, el ancla ya no presupone `VER`, `DIR` entra por la misma regla **sin excepción escrita**, `deriva_emitida` está PROHIBIDO, el `fsync` del `deriva` **con su directorio** existe, y el paso 0 completa en vez de prohibir.
- **`M-12` está cerrado y lo comprobé sin `.git`:** `G-21`, `G-22` y `G-23` fallan **cerrado**, con diagnóstico. `M-11` está cerrado y su **control positivo dispara**. `O-02` está cerrado: los dos censos escritos a mano **desaparecieron** y el mensaje de éxito se deriva.
- **La disciplina de inmutabilidad se cumple sin excepción:** `git diff --numstat 652ab8e..HEAD` sobre el registro da **169 inserciones y CERO supresiones**. `D1`–`D103` conservan su texto, `O1`–`O16` están intactas, los documentos 15–18 sin tocar, `C7` sin tocar.
- **El addendum de `O16` es un acto de honestidad poco frecuente**: no retro-fecha nada; **empeora su propia posición para ser exacto**, declarando que entre el 28 y el 29 la resolución estaba a la espera de confirmación. Y no reescribe `O16` ni crea `O17`.
- **`PN-15` es honesta y su prueba FALLA HOY**, como debe. `D106` retiró una disyunción que se autosatisfacía y la sustituyó por un disyunto que sólo `F5` puede cerrar. Lo ejecuté: `grep 'G2[0-3]'` sobre (a) devuelve una línea, la ficha de `INV`.
- **`D104` supera su listón donde importa.** `Q` lo intentó refutar por nueve caminos y no cayó por ninguno; yo reproduje `R1` y la derivación de las cuatro combinaciones, y **no cayó tampoco**. Es la primera de las cuatro formulaciones que **no obliga a F6 a elegir nada**.
- **El manifiesto de asignación es el primer instrumento del expediente que hace comprobable una regla de cobertura.** Sus 43 filas verifican fila a fila contra el árbol, sin una sola discrepancia, y **por primera vez la resta se puede hacer en vez de presumirse**. `O-04` queda cerrado y `C-L.5`, certificada.
- **`P` y `Q` publicaron sus derrotas.** `P` publica seis refutaciones que intentó y perdió, incluida la de `fsync` y la de `M-05`; `Q` retiró dos sospechas y declaró que su evaluación provisional decía SUFICIENTE. **Que `P` haya publicado sus seis derrotas es lo que me permitió reconstruir por qué su séptima —`P-03`— tampoco se sostiene.**
- **Y lo que quiero que no se lea de menos, con las palabras de `Q`:** «*Mis quince hallazgos son MEDIOS y MENORES, ninguno GRAVE ni BLOQUEANTE, y todos se cierran propagando material que el corpus ya tiene escrito.*» Lo verifiqué, y es cierto de los veinticuatro. **Ésta es, con distancia, la candidata más sólida que este corpus ha producido.** No falla por concepción, no falla por cobertura y no falla por lo que decidió. Falla, otra vez, en la mitad de los sitios donde sus decisiones tenían que llegar — y esta vez la mitad que falta incluye la página que un agente lee cuando escribe «Continúa».

```text
ÁRBOL AL CERRAR   git status --porcelain  →  VACÍO
HEAD AL CERRAR    18cbfb57fe2286bb68011a31a8f3d07556d7aea9   (idéntico al de apertura)
COMMIT JUZGADO    7764cca69c9fbb7c3e89b70efdae7d6990f6c3b6
ÁRBOL JUZGADO     03116b33bf4d8e996d8eccae51db927f4667ca58
NINGÚN HALLAZGO SE HA CORREGIDO EN ESTA PASADA, y es deliberado.
```

**`F4c` sigue ABIERTA. `F5` NO queda autorizada. `C-L.5` queda CERTIFICADA por primera vez.**

---

## 8 · Los 21 hallazgos del documento 20, adjudicados

Un solo estado cada uno, sin estados compuestos. **El motivo verificado de cada fila está en la
adjudicación literal de `R`, sección 7 · §9.** Aquí van los estados y el recuento derivado.

| id | estado |
|---|---|
| `M-01` | **SUPERADO** |
| `M-02` | **SUPERADO** |
| `M-03` | **SUPERADO** |
| `M-04` | **FALLIDO** |
| `M-05` | **SUPERADO** |
| `M-06` | **SUPERADO** |
| `M-07` | **SUPERADO** |
| `M-08` | **SUPERADO** |
| `M-09` | **REGISTRADO PARA F5** |
| `M-10` | **SUPERADO** |
| `M-11` | **SUPERADO** |
| `M-12` | **SUPERADO** |
| `N-01` | **SUPERADO** |
| `N-02` | **SUPERADO** |
| `N-03` | **REGISTRADO PARA F5** |
| `N-04` | **CONTRATADO PARA F6** |
| `N-05` | **SUPERADO** |
| `O-01` | **SUPERADO** |
| `O-02` | **SUPERADO** |
| `O-03` | **SUPERADO** |
| `O-04` | **SUPERADO** |

```text
RECUENTO DERIVADO DE LAS FILAS DE ARRIBA, no copiado

  SUPERADO                17   M-01 M-02 M-03 M-05 M-06 M-07 M-08 M-10 M-11 M-12
                               N-01 N-02 N-05 · O-01 O-02 O-03 O-04
  FALLIDO                   1   M-04
  REGISTRADO PARA F5        2   M-09 · N-03
  CONTRATADO PARA F6        1   N-04
  ABIERTO                   0
  NO APLICABLE              0
                           ──
                           21   los veintiún ids, cada uno EXACTAMENTE UNA VEZ
```

**Los cuatro bloqueantes del gate anterior —`M-01`, `M-02`, `M-03` y `N-01`— están los cuatro
SUPERADOS**, verificados por `R` uno a uno y con mecanismo, no con prosa.

**`M-04` es FALLIDO, y es la única discrepancia de `R` con `Q` y con el checkpoint.** `R` la
argumenta y declara su punto débil: las **cuatro refutaciones nombradas** de `M-04` están
cerradas —las reprodujo—, pero `M-04` no es una lista de cuatro fixtures, es la **proposición**
«se puede construir un árbol defectuoso que pase 30/30 en verde», y esa proposición **sigue
siendo verdadera**: `Q-04` la demuestra con un árbol que contiene una copia íntegra del catálogo
de procesos y un contrato que declara por escrito que contradice a `C4`. `R` deja escrito que si
alguien sostiene que un hallazgo se cierra cerrando sus instancias nombradas, `M-04` sería
SUPERADO y `Q-04` un hallazgo nuevo — **y que el veredicto no cambiaría por eso.**

## 9 · Los hallazgos de este gate

`P` emitió **8**, `Q` **15**, `R` **4 propios**. Tres son el mismo defecto hallado por los dos
revisores desde lotes disjuntos y sin verse: `P-01`≡`Q-13`, `P-02`≡`Q-06`, `P-05`≡`Q-08`.

```text
8 + 15 + 4 − 3 solapes  =  24 HALLAZGOS DISTINTOS
```

| severidad final | nº | ids |
|---|---|---|
| **BLOQUEANTE** | **0** | — |
| **GRAVE** | **1** | `P-05`≡`Q-08` |
| **MEDIO** | **12** | `P-01`≡`Q-13` · `P-02`≡`Q-06` · `P-04` · `P-06` · `Q-01` · `Q-02` · `Q-04` · `Q-05` · `Q-07` · `Q-14` · `R-02` · `R-03` |
| **MENOR** | **11** | `P-03` · `P-07` · `P-08` · `Q-03` · `Q-09` · `Q-10` · `Q-11` · `Q-12` · `Q-15` · `R-01` · `R-04` |
| | **24** | recuento derivado de las filas, no escrito aparte |

**Severidades ADJUDICADAS, no las que propusieron los revisores.** `R` regraduó cuatro:
`P-03` de GRAVE a MENOR **rechazando su tesis**, `P-08` de GRAVE a MENOR **declarando falsa su
premisa de hecho**, `P-07` de MEDIO a MENOR, y `P-05`≡`Q-08` a **GRAVE** —`Q` lo daba MEDIO—
por dos puntos que ninguno de los dos revisores vio.

**El rechazo de `P-03` es la resolución más consecuente de este gate, y va dicha entera.** `P`
fundaba su **primera razón de veredicto** en que la idempotencia de `W17` descansa en una regla
escrita en una sola sede y contradicha por dos sedes canónicas. `R` abrió las cinco sedes y
**cuatro de las cinco afirmaciones son falsas**: `predecesor = id(abandonada)` aparece **tres**
veces en §2.6.9; la regla de unicidad que `P` da por ausente **está escrita en L4406** con su
nombre y su motivo; **dos arranques no pueden emitir dos `deriva`** porque el paso 0 comprueba la
existencia por `abandonada_id` **antes de emitir**; y `predecesor` es campo **común** a todo
evento, de modo que su ausencia de una fila de campos específicos no es un silencio sino la
estructura de la tabla. Sobrevive un residuo menor —`R-01`—: una justificación redundante que se
apoya en un razonamiento que §2.8 retiró. **`D105` no deja el segundo terminal inconstruible; lo
deja construible, guardado y verificado.**

## 10 · Discrepancias entre P y Q, y su resolución

Ninguna resultó irresoluble: **las seis se resuelven abriendo la fuente**, y `R` las resolvió
así. El detalle está en su §8.

| # | discrepancia | resolución de `R` |
|---|---|---|
| **D-1** | `N-04`: `P` lo declara SUPERADO; `Q`, CONTRATADO PARA F6 | **a favor de `Q`** — cifra reanclada a 21 en sede vigente, derivación contratada como CONTRATO 1bis, propietario `PLT`, fase F6, dentro de `C-L.10`; `RECUENTOS-generado.md` sigue sin contar perfiles |
| **D-2** | `O-04`: `P` lo declara SUPERADO; `Q` distingue la causa del estado de `C-L.5` | **la precisión de `Q` y el resultado de `P`** — la causa era que `asignado − leído` no fuera calculable; hoy lo es y `R` lo calculó: **∅**. `O-04` SUPERADO y **`C-L.5` CERTIFICADA** |
| **D-3** | `P-03` frente al silencio de `Q` | **contra `P`** — «que `Q` no lo hallara no es evidencia; que las cinco sedes lo desmientan, sí» |
| **D-4** | `P-08`: `P` cuenta siete fuentes sin abrir; `Q` no registra laguna de cobertura | **contra `P` en el hecho** — las siete fueron leídas íntegras en el gate anterior. Sobrevive sólo la mitad formal: `D106` no fija de dónde se deriva «obligatorias» |
| **D-5** | `M-04`: `Q` lo pone entre los SUPERADOS; `P` no lo adjudica | **contra los dos** — FALLIDO, con su límite declarado |
| **D-6** | severidad de `P-05`≡`Q-08`: `P` GRAVE, `Q` MEDIO | **GRAVE** — por el punto 2 y el punto 3, que ninguno vio, y porque es la sede de entrada |

## 11 · Las siete condiciones de suficiencia

| # | condición | resultado |
|---|---|---|
| 1 | `asignadas − leídas = ∅` | **SE CUMPLE** |
| 2 | `C-L.5` **certificada** | **SE CUMPLE, y es la primera vez** |
| 3 | `D104`–`D106` superan el intento adversarial | **NO SE CUMPLE** |
| 4 | los cuatro bloqueantes del gate anterior superados | **SE CUMPLE** |
| 5 | ningún pendiente de F5/F6 exige inventar arquitectura | **SE CUMPLE** |
| 6 | ninguna contradicción material vigente sin registrar | **NO SE CUMPLE** |
| 7 | la batería no ofrece falsos verdes en `R1`–`R4` | **SE CUMPLE** |

**La condición 3 falla por `D104`, y no por su arquitectura.** `R` deja escrito primero que
`D104` es una buena decisión y que la reprodujo: las cuatro vías operan, la propietaria **hace
fallar** `G-15`, el discriminante es estructural, las cuatro combinaciones de `AUD` se derivan,
`DIR` entra por la misma regla sin excepción escrita y **no hay décimo par**. Lo que falla son
**dos de sus cuatro pilares declarados**, y `R` los falsó contra el árbol: el pilar (ii) —«los
campos de prosa **NO se leen**»— es falso del troceado real, que es un `re.findall` sobre un
segmento de texto y no un parseo YAML (`Q-05`); y el pilar (iv) —el ancla de posición— **no
normaliza**, contra la declaración del propio `D104` de que la normalización a la capacidad base
«ES TODA LA INFERENCIA QUE HAY» (`Q-02`). **Las dos pasan en verde.**

**`D105` supera su intento adversarial**, y con holgura: `R` intentó tumbarlo por el camino de
`P-03` y no cayó. **`D106` supera el suyo**: su prueba de `PN-15` falla hoy, y `R` lo comprobó
ejecutándola.

**La condición 6 falla por siete contradicciones materiales vigentes y sin registrar**, todas
verificadas contra fichero y línea, **y tres de ellas son la segunda o tercera recurrencia de la
misma frase**:

```text
1  X54 dice «diecisiete» · §2.6.5 dice DIECIOCHO y lo deriva de 18 filas     P-01 ≡ Q-13
2  capa B L4360 «DECLARA SU deriva» · D105 lo invirtió, y L4406 lo dice bien  P-02 ≡ Q-06
   — y §2.6.9 L1941 invoca la capa B para una regla que la capa B no escribe  R-03
3  CHECKPOINT L1142 cuenta 9 ventanas RC-1–RC-9 · 11-ARQ:8672 dice que NO
   se cuentan · y el propio L1641 declara M-8 corregido POR RETIRARLAS       P-04
4  «Siguiente acción exacta»: CINCO afirmaciones falsas, sin marca de
   histórica, en la sede que se autodesigna punto de entrada — y una de
   ellas reproduce M-06 en la tanda que declara M-06 corregido      P-05 ≡ Q-08 + R-02
5  PN-15 declara «cero apariciones de G20/G21/G23 en el documento 11»
   y hay 13 · 11 · 14, introducidas por el propio bloque que lo niega        P-06
6  §16 L7887 «PN-6 a PN-14» = DOCE · L8447 dice TRECE · L8687 dice bien
   «PN-6 a PN-15» — y omite justo la presión que va al Owner                 Q-07
7  C-L.3 descrita en el registro reanudable con la regla de D103 que M-01
   refutó, y D104 no aparece en NINGUNA de sus seis sedes                    Q-14
```

**Las cuatro refutaciones prescritas `R1`–`R4` fueron reproducidas por `R` en copias de `/tmp`**,
sobre `git archive` del `HEAD`, sin tocar el repositorio:

```text
BASELINE                                                   30/30 EN VERDE
R1  proceso:SIS → propietario_global "SEG"      28/30   FALLA G-15 (+G-23 lateral)
R2  segunda proyección «SEIS procesos, DIEZ pares»  29/30   FALLA G-15, y SÓLO G-15
R3  C-L.12 movida a CORREGIDAS con contadores    29/30   FALLA G-16, y SÓLO G-16
R4  .git ausente + D67 reescrita + doc 18 volteado  26/30   FALLAN G-11 G-21 G-22 G-23
```

**Las cuatro refutan, y en `R2` y `R3` falla la comprobación responsable SOLA.** La condición 7
se cumple. Lo que la condición 7 **no** cubre, y este gate deja probado, son **tres falsos verdes
fuera de `R1`–`R4`**: `Q-01`, `Q-04` y `Q-05`.

---

## 12 · Veredicto

> Es el veredicto **literal** del adjudicador `R`, y el único de este gate. `P` y `Q` recomendaron
> lo mismo, cada uno por su cuenta, y ninguno de los tres lo funda en la cobertura.

# INSUFICIENTE PARA F5

**`F4c` NO se cierra. Sigue ABIERTA. `F5` NO queda autorizada. No se ha corregido nada.**

**Cuatro razones. Las dos primeras son, cada una, una condición de suficiencia incumplida; las
dos últimas explican por qué no son formalismos.**

1. **La condición 6 no se cumple: quedan SIETE contradicciones materiales vigentes y sin
   registrar.** Entre ellas, la sección que el checkpoint designa como **punto de entrada** y que
   contiene **cinco afirmaciones falsas a la vez**. Tres son segunda o tercera recurrencia de la
   misma frase, y en tres de ellas lo omitido es exactamente **lo que va al Owner**.
2. **La condición 3 no se cumple: `D104` no supera íntegro el intento adversarial.** Su
   arquitectura resiste; **dos de sus cuatro pilares declarados son falsables contra el árbol**, y
   las dos falsaciones **pasan en verde**.
3. **La única garantía mecánica sigue produciendo falsos verdes, y el contraejemplo es peor que
   los anteriores:** `30/30 EN VERDE` sobre un árbol con una **copia íntegra del catálogo de
   procesos** y un contrato que **declara por escrito que contradice a `C4`**. Y `G-11b` —el de
   mayor alcance de los que dependen de Git, ochenta y seis filas— es **el único que no falla
   cerrado**.
4. **Y la razón de método.** De los veinticuatro hallazgos, **la mayoría los introdujo o los dejó
   pasar esta misma tanda**, y tres son la enésima reaparición de una frase ya corregida. `P-05`
   punto 3 lo enseña en su forma más pura: **la tanda que declara `M-06` corregido reproduce
   `M-06` en la sede de entrada del mismo fichero.**

**Lo que expresamente NO fundamenta este veredicto:**

- **NO falla por cobertura.** `C-L.5` queda **CERTIFICADA por primera vez**, y `R` la certifica.
- **NO falla por los cuatro bloqueantes del gate anterior.** Los cuatro SUPERADOS.
- **NO falla por `D105`**, que resiste el ataque más duro que se le hizo.
- **NO falla porque nada esté construido.** Ninguna razón es la ausencia de runtime, piloto,
  adaptadores certificados o adopción de PesquerApp. `R` verificó que están declaradas con
  propietario y fase.
- **NO falla porque quede arquitectura por inventar.** Ninguno de los veinticuatro hallazgos
  exige decidir diseño.

## 13 · Qué consta a favor, y no es cortesía

- **`D105` es la mejor decisión que este expediente ha producido** —`R`—: tres alternativas
  comparadas en tabla, elegida la mínima con el motivo escrito de por qué se descartan las otras
  dos. Cierra `M-02`, `M-03` y `O-03` de una vez, **sobrevivió al ataque de `P` y al de `R`**, y
  no añade ni un evento, ni un tipo, ni un campo.
- **Los cuatro bloqueantes anteriores están cerrados con mecanismo:** la vía propietaria **hace
  fallar** `G-15`, las cuatro combinaciones de `AUD` se derivan, el ancla ya no presupone `VER`,
  `DIR` entra por la misma regla **sin excepción escrita**, `deriva_emitida` está PROHIBIDO, el
  `fsync` del `deriva` **con su directorio** existe, y el paso 0 completa en vez de prohibir.
- **`M-12` cerrado y comprobado sin `.git`:** `G-21`, `G-22` y `G-23` fallan **cerrado**, con
  diagnóstico. **`M-11` cerrado y su control positivo dispara.** **`O-02` cerrado:** los dos
  censos escritos a mano desaparecieron y el mensaje de éxito se **deriva**.
- **La disciplina de inmutabilidad se cumple sin excepción:** `git diff --numstat 652ab8e..HEAD`
  sobre el registro da **169 inserciones y CERO supresiones**. `D1`–`D103` conservan su texto,
  `O1`–`O16` están intactas, los documentos 15–18 sin tocar.
- **El addendum de `O16` es un acto de honestidad poco frecuente:** no retro-fecha nada;
  **empeora su propia posición para ser exacto**, y no reescribe `O16` ni crea `O17`.
- **`PN-15` es honesta y su prueba FALLA HOY**, como debe. `D106` retiró una disyunción que se
  autosatisfacía y la sustituyó por un disyunto que sólo `F5` puede cerrar.
- **`D104` supera su listón donde importa.** `Q` intentó refutarlo **por nueve caminos** —tras
  derivar el catálogo por su cuenta, a ciegas, y coincidir exactamente— y no cayó por ninguno:
  «La cuarta formulación es la buena.» Es la primera que **no obliga a F6 a elegir nada**.
- **El manifiesto de asignación es el primer instrumento del expediente que hace comprobable una
  regla de cobertura.** Sus 43 filas verifican fila a fila contra el árbol sin una discrepancia, y
  **por primera vez la resta se puede hacer en vez de presumirse**.
- **`P` y `Q` publicaron sus derrotas.** `P` publica seis refutaciones que intentó y perdió; `Q`
  retiró dos sospechas y declaró que su evaluación provisional decía SUFICIENTE. `R`: «Que `P`
  haya publicado sus seis derrotas es lo que me permitió reconstruir por qué su séptima tampoco
  se sostiene.»
- **Y lo que no debe leerse de menos**, con las palabras de `Q`: «Mis quince hallazgos son MEDIOS
  y MENORES, ninguno GRAVE ni BLOQUEANTE, y todos se cierran propagando material que el corpus ya
  tiene escrito.» `R` lo verificó y lo extiende a los veinticuatro: **ésta es, con distancia, la
  candidata más sólida que este corpus ha producido.** No falla por concepción, no falla por
  cobertura y no falla por lo que decidió. Falla, otra vez, en la mitad de los sitios donde sus
  decisiones tenían que llegar — y esta vez la mitad que falta incluye la página que un agente lee
  cuando escribe «Continúa».

## 14 · Ningún hallazgo se ha corregido, y es deliberado

```text
MODO DE LOS TRES REVISORES   SÓLO LECTURA. git status --porcelain vacío al abrir y al cerrar
                             en los tres. Todos los experimentos, en copias bajo /tmp.
HEAD DURANTE TODO EL GATE    18cbfb57fe2286bb68011a31a8f3d07556d7aea9   sin cambios
COMMIT JUZGADO               7764cca69c9fbb7c3e89b70efdae7d6990f6c3b6
ÁRBOL JUZGADO                03116b33bf4d8e996d8eccae51db927f4667ca58
FICHEROS DEL REPOSITORIO MODIFICADOS DURANTE EL GATE   ninguno
COMMITS DURANTE EL GATE      ninguno · PUSH  ninguno · PR  ninguno · MERGE  ninguno
```

Los veinticuatro hallazgos de este gate y el `M-04` FALLIDO **quedan abiertos**. Quien los
corrija no podrá certificarlos, y la corrección deberá pasar por un gate posterior con revisores
que no la hayan aplicado.

**`F4c` sigue ABIERTA. `F5` NO queda autorizada. `C-L.5` queda CERTIFICADA por primera vez.**
