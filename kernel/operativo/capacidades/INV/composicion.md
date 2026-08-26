# INV — composición del equipo

```yaml ads:composicion
id: composicion:inv-documental
capacidad: INV
clase_de_trabajo: "pregunta que se contesta con fuentes, sin construir nada"
condicion: >
  La pregunta se puede contestar consultando fuentes, documentación o el propio repositorio,
  sin necesidad de medir contra el entorno real.
roles:
  - rol: INV/investigacion
    obligatorio: true
    agentes: "1"
combinables: []
independientes:
  - rol: INV/investigacion
    de: ["ninguno en esta composición: no hay experimento que sesgar"]
    motivo: "se declara expresamente para que la ausencia de separación sea una decisión y no un olvido"
ampliacion: >
  Si contestar exige medir contra el entorno real, se añade CON/experimental y la
  composición pasa a inv-con-experimento.
reduccion: "no admite reducción."
retirada: "al entregar el informe al consumidor declarado."
```

```yaml ads:composicion
id: composicion:inv-con-experimento
capacidad: INV
clase_de_trabajo: "pregunta que exige construir para obtener evidencia"
condicion: >
  La respuesta exige medir contra el entorno real, y sólo puede obtenerse construyendo un
  spike, un simulador o instrumentación.
roles:
  - rol: INV/investigacion
    obligatorio: true
    agentes: "1"
  - rol: CON/experimental
    obligatorio: true
    agentes: "1"
combinables:
  - roles: [INV/investigacion, CON/experimental]
    motivo: "en un experimento corto, formular y medir son el mismo trabajo"
    condicion: "la evidencia NO sostiene una decisión difícilmente reversible"
independientes:
  - rol: CON/experimental
    de: [INV/investigacion]
    motivo: >
      quien formula la hipótesis tiende a construir el experimento que la confirma, y la
      decisión que se apoye en él heredará ese sesgo
ampliacion: >
  Dos experimentos alternativos en paralelo cuando hay que comparar dos caminos, con el
  criterio de comparación escrito antes de empezar.
reduccion: >
  CON/experimental se retira si al acotar la pregunta resulta que puede contestarse con
  fuentes.
retirada: "al entregar el informe y ejecutar el criterio de descarte del experimento."
```
