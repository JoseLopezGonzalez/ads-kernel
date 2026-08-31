# MANIFIESTO PREVIO DE ASIGNACIÓN — SEXTO GATE DE CERTIFICACIÓN DE F4c (`6B`)

> **EMITIDO ANTES DE REPARTIR**, commiteado **ANTES de que exista ningún revisor**, y
> **después de cerrar todo `verificacion/`**. Una vez commiteado no se modifica.
>
> **SUSTITUYE AL PRIMER MANIFIESTO DE ESTE GATE, QUE NO SE REPARTIÓ A NADIE Y NO SE
> MODIFICA.** Aquél —`…-6-20260831.md`, commit `7940945`, publicado en
> `gate/f4c-certificacion-6-20260831`— usaba la marca **`ADJ`** para el adjudicador en la
> columna `revisor`, y el contrato del emisor exige marcas que casen con
> `^[A-Z]{1,2}[0-9]?$`. **El sobre NO SE EMITIÓ**: el emisor salió con código 2 y el
> diagnóstico «*el reparto trae marcas de revisor que no lo son: `['ADJ']`. El emisor no
> adivina a quién se asignó una fuente*». **Falló CERRADO, que es lo que tenía que hacer, y
> lo hizo ANTES de que existiera ningún revisor.** Aquel manifiesto queda publicado como
> historia, no se mueve y no se edita —`G-22` lo trata como inmutable—; la marca del
> adjudicador pasa a ser **`EE`**, que continúa la serie `…·BB·CC·DD` de los gates
> anteriores. Es el mismo procedimiento que el corpus ya usó en el CUARTO GATE con su
> manifiesto `4B`, y por la misma razón: un manifiesto defectuoso detectado antes de
> repartir se SUSTITUYE publicando otro, nunca reescribiendo el primero.
>
> **Y estrena el remedio de `DD-17` del quinto gate.** Cinco gates consecutivos dejaron el
> árbol que juzgaban con un validador canónico en ROJO porque el commit del manifiesto
> llevaba **el manifiesto solo**: añadir un fichero al corpus mueve los recuentos que la
> evidencia derivada publica, y `T147` falla mientras un documento no tenga enlace entrante.
> **Este commit lleva CUATRO cosas y no una**: el manifiesto, **su fila en `00-INDICE.md`**,
> **la evidencia derivada reejecutada** y el registro de esta asignación. Verificado, no
> supuesto: la batería y el runner corren sobre este mismo commit y su salida está en §9.

## 1 · Objeto del reparto

```text
COMMIT CANDIDATO   b27a761bb3eb6b0b1b3db2344b7184ef4b993309
TREE SHA           0a0992a3b46dc7fa67f1321a86ac4a9e776e2472
REFERENCIA REMOTA  refs/heads/review/f4c-clase-cerrada-candidate-20260831
FECHA              2026-08-31
RAMA DEL GATE      gate/f4c-certificacion-6b-20260831, creada sobre ese commit exacto
QUÉ TRAE           la tanda posterior al QUINTO GATE: los VEINTIDÓS hallazgos de `DD` y los
                   DOS que encontró el barrido transversal de la propia tanda (`BT-01`,
                   `BT-02`). Su enumeración NO se copia aquí: vive en el **PARTE DE LA
                   TANDA** de `CHECKPOINT-ADS-NEXT.md`, una fila por identificador, y se
                   cuenta con el `awk` que ese parte publica.
                   La cabeza del trabajo es el OCTAVO ÁRBOL: el perímetro deja de excluir
                   por NOMBRE y pasa a excluir por NATURALEZA —`.git` anclado a la RAÍZ,
                   poda sobre la RUTA COMPLETA, bytecode por CONTENIDO— con todo lo
                   excluido PUBLICADO con su ruta; la admisión de `docs/owner/` se evalúa
                   sobre el CONTENIDO DEL COMMIT; la zona normativa se DERIVA entera;
                   `G-10` deriva el censo que avala la excepción de §0; y la única prueba
                   negativa anclada deja de ser TAUTOLÓGICA.
ESTADO DECLARADO   APLICADO y NO CERTIFICADO · `F4c` ABIERTA · `F5` NO autorizada ·
                   `M-04` NO superada · `C-L.5` ABIERTA · `C-L.7` NO CERRADA
```

