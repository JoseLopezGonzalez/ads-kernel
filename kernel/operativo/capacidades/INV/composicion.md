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
combinables: []
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
  fuentes; entonces la composición vuelve a inv-documental.
retirada: "al entregar el informe y ejecutar el criterio de descarte del experimento."
```

```yaml ads:composicion
id: composicion:inv-experimento-corto
capacidad: INV
clase_de_trabajo: "experimento corto cuya evidencia no sostiene una decisión difícilmente reversible"
condicion: >
  Contestar exige construir, Y la decisión que consumirá la respuesta es reversible: no toca
  materia reservada, no compromete al producto a largo plazo y no destruye nada.
roles:
  - rol: INV/investigacion
    obligatorio: true
    agentes: "1"
  - rol: CON/experimental
    obligatorio: true
    agentes: "el mismo agente que investigacion"
combinables:
  - roles: [INV/investigacion, CON/experimental]
    motivo: "en un experimento corto y reversible, formular y medir son el mismo trabajo y separarlos es ceremonia"
independientes:
  - rol: INV/investigacion
    de: ["ninguno en esta composición: la decisión que consumirá la evidencia es reversible"]
    motivo: >
      se declara expresamente que aquí NO se exige independencia, y por qué: el sesgo de
      confirmación existe igual, pero su consecuencia es revertible y el coste de separar
      excede al del error
ampliacion: >
  Si al trabajar resulta que la decisión NO es reversible, la composición pasa a
  inv-con-experimento y CON/experimental se separa en otro agente ANTES de medir.
reduccion: "no admite reducción."
retirada: "al entregar el informe y ejecutar el criterio de descarte."
```
