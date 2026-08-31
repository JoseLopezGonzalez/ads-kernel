# MANIFIESTO PREVIO DE ASIGNACIÓN — OCTAVO GATE DE CERTIFICACIÓN DE F4c

> **EMITIDO ANTES DE REPARTIR**, commiteado **ANTES de que exista ningún revisor**, y
> **después de cerrar todo `verificacion/`**. Una vez commiteado no se modifica.
>
> **Aplica los cuatro remedios que los gates anteriores dejaron escritos para este
> documento:** `DD-17` —el commit lleva el manifiesto, **su fila en la LISTA de
> `00-INDICE.md`** y la evidencia derivada reejecutada—, `DD-19` —cada cifra dice de qué
> árbol habla—, `EE-02` —**las dos aritméticas se DERIVAN** y toda fuente sin fila lleva su
> razón publicada— y **`S1-09`**, que es el que estrena: **el revisor que audita el
> INSTRUMENTO tiene asignada la sede `C-L.5`·`1bis` del documento 11**, que en los dos gates
> anteriores cayó en la mitad del otro.

## 1 · Objeto del reparto

```text
COMMIT CANDIDATO   61492c1a474f2d3ddfced2a9b358e700c980bc29
TREE SHA           4f0b04310e517a1daacb7023af58b3d6993dd07b
REFERENCIA REMOTA  refs/heads/review/f4c-mutacion-guardada-candidate-20260831
FECHA              2026-08-31
RAMA DEL GATE      gate/f4c-certificacion-8-20260831, creada sobre ese commit exacto
QUÉ TRAE           la tanda posterior al SÉPTIMO GATE: sus CATORCE hallazgos. Su
                   enumeración NO se copia aquí: vive en el **PARTE DE LA TANDA POSTERIOR
                   AL SÉPTIMO GATE** de `CHECKPOINT-ADS-NEXT.md`, con el comando que lo
                   cuenta y el que comprueba su cobertura.
                   La cabeza del trabajo son **LAS DOS CLASES BLOQUEANTES**: toda lectura
                   de una lista de rutas pasa por **una sola función** que fuerza
                   `core.quotePath=false`, separa por `NUL`, decodifica en estricto y
                   detecta el TRUNCAMIENTO, con un **barrido** que impide que nazca otra; y
                   la guarda juzga **toda MUTACIÓN** de una ruta gobernada —añadida,
                   modificada, borrada, renombrada, copiada o cambiada de tipo— **exista o
                   no en la revisión base y esté o no confirmada**.
                   Y dos caras más de esa clase, encontradas por el banco de la tanda: la
                   EVIDENCIA DERIVADA se juzga por **la forma que su productor garantiza**,
                   y la SEDE DEL OWNER se comprueba **APPEND-ONLY contra el commit que la
                   creó**, no contra `HEAD`.
ESTADO DECLARADO   APLICADO y NO CERTIFICADO · `F4c` ABIERTA · `F5` NO autorizada ·
                   `M-04` NO superada · `C-L.5` **CERTIFICADA POR COBERTURA** por el
                   adjudicador del séptimo gate · `C-L.7` NO CERRADA
```

## 2 · El universo obligatorio se DERIVA, y cada cifra dice de qué árbol habla

```bash
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py | tail -1
```

```text
SOBRE EL ÁRBOL DE LA CANDIDATA   81 fuentes · 82835 líneas — el objeto que este gate juzga
SOBRE EL ÁRBOL DEL GATE          NO se copia: se DERIVA con el mismo comando sobre él, y su
                                 resta va enumerada fuente a fuente en §6
```

## 3 · Los agentes

