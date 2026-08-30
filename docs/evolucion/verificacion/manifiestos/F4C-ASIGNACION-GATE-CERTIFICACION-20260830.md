# MANIFIESTO PREVIO DE ASIGNACIÓN — GATE INDEPENDIENTE DE CERTIFICACIÓN DE F4c

> **EMITIDO ANTES DE REPARTIR.**
>
> Este documento se escribe y se commitea **solo, y antes de crear o contactar a ningún
> revisor**. Una vez commiteado **no se modifica**. Si hiciera falta ampliar una asignación,
> se publica un **ADDENDUM** nuevo con su motivo, commiteado antes de entregar la fuente
> adicional. Es lo que exige `D106` y lo que `C-L.5` · `1bis` regula.

## 1 · Objeto del reparto

```text
COMMIT CANDIDATO   4d231eef4ada99b3258f698b161f0e0148087e89
TREE SHA           02ba78c5af76628006d7e7dd0d70f209feddbdbf
REFERENCIA REMOTA  refs/heads/review/f4c-post-gate-manifiestos-candidate-20260830
FECHA              2026-08-30
RAMA DEL GATE      gate/f4c-certificacion-20260830, creada en ese commit exacto, sin upstream
ESTADO DECLARADO   los 24 hallazgos del documento 21 APLICADOS y NO CERTIFICADOS ·
                   `F4c` ABIERTA · `F5` NO autorizada · `C-L.5` CERTIFICADA ·
                   `M-04` FALLIDA · `PN-16` única presión nueva · 14 presiones vigentes
```

## 2 · De dónde sale «FUENTE OBLIGATORIA» — la regla y el comando

`1bis` de `C-L.5` exige publicar **la REGLA y el COMANDO auditable** con que se materializa
el universo, «de modo que cualquiera pueda reejecutarlo y obtener el mismo universo». El
manifiesto anterior publicó una **tabla escrita a mano**, y por eso su «FUENTES SIN ASIGNAR
0» era verdadero por construcción: se cumplía escogiendo sólo lo ya asignado. Es `P-08`.

**Aquí el universo no se escribe: se deriva, y el derivador se publica con él.**

```bash
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py          # tabla
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py --md     # Markdown
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py --rutas  # sólo rutas
```

Publicado en `e645db1`, **antes que este manifiesto y en un commit propio**. Lee cada uno de
los cinco componentes de `1bis` de **su sede normativa**, no de una copia, y **falla cerrado
con código 2** si una sede no se puede leer, si un recuento derivado no coincide con el que
su sede declara o si una ruta derivada no existe en el árbol. Un universo que encoge en
silencio es exactamente el defecto que `P-08` describió.

```text
(i)    las CUATRO fuentes de «QUÉ HAY QUE LEER ÍNTEGRO»
       SEDE  `11-ARQUITECTURA-INTEGRADA.md`, la propia sección `C-L.5`, parseada
       CIERRA con excepción si no derivan exactamente cuatro

(ii)   las CATORCE fuentes de `C-0.1` y las QUINCE fichas de `C-0.2` del documento 18
       SEDE  el bloque `G-24` de `comprobar-correccion-gate-de-cierre.py`, ÚNICA sede del
             árbol que las enumera nombre a nombre y las contrasta en cada ejecución.
             Leerlas de ahí evita crear una SEGUNDA sede del mismo catálogo, que es la
             clase de defecto que `Q-04` castigó
       CIERRA con excepción si no derivan exactamente catorce y quince

(iii)  el documento 11, el registro de decisiones y el checkpoint

(iv)   todo dictamen de gate anterior
       SEDE  barrido de `docs/evolucion/NN-*.md` por el TÍTULO de su H1. Se deriva y no se
             enumera: una lista escrita a mano deja fuera el dictamen publicado después,
             que es precisamente el que nadie ha leído

(v)    el objeto que ESTE gate juzga, según su encargo
       SEDE  el bloque `ENCARGO` del derivador, con la CLÁUSULA del encargo que mete a
             cada entrada. Sin cláusula no entra
```

