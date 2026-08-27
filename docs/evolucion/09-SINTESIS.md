# F3 — SÍNTESIS

Fase **F3** del [plan](04-PLAN-DE-INVESTIGACION.md) y trabajo **23.4** de la
[directiva](ADS-NEXT-OWNER-BRIEF.md). Compara, en una sola lectura, cuatro materiales que
hasta ahora estaban separados:

```text
ADS ACTUAL          el corpus vigente: quince capacidades, diez procesos, siete contratos,
                    diecinueve esquemas, tres packs y los validadores que los comprueban
LA DIRECTIVA        veintiséis apartados del brief, más las decisiones del Owner posteriores
LOS CANDIDATOS      29 fichas de PesquerApp con procedencia, y sus 29 veredictos
LO PENDIENTE        el documento vivo de trabajo con el Owner, que amplía todo lo anterior
```

## Qué hace esta fase, y qué no

```text
HACE      relaciona, fusiona, separa, encoge y contradice. Cada conclusión enlaza el
          candidato, el problema o la regla de la que sale.
HACE      propone resolución para X1–X5, que es la puerta que el plan exige para cerrar F3.
HACE      registra las contradicciones nuevas que la comparación descubre, sin resolverlas
          cuando su resolución no es técnica.

NO HACE   arquitectura integrada. Eso es F4, y su puerta es la crítica independiente.
NO HACE   enmiendas a (a), (b), E1 ni E2. Eso es F5, y su puerta es el Owner.
NO HACE   kernel, packs, runtime, tooling, esquemas, agentes, skills, validadores ni
          migraciones. Eso es F6.
NO HACE   aceptar el documento de pendientes propuesta a propuesta. Aceptar mecánicamente
          una lista es exactamente lo que la regla 1 de la directiva prohíbe.
```

**Ningún fichero de `kernel/operativo/`, `packs/` ni `docs/rediseno/` cambia en F3.**

## El material, y con qué autoridad entra

| material | autoridad | qué aporta |
|---|---|---|
| [`ADS-NEXT-OWNER-BRIEF.md`](ADS-NEXT-OWNER-BRIEF.md) | directiva del Owner | los veintiséis apartados y las doce reglas de interpretación |
| [`ADS-ARQUITECTURA-MULTIREPO-APROBADA.md`](../../ADS-ARQUITECTURA-MULTIREPO-APROBADA.md) | decisión aprobada, ya implementada | `D1`–`D10`, `N1`–`N14`, `I1`–`I10`, `CA-1`–`CA-17` |
| [`ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md`](ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md) | **material temporal de evolución** | principios que el Owner declara aceptados, propuestas todavía abiertas y problemas por sintetizar |
| [`05-CANDIDATOS.md`](05-CANDIDATOS.md) | inventario con procedencia | 29 candidatos de PesquerApp, con evidencia de uso |
| [`06-CONTRASTE.md`](06-CONTRASTE.md) | veredictos | 29 lecturas contra el corpus, y `P-01`–`P-06` |
| [`07-DECISION-MULTIREPO.md`](07-DECISION-MULTIREPO.md) | registro | la contradicción resuelta por el Owner, y `P-07` |
| [`08-EVIDENCIA-MULTIREPO.md`](08-EVIDENCIA-MULTIREPO.md) | matriz de evidencia | qué está demostrado del modelo multi-repo, y qué no |
| [`02-MAPA-DIRECTIVA.md`](02-MAPA-DIRECTIVA.md) | mapa | los veredictos por apartado y las contradicciones `X1`–`X5` |
| [`03-INVARIANTES.md`](03-INVARIANTES.md) | invariantes | qué no se modifica en silencio, y por qué vía |
| `kernel/operativo/` · `packs/` | corpus vigente | leído por identificador, no de memoria |

> **El documento de pendientes es material temporal.** Sus principios aceptados por el Owner
> se tratan aquí como dirección de diseño; sus propuestas, como propuestas. No se copia su
> contenido en ningún otro fichero, y el gate de higiene que él mismo propone en su §26.25 lo
> alcanza a él primero.

## Los siete veredictos de esta fase

```text
ACEPTADA        la síntesis sostiene el principio o la dirección, y entra en F4 tal cual.
FUSIONADA       se une a otra propuesta, a un candidato o a una pieza que ya existe.
                Deja de existir por separado.
YA EXPRESABLE   se expresa con capacidades, procesos, contratos o esquemas vigentes.
                No crea pieza nueva. La regla que lo exige es del propio documento: antes
                de crear algo, comprobar si lo existente ya lo dice.
REDUCIDA        se acepta la necesidad y se rechaza el tamaño. Entra encogida, y lo que
                se retira queda escrito.
RECHAZADA       no entra, con su motivo.
OWNER           su resolución no es técnica.
DEFERIDA        la evidencia disponible no permite decidir. No es una tarea pendiente.
```

**La regla inversa también vale, y viene del mismo sitio:** dos conceptos realmente
distintos no se fusionan para reducir el recuento. Cada fusión de abajo dice qué propiedad
comparten las piezas que une.

---

# Los seis hallazgos

Son el resultado de la fase. Todo lo demás —las tablas, los veredictos, las preguntas— se
deriva de ellos.

## H1 · Los cuatro macrocircuitos son una composición, no cuatro diseños

El documento pide cuatro recorridos: instalación (`N0`–`N7`), adopción (`A0`–`A10`),
migración desde un ADS anterior (§6) y actualización de un ADS instalado (§7). Añade un
quinto para auditar el propio ADS (`E0`–`E8`), un sexto para la campaña de corrección de
`P-03` y un séptimo para el gate de higiene del corpus.

**Los siete tienen la misma forma**: fases con nombre, participantes por fase, evidencia por
fase, un gate final, y memoria que sobrevive al chat. Y ninguno de los siete necesita un
tipo de proceso nuevo. Comprobado fase a fase contra
[`recorrido/01-PROCESOS.md`](../../kernel/operativo/recorrido/01-PROCESOS.md):

| fase de `A0`–`A10` | proceso vigente que la representa |
|---|---|
| A0 apertura y perímetro | encuadre de [`entrada/`](../../kernel/operativo/entrada/00-INDICE.md), y el item que lo consume |
| A1 topología | `SIS`, con `PLT` como productora — es lo que `workspace.py` ya hace |
| A2 inventario · A3 baseline | `AUD`: *«producir una CONCLUSIÓN sobre un objeto ya existente, para que alguien decida con ella»*, con `INV` produciendo la capa |
| A4 conocimiento | `AUD` con `SIS` como consumidora de la conclusión |
| A5 especialización | `SIS` |
| A6 reconstrucción | `AUD`, y sus condicionales ya declaradas: `DOM`, `SEG`, `DIS/Reconstruccion`, `PRD` |
| A7 trabajo vivo | las nueve clases de [`entrada/01-TAXONOMIA.md`](../../kernel/operativo/entrada/01-TAXONOMIA.md) |
| A8 limpieza | `DEU` |
| A9 certificación | `SIS/Conformidad` más un dictamen de `VER` |
| A10 preparación | el gate del item, no un tipo nuevo |

**La correspondencia de A6 no es una interpretación.** El bloque `ads:proceso` de `AUD`
declara literalmente como condicionales `DOM`, `SEG`, `DIS/Reconstruccion`, `PRD` y `APR`, y
cierra *«sin pasar por PRD»*. Es la lista de participantes que el documento escribe para A2 y
A6, escrita antes y por otro motivo.

```text
LO QUE FALTA NO ES UN PROCESO
falta la pieza que sostiene juntas once fases durante semanas, entre chats y entre agentes.
Eso es el BLOQUE C del documento —la unidad amplia con dosier vivo—, y es UNA pieza.
```

**Conclusión.** Los cuatro macrocircuitos entran como **plantillas de ruta** sobre procesos
existentes, no como tipos canónicos. La única pieza nueva que los cuatro necesitan es la
misma, y es una. La opción 3 que el propio documento enumera en su §5.2 es la correcta, y
esta fase la escoge.

`traza` §4.4 · §5.2 · §5.3 · §6 · §7 · §26.15 del documento · `X4` del mapa · `proceso:AUD`

## H2 · El estado persistido es el cuello de botella de todo lo demás

