# T530–T539 — el diario canónico segmentado, sin que cambie ni una línea

**Qué cierran.** Un límite medido en la instancia de La Pesquerapp (2026-10-17): el diario
canónico ocupaba 59 MiB en un solo fichero, crecía de 2 a 5 MiB al día con la oficina activa, y
GitHub rechaza el push de un fichero de más de 100 MiB. El sellado de `g.7` no lo resuelve:
retira cuerpos —el Owner no autoriza retirarlos— y `transicion.preparada`, un tercio del fichero,
no se sella nunca. El Owner autorizó la segmentación como mantenimiento preventivo, con la
condición de conservar íntegramente todos los eventos, su contenido, su secuencia y su cadena.

El mecanismo es `Diario.rotar` en [`../runtime/estado/diario.py`](../runtime/estado/diario.py)
(sección «LA SEGMENTACIÓN»), publicado por `Almacen.segmentar` y `ads_estado.py segmentar`, y
compuesto también por `ramas.diario_en` para leer otras referencias. Su contrato es el §6 ter de
[`../runtime/CONTRATO-ESTADO-DURABLE.md`](../runtime/CONTRATO-ESTADO-DURABLE.md). Se mide
ejecutando: almacenes reales, cortes reales con `ADS_ESTADO_FALLO` en las dos fronteras de la
rotación, y repositorios Git reales para la lectura desde otra rama.

**Lo que NO afirman.**
- Que la oficina rote sola: la rotación es una orden explícita y firmada. Cuándo se invoca lo
  decide la instancia.
- Que un segmento cerrado esté a salvo de quien reescriba A LA VEZ el segmento, su `sha256` y la
  cadena entera hasta el final del vivo: ese residuo es el mismo del sellado y lo reserva `g.15`
  a la raíz externa.

```text
T530  la rotación conserva cada byte y la cadena; la revisión publicada no se mueve
T531  tras rotar, la historia sigue creciendo encadenada; un lector que coincide con una rotación lee la historia real
T532  un diario sin segmentar se lee, escribe y recupera como siempre; un umbral no alcanzado no deja rastro
T533  un corte REAL tras publicar el segmento no pierde ni duplica; la siguiente escritura —o un sellado— limpia el huérfano
T534  un corte REAL tras publicar el índice no duplica, `recuperar` completa, y la cadena continúa
T535  ni una transacción sin cerrar ni una rotación sin autor y motivo se segmentan
T536  un segmento alterado en un byte es DIARIO_CORRUPTO al abrir y al verificar
T537  lo que falta o sobra entre segmentos —segmento, rango, índice, fichero ajeno, anexado sobre una rotación a medias— es DIARIO_CORRUPTO
T538  con segmentos el sellado se niega, y una cola rota sólo trunca el vivo
T539  un diario segmentado se compone igual desde Git; un segmento alterado o un commit sin sus segmentos es BLOQUEO
```

---

```yaml ads:escenario
id: T530
nombre: La rotación cierra el vivo como segmento sin cambiar un byte ni la cadena
cubre: ["CONTRATO-ESTADO-DURABLE §6 ter", "g.7", "g.13"]
dado:
  - "un almacén con transacciones confirmadas"
cuando:
  - "se invoca `Almacen.segmentar` con autor y motivo"
entonces:
  - "el segmento tiene byte a byte las bytes que tenía el vivo, y el vivo queda vacío"
  - "el índice registra desde, hasta, bytes, sha256 y la huella del último evento"
  - "la lista de eventos que lee el motor es idéntica a la de antes de rotar"
  - "la revisión publicada no se mueve, y la integridad y la auditoría verifican"
falla_si:
  - "una línea cambia, se reordena, se pierde o se duplica"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: validador-implementado
```

```yaml ads:escenario
id: T531
nombre: Tras rotar, el vivo nuevo encadena con el último segmento
cubre: ["CONTRATO-ESTADO-DURABLE §6 ter", "§2.4"]
dado:
  - "un almacén rotado una vez"
cuando:
  - "se aplican transacciones, se rota otra vez y se aplica una más"
entonces:
  - "el primer evento del vivo lleva como `previo` la huella del último del segmento, y la secuencia siguiente"
  - "las secuencias son contiguas desde 1 a través de los dos segmentos y el vivo"
  - "`verificar` y `auditar` de la CLI, en otro proceso, salen con 0"
  - "un lector sin bloqueo al que, entre leer el vivo y el índice, un escritor anexa y rota —o anexa y deja una rotación cortada tras el paso 1— devuelve la historia real"
falla_si:
  - "la cadena o la secuencia se rompen en un corte entre ficheros"
  - "un lector compone el vivo viejo detrás del segmento nuevo, o da DIARIO_CORRUPTO sobre un almacén sano (revisión independiente, H3)"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: validador-implementado
```

```yaml ads:escenario
id: T532
nombre: Un diario que nunca se segmentó se lee como siempre
cubre: ["CONTRATO-ESTADO-DURABLE §6 ter", "compatibilidad"]
dado:
  - "un almacén sin `segmentos/`"
cuando:
  - "se lee, se escribe, se verifica y se pide una rotación con un umbral por encima del vivo"
entonces:
  - "todo verifica y no aparece `segmentos/`"
  - "la rotación no rota, dice por qué y no deja rastro"
falla_si:
  - "el código nuevo exige segmentos o crea ficheros al leer"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: validador-implementado
```