## 3 · Identidad prevista de los agentes, y su independencia

```text
REVISOR P     material normativo, protocolo transaccional y material APROBADO.
              Foco: `D105` · `abandonada` -> `deriva` y la DIRECCIÓN de la referencia ·
              las DIECIOCHO ventanas y `W17` · `W8` frente a `W17` · `fsync`, marcador y
              durabilidad · `PN-15`, `PN-16` y las CATORCE presiones vigentes ·
              `C-L.3` · contratos `C1`-`C7` · la afirmación de `D97` sobre `G20`/`G21`/`G23`

REVISOR Q     derivación, batería, kernel operativo y dictámenes previos.
              Foco: `D104` y las CUATRO vías tipadas · obligatorias frente a condicionales ·
              distribución exacta de vías · lector estructurado frente a prosa (`Q-05`) ·
              ancla normalizada (`Q-02`) · conjunto vigilado derivado (`Q-09`) ·
              `G-11b` fallando cerrado sin Git (`Q-01`) · catálogo y contratos duplicados y
              adiciones no rastreadas (`Q-04`) · `M-04` como PROPOSICIÓN GENERAL ·
              los 24 hallazgos del documento 21 · `C-L.5`

ADJUDICADOR R recibe los dos dictámenes YA CERRADOS, cruza asignación contra lectura,
              RECALCULA por sí mismo universo, asignaciones, lecturas, cobertura,
              severidades, recuentos y condiciones de cierre, verifica cada hallazgo
              contra fichero y línea, intenta REFUTAR activamente batería y arquitectura,
              y emite el veredicto único. **No resuelve por mayoría** y **no corrige nada**

INDEPENDENCIA EXIGIDA A TODOS — ninguno ha escrito F4, aplicado `D16`-`D106`, sido autor
              de las correcciones de ninguna tanda, ni sido revisor `A`-`R`. `P` y `Q`
              trabajan EN PARALELO y sin verse. `R` no ve ningún dictamen hasta que los dos
              están cerrados. Ninguno ha participado en ningún gate anterior
```

### 3bis · Por qué cada revisor es una CADENA DE RELEVO, y qué cambia

El universo obligatorio derivado son **41 174 líneas**, y sólo el documento 11 son 9 494.
Un único lector no puede sostener en contexto limpio el lote entero **y leerlo íntegro**;
fingir que sí es la forma exacta en que tres gates anteriores acabaron declarando cobertura
que no tenían. Por eso cada revisor se realiza como una **cadena de relevos con contexto
limpio y tramos DISJUNTOS**, declarada aquí por delante:

```text
REVISOR P   P1 · P2 · P3 · P4     P4 es el DICTAMINADOR: lee su propio lote, recibe las
                                  notas de P1-P3 y cierra el dictamen de `P`
REVISOR Q   Q1 · Q2 · Q3 · Q4     Q4 es el DICTAMINADOR, con el mismo papel
```

**Qué NO cambia.** El manifiesto de LECTURA sigue siendo uno por revisor, y es la **unión**
de los manifiestos de sus relevos: cada relevo declara ruta, líneas, SHA-256 recalculado por
él, `LEÍDO ÍNTEGRO` o los tramos exactos que no abrió, primera y última sección sustantiva y
**dos anclas de regiones separadas**. La resta `asignado menos leído` se calcula igual, y una
fuente asignada y no leída por la cadena excluye la suficiencia igual.

**Qué sí cambia, y se dice contra el propio interés:** el documento 11 lo leen `P1` y `P2` en
dos tramos consecutivos, y **ningún ojo único recorre sus 9 494 líneas seguidas**. Una
contradicción entre dos secciones muy separadas es más difícil de ver así. Se mitiga con
`grep` cruzado y con que `P4` puede reabrir cualquier región, **pero no se elimina, y el
adjudicador tiene que pesarlo**.

**El orden es obligatorio: primero las FUENTES, después los HALLAZGOS.** El documento 21
—que es donde viven los 24 hallazgos— está asignado a `P4`, a `Q4` y a `R`, y **sólo se abre
cuando el resto del lote de la cadena está leído**. Un revisor que lee primero los hallazgos
ya no busca: confirma.

