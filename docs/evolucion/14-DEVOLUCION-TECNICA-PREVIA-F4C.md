# DEVOLUCIÓN TÉCNICA PREVIA A LA TERCERA REVISIÓN DE F4C

> **Qué es esto, y qué NO es.**
>
> ```text
> PROCEDENCIA        auditoría externa de CODEX sobre el ÁRBOL REMOTO REAL, en el commit
>                    7ebdd8acdfc28bd55a17b8855ca3fb932a8ffa7e. No procede de un informe:
>                    procede de leer el repositorio publicado.
>
> QUÉ ES             una REVISIÓN TÉCNICA PREVIA. Encuentra contradicciones internas y
>                    restos editoriales que sobrevivieron a las dos devoluciones anteriores.
>
> QUÉ NO ES          un VEREDICTO INDEPENDIENTE DE SUFICIENCIA. **Esta devolución NO
>                    certifica `F4c`**, y su aplicación tampoco. `F4c` sigue ABIERTA.
>
> A QUIÉN NO SE      estos hallazgos **NO son del segundo revisor**. Son de una auditoría
> ATRIBUYE           posterior y distinta, sobre el resultado ya corregido. Atribuírselos
>                    falsearía la procedencia, que es lo que estos documentos protegen.
>
> QUIÉN APLICA       el autor material de F4. Como en las dos anteriores, **quien aplica es
>                    quien recibe**, y eso no prueba que esté bien resuelto.
> ```

**Por qué llega esta devolución y no la tercera revisión.** Las dos devoluciones anteriores
corrigieron el diseño; ésta encuentra que **el texto corregido no es internamente
consistente**: el autómata transaccional tiene dos vocabularios, un mecanismo de
detectabilidad rompe los hashes que protege, y una transacción necesita abrir otra
transacción para registrar lo que impide abrir transacciones. Llevar eso a una tercera
revisión independiente sería gastarle el tiempo en defectos que un barrido mecánico ya
encuentra.

---

# Los once hallazgos

## `1` · El ciclo transaccional no tiene un vocabulario único — **BLOQUEANTE**

**Reproducción textual.** El documento titula §2.6.1 *«Los **cuatro** registros»* y enumera
cinco: `preparada`, `confirmada`, `derivada`, `conflicto`, `reconciliada`. Y a la vez:

```text
§2.6.1 título     «Los cuatro registros, y qué significa cada uno»       → enumera CINCO
`D38`             «`fase: abortada` se RETIRA. Cuatro registros de
                  transacción, no cinco»                                 → hay cinco
§3.6              `fase  preparada | confirmada | derivada | abortada |
                  conflicto`                                             → conserva
                                                                           `abortada` y
                                                                           OMITE
                                                                           `reconciliada`
§2.6.2 punto 1    «La comparten los CINCO registros de esa transacción»  → contradice §2.6.1
integridad        «toda transacción cuyo evento terminal sea `confirmada`
post-terminal      o `derivada`»                                         → `confirmada` no
                                                                           es terminal: el
                                                                           marcador sigue
                                                                           abierto hasta
                                                                           `derivada`
```

**Corrección.** Un solo autómata, con dos rutas y **un único cierre terminal**:

```text
RUTA NORMAL       preparada → confirmada → derivada
RUTA DE CONFLICTO preparada → conflicto → reconciliada → derivada
```

`conflicto` abierto y absorbente · `reconciliada` devuelve la coherencia y declara los hashes
finales, **pero todavía hay que regenerar derivados** · `derivada` es el **único** terminal de
ambas rutas · `abortada` retirada y **rechazada por el esquema**.

> **ADDENDUM 2 · dos palabras de esta prescripción quedaron revisadas, y se dicen.** Una
> SEGUNDA corrección técnica encontró que **«absorbente» describe mal lo vigente** —de
> `conflicto` sale una transición, hacia `reconciliacion-preparada`, y puede volver a
> entrarse en él hasta tres veces—, y que **«rechazada por el esquema» sólo es cierto para
> `abortada`**, que es un valor fuera del enum: las demás reglas que se le atribuyeron al
> esquema exigen recorrer el diario o mirar el disco. La norma vigente dice **«abierto y
> bloqueante»** y reparte las garantías en tres capas. Son `D55` y parte de `D57`. El texto
> de arriba se conserva.

**No se reescribe `D38`.** Se añade `D46`, que la revisa y explica que retirar `abortada` y
añadir `reconciliada` deja **cinco fases, no cuatro**.

