# Gates adicionales del pack web-app

Se **suman** a los del kernel. No los sustituyen ni los rebajan: un paquete de una web app
pasa `gate:usabilidad`, `gate:excelencia-visual` y además estos tres.

```yaml ads:gate
id: gate:web-accesibilidad
aplica_a: "toda superficie web antes de pasar a entrega"
comprobaciones:
  - id: teclado-solo
    comprueba: "todo recorrido principal se completa con teclado solo, sin puntero"
    como: "grabación del recorrido completo usando únicamente el teclado"
    automatizable: parcial
  - id: foco-visible
    comprueba: "el foco es visible en todo elemento alcanzable y su orden sigue el de lectura"
    como: "recorrido con captura en cada parada del foco"
    automatizable: parcial
  - id: sin-solo-hover
    comprueba: "ninguna acción ni información existe sólo al pasar el puntero por encima"
    como: "recorrido sin puntero: lo que desaparece es el hallazgo"
    automatizable: parcial
  - id: texto-ampliado
    comprueba: "la superficie funciona con el texto ampliado al doble sin perder función"
    como: "captura con el texto ampliado en cada tamaño extremo de la matriz"
    automatizable: si
  - id: movimiento-reducido
    comprueba: "con movimiento reducido, la superficie sigue comunicando los cambios de estado"
    como: "grabación con la preferencia de movimiento reducido activada"
    automatizable: si
  - id: comprobacion-automatica
    comprueba: "la comprobación automática de accesibilidad no reporta incumplimientos del nivel declarado"
    como: "salida de la herramienta sobre cada superficie de la matriz"
    automatizable: si
evidencia:
  - "grabación del recorrido con teclado solo"
  - "capturas con texto ampliado y con movimiento reducido"
  - "salida de la comprobación automática"
fallo: >
  El paquete no pasa. Un fallo de teclado o de foco vuelve a DIS/diseno-interaccion; uno de
  contraste o de texto ampliado, a DIS/diseno-visual; uno de implementación, a CON.
```

```yaml ads:gate
id: gate:web-rendimiento-percibido
aplica_a: "toda superficie web que carga datos o ejecuta operaciones"
comprobaciones:
  - id: primera-respuesta
    comprueba: "existe respuesta visible dentro del presupuesto declarado tras cada acción"
    como: "medición sobre grabación, en el entorno y la red declarados por el proyecto"
    automatizable: si
  - id: utilizable
    comprueba: "la superficie principal es utilizable dentro del presupuesto declarado"
    como: "medición en el entorno declarado, con red degradada además de con red buena"
    automatizable: si
  - id: sin-desplazamiento
    comprueba: "el contenido ya leído NO se desplaza durante la carga"
    como: "grabación de la carga completa: cualquier salto es el hallazgo"
    automatizable: si
  - id: respuesta-durante-operacion
    comprueba: "la interfaz responde mientras una operación larga está en curso"
    como: "recorrido durante la operación, registrando si algo queda bloqueado"
    automatizable: parcial
  - id: medido-fuera-de-desarrollo
    comprueba: "las mediciones NO se hicieron en la máquina de desarrollo con red local"
    como: "el entorno de medición está declarado y no es el de desarrollo"
    automatizable: si
evidencia:
  - "las mediciones con su entorno y su red declarados"
  - "la grabación de la carga completa"
fallo: >
  Vuelve a CON con la medición. Si el presupuesto es inalcanzable por diseño, vuelve a DIS o
  a ARQ con la evidencia, y no se rebaja el presupuesto sin decisión escrita.
```

```yaml ads:gate
id: gate:web-estados-de-red
aplica_a: "toda superficie que ejecuta operaciones contra la red"
comprobaciones:
  - id: cinco-estados-de-red
    comprueba: "los cinco estados de red están implementados y probados con red simulada"
    como: "una grabación por estado, con la red degradada de la forma correspondiente"
    automatizable: si
  - id: no-se-pierde-lo-escrito
    comprueba: "lo escrito por el usuario sobrevive a un fallo de envío"
    como: "prueba: escribir, cortar la red, enviar, restaurar, comprobar que sigue ahí"
    automatizable: si
  - id: reintento-seguro
    comprueba: "ninguna operación no idempotente se reintenta sin haber consultado a DOM"
    como: "el paquete enlaza la consulta a DOM por cada operación reintentada"
    automatizable: si
  - id: salida-de-la-caida
    comprueba: "con la red caída, la aplicación no queda en un estado del que no se sale"
    como: "recorrido con red caída desde cada superficie principal"
    automatizable: parcial
evidencia:
  - "una grabación por estado de red"
  - "la prueba de que lo escrito sobrevive"
  - "las consultas a DOM por operación reintentada"
fallo: >
  Vuelve a web:CON/estados-de-red. Si lo que falta es qué comunicar en un estado, vuelve a
  DIS/diseno-interaccion.
```
