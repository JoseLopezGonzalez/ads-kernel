# `F6` · GATE DEFINITIVO DE CERTIFICACIÓN · 2026-09-05 · **EL GATE NO ES VÁLIDO**

**Qué es este documento.** El REGISTRO íntegro del gate definitivo de `F6`: su objeto
congelado, su manifiesto previo, los TRES manifiestos de lectura, los TRES dictámenes
completos, la cobertura MEDIDA, y la razón por la que **no hay adjudicación**. Es DERIVADO:
no crea autoridad, no aprueba nada y **no certifica nada**.

**Qué NO es.** No es una tanda de corrección. **Durante este gate no se corrigió ni un byte**,
y los hallazgos quedan REGISTRADOS y NO APLICADOS. No es la sede del estado de las fases: ésa
es [`03-GOBIERNO-Y-AUTORIDAD.md`](../../canonico/03-GOBIERNO-Y-AUTORIDAD.md) §6, que este gate
**no mueve** porque su veredicto no la mueve.

---

## 1 · POR QUÉ NO HAY ADJUDICACIÓN, Y QUIÉN RESPONDE DE ELLO

`O27` §5 es norma del Owner y no admite matices: *«Un gate no puede llegar a adjudicación
mientras algún revisor tenga una resta `ASIGNADO − LEÍDO` distinta del conjunto vacío.»* El
manifiesto de este gate lo convirtió en un programa —`comprobar-cobertura-de-gate.py`— y el
programa dice esto:

```text
  REV-1    asignadas  68 · leídas sin hueco  68 · sin abrir 0 · con huecos 0 · sin leer     0
  REV-2    asignadas 104 · leídas sin hueco 103 · sin abrir 0 · con huecos 1 · sin leer     1
  REV-3    asignadas  77 · leídas sin hueco  77 · sin abrir 0 · con huecos 0 · sin leer     0

  OBLIGATORIO − ASIGNADO                 ∅
  ASIGNADO − LEÍDO                       ∅
  LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS       1
      REV-2 · docs/evolucion/11-ARQUITECTURA-INTEGRADA.md · faltan 1 líneas en 12153-12153
  FUENTES MODIFICADAS − LEÍDAS ÍNTEGRAS  ∅

  COBERTURA INCOMPLETA · EXIT=1
```

**Y LA CAUSA ES DEL COORDINADOR, no de ningún revisor.** `11-ARQUITECTURA-INTEGRADA.md` tiene
**12 152 líneas**. El manifiesto que yo emití asigna a `REV-2` el tramo `11907-12153`, es
decir **una línea que no existe**, y además **deja las líneas 1-94 sin asignar a nadie**.
Verificado:

```text
11-ARQ líneas reales                                        12152
el manifiesto declara, en esa misma entrada                 12152
rango asignado a REV-2 para §20                        11907-12153
líneas asignadas que NO EXISTEN                             [12153]
líneas de 11-ARQ sin asignar a nadie                    94  (1-94)
```

**`REV-2` leyó su lote entero**: las 40 622 líneas que existen, con los 113 SHA-256
verificados uno a uno contra el checkout congelado. Su lote no cierra porque **no puede**: no
hay forma de leer una línea inexistente, y el manifiesto **no se modifica una vez commiteado**
—lo escribí yo en su §1—.

> **El gate anterior cayó porque un revisor no leyó. Éste cae porque el coordinador midió mal
> el objeto.** Son fallos distintos y conviene no confundirlos: aquí los tres revisores
> hicieron su trabajo, y el que falló fue quien repartió.

**En consecuencia, y aplicando la regla sin atenuarla: NO SE CREA AL ADJUDICADOR.** No se
compensa, no se sustituye la lectura de nadie, no se redondea la resta a cero y no se emite
ninguna de las declaraciones que sólo un adjudicador puede emitir. Se registra y se para.

## 2 · Objeto congelado

```text
CANDIDATA        2ae0a93888a425cf85ba38d0ac054d069bbbe7d6
REFERENCIA       refs/heads/review/f6-final-candidate-after-c35791b-20260904
                 comprobada contra el REMOTO con `git ls-remote`
RAMA DEL GATE    gate/f6-certificacion-definitiva-20260904, creada DESDE ese SHA
CHECKOUT         extraído con `git archive`, SIN `.git` y SIN el manifiesto dentro (`O27` §4)
INTÉRPRETE       Python 3.12.14 · PyYAML 6.0.2
`fd633383…`      NO es ancestro, NO se leyó y NO se publica
```

**`O27` §4 SÍ se cumplió, y es lo único del aparato del gate que mejoró:** los tres revisores
validaron sobre el checkout congelado, que no contiene este documento ni el manifiesto. La
línea base se reprodujo sobre el objeto correcto por primera vez en tres gates.

## 3 · LA LÍNEA BASE, REPRODUCIDA POR LOS TRES

```text
36/36 validadores en verde · 36 evidencias publicadas · 0 problemas   REV-1 · REV-2 · REV-3
158 infracciones deliberadas detectadas · 0 NO detectadas             los tres
195 escenarios contrastados · 72 no contrastables · 0 divergencias    los tres
huella del kernel 7196ce99457a77d4                                    los tres
determinismo byte a byte entre dos corridas completas                 REV-1 · REV-3
las 36 evidencias byte a byte IDÉNTICAS a las publicadas              REV-2
universo 58 · A=0 · B=0 · C=0                                         REV-3 sí · REV-1 y
                                                                      REV-2 NO lo reprodujeron
```

**La divergencia sobre el universo se explica y no se tapa.** `--obligaciones` sale con
`EXIT=0` y `A=B=C=0` sobre el checkout congelado —lo midieron el coordinador y `REV-3`—;
lo que falla cerrado con `EXIT=2` es `--rutas`/`--tabla`, porque el manifiesto del gate
ANTERIOR vive dentro de la candidata y no aporta filas al cliquet. Es `ADJ-GT1` exactamente,
y es la razón por la que este gate se sacó fuera. `REV-1` lo eleva a bloqueante con un
argumento propio que consta en su dictamen: **el mecanismo que decide qué hay que leer está
roto sobre su propio objeto, y el validador que lo cubre sale VERDE porque su evidencia sólo
ejecuta `--autopruebas`.**

## 4 · LO QUE LOS TRES REVISORES SOSTIENEN DEL PRODUCTO

Se dice antes que lo negativo, porque un registro que sólo publica lo que falla describe mal
el objeto. Todo lo de abajo está MEDIDO por un revisor que no escribió el código:

```text
· la migración `0→1` cortada en sus DIEZ puntos: los diez convergen en el mismo `cid_raiz`,
  `verificar` da ok, y la tercera llamada nunca corrompe. `ADJ-B1` cerrado
· omitir el testigo de `E-08` pone rojas 76 pruebas y los tres E2E
· la inversión 8/9 en sus DOS formas, incluida la sutil que fabrica el testigo; y retirar la
  siembra de `ADJ-M3` devuelve los tres E2E a VERDE sobre un almacén irrecuperable, o sea que
  la siembra es PORTANTE y no decorativa
· `C4` plural en sus dos formas
· `FD-5` completo por la vía productiva: bisnieto con `setsid` muerto bajo contención fuerte,
  superviviente bajo el backend débil que lo declara, y `EXIT=4` con cero ejecución sin
  backend fuerte
· concurrencia con dos escritores reales y corte en las DIEZ ventanas: la revisión es siempre
  1 o 2, nunca intermedia
· `O26` §1: SIETE de las OCHO condiciones se cumplen, medidas de cero por `REV-2`, incluida
  la §1.6 EJERCIDA en contenedor real —uid 65534 frente a 1000, 8/8 escrituras impedidas, con
  control positivo—. La condición 3 resiste el ataque fuerte: atestaciones VÁLIDAS de tuplas
  falsas enrojecen por códigos DISJUNTOS
· los ocho sabotajes de `b.12` ponen roja UNA prueba distinta cada uno, más la meta-prueba
```

## 5 · LOS BLOQUEANTES QUE LOS TRES ENCONTRARON

Ninguno se corrige aquí. Ninguno cambia de clase.

```text
REV-1 · el derivador del universo FALLA CERRADO sobre la propia candidata, y su validador
        sale VERDE porque su evidencia sólo ejecuta `--autopruebas`
REV-1 · `b.12` dice «DSP informa de la inanición. NO CAMBIA LA PRIORIDAD. NUNCA» —citado
        literal en tres sedes— y subir la prioridad en la misma transición durable pasa DOCE
        baterías en verde, con la línea ejecutándose 16 veces y mutando el estado 50→60→70.
        LA ÚNICA AFIRMACIÓN ABSOLUTA DEL CONTRATO ES LA ÚNICA SIN RED
REV-2 · el prólogo `E-10` es EVADIBLE con `sitecustomize`: `site.py` lo importa antes de que
        la primera sentencia del prólogo purgue `sys.path`. Con gancho instalado, un
        `verificador.py` con código inyectado publica `{"ok": true}` con código 0 y la huella
        anclada pasa a un valor fabricado
REV-2 · `OBLIGATORIO` no se deriva del árbol: el comentario declara «derivarlo con git diff»
        y el código lee `manifiesto["modificadas"]`. El fichero ni siquiera importa `subprocess`
REV-2 · la firma de éxito de 14 componentes lleva `\d+`, que casa con `0`: una evidencia que
        declare «0 infracciones detectadas · 0 NO detectadas» pasa la comprobación
LOS TRES · `comprobar-cobertura-de-gate.py` indexa el lote por RUTA, de modo que de los
        rangos de `11-ARQ` sobrevive sólo el último. Medido: REV-1 34 922 de 40 630 líneas,
        REV-3 46 649 de 47 534. Un revisor que leyera sólo el último tramo cerraría con la
        resta vacía
```

> **Los dos últimos son del coordinador, y los tres revisores los encontraron por separado y
> sin verse.** El instrumento que escribí para impedir que un gate cayera por cobertura tiene
> un defecto que permite exactamente eso, y el manifiesto que escribí para repartir la lectura
> asigna una línea que no existe. **El aparato del gate falló por donde el gate anterior ya
> había fallado, y de una manera nueva.**

## 6 · Digests de lo que se registra íntegro

```text
MANIFIESTO DE ASIGNACIÓN   docs/f6/gate-definitivo/MANIFIESTO-ASIGNACION.md · .json
MANIFIESTOS DE LECTURA     LECTURA-REV-1.json · LECTURA-REV-2.json · LECTURA-REV-3.json
COBERTURA MEDIDA           COBERTURA-MEDIDA.txt
DICTAMEN REV-1              960 líneas · sha256 d9ac50c8370d2308a2137f9bfa4fe088ba3bbee8f8094e472a3172333421b595
DICTAMEN REV-2              797 líneas · sha256 89a3a554a21259563917f7434309b59671daf0c40f7cd0f9e9cfe48893b6e5e1
DICTAMEN REV-3              936 líneas · sha256 2659fccae1c3a0c53b36549d32fae4b4370773b1a4a982c1ae05ebabf4d24152
ADJUDICACIÓN               NO EXISTE, y §1 dice por qué
```

Los tres dictámenes se transcriben ÍNTEGROS y sin editar una coma. Lo que sigue no es un
resumen.

---

# 7 · DICTAMEN ÍNTEGRO DEL REVISOR 1

## DICTAMEN · REVISOR 1 (`REV-1`) · gate independiente de certificación de `F6`

**Eje asignado:** estado durable, migración, runtime, dispatcher, `b.12`, `C2`/`C4`/`C5`,
concurrencia, recuperación, `Continúa`, macrocircuitos y contención.

**No he hablado con `REV-2` ni con `REV-3`, no he leído sus dictámenes ni sus manifiestos de
lectura, y no he escrito ni un byte fuera de mi propio espacio de trabajo.**

---

## 1 · Precondiciones y cobertura

### 1.1 · El objeto congelado, y qué se midió sobre él

```text
CHECKOUT CONGELADO   …/scratchpad/CANDIDATA
CANDIDATA            2ae0a93888a425cf85ba38d0ac054d069bbbe7d6
REFERENCIA           refs/heads/review/f6-final-candidate-after-c35791b-20260904
INTÉRPRETE           /home/jose/.local/bin/python3.12 · Python 3.12.14 · PyYAML 6.0.2
MANIFIESTO           docs/f6/gate-definitivo/MANIFIESTO-ASIGNACION.{md,json}
                     leído de la rama `gate/f6-certificacion-definitiva-20260904`
```

**Toda la validación de producto se ha hecho sobre COPIAS del checkout congelado**, nunca
sobre el checkout ni sobre `/home/jose/ads-kernel`. Cada sabotaje se aplicó sobre una copia
recién hecha y la copia se destruyó al terminar.

### 1.2 · El repositorio del Owner, al abrir y al cerrar

```text
AL ABRIR    git status --porcelain   → VACÍO
            git rev-parse HEAD       → 54898fc9154b7f15bd93ba09003fe1b4e0941001
            rama                     → gate/f6-certificacion-definitiva-20260904

AL CERRAR   git status --porcelain   → VACÍO
            git rev-parse HEAD       → 54898fc9154b7f15bd93ba09003fe1b4e0941001
            rama                     → gate/f6-certificacion-definitiva-20260904
```

**Idénticos.** No he ejecutado ningún comando `git` que cambie estado en ese repositorio.

Y el checkout congelado sigue intacto: tras las siete tandas de ataque,

```text
$ diff -rq --exclude=__pycache__ CANDIDATA R1/SANO
(sin salida)
SANO == CANDIDATA (byte a byte)
```

### 1.3 · La comprobación de cobertura, con la resta a cero

```text
$ python3.12 docs/evolucion/verificacion/comprobar-cobertura-de-gate.py \
      --manifiesto MANIFIESTO.json --lectura lectura-REV-1.json --raiz CANDIDATA

COBERTURA DEL GATE · candidata 2ae0a93888a425cf85ba38d0ac054d069bbbe7d6
==============================================================================
  REV-1    asignadas  68 · leídas sin hueco  68 · sin abrir   0 · con huecos   0
           líneas asignadas  34922 · sin leer      0 · cerrado declarado: sí

LAS CUATRO RESTAS
------------------------------------------------------------------------------
  OBLIGATORIO − ASIGNADO                 ∅
  ASIGNADO − LEÍDO                       ∅
  LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS       ∅
  FUENTES MODIFICADAS − LEÍDAS ÍNTEGRAS  172
      … (172 rutas, TODAS de los lotes de REV-2 y REV-3)
  SIN MANIFIESTO DE LECTURA: REV-2, REV-3
```

**MI PARTE ESTÁ A CERO**, y las dos restas que me obligan a mí —`ASIGNADO − LEÍDO` y
`LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS`— son **∅**. Las otras dos filas no son mías: la tercera
resta enumera fuentes de los lotes de los otros dos revisores, y `EXIT=1` sale por eso y por
que sus manifiestos de lectura no estaban presentes cuando yo corrí el instrumento.

**Mi lote, medido:** 67 ficheros enteros + 8 tramos de
`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` = **68 rutas distintas · 40 630 líneas
asignadas**, todas leídas ÍNTEGRAS y una a una, y declaradas en
`lectura-REV-1.json` con el `sha256` del checkout congelado y con tramos que cubren cada
fichero o cada rango entero.

> **El instrumento sólo mide 34 922 de esas 40 630, y esto es un hallazgo, no una excusa.**
> `comprobar-cobertura-de-gate.py:205` construye el lote como
> `{f["ruta"]: f for f in lote.get("fuentes")}` —un diccionario indexado por RUTA—, de modo
> que los **ocho tramos** de `11-ARQUITECTURA-INTEGRADA.md` colapsan en UNA sola entrada y
> sobrevive **sólo el último**, `§17 · [10853, 10881]`, de 29 líneas. 40 630 − 34 922 =
> **5 708 = 5 737 − 29**: exactamente los siete tramos que el instrumento descarta. Ver
> `R1-H04`.

---

## 2 · La línea base, reproducida — mis cifras al lado de las afirmadas

Dos corridas completas e independientes del arnés sobre dos copias distintas del checkout
congelado (`work/BASE1`, `work/BASE2`).

| lo afirmado | lo medido por mí | ¿reproduce? |
|---|---|---|
| 36/36 validadores en verde · 36 evidencias · 0 problemas | `36/36 validadores en verde · 36 evidencias publicadas · 0 problemas`, en las DOS corridas | **SÍ** |
| 158 infracciones detectadas · 0 NO detectadas | `158 infracciones detectadas · 0 NO detectadas` | **SÍ** |
| 195 escenarios contrastados · 72 no contrastables · 0 divergencias | `contrastados 195 · no contrastables 72 · divergencias 0 · no contrastables por estado declarado: contrato-definido=56 prueba-ejecutada=12 validador-implementado=4` | **SÍ** |
| universo obligatorio 58 · A=0 · B=0 · C=0 · 12 sabotajes al derivador sin fallo | **NO REPRODUCE.** El derivador **FALLA CERRADO con `EXIT=2`** sobre la propia candidata. Sólo reproduce la mitad de `--autopruebas`: `12 sabotajes · 0 sin detectar` | **NO** — ver `R1-H01` |
| comprobador de cobertura 11 controles · 0 sin detectar | `11 controles · 0 sin detectar` | **SÍ** |
| huella `7196ce99457a77d4` | `kernel/.upstream-hash` → `7196ce99457a77d4`, y el arnés de negativos la usa como huella almacenada | **SÍ** |
| determinismo byte a byte entre dos corridas | `diff -q base1.log base2.log` → idénticos · `diff -rq --exclude=__pycache__ BASE1 BASE2` → **sin salida** | **SÍ** |

**Seis de siete reproducen exactamente. La séptima no, y la divergencia es material:**

```text
$ python3.12 docs/evolucion/verificacion/derivar-universo-obligatorio.py
FALLA CERRADO · 1 manifiesto(s) INMUTABLE(s) de docs/evolucion/verificacion/manifiestos no
aportan NI UNA fila al cliquet: ['F6-ASIGNACION-GATE-CERTIFICACION-FINAL-20260904.md']. Un
manifiesto es la sede que declaró qué fuentes eran obligatorias en su gate; si el lector no
las ve, esas rutas pueden desaparecer del universo sin que nada lo diga …
EXIT=2

$ python3.12 docs/evolucion/verificacion/derivar-universo-obligatorio.py --autopruebas
  12 sabotajes · 0 sin detectar
EXIT=0
```

Y la evidencia publicada del validador `universo-obligatorio` sólo contiene la SEGUNDA orden:

```text
## evidencia de: universo-obligatorio
## orden:        python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py --autopruebas
## codigo:       0
```

Es decir: **el instrumento está muerto para su propósito productivo y el validador sale
VERDE igualmente.** Detalle y causa exacta en `R1-H01`.

---

## 3 · Los siete ataques, uno a uno

Criterio aplicado en los siete: **sano → VERDE · sabotaje → ROJO POR EL MOTIVO ESPERADO ·
restaurado → VERDE.** Un sabotaje que sólo pusiera roja la huella no cuenta y no lo he
contado.

### 3.1 · Ataque 1 · migración REAL `0 → 1`, cortada en cada punto de fallo

**Heredado GENUINO construido desde la especificación** —`estado/canonico/items/*.json` y
NADA más: sin `FORMATO.json`, sin diario y sin `REVISION.json`—:

```text
$ find . -type f | sort
./estado/canonico/items/it-dos.json
./estado/canonico/items/it-uno.json
```

**SANO · migración limpia:**

```text
$ ads_estado.py --repo limpio migrar
desde         0
hasta         1
aplicadas     1
transacciones tx-0001-ae70f1b7
EXIT=0
$ ads_estado.py --repo limpio revision
revision           1
cid_raiz           sha256:d06ca19af88c533661789c34c6672fa1849d47da72c244e95132bb85c4489622
ventana            cerrada
```

**CORTE EN LOS DIEZ PUNTOS DE `estado/fallos.py`**, con `ADS_ESTADO_FALLO`, y tres llamadas
seguidas a `migrar` después de cada corte:

```text
punto de corte                   corte   2ª llamada   3ª llamada   revisión   verificar
antes-de-escribir-temporal        70          1            0           1          ok
despues-de-escribir-temporal      70          1            0           1          ok
despues-de-sincronizar-temporal   70          1            0           1          ok
antes-del-commit-atomico          70          0            0           1          ok
despues-del-commit-atomico        70          0            0           1          ok
antes-de-sincronizar-directorio   70          0            0           1          ok
entre-el-paso-8-y-el-9            70          0            0           1          ok
durante-el-diario                 70          0            0           1          ok
durante-el-registro-auxiliar       0          0            0           1          ok
antes-de-devolver-exito           70          0            0           1          ok

cid_raiz distintos entre los DIEZ almacenes cortados y el no cortado: UNO SOLO
  sha256:d06ca19af88c533661789c34c6672fa1849d47da72c244e95132bb85c4489622
```

**Los diez convergen al MISMO `cid_raiz` que la migración sin interrupción, `verificar`
devuelve `ok si` en los diez, y la tercera llamada nunca corrompe.**

Los tres puntos ANTERIORES al punto de no retorno no retoman a la primera: devuelven

```text
[RECUPERACION_MARCADA] la transacción tx-0001-ae70f1b7 diverge y se ha MARCADO; la copia
íntegra está en estado/reconciliacion/conflictos/tx-0001-ae70f1b7 y la salida la decide la
autoridad
EXIT=1
```

y la llamada siguiente retoma con identificador propio (`tx-0001-04f8c477`).
**Esto NO es un hallazgo: el árbol lo declara literalmente**, en `migracion.py`,
`DECISIÓN · un corte ANTERIOR al punto de no retorno se cierra por MARCAR, y se dice`,
nombrando los tres puntos exactos y la causa (la revisión 0 de un heredado tiene la raíz
vacía mientras `canonico/` ya tiene contenido). **Medido y coincide con lo declarado, punto
por punto.** El único punto que no llega a cortar —`durante-el-registro-auxiliar`— es
coherente: una migración no abre registro auxiliar.

**VEREDICTO DEL ATAQUE 1: el árbol lo sostiene, y su declaración es exacta.**

### 3.2 · Ataque 2 · omisión del testigo `E-08`

**Sabotaje** (`estado/motor.py:743`, se retira la última acción del paso 8):

```python
        self._sincronizar_dominios(plan)
        pass  # SABOTAJE A2: se omite la escritura del testigo E-08
        fallos.punto("entre-el-paso-8-y-el-9")
```

```text
test_estado_durable            EXIT=1   FAILED (failures=51, errors=25)
escenario_extremo_a_extremo    EXIT=1
escenario_e2e_runtime          EXIT=1
escenario_e2e_f6               EXIT=1
```

**Motivo literal, y es el esperado:**

```text
estado.errores.EstadoCorrupto: [ESTADO_CORRUPTO] el paso 9 no encuentra el testigo durable
que el paso 8 tiene que haber escrito: o los pasos se han invertido, o el paso 8 no llegó a
publicar. Publicar la revisión ahora dejaría `REVISION.json` nombrando objetos que no están
en `canonico/`, que es un almacén IRRECUPERABLE
(estado/operacional/tx/tx-0001-b5ba850a/PUBLICADOS.json)
```

**Restaurado → VERDE** (la copia sana da `EXIT=0` en las cuatro).

### 3.3 · Ataque 3 · inversión de los pasos 8 y 9, en sus formas

#### Forma A · inversión literal (la revisión se publica antes del testigo)

`testigo = None` al publicar la revisión, y el testigo escrito después:

```text
test_estado_durable            EXIT=1   FAILED (failures=51, errors=25)
escenario_extremo_a_extremo    EXIT=1
escenario_e2e_runtime          EXIT=1
escenario_e2e_f6               EXIT=1

T362 · corte 8-9: el paso 8 no dejó su testigo durable, luego el corte no cayó entre los
       pasos 8 y 9 ... FAIL
T297b · un testigo con los cid VIEJOS no deja publicar ... FAIL
```

La forma A es **detectada dos veces**: por la guarda `testigo is None` de
`_publicar_revision` —que existe exactamente para esto— y por la siembra del E2E.

#### Forma B · inversión SUTIL, respetando el significado de cada punto de fallo

Ésta es la que importa: el paso 9 va PRIMERO, el 8 DESPUÉS, el punto de fallo
`entre-el-paso-8-y-el-9` conserva su sitio ENTRE los dos pasos invertidos, y el testigo se
**fabrica en memoria** para franquear las dos guardas. Una migración normal completa sin
error; lo que queda roto es el corte.

```text
test_estado_durable            EXIT=1   FAILED (failures=3, errors=1)
escenario_extremo_a_extremo    EXIT=1
escenario_e2e_runtime          EXIT=1
escenario_e2e_f6               EXIT=1

pruebas rojas, y son exactamente las que tienen que serlo:
  FAIL  test_T300_caida_ENTRE_los_pasos_8_y_9_y_RECUPERACION_posterior
  FAIL  test_T323_la_migracion_no_publica_sin_el_testigo_del_paso_8  (ausente y corrupto)
  ERROR test_T314b_la_rama_COMPLETAR_funciona_sobre_un_diario_sellado

y en los tres E2E:
  T362 · corte 8-9: la revisión vigente es 1 y tenía que seguir siendo 0. El paso 9 llegó a
         publicar, y entonces el almacén no queda a medias ... FAIL
  T301 · recuperabilidad  almacen-cortado-8-9: NO SE PUDO ABRIR NI RECUPERAR
         (RecuperacionMarcada)
```

**`T297` y `T297b` —las dos pruebas dedicadas a la inversión— PASAN bajo la forma B.** No es
un defecto: comprueban las guardas, y la forma B las franquea deliberadamente fabricando el
testigo. Lo que caza la forma B es `T300` más la siembra de los E2E. **Queda dicho porque
importa: la propiedad no la sostiene la guarda, la sostiene el corte sembrado.**

#### La mitad que el encargo pedía comprobar aparte

**(i) ¿pueden los tres E2E quedar verdes sobre un almacén irrecuperable?**
**NO.** Con la forma B, los tres salen `EXIT=1` y nombran el almacén cortado.

**(ii) ¿retirar la siembra los devuelve a verde?**
**SÍ, y esto es la prueba de que la siembra es portante y no decorativa.** Sobre el MISMO
árbol saboteado con la forma B, neutralizando la llamada a `sembrar_almacen_cortado` en los
tres ficheros:

```text
escenario_extremo_a_extremo      EXIT=0  T301 · recuperabilidad  control: abierto, recuperado e íntegro
escenario_e2e_runtime            EXIT=0  T301 · recuperabilidad  ws/ads: abierto, recuperado e íntegro
escenario_e2e_f6                 EXIT=0  T301 · recuperabilidad  maquina-b/control: abierto, recuperado e íntegro
```

Con la inversión sutil viva y sin siembra, **los tres escenarios extremo a extremo dan
VERDE**. La afirmación del contrato —«ya no pueden seguir verdes sobre un almacén
irrecuperable»— es cierta **por la siembra y sólo por ella**, exactamente como su propio
bloque `ADJ-M3` declara. Medido, no supuesto.

**VEREDICTO DEL ATAQUE 3: el árbol lo sostiene, en las dos formas, y la pieza que lo
sostiene es la que él mismo señala.**

### 3.4 · Ataque 4 · `C4` plural

#### Forma A · el cardinal plural se aplana a 1

```python
    minimo = 1  # SABOTAJE A4a: el cardinal plural se aplana a 1
    maximo = 1  # SABOTAJE A4a
```

```text
test_cardinalidad_y_seleccion   EXIT=1   FAILED (failures=3, errors=6)
  ERROR test_251_el_registro_durable_no_puede_publicar_dos_o_tres_y_un_agente
        (dentro de equipos.derivar_reparto)
test_ciclo                      EXIT=0
escenario_e2e_f6                EXIT=0
```

#### Forma B · el vocabulario cerrado se abre («1 por omisión»)

```python
    if not casa:
        return lectura  # SABOTAJE A4b: vocabulario ABIERTO, «1 por omisión»
```

```text
test_cardinalidad_y_seleccion   EXIT=1   FAILED (failures=1)
  FAIL test_259_un_cardinal_ilegible_falla_cerrado_y_nunca_vale_uno_por_omision
       T259 · Defecto que previene: «lo que no entiendo, que sea uno».
```

**Las dos formas se cazan, y por el motivo exacto.** Queda registrado que **quien las caza
es UNA sola batería**: `test_ciclo` y `escenario_e2e_f6` siguen verdes con `C4` aplanado
(`R1-H05`).

### 3.5 · Ataque 5 · inanición de `b.12`

#### Los CUATRO criterios de orden, saboteados por separado

Se retira uno por sabotaje de `politica.clave_de_orden`:

```text
SABOTAJE C1 · se retira `prioridad`
   test_cardinalidad_y_seleccion  EXIT=1
   rojas: test_260_criterio_a_la_prioridad_declarada_manda_sobre_todo_lo_demas,
          test_269_cada_sabotaje_pone_roja_una_prueba_DISTINTA
SABOTAJE C2 · se retira `grado_de_salida`
   rojas: test_261_criterio_b_desbloquear_a_mas_paquetes_decide_entre_iguales, test_269
SABOTAJE C3 · se retira `tiempo_listo`
   rojas: test_262_criterio_c_la_antiguedad_saca_de_la_cola_al_que_lleva_mas_esperando, test_269
SABOTAJE C4 · se retira el desempate por identificador
   rojas: test_263_criterio_d_el_identificador_hace_TOTAL_el_orden, test_269
```

**Cada uno pone roja una prueba DISTINTA**, y además dispara la meta-prueba `T269`, que es
la que afirma justamente eso.

#### Los CUATRO campos de inanición, saboteados por separado

Cada campo deja de registrarse en `dispatcher.py`, sin tocar el esquema:

```text
SABOTAJE campo `listo_en`         rojas: T267 (reloj LÓGICO, no de pared), T260, T261, T262, T269
SABOTAJE campo `postergaciones`   rojas: T264 (se CUENTAN pasada a pasada y son durables),
                                          T268 (sobreviven a la caída y a dos planificadores), T269
SABOTAJE campo `adelantado_por`   rojas: T265 (dice QUIÉN le pasó por delante), T268, T269
SABOTAJE campo `impedimento`      rojas: T266 (nombra el criterio que de verdad decidió), T269
```

**Cada campo pone roja una prueba DISTINTA y propia.** Ocho sabotajes, ocho pruebas
distintas. Esta parte del árbol es sólida y su meta-prueba `T269` no es decorativa.

#### `DSP` no sube la prioridad — ESTO NO SE SOSTIENE

`b.12` es terminante, y el árbol lo cita literalmente en TRES sedes
(`runtime/politica.py`, `ciclo/planificacion.py:32`, `runtime/vistas.py:29`):
**«DSP informa de la inanición. NO cambia la prioridad. Nunca».**

Sabotaje: al postergar, `DSP` SUBE la prioridad del postergado, en la MISMA transición
durable que ya escribe `postergaciones`:

```python
                nuevo = dict(actual)
                # SABOTAJE A5c: DSP SUBE la prioridad del postergado.
                nuevo["prioridad"] = int(actual["prioridad"]) + 10
                nuevo["seleccion"] = normalizar_seleccion(seleccion, ruta=actual["id"])
```

```text
test_cardinalidad_y_seleccion   EXIT=0   Ran 20 tests   OK
test_runtime                    EXIT=0
test_ciclo                      EXIT=0
test_continua                   EXIT=0
test_agentes                    EXIT=0
test_arboles                    EXIT=0
test_sesion_nueva               EXIT=0
test_estado_durable             EXIT=0
test_integridad_y_evidencia     EXIT=0
escenario_extremo_a_extremo     EXIT=0
escenario_e2e_runtime           EXIT=0
escenario_e2e_f6                EXIT=0
```

**DOCE baterías, TODAS VERDES.** Y no es código muerto: con una sonda en la línea
saboteada,

```text
test_cardinalidad_y_seleccion  EXIT=0 · sondas=16
  SONDA-A5c ALCANZADA: pq-espera-1 50 -> 60
  SONDA-A5c ALCANZADA: pq-espera-2 50 -> 60
  SONDA-A5c ALCANZADA: pq-espera-1 60 -> 70
  SONDA-A5c ALCANZADA: pq-espera-2 60 -> 70
```

La línea se ejecuta **dieciséis veces**, muta la prioridad DURABLE 50→60→70 y cambia el
orden de selección futuro, **y ninguna batería lo nota**. Ver `R1-H02`.

### 3.6 · Ataque 6 · contención y `setsid`, por la vía productiva

Todo por `ads_runtime.py despachar`, con una tarea generacional real —hijo, nieto y
bisnieto, los tres con `setsid`, cada uno con su marca en la línea de órdenes.

#### Anfitrión real

```text
cgroup-v2                  arbol-de-procesos  False  el subgrupo se crea pero la tarea NO acaba dentro
espacio-de-nombres-de-pid  arbol-de-procesos  True
systemd-scope              arbol-de-procesos  True
contenedor                 arbol-de-procesos  True
simple                     grupo-de-procesos  True   AISLAMIENTO INFERIOR y declarado
```

#### (a) contención FUERTE · el bisnieto con `setsid` NO escapa

```text
$ ads_runtime.py … --contencion arbol-de-procesos despachar pq-a6
[TIEMPO_AGOTADO] el adaptador excedió su `limite_segundos`: el límite venció y la CONTENCIÓN
`espacio-de-nombres-de-pid` terminó el ESPACIO DE NOMBRES de PID entero: al morir su PID 1
el núcleo mata a todos los demás, `setsid` incluido

descendencia REV1A6 viva después:  (ninguna)
```

#### (b) backend DÉBIL pedido expresamente · el bisnieto SÍ escapa, y se dice

```text
$ ads_runtime.py … --contencion grupo-de-procesos --contencion-backend simple despachar pq-a6
[TIEMPO_AGOTADO] … la CONTENCIÓN `simple` terminó el GRUPO de procesos. Un descendiente que
ejecutó `setsid` NO está en el grupo y sobrevive

descendencia REV1A6 viva después:
  899053 REV1A6-BISNIETO
  899155 REV1A6-…
```

El límite está **medido y declarado en el propio mensaje**, no escondido.

#### (c) backend débil con política FUERTE · NO se degrada en silencio

```text
$ ads_runtime.py … --contencion arbol-de-procesos --contencion-backend simple despachar pq-a6
[CONTENCION_FUERTE_NO_DISPONIBLE] se pidió el backend `simple`, cuyo nivel es
`grupo-de-procesos`, y la política exige `arbol-de-procesos`. No se degrada en silencio
clase_de_fallo: error-de-contencion
```

#### (d) anfitrión SIN NINGÚN backend fuerte · FALLO CERRADO y CERO ejecución

Se simula el anfitrión —se marcan indisponibles los cuatro backends de nivel
`arbol-de-procesos` en `deteccion.capacidades()`—, **sin tocar la política**:

```text
hay_contencion_fuerte: False · mejor_disponible: simple

$ ads_runtime.py … --contencion arbol-de-procesos despachar pq-a6
[CONTENCION_FUERTE_NO_DISPONIBLE] la política exige contención FUERTE (`arbol-de-procesos`)
y este anfitrión no ofrece ningún backend que la dé. NO se degrada a `killpg`: sin
contención fuerte no se ejecuta
EXIT=4

descendencia REV1A6:      (ninguna)
estado del paquete:       listo · intentos 0 de 3 · efecto None · acuse no · lease (ninguno)
recibos del adaptador:    ws4/efectos → VACÍO
```

**Cero ejecución, cero intentos, cero lease, cero recibos.** No hay caída al backend débil.

#### (e) contención NO cableada · el sabotaje se caza

Se retira el cableado de la CLI —el estado exacto que el propio `ads_runtime.py` describe
como «hecho reproducido antes de corregir: la cadena `contencion` no aparecía en NINGUNO de
los cinco `ads_*.py`»—:

```python
def _politica_de_contencion(argumentos):
    return None   # SABOTAJE A6b
```

```text
test_contencion               EXIT=0    ← no lo caza
test_adaptadores              EXIT=0    ← no lo caza
test_runtime                  EXIT=0    ← no lo caza
test_ciclo                    EXIT=0    ← no lo caza
test_arboles                  EXIT=0    ← no lo caza
test_sesion_nueva             EXIT=0    ← no lo caza
escenario_e2e_runtime         EXIT=0    ← no lo caza
escenario_e2e_f6              EXIT=0    ← no lo caza
test_integridad_y_evidencia   EXIT=1    ← LO CAZA
  FAIL test_T309_el_punto_ejecutable_ACTIVA_la_politica_y_contiene_al_bisnieto
       AssertionError: [908483, 908485, 908487] != [] : sobrevivió descendencia al camino
       PRODUCTIVO con política de contención
  FAIL test_T309b_sin_backend_fuerte_el_punto_ejecutable_FALLA_CERRADO
  FAIL test_T308d_el_error_de_CONTENCION_tiene_su_propio_codigo
```

**Se caza, y nombrando los PID supervivientes.** La caza vive en UNA sola batería
(`test_integridad_y_evidencia`), lo cual es correcto pero conviene saberlo: `test_contencion`
prueba el paquete, no su cableado.

**VEREDICTO DEL ATAQUE 6: `FD-5` se sostiene entero, con su límite declarado y su fallo
cerrado medido.**

### 3.7 · Ataque 7 · `Continúa`, recuperación y concurrencia

#### (a) DOS escritores REALES simultáneos sobre el mismo almacén

Dos procesos `ads_estado.py transicion` lanzados a la vez, tres rondas:

```text
ronda 0 · códigos=[0, 0] · revisión=2 · verificar=0 (ok si)
ronda 1 · códigos=[0, 0] · revisión=2 · verificar=0 (ok si)
ronda 2 · códigos=[0, 0] · revisión=2 · verificar=0 (ok si)
```

Se serializan por el `flock` exclusivo y los dos aplican. Ninguna corrupción.

#### (b) corte en cada ventana del protocolo CON el otro escritor vivo

```text
                                  corte  otro  recuperar  revisión  verificar
antes-de-escribir-temporal          70     0      0/0         1         0   OK
despues-de-escribir-temporal        70     0      0/0         1         0   OK
despues-de-sincronizar-temporal     70     0      0/0         1         0   OK
antes-del-commit-atomico            70     0      0/0         2         0   OK
despues-del-commit-atomico          70     0      0/0         2         0   OK
antes-de-sincronizar-directorio     70     0      0/0         2         0   OK
entre-el-paso-8-y-el-9              70     0      0/0         2         0   OK
durante-el-diario                   70     0      0/0         1         0   OK
durante-el-registro-auxiliar         0     0      0/0         2         0   OK
antes-de-devolver-exito             70     0      0/0         2         0   OK
```

**La revisión final es SIEMPRE 1 o 2, NUNCA una intermedia ni un estado sin explicar**, y
`verificar` devuelve `ok` en las diez. La recuperación es idempotente: la segunda llamada
también devuelve 0 y no cambia nada.

#### (c) sabotaje de la exclusión mutua

`fcntl.LOCK_EX` → `fcntl.LOCK_SH`: el bloqueo deja de ser exclusivo.

```text
test_estado_durable   EXIT=1
  FAIL  test_60_cuatro_escritores_desde_la_misma_base_no_dan_doble_exito
  FAIL  test_61_los_perdedores_pueden_reintentar_sobre_la_base_nueva
  FAIL  test_62_ocho_escritores_no_rompen_la_integridad
  ERROR test_65_dos_caidas_simultaneas_no_publican_dos_veces
```

**ROJO por el motivo exacto.** Restaurado → VERDE.

#### (d) `Continúa` · determinismo y modo PLAN

```text
$ ads_ciclo.py --repo D --instancia inst-A --json continuar
$ ads_ciclo.py --repo D --instancia inst-B --json continuar
huella A: sha256:d024f26ae81d8ce150e0906c99c14518eae9a40e13694928df4b53cb7ced82ea
huella B: sha256:d024f26ae81d8ce150e0906c99c14518eae9a40e13694928df4b53cb7ced82ea
¿mismos bytes?: SI
revisión antes/después: 2 / 2
```

**Determinista y sin tocar el estado — sobre un almacén con la ventana cerrada.**

**Sobre un almacén con la VENTANA ABIERTA, no:**

```text
--- ANTES de Continúa ---   revision 0 · ventana preparada
$ ads_ciclo.py --repo D --instancia inst-D continuar        (modo PLAN, SIN --ejecutar)
EXIT=0
--- DESPUÉS de Continúa --- revision 1 · ventana cerrada
```

