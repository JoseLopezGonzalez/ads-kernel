# Los diez procesos y sus obligaciones

> **El proceso lo determina el RESULTADO PERSEGUIDO por el item, no las capacidades que se
> usan para obtenerlo** (b.1). Ésta es la regla de la que dependen las demás.

Las diez rutas de b.16, en forma canónica. Cada entrada de `obligatorias` **es** una
obligación del proceso: el runtime la instancia por item al componer la ruta, y
[`gate:cierre-de-item`](00-OBLIGACIONES-Y-CIERRE.md) comprueba su estado antes de dejar
cerrar nada.

Lo que aquí se fija y antes vivía sólo en prosa:

<!-- ads-lint-ignore-start: se CITA la expresión prohibida para decir que está prohibida -->
```text
QUÉ RESULTADO debe existir para cada obligación, y QUIÉN lo produce
QUÉ CRITERIO la satisface, comprobable por alguien que no la escribió
QUIÉN puede RETIRARLA — nunca DSP, porque retirar es autoridad semántica
QUÉ CONDICIÓN activa cada capacidad condicional, sin «si aplica»
```
<!-- ads-lint-ignore-end -->

Los circuitos concretos —qué comprueba quien recibe, qué pasa si falla— están en
[`../circuitos/00-CIRCUITOS.md`](../circuitos/00-CIRCUITOS.md). Aquí está el molde.


## `FEA` — Capacidad nueva

```yaml ads:proceso
id: proceso:FEA
nombre: Capacidad nueva
intencion: >
  Introducir una capacidad o un comportamiento que el producto NO tenía.
condicion_de_entrada: >
  No existe todavía, y el Owner o el uso real lo pide.
propietario_global: "PRD"
obligatorias:
  - id: intencion-definida
    capa_exigida: >
      la capa de PRD: para quién, qué cambia, qué queda fuera y qué haría que esto fuera un fracaso aunque funcione
    capacidad_productora: "PRD"
    criterio_de_satisfaccion: >
      existe criterio de éxito escrito que un tercero puede comprobar sin preguntar a quien lo escribió
    autoridad_de_retirada: >
      PRD, y el Owner cuando el alcance retirado es materia suya (a.8)
  - id: comportamiento-construido
    capa_exigida: >
      la capa de CON: el comportamiento existe y está probado en su nivel
    capacidad_productora: "CON"
    criterio_de_satisfaccion: >
      cada criterio de éxito de PRD tiene comportamiento construido que lo satisface, y la suite pasa
    autoridad_de_retirada: >
      PRD, porque retirar el comportamiento es retirar alcance
  - id: evidencia-suficiente
    capa_exigida: >
      el dosier de VER: evidencia juzgable por un humano, con los estados extremos
    capacidad_productora: "VER"
    criterio_de_satisfaccion: >
      existe dosier sin evidencia en rojo, con revisión independiente de quien construyó
    autoridad_de_retirada: >
      el Owner: entregar sin evidencia es decisión suya y queda registrada
condicionales:
  - capacidad: "DIS"
    condicion: "C-DIS"
  - capacidad: "ARQ"
    condicion: "C-ARQ"
  - capacidad: "DOM:condiciones"
    condicion: "C-DOM"
  - capacidad: "SEG:condiciones"
    condicion: "C-SEG"
  - capacidad: "ENT"
    condicion: "C-ENT"
  - capacidad: "USO"
    condicion: "C-USO"
  - capacidad: "APR"
    condicion: "C-APR"
evidencia_necesaria:
  - "el comportamiento nuevo funciona en las condiciones declaradas"
  - "la evidencia de los estados extremos"
criterio_de_cierre: >
  La capacidad existe, se acepta, y sus obligaciones están resueltas según b.10.
aprendizaje: >
  Sobre el producto: qué se aprendió de introducir esta capacidad.
```


## `GAP` — Expectativa o calidad ausente

