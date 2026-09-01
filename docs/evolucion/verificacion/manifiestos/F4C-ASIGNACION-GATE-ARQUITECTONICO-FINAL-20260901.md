# MANIFIESTO PREVIO DE ASIGNACIÓN — GATE ARQUITECTÓNICO FINAL DE `F4c`

> **EMITIDO ANTES DE REPARTIR**, commiteado **ANTES de que exista ningún revisor**, y
> **después de cerrar todo `verificacion/`**. Una vez commiteado no se modifica.
>
> **Y ESTE GATE NO ES COMO LOS OCHO ANTERIORES.** `O20` cambió la frontera de
> certificación: **su objeto NO es la implementación del verificador, que es de `F6`**. Es la
> SUFICIENCIA ARQUITECTÓNICA de `F4c`. El §7 lo escribe entero, incluido **lo que este gate
> NO puede usar como razón de insuficiencia**.
>
> **Aplica además los cinco remedios que los gates anteriores dejaron escritos para este
> documento:** `DD-17` · `DD-19` · `EE-02` · **`C-05`**, el reparto se comprueba contra la
> propia tabla y ninguna frase afirma lo que la tabla no dé · **`C-10`**, la columna de
> agotamiento **distingue LEÍDA de AGOTADA POR DELEGACIÓN**.

## 1 · Objeto del reparto

```text
COMMIT CANDIDATO   7aeed6aa3a3eae1133f57a08d757020e62197b3d
TREE SHA           0a8f5804e37bfb4ea05deabd18659cd2864f1d73
REFERENCIA REMOTA  refs/heads/review/f4c-o20-frontera-de-fase-candidate-20260901
FECHA              2026-09-01
RAMA DEL GATE      gate/f4c-arquitectonico-final-20260901, creada sobre ese commit exacto
QUÉ TRAE           **`O20` DEL OWNER**, registrada en la SEDE CANÓNICA —append-only— y
                   proyectada en `O20` y `D109`; **el CONTRATO OBLIGATORIO DE `F6`** en §20
                   del documento 11, con DIECIOCHO puntos y once campos cada uno, **ninguno
                   implementado y ninguno ejecutado**; la **MATRIZ DE CIERRE** de los 22
                   hallazgos del octavo gate, con un estado primario cada uno; y los
                   **CATORCE** que son de `F4c`, corregidos.
ESTADO DECLARADO   APLICADO y NO CERTIFICADO · `F4c` ABIERTA · `F5` NO autorizada ·
                   `M-04` NO superada —cambia de FASE, no de ESTADO— · `C-L.5` ABIERTA ·
                   `C-L.7` NO CERRADA · **PesquerApp BLOQUEADA**
```

## 2 · El universo obligatorio se DERIVA, y cada cifra dice de qué árbol habla

```bash
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py | tail -1
```

```text
SOBRE EL ÁRBOL DE LA CANDIDATA   83 fuentes · 87898 líneas — el objeto de este gate
SOBRE EL ÁRBOL DEL GATE          NO se copia: se DERIVA con el mismo comando sobre él, y su
                                 resta va enumerada fuente a fuente en §6
```

## 3 · Los agentes

```text
REVISOR U1        arquitectura del verificador y de la raíz de confianza, contratos de
                  `F6`, protocolo, Git, pruebas y derivadores. **Audita si lo ENTREGADO A
                  `F6` se puede construir sin volver a decidir nada.**
REVISOR U2        arquitectura documental, decisiones, procesos, capacidades, contratos,
                  presiones, checkpoint, la frontera `F4c`/`F6` y la trazabilidad hasta
                  PesquerApp.
ADJUDICADOR `HH`  recibe los DOS dictámenes YA CERRADOS, reproduce sus afirmaciones contra
                  FICHERO Y LÍNEA y **NO resuelve por mayoría**. No corrige.

INDEPENDENCIA     ninguno de los tres ha escrito F4, aplicado ninguna corrección, ni
                  participado en NINGÚN gate anterior —`A` a `HH` incluidos—. `U1` y `U2` en
                  PARALELO y SIN VERSE; `HH` no ve nada hasta que los dos cierran.
EL SOBRE          se emite UNA vez a un fichero FUERA del repositorio auditado y los tres
                  leen de ahí. **No se transcribe.**
```

