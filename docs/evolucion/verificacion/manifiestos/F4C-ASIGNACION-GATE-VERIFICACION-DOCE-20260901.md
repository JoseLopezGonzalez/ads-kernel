# MANIFIESTO PREVIO DE ASIGNACIÓN — GATE DE VERIFICACIÓN DE LOS DOCE HALLAZGOS `HH2`

> **EMITIDO ANTES DE REPARTIR**, commiteado **ANTES de que exista ningún revisor**, y después
> de cerrar todo `verificacion/`. Una vez commiteado no se modifica.
>
> **QUÉ SE JUZGA AQUÍ, Y QUÉ NO.** Se juzga si la tanda que aplicó los DOCE hallazgos del gate
> anterior los cerró de verdad, si alguno quedó a medias, si alguno introdujo un defecto nuevo
> y si alguno se suavizó cambiándolo de fase. **No se juzga que `F6` no esté implementado**:
> §7 lo escribe entero, con lo que puede y lo que no puede fundar insuficiencia.
>
> **NADIE HA CERTIFICADO NADA TODAVÍA.** La corrección está APLICADA y NO CERTIFICADA, la
> OPCIÓN C sigue activada, y este gate no la levanta: sólo juzga.
>
> **Aplica los remedios que los gates anteriores dejaron escritos para este documento:**
> `DD-17` · `DD-19` · `EE-02` · **`C-05`**, ninguna frase afirma un reparto que su §4 no dé ·
> **`C-10`**, la columna de agotamiento distingue LEÍDA de AGOTADA POR DELEGACIÓN.

## 1 · Objeto del reparto

```text
COMMIT CANDIDATO   909a7a1473c732308306805da9144b4ff9fc0977
TREE SHA           44585ff8c5ad81d3c2aca0d502613344bb3399dd
REFERENCIA REMOTA  refs/heads/review/f4c-doce-hallazgos-o21-candidate-20260901
BASE DEL RANGO     eafd2ee46852dd69d4704c21b73c4f7a54f36155 — un solo commit sobre ella
FECHA              2026-09-01
RAMA DEL GATE      gate/f4c-verificacion-doce-20260901, creada sobre ese commit exacto
QUÉ TRAE           los DOCE hallazgos `HH2-01`…`HH2-12` del documento 31, aplicados con el
                   remedio que ese gate adjudicó, en CINCO ficheros. Entre ellos: §20.5
                   deriva ÁRBOLES ADVERSARIALES y no identificadores de hallazgo, y el
                   OCTAVO —`DD-01`— vuelve a `SIS`/`F4c`; el comando de la regla 7 deja de
                   devolver el conjunto vacío y gana control positivo; §18 enuncia UNA sola
                   condición de entrada para su paso 8.
ESTADO DECLARADO   APLICADO y NO CERTIFICADO · `F4c` ABIERTA · `F5` NO autorizada ·
                   OPCIÓN C ACTIVA · `C-L.5` ABIERTA · `C-L.7` NO CERRADA ·
                   `M-04` NO superada · **PesquerApp BLOQUEADA** ·
                   **ningún hallazgo declarado SUPERADO**
```

## 2 · El universo obligatorio se DERIVA, y cada cifra dice de qué árbol habla

```bash
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py | tail -1
```

```text
SOBRE EL ÁRBOL DE LA CANDIDATA   88 fuentes · 93831 líneas — el objeto de este gate
SOBRE EL ÁRBOL DEL GATE          NO se copia: se DERIVA con el mismo comando sobre él, y su
                                 resta va enumerada fuente a fuente en §6
```

## 3 · Los agentes, y sus marcas se DERIVARON del expediente