```yaml ads:proceso
id: proceso:GAP
nombre: Expectativa o calidad ausente
intencion: >
  Reconciliar una expectativa, necesidad o nivel de calidad AUSENTE respecto a algo que ya existe.
condicion_de_entrada: >
  Existe algo, y no llega a lo que se esperaba de ello.
propietario_global: "PRD"
obligatorias:
  - id: distancia-medida
    capa_exigida: >
      la capa de PRD/Gap: la distancia entre lo pretendido y lo real, medida, no supuesta
    capacidad_productora: "PRD"
    criterio_de_satisfaccion: >
      está escrito qué se esperaba, qué hay, y cuánto falta, con un caso concreto que lo muestra
    autoridad_de_retirada: >
      PRD, y el Owner si la expectativa retirada era suya
  - id: hueco-cerrado
    capa_exigida: >
      la capa de CON que elimina la distancia medida
    capacidad_productora: "CON"
    criterio_de_satisfaccion: >
      la distancia medida en la capa de PRD ha desaparecido, comprobado con el mismo caso
    autoridad_de_retirada: >
      PRD, porque cerrar el hueco de otra manera es redefinir el alcance de la expectativa
  - id: evidencia-suficiente
    capa_exigida: >
      el dosier de VER sobre el hueco cerrado
    capacidad_productora: "VER"
    criterio_de_satisfaccion: >
      la evidencia muestra el antes y el después del caso que definió la distancia
    autoridad_de_retirada: >
      el Owner: renunciar a la evidencia de verificación es una decisión suya, y queda registrada con su alcance y su fecha
condicionales:
  - capacidad: "DIS"
    condicion: "C-DIS"
  - capacidad: "ARQ"
    condicion: "C-ARQ"
  - capacidad: "DOM:condiciones"
    condicion: "C-DOM"
  - capacidad: "SEG:condiciones"
    condicion: "C-SEG"
  - capacidad: "ENT"
    condicion: "C-ENT"
  - capacidad: "USO"
    condicion: "C-USO"
  - capacidad: "APR"
    condicion: "C-APR"
evidencia_necesaria:
  - "la distancia entre lo pretendido y lo real ha desaparecido"
criterio_de_cierre: >
  La expectativa queda satisfecha y sus obligaciones resueltas.
aprendizaje: >
  Sobre POR QUÉ apareció el hueco. Es la fuente más valiosa del sistema y se pierde si el item cierra sin ella.
```


## `DEF` — Defecto

```yaml ads:proceso
id: proceso:DEF
nombre: Defecto
intencion: >
  Restaurar un comportamiento esperado que ha dejado de cumplirse.
condicion_de_entrada: >
  Algo especificado no hace lo que su especificación dice.
propietario_global: "ARQ cuando C-ARQ es verdadera; CON en caso contrario"
obligatorias:
  - id: correccion-construida
    capa_exigida: >
      la capa de CON que restaura el comportamiento esperado
    capacidad_productora: "CON"
    criterio_de_satisfaccion: >
      el caso que reproducía el defecto ya no lo reproduce, y existe test que lo fija
    autoridad_de_retirada: >
      el Owner, si decide convivir con el defecto: queda registrado con su alcance
  - id: evidencia-suficiente
    capa_exigida: >
      el dosier de VER con la regresión comprobada
    capacidad_productora: "VER"
    criterio_de_satisfaccion: >
      existe evidencia del caso corregido y de que no ha aparecido regresión
    autoridad_de_retirada: >
      el Owner: renunciar a la evidencia de verificación es una decisión suya, y queda registrada con su alcance y su fecha
condicionales:
  - capacidad: "ARQ:diagnostico"
    condicion: "C-ARQ"
  - capacidad: "DIS"
    condicion: "C-DIS"
  - capacidad: "ENT"
    condicion: "C-ENT"
  - capacidad: "USO"
    condicion: "C-USO"
  - capacidad: "APR"
    condicion: "C-APR"
evidencia_necesaria:
  - "el comportamiento esperado vuelve a cumplirse"
  - "ninguna regresión detectada"
criterio_de_cierre: >
  El comportamiento esperado se cumple y sus obligaciones están resueltas. Si el diagnóstico revela C-PRD, el item CAMBIA DE PROCESO (b.1): no se amplía en silencio.
aprendizaje: >
  Por qué se coló: qué comprobación faltaba.
```


