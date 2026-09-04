# T290–T311 — vínculo, orden durable, procedencia, evidencia y contención

**Qué cierran.** Los siete hallazgos que la corrección del 2026-09-04 asigna a este eje:
`E-07` el vínculo commit + `tree` de la raíz externa · `E-08` el orden irrompible de los
pasos 8 y 9 del motor de estado · `E-09` `V6-12` sin degradación silenciosa · `E-10` la
procedencia del `sys.path` en el camino productivo `--repo` · `E-14` la evidencia, donde
`OK` no puede seguir equivaliendo a `OK (skipped=N)` · `E-15` los errores tipados que
escapaban de `main()` · `E-16` la política de contención, que estaba construida y no era
alcanzable desde ningún punto ejecutable. Y el REGISTRO de `E-17` —custodia productiva de
claves, que sigue EXTERNA— y `E-18` —la limitación de este anfitrión, con su alcance exacto—.

**Cada hallazgo se REPRODUJO antes de corregirlo**, con un comando concreto y su salida
literal, y ninguna corrección se escribió sobre un hecho que no se hubiera vuelto a ver. Lo
que las pruebas de abajo ejercitan es la PROPIEDAD, no el texto de ningún fichero:
reintroducir el defecto las pone en rojo, y la matriz «sano → VERDE, sabotaje → ROJO por el
motivo esperado, restaurado → VERDE» se ejecutó una a una.

> **Los sabotajes de `E-14` son infracciones deliberadas del catálogo negativo**, en
> [`../validadores/negativos_integridad.py`](../validadores/negativos_integridad.py), que
> [`../validadores/comprobar_negativos.py`](../validadores/comprobar_negativos.py) aplica
> sobre una COPIA temporal del repositorio —el corpus real no se toca— y exige que `T158`
> falle **por el motivo esperado**: `NE14a`, `NE14b`, `NE14c`, `NE14d` y `NE14e`.
>
> **Los de `E-07`, `E-08`, `E-09`, `E-10`, `E-15` y `E-16` se ejercen sobre el CÓDIGO**, no
> sobre el corpus, y por eso no caben en ese catálogo: su matriz se reproduce copiando el
> repositorio, reintroduciendo el defecto y volviendo a ejecutar la batería que lo mide.

**Las dos mitades de `exigir_vinculo` tienen prueba INDEPENDIENTE.** Es la corrección de
`E-07` y su criterio de cierre: sabotear la mitad `tree` pone en rojo `T291` y sólo `T291`;
sabotear la mitad `commit` pone en rojo `T292`, `T293` y la prueba de `T220` que ya existía.
Los dos conjuntos son DISJUNTOS, que es lo que antes no ocurría —con cualquiera de las dos
mitades neutralizada la batería seguía dando 38/38 en verde—.

**Lo que NO cierran.** `E-17` sigue ABIERTA y es EXTERNA: su registro —propietario, mecanismo
previsto, condición de cierre y por qué una clave efímera no la satisface— está en el README
del paquete de la raíz externa, y `T309` comprueba que ninguna salida de esta zona afirma
custodia productiva. `E-18` sigue siendo LIMITACIÓN DE ANFITRIÓN: `cgroup v2` está presente
y NO es ejercitable aquí, y `T309` exige que lo no ejercido se declare con su motivo y no se
cuente como ejercido.

```yaml ads:escenario
id: T290
nombre: Control positivo del vínculo commit y tree de la raíz externa
cubre: ["E-07", "V6-16", "g.15", "O26 1.3", "CONTRATO-RAIZ-EXTERNA 1"]
dado:
  - "una atestación firmada de verdad con la clave que el anillo externo acepta"
  - "el commit y el tree que la atestación declara son los del árbol que se comprueba"
cuando: ["se comprueba la atestación con el punto ejecutable de la raíz externa"]
entonces:
  - "la comprobación pasa y publica los siete pasos de verificación en su orden"
  - "la secuencia publicada es firma, clave aceptada, época, commit, tree, política, identidad del emisor"
falla_si:
  - "el camino de comprobación deja de pasar sobre una atestación correcta"
  - "la secuencia publicada no enumera los siete pasos, con lo que el resto de pruebas medirían un camino roto"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_raiz_externa.py"
estado: prueba-superada
evidencia: "evidencia/raiz-externa-salida.txt"
```

