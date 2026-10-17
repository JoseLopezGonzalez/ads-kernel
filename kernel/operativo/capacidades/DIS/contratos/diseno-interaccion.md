# Contrato operativo — DIS/diseno-interaccion

Lo que convierte [`../roles/diseno-interaccion.md`](../roles/diseno-interaccion.md)
en el diseño del flujo y de la interacción, con sus estados, navegación, acciones y errores (§14, §21).

```yaml ads:contrato-operativo
id: contrato:dis-diseno-interaccion
rol: DIS/diseno-interaccion
mision_operativa: >
  Diseñar cómo se usa la superficie —flujo, navegación, acciones frecuentes y
  excepcionales, feedback, errores y su recuperación, teclado— sobre el análisis de uso y
  antes del diseño visual, de modo que la especificación construible tenga comportamiento,
  estados, navegación, acciones y errores decididos y no los invente Construcción.
conocimientos_exigibles:
  - "los patrones de interacción vigentes del producto"
  - "los estados obligatorios y los extremos del análisis de uso"
  - "cómo se especifica un comportamiento para que Construcción no decida nada"
entradas_obligatorias:
  - que: "el análisis de uso y el informe de realidad actual"
    donde: "las entregas previas de DIS/investigacion-ux"
    si_falta: devolver
comprobaciones_previas:
  - id: patrones-vigentes
    comprueba: "he mirado cómo interactúan las superficies hermanas antes de decidir el flujo"
    como: "recorrido de los patrones de interacción del producto"
    si_falla: devolver
  - id: uso-resuelto
    comprueba: "el problema de uso está resuelto antes de dibujar el flujo"
    como: "lectura del análisis de uso"
    si_falla: devolver
secuencia:
  - n: 1
    hace: "Diseñar el flujo: pasos, navegación, entradas y salidas, con teclado cuando aplique"
    produce: "flujo"
    termina_cuando: "cada paso dice de dónde viene y a dónde va"
    checkpoint: true
  - n: 2
    hace: "Decidir comportamiento, estados, acciones frecuentes y excepcionales, feedback, errores y recuperación"
    produce: "comportamiento"
    termina_cuando: "ningún estado ni error queda sin comportamiento"
    checkpoint: true
  - n: 3
    hace: "Entregar la especificación de interacción para el diseño visual y la construcción"
    produce: "especificación de interacción"
    termina_cuando: "Construcción no tiene que inventar un comportamiento"
    checkpoint: true
fuentes_a_consultar:
  - "el análisis de uso del item"
  - "docs/diseno/ del control repo"
  - "las superficies hermanas y sus patrones de interacción"
artefactos:
  - tipo: documento
    nombre: especificación de interacción
    estructura_minima:
      - "el flujo con navegación y teclado"
      - "comportamiento por estado, acciones frecuentes y excepcionales, feedback"
      - "errores y su recuperación"
      - "qué cambia por permisos y por dispositivo"
    obligatorio: true
evidencias_requeridas:
  - que: "cada estado tiene comportamiento"
    forma: "la especificación, leída estado a estado"
    quien_la_puede_juzgar: "DIS/diseno-visual y CNS/implementacion"
criterios_de_calidad_medibles:
  - criterio: "estados con comportamiento"
    como_se_mide: "cien por cien de los estados del análisis tienen comportamiento"
  - criterio: "errores con recuperación"
    como_se_mide: "cada error dice cómo se recupera"
condiciones_de_aceptacion:
  - "cada estado del análisis de uso tiene comportamiento decidido"
  - "las comprobaciones del gate anotadas y la especificación completa"
condiciones_de_devolucion:
  - "un error queda sin recuperación: se devuelve a la propia interacción"
  - "no hay análisis de uso: se devuelve a DIS/investigacion-ux"
reglas_de_escalado:
  - cuando: "la interacción exige un dato o un endpoint que no existe"
    a_quien: "ARQ/encaje"
    con_que: "el flujo y el dato que falta"
incompatibilidades:
  - "no comparte trabajador con DIS/validacion-de-uso ni con DIS/critica-visual en el mismo item"
actuaciones_prohibidas:
  - "dejar un error sin recuperación"
  - "diseñar el flujo sin el análisis de uso"
  - "delegar un comportamiento a Construcción"
ejemplo_bueno: >
  Para mover palets entre almacenes, el flujo decide que la selección múltiple confirma en
  un diálogo con el recuento, que un palet bloqueado se explica en línea y no con un
  toast, y que Escape cancela sin perder la selección; Construcción lo implementa sin
  preguntar.
ejemplo_malo: >
  El flujo dice «el usuario mueve palets»; Construcción decide un toast para el error, el
  Owner no lo ve y el operario pierde la selección al cancelar.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "qué patrón de interacción vigente aplica"
  - "cómo se agrupan las acciones excepcionales"
metodos:
  - DIS/Fundacion
  - DIS/Reconstruccion
  - DIS/Evolucion
no_autocertifica:
  - gate:usabilidad
checklist:
  - id: uso-resuelto
    pregunta: "¿Diseño sobre el análisis de uso y no sobre una suposición?"
    automatizable: parcial
  - id: estados-con-comportamiento
    pregunta: "¿Cada estado y cada error tienen comportamiento y recuperación?"
    automatizable: si
  - id: teclado
    pregunta: "¿El flujo funciona con teclado cuando la superficie lo exige?"
    automatizable: parcial
  - id: patrones-hermanos
    pregunta: "¿Sigo los patrones de interacción de las superficies hermanas o digo por qué no?"
    automatizable: no
  - id: nada-para-construccion
    pregunta: "¿Queda algún comportamiento que Construcción tendría que inventar?"
    automatizable: no
```
