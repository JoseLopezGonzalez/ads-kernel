# Handoffs de Diseño con las demás capacidades

Forma del handoff y de la devolución: [`C5`](../contratos/C5-HANDOFF.md). Aquí están las
**instancias concretas**. Cada una responde: quién entrega qué · quién comprueba qué ·
quién puede devolver · con qué evidencia · qué pertenece al Owner · qué checkpoint viaja.

```text
                      PRD ──────► DIS ──────► ARQ ──────► CON
                       ▲           │  ▲                    │
                       │           ▼  └────────────────────┘
                      INV        DIS/critica          devolución por fidelidad
                                   │
                       USO ◄───────┴───────► VER ──────► ENT
```

---

```yaml ads:handoff
id: handoff:prd-a-dis
de: PRD
a: DIS
cuando: "el item cumple C-DIS y PRD ha depositado su capa de intención y criterio de éxito"
entrega:
  - "el resultado perseguido y el criterio de éxito, con su definición de fracaso"
  - "para quién es, en qué momento y con qué frecuencia se usa"
  - "qué queda expresamente fuera de alcance"
  - "las restricciones declaradas por el Owner, con su origen citado"
  - "las áreas premium que afecta, según memoria:areas-premium"
comprueba_al_recibir:
  - "el criterio de éxito es comprobable por alguien que no participó en definirlo"
  - "el fuera de alcance está escrito, no sólo el alcance"
  - "existe al menos una superficie identificada, o consta que la superficie está por decidir"
  - "las restricciones del Owner citan su origen y no son interpretaciones"
rechaza_si:
  - "el criterio de éxito es una actividad y no un resultado"
  - "no hay fuera de alcance escrito"
  - "el item no cumple realmente C-DIS y activarlo sería ceremonia"
devolucion: >
  DIS devuelve a PRD cuando el alcance exige una forma que no es operable en el entorno
  declarado por el pack, o cuando el criterio de éxito no permite decidir entre dos
  direcciones que lo cumplen igual.
evidencia_de_devolucion:
  - "las dos formas que cumplen igual el criterio, con lo que cada una implica"
  - "o la restricción física del pack que hace inoperable lo pedido, citada"
owner: "ninguna en el handoff. El Owner interviene dentro de DIS según a.8, no en la entrega."
checkpoint: "DIS lee de PRD: decisiones del Owner captadas y su fecha, para no volver a preguntarlas."
```

```yaml ads:handoff
id: handoff:dis-a-arq
de: DIS
a: ARQ
cuando: "la dirección o la superficie está especificada y el item cumple C-ARQ"
entrega:
  - "la especificación construible con sus cinco estados"
  - "la especificación de movimiento con sus grabaciones"
  - "los valores del sistema que la superficie usa"
  - "qué componentes existentes reutiliza y cuáles introduce"
comprueba_al_recibir:
  - "la especificación no exige decidir nada de forma para poder planificar"
  - "los componentes que introduce están declarados en el sistema"
  - "el movimiento tiene grabación, no sólo descripción"
rechaza_si:
  - "la especificación deja estados sin resolver y habría que inventarlos al planificar"
  - "el movimiento se entrega descrito sin grabación"
devolucion: >
  ARQ devuelve a DIS SÓLO trayendo alternativas de forma, nunca sólo la negativa (a.3).
  La devolución nombra la restricción y propone al menos un camino que conserve la intención.
evidencia_de_devolucion:
  - "el radio de impacto MEDIDO sobre las fuentes del alcance, no estimado"
  - "al menos una alternativa de forma que ARQ considera viable"
owner: "ninguna: en este handoff no hay materia de decisión del Owner."
checkpoint: "ARQ lee de DIS: nivel de novedad, direcciones descartadas y por qué, para no proponer una descartada como alternativa."
```

