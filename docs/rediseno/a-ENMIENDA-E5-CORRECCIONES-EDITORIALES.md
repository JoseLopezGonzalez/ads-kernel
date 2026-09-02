# ENMIENDA `E5` a las SECCIONES (a) y (b) y a `E1` — correcciones editoriales que no cambian ninguna norma

```text
identificador   E5
enmienda a      docs/rediseno/b-RECORRIDO-APROBADA.md
                docs/rediseno/a-CAPACIDADES-APROBADA.md
                docs/rediseno/a-ENMIENDA-E1-ENC.md
fecha           2026-09-02
autoridad       Owner
motivo          aplicar la checklist editorial obligatoria de F5 sobre material aprobado:
                una cita a un predicado equivocado, una lista mal numerada, un recuento de
                marcas que el árbol no da, y el inventario de enmiendas vigentes que no
                coincide entre las sedes que lo enumeran
origen          docs/owner/ADS-OWNER-RESOLUCIONES.md · O23 §10
                docs/evolucion/11-ARQUITECTURA-INTEGRADA.md · §19, filas E5-1, E5-2 y E5-4
                docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md · §11, observación OC-2
estado          APROBADA
```

> **Qué es este documento.** **NINGUNA de estas correcciones cambia una norma.** El texto
> final de cada una es calculable sin decidir nada, y se verificó contra el árbol antes de
> escribirlo. La autoridad de esta materia es «`F5`, con aprobación del Owner», y esa
> aprobación consta.
>
> **Lo que esta enmienda NO hace:** no cambia ninguna regla, no altera ninguna composición,
> no toca la grafía de ningún identificador —esa materia se resolvió aparte y NO exige
> enmendar la fuente— y no corrige nada fuera del material aprobado.

---

## `E5.0` — La decisión

Se aplican las cuatro correcciones de abajo, y ninguna más. **Cada una lleva su prueba
posterior**, porque una corrección editorial sin prueba vuelve a caducar.

## `E5.1` — Una cita a un predicado equivocado

### Texto de `(b)` que SUSTITUYE · L358

```text
DICE           «Un `devuelto` sin paquete de corrección deja al item en `en espera` (P7)»
PASA A DECIR   «Un `devuelto` sin paquete de corrección deja al item en `en espera` (P9)»
```

**Por qué es mecánica y no un criterio:** `(b)` define el primer predicado como «→ `activo`»
y el segundo como «→ `en espera`», y `devuelto` está entre los casos del segundo. **Y el
mismo documento ya lo usa bien en L255**, donde escribe «`activo` (P7) … `en espera` (P9)».

**PRUEBA POSTERIOR:** que toda cita de un predicado en `(b)` case con el predicado que ese
número define.

## `E5.2` — Una lista mal numerada

### Texto de `(b)` que SUSTITUYE · L459–L473

```text
DICE           la secuencia de las reglas de recomposición va 1, 2, 5, 3, 4 — el bloque
               numerado «5.» está físicamente entre el «2.» y el «3.»
PASA A DECIR   1, 2, 3, 4, 5, CONSERVANDO EL TEXTO DE CADA REGLA SIN TOCAR UNA PALABRA
```

**Cómo se aplica, exactamente:** el bloque hoy numerado `5.` se traslada detrás del bloque
`4.`, y la numeración pasa a ser correlativa. **Ningún texto de regla cambia**, y el orden
lógico de las reglas es el que resulta de su numeración correcta.

**CONDICIÓN PREVIA, comprobada:** ninguna otra sede cita esas reglas por su número. Se
verificó por barrido sobre el árbol de este commit, **después** de aplicar `E3` y `E4`, que
son las enmiendas que podían introducir referencias nuevas.

**PRUEBA POSTERIOR:** que la secuencia de una lista numerada de `(b)` sea estrictamente
creciente.

## `E5.3` — El recuento de marcas de remisión, reanclado a su derivación

### Texto de `(a)` que SUSTITUYE · L269 y L276

