# 20 · PAQUETE ÚNICO DE DECISIONES DEL OWNER · `F5`

**Este documento reúne TODAS las decisiones que `F5` necesita del Owner, agrupadas para que
puedan responderse en una sola interacción.** No hay una segunda tanda escondida: el
macrobloque recorrió `F5-A`…`F5-G` completos antes de escribir esto.

> **QUÉ ES ESTE DOCUMENTO.** Un artefacto DERIVADO que plantea preguntas. **No es norma, no
> es una enmienda y no contiene ninguna respuesta del Owner.** Ninguna opción está
> ejecutada. Ninguna recomendación está aplicada.
>
> **CÓMO SE COMPRUEBA QUE NO INVENTA PREGUNTAS.** Cada decisión de aquí está referenciada
> por al menos una fila de [`MATRIZ-F5.yml`](MATRIZ-F5.yml), y cada fila que declara
> `decision_owner: SI` nombra una decisión de aquí. El control `F8` de
> [`validar-f5.py`](validar-f5.py) lo comprueba **en los dos sentidos**: una pregunta sin
> obligación detrás es una pregunta inventada, y una obligación sin pregunta es una
> obligación que nadie contesta.

**Antes:** [`10-MATRIZ-CANONICA-DE-F5.md`](10-MATRIZ-CANONICA-DE-F5.md) ·
**Índice:** [`00-INDICE-F5.md`](00-INDICE-F5.md)

---

## 0 · Cómo leer esto, y qué se espera de usted

**Hay dos clases de asunto, y no se mezclan.**

```text
ELECCIÓN REAL      D-01 … D-10, y R-05.  Existen DOS o TRES salidas legítimas y ninguna autoridad
                   vigente impone una. Usted elige. Cada una lleva una recomendación
                   técnica razonada, que es una recomendación y no una decisión tomada.

ACTO DE APROBACIÓN R-01 … R-04.  El contenido ya está determinado por una autoridad
                   vigente y NO hay nada que elegir. Lo que falta es su acto: el material
                   es APROBADO, y nada se aplica sobre él sin aprobación expresa suya.
                   No se le presentan opciones inventadas para simular una elección.
```

**Lo que NO está aquí, y se dice para que no lo busque:**

```text
NO ESTÁ AQUÍ   la sede del gobierno Git del control repo. La resolvió `O16` y no se
               vuelve a preguntar
NO ESTÁ AQUÍ   el contenido de la raíz externa de confianza. Lo ratificó `O18`. Sólo se
               pregunta DÓNDE vive su norma
NO ESTÁ AQUÍ   el valor por defecto de la política de publicación del control repo.
               `esperando-owner` está fijado, y la ausencia nunca significa «publica»
NO ESTÁ AQUÍ   las dos decisiones que el corpus declara DEFERIDAS. Siguen deferidas, y
               este paquete no las reabre
NO ESTÁ AQUÍ   nada de `F6`. Ni un contrato, ni un verificador, ni la raíz externa como
               implementación
```

**Respuesta mínima que se le pide:** para cada `D-nn`, la letra de la opción. Para cada
`R-nn`, `APRUEBO` o `NO APRUEBO`. Un renglón por asunto es suficiente.

---

# PARTE 1 · ELECCIONES REALES

## `D-01` · La sección `(g)`: qué se aprueba, y con qué forma

> **Ésta es la primera puerta.** El corpus la identifica como la presión que **bloquea todo
> el estado durable**, y con él casi toda la construcción posterior. Mientras no se
> responda, no se puede construir el estado, ni el runtime, ni la iniciativa, ni la
> cobertura, ni el nivel Operativo.

**LA PREGUNTA, EN CLARO.** ADS necesita decidir **cómo se guarda su memoria en disco**: en
cuántos ficheros, cómo se parten, qué pasa si se corta la luz a mitad de una escritura, si
hay un diario de lo ocurrido y cómo se recupera. Eso ya está **diseñado** con mucho detalle,
pero el diseño **no tiene rango de norma**: la especificación que usted aprobó reservó esa
materia a una sección `(g)` que nunca se escribió. Un documento derivado no puede darse a sí
mismo la autoridad que su fuente reservó a otra sección. **La pregunta es qué forma le da
usted a esa sección.**

- **Por qué hay que decidirlo ahora:** es el primer nodo del orden de construcción y el
  único que está declarado bloqueado desde el principio.
- **De qué depende:** el estado durable, el runtime y el dispatcher, la iniciativa y su
  dosier, la certificación, el sujeto auditable y la cobertura, y el corte vertical de
  estado durable mínimo. Y, dentro de ella, el apartado de gobierno Git del repositorio de
  control, cuya sede ya fijó `O16`.
- **Fuente y presión:** `PN-1` y `PN-11`, en su sede única. Autoridad de origen: la
  especificación aprobada `(a)` `a.9` y `a.11`, y su resolución `O16`.

| | opción | qué es, en claro |
|---|---|---|
| **A** | **Ratificación íntegra por remisión** | Usted aprueba **el diseño entero tal como está**, sin reescribirlo, declarándolo sección `(g)`. |
| **B** | **`(g)` normativa breve + contrato derivado** ← recomendada | `(g)` fija **sólo lo que es norma** —la forma elegida, los invariantes, la relación entre el estado y su diario, y la tabla de propiedad del control repo—, y todo el detalle mecánico baja a un **contrato técnico** que `F6` construye y valida. |
| **C** | **`(g)` acotada al desbloqueo** | `(g)` aprueba **sólo lo imprescindible** para desbloquear el estado durable, y difiere expresamente el sellado, la migración y la concurrencia entre máquinas. |

**VENTAJAS · INCONVENIENTES · RIESGO**

