# USO · USO REAL — validación en condiciones reales

**No equivale al Owner.** La evidencia de uso real puede venir de él, de otro usuario, de un
operador, de un dispositivo físico, de telemetría, de logs o de un plan de validación
humana (a.3). El Owner interviene sólo cuando el resultado requiere su autoridad o su juicio.

```yaml ads:capacidad
id: USO
nombre: Uso real
clase: estacion
mision: >
  Comprobar en condiciones reales que lo entregado sirve para lo que se pidió, y traer de
  vuelta lo que el uso revela y nadie había previsto.
capa_de_valor: >
  Añade evidencia de realidad: qué ocurre cuando esto lo usa alguien, con sus datos, en su
  dispositivo y con su prisa.
entrada:
  - "un cambio entregado que cumple C-USO: existe fuente de uso real aplicable y VER no basta"
  - "telemetría o logs que contradicen lo esperado"
salida:
  - "evidencia de uso real con su fuente declarada"
  - "lo que el uso reveló y no estaba previsto, como candidatos a item"
  - "confirmación de que la expectativa quedó satisfecha, o de que no"
gate: gate:uso-comprobado
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "docs/uso/OBSERVACIONES.md — qué se ha observado, cuándo y con qué fuente"
  - "docs/uso/COLA-DE-VALIDACION.md — el lote pendiente del Owner, ordenado por coste de preparación"
tablero: "estado/tableros/USO.md — validaciones en curso y lote pendiente"
metodos: [USO/Validacion]
checkpoint: "en el paquete, con qué se ha observado y con qué fuente"
autoridad:
  decide_sola:
    - "qué fuente de uso real se usa y por qué"
    - "si la evidencia disponible basta para el criterio que se valida"
    - "declarar que un criterio no se pudo validar, y decirlo"
  escala:
    - "el uso revela que la expectativa era otra: escala a PRD"
    - "el uso contradice una decisión de forma: escala a DIS"
  veta: []
owner:
  nivel: opcional-acumulada
  criterio: >
    El Owner es UNA fuente entre varias. Cuando es la fuente, se le convoca POR LOTES (G36),
    con el estado preparado de antemano y ordenado por coste de preparación. Nunca item por
    item, y nunca detiene el item salvo que su juicio sea condición de cierre.
roles: [USO/validacion]
deriva_de:
  - "a.3 · USO: siete fuentes posibles; G36 íntegro cuando la fuente es humana"
  - "b.16 · C-USO y su activación en FEA, GAP, DEF, DEU e INC"
materializacion: >
  Se materializa cuando existe fuente de uso real aplicable Y el resultado no es verificable
  sólo por VER. Si no hay fuente aplicable, la ruta lo deja escrito en `no activadas`.
retirada: >
  El rol se retira al entregar la evidencia. Las observaciones persisten: son la fuente de
  los items que nacen del uso real.
```

```yaml ads:gate
id: gate:uso-comprobado
aplica_a: "la capa de USO antes de cerrar el item"
comprobaciones:
  - id: fuente-declarada
    comprueba: "está escrito de cuál de las siete fuentes procede la evidencia"
    como: "campo fuente presente, con una de las siete"
    automatizable: si
  - id: comportamiento-no-opinion
    comprueba: "la evidencia registra comportamiento observado, no opinión sobre el comportamiento"
    como: "lectura: grabación, telemetría, medición o registro de lo que ocurrió"
    automatizable: parcial
  - id: condiciones-reales
    comprueba: "las condiciones están declaradas: dispositivo, datos, momento"
    como: "campos presentes"
    automatizable: si
  - id: lote-cuando-owner
    comprueba: "si la fuente es el Owner, se le convocó por lotes con el estado preparado"
    como: "enlace a la cola de validación y a su preparación"
    automatizable: si
  - id: no-validado-declarado
    comprueba: "lo que no se pudo validar está dicho"
    como: "sección presente, aunque sea declarada vacía"
    automatizable: si
evidencia:
  - "grabaciones, telemetría, logs o registro de observación"
  - "las condiciones declaradas"
  - "el lote de validación cuando la fuente fue el Owner"
fallo: >
  La capa no se deposita. Si lo que falta es evidencia, vuelve a USO. Si lo que la evidencia
  muestra es que la expectativa no se cumple, vuelve a la capacidad propietaria de la capa
  que falla.
```

Roles, métodos, prompts y composición: [`roles/`](roles/) · [`metodos/`](metodos/) ·
[`prompts/`](prompts/) · [`composicion.md`](composicion.md).