> **ADDENDUM · esta prescripción quedó CORTA, y se dice.** Una corrección técnica posterior
> encontró que la ruta de conflicto de este mismo autómata **no era recuperable**:
> `reconciliada` declaraba la decisión y a la vez la daba por aplicada, luego una caída entre
> decidir y emitir dejaba el diario sin la decisión, sin su mecanismo y sin el resultado
> esperado. Se añadió `reconciliacion-preparada`, y el autómata vigente tiene **SEIS fases**.
> Es `D52`, y revisa a `D46`. El texto de arriba se conserva como lo que era: la prescripción
> de esta devolución, correcta en lo que vio e insuficiente en lo que no.

**Prueba futura `X47`.** El enum de `evento.fase` es único en todo el corpus, `abortada` es
rechazada por el validador de esquema, y ninguna sección enumera un conjunto distinto.

## `2` · `tx_abierta` hace incoherentes los hashes — **BLOQUEANTE**

**Reproducción textual.** §2.6.8 exigía:

> *«CADA CANÓNICO AFECTADO LO DICE EN SU CABECERA — durante la ventana, su cabecera lleva
> `tx_abierta: TX-<id>`. Lo escribe la propia transacción al preparar y lo retira al
> confirmar, dentro de la misma transacción.»*

**Seis consecuencias, y ninguna estaba resuelta:**

```text
1  el contenido con `tx_abierta` NO CASA con el `hash_posterior_esperado` declarado
2  retirarlo exige una SEGUNDA escritura de todos los ficheros
3  esa retirada es, ella misma, otra TRANSICIÓN MULTIARCHIVO
4  el paso APLICAR describe UNA escritura, no dos
5  CONFIRMAR emite un evento y NO retira cabeceras
6  «lo escribe al preparar» contradice que PREPARAR no toca ningún canónico
```

**Corrección.** **`tx_abierta` se retira de los canónicos.** La detectabilidad no exige
contaminar el contenido canónico, y se sostiene sobre tres piezas que ya existen: la **regla
de lectura obligatoria**, el **marcador con `tx` y rutas afectadas**, y el **diario como
fuente de reconstrucción**.

**Prueba futura `X48`.** Ningún mecanismo de detección modifica el contenido de un canónico:
tras aplicar una transacción, el hash de cada fichero es **exactamente** el
`hash_posterior_esperado` declarado en `preparada`, byte a byte.

## `3` · Reconciliación recursiva e imposible — **BLOQUEANTE**

**Reproducción textual.** §2.6.9 decía:

> *«al escribir `conflicto`, la transacción marca `reconciliacion_pendiente` en el
> `03-integracion.md` de CADA ITEM AFECTADO, y lo hace **DENTRO DE UNA TRANSACCIÓN PROPIA**
> con las mismas garantías»*

Contra `X08`, en la propia tabla adversarial:

> *«dos ejecutores preparan transacciones que tocan el mismo fichero → el segundo encuentra
> el marcador `.abierta` y **no arranca**: `R5` es un lock, no un consejo»*

**El protocolo necesitaba abrir otra transacción para registrar el estado que impide abrir
otra transacción.** La transacción original sigue abierta y su marcador bloquea.

**Corrección.** `reconciliacion_pendiente` **deja de ser una bandera que se escribe** y pasa a
ser un **predicado derivado**:

```text
reconciliacion_pendiente(item) ≡
    existe una transacción con evento `conflicto` SIN `reconciliada` ni `derivada`,
    cuyo evento `conflicto` nombra ese item
```

El evento de conflicto **ya conoce** los items y rutas afectados. `b.4` P0 y §3.3.1 `Q0`
consumen el predicado **sin mutar ningún item** y sin transacción recursiva.

**Prueba futura `X49`.** Provocar un conflicto y comprobar que `b.4` P0 devuelve
`reconciliacion-pendiente` para los items afectados **sin que se haya escrito un solo byte en
ningún `03-integracion.md`** y sin que exista un segundo marcador.

## `4` · Reconciliar también exige regenerar — **GRAVE**

**Reproducción textual.** §2.6.9 declaraba `reconciliada` *«terminal, y es el único que lo es
para una transacción en conflicto»*, y a la vez su decisión puede *«conservar lo divergente,
aplicar lo preparado, o un tercer contenido decidido»* — cualquiera de las cuales **cambia los
canónicos**. Los derivados estaban bloqueados durante el conflicto, y nadie los regeneraba.

**Corrección.** `reconciliada` **deja de ser terminal**. Declara cinco cosas y cierra por
`derivada`:

```text
1  APLICACIÓN DURABLE de la decisión, fichero a fichero, con la disciplina de fsync de §2.6.6
2  HASHES FINALES resultantes, que SUSTITUYEN al `hash_posterior_esperado` para los ficheros
   que la reconciliación tocó
3  REGENERACIÓN de los derivados que dependen del estado reconciliado
4  CIERRE por `derivada`, único terminal
5  RETIRADA DEL MARCADOR, sólo entonces
```

