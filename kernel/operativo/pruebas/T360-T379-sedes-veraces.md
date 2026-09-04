# T360–T379 — sedes veraces: que ningún documento vivo contradiga al árbol

**Qué cierran.** Los hallazgos del gate del 2026-09-04 cuya clase es **una sede que afirma
algo que su propio código o su propio árbol desmienten**: `ADJ-G3` —el documento que se
declara ÚNICA SEDE de la distinción construido/diseñado negando en cuatro secciones lo que su
§1 declara construido—, `ADJ-M1` —la orden `censo-formulas` censando un conjunto distinto del
que mide su prueba—, `ADJ-M2` —cinco puntos ejecutables declarando que publican su procedencia
y sólo uno publicándola—, `ADJ-M3` —el contrato del estado durable afirmando que los tres E2E
no pueden seguir verdes sobre un almacén irrecuperable sin que ninguno inyectara el único
punto que produce ese estado—, `ADJ-M5` —la frontera del barrido de recuentos motivada sólo
en una de sus dos mitades— y `ADJ-M11` —dos sedes afirmando que `arboles/` queda fuera del
censo con el código diciendo lo contrario—.

**Cada hallazgo se REPRODUJO antes de corregirlo**, con su comando y su salida literal, y
ninguna corrección se escribió sobre un hecho que no se hubiera vuelto a ver. `ADJ-G3` se
reprodujo además **mecánicamente**: el propio `T360`, ejecutado sobre el árbol sin corregir,
publicó las ONCE sedes —las cuatro secciones citadas por el gate, más `06-DEUDA` §6 en sus dos
mitades y `05-PLAN` L6—, y ninguna otra.

**Es la TERCERA recurrencia de la misma clase en el mismo documento, y por eso lo que se
corrige no son las líneas.** Dos veces se sustituyó aquí un cardinal caducado por otro
cardinal escrito a mano, y dos veces volvió a envejecer —una de ellas **en menos de
veinticuatro horas**—. Lo que cambia ahora es el mecanismo: **el estado de construcción tiene
UNA sección**, las demás **remiten** o **derivan**, y `T360` contrasta cada negación de
existencia contra una **SONDA en el disco**. Reintroducir la afirmación falsa —con estas
palabras o con otras— pone la comprobación en ROJO.

**Lo que estas pruebas NO dicen.** Ninguna afirma que nada esté CERTIFICADO. Estar construido,
estar ejecutado y estar certificado son tres cosas distintas, y la tercera sólo la puede
emitir un juicio independiente sobre un SHA exacto: eso sigue siendo deuda viva y su sede no
es ésta.

> **Los sabotajes de `ADJ-G3` y `ADJ-M5` son infracciones deliberadas del catálogo negativo**,
> en [`../validadores/negativos_integridad.py`](../validadores/negativos_integridad.py), que
> [`../validadores/comprobar_negativos.py`](../validadores/comprobar_negativos.py) aplica
> sobre una COPIA temporal del repositorio —el corpus real no se toca— y exige que la prueba
> señalada falle **por el motivo esperado**.
>
> **Los de `ADJ-M1`, `ADJ-M2`, `ADJ-M3` y `ADJ-M11` se ejercen sobre el CÓDIGO**, y por eso no
> caben en ese catálogo: su matriz «sano → VERDE, sabotaje → ROJO por el motivo esperado,
> restaurado → VERDE» se reproduce copiando el repositorio, reintroduciendo el defecto y
> volviendo a ejecutar el escenario que lo mide.

```yaml ads:escenario
id: T360
nombre: Ninguna sede viva niega una pieza que el arbol tiene construida
cubre: ["ADJ-G3", "11-ARQ 19 CONTRATO 1", "04-CONTRATOS 1", "g.15"]
dado:
  - "el corpus vivo se descubre barriendo, y cada pieza construida declara una SONDA en el disco"
  - "las negaciones de existencia que el corpus usa estan declaradas una a una, con sus recitales y sus restrictivos"
cuando: ["se barren todas las sedes vivas y se contrasta cada negacion contra la sonda de la pieza a la que se refiere"]
entonces:
  - "negar una pieza cuyo fichero esta en el arbol produce un hallazgo con la sede, la linea y la evidencia que la desmiente"
  - "una negacion restringida —«ningun adaptador de proveedor»— NO produce hallazgo, porque afirma otra cosa y es cierta"
  - "un recital que CITA la redaccion anterior para desmentirla tampoco produce hallazgo"
  - "si una sonda desaparece del arbol la prueba falla, porque entonces la que ha envejecido es la tabla de piezas"
falla_si:
  - "una sede viva vuelve a declarar inexistente el verificador de admision, la raiz externa, los adaptadores, el sellado del diario, el ciclo o los macrocircuitos"
  - "la negacion se reescribe con otras palabras y deja de detectarse, que es como reaparecio las dos veces anteriores"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_recuentos.py"
estado: prueba-superada
evidencia: "evidencia/recuentos-salida.txt"
```

```yaml ads:escenario
id: T361
nombre: La frontera del barrido de recuentos esta motivada en sus dos mitades
cubre: ["ADJ-M5", "11-ARQ 19 CONTRATO 1", "T151"]
dado:
  - "el ambito vivo era una lista de seis prefijos de INCLUSION sin un solo motivo escrito"
  - "la otra mitad, FUERA_DEL_AMBITO, motivaba los suyos uno a uno y T151 ya comprobaba esos motivos"
cuando: ["se ejecuta T151 sobre el arbol"]
entonces:
  - "cada patron de inclusion, cada exclusion y cada zona sin barrido declara por que barre o deja de barrer lo que abarca"
  - "todo documento .md del arbol cae en una de las dos mitades declaradas, y el que no cae se publica con su ruta"
  - "docs/rediseno, docs/owner, docs/evolucion, docs/f5 y tooling quedan fuera CON su motivo, y ya no por omision"
falla_si:
  - "una zona nueva de documentos aparece en el arbol y queda fuera del barrido sin que nada lo diga, que es como docs/f5 quedo fuera"
  - "un patron de cualquiera de las dos mitades se queda sin motivo escrito"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_recuentos.py"
estado: prueba-superada
evidencia: "evidencia/recuentos-salida.txt"
```

