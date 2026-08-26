# Las dos rúbricas y sus dos gates

<!-- ads-lint: permitir-vocabulario-prohibido -->

Una rúbrica **no es una nota**. Es una lista de ejes, cada uno con tres niveles descritos
en palabras y con la evidencia que permite situarse en uno de ellos. El resultado de
aplicarla es un **dictamen**, no una puntuación.

```text
LA RÚBRICA ORDENA EL JUICIO. NO LO SUSTITUYE.
Quien la aplica sigue teniendo que mirar, y sigue respondiendo de lo que dictamina.
```

---

## Rúbrica de usabilidad

```yaml ads:rubrica
id: rubrica:usabilidad
nombre: Usabilidad
aplica_a: "toda superficie que un humano usa, en cualquier medio"
ejes:
  - id: comprension
    eje: "Se entiende sin que nadie lo explique"
    rechazo: "un usuario del perfil declarado no sabe qué está viendo ni qué puede hacer"
    suficiente: "sabe qué está viendo y encuentra la acción principal sin ayuda"
    excelente: "el orden de lectura conduce a la acción principal sin que haya que buscarla"
    evidencia: "observación de uso real o plan de validación humana, con la tarea y el tiempo hasta encontrarla"
  - id: operabilidad
    eje: "Se puede usar con los medios del entorno"
    rechazo: "hay una acción que no puede completarse con los medios que el pack declara para ese entorno"
    suficiente: "toda acción es completable con teclado, puntero o gesto según el medio"
    excelente: "las acciones frecuentes tienen camino corto y el camino corto es descubrible"
    evidencia: "recorrido completo por cada medio de entrada declarado en el pack"
  - id: correccion
    eje: "Hace lo que dice que hace"
    rechazo: "una acción produce un resultado distinto del anunciado, o ninguno"
    suficiente: "toda acción produce el resultado anunciado y lo comunica"
    excelente: "el resultado es visible sin que el usuario tenga que comprobarlo en otro sitio"
    evidencia: "salida de tests de comportamiento y capturas del antes y el después"
  - id: estados-extremos
    eje: "Aguanta vacío, error, carga, mínimo y máximo"
    rechazo: "algún estado extremo rompe la composición, oculta información o no está resuelto"
    suficiente: "los cinco estados están resueltos y son legibles"
    excelente: "los estados extremos informan y ofrecen salida, en vez de limitarse a no romperse"
    evidencia: "captura de los cinco estados en cada superficie afectada"
  - id: accesibilidad
    eje: "Es usable con las capacidades y ajustes que el pack declara"
    rechazo: "incumple un criterio de accesibilidad declarado como exigible por el pack"
    suficiente: "cumple todos los criterios exigibles con su método de comprobación registrado"
    excelente: "funciona con texto ampliado, contraste aumentado y movimiento reducido sin perder función"
    evidencia: "comprobación automática más recorrido manual del pack correspondiente"
  - id: fluidez-percibida
    eje: "Responde cuando el usuario actúa"
    rechazo: "hay acciones sin acuse de recibo, o la espera no se comunica"
    suficiente: "toda acción acusa recibo dentro del presupuesto declarado por el pack"
    excelente: "la espera se convierte en información: el usuario sabe qué ocurre y cuánto falta"
    evidencia: "grabación con marca de tiempo entre acción y primera respuesta visible"
evidencia:
  - "capturas de los cinco estados por superficie"
  - "grabación de los recorridos principales"
  - "salida de la comprobación de accesibilidad del pack"
  - "mediciones de respuesta contra los presupuestos del pack"
umbral: >
  El gate exige `suficiente` o superior en LOS SEIS ejes. Un solo eje en `rechazo` detiene
  el tránsito, con independencia de los otros cinco. No se compensan entre sí.
juicio_humano: >
  Los ejes comprension y fluidez_percibida admiten medición parcial, pero su nivel
  `excelente` lo dictamina una persona o un plan de validación humana (G36). VER puede
  declarar `suficiente` con evidencia; NO puede declarar `excelente` sin observación real.
no_automatizable:
  - "si el orden de lectura conduce a la acción principal"
  - "si un estado extremo informa o sólo evita romperse"
  - "si la espera comunica lo que ocurre"
```

