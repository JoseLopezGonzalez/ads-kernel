# `F6` · MATRIZ DEL CIERRE FINAL · `G-01`…`G-08` y `D-01`…`D-05`

**Qué es.** La clasificación de los trece defectos que el gate del 2026-09-05 dejó
REGISTRADOS y NO APLICADOS, más los dos que no cambian de clase. **Se escribe ANTES de editar
una sola línea**, y su función es que la disposición de cada uno sea una decisión declarada y
no un residuo de lo que se acabó tocando.

**De dónde sale.** Del registro íntegro del gate —
[`gate-definitivo/00-REGISTRO-DEL-GATE.md`](gate-definitivo/00-REGISTRO-DEL-GATE.md)—, leído
entero: los hallazgos `R1-H01`…`R1-H07` del revisor 1, `H-1`…`H-8` del revisor 2 y
`HALLAZGO 0`…`HALLAZGO 12` del revisor 3. Donde dos revisores midieron lo mismo por caminos
distintos, se dice.

**Regla que gobierna esta matriz:** se reproduce cada hecho antes de corregirlo · lo que no
reproduzca se adjudica técnicamente y no se «corrige» a ciegas · **ningún interno se convierte
en externo** · `E-17` y `E-18` conservan su clase.

---

## 1 · Los ocho `G`

| id | sede | hecho reproducido | causa de CLASE | remedio | propietario | prueba capaz de fallar |
|---|---|---|---|---|---|---|
| **`G-01`** | el manifiesto del gate anterior | asigna a `REV-2` el tramo `11907-12153` de un fichero de **12152** líneas, y deja **1-94** sin asignar. La resta quedó en 1 línea inexistente y **el gate cayó por eso** | el final del fichero se **escribió**, no se derivó del blob | generar el manifiesto MECÁNICAMENTE: `N` sale del blob, y se exige `unión(rangos) = [1,N]` sin huecos, sin solapes y sin `N+1` | el COORDINADOR | preflight que rechace `N+1`, hueco, solape y `1-94` sin asignar |
| **`G-02`** | `comprobar-cobertura-de-gate.py:205` y `:267` | `{f["ruta"]: f for f in fuentes}` colapsa varias entradas del mismo fichero: **sólo sobrevive la última**. `REV-2` declaró leídas 246 de 4 600 líneas de `11-ARQ` y la salida salió **byte a byte idéntica** a su lectura honesta. `REV-1` midió 34 922 de 40 630; `REV-3`, 46 649 de 47 534 | indexar por RUTA una relación que es **(ruta, rango)** | indexar por `(ruta, inicio, fin, revisor)` | el COORDINADOR | los diez casos del §3 del encargo, cada uno con su sabotaje |
| **`G-03`** | los 37 puntos con prólogo `E-10` · `raiz-externa/{verificador,instalar}.py` · `validadores/huella.py` | `site.py` importa `sitecustomize` **antes** de que la primera sentencia del prólogo purgue `sys.path`. Con gancho, `verificador.py instalacion` devuelve `{"ok": true, "alteradas": []}` con **código 0** sobre una instalación con código inyectado, y la huella anclada pasa a un valor fabricado | la purga vive DENTRO del programa: llega tarde por construcción | aislar **ANTES de inicializar el intérprete** (`-I -S -E`, entorno mínimo, intérprete y ruta verificados) **y** autocomprobar las primitivas contra vector conocido | `PLT` construye · `SIS` define conformidad | los doce ataques del §4, con el `sitecustomize` demostrando que **llega** en la versión vulnerable y **no llega** por la vía oficial |
| **`G-04`** | `runtime/dispatcher.py`, transición `runtime.seleccion.postergada` | `b.12` dice «DSP informa de la inanición. **No cambia la prioridad. Nunca**», citado literal en TRES sedes, y sumar 10 a la prioridad en esa transición pasa **DOCE baterías en verde** | la prohibición es prosa: no hay invariante que la ejecute | invariante ejecutable: **imposible confirmar** una transición de DSP que mueva la prioridad | autoría de `F6` | los diez casos del §5, incluido el sabotaje exacto que pasaba doce baterías |
| **`G-05`** | `validadores.yaml`, componente `universo-obligatorio` | su evidencia ejecuta **sólo** `--autopruebas`, y el modo productivo `--rutas` **falla cerrado con `EXIT=2`** sobre la propia candidata. `36/36 en verde` era compatible con un derivador muerto | la evidencia cubre el autotest y no el producto | ejecutar y publicar **todos** los modos productivos, con comando, exit, digest y cardinales | `SIS` | modo productivo rojo con autopruebas verdes → la evidencia debe caer |
| **`G-06`** | `validadores.yaml`, 14 componentes | `firma_de_exito: '\d+ …'` casa con **`0`**: una evidencia que declare `0 infracciones detectadas · 0 NO detectadas` pasa la comprobación | la firma mide la forma del número, no su mínimo | mínimo real por validador, derivado del contrato, distinguiendo «cero legítimo» de «no corrió nada» | `PLT` | el ataque `0 · 0` con corpus de negativos no vacío |
| **`G-07`** | `comprobar-cobertura-de-gate.py`, bloque `DECISIÓN · OBLIGATORIO se DERIVA DEL ÁRBOL` | el bloque declara derivarlo con `git diff`; el código hace `set(manifiesto.get("modificadas") or [])` y **el fichero no importa `subprocess`**. Un manifiesto con UNA ruta y UNA línea leída satisface las cuatro restas | el comentario y el código dicen cosas distintas | derivar de verdad con `git diff --name-status -M -C -z` entre base y candidata; el manifiesto **contrasta**, no define | el COORDINADOR | los diez casos del §8, incluidos renombrado, copia y ruta no ASCII |
| **`G-08`** | `test_contencion.py` · `T216` | la prueba que exige que el bisnieto **sobreviva** a `killpg` falla bajo carga porque el bisnieto puede no existir a tiempo. Falla al lado seguro —rojo— pero **no es determinista**, y la línea base declara «determinismo byte a byte» | espera temporal en vez de protocolo de preparación | protocolo observable: hijo, nieto y bisnieto **confirman que existen y están preparados** antes del `killpg` | `PLT` | distinguir «muerto por contención» de «nunca creado», y repetir bajo carga |

