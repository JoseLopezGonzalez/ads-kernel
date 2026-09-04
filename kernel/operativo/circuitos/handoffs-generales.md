# Handoffs entre las demás capacidades

Forma del handoff: [`C5`](../contratos/C5-HANDOFF.md). Los de Diseño están en
[`DIS-handoffs.md`](DIS-handoffs.md).

**La ENTREGA DE VUELTA de `DOM` y de `SEG`.** `b.16` da a esas dos capacidades una
participación DOBLE: condiciones antes de construir —`dom-a-con` y `seg-a-con`— y
**revisión después**. La ida estaba instanciada y la vuelta no, y sin instancia de vuelta la
mitad posterior de la participación no tenía forma de entregarse ni de rechazarse:
`ver-a-dom` y `ver-a-seg` la materializan. Su `cuando` está anclado al ANCLA que
[`../recorrido/01-PROCESOS.md`](../recorrido/01-PROCESOS.md) deriva para cada proceso —el
dosier de `VER`—, no a una estación escrita a mano.

```yaml ads:handoff
id: handoff:enc-a-dsp
de: ENC
a: DSP
cuando: "un encuadre alcanza el estado listo-para-dsp y pasa su gate"
entrega:
  - "el encuadre completo, con la expresión literal intacta"
  - "el dosier de anclaje con sus cinco campos"
  - "el tipo de proceso propuesto con su motivo"
  - "el nivel de intervención del Owner calculado, citando la fila de a.8"
comprueba_al_recibir:
  - "el tipo propuesto deriva del resultado perseguido, no de las capacidades previstas"
  - "el anclaje declara si duplica un item abierto"
  - "existe evidencia de cierre comprobable"
rechaza_si:
  - "falta el tipo de proceso propuesto: sin él no se puede componer ruta"
  - "el anclaje señala un duplicado que ENC no ha resuelto como orden"
devolucion: >
  DSP devuelve a ENC cuando falta un campo estructural del encuadre. NUNCA cambia la
  interpretación, el resultado perseguido ni la evidencia de cierre: eso es contenido.
evidencia_de_devolucion:
  - "el campo concreto que falta y por qué impide componer ruta"
owner: "ninguna: DSP crea el item y ENC informa después."
checkpoint: "DSP lee de ENC: las decisiones del Owner captadas, para no volver a preguntarlas."
```

```yaml ads:handoff
id: handoff:prd-a-arq
de: PRD
a: ARQ
cuando: "el item cumple C-ARQ y PRD ha depositado su capa"
entrega:
  - "alcance con su fuera de alcance"
  - "criterios de éxito y definición de fracaso"
  - "restricciones declaradas por el Owner con su origen"
comprueba_al_recibir:
  - "el alcance permite acotar qué se toca"
  - "los criterios no exigen decidir alcance para poder planificar"
rechaza_si:
  - "el fuera de alcance está vacío y el radio sería indeterminable"
devolucion: >
  ARQ devuelve a PRD cuando el alcance excluye contratos que hay que cambiar para
  conseguirlo, o cuando dos caminos cumplen igual el criterio y hay que decidir cuál importa.
evidencia_de_devolucion:
  - "el contrato que hay que tocar y por qué el alcance lo excluye"
  - "o los dos caminos con su coste"
owner: "ninguna: ARQ escala a PRD, y PRD traduce a consecuencias de producto."
checkpoint: "ARQ lee de PRD: qué quedó fuera de alcance, para no planificarlo."
```

