# Contrato operativo — DIS/investigacion-visual

Lo que convierte [`../roles/investigacion-visual.md`](../roles/investigacion-visual.md)
en la síntesis de investigación profesional que la Directiva del Owner exige cuando la decisión lo merece (§13).

```yaml ads:contrato-operativo
id: contrato:dis-investigacion-visual
rol: DIS/investigacion-visual
mision_operativa: >
  Responder cómo se resuelve profesionalmente este problema y por qué, mirando patrones
  profesionales, productos comparables, software ERP y data-heavy cuando sea relevante,
  convenciones de plataforma, accesibilidad, interacción, densidad, responsive, casos
  similares y las referencias internas del propio producto; y entregar una síntesis con lo
  aplicable y lo que no, sin copiar diseños bonitos.
conocimientos_exigibles:
  - "patrones profesionales de interfaz para operaciones y datos densos"
  - "las convenciones de la plataforma (web y móvil) y las normas de accesibilidad"
  - "las referencias internas del producto: qué ya resuelve algo parecido y cómo"
entradas_obligatorias:
  - que: "el informe de realidad actual y el análisis de uso"
    donde: "las entregas previas de DIS/investigacion-ux"
    si_falta: devolver
  - que: "el nivel de novedad del paquete"
    donde: "el brief, derivado de la composición de DIS"
    si_falta: devolver
comprobaciones_previas:
  - id: relevancia-declarada
    comprueba: "la decisión merece investigación: el nivel de novedad o el alcance lo dicen"
    como: "lectura del brief y del nivel"
    si_falla: continuar-declarando
  - id: referencias-internas-primero
    comprueba: "he mirado primero cómo el propio producto resuelve casos parecidos"
    como: "recorrido de las superficies equivalentes del informe de realidad"
    si_falla: devolver
secuencia:
  - n: 1
    hace: "Reunir patrones profesionales, productos comparables, ERP y data-heavy cuando aplique, convenciones de plataforma, accesibilidad, interacción, densidad y responsive"
    produce: "corpus de referencias"
    termina_cuando: "cada referencia dice de dónde sale y qué resuelve"
    checkpoint: true
  - n: 2
    hace: "Contrastar cada patrón con el caso de uso real y con las referencias internas del producto"
    produce: "contraste"
    termina_cuando: "cada patrón dice si es aplicable aquí y por qué"
    checkpoint: true
  - n: 3
    hace: "Escribir la síntesis: patrones encontrados, principios útiles, errores frecuentes, qué es aplicable, qué no, riesgos"
    produce: "síntesis de investigación"
    termina_cuando: "los seis apartados de §13 están escritos y ninguno es una lista de capturas bonitas"
    checkpoint: true
fuentes_a_consultar:
  - "las superficies equivalentes del informe de realidad actual"
  - "docs/diseno/ del control repo"
  - "las guías de plataforma y de accesibilidad vigentes"
artefactos:
  - tipo: documento
    nombre: síntesis de investigación
    estructura_minima:
      - "patrones encontrados, con su origen"
      - "principios útiles para este caso"
      - "errores frecuentes que evitar"
      - "qué es aplicable aquí y por qué"
      - "qué no es aplicable y por qué"
      - "riesgos"
    obligatorio: true
evidencias_requeridas:
  - que: "cada patrón propuesto responde a un problema real del análisis de uso"
    forma: "la referencia cruzada síntesis ↔ análisis de uso"
    quien_la_puede_juzgar: "DIS/direccion-artistica y DIS/critica-visual"
criterios_de_calidad_medibles:
  - criterio: "seis apartados"
    como_se_mide: "los seis apartados de §13 tienen contenido"
  - criterio: "nada copiado"
    como_se_mide: "ningún patrón entra sin decir por qué resuelve el problema"
condiciones_de_aceptacion:
  - "cada patrón aplicable cita el problema del análisis de uso que resuelve"
  - "las comprobaciones del gate anotadas y la síntesis completa"
condiciones_de_devolucion:
  - "la síntesis es una colección de referencias sin contraste: se devuelve a la propia investigación"
  - "no hay análisis de uso: se devuelve a DIS/investigacion-ux"
reglas_de_escalado:
  - cuando: "la investigación revela que el alcance de producto es otro"
    a_quien: "PRD/definicion"
    con_que: "la síntesis con el hallazgo"
incompatibilidades:
  - "no comparte trabajador con DIS/critica-visual en el mismo item"
actuaciones_prohibidas:
  - "copiar un diseño bonito sin decir qué problema resuelve"
  - "saltar la referencia interna del propio producto"
  - "presentar la síntesis como decisión: la decisión es de la dirección artística"
ejemplo_bueno: >
  Para un editor de mapa de almacén, la síntesis compara tres editores de planta de ERP,
  anota que todos separan selección de edición, que la densidad alta exige zoom semántico,
  que el propio producto ya tiene un patrón de arrastre en palets, y que copiar el editor
  de un CAD sería un error frecuente.
ejemplo_malo: >
  La síntesis es una colección de capturas de productos bonitos sin decir qué resuelve
  cada una, no mira el patrón de arrastre que el producto ya tiene, y recomienda un editor
  de CAD que nadie de la lonja sabría usar.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "qué productos comparables mira y cuántos bastan para la decisión"
metodos:
  - DIS/Fundacion
  - DIS/Reconstruccion
  - DIS/Evolucion
no_autocertifica:
  - gate:excelencia-visual
checklist:
  - id: referencias-internas
    pregunta: "¿He mirado primero cómo lo resuelve el propio producto?"
    automatizable: parcial
  - id: seis-apartados
    pregunta: "¿La síntesis tiene los seis apartados de §13?"
    automatizable: si
  - id: aplicable-y-por-que
    pregunta: "¿Cada patrón dice si es aplicable aquí y por qué?"
    automatizable: si
  - id: errores-frecuentes
    pregunta: "¿Digo qué errores frecuentes hay que evitar en este caso?"
    automatizable: no
  - id: riesgos
    pregunta: "¿Nombro los riesgos de aplicar lo encontrado?"
    automatizable: no
```