## 2 · Las cinco deudas `D`

| id | sede | hecho | remedio | propietario |
|---|---|---|---|---|
| **`D-01`** | 21-22 baterías de `runtime/pruebas/` sin el prólogo, y `registrar_evidencia.py:212` con `subprocess.run` **sin `env=`** | `E-10` no alcanza al canal que PRODUCE la evidencia. La exclusión `motivo: "bateria"` del inventario las eximía por su zona | o el prólogo entra en las baterías, o el runner sanea el entorno de sus hijos y lo publica en la cabecera de cada evidencia. **Lo segundo cierra las 21 de una vez; lo primero cierra también la ejecución suelta** | `PLT` |
| **`D-02`** | nueve escenarios | sólo pueden ascender de estado reescribiendo cuatro baterías ajenas | cada escenario con contrato, ejecutor, evidencia, transición, condición de ascenso, negativo, digest y vínculo al SHA. **Las baterías observan; no son el mecanismo** | `SIS` · `PLT` |
| **`D-03`** | `docs/canonico/FUENTES-CANONICAS.yml`, clase `AUTORIDAD_SUPERIOR` | mezcla la sede append-only con material aprobado que se cambia **por enmienda**. Medido: aplicarles el mismo régimen da **cuatro rojos falsos sobre árbol intacto** | separar las clases y dar a cada una su regla de integridad, sin abrir falsos verdes | `SIS` |
| **`D-04`** | componente `C` del universo | `C2`/`C4`/`C5` se seleccionan con un patrón escrito y **ninguna sede canónica declara por qué** | sede derivable única, o retirar la clasificación si otra familia ya la absorbe. **No inventar contenido** | `PLT` · `SIS` |
| **`D-05`** | el canal «la evidencia es la confirmada en `HEAD`» | implementado y **sin sabotaje mecanizado**: `comprobar_negativos` copia el corpus sin `.git` | mecanizar los ocho ataques del §13, con control sano que demuestre blob, commit, tree, digest y árbol limpio | `PLT` |

## 3 · Lo que NO cambia de clase

