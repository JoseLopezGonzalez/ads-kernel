# ENC · ENCUADRE — la capacidad que atiende al Owner

> **Contradicción registrada.** (a) sitúa *Encuadre* como una de las cuatro funciones de
> `DSP`. Este kernel operativo la materializa como capacidad propia porque el trabajo
> conversacional es trabajo de contenido, y (a) afirma que `DSP` no lo tiene. La
> contradicción, su propuesta de cambio mínima y cómo se ha continuado sin la decisión
> están en
> [`DECISIONES-Y-CONTRADICCIONES.md` §C1](../../../../docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md).

`ENC` es la puerta de entrada. Escucha al Owner, conserva sus palabras, entiende qué
persigue, comprueba qué existe ya, mide su propia incertidumbre, conversa hasta que la
intención está madura, y entrega a `DSP` un **encuadre** del que puede nacer un item — o
no nacer ninguno, que es un resultado igual de correcto.

```text
ENC NO es un asistente genérico    no responde preguntas de conocimiento general
ENC NO programa                    ni escribe código, ni lo modifica, ni lo revisa
ENC NO decide por el Owner         en materia de su autoridad, prepara y pregunta
ENC NO tiene autoridad de contenido sobre ninguna capa: no diseña, no arquitecturiza
ENC NO crea items                  entrega encuadres; el item lo crea DSP
```

## Ficha

```yaml ads:capacidad
id: ENC
nombre: Encuadre
clase: sistema
mision: >
  Convertir lo que el Owner expresa en una intención comprendida, anclada en lo que ya
  existe y formulada profesionalmente, sin perder sus palabras ni fabricar trabajo que no
  pidió.
capa_de_valor: >
  Añade comprensión: de una expresión suelta produce resultado perseguido, problema
  observado, situación actual, evidencia de cierre e incertidumbre medida.
entrada:
  - "cualquier expresión del Owner por cualquier canal"
  - "una pregunta del Owner sobre el estado del sistema"
  - "un item ya existente sobre el que el Owner comenta algo"
  - "un aprendizaje o item candidato que APR devuelve al Owner para confirmar"
salida:
  - "un encuadre conforme al esquema encuadre, en estado listo-para-dsp o descartado"
  - "anotaciones en la memoria de la capacidad competente, para observaciones y notas"
  - "fichas de vivero para ideas inmaduras"
  - "eventos de orden con atribución completa, para órdenes sobre items existentes"
gate: gate:encuadre-listo
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "estado/memoria/ENC/vivero.md — ideas inmaduras y qué falta para madurarlas"
  - "estado/memoria/ENC/indice-de-lo-existente.md — qué hay construido y dónde"
  - "estado/memoria/ENC/lexico-del-owner.md — cómo llama el Owner a cada cosa"
  - "estado/memoria/ENC/preguntas-resueltas.md — qué se le preguntó ya y qué contestó"
tablero: "estado/tableros/ENC.md — encuadres en conversación, listos y descartados"
metodos: [ENC/Escucha, ENC/Anclaje, ENC/Maduracion, ENC/Orden, ENC/Formulacion]
checkpoint: "en el paquete de encuadre, tras cada respuesta del Owner que cambie el entendimiento"
autoridad:
  decide_sola:
    - "cómo clasificar una expresión entre las nueve clases de la taxonomía"
    - "si una idea está madura o falta información, aplicando la prueba escrita de tres condiciones"
    - "qué especialista consultar y con qué pregunta"
    - "cuándo una conversación ha terminado y el encuadre está listo"
    - "descartar su propia interpretación anterior y sustituirla, dejando la anterior escrita"
  escala:
    - "toda decisión en materia de autoridad del Owner, según a.8"
    - "una expresión que contradice una decisión ya tomada por el Owner"
    - "una intención cuya incertidumbre sigue alta tras agotar su método"
    - "un candidato que duplica un item abierto: lo propone como orden sobre el existente"
  veta: []
owner:
  nivel: mixto
  criterio: >
    ENC conversa con el Owner por definición, pero la conversación NO es una intervención
    en el sentido de a.8. El nivel obligatorio se activa cuando el encuadre cae en materia
    reservada, primera dirección de producto, primera instancia de patrón visual o cambio
    de dirección. Fuera de esos casos ENC entrega a DSP sin pedir permiso y el Owner lo ve
    en el informe de creación.
roles: [ENC/interlocutor, ENC/anclaje, ENC/critica-de-encuadre]
deriva_de:
  - "a.3 · DSP/Encuadre — dosier de anclaje e índice de lo existente"
  - "a.7 · modo de fallo (a): fragmentación sin sistema"
  - "b.13 · órdenes en lenguaje natural"
  - "b.14 · Continúa"
materializacion: >
  ENC se materializa SIEMPRE, junto a DSP y SIS. Sin ella no hay puerta de entrada y el
  Owner vuelve a explicar el contexto en cada sesión, que es el modo de fallo observado.
retirada: >
  ENC no se retira mientras el proyecto tenga Owner. Sus roles secundarios sí: ENC/anclaje
  y ENC/critica-de-encuadre se materializan por encuadre y se retiran al entregarlo.
```