**`C-05`, aplicado y comprobable contra la tabla de abajo:** `U1` —que audita lo entregado a
`F6`— lee `L1-L5200` **y `L8200-L11791`** del documento 11, rango que contiene **§11.4, §11.6,
§11.9, la sede `C-L.5`·`1bis` y §20 entera**, que es el contrato que tiene que juzgar. `U2` lee
`L5201-L11791`. **La SEDE CANÓNICA DEL OWNER la leen LOS TRES**, porque `O20` nace en ella.
**Ninguna frase de este manifiesto afirma un reparto que su §4 no dé**: si difieren, manda §4.

## 4 · Reparto para LECTURA ÍNTEGRA

| # | ruta | líneas | SHA-256 | `1bis` | revisor | reparto |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 241 | `1077403f421f5609a6b5393c5f86b77054fc426b7daa64947fc3ed1eb1d69118` | v | **U2** | U2 |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11791 | `4ad648c17b0e753fcd0373bcbe8922e76593e0968f9c36a9a8ae693fecf0c815` | iii | **U1+U2** | U1 `L1-L5200` **y `L8200-L11791`** —§11.4, §11.6, §11.9, `C-L.5`·`1bis` y **§20, el contrato de `F6`**— · U2 `L5201-L11791` |
| 3 | `docs/evolucion/29-OCTAVO-GATE-DE-CERTIFICACION-F4C.md` | 4197 | `0b9064490c8dd68ec7c50ed87778d31ab8ab5360c966642113367a0eeba2e5ac` | iv | **U1+U2+HH** | los tres · DESPUÉS de las demás fuentes |
| 4 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 5339 | `edba17ec59bf60e85a0c70a3d49b90d3a2641d4baaa3b65e50d65a04b00d6828` | iii | **U2** | U2 |
| 5 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 4339 | `29a754dac385115b773a43f4b714872540aee4236875c42126f9d4f97f906db0` | v | **U1** | U1 |
| 6 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 846 | `0eca7103833110c32b4d2fda23acf54a04c905e40e98b6fda102e5d2dd5f312e` | v | **U1** | U1 |
| 7 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md` | 248 | `a82e74968e4ca31fbae0825a43f295736af39e58a16b3adf8879d021688e3d76` | v | **U1** | U1 |
| 8 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 444 | `4e4081efb29dcd2f095879b07104e4e169a46b497d11213256541fd6599a4e3a` | v | **U1+U2+HH** | los tres · es la SEDE CANÓNICA y `O20` nace en ella |
| 9 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1402 | `07ddfcbe05f8b56f9846bba38a29a6c5dabc38796d3c4bc3bf075903e453bf01` | iii | **U2** | U2 |

## 5 · Fuentes AGOTADAS — y la columna distingue LEÍDA de DELEGADA (`C-10`)

```text
LA REGLA QUE SE APLICA, dicha como se ejecuta:
1  LEÍDA        un revisor de un gate anterior declaró LEÍDO ÍNTEGRO DE ESA RUTA, con fila
                propia y citado con documento y línea
2  DELEGADA     el manifiesto de un gate anterior publicó su SHA-256 en fila propia, y ese
                gate la dio por agotada — pero **NADIE declaró haberla leído íntegra allí**
3  en los DOS casos, los BYTES de hoy son IDÉNTICOS a los del árbol que ese gate juzgó
4  si no se cumple, no se agota, y vuelve a LECTURA ÍNTEGRA

