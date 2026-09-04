# T172–T181 · T312–T319 · T320–T327 — el estado durable, ejecutado

Conformidad de la sección
[`(g)`](../../../docs/rediseno/g-ESTADO-DURABLE-APROBADA.md) y de su contrato derivado
[`CONTRATO-ESTADO-DURABLE.md`](../runtime/CONTRATO-ESTADO-DURABLE.md).

**Estas pruebas EJECUTAN CÓDIGO.** No inspeccionan texto, no comprueban que un fichero
exista y no simulan nada: crean almacenes reales en directorios temporales, escriben en
disco, **matan procesos de verdad** en fronteras controladas y lanzan **procesos
concurrentes de verdad**. Una prueba que sólo se ha visto pasar sobre un mock no verifica un
motor de estado.

**Tres ejecutables, y la distinción importa:**

```text
validadores/entorno.py                         T172 — la guarda de entorno, antes de correr
runtime/pruebas/test_estado_durable.py         T173..T179 — el motor, caso a caso
                                               T312..T319 — el SELLADO del diario (`g.7`)
                                               T320..T327 — la MIGRACIÓN 0->1 sobre un
                                                            almacén heredado REAL (`ADJ-B1`)
runtime/pruebas/escenario_extremo_a_extremo.py T180 — los quince pasos, de una sola pieza
validadores/comprobar_arranque.py              T181 — la norma viaja al proyecto instalado
```

**`T312`–`T319` cierran la mitad de `g.7` que no existía.** `g.7` escribe cinco puntos sobre
el diario. Los tres primeros —orden reconstruible, sostener la recuperación de `g.8`, no ser
la sede del estado— estaban construidos y probados. Los dos últimos **no estaban ni en el
código ni en el contrato derivado**, y `g.7` figuraba sin embargo como obligación con
cobertura declarada. Reproducido el 2026-09-04:

```text
$ grep -rniE "sellad|sellar|compacta" kernel/operativo/runtime/ --include=*.py --include=*.md
kernel/operativo/runtime/estado/serializacion.py:13:    COMPACTA  `separators=(",", ":")` …
$ grep -nEi "sellad|compact|umbral" kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md
(sin salida)
```

La única coincidencia era la forma **compacta** de serialización, que es otra cosa: la forma
de transporte del JSONL.

**Cómo se reparte `g.7` entre los escenarios de este fichero**, punto por punto:

```text
orden reconstruible                       T174 · T175 · T177
sostiene la recuperación de `g.8`         T175 · T314
NO es la sede del estado                  T173
el SELLADO compacta, con umbral           T312 · T313 · T315 · T316
CALIBRABLE del contrato derivado
retirar un cuerpo exige transición        T317 · T318 · T319
explícita y auditable
```

**Cobertura de `g.16`.** Las nueve condiciones observables de aceptación tienen aquí su
escenario positivo **y** su escenario negativo, y ambos son obligatorios: `G-A1` en `T173`,
`G-A2` y `G-A3` en `T174` y `T175`, `G-A4` en `T177`, `G-A5` en `T176` y `T178`, `G-A6` en
`T178`, `G-A7` en `T179`, `G-A8` **parcialmente** en `T174` —la rama canónica no contiene
estado parcial porque la zona operacional queda fuera del versionado; la prohibición
ejecutable de forzar referencias es del corte siguiente— y `G-A9` en `T177`, con la
atestación externa y su proveedor efímero **de pruebas**.

