# CNS/RevisionDeConstruccion — leer entero, revertir para medir, citar la línea

```yaml ads:metodo
id: CNS/RevisionDeConstruccion
nombre: RevisionDeConstruccion
capacidad: CNS
disparador:
  - "CNS/implementacion deposita su capa y el paquete de revisión de construcción se despacha"
carga:
  - "la entrega de CNS/implementacion: commit, diferencias declaradas y autoevaluación del gate"
  - "las capas de PRD, DIS y ARQ cuando existen, con sus versiones"
  - "las convenciones vigentes de la fuente tocada"
preguntas_iniciales:
  - "¿el commit entregado existe y es el que la entrega nombra, o hay otro más nuevo sin declarar?"
  - "¿qué ficheros toca el diff y cuáles de ellos no están en el alcance declarado?"
  - "¿qué pruebas nuevas hay, y qué cambio dice proteger cada una?"
pasos:
  - n: 1
    nombre: ACUSAR O RECHAZAR
    modo: lineal
    hace: >
      Recorrer las comprobaciones al recibir del handoff: commit localizable, autoevaluación
      completa, diferencias fechadas antes de la entrega. Si una falla, rechazar SIN tomar
      custodia; si pasan, acusar.
    produce: "acuse o rechazo del handoff, con las comprobaciones anotadas"
    termina_cuando: "el handoff está acusado o rechazado, y ninguna comprobación quedó sin anotar"
    checkpoint: true
  - n: 2
    nombre: RECORRER EL DIFF
    modo: lineal
    hace: >
      Leer el diff completo, fichero a fichero, anotando por cada uno: qué cambia, si está
      dentro del alcance y si cumple las convenciones de la fuente. Todo fichero tocado
      recibe veredicto; ninguno se salta por parecer trivial.
    produce: "lista de ficheros tocados con veredicto y observaciones"
    termina_cuando: "cada fichero del diff tiene su veredicto escrito"
    checkpoint: true
  - n: 3
    nombre: MEDIR SI LAS PRUEBAS MUERDEN
    modo: lineal
    hace: >
      Por cada prueba nueva, revertir en una copia el cambio que dice proteger y ejecutarla.
      Una prueba que sigue verde con el cambio revertido no protege nada, y es hallazgo
      bloqueante.
    produce: "tabla prueba → cambio revertido → resultado"
    termina_cuando: "cada prueba nueva tiene su resultado de reversión anotado"
    checkpoint: true
  - n: 4
    nombre: CONTRASTAR CON LAS CAPAS ANTERIORES
    modo: lineal
    hace: >
      Comparar lo construido con las capas de PRD, DIS y ARQ: toda decisión de esas capas
      que el diff cambia sin haberla devuelto es hallazgo bloqueante que se devuelve a la
      capacidad propietaria, no a CNS.
    produce: "lista de decisiones ajenas tocadas, con su capa"
    termina_cuando: "cada capa anterior está contrastada o consta que no existe"
    checkpoint: false
  - n: 5
    nombre: DICTAMINAR
    modo: convergente
    hace: >
      Recorrer las siete comprobaciones de gate:revision-de-construccion y anotarlas. Cada
      hallazgo lleva fichero, línea, si bloquea y el arreglo exacto. Si hay un bloqueante,
      el dictamen es no-superado y la entrega es una devolución con los cuatro campos de C5.
    produce: "dictamen y, cuando hay un hallazgo bloqueante, la devolución"
    termina_cuando: "las siete comprobaciones están anotadas y el dictamen es superado o no-superado"
    checkpoint: true
artefactos:
  - "ficheros tocados con veredicto"
  - "tabla de reversión de pruebas"
  - "hallazgos con fichero, línea, si bloquea y arreglo propuesto"
  - "dictamen del gate"
puntos_owner:
  - "ninguno"
consultas:
  - "ARQ: ¿esta decisión del diff cambia el plan técnico aprobado? Responde sí o no, y qué parte"
  - "DIS: ¿esta diferencia respecto a la especificación conserva la intención? Responde sí o no"
checkpoints:
  - "tras cada paso con checkpoint"
critica:
  - "¿he leído el diff entero o he mirado sólo lo que el encargo nombraba?"
  - "¿he ejecutado la reversión de cada prueba, o he dado por bueno que muerden?"
  - "¿cada hallazgo bloqueante tiene fichero y línea, o es una impresión?"
  - "¿he corregido algo en vez de devolverlo?"
gate: gate:revision-de-construccion
salida:
  - "dictamen de gate:revision-de-construccion con su evidencia"
devolucion:
  - "a CNS/implementacion, con los hallazgos bloqueantes como los cuatro campos de C5"
  - "a PRD, DIS o ARQ, cuando el diff revela que su capa era insuficiente"
bloqueo:
  - "no hay commit localizable que revisar"
  - "no hay entorno donde ejecutar las pruebas"
cancelacion:
  - "el item se cancela: el dictamen parcial se conserva como evidencia"
aprendizaje:
  - "un hallazgo que se repite en dos paquetes es una convención que falta, y se propone"
  - "una prueba que no muerde y nadie vio señala un patrón de prueba decorativa que hay que nombrar"
prueba_de_reanudacion: >
  Un revisor nuevo lee el checkpoint, ve qué ficheros ya tienen veredicto y qué pruebas ya
  se revirtieron, y continúa por el siguiente fichero sin releer los anteriores ni repetir
  reversiones. Es la prueba T461.
```
