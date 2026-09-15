# Las bases de contrato operativo — una por familia de roles

> **Qué es.** Lo que comparten todos los roles de una misma familia y no tiene sentido
> escribir treinta veces: qué comprueban antes de empezar, cómo abren y cierran su
> secuencia, qué tienen prohibido, qué contestan en su checklist, cuándo escalan y qué
> gates no pueden dictaminar sobre su propio paquete. Un rol pertenece a **una** base, por
> su id. Su contrato efectivo —el que el brief entrega y la entrega comprueba— es la fusión
> de esta base, de lo que se **deriva** de sus veintinueve campos de rol y de su
> especialización `ads:contrato-de-rol` cuando la tiene. La mecánica vive en
> [`../runtime/ciclo/contratos.py`](../runtime/ciclo/contratos.py); la forma final, en
> [`../esquemas/contrato-operativo.yaml`](../esquemas/contrato-operativo.yaml).
>
> **Qué NO es.** Prosa que un agente pueda leer de otra manera. Cada lista de aquí entra en
> el checklist del brief y en la validación de la entrega, y `comprobar_contratos` falla si
> un rol materializable queda sin base o su fusión no cumple el esquema.
>
> Este fichero es un catálogo de bases, una por familia.

## Las siete familias

```text
productor      produce una capa que otro juzga: define, diseña, construye, especifica
revisor        juzga la capa de otro y emite un dictamen; nunca corrige lo que juzga
consultor      declara CONDICIONES antes de construir, y las revisa después
investigador   responde a una pregunta acotada con evidencia, o valida con personas reales
operador       ejecuta sobre entornos reales: despliega, observa, contiene
aprendizaje    convierte lo aprendido en regla candidata, sin escribir norma
orquestador    DSP: planifica, supervisa y deriva trabajo POR el runtime, nunca a mano
```

Los roles que no aparecen en ninguna base son los que la oficina no materializa como
paquete: `ENC/*`, que ocurre antes de que exista una ruta —lo ejecuta la sesión que abre
el encargo, con `trabajo.py`—. `comprobar_contratos` los publica como conceptuales, no los
exime en silencio. `DSP/*` sí tiene base: el proceso `DIR` le exige derivar items de una
decisión, y eso es un paquete que un supervisor toma y ejecuta con las órdenes de la
oficina.

Este fichero contiene un bloque por familia.

## productor