El modo PLAN **cerró la ventana y avanzó la revisión durable de 0 a 1**. Es lo que `b.14`
paso 2 manda hacer, y por tanto **no es un defecto de comportamiento**; lo que es falso es
la frase que lo describe. Ver `R1-H03`.

---

## 4 · HALLAZGOS

Formato: `identificador · severidad · sede · reproducción · remedio · propietario · fase ·
clase`.

---

### `R1-H01` · el derivador del universo obligatorio está MUERTO sobre su propia candidata, y el validador sale VERDE

```text
SEVERIDAD     BLOQUEANTE
SEDE          docs/evolucion/verificacion/derivar-universo-obligatorio.py — el filtro
              `_FILA_MANIFIESTO`, que exige fila de TABLA Markdown (`| `ruta` |`), y la
              guarda `if sin_filas: raise SedeIlegible(...)`
              docs/evolucion/verificacion/manifiestos/F6-ASIGNACION-GATE-CERTIFICACION-FINAL-20260904.md
              kernel/operativo/pruebas/evidencia/universo-obligatorio-salida.txt

REPRODUCCIÓN  $ python3.12 docs/evolucion/verificacion/derivar-universo-obligatorio.py
              FALLA CERRADO · 1 manifiesto(s) INMUTABLE(s) … no aportan NI UNA fila al
              cliquet: ['F6-ASIGNACION-GATE-CERTIFICACION-FINAL-20260904.md']
              EXIT=2

              $ cd docs/evolucion/verificacion/manifiestos
              $ for f in *.md; do printf "%-58s %s\n" "$f" \
                    "$(grep -cE '^\|\s*(`|[0-9])' "$f")"; done
              F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md               21
              F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md        83
              …  (los quince de `F4c`, entre 21 y 88 filas cada uno)
              F6-ASIGNACION-GATE-CERTIFICACION-FINAL-20260904.md           0

              El manifiesto de ESTE gate escribe su censo como texto indentado y no como
              tabla:
                kernel/operativo/runtime/estado/motor.py                      1817
              luego el cliquet no ve NI UNA de sus rutas.

              Y el validador que el arnés ejecuta NO ejecuta esa orden:
              # evidencia de: universo-obligatorio
              # orden: … derivar-universo-obligatorio.py --autopruebas
              # codigo: 0

              De modo que `36/36 validadores en verde` es compatible con un derivador que no
              puede derivar nada. La línea de base afirmada «universo obligatorio 58 · A=0 ·
              B=0 · C=0» NO ES REPRODUCIBLE desde la candidata.

REMEDIO       DOS piezas, y ninguna sola basta:
              (1) el manifiesto `F6-…-20260904.md` publica su censo como TABLA Markdown, con
                  la misma forma que los quince que sí funcionan;
              (2) el validador `universo-obligatorio` del arnés ejecuta la DERIVACIÓN REAL
                  además de `--autopruebas`, y publica su salida y su código. Un instrumento
                  cuya única evidencia son sus autopruebas puede estar muerto y salir verde,
                  que es exactamente el modo de fallo que este gate existe para impedir.

PROPIETARIO   SIS
FASE          F6
CLASE         instrumento de verificación · evidencia que no sostiene lo que afirma
```

---

### `R1-H02` · nada impide que `DSP` suba la prioridad, y `b.12` lo prohíbe con esas palabras

```text
SEVERIDAD     BLOQUEANTE
SEDE          kernel/operativo/runtime/runtime/dispatcher.py, el bloque `construir(revision)`
              de la transición `runtime.seleccion.postergada` (≈L766-795)
              La norma citada en TRES sedes del árbol:
                kernel/operativo/runtime/ciclo/planificacion.py:32
                kernel/operativo/runtime/runtime/vistas.py:29-31
                kernel/operativo/runtime/runtime/politica.py (docstring de `clave_de_orden`)
              «`b.12` es terminante —"DSP informa de la inanición. No cambia la prioridad.
              Nunca"»

REPRODUCCIÓN  Sobre una copia del checkout congelado, en `dispatcher.py`:
                                nuevo = dict(actual)
              +                 nuevo["prioridad"] = int(actual["prioridad"]) + 10
                                nuevo["seleccion"] = normalizar_seleccion(...)

              DOCE baterías, TODAS EXIT=0:
                test_cardinalidad_y_seleccion  OK (Ran 20 tests)
                test_runtime · test_ciclo · test_continua · test_agentes · test_arboles ·
                test_sesion_nueva · test_estado_durable · test_integridad_y_evidencia ·
                escenario_extremo_a_extremo · escenario_e2e_runtime · escenario_e2e_f6

              Y NO es código muerto — con una sonda en esa misma línea:
                test_cardinalidad_y_seleccion  EXIT=0 · sondas=16
                SONDA-A5c ALCANZADA: pq-espera-1 50 -> 60
                SONDA-A5c ALCANZADA: pq-espera-2 50 -> 60
                SONDA-A5c ALCANZADA: pq-espera-1 60 -> 70
                SONDA-A5c ALCANZADA: pq-espera-2 60 -> 70

              Se ejecuta 16 veces, muta la prioridad DURABLE y cambia el orden de selección
              de las pasadas siguientes. Ninguna prueba lo ve.

              CONTRASTE que lo hace grave: los OTROS OCHO sabotajes del mismo eje —los
              cuatro criterios de orden y los cuatro campos de inanición— ponen roja una
              prueba DISTINTA cada uno, y además disparan la meta-prueba `T269`. La única
              afirmación de `b.12` que el árbol cita LITERALMENTE tres veces es justo la
              única que no tiene prueba.

REMEDIO       una prueba `T2xx` en `test_cardinalidad_y_seleccion.py` que, tras N pasadas de
              postergación sobre el mismo paquete, exija que `paquete["prioridad"]` sea
              IDÉNTICA a la declarada al crearlo, y que la meta-prueba `T269` la incluya en
              su censo de sabotajes.

PROPIETARIO   ARQ (la prueba) · SIS (el contrato)
FASE          F6
CLASE         propiedad normativa citada y no probada
```

---

### `R1-H03` · «sin tocar el estado en modo PLAN» es falso, y es la sede que un implementador lee

```text
SEVERIDAD     MEDIA
SEDE          kernel/operativo/runtime/ciclo/continuacion.py:658
              """Los siete pasos, en orden. Determinista, y sin tocar el estado en modo PLAN."""

REPRODUCCIÓN  $ ads_estado.py --repo D inicializar
              $ ADS_ESTADO_FALLO=entre-el-paso-8-y-el-9 ads_estado.py --repo D transicion …
                EXIT=70
              $ ads_estado.py --repo D revision      → revision 0 · ventana preparada
              $ ads_ciclo.py --repo D --instancia inst-D continuar     (SIN --ejecutar)
                EXIT=0
              $ ads_estado.py --repo D revision      → revision 1 · ventana cerrada

              El modo PLAN cerró la ventana y AVANZÓ la revisión durable.

              EL COMPORTAMIENTO ES CORRECTO —§7.4 paso 2 manda COMPLETAR o MARCAR toda
              transacción con `abierta(tx)`, y §2.6.8 prohíbe leer el estado con la ventana
              abierta—. LO QUE ES FALSO ES LA FRASE, y es la única sede que describe el
              contrato del modo PLAN al que la implemente.

REMEDIO       reescribir la frase por lo que de verdad ocurre: «Determinista. En modo PLAN no
              consume órdenes, no despacha y no ordena reparaciones; SÍ cierra la ventana de
              una transacción abierta, porque el paso 2 de `b.14` lo manda y porque no se
              puede leer el estado sin cerrarla». Y una prueba que fije las dos mitades.

PROPIETARIO   ARQ
FASE          F6
CLASE         sede que dice menos —o más— de lo que el código hace
```

---

### `R1-H04` · el comprobador de cobertura sólo mide el ÚLTIMO tramo de un fichero con varios rangos

```text
SEVERIDAD     ALTA
SEDE          docs/evolucion/verificacion/comprobar-cobertura-de-gate.py:205
              asignadas_por_revisor[revisor] = {f["ruta"]: f for f in lote.get("fuentes")}

REPRODUCCIÓN  El manifiesto de este gate asigna a `REV-1` OCHO tramos distintos de
              `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` (§1, §2, §4, §7, §8, §14, §15,
              §17), 5 737 líneas en total. Al indexar por RUTA los ocho colapsan en uno y
              sobrevive el ÚLTIMO, §17 · [10853, 10881] · 29 líneas.

              Medido sobre mi propio manifiesto de lectura, que declara los OCHO tramos:
                líneas asignadas por el manifiesto (suma real): 40 630
                líneas asignadas que el instrumento cuenta:     34 922
                diferencia: 5 708 = 5 737 − 29

              CONSECUENCIA: un revisor que hubiera leído SÓLO las 29 líneas de §17 y
              declarado ese único tramo habría obtenido `LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS
              ∅` y `cerrado: sí`. El instrumento que `O27` §5 designa para impedir el cierre
              prematuro no puede verlo.

REMEDIO       indexar el lote por `(ruta, rango)` y no por `ruta`, y comprobar los huecos
              tramo a tramo; o exigir que un fichero con varios rangos aparezca como una sola
              entrada con lista de rangos. Y una autoprueba nueva en `--autopruebas`: «un
              fichero con DOS rangos asignados y sólo uno leído da resta NO vacía» —hoy los
              once controles no lo cubren.

PROPIETARIO   SIS
FASE          F6
CLASE         instrumento de gate con una resta que puede quedar vacía sin haberse medido
```

---

### `R1-H05` · `C4` plural lo sostiene UNA sola batería

```text
SEVERIDAD     BAJA
SEDE          kernel/operativo/runtime/ciclo/equipos.py `leer_cardinal` ·
              kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py

REPRODUCCIÓN  Con el cardinal plural aplanado a 1 (`minimo = maximo = 1`):
                test_cardinalidad_y_seleccion   EXIT=1  (failures=3, errors=6)
                test_ciclo                      EXIT=0
                escenario_e2e_f6                EXIT=0

REMEDIO       ninguno obligatorio: la cobertura EXISTE y es específica. Se registra para que
              nadie suponga que el E2E la sostiene: si esa batería se desactivara, `C4`
              plural quedaría sin red.

PROPIETARIO   ARQ
FASE          F6
CLASE         informativa sobre concentración de cobertura
```

---

### `R1-H06` · «trece campos» donde hay catorce, en las tres sedes definitorias

```text
SEVERIDAD     BAJA
SEDE          kernel/operativo/runtime/adaptadores/contrato.py:13  «con sus trece campos»
              kernel/operativo/runtime/adaptadores/contrato.py:53  «Los trece campos …»
              kernel/operativo/runtime/adaptadores/__init__.py:10  «con sus trece campos»

REPRODUCCIÓN  CAMPOS_DE_FICHA (contrato.py:54-58) tiene CATORCE entradas:
                identificador, version, capacidades, operaciones, limites, timeout,
                cancelacion, idempotencia, forma_de_progreso, resultado, errores,
                evidencia, compatibilidad, resolucion_del_control_repo

              Y el árbol YA LO SABE, en la batería y no en la norma:
              test_adaptadores.py:102 «afirmaba «los trece campos» y caducó en cuanto
              `CAMPOS_DE_FICHA` creció con …»

              Es decir: se corrigió la prueba y se dejó el cardinal caducado en las TRES
              sedes definitorias. Es la clase exacta de defecto que el propio corpus llama
              «cardinal escrito al lado de la enumeración que lo desmiente».

REMEDIO       retirar el cardinal en las tres sedes y remitir a `CAMPOS_DE_FICHA`, que es
              quien lo deriva. No sustituirlo por «catorce»: volvería a caducar.

PROPIETARIO   PLT
FASE          F6
CLASE         cardinal caducado en sede normativa
```

---

### `R1-H07` · confirmaciones que NO son hallazgos, y se dicen porque se midieron

```text
SEVERIDAD     INFORMATIVA

(a) LA MIGRACIÓN `0→1` HACE EXACTAMENTE LO QUE DECLARA. Los tres puntos de corte anteriores
    al punto de no retorno necesitan DOS llamadas —la primera cierra la ventana con
    `RECUPERACION_MARCADA`, la segunda retoma con identificador propio— y `migracion.py` lo
    declara nombrando los tres puntos y la causa. Medido punto por punto: coincide.

(b) LA SIEMBRA DE `ADJ-M3` ES PORTANTE. Retirándola, los tres E2E vuelven a VERDE sobre un
    almacén irrecuperable. La afirmación del contrato es cierta POR ELLA y sólo por ella,
    exactamente como su propio bloque declara.

(c) `FD-5` SE SOSTIENE ENTERO por la vía productiva: contención fuerte que mata al bisnieto
    con `setsid`, backend débil que lo deja escapar y LO DICE, y fallo cerrado con CERO
    ejecución cuando el anfitrión no ofrece contención fuerte.

(d) EL DETERMINISMO ES REAL: dos corridas completas independientes dejan los dos árboles
    byte a byte idénticos y los dos registros idénticos.
```

---

## 5 · Qué SÍ sostiene el árbol, en mi eje

Dicho en positivo, y sólo lo que he medido yo:

```text
ESTADO DURABLE        el protocolo de once pasos es recuperable en los DIEZ puntos de corte
                      controlados, con `verificar` en `ok` y convergencia al mismo `cid_raiz`.
                      El testigo `E-08` es una guarda REAL: retirarlo pone rojas 76 pruebas y
                      los tres escenarios extremo a extremo.

INVERSIÓN 8/9         detectable en sus dos formas —la literal y la sutil que fabrica el
                      testigo—, y los tres E2E NO pueden terminar verdes sobre un almacén
                      irrecuperable mientras la siembra esté puesta.

MIGRACIÓN 0→1         construida desde la especificación sobre un heredado GENUINO, migra,
                      retoma tras cada corte y no corrompe. Su comportamiento coincide con su
                      declaración incluso en el caso incómodo de los tres puntos que exigen
                      dos llamadas.

CONCURRENCIA          dos escritores REALES se serializan por `flock` exclusivo; cortar a uno
                      en cualquiera de las diez ventanas con el otro vivo deja la revisión en
                      1 o en 2, NUNCA en un estado intermedio, y `verificar` en `ok`. Romper
                      la exclusión mutua pone rojas cuatro pruebas de `Concurrencia`.

`b.12` PASO 5         los CUATRO criterios de orden y los CUATRO campos de inanición tienen
                      cada uno su prueba propia: ocho sabotajes, ocho pruebas distintas, más
                      la meta-prueba `T269` que lo afirma. Es la mejor cobertura que he
                      medido en todo mi lote — con el agujero de `R1-H02`.

`C4` PLURAL           el cardinal se DERIVA del campo `agentes`, el vocabulario es CERRADO y
                      lo ilegible falla cerrado en vez de valer 1.

CONTENCIÓN `FD-5`     política por NIVEL, elección comprobada al construir el adaptador,
                      fallo cerrado sin degradación silenciosa, y el límite del `setsid` en
                      el backend débil declarado en el propio mensaje de error.

`Continúa`            determinista: dos instancias distintas sobre el mismo estado producen
                      la MISMA huella y los MISMOS bytes.

DETERMINISMO GLOBAL   dos corridas completas del arnés dejan árbol y registro idénticos.
```

---

## 6 · Juicio expreso sobre bloqueantes internos vivos en mi eje

**Hay DOS bloqueantes vivos en mi eje, y los dos son del mismo tipo: una propiedad que el
árbol afirma y que nada mide.**

```text
`R1-H01`   El instrumento que DERIVA el universo obligatorio no puede derivarlo sobre la
           propia candidata —`EXIT=2`, fallo cerrado— porque el manifiesto que ESTE gate
           añadió es el único de los dieciséis que no publica su censo como tabla. Y el
           validador correspondiente sale VERDE porque sólo ejecuta sus autopruebas. La
           cifra de la línea base —«universo obligatorio 58 · A=0 · B=0 · C=0»— NO es
           reproducible desde el árbol congelado.

           POR QUÉ ES BLOQUEANTE Y NO ALTA: no es que una cifra no case. Es que el
           mecanismo por el que este gate sabe QUÉ hay que leer está roto sobre su propio
           objeto, y su verde no lo dice. Un gate cuyo derivador de obligatorio falla
           cerrado no puede afirmar que su universo esté completo.

`R1-H02`   `b.12` dice, y el árbol lo cita LITERALMENTE en tres sedes, «DSP informa de la
           inanición. NO cambia la prioridad. Nunca». Subir la prioridad en la misma
           transición durable que registra la postergación pasa DOCE baterías en verde, con
           la línea ejecutándose dieciséis veces y mutando el estado durable.

           POR QUÉ ES BLOQUEANTE: el resto de `b.12` paso 5 está probado con una disciplina
           ejemplar —ocho sabotajes, ocho pruebas distintas, meta-prueba incluida—, de modo
           que el hueco no es un descuido de cobertura general: es exactamente la única
           afirmación absoluta del contrato, y es la que no tiene red. Y su efecto no es
           cosmético: cambia el orden de despacho de las pasadas siguientes, escrito en el
           estado canónico.
```

**Y una precisión sobre el alcance de mi juicio, que es parte del juicio.** `R1-H04` no lo
declaro bloqueante porque su efecto sobre ESTE gate es nulo —yo leí los ocho tramos, y mi
resta es cero por lectura y no por la generosidad del instrumento—; pero es ALTA porque el
mecanismo que `O27` §5 designa para impedir un cierre prematuro **no puede detectar** un
lote de rangos leído a medias, y eso vale para cualquier gate futuro con la misma forma de
manifiesto.

**Fuera de eso, y en mi eje, no he encontrado ningún otro bloqueante.** Los siete ataques
que se me pidieron los he ejecutado enteros; cinco de ellos —migración, testigo, inversión
8/9, `C4` y contención— el árbol los sostiene, y en dos casos —la migración que MARCA y la
siembra portante— lo sostiene **diciendo la verdad incómoda en su propia sede**, que es lo
que más peso tiene de todo lo que he medido.

**No he corregido nada.** He atacado, he medido y he dictaminado.

---

**`REV-1` · lote CERRADO · `ASIGNADO − LEÍDO = ∅` · `LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS = ∅`**


---

# 8 · DICTAMEN ÍNTEGRO DEL REVISOR 2

## DICTAMEN · REVISOR 2 · GATE ÚNICO Y FINAL DE CERTIFICACIÓN DE `F6`

**Eje:** raíz externa, `O26`, firma, commit/tree, identidad, `--repo`, contaminación, `V6-15`,
admisión, Git multimáquina, evidencias, skips y sabotajes.

---

### 0 · LO PRIMERO, PORQUE MI RESTA NO ESTÁ A CERO

**`LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS ≠ ∅` para mi lote, y NO es porque me falte leer.**
He leído las 40 622 líneas que existen de mi lote. La línea que falta **no existe en el
árbol**: el manifiesto de asignación me asigna el tramo `11907-12153` de
`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, y ese fichero tiene **12 152 líneas** — el
propio manifiesto lo declara así, en el campo `lineas` de esa misma entrada.

Con el tramo declarado tal como el manifiesto lo asigna, el instrumento **se niega a medir**:

```
$ python3.12 docs/evolucion/verificacion/comprobar-cobertura-de-gate.py \
      --manifiesto .../MANIFIESTO-ASIGNACION.json --lectura .../lectura-REV-2.json \
      --raiz .../CANDIDATA
NO SE PUDO COMPROBAR · `REV-2` declara el tramo 11907-12153 sobre
`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, que tiene 12152 líneas: un tramo fuera del
fichero no describe ninguna lectura
CODIGO DE SALIDA = 2
```

Con el tramo recortado a lo que existe (`11907-12152`), la medida sale y la resta queda en
**una línea, la inexistente**:

```
COBERTURA DEL GATE · candidata 2ae0a93888a425cf85ba38d0ac054d069bbbe7d6
  REV-2    asignadas 104 · leídas sin hueco 103 · sin abrir   0 · con huecos   1
           líneas asignadas  36270 · sin leer      1 · cerrado declarado: sí