```yaml ads:gate
id: gate:usabilidad
aplica_a: "toda capa de DIS o de CON que produce o modifica una superficie usable"
comprobaciones:
  - id: seis-ejes-evaluados
    comprueba: "los seis ejes de rubrica:usabilidad tienen nivel asignado y evidencia enlazada"
    como: "recorrido de la rúbrica, eje por eje, con la evidencia de cada uno"
    automatizable: si
  - id: ninguno-en-rechazo
    comprueba: "ningún eje está en nivel rechazo"
    como: "comparación del dictamen contra la rúbrica"
    automatizable: si
  - id: cinco-estados
    comprueba: "existen capturas de vacío, error, carga, mínimo y máximo por superficie afectada"
    como: "recuento de artefactos de evidencia por superficie"
    automatizable: si
  - id: accesibilidad-del-pack
    comprueba: "los criterios de accesibilidad exigibles del pack instalado están comprobados"
    como: "salida de la comprobación automática más recorrido manual declarado por el pack"
    automatizable: parcial
  - id: medios-de-entrada
    comprueba: "cada medio de entrada declarado por el pack completa los recorridos principales"
    como: "un recorrido registrado por medio"
    automatizable: parcial
  - id: presupuestos-de-respuesta
    comprueba: "las mediciones de respuesta están dentro de los presupuestos del pack"
    como: "medición registrada frente al presupuesto declarado"
    automatizable: si
evidencia:
  - "el dictamen de usabilidad con los seis ejes"
  - "las capturas de los cinco estados"
  - "las grabaciones de recorrido por medio de entrada"
  - "la salida de accesibilidad y las mediciones de respuesta"
fallo: >
  El paquete no pasa a la siguiente capacidad. Si el fallo es de la capa de DIS, vuelve a
  DIS; si es de la construcción de una capa aprobada, vuelve a CON con la evidencia. VER
  mantiene su veto sobre el tránsito mientras haya un eje en rechazo.
```

---

## Rúbrica de excelencia visual

Los diez motivos de rechazo del sistema, convertidos en ejes evaluables.

