# SEG/Condiciones — condiciones antes, revisión después

```yaml ads:metodo
id: SEG/Condiciones
nombre: Condiciones
capacidad: SEG
disparador:
  - "un item cumple C-SEG"
  - "VER entrega una capa construida que tocaba superficie de seguridad"
carga:
  - "el plan de ARQ o la especificación"
  - "docs/seguridad/SUPERFICIE.md y CUMPLIMIENTO.md"
  - "la configuración real y las fuentes que exponen la superficie, cada una con su propio despliegue y sus propios secretos"
preguntas_iniciales:
  - "¿qué expone esto que antes no estaba expuesto?"
  - "¿qué acciones nuevas aparecen, y quién puede ejecutarlas?"
  - "¿algún campo de estos es dato personal?"
pasos:
  - n: 1
    nombre: DELIMITAR LA SUPERFICIE
    modo: lineal
    hace: "Escribir qué queda expuesto, a quién y por qué camino, comparado con lo que ya había."
    produce: "superficie del cambio"
    termina_cuando: "está escrito qué es nuevo respecto a SUPERFICIE.md, o que no hay nada nuevo"
    checkpoint: true
  - n: 2
    nombre: AUTORIZACIÓN
    modo: lineal
    hace: >
      Por cada acción nueva, exigir quién puede ejecutarla y cómo se comprueba, incluida la
      comprobación del lado del servidor.
    produce: "matriz de acciones y autorización"
    termina_cuando: "cada acción nueva tiene su comprobación declarada"
    checkpoint: true
  - n: 3
    nombre: DATOS PERSONALES
    modo: lineal
    hace: >
      Identificar qué campos son dato personal en el marco declarado del proyecto, y qué se
      hace con ellos: dónde se guardan, quién los ve, si salen en logs.
    produce: "lista de campos con su tratamiento"
    termina_cuando: "cada campo está clasificado, o consta que no hay ninguno"
    checkpoint: true
  - n: 4
    nombre: SECRETOS
    modo: lineal
    hace: "Comprobar que no hay credenciales ni secretos en código, configuración ni logs."
    produce: "salida de la comprobación de secretos"
    termina_cuando: "la comprobación pasa, o los hallazgos están corregidos y rotados"
    checkpoint: false
  - n: 5
    nombre: ENTREGAR CONDICIONES
    modo: convergente
    hace: >
      Escribir las condiciones que CON debe cumplir, comprobables una a una, antes de
      construir.
    produce: "condiciones de seguridad"
    termina_cuando: "cada condición se puede comprobar con una prueba o una lectura concreta"
    checkpoint: true
  - n: 6
    nombre: REVISAR DESPUÉS
    modo: convergente
    hace: >
      Tras la construcción, comprobar cada condición sobre lo construido y emitir veredicto,
      declarando lo que no se pudo comprobar.
    produce: "revisión posterior con veredicto"
    termina_cuando: "gate:seguridad-conforme recorrido y anotado"
    checkpoint: true
artefactos:
  - "superficie del cambio"
  - "matriz de acciones y autorización"
  - "lista de datos personales"
  - "salida de comprobación de secretos"
  - "condiciones y revisión posterior"
puntos_owner:
  - "cuando la única forma de conseguir lo pedido tiene una consecuencia de seguridad real y aceptable"
consultas:
  - "DOM: ¿alguno de estos campos identifica a una persona en el modelo? Responde con la lista"
  - "ARQ: ¿por qué caminos se puede llegar a esta acción? Responde con las rutas"
checkpoints:
  - "tras los pasos 1, 2, 3, 5 y 6"
critica:
  - "¿estoy vetando sin poder decir qué queda expuesto y por qué camino?"
  - "¿he comprobado la autorización del lado del servidor, o sólo la de la interfaz?"
  - "¿he mirado los logs, o sólo el código?"
gate: gate:seguridad-conforme
salida:
  - "condiciones antes de construir y revisión después"
devolucion:
  - "a CON o a ARQ, según de quién sea lo que expone"
bloqueo:
  - "no hay acceso a la configuración real"
cancelacion:
  - "el item se cancela: las condiciones se conservan para el siguiente que toque esa superficie"
aprendizaje:
  - "toda exposición encontrada entra en SUPERFICIE.md aunque se corrigiera en el acto"
  - "una condición que CON incumple dos veces señala una condición mal escrita"
prueba_de_reanudacion: >
  Un agente nuevo lee qué superficies están revisadas y continúa por las que faltan. Un veto
  emitido sigue vigente aunque cambie el agente: vive en el paquete, no en quien lo emitió.
  Es la prueba T114.
```