```text
L269   DICE          «Las 14 son el **catálogo base**, no un catálogo universal cerrado»
       PASA A DECIR  «Las 14 `[E1: 15]` son el **catálogo base**, no un catálogo universal
                     cerrado»

L276   DICE          «CATÁLOGO BASE DEL KERNEL     capacidades universales · 14 · códigos
                     reservados»
       PASA A DECIR  «CATÁLOGO BASE DEL KERNEL     capacidades universales · 14 `[E1: 15]` ·
                     códigos reservados»
```

### Texto de `E1` que SUSTITUYE · L196–L197

**El remedio no es corregir el cardinal: es retirarlo.** Un cardinal escrito a mano al lado
de una sede que crece caduca solo, y éste ya caducó una vez.

```text
DICE           «siete MARCAS DE REMISIÓN `[E1]` insertadas en línea, en los puntos exactos
               que esta enmienda sustituye — cinco recuentos y dos párrafos»

PASA A DECIR   «MARCAS DE REMISIÓN `[E1]` insertadas en línea, en los puntos exactos que
               esta enmienda sustituye. EL NÚMERO NO SE ESCRIBE: se deriva con
                 grep -c '\[E1[ :→]' docs/rediseno/a-CAPACIDADES-APROBADA.md»
```

> **Por qué el comando lleva ese filtro, y no es un detalle.** `grep -c '\[E1'` a secas
> devuelve una línea de más: la frase del bloque de aviso que **anuncia** las marcas escribe
> `[E1]` cerrado y no es una marca. Exigir un separador tras `[E1` la excluye. **Consagrar
> el comando sin filtro habría repetido, en la única corrección que existe para que la cifra
> no pueda estar mal, exactamente el error que corrige.**

**ALCANCE, declarado:** el mismo cardinal aparece en un tercer documento que **no es material
aprobado**. Su corrección **no es de `F5`** y no se hace aquí. Se declara para que nadie
cuente tres sedes y dos verdades sin saberlo.

**PRUEBA POSTERIOR:** que el número de marcas que `E1` declara coincida con las que `(a)`
lleva, **derivado por barrido y no escrito**.

## `E5.4` — El inventario de enmiendas vigentes, que no coincidía

### Texto de `(a)` que AMPLÍA · bloque de aviso, L9–L18

El bloque de aviso de `(a)` listaba **una sola** enmienda cuando ya había más. Pasa a listar
todas las vigentes, y **su contenido se deriva en vez de escribirse**.

### Texto de `(b)` que AMPLÍA · cabecera

**`(b)` estaba enmendada y no lo decía en ninguna parte de su propio texto.** Recibe el
bloque de aviso de enmiendas vigentes que la mecánica de `E1` prescribe y que hasta hoy no
existía.

### Las sedes que enumeran las enmiendas, y cuáles son de `F5`

**La sede de `OC-2` nombra tres**: la sección aprobada, el índice de la iniciativa y el
documento de invariantes. **Son CINCO en total**, y sólo tres son de `F5`:

| sede | clase | ¿la corrige `F5`? |
|---|---|---|
| `(a)`, bloque de aviso | material APROBADO | **SÍ** — sólo `F5` puede tocarlo |
| `(b)`, sin bloque de aviso | material APROBADO | **SÍ** — se le crea |
| [`docs/rediseno/README.md`](README.md) | índice del rediseño | **SÍ** — se actualiza con `E2`…`E6` y con `(g)` |
| [`docs/evolucion/03-INVARIANTES.md`](../evolucion/03-INVARIANTES.md) | evidencia de proceso | **NO** — es derivado, y su alineación es de `F6` |
| [`docs/evolucion/00-INDICE.md`](../evolucion/00-INDICE.md) | índice de la iniciativa, DERIVADO | **NO** — su alineación es de `F6` |