Cinco de los seis bloques del documento dependen de la misma pieza ausente.

| lo que se pide | qué necesita para existir |
|---|---|
| certificación nivel **Operativo** (§10) | persistir y recuperar un checkpoint mínimo |
| unidad amplia y dosier vivo (§13–§15) | estado que sobreviva al chat |
| matriz de cobertura (§20.4) | el propio documento lo dice: *«necesita estado estructurado»* |
| telemetría y presupuesto (§26.4, §26.16) | un sitio donde contar |
| trazabilidad Git de `P-04` (§21) | items y paquetes con identidad persistida |
| estado ejecutivo del Owner (brief §20) | estado del que derivar la vista |

Y la pieza sigue exactamente donde el baseline la dejó. El
[mapa](02-MAPA-DIRECTIVA.md) marca **PARCIAL** los apartados 2, 3.6, 19 y 20 con la misma
frase: contrato completo y ningún portador. `a.9` fija seis invariantes —`I1`–`I6`— y
**delega expresamente la disposición física**. `T25` está declarada abierta por diseño en
[`03-INVARIANTES.md`](03-INVARIANTES.md) por ese motivo. Y el contraste ya lo había medido:
`CAND-008` quedó como MEJORA KERNEL con la observación de que *«no hay ninguna vista derivada
del estado de trabajo, porque no hay estado»*.

**Consecuencia sobre el orden.** El orden que el documento propone en su BLOQUE G es
correcto en sus fases y no dice qué se construye primero dentro de F6. Esta síntesis lo
concluye: la disposición física del estado se decide **antes** que la certificación
operativa, antes que la unidad amplia y antes que la matriz de cobertura, porque las tres se
apoyan en ella. Construirlas antes produciría tres almacenes paralelos, que es el modo de
fallo (a) de `a.7`.

**Y el material para decidirla ya está minado.** `CAND-001` es la estructura persistente de
sesión de PesquerApp, con 17 sesiones reales y 129 ficheros versionados. El contraste la
aceptó como material de runtime **con una reserva que se conserva entera**: su unidad de
organización es la sesión, y la sesión es aquello de lo que ADS está diseñado para no
depender. Lo reutilizable es su subestructura —trabajo, análisis, plan, ejecución, registro,
entregables— colgando de la unidad de custodia de ADS, que es el paquete.

`traza` `CAND-001` · `CAND-008` · `a.9` `I1`–`I6` · `T25` · mapa §2 §3.6 §19 §20 · §9 §10
§13 §20.4 §26.4 del documento

## H3 · El adaptador es una proyección compilada, no una capa de conocimiento

`X3` quedó registrado en el mapa como *«el mismo hueco de X1, encontrado por otro camino»*:
un adaptador no es kernel, no es pack y no es PROFILE, luego parecía exigir una capa nueva.
**Esa lectura ya no se sostiene**, y lo que la desmiente es material posterior a ella.

```text
K-1 CLASIFICA CONOCIMIENTO      ¿esto sería cierto en otro proyecto de otra clase, de la
                                misma clase, o sólo aquí? Es el test de contaminación K0.10.

UN ADAPTADOR NO ES CONOCIMIENTO es una PROYECCIÓN: el mismo contenido canónico, renderizado
                                sobre la superficie que un entorno concreto sabe leer.
                                No responde al test de contaminación porque no es su sujeto.
```

Tres materiales convergen en la misma forma, y ninguno es una capa:

- **`C6` ya le dio sitio.** *«ADAPTADOR: cómo se le entregan esos directorios en cada
  entorno agentic. Es adaptación, NO semántica del kernel.»* Y `D10` de la decisión aprobada
  fija sobre qué se apoya: filesystem y Git.
- **PesquerApp lo construyó entero, y funciona.** `CAND-009`: un núcleo declarado neutral con
  `rules/`, `workflows/`, `agents/`, `commands/` y `memory/`, consumido por cuatro
  adaptadores. Vive **junto al proyecto**, no en una capa compartida.
- **La forma de generarlo ya está probada en este repositorio.** `CAND-008` —registro
  derivado, regenerable, no editable— es el patrón, e `I4`/`I5` son los invariantes que lo
  gobiernan. `registro_pruebas.py` y `comprobar_recuentos.py --generar` lo implementan para
  el propio corpus. [`tooling/compile-agents.sh`](../../tooling/compile-agents.sh) es su
  primer intento fuera del corpus: hoy inventaría las fuentes y emite el encargo, y no genera.

**El compilador de adaptadores del §4.10 es ese patrón, aplicado a más de un destino.** Y la
huella que el §4.10 pide para detectar edición manual es `I5` hecho comprobable, que es
justo lo que le falta a `compile-agents.sh`.

**Y trae consigo el validador que `P-06` reclama.** Si la proyección es derivada, la deriva
entre núcleo y adaptador deja de ser un descuido invisible y pasa a ser una huella que no
casa. `CAND-016` y `CAND-028` midieron el coste de no tenerlo: la memoria espejada divergió
23 contra 32 entradas, y cuatro skills duplicadas divergieron las cuatro, la segunda vez
**después** de haber detectado y documentado la primera.

**Conclusión.** `X3` deja de presionar sobre `K-1`. El adaptador es un tipo canónico con
propietario, gate y prueba de humo —que es lo que `P-01` pide—, vive en el repositorio de
control del ADS Project, se genera y no se edita, lleva huella, y su validador cierra `P-06`.
**Una pieza cierra dos problemas y una contradicción, y no toca las tres capas.**

`traza` `X3` · `P-01` · `P-06` · `CAND-008` `009` `010` `011` `012` `013` `014` `016` `023`
`028` · `C6` · `D10` · `I4` `I5` · §4.10 §18 §23 §25 del documento

## H4 · El sujeto que le faltaba a `P-03` ya existe, y se llama componente

`P-03` quedó registrado con una pregunta abierta escrita con estas palabras: *«si el sujeto
«área del producto» debe existir en ADS, qué lo posee, y si su nivel es estado o es
aprendizaje»*. Y [`07-DECISION-MULTIREPO.md`](07-DECISION-MULTIREPO.md) anticipó la
respuesta sin decidirla: la decisión aprobada introduce el **componente lógico**, *«candidato
natural a ser ese sujeto»*.

**Desde el release 2.0.0-alpha.6 el componente no es un candidato: es canónico.** `N6` y `N7`
de [`C6`](../../kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md) lo definen,
[`plantillas/SOURCES.toml`](../../kernel/operativo/plantillas/SOURCES.toml) lo declara con
`id`, `source`, `path` y `kind`, `comprobar_fuentes.py` lo valida, y `E2.2` hace que los
paquetes declaren su alcance sobre las fuentes que lo materializan.

Y la segunda mitad del §20.3 tampoco es nueva. Las doce dimensiones que el documento enumera
son, una a una, capacidades que ya existen con propietario, autoridad, método y gate:

| dimensión del §20.3 | capacidad propietaria |
|---|---|
| producto y funcionalidad | `PRD` |
| UI, UX, diseño visual, sistema de diseño, responsive, accesibilidad | `DIS` |
| arquitectura, integraciones, calidad estructural | `ARQ` |
| dominio y datos | `DOM` |
| seguridad, privacidad y cumplimiento | `SEG` |
| pruebas y regresión | `VER` |
| CI/CD, despliegue, observabilidad y recuperación | `ENT` |
| tecnologías, herramientas y entorno de desarrollo | `PLT` |
| documentación y conformidad ADS | `SIS` |
| uso real | `USO` |

Dos no tienen propietario evidente y se dicen: **rendimiento y resiliencia**, que reparten
`ARQ` y `ENT`, y **dependencias y supply chain**, que hoy son el proceso `DEP` y no una
dimensión de auditoría.

**Conclusión.** El sistema permanente de auditoría del §20 no necesita un universo auditable
nuevo, ni una taxonomía de dimensiones nueva, ni una capacidad nueva. Necesita **una sola
pieza**: la celda persistida `componente × capacidad`, con su vigencia. Todo lo demás del §20
—la auditoría concreta, la clasificación de findings, la campaña, la prevención, la
verificación independiente— ya tiene portador: `AUD`, la taxonomía de entrada, la unidad
amplia de H1, `APR/Promocion` y `VER`.

