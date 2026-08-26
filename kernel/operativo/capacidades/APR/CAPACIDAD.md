# APR · APRENDIZAJE — convertir el recorrido en criterio

**No es un trámite universal.** El cierre de un item ejecuta una comprobación
—`learning_candidate: none | <enlace>`— que NO requiere crear paquete de APR (a.3). APR
recibe paquete sólo ante **señal real**.

```yaml ads:capacidad
id: APR
nombre: Aprendizaje
clase: estacion
mision: >
  Convertir lo ocurrido en cambio de criterio: reglas, patrones, memorias y composiciones
  que hagan que el sistema no repita lo que ya le pasó.
capa_de_valor: >
  Añade criterio: transforma un hecho aislado en una regla comprobable, o declara
  expresamente que no hay aprendizaje promovible.
entrada:
  - "un item cerrado con learning_candidate != none"
  - "un incidente: APR es obligatorio en todo INC (b.16)"
  - "una revisión de circuito o una promoción a upstream"
salida:
  - "entrada en el ledger con la regla candidata y su evidencia"
  - "actualización de la memoria de la capacidad competente"
  - "candidato a UPSTREAM cuando la regla vale para más de un proyecto"
  - "el veredicto «sin aprendizaje promovible», que es una salida legítima"
gate: gate:aprendizaje-fundado
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "docs/PROJECT_LEARNINGS.md — el ledger del proyecto (G52)"
  - "docs/agentic/ORG_LEARNINGS.md — el ledger de la organización (G52)"
  - "docs/UPSTREAM.md — candidatos a promover a kernel o a pack (K0.12)"
tablero: "estado/tableros/APR.md — señales pendientes de convertir en criterio"
metodos: [APR/Promocion]
checkpoint: "en el paquete, con la evidencia reunida y las observaciones anteriores enlazadas"
autoridad:
  decide_sola:
    - "si una señal es aprendizaje promovible o un hecho aislado"
    - "el enunciado de la regla candidata"
    - "declarar «sin aprendizaje promovible», que es un resultado normal"
  escala:
    - "una regla candidata que contradice una regla vigente del kernel"
    - "una promoción a UPSTREAM que cambia el contrato de una capacidad"
  veta: []
owner:
  nivel: opcional-acumulada
  criterio: >
    APR no consulta al Owner salvo cuando la regla candidata afecta a una materia suya. Las
    promociones a UPSTREAM van a su cola de validación por lotes, y no detienen nada.
roles: [APR/promocion]
deriva_de:
  - "a.3 · APR: no es trámite universal; se materializa ante señal real"
  - "b.10 · la comprobación de aprendizaje se ejecuta en el cierre, sin crear paquete"
  - "G52 · los dos ledgers · K0.12 · upstream"
materializacion: >
  Se materializa SÓLO ante señal real: learning_candidate con enlace, incidente, revisión de
  circuito o promoción. Una entrada forzada contamina el ledger con falsa autoridad.
retirada: >
  El rol se retira al escribir la entrada del ledger. Los ledgers persisten siempre: son la
  memoria más valiosa del sistema y la que justifica que exista.
```

```yaml ads:gate
id: gate:aprendizaje-fundado
aplica_a: "toda entrada de ledger y toda promoción a UPSTREAM"
comprobaciones:
  - id: evidencia-de-ocurrencia
    comprueba: "la entrada enlaza los items o incidentes concretos de los que sale"
    como: "enlaces presentes y resolubles"
    automatizable: si
  - id: dos-veces-o-incidente
    comprueba: "la regla se apoya en al menos dos ocurrencias, o en un incidente"
    como: "recuento de enlaces, o marca de incidente"
    automatizable: si
  - id: regla-comprobable
    comprueba: "la regla candidata se puede comprobar: dice qué hacer y cómo se sabe si se hizo"
    como: "lectura: la regla contiene una condición y una comprobación"
    automatizable: parcial
  - id: capa-correcta
    comprueba: "la regla está en la capa que le corresponde: proyecto, pack o kernel"
    como: "test de contaminación de K0.10 aplicado y escrito"
    automatizable: parcial
  - id: no-contradice
    comprueba: "la regla no contradice una vigente sin declararlo"
    como: "búsqueda de la materia en las reglas vigentes"
    automatizable: parcial
evidencia:
  - "los enlaces a las ocurrencias"
  - "el test de contaminación aplicado"
fallo: >
  La entrada no se escribe. Una regla promovida desde una sola ocurrencia no incidental
  contamina el ledger: hace que el sistema cambie de criterio por una casualidad.
```

Roles, métodos, prompts y composición: [`roles/`](roles/) · [`metodos/`](metodos/) ·
[`prompts/`](prompts/) · [`composicion.md`](composicion.md).
