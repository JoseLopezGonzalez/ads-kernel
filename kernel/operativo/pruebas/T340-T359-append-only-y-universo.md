# T340–T359 — append-only por entrada cerrada, universo que no encoge y estado derivado

**Qué cierran.** Los tres hallazgos que el gate del 2026-09-04 asigna a este eje:

```text
ADJ-B3  BLOQUEANTE  el append-only de la sede del Owner era un PREFIJO del commit de
                    nacimiento: 14 395 de 42 181 bytes, el 34,1 %. `O17`, `O18` y `O19`
                    dentro; `O20`…`O26` FUERA. `O27` §3 lo eleva a NORMA
ADJ-G1  GRAVE       el universo obligatorio ENCOGÍA con `exit 0` por tres vías, y la causa
                    era una clase: los suelos estaban ESCRITOS y uno no existía
ADJ-G2  GRAVE       el `estado:` de un escenario se escribía a mano y no lo contrastaba
                    nadie contra la evidencia. La divergencia estaba VIVA en el árbol
```

**Cada hallazgo se REPRODUJO antes de corregirlo**, con su comando y su salida literal, y
ninguna corrección se escribió sobre un hecho que no se hubiera vuelto a ver. La
reproducción de `ADJ-B3` es la del adjudicador, ejecutada de nuevo sobre un clon: borrar
`O20`–`O26` enteras, sustituirlas por «F6 QUEDA CERTIFICADA SIN CONDICIONES», confirmar, y
medir que el verificador publicaba `color=INDETERMINADO · hallazgos=0` con la sede perdiendo
el 66 % de su contenido.

**Lo que estas pruebas ejercitan es la PROPIEDAD, no el texto de ningún fichero.** La
implementación deriva las entradas cerradas de la ESTRUCTURA de la sede y ancla cada una al
COMMIT QUE LA INTRODUJO leyendo la historia de la ruta; no hay ninguna lista de
identificadores escrita, de modo que `O28` nacerá protegida sin que nadie escriba una línea.

> **Los sabotajes son infracciones deliberadas del catálogo negativo**, en
> [`../validadores/negativos_contratos19.py`](../validadores/negativos_contratos19.py), que
> [`../validadores/comprobar_negativos.py`](../validadores/comprobar_negativos.py) aplica
> sobre una COPIA temporal del repositorio —el corpus real no se toca— y exige que la
> prueba señalada falle **por el motivo esperado**: `N340`, `N341`, `N342`, `N343`, `N343b`,
> `N349`, `N350`, `N350b`, `N350c` y `N350d`.
>
> **Los TRES CANALES del juicio de la sede están discriminados uno a uno.** El estructural
> —comparación byte a byte de cada entrada—, el de presencia literal —que sigue hablando
> cuando la estructura queda rota— y el de la historia —que ve una alteración confirmada y
> luego revertida—. Retirar cualquiera de los tres pone en rojo una prueba distinta, y eso
> se midió: sin la discriminación, retirar el canal estructural dejaba la batería en verde
> porque los otros dos tapaban el hueco.

**Lo que NO cierran, dicho entero.** El régimen de ENTRADAS CERRADAS gobierna las rutas
cuya HISTORIA publica entradas derivables; los documentos continuos de la misma clase
—`kernel/KERNEL.md` y las especificaciones aprobadas— conservan el contraste contra el
prefijo del nacimiento, y el veredicto PUBLICA cuál de los dos regímenes aplicó a cada
ruta. Medido al probar la vigilancia permanente sobre todas las rutas de clase
`AUTORIDAD_SUPERIOR`: cuatro de ellas están intactas y NO son un prefijo de su nacimiento,
porque el registro canónico mete en la misma clase la sede del Owner, que es append-only, y
las especificaciones aprobadas, cuyo propio motivo dice «se cambia POR ENMIENDA». Partir esa
clase exige tocar `docs/canonico/FUENTES-CANONICAS.yml`, que no es sede de este eje, y queda
como petición.