Y la celda no necesita esquema nuevo: es un `memoria` con dos campos más. Que es H5.

`traza` `P-03` · `CAND-019` · `CAND-021` · `C6` `N6` `N7` · `E2.2` · §20.3 §20.4 §20.14 del
documento · §31 §33 de la decisión aprobada

## H5 · El contrato documental es `memoria` con dos campos más

El §5.23 pide un contrato verificable que declare familias aplicables, fuente canónica,
responsable, estado, evidencia, última verificación, triggers de revisión, relaciones y
gaps. El §5.19 lo detalla por documento. El §5.24 reparte la responsabilidad por capacidad.

[`esquemas/memoria.yaml`](../../kernel/operativo/esquemas/memoria.yaml) ya declara siete de
esos campos, y con los mismos nombres semánticos:

```text
capacidad             el §5.24 entero: quién responde de esta materia
capa                  kernel · pack · profile — el ámbito del §5.19
fichero               la fuente canónica del §5.23
autoridad             quién puede escribirlo
contiene              qué materia cubre
se_actualiza_cuando   los eventos del §5.20, uno a uno
se_consulta_en        el consumidor operativo, que es lo que SIS ya audita
caducidad             la vigencia del §5.19 y la reauditoría del §20.4
vacio_significa       el §5.18 literal: «no aplicable» debe ser una evaluación
                      registrada, no una ausencia silenciosa
```

**Faltan dos**, y sólo dos: `estado` —no evaluado, observado, provisional, aprobado, necesita
revisión, sustituido— y `ultima_verificacion_real`, que el §5.19 distingue con acierto de la
última edición.

**Conclusión.** El manifiesto documental del §5.23 no es un subsistema. Es el esquema
`memoria` extendido con dos campos, instanciado por familia. La pregunta del §30 sobre si se
materializa como manifiesto central, como metadata por documento o como ambos **queda
respondida por lo que ya existe**: como bloque canónico dentro de cada documento, que es como
el corpus declara todo lo demás, y con la vista central derivada de esos bloques, que es
`I4`.

`traza` §5.19 §5.23 §5.24 §5.18 §5.20 §30 del documento · `esquemas/memoria.yaml` · `I4`

## H6 · El documento se contradice consigo mismo, y la contradicción es su eje

Dos exigencias del mismo documento tiran en direcciones opuestas, y ninguna de las dos es
descartable.

```text
BLOQUE A pide MÁS      diecinueve familias documentales, doce obligatorias en TODO producto
                       (§5.13, §5.18); un universo auditable cruzado por doce dimensiones
                       (§20.3); once fases de adopción con participantes por fase (§5.3);
                       catorce requisitos en el gate de preparación (§5.9)

BLOQUE F pide MENOS    auditoría subtractiva; prueba de utilidad para cada pieza (§26.5);
                       contexto mínimo suficiente (§26.6); evitar burocracia y auditoría
                       infinita (§26.18); corpus final limpio (§26.22)
```

El brief lo había dicho antes en su 3.7: *«más agentes, más roles, más skills y más
documentación no son automáticamente una mejora»*. Y el corpus lo tiene escrito como regla
dura: `R04` obliga a que **toda capacidad declare su condición de retirada**, precisamente
porque no se materializan equipos permanentes.

**No se resuelve eligiendo un bloque.** Se resuelve aplicando la prueba del §26.5 a las
propuestas del BLOQUE A antes de declararlas obligatorias, que es lo que hace la tabla
maestra de esta síntesis. El resultado está medido abajo: de los ítems del BLOQUE A, la
mayoría resulta `YA EXPRESABLE` o `FUSIONADA`, y lo que queda `ACEPTADA` cabe en tres piezas.

Queda registrada como contradicción `X7`, porque la línea exacta del mínimo documental
obligatorio pertenece al Owner.

`traza` §5.13 §5.18 §5.9 §20.3 §26.5 §26.6 §26.18 §26.22 del documento · brief 3.7 · `R04`

---

# La puerta de F3 — resolución propuesta para `X1`–`X5`

El [plan](04-PLAN-DE-INVESTIGACION.md) fija la puerta de esta fase con una sola condición:
*«las contradicciones X1..X5 tienen resolución propuesta»*. **Propuesta**, no aprobada: las
que tocan material del Owner van a F5 por su vía.

## `X1` · Una cuarta capa contra `K-1` — **DEFERIDA, con la línea escrita**

`X1` sigue sin poder responderse: la regla 6 de [`03-INVARIANTES.md`](03-INVARIANTES.md) lo
declara, `P-05` lo registra y el motivo es del Owner. Lo que esta síntesis aporta no es una
respuesta: es **la línea que separa lo que se puede construir hoy de lo que sigue bloqueado**.

```text
NO ES X1   la DISTRIBUCIÓN PREESTRUCTURADA del §4.5. Un blueprint de control repo es
           ESTRUCTURA —directorios, esquemas, huecos tipados, plantillas, contratos—, y la
           estructura no responde al test de contaminación K0.10 porque no es conocimiento.
           Se puede construir sin decidir X1.

ES X1      el momento en que ese blueprint traiga CONTENIDO propio: un stack preferente,
           una librería por defecto, un conjunto de componentes de UI, una convención
           nuestra. Ahí deja de ser estructura y pasa a ser la cuarta capa por la puerta
           de atrás, sin la evidencia independiente que la regla 6 exige.

LA PRUEBA  ante cada pieza del blueprint: ¿esto seguiría siendo cierto en un proyecto de
           otro Owner? Si sí, es kernel o pack. Si no, y tampoco es de un solo proyecto,
           es X1 y se detiene.
```

**Y la presión del 4.3 de la directiva se reparte en dos destinos que no son una capa.** El
conocimiento *nuestro* que el 4.3 describe se parece a dos cosas distintas que esta síntesis
sí separa: lo que viene **de fuera** —librerías, presets, doctrinas de terceros— es `P-02`, y
tiene tratamiento propuesto abajo; lo que es **nuestro y repetido** sigue siendo `X1` y sigue
deferido. Confundirlos sería, con las palabras del propio `P-02`, *«la forma más fácil de
justificar mal una capa nueva»*.

`estado` abierta y deferida · `se reabre` con un proyecto independiente y maduro que minar

## `X2` · Runtime contra `G03` — **RESUELTA por lectura, salvo una pregunta**

El mapa ya la había separado: `Continúa` no es autonomía temporal; la ejecución desatendida
sí. Lo que el documento nuevo aporta es que **la parte desatendida ya tiene un caso
concreto**, en vez de ser una categoría abstracta.

```text
NO ES AUTONOMÍA TEMPORAL   persistencia, estado, checkpoint, handoff, vistas derivadas,
                           reanudación por otro agente, integración multi-fuente.
                           Es la mayor parte del apartado 16 del brief, y del BLOQUE C
                           y el BLOQUE B del documento. Procede sin levantar G03.

SÍ LO ES                   §20.6: «el sistema debe generar auditorías sin petición expresa
                           del Owner», por evento, por recurrencia y por envejecimiento.
                           Crear trabajo por su cuenta es exactamente lo que G03 frena.
```

**Resolución propuesta:** la detección es una **vista derivada** y procede —una celda vencida
se ve sin crear nada—; la **creación** del item exige o una entrada por `ENC`, o una política
de recurrencia registrada como decisión del Owner con su alcance. La diferencia entre las dos
es `I4` frente a `b.15.1`, y las dos ya existen. Queda como `X6` y como pregunta del Owner.

## `X3` · Neutralidad frente a adaptadores — **RESUELTA**

Es H3. El adaptador no es una capa de conocimiento: es una proyección compilada del
contenido canónico más la especialización del producto, vive en el repositorio de control,
se genera y no se edita, y lleva huella. `K-1` no se toca, `K0.8` se cumple —la marca sale
fuera del contrato, que es lo que `C2` ya ordenaba— y `X1` no queda prejuzgada.

**`X3` deja de ser «la segunda prueba de que falta una capa».** Era la primera prueba de que
faltaba un tipo canónico, y ese tipo es `P-01`.

## `X4` · La minería entra en proyectos que ADS no gobierna — **RESUELTA, con evidencia**