```text
REVISOR `JA`      REMEDIOS, TRAZABILIDAD, GIT Y COMPROBACIONES DIRIGIDAS. Adjudica
                  `HH2-01`…`HH2-12` uno por uno con `CERRADO`, `FALLIDO` o `NO APLICABLE`.
                  Reproduce el defecto en la base cuando sea posible y el remedio en la
                  candidata, y comprueba la CLASE, no sólo la línea.
REVISOR `JB`      SUFICIENCIA ARQUITECTÓNICA, CONTRATOS, FASES Y ESTADO. `O20` y `O21` en la
                  sede, las condiciones `C-L`, `M-04`, §18, §19 y §20 enteras, todas las
                  filas `V6` y su clasificación semántica, y si queda arquitectura oculta.
ADJUDICADOR `JC`  recibe los DOS dictámenes YA CERRADOS, recalcula universo, asignaciones,
                  líneas y digests, reproduce en clones desechables y **NO decide por
                  mayoría**. No corrige.

CÓMO SE ELIGIERON LAS MARCAS, y no fue de memoria: se barrieron las marcas de revisor y de
adjudicador de todos los documentos de gate y de todos los manifiestos publicados —53
consumidas, de `A` a `Z` y las series de dos letras— y se tomaron las tres primeras libres
cuya inicial no abre ninguna serie viva. Las tres casan con `^[A-Z]{1,2}[0-9]?$`, que es lo
que el emisor del sobre exige, y **ninguna aparece en el expediente**.

INDEPENDENCIA     ninguno de los tres ha escrito este corpus, aplicado ninguna corrección ni
                  participado en NINGÚN gate anterior. `JA` y `JB` en PARALELO y SIN VERSE;
                  `JC` no ve nada hasta que los dos cierran. **Ninguno modifica el árbol.**
EL SOBRE          se emite UNA vez a un fichero FUERA del repositorio auditado y los tres
                  leen de ahí. **No se transcribe.**
```

**`C-05`, aplicado y comprobable contra la tabla de abajo:** `JA` lee del documento 11
`L1-L5200` y del `CHECKPOINT` `L1-L2900` —el bloque reanudable entero, donde viven `HH2-02`,
`HH2-04`, `HH2-05` y `HH2-10`—; `JB` lee `L5201-L12104` del documento 11 —§15.4, §15.8, §18,
§19 y §20 entera— y `L2901-L6021` del `CHECKPOINT` —la clasificación `C-L`, la matriz de los
22 y el bloque de `M-04`—. **La SEDE CANÓNICA la leen LOS TRES.** Si esta frase difiere de §4,
manda §4.

## 4 · Reparto para LECTURA ÍNTEGRA

| # | ruta | líneas | SHA-256 | `1bis` | revisor | reparto |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 255 | `6339aa806335ce93d91cc66fa4ecb1231a285e7934f39f527ba909c08c54e187` | v | **JB** | JB |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 12103 | `e65c9c02572ce63d47f68673b3c9d083e85dc56f8c5ccd40e53afb4cf02a69ec` | iii | **JA+JB** | JA `L1-L5200` —§0 a §9.5, con §2.1 y la regla de titulares— · JB `L5201-L12104`, que contiene **§15.4, §15.8, §18, §19 y §20 entera**, la sede `C-L.5`·`1bis` y `PN-19` |
| 3 | `docs/evolucion/30-GATE-ARQUITECTONICO-FINAL-F4C.md` | 3084 | `712058b2467287d7ca51380cf305e84ac311f141d1c12ec0649c8b901aee6503` | iv | **JA** | JA · es la sede del remedio adjudicado de `H-06` que `HH2-01` invoca (§9) |
| 4 | `docs/evolucion/31-GATE-FINAL-O21-F4C.md` | 783 | `d184e9528ce38356235d726385eb4cb795d3a75daaaf0e19450fb33c57616eba` | iv | **JA+JB+JC** | los tres · es el gate cuyos DOCE hallazgos se juzgan |
| 5 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 5923 | `1ddaba90c0140c07f3d04712d4269fd390ff9feb7402d2d2bc054fac12799f98` | iii | **JA+JB** | JA `L1-L2900` —el bloque reanudable entero, la regla 7 y la regla 8, y `falta_para_cerrar_la_capa`— · JB `L2901-L6021` —la clasificación `C-L`, la matriz de los 22, el bloque de `M-04` y el parte de la tanda— |
| 6 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 683 | `c0cc2ee5bb5397888f3cbf4c91c088600d2e7d1bd5db0b88001cbeb58d86760c` | v | **JA** | JA · §19 es donde vive la tercera sede de `HH2-08` |
| 7 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 559 | `ebfef288de70d1ec6d58306720440b9a4c706197cc66f99b92e54a147678fc9a` | v | **JA+JB+JC** | los tres · es la SEDE CANÓNICA, y `O21` gobierna las dos declaraciones de este gate |
| 8 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1495 | `c8cb3a5ca5a73627f8836cf222d32d28abdf3308d182c0f8e67feee94ddfa1e9` | iii | **JB** | JB · `HH2-09` y las proyecciones `D109` y `D110` |