```yaml ads:rubrica
id: rubrica:excelencia-visual
nombre: Excelencia visual
aplica_a: "toda superficie visible del producto, y el sistema de diseño en su conjunto"
ejes:
  - id: personalidad
    eje: "Es reconociblemente de este producto"
    rechazo: "quitando el logotipo, podría ser de cualquier producto de su categoría"
    suficiente: "aplica la dirección declarada y es coherente con el resto del producto"
    excelente: "alguien que conoce el producto lo reconoce por la composición, la tipografía o el ritmo"
    evidencia: "comparación lado a lado contra dos productos genéricos de la misma categoría"
  - id: intencion
    eje: "Cada decisión formal responde a una intención escrita"
    rechazo: "usa los valores por defecto de la herramienta; no hay decisión detrás de nada"
    suficiente: "las decisiones principales citan el principio o el patrón del que salen"
    excelente: "hay al menos una decisión formal deliberada que resuelve un problema real del contenido"
    evidencia: "trazado de cada decisión visual hasta su principio o su patrón en la memoria"
  - id: jerarquia
    eje: "La mirada tiene recorrido"
    rechazo: "todos los elementos pesan lo mismo; no hay dónde mirar primero"
    suficiente: "hay un elemento dominante por zona y el orden de lectura es deducible"
    excelente: "la jerarquía se sostiene con datos reales, incluidos los casos largos y los vacíos"
    evidencia: "prueba de entrecerrado sobre captura y recorrido de lectura declarado, con datos reales"
  - id: sistema
    eje: "Tipografía, color, espaciado y composición forman sistema"
    rechazo: "hay valores fuera de la escala declarada, o el mismo elemento resuelto de dos formas"
    suficiente: "todos los valores pertenecen al sistema declarado"
    excelente: "el sistema resuelve casos que no estaban previstos sin necesitar excepciones"
    evidencia: "extracción de los valores usados y comparación contra el sistema declarado"
  - id: actualidad
    eje: "No recurre a soluciones formales que dejaron de significar algo"
    rechazo: "el lenguaje visual imita convenciones que su propia categoría ya abandonó"
    suficiente: "el lenguaje visual es contemporáneo de su categoría"
    excelente: "toma una decisión formal que su categoría todavía no da por supuesta, y la sostiene"
    evidencia: "referencias con fecha de captura y qué se extrajo de cada una"
  - id: respuesta
    eje: "El producto acusa recibo de lo que el usuario hace"
    rechazo: "no hay estados, ni transiciones, ni respuesta a la interacción"
    suficiente: "los estados y transiciones declarados existen y se comportan como se especificó"
    excelente: "el movimiento explica lo que ocurre en vez de decorarlo, y desaparece bien al reducirse"
    evidencia: "grabación de cada transición y de su estado reducido"
  - id: acabado
    eje: "Calidad de ejecución en el detalle"
    rechazo: "alineaciones sueltas, espaciados arbitrarios, cortes de texto, saltos al cargar"
    suficiente: "el detalle está resuelto y no distrae"
    excelente: "el detalle premia la mirada de quien lo usa a diario"
    evidencia: "capturas a tamaño real en los entornos de la matriz del pack, con zoom en las juntas"
  - id: fidelidad
    eje: "Lo construido es lo aprobado"
    rechazo: "se simplificó una animación, un estado, una composición o un espaciado sin devolverlo"
    suficiente: "lo construido corresponde a la intención aprobada, o la diferencia está registrada como deuda aceptada"
    excelente: "lo construido mejora la intención en algún punto, y la memoria de diseño lo recoge"
    evidencia: "comparación intención/resultado del procedimiento de fidelidad"
  - id: alma
    eje: "Transmite algo"
    rechazo: "técnicamente correcto y emocionalmente mudo: no produce ninguna reacción"
    suficiente: "transmite la emoción declarada en la visión artística, al menos en la superficie principal"
    excelente: "produce una reacción en quien lo ve por primera vez, y esa reacción es la buscada"
    evidencia: "reacción registrada del Owner o de un usuario real, en sus palabras"
evidencia:
  - "capturas a tamaño real en cada entorno de la matriz del pack"
  - "grabaciones de las transiciones y de su estado reducido"
  - "extracción de valores usados frente al sistema declarado"
  - "comparación con dos productos genéricos de la misma categoría"
  - "reacción registrada del Owner o de un usuario real"
umbral: >
  El gate exige `suficiente` o superior en los NUEVE ejes, y `excelente` en al menos DOS
  cuando la superficie está declarada premium en la memoria. Un eje en `rechazo` detiene
  el tránsito aunque el gate de usabilidad esté completo.
juicio_humano: >
  Los ejes personalidad, actualidad y alma NO son medibles y no se declaran nunca por
  automatismo: los dictamina DIS/critica-visual, y su nivel `excelente` en materia de
  primera instancia de un patrón visual lo confirma el Owner (a.8). El resto de ejes
  admite evidencia objetiva, pero su lectura sigue siendo un dictamen firmado por un rol.
no_automatizable:
  - "si el producto es reconocible sin su logotipo"
  - "si una decisión formal resuelve un problema real o sólo adorna"
  - "si el lenguaje visual es contemporáneo de su categoría"
  - "si transmite la emoción declarada"
```

