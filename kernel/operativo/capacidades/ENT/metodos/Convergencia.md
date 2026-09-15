# ENT/Convergencia — declarar el conjunto exacto que se probó junto

```yaml ads:metodo
id: ENT/Convergencia
nombre: Convergencia
capacidad: ENT
disparador:
  - "un item que escribe fuentes tiene su capa de construcción revisada y su dosier de VER, y su circuito base exige el nivel integrado"
carga:
  - "las entregas de CNS/implementacion del item, con commit, rama y PR de cada fuente"
  - "el dosier de VER/dosier con las revisiones que verificó"
  - "las fuentes que el item escribe, y SOURCES.toml para su identidad"
preguntas_iniciales:
  - "¿qué fuentes escribe el item, y tiene cada una una revisión entregada?"
  - "¿el dosier de VER se hizo sobre esas mismas revisiones, o sobre otras?"
  - "¿a qué combinación anterior se vuelve si hay que revertir?"
pasos:
  - n: 1
    nombre: RESOLVER LAS REVISIONES
    modo: lineal
    hace: >
      Para cada fuente escrita por el item, tomar el commit de la entrega de construcción,
      comprobar que existe en su fuente y anotar rama y PR. Una fuente sin revisión no se
      inventa: el conjunto queda parcial y se devuelve.
    produce: "lista fuente → SHA → rama → PR"
    termina_cuando: "cada fuente escrita tiene su SHA verificado, o consta cuál falta"
    checkpoint: true
  - n: 2
    nombre: CRUZAR CON LA VERIFICACIÓN
    modo: lineal
    hace: >
      Cruzar los commits del dosier de VER con los resueltos. Escribir una fila de
      verificación por ámbito citando el dosier; si el dosier verificó otra revisión, no se
      cita: se devuelve a VER.
    produce: "filas de verificación con resultado y evidencia"
    termina_cuando: "ningún ámbito queda pendiente ni en fallo, o el conjunto se devuelve"
    checkpoint: true
  - n: 3
    nombre: DECLARAR Y DICTAMINAR
    modo: lineal
    hace: >
      Declarar el estado del conjunto y a qué combinación se restaura, escribir el
      Integration Set con su forma canónica, y emitir el dictamen de
      gate:convergencia-de-fuentes sobre la capa de construcción.
    produce: "el Integration Set y el dictamen"
    termina_cuando: "el conjunto valida contra su esquema y la oficina admite el dictamen"
    checkpoint: true
artefactos:
  - "el Integration Set del item"
  - "el dictamen de gate:convergencia-de-fuentes"
puntos_owner:
  - "ninguno: la convergencia no es materia reservada"
consultas:
  - "VER: ¿sobre qué revisiones exactas se hizo el dosier? Responde con los SHA"
checkpoints:
  - "tras cada paso"
critica:
  - "¿cada fuente entra por SHA, o he escrito una rama?"
  - "¿la verificación que cito se hizo sobre estas revisiones?"
  - "¿he dejado alguna fuente escrita fuera del conjunto?"
gate: gate:convergencia-de-fuentes
salida:
  - "Integration Set con estado verificado o integrado"
devolucion:
  - "a CNS/implementacion, cuando una fuente escrita no tiene revisión o la entregada no existe"
  - "a VER/dosier, cuando la verificación no cubre estas revisiones"
bloqueo:
  - "no hay acceso a una fuente para resolver su revisión"
cancelacion:
  - "el item se cancela: el conjunto se conserva como descartado, explicando por qué existe el siguiente"
aprendizaje:
  - "una fuente que se olvida sistemáticamente en el alcance señala un defecto de encuadre"
prueba_de_reanudacion: >
  Un agente nuevo lee el checkpoint, ve qué fuentes ya tienen SHA resuelto y cuáles no, y
  continúa por la que falta sin volver a resolver las anteriores. Es la prueba T468.
```