El mapa la dejó abierta con estas palabras: *«cuál de los diez procesos canónicos de b.16 lo
representa —o si hace falta uno más— es materia de la síntesis»*. Ya no hace falta suponerlo:
**la minería se ha ejecutado una vez**, en F1 y F2, y se puede leer qué forma tuvo.

| lo que hizo la minería | lo que declara `proceso:AUD` |
|---|---|
| produjo una conclusión sobre objetos existentes para que alguien decidiera | *«producir una CONCLUSIÓN sobre un objeto ya existente, para que alguien decida con ella»* |
| `INV` recorrió ocho lentes y produjo 29 fichas con procedencia | obligatoria `conclusion-fundada`, `capacidad_productora: INV` |
| el consumidor fue `SIS`, que decide qué entra al kernel | *«propietario_global DERIVADO del encargo: la capacidad responsable de la decisión que la consumirá»* |
| no se escribió una línea en los proyectos minados | *«AUD no activa CON»* |
| terminó en candidatos, no en producto | *«PUEDE cerrar en APR sin pasar por PRD»* |

**La minería es un `AUD` con `SIS` como consumidor declarado. No hace falta un proceso
nuevo.** Lo que la minería usó y no existe como tipo es la **ficha de candidato**, y `F1` ya
lo advirtió: *«hoy no existe un esquema candidato, y crear un tipo canónico es materia de la
síntesis, no de una comodidad de registro»*.

**Resolución propuesta:** no se crea el tipo todavía. La ficha de candidato es la evidencia
de la obligación `conclusion-fundada` de ese `AUD`, y una tabla la sostiene. Un esquema
canónico se justifica cuando la minería ocurra por segunda vez sobre una fuente
independiente — que es exactamente la condición que reabre `P-05`. **Un solo evento
desbloquea las dos cosas**, y hasta que ocurra ninguna de las dos se construye.

## `X5` · Un documento en voz del Owner no tiene sitio — **RESUELTA en su forma, OWNER en su ubicación**

`X5` y `P-07` son el mismo problema, y hoy tiene recuento. Al entrar el documento de
pendientes, `ads_lint` lo rechazó por dos expresiones de vocabulario y `T147` por *«existe
para nadie»*. Son los mismos dos validadores, con el mismo remedio manual, por quinta vez:

```text
docs/evolucion/ADS-NEXT-OWNER-BRIEF.md
docs/evolucion/PROMPT-ARRANQUE-ADS-NEXT.md
ADS-ARQUITECTURA-MULTIREPO-APROBADA.md
ADS-IDEAS-PENDIENTES-MULTIREPO.md
docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md
```

**Cinco exenciones por fichero para la misma clase de documento son la señal de que falta la
clase, no la exención.** Y la clase no necesita un tipo canónico nuevo: necesita tres cosas
que el repositorio ya sabe expresar.

```text
1  UBICACIÓN DECLARADA    un sitio para el material en voz del Owner, escrito en el README
                          y en el índice. Hoy dos de los cinco están en la raíz, que el
                          README no describe como sitio de nada.

2  GRADO DE AUTORIDAD     los cuatro grados de 03-INVARIANTES ya sirven: aprobado por el
                          Owner, constitucional, derivado, registrado. Un documento del
                          Owner declara el suyo en su cabecera, y de ahí sale si origina
                          una enmienda, una decisión o sólo material de trabajo.

3  EXENCIÓN POR UBICACIÓN  el vocabulario se exime por DÓNDE VIVE el documento, no fichero
                          a fichero. Los enlaces se siguen comprobando, que es lo que hoy
                          ya ocurre y debe conservarse.
```

**Lo que pertenece al Owner** es dónde viven y si los dos de la raíz se mueven: moverlos es
una decisión suya, no una limpieza, y así quedó escrito cuando `P-07` se registró.

`traza` `X5` · `P-07` · `exclusiones.yaml` · `03-INVARIANTES` cuatro grados de autoridad

---

# Tres contradicciones nuevas

Se registran con las dos posturas escritas, como exige el freno 1 de `a.7`. Ninguna se
resuelve aquí.

## `X6` · La auditoría autónoma crea trabajo, y ninguna entrada del Owner lo autoriza

```text
POSTURA A — el sistema debe planificar solo
  §20.2 nombra el problema con precisión: el recorrido manual convierte al Owner en
  planificador y memoria del control de calidad. Si el sistema no abre el trabajo, el
  Owner vuelve a ser quien recuerda qué revisar y cuándo. §20.6 lo ordena por evento,
  por recurrencia y por envejecimiento.

POSTURA B — nada crea trabajo por su cuenta
  La regla 2 de entrada/01-TAXONOMIA es dura: «ninguna clase de entrada crea trabajo por
  sí misma salvo las tres que lo declaran». G03 frena la autonomía temporal. a.8 fija los
  tres niveles de intervención del Owner. Y DSP sólo crea y despacha desbloqueadores
  «dentro del alcance ya autorizado» (b.15.1). Un sistema que abre auditorías por su
  cuenta llena la cola con trabajo que el Owner no pidió, que es la primera de las dos
  patologías que la taxonomía de entrada existe para evitar.

LO QUE NO PUEDE HACERSE
  Resolverlo por redacción. «Según la política autorizada» —las palabras del §20.6— no
  dice quién autoriza esa política, ni con qué alcance, ni cómo se revoca.

QUÉ SE PROPONE
  Separar DETECTAR de CREAR. Detectar es una vista derivada sobre la celda de cobertura y
  no crea nada: I4 ya lo permite y no toca G03. Crear exige una POLÍTICA DE RECURRENCIA
  registrada como decisión del Owner, con su alcance, su umbral y su condición de
  revocación. Sin esa decisión, el sistema propone y espera.
```

## `X7` · El mínimo documental obligatorio contra el control de crecimiento

```text
POSTURA A — sin mínimo no hay gobierno
  §5.18 exige doce familias documentales en todo producto, y el §5.9 catorce requisitos
  antes de permitir código. Sin ellas, un agente sin contexto conversacional no puede
  cambiar el producto con seguridad, que es el objetivo entero del brief §19.

POSTURA B — el mínimo es la vía por la que el sistema crece sin control
  Brief 3.7 y §26.5 exigen que cada pieza justifique su valor. R04 obliga a declarar la
  retirada de toda capacidad por ese mismo motivo. Doce documentos obligatorios por
  producto, mantenidos a mano, son doce fuentes que envejecen — y el §20.13 del propio
  documento advierte contra «otra memoria manual obsoleta».

QUÉ SE PROPONE
  Que la obligatoriedad no salga de una lista sino de un CRITERIO comprobable: una familia
  es obligatoria cuando su ausencia hace fallar la reanudación por un agente sin contexto,
  o deja un gate sin poder comprobarse. Ese criterio ya tiene forma medible en este
  repositorio: es lo que T171 comprueba para los diez criterios del §100, con su alcance
  estructural declarado. Convierte doce filas en una prueba.

QUÉ PERTENECE AL OWNER
  Dónde cae la línea. Es su tolerancia al riesgo, no una propiedad del sistema.
```

## `X8` · Organización preestructurada contra «no se materializan equipos permanentes»

```text
POSTURA A — la instalación no debe volver a diseñar ADS
  §4.5 y §4.7: la distribución debe traer catálogo completo de capacidades, agentes,
  roles, métodos, prompts, skills base, «agentes permanentes y agentes activables». C0 no
  debe pedir a cada agente que vuelva a redactar lo universal y determinista. Es correcto:
  hoy C0 es un prompt con diez entregables, y eso es rediseñar en cada instalación.

POSTURA B — materializar la organización entera es lo que el kernel prohíbe
  R04 existe con estas palabras: «no se materializan equipos permanentes: toda capacidad
  declara su condición de retirada». C4 es el algoritmo de materialización, ampliación y
  retirada, y a.4 gobierna el catálogo. SIS declara en su propia ficha que se materializa
  SIEMPRE junto a DSP — y es la única que lo declara. Traer un equipo ya montado invierte
  esa regla.

DÓNDE ESTÁ LA CONFUSIÓN
  Entre CATÁLOGO DISPONIBLE y EQUIPO MATERIALIZADO. El §4.9 del documento las separa bien;
  el §4.7 las vuelve a juntar al listar «agentes permanentes» como contenido de la
  distribución.

QUÉ SE PROPONE
  La distribución trae el CATÁLOGO —que ya lo trae: kernel/operativo/capacidades es
  exactamente eso— y las plantillas, contratos, esquemas y validadores. No trae equipo
  materializado. Quién se materializa lo decide C4 con el trabajo delante, y hoy la
  respuesta ya está escrita: DSP y SIS siempre; el resto, cuando su condición se cumple.
  Lo único abierto de verdad es si ENC entra en ese mínimo permanente, porque E1 la
  declaró «capacidad base, materializada bajo demanda».
```

