# APR/Promocion — de lo ocurrido a criterio

```yaml ads:metodo
id: APR/Promocion
nombre: Promocion
capacidad: APR
disparador:
  - "un item cierra con learning_candidate != none"
  - "un incidente: APR es obligatorio en todo INC"
  - "una revisión de circuito o una promoción a upstream"
carga:
  - "el item o incidente de origen, con su recorrido completo"
  - "los dos ledgers y el histórico de items"
  - "las reglas vigentes del kernel y de los packs instalados"
preguntas_iniciales:
  - "¿esto ha pasado antes? ¿cuándo, y dónde está registrado?"
  - "¿qué haría distinto el sistema la próxima vez si esta regla existiera?"
  - "¿esta regla sería igual de cierta en otro proyecto? ¿en otro de la misma clase?"
pasos:
  - n: 1
    nombre: BUSCAR OCURRENCIAS
    modo: divergente
    hace: >
      Buscar en el histórico y en los ledgers si esto ya ocurrió. Una regla se apoya en DOS
      ocurrencias, salvo que venga de un incidente.
    produce: "lista de ocurrencias con sus enlaces"
    termina_cuando: "hay dos ocurrencias enlazadas, o una y es un incidente, o consta que sólo hay una"
    checkpoint: true
  - n: 2
    nombre: DECIDIR SI ES PROMOVIBLE
    modo: convergente
    hace: >
      Si sólo hay una ocurrencia y no es incidente, el veredicto es «sin aprendizaje
      promovible», y se registra la observación sin convertirla en regla.
    produce: "veredicto de promovibilidad"
    termina_cuando: "el veredicto está escrito con su motivo"
    checkpoint: true
  - n: 3
    nombre: ESCRIBIR LA REGLA
    modo: convergente
    hace: >
      Enunciar qué hacer y CÓMO SE SABE si se hizo. Una regla que no se puede comprobar no
      cambia el comportamiento de nadie.
    produce: "regla candidata comprobable"
    termina_cuando: "la regla contiene una condición y su comprobación"
    checkpoint: true
  - n: 4
    nombre: ELEGIR LA CAPA
    modo: convergente
    hace: >
      Aplicar el test de contaminación: ¿sería igual de cierta en un proyecto de otra clase?
      → kernel. ¿En otro de la misma clase? → pack. ¿Sólo aquí? → proyecto.
    produce: "capa elegida con el test escrito"
    termina_cuando: "la capa está elegida y el razonamiento del test está escrito"
    checkpoint: true
  - n: 5
    nombre: COMPROBAR CONTRADICCIONES
    modo: lineal
    hace: >
      Buscar si alguna regla vigente dice lo contrario. Si la hay, se declara y se escala:
      no se añade la nueva encima.
    produce: "veredicto de compatibilidad"
    termina_cuando: "está comprobado que no contradice, o la contradicción está escalada"
    checkpoint: true
  - n: 6
    nombre: ESCRIBIR Y PROPONER
    modo: lineal
    hace: >
      Escribir la entrada del ledger y, cuando la capa es pack o kernel, el candidato a
      UPSTREAM. Proponer a la capacidad competente que actualice su memoria; no escribirla
      por ella.
    produce: "entrada de ledger y candidato a UPSTREAM cuando corresponde"
    termina_cuando: "gate:aprendizaje-fundado recorrido y anotado"
    checkpoint: true
artefactos:
  - "lista de ocurrencias"
  - "veredicto de promovibilidad"
  - "regla candidata comprobable"
  - "test de contaminación escrito"
  - "entrada de ledger"
puntos_owner:
  - "cola de validación por lotes cuando la regla afecta a materia de su autoridad"
consultas:
  - "la capacidad competente en la materia: ¿esta regla contradice algo que ya decidisteis? Responde sí o no, y qué"
  - "SIS: ¿esta regla exige cambiar una composición de ruta? Responde sí o no"
checkpoints:
  - "tras cada paso"
critica:
  - "¿estoy promoviendo una casualidad de un solo item?"
  - "¿esta regla se puede comprobar, o es un buen propósito?"
  - "¿estoy metiendo en el kernel una preferencia de este proyecto?"
  - "¿estoy escribiendo esto para justificar que el paquete de APR existió?"
gate: gate:aprendizaje-fundado
salida:
  - "entrada de ledger, o veredicto «sin aprendizaje promovible»"
devolucion:
  - "al propietario global, cuando el learning_candidate no tiene evidencia detrás"
bloqueo:
  - "el histórico no registró las ocurrencias anteriores y no son localizables"
cancelacion:
  - "la señal resulta ser un duplicado de un aprendizaje ya promovido: se enlaza y se cierra"
aprendizaje:
  - "un aprendizaje que hubo que revertir se registra con qué lo delató"
  - "una regla que nadie ha aplicado en seis meses es candidata a retirada (G52)"
prueba_de_reanudacion: >
  Un agente nuevo lee las ocurrencias ya reunidas y el veredicto de promovibilidad, y
  continúa. Es la prueba T117.
```