## 2 · El universo obligatorio se DERIVA, y se dice DE QUÉ ÁRBOL habla cada cifra

```bash
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py
```

```text
SOBRE EL ÁRBOL DE LA CANDIDATA   76 fuentes · 72592 líneas
                                 —y es el objeto que este gate juzga—

SOBRE EL ÁRBOL DEL GATE          NO SE ESCRIBE AQUÍ, Y NO ES UN DESCUIDO: es `DD-19`.
                                 Desde que `AA-01` convirtió `manifiestos/` en ZONA
                                 BARRIDA, **este manifiesto es fila de su propio
                                 universo**, y §5.4 obliga a que cada fila publique el
                                 SHA-256 de su fuente. Un manifiesto no puede contener su
                                 propio SHA-256: fijarlo lo cambia. La cifra del árbol del
                                 gate se DERIVA ejecutando el mismo comando sobre él, y la
                                 diferencia estructural es exactamente **+1 fuente: este
                                 fichero**.
```

> **POR QUÉ ESTE APARTADO ESTÁ ESCRITO ASÍ.** El manifiesto del QUINTO GATE rotuló
> «—sobre el árbol del GATE—» dos cifras que eran del árbol de la CANDIDATA, y su resta
> `OBLIGATORIO − ASIGNADO = 0` era **inalcanzable por punto fijo** sobre el árbol del gate.
> Son `DD-18` y `DD-19`, acotados en las entradas **§14** y **§15** del
> [`CORRIGENDUM-DICTAMENES-INMUTABLES.md`](../CORRIGENDUM-DICTAMENES-INMUTABLES.md), con
> las dos derivaciones y su comando. **Aquí se aplican las dos vías que `DD` determinó:
> rotular de qué árbol habla cada cifra, y publicar las dos aritméticas.** La tercera —que
> el derivador se excluya a sí mismo del barrido— **se rechazó expresamente**: sacar a un
> instrumento del universo que deriva es la clase de perímetro escrito que `DD-01` acaba de
> cerrar un piso más abajo.

## 3 · Los agentes

```text
REVISOR R1    protocolo, transacciones, recuperación, fuentes de verdad, Git, identidad,
              pruebas y DERIVADORES. Es quien audita el INSTRUMENTO —batería, derivador y
              emisor— y los manifiestos.
REVISOR R2    arquitectura documental, decisiones, procesos, capacidades, composición,
              contratos, presiones, checkpoint y COHERENCIA TRANSVERSAL.
ADJUDICADOR `EE`  recibe los DOS dictámenes YA CERRADOS, reproduce sus afirmaciones contra
              FICHERO Y LÍNEA y **NO resuelve por mayoría**. No corrige.

INDEPENDENCIA ninguno de los tres ha escrito F4, aplicado `D16`–`D108`, sido autor de
              ninguna corrección de ninguna tanda, ni participado en ningún gate anterior
              —`A` a `DD` incluidos—. `R1` y `R2` trabajan en PARALELO y SIN VERSE; el
              adjudicador no ve nada hasta que los dos cierran.
EL SOBRE      se entrega a cada uno DENTRO de su encargo y ANTES de que empiece a leer, y
              **no se transcribe a mano**: se emite UNA vez a un fichero fuera del
              repositorio auditado y los tres leen de ahí. Es el remedio que hizo VÁLIDO al
              quinto gate después de que el cuarto muriera por transcripción.
```

**El coste de las cadenas:** el lote de lectura son **29855** líneas, y sólo el documento 11
son **11682**. Ningún ojo único recorre esas 11682 líneas seguidas: se reparte por rangos, y
la unión de los rangos leídos tiene que cubrir el fichero entero o la lectura no es íntegra.