---

# Estado de `P-01` a `P-07` tras la síntesis

| | problema | estado tras F3 | por qué |
|---|---|---|---|
| `P-01` | el adaptador no tiene contrato | **RESUELTO EN SU FORMA** — entra en F4 como tipo canónico | H3. Contenido: `CAND-010` qué lee · `CAND-013` qué comandos traduce · `CAND-014` qué puede escribir · `CAND-023` con qué permisos · `CAND-011` cómo degrada · `CAND-012` cómo se prueba · §4.10 cómo se genera y su matriz de soporte |
| `P-02` | no hay posición para el conocimiento externo | **RESUELTO EN SU FORMA** — un contrato de vendorizado, no una capa | `K0.11` y `huella.py` ya lo hacen con el propio kernel. `CAND-027` lo hace con conocimiento ajeno: origen, tipo, ruta y hash. El §26.7 aporta los campos que faltaban —precisión, privacidad, frescura, degradación, coste de mantenimiento— porque los pide para las herramientas de contexto, que son el mismo caso |
| `P-03` | no hay calidad persistente por área | **RESUELTO EN SU SUJETO** — reducido a una pieza | H4. El sujeto es el componente de `C6`; las dimensiones son las capacidades; la celda es un `memoria` extendido; el nivel es **estado**, no aprendizaje, porque los ledgers ya tienen otro sujeto y `F2` lo midió |
| `P-04` | `G29` gobierna Git y la línea 2.0 no lo recogió | **CERRADO EN ARQUITECTURA, ABIERTO EN EVIDENCIA** | `C7` reparte cada operación y el `integration-set` representa la convergencia. Lo que falta es lo que [`08-EVIDENCIA`](08-EVIDENCIA-MULTIREPO.md) declara: `T169` y `T170` en contrato-definido, y `CAND-026` —diez ramas sin fusionar y nada que las mire— sigue sin medida. Exige runtime y piloto |
| `P-05` | sin evidencia independiente no se decide la cuarta capa | **DEFERIDO, con la línea escrita** | `X1`. Y ahora comparte condición de reapertura con `X4`: la segunda minería sobre una fuente independiente desbloquea las dos |
| `P-06` | la deriva núcleo/adaptadores no la ve nadie | **RESUELTO EN SU FORMA** — es el validador del tipo de `P-01` | H3. Si la proyección es derivada y lleva huella, la deriva deja de ser invisible. `CAND-016` y `CAND-028` son las dos ocurrencias que lo justifican |
| `P-07` | material normativo en voz del Owner sin sitio | **RESUELTO EN SU FORMA, OWNER EN SU UBICACIÓN** | `X5`. Quinta ocurrencia medida hoy |

**Cinco de siete quedan resueltos en su forma y entran en F4.** Uno queda deferido con su
condición de reapertura escrita, y uno queda abierto en evidencia porque exige un producto
real, que sigue sin existir.

---

# Tabla maestra de propuestas

Todo lo que el documento de pendientes propone, con su veredicto y su destino. **Ninguna
fila autoriza a implementar nada**: dicen qué entra en F4 y con qué forma.

## BLOQUE A · instalación, adopción, migración y actualización

| § | propuesta | veredicto | destino y traza |
|---|---|---|---|
| 4.5 | ADS se distribuye preestructurado | **ACEPTADA** con límite | H3 y `X1`. La distribución trae estructura; el día que traiga stack o librerías preferentes es `X1` y se detiene |
| 4.6 | cinco capas: canónica, blueprint, especialización, proyección, estado | **REDUCIDA a cuatro** | el blueprint viaja **dentro** de la distribución: `plantillas/` y `new-project.sh` ya son su primera versión. Aviso escrito: estas cuatro clasifican **ciclo de vida**, y `K-1` clasifica **conocimiento**. Confundirlas fabrica la cuarta capa por la puerta de atrás |
| 4.7 | qué debe venir preparado | **REDUCIDA** | catálogo, contratos, esquemas, plantillas, validadores y blueprints: sí, y en buena parte ya viajan. «Agentes permanentes» materializados: no → `X8` |
| 4.8 | qué sólo se completa al conocer el producto | **ACEPTADA** | son `PROFILE`, `PROJECT` y `SOURCES.toml`, que ya existen. Lo nuevo es que sus huecos sean **tipados y validables**, no prosa libre |
| 4.9 | catálogo completo frente a equipo activo | **YA EXPRESABLE** | [`C4`](../../kernel/operativo/contratos/C4-MATERIALIZACION.md) es el algoritmo, `a.4` gobierna el catálogo, y la ficha de [`SIS`](../../kernel/operativo/capacidades/SIS/CAPACIDAD.md) ya declara *«se materializa SIEMPRE, junto a DSP»*. Abierto sólo si `ENC` entra en ese mínimo |
| 4.10 | fuente canónica única y compilador de adaptadores | **ACEPTADA y FUSIONADA** | H3. Con `I4`/`I5` y huella. La matriz soportado / compatible / genérico / desconocido entra entera, y `CAND-011` es la fila «genérico» ya construida en un proyecto real |
| 4.11 | C0 se reduce a especializar y certificar | **ACEPTADA** | corrige un defecto medido: hoy C0 es un prompt con diez entregables que cada instalación vuelve a redactar |
| 4.4 | recorrido `N0`–`N7` de proyecto nuevo | **FUSIONADA** | H1: plantilla de ruta sobre procesos existentes |
| 5.3 | recorrido `A0`–`A10` de adopción | **FUSIONADA** | H1. Es la opción 3 que el propio §5.2 enumera |
| 5.4 | reparto de responsabilidades de adopción | **YA EXPRESABLE** | cada línea del reparto es la `autoridad` que la ficha de esa capacidad ya declara. Repetirla en un documento nuevo crearía una segunda verdad |
| 5.5 · 5.22 | qué vive en el control repo y qué en la fuente | **YA EXPRESABLE** | [`C6`](../../kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md) ya tiene la frontera, y como pregunta comprobable: *«¿esto deja de ser cierto si cambia el código de al lado?»*. Tres secciones del documento la reformulan sin añadirle nada |
| 5.6 | reglas de seguridad para migrar y limpiar | **ACEPTADA** | importar, validar, retirar; rollback; commits revisables por fuente. `CAND-016` es la evidencia de qué pasa sin ellas |
| 5.7 | reconstruir UI/UX y sistema de diseño existentes | **YA EXPRESABLE** | [`DIS/Reconstruccion`](../../kernel/operativo/capacidades/DIS/metodos/Reconstruccion.md) existe, con inventario, capturas y la regla escrita: *«conservar lo valioso»*. Los siete pasos del §5.7 son sus pasos |
| 5.8 | conversión del trabajo histórico | **YA EXPRESABLE** | las nueve clases de entrada y su regla 2. La lista de resultados posibles del §5.8 es esa taxonomía con otros nombres |
| 5.9 | gate «ahora puedes empezar a programar» | **FUSIONADA y REDUCIDA** | = certificación nivel **Integrado** + baseline aprobado por el Owner. Definir dos gates para el mismo momento es la duplicación que `SIS` audita |
| 5.10 | persistencia entre chats de la adopción | **FUSIONADA** | unidad amplia y dosier vivo |
| 5.11 | documentación viva global del producto | **ACEPTADA** | no choca con `C6`: la respuesta de su pregunta frontera para producto, arquitectura, dominio y dirección es «vive en el control repo» |
| 5.12 | cuatro vistas: baseline, dirección, reglas, decisiones | **ACEPTADA** | cuesta un campo y evita el error más caro: presentar una arquitectura objetivo como implementada. Es `3.4` del brief aplicado a documentación |
| 5.13 – 5.18 | diecinueve familias, doce obligatorias | **REDUCIDA** | → `X7`. La obligatoriedad sale de un criterio comprobable, no de una lista |
| 5.19 | estado, procedencia y vigencia por documento | **FUSIONADA** | H5: `memoria` + `estado` + `ultima_verificacion_real` |
| 5.20 | eventos que obligan a actualizar documentación | **YA EXPRESABLE** | es el campo `se_actualiza_cuando`, que ya es obligatorio en `memoria` |
| 5.21 | extracción y reconstrucción durante la adopción | **FUSIONADA** | `AUD` + `DIS/Reconstruccion` |
| 5.23 | contrato o manifiesto documental | **FUSIONADA** | H5. Y responde la pregunta del §30: bloque canónico por documento, vista central derivada |
| 5.24 | responsabilidad documental por capacidad | **YA EXPRESABLE** | es el campo `capacidad` de `memoria` |
| 6 | migración desde una versión anterior de ADS | **FUSIONADA** | H1. Su contenido propio —estado en curso, overrides, mecanismos retirados— es el mismo que el §7 |
| 7 | actualización de ADS en proyectos instalados | **ACEPTADA y FUSIONADA** | H1. `kernel-status.sh` y `.upstream-hash` ya son la mitad de la detección; falta comparación, impacto, plan y rollback. El principio *«detectar automáticamente, actualizar conscientemente»* entra tal cual |

