# ARQ — composición del equipo

```yaml ads:composicion
id: composicion:arq-diagnostico-corto
capacidad: ARQ
clase_de_trabajo: "defecto cuyo diagnóstico se cierra leyendo una zona acotada"
condicion: >
  El item es de tipo DEF, el fallo se reproduce con las condiciones del encuadre, y la zona
  afectada está identificada en el encuadre o en el primer paso del diagnóstico.
roles:
  - rol: ARQ/diagnostico
    obligatorio: true
    agentes: "1"
  - rol: ARQ/encaje
    obligatorio: false
    agentes: "el mismo agente que diagnostico"
    condicion: "la corrección toca contratos o afecta a más de un módulo"
combinables:
  - roles: [ARQ/diagnostico, ARQ/encaje]
    motivo: "en una zona acotada, encontrar la causa y planificar la corrección son el mismo acto de lectura"
independientes:
  - rol: ARQ/diagnostico
    de: ["el rol de CON que construyó el código donde está la causa, cuando el defecto es reciente"]
    motivo: "quien escribió el código busca la causa donde cree que está, no donde está"
ampliacion: >
  Si el diagnóstico revela que la causa está en una decisión de producto o de forma, el item
  cambia de proceso y ARQ deja de ser propietario global.
reduccion: "no admite reducción."
retirada: "al entregar el diagnóstico con su reproducción."
```

```yaml ads:composicion
id: composicion:arq-plan-completo
capacidad: ARQ
clase_de_trabajo: "planificación técnica de un item que toca contratos o excede un módulo"
condicion: >
  El item cumple C-ARQ por tocar contratos o estructura, o porque el radio de impacto excede
  un módulo, y no es un diagnóstico de defecto.
roles:
  - rol: ARQ/encaje
    obligatorio: true
    agentes: "1"
  - rol: ARQ/diagnostico
    obligatorio: false
    agentes: "1"
    condicion: "el item es una deuda cuya causa hay que establecer antes de planificar"
combinables:
  - roles: [ARQ/encaje, ARQ/diagnostico]
    motivo: "en una deuda acotada, causa y plan se establecen a la vez"
    condicion: "la deuda afecta a un solo módulo"
independientes:
  - rol: ARQ/encaje
    de: ["ninguno en esta composición: el plan lo revisa VER, no otro rol de ARQ"]
    motivo: "se declara expresamente para que la ausencia de separación sea una decisión y no un olvido"
ampliacion: >
  Con un radio que excede cinco módulos, se reparte la medición entre varios agentes de
  ARQ/encaje por zona, con un integrador declarado que escribe el radio único.
reduccion: "ARQ/diagnostico se retira cuando la causa ya está establecida por otro item."
retirada: "al depositar el plan y entregar el grafo de paquetes a DSP."
```