**Y la disciplina que el cuarto gate impuso y el quinto cumplió:** cada revisor entrega
**manifiesto de lectura de todas sus fuentes**, con ruta, líneas, SHA-256 y los rangos cuya
unión cubre el fichero. `ASIGNADO − LEÍDO` lo declara cada uno **contra su propio interés**.

## 4 · Reparto para LECTURA ÍNTEGRA

| # | ruta | líneas | SHA-256 | `1bis` | revisor | reparto |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 216 | `6eacea232af0be841614b85b62cc0e212b032a85d275c57d1b1e981db73ef7a6` | v | **R2** | R2 |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11682 | `2d89dbe3725b8487e3d60721ac1f5ebd6704882a7472ce2f8a64daa6d2f06a79` | iii | **R1+R2** | R1 L1–L5200 · R2 L5201–final |
| 3 | `docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md` | 4526 | `e2c34215d92937fb467b1ffdb4e6654f66198ead4dac8128c411469bf86c297e` | iv | **R1+R2+EE** | los tres · DESPUÉS de las demás fuentes |
| 4 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 4515 | `979fdcba16c7c53f0cf77f7dcbe724c2025aac007e88038a5172b03d0b70a648` | iii | **R2** | R2 |
| 5 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 562 | `02649f623df65e3955a4030831386e01dd3d2e4c20ed05609eb889a1a9caab6a` | v | **R1** | R1 |
| 6 | `docs/evolucion/verificacion/README.md` | 386 | `a3d343f4e155a232c7f751fdac8bafd2e5ed49023a38033762273426c2622930` | v | **R1** | R1 |
| 7 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 3873 | `ec9b948af5a901276dff46c7eff1e54f55e5032de386b78287d747519e87ff1d` | v | **R1** | R1 |
| 8 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 787 | `77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b` | v | **R1** | R1 |
| 9 | `docs/evolucion/verificacion/emitir-sobre-de-ancla.py` | 688 | `f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715` | v | **R1** | R1 |
| 10 | `docs/evolucion/verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` | 119 | `b1c29244dfedc139ff7e80a6167d200803d054f25554c75f31303fea5687a434` | v | **R1** | R1 |
| 11 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` | 240 | `c64a0ec4731e6d27751469e84cbcc33104bfe535c42efe4f98533f4d84a0b970` | v | **R1** | R1 |
| 12 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` | 316 | `fc4d1c2fdedbcb13be512e88303e21eddbeb194f6cc38b8e50fa0612dad08bbc` | v | **R1** | R1 |
| 13 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md` | 210 | `ac9e0edd59cf3e1b783b42ce0fc052e1eb28af7d5d66e218709d76589f724988` | v | **R1** | R1 |
| 14 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md` | 221 | `fc4902591eff43bc6736f626fdf2dd1bef7c4f193b1be31f3ddf26f436adb599` | v | **R1** | R1 |
| 15 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md` | 193 | `0f08b961c31f03bbedbae700fa67029ac87b6b962067b39b3e504fe28e8d1939` | v | **R1** | R1 |
| 16 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1321 | `789b3fd62831dd4bee642f74bf7296b865fd1c427115a497cd673416cdd08cea` | iii | **R2** | R2 |

## 5 · Fuentes AGOTADAS

```text
1  un gate anterior declara LEÍDO ÍNTEGRO DE ESA RUTA, con FILA PROPIA, citado con
   documento y línea. Una declaración de CONJUNTO no agota nada
2  los BYTES idénticos a los del árbol que ESE gate leyó DE VERDAD
3  si no se cumplen las dos, no se agota