```yaml ads:escenario
id: T172
nombre: Un intérprete insuficiente detiene la batería antes de correr, y no como defecto del producto
cubre: [A14, F6-I, corte V1]
dado:
  - "la versión mínima del intérprete declarada UNA sola vez en validadores/entorno.py"
  - "el runner canónico y el materializador de workspace, que dependen de la biblioteca TOML"
cuando:
  - "se invoca la guarda con una exigencia superior a la del intérprete en uso"
  - "se invoca el runner y el materializador bajo esa misma exigencia"
entonces:
  - "los tres terminan con el código 78, que no es el 1 de «una comprobación no pasó» ni el 2 de «uso incorrecto»"
  - "no se ejecuta ningún validador y no se republica ninguna evidencia"
  - "el mensaje dice qué falta, qué hay, qué hace falta y qué se rompería"
falla_si:
  - "la guarda se puede relajar por entorno: bajar la exigencia por variable la convertiría en un interruptor"
  - "el entorno insuficiente sale con el mismo código que un producto defectuoso"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T173
nombre: El estado canónico se inicializa y se lee sin reproyectar el diario
cubre: [g.1, g.2 I-g1, g.7, g.16 G-A1]
dado:
  - "un repositorio de control temporal sin estado"
cuando:
  - "se inicializa el almacén y se leen la revisión inicial y las entidades escritas"
entonces:
  - "el estado canónico son ficheros JSON legibles con `cat`, sin herramienta"
  - "ninguna lectura del estado necesita reproyectar el diario"
  - "estado canónico, diario y registro auxiliar son TRES estructuras con formato y semántica distintos"
falla_si:
  - "leer el estado exige reconstruirlo desde los eventos"
  - "las tres materias comparten estructura: colapsarlas rompe I-g7"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T174
nombre: Una transición multiarchivo se ve entera o no se ve
cubre: [g.3, g.4, g.12, g.16 G-A2, g.16 G-A3]
dado:
  - "un almacén inicializado y una transición que toca varios ficheros a la vez"
cuando:
  - "se aplican varias transiciones consecutivas y se comprueba el disco tras cada una"
  - "se repite una transición ya confirmada con el mismo identificador"
entonces:
  - "la publicación es un solo renombrado atómico sobre el punto de publicación"
  - "lo confirmado como durable sobrevive a releer el almacén en otro proceso"
  - "repetir una transición confirmada no la aplica dos veces: es idempotente"
  - "un mismo identificador con operaciones distintas produce error tipado, no una mezcla"
falla_si:
  - "queda una mezcla parcial visible entre el primer fichero escrito y el último"
  - "la zona de preparación entra en el versionado, y la rama canónica pasa a contener estado parcial"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T175
nombre: Una interrupción en cualquier frontera termina en COMPLETAR o en MARCAR, y en nada más
cubre: [g.8, g.3, g.16 G-A2]
dado:
  - "los nueve puntos de fallo declarados, uno por frontera del protocolo transaccional"
  - "una expectativa EXPLÍCITA de recuperación escrita para cada punto"
cuando:
  - "se mata el proceso de verdad en cada punto y se reabre el almacén en un proceso nuevo"
entonces:
  - "antes del punto de no retorno se REVIERTE, y lo revertido es sólo especulativo local"
  - "después del punto de no retorno se COMPLETA, y ninguna transición confirmada se pierde"
  - "lo que no casa ni con la base ni con el resultado se MARCA, con copia íntegra de lo divergente"
  - "recuperar dos veces no cambia el estado ni añade eventos: es idempotente"
falla_si:
  - "una transición confirmada se pierde"
  - "una transición incompleta queda publicada"
  - "el runtime decide por su cuenta la salida de un conflicto que la autoridad debe resolver"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T176
nombre: Dos escritores concurrentes se serializan y no hay doble éxito para la misma revisión
cubre: [g.6, g.12 I-g4, g.16 G-A5]
dado:
  - "dos procesos reales que parten de la misma revisión base"
  - "un almacén con el bloqueo de escritor tomado y abandonado por un proceso muerto"
cuando:
  - "los dos procesos intentan aplicar una transición sobre la misma base"
  - "se agotan los reintentos en un escenario dirigido"
entonces:
  - "exactamente uno tiene éxito y el otro recibe revisión obsoleta o escritor concurrente"
  - "un bloqueo abandonado por un proceso muerto se reclama sin heurística de caducidad"
  - "agotar los reintentos NO modifica el estado canónico y produce el registro auxiliar"
  - "agotarlos AL RECUPERAR al abrir, con una ventana abierta, produce el registro igual: G-A5 no dice «al aplicar»"
falla_si:
  - "los dos escritores tienen éxito para la misma revisión"
  - "agotar reintentos deja el estado canónico tocado"
  - "agotar reintentos se declara con el código del camino que NO abre el registro auxiliar"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T177
nombre: La corrupción, el truncamiento y la evidencia manipulada fallan CERRADO
cubre: [g.5, g.13, g.15, g.16 G-A4, g.16 G-A9]
dado:
  - "un almacén íntegro, y copias suyas con un fichero canónico alterado a mano"
  - "un diario truncado a media línea y un registro auxiliar con una línea borrada"
  - "una atestación externa firmada por un proveedor efímero DE PRUEBAS"
cuando:
  - "se leen y se auditan"
entonces:
  - "cada alteración produce un error tipado y ninguna produce una lectura silenciosa"
  - "una modificación del estado sin evento en el diario NO es explicable, y la auditoría lo dice"
  - "una evidencia manipulada o firmada por otra identidad se rechaza"
  - "sin proveedor de firma válido no se atesta: falla cerrado, no firma con nada"
falla_si:
  - "una corrupción se lee como estado válido"
  - "la evidencia de verificación se escribe DENTRO del árbol verificado"
  - "una clave efímera de prueba se presenta como custodia productiva"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T178
nombre: La reconciliación pendiente se deduce del registro auxiliar y sólo se retira por transición explícita
cubre: [g.9, g.2 I-g7, g.16 G-A5, g.16 G-A6]
dado:
  - "un escenario dirigido que agota los reintentos y escribe el registro operativo auxiliar"
cuando:
  - "se consulta la reconciliación pendiente, se resuelve por transición explícita y se intenta borrarla a mano"
entonces:
  - "la existencia del registro permite deducir `reconciliacion-pendiente` de forma INEQUÍVOCA"
  - "el registro identifica producto, repositorio, item, intento, causa y momento lógico"
  - "la resolución es una transición auditable que deja rastro en el diario"
  - "borrar el registro a mano rompe su cadena y produce fallo cerrado"
falla_si:
  - "el registro auxiliar es el estado canónico o el diario con otro nombre"
  - "la pendencia desaparece sin una transición que la explique"
  - "quitarle la COLA al registro pasa desapercibido: una cadena de huellas no detecta que le quiten la última línea"
  - "la comprobación vive sólo en la verificación y no en el camino de lectura que deduce la pendencia"
  - "el registro modifica por sí mismo el estado canónico"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T179
nombre: Una versión de esquema desconocida falla CERRADO, y subir de versión exige migración declarada
cubre: [g.10, g.11, g.16 G-A7]
dado:
  - "un almacén heredado sin declaración de formato, y otro con una versión que este lector no entiende"
cuando:
  - "se abren, se migra el primero y se intenta migrar a una versión no registrada"
entonces:
  - "la versión desconocida produce error tipado y no una adivinanza"
  - "la migración soportada corre como una transacción normal, auditable y recuperable"
  - "una migración no registrada se rechaza por su nombre, sin efectos parciales"
falla_si:
  - "un lector adivina el significado de una versión que no conoce"
  - "existe migración implícita al leer"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T180
nombre: Los quince pasos del escenario extremo a extremo, sobre un control repo real
cubre: [g.3, g.4, g.5, g.6, g.8, g.9, g.13, g.16]
dado:
  - "un repositorio de control temporal y el punto ejecutable del motor"
cuando:
  - "se recorren los quince pasos con procesos reales: inicializar, leer, transicionar, interrumpir, reiniciar, recuperar, concurrir, agotar reintentos, reconciliar y resolver"
entonces:
  - "no se pierde ninguna transición confirmada y no se publica ninguna incompleta"
  - "el estado final es íntegro y la evidencia es auditable"
  - "dos ejecuciones seguidas producen bytes idénticos"
falla_si:
  - "algún paso se simula en vez de ejecutarse"
  - "la salida lleva reloj, duración, identidad de proceso o ruta absoluta, y deja de ser reproducible"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/escenario_extremo_a_extremo.py
estado: prueba-superada
evidencia: evidencia/estado-e2e-salida.txt
```