```text
REVISOR T1        protocolo, transacciones, recuperación, fuentes de verdad, Git,
                  identidad, pruebas y DERIVADORES. Audita EL INSTRUMENTO y los manifiestos.
REVISOR T2        arquitectura documental, decisiones, procesos, capacidades, composición,
                  contratos, presiones, checkpoint y COHERENCIA TRANSVERSAL.
ADJUDICADOR `GG`  recibe los DOS dictámenes YA CERRADOS, reproduce sus afirmaciones contra
                  FICHERO Y LÍNEA y **NO resuelve por mayoría**. No corrige.

INDEPENDENCIA     ninguno de los tres ha escrito F4, aplicado ninguna corrección, ni
                  participado en NINGÚN gate anterior —`A` a `FF` incluidos—. `T1` y `T2`
                  en PARALELO y SIN VERSE; `GG` no ve nada hasta que los dos cierran.
EL SOBRE          se emite UNA vez a un fichero FUERA del repositorio auditado y los tres
                  leen de ahí. **No se transcribe.**
```

**`S1-09`, aplicado y visible en la tabla de abajo:** `T1` —que audita el instrumento— lee
`L1-L5200` **y `L11380-L11717`** del documento 11, de modo que la sede `C-L.5`·`1bis`, §11.4,
§11.6 y §11.9 **entran en su lote**. `T2` lee `L5201-L11717`. La unión cubre el fichero
entero y el solape es deliberado: era la limitación de método que dos adjudicadores
seguidos señalaron.

## 4 · Reparto para LECTURA ÍNTEGRA

| # | ruta | líneas | SHA-256 | `1bis` | revisor | reparto |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 237 | `3bf36822b23cf27b97fb7ee7d5cb074de267715349bf5a4f28296adc9687875b` | v | **T2** | T2 |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11717 | `6c99ad6808f8c1ad721f29001f3cf76d5038fbdf686dbf3ae3f6390fbbf0ff22` | iii | **T1+T2** | T1 `L1-L5200` **y `L11380-L11717`** · T2 `L5201-L11717` |
| 3 | `docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md` | 4275 | `4711738d2a5d64740cc382d7808cf3b185686f80930b3f0d26ff3cf756506854` | iv | **T1+T2+GG** | los tres · DESPUÉS de las demás fuentes |
| 4 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 5015 | `be8ac68470552e0431889439252769a03f0b6d548eb4979b758ff8daed6ae223` | iii | **T2** | T2 |
| 5 | `docs/evolucion/verificacion/README.md` | 386 | `f216def357a4075e3175bd9a7cb2bedf169fc6114b82bacb4d23d91ae5ba4dbe` | v | **T1** | T1 |
| 6 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 4313 | `d6f1210aae1ccf9d1da39d63e2a6aae57619b486741f488716047739b0d365ed` | v | **T1** | T1 |
| 7 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 833 | `8e08eae0ac1719b6d347c8d81c88044e88bbc1075d40d54ee786b6da3e9d4d5c` | v | **T1** | T1 |
| 8 | `docs/evolucion/verificacion/emitir-sobre-de-ancla.py` | 734 | `8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453` | v | **T1** | T1 |
| 9 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md` | 260 | `f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff` | v | **T1** | T1 |
| 10 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1335 | `5d0d84a8dabf3e3194fd3affe7d159a01f77bf7300c8493177d3cd46815ecf4d` | iii | **T2** | T2 |

## 5 · Fuentes AGOTADAS

```text
LA REGLA QUE SE APLICA, dicha como se ejecuta (`EE-08`):
1  un gate anterior declara LEÍDO ÍNTEGRO DE ESA RUTA con fila propia, citado con documento
   y línea — o el manifiesto de ese gate publicó su SHA-256 en una fila propia
