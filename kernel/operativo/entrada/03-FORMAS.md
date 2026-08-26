# Catálogo de formas de conversación

> Catálogo. Contiene catorce bloques `ads:forma-conversacion`, uno por clase de expresión.
> Lo ejecuta [`ENC/Escucha`](../capacidades/ENC/metodos/Escucha.md) en su paso 3.

Cada forma declara, sin dejar nada al criterio del momento: **qué resuelve sola · qué
pregunta · cuándo muestra referencias · cuándo hace brainstorming · cuándo consulta a un
especialista · cuándo necesita confirmación · cuándo crea item · qué checkpoint guarda.**

---

## 1 · Orden clara y reversible

```yaml ads:forma-conversacion
id: forma:orden-clara
nombre: Orden clara y reversible
reconoce_por:
  - "el objetivo es un item o paquete que ya existe"
  - "la intención está en el catálogo de b.13 y es unívoca"
  - "deshacerla devuelve el sistema al estado anterior sin pérdida"
entrada_tipica:
  - "«esto es lo primero ahora»"
  - "«aparca lo del stock, céntrate en la pantalla de entradas»"
  - "«retoma lo del gap»"
resuelve_autonomamente:
  - "anclar el objetivo con el índice de lo existente"
  - "emitir el evento con atribución completa y aplicarlo"
  - "informar en una línea de lo aplicado"
preguntas:
  - "ninguna, salvo que el anclaje deje dos candidatos por encima del margen: entonces se desambigua por nombre humano"
muestra_referencias: "no muestra referencias: no hay nada que explorar"
brainstorming: "no procede"
consulta_especialista: "no consulta: una orden no es contenido"
confirmacion: "no se pide. Pedirla convierte al Owner en un botón de OK"
crea_item: "no crea item. Produce un evento sobre lo que ya existe"
checkpoint: "candidatos puntuados y evento emitido, para que un relevo sepa si llegó a aplicarse"
salida:
  - "evento de orden aplicado"
  - "confirmación de una línea al Owner"
error_tipico: >
  Preguntar «¿seguro que quieres aparcarlo?» ante una orden reversible. El Owner ya lo
  dijo; volver a preguntarlo no añade seguridad, añade fricción.
```

---

## 2 · Error evidente

```yaml ads:forma-conversacion
id: forma:error-evidente
nombre: Error evidente
reconoce_por:
  - "el Owner describe algo que no funciona, y el comportamiento correcto está especificado o es obvio"
  - "no hay decisión de producto que tomar: nadie tiene que elegir qué debería pasar"
entrada_tipica:
  - "«al guardar sale error 500»"
  - "«el total no cuadra, suma mal el IVA»"
  - "«este botón no hace nada»"
resuelve_autonomamente:
  - "capturar la literal y el caso concreto"
  - "anclar contra lo implementado y contra defectos abiertos"
  - "proponer el tipo DEF y entregarlo a DSP sin confirmación"
preguntas:
  - "¿en qué pantalla y con qué dato lo has visto? — sólo si la literal no lo dice"
  - "¿pasa siempre o te ha pasado una vez? — sólo si condiciona la reproducción"
muestra_referencias: "no muestra referencias"
brainstorming: "no procede: no hay nada que explorar, hay algo que reparar"
consulta_especialista: >
  no consulta durante el encuadre. El diagnóstico pertenece a ARQ o a CON dentro de la ruta
  DEF, no a la puerta de entrada
confirmacion: "no se pide: reparar lo que está roto no es una decisión del Owner"
crea_item: "sí, tipo DEF, directamente"
checkpoint: "caso concreto capturado y anclaje contra defectos abiertos"
salida:
  - "encuadre de tipo DEF entregado a DSP"
error_tipico: >
  Convertirlo en investigación. Un error con comportamiento esperado conocido no necesita
  que ENC averigüe la causa: necesita llegar rápido a quien la averigua.
```

---

## 3 · Comentario subjetivo

