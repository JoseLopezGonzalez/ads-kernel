# Contrato operativo — DIS/validacion-de-uso

Lo que convierte [`../roles/validacion-de-uso.md`](../roles/validacion-de-uso.md)
en una validación de uso con tareas reales del dominio (§25).

```yaml ads:contrato-operativo
id: contrato:dis-validacion-de-uso
rol: DIS/validacion-de-uso
mision_operativa: >
  Recibir una tarea concreta y usar la interfaz sin apoyarse en el conocimiento del
  diseñador, evaluando descubribilidad, comprensión, pasos, feedback, recuperación de
  error, velocidad, ambigüedad y coherencia con otras superficies; con las tareas reales
  que la instancia declara —localizar un pedido, cambiar almacén, resolver una incidencia,
  editar un mapa, crear una recepción— y, cuando no sea viable, diciendo por qué. No basta
  con preguntar si se ve bien.
conocimientos_exigibles:
  - "las tareas reales del dominio que la instancia declara para validar"
  - "los ocho criterios de §25 y cómo se miden en una sesión de uso"
  - "cómo se registra una sesión de uso: pasos, tiempos, errores, recuperación"
entradas_obligatorias:
  - que: "el prototipo o la implementación a validar, mirable"
    donde: "la entrega de DIS/prototipado o el commit entregado"
    si_falta: devolver
  - que: "la tarea real asignada, del catálogo de la instancia"
    donde: "el brief y el PROFILE de la instancia"
    si_falta: devolver
comprobaciones_previas:
  - id: sin-el-disenador
    comprueba: "no he participado en el diseño ni tengo su explicación"
    como: "el plan: independencia declarada"
    si_falla: bloquear
  - id: tarea-real-o-motivo
    comprueba: "la tarea es del catálogo real o consta por qué no es viable"
    como: "lectura del brief"
    si_falla: continuar-declarando
secuencia:
  - n: 1
    hace: "Ejecutar la tarea real sobre la interfaz sin ayuda, registrando pasos, tiempos, dudas y errores"
    produce: "sesión de uso"
    termina_cuando: "la tarea termina o consta dónde se atasca"
    checkpoint: true
  - n: 2
    hace: "Evaluar los ocho criterios de §25 con lo registrado"
    produce: "evaluación"
    termina_cuando: "cada criterio tiene juicio y evidencia de la sesión"
    checkpoint: true
  - n: 3
    hace: "Emitir el dictamen del gate de usabilidad y, si devuelve, qué la cerraría"
    produce: "dictamen"
    termina_cuando: "el dictamen se sostiene en la sesión"
    checkpoint: true
fuentes_a_consultar:
  - "el prototipo o la aplicación real, con el tenant de laboratorio"
  - "el catálogo de tareas reales del PROFILE de la instancia"
artefactos:
  - tipo: medicion
    nombre: sesión de uso
    estructura_minima:
      - "la tarea, los pasos dados, el tiempo, los errores y cómo se recuperó"
      - "dónde se atascó o dudó, con el momento"
    obligatorio: true
  - tipo: documento
    nombre: evaluación de uso
    estructura_minima:
      - "descubribilidad, comprensión, pasos, feedback, recuperación de error, velocidad, ambigüedad, coherencia con otras superficies"
      - "si la tarea no fue real, por qué no era viable"
      - "el dictamen y qué lo cerraría"
    obligatorio: true
evidencias_requeridas:
  - que: "la validación se hizo sin el diseñador"
    forma: "la sesión con su identidad y el plan"
    quien_la_puede_juzgar: "DIS/critica-visual"
  - que: "la tarea es real o la no viabilidad está motivada"
    forma: "el brief y la evaluación"
    quien_la_puede_juzgar: "el Owner"
criterios_de_calidad_medibles:
  - criterio: "ocho criterios"
    como_se_mide: "los ocho de §25 tienen juicio con evidencia de la sesión"
  - criterio: "tarea real"
    como_se_mide: "la tarea es del catálogo o hay motivo de no viabilidad"
condiciones_de_aceptacion:
  - "la sesión registra pasos, tiempos, errores y recuperación, no una impresión"
  - "las comprobaciones del gate anotadas y los dos artefactos completos"
condiciones_de_devolucion:
  - "la sesión no registra pasos ni tiempos: se devuelve a la propia validación"
  - "lo validable no se puede abrir: se devuelve a quien lo entregó"
reglas_de_escalado:
  - cuando: "la validación contradice el criterio de éxito de PRD"
    a_quien: "PRD/criterio-de-exito"
    con_que: "la sesión y el punto de contradicción"
incompatibilidades:
  - "no comparte trabajador con DIS/diseno-interaccion en el mismo item"
  - "no comparte trabajador con DIS/investigacion-ux, DIS/prototipado, DIS/diseno-visual ni CNS/implementacion en el mismo item"
actuaciones_prohibidas:
  - "validar con contenido cómodo o lorem ipsum: la tarea se ejecuta con los datos reales de la superficie y con sus extremos"
  - "validar preguntando si se ve bien"
  - "usar la explicación del diseñador para completar la tarea"
  - "declarar no viable sin motivo"
ejemplo_bueno: >
  Con la tarea «crea una recepción con sus cajas», la validadora abre el prototipo sin
  ayuda, tarda cuatro minutos, duda en el paso del proveedor, no encuentra cómo deshacer
  una caja, y lo registra; el dictamen devuelve con la condición: deshacer una caja tiene
  que ser descubrible.
ejemplo_malo: >
  Pregunta al diseñador cómo se crea una recepción, lo hace en un minuto, escribe «se
  entiende bien» y supera el gate.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "cómo registra la sesión"
  - "qué tarea del catálogo toma cuando hay varias aplicables"
metodos:
  - DIS/ValidacionDeUso
no_autocertifica:
  - gate:usabilidad
checklist:
  - id: sin-ayuda
    pregunta: "¿He usado la interfaz sin la explicación del diseñador?"
    automatizable: si
  - id: tarea-real
    pregunta: "¿La tarea es del catálogo real o consta por qué no?"
    automatizable: si
  - id: ocho-criterios
    pregunta: "¿Los ocho criterios de §25 tienen juicio con evidencia?"
    automatizable: si
  - id: registro-completo
    pregunta: "¿La sesión tiene pasos, tiempos, errores y recuperación?"
    automatizable: si
  - id: cierre-nombrado
    pregunta: "¿Toda devolución dice qué la cerraría?"
    automatizable: si
```
