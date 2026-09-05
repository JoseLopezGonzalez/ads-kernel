# T400–T419 — la prioridad es INMUTABLE, la contención es DETERMINISTA, y la deuda de los escenarios tiene nombre

**Qué cierran.** Tres defectos del cierre final de `F6`, los tres reproducidos ANTES de
escribir una línea de remedio y los tres con su reproducción publicada aquí:

`G-04` · **la prohibición de `b.12` era prosa**. El contrato es terminante —«DSP informa de
la inanición. No cambia la prioridad. Nunca»— y el árbol lo cita LITERAL en tres sedes; sumar
diez a la prioridad en el `construir` de la transición `runtime.seleccion.postergada` pasaba
**doce baterías en verde**, con la línea ejecutándose dieciséis veces y mutando el estado
durable `50 → 60 → 70`. Los otros ocho sabotajes del mismo eje —los cuatro criterios de orden
del paso 5 y los cuatro campos de inanición— ponen roja una prueba distinta cada uno. La única
afirmación ABSOLUTA del contrato era la única sin red.

`G-08` · **la contención se medía tras una espera arbitraria**. La tarea generacional decía
`sleep 0.6` y después `echo listo`, y en ese instante se capturaban las cuatro generaciones.
Bajo carga, el bisnieto puede no existir todavía: la captura sale vacía y `T216` cae. Cae al
lado seguro —rojo, no verde—, pero **no es determinista**, y la línea base de `F6` declara
determinismo byte a byte.

`D-02` · **doce escenarios sólo pueden ascender si otro reescribe la salida de su ejecutor**.
Su evidencia existe, tiene cabecera de procedencia, terminó con código 0 y la produjo el
ejecutable que el escenario declara — y **no los nombra**. El aparato de contraste de
`registro_pruebas.py` ya publicaba la cifra; lo que faltaba era la prueba que impide que la
clase vuelva a crecer.

**Sedes normativas**, citadas en texto plano porque no viajan al proyecto instalado:
`docs/rediseno/b-RECORRIDO-APROBADA.md`, sección «b.12 — Selección del siguiente trabajo, e
inanición»; `kernel/operativo/runtime/CONTRATO-RUNTIME-Y-DISPATCHER.md` §3, §4.1 y §4.2;
`kernel/operativo/runtime/CONTRATO-CONTENCION.md`; `kernel/operativo/pruebas/REGISTRO.md`,
regla dura «ninguna prueba sube de estado por argumento».

---

## La reproducción de `G-04`, literal

```text
$ (sobre una COPIA) kernel/operativo/runtime/runtime/dispatcher.py
  bloque `construir(revision)` de `_anotar_postergacion`
                  nuevo = dict(actual)
  +               nuevo["prioridad"] = int(actual["prioridad"]) + 10
                  nuevo["seleccion"] = normalizar_seleccion(seleccion, ruta=actual["id"])

  test_cardinalidad_y_seleccion  EXIT=0  Ran 20 tests  OK
  test_runtime                   EXIT=0  Ran 54 tests  OK
  test_ciclo                     EXIT=0  Ran 52 tests  OK
  test_continua                  EXIT=0  Ran 24 tests  OK
  test_agentes                   EXIT=0  Ran 15 tests  OK
  test_arboles                   EXIT=0  Ran 38 tests  OK
  test_sesion_nueva              EXIT=0  Ran 27 tests  OK
  test_estado_durable            EXIT=0  Ran 100 tests OK
  escenario_extremo_a_extremo    EXIT=0
  escenario_e2e_runtime          EXIT=0
  escenario_e2e_f6               EXIT=0
```

**Dónde está la red ahora, y por qué ahí.** No en `_anotar_postergacion`: una comprobación
dentro de un `construir` la esquiva quien escriba otra transición. La invariante vive en
`runtime/estado_util.py`, que es **la puerta por la que toda transición del runtime pasa antes
de confirmarse** —lo declaran el propio módulo y el docstring de `dispatcher.py`, y `ciclo/`
escribe por ella sin abrir almacén propio—, y se acompaña de `AlmacenVigilado`, que envuelve
el almacén que `Runtime.abrir()` abre para que la propiedad pública `almacen` no sea la puerta
trasera de la misma prohibición. La invariante no es «no subir la prioridad al postergar»: es
que **la prioridad de un paquete que ya existe no cambia en ninguna transición del runtime**.
La prioridad nace en el alta y ahí termina; la inanición se INFORMA en `tiempo_listo`,
`postergaciones`, `adelantado_por` e `impedimento`, que siguen siendo escribibles.