## 5 · Fuentes AGOTADAS — y la columna distingue LEÍDA de DELEGADA (`C-10`)

```text
LA REGLA QUE SE APLICA, dicha como se ejecuta:
1  LEÍDA        un revisor de un gate anterior declaró LEÍDO ÍNTEGRO DE ESA RUTA, con fila
                propia y citado con documento y rango
2  DELEGADA     el manifiesto de un gate anterior publicó su SHA-256 en fila propia, y ese
                gate la dio por agotada — pero **NADIE declaró haberla leído íntegra allí**
3  en los DOS casos, los BYTES de hoy son IDÉNTICOS a los del árbol que ese gate juzgó, y el
   coordinador lo ha comprobado ruta a ruta contra `2e31452` antes de emitir: ninguna difiere
4  si no se cumple, no se agota, y vuelve a LECTURA ÍNTEGRA
```

| # | ruta | líneas | SHA-256 | `1bis` | tipo | procedencia del agotamiento |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md` | 336 | `202ac1af8df5ca6e032cb06f6566c63cf2656fb1a54d65a8c9a0f5d0ef5d41d9` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 2 | `docs/evolucion/12-CRITICA-INDEPENDIENTE-F4.md` | 764 | `c50e0aa6c1b9827c166171efee1737b2e091cc5518d78bad8c469c709c0dd56f` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 3 | `docs/evolucion/13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md` | 797 | `6804d134dfb66b5304ec9c539750559e578a2d5855785b5803189baac2da931f` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 4 | `docs/evolucion/14-DEVOLUCION-TECNICA-PREVIA-F4C.md` | 325 | `7f94e236f3cfb11e78762a301d9a3e94939ab47df34658710d1b8686ed7050fb` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 5 | `docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` | 651 | `b0e015c118ceb916e58fc8191b2a5e40cf28c44dd426618fdd49d10e3ea495d6` | ii+iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 6 | `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | 1257 | `8243034f286160cc89330af95b49f558af0dd16d1b36a37ccbdf02f74a79d185` | i+iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 7 | `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` | 1650 | `18f876d4cd47a2f7cfde15594f98696cfacf750607cd23811dd40ffb36d6c29c` | i+iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 8 | `docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` | 3665 | `1e71366b10d2293802db435de14953771ebd8fc13b426acedd7c0efe21cdb496` | i+iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 9 | `docs/evolucion/19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md` | 1152 | `48baaa1a8e69c6ef3401eb7a0088dcf06849bd66fa3f238bf3e7b8c8fd14392d` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 10 | `docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md` | 801 | `d7d2e4fa3f878e0c010d979e89affdb63462cc6fdd6628ed885d3a760bde09d1` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 11 | `docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md` | 2679 | `9f869ffbdbdb834ca872c03abc8826c125a47b4344ed32cd9b6266db08f8be03` | iv+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 12 | `docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md` | 3478 | `3e2bdece758e6b69d6695bb52f20d21b910a123a27ac643845dbad75e8355f1c` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 13 | `docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md` | 2913 | `0f81f13d8cb319d8ccc5243d19bb26d7f71f57e860cde2eb2edefe33b6993dc2` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 14 | `docs/evolucion/24-TERCER-GATE-DE-CERTIFICACION-F4C.md` | 2515 | `8df584529c857c071954b0d1b426faff82277e29a43556abe5dccfd93714fae1` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 15 | `docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md` | 2754 | `e8431c653cb7919e8d2ec82c5b4d3d11247a01aa61577bb8e5dd266916fb0e5d` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 16 | `docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md` | 4526 | `e2c34215d92937fb467b1ffdb4e6654f66198ead4dac8128c411469bf86c297e` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 17 | `docs/evolucion/27-SEXTO-GATE-DE-CERTIFICACION-F4C.md` | 3946 | `d81b56366e5062ffe0abcd55ba2ef52ddbc3fadf073ea5a280e6cfc15b87ef26` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 18 | `docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md` | 4275 | `4711738d2a5d64740cc382d7808cf3b185686f80930b3f0d26ff3cf756506854` | iv | **LEÍDA** | LEÍDA ÍNTEGRA · documento **29**, L537 · árbol `2e31452` |
| 19 | `docs/evolucion/29-OCTAVO-GATE-DE-CERTIFICACION-F4C.md` | 4197 | `0b9064490c8dd68ec7c50ed87778d31ab8ab5360c966642113367a0eeba2e5ac` | iv | **LEÍDA** | LECTURA ÍNTEGRA declarada por `U1`, `U2` y `HH` en el documento **30** · árbol `2e31452` |
| 20 | `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | 2163 | `a88609167dbbea2818b7f2e68cbd4c6fc704cb7e2245ee0a2c873052486fd159` | i | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 21 | `docs/evolucion/verificacion/README.md` | 386 | `f216def357a4075e3175bd9a7cb2bedf169fc6114b82bacb4d23d91ae5ba4dbe` | v | **LEÍDA** | LEÍDA ÍNTEGRA · documento **29**, L538 · árbol `2e31452` |
| 22 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 4345 | `6f416b9f08b955770295a762226733acd3d004edb28cc902013c0ee99e3bdb3f` | v | **LEÍDA** | LECTURA ÍNTEGRA declarada por `W1` en el documento **31**, §2, con sus rangos enumerados · árbol `f232d1a` |
| 23 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 857 | `fc8adef3a8baf223fd8bc9ae9403b2e5430c6c5f4cc09e83803d301b920fd0be` | v | **LEÍDA** | LECTURA ÍNTEGRA declarada por `W1` en el documento **31**, §2 (`1-857`) · árbol `f232d1a` |
| 24 | `docs/evolucion/verificacion/emitir-sobre-de-ancla.py` | 791 | `f915a840fae8b1553082ccbf381551b8a3abb10dd515a64d314a32772e30d20a` | v | **LEÍDA** | LECTURA ÍNTEGRA declarada por `W1` en el documento **31**, §2 (`1-791`) · árbol `f232d1a` |
| 25 | `docs/evolucion/verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` | 119 | `b1c29244dfedc139ff7e80a6167d200803d054f25554c75f31303fea5687a434` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 26 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md` | 256 | `ff4116703b648586bae866cd259f37f7800088e8fe2148b4f4224b466322fc13` | v | **LEÍDA** | LECTURA ÍNTEGRA declarada por `W1` en el documento **31**, §2 (`1-256`) · árbol `f232d1a` |
| 27 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` | 240 | `c64a0ec4731e6d27751469e84cbcc33104bfe535c42efe4f98533f4d84a0b970` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 28 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` | 316 | `fc4d1c2fdedbcb13be512e88303e21eddbeb194f6cc38b8e50fa0612dad08bbc` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 29 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md` | 210 | `ac9e0edd59cf3e1b783b42ce0fc052e1eb28af7d5d66e218709d76589f724988` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 30 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md` | 221 | `fc4902591eff43bc6736f626fdf2dd1bef7c4f193b1be31f3ddf26f436adb599` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 31 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md` | 193 | `0f08b961c31f03bbedbae700fa67029ac87b6b962067b39b3e504fe28e8d1939` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 32 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md` | 278 | `528dd68fc81134c16f874ab5803996ec50ee838241fd95470a9e07dd66770b2c` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 33 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md` | 292 | `41a4ff29d11c1edf26e6370ea7bcf8cf1ee24d75895336d991b6c12fa4251924` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 34 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md` | 260 | `f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 35 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md` | 248 | `a82e74968e4ca31fbae0825a43f295736af39e58a16b3adf8879d021688e3d76` | v | **LEÍDA** | LECTURA ÍNTEGRA declarada por `U1` en el documento **30** · árbol `2e31452` |
| 36 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md` | 140 | `c843b0c341183859b7f0f07db78cc67eade7ef98c4a96ad3edee23c769d2a976` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 37 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-FINAL-O21-20260901.md` | 284 | `3dc69768487de794aae577df3468abd97cae30a87b867e3920bb46e02fc5a529` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** en su fila 11, asignada a `W1` · árbol `2e31452`. **NADIE declaró haberla leído íntegra allí** |
| 38 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-FINAL-O21-20260901B.md` | 303 | `4a27b5ef2146753afa5ab8c1c6fc95b195d97e493a28af642ebf97c5ef5090f8` | v | **LEÍDA** | LECTURA ÍNTEGRA declarada por `W1`, `W2` **y el adjudicador `WA`** en el documento **31** · árbol `2e31452` |
| 39 | `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | 3343 | `64d170f5acc151445eff6f3f68a0bade91d00744dffa6bdf36c13cd2d366bd3e` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 40 | `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | 597 | `48412108f711204f5389e17fac974133e848737676eb4c57ba5b22c6a37ab8b0` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 41 | `docs/rediseno/CHECKPOINT-OPERATIVO.md` | 195 | `d2131faa4aeddc6d66e98f5eb88d6d9d172a8910b174a1866eecc969633818bb` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 42 | `docs/rediseno/a-CAPACIDADES-APROBADA.md` | 1132 | `10cafb5ceee44f576d327ce614c14c86eb7b22ff43c3dfb82918b785eb36fb04` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 43 | `docs/rediseno/a-ENMIENDA-E1-ENC.md` | 211 | `18dae19523b25ed4a2370ea9c1d23d68beb578f9365bd54587d2f2821093d4da` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 44 | `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | 230 | `9d5a23806fc33fc1d76ba6be9b46ae3499c729c1f11203f80b32550c658ed2eb` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 45 | `docs/rediseno/b-RECORRIDO-APROBADA.md` | 1288 | `f8cb974316e283fa2f16f9ecdd3b94ac19bf4a20cf5816cd155a2449f02719b4` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 46 | `kernel/KERNEL.md` | 1590 | `aa635dff79e73fe13e271cb115653ebc042dc834d32007c634c8ee1df07e3150` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 47 | `kernel/operativo/capacidades/APR/CAPACIDAD.md` | 95 | `a8709115309095849707e2d42290631dca6b3de95d49cc2c3c7ffa4e0546d708` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 48 | `kernel/operativo/capacidades/ARQ/CAPACIDAD.md` | 104 | `6ca11b5f09883e24834f770e61963ae69ca738770ffb1de64f7be0afe4757a47` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 49 | `kernel/operativo/capacidades/CON/CAPACIDAD.md` | 107 | `e0f79e6c3a467302c3d16aa5ee4ccb45583daf146d1676b2b06995419656c5d5` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 50 | `kernel/operativo/capacidades/DIS/CAPACIDAD.md` | 147 | `06f019010d45771fd2a125f9f08f88159b45f15e9f83fd2404c7f2a23f32ad06` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 51 | `kernel/operativo/capacidades/DOM/CAPACIDAD.md` | 135 | `926c7144cb098caaa0b87cdebb5c49b955b74832bc238e66d501ecbb2a635bb3` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 52 | `kernel/operativo/capacidades/DSP/CAPACIDAD.md` | 152 | `acb292f882e77d74693caaab3e392a0d691e988cf875ca4394c59f859ebe7937` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 53 | `kernel/operativo/capacidades/ENC/CAPACIDAD.md` | 174 | `f71b8e43f6e2d66f0801d53ce6e018806d33ef9b5ad5b3300bf1d38fe834d946` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 54 | `kernel/operativo/capacidades/ENT/CAPACIDAD.md` | 123 | `91a81d3cf1cbfa619b7b69553a01810d7074b419fc7e2efb5f8ff2f8f9e7f9ed` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 55 | `kernel/operativo/capacidades/INV/CAPACIDAD.md` | 96 | `47412638e7552da14b7bb89e590aea2f37cc61116c83b902e32952647380ed36` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 56 | `kernel/operativo/capacidades/PLT/CAPACIDAD.md` | 108 | `a5f87977c58ed1d0d4deb3504d664a47fc90382a9790986e5aa277f1dad130d2` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 57 | `kernel/operativo/capacidades/PRD/CAPACIDAD.md` | 105 | `e83b0e08272e219db0c5cc2e17b6d1a95dc4304a9f381d3acfe9c76ff528e3b3` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 58 | `kernel/operativo/capacidades/SEG/CAPACIDAD.md` | 135 | `19bfd38a7a24b57fbec8365327926f7e281092a9e33a06e59355cfda5a5e5a13` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 59 | `kernel/operativo/capacidades/SIS/CAPACIDAD.md` | 119 | `02089f36d124435669b7cf14cf46abd1365a860a4842b739663310b8ceb41628` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 60 | `kernel/operativo/capacidades/USO/CAPACIDAD.md` | 94 | `65f144e4a5c756ef97596a997673d7ad73c194ee6936e616bafd434302ff5d0d` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 61 | `kernel/operativo/capacidades/VER/CAPACIDAD.md` | 135 | `91a16b482629daf3455a3c6963a0568a7a68bcd2bd5553e7540d8c9edbfaf0e2` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 62 | `kernel/operativo/contratos/00-INDICE.md` | 29 | `0b9562119f0b5b5c3f59e66c09446129fbe56865983d6424b76825bf570d004c` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 63 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | 161 | `825f15a914c10d6f07f74e62967f93743efcf629a13379acb3947e70e2952ffa` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 64 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | 539 | `3ee58ca4bc47988d4e6bdd652e2ea5de79ebcf8be79270664c0bd4b4cf391510` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 65 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | 150 | `d56bf6b81e0fe4a9b3ba811f1adf57748cbae65692db557d15960c8506f84234` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 66 | `kernel/operativo/contratos/C4-MATERIALIZACION.md` | 170 | `670289180e59b176743571a22f22047d20792db266b6426c1c91bd2fd3c1ee81` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 67 | `kernel/operativo/contratos/C5-HANDOFF.md` | 115 | `af6f1a4c4f5def8da0dcecee8ea57c17516b41bbbd4abe963460c21024cc7b9e` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 68 | `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` | 336 | `14805a79aeb07f314a55913864ee7d359ead05a932d59b207b66b6279d3a41e9` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 69 | `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | 250 | `83f82e2be4756a4651e61f1883d2a99f1d141954097a6e4176a3482a951fc69c` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 70 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | 141 | `08f4bea44594e026aee24cdddc93765cba0fa5c197b26adee0a0cad00d2c366a` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 71 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | 352 | `dd323d1aa2f7ede3efa18ac01564b636fff8f0f77beac7db3abed667bbd429ec` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 72 | `kernel/operativo/diseno/02-RUBRICAS.md` | 343 | `8aa8fb18426eac219c275c102f757d50727da2e363d905529c8c061d6721d842` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 73 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | 130 | `5d2f54535c1334c053e27bf99b6b81a15a33be7180adf58ddf884cf79ef3a9c1` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 74 | `kernel/operativo/diseno/05-FIDELIDAD.md` | 129 | `fdabb29f7592e603e755c12f191d189755e795ecee104c9b5f583b1ead56e441` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 75 | `kernel/operativo/entrada/00-INDICE.md` | 28 | `315b2790cb66bb4c2c84272468675c8e77fb5a26b8cc2b95ff56db7ee266ddb1` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 76 | `kernel/operativo/entrada/02-CIRCUITO.md` | 145 | `750d39a29f05e7f2b037f9c246c9869ba80edec493e104e206baadda19c09c70` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 77 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | 187 | `1716bd3d8b48107d28a93e4297a6d93c0e6125107c0cc14811f092641e3d0cd2` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 78 | `kernel/operativo/esquemas/proceso.yaml` | 49 | `bd391d5acddff1342ce307829dfb8494df535dbd1924d44948d1e17176440dcc` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 79 | `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` | 130 | `f56e8fe4872e46b5ccc8bd2b9531cdc9e53247aaec1e36ebcae131efbe3674ac` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 80 | `kernel/operativo/recorrido/01-PROCESOS.md` | 564 | `98b5cbc836121044a1b3b38690331325cd730ac71d1f30da69482937c392ee85` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto `B` del documento **31** · árbol `2e31452`. **Nadie declaró haberla leído íntegra en aquel gate** |

## 6 · Totales, y las DOS aritméticas — DERIVADAS (`EE-02`)

```text
SOBRE EL ÁRBOL DE LA CANDIDATA
  ASIGNADAS A LECTURA         8   24885 líneas
  ASIGNADAS COMO AGOTADAS    80   68946 líneas · de ellas 9 LEÍDAS y 71 DELEGADAS
  SUMA                       88   93831 líneas, que es el universo derivado de §2
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

