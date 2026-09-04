# T250–T269 — cuántos agentes por rol (`C4`), y cómo se elige el siguiente trabajo (`b.12`)

**Qué cierran.** Dos hallazgos bloqueantes de la certificación del 2026-09-03.

`E-01` · **la cardinalidad real de `C4`**. Las TRES composiciones que declaran varios
agentes sobre un mismo rol materializaban **UNO**, con `reparto_de_agentes` vacío,
sin error, sin aviso y sin `esperando-capacidad`, y el registro durable quedaba
internamente contradictorio: publicaba «2 o 3» al lado de un agente único. La causa estaba
escrita en el propio módulo: el reparto entraba como **parámetro externo** porque se daba
por hecho que el campo `agentes` era prosa y que derivar de ahí «exigiría reglas léxicas
sobre texto libre». La medición desmontó la premisa — noventa y nueve valores en
**veintidós formas**, tres de ellas plurales —: no es texto libre, es un vocabulario
cerrado. Ahora el cardinal se DERIVA de la composición, el integrador se lee de su campo
`ampliacion`, y las tres condiciones de `C4` se comprueban de verdad.

`E-06` · **`b.12` completa**. De los cuatro criterios de orden del paso 5 sólo estaban
(a) prioridad y (d) identificador; faltaban (b) grado de salida en el grafo y (c) antigüedad
de espera. De los cuatro campos de la detección de inanición no existía ninguno. Ahora están
los cuatro y los cuatro, con persistencia durable, reanudación y concurrencia, y la
antigüedad se mide con el **reloj lógico** del estado —la revisión del motor—, nunca con la
hora de pared que `a.9` prohíbe en el estado canónico.

**Sedes normativas**, citadas en texto plano porque no viajan al proyecto instalado y un
enlace roto allí es el defecto que `E5` destapó: `kernel/operativo/contratos/C4-MATERIALIZACION.md`,
sección «Cuántos agentes por rol»; `docs/rediseno/b-RECORRIDO-APROBADA.md`, sección
«b.12 — Selección del siguiente trabajo, e inanición»; `kernel/operativo/capacidades/DIS/composicion.md`
y `kernel/operativo/capacidades/CON/composicion.md` como corpus de datos.

**Ninguna de las veinte mira texto.** Todas mueven el código sobre el corpus real del
kernel, sobre un control repo real con su catálogo de modelos y sobre un estado durable real
escrito por el motor. `T269` sabotea, en una COPIA del árbol y en procesos reales, los cuatro
criterios de orden, los cuatro campos de inanición y tres piezas de la cardinalidad, y exige
que **cada sabotaje ponga roja una prueba distinta**: es lo que demuestra que ningún criterio
queda decorativo.

> **El sabotaje que cierra `E-01`** —`agentes: "7 repartidos por artefacto, sin integrador"`,
> literalmente lo que `C4` llama prohibido— está además en el catálogo de infracciones
> deliberadas, en `kernel/operativo/validadores/negativos_cardinalidad.py`, y se ejecuta
> sobre una copia temporal del repositorio con
> `comprobar_negativos.py --caso N250`. Tiene que caer **por semántica** —varios agentes sin
> integrador declarado—, no por la huella del kernel, que saltaría con cualquier edición
> legítima.

