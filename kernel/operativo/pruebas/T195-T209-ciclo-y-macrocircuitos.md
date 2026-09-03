# T195–T209 — el ciclo, `Continúa` y los cuatro macrocircuitos

Conformidad del **macrobloque 3 de `F6`**. Su contrato derivado:
[`CONTRATO-CICLO-Y-MACROCIRCUITOS.md`](../runtime/CONTRATO-CICLO-Y-MACROCIRCUITOS.md), que
instancia `11-ARQ` §7.2, §7.4, §8.0, §9.6 y §18, `b.16` en
[`../recorrido/01-PROCESOS.md`](../recorrido/01-PROCESOS.md), `b.14`, `C4`, `C5` y la
taxonomía de [`../entrada/01-TAXONOMIA.md`](../entrada/01-TAXONOMIA.md).

**Todo esto EJECUTA.** Control repos reales en directorios temporales, repositorios Git
reales sin red, un proceso que toma un lease y se mata con `SIGKILL` de verdad, y dos
procesos reales compitiendo por la autoridad sobre el mismo producto. Ningún mock hace de
pieza en ningún sitio.

**Tres ejecutables:**

```text
runtime/pruebas/test_ciclo.py           T195..T202 — encuadre, `b.16`, `C4`, gates, `C5`
runtime/pruebas/test_continua.py        T203..T205 — los siete pasos y los diez escenarios
runtime/pruebas/test_macrocircuitos.py  T206..T209 — §18, la `FASE 0` y `X-S1`..`X-S11`
```

**Ninguna de ellas certifica nada.** `prueba-superada` significa que la prueba se ejecutó y
pasó. La CERTIFICACIÓN de `F6` la emite un juicio independiente y no quien construyó.

```yaml ads:escenario
id: T195
nombre: El encuadre clasifica la entrada del Owner y sólo tres clases crean trabajo
cubre: [11-ARQ 7.2, entrada 01-TAXONOMIA, C6]
dado:
  - "un control repo real y una entrada del Owner con su expresión literal, fecha y canal"
cuando:
  - "se encuadra: producto, control repo, fuentes, perfil, política y precondiciones"
entonces:
  - "las nueve clases se derivan del corpus y sólo tres declaran crear trabajo"
  - "la frontera entre idea inmadura y candidato aplica las tres casillas escritas"
  - "el encuadre descubre las fuentes de SOURCES.toml sin copiar ningún remoto"
  - "el encuadre es determinista y no contiene ninguna ruta absoluta de la máquina"
falla_si:
  - "una clase que no crea trabajo produce proceso, o un remoto aparece en el estado durable"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_ciclo.py
estado: prueba-superada
evidencia: evidencia/ciclo-salida.txt
```

```yaml ads:escenario
id: T196
nombre: La ruta se compone desde b.16 por las cuatro vías, y el gate de composición no abre la fase
cubre: [11-ARQ 8.0, b.16, b.1, a.6]
dado:
  - "los diez procesos derivados de sus bloques ads:proceso y un encuadre que crea trabajo"
cuando:
  - "se compone la ruta con las condiciones declaradas verdaderas"
entonces:
  - "renombrar el título no cambia la ruta y un sinónimo no activa ninguna capacidad"
  - "las cuatro vías se distinguen y no hay una quinta"
  - "las tres formas de estar presente que no son participar quedan fuera de participantes"
  - "una capacidad sin vía produce composicion-incompleta nombrando capacidad y fase"
  - "una condición vaga se rechaza y el propietario de AUD y DIR se deriva del encargo"
falla_si:
  - "el proceso se elige por coincidencias léxicas sobre texto libre"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_ciclo.py
estado: prueba-superada
evidencia: evidencia/ciclo-salida.txt
```