**Prueba futura `X50`.** Reconciliar un conflicto y comprobar que los derivados afectados se
regeneran **antes** de `derivada`, que el marcador sobrevive hasta `derivada`, y que los
canónicos casan con los `hash_final` de `reconciliada`.

## `5` · Integridad posterior incompleta — **GRAVE**

**Reproducción textual.**

```text
«toda transacción cuyo evento terminal sea `confirmada` o `derivada`»   → `confirmada` no es
                                                                          terminal
«Todo lo anterior al último commit está RESPALDADO POR GIT»             → «respaldado» no es
                                                                          «el fichero actual
                                                                          es correcto»
```

Y no contemplaba los hashes finales de una reconciliación, ni el caso de un working tree
divergente sin transacción abierta.

**Corrección.** Se define con precisión qué es una ventana de commit, qué transacciones se
comprueban, qué hash rige tras `reconciliada`, cómo se verifica que los canónicos versionados
coinciden con `HEAD`, qué ocurre ante un working tree divergente **sin** transacción abierta
—se reporta y se escala, y **nunca se restaura sola**— y con qué autoridad se restaura desde
Git: **la del Owner, nunca automática**.

> **ADDENDUM · esta corrección introdujo un defecto propio, y se dice.** Al hacer que la
> comprobación emitiera `conflicto`, y siendo `derivada` terminal por `D46`, quedó **una
> transición que sale del terminal**. La corrección técnica posterior lo separó por
> identidad: `conflicto` para una transacción abierta, evento **`deriva`** para lo descubierto
> tras el cierre. Es `D53`, y revisa a `D34` y a `D46`.

> **ADDENDUM 2 · y el reparto entre `conflicto` y lo demás quedó otra vez corto.** La
> corrección técnica posterior separó por identidad —`conflicto` para la transacción abierta,
> `deriva` para lo descubierto tras el cierre—, y al hacerlo dejó `W12a` mandando `conflicto`
> ante un canónico revertido a su `hash_previo`, que es exactamente la caja **NO APLICADO**
> de §2.6.4 y lo que `W3` y `W4` completan. La segunda corrección técnica lo clasifica contra
> la **última fase durable**: se reaplica de forma idempotente, y `conflicto` exige
> **transacción abierta Y divergencia real**. Es `D56`, y revisa a `D34`, `D36`, `D35` y
> `D53`.

**Prueba futura `X51`.** Working tree divergente respecto a `HEAD` sin transacción abierta: el
arranque **lo nombra**, no lo completa, no lo revierte y no lo restaura.

## `6` · El marcador creaba una tercera categoría informal — **MEDIO**

**Reproducción textual.** §2.4 divide todo en dos: *«DURABLE Y VERSIONADO: todo `estado/`»* y
*«OPERACIONAL Y NO VERSIONADO: `.ads/run/`»*. Y `D40` dejaba el marcador en `estado/tx/`, **no
versionado**, reconstruible, *«vive en el árbol durable y no viaja»* — una tercera categoría
que el modelo no tiene.

**Corrección.** El marcador es **OPERACIONAL**, y está bajo `estado/` por una **excepción de
ruta declarada**, no por su naturaleza. Con ello: `plano: operacional`, «todo `estado/` es
durable y versionado» deja de ser cierto y se corrige con la excepción nombrada, y
`.gitignore`, reconstrucción y ausencia en clones quedan alineados. **No se inventa una
tercera categoría.**

## `7` · Contratos canónicos no actualizados — **MEDIO**

Restos comprobados uno a uno contra el fichero:

```text
§2.6.3     «se crea `estado/tx/<TX-ID>.abierta`, marcador SIN CONTENIDO»  frente a §2.6.8,
           que declara que lleva `tx` y rutas afectadas
§3.6       conserva `abortada` y OMITE `reconciliada`
§3.4       NO contiene `resolucion_del_control_repo`, y §6.7 afirma que se añadió allí
§5.6       los tres ejemplos siguen usando `verificador`
§9.2       sigue usando `verificador`
§9.2       «responsables  las que la norma declara», cuando §3.5 establece que la celda
           registra SÓLO LA DESVIACIÓN
```

**Corrección.** Los campos vigentes pasan a ser: `auditor` **siempre** ·
`verificador_de_correccion` **cuando el estado de la celda es `corregido-sin-verificar` o
`verificado`**, y vacío en los demás · reparto por defecto **heredado** del contrato de clase ·
desviación local **motivada**.

