# ENC/Anclaje — averiguar qué existe ya

```yaml ads:metodo
id: ENC/Anclaje
nombre: Anclaje
capacidad: ENC
disparador:
  - "ENC/Escucha llega a su paso 4 con una expresión candidata a trabajo"
  - "un item devuelto exige reanclar porque el control repo o alguna fuente cambiaron desde el encuadre"
carga:
  - "estado/memoria/ENC/indice-de-lo-existente.md"
  - "estado/memoria/ENC/lexico-del-owner.md — para traducir el término del Owner al del código"
  - "la lista completa de items abiertos, incluidos aparcados y bloqueados"
  - "las decisiones y ADR vigentes"
preguntas_iniciales:
  - "¿cómo llama el Owner a esto, y cómo se llama en el código?"
  - "¿qué tres términos distintos hay que buscar: el del Owner, el del dominio y el del código?"
pasos:
  - n: 1
    nombre: TRADUCIR
    modo: lineal
    hace: >
      Producir la lista de términos de búsqueda: el del Owner, el del dominio del negocio y
      el probable del código. Sin los tres, una búsqueda negativa no vale nada.
    produce: "lista de términos, mínimo tres"
    termina_cuando: "hay al menos tres términos distintos escritos"
    checkpoint: false
  - n: 2
    nombre: BUSCAR LO IMPLEMENTADO
    modo: divergente
    hace: >
      Ejecutar las búsquedas sobre el control repo y sobre las fuentes materializadas, y registrar consulta, ámbito y
      resultado de cada una. Se busca lo que contradice la interpretación, no sólo lo que
      la confirma.
    produce: "traza de búsquedas y lista de artefactos que tocan la intención"
    termina_cuando: "los tres términos están buscados y sus resultados registrados"
    checkpoint: true
  - n: 3
    nombre: LEER DECISIONES
    modo: lineal
    hace: >
      Localizar decisiones, ADR y patrones vigentes que gobiernen esta materia, y anotar
      cuáles la condicionan.
    produce: "anclaje.decisiones_que_gobiernan"
    termina_cuando: "cada decisión localizada tiene enlace y estado de vigencia"
    checkpoint: true
  - n: 4
    nombre: CONSULTAR APRENDIZAJE
    modo: lineal
    hace: >
      Buscar en los ledgers si el sistema ya aprendió algo sobre esta materia, incluido un
      intento anterior que salió mal.
    produce: "anclaje.aprendizajes"
    termina_cuando: "los ledgers están consultados y el resultado escrito, aunque sea vacío"
    checkpoint: false
  - n: 5
    nombre: COMPARAR CON ITEMS ABIERTOS
    modo: convergente
    hace: >
      Comparar por RESULTADO PERSEGUIDO, no por título, contra todos los items abiertos.
      Un item aparcado que persigue lo mismo es duplicación igual que uno activo.
    produce: "anclaje.duplica y la lista de items comparados"
    termina_cuando: "todos los items abiertos están comparados"
    checkpoint: true
  - n: 6
    nombre: DECLARAR LO QUE NO EXISTE
    modo: convergente
    hace: >
      Escribir qué se daba por implementado y no lo está. Es el campo más valioso del
      dosier y el que más veces sale vacío por comodidad.
    produce: "anclaje.no_existe_y_se_creia"
    termina_cuando: "el campo está resuelto, con valor concreto o con «nada detectado» y la traza que lo sostiene"
    checkpoint: true
  - n: 7
    nombre: ACTUALIZAR EL ÍNDICE
    modo: lineal
    hace: >
      Incorporar al índice de lo existente cada hallazgo nuevo, con su ruta y su fecha.
    produce: "índice de lo existente actualizado"
    termina_cuando: "los hallazgos nuevos están en el índice"
    checkpoint: false
artefactos:
  - "traza de búsquedas: consulta, ámbito, resultado"
  - "lista de items comparados"
  - "objeto anclaje con sus cinco campos"
  - "actualización del índice de lo existente"
puntos_owner:
  - "ninguno: este método no habla con el Owner"
consultas:
  - "ARQ en modo consulta cuando la estructura de una fuente no es legible por búsqueda de texto"
checkpoints:
  - "tras los pasos 2, 3, 5 y 6"
  - "antes de declarar que algo no existe"
critica:
  - "¿se buscó con los tres términos, o sólo con el del Owner?"
  - "¿la comparación de duplicados fue por resultado perseguido o por coincidencia de palabras?"
  - "¿se compararon también los items aparcados y bloqueados?"
  - "¿alguna afirmación del dosier carece de traza?"
gate: gate:anclaje-completo
salida:
  - "objeto anclaje del encuadre"
  - "traza de búsquedas"
  - "índice de lo existente actualizado"
devolucion:
  - "al interlocutor, cuando la interpretación es tan vaga que no permite formular términos de búsqueda"
bloqueo:
  - "el control repo no está accesible"
  - "existe código relevante en una fuente no declarada, no materializada o sin acceso"
cancelacion:
  - "el interlocutor descarta la expresión antes de terminar el anclaje: se conserva la traza parcial"
aprendizaje:
  - "cada término nuevo del Owner traducido al del código se incorpora al léxico"
  - "dos implementaciones paralelas de lo mismo generan un candidato de tipo DEU"
prueba_de_reanudacion: >
  Un agente nuevo abre el paquete, lee la traza de búsquedas ya ejecutadas y continúa por
  los términos que faltan sin repetir los hechos. La prueba es T81: se interrumpe tras el
  paso 2 y el agente entrante no vuelve a ejecutar las búsquedas registradas.
```
