# MANIFIESTO PREVIO DE ASIGNACIÓN — CUARTO GATE DE CERTIFICACIÓN DE F4c

> **EMITIDO ANTES DE REPARTIR**, commiteado **solo** y antes de crear o contactar a ningún
> revisor. Una vez commiteado **no se modifica**.
>
> **Y este gate estrena la SEDE CANÓNICA DEL OWNER.** Desde `O19`, la autoridad sobre las
> resoluciones del Owner **deja de ser la paráfrasis del coordinador** y pasa a
> [`docs/owner/ADS-OWNER-RESOLUCIONES.md`](../../../owner/ADS-OWNER-RESOLUCIONES.md). El
> sobre de ancla publica su huella, y **un gate FALLA CERRADO si la sede no coincide con la
> huella recibida externamente**.

## 1 · Objeto del reparto

```text
COMMIT CANDIDATO   dc9be3f68b3961fe4fa6010b4e446c24fc1510cb
TREE SHA           0cd9a2ef051ba2a509e13338912c17ecbed70506
REFERENCIA REMOTA  refs/heads/review/f4c-o19-sede-canonica-candidate-20260830
FECHA              2026-08-30
RAMA DEL GATE      gate/f4c-certificacion-4-20260830, creada en ese commit exacto, sin upstream
QUÉ TRAE           la RATIFICACIÓN `O19` del Owner y la SEDE CANÓNICA; la corrección de la
                   atribución en doce sedes SIN retirar contenido; el sobre anclando la sede
                   con los digest de `O17`, `O18` y `O19`; el inventario de integridad
                   extendido a `docs/owner/`; y la reparación del emisor que el tercer gate
                   exigió —leer del commit, negarse con el árbol sucio, publicar los dos
                   árboles, receta que reproduce el digest—
ESTADO DECLARADO   APLICADO y NO CERTIFICADO · `F4c` ABIERTA · `F5` NO autorizada ·
                   `M-04` NO declarada superada · `C-L.7` NO CERRADA
```

## 2 · El universo obligatorio se DERIVA, y el comando se publica

```bash
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py
```

Publicado y commiteado **antes que este manifiesto y en un commit propio**.

```text
UNIVERSO DERIVADO   70 fuentes · 58 788 líneas
QUÉ ENTRÓ NUEVO     el documento 24 por el componente (iv), derivado del título de su H1;
                    la SEDE CANÓNICA y el manifiesto del gate anterior por el componente (v)
```

## 3 · Los agentes, y su independencia

```text
REVISOR Y     arquitectura, protocolo, registro y SEDE CANÓNICA. Cadena `Y1`·`Y2`·`Y3`·`Y4`.
              Foco: `O19` y la sede canónica · si la propagación corrige la ATRIBUCIÓN sin
              cambiar el DISEÑO · si alguna paráfrasis AMPLÍA el texto canónico · `D108`
              como proyección y no como fuente de autoridad · `PN-19` · `C-L.3` · `C-L.5` ·
              `C-L.7`, que este gate hereda como NO CERRADA

REVISOR Z     el instrumento. Cadena `Z1`·`Z2`·`Z3`.
              Foco: **`M-04` como proposición general** · el emisor reparado · si el sobre
              ancla de verdad la sede · el derivador · los CUATRO manifiestos inmutables ·
              el CORRIGENDUM · el inventario de integridad extendido

ADJUDICADOR AA  recibe los dos dictámenes YA CERRADOS y los dos sobres que los revisores
              declaran. Comprueba que sean idénticos, verifica los cálculos por su cuenta y
              **declara INVÁLIDO el gate ante cualquier diferencia**. No resuelve por
              mayoría. No corrige nada.

INDEPENDENCIA ninguno de los siete ha escrito F4, aplicado `D16`–`D108`, sido autor de
              ninguna corrección, ni sido revisor `A`–`X` de ningún gate anterior.
              `Y` y `Z` en paralelo y sin verse; `AA` sin ver nada hasta que los dos cierran
```

**El coste de las cadenas, declarado:** el lote de lectura son **28507 líneas**, y sólo el
documento 11 son 11 392. **Ningún ojo único recorre esas 11 392 líneas seguidas.**

**El orden: primero el SOBRE Y LA SEDE, después las FUENTES, y sólo al final los HALLAZGOS.**
Los documentos 23 y 24 están asignados a `Y4`, a `Z3` y a `AA`, y no se abren antes.