## 4 · Reparto para LECTURA ÍNTEGRA en este gate

Ruta · líneas · SHA-256 · componentes de `1bis` que la meten · revisor · relevo. Todo
derivado del árbol `02ba78c5af76628006d7e7dd0d70f209feddbdbf`, nada copiado.

| # | ruta | líneas | SHA-256 | `1bis` | revisor | relevo |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 113 | `56d1cdb133108c77f87fe70d096ca2547c04cc733fe84694846b72a5cc873307` | v | **Q+R** | Q1 · R |
| 2 | `docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md` | 336 | `202ac1af8df5ca6e032cb06f6566c63cf2656fb1a54d65a8c9a0f5d0ef5d41d9` | iv | **Q** | Q3 |
| 3 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 9494 | `ebbd3311f1016c05f5f96ab1673144feecc0f1de3a55e5ac7731ce0ddab2def0` | iii | **P** | P1 L1-L4800 · P2 L4801-final |
| 4 | `docs/evolucion/12-CRITICA-INDEPENDIENTE-F4.md` | 764 | `c50e0aa6c1b9827c166171efee1737b2e091cc5518d78bad8c469c709c0dd56f` | iv | **Q** | Q3 |
| 5 | `docs/evolucion/13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md` | 797 | `6804d134dfb66b5304ec9c539750559e578a2d5855785b5803189baac2da931f` | iv | **Q** | Q3 |
| 6 | `docs/evolucion/14-DEVOLUCION-TECNICA-PREVIA-F4C.md` | 325 | `7f94e236f3cfb11e78762a301d9a3e94939ab47df34658710d1b8686ed7050fb` | iv | **Q** | Q3 |
| 7 | `docs/evolucion/19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md` | 1152 | `48baaa1a8e69c6ef3401eb7a0088dcf06849bd66fa3f238bf3e7b8c8fd14392d` | iv | **Q** | Q3 |
| 8 | `docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md` | 801 | `d7d2e4fa3f878e0c010d979e89affdb63462cc6fdd6628ed885d3a760bde09d1` | iv | **Q** | Q3 |
| 9 | `docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md` | 2679 | `9f869ffbdbdb834ca872c03abc8826c125a47b4344ed32cd9b6266db08f8be03` | iv+v | **P+Q+R** | P4 · Q4 · R — DESPUÉS de las fuentes |
| 10 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 2382 | `3b6e1f776cc0f89e3068ee3ff9a89c88f6436b68114c3e77d637402d31cef613` | iii | **Q+R** | Q1 · R |
| 11 | `docs/evolucion/verificacion/README.md` | 124 | `3f8741613a060312494f2de2d70043e70c6fea78456a61b00b2fb78f7e9f9fcb` | v | **Q** | Q2 |
| 12 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 1568 | `d245651397790f64fae51392ede29327ee23b2f28777531aaa88905d1b4c5bff` | v | **Q** | Q2 |
| 13 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md` | 140 | `c843b0c341183859b7f0f07db78cc67eade7ef98c4a96ad3edee23c769d2a976` | v | **Q** | Q2 |
| 14 | `docs/rediseno/CHECKPOINT-OPERATIVO.md` | 160 | `5f19d517ec4812e28b003202ffddbfc38885c544febf81e9456af82c7c7b51ff` | v | **Q** | Q1 |
| 15 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 725 | `3be45994f4d00e82d4a136a2140c738b926a3baee4811e757d523125e4239959` | iii | **P** | P3 |
| 16 | `docs/rediseno/a-CAPACIDADES-APROBADA.md` | 1132 | `10cafb5ceee44f576d327ce614c14c86eb7b22ff43c3dfb82918b785eb36fb04` | v | **P** | P3 |
| 17 | `docs/rediseno/b-RECORRIDO-APROBADA.md` | 1288 | `f8cb974316e283fa2f16f9ecdd3b94ac19bf4a20cf5816cd155a2449f02719b4` | v | **P** | P3 |
| 18 | `kernel/KERNEL.md` | 1590 | `aa635dff79e73fe13e271cb115653ebc042dc834d32007c634c8ee1df07e3150` | v | **P** | P4 |
| 19 | `kernel/operativo/contratos/00-INDICE.md` | 29 | `0b9562119f0b5b5c3f59e66c09446129fbe56865983d6424b76825bf570d004c` | v | **P** | P4 |
| 20 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | 161 | `825f15a914c10d6f07f74e62967f93743efcf629a13379acb3947e70e2952ffa` | v | **P** | P4 |
| 21 | `kernel/operativo/contratos/C5-HANDOFF.md` | 115 | `af6f1a4c4f5def8da0dcecee8ea57c17516b41bbbd4abe963460c21024cc7b9e` | v | **P** | P4 |
| 22 | `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` | 336 | `14805a79aeb07f314a55913864ee7d359ead05a932d59b207b66b6279d3a41e9` | v | **P** | P4 |
| 23 | `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | 250 | `83f82e2be4756a4651e61f1883d2a99f1d141954097a6e4176a3482a951fc69c` | v | **P** | P4 |
| 24 | `kernel/operativo/esquemas/proceso.yaml` | 49 | `bd391d5acddff1342ce307829dfb8494df535dbd1924d44948d1e17176440dcc` | v | **Q** | Q2 |
| 25 | `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` | 130 | `f56e8fe4872e46b5ccc8bd2b9531cdc9e53247aaec1e36ebcae131efbe3674ac` | v | **Q** | Q2 |
| 26 | `kernel/operativo/recorrido/01-PROCESOS.md` | 564 | `98b5cbc836121044a1b3b38690331325cd730ac71d1f30da69482937c392ee85` | v | **Q** | Q2 |