## BLOQUE B · certificación

| § | propuesta | veredicto | destino y traza |
|---|---|---|---|
| 10 | cuatro niveles: estructural, operativo, integrado, completo | **ACEPTADA** | y con portador ya existente para dos: **estructural** son los trece validadores y `gate:sistema-conforme`; **integrado** incluye `workspace check`, que ya existe. **Operativo** es `CAND-012` y no existe. **Completo** exige runtime |
| 10 | ningún nivel se declara por argumento | **ACEPTADA** | es la disciplina de [`08-EVIDENCIA`](08-EVIDENCIA-MULTIREPO.md) aplicada a una instalación: un nivel se afirma con evidencia **ejecutada**, no por haber pasado el nivel anterior |
| 11 | `SIS` posee, pero no es el único crítico | **YA EXPRESABLE** | `G13` —creación no es validación— y `C4` paso 5. La ficha de `SIS` ya escala lo que afecta a material aprobado |
| 12 | gate obligatorio y dosier de certificación | **ACEPTADA** | el dosier es [`plantillas/DICTAMEN.md`](../../kernel/operativo/plantillas/DICTAMEN.md), cuya regla 4 prohíbe el término medio. Sus seis disparadores entran tal cual |

## BLOQUE C · unidad amplia y dosier vivo

| § | propuesta | veredicto | destino y traza |
|---|---|---|---|
| 13 · 14 | unidad persistente superior al paquete | **ACEPTADA** | **es la única pieza de coordinación nueva que esta síntesis sostiene.** H1 la justifica siete veces: los cuatro macrocircuitos, la campaña de corrección, la auditoría del ADS y el gate de higiene la necesitan igual |
| 14 | no debilita item, paquete, source change ni integration set | **ACEPTADA** | condición de aceptación, no comentario. `(b)` y `C7` no se tocan |
| 15 | el dosier es índice y memoria, no copia | **ACEPTADA** | es `I5` literal. `CAND-016` mide qué pasa cuando un índice se convierte en copia |
| 16 | umbral de activación | **REDUCIDA** | nueve señales candidatas son nueve formas de decir una: **el cierre no puede explicarse con un solo item**. Las otras ocho se derivan de ésa o la aproximan |
| 17 | doce decisiones pendientes sobre la unidad | **REDUCIDA a tres** | nombre; si es tipo canónico o composición; qué gate la cierra. Las otras nueve se responden desde `(b)` una vez decididas esas tres |

## BLOQUE D · los siete problemas

Su estado está en la tabla de `P-01`–`P-07`. Lo que el documento añade sobre `P-03`:

| § | propuesta | veredicto | destino y traza |
|---|---|---|---|
| 20.1 | sistema permanente de aseguramiento y mejora | **ACEPTADA en la necesidad, REDUCIDA en el tamaño** | H4. Diecisiete subsecciones se reducen a una pieza persistida y a procesos que ya existen |
| 20.3 | universo auditable y dimensiones | **YA EXPRESABLE** | universo = componentes de `SOURCES.toml`; dimensiones = capacidades. Dos dimensiones sin propietario evidente quedan nombradas en H4 |
| 20.4 | matriz viva de cobertura | **FUSIONADA y REDUCIDA** | celda `componente × capacidad`, con la forma de `memoria`. Doce estados candidatos entran sólo los que cambian una decisión |
| 20.5 | catálogos sistemáticos por especialidad | **YA EXPRESABLE** | son las rúbricas y gates de cada capacidad. `DIS` ya tiene [`02-RUBRICAS`](../../kernel/operativo/diseno/02-RUBRICAS.md) y `05-FIDELIDAD`, y la lista de comprobaciones visuales del §20.5 es su contenido |
| 20.6 | planificación autónoma por evento, riesgo y envejecimiento | **OWNER** | `X6` |
| 20.8 | clasificación de findings | **YA EXPRESABLE** | la tabla del §20.8 mapea uno a uno sobre los diez procesos de `b.16` y sobre la taxonomía de entrada. Y su regla —*«no todo finding es un GAP»*— es la regla 2 de la taxonomía |
| 20.9 | corregir causas raíz, no síntomas | **ACEPTADA** | veinte inputs con alturas distintas no son veinte items. Es lo que evita que la auditoría continua fabrique cola |
| 20.11 | convertir lo repetible en prevención | **YA EXPRESABLE** | `APR/Promocion` y `gate:aprendizaje-fundado`, que ya exige dos ocurrencias o un incidente antes de dejar escribir la entrada |
| 20.12 | autonomía con límites por nivel de riesgo | **OWNER** | los cinco niveles del §20.12 son materia de `a.8`. Su forma es correcta; el umbral es del Owner |
| 20.13 | estado estructurado del que derivar vistas | **FUSIONADA** | H2 e `I4` |
| 20.15 | `corregido` y `verificado` son estados distintos | **ACEPTADA** | `G13` con otro nombre, y `DICTAMEN` ya prohíbe el término medio que lo borraría |

## BLOQUE E · las siete mejoras concretas

| propuesta | veredicto | destino y traza |
|---|---|---|
| capturar y comparar estados de carga bajo las mismas condiciones | **ACEPTADA** → pack `web-app` | `CAND-022`, MEJORA PACK en F2. Primera evidencia de que `DIS/RevisionDeFidelidad` es ejecutable |
| gancho Git con degradación explícita | **ACEPTADA** → pack `web-app` | `CAND-024`, MEJORA PACK en F2 |
| mapa por adaptador de qué consume y qué escribe | **FUSIONADA** → `P-01` | `CAND-010` |
| prueba de humo en sesión nueva tras instalar o cambiar adaptador | **FUSIONADA** → `P-01` y certificación **Operativo** | `CAND-012` |
| vendorado controlado de skills externas | **FUSIONADA** → `P-02` | `CAND-027` |
| detección de ramas o trabajo Git abandonado | **ACEPTADA** → `C7`, exige runtime | `CAND-026`. Es la medida que el 8.3 del brief pide literalmente |
| fronteras de escritura entre entornos agentic | **FUSIONADA** → `P-01` | `CAND-014`, extensión de `I2` a zonas del repositorio |

**Los dos primeros son los únicos de toda esta síntesis cuya forma no depende de ninguna
pregunta abierta**, que es lo que el checkpoint anterior ya había marcado como punto de
partida de F3.

## BLOQUE F · simplificación, coste y complejidad