**Se declara expresamente en vez de callarlo:** dos de las cinco quedan sin alinear al
terminar `F5`, porque son derivados y su fase es `F6`. **Quien las lea después de `F5` verá
un inventario más corto que el del árbol**, y ésa es la razón por la que la regla de abajo
manda derivar y no escribir.

### Y la regla que impide que vuelva a discrepar

```text
EL INVENTARIO DE ENMIENDAS VIGENTES SE DERIVA, NO SE ESCRIBE:

  ls -1 docs/rediseno/a-ENMIENDA-E*.md

Una sede que enumere enmiendas a mano al lado de un directorio que crece vuelve a caducar.
```

> **Qué es esta fila y qué no es.** Su origen es una **observación** que la consolidación
> canónica registró, y el propio corpus dice de ella que **ningún gate la ha adjudicado, no
> lleva identificador de gate y no tiene severidad asignada**. Esta enmienda **no le asigna
> ninguna**. Se corrige porque su sede es material aprobado, su fase declarada es `F5`, y
> dejarla habría hecho que la checklist cerrara con el inventario todavía discrepando.

**PRUEBA POSTERIOR:** que las sedes que enumeran las enmiendas vigentes coincidan entre sí y
con el árbol, y que `(b)` declare que está enmendada.

## `E5.5` — Impacto

```text
SOBRE (b)     una cita corregida, una lista renumerada sin tocar el texto de sus reglas,
              un bloque de aviso de enmiendas NUEVO, y UNA MARCA DE REMISIÓN a `E2`
SOBRE (a)     dos recuentos marcados, el bloque de aviso actualizado, y UNA MARCA DE
              REMISIÓN a `E2`
SOBRE E1      un cardinal sustituido por su comando de derivación
SOBRE LA      ninguna. NINGUNA de las cuatro correcciones cambia una norma, una composición
NORMA         ni una obligación
```

## `E5.6` — Las dos marcas de remisión a `E2` que nunca se insertaron

**`E1` fijó la mecánica: bloque de aviso en la cabecera MÁS marcas de remisión en línea, en
los puntos exactos que la enmienda sustituye. `E2` no la siguió**, y sus puntos sustituidos
quedaron sin marca durante meses:

```bash
grep -c '\[E2' docs/rediseno/a-CAPACIDADES-APROBADA.md      # antes de E5: 0
grep -c '\[E2' docs/rediseno/b-RECORRIDO-APROBADA.md        # antes de E5: 0
```

### Texto de `(a)` y `(b)` que AMPLÍA

```text
(a) a.9, encabezado   el requisito del Owner sobre el estado operativo recibe la marca
                      `[E2: del repositorio ADS de CONTROL — ver E2.1]`

(b) b.14              el apartado de reanudación recibe la marca `[E2]`, que remite a la
                      reanudación MULTI-FUENTE de `E2.3`
```

**Ninguna de las dos cambia una palabra del texto normativo:** señalan dónde hay que leer
`E2` para saber qué rige, que es exactamente lo que una marca de remisión hace.

**PRUEBA POSTERIOR:** que toda enmienda vigente que sustituya un punto de `(a)` o de `(b)`
deje su marca en ese punto, y que el recuento se derive.

## `E5.7` — Trazabilidad

| fila de la checklist | qué corrige | apartado |
|---|---|---|
| `E5-1` de la sede | la cita a un predicado equivocado | `E5.1` |
| `E5-2` de la sede | la lista mal numerada | `E5.2` |
| `E5-4` de la sede | el recuento de marcas de remisión | `E5.3` |
| `OC-2` del corpus | el inventario de enmiendas vigentes | `E5.4` |
| la mecánica de `E1` | las dos marcas de remisión a `E2`, que nunca se insertaron | `E5.6` |

**La fila `E5-3` de la sede NO está aquí**, y se dice para que nadie la busque: era la
grafía, era una elección real del Owner, y su resolución **no exige enmendar la fuente** —
manda la grafía de la fuente aprobada, y lo que se alinea es el derivado, en `F6`.
