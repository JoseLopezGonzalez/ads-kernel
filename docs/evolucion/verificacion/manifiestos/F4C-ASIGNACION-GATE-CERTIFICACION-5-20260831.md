# MANIFIESTO PREVIO DE ASIGNACIÓN — QUINTO GATE DE CERTIFICACIÓN DE F4c

> **EMITIDO ANTES DE REPARTIR**, commiteado **solo**, y **después de cerrar todo
> `verificacion/`**. Una vez commiteado no se modifica.
>
> **Y estrena el remedio del defecto que INVALIDÓ el gate anterior.** Aquél no falló por el
> corpus ni por la batería ni por la candidata: falló porque **el coordinador transcribió el
> sobre a mano** y las cinco transcripciones difirieron en ocho campos. Desde este gate **el
> sobre no se transcribe**: se emite UNA vez a un fichero fuera del repositorio auditado, y
> **cada revisor lo lee de ahí, verbatim e idéntico por construcción**.

## 1 · Objeto del reparto

```text
COMMIT CANDIDATO   8c9ca9c3920000bdf327cef7a6dbaf9aeff4eaeb
TREE SHA           91fe62d369152f9d1b58361f0ffc888358364175
REFERENCIA REMOTA  refs/heads/review/f4c-perimetro-derivado-candidate-20260831
FECHA              2026-08-31
RAMA DEL GATE      gate/f4c-certificacion-5-20260831, creada en ese commit exacto
QUÉ TRAE           el perímetro DERIVADO en vez de enumerado —la clase, no los tres casos
                   que el cuarto gate encontró—; el fixture insatisfacible de `G-31`
                   invocando de verdad; `read-tree`+`checkout-index` en lugar de
                   `git archive`, que honraba `export-ignore`; las afirmaciones falsas del
                   instrumento retiradas; `D105` propagado a las OCHO sedes que faltaban,
                   `X55` incluida; y la NOTA DE ALCANCE que `O19` decía haber escrito
ESTADO DECLARADO   APLICADO y NO CERTIFICADO · `F4c` ABIERTA · `F5` NO autorizada ·
                   `M-04` NO superada · `C-L.5` ABIERTA · `C-L.7` NO CERRADA
```

## 2 · El universo obligatorio se DERIVA

```bash
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py
```

```text
UNIVERSO DERIVADO   74 fuentes · 66 747 líneas —sobre el árbol del GATE—
QUÉ CAMBIÓ          `docs/owner/` y `manifiestos/` dejan de ser rutas literales y pasan a
                    ser ZONAS BARRIDAS: entran los DOS documentos del Owner que el
                    `ENCARGO` no nombraba y el manifiesto del gate en curso. Es el remedio
                    que el adjudicador `AA` determinó para su propio hallazgo
```

## 3 · Los agentes

```text
REVISOR BB    arquitectura, protocolo, registro y punto de entrada. `BB1`·`BB2`·`BB3`·`BB4`
REVISOR CC    el instrumento y la voz del Owner. `CC1`·`CC2`·`CC3`
ADJUDICADOR DD  recibe los dos dictámenes YA CERRADOS y **los sobres que los revisores
              declaran**. Comprueba que sean IDÉNTICOS campo a campo y **declara INVÁLIDO
              el gate ante cualquier diferencia entre sobres**. No resuelve por mayoría.

INDEPENDENCIA ninguno de los ocho ha escrito F4, aplicado `D16`–`D108`, sido autor de
              ninguna corrección, ni sido revisor `A`–`AA` de ningún gate anterior.
              `BB` y `CC` en paralelo y sin verse; `DD` sin ver nada hasta que los dos cierran
```

**El coste de las cadenas:** el lote de lectura son **30704 líneas**, y sólo el documento 11 son
11 504. **Ningún ojo único recorre esas 11 504 líneas seguidas**, y el adjudicador lo pesa.

**Y una disciplina que el cuarto gate impuso:** cada relevo entrega **manifiesto de lectura de
todas sus fuentes**. `ASIGNADO − LEÍDO = 1` fue una de las razones de aquel veredicto.

## 4 · Reparto para LECTURA ÍNTEGRA