```yaml ads:escenario
id: T181
nombre: La especificación normativa vigente viaja al proyecto instalado, derivada y no escrita a mano
cubre: [FD-3, C6, E2.0]
dado:
  - "un proyecto creado con el arranque documentado, en un temporal"
cuando:
  - "se comprueba qué especificación normativa llegó al control repo creado"
entonces:
  - "llegan las secciones aprobadas, la sección (g) y TODAS las enmiendas vigentes"
  - "la lista se DERIVA del árbol: añadir una enmienda no exige tocar el arranque"
  - "el runtime del estado durable viaja con el kernel al proyecto instalado"
falla_si:
  - "la lista de copia vuelve a escribirse a mano y caduca en cuanto F5 emite una enmienda más"
  - "el proyecto instalado queda con un enlace roto a una sede que el corpus operativo nombra"
ejecucion: validador-estructural
validador: kernel/operativo/validadores/comprobar_arranque.py
estado: prueba-superada
evidencia: evidencia/arranque-salida.txt
```

```yaml ads:escenario
id: T312
nombre: El sellado compacta el diario retirando el cuerpo de los eventos, y jamás su eslabón
cubre: [g.7, g.1, CONTRATO-ESTADO-DURABLE 6 bis]
dado:
  - "un almacén con historia real: transiciones multiarchivo confirmadas, y un umbral calibrado más corto que esa historia"
cuando:
  - "se sella el diario y se MIDE el fichero en disco antes y después"
entonces:
  - "el diario ocupa menos bytes que antes: compactar es una propiedad del fichero, no de una estructura en memoria"
  - "el diario conserva EXACTAMENTE una línea por evento, más la del `diario.sellado` que explica la retirada"
  - "cada talón conserva `esquema`, `secuencia`, `tipo`, `previo` y `huella`, y declara qué campos se le retiraron"
  - "la cola que el umbral reserva queda intacta, y `almacen.inicializado` y `transicion.preparada` no se sellan nunca"
falla_si:
  - "sellar no retira ni un byte: un sellado que no compacta no es el sellado que `g.7` escribe"
  - "sellar retira LÍNEAS en vez de cuerpos, y con ellas la secuencia, el eslabón siguiente y el recuento que la revisión publicada exige"
  - "se sella el punto de no retorno o el arranque del linaje, que la recuperación y la auditoría leen enteros"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T313
nombre: La cadena de huellas y la auditoría siguen verificándose sobre un diario sellado
cubre: [g.7, g.5, g.13]
dado:
  - "un almacén cuyo diario ya se ha sellado, y su revisión publicada anterior al sellado"
cuando:
  - "se leen los eventos, se exige coherencia, se verifica integridad, se audita y se detecta bifurcación"
  - "se vuelve a sellar tras nuevas transiciones, y se aplica una transición más sobre el diario ya sellado"
entonces:
  - "la cadena de `previo` casa eslabón a eslabón de principio a fin"
  - "la auditoría reproduce el mismo `cid_raiz` desde el diario que la revisión declara"
  - "el linaje se reconstruye entero y la detección de bifurcación sigue reconociendo la revisión propia"
  - "un almacén sellado sigue admitiendo transiciones nuevas: anexar toma la huella de la última línea y la encuentra"
falla_si:
  - "sellar rompe la verificabilidad del eslabón, que es la restricción de diseño que manda"
  - "la auditoría deja de reproducir la raíz porque el sellado se llevó lo que `g.13` necesita"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T314
nombre: La recuperación de g.8 funciona sobre un diario sellado, en sus dos ramas
cubre: [g.7, g.8, g.4]
dado:
  - "un almacén con el diario ya sellado, y los puntos de corte inyectables del protocolo"
cuando:
  - "se mata un escritor real antes del punto de no retorno, y en otra pasada entre los pasos 8 y 9"
  - "se reabre el almacén, que recupera"
entonces:
  - "la rama REVERTIR pierde la transición y no publica nada, y el diario sellado lo explica"
  - "la rama COMPLETAR republica y confirma leyendo la `transicion.preparada`, que el sellado nunca toca"
  - "el almacén queda íntegro y auditable tras cada una de las dos ramas"
falla_si:
  - "el sellado se lleva el cuerpo que la recuperación necesita y una de las dos ramas deja de poder cerrarse"
  - "la recuperación sobre un diario sellado publica una transición que debía revertirse"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T315
nombre: Una transacción que todavía puede estar en su ventana no se sella
cubre: [g.7, g.8]
dado:
  - "un almacén con una transacción abierta y sin cerrar, dejada por una caída real"
cuando:
  - "se intenta sellar el diario, y se pregunta por separado qué eventos serían sellables sin cola reservada"
entonces:
  - "sellar se niega con `SELLADO_IMPOSIBLE` y no toca ni un byte del diario"
  - "ningún evento de la transacción sin cerrar entra en la lista de sellables, aunque no haya cola que lo proteja"
falla_si:
  - "se compacta por encima de una ventana abierta, haciendo parecer cerrada una historia que no lo está"
  - "lo único que protege la ventana es la cola del umbral, que es un parámetro y no una garantía"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T316
nombre: El umbral del sellado es calibrable en el contrato derivado, y su ausencia es fallo cerrado
cubre: [g.7, CONTRATO-ESTADO-DURABLE 6 bis]
dado:
  - "el contrato derivado, que declara el umbral en un bloque de calibración, y sedes alternativas del contrato para la prueba"
cuando:
  - "se lee el umbral de dos sedes que sólo difieren en el número, y se sella con cada una"
  - "se lee el umbral de sedes sin bloque, sin la clave, con cero, con un negativo, con un texto, con un fraccionario, con JSON roto y con dos declaraciones"
  - "se pasa un umbral absurdo por la API y por el punto ejecutable"
entonces:
  - "cambiar el número en el contrato cambia lo que se sella, sin tocar una línea de código"
  - "cada forma de umbral inservible produce `UMBRAL_DE_SELLADO_INVALIDO` y no se sella nada"
  - "el punto ejecutable devuelve el código de salida del fallo tipado del kernel"
falla_si:
  - "el umbral es una constante del código con nombre en mayúsculas y el contrato sólo lo describe"
  - "un umbral ausente o ilegible cae en un valor por omisión silencioso, y la sede queda de decorado"
  - "el valor se valida al leer el contrato y no cuando entra por la llamada, que es la puerta de atrás"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T317
nombre: Retirar el cuerpo de un evento sin transición explícita es fallo cerrado
cubre: [g.7, g.13]
dado:
  - "un almacén con historia, y un diario editado a mano para vaciar el cuerpo de un evento conservando su huella"
cuando:
  - "se pide sellar sin autor o sin motivo, en sus seis combinaciones"
  - "se lee el diario cuyo cuerpo se vació a mano"
entonces:
  - "una retirada sin autor y sin motivo produce `RETIRADA_SIN_TRANSICION` y no toca el diario"
  - "un cuerpo vaciado a mano produce `DIARIO_CORRUPTO`, y el error nombra la transición que falta"
falla_si:
  - "se puede retirar un cuerpo sin dejar quién lo decidió ni por qué, que es un borrado y no una transición"
  - "vaciar un cuerpo conservando la huella pasa desapercibido porque no rompe ningún eslabón"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T318
nombre: La retirada dirigida respeta lo que la recuperación necesita y deja rastro auditable
cubre: [g.7, g.8, g.13]
dado:
  - "un almacén con una transacción sin cerrar, su punto de no retorno y el arranque de su linaje"
cuando:
  - "se pide retirar dirigidamente el cuerpo de cada uno de ellos, y el de un evento que no existe"
  - "se retira el cuerpo de un evento que sí es admisible"
  - "se sella y se retira desde el punto ejecutable"
entonces:
  - "cada retirada inadmisible produce `RETIRADA_NO_ADMISIBLE` y no toca el diario"
  - "la retirada admisible deja en el diario un evento que dice autor, motivo, qué secuencias se llevó y qué ancla las verifica"
  - "el punto ejecutable sella con los mismos códigos de salida que las demás órdenes, y el resto del motor sigue funcionando sobre el diario sellado"
falla_si:
  - "la retirada dirigida se salta las comprobaciones de conservación por ser un acto de autoridad"
  - "se retira un cuerpo sin dejar rastro de quién y por qué"
  - "el sellado sólo existe en la API y no en el punto ejecutable del motor"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

```yaml ads:escenario
id: T319
nombre: Alterar un evento sellado lo caza la verificación de la cadena
cubre: [g.7, g.5, g.15]
dado:
  - "un diario ya sellado, y las cuatro formas de alterar un talón: su resumen, su huella, un campo conservado y un campo repuesto"
