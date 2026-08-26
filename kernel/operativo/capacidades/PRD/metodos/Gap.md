# PRD/Gap — el procedimiento estándar de gaps

Un GAP no es una feature pequeña. Es **la distancia entre lo que se pretendía y lo que
hay**, y su pregunta más valiosa —por qué apareció el hueco— se pierde si se encuadra como
feature.

```yaml ads:metodo
id: PRD/Gap
nombre: Gap
capacidad: PRD
disparador:
  - "DSP despacha un paquete de PRD sobre un item de tipo GAP"
carga:
  - "el encuadre y su dosier de anclaje sobre LO YA IMPLEMENTADO"
  - "el item que construyó lo que ahora se queda corto, y su traza de ruta"
  - "docs/producto/ALCANCE.md y los criterios de éxito de aquel item"
preguntas_iniciales:
  - "¿qué se pretendía cuando se construyó esto, y qué se consiguió?"
  - "¿el hueco fue una decisión consciente o un accidente?"
  - "¿la expectativa estaba escrita, o apareció después?"
pasos:
  - n: 1
    nombre: MEDIR LA DISTANCIA
    modo: convergente
    hace: >
      Escribir qué se pretendía y qué hay, uno al lado del otro, con la evidencia de ambos.
      La distancia es el objeto del item.
    produce: "la distancia escrita, con evidencia de lo pretendido y de lo real"
    termina_cuando: "ambas columnas están escritas y la diferencia es identificable sin interpretar"
    checkpoint: true
  - n: 2
    nombre: DETERMINAR EL ORIGEN
    modo: convergente
    hace: >
      Averiguar si el hueco fue decisión consciente —y entonces está en el fuera de alcance
      de aquel item— o accidente. Se consulta la capacidad propietaria de la capa que se
      quedó corta.
    produce: "origen del hueco: decisión declarada, decisión no escrita, o accidente"
    termina_cuando: "el origen está clasificado con la evidencia que lo sostiene"
    checkpoint: true
  - n: 3
    nombre: DECIDIR SI LA EXPECTATIVA CAMBIA EL ALCANCE
    modo: convergente
    hace: >
      Si la expectativa estaba escrita, cerrar el hueco es reconciliar. Si es nueva, AMPLÍA
      el alcance del producto y eso es materia del Owner.
    produce: "veredicto: reconciliación o ampliación, con su motivo"
    termina_cuando: "el veredicto está escrito y, si es ampliación, escalado al Owner"
    checkpoint: true
  - n: 4
    nombre: DEFINIR EL CIERRE
    modo: convergente
    hace: >
      Escribir qué evidencia demostrará que la distancia ha desaparecido. No es «que
      funcione»: es la medición o la observación concreta.
    produce: "criterio de cierre del gap"
    termina_cuando: "el criterio mide la distancia, no la existencia de la funcionalidad"
    checkpoint: true
  - n: 5
    nombre: REGISTRAR EL APRENDIZAJE DEL HUECO
    modo: lineal
    hace: >
      Escribir POR QUÉ apareció el hueco. Es la fuente más valiosa del sistema y se pierde
      si el item se cierra sin ella.
    produce: "learning_candidate con enlace, o none con motivo"
    termina_cuando: "el campo está resuelto, no vacío"
    checkpoint: true
artefactos:
  - "la distancia con evidencia de ambas columnas"
  - "el origen clasificado del hueco"
  - "veredicto reconciliación o ampliación"
  - "criterio de cierre"
  - "learning_candidate resuelto"
puntos_owner:
  - "paso 3, cuando la expectativa es nueva y amplía el alcance del producto"
consultas:
  - "la capacidad propietaria de la capa que se quedó corta: ¿fue decisión o accidente? Responde con el enlace a la decisión, o con «no consta»"
  - "USO: ¿cómo se detectó el hueco: por telemetría, por el Owner, por un usuario?"
checkpoints:
  - "tras cada paso"
critica:
  - "¿estoy tratando esto como una feature y perdiendo la pregunta de por qué apareció?"
  - "¿la expectativa estaba escrita, o la estoy dando por evidente ahora?"
  - "¿el criterio de cierre mide la distancia o sólo la existencia de algo nuevo?"
gate: gate:intencion-definida
salida:
  - "capa de intención del gap, con su distancia, su criterio de cierre y su aprendizaje"
devolucion:
  - "a ENC, cuando el anclaje no determinó qué existe realmente y la distancia no es medible"
bloqueo:
  - "no se puede establecer qué se pretendía porque aquel item no dejó criterio de éxito"
cancelacion:
  - "la distancia desapareció por otro trabajo: se cancela con enlace al item que la cerró"
aprendizaje:
  - "todo gap registra por qué apareció; es obligatorio y es lo que distingue GAP de FEA"
  - "tres gaps con el mismo origen señalan un defecto de método, no de item"
prueba_de_reanudacion: >
  Un agente nuevo abre el paquete y ve la distancia ya medida y el origen ya clasificado, y
  continúa sin repetir el análisis. Es la prueba T101.
```