```yaml ads:handoff
id: handoff:dis-a-con
de: DIS
a: CON
cuando: "la especificación está aprobada y ARQ ha depositado su plan, o el item no cumple C-ARQ"
entrega:
  - "la especificación con los cinco estados y los valores del sistema"
  - "las grabaciones de movimiento con duración y curva"
  - "los puntos de adaptación y qué cambia en cada uno"
  - "qué patrón aplica y con qué alcance"
  - "las ocho cosas que no se simplifican en silencio, señaladas en la propia especificación"
comprueba_al_recibir:
  - "todo valor de la especificación pertenece al sistema declarado"
  - "cada transición tiene grabación, duración y curva"
  - "los estados están especificados con datos reales, no con contenido de ejemplo"
  - "existe estado reducido para cada movimiento"
rechaza_si:
  - "hay un valor sin correspondencia en el sistema y sin excepción declarada"
  - "falta el estado reducido de algún movimiento"
  - "la adaptación no cubre algún entorno de la matriz del pack"
devolucion: >
  CON devuelve a DIS cuando demuestra imposibilidad con la evidencia que exige 05-FIDELIDAD:
  medición contra presupuesto, limitación documentada con enlace y versión, prototipo que
  lo intenta y falla con grabación, o coste medido que excede lo autorizado. CON NO decide
  qué se sacrifica.
evidencia_de_devolucion:
  - "una de las cuatro formas de evidencia de imposibilidad de 05-FIDELIDAD"
owner: "ninguna, salvo aceptación de deuda sobre superficie premium o patrón suyo."
checkpoint: "CON lee de DIS: qué se descartó y por qué, para no reintroducirlo como simplificación."
```

```yaml ads:handoff
id: handoff:con-a-dis
de: CON
a: DIS
cuando: "CON ha construido una capa que implementa una especificación de DIS"
entrega:
  - "el artefacto construido con su commit exacto"
  - "el entorno donde se puede ejecutar y cómo"
  - "las diferencias conocidas respecto a la especificación, si las hay, con su motivo"
comprueba_al_recibir:
  - "el artefacto es ejecutable en los entornos de la matriz del pack"
  - "el commit está identificado y corresponde a la especificación versionada"
  - "las diferencias conocidas están declaradas ANTES de la comparación, no después"
rechaza_si:
  - "el artefacto no es ejecutable y no se puede comparar"
  - "no se sabe qué versión de la especificación se implementó"
devolucion: >
  DIS/revision-de-fidelidad devuelve con veredicto infiel, adjuntando la comparación
  completa. Una diferencia descubierta en la comparación NO se acepta como deuda a
  posteriori.
evidencia_de_devolucion:
  - "el artefacto de comparación de 05-FIDELIDAD, con estático, estados, movimiento y valores"
owner: "acepta la deuda cuando la superficie es premium o el patrón es suyo."
checkpoint: "DIS lee de CON: qué diferencias declaró antes de construir, para distinguirlas de las descubiertas."
```

```yaml ads:handoff
id: handoff:dis-a-ver
de: DIS
a: VER
cuando: "la ESTACIÓN 11 del ciclo de calidad —REVISIÓN DE FIDELIDAD— queda dictaminada: es la SEGUNDA pasada del gate visual, y el gate de diseño NO cierra hasta ella (02-RUBRICAS, «Las dos pasadas del gate visual»). Antes de esa estación el eje fidelidad está `pendiente-de-construccion` y los nueve ejes no tienen nivel"
entrega:
  - "el dictamen de excelencia visual con sus nueve ejes, y de qué PASADA procede cada uno: los ocho de la PASADA DE DISEÑO —estación 9, antes de entregar a Construcción— y el eje fidelidad de la PASADA DE FIDELIDAD —estación 11, con la capa ya construida—"
  - "el dictamen de usabilidad con sus seis ejes, procedente de la estación 8, VALIDACIÓN DE USO"
  - "las capturas de referencia para la regresión visual"
  - "los patrones que este item aprobó, con su clase y su alcance"
comprueba_al_recibir:
  - "ambos dictámenes existen y ningún eje está en rechazo"
  - "cada dictamen nombra la estación del ciclo de la que procede, y el eje fidelidad procede de la estación 11 y no de la 9"
  - "las capturas de referencia cubren los entornos de la matriz del pack"
  - "el agente que dictaminó no ocupó ningún rol productor"
rechaza_si:
  - "falta uno de los dos dictámenes"
  - "el dictamen visual llega con el eje fidelidad todavía `pendiente-de-construccion`: procede de la primera pasada y el gate no ha cerrado"
  - "el dictamen lo emitió un agente que produjo el artefacto"
  - "no hay capturas de referencia y la regresión visual sería imposible"
devolucion: >
  VER devuelve a DIS cuando la regresión visual detecta que el cambio rompe una superficie
  que no estaba en el alcance del item.
evidencia_de_devolucion:
  - "la comparación de la superficie afectada, antes y después"
owner: "ninguna: en este handoff no hay materia de decisión del Owner."
checkpoint: "VER lee de DIS: qué superficies toca el cambio, para acotar la regresión visual."
```

