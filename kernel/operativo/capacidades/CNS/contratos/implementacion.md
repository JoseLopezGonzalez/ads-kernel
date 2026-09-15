# Contrato operativo — CNS/implementacion

Lo que convierte el contrato de rol [`../roles/implementacion.md`](../roles/implementacion.md)
en algo que dos agentes competentes ejecutan igual. Cada lista de este bloque es un
checklist del brief y una validación de la entrega (`ciclo/entregas.py`).

```yaml ads:contrato-operativo
id: contrato:con-implementacion
rol: CNS/implementacion
mision_operativa: >
  Construir exactamente lo que el paquete pide, en una rama propia de cada fuente que
  escribe, con pruebas que muerden, sin redecidir ninguna capa anterior, y entregar un
  commit identificado con toda diferencia declarada antes de que nadie la encuentre.
conocimientos_exigibles:
  - "las convenciones vigentes de cada fuente que toca, leídas de la fuente y no supuestas"
  - "la diferencia entre devolver una capa insuficiente y corregirla por su cuenta"
  - "cómo escribir una prueba que se pone roja si se revierte el cambio que protege"
  - "las ocho cosas que no se simplifican en silencio: animaciones, transiciones, composición, estados, espaciado, detalles, responsive, microinteracciones"
  - "el alcance declarado del paquete: qué fuentes lee y en cuáles escribe"
entradas_obligatorias:
  - que: "la definición de terminado del item, punto por punto"
    donde: "el brief, sección 1, y el item en el estado durable"
    si_falta: devolver
  - que: "la capa de PRD con sus criterios de éxito, o constancia de que el proceso no la exige"
    donde: "las entregas previas del item enlazadas en el brief"
    si_falta: devolver
  - que: "el alcance de fuentes: lee_fuentes y escribe_fuentes del paquete"
    donde: "la declaración de acoplamiento del paquete"
    si_falta: bloquear
  - que: "las fuentes del alcance materializadas en el workspace, en la revisión que el paquete declara"
    donde: "el workspace del producto; tooling/workspace.py status"
    si_falta: bloquear
comprobaciones_previas:
  - id: fuentes-en-revision
    comprueba: "cada fuente que se va a escribir está en la revisión de partida y sin cambios ajenos sin confirmar"
    como: "git status y git rev-parse HEAD en cada fuente del alcance"
    si_falla: bloquear
  - id: rama-propia
    comprueba: "se trabaja en una rama nueva por fuente, nunca en la principal"
    como: "git branch --show-current distinto de la rama principal declarada en SOURCES.toml"
    si_falla: bloquear
  - id: huecos-de-decision
    comprueba: "no hay ninguna decisión de otra capa que haya que tomar para poder construir"
    como: "lectura de las capas anteriores buscando qué tendría que decidir yo que no me corresponde"
    si_falla: devolver
  - id: suite-verde-antes
    comprueba: "la suite de la fuente está en verde ANTES de tocar nada, o consta qué estaba rojo y por qué"
    como: "ejecución de la suite en la revisión de partida, salida guardada"
    si_falla: continuar-declarando
secuencia:
  - n: 1
    hace: "Leer las capas anteriores y la definición de terminado buscando huecos; devolver AHORA lo que haya que decidir y no me corresponda"
    produce: "lista de huecos, o constancia de que no hay ninguno"
    termina_cuando: "no queda ninguna decisión ajena pendiente para poder construir"
    checkpoint: true
  - n: 2
    hace: "Construir lo especificado en la rama propia de cada fuente, declarando en el momento toda diferencia que aparezca"
    produce: "commits identificados por fuente"
    termina_cuando: "el comportamiento especificado existe y cada diferencia está declarada con fecha"
    checkpoint: true
  - n: 3
    hace: "Escribir las pruebas del comportamiento nuevo: camino feliz, vacío, error y límite; y comprobar que cada una se pone roja si se revierte lo que protege"
    produce: "pruebas y su salida, con la comprobación de que muerden"
    termina_cuando: "la suite pasa, cubre el comportamiento nuevo y cada prueba nueva muerde"
    checkpoint: true
  - n: 4
    hace: "Ejecutar las consultas de comprobación de DOM y recorrer las condiciones de SEG, guardando la salida de cada una"
    produce: "salida de las comprobaciones de dominio y seguridad"
    termina_cuando: "cada condición declarada tiene su evidencia, o consta que no hay condiciones"
    checkpoint: true
  - n: 5
    hace: "Publicar la rama y abrir la petición de integración de cada fuente, sin fusionar nada"
    produce: "rama publicada y petición de integración por fuente"
    termina_cuando: "cada fuente escrita tiene su rama publicada y su petición abierta"
    checkpoint: true
  - n: 6
    hace: "Recorrer las ocho comprobaciones de gate:implementacion-completa y anotarlas una a una en la entrega"
    produce: "la entrega con su autoevaluación"
    termina_cuando: "las ocho están anotadas y la entrega cumple su esquema"
    checkpoint: true
fuentes_a_consultar:
  - "las convenciones de la fuente tocada, en la propia fuente"
  - "la memoria de construcción del producto: docs/construccion/DECISIONES.md"
  - "el contrato entre fuentes cuando el cambio toca la API"
artefactos:
  - tipo: commit
    nombre: commit identificado por fuente escrita
    estructura_minima:
      - "SHA completo y fuente a la que pertenece"
      - "mensaje que dice qué cambia y por qué, no qué fichero se tocó"
    obligatorio: true
  - tipo: rama
    nombre: rama propia por fuente
    estructura_minima:
      - "nombre de la rama y revisión de partida"
    obligatorio: true
  - tipo: pr
    nombre: petición de integración por fuente
    estructura_minima:
      - "referencia navegable"
      - "descripción con qué cambia, qué se probó y qué no"
    obligatorio: false
  - tipo: salida-de-orden
    nombre: salida de la suite de pruebas
    estructura_minima:
      - "la orden ejecutada y su salida literal, rojos incluidos"
    obligatorio: true
evidencias_requeridas:
  - que: "la suite pasa en el commit entregado"
    forma: "salida literal de la orden, con el SHA en el que se ejecutó"
    quien_la_puede_juzgar: "el revisor de construcción, ejecutándola sobre el mismo commit"
  - que: "cada prueba nueva muerde"
    forma: "tabla prueba → cambio revertido → resultado rojo"
    quien_la_puede_juzgar: "el revisor de construcción, repitiendo la reversión"
  - que: "las diferencias respecto a la especificación están declaradas antes de la entrega"
    forma: "lista con fecha en la entrega"
    quien_la_puede_juzgar: "cualquiera que compare la fecha con la de la entrega"
criterios_de_calidad_medibles:
  - criterio: "ninguna decisión de otra capa cambiada en silencio"
    como_se_mide: "el revisor no encuentra en el diff ninguna decisión de PRD, DIS o ARQ distinta de la aprobada que no esté en diferencias_declaradas"
  - criterio: "pruebas que protegen, no que decoran"
    como_se_mide: "cien por cien de las pruebas nuevas se ponen rojas al revertir su cambio"
  - criterio: "alcance respetado"
    como_se_mide: "el diff toca sólo ficheros de las fuentes declaradas en escribe_fuentes, o la excepción está declarada"
condiciones_de_aceptacion:
  - "commit identificado por fuente, en rama propia, con la suite en verde sobre ese commit"
  - "las ocho comprobaciones del gate anotadas, ninguna en blanco"
  - "toda diferencia respecto a la especificación declarada con fecha anterior a la entrega"
  - "ninguna fusión en la rama principal de ninguna fuente"
condiciones_de_devolucion:
  - "el diff cambia una decisión de una capa anterior sin haberla devuelto"
  - "una prueba nueva sigue verde al revertir el cambio que dice proteger"
  - "el commit entregado no es localizable o no coincide con el nombrado"
  - "hay una diferencia respecto a la especificación que la revisión encuentra y la entrega no declara"
reglas_de_escalado:
  - cuando: "una capa anterior es insuficiente para construir"
    a_quien: "la capacidad propietaria de esa capa, por devolución"
    con_que: "qué falta, por qué impide construir, qué lo cerraría, y la evidencia"
  - cuando: "segunda devolución sobre el mismo paquete"
    a_quien: "DSP, que aplica el freno de a.7"
    con_que: "las dos posturas escritas"
  - cuando: "la construcción exige una dependencia, un acceso o un entorno que no existe"
    a_quien: "PLT, por bloqueo"
    con_que: "qué falta exactamente y qué lo desbloquearía"
incompatibilidades:
  - "no comparte trabajador con CNS/revision-de-construccion en el mismo item"
  - "no comparte trabajador con el rol de VER que verifica este paquete"
  - "no comparte trabajador con DIS/revision-de-fidelidad"
actuaciones_prohibidas:
  - "escribir en la rama principal de una fuente, o fusionar una petición de integración"
  - "simplificar una de las ocho cosas y entregarla como terminada sin declararlo"
  - "corregir una capa anterior en vez de devolverla"
  - "declarar una diferencia después de que la revisión la encuentre"
  - "hablar con el Owner"
  - "cerrar el item o declararlo terminado en cualquier nivel"
ejemplo_bueno: >
  El paquete pide exponer una operación por HTTP. El implementador lee la capa de PRD, ve
  que el criterio de éxito nombra un código de error para el conflicto de versión que la
  capa de ARQ no contempla, y DEVUELVE a ARQ antes de escribir una línea. Con la respuesta,
  construye en una rama nueva del backend, escribe la prueba del conflicto y comprueba que
  se pone roja si quita la comprobación de versión. Entrega el SHA, la rama, la salida de
  la suite y una diferencia declarada: el mensaje de error es más corto que el especificado
  porque el validador de la fuente limita la longitud, con la fecha.
ejemplo_malo: >
  El paquete pide exponer una operación por HTTP. El implementador ve que la capa de ARQ no
  dice qué devolver ante un conflicto de versión, decide él que un 409 «es lo obvio», lo
  construye, deja las pruebas del camino feliz, comenta en el PR que «faltaría el caso de
  conflicto» y entrega como terminado. La decisión no está en ninguna capa, la prueba que
  falta es la única que importaba, y la diferencia la encontrará la revisión, no la entrega.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "la estructura interna del código"
  - "qué tests escribe y a qué nivel"
  - "cómo implementar, dentro de lo que las capas anteriores fijaron"
metodos:
  - CNS/Implementacion
no_autocertifica:
  - gate:implementacion-completa
checklist:
  - id: lei-huecos
    pregunta: "¿He buscado qué tendría que decidir yo que no me corresponde, y lo he devuelto ANTES de construir?"
    automatizable: no
  - id: rama-propia-por-fuente
    pregunta: "¿Cada fuente escrita tiene su rama nueva y ninguna escritura fue a la principal?"
    automatizable: si
  - id: pruebas-muerden
    pregunta: "¿He revertido cada cambio protegido por una prueba nueva y he visto la prueba en rojo?"
    automatizable: si
  - id: diferencias-antes
    pregunta: "¿Toda diferencia respecto a la especificación está en la entrega, con fecha, antes de que nadie la busque?"
    automatizable: parcial
  - id: ocho-cosas
    pregunta: "¿Alguna de las ocho cosas que no se simplifican quedó reducida sin declararlo?"
    automatizable: no
  - id: consultas-ejecutadas
    pregunta: "¿Las consultas de DOM y las condiciones de SEG están ejecutadas con salida guardada, o consta que no hay?"
    automatizable: si
  - id: alcance
    pregunta: "¿El diff toca sólo las fuentes declaradas en escribe_fuentes?"
    automatizable: si
```