```yaml ads:escenario
id: T533
nombre: Un corte tras publicar el segmento no pierde ni duplica eventos
cubre: ["CONTRATO-ESTADO-DURABLE §6 ter", "§10", "g.4", "g.8"]
dado:
  - "un almacén con transacciones confirmadas"
cuando:
  - "la CLI muere con ADS_ESTADO_FALLO=segmentacion-tras-el-segmento"
entonces:
  - "queda un segmento huérfano que ningún índice nombra, y el diario sigue siendo el vivo"
  - "la historia y la revisión son las de antes del corte"
  - "la siguiente escritura retira el huérfano y la rotación repetida termina sin duplicados"
  - "sellar sobre el huérfano completa antes la rotación y el almacén sigue utilizable (revisión independiente, H1)"
falla_si:
  - "el huérfano se cuenta como historia, o bloquea el almacén"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: validador-implementado
```

```yaml ads:escenario
id: T534
nombre: Un corte tras publicar el índice no duplica y se completa al recuperar
cubre: ["CONTRATO-ESTADO-DURABLE §6 ter", "§10", "g.4", "g.8"]
dado:
  - "un almacén con transacciones confirmadas"
cuando:
  - "la CLI muere con ADS_ESTADO_FALLO=segmentacion-tras-el-indice y después se invoca `recuperar`"
entonces:
  - "el vivo tiene las mismas bytes que el último segmento y se lee como vacío"
  - "la historia y la revisión son las de antes del corte"
  - "`recuperar` vacía el vivo y la transacción siguiente encadena con `huella_ultima`"
falla_si:
  - "los eventos del último segmento se leen dos veces"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: validador-implementado
```

```yaml ads:escenario
id: T535
nombre: No se segmenta una ventana abierta ni una rotación sin firma
cubre: ["CONTRATO-ESTADO-DURABLE §6 ter", "g.8"]
dado:
  - "una transacción muerta con ADS_ESTADO_FALLO=entre-el-paso-8-y-el-9"
cuando:
  - "se pide `segmentar`, y después se pide sin autor o sin motivo"
entonces:
  - "las tres veces SEGMENTACION_IMPOSIBLE, sin crear `segmentos/`"
  - "tras recuperar, la misma orden segmenta"
falla_si:
  - "una transacción sin evento terminal queda partida entre dos ficheros"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: validador-implementado
```

```yaml ads:escenario
id: T536
nombre: Un segmento alterado es diario corrupto
cubre: ["CONTRATO-ESTADO-DURABLE §6 ter", "g.5"]
dado:
  - "un almacén rotado"
cuando:
  - "se cambia un byte de un segmento cerrado"
entonces:
  - "abrir para leer, abrir para escribir y `verificar` fallan cerrado con DIARIO_CORRUPTO"
falla_si:
  - "el almacén se abre con un segmento que no es el que el índice registró"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: validador-implementado
```

```yaml ads:escenario
id: T537
nombre: Lo que falta o sobra entre segmentos es diario corrupto
cubre: ["CONTRATO-ESTADO-DURABLE §6 ter", "g.5", "g.13"]
dado:
  - "un almacén con dos segmentos y un vivo"
cuando:
  - "en cinco copias: se borra un segmento, el índice salta un rango, el índice no es JSON, aparece un fichero ajeno en `segmentos/`, y el vivo empieza con el último segmento y sigue"
entonces:
  - "las cinco son DIARIO_CORRUPTO"
falla_si:
  - "se compone una historia con un hueco o con un añadido"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: validador-implementado
```

```yaml ads:escenario
id: T538
nombre: Con segmentos el sellado se niega y una cola rota sólo trunca el vivo
cubre: ["CONTRATO-ESTADO-DURABLE §6 ter", "g.7", "g.8"]
dado:
  - "un almacén rotado con una transacción posterior"
cuando:
  - "se pide sellar, y después se deja una cola desgarrada en el vivo y se recupera"
entonces:
  - "el sellado sale con SELLADO_IMPOSIBLE"
  - "la reparación trunca sólo el vivo, el segmento conserva sus bytes y la historia verifica"
falla_si:
  - "el sellado o la reparación reescriben un segmento"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: validador-implementado
```

```yaml ads:escenario
id: T539
nombre: Un diario segmentado se lee igual desde Git
cubre: ["CONTRATO-ESTADO-DURABLE §6 bis", "§6 ter"]
dado:
  - "un control repo Git con un almacén segmentado y confirmado en una rama"
cuando:
  - "`ramas.diario_en` lo lee como blobs y `ramas.comparar` lo compara con la rama sin segmentar"
entonces:
  - "los eventos compuestos desde Git son los que el motor lee del disco"
  - "la comparación es COMPATIBLE, y con un segmento alterado en otra rama es BLOQUEO"
  - "un commit que lleva el vivo y no sus segmentos es BLOQUEO: `diario_en` exige empezar en la secuencia 1 sin `previo` y sin saltos (revisión independiente, H2)"
falla_si:
  - "una rama segmentada parece truncada o manipulada, o una alterada parece sana"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_estado_entre_ramas.py
estado: validador-implementado
```
