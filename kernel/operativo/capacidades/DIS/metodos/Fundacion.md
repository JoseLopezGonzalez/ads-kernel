# DIS/Fundacion — dirección visual de un proyecto nuevo

Para un producto **sin dirección visual**. Es el método más largo del sistema y **no tiene
techo de sesiones**: limitarlo artificialmente produce la primera dirección que se le
ocurrió a alguien, que es como se fabrica un producto genérico.

```yaml ads:metodo
id: DIS/Fundacion
nombre: Fundacion
capacidad: DIS
disparador:
  - "la escala de novedad devuelve N4: no existe memoria:vision-artistica o está vacía"
  - "un item DIR aprobado sustituye la dirección visual del producto"
carga:
  - "el encuadre del item y el criterio de éxito de PRD"
  - "toda la memoria de diseño existente, aunque esté casi vacía"
  - "las restricciones del pack instalado: medio, entornos, límites físicos"
  - "los datos reales del producto y sus casos extremos"
preguntas_iniciales:
  - "¿qué quiere ser este producto, y qué NO quiere ser? — en palabras del Owner"
  - "¿qué siente alguien la primera vez que lo abre, y qué debería sentir?"
  - "¿qué productos usa el Owner con gusto, y qué le gusta exactamente de ellos?"
  - "¿qué superficie es la que él usa a diario? — será la superficie representativa"
pasos:
  - n: 1
    nombre: CONVERSACIÓN DE VISIÓN
    modo: conversacional
    hace: >
      Conversar con el Owner hasta poder escribir qué quiere ser el producto, con qué
      personalidad y qué emociones en los tres momentos clave. Se le enseñan cosas: no se
      le pide que describa en abstracto. Cada sesión abre y cierra su punto de atención,
      dejando el slot libre entre sesiones.
    produce: "borrador de visión y personalidad, con las palabras literales del Owner"
    termina_cuando: >
      la personalidad está en tres a cinco adjetivos y cada uno tiene su CONTRAEJEMPLO
      escrito, y el Owner reconoce el conjunto como suyo
    checkpoint: true
  - n: 2
    nombre: RECEPCIÓN DE MATERIAL
    modo: lineal
    hace: >
      Recoger las imágenes, capturas, enlaces y productos que el Owner aporta, con su
      reacción a cada uno citada literalmente. Si el agente no tiene visión, la lectura se
      deriva a un rol con visión requerida y queda escrito.
    produce: "material del Owner con su reacción citada"
    termina_cuando: "todo el material aportado está registrado con la reacción a cada pieza"
    checkpoint: true
  - n: 3
    nombre: INVESTIGACIÓN
    modo: divergente
    hace: >
      DIS/investigacion-visual busca dentro y FUERA de la categoría, y extrae el principio
      de cada referencia. DIS/investigacion-ux establece el perfil de uso y consigue datos
      reales con sus extremos.
    produce: "referencias con principio extraído, antirreferencias y perfil de uso"
    termina_cuando: >
      hay al menos ocho referencias con principio extraído, de las cuales al menos tres son
      de fuera de la categoría, y existen datos reales con sus casos extremos
    checkpoint: true
  - n: 4
    nombre: MOODBOARDS Y TERRITORIOS
    modo: divergente
    hace: >
      Agrupar el material en TERRITORIOS CREATIVOS: cada uno con su moodboard, su
      principio rector en una frase, y qué tipo de producto sería el resultado.
    produce: "territorios creativos con moodboard y principio rector"
    termina_cuando: >
      hay al menos tres territorios y ninguno puede describirse con el principio rector de
      otro
    checkpoint: true
  - n: 5
    nombre: REACCIÓN DEL OWNER A LOS TERRITORIOS
    modo: conversacional
    hace: >
      Enseñar los territorios y registrar la reacción literal a cada uno. Se pregunta qué
      le atrae y qué le repele: el rechazo informa tanto como la atracción.
    produce: "reacción del Owner a cada territorio, citada"
    termina_cuando: "el Owner ha reaccionado a todos, aunque sea rechazándolos todos"
    checkpoint: true
  - n: 6
    nombre: EXPLORACIÓN
    modo: divergente
    hace: >
      DIS/diseno-visual desarrolla la superficie representativa en al menos TRES
      direcciones, distintas en al menos dos de las cinco dimensiones, resueltas con datos
      reales y con sus cinco estados esbozados. PROHIBIDO descartar durante esta fase.
    produce: "tres o más direcciones desarrolladas sobre la misma superficie"
    termina_cuando: >
      cada dirección tiene escrito qué gana y qué sacrifica, y DIS/critica-visual confirma
      que difieren en al menos dos dimensiones
    checkpoint: true
  - n: 7
    nombre: CRÍTICA DE LA EXPLORACIÓN
    modo: convergente
    hace: >
      DIS/critica-visual dictamina sobre la exploración: si las direcciones son
      verdaderamente distintas, si alguna es genérica, y si el material de partida bastaba.
    produce: "dictamen sobre la exploración"
    termina_cuando: "el dictamen es conforme, o la exploración vuelve al paso 6 o al 3"
    checkpoint: true
  - n: 8
    nombre: PROTOTIPO DE LAS FINALISTAS
    modo: convergente
    hace: >
      DIS/prototipado hace ejecutables las direcciones finalistas con datos reales, y
      DIS/movimiento especifica y graba el movimiento de cada una.
    produce: "prototipos ejecutables de las finalistas"
    termina_cuando: "cada finalista se puede usar con datos reales en el medio del pack"
    checkpoint: true
  - n: 9
    nombre: DECISIÓN DEL OWNER
    modo: conversacional
    hace: >
      Enseñar los prototipos y recoger la decisión. Es punto de intervención OBLIGATORIO:
      primera dirección visual del producto (a.8).
    produce: "la dirección elegida, con las palabras del Owner"
    termina_cuando: "el Owner ha elegido, o ha pedido volver a explorar con un criterio nuevo"
    checkpoint: true
  - n: 10
    nombre: SISTEMA INICIAL
    modo: convergente
    hace: >
      DIS/sistema-de-diseno formaliza la dirección elegida en sistema: escala tipográfica,
      roles de color con contraste comprobado por par, unidad de ritmo, elevación,
      iconografía y los componentes que la superficie representativa necesita.
    produce: "el sistema de diseño inicial, declarado y construible"
    termina_cuando: >
      la superficie representativa puede construirse entera usando SÓLO valores del
      sistema, sin excepciones
    checkpoint: true
  - n: 11
    nombre: VALIDACIÓN EN SUPERFICIES REPRESENTATIVAS
    modo: convergente
    hace: >
      Aplicar el sistema a una SEGUNDA superficie de naturaleza distinta a la primera, para
      comprobar que el sistema gobierna y no sólo describe.
    produce: "segunda superficie resuelta con el sistema, y las excepciones que necesitó"
    termina_cuando: >
      la segunda superficie está resuelta y toda excepción que necesitó está declarada o
      incorporada al sistema
    checkpoint: true
  - n: 12
    nombre: CIERRE Y MEMORIA
    modo: lineal
    hace: >
      Escribir visión, principios, referencias, sistema, movimiento, componentes y
      decisiones, incluidos TODOS los descartes con su motivo.
    produce: "memoria de diseño completa"
    termina_cuando: "las doce secciones del corpus que aplican están escritas"
    checkpoint: true
artefactos:
  - "borrador y versión final de la visión y la personalidad"
  - "material del Owner con reacciones citadas"
  - "referencias con principio extraído y antirreferencias"
  - "territorios creativos con moodboard"
  - "tres o más direcciones desarrolladas"
  - "dictamen de crítica sobre la exploración"
  - "prototipos ejecutables de las finalistas"
  - "sistema de diseño inicial"
  - "segunda superficie de validación"
puntos_owner:
  - "paso 1: conversación de visión, tantas sesiones como haga falta, abriendo y cerrando el slot"
  - "paso 2: aportación de material"
  - "paso 5: reacción a los territorios"
  - "paso 9: DECISIÓN de la dirección — obligatorio por a.8"
consultas:
  - "PRD: ¿cuál es el criterio de éxito del producto y qué superficie lo concentra?"
  - "ARQ: ¿existe alguna restricción técnica que descarte de entrada alguna dirección? Responde con la restricción y su evidencia"
  - "el pack instalado: matriz de entornos, presupuestos y límites físicos del medio"
checkpoints:
  - "tras cada uno de los doce pasos"
  - "tras cada sesión de conversación con el Owner, persistiendo lo comprendido antes de preguntar"
  - "al descartar un territorio o una dirección, con el motivo escrito antes de seguir"
critica:
  - "¿las tres direcciones difieren en dos dimensiones, o son la misma con otra paleta?"
  - "¿el material de investigación incluye fuentes de fuera de la categoría?"
  - "¿la superficie representativa es la que el Owner usa, o la más fácil de dibujar?"
  - "¿el sistema gobierna la segunda superficie, o hubo que hacer excepciones para todo?"
  - "¿están escritos los descartes, o sólo lo elegido?"
gate: gate:excelencia-visual
salida:
  - "dirección visual aprobada por el Owner"
  - "sistema de diseño inicial construible"
  - "dos superficies representativas resueltas"
  - "memoria de diseño completa"
devolucion:
  - "a PRD, cuando el criterio de éxito no permite decidir qué superficie es representativa"
  - "a ENC, cuando el encuadre no distingue entre fundar una dirección y resolver una pantalla"
bloqueo:
  - "el Owner no está disponible para la conversación de visión: sin él no hay visión"
  - "no hay datos reales del producto y toda exploración sería sobre contenido inventado"
cancelacion:
  - "un item DIR posterior cambia el criterio de éxito del producto antes de que se decida la dirección"
aprendizaje:
  - "qué tipo de material hace converger a este Owner se registra en el léxico y en el historial"
  - "los territorios rechazados y su motivo, para no volver a proponerlos"
  - "si una dirección elegida falla en la segunda superficie, se registra qué la delató tarde"
prueba_de_reanudacion: >
  Un agente nuevo abre el paquete, lee el checkpoint, comprueba qué territorios y qué
  direcciones están ya descartados y con qué motivo, y continúa en el paso exacto sin
  volver a proponerlos ni pedir al Owner que repita su reacción. Es la prueba T93.
```