## `INC` — Incidente en uso real

```yaml ads:proceso
id: proceso:INC
nombre: Incidente en uso real
intencion: >
  Contener el daño en producción, entender la causa y devolver el servicio.
condicion_de_entrada: >
  Algo falla en uso real, con impacto observable.
propietario_global: "ENT"
obligatorias:
  - id: dano-contenido
    capa_exigida: >
      la capa de ENT/Contención: el daño deja de crecer
    capacidad_productora: "ENT"
    criterio_de_satisfaccion: >
      la señal roja que abrió el incidente ha dejado de empeorar, con la medición que lo muestra
    autoridad_de_retirada: >
      nadie: no se retira. Un incidente sin contención no cierra
  - id: causa-diagnosticada
    capa_exigida: >
      la capa de ARQ/Diagnóstico: la causa, no el síntoma
    capacidad_productora: "ARQ"
    criterio_de_satisfaccion: >
      la causa explica TODOS los síntomas observados, y se nombra el mecanismo
    autoridad_de_retirada: >
      el Owner, si decide cerrar sin causa: queda registrado como riesgo asumido
  - id: correccion-construida
    capa_exigida: >
      la capa de CON que elimina la causa
    capacidad_productora: "CON"
    criterio_de_satisfaccion: >
      la causa diagnosticada ya no puede producirse, con test que lo fija
    autoridad_de_retirada: >
      el Owner: renunciar a la evidencia de verificación es una decisión suya, y queda registrada con su alcance y su fecha
  - id: evidencia-suficiente
    capa_exigida: >
      el dosier de VER sobre la corrección
    capacidad_productora: "VER"
    criterio_de_satisfaccion: >
      evidencia en verde del caso del incidente y de su regresión
    autoridad_de_retirada: >
      el Owner: renunciar a la evidencia de verificación es una decisión suya, y queda registrada con su alcance y su fecha
  - id: servicio-restaurado
    capa_exigida: >
      la capa de ENT/reentrega: el servicio funciona en el entorno real
    capacidad_productora: "ENT"
    criterio_de_satisfaccion: >
      observado durante la ventana declarada, sin la señal roja. Un rollback que restaura el servicio SATISFACE esta obligación; decidir NO reentregar es RETIRARLA, y son cosas distintas
    autoridad_de_retirada: >
      el Owner: no reentregar es decisión suya
  - id: aprendizaje-registrado
    capa_exigida: >
      la entrada de APR en el ledger
    capacidad_productora: "APR"
    criterio_de_satisfaccion: >
      existe entrada con la regla candidata y su evidencia, o el veredicto sin aprendizaje promovible con su motivo
    autoridad_de_retirada: >
      nadie: es el único proceso donde APR es obligatorio, porque un incidente sin aprendizaje se repite
condicionales:
  - capacidad: "SEG:condiciones"
    condicion: "C-SEG"
  - capacidad: "USO"
    condicion: "C-USO"
evidencia_necesaria:
  - "el servicio se comporta como debía en el entorno real, durante la ventana declarada"
criterio_de_cierre: >
  El servicio está restaurado, la causa eliminada y el aprendizaje registrado.
aprendizaje: >
  Obligatorio. Un incidente sin aprendizaje registrado se repite.
```


## `INV` — Investigación

```yaml ads:proceso
id: proceso:INV
nombre: Investigación
intencion: >
  Producir CONOCIMIENTO que permita decidir algo que hoy no puede decidirse.
condicion_de_entrada: >
  Existe una decisión que no puede tomarse porque falta evidencia.
propietario_global: "INV"
obligatorias:
  - id: evidencia-producida
    capa_exigida: >
      la capa de INV: la evidencia que responde a la pregunta declarada
    capacidad_productora: "INV"
    criterio_de_satisfaccion: >
      la pregunta del encuadre tiene respuesta apoyada en evidencia reproducible, o consta que NO puede responderse todavía y por qué
    autoridad_de_retirada: >
      el Owner, si retira la pregunta
condicionales:
  - capacidad: "CON:experimental"
    condicion: "la evidencia exige construir un spike, prototipo o banco de pruebas"
  - capacidad: "PRD"
    condicion: "el destino declarado es una decisión de producto"
  - capacidad: "ARQ"
    condicion: "el destino declarado es una decisión técnica"
  - capacidad: "APR"
    condicion: "C-APR"
evidencia_necesaria:
  - "la evidencia es reproducible por alguien que no la produjo"
criterio_de_cierre: >
  La pregunta tiene respuesta, o consta que no puede responderse. Un INV PUEDE cerrar SIN generar un segundo item: la evidencia es el resultado.
aprendizaje: >
  Qué se aprendió del método, no sólo del resultado.
```


