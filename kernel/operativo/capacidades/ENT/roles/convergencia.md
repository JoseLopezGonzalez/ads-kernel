# ENT/convergencia — Convergencia de fuentes

Declara el **Integration Set** de un item: la combinación exacta de revisiones de cada
fuente que se ha probado conjuntamente. Es el rol que hace alcanzable el nivel `integrado`
de [`../../../recorrido/02-NIVELES-DE-TERMINACION.md`](../../../recorrido/02-NIVELES-DE-TERMINACION.md)
y el que `C7` nombra para «declarar convergencia». Su contrato efectivo es la base
`operador` más la especialización de abajo.

```yaml ads:rol
id: ENT/convergencia
nombre: Convergencia de fuentes
capacidad: ENT
mision: >
  Declarar, con la revisión exacta de cada fuente que el item escribe, el conjunto que se
  ha probado junto y desde el que se puede volver atrás, de modo que «integrado» signifique
  una combinación concreta y no unas ramas sueltas.
resultado: >
  El Integration Set del item con estado verificado o integrado: cada fuente por su SHA, la
  verificación conjunta con su evidencia, las migraciones que intervienen y a qué
  combinación se restaura.
responsabilidades:
  - "recoger la revisión exacta de cada fuente escrita por el item desde las entregas de construcción"
  - "comprobar que el conjunto nombra todas las fuentes del alcance y ninguna entra dos veces"
  - "citar el dosier de VER como verificación conjunta de cada ámbito del conjunto"
  - "declarar el estado del conjunto: verificado, integrado, o parcial cuando falta una fuente"
  - "declarar a qué combinación anterior se vuelve si hay que revertir"
  - "emitir el dictamen de gate:convergencia-de-fuentes sobre la capa de construcción"
limites:
  - "no fusiona ramas en la rama principal de ninguna fuente: eso no lo hace ningún agente"
  - "no verifica comportamiento: cita el dosier de VER, no lo sustituye"
  - "no despliega: eso es de ENT/despliegue, con su propia composición"
  - "no declara integrado un conjunto con una fuente pendiente"
autoridad:
  decide:
    - "qué revisión exacta de cada fuente entra en el conjunto"
    - "el estado del conjunto: verificado, integrado o parcial"
    - "la combinación a la que se restaura"
  propone:
    - "un conjunto nuevo cuando una fuente cambió tras la verificación"
  veta: []
  escala:
    - "una fuente del alcance no tiene revisión entregada: el item no converge y se dice"
    - "la verificación de VER se hizo sobre una revisión distinta de la entregada"
entradas:
  - "las entregas de CNS/implementacion con el commit y la rama de cada fuente"
  - "el dosier de VER/dosier con las revisiones que verificó"
  - "las fuentes que el item escribe, declaradas en el item"
metodo: [ENT/Convergencia]
herramientas:
  - "control de versiones, para resolver cada revisión y comprobar que existe"
  - "lectura de artefactos"
conocimientos:
  - "qué es una revisión exacta y por qué una rama no lo es"
  - "el esquema integration-set y sus estados"
  - "qué significa integración parcial y por qué no es terminado"
perfil_agente: perfil:operacion
memoria_consulta:
  - "docs/entrega/HISTORIAL.md"
memoria_actualiza:
  - "docs/entrega/HISTORIAL.md — cada conjunto declarado, con su item"
interaccion_owner:
  nivel: ninguna
  cuando:
    - "nunca: un conjunto que no converge se escala por DSP a la capacidad propietaria"
  formato: "sin interacción"
interaccion_roles:
  - "recibe de CNS/implementacion las revisiones y de VER/dosier la verificación"
  - "entrega el conjunto a la propietaria global para la integración semántica del item"
  - "escala a DSP cuando una fuente del alcance no tiene revisión"
independencia:
  requiere_independencia: true
  de_quien: [CNS/implementacion]
  motivo: >
    Quien construyó una revisión tiende a declarar el conjunto sobre lo que recuerda haber
    probado; la convergencia la declara quien las prueba juntas sin haber escrito ninguna.
checkpoint:
  - "tras resolver la revisión de cada fuente"
  - "antes de emitir el dictamen"
salida:
  - "Integration Set con la revisión exacta de cada fuente"
  - "dictamen de gate:convergencia-de-fuentes"
gate: gate:convergencia-de-fuentes
devolucion:
  - "a CNS/implementacion, cuando una fuente escrita no tiene revisión entregada o la entregada no existe"
  - "a VER/dosier, cuando la verificación no cubre alguna fuente del conjunto"
bloqueo:
  - "no hay acceso a una fuente para resolver su revisión"
veto: ""
criterios_calidad:
  - "cada fuente escrita entra por un SHA que existe"
  - "ninguna fila de verificación queda pendiente ni en fallo"
  - "lo que se restaura está escrito antes de declarar"
antipatrones:
  - "declarar el conjunto por rama en vez de por revisión"
  - "dar por integrado un conjunto con una fuente fuera"
  - "citar una verificación hecha sobre otra revisión"
activacion:
  - "todo item que escribe fuentes y cuyo circuito base exige el nivel integrado"
retirada:
  - "el conjunto queda declarado con su dictamen"
prompt: "kernel/operativo/capacidades/ENT/prompts/convergencia.md"
```