LAS CUATRO RESTAS
  OBLIGATORIO − ASIGNADO                 ∅
  ASIGNADO − LEÍDO                       ∅
  LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS       1
      REV-2 · docs/evolucion/11-ARQUITECTURA-INTEGRADA.md · faltan 1 líneas en 12153-12153
  FUENTES MODIFICADAS − LEÍDAS ÍNTEGRAS  136
  SIN MANIFIESTO DE LECTURA: REV-1, REV-3
  COBERTURA INCOMPLETA
```

**Ningún revisor puede llevar esa resta a cero**, porque la línea 12153 no existe. Por
`O27` §5 mi lote no cierra, y lo digo en la primera línea del dictamen como se me ordenó.
La partición del fichero, derivada del manifiesto, es: `1-94` **sin asignar a nadie**, sin
solapes entre revisores, y `12153` **asignada e inexistente**.

**Y hay algo peor, que mide el mismo instrumento contra sí mismo.** Ver `H-2` en §5.

---

### 1 · PRECONDICIONES

```
OBJETO           checkout congelado .../scratchpad/CANDIDATA
CANDIDATA        2ae0a93888a425cf85ba38d0ac054d069bbbe7d6
INTÉRPRETE       /home/jose/.local/bin/python3.12   (3.12.14 · PyYAML 6.0.2)
MANIFIESTO       /home/jose/ads-kernel/docs/f6/gate-definitivo/MANIFIESTO-ASIGNACION.{md,json}
                 rama gate/f6-certificacion-definitiva-20260904 · LEÍDO, no modificado
```

**Repositorio de control, al abrir y al cerrar:**

```
$ git status --porcelain     → vacío (las dos veces)
$ git rev-parse HEAD         → 54898fc9154b7f15bd93ba09003fe1b4e0941001 (las dos veces)
$ git rev-parse --abbrev-ref HEAD → gate/f6-certificacion-definitiva-20260904
```

Ningún comando `git` mío ha cambiado estado en `/home/jose/ads-kernel`. No he hablado con
los otros revisores.

**Integridad de mi lote contra el árbol congelado.** He recalculado el SHA-256 de las 113
entradas de mi lote sobre el checkout: **113/113 coinciden con el manifiesto**, y los
recuentos de líneas declarados coinciden con los reales en las 103 entradas de fichero
entero. Total real de mi lote: **40 622 líneas** (las 40 623 declaradas menos la
inexistente).

#### Declaración de un incidente propio, medido

Al principio ejecuté por error `registrar_evidencia.py --raiz` **sobre el checkout
congelado**. Lo maté, reextraje una copia prístina del SHA candidato con `git archive`
(operación de sólo lectura) y comprobé el checkout contra ella:

```
$ diff -rq REV2/PRISTINA CANDIDATA
Only in CANDIDATA/...: __pycache__      (14 directorios, 97 ficheros .pyc)
                                        ← NINGÚN "Files ... differ"
```

**Ningún fichero fuente del checkout difiere de la candidata.** El residuo es bytecode. He
medido si contamina lo que otros midan: `huella.py` da `7196ce99457a77d4` **igual** sobre el
checkout con residuo y sobre la copia prístina, luego el residuo no altera la huella
anclada. Lo declaro igualmente: **hay 97 `.pyc` en el objeto congelado que no están en la
candidata, y son míos**. Todo mi trabajo posterior se hizo sobre copias.

---

### 2 · LA LÍNEA BASE, REPRODUCIDA

Corrida limpia sobre una copia (`REV2/BASE`), no sobre el checkout:

```
$ cd REV2/BASE && python3.12 kernel/operativo/validadores/registrar_evidencia.py
...
36/36 validadores en verde · 36 evidencias publicadas · 0 problemas
CÓDIGO DE SALIDA = 0
```

**Y la evidencia que produce mi corrida es BYTE A BYTE la publicada en la candidata:**

```
$ diff -rq REV2/ev1 CANDIDATA/kernel/operativo/pruebas/evidencia/
(sin salida)
```

Y una **segunda corrida** sobre la misma copia, comparada byte a byte con la primera:

```
$ cd REV2/BASE && python3.12 kernel/operativo/validadores/registrar_evidencia.py
36/36 validadores en verde · 36 evidencias publicadas · 0 problemas
$ diff -rq REV2/ev1 REV2/BASE/kernel/operativo/pruebas/evidencia/
(sin salida)   ← determinismo byte a byte CONFIRMADO
```

Es más fuerte que dos corridas seguidas: los 36 ficheros que la candidata publica se
reproducen exactamente desde cero en otro anfitrión y otro momento, **y** dos corridas
consecutivas coinciden. Contadores, leídos de **mi** evidencia y no de la publicada:

```
158 infracciones detectadas · 0 NO detectadas
contrastados 195 · no contrastables 72 · divergencias 0
   (no contrastables por estado declarado: contrato-definido=56 prueba-ejecutada=12
    validador-implementado=4)
12 sabotajes del universo · 0 sin detectar
huella anclada: 7196ce99457a77d4
```

#### Lo que NO he podido reproducir: `universo 58 · A=0 · B=0 · C=0`

El validador `universo-obligatorio` sale en verde porque el manifiesto lo invoca con
`--autopruebas`, y sus 12 sabotajes internos pasan. **El mismo instrumento, haciendo su
trabajo real sobre esta candidata, FALLA CERRADO:**

```
$ cd REV2/BASE && python3.12 docs/evolucion/verificacion/derivar-universo-obligatorio.py
FALLA CERRADO · 1 manifiesto(s) INMUTABLE(s) de docs/evolucion/verificacion/manifiestos no
aportan NI UNA fila al cliquet: ['F6-ASIGNACION-GATE-CERTIFICACION-FINAL-20260904.md'] ...
CODIGO = 2
```

Reproducido idéntico sobre la copia prístina intacta (`CODIGO sobre PRISTINA = 2`). Causa
medida: ese manifiesto **no tiene ni una fila de tabla**
(`grep -c '^|'` → **0**; un manifiesto anterior comparable da **89**). Ver `H-3` en §5.

---

### 3 · LAS OCHO CONDICIONES DE `O26` §1, UNA A UNA, CON MI MEDIDA

Montaje propio, sobre copias: repo Git real (`commit 7a08168a…`, `tree fc227c1b…`),
instalación de la raíz externa **fuera** del árbol, par Ed25519 efímero **fuera**,
`CONFIANZA.yml` **fuera**. Corrida sana: **VERDE, código 0**, con la secuencia de siete
pasos completa (`firma · clave-aceptada · epoca · commit · tree · politica ·
identidad-del-emisor`).

#### 1 · La raíz y su evidencia viven fuera del árbol verificado — **CUMPLE**

```
$ ... verificador.py verificar --evidencia <DENTRO del árbol>
CODIGO=1
[EVIDENCIA_DENTRO_DEL_ARBOL] la evidencia de la raíz externa no puede escribirse dentro del
árbol que verifica ... (atestacion.json)
¿existe el fichero dentro? NO      ← no hay escritura parcial

$ ... verificador.py verificar --configuracion <DENTRO del árbol>
CODIGO=1
[CONFIGURACION_DENTRO_DEL_ARBOL] ... el repositorio decidiría por sí mismo qué identidad se
acepta, y `O25` §3 lo prohíbe
```

La instalación se materializa en un directorio ajeno al repo (42 ficheros, manifiesto de
6 897 bytes con SHA-256 por fichero).

#### 2 · La firma es asimétrica — **CUMPLE**

`ssh-keygen -Y` con Ed25519. `comprobar` verifica **sin** `ADS_ANFITRION_ALMACEN` y devuelve
código 0: quien verifica no necesita la clave privada. `anfitrion_verificador.py` no
contiene ni una mención de `ADS_ANFITRION_ALMACEN` ni de clave privada (`grep`, cero
resultados).

#### 3 · La atestación queda ligada SIMULTÁNEAMENTE al SHA del commit y a su `tree` — **CUMPLE**

Ataque real, no manipulación de bytes: **fabriqué tres atestaciones con firma VÁLIDA de la
clave aceptada**, cambiando sólo la tupla `(commit, tree)`.

```
atk-control  commit ✔ tree ✔ (refirmada)  → CODIGO=0 · VERDE
atk-commit   commit ✘ tree ✔              → CODIGO=1
   [VINCULO_DE_COMMIT_ROTO] la atestación habla del commit 000000000000 y se está
   comprobando 7a08168ad3f5
atk-tree     commit ✔ tree ✘              → CODIGO=1
   [VINCULO_DE_TREE_ROTO] la atestación habla del árbol 000000000000 y el commit comprobado
   tiene el árbol fc227c1b8f21: el commit coincide y su CONTENIDO no
```

**Las dos mitades enrojecen por códigos DISJUNTOS**, y una firma correcta de otra tupla no
pasa. La matriz `sano → VERDE · sabotaje → ROJO por el motivo esperado · restaurado → VERDE`
se cumple.

#### 4 · Firmante y verificador son componentes separados — **CUMPLE**

Dos ficheros distintos, dos procesos distintos, y cada uno rechaza el papel del otro:

```
$ anfitrion_firmante.py verificar
este anfitrion SOLO firma. Verificar es de anfitrion_verificador.py, que no tiene clave
privada                                              (código 4)
$ anfitrion_verificador.py firmar
uso: anfitrion_verificador.py --firmantes <fichero> verificar <identidad> <firma-hex>
```

#### 5 · El verificador no dispone de la clave privada — **CUMPLE**

Medido en 2 y 4. El circuito de comprobación completo se ejecuta sin la variable del
almacén.

#### 6 · El ejecutor no comparte capacidad de escritura sobre el control repo — **CUMPLE, EJERCIDA**

No la he leído: la he ejecutado. Mecanismo elegido por el propio aparato: **contenedor**,
imagen `alpine:3.20`, montaje de sólo lectura.

```
identidad_del_runtime      uid 1000 · gid 1000
identidad_del_verificador  uid 65534 · gid 65534      identidad_distinta: true
8 intentos de escritura · 8 impedidos:
  modificar-un-fichero                     Permission denied
  crear-un-fichero                         Read-only file system
  borrar-un-fichero                        Read-only file system
  cambiar-una-ref                          Read-only file system
  alterar-la-configuracion-de-git          Permission denied
  sustituir-la-clave-publica-aceptada      Read-only file system
  cambiar-la-politica                      Permission denied
  modificar-la-atestacion-ya-firmada       Permission denied
control_positivo (escribir en lo propio)   escribio: true   ← el control no falla por no arrancar
control_de_lectura (el árbol está montado) leyo: true
ok: true · no_ejecutados: []
EXIGIR_SIN_ESCRITURA: PASA
```

Es exactamente la demostración transitoria que `O26` §3 acepta.

#### 7 · Existen rotación, solapamiento, retirada y revocación — **CUMPLE**

```
retirada época 1, solapamiento 3, atestación de época 1  → CODIGO=0  (control POSITIVO)
retirada época 1, solapamiento 0, atestación de época 5  → CODIGO=1
   [IDENTIDAD_NO_ACEPTADA] ... verifica hasta la 1 y la firma es de la 5
revocada, solapamiento 9                                 → CODIGO=1
   [IDENTIDAD_NO_ACEPTADA] ... está REVOCADA: lo que firmó no vale, y su solapamiento no se
   honra
```

Se mide en ÉPOCAS y no en reloj, y la revocación no honra el solapamiento.

#### 8 · Clave desconocida, firma inválida, commit incorrecto, tree incorrecto, ausencia de proveedor y **contaminación del entorno** fallan cerrado — **NO CUMPLE**

Cinco de los seis, cumplidos:

```
clave desconocida (otra clave válida, no declarada)  → CODIGO=1 [FIRMA_NO_VERIFICADA]
firma inválida (un byte cambiado)                    → CODIGO=1 [FIRMA_NO_VERIFICADA]
modificación posterior a la firma                    → CODIGO=1 [ATESTACION_INVALIDA]
                                                       "el sobre se ha manipulado"
commit incorrecto                                    → CODIGO=1 [VINCULO_DE_COMMIT_ROTO]
tree incorrecto                                      → CODIGO=1 [VINCULO_DE_TREE_ROTO]
ausencia de proveedor (sin ADS_ANFITRION_ALMACEN)    → CODIGO=1 [ANFITRION_NO_RESPONDE]
                                                       evidencia escrita: NO
almacén inexistente                                  → CODIGO=1 [ANFITRION_NO_RESPONDE]
                                                       evidencia escrita: NO
```

**El sexto, no.** La contaminación del entorno **no falla cerrado: produce VERDE FALSO.**
Es `H-1`, y está medido entero en §4.

---

### 4 · LOS ATAQUES, CON SU ORDEN Y SU SALIDA LITERAL

#### 4.1 · Contaminación por `PYTHONPATH` con homónimos de la biblioteca estándar

**Control positivo primero**, para que «no pasó nada» no tenga la explicación fácil:

```
$ cat veneno/json.py      → loads/dumps devuelven {} 
$ cat veneno/hashlib.py   → sha256().hexdigest() == "deadbeef…"
$ PYTHONPATH=veneno python3.12 control-sin-prologo.py
json.dumps: {}
sha256: deadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef
modulo json desde: .../veneno/json.py            ← el veneno FUNCIONA
```

**Contra los puntos ejecutables CON prólogo `E-10`, el veneno no entra:**

```
$ PYTHONPATH=veneno python3.12 raiz-externa/verificador.py capacidades
CODIGO=0   y la salida es REAL, no {}
$ PYTHONPATH=veneno python3.12 validadores/huella.py
7196ce99457a77d4                                  ← la huella verdadera
```

**Y el ataque histórico de `ADJ-B2` está cerrado.** Instalar con el homónimo `json.py`
puesto ya no produce un manifiesto de tres bytes:

```
$ PYTHONPATH=veneno python3.12 raiz-externa/instalar.py --destino inst-json --arbol …
CODIGO=0 · manifiesto de 6897 bytes · 42 ficheros
$ python3.12 inst-json/raiz-externa/verificador.py instalacion --instalacion inst-json
CODIGO=0 · {"alteradas": [], "ausentes": [], "ok": true, "sobrantes": []}
```

#### 4.2 · El vector que el prólogo NO cubre: el gancho de arranque — **VERDE FALSO**

El prólogo purga `sys.path` **en su primera sentencia**. `site.py` importa
`sitecustomize` **antes de que el guion ejecute su primer byte**, y un gancho de arranque no
necesita `sys.path` para nada: **muta el módulo ya importado en su sitio**. El
CONTROL DEL CONTROL del prólogo comprueba de dónde vino `os`, no si una primitiva fue
sustituida, y `os` aquí es el auténtico.

```
$ cat hook/sitecustomize.py
import hashlib as _h
class _D: ...  hexdigest() -> "deadbeefbeefbeef…"
_h.sha256 = lambda *a, **k: _D()

$ PYTHONPATH=hook python3.12 -c "import hashlib;print(hashlib.sha256(b'x').hexdigest())"
deadbeefbeefbeefdeadbeefbeefbeefdeadbeefbeefbeefdeadbeefbeefbeef

$ PYTHONPATH=hook python3.12 validadores/huella.py
deadbeefbeefbeef                     ← la huella anclada NEUTRALIZADA
```

**Y la cadena completa, que es lo que lo convierte en verde falso:**

```
1 · INSTALAR con el gancho puesto
    $ PYTHONPATH=hook python3.12 raiz-externa/instalar.py --destino inst-hook --arbol …
    CODIGO=0 · 41 entradas de manifiesto, todas con el digest constante

2 · ALTERAR la instalación
    $ echo "# CODIGO INYECTADO POR EL ATACANTE" >> inst-hook/raiz-externa/verificador.py

3 · COMPROBAR con el mismo gancho
    $ PYTHONPATH=hook python3.12 inst-hook/raiz-externa/verificador.py instalacion …
    CODIGO=0
    { "alteradas": [], "ausentes": [], "ok": true, "sobrantes": [] }   ← VERDE FALSO

4 · CONTROL: la misma comprobación SIN el gancho
    CODIGO=1
    [INSTALACION_ALTERADA] ... 41 alteradas, 0 ausentes, 0 sobrantes
```

`grep` sobre `verificador.py`: **cero** menciones de `sitecustomize`, `usercustomize`, `-S`,
`-E` o `PYTHONNOUSERSITE`. El vector no está contemplado.

**Tres remedios, medidos por mí:**

```
autocomprobación de la primitiva  sha256(b"") ≠ e3b0c442…  → CAZADO
python3.12 -S                     → 2d711642b726b044… (digest real)
python3.12 -E                     → 2d711642b726b044… (digest real)
```

#### 4.3 · El inventario de puntos ejecutables, DERIVADO por mí

No me fío del recuento del commit (35 puntos / 109 exclusiones / 0 sin clasificar). Lo
derivé con `ast`, con el predicado que el propio `README` declara (`__main__` o
`sys.exit`/`raise SystemExit` en el nivel superior):

```
ficheros .py en el árbol      144
con línea `#!`                137
INVOCABLES (predicado T330)    56
con el MECANISMO E-10          37
INVOCABLES SIN el mecanismo    20   ← 19 baterías de runtime/pruebas/ + tooling/tests/test_workspace.py
con el mecanismo sin ser invocable  1   (validadores/negativos_runtime.py)
```

La equivalencia que el `README` publica —`lleva #!` ⟺ `es INVOCABLE` ⟺ `lleva el
MECANISMO`— **no es cierta sobre el árbol tal cual**: 137 llevan `#!`, 56 son invocables y
37 llevan el mecanismo. `kernel/operativo/runtime/estado/motor.py`, que el `README` describe
como módulo, lleva `#!/usr/bin/env python3` en su primera línea.

#### 4.4 · Las baterías sin prólogo: **deuda acotada o agujero** — es AGUJERO

La cadena, medida en tres pasos:

```
1 · registrar_evidencia.py:212 (literal, sin `env=`):
      proc = subprocess.run([sys.executable, script, *ej.args],
                            cwd=base, capture_output=True, text=True)
    NO leído: OBSERVADO. Repetí esa llamada exacta con una sonda por hijo:
      PYTHONPATH del hijo: .../veneno2
      hashlib del hijo:    .../veneno2/hashlib.py
      sha256 del hijo:     c0ffeec0ffee…
    → el PYTHONPATH del lanzador llega intacto a los 36 hijos

2 · la batería SIN prólogo carga el veneno y no se entera:
    $ PYTHONPATH=veneno2 python3.12 runtime/pruebas/test_identidad.py
      Ran 23 tests  (duración no registrada: varía por ejecución)
      OK
      CODIGO=0
    sonda en el mismo directorio y entorno:
      hashlib.__file__ = .../veneno2/hashlib.py
      hashlib.sha256(b'x').hexdigest() = c0ffeec0ffee…

3 · el punto ejecutable CON prólogo, en el mismo entorno, resiste:
    $ PYTHONPATH=veneno2 python3.12 validadores/huella.py
      7196ce99457a77d4
```

`test_identidad.py` es precisamente la batería que demuestra `O25` §2 —que ningún secreto
aparece en estado, diario, evidencia ni errores— y **su instrumento de medida es
`hashlib.sha256`**. Bajo el veneno esa garantía se comprueba con una primitiva falsa y la
batería sigue diciendo `OK`.

**Lo MEDIDO y lo INFERIDO, separados, para que nadie me lea de más.** Medidos, los dos
eslabones: que el entorno del lanzador llega intacto al hijo (paso 1, observado con sonda) y
que una batería sin prólogo carga el veneno y publica `OK` con código 0 (paso 2). **Inferido,
el extremo:** que una corrida completa bajo `PYTHONPATH` envenenado publicaría las 20
evidencias de batería sobre primitivas sustituidas. No he ejecutado esa corrida completa, y
lo digo en vez de presentarlo como medido. Lo que sí queda medido es que **no es deuda
acotada**: los 20 puntos invocables sin prólogo son alcanzables desde el entorno del
lanzador, y ninguno se defiende.

#### 4.5 · Evidencias, skips y contadores — matriz completa, y **AGUANTA**

Sobre copia, con `comprobar_evidencia.py`:

```
SANO                                                              CODIGO=0
SABOTAJE A · "OK" → "OK (skipped=7)", skips no declarados         CODIGO=1
   · no contiene el resumen de éxito que su validador produce (/(?m)^OK$/)
   · la corrida SALTÓ 7 caso(s) y el manifiesto no declara ninguno. `OK (skipped=7)` no es
     `OK`: los casos saltados no demuestran nada y su ausencia no se publica
RESTAURADO                                                        CODIGO=0
SABOTAJE B · contador manipulado, "Ran 23" → "Ran 99"             CODIGO=1
   · declara `Ran 99 tests` y su salida contiene 23 desenlaces de caso ... manipular el
     contador INVALIDA la evidencia
SABOTAJE C · "FAILED (failures=3)" + una línea que TERMINA en "OK" CODIGO=1
   · no contiene el resumen de éxito ... (/(?m)^OK$/)
   · la batería NO terminó en OK (FAILED failures=3)
```

**`firma_de_exito` es `(?m)^OK$`, anclada por los dos extremos: no casa con un subcadena.**
La pregunta del encargo tiene respuesta negativa: no se puede colar un éxito pegando `OK` a
otra línea. Lo usan 18 de los 36 componentes.

#### 4.5bis · El sabotaje que NO discrimina: la firma de éxito admite el CERO

El encargo me pide buscar uno que no discrimine. Lo hay, y no en el catálogo de mutaciones
sino en la firma de éxito de 14 componentes. Los valores distintos de `firma_de_exito` en
`validadores.yaml` son nueve; cuatro de ellos llevan `\d+`, y **`\d+` casa con `0`**:

```
18 × '(?m)^OK$'
11 × '\d+ superadas · 0 fallidas'
 1 × '\d+ infracciones detectadas · 0 NO detectadas'
 1 × '\d+ sabotajes · 0 sin detectar'
 1 × '\d+ controles · 0 sin detectar'
 3 × cardinal FIJO ('25 de 25 pasos CUMPLIDOS', '24 de 24', '15 de 15')
 1 × 'errores: 0 · avisos: 0'
```

Medido sobre copia, un sabotaje a la vez, con control:

```
CONTROL · árbol sano                                                CODIGO=0
SABOTAJE · recuentos-salida.txt: '7 superadas · 0 fallidas'
           →                     '0 superadas · 0 fallidas'         CODIGO=0  ← NO ENROJECE
SABOTAJE · negativos-salida.txt: '158 infracciones detectadas · 0 NO detectadas'
           →                     '0 infracciones detectadas · 0 NO detectadas'
           universo-obligatorio-salida.txt: '12 sabotajes · 0 sin detectar'
           →                               '0 sabotajes · 0 sin detectar'
                                                                    CODIGO=0  ← NO ENROJECE
           veredicto publicado: "2 superadas · 0 fallidas"
```

**La evidencia puede declarar que se ejercitaron CERO sabotajes y que se detectaron CERO
infracciones, y el comprobador de evidencia lo acepta como éxito.** No distingue «pasó todo»
de «no corrió nada». Y no hay red debajo: `grep` sobre el árbol entero no encuentra ninguna
sede que ancle el cardinal `158`, y `comprobar_negativos.py` no lleva ningún suelo — su
`CATALOGO` tiene hoy 158 entradas y nada comprueba que no encoja. Es `H-8`.

#### 4.6 · Git multimáquina: la serialización no descansa en `flock`

`estado/bloqueo.py` usa `fcntl.flock`, que es **por máquina**. Lo que serializa entre
escritores es un **objeto durable**, y lo he ejercido con el `flock` libre:

```
A concede refs/heads/canonica                    → OK
B (otro titular) concede la MISMA ref            → DOBLE_ESCRITOR
   "la ref ya está concedida a otro titular en la época 1; la autoridad no se comparte"
B concede otra ref distinta (CONTROL POSITIVO)   → OK
objeto que serializa: refs/refs.heads.canonica.json
   {"epoca": 1, "titular": "maquina-A", "ref": "refs/heads/canonica", ...}
```

El rechazo se produce **sin concurrencia y con el cerrojo libre**: decide el estado durable
(titular + época), no el `flock`. `gobierno/control.py` lo declara así y lo cumple.

#### 4.7 · Los dos sabotajes que NO enrojecen nada

Están en `H-2` (la propia cobertura: 4 600 líneas leídas y 246 dan salida idéntica) y en
`H-8` (la firma de éxito acepta el cero), porque son hallazgos y no sólo ataques.

---

### 5 · HALLAZGOS

#### `H-1` · La contaminación del entorno produce VERDE FALSO — la condición 8 de `O26` §1 NO se cumple

```
SEVERIDAD     BLOQUEANTE
CLASE         interna de `F6`
SEDE          kernel/operativo/raiz-externa/{verificador,instalar}.py y los 37 puntos que
              copian el mecanismo `E-10`; kernel/operativo/validadores/huella.py
REPRODUCCIÓN  §4.2 de este dictamen, cuatro órdenes, con control positivo y control sin
              gancho. `verificador.py instalacion` devuelve
              {"ok": true, "alteradas": []} CÓDIGO 0 sobre una instalación con código
              inyectado
POR QUÉ       el prólogo purga `sys.path` en su primera sentencia; `site.py` importa
              `sitecustomize` antes de esa sentencia, y un gancho muta la primitiva ya
              importada. El CONTROL DEL CONTROL mira la procedencia de `os`, no la
              sustitución de `hashlib.sha256`
REMEDIO       (a) reejecutar el punto con `-S -E` y entorno saneado; o (b) autocomprobar la
              primitiva contra un vector conocido antes de usarla —medido: caza el gancho—.
              (b) es más barato y además cubre la mutación en sitio
PROPIETARIO   PLT construye · SIS define la conformidad
FASE          F6
```

**Consecuencia directa sobre el gate:** `O26` §1 exige las ocho conjuntamente y `O26` §5.4
exige que la implementación las satisfaga. Con la condición 8 incumplida, **`O26` §5 no
autoriza declarar `F6 CERTIFICADA`**.

#### `H-2` · El instrumento de cobertura no mide la mayor parte de lo que declara asignado

```
SEVERIDAD     BLOQUEANTE (del método del gate, no del árbol)
CLASE         interna de `F6` / instrumental del gate
SEDE          docs/evolucion/verificacion/comprobar-cobertura-de-gate.py:205
                  asignadas_por_revisor[revisor] = {f["ruta"]: f for f in lote["fuentes"]}
              un diccionario indizado por RUTA: varias entradas del mismo fichero se
              colapsan y sólo sobrevive la ÚLTIMA
REPRODUCCIÓN  declaré leída de `11-ARQ` SÓLO el último rango asignado (246 de las 4 600
              líneas que el manifiesto me asigna) y comparé con mi lectura honesta:
                 $ diff cob-honesta.txt cob-solo-ultimo-rango.txt
                 (sin salida)  ← SIN DIFERENCIAS
              y con una sola línea declarada, el instrumento sólo echa en falta las del
              último rango: "faltan 246 líneas en 11907-12151, 12153-12153"
QUÉ SIGNIFICA de los 10 rangos que se me asignan, el instrumento comprueba 1. Las 4 353
              líneas de los otros 9 son invisibles: un revisor que no leyera ninguna
              produciría exactamente la misma salida que yo. Lo mismo vale para REV-1
              (8 rangos → 1) y REV-3 (3 rangos → 1)
              Y el número que publica es falso por lo mismo: dice "líneas asignadas 36270"
              cuando mi lote son 40 622
REMEDIO       indizar por (ruta, rango) y acumular los tramos asignados por fichero antes
              de restar
PROPIETARIO   PLT
FASE          F6, y ANTES de cualquier gate que invoque `O27` §5
```

#### `H-3` · El universo obligatorio no se deriva del árbol, y su derivador falla cerrado sobre esta candidata

```
SEVERIDAD     BLOQUEANTE (del método del gate)
CLASE         interna de `F6` / instrumental del gate
SEDE (a)      docs/evolucion/verificacion/derivar-universo-obligatorio.py
              $ python3.12 derivar-universo-obligatorio.py     → CÓDIGO 2, FALLA CERRADO
              causa: docs/evolucion/verificacion/manifiestos/
                     F6-ASIGNACION-GATE-CERTIFICACION-FINAL-20260904.md aporta CERO filas
                     (`grep -c '^|'` = 0; un manifiesto comparable da 89)
              el validador sale en verde porque el manifiesto lo invoca `--autopruebas`:
              se ejercitan sus 12 sabotajes internos, NO su trabajo sobre esta candidata
SEDE (b)      comprobar-cobertura-de-gate.py:236-246. Su propio comentario declara la
              DECISIÓN (c) —«el suelo lo pone el árbol: toda fuente MODIFICADA entre la
              base y la candidata es obligatoria», «derivarlo del árbol con `git diff`»—
              y el código hace (a): `declarado_obligatorio = manifiesto["obligatorio"] |
              manifiesto["modificadas"]`. El fichero no importa `subprocess` y no invoca
              `git` ni una vez
QUÉ SIGNIFICA la primera resta, `OBLIGATORIO − ASIGNADO`, se calcula contra lo que el
              propio manifiesto declara obligatorio. Es la alternativa que el comentario
              rechaza con estas palabras: «el manifiesto que se equivoca al asignar se
              equivoca igual al declarar qué era obligatorio». Su `∅` no prueba lo que
              `O27` §5 pide
REMEDIO       (a) arreglar la forma del manifiesto nuevo o el lector del cliquet, y que el
              validador ejerza la derivación real y no sólo `--autopruebas`;
              (b) implementar la decisión (c) declarada, con `git diff base..candidata`
PROPIETARIO   PLT
FASE          F6, y antes de cualquier gate posterior
```

#### `H-4` · El manifiesto de asignación asigna una línea que no existe

```
SEVERIDAD     BLOQUEANTE del gate (impide cerrar mi lote por `O27` §5)
CLASE         del método del gate
SEDE          docs/f6/gate-definitivo/MANIFIESTO-ASIGNACION.json, entrada de REV-2 para
              docs/evolucion/11-ARQUITECTURA-INTEGRADA.md: rango [11907, 12153] con
              lineas: 12152 en la MISMA entrada
REPRODUCCIÓN  §0 de este dictamen. El instrumento se niega a medir (CÓDIGO 2) o, recortado
              a lo existente, deja la tercera resta en 1
ADEMÁS        las líneas 1-94 del mismo fichero no se asignan a ningún revisor (sin
              solapes entre los tres)
REMEDIO       corregir el extremo del rango a 12152 y decidir expresamente si 1-94 quedan
              fuera del universo
PROPIETARIO   el coordinador del gate
FASE          ya
```

#### `H-5` · Una evidencia ausente produce una traza de Python, no un veredicto

```
SEVERIDAD     MEDIO (falla cerrado: código 1; el defecto es de diagnóstico)
CLASE         interna de `F6`
SEDE          kernel/operativo/raiz-externa/verificador.py:604, `_orden_comprobar`
REPRODUCCIÓN  $ verificador.py comprobar --evidencia <ruta que no existe>
              CODIGO=1
              Traceback ... FileNotFoundError: [Errno 2] No such file or directory
REMEDIO       tipar el caso, como hacen los demás (`[EVIDENCIA_...]` con su motivo). El
              propio corpus lo exige por dos vías: `V6-03` («fallo CERRADO ... nunca lista
              vacía silenciosa») y `T344` («una traza no es un veredicto»)
PROPIETARIO   PLT
FASE          F6
```

#### `H-6` · La equivalencia de `T330` publicada en el `README` de la raíz externa no describe el árbol

```
SEVERIDAD     BAJO (documental; no afecta al veredicto de ninguna prueba)
CLASE         interna de `F6`
SEDE          kernel/operativo/raiz-externa/README.md, bloque
              «lleva `#!` ⟺ define `__main__` ⟺ lleva el prólogo `E-10`»
REPRODUCCIÓN  §4.3. 137 ficheros llevan `#!`, 56 son invocables, 37 llevan el mecanismo.
              `runtime/estado/motor.py`, descrito como módulo, lleva `#!/usr/bin/env python3`
REMEDIO       escribir la equivalencia sobre el predicado que `T330` usa de verdad
              (INVOCABLE ⟺ MECANISMO), y decir que `#!` es una tercera cosa con sus clases
              de exclusión
PROPIETARIO   SIS
FASE          F6
```

#### `H-8` · La firma de éxito de 14 componentes admite el CERO: no distingue «pasó todo» de «no corrió nada»

```
SEVERIDAD     GRAVE
CLASE         interna de `F6`
SEDE          kernel/operativo/validadores/validadores.yaml — los `firma_de_exito` con
              `\d+`: '\d+ superadas · 0 fallidas' (11 componentes),
              '\d+ infracciones detectadas · 0 NO detectadas',
              '\d+ sabotajes · 0 sin detectar', '\d+ controles · 0 sin detectar'
REPRODUCCIÓN  §4.5bis. Con la evidencia del catálogo de mutaciones editada a
              `0 infracciones detectadas · 0 NO detectadas` y la del universo a
              `0 sabotajes · 0 sin detectar`, `comprobar_evidencia.py` publica
              «2 superadas · 0 fallidas» y sale con CÓDIGO 0
POR QUÉ IMPORTA el catálogo de 158 mutaciones y los 12 sabotajes del universo son la mitad
              adversarial del aparato: son lo que demuestra que los validadores pueden
              fallar. Su cardinal no está anclado en ninguna sede (`grep` sobre el árbol:
              cero resultados para `158 infracciones`), `comprobar_negativos.py` no lleva
              suelo alguno, y la firma que los certifica acepta el cero. Un catálogo que
              encogiera —por edición del código o de la evidencia— seguiría certificándose
QUÉ SÍ COMPENSA, la zona `kernel/operativo/pruebas/evidencia/` es INMUTABLE para el
Y HASTA DÓNDE verificador de admisión, y he comprobado que ese control existe y enrojece
              (`T189`, ataque `S1-02` §3.6: hallazgo con `zona = EVIDENCIA` y causa
              `INMUTABLE`). Pero eso ataja la EDICIÓN de la evidencia, no el ENCOGIMIENTO
              del catálogo, y depende de un ancla externa que es `V6-16` — no implementado
              en producción. La firma en sí no es un control
REMEDIO       sustituir `\d+` por un suelo derivado (`[1-9]\d*` como mínimo) y, mejor,
              anclar el cardinal del catálogo como los tres escenarios ya hacen con
              `'25 de 25 pasos CUMPLIDOS'`, que sí discrimina
PROPIETARIO   SIS define · PLT materializa
FASE          F6
```

#### `H-7` · Contaminación del objeto congelado por este revisor

```
SEVERIDAD     BAJO, y declarado
CLASE         del método del gate
SEDE          el checkout .../scratchpad/CANDIDATA: 14 directorios __pycache__, 97 .pyc
REPRODUCCIÓN  diff -rq PRISTINA CANDIDATA (§1). Ningún fichero fuente difiere
MEDIDO        no altera la huella anclada (7196ce99457a77d4 con y sin residuo)
REMEDIO       reextraer el checkout con `git archive` si otro revisor va a inventariar el
              árbol por extensión
PROPIETARIO   yo, REV-2
```

---

### 6 · LO QUE EL ÁRBOL SÍ SOSTIENE

No todo lo que he atacado ha cedido, y decirlo es parte del dictamen.

```
LA LÍNEA BASE ES REAL          36/36 · 36 evidencias · 0 problemas, reproducido desde cero,
                               y las 36 evidencias salen BYTE A BYTE iguales a las
                               publicadas. El determinismo no es una declaración

EL VÍNCULO COMMIT/TREE         resiste el ataque fuerte —firma VÁLIDA de otra tupla— y
                               enrojece por códigos DISJUNTOS. Es lo que `O26` §1.3 pide

LA ASIMETRÍA Y LA SEPARACIÓN   firmante y verificador son procesos distintos que rechazan el
                               papel del otro; el verificador nunca ve la clave privada

EL AISLAMIENTO DEL EJECUTOR    ejercido de verdad: contenedor, uid 65534 frente a 1000,
                               8/8 escrituras impedidas, con control positivo y de lectura

LA ROTACIÓN EN ÉPOCAS          solapamiento honrado, retirada fuera de él rechazada,
                               revocación que no honra solapamiento

LA EVIDENCIA NO SE FALSEA      `(?m)^OK$` está anclada por los dos extremos; los skips no
POR LA VÍA DE `OK`             declarados, el contador manipulado y el `OK` pegado se cazan
                               los tres, con su motivo propio. Lo que NO tapa esa firma es
                               el cero: ver `H-8`

EL DETERMINISMO ES REAL        dos corridas consecutivas producen las 36 evidencias byte a
                               byte iguales entre sí y byte a byte iguales a las publicadas

EL ATAQUE HISTÓRICO `ADJ-B2`   cerrado: `PYTHONPATH` con homónimos de la estándar ya no
                               produce el manifiesto de tres bytes, y el prólogo `E-10`
                               protege los 37 puntos que lo llevan

LA SERIALIZACIÓN MULTIMÁQUINA  no descansa en `flock`: la decide un objeto durable con
                               titular y época, verificado con el cerrojo libre y con
                               control positivo