## `DEU` — Deuda técnica

```yaml ads:proceso
id: proceso:DEU
nombre: Deuda técnica
intencion: >
  Reducir riesgo interno o coste de cambio, sin introducir capacidad de producto.
condicion_de_entrada: >
  Algo funciona y su forma interna encarece o arriesga todo lo que venga después.
propietario_global: "ARQ"
obligatorias:
  - id: plan-tecnico
    capa_exigida: >
      la capa de ARQ: qué se cambia, con radio de impacto MEDIDO
    capacidad_productora: "ARQ"
    criterio_de_satisfaccion: >
      el radio de impacto está medido y no estimado, con la lista de ficheros y contratos afectados
    autoridad_de_retirada: >
      ARQ, y el Owner si el coste retirado cambia una prioridad suya
  - id: cambio-construido
    capa_exigida: >
      la capa de CON que ejecuta el plan
    capacidad_productora: "CON"
    criterio_de_satisfaccion: >
      lo construido corresponde al plan, sin cambio de comportamiento observable no declarado
    autoridad_de_retirada: >
      ARQ, que es quien fijó el plan y quien responde de la reducción de riesgo
  - id: evidencia-suficiente
    capa_exigida: >
      el dosier de VER sin regresión
    capacidad_productora: "VER"
    criterio_de_satisfaccion: >
      evidencia de que el comportamiento observable no cambió, salvo donde el plan lo declaraba
    autoridad_de_retirada: >
      el Owner: renunciar a la evidencia de verificación es una decisión suya, y queda registrada con su alcance y su fecha
condicionales:
  - capacidad: "DOM:condiciones"
    condicion: "C-DOM"
  - capacidad: "SEG:condiciones"
    condicion: "C-SEG"
  - capacidad: "ENT"
    condicion: "C-ENT"
  - capacidad: "USO"
    condicion: "C-USO"
  - capacidad: "APR"
    condicion: "C-APR"
evidencia_necesaria:
  - "ausencia de regresión perceptible"
  - "el riesgo o el coste declarado se ha reducido de forma medible"
criterio_de_cierre: >
  El riesgo interno declarado se ha reducido, sin capacidad de producto nueva. Activar USO no convierte la deuda en feature.
aprendizaje: >
  Por qué se acumuló la deuda: qué decisión la generó.
```


## `DEP` — Dependencia

```yaml ads:proceso
id: proceso:DEP
nombre: Dependencia
intencion: >
  Incorporar, actualizar o retirar una dependencia externa sin abrir una superficie.
condicion_de_entrada: >
  Una dependencia externa entra, cambia de versión o sale.
propietario_global: "PLT"
obligatorias:
  - id: condiciones-de-seguridad
    capa_exigida: >
      la capa de SEG/Dependencia ANTES de construir
    capacidad_productora: "SEG"
    criterio_de_satisfaccion: >
      existe veredicto fechado sobre la dependencia, con su riesgo conocido y su mitigación o la constancia de que no existe
    autoridad_de_retirada: >
      nadie: G28 lo hace obligatorio en este proceso y no se retira
  - id: cambio-construido
    capa_exigida: >
      la capa de CON que incorpora o retira la dependencia
    capacidad_productora: "CON"
    criterio_de_satisfaccion: >
      la dependencia está en la versión declarada y el proyecto construye y pasa su suite
    autoridad_de_retirada: >
      PLT, que posee la maquinaria y responde de la dependencia incorporada
  - id: evidencia-suficiente
    capa_exigida: >
      el dosier de VER sobre el cambio
    capacidad_productora: "VER"
    criterio_de_satisfaccion: >
      evidencia de que nada que dependiera de ella se ha roto
    autoridad_de_retirada: >
      el Owner: renunciar a la evidencia de verificación es una decisión suya, y queda registrada con su alcance y su fecha
condicionales:
  - capacidad: "DOM:condiciones"
    condicion: "C-DOM"
  - capacidad: "ARQ"
    condicion: "el cambio de versión altera contratos"
  - capacidad: "ENT"
    condicion: "C-ENT"
evidencia_necesaria:
  - "el veredicto de seguridad, fechado y anterior a la construcción"
criterio_de_cierre: >
  La dependencia está en su sitio, con su veredicto de seguridad y sin superficie nueva expuesta.
aprendizaje: >
  Qué señal habría avisado antes de que esta dependencia era un riesgo.
```


