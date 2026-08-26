# SEG/Dependencia — antes de incorporar nada de fuera

```yaml ads:metodo
id: SEG/Dependencia
nombre: Dependencia
capacidad: SEG
disparador:
  - "un item de tipo DEP incorpora o actualiza una dependencia"
  - "CON necesita una dependencia nueva para construir"
carga:
  - "la dependencia propuesta, con su versión exacta"
  - "docs/seguridad/DEPENDENCIAS.md"
preguntas_iniciales:
  - "¿qué problema resuelve, y qué alternativa hay sin incorporar nada?"
  - "¿qué trae consigo: qué otras dependencias arrastra?"
  - "¿qué avisos publicados tiene esta versión?"
pasos:
  - n: 1
    nombre: JUSTIFICAR
    modo: convergente
    hace: >
      Escribir qué resuelve y qué alternativa habría sin incorporarla. Una dependencia que
      sustituye a veinte líneas propias no se incorpora.
    produce: "justificación con alternativa considerada"
    termina_cuando: "está escrito por qué se incorpora en vez de resolverlo dentro"
    checkpoint: true
  - n: 2
    nombre: MIRAR LO QUE ARRASTRA
    modo: lineal
    hace: "Enumerar las dependencias transitivas que trae y su superficie."
    produce: "árbol de lo que se incorpora"
    termina_cuando: "el árbol está enumerado hasta el nivel que el pack declare"
    checkpoint: true
  - n: 3
    nombre: AVISOS Y MANTENIMIENTO
    modo: lineal
    hace: >
      Consultar avisos publicados de esa versión, y comprobar el estado de mantenimiento:
      última publicación, personas que la mantienen, ritmo de corrección.
    produce: "veredicto de riesgo con sus fuentes y su fecha"
    termina_cuando: "hay veredicto con fuentes comprobables"
    checkpoint: true
  - n: 4
    nombre: FIJAR Y REGISTRAR
    modo: convergente
    hace: >
      Fijar la versión exacta, registrar la incorporación con su fecha y su veredicto, y
      declarar qué la haría revisarse.
    produce: "entrada en DEPENDENCIAS.md"
    termina_cuando: "la entrada tiene versión, fecha, veredicto y condición de revisión"
    checkpoint: true
artefactos:
  - "justificación con alternativa"
  - "árbol de dependencias transitivas"
  - "veredicto de riesgo con fuentes"
  - "entrada en DEPENDENCIAS.md"
puntos_owner:
  - "cuando la dependencia es necesaria y su riesgo es real: decide el Owner con el coste delante"
consultas:
  - "ARQ: ¿existe alternativa dentro del sistema? Responde sí o no, y cuál"
  - "PLT: ¿esta dependencia afecta al tiempo de construcción o al tamaño del artefacto? Responde con la medición"
checkpoints:
  - "tras los pasos 1, 2, 3 y 4"
critica:
  - "¿estoy aprobando esto porque es popular?"
  - "¿he mirado lo que arrastra, o sólo la dependencia directa?"
  - "¿la alternativa de no incorporarla estaba realmente considerada?"
gate: gate:seguridad-conforme
salida:
  - "veredicto sobre la dependencia y entrada registrada"
devolucion:
  - "a CON o a ARQ, cuando existe alternativa dentro del sistema"
bloqueo:
  - "no hay forma de consultar avisos publicados para esa dependencia"
cancelacion:
  - "la dependencia se descarta: la justificación y el veredicto se conservan para la próxima vez que alguien la proponga"
aprendizaje:
  - "una dependencia que hubo que retirar entra en el ledger con qué la delató tarde"
  - "un aviso que apareció después de incorporarla ajusta la condición de revisión"
prueba_de_reanudacion: >
  Un agente nuevo lee el árbol ya enumerado y los avisos ya consultados con su fecha, y
  continúa. Es la prueba T115.
```
