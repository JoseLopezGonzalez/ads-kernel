# MANIFIESTO PREVIO DE ASIGNACIÓN — SEGUNDO GATE DE CERTIFICACIÓN DE F4c

> **EMITIDO ANTES DE REPARTIR.** Se escribe y se commitea **solo, y antes de crear o
> contactar a ningún revisor**. Una vez commiteado **no se modifica**: si hiciera falta
> reasignar, se publica un ADDENDUM nuevo con su motivo. Lo exige `D106` y lo regula
> `C-L.5` · `1bis`.

## 1 · Objeto del reparto

```text
COMMIT CANDIDATO   e3163967e2eb8191294ce79c25af7d10220a0944
TREE SHA           2451141c40e1bba7823528edd2df073af92a4037
REFERENCIA REMOTA  refs/heads/review/f4c-o17-candidate-20260830
FECHA              2026-08-30
RAMA DEL GATE      gate/f4c-certificacion-2-20260830, creada en ese commit exacto, sin upstream
QUÉ TRAE ESTA      la resolución `O17` del Owner y su propagación `D107`; los 68 hallazgos
CANDIDATA          de clase A del documento 22; QUINCE protecciones sistémicas nuevas en la
                   batería, que pasa de 30 a 37 comprobaciones; `PN-17` y `PN-18`; y un
                   CORRIGENDUM de dictámenes inmutables
ESTADO DECLARADO   APLICADO y NO CERTIFICADO · `F4c` ABIERTA · `F5` NO autorizada ·
                   `C-L.5` CERTIFICADA · `M-04` FALLIDA hasta que un gate diga otra cosa
```

## 2 · El universo obligatorio se DERIVA, y el comando se publica

```bash
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py
```

Publicado y commiteado **antes que este manifiesto y en un commit propio** (`6b5d3e6`), como
en el gate anterior. Lee los cinco componentes de `1bis` de su **sede normativa** y **falla
cerrado con código 2** si una sede no se lee, si un recuento no coincide con el que su sede
declara o si una ruta derivada no existe.

```text
UNIVERSO DERIVADO   64 fuentes · 47 728 líneas
QUÉ CAMBIÓ          el componente (iv) —«todo dictamen de gate anterior»— incorporó SOLO el
                    documento 22, derivado del título de su H1: **nadie escribió su nombre en
                    ninguna lista**. El componente (v) creció con el aparato que el gate
                    anterior produjo: sus dos manifiestos inmutables, el CORRIGENDUM y **el
                    propio derivador, que pasa a juzgarse a sí mismo**
```

## 3 · Los agentes, y su independencia

```text
REVISOR S     arquitectura, protocolo y registro. Cadena `S1`·`S2`·`S3`·`S4`.
              Foco: `O17` y su propagación real a los CUATRO macrocircuitos · §9.6 ·
              el sujeto de seis identificadores · la reutilización de evidencia ·
              `D107` declarada derivada · `W17`/`W8`/punto 7 · `PN-17` y `PN-18` ·
              el addendum de `D97` · `C-L.3` y `C-L.5`

REVISOR T     el instrumento. Cadena `T1`·`T2`·`T3`.
              Foco: **`M-04` como proposición general** · las QUINCE protecciones ·
              si generalizan o vuelven a cerrar sólo su perímetro · el derivador
              juzgándose a sí mismo · los manifiestos y el CORRIGENDUM

ADJUDICADOR U recibe los dos dictámenes YA CERRADOS. Recalcula por sí mismo universo,
              asignaciones, lecturas, cobertura, severidades, recuentos y condiciones de
              cierre. Verifica cada hallazgo contra fichero y línea. **No resuelve por
              mayoría** y **no corrige nada**

INDEPENDENCIA ninguno de los ocho ha escrito F4, aplicado `D16`–`D107`, sido autor de
              ninguna corrección, ni sido revisor `A`–`R` ni `P1`–`Q5` de ningún gate
              anterior. **Ninguno participó en el gate del documento 22.** `S` y `T`
              trabajan EN PARALELO y sin verse; `U` no ve nada hasta que los dos cierran
```