| id | clase | disposición |
|---|---|---|
| **`E-17`** | **DEUDA EXTERNA** | custodia productiva de claves. Propietario el Owner, mecanismo previsto, condición de cierre, y **una clave efímera NO la satisface**. No bloquea la certificación técnica; bloquea toda afirmación de custodia productiva |
| **`E-18`** | **LIMITACIÓN DE ANFITRIÓN** | `cgroup v2` presente y **no ejercitable** aquí; identidad diferenciada **ejercida** en contenedor; backend fuerte probado; el débil no contiene `setsid`; sin backend fuerte, fallo cerrado. **Ninguna afirmación universal** |

## 4 · Los que el gate encontró y este encargo NO enumera

Se registran porque el gate los publicó y callarlos sería elegir qué se corrige por omisión.
**Se corrigen los que caen dentro de la clase de un `G` o una `D`; el resto queda declarado.**

```text
R1-H03  «sin tocar el estado en modo PLAN» es falso en la sede que un implementador lee
R1-H05  `C4` plural lo sostiene UNA sola batería — cobertura existente y específica
R1-H06  «trece campos» donde hay catorce, en las tres sedes definitorias
H-5     una evidencia ausente produce una TRAZA de Python y no un veredicto
H-6     la equivalencia de `T330` publicada en el README de la raíz externa no describe el árbol
HALL.1  `ZONAS_SIN_BARRIDO` rotula `^docs/evolucion/` como «historia inmutable» y ahí viven
        32 obligaciones vivas: la misma negación da ROJO en `docs/canonico/` y VERDE aquí
HALL.2  `_seccion_19()` hace `return texto` y trunca el cuerpo a 4000 caracteres: vía NUEVA de
        encogimiento silencioso del universo, `TOTAL 57 · EXIT=0`
HALL.6  el diagnóstico del append-only nombra UNA entrada y agrega el resto
HALL.7  `D112` no abre epígrafe propio — cuarta vez
HALL.8  la VERSIÓN del kernel no se movió en 188 ficheros de cambio
HALL.10 cifra escrita a mano que la evidencia del propio árbol desmiente
HALL.11 las tres pruebas que cubren `ADJ-G1` no están ejecutadas
HALL.12 nota caducada sobre `CONTRATO 3`
```

**`HALLAZGO 1` y `HALLAZGO 2` son de la clase de `G-05`** —un instrumento del universo que no
mide lo que dice— y se corrigen con él. **`HALLAZGO 3` es `D-01`.** **`HALLAZGO 4` es `G-02`**
y **`HALLAZGO 5` es `G-07`**, medidos por dos revisores distintos sin verse.

---

## §5 · ESTADO FINAL DE CADA FILA, cerrada la pasada de corrección

Esta sección se escribe **al terminar** y no antes: la columna que importa es la última, y
una matriz que se rellena por adelantado no mide, promete.