```yaml ads:escenario
id: T197
nombre: C4 materializa equipos por capacidad, nunca por método, y lo que no cabe espera
cubre: [C4, C1, b.11]
dado:
  - "las composiciones reales de una capacidad, en el orden en que están escritas"
cuando:
  - "se materializa el equipo con sus condiciones declaradas y sus execution_slots"
entonces:
  - "un método nunca se usa como capacidad, y la confusión tiene error propio"
  - "se elige la primera composición cuya condición consta verdadera, en su orden escrito"
  - "lo que no cabe queda esperando-capacidad y la composición no se reduce"
  - "independientes manda sobre combinables y el equipo se persiste por el motor"
falla_si:
  - "el equipo se recorta para caber, o dos roles independientes comparten agente"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_ciclo.py
estado: prueba-superada
evidencia: evidencia/ciclo-salida.txt
```

```yaml ads:escenario
id: T198
nombre: La planificación crea items y paquetes por el runtime y el despacho delega
cubre: [11-ARQ 7.2, b.15.1, a.9, gate:despacho-coherente]
dado:
  - "una ruta compuesta y un control repo con estado durable"
cuando:
  - "se planifica y se despacha un barrido completo"
entonces:
  - "los items y paquetes salen del runtime y el paquete conserva su vocabulario cerrado"
  - "la prioridad se deriva de la vía y la selección es determinista"
  - "b.15.1 abre el desbloqueador dentro del alcance autorizado y escala fuera de él"
  - "todo el despacho pasa por un único punto observable y no se aplica un efecto dos veces"
falla_si:
  - "existe una segunda máquina de despacho o un alta de trabajo paralela"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_ciclo.py
estado: prueba-superada
evidencia: evidencia/ciclo-salida.txt
```

```yaml ads:escenario
id: T199
nombre: Los gates se derivan del corpus, fallan cerrado y ninguno es fuente normativa
cubre: [11-ARQ 7.2, esquemas/gate.yaml]
dado:
  - "el censo de gates derivado de los bloques ads:gate del corpus"
cuando:
  - "se aplica un gate con su entrada, su evidencia y su revisor"
entonces:
  - "el censo derivado coincide con un barrido independiente del árbol"
  - "sin todas las comprobaciones y toda la evidencia el dictamen es negativo y no hay salida"
  - "un gate no puede escribir fuera de dictamenes ni ampliar la ruta"
  - "el revisor no puede ser quien construyó lo que se juzga"
falla_si:
  - "se aplica un gate que el corpus no declara, o un gate aprueba con reparos"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_ciclo.py
estado: prueba-superada
evidencia: evidencia/ciclo-salida.txt
```

```yaml ads:escenario
id: T200
nombre: C5 se aplica sobre las instancias declaradas, con acuse, rechazo y reanudación
cubre: [C5, 11-ARQ 8.0, esquemas/handoff.yaml]
dado:
  - "las instancias de circuitos y las cinco entregas que 11-ARQ 8.0 declara"
cuando:
  - "se emite una entrega y su receptor comprueba antes de tomar custodia"
entonces:
  - "toda instancia trae los once campos obligatorios del esquema"
  - "las cinco entregas de 8.0 están materializadas con sus extremos correctos"
  - "rechazar no cambia la custodia y no cuenta para el freno; devolver sí"
  - "una devolución sin los cuatro campos se rechaza como devolución"
falla_si:
  - "una entrega existe sólo en la conversación, o un rechazo gasta una devolución"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_ciclo.py
estado: prueba-superada
evidencia: evidencia/ciclo-salida.txt
```

```yaml ads:escenario
id: T201
nombre: El cierre comprueba las obligaciones, no las declara, y el trabajo derivado conserva su enlace
cubre: [b.10, b.3, b.5, b.9, gate:cierre-de-item]
dado:
  - "un item con su plan, sus paquetes y las obligaciones de su proceso"
cuando:
  - "se propone cerrar, bloquear, pausar, escalar o derivar trabajo"
entonces:
  - "cancelar un paquete no retira su obligación y la deja huérfana"
  - "DSP no retira, y toda retirada identifica autoridad y explica cómo afecta"
  - "el informe separa satisfechas de retiradas y no las suma"
  - "la integración la declara el propietario global, y el item derivado enlaza a su origen"
falla_si:
  - "un item cierra con una obligación huérfana, o DSP declara la integración semántica"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_ciclo.py
estado: prueba-superada
evidencia: evidencia/ciclo-salida.txt
```