2  los BYTES de HOY son idénticos a los del ÁRBOL QUE ESE GATE LEYÓ DE VERDAD
3  si no se cumplen las dos, no se agota, y vuelve a LECTURA ÍNTEGRA
```

| # | ruta | líneas | SHA-256 | `1bis` | lectura íntegra certificada en |
|---|---|---|---|---|---|
| 1 | `docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md` | 336 | `202ac1af8df5ca6e032cb06f6566c63cf2656fb1a54d65a8c9a0f5d0ef5d41d9` | iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 2 | `docs/evolucion/12-CRITICA-INDEPENDIENTE-F4.md` | 764 | `c50e0aa6c1b9827c166171efee1737b2e091cc5518d78bad8c469c709c0dd56f` | iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 3 | `docs/evolucion/13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md` | 797 | `6804d134dfb66b5304ec9c539750559e578a2d5855785b5803189baac2da931f` | iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 4 | `docs/evolucion/14-DEVOLUCION-TECNICA-PREVIA-F4C.md` | 325 | `7f94e236f3cfb11e78762a301d9a3e94939ab47df34658710d1b8686ed7050fb` | iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 5 | `docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` | 651 | `b0e015c118ceb916e58fc8191b2a5e40cf28c44dd426618fdd49d10e3ea495d6` | ii+iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 6 | `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | 1257 | `8243034f286160cc89330af95b49f558af0dd16d1b36a37ccbdf02f74a79d185` | i+iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 7 | `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` | 1650 | `18f876d4cd47a2f7cfde15594f98696cfacf750607cd23811dd40ffb36d6c29c` | i+iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 8 | `docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` | 3665 | `1e71366b10d2293802db435de14953771ebd8fc13b426acedd7c0efe21cdb496` | i+iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 9 | `docs/evolucion/19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md` | 1152 | `48baaa1a8e69c6ef3401eb7a0088dcf06849bd66fa3f238bf3e7b8c8fd14392d` | iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 10 | `docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md` | 801 | `d7d2e4fa3f878e0c010d979e89affdb63462cc6fdd6628ed885d3a760bde09d1` | iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 11 | `docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md` | 2679 | `9f869ffbdbdb834ca872c03abc8826c125a47b4344ed32cd9b6266db08f8be03` | iv+v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 12 | `docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md` | 3478 | `3e2bdece758e6b69d6695bb52f20d21b910a123a27ac643845dbad75e8355f1c` | iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 13 | `docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md` | 2913 | `0f81f13d8cb319d8ccc5243d19bb26d7f71f57e860cde2eb2edefe33b6993dc2` | iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 14 | `docs/evolucion/24-TERCER-GATE-DE-CERTIFICACION-F4C.md` | 2515 | `8df584529c857c071954b0d1b426faff82277e29a43556abe5dccfd93714fae1` | iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 15 | `docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md` | 2754 | `e8431c653cb7919e8d2ec82c5b4d3d11247a01aa61577bb8e5dd266916fb0e5d` | iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 16 | `docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md` | 4526 | `e2c34215d92937fb467b1ffdb4e6654f66198ead4dac8128c411469bf86c297e` | iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 17 | `docs/evolucion/27-SEXTO-GATE-DE-CERTIFICACION-F4C.md` | 3946 | `d81b56366e5062ffe0abcd55ba2ef52ddbc3fadf073ea5a280e6cfc15b87ef26` | iv | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 18 | `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | 2163 | `a88609167dbbea2818b7f2e68cbd4c6fc704cb7e2245ee0a2c873052486fd159` | i | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 19 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 652 | `7876a2bb81b38c764d1bec924e972fb15df30d78058ef299c8adeff087a14255` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 20 | `docs/evolucion/verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` | 119 | `b1c29244dfedc139ff7e80a6167d200803d054f25554c75f31303fea5687a434` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 21 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` | 240 | `c64a0ec4731e6d27751469e84cbcc33104bfe535c42efe4f98533f4d84a0b970` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 22 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` | 316 | `fc4d1c2fdedbcb13be512e88303e21eddbeb194f6cc38b8e50fa0612dad08bbc` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 23 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md` | 210 | `ac9e0edd59cf3e1b783b42ce0fc052e1eb28af7d5d66e218709d76589f724988` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 24 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md` | 221 | `fc4902591eff43bc6736f626fdf2dd1bef7c4f193b1be31f3ddf26f436adb599` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 25 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md` | 193 | `0f08b961c31f03bbedbae700fa67029ac87b6b962067b39b3e504fe28e8d1939` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 26 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md` | 278 | `528dd68fc81134c16f874ab5803996ec50ee838241fd95470a9e07dd66770b2c` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 27 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md` | 292 | `41a4ff29d11c1edf26e6370ea7bcf8cf1ee24d75895336d991b6c12fa4251924` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 28 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md` | 140 | `c843b0c341183859b7f0f07db78cc67eade7ef98c4a96ad3edee23c769d2a976` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 29 | `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | 3343 | `64d170f5acc151445eff6f3f68a0bade91d00744dffa6bdf36c13cd2d366bd3e` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 30 | `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | 597 | `48412108f711204f5389e17fac974133e848737676eb4c57ba5b22c6a37ab8b0` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 31 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 334 | `db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 32 | `docs/rediseno/CHECKPOINT-OPERATIVO.md` | 195 | `d2131faa4aeddc6d66e98f5eb88d6d9d172a8910b174a1866eecc969633818bb` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 33 | `docs/rediseno/a-CAPACIDADES-APROBADA.md` | 1132 | `10cafb5ceee44f576d327ce614c14c86eb7b22ff43c3dfb82918b785eb36fb04` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 34 | `docs/rediseno/a-ENMIENDA-E1-ENC.md` | 211 | `18dae19523b25ed4a2370ea9c1d23d68beb578f9365bd54587d2f2821093d4da` | ii+v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 35 | `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | 230 | `9d5a23806fc33fc1d76ba6be9b46ae3499c729c1f11203f80b32550c658ed2eb` | ii+v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 36 | `docs/rediseno/b-RECORRIDO-APROBADA.md` | 1288 | `f8cb974316e283fa2f16f9ecdd3b94ac19bf4a20cf5816cd155a2449f02719b4` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 37 | `kernel/KERNEL.md` | 1590 | `aa635dff79e73fe13e271cb115653ebc042dc834d32007c634c8ee1df07e3150` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 38 | `kernel/operativo/capacidades/APR/CAPACIDAD.md` | 95 | `a8709115309095849707e2d42290631dca6b3de95d49cc2c3c7ffa4e0546d708` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 39 | `kernel/operativo/capacidades/ARQ/CAPACIDAD.md` | 104 | `6ca11b5f09883e24834f770e61963ae69ca738770ffb1de64f7be0afe4757a47` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 40 | `kernel/operativo/capacidades/CON/CAPACIDAD.md` | 107 | `e0f79e6c3a467302c3d16aa5ee4ccb45583daf146d1676b2b06995419656c5d5` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 41 | `kernel/operativo/capacidades/DIS/CAPACIDAD.md` | 147 | `06f019010d45771fd2a125f9f08f88159b45f15e9f83fd2404c7f2a23f32ad06` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 42 | `kernel/operativo/capacidades/DOM/CAPACIDAD.md` | 135 | `926c7144cb098caaa0b87cdebb5c49b955b74832bc238e66d501ecbb2a635bb3` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 43 | `kernel/operativo/capacidades/DSP/CAPACIDAD.md` | 152 | `acb292f882e77d74693caaab3e392a0d691e988cf875ca4394c59f859ebe7937` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 44 | `kernel/operativo/capacidades/ENC/CAPACIDAD.md` | 174 | `f71b8e43f6e2d66f0801d53ce6e018806d33ef9b5ad5b3300bf1d38fe834d946` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 45 | `kernel/operativo/capacidades/ENT/CAPACIDAD.md` | 123 | `91a81d3cf1cbfa619b7b69553a01810d7074b419fc7e2efb5f8ff2f8f9e7f9ed` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 46 | `kernel/operativo/capacidades/INV/CAPACIDAD.md` | 96 | `47412638e7552da14b7bb89e590aea2f37cc61116c83b902e32952647380ed36` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 47 | `kernel/operativo/capacidades/PLT/CAPACIDAD.md` | 108 | `a5f87977c58ed1d0d4deb3504d664a47fc90382a9790986e5aa277f1dad130d2` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 48 | `kernel/operativo/capacidades/PRD/CAPACIDAD.md` | 105 | `e83b0e08272e219db0c5cc2e17b6d1a95dc4304a9f381d3acfe9c76ff528e3b3` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 49 | `kernel/operativo/capacidades/SEG/CAPACIDAD.md` | 135 | `19bfd38a7a24b57fbec8365327926f7e281092a9e33a06e59355cfda5a5e5a13` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 50 | `kernel/operativo/capacidades/SIS/CAPACIDAD.md` | 119 | `02089f36d124435669b7cf14cf46abd1365a860a4842b739663310b8ceb41628` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 51 | `kernel/operativo/capacidades/USO/CAPACIDAD.md` | 94 | `65f144e4a5c756ef97596a997673d7ad73c194ee6936e616bafd434302ff5d0d` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 52 | `kernel/operativo/capacidades/VER/CAPACIDAD.md` | 135 | `91a16b482629daf3455a3c6963a0568a7a68bcd2bd5553e7540d8c9edbfaf0e2` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 53 | `kernel/operativo/contratos/00-INDICE.md` | 29 | `0b9562119f0b5b5c3f59e66c09446129fbe56865983d6424b76825bf570d004c` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 54 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | 161 | `825f15a914c10d6f07f74e62967f93743efcf629a13379acb3947e70e2952ffa` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 55 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | 539 | `3ee58ca4bc47988d4e6bdd652e2ea5de79ebcf8be79270664c0bd4b4cf391510` | ii+v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 56 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | 150 | `d56bf6b81e0fe4a9b3ba811f1adf57748cbae65692db557d15960c8506f84234` | ii+v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 57 | `kernel/operativo/contratos/C4-MATERIALIZACION.md` | 170 | `670289180e59b176743571a22f22047d20792db266b6426c1c91bd2fd3c1ee81` | ii+v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 58 | `kernel/operativo/contratos/C5-HANDOFF.md` | 115 | `af6f1a4c4f5def8da0dcecee8ea57c17516b41bbbd4abe963460c21024cc7b9e` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 59 | `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` | 336 | `14805a79aeb07f314a55913864ee7d359ead05a932d59b207b66b6279d3a41e9` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 60 | `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | 250 | `83f82e2be4756a4651e61f1883d2a99f1d141954097a6e4176a3482a951fc69c` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 61 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | 141 | `08f4bea44594e026aee24cdddc93765cba0fa5c197b26adee0a0cad00d2c366a` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 62 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | 352 | `dd323d1aa2f7ede3efa18ac01564b636fff8f0f77beac7db3abed667bbd429ec` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 63 | `kernel/operativo/diseno/02-RUBRICAS.md` | 343 | `8aa8fb18426eac219c275c102f757d50727da2e363d905529c8c061d6721d842` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 64 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | 130 | `5d2f54535c1334c053e27bf99b6b81a15a33be7180adf58ddf884cf79ef3a9c1` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 65 | `kernel/operativo/diseno/05-FIDELIDAD.md` | 129 | `fdabb29f7592e603e755c12f191d189755e795ecee104c9b5f583b1ead56e441` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 66 | `kernel/operativo/entrada/00-INDICE.md` | 28 | `315b2790cb66bb4c2c84272468675c8e77fb5a26b8cc2b95ff56db7ee266ddb1` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 67 | `kernel/operativo/entrada/02-CIRCUITO.md` | 145 | `750d39a29f05e7f2b037f9c246c9869ba80edec493e104e206baadda19c09c70` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 68 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | 187 | `1716bd3d8b48107d28a93e4297a6d93c0e6125107c0cc14811f092641e3d0cd2` | ii | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 69 | `kernel/operativo/esquemas/proceso.yaml` | 49 | `bd391d5acddff1342ce307829dfb8494df535dbd1924d44948d1e17176440dcc` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 70 | `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` | 130 | `f56e8fe4872e46b5ccc8bd2b9531cdc9e53247aaec1e36ebcae131efbe3674ac` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |
| 71 | `kernel/operativo/recorrido/01-PROCESOS.md` | 564 | `98b5cbc836121044a1b3b38690331325cd730ac71d1f30da69482937c392ee85` | v | manifiesto `7` del documento **28** · árbol `f8fc037` |

