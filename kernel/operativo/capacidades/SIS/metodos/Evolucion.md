# SIS/Evolucion — cambiar la fábrica con prueba

```yaml ads:metodo
id: SIS/Evolucion
nombre: Evolucion
capacidad: SIS
disparador:
  - "DSP despacha un item SIS con su justificación de producto enlazada"
  - "APR promueve un aprendizaje a upstream"
carga:
  - "el item SIS y el problema de producto que lo justifica"
  - "el kernel operativo y las secciones normativas aprobadas"
  - "el estado real de las pruebas afectadas"
preguntas_iniciales:
  - "¿qué problema real de producto deja de existir con este cambio?"
  - "¿este cambio contradice alguna sección aprobada?"
  - "¿qué validador y qué prueba van a demostrar que funciona?"
pasos:
  - n: 1
    nombre: COMPROBAR LA JUSTIFICACIÓN
    modo: convergente
    hace: >
      Comprobar que el item enlaza un problema real, una fricción o una capacidad de producto.
      Sin ella, el item no se trabaja: es autorreferencia.
    produce: "justificación comprobada"
    termina_cuando: "el enlace existe y describe un problema que alguien ha tenido"
    checkpoint: true
  - n: 2
    nombre: BUSCAR CONTRADICCIÓN
    modo: lineal
    hace: >
      Comprobar si el cambio contradice una sección normativa aprobada. Si la contradice, se
      REGISTRA y se propone un cambio mínimo; no se modifica.
    produce: "veredicto de contradicción, y propuesta mínima cuando la hay"
    termina_cuando: "está comprobado, y toda contradicción está registrada"
    checkpoint: true
  - n: 3
    nombre: COMPROBAR FUENTE ÚNICA
    modo: lineal
    hace: >
      Comprobar que el cambio no crea una segunda fuente de una verdad que ya existe en otro
      fichero.
    produce: "veredicto de fuente única"
    termina_cuando: "la verdad afectada vive en un solo sitio, y los demás la enlazan"
    checkpoint: false
  - n: 4
    nombre: CAMBIAR
    modo: lineal
    hace: "Modificar el contrato, esquema, método, composición o plantilla que corresponda."
    produce: "el cambio"
    termina_cuando: "el cambio está escrito y es coherente con su bloque canónico"
    checkpoint: true
  - n: 5
    nombre: VALIDADOR
    modo: convergente
    hace: >
      Escribir o ampliar el validador que comprueba el cambio. Si no es automatizable, ESCRIBIR
      POR QUÉ y qué revisión humana lo cubre.
    produce: "regla de validador, o motivo escrito de no automatizable"
    termina_cuando: "el validador pasa sobre el corpus, o el motivo está escrito"
    checkpoint: true
  - n: 6
    nombre: PRUEBA CON ESTADO REAL
    modo: convergente
    hace: >
      Escribir el escenario y declarar su estado REAL: contrato definido, validador
      implementado, prueba ejecutada o prueba superada. Ninguna sube de estado por argumento.
    produce: "escenario con su estado real y su evidencia"
    termina_cuando: "el estado declarado corresponde con la evidencia enlazada"
    checkpoint: true
  - n: 7
    nombre: ENTREGAR SI TOCA RUNTIME
    modo: lineal
    hace: >
      Si el cambio modifica el runtime, entregarlo a ENT para activación segura y reversible
      (b.16).
    produce: "paquete de entrega, cuando corresponde"
    termina_cuando: "el cambio está activado de forma reversible, o consta que no toca el runtime"
    checkpoint: true
artefactos:
  - "justificación de producto comprobada"
  - "el cambio en el kernel operativo"
  - "la regla del validador"
  - "el escenario con su estado real"
puntos_owner:
  - "cuando el cambio contradice una sección aprobada: se le propone el cambio mínimo"
consultas:
  - "APR: ¿este aprendizaje se apoya en dos ocurrencias? Responde con los enlaces"
  - "la capacidad cuyo contrato se toca: ¿esto cambia tu autoridad? Responde sí o no"
checkpoints:
  - "tras los pasos 1, 2, 4, 5, 6 y 7"
critica:
  - "¿estoy cambiando el sistema por una fricción real o por elegancia?"
  - "¿he declarado superada alguna prueba que sólo he escrito?"
  - "¿he modificado algo aprobado en vez de registrar la contradicción?"
  - "¿he creado una segunda fuente de algo que ya estaba escrito?"
gate: gate:sistema-conforme
salida:
  - "kernel operativo modificado con validador y prueba"
devolucion:
  - "a APR, cuando el aprendizaje no tiene evidencia para cambiar un contrato"
bloqueo:
  - "el cambio exige decidir sobre una contradicción con una sección aprobada"
cancelacion:
  - "la fricción que lo justificaba desaparece: el item se cancela con enlace a lo que la resolvió"
aprendizaje:
  - "un contrato que hay que cambiar dos veces en poco tiempo estaba mal formulado"
  - "una prueba que nunca llega a ejecutarse señala una capacidad que el sistema no tiene"
prueba_de_reanudacion: >
  Un agente nuevo lee qué contratos están tocados y qué validadores se han ejecutado, y
  continúa. La comprobación es reejecutar los validadores: si pasan, el estado es coherente.
  Es la prueba T120.
```