cuando:
  - "se altera cada una y se lee el diario"
  - "se borra el evento de sellado y se lee el diario"
  - "se sustituye la comprobación del ancla por una que no comprueba nada, y se vuelve a leer"
entonces:
  - "cada alteración produce `DIARIO_CORRUPTO`: el ancla cubre el talón entero y no tres campos suyos"
  - "borrar el evento de sellado deja talones sin transición que los explique, y también se caza"
  - "sin la comprobación, el diario alterado pasa como bueno: el control del control se EJECUTA y no se afirma"
falla_si:
  - "un talón se puede editar a mano con la cadena intacta, porque su huella no se recalcula"
  - "la prueba del ancla sigue verde con la comprobación retirada, y entonces es decorado"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```

---

## `T320`–`T327` · `ADJ-B1` — la migración `0→1` sobre un almacén heredado **REAL**

**Qué cierran.** El bloqueante `ADJ-B1` del gate del 2026-09-04. De las **cinco** llamadas a
`_publicar_revision` del árbol, una —la de la migración— no pasaba el `testigo` que `E-08`
hizo obligatorio de sólo palabra clave. Reproducido sobre un almacén heredado **genuino**
—`estado/canonico/items/it-uno.json` y nada más: sin `FORMATO.json`, sin diario y sin
`REVISION.json`—:

```text
$ ads_estado.py --repo mig migrar
  File ".../estado/migracion.py", line 178, in _migrar_0_a_1
    almacen._publicar_revision(revision_cero)