**LA DISTINCIÓN NO ES COSMÉTICA, y es `C-10`:** un rótulo «lectura íntegra certificada en»
sobre una fila que nadie leyó íntegra dice más de lo que la regla entrega. Aquí se dice cuál
es cuál, y el adjudicador puede pesar la diferencia.
```

| # | ruta | líneas | SHA-256 | `1bis` | tipo | procedencia del agotamiento |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md` | 336 | `202ac1af8df5ca6e032cb06f6566c63cf2656fb1a54d65a8c9a0f5d0ef5d41d9` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 2 | `docs/evolucion/12-CRITICA-INDEPENDIENTE-F4.md` | 764 | `c50e0aa6c1b9827c166171efee1737b2e091cc5518d78bad8c469c709c0dd56f` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 3 | `docs/evolucion/13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md` | 797 | `6804d134dfb66b5304ec9c539750559e578a2d5855785b5803189baac2da931f` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 4 | `docs/evolucion/14-DEVOLUCION-TECNICA-PREVIA-F4C.md` | 325 | `7f94e236f3cfb11e78762a301d9a3e94939ab47df34658710d1b8686ed7050fb` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 5 | `docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` | 651 | `b0e015c118ceb916e58fc8191b2a5e40cf28c44dd426618fdd49d10e3ea495d6` | ii+iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 6 | `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | 1257 | `8243034f286160cc89330af95b49f558af0dd16d1b36a37ccbdf02f74a79d185` | i+iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 7 | `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` | 1650 | `18f876d4cd47a2f7cfde15594f98696cfacf750607cd23811dd40ffb36d6c29c` | i+iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 8 | `docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` | 3665 | `1e71366b10d2293802db435de14953771ebd8fc13b426acedd7c0efe21cdb496` | i+iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 9 | `docs/evolucion/19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md` | 1152 | `48baaa1a8e69c6ef3401eb7a0088dcf06849bd66fa3f238bf3e7b8c8fd14392d` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 10 | `docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md` | 801 | `d7d2e4fa3f878e0c010d979e89affdb63462cc6fdd6628ed885d3a760bde09d1` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 11 | `docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md` | 2679 | `9f869ffbdbdb834ca872c03abc8826c125a47b4344ed32cd9b6266db08f8be03` | iv+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 12 | `docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md` | 3478 | `3e2bdece758e6b69d6695bb52f20d21b910a123a27ac643845dbad75e8355f1c` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 13 | `docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md` | 2913 | `0f81f13d8cb319d8ccc5243d19bb26d7f71f57e860cde2eb2edefe33b6993dc2` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 14 | `docs/evolucion/24-TERCER-GATE-DE-CERTIFICACION-F4C.md` | 2515 | `8df584529c857c071954b0d1b426faff82277e29a43556abe5dccfd93714fae1` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 15 | `docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md` | 2754 | `e8431c653cb7919e8d2ec82c5b4d3d11247a01aa61577bb8e5dd266916fb0e5d` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 16 | `docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md` | 4526 | `e2c34215d92937fb467b1ffdb4e6654f66198ead4dac8128c411469bf86c297e` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 17 | `docs/evolucion/27-SEXTO-GATE-DE-CERTIFICACION-F4C.md` | 3946 | `d81b56366e5062ffe0abcd55ba2ef52ddbc3fadf073ea5a280e6cfc15b87ef26` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 18 | `docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md` | 4275 | `4711738d2a5d64740cc382d7808cf3b185686f80930b3f0d26ff3cf756506854` | iv | **LEÍDA** | LEÍDA ÍNTEGRA · documento **29**, L537 · árbol `61492c1` |
| 19 | `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | 2163 | `a88609167dbbea2818b7f2e68cbd4c6fc704cb7e2245ee0a2c873052486fd159` | i | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 20 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 652 | `7876a2bb81b38c764d1bec924e972fb15df30d78058ef299c8adeff087a14255` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 21 | `docs/evolucion/verificacion/README.md` | 386 | `f216def357a4075e3175bd9a7cb2bedf169fc6114b82bacb4d23d91ae5ba4dbe` | v | **LEÍDA** | LEÍDA ÍNTEGRA · documento **29**, L538 · árbol `61492c1` |
| 22 | `docs/evolucion/verificacion/emitir-sobre-de-ancla.py` | 734 | `8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453` | v | **LEÍDA** | LEÍDA ÍNTEGRA · documento **29**, L541 · árbol `61492c1` |
| 23 | `docs/evolucion/verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` | 119 | `b1c29244dfedc139ff7e80a6167d200803d054f25554c75f31303fea5687a434` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 24 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` | 240 | `c64a0ec4731e6d27751469e84cbcc33104bfe535c42efe4f98533f4d84a0b970` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 25 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` | 316 | `fc4d1c2fdedbcb13be512e88303e21eddbeb194f6cc38b8e50fa0612dad08bbc` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 26 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md` | 210 | `ac9e0edd59cf3e1b783b42ce0fc052e1eb28af7d5d66e218709d76589f724988` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 27 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md` | 221 | `fc4902591eff43bc6736f626fdf2dd1bef7c4f193b1be31f3ddf26f436adb599` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 28 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md` | 193 | `0f08b961c31f03bbedbae700fa67029ac87b6b962067b39b3e504fe28e8d1939` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 29 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md` | 278 | `528dd68fc81134c16f874ab5803996ec50ee838241fd95470a9e07dd66770b2c` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 30 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md` | 292 | `41a4ff29d11c1edf26e6370ea7bcf8cf1ee24d75895336d991b6c12fa4251924` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 31 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md` | 260 | `f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 32 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md` | 140 | `c843b0c341183859b7f0f07db78cc67eade7ef98c4a96ad3edee23c769d2a976` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 33 | `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | 3343 | `64d170f5acc151445eff6f3f68a0bade91d00744dffa6bdf36c13cd2d366bd3e` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 34 | `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | 597 | `48412108f711204f5389e17fac974133e848737676eb4c57ba5b22c6a37ab8b0` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 35 | `docs/rediseno/CHECKPOINT-OPERATIVO.md` | 195 | `d2131faa4aeddc6d66e98f5eb88d6d9d172a8910b174a1866eecc969633818bb` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 36 | `docs/rediseno/a-CAPACIDADES-APROBADA.md` | 1132 | `10cafb5ceee44f576d327ce614c14c86eb7b22ff43c3dfb82918b785eb36fb04` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 37 | `docs/rediseno/a-ENMIENDA-E1-ENC.md` | 211 | `18dae19523b25ed4a2370ea9c1d23d68beb578f9365bd54587d2f2821093d4da` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 38 | `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | 230 | `9d5a23806fc33fc1d76ba6be9b46ae3499c729c1f11203f80b32550c658ed2eb` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 39 | `docs/rediseno/b-RECORRIDO-APROBADA.md` | 1288 | `f8cb974316e283fa2f16f9ecdd3b94ac19bf4a20cf5816cd155a2449f02719b4` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 40 | `kernel/KERNEL.md` | 1590 | `aa635dff79e73fe13e271cb115653ebc042dc834d32007c634c8ee1df07e3150` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 41 | `kernel/operativo/capacidades/APR/CAPACIDAD.md` | 95 | `a8709115309095849707e2d42290631dca6b3de95d49cc2c3c7ffa4e0546d708` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 42 | `kernel/operativo/capacidades/ARQ/CAPACIDAD.md` | 104 | `6ca11b5f09883e24834f770e61963ae69ca738770ffb1de64f7be0afe4757a47` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 43 | `kernel/operativo/capacidades/CON/CAPACIDAD.md` | 107 | `e0f79e6c3a467302c3d16aa5ee4ccb45583daf146d1676b2b06995419656c5d5` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 44 | `kernel/operativo/capacidades/DIS/CAPACIDAD.md` | 147 | `06f019010d45771fd2a125f9f08f88159b45f15e9f83fd2404c7f2a23f32ad06` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 45 | `kernel/operativo/capacidades/DOM/CAPACIDAD.md` | 135 | `926c7144cb098caaa0b87cdebb5c49b955b74832bc238e66d501ecbb2a635bb3` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 46 | `kernel/operativo/capacidades/DSP/CAPACIDAD.md` | 152 | `acb292f882e77d74693caaab3e392a0d691e988cf875ca4394c59f859ebe7937` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 47 | `kernel/operativo/capacidades/ENC/CAPACIDAD.md` | 174 | `f71b8e43f6e2d66f0801d53ce6e018806d33ef9b5ad5b3300bf1d38fe834d946` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 48 | `kernel/operativo/capacidades/ENT/CAPACIDAD.md` | 123 | `91a81d3cf1cbfa619b7b69553a01810d7074b419fc7e2efb5f8ff2f8f9e7f9ed` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 49 | `kernel/operativo/capacidades/INV/CAPACIDAD.md` | 96 | `47412638e7552da14b7bb89e590aea2f37cc61116c83b902e32952647380ed36` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 50 | `kernel/operativo/capacidades/PLT/CAPACIDAD.md` | 108 | `a5f87977c58ed1d0d4deb3504d664a47fc90382a9790986e5aa277f1dad130d2` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 51 | `kernel/operativo/capacidades/PRD/CAPACIDAD.md` | 105 | `e83b0e08272e219db0c5cc2e17b6d1a95dc4304a9f381d3acfe9c76ff528e3b3` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 52 | `kernel/operativo/capacidades/SEG/CAPACIDAD.md` | 135 | `19bfd38a7a24b57fbec8365327926f7e281092a9e33a06e59355cfda5a5e5a13` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 53 | `kernel/operativo/capacidades/SIS/CAPACIDAD.md` | 119 | `02089f36d124435669b7cf14cf46abd1365a860a4842b739663310b8ceb41628` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 54 | `kernel/operativo/capacidades/USO/CAPACIDAD.md` | 94 | `65f144e4a5c756ef97596a997673d7ad73c194ee6936e616bafd434302ff5d0d` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 55 | `kernel/operativo/capacidades/VER/CAPACIDAD.md` | 135 | `91a16b482629daf3455a3c6963a0568a7a68bcd2bd5553e7540d8c9edbfaf0e2` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 56 | `kernel/operativo/contratos/00-INDICE.md` | 29 | `0b9562119f0b5b5c3f59e66c09446129fbe56865983d6424b76825bf570d004c` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 57 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | 161 | `825f15a914c10d6f07f74e62967f93743efcf629a13379acb3947e70e2952ffa` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 58 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | 539 | `3ee58ca4bc47988d4e6bdd652e2ea5de79ebcf8be79270664c0bd4b4cf391510` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 59 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | 150 | `d56bf6b81e0fe4a9b3ba811f1adf57748cbae65692db557d15960c8506f84234` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 60 | `kernel/operativo/contratos/C4-MATERIALIZACION.md` | 170 | `670289180e59b176743571a22f22047d20792db266b6426c1c91bd2fd3c1ee81` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 61 | `kernel/operativo/contratos/C5-HANDOFF.md` | 115 | `af6f1a4c4f5def8da0dcecee8ea57c17516b41bbbd4abe963460c21024cc7b9e` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 62 | `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` | 336 | `14805a79aeb07f314a55913864ee7d359ead05a932d59b207b66b6279d3a41e9` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 63 | `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | 250 | `83f82e2be4756a4651e61f1883d2a99f1d141954097a6e4176a3482a951fc69c` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 64 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | 141 | `08f4bea44594e026aee24cdddc93765cba0fa5c197b26adee0a0cad00d2c366a` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 65 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | 352 | `dd323d1aa2f7ede3efa18ac01564b636fff8f0f77beac7db3abed667bbd429ec` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 66 | `kernel/operativo/diseno/02-RUBRICAS.md` | 343 | `8aa8fb18426eac219c275c102f757d50727da2e363d905529c8c061d6721d842` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 67 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | 130 | `5d2f54535c1334c053e27bf99b6b81a15a33be7180adf58ddf884cf79ef3a9c1` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 68 | `kernel/operativo/diseno/05-FIDELIDAD.md` | 129 | `fdabb29f7592e603e755c12f191d189755e795ecee104c9b5f583b1ead56e441` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 69 | `kernel/operativo/entrada/00-INDICE.md` | 28 | `315b2790cb66bb4c2c84272468675c8e77fb5a26b8cc2b95ff56db7ee266ddb1` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 70 | `kernel/operativo/entrada/02-CIRCUITO.md` | 145 | `750d39a29f05e7f2b037f9c246c9869ba80edec493e104e206baadda19c09c70` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 71 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | 187 | `1716bd3d8b48107d28a93e4297a6d93c0e6125107c0cc14811f092641e3d0cd2` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 72 | `kernel/operativo/esquemas/proceso.yaml` | 49 | `bd391d5acddff1342ce307829dfb8494df535dbd1924d44948d1e17176440dcc` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 73 | `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` | 130 | `f56e8fe4872e46b5ccc8bd2b9531cdc9e53247aaec1e36ebcae131efbe3674ac` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |
| 74 | `kernel/operativo/recorrido/01-PROCESOS.md` | 564 | `98b5cbc836121044a1b3b38690331325cd730ac71d1f30da69482937c392ee85` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `8` del documento **29** · árbol `61492c1`. **Nadie declaró haberla leído íntegra en ese gate** |