> **El sabotaje exacto de `R1-H02` está en el censo de `T269`** y además tiene prueba propia,
> `T409`, que lo aplica sobre una COPIA real del kernel en un proceso real y exige que caiga
> **por la prohibición semántica**: la salida tiene que nombrar `PRIORIDAD_INMUTABLE` y citar
> `b.12`. Un rojo por la huella del kernel saltaría con cualquier edición legítima y no
> probaría nada de `b.12`.

## La reproducción de `G-08`, literal

Banco que sustituye SÓLO la constante de espera y deja el resto del código intacto, sobre un
anfitrión de veinte núcleos, con carga real —quemadores de CPU más tormentas de `fork`—:

```text
$ (en reposo)      sleep=0.6  ·  0/25 capturas INCOMPLETAS
$ (bajo carga)     sleep=0.6  ·  4/15 capturas INCOMPLETAS · {nieto: 3, bisnieto: 4}
$ (bajo carga)     sleep=0.6  ·  5/10 capturas INCOMPLETAS · {nieto: 2, bisnieto: 5}
$ (bajo carga, con el PROTOCOLO)
                              ·  0/10 capturas INCOMPLETAS · 0 sin-preparar
                              ·  0/20 capturas INCOMPLETAS · 0 sin-preparar
```

**El remedio no es una espera más larga.** Una constante mayor mueve la frontera y no la
quita. En su lugar hay un protocolo de preparación con dos canales: cada generación se anuncia
por `stdout` —el descriptor que `setsid` no cierra y que el ejecutor ya lee, de modo que el
anuncio llega desde dentro de cualquier backend, contenedor incluido— y deja además su testigo
en un directorio que las cuatro comparten; la RAÍZ no publica `listo` hasta haber **observado**
los tres testigos. El `killpg` ocurre después de esa línea y no antes. Si la raíz agota sus
sondeos publica `sin-preparar` con la lista de testigos que sí vio, y el veredicto es
`NUNCA CREADO`, que es un fallo **distinto** de «sobrevivió a la contención».

> **La repetición no sustituye al protocolo.** `T414` repite bajo carga generada a propósito y
> con los dos niveles de aislamiento, y eso MIDE que la intermitencia ya no aparece. Lo que
> GARANTIZA que no puede aparecer es `T411`: que el `killpg` no ocurre hasta que las cuatro
> generaciones han confirmado.

## `D-02`, medido

Doce escenarios, no nueve, y con nombre. Diez dependen de **cuatro baterías ajenas** y dos de
un validador:

```text
T162 T163 T164 T165 T166 T167   tooling/tests/test_workspace.py
T180                            kernel/operativo/runtime/pruebas/escenario_extremo_a_extremo.py
T193                            kernel/operativo/runtime/pruebas/escenario_e2e_runtime.py
T225 T301                       kernel/operativo/runtime/pruebas/escenario_e2e_f6.py
T168 T181                       kernel/operativo/validadores/comprobar_arranque.py
```

**Las baterías OBSERVAN; no son el mecanismo.** Lo que cambia el estado de un escenario es que
su ejecutor publique un **veredicto nominal** —`Tnnn SUPERADA` o `Tnnn · … ok`— en una
evidencia con cabecera de procedencia, código 0 y resumen de cierre. Los doce se ejecutaban y
terminaban bien; lo que no constaba era el veredicto **de cada uno**. Los doce caían fuera de
la zona de esta autoría y su remedio fue como PETICIÓN; lo que se entregó aquí fue el cliquet
que impide que la clase crezca —`T415`—, la ficha accionable de cada uno —`T416`— y el control
sano que demuestra que el mecanismo del ascenso existe y funciona para los demás —`T417`—.