TypeError: Almacen._publicar_revision() missing 1 required keyword-only argument: 'testigo'
EXIT=1     stdout VACÍO · SIETE rutas absolutas del anfitrión · CERO códigos tipados

$ ads_estado.py --repo mig migrar        (2ª y 3ª llamada)
[ESTADO_CORRUPTO] el fichero no existe (estado/REVISION.json)
EXIT=1
```

**Y el agravante, también medido.** Con la línea corregida en una copia, un heredado NUEVO
migraba (`EXIT=0`) y el almacén que ya había pasado por el fallo seguía dando
`ESTADO_CORRUPTO`: la fundación del diario y la publicación de la revisión 0 eran dos actos,
la guarda de la rama miraba el primero y un corte entre los dos dejaba un almacén al que la
rama de fundación no volvía a entrar nunca. El remedio son tres cosas: la línea, el fixture
y un camino de recuperación.

**Por qué ninguna prueba lo veía.** `test_09` fabricaba el «heredado» con `inicializar()` y
un `os.remove(FORMATO.json)` a continuación: ese almacén tiene diario **y** tiene
`REVISION.json`, así que la rama rota **no se entra**. La prueba pasaba sobre un camino que
el código productivo no recorre. `test_09` se conserva —cubre el heredado por PÉRDIDA del
fichero de formato, que es otro caso real— y lo que se añade es el que faltaba.

**El fixture se construye desde la especificación**, no del motor: el §7 del contrato dice
«`FORMATO.json` versiona el ALMACÉN; su ausencia es la versión 0 heredada» y el §1 fija
`canonico/<dominio>/<id>.json`. Eso es todo lo que un almacén de versión 0 tiene, y así se
escribe: con `json.dump` corriente, sin `esquema` declarado y sin orden de claves.

**Los diez puntos de corte, medidos.** Cortando con `ADS_ESTADO_FALLO` en cada uno de los
diez puntos del §10, los diez convergen en el **mismo** `cid_raiz`. Siete retoman con UNA
llamada a `migrar()`; los tres anteriores al punto de no retorno necesitan DOS: la primera
cierra la ventana con `RECUPERACION_MARCADA` —tipada, sin traza— y la segunda retoma con
identificador propio.

```yaml ads:escenario
id: T320
nombre: Un almacén heredado REAL migra del formato 0 al 1 y publica la revisión esperada
cubre: [g.10, g.11, "E-08", "E-15", "ADJ-B1"]
dado:
  - "un almacén de versión 0 construido desde la especificación del §7: `canonico/<dominio>/<id>.json` con tres objetos, sin `FORMATO.json`, sin diario y sin `REVISION.json`"