```yaml ads:forma-conversacion
id: forma:comentario-subjetivo
nombre: Comentario subjetivo
reconoce_por:
  - "el enunciado expresa una valoración, no un hecho comprobable"
  - "usa adjetivos de percepción: básico, plano, sin alma, feo, lento, incómodo, raro"
  - "no dice qué debería pasar en su lugar"
entrada_tipica:
  - "«esta pantalla funciona, pero se ve básica, plana y sin alma»"
  - "«esto se siente lento aunque el número diga que va rápido»"
  - "«no me gusta cómo ha quedado»"
resuelve_autonomamente:
  - "capturar la literal COMPLETA, incluidos los adjetivos, que son el dato"
  - "localizar la superficie concreta a la que se refiere"
  - "anclar contra la memoria de diseño: qué dirección se aprobó para esa superficie"
preguntas:
  - "¿de todo lo que ves ahí, qué es lo primero que te chirría?"
  - "¿hay algún sitio donde hayas visto esto resuelto de una forma que te gustara?"
  - "¿te pasa siempre que entras, o sólo con ciertos datos?"
muestra_referencias: >
  SÍ, siempre. Un comentario subjetivo no se resuelve preguntando más: se resuelve
  enseñando. Se pide a DIS en modo consulta entre dos y cuatro referencias con el
  principio extraído de cada una, y se observa a cuál reacciona
brainstorming: >
  cuando tras ver las referencias el Owner sigue sin reconocer lo que quiere, se abren
  direcciones distintas entre sí, incluidas las que el sistema considera malas, marcadas
consulta_especialista: >
  DIS en modo consulta, SIEMPRE que el comentario sea de forma, percepción o experiencia.
  ENC no interpreta materia de diseño por su cuenta
confirmacion: >
  se pide antes de entregar, porque un comentario subjetivo casi siempre implica primera
  instancia de patrón visual, que es nivel obligatorio en a.8
crea_item: >
  NO directamente. Primero se convierte en un problema formulado. El tipo depende de lo
  que la conversación revele: GAP si la superficie nunca alcanzó una dirección aprobada,
  DEF si la incumple, DIR si el Owner quiere cambiar la dirección aprobada
checkpoint: >
  literal con sus adjetivos, superficie identificada, referencias mostradas y reacción del
  Owner a cada una. Sin la reacción, un relevo repetiría las mismas referencias
salida:
  - "encuadre con el problema de forma formulado, o"
  - "ficha de vivero si el Owner no quiere profundizar ahora"
error_tipico: >
  Traducirlo a una tarea técnica: «cambiar CSS», «añadir sombras», «subir el contraste».
  Es el error central que este catálogo existe para impedir. El adjetivo del Owner es un
  síntoma, no una especificación.
```

---

## 4 · Idea todavía inmadura

```yaml ads:forma-conversacion
id: forma:idea-inmadura
nombre: Idea todavía inmadura
reconoce_por:
  - "falla al menos una de las tres condiciones de la prueba de frontera"
  - "el Owner la enuncia en condicional o con horizonte indeterminado"
entrada_tipica:
  - "«algún día habría que hacer algo con los informes»"
  - "«estaría bien que esto se pudiera compartir»"
resuelve_autonomamente:
  - "abrir o recuperar la ficha del vivero"
  - "registrar qué condición de la prueba falla"
preguntas:
  - "¿qué te haría decir que esto ha quedado bien?"
  - "¿qué pasa hoy que te lleva a pensar en esto?"
  - "¿esto es para ti, o para alguien más?"
muestra_referencias: "sí, cuando la idea es de forma o de experiencia y el Owner no sabe concretarla"
brainstorming: >
  sí, cuando tras las preguntas y las referencias sigue sin poder escribirse el resultado
  perseguido. Es el uso legítimo del brainstorming: reconocer por contraste
consulta_especialista: >
  INV en modo consulta cuando la duda es si algo es posible; DIS cuando es de forma; PRD
  cuando es si encaja con la definición de éxito del proyecto
confirmacion: "no se pide confirmación para dejar algo en el vivero: no compromete nada"
crea_item: "no. Sólo si la conversación la hace pasar la prueba de frontera"
checkpoint: >
  alternativas ya presentadas y reacción del Owner a cada una, para que un relevo no
  vuelva a proponer lo ya rechazado
salida:
  - "ficha de vivero actualizada con qué falta, o"
  - "candidato a trabajo si maduró"
error_tipico: >
  Abrir un item «para no perderla». El vivero existe justamente para no perderla sin
  crear trabajo. Un item sin criterio de terminado envejece en la cola y contamina toda
  medición de estado.
```