| id | estado final | dónde se comprueba |
|---|---|---|
| **`G-01`** | **CERRADO** · el lector del manifiesto valida el rango contra las líneas reales del árbol y falla cerrado nombrando el defecto que hundió el gate del 2026-09-05 | `comprobar-cobertura-de-gate.py --autopruebas` · 23 controles · 0 sin detectar |
| **`G-02`** | **CERRADO** · la clave de asignación pasa a ser `(ruta, desde, hasta, revisor)`; dos tramos distintos del mismo fichero dejan de pisarse, y una asignación repetida es fallo | ídem |
| **`G-03`** | **CERRADO** por `A1` · la guarda cambia el MOMENTO —`-I -S -E` antes de que `sitecustomize` exista— y alcanza a **56 de 56** puntos ejecutables del inventario derivado, con mecanismo idéntico byte a byte | `T380`–`T397` · `test_integridad_y_evidencia.py` |
| **`G-04`** | **CERRADO** por `A2` · la invariante de `b.12` se interpone en la PUERTA y en el `AlmacenVigilado`; la prioridad de un paquete existente no se mueve en ninguna transición del runtime. **Límite declarado**: un proceso que abra su propio `estado.Almacen` escribe por el motor, y esa tercera capa queda como PETICIÓN escrita en la sede, no como verde | `T400`–`T419` · docstring de `runtime/estado_util.py` |
| **`G-05`** | **CERRADO** · los dos modos del derivador del universo que nadie ejecutaba entran en `validadores.yaml` como `universo-obligaciones` y `universo-rutas`; `HALLAZGO 1` y `HALLAZGO 2` son de esta clase y caen con ella | `validadores.yaml`, cuyo cardinal NO se copia aquí: se deriva con `grep -c '^  - id: '` sobre el fichero, que es la lección de `J-07` y de `HALL.10` |
| **`G-06`** | **CERRADO** · catorce firmas de éxito pasan de `\d+` a `[1-9]\d*`: «0 superadas» deja de casar con la firma que declara el éxito | ídem |
| **`G-07`** | **CERRADO** · las rutas modificadas se DERIVAN del árbol (`git diff --name-status -M -C -z`, con las dos rutas de cada `R`/`C`), y la lectura íntegra se mide por UNIÓN de tramos | `comprobar-cobertura-de-gate.py --autopruebas` |
| **`G-08`** | **CERRADO** por `A2` | ver su informe |
| **`D-01`** | **CERRADO** por `A1` · el prólogo y la guarda entran en las 21 baterías, el runner lanza a sus hijos aislados y **publica la garantía en la cabecera** de cada evidencia, y `comprobar_evidencia` la exige. La exclusión por zona `motivo: "bateria"` se retiró | `T380`–`T397` |
| **`D-02`** | **CERRADO** · los doce escenarios que no tenían veredicto nominal lo tienen: seis por docstring en `test_workspace.py`, `T168` y `T181` por `ResultadoRepartido` —un montaje, tres veredictos—, y `T180`, `T193`, `T225` y `T301` por línea propia al cierre de su ejecutable. `T181` gana además la **sonda de derivación** que su promesa exigía: una enmienda que el arranque no puede conocer, sembrada en la copia | negativos `N168` y `N181`, cada uno rojo por su motivo |
| **`D-03`** | **CERRADO** · clase `APROBADA_POR_ENMIENDA` separada de `AUTORIDAD_SUPERIOR`, con su régimen propio en las tres sedes que la juzgan | `ads_lint` 0 errores · perímetro · `FUENTES-CANONICAS.yml` |
| **`D-04`** | **CERRADO** · el componente `C` deja de derivarse del patrón `^(C[245])-` escrito en el instrumento que mide, y pasa a leerse del párrafo «Universo de la resta» de `01-MATRIZ-DE-COMPLETITUD-F6.md`. **Se buscó y se descartó la alternativa**: `11-ARQ` §15.7 recorre `C1`–`C7` y declara con ejecución `F6` pendiente `C2`, `C5`, `C6` y `C7` —**no `C4`**—, así que no es la sede de esta selección y hacerla pasar por tal habría cambiado el universo inventando el motivo | dos sabotajes nuevos: la sede deja de nombrarlos → falla cerrado; la sede nombra uno más → el universo lo recoge |
| **`D-05`** | **CERRADO, y encontró un hueco abierto** · los ocho ataques se mecanizan sobre un repositorio Git REAL, con control sano que demuestra blob, commit, tree, digest y árbol limpio. `T425` salió **rojo del canal, no de la prueba**: la guarda `if not (antes and despues): continue` dejaba pasar en VERDE vaciar la evidencia o renombrar el escenario, que es la vía más limpia de retirar un dictamen. Corregido | `T420`–`T428` · 9 casos |
| **`E-17`** | **EXTERNO, sin cambio de clase** | — |
| **`E-18`** | **limitación del anfitrión, sin cambio de clase** | — |

**Peticiones cerradas de los agentes.** `A1` pidió declarar `aislamiento_de_arranque.py` en
`validadores.yaml` (hecho), aplicar la guarda a los cuatro ejecutables de
`docs/evolucion/verificacion/` **y retirar entonces la declaración** (hecho: la zona exenta ya
no existe y `PUNTOS_SIN_GUARDA_ADMITIDOS` es **0**; el diccionario se deja vacío a propósito
para que su prueba siga midiendo las dos mitades). `A2` pidió promover `T400`–`T419` tras
regenerar la evidencia (hecho) y una tercera capa de la invariante de `G-04` en
`estado/motor.py` (**NO hecha**, y dicho por qué: `estado/` no importa de `runtime/`, y la
inversión de zona que exigiría es una decisión de diseño fuera de la lista finita de este
encargo; el límite queda **declarado en la sede**, que es donde un lector lo encuentra).

