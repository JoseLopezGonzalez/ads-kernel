# La entrada todavía no es un item

> Catálogo. Contiene varios bloques `ads:entrada`, uno por clase de expresión.

Una frase del Owner **no es** una tarea. Entre lo que dice y lo que el sistema fabrica hay
nueve cosas distintas, y confundirlas produce las dos patologías simétricas:

```text
BUROCRACIA      cada comentario se convierte en item, y la cola se llena de trabajo
                que el Owner no pidió
PÉRDIDA         una intención real se queda en la conversación, se olvida, y el Owner
                tiene que volver a explicarla
```

## Dos reglas duras sobre la expresión del Owner

```text
1  LA EXPRESIÓN LITERAL SE CONSERVA SIEMPRE, con fecha y canal, en el encuadre.
   La interpretación profesional se añade AL LADO. Nunca la sustituye ni la corrige.

2  NINGUNA CLASE DE ENTRADA CREA TRABAJO POR SÍ MISMA salvo las tres que lo declaran
   explícitamente abajo. El resto se registra, se ancla y espera.
```

## Las nueve clases

```text
                       ¿se conserva?  ¿genera trabajo?  ¿necesita al Owner otra vez?
expresión original          sí            no                    —
interpretación              sí            no                 sólo si es dudosa
observación                 sí            no                    no
nota                        sí            no                    no
idea inmadura               sí            no                 cuando él vuelva a ella
candidato a trabajo         sí            tras confirmar        sí
orden sobre item existente  sí            sí                    no
decisión                    sí            sí (registro)         no
item formal                 sí            sí                    no
```

---

## expresión original

```yaml ads:entrada
id: entrada:expresion-original
nombre: Expresión original del Owner
que_es: >
  Las palabras exactas que el Owner dijo o escribió, con su fecha y su canal. Es el único
  material que el sistema no puede reconstruir ni mejorar: todo lo demás se deriva de ella.
no_es: >
  No es una interpretación, ni un resumen, ni una versión corregida en lenguaje profesional.
senales:
  - "existe cualquier mensaje del Owner dirigido al sistema"
produce:
  - "una entrada literal en expresion_literal[] del encuadre, con fecha y canal"
crea_item: nunca
conserva:
  - "el texto exacto, sin corregir ortografía, orden ni tono"
  - "la fecha y el canal"
  - "el enlace al encuadre que la interpreta, cuando exista"
siguiente: "se interpreta; la literal permanece intacta para siempre"
```

**Antipatrón característico:** *«He entendido que quieres X»* sustituyendo a lo que el
Owner dijo. El sistema pierde entonces el matiz que motivó todo el trabajo — y el Owner,
al releerlo dos meses después, no reconoce su propia idea.

---

## interpretación

```yaml ads:entrada
id: entrada:interpretacion
nombre: Interpretación profesional
que_es: >
  La lectura que el sistema hace de la expresión original: qué problema parece haber
  detrás, qué resultado parece perseguirse, y con qué grado de confianza.
no_es: >
  No es una decisión ni un compromiso. No autoriza a construir nada.
senales:
  - "existe una expresión original sin interpretar"
  - "una interpretación anterior dejó de encajar con lo que el Owner añadió después"
produce:
  - "el campo interpretacion del encuadre"
  - "el grado de incertidumbre y sus ejes"
crea_item: nunca
conserva:
  - "la interpretación anterior cuando cambia, con el motivo del cambio"
  - "el enlace a la expresión literal de la que deriva"
siguiente: "se contrasta con el anclaje y con el Owner cuando la incertidumbre es alta"
```

---

## observación