Y ESTE MANIFIESTO APLICA LA REGLA MÁS ESTRICTA QUE EL ÁRBOL SOSTIENE: una fuente sólo se
agota si su SHA-256 de HOY coincide **byte a byte** con el que publicó el gate que la
certificó. Cualquier fuente que la tanda tocó vuelve a LECTURA ÍNTEGRA, aunque un gate
anterior la hubiera agotado.
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
| 15 | `docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md` | 2754 | `e8431c653cb7919e8d2ec82c5b4d3d11247a01aa61577bb8e5dd266916fb0e5d` | iv | documento **26**, L1978 · árbol `8c9ca9c` |
| 16 | `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | 2163 | `a88609167dbbea2818b7f2e68cbd4c6fc704cb7e2245ee0a2c873052486fd159` | i | documento **22**, L2642 · árbol `4d231ee` |
| 17 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md` | 140 | `c843b0c341183859b7f0f07db78cc67eade7ef98c4a96ad3edee23c769d2a976` | v | documento **22**, L1577 · árbol `4d231ee` |
| 18 | `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | 3343 | `64d170f5acc151445eff6f3f68a0bade91d00744dffa6bdf36c13cd2d366bd3e` | v | documento **26**, L1972 · árbol `8c9ca9c` |
| 19 | `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | 597 | `48412108f711204f5389e17fac974133e848737676eb4c57ba5b22c6a37ab8b0` | v | documento **26**, L1973 · árbol `8c9ca9c` |
| 20 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 334 | `db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a` | v | documento **25**, L1735 · árbol `82d8783` |
| 21 | `docs/rediseno/CHECKPOINT-OPERATIVO.md` | 195 | `d2131faa4aeddc6d66e98f5eb88d6d9d172a8910b174a1866eecc969633818bb` | v | documento **23**, L859 · árbol `c36d2ba` |
| 22 | `docs/rediseno/a-CAPACIDADES-APROBADA.md` | 1132 | `10cafb5ceee44f576d327ce614c14c86eb7b22ff43c3dfb82918b785eb36fb04` | v | documento **22**, L277 · árbol `4d231ee` |
| 23 | `docs/rediseno/a-ENMIENDA-E1-ENC.md` | 211 | `18dae19523b25ed4a2370ea9c1d23d68beb578f9365bd54587d2f2821093d4da` | ii+v | documento **21**, L395 · árbol `7764cca` |
| 24 | `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | 230 | `9d5a23806fc33fc1d76ba6be9b46ae3499c729c1f11203f80b32550c658ed2eb` | ii+v | documento **21**, L396 · árbol `7764cca` |
| 25 | `docs/rediseno/b-RECORRIDO-APROBADA.md` | 1288 | `f8cb974316e283fa2f16f9ecdd3b94ac19bf4a20cf5816cd155a2449f02719b4` | v | documento **22**, L278 · árbol `4d231ee` |
| 26 | `kernel/KERNEL.md` | 1590 | `aa635dff79e73fe13e271cb115653ebc042dc834d32007c634c8ee1df07e3150` | v | documento **22**, L279 · árbol `4d231ee` |
| 27 | `kernel/operativo/capacidades/APR/CAPACIDAD.md` | 95 | `a8709115309095849707e2d42290631dca6b3de95d49cc2c3c7ffa4e0546d708` | ii | documento **22**, L1588 · árbol `4d231ee` |
| 28 | `kernel/operativo/capacidades/ARQ/CAPACIDAD.md` | 104 | `6ca11b5f09883e24834f770e61963ae69ca738770ffb1de64f7be0afe4757a47` | ii | documento **22**, L1589 · árbol `4d231ee` |
| 29 | `kernel/operativo/capacidades/CON/CAPACIDAD.md` | 107 | `e0f79e6c3a467302c3d16aa5ee4ccb45583daf146d1676b2b06995419656c5d5` | ii | documento **22**, L1590 · árbol `4d231ee` |
| 30 | `kernel/operativo/capacidades/DIS/CAPACIDAD.md` | 147 | `06f019010d45771fd2a125f9f08f88159b45f15e9f83fd2404c7f2a23f32ad06` | ii | documento **22**, L1591 · árbol `4d231ee` |
| 31 | `kernel/operativo/capacidades/DOM/CAPACIDAD.md` | 135 | `926c7144cb098caaa0b87cdebb5c49b955b74832bc238e66d501ecbb2a635bb3` | ii | documento **22**, L1592 · árbol `4d231ee` |
| 32 | `kernel/operativo/capacidades/DSP/CAPACIDAD.md` | 152 | `acb292f882e77d74693caaab3e392a0d691e988cf875ca4394c59f859ebe7937` | ii | documento **22**, L1593 · árbol `4d231ee` |
| 33 | `kernel/operativo/capacidades/ENC/CAPACIDAD.md` | 174 | `f71b8e43f6e2d66f0801d53ce6e018806d33ef9b5ad5b3300bf1d38fe834d946` | ii | documento **22**, L1594 · árbol `4d231ee` |
| 34 | `kernel/operativo/capacidades/ENT/CAPACIDAD.md` | 123 | `91a81d3cf1cbfa619b7b69553a01810d7074b419fc7e2efb5f8ff2f8f9e7f9ed` | ii | documento **22**, L1595 · árbol `4d231ee` |
| 35 | `kernel/operativo/capacidades/INV/CAPACIDAD.md` | 96 | `47412638e7552da14b7bb89e590aea2f37cc61116c83b902e32952647380ed36` | ii | documento **22**, L1596 · árbol `4d231ee` |
| 36 | `kernel/operativo/capacidades/PLT/CAPACIDAD.md` | 108 | `a5f87977c58ed1d0d4deb3504d664a47fc90382a9790986e5aa277f1dad130d2` | ii | documento **22**, L1597 · árbol `4d231ee` |
| 37 | `kernel/operativo/capacidades/PRD/CAPACIDAD.md` | 105 | `e83b0e08272e219db0c5cc2e17b6d1a95dc4304a9f381d3acfe9c76ff528e3b3` | ii | documento **22**, L1598 · árbol `4d231ee` |
| 38 | `kernel/operativo/capacidades/SEG/CAPACIDAD.md` | 135 | `19bfd38a7a24b57fbec8365327926f7e281092a9e33a06e59355cfda5a5e5a13` | ii | documento **22**, L1599 · árbol `4d231ee` |
| 39 | `kernel/operativo/capacidades/SIS/CAPACIDAD.md` | 119 | `02089f36d124435669b7cf14cf46abd1365a860a4842b739663310b8ceb41628` | ii | documento **22**, L1600 · árbol `4d231ee` |
| 40 | `kernel/operativo/capacidades/USO/CAPACIDAD.md` | 94 | `65f144e4a5c756ef97596a997673d7ad73c194ee6936e616bafd434302ff5d0d` | ii | documento **22**, L1601 · árbol `4d231ee` |
| 41 | `kernel/operativo/capacidades/VER/CAPACIDAD.md` | 135 | `91a16b482629daf3455a3c6963a0568a7a68bcd2bd5553e7540d8c9edbfaf0e2` | ii | documento **22**, L1602 · árbol `4d231ee` |
| 42 | `kernel/operativo/contratos/00-INDICE.md` | 29 | `0b9562119f0b5b5c3f59e66c09446129fbe56865983d6424b76825bf570d004c` | v | documento **22**, L280 · árbol `4d231ee` |
| 43 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | 161 | `825f15a914c10d6f07f74e62967f93743efcf629a13379acb3947e70e2952ffa` | v | documento **22**, L281 · árbol `4d231ee` |
| 44 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | 539 | `3ee58ca4bc47988d4e6bdd652e2ea5de79ebcf8be79270664c0bd4b4cf391510` | ii+v | documento **21**, L399 · árbol `7764cca` |
| 45 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | 150 | `d56bf6b81e0fe4a9b3ba811f1adf57748cbae65692db557d15960c8506f84234` | ii+v | documento **21**, L400 · árbol `7764cca` |
| 46 | `kernel/operativo/contratos/C4-MATERIALIZACION.md` | 170 | `670289180e59b176743571a22f22047d20792db266b6426c1c91bd2fd3c1ee81` | ii+v | documento **21**, L401 · árbol `7764cca` |
| 47 | `kernel/operativo/contratos/C5-HANDOFF.md` | 115 | `af6f1a4c4f5def8da0dcecee8ea57c17516b41bbbd4abe963460c21024cc7b9e` | v | documento **22**, L282 · árbol `4d231ee` |
| 48 | `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` | 336 | `14805a79aeb07f314a55913864ee7d359ead05a932d59b207b66b6279d3a41e9` | v | documento **22**, L283 · árbol `4d231ee` |
| 49 | `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | 250 | `83f82e2be4756a4651e61f1883d2a99f1d141954097a6e4176a3482a951fc69c` | v | documento **22**, L284 · árbol `4d231ee` |
| 50 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | 141 | `08f4bea44594e026aee24cdddc93765cba0fa5c197b26adee0a0cad00d2c366a` | ii | documento **22**, L1603 · árbol `4d231ee` |
| 51 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | 352 | `dd323d1aa2f7ede3efa18ac01564b636fff8f0f77beac7db3abed667bbd429ec` | ii | documento **22**, L1604 · árbol `4d231ee` |
| 52 | `kernel/operativo/diseno/02-RUBRICAS.md` | 343 | `8aa8fb18426eac219c275c102f757d50727da2e363d905529c8c061d6721d842` | ii | documento **22**, L1605 · árbol `4d231ee` |
| 53 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | 130 | `5d2f54535c1334c053e27bf99b6b81a15a33be7180adf58ddf884cf79ef3a9c1` | ii | documento **22**, L1606 · árbol `4d231ee` |
| 54 | `kernel/operativo/diseno/05-FIDELIDAD.md` | 129 | `fdabb29f7592e603e755c12f191d189755e795ecee104c9b5f583b1ead56e441` | ii | documento **22**, L1607 · árbol `4d231ee` |
| 55 | `kernel/operativo/entrada/00-INDICE.md` | 28 | `315b2790cb66bb4c2c84272468675c8e77fb5a26b8cc2b95ff56db7ee266ddb1` | ii | documento **21**, L1056 · árbol `7764cca` |
| 56 | `kernel/operativo/entrada/02-CIRCUITO.md` | 145 | `750d39a29f05e7f2b037f9c246c9869ba80edec493e104e206baadda19c09c70` | ii | documento **21**, L1057 · árbol `7764cca` |
| 57 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | 187 | `1716bd3d8b48107d28a93e4297a6d93c0e6125107c0cc14811f092641e3d0cd2` | ii | documento **21**, L1058 · árbol `7764cca` |
| 58 | `kernel/operativo/esquemas/proceso.yaml` | 49 | `bd391d5acddff1342ce307829dfb8494df535dbd1924d44948d1e17176440dcc` | v | documento **22**, L1580 · árbol `4d231ee` |
| 59 | `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` | 130 | `f56e8fe4872e46b5ccc8bd2b9531cdc9e53247aaec1e36ebcae131efbe3674ac` | v | documento **22**, L1579 · árbol `4d231ee` |
| 60 | `kernel/operativo/recorrido/01-PROCESOS.md` | 564 | `98b5cbc836121044a1b3b38690331325cd730ac71d1f30da69482937c392ee85` | v | documento **22**, L1578 · árbol `4d231ee` |