## 6 · Totales, y las DOS aritméticas — DERIVADAS (`EE-02`)

```text
SOBRE EL ÁRBOL DE LA CANDIDATA
  ASIGNADAS A LECTURA        9   28847 líneas
  ASIGNADAS COMO AGOTADAS    74   59051 líneas · de ellas 3 LEÍDAS y 71 DELEGADAS
  OBLIGATORIO menos ASIGNADO  0    CERO FUENTES SIN ASIGNAR
  ASIGNADO menos LEÍDO        —    la calcula el ADJUDICADOR, no el coordinador

SOBRE EL ÁRBOL DEL GATE — las fuentes sin fila, UNA A UNA y con su razón
  ESTE MANIFIESTO               sin fila, y es INEVITABLE: no puede contener su propio
                                SHA-256. Exención de PUNTO FIJO de `DD-19`, y cubre a ESTE
                                fichero y a NINGÚN OTRO
  LA EVIDENCIA REEJECUTADA      no son fuentes obligatorias: no entran en el universo
  LA FILA DE `00-INDICE.md`     el índice SÍ es fuente obligatoria y SÍ tiene fila; lo que
                                cambia es su SHA-256, y el sobre publica las rutas en que
                                los universos difieren

  CUALQUIER OTRA FUENTE SIN FILA sobre el árbol del gate es un DEFECTO de este manifiesto.
```