```yaml ads:entrada
id: entrada:observacion
nombre: Observación
que_es: >
  Un hecho comprobable que el Owner señala sobre el producto o sobre el trabajo, sin pedir
  nada: «la lista tarda en cargar», «esto ya no se usa».
no_es: >
  No es una queja subjetiva ni una petición. No lleva implícita una preferencia.
senales:
  - "el enunciado describe un hecho verificable"
  - "no contiene petición, preferencia ni valoración"
produce:
  - "una anotación en la memoria de ENC, enlazada al elemento observado"
  - "cero o más candidatos a trabajo, cuando el hecho contradice algo aprobado"
crea_item: nunca
conserva:
  - "el hecho tal como se enunció"
  - "el elemento del producto al que se refiere"
  - "si fue verificado, por quién y con qué evidencia"
siguiente: "se verifica; si contradice algo aprobado, se propone como candidato a trabajo"
```

---

## nota

```yaml ads:entrada
id: entrada:nota
nombre: Nota
que_es: >
  Información que el Owner quiere que el sistema recuerde, sin que implique trabajo:
  un contexto de negocio, una fecha, una restricción externa, una preferencia general.
no_es: >
  No es una orden ni un requisito de un item concreto.
senales:
  - "el enunciado aporta contexto y no describe un resultado a producir"
  - "el Owner usa formas como «para que lo sepas», «ten en cuenta que», «recuerda que»"
produce:
  - "una entrada en la memoria de la capacidad competente en esa materia"
crea_item: nunca
conserva:
  - "el texto literal"
  - "la capacidad a cuya memoria se incorporó"
  - "la fecha, porque una nota de contexto caduca"
siguiente: "se enruta a la memoria del equipo competente y se confirma dónde quedó"
```

---

## idea inmadura

```yaml ads:entrada
id: entrada:idea-inmadura
nombre: Idea inmadura
que_es: >
  Una dirección que al Owner le interesa pero que todavía no tiene resultado perseguido,
  problema definido ni criterio de terminado. «Algún día habría que hacer algo con X.»
no_es: >
  No es un candidato a trabajo. Convertirla en item es la forma más rápida de llenar la
  cola de trabajo que nadie pidió y que nadie sabe cuándo está terminado.
senales:
  - "no puede escribirse su evidencia de cierre sin inventarla"
  - "el Owner la enuncia en condicional o con horizonte indeterminado"
  - "la incertidumbre es alta en el eje «qué resultado se persigue»"
produce:
  - "una ficha en el vivero de ideas de ENC, con lo que falta para madurarla"
crea_item: nunca
conserva:
  - "la expresión literal"
  - "qué falta exactamente para que deje de ser inmadura"
  - "toda conversación posterior sobre ella, acumulada en la misma ficha"
siguiente: >
  espera en el vivero. El sistema NO propone retomarla por antigüedad; la lista cuando el
  Owner pregunta por ella o cuando otro trabajo la vuelve relevante, diciendo por qué
```

**El vivero no es una cola.** Nadie trabaja en él y nadie lo prioriza. Es memoria.

---

## candidato a trabajo

```yaml ads:entrada
id: entrada:candidato
nombre: Candidato a trabajo
que_es: >
  Una intención con resultado perseguido identificable y evidencia de cierre escribible,
  que todavía no ha sido confirmada como item por quien tiene autoridad para hacerlo.
no_es: >
  No es un item. Mientras es candidato no tiene ruta, ni paquetes, ni consume capacidad.
senales:
  - "puede escribirse su resultado perseguido en una frase"
  - "puede escribirse al menos una evidencia de cierre comprobable"
  - "el anclaje ha comprobado que no duplica un item abierto"
produce:
  - "un encuadre en estado listo-para-dsp"
crea_item: tras-confirmacion
condicion_de_item: >
  se confirma con el Owner cuando el nivel de intervención calculado es obligatorio segun
  a.8, o cuando la incertidumbre declarada es alta. En los demás casos ENC lo entrega a DSP
  sin preguntar, y el Owner lo ve en el informe de creación.
conserva:
  - "la expresión literal y toda la conversación que lo maduró"
  - "las alternativas descartadas durante la conversación y por qué"
siguiente: "se entrega a DSP, que crea el item, compone la ruta y crea los paquetes"
```

---

## orden sobre un item existente