## 6 · Totales, y las DOS aritméticas — DERIVADAS, no copiadas (`EE-02`)

```text
SOBRE EL ÁRBOL DE LA CANDIDATA — el objeto del reparto
  ASIGNADAS A LECTURA        10   29105 líneas
  ASIGNADAS COMO AGOTADAS    71   53730 líneas
  OBLIGATORIO menos ASIGNADO  0    CERO FUENTES SIN ASIGNAR
  ASIGNADO menos LEÍDO        —    la calcula el ADJUDICADOR, no el coordinador

SOBRE EL ÁRBOL DEL GATE — las fuentes sin fila, UNA A UNA y con su razón
  ESTE MANIFIESTO               sin fila, y es INEVITABLE: no puede contener su propio
                                SHA-256. Exención de PUNTO FIJO de `DD-19`, y cubre a ESTE
                                fichero y a NINGÚN OTRO
  LA EVIDENCIA REEJECUTADA      no son fuentes obligatorias: no entran en el universo
  LA FILA DE `00-INDICE.md`     el índice SÍ es fuente obligatoria y SÍ tiene fila; lo que
                                cambia entre los dos árboles es su SHA-256, y por eso el
                                sobre publica las rutas en que los universos difieren

  CUALQUIER OTRA FUENTE SIN FILA sobre el árbol del gate es un DEFECTO de este manifiesto.
```