## 5 · Fuentes AGOTADAS por lectura íntegra CERTIFICADA en un gate anterior

`1bis` lo dice con todas las letras: «**Una lectura íntegra CERTIFICADA en un gate anterior
sigue siendo evidencia válida** y no se declara ausente: agota la parte de `C-0.1` que
cubrió, y el manifiesto la cita con el gate y la línea donde consta». Es la resolución que
el adjudicador `R` fijó al rechazar la premisa de hecho de `P-08`: `C-0.1` es condición de
**ESTADO DEL CORPUS** —«fuentes que nadie abrió»— y se agota cuando alguien independiente
las abre, no una obligación de releer 41 174 líneas por pasada.

**La regla de agotamiento que se aplica aquí, y es más dura que la que `1bis` exige:**

```text
1  un gate anterior tiene que declarar LEÍDO ÍNTEGRO DE ESA RUTA, y se cita con documento
   y línea. La fila del manifiesto de ASIGNACIÓN transcrita en un dictamen NO es una
   lectura: confundirlas es el defecto que P-08 describió, y el derivador las separa

2  los BYTES de la candidata tienen que ser IDÉNTICOS a los del árbol que ese gate leyó.
   Se comprueba con git show del árbol certificador contra el SHA-256 de la candidata.
   Si difieren, la lectura NO agota nada y la fuente vuelve al reparto de lectura

3  si no se cumplen las dos, la fuente NO se agota. No hay tercera vía y no hay presunción
```

**Las cinco fuentes del universo que CAMBIARON desde el árbol que las certificó vuelven al
reparto de §4, y ahí están**: `11-ARQUITECTURA-INTEGRADA.md` (9 280 -> 9 494 líneas),
`CHECKPOINT-ADS-NEXT.md` (2 051 -> 2 382), `00-INDICE.md`, `verificacion/README.md` y
`comprobar-correccion-gate-de-cierre.py` (1 109 -> 1 568). **Ninguna se agota.**