```yaml ads:contrato-base
id: contrato-base:productor
familia: productor
roles:
  - CNS/implementacion
  - CNS/experimental
  - PRD/definicion
  - PRD/criterio-de-exito
  - DIS/diseno-visual
  - DIS/diseno-interaccion
  - DIS/direccion-artistica
  - DIS/movimiento
  - DIS/prototipado
  - DIS/sistema-de-diseno
  - DIS/investigacion-visual
  - ARQ/diagnostico
  - ARQ/encaje
  - DOM/migracion
  - SIS/evolucion
conocimientos_exigibles:
  - "la forma exacta de la entrega que el brief describe, y qué artefacto de los suyos la satisface"
entradas_obligatorias:
  - que: "el brief del paquete, con su rol, su gate y las entregas previas del item"
    donde: "el brief que la oficina escribe al tomar el paquete"
    si_falta: bloquear
comprobaciones_previas:
  - id: entradas-localizables
    comprueba: "cada entrada obligatoria existe donde el brief dice, y es lo que dice ser"
    como: "abrir cada entrada nombrada en el brief y cotejarla con su descripción"
    si_falla: devolver
  - id: alcance-del-paquete
    comprueba: "lo que voy a producir cabe en la obligación y el criterio de satisfacción del paquete"
    como: "lectura de la obligación, el criterio de satisfacción y la salida exigida del brief"
    si_falla: escalar
  - id: no-hay-checkpoint-ajeno-sin-leer
    comprueba: "si el paquete tiene checkpoint de un titular anterior, lo he leído antes de empezar"
    como: "el brief lista el checkpoint; se lee y se continúa desde él, no desde cero"
    si_falla: continuar-declarando
secuencia_inicial:
  - hace: "Acusar o rechazar cada handoff recibido recorriendo sus comprobaciones al recibir"
    produce: "acuses o rechazos con las comprobaciones anotadas"
    termina_cuando: "ningún handoff emitido a este paquete queda sin acusar ni rechazar"
    checkpoint: true
secuencia_final:
  - hace: "Recorrer las comprobaciones del gate y el checklist del contrato y escribir la autoevaluación, sin dejar ninguna sin contestar"
    produce: "la autoevaluación de la entrega"
    termina_cuando: "cada comprobación del gate y cada pregunta del checklist tienen respuesta"
    checkpoint: true
  - hace: "Escribir la entrega con la forma exacta del brief: artefactos localizables, evidencias, diferencias declaradas, decisiones asumidas, riesgos, deuda, no hecho y siguiente"
    produce: "la entrega"
    termina_cuando: "la oficina la acepta sin rechazarla"
    checkpoint: false
evidencias_requeridas:
  - que: "cada artefacto obligatorio del contrato está en la entrega y es localizable"
    forma: "la lista de artefactos de la entrega, con referencia real"
    quien_la_puede_juzgar: "el revisor del gate del rol, y la propia oficina al validar la forma"
criterios_de_calidad_medibles:
  - criterio: "sin diferencia silenciosa con lo pedido"
    como_se_mide: "toda desviación de la obligación aparece en diferencias_declaradas de la entrega"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas en la autoevaluación, una a una"
  - "los artefactos obligatorios del contrato presentes con su estructura mínima"
condiciones_de_devolucion:
  - "una entrada obligatoria no es lo que dice ser: se rechaza al recibir, no se devuelve después"
reglas_de_escalado:
  - cuando: "lo que hay que producir amplía o cambia el alcance del paquete"
    a_quien: "DSP, que enruta a la capacidad propietaria del alcance o al Owner"
    con_que: "la diferencia entre lo pedido y lo necesario, y las dos posturas escritas"
  - cuando: "segunda devolución sobre el mismo paquete"
    a_quien: "DSP, freno de a.7"
    con_que: "las dos posturas escritas y la evidencia de cada una"
actuaciones_prohibidas:
  - "dictaminar el gate de su propio paquete"
  - "declarar terminado sin escribir la entrega con la forma exacta del brief"
  - "ampliar el alcance en silencio"
  - "escribir en el estado durable a mano"
incompatibilidades:
  - "no comparte trabajador con el rol que dictamina su gate en el mismo item"
entrega_a:
  - segun-el-plan
checklist:
  - id: acuse-antes
    pregunta: "¿He acusado o rechazado cada handoff recibido recorriendo sus comprobaciones?"
    automatizable: si
  - id: entradas-comprobadas
    pregunta: "¿He comprobado cada entrada obligatoria antes de empezar?"
    automatizable: parcial
  - id: artefactos-completos
    pregunta: "¿Cada artefacto obligatorio del contrato está en la entrega y es localizable?"
    automatizable: si
  - id: gate-recorrido
    pregunta: "¿He recorrido cada comprobación de mi gate y anotado su resultado?"
    automatizable: si
  - id: diferencias-declaradas
    pregunta: "¿Toda desviación respecto a lo pedido está en diferencias_declaradas?"
    automatizable: parcial
no_autocertifica_ademas: []
```

## revisor

