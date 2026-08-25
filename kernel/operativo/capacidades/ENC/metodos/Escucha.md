# ENC/Escucha — método principal del interlocutor

El método que se ejecuta **siempre** que el Owner dice algo. Los demás métodos de ENC se
invocan desde dentro de éste.

```yaml ads:metodo
id: ENC/Escucha
nombre: Escucha
capacidad: ENC
disparador:
  - "el Owner escribe o dice cualquier cosa al sistema"
  - "un encuadre entregado vuelve devuelto por DSP o por el crítico"
carga:
  - "estado/memoria/ENC/lexico-del-owner.md"
  - "estado/memoria/ENC/preguntas-resueltas.md"
  - "el encuadre en curso, si la expresión continúa una conversación anterior"
  - "el checkpoint del paquete de encuadre, si existe"
preguntas_iniciales:
  - "¿esta expresión continúa algo anterior, o abre algo nuevo? — se resuelve contra el estado, no preguntando"
  - "¿de cuál de las nueve clases de entrada se trata?"
  - "¿qué forma de conversación del catálogo aplica?"
pasos:
  - n: 1
    nombre: CAPTURAR
    modo: lineal
    hace: >
      Escribir la expresión literal con fecha y canal en expresion_literal[], sin corregir
      ortografía, orden ni tono. Si el Owner aporta imágenes, se registran como referencia
      con su fecha, y si el agente no tiene visión se deriva su lectura y se deja escrito.
    produce: "entrada en expresion_literal[]"
    termina_cuando: "la literal está escrita antes de que exista ninguna interpretación"
    checkpoint: false
  - n: 2
    nombre: CLASIFICAR
    modo: lineal
    hace: >
      Aplicar la taxonomía de entrada. Para separar idea inmadura de candidato se usa la
      prueba escrita de tres condiciones, no la intuición. La clase elegida y su motivo
      quedan escritos.
    produce: "clasificacion.naturaleza con motivo"
    termina_cuando: "hay exactamente una clase elegida y su motivo escrito"
    checkpoint: true
  - n: 3
    nombre: ELEGIR FORMA
    modo: lineal
    hace: >
      Localizar en el catálogo de formas de conversación la que corresponde a esta
      expresión y ejecutar lo que esa forma declara: qué resuelve solo, qué pregunta,
      cuándo muestra referencias, cuándo hace brainstorming, cuándo consulta especialista.
    produce: "la forma aplicada, escrita en el checkpoint"
    termina_cuando: "la forma está elegida y su primer paso ejecutado"
    checkpoint: true
  - n: 4
    nombre: ANCLAR
    modo: lineal
    hace: >
      Invocar ENC/Anclaje. No se clasifica nada como candidato a trabajo antes de tener
      el dosier. Si el dosier revela duplicación, la expresión se replantea como orden
      sobre el item existente y se vuelve al paso 2.
    produce: "el objeto anclaje del encuadre"
    termina_cuando: "gate:anclaje-completo cumplido, o la expresión no requería anclaje por no ser candidato"
    checkpoint: true
  - n: 5
    nombre: MEDIR INCERTIDUMBRE
    modo: lineal
    hace: >
      Aplicar la escala de incertidumbre sobre los cinco ejes y escribir grado, ejes y
      motivo. El grado determina si el paso 6 es obligatorio.
    produce: "el objeto incertidumbre"
    termina_cuando: "los tres campos están escritos y el grado deriva de los ejes, no de una impresión"
    checkpoint: true
  - n: 6
    nombre: CONVERSAR
    modo: conversacional
    hace: >
      Ejecutar la conversación que la forma elegida declara: preguntas, referencias,
      brainstorming o consulta a especialista. Se persiste lo comprendido ANTES de
      formular cada pregunta, para que un corte no pierda lo entendido.
    produce: "respuestas del Owner captadas literalmente y su efecto sobre la interpretación"
    termina_cuando: >
      la incertidumbre baja a media o baja en todos los ejes que condicionan el resultado
      perseguido, o el Owner declara que no quiere seguir profundizando ahora
    checkpoint: true
  - n: 7
    nombre: FORMULAR
    modo: convergente
    hace: >
      Invocar ENC/Formulacion para producir el encuadre completo conforme al esquema.
    produce: "el bloque ads:encuadre"
    termina_cuando: "todos los campos del esquema están escritos, incluidas las dudas abiertas"
    checkpoint: true
  - n: 8
    nombre: CRITICAR
    modo: convergente
    hace: >
      Si la incertidumbre es alta o el nivel de Owner calculado es obligatorio, invocar
      ENC/Critica con un agente distinto. Si el dictamen devuelve, volver al paso que
      corresponda al hueco señalado.
    produce: "dictamen de crítica"
    termina_cuando: "el dictamen es conforme, o el encuadre vuelve al paso señalado"
    checkpoint: true
  - n: 9
    nombre: CONFIRMAR
    modo: conversacional
    hace: >
      Pedir confirmación al Owner SÓLO cuando la tabla de confirmación lo exige. En los
      demás casos no se pregunta: se entrega y se informa.
    produce: "confirmación registrada, o constancia de que no era exigible"
    termina_cuando: "hay confirmación, o la tabla declara que no procedía pedirla"
    checkpoint: true
  - n: 10
    nombre: ENTREGAR
    modo: lineal
    hace: >
      Comprobar gate:encuadre-listo y entregar a DSP. Informar al Owner en lenguaje
      comprensible: qué se ha entendido, qué va a pasar, qué NO se ha creado y por qué.
    produce: "encuadre en estado entregado y respuesta al Owner"
    termina_cuando: "DSP acusa recibo del encuadre"
    checkpoint: true
artefactos:
  - "expresion_literal[] — se escribe en el paso 1 y no se toca más"
  - "dosier de anclaje — paso 4"
  - "medición de incertidumbre — paso 5"
  - "transcripción de decisiones del Owner captadas — paso 6"
  - "encuadre completo — paso 7"
  - "dictamen de crítica — paso 8"
puntos_owner:
  - "paso 6: la conversación, tantas veces como la forma elegida declare"
  - "paso 9: confirmación, sólo cuando la tabla de confirmación la exige"
  - "paso 10: informe de qué se creó y qué no; no es una petición de permiso"
consultas:
  - "ENC/anclaje en el paso 4, siempre que la expresión sea candidata a trabajo"
  - "DIS, ARQ, DOM, SEG, PRD o INV en modo consulta durante el paso 6, con pregunta cerrada"
  - "ENC/critica-de-encuadre en el paso 8, cuando la condición se cumple"
checkpoints:
  - "tras los pasos 2 a 10"
  - "dentro del paso 6, tras cada respuesta del Owner que cambie el entendimiento"
  - "antes de formular cada pregunta importante, persistiendo primero lo comprendido"
critica:
  - "¿la interpretación se sostiene leyendo sólo la expresión literal?"
  - "¿alguna pregunta hecha ya estaba contestada en preguntas-resueltas.md?"
  - "¿la incertidumbre declarada coincide con la que se lee en el texto?"
  - "¿se ha creado trabajo que el Owner no pidió?"
  - "¿se ha perdido una intención real por clasificarla como nota u observación?"
gate: gate:encuadre-listo
salida:
  - "encuadre entregado a DSP, o"
  - "ficha de vivero para una idea inmadura, o"
  - "anotación en la memoria de la capacidad competente, o"
  - "evento de orden sobre un item existente, o"
  - "descarte con motivo escrito"
devolucion:
  - "al Owner, cuando su expresión contradice una decisión suya anterior: se muestran ambas"
  - "a ENC/anclaje, cuando el dosier no resuelve no_existe_y_se_creia"
bloqueo:
  - "el Owner no responde una pregunta que condiciona el resultado perseguido: el encuadre queda esperando-owner, no bloqueado"
  - "el repositorio no está accesible y el anclaje no puede ejecutarse: bloqueado, nombrando eso"
cancelacion:
  - "el Owner declara que retira la expresión"
  - "el anclaje demuestra que lo pedido ya existe y funciona: se descarta con enlace a lo existente"
aprendizaje:
  - "toda pregunta hecha se registra en preguntas-resueltas.md para no repetirla"
  - "todo término nuevo del Owner se registra en el léxico"
  - "un encuadre devuelto dos veces por el mismo tipo de hueco genera entrada en defectos-de-encuadre.md"
prueba_de_reanudacion: >
  Un agente nuevo abre el paquete de encuadre, lee el checkpoint, comprueba based_on
  contra el índice de lo existente y el estado, y continúa en el paso exacto. La prueba
  concreta es T77: se corta la conversación entre el paso 6 y el 7, se releva al agente, y
  el nuevo formula el encuadre sin volver a preguntar al Owner nada ya contestado.
```
