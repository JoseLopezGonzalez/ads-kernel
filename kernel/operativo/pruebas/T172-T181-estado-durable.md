# T172–T181 — el estado durable, ejecutado

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
runtime/pruebas/escenario_extremo_a_extremo.py T180 — los quince pasos, de una sola pieza
validadores/comprobar_arranque.py              T181 — la norma viaja al proyecto instalado
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
cubre: [g.1, g.2 I-g1, g.16 G-A1]
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