## 6 · Totales derivados, y CADA UNO CON SU ÁRBOL

```text
SOBRE EL ÁRBOL DE LA CANDIDATA — el objeto del reparto
  FUENTES OBLIGATORIAS       76          LÍNEAS OBLIGATORIAS   72592
  ASIGNADAS A LECTURA        16   29855 líneas
  ASIGNADAS COMO AGOTADAS    60   42737 líneas
  OBLIGATORIO menos ASIGNADO  0     CERO FUENTES SIN ASIGNAR
  ASIGNADO menos LEÍDO        —     la calcula el ADJUDICADOR sobre los manifiestos de
                                    lectura, y NO el coordinador

SOBRE EL ÁRBOL DEL GATE — `DD-19`
  OBLIGATORIO menos ASIGNADO  1     Y ES INALCANZABLE QUE SEA 0, en éste y en todos los
                                    gates siguientes: la fuente que sobra es ESTE
                                    manifiesto, que entró en su propio universo cuando
                                    `AA-01` convirtió `manifiestos/` en zona barrida.
                                    Cerrarla a cero exigiría que este fichero contuviera su
                                    propio SHA-256. **No es un defecto de esta tanda: es una
                                    propiedad del corpus, y queda declarada en vez de
                                    disimulada.**
```

## 7 · Lo que este gate tiene que juzgar

