# INV/Investigacion — contestar con evidencia

```yaml ads:metodo
id: INV/Investigacion
nombre: Investigacion
capacidad: INV
disparador:
  - "una capacidad hace una pregunta acotada con su consumidor declarado"
  - "DSP despacha un item de tipo INV"
carga:
  - "la pregunta y su consumidor"
  - "investigaciones anteriores sobre la misma materia y su frescura"
preguntas_iniciales:
  - "¿qué decisión se tomará con esta respuesta?"
  - "¿qué respuesta cambiaría el plan de quien pregunta?"
  - "¿esta pregunta se puede contestar, o hay que acotarla primero?"
pasos:
  - n: 1
    nombre: ACOTAR
    modo: convergente
    hace: >
      Reformular la pregunta hasta que tenga respuesta posible, y escribir qué decisión la
      consumirá. Sin consumidor, la investigación no empieza.
    produce: "pregunta acotada y consumidor declarado"
    termina_cuando: "la pregunta admite una respuesta que cambiaría el plan de alguien"
    checkpoint: true
  - n: 2
    nombre: BUSCAR Y CONTRASTAR
    modo: divergente
    hace: >
      Reunir fuentes, contrastarlas entre sí y registrar cuáles son fiables y por qué,
      con su fecha.
    produce: "fuentes con su fiabilidad y fecha"
    termina_cuando: "las fuentes coinciden, o su desacuerdo está registrado como parte de la respuesta"
    checkpoint: true
  - n: 3
    nombre: MEDIR CONTRA LO REAL
    modo: lineal
    hace: >
      Cuando la pregunta lo exige, encargar a CON/experimental un spike contra el entorno
      real, con la evidencia declarada antes de construirlo.
    produce: "medición o experimento con su evidencia"
    termina_cuando: "la medición existe, o está escrito que no era necesaria y por qué"
    checkpoint: true
  - n: 4
    nombre: RESPONDER
    modo: convergente
    hace: >
      Escribir la respuesta, incluida la evidencia que la contradice, el límite de alcance y
      la frescura. Si no se puede decidir todavía, DECLARARLO y decir qué falta.
    produce: "informe de investigación"
    termina_cuando: "gate:evidencia-fresca recorrido y anotado"
    checkpoint: true
artefactos:
  - "pregunta acotada y consumidor"
  - "fuentes con fiabilidad y fecha"
  - "medición o experimento"
  - "informe con frescura y límite"
puntos_owner:
  - "ninguno: la evidencia la presenta la capacidad propietaria de la materia"
consultas:
  - "CON/experimental: construir el spike declarado, con la evidencia que debe producir"
  - "la capacidad que preguntó: ¿esta reformulación sigue sirviendo para tu decisión? Responde sí o no"
checkpoints:
  - "tras cada paso"
  - "al descartar cada hipótesis"
critica:
  - "¿estoy contestando la pregunta que me hicieron o una parecida más fácil?"
  - "¿he incluido lo que contradice mi conclusión?"
  - "¿estoy rellenando con una aproximación lo que no he averiguado?"
gate: gate:evidencia-fresca
salida:
  - "informe entregado al consumidor declarado"
  - "cero o más items nuevos, sólo si se decide fabricar algo con la evidencia"
devolucion:
  - "a quien preguntó, cuando la pregunta no es respondible como está"
bloqueo:
  - "no hay acceso a fuentes ni al entorno donde medir"
cancelacion:
  - "la decisión se toma por otra vía: se conserva la evidencia parcial con su fecha"
aprendizaje:
  - "toda investigación entra en docs/investigacion con su respuesta, incluida la negativa"
  - "una respuesta que caducó antes de usarse señala que la pregunta llegó demasiado pronto"
prueba_de_reanudacion: >
  Un agente nuevo lee las fuentes ya consultadas y las hipótesis descartadas, y continúa sin
  repetirlas. Un INV puede cerrar SIN generar un segundo item: la evidencia es su resultado.
  Es la prueba T113.
```