---

## §6 · LA AUDITORÍA INDEPENDIENTE, Y LO QUE ENCONTRÓ

El auditor no escribió una línea de código y no tocó el repositorio: montó sus sabotajes
sobre una copia, y al cerrar comprobó que la huella seguía siendo la misma y que el árbol
sólo tenía los cambios del coordinador. **Encontró once hallazgos, y cuatro de ellos eran
graves.** Se aplican los once en la pasada única de corrección, y cada uno queda con un
sabotaje mecanizado que lo pondría rojo otra vez.

**La clase que el auditor nombró por encima de los casos, y que es la que importa:** *en
cuatro sitios distintos de esta pasada, lo que la prosa promete no es lo que el código
ejecuta.* «Cada fallo se apunta en el escenario cuya promesa rompe» —22 de 36 no lo hacían—;
«su contenido lo escribió una EJECUCIÓN» —nada lo comprobaba—; «las rutas se derivan del
árbol» —ninguna prueba lo ejercía—; «el canal lo DICE» —no lo decía—. En un corpus donde la
prosa **es** la norma, ésa es la clase que más caro sale.

| # | hallazgo | qué se ha hecho | prueba que lo mide |
|---|---|---|---|
| **1** GRAVE | `ResultadoRepartido` publicaba **`T168 SUPERADA` y `T181 SUPERADA` sobre un árbol donde el arranque no producía nada**: el fallo que aborta hacía `continue` y las comprobaciones de los derivados no se ejecutaban. 22 de los 36 sitios de fallo no declaraban destinatario | un derivado tiene **TRES** estados y el tercero es `NO EJERCIDA`; se cuenta cuántas veces se ejerció cada uno y cero no puede ser verde. Y `para` pasa a ser **posicional y obligatorio**: un sitio de fallo nuevo no puede nacer sin decidir a quién rompe | `N168b` (el arranque no produce nada) y `N181b` (el montaje se aborta a media altura y `T181` no llega a ejercerse) — hacen falta los dos, porque son los dos caminos |
| **2** GRAVE | la exención de `T360` la concedía **el rótulo**: tres tildes invertidas y la palabra `console`, escritas por el mismo autor cuya afirmación se juzga. Una cerca vacía convertía el rojo en verde | la exención **se gana**: el bloque tiene que llevar línea de orden (`$ `, `> `, `# orden:`) o de salida de máquina (`EXIT=`, `Tnnn SUPERADA`, cierre de recuento). Y **deja rastro contado**: `T360` publica cuántas líneas eximió y en qué sedes | `NG3g`, con la cerca vacía exacta del auditor. Y se dice lo que NO hace: no demuestra procedencia, sube su precio |
| **3** GRAVE | `G-07` **no se ejercía**: los 23 controles llevaban `derivacion: declarada-sin-arbol` y no invocaban `git` **ni una vez** —medido con un `git` instrumentado en el `PATH`—. Más dos puertas traseras: el manifiesto elegía el repositorio, y la vía declarada prometía publicarse y no publicaba nada | tres controles nuevos sobre un **repositorio Git real**: `M`, `A`, `D`, renombrado, **copia con su fuente modificada** —que es la condición que `git` necesita para emitir `C100`—, ruta no ASCII y ruta con salto de línea. El `repositorio` deja de elegirlo el manifiesto; `base == candidata` falla cerrado; y **el origen del conjunto se imprime siempre**, lo primero del informe | 26 controles · 0 sin detectar, y la sonda del auditor mide ahora **8 llamadas a `git`**, una de ellas el `diff --name-status` |
| **4** GRAVE | `D-05` tenía un **noveno ataque abierto**: borrar el fichero era verde mientras vaciarlo era rojo. Y el canal era **mudo**: `r.nota` se calculaba y se descartaba, así que `T427` y `T428` asertaban sobre algo que ningún lector recibía | borrar se juzga igual que vaciar, y se cuenta. Y la nota se parte en dos: **si el canal se ejerció o no** se publica siempre —depende del árbol, no del reloj—; el detalle volátil sigue fuera, que era el motivo correcto de la decisión anterior | `T429`, y la línea `contraste contra el blob de HEAD: EJERCIDO` en la evidencia |
| **5** SERIO | «56 de 56» era 56 sobre un inventario que **no veía una clase entera**: el auditor coló un `.py` sin shebang, sin `main` y sin `sys.exit` que imprime desde el nivel superior, y quedó clasificado `biblioteca-suelta` | la carga se invierte: es punto ejecutable **todo `.py` que hace trabajo al importarse**. Se eximen sólo el prólogo y la fontanería de `sys.path`, con su motivo. Entran los dos catálogos de negativos, y **los dos llevan ya la guarda** | `T380` monta el fichero del auditor en un temporal y exige que entre, **y su control**: un módulo que sólo declara tiene que quedar fuera, o la regla sería «todo `.py` es un punto» |
| **6** SERIO | la sede que `D-04` puso a gobernar el universo **no estaba dentro del universo**: `--rutas \| grep -c docs/f6` daba `0`. El remedio movió la decisión de dentro del perímetro auditado a fuera | la sede entra en el `ENCARGO`, y una guarda exige que siga entrando: **ninguna sede gobierna el universo obligatorio desde fuera de él** | sabotaje: se le quita la fila al `ENCARGO` y falla cerrado |
| **7** MODERADO | el ancla de `D-04` dependía de **dónde caía el salto de línea**: moverlo una palabra tumbaba tres validadores con `EXIT=2`, y el arreglo barato ante eso es relajar la expresión —así se desanclan las sedes— | el ancla es el **contenido normalizado**: el espacio en blanco se colapsa antes de buscar | sabotaje que repliega el párrafo **y** quita un contrato, y exige que el motivo siga siendo `EL UNIVERSO HA ENCOGIDO` y no un ancla rota |
| **8** MODERADO | `publicaria_veredicto` medía **una subcadena sobre el fichero entero**: un comentario con `"T168"` bastaba para vaciar el censo de `D-02`, incluida la explicación de por qué se vació | la respuesta firme la da la **evidencia**, que es un hecho; y la predicción sobre la fuente se hace sobre el **árbol sintáctico** —el identificador dentro de una cadena, no en un comentario— | medido: sólo un comentario → `False`; dentro de una cadena → `True`. Y se declara lo que la predicción **no** puede hacer: distinguir una cadena viva de una muerta |
| **9** MODERADO | la garantía de aislamiento de `D-01` es **una declaración sobre sí misma**: reescribirla a mano en una evidencia confirmada no cambia ningún veredicto | **no se finge que se cierra.** El alcance queda escrito donde lo encuentra quien lee la comprobación: funciona contra la regresión, no contra el editor deliberado. La prueba de procedencia de verdad —un digest calculado por el hijo— es otro aparato y queda como PETICIÓN | — |
| **10** MENOR | «48 componentes» donde había 49: `HALL.10` reproducido **dentro de la matriz que registra su corrección** | el cardinal se **retira**, y la fila remite a la derivación. No se sustituye un número a mano por otro número a mano | — |
| **11** MENOR | el patrón de `D-03` llevaba el rango `E[3-9]` escrito a mano: una enmienda `E10` caería sola a `DERIVADA` | pasa a `E[0-9]+`, sin tope: quien decide qué enmiendas hay es el árbol | `validar-fuentes-canonicas.py` · 0 fallos |

**Lo que el auditor dio por bien cerrado sin reservas**, tras atacarlo: `G-01`, `G-02`,
`G-04` —reinsertó el sabotaje exacto de `R1-H02` y salió `[PRIORIDAD_INMUTABLE] … de 50 a
60`—, `G-06`, y la sonda de derivación de `T181`, cuyo escape al árbol real comprobó que es
imposible. Y el control sano de `D-05`: «*eso está bien hecho y no es un decorado*».

**Lo que el auditor declaró NO haber podido comprobar** queda registrado tal cual, porque un
alcance sin declarar es el defecto que este proyecto ha visto más veces: la corrida completa
de los 38 validadores por `registrar_evidencia.py` —publicar evidencia escribe en el árbol y
le estaba prohibido—; el catálogo de mutaciones uno a uno; `G-08` bajo carga; que la
clasificación de los trece defectos sea completa respecto del registro del gate; y los doce
ataques de `T380`-`T399` por dentro.