## 7 · Lo que este gate tiene que responder — Y LO QUE NO PUEDE FUNDAR INSUFICIENCIA

```text
LAS DIECIOCHO PREGUNTAS, y son la lista entera:
 1 ¿los DOCE identificadores aparecen exactamente una vez?
 2 ¿`HH2-01` está cerrado POR PROPIEDAD —el conjunto derivado son ÁRBOLES, con cabecera e
   identificador estable, y entrada, escenario y cierre remiten al mismo conjunto?
 3 ¿`HH2-02` está cerrado con un control NO TAUTOLÓGICO, que entra en la valla, deriva los
   catorce campos y delata una copia introducida?
 4 ¿`HH2-03`…`HH2-12` están cerrados?
 5 ¿queda algún remedio PARCIAL?
 6 ¿algún remedio introdujo un DEFECTO NUEVO?
 7 ¿algún hallazgo se SUAVIZÓ cambiándolo de fase?
 8 ¿`C-L.5` se certifica conforme a `O21`?
 9 ¿`C-L.7` queda cerrada?
10 ¿`M-04` queda superada o mantiene deuda?
11 ¿`V6-15` es CONSTRUIBLE?
12 ¿`V6-16` declara correctamente `PN-19` y su dependencia de `F5`?
13 ¿`V6-19` contiene MATERIALMENTE la obligación de `C-11`?
14 ¿los contratos de `F6` son completos y están correctamente clasificados?
15 ¿queda alguna decisión ARQUITECTÓNICA sin tomar?
16 ¿PesquerApp sigue BLOQUEADA hasta certificar `F6`?
17 ¿alguna deuda de `F6` se presenta falsamente como implementación?
18 ¿puede cerrarse `F4c` sin ejecutar `F6`?

NO CONSTITUYE DEFECTO DE `F4c`, y no puede fundar insuficiencia por sí solo:
· que el verificador de `F6` no esté implementado
· que los contratos de `F6` no estén ejecutados
· que PesquerApp no haya comenzado
· que no exista runtime operativo
· que una deuda esté CORRECTAMENTE asignada a `F5`/`F6` con propietario, fase y criterio
· que la batería interna no certifique la implementación futura de `F6`

SÍ CONSTITUYE DEFECTO:
· contrato NO CONSTRUIBLE · fase incorrecta · obligación ausente · dependencia no declarada
· arquitectura oculta · cobertura incompleta · hallazgo suavizado · contradicción vigente
· remedio que introduce otro defecto · PesquerApp que pueda iniciarse antes de `F6`

LÍMITE DE HALLAZGOS NUEVOS. Un hallazgo que no sea uno de los doce sólo sostiene
insuficiencia si es REPRODUCIBLE, afecta DIRECTAMENTE a una condición de cierre de `F4c`,
cita FICHERO Y LÍNEA, identifica el contrato incumplido, declara si lo introdujo `909a7a` y
su remedio NO pertenece a la implementación futura de `F6`. **No se abre auditoría ilimitada.**
```