```text
A  VENTAJA        conserva íntegra la cobertura de un diseño que ya pasó por ocho juicios
                  independientes; desbloquea sin trabajo de redacción nuevo
   INCONVENIENTE  convierte en norma un texto que vive en un directorio que el propio
                  corpus ordena RETIRAR tras F6. Una norma no puede tener por sede algo con
                  fecha de caducidad
   RIESGO         PROCEDIMENTAL ALTO. Aprobar de golpe un texto muy extenso es exactamente
                  el acto que un juicio posterior puede impugnar por no ser «expreso»

B  VENTAJA        es el reparto que USTED YA ORDENÓ en `O16` para el gobierno Git: autoridad
                  en (g), contrato derivado en F6. Aplicarlo al resto de (g) es coherente,
                  y le deja un texto que se puede leer entero antes de firmarlo
   INCONVENIENTE  exige trazar la frontera entre «norma» y «mecanismo» materia a materia,
                  y esa frontera es discutible en al menos tres puntos
   RIESGO         MEDIO. El modo de fallo conocido es corregir el derivado dejando la
                  fuente, o al revés

C  VENTAJA        mínima superficie de decisión hoy; honra que cinco parámetros sólo pueden
                  salir del uso real y no de una preferencia escrita ahora
   INCONVENIENTE  choca con DOS criterios de aceptación de la propia fase: el que exige que
                  ninguna presión quede «pendiente» sin acto, y el que exige que (g) cubra
                  las materias que su fuente le reservó
   RIESGO         NORMATIVO ALTO. Institucionaliza una segunda ronda de F5, que es la única
                  fase con autoridad para tocar material aprobado
```

**EFECTO SOBRE LA EVOLUCIÓN FUTURA.** `B` es la que menos veces obliga a volver a usted: un
cambio mecánico posterior se hace en el contrato, sin tocar material aprobado. `A` es
neutra. `C` garantiza otra ronda.

**REVERSIBILIDAD.** Las tres son reversibles **mientras no exista estado persistido**. En
cuanto exista, ninguna lo es del todo: el repositorio de control nace definitivo, y
rehacerlo exigiría migración explícita, autoridad y evidencia.

> ### ✅ RECOMENDACIÓN TÉCNICA · **OPCIÓN B**
>
> **Por cuatro razones, y ninguna es estética.** (1) La presión no exige que `(g)` contenga
> el detalle: exige que **la autoridad** vuelva a donde su fuente la puso. (2) `O16` ya
> estableció ese reparto exacto —norma en `(g)`, contrato en `F6`— y hacer distinto el resto
> de `(g)` sería incoherente con la única resolución vigente sobre su forma. (3) `A` falla
> por un motivo concreto: la sede del diseño es un directorio que el corpus ordena retirar.
> (4) `C` sacrifica dos criterios de aceptación explícitos de la fase.
>
> **Y una condición que la recomendación lleva dentro:** la frontera se traza **antes** de
> redactar, con una regla escrita. La regla propuesta es *«es norma todo lo que, si
> cambiara, obligaría a reaprobar (a), (b) o una enmienda; es mecanismo todo lo demás»*.

**RESPUESTA MÍNIMA:** `D-01: A` · `D-01: B` · o `D-01: C`.

---

## `D-02` · Dónde vive la norma de la RAÍZ EXTERNA DE CONFIANZA

**LA PREGUNTA, EN CLARO.** Usted ya decidió, y no se vuelve a preguntar, que ADS tendrá un
verificador que **se ejecuta fuera del repositorio que verifica, con una identidad que no
puede escribir en él**, y que eso es obligatorio antes de la primera adopción real. Lo que
nadie ha decidido es **en qué documento vive esa norma**.

- **Por qué ahora:** es el único contrato de `F6` clasificado *bloqueado por dependencia*, y
  su desbloqueo depende de esta sede y de nada más.
- **De qué depende:** ese contrato, el corte vertical de la raíz externa, y por la cadena
  que usted mismo fijó, la adopción permanente de PesquerApp, la declaración de ADS
  operativo y la certificación de cualquier adaptador.
- **Fuente:** `PN-19`. Autoridad de origen: `O18`, ratificada en su proyección por `O19`.

| | opción | qué implica |
|---|---|---|
| **A** | **Dentro de `(g)`, y su contrato derivado** ← recomendada | La norma vive en la misma sección que gobierna el control repo. No toca `C7`, ni `E2`, ni la constitución. |
| **B** | **Ampliar `C7`** | El contrato Git existente crece para cubrir un sujeto nuevo. |
| **C** | **Sede nueva propia** | Una norma de raíz de confianza independiente de `(g)` y de `C7`. |

```text
A  VENTAJA        la propia presión declara que por esta vía queda RESUELTA en vez de
                  retirada; es la única que NO enmienda material aprobado, y por tanto la
                  que menos actos suyos exige. Comparte sujeto con (g): la raíz externa
                  verifica el control repo
   INCONVENIENTE  mete materia de seguridad en una sección cuyo objeto es la disposición
                  del estado; (g) crece
   RIESGO         BAJO          REVERSIBILIDAD  ALTA

B  VENTAJA        el contrato Git ya existe y ya tiene tabla de propiedad
   INCONVENIENTE  la propia presión advierte que por esta vía SÍ hay enmienda de material
                  aprobado; y choca de frente con su resolución `O16`, que dice «C7 NO
                  CAMBIA», y con `E2.4`, que acota su regla Git a las fuentes
   RIESGO         ALTO          REVERSIBILIDAD  BAJA

C  VENTAJA        separación limpia: la seguridad no queda subordinada al estado
   INCONVENIENTE  crea una sede más en un corpus cuyo defecto recurrente es la fragmentación
   RIESGO         MEDIO         REVERSIBILIDAD  MEDIA
```

**LO QUE NO ES REVERSIBLE, y hay que decirlo:** la **obligación** no lo es. Retirarla sería
volver a la alternativa que usted **rechazó expresamente**. Esta decisión es sobre la sede,
no sobre si la raíz externa existe.

> ### ✅ RECOMENDACIÓN TÉCNICA · **OPCIÓN A**
> Es la salida que la propia presión declara como cierre limpio; comparte sujeto con `(g)`;
> es la única de las tres que no enmienda material aprobado; y `B` contradice una resolución
> suya vigente, lo que obligaría a revisarla expresamente antes de poder elegirla.

**RESPUESTA MÍNIMA:** `D-02: A` · `B` · o `C`.

---

## `D-03` · Qué significa «registra reconciliación pendiente» cuando se agotan los reintentos

**LA PREGUNTA, EN CLARO.** Cuando dos procesos intentan escribir a la vez, ADS reintenta; si
se agotan los reintentos, la especificación aprobada dice que el ciclo se detiene, las
órdenes quedan intactas y **se registra «reconciliación pendiente»**. El problema: la
arquitectura define ese aviso como algo que **se deduce del diario de transacciones**, y ese
caso **no escribe nada en el diario**. Resultado: el aviso nunca se enciende, una prueba de
conformidad que usted aprobó **no puede pasarse por ninguna vía**, y un freno del despacho
nunca dispara.

