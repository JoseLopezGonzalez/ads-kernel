# Contrato operativo — DIS/movimiento

Lo que convierte [`../roles/movimiento.md`](../roles/movimiento.md)
en el movimiento que acompaña a cada estado, con curva y duración trazadas al sistema (§21).

```yaml ads:contrato-operativo
id: contrato:dis-movimiento
rol: DIS/movimiento
mision_operativa: >
  Decidir qué movimiento acompaña a cada cambio de estado y transición de la superficie,
  con qué curva y duración, trazado al sistema de diseño, para que Construcción no lo
  invente y la crítica visual pueda medirlo; y decir dónde no hay movimiento y por qué.
conocimientos_exigibles:
  - "la regla de no animar pantallas operativas por gusto y sus excepciones"
  - "los valores de movimiento del sistema de diseño: curvas y duraciones"
  - "qué transiciones merecen movimiento en una pantalla operativa y cuáles no"
entradas_obligatorias:
  - que: "la especificación de interacción"
    donde: "las entregas previas de DIS/diseno-interaccion"
    si_falta: devolver
comprobaciones_previas:
  - id: interaccion-cerrada
    comprueba: "la especificación de interacción tiene todos los estados y transiciones decididos"
    como: "lectura de la especificación estado a estado"
    si_falla: devolver
  - id: sistema-de-movimiento
    comprueba: "conozco las curvas y duraciones vigentes antes de decidir"
    como: "lectura del sistema de diseño"
    si_falla: devolver
secuencia:
  - n: 1
    hace: "Decidir el movimiento de cada transición y estado, o su ausencia"
    produce: "tabla de movimiento"
    termina_cuando: "cada transición dice curva, duración y si no hay movimiento, por qué"
    checkpoint: true
  - n: 2
    hace: "Trazar cada valor al sistema o pedir su ampliación"
    produce: "valores trazados"
    termina_cuando: "ningún valor fuera del sistema sin petición"
    checkpoint: true
  - n: 3
    hace: "Entregar la tabla al diseño visual y a la crítica, con lo que no se anima y por qué"
    produce: "tabla de movimiento entregada"
    termina_cuando: "el diseño visual la incorpora a la especificación construible"
    checkpoint: true

fuentes_a_consultar:
  - "docs/diseno/03-SISTEMA.md del control repo"
  - "la especificación de interacción del item"
artefactos:
  - tipo: documento
    nombre: tabla de movimiento
    estructura_minima:
      - "una fila por transición y estado: curva, duración, token, o sin movimiento y por qué"
    obligatorio: true
evidencias_requeridas:
  - que: "los valores están trazados"
    forma: "la tabla con sus tokens"
    quien_la_puede_juzgar: "DIS/revision-de-fidelidad"
criterios_de_calidad_medibles:
  - criterio: "valores trazados al sistema"
    como_se_mide: "cien por cien de las filas con token o petición de ampliación"
  - criterio: "transiciones cubiertas"
    como_se_mide: "cien por cien de las transiciones de la interacción tienen fila"
condiciones_de_aceptacion:
  - "cada ausencia de movimiento está justificada"
  - "las comprobaciones del gate anotadas y la tabla completa"
condiciones_de_devolucion:
  - "hay una transición sin fila: se devuelve al propio movimiento"
  - "no hay especificación de interacción: se devuelve a DIS/diseno-interaccion"
reglas_de_escalado:
  - cuando: "un movimiento exige una curva que el sistema no tiene"
    a_quien: "DIS/sistema-de-diseno"
    con_que: "la transición y el valor"
incompatibilidades:
  - "no comparte trabajador con DIS/critica-visual en el mismo item"
actuaciones_prohibidas:
  - "dejar que Construcción decida una duración o una curva"
  - "animar una pantalla operativa por gusto"
  - "usar un valor fuera del sistema sin petición"
ejemplo_bueno: >
  Para el diálogo de palets, la tabla decide que abrir usa la curva de entrada del sistema
  en 150 ms, que el error no se anima, y que el recuento cambia con el token de énfasis;
  nada más se mueve.
ejemplo_malo: >
  Construcción añade un rebote al abrir porque quedaba bien; la crítica lo devuelve y el
  sistema no tiene esa curva.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "qué transiciones no se animan"
metodos:
  - DIS/Fundacion
  - DIS/Evolucion
no_autocertifica:
  - gate:excelencia-visual
checklist:
  - id: trazado
    pregunta: "¿Cada valor de movimiento está trazado al sistema o pedido?"
    automatizable: si
  - id: ausencias-justificadas
    pregunta: "¿Digo dónde no hay movimiento y por qué?"
    automatizable: si
  - id: todas-las-transiciones
    pregunta: "¿Cada transición de la interacción tiene su fila?"
    automatizable: si
  - id: operativa-sin-adornos
    pregunta: "¿He evitado animar por gusto una pantalla operativa?"
    automatizable: no
  - id: entregado-al-visual
    pregunta: "¿La tabla está en la especificación construible?"
    automatizable: parcial
```