```yaml ads:escenario
id: T291
nombre: Un commit correcto con un tree incorrecto se rechaza por la mitad TREE
cubre: ["E-07", "V6-16", "O26 1.3", "11-ARQ 11.8"]
dado:
  - "una atestación firmada válida cuyo repositorio declara el commit vigente"
  - "el tree que esa atestación declara no es el del commit vigente"
cuando: ["se comprueba la atestación contra el árbol real"]
entonces:
  - "la raíz externa RECHAZA con el código VINCULO_DE_TREE_ROTO"
  - "el código publicado NO es el de la mitad commit, de modo que se sabe cuál de las dos cortó"
  - "la función exigir_tree levanta por sí sola, con exigir_commit pasando al lado"
falla_si:
  - "la mitad tree deja de comprobarse y la atestación se acepta"
  - "las dos mitades vuelven a compartir código de error y dejan de distinguirse"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_raiz_externa.py"
estado: prueba-superada
evidencia: "evidencia/raiz-externa-salida.txt"
```

```yaml ads:escenario
id: T292
nombre: Un tree correcto con un commit incorrecto se rechaza por la mitad COMMIT
cubre: ["E-07", "V6-16", "O26 1.3", "11-ARQ 11.8"]
dado:
  - "una atestación firmada válida cuyo repositorio declara el tree vigente"
  - "el commit que esa atestación declara no es el vigente"
cuando: ["se comprueba la atestación contra el árbol real"]
entonces:
  - "la raíz externa RECHAZA con el código VINCULO_DE_COMMIT_ROTO"
  - "la función exigir_commit levanta por sí sola, con exigir_tree pasando al lado"
falla_si:
  - "la mitad commit deja de comprobarse y la atestación se acepta"
  - "el rechazo se produce por cualquier otro motivo, que haría la prueba insensible al defecto"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_raiz_externa.py"
estado: prueba-superada
evidencia: "evidencia/raiz-externa-salida.txt"
```

```yaml ads:escenario
id: T293
nombre: Una firma correcta de una tupla distinta no vale para este árbol
cubre: ["E-07", "V6-16", "O26 1.3", "g.15"]
dado:
  - "una atestación firmada de verdad, cuya firma verifica byte a byte contra los firmantes autorizados"
  - "el árbol ha avanzado y la tupla commit y tree que la atestación declara ya no es la vigente"
cuando: ["se comprueba esa atestación sobre el árbol nuevo"]
entonces:
  - "la firma sigue verificando, y el control positivo lo comprueba explícitamente"
  - "la raíz externa RECHAZA igualmente, porque la atestación habla de otra tupla"
  - "commit y tree incorrectos a la vez también se rechazan"
falla_si:
  - "una firma válida se toma por una atestación aplicable"
  - "reutilizar una atestación buena sobre otro árbol produce veredicto favorable"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_raiz_externa.py"
estado: prueba-superada
evidencia: "evidencia/raiz-externa-salida.txt"
```

