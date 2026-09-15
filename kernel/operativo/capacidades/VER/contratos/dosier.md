# Contrato operativo — VER/dosier

Lo que convierte [`../roles/dosier.md`](../roles/dosier.md) en un dosier que dos
verificadores competentes producen igual.

```yaml ads:contrato-operativo
id: contrato:ver-dosier
rol: VER/dosier
mision_operativa: >
  Recorrer los criterios de éxito del item uno por uno sobre la capa construida y ya
  revisada, ejecutar la regresión, capturar los estados extremos, medir los presupuestos y
  entregar un dosier con veredicto por criterio y una sección de lo no comprobado, sin haber
  construido nada de lo que verifica y sin emitir un sí o un no global.
conocimientos_exigibles:
  - "los criterios de éxito de PRD del item, leídos de su entrega y no del título"
  - "cómo ejecutar la suite de regresión de la fuente y leer su salida entera"
  - "qué evidencia puede juzgar un humano sin ejecutar nada: captura, grabación, comparativa"
  - "los presupuestos y la matriz de entornos del pack instalado"
entradas_obligatorias:
  - que: "la entrega de CNS/implementacion con su commit y su rama, y el dictamen de CNS/revision-de-construccion"
    donde: "los handoffs emitidos a este paquete y las entregas previas del item"
    si_falta: devolver
  - que: "los criterios de éxito de PRD, cada uno con su forma de comprobación"
    donde: "la entrega de PRD/criterio-de-exito del item"
    si_falta: devolver
  - que: "un entorno donde ejecutar la regresión sobre la revisión entregada"
    donde: "el workspace del producto o la matriz del pack"
    si_falta: bloquear
comprobaciones_previas:
  - id: capa-revisada
    comprueba: "el commit que voy a verificar es el que la revisión de construcción dictaminó superado"
    como: "cruce del commit de la entrega de CNS con el sobre_paquete del dictamen de revisión"
    si_falla: devolver
  - id: criterios-verificables
    comprueba: "cada criterio de éxito dice cómo se comprueba; ninguno es una intención"
    como: "lectura de cada criterio buscando su forma de comprobación"
    si_falla: devolver
  - id: no-soy-el-autor
    comprueba: "no he construido ni revisado nada de lo que voy a verificar"
    como: "comparación del titular de las entregas previas del item con el mío"
    si_falla: escalar
secuencia:
  - n: 1
    hace: "Acusar o rechazar los handoffs recibidos recorriendo sus comprobaciones al recibir"
    produce: "acuses o rechazos con las comprobaciones anotadas"
    termina_cuando: "ningún handoff emitido a este paquete queda sin acusar ni rechazar"
    checkpoint: true
  - n: 2
    hace: "Verificar cada criterio de éxito por separado sobre la revisión entregada, anotando la evidencia"
    produce: "tabla criterio → método → evidencia → veredicto"
    termina_cuando: "cada criterio tiene su veredicto propio, sin agregar"
    checkpoint: true
  - n: 3
    hace: "Ejecutar la regresión completa, y la visual cuando hay superficie"
    produce: "salida de la regresión con su resultado"
    termina_cuando: "la regresión terminó y su salida está leída entera"
    checkpoint: true
  - n: 4
    hace: "Capturar los estados extremos con datos reales y medir los presupuestos del pack"
    produce: "capturas de los estados extremos y tabla de presupuestos medidos"
    termina_cuando: "cada estado extremo tiene captura o consta por qué no la tiene, y cada presupuesto su medida"
    checkpoint: true
  - n: 5
    hace: "Escribir la sección de no comprobado y recorrer las comprobaciones del gate para emitir el dictamen; si un criterio está en rojo, la entrega es una devolución con los cuatro campos de C5"
    produce: "el dosier con el dictamen de gate:evidencia-suficiente, o la devolución"
    termina_cuando: "las comprobaciones del gate están anotadas y el dictamen tiene un valor"
    checkpoint: true
fuentes_a_consultar:
  - "la entrega de PRD/criterio-de-exito del item"
  - "docs/verificacion/COBERTURA.md y docs/verificacion/REGRESIONES.md"
  - "los presupuestos y la matriz de entornos del pack instalado"
artefactos:
  - tipo: dosier
    nombre: veredicto por criterio
    estructura_minima:
      - "una fila por criterio de éxito: criterio, método, evidencia enlazada, veredicto"
      - "la sección de no comprobado, aunque esté vacía y lo diga"
    obligatorio: true
  - tipo: salida-de-orden
    nombre: salida de la regresión
    estructura_minima:
      - "la orden ejecutada y su salida completa, con el código de salida"
    obligatorio: true
  - tipo: medicion
    nombre: presupuestos medidos
    estructura_minima:
      - "una fila por presupuesto del pack: presupuesto, medida, dentro o fuera"
    obligatorio: true
evidencias_requeridas:
  - que: "cada criterio se verificó por separado"
    forma: "la tabla del dosier con una fila por criterio de la entrega de PRD"
    quien_la_puede_juzgar: "el propietario global, cruzando la tabla con los criterios"
  - que: "la regresión se ejecutó sobre la revisión entregada"
    forma: "la salida de la orden con el commit nombrado"
    quien_la_puede_juzgar: "cualquiera con acceso a la fuente, repitiendo la orden"
criterios_de_calidad_medibles:
  - criterio: "cobertura de criterios"
    como_se_mide: "cien por cien de los criterios de la entrega de PRD tienen fila y veredicto"
  - criterio: "evidencia juzgable"
    como_se_mide: "cada veredicto enlaza una captura, una salida o una medida, no una afirmación"
  - criterio: "no comprobado declarado"
    como_se_mide: "la sección existe y cada criterio sin evidencia aparece en ella"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas y el dictamen emitido"
  - "tabla de criterios completa, regresión ejecutada y presupuestos medidos"
  - "sección de no comprobado presente"
condiciones_de_devolucion:
  - "un criterio en rojo con evidencia: se devuelve a CNS con los cuatro campos"
  - "un criterio no verificable tal como está escrito: se devuelve a PRD"
  - "la capa entregada no es la que la revisión dictaminó: se rechaza al recibir"
reglas_de_escalado:
  - cuando: "CNS sostiene que cumple y la evidencia dice lo contrario por segunda vez"
    a_quien: "DSP, freno de a.7"
    con_que: "las dos posturas y la evidencia"
  - cuando: "un criterio exige el juicio del Owner"
    a_quien: "la cola de validación por lotes del Owner"
    con_que: "la evidencia que él pueda juzgar, no la pregunta"
  - cuando: "resulto ser el autor o el revisor de lo verificado"
    a_quien: "DSP, para reasignar el rol"
    con_que: "la coincidencia de titulares"
incompatibilidades:
  - "no comparte trabajador con CNS/implementacion ni con CNS/revision-de-construccion en el mismo item"
actuaciones_prohibidas:
  - "emitir un veredicto global sin la tabla por criterio"
  - "redefinir un criterio para que la evidencia encaje"
  - "omitir del dosier lo que no se pudo comprobar"
  - "corregir lo que encuentra en la rama verificada"
  - "dar por ejecutada una regresión cuya salida no se leyó entera"
ejemplo_bueno: >
  El verificador toma los cinco criterios de la entrega de PRD, ejecuta la regresión sobre
  el commit dictaminado y lee sus 214 líneas, captura los cinco estados extremos con datos
  del tenant de laboratorio y mide los dos presupuestos del pack. Cuatro criterios en verde
  con su captura; el quinto exige el juicio del Owner y va a la cola con su grabación. La
  sección de no comprobado dice que el entorno móvil de la matriz no estaba disponible.
ejemplo_malo: >
  El verificador abre la PR, ve que la CI está en verde, prueba a mano la pantalla principal
  con el caso feliz, escribe «verificado, funciona» y emite superado. No hay tabla, no hay
  estados extremos, nadie midió nada y lo que no se comprobó no existe para nadie.
checklist:
  - id: acuse-antes
    pregunta: "¿He acusado o rechazado cada handoff recibido recorriendo sus comprobaciones?"
    automatizable: si
  - id: criterio-a-criterio
    pregunta: "¿Cada criterio de la entrega de PRD tiene su fila con veredicto propio?"
    automatizable: si
  - id: regresion-leida
    pregunta: "¿He ejecutado la regresión sobre el commit dictaminado y leído su salida entera?"
    automatizable: si
  - id: extremos-y-presupuestos
    pregunta: "¿He capturado los estados extremos y medido los presupuestos, o dicho por qué no?"
    automatizable: parcial
  - id: no-comprobado
    pregunta: "¿La sección de no comprobado existe y nombra lo que falta?"
    automatizable: si
  - id: no-construi
    pregunta: "¿No he construido ni revisado nada de lo que verifico?"
    automatizable: si
```
