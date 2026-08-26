# DSP · DESPACHO — orden y ruta, nunca contenido

Su autoridad es **total sobre el orden y la ruta, y ninguna sobre el contenido de ninguna
capa** (a.3). La [enmienda E1.1](../../../../docs/rediseno/a-ENMIENDA-E1-ENC.md) fija la
frontera con `ENC`: `DSP` **recibe** el encuadre que `ENC` produce y hace nacer el item; no
interpreta contenido, no conversa con el Owner en lugar de `ENC`, y **no decide
semánticamente una cancelación**. Es implementación software primero: lo que aquí se describe es el
comportamiento que ese runtime tendrá, y lo que un supervisor humano o agente ejecuta
mientras el runtime no exista.

> **Esta ficha NO implementa el dispatcher.** El runtime queda expresamente fuera del
> alcance de esta iteración. Lo que existe aquí es el contrato de comportamiento que ese
> runtime deberá cumplir, y los métodos que hoy ejecuta un supervisor.

```yaml ads:capacidad
id: DSP
nombre: Despacho
clase: sistema
mision: >
  Mantener el estado coherente y decidir qué se trabaja ahora, componiendo rutas y creando
  paquetes, sin decidir nunca el contenido de ninguna capa.
capa_de_valor: >
  Añade orden: encuadre estructural, ruta compuesta con su traza, paquetes con su
  declaración de acoplamiento, despacho determinista y explicado, y estado reconstruible.
entrada:
  - "un encuadre entregado por ENC en estado listo-para-dsp"
  - "una orden del Owner, natural o escrita en el tablero"
  - "un «Continúa»"
  - "un resultado emitido por cualquier capacidad"
salida:
  - "items con ficha, ruta y paquetes"
  - "la traza de activadas y NO activadas con motivo"
  - "el estado global calculado y las vistas derivadas regeneradas"
  - "la explicación de qué se eligió y qué se excluyó, y por qué"
gate: gate:despacho-coherente
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "el estado persistido completo: items, rutas, paquetes, control y eventos"
  - "estado/memoria/DSP/composiciones.md — composiciones por defecto y sus recomposiciones"
tablero: "estado/tableros/ — DSP regenera la zona COLA de todos los tableros"
metodos: [DSP/Enrutamiento, DSP/Continua, DSP/Supervision]
checkpoint: "no aplica a DSP como capacidad: el estado persistido ES su checkpoint"
autoridad:
  decide_sola:
    - "la composición de la ruta y su recomposición, con traza"
    - "la creación de paquetes y sus dependencias"
    - "el orden de despacho, aplicando b.12 de forma determinista"
    - "que un freno de a.7 o de b.9 se ha disparado, aplicando el umbral ya aprobado, y detener lo que ese freno detiene"
    - "crear y despachar desbloqueadores dentro del alcance ya autorizado (b.15.1)"
    - "prioridad normal por defecto, porque procede de una regla del kernel"
  escala:
    - "todo lo que exceda el alcance ya autorizado"
    - "los frenos de a.7 disparados"
    - "una inconsistencia de estado irresoluble sin decidir"
    - "toda CANCELACIÓN: DSP la propone cuando detecta la condición mecánica y la ejecuta con la orden ya autorizada, pero NUNCA posee la autoridad semántica para decidirla (b.7)"
    - "todo lo que exija interpretar contenido de producto, de diseño o de dominio: eso es de ENC y de la capacidad competente, no de DSP (enmienda E1.1)"
  veta: []
owner:
  nivel: mixto
  criterio: >
    DSP ejecuta las órdenes del Owner y le reporta; no le pide permiso para despachar. Sólo
    escala cuando un freno se dispara, cuando el desbloqueador amplía el alcance, o cuando
    encuentra una inconsistencia que no puede resolver sin decidir.
roles: [DSP/enrutamiento, DSP/estado, DSP/supervision]
deriva_de:
  - "a.3 + enmienda E1.1 · DSP: recepción del encuadre, enrutamiento, estado y supervisión; autoridad sobre orden y ruta, ninguna sobre contenido"
  - "b.5, b.12, b.14, b.15 · transiciones, selección, Continúa y cola vacía"
materializacion: "DSP se materializa SIEMPRE. Sin ella no hay sistema operativo."
retirada: "DSP no se retira mientras exista el proyecto."
```

```yaml ads:gate
id: gate:despacho-coherente
aplica_a: "toda acción de despacho: crear item, componer ruta, despachar o regenerar estado"
comprobaciones:
  - id: traza-de-ruta
    comprueba: "toda ruta declara activadas y NO activadas, cada una con motivo escrito"
    como: "comprobación estructural de la ficha de ruta"
    automatizable: si
  - id: seleccion-explicada
    comprueba: "todo despacho deja escrito qué se eligió, por qué, y qué se excluyó y por qué"
    como: "registro de selección presente por cada despacho"
    automatizable: si
  - id: determinismo
    comprueba: "mismo estado produce misma selección, con desempate por identificador"
    como: "reejecutar la selección sobre el mismo estado y comparar"
    automatizable: si
  - id: sin-contenido
    comprueba: "ninguna acción de DSP ha decidido el contenido de una capa"
    como: "toda mutación registra su autoridad, y ninguna con autoridad DSP toca una capa"
    automatizable: si
  - id: atribucion
    comprueba: "toda mutación registra quién la ordenó, quién la aplicó, sobre qué versión y con qué evento"
    como: "comprobación estructural del evento"
    automatizable: si
  - id: devolucion-con-paquete
    comprueba: "toda devolución tiene su paquete de corrección creado o reabierto en el mismo ciclo"
    como: "comprobación: ningún paquete devuelto sin paquete de corrección enlazado"
    automatizable: si
  - id: frenos-evaluados
    comprueba: "antes de despachar se han evaluado los cuatro frenos: devoluciones por par, ciclo multiparte, racha SIS y recomposiciones sin avance material"
    como: "el registro de selección enlaza los contadores vigentes de los cuatro; un despacho sin ellos no es conforme"
    automatizable: si
  - id: freno-disparado-con-dos-posturas
    comprueba: "todo freno disparado detiene lo que le corresponde y escala con LAS DOS posturas enfrentadas escritas"
    como: "el registro del freno contiene qué sostiene cada capacidad, con qué evidencia, y a quién se escaló"
    automatizable: si
  - id: inanicion-visible-sin-tocar-prioridad
    comprueba: "todo paquete listo no despachado muestra tiempo, postergaciones, quién lo adelantó y qué lo impide, y ninguna prioridad se ha modificado por el sistema"
    como: "la tabla de inanición existe y ningún evento de prioridad tiene autoridad distinta del Owner"
    automatizable: si
  - id: cancelacion-con-autoridad-ajena
    comprueba: "ninguna cancelación ejecutada por DSP tiene a DSP como autoridad semántica: ordenante, autoridad y ejecutor son campos distintos y la autoridad NUNCA es DSP"
    como: "lectura del evento de cancelación: autoridad pertenece a la capacidad con custodia, al propietario global o al Owner según materia (b.7)"
    automatizable: si
evidencia:
  - "la ficha de ruta con su traza"
  - "el registro de selección"
  - "los eventos con su atribución completa"
fallo: >
  La acción no se aplica y el estado queda como estaba. Si la incoherencia ya se aplicó, se
  registra `reconciliacion_pendiente` y DSP deja de girar hasta resolverla.
```

Roles, métodos, prompts y composición: [`roles/`](roles/) · [`metodos/`](metodos/) ·
[`prompts/`](prompts/) · [`composicion.md`](composicion.md).
