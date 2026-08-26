# DOM/Migracion — cambiar datos sin perderlos

```yaml ads:metodo
id: DOM/Migracion
nombre: Migracion
capacidad: DOM
disparador:
  - "un item cambia el esquema o el contenido de los datos"
carga:
  - "las condiciones de DOM/modelo"
  - "una copia de datos con volumen y casos reales"
  - "docs/dominio/MIGRACIONES.md"
preguntas_iniciales:
  - "¿este cambio es compatible hacia atrás?"
  - "¿qué filas quedan fuera del criterio de la migración, y qué se hace con ellas?"
  - "¿cuánto dura la ventana de incompatibilidad?"
pasos:
  - n: 1
    nombre: ESCRIBIR IDA Y VUELTA
    modo: lineal
    hace: "Escribir la migración y su reversión como dos artefactos separados."
    produce: "migración y reversión"
    termina_cuando: "ambos existen y la reversión no depende de datos que la migración destruye"
    checkpoint: true
  - n: 2
    nombre: PROBAR SOBRE COPIA REAL
    modo: lineal
    hace: >
      Ejecutar sobre una copia con volumen y casos reales, registrando recuento antes y
      después y qué filas quedaron fuera del criterio.
    produce: "salida de la ejecución con recuentos"
    termina_cuando: "la migración termina y los recuentos cuadran con lo esperado, o la diferencia está explicada"
    checkpoint: true
  - n: 3
    nombre: PROBAR LA VUELTA
    modo: lineal
    hace: >
      Ejecutar la reversión sobre el resultado y comprobar que los datos vuelven a su estado
      anterior. Una reversión no ejecutada no es reversible.
    produce: "salida de la reversión con su comprobación"
    termina_cuando: "los datos coinciden con el estado previo, o la diferencia está declarada y aceptada"
    checkpoint: true
  - n: 4
    nombre: DECLARAR LA VENTANA
    modo: convergente
    hace: >
      Escribir cuánto tiempo el sistema estará en estado incompatible y cómo se cubre: paso
      intermedio, doble escritura o parada declarada.
    produce: "ventana de incompatibilidad y su cobertura"
    termina_cuando: "la ventana está escrita y ENT sabe qué hacer durante ella"
    checkpoint: true
  - n: 5
    nombre: REGISTRAR
    modo: lineal
    hace: "Escribir en el historial el resultado REAL, incluidos los problemas encontrados."
    produce: "entrada en MIGRACIONES.md"
    termina_cuando: "la entrada refleja lo que pasó, no lo que se esperaba"
    checkpoint: false
artefactos:
  - "migración y reversión"
  - "salidas de ejecución con recuentos"
  - "ventana de incompatibilidad"
  - "entrada de historial"
puntos_owner:
  - "cuando la migración no es reversible y hay que decidir asumir la pérdida"
consultas:
  - "ENT: ¿qué ventana de indisponibilidad es admisible en este entorno? Responde con el tiempo y la franja"
  - "PLT: ¿hay copia con volumen real disponible para probar? Responde sí o no, y dónde"
checkpoints:
  - "tras cada ejecución, con su salida"
critica:
  - "¿he ejecutado la reversión o sólo la he escrito?"
  - "¿mi copia de prueba tiene el volumen y los casos raros de producción?"
  - "¿qué pasa con las filas que no cumplen el criterio: las he mirado?"
gate: gate:dominio-conforme
salida:
  - "migración probada, reversión probada, ventana declarada"
devolucion:
  - "a ARQ, cuando la ventana exige otro orden de paquetes"
bloqueo:
  - "no hay copia representativa sobre la que probar"
cancelacion:
  - "el cambio de modelo se retira: la migración se conserva sin ejecutar, con su motivo"
aprendizaje:
  - "toda migración que falló en la prueba entra en el historial con qué la hizo fallar"
  - "una ventana que resultó mayor de la declarada es aprendizaje promovible"
prueba_de_reanudacion: >
  Un agente nuevo lee qué pasos de la migración se ejecutaron y con qué resultado, y
  continúa sin repetir ejecuciones. Es la prueba T105.
```
