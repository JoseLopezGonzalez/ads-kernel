# ARQ · ARQUITECTURA — encaje y plan técnico

Su aportación distintiva no es opinar sobre tecnología: es **medir el radio de impacto**
sobre el código real de las fuentes, en vez de estimarlo. Es lo que impide construir sobre una
suposición de tamaño.

```yaml ads:capacidad
id: ARQ
nombre: Arquitectura
clase: estacion
mision: >
  Establecer cómo entra un cambio en lo que ya existe: qué toca de verdad, qué contratos
  cambian, qué alternativas hay con su coste, y en qué paquetes se descompone.
capa_de_valor: >
  Añade encaje: convierte una intención en un plan técnico con radio de impacto medido,
  contratos afectados, alternativas comparadas y descomposición en paquetes con dependencias.
entrada:
  - "un item que cumple C-ARQ: diagnóstico no evidente, toca contratos o estructura, o el radio excede un módulo"
  - "una ruta de defecto donde el diagnóstico no es evidente"
  - "una consulta en modo consulta desde PRD, DIS o ENC"
salida:
  - "radio de impacto MEDIDO, con la lista de ficheros y contratos afectados"
  - "alternativas con su coste, y la elegida con su motivo"
  - "ADR cuando la decisión es difícilmente reversible"
  - "descomposición en paquetes con orden y dependencias declaradas"
gate: gate:plan-tecnico
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "docs/arquitectura/ADR/ — decisiones arquitectónicas con su contexto y su estado"
  - "docs/arquitectura/MAPA.md — qué módulos hay, qué contratos exponen y quién los consume"
  - "CONVENTIONS.md — patrones técnicos vigentes, con su clase (a.8)"
tablero: "estado/tableros/ARQ.md — items en planificación técnica y diagnósticos abiertos"
metodos: [ARQ/Encaje, ARQ/Diagnostico]
checkpoint: "en el paquete, con el radio medido hasta ahora y las alternativas descartadas"
autoridad:
  decide_sola:
    - "la descomposición en paquetes y sus dependencias"
    - "qué alternativa técnica se elige, dentro de lo que no altera forma ni alcance"
    - "los patrones técnicos, junto a VER, con clase capability_approved (a.8)"
  escala:
    - "una decisión difícilmente reversible que compromete al producto a largo plazo"
    - "una alternativa que exige cambiar el alcance: escala a PRD"
    - "una alternativa que exige degradar la forma aprobada: escala a DIS con alternativas"
  veta: []
owner:
  nivel: ninguna
  criterio: >
    Los patrones técnicos dentro de la autoridad delegada NO son materia del Owner (a.8).
    ARQ escala al Owner sólo cuando la decisión técnica compromete el producto de forma
    difícilmente reversible, y entonces lo hace a través de PRD, con el coste traducido a
    consecuencias de producto.
roles: [ARQ/encaje, ARQ/diagnostico]
deriva_de:
  - "a.3 · ARQ: radio de impacto medido, no estimado; devolver a DIS con alternativas"
  - "b.16 · ARQ es propietario global de DEU y de DEF cuando C-ARQ"
materializacion: >
  Se materializa cuando DSP crea un paquete de ARQ. En items pequeños que no cumplen C-ARQ
  no se materializa, y la ruta lo deja escrito en `no activadas`.
retirada: >
  Los roles se retiran al depositar la capa. La memoria de arquitectura y los ADR persisten
  siempre: son la fuente que evita volver a decidir lo mismo distinto.
```

```yaml ads:gate
id: gate:plan-tecnico
aplica_a: "la capa de ARQ antes de que el item pase a construcción"
comprobaciones:
  - id: radio-medido
    comprueba: "el radio de impacto es una lista de ficheros y contratos obtenida de las fuentes, con su source id"
    como: "la capa enlaza la búsqueda ejecutada y su salida, no una estimación en prosa"
    automatizable: si
  - id: contratos-declarados
    comprueba: "está escrito qué contratos, endpoints o esquemas cambian, o que no cambia ninguno"
    como: "campo presente y no ambiguo"
    automatizable: si
  - id: alternativas-con-coste
    comprueba: "hay al menos dos alternativas con su coste, salvo que sólo exista un camino y esté demostrado"
    como: "recuento de alternativas y motivo escrito cuando sólo hay una"
    automatizable: parcial
  - id: adr-cuando-corresponde
    comprueba: "si la decisión es difícilmente reversible, existe ADR con contexto, decisión y consecuencias"
    como: "enlace al ADR desde la capa"
    automatizable: si
  - id: paquetes-con-dependencias
    comprueba: "la descomposición declara orden y dependencias, y ningún paquete depende de sí mismo"
    como: "comprobación de aciclicidad sobre el grafo propuesto"
    automatizable: si
  - id: sin-decidir-forma
    comprueba: "el plan no decide nada de forma que DIS no haya aprobado"
    como: "lectura cruzada contra la especificación de DIS cuando existe"
    automatizable: parcial
evidencia:
  - "la salida de las búsquedas que produjeron el radio"
  - "las alternativas con su coste"
  - "el ADR cuando fue exigible"
  - "el grafo de paquetes propuesto"
fallo: >
  El item no pasa a construcción. Vuelve a ARQ nombrando qué falta. Un radio estimado en
  lugar de medido es el defecto característico y produce descomposiciones que se rehacen a
  mitad de la construcción.
```

Roles, métodos, prompts y composición: [`roles/`](roles/) · [`metodos/`](metodos/) ·
[`prompts/`](prompts/) · [`composicion.md`](composicion.md).
