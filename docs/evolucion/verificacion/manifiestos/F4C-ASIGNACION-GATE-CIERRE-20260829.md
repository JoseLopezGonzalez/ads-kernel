# MANIFIESTO PREVIO DE ASIGNACIÓN — GATE INDEPENDIENTE DE CIERRE DE F4c

> **EMITIDO ANTES DE REPARTIR.**
>
> Este documento se escribe y se commitea **antes de crear o contactar a ningún revisor**.
> Una vez commiteado **no se modifica**. Si hiciera falta ampliar una asignación, se publica
> un **ADDENDUM** nuevo con su motivo, commiteado antes de entregar la fuente adicional.

## 1 · Objeto del reparto

```text
COMMIT CANDIDATO   7764cca69c9fbb7c3e89b70efdae7d6990f6c3b6
TREE SHA           03116b33bf4d8e996d8eccae51db927f4667ca58
REFERENCIA REMOTA  refs/heads/review/f4c-post-gate-cobertura-candidate-20260829
FECHA              2026-08-29
RAMA DEL GATE      gate/f4c-cierre-con-manifiestos-20260829, creada en ese commit exacto,
                   sin upstream
```

## 2 · Identidad prevista de los revisores

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

## 3 · Dos rutas del encargo que no existen, y cómo se resuelven

El encargo asigna a `P` dos contratos por títulos que **no existen en el árbol**:
`C1-ESTADOS-Y-TRANSICIONES.md` y `C7-INTEGRACION-DISTRIBUIDA.md`. Los contratos `C1` y `C7`
reales son `C1-EQUIPO-ROL-AGENTE-METODO.md` y `C7-GOBIERNO-GIT-MULTI-SOURCE.md`, **y son
inequívocos por número: hay exactamente uno de cada**. Se asignan esos, y consta aquí en
lugar de resolverse en silencio.

## 4 · Reparto, fuente a fuente

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

## 5 · Totales derivados

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

## 6 · Regla de cierre, declarada por delante

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

## 7 · Por qué existe este documento

Lo exige `D106`, y lo exige porque el gate anterior no pudo cerrar su propia regla. Su
adjudicador `O` declaró la cláusula más dura de `C-L.5` **NO CERTIFICABLE**: los tres
revisores habían declarado con honestidad qué leyeron y qué no, y **ninguno declaró qué se
le había asignado**, con lo que `asignado − leído` no era calculable. Es `O-04`.

**Con este manifiesto, esa resta es calculable por primera vez.**