LA CONFIGURACIÓN Y LA          las dos viven fuera del árbol verificado, y las dos rutas
EVIDENCIA                      hacia dentro fallan cerrado sin dejar escritura parcial
```

---

### 7 · MI JUICIO EXPRESO SOBRE BLOQUEANTES INTERNOS VIVOS EN MI EJE

**Sí quedan bloqueantes internos vivos en mi eje, y son tres.**

1. **`H-1`.** La octava condición de `O26` §1 —«contaminación del entorno falla cerrado»—
   **no se cumple sobre esta candidata**. No es que falle abierto en un caso raro: un gancho
   de arranque neutraliza la huella anclada y hace que la comprobación de integridad de la
   instalación diga `{"ok": true}` sobre ficheros con código inyectado. `O26` §1 exige las
   ocho **conjuntamente**, y `O26` §5.4 hace de esa satisfacción condición de competencia del
   gate. **Con esta condición incumplida, un gate válido no puede declarar `F6 CERTIFICADA`.**

2. **`H-4`.** Mi lote **no cierra** por `O27` §5, y no por falta de lectura: el manifiesto me
   asigna una línea que no existe. Es defecto del gate, no de la candidata, pero el efecto es
   el mismo: la tercera resta no puede llegar a `∅`.

3. **`H-2` y `H-3`.** Los dos instrumentos sobre los que descansa `O27` §5 no miden lo que
   dicen medir. El de cobertura ignora todos los rangos de un fichero salvo el último —lo he
   demostrado produciendo salida **idéntica** con 4 600 líneas leídas y con 246—, y la
   primera resta se calcula contra lo que el propio manifiesto declara obligatorio mientras
   el derivador real del universo **falla cerrado** sobre esta candidata. Una cobertura
   medida con ellos no sostiene la afirmación que `O27` §5 exige.

Y un cuarto, que no clasifico como bloqueante pero que el adjudicador debe pesar:
**`H-8`**, la firma de éxito de 14 componentes admite el cero, de modo que la mitad
adversarial del aparato —158 mutaciones y 12 sabotajes del universo— se certificaría igual
si encogiera a nada. Lo dejo en GRAVE y no en BLOQUEANTE porque existe un control
compensatorio real —la zona de evidencia es INMUTABLE para el verificador de admisión, y lo
he visto enrojecer—, pero ese control depende de un ancla externa que es `V6-16`.

**Recomendación, ceñida a mi eje y sin extenderme a lo que no he medido:** las cinco
condiciones de `O26` §5 **no se satisfacen simultáneamente** sobre `2ae0a938…`. En concreto
falla la 4 (por `H-1`) y no es demostrable la cobertura que el propio método exige (por
`H-2`, `H-3` y `H-4`). Por `O26` §8, la aceptación arquitectónica de la raíz externa
permanece —y he medido que siete de sus ocho condiciones **sí** se cumplen—, pero `F6` sigue
ABIERTA y PesquerApp sigue BLOQUEADA.

No corrijo nada. He atacado, he medido y esto es lo que sale.

---

### 8 · CIERRE

```
LOTE          113 entradas · 103 ficheros enteros + 10 rangos de 11-ARQ
LEÍDO         40 622 líneas, que son TODAS las que existen de lo asignado
CERRADO       NO, por `H-4`: la línea 12153 no existe y ninguna lectura puede cubrirla
REPOSITORIO   porcelain vacío · HEAD 54898fc9154b7f15bd93ba09003fe1b4e0941001, sin cambios
FICHEROS      lectura-REV-2.json · cob1.txt · cob2.txt · cob-mut.txt ·
DE APOYO      lectura-REV-2-SOLO-ULTIMO-RANGO.json · lectura-REV-2-MUTANTE.json ·
              REV2/O26/* · REV2/SKIPS/* · REV2/MM/* · REV2/run1.txt · REV2/ev1/
```


---

# 9 · DICTAMEN ÍNTEGRO DEL REVISOR 3

## DICTAMEN DEL REVISOR 3 · GATE ÚNICO DE CERTIFICACIÓN FINAL DE `F6`

**Objeto juzgado:** el checkout congelado de la candidata `2ae0a93888a425cf85ba38d0ac054d069bbbe7d6`.
**Intérprete:** `/home/jose/.local/bin/python3.12` · 3.12.14 · PyYAML 6.0.2.
**Fecha del dictamen:** 2026-09-05.

> **No he corregido nada.** Todo ataque se ejecutó sobre COPIAS del checkout congelado o
> sobre CLONES `git clone --no-local` del repositorio. Los hallazgos quedan REGISTRADOS y NO
> APLICADOS.

---

### 0 · PRECONDICIONES

#### 0.1 · El repositorio del Owner, intacto a la apertura y al cierre

```console
$ git -C /home/jose/ads-kernel rev-parse HEAD
54898fc9154b7f15bd93ba09003fe1b4e0941001
$ git -C /home/jose/ads-kernel rev-parse --abbrev-ref HEAD
gate/f6-certificacion-definitiva-20260904
$ git -C /home/jose/ads-kernel status --porcelain
(vacío)
$ git -C /home/jose/ads-kernel for-each-ref | wc -l
106
```

Idénticos a la apertura. Ni un comando de git que cambie estado se ejecutó sobre esa ruta:
el manifiesto se LEYÓ, y para atacar la sede del Owner cloné con `git clone --no-local` a
`scratchpad/CLONF`.

#### 0.2 · El checkout congelado es el objeto correcto

Las 79 filas de mi lote se contrastaron una a una por SHA-256 contra el checkout: **0
discrepancias**. El checkout no tiene `.git` y no contiene la rama del gate, conforme a
`O27` §4.

#### 0.2 bis · `O27` §4 · el manifiesto NO está dentro del objeto auditado — **SOSTENIDO**

Es uno de los ataques que el manifiesto §8 reparte a «LOS TRES».

```console
$ ls CANDIDATA/docs/f6/gate-definitivo/
ls: cannot access 'CANDIDATA/docs/f6/gate-definitivo/': No such file or directory
$ ls -d CANDIDATA/.git
ls: cannot access 'CANDIDATA/.git': No such file or directory
$ git -C CLONF ls-tree -r --name-only HEAD | grep -c gate-definitivo
0
```

El commit candidato `2ae0a93…` **no contiene** ni el manifiesto ni ningún documento de este
gate: `docs/f6/` termina en `04-MATRIZ-DE-HALLAZGOS-DEL-GATE-20260904.md`. `O27` §4 se
cumple, y con ello queda cerrado `ADJ-GT1` —«el acto de convocar el gate cambió el corpus que
dos instrumentos del gate miden»—: los dos instrumentos miden hoy el SHA candidato y sólo él.

#### 0.3 · COBERTURA · `ASIGNADO − LEÍDO = ∅` y `LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS = ∅`

**Mi lote está CERRADO.** Manifiesto de lectura en `lectura-REV-3.json`, con los tramos
reales que abrí, y comprobado con el instrumento del propio árbol:

```console
$ python3.12 CANDIDATA/docs/evolucion/verificacion/comprobar-cobertura-de-gate.py \
    --manifiesto /home/jose/ads-kernel/docs/f6/gate-definitivo/MANIFIESTO-ASIGNACION.json \
    --lectura lectura-REV-3.json --raiz CANDIDATA

COBERTURA DEL GATE · candidata 2ae0a93888a425cf85ba38d0ac054d069bbbe7d6
==============================================================================
  REV-3    asignadas  77 · leídas sin hueco  77 · sin abrir   0 · con huecos   0
           líneas asignadas  46649 · sin leer      0 · cerrado declarado: sí

LAS CUATRO RESTAS
------------------------------------------------------------------------------
  OBLIGATORIO − ASIGNADO                 ∅
  ASIGNADO − LEÍDO                       ∅
  LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS       ∅
  FUENTES MODIFICADAS − LEÍDAS ÍNTEGRAS  170          ← de los lotes de REV-1 y REV-2
  SIN MANIFIESTO DE LECTURA: REV-1, REV-2
  COBERTURA INCOMPLETA
```

**Las dos restas que son mías están a CERO.** La `COBERTURA INCOMPLETA` global y la cuarta
resta se deben a que REV-1 y REV-2 aún no han entregado su manifiesto de lectura; no son
mías y no las declaro por ellos.

**Y hay que decir aquí, en la primera página, lo que el gate necesita saber antes que nada:
con el manifiesto tal como está commiteado, `COBERTURA COMPLETA` es INALCANZABLE para
cualquier conjunto de manifiestos de lectura.** El rango `[11907, 12153]` asignado a REV-2
excede el fichero, y el comprobador tiene las dos puertas cerradas. Está medido en
`HALLAZGO 0`.

**Y una discrepancia que hay que decir aquí, porque es del aparato y no mía:** el manifiesto
declara **47 534** líneas para REV-3 y el comprobador cuenta **46 649**. La diferencia son
**885 líneas** = los rangos `[7378, 8074]` (697) y `[10882, 11069]` (188) de `11-ARQ`, que el
comprobador **pierde**. Los leí igual, y están en mi manifiesto de lectura. La causa es
`HALLAZGO 1`, abajo.

---

### 1 · LA LÍNEA BASE, REPRODUCIDA

Sobre una copia limpia del checkout congelado (`REPRO-R3b`), con el intérprete prescrito:

```console
$ python3.12 kernel/operativo/validadores/registrar_evidencia.py
…
36/36 validadores en verde · 36 evidencias publicadas · 0 problemas
EXIT=0

$ tail -1 kernel/operativo/pruebas/evidencia/negativos-salida.txt
158 infracciones detectadas · 0 NO detectadas

$ python3.12 kernel/operativo/validadores/registro_pruebas.py | tail -2
contraste del estado: 195 contrastados · 72 no contrastables · 0 divergencias
no contrastables por estado declarado: contrato-definido 56 · prueba-ejecutada 12 · validador-implementado 4

$ python3.12 docs/evolucion/verificacion/derivar-universo-obligatorio.py --obligaciones
  (§19   )   5   ·  (F-nn  )   8  ·  (V6    )  19  ·  (g     )  16  ·  (C     )   3  ·  (deuda )   7
  TOTAL 58 obligaciones
  A · sin COBERTURA DECLARADA … 0
  B · con cobertura y SIN NI UN SABOTAJE … 0
  C · con cobertura y SIN FICHERO DE EVIDENCIA … 0

$ python3.12 docs/evolucion/verificacion/derivar-universo-obligatorio.py --autopruebas | tail -1
  12 sabotajes · 0 sin detectar

$ cat kernel/.upstream-hash
7196ce99457a77d4
```

**La línea base se reproduce ENTERA.** 36/36 · 36 evidencias · 0 problemas · 158 detectadas y
0 no detectadas · 195/72/0 · universo 58 con A=B=C=0 · 12 sabotajes del derivador sin fallo ·
huella `7196ce99457a77d4`.

#### 1.1 · Con una salvedad medida, y la digo porque la línea base declara «determinismo»

Mi **primera** corrida del runner, con otras DOS corridas del mismo runner en la misma
máquina, dio:

```console
35/36 validadores en verde · 35 evidencias publicadas · 1 problemas
FALLO  contencion  código 1  NO publicada
  └─ test_con_el_backend_simple_el_bisnieto_SI_escapa (T216)
```

La MISMA batería, aislada y sobre copia limpia: `Ran 20 tests · OK · EXIT=0`. La prueba que
se cae es la que EXIGE que el bisnieto **sobreviva** a `killpg`; bajo carga el bisnieto puede
no llegar a existir a tiempo y el resultado se lee como fallo. **Falla al lado seguro** —rojo,
no verde— pero **no es determinista**, y la línea base dice «determinismo byte a byte».
Queda como `HALLAZGO 9`.

---

### 2 · LOS OCHO ATAQUES

#### ATAQUE 1 · Borrar `O20`–`O27` y fabricar una certificación · **ROJO, pero incompleto**

Clon real (`git clone --no-local`) del commit candidato. Se recorta la sede desde `O20` y se
sustituye por `# \`O20\` · CERTIFICACION … F6 QUEDA CERTIFICADA SIN CONDICIONES.`, se
confirma, `git status --porcelain` queda **vacío**.

```console
$ python3.12 kernel/operativo/runtime/ads_admision.py --repo . verificar --base <candidata>
  (CONTROL SANO) veredicto INDETERMINADO · hallazgos 0
  (ATAQUE)       veredicto ROJO           · hallazgos 1     EXIT=1
  V6-12  SEDE_DEL_OWNER_ALTERADA  docs/owner/ADS-OWNER-RESOLUCIONES.md
    ALTERACIÓN DE ENTRADAS CERRADAS [ENTRADA_ALTERADA] la entrada `O20` no coincide BYTE A
    BYTE con la que se introdujo en el commit 7aeed6aa3a3e (5220 bytes → 110 bytes) …
    (y 8 más: ENTRADA_ALTERADA, ENTRADA_BORRADA)
```

**El ataque se para.** La sede pierde de 43 476 a 14 174 bytes y el verificador lo caza.
**Lo que NO cumple es la exigencia de nombrar CADA una:** de las nueve infracciones el
diagnóstico publica UNA y agrega las demás en un recuento y un conjunto de códigos → `HALLAZGO 5`.

#### ATAQUE 2 · Un byte en CADA resolución cerrada `O17`…`O27` · **LAS ONCE EN ROJO**

Once clones independientes; un byte mutado dentro de cada entrada; confirmado.

```text
O17 rc=1 ROJO 1 hallazgo | ENTRADA_ALTERADA `O17` … commit 1d3b5d41434b (3716 bytes →
O18 rc=1 ROJO 1 hallazgo | ENTRADA_ALTERADA `O18` … commit 1d3b5d41434b (4712 bytes →
O19 rc=1 ROJO 1 hallazgo | ENTRADA_ALTERADA `O19` … commit 1d3b5d41434b (3118 bytes →
O20 rc=1 ROJO 1 hallazgo | ENTRADA_ALTERADA `O20` … commit 7aeed6aa3a3e (5220 bytes →
O21 rc=1 ROJO 1 hallazgo | ENTRADA_ALTERADA `O21` … commit 07a6975ec214 (4571 bytes →
O22 rc=1 ROJO 1 hallazgo | ENTRADA_ALTERADA `O22` … commit 196de0368f89 (5069 bytes →
O23 rc=1 ROJO 1 hallazgo | ENTRADA_ALTERADA `O23` … commit 517c38fcece7 (5184 bytes →
O24 rc=1 ROJO 1 hallazgo | ENTRADA_ALTERADA `O24` … commit 99b06d3625b7 (2038 bytes →
O25 rc=1 ROJO 1 hallazgo | ENTRADA_ALTERADA `O25` … commit 0e57f706c27d (2345 bytes →
O26 rc=1 ROJO 1 hallazgo | ENTRADA_ALTERADA `O26` … commit 6db4605b7f67 (3317 bytes →
O27 rc=1 ROJO 1 hallazgo | ENTRADA_ALTERADA `O27` … commit c46c468a2cf3 (2246 bytes →
```

Cada una nombra la entrada **y el commit que la introdujo**. Control sano sobre el mismo
clon: `INDETERMINADO · hallazgos 0`. **`ADJ-B3` está cerrado por su propiedad, no por su
instancia.** Es lo más sólido que he medido en todo el árbol.

#### ATAQUE 3 · El apéndice legítimo · **SE PERMITE**, y las siete formas defectuosas dan ROJO por su motivo

El delimitador estructural de la sede es `b"\n---\n\n"` (`admision/sede.py` L111).

```text
legitimo     rc=1  veredicto INDETERMINADO · SIN hallazgo de `V6-12`      ← PERMITIDO
sin_campos   rc=1  ROJO ENTRADA_INCOMPLETA   «no declara `**Fecha:**`, y la forma quedó
                                              establecida en `O23`»
solo_titulo  rc=1  ROJO ENTRADA_INCOMPLETA   «no tiene cuerpo: es un título sin resolución»
salto        rc=1  ROJO SALTO_DE_NUMERACION  «después de `O27` la sede publica `O30`»
familia      rc=1  ROJO FAMILIA_DESCONOCIDA  «la entrada `Z1` pertenece a la familia `Z`»
duplicado    rc=1  ROJO ENTRADA_DUPLICADA    «DOS entradas con el identificador `O27`
                                              (posiciones 11 y 12)»
enmedio      rc=1  ROJO ENTRADAS_REORDENADAS con la secuencia hallada frente a la del libro
borra_ultima rc=1  ROJO ENTRADA_BORRADA      «`O27`, introducida en el commit c46c468a2cf3
                                              … ya no está»
metadatos    rc=1  ROJO ENTRADA_ALTERADA     cambiar SÓLO la fecha de `O27` da rojo
```

**El guardián NO impide el acto que la sede existe para permitir**, que era la mitad del
ataque que importaba tanto como la otra. Y consta contra mi primera medición: un apéndice
**sin** el delimitador da `ESTRUCTURA_ILEGIBLE`, y eso es CORRECTO —el delimitador es forma
declarada de la sede—, no un falso rojo. Rectifico mi propia medición inicial.

#### ATAQUE 4 · Encoger el universo obligatorio · **VÍA NUEVA ENCONTRADA · 58 → 57 con EXIT=0**

Las TRES vías conocidas (`ADJ-G1`) están cerradas: el cliquet las caza y NOMBRA quién ejerce
la obligación que se cae. Lo comprobé con controles:

```console
(1) sólo cambiar la fase / retirar la fila / retirar el bloque  → EXIT=2 · FALLA CERRADO
```

**La vía nueva.** `obligaciones_de_19()` lee el cuerpo de cada contrato con
`cuerpo = trozos[i + 1][:4000]` —**sólo los primeros 4000 caracteres**—, y `_seccion_19()`,
cuyo docstring dice «El cuerpo de §19, acotado por sus dos cabeceras», hace `return texto`:
**devuelve el fichero entero**. El criterio publicado —«por FASE declarada en el bloque del
contrato»— no es lo que ejecuta.

RECETA, cuatro ficheros y NINGUNA retirada de bloque:

```text
1  `11-ARQ` §19 · insertar ~5 KB de prosa DESPUÉS de la cabecera
   `--- CONTRATO 2 · AMPLIAR `T152` … ---`, de modo que su `FASE **F6**` caiga fuera de la
   ventana de 4000. NO se retira nada: la consecutividad {1, 2, 3} queda intacta
2  `T270-T289-…md`     · quitar `CONTRATO 2` de los `cubre`
3  `REGISTRO-generado.md` · idem (es derivado y se regenera solo)
4  `negativos_contratos19.py` · retirar las dos `Mutacion` `N272` y `N272b`
```

```console
$ python3.12 docs/evolucion/verificacion/derivar-universo-obligatorio.py --obligaciones
  (§19   )   4   las obligaciones de fase F6 de `11-ARQ` §19
  TOTAL 57 obligaciones                                                        EXIT=0
  A · sin COBERTURA DECLARADA … 0
  B · con cobertura y SIN NI UN SABOTAJE … 0
  C · con cobertura y SIN FICHERO DE EVIDENCIA … 0
$ python3.12 …/derivar-universo-obligatorio.py --autopruebas | tail -1
  12 sabotajes · 0 sin detectar
$ comprobar_versiones · comprobar_recuentos · comprobar_evidencia · comprobar_contratos
  EXIT=0 · EXIT=0 · EXIT=0 · EXIT=0
```

`CONTRATO 2` desaparece del universo y **nada lo dice** — que es literalmente el `falla_si`
de `T351`: «el modo obligaciones publica un total menor sin decir qué ha perdido».

CONTROLES, y son los que dan valor al hallazgo:

```text
sólo el paso 1                     → EXIT=2 · el cliquet NOMBRA a N272, N272b, T272, T277
pasos 1+2+3                        → EXIT=2 · sigue nombrando N272, N272b
reimputar los sabotajes a `CONTRATO 9` → EXIT=2 · el cliquet no se engaña renombrando
```

El cliquet es sólido; lo que NO protege es el **tamaño** del universo. → `HALLAZGO 2`.

#### ATAQUE 4 bis · EL CRITERIO de las tres restas, juzgado y no sólo su cifra

**¿`A=0` demuestra `O26` §5.1 —«no quedan obligaciones internas sin implementar»?— NO.**
El propio derivador lo escribe pegado a la cifra, y eso es un mérito. Pero hay un
**contraejemplo VIVO en mi eje**, y lo aporto porque una advertencia sin instancia no obliga
a nadie: `01-MATRIZ` L195-200 declara para `CONTRATO 3` una **divergencia con su contrato**
—§19 le prescribe el código de salida **2** y la implementación usa **78**—, y `CONTRATO 3`
cuenta como CUBIERTO en `A` porque `T158` y `T350` lo nombran en un `cubre:`. Una obligación
cuya cláusula de cierre literal NO se cumple sale de la resta como si se cumpliera.

**¿`B=0` demuestra `O26` §5.2 —«no quedan propiedades críticas sin una prueba capaz de
fallar»?— NO.** `B` mide que exista AL MENOS UN sabotaje imputado a la obligación, no que sus
propiedades estén cubiertas una a una. `V6-12` tenía `B=0` mientras el append-only más allá
del prefijo del nacimiento no tenía sabotaje ninguno; eso es `ADJ-B3`, y hoy está cerrado —
pero el predicado que lo dejó pasar **sigue siendo el mismo**.

**¿`C=0`?** Mide que exista un fichero de evidencia enlazado y presente. No mide vigencia.

**Y la conclusión que importa para `O26` §5:** con la vía nueva del ataque 4, **las tres
restas siguen a cero sobre un universo mutilado**. Una resta vacía sobre 57 obligaciones no
distingue el árbol sano del atacado, de modo que su vacío **no acredita lo que `O26` §5 le
pide acreditar**.

#### ATAQUE 5 · Estado de escenario contradictorio · **ROJO POR EL MOTIVO ESPERADO**

Verificado primero el estado sano: `195 contrastados · 72 no contrastables · 0 divergencias`,
y el desglose de los 72 —`contrato-definido 56 · prueba-ejecutada 12 · validador-implementado
4`—: **ninguno es `prueba-superada`**, que es la pregunta que había que hacer.

Sabotaje: `T100` —`ejecucion: guion-manual`, sin evidencia— sube de `contrato-definido` a
`prueba-superada`.

```console
$ python3.12 kernel/operativo/validadores/comprobar_evidencia.py            EXIT=1
T350  FALLIDA   El estado declarado de cada escenario lo sostiene su evidencia
  · T100: declara `estado: prueba-superada` y su evidencia sostiene `contrato-definido`
    — declara `prueba-superada` sobre una evidencia que NO lo nombra … eso es subir de
    estado por argumento, y la regla dura de `REGISTRO.md` lo prohíbe con o sin contraste
  · T100: declara `prueba-superada` y no declara `evidencia`
  cobertura del contraste: contrastados 195 · no contrastables 72 · divergencias 1 ·
  no contrastables por estado declarado: … prueba-superada 1 …
```

Restaurado → verde. **`ADJ-G2` está cerrado por su propiedad.**

**¿Son los 72 un límite honesto o una frontera cómoda?** Honesto, y por una razón mecánica:
un `prueba-superada` **no puede esconderse** entre los no contrastables —lo demuestra el
sabotaje de arriba, que lo caza y lo nombra— y `H-02` BAJÓ catorce escenarios de
`prueba-superada` a `prueba-ejecutada` cuando midió que su evidencia no los nombraba, contra
el propio interés del corpus. Un aparato que baja catorce estados por su cuenta no está
escondiendo nada en esa bolsa.

**Con un defecto, y es de cifra:** `T340-T359-append-only-y-universo.md` L57-58 publica «el
contraste del estado tiene COBERTURA publicada: **161** escenarios lo tienen y **92** no»
mientras la evidencia del mismo árbol dice **195 · 72 · 0**. Es el documento que cierra
`ADJ-G2`. → `HALLAZGO 6`.

#### ATAQUE 6 · Una obligación borrada de la matriz · **la matriz REMITE, y eso la salva**

Medido: **ningún validador contrasta `01-MATRIZ-DE-COMPLETITUD-F6.md` contra el universo
derivado**. La matriz no lo necesita porque **no publica el universo: remite al comando**
(§2.6, §0). Ésa es la disciplina correcta y hay que decirla.

Su §2.5 enumera **CUATRO** obligaciones de §19 y el derivador publica **CINCO**. La quinta,
`CONTRATO 3`, queda fuera **con su motivo escrito** —es `F6-I`, L195-203—, luego no es una
omisión silenciosa. Lo acepto como frontera dicha.

Lo que sí está caducado: esa misma nota afirma «**ningún escenario nombra `CONTRATO 3` en su
`cubre`**, de modo que el derivador lo publica en la resta **A**». Medido: `T158` y `T350` lo
nombran, y `A = 0`. Falsa por los dos extremos. → `HALLAZGO 8`.

#### ATAQUE 7 · `O27` · **SOSTENIDO EN LOS CUATRO PUNTOS**

```text
LITERAL              la entrada reproduce §1…§6 con `**Fecha:** 2026-09-04` y
                     `**Autoridad:** Owner`. Su §6 dice de sí misma: «no certifica F6 · no
                     corrige por sí misma ningún hallazgo técnico · NO DECLARA SATISFECHO B3
                     · no inicia PesquerApp · no rebaja ninguna obligación»
APPEND-ONLY          demostrado entrada a entrada por el ATAQUE 2 contra el commit que
                     introdujo cada una. `O17`–`O26` intactas (control sano: hallazgos 0)
NO ES CERTIFICACIÓN  barrido sobre `docs/` y `kernel/`: ninguna sede la presenta como tal.
                     `D116` escribe «**`O27` NO CERTIFICA NADA.** Lo dice de sí misma en su
                     §6, y esta fila tampoco»
`B3` NO SATISFECHO   `06-DEUDA` §3: «**`B3` NO queda satisfecho por este acto**».
                     `01-MATRIZ` `F6-B`: «**No se declara satisfecho `B3`**, y `O26` **no se
                     presenta como certificación**»
```

**Y rectifico un hallazgo mío.** Escribí, apoyándome en el `FALLO G-21` de la batería del
corpus, que `O23`…`O27` «no están proyectadas al registro». **Es falso y lo retiro.** La
proyección existe con otra FORMA: `D112` (`O23`), `D113` (`O24`), `D114` (`O25`), `D115`
(`O26`) y `D116` (`O27`), cada una declarada DERIVADA, con su fuente única y con el `awk` que
extrae el literal de la sede. `O19` §3 y §4 quedan satisfechas en sustancia. `G-21` exige la
forma antigua `### \`Onn\``, que dejó de usarse desde `O23`: **ese rojo es del instrumento,
no del candidato.** Lo que sí queda es que `D112` no abre epígrafe propio → `HALLAZGO 7`.

#### ATAQUE 8 · Las sedes de ESTADO

**`03-GOBIERNO-Y-AUTORIDAD.md` §6 · CORRECTO.** Contrastado línea a línea contra `O24` y
contra el manifiesto:

```text
F4c CERRADA por composición · F5 CERRADA (O24 §1) · F6 INICIADA · EN CURSO (O24 §2)
PesquerApp BLOQUEADA (O20 §8, O24 §4) · C-L.5 CERTIFICADA/POR DELTA · C-L.7 NO CERRADA
M-04 NO SUPERADA
```

Y `03-GOBIERNO` §6 **no copia** el estado de construcción: remite a `04-CONTRATOS` §1.

**`04-CONTRATOS-TECNICOS.md` · barrido entero, y hoy NO reincide.** El remedio de `ADJ-G3`
está mecanizado en `T360`, que contrasta cada negación de existencia declarada contra una
SONDA en el disco. Lo verifiqué con su matriz:

```console
$ printf '\n\nNo existe ningun verificador de admision.\n' >> docs/canonico/04-CONTRATOS-TECNICOS.md
$ python3.12 kernel/operativo/validadores/comprobar_recuentos.py            EXIT=1
T360  FALLIDA   Ninguna sede viva niega una pieza que el árbol tiene construida
  · docs/canonico/04-CONTRATOS-TECNICOS.md:516: «No existe ningun» dicho de «verificador de
    admisión», que SÍ está construida — el paquete `runtime/admision/` … O se remite a
    `04-CONTRATOS-TECNICOS.md` §1, o se restringe la afirmación (`ADJ-G3`)
```

**Pero el barrido tiene una frontera que no aguanta el examen, y es el hallazgo central de
este dictamen.** Ver `HALLAZGO 1`.

---

### 3 · EL ATAQUE QUE MÁS IMPORTA · ¿SE HA RECLASIFICADO ALGUNA DEUDA INTERNA?

Busqué deuda interna convertida en «externa», «límite de anfitrión», «frontera declarada»,
«no contrastable» o «deuda acotada» para no tener que cerrarla. **He encontrado UNA
reclasificación, y no es de una deuda: es de una SEDE.** Las cinco cosas que el commit declara
abiertas las juzgo una a una abajo, y **cuatro de las cinco son límites honestos**.

#### 3.1 · LA RECLASIFICACIÓN · `docs/evolucion/` rotulado «historia inmutable»

El remedio de `ADJ-M5` ordenaba motivar cada mitad de la frontera del barrido de sedes vivas.
Se hizo, y el motivo escrito para `^docs/evolucion/` es:

> «historia del kernel y actas de los gates anteriores: son **INMUTABLES por el registro
> canónico** y describen el árbol del día en que se escribieron»

**Las dos mitades del motivo son falsas para el fichero que importa.**

```text
NO ES INMUTABLE   `G-22` de la batería del propio corpus declara a
                  `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **EXENTO y NOMBRADO**, «por
                  ser el objeto declarado de esta tanda», y su último commit es
                  `517c38f feat(f5): …`. Se edita
NO ES HISTORIA    es la SEDE de la que el derivador saca §19 (5 obligaciones), F-nn (8) y
                  V6 (19) = **32 de las 58** del universo obligatorio de `F6`, con digest
                  `616044e4827b18dc`
```

**Y contiene HOY, en presente, una negación falsa de la clase exacta de `ADJ-G3`:**

```text
L11236  «`kernel/operativo/` devuelve **cero instancias de `:revision`**»
L11406  «**CINCO procesos y NUEVE pares, los NUEVE AUSENTES** —hay cero instancias de
         `:revision` en todo `kernel/operativo/`—»
```

Medido sobre el checkout congelado:

```console
$ grep -rno "\(DOM\|SEG\):revision" kernel/operativo/recorrido/01-PROCESOS.md | wc -l
9
$ python3.12 kernel/operativo/validadores/comprobar_composicion_procesos.py --catalogo
5 procesos · 9 pares      (los NUEVE, PRESENTES)
$ tail -3 kernel/operativo/pruebas/evidencia/composicion-procesos-salida.txt
T273  SUPERADA  Todo par del catálogo estático de D104 tiene su <CAP>:revision
```

`T273` certifica exactamente lo contrario de lo que §19 publica. **Y el barrido que existe
para cazar esto no llega**, porque la zona está rotulada como historia:

```console
   A · «No existe ningun verificador de admision.» → docs/canonico/04-CONTRATOS-TECNICOS.md
       T360 FALLIDA · EXIT=1 · nombra fichero, línea, pieza y sonda        ROJO CORRECTO
   B · LA MISMA FRASE            → docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
       T360 SUPERADA · EXIT=0 · «7 superadas · 0 fallidas»                 VERDE
```

**La misma frase, la misma pieza, dos veredictos según el directorio.** El remedio adjudicado
de `ADJ-G3` decía «BARRIDO DE CLASE sobre todo el documento **y las demás sedes vivas**»; la
sede más viva del expediente quedó fuera, rotulada como historia inmutable, en el mismo
commit que cerraba el hallazgo. **Eso es una reclasificación, y es GRAVE.** → `HALLAZGO 1`.

#### 3.2 · Las cinco que el commit declara abiertas, juzgadas una a una

**(1) Las 22 baterías sin el prólogo `E-10` — NO es un límite honesto. Es un agujero medido.**

`inventariar_el_arbol()` recorre el árbol entero y clasifica todo `.py`; las zonas de
baterías se excluyen con `motivo: "bateria"`. Medido: **21 ficheros** sin la purga, entre
ellos los tres escenarios extremo a extremo y diecisiete baterías del runtime.

```console
$ cd /tmp && python3.12 <copia>/…/pruebas/test_admision.py
  Ran 94 tests · OK · EXIT=0                                          (CONTROL SANO)
$ cd /tmp && TESTIGO=… PYTHONPATH=<veneno con `json.py` homónimo> python3.12 …/test_admision.py
  Ran 94 tests · OK · EXIT=0
$ cat /tmp/testigo-veneno.txt
  el homonimo ENTRO
```

**El módulo del atacante se importa dentro del proceso de la batería y la batería publica su
verde.** Y no lo salva el runner: `registrar_evidencia.py` purga su propio `sys.path` pero
lanza a sus hijos con `subprocess.run([sys.executable, script, *ej.args], cwd=base, ...)`
**sin `env=`**, de modo que el `PYTHONPATH` del lanzador llega intacto a los 36 validadores.
`E-10` está cerrada para los nueve puntos ejecutables y **abierta para el canal que produce
TODA la evidencia**. → `HALLAZGO 3`.

**(2) Los nueve escenarios que sólo suben reescribiendo baterías ajenas — LÍMITE HONESTO.**
Son los `prueba-ejecutada` de `H-02`. El corpus los BAJÓ por su cuenta cuando midió que su
evidencia no los nombraba, y la regla que lo gobierna —«un `estado` superior al derivado es
DIVERGENCIA se pueda contrastar o no»— está mecanizada y la puse a prueba (ataque 5). Subir
uno exige que la salida lo NOMBRE. No hay alibi aquí.

**(3) La clase `AUTORIDAD_SUPERIOR` mezclando dos regímenes — LÍMITE HONESTO, con mecanismo.**
Medido en `FUENTES-CANONICAS.yml`: la clase contiene a la vez la sede del Owner
(«APPEND-ONLY») y las especificaciones aprobadas («se cambia por enmienda») y
`kernel/KERNEL.md` («constitución en prosa»). Dos regímenes, una clase. **Pero la
consecuencia está cerrada por otro sitio:** `admision/sede.py` decide el régimen desde la
**HISTORIA** de la ruta y no desde la clase, y el veredicto **publica cuál aplicó**
(`T340`). Partir la clase toca el registro canónico, que no es sede de este eje, y queda como
petición escrita. Lo acepto.

**(4) La frontera del componente `C` sin sede — LÍMITE HONESTO, y de los mejores.** El
derivador publica, pegado a la cifra, su propio criterio: «SELECCIÓN ESCRITA `C2`, `C4`, `C5`
— **sin sede que la derive (PETICIÓN abierta)**; los otros cuatro contratos del directorio se
publican como excluidos». Una frontera que se rotula por lo que es —una selección escrita— y
publica lo que deja fuera no es un alibi: es exactamente lo contrario.

**(5) El canal de evidencia sin sabotaje mecanizado — NO es un límite honesto.** Es el
mismo agujero que (1), y su consecuencia es que la línea base entera —36/36, 158/0, 195/72/0—
la producen procesos cuyo `sys.path` controla quien lance el runner. → `HALLAZGO 3`.

#### 3.3 · Lo que NO es reclasificación, y lo digo contra mi propio ataque

**`E-17` y `E-18` NO se han reclasificado.** `E-17` (custodia productiva de claves) está
registrada con propietario —el Owner, `O25` §3—, mecanismo previsto, condición de cierre y la
declaración expresa de que una clave efímera `0600` fuera de los repositorios **NO** la
satisface; `T309` barre que ninguna salida de la zona afirme custodia productiva. `E-18`
(`cgroup v2` presente y no ejercitable aquí) se declara con su `errno 5 (EIO)`, con los
backends que SÍ se ejercen y con la cláusula «la certificación queda LIMITADA AL BACKEND
EJERCIDO. Este corpus no afirma nada sobre anfitriones que no ha medido». Las dos son
externas de verdad y ninguna bloquea lo que dice no bloquear.

**Y una reclasificación HACIA DENTRO, que hay que decir a favor:** `F6-B` retiró el rótulo
«límite de anfitrión» y lo sustituyó por «ACTO DEL OWNER EMITIDO Y CONDICIONADO». Eso es
mover una deuda de fuera hacia dentro, y es correcto.

**Lo que sí es una frontera declarada que no imputo:** `docs/rediseno/` queda fuera del
barrido con motivo real —material APROBADO, sólo `F5` puede editarlo, `O24` §5 prohíbe
reabrirlo— y ahí viven dos negaciones falsas: `g.17` («Ninguno existe, ninguno está
implementado») y `DECISIONES` §4 («sigue sin haber runtime»). **No lo imputo** porque la
frontera tiene motivo verdadero y porque `00-ESTADO-DE-IMPLEMENTACION-F6.md` es la sede única
que sí lo dice bien. Lo separo de `HALLAZGO 1` precisamente porque allí no se da ninguna de
las dos cosas.

---

### 4 · HALLAZGOS

`severidad · sede · reproducción · remedio · propietario · fase · clase`

#### `HALLAZGO 0` · **BLOQUEANTE · del APARATO DEL GATE** — el manifiesto hace INALCANZABLE la cobertura

**Sede:** `docs/f6/gate-definitivo/MANIFIESTO-ASIGNACION.json` (§7 y su `.md`), rango de
`11-ARQ` asignado a REV-2.

**Hecho.** `11-ARQUITECTURA-INTEGRADA.md` tiene **12 152** líneas. El manifiesto asigna a
REV-2 el rango **`[11907, 12153]`**, que excede el fichero en una línea. El comprobador de
cobertura —el instrumento que `O27` §5 convierte en norma— tiene las dos puertas cerradas:

```console
(a) REV-2 declara el tramo 11907-12152
    REV-2  asignadas 104 · con huecos 1
    LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS       1
       REV-2 · docs/evolucion/11-ARQUITECTURA-INTEGRADA.md · faltan 1 líneas en 12153-12153
    COBERTURA INCOMPLETA

(b) REV-2 declara el tramo 11907-12153
    NO SE PUDO COMPROBAR · `REV-2` declara el tramo 11907-12153 sobre
    `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, que tiene 12152 líneas: un tramo fuera
    del fichero no describe ninguna lectura
```

**Haga lo que haga REV-2, `COBERTURA COMPLETA` es inalcanzable.** Y el manifiesto §4 lo
convierte en bloqueo del gate con sus propias palabras: «**Devuelve 0 sólo si las cuatro son
vacías, y NO SE CREA AL ADJUDICADOR mientras no devuelva 0 para los tres revisores.**» El
rango está escrito también en el `.md`, L198: `§20   L11907 -L12153      247 líneas`. Y además: las líneas
**1–94** de `11-ARQ` no están asignadas a nadie —los rangos de los tres revisores empiezan en
95—, de modo que 94 líneas de la sede de 32 obligaciones quedan sin lector.

**Remedio:** corregir el rango a `[11907, 12152]` y asignar `[1, 94]`, publicando un
manifiesto NUEVO con su motivo, sin editar el anterior —que es la disciplina que este mismo
expediente escribió con los manifiestos `4B` y `6B`—.
**Propietario:** el coordinador que dimensionó y repartió. **Fase:** el método del gate.
**Clase:** DEL APARATO DEL GATE.

#### `HALLAZGO 1` · **GRAVE · INTERNO** — la sede de 32 obligaciones, rotulada «historia inmutable»

**Sede:** `kernel/operativo/validadores/comprobar_recuentos.py`, `ZONAS_SIN_BARRIDO`, patrón
`^docs/evolucion/` · y `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` L11236 y L11406-11408.

**Reproducción:** §3.1 de este dictamen, con su matriz completa —la misma negación da ROJO en
`docs/canonico/` y VERDE en `docs/evolucion/`— y con la medición de las nueve instancias de
`:revision` que §19 declara ausentes y `T273` certifica presentes.

**Remedio:** el motivo del patrón `^docs/evolucion/` es falso para `11-ARQ` en sus dos
mitades. O se PARTE la zona —`11-ARQ`, el registro y el checkpoint son sedes VIVAS; los
documentos numerados de los gates son historia— y las vivas entran en `AMBITO_VIVO`, o se
corrige §19 para que deje de afirmar en presente un hecho que su propia fase ha cambiado. **Lo
primero cierra la clase; lo segundo, la instancia.** Y la prueba posterior está escrita en el
propio corpus: la de `T360`, aplicada a esa zona.
**Propietario:** `PLT` implementa · `SIS` propietario. **Fase:** `F6`. **Clase:** INTERNO.

#### `HALLAZGO 2` · **GRAVE · INTERNO** — vía nueva de encogimiento silencioso del universo

**Sede:** `docs/evolucion/verificacion/derivar-universo-obligatorio.py`, `_seccion_19()` y
`obligaciones_de_19()` (`cuerpo = trozos[i + 1][:4000]`).
**Reproducción:** ATAQUE 4, con sus tres controles. `TOTAL 57 · EXIT=0 · A=B=C=0`.
**Remedio:** acotar `_seccion_19()` de verdad a §19 —hoy hace `return texto`—, leer el cuerpo
ENTERO de cada contrato, y **publicar el DELTA del universo contra la corrida anterior**, no
sólo el total. La primera mitad cierra esta vía; la segunda cierra la clase.
**Propietario:** `PLT`. **Fase:** `F6`. **Clase:** INTERNO.

#### `HALLAZGO 3` · **GRAVE · INTERNO** — `E-10` no alcanza al canal que produce la evidencia

**Sede:** `kernel/operativo/runtime/pruebas/*.py` (21 ficheros sin la purga) ·
`test_integridad_y_evidencia.py::inventariar_el_arbol()` (exclusión `motivo: "bateria"`) ·
`kernel/operativo/validadores/registrar_evidencia.py` L212 (`subprocess.run` sin `env=`).
**Reproducción:** §3.2 (1), con control sano y con el testigo del homónimo en disco.
**Remedio:** o el prólogo `E-10` entra en las baterías —y la equivalencia de tres términos de
`T330` deja de eximirlas por su zona—, o el runner sanea el entorno de sus hijos
(`env` sin `PYTHONPATH`) y lo publica en la cabecera de cada evidencia. **Lo segundo cierra
las 21 de una vez y es más barato; lo primero cierra también la ejecución suelta.**
**Propietario:** `PLT` implementa · autoría de `F6`. **Fase:** `F6`. **Clase:** INTERNO.

#### `HALLAZGO 4` · **GRAVE · del APARATO DEL GATE** — el comprobador de cobertura COLAPSA los rangos múltiples

**Sede:** `docs/evolucion/verificacion/comprobar-cobertura-de-gate.py` L205 y L267:
`asignadas = {f["ruta"]: f for f in lote.get("fuentes") or []}`.

**Hecho.** Una fuente asignada por VARIOS rangos se colapsa a UNA clave y **sólo se comprueba
el último**. REV-1 tiene 75 asignaciones y 68 rutas únicas: **siete de sus ocho rangos de
`11-ARQ` nunca se miden**, incluido §2 (`[396, 3794]`, 3 399 líneas) y §8
(`[6285, 7377]`, 1 093 líneas): de sus 5 737 líneas de `11-ARQ` sólo se miden las 29 del
último rango.

**Reproducción.** Un `lectura-REV-1` que declara ÚNICAMENTE el último rango —29 de las 5 737
líneas de `11-ARQ` que tiene asignadas— y el resto de sus ficheros enteros:

```console
$ comprobar-cobertura-de-gate.py --manifiesto <el del gate> \
    --lectura lectura-REV-3.json lectura-REV-1-FALSA.json --raiz CANDIDATA
  REV-1    asignadas  68 · leídas sin hueco  68 · sin abrir   0 · con huecos   0
           líneas asignadas  34922 · sin leer      0 · cerrado declarado: sí
  ASIGNADO − LEÍDO                       ∅
  LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS       ∅
```

Y la misma pérdida se ve en mi propia fila: el manifiesto me asigna 47 534 líneas y el
comprobador cuenta 46 649 — las 885 de mis dos primeros rangos.

**Remedio:** indexar por `(ruta, rango)` y no por `ruta`, y contrastar el total de líneas
publicado por el manifiesto contra el derivado, que es lo que habría delatado esto solo.
**Propietario:** `PLT`. **Fase:** `F6`. **Clase:** INTERNO / DEL APARATO DEL GATE.

#### `HALLAZGO 5` · **GRAVE · INTERNO** — el SUELO del universo del gate no se deriva: se declara

**Sede:** `comprobar-cobertura-de-gate.py` L220-239 y su bloque `DECISIÓN · OBLIGATORIO se
DERIVA DEL ÁRBOL`.

**Hecho.** El bloque de decisión dice «Se elige (c) … el suelo lo pone el árbol: **toda
fuente MODIFICADA entre la base y la candidata es obligatoria**, la declaración puede añadir,
y ninguna de las dos puede quitar». El código hace
`derivado = set(manifiesto.get("modificadas") or [])`: **ni una llamada a `git`**. `H-06`
cerró el caso VACÍO, no el INFRA-DECLARADO.

**Reproducción:**

```console
manifiesto: {"modificadas": ["kernel/VERSION"],
             "revisores": {"REV-X": {"fuentes": [kernel/VERSION]}}}
lectura   : REV-X, cerrado, tramos [[1,1]]
$ comprobar-cobertura-de-gate.py --manifiesto m_min.json --lectura l_min.json --raiz CANDIDATA
  OBLIGATORIO − ASIGNADO                 ∅
  ASIGNADO − LEÍDO                       ∅
  LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS       ∅
  FUENTES MODIFICADAS − LEÍDAS ÍNTEGRAS  ∅
  COBERTURA COMPLETA                                              EXIT=0
```

**Una línea leída satisface las cuatro restas de `O27` §5.**

**Y el manifiesto de ESTE gate repite la afirmación falsa en su §4:** «**`OBLIGATORIO` se
deriva del ÁRBOL** —las 239 modificadas— y el manifiesto sólo puede AMPLIARLO. Esto se dice
porque la primera versión de este instrumento tenía ahí una TAUTOLOGÍA … Lo encontró la
auditoría del 2026-09-04 (`H-06`) y **está corregido**». La tautología `X − X` está corregida;
la DERIVACIÓN DESDE EL ÁRBOL que se anuncia en su lugar **no se ha escrito**.

**Remedio:** derivar `modificadas` con `git diff --name-only <base>..<candidata>` DENTRO del
instrumento y prohibir que el manifiesto quite nada de ese conjunto — que es lo que su propio
bloque de decisión dice que hace. **Propietario:** `PLT`. **Fase:** `F6`. **Clase:** INTERNO.

#### `HALLAZGO 6` · **MEDIO · INTERNO** — el diagnóstico del append-only nombra UNA entrada y agrega el resto

**Sede:** `kernel/operativo/runtime/admision/perimetro.py` L487-499 ·
`test_admision.py::test_T342_*`.
**Hecho.** `sede.juzgar()` devuelve TODAS las infracciones; el `Hallazgo` publicado lleva
`primera["causa"]` más `" (y N más: <códigos>)"`. Las identidades de las demás entradas
destruidas y sus commits se calculan y se descartan. Medido en el ATAQUE 1: ocho entradas
destruidas, UNA nombrada.
`T342` declara en su `entonces` «el diagnóstico **nombra una a una** las entradas destruidas
y el commit que introdujo cada una» y está en VERDE porque sus dos pruebas miden otro objeto:
una afirma sobre la lista cruda de `sede.juzgar`, y la del veredicto sólo exige
`"ALTERACIÓN DE ENTRADAS CERRADAS" in hallazgo.causa`.
**Remedio:** publicar la lista completa en el `Hallazgo` —el dato ya está calculado— y hacer
que la prueba del veredicto exija cada identificador.
**Propietario:** autoría de `F6`. **Fase:** `F6`. **Clase:** INTERNO.

#### `HALLAZGO 7` · **MEDIO · INTERNO** — `D112` no abre epígrafe propio, y es la CUARTA vez

**Sede:** `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` L611.
**Hecho.** El propio registro escribe la regla en L552-556: «**LA REGLA, escrita ahora para
que no haya una cuarta vez:** *toda propagación de una resolución del Owner abre EPÍGRAFE
PROPIO*. Una fila de propagación bajo el epígrafe de otra tanda es el defecto, no la
excepción». Medido: `### D110`, `### D111`, `### D113`, `### D114`, `### D115` y `### D116`
existen; **`D112` no**. `D112` es la propagación de `O23`, el acto que APRUEBA la sección
`(g)` —la norma de todo el eje de estado durable de `F6`—, y vive como fila suelta bajo el
epígrafe de `D111`, que habla de otra tanda.
**Remedio:** abrirle su epígrafe, moviendo la fila VERBATIM, como se hizo con `D107` (`S-19`).
**Propietario:** `SIS`. **Fase:** `F6`. **Clase:** INTERNO.

#### `HALLAZGO 8` · **MEDIO · INTERNO** — la VERSIÓN del kernel no se movió en 188 ficheros de cambio

**Sede:** `kernel/VERSION` · `kernel/KERNEL_CHANGELOG.md` · `comprobar_versiones.py`.
**Reproducción:**

```console
$ git log -1 --format=%H -- kernel/VERSION                       → d050836 «segundo corte»
$ git log -1 --oneline   -- kernel/KERNEL_CHANGELOG.md           → d050836 (el mismo)
$ git diff --name-only d050836..HEAD -- kernel/ | wc -l          → 188
```

Entre esos 188 está el macrobloque 3 entero, las correcciones `E-07`…`E-18` y los tres
bloqueantes `ADJ-B1`, `ADJ-B2`, `ADJ-B3`. `kernel/VERSION` sigue en `2.0.0-alpha.11` y la
entrada más reciente del CHANGELOG describe **sólo el segundo corte**. `VERSIONES.md` regla 3
dice «Si no coinciden, o falta la entrada **o falta el cambio de versión**»; `T152` compara
los dos entre sí —ambos congelados— y **ninguno contra el contenido del kernel**, de modo que
la segunda mitad de la regla no está mecanizada. La huella SÍ se movió
(`7196ce99457a77d4`): lo que falta es el ANUNCIO, no la integridad.
**Remedio:** subir el release y escribir su entrada, y que `T152` exija que un cambio bajo
`kernel/` sin cambio de `kernel/VERSION` sea ROJO. **Propietario:** `PLT` implementa · `SIS`
propietario. **Fase:** `F6`. **Clase:** INTERNO.

#### `HALLAZGO 9` · **MEDIO · INTERNO** — la línea base no es determinista bajo carga

**Sede:** `kernel/operativo/runtime/pruebas/test_contencion.py::test_con_el_backend_simple_el_bisnieto_SI_escapa`.
**Reproducción:** §1.1. Con dos corridas concurrentes del mismo runner: `35/36 · 1 problema`.
Aislada: `Ran 20 tests · OK`. **Remedio:** la prueba tiene que ESPERAR a que el bisnieto
exista antes de cancelar, o declarar el requisito de exclusividad de la máquina en la línea
base. **Propietario:** autoría de `F6`. **Fase:** `F6`. **Clase:** INTERNO.

#### `HALLAZGO 10` · **MEDIO · INTERNO** — cifra escrita a mano que la evidencia del propio árbol desmiente

**Sede:** `kernel/operativo/pruebas/T340-T359-append-only-y-universo.md` L57-58.
**Hecho.** Publica «**161** escenarios lo tienen y **92** no»; `evidencia/evidencia-salida.txt`
dice «contrastados **195** · no contrastables **72** · divergencias 0», reproducido con
`registro_pruebas.py`. Es el documento que cierra `ADJ-G2` —el hallazgo de que el estado se
escribía a mano y nadie lo contrastaba— y publica a mano una cobertura caducada. `T151` está
en VERDE: su tabla de cifras no alcanza a ésta.
**Remedio:** retirar las dos cifras y remitir a la evidencia, como hace el resto del corpus.
**Propietario:** autoría de `F6`. **Fase:** `F6`. **Clase:** INTERNO.

#### `HALLAZGO 11` · **MEDIO · INTERNO** — las tres pruebas que cubren `ADJ-G1` no están ejecutadas

**Sede:** `T340-T359-…md`, escenarios `T351`, `T352`, `T353`.
**Hecho.** Las tres declaran `ejecucion: guion-manual` y `estado: validador-implementado`, sin
campo `evidencia:`. El remedio del GRAVE `ADJ-G1` —el cliquet del universo, el fallo cerrado
del derivador y el alcance medido del cliquet— **no tiene veredicto publicado por escenario**.
Lo que sí corre en el runner es `derivar-universo-obligatorio.py --autopruebas`, que es otra
cosa: sus 12 sabotajes no atacan la fuente del cliquet.
**Remedio:** llevarlas a un validador del manifiesto canónico, o declarar por qué no pueden
estarlo. **Propietario:** `PLT`. **Fase:** `F6`. **Clase:** INTERNO.

#### `HALLAZGO 12` · **MENOR · INTERNO** — nota caducada sobre `CONTRATO 3`

**Sede:** `docs/f6/01-MATRIZ-DE-COMPLETITUD-F6.md` L201-203.
**Hecho.** Afirma «ningún escenario nombra `CONTRATO 3` en su `cubre`, de modo que el
derivador del universo lo publica en la resta **A**». Medido: `T158` y `T350` lo nombran, y
`A = 0`. Falsa por los dos extremos. **Remedio:** retirarla o remitir.
**Propietario:** `SIS`. **Fase:** `F6`. **Clase:** INTERNO.

#### RECUENTO

```text
BLOQUEANTE            1   HALLAZGO 0                            del APARATO DEL GATE
GRAVE                 5   HALLAZGOS 1, 2, 3, 4, 5               todos INTERNOS
MEDIO                 6   HALLAZGOS 6, 7, 8, 9, 10, 11          todos INTERNOS
MENOR                 1   HALLAZGO 12                           INTERNO
EXTERNOS                  ninguno nuevo. `E-17` y `E-18` permanecen donde estaban, y lo
                          he verificado en vez de aceptarlo
```

**Ninguno de mis hallazgos convierte una deuda interna en externa.** Los doce son del árbol o
del aparato del gate, y ninguno se cierra con una búsqueda textual.

---

### 5 · LO QUE EL ÁRBOL SÍ SOSTIENE

Esto no es cortesía. Cada línea se ha medido, y varias van contra mi propio ataque.

**El append-only de la sede del Owner, cerrado por su PROPIEDAD.** Es lo mejor que he medido.
Once resoluciones, once mutaciones de un byte, once rojos, cada uno nombrando la entrada y el
**commit que la introdujo**. Y la otra mitad, que es la que separa un guardián de un cerrojo:
el apéndice legítimo PASA, y las siete formas defectuosas dan rojo **cada una con su código
propio** —`ENTRADA_INCOMPLETA`, `SALTO_DE_NUMERACION`, `FAMILIA_DESCONOCIDA`,
`ENTRADA_DUPLICADA`, `ENTRADAS_REORDENADAS`, `ENTRADA_BORRADA`, `ENTRADA_ALTERADA`—. El
régimen se decide desde la HISTORIA y no desde el fichero de hoy, de modo que borrar las
cabeceras no apaga el guardián. `ADJ-B3` está cerrado de verdad.

**El delimitador NO se cuenta como contenido**, y eso —que parece un detalle— es lo que
impide que la sede dé rojo sobre sí misma en cuanto se inscriba `O28`. Medido: la última
entrada gana exactamente los seis bytes del delimitador cuando se inscribe la siguiente, y el
juicio lo descuenta.

**El cliquet de obligaciones resiste tres ataques y no se engaña renombrando.** Retirar la
cobertura y reimputar los sabotajes a un identificador inexistente sigue dando `EXIT=2` con
el nombre de quien ejerce la obligación perdida. Hacen falta cuatro ediciones coordinadas —y
una de ellas es la vía que yo he encontrado— para que ceda.

**Las tres restas publican, pegada a su cifra, la proposición que NO demuestran.** El
derivador escribe «`A=0` **NO demuestra** `O26` §5.1» y «`B=0` **NO demuestra** §5.2» dentro
de su propia salida. Es exactamente lo contrario de un alibi: es un instrumento que se acota
a sí mismo en el sitio donde alguien podría leerlo de más.

**El estado de un escenario está mecanizado contra su evidencia, y baja solo.** `T350` caza
un `prueba-superada` fabricado, lo nombra y dice por qué. Y `H-02` bajó CATORCE escenarios de
`prueba-superada` a `prueba-ejecutada` contra el interés del corpus, cuando midió que su
evidencia no los nombraba. `ADJ-G2` está cerrado.

**`T360` mecaniza `ADJ-G3` por SONDA en el disco y no por texto.** Reintroducir la negación
falsa en una sede barrida da rojo con fichero, línea, pieza y sonda. Es el mecanismo correcto;
lo que falla es su FRONTERA, no su diseño.

**Las sedes de estado dicen la verdad.** `03-GOBIERNO` §6 coincide campo a campo con `O24` y
con el manifiesto, y **remite** en vez de copiar el estado de construcción. `04-CONTRATOS` §1
es la única sede de construido/diseñado y las demás secciones remiten a ella.

**`O27` está inscrita literal y no se sobreactúa.** No se presenta como certificación en
ninguna sede —cuatro lo niegan expresamente—, y `B3` no se declara satisfecho en ninguna;
`06-DEUDA` §3 escribe «`B3` NO queda satisfecho por este acto».

**`E-17` y `E-18` no se han maquillado.** La una lleva propietario, mecanismo, condición de
cierre y un barrido que impide afirmar custodia productiva; la otra lleva su `errno` medido y
la cláusula «la certificación queda LIMITADA AL BACKEND EJERCIDO».

**El derivador y el emisor declaran lo que NO garantizan dentro de su propia salida.** El
sobre de ancla escribe, en el sobre y no en una nota aparte, que `git status --porcelain`
vacío «es TODO lo que esa negativa prueba», y que la sede canónica **no es mecánicamente
verificable contra una fuente externa al sistema**. Un aparato que publica su propio límite
donde el lector lo va a encontrar es lo contrario de lo que este gate busca.

**Y la línea base se reproduce entera**, con el intérprete prescrito y sobre el checkout
congelado. No es poco: es 36 validadores, 158 infracciones deliberadas detectadas y ninguna
sin detectar, y 195 estados contrastados sin una divergencia.

---

### 6 · MI JUICIO EXPRESO SOBRE BLOQUEANTES INTERNOS VIVOS EN MI EJE

Mi eje es `F6-A`…`F6-J`, `V6-01`…`V6-19`, `g.1`…`g.16`, §19, `F6-H`, las matrices, la deuda,
la autoridad, las sedes de estado, `O27` y las tres restas.

**¿Hay algún BLOQUEANTE interno vivo en mi eje?**

**NO.** Y lo digo con la misma dureza con la que he escrito lo demás: los tres bloqueantes
del gate anterior —`ADJ-B1`, `ADJ-B2`, `ADJ-B3`— los he atacado uno a uno donde caen dentro
de mi lote y **`ADJ-B3` está cerrado por su propiedad**, no por su instancia. No he
encontrado en mi eje ninguna propiedad crítica que se pueda romper con el árbol en verde.

**Pero hay CINCO GRAVES internos vivos**, y tres de ellos tocan directamente lo que `O26` §5
convierte en criterio de certificación:

```text
HALLAZGO 2   el universo obligatorio ENCOGE en silencio por una vía nueva, y las tres
             restas siguen a cero sobre el universo mutilado
HALLAZGO 5   el SUELO del universo del gate se DECLARA en vez de derivarse, de modo que una
             línea leída satisface las cuatro restas de `O27` §5
HALLAZGO 4   el comprobador de cobertura COLAPSA los rangos múltiples y no mide siete de los
             ocho rangos de `11-ARQ` de REV-1
HALLAZGO 1   la sede de 32 de las 58 obligaciones está rotulada «historia inmutable» y
             exenta del barrido que existe para cazar exactamente lo que ella contiene
HALLAZGO 3   `E-10` no alcanza al canal que produce TODA la evidencia de la línea base
```

**Y un BLOQUEANTE del APARATO DEL GATE, que es el que decide si este gate puede llegar a
adjudicación:** `HALLAZGO 0`. El manifiesto asigna a REV-2 un rango que excede el fichero, y
el comprobador que `O27` §5 eleva a norma **no puede devolver 0 con ese manifiesto**, haga lo
que haga REV-2.

#### Por qué NO he graduado BLOQUEANTE ninguno de los cinco, y lo razono en vez de afirmarlo

Un revisor que gradúa a ojo no sirve. El criterio que aplico es el que el expediente ya usa:
**BLOQUEANTE es lo que rompe una propiedad que una condición de `O26` §1 nombra, o lo que
impide que el gate mida.**

```text
HALLAZGO 3   `E-10` en las baterías. El defecto es el MISMO que `ADJ-B2`, que el gate
             anterior graduó BLOQUEANTE — y lo graduó así porque `O26` §1 condición 8 juzga
             expresamente `kernel/operativo/raiz-externa/`. NINGUNA condición de `O26` §1
             nombra las baterías. Lo gradúo GRAVE por eso, y digo que la diferencia es de
             COMPETENCIA y no de gravedad técnica: técnicamente es peor, porque el canal
             afectado produce las 36 evidencias
HALLAZGO 2   encoger el universo exige CUATRO ediciones coordinadas de quien ya puede
             escribir el árbol. Es la clase `M-04`, que el corpus declara insatisfacible
             desde dentro y que `O18` reserva al verificador externo de `F6`. El gate
             anterior graduó GRAVE su hermano `ADJ-G1`, y mantengo la graduación
HALLAZGO 1   una sede que miente no rompe ninguna propiedad ejecutable: rompe la
             TRAZABILIDAD de 32 obligaciones. `ADJ-G3`, su hermano exacto, se graduó GRAVE
HALLAZGO 4
HALLAZGO 5   son del APARATO DEL GATE. No degradan la candidata: degradan la medida. Su
             consecuencia la recoge `HALLAZGO 0`, que sí es BLOQUEANTE
```

**Si el adjudicador considera que el canal de evidencia entra en `O26` §5.5 —«ningún
bloqueante interno vivo»— porque sin él ninguna de las cinco condiciones es comprobable, la
graduación de `HALLAZGO 3` sube a BLOQUEANTE y mi conclusión de este apartado cambia. Lo dejo
dicho para que la decisión sea suya y no quede escondida en mi tabla.**

#### Lo que eso significa, dicho sin rodear

`O26` §5 pide cinco cosas para que un gate gane competencia. Sobre lo que yo he medido:

```text
§5.1  «no quedan obligaciones internas sin implementar»   `A=0` NO lo demuestra, y el
                                                          propio derivador lo escribe
§5.2  «no quedan propiedades críticas sin prueba capaz     `B=0` NO lo demuestra, mismo
      de fallar»                                           motivo, y sigue el predicado
                                                           que dejó pasar `ADJ-B3`
§5.5  «ningún bloqueante interno vivo»                     EN MI EJE, SE CUMPLE
```

Y `O27` §5 —«un gate no puede llegar a adjudicación mientras algún revisor tenga una resta
`ASIGNADO − LEÍDO` distinta del conjunto vacío»— **no es satisfacible con este manifiesto**.

**Mi lote está cerrado y mis dos restas están a cero.** No sustituyo la lectura de nadie, no
compenso con lo que otro haya leído y no cierro por ellos. Lo que digo es que, con el
manifiesto tal como está commiteado, la cobertura del gate es **mecánicamente inalcanzable**,
y decirlo a tiempo es lo correcto.

---

> **CIERRE.** `/home/jose/ads-kernel`: `HEAD 54898fc9154b7f15bd93ba09003fe1b4e0941001`,
> `git status --porcelain` **vacío**, 106 referencias — idénticos a la apertura. No he
> corregido nada, no he propuesto ningún commit, no he hablado con los otros revisores y no
> he abierto ningún otro gate. Los hallazgos quedan **REGISTRADOS Y NO APLICADOS**.

— **REVISOR 3**, 2026-09-05

