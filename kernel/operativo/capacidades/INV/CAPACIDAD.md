# INV · INVESTIGACIÓN Y EVIDENCIA — saber antes de decidir

Puede declarar que **una decisión no puede tomarse todavía** (a.3). Es una autoridad
inusual y es la que hace que la investigación sirva para algo: sin ella, se decide igual y
la investigación es decorativa.

```yaml ads:capacidad
id: INV
nombre: Investigación y evidencia
clase: servicio
mision: >
  Responder preguntas concretas con evidencia comprobable y fechada, y declarar cuándo la
  evidencia disponible no permite todavía tomar una decisión.
capa_de_valor: >
  Añade conocimiento: convierte una duda en una respuesta con fuentes, frescura declarada y
  límite de alcance escrito.
entrada:
  - "una pregunta acotada con su consumidor declarado"
  - "un item INV cuyo resultado perseguido es conocimiento"
salida:
  - "la respuesta con sus fuentes, su frescura y qué queda fuera de su alcance"
  - "la evidencia producida, incluida la que contradice la hipótesis"
  - "el veredicto «no se puede decidir todavía», cuando corresponde"
gate: gate:evidencia-fresca
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "docs/investigacion/ — una carpeta por investigación, con pregunta, evidencia y destino"
  - "docs/investigacion/FRESCURA.md — qué respuestas caducan y cuándo"
tablero: "estado/tableros/INV.md — preguntas abiertas y evidencia entregada"
metodos: [INV/Investigacion]
checkpoint: "en el paquete, con las fuentes ya consultadas y las hipótesis descartadas"
autoridad:
  decide_sola:
    - "qué fuentes consulta y cuáles considera fiables"
    - "la frescura de una respuesta y cuándo caduca"
    - "declarar que una decisión NO PUEDE TOMARSE todavía, con qué falta"
  escala:
    - "la pregunta no es respondible con los medios disponibles"
    - "la evidencia contradice una decisión ya tomada y en ejecución"
  veta: []
owner:
  nivel: ninguna
  criterio: >
    INV no consulta al Owner: entrega evidencia a quien decidirá. Si el consumidor de la
    respuesta es el Owner, se la entrega la capacidad propietaria de esa materia, no INV.
roles: [INV/investigacion]
deriva_de:
  - "a.3 · INV: spikes contra entorno real, freshness (G22+G33), puede declarar que no se puede decidir"
  - "b.16 · INV es propietario global de los items INV y activa CON:experimental"
materializacion: >
  Se materializa cuando existe una pregunta acotada con consumidor declarado. Sin consumidor
  declarado no se materializa: produciría conocimiento que nadie usa.
retirada: >
  El rol se retira al entregar la respuesta. Las investigaciones persisten con su fecha: una
  respuesta vieja sigue valiendo si se declara su frescura.
```

```yaml ads:gate
id: gate:evidencia-fresca
aplica_a: "toda respuesta de INV antes de entregarse a quien decidirá"
comprobaciones:
  - id: contesta-la-pregunta
    comprueba: "la respuesta contesta la pregunta acotada que se hizo, no una parecida"
    como: "comparación literal entre la pregunta registrada y la respuesta"
    automatizable: parcial
  - id: fuentes-comprobables
    comprueba: "cada fuente tiene enlace o referencia verificable y su fecha"
    como: "comprobación estructural de las fuentes"
    automatizable: si
  - id: frescura-declarada
    comprueba: "está escrito hasta cuándo vale esta respuesta y qué la caducaría"
    como: "campo frescura presente con su condición"
    automatizable: si
  - id: limite-de-alcance
    comprueba: "está escrito qué NO responde esta investigación"
    como: "campo presente y no vacío"
    automatizable: si
  - id: evidencia-contraria
    comprueba: "la evidencia que contradice la hipótesis está incluida, no omitida"
    como: "lectura del informe: si no hay ninguna, se declara que no apareció"
    automatizable: parcial
  - id: consumidor-declarado
    comprueba: "está escrito quién consumirá esta respuesta y para qué decisión"
    como: "campo presente con enlace al item o a la decisión"
    automatizable: si
evidencia:
  - "las fuentes con su fecha"
  - "las mediciones o el experimento, cuando los hubo"
  - "la declaración de frescura y de límite de alcance"
fallo: >
  La respuesta no se entrega. Si la pregunta no era respondible, INV lo declara y esa
  declaración ES la respuesta: no se rellena con una aproximación.
```

Roles, métodos, prompts y composición: [`roles/`](roles/) · [`metodos/`](metodos/) ·
[`prompts/`](prompts/) · [`composicion.md`](composicion.md).
