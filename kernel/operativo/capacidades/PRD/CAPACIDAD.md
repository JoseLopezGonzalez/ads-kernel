# PRD · PRODUCTO — intención y criterio de éxito

Convierte una intención en un **resultado definido con criterio de terminado**. En un GAP,
es donde el hueco pasa de «falta algo» a algo que alguien puede dar por hecho: es el
procedimiento estándar de gaps que el kernel 1.3.0 no tenía.

```yaml ads:capacidad
id: PRD
nombre: Producto
clase: estacion
mision: >
  Establecer para quién es un cambio, qué cambia, qué queda fuera, y qué haría que fuera un
  fracaso aunque funcionase técnicamente.
capa_de_valor: >
  Añade intención y criterio: convierte un encuadre en alcance declarado, criterio de éxito
  comprobable y definición de fracaso, enlazados con la definición de éxito del Owner.
entrada:
  - "un encuadre entregado por ENC cuyo item cumple C-PRD"
  - "un hallazgo de USO o de APR que revela una expectativa no satisfecha"
  - "una consulta en modo consulta desde DIS, ARQ o ENC"
salida:
  - "alcance declarado: qué entra, qué NO entra y por qué"
  - "criterio de éxito comprobable por alguien que no participó en definirlo"
  - "definición de fracaso: qué haría que esto fuera un fracaso aunque funcione"
  - "prioridad relativa propuesta, que el Owner confirma o cambia"
gate: gate:intencion-definida
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "docs/producto/EXITO.md — la definición de éxito del Owner (K0.13) y su historia"
  - "docs/producto/ALCANCE.md — qué está dentro y fuera del producto, con fecha"
  - "docs/producto/DECISIONES.md — decisiones de producto y qué sustituyen"
tablero: "estado/tableros/PRD.md — items en definición de intención"
metodos: [PRD/Definicion, PRD/Gap]
checkpoint: "en el paquete, con el alcance cerrado hasta ahora y la pregunta pendiente al Owner"
autoridad:
  decide_sola:
    - "alcance rutinario: qué entra y qué no dentro de una dirección ya aprobada"
    - "el criterio de éxito y la definición de fracaso de un item"
    - "cancelar items de naturaleza interna que han dejado de tener sentido"
  escala:
    - "alcance relevante: lo que cambia lo que el producto es"
    - "prioridad estratégica"
    - "cancelar algo que el Owner pidió expresamente: se propone, decide él"
    - "primera dirección de producto (a.8)"
  veta: []
owner:
  nivel: mixto
  criterio: >
    Obligatorio en primera dirección de producto, decisión estratégica o difícilmente
    reversible, y en toda cancelación de algo que él pidió. Opcional acumulada cuando el
    item extiende un owner_approved_pattern. Ninguna en alcance rutinario dentro de una
    dirección aprobada, y en items internos.
roles: [PRD/definicion, PRD/criterio-de-exito]
deriva_de:
  - "a.3 · PRD: intención, criterio de éxito, procedimiento estándar de gaps"
  - "b.16 · PRD es propietario global de FEA y GAP"
  - "K0.13 · definición de éxito del Owner"
materializacion: >
  Se materializa cuando DSP crea un paquete de PRD, lo que ocurre en todo FEA y GAP y en
  los DEF cuyo diagnóstico revela C-PRD.
retirada: >
  Los roles se retiran al depositar la capa. El equipo se desmaterializa cuando el tablero
  queda sin cola durante dos auditorías; la memoria de producto persiste.
```

```yaml ads:gate
id: gate:intencion-definida
aplica_a: "la capa de PRD antes de que el item continúe hacia diseño, arquitectura o construcción"
comprobaciones:
  - id: para-quien
    comprueba: "está escrito para quién es el cambio y en qué momento lo usa"
    como: "lectura del alcance: nombra un perfil de uso concreto, no «el usuario»"
    automatizable: parcial
  - id: fuera-de-alcance
    comprueba: "está escrito qué NO entra, con al menos un elemento"
    como: "comprobación estructural: la lista de fuera de alcance no está vacía"
    automatizable: si
  - id: criterio-comprobable
    comprueba: "el criterio de éxito lo puede verificar alguien que no participó en definirlo"
    como: "cada criterio declara qué se mira, dónde, y qué resultado cuenta"
    automatizable: parcial
  - id: definicion-de-fracaso
    comprueba: "está escrito qué haría que esto fuera un fracaso aunque funcione"
    como: "campo presente y distinto de la negación del criterio de éxito"
    automatizable: parcial
  - id: enlace-con-exito-del-owner
    comprueba: "el item enlaza con qué parte de la definición de éxito del Owner se relaciona"
    como: "enlace a docs/producto/EXITO.md o constancia de que es trabajo interno"
    automatizable: si
  - id: owner-cuando-corresponde
    comprueba: "si el alcance es relevante o estratégico, el Owner lo confirmó"
    como: "el paquete enlaza la confirmación con su fecha"
    automatizable: si
evidencia:
  - "el alcance declarado con su fuera de alcance"
  - "el criterio de éxito y la definición de fracaso"
  - "la confirmación del Owner cuando fue exigible"
fallo: >
  El item no avanza. Vuelve a PRD nombrando el campo que falta. Un item que avanza sin
  criterio de éxito comprobable llega a Verificación sin nada contra lo que verificar, y
  ahí el coste de arreglarlo es máximo.
```

Roles, métodos, prompts y composición: [`roles/`](roles/) · [`metodos/`](metodos/) ·
[`prompts/`](prompts/) · [`composicion.md`](composicion.md).
