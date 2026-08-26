# DIS/CriticaVisual — el método del juicio independiente

```yaml ads:metodo
id: DIS/CriticaVisual
nombre: CriticaVisual
capacidad: DIS
disparador:
  - "una fase divergente de nivel N1 o superior termina y va a converger"
  - "un paquete de DIS va a cerrar su gate de excelencia visual"
  - "DIS/revision-de-fidelidad emite un veredicto que afecta al eje fidelidad"
carga:
  - "las direcciones o la propuesta, con sus artefactos y su evidencia"
  - "docs/diseno/00-VISION.md, 01-PRINCIPIOS.md, 02-REFERENCIAS.md, 08-DECISIONES.md"
  - "el nivel de novedad declarado del paquete y su motivo"
  - "la comparación de fidelidad, cuando existe"
preguntas_iniciales:
  - "¿qué exigía el nivel de novedad declarado, y se ha cumplido?"
  - "¿cuáles son los dos productos genéricos de esta categoría contra los que voy a comparar?"
pasos:
  - n: 1
    nombre: COMPROBAR EL MÍNIMO DE EXPLORACIÓN
    modo: lineal
    hace: >
      Verificar que el número de direcciones corresponde al nivel declarado, y que difieren
      en al menos dos de las cinco dimensiones. Se comprueba dimensión por dimensión, no de
      un vistazo.
    produce: "tabla de dimensiones por dirección"
    termina_cuando: "cada par de direcciones tiene contadas sus dimensiones distintas"
    checkpoint: true
  - n: 2
    nombre: COMPARAR CON LA CATEGORÍA
    modo: convergente
    hace: >
      Poner la propuesta al lado de dos productos genéricos de su categoría y responder qué
      la distingue. Si la respuesta es «el color» o «el logotipo», el eje personalidad está
      en rechazo.
    produce: "comparación lado a lado con su conclusión escrita"
    termina_cuando: "está escrito qué distingue la propuesta, o que no la distingue nada"
    checkpoint: true
  - n: 3
    nombre: RECORRER LOS NUEVE EJES
    modo: convergente
    hace: >
      Evaluar cada eje de rubrica:excelencia-visual con su evidencia. En los ejes no
      automatizables se escribe una razón que otro pueda discutir, no una etiqueta.
    produce: "nivel y razón por eje, con evidencia enlazada"
    termina_cuando: "los nueve ejes tienen nivel, razón y evidencia"
    checkpoint: true
  - n: 4
    nombre: COMPROBAR LAS REFERENCIAS
    modo: lineal
    hace: >
      Verificar que toda referencia usada tiene enlace, fecha y principio extraído, y que
      ninguna propuesta reproduce una obra o un estilo completo.
    produce: "veredicto sobre el uso de referencias"
    termina_cuando: "cada referencia usada está comprobada"
    checkpoint: false
  - n: 5
    nombre: DICTAMINAR
    modo: convergente
    hace: >
      Escribir el dictamen conforme a la plantilla común, con veredicto conforme o
      devuelto. Si algún eje está en rechazo, el veredicto es devuelto, sin excepción.
    produce: "dictamen"
    termina_cuando: "gate:critica-de-encuadre no aplica aquí; se cumple la plantilla de dictamen y el veredicto está escrito"
    checkpoint: true
artefactos:
  - "tabla de dimensiones por dirección"
  - "comparación con dos productos genéricos"
  - "los nueve ejes con nivel, razón y evidencia"
  - "dictamen"
puntos_owner:
  - "ninguno: la crítica no habla con el Owner. Su dictamen es evidencia para el gate"
consultas:
  - "ninguna: se juzga con el material entregado. Si falta material, ése es el hallazgo"
checkpoints:
  - "tras los pasos 1, 2, 3 y 5"
critica:
  - "¿alguna observación mía es una preferencia disfrazada de hallazgo?"
  - "¿he propuesto la solución en lugar de nombrar el defecto?"
  - "¿mi razón en los ejes no automatizables es discutible, o es una etiqueta?"
gate: gate:excelencia-visual
salida:
  - "dictamen conforme, o dictamen devuelto con los ejes en rechazo y su evidencia"
devolucion:
  - "a DIS/diseno-visual, cuando falla el mínimo de exploración"
  - "a DIS/direccion-artistica, cuando la propuesta incumple un principio vigente"
bloqueo:
  - "no existe la evidencia que la rúbrica exige: sin capturas ni grabaciones no hay juicio"
  - "no hay memoria de diseño y no se puede juzgar coherencia con nada"
cancelacion:
  - "el paquete se cancela antes de que el dictamen se emita: el trabajo parcial se conserva"
aprendizaje:
  - "un eje que se rechaza repetidamente en el mismo producto señala un principio mal escrito"
  - "los rechazos y su motivo se registran en el historial"
prueba_de_reanudacion: >
  Un agente nuevo lee los ejes ya evaluados con su evidencia y continúa por los que faltan.
  Si el paso 2 no está hecho, DEBE hacerlo antes de dictaminar: sin comparación con la
  categoría, el eje personalidad no es evaluable. Es la prueba T96.
```
