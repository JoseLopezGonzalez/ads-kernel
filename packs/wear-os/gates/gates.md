# Gates adicionales del pack wear-os

```yaml ads:gate
id: gate:wear-vistazo
aplica_a: "toda superficie de reloj antes de pasar a entrega"
comprobaciones:
  - id: duracion-declarada
    comprueba: "la superficie declara cuántos segundos dura su uso previsto y qué consigue el usuario"
    como: "campo presente en la especificación, y cronometrado en la validación"
    automatizable: si
  - id: dato-dominante
    comprueba: "existe UN dato dominante, legible sin enfocar"
    como: "prueba de entrecerrado sobre la captura al tamaño real del reloj"
    automatizable: parcial
  - id: una-accion
    comprueba: "hay una sola acción principal por superficie"
    como: "lectura de la especificación: dos acciones con el mismo peso es el hallazgo"
    automatizable: parcial
  - id: legible-al-sol
    comprueba: "la superficie es legible a la luz del sol en el reloj más pequeño de la matriz"
    como: "fotografía de la pantalla en exterior con luz directa"
    automatizable: no
  - id: dedo-no-tapa
    comprueba: "lo que confirma la acción no queda debajo del dedo al pulsarla"
    como: "grabación de la pulsación en reloj real"
    automatizable: parcial
  - id: sin-entrada-de-texto
    comprueba: "la superficie no exige escribir texto, o el proyecto declaró la excepción"
    como: "lectura de la especificación"
    automatizable: si
evidencia:
  - "captura al tamaño real y fotografía al sol"
  - "grabación de la pulsación en reloj real"
  - "cronometraje del uso en la validación"
fallo: >
  Vuelve a wear:DIS/lectura-de-un-vistazo. Si el problema es que el alcance exige dos
  acciones principales, vuelve a PRD: partir la superficie o mover la función al móvil es
  una decisión de producto.
```

```yaml ads:gate
id: gate:wear-ambiental
aplica_a: "toda superficie de reloj que permanece visible"
comprobaciones:
  - id: ambiental-declarado
    comprueba: "cada superficie declara qué se ve en estado ambiental"
    como: "campo presente por superficie"
    automatizable: si
  - id: ambiental-util
    comprueba: "lo que se ve en ambiental es la información principal, no un elemento decorativo"
    como: "captura del ambiental y comparación con el dato dominante declarado"
    automatizable: parcial
  - id: volver-no-reinicia
    comprueba: "volver del ambiental no reinicia lo que el usuario estaba haciendo"
    como: "prueba en reloj real: iniciar una tarea, bajar la muñeca, esperar, volver"
    automatizable: si
  - id: ambiental-en-presupuesto
    comprueba: "el consumo del estado ambiental está dentro del presupuesto declarado"
    como: "medición en reloj real desconectado del cargador"
    automatizable: si
evidencia:
  - "captura del ambiental de cada superficie"
  - "grabación de la vuelta del ambiental"
  - "medición de consumo del ambiental"
fallo: >
  Vuelve a wear:CON/energia-y-estados. Si lo que falta es qué mostrar, vuelve a
  wear:DIS/lectura-de-un-vistazo.
```

```yaml ads:gate
id: gate:wear-consumo
aplica_a: "toda aplicación de reloj con actualizaciones, sensores o sincronización"
comprobaciones:
  - id: medido-sin-cargador
    comprueba: "el consumo se ha medido en reloj real desconectado del cargador"
    como: "la medición declara el reloj y que estaba desconectado"
    automatizable: si
  - id: frecuencia-declarada
    comprueba: "cada superficie declara su frecuencia de actualización y su motivo"
    como: "lista de superficies con su frecuencia"
    automatizable: si
  - id: ciclo-de-sensores
    comprueba: "cada sensor declara cuándo se enciende y cuándo se apaga, y se comprueba"
    como: "traza del ciclo de cada sensor durante un recorrido completo"
    automatizable: si
  - id: sin-telefono
    comprueba: "el comportamiento sin teléfono corresponde a la decisión de independencia declarada"
    como: "recorrido completo con el teléfono fuera de alcance"
    automatizable: si
  - id: reconexion-idempotente
    comprueba: "lo encolado no se sincroniza dos veces al reconectar"
    como: "prueba: encolar, desconectar, reconectar dos veces, comprobar efectos"
    automatizable: si
evidencia:
  - "mediciones de consumo con el reloj desconectado"
  - "traza del ciclo de sensores"
  - "recorrido sin teléfono y prueba de reconexión"
fallo: >
  Vuelve a wear:CON/energia-y-estados. Si el consumo es inherente al alcance, vuelve a PRD:
  reducir la función o su frecuencia es decisión de producto y del Owner.
```