> **`D-02` está CERRADA, y la cerró este cliquet.** El coordinador aplicó el remedio a los
> doce ejecutores, y en cuanto lo hizo `T415` y `T416` se pusieron **rojas** diciendo,
> escenario a escenario, «*su ejecutor YA sabe publicar su veredicto nominal: este escenario
> tiene que salir del censo*». `CENSO_D02` pasa de doce entradas a **cero**. No se borra con
> sus pruebas: vacío, `T415` sigue midiendo la mitad que importa ahora —que no aparezca
> ninguno nuevo— y `T417` sigue comprobando entera la afirmación de la que todo depende.
> El remedio, por ejecutor: la primera línea del docstring en `test_workspace.py` (`T162`–
> `T167`); un `ResultadoRepartido` en `comprobar_arranque.py` —un montaje, tres veredictos—
> para `T168` y `T181`; y una línea propia al cierre de cada escenario extremo a extremo,
> calculada aparte para que una excepción por el medio deje el veredicto en **rojo** y no
> sin emitir.

---

```yaml ads:escenario
id: T400
nombre: La prioridad declarada sobrevive intacta a una postergación
cubre: ["G-04", "R1-H02", "b.12 paso 5", "b.12 inanición"]
dado:
  - "b.12 dice DSP informa de la inanición y no cambia la prioridad nunca"
  - "un paquete de prioridad 50 y otro de prioridad 90 compiten por el mismo turno"
cuando:
  - "se ejecuta una pasada de seleccionar_siguiente con cabida 1"
entonces:
  - "la prioridad durable del postergado es exactamente la que declaró el Owner al darlo de alta"
  - "las postergaciones del postergado suben a 1 y adelantado_por nombra al que se llevó el turno"
falla_si:
  - "la transición de postergación mueve la prioridad del paquete postergado"
  - "la prohibición se cumple porque la postergación no anota nada"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T401
nombre: La prioridad sobrevive a muchas postergaciones seguidas y no deriva
cubre: ["G-04", "R1-H02", "b.12 inanición"]
dado:
  - "la mutación reproducida por el revisor 1 era acumulativa y medía 50 a 60 a 70"
  - "tres paquetes en espera con dos prioridades declaradas distintas"
cuando:
  - "se ejecutan doce pasadas de selección sobre la misma cola"
entonces:
  - "la prioridad durable de cada uno de los tres es la del alta, exacta"
  - "las doce postergaciones se contaron, de modo que las doce pasadas ocurrieron"
falla_si:
  - "una deriva lenta cambia la prioridad después de varias pasadas"
  - "las pasadas no llegan a postergar y la prueba mide una cola vacía"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T402
nombre: El veterano adelanta por antigüedad y ninguna prioridad se altera
cubre: ["G-04", "b.12 paso 5 c", "prevención de inanición"]
dado:
  - "b.12 previene la inanición con el criterio c y no subiendo la prioridad"
  - "un paquete veterano y cuatro competidores nuevos, todos con la misma prioridad declarada"
cuando:
  - "entra un competidor nuevo en cada ronda y se ejecuta una pasada de selección"
entonces:
  - "el veterano acaba a la cabeza de la cola por antigüedad de espera"
  - "la prioridad durable de los cinco es la declarada, sin excepción"
falla_si:
  - "el veterano sale de la cola porque alguien le subió la prioridad"
  - "el veterano no adelanta, con lo que la prueba no distingue las dos causas"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T403
nombre: La prioridad sobrevive a la caída del runtime y a su reanudación
cubre: ["G-04", "b.12 inanición", "recuperación del §4.2"]
dado:
  - "abrir el runtime recupera el estado antes de despachar, y ese camino también escribe"
  - "un paquete postergado con su cuenta ya anotada en el estado durable"
cuando:
  - "el runtime se cierra y otra instancia se abre sobre el mismo control repo"
entonces:
  - "la prioridad durable sigue siendo la declarada tras la reanudación"
  - "la postergación anterior sobrevivió, de modo que la reanudación es real"
  - "una pasada más tras reabrir tampoco la mueve"
falla_si:
  - "el barrido de reanudación mueve la prioridad de un paquete"
  - "los contadores se pierden al reiniciar y la prueba no mide ninguna reanudación"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T404
nombre: Dos planificadores compitiendo tampoco mueven la prioridad de nadie
cubre: ["G-04", "g.6", "b.12 inanición", "comparación e intercambio"]
dado:
  - "el motor aplica cada transición con comparación e intercambio sobre la revisión base"
  - "la reconstrucción por revisión obsoleta vuelve a llamar a construir en cada vuelta"
cuando:
  - "dos instancias reales alternan cuatro pasadas de selección sobre el mismo almacén"
entonces:
  - "la invariante se reevalúa contra el estado releído en cada vuelta"
  - "las prioridades durables de los dos postergados son las declaradas"
  - "las postergaciones acumuladas demuestran que la carrera ocurrió"
falla_si:
  - "la carrera entre dos DSP deja pasar una escritura que mueve la prioridad"
  - "la comprobación se hace sobre bytes caducados en vez de sobre la revisión releída"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T405
nombre: La edición directa de la prioridad de 50 a 60 no se puede confirmar
cubre: ["G-04", "b.12", "invariante en la puerta"]
dado:
  - "la propiedad almacen del runtime es pública porque la verdad vive en el estado"
  - "con ella se puede construir una Transicion a mano y aplicarla sin pasar por el dispatcher"
cuando:
  - "se construye y se aplica una transición que escribe el paquete con prioridad 60"
entonces:
  - "se levanta PrioridadInmutable con el campo, los dos valores y la cita de b.12"
  - "el estado canónico no se ha tocado: la prioridad sigue en 50"
  - "la misma edición directa que no toca la prioridad sí se confirma"
falla_si:
  - "la escritura a mano confirma un cambio de prioridad"
  - "el almacén vigilado rechaza también las escrituras legítimas"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T406
nombre: La secuencia 50 a 60 a 70 se corta en el primer escalón
cubre: ["G-04", "R1-H02", "b.12"]
dado:
  - "la reproducción del revisor 1 publicó la mutación durable 50 a 60 a 70"
  - "una invariante que sólo viera la deriva acumulada dejaría escrito el primer valor falso"
cuando:
  - "se intentan los dos escalones de la secuencia, uno tras otro"
entonces:
  - "los dos intentos se rechazan y el valor anterior sigue siendo 50 en los dos"
  - "el estado durable nunca llega a contener 60"
falla_si:
  - "el primer escalón se confirma y sólo se detecta el segundo"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T407
nombre: La mutación escondida dentro de otra transición tampoco se confirma
cubre: ["G-04", "b.12", "atomicidad de la transición"]
dado:
  - "una comprobación dentro de un construir la esquiva quien escriba otra transición"
  - "la mutación puede viajar dentro de una transición que hace además un cambio legítimo"
cuando:
  - "se aplica una transición de tipo runtime.paquete.despachado que cambia max_intentos y la prioridad"
entonces:
  - "se rechaza entera y el contexto del error nombra el tipo de transición"
  - "el cambio legítimo tampoco entra: una transición es atómica o no es una transición"
falla_si:
  - "una transición de otra clase puede mover la prioridad"
  - "la transición se aplica a medias, entrando el cambio legítimo y quedando fuera el prohibido"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T408
nombre: Cambiar la prioridad y restaurarla después no lava la mutación
cubre: ["G-04", "b.12", "g.2 diario canónico"]
dado:
  - "una prueba escrita sobre el resultado final no vería un viaje de ida y vuelta"
  - "la invariante compara contra el estado vigente en cada transición"
cuando:
  - "se intenta la ida, subir la prioridad, con la intención de restaurarla después"
entonces:
  - "la ida se rechaza y la vuelta no llega a poder intentarse"
  - "la revisión del almacén no avanza: nada se confirmó"
  - "el diario canónico no registra la transición de ida"
falla_si:
  - "el par de transiciones deja el estado final igual y la cola reordenada por el camino"
  - "la revisión avanza aunque la transición se rechazara"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T409
nombre: El sabotaje que pasaba doce baterías cae ahora por la prohibición semántica
cubre: ["G-04", "R1-H02", "b.12", "T269"]
dado:
  - "el sabotaje exacto es sumar diez a la prioridad en el construir de runtime.seleccion.postergada"
  - "con él, doce baterías salían con EXIT 0 y la prioridad durable mutaba 50 a 60 a 70"
cuando:
  - "se copia el kernel entero, se aplica el sabotaje y se ejecuta la prueba en un proceso real"
entonces:
  - "la copia sin sabotear pasa en verde, que es el control positivo"
  - "la copia saboteada falla y su salida nombra PRIORIDAD_INMUTABLE"
  - "la salida cita la norma de b.12 que se violó"
falla_si:
  - "el sabotaje sigue pasando en verde"
  - "cae por la huella del kernel y no por la semántica de b.12"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```