**El cliquet del universo tiene ALCANCE MEDIDO y publicado.** Cubre 58 de las 58
obligaciones vivas, y cinco identificadores de la misma forma quedan declarados fuera con su
motivo comprobado en cada corrida —`C1`, `C3`, `C6` y `C7`, contratos transversales de fase
anterior, y `S1-01`, hallazgo del octavo gate cuya sede es el documento del gate—.

**El contraste del estado tiene COBERTURA publicada.** 161 escenarios lo tienen y 92 no,
porque la salida de su ejecutable no imprime una línea de veredicto por escenario. Para esos
92 el estado no se sube por omisión ni se baja por desconocimiento: se publica como NO
CONTRASTABLE con su cifra, para que quien la vea crecer tenga delante el número.

```yaml ads:escenario
id: T340
nombre: Las entradas cerradas de la sede del Owner se derivan de su estructura y se anclan a su commit
cubre: ["ADJ-B3", "O27 3", "V6-12", "CONTRATO-ADMISION 5"]
dado:
  - "una sede con la forma real del corpus, inscrita en commits sucesivos como la de verdad"
  - "ninguna lista de identificadores escrita a mano en ninguna parte del aparato"
cuando:
  - "se deriva el LIBRO de entradas cerradas recorriendo la historia de la ruta"
entonces:
  - "cada entrada aparece con el commit que la introdujo, y no con el commit de nacimiento del fichero"
  - "el preámbulo anterior a la primera entrada es un bloque cerrado más"
  - "sobre la sede intacta el juicio no produce ni una infracción"
  - "el veredicto publica el REGIMEN que ha aplicado a cada ruta append-only"
falla_si:
  - "las entradas se enumeran en una constante en vez de derivarse de la estructura"
  - "el término de comparación se deriva del fichero de hoy, con lo que quien borra una entrada borra la lista de lo que había que conservar"
  - "el veredicto emite verde sin decir con qué regla lo emitió"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: evidencia/admision-salida.txt
```

```yaml ads:escenario
id: T341
nombre: Añadir una resolución completa al final sigue siendo legítimo, y el delimitador no es contenido
cubre: ["ADJ-B3", "O27 1", "O27 3", "V6-12"]
dado:
  - "una sede con tres entradas cerradas y su delimitador estructural entre cada dos"
  - "la medición de que la última entrada gana exactamente los bytes del delimitador cuando se inscribe la siguiente"
cuando:
  - "se añade una entrada nueva y completa al final y se confirma"
entonces:
  - "el juicio no produce ninguna infracción"
  - "los bytes de cada entrada anterior son idénticos antes y después de la inscripción"
  - "el veredicto del verificador de admisión sigue siendo VERDE"
falla_si:
  - "el delimitador entre dos entradas se cuenta como contenido de la de arriba, con lo que una sede intacta da ROJO en cuanto se inscribe la resolución siguiente"
  - "el guardián impide el acto que la sede existe para permitir"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: evidencia/admision-salida.txt
```

```yaml ads:escenario
id: T342
nombre: Borrar entradas posteriores al nacimiento y sustituirlas por otro texto da ROJO
cubre: ["ADJ-B3", "O27 3", "V6-12", "O26 5"]
dado:
  - "la sede real del Owner, con su preámbulo y sus once entradas cerradas"
  - "el ataque del adjudicador: conservar el prefijo del nacimiento y sustituir todo lo demás"
cuando:
  - "se borran las entradas posteriores al prefijo protegido y se escribe en su lugar un texto fabricado"
  - "se confirma el resultado, de modo que el árbol de trabajo queda limpio"
entonces:
  - "el veredicto es ROJO por ALTERACION DE ENTRADAS CERRADAS y no sólo por una huella general"
  - "el diagnóstico nombra una a una las entradas destruidas y el commit que introdujo cada una"
  - "la regla anterior, el prefijo del nacimiento, sigue aprobando el mismo ataque y se comprueba que lo aprueba"
falla_si:
  - "el contraste vuelve a ser un prefijo del commit de nacimiento"
  - "una alteración confirmada antes de la revisión base queda sin juzgar por no aparecer en el diff"
  - "el ataque se detecta pero el diagnóstico no dice qué entradas ha destruido"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: evidencia/admision-salida.txt
```

