# MANIFIESTO PREVIO DE ASIGNACIÓN — GATE FINAL DE `F4c`, EL PRIMERO BAJO `O21` · **`B`**

> **EMITIDO ANTES DE REPARTIR**, commiteado **ANTES de que exista ningún revisor**, y
> **después de cerrar todo `verificacion/`**. Una vez commiteado no se modifica.
>
> **ESTE ES EL ÚLTIMO GATE AUTORIZADO DE ESTA SERIE.** Después de su veredicto el método se
> detiene, cualquiera que sea el resultado: no se corrigen sus hallazgos, no se abre otro
> gate y no se inicia `F5`, `F6` ni PesquerApp. El coordinador lo dice aquí, antes de
> repartir, para que ningún revisor pueda pensar que suavizar algo abre un camino.
>
> **QUÉ LO DISTINGUE DEL ANTERIOR.** Aquel fue el primero bajo `O20` —la frontera de fase—.
> Éste es el primero bajo **`O21`**, que quita la última ambigüedad que quedaba sin normar:
> si certificar cobertura es un acto discrecional y si depende del veredicto de suficiencia.
> **Ya no lo es**, y §8 escribe cómo se cierra en consecuencia.
>
> **Aplica los remedios que los gates anteriores dejaron escritos para este documento:**
> `DD-17` · `DD-19` · `EE-02` · **`C-05`**, el reparto se comprueba contra la propia tabla y
> ninguna frase afirma lo que la tabla no dé · **`C-10`**, la columna de agotamiento
> **distingue LEÍDA de AGOTADA POR DELEGACIÓN**.

> **POR QUÉ ESTE MANIFIESTO ES `B`, Y QUÉ PASA CON EL ANTERIOR.** El manifiesto
> [`F4C-ASIGNACION-GATE-FINAL-O21-20260901.md`](F4C-ASIGNACION-GATE-FINAL-O21-20260901.md)
> se commiteó con la marca `ADJ` para el adjudicador, y **el emisor del sobre se niega a
> emitir sobre él**: sus marcas de revisor tienen que casar con `^[A-Z]{1,2}[0-9]?$`, y
> `ADJ` no casa. Un emisor que adivinara a quién se asignó una fuente sería exactamente lo
> que `X-05` cerró. **Los manifiestos no se editan una vez commiteados**, así que aquél
> queda PUBLICADO E INTACTO como lo que es —un manifiesto sobre el que no se puede emitir
> sobre, y por tanto no operativo— y éste lo sustituye con la marca **`WA`**. Es el mismo
> precedente que los manifiestos `4B` y `6B`.
>
> **QUÉ CAMBIA respecto de aquél, y es todo lo que cambia:** la marca del adjudicador
> —`ADJ` → `WA`— y **una fila más en §4**, la del propio manifiesto anterior, que sobre el
> árbol del gate es una fuente obligatoria nueva y necesita revisor. **Ni una asignación se
> mueve, ni una cifra del universo cambia sobre el árbol de la CANDIDATA**, que es el objeto
> del gate y no contiene ninguno de los dos.

## 1 · Objeto del reparto

```text
COMMIT CANDIDATO   f232d1aab53a8c6dfb9e80cd9a669aad9fcf35b3
TREE SHA           4ced788caab8e0cfc59cd4fa894d9015848565e4
REFERENCIA REMOTA  refs/heads/review/f4c-o21-semantica-de-cl5-candidate-20260901
FECHA              2026-09-01
RAMA DEL GATE      gate/f4c-final-o21-20260901, creada sobre ese commit exacto
QUÉ TRAE           **`O21` DEL OWNER**, registrada en la SEDE CANÓNICA —append-only— y
                   proyectada en `O21`, `D110`, §15.4 y §15.8; y **los DIECISÉIS hallazgos
                   del gate anterior aplicados, uno por identificador**, con su parte y su
                   comando de cobertura en el `CHECKPOINT`. Entre ellos: `C-20` vuelve a
                   `F4c` y **el sobre transporta materialmente el texto íntegro de `O19`**;
                   §18 gana el nodo del verificador con la arista que bloquea PesquerApp;
                   `V6-15` deriva su conjunto de fixtures en vez de enumerarlo; `V6-16`
                   declara su dependencia de `PN-19`; `C-11` estrena `V6-19`; y `C-L.7` se
                   barre como CLASE, con la garantía escrita DENTRO del bloque reanudable.
ESTADO DECLARADO   APLICADO y NO CERTIFICADO · `F4c` ABIERTA · `F5` NO autorizada ·
                   `M-04` NO superada · `C-L.5` ABIERTA · `C-L.7` NO CERRADA ·
                   **PesquerApp BLOQUEADA** · **ningún hallazgo declarado SUPERADO**
```

