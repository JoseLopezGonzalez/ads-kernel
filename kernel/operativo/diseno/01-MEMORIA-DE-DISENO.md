# La memoria de Diseño

<!-- ads-lint: permitir-vocabulario-prohibido -->

> Catálogo. Contiene bloques `ads:memoria`, uno por sección del corpus.

Sin memoria, cada pantalla se decide de nuevo y el producto acaba siendo la suma de
decisiones sin relación entre sí — que es literalmente la definición de *incoherente*, uno
de los diez motivos de rechazo.

`DIS` tiene **condición de entrada** —consultar la memoria— y **salida obligatoria** —
memoria actualizada con lo decidido **y con lo descartado y su porqué** (a.3).

## Las tres capas, y qué va en cada una

```text
KERNEL    lo que es cierto en CUALQUIER producto con interfaz.
          Principios de composición, qué significa jerarquía, cómo se juzga la calidad.
          No contiene un solo valor concreto: ni un color, ni una fuente, ni un número.

PACK      lo que es cierto en TODA UNA CLASE de producto.
          Un reloj no se lee igual que una hoja de cálculo. Rangos, límites físicos,
          mínimos de contraste, tamaños de objetivo táctil, patrones propios del medio.

PROFILE   lo que es cierto en ESTE producto y en ningún otro.
          La visión artística, la personalidad, la paleta, la tipografía, los patrones
          aprobados, las decisiones, la deuda visual y el historial.
```

**Prueba de capa** (K0.10 aplicado a diseño): *si sustituyo mentalmente este producto por
una CLI de facturación, ¿la regla sigue siendo cierta?* Sí → kernel. *¿Y por otro producto
de la misma clase?* Sí → pack. Sólo aquí → profile.

> El error característico es escribir en el kernel una preferencia del Owner. «Preferimos
> la tipografía de palo seco» **no** es un principio universal: es una decisión de este
> producto.

## Ubicación física

```text
kernel/operativo/diseno/                       la capa kernel: este directorio
packs/<clase>/diseno/                          la capa pack
<proyecto>/docs/diseno/                        la capa profile — la memoria viva
    ├─ 00-VISION.md            visión artística, personalidad, emociones
    ├─ 01-PRINCIPIOS.md        principios visuales de ESTE producto
    ├─ 02-REFERENCIAS.md       referencias y antirreferencias, con principio extraído
    ├─ 03-SISTEMA.md           tipografía, color, composición, ritmo, espaciado
    ├─ 04-MATERIA.md           iconografía, ilustración, fotografía, profundidad, textura
    ├─ 05-MOVIMIENTO.md        transiciones, microinteracciones, sonido, vibración
    ├─ 06-ADAPTACION.md        responsive, densidad, accesibilidad
    ├─ 07-COMPONENTES.md       componentes, patrones, estados y excepciones
    ├─ 08-DECISIONES.md        qué se decidió, qué se descartó y por qué
    ├─ 09-PREMIUM.md           áreas donde se invierte más, y por qué
    ├─ 10-DEUDA.md             deuda de diseño conocida y aceptada
    └─ 11-HISTORIAL.md         qué se aprendió, qué se revirtió, qué envejeció
```

---

## Las doce secciones del corpus

```yaml ads:memoria
id: memoria:vision-artistica
nombre: Visión artística, personalidad y emociones
capacidad: DIS
capa: profile
fichero: "docs/diseno/00-VISION.md"
autoridad: "Owner, sobre la visión y la personalidad. DIS/direccion-artistica la formula y la mantiene."
contiene:
  - "qué quiere ser este producto y qué NO quiere ser, en palabras del Owner"
  - "la personalidad en tres a cinco adjetivos, cada uno con su contraejemplo"
  - "las emociones buscadas en los tres momentos clave: primer contacto, uso diario, error"
  - "qué haría que el producto dejara de ser reconocible"
se_actualiza_cuando:
  - "DIS/Fundacion la escribe por primera vez con el Owner"
  - "un item DIR cambia la dirección y el Owner aprueba la nueva"
se_consulta_en:
  - "el paso 1 de todo método de DIS, sin excepción"
  - "el gate de excelencia visual, para juzgar si una propuesta es de este producto"
caducidad: "no caduca por tiempo. La sustituye una decisión DIR aprobada por el Owner."
vacio_significa: >
  el producto NO tiene dirección visual. Cualquier trabajo de superficie que se haga
  antes de llenarla produce deuda de diseño, y el encuadre DEBE declararlo.
```