```yaml ads:escenario
id: T294
nombre: Clave válida para otra época, huella ajena y ancla distinta se rechazan
cubre: ["E-07", "O25 5", "I-g3", "V6-17"]
dado:
  - "una atestación firmada con la clave legítima que declara una época fuera del solapamiento de su identidad"
  - "otra que se atribuye a una identidad del anillo publicando la huella pública de otra clave"
  - "otra cuyo veredicto se calculó contra una base distinta de la que ancla la configuración externa"
cuando: ["se comprueba cada una con la configuración externa de confianza"]
entonces:
  - "la de la época fuera de ventana se rechaza con IDENTIDAD_NO_ACEPTADA"
  - "la de la huella ajena se rechaza con EMISOR_NO_COINCIDE"
  - "la del ancla distinta se rechaza con ANCLA_NO_COINCIDE"
falla_si:
  - "la validez de una firma depende del reloj de la máquina que verifica y no de la época"
  - "una atestación puede atribuirse a quien no la firmó"
  - "un veredicto calculado bajo otra política se acepta como propio"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_raiz_externa.py"
estado: prueba-superada
evidencia: "evidencia/raiz-externa-salida.txt"
```

```yaml ads:escenario
id: T295
nombre: Modificar la atestación después de firmarla la invalida
cubre: ["E-07", "V6-16", "g.15", "O26 1.8"]
dado:
  - "una atestación firmada y su sobre, con el digest de lo firmado publicado al lado"
  - "alguien cambia el tree del cuerpo y recalcula el digest para que el sobre no se delate por ahí"
cuando: ["se comprueba el sobre modificado"]
entonces:
  - "la comprobación falla con FIRMA_NO_VERIFICADA y no llega a mirar el vínculo"
falla_si:
  - "la firma deja de cubrir todo el cuerpo que la atestación publica"
  - "el digest publicado sustituye a la firma como prueba de integridad"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_raiz_externa.py"
estado: prueba-superada
evidencia: "evidencia/raiz-externa-salida.txt"
```

```yaml ads:escenario
id: T296
nombre: La evidencia de la raíz externa sólo se escribe tras los siete pasos
cubre: ["E-07", "g.15", "g.13", "O25 2"]
dado:
  - "los siete pasos declarados en orden: firma, clave aceptada, época, commit, tree, política, identidad del emisor"
  - "la única puerta de escritura de evidencia exige el testigo de la secuencia completa"
cuando: ["se interrumpe la secuencia en cada uno de los siete pasos y se intenta escribir"]
entonces:
  - "cada interrupción levanta SECUENCIA_DE_VERIFICACION_INCOMPLETA y NO deja fichero"
  - "con los siete anotados la misma llamada SÍ escribe, que es el control del control"
  - "anotar un paso fuera de orden es un fallo, no un reordenamiento"
  - "la emisión publica la secuencia completa en su orden, de modo que se puede auditar"
falla_si:
  - "la evidencia se escribe antes de completar los siete pasos"
  - "el orden depende sólo de que el código esté escrito en cierto orden"
  - "se puede publicar evidencia sin testigo de verificación"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_raiz_externa.py"
estado: prueba-superada
evidencia: "evidencia/raiz-externa-salida.txt"
```

```yaml ads:escenario
id: T297
nombre: El paso 9 no publica la revisión sin el testigo durable del paso 8
cubre: ["E-08", "g.3", "g.4", "g.8", "CONTRATO-ESTADO-DURABLE 3"]
dado:
  - "el protocolo transaccional declara que el orden de sus doce pasos no admite reordenación"
  - "el paso 8 deja un testigo durable con el cid observado de cada objeto que acaba de publicar"
cuando: ["se intenta publicar la revisión sin ese testigo, que es el estado del disco cuando el 9 se adelanta al 8"]
entonces:
  - "la publicación falla con un error tipado y la revisión vigente no cambia"
  - "un testigo escrito antes de publicar los objetos anota los cid VIEJOS y tampoco deja publicar"
falla_si:
  - "los pasos 8 y 9 se pueden invertir sin que nada observable lo note"
  - "el testigo se puede fabricar antes de que los objetos estén en canonico"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_estado_durable.py"
estado: prueba-superada
evidencia: "evidencia/estado-durable-salida.txt"
```

