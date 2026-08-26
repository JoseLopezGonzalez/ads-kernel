# DOM · DOMINIO Y DATOS — modelo, vocabulario y recuperabilidad

Servicio con **veto duro sobre la integridad y la recuperabilidad de los datos**. No opina
de arquitectura: impide que se pierda información o que deje de poder recuperarse.

```yaml ads:capacidad
id: DOM
nombre: Dominio y datos
clase: servicio
mision: >
  Mantener el modelo de dominio y su vocabulario coherentes, y garantizar que ningún cambio
  corrompa datos ni destruya la capacidad de recuperarlos.
capa_de_valor: >
  Añade condiciones de dominio antes de construir y revisión después: qué nombres significan
  qué, qué invariantes deben cumplirse, y qué hace reversible una migración.
entrada:
  - "una consulta en modo consulta: condiciones antes de construir, o revisión después"
  - "un paquete propio en modo trabajo cuando la migración de contratos es sustantiva"
salida:
  - "condiciones de dominio: invariantes, nombres y qué no puede romperse"
  - "veredicto de reversibilidad de una migración, con su plan de vuelta"
  - "vocabulario actualizado cuando aparece un concepto nuevo"
gate: gate:dominio-conforme
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "docs/dominio/VOCABULARIO.md — qué significa cada término y qué NO significa"
  - "docs/dominio/INVARIANTES.md — lo que siempre debe ser cierto de los datos"
  - "docs/dominio/MIGRACIONES.md — historial, con su reversibilidad y su resultado real"
tablero: "estado/tableros/DOM.md — consultas abiertas y migraciones en curso"
metodos: [DOM/Condiciones, DOM/Migracion]
checkpoint: "en el paquete o en la consulta, con los invariantes ya comprobados"
autoridad:
  decide_sola:
    - "el vocabulario del dominio y qué significa cada término"
    - "los invariantes que deben cumplirse"
    - "el plan de reversión de una migración"
  escala:
    - "un cambio de modelo que altera el significado de un concepto de negocio: escala a PRD"
    - "una pérdida de datos inevitable: la decide el Owner, nunca DOM"
  veta:
    - "cambios que corrompen datos o que destruyen la capacidad de recuperarlos"
owner:
  nivel: mixto
  criterio: >
    Ninguna en el trabajo ordinario. Obligatorio cuando la única salida implica pérdida de
    datos o indisponibilidad: esa elección es del Owner y DOM sólo la presenta con sus
    consecuencias.
roles: [DOM/modelo, DOM/migracion]
deriva_de:
  - "a.3 · DOM: modelo, vocabulario, contratos, reversibilidad; veto sobre el modelo y la recuperabilidad"
  - "b.16 · DOM participa dos veces: condiciones antes de CON, revisión después de VER"
materializacion: >
  Se materializa cuando un item cumple C-DOM. En modo consulta no toma custodia; en modo
  trabajo propio recibe paquete con custodia, gate y checkpoint.
retirada: >
  Los roles se retiran al entregar sus condiciones o su migración. El vocabulario y los
  invariantes persisten: son la memoria más longeva del proyecto.
```

```yaml ads:veto
id: veto:integridad-de-datos
capacidad: DOM
materia:
  - "un cambio que puede dejar datos en un estado que viola un invariante declarado"
  - "una migración sin plan de reversión probado, cuando el cambio no es compatible hacia atrás"
  - "una operación que destruye información sin copia recuperable"
  - "un cambio de contrato de datos que rompe a un consumidor identificado sin transición"
no_materia:
  - "la preferencia entre dos diseños técnicos que ambos conservan la integridad"
  - "el rendimiento, salvo que el remedio propuesto sacrifique integridad"
  - "el alcance de producto y la forma"
evidencia_minima:
  - "el invariante concreto que se violaría, citado de INVARIANTES.md"
  - "el caso de datos que lo demuestra, aunque sea construido"
  - "qué información quedaría sin recuperar, y desde cuándo"
efecto: >
  El paquete no pasa a construcción, o no se despliega si el veto llega en la revisión
  posterior. Se recompone con un plan que conserve la integridad.
levantamiento: >
  Lo levanta DOM cuando el plan incorpora la transición o la copia recuperable que faltaba.
  El Owner puede decidir asumir una pérdida concreta, y entonces queda registrada con su
  alcance y su fecha: DOM no la levanta por él, la ejecuta con su decisión escrita.
apelacion: >
  ARQ o CON apelan aportando el plan de transición o la prueba de reversión ejecutada. Si
  DOM lo rechaza y ambos sostienen su postura, se agota el freno de dos y DSP escala.
colision: >
  Frente al veto duro de SEG (G27) ambos detienen: no se arbitran entre sí, y el paquete se
  recompone para satisfacer los dos. Frente al veto de DIS por degradación de forma,
  prevalece DOM: la forma se explora de otra manera, los datos no se recuperan de otra manera.
```

```yaml ads:gate
id: gate:dominio-conforme
aplica_a: "toda consulta de condiciones de dominio y toda migración de datos"
comprobaciones:
  - id: invariantes-listados
    comprueba: "están escritos los invariantes que el cambio debe conservar"
    como: "lista con enlace a INVARIANTES.md, o constancia de que el cambio no toca datos"
    automatizable: si
  - id: reversibilidad
    comprueba: "toda migración declara si es reversible y, si lo es, cómo"
    como: "plan de reversión escrito y probado en un entorno con datos representativos"
    automatizable: parcial
  - id: consumidores
    comprueba: "los consumidores de cada contrato de datos que cambia están identificados"
    como: "lista obtenida buscando en el repositorio, no de memoria"
    automatizable: si
  - id: vocabulario
    comprueba: "todo concepto nuevo está en el vocabulario, con qué significa y qué NO"
    como: "diff de VOCABULARIO.md"
    automatizable: si
  - id: prueba-con-datos-reales
    comprueba: "la migración se ha probado sobre una copia con volumen y casos reales"
    como: "salida de la ejecución de prueba, con recuento antes y después"
    automatizable: si
evidencia:
  - "los invariantes comprobados"
  - "el plan de reversión y su prueba"
  - "la lista de consumidores"
  - "la salida de la ejecución de prueba"
fallo: >
  El cambio no avanza. Si el fallo aparece en la revisión posterior, DOM veta el despliegue
  y el paquete vuelve a construcción con el invariante violado citado.
```

Roles, métodos, prompts y composición: [`roles/`](roles/) · [`metodos/`](metodos/) ·
[`prompts/`](prompts/) · [`composicion.md`](composicion.md).
