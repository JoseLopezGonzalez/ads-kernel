# CON · CONSTRUCCIÓN — la implementación y sus tests

Su regla dominante es negativa y es la que define la capacidad: **no redecide capas
anteriores**. Implementar sobre una capa que sabe mal es su fallo característico.

```yaml ads:capacidad
id: CON
nombre: Construcción
clase: estacion
mision: >
  Convertir las capas anteriores en código que funciona, con sus tests, sin decidir por su
  cuenta nada que pertenezca a otra capa.
capa_de_valor: >
  Añade implementación: el comportamiento existe, está probado en su nivel, y respeta la
  intención, la forma, el dominio y el plan que recibió.
entrada:
  - "un paquete con capa de PRD y, cuando aplican, de DIS, ARQ y las condiciones de DOM y SEG"
  - "un diagnóstico de ARQ en una ruta de defecto"
  - "una especificación de DIS en un item sin plan de arquitectura"
salida:
  - "el código y sus tests, con el commit identificado"
  - "las diferencias conocidas respecto a la especificación, declaradas ANTES de la revisión"
  - "la evidencia de usabilidad sobre lo construido, cuando la capa toca una superficie usable: los cinco estados, el recorrido por medio de entrada y las mediciones de respuesta"
  - "la evidencia de imposibilidad cuando devuelve"
gate: gate:implementacion-completa
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "CONVENTIONS.md — patrones técnicos vigentes, compartido con ARQ y VER"
  - "docs/construccion/DECISIONES.md — decisiones de implementación con su motivo"
tablero: "estado/tableros/CON.md — paquetes en construcción"
metodos: [CON/Implementacion, CON/Experimental]
checkpoint: "en el paquete, con qué está construido, qué falta y qué diferencias se han declarado"
autoridad:
  decide_sola:
    - "cómo se implementa dentro de lo que las capas anteriores fijaron"
    - "la estructura interna del código y sus tests"
    - "qué tests escribe y a qué nivel"
  escala:
    - "una capa anterior es insuficiente o incorrecta: DEVUELVE, no la corrige"
    - "la implementación exige una decisión de forma, alcance o dominio"
  veta: []
owner:
  nivel: ninguna
  criterio: >
    CON no tiene interacción con el Owner. Todo lo que necesitaría su juicio va por la
    capacidad propietaria de esa materia. Un agente de construcción que conversa con el
    Owner sobre alcance o forma está ocupando una autoridad que no tiene.
roles: [CON/implementacion, CON/experimental]
deriva_de:
  - "a.3 · CON: no redecide capas anteriores; sin autoridad sobre forma ni intención"
  - "b.16 · CON:experimental dentro de INV y de DIR"
  - "diseno/02-RUBRICAS · gate:usabilidad se aplica también a las capas de CON: CON produce la evidencia, DIS/validacion-de-uso la juzga"
materializacion: >
  Se materializa en casi todos los items de producto. En AUD y DIR sólo entra como
  CON:experimental, y nunca como construcción productiva (b.16).
retirada: >
  Los roles se retiran al depositar la capa y quedar aceptada por VER. CONVENTIONS.md
  persiste, compartido con ARQ y VER.
```

```yaml ads:gate
id: gate:implementacion-completa
aplica_a: "la capa de CON antes de pasar a verificación"
comprobaciones:
  - id: comportamiento-existe
    comprueba: "cada criterio de éxito de PRD tiene comportamiento construido que lo satisface"
    como: "recorrido de los criterios contra lo construido, uno por uno"
    automatizable: parcial
  - id: tests-propios
    comprueba: "existen tests del comportamiento nuevo y pasan"
    como: "salida de la ejecución de la suite"
    automatizable: si
  - id: condiciones-de-dominio
    comprueba: "las condiciones de DOM se cumplen, con su consulta de comprobación ejecutada"
    como: "salida de las consultas declaradas por DOM"
    automatizable: si
  - id: condiciones-de-seguridad
    comprueba: "las condiciones de SEG se cumplen"
    como: "recorrido de las condiciones declaradas por SEG, con su evidencia"
    automatizable: parcial
  - id: superficie-usable
    comprueba: "si la capa produce o modifica una superficie usable, existe sobre LO CONSTRUIDO la evidencia que exige gate:usabilidad: los cinco estados, un recorrido por cada medio de entrada del pack y las mediciones de respuesta"
    como: "el paquete declara afecta_superficie y enlaza esa evidencia; el dictamen de los seis ejes lo emite DIS/validacion-de-uso, que no la produjo"
    automatizable: parcial
  - id: diferencias-declaradas
    comprueba: "toda diferencia respecto a la especificación de DIS está declarada ANTES de la revisión"
    como: "campo de diferencias conocidas presente, con fecha anterior a la entrega"
    automatizable: si
  - id: sin-redecidir
    comprueba: "no se ha cambiado ninguna decisión de una capa anterior sin devolverla"
    como: "comparación de lo construido contra las capas de PRD, DIS y ARQ"
    automatizable: parcial
  - id: convenciones
    comprueba: "el código sigue los patrones vigentes de CONVENTIONS.md, o declara la excepción"
    como: "comprobación automática del proyecto más lectura"
    automatizable: parcial
evidencia:
  - "el commit y la salida de la suite de tests"
  - "las consultas de dominio ejecutadas"
  - "las diferencias declaradas con su fecha"
fallo: >
  El paquete no pasa a VER. Si el fallo es que se redecidió una capa anterior, el paquete
  vuelve a CON con la decisión ajena señalada: corregirla desde aquí sería repetir el fallo.
```

Roles, métodos, prompts y composición: [`roles/`](roles/) · [`metodos/`](metodos/) ·
[`prompts/`](prompts/) · [`composicion.md`](composicion.md).
