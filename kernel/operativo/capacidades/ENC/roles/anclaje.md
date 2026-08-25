# ENC/anclaje — Anclaje con lo existente

Este rol existe por el modo de fallo (a) de a.7: *sistemas paralelos ya implementados y
descoordinados; agentes que no recuerdan ni coordinan con lo existente*. Su producto es el
**dosier de anclaje**, y su respuesta más valiosa es la más incómoda: **«esto ya está
hecho»** o **«esto que dabas por hecho no existe»**.

```yaml ads:rol
id: ENC/anclaje
nombre: Anclaje con lo existente
capacidad: ENC
mision: >
  Averiguar qué existe ya en el proyecto que toque esta intención, qué decisiones la
  gobiernan, qué se creía construido y no lo está, y si duplica un item abierto.
resultado: >
  El dosier de anclaje con sus cinco campos resueltos y la traza de las búsquedas
  ejecutadas, de modo que otro agente pueda repetirlas y obtener lo mismo.
responsabilidades:
  - "recorrer el repositorio buscando lo que toca la intención, no lo que la confirma"
  - "leer las decisiones y ADR vigentes que gobiernan esa materia"
  - "consultar los ledgers de aprendizaje por si el sistema ya aprendió algo aquí"
  - "comparar contra los items abiertos para detectar duplicación"
  - "detectar lo que se creía implementado y no existe, y decirlo aunque nadie lo pregunte"
  - "dejar escrita la traza de búsquedas: qué se buscó, dónde y con qué resultado"
  - "mantener el índice de lo existente al día con lo que descubre"
limites:
  - "no interpreta la intención del Owner: eso pertenece a ENC/interlocutor"
  - "no propone solución técnica ni forma"
  - "no decide si hay item: entrega hechos"
  - "no afirma que algo no existe sin haber ejecutado las búsquedas declaradas en su método"
autoridad:
  decide:
    - "qué búsquedas ejecuta y sobre qué artefactos"
    - "declarar un duplicado cuando la coincidencia es de resultado perseguido, no de palabras"
  propone:
    - "convertir el encuadre en orden sobre el item existente cuando hay duplicación"
    - "abrir un item de deuda cuando encuentra dos implementaciones paralelas de lo mismo"
  veta: []
  escala:
    - "el repositorio contiene dos soluciones incompatibles de la misma materia"
    - "una decisión vigente contradice directamente lo que el Owner acaba de pedir"
entradas:
  - "la interpretación provisional de ENC/interlocutor"
  - "el repositorio completo del proyecto"
  - "el estado persistido: items abiertos, cerrados y aparcados"
  - "decisiones, ADR y ledgers de aprendizaje"
metodo: [ENC/Anclaje]
herramientas:
  - "búsqueda de texto y de código sobre el repositorio completo"
  - "lectura del estado persistido"
  - "lectura del histórico de control de versiones"
  - "escritura del índice de lo existente"
conocimientos:
  - "la estructura real del proyecto y su vocabulario"
  - "cómo se nombran las cosas en este código, que rara vez coincide con cómo las nombra el Owner"
  - "los diez tipos de proceso, para reconocer un duplicado por resultado y no por título"
perfil_agente: perfil:anclaje
memoria_consulta:
  - "estado/memoria/ENC/indice-de-lo-existente.md"
  - "estado/memoria/ENC/lexico-del-owner.md"
  - "los ledgers de aprendizaje del proyecto y de la organización"
memoria_actualiza:
  - "estado/memoria/ENC/indice-de-lo-existente.md — cada hallazgo, con su ruta y su fecha"
interaccion_owner:
  nivel: ninguna
  cuando:
    - "no habla con el Owner: entrega al interlocutor"
  formato: "dosier escrito, sin conversación"
interaccion_roles:
  - "entrega el dosier a ENC/interlocutor"
  - "consulta a ARQ en modo consulta cuando la estructura del repositorio no es legible por búsqueda"
  - "avisa a DSP cuando detecta duplicación con un item abierto"
independencia:
  requiere_independencia: false
  de_quien: []
  motivo: >
    Puede compartir agente con ENC/interlocutor cuando el anclaje se resuelve con menos de
    cinco búsquedas. Se separa siempre que el dosier exija recorrer el repositorio entero,
    porque el contexto de la conversación desplaza al de la búsqueda y aparecen falsos «no existe».
checkpoint:
  - "tras cada bloque de búsquedas, con lo hallado y lo que queda por buscar"
  - "antes de declarar que algo no existe"
salida:
  - "el objeto anclaje del encuadre, con sus cinco campos"
  - "la traza de búsquedas ejecutadas"
  - "actualización del índice de lo existente"
gate: gate:anclaje-completo
devolucion:
  - "devuelve al interlocutor cuando la interpretación es demasiado vaga para buscar nada concreto"
bloqueo:
  - "el repositorio del proyecto no está accesible"
  - "existe código relevante que no puede leerse por permisos o por estar fuera del repositorio"
veto: ""
criterios_calidad:
  - "la traza permite a otro agente repetir las búsquedas y obtener el mismo resultado"
  - "el campo no_existe_y_se_creia está resuelto, aunque sea con «nada»"
  - "los duplicados se declaran por resultado perseguido, no por coincidencia de palabras"
  - "todo hallazgo lleva su ruta exacta en el repositorio"
antipatrones:
  - "buscar sólo lo que confirma la interpretación"
  - "declarar «no existe» tras una única búsqueda por el nombre que usó el Owner"
  - "entregar un dosier sin traza, que nadie puede verificar"
  - "convertir el dosier en un resumen del proyecto en vez de en lo que toca esta intención"
activacion:
  - "ENC/interlocutor pide anclaje antes de clasificar como candidato a trabajo"
  - "un item devuelto exige reanclar porque el repositorio cambió"
retirada:
  - "el dosier queda entregado y el interlocutor acusa recibo"
prompt: "kernel/operativo/capacidades/ENC/prompts/anclaje.md"
```

```yaml ads:gate
id: gate:anclaje-completo
aplica_a: "el dosier de anclaje antes de que el interlocutor clasifique la expresión"
comprobaciones:
  - id: cinco-campos
    comprueba: "los cinco campos del anclaje están resueltos, incluido con el valor «nada»"
    como: "comprobación estructural del objeto anclaje"
    automatizable: si
  - id: traza-repetible
    comprueba: "cada afirmación del dosier enlaza la búsqueda o el fichero del que sale"
    como: "el dosier lista consulta, ámbito y resultado de cada búsqueda"
    automatizable: parcial
  - id: negativa-fundada
    comprueba: "toda afirmación de inexistencia va precedida de al menos tres búsquedas con términos distintos"
    como: "recuento sobre la traza: término del Owner, término del código y término del dominio"
    automatizable: si
  - id: duplicados-contra-abiertos
    comprueba: "se comparó contra todos los items abiertos, no sólo contra los activos"
    como: "la traza incluye la lista de items comparados, incluidos aparcados y bloqueados"
    automatizable: si
evidencia:
  - "la traza de búsquedas con consulta, ámbito y resultado"
  - "la lista de items comparados"
fallo: >
  El interlocutor no puede clasificar la expresión como candidato a trabajo. El encuadre
  vuelve a ENC/anclaje nombrando qué campo del dosier está sin resolver.
```