| # | ruta | líneas | SHA-256 | `1bis` | revisor | relevo |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 205 | `c29c16aca4f2ef32998713cf9a09daffc70d7824870c77f239584f92f857bdd8` | v | **BB+DD** | BB3 · DD |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11504 | `3b7c3dd54f1b7abde2a7b4c8049064a5c4ca3915f8f0901d14c285ab164d64d7` | iii | **BB** | BB1 L1-L5800 · BB2 L5801-final |
| 3 | `docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md` | 2754 | `e8431c653cb7919e8d2ec82c5b4d3d11247a01aa61577bb8e5dd266916fb0e5d` | iv | **BB+CC+DD** | BB4 · CC3 · DD — DESPUÉS de las fuentes |
| 4 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 4085 | `8433bf23d559801fa3cfada1818996c2849521421545aa5e7eae33b4ce88e2bf` | iii | **BB+DD** | BB3 · DD |
| 5 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 483 | `448f8b36d39be88ec46178742e75208c4bcd743030cfc5e4a71ed2c049674a7e` | v | **CC** | CC2 |
| 6 | `docs/evolucion/verificacion/README.md` | 355 | `d2f2298a6dbf9003a8183641945dcd611c45a5078ef4affdfeca27a3b4bae839` | v | **CC** | CC1 |
| 7 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 3621 | `dce55353edc9c0a472dc6e47c17d3f903c2e508127ae87d21c4f10c0cb55ddf4` | v | **CC** | CC1 |
| 8 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 703 | `107fbb03f4440969508d93b3084bd6a2782735faa308129f78dbc3f45bf78633` | v | **CC** | CC2 |
| 9 | `docs/evolucion/verificacion/emitir-sobre-de-ancla.py` | 688 | `f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715` | v | **CC** | CC2 |
| 10 | `docs/evolucion/verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` | 119 | `b1c29244dfedc139ff7e80a6167d200803d054f25554c75f31303fea5687a434` | v | **CC** | CC2 |
| 11 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` | 240 | `c64a0ec4731e6d27751469e84cbcc33104bfe535c42efe4f98533f4d84a0b970` | v | **CC** | CC2 |
| 12 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` | 316 | `fc4d1c2fdedbcb13be512e88303e21eddbeb194f6cc38b8e50fa0612dad08bbc` | v | **CC** | CC2 |
| 13 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md` | 210 | `ac9e0edd59cf3e1b783b42ce0fc052e1eb28af7d5d66e218709d76589f724988` | v | **CC** | CC2 |
| 14 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md` | 221 | `fc4902591eff43bc6736f626fdf2dd1bef7c4f193b1be31f3ddf26f436adb599` | v | **CC** | CC2 |
| 15 | `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | 3343 | `64d170f5acc151445eff6f3f68a0bade91d00744dffa6bdf36c13cd2d366bd3e` | v | **CC** | CC3 |
| 16 | `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | 597 | `48412108f711204f5389e17fac974133e848737676eb4c57ba5b22c6a37ab8b0` | v | **CC** | CC3 |
| 17 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1260 | `036e2fb3366c807374ad55e902c4ea9cea242422c2f8f0a12505de4902cfbde8` | iii | **BB** | BB3 |

## 5 · Fuentes AGOTADAS