- **Por qué ahora:** las tres salidas tocan sedes distintas y son incompatibles entre sí;
  elegir después obligaría a reabrir lo que se apruebe antes.
- **De qué depende:** la conformidad de esa prueba, el freno del despacho para el canal de
  órdenes, y cualquier prueba de `F6` que pretenda verificarla en verde.
- **Fuente:** `PN-17`. Material afectado: `(a)` `a.9` y su prueba `T22`, y el freno de `b.12`.

| | opción | qué implica |
|---|---|---|
| **A** | **Tercer disyunto en el aviso deducido** | El aviso pasa a deducirse también del agotamiento de reintentos — lo que obliga a que algo durable lo sostenga. |
| **B** | **Un registro que NO es estado canónico** ← recomendada | El agotamiento deja rastro en un registro operativo, fuera del estado canónico, y el aviso lo lee. |
| **C** | **Enmendar la prueba aprobada** | Se acota qué significa «registrar» en la prueba, que es material aprobado. |

```text
A  INCONVENIENTE  la especificación aprobada prohíbe expresamente modificar el estado
                  canónico en ese punto. Sostener el disyunto exige justo lo prohibido
   RIESGO         ALTO: entra en conflicto directo con el texto vigente

B  VENTAJA        cumple literalmente la prohibición —no modifica el estado canónico—, da
                  productor al aviso y hace disparable el freno, SIN enmendar (a)
   INCONVENIENTE  hay que declarar con precisión que ese registro no es estado canónico y
                  no exige abrir transacción; hacerlo mal reabriría un problema ya cerrado
   RIESGO         MEDIO       REVERSIBILIDAD  ALTA

C  VENTAJA        cierra la incoherencia por la vía más directa
   INCONVENIENTE  toca material aprobado y una prueba de conformidad que usted aprobó; es
                  la salida más cara de las tres
   RIESGO         MEDIO       REVERSIBILIDAD  BAJA
```

> ### ✅ RECOMENDACIÓN TÉCNICA · **OPCIÓN B**
> Es la única que satisface a la vez las tres restricciones vigentes: no modifica el estado
> canónico, da al aviso un productor real, y no enmienda material aprobado. `A` choca con el
> texto que dice «no modifica el estado canónico»; `C` gasta una enmienda sobre `(a)` para
> un problema que se puede cerrar sin ella.

**RESPUESTA MÍNIMA:** `D-03: A` · `B` · o `C`.

---

## `D-04` · Las reglas constitucionales `G20`–`G23` frente al nuevo circuito de arranque

**LA PREGUNTA, EN CLARO.** La constitución de ADS fija cómo arranca un proyecto: un circuito
inicial con un **gate de salida cerrado** —un plazo máximo, diez entregables obligatorios y
cuatro prohibiciones— y dice expresamente que **ese gate lo fija la constitución y no lo
puede negociar el sistema**, porque un sistema no puede aprobar sin conflicto de interés los
criterios de su propia existencia. El diseño nuevo propone **otro** circuito de arranque con
**otro** gate. **Nadie ha derogado el primero.** Hasta que usted decida, las cuatro reglas
siguen vigentes, y una instalación real tendría que satisfacer las dos cosas.

- **Por qué ahora:** bloquea la ejecución real del circuito de arranque por la ruta nueva.
- **De qué depende:** los cuatro macrocircuitos de `F6` y su fase inicial compartida.
- **Fuente:** `PN-15`, que registra la condición de cierre `C-L.2`. Material afectado: la
  constitución, vía una fila de enmienda en `a.11`.

| | opción | qué implica |
|---|---|---|
| **A** | **CONSERVAR: el circuito nuevo se subordina al gate constitucional** ← recomendada | Las cuatro reglas quedan intactas. El circuito nuevo pasa a ser **la instrumentación** de ese gate, no su sustituto. |
| **B** | **SUSTITUIR: usted fija expresamente el gate nuevo** | Se enmienda `a.11` derogando el gate anterior, y usted declara el nuevo — porque la constitución reserva esa decisión a usted y no al sistema. |
| **C** | **AJUSTAR** | Se conservan el plazo y las cuatro prohibiciones, y se sustituye sólo la lista de diez entregables por las salidas del circuito nuevo. |

```text
A  VENTAJA        es la salida que la propia presión declara «legítima y que NO exige
                  rediseñar» el circuito nuevo. Coste de decisión mínimo, y respeta la
                  regla de que el sistema no fija su propio criterio de aprobación
   INCONVENIENTE  el circuito nuevo carga con un plazo y diez entregables que no fueron
                  pensados para él; hay que demostrar la correspondencia entregable a
                  entregable
   RIESGO         BAJO        REVERSIBILIDAD  ALTA

B  VENTAJA        deja un solo gate, sin correspondencias que mantener
   INCONVENIENTE  es la opción que más material constitucional toca, y exige que usted
                  redacte el gate nuevo con su plazo, sus entregables y sus prohibiciones:
                  el sistema no puede hacerlo por usted
   RIESGO         ALTO        REVERSIBILIDAD  BAJA

C  VENTAJA        conserva las garantías que de verdad protegen —plazo y prohibiciones— y
                  moderniza sólo la lista de salidas
   INCONVENIENTE  es la que exige el trabajo más fino: hay que decidir regla a regla y
                  demostrar que ninguna garantía se pierde por el camino
   RIESGO         MEDIO       REVERSIBILIDAD  MEDIA
```

**LAS CUATRO PREGUNTAS QUE SU RESPUESTA CIERRA** (la sede las formula así, y la prueba
posterior exige **una fila por regla**, no una respuesta global):

```text
1  ¿el gate de salida del circuito inicial sigue siendo el constitucional, o pasa a ser el
   nuevo? Y si pasa, ¿quién lo fija, dado que la constitución dice que no puede fijarlo el
   sistema?
2  ¿el plazo máximo sobrevive, se ajusta o se retira?
3  ¿los diez entregables obligatorios sobreviven, y cómo se corresponden con las salidas
   del circuito nuevo?
4  ¿las reglas de macrocircuitos y de línea base quedan intactas, ajustadas o sustituidas?
```