| # | ruta | líneas | SHA-256 | `1bis` | lectura íntegra certificada en |
|---|---|---|---|---|---|
| 1 | `docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` | 651 | `b0e015c118ceb916e58fc8191b2a5e40cf28c44dd426618fdd49d10e3ea495d6` | ii+iv | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 2 | `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | 1257 | `8243034f286160cc89330af95b49f558af0dd16d1b36a37ccbdf02f74a79d185` | i+iv | documento **21**, L381 · árbol `7764cca` · revisores `P`/`Q`/`R`, manifiesto de LECTURA |
| 3 | `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` | 1650 | `18f876d4cd47a2f7cfde15594f98696cfacf750607cd23811dd40ffb36d6c29c` | i+iv | documento **21**, L382 · árbol `7764cca` · revisores `P`/`Q`/`R`, manifiesto de LECTURA |
| 4 | `docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` | 3665 | `1e71366b10d2293802db435de14953771ebd8fc13b426acedd7c0efe21cdb496` | i+iv | documento **21**, L383 · árbol `7764cca` · revisores `P`/`Q`/`R`, manifiesto de LECTURA |
| 5 | `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | 2163 | `a88609167dbbea2818b7f2e68cbd4c6fc704cb7e2245ee0a2c873052486fd159` | i | documento **21**, L380 · árbol `7764cca` · revisores `P`/`Q`/`R`, manifiesto de LECTURA |
| 6 | `docs/rediseno/a-ENMIENDA-E1-ENC.md` | 211 | `18dae19523b25ed4a2370ea9c1d23d68beb578f9365bd54587d2f2821093d4da` | ii+v | documento **21**, L395 · árbol `7764cca` · revisores `P`/`Q`/`R`, manifiesto de LECTURA |
| 7 | `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | 230 | `9d5a23806fc33fc1d76ba6be9b46ae3499c729c1f11203f80b32550c658ed2eb` | ii+v | documento **21**, L396 · árbol `7764cca` · revisores `P`/`Q`/`R`, manifiesto de LECTURA |
| 8 | `kernel/operativo/capacidades/APR/CAPACIDAD.md` | 95 | `a8709115309095849707e2d42290631dca6b3de95d49cc2c3c7ffa4e0546d708` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 9 | `kernel/operativo/capacidades/ARQ/CAPACIDAD.md` | 104 | `6ca11b5f09883e24834f770e61963ae69ca738770ffb1de64f7be0afe4757a47` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 10 | `kernel/operativo/capacidades/CON/CAPACIDAD.md` | 107 | `e0f79e6c3a467302c3d16aa5ee4ccb45583daf146d1676b2b06995419656c5d5` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 11 | `kernel/operativo/capacidades/DIS/CAPACIDAD.md` | 147 | `06f019010d45771fd2a125f9f08f88159b45f15e9f83fd2404c7f2a23f32ad06` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 12 | `kernel/operativo/capacidades/DOM/CAPACIDAD.md` | 135 | `926c7144cb098caaa0b87cdebb5c49b955b74832bc238e66d501ecbb2a635bb3` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 13 | `kernel/operativo/capacidades/DSP/CAPACIDAD.md` | 152 | `acb292f882e77d74693caaab3e392a0d691e988cf875ca4394c59f859ebe7937` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 14 | `kernel/operativo/capacidades/ENC/CAPACIDAD.md` | 174 | `f71b8e43f6e2d66f0801d53ce6e018806d33ef9b5ad5b3300bf1d38fe834d946` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 15 | `kernel/operativo/capacidades/ENT/CAPACIDAD.md` | 123 | `91a81d3cf1cbfa619b7b69553a01810d7074b419fc7e2efb5f8ff2f8f9e7f9ed` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 16 | `kernel/operativo/capacidades/INV/CAPACIDAD.md` | 96 | `47412638e7552da14b7bb89e590aea2f37cc61116c83b902e32952647380ed36` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 17 | `kernel/operativo/capacidades/PLT/CAPACIDAD.md` | 108 | `a5f87977c58ed1d0d4deb3504d664a47fc90382a9790986e5aa277f1dad130d2` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 18 | `kernel/operativo/capacidades/PRD/CAPACIDAD.md` | 105 | `e83b0e08272e219db0c5cc2e17b6d1a95dc4304a9f381d3acfe9c76ff528e3b3` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 19 | `kernel/operativo/capacidades/SEG/CAPACIDAD.md` | 135 | `19bfd38a7a24b57fbec8365327926f7e281092a9e33a06e59355cfda5a5e5a13` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 20 | `kernel/operativo/capacidades/SIS/CAPACIDAD.md` | 119 | `02089f36d124435669b7cf14cf46abd1365a860a4842b739663310b8ceb41628` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 21 | `kernel/operativo/capacidades/USO/CAPACIDAD.md` | 94 | `65f144e4a5c756ef97596a997673d7ad73c194ee6936e616bafd434302ff5d0d` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 22 | `kernel/operativo/capacidades/VER/CAPACIDAD.md` | 135 | `91a16b482629daf3455a3c6963a0568a7a68bcd2bd5553e7540d8c9edbfaf0e2` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 23 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | 539 | `3ee58ca4bc47988d4e6bdd652e2ea5de79ebcf8be79270664c0bd4b4cf391510` | ii+v | documento **21**, L399 · árbol `7764cca` · revisores `P`/`Q`/`R`, manifiesto de LECTURA |
| 24 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | 150 | `d56bf6b81e0fe4a9b3ba811f1adf57748cbae65692db557d15960c8506f84234` | ii+v | documento **21**, L400 · árbol `7764cca` · revisores `P`/`Q`/`R`, manifiesto de LECTURA |
| 25 | `kernel/operativo/contratos/C4-MATERIALIZACION.md` | 170 | `670289180e59b176743571a22f22047d20792db266b6426c1c91bd2fd3c1ee81` | ii+v | documento **21**, L401 · árbol `7764cca` · revisores `P`/`Q`/`R`, manifiesto de LECTURA |
| 26 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | 141 | `08f4bea44594e026aee24cdddc93765cba0fa5c197b26adee0a0cad00d2c366a` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 27 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | 352 | `dd323d1aa2f7ede3efa18ac01564b636fff8f0f77beac7db3abed667bbd429ec` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 28 | `kernel/operativo/diseno/02-RUBRICAS.md` | 343 | `8aa8fb18426eac219c275c102f757d50727da2e363d905529c8c061d6721d842` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 29 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | 130 | `5d2f54535c1334c053e27bf99b6b81a15a33be7180adf58ddf884cf79ef3a9c1` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 30 | `kernel/operativo/diseno/05-FIDELIDAD.md` | 129 | `fdabb29f7592e603e755c12f191d189755e795ecee104c9b5f583b1ead56e441` | ii | documento **20**, L368 · L372 · adjudicado en L638 · árbol `c3d6465` · revisor `N`, lote propio ÍNTEGRO |
| 31 | `kernel/operativo/entrada/00-INDICE.md` | 28 | `315b2790cb66bb4c2c84272468675c8e77fb5a26b8cc2b95ff56db7ee266ddb1` | ii | documento **21**, L1056 · árbol `7764cca` · revisores `P`/`Q`/`R`, manifiesto de LECTURA |
| 32 | `kernel/operativo/entrada/02-CIRCUITO.md` | 145 | `750d39a29f05e7f2b037f9c246c9869ba80edec493e104e206baadda19c09c70` | ii | documento **21**, L1057 · árbol `7764cca` · revisores `P`/`Q`/`R`, manifiesto de LECTURA |
| 33 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | 187 | `1716bd3d8b48107d28a93e4297a6d93c0e6125107c0cc14811f092641e3d0cd2` | ii | documento **21**, L1058 · árbol `7764cca` · revisores `P`/`Q`/`R`, manifiesto de LECTURA |

## 6 · Totales derivados, y las DOS restas de `1bis`

```text
FUENTES OBLIGATORIAS        59     derivadas, no elegidas. Superconjunto ESTRICTO de las 43
                                   del manifiesto anterior: ninguna de aquéllas se pierde y
                                   entran DIECISÉIS más