**Por qué cadenas, y qué cuesta.** El lote de lectura son **21 530 líneas**, y sólo el
documento 11 son 10 275. Un lector único no las sostiene en contexto limpio **y las lee
íntegras**. Se declara el coste, igual que en el gate anterior: **ningún ojo único recorre las
10 275 líneas seguidas**, y el adjudicador tiene que pesarlo.

**El orden es obligatorio: primero las FUENTES, después los HALLAZGOS.** El documento 22 está
asignado a `S4`, a `T3` y a `U`, y **sólo se abre cuando el resto del lote está leído**.

## 4 · Reparto para LECTURA ÍNTEGRA

Todo derivado del árbol `2451141c40e1bba7823528edd2df073af92a4037`, nada copiado.

| # | ruta | líneas | SHA-256 | `1bis` | revisor | relevo |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 148 | `004cad57881dc75d08cae8311c5e9b4334cd7c424330769657fcf11d3557ab1b` | v | **T+U** | T2 · U |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 10275 | `47f924c9a2b5c36df111ca325f83c18f161db383a0b14acb44e84e8d0ddeddf3` | iii | **S** | S1 L1-L5200 · S2 L5201-final |
| 3 | `docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md` | 3478 | `3e2bdece758e6b69d6695bb52f20d21b910a123a27ac643845dbad75e8355f1c` | iv | **S+T+U** | S4 · T3 · U — DESPUÉS de las fuentes |
| 4 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 2782 | `e9078a7434d2a8a898d0d4edec242aee7fcac289c8f1dea3dfcf0f669c5b8a7a` | iii | **S+U** | S3 · U |
| 5 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 131 | `274192d416368cb5a7ec3a0b07bc2e5dd97fffb5502c21d4dd3be5703c20b0ea` | v | **T** | T2 |
| 6 | `docs/evolucion/verificacion/README.md` | 133 | `7b9fae2c65f1e2311c68218110d87aa64aac84ae66c0855d8a0e4309b4f22de4` | v | **T** | T1 |
| 7 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 2685 | `5f39512d16594e2c103a432db5a1bcae736b7bfe397ac7e078b7d1bfe1fe14db` | v | **T** | T1 |
| 8 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 410 | `6753a245103dcc5a558bfb39336c0e43b5e032d146dd03f7ded4861c0f5659a8` | v | **T** | T2 |
| 9 | `docs/evolucion/verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` | 119 | `b1c29244dfedc139ff7e80a6167d200803d054f25554c75f31303fea5687a434` | v | **T** | T2 |
| 10 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` | 316 | `fc4d1c2fdedbcb13be512e88303e21eddbeb194f6cc38b8e50fa0612dad08bbc` | v | **T** | T2 |
| 11 | `docs/rediseno/CHECKPOINT-OPERATIVO.md` | 195 | `d2131faa4aeddc6d66e98f5eb88d6d9d172a8910b174a1866eecc969633818bb` | v | **T** | T2 |
| 12 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 858 | `73e40d95cb2688ba1a83307ba27640400dd5a4fc8835c3eaf59173b99cb9cb02` | iii | **S** | S3 |

## 5 · Fuentes AGOTADAS por lectura íntegra CERTIFICADA en un gate anterior

**La regla de agotamiento, la misma que el gate anterior y con la corrección que su propio
`ADDENDUM 1` le impuso:**

```text
1  un gate anterior tiene que declarar LEÍDO ÍNTEGRO DE ESA RUTA, con fila propia, y se
   cita con documento y línea. Una declaración de CONJUNTO no agota nada: es el defecto
   que el ADDENDUM 1 del gate anterior tuvo que reparar pagando 3 575 líneas de lectura