```yaml ads:entrada
id: entrada:orden
nombre: Orden sobre un item existente
que_es: >
  Una instrucción del Owner que cambia el gobierno de algo que ya existe: prioridad,
  aparcado, retomar, cancelar, recomponer, o continuar.
no_es: >
  No es contenido. Una orden nunca decide qué contiene una capa: eso pertenece a la
  capacidad competente.
senales:
  - "el objetivo de la frase es un item o paquete que ya existe"
  - "la intención está en el catálogo de b.13"
produce:
  - "un evento con atribución completa: autoridad Owner, ordenante Owner, ejecutor DSP"
crea_item: nunca
conserva:
  - "la frase literal como texto del comando"
  - "la base sobre la que se emitió, para detectar que dejó de ser vigente"
siguiente: "se ancla, se clasifica como unívoca o ambigua, y se aplica por el pipeline de b.13"
```

---

## decisión

```yaml ads:entrada
id: entrada:decision
nombre: Decisión del Owner
que_es: >
  Una elección en materia de su autoridad: dirección de producto, forma visual o de
  interacción, materia reservada, o resolución de un desacuerdo escalado.
no_es: >
  No es una preferencia comentada al pasar. Una decisión cierra una pregunta abierta y
  sustituye a lo que hubiera decidido antes.
senales:
  - "existe una pregunta abierta registrada a la que responde"
  - "o el Owner declara explícitamente que decide algo"
produce:
  - "un registro de decisión en la memoria de la capacidad propietaria de esa materia"
  - "la actualización de todo checkpoint cuyo based_on la incluya"
  - "cero o más items derivados cuando la decisión sustituye a una anterior"
crea_item: condicional
condicion_de_item: >
  crea items derivados cuando la decisión sustituye a una decisión ya implementada; en ese
  caso el proceso es DIR y la regla de propietario global de b.16 decide quién responde
conserva:
  - "la formulación literal de la decisión"
  - "qué decisión anterior sustituye, si alguna"
  - "las alternativas que estaban sobre la mesa cuando decidió"
siguiente: "se registra, se propaga a los checkpoints afectados y se comprueba su radio"
```

**Una decisión no comentada se pierde.** Es la fuente de la patología que el Owner
describió: la misma decisión tomada dos veces con resultado distinto (modo de fallo (a)).

---

## item formal

```yaml ads:entrada
id: entrada:item
nombre: Item formal
que_es: >
  La unidad de trabajo con identidad persistente, encuadre, proceso, ruta y paquetes.
  Es lo único que consume capacidad de los equipos.
no_es: >
  No es la meta de toda conversación. La mayoría de las expresiones del Owner terminan
  legítimamente sin item.
senales:
  - "DSP ha creado su ficha a partir de un encuadre en estado listo-para-dsp"
produce:
  - "ficha, ruta r1 y paquetes en estado propuesto"
crea_item: directamente
conserva:
  - "el enlace al encuadre completo, y a través de él a la expresión literal"
siguiente: "recorre lo que (b) define; ENC deja de tener custodia sobre él"
```

---

## Frontera entre idea inmadura y candidato — prueba escrita

Es la frontera que más burocracia genera si se decide por intuición. Se decide así:

```text
Un enunciado es CANDIDATO si y sólo si se cumplen las tres:

  [ ] puede escribirse su RESULTADO PERSEGUIDO en una frase, sin usar «mejorar»,
      «optimizar» ni «revisar» como único verbo
  [ ] puede escribirse al menos UNA EVIDENCIA DE CIERRE comprobable por alguien
      distinto de quien la escribió
  [ ] el ANCLAJE ha terminado: se sabe qué existe ya, qué decisiones lo gobiernan
      y si duplica algo abierto

Si falla cualquiera → IDEA INMADURA, y lo que falla es exactamente lo que hay que
madurar. Se escribe en la ficha del vivero.
```

La frase del escenario de referencia —*«Esta pantalla funciona, pero se ve básica, plana y
sin alma»*— **falla las tres** en el momento de decirse. El recorrido completo hasta
convertirla en item correcto está en
[`05-ESCENARIOS.md`](05-ESCENARIOS.md).
