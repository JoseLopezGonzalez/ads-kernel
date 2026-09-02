# BORRADOR · `B-08` · La grafía canónica de dos identificadores

```text
ESTADO-DEL-BORRADOR: NO_APROBADO
PENDIENTE-DECISION-DEL-OWNER: D-08
ENTREGABLES: F5-E · F5-A
PRESIONES: PN-16 · PN-18
FILAS DE LA MATRIZ: F5-OB-16 · F5-OB-17
```

> **ESTO NO ES NORMA Y NO ESTÁ APROBADO.** Las dos presiones se responden con **un solo
> criterio**, aplicado a **dos identificadores**. Este borrador no elige el criterio.

---

## 1 · Los dos casos, y por qué son distintos entre sí

```text
CASO 1 · PN-16   la fuente aprobada escribe el identificador CON TILDE en su única
                 aparición normativa, y TODO el aparato derivado lo escribe SIN TILDE.
                 Instancias construidas en el kernel: CERO
CASO 2 · PN-18   la fuente aprobada lo escribe CON TILDE en sus doce apariciones
                 normativas, y el KERNEL YA CONSTRUIDO usa LAS DOS a la vez
```

**No son la misma presión** —la segunda se registró precisamente porque la primera está
acotada por su propio texto a otro identificador, y ampliarla habría sido reescribir una
presión ya llevada al Owner—. **Pero se contestan con el mismo criterio**, y por eso van
juntas: responderlas por separado permite una respuesta incoherente que dejaría la
comprobación de grafía única sin poder exigir nada.

**Los recuentos NO se escriben: se derivan**, y esa disciplina se conserva aquí.

## 2 · Las dos salidas

<!-- ads-lint-ignore-start: marcadores estructurales de decisión pendiente -->

```text
SI D-08 = A · manda la fuente aprobada, CON TILDE              ← recomendada
   NO SE ENMIENDA la especificación de recorrido. Las dos presiones quedan RESUELTAS en
   vez de retiradas, que es la salida que su propia sede describe.
   TRABAJO POSTERIOR, y es de F6, NO de F5:
     · alinear el aparato derivado del primer identificador
     · alinear las apariciones sin tilde del kernel construido y de los packs
   Y ENTONCES la comprobación de grafía única pasa a poder exigir UNA sola grafía en todo
   el corpus vigente, con las citas históricas marcadas como tales

SI D-08 = B · manda la grafía SIN TILDE
   SE ENMIENDA la especificación de recorrido: la aparición normativa del primer
   identificador, y las doce del segundo.
   TRABAJO POSTERIOR de F6: alinear lo poco que quede desalineado.
   ESTE BORRADOR REGISTRA, sin decidir, que esta salida enmienda la fuente para
   adaptarla a su propio derivado, lo que invierte la regla de precedencia del corpus
```

<!-- ads-lint-ignore-end -->

## 3 · Lo que NO alcanza

```text
NO CAMBIA   qué exige la participación, ni su ancla, ni su cardinalidad. Sólo cómo se
            escribe su nombre
NO ALCANZA  a ninguna otra regla
```

## 4 · Trazabilidad

| presión | fila | decisión | qué desbloquea |
|---|---|---|---|
| `PN-16` | `F5-OB-16` | `D-08` | la materialización del identificador en `F6` |
| `PN-18` | `F5-OB-17` | `D-08` | que el kernel construido deje de usar las dos grafías a la vez |

**Prueba prevista:** un barrido que exija **una sola grafía** en todo el corpus vigente, con
las citas históricas marcadas como tales, y con los recuentos derivados y no escritos.