## `AUD` — Auditoría de un proyecto existente

```yaml ads:proceso
id: proceso:AUD
nombre: Auditoría de un proyecto existente
intencion: >
  Producir una CONCLUSIÓN sobre un objeto ya existente, para que alguien decida con ella.
condicion_de_entrada: >
  El Owner o una capacidad necesita saber en qué estado está algo que ya existe.
propietario_global: "DERIVADO del encargo: la capacidad responsable de la conclusión perseguida, o de la decisión que la consumirá. NUNCA se asigna a mano"
obligatorias:
  - id: conclusion-fundada
    capa_exigida: >
      la capa de INV: la conclusión, con la evidencia que la sostiene
    capacidad_productora: "INV"
    criterio_de_satisfaccion: >
      la conclusión responde a la pregunta declarada en el encuadre, y su consumidor puede actuar con ella sin pedir más
    autoridad_de_retirada: >
      el consumidor de la conclusión declarado en el encuadre
condicionales:
  - capacidad: "DOM"
    condicion: "C-DOM"
  - capacidad: "SEG"
    condicion: "C-SEG"
  - capacidad: "DIS"
    condicion: "C-DIS"
  - capacidad: "PRD"
    condicion: "la auditoría produce una decisión de producto"
  - capacidad: "APR"
    condicion: "C-APR"
evidencia_necesaria:
  - "la evidencia mínima declarada en los siete campos del encargo"
criterio_de_cierre: >
  La conclusión existe, su consumidor la ha recibido y los items nuevos que genera están creados. AUD no activa CON y PUEDE cerrar en APR sin pasar por PRD.
aprendizaje: >
  Qué reveló la auditoría sobre cómo se llegó hasta ahí.
```


## `DIR` — Cambio de dirección