> ### ✅ RECOMENDACIÓN TÉCNICA · **OPCIÓN A**
> Es la salida que la propia sede declara legítima y barata, y la única que **no reintroduce
> el conflicto de interés** que la regla existe para evitar: bajo `A`, el criterio que
> aprueba la existencia del sistema lo sigue fijando la constitución. `B` es defendible pero
> le traslada a usted la redacción íntegra de un gate nuevo. `C` es la más costosa de
> verificar y la que más superficie deja para una incoherencia.

**RESPUESTA MÍNIMA:** `D-04: A` · `B` · o `C`. Con `B` o `C`, hace falta además su respuesta
a las cuatro preguntas de arriba.

---

## `D-05` · La vía por la que nace el trabajo que usted no pidió uno a uno

**LA PREGUNTA, EN CLARO.** Usted aprobó que las auditorías se abran **por política**: por
evento, riesgo, recurrencia y caducidad, con alcance, presupuesto y revocación declarados.
Pero la especificación de recorrido dice que **el trabajo nace de una entrada suya o de un
desbloqueo dentro de lo ya autorizado**, y una política de recurrencia es una **tercera
vía** que no está contemplada. En paralelo, la constitución tiene una regla que limita la
ejecución desatendida y que nadie ha ajustado al alcance que su política autoriza.

- **Por qué ahora:** sin la vía, el paso que **abre** trabajo automáticamente no tiene
  respaldo normativo. La sustancia ya la decidió usted; falta el vehículo.
- **De qué depende:** el paso de apertura automática del sistema de cobertura.
- **Fuente:** `PN-2` y `PN-3` — el corpus las declara **la misma pregunta por dos caminos**,
  y por eso van juntas y se aplican en un solo acto.

| | opción | qué implica |
|---|---|---|
| **A** | **Reconocer la tercera vía** ← recomendada | Se enmienda el recorrido para reconocer la política de recurrencia como fuente de trabajo, y se añade una fila que ajusta la regla constitucional **al alcance exacto** que su política autoriza, conservando el resto. |
| **B** | **No ampliar la taxonomía** | Se declara que la política opera **dentro** del alcance ya autorizado, sin tercera vía y sin tocar la regla constitucional. |

```text
A  VENTAJA        hace explícito lo que su resolución ya autoriza, y deja la regla
                  constitucional ajustada y NO levantada en bloque
   INCONVENIENTE  enmienda material aprobado en dos sedes
   RIESGO         BAJO      REVERSIBILIDAD  MEDIA

B  VENTAJA        no toca material aprobado
   INCONVENIENTE  obliga a sostener que abrir una auditoría por recurrencia es «dentro del
                  alcance ya autorizado», lo que la sede declara que NO es. Deja el paso de
                  apertura sin respaldo, y el problema vuelve en F6
   RIESGO         MEDIO     REVERSIBILIDAD  ALTA
```

> ### ✅ RECOMENDACIÓN TÉCNICA · **OPCIÓN A**
> Su resolución ya decidió la sustancia; negarle la vía deja una capacidad autorizada sin
> norma que la sostenga. Y el ajuste de la regla constitucional se hace **acotado**, que es
> justo lo que impide levantarla en bloque.

**RESPUESTA MÍNIMA:** `D-05: A` · o `B`.

---

## `D-06` · Quién emite el dictamen en la ruta de auditoría

**LA PREGUNTA, EN CLARO.** La ruta de **auditoría de un proyecto existente** declara sus
participantes obligatorios, y la capacidad de **verificación** no figura ni siquiera como
opcional. Pero el diseño nuevo exige un **dictamen de verificación** como evidencia para que
una casilla de cobertura pueda darse por verificada. **Ninguna ruta produce hoy ese
dictamen.**

- **De qué depende:** que una casilla de cobertura alcance «verificado» **con evidencia**.
  El inventario, la detección y la propuesta funcionan sin esto.
- **Fuente:** `PN-8`. Material afectado: la tabla de rutas de `(b)`.

| | opción | qué implica |
|---|---|---|
| **A** | **Añadir verificación como participante condicional** ← recomendada | La ruta de auditoría puede incorporar verificación cuando su condición se cumpla. |
| **B** | **Nombrar otro productor** | Se deja de exigir dictamen de verificación en esa casilla, y se declara qué capacidad lo produce en su lugar. |

```text
A  VENTAJA        cierra el hueco por donde está abierto, con el participante que el diseño
                  ya nombra. Cambio mínimo sobre la tabla
   INCONVENIENTE  enmienda material aprobado
   RIESGO         BAJO      REVERSIBILIDAD  ALTA

B  VENTAJA        no añade participantes a una ruta aprobada
   INCONVENIENTE  obliga a nombrar OTRO productor del dictamen y a justificar por qué es
                  competente; si no aparece ninguno, la casilla queda sin evidencia posible
   RIESGO         MEDIO     REVERSIBILIDAD  ALTA
```

> ### ✅ RECOMENDACIÓN TÉCNICA · **OPCIÓN A**
> El diseño ya nombra a verificación como la que emite ese dictamen, y no hay otra capacidad
> con esa autoridad. `B` exige inventar un productor donde el corpus no tiene ninguno.

**RESPUESTA MÍNIMA:** `D-06: A` · o `B`.

---

## `D-07` · Quién participa en la puesta en marcha de un producto nuevo

**LA PREGUNTA, EN CLARO.** El circuito de instalación tiene un paso de **descubrimiento de
producto, dominio y diseño**, anterior al gate de «listo para construir». Pero los dos
procesos por los que ese paso puede entrar **no admiten a dominio, seguridad ni diseño**, ni
siquiera como participantes opcionales. La ruta que sí los admite exige **un objeto ya
existente**, y en una instalación nueva no lo hay.

- **De qué depende:** que el paso de descubrimiento pueda abrirse con dominio y diseño, y
  que el paso de arranque incorpore el dictamen de seguridad.
- **Fuente:** `PN-13`. Material afectado: dos filas de la tabla de rutas de `(b)`.

| | opción | qué implica |
|---|---|---|
| **A** | **Añadirlos como participantes condicionales** ← recomendada | Los dos procesos admiten dominio, seguridad y diseño cuando su condición se cumpla. |
| **B** | **Sacar el descubrimiento de ese paso** | Se declara que el descubrimiento de dominio y diseño de un producto nuevo **no pertenece** a ese paso, y se nombra dónde pertenece. |

