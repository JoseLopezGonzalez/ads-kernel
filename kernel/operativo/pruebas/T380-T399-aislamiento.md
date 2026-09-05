# T380–T399 — el aislamiento de arranque: `G-03` y `D-01`

**Qué cierran.** Los dos defectos que el gate del 2026-09-05 dejó registrados sobre el mismo
mecanismo: `G-03` —`H-1` del revisor 2—, que la purga de `sys.path` que todo el aparato lleva
desde `E-10` **llega tarde por construcción**, porque `site.py` importa `sitecustomize`
mientras el intérprete arranca y antes de que la primera sentencia de cualquier módulo exista;
y `D-01` —`HALLAZGO 3` del revisor 3—, que ese mismo mecanismo **no alcanzaba al canal que
PRODUCE la evidencia**: veintiuna baterías sin el prólogo, eximidas del inventario por vivir en
`runtime/pruebas/`, y un runner que lanzaba a sus hijos con `subprocess.run` **sin `env=`**.

**El hecho, reproducido antes de corregir**, con la orden y la salida literales:

```console
$ cat veneno/sitecustomize.py
  import hashlib; hashlib.sha256 = lambda *a, **k: _Falso()   # digest 0000…, y deja TESTIGO
$ PYTHONPATH=veneno python3.12 <copia de huella.py SIN la guarda> --raiz <repo>
  0000000000000000                     ← la huella FORJADA sobre el árbol real
  testigo en disco: sitecustomize      ← el gancho LLEGÓ a ejecutarse
$ PYTHONPATH=veneno python3.12 kernel/operativo/validadores/huella.py
  078074dae8f687e8                     ← el valor SANO
  testigo en disco: sitecustomize      ← llegó al proceso LANZADOR, no al que trabaja
$ PYTHONPATH=veneno python3.12 -I -S -E kernel/operativo/validadores/huella.py
  078074dae8f687e8                     ← el valor SANO
  testigo en disco: NINGUNO            ← el gancho NO LLEGÓ a existir
```

**Las dos mitades del testigo son la prueba.** Que el gancho APAREZCA sobre la versión sin
guarda —si no apareciera, el veneno no funcionaría y estas pruebas no medirían nada— y que NO
APAREZCA por la vía oficial. Mirar sólo el valor publicado no bastaría: un valor correcto es
compatible con «el gancho corrió y no le tocó el turno».

**Lo que se corrige no es una lista de ficheros.** El remedio es de CLASE: la guarda se exige
a **todo punto ejecutable del inventario derivado del árbol** —el mismo inventario mecánico de
`T330`, que no conoce zonas sino ficheros—, y la exención por domicilio `motivo: "bateria"`
**se ha retirado**: eximir una batería por vivir en `pruebas/` es la lista escrita a mano que
`ADJ-B2` prohibió, sólo que escrita por directorios. El inventario pasa de **35 puntos
ejecutables y 110 exclusiones** a **56 y 89**, sobre los mismos 145 ficheros `.py`, y **nada
queda sin clasificar**.

**Y la exención por propietario se ha CERRADO, no ha caducado.** Los cuatro ejecutables de
`docs/evolucion/verificacion/` quedaron fuera en la primera pasada porque `G-01`, `G-02` y
`G-07` estaban abiertos sobre esos mismos ficheros, y dos pasadas simultáneas sobre el mismo
texto se pisan. Se declararon con motivo, con propietario y con cliquet —la cifra era **4** y
no podía subir—, y con una caducidad que ponía `T380` en rojo el día que la zona dejara de
tener puntos sin guarda. Cerrados `G-01`, `G-02` y `G-07`, el coordinador les aplicó el
mecanismo **byte a byte idéntico** al de los otros 52 y retiró la declaración. Hoy son
**56 de 56**, y los puntos sin guarda admitidos son **CERO**.