```yaml ads:escenario
id: T343
nombre: Alterar un byte, insertar texto dentro o cambiar sólo los metadatos de una entrada cerrada da ROJO
cubre: ["ADJ-B3", "O27 3", "V6-12"]
dado:
  - "una entrada ya publicada y cerrada, con sus bytes anclados al commit que la introdujo"
cuando:
  - "se cambia UN byte de su interior sin variar su longitud"
  - "se inserta texto dentro de una resolución anterior"
  - "se cambia exclusivamente su fecha, sin tocar el texto resolutivo"
  - "se altera, se confirma y después se restaura, dejando el árbol de hoy correcto"
entonces:
  - "los tres primeros dan ALTERACION con el motivo del canal ESTRUCTURAL, que nombra la comparación byte a byte"
  - "el cuarto sigue constando por el canal de la HISTORIA, porque confirmar no exime y confirmar dos veces tampoco"
falla_si:
  - "la comparación byte a byte se retira y los otros canales tapan el hueco"
  - "el canal de la historia se retira y una alteración confirmada se blanquea restaurando el fichero"
  - "un cambio de metadatos se considera menor que un cambio de texto"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: evidencia/admision-salida.txt
```

```yaml ads:escenario
id: T344
nombre: Borrar la última resolución o una intermedia da ROJO
cubre: ["ADJ-B3", "O27 3", "V6-12"]
dado:
  - "una sede cuyas entradas están todas cerradas y ancladas a su commit"
cuando:
  - "se trunca el fichero por la cola, llevándose la última resolución entera"
  - "se retira una resolución intermedia dejando el resto intacto"
entonces:
  - "las dos producen BORRADA nombrando la entrada perdida y el commit que la introdujo"
  - "el diagnóstico dice que una resolución posterior REVISA a la anterior sin borrarla"
falla_si:
  - "el truncamiento por la cola pasa por ser una sede que simplemente es más corta"
  - "el juicio sólo mira las entradas que hoy están, con lo que lo borrado deja de existir para el guardián"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: evidencia/admision-salida.txt
```

```yaml ads:escenario
id: T345
nombre: Reordenar dos resoluciones da ROJO aunque no se pierda un solo byte
cubre: ["ADJ-B3", "O27 3", "V6-12"]
dado:
  - "dos entradas cerradas consecutivas, cada una entera"
cuando:
  - "se intercambian de posición conservando exactamente los mismos bytes del fichero"
entonces:
  - "el juicio produce REORDENADAS y publica la secuencia hallada frente a la del libro"
  - "el diagnóstico dice que reordenar cambia qué revisa a qué"
falla_si:
  - "el orden no se comprueba porque cada entrada sigue entera"
  - "la comprobación se hace sobre el conjunto y no sobre la secuencia"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: evidencia/admision-salida.txt
```

```yaml ads:escenario
id: T346
nombre: Dos resoluciones con el mismo identificador dan ROJO
cubre: ["ADJ-B3", "O27 3", "V6-12"]
dado:
  - "una sede con sus entradas cerradas y un identificador por entrada"
cuando:
  - "se duplica una resolución al final, con su identificador repetido"
entonces:
  - "el juicio produce DUPLICADA nombrando las dos posiciones"
  - "el diagnóstico dice que con dos textos bajo el mismo nombre cuál rige deja de tener respuesta"
falla_si:
  - "la derivación descarta duplicados en silencio quedándose con el primero"
  - "un identificador repetido se trata como una excepción de lectura en vez de como un hallazgo"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: evidencia/admision-salida.txt
```

```yaml ads:escenario
id: T347
nombre: Un salto de numeración o una familia de identificadores nueva dan ROJO
cubre: ["ADJ-B3", "O27 3", "V6-12"]
dado:
  - "una sede cuya numeración es consecutiva y cuya familia de identificadores es una sola"
cuando:
  - "se añade una entrada saltándose números"
  - "se añade una entrada de una familia que esta sede no gobierna"
entonces:
  - "el salto produce SALTO_DE_NUMERACION diciendo qué identificador esperaba la sede"
  - "la familia ajena produce FAMILIA_DESCONOCIDA diciendo que no hereda ni el orden ni el cliquet"
falla_si:
  - "un hueco de numeración pasa sin decir nada, con lo que falta una resolución o se ha renumerado una que estaba"
  - "una familia nueva entra en la sede sin criterio que la ordene"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: evidencia/admision-salida.txt
```