## 2 · El universo obligatorio se DERIVA, y cada cifra dice de qué árbol habla

```bash
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py | tail -1
```

```text
SOBRE EL ÁRBOL DE LA CANDIDATA   85 fuentes · 92110 líneas — el objeto de este gate
SOBRE EL ÁRBOL DEL GATE          NO se copia: se DERIVA con el mismo comando sobre él, y su
                                 resta va enumerada fuente a fuente en §6
```

## 3 · Los agentes

```text
REVISOR `W1`      el APARATO: emisor del sobre, batería, derivador, manifiestos, contratos
                  de `F6` y la frontera `F4c`/`F6`. **Audita si `C-20` está realmente
                  cerrado en el artefacto y si lo entregado a `F6` se puede construir.**
REVISOR `W2`      la ARQUITECTURA DOCUMENTAL: decisiones, resoluciones, checkpoint, índice,
                  procesos, capacidades, presiones y la trazabilidad hasta PesquerApp.
                  **Audita `O21`, la clase `C-L.7` y que ningún cardinal vuelva a caducar.**
ADJUDICADOR `WA` recibe los DOS dictámenes YA CERRADOS, reproduce sus afirmaciones contra
                  FICHERO Y LÍNEA y **NO resuelve por mayoría**. No corrige.

INDEPENDENCIA     ninguno de los tres ha escrito F4, aplicado ninguna corrección, ni
                  participado en NINGÚN gate anterior —`A` a `HH` incluidos—. `W1` y `W2` en
                  PARALELO y SIN VERSE; `WA` no ve nada hasta que los dos cierran.
EL SOBRE          se emite UNA vez a un fichero FUERA del repositorio auditado y los tres
                  leen de ahí. **No se transcribe.**
```

**`C-05`, aplicado y comprobable contra la tabla de abajo:** `W1` lee del documento 11
`L1-L5200` **y `L7700-L12071`**, rango que contiene §11.6 con los campos 17-18-19 y el paso
`6ter`, §11.8, §11.9, la sede `C-L.5`·`1bis`, `PN-19` y **§20 entera**. `W2` lee
`L5201-L12071`. **La SEDE CANÓNICA DEL OWNER la leen LOS TRES**, porque `O21` nace en ella.
**Ninguna frase de este manifiesto afirma un reparto que su §4 no dé**: si difieren, manda §4.

## 4 · Reparto para LECTURA ÍNTEGRA