**De `D-01` se hacen las DOS cosas que el revisor adjudicó**, con sus palabras: «o el prólogo
entra en las baterías, o el runner sanea el entorno de sus hijos y lo publica en la cabecera de
cada evidencia. **Lo segundo cierra las 21 de una vez y es más barato; lo primero cierra
también la ejecución suelta**». Una batería se ejecuta a mano mientras se escribe, y ésa no
pasa por el runner; y un runner limpio que lanzara una batería sin guarda dependería de que
nadie la invocara de otro modo.

**Lo que estas pruebas NO dicen.** Ninguna afirma que el aislamiento sea inviolable. Dicen algo
más estrecho y comprobable: que el gancho **no llega a ejecutarse** por la vía oficial, que el
punto **falla cerrado** cuando no puede decidir su aislamiento, y que la primitiva con la que
se firma la evidencia **se autocomprueba contra un vector conocido** antes de usarse. Un
atacante con permiso de escritura sobre el árbol o sobre el intérprete no está cubierto por
esto, y eso sigue siendo lo que la instalación y la atestación cubren.

> Los sabotajes de esta tanda se ejercen sobre el CÓDIGO y no caben en el catálogo de
> infracciones documentales: su matriz «sano → VERDE, sabotaje → ROJO por el motivo esperado,
> restaurado → VERDE» se reproduce copiando el repositorio, reintroduciendo el defecto y
> volviendo a ejecutar el escenario que lo mide. Dos de ellos —retirar la guarda de un punto y
> quitarle el `env=` al runner— están además MECANIZADOS en
> [`../validadores/negativos_runtime.py`](../validadores/negativos_runtime.py), que
> [`../validadores/comprobar_negativos.py`](../validadores/comprobar_negativos.py) aplica sobre
> una COPIA temporal del repositorio.

