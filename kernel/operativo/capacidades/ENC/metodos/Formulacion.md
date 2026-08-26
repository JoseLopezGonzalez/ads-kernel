# ENC/Formulacion — de lo comprendido al encuadre

Escribir el encuadre completo. La plantilla rellenable está en
[`plantillas/ENCUADRE.md`](../../../plantillas/ENCUADRE.md); este método dice **cómo se
llena cada campo sin inventarlo**.

```yaml ads:metodo
id: ENC/Formulacion
nombre: Formulacion
capacidad: ENC
disparador:
  - "ENC/Escucha llega a su paso 7"
  - "un encuadre devuelto vuelve con huecos concretos que cerrar"
carga:
  - "la expresión literal completa y todas las respuestas del Owner captadas"
  - "el dosier de anclaje"
  - "la medición de incertidumbre"
  - "la plantilla de encuadre"
preguntas_iniciales:
  - "¿qué campo del esquema no puedo escribir sin inventarlo? — ése va a dudas_abiertas, no a suposiciones"
  - "¿qué estoy afirmando que el Owner no ha dicho? — eso va a interpretación, nunca a literal"
pasos:
  - n: 1
    nombre: SEPARAR
    modo: lineal
    hace: >
      Repartir lo que se sabe en tres montones: lo que el Owner dijo, lo que el anclaje
      demostró, y lo que ENC interpreta. Cada montón va a un campo distinto y nunca se
      mezclan.
    produce: "los tres montones etiquetados"
    termina_cuando: "ninguna frase está en dos montones"
    checkpoint: false
  - n: 2
    nombre: ESCRIBIR EL RESULTADO PERSEGUIDO
    modo: convergente
    hace: >
      Una frase que diga qué existirá cuando esto termine. Prohibido usar mejorar,
      optimizar o revisar como único verbo: no describen un resultado, describen una
      actividad.
    produce: "resultado_perseguido"
    termina_cuando: "la frase pasa la prueba del verbo y nombra algo comprobable"
    checkpoint: true
  - n: 3
    nombre: ESCRIBIR LA EVIDENCIA DE CIERRE
    modo: convergente
    hace: >
      Por cada expectativa, una evidencia que otro pueda comprobar: qué se mira, dónde, y
      qué resultado cuenta como cierre. Si no se puede escribir, la idea no estaba madura y
      se vuelve a ENC/Maduracion.
    produce: "evidencia_de_cierre[]"
    termina_cuando: "hay al menos una evidencia comprobable por alguien distinto de quien la escribió"
    checkpoint: true
  - n: 4
    nombre: DECLARAR SUPOSICIONES Y DUDAS
    modo: lineal
    hace: >
      Todo lo que la interpretación necesita para sostenerse y el Owner no confirmó va a
      suposiciones. Todo lo que sigue sin respuesta va a dudas_abiertas. Ninguna de las dos
      puede quedarse escondida dentro de la interpretación.
    produce: "suposiciones[] y dudas_abiertas[]"
    termina_cuando: "el crítico no puede señalar ningún supuesto no declarado"
    checkpoint: true
  - n: 5
    nombre: CALCULAR EL NIVEL DEL OWNER
    modo: lineal
    hace: >
      Aplicar la tabla de a.8 y el test de «extiende un patrón aprobado». El encuadre cita
      la fila concreta que aplica. No se marca obligatorio por prudencia.
    produce: "nivel_owner con su motivo citando a.8"
    termina_cuando: "el nivel deriva de una fila citada, no de una impresión"
    checkpoint: true
  - n: 6
    nombre: PROPONER TIPO DE PROCESO
    modo: convergente
    hace: >
      Proponer el tipo de b.16 según el RESULTADO PERSEGUIDO, no según las capacidades que
      se imaginan necesarias. Es propuesta: DSP decide.
    produce: "clasificacion.tipo_propuesto con motivo"
    termina_cuando: "el motivo cita el resultado perseguido, no una lista de capacidades"
    checkpoint: true
  - n: 7
    nombre: CERRAR CONTRA EL GATE
    modo: convergente
    hace: >
      Recorrer las diez comprobaciones de gate:encuadre-listo una por una y anotar el
      resultado de cada una.
    produce: "encuadre en estado listo-para-dsp, o lista de lo que falta"
    termina_cuando: "las diez comprobaciones están anotadas"
    checkpoint: true
artefactos:
  - "bloque ads:encuadre completo"
  - "anotación del recorrido del gate"
puntos_owner:
  - "ninguno: este método no conversa. Si necesita preguntar, devuelve a ENC/Escucha paso 6"
consultas:
  - "la capacidad competente en modo consulta, cuando una restricción declarada por el Owner necesita verificarse"
checkpoints:
  - "tras los pasos 2 a 7"
critica:
  - "¿hay alguna afirmación en interpretación que el Owner no dijo y el anclaje no demostró?"
  - "¿alguna duda quedó escondida como si fuera un hecho?"
  - "¿el nivel del Owner se marcó obligatorio por prudencia en vez de por la tabla?"
  - "¿la evidencia de cierre la puede comprobar alguien que no participó en la conversación?"
gate: gate:encuadre-listo
salida:
  - "encuadre en estado listo-para-dsp"
devolucion:
  - "a ENC/Escucha paso 6, cuando un campo no puede escribirse sin preguntar al Owner"
  - "a ENC/Maduracion, cuando la evidencia de cierre no puede escribirse"
bloqueo:
  - "una restricción declarada por el Owner no puede verificarse y condiciona el resultado perseguido"
cancelacion:
  - "el anclaje, releído al formular, demuestra que lo pedido ya existe: se descarta con enlace"
aprendizaje:
  - "un campo que se deja vacío repetidamente señala un hueco del método, y se registra"
prueba_de_reanudacion: >
  Un agente nuevo abre el encuadre a medio escribir, ve qué campos están cerrados y cuál
  fue el último paso anotado, y continúa. La prueba es T84: se corta entre el paso 4 y el
  5 y el agente entrante completa sin volver a separar los montones.
```