```text
· **EL PERÍMETRO, OTRA VEZ, Y POR CLASE.** `DD-01` cerró el octavo árbol excluyendo por
  CONTENIDO y por RUTA. **¿Hay un NOVENO?** El ataque tiene que alcanzar el COMMIT y dejar
  la batería en verde. Recuerda que `C` —actor privilegiado— NO es exigible dentro de `F4c`.
· **`M-04` COMO PROPOSICIÓN GENERAL.** Cinco gates han encontrado ocho árboles. Busca el
  siguiente. Cuentan `A` y `B`.
· **`C-L.5`.** El quinto gate midió las DOS restas a ∅ y escribió «no se reabre por
  cobertura», **pero NO escribió CERTIFICADA**; la tanda la dejó ABIERTA y NO puso esa
  palabra por el adjudicador. **Este gate tiene que resolverlo EXPRESAMENTE: o emite la
  palabra, o dice por qué no la emite.**
· **`C-L.7`.** Sigue NO CERRADA, con la recurrencia de `DD-08` encima. ¿Reancla el
  checkpoint su estado en cada tanda, o vuelve a haber una sede que copia lo que declara
  no copiar?
· **`X63`.** Es CONTRATO DE PRUEBA DE `F6`. Comprueba que NO se presente como prueba
  ejecutada ni como certificación presente en ninguna sede.
· **LA TANDA `DD`/`BT` ENTERA.** El PARTE DE LA TANDA del checkpoint declara una fila por
  identificador. **¿Está cada remedio donde dice estar, y cierra la CLASE o sólo la
  instancia?** Los cuatro controles positivos que declara, ¿se reproducen?
· **LA RECONCILIACIÓN DE «SIETE HALLAZGOS APLICADOS».** El parte declara haberla hecho
  mecánicamente. Compruébala.
· **LAS CLASES, NO LAS INSTANCIAS.** `BB4` dictaminó que este sistema «cierra INSTANCIAS y
  no CLASES». Esta tanda dice haberse escrito contra esa frase. **Falsa esa afirmación si
  puedes**: busca la sede una más allá de la corregida.
· y lo que el Owner prohíbe como evidencia primaria: mensajes de commit, paráfrasis del
  coordinador, una fila derivada del registro, o afirmaciones internas del propio corpus
```