cuando:
  - "se ejecuta `ads_estado.py --repo <almacén> migrar --json` en un proceso real"
  - "se intercepta `_publicar_revision` y se mira con qué testigo la llama la migración"
entonces:
  - "la migración termina con código 0, sin traza y sin rutas absolutas del anfitrión"
  - "la fundación publica la revisión 0 con el testigo DECLARADO de fundación, y ninguna publicación se hace sin testigo"
  - "la revisión publicada es la 1, hija de la 0, con la transacción que el informe nombra y con los tres objetos normalizados a `ads.estado/1`"
  - "`verificar_integridad` y `auditar` no encuentran ni un hallazgo sobre el almacén migrado"
falla_si:
  - "la llamada de la migración vuelve a omitir el `testigo` y el proceso muere con una `TypeError` no tipada"
  - "la migración se da por buena sobre un almacén que el propio motor había inicializado, que es el camino que el código productivo no recorre"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```
```yaml ads:escenario
id: T321
nombre: El almacén que la primera migración fallida dejó roto vuelve a ser migrable
cubre: [g.8, g.11, "ADJ-B1"]
dado:
  - "un almacén heredado REAL en el que la migración se corta con `ADS_ESTADO_FALLO=durante-el-diario`, que deja el diario fundado y `REVISION.json` AUSENTE"
