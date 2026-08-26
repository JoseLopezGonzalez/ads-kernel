# DOM/Condiciones — condiciones antes de construir

```yaml ads:metodo
id: DOM/Condiciones
nombre: Condiciones
capacidad: DOM
disparador:
  - "un item cumple C-DOM y ARQ ha depositado su plan, o el item no cumple C-ARQ"
  - "CON pregunta en modo consulta antes de tocar datos"
carga:
  - "el plan de ARQ o la especificación de lo que se va a construir"
  - "docs/dominio/VOCABULARIO.md e INVARIANTES.md"
  - "el esquema real de datos"
preguntas_iniciales:
  - "¿qué invariantes toca esto, y cómo se comprueban con una consulta?"
  - "¿qué contratos de datos cambian, y quién los consume hoy?"
  - "¿algún término nuevo significa lo mismo que uno que ya existe?"
pasos:
  - n: 1
    nombre: LOCALIZAR INVARIANTES
    modo: lineal
    hace: "Identificar qué invariantes declarados toca el cambio y cómo se comprueba cada uno."
    produce: "lista de invariantes afectados con su consulta de comprobación"
    termina_cuando: "cada invariante afectado tiene escrita la consulta que lo verifica"
    checkpoint: true
  - n: 2
    nombre: BUSCAR CONSUMIDORES
    modo: lineal
    hace: >
      Buscar en el repositorio quién consume cada contrato de datos que cambia. Se busca; no
      se recuerda.
    produce: "lista de consumidores con su ruta"
    termina_cuando: "ninguna búsqueda nueva añade consumidores"
    checkpoint: true
  - n: 3
    nombre: REVISAR VOCABULARIO
    modo: convergente
    hace: >
      Comprobar si el cambio introduce un término nuevo, y si ese término nombra algo que ya
      tiene otro nombre en el dominio.
    produce: "entradas nuevas de vocabulario, o constancia de que no hay ninguna"
    termina_cuando: "todo término nuevo está definido, con qué significa y qué NO"
    checkpoint: false
  - n: 4
    nombre: ESCRIBIR CONDICIONES
    modo: convergente
    hace: >
      Entregar a Construcción qué debe conservarse, qué transición necesita cada consumidor y
      qué está prohibido hacer con estos datos.
    produce: "condiciones de dominio del item"
    termina_cuando: "las condiciones son comprobables con una consulta o una prueba"
    checkpoint: true
artefactos:
  - "invariantes afectados con su consulta"
  - "lista de consumidores"
  - "vocabulario actualizado"
  - "condiciones de dominio"
puntos_owner:
  - "cuando un término del dominio resulta significar algo distinto de lo que el equipo creía"
consultas:
  - "ARQ: ¿qué contratos de datos toca este plan? Responde con la lista de ficheros"
  - "SEG: ¿alguno de estos campos es dato personal? Responde con la lista"
checkpoints:
  - "tras los pasos 1, 2 y 4"
critica:
  - "¿he buscado los consumidores o los he recordado?"
  - "¿mis condiciones se pueden comprobar, o son advertencias?"
  - "¿estoy vetando por preferencia estructural sin invariante que citar?"
gate: gate:dominio-conforme
salida:
  - "condiciones de dominio entregadas antes de construir"
devolucion:
  - "a ARQ, cuando el plan rompe un consumidor sin transición"
bloqueo:
  - "no hay acceso al esquema real"
cancelacion:
  - "el item se cancela antes de construir: las condiciones se conservan para el siguiente"
aprendizaje:
  - "un invariante que nadie había escrito y que este item reveló se añade a INVARIANTES.md"
  - "un consumidor que apareció tarde señala una zona del mapa sin documentar"
prueba_de_reanudacion: >
  Un agente nuevo lee los invariantes ya localizados y los consumidores ya buscados, y
  continúa. Es la prueba T104.
```