## 8 · Regla de cierre

```text
CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA.
CUALQUIER DIFERENCIA ENTRE LOS SOBRES DE DOS REVISORES INVALIDA EL GATE.
LA SEDE CANÓNICA que no coincida con la huella recibida FALLA CERRADO.

EL VEREDICTO es uno de estos dos literales:
    SUFICIENTE PARA F5
    INSUFICIENTE PARA F5

EL ADJUDICADOR NO CORRIGE, NO RESUELVE POR MAYORÍA Y NO SUAVIZA.
```

## 9 · La validación de ESTE commit, que `DD-17` obliga a traer aquí

```text
BATERÍA DEL GATE      38/38 en verde · EXIT=0
RUNNER CANÓNICO       13/13 validadores en verde · 13 evidencias publicadas · 0 problemas
DETERMINISMO          `git status --porcelain` VACÍO tras correr el runner
HUELLA DEL KERNEL     LIMPIO, coincide con el release
T147                  SUPERADA — este manifiesto se enlaza desde `00-INDICE.md` en el
                      MISMO commit que lo crea, que es lo que `C-L.5` obliga
INTÉRPRETE            el runner exige >= 3.11 (`tomllib`). Con el 3.10 del sistema caen
                      `arranque`, `fuentes` y `workspace`, IDÉNTICAS sobre `HEAD` sin
                      tocar: es `A14`, limitación aceptada, propietario `PLT`, fase `F6`.
                      La cifra de arriba se obtuvo con Python 3.12, y se dice.

Las cifras de este apartado NO son una promesa: son la salida de los dos comandos que
cualquiera puede reejecutar sobre este commit.
```