```text
A  VENTAJA        resuelve el hueco sin mover el diseño de circuitos, y con el mismo
                  mecanismo —participante condicional— que otras rutas ya usan
   INCONVENIENTE  enmienda material aprobado en dos filas
   RIESGO         BAJO      REVERSIBILIDAD  ALTA

B  VENTAJA        no toca la tabla de rutas
   INCONVENIENTE  la propia sede declara el coste: el gate de «listo para construir» se
                  superaría SIN modelo de dominio. Y obliga a nombrar otro sitio para el
                  descubrimiento, que hoy no existe
   RIESGO         ALTO      REVERSIBILIDAD  MEDIA
```

> ### ✅ RECOMENDACIÓN TÉCNICA · **OPCIÓN A**
> `B` tiene un coste que la propia sede escribe: aprobar «listo para construir» sin modelo
> de dominio. `A` usa un mecanismo que la tabla ya emplea en otras rutas.

**RESPUESTA MÍNIMA:** `D-07: A` · o `B`.

---

## `D-08` · La grafía canónica de dos identificadores, respondida con UN solo criterio

> **Estas dos van JUNTAS a propósito.** Responderlas por separado permite una respuesta
> incoherente —«manda la fuente para uno, manda el kernel para el otro»— que dejaría sin
> criterio la comprobación de grafía única. Es la agrupación que más trabajo futuro ahorra.

**LA PREGUNTA, EN CLARO.** Dos identificadores normativos se escriben de dos maneras. En un
caso, la especificación aprobada lo escribe **con tilde** y todo lo derivado **sin tilde**.
En el otro, la especificación lo escribe con tilde en sus doce apariciones, y **el kernel ya
construido usa las dos a la vez**. Ninguna sede dice cuál manda. Mientras nadie lo diga, no
se puede exigir una sola grafía en ningún sitio.

- **Por qué ahora:** `F6` tendrá que **escribir** esos identificadores, y no puede elegir la
  grafía por su cuenta.
- **De qué depende:** la materialización de esos identificadores, y la comprobación de
  grafía única, que hoy no puede exigir nada.
- **Fuente:** `PN-16` y `PN-18`. Material afectado: `(b)`.

| | opción | qué implica |
|---|---|---|
| **A** | **Manda la fuente aprobada: CON TILDE** ← recomendada | **No se enmienda `(b)`.** `F6` alinea todo lo derivado y el kernel construido a la grafía con tilde. |
| **B** | **Manda la grafía SIN TILDE** | Se enmienda `(b)` en las apariciones afectadas, y `F6` alinea lo poco que quede desalineado. |

```text
A  VENTAJA        respeta la regla de precedencia del propio corpus —la fuente aprobada
                  manda sobre el derivado—, y cierra las dos presiones SIN gastar una
                  enmienda sobre material aprobado. La primera queda RESUELTA en vez de
                  retirada, que es la salida que su sede describe
   INCONVENIENTE  obliga a F6 a tocar más sitios: catorce de diecisiete apariciones del
                  kernel y los packs cambian
   RIESGO         BAJO      REVERSIBILIDAD  ALTA

B  VENTAJA        menos ficheros que tocar en el kernel construido
   INCONVENIENTE  enmienda material aprobado para adaptarlo a su propio derivado, que es
                  invertir la regla de precedencia del corpus. Y hay que enmendar las doce
                  apariciones normativas, no una
   RIESGO         MEDIO     REVERSIBILIDAD  MEDIA
```

> ### ✅ RECOMENDACIÓN TÉCNICA · **OPCIÓN A**
> La jerarquía de autoridad del corpus dice que el material aprobado manda sobre lo
> derivado. Elegir `B` sería enmendar la fuente para que se parezca a su copia, y sentaría
> precedente para cualquier discrepancia futura del mismo tipo. El coste de `A` es trabajo
> mecánico de `F6`, que es trabajo barato y verificable.

**RESPUESTA MÍNIMA:** `D-08: A` · o `B`. Se aplica a los DOS identificadores.

> **Y una salida que este paquete NO le cierra, aunque no la recomiende.** Agruparlas es una
> decisión de presentación, **no** una restricción normativa: son dos identificadores
> distintos y ninguna autoridad vigente le obliga a responderlos igual. Si quiere criterios
> distintos, escríbalo —`D-08: A para el primero, B para el segundo`— y se aplicará. Se
> agrupan porque una respuesta dividida deja la comprobación de grafía única sin criterio
> general, no porque usted no pueda darla.

---

## `D-09` · Un método nombrado donde debería ir una capacidad

**LA PREGUNTA, EN CLARO.** En dos puntos del material aprobado se nombra como participante
algo que **no es un participante**: es uno de los seis **métodos** de la capacidad de
diseño. Nombrar el método en la ruta **predetermina** lo que otra regla prohíbe
predeterminar: cuál se ejecuta lo calcula una escala de novedad, no lo elige la ruta.

- **Por qué no basta corregir el kernel:** la misma cadena está en material aprobado. Tocar
  sólo lo derivado dejaría la fuente diciendo lo contrario — que es el modo de fallo que el
  corpus registra expresamente.
- **De qué depende:** que la composición de esa ruta sea verificable mecánicamente **contra
  la fuente**.
- **Fuente:** `PN-14`. Material afectado: `(a)` y `(b)`, un punto en cada uno.

| | opción | qué implica |
|---|---|---|
| **A** | **Sustituir por la capacidad, con su condición** ← recomendada | En los dos puntos aprobados se nombra la capacidad de diseño con su condición, y se declara que el método lo calcula la escala de novedad. |
| **B** | **No tocar `(a)` ni `(b)`** | Se declara expresamente que las dos formas designan al mismo participante. |

```text
A  VENTAJA        deja fuente y derivado diciendo lo mismo, y devuelve a la escala de
                  novedad la elección que le corresponde. Es la única que hace verificable
                  la composición contra la fuente
   INCONVENIENTE  enmienda material aprobado en dos puntos
   RIESGO         BAJO      REVERSIBILIDAD  ALTA

B  VENTAJA        la propia sede la declara «legítima y más barata»: no toca material
                  aprobado
   INCONVENIENTE  conserva en la norma un nombre que predetermina un método, y deja la
                  comprobación mecánica contra la fuente sin poder ejecutarse
   RIESGO         MEDIO     REVERSIBILIDAD  ALTA
```

