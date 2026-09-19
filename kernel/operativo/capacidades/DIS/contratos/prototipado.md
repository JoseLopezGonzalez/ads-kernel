# Contrato operativo — DIS/prototipado

Lo que convierte [`../roles/prototipado.md`](../roles/prototipado.md)
en un prototipo que valida producto antes de construir producción (§18).

```yaml ads:contrato-operativo
id: contrato:dis-prototipado
rol: DIS/prototipado
mision_operativa: >
  Entregar, para toda superficie nueva o cambio relevante, un prototipo mirable antes de
  la implementación definitiva, con contenido real o representativo, jerarquía real, las
  interacciones principales, los estados, los datos extremos, responsive, acciones,
  errores, vacíos y loading; en el formato que la tarea pida —navegable, visual,
  composición reproducible, fixture, Storybook o implementación desechable— y siempre con
  una referencia que otro pueda abrir.
conocimientos_exigibles:
  - "los formatos de prototipo que la instancia admite y cómo se referencian"
  - "los datos representativos del tenant de laboratorio y sus extremos"
  - "las interacciones principales del análisis de uso"
entradas_obligatorias:
  - que: "la recomendación de la dirección artística y la auditoría de reutilización"
    donde: "las entregas previas de DIS"
    si_falta: devolver
  - que: "datos reales o representativos"
    donde: "el tenant de laboratorio o los fixtures declarados por la instancia"
    si_falta: bloquear
comprobaciones_previas:
  - id: datos-representativos
    comprueba: "tengo datos reales o representativos, con sus extremos, antes de montar nada"
    como: "lectura del análisis de uso y del tenant de laboratorio"
    si_falla: bloquear
  - id: formato-decidido
    comprueba: "he elegido el formato por la tarea y sé cómo lo abrirá quien valide"
    como: "lectura del análisis de uso y de los formatos admitidos"
    si_falla: devolver
secuencia:
  - n: 1
    hace: "Construir el prototipo con contenido real o representativo y jerarquía real"
    produce: "prototipo"
    termina_cuando: "no hay lorem ipsum ni datos de ejemplo cómodos"
    checkpoint: true
  - n: 2
    hace: "Cubrir las interacciones principales, los estados, los datos extremos, responsive, acciones, errores, vacíos y loading"
    produce: "prototipo completo"
    termina_cuando: "los diez contenidos de §18 están resueltos"
    checkpoint: true
  - n: 3
    hace: "Publicar la referencia mirable y describirla como prototipo"
    produce: "referencia del prototipo"
    termina_cuando: "otro rol lo abre sin ayuda y la síntesis lo recoge en PROTOTIPO"
    checkpoint: true
fuentes_a_consultar:
  - "el análisis de uso y la recomendación del item"
  - "docs/diseno/ del control repo"
  - "los formatos y previews que la instancia declara (PROFILE)"
artefactos:
  - tipo: captura
    nombre: prototipo mirable
    estructura_minima:
      - "una referencia que se abre: navegable, visual, composición reproducible, fixture, Storybook o implementación desechable"
      - "contenido real o representativo y jerarquía real"
      - "interacciones principales, estados, datos extremos, responsive, acciones, errores, vacíos y loading"
    obligatorio: true
  - tipo: documento
    nombre: guion del prototipo
    estructura_minima:
      - "qué muestra cada pantalla o estado y con qué datos"
      - "qué interacciones están y cuáles no, y por qué"
    obligatorio: true
evidencias_requeridas:
  - que: "el prototipo usa contenido real o representativo"
    forma: "los datos citados y su origen"
    quien_la_puede_juzgar: "DIS/critica-visual y DIS/validacion-de-uso"
  - que: "los estados y extremos están"
    forma: "una vista por estado y por extremo"
    quien_la_puede_juzgar: "DIS/critica-visual"
criterios_de_calidad_medibles:
  - criterio: "diez contenidos"
    como_se_mide: "los diez contenidos de §18 tienen su vista"
  - criterio: "referencia mirable"
    como_se_mide: "otro rol abre la referencia sin ayuda"
condiciones_de_aceptacion:
  - "la referencia del prototipo se abre y aparece en la sección PROTOTIPO de la síntesis"
  - "las comprobaciones del gate anotadas y los dos artefactos completos"
condiciones_de_devolucion:
  - "el prototipo no cubre un estado o un extremo: se devuelve al propio prototipado"
  - "no hay recomendación de dirección: se devuelve a DIS/direccion-artistica"
reglas_de_escalado:
  - cuando: "el prototipo revela que la recomendación no funciona en uso"
    a_quien: "DIS/direccion-artistica"
    con_que: "el prototipo y el punto donde falla"
incompatibilidades:
  - "no comparte trabajador con DIS/validacion-de-uso ni con DIS/critica-visual en el mismo item"
actuaciones_prohibidas:
  - "prototipar con lorem ipsum o datos cómodos"
  - "entregar una descripción en vez de una referencia mirable"
  - "omitir el estado de error o el vacío porque «son obvios»"
ejemplo_bueno: >
  Para el diálogo de recepción, el prototipo es una preview aislada con tres recepciones
  reales, una de 200 cajas, el error de permiso, el vacío del primer día y el loading, en
  móvil y escritorio, con su guion; validación de uso lo abre y prueba crear una recepción
  sin ayuda.
ejemplo_malo: >
  Entrega un mockup con dos cajas de ejemplo y sin estados, descrito en un párrafo, que
  nadie puede abrir; Construcción inventa el error y el vacío, y el Owner los corrige uno
  a uno.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "qué formato de prototipo conviene a la tarea"
  - "qué datos representativos elige y cuáles son los extremos"
metodos:
  - DIS/Fundacion
  - DIS/Evolucion
no_autocertifica:
  - gate:usabilidad
checklist:
  - id: contenido-real
    pregunta: "¿El prototipo usa contenido real o representativo con jerarquía real?"
    automatizable: parcial
  - id: diez-contenidos
    pregunta: "¿Están las interacciones, estados, extremos, responsive, acciones, errores, vacíos y loading?"
    automatizable: si
  - id: mirable
    pregunta: "¿Otro rol puede abrir la referencia sin ayuda?"
    automatizable: parcial
  - id: formato-por-la-tarea
    pregunta: "¿He elegido el formato por lo que la tarea necesita validar?"
    automatizable: no
  - id: guion
    pregunta: "¿El guion dice qué muestra cada vista y con qué datos?"
    automatizable: si
```