## 4 · Reparto para LECTURA ÍNTEGRA

Todo derivado del árbol `0cd9a2ef051ba2a509e13338912c17ecbed70506`, nada copiado.

| # | ruta | líneas | SHA-256 | `1bis` | revisor | relevo |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 185 | `4f5d7d86db98298dfa39bb40472dcb466f36b6bea332859c0d644b539790f555` | v | **Y+AA** | Y3 · AA |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11392 | `893840385fbfcbf2f2a26735c9ae8b6aa87c6d823684784f6a28f2f37f5c53d7` | iii | **Y** | Y1 L1-L5700 · Y2 L5701-final |
| 3 | `docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md` | 2913 | `0f81f13d8cb319d8ccc5243d19bb26d7f71f57e860cde2eb2edefe33b6993dc2` | iv | **Y+Z+AA** | Y4 · Z3 · AA — DESPUÉS de las fuentes |
| 4 | `docs/evolucion/24-TERCER-GATE-DE-CERTIFICACION-F4C.md` | 2515 | `8df584529c857c071954b0d1b426faff82277e29a43556abe5dccfd93714fae1` | iv | **Y+Z+AA** | Y4 · Z3 · AA — DESPUÉS de las fuentes |
| 5 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 3816 | `51c5c099f290373aaf45d7d45d8ca00877ec3d1177eac9bd99df4df9db4c6430` | iii | **Y+AA** | Y3 · AA |
| 6 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 340 | `8c17aeaa018af0469f726bdd43f3a2d8ed4b5f3de8316b65227153a24b969a0d` | v | **Z** | Z2 |
| 7 | `docs/evolucion/verificacion/README.md` | 317 | `4bfce607e30db67050814d29d87a2b342482303d7f098a3d87e837d04bbef55c` | v | **Z** | Z1 |
| 8 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 3486 | `b4cb57b3349a881ae6728d77e6e4eacee653b426600621426b00127993032064` | v | **Z** | Z1 |
| 9 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 580 | `fd1d150590e5b3e4b79155b33c7513b1a99c04ba2a17d7e2b9fc562a18b12dec` | v | **Z** | Z2 |
| 10 | `docs/evolucion/verificacion/emitir-sobre-de-ancla.py` | 548 | `94ad8c38651c32bf13b197e1f7c2340ebe18f68cdf1a8cdf1a808891c9187f52` | v | **Z** | Z2 |
| 11 | `docs/evolucion/verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` | 119 | `b1c29244dfedc139ff7e80a6167d200803d054f25554c75f31303fea5687a434` | v | **Z** | Z2 |
| 12 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` | 240 | `c64a0ec4731e6d27751469e84cbcc33104bfe535c42efe4f98533f4d84a0b970` | v | **Z** | Z2 |
| 13 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` | 316 | `fc4d1c2fdedbcb13be512e88303e21eddbeb194f6cc38b8e50fa0612dad08bbc` | v | **Z** | Z2 |
| 14 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md` | 210 | `ac9e0edd59cf3e1b783b42ce0fc052e1eb28af7d5d66e218709d76589f724988` | v | **Z** | Z2 |
| 15 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 334 | `db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a` | v | **Y+AA** | Y3 · AA |
| 16 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1196 | `2e673c6e80cee0c00f5cd8db0e3b461fc957d2d3f16f972aa7f78f8cd1aa20e9` | iii | **Y** | Y3 |

## 5 · Fuentes AGOTADAS por lectura íntegra CERTIFICADA en un gate anterior

```text
1  un gate anterior tiene que declarar LEÍDO ÍNTEGRO DE ESA RUTA, con FILA PROPIA, y se
   cita con documento y línea. Una declaración de CONJUNTO no agota nada
2  los BYTES tienen que ser IDÉNTICOS a los del árbol que ESE gate leyó DE VERDAD — la rama
   del gate, no una tanda de corrección posterior
