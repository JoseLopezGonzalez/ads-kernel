# BORRADOR · `B-09` · La checklist editorial sobre material aprobado

```text
ESTADO-DEL-BORRADOR: NO_APROBADO
PENDIENTE-DECISION-DEL-OWNER: R-02
ENTREGABLE: F5-E
FILAS DE LA MATRIZ: F5-OB-18 · F5-OB-19 · F5-OB-20 · F5-OB-21
```

> **ESTO NO ES NORMA Y NO ESTÁ APROBADO.** Todo lo de aquí tiene **texto final calculable
> sin decidir nada**, y ninguna fila cambia norma alguna. Lo que falta es el acto: sólo `F5`
> puede tocar material aprobado, y su autoridad declarada es «`F5`, con aprobación del
> Owner». **Nada de esto se ha aplicado.**
>
> **La cuarta fila de la checklist de origen NO está aquí.** Es la grafía, es una elección
> real del Owner, y vive en [`B-08-GRAFIA-CANONICA.md`](B-08-GRAFIA-CANONICA.md).

**Todas las líneas de abajo están verificadas contra el árbol de este commit.**

---

## 1 · Una cita a un predicado equivocado · `F5-OB-18`

**Sede:** `docs/rediseno/b-RECORRIDO-APROBADA.md` **L358**.

```text
DICE          «Un `devuelto` sin paquete de corrección deja al item en `en espera` (P7)»
PASA A DECIR  «Un `devuelto` sin paquete de corrección deja al item en `en espera` (P9)»
```

**Por qué es mecánica y no un criterio:** el propio documento define el primer predicado como
«→ `activo`» y el segundo como «→ `en espera`», y `devuelto` está entre los casos del
segundo. **Y el mismo documento ya lo usa bien en L255**, donde escribe «`activo` (P7) … `en
espera` (P9)». El texto final es un carácter y no admite otra lectura.

**Prueba posterior:** que toda cita de un predicado en el recorrido aprobado case con el
predicado que ese número define.

---

## 2 · Una lista mal numerada · `F5-OB-19`

**Sede:** `docs/rediseno/b-RECORRIDO-APROBADA.md` **L459–L473**, verificado contra el árbol de este commit. La sede de origen escribe «L462–472»; el rango real empieza en L459 y su última línea de continuación es L473.

```text
DICE          la secuencia va 1, 2, 5, 3, 4 — el bloque numerado «5.» está físicamente
              entre el «2.» y el «3.»
PASA A DECIR  1, 2, 3, 4, 5, CONSERVANDO EL TEXTO DE CADA REGLA SIN TOCAR UNA PALABRA
```

**Cómo se aplica, exactamente:** el bloque hoy numerado `5.` se traslada detrás del bloque
`4.`, y la numeración pasa a ser correlativa. **Ningún texto de regla cambia.**

> **CONDICIÓN PREVIA OBLIGATORIA, y es parte de la fila, no un extra.** Antes de renumerar
> hay que comprobar por barrido que **ninguna otra sede cita esas reglas por su número**.
> Este borrador lo comprobó sobre el árbol de hoy y no encontró citas por número — **y el
> barrido debe repetirse en el momento de aplicar**, porque las enmiendas a la tabla de
> rutas pueden introducir referencias nuevas.

**Orden:** esta fila se aplica **después** de las enmiendas de
[`B-06-RUTAS-DE-b16.md`](B-06-RUTAS-DE-b16.md), por esa misma razón.

**Prueba posterior:** que la secuencia de una lista numerada del recorrido aprobado sea
estrictamente creciente.

---

## 3 · Un recuento de marcas que el árbol no da · `F5-OB-20`

**Sedes:** `docs/rediseno/a-ENMIENDA-E1-ENC.md` **L196–L197**, y
`docs/rediseno/a-CAPACIDADES-APROBADA.md` **L269** y **L276**.

**El estado real, derivado y no escrito:**

```bash
grep -n '\[E1' docs/rediseno/a-CAPACIDADES-APROBADA.md         # incluye la frase anunciadora
grep -c '\[E1[ :→]' docs/rediseno/a-CAPACIDADES-APROBADA.md    # SÓLO las marcas reales
```

El primero devuelve **siete líneas**, de las cuales **L18 no es una marca**: es la frase que
anuncia las marcas, y escribe `[E1]` cerrado. El segundo la excluye exigiendo que tras `[E1`
venga un separador, y devuelve **las marcas reales**: cinco que sustituyen y **una que
confirma**. Y **dos recuentos quedan sin marcar**, en L269 y L276.

> **El comando que se propone como remedio es el SEGUNDO, y la distinción importa:** el
> primero sobrecuenta en uno, y consagrarlo como derivación oficial repetiría —en la única
> fila que existe para que la cifra no pueda volver a estar mal— exactamente el error que
> esa fila corrige.

**La parte completamente determinada:**