---

## 5 · Feature

```yaml ads:forma-conversacion
id: forma:feature
nombre: Feature
reconoce_por:
  - "pide una capacidad o comportamiento que NO existe todavía"
  - "puede escribirse su resultado perseguido y su evidencia de cierre"
entrada_tipica:
  - "«quiero poder exportar el listado a Excel»"
  - "«necesito ver el histórico de cambios de cada pedido»"
resuelve_autonomamente:
  - "anclar contra lo implementado y contra items abiertos"
  - "escribir resultado perseguido, expectativas y evidencia de cierre"
  - "proponer tipo FEA"
preguntas:
  - "¿para quién es esto y en qué momento lo usaría?"
  - "¿qué haría que esto fuera un fracaso aunque funcionara?"
  - "¿qué NO tiene que hacer? — el fuera de alcance ahorra más trabajo que el alcance"
muestra_referencias: "cuando la feature tiene superficie visible y el Owner no tiene formada la expectativa de forma"
brainstorming: "no por defecto: hay una petición concreta. Sí si el fuera de alcance resulta indefinible"
consulta_especialista: >
  DIS en modo consulta si hay superficie visible y no existe patrón aprobado que la cubra;
  ARQ si el Owner condiciona la petición a una restricción técnica que hay que verificar
confirmacion: >
  obligatoria cuando es primera dirección de producto o toca materia reservada, según a.8.
  En una feature que extiende un patrón vigente dentro de su alcance, no se pide
crea_item: "sí, tipo FEA, tras el gate"
checkpoint: "resultado perseguido, fuera de alcance acordado y evidencia de cierre"
salida:
  - "encuadre de tipo FEA entregado a DSP"
error_tipico: >
  Aceptar la solución que el Owner propone sin capturar el problema que la motiva. Si sólo
  se registra «exportar a Excel», nadie sabrá después que lo que necesitaba era enviar el
  listado a su gestoría, y que había maneras mejores.
```

---

## 6 · Gap

```yaml ads:forma-conversacion
id: forma:gap
nombre: Gap
reconoce_por:
  - "algo EXISTE y no llega al nivel esperado"
  - "la distancia es entre lo que se pretendía y lo que hay, no entre lo que hay y lo que no hay"
entrada_tipica:
  - "«esto ya está, pero le falta la mitad de los casos»"
  - "«la búsqueda funciona pero no encuentra por referencia de proveedor»"
resuelve_autonomamente:
  - "anclar sobre LO YA IMPLEMENTADO: qué existe, qué se creía que existía"
  - "escribir la distancia concreta entre lo pretendido y lo real"
  - "proponer tipo GAP"
preguntas:
  - "¿qué esperabas que hiciera y no hace?"
  - "¿cuándo te diste cuenta?"
  - "¿esto lo hemos hablado antes? — se comprueba en memoria antes de preguntarlo"
muestra_referencias: "sólo si el gap es de forma o de calidad percibida"
brainstorming: "no procede: la expectativa ya existe, hay que reconciliarla"
consulta_especialista: >
  la capacidad propietaria de la capa que se quedó corta, en modo consulta, para saber si
  el hueco fue decisión consciente o accidente
confirmacion: "no se pide si la expectativa estaba escrita. Sí, si el gap la amplía"
crea_item: "sí, tipo GAP, tras el gate"
checkpoint: "la distancia escrita y el resultado del anclaje sobre lo ya implementado"
salida:
  - "encuadre de tipo GAP entregado a DSP"
error_tipico: >
  Tratarlo como feature. Un GAP arrastra la pregunta más valiosa del sistema —por qué
  apareció el hueco— y si se encuadra como FEA, ese aprendizaje se pierde.
```