```yaml ads:escenario
id: T202
nombre: El corpus se lee con la biblioteca estándar y la salida es determinista
cubre: [I-g3, 11-ARQ 7.2]
dado:
  - "los bloques canónicos del corpus real y los ficheros de esquemas"
cuando:
  - "se analizan con el analizador acotado del kernel"
entonces:
  - "el resultado coincide bloque a bloque con el de la biblioteca de referencia"
  - "lo que el subconjunto no cubre falla cerrado y nombra su fichero"
  - "las quince capacidades del árbol y las de 11-ARQ 18 coinciden"
  - "dos ejecuciones desde directorios de trabajo distintos dan bytes idénticos"
falla_si:
  - "el analizador ignora en silencio lo que no entiende, o la salida depende del cwd"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_ciclo.py
estado: prueba-superada
evidencia: evidencia/ciclo-salida.txt
```

```yaml ads:escenario
id: T203
nombre: Continúa recorre los siete pasos de b.14 y su paso 2 ejecuta las ocho comprobaciones
cubre: [b.14, 11-ARQ 7.4, b.8, g.9]
dado:
  - "un control repo con trabajo planificado y estado durable"
cuando:
  - "se ejecuta Continúa en modo plan"
entonces:
  - "los siete pasos se recorren en orden y el paso 7 no se ejecuta en modo plan"
  - "la deriva no transaccional se reporta y escala, y no se selecciona nada"
  - "una espera que dejó de ser viable se convierte en bloqueo"
  - "las celdas de cobertura vencidas sólo se reportan, sin abrir trabajo"
  - "una orden emitida sobre otra base se declara caduca y no se aplica"
falla_si:
  - "Continúa despacha todo lo pendiente, o resuelve una reconciliación por su cuenta"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_continua.py
estado: prueba-superada
evidencia: evidencia/continua-salida.txt
```

```yaml ads:escenario
id: T204
nombre: Los diez escenarios de Continúa, cada uno con proceso y estado reales
cubre: [b.14, 11-ARQ 7.4, C5, C6]
dado:
  - "un control repo real y procesos reales que se detienen, mueren o dejan trabajo a medias"
cuando:
  - "se ejecuta Continúa desde otra instancia"
entonces:
  - "un proceso detenido limpiamente deja el paquete completado y sin lease huérfano"
  - "un proceso muerto con SIGKILL deja el paquete en curso, con efecto y sin acuse"
  - "un artefacto declarado y ausente escala, y un handoff emitido se reporta"
  - "un gate fallido, un paquete pausado y una reconciliación abierta no se seleccionan"
  - "el trabajo automático por política se retoma, y dos repositorios se descubren"
  - "sin trabajo elegible se dice, y no se abre nada"
falla_si:
  - "Continúa roba un lease vivo, o fabrica trabajo cuando la cola está vacía"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_continua.py
estado: prueba-superada
evidencia: evidencia/continua-salida.txt
```

```yaml ads:escenario
id: T205
nombre: Dos ejecuciones consecutivas de Continúa dan los mismos bytes y no mueven el estado
cubre: [I-g3, b.14, a.8, a.10]
dado:
  - "un control repo cuyo estado no cambia entre las dos ejecuciones"
cuando:
  - "se ejecuta Continúa dos veces seguidas"
entonces:
  - "los dos planes son idénticos byte a byte y su huella coincide"
  - "revision_id y cid_raiz son los mismos antes y después"
  - "dos instancias con nombres distintos producen el mismo plan"
  - "la ejecución no interactiva se niega si queda una decisión del Owner"
falla_si:
  - "el plan lleva la instancia, el cwd o una ruta de la máquina"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_continua.py
estado: prueba-superada
evidencia: evidencia/continua-salida.txt
```

