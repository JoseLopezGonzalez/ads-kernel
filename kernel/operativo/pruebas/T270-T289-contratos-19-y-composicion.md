# T270–T289 — las CUATRO obligaciones de fase `F6` de `11-ARQ` §19

**Qué cierran.** Las cuatro obligaciones que la sección §19 del documento de arquitectura
declara con fase `F6`, propietario y condición de cierre, y que hasta esta entrega estaban
**sin cerrar**. Su sede es `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` §19: el
subapartado «Los censos escritos a mano, derivados — el contrato F6 que cierra nueve
hallazgos» y la ficha `D104`. **Esa sede NO se enlaza desde aquí**: es historia del kernel,
no viaja al proyecto instalado, y un enlace roto en el proyecto instalado es el defecto que
`E5` destapó. Se cita en texto plano.

**Cuatro obligaciones, y ninguna se absorbe bajo un identificador común.** Cada una tiene
su condición de cierre literal, su código y su prueba, y aquí se enumeran una a una:

```text
CONTRATO 1     el censo `AFIRMACIONES` deja de ser una LISTA LITERAL y la cobertura de
               sedes se DESCUBRE barriendo, en dígitos y en letra
               → comprobar_recuentos.py · T151 (cifra) y T270 (cobertura derivada)

CONTRATO 1bis  los `ads:perfil-agente` de `C2` dejan de existir sólo en prosa: se cuentan
               como los demás bloques tipados y la cifra se publica
               → comprobar_recuentos.py · T271

CONTRATO 2     el ALCANCE de `T152` deja de ser dos ficheros escritos a mano y pasa a ser
               TODA SEDE QUE PUBLIQUE VERSIÓN, descubierta por barrido
               → comprobar_versiones.py · T152 (versión) y T272 (alcance derivado)

D104           los pares `<CAP>:revision` se MATERIALIZAN en `recorrido/01-PROCESOS.md` y
               en `circuitos/`, y el gate de composición los comprueba con el error
               `composicion-incompleta`, que NO es un aviso
               → comprobar_composicion_procesos.py · T273, T274, T275 y T276
```

**Ninguna comprueba que un texto esté escrito: comprueban la PROPIEDAD.** `T270`, `T272`,
`T274` y `T275` fabrican entradas sintéticas —una sede que no existe, un proceso que no
existe— y ejercen la derivación contra ellas. Reintroducir el defecto las pone en rojo.

> **Todas llevan prueba negativa, y son SABOTAJES ejecutados.** Catorce infracciones
> deliberadas en [`../validadores/negativos_contratos19.py`](../validadores/negativos_contratos19.py),
> incorporadas por nombre al catálogo único de
> [`../validadores/comprobar_negativos.py`](../validadores/comprobar_negativos.py): `N270`,
> `N270b`, `N270c`, `N271`, `N272`, `N272b`, `N273`, `N273b`, `N273c`, `N273d`, `N273e`,
> `N273f`, `N275` y `N276`. Cada una se aplica sobre una COPIA temporal del repositorio —el
> corpus real no se toca— y exige que la prueba señalada FALLE **por el motivo esperado**.

> **La lectura del contraejemplo de `D104`, dicha explícitamente.** `D104` prescribe que
> sobre el árbol de HOY la prueba devuelva FALLIDA nombrando `proceso:DEP` →
> `SEG:revision` AUSENTE. Eso describe el árbol **ANTES** de que `F6` materialice: había
> cero instancias de `:revision` en todo `kernel/operativo/`. `F6` materializa, `T273` queda
> en VERDE **sobre el árbol materializado**, y el contraejemplo se CONSERVA como sabotaje
> `N273`: retirar `SEG:revision` de `DEP` —dejando intactas las de los otros cuatro
> procesos del catálogo— vuelve a producir exactamente ese diagnóstico.

**La grafía.** Todo el aparato de §19, `D92`, `D98`, `D103` y `D104` escribe `revision`
**sin tilde**, y ésa es la canónica que el kernel usa. `b.16` L836 escribe `<CAP>:revisión`
con tilde en su única aparición normativa; es material APROBADO de fase `F5` y no se
enmienda desde aquí. La discrepancia está registrada como `E5-3`.