| # | ruta | líneas | SHA-256 | `1bis` | revisor | reparto |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 245 | `4d2077f3735519e20de4eee1cc4fc4200339dce9a26c82978f54df92646fc910` | v | **W2** | W2 |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 12071 | `1303d98c97b78016a96e78bcf60c4ee3d5166f3a3cef38a609ec33ce1aaf9859` | iii | **W1+W2** | W1 `L1-L5200` **y `L7700-L12071`** —§11.6 con los campos 17-18-19 y el paso `6ter`, §11.8, §11.9, la sede `C-L.5`·`1bis`, `PN-19` y **§20 entera, con §20.3, §20.4 y §20.5**— · W2 `L5201-L12071` |
| 3 | `docs/evolucion/30-GATE-ARQUITECTONICO-FINAL-F4C.md` | 3084 | `712058b2467287d7ca51380cf305e84ac311f141d1c12ec0649c8b901aee6503` | iv | **W1+W2+WA** | los tres · DESPUÉS de las demás fuentes: es el gate cuyos dieciséis hallazgos se juzgan |
| 4 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 5691 | `d9cf16af705b8be47997c15020b9a038a23d2d5e8239374fd7d835a1ff7b02f4` | iii | **W2** | W2 |
| 5 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 4345 | `6f416b9f08b955770295a762226733acd3d004edb28cc902013c0ee99e3bdb3f` | v | **W1** | W1 |
| 6 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 857 | `fc8adef3a8baf223fd8bc9ae9403b2e5430c6c5f4cc09e83803d301b920fd0be` | v | **W1** | W1 |
| 7 | `docs/evolucion/verificacion/emitir-sobre-de-ancla.py` | 791 | `f915a840fae8b1553082ccbf381551b8a3abb10dd515a64d314a32772e30d20a` | v | **W1** | W1 · es donde `C-20` se cierra o no se cierra |
| 8 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md` | 256 | `ff4116703b648586bae866cd259f37f7800088e8fe2148b4f4224b466322fc13` | v | **W1** | W1 · el reparto bajo el que corrió el gate anterior |
| 9 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 559 | `ebfef288de70d1ec6d58306720440b9a4c706197cc66f99b92e54a147678fc9a` | v | **W1+W2+WA** | los tres · es la SEDE CANÓNICA y `O21` nace en ella |
| 10 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1449 | `4fd82ebeff2afc3b56715c689eed21dd677660c3a8424b1f14dc4f1466665045` | iii | **W2** | W2 |
| 11 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-FINAL-O21-20260901.md` | 284 | `3dc69768487de794aae577df3468abd97cae30a87b867e3920bb46e02fc5a529` | v | **W1** | W1 · sobre el árbol del GATE es fuente obligatoria nueva, y **es el manifiesto que este `B` sustituye**: quien juzgue el reparto tiene que poder leer los dos |

## 5 · Fuentes AGOTADAS — y la columna distingue LEÍDA de DELEGADA (`C-10`)

```text
LA REGLA QUE SE APLICA, dicha como se ejecuta:
1  LEÍDA        un revisor de un gate anterior declaró LEÍDO ÍNTEGRO DE ESA RUTA, con fila
                propia y citado con documento y línea
2  DELEGADA     el manifiesto de un gate anterior publicó su SHA-256 en fila propia, y ese
                gate la dio por agotada — pero **NADIE declaró haberla leído íntegra allí**
3  en los DOS casos, los BYTES de hoy son IDÉNTICOS a los del árbol que ese gate juzgó, y
   el coordinador lo ha comprobado ruta a ruta contra `7aeed6a` antes de emitir
4  si no se cumple, no se agota, y vuelve a LECTURA ÍNTEGRA

**LA DISTINCIÓN NO ES COSMÉTICA, y es `C-10`:** un rótulo «lectura íntegra certificada en»
sobre una fila que nadie leyó íntegra dice más de lo que la regla entrega. Aquí se dice cuál
es cuál, y el adjudicador puede pesar la diferencia.
```

