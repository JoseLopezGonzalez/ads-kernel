# ENC/Critica — segunda lectura del encuadre

```yaml ads:metodo
id: ENC/Critica
nombre: Critica
capacidad: ENC
disparador:
  - "la incertidumbre declarada del encuadre es alta"
  - "el nivel de intervención del Owner calculado es obligatorio"
  - "el tipo de proceso propuesto es DIR, AUD o INC"
carga:
  - "el encuadre completo, empezando por la expresión literal"
  - "el dosier de anclaje y su traza"
  - "las decisiones vigentes en la materia"
preguntas_iniciales:
  - "leyendo SÓLO lo que el Owner dijo, ¿llegaría yo a esta interpretación?"
  - "¿qué necesita ser verdad para que este encuadre se sostenga, y está escrito?"
pasos:
  - n: 1
    nombre: LEER LA LITERAL PRIMERO
    modo: lineal
    hace: >
      Leer la expresión literal antes que la interpretación, y escribir la propia lectura
      antes de contaminarse con la del interlocutor.
    produce: "lectura independiente de la literal"
    termina_cuando: "la lectura propia está escrita"
    checkpoint: false
  - n: 2
    nombre: CONTRASTAR
    modo: convergente
    hace: >
      Comparar la lectura propia con la interpretación del encuadre y localizar cada
      diferencia. Toda diferencia es un hallazgo, aunque la interpretación ajena sea mejor.
    produce: "lista de diferencias"
    termina_cuando: "cada diferencia está escrita con la cita literal que la origina"
    checkpoint: true
  - n: 3
    nombre: BUSCAR SUPUESTOS
    modo: convergente
    hace: >
      Enumerar lo que el encuadre necesita que sea verdad y no declara. Cada supuesto no
      declarado es un hueco.
    produce: "lista de supuestos no declarados"
    termina_cuando: "no quedan afirmaciones del encuadre sin su fundamento localizado"
    checkpoint: true
  - n: 4
    nombre: PROBAR LA EVIDENCIA DE CIERRE
    modo: convergente
    hace: >
      Por cada evidencia declarada, responder: ¿podría yo comprobarla sin hablar con nadie?
      Si la respuesta es no, es un hueco.
    produce: "veredicto por evidencia"
    termina_cuando: "todas las evidencias tienen veredicto"
    checkpoint: true
  - n: 5
    nombre: DICTAMINAR
    modo: convergente
    hace: >
      Escribir el dictamen: veredicto conforme o devuelto, y por cada hueco qué lo cerraría.
      Sin versión alternativa del encuadre.
    produce: "dictamen"
    termina_cuando: "gate:critica-de-encuadre cumplido"
    checkpoint: true
artefactos:
  - "lectura independiente de la literal"
  - "dictamen con veredicto y huecos"
puntos_owner:
  - "ninguno: este método nunca habla con el Owner"
consultas:
  - "ninguna: la crítica se hace con el material entregado. Si falta material, ése es el hallazgo"
checkpoints:
  - "tras los pasos 2, 3, 4 y 5"
critica:
  - "¿alguna observación es de estilo de redacción en lugar de de fondo?"
  - "¿el dictamen contiene una versión alternativa del encuadre?"
  - "¿se rechazó por preferencia en vez de por hueco?"
gate: gate:critica-de-encuadre
salida:
  - "dictamen conforme, o"
  - "dictamen devuelto con huecos y qué cerraría cada uno"
devolucion:
  - "al interlocutor, con la lista de huecos"
bloqueo:
  - "el dosier de anclaje no está: sin él no puede juzgarse qué se da por supuesto"
cancelacion:
  - "el interlocutor descarta el encuadre antes de que el dictamen se emita"
aprendizaje:
  - "un mismo tipo de hueco en tres encuadres genera entrada en defectos-de-encuadre.md y candidato a mejorar el método"
prueba_de_reanudacion: >
  Un agente nuevo lee la lectura independiente ya escrita y las diferencias localizadas, y
  continúa. Si la lectura independiente no estaba escrita, DEBE reiniciar el método desde
  el paso 1 con otro agente: leer primero la interpretación ajena invalida la crítica. La
  prueba es T85.
```