```yaml ads:escenario
id: T270
nombre: La cobertura de sedes del censo se descubre barriendo, y no se enumera
cubre: ["CONTRATO 1", "J-05", "K-11", "A-24", "comprobar_recuentos AFIRMACIONES"]
dado:
  - "el censo declara REGLAS de (patrón de sede, derivación) y ninguna nombra una ruta"
  - "el ámbito vivo son patrones, y cada exclusión lleva su motivo escrito"
cuando:
  - "se fabrica en un directorio temporal una sede que no existe en el corpus, con una afirmación falsa sobre un objeto censable"
  - "se barre ese directorio con el mismo motor que ejecuta T151"
entonces:
  - "la sede nueva queda cubierta el día que nace, sin tocar el validador"
  - "la misma sede con la cifra verdadera no produce ningún fallo"
falla_si:
  - "la cobertura vuelve a ser una lista literal de rutas"
  - "una sede nueva con una cifra falsa pasa en verde"
  - "el barrido denuncia también la cifra verdadera, con lo que no distinguiría nada"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_recuentos.py"
estado: prueba-superada
evidencia: "evidencia/recuentos-salida.txt"
```

```yaml ads:escenario
id: T271
nombre: Todo tipo canónico tiene recuento derivado y publicado, incluidos los perfiles de agente
cubre: ["CONTRATO 1bis", "N-04", "C2-AGENTES-Y-MODELOS", "RECUENTOS-generado"]
dado:
  - "el conjunto de tipos canónicos se deriva de los esquemas del árbol y no de una lista"
  - "C2 declara sus bloques ads:perfil-agente y nadie los contaba"
cuando:
  - "se derivan los recuentos y se contrastan contra la tabla publicada"
entonces:
  - "cada tipo declarado por un esquema tiene una cifra derivada que coincide con sus bloques"
  - "la cifra de perfiles de agente existe y está publicada, no sólo en prosa"
falla_si:
  - "un tipo canónico nuevo queda sin censo"
  - "una cifra derivada no llega a la tabla publicada"
  - "entra un perfil nuevo en C2 y el recuento no se mueve solo"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_recuentos.py"
estado: prueba-superada
evidencia: "evidencia/recuentos-salida.txt"
```

```yaml ads:escenario
id: T272
nombre: El alcance de T152 se descubre por barrido y cada sede tiene remedio declarado
cubre: ["CONTRATO 2", "J-06", "K-07", "A-12", "kernel/VERSIONES.md regla 5"]
dado:
  - "la versión vigente de cada artefacto se resuelve en kernel/VERSIONES.md, su sede única"
  - "las clases de remedio se declaran por patrón de sede, con su fase"
cuando:
  - "se fabrica en un directorio temporal una sede nueva que publica una versión del kernel que no es la vigente"
  - "se barre la capa documental buscando versiones obsoletas"
entonces:
  - "la sede nueva se detecta sin modificar el validador"
  - "la misma sede con la versión vigente no produce ningún fallo"
  - "toda sede con versión obsoleta tiene una clase de remedio con propietario y fase"
falla_si:
  - "el alcance vuelve a ser los dos ficheros escritos a mano"
  - "una sede con versión obsoleta se queda sin clase de remedio declarada"
  - "la sede única publica dos versiones distintas para el mismo artefacto"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_versiones.py"
estado: prueba-superada
evidencia: "evidencia/versiones-salida.txt"
```

```yaml ads:escenario
id: T273
nombre: Todo par del catálogo estático de D104 tiene su CAP revision, heredada y posterior a su ancla
cubre: ["D104", "O-01", "M-01", "N-01", "N-02", "recorrido/01-PROCESOS", "b.16 participación doble"]
dado:
  - "el conjunto vigilado se deriva de las fichas que declaran la doble participación de b.16"
  - "el discriminante estático/por item es la pertenencia al conjunto de las quince, por igualdad"
  - "el ancla es la obligatoria de VER si el proceso la declara, y si no su última obligatoria"
cuando:
  - "se deriva el catálogo estático del árbol y se contrasta contra las participaciones declaradas"
entonces:
  - "cada par exigido tiene su participación CAP revision instanciada"
  - "la instancia está colocada después del ancla derivada de su proceso"
  - "la instancia hereda activación, obligatoriedad y autoridad de retirada de su origen"
  - "ninguna instancia existe sin una participación del catálogo que la exija"
falla_si:
  - "un proceso del catálogo se queda sin la revisión que su participación exige"
  - "la revisión de DEP se vuelve retirable, siendo irretirable su origen"
  - "una revisión se coloca antes de su ancla"
  - "una revisión condicional se activa con una condición distinta de la de su origen"
  - "la ficha de una capacidad deja de declarar la doble participación y el catálogo no se mueve"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_composicion_procesos.py"
estado: prueba-fallida
evidencia: "evidencia/composicion-procesos-salida.txt"
```

