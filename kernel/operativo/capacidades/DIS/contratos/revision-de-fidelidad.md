# Contrato operativo — DIS/revision-de-fidelidad

Lo que convierte [`../roles/revision-de-fidelidad.md`](../roles/revision-de-fidelidad.md)
en una comparación que dos revisores competentes hacen igual.

```yaml ads:contrato-operativo
id: contrato:dis-revision-de-fidelidad
rol: DIS/revision-de-fidelidad
mision_operativa: >
  Comparar, con contexto limpio, la especificación aprobada con lo construido —en estático,
  en cada estado, en movimiento y en dispositivo real cuando el pack lo exige— y emitir el
  veredicto de fidelidad con la evidencia de cada diferencia delante, sin haber
  especificado ni construido lo que se compara.
conocimientos_exigibles:
  - "las ocho cosas que no se simplifican en silencio, y cómo se ven cuando faltan"
  - "cómo extraer los valores realmente usados de lo construido y compararlos con el sistema"
  - "la matriz de entornos y dispositivos del pack instalado"
  - "la diferencia entre una diferencia con lo aprobado y una preferencia propia"
entradas_obligatorias:
  - que: "la especificación aprobada con su versión, de DIS/diseno-visual"
    donde: "la entrega previa del item, enlazada desde el brief"
    si_falta: devolver
  - que: "lo construido, con su commit exacto y su rama"
    donde: "la entrega de CNS/implementacion, en el handoff a este paquete"
    si_falta: devolver
  - que: "un entorno donde ejecutar lo construido en la revisión entregada"
    donde: "el workspace del producto o la matriz del pack"
    si_falta: bloquear
comprobaciones_previas:
  - id: contexto-limpio
    comprueba: "no he especificado ni construido nada de lo que voy a comparar"
    como: "comparación de los titulares de las entregas previas del item con el mío"
    si_falla: escalar
  - id: commit-ejecutable
    comprueba: "el commit nombrado existe y arranca en el entorno declarado"
    como: "git rev-parse y arranque de la aplicación sobre esa revisión"
    si_falla: devolver
  - id: deuda-previa
    comprueba: "sé qué deuda se acordó ANTES de construir distinto, y no acepto ninguna otra"
    como: "lectura de docs/diseno/10-DEUDA.md y de las diferencias declaradas de CNS"
    si_falla: devolver
secuencia:
  - n: 1
    hace: "Acusar o rechazar el handoff de Construcción recorriendo sus comprobaciones al recibir"
    produce: "acuse o rechazo"
    termina_cuando: "el handoff está acusado o rechazado"
    checkpoint: true
  - n: 2
    hace: "Comparar cada superficie en estático, lado a lado, en escritorio y en móvil"
    produce: "comparación estática por superficie y tamaño"
    termina_cuando: "cada superficie tiene su par especificación/construido con las diferencias marcadas"
    checkpoint: true
  - n: 3
    hace: "Comparar los cinco estados obligatorios con datos reales, en ambas columnas"
    produce: "comparación por estado"
    termina_cuando: "cada estado está comparado o consta por qué no se pudo provocar"
    checkpoint: true
  - n: 4
    hace: "Medir el movimiento sobre la grabación y extraer los valores usados para contrastarlos con el sistema"
    produce: "tabla de movimiento y tabla de valores"
    termina_cuando: "cada duración medida y cada valor extraído tienen su comparación"
    checkpoint: true
  - n: 5
    hace: "Emitir el veredicto —fiel, fiel con deuda aceptada, infiel— recorriendo las comprobaciones del gate; si es infiel, la entrega es una devolución con los cuatro campos de C5"
    produce: "el dictamen de gate:excelencia-visual en su eje fidelidad, o la devolución"
    termina_cuando: "el veredicto tiene valor y cada diferencia tiene evidencia"
    checkpoint: true
fuentes_a_consultar:
  - "docs/diseno/03-SISTEMA.md, 05-MOVIMIENTO.md y 10-DEUDA.md"
  - "la especificación aprobada y las diferencias declaradas de Construcción"
  - "la matriz de entornos del pack instalado"
artefactos:
  - tipo: documento
    nombre: comparación de fidelidad
    estructura_minima:
      - "una fila por superficie, tamaño y estado: especificado, construido, diferencia, si incumple un eje"
      - "la tabla de movimiento medido y la tabla de valores contrastados"
      - "el veredicto y, si hay deuda, su referencia a lo acordado antes"
    obligatorio: true
  - tipo: captura
    nombre: pares lado a lado
    estructura_minima:
      - "una imagen por superficie, tamaño y estado con las dos columnas"
    obligatorio: true
evidencias_requeridas:
  - que: "cada diferencia nombrada es visible"
    forma: "el par lado a lado con la diferencia marcada"
    quien_la_puede_juzgar: "DIS/critica-visual, y el Owner en superficie premium"
  - que: "la comparación se hizo sobre el commit entregado"
    forma: "el commit citado en la comparación"
    quien_la_puede_juzgar: "cualquiera con acceso a la fuente"
criterios_de_calidad_medibles:
  - criterio: "cobertura de estados"
    como_se_mide: "cinco estados por superficie comparados o justificados"
  - criterio: "diferencias con evidencia"
    como_se_mide: "cien por cien de las diferencias tienen su par lado a lado"
  - criterio: "sin deuda a posteriori"
    como_se_mide: "toda deuda aceptada cita un acuerdo anterior a la construcción"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas y los dos artefactos completos"
  - "el veredicto tiene valor y cada diferencia nombrada tiene su par lado a lado"
condiciones_de_devolucion:
  - "veredicto infiel: se devuelve a CNS con los cuatro campos y los pares que lo sostienen"
  - "la especificación aprobada no cubre lo construido: se devuelve a DIS/diseno-visual"
  - "el commit no arranca o no es localizable: se rechaza al recibir"
reglas_de_escalado:
  - cuando: "segunda devolución a Construcción sobre el mismo paquete"
    a_quien: "DSP, freno de a.7"
    con_que: "las dos posturas y los pares"
  - cuando: "la diferencia afecta a superficie premium o a un patrón aprobado por el Owner"
    a_quien: "el Owner"
    con_que: "la comparación lado a lado y lo que se pierde, en una frase"
  - cuando: "resulto haber especificado o construido lo revisado"
    a_quien: "DSP, para reasignar el rol"
    con_que: "la coincidencia de titulares"
incompatibilidades:
  - "no comparte trabajador con DIS/diseno-visual, DIS/prototipado, DIS/movimiento ni CNS/implementacion en el mismo item"
actuaciones_prohibidas:
  - "aceptar a posteriori como deuda una simplificación descubierta al comparar"
  - "rechazar por preferencia: sólo por diferencia con lo aprobado"
  - "proponer la corrección: se nombra la diferencia"
  - "comparar sobre una revisión distinta de la entregada"
  - "dar por fiel una superficie sin haber provocado sus cinco estados"
ejemplo_bueno: >
  El revisor arranca el commit entregado, compara la lista de pedidos del portal en
  escritorio y móvil, provoca el error de permisos y ve que la pantalla dice «no hay nada»:
  diferencia con la especificación, eje fidelidad incumplido. Mide el desplegable a 180 ms
  contra los 200 especificados. Emite infiel con dos pares lado a lado y devuelve con los
  cuatro campos; no propone cómo arreglarlo.
ejemplo_malo: >
  El revisor abre la captura que le pasó Construcción, la compara de memoria con lo que
  recuerda de la especificación, ve que «se parece bastante», anota como deuda aceptada que
  falta el estado de error y emite fiel con deuda.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "el veredicto: fiel, fiel con deuda aceptada, o infiel"
  - "si una diferencia incumple un eje de la rúbrica o es irrelevante"
metodos:
  - DIS/RevisionDeFidelidad
no_autocertifica:
  - gate:excelencia-visual
checklist:
  - id: acuse-antes
    pregunta: "¿He acusado o rechazado el handoff recorriendo sus comprobaciones?"
    automatizable: si
  - id: contexto-limpio
    pregunta: "¿No he especificado ni construido nada de lo que comparo?"
    automatizable: si
  - id: cinco-estados-comparados
    pregunta: "¿He provocado y comparado los cinco estados, o consta por qué no?"
    automatizable: parcial
  - id: diferencias-con-par
    pregunta: "¿Cada diferencia tiene su par lado a lado?"
    automatizable: si
  - id: deuda-solo-previa
    pregunta: "¿Toda deuda aceptada cita un acuerdo anterior a la construcción?"
    automatizable: si
```