LÍNEAS OBLIGATORIAS     41 174

ASIGNADAS A LECTURA         26     27 204 líneas · lotes complementarios de `P` y `Q`
ASIGNADAS COMO AGOTADAS     33     13 970 líneas · con gate y línea, y bytes idénticos

OBLIGATORIO menos ASIGNADO   0     <- la resta que `1bis` añadió, y que el manifiesto
                                      anterior no podía calcular porque su universo era
                                      elegido. CERO FUENTES SIN ASIGNAR

ASIGNADO menos LEÍDO         —     <- la de siempre, y la que EXCLUYE la suficiencia. NO se
                                      puede calcular todavía: la calcula el adjudicador `R`
                                      cruzando ESTE manifiesto con los manifiestos de
                                      LECTURA. Aquí queda declarada, no presumida
```

**Distribución del reparto de lectura, derivada de §4:**

```text
REVISOR P    10 fuentes    P1  documento 11, L1-L4800
                           P2  documento 11, L4801-final
                           P3  DECISIONES-Y-CONTRADICCIONES · (a) · (b)
                           P4  KERNEL.md · contratos/00-INDICE · C1 · C5 · C6 · C7
                               más el documento 21, AL FINAL

REVISOR Q    16 fuentes    Q1  CHECKPOINT-ADS-NEXT · CHECKPOINT-OPERATIVO · 00-INDICE
                           Q2  la batería · su README · el manifiesto previo anterior ·
                               01-PROCESOS · 00-OBLIGACIONES-Y-CIERRE · proceso.yaml
                           Q3  documentos 19 · 20 · 10 · 12 · 13 · 14
                           Q4  documento 21, AL FINAL