```yaml ads:escenario
id: T410
nombre: Las cuatro generaciones confirman que existen antes de que se mate nada
cubre: ["G-08", "FD-5", "T216", "determinismo byte a byte"]
dado:
  - "la captura de las generaciones ocurría tras una espera fija de seis décimas"
  - "bajo carga el bisnieto puede no existir todavía en ese instante"
cuando:
  - "cada generación se anuncia por stdout y deja su testigo, y la raíz espera a observar los tres"
entonces:
  - "los cuatro anuncios aparecen en la salida antes de la línea listo"
  - "la cancelación se dispara con la línea listo y no antes"
  - "las cuatro generaciones tienen PID capturado del anfitrión"
falla_si:
  - "la raíz publica listo sin haber observado los tres testigos"
  - "una generación se anuncia después de listo"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_contencion.py
estado: prueba-superada
evidencia: evidencia/contencion-salida.txt
```

```yaml ads:escenario
id: T411
nombre: Nunca creado y muerto por contención son veredictos distintos
cubre: ["G-08", "FD-5", "T215", "T216"]
dado:
  - "un descendiente que no llegó a existir producía el mismo rojo que uno que sobrevivió"
  - "el canal de anuncios sobrevive a la muerte del proceso que lo emitió"
cuando:
  - "se corre la tarea con una generación amputada y después la tarea entera"
entonces:
  - "con la generación amputada la raíz publica sin-preparar y el veredicto es NUNCA CREADO, nombrando al ausente"
  - "con la tarea entera las cuatro se anuncian y la raíz muere por killpg sin que el protocolo se queje"
  - "el texto del veredicto de nunca creado no menciona supervivencia"
falla_si:
  - "el protocolo no detecta a la generación amputada"
  - "los dos veredictos son indistinguibles desde fuera"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_contencion.py
estado: prueba-superada
evidencia: evidencia/contencion-salida.txt
```

