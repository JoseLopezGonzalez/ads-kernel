# VER/Dosier — reunir evidencia juzgable

```yaml ads:metodo
id: VER/Dosier
nombre: Dosier
capacidad: VER
disparador:
  - "una capa de CON queda depositada"
carga:
  - "los criterios de éxito de PRD y la definición de fracaso"
  - "la capa de CON con su commit y sus diferencias declaradas"
  - "los dictámenes de DIS cuando hay superficie"
  - "docs/verificacion/REGRESIONES.md y los presupuestos del pack"
preguntas_iniciales:
  - "¿qué criterio de éxito voy a poder comprobar y cuál no, y por qué?"
  - "¿qué se rompió alguna vez en esta zona, según el historial de regresiones?"
  - "¿qué evidencia de ésta podría juzgar el Owner por sí mismo?"
pasos:
  - n: 1
    nombre: CRITERIO POR CRITERIO
    modo: lineal
    hace: >
      Recorrer los criterios de éxito uno a uno, comprobando cada uno y enlazando su
      evidencia. Sin agregar: diez criterios producen diez veredictos.
    produce: "veredicto por criterio con evidencia"
    termina_cuando: "todos los criterios tienen veredicto, incluido «no comprobable» con su motivo"
    checkpoint: true
  - n: 2
    nombre: REGRESIÓN
    modo: lineal
    hace: >
      Ejecutar la suite de regresión y, cuando hay superficie, la regresión visual contra
      las capturas de referencia de DIS.
    produce: "salida de regresión y comparación de capturas"
    termina_cuando: "la regresión está ejecutada y toda diferencia está explicada o devuelta"
    checkpoint: true
  - n: 3
    nombre: ESTADOS EXTREMOS
    modo: lineal
    hace: "Provocar y capturar vacío, error, carga, mínimo y máximo con datos reales."
    produce: "capturas de los cinco estados"
    termina_cuando: "los cinco están capturados, o está dicho cuál no se pudo provocar y por qué"
    checkpoint: true
  - n: 4
    nombre: PRESUPUESTOS
    modo: lineal
    hace: "Medir lo que el pack instalado declara como presupuesto y compararlo."
    produce: "mediciones frente a presupuestos"
    termina_cuando: "cada presupuesto declarado tiene su medición"
    checkpoint: false
  - n: 5
    nombre: ESCRIBIR EL DOSIER
    modo: convergente
    hace: >
      Componer el dosier con los veredictos, la evidencia y —obligatorio— la sección de lo
      NO comprobado.
    produce: "dosier"
    termina_cuando: "gate:evidencia-suficiente recorrido y anotado"
    checkpoint: true
artefactos:
  - "veredictos por criterio"
  - "salida de regresión y comparación visual"
  - "capturas de estados extremos"
  - "mediciones de presupuestos"
  - "dosier"
puntos_owner:
  - "cola de validación por lotes cuando un criterio exige su juicio (G36)"
consultas:
  - "DIS: ¿esta diferencia visual es una regresión o es la intención aprobada? Responde con el patrón que aplica"
  - "SEG: ¿este cambio exige comprobación de seguridad? Responde sí o no, y cuál"
checkpoints:
  - "tras los pasos 1, 2, 3 y 5"
critica:
  - "¿he agregado criterios en un veredicto global?"
  - "¿mi evidencia la puede juzgar una persona, o sólo dice «los tests pasan»?"
  - "¿he omitido lo que no pude comprobar?"
gate: gate:evidencia-suficiente
salida:
  - "dosier emitido, que viaja hacia adelante"
devolucion:
  - "a CON, a DIS o a PRD según de quién sea la capa que falla, con la evidencia"
bloqueo:
  - "no hay entorno donde ejecutar la regresión"
  - "no hay datos representativos para los estados extremos"
cancelacion:
  - "el paquete se cancela: el dosier parcial se conserva como evidencia histórica"
aprendizaje:
  - "toda regresión detectada genera una prueba que la vigile, y entra en REGRESIONES.md"
  - "un criterio que no se pudo verificar señala una forma de escribir criterios que hay que corregir en PRD"
prueba_de_reanudacion: >
  Un agente nuevo lee qué criterios están ya verificados con su evidencia y continúa por los
  que faltan, sin repetir mediciones. Es la prueba T108.
```