```yaml ads:escenario
id: T298
nombre: Una mezcla parcial de objetos publicados no se convierte en vigente
cubre: ["E-08", "g.3", "g.14", "CONTRATO-ESTADO-DURABLE 3"]
dado:
  - "un plan con dos rutas y un testigo que sólo cubre una"
cuando: ["el paso 9 exige el testigo antes de publicar la revisión"]
entonces:
  - "la publicación falla y el mensaje nombra la mezcla parcial"
  - "la revisión no llega a nombrar objetos que no están en canonico"
falla_si:
  - "una publicación a medias se convierte en vigente"
  - "el testigo se acepta sin cubrir exactamente las rutas del plan"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_estado_durable.py"
estado: prueba-superada
evidencia: "evidencia/estado-durable-salida.txt"
```

```yaml ads:escenario
id: T299
nombre: El testigo del paso 8 se escribe con fsync de contenido y de directorio
cubre: ["E-08", "g.4", "CONTRATO-ESTADO-DURABLE 2"]
dado:
  - "la entrada de directorio que un os.replace crea es metadato del directorio"
cuando: ["el paso 8 escribe su testigo y se interceptan las primitivas de durabilidad"]
entonces:
  - "el testigo pasa por la primitiva que sincroniza el CONTENIDO del fichero"
  - "y por la que sincroniza el DIRECTORIO que lo contiene"
falla_si:
  - "el testigo se escribe sin fsync y un corte de corriente se lo lleva"
  - "se sincroniza el fichero y no su directorio, con lo que el contenido está y el nombre no"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_estado_durable.py"
estado: prueba-superada
evidencia: "evidencia/estado-durable-salida.txt"
```

```yaml ads:escenario
id: T300
nombre: Una caída entre los pasos 8 y 9 se recupera y deja el almacén íntegro
cubre: ["E-08", "g.8", "g.4", "CONTRATO-ESTADO-DURABLE 4"]
dado:
  - "un punto de fallo inyectable exactamente entre los pasos 8 y 9, que antes no existía"
  - "la rama COMPLETAR reejecuta los pasos 8, 9 y 10 de forma idempotente"
cuando: ["el proceso muere en ese punto y se vuelve a abrir el almacén"]
entonces:
  - "el testigo del paso 8 está en disco, luego el paso 8 había terminado"
  - "la revisión vigente sigue siendo la anterior, luego el paso 9 no llegó"
  - "tras recuperar, la transición se completa, la ruta queda publicada y la integridad es verde"
  - "borrar el testigo antes de recuperar no permite publicar a ciegas: la recuperación lo reescribe"
falla_si:
  - "la recuperación publica la revisión sin el testigo que el paso 9 exige"
  - "la garantía del orden vale para el camino feliz y no para la recuperación"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_estado_durable.py"
estado: prueba-superada
evidencia: "evidencia/estado-durable-salida.txt"
```

```yaml ads:escenario
id: T301
nombre: Los tres escenarios extremo a extremo no terminan sobre un almacén irrecuperable
cubre: ["E-08", "g.4", "g.8", "T175", "T182"]
dado:
  - "con los pasos 8 y 9 invertidos los tres escenarios terminaban en verde sobre un almacén irrecuperable"
cuando: ["cada escenario termina, y antes de borrar su temporal"]
entonces:
  - "se descubren todos los almacenes durables que el escenario dejó, y se exige encontrar al menos uno"
  - "cada uno se ABRE, se RECUPERA y se verifica su integridad"
  - "un almacén que no se pueda abrir o cuya integridad falle hace que el escenario salga con código distinto de cero"
falla_si:
  - "un escenario termina en verde dejando un REVISION.json que nombra objetos que no están publicados"
  - "el descubrimiento no encuentra ningún almacén, con lo que la comprobación no habría podido fallar"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/escenario_e2e_f6.py"
estado: prueba-superada
evidencia: "evidencia/e2e-f6-salida.txt"
```