```yaml ads:contrato-base
id: contrato-base:revisor
familia: revisor
roles:
  - CNS/revision-de-construccion
  - VER/dosier
  - VER/decision
  - DIS/revision-de-fidelidad
  - DIS/critica-visual
  - SIS/coherencia
conocimientos_exigibles:
  - "la diferencia entre un hallazgo que bloquea y una preferencia propia"
  - "los cuatro campos de una devolución de C5: qué falta, por qué es insuficiente, qué la cerraría, evidencia"
entradas_obligatorias:
  - que: "la entrega que se juzga, con sus artefactos localizables y su autoevaluación"
    donde: "el handoff emitido a este paquete y la entrega previa que nombra"
    si_falta: devolver
comprobaciones_previas:
  - id: contexto-limpio
    comprueba: "no he producido nada de lo que voy a juzgar, ni en este paquete ni en una corrección anterior"
    como: "comparación del titular de las entregas previas del item con el mío"
    si_falla: escalar
  - id: entrega-localizable
    comprueba: "lo que juzgo existe donde la entrega dice y es su versión exacta"
    como: "abrir cada artefacto nombrado y cotejar su referencia"
    si_falla: devolver
  - id: autoevaluacion-completa
    comprueba: "la autoevaluación del productor no deja ninguna comprobación de su gate sin anotar"
    como: "cruce de las comprobaciones anotadas contra las del gate"
    si_falla: devolver
secuencia_inicial:
  - hace: "Acusar o rechazar el handoff recorriendo sus comprobaciones al recibir; un rechazo se hace ahora, no después de aceptar"
    produce: "acuse o rechazo con las comprobaciones anotadas"
    termina_cuando: "el handoff está acusado o rechazado"
    checkpoint: true
secuencia_final:
  - hace: "Recorrer las comprobaciones del gate que juzgo y emitir el dictamen; si hay un hallazgo bloqueante, la entrega es una devolución con los cuatro campos de C5"
    produce: "el dictamen, o la devolución"
    termina_cuando: "cada comprobación del gate juzgado está anotada y el dictamen tiene un valor"
    checkpoint: true
  - hace: "Escribir la entrega con los dictámenes, los hallazgos con su localización y la autoevaluación de mi propio gate"
    produce: "la entrega"
    termina_cuando: "la oficina la acepta sin rechazarla"
    checkpoint: false
evidencias_requeridas:
  - que: "cada hallazgo bloqueante es reproducible por otro"
    forma: "el hallazgo cita dónde está y qué se ve"
    quien_la_puede_juzgar: "cualquiera con acceso al artefacto juzgado"
criterios_de_calidad_medibles:
  - criterio: "sin corrección propia"
    como_se_mide: "el revisor no ha escrito ningún artefacto en lo que juzga"
  - criterio: "sin devolución sin campos"
    como_se_mide: "toda devolución lleva los cuatro campos de C5 y la oficina la acepta"
condiciones_de_aceptacion:
  - "las comprobaciones del gate juzgado anotadas y el dictamen emitido"
  - "cada hallazgo bloqueante localizado, y la devolución con sus cuatro campos cuando la hay"
condiciones_de_devolucion:
  - "un hallazgo bloqueante: se devuelve al productor con los cuatro campos, y la corrección entra como paquete nuevo"
  - "lo que se juzga no es localizable o su autoevaluación está incompleta: se rechaza al recibir"
reglas_de_escalado:
  - cuando: "resulto ser el autor de lo que juzgo"
    a_quien: "DSP, para reasignar el rol"
    con_que: "la coincidencia de titulares"
  - cuando: "segunda devolución al mismo productor sobre el mismo paquete"
    a_quien: "DSP, freno de a.7"
    con_que: "las dos posturas escritas"
actuaciones_prohibidas:
  - "corregir lo que juzga"
  - "aprobar sin haber abierto lo que juzga"
  - "juzgar lo que uno mismo produjo"
  - "devolver por preferencia: sólo por diferencia con lo exigido"
  - "hablar con el Owner"
incompatibilidades:
  - "no comparte trabajador con el rol que produjo lo que juzga en el mismo item"
entrega_a:
  - segun-el-plan
checklist:
  - id: acuse-antes
    pregunta: "¿He acusado o rechazado el handoff recorriendo sus comprobaciones antes de empezar?"
    automatizable: si
  - id: contexto-limpio
    pregunta: "¿No he producido nada de lo que juzgo?"
    automatizable: si
  - id: abierto-entero
    pregunta: "¿He abierto entero lo que juzgo, no sólo lo que la entrega describe?"
    automatizable: parcial
  - id: hallazgos-localizados
    pregunta: "¿Cada hallazgo bloqueante dice dónde está y qué se ve?"
    automatizable: parcial
  - id: no-corregi
    pregunta: "¿No he corregido nada en lo que juzgo?"
    automatizable: si
no_autocertifica_ademas: []
```

## consultor