---

## 7 · Cambio de dirección

```yaml ads:forma-conversacion
id: forma:cambio-de-direccion
nombre: Cambio de dirección
reconoce_por:
  - "contradice una decisión que el Owner ya tomó y que está implementada o en curso"
  - "no es un matiz: sustituye el criterio, no el resultado"
entrada_tipica:
  - "«ya no quiero que la app funcione sin conexión, olvidemos eso»"
  - "«esto lo habíamos hecho por proveedor y quiero que sea por almacén»"
resuelve_autonomamente:
  - "localizar la decisión anterior y mostrarla junto a la nueva expresión"
  - "identificar qué decisiones concretas pretende sustituir"
preguntas:
  - "esto sustituye a <decisión anterior, con sus palabras de entonces>. ¿Lo sustituye o convive?"
  - "¿qué te ha hecho cambiar de criterio? — el motivo es lo que hereda el registro de la nueva dirección"
  - "¿qué tiene que seguir siendo verdad después del cambio?"
muestra_referencias: "cuando el cambio es de dirección visual o de experiencia"
brainstorming: "no: hay una dirección propuesta. La exploración pertenece al proceso DIR, con sus capacidades"
consulta_especialista: >
  ARQ en modo consulta para una estimación previa del radio de impacto. Se declara
  expresamente como orientativa: el radio MEDIDO pertenece a la ruta DIR
confirmacion: "obligatoria siempre. Es nivel obligatorio en a.8 sin excepción"
crea_item: >
  sí, tipo DIR. ENC NO elige su propietario global: eso lo resuelve la regla de b.16 sobre
  las decisiones concretas que se sustituyen
checkpoint: "decisión anterior localizada, motivo del cambio en palabras del Owner, decisiones que se pretenden sustituir"
salida:
  - "encuadre de tipo DIR entregado a DSP"
error_tipico: >
  Aplicarlo como si fuera una feature nueva y dejar la decisión anterior viva. El sistema
  acaba con dos criterios vigentes y contradictorios, que es el modo de fallo (a).
```

---

## 8 · Problema de diseño

```yaml ads:forma-conversacion
id: forma:problema-de-diseno
nombre: Problema de diseño
reconoce_por:
  - "el problema está en la forma, la experiencia o la comprensión, no en el comportamiento"
  - "el sistema hace lo que debe y aun así el resultado no sirve o no convence"
entrada_tipica:
  - "«hace lo que tiene que hacer pero no se entiende nada»"
  - "«hay tanta información que no sé dónde mirar»"
resuelve_autonomamente:
  - "identificar la superficie y su dirección aprobada, si la tiene"
  - "distinguir tres casos: no hay patrón · lo hay y se incumple · lo hay y no cubre este caso"
preguntas:
  - "¿qué estabas intentando hacer cuando te pasó?"
  - "¿qué esperabas ver primero al entrar?"
  - "¿te ha pasado con pocos datos o con muchos?"
muestra_referencias: "sí, siempre: el problema es de forma y la forma se enseña"
brainstorming: "cuando no existe patrón aprobado para esa superficie y hay que abrir direcciones"
consulta_especialista: "DIS en modo consulta, obligatoriamente, antes de formular el problema"
confirmacion: >
  obligatoria si implica primera instancia de un patrón visual o de interacción; no, si el
  caso está cubierto por un patrón vigente y sólo se ha incumplido
crea_item: >
  sí, y el tipo depende del caso: GAP si la superficie nunca alcanzó dirección aprobada,
  DEF si la incumple, DIR si el Owner quiere cambiar la dirección
checkpoint: "superficie, patrón aplicable y cuál de los tres casos es"
salida:
  - "encuadre con el problema de diseño formulado, del tipo que corresponda"
error_tipico: >
  Encuadrarlo como problema de rendimiento o de datos porque es más fácil de escribir. Lo
  que no se entiende no se arregla haciéndolo más rápido.
```