```yaml ads:handoff
id: handoff:arq-a-con
de: ARQ
a: CON
cuando: "el plan está depositado y DSP ha creado los paquetes de construcción"
entrega:
  - "el radio medido con su traza"
  - "la alternativa elegida con su motivo y el ADR cuando lo hay"
  - "la descomposición con dependencias y paralelismo declarado"
comprueba_al_recibir:
  - "el plan no exige decidir nada de otra capa para poder ejecutarlo"
  - "las dependencias del paquete están cerradas con capa vigente"
rechaza_si:
  - "el plan deja huecos que obligarían a CON a decidir alcance, forma o modelo"
devolucion: >
  CON devuelve a ARQ cuando el plan no es ejecutable como está descrito, con qué parte
  concreta no lo es.
evidencia_de_devolucion:
  - "el paso del plan que no se puede ejecutar y por qué"
owner: "ninguna: en este tramo no hay materia de decisión del Owner."
checkpoint: "CON lee de ARQ: qué alternativas se descartaron, para no reintroducirlas."
```

```yaml ads:handoff
id: handoff:dom-a-con
de: DOM
a: CON
cuando: "el item cumple C-DOM y las condiciones se entregan ANTES de construir"
entrega:
  - "los invariantes que conservar, con la consulta que comprueba cada uno"
  - "los consumidores de cada contrato de datos que cambia"
  - "la migración probada con su ventana de incompatibilidad, cuando la hay"
comprueba_al_recibir:
  - "cada condición se puede comprobar con una consulta o una prueba concreta"
  - "la migración tiene reversión ejecutada, no sólo escrita"
rechaza_si:
  - "una condición es una advertencia y no una comprobación"
  - "la migración se declara reversible sin salida de reversión ejecutada"
devolucion: >
  CON devuelve a DOM cuando dos condiciones son incompatibles entre sí, o cuando la de
  seguridad y la de dominio se contradicen.
evidencia_de_devolucion:
  - "las dos condiciones y el caso en que no pueden cumplirse a la vez"
owner: "sólo cuando la única salida implica pérdida de datos: decide él, no DOM."
checkpoint: "CON lee de DOM: qué consultas debe ejecutar y guardar como evidencia."
```

```yaml ads:handoff
id: handoff:seg-a-con
de: SEG
a: CON
cuando: "el item cumple C-SEG, y siempre en items DEP antes de construir"
entrega:
  - "las condiciones de seguridad, comprobables una a una"
  - "la superficie que el cambio no debe abrir"
  - "el veredicto sobre las dependencias con su fecha"
comprueba_al_recibir:
  - "cada condición dice qué comprobar y cómo"
  - "las dependencias autorizadas están fijadas a una versión concreta"
rechaza_si:
  - "una condición no se puede comprobar sobre el código o la configuración"
devolucion: >
  CON devuelve a SEG cuando cumplir una condición exige una decisión de producto o de
  arquitectura que no le corresponde.
evidencia_de_devolucion:
  - "la condición y qué decisión ajena exigiría para cumplirse"
owner: "sólo cuando el riesgo es real y aceptable: lo presenta SEG, decide el Owner."
checkpoint: "CON lee de SEG: qué superficie no debe abrir, y qué comprobar antes de entregar."
```

```yaml ads:handoff
id: handoff:ver-a-ent
de: VER
a: ENT
cuando: "el dosier no tiene evidencia en rojo y el item cumple C-ENT"
entrega:
  - "el dosier con el veredicto por criterio"
  - "las diferencias declaradas y las deudas aceptadas"
  - "qué habría que mirar tras el despliegue"
comprueba_al_recibir:
  - "ningún criterio está en rojo"
  - "hay al menos una señal observable declarada"
rechaza_si:
  - "el dosier omite lo no comprobado"
  - "no hay ninguna señal que mirar tras el despliegue"
devolucion: >
  ENT devuelve a VER cuando lo desplegado se comporta distinto de lo verificado, adjuntando
  la observación del entorno real.
evidencia_de_devolucion:
  - "la comparación entre lo observado en el entorno real y el dosier"
owner: "la publicación es materia reservada suya (G05); el resto del tramo no lo es."
checkpoint: "ENT lee de VER: qué se comprobó y qué no, para saber qué vigilar de cerca."
```