```yaml ads:contrato-base
id: contrato-base:consultor
familia: consultor
roles:
  - DOM/modelo
  - SEG/condiciones
  - PLT/maquinaria
conocimientos_exigibles:
  - "la diferencia entre una condición que se impone ANTES de construir y una revisión de lo construido"
entradas_obligatorias:
  - que: "el encuadre y el alcance del item, para saber sobre qué materia se declaran condiciones"
    donde: "el item y las entregas previas del plan, listadas en el brief"
    si_falta: devolver
comprobaciones_previas:
  - id: materia-afectada
    comprueba: "el item toca de verdad la materia sobre la que voy a declarar condiciones"
    como: "cruce del alcance y las fuentes del item con la materia de mi capacidad"
    si_falla: continuar-declarando
  - id: entradas-localizables
    comprueba: "cada entrada obligatoria existe donde el brief dice"
    como: "abrir cada entrada nombrada en el brief"
    si_falla: devolver
secuencia_inicial:
  - hace: "Acusar o rechazar cada handoff recibido recorriendo sus comprobaciones al recibir"
    produce: "acuses o rechazos"
    termina_cuando: "ningún handoff emitido a este paquete queda sin acusar ni rechazar"
    checkpoint: true
secuencia_final:
  - hace: "Escribir cada condición de forma que quien construye pueda comprobarla y quien revisa pueda dictaminarla, y declarar expresamente cuando NO hay condiciones"
    produce: "la lista de condiciones, o la declaración de que no hay ninguna"
    termina_cuando: "cada condición dice qué se comprueba y cómo, o consta que no hay condiciones"
    checkpoint: true
  - hace: "Recorrer las comprobaciones del gate y el checklist y escribir la entrega"
    produce: "la entrega"
    termina_cuando: "la oficina la acepta sin rechazarla"
    checkpoint: false
evidencias_requeridas:
  - que: "cada condición es comprobable por un tercero"
    forma: "la condición dice qué se mira y qué se espera ver"
    quien_la_puede_juzgar: "el revisor de la misma capacidad en su pasada de revisión"
criterios_de_calidad_medibles:
  - criterio: "sin condición vaga"
    como_se_mide: "ninguna condición contiene «adecuado» ni «correcto» sin una medida, ni deja a criterio del lector cuándo aplica"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas y las condiciones escritas o su ausencia declarada"
  - "cada condición dice qué se mira y qué se espera ver"
condiciones_de_devolucion:
  - "el alcance no permite saber qué materia se toca: se devuelve a la capacidad propietaria"
reglas_de_escalado:
  - cuando: "una condición exige una decisión que cambia el alcance o el producto"
    a_quien: "DSP, que enruta a la capacidad propietaria o al Owner"
    con_que: "la condición, lo que cambia y las dos posturas"
actuaciones_prohibidas:
  - "construir o corregir en vez de declarar la condición"
  - "declarar «sin condiciones» sin haber mirado el alcance"
  - "escribir una condición que sólo su autor sabe comprobar"
incompatibilidades:
  - "no comparte trabajador con el rol que construye lo condicionado en el mismo item"
entrega_a:
  - segun-el-plan
checklist:
  - id: acuse-antes
    pregunta: "¿He acusado o rechazado cada handoff recibido?"
    automatizable: si
  - id: materia-mirada
    pregunta: "¿He mirado el alcance y las fuentes del item antes de declarar condiciones?"
    automatizable: parcial
  - id: condiciones-comprobables
    pregunta: "¿Cada condición dice qué se mira y qué se espera ver?"
    automatizable: parcial
  - id: ausencia-declarada
    pregunta: "¿Si no hay condiciones, lo he declarado expresamente?"
    automatizable: si
  - id: gate-recorrido
    pregunta: "¿He recorrido cada comprobación de mi gate y anotado su resultado?"
    automatizable: si
no_autocertifica_ademas: []
```

## investigador

