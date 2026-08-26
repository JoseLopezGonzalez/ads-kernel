# VER/Decision — verificar una decisión, no su implementación

```yaml ads:metodo
id: VER/Decision
nombre: Decision
capacidad: VER
disparador:
  - "un item DIR ha producido su registro de decisión y sus items derivados"
carga:
  - "el registro de decisión del DIR"
  - "el radio de impacto analizado por ARQ"
  - "la lista de items derivados creados"
  - "las decisiones anteriores que se sustituyen"
preguntas_iniciales:
  - "¿qué decisiones concretas quedan sustituidas, y está escrito?"
  - "¿qué impactos conocidos hay, y cuál de ellos no tiene item derivado?"
  - "¿hay alguna construcción productiva escondida dentro de este DIR?"
pasos:
  - n: 1
    nombre: RECORRER LAS NUEVE
    modo: lineal
    hace: >
      Comprobar una a una las nueve condiciones de VER:decision de b.16, anotando el
      resultado y la evidencia de cada una.
    produce: "las nueve comprobaciones con su resultado"
    termina_cuando: "las nueve están anotadas"
    checkpoint: true
  - n: 2
    nombre: BUSCAR IMPACTOS SIN PROPIETARIO
    modo: divergente
    hace: >
      Cruzar el radio de impacto con la lista de items derivados y localizar lo que queda
      sin cubrir.
    produce: "lista de impactos sin item derivado"
    termina_cuando: "cada elemento del radio está cubierto por un item o declarado como no accionable"
    checkpoint: true
  - n: 3
    nombre: BUSCAR CONSTRUCCIÓN ESCONDIDA
    modo: lineal
    hace: >
      Comprobar que ningún paquete del DIR ha construido funcionalidad productiva. Sólo
      CON:experimental es admisible, y sólo antes de la decisión.
    produce: "veredicto sobre construcción productiva"
    termina_cuando: "está comprobado que no hay implementación productiva dentro del DIR"
    checkpoint: true
  - n: 4
    nombre: GATE CONJUNTO
    modo: convergente
    hace: >
      Las capacidades propietarias de las decisiones sustituidas confirman que su materia
      está representada correctamente. Esto NO les da veto sobre la dirección elegida.
    produce: "confirmaciones de las capacidades afectadas"
    termina_cuando: "cada capacidad afectada ha confirmado o ha registrado su objeción"
    checkpoint: true
  - n: 5
    nombre: DICTAMINAR
    modo: convergente
    hace: "Emitir conforme o devuelto, con los huecos y qué cerraría cada uno."
    produce: "dictamen"
    termina_cuando: "el veredicto está escrito"
    checkpoint: true
artefactos:
  - "las nueve comprobaciones"
  - "lista de impactos sin item derivado"
  - "confirmaciones del gate conjunto"
  - "dictamen"
puntos_owner:
  - "ninguno: la decisión del Owner ya está tomada y este método no la juzga"
consultas:
  - "ARQ: ¿el radio de impacto está medido o estimado? Responde con la traza"
  - "las capacidades propietarias de las decisiones sustituidas, por gate conjunto"
checkpoints:
  - "tras cada paso"
critica:
  - "¿estoy rechazando porque habría elegido otra dirección? Eso es un defecto de conformidad"
  - "¿he dado por cubierto un impacto porque alguien dijo que se hará luego?"
  - "¿he mirado si hay construcción productiva escondida?"
gate: gate:evidencia-suficiente
salida:
  - "dictamen conforme, o devuelto con los huecos"
devolucion:
  - "al propietario global del DIR, con los huecos concretos"
bloqueo:
  - "el radio de impacto no está analizado"
cancelacion:
  - "el DIR se cancela antes de dictaminar: las comprobaciones hechas se conservan"
aprendizaje:
  - "un impacto que apareció después señala un radio mal medido, y se registra"
  - "una construcción productiva escondida es aprendizaje promovible sobre composición de rutas"
prueba_de_reanudacion: >
  Un agente nuevo lee qué comprobaciones están hechas y continúa por las que faltan. Es la
  prueba T109.
```
