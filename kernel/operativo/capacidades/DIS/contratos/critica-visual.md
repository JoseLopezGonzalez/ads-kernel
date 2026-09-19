# Contrato operativo — DIS/critica-visual

Lo que convierte [`../roles/critica-visual.md`](../roles/critica-visual.md)
en la crítica independiente antes del Owner (§19) y la crítica visual de la implementación construida (§24).

```yaml ads:contrato-operativo
id: contrato:dis-critica-visual
rol: DIS/critica-visual
mision_operativa: >
  Evaluar, sin haber sido el autor, una dirección importante antes de que llegue al Owner
  y la implementación real una vez construida: claridad, jerarquía, carga cognitiva,
  coherencia, densidad, profesionalidad, accesibilidad, consistencia con el producto,
  posible simplificación, reutilización, responsive, estados extremos y riesgo de
  introducir otro patrón innecesario; y devolver el trabajo cuando no supera, porque
  fidelidad y excelencia no son lo mismo.
conocimientos_exigibles:
  - "los trece criterios de §19 y cómo se juzga cada uno con evidencia"
  - "el gate de excelencia visual y en qué se distingue de la fidelidad"
  - "el producto entero: cómo se ven las superficies hermanas"
entradas_obligatorias:
  - que: "la propuesta o la implementación a criticar, con su prototipo o su aplicación real"
    donde: "las entregas previas del item o el commit entregado"
    si_falta: devolver
  - que: "la auditoría de reutilización"
    donde: "las entregas previas de DIS/sistema-de-diseno"
    si_falta: devolver
comprobaciones_previas:
  - id: no-soy-el-autor
    comprueba: "no he producido la propuesta ni la implementación que critico"
    como: "el plan: independencia declarada"
    si_falla: bloquear
  - id: mirado-de-verdad
    comprueba: "he abierto la propuesta o la aplicación real, no sólo su descripción"
    como: "recorrido con capturas"
    si_falla: devolver
secuencia:
  - n: 1
    hace: "Evaluar los trece criterios de §19 sobre la propuesta o sobre la aplicación real"
    produce: "crítica por criterio"
    termina_cuando: "cada criterio tiene un juicio y su evidencia"
    checkpoint: true
  - n: 2
    hace: "Señalar simplificaciones posibles y patrones innecesarios que se introducirían"
    produce: "hallazgos"
    termina_cuando: "cada hallazgo dice dónde y por qué"
    checkpoint: true
  - n: 3
    hace: "Emitir el dictamen del gate de excelencia visual, devolviendo si no supera"
    produce: "dictamen"
    termina_cuando: "el dictamen se sostiene en los criterios y las devoluciones dicen qué la cerraría"
    checkpoint: true
fuentes_a_consultar:
  - "la propuesta o el commit entregado, abiertos"
  - "docs/diseno/ del control repo"
  - "las superficies hermanas del producto"
artefactos:
  - tipo: documento
    nombre: crítica por criterio
    estructura_minima:
      - "una fila por criterio de §19: claridad, jerarquía, carga cognitiva, coherencia, densidad, profesionalidad, accesibilidad, consistencia, simplificación, reutilización, responsive, estados extremos, patrón innecesario"
      - "los hallazgos con dónde y por qué"
      - "el dictamen y, si devuelve, qué la cerraría"
    obligatorio: true
  - tipo: captura
    nombre: lo criticado, visto
    estructura_minima:
      - "una captura por hallazgo, sobre la propuesta o la aplicación real"
    obligatorio: true
evidencias_requeridas:
  - que: "la crítica se hizo sobre lo mirable, no sobre su descripción"
    forma: "las capturas con el hallazgo marcado"
    quien_la_puede_juzgar: "DIS/direccion-artistica y el Owner"
  - que: "los trece criterios están juzgados"
    forma: "la tabla por criterio"
    quien_la_puede_juzgar: "cualquiera"
criterios_de_calidad_medibles:
  - criterio: "trece criterios"
    como_se_mide: "los trece de §19 tienen juicio y evidencia"
  - criterio: "devolución cerrable"
    como_se_mide: "toda devolución dice qué la cerraría"
condiciones_de_aceptacion:
  - "las capturas muestran lo criticado y no una descripción de segunda mano"
  - "las comprobaciones del gate anotadas y los dos artefactos completos"
condiciones_de_devolucion:
  - "falta la auditoría de reutilización: se devuelve a DIS/sistema-de-diseno antes de criticar"
  - "lo criticado no se puede abrir: se devuelve a quien lo entregó"
reglas_de_escalado:
  - cuando: "la crítica y la dirección artística no coinciden tras dos devoluciones"
    a_quien: "OWNER"
    con_que: "las dos posturas con su evidencia"
incompatibilidades:
  - "no comparte trabajador con DIS/movimiento ni con DIS/sistema-de-diseno en el mismo item"
  - "no comparte trabajador con DIS/direccion-artistica, DIS/diseno-visual, DIS/prototipado ni CNS/implementacion en el mismo item"
actuaciones_prohibidas:
  - "criticar desde la descripción sin abrir la propuesta"
  - "superar el gate por fidelidad al prototipo cuando la implementación no es profesional"
  - "devolver sin decir qué la cerraría"
ejemplo_bueno: >
  Sobre el detalle de pedido construido, la crítica abre la aplicación, encuentra que la
  toolbar es fiel al prototipo pero que en móvil tapa el total, lo marca con captura, y
  devuelve a Diseño con la condición de cierre: la toolbar en móvil no oculta información
  esencial.
ejemplo_malo: >
  La crítica lee el PR, dice «se parece al prototipo» y supera el gate; en producción la
  toolbar tapa el total en móvil y el Owner lo descubre.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "qué hallazgo bloquea y cuál es mejora"
  - "cómo ordena los hallazgos"
metodos:
  - DIS/CriticaVisual
no_autocertifica:
  - gate:excelencia-visual
checklist:
  - id: no-autor
    pregunta: "¿No soy el autor de lo que critico?"
    automatizable: si
  - id: trece-criterios
    pregunta: "¿He juzgado los trece criterios de §19 con evidencia?"
    automatizable: si
  - id: abierto-de-verdad
    pregunta: "¿He abierto la propuesta o la aplicación real?"
    automatizable: parcial
  - id: cierre-nombrado
    pregunta: "¿Toda devolución dice qué la cerraría?"
    automatizable: si
  - id: fidelidad-no-es-excelencia
    pregunta: "¿He juzgado profesionalidad y no sólo parecido con el prototipo?"
    automatizable: no
```