```yaml ads:escenario
id: T274
nombre: La regla POR ITEM se resuelve con el item delante, y nunca por declaración
cubre: ["D104 salida B", "M-01", "N-01", "proceso:AUD", "proceso:DIR", "proceso:DEF"]
dado:
  - "tres procesos del árbol resultan de propietario POR ITEM por el discriminante estructural"
  - "el conjunto exigido es la unión del propietario efectivo y de los condicionales activados"
cuando:
  - "se ejerce la regla contra cada proceso POR ITEM del árbol, con propietario vigilado, con propietario ajeno y con sus condicionales activos y sin ellos"
entonces:
  - "ningún proceso POR ITEM aporta par al catálogo estático"
  - "con propietario ajeno y sin condicionales activos el item pasa vacío"
  - "con propietario vigilado el item exige su par por la vía 1"
  - "con todos sus condicionales vigilados activos el conjunto exigido es la unión, y puede ser los dos"
falla_si:
  - "un proceso POR ITEM emite par estático sin el item delante"
  - "se declara que un proceso pasa vacío sin resolver su item"
  - "un item que activa dos condicionales vigilados exige uno solo"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_composicion_procesos.py"
estado: prueba-superada
evidencia: "evidencia/composicion-procesos-salida.txt"
```

```yaml ads:escenario
id: T275
nombre: Los fixtures de D104 se ejecutan en cada corrida y su censo coincide con su sede
cubre: ["D104 censo de fixtures", "Q-12", "Q-10", "M-04"]
dado:
  - "la batería declara un fixture por vía, por combinación de proceso POR ITEM y por modo de fallo cerrado"
  - "la cifra del censo se publica una sola vez, en la sede de D104"
cuando:
  - "se ejecutan todos los fixtures y se cuenta cuántos son"
  - "se lee de su sede la cifra publicada y se contrasta contra la contada"
entonces:
  - "todos los fixtures pasan"
  - "el número de fixtures ejecutados es el que la sede publica"
falla_si:
  - "un fixture deja de pasar"
  - "la cifra publicada deja de ser la que la batería corre, y el diagnóstico no nombra sede, responsable y remedio"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_composicion_procesos.py"
estado: prueba-superada
evidencia: "evidencia/composicion-procesos-salida.txt"
```

```yaml ads:escenario
id: T276
nombre: Los repartos por vía, procedencia y ancla derivan del árbol y no de una proyección escrita
cubre: ["D104 salida A", "Q-03", "Q-09", "Q-11", "Q-28"]
dado:
  - "las quince capacidades salen de los directorios del árbol"
  - "los tres repartos se publican una sola vez en la sede de D104"
cuando:
  - "se deriva el catálogo del árbol y se contrasta reparto a reparto contra la proyección publicada"
entonces:
  - "el reparto por vía derivado coincide con el publicado, vía a vía"
  - "el reparto por procedencia derivado coincide con el publicado, procedencia a procedencia"
  - "el ancla derivada de cada proceso coincide con la publicada, proceso a proceso"
falla_si:
  - "una proyección publica un total fijo distinto del derivado"
  - "el reparto por vía cambia sin que la proyección se mueva"
  - "el conjunto de las quince deja de derivarse de los directorios"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_composicion_procesos.py"
estado: prueba-superada
evidencia: "evidencia/composicion-procesos-salida.txt"
```

```yaml ads:escenario
id: T277
nombre: El universo obligatorio de F6 se deriva completo y no puede omitir una obligación en silencio
cubre: ["F6-H", "C-L.5 regla 1bis", "P-08", "CONTRATO 1", "CONTRATO 1bis", "CONTRATO 2", "D104"]
dado:
  - "el universo se lee de sus sedes normativas y no de una tabla escrita a mano"
  - "las cuatro obligaciones de fase F6 de la sección 19 son componente propio del universo"
cuando:
  - "se deriva el universo obligatorio y se cruza contra los escenarios, los validadores y los sabotajes del corpus"
entonces:
  - "las cuatro obligaciones de la sección 19 aparecen en el universo, una a una y con su identificador propio"
  - "cada obligación publica su implementación, su prueba capaz de fallar y su evidencia, o aparece en la resta que le corresponde"
  - "las tres restas se publican derivadas, aunque no estén vacías"
falla_si:
  - "una obligación de fase F6 queda fuera del universo sin que nada lo diga"
  - "una resta se publica escrita a mano en vez de derivada"
  - "el universo encoge y el derivador sale con código cero"
ejecucion: guion-manual
validador: "docs/evolucion/verificacion/derivar-universo-obligatorio.py"
estado: prueba-ejecutada
evidencia: "evidencia/universo-obligatorio-salida.txt"
```
