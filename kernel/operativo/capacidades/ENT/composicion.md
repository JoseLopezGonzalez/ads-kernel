# ENT — composición del equipo

```yaml ads:composicion
id: composicion:ent-entorno-no-productivo
capacidad: ENT
clase_de_trabajo: "despliegue a vista previa, staging o dispositivo de pruebas"
condicion: "el entorno de destino no es producción y el despliegue no es una publicación."
roles:
  - rol: ENT/despliegue
    obligatorio: true
    agentes: "1"
  - rol: ENT/observacion
    obligatorio: true
    agentes: "el mismo agente que despliegue"
combinables:
  - roles: [ENT/despliegue, ENT/observacion]
    motivo: "fuera de producción, el sesgo de interpretar las señales a favor no tiene consecuencias sobre usuarios reales"
independientes:
  - rol: ENT/observacion
    de: ["ninguno en esta composición: el entorno no es productivo"]
    motivo: "se declara expresamente para que la ausencia de separación sea una decisión y no un olvido"
ampliacion: >
  Si el despliegue de vista previa se convierte en publicación, la composición pasa a
  ent-produccion y los roles se separan.
reduccion: "no admite reducción."
retirada: "al cerrar la ventana de observación declarada."
```

```yaml ads:composicion
id: composicion:ent-produccion
capacidad: ENT
clase_de_trabajo: "despliegue a producción o publicación"
condicion: "el entorno de destino es producción, o el despliegue es una publicación."
roles:
  - rol: ENT/despliegue
    obligatorio: true
    agentes: "1"
  - rol: ENT/observacion
    obligatorio: true
    agentes: "1, distinto del anterior"
combinables: []
independientes:
  - rol: ENT/observacion
    de: [ENT/despliegue]
    motivo: >
      quien despliega interpreta las señales a favor de que su despliegue ha ido bien, y en
      producción ese sesgo lo pagan los usuarios
ampliacion: >
  En un incidente se añade ARQ/diagnostico en modo consulta desde el primer minuto: contener
  y diagnosticar a la vez acorta la ventana de daño.
reduccion: "ninguna: la separación es la razón de ser de esta composición."
retirada: "al cerrar la ventana con su registro completo de señales."
```