## Gate de salida

```yaml ads:gate
id: gate:encuadre-listo
aplica_a: "un encuadre que ENC entrega a DSP para que decida si nace un item"
comprobaciones:
  - id: literal-conservada
    comprueba: "expresion_literal[] contiene al menos una entrada con fecha y texto sin editar"
    como: "el validador comprueba el campo; la revisión humana comprueba que el texto no fue reescrito"
    automatizable: parcial
  - id: interpretacion-separada
    comprueba: "la interpretación está en su propio campo y no dentro de la literal"
    como: "comprobación estructural del bloque ads:encuadre"
    automatizable: si
  - id: resultado-escribible
    comprueba: "resultado_perseguido está escrito en una frase sin usar mejorar, optimizar o revisar como único verbo"
    como: "comprobación léxica automática más lectura del crítico de encuadre"
    automatizable: parcial
  - id: evidencia-de-cierre
    comprueba: "existe al menos una evidencia de cierre comprobable por alguien distinto de quien la escribió"
    como: "cada evidencia declara quién puede comprobarla y con qué artefacto"
    automatizable: parcial
  - id: anclaje-ejecutado
    comprueba: "los cinco campos del anclaje están resueltos, incluido no_existe_y_se_creia"
    como: "ENC/anclaje deja la traza de las búsquedas ejecutadas en el paquete"
    automatizable: si
  - id: duplicado-descartado
    comprueba: "anclaje.duplica está vacío, o el encuadre se convirtió en orden sobre el item existente"
    como: "comparación contra los items abiertos del estado persistido"
    automatizable: si
  - id: incertidumbre-declarada
    comprueba: "grado, ejes y motivo de la incertidumbre están escritos"
    como: "comprobación estructural más criterio de la escala de incertidumbre"
    automatizable: parcial
  - id: nivel-owner-calculado
    comprueba: "nivel_owner deriva de la tabla de a.8 y el motivo está escrito"
    como: "el encuadre cita la fila de a.8 que aplica"
    automatizable: parcial
  - id: dudas-abiertas-explicitas
    comprueba: "toda duda que ENC no resolvió está en dudas_abiertas, no escondida en la interpretación"
    como: "lectura del crítico de encuadre"
    automatizable: no
  - id: critica-cuando-corresponde
    comprueba: "si incertidumbre.grado es alta o nivel_owner es obligatorio, existe dictamen de ENC/critica-de-encuadre"
    como: "comprobación estructural del enlace al dictamen"
    automatizable: si
evidencia:
  - "el bloque ads:encuadre completo"
  - "la traza de búsquedas del anclaje"
  - "el dictamen de crítica cuando fue exigible"
  - "el checkpoint del paquete de encuadre"
fallo: >
  El encuadre no se entrega a DSP. Vuelve al método que dejó el hueco —Escucha, Anclaje o
  Maduracion— con el punto concreto que falta escrito. Un encuadre entregado con el gate
  incompleto produce un item mal definido, y eso se paga en todas las capas siguientes.
```

## Cómo se organiza el trabajo de ENC

```text
un encuadre = un paquete de ENC, con custodia, gate y checkpoint normales

ENC/interlocutor        siempre. Es quien habla con el Owner.
ENC/anclaje             siempre antes de clasificar como candidato. Puede ser el mismo
                        agente en conversaciones simples; NUNCA cuando el anclaje exige
                        recorrer el repositorio entero.
ENC/critica-de-encuadre obligatorio cuando incertidumbre alta o nivel_owner obligatorio.
                        Agente distinto del interlocutor, siempre.
```

La composición concreta está en [`composicion.md`](composicion.md), y el circuito completo
en [`entrada/02-CIRCUITO.md`](../../entrada/02-CIRCUITO.md).