3  si no se cumplen las dos, la fuente NO se agota
```

**Las DIECISÉIS que esta tanda tocó vuelven al reparto de lectura**, la sede canónica entre
ellas —es nueva y nadie la ha leído—. **Ninguna se agota.**

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
| 13 | `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | 2163 | `a88609167dbbea2818b7f2e68cbd4c6fc704cb7e2245ee0a2c873052486fd159` | i | documento **22**, L2642 · árbol `4d231ee` |
| 14 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md` | 140 | `c843b0c341183859b7f0f07db78cc67eade7ef98c4a96ad3edee23c769d2a976` | v | documento **22**, L1577 · árbol `4d231ee` |
| 15 | `docs/rediseno/CHECKPOINT-OPERATIVO.md` | 195 | `d2131faa4aeddc6d66e98f5eb88d6d9d172a8910b174a1866eecc969633818bb` | v | documento **23**, L859 · árbol `c36d2ba` |
| 16 | `docs/rediseno/a-CAPACIDADES-APROBADA.md` | 1132 | `10cafb5ceee44f576d327ce614c14c86eb7b22ff43c3dfb82918b785eb36fb04` | v | documento **22**, L277 · árbol `4d231ee` |
| 17 | `docs/rediseno/a-ENMIENDA-E1-ENC.md` | 211 | `18dae19523b25ed4a2370ea9c1d23d68beb578f9365bd54587d2f2821093d4da` | ii+v | documento **21**, L395 · árbol `7764cca` |
| 18 | `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | 230 | `9d5a23806fc33fc1d76ba6be9b46ae3499c729c1f11203f80b32550c658ed2eb` | ii+v | documento **21**, L396 · árbol `7764cca` |
| 19 | `docs/rediseno/b-RECORRIDO-APROBADA.md` | 1288 | `f8cb974316e283fa2f16f9ecdd3b94ac19bf4a20cf5816cd155a2449f02719b4` | v | documento **22**, L278 · árbol `4d231ee` |
| 20 | `kernel/KERNEL.md` | 1590 | `aa635dff79e73fe13e271cb115653ebc042dc834d32007c634c8ee1df07e3150` | v | documento **22**, L279 · árbol `4d231ee` |
| 21 | `kernel/operativo/capacidades/APR/CAPACIDAD.md` | 95 | `a8709115309095849707e2d42290631dca6b3de95d49cc2c3c7ffa4e0546d708` | ii | documento **22**, L1588 · árbol `4d231ee` |
| 22 | `kernel/operativo/capacidades/ARQ/CAPACIDAD.md` | 104 | `6ca11b5f09883e24834f770e61963ae69ca738770ffb1de64f7be0afe4757a47` | ii | documento **22**, L1589 · árbol `4d231ee` |
| 23 | `kernel/operativo/capacidades/CON/CAPACIDAD.md` | 107 | `e0f79e6c3a467302c3d16aa5ee4ccb45583daf146d1676b2b06995419656c5d5` | ii | documento **22**, L1590 · árbol `4d231ee` |
| 24 | `kernel/operativo/capacidades/DIS/CAPACIDAD.md` | 147 | `06f019010d45771fd2a125f9f08f88159b45f15e9f83fd2404c7f2a23f32ad06` | ii | documento **22**, L1591 · árbol `4d231ee` |
| 25 | `kernel/operativo/capacidades/DOM/CAPACIDAD.md` | 135 | `926c7144cb098caaa0b87cdebb5c49b955b74832bc238e66d501ecbb2a635bb3` | ii | documento **22**, L1592 · árbol `4d231ee` |
| 26 | `kernel/operativo/capacidades/DSP/CAPACIDAD.md` | 152 | `acb292f882e77d74693caaab3e392a0d691e988cf875ca4394c59f859ebe7937` | ii | documento **22**, L1593 · árbol `4d231ee` |
| 27 | `kernel/operativo/capacidades/ENC/CAPACIDAD.md` | 174 | `f71b8e43f6e2d66f0801d53ce6e018806d33ef9b5ad5b3300bf1d38fe834d946` | ii | documento **22**, L1594 · árbol `4d231ee` |
| 28 | `kernel/operativo/capacidades/ENT/CAPACIDAD.md` | 123 | `91a81d3cf1cbfa619b7b69553a01810d7074b419fc7e2efb5f8ff2f8f9e7f9ed` | ii | documento **22**, L1595 · árbol `4d231ee` |
| 29 | `kernel/operativo/capacidades/INV/CAPACIDAD.md` | 96 | `47412638e7552da14b7bb89e590aea2f37cc61116c83b902e32952647380ed36` | ii | documento **22**, L1596 · árbol `4d231ee` |
| 30 | `kernel/operativo/capacidades/PLT/CAPACIDAD.md` | 108 | `a5f87977c58ed1d0d4deb3504d664a47fc90382a9790986e5aa277f1dad130d2` | ii | documento **22**, L1597 · árbol `4d231ee` |
| 31 | `kernel/operativo/capacidades/PRD/CAPACIDAD.md` | 105 | `e83b0e08272e219db0c5cc2e17b6d1a95dc4304a9f381d3acfe9c76ff528e3b3` | ii | documento **22**, L1598 · árbol `4d231ee` |
| 32 | `kernel/operativo/capacidades/SEG/CAPACIDAD.md` | 135 | `19bfd38a7a24b57fbec8365327926f7e281092a9e33a06e59355cfda5a5e5a13` | ii | documento **22**, L1599 · árbol `4d231ee` |
| 33 | `kernel/operativo/capacidades/SIS/CAPACIDAD.md` | 119 | `02089f36d124435669b7cf14cf46abd1365a860a4842b739663310b8ceb41628` | ii | documento **22**, L1600 · árbol `4d231ee` |
| 34 | `kernel/operativo/capacidades/USO/CAPACIDAD.md` | 94 | `65f144e4a5c756ef97596a997673d7ad73c194ee6936e616bafd434302ff5d0d` | ii | documento **22**, L1601 · árbol `4d231ee` |
| 35 | `kernel/operativo/capacidades/VER/CAPACIDAD.md` | 135 | `91a16b482629daf3455a3c6963a0568a7a68bcd2bd5553e7540d8c9edbfaf0e2` | ii | documento **22**, L1602 · árbol `4d231ee` |
| 36 | `kernel/operativo/contratos/00-INDICE.md` | 29 | `0b9562119f0b5b5c3f59e66c09446129fbe56865983d6424b76825bf570d004c` | v | documento **22**, L280 · árbol `4d231ee` |
| 37 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | 161 | `825f15a914c10d6f07f74e62967f93743efcf629a13379acb3947e70e2952ffa` | v | documento **22**, L281 · árbol `4d231ee` |
| 38 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | 539 | `3ee58ca4bc47988d4e6bdd652e2ea5de79ebcf8be79270664c0bd4b4cf391510` | ii+v | documento **21**, L399 · árbol `7764cca` |
| 39 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | 150 | `d56bf6b81e0fe4a9b3ba811f1adf57748cbae65692db557d15960c8506f84234` | ii+v | documento **21**, L400 · árbol `7764cca` |
| 40 | `kernel/operativo/contratos/C4-MATERIALIZACION.md` | 170 | `670289180e59b176743571a22f22047d20792db266b6426c1c91bd2fd3c1ee81` | ii+v | documento **21**, L401 · árbol `7764cca` |
| 41 | `kernel/operativo/contratos/C5-HANDOFF.md` | 115 | `af6f1a4c4f5def8da0dcecee8ea57c17516b41bbbd4abe963460c21024cc7b9e` | v | documento **22**, L282 · árbol `4d231ee` |
| 42 | `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` | 336 | `14805a79aeb07f314a55913864ee7d359ead05a932d59b207b66b6279d3a41e9` | v | documento **22**, L283 · árbol `4d231ee` |
| 43 | `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | 250 | `83f82e2be4756a4651e61f1883d2a99f1d141954097a6e4176a3482a951fc69c` | v | documento **22**, L284 · árbol `4d231ee` |
| 44 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | 141 | `08f4bea44594e026aee24cdddc93765cba0fa5c197b26adee0a0cad00d2c366a` | ii | documento **22**, L1603 · árbol `4d231ee` |
| 45 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | 352 | `dd323d1aa2f7ede3efa18ac01564b636fff8f0f77beac7db3abed667bbd429ec` | ii | documento **22**, L1604 · árbol `4d231ee` |
| 46 | `kernel/operativo/diseno/02-RUBRICAS.md` | 343 | `8aa8fb18426eac219c275c102f757d50727da2e363d905529c8c061d6721d842` | ii | documento **22**, L1605 · árbol `4d231ee` |
| 47 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | 130 | `5d2f54535c1334c053e27bf99b6b81a15a33be7180adf58ddf884cf79ef3a9c1` | ii | documento **22**, L1606 · árbol `4d231ee` |
| 48 | `kernel/operativo/diseno/05-FIDELIDAD.md` | 129 | `fdabb29f7592e603e755c12f191d189755e795ecee104c9b5f583b1ead56e441` | ii | documento **22**, L1607 · árbol `4d231ee` |
| 49 | `kernel/operativo/entrada/00-INDICE.md` | 28 | `315b2790cb66bb4c2c84272468675c8e77fb5a26b8cc2b95ff56db7ee266ddb1` | ii | documento **21**, L1056 · árbol `7764cca` |
| 50 | `kernel/operativo/entrada/02-CIRCUITO.md` | 145 | `750d39a29f05e7f2b037f9c246c9869ba80edec493e104e206baadda19c09c70` | ii | documento **21**, L1057 · árbol `7764cca` |
| 51 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | 187 | `1716bd3d8b48107d28a93e4297a6d93c0e6125107c0cc14811f092641e3d0cd2` | ii | documento **21**, L1058 · árbol `7764cca` |
| 52 | `kernel/operativo/esquemas/proceso.yaml` | 49 | `bd391d5acddff1342ce307829dfb8494df535dbd1924d44948d1e17176440dcc` | v | documento **22**, L1580 · árbol `4d231ee` |
| 53 | `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` | 130 | `f56e8fe4872e46b5ccc8bd2b9531cdc9e53247aaec1e36ebcae131efbe3674ac` | v | documento **22**, L1579 · árbol `4d231ee` |
| 54 | `kernel/operativo/recorrido/01-PROCESOS.md` | 564 | `98b5cbc836121044a1b3b38690331325cd730ac71d1f30da69482937c392ee85` | v | documento **22**, L1578 · árbol `4d231ee` |

## 6 · Totales derivados, y las DOS restas de `1bis`

```text
FUENTES OBLIGATORIAS        70
LÍNEAS OBLIGATORIAS     58 788