```text
1  un gate anterior declara LEÍDO ÍNTEGRO DE ESA RUTA, con FILA PROPIA, citado con
   documento y línea. Una declaración de CONJUNTO no agota nada
2  los BYTES idénticos a los del árbol que ESE gate leyó DE VERDAD
3  si no se cumplen las dos, no se agota
```

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
| 12 | `docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md` | 3478 | `3e2bdece758e6b69d6695bb52f20d21b910a123a27ac643845dbad75e8355f1c` | iv | documento **23**, L860 · árbol `c36d2ba` |
| 13 | `docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md` | 2913 | `0f81f13d8cb319d8ccc5243d19bb26d7f71f57e860cde2eb2edefe33b6993dc2` | iv | documento **25**, L878 · árbol `82d8783` |
| 14 | `docs/evolucion/24-TERCER-GATE-DE-CERTIFICACION-F4C.md` | 2515 | `8df584529c857c071954b0d1b426faff82277e29a43556abe5dccfd93714fae1` | iv | documento **25**, L879 · árbol `82d8783` |
| 15 | `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | 2163 | `a88609167dbbea2818b7f2e68cbd4c6fc704cb7e2245ee0a2c873052486fd159` | i | documento **22**, L2642 · árbol `4d231ee` |
| 16 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md` | 140 | `c843b0c341183859b7f0f07db78cc67eade7ef98c4a96ad3edee23c769d2a976` | v | documento **22**, L1577 · árbol `4d231ee` |
| 17 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 334 | `db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a` | v | documento **25**, L1735 · árbol `82d8783` |
| 18 | `docs/rediseno/CHECKPOINT-OPERATIVO.md` | 195 | `d2131faa4aeddc6d66e98f5eb88d6d9d172a8910b174a1866eecc969633818bb` | v | documento **23**, L859 · árbol `c36d2ba` |
| 19 | `docs/rediseno/a-CAPACIDADES-APROBADA.md` | 1132 | `10cafb5ceee44f576d327ce614c14c86eb7b22ff43c3dfb82918b785eb36fb04` | v | documento **22**, L277 · árbol `4d231ee` |
| 20 | `docs/rediseno/a-ENMIENDA-E1-ENC.md` | 211 | `18dae19523b25ed4a2370ea9c1d23d68beb578f9365bd54587d2f2821093d4da` | ii+v | documento **21**, L395 · árbol `7764cca` |
| 21 | `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | 230 | `9d5a23806fc33fc1d76ba6be9b46ae3499c729c1f11203f80b32550c658ed2eb` | ii+v | documento **21**, L396 · árbol `7764cca` |
| 22 | `docs/rediseno/b-RECORRIDO-APROBADA.md` | 1288 | `f8cb974316e283fa2f16f9ecdd3b94ac19bf4a20cf5816cd155a2449f02719b4` | v | documento **22**, L278 · árbol `4d231ee` |
| 23 | `kernel/KERNEL.md` | 1590 | `aa635dff79e73fe13e271cb115653ebc042dc834d32007c634c8ee1df07e3150` | v | documento **22**, L279 · árbol `4d231ee` |
| 24 | `kernel/operativo/capacidades/APR/CAPACIDAD.md` | 95 | `a8709115309095849707e2d42290631dca6b3de95d49cc2c3c7ffa4e0546d708` | ii | documento **22**, L1588 · árbol `4d231ee` |
| 25 | `kernel/operativo/capacidades/ARQ/CAPACIDAD.md` | 104 | `6ca11b5f09883e24834f770e61963ae69ca738770ffb1de64f7be0afe4757a47` | ii | documento **22**, L1589 · árbol `4d231ee` |
| 26 | `kernel/operativo/capacidades/CON/CAPACIDAD.md` | 107 | `e0f79e6c3a467302c3d16aa5ee4ccb45583daf146d1676b2b06995419656c5d5` | ii | documento **22**, L1590 · árbol `4d231ee` |
| 27 | `kernel/operativo/capacidades/DIS/CAPACIDAD.md` | 147 | `06f019010d45771fd2a125f9f08f88159b45f15e9f83fd2404c7f2a23f32ad06` | ii | documento **22**, L1591 · árbol `4d231ee` |
| 28 | `kernel/operativo/capacidades/DOM/CAPACIDAD.md` | 135 | `926c7144cb098caaa0b87cdebb5c49b955b74832bc238e66d501ecbb2a635bb3` | ii | documento **22**, L1592 · árbol `4d231ee` |
| 29 | `kernel/operativo/capacidades/DSP/CAPACIDAD.md` | 152 | `acb292f882e77d74693caaab3e392a0d691e988cf875ca4394c59f859ebe7937` | ii | documento **22**, L1593 · árbol `4d231ee` |
| 30 | `kernel/operativo/capacidades/ENC/CAPACIDAD.md` | 174 | `f71b8e43f6e2d66f0801d53ce6e018806d33ef9b5ad5b3300bf1d38fe834d946` | ii | documento **22**, L1594 · árbol `4d231ee` |
| 31 | `kernel/operativo/capacidades/ENT/CAPACIDAD.md` | 123 | `91a81d3cf1cbfa619b7b69553a01810d7074b419fc7e2efb5f8ff2f8f9e7f9ed` | ii | documento **22**, L1595 · árbol `4d231ee` |
| 32 | `kernel/operativo/capacidades/INV/CAPACIDAD.md` | 96 | `47412638e7552da14b7bb89e590aea2f37cc61116c83b902e32952647380ed36` | ii | documento **22**, L1596 · árbol `4d231ee` |
| 33 | `kernel/operativo/capacidades/PLT/CAPACIDAD.md` | 108 | `a5f87977c58ed1d0d4deb3504d664a47fc90382a9790986e5aa277f1dad130d2` | ii | documento **22**, L1597 · árbol `4d231ee` |
| 34 | `kernel/operativo/capacidades/PRD/CAPACIDAD.md` | 105 | `e83b0e08272e219db0c5cc2e17b6d1a95dc4304a9f381d3acfe9c76ff528e3b3` | ii | documento **22**, L1598 · árbol `4d231ee` |
| 35 | `kernel/operativo/capacidades/SEG/CAPACIDAD.md` | 135 | `19bfd38a7a24b57fbec8365327926f7e281092a9e33a06e59355cfda5a5e5a13` | ii | documento **22**, L1599 · árbol `4d231ee` |
| 36 | `kernel/operativo/capacidades/SIS/CAPACIDAD.md` | 119 | `02089f36d124435669b7cf14cf46abd1365a860a4842b739663310b8ceb41628` | ii | documento **22**, L1600 · árbol `4d231ee` |
| 37 | `kernel/operativo/capacidades/USO/CAPACIDAD.md` | 94 | `65f144e4a5c756ef97596a997673d7ad73c194ee6936e616bafd434302ff5d0d` | ii | documento **22**, L1601 · árbol `4d231ee` |
| 38 | `kernel/operativo/capacidades/VER/CAPACIDAD.md` | 135 | `91a16b482629daf3455a3c6963a0568a7a68bcd2bd5553e7540d8c9edbfaf0e2` | ii | documento **22**, L1602 · árbol `4d231ee` |
| 39 | `kernel/operativo/contratos/00-INDICE.md` | 29 | `0b9562119f0b5b5c3f59e66c09446129fbe56865983d6424b76825bf570d004c` | v | documento **22**, L280 · árbol `4d231ee` |
| 40 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | 161 | `825f15a914c10d6f07f74e62967f93743efcf629a13379acb3947e70e2952ffa` | v | documento **22**, L281 · árbol `4d231ee` |
| 41 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | 539 | `3ee58ca4bc47988d4e6bdd652e2ea5de79ebcf8be79270664c0bd4b4cf391510` | ii+v | documento **21**, L399 · árbol `7764cca` |
| 42 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | 150 | `d56bf6b81e0fe4a9b3ba811f1adf57748cbae65692db557d15960c8506f84234` | ii+v | documento **21**, L400 · árbol `7764cca` |
| 43 | `kernel/operativo/contratos/C4-MATERIALIZACION.md` | 170 | `670289180e59b176743571a22f22047d20792db266b6426c1c91bd2fd3c1ee81` | ii+v | documento **21**, L401 · árbol `7764cca` |
| 44 | `kernel/operativo/contratos/C5-HANDOFF.md` | 115 | `af6f1a4c4f5def8da0dcecee8ea57c17516b41bbbd4abe963460c21024cc7b9e` | v | documento **22**, L282 · árbol `4d231ee` |
| 45 | `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` | 336 | `14805a79aeb07f314a55913864ee7d359ead05a932d59b207b66b6279d3a41e9` | v | documento **22**, L283 · árbol `4d231ee` |
| 46 | `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | 250 | `83f82e2be4756a4651e61f1883d2a99f1d141954097a6e4176a3482a951fc69c` | v | documento **22**, L284 · árbol `4d231ee` |
| 47 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | 141 | `08f4bea44594e026aee24cdddc93765cba0fa5c197b26adee0a0cad00d2c366a` | ii | documento **22**, L1603 · árbol `4d231ee` |
| 48 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | 352 | `dd323d1aa2f7ede3efa18ac01564b636fff8f0f77beac7db3abed667bbd429ec` | ii | documento **22**, L1604 · árbol `4d231ee` |
| 49 | `kernel/operativo/diseno/02-RUBRICAS.md` | 343 | `8aa8fb18426eac219c275c102f757d50727da2e363d905529c8c061d6721d842` | ii | documento **22**, L1605 · árbol `4d231ee` |
| 50 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | 130 | `5d2f54535c1334c053e27bf99b6b81a15a33be7180adf58ddf884cf79ef3a9c1` | ii | documento **22**, L1606 · árbol `4d231ee` |
| 51 | `kernel/operativo/diseno/05-FIDELIDAD.md` | 129 | `fdabb29f7592e603e755c12f191d189755e795ecee104c9b5f583b1ead56e441` | ii | documento **22**, L1607 · árbol `4d231ee` |
| 52 | `kernel/operativo/entrada/00-INDICE.md` | 28 | `315b2790cb66bb4c2c84272468675c8e77fb5a26b8cc2b95ff56db7ee266ddb1` | ii | documento **21**, L1056 · árbol `7764cca` |
| 53 | `kernel/operativo/entrada/02-CIRCUITO.md` | 145 | `750d39a29f05e7f2b037f9c246c9869ba80edec493e104e206baadda19c09c70` | ii | documento **21**, L1057 · árbol `7764cca` |
| 54 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | 187 | `1716bd3d8b48107d28a93e4297a6d93c0e6125107c0cc14811f092641e3d0cd2` | ii | documento **21**, L1058 · árbol `7764cca` |
| 55 | `kernel/operativo/esquemas/proceso.yaml` | 49 | `bd391d5acddff1342ce307829dfb8494df535dbd1924d44948d1e17176440dcc` | v | documento **22**, L1580 · árbol `4d231ee` |
| 56 | `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` | 130 | `f56e8fe4872e46b5ccc8bd2b9531cdc9e53247aaec1e36ebcae131efbe3674ac` | v | documento **22**, L1579 · árbol `4d231ee` |
| 57 | `kernel/operativo/recorrido/01-PROCESOS.md` | 564 | `98b5cbc836121044a1b3b38690331325cd730ac71d1f30da69482937c392ee85` | v | documento **22**, L1578 · árbol `4d231ee` |

