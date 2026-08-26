# USO — composición del equipo

```yaml ads:composicion
id: composicion:uso-fuente-no-humana
capacidad: USO
clase_de_trabajo: "validación con telemetría, logs o dispositivo"
condicion: >
  Existe telemetría, logs o dispositivo físico capaz de producir evidencia del criterio que
  se valida, y ninguna persona tiene que ejecutar la tarea.
roles:
  - rol: USO/validacion
    obligatorio: true
    agentes: "1"
combinables: []
independientes:
  - rol: USO/validacion
    de: [CON/implementacion]
    motivo: "quien construyó interpreta la telemetría a favor de que su cambio ha funcionado"
ampliacion: >
  Si la evidencia no basta para el criterio, se añade un plan de validación humana y la
  composición pasa a uso-fuente-humana.
reduccion: "no admite reducción."
retirada: "al entregar la evidencia."
```

```yaml ads:composicion
id: composicion:uso-fuente-humana
capacidad: USO
clase_de_trabajo: "validación que exige que alguien ejecute la tarea"
condicion: >
  El criterio sólo puede validarse observando a una persona usar el producto: el Owner, un
  usuario o un operador.
roles:
  - rol: USO/validacion
    obligatorio: true
    agentes: "1"
combinables: []
independientes:
  - rol: USO/validacion
    de: [CON/implementacion, DIS/diseno-interaccion]
    motivo: >
      quien construyó o diseñó el flujo lo recorre sin dudar: validaría su memoria, no el
      producto
ampliacion: >
  Cuando la validación es de forma además de función, se coordina con DIS/validacion-de-uso
  y se ejecuta UNA sola sesión para las dos, no dos sesiones.
reduccion: "ninguna: la independencia es obligatoria cuando hay una persona delante."
retirada: "al cerrar el lote de validación con su registro."
```