cuando:
  - "se comprueba que el corte dejó exactamente ese estado"
  - "se vuelve a llamar a `migrar` desde el punto ejecutable"
entonces:
  - "la segunda llamada termina con código 0 y el almacén queda migrado y verificable"
  - "la fundación NO se anexa dos veces: el diario sigue teniendo un solo `almacen.inicializado`"
falla_si:
  - "la guarda de la rama de fundación vuelve a mirar el evento del diario en vez de la revisión que falta, y el almacén queda inmigrable incluso con el testigo puesto"
  - "la reanudación funda otra vez el diario y parte el linaje en dos"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```
```yaml ads:escenario
id: T322
nombre: Los diez puntos de corte de una migración convergen en la misma revisión
cubre: [g.4, g.8, g.11, "E-08"]
dado:
  - "un almacén heredado REAL por cada uno de los diez puntos de corte declarados en el §10"
  - "la revisión que produce la migración sin cortes, tomada como referencia"
cuando:
  - "se corta la migración en cada punto con `ADS_ESTADO_FALLO`, en procesos reales que mueren por `os._exit(70)`"
  - "se vuelve a llamar a `migrar` hasta tres veces"
entonces:
  - "los diez almacenes acaban con el MISMO `cid_raiz` que la migración sin cortes"
  - "siete puntos retoman con una sola llamada, y los tres anteriores al punto de no retorno con dos"
  - "la llamada que cierra la ventana sale con `RECUPERACION_MARCADA`, tipada y sin traza"
falla_si:
  - "algún punto de corte deja el almacén inmigrable, o lo lleva a un estado canónico distinto del de la migración sin cortes"
  - "la expectativa de cada punto se decide después de mirar el resultado en vez de antes"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```
```yaml ads:escenario
id: T323
nombre: El paso 9 de la migración no publica sin el testigo del paso 8
cubre: ["E-08", g.8, g.11]
dado:
  - "un almacén heredado REAL y el paso 8 intervenido para que no deje testigo, o para que deje uno que habla de otra transacción"