```yaml ads:contrato-base
id: contrato-base:investigador
familia: investigador
roles:
  - INV/investigacion
  - DIS/investigacion-ux
  - DIS/validacion-de-uso
  - USO/validacion
conocimientos_exigibles:
  - "la diferencia entre evidencia observada y opinión, y cómo se registra cada una"
entradas_obligatorias:
  - que: "la pregunta acotada o el criterio a validar, con su consumidor declarado"
    donde: "el encuadre del item y las entregas previas, listadas en el brief"
    si_falta: devolver
comprobaciones_previas:
  - id: pregunta-acotada
    comprueba: "sé qué pregunta respondo o qué criterio valido, y quién consumirá la respuesta"
    como: "lectura del encuadre y de la obligación del paquete"
    si_falla: devolver
  - id: fuente-declarada
    comprueba: "la fuente de evidencia —documental, experimento, personas reales— está declarada y disponible"
    como: "comprobación de acceso a la fuente antes de empezar"
    si_falla: bloquear
secuencia_inicial:
  - hace: "Acusar o rechazar cada handoff recibido recorriendo sus comprobaciones al recibir"
    produce: "acuses o rechazos"
    termina_cuando: "ningún handoff emitido a este paquete queda sin acusar ni rechazar"
    checkpoint: true
secuencia_final:
  - hace: "Separar en la entrega lo observado de lo interpretado, y declarar lo que no se pudo comprobar"
    produce: "la respuesta o el veredicto, con su evidencia y su sección de no comprobado"
    termina_cuando: "cada afirmación cita su evidencia o consta como no comprobada"
    checkpoint: true
  - hace: "Recorrer las comprobaciones del gate y el checklist y escribir la entrega"
    produce: "la entrega"
    termina_cuando: "la oficina la acepta sin rechazarla"
    checkpoint: false
evidencias_requeridas:
  - que: "cada afirmación tiene su evidencia"
    forma: "la observación, grabación, dato o documento que la sostiene, enlazado"
    quien_la_puede_juzgar: "el consumidor declarado de la respuesta"
criterios_de_calidad_medibles:
  - criterio: "no comprobado declarado"
    como_se_mide: "la sección de no comprobado existe y nombra lo que falta"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas y la respuesta con su evidencia y su no comprobado"
  - "lo observado y lo interpretado separados en la entrega"
condiciones_de_devolucion:
  - "la pregunta no está acotada o no tiene consumidor: se devuelve a quien la formuló"
reglas_de_escalado:
  - cuando: "la respuesta exige una decisión de producto o técnica que no es del rol"
    a_quien: "DSP, que enruta a la capacidad propietaria de la decisión"
    con_que: "la evidencia y las opciones que abre"
actuaciones_prohibidas:
  - "afirmar sin evidencia"
  - "omitir lo que no se pudo comprobar"
  - "decidir lo que la evidencia sólo informa"
incompatibilidades:
  - "no comparte trabajador con el rol que decide sobre la respuesta en el mismo item"
entrega_a:
  - segun-el-plan
checklist:
  - id: acuse-antes
    pregunta: "¿He acusado o rechazado cada handoff recibido?"
    automatizable: si
  - id: evidencia-por-afirmacion
    pregunta: "¿Cada afirmación cita su evidencia?"
    automatizable: parcial
  - id: no-comprobado
    pregunta: "¿La sección de no comprobado existe y nombra lo que falta?"
    automatizable: si
  - id: observado-vs-interpretado
    pregunta: "¿Lo observado y lo interpretado están separados?"
    automatizable: parcial
  - id: gate-recorrido
    pregunta: "¿He recorrido cada comprobación de mi gate y anotado su resultado?"
    automatizable: si
no_autocertifica_ademas: []
```

## operador

```yaml ads:contrato-base
id: contrato-base:operador
familia: operador
roles:
  - ENT/despliegue
  - ENT/observacion
  - ENT/convergencia
conocimientos_exigibles:
  - "qué entorno es cada uno, qué autoridad exige cada despliegue, y cómo se revierte"
entradas_obligatorias:
  - que: "el dosier de VER sin evidencia en rojo, y la autorización del Owner cuando el entorno es producción"
    donde: "las entregas previas del item y las decisiones del Owner, listadas en el brief"
    si_falta: bloquear
comprobaciones_previas:
  - id: autoridad-del-entorno
    comprueba: "tengo la autoridad que el entorno exige; a producción sólo con la decisión del Owner registrada"
    como: "lectura de la decisión del Owner y del entorno declarado en el brief"
    si_falla: bloquear
  - id: reversion-preparada
    comprueba: "sé cómo revertir antes de aplicar"
    como: "el procedimiento de reversión está escrito y probado en un entorno no productivo"
    si_falla: bloquear
secuencia_inicial:
  - hace: "Acusar o rechazar cada handoff recibido recorriendo sus comprobaciones al recibir"
    produce: "acuses o rechazos"
    termina_cuando: "ningún handoff emitido a este paquete queda sin acusar ni rechazar"
    checkpoint: true
secuencia_final:
  - hace: "Registrar lo aplicado, la ventana de observación y lo observado, con las órdenes y su salida"
    produce: "el registro de la operación"
    termina_cuando: "cada orden ejecutada consta con su salida y su resultado"
    checkpoint: true
  - hace: "Recorrer las comprobaciones del gate y el checklist y escribir la entrega"
    produce: "la entrega"
    termina_cuando: "la oficina la acepta sin rechazarla"
    checkpoint: false
evidencias_requeridas:
  - que: "lo aplicado es lo que el dosier verificó"
    forma: "la revisión exacta desplegada, citada en la entrega"
    quien_la_puede_juzgar: "VER, cruzando la revisión con su dosier"
criterios_de_calidad_medibles:
  - criterio: "reversible"
    como_se_mide: "el procedimiento de reversión está escrito y se ejecutó en un entorno no productivo"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas y el registro de la operación con sus órdenes y salidas"
  - "la revisión desplegada citada y el procedimiento de reversión escrito"
condiciones_de_devolucion:
  - "el dosier tiene evidencia en rojo: se devuelve a VER sin desplegar"
reglas_de_escalado:
  - cuando: "el despliegue exige una autoridad que no consta"
    a_quien: "el Owner, por DSP"
    con_que: "el entorno, lo que se despliega y lo que se pierde si no se despliega"
actuaciones_prohibidas:
  - "desplegar a producción sin la decisión del Owner registrada"
  - "aplicar sin saber revertir"
  - "declarar observado sin ventana de observación"
incompatibilidades:
  - "no comparte trabajador con VER/dosier en el mismo item"
entrega_a:
  - segun-el-plan
checklist:
  - id: acuse-antes
    pregunta: "¿He acusado o rechazado cada handoff recibido?"
    automatizable: si
  - id: autoridad-comprobada
    pregunta: "¿Tengo la autoridad que el entorno exige, registrada?"
    automatizable: si
  - id: reversion-lista
    pregunta: "¿El procedimiento de reversión está escrito y probado?"
    automatizable: parcial
  - id: ordenes-con-salida
    pregunta: "¿Cada orden ejecutada consta con su salida?"
    automatizable: si
  - id: gate-recorrido
    pregunta: "¿He recorrido cada comprobación de mi gate y anotado su resultado?"
    automatizable: si
no_autocertifica_ademas: []
```

