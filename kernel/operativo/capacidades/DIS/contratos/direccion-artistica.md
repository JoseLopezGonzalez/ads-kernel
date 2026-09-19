# Contrato operativo — DIS/direccion-artistica

Lo que convierte [`../roles/direccion-artistica.md`](../roles/direccion-artistica.md)
en alternativas reales, una recomendación y una síntesis que el Owner puede leer (§16, §17, §20).

```yaml ads:contrato-operativo
id: contrato:dis-direccion-artistica
rol: DIS/direccion-artistica
mision_operativa: >
  Generar para cada decisión importante dos o tres alternativas conceptualmente distintas
  —no variantes de borde—, cada una con sus diez campos; recomendar una y decir por qué en
  vez de delegar la elección al Owner; y producir la síntesis de ocho secciones que el
  Owner recibe, donde NECESITAMOS DEL OWNER sólo pide lo que es suyo: aprobar dirección o
  elegir entre decisiones realmente estratégicas.
conocimientos_exigibles:
  - "los principios de diseño del producto y su dirección visual vigente"
  - "qué decisiones son del Owner (§20) y cuáles decide el equipo"
  - "cómo se escribe una alternativa real: distinta en principio, no en el borde de una tarjeta"
entradas_obligatorias:
  - que: "el análisis de uso, la síntesis de investigación y la auditoría de reutilización"
    donde: "las entregas previas de DIS"
    si_falta: devolver
  - que: "la dirección visual aprobada del producto"
    donde: "docs/diseno/ y la memoria de diseño"
    si_falta: bloquear
comprobaciones_previas:
  - id: alternativas-distintas
    comprueba: "las alternativas difieren en principio, no en un atributo"
    como: "lectura del campo principio de cada una"
    si_falla: devolver
  - id: es-decision-importante
    comprueba: "la decisión merece alternativas: cambia experiencia, comportamiento, información esencial o coste"
    como: "contraste con los seis casos de escalado de §20"
    si_falla: continuar-declarando
secuencia:
  - n: 1
    hace: "Generar dos o tres alternativas conceptualmente distintas para la decisión importante"
    produce: "alternativas"
    termina_cuando: "cada alternativa tiene otro principio y ninguna es una variante de otra"
    checkpoint: true
  - n: 2
    hace: "Rellenar los diez campos de cada alternativa: principio, ventajas, inconvenientes, coste, escalabilidad, impacto móvil, impacto en consistencia, riesgos, qué reutiliza, qué introduce"
    produce: "alternativas completas"
    termina_cuando: "los diez campos de §16 están en cada alternativa"
    checkpoint: true
  - n: 3
    hace: "Recomendar una y decir por qué, sin delegar la elección"
    produce: "recomendación"
    termina_cuando: "hay una recomendación argumentada y la decisión queda en el equipo salvo que sea del Owner (§20)"
    checkpoint: true
  - n: 4
    hace: "Escribir la síntesis de ocho secciones para el Owner y decidir qué va en NECESITAMOS DEL OWNER"
    produce: "síntesis para el Owner"
    termina_cuando: "las ocho secciones de §20 están y NECESITAMOS DEL OWNER dice nada o una decisión realmente suya"
    checkpoint: true
fuentes_a_consultar:
  - "docs/diseno/01-PRINCIPIOS.md y 08-DECISIONES.md del control repo"
  - "las entregas previas de DIS del item"
artefactos:
  - tipo: documento
    nombre: alternativas
    estructura_minima:
      - "dos o tres alternativas, cada una con principio, ventajas, inconvenientes, coste, escalabilidad, impacto móvil, impacto en consistencia, riesgos, qué reutiliza y qué introduce"
    obligatorio: true
  - tipo: documento
    nombre: recomendación
    estructura_minima:
      - "la alternativa recomendada y por qué"
      - "qué se sacrifica al elegirla"
    obligatorio: true
  - tipo: documento
    nombre: síntesis para el Owner
    estructura_minima:
      - "PROBLEMA · REALIDAD ACTUAL · ALTERNATIVAS ESTUDIADAS · RECOMENDACIÓN DEL EQUIPO"
      - "QUÉ REUTILIZAMOS / UNIFICAMOS · RIESGOS / SACRIFICIOS · PROTOTIPO · NECESITAMOS DEL OWNER (o nada)"
    obligatorio: true
evidencias_requeridas:
  - que: "las alternativas son conceptualmente distintas"
    forma: "el campo principio de cada una, contrastado"
    quien_la_puede_juzgar: "DIS/critica-visual"
  - que: "NECESITAMOS DEL OWNER no pide spacing, iconos, tokens ni microdecisiones"
    forma: "la sección, leída contra la lista de §20"
    quien_la_puede_juzgar: "el Owner"
criterios_de_calidad_medibles:
  - criterio: "diez campos"
    como_se_mide: "cada alternativa tiene los diez campos de §16"
  - criterio: "alternativas reales"
    como_se_mide: "ninguna alternativa comparte principio con otra"
  - criterio: "ocho secciones"
    como_se_mide: "la síntesis tiene las ocho secciones en el orden de §20"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas y los tres artefactos completos"
  - "hay recomendación: no se delega la elección al Owner"
condiciones_de_devolucion:
  - "una alternativa es variante de otra: se devuelve a la propia dirección antes de escalar"
  - "no hay auditoría de reutilización: se devuelve a DIS/sistema-de-diseno"
reglas_de_escalado:
  - cuando: "la decisión cambia la experiencia, el comportamiento principal, la filosofía de producto, la información esencial o el coste/riesgo, o hay alternativas legítimas que afectan al producto"
    a_quien: "OWNER"
    con_que: "la síntesis de ocho secciones con las alternativas y la recomendación"
incompatibilidades:
  - "no comparte trabajador con DIS/critica-visual ni con DIS/revision-de-fidelidad en el mismo item"
actuaciones_prohibidas:
  - "presentar variantes de borde como alternativas"
  - "preguntar al Owner qué prefiere sin recomendar"
  - "escalar spacing, tamaños menores, iconos rutinarios, tokens o microdecisiones"
ejemplo_bueno: >
  Para las acciones del detalle de pedido, la dirección artística propone toolbar
  contextual, menú agrupado por operación y acciones distribuidas por sección, con sus
  diez campos; recomienda la toolbar por coste y consistencia con Palets; y la síntesis
  dice NECESITAMOS DEL OWNER: nada.
ejemplo_malo: >
  Presenta card con borde, card sin borde y card con sombra como tres alternativas, no
  recomienda ninguna, y pregunta al Owner cuál le gusta más; el Owner recibe una
  conversación interna en vez de una síntesis.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "qué dirección elige entre las exploradas dentro de lo aprobado"
  - "cuándo una decisión merece alternativas"
metodos:
  - DIS/Fundacion
  - DIS/Reconstruccion
  - DIS/Evolucion
no_autocertifica:
  - gate:excelencia-visual
checklist:
  - id: distintas-en-principio
    pregunta: "¿Las alternativas difieren en principio y no en un atributo?"
    automatizable: parcial
  - id: diez-campos
    pregunta: "¿Cada alternativa tiene los diez campos de §16?"
    automatizable: si
  - id: hay-recomendacion
    pregunta: "¿Recomiendo una y digo por qué?"
    automatizable: si
  - id: ocho-secciones
    pregunta: "¿La síntesis tiene las ocho secciones y NECESITAMOS DEL OWNER sólo pide lo suyo?"
    automatizable: si
  - id: nada-de-microdecisiones
    pregunta: "¿He dejado fuera de NECESITAMOS DEL OWNER lo que decide el equipo?"
    automatizable: no
```