| § | propuesta | veredicto | destino y traza |
|---|---|---|---|
| 26.1 · 26.2 | calidad profesional no negociable; el presupuesto no rebaja el gate | **ACEPTADA, y en buena parte YA EXPRESABLE** | [`esquemas/rubrica.yaml`](../../kernel/operativo/esquemas/rubrica.yaml) existe *«para no reducir el juicio a una nota»*; `DICTAMEN` prohíbe el término medio; [`03-ESCALA-DE-NOVEDAD`](../../kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md) escribe *«N0 no significa trabajo barato, acabado inferior ni verificación reducida»*. Lo que falta es extenderlo fuera de diseño |
| 26.2 | spike, prototipo e implementación profesional son cosas distintas | **YA EXPRESABLE** | [`CON/Experimental`](../../kernel/operativo/capacidades/CON/metodos/Experimental.md) es *«construir para saber, no para entregar»*, y exige el criterio de descarte **antes de la primera línea**. Es más estricto que la tabla del §26.2 |
| 26.3 | coste por resultado aceptado y verificado | **ACEPTADA** | cambia la unidad de medida, y sin ella toda comparativa de modelos miente |
| 26.4 | auditoría empírica del propio ADS | **ACEPTADA** | y es un `AUD` con `SIS` como consumidor: el mismo molde que `X4` |
| 26.5 | prueba de utilidad de cada pieza | **ACEPTADA** | esta tabla es su primera aplicación |
| 26.6 | catálogo completo, contexto selectivo, ampliable | **ACEPTADA y FUSIONADA** | `C6` ya tiene la mitad: *«necesidad → componentes afectados → fuentes necesarias → lee/escribe → contexto mínimo»*, con `E2.2`. Falta la mitad de dentro del control repo, que es el hueco que `K0.2` dejó al ser sustituido y que `compile-agents.sh` todavía cita |
| 26.7 | Caveman y herramientas de contextualización | **FUSIONADA** → `P-02`, y es un item `INV` | sus nueve exigencias por candidato —procedencia, precisión, privacidad, frescura, degradación— son los campos que le faltaban al contrato de vendorizado. Cuáles se adoptan lo decide investigación, no esta fase |
| 26.9 | enrutamiento de modelos por juicio y riesgo | **YA EXPRESABLE** | [`C2`](../../kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md) fija perfiles neutrales, asignación, combinación y relevo. Lo que el §26.9 añade es el **escalado ante incertidumbre** y el registro del modelo ejecutor |
| 26.10 | delegación y tamaño de paquete | **YA EXPRESABLE, sin dato** | `DSP` ya decide sola el tamaño del paquete. Los límites de fan-out salen de un piloto, y el piloto no existe |
| 26.12 | automatizar lo determinista, reservar IA para juicio | **YA EXPRESABLE** | es la doctrina de `validadores/` desde el primer día |
| 26.13 | métricas equilibradas, sin puntuación única | **ACEPTADA** | y coherente con el rechazo de la nota de 1 a 10 en `CAND-019` |
| 26.14 | banco de diez escenarios | **ACEPTADA** | es también el guion del piloto que falta |
| 26.15 | fases `E0`–`E8` | **FUSIONADA** | H1 |
| 26.16 | presupuesto como ritmo | **ACEPTADA y FUSIONADA** | `G24` es un hueco ya declarado en [`03-INVARIANTES`](03-INVARIANTES.md) con dueño asignado. El protocolo de pausa —unidad segura, verificar, persistir, siguiente acción exacta, no declarar terminación— es `a.10` y `b.14` ya escritos |
| 26.17 | protección del diseño profesional | **YA EXPRESABLE** | la escala de novedad, los gates de `DIS` y `05-FIDELIDAD` son ese recorrido |
| 26.18 | evitar auditoría infinita; stop conditions | **YA EXPRESABLE** | los tres frenos de `a.7`, y el de racha `SIS` como precedente exacto |
| 26.19 | reparto de responsabilidades | **YA EXPRESABLE** | son las autoridades ya declaradas |
| 26.22 – 26.24 | corpus final limpio, y un único ledger de evolución | **ACEPTADA el principio · RECHAZADO el fichero nuevo** | `EVOLUTION.md` sería una **segunda** verdad: [`kernel/KERNEL_CHANGELOG.md`](../../kernel/KERNEL_CHANGELOG.md) y `kernel/VERSIONES.md` ya son ese ledger, con política escrita y validador. Crear otro es el defecto que el propio §26.24 quiere evitar |
| 26.25 | gate de higiene del corpus | **FUSIONADA** | `SIS/Conformidad` ya comprueba documentos sin consumidor operativo y duplicación de fuentes de verdad; `T147` ya detecta el documento que existe para nadie; `exclusiones.yaml` ya obliga a escribir el motivo de cada excepción y a retirarla cuando caduca. El gate del §26.25 es ese método extendido, no uno nuevo |
| 26.26 | limpio no es menos documentación gobernante | **ACEPTADA** | y es la salvaguarda que impide leer el §26.22 como una poda |

---

# Los 29 candidatos, después de F3

F2 los clasificó por veredicto. F3 los coloca en su destino, y el reparto tiene una forma
que no se veía candidato a candidato.

| destino tras F3 | candidatos | qué significa |
|---|---|---|
| **contrato de adaptador** (`P-01`) | `009` `010` `011` `012` `013` `014` `023` | **siete de veintinueve son la misma pieza.** Es el resultado más concentrado de la minería, y explica por qué `P-01` sale de F3 con contenido y no con una pregunta |
| **estado persistido** (H2) | `001` `004` `007` `008` | la subestructura de sesión sin la sesión; las zonas de autoridad de `a.9` aplicadas al paquete; el estado legible sin herramienta de `I4`; y la vista derivada regenerable |
| **calidad por área** (`P-03` → H4) | `019` `021` | la nota de 1 a 10 sigue rechazada. Lo que se conserva es el sujeto y la comparación consigo mismo a lo largo del tiempo |
| **conocimiento externo** (`P-02`) | `015` `027` | la precedencia que falta y el mecanismo que ya funciona: origen, ruta y hash |
| **deriva** (`P-06`) | `016` `028` | dos ocurrencias medidas, y el validador que las habría visto |
| **gobierno Git** (`P-04`) | `025` `026` | cerrado en arquitectura por `C7`; `026` sigue sin medida porque exige runtime |
| **pack `web-app`** | `022` `024` | entran tal cual. Los únicos que no dependen de ninguna pregunta abierta |
| **confirmación sin cambio** | `002` `003` `005` `020` | ADS ya lo resolvía, y en `003` y `020` con más precisión que el proyecto |
| **contenido de plantilla** | `017` `018` | H5. `CAND-017` no necesita campo nuevo: `memoria.se_consulta_en` ya es obligatorio. Lo que falta es que sus instancias nombren roles y métodos en vez de ocasiones |
| **no sube** | `006` | el contenido es de ese proyecto; su forma ya es doctrina de ADS |
| **deferido** | `029` | `P-05` y `X1` |

---

# Qué debe retirarse o encogerse

La auditoría subtractiva que el §26 pide, aplicada primero al propio documento que la pide.

```text
SE RETIRAN COMO DISEÑOS SEPARADOS
  · los cuatro macrocircuitos como cuatro diseños        → una composición y cuatro rutas
  · las fases E0–E8 de auditoría del propio ADS          → un AUD con SIS como consumidor
  · el gate de higiene del §26.25 como gate nuevo        → SIS/Conformidad extendida
  · el manifiesto documental del §5.23 como subsistema   → memoria con dos campos
  · el universo auditable del §20.3 como taxonomía nueva → componentes × capacidades
  · el fichero EVOLUTION.md                              → KERNEL_CHANGELOG ya es el ledger
  · el reparto de responsabilidades repetido tres veces
    (§5.4, §5.24, §20.14, §26.19)                        → las fichas ya lo declaran

SE ENCOGEN
  · diecinueve familias documentales, doce obligatorias  → un criterio comprobable   X7
  · nueve señales de activación de la unidad amplia      → una
  · doce decisiones pendientes sobre la unidad amplia    → tres
  · doce estados de celda de cobertura                   → los que cambian una decisión
  · catorce requisitos del gate de adopción              → certificación + baseline
  · las treinta y tres preguntas del §30                 → nueve que bloquean de verdad

SE CONSERVAN ENTEROS, y no por inercia
  · la unidad amplia con dosier vivo: es la única pieza de coordinación que falta
  · el contrato de adaptador: siete candidatos y dos problemas convergen en él
  · la celda de cobertura componente × capacidad: es lo único nuevo de todo el §20
  · los cuatro niveles de certificación: separan afirmaciones que hoy se confunden
  · la calidad profesional como suelo, y el presupuesto como ritmo
```