```yaml ads:escenario
id: T302
nombre: Con nacimiento trazable, crecer una sede append-only sigue siendo legítimo
cubre: ["E-09", "V6-12", "O10", "S1-02"]
dado:
  - "la sede del Owner nació en un commit alcanzable y su contenido publicado allí es prefijo del actual"
cuando: ["se emite el veredicto de admisión"]
entonces:
  - "el veredicto es VERDE y no hay hallazgo de V6-12"
falla_si:
  - "añadir una resolución produce rojo, con lo que la comprobación sería imposible de superar y no mediría nada"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: "evidencia/admision-salida.txt"
```

```yaml ads:escenario
id: T303
nombre: Sin commit de nacimiento trazable V6-12 falla cerrado y no compara contra la base
cubre: ["E-09", "V6-12", "S1-02", "g.13"]
dado:
  - "la sede nació en C0, fue ALTERADA en C1, y C1 es la base declarada; encima se añade en C2"
  - "contra el nacimiento el ataque se ve; contra la base queda blanqueado"
cuando: ["el commit de nacimiento no se puede derivar, o se deriva a un commit que no resuelve, o a uno que no contiene la sede"]
entonces:
  - "el veredicto es ROJO en los tres casos, con el punto V6-12 y la procedencia en la causa"
  - "la causa nombra la procedencia concreta: sin-nacimiento o nacimiento-sin-la-sede"
falla_si:
  - "un nacimiento desconocido se sustituye en silencio por el contenido de la base"
  - "la comprobación se omite sin decirlo y el veredicto sale verde"
  - "se acepta una sede sin nacimiento trazable"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: "evidencia/admision-salida.txt"
```

```yaml ads:escenario
id: T304
nombre: Una historia truncada o injertada no sostiene el contraste de V6-12
cubre: ["E-09", "V6-12", "V6-03", "g.13"]
dado:
  - "en un clon superficial git log --diff-filter=A sigue devolviendo un commit, y es el corte de la clonación"
  - "grafts y refs de replace reescriben qué historia se alcanza sin tocar ningún commit"
cuando: ["se juzga una sede append-only sobre una copia con la historia truncada o injertada"]
entonces:
  - "la procedencia de la historia se declara incompleta con su motivo"
  - "el veredicto es ROJO y la causa nombra historia-truncada"
  - "el control positivo comprueba antes que la historia de partida SÍ era completa"
falla_si:
  - "el primer commit que la copia alcanza se toma por el nacimiento"
  - "una historia reescrita produce un contraste que sale verde contra la alteración"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: "evidencia/admision-salida.txt"
```

```yaml ads:escenario
id: T305
nombre: Vaciar los bytes del nacimiento no produce verde
cubre: ["E-09", "V6-12", "V6-03"]
dado:
  - "la sede está alterada respecto de lo publicado en su nacimiento"
  - "además, la lectura del contenido del nacimiento devuelve vacío"
cuando: ["se emite el veredicto"]
entonces:
  - "el veredicto es ROJO con el punto V6-12"
falla_si:
  - "la ausencia de bytes con que comparar se resuelve dando por buena la sede"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_admision.py"
estado: prueba-superada
evidencia: "evidencia/admision-salida.txt"
```

