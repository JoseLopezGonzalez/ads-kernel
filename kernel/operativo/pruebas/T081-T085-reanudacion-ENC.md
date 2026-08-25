# T81–T85 — reanudación de los métodos de ENC

Cada método de `ENC` declara en su contrato una `prueba_de_reanudacion`. Aquí están esas
pruebas como escenarios ejecutables. Todas comparten la misma forma: **se interrumpe el
método en un punto concreto, se releva al agente por otro que no vio nada, y se comprueba
que continúa sin repetir trabajo ni molestar al Owner.**

Su estado real está en [`REGISTRO-generado.md`](REGISTRO-generado.md).

```yaml ads:escenario
id: T81
nombre: Reanudación de ENC/Anclaje sin repetir búsquedas
cubre: ["ENC/Anclaje", "a.10 checkpoint", "gate:anclaje-completo"]
dado:
  - "un dosier de anclaje a medias, con la traza del paso 2 escrita"
  - "un agente nuevo sin acceso a la sesión anterior"
cuando:
  - "el agente nuevo abre el paquete y lee el checkpoint"
entonces:
  - "no vuelve a ejecutar ninguna búsqueda ya registrada en la traza"
  - "continúa por los términos que faltaban"
  - "el dosier final contiene la traza completa de ambos tramos"
falla_si:
  - "se repite una búsqueda ya registrada"
  - "se declara que algo no existe apoyándose sólo en las búsquedas del segundo tramo"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T82
nombre: Reanudación de ENC/Maduracion sin repetir alternativas rechazadas
cubre: ["ENC/Maduracion", "forma:idea-inmadura", "a.10 checkpoint"]
dado:
  - "una ficha de vivero con dos alternativas presentadas y la reacción del Owner a cada una"
  - "un agente nuevo"
cuando:
  - "el Owner vuelve sobre la idea"
entonces:
  - "el agente nuevo lee las alternativas y sus reacciones antes de proponer nada"
  - "las alternativas nuevas son distintas de las ya rechazadas"
falla_si:
  - "se propone de nuevo una alternativa que el Owner ya rechazó"
  - "se pide al Owner que repita qué le pareció cada una"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T83
nombre: Reanudación de ENC/Orden sin aplicar dos veces el mismo evento
cubre: ["ENC/Orden", "gate:orden-emitida", "a.9 idempotencia por id"]
dado:
  - "una orden cuyo evento se escribió pero cuya aplicación se interrumpió"
cuando:
  - "un agente nuevo reanuda"
entonces:
  - "detecta el evento ya emitido por su identificador"
  - "aplicar el evento por segunda vez es una no-operación"
  - "el estado converge al mismo resultado que una ejecución sin interrupción"
falla_si:
  - "la orden se aplica dos veces"
  - "la orden se pierde por considerarse ya aplicada sin comprobar el estado"
ejecucion: requiere-runtime
estado: contrato-definido
```

```yaml ads:escenario
id: T84
nombre: Reanudación de ENC/Formulacion desde campos parcialmente escritos
cubre: ["ENC/Formulacion", "gate:encuadre-listo"]
dado:
  - "un encuadre con los campos hasta suposiciones escritos y el checkpoint en el paso 4"
  - "un agente nuevo"
cuando:
  - "el agente nuevo reanuda la formulación"
entonces:
  - "continúa en el paso 5 sin rehacer la separación de montones"
  - "el nivel de Owner resultante cita la fila de a.8 que aplica"
falla_si:
  - "se reescriben campos ya cerrados sin motivo registrado"
  - "el nivel de Owner se marca obligatorio sin citar la fila que lo justifica"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T85
nombre: La crítica no se reanuda si su lectura independiente no se escribió
cubre: ["ENC/Critica", "gate:critica-de-encuadre", "G13"]
dado:
  - "una crítica interrumpida antes de escribir su lectura independiente de la literal"
cuando:
  - "se intenta reanudar con otro agente"
entonces:
  - "el método se reinicia desde el paso 1 con un agente que no ha leído la interpretación ajena"
  - "queda registrado que hubo reinicio y por qué"
falla_si:
  - "el agente entrante continúa habiendo leído primero la interpretación del interlocutor"
  - "el dictamen se emite sin lectura independiente registrada"
ejecucion: guion-manual
estado: contrato-definido
```