```yaml ads:memoria
id: memoria:principios-visuales
nombre: Principios visuales del producto
capacidad: DIS
capa: profile
fichero: "docs/diseno/01-PRINCIPIOS.md"
autoridad: "DIS/direccion-artistica. El Owner los aprueba la primera vez (a.8)."
contiene:
  - "entre tres y siete principios, cada uno enunciado como una decisión, no como un deseo"
  - "por cada principio: qué obliga a hacer, y qué prohíbe"
  - "el conflicto entre principios resuelto por orden de prioridad escrito"
se_actualiza_cuando:
  - "una exploración descubre que un principio no se sostiene en un caso real"
  - "el sistema de diseño incorpora un patrón que exige un principio nuevo"
se_consulta_en:
  - "la fase convergente de toda exploración: los principios son el criterio de comparación"
  - "la crítica visual: un rechazo cita el principio incumplido"
caducidad: "un principio que no ha decidido nada en tres items consecutivos se revisa."
vacio_significa: "las direcciones no pueden compararse entre sí más que por gusto."
```

```yaml ads:memoria
id: memoria:referencias
nombre: Referencias y antirreferencias
capacidad: DIS
capa: profile
fichero: "docs/diseno/02-REFERENCIAS.md"
autoridad: "DIS/investigacion-visual"
contiene:
  - "por cada referencia: enlace, autor, fecha de captura y PRINCIPIO EXTRAÍDO"
  - "qué se toma y qué NO se toma de cada una"
  - "antirreferencias: qué no queremos parecer, con el motivo"
  - "la reacción del Owner a cada referencia mostrada, en sus palabras"
se_actualiza_cuando:
  - "se muestra una referencia al Owner y reacciona"
  - "una exploración usa una referencia nueva"
  - "se detecta que el producto se está pareciendo a una antirreferencia"
se_consulta_en:
  - "el paso de investigación de toda exploración divergente"
  - "el método de maduración de ENC, cuando hay que enseñar en vez de preguntar"
caducidad: >
  una referencia con más de dieciocho meses se marca para revalidar antes de volver a
  usarse como argumento de actualidad. Sigue valiendo como principio.
vacio_significa: "la exploración partirá de la memoria del modelo, que es material no comprobable."
```

```yaml ads:memoria
id: memoria:sistema-visual
nombre: Tipografía, color, composición, ritmo y espaciado
capacidad: DIS
capa: profile
fichero: "docs/diseno/03-SISTEMA.md"
autoridad: "DIS/sistema-de-diseno, con DIS/diseno-visual como productor de las decisiones"
contiene:
  - "escala tipográfica completa: familias, pesos, tamaños, interlineado y para qué sirve cada nivel"
  - "sistema de color: roles semánticos, no nombres de color; contraste comprobado por par"
  - "rejilla y composición: columnas, márgenes, anchos máximos de lectura"
  - "ritmo y espaciado: la unidad base y sus múltiplos permitidos; qué está prohibido"
  - "densidad: cuántos elementos por zona, y qué se atenúa cuando aumenta"
se_actualiza_cuando:
  - "se aprueba una dirección visual"
  - "un caso nuevo exige un nivel de la escala que no existía"
  - "una revisión de consistencia encuentra un valor usado fuera del sistema"
se_consulta_en:
  - "todo trabajo de superficie, antes de escribir un solo valor"
  - "la revisión de fidelidad: los valores construidos se comparan contra los declarados"
caducidad: "no caduca. Se sustituye por versión, conservando la anterior enlazada."
vacio_significa: "cada pantalla inventará sus propios valores y el producto será incoherente por construcción."
```

```yaml ads:memoria
id: memoria:materia
nombre: Iconografía, ilustración, fotografía, profundidad y textura
capacidad: DIS
capa: profile
fichero: "docs/diseno/04-MATERIA.md"
autoridad: "DIS/direccion-artistica"
contiene:
  - "iconografía: familia, grosor, tamaño de rejilla, qué se icona y qué no"
  - "ilustración y fotografía: si las hay, con qué tratamiento y qué proscribe"
  - "profundidad: cómo se expresa la elevación — sombra, capa, borde, desenfoque — y su escala"
  - "materiales y texturas: qué superficie tiene el producto, si tiene alguna"
se_actualiza_cuando:
  - "se introduce un icono, ilustración o tratamiento que no existía"
  - "la crítica visual detecta dos tratamientos distintos para el mismo tipo de elemento"
se_consulta_en:
  - "toda superficie que introduzca elementos gráficos"
caducidad: "no caduca por tiempo. La revisa una decisión de dirección."
vacio_significa: "los elementos gráficos se elegirán uno a uno, y no formarán familia."
```