```yaml ads:escenario
id: T362
nombre: Los tres escenarios extremo a extremo siembran el corte entre los pasos 8 y 9
cubre: ["ADJ-M3", "E-08", "g.4", "g.8", "CONTRATO-ESTADO-DURABLE 3", "T301"]
dado:
  - "entre-el-paso-8-y-el-9 es el unico punto del protocolo que deja objetos publicados con su testigo y la revision sin publicar"
  - "ninguno de los tres escenarios inyectaba ese punto, de modo que la comprobacion de recuperabilidad no habia visto nunca ese estado"
cuando: ["cada escenario, al terminar sus pasos, siembra un control repo aparte y corta una transicion en ese punto exacto"]
entonces:
  - "el corte sale con codigo 70, el testigo del paso 8 esta en disco y la revision vigente sigue siendo la anterior"
  - "el barrido de recuperabilidad encuentra ese almacen por su marca en disco y lo RECUPERA por la rama COMPLETAR"
  - "el almacen recuperado queda integro y auditable, y el escenario sale con cero"
falla_si:
  - "el corte no corta, o cae en otro sitio, con lo que el escenario terminaria sobre un almacen sano y no mediria nada"
  - "la rama COMPLETAR deja de recuperar, o el almacen recuperado no verifica su integridad"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/escenario_e2e_f6.py"
estado: prueba-superada
evidencia: "evidencia/e2e-f6-salida.txt"
```

```yaml ads:escenario
id: T363
nombre: La orden censo-formulas censa el mismo conjunto que el veredicto de V6-19
cubre: ["ADJ-M1", "V6-19", "11-ARQ 20.1"]
dado:
  - "la orden censaba todo el runtime, que es el sujeto de V6-04, y el veredicto censaba el aparato de verificacion, que es el de V6-19"
  - "sobre el propio candidato la orden daba segundas definiciones 7, ok no y codigo 1 con la bateria en verde"
cuando: ["se ejecuta la orden sobre el propio arbol y se compara su conjunto censado con el que mide el veredicto"]
entonces:
  - "los dos conjuntos son el MISMO, modulo a modulo, y la orden sale con cero sobre un arbol limpio"
  - "las siete segundas definiciones desaparecen porque eran del MOTOR, que V6-19 no reclama y que no puede depender del verificador"
falla_si:
  - "la orden vuelve a censar un conjunto distinto del que mide el veredicto, con lo que una CLI de diagnostico contradiria al instrumento que diagnostica"
  - "el veredicto se ensancha al runtime entero y obliga al motor a importar su direccionamiento por contenido desde el verificador"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/escenario_e2e_f6.py"
estado: prueba-superada
evidencia: "evidencia/e2e-f6-salida.txt"
```

```yaml ads:escenario
id: T364
nombre: Los cinco puntos ejecutables publican su procedencia con una orden propia
cubre: ["ADJ-M2", "E-10", "g.15", "V6-11"]
dado:
  - "los cinco llevan el comentario E-10 la PROCEDENCIA se PUBLICA y calculan su procedencia"
  - "medido en las cinco tablas ORDENES, solo ads_admision.py tenia una orden que la publicase"
cuando: ["se ejecuta la orden procedencia en cada punto ejecutable, en un proceso real, y el conjunto se DERIVA del disco"]
entonces:
  - "los cinco salen con cero y publican de donde sale cada modulo del aparato y cuantas entradas del lanzador se retiraron"
  - "ninguno exige un --repo para responder de donde sale, porque preguntar por el aparato no puede depender del arbol juzgado"
falla_si:
  - "un punto ejecutable declara que publica su procedencia y no tiene orden que la publique"
  - "un punto ejecutable nuevo entra en el runtime sin la orden, y el conjunto derivado del disco lo cuenta igual"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/escenario_e2e_f6.py"
estado: prueba-superada
evidencia: "evidencia/e2e-f6-salida.txt"
```

```yaml ads:escenario
id: T365
nombre: arboles esta en los dos censos y sus dos sedes lo dicen
cubre: ["ADJ-M11", "V6-04", "V6-15", "V6-19", "S1-01"]
dado:
  - "versiones.py y CONTRATO-ARBOLES-ADVERSARIALES.md afirmaban que arboles no esta entre los paquetes del censo"
  - "el codigo declara PAQUETES_DEL_VERIFICADOR con arboles dentro, y el censo de lecturas deriva sus paquetes del disco"
cuando: ["se ejecuta el censo de los dos ambitos y se leen las dos sedes documentales"]
entonces:
  - "arboles esta en el censo de formulas y en el de lecturas, y la via historica esta acotada por paquete y modulo con su motivo"
  - "ninguna de las dos sedes afirma que el paquete quede fuera del censo"
falla_si:
  - "arboles sale de cualquiera de los dos censos, con lo que una lectura insegura nueva en ese paquete seria invisible"
  - "una de las dos sedes vuelve a afirmar que el paquete no esta entre los del censo"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/escenario_e2e_f6.py"
estado: prueba-superada
evidencia: "evidencia/e2e-f6-salida.txt"
```
