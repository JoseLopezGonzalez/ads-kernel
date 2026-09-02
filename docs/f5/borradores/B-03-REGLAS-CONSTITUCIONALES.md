# BORRADOR · `B-03` · Las reglas constitucionales frente al circuito de arranque

```text
ESTADO-DEL-BORRADOR: NO_APROBADO
PENDIENTE-DECISION-DEL-OWNER: D-04
ENTREGABLE: F5-G
PRESION: PN-15
FILA DE LA MATRIZ: F5-OB-04
```

> **ESTO NO ES NORMA Y NO ESTÁ APROBADO.** Y hay una razón adicional para decirlo aquí: la
> regla presionada declara que **el criterio que aprueba la existencia del sistema no lo
> puede fijar el sistema**. Un borrador escrito por un agente **no puede** decidir esto, y
> este fichero no lo intenta.

---

## 1 · El conflicto, en una frase

La constitución fija el gate de salida del circuito inicial **con contenido** —un plazo, diez
entregables y cuatro prohibiciones— y declara que **no es negociable por el sistema**. El
diseño nuevo fija otro gate distinto, **sin** ese contenido. **No hay lectura bajo la cual
los dos sean el mismo gate**, y el material aprobado **no contiene ninguna derogación
válida** de las cuatro reglas.

**Consecuencia vigente, y hay que decirla:** hasta que el Owner decida, **las cuatro reglas
siguen vigentes**, y una instalación real tendría que satisfacer las dos cosas o esperar.

## 2 · La forma que la enmienda tiene que tener

**La prueba posterior es explícita y no admite otra sede:** hace falta **una fila por cada
una de las cuatro reglas** en la lista de efecto sobre el kernel de `(a)`, que la nombre y
declare su disposición —derogada, sustituida, ajustada, conservada, o pendiente con plazo—.
**Una fila global no la satisface**, y la fila que ya existe en otra sección **no puede**
satisfacerla.

## 3 · Esqueleto de la enmienda, por opción

<!-- ads-lint-ignore-start: marcadores estructurales de decisión pendiente -->

```text
ENMIENDA E<n> A LA SECCIÓN (a) · efecto sobre las reglas del circuito de arranque

  identificador   E<n>
  enmienda a      docs/rediseno/a-CAPACIDADES-APROBADA.md · a.11
  fecha           PENDIENTE-DECISION-DEL-OWNER: D-04
  autoridad       Owner
  motivo          fijar, regla a regla, la disposición de las cuatro reglas del circuito
                  de arranque frente al diseño de macrocircuitos
  estado          PENDIENTE-DECISION-DEL-OWNER: D-04

  LA TABLA, con UNA FILA POR REGLA. Los valores dependen de D-04:

  | regla                        | disposición | qué pasa a regir |
  |------------------------------|-------------|------------------|
  | macrocircuitos               | ?           | ?                |
  | gates entre circuitos        | ?           | ?                |
  | gate fijo del circuito 0     | ?           | ?                |
  | línea base de producto       | ?           | ?                |

  SI D-04 = A · CONSERVAR
     las cuatro filas dicen CONSERVADA, y se añade una quinta declaración: el circuito
     nuevo es la INSTRUMENTACIÓN del gate constitucional, no su sustituto. Hay que
     demostrar la correspondencia entregable a entregable, y esa demostración es parte
     de la enmienda.

  SI D-04 = B · SUSTITUIR
     el gate del circuito 0 dice SUSTITUIDA, y el Owner declara EXPRESAMENTE el gate
     nuevo con su plazo, sus entregables y sus prohibiciones. Este borrador NO lo
     redacta: la constitución reserva esa redacción al Owner y no al sistema.

  SI D-04 = C · AJUSTAR
     plazo y prohibiciones dicen CONSERVADA; la lista de diez entregables dice AJUSTADA,
     con la correspondencia escrita salida a salida.
```

<!-- ads-lint-ignore-end -->

## 4 · El orden, que importa y está escrito

**Primero la fuente, después el derivado.** La enmienda entra en `(a)`; **después**, `F6`
actualiza la constitución en prosa, la guía de arranque y el resto de derivados. **Al revés
es el modo de fallo que el corpus registra expresamente.**

## 5 · Trazabilidad

| presión | fila | decisión | qué desbloquea |
|---|---|---|---|
| `PN-15` | `F5-OB-04` | `D-04` | la ejecución real del circuito de arranque por la ruta nueva, y con ella los cuatro macrocircuitos de `F6` |

**Prueba prevista:** una fila por cada una de las cuatro reglas, nombrándola y declarando su
disposición. **Condición de cierre registrada:** es la que el corpus tiene inscrita para
`F5` con propietario «el Owner».