| # | ruta | líneas | SHA-256 | `1bis` | tipo | procedencia del agotamiento |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md` | 336 | `202ac1af8df5ca6e032cb06f6566c63cf2656fb1a54d65a8c9a0f5d0ef5d41d9` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 2 | `docs/evolucion/12-CRITICA-INDEPENDIENTE-F4.md` | 764 | `c50e0aa6c1b9827c166171efee1737b2e091cc5518d78bad8c469c709c0dd56f` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 3 | `docs/evolucion/13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md` | 797 | `6804d134dfb66b5304ec9c539750559e578a2d5855785b5803189baac2da931f` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 4 | `docs/evolucion/14-DEVOLUCION-TECNICA-PREVIA-F4C.md` | 325 | `7f94e236f3cfb11e78762a301d9a3e94939ab47df34658710d1b8686ed7050fb` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 5 | `docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` | 651 | `b0e015c118ceb916e58fc8191b2a5e40cf28c44dd426618fdd49d10e3ea495d6` | ii+iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 6 | `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | 1257 | `8243034f286160cc89330af95b49f558af0dd16d1b36a37ccbdf02f74a79d185` | i+iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 7 | `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` | 1650 | `18f876d4cd47a2f7cfde15594f98696cfacf750607cd23811dd40ffb36d6c29c` | i+iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 8 | `docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` | 3665 | `1e71366b10d2293802db435de14953771ebd8fc13b426acedd7c0efe21cdb496` | i+iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 9 | `docs/evolucion/19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md` | 1152 | `48baaa1a8e69c6ef3401eb7a0088dcf06849bd66fa3f238bf3e7b8c8fd14392d` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 10 | `docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md` | 801 | `d7d2e4fa3f878e0c010d979e89affdb63462cc6fdd6628ed885d3a760bde09d1` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 11 | `docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md` | 2679 | `9f869ffbdbdb834ca872c03abc8826c125a47b4344ed32cd9b6266db08f8be03` | iv+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 12 | `docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md` | 3478 | `3e2bdece758e6b69d6695bb52f20d21b910a123a27ac643845dbad75e8355f1c` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 13 | `docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md` | 2913 | `0f81f13d8cb319d8ccc5243d19bb26d7f71f57e860cde2eb2edefe33b6993dc2` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 14 | `docs/evolucion/24-TERCER-GATE-DE-CERTIFICACION-F4C.md` | 2515 | `8df584529c857c071954b0d1b426faff82277e29a43556abe5dccfd93714fae1` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 15 | `docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md` | 2754 | `e8431c653cb7919e8d2ec82c5b4d3d11247a01aa61577bb8e5dd266916fb0e5d` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 16 | `docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md` | 4526 | `e2c34215d92937fb467b1ffdb4e6654f66198ead4dac8128c411469bf86c297e` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 17 | `docs/evolucion/27-SEXTO-GATE-DE-CERTIFICACION-F4C.md` | 3946 | `d81b56366e5062ffe0abcd55ba2ef52ddbc3fadf073ea5a280e6cfc15b87ef26` | iv | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 18 | `docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md` | 4275 | `4711738d2a5d64740cc382d7808cf3b185686f80930b3f0d26ff3cf756506854` | iv | **LEÍDA** | LEÍDA ÍNTEGRA · documento **29**, L537 · árbol `7aeed6a` |
| 19 | `docs/evolucion/29-OCTAVO-GATE-DE-CERTIFICACION-F4C.md` | 4197 | `0b9064490c8dd68ec7c50ed87778d31ab8ab5360c966642113367a0eeba2e5ac` | iv | **LEÍDA** | LECTURA ÍNTEGRA declarada por `U1`, `U2` y `HH` en el documento **30** · árbol `7aeed6a` |
| 20 | `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | 2163 | `a88609167dbbea2818b7f2e68cbd4c6fc704cb7e2245ee0a2c873052486fd159` | i | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 21 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 652 | `7876a2bb81b38c764d1bec924e972fb15df30d78058ef299c8adeff087a14255` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 22 | `docs/evolucion/verificacion/README.md` | 386 | `f216def357a4075e3175bd9a7cb2bedf169fc6114b82bacb4d23d91ae5ba4dbe` | v | **LEÍDA** | LEÍDA ÍNTEGRA · documento **29**, L538 · árbol `7aeed6a` |
| 23 | `docs/evolucion/verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` | 119 | `b1c29244dfedc139ff7e80a6167d200803d054f25554c75f31303fea5687a434` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 24 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` | 240 | `c64a0ec4731e6d27751469e84cbcc33104bfe535c42efe4f98533f4d84a0b970` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 25 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` | 316 | `fc4d1c2fdedbcb13be512e88303e21eddbeb194f6cc38b8e50fa0612dad08bbc` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 26 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md` | 210 | `ac9e0edd59cf3e1b783b42ce0fc052e1eb28af7d5d66e218709d76589f724988` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 27 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md` | 221 | `fc4902591eff43bc6736f626fdf2dd1bef7c4f193b1be31f3ddf26f436adb599` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 28 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md` | 193 | `0f08b961c31f03bbedbae700fa67029ac87b6b962067b39b3e504fe28e8d1939` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 29 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md` | 278 | `528dd68fc81134c16f874ab5803996ec50ee838241fd95470a9e07dd66770b2c` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 30 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md` | 292 | `41a4ff29d11c1edf26e6370ea7bcf8cf1ee24d75895336d991b6c12fa4251924` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 31 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md` | 260 | `f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 32 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md` | 248 | `a82e74968e4ca31fbae0825a43f295736af39e58a16b3adf8879d021688e3d76` | v | **LEÍDA** | LECTURA ÍNTEGRA declarada por `U1` en el documento **30** · árbol `7aeed6a` |
| 33 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CIERRE-20260829.md` | 140 | `c843b0c341183859b7f0f07db78cc67eade7ef98c4a96ad3edee23c769d2a976` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 34 | `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | 3343 | `64d170f5acc151445eff6f3f68a0bade91d00744dffa6bdf36c13cd2d366bd3e` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 35 | `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | 597 | `48412108f711204f5389e17fac974133e848737676eb4c57ba5b22c6a37ab8b0` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 36 | `docs/rediseno/CHECKPOINT-OPERATIVO.md` | 195 | `d2131faa4aeddc6d66e98f5eb88d6d9d172a8910b174a1866eecc969633818bb` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 37 | `docs/rediseno/a-CAPACIDADES-APROBADA.md` | 1132 | `10cafb5ceee44f576d327ce614c14c86eb7b22ff43c3dfb82918b785eb36fb04` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 38 | `docs/rediseno/a-ENMIENDA-E1-ENC.md` | 211 | `18dae19523b25ed4a2370ea9c1d23d68beb578f9365bd54587d2f2821093d4da` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 39 | `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | 230 | `9d5a23806fc33fc1d76ba6be9b46ae3499c729c1f11203f80b32550c658ed2eb` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 40 | `docs/rediseno/b-RECORRIDO-APROBADA.md` | 1288 | `f8cb974316e283fa2f16f9ecdd3b94ac19bf4a20cf5816cd155a2449f02719b4` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 41 | `kernel/KERNEL.md` | 1590 | `aa635dff79e73fe13e271cb115653ebc042dc834d32007c634c8ee1df07e3150` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 42 | `kernel/operativo/capacidades/APR/CAPACIDAD.md` | 95 | `a8709115309095849707e2d42290631dca6b3de95d49cc2c3c7ffa4e0546d708` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 43 | `kernel/operativo/capacidades/ARQ/CAPACIDAD.md` | 104 | `6ca11b5f09883e24834f770e61963ae69ca738770ffb1de64f7be0afe4757a47` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 44 | `kernel/operativo/capacidades/CON/CAPACIDAD.md` | 107 | `e0f79e6c3a467302c3d16aa5ee4ccb45583daf146d1676b2b06995419656c5d5` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 45 | `kernel/operativo/capacidades/DIS/CAPACIDAD.md` | 147 | `06f019010d45771fd2a125f9f08f88159b45f15e9f83fd2404c7f2a23f32ad06` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 46 | `kernel/operativo/capacidades/DOM/CAPACIDAD.md` | 135 | `926c7144cb098caaa0b87cdebb5c49b955b74832bc238e66d501ecbb2a635bb3` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 47 | `kernel/operativo/capacidades/DSP/CAPACIDAD.md` | 152 | `acb292f882e77d74693caaab3e392a0d691e988cf875ca4394c59f859ebe7937` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 48 | `kernel/operativo/capacidades/ENC/CAPACIDAD.md` | 174 | `f71b8e43f6e2d66f0801d53ce6e018806d33ef9b5ad5b3300bf1d38fe834d946` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 49 | `kernel/operativo/capacidades/ENT/CAPACIDAD.md` | 123 | `91a81d3cf1cbfa619b7b69553a01810d7074b419fc7e2efb5f8ff2f8f9e7f9ed` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 50 | `kernel/operativo/capacidades/INV/CAPACIDAD.md` | 96 | `47412638e7552da14b7bb89e590aea2f37cc61116c83b902e32952647380ed36` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 51 | `kernel/operativo/capacidades/PLT/CAPACIDAD.md` | 108 | `a5f87977c58ed1d0d4deb3504d664a47fc90382a9790986e5aa277f1dad130d2` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 52 | `kernel/operativo/capacidades/PRD/CAPACIDAD.md` | 105 | `e83b0e08272e219db0c5cc2e17b6d1a95dc4304a9f381d3acfe9c76ff528e3b3` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 53 | `kernel/operativo/capacidades/SEG/CAPACIDAD.md` | 135 | `19bfd38a7a24b57fbec8365327926f7e281092a9e33a06e59355cfda5a5e5a13` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 54 | `kernel/operativo/capacidades/SIS/CAPACIDAD.md` | 119 | `02089f36d124435669b7cf14cf46abd1365a860a4842b739663310b8ceb41628` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 55 | `kernel/operativo/capacidades/USO/CAPACIDAD.md` | 94 | `65f144e4a5c756ef97596a997673d7ad73c194ee6936e616bafd434302ff5d0d` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 56 | `kernel/operativo/capacidades/VER/CAPACIDAD.md` | 135 | `91a16b482629daf3455a3c6963a0568a7a68bcd2bd5553e7540d8c9edbfaf0e2` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 57 | `kernel/operativo/contratos/00-INDICE.md` | 29 | `0b9562119f0b5b5c3f59e66c09446129fbe56865983d6424b76825bf570d004c` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 58 | `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` | 161 | `825f15a914c10d6f07f74e62967f93743efcf629a13379acb3947e70e2952ffa` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 59 | `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` | 539 | `3ee58ca4bc47988d4e6bdd652e2ea5de79ebcf8be79270664c0bd4b4cf391510` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 60 | `kernel/operativo/contratos/C3-METODO-EJECUTABLE.md` | 150 | `d56bf6b81e0fe4a9b3ba811f1adf57748cbae65692db557d15960c8506f84234` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 61 | `kernel/operativo/contratos/C4-MATERIALIZACION.md` | 170 | `670289180e59b176743571a22f22047d20792db266b6426c1c91bd2fd3c1ee81` | ii+v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 62 | `kernel/operativo/contratos/C5-HANDOFF.md` | 115 | `af6f1a4c4f5def8da0dcecee8ea57c17516b41bbbd4abe963460c21024cc7b9e` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 63 | `kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md` | 336 | `14805a79aeb07f314a55913864ee7d359ead05a932d59b207b66b6279d3a41e9` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 64 | `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | 250 | `83f82e2be4756a4651e61f1883d2a99f1d141954097a6e4176a3482a951fc69c` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 65 | `kernel/operativo/diseno/00-SISTEMA-DE-EXCELENCIA.md` | 141 | `08f4bea44594e026aee24cdddc93765cba0fa5c197b26adee0a0cad00d2c366a` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 66 | `kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md` | 352 | `dd323d1aa2f7ede3efa18ac01564b636fff8f0f77beac7db3abed667bbd429ec` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 67 | `kernel/operativo/diseno/02-RUBRICAS.md` | 343 | `8aa8fb18426eac219c275c102f757d50727da2e363d905529c8c061d6721d842` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 68 | `kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md` | 130 | `5d2f54535c1334c053e27bf99b6b81a15a33be7180adf58ddf884cf79ef3a9c1` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 69 | `kernel/operativo/diseno/05-FIDELIDAD.md` | 129 | `fdabb29f7592e603e755c12f191d189755e795ecee104c9b5f583b1ead56e441` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 70 | `kernel/operativo/entrada/00-INDICE.md` | 28 | `315b2790cb66bb4c2c84272468675c8e77fb5a26b8cc2b95ff56db7ee266ddb1` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 71 | `kernel/operativo/entrada/02-CIRCUITO.md` | 145 | `750d39a29f05e7f2b037f9c246c9869ba80edec493e104e206baadda19c09c70` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 72 | `kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` | 187 | `1716bd3d8b48107d28a93e4297a6d93c0e6125107c0cc14811f092641e3d0cd2` | ii | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 73 | `kernel/operativo/esquemas/proceso.yaml` | 49 | `bd391d5acddff1342ce307829dfb8494df535dbd1924d44948d1e17176440dcc` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 74 | `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` | 130 | `f56e8fe4872e46b5ccc8bd2b9531cdc9e53247aaec1e36ebcae131efbe3674ac` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |
| 75 | `kernel/operativo/recorrido/01-PROCESOS.md` | 564 | `98b5cbc836121044a1b3b38690331325cd730ac71d1f30da69482937c392ee85` | v | **DELEGADA** | AGOTADA POR DELEGACIÓN · su SHA-256 lo publicó el manifiesto del documento **30** · árbol `7aeed6a`. **Nadie declaró haberla leído íntegra en aquel gate** |