```yaml ads:handoff
id: handoff:ent-a-uso
de: ENT
a: USO
cuando: "el cambio está desplegado y el item cumple C-USO"
entrega:
  - "el cambio corriendo, con su entorno y su commit"
  - "el registro de observación de la ventana"
  - "qué criterios quedaron sin verificar por VER"
comprueba_al_recibir:
  - "existe una fuente de uso real aplicable para lo que hay que validar"
  - "el estado del entorno permite preparar la validación de antemano"
rechaza_si:
  - "no hay ninguna de las siete fuentes disponible"
devolucion: >
  USO devuelve a la capacidad propietaria de la capa cuya insuficiencia revela el uso, no a
  ENT, salvo que el problema sea del despliegue.
evidencia_de_devolucion:
  - "la observación con sus condiciones: dispositivo, datos y momento"
owner: "es una de las siete fuentes; se le convoca por lotes, nunca item por item."
checkpoint: "USO lee de ENT: qué se observó ya durante la ventana, para no repetirlo."
```

```yaml ads:handoff
id: handoff:cierre-a-apr
de: DSP
a: APR
cuando: >
  el cierre del item resuelve learning_candidate con un enlace, o el item es un INC, o hay
  una revisión de circuito o una promoción. El emisor es DSP porque la comprobación de
  aprendizaje se ejecuta EN EL CIERRE (b.10) y quien crea el paquete de APR es quien crea
  paquetes. NO es USO: USO es condicional, y en un DEF, un DEU o un SIS no se activa,
  de modo que un handoff emitido por USO dejaba sin emisor a la mayoría de los cierres
entrega:
  - "el recorrido completo del item con su traza de ruta"
  - "la señal concreta: qué ocurrió y dónde está registrado"
  - "los hallazgos no previstos que el uso reveló"
comprueba_al_recibir:
  - "la señal tiene evidencia detrás, no es una impresión"
  - "se puede buscar si esto ha ocurrido antes"
rechaza_si:
  - "el learning_candidate se declaró sin evidencia que lo sostenga"
devolucion: >
  APR devuelve al propietario global cuando el candidato declarado no tiene evidencia. El
  cierre del item no espera: la comprobación de aprendizaje se ejecuta EN el cierre y APR
  sólo recibe paquete ante señal real.
evidencia_de_devolucion:
  - "qué evidencia falta para poder buscar ocurrencias"
owner: "cola de validación por lotes cuando la regla afecta a materia suya."
checkpoint: "APR lee del item: su traza de ruta completa, para localizar dónde nació la señal."
```

```yaml ads:handoff
id: handoff:con-a-ver
de: CON
a: VER
cuando: "CON deposita su capa y el paquete continúa hacia verificación"
entrega:
  - "el commit identificado y la salida de la suite de tests"
  - "las DIFERENCIAS conocidas respecto a la especificación, declaradas ANTES de la revisión"
  - "las consultas de dominio y de seguridad ejecutadas, con su salida"
  - "la evidencia de usabilidad sobre lo construido, cuando la capa toca una superficie usable"
comprueba_al_recibir:
  - "las diferencias declaradas llevan fecha ANTERIOR a la entrega: declararlas después es enterarse, no declarar"
  - "la suite pasa en el commit entregado, no en otro"
  - "cada criterio de éxito de PRD tiene comportamiento que lo satisface, o consta por qué no"
  - "las condiciones de DOM y de SEG que aplicaban están comprobadas, con su salida enlazada"
rechaza_si:
  - "las diferencias aparecen fechadas después de la entrega"
  - "la capa cambia una decisión de PRD, DIS o ARQ sin haberla devuelto"
  - "falta la evidencia de usabilidad de una superficie que la capa modificó"
devolucion: >
  VER devuelve a CON con la evidencia concreta: qué criterio no se cumple, con qué salida o
  medición se demuestra, y qué lo cerraría. Si lo que falla es una capa anterior y no la
  construcción, VER devuelve a la capacidad propietaria de esa capa, no a CON.
evidencia_de_devolucion:
  - "el criterio concreto que no se cumple, citado de la capa de PRD"
  - "la salida, captura o medición que lo demuestra"
  - "la comparación con el estado anterior cuando se alega regresión"
owner: "ninguna. Entre CON y VER no hay un humano validando el traspaso."
checkpoint: >
  VER lee de CON: qué está construido, qué diferencias se declararon y con qué fecha, y qué
  consultas quedaron ejecutadas. Sin eso no puede recoger evidencia sin volver a preguntar.
```

