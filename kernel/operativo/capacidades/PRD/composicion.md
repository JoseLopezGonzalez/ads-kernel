# PRD — composición del equipo

```yaml ads:composicion
id: composicion:prd-alcance-rutinario
capacidad: PRD
clase_de_trabajo: "item dentro de una dirección de producto ya aprobada"
condicion: >
  Existe dirección de producto aprobada que cubre este item, y el alcance no amplía lo que
  el producto es: extiende un patrón o resuelve un hueco de una expectativa ya escrita.
roles:
  - rol: PRD/definicion
    obligatorio: true
    agentes: "1"
  - rol: PRD/criterio-de-exito
    obligatorio: true
    agentes: "el mismo agente que definicion"
combinables:
  - roles: [PRD/definicion, PRD/criterio-de-exito]
    motivo: "en alcance rutinario, la frontera y su comprobación se deciden en el mismo acto"
independientes:
  - rol: PRD/criterio-de-exito
    de: ["ninguno en esta composición: el alcance no es de primera dirección"]
    motivo: "se declara expresamente que aquí no se exige separación, para que su ausencia sea una decisión"
ampliacion: >
  Si al definir el alcance resulta que amplía lo que el producto es, la composición pasa a
  prd-direccion-nueva y los roles se separan.
reduccion: "no admite reducción: los dos roles son el mínimo, aunque los ocupe un agente."
retirada: "al depositar la capa de intención y pasar el gate."
```

```yaml ads:composicion
id: composicion:prd-direccion-nueva
capacidad: PRD
clase_de_trabajo: "primera dirección de producto, o alcance que cambia lo que el producto es"
condicion: >
  No existe dirección de producto que cubra este item, o el alcance amplía lo que el
  producto es, o el item procede de un DIR.
roles:
  - rol: PRD/definicion
    obligatorio: true
    agentes: "1"
  - rol: PRD/criterio-de-exito
    obligatorio: true
    agentes: "1, distinto del anterior"
combinables: []
independientes:
  - rol: PRD/criterio-de-exito
    de: [PRD/definicion]
    motivo: >
      quien define el alcance tiende a escribir criterios que describen su propia propuesta
      en lugar de medir el resultado, y así el item se verifica contra sí mismo
ampliacion: >
  Se añade una consulta a INV en modo consulta cuando el alcance depende de evidencia que
  no existe. La consulta no añade rol a PRD.
reduccion: "ninguna: es materia del Owner y la separación de roles es obligatoria."
retirada: "al confirmar el Owner el alcance y quedar escritos los criterios."
```