## 6 · Totales, y las DOS aritméticas — DERIVADAS (`EE-02`)

```text
SOBRE EL ÁRBOL DE LA CANDIDATA
  ASIGNADAS A LECTURA        10   29348 líneas sobre el árbol de la CANDIDATA · 11 sobre
                                  el árbol del GATE, con la fila del manifiesto anterior
  ASIGNADAS COMO AGOTADAS    75   62762 líneas · de ellas 4 LEÍDAS y 71 DELEGADAS
  SUMA                       85   92110 líneas, que es el universo derivado de §2
  OBLIGATORIO menos ASIGNADO  0    CERO FUENTES SIN ASIGNAR
  ASIGNADO menos LEÍDO        —    la calcula el ADJUDICADOR, no el coordinador

SOBRE EL ÁRBOL DEL GATE — las fuentes sin fila, UNA A UNA y con su razón
  ESTE MANIFIESTO `B`           sin fila, y es INEVITABLE: no puede contener su propio
                                SHA-256. Exención de PUNTO FIJO de `DD-19`, y cubre a ESTE
                                fichero y a NINGÚN OTRO. **El manifiesto anterior SÍ tiene
                                fila** —la 11 de §4—, precisamente porque ya no es éste
  LA EVIDENCIA REEJECUTADA      no son fuentes obligatorias: no entran en el universo
  LA FILA DE `00-INDICE.md`     el índice SÍ es fuente obligatoria y SÍ tiene fila; lo que
                                cambia es su SHA-256, y el sobre publica las rutas en que
                                los universos difieren

  CUALQUIER OTRA FUENTE SIN FILA sobre el árbol del gate es un DEFECTO de este manifiesto.
```