2  los BYTES de la candidata tienen que ser IDÉNTICOS a los del árbol que ese gate leyó
3  si no se cumplen las dos, la fuente NO se agota. No hay tercera vía y no hay presunción
```

**Las DOCE fuentes que esta tanda tocó vuelven al reparto de lectura, y ahí están** —el
documento 11, el registro de decisiones, el checkpoint, el índice, la batería, su README, el
derivador, el `CHECKPOINT-OPERATIVO`, los dos manifiestos, el CORRIGENDUM y el documento 22—.
**Ninguna se agota.**

| # | ruta | líneas | SHA-256 | `1bis` | lectura íntegra certificada en |
|---|---|---|---|---|---|
| 1 | `docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md` | 336 | `202ac1af8df5ca6e032cb06f6566c63cf2656fb1a54d65a8c9a0f5d0ef5d41d9` | iv | documento **22**, L1583 · árbol `4d231ee` |
| 2 | `docs/evolucion/12-CRITICA-INDEPENDIENTE-F4.md` | 764 | `c50e0aa6c1b9827c166171efee1737b2e091cc5518d78bad8c469c709c0dd56f` | iv | documento **22**, L1584 · árbol `4d231ee` |
| 3 | `docs/evolucion/13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md` | 797 | `6804d134dfb66b5304ec9c539750559e578a2d5855785b5803189baac2da931f` | iv | documento **22**, L1585 · árbol `4d231ee` |
| 4 | `docs/evolucion/14-DEVOLUCION-TECNICA-PREVIA-F4C.md` | 325 | `7f94e236f3cfb11e78762a301d9a3e94939ab47df34658710d1b8686ed7050fb` | iv | documento **22**, L1586 · árbol `4d231ee` |
| 5 | `docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` | 651 | `b0e015c118ceb916e58fc8191b2a5e40cf28c44dd426618fdd49d10e3ea495d6` | ii+iv | documento **22**, L1587 · árbol `4d231ee` |
| 6 | `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | 1257 | `8243034f286160cc89330af95b49f558af0dd16d1b36a37ccbdf02f74a79d185` | i+iv | documento **21**, L381 · árbol `7764cca` |
| 7 | `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` | 1650 | `18f876d4cd47a2f7cfde15594f98696cfacf750607cd23811dd40ffb36d6c29c` | i+iv | documento **21**, L382 · árbol `7764cca` |
| 8 | `docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` | 3665 | `1e71366b10d2293802db435de14953771ebd8fc13b426acedd7c0efe21cdb496` | i+iv | documento **21**, L383 · árbol `7764cca` |
| 9 | `docs/evolucion/19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md` | 1152 | `48baaa1a8e69c6ef3401eb7a0088dcf06849bd66fa3f238bf3e7b8c8fd14392d` | iv | documento **22**, L1581 · árbol `4d231ee` |
| 10 | `docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md` | 801 | `d7d2e4fa3f878e0c010d979e89affdb63462cc6fdd6628ed885d3a760bde09d1` | iv | documento **22**, L1582 · árbol `4d231ee` |
| 11 | `docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md` | 2679 | `9f869ffbdbdb834ca872c03abc8826c125a47b4344ed32cd9b6266db08f8be03` | iv+v | documento **22**, L275 · árbol `4d231ee` |
| 12 | `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | 2163 | `a88609167dbbea2818b7f2e68cbd4c6fc704cb7e2245ee0a2c873052486fd159` | i | documento **22**, L2642 · árbol `4d231ee` |
| 13 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md` | 140 | `c843b0c341183859b7f0f07db78cc67eade7ef98c4a96ad3edee23c769d2a976` | v | documento **22**, L1577 · árbol `4d231ee` |
| 14 | `docs/rediseno/a-CAPACIDADES-APROBADA.md` | 1132 | `10cafb5ceee44f576d327ce614c14c86eb7b22ff43c3dfb82918b785eb36fb04` | v | documento **22**, L277 · árbol `4d231ee` |
| 15 | `docs/rediseno/a-ENMIENDA-E1-ENC.md` | 211 | `18dae19523b25ed4a2370ea9c1d23d68beb578f9365bd54587d2f2821093d4da` | ii+v | documento **21**, L395 · árbol `7764cca` |
| 16 | `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | 230 | `9d5a23806fc33fc1d76ba6be9b46ae3499c729c1f11203f80b32550c658ed2eb` | ii+v | documento **21**, L396 · árbol `7764cca` |
| 17 | `docs/rediseno/b-RECORRIDO-APROBADA.md` | 1288 | `f8cb974316e283fa2f16f9ecdd3b94ac19bf4a20cf5816cd155a2449f02719b4` | v | documento **22**, L278 · árbol `4d231ee` |
| 18 | `kernel/KERNEL.md` | 1590 | `aa635dff79e73fe13e271cb115653ebc042dc834d32007c634c8ee1df07e3150` | v | documento **22**, L279 · árbol `4d231ee` |
| 19 | `kernel/operativo/capacidades/APR/CAPACIDAD.md` | 95 | `a8709115309095849707e2d42290631dca6b3de95d49cc2c3c7ffa4e0546d708` | ii | documento **22**, L1588 · árbol `4d231ee` |
| 20 | `kernel/operativo/capacidades/ARQ/CAPACIDAD.md` | 104 | `6ca11b5f09883e24834f770e61963ae69ca738770ffb1de64f7be0afe4757a47` | ii | documento **22**, L1589 · árbol `4d231ee` |
| 21 | `kernel/operativo/capacidades/CON/CAPACIDAD.md` | 107 | `e0f79e6c3a467302c3d16aa5ee4ccb45583daf146d1676b2b06995419656c5d5` | ii | documento **22**, L1590 · árbol `4d231ee` |
| 22 | `kernel/operativo/capacidades/DIS/CAPACIDAD.md` | 147 | `06f019010d45771fd2a125f9f08f88159b45f15e9f83fd2404c7f2a23f32ad06` | ii | documento **22**, L1591 · árbol `4d231ee` |
| 23 | `kernel/operativo/capacidades/DOM/CAPACIDAD.md` | 135 | `926c7144cb098caaa0b87cdebb5c49b955b74832bc238e66d501ecbb2a635bb3` | ii | documento **22**, L1592 · árbol `4d231ee` |
| 24 | `kernel/operativo/capacidades/DSP/CAPACIDAD.md` | 152 | `acb292f882e77d74693caaab3e392a0d691e988cf875ca4394c59f859ebe7937` | ii | documento **22**, L1593 · árbol `4d231ee` |
| 25 | `kernel/operativo/capacidades/ENC/CAPACIDAD.md` | 174 | `f71b8e43f6e2d66f0801d53ce6e018806d33ef9b5ad5b3300bf1d38fe834d946` | ii | documento **22**, L1594 · árbol `4d231ee` |
| 26 | `kernel/operativo/capacidades/ENT/CAPACIDAD.md` | 123 | `91a81d3cf1cbfa619b7b69553a01810d7074b419fc7e2efb5f8ff2f8f9e7f9ed` | ii | documento **22**, L1595 · árbol `4d231ee` |
| 27 | `kernel/operativo/capacidades/INV/CAPACIDAD.md` | 96 | `47412638e7552da14b7bb89e590aea2f37cc61116c83b902e32952647380ed36` | ii | documento **22**, L1596 · árbol `4d231ee` |
| 28 | `kernel/operativo/capacidades/PLT/CAPACIDAD.md` | 108 | `a5f87977c58ed1d0d4deb3504d664a47fc90382a9790986e5aa277f1dad130d2` | ii | documento **22**, L1597 · árbol `4d231ee` |
| 29 | `kernel/operativo/capacidades/PRD/CAPACIDAD.md` | 105 | `e83b0e08272e219db0c5cc2e17b6d1a95dc4304a9f381d3acfe9c76ff528e3b3` | ii | documento **22**, L1598 · árbol `4d231ee` |
| 30 | `kernel/operativo/capacidades/SEG/CAPACIDAD.md` | 135 | `19bfd38a7a24b57fbec8365327926f7e281092a9e33a06e59355cfda5a5e5a13` | ii | documento **22**, L1599 · árbol `4d231ee` |
| 31 | `kernel/operativo/capacidades/SIS/CAPACIDAD.md` | 119 | `02089f36d124435669b7cf14cf46abd1365a860a4842b739663310b8ceb41628` | ii | documento **22**, L1600 · árbol `4d231ee` |
| 32 | `kernel/operativo/capacidades/USO/CAPACIDAD.md` | 94 | `65f144e4a5c756ef97596a997673d7ad73c194ee6936e616bafd434302ff5d0d` | ii | documento **22**, L1601 · árbol `4d231ee` |
| 33 | `kernel/operativo/capacidades/VER/CAPACIDAD.md` | 135 | `91a16b482629daf3455a3c6963a0568a7a68bcd2bd5553e7540d8c9edbfaf0e2` | ii | documento **22**, L1602 · árbol `4d231ee` |
| 34 | `kernel/operativo/contratos/00-INDICE.md` | 29 | `0b9562119f0b5b5c3f59e66c09446129fbe56865983d6424b76825bf570d004c` | v | documento **22**, L280 · árbol `4d231ee` |
| 35 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | 161 | `825f15a914c10d6f07f74e62967f93743efcf629a13379acb3947e70e2952ffa` | v | documento **22**, L281 · árbol `4d231ee` |
| 36 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | 539 | `3ee58ca4bc47988d4e6bdd652e2ea5de79ebcf8be79270664c0bd4b4cf391510` | ii+v | documento **21**, L399 · árbol `7764cca` |
| 37 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | 150 | `d56bf6b81e0fe4a9b3ba811f1adf57748cbae65692db557d15960c8506f84234` | ii+v | documento **21**, L400 · árbol `7764cca` |
| 38 | `kernel/operativo/contratos/C4-MATERIALIZACION.md` | 170 | `670289180e59b176743571a22f22047d20792db266b6426c1c91bd2fd3c1ee81` | ii+v | documento **21**, L401 · árbol `7764cca` |
| 39 | `kernel/operativo/contratos/C5-HANDOFF.md` | 115 | `af6f1a4c4f5def8da0dcecee8ea57c17516b41bbbd4abe963460c21024cc7b9e` | v | documento **22**, L282 · árbol `4d231ee` |
| 40 | `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` | 336 | `14805a79aeb07f314a55913864ee7d359ead05a932d59b207b66b6279d3a41e9` | v | documento **22**, L283 · árbol `4d231ee` |
| 41 | `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | 250 | `83f82e2be4756a4651e61f1883d2a99f1d141954097a6e4176a3482a951fc69c` | v | documento **22**, L284 · árbol `4d231ee` |
| 42 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | 141 | `08f4bea44594e026aee24cdddc93765cba0fa5c197b26adee0a0cad00d2c366a` | ii | documento **22**, L1603 · árbol `4d231ee` |
| 43 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | 352 | `dd323d1aa2f7ede3efa18ac01564b636fff8f0f77beac7db3abed667bbd429ec` | ii | documento **22**, L1604 · árbol `4d231ee` |
| 44 | `kernel/operativo/diseno/02-RUBRICAS.md` | 343 | `8aa8fb18426eac219c275c102f757d50727da2e363d905529c8c061d6721d842` | ii | documento **22**, L1605 · árbol `4d231ee` |
| 45 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | 130 | `5d2f54535c1334c053e27bf99b6b81a15a33be7180adf58ddf884cf79ef3a9c1` | ii | documento **22**, L1606 · árbol `4d231ee` |
| 46 | `kernel/operativo/diseno/05-FIDELIDAD.md` | 129 | `fdabb29f7592e603e755c12f191d189755e795ecee104c9b5f583b1ead56e441` | ii | documento **22**, L1607 · árbol `4d231ee` |
| 47 | `kernel/operativo/entrada/00-INDICE.md` | 28 | `315b2790cb66bb4c2c84272468675c8e77fb5a26b8cc2b95ff56db7ee266ddb1` | ii | documento **21**, L1056 · árbol `7764cca` |
| 48 | `kernel/operativo/entrada/02-CIRCUITO.md` | 145 | `750d39a29f05e7f2b037f9c246c9869ba80edec493e104e206baadda19c09c70` | ii | documento **21**, L1057 · árbol `7764cca` |
| 49 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | 187 | `1716bd3d8b48107d28a93e4297a6d93c0e6125107c0cc14811f092641e3d0cd2` | ii | documento **21**, L1058 · árbol `7764cca` |
| 50 | `kernel/operativo/esquemas/proceso.yaml` | 49 | `bd391d5acddff1342ce307829dfb8494df535dbd1924d44948d1e17176440dcc` | v | documento **22**, L1580 · árbol `4d231ee` |
| 51 | `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` | 130 | `f56e8fe4872e46b5ccc8bd2b9531cdc9e53247aaec1e36ebcae131efbe3674ac` | v | documento **22**, L1579 · árbol `4d231ee` |
| 52 | `kernel/operativo/recorrido/01-PROCESOS.md` | 564 | `98b5cbc836121044a1b3b38690331325cd730ac71d1f30da69482937c392ee85` | v | documento **22**, L1578 · árbol `4d231ee` |