ADJUDICADOR R  4 fuentes   ESTE manifiesto · documento 21 · CHECKPOINT-ADS-NEXT ·
                           00-INDICE, más las 33 AGOTADAS, cuya identidad de bytes
                           verifica él mecánicamente, y cualquier fuente sobre la que
                           exista discrepancia material
```

Los lotes de `P` y `Q` son **complementarios**: ninguna fuente de lectura se asigna a los
dos, salvo el documento 21, que los dos abren **al final** y por mandato del encargo.

## 7 · Lo que este gate tiene que juzgar, dicho por delante

```text
· los 24 hallazgos del documento 21, uno a uno
· M-04 como PROPOSICIÓN GENERAL —«se puede construir un árbol defectuoso que pase la
  batería en verde»—, no sólo sus fixtures conocidos
· Q-01, Q-04 y Q-05
· las DIECIOCHO ventanas y W17
· la dirección de la referencia entre abandonada y su deriva
· W8 frente a W17
· el lector estructurado frente a la prosa
· la distribución exacta de vías, y obligatorias frente a condicionales
· el conjunto vigilado, derivado
· catálogo y contratos duplicados, y adiciones no rastreadas
· Git ausente
· las CATORCE presiones y PN-16
· el estado de C-L.3
· C-L.5
· la afirmación conservada en D97 sobre las apariciones de G20/G21/G23: el adjudicador
  debe decidir EXPRESAMENTE si funciona como registro histórico suficientemente
  identificado o si sigue siendo una contradicción vigente
```

## 8 · Regla de cierre, declarada por delante

```text
CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA.

Se evalúa cruzando ESTE manifiesto con los MANIFIESTOS DE LECTURA que cada revisor entrega
dentro de su dictamen: asignadas menos leídas íntegramente. Si ese conjunto no está vacío,
el veredicto sólo puede ser INSUFICIENTE PARA F5, con independencia de los hallazgos.

Ni un grep, ni un resumen previo, ni un índice, ni la asignación misma equivalen a lectura.
Cada relevo recalcula el SHA-256 de cada fuente que declara haber leído y aporta dos anclas
verificables de regiones separadas.

Una fuente AGOTADA no está exenta: su prueba es la CITA del gate que la leyó MÁS la
identidad de bytes, y el adjudicador la recalcula. Si una sola no coincide, deja de estar
agotada y pasa a ser asignada y no leída.

EL VEREDICTO es uno de estos dos literales, y ninguna otra formulación vale:
    SUFICIENTE PARA F5
    INSUFICIENTE PARA F5

EL ADJUDICADOR NO CORRIGE los hallazgos que encuentre. Adjudica y devuelve.
```