## 6 · Totales derivados

```text
FUENTES OBLIGATORIAS       74          LÍNEAS OBLIGATORIAS   66 747
ASIGNADAS A LECTURA         17   30704 líneas
ASIGNADAS COMO AGOTADAS     57   36043 líneas
OBLIGATORIO menos ASIGNADO   0     CERO FUENTES SIN ASIGNAR
ASIGNADO menos LEÍDO         —     la calcula el adjudicador `DD`
```

## 7 · Lo que este gate tiene que juzgar

```text
· **el SOBRE, y su ENTREGA.** Se entrega desde un fichero externo al repositorio, idéntico
  para todos por construcción. ¿Lo es? ¿Sigue siendo externo? ¿Qué prueba y qué no?
· `M-04` COMO PROPOSICIÓN GENERAL. El gate anterior encontró SEIS árboles en verde y uno
  nuevo del adjudicador. **Busca el siguiente.** Y respeta que `C` —actor privilegiado—
  NO es exigible dentro de `F4c`: es contrato de `F6`. Cuentan `A` y `B`
· el perímetro derivado: ¿cierra la CLASE, o sólo los tres casos?
· la SEDE CANÓNICA y los otros dos documentos del Owner, que entran por primera vez
· los 36 hallazgos del documento 25: cuáles están cerrados
· `C-L.5`, que llega ABIERTA · `C-L.7`, NO CERRADA · `C-L.3`
· y lo que el Owner prohíbe como evidencia primaria: mensajes de commit, paráfrasis del
  coordinador, una fila derivada del registro, o afirmaciones internas
```

## 8 · Regla de cierre

```text
CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA.
CUALQUIER DIFERENCIA ENTRE LOS SOBRES DE DOS REVISORES INVALIDA EL GATE.
LA SEDE CANÓNICA que no coincida con la huella recibida FALLA CERRADO.

EL VEREDICTO es uno de estos dos literales:
    SUFICIENTE PARA F5
    INSUFICIENTE PARA F5

EL ADJUDICADOR NO CORRIGE.
```