> ### ✅ RECOMENDACIÓN TÉCNICA · **OPCIÓN A**
> `B` es legítima y más barata hoy, y la sede lo dice. Pero deja viva la causa —un método
> nombrado donde va una capacidad— y con ella la imposibilidad de comprobar la composición
> contra su fuente. `A` cuesta dos líneas y cierra la clase entera.

**RESPUESTA MÍNIMA:** `D-09: A` · o `B`.

---

## `D-10` · El «mapa documental»: ¿derivado, o escrito y mantenido?

**LA PREGUNTA, EN CLARO.** Usted resolvió que doce áreas semánticas son **obligatorias como
materia y no como ficheros**. Al restituirlas, el diseño declara que una de ellas —el mapa
documental— **se deriva** en vez de escribirse: se regenera desde el corpus. Eso es una
precisión sobre su resolución, y por eso se le pregunta en vez de darla por buena.

- **Por qué ahora:** con la lectura derivada, `F6` puede construir los doce contratos de
  aspecto sin esperar a nada.
- **De qué depende:** hoy no bloquea nada. Si usted exige un mapa escrito, esa área pasa a
  tener responsable y caducidad propios.
- **Fuente:** `PN-12`. Autoridad de origen: su resolución `O8`.

| | opción | qué implica |
|---|---|---|
| **A** | **Se satisface DERIVADO** ← recomendada | El mapa se regenera desde el corpus. Nadie lo mantiene a mano y no puede quedarse obsoleto en silencio. |
| **B** | **Un mapa escrito y mantenido** | El área pasa a tener responsable declarado y caducidad propia. |

```text
A  VENTAJA        un mapa derivado no envejece, que es exactamente el defecto que el corpus
                  persigue por diseño. Coste de mantenimiento cero
   INCONVENIENTE  exige que el derivador exista y esté cubierto; hasta entonces el área no
                  tiene autoridad asignada
   RIESGO         BAJO      REVERSIBILIDAD  ALTA

B  VENTAJA        el mapa existe desde el primer día, sin depender de ninguna herramienta
   INCONVENIENTE  un mapa escrito a mano al lado de una sede que crece caduca solo. Es la
                  clase de defecto que el corpus tiene abierta y sin cerrar
   RIESGO         MEDIO     REVERSIBILIDAD  ALTA
```

> ### ✅ RECOMENDACIÓN TÉCNICA · **OPCIÓN A**
> Su resolución dice «obligatorias como materia y no como ficheros», y un mapa derivado
> satisface la materia sin crear un fichero que envejece. `B` reintroduce por la puerta de
> atrás la clase de defecto que el corpus persigue.

**RESPUESTA MÍNIMA:** `D-10: A` · o `B`.

---

# PARTE 2 · ACTOS DE APROBACIÓN

> **Aquí NO se le presentan opciones**, porque no las hay: el contenido está determinado por
> una autoridad vigente. Lo que falta es su acto, porque el material es APROBADO y nada se
> aplica sobre él sin aprobación expresa suya. Inventar alternativas para simular una
> elección sería exactamente lo que este paquete tiene prohibido hacer.

## `R-01` · Cuatro lecturas de una frase, y una retirada que se confirma

**QUÉ SE APRUEBA.** Cuatro precisiones que **no cambian ninguna norma** y que se registran
porque reinterpretar la lectura de una resolución suya, o del dominio de un predicado
aprobado, es materia suya y no del sistema:

```text
· que «Integrada» significa lo que el diseño deriva, para un producto de una sola fuente
· que la reanudación distingue lo PUBLICADO de lo ESPECULATIVO: completar, o revertir las
  escrituras especulativas a su revisión base, registrar el incidente y escalar — SIN
  autorizar la reversión de estado ya publicado. No hay un tercer desenlace normativo
· que consumir el resultado de la especificación de recorrido NO redefine su dominio, por
  la misma vía por la que una presión anterior se retiró tras comprobarlo
· que «estado durable» de la iniciativa se lee como el diseño ya lo deriva
```

**Y una confirmación añadida:** que la presión retirada en su día **no se reinstaura**. Su
sede la declara «reinstaurable por `F5` si el Owner lo prefiere», de modo que `F5` tiene que
decir que no la reinstaura, en vez de callarlo.

- **Fuente:** `PN-6`, `PN-7`, `PN-9`, `PN-10`, y la nota de `PN-4`.
- **Por qué no es una elección:** para tres de ellas, ninguna sede sostiene la lectura
  contraria; lo que falta es el acto, no el criterio.
- **La salvedad, dicha en vez de disimulada:** para la cuarta —«estado durable» de la
  iniciativa— su sede pide fijar **cuál de las dos lecturas rige**, y llama a la elegida
  «defendible y **probablemente** correcta». Ahí sí hay dos lecturas, y sólo usted puede
  fijar cuál. Se agrupa aquí porque la lectura contraria no la sostiene ninguna sede **y**
  porque la respuesta esperada es la misma; **si prefiere reabrirla, nómbrela**.
- **Borrador preparado:** [`borradores/B-05-RATIFICACIONES-DE-LECTURA.md`](borradores/B-05-RATIFICACIONES-DE-LECTURA.md)

**RESPUESTA MÍNIMA:** `R-01: APRUEBO` · o `NO APRUEBO`, nombrando cuál de las cuatro quiere
reabrir.

---

## `R-02` · La checklist editorial sobre material aprobado

**QUÉ SE APRUEBA.** Correcciones cuyo texto final es **calculable sin decidir nada**, y que
**no cambian ninguna norma**:

```text
· una cita a un predicado equivocado en el recorrido aprobado: dice (P7) y el predicado que
  describe es (P9). El propio documento ya lo usa bien unas líneas antes
· una lista numerada 1, 2, 5, 3, 4 que pasa a 1, 2, 3, 4, 5, conservando el texto de cada
  regla SIN TOCAR UNA PALABRA, y comprobando antes que ninguna sede las cita por su número
· un recuento de marcas de remisión que el árbol no da: se marcan los dos recuentos sin
  marcar y, sobre todo, el cardinal escrito a mano se SUSTITUYE POR SU COMANDO DE
  DERIVACIÓN, para que la fila no pueda volver a caducar
· el inventario de enmiendas vigentes, que hoy NO coincide entre las sedes que lo enumeran:
  unas nombran una enmienda y otras dos, y el recorrido aprobado está enmendado y no lo
  dice en ninguna parte de su propio texto
```

