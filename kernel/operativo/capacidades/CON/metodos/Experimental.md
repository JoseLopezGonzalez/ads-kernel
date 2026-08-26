# CON/Experimental — construir para saber, no para entregar

```yaml ads:metodo
id: CON/Experimental
nombre: Experimental
capacidad: CON
disparador:
  - "un item INV necesita construir para obtener evidencia"
  - "un item DIR necesita un prototipo PARA DECIDIR"
carga:
  - "la pregunta acotada que el experimento debe contestar"
  - "experimentos anteriores sobre la misma materia"
preguntas_iniciales:
  - "¿qué medición o qué observación contestaría la pregunta?"
  - "¿qué es lo mínimo que hay que construir para obtenerla?"
  - "¿qué pasa con este código cuando termine?"
pasos:
  - n: 1
    nombre: DECLARAR ANTES
    modo: lineal
    hace: >
      Escribir qué evidencia debe producir el experimento y cuál es el criterio de descarte
      o conservación. Los dos, antes de la primera línea.
    produce: "declaración de evidencia y criterio de descarte"
    termina_cuando: "ambos están escritos y el criterio no depende del resultado"
    checkpoint: true
  - n: 2
    nombre: AISLAR
    modo: lineal
    hace: >
      Preparar un entorno donde construir sin tocar el producto, e identificar el artefacto
      como experimental de forma visible en el propio código.
    produce: "entorno aislado y artefacto identificado"
    termina_cuando: "el artefacto no es alcanzable desde el producto ni desplegable con él"
    checkpoint: false
  - n: 3
    nombre: CONSTRUIR LO MÍNIMO
    modo: lineal
    hace: >
      Construir sólo lo necesario para obtener la evidencia, declarando qué queda simulado.
    produce: "artefacto experimental"
    termina_cuando: "la evidencia se puede obtener y lo simulado está declarado"
    checkpoint: true
  - n: 4
    nombre: MEDIR
    modo: lineal
    hace: >
      Obtener la evidencia declarada, registrando también los resultados que contradicen la
      hipótesis. Ocultarlos invalida el experimento.
    produce: "evidencia con sus mediciones"
    termina_cuando: "la pregunta tiene respuesta, aunque sea negativa o no concluyente"
    checkpoint: true
  - n: 5
    nombre: EJECUTAR EL CRITERIO
    modo: convergente
    hace: >
      Aplicar el criterio de descarte declarado en el paso 1. Si algo debe conservarse, se
      propone un ITEM NUEVO ENLAZADO; nunca se integra desde aquí.
    produce: "artefacto descartado, o propuesta de item nuevo enlazado"
    termina_cuando: "el destino del artefacto está ejecutado o propuesto"
    checkpoint: true
artefactos:
  - "declaración de evidencia y criterio de descarte"
  - "artefacto experimental aislado"
  - "evidencia con mediciones"
puntos_owner:
  - "ninguno directo"
consultas:
  - "PLT: ¿hay entorno aislado disponible? Responde sí o no, y dónde"
checkpoints:
  - "tras los pasos 1, 3, 4 y 5"
critica:
  - "¿mi criterio de descarte lo escribí antes o lo estoy escribiendo ahora que veo el resultado?"
  - "¿estoy presentando como medido algo que está simulado?"
  - "¿estoy abandonando el experimento porque la evidencia no me gusta?"
gate: gate:implementacion-completa
salida:
  - "evidencia entregada a INV o al propietario del DIR"
  - "artefacto descartado o propuesto para conservar mediante item nuevo"
devolucion:
  - "a INV, cuando la pregunta no permite diseñar un experimento que la conteste"
bloqueo:
  - "no hay entorno aislado disponible"
cancelacion:
  - "la decisión que motivaba el experimento se toma por otra vía: se registra la evidencia parcial"
aprendizaje:
  - "todo experimento entra en docs/investigacion con su respuesta, incluida la negativa"
  - "un experimento cuya evidencia se ignoró se registra: es señal de decisión ya tomada de antemano"
prueba_de_reanudacion: >
  Un agente nuevo lee el criterio de descarte declarado y las mediciones ya obtenidas, y
  continúa. Si el criterio no estaba declarado, el experimento se reinicia desde el paso 1:
  un criterio escrito después del resultado no es un criterio. Es la prueba T107.
```