```yaml ads:memoria
id: memoria:movimiento
nombre: Movimiento, transiciones y microinteracciones
capacidad: DIS
capa: profile
fichero: "docs/diseno/05-MOVIMIENTO.md"
autoridad: "DIS/movimiento"
contiene:
  - "por cada transición: disparador, duración, curva, qué se mueve y qué permanece"
  - "microinteracciones: qué acusa recibo de qué acción del usuario"
  - "sonido y vibración cuando el medio los admite, con su significado"
  - "el estado REDUCIDO obligatorio: qué ocurre cuando el usuario pide menos movimiento"
  - "qué NO se anima nunca, y por qué"
se_actualiza_cuando:
  - "se define una transición o microinteracción nueva"
  - "una prueba en dispositivo real demuestra que una duración no funciona en ese hardware"
se_consulta_en:
  - "todo trabajo con transición, estado o respuesta a una acción"
  - "la revisión de fidelidad, comparando grabaciones contra lo especificado"
caducidad: "una curva o duración validada en un dispositivo se revalida al cambiar de clase de dispositivo."
vacio_significa: >
  el producto no acusará recibo de las acciones del usuario: es el motivo de rechazo
  «sin respuesta» de la rúbrica.
```

```yaml ads:memoria
id: memoria:adaptacion
nombre: Responsive, densidad y accesibilidad
capacidad: DIS
capa: profile
fichero: "docs/diseno/06-ADAPTACION.md"
autoridad: "DIS/diseno-interaccion, con veto de la rúbrica de usabilidad"
contiene:
  - "los puntos de adaptación reales del producto, derivados del contenido, no de dispositivos de moda"
  - "qué cambia en cada uno: composición, densidad, navegación, tamaño de objetivo"
  - "criterios de accesibilidad exigidos, con su nivel y su método de comprobación"
  - "comportamiento con texto ampliado y con contraste aumentado"
se_actualiza_cuando:
  - "un caso real rompe una adaptación declarada"
  - "el pack de la clase de proyecto añade un entorno nuevo"
se_consulta_en:
  - "todo trabajo de superficie"
  - "el gate de usabilidad"
caducidad: "se revalida cuando la matriz de entornos del pack cambia."
vacio_significa: "la adaptación se improvisará por pantalla y fallará en los extremos."
```

```yaml ads:memoria
id: memoria:componentes
nombre: Componentes, patrones, estados y excepciones
capacidad: DIS
capa: profile
fichero: "docs/diseno/07-COMPONENTES.md"
autoridad: "DIS/sistema-de-diseno"
contiene:
  - "por cada componente: para qué sirve, qué estados tiene y cuál es su alcance"
  - "los cinco estados obligatorios de todo componente con datos: vacío, cargando, error, mínimo, máximo"
  - "patrones aprobados con su clase (a.8), su alcance y sus criterios comprobables"
  - "excepciones autorizadas: dónde el producto se sale del sistema a propósito, y por qué"
se_actualiza_cuando:
  - "se aprueba un componente o patrón nuevo"
  - "una excepción se repite tres veces: deja de ser excepción y se incorpora o se elimina"
se_consulta_en:
  - "el paso 1 de DIS/Evolucion: ¿existe patrón que cubra este caso?"
  - "la crítica visual y la revisión de fidelidad"
caducidad: "un patrón declara su condición de caducidad en su propia ficha (a.8)."
vacio_significa: "cada superficie construirá sus propios componentes y la inconsistencia será estructural."
```