```text
(a) L269   DICE          «Las 14 son el **catálogo base**, no un catálogo universal cerrado»
           PASA A DECIR  «Las 14 `[E1: 15]` son el **catálogo base**, no un catálogo
                         universal cerrado»

(a) L276   DICE          «CATÁLOGO BASE DEL KERNEL     capacidades universales · 14 ·
                         códigos reservados»
           PASA A DECIR  «CATÁLOGO BASE DEL KERNEL     capacidades universales ·
                         14 `[E1: 15]` · códigos reservados»
```

**Y el remedio que impide que la fila vuelva a caducar** — que es el que este borrador
propone, porque el cardinal escrito a mano ya ha caducado una vez:

```text
E1 L196-197  DICE          «siete MARCAS DE REMISIÓN `[E1]` insertadas en línea … cinco
                           recuentos y dos párrafos»
             PASA A DECIR  «MARCAS DE REMISIÓN `[E1]` insertadas en línea, en los puntos
                           exactos que esta enmienda sustituye. EL NÚMERO NO SE ESCRIBE:
                           se deriva con
                             grep -c '\[E1[ :→]' docs/rediseno/a-CAPACIDADES-APROBADA.md»
```

> **LA PARTE QUE EXIGE CRITERIO, declarada y no disimulada.** El texto vigente distingue
> «cinco recuentos y dos párrafos», y **una de las marcas es de CONFIRMACIÓN y no de
> sustitución**. Si el cardinal se sustituye por su comando de derivación, la distinción
> deja de tener que cuadrar y la cuestión desaparece. **Ésa es la razón de fondo del remedio
> propuesto**, y por eso la fila se clasifica como parcialmente determinada.

**Y un aviso de alcance:** el mismo cardinal aparece en un tercer documento que **no es
material aprobado**. Su corrección **no es de `F5`**. Si `F5` cambia el cardinal aquí sin
decir nada, quedan tres sedes y dos verdades: la enmienda debe **declararlo expresamente**.

**Prueba posterior:** que el número de marcas que la enmienda declara coincida con las que
el material aprobado lleva, **derivado por barrido y no escrito**.

---

## 4 · El inventario de enmiendas vigentes, que no coincide · `F5-OB-21`

**Sedes:** el bloque de aviso de `docs/rediseno/a-CAPACIDADES-APROBADA.md` **L9–L18**, la
tabla de estado de `docs/rediseno/README.md` **L22–L32**, y
`docs/rediseno/b-RECORRIDO-APROBADA.md`, **que no tiene bloque de aviso**.

**El estado real, derivado:**

```bash
grep -c '\[E2' docs/rediseno/a-CAPACIDADES-APROBADA.md        # marcas de la segunda enmienda en (a)
grep -c '\[E1\|\[E2' docs/rediseno/b-RECORRIDO-APROBADA.md    # marcas en el recorrido aprobado
```

**Los dos devuelven cero.** Es decir: **la segunda enmienda no dejó ninguna marca ni ninguna
entrada de aviso**, aunque ella misma declara que enmienda a las dos secciones. La primera
fijó la mecánica —«las enmiendas futuras se numeran y se listan en el aviso de cabecera, con
la misma mecánica»— y la segunda no la siguió.

**Lo que la corrección hace:**

```text
1  añadir la fila de la segunda enmienda al bloque de aviso de la sección de capacidades
2  añadir esa misma fila a la tabla de estado del índice de la especificación
3  CREAR el bloque de aviso de enmiendas vigentes en el recorrido aprobado, que hoy NO
   EXISTE pese a estar enmendado
4  insertar las marcas de remisión en línea que la mecánica exige
5  y, para que no vuelva a discrepar, DERIVAR el inventario en vez de escribirlo
```

> **QUÉ ES ESTA FILA Y QUÉ NO ES.** Su origen es una **observación** que la consolidación
> canónica registró, y el propio corpus dice de ella que **ningún gate la ha adjudicado, no
> lleva identificador de gate y no tiene severidad asignada**. Este borrador **no le asigna
> ninguna**. Se incluye porque su sede es material aprobado y su fase declarada es `F5`, y
> porque dejarla fuera haría que `F5-E` cerrara con el inventario todavía discrepando.

**Prueba posterior:** que el inventario de enmiendas vigentes se **derive** y no se escriba,
de modo que no pueda volver a discrepar entre sedes.

---

## 5 · Lo que este borrador NO toca, y por qué

```text
NO TOCA   la grafía. Es elección real del Owner y vive en B-08
NO TOCA   los diez hallazgos vivos. Ninguno se declara superado, y varios esperan un
          instrumento que es de F6
NO TOCA   la condición de cierre que exige comprobar por CLASE y no por instancia: exige
          escribir una regla nueva, que es especificación y no corrección editorial
NO TOCA   la deuda del propio corpus canónico. Ninguna de sus seis entradas bloquea F5, y
          este macrobloque no abre una tanda para corregirlas
NO TOCA   las dos observaciones sobre el kernel y el lenguaje canónico: siguen registradas
          sin corregir, porque ninguna obligación expresa de F5 las alcanza
```
