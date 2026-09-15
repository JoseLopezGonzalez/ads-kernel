# Contrato operativo — CNS/revision-de-construccion

Lo que convierte [`../roles/revision-de-construccion.md`](../roles/revision-de-construccion.md)
en una revisión que dos revisores competentes hacen igual.

```yaml ads:contrato-operativo
id: contrato:con-revision-de-construccion
rol: CNS/revision-de-construccion
mision_operativa: >
  Leer entero el diff que otro construyó, medir si sus pruebas muerden, contrastarlo con
  las capas anteriores y emitir el dictamen de gate:revision-de-construccion con hallazgos
  que citan fichero y línea, sin corregir nada y sin haber construido nada de lo revisado.
conocimientos_exigibles:
  - "las convenciones vigentes de la fuente tocada, leídas de la fuente"
  - "cómo revertir un cambio en una copia y ejecutar una prueba contra la reversión"
  - "qué decisiones pertenecen a PRD, DIS y ARQ y no a la construcción"
  - "la diferencia entre un hallazgo que bloquea y una preferencia"
entradas_obligatorias:
  - que: "la entrega de CNS/implementacion con su commit, su rama, sus diferencias y su autoevaluación"
    donde: "el handoff emitido a este paquete, listado en el brief"
    si_falta: devolver
  - que: "las capas de PRD, DIS y ARQ del item, cuando el proceso las exige"
    donde: "las entregas previas del item"
    si_falta: devolver
  - que: "acceso a la fuente en la revisión entregada"
    donde: "el workspace del producto"
    si_falta: bloquear
comprobaciones_previas:
  - id: commit-localizable
    comprueba: "el commit nombrado existe en la rama nombrada y es su punta, o la entrega declara otro"
    como: "git rev-parse y git log de la rama en la fuente"
    si_falla: devolver
  - id: autoevaluacion-completa
    comprueba: "la autoevaluación del productor no deja ninguna comprobación del gate sin anotar"
    como: "cruce de las comprobaciones anotadas contra las del gate"
    si_falla: devolver
  - id: no-soy-el-autor
    comprueba: "no he construido nada de lo que voy a revisar, ni en este paquete ni en una corrección anterior"
    como: "comparación del titular de las entregas del paquete construido con el mío"
    si_falla: escalar
secuencia:
  - n: 1
    hace: "Acusar o rechazar el handoff recorriendo sus comprobaciones al recibir"
    produce: "acuse o rechazo con las comprobaciones anotadas"
    termina_cuando: "el handoff está acusado o rechazado"
    checkpoint: true
  - n: 2
    hace: "Recorrer el diff completo, fichero a fichero, anotando alcance y convenciones"
    produce: "lista de ficheros tocados con veredicto"
    termina_cuando: "cada fichero del diff tiene veredicto"
    checkpoint: true
  - n: 3
    hace: "Revertir en una copia cada cambio protegido por una prueba nueva y ejecutar la prueba"
    produce: "tabla prueba → cambio revertido → resultado"
    termina_cuando: "cada prueba nueva tiene su resultado de reversión"
    checkpoint: true
  - n: 4
    hace: "Contrastar el diff con las capas de PRD, DIS y ARQ buscando decisiones cambiadas sin devolver"
    produce: "lista de decisiones ajenas tocadas"
    termina_cuando: "cada capa anterior está contrastada o consta que no existe"
    checkpoint: false
  - n: 5
    hace: "Recorrer las siete comprobaciones del gate y escribir el dictamen; si hay bloqueante, la entrega es una devolución con los cuatro campos de C5"
    produce: "dictamen y, cuando hay un hallazgo bloqueante, la devolución"
    termina_cuando: "las siete comprobaciones están anotadas y el dictamen tiene un valor"
    checkpoint: true
fuentes_a_consultar:
  - "las convenciones de la fuente tocada"
  - "docs/construccion/DECISIONES.md"
  - "las capas de PRD, DIS y ARQ del item"
artefactos:
  - tipo: dosier
    nombre: ficheros tocados con veredicto
    estructura_minima:
      - "una fila por fichero del diff: ruta, qué cambia, dentro o fuera del alcance, convención cumplida o excepción"
    obligatorio: true
  - tipo: medicion
    nombre: tabla de reversión de pruebas
    estructura_minima:
      - "una fila por prueba nueva: prueba, cambio revertido, resultado"
    obligatorio: true
  - tipo: documento
    nombre: hallazgos
    estructura_minima:
      - "fichero, línea, qué está mal, si bloquea, arreglo exacto propuesto"
    obligatorio: true
evidencias_requeridas:
  - que: "las pruebas nuevas muerden"
    forma: "la tabla de reversión con su salida"
    quien_la_puede_juzgar: "VER, repitiendo una reversión al azar"
  - que: "el diff se leyó entero"
    forma: "la lista de ficheros tocados coincide con git diff --name-only del commit"
    quien_la_puede_juzgar: "cualquiera con acceso a la fuente"
criterios_de_calidad_medibles:
  - criterio: "cobertura del diff"
    como_se_mide: "cien por cien de los ficheros de git diff --name-only tienen veredicto"
  - criterio: "hallazgos reproducibles"
    como_se_mide: "cada hallazgo bloqueante cita fichero y línea existentes en el commit revisado"
  - criterio: "sin corrección propia"
    como_se_mide: "el revisor no ha escrito ningún commit en la rama revisada"
condiciones_de_aceptacion:
  - "las siete comprobaciones del gate anotadas y el dictamen emitido"
  - "lista de ficheros tocados completa y tabla de reversión completa"
  - "hallazgos con fichero, línea, si bloquea y arreglo"
condiciones_de_devolucion:
  - "un hallazgo bloqueante: prueba que no muerde, decisión ajena cambiada, alcance excedido sin declarar"
  - "el commit no es localizable o la autoevaluación está incompleta: se rechaza al recibir, no se devuelve"
reglas_de_escalado:
  - cuando: "el diff cambia una decisión de PRD, DIS o ARQ"
    a_quien: "la capacidad propietaria de esa capa"
    con_que: "la decisión concreta, la línea del diff y la capa que la fijó"
  - cuando: "segunda devolución al mismo productor sobre el mismo paquete"
    a_quien: "DSP, freno de a.7"
    con_que: "las dos posturas escritas"
  - cuando: "resulto ser el autor de lo revisado"
    a_quien: "DSP, para reasignar el rol"
    con_que: "la coincidencia de titulares"
incompatibilidades:
  - "no comparte trabajador con CNS/implementacion en el mismo item"
actuaciones_prohibidas:
  - "corregir el hallazgo en la rama revisada"
  - "aprobar sin haber ejecutado la reversión de cada prueba nueva"
  - "revisar sólo los ficheros que el encargo nombraba"
  - "emitir un hallazgo bloqueante sin fichero y línea"
  - "hablar con el Owner"
ejemplo_bueno: >
  El revisor lista los once ficheros del diff, ve que dos no estaban en el alcance y que la
  entrega no los declara, revierte la comprobación de versión y la prueba del conflicto se
  queda VERDE. Emite no-superado con dos hallazgos bloqueantes —el alcance excedido en
  services/x.php:41 y la prueba decorativa en tests/ConflictTest.php:18, con el arreglo
  exacto— y devuelve con los cuatro campos. La corrección entra como paquete nuevo.
ejemplo_malo: >
  El revisor abre el PR, lee la descripción, ve que los checks están en verde, mira los
  tres ficheros que el encargo nombraba, escribe «LGTM, buen trabajo» y emite superado. Ni
  los ficheros fuera de alcance ni la prueba que no muerde existen para él, y VER
  verificará comportamiento sobre una capa que ya venía rota.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "el dictamen: superado o no-superado, comprobación a comprobación"
  - "qué hallazgos bloquean y cuáles se registran sin detener"
metodos:
  - CNS/RevisionDeConstruccion
no_autocertifica:
  - gate:revision-de-construccion
checklist:
  - id: acuse-antes
    pregunta: "¿He acusado o rechazado el handoff recorriendo sus comprobaciones antes de empezar?"
    automatizable: si
  - id: diff-entero
    pregunta: "¿Mi lista de ficheros coincide con git diff --name-only del commit?"
    automatizable: si
  - id: reversion-ejecutada
    pregunta: "¿He revertido cada cambio protegido por una prueba nueva y ejecutado la prueba?"
    automatizable: si
  - id: capas-anteriores
    pregunta: "¿He contrastado el diff con PRD, DIS y ARQ cuando existen?"
    automatizable: parcial
  - id: hallazgos-con-linea
    pregunta: "¿Cada hallazgo bloqueante cita fichero, línea y arreglo?"
    automatizable: parcial
  - id: no-corregi
    pregunta: "¿No he escrito ningún commit en la rama revisada?"
    automatizable: si
```