## aprendizaje

```yaml ads:contrato-base
id: contrato-base:aprendizaje
familia: aprendizaje
roles:
  - APR/promocion
conocimientos_exigibles:
  - "la diferencia entre un aprendizaje fundado en evidencia del item y una opinión sobre el proceso"
entradas_obligatorias:
  - que: "el cierre del item con su aprendizaje declarado y la evidencia que lo sostiene"
    donde: "el cierre y las entregas del item, listados en el brief"
    si_falta: devolver
comprobaciones_previas:
  - id: item-cerrado
    comprueba: "el item del que sale el aprendizaje está cerrado o su cierre está en curso con el aprendizaje escrito"
    como: "lectura del cierre del item en el estado"
    si_falla: devolver
  - id: fundado
    comprueba: "el aprendizaje cita la evidencia del item que lo sostiene"
    como: "cruce del texto del aprendizaje con las entregas y dictámenes del item"
    si_falla: devolver
secuencia_inicial:
  - hace: "Acusar o rechazar cada handoff recibido recorriendo sus comprobaciones al recibir"
    produce: "acuses o rechazos"
    termina_cuando: "ningún handoff emitido a este paquete queda sin acusar ni rechazar"
    checkpoint: true
secuencia_final:
  - hace: "Escribir la regla candidata con su evidencia y su alcance, sin convertirla en norma"
    produce: "la regla candidata"
    termina_cuando: "la regla dice qué cambia, para quién, y qué evidencia la sostiene"
    checkpoint: true
  - hace: "Recorrer las comprobaciones del gate y el checklist y escribir la entrega"
    produce: "la entrega"
    termina_cuando: "la oficina la acepta sin rechazarla"
    checkpoint: false
evidencias_requeridas:
  - que: "la regla candidata está fundada"
    forma: "la evidencia del item citada en la regla"
    quien_la_puede_juzgar: "SIS, al decidir si la promueve"
criterios_de_calidad_medibles:
  - criterio: "sin norma escrita"
    como_se_mide: "la entrega no modifica ningún documento normativo: propone"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas y la regla candidata con su evidencia"
  - "ningún documento normativo modificado"
condiciones_de_devolucion:
  - "el aprendizaje no cita evidencia del item: se devuelve a quien cerró"
reglas_de_escalado:
  - cuando: "la regla candidata cambia una decisión del Owner"
    a_quien: "el Owner, por DSP"
    con_que: "la regla, la decisión que toca y la evidencia"
actuaciones_prohibidas:
  - "escribir norma"
  - "promover un aprendizaje sin evidencia"
incompatibilidades:
  - "no comparte trabajador con SIS/coherencia en el mismo item"
entrega_a:
  - segun-el-plan
checklist:
  - id: acuse-antes
    pregunta: "¿He acusado o rechazado cada handoff recibido?"
    automatizable: si
  - id: evidencia-citada
    pregunta: "¿La regla candidata cita la evidencia del item?"
    automatizable: parcial
  - id: sin-norma
    pregunta: "¿No he modificado ningún documento normativo?"
    automatizable: si
  - id: gate-recorrido
    pregunta: "¿He recorrido cada comprobación de mi gate y anotado su resultado?"
    automatizable: si
  - id: alcance-de-la-regla
    pregunta: "¿La regla candidata dice para quién aplica y para quién no?"
    automatizable: parcial
no_autocertifica_ademas: []
```