## 7 · Lo que este gate tiene que juzgar — Y LO QUE NO

```text
JUZGA, Y SÓLO ESTO:
· **SUFICIENCIA ARQUITECTÓNICA de `F4c`**: ¿queda arquitectura por decidir?
· **COHERENCIA de la nueva frontera `F4c`/`F6`** que `O20` fija
· **COMPLETITUD de los contratos entregados a `F6`**: los DIECIOCHO puntos de §20, ¿se
  pueden construir sin volver a decidir nada?
· **AUSENCIA DE DECISIONES ARQUITECTÓNICAS OCULTAS** detrás de una obligación de `F6`
· **CLASIFICACIÓN CORRECTA de los 22 hallazgos**: un estado primario cada uno, sin omitir,
  sin fusionar en silencio y sin duplicar
· **IMPOSIBILIDAD DE PRESENTAR DEUDA DE `F6` COMO IMPLEMENTACIÓN EXISTENTE**, en cualquier
  sede del corpus
· **TRAZABILIDAD COMPLETA hasta PesquerApp**, y que no pueda iniciarse antes de certificar `F6`
· **COBERTURA VERIFICABLE** del corpus asignado

NO PUEDE declarar insuficiente a `F4c` ÚNICAMENTE porque el verificador de `F6` todavía no
esté implementado: **esa ausencia es ESPERADA y está DECLARADA**, y `O20` la fija.

SÍ DEBE declarar insuficiente si:
· falta una REGLA necesaria para construirlo
· existen DOS soluciones arquitectónicas incompatibles sin decidir
· falta PROPIETARIO, FASE o CRITERIO DE CIERRE en algún contrato
· algún hallazgo se ha ESCONDIDO o SUAVIZADO
· la MATRIZ ADVERSARIAL no especifica una clase reproducida
· PesquerApp PODRÍA INICIARSE antes de certificar `F6`
· una obligación sigue dependiendo de INTERPRETACIÓN HUMANA NO NORMADA
```