```yaml ads:escenario
id: T412
nombre: La preparación es una condición observada y no una espera arbitraria
cubre: ["G-08", "FD-5", "determinismo byte a byte"]
dado:
  - "cambiar la constante por otra mayor mueve la frontera y no la quita"
  - "la tarea generacional ya no contiene ninguna espera fija antes de anunciar listo"
cuando:
  - "se inspecciona el texto de la tarea y se corre una variante con el bisnieto retardado cinco segundos"
entonces:
  - "el texto de la tarea no lleva la espera fija y sí la conjunción de los tres testigos"
  - "con cinco segundos de retardo, ocho veces la constante anterior, la captura sigue completa"
  - "la raíz publica cuántos sondeos necesitó, y fueron más de uno"
falla_si:
  - "la espera fija sigue en la tarea"
  - "una generación lenta rompe la captura"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_contencion.py
estado: prueba-superada
evidencia: evidencia/contencion-salida.txt
```

```yaml ads:escenario
id: T413
nombre: La contención se repite bajo carga sin intermitencia, con el backend débil y con el fuerte
cubre: ["G-08", "E-18", "FD-5", "determinismo byte a byte"]
dado:
  - "la intermitencia se midió bajo carga y en reposo daba cero de quince"
  - "repetir en reposo no demuestra ausencia de intermitencia"
cuando:
  - "se generan quemadores de CPU reales y se repiten ocho pasadas por cada nivel de aislamiento disponible"
entonces:
  - "todas las pasadas confirman las cuatro generaciones antes de matar"
  - "el protocolo vale igual para el nivel grupo-de-procesos y para el nivel arbol-de-procesos"
falla_si:
  - "alguna pasada bajo carga deja una generación sin capturar"
  - "la carga no se genera y la prueba mide en reposo"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_contencion.py
estado: prueba-superada
evidencia: evidencia/contencion-salida.txt
```

```yaml ads:escenario
id: T414
nombre: setsid se conserva y se mide generación a generación por su identificador de sesión
cubre: ["G-08", "FD-5", "T215", "T216"]
dado:
  - "T215 y T216 sólo distinguen los dos niveles si las generaciones se salen del grupo"
  - "comparar listas de PID aproximaba lo que setsid cambia de verdad"
cuando:
  - "se lee el identificador de sesión de cada generación en el mismo instante de la captura"
entonces:
  - "las cuatro generaciones tienen identificadores de sesión distintos entre sí"
  - "la lectura ocurre antes de matar, cuando /proc todavía existe"
falla_si:
  - "dos generaciones comparten sesión, con lo que la tarea dejó de hacer setsid"
  - "la sesión se lee después de la muerte y no se puede leer"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_contencion.py
estado: prueba-superada
evidencia: evidencia/contencion-salida.txt
```