```yaml ads:escenario
id: T348
nombre: Un apéndice incompleto se rechaza y las entradas históricas sin los campos no se ponen en rojo
cubre: ["ADJ-B3", "O27 2", "O27 3", "ADJ-O1"]
dado:
  - "una sede cuyas primeras entradas no llevan los campos de forma y cuyas posteriores sí"
  - "el umbral desde el que los campos son exigibles se DERIVA de la primera entrada que ya los trae"
cuando:
  - "se añade una entrada sin cuerpo, y otra con cuerpo y sin los campos de forma"
entonces:
  - "las dos producen INCOMPLETA, y el diagnóstico nombra el umbral derivado"
  - "las entradas históricas anteriores al umbral siguen sin producir ninguna infracción"
falla_si:
  - "la comprobación de forma se aplica al libro y pone en rojo resoluciones ya emitidas, que es lo que O27 2 prohíbe"
  - "el umbral se escribe como una cifra y caduca en cuanto la forma vuelva a cambiar"
  - "un título sin resolución se acepta como entrada completa"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: evidencia/admision-salida.txt
```

```yaml ads:escenario
id: T349
nombre: Sólo se admite añadir al final, el hueco entre entradas no es zona franca y el régimen se deriva de la historia
cubre: ["ADJ-B3", "O27 1", "O27 3", "V6-12", "E-09"]
dado:
  - "una sede con entradas cerradas y un delimitador estructural declarado entre cada dos"
cuando:
  - "se intercala una entrada nueva entre dos ya cerradas"
  - "se escribe texto en el hueco que separa dos entradas"
  - "se borran las cabeceras de entrada para que el documento parezca no tener ninguna"
  - "se altera una entrada, se confirma, y se añade otra encima"
entonces:
  - "intercalar produce INSERCION_NO_AL_FINAL"
  - "el texto del hueco produce infracción, porque ninguna entrada lo reclama"
  - "borrar las cabeceras NO degrada el régimen, porque el régimen se decide desde la historia y no desde el fichero de hoy"
  - "la alteración sigue constando después del commit que la tapa"
falla_si:
  - "el régimen se decide mirando los bytes de hoy, con lo que quitar las cabeceras apaga el guardián"
  - "el hueco entre dos resoluciones admite prosa que nadie firma"
  - "un commit posterior blanquea la alteración anterior"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: evidencia/admision-salida.txt
```

```yaml ads:escenario
id: T350
nombre: El estado declarado de cada escenario lo sostiene su evidencia, y la cobertura del contraste se publica
cubre: ["ADJ-G2", "CONTRATO 3", "P-08"]
dado:
  - "el campo estado de un bloque ads escenario, que hasta ahora se escribía a mano y se copiaba verbatim"
  - "la evidencia publicada por el runner canónico, con su cabecera de procedencia y su código de salida"
cuando:
  - "se deriva el estado de cada escenario de su evidencia y se contrasta contra el declarado"
entonces:
  - "una prueba cuya evidencia publica un veredicto distinto del declarado da FALLIDA nombrando los dos"
  - "un escenario que declara una ejecución sin evidencia declarada da FALLIDA"
  - "un escenario que cita una evidencia que el manifiesto canónico no declara da FALLIDA"
  - "una evidencia del árbol de trabajo que no coincide con la confirmada en HEAD da FALLIDA"
  - "se publica cuántos escenarios se han contrastado y cuántos no son contrastables"
falla_si:
  - "el estado vuelve a copiarse verbatim sin contrastar nada"
  - "la sede de la derivación deja de publicar la fórmula y este validador calcula una suya equivalente"
  - "lo no contrastable se cuenta como contrastado, con lo que la cobertura del contraste crece sin que nadie la mida"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_evidencia.py"
estado: prueba-superada
evidencia: evidencia/evidencia-salida.txt
```

