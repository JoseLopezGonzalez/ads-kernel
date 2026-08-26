# ENC/Orden — cuando el Owner manda sobre algo que ya existe

Una orden no es contenido. Cambia el **gobierno** de un item: prioridad, aparcado,
cancelación, recomposición, continuación. Este método traduce lenguaje natural a evento,
y su regla dominante es la de b.13: **el Owner nunca tiene que escribir un identificador**.

```yaml ads:metodo
id: ENC/Orden
nombre: Orden
capacidad: ENC
disparador:
  - "la expresión del Owner tiene como objetivo un item o paquete que ya existe"
  - "la intención cae en el catálogo de b.13"
carga:
  - "el estado persistido: items abiertos, aparcados, bloqueados y en espera"
  - "estado/memoria/ENC/lexico-del-owner.md"
  - "la base vigente sobre la que se emitiría la orden"
preguntas_iniciales:
  - "¿qué intención del catálogo es? — se resuelve interpretando, no preguntando"
  - "¿a qué item se refiere? — se resuelve con el índice de lo existente"
  - "¿es unívoca y reversible, o ambigua o irreversible?"
pasos:
  - n: 1
    nombre: INTERPRETAR
    modo: lineal
    hace: >
      Proponer intención, objetivo y parámetros. La intención sale del catálogo de b.13;
      los parámetros, de la frase.
    produce: "tripleta intención + objetivo + parámetros"
    termina_cuando: "la tripleta está escrita"
    checkpoint: false
  - n: 2
    nombre: ANCLAR EL OBJETIVO
    modo: lineal
    hace: >
      Resolver a qué item se refiere el Owner usando el índice de lo existente y el léxico.
      Se puntúa cada candidato y se conservan los dos mejores con su puntuación.
    produce: "candidato principal, segundo candidato y sus puntuaciones"
    termina_cuando: "hay puntuación para todos los candidatos plausibles"
    checkpoint: true
  - n: 3
    nombre: CLASIFICAR
    modo: lineal
    hace: >
      Aplicar las cuatro condiciones de ambigüedad de b.13 y la definición de
      irreversibilidad. Unívoca y reversible se aplica directamente, sin confirmar.
    produce: "veredicto: aplicable directamente, o requiere desambiguación, o requiere confirmación"
    termina_cuando: "el veredicto está escrito con la condición concreta que lo produjo"
    checkpoint: true
  - n: 4
    nombre: DESAMBIGUAR
    modo: conversacional
    hace: >
      Sólo si el paso 3 lo exige. Presentar los candidatos por nombre humano, naturaleza y
      estado. NUNCA por identificador. Máximo tres candidatos; si hay más, se pregunta por
      la materia antes que por el item.
    produce: "el item elegido por el Owner"
    termina_cuando: "el Owner ha señalado uno, o ha dicho que ninguno"
    checkpoint: true
  - n: 5
    nombre: EMITIR EVENTO
    modo: lineal
    hace: >
      Escribir el evento con atribución completa: autoridad Owner, ordenante Owner,
      escritor del comando el agente, ejecutor DSP, base y texto literal de la orden.
    produce: "evento de orden"
    termina_cuando: "el evento está escrito ANTES de que se toque el estado canónico"
    checkpoint: true
  - n: 6
    nombre: INFORMAR
    modo: lineal
    hace: >
      Decir al Owner qué se ha hecho, en una línea, con el nombre humano del item. No se
      pide confirmación de lo ya aplicado.
    produce: "respuesta al Owner"
    termina_cuando: "el Owner tiene la confirmación de lo aplicado"
    checkpoint: false
artefactos:
  - "tripleta intención + objetivo + parámetros"
  - "puntuación de candidatos"
  - "evento de orden con atribución completa"
puntos_owner:
  - "paso 4: sólo cuando la orden es ambigua según las cuatro condiciones de b.13"
  - "confirmación explícita cuando la orden es irreversible: cancela algo, toca materia reservada o un item cerrado"
consultas:
  - "DSP, para comprobar que la base de la orden sigue vigente antes de emitir el evento"
checkpoints:
  - "tras los pasos 2, 3, 4 y 5"
critica:
  - "¿se pidió confirmación de algo unívoco y reversible? Eso convierte al Owner en un botón"
  - "¿se presentó algún identificador al Owner?"
  - "¿la orden se aplicó sobre una base que ya había cambiado?"
gate: gate:orden-emitida
salida:
  - "evento de orden entregado a DSP"
  - "respuesta al Owner en lenguaje natural"
devolucion:
  - "a DSP, cuando la base de la orden dejó de ser vigente: la orden se marca en conflicto con ambas intenciones escritas"
bloqueo:
  - "el objetivo de la orden no existe en el estado y el Owner no está disponible para desambiguar"
cancelacion:
  - "el Owner retira la orden antes de que se emita el evento"
aprendizaje:
  - "cada desambiguación registra qué nombre usó el Owner y a qué item correspondía, en el léxico"
  - "tres desambiguaciones sobre el mismo item señalan que su nombre humano está mal elegido"
prueba_de_reanudacion: >
  Un agente nuevo lee el checkpoint y sabe si el evento llegó a emitirse. Aplicar un evento
  por identificador dos veces es una no-operación, de modo que la reanudación converge sin
  inventar estado. La prueba es T83.
```

```yaml ads:gate
id: gate:orden-emitida
aplica_a: "un evento de orden antes de que DSP lo aplique al estado canónico"
comprobaciones:
  - id: atribucion-completa
    comprueba: "el evento distingue autoridad, ordenante, escritor del comando y ejecutor"
    como: "comprobación estructural de los cuatro campos"
    automatizable: si
  - id: base-vigente
    comprueba: "la base declarada por el evento sigue siendo la vigente"
    como: "comparación contra el estado canónico en el momento de aplicar"
    automatizable: si
  - id: literal-conservada
    comprueba: "el texto literal de la orden está en el evento"
    como: "comprobación estructural"
    automatizable: si
  - id: sin-identificadores-al-owner
    comprueba: "ninguna pregunta hecha al Owner durante la desambiguación contenía un identificador"
    como: "lectura de la transcripción de la desambiguación"
    automatizable: parcial
  - id: confirmacion-solo-si-procede
    comprueba: "no se pidió confirmación de una orden unívoca y reversible"
    como: "comparación entre el veredicto del paso 3 y lo que se preguntó"
    automatizable: si
evidencia:
  - "el evento con su atribución"
  - "la puntuación de candidatos del paso 2"
  - "la transcripción de la desambiguación, cuando la hubo"
fallo: >
  El evento no se aplica. Si falló base-vigente, la orden se marca en conflicto con ambas
  intenciones escritas y no se aplica ni se borra, conforme al protocolo de a.9.
```
