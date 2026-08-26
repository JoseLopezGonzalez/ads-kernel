# DOM — composición del equipo

```yaml ads:composicion
id: composicion:dom-consulta
capacidad: DOM
clase_de_trabajo: "condiciones de dominio en modo consulta, sin cambio de esquema"
condicion: >
  El item cumple C-DOM pero no cambia el esquema ni el contenido de los datos: toca
  vocabulario, invariantes o contratos de lectura.
roles:
  - rol: DOM/modelo
    obligatorio: true
    agentes: "1"
combinables: []
independientes:
  - rol: DOM/modelo
    de: ["ninguno en esta composición: no hay migración que certificar"]
    motivo: "se declara expresamente para que la ausencia de separación sea una decisión y no un olvido"
ampliacion: >
  Si al escribir las condiciones aparece un cambio de esquema, la composición pasa a
  dom-migracion y DOM/migracion entra con agente propio.
reduccion: "no admite reducción."
retirada: "al entregar las condiciones y emitir la revisión posterior."
```

```yaml ads:composicion
id: composicion:dom-migracion
capacidad: DOM
clase_de_trabajo: "cambio de esquema o de contenido de los datos"
condicion: >
  El item cambia el esquema, migra contenido o altera un contrato de datos de escritura.
roles:
  - rol: DOM/modelo
    obligatorio: true
    agentes: "1"
  - rol: DOM/migracion
    obligatorio: true
    agentes: "1, distinto del anterior"
combinables: []
independientes:
  - rol: DOM/migracion
    de: [DOM/modelo]
    motivo: >
      quien declara el invariante no debe certificar que su propia migración lo conserva:
      la prueba se diseña, sin querer, para pasar
ampliacion: >
  Con datos de varios sistemas, se añade un agente de DOM/migracion por origen, con
  DOM/modelo como integrador declarado de los invariantes comunes.
reduccion: "ninguna: la separación es la razón de ser de esta composición."
retirada: "cuando la migración y su reversión están probadas y entregadas a ENT."
```