```yaml ads:escenario
id: T415
nombre: Ningún escenario nuevo queda atado a que otro reescriba la salida de su ejecutor
cubre: ["D-02", "H-02", "ADJ-G2", "REGISTRO.md regla dura"]
dado:
  - "el censo de la clase esta VACIO: los doce que lo formaban se cerraron y se tacharon"
  - "el mecanismo del ascenso es el veredicto nominal, no la ejecución de la batería"
cuando:
  - "se deriva del árbol la clase entera y se confronta con el censo escrito"
entonces:
  - "no aparece ningún escenario nuevo en la clase"
  - "ninguno de los del censo ha dejado de estar atado sin que el censo se actualice"
falla_si:
  - "un escenario nuevo entra en la clase y nadie se entera"
  - "el censo se queda rancio porque uno se cerró y sigue listado"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_runtime.py
estado: prueba-superada
evidencia: evidencia/runtime-salida.txt
```

```yaml ads:escenario
id: T416
nombre: Cada escenario atado declara qué ejecutable tendría que nombrarlo
cubre: ["D-02", "H-02"]
dado:
  - "una deuda con cifra y sin nombre no es accionable"
  - "D-02 pide ejecutor, evidencia y condición de ascenso para cada uno"
  - "cerrada D-02 el censo esta vacio, y recorrerlo entero sigue siendo la comprobacion"
cuando:
  - "se recorre el censo y se confronta cada ficha contra el árbol"
entonces:
  - "el ejecutable que el censo nombra es el que el árbol dice, y existe"
  - "la evidencia que hoy no lo nombra existe en el árbol"
  - "ninguno declara prueba-superada sobre una evidencia que no lo nombra"
falla_si:
  - "el censo nombra un ejecutable que no es el del árbol"
  - "uno de los atados sube de estado por argumento"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_runtime.py
estado: prueba-superada
evidencia: evidencia/runtime-salida.txt
```

```yaml ads:escenario
id: T417
nombre: El ascenso lo da el veredicto nominal y no el hecho de ejecutar una batería
cubre: ["D-02", "H-02", "ADJ-G2"]
dado:
  - "si el mecanismo del ascenso no existiera, la clase de D-02 sería todo el corpus"
  - "las baterías observan y publican el veredicto; lo que cambia el estado es ese veredicto"
cuando:
  - "se recorren todos los escenarios que declaran prueba-superada"
entonces:
  - "cada uno está nombrado por su evidencia con un veredicto bueno"
  - "cada evidencia publica su resumen de cierre y no está truncada"
  - "hay más de cien escenarios en ese estado, de modo que el mecanismo funciona"
falla_si:
  - "un escenario declara prueba-superada sin que su evidencia lo nombre"
  - "las expresiones de veredicto caducan y la prueba deja de ver los ascensos"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_runtime.py
estado: prueba-superada
evidencia: evidencia/runtime-salida.txt
```

```yaml ads:escenario
id: T419
nombre: La norma de b.12 se cita igual en las cuatro sedes y una de ellas la ejecuta
cubre: ["G-04", "b.12", "R1-H02"]
dado:
  - "el gate dio por citada literalmente la norma en tres sedes del árbol"
  - "una de esas tres, runtime/politica.py, no la llevaba escrita"
cuando:
  - "se confrontan las tres sedes que la citan con la constante que la ejecuta en la puerta"
entonces:
  - "ciclo/planificacion.py, runtime/vistas.py y runtime/politica.py llevan la cita literal"
  - "estado_util.CITA_DE_B12 dice exactamente lo mismo y es el texto que viaja en el error"
  - "el campo prioridad está declarado entre los inmutables del paquete"
falla_si:
  - "una de las cuatro sedes deriva y aparecen dos normas"
  - "la constante que ejecuta la norma deja de coincidir con la citada"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
estado: prueba-superada
evidencia: evidencia/cardinalidad-salida.txt
```