- **Fuente:** la checklist editorial de la sede, más la observación `OC-2` que el corpus
  registra con fase `F5`.
- **Por qué necesita su acto:** sólo `F5` puede tocar el material aprobado, y su autoridad
  declarada es «`F5`, con aprobación del Owner».
- **Advertencia honesta:** la cuarta fila de la checklist **no** está aquí. Es la grafía, y
  es una elección real: está en `D-08`.
- **Borrador preparado:** [`borradores/B-09-CHECKLIST-EDITORIAL.md`](borradores/B-09-CHECKLIST-EDITORIAL.md)

**RESPUESTA MÍNIMA:** `R-02: APRUEBO` · o `NO APRUEBO`.

---

## `R-03` · La nota de vigencia en su documento de trabajo

**QUÉ SE APRUEBA.** Su documento de trabajo sobre la arquitectura multirrepositorio dice, en
cuatro sitios distintos, **«no implementar sin diseño previo»** y **«no implementar
todavía»**. Mientras tanto, los contratos multirrepositorio **ya implementan** esa materia,
y usted la aprobó por otra vía. Las dos posturas están registradas y la contradicción sigue
abierta.

**Es su documento, y la nota es suya.** El borrador está redactado para que usted lo adopte,
lo corrija o lo sustituya por su propio texto — **no para aplicarlo sin usted**.

- **Cobertura:** el borrador cubre **las cuatro** afirmaciones equivalentes, no sólo la que
  el hallazgo nombra. Una nota que tocara una sola dejaría vivas tres idénticas.
- **Fuente:** el hallazgo externo con propietario «el Owner» y fase `F5`.
- **Borrador preparado:** [`borradores/B-10-NOTA-DE-VIGENCIA.md`](borradores/B-10-NOTA-DE-VIGENCIA.md)

**RESPUESTA MÍNIMA:** `R-03: APRUEBO` · `APRUEBO CON CAMBIOS` (con su texto) · o `NO APRUEBO`.

---

## `R-04` · Cómo se inscriben sus respuestas

**QUÉ SE APRUEBA.** Dónde y cómo quedan registrados **el acto por el que usted inició `F5`**
y las respuestas de este paquete.

Su sede canónica de resoluciones es **APPEND-ONLY** y **sólo usted escribe en ella**: una
comprobación mecánica verifica que su contenido de hoy empieza por el contenido de la
versión que la creó, y la referencia **no es el estado actual, sino el nacimiento**, de modo
que confirmar una alteración no la vuelve legítima. **Ningún agente ha escrito nunca en esa
sede, y este macrobloque tampoco.**

Pero el criterio de aceptación `A2` exige que ninguna enmienda se aplique sin aprobación
**expresa** suya, y lo comprobable es que cada enmienda cite una resolución que exista en
esa sede. Hace falta saber por qué vía llegan sus respuestas allí.

| | opción | qué implica |
|---|---|---|
| **A** | **El siguiente macrobloque prepara el texto, usted lo inscribe** ← recomendada | El acto de inicio y sus respuestas se convierten en el texto de una resolución con sus campos —identificador, fecha, procedencia, texto, alcance y relaciones de revisión— y **usted** la pega en su sede. Ningún agente escribe en ella. |
| **B** | **Usted escribe las entradas directamente** | Sin intermediación. |

> ### ✅ RECOMENDACIÓN TÉCNICA · **OPCIÓN A**
> Conserva intacta la propiedad que hace auditable la sede —que sólo usted escriba en ella—
> y le ahorra redactar los campos obligatorios. El texto se le entrega para que lo revise
> antes de inscribirlo; no se inscribe solo.

**RESPUESTA MÍNIMA:** `R-04: A` · o `B`.

---

## `R-05` · Quién cierra `F5`

**LA PREGUNTA, EN CLARO.** Cuando las catorce respuestas estén aplicadas y los siete
criterios de aceptación se comprueben, **alguien tiene que declarar `F5` cerrada**. Y hoy
**ninguna sede vigente dice quién**.

> **POR QUÉ ESTÁ AQUÍ, dicho contra el interés de quien escribe.** Este macrobloque llegó a
> escribir en el corpus canónico que cerrar `F5` era «acto del Owner por la misma razón que
> su inicio». **Era una inferencia, no una derivación, y se ha retirado.** El precedente
> apunta en la otra dirección: `F4c` **no la cerró el Owner** — la cerró la **composición de
> dos juicios independientes**, y su propia sede subraya que «no la cerró el coordinador».
> Escribir esa regla sin autoridad era exactamente el defecto que este paquete existe para
> evitar, y por eso la pregunta viene aquí en vez de quedarse contestada sola.

- **Por qué ahora:** para que el siguiente macrobloque no tenga que volver a preguntarlo al
  llegar al final de `F5`. No bloquea nada hasta entonces.
- **De qué depende:** el cierre de `F5`, y con él el inicio de `F6`, que exige `F5` cerrada.
- **Fuente:** la ausencia. Ninguna sede vigente lo fija, y los dos precedentes del corpus
  —el inicio de `F5`, que es acto suyo, y el cierre de `F4c`, que fue por composición— apuntan
  a salidas distintas.

| | opción | qué implica |
|---|---|---|
| **A** | **Acto del Owner** ← recomendada | Usted declara `F5` cerrada, por simetría con su inicio. `F5` no construye software: redacta norma y registra su aprobación, y quien aprueba la norma es usted. |
| **B** | **Composición de juicios independientes** | Como se cerró `F4c`: un juicio independiente comprueba `A1`…`A7` y la composición cierra la fase. |

```text
A  VENTAJA        F5 entrega NORMA APROBADA, y la autoridad que la aprueba es la suya.
                  Comprobar A1…A7 es mecánico y no exige juicio adversarial: cada criterio
                  tiene una prueba derivable. Barato y sin ciclo nuevo
   INCONVENIENTE  quien aprueba las enmiendas es también quien declara cerrada la fase que
                  las produjo
   RIESGO         BAJO        REVERSIBILIDAD  ALTA

B  VENTAJA        replica el precedente de F4c, y separa a quien produce de quien cierra
   INCONVENIENTE  abre un ciclo de verificación con su aparato completo para comprobar
                  criterios que en su mayoría son barridos mecánicos. Y la resolución que
                  abrió aquella vía declaró que NO deja otro ciclo
   RIESGO         MEDIO       REVERSIBILIDAD  ALTA
```