## 8 · Regla de cierre

```text
CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA.
CUALQUIER DIFERENCIA ENTRE LOS SOBRES DE DOS REVISORES INVALIDA EL GATE.
LA SEDE CANÓNICA que no coincida con la huella recibida FALLA CERRADO.

EL VEREDICTO es uno de estos dos literales, y NO hay estados intermedios:
    SUFICIENTE PARA F5
    INSUFICIENTE PARA F5

EL ADJUDICADOR NO CORRIGE, NO RESUELVE POR MAYORÍA Y NO SUAVIZA.
```

## 9 · La validación de ESTE commit (`DD-17`)

```text
BATERÍA DEL GATE      38/38 en verde · EXIT=0
RUNNER CANÓNICO       13/13 validadores · 13 evidencias publicadas · 0 problemas
DETERMINISMO          `git status --porcelain` VACÍO tras correr el runner
HUELLA DEL KERNEL     LIMPIO, coincide con el release
T147                  SUPERADA
INTÉRPRETE            Python 3.12.14, y se dice

**Y ESTAS CIFRAS NO PRUEBAN QUE LOS CONTRATOS DE `F6` ESTÉN IMPLEMENTADOS.** `O20` lo
escribe: la batería es EVIDENCIA DE CONSISTENCIA DEL CORPUS, y un verde suyo no demuestra
que el verificador de `F6` esté construido ni certificado.
```