## 7 · Lo que este gate tiene que juzgar

```text
· **EL UNDÉCIMO ÁRBOL.** La guarda juzga la MUTACIÓN y no la existencia, y toda lectura de
  listas pasa por una función que falla cerrado. **¿Queda otra puerta?** Un ataque vale si
  ALCANZA EL COMMIT y deja la batería en verde. `C` NO es exigible dentro de `F4c`.
· **LAS CUATRO LECTURAS DE GIT y cualquier otra equivalente.** Rutas con espacios, saltos
  de línea, Unicode, guion inicial, y rutas confundibles al separar por líneas.
· **LOS OCHO FICHEROS PREEXISTENTES**, y toda mutación: adición, modificación, renombrado,
  borrado, cambio de tipo. Cambios NUEVOS y cambios YA CONFIRMADOS.
· **QUE LA DEFINICIÓN DE LO VERIFICADO Y LA REGLA DE ADMISIÓN NO PUEDAN EXCLUIRSE A SÍ
  MISMAS.** Es la propiedad que dos adjudicadores han nombrado sin cerrarla.
· **`C-L.5`** — certificada por cobertura por el séptimo gate y recogida en el checkpoint.
  ¿Es correcto el registro, y sigue siendo cierta la medición sobre ESTA candidata?
· **`C-L.7`** — se cierra RETIRANDO por primera vez. ¿Queda alguna sede del bloque de
  estado que copie lo que declara no copiar?
· **`M-04` como proposición general.**
· **LOS 14 DEL SÉPTIMO GATE, UNO POR UNO**, y su cobertura contra el documento 28.
· **AUSENCIA DE REGRESIONES** en los 19 del sexto gate y en los 24 `DD`/`BT` del quinto.
· **LOS DIECISIETE CONTROLES ADVERSARIALES** que la tanda declara en rojo: reprodúcelos, y
  busca el decimoctavo.
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

EL ADJUDICADOR NO CORRIGE, NO RESUELVE POR MAYORÍA Y NO SUAVIZA. **Y tiene que INTENTAR
construir un árbol adversarial que pase en verde**: si lo consigue, lo documenta y declara
insuficiencia. Que la batería esté verde NO es razón de suficiencia.
```

## 9 · La validación de ESTE commit (`DD-17`)

```text
BATERÍA DEL GATE      38/38 en verde · EXIT=0, desde la raíz y desde otro cwd
RUNNER CANÓNICO       13/13 validadores · 13 evidencias publicadas · 0 problemas
DETERMINISMO          dos ejecuciones, `git status --porcelain` VACÍO
HUELLA DEL KERNEL     LIMPIO, coincide con el release
T147 · T158 · T161    SUPERADAS · negativas 67/0 · workspace 57 tests OK
INTÉRPRETE            Python 3.12.14, y se dice. Con el 3.10 del sistema caen tres
                      validadores por `tomllib`: es `A14`, NO un hallazgo
```
