# Gates adicionales del pack mobile-app

Se **suman** a los del kernel.

```yaml ads:gate
id: gate:mob-dispositivo-real
aplica_a: "toda superficie móvil antes de pasar a entrega"
comprobaciones:
  - id: recorrido-en-hardware
    comprueba: "cada recorrido principal se ha ejecutado en un dispositivo REAL de la matriz"
    como: "grabación en el dispositivo, con su modelo y versión de sistema declarados"
    automatizable: si
  - id: gama-baja
    comprueba: "la evidencia incluye el dispositivo más lento de la matriz"
    como: "la matriz declara cuál es, y existe grabación en él"
    automatizable: si
  - id: fluidez
    comprueba: "las transiciones se comportan en el dispositivo lento como se especificaron"
    como: "medición sobre la grabación en ese dispositivo"
    automatizable: si
  - id: teclado-abierto
    comprueba: "existe captura con el teclado abierto de cada superficie que lo recibe"
    como: "recuento de capturas por superficie con campo de entrada"
    automatizable: si
  - id: emulador-no-sustituye
    comprueba: "ninguna evidencia de este gate procede de un emulador"
    como: "cada pieza de evidencia declara el dispositivo donde se obtuvo"
    automatizable: si
evidencia:
  - "grabaciones en dispositivo real con modelo y versión"
  - "mediciones de fluidez en el dispositivo más lento"
  - "capturas con teclado abierto"
fallo: >
  El paquete no pasa. Si el fallo es de fluidez, vuelve a DIS/movimiento con la grabación;
  si es de composición con teclado, a mob:DIS/interaccion-tactil.
```

```yaml ads:gate
id: gate:mob-ciclo-y-permisos
aplica_a: "toda aplicación con estado de trabajo del usuario o con permisos"
comprobaciones:
  - id: suspension
    comprueba: "suspendida y reanudada, la aplicación vuelve al mismo estado"
    como: "prueba en dispositivo real: suspender, esperar, reanudar"
    automatizable: si
  - id: terminacion-forzada
    comprueba: "terminada por el sistema y reabierta, no se ha perdido lo escrito"
    como: "prueba en dispositivo real forzando la terminación, no cerrando la aplicación"
    automatizable: si
  - id: operacion-interrumpida
    comprueba: "una operación en curso al suspender termina, se reanuda o se declara perdida"
    como: "prueba por cada tipo de operación larga del producto"
    automatizable: si
  - id: tres-estados-de-permiso
    comprueba: "cada permiso tiene resueltos concedido, denegado y revocado después"
    como: "recorrido con cada estado provocado en dispositivo real"
    automatizable: si
  - id: utilidad-sin-permiso
    comprueba: "con el permiso denegado la aplicación sigue siendo útil y lo dice"
    como: "recorrido con el permiso denegado desde el inicio"
    automatizable: parcial
evidencia:
  - "grabaciones de suspensión y de terminación forzada"
  - "recorrido con cada estado de permiso"
fallo: >
  Vuelve a mob:CON/ciclo-de-vida. Si lo que falta es qué comunicar, vuelve a
  DIS/diseno-interaccion.
```

```yaml ads:gate
id: gate:mob-consumo
aplica_a: "toda aplicación con trabajo en segundo plano, sensores o sincronización"
comprobaciones:
  - id: trabajo-en-segundo-plano-declarado
    comprueba: "está escrito qué hace la aplicación en segundo plano, cuándo y por qué"
    como: "lista de trabajos con su disparador y su frecuencia"
    automatizable: si
  - id: consumo-medido
    comprueba: "las operaciones declaradas costosas tienen su consumo medido en dispositivo real"
    como: "medición con el dispositivo desconectado de la corriente"
    automatizable: si
  - id: sensores-con-limite
    comprueba: "todo sensor declara cuándo se activa y cuándo se apaga"
    como: "lista de sensores con su ciclo de activación"
    automatizable: si
  - id: sin-sorpresas
    comprueba: "ninguna operación consume batería sin que el usuario pueda saber que ocurre"
    como: "recorrido: lo que consume en segundo plano es visible o es detenible"
    automatizable: parcial
evidencia:
  - "lista de trabajos en segundo plano con su frecuencia"
  - "mediciones de consumo en dispositivo real"
fallo: >
  Vuelve a CON con la medición. Si el consumo es inherente al alcance, vuelve a PRD: reducir
  la frecuencia o el alcance de la sincronización es una decisión de producto.
```