## orquestador

```yaml ads:contrato-base
id: contrato-base:orquestador
familia: orquestador
roles:
  - DSP/enrutamiento
  - DSP/estado
  - DSP/supervision
conocimientos_exigibles:
  - "las órdenes de la oficina: planificar, tablero, supervisar, reanudar; DSP no escribe estado a mano"
entradas_obligatorias:
  - que: "la decisión, el encuadre o el estado sobre el que hay que enrutar, derivar o supervisar"
    donde: "el item y el estado durable, listados en el brief"
    si_falta: devolver
comprobaciones_previas:
  - id: estado-verificable
    comprueba: "el estado durable verifica y no hay reconciliaciones abiertas antes de planificar o despachar"
    como: "ads_estado.py verificar y el tablero de la oficina"
    si_falla: bloquear
  - id: alcance-autorizado
    comprueba: "lo que voy a planificar cabe en el alcance autorizado por el Owner"
    como: "cruce del item con la autorización de su objetivo"
    si_falla: escalar
secuencia_inicial:
  - hace: "Acusar o rechazar cada handoff recibido recorriendo sus comprobaciones al recibir"
    produce: "acuses o rechazos"
    termina_cuando: "ningún handoff emitido a este paquete queda sin acusar ni rechazar"
    checkpoint: true
secuencia_final:
  - hace: "Publicar el tablero resultante y lo que hará el sistema si nadie dice nada"
    produce: "el tablero derivado y su frase de continuación"
    termina_cuando: "el tablero se deriva del estado sin diferencia entre dos lecturas"
    checkpoint: true
  - hace: "Recorrer las comprobaciones del gate y el checklist y escribir la entrega"
    produce: "la entrega"
    termina_cuando: "la oficina la acepta sin rechazarla"
    checkpoint: false
evidencias_requeridas:
  - que: "todo lo planificado o despachado está en el estado durable, escrito por el runtime"
    forma: "los identificadores de plan, paquetes y equipos, legibles con ads_estado.py"
    quien_la_puede_juzgar: "cualquiera que abra el estado desde otro proceso"
criterios_de_calidad_medibles:
  - criterio: "determinismo del despacho"
    como_se_mide: "dos lecturas del tablero desde instancias distintas producen los mismos bytes"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas y el tablero publicado"
  - "ningún objeto del estado escrito a mano"
condiciones_de_devolucion:
  - "la decisión o el encuadre no permiten derivar trabajo: se devuelve a quien lo formuló"
reglas_de_escalado:
  - cuando: "derivar trabajo amplía o cambia el alcance autorizado"
    a_quien: "el Owner"
    con_que: "el alcance autorizado, lo que se deriva y la diferencia"
actuaciones_prohibidas:
  - "escribir en el estado durable a mano"
  - "cambiar la prioridad de un paquete"
  - "decidir por contenido lo que es de la capacidad propietaria"
incompatibilidades:
  - "no comparte trabajador con el productor de lo que despacha en el mismo item"
entrega_a:
  - segun-el-plan
checklist:
  - id: acuse-antes
    pregunta: "¿He acusado o rechazado cada handoff recibido?"
    automatizable: si
  - id: estado-verificado
    pregunta: "¿El estado durable verificaba antes de planificar o despachar?"
    automatizable: si
  - id: por-el-runtime
    pregunta: "¿Todo lo que creé o moví lo escribió el runtime, no yo?"
    automatizable: si
  - id: tablero-publicado
    pregunta: "¿He publicado el tablero y lo que hará el sistema si nadie dice nada?"
    automatizable: si
  - id: gate-recorrido
    pregunta: "¿He recorrido cada comprobación de mi gate y anotado su resultado?"
    automatizable: si
no_autocertifica_ademas: []
```