## 7 · Lo que este gate tiene que juzgar — Y LO QUE NO

```text
JUZGA, Y ESTO ES LA LISTA ENTERA:
 1 los DIECISÉIS hallazgos `H-01`…`H-16` del documento 30, uno a uno
 2 las OCHO CAUSAS INDEPENDIENTES en que se agrupan, y si se han cerrado por CLASE
 3 `O21` y la INDEPENDENCIA entre certificar cobertura y declarar suficiencia
 4 `C-L.5` medida por sus SEIS condiciones, una a una
 5 `C-L.7` como CLASE COMPLETA, no como tres renglones
 6 `C-20` y **el contenido REAL del sobre**: ¿viaja el texto íntegro de `O19`, o un resumen?
 7 `V6-15`: ¿entrada, escenario negativo y cierre describen el MISMO conjunto derivado?
 8 `V6-16` y `PN-19`: ¿la dependencia está declarada, enlazada y con condición de desbloqueo?
 9 los contratos de §20 y su CLASIFICACIÓN SEMÁNTICA — estructuralmente completo,
   construible, bloqueado por dependencia—, y que ninguno bloqueado se cuente como construible
10 el ORDEN DE CONSTRUCCIÓN hasta PesquerApp, con la arista que la bloquea
11 AUSENCIA DE ARQUITECTURA OCULTA detrás de una obligación de `F6`
12 que NINGUNA DEUDA DE `F6` se presente como implementada, en ninguna sede del corpus
13 que PesquerApp SIGA BLOQUEADA
14 AUSENCIA DE REGRESIONES en `O20` y en la MATRIZ DE LOS 22

NO PUEDE declarar insuficiente a `F4c` ÚNICAMENTE porque el verificador de `F6` todavía no
esté implementado: **esa ausencia es ESPERADA y está DECLARADA**, y `O20` la fija.

SÍ DEBE declarar insuficiente si:
· falta una REGLA necesaria para construir el verificador
· existen DOS soluciones arquitectónicas incompatibles sin decidir
· falta PROPIETARIO, FASE o CRITERIO DE CIERRE en algún contrato
· algún hallazgo se ha ESCONDIDO o SUAVIZADO, o se ha cambiado de fase para ablandarlo
· PesquerApp PODRÍA INICIARSE antes de certificar `F6`
· una obligación sigue dependiendo de INTERPRETACIÓN HUMANA NO NORMADA
```