ASIGNADAS A LECTURA         16     28507 líneas · lotes complementarios de `Y` y `Z`
ASIGNADAS COMO AGOTADAS     54     30281 líneas

OBLIGATORIO menos ASIGNADO   0     CERO FUENTES SIN ASIGNAR
ASIGNADO menos LEÍDO         —     la calcula el adjudicador `AA`
```

## 7 · Lo que este gate tiene que juzgar

```text
· la SEDE CANÓNICA: ¿es autoridad de verdad, o una copia más? ¿la proyección la ENLAZA?
  ¿alguna paráfrasis AMPLÍA el texto canónico? ¿el sobre ancla su huella y falla cerrado
  sin ella?
· `O19` corrige PROCEDENCIA y AUTORIDAD. **¿Ha cambiado alguien el DISEÑO por el camino?**
  Si `O17` o `O18` dicen hoy algo distinto de lo que decidieron, es GRAVE
· el emisor reparado: ¿lee del commit? ¿se niega con el árbol sucio? ¿publica los dos
  árboles? ¿su receta reproduce el digest **sin ejecutar el emisor**?
· `M-04` COMO PROPOSICIÓN GENERAL. El gate anterior encontró SEIS árboles en verde, dos por
  puertas nuevas. **Busca el séptimo.** Y recuerda la distinción que `O18` fija: `C`
  —resistencia a un actor privilegiado— **NO es exigible como implementación dentro de
  `F4c`**. Un ataque que exija privilegio de escritura demuestra `C`, ya contratada para
  `F6`. Lo que cuenta es `A` —coherencia interna— y `B` —identidad de la candidata—
· los 43 hallazgos del documento 24: cuáles están cerrados y cuáles no
· `C-L.7`, que llega NO CERRADA · `C-L.3` · `C-L.5`
· y lo que el Owner prohíbe usar como evidencia primaria: mensajes de commit, paráfrasis
  del coordinador, una fila derivada del registro, o afirmaciones internas de que el Owner
  dijo algo
```

## 8 · Regla de cierre

```text
CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA.

Y cualquier diferencia entre el SOBRE recibido y lo que el árbol muestra INVALIDA EL GATE
—salvo que el adjudicador demuestre, como hizo `X`, que el objeto no está en duda y que la
diferencia es del instrumento y no del corpus. Esa demostración debe ser EXPRESA.

LA SEDE CANÓNICA que no coincida con la huella recibida externamente FALLA CERRADO.

EL VEREDICTO es uno de estos dos literales, y ninguna otra formulación vale:
    SUFICIENTE PARA F5
    INSUFICIENTE PARA F5

EL ADJUDICADOR NO CORRIGE. Adjudica y devuelve.
```