> ### RECOMENDACIÓN TÉCNICA · **OPCIÓN A**
> `F4c` se cerró por composición porque lo que se juzgaba era **cobertura de una
> verificación**, y ahí quien construye no puede certificarse. `F5` entrega **norma
> aprobada por usted**: los siete criterios se comprueban por barrido derivado, no por
> juicio. `B` gasta un aparato de gate completo en comprobar lo que un comando comprueba.

**RESPUESTA MÍNIMA:** `R-05: A` · o `B`.

---

# 3 · Plantilla de respuesta

**Copie y rellene.** Con esto el siguiente macrobloque puede aplicarlo **todo** sin volver a
preguntar — también si elige una opción no recomendada, porque la plantilla recoge el dato
adicional que cada una necesita.

```text
D-01: _   (A ratificación íntegra · B (g) breve + contrato · C acotada)
          si B → confirme la regla de frontera norma/mecanismo, o dé la suya
D-02: _   (A en (g) y su contrato · B ampliar C7 · C sede nueva)
          si C → nombre la sede nueva
D-03: _   (A tercer disyunto · B registro no canónico · C enmendar la prueba)
          si B → diga dónde vive ese registro
D-04: _   (A conservar · B sustituir · C ajustar)
          si B o C → las cuatro respuestas de la lista de D-04
D-05: _   (A reconocer la tercera vía · B no ampliar)
D-06: _   (A verificación condicional · B otro productor)
          si B → nombre la capacidad que produce el dictamen
D-07: _   (A añadir condicionales · B sacar el descubrimiento)
          si B → nombre dónde pertenece el descubrimiento
D-08: _   (A con tilde, manda la fuente · B sin tilde, se enmienda)
          puede responder distinto para cada identificador si lo prefiere
D-09: _   (A sustituir por la capacidad · B declarar equivalencia)
D-10: _   (A derivado · B escrito y mantenido)

R-01: APRUEBO / NO APRUEBO      si NO → nombre cuál de las cuatro reabre
R-02: APRUEBO / NO APRUEBO
R-03: APRUEBO / APRUEBO CON CAMBIOS / NO APRUEBO
R-04: _   (A el texto se le prepara · B usted escribe)
R-05: _   (A acto del Owner · B composición de juicios independientes)
```

**Las líneas indentadas sólo hacen falta si elige la opción que las pide.** Con las opciones
recomendadas, un renglón por asunto basta.

---

## 4 · Dónde comprobar cada afirmación de este documento

**Ninguna afirmación de aquí le pide que se fíe.** Éstas son las rutas exactas, para que
pueda verificar lo que se le pide firmar sin depender de este documento.

| lo que quiera comprobar | dónde está |
|---|---|
| qué es `F5`, sus siete entregables y sus siete criterios | [`05-PLAN-DE-IMPLEMENTACION-F5-F6.md`](../canonico/05-PLAN-DE-IMPLEMENTACION-F5-F6.md) §1.1 y §1.2 |
| las presiones, una a una, con qué presiona cada una y qué bloquea | [`11-ARQUITECTURA-INTEGRADA.md`](../evolucion/11-ARQUITECTURA-INTEGRADA.md) §16 |
| la checklist editorial y los hallazgos externos con propietario | ídem, §19 |
| los contratos de `F6` y la condición exacta de desbloqueo del bloqueado | ídem, §20 y §20.4 |
| sus propias resoluciones, íntegras | [`docs/owner/ADS-OWNER-RESOLUCIONES.md`](../owner/ADS-OWNER-RESOLUCIONES.md) |
| las resoluciones anteriores a esa sede, en su registro histórico | [`DECISIONES-Y-CONTRADICCIONES.md`](../rediseno/DECISIONES-Y-CONTRADICCIONES.md) §2 |
| el material aprobado que las enmiendas tocarían | [`a-CAPACIDADES-APROBADA.md`](../rediseno/a-CAPACIDADES-APROBADA.md) · [`b-RECORRIDO-APROBADA.md`](../rediseno/b-RECORRIDO-APROBADA.md) |
| las enmiendas ya existentes, y el patrón que las nuevas siguen | [`a-ENMIENDA-E1-ENC.md`](../rediseno/a-ENMIENDA-E1-ENC.md) · [`a-ENMIENDA-E2-MULTIREPO.md`](../rediseno/a-ENMIENDA-E2-MULTIREPO.md) |
| las reglas constitucionales que `D-04` decide | [`kernel/KERNEL.md`](../../kernel/KERNEL.md) |
| su documento de trabajo, que `R-03` toca | [`ADS-IDEAS-PENDIENTES-MULTIREPO.md`](../owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md) |
| el estado vigente de las fases, en su **única** sede | [`03-GOBIERNO-Y-AUTORIDAD.md`](../canonico/03-GOBIERNO-Y-AUTORIDAD.md) §6 |
| la deuda viva, con propietario, fase y condición de cierre | [`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](../canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md) |
| la fila de matriz que respalda cada decisión de aquí | [`MATRIZ-F5.yml`](MATRIZ-F5.yml), campo `decision_id` |

> **Y una regla que este documento respeta:** ningún documento de gate, dictamen o
> manifiesto se cita aquí como fuente de una obligación, **ni siquiera cuando dice algo
> verdadero**. Toda obligación de este paquete tiene sede en la especificación aprobada, en
> una resolución suya, o en la arquitectura entregada — y es esa sede la que se enlaza.

---

## 5 · Lo que este documento NO hace

```text
NO APRUEBA        ninguna de sus opciones. Ninguna está ejecutada
NO INVENTA        ninguna respuesta suya. No hay ni una decisión dada por tomada
NO REABRE         F4c, ni la consolidación canónica, ni ninguna resolución O1–O22
NO INICIA         F6, y no desbloquea PesquerApp
NO DECLARA        superado ningún hallazgo vivo, ninguna condición de cierre, ni M-04
NO PRESENTA       como abierto nada que una autoridad vigente ya haya resuelto
```