cuando:
  - "se ejecuta la migración con cada una de las dos intervenciones"
entonces:
  - "las dos producen `ESTADO_CORRUPTO`, y ninguna publica la revisión de la migración"
  - "`FORMATO.json` no llega a escribirse: el almacén sigue siendo heredado y sigue siendo migrable"
falla_si:
  - "la migración publica una revisión que nombra objetos que el paso 8 no dejó en `canonico/`"
  - "el testigo se comprueba sólo en el camino de transición corriente y no en el de migración"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```
```yaml ads:escenario
id: T324
nombre: Migrar dos veces no mueve la revisión ni reescribe el estado canónico
cubre: [g.11, "I-g3"]
dado:
  - "un almacén heredado REAL ya migrado, con su revisión, su diario y los bytes de sus objetos canónicos"
cuando:
  - "se vuelve a ejecutar `migrar` sobre él"
entonces:
  - "el informe declara `desde 1` y `hasta 1` y no aplica ninguna migración"
  - "la revisión no se mueve, el diario no crece y ni un byte de `canonico/` cambia"
falla_si:
  - "una segunda migración anexa eventos, publica una revisión nueva o reescribe los objetos con el mismo contenido"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```
```yaml ads:escenario
id: T325
nombre: Un formato del futuro no se migra ni se adivina
cubre: [g.10, g.11]
dado:
  - "un almacén ya migrado cuyo `FORMATO.json` se reescribe declarando la versión 99"
cuando:
  - "se intenta migrarlo desde el punto ejecutable"
  - "se pide migrar a una versión sin registrar, y también hacia atrás"
entonces:
  - "el formato desconocido produce `FORMATO_DESCONOCIDO` sin traza"
  - "la migración a una versión sin registrar y la descendente producen `MIGRACION_DESCONOCIDA`"
falla_si:
  - "una versión de formato que este motor no entiende se abre «a lo que se pueda»"
  - "bajar de versión se simula en vez de declararse inexistente"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```
```yaml ads:escenario
id: T326
nombre: Sin revisión vigente y con el diario poblado, la migración no adivina
cubre: [g.8, "I-g7", g.11]
dado:
  - "un almacén ya migrado al que se le retiran `FORMATO.json` y `REVISION.json`, de modo que vuelve a parecer heredado y su diario ya lleva transiciones"
  - "un almacén cortado durante la fundación, con el `resultado` de su evento de fundación alterado a mano"
cuando:
  - "se intenta migrar cada uno de los dos"
entonces:
  - "el del diario poblado produce `MIGRACION_NO_RECUPERABLE`: cuál era la revisión vigente no se deduce sin reproyectar el diario"
  - "el de la fundación alterada falla cerrado con código tipado en vez de publicar una revisión 0 que el diario no declara"
falla_si:
  - "la migración recompone una revisión vigente cualquiera para poder seguir"
  - "la revisión 0 recompuesta se publica sin contrastarla con lo que el diario declara"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```
```yaml ads:escenario
id: T327
nombre: La CLI de migración no publica ni trazas ni rutas absolutas del anfitrión
cubre: ["E-15", g.11]
dado:
  - "cuatro caminos de la orden `migrar`: el sano, uno sin revisión vigente, uno sobre un `estado/` vacío y uno sobre un repo que no existe"
cuando:
  - "se ejecuta cada uno en un proceso real y se recoge su salida entera"
entonces:
  - "ninguno publica un `Traceback` ni una ruta absoluta del anfitrión, ni por `stdout` ni por `stderr`"
  - "los caminos de error salen con código 1 y con su código tipado en `stderr`"
falla_si:
  - "un error no tipado cruza `main()` y se publica como traza con las rutas de la máquina"
  - "un fallo de la operación se confunde con un defecto de programación por compartir código de salida y forma"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_estado_durable.py
estado: prueba-superada
evidencia: evidencia/estado-durable-salida.txt
```