## `8` · Las pruebas de Integrada seguían duplicadas — **MEDIO**

**Reproducción textual.** §9.1 enumera **cuatro** pruebas propias de Integrado; §9.5 enumera
**cinco**, porque añade `integration-set producido`. El documento afirma que ambas tablas son
proyecciones de una única lista, **y no proyectan el mismo censo**.

**Corrección.** La lista normativa vive **una sola vez**, en `nivel-certificacion:integrado`.
§9.1 y §9.5 derivan de ella, muestran el mismo censo, distinguen prueba, aplicabilidad y
condición, no fusionan dos pruebas sin declararlo y no repiten comprobaciones estructurales.

**Prueba futura `X52`.** Las proyecciones de §9.1 y §9.5 enumeran **exactamente** las mismas
pruebas que la lista normativa del nivel. Una diferencia de censo es un fallo.

## `9` · Dos huellas no son tres huellas — **MENOR**

`D31` y varios resúmenes dicen «tres huellas separadas». El diseño define **dos** —semántica y
de entorno— más un **artefacto de salida que las contiene**. El artefacto no es una huella.

**Corrección.** Se añade `D47`, que revisa `D31` sin reescribirla; se corrigen los resúmenes
**vigentes**; y se conserva como histórico todo texto claramente marcado como estado anterior
—incluido el propio hallazgo `N-13` del segundo revisor, que es quien lo detectó primero.

## `10` · Solapamiento entre dos esquemas de clase — **MEDIO**

`contrato-de-aspecto` declara `familia: calidad | documental | certificacion`, y
`nivel-certificacion` ya declara para certificación pruebas, propietario, crítico, jerarquía,
invalidación y criterio. **Dos normas editables para el mismo aspecto.**

**Corrección.** Fuente única por reparto de dominio: **`contrato-de-aspecto` cubre `calidad` y
`documental`; la certificación usa EXCLUSIVAMENTE `nivel-certificacion`.** El valor
`certificacion` desaparece del enum de familia.

**Prueba futura `X53`.** No existe ningún `contrato-de-aspecto` de familia `certificacion`, y
ningún campo de certificación está declarado en dos sitios.

## `11` · Restos editoriales que invalidan los overclaims — **MENOR**

**Confirmadas** tres formulaciones mutuamente excluyentes, todas resueltas por los hallazgos
1, 2 y 5: cuatro registros frente a cinco · «sin contenido» frente a «con contenido» ·
`confirmada` terminal frente a no terminal.

> **Y dos que NO se reproducen, dicho porque corregir lo que no existe sería peor que no
> corregirlo.** La auditoría señala `2 HASH PREVIO` y `QUE b.4 P0 CONSUME` como
> «duplicados». Un barrido literal sobre todo `docs/` devuelve **una sola aparición de cada
> uno**: son etiquetas de dos líneas dentro de un bloque de ancho fijo —la etiqueta
> `EMITE LA BANDERA / QUE b.4 P0 CONSUME` y el punto `2 HASH PREVIO` de una lista numerada—,
> no repeticiones. Se registra como **no reproducido**, y el bloque que las contenía se
> reescribe igualmente por el hallazgo 3.

---

# Veredicto

> **Estado de esta devolución tras DOS correcciones técnicas posteriores.** Dos de sus once
> prescripciones —el autómata de cinco fases y la integridad post-terminal— resultaron
> **insuficientes o defectuosas**, y están revisadas por `D52` y `D53`. Una **segunda**
> corrección técnica revisó además el término «absorbente», la atribución de garantías al
> esquema y la clasificación de `W12a`: `D55`, `D56` y `D57`. Se conservan enteras: son el
> registro de qué se vio entonces, y la prueba de que una devolución que se aplica no queda
> por ello comprobada.

```text
ESTA DEVOLUCIÓN NO CERTIFICA `F4c`.

Es una revisión TÉCNICA y PREVIA. Encuentra contradicciones internas del texto ya corregido;
no juzga si la arquitectura es suficiente, y no sustituye a la tercera revisión independiente.

TRES BLOQUEANTES    1 · el autómata no tenía vocabulario único
                    2 · el mecanismo de detectabilidad rompía los hashes que protege
                    3 · la reconciliación era recursiva e imposible
DOS GRAVES          4 · reconciliar no regeneraba · 5 · integridad posterior incompleta
CUATRO MEDIOS       6 · 7 · 8 · 10
DOS MENORES         9 · 11
NO REPRODUCIDO      dos de los cinco restos del hallazgo 11

QUIEN APLICA ES QUIEN RECIBE. `F4c` sigue ABIERTA, y la tercera revisión independiente sigue
siendo su única puerta.
```