```yaml ads:escenario
id: T351
nombre: El universo obligatorio no puede encoger en silencio por ninguna de sus tres vías
cubre: ["ADJ-G1", "F6-H", "P-08", "O26 5"]
dado:
  - "el derivador del universo obligatorio, cuya cabecera promete que nunca reduce el universo en silencio"
  - "los cuatro suelos que estaban ESCRITOS y el componente F-nn, que no tenía ninguno"
cuando:
  - "se cambia la fase de una fila de hallazgo externo de F6 a F5"
  - "se retira una fila de hallazgo externo entera"
  - "se retira un bloque de contrato entero de la sección 19"
entonces:
  - "las tres terminan con código 2 y el mensaje FALLA CERRADO"
  - "el cambio de fase y la retirada de la fila las caza el cliquet, que nombra qué escenarios y qué sabotajes ejercen la obligación desaparecida"
  - "la retirada del bloque la caza la consecutividad de la numeración, que nombra el hueco"
falla_si:
  - "un suelo vuelve a escribirse como cifra, que es lo que regalaba una unidad de holgura"
  - "una obligación que el corpus ejerce puede caerse del universo con código 0"
  - "el modo obligaciones publica un total menor sin decir qué ha perdido"
ejecucion: guion-manual
validador: "docs/evolucion/verificacion/derivar-universo-obligatorio.py"
estado: validador-implementado
```

```yaml ads:escenario
id: T352
nombre: El derivador falla cerrado ante toda fuente que no puede leer, y distingue el vacío legítimo del fallo
cubre: ["ADJ-G1", "P-08", "V6-03"]
dado:
  - "las sedes de las que sale cada componente del universo obligatorio"
cuando:
  - "una sede no existe, no decodifica como UTF-8, o pierde el bloque que el barrido busca"
  - "un identificador derivado no tiene la forma de su familia"
  - "un componente deriva el conjunto vacío"
entonces:
  - "todas terminan con código 2 y nombran la causa concreta"
  - "el conjunto vacío se declara como derivación que ha dejado de funcionar y no como universo vacío legítimo"
falla_si:
  - "una sede ilegible produce una lista parcial en vez de un fallo"
  - "un identificador de familia desconocida entra en el universo porque venía de la sede"
  - "un componente vacío se publica como cero sin decir que su sede sí tiene contenido"
ejecucion: guion-manual
validador: "docs/evolucion/verificacion/derivar-universo-obligatorio.py"
estado: validador-implementado
```

```yaml ads:escenario
id: T353
nombre: El cliquet del universo tiene alcance medido, sus excepciones se comprueban y las fronteras se declaran
cubre: ["ADJ-G1", "ADJ-M4", "ADJ-M10", "O18 6"]
dado:
  - "las obligaciones que el corpus ejerce, derivadas del cubre de cada escenario y de la obligación de cada sabotaje"
  - "cinco identificadores de la misma forma que pertenecen a fases anteriores"
cuando:
  - "se deriva el universo y se publica su procedencia, su criterio de pertenencia y sus restas"
entonces:
  - "cada componente publica de qué sede sale, con su digest y su tamaño"
  - "cada componente publica su CRITERIO DE PERTENENCIA, que no es el mismo para todos y se dice"
  - "cada exclusión se publica con su motivo, y una exclusión sin motivo escrito falla cerrado"
  - "cada resta publica, pegado a su cifra, la proposición que esa cifra NO demuestra"
  - "una excepción del cliquet cuyo motivo deja de ser cierto falla cerrado"
falla_si:
  - "una resta vacía se lee como prueba de una condición de O26 5 que no mide"
  - "la frontera de un componente se rotula por estructura cuando es una selección escrita"
  - "la lista de excepciones del cliquet se estira sin que nadie compruebe que siguen siendo ciertas"
ejecucion: guion-manual
validador: "docs/evolucion/verificacion/derivar-universo-obligatorio.py"
estado: validador-implementado
```
