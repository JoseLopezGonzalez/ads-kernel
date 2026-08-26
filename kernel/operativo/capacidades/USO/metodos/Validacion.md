# USO/Validacion — evidencia de que funciona de verdad

```yaml ads:metodo
id: USO/Validacion
nombre: Validacion
capacidad: USO
disparador:
  - "un item cumple C-USO y su cambio está entregado"
  - "telemetría o logs contradicen lo esperado"
carga:
  - "los criterios de éxito de PRD y el dosier de VER"
  - "docs/uso/COLA-DE-VALIDACION.md"
  - "el acceso a la fuente de uso real elegida"
preguntas_iniciales:
  - "¿cuál de las siete fuentes es aplicable aquí, y qué evidencia produce?"
  - "¿qué criterio concreto estoy validando?"
  - "¿hay más validaciones pendientes que agrupar en el mismo lote?"
pasos:
  - n: 1
    nombre: ELEGIR FUENTE
    modo: convergente
    hace: >
      Elegir entre Owner, usuario real, operador, dispositivo, telemetría, logs o plan de
      validación humana, y declarar por qué esa y no otra.
    produce: "fuente declarada con su motivo"
    termina_cuando: "la fuente está elegida y es capaz de producir evidencia del criterio"
    checkpoint: true
  - n: 2
    nombre: AGRUPAR EN LOTE
    modo: lineal
    hace: >
      Si la fuente es humana, buscar qué otras validaciones están pendientes y agruparlas,
      ordenadas por coste de preparación. Preparar el estado de antemano.
    produce: "lote de validación con su orden y su estado preparado"
    termina_cuando: "el lote está ordenado y el estado listo para empezar sin montarlo delante"
    checkpoint: true
  - n: 3
    nombre: OBSERVAR
    modo: lineal
    hace: >
      Registrar lo que OCURRE: dónde duda, dónde vuelve atrás, qué toca primero, qué
      abandona. Si la fuente es telemetría, extraer el comportamiento, no la media.
    produce: "registro de observación con condiciones"
    termina_cuando: "cada criterio del lote tiene observación, o consta por qué no la tiene"
    checkpoint: true
  - n: 4
    nombre: SEPARAR HALLAZGOS
    modo: convergente
    hace: >
      Distinguir lo que valida el criterio de lo que el uso reveló y nadie había previsto.
      Lo segundo son candidatos a item y se entregan a ENC o a APR.
    produce: "evidencia del criterio, y lista de hallazgos no previstos"
    termina_cuando: "ambos están escritos por separado"
    checkpoint: true
  - n: 5
    nombre: CERRAR
    modo: convergente
    hace: "Recorrer gate:uso-comprobado y declarar lo que no se pudo validar."
    produce: "capa de uso real depositada"
    termina_cuando: "las cinco comprobaciones están anotadas"
    checkpoint: true
artefactos:
  - "fuente declarada"
  - "lote de validación con su orden"
  - "registro de observación"
  - "hallazgos no previstos"
puntos_owner:
  - "paso 3, cuando él es la fuente: por lotes, con el estado preparado, nunca item por item"
consultas:
  - "PLT: ¿hay dispositivo real disponible? Responde sí o no, y en qué estado"
  - "DIS: ¿esta observación contradice un patrón vigente? Responde con el patrón"
checkpoints:
  - "tras los pasos 1, 2, 3, 4 y 5"
critica:
  - "¿estoy registrando comportamiento o estoy registrando opiniones?"
  - "¿he convocado al Owner por este item solo, pudiendo agrupar?"
  - "¿estoy descartando un hallazgo por no encajar en el alcance?"
gate: gate:uso-comprobado
salida:
  - "evidencia de uso real depositada"
  - "candidatos a item entregados a ENC o APR"
devolucion:
  - "a la capacidad propietaria de la capa que el uso muestra insuficiente"
bloqueo:
  - "no hay ninguna fuente aplicable disponible"
cancelacion:
  - "el cambio se revierte antes de validarlo: la observación parcial se conserva"
aprendizaje:
  - "todo hallazgo no previsto entra en OBSERVACIONES.md y alimenta a APR"
  - "una expectativa que el uso contradice es aprendizaje de producto, no un defecto"
prueba_de_reanudacion: >
  Un agente nuevo lee qué criterios del lote están ya observados y continúa por los que
  faltan, sin volver a convocar al Owner por lo ya hecho. Es la prueba T112.
```
