# DSP/Supervision — vigilar los frenos, y detener cuando toca

La cuarta función de `DSP` en a.3 —**Supervisión**— no tenía rol, ni método, ni
comprobación de gate. Los tres frenos de a.7 y el de b.9 aparecían citados en prosa y
nadie los contaba: un agente podía cerrar el gate de despacho sin haber evaluado una sola
devolución, un solo ciclo ni una sola racha, y el gate no se lo impedía (hallazgo **A-10**).

> **La supervisión no crea un equipo permanente nuevo.** Es un rol de `DSP`, que ya es
> permanente. La propiedad de ingeniería de los frenos —cambiar un umbral, añadir una
> señal— es de `SIS`, como todo lo que es la fábrica.

**Los números no se inventan aquí.** Son los ya aprobados: 2 devoluciones entre el mismo
par (a.7), 2 items SIS consecutivos (a.7), 3 recomposiciones sin avance material (b.9), 3
fallos de comparación e intercambio (a.9). Este método los cuenta; no los redefine.

```yaml ads:metodo
id: DSP/Supervision
nombre: Supervision
capacidad: DSP
disparador:
  - "cada ciclo de reconciliación, antes de seleccionar el siguiente trabajo (b.12 paso 4)"
  - "cada resultado emitido por una capacidad: devolución, bloqueo o cancelación"
  - "cada recomposición de ruta"
carga:
  - "el estado persistido completo: items, rutas, paquetes y eventos"
  - "los contadores persistidos de freno: devoluciones por par, rachas y recomposiciones"
  - "los tiempos de espera de cada paquete listo no despachado"
preguntas_iniciales:
  - "¿algún par de capacidades ha agotado sus dos devoluciones sobre el mismo paquete?"
  - "¿hay un ciclo de ruta que se repite atravesando tres o más capacidades?"
  - "¿cuántos items SIS consecutivos se han completado, y hay item de producto listo?"
  - "¿cuántas recomposiciones lleva esta ruta sin avance material?"
pasos:
  - n: 1
    nombre: CONTAR DEVOLUCIONES
    modo: lineal
    hace: >
      Por cada paquete vivo, contar las devoluciones entre el mismo PAR de capacidades. La
      primera es información y la segunda es desacuerdo; la tercera no se ejecuta.
    produce: "contador de devoluciones por par y por paquete"
    termina_cuando: "todo paquete vivo tiene su contador por par actualizado en el estado"
    checkpoint: false
  - n: 2
    nombre: DETECTAR CICLOS MULTIPARTE
    modo: lineal
    hace: >
      Recorrer la traza de custodias de cada paquete buscando una secuencia de tres o más
      capacidades que se repita. El freno no puede evitarse porque el rebote atraviese tres
      equipos en vez de dos.
    produce: "lista de ciclos detectados, con la secuencia repetida escrita"
    termina_cuando: "cada paquete vivo tiene su traza recorrida y su veredicto anotado"
    checkpoint: false
  - n: 3
    nombre: MEDIR LA RACHA SIS
    modo: lineal
    hace: >
      Contar items de tipo SIS completados consecutivamente y comprobar si existe al menos
      un item de producto listo para avanzar. Comprobar las tres excepciones declaradas en
      a.7 antes de aplicar el freno.
    produce: "racha SIS vigente, y si alguna excepción aplica"
    termina_cuando: "la racha está contada y las excepciones comprobadas una a una"
    checkpoint: false
  - n: 4
    nombre: MEDIR AVANCE MATERIAL
    modo: lineal
    hace: >
      Por cada ruta recompuesta, comprobar cuál de las SIETE señales de avance material de
      b.9 ha ocurrido desde la recomposición anterior. Renombrar, reordenar, reformular o
      añadir nodos sin evidencia NO cuentan.
    produce: "recomposiciones consecutivas sin avance material, por item"
    termina_cuando: "cada ruta recompuesta tiene su veredicto de avance con la señal citada"
    checkpoint: false
  - n: 5
    nombre: MEDIR INANICIÓN
    modo: lineal
    hace: >
      Por cada paquete listo no despachado, actualizar tiempo en espera, postergaciones,
      qué items lo adelantaron y qué recurso o condición lo impide.
    produce: "tabla de inanición"
    termina_cuando: "todo paquete listo no despachado tiene las cuatro cifras"
    checkpoint: false
  - n: 6
    nombre: DETECTAR ESTANCAMIENTO Y CONTRADICCIÓN
    modo: lineal
    hace: >
      Localizar paquetes en curso sin avance semántico en su checkpoint desde la última
      reconciliación, y contradicciones de estado: derivados divergentes de su
      source_revision, esperas que dejaron de ser viables, transiciones multiarchivo
      incompletas.
    produce: "lista de estancados y de contradicciones"
    termina_cuando: "cada paquete en curso tiene su veredicto y cada contradicción su ficha"
    checkpoint: false
  - n: 7
    nombre: DETENER Y ESCALAR
    modo: convergente
    hace: >
      Por cada freno disparado, DETENER lo que el freno detiene y escalar con las DOS
      posturas enfrentadas escritas: qué sostiene cada capacidad y por qué. A DSP si es
      problema de ruta; al Owner si es de fondo. Prohibido una tercera revisión muda, y
      prohibido que una capacidad ceda en silencio.
    produce: "registro de freno disparado, con las dos posturas y el destino del escalado"
    termina_cuando: >
      todo freno disparado tiene su registro con las dos posturas escritas y su destino, y
      ningún paquete afectado sigue despachándose
    checkpoint: true
  - n: 8
    nombre: PUBLICAR
    modo: lineal
    hace: >
      Proyectar en las vistas derivadas los contadores, la inanición y los frenos
      disparados, para que sean visibles sin herramienta.
    produce: "vistas derivadas con la sección de supervisión regenerada"
    termina_cuando: "la vista muestra contadores, inanición y frenos, y coincide con el estado"
    checkpoint: false
artefactos:
  - "contadores de devolución por par y por paquete"
  - "trazas de custodia con los ciclos detectados"
  - "racha SIS vigente y excepciones comprobadas"
  - "veredicto de avance material por recomposición"
  - "tabla de inanición con sus cuatro cifras"
  - "registro de cada freno disparado, con las dos posturas escritas"
puntos_owner:
  - "paso 7: se escala al Owner cuando el desacuerdo es de fondo, con ambas posturas escritas. No se le pide que arbitre sin material"
  - "paso 7: se escala al Owner cuando la racha SIS se detiene y él quiere decidir la excepción"
consultas:
  - "SIS: ¿este freno se dispara siempre en el mismo punto? Responde con los items afectados, para proponer revisión de circuito"
checkpoints:
  - "en el paso 7, antes de escalar, persistiendo qué freno se disparó y con qué contadores"
critica:
  - "¿he contado devoluciones entre PARES, o he sumado todas las del paquete?"
  - "¿he buscado ciclos de tres o más, o sólo rebotes entre dos?"
  - "¿he comprobado las tres excepciones de la racha SIS antes de detener?"
  - "¿he tratado como avance material algo que sólo era renombrar o reordenar?"
  - "¿he elevado alguna prioridad para resolver una inanición? Eso está prohibido"
gate: gate:despacho-coherente
salida:
  - "los contadores actualizados y proyectados"
  - "los frenos disparados, detenidos y escalados con las dos posturas"
devolucion:
  - "a la capacidad que emitió una devolución sin los cuatro campos de C5: no era una devolución y no cuenta para el freno"
bloqueo:
  - "el estado no permite contar: hay una transición multiarchivo incompleta que hay que resolver antes"
cancelacion:
  - "no aplica: la supervisión no cancela nada. Detecta, detiene y escala"
aprendizaje:
  - "un freno que se dispara siempre entre el mismo par señala un circuito mal definido, y se propone a SIS como revisión de circuito"
  - "una inanición persistente sin impedimento nombrable señala una regla de selección mal escrita"
prueba_de_reanudacion: >
  Los contadores viven en el estado persistido, no en la memoria del agente. Un supervisor
  nuevo los carga y obtiene los mismos veredictos que uno que llevara toda la sesión: el
  tercer rebote entre el mismo par sigue sin ejecutarse aunque el agente que contó los dos
  primeros ya no exista. Es la prueba T141.
```
