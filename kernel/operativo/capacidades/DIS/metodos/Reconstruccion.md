# DIS/Reconstruccion — reconstruir la dirección de un producto existente

Para un producto **ya construido cuya dirección visual no está escrita en ninguna parte**.
Existe porque es el caso real de la mayoría de los proyectos que llegan a esta
organización, incluido el que motivó este kernel.

> La regla que gobierna este método: **conservar lo valioso**. Un producto en uso contiene
> decisiones acertadas que nadie escribió, y tirarlas por no reconocerlas es la forma más
> cara de empezar de cero.

```yaml ads:metodo
id: DIS/Reconstruccion
nombre: Reconstruccion
capacidad: DIS
disparador:
  - "la escala de novedad devuelve N3: hay producto o superficie real y la memoria de diseño falta, no es fiable, está obsoleta o no representa lo implementado"
  - "un item AUD de auditoría activa DIS/Reconstruccion por C-DIS"
carga:
  - "el producto construido, ejecutable"
  - "el código de las superficies y de los componentes"
  - "el historial de control de versiones de las superficies"
  - "la memoria de diseño, si existe algo"
  - "los items cerrados que produjeron cada superficie, con su traza de ruta"
preguntas_iniciales:
  - "¿cuántas superficies hay realmente, y cuáles usa alguien?"
  - "¿qué decisiones se repiten en todas ellas? — eso es el sistema no escrito"
  - "¿qué se hizo a propósito y qué salió así?"
pasos:
  - n: 1
    nombre: INVENTARIO
    modo: lineal
    hace: >
      Enumerar TODAS las superficies del producto, no las principales: las de error, las
      vacías, las de impresión, las de configuración. Con su ruta en el código y con quién
      las usa.
    produce: "inventario de superficies con ruta y uso"
    termina_cuando: "no queda superficie alcanzable desde la navegación sin inventariar"
    checkpoint: true
  - n: 2
    nombre: CAPTURAS
    modo: lineal
    hace: >
      Capturar cada superficie en cada entorno de la matriz del pack, con datos reales, y
      en sus cinco estados cuando el estado es alcanzable.
    produce: "corpus de capturas fechadas"
    termina_cuando: "toda superficie del inventario tiene captura en cada entorno declarado"
    checkpoint: true
  - n: 3
    nombre: EXTRACCIÓN DE PATRONES REALES
    modo: convergente
    hace: >
      Extraer del código y de las capturas los valores realmente usados: tipografías,
      tamaños, colores, espaciados, radios, elevaciones, duraciones. Contarlos.
    produce: "tabla de valores usados con su frecuencia y dónde aparecen"
    termina_cuando: >
      cada valor está contado y localizado, y se distingue el valor dominante del valor
      residual en cada dimensión
    checkpoint: true
  - n: 4
    nombre: INCONSISTENCIAS
    modo: convergente
    hace: >
      Localizar dónde el producto resuelve lo mismo de dos formas distintas, y dónde un
      valor residual contradice al dominante.
    produce: "lista de inconsistencias con su evidencia"
    termina_cuando: "cada inconsistencia tiene las dos formas capturadas lado a lado"
    checkpoint: true
  - n: 5
    nombre: INTENCIONAL FRENTE A ACCIDENTAL
    modo: convergente
    hace: >
      Por cada patrón y cada inconsistencia, determinar si fue decisión o accidente. La
      evidencia sale del historial de control de versiones, de los items que la produjeron
      y, cuando no basta, de una pregunta al Owner.
    produce: "clasificación de cada patrón: intencional, accidental o indeterminado"
    termina_cuando: >
      todo patrón dominante está clasificado, y los indeterminados están en la lista de
      preguntas al Owner
    checkpoint: true
  - n: 6
    nombre: DEUDA VISUAL
    modo: convergente
    hace: >
      Registrar como deuda todo lo accidental que empeora el producto, con qué la saldaría
      y qué empeora si no se salda.
    produce: "registro de deuda de diseño con sus cuatro campos por entrada"
    termina_cuando: "toda inconsistencia accidental está registrada o descartada por irrelevante"
    checkpoint: true
  - n: 7
    nombre: RECONSTRUCCIÓN DE LA DIRECCIÓN
    modo: convergente
    hace: >
      Escribir la dirección que el producto TIENE, no la que debería tener: qué
      personalidad transmite hoy, con qué principios implícitos, y qué conserva de valioso.
    produce: "dirección reconstruida, con lo valioso identificado"
    termina_cuando: >
      la dirección reconstruida explica al menos el ochenta por ciento de los patrones
      dominantes clasificados como intencionales
    checkpoint: true
  - n: 8
    nombre: CONTRASTE CON EL OWNER
    modo: conversacional
    hace: >
      Enseñar al Owner la dirección reconstruida y la deuda, y recoger qué reconoce como
      querido y qué como accidente que nunca le gustó.
    produce: "reacción del Owner a la reconstrucción, citada"
    termina_cuando: "el Owner ha confirmado o corregido lo que se conserva como valioso"
    checkpoint: true
  - n: 9
    nombre: PROPUESTA DE EVOLUCIÓN
    modo: divergente
    hace: >
      Producir al menos DOS propuestas de evolución que conserven lo valioso y resuelvan la
      deuda, con lo que cada una cuesta y lo que cada una gana.
    produce: "dos o más propuestas de evolución comparadas"
    termina_cuando: >
      cada propuesta declara qué conserva, qué cambia, qué deuda salda y qué esfuerzo de
      construcción implica
    checkpoint: true
  - n: 10
    nombre: CORPUS INICIAL
    modo: lineal
    hace: >
      Escribir el corpus de diseño con lo reconstruido: sistema realmente usado, componentes
      existentes, patrones con su alcance real, deuda registrada e historial.
    produce: "memoria de diseño inicial del producto existente"
    termina_cuando: "las secciones que aplican del corpus están escritas y el sistema declarado corresponde al código"
    checkpoint: true
artefactos:
  - "inventario de superficies"
  - "corpus de capturas fechadas por entorno y estado"
  - "tabla de valores usados con frecuencia"
  - "lista de inconsistencias con evidencia"
  - "clasificación intencional/accidental"
  - "registro de deuda visual"
  - "dirección reconstruida"
  - "dos o más propuestas de evolución"
puntos_owner:
  - "paso 5: preguntas sobre los patrones indeterminados, agrupadas en un solo lote (G36)"
  - "paso 8: contraste de la reconstrucción — obligatorio, es dirección de producto"
consultas:
  - "ARQ: ¿qué superficies comparten componente en el código? Responde con la lista de ficheros"
  - "USO: ¿qué superficies se usan de verdad y con qué frecuencia? Responde con telemetría o con la observación disponible"
checkpoints:
  - "tras cada uno de los diez pasos"
  - "antes de preguntar al Owner por los patrones indeterminados"
critica:
  - "¿el inventario incluye las superficies feas: errores, vacíos, configuración?"
  - "¿se ha confundido «frecuente» con «intencional»? Un error repetido sigue siendo un error"
  - "¿se conserva lo valioso, o se ha reconstruido lo que el equipo habría preferido?"
  - "¿las dos propuestas de evolución son distintas, o una es la otra con menos esfuerzo?"
gate: gate:excelencia-visual
salida:
  - "dirección reconstruida y confirmada por el Owner"
  - "memoria de diseño inicial del producto existente"
  - "registro de deuda visual"
  - "propuestas de evolución, que continúan como items enlazados"
devolucion:
  - "a ENC, cuando el encuadre pedía rediseñar y lo que hace falta es reconstruir primero"
bloqueo:
  - "el producto no es ejecutable y no se pueden capturar sus superficies"
  - "no hay acceso al historial de control de versiones y lo intencional no es distinguible de lo accidental"
cancelacion:
  - "el Owner decide fundar una dirección nueva desde cero: el método pasa a DIS/Fundacion y la reconstrucción se conserva como material"
aprendizaje:
  - "los patrones accidentales frecuentes señalan qué le falta al sistema para gobernar"
  - "toda superficie construida sin activar DIS se registra como aprendizaje de ruta para APR"
prueba_de_reanudacion: >
  Un agente nuevo abre el paquete, lee el inventario y las capturas ya hechas, y continúa
  por las superficies que faltan sin recapturar las registradas. Es la prueba T94.
```