## La regla que atraviesa todos estos handoffs

```text
EL RECEPTOR COMPRUEBA ANTES DE TOMAR CUSTODIA.

Rechazar al recibir NO cuenta como devolución a efectos del freno de a.7: la capa nunca
se depositó. Aceptar y devolver DESPUÉS sí cuenta.

Esa distinción es lo que impide aceptar trabajo malo por cortesía y gastar después una de
las dos devoluciones disponibles en algo que era comprobable de entrada.
```

```yaml ads:handoff
id: handoff:ver-a-seg
de: VER
a: SEG
cuando: "el dosier de VER está depositado y el proceso exige la revisión posterior de SEG, sea porque C-SEG está activa o porque el proceso es DEP, donde no se retira"
entrega:
  - "el dosier de VER con la superficie realmente expuesta por lo construido"
  - "las condiciones de seguridad emitidas ANTES de construir, para poder confrontarlas"
  - "qué cambió entre lo que se planificó y lo que se construyó, con su alcance"
comprueba_al_recibir:
  - "la superficie expuesta se puede comparar contra el veredicto previo sin volver a leer el código"
  - "el dosier declara los estados extremos, que son donde la superficie aparece"
  - "consta si el cambio construido tocó algo que el veredicto previo no contemplaba"
rechaza_si:
  - "no hay veredicto previo con el que comparar: la revisión posterior no puede inventar la línea base"
  - "el dosier no permite decidir qué quedó expuesto y qué no"
devolucion: >
  SEG devuelve a VER cuando el dosier no permite decidir qué superficie quedó expuesta.
  NUNCA cambia el veredicto previo para que encaje: un veredicto que se reescribe hacia
  atrás deja de ser una línea base.
evidencia_de_devolucion:
  - "qué parte de la superficie no se puede juzgar con el dosier entregado"
owner: "el Owner decide sólo si la revisión encuentra un riesgo aceptable pero real; un veto no levantable por G27 NO admite su decisión."
checkpoint: "SEG lee de VER: qué se construyó de verdad, para no revisar el plan en vez del producto."
```

```yaml ads:handoff
id: handoff:ver-a-dom
de: VER
a: DOM
cuando: "el dosier de VER está depositado y C-DOM está activa, que es lo que hace exigible la revisión posterior de DOM en ese proceso"
entrega:
  - "el dosier de VER con los nombres y contratos del modelo tal como quedaron construidos"
  - "las condiciones de dominio emitidas ANTES de construir, para poder confrontarlas"
  - "qué migraciones o cambios de forma se ejecutaron, y si son reversibles"
comprueba_al_recibir:
  - "los nombres construidos significan lo que las condiciones de dominio dijeron que significaban"
  - "la reversibilidad declarada antes de construir sigue siendo cierta después"
  - "ninguna migración dejó estado que el modelo no sepa nombrar"
rechaza_si:
  - "no hay condiciones de dominio previas con las que comparar"
  - "el dosier no dice qué migraciones se ejecutaron ni si son reversibles"
devolucion: >
  DOM devuelve a VER cuando el dosier no permite comprobar la reversibilidad. NUNCA
  reinterpreta el modelo para que lo construido encaje: eso es cambiar el dominio para
  salvar una implementación.
evidencia_de_devolucion:
  - "qué propiedad del modelo no se puede comprobar con el dosier entregado"
owner: "obligatorio cuando la única salida implica pérdida de datos o indisponibilidad: esa elección es del Owner y DOM sólo la presenta con sus consecuencias."
checkpoint: "DOM lee de VER: qué se construyó de verdad, para revisar el modelo vivo y no el previsto."
```