```yaml ads:memoria
id: memoria:decisiones-de-diseno
nombre: Decisiones tomadas y descartadas
capacidad: DIS
capa: profile
fichero: "docs/diseno/08-DECISIONES.md"
autoridad: "la capacidad o el Owner que tomó cada decisión; DIS la registra"
contiene:
  - "qué se decidió, cuándo, quién tuvo autoridad y sobre qué alcance"
  - "QUÉ SE DESCARTÓ Y POR QUÉ — obligatorio por a.3"
  - "qué decisión sustituye a cuál, cuando las hay"
  - "las palabras literales del Owner cuando la decisión fue suya"
se_actualiza_cuando:
  - "toda fase convergente de todo método de DIS, sin excepción"
  - "el Owner decide en materia de forma"
se_consulta_en:
  - "toda exploración, para no volver a proponer lo ya descartado"
  - "el anclaje de ENC, cuando la expresión toca una superficie"
caducidad: "las decisiones no caducan: se sustituyen, dejando la anterior enlazada."
vacio_significa: >
  el sistema volverá a proponer lo que ya se rechazó, que es el modo de fallo (a) de a.7
  aplicado al diseño.
```

```yaml ads:memoria
id: memoria:areas-premium
nombre: Áreas premium
capacidad: DIS
capa: profile
fichero: "docs/diseno/09-PREMIUM.md"
autoridad: "Owner"
contiene:
  - "qué superficies concentran la diferencia del producto y merecen más profundidad"
  - "por cada una: por qué es premium y qué nivel de acabado se exige"
  - "qué superficies son explícitamente NO premium, y qué significa eso en la práctica"
se_actualiza_cuando:
  - "el Owner declara una superficie premium"
  - "el uso real demuestra que una superficie concentra más valor del previsto"
se_consulta_en:
  - "la escala de novedad, para decidir cuánta exploración exige un trabajo"
  - "la composición del equipo de DIS"
caducidad: "se revisa cuando el uso real contradice la lista."
vacio_significa: >
  todas las superficies reciben el mismo tratamiento. NO significa que alguna pueda
  hacerse por debajo del mínimo: el mínimo del kernel se aplica a todas.
```

```yaml ads:memoria
id: memoria:deuda-de-diseno
nombre: Deuda de diseño
capacidad: DIS
capa: profile
fichero: "docs/diseno/10-DEUDA.md"
autoridad: "DIS/sistema-de-diseno la registra; sólo el Owner la acepta indefinidamente"
contiene:
  - "qué se construyó por debajo de la intención, dónde, y qué se sacrificó"
  - "por qué se aceptó: la restricción concreta que lo obligó"
  - "qué la salda: el trabajo concreto que la eliminaría"
  - "qué empeora si no se salda"
se_actualiza_cuando:
  - "la revisión de fidelidad acepta una simplificación con motivo"
  - "se construye una superficie sin dirección aprobada"
  - "se salda una deuda registrada"
se_consulta_en:
  - "el encuadre de todo item que toque una superficie con deuda registrada"
  - "la revisión de consistencia de DIS/Evolucion"
caducidad: "la deuda no caduca: se salda o se acepta por decisión escrita del Owner."
vacio_significa: "no hay deuda registrada, lo que sólo es cierto si nadie ha simplificado nunca."
```

```yaml ads:memoria
id: memoria:historial-de-diseno
nombre: Historial y aprendizaje de diseño
capacidad: DIS
capa: profile
fichero: "docs/diseno/11-HISTORIAL.md"
autoridad: "DIS/direccion-artistica, con APR como consumidor"
contiene:
  - "qué se probó y no funcionó, con la evidencia de por qué"
  - "qué se revirtió y qué lo motivó"
  - "qué envejeció: decisiones que fueron correctas y dejaron de serlo"
  - "qué reacciones del Owner se repiten, en sus palabras"
se_actualiza_cuando:
  - "una dirección se descarta tras haberse construido"
  - "el uso real contradice una decisión de forma"
  - "el Owner reacciona igual ante dos propuestas distintas"
se_consulta_en:
  - "el paso de investigación de DIS/Fundacion y DIS/Reconstruccion"
  - "el ledger de aprendizaje, cuando APR promueve una regla"
caducidad: "no caduca: es histórico."
vacio_significa: "el equipo repetirá los errores que ya cometió, sin saberlo."
```

---

## Regla de entrada y de salida de DIS

```text
ENTRADA   ningún método de DIS empieza sin haber leído la memoria que su método declara
          en `carga`. Empezar sin leerla produce lo ya descartado, otra vez.

SALIDA    ningún paquete de DIS cierra sin haber escrito en la memoria:
            [ ] lo decidido
            [ ] LO DESCARTADO Y SU PORQUÉ          ← obligatorio por a.3
            [ ] los patrones nuevos, con clase, alcance y criterios comprobables
            [ ] la deuda de diseño aceptada, si la hubo
          Es una comprobación del gate, no un buen hábito.
```