```yaml ads:escenario
id: T380
nombre: La guarda de aislamiento alcanza a TODO punto ejecutable del inventario derivado
cubre: ["G-03", "H-1", "ADJ-B2", "O26 1.8"]
dado:
  - "el inventario se deriva del arbol entero y clasifica los 145 ficheros .py sin dejar ninguno fuera"
  - "no queda ninguna zona exenta, y la cifra de puntos sin guarda admitidos es CERO"
cuando: ["se inventaria el arbol y se mide, fichero a fichero, si el punto exige el aislamiento al entrar"]
entonces:
  - "los 56 puntos ejecutables de las nueve zonas del kernel, tooling y docs llevan la guarda, sin una sola exencion"
  - "ninguna zona queda declarada: la exencion de docs/evolucion/verificacion se cerro y se retiro"
  - "si alguna zona volviera a declararse sin tener puntos sin guarda, la declaracion CADUCA y la prueba lo dice"
falla_si:
  - "un punto ejecutable nuevo entra en cualquier zona sin la guarda, que es como H-03 volvio dos veces"
  - "el numero de puntos sin guarda sube, o aparece una zona sin guarda que nadie declaro"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T381
nombre: El mecanismo de la guarda es identico byte a byte en todos los puntos
cubre: ["G-03", "ADJ-B2", "T330"]
dado:
  - "lo que protege es el MECANISMO, y el recital que va encima es propio de cada sede"
  - "la misma disciplina que T330 ya exige para el mecanismo E-10"
cuando: ["se extrae el mecanismo de cada punto ejecutable y se compara su digest"]
entonces:
  - "hay un unico digest para todos los puntos que llevan la guarda"
  - "un punto que llame a la guarda y no lleve el mecanismo pone la prueba en rojo"
falla_si:
  - "el mecanismo se adapta en una sede, que es como una guarda deja de proteger sin que nadie lo note"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T382
nombre: El sitecustomize LLEGA en la version vulnerable y NO LLEGA por la via oficial
cubre: ["G-03", "H-1", "O26 1.8"]
dado:
  - "un sitecustomize alcanzable desde PYTHONPATH que sustituye hashlib.sha256 y deja un TESTIGO en disco al ejecutarse"
  - "una copia de huella.py a la que se le ha retirado el bloque de la guarda, como control del control"
cuando: ["se ejecutan las tres filas: sin guarda, con guarda a pelo, y por la via oficial con -I -S -E"]
entonces:
  - "sin guarda la huella sale FORJADA y el testigo aparece: el veneno funciona"
  - "con guarda la huella es la SANA y el testigo aparece UNA sola vez, la del proceso lanzador"
  - "por la via oficial la huella es la SANA y el testigo NO APARECE: el gancho no llego a existir"
falla_si:
  - "la version sin guarda no se deja falsificar, con lo que la prueba no estaria midiendo nada"
  - "el gancho se ejecuta por la via oficial, o la huella cambia bajo el veneno"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T383
nombre: El usercustomize tampoco llega, y por eso -S no se retira
cubre: ["G-03", "H-1"]
dado:
  - "usercustomize es el gemelo de sitecustomize y lo importa el mismo site.py durante el arranque"
  - "retirar -S y quedarse con -I -E cerraria una mitad y dejaria la otra abierta"
cuando: ["se repite la matriz de T382 con un usercustomize en vez de un sitecustomize"]
entonces:
  - "la version sin guarda sale forjada y el testigo aparece"
  - "por la via oficial el valor es el sano y el testigo no aparece"
falla_si:
  - "se retira -S de las banderas de aislamiento y el gemelo vuelve a entrar"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T384
nombre: Un hashlib homonimo en el PYTHONPATH no decide la huella
cubre: ["G-03", "E-10", "H-01"]
dado:
  - "el homonimo deja un fichero TESTIGO al importarse, porque una salida se puede tragar y un fichero en disco no"
cuando: ["se ejecuta huella.py con el homonimo en PYTHONPATH y con el cwd dentro del directorio envenenado"]
entonces:
  - "la huella publicada no es la fabricada y el testigo no existe"
falla_si:
  - "se retiran a la vez la purga E-10 y la guarda G-03, con lo que el homonimo vuelve a entrar"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T385
nombre: Un paquete homonimo no entra ni desde el PYTHONPATH ni desde el cwd
cubre: ["G-03", "ADJ-B2", "E-10"]
dado:
  - "el defecto medido fue capacidades publicando {} con codigo 0 sobre la raiz externa"
  - "los paquetes homonimos json, errores, firma y atestacion dejan testigo al importarse"
cuando: ["se ejecuta verificador.py capacidades desde dentro del directorio envenenado y con el en PYTHONPATH"]
entonces:
  - "las nueve condiciones de certificacion se publican enteras y el testigo no existe"
falla_si:
  - "capacidades vuelve a publicar un conjunto encogido, o se importa alguno de los homonimos"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T386
nombre: Un PATH con interprete falso no decide el resultado
cubre: ["G-03", "H-1"]
dado:
  - "el interprete falso es un guion puesto antes en el PATH que reexporta PYTHONPATH hacia el veneno y llama al real"
  - "control del control: sobre la version sin guarda, el mismo guion SI envenena"
cuando: ["se invoca el punto a traves del interprete falso, con el PATH manipulado"]
entonces:
  - "el valor publicado es el sano y el testigo aparece una sola vez, la del lanzador"
  - "la guarda comprueba ademas que sys.executable es un fichero real dentro del prefijo que el mismo declara y que la biblioteca estandar sale de ese prefijo"
falla_si:
  - "se retira -E de las banderas y la variable reexportada vuelve a llegar al proceso que trabaja"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T387
nombre: Un punto del arbol B usa la guarda de B y no la del arbol desde el que se lanza
cubre: ["G-03", "E-10", "T306d"]
dado:
  - "la guarda se busca subiendo desde __file__ y nunca desde el cwd ni desde el PYTHONPATH"
  - "el arbol A trae su propia guarda SABOTEADA, que no comprueba nada y lo grita por stderr"
cuando: ["se ejecuta el punto del arbol B con el cwd dentro del arbol A y con A en PYTHONPATH"]
entonces:
  - "la guarda que corre es la de B y la del arbol A no deja rastro"
  - "el punto publica un resultado normal y sale con cero"
falla_si:
  - "la guarda se busca desde el cwd, con lo que el arbol juzgado aportaria el codigo que lo protege"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T388
nombre: Un modulo importado ANTES de que la guarda tome la palabra se ve y falla cerrado
cubre: ["G-03", "H-1", "O26 1.8"]
dado:
  - "el intruso no se cuela por sys.path: se carga por ruta absoluta, que es la forma que ni -I ni la purga pueden impedir"
  - "cuando la guarda toma la palabra, el intruso ya esta en sys.modules"
cuando: ["se exige el aislamiento en un proceso que ya lleva dentro un modulo de procedencia ajena"]
entonces:
  - "la guarda nombra el modulo colado y su ruta"
  - "el proceso sale con el codigo de procedencia y no llega a ejecutar nada mas"
falla_si:
  - "la guarda deja de mirar sys.modules y lo ya cargado vuelve a ser invisible"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T389
nombre: El lanzamiento directo no evita la guarda, y la marca de reejecucion no se puede forjar
cubre: ["G-03", "H-1"]
dado:
  - "con solo un lanzador oficial, invocar el guion a pelo esquivaria el aislamiento entero"
  - "la marca que corta el bucle vive en la opcion -X y no en el entorno, que cualquiera puede poner y que se hereda"
cuando: ["se invoca el punto a pelo bajo veneno, y se invoca otra vez con la marca puesta en el entorno"]
entonces:
  - "el punto se reejecuta a si mismo aislado y publica el valor sano"
  - "una marca puesta en el entorno no impide el aislamiento ni provoca un fallo cerrado falso"
falla_si:
  - "la guarda se limita a avisar en vez de reejecutar"
  - "la marca vuelve al entorno, donde la hereda cualquier nieto y la puede poner cualquiera"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T390
nombre: El manifiesto de la instalacion no encoge bajo el gancho
cubre: ["G-03", "ADJ-B2", "H-1"]
dado:
  - "el defecto medido fue un manifiesto de TRES bytes sobre cuarenta y un ficheros, con codigo 0"
  - "el gancho sustituye a la vez hashlib.sha256 y json.dumps"
cuando: ["se instala la raiz externa bajo el gancho y se compara con la instalacion limpia"]
entonces:
  - "el manifiesto tiene las mismas filas y los mismos digests que el sano"
  - "el testigo aparece una sola vez, la del proceso lanzador"
falla_si:
  - "el manifiesto vuelve a encoger, o sus digests se fabrican desde el entorno"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T391
nombre: capacidades no publica el vacio bajo el gancho
cubre: ["G-03", "ADJ-B2", "H-1"]
dado:
  - "capacidades es la orden con la que la raiz externa declara que puede certificar"
cuando: ["se ejecuta verificador.py capacidades con el gancho puesto y se compara con la corrida sana"]
entonces:
  - "las nueve condiciones son identicas a las de la corrida sana"
falla_si:
  - "se retira la guarda de verificador.py y el conjunto vuelve a encoger"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T392
nombre: Una instalacion a la que le falta la guarda NO ejecuta
cubre: ["G-03", "ADJ-B2", "O25 2"]
dado:
  - "la raiz externa se instala FUERA del arbol y ahi no existe kernel operativo validadores"
  - "por eso la guarda viaja dentro del paquete instalado y entra en el manifiesto con su digest"
cuando: ["se instala, se comprueba que la guarda esta en el manifiesto, y luego se borra del destino"]
entonces:
  - "con la guarda presente los puntos de la raiz externa funcionan normalmente"
  - "sin ella salen con el codigo de procedencia, lo dicen por stderr y no publican nada"
falla_si:
  - "una instalacion incompleta ejecuta igual, sin poder decidir su aislamiento"
  - "la guarda instalada no entra en el manifiesto y se le puede cambiar sin que nada lo note"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T393
nombre: Una bateria NUEVA ya no queda exenta por su zona
cubre: ["D-01", "HALLAZGO 3", "ADJ-B2"]
dado:
  - "el inventario eximia por domicilio con motivo bateria, y asi veintiun ficheros quedaban fuera"
  - "eximir por vivir en un directorio es la lista escrita a mano de ADJ-B2, escrita por directorios"
cuando: ["se inventaria un arbol sintetico que contiene una bateria nueva sin guarda ni purga"]
entonces:
  - "la bateria nueva aparece como PUNTO EJECUTABLE y no entre los excluidos"
  - "sus senales dicen que no lleva ni la purga ni la guarda, y eso es lo que la pone en rojo"
  - "la clase de exclusion bateria ya no existe en la tabla de motivos"
falla_si:
  - "vuelve la clase bateria a la tabla de motivos de exclusion"
  - "una bateria nueva vuelve a quedar fuera del inventario por su zona"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T394
nombre: El runner sanea el entorno de sus hijos y lo PUBLICA en la cabecera
cubre: ["D-01", "HALLAZGO 3", "E-14"]
dado:
  - "registrar_evidencia.py lanzaba a sus hijos con subprocess.run SIN env, y el veneno del padre llegaba a cada bateria"
  - "el remedio adjudicado incluye, con esas palabras, y lo publica en la cabecera de cada evidencia"
cuando: ["se ejecuta el runner sobre una sonda que publica sus variables y sus banderas, con el gancho puesto en el padre"]
entonces:
  - "el hijo no recibe el PYTHONPATH del padre y arranca con las tres banderas de aislamiento"
  - "la cabecera de la evidencia publica con que banderas y con que variables se lanzo el hijo"
  - "el gancho no llega a ejecutarse en el hijo, y el control del control demuestra que sin el saneamiento SI llegaria"
falla_si:
  - "se quita el env de la llamada, o se deja de escribir la linea de aislamiento en la cabecera"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T395
nombre: El comprobador de evidencia EXIGE la garantia publicada
cubre: ["D-01", "HALLAZGO 3", "E-14"]
dado:
  - "una garantia que no se publica no la puede comprobar nadie, y una que se publica y no se comprueba tampoco vale"
cuando: ["se juzgan cuatro cabeceras fabricadas: la correcta, una sin la linea, una que no nombra las banderas y una que declara haber entregado PYTHONPATH"]
entonces:
  - "la correcta pasa y las tres restantes producen un fallo que nombra la causa exacta"
falla_si:
  - "se retira la comprobacion, con lo que la linea de la cabecera pasaria a ser decorativa"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T396
nombre: La primitiva sustituida EN SITIO se caza con el vector conocido
cubre: ["G-03", "H-1", "O26 1.8"]
dado:
  - "las banderas cierran la via del sitecustomize; la autocomprobacion cubre la mutacion que llegue por cualquier otra"
  - "se comprueba lo que el aparato USA para decidir: el digest con el que firma la huella y la evidencia"
cuando: ["se exige el aislamiento en un proceso aislado en el que hashlib.sha256 ya esta sustituido"]
entonces:
  - "la guarda dice que la primitiva no produce el digest conocido de un vector fijo y sale con el codigo de procedencia"
falla_si:
  - "se retira la autocomprobacion contra el vector conocido"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T397
nombre: Las cuatro banderas se exigen y una sola que falte no basta
cubre: ["G-03", "O26 1.8"]
dado:
  - "safe_path solo existe desde 3.11 y se exige DONDE EXISTE, porque no se puede exigir lo que no se puede medir"
  - "-I implica -P desde 3.11, y aun asi se comprueba lo que el interprete DICE de si mismo"
cuando: ["se mide la declaracion de aislamiento con seis combinaciones de banderas"]
entonces:
  - "solo -I -S -E juntas declaran aislamiento; ninguna combinacion parcial lo hace"
  - "el interprete de este anfitrion expone safe_path, y por eso la cuarta bandera se mide y no se supone"
falla_si:
  - "se acepta -S -E sin -I, con lo que el directorio del guion volveria a sys.path[0]"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```