## 8 · Regla de cierre — y desde `O21` son DOS declaraciones, no una

```text
EL ADJUDICADOR EMITE DOS COSAS SEPARADAS, y `O21` le PROHÍBE condicionar la primera a la
segunda:

  (A) COBERTURA      `C-L.5 CERTIFICADA PARA ESTE GATE`   ó   `C-L.5 ABIERTA`
                     Si es ABIERTA, **nombra la condición incumplida**, y sólo puede serlo
                     por fallar una de las SEIS. Si las seis se cumplen, **DEBE** certificar:
                     no es un acto discrecional, y no puede negarse por haber encontrado
                     otros defectos.

  (B) SUFICIENCIA    `SUFICIENTE PARA F5`   ó   `INSUFICIENTE PARA F5`
                     Sin estados intermedios.

LAS DOS PUEDEN COEXISTIR: la primera habla de COBERTURA, la segunda de SUFICIENCIA
ARQUITECTÓNICA, y `O21` declara que no hay contradicción.

CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA.
CUALQUIER DIFERENCIA ENTRE LOS SOBRES DE DOS REVISORES INVALIDA EL GATE.
LA SEDE CANÓNICA que no coincida con la huella recibida FALLA CERRADO.

EL ADJUDICADOR NO CORRIGE, NO RESUELVE POR MAYORÍA Y NO SUAVIZA.
```

## 9 · La validación de ESTE commit (`DD-17`)

```text
BATERÍA DEL GATE      38/38 en verde · EXIT=0
RUNNER CANÓNICO       13/13 validadores · 13 evidencias publicadas · 0 problemas
WORKSPACE             57/57
NEGATIVAS             67 infracciones detectadas · 0 NO detectadas
DETERMINISMO          `git status --porcelain` VACÍO tras correr el runner
T147 · T158 · T161    SUPERADAS
INTÉRPRETE            Python 3.12.14, y se dice

**Y ESTAS CIFRAS NO PRUEBAN QUE LOS CONTRATOS DE `F6` ESTÉN IMPLEMENTADOS.** `O20` lo
escribe: la batería es EVIDENCIA DE CONSISTENCIA DEL CORPUS, y un verde suyo no demuestra
que el verificador de `F6` esté construido ni certificado. **Ni uno de los puntos de §20
está construido.**
```