## 8 · Manifiestos de lectura — lo que cada revisor entrega ANTES de cerrar

```text
POR CADA FUENTE ASIGNADA:  ruta · nº de líneas · SHA-256 RECALCULADO · `LEÍDA ÍNTEGRA` o los
                           TRAMOS EXACTOS no abiertos · primera sección sustantiva · última
                           sección sustantiva · DOS ANCLAS de regiones separadas
Y AL CERRAR:               declaración CONTRA SU PROPIO INTERÉS y el conjunto
                           `ASIGNADO − LEÍDO`

REGLAS, Y NO ADMITEN LECTURA BLANDA:
· toda fuente asignada debe leerse ÍNTEGRAMENTE
· `grep`, búsquedas dirigidas y fragmentos **NO equivalen** a lectura íntegra, y quien los
  use lo dice y no los cuenta
· no se reasignan fuentes después del cierre
· si un revisor no termina una fuente, LO DECLARA, y `C-L.5` queda ABIERTA
· **no se oculta una lectura incompleta para salvar el gate**
```

## 9 · Regla de cierre — DOS declaraciones separadas, y `O21` prohíbe condicionar una a otra

```text
  (A) COBERTURA      `C-L.5 CERTIFICADA PARA ESTE GATE`
                 ó   `C-L.5 ABIERTA: condición <número y causa exacta>`
                     **Si las SEIS condiciones de `O21` se cumplen, el adjudicador DEBE
                     certificar, AUNQUE el gate sea insuficiente por otros defectos.** No es
                     discrecional y no depende del veredicto global.

  (B) SUFICIENCIA    `SUFICIENTE PARA F5`   ó   `INSUFICIENTE PARA F5`. Sin estados
                     intermedios.

CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA.
CUALQUIER DIFERENCIA ENTRE LOS SOBRES DE DOS REVISORES INVALIDA EL GATE.
LA SEDE CANÓNICA que no coincida con la huella recibida FALLA CERRADO.

EL ADJUDICADOR NO CORRIGE, NO RESUELVE POR MAYORÍA Y NO SUAVIZA. Y distingue cuatro cosas:
defecto PREEXISTENTE · defecto INTRODUCIDO por `909a7a` · defecto del APARATO de este gate ·
deuda LEGÍTIMA de `F5`/`F6`.

DURANTE TODO EL GATE NO SE CORRIGE NADA: ni la candidata, ni los instrumentos, ni los
estados, ni la evidencia. Un gate no corrige.
```

## 10 · La validación de ESTE commit (`DD-17`)

```text
BATERÍA DEL GATE      38/38 en verde · EXIT=0 · desde la raíz y desde otro cwd
RUNNER CANÓNICO       13/13 validadores · 13 evidencias publicadas · 0 problemas
WORKSPACE             57/57
NEGATIVAS             67 infracciones detectadas · 0 NO detectadas
DETERMINISMO          `git status --porcelain` VACÍO tras correr el runner
T147 · T158 · T161    SUPERADAS
INTÉRPRETE            Python 3.12.14, y se dice

**Y ESTAS CIFRAS NO CERTIFICAN NADA DE LOS DOCE.** La batería es evidencia de consistencia
del corpus; ninguno de los doce hallazgos se declara superado por un verde suyo, y ninguno
de los puntos de §20 está implementado.
```