## 6 · Totales derivados, y las DOS restas de `1bis`

```text
FUENTES OBLIGATORIAS        64     derivadas, no elegidas
LÍNEAS OBLIGATORIAS     47 728

ASIGNADAS A LECTURA         12     21 530 líneas · lotes complementarios de `S` y `T`
ASIGNADAS COMO AGOTADAS     52     26 608 líneas · con fila propia, documento, línea y
                                   bytes idénticos, en el documento 21 o en el 22

OBLIGATORIO menos ASIGNADO   0     CERO FUENTES SIN ASIGNAR
ASIGNADO menos LEÍDO         —     la calcula el adjudicador `U`. Aquí queda declarada,
                                   no presumida
```

```text
REVISOR S     4 fuentes    S1  documento 11, L1-L5200
                           S2  documento 11, L5201-final
                           S3  registro de decisiones · CHECKPOINT-ADS-NEXT
                           S4  documento 22, AL FINAL — DICTAMINADOR

REVISOR T     9 fuentes    T1  la batería · su README
                           T2  el derivador · los dos manifiestos · el CORRIGENDUM ·
                               00-INDICE · CHECKPOINT-OPERATIVO
                           T3  documento 22, AL FINAL — DICTAMINADOR

ADJUDICADOR U 3 fuentes    ESTE manifiesto · documento 22 · CHECKPOINT-ADS-NEXT ·
                           00-INDICE, más las 52 AGOTADAS, cuya identidad de bytes
                           verifica él mecánicamente
```