```yaml ads:proceso
id: proceso:DIR
nombre: Cambio de dirección
intencion: >
  DECIDIR y registrar una dirección nueva con conocimiento de su impacto. No implementarla.
condicion_de_entrada: >
  El Owner quiere sustituir una dirección ya decidida.
propietario_global: "la capacidad PROPIETARIA de la decisión que se sustituye; con varias decisiones inseparables, la que el OWNER declare líder. NUNCA lo elige DSP"
obligatorias:
  - id: radio-de-impacto
    capa_exigida: >
      la capa de ARQ: qué alcanza la nueva dirección, medido
    capacidad_productora: "ARQ"
    criterio_de_satisfaccion: >
      existe la lista de decisiones, contratos y superficies afectadas, y ningún impacto detectado queda sin propietario
    autoridad_de_retirada: >
      el Owner: renunciar a la evidencia de verificación es una decisión suya, y queda registrada con su alcance y su fecha
  - id: decision-del-owner
    capa_exigida: >
      la decisión registrada con las palabras del Owner
    autoridad_productora: "OWNER"
    criterio_de_satisfaccion: >
      la dirección nueva y su criterio de éxito están escritos sin ambigüedad
    autoridad_de_retirada: >
      nadie: sin decisión del Owner no hay DIR
  - id: sustituciones-registradas
    capa_exigida: >
      el registro de qué decisiones anteriores quedan sustituidas
    capacidad_productora: "la capacidad propietaria de cada decisión sustituida"
    capacidad_productora_derivada: true
    criterio_de_satisfaccion: >
      cada decisión sustituida está identificada y enlazada a la que la reemplaza
    autoridad_de_retirada: >
      el Owner: renunciar a la evidencia de verificación es una decisión suya, y queda registrada con su alcance y su fecha
  - id: items-derivados
    capa_exigida: >
      los items enlazados que ejecutarán la dirección
    capacidad_productora: "DSP"
    criterio_de_satisfaccion: >
      cada consecuencia ejecutable está cubierta por un item derivado que enlaza a DIR y a la decisión concreta que ejecuta
    autoridad_de_retirada: >
      el Owner: renunciar a la evidencia de verificación es una decisión suya, y queda registrada con su alcance y su fecha
  - id: decision-verificada
    capa_exigida: >
      la capa de VER/Decisión: el resultado de DIR es íntegro, coherente, trazable y ejecutable
    capacidad_productora: "VER"
    criterio_de_satisfaccion: >
      las nueve comprobaciones de VER:decisión están recorridas y anotadas
    autoridad_de_retirada: >
      nadie: un DIR no cierra sin VER:decisión con capa vigente
condicionales:
  - capacidad: "DIS"
    condicion: "C-DIS"
  - capacidad: "CON:experimental"
    condicion: "hace falta un prototipo PARA PODER DECIDIR"
  - capacidad: "APR"
    condicion: "C-APR"
evidencia_necesaria:
  - "el radio de impacto medido"
  - "el registro de sustituciones"
  - "los items derivados con sus enlaces"
criterio_de_cierre: >
  La decisión está tomada, registrada, descompuesta en items ejecutables y verificada por VER:decisión. CON, VER, ENT y USO PRODUCTIVOS no son obligatorios: ninguna construcción productiva puede vivir dentro de un DIR.
aprendizaje: >
  Qué hizo falta para decidir, y qué se supo tarde.
```


## `SIS` — Evolución del sistema

```yaml ads:proceso
id: proceso:SIS
nombre: Evolución del sistema
intencion: >
  Cambiar la propia fábrica: memoria, plantillas, catálogo, composiciones o runtime.
condicion_de_entrada: >
  Una fricción real, un incidente del sistema o una capacidad de producto bloqueada lo exigen.
propietario_global: "SIS"
obligatorias:
  - id: cambio-de-sistema
    capa_exigida: >
      la capa de SIS: qué cambia en la fábrica y por qué
    capacidad_productora: "SIS"
    criterio_de_satisfaccion: >
      el item enlaza el problema real, la fricción o la capacidad de producto que justifica su existencia. Sin ese enlace no se trabaja
    autoridad_de_retirada: >
      el Owner: renunciar a la evidencia de verificación es una decisión suya, y queda registrada con su alcance y su fecha
  - id: cambio-construido
    capa_exigida: >
      la capa de CON que implementa el cambio del sistema
    capacidad_productora: "CON"
    criterio_de_satisfaccion: >
      lo construido corresponde a lo declarado por SIS y sus validadores pasan
    autoridad_de_retirada: >
      SIS, que es la dueña de la fábrica y quien responde de su coherencia
  - id: evidencia-suficiente
    capa_exigida: >
      el dosier de VER sobre el cambio del sistema
    capacidad_productora: "VER"
    criterio_de_satisfaccion: >
      existe validador o guion que comprueba el cambio, con su estado real de prueba registrado
    autoridad_de_retirada: >
      el Owner: renunciar a la evidencia de verificación es una decisión suya, y queda registrada con su alcance y su fecha
condicionales:
  - capacidad: "ENT"
    condicion: "el cambio modifica el runtime: activación segura y reversible"
  - capacidad: "APR"
    condicion: "C-APR"
evidencia_necesaria:
  - "el validador nuevo o modificado, con su estado real de prueba"
criterio_de_cierre: >
  La fábrica cambió, el cambio está comprobado y su justificación de producto está enlazada. Sujeto al freno de racha SIS de a.7.
aprendizaje: >
  Qué fricción lo motivó, para saber si desapareció.
```
