# DIS/ValidacionDeUso — comprobar con personas y datos reales

```yaml ads:metodo
id: DIS/ValidacionDeUso
nombre: ValidacionDeUso
capacidad: DIS
disparador:
  - "existe prototipo ejecutable o construcción que cierra gate:usabilidad"
  - "un item DEU de rendimiento o accesibilidad activa USO por C-USO"
carga:
  - "el prototipo o la construcción, ejecutable"
  - "el perfil de uso y las tareas principales"
  - "los datos reales con sus casos extremos"
  - "los presupuestos, la matriz de entornos y los criterios de accesibilidad del pack"
preguntas_iniciales:
  - "¿qué tarea concreta se valida, y cuál es su criterio de éxito?"
  - "¿qué fuente de uso real hay disponible: persona, dispositivo, telemetría o plan por lotes?"
pasos:
  - n: 1
    nombre: PLAN
    modo: lineal
    hace: >
      Escribir la tarea, el criterio de éxito y qué se observa, ANTES de convocar a nadie.
      Si hay varias validaciones pendientes, se agrupan en un solo lote ordenado por coste
      de preparación (G36).
    produce: "plan de validación"
    termina_cuando: "cada tarea tiene criterio de éxito comprobable y el estado de partida está preparado"
    checkpoint: true
  - n: 2
    nombre: RECORRIDO POR MEDIO DE ENTRADA
    modo: lineal
    hace: >
      Completar las tareas principales con cada medio de entrada que el pack declara, y
      registrar dónde falla o dónde no hay camino.
    produce: "recorridos registrados por medio"
    termina_cuando: "cada medio declarado tiene su recorrido registrado"
    checkpoint: true
  - n: 3
    nombre: ESTADOS Y EXTREMOS
    modo: lineal
    hace: >
      Provocar los cinco estados con datos reales, incluidos el listado vacío, el nombre
      más largo y el máximo, y registrar el comportamiento.
    produce: "evidencia de los cinco estados"
    termina_cuando: "los cinco están provocados y capturados, o está declarado cuál no se pudo provocar y por qué"
    checkpoint: true
  - n: 4
    nombre: MEDIR RESPUESTA
    modo: lineal
    hace: >
      Medir el tiempo entre la acción y la primera respuesta visible, y compararlo con el
      presupuesto declarado por el pack.
    produce: "mediciones frente a presupuesto"
    termina_cuando: "cada acción principal tiene su medición"
    checkpoint: false
  - n: 5
    nombre: ACCESIBILIDAD
    modo: lineal
    hace: >
      Ejecutar la comprobación automática del pack y el recorrido manual que el pack
      declare, incluidos texto ampliado, contraste aumentado y movimiento reducido.
    produce: "salida de accesibilidad"
    termina_cuando: "los criterios exigibles del pack están comprobados con su método declarado"
    checkpoint: true
  - n: 6
    nombre: OBSERVAR
    modo: conversacional
    hace: >
      Cuando hay persona, darle la tarea sin explicarle cómo se hace, y registrar lo que
      HACE. Su comentario se cita, pero la evidencia es su comportamiento.
    produce: "grabación u observación registrada"
    termina_cuando: "la tarea se completó, se abandonó o se agotó el tiempo declarado en el plan"
    checkpoint: true
  - n: 7
    nombre: DICTAMINAR
    modo: convergente
    hace: >
      Evaluar los seis ejes de rubrica:usabilidad. Lo que no pudo comprobarse SE DICE en
      el dictamen, no se omite.
    produce: "dictamen de usabilidad"
    termina_cuando: "los seis ejes tienen nivel y evidencia, o constancia de por qué no se pudo evaluar"
    checkpoint: true
artefactos:
  - "plan de validación"
  - "recorridos por medio de entrada"
  - "evidencia de los cinco estados"
  - "mediciones de respuesta"
  - "salida de accesibilidad"
  - "grabación u observación"
  - "dictamen de usabilidad"
puntos_owner:
  - "paso 6, cuando el Owner es la fuente de uso real: se le convoca POR LOTES, no por item"
consultas:
  - "USO: ¿existe telemetría o usuario real distinto del Owner para esta superficie?"
  - "PLT: ¿hay dispositivo real disponible y en qué estado?"
checkpoints:
  - "tras los pasos 1, 2, 3, 5, 6 y 7"
critica:
  - "¿he validado recorriendo yo mismo una interfaz que ya conozco?"
  - "¿estoy declarando excelente un eje que exige observación sin haber observado?"
  - "¿he omitido del dictamen lo que no pude comprobar?"
gate: gate:usabilidad
salida:
  - "dictamen de usabilidad con los seis ejes"
  - "toda la evidencia enlazada"
devolucion:
  - "a DIS/diseno-interaccion, cuando el eje en rechazo es de flujo"
  - "a CON, cuando el fallo está en la construcción y no en la especificación"
bloqueo:
  - "no hay fuente de uso real aplicable y la superficie es premium"
  - "no hay dispositivo real y el pack lo exige"
cancelacion:
  - "la superficie se retira del alcance antes de validarla"
aprendizaje:
  - "toda tarea que se abandona señala un flujo mal diseñado, y se registra"
  - "un presupuesto de respuesta incumplido de forma sistemática se promueve a item DEU"
prueba_de_reanudacion: >
  Un agente nuevo lee el plan y qué tareas y qué estados están ya validados, y continúa sin
  repetirlos ni volver a convocar al Owner por lo ya observado. Es la prueba T98.
```