Los lotes de `S` y `T` son **complementarios**: ninguna fuente de lectura se asigna a los dos,
salvo el documento 22, que los dos abren **al final** y por mandato del encargo.

## 7 · Lo que este gate tiene que juzgar

```text
· `O17` propagada DE VERDAD: los cuatro macrocircuitos produciendo el nivel Estructural
  como precondición propia, con `SIS` productor, `VER` dosier, `PLT` maquinaria y `SEG`
  bloqueo; el sujeto de SEIS identificadores; la reutilización de evidencia con sus tres
  cláusulas; y si `O12` es HOY satisfacible por un recorrido completo
· que `D107` no exceda a `O17` ni elija nada que el Owner no eligió
· `M-04` COMO PROPOSICIÓN GENERAL: construir un árbol defectuoso que pase en verde.
  El gate anterior encontró OCHO. **Busca el noveno.**
· si las QUINCE protecciones GENERALIZAN o vuelven a cerrar sólo su perímetro — que es
  el defecto que el gate anterior diagnosticó y esta tanda dice haber curado
· las tres pruebas negativas: ¿fallan de verdad, o son tautologías?
· los 68 hallazgos de clase A: cuáles están cerrados y cuáles no
· `PN-17` y `PN-18`: ¿registran sin elegir?
· el addendum de `D97`: ¿acota, o sigue siendo contradicción vigente?
· el CORRIGENDUM: ¿acota sin editar?
· `C-L.3` · `C-L.5` · las presiones vigentes, derivadas
· y el derivador juzgándose a sí mismo: ¿deriva, o esconde una lista escrita a mano?
```

## 8 · Regla de cierre

```text
CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA.

Se evalúa cruzando ESTE manifiesto con los MANIFIESTOS DE LECTURA de cada revisor.
Ni un grep, ni un resumen, ni un índice, ni la asignación misma equivalen a lectura.

Una fuente AGOTADA no está exenta: su prueba es la CITA con fila propia MÁS la identidad
de bytes, y el adjudicador la recalcula.

EL VEREDICTO es uno de estos dos literales, y ninguna otra formulación vale:
    SUFICIENTE PARA F5
    INSUFICIENTE PARA F5

EL ADJUDICADOR NO CORRIGE. Adjudica y devuelve.
```