```yaml ads:gate
id: gate:excelencia-visual
aplica_a: "toda capa que produce o modifica superficie visible, y todo cambio del sistema de diseño"
comprobaciones:
  - id: dictamen-existe
    comprueba: "existe dictamen de DIS/critica-visual sobre este paquete"
    como: "el paquete enlaza el dictamen y el identificador del agente que lo emitió"
    automatizable: si
  - id: dictamen-independiente
    comprueba: "el agente que emitió el dictamen no ocupó ningún rol productor en este paquete"
    como: "comparación de identificadores de agente en el registro de materialización"
    automatizable: si
  - id: nueve-ejes
    comprueba: "los nueve ejes de rubrica:excelencia-visual tienen nivel y evidencia"
    como: "recorrido de la rúbrica eje por eje"
    automatizable: si
  - id: ninguno-en-rechazo
    comprueba: "ningún eje está en nivel rechazo"
    como: "comparación del dictamen contra la rúbrica"
    automatizable: si
  - id: premium
    comprueba: "si la superficie está declarada premium, al menos dos ejes están en excelente"
    como: "comparación contra memoria:areas-premium"
    automatizable: si
  - id: owner-primera-instancia
    comprueba: "si es la primera instancia de un patrón visual, artístico o de interacción, el Owner la aprobó"
    como: "el patrón declara clase owner_approved con fecha y el item que lo aprobó"
    automatizable: si
  - id: memoria-actualizada
    comprueba: "la memoria de diseño recoge lo decidido y lo descartado con su porqué"
    como: "diff de los ficheros de memoria declarados en el método"
    automatizable: si
  - id: referencias-con-principio
    comprueba: "toda referencia usada tiene enlace, fecha y principio extraído"
    como: "comprobación estructural sobre memoria:referencias"
    automatizable: si
  - id: sin-copia
    comprueba: "ninguna propuesta reproduce una obra o un estilo completo de un tercero"
    como: "el dictamen declara expresamente qué se extrajo de cada referencia y qué NO se tomó"
    automatizable: no
evidencia:
  - "el dictamen de excelencia visual con sus nueve ejes"
  - "las capturas y grabaciones que lo sostienen"
  - "el diff de la memoria de diseño"
  - "la aprobación del Owner cuando fue exigible"
fallo: >
  El paquete no pasa. Si el rechazo es de la capa de diseño, el paquete vuelve a DIS con
  el eje y su evidencia. Si el rechazo es de fidelidad, vuelve a CON. Un rechazo por
  personalidad, actualidad o alma NO se cierra con retoques: exige volver a la fase
  divergente del método correspondiente, porque el problema es de dirección, no de acabado.
```

---

## Por qué el gate visual no se puede automatizar del todo

```text
Los nueve ejes se dividen así:

AUTOMATIZABLE          sistema · acabado(parcial) · fidelidad · respuesta(parcial)
                       → se extraen valores, se comparan capturas, se miden tiempos

NO AUTOMATIZABLE       personalidad · intencion · actualidad · alma · jerarquia(parcial)
                       → exigen mirar, comparar contra la categoría y reconocer

Si el gate se cerrara sólo con lo automatizable, produciría exactamente el resultado que
el Owner rechazó: un producto que cumple todas las métricas y no tiene alma. Por eso el
juicio vive en un ROL con nombre, y el gate comprueba que ese rol se pronunció.
```

## Lo que un dictamen de excelencia visual debe contener

Se usa la plantilla común de [`DICTAMEN.md`](../plantillas/DICTAMEN.md), con dos añadidos
obligatorios propios de esta rúbrica:

```text
[ ] el NIVEL de cada uno de los nueve ejes, con su evidencia enlazada
[ ] en los ejes no automatizables, LA RAZÓN del nivel, en una frase que otro pueda discutir
    «genérica» no basta: «resuelve la tabla con los valores por defecto del framework y
    la jerarquía la crea sólo el color, que es lo que hace cualquier panel de su
    categoría» sí basta
```