```yaml ads:escenario
id: T306
nombre: La procedencia de los módulos con --repo es del aparato y se publica
cubre: ["E-10", "V6-04", "V6-11", "g.15", "6.4 sesión nueva"]
dado:
  - "los cinco puntos ejecutables importaban un homónimo colocado en PYTHONPATH, porque sys.path[0] protege a los paquetes vecinos y no a la biblioteca estándar"
  - "un paquete homónimo que deja un fichero testigo al importarse, de modo que su importación no se puede tragar"
cuando: ["se ejecuta cada punto ejecutable en SESIÓN NUEVA con PYTHONPATH envenenado, y también desde dentro del directorio envenenado"]
entonces:
  - "ningún punto ejecutable importa el homónimo y el fichero testigo no existe"
  - "el control del control comprueba que el homónimo SÍ se importa cuando nadie lo impide"
  - "el veredicto se publica entero y no como el objeto vacío que el json sustituido devolvía"
  - "la salida publica de dónde salió cada módulo del aparato y cuántas entradas del lanzador se retiraron"
  - "juzgar un repositorio ajeno que trae su propio aparato no importa ni una línea de él"
falla_si:
  - "el sys.path, el cwd o el PYTHONPATH del lanzador sustituyen a un módulo del aparato"
  - "la procedencia no es demostrable en la salida"
  - "dos repositorios distintos se contaminan"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T307
nombre: OK no equivale a OK con saltos y el contador se contrasta con la salida
cubre: ["E-14", "T158", "g.13", "validadores.yaml"]
dado:
  - "dieciséis componentes declaran firma_de_exito OK, que con re.search casa igual con OK que con OK (skipped=17)"
  - "hay diecisiete llamadas a skipTest en seis baterías del runtime, sin contar ni publicar"
cuando: ["se juzga el resultado de una batería de unittest"]
entonces:
  - "una corrida con saltos no declarados es ROJA"
  - "los saltos permitidos se declaran uno a uno con id y motivo, y el recuento tiene que casar exactamente"
  - "un OK que declara failures, errors, expected failures o unexpected successes es ROJO"
  - "el número de casos declarado se contrasta con los desenlaces que la salida verbosa imprime"
  - "dos corridas pegadas en el mismo fichero son ROJO"
  - "la evidencia que el repositorio publica hoy supera la comprobación, que es el control positivo"
falla_si:
  - "la comprobación vuelve a ser una subcadena y OK vuelve a casar con OK (skipped=N)"
  - "se permiten saltos sin declarar cuáles y por qué"
  - "manipular el contador de casos no invalida la evidencia"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T308
nombre: Ningún error tipado sale de main como traza, y cada clase tiene su código
cubre: ["E-15", "11 CLI", "g.15", "CONTRATO-ADAPTADOR 2"]
dado:
  - "hay DOS clases homónimas CapacidadNoSoportada: la del runtime se capturaba y la del adaptador escapaba como traceback con rutas absolutas y código 1"
  - "los cinco puntos ejecutables comparten el mismo convenio de códigos de salida"
cuando: ["se lleva cada punto ejecutable a un fallo tipado de cada jerarquía que puede alcanzarlo"]
entonces:
  - "la tabla de códigos es idéntica en los cinco, y sus valores son distintos entre sí"
  - "el error del adaptador sale con su código propio y con salida estructurada"
  - "la clase homónima del runtime sigue saliendo por el código que ya publicaba"
  - "el error de contención tiene su propio código, distinto del de la tarea que falla"
  - "ninguna salida contiene una traza ni una ruta absoluta del anfitrión"
  - "no hay éxito parcial: cuando el fallo es tipado, la salida de éxito está vacía"
falla_si:
  - "una jerarquía tipada esperable vuelve a escapar como traceback"
  - "dos clases de fallo comparten código de salida y un guion no las puede distinguir"
  - "el stderr publica el árbol de directorios de quien ejecuta"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T309
nombre: La contención se activa desde el punto ejecutable y el alcance del anfitrión se mide
cubre: ["E-16", "E-17", "E-18", "FD-5", "O25 5", "O26 3", "O26 4", "T215", "T216"]
dado:
  - "la cadena contencion no aparecía en ninguno de los cinco ads_*.py, luego la política estaba construida y no era alcanzable"
  - "una tarea que engendra hijo, nieto y bisnieto, los tres haciendo setsid"
cuando: ["se despacha esa tarea por el punto ejecutable con la política de contención pedida en la línea de órdenes"]
entonces:
  - "las tres generaciones se capturan mientras viven y ninguna sobrevive"
  - "pedir el nivel fuerte con un backend de nivel inferior FALLA CERRADO, con su código propio, y no engendra ni una generación"
  - "ads_ciclo declara las mismas opciones y su fallo cerrado llega hasta el final"
  - "cada backend publica si está disponible y, si no lo está, POR QUÉ; un backend no disponible no se cuenta entre los fuertes disponibles"
  - "el README de la raíz externa registra E-17 con propietario, mecanismo previsto y condición de cierre, y ninguna sede de esta zona afirma custodia productiva"
falla_si:
  - "ningún punto ejecutable puede activar la política de contención"
  - "la ausencia de contención fuerte se resuelve cayendo al backend débil y siguiendo"
  - "un backend que no se puede ejercer se cuenta como ejercido, o su ausencia produce un falso rojo"
  - "una clave efímera de pruebas se presenta como custodia productiva"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

## `T310` y `T311` — la ventana de publicación, aparecida AL INTEGRAR

**No son de este eje ni de ningún otro: aparecieron al juntar los tres.** `test_continua.py`
`test_21` —que mata con `SIGKILL` a un escritor real mientras otra instancia lee el mismo
paquete en bucle y sin bloqueo— empezó a reventar con `ESTADO_CORRUPTO` diciendo «*el fichero
fue modificado fuera del diario, o está truncado*». **Ninguna de las dos cosas era cierta:**
el lector veía el objeto NUEVO con la revisión VIEJA, que es la ventana entre el paso 8 y el
paso 9 del protocolo transaccional.

La carrera era **LATENTE desde el primer corte** —el paso 8 ya reemplazaba en `canonico/`
antes de que el 9 publicara `REVISION.json`— y la corrección de `E-08` la **ENSANCHÓ** al
meter entre los dos el testigo durable con sus dos `fsync`. Se dice así, y no «la introdujo
el testigo»: una carrera que sólo se manifiesta cuando la ventana crece llevaba abierta
desde el principio, y el diagnóstico falso llevaba el mismo tiempo esperando.

**Las dos pruebas son las dos mitades, y hacen falta las dos.** Una sola que exigiera «no
revientes» se satisfaría devolviendo el objeto nuevo —publicar una transición que todavía
puede REVERTIRSE, que es el «por si acaso sirve» que `g.5` prohíbe—; una sola que exigiera
«revienta» volvería a dar el diagnóstico falso. Juntas fijan que la ventana y la corrupción
se distinguen, que el remedio de cada una se nombra, y que **ninguna de las dos devuelve
contenido**.

```yaml ads:escenario
id: T310
nombre: La ventana de publicación no se diagnostica como corrupción
cubre: ["E-08", "g.3", "g.5", "CONTRATO-ESTADO-DURABLE 3", "CONTRATO-ESTADO-DURABLE 5"]
dado:
  - "un objeto canónico ya reemplazado por el paso 8 y una revisión que todavía nombra la anterior"
  - "el testigo durable del paso 8 declara ese mismo cid para esa misma ruta"
cuando: ["un lector concurrente, que no toma el bloqueo de escritor, lee esa ruta"]
entonces:
  - "el lector NO devuelve contenido, porque la transición todavía puede revertirse"
  - "el error es PUBLICACION_EN_VUELO, nombra la transacción y nombra la rama COMPLETAR como remedio"
falla_si:
  - "el lector devuelve el objeto nuevo, publicando una transición reversible"
  - "el lector lo llama ESTADO_CORRUPTO, que manda a buscar un fichero roto que no existe"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T311
nombre: Sin testigo que lo avale, un cid que no casa sigue siendo estado corrupto
cubre: ["E-08", "g.5", "CONTRATO-ESTADO-DURABLE 3"]
dado:
  - "el mismo objeto canónico alterado en disco y la misma revisión sin mover"
  - "ningún testigo de publicación declara ese cid para esa ruta"
cuando: ["un lector concurrente lee esa ruta"]
entonces:
  - "el error es ESTADO_CORRUPTO y dice que el fichero fue modificado fuera del diario"
  - "el error NO es PUBLICACION_EN_VUELO, que tiene otro remedio"
falla_si:
  - "la tolerancia de la ventana se come la corrupción real y llama ventana a todo lo que no casa"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```