```yaml ads:handoff
id: handoff:uso-a-dis
de: USO
a: DIS
cuando: "el uso real produce evidencia que contradice una decisión de forma"
entrega:
  - "la evidencia: grabación, telemetría, observación o reacción registrada"
  - "qué decisión de forma contradice, enlazada"
  - "en qué condiciones ocurrió: dispositivo, datos, momento"
comprueba_al_recibir:
  - "la evidencia registra comportamiento, no opinión sobre el comportamiento"
  - "la decisión contradicha está identificada y vigente"
  - "las condiciones permiten reproducir la situación"
rechaza_si:
  - "la evidencia es una preferencia sin comportamiento observado detrás"
  - "no se identifica qué decisión concreta queda contradicha"
devolucion: >
  DIS devuelve a USO cuando la evidencia no permite distinguir un fallo de forma de un
  fallo de construcción, pidiendo la observación concreta que lo separaría.
evidencia_de_devolucion:
  - "qué observación adicional distinguiría ambos casos"
owner: "el Owner decide si la contradicción cambia la dirección: eso es un item DIR."
checkpoint: "DIS lee de USO: qué se observó y con qué datos, para reproducirlo en la exploración."
```

```yaml ads:handoff
id: handoff:inv-a-dis
de: INV
a: DIS
cuando: "una investigación produce evidencia que condiciona una decisión de forma"
entrega:
  - "la respuesta a la pregunta acotada, con su frescura declarada"
  - "las fuentes con enlace y fecha"
  - "qué queda fuera del alcance de la investigación"
comprueba_al_recibir:
  - "la respuesta contesta la pregunta cerrada que se hizo, no una parecida"
  - "las fuentes son comprobables"
  - "la frescura está declarada"
rechaza_si:
  - "la respuesta es una opinión general en lugar de la contestación a la pregunta"
  - "las fuentes no son comprobables"
devolucion: >
  DIS devuelve a INV reformulando la pregunta cerrada que necesita, cuando la respuesta no
  permite decidir entre las alternativas que tiene sobre la mesa.
evidencia_de_devolucion:
  - "las alternativas concretas entre las que hay que decidir"
owner: "ninguna: en este handoff no hay materia de decisión del Owner."
checkpoint: "DIS lee de INV: la frescura, para saber si tendrá que revalidar antes de usarla."
```

```yaml ads:handoff
id: handoff:dis-a-ent
de: DIS
a: ENT
cuando: "el item llega a entrega y la superficie debe observarse en el entorno real"
entrega:
  - "qué superficies cambian y qué hay que mirar en cada una"
  - "las capturas de referencia para comparar tras el despliegue"
  - "qué señalaría que el cambio de forma ha empeorado algo medible"
comprueba_al_recibir:
  - "existe una señal observable, no sólo una superficie que mirar"
  - "las capturas de referencia corresponden a lo aprobado"
rechaza_si:
  - "no hay ninguna señal declarada que se pueda observar tras el despliegue"
devolucion: >
  ENT devuelve a DIS cuando la observación tras el despliegue muestra que la superficie se
  comporta distinto en el entorno real que en el de desarrollo.
evidencia_de_devolucion:
  - "la comparación entre lo observado en el entorno real y las capturas de referencia"
owner: "la publicación es materia reservada del Owner (G05), no de este handoff."
checkpoint: "ENT lee de DIS: qué mirar y qué contaría como empeoramiento."
```

## Reglas comunes a todos los handoffs de DIS

```text
1  DIS NUNCA entrega una especificación que exija decidir forma para poder ejecutarla.
   Si el receptor tiene que decidir algo de forma, la capa de DIS está incompleta.

2  NADIE devuelve a DIS sólo con la negativa. ARQ y CON devuelven con evidencia y, ARQ
   además, con al menos una alternativa de forma.

3  UNA DIFERENCIA DESCUBIERTA NO SE CONVIERTE EN DEUDA. La deuda se acuerda antes de
   construir distinto. Ésta es la regla que sostiene todo el sistema de fidelidad.

4  EL RECHAZO AL RECIBIR no cuenta como devolución a efectos del freno de a.7, porque la
   capa nunca se depositó. La devolución posterior sí cuenta.
```
