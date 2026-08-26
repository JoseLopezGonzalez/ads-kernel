# PRD/Definicion — de encuadre a intención definida

```yaml ads:metodo
id: PRD/Definicion
nombre: Definicion
capacidad: PRD
disparador:
  - "DSP despacha un paquete de PRD sobre un item de tipo FEA"
  - "un DEF cambia de proceso porque el diagnóstico reveló C-PRD"
carga:
  - "el encuadre completo, incluida la expresión literal del Owner"
  - "docs/producto/EXITO.md, ALCANCE.md y DECISIONES.md"
  - "el dosier de anclaje: qué existe ya que toque esto"
preguntas_iniciales:
  - "¿qué problema tiene detrás la solución que el Owner propuso?"
  - "¿a quién le cambia la vida esto, y en qué momento de su trabajo?"
  - "¿qué haría que esto fuera un fracaso aunque funcionara?"
pasos:
  - n: 1
    nombre: SEPARAR PROBLEMA DE SOLUCIÓN
    modo: convergente
    hace: >
      Distinguir lo que el Owner pidió de lo que le pasa. Ambos se conservan: la solución
      propuesta es un dato, no el alcance.
    produce: "problema y solución propuesta, escritos por separado"
    termina_cuando: "el problema está escrito sin mencionar la solución propuesta"
    checkpoint: true
  - n: 2
    nombre: DECLARAR EL FUERA DE ALCANCE
    modo: convergente
    hace: >
      Escribir qué NO entra. Se empieza por aquí y no por el alcance: es lo que ahorra
      trabajo y lo que casi nadie escribe.
    produce: "lista de fuera de alcance con el motivo de cada exclusión"
    termina_cuando: "hay al menos un elemento fuera de alcance con su motivo"
    checkpoint: true
  - n: 3
    nombre: DECLARAR EL ALCANCE
    modo: convergente
    hace: >
      Escribir qué entra, para quién y en qué momento se usa, enlazando con la definición de
      éxito del Owner o declarando que es trabajo interno.
    produce: "alcance declarado con perfil de uso"
    termina_cuando: "el alcance nombra un perfil concreto y enlaza con el éxito del Owner"
    checkpoint: true
  - n: 4
    nombre: ESCRIBIR CRITERIOS
    modo: convergente
    hace: >
      Escribir cada criterio de éxito con qué se mira, dónde y qué resultado cuenta. Y la
      definición de fracaso, que aporta algo distinto de negar el éxito.
    produce: "criterios de éxito y definición de fracaso"
    termina_cuando: "un tercero podría verificar cada criterio leyéndolo, sin preguntar"
    checkpoint: true
  - n: 5
    nombre: CERRAR CONTRA EL GATE
    modo: convergente
    hace: "Recorrer las seis comprobaciones de gate:intencion-definida y anotar cada una."
    produce: "capa de PRD depositada, o lista de lo que falta"
    termina_cuando: "las seis comprobaciones están anotadas"
    checkpoint: true
artefactos:
  - "problema y solución propuesta separados"
  - "fuera de alcance con motivos"
  - "alcance con perfil de uso"
  - "criterios de éxito y definición de fracaso"
puntos_owner:
  - "paso 3, cuando el alcance es relevante o estratégico"
  - "paso 4, cuando un criterio depende de su juicio y no de una medición"
consultas:
  - "ARQ: ¿hay alguna restricción técnica que haga inviable parte de este alcance? Responde con la restricción y su evidencia"
  - "DIS: ¿este alcance toca alguna superficie sin patrón vigente? Responde sí o no, y cuál"
checkpoints:
  - "tras cada paso"
  - "antes de escalar cualquier decisión al Owner"
critica:
  - "¿he registrado el problema, o sólo la solución que me pidieron?"
  - "¿el fuera de alcance está vacío porque no hay nada, o porque no lo he pensado?"
  - "¿algún criterio de éxito sólo lo puedo comprobar yo?"
gate: gate:intencion-definida
salida:
  - "capa de intención depositada, con alcance, criterios y definición de fracaso"
devolucion:
  - "a ENC, cuando el encuadre contiene dos resultados perseguidos sin separar"
bloqueo:
  - "el alcance depende de una decisión del Owner sin respuesta"
  - "el alcance depende de evidencia que exige un item INV previo"
cancelacion:
  - "el anclaje demuestra que el resultado ya existe: se cancela con enlace a lo existente"
  - "el problema se disolvió: en items internos lo cancela PRD; si lo pidió el Owner, lo propone"
aprendizaje:
  - "un fuera de alcance que después hubo que incluir señala un encuadre incompleto"
  - "un criterio que VER no supo verificar se registra para reformular la forma de escribirlos"
prueba_de_reanudacion: >
  Un agente nuevo abre el paquete, lee qué está cerrado del alcance y qué preguntas están
  pendientes con el Owner, y continúa sin volver a preguntar lo contestado. Es la prueba T100.
```