---

## 9 · Investigación

```yaml ads:forma-conversacion
id: forma:investigacion
nombre: Investigación
reconoce_por:
  - "lo que se persigue es CONOCIMIENTO, no software productivo"
  - "hay una decisión esperando y falta evidencia para tomarla"
entrada_tipica:
  - "«¿esto se puede hacer con lo que tenemos?»"
  - "«averigua si merece la pena cambiar de librería»"
resuelve_autonomamente:
  - "escribir la pregunta que la investigación debe responder"
  - "identificar qué decisión concreta consumirá la respuesta"
  - "proponer tipo INV"
preguntas:
  - "¿qué vas a decidir con la respuesta?"
  - "¿qué respuesta te haría cambiar de plan?"
  - "¿para cuándo la necesitas para que te sirva?"
muestra_referencias: "no por defecto; sí cuando la pregunta es sobre cómo lo resuelven otros"
brainstorming: "no: acotar la pregunta es lo contrario de abrirla"
consulta_especialista: "INV en modo consulta para acotar la pregunta y estimar si es respondible"
confirmacion: "no se pide si el destino de la respuesta está claro. Sí, si la investigación consumiría trabajo de varios equipos"
crea_item: "sí, tipo INV, con la pregunta y el consumidor de la respuesta escritos"
checkpoint: "pregunta acotada y decisión que la consumirá"
salida:
  - "encuadre de tipo INV entregado a DSP"
error_tipico: >
  Encuadrar una investigación sin decir qué se va a decidir con ella. Produce conocimiento
  que nadie consume y alimenta el modo de fallo de autorreferencia sin producto.
```

---

## 10 · Decisión del Owner

```yaml ads:forma-conversacion
id: forma:decision
nombre: Decisión del Owner
reconoce_por:
  - "responde a una pregunta abierta registrada, o el Owner declara que decide algo"
  - "la materia pertenece a su autoridad"
entrada_tipica:
  - "«prefiero perder densidad antes que truncar nombres»"
  - "«nos quedamos con la segunda opción»"
resuelve_autonomamente:
  - "registrar la decisión con sus palabras literales en la memoria de la capacidad propietaria"
  - "localizar qué checkpoints la incluyen en su based_on y marcarlos para revalidar"
  - "localizar si sustituye a una decisión anterior"
preguntas:
  - "¿esto vale sólo para esta pantalla, o es una regla general? — determina el alcance del patrón"
  - "¿hasta cuándo vale? — determina la condición de caducidad"
muestra_referencias: "no: la decisión ya está tomada"
brainstorming: "no procede"
consulta_especialista: "la capacidad propietaria de la materia, para que registre la decisión en su memoria con el alcance correcto"
confirmacion: >
  no se pide confirmación de la decisión, se acaba de tomar. Sí se devuelve escrita para
  que el Owner vea con qué alcance ha quedado registrada
crea_item: >
  no crea item por sí misma. Crea items derivados cuando sustituye a una decisión ya
  implementada: entonces continúa como proceso DIR
checkpoint: "decisión literal, alcance, caducidad y checkpoints marcados para revalidar"
salida:
  - "registro de decisión con clase de patrón, alcance y caducidad"
  - "encuadre DIR si sustituye a algo implementado"
error_tipico: >
  Registrar la decisión sin alcance ni caducidad. Seis semanas después nadie sabe si valía
  para una pantalla o para todo el producto, y se vuelve a decidir distinto.
```

---

## 11 · Feedback sobre una implementación

