# ENC/Maduracion — llevar una idea inmadura hasta poder decidir si es trabajo

El Owner no tiene que saber redactar requisitos. Este método existe para que **descubra**
lo que quiere, no para exigirle que lo traiga escrito.

```yaml ads:metodo
id: ENC/Maduracion
nombre: Maduracion
capacidad: ENC
disparador:
  - "la prueba de frontera clasifica la expresión como idea inmadura"
  - "el Owner vuelve sobre una ficha del vivero"
  - "la incertidumbre medida es alta en el eje «qué resultado se persigue»"
carga:
  - "la ficha del vivero, si la idea ya estuvo aquí"
  - "el dosier de anclaje, cuando existe"
  - "las referencias y decisiones de la materia, para poder mostrar alternativas"
preguntas_iniciales:
  - "¿qué te haría decir que esto ha quedado bien?"
  - "¿qué pasa hoy que no te gusta, la última vez que lo viste?"
  - "¿esto lo has visto resuelto en algún sitio que te gustara?"
pasos:
  - n: 1
    nombre: LOCALIZAR LA MOLESTIA
    modo: conversacional
    hace: >
      Llevar la conversación del deseo abstracto al momento concreto: cuándo lo notó, qué
      estaba haciendo, qué esperaba que pasara. Un ejemplo concreto vale más que tres
      adjetivos.
    produce: "problema_observado y situacion_actual del encuadre"
    termina_cuando: "existe al menos un caso concreto, con pantalla, momento o dato real"
    checkpoint: true
  - n: 2
    nombre: MOSTRAR ALTERNATIVAS
    modo: divergente
    hace: >
      Cuando el Owner no sabe qué quiere, no se le pregunta más: se le enseña. Se presentan
      entre dos y cuatro direcciones distintas ENTRE SÍ —no variaciones de una— con lo que
      cada una implica y lo que cada una sacrifica. Para materia de forma, se pide a DIS en
      modo consulta que aporte referencias con su principio extraído.
    produce: "alternativas presentadas y reacción del Owner a cada una"
    termina_cuando: "el Owner ha reaccionado a todas, aunque sea rechazándolas"
    checkpoint: true
  - n: 3
    nombre: BRAINSTORMING
    modo: divergente
    hace: >
      Sólo si el paso 2 no convergió: generar posibilidades sin filtrar, incluidas las que
      el sistema cree malas, marcadas como tales. El objetivo es que el Owner reconozca por
      contraste lo que sí quiere.
    produce: "lista de posibilidades con la reacción del Owner"
    termina_cuando: "el Owner señala una dirección, o declara que no quiere seguir ahora"
    checkpoint: true
  - n: 4
    nombre: PROBAR LA FRONTERA
    modo: convergente
    hace: >
      Aplicar la prueba de tres condiciones. Si pasa, la idea deja de ser inmadura y el
      control vuelve a ENC/Escucha en su paso 5. Si no pasa, se escribe en la ficha del
      vivero exactamente cuál de las tres falló.
    produce: "veredicto de madurez con la condición que falló, si falló"
    termina_cuando: "el veredicto está escrito"
    checkpoint: true
  - n: 5
    nombre: DEVOLVER AL VIVERO
    modo: lineal
    hace: >
      Si sigue inmadura, actualizar la ficha con todo lo conversado y con qué falta. No se
      propone plazo ni recordatorio: el vivero no es una cola.
    produce: "ficha de vivero actualizada"
    termina_cuando: "la ficha recoge la conversación completa y lo que falta"
    checkpoint: true
artefactos:
  - "ficha de vivero"
  - "alternativas presentadas y reacción a cada una"
  - "casos concretos aportados por el Owner"
puntos_owner:
  - "paso 1: conversación para localizar la molestia"
  - "paso 2: presentación de alternativas"
  - "paso 3: brainstorming, sólo si el paso 2 no convergió"
consultas:
  - "DIS en modo consulta, para aportar referencias y principios cuando la materia es de forma"
  - "INV en modo consulta, cuando la duda es sobre lo que es técnicamente posible"
  - "PRD en modo consulta, cuando la duda es si esto encaja con la definición de éxito del Owner"
checkpoints:
  - "tras cada paso"
  - "tras cada reacción del Owner a una alternativa, incluyendo su formulación literal"
critica:
  - "¿las alternativas eran distintas entre sí, o variaciones de la misma?"
  - "¿se convirtió en candidato una idea que sigue sin evidencia de cierre escribible?"
  - "¿se presionó al Owner para cerrar cuando él no quería cerrar todavía?"
gate: gate:encuadre-listo
salida:
  - "la idea pasa a candidato y vuelve a ENC/Escucha paso 5, o"
  - "la idea vuelve al vivero con lo que falta escrito"
devolucion:
  - "al Owner, cuando la idea contradice una decisión suya vigente"
bloqueo:
  - "las alternativas requieren evidencia técnica que no existe: se propone un item INV y la idea espera"
cancelacion:
  - "el Owner retira la idea: la ficha del vivero se marca retirada y se conserva"
aprendizaje:
  - "el tipo de alternativa que hace converger a este Owner se registra en el léxico"
  - "una idea que vuelve al vivero tres veces por la misma condición señala un hueco de conocimiento del sistema"
prueba_de_reanudacion: >
  Un agente nuevo abre la ficha del vivero, lee las alternativas ya presentadas y la
  reacción del Owner a cada una, y continúa sin repetirlas. La prueba es T82: se releva al
  agente entre el paso 2 y el 3 y el entrante no vuelve a proponer una alternativa ya
  rechazada.
```
