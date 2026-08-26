# ENC — composición del equipo

`ENC` se materializa siempre, pero **no siempre con tres agentes**. La composición se
elige por la clase de expresión que entra, no por costumbre.

```yaml ads:composicion
id: composicion:enc-conversacion-simple
capacidad: ENC
clase_de_trabajo: "expresión que se resuelve sin item, o candidato de anclaje corto"
condicion: >
  La expresión es observación, nota u orden sobre item existente, O es candidato cuyo
  anclaje se resuelve con menos de cinco búsquedas y no toca materia reservada.
roles:
  - rol: ENC/interlocutor
    obligatorio: true
    agentes: "1"
  - rol: ENC/anclaje
    obligatorio: true
    agentes: "el mismo agente que interlocutor"
    condicion: "el anclaje se cierra con menos de cinco búsquedas"
combinables:
  - roles: [ENC/interlocutor, ENC/anclaje]
    motivo: "con menos de cinco búsquedas, el contexto de la conversación no desplaza al de la búsqueda"
    condicion: "el anclaje se cierra con menos de cinco búsquedas"
independientes:
  - rol: ENC/interlocutor
    de: ["ninguno en esta composición: no hay crítica, porque la incertidumbre es baja y el nivel de Owner no es obligatorio"]
    motivo: "se declara expresamente que aquí no se exige independencia, para que su ausencia sea una decisión y no un olvido"
ampliacion: >
  Si el anclaje supera cinco búsquedas o aparece un duplicado dudoso, se separa ENC/anclaje
  en su propio agente y la composición pasa a enc-candidato-completo.
reduccion: >
  No admite reducción: ENC/interlocutor es el mínimo absoluto. Sin él no hay quien escuche.
retirada: >
  Al entregar el encuadre, la anotación o el evento de orden. El equipo no permanece entre
  expresiones: se materializa por expresión.
```

```yaml ads:composicion
id: composicion:enc-candidato-completo
capacidad: ENC
clase_de_trabajo: "candidato a trabajo con anclaje largo o incertidumbre media"
condicion: >
  La expresión es candidato a trabajo Y el anclaje exige recorrer más de cinco búsquedas o
  varias zonas del repositorio, Y la incertidumbre declarada no es alta.
roles:
  - rol: ENC/interlocutor
    obligatorio: true
    agentes: "1"
  - rol: ENC/anclaje
    obligatorio: true
    agentes: "1, distinto del interlocutor"
combinables: []
independientes:
  - rol: ENC/anclaje
    de: [ENC/interlocutor]
    motivo: "el contexto de la conversación desplaza al de la búsqueda y aparecen falsos «no existe»"
ampliacion: >
  Si al medir la incertidumbre resulta alta, o el nivel de Owner calculado es obligatorio,
  se añade ENC/critica-de-encuadre y la composición pasa a enc-alta-incertidumbre.
reduccion: >
  Si el anclaje se cierra antes de las cinco búsquedas, vuelve a enc-conversacion-simple y
  el segundo agente se retira sin entregar nada más que su traza.
retirada: >
  ENC/anclaje se retira al entregar el dosier. ENC/interlocutor, al entregar el encuadre.
```

```yaml ads:composicion
id: composicion:enc-alta-incertidumbre
capacidad: ENC
clase_de_trabajo: "idea inmadura, incertidumbre alta, materia reservada o proceso DIR, AUD o INC"
condicion: >
  La incertidumbre declarada es alta en cualquier eje, O el nivel de intervención del Owner
  calculado es obligatorio, O el tipo de proceso propuesto es DIR, AUD o INC.
roles:
  - rol: ENC/interlocutor
    obligatorio: true
    agentes: "1"
  - rol: ENC/anclaje
    obligatorio: true
    agentes: "1, distinto del interlocutor"
  - rol: ENC/critica-de-encuadre
    obligatorio: true
    agentes: "1, distinto de los otros dos"
combinables: []
independientes:
  - rol: ENC/critica-de-encuadre
    de: [ENC/interlocutor, ENC/anclaje]
    motivo: "quien interpretó no encuentra el hueco de su propia interpretación: encuentra los que evitó"
  - rol: ENC/anclaje
    de: [ENC/interlocutor]
    motivo: "el contexto de la conversación desplaza al de la búsqueda y aparecen falsos «no existe»"
ampliacion: >
  En una idea inmadura que exige explorar dirección de forma, se añade una consulta a DIS
  en modo consulta. La consulta NO añade rol a ENC: DIS conserva su propia custodia.
reduccion: >
  Si tras conversar la incertidumbre baja a media en todos los ejes y el nivel de Owner deja
  de ser obligatorio, la crítica sigue siendo obligatoria: ya se emitió el trabajo y su
  dictamen forma parte del gate. No se retira para ahorrar una lectura.
retirada: >
  Cada rol se retira al entregar su artefacto. La ficha del vivero, si la idea sigue
  inmadura, no tiene equipo asignado: es memoria, no cola.
```

## Cuándo NO se materializa nada

```text
· el Owner hace una pregunta sobre el estado del sistema      → la responde DSP, no ENC
· el Owner dice «Continúa»                                    → es b.14, no un encuadre
· llega un evento externo (CI, telemetría, incidente)         → entra por su capacidad,
                                                                no por la puerta del Owner
```

ENC es la puerta **del Owner**. No es la puerta de todo lo que ocurre.