**Lo que NO se retira, y conviene decirlo.** El §26.26 lo advierte y esta síntesis lo
suscribe: retirar andamiaje no es podar documentación gobernante. Contratos, esquemas,
métodos, plantillas, rúbricas, decisiones y pruebas se quedan enteros. Lo que sale del HEAD
estable es el material de construcción ya consumido — y esta iniciativa, incluida esta
síntesis, es material de construcción.

---

# `Q9` y `Q10`, respondidas

Eran las dos últimas preguntas abiertas del [plan](04-PLAN-DE-INVESTIGACION.md), y ambas
entraban expresamente en la síntesis.

## `Q9` — qué representa la minería dentro de `b.16` · **RESPONDIDA**

Un `AUD` con `SIS` como consumidor declarado. La correspondencia, campo a campo, está en la
resolución de `X4`. **No hace falta un proceso nuevo**, y el esquema `candidato` se aplaza
con su condición escrita.

## `Q10` — qué tiene ya un proyecto que ADS no debe sustituir · **RESPONDIDA, y con criterio operable**

La pregunta pedía una lista. La minería devuelve algo mejor: **una señal**.

```text
LO QUE NO SE SUSTITUYE ES LO QUE TIENE CICATRIZ ESCRITA

CAND-012   la prueba de humo existe porque una skill añadida no aparecía hasta reiniciar
           la sesión, y nadie lo sabía.
CAND-014   la frontera de escritura dice por qué existe en su propio comentario:
           «to avoid re-introducing the same drift».
CAND-024   el gancho se degrada con aviso porque en entornos de nube las dependencias las
           gestiona otro.
```

F1 ya lo había medido sin nombrarlo: al declarar que el coste evitado no se puede leer desde
un repositorio, escribió que *«la única señal indirecta es que los mecanismos con cicatriz
escrita nombran el error que los provocó»*. Y el protocolo de minería llevaba la señal desde
F0: `L7` es la lente de las cicatrices, y el plan ya la declaraba *«lo más valioso»*. Lo que
`Q10` añade es que esa lente **también gobierna la adopción**, y no sólo la minería.

**Y la comprobación es que ADS los adoptó.** Tres de esos cuatro salieron de F2 como MEJORA
KERNEL o MEJORA PACK. Lo que un proyecto trae y ADS no debe sustituir no es una categoría de
fichero: es un mecanismo cuyo motivo está escrito y sigue siendo cierto. Es el criterio
operable que le faltaba al 6.5 del brief, y el que gobierna `A4` y `A8` de la adopción.

---

# Lo que la síntesis concluye sobre el orden

**No es la arquitectura, y no la sustituye.** Es la consecuencia de H2 sobre el orden que el
BLOQUE G propone, que es correcto en sus fases y no dice qué se construye primero dentro de
cada una.

```text
1  DISPOSICIÓN FÍSICA DEL ESTADO       a.9 la delega, T25 está abierta por diseño, y
                                       CAND-001 es su material minado. Sin ella, la
                                       certificación operativa, la unidad amplia y la
                                       matriz de cobertura serían tres almacenes paralelos.

2  CONTRATO DE ADAPTADOR               siete candidatos convergen, cierra P-01 y P-06, y
   Y SU VALIDADOR DE DERIVA            no depende del estado.

3  UNIDAD AMPLIA Y DOSIER VIVO         se apoya en 1, y desbloquea los cuatro
                                       macrocircuitos a la vez.

4  CERTIFICACIÓN POR NIVELES           se apoya en 1 y 2. Su nivel Operativo es CAND-012.

5  LOS DOS DE PACK                     022 y 024. No dependen de nada de lo anterior, y
                                       pueden ir en cualquier momento.

6  CELDA DE COBERTURA                  se apoya en 1. Sin política de recurrencia, sólo
                                       detecta: crear trabajo espera a X6.

7  PILOTO REAL                         lo único que convierte T169, T170, CA-10, CA-11 y
                                       el §100 como descubrimiento en algo demostrado.
                                       El banco de escenarios del §26.14 es su guion.
```

**El gate de higiene del corpus va al final, y no por comodidad.** El §26.22 alcanza a
`docs/evolucion/` entero, y esta síntesis está dentro. Retirarlo antes de que F5 y F6
promuevan sus conclusiones a fuentes canónicas rompería la trazabilidad que la regla 1 de
[`03-INVARIANTES`](03-INVARIANTES.md) exige para toda enmienda. Se retira **después** de que
exista el destino, nunca antes — que es exactamente lo que el §26.23 ordena al pedir
clasificación obligatoria antes de retirar.

---

# Preguntas que necesitan al Owner

El §30 del documento enumera treinta y tres asuntos. La mayoría son técnicos y los decide
F4. **Éstas nueve no**: o son autoridad del Owner, o su respuesta cambia qué se construye.

| | pregunta | qué desbloquea |
|---|---|---|
| 1 | ¿Autoriza una **política de recurrencia** que permita al sistema **abrir** trabajo de auditoría sin petición suya? ¿Con qué alcance y cómo se revoca? | `X6`. Sin ella el sistema detecta y propone, y la cobertura no se planifica sola |
| 2 | ¿Dónde cae el **mínimo documental obligatorio** de un producto? | `X7`. Decide si son doce familias en todo producto o un criterio de reanudación |
| 3 | ¿Confirma que la distribución trae **catálogo** y nunca equipo materializado? | `X8`. Y su consecuencia: qué hace exactamente C0 |
| 4 | ¿Entra **`ENC`** en el equipo mínimo permanente junto a `DSP` y `SIS`? | `E1` la declaró materializada bajo demanda. Es la única duda real del §4.9 |
| 5 | ¿Dónde viven los **documentos en voz del Owner**, y se mueven los dos de la raíz? | `P-07` y `X5`. Cinco exenciones manuales van ya |
| 6 | ¿Qué **nombre** lleva la unidad amplia, y es tipo canónico o composición? | `BLOQUE C`. Las otras diez decisiones se derivan de ésta |
| 7 | ¿Qué **nivel de certificación** basta para empezar a trabajar en un producto? | decide si el gate de adopción exige **Operativo** o **Integrado** |
| 8 | ¿Qué **entornos agentic** entran en la primera matriz soportada? | `P-01`. Certificar un adaptador cuesta una prueba de humo por entorno |
| 9 | ¿Qué **producto real** se usa para el piloto? | `T169`, `T170`, `CA-10`, `CA-11`, el §100 como descubrimiento, `CAND-026` y los límites de fan-out. Todo eso sigue sin poder demostrarse |

**La novena es la más cara de aplazar.** La columna de uso real sigue vacía para todo el
sistema, y lo dice el mapa desde F0.

---

# Lo que esta síntesis NO decide

```text
LA ARQUITECTURA INTEGRADA     es F4, y su puerta es la crítica independiente por quien no
                              la escribió. La iteración anterior dejó el precedente: una
                              auditoría independiente encontró treinta y tres hallazgos.

NINGUNA ENMIENDA              (a), (b), E1 y E2 siguen íntegras. Lo que esta fase encuentra
                              que las presiona queda registrado, no aplicado.

LA CUARTA CAPA                X1 sigue deferida. La línea que separa lo construible de lo
                              bloqueado está escrita arriba, y no la cruza nada de F3.

EL LEVANTAMIENTO DE G03       la parte desatendida de X2 es del Owner, y ahora tiene una
                              pregunta concreta en vez de una categoría.

EL NOMBRE DE NADA             ni la unidad amplia, ni el tipo del adaptador, ni el fichero
                              de la celda de cobertura. Nombrar es F4.

QUÉ ENTRA EN CADA RELEASE     es F6, y exige items SIS trazables.
```

**Ninguna decisión de este documento es irreversible.** Ningún fichero de
`kernel/operativo/`, `packs/` ni `docs/rediseno/` ha cambiado en F3, igual que en F2.