```yaml ads:escenario
id: T206
nombre: El conjunto derivado de los cuatro macrocircuitos coincide con la tabla de 11-ARQ 18
cubre: [11-ARQ 18, 11-ARQ 8.0, b.16]
dado:
  - "la tabla de 11-ARQ 18 y la definición derivada que vive en el kernel"
cuando:
  - "se analiza la tabla del documento y se compara fila a fila"
entonces:
  - "macrocircuito, fase, proceso, propietario y gate coinciden en las trece filas"
  - "la secuencia de procesos derivada es la que 11-ARQ 8.0 escribe, con la FASE 0 dentro"
  - "cada fase compone su ruta y sus participantes son los que la fila nombra"
  - "la FASE 0 es la misma en los cuatro, campo a campo"
falla_si:
  - "la proyección del kernel y la tabla dejan de coincidir sin que nada lo diga"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_macrocircuitos.py
estado: prueba-superada
evidencia: evidencia/macrocircuitos-salida.txt
```

```yaml ads:escenario
id: T207
nombre: La FASE 0 resuelve los seis identificadores y escribe en su soporte propio
cubre: [11-ARQ 9.6, O17]
dado:
  - "un control repo sin estado durable y el disparador de un macrocircuito"
cuando:
  - "se ejecuta la FASE 0"
entonces:
  - "los seis identificadores se resuelven y el segundo se acuña por huella de los otros"
  - "el soporte queda fuera de estado, y estado no existe cuando la fase termina"
  - "repetirla sobre el mismo disparador produce la misma declaración"
  - "la incorporación a cobertura no reemite y conserva la misma huella"
falla_si:
  - "la fase consume un contador, abre iniciativa o escribe dentro de estado"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_macrocircuitos.py
estado: prueba-superada
evidencia: evidencia/macrocircuitos-salida.txt
```

```yaml ads:escenario
id: T208
nombre: Las once filas adversariales X-S1 a X-S11 de la FASE 0 dan el resultado exigido
cubre: [11-ARQ 9.6, O17]
dado:
  - "un control repo y la FASE 0 de un macrocircuito"
cuando:
  - "se intenta cada uno de los once escenarios adversariales"
entonces:
  - "cada fila falla con su código propio y nombra lo que la norma exige nombrar"
  - "omitir la FASE 0 impide la primera mutación, y una certificación copiada no vale"
  - "una sola huella distinta invalida la reutilización de evidencia"
  - "el veto de SEG no lo levanta nadie y el propietario no puede sustituir a SIS"
falla_si:
  - "una fila falla con un error genérico que no distingue qué salió mal"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_macrocircuitos.py
estado: prueba-superada
evidencia: evidencia/macrocircuitos-salida.txt
```

```yaml ads:escenario
id: T209
nombre: Los cuatro macrocircuitos se ejecutan por el mismo motor y no comparten autoridad
cubre: [11-ARQ 18, 11-ARQ 8.4, CI-5, g.6]
dado:
  - "los cuatro macrocircuitos y un control repo real por cada uno"
cuando:
  - "cada uno recorre su FASE 0, abre, compone, planifica, despacha y termina"
entonces:
  - "los cuatro terminan de forma inequívoca y su terminación queda escrita"
  - "con el gate en rojo ninguno abre estado ni deja soporte que deshacer"
  - "las cuatro ejecuciones pasan por el mismo punto de despacho y por ningún otro"
  - "dos procesos reales sobre el mismo producto: exactamente uno adquiere la autoridad"
falla_si:
  - "existen cuatro implementaciones divergentes, o dos autoridades sobre un producto"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_macrocircuitos.py
estado: prueba-superada
evidencia: evidencia/macrocircuitos-salida.txt
```