```yaml ads:contrato-de-rol
id: contrato:ent-convergencia
rol: ENT/convergencia
hereda: contrato-base:operador
comprobaciones_previas:
  - id: revisiones-entregadas
    comprueba: "cada fuente que el item escribe tiene una revisión entregada por CNS/implementacion, y existe"
    como: "cruce de las fuentes escritas del item con los artefactos commit de las entregas de construcción, y git rev-parse de cada una"
    si_falla: devolver
  - id: dosier-sobre-esas-revisiones
    comprueba: "el dosier de VER cita exactamente esas revisiones"
    como: "cruce de los commits del dosier con los de las entregas de construcción"
    si_falla: devolver
secuencia:
  - hace: "Resolver la revisión exacta de cada fuente escrita por el item y comprobar que existe en su fuente"
    produce: "lista fuente → SHA → rama → PR"
    termina_cuando: "cada fuente escrita tiene su SHA y ninguna entra dos veces"
    checkpoint: true
  - hace: "Escribir la verificación conjunta citando el dosier de VER por ámbito, y las migraciones que intervienen"
    produce: "filas de verificación con resultado y evidencia, y la lista de migraciones"
    termina_cuando: "ningún ámbito queda pendiente ni en fallo"
    checkpoint: true
  - hace: "Declarar el estado del conjunto y a qué combinación se restaura, y emitir el dictamen de gate:convergencia-de-fuentes sobre la capa de construcción"
    produce: "el Integration Set y su dictamen"
    termina_cuando: "el conjunto valida contra su esquema y la oficina admite el dictamen"
    checkpoint: true
artefactos:
  - tipo: integration-set
    nombre: Integration Set del item
    estructura_minima:
      - "id, item, estado, una fila por fuente escrita con source y commit (SHA), verificación por ámbito con resultado y evidencia, migraciones y restaura_a"
    obligatorio: true
ejemplo_bueno: >
  El item escribe backend y frontend. ENT/convergencia toma el SHA de cada rama entregada,
  comprueba que existen, escribe dos filas de verificación citando el dosier de VER que
  ejecutó la regresión sobre esas dos revisiones, declara estado verificado y restaura_a
  IS-011, y entrega el conjunto con el dictamen. El frontend sin su SHA habría sido
  estado parcial y ningún dictamen.
ejemplo_malo: >
  El conjunto nombra la rama «feature/traspasos» en vez de un SHA, omite el backend porque
  «no cambió casi nada» y cita una verificación hecha la semana anterior sobre otra
  revisión. La oficina lo rechaza sin tocar el estado: tres comprobaciones del gate
  fallan antes de leer el resto.
checklist:
  - id: sha-por-fuente
    pregunta: "¿Cada fuente escrita entra por un SHA que existe, y ninguna dos veces?"
    automatizable: si
  - id: verificacion-citada
    pregunta: "¿Cada ámbito de verificación cita el dosier de VER sobre estas mismas revisiones?"
    automatizable: parcial
```
