# APR — composición del equipo

```yaml ads:composicion
id: composicion:apr-senal
capacidad: APR
clase_de_trabajo: "convertir una señal en criterio, o declarar que no es promovible"
condicion: >
  Existe señal real: un item cerró con learning_candidate distinto de none, o hubo un
  incidente, o una revisión de circuito, o una promoción a upstream.
roles:
  - rol: APR/promocion
    obligatorio: true
    agentes: "1"
combinables: []
independientes:
  - rol: APR/promocion
    de: ["las capacidades que participaron en el item del que sale el aprendizaje"]
    motivo: >
      quien vivió el recorrido promueve a regla su propia decisión reciente, y así el ledger
      se llena de reglas que sólo valían aquella vez
ampliacion: >
  En una revisión de circuito que abarca varios items, se reparte la búsqueda de ocurrencias
  por materia, con un integrador declarado que escribe las reglas.
reduccion: >
  Ninguna. Y APR no se materializa sin señal real: la comprobación de aprendizaje del cierre
  se ejecuta SIN crear paquete (b.10).
retirada: "al escribir la entrada del ledger, o el veredicto de no promovible."
```