```yaml ads:escenario
id: T250
nombre: El cardinal de agentes se deriva del corpus y hay tantos agentes como el cardinal dice
cubre: ["E-01", "C4 cuántos agentes por rol", "C4 paso 4", "C4 paso 7", "b.11 execution_slots"]
dado:
  - "el campo agentes de las composiciones tiene noventa y nueve valores en veintidós formas"
  - "exactamente tres de esas formas declaran más de un agente sobre un mismo rol"
  - "la composición declara su integrador en el campo ampliacion del bloque ads:composicion"
cuando:
  - "se deriva el censo de formas del corpus real y se lee cada una con el lector cerrado"
  - "se materializa composicion:dis-proyecto-nuevo con sus territorios y direcciones declarados"
entonces:
  - "el censo de composiciones plurales derivado es exactamente el medido, ni una más ni una menos"
  - "DIS/diseno-visual materializa tres agentes, uno por dirección explorada"
  - "DIS/investigacion-visual materializa dos agentes, uno por territorio"
  - "cada agente tiene identificador propio, unidad de reparto propia e integrador escrito"
  - "el equipo consume tantos execution_slots como agentes reales, no como roles"
falla_si:
  - "un rol que declara dos o tres materializa uno solo"
  - "el reparto de agentes sale vacío teniendo la composición un cardinal plural"
  - "los agentes de un rol repartido comparten identificador"
  - "aparece en el corpus una cuarta composición plural y el censo derivado no la ve"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T251
nombre: El registro durable del equipo no puede publicar dos o tres junto a un agente
cubre: ["E-01", "C4 paso 7", "materialización auditable"]
dado:
  - "el paso 7 de C4 es lo que convierte la materialización en auditable"
  - "el equipo escrito publica el cardinal de cada rol y la lista de sus agentes"
cuando:
  - "se materializa el equipo y después se fuerza sobre el objeto escrito la contradicción medida"
entonces:
  - "el equipo real pasa la comprobación de coherencia del reparto"
  - "retirar agentes dejando el cardinal intacto levanta reparto incoherente nombrando el rol"
  - "declarar un cardinal fuera del rango escrito en la composición también lo levanta"
falla_si:
  - "un equipo publica un cardinal y un número distinto de agentes y nadie lo detecta"
  - "un rol plural se publica sin integrador"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T252
nombre: Repartir por territorio sin territorios declarados falla cerrado
cubre: ["E-01", "C4 condición a", "reparto sin solapamiento"]
dado:
  - "C4 admite varios agentes cuando el trabajo se reparte por artefacto o superficie sin solapamiento"
  - "esa condición no se puede comprobar sin saber cuáles son las unidades del reparto"
cuando:
  - "se materializa una composición con reparto por territorio sin declarar los territorios"
  - "y después con territorios repetidos, con uno solo, y con más de los que el cardinal admite"
entonces:
  - "sin unidades declaradas se levanta reparto sin unidades nombrando el rol y la clave que falta"
  - "con unidades repetidas también, porque dos agentes sobre la misma unidad es el solapamiento prohibido"
  - "con una unidad se materializa un agente, dentro del cardinal escrito"
  - "con más unidades que el máximo escrito se levanta reparto incoherente"
falla_si:
  - "un reparto sin unidades declaradas se resuelve como un agente por omisión"
  - "el número de unidades declaradas puede salirse del cardinal que escribe la composición"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T253
nombre: La competencia exige criterio de comparación escrito ANTES de empezar
cubre: ["E-01", "C4 competencia", "composicion:dis-feature-visual"]
dado:
  - "C4 admite competencia sólo si el método la declara y con criterio escrito antes de empezar"
  - "el instante lógico de inicio del trabajo se declara en la lectura del paquete"
cuando:
  - "se materializa la competencia sin criterio, con criterio sin instante, con criterio posterior, con criterio simultáneo, sin inicio y con un método sin fase divergente"
  - "y después con criterio escrito en un instante estrictamente anterior al inicio"
entonces:
  - "los seis casos levantan criterio de comparación ausente"
  - "el caso correcto materializa dos agentes, con integrador y con el criterio escrito en cada uno"
  - "sin competencia declarada se materializa el mínimo del cardinal, que es el uno por defecto de C4"
falla_si:
  - "se admite una competencia cuyo criterio se escribió después de ver las propuestas"
  - "se admite una competencia sin criterio o sin poder situarla en el tiempo"
  - "se admite competencia con un método que no declara fase divergente"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T254
nombre: Varios agentes sin integrador declarado está prohibido
cubre: ["E-01", "C4 prohibición del integrador", "campo ampliacion de la composición"]
dado:
  - "la ampliacion de composicion:dis-proyecto-nuevo declara DIS/direccion-artistica como integrador"
  - "el runtime lee el integrador de la composición y no de un parámetro del llamador"
cuando:
  - "se borra la declaración de integrador en una copia del corpus y se materializa el equipo"
entonces:
  - "la lectura del integrador devuelve ausencia sobre la composición mutada"
  - "la materialización levanta varios agentes sin integrador nombrando la composición"
  - "sobre el corpus intacto el mismo equipo se materializa con su reparto"
falla_si:
  - "un rol materializa varios agentes y nadie exige quién integra el resultado"
  - "el integrador se puede declarar por la firma en vez de leerse de la composición"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T255
nombre: Un integrador que no es rol de la composición no integra nada
cubre: ["E-01", "C4 quién integra", "contraste contra la lista roles"]
dado:
  - "el integrador declarado en ampliacion se contrasta contra la lista roles de la composición"
cuando:
  - "se sustituye el integrador por un rol que la composición no declara y se materializa"
entonces:
  - "se levanta varios agentes sin integrador nombrando el rol inexistente"
falla_si:
  - "un integrador nombrado que no ocupa ningún rol se da por bueno"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T256
nombre: Un volumen que excede lo que un contexto sostiene no se despacha a ciegas
cubre: ["E-01", "C4 condición c", "esquemas/perfil-agente escala de contexto", "C2 paso 3"]
dado:
  - "el esquema perfil-agente declara la escala ordenada de contexto con cuatro escalones"
  - "el paquete puede declarar su volumen en unidades de trabajo"
  - "la capacidad de contexto se deriva de la posición en la escala y no de un número de tokens inventado"
cuando:
  - "se materializa un rol de un solo agente con un volumen mayor que su capacidad de contexto"
  - "y un rol con reparto declarado cuyas unidades no llegan a los agentes que el volumen exige"
entonces:
  - "los dos levantan volumen excede el contexto, con volumen, capacidad y agentes necesarios en el contexto del error"
  - "un volumen que cabe se materializa y queda publicado en la lectura del paquete"
falla_si:
  - "un paquete que no cabe en un contexto se despacha sin reparto y sin aviso"
  - "la capacidad de contexto se escribe a mano en vez de derivarse de la escala del esquema"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T257
nombre: Con slots insuficientes los agentes esperan, la composición no se reduce y nunca hay dos en un slot
cubre: ["E-01", "C4 paso 6", "b.11 execution_slots", "esperando-capacidad"]
dado:
  - "b.11 calcula la concurrencia a partir de agentes disponibles, de modo que la unidad del corte es el agente"
  - "C4 paso 6 deja fuera lo que no cabe y prohíbe reducir la composición para que quepa"
cuando:
  - "se materializa un equipo con un rol de tres agentes y menos slots que agentes"
  - "y se fuerza después una doble ocupación y una unidad de reparto repetida"
entonces:
  - "los agentes que no caben quedan esperando capacidad, con su agente asignado y sin slot"
  - "el censo de rol y unidad es idéntico con holgura y sin ella: la composición no se recorta"
  - "dos agentes en el mismo execution slot levantan agente sobreasignado"
  - "dos agentes del mismo rol sobre la misma unidad de reparto también"
falla_si:
  - "un rol de tres agentes ocupa un solo slot"
  - "lo que no cabe se retira de la composición en vez de esperar"
  - "dos agentes comparten slot o unidad de reparto sin que nadie lo detecte"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T258
nombre: Reanudar una materialización no puede cambiar el reparto en silencio
cubre: ["E-01", "C4 ampliación y reducción", "I-g3 determinismo"]
dado:
  - "C4 manda que al ampliar el equipo no se rehaga, y que el trabajo en curso conserve su custodia"
  - "un reparto cambiado deja al agente anterior produciendo sobre una unidad que ya no se declara"
cuando:
  - "se vuelve a materializar sobre el equipo ya escrito con el mismo reparto y con otro"
entonces:
  - "la reanudación idéntica produce el mismo equipo byte a byte y el mismo identificador"
  - "un reparto con distinto cardinal levanta reparto incoherente nombrando los roles que cambian"
  - "un reparto con las mismas unidades cambiadas de nombre también, aunque sean el mismo número"
falla_si:
  - "reanudar cambia el reparto y nadie lo dice"
  - "dos materializaciones del mismo estado producen equipos distintos"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T259
nombre: Un cardinal ilegible falla cerrado y nunca vale uno por omisión
cubre: ["E-01", "C4 cuántos agentes por rol", "vocabulario cerrado del campo agentes"]
dado:
  - "el vocabulario del campo agentes está enumerado y cerrado, derivado del censo del corpus"
  - "el valor de CON declara paralelismo de paquetes del mismo item, no pluralidad de agentes"
cuando:
  - "se leen nueve formas que el lector no conoce"
  - "se recorre el censo completo del corpus real"
  - "se inyecta en una copia del corpus el valor siete repartidos por artefacto sin integrador"
entonces:
  - "cada forma desconocida levanta cardinal de agentes ilegible"
  - "las veintidós formas del corpus se leen enteras"
  - "el valor de CON se lee como un agente por paquete, con paralelismo de paquetes marcado"
  - "el sabotaje se LEE como cardinal siete con reparto por artefacto e integrador negado"
  - "y la materialización cae por varios agentes sin integrador, que es una prohibición de C4, y no por ilegibilidad ni por la huella del kernel"
falla_si:
  - "un valor que el lector no entiende se resuelve como un agente"
  - "aparece una forma nueva en el corpus y el censo no la denuncia"
  - "el sabotaje de los siete agentes sólo se detecta por la huella del kernel"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T260
nombre: La prioridad declarada es el primer criterio de orden y manda sobre los otros tres
cubre: ["E-06", "b.12 paso 5 a", "autoridad del Owner sobre la prioridad"]
dado:
  - "la prioridad declarada es autoridad exclusiva del Owner y el sistema no la eleva nunca"
cuando:
  - "se monta una cola donde el de prioridad de fondo desbloquea a dos paquetes y lleva más tiempo listo"
entonces:
  - "el urgente encabeza la cola pese a perder en los criterios b y c"
  - "el grado de salida y la antigüedad se publican en la entrada elegible, para poder contrastarlo"
falla_si:
  - "la prioridad declarada deja de ser el primer criterio del orden"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T261
nombre: Desbloquear a más paquetes decide el orden entre iguales en prioridad
cubre: ["E-06", "b.12 paso 5 b", "grado de salida en el grafo depende_de"]
dado:
  - "el grafo del criterio b es la declaración depende_de que escribe la planificación"
  - "sólo cuentan los dependientes vivos: liberar a un paquete cancelado no libera a nadie"
cuando:
  - "se monta la cola en contra del que desbloquea: entra el último y su identificador ordena el último"
  - "y después se cancelan sus dos dependientes"
entonces:
  - "el que desbloquea a dos encabeza la cola pese a perder en antigüedad y en identificador"
  - "cancelados los dependientes su grado cae a cero y el turno vuelve al otro"
falla_si:
  - "el grado de salida deja de contar y la cola se para detrás de lo que no libera nada"
  - "un dependiente cancelado sigue sumando grado"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T262
nombre: La antigüedad de espera saca de la cola al que lleva más esperando, sin tocar su prioridad
cubre: ["E-06", "b.12 paso 5 c", "b.12 DSP informa de la inanición y no cambia la prioridad"]
dado:
  - "b.12 prohíbe expresamente que el sistema eleve prioridades para prevenir la inanición"
  - "la prevención tiene que salir del criterio de antigüedad, que es para lo que está"
cuando:
  - "un paquete de prioridad de fondo cuyo identificador ordena el último espera cinco rondas"
  - "y en cada ronda entra un competidor nuevo de su misma prioridad con identificador anterior"
entonces:
  - "el veterano encabeza la cola en las cinco rondas, por antigüedad y no por prioridad"
  - "se despacha con un proceso real y termina completado"
  - "su prioridad durable al final es exactamente la misma que al principio"
falla_si:
  - "el veterano queda detrás de cada paquete nuevo y no llega a ejecutarse nunca"
  - "alguien le sube la prioridad para sacarlo de la cola"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T263
nombre: El identificador hace TOTAL el orden de selección y lo deja determinista
cubre: ["E-06", "b.12 paso 5 d", "gate:despacho-coherente", "I-g3"]
dado:
  - "gate:despacho-coherente exige que el mismo estado produzca la misma selección con desempate por identificador"
  - "los tres primeros criterios pueden empatar y el cuarto no empata nunca"
cuando:
  - "se comparan dos entradas empatadas en prioridad, grado de salida y antigüedad"
  - "y se lee dos veces seguidas la cola real de un estado durable"
entonces:
  - "las dos claves de orden son distintas y el desempate es el identificador ascendente"
  - "las dos lecturas de la cola son idénticas byte a byte"
  - "la cola coincide con la ordenación por la clave, y todas sus claves son distintas"
falla_si:
  - "dos entradas producen la misma clave y el orden queda a merced de la estabilidad del sort"
  - "dos lecturas del mismo estado devuelven órdenes distintos"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T264
nombre: Las postergaciones se cuentan pasada a pasada y viven en el estado durable
cubre: ["E-06", "b.12 detección de inanición", "campo postergaciones"]
dado:
  - "b.12 obliga a mantener y mostrar cuántas veces fue postergado cada paquete listo no despachado"
  - "el contador vive en el objeto durable del paquete, no en la memoria del planificador"
cuando:
  - "se selecciona tres veces con cabida para uno y una cuarta con cabida para dos"
entonces:
  - "los dos que esperan acumulan tres postergaciones y el que se llevó el turno ninguna"
  - "con cabida para dos sólo el tercero suma una más"
  - "el recuento se lee del paquete escrito y se publica en la entrada elegible"
falla_si:
  - "el contador no sube al postergar"
  - "el que se lleva el turno acumula postergaciones"
  - "el recuento vive en memoria y no en el estado durable"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T265
nombre: adelantado_por dice quién le pasó por delante, sin repetirse y en orden
cubre: ["E-06", "b.12 detección de inanición", "campo adelantado_por", "b.12 paso 7"]
dado:
  - "sin este campo la inanición se ve pero no se explica, y el paso 7 obliga a explicar"
cuando:
  - "se selecciona tres veces con dos adelantamientos distintos y una repetición"
entonces:
  - "el postergado acumula los dos que le adelantaron, en orden y sin duplicados"
  - "el que se llevó el turno no acumula a nadie"
falla_si:
  - "el campo queda vacío mientras hay paquetes adelantándose"
  - "el mismo adelantamiento se cuenta dos veces, o el orden depende de la ejecución"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T266
nombre: El impedimento nombra el criterio que de verdad decidió, y la vista lo muestra
cubre: ["E-06", "b.12 detección de inanición", "campo impedimento", "b.12 paso 7", "§7.5 vistas derivadas"]
dado:
  - "b.12 paso 7 dice que un dispatcher que elige sin explicar es una caja negra"
  - "el motivo se deriva comparando criterio a criterio y parando en el primero que decide"
cuando:
  - "se posterga un paquete por prioridad sobre un estado real"
  - "y se derivan los motivos de los otros tres criterios sobre la función que los decide"
entonces:
  - "el impedimento durable nombra la prioridad declarada"
  - "los cuatro criterios producen cuatro textos distintos, y el elegido no tiene impedimento"
  - "la vista derivada del §7.5 publica los cuatro campos de inanición de cada paquete que espera"
falla_si:
  - "dos criterios distintos producen el mismo motivo y desde fuera son indistinguibles"
  - "los contadores se mantienen y nadie los muestra"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T267
nombre: La antigüedad de espera se mide con el reloj lógico y nunca con la hora de pared
cubre: ["E-06", "b.12 campo tiempo_listo", "a.9 determinismo", "I-g3"]
dado:
  - "a.9 prohíbe la hora de pared en el estado canónico y registro_pruebas lo repite"
  - "el motor publica un contador monótono por revisión, que es el orden real de los sucesos"
cuando:
  - "se da de alta un paquete, se lee su objeto durable y se hace avanzar el estado"
  - "y se pausa y se reanuda otro paquete"
entonces:
  - "el instante en que entró en listo es un entero no mayor que la revisión vigente"
  - "el objeto durable no contiene ninguna fecha ni ninguna marca de tiempo real"
  - "la antigüedad no cambia si el estado no avanza y crece cuando avanza"
  - "volver a listo reinicia la espera, porque es una espera nueva"
falla_si:
  - "aparece una hora de pared en el paquete durable"
  - "la antigüedad no avanza con las revisiones"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T268
nombre: Los contadores de inanición sobreviven a la caída y a dos planificadores concurrentes
cubre: ["E-06", "b.12 detección de inanición", "§4.2 reanudación", "concurrencia entre instancias"]
dado:
  - "un contador en memoria se borra con el proceso, y es tras un reinicio cuando más falta hace"
  - "dos planificadores pueden trabajar sobre el mismo estado durable"
cuando:
  - "se postergan dos veces, se cierra el runtime y OTRO proceso distinto lee y posterga una tercera"
  - "y después dos instancias abiertas a la vez seleccionan una vez cada una"
entonces:
  - "el proceso nuevo ve las dos postergaciones que contó el anterior y continúa la cuenta"
  - "adelantado_por sobrevive a la reanudación"
  - "las dos instancias ven exactamente la misma cola"
  - "dos pasadas concurrentes dejan exactamente dos postergaciones más, ni una perdida ni una doble"
  - "el paquete resultante sigue siendo válido para el vocabulario cerrado del §3"
falla_si:
  - "los contadores se pierden al reiniciar"
  - "dos planificadores ven colas distintas o corrompen la cuenta"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T269
nombre: Cada sabotaje de un criterio o de un campo pone roja una prueba distinta
cubre: ["E-01", "E-06", "b.12 paso 5", "b.12 detección de inanición", "C4 cuántos agentes por rol"]
dado:
  - "una regla que se puede borrar entera sin que ninguna prueba parpadee no está probada, está descrita"
  - "el control positivo va primero: la copia sin sabotear tiene que pasar en verde"
cuando:
  - "se sabotean uno a uno, en una copia del árbol y en procesos reales, los cuatro criterios de orden, los cuatro campos de inanición y tres piezas de la cardinalidad de C4"
entonces:
  - "las once pruebas señaladas son distintas entre sí"
  - "la copia intacta pasa en verde cada una de las once, y ejecuta exactamente una prueba"
  - "cada sabotaje pone en rojo su prueba, y restaurar el fichero la devuelve a verde"
falla_si:
  - "algún sabotaje deja su prueba en verde: ese criterio o ese campo es decorativo"
  - "dos sabotajes apuntan a la misma prueba y uno de los dos no demuestra nada propio"
  - "la copia restaurada no vuelve a verde, con lo que el rojo no probaba el sabotaje"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```