```yaml ads:forma-conversacion
id: forma:feedback
nombre: Feedback sobre una implementación
reconoce_por:
  - "se refiere a algo que se acaba de entregar o desplegar"
  - "hay un item cerrado o en entrega al que apunta"
entrada_tipica:
  - "«ya lo he probado; la lista va bien pero la animación al abrir da tirones»"
  - "«esto no es lo que había pedido»"
resuelve_autonomamente:
  - "localizar el item que lo produjo y su evidencia de cierre"
  - "comparar lo dicho contra la intención aprobada de ese item"
  - "clasificar en tres: cumple y no gusta · no cumple · cumple y revela expectativa nueva"
preguntas:
  - "¿en qué dispositivo o navegador lo has visto?"
  - "¿te refieres a esto de aquí? — mostrando la evidencia de cierre que se aceptó"
muestra_referencias: "cuando el feedback es de forma y hay que comparar con la intención aprobada"
brainstorming: "no por defecto: hay algo construido que evaluar"
consulta_especialista: >
  VER en modo consulta para contrastar contra la evidencia recogida; DIS cuando el
  feedback es de forma o movimiento
confirmacion: >
  no se pide para clasificar. Sí, cuando el feedback revela una expectativa nueva: eso es
  ampliación de alcance y es del Owner
crea_item: >
  depende de la clasificación: DEF si no cumple lo aprobado, GAP si cumple y revela que la
  expectativa era mayor, DIR si el Owner cambia de criterio sobre lo aprobado, ninguno si
  cumple y el comentario es una preferencia sin consecuencia
checkpoint: "item de origen localizado, comparación con la intención aprobada y clasificación de los tres casos"
salida:
  - "encuadre del tipo que corresponda, o anotación sin item"
error_tipico: >
  Reabrir el item cerrado. Un item cerrado no se reabre: nace uno nuevo enlazado. Reabrir
  destruye la trazabilidad de qué se entregó y cuándo.
```

---

## 12 · Frase que hace referencia a algo anterior

```yaml ads:forma-conversacion
id: forma:referencia-anterior
nombre: Frase que hace referencia a algo anterior
reconoce_por:
  - "usa deícticos sin antecedente en el mensaje: «eso», «lo de antes», «lo que hablamos»"
  - "presupone un contexto que no está en la expresión"
entrada_tipica:
  - "«eso que te dije de los lotes, ¿cómo va?»"
  - "«mételo también en lo otro»"
resuelve_autonomamente:
  - "resolver el antecedente contra el estado, la memoria de conversaciones y el léxico del Owner"
  - "puntuar candidatos y quedarse con los dos mejores"
preguntas:
  - "sólo si la distancia entre los dos mejores candidatos no supera el margen declarado: se presentan por nombre humano, naturaleza y estado, nunca por identificador"
muestra_referencias: "no muestra referencias: el trabajo es resolver un antecedente, no explorar una forma"
brainstorming: "no procede"
consulta_especialista: "no consulta: resolver el antecedente es trabajo de memoria, no de materia"
confirmacion: "sólo la desambiguación, y sólo cuando el margen no se supera"
crea_item: "no por sí misma: una vez resuelto el antecedente, se aplica la forma que corresponda a la expresión"
checkpoint: "antecedente resuelto y con qué puntuación, para que un relevo no vuelva a resolverlo"
salida:
  - "la expresión reencuadrada con su antecedente resuelto"
error_tipico: >
  Preguntar «¿a qué te refieres?» sin haber intentado resolverlo. El Owner ya lo dijo una
  vez; que el sistema no lo recuerde es precisamente el problema que existe para eliminar.
```

---

## 13 · «Continúa»

```yaml ads:forma-conversacion
id: forma:continua
nombre: Continúa
reconoce_por:
  - "el Owner pide seguir sin decir con qué"
  - "no aporta contenido nuevo"
entrada_tipica:
  - "«continúa»"
  - "«sigue»"
  - "«retoma lo del gap»"
resuelve_autonomamente:
  - "TODO: es la función Estado de DSP, no un encuadre"
  - "ENC se limita a reconocer la intención y pasar el control a DSP"
preguntas:
  - "ninguna. Los pasos 1 a 4 de b.14 son deterministas y no requieren al Owner"
muestra_referencias: "no muestra referencias: no hay nada que encuadrar"
brainstorming: "no procede"
consulta_especialista: "no consulta a nadie: el control pasa entero a DSP"
confirmacion: "no se pide permiso para continuar: eso es lo que el Owner acaba de pedir"
crea_item: "no crea item"
checkpoint: "ninguno propio: el checkpoint que importa es el del paquete que se retoma"
salida:
  - "control transferido a DSP, que reconstruye, verifica, consume órdenes, selecciona y reporta en pocas líneas"
error_tipico: >
  Responder con un resumen del proyecto en lugar de retomar el trabajo. «Continúa» significa
  trabajar, no informar; el informe son las pocas líneas del paso 5 de b.14.
```

---

## 14 · Interrupción del chat antes de terminar

```yaml ads:forma-conversacion
id: forma:interrupcion
nombre: Interrupción del chat antes de terminar
reconoce_por:
  - "una conversación anterior quedó abierta sin encuadre entregado"
  - "existe checkpoint con pregunta_pendiente sin respuesta"
entrada_tipica:
  - "el Owner vuelve días después y escribe algo distinto"
  - "el Owner vuelve y responde a la pregunta pendiente sin repetir el contexto"
resuelve_autonomamente:
  - "cargar el checkpoint del encuadre abierto antes de procesar el mensaje nuevo"
  - "comprobar based_on: si las fuentes cambiaron, marcar freshness y revalidar sólo la parte afectada"
  - "decidir si el mensaje nuevo responde a la pregunta pendiente o abre otra cosa"
preguntas:
  - "ninguna sobre lo ya conversado. Se recuerda lo entendido en una línea y se sigue desde ahí"
muestra_referencias: "las que ya se mostraron NO se repiten: están en el checkpoint con la reacción del Owner"
brainstorming: "sólo si la conversación se cortó en mitad de uno, y entonces se retoma con las opciones ya descartadas marcadas"
consulta_especialista: "las consultas ya respondidas no se repiten: se recargan del paquete"
confirmacion: "no se pide confirmación para retomar"
crea_item: "según la forma que estuviera en curso cuando se cortó"
checkpoint: >
  se actualiza al reanudar con freshness y con qué parte se revalidó. Un checkpoint que no
  registra la reanudación hace indistinguible el trabajo continuado del reiniciado
salida:
  - "la conversación continúa desde su paso exacto"
error_tipico: >
  Empezar de cero y volver a preguntar lo ya contestado. Es el fallo que el Owner nombró
  explícitamente: reescribir cada sesión cómo guiar la conversación.
```

---

## Cómo se elige la forma

```text
1  ¿la expresión apunta a un item o paquete existente?
       intención de gobierno       → forma:orden-clara
       deíctico sin antecedente    → forma:referencia-anterior
       comenta algo entregado      → forma:feedback
       pide seguir                 → forma:continua
2  ¿hay una conversación abierta con checkpoint sin cerrar?     → forma:interrupcion
3  ¿el Owner decide algo de su autoridad?                       → forma:decision
4  ¿contradice una decisión suya vigente e implementada?        → forma:cambio-de-direccion
5  ¿describe un hecho roto con comportamiento esperado conocido? → forma:error-evidente
6  ¿es una valoración con adjetivos de percepción?              → forma:comentario-subjetivo
7  ¿el problema es de comprensión, forma o experiencia?         → forma:problema-de-diseno
8  ¿persigue conocimiento para decidir?                         → forma:investigacion
9  ¿existe algo que no llega al nivel esperado?                 → forma:gap
10 ¿pide algo que no existe todavía?                            → forma:feature
11 en otro caso                                                 → forma:idea-inmadura
```

**El orden importa.** Se evalúa de arriba abajo y gana la primera que se cumple. Dos
formas nunca se aplican a la vez sobre la misma expresión; si una expresión contiene dos
cosas —«esto va lento y además quiero exportar a Excel»— **se parte en dos expresiones**,
cada una con su literal citada del mismo mensaje.
