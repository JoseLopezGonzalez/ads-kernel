# CONTRATO · EL CICLO Y LOS CUATRO MACROCIRCUITOS

**Qué es.** El contrato derivado del macrobloque 3 de `F6`, cuya norma es `11-ARQ` §7.2,
§7.4, §8.0, §9.6 y §18 —`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, que no viaja al
proyecto instalado—, `b.16` en [`../recorrido/01-PROCESOS.md`](../recorrido/01-PROCESOS.md),
`b.14`, `C4`, `C5` y la taxonomía de entrada. Fija cómo se encuadra una entrada del Owner,
cómo se compone su ruta, cómo se materializa su equipo, cómo se planifica y despacha su
trabajo, cómo se aplican sus gates y sus handoffs, cómo cierra, cómo se continúa, y cómo los
cuatro macrocircuitos se ejecutan **como composiciones del mismo motor**.

**Qué NO es.** No es norma. No reformula `(g)` ni `b.16`: los diez procesos se DERIVAN de
sus bloques `ads:proceso` y no se copian; los gates se DERIVAN de los bloques `ads:gate` del
corpus y no se inventan; los handoffs se DERIVAN de `circuitos/` y de las cinco entregas que
§8.0 declara. Y no es un segundo sistema de estado: todo lo durable es una `Transicion`
sobre el `Almacen` de [`CONTRATO-ESTADO-DURABLE.md`](CONTRATO-ESTADO-DURABLE.md), y el alta
de trabajo pasa por `Runtime.crear_item` y `Runtime.crear_paquete` de
[`CONTRATO-RUNTIME-Y-DISPATCHER.md`](CONTRATO-RUNTIME-Y-DISPATCHER.md).

---

## 1 · Lo que el ciclo escribe, y dónde

```text
canonico/encuadres/<id>.json     el ENCUADRE: producto, clase de entrada, materia, fuentes
canonico/rutas/<id>.json         la RUTA compuesta: participantes con su vía y las NO activadas
canonico/equipos/<id>.json       el EQUIPO materializado por C4, con lo que quedó fuera
canonico/planes/<id>.json        el PLAN: qué paquete cubre qué obligación de qué capacidad
canonico/dictamenes/<id>.json    el DICTAMEN de un gate, con su entrada y su evidencia
canonico/handoffs/<id>.json      la ENTREGA de C5, con su acuse, su rechazo o su devolución
canonico/cierres/<id>.json       la salida del item: completado, bloqueado, pausado, escalado
canonico/derivaciones/<id>.json  el enlace durable entre un item derivado y su origen
canonico/cobertura/<id>.json     la celda de certificación INCORPORADA desde la FASE 0
canonico/autoridad/<id>.json     qué macrocircuito gobierna un producto, y en qué ejecución
canonico/macrocircuitos/<id>.json  cómo terminó cada uno, de forma INEQUÍVOCA
canonico/ordenes/<id>.json       las órdenes del Owner pendientes de consumir, con su base
canonico/derivados/<id>.json     un derivado con su `source_revision`, para regenerarlo
canonico/proyecciones/<id>.json  una proyección declarada, para validar su huella
```

Los cuatro dominios del corte 2 —`items`, `paquetes`, `leases`, `efectos`— **no cambian**, y
el objeto `paquete` conserva su vocabulario CERRADO: la correspondencia entre un paquete y la
capacidad de `b.16` que lo produce vive en `planes/`, no dentro del paquete.

**Vocabulario CERRADO del ciclo**, y ninguna otra palabra vale:

```text
MATERIAS               capacidad-ausente · expectativa-no-alcanzada ·
                       comportamiento-especificado-roto · incidente-en-uso-real ·
                       conocimiento-ausente · forma-interna-costosa · dependencia-externa ·
                       conclusion-sobre-lo-existente · direccion-ya-decidida ·
                       la-propia-fabrica
ESTADO DEL OBJETO      no-existe · existe · en-uso-real
VÍAS                   1 propietaria global · 2 obligatoria · 3 condicional · 4 item propio
PRESENCIAS             ejecutor · autoridad · encuadre — y ninguna de las tres participa
DICTAMEN               superado · no-superado
ENTREGA                emitido · acusado · rechazado · devuelto
OBLIGACIÓN             satisfecha · retirada · huerfana
SALIDA DEL ITEM        completado · bloqueado · pausado · escalado · continua
TERMINACIÓN DE UN      completado · bloqueado · pausado · escalado
MACROCIRCUITO
```

## 2 · La ruta se compone por MATERIA y ESTADO, nunca por texto libre

`b.1` fija que el proceso lo determina el RESULTADO PERSEGUIDO. Aquí el resultado perseguido
es una DECLARACIÓN del encuadre —su `materia` y el `estado_del_objeto`—, y una tabla
declarada las lleva al `id` del proceso.

```text
ALTERNATIVA DESCARTADA  buscar palabras en el título o en la expresión del Owner y elegir el
                        proceso que más case
POR QUÉ                 renombrar un item cambiaría su proceso, un sinónimo activaría una
                        ruta que nadie pidió, y dos encuadres idénticos en sustancia caerían
                        en procesos distintos según cómo se redactaron
CÓMO SE COMPRUEBA       `T196` tiene las dos mitades: renombrar el título no mueve la ruta, y
                        una expresión que nombra diseño, arquitectura, dominio y seguridad no
                        activa ninguna de las cuatro
POR QUÉ EL PAR          `FEA` y `GAP` se distinguen sólo por el ESTADO del objeto. Con una
                        tabla de una columna habría que desempatarlas leyendo prosa
```

La misma regla gobierna la vía 3 —la condición se DECLARA verdadera, no se adivina, porque
juzgarla es decidir contenido y `gate:despacho-coherente` se lo prohíbe a DSP en su
comprobación `sin-contenido`— y la elección de composición de `C4`, que se hace por el
identificador del bloque `ads:composicion` y en el ORDEN EN QUE ESTÁN ESCRITOS.

## 3 · El GATE DE COMPOSICIÓN, y qué significa que la fase NO ABRA

```text
QUÉ EXIGE     para CADA capacidad que la fase declara, consta UNA de las cuatro vías, con su
              proceso y —si es la 3— su condición nombrada
QUÉ EMITE     `COMPOSICION_INCOMPLETA`, y su constructor EXIGE capacidad y fase: un error que
              para pero no dice a quién escalar no cumple el contrato aunque pare
POR QUÉ ES    componer es una función PURA que no toca el estado. Quien escribe la ruta sólo
PURA          recibe rutas que ya pasaron el gate, de modo que un fallo de composición no
              puede dejar media ruta publicada, que es como un gate se vuelve decorativo
QUÉ NO HACE   no inventa un handoff para tapar una capacidad sin vía, y no ensancha `b.16`
```

## 4 · Ningún gate es fuente normativa, y se impide por MECANISMO

```text
MECANISMO 1   lo ÚNICO que un dictamen escribe en el estado durable es su propio objeto, en
              el dominio `dictamenes`. Cualquier operación fuera de ese dominio es
              `GATE_NORMATIVO`
MECANISMO 2   la ruta ANTES y DESPUÉS del gate tiene los mismos participantes y las mismas
              obligaciones. Un gate que añade una capacidad ha ensanchado el proceso
POR QUÉ DOS   una prohibición sin mecanismo es una intención, y las dos formas de ser fuente
              normativa son distintas: escribir norma, y ampliar el proceso
NO HAY UN     el dictamen es `superado` o `no-superado`. Un tercer valor —«superado con
TERCER VALOR  observaciones»— convierte el fallo cerrado en fallo abierto, y deja la decisión
              de si las observaciones importan sin nadie asignado
```

## 5 · `C5`: RECHAZO y DEVOLUCIÓN no comparten camino

```text
RECHAZO       antes del acuse. El paquete NO cambia de custodia y NO cuenta para el freno de
              `a.7`, porque la capa nunca se depositó
DEVOLUCIÓN    después del acuse, y con los CUATRO campos. Cuenta para el freno de dos
SIN LOS       no es una devolución: se rechaza COMO devolución y el paquete vuelve al receptor
CUATRO
ALTERNATIVA   una sola operación con una bandera `antes_de_aceptar`
DESCARTADA
POR QUÉ       el contador del freno dependería de un booleano que alguien puede pasar mal, y
              el defecto que `C5` describe —aceptar por cortesía y devolver después—
              reaparecería por la puerta de atrás. Con dos operaciones, `rechazar` sólo vale
              mientras el estado es `emitido` y `devolver` sólo después del acuse
```

**Las CINCO entregas que §8.0 declara** —`SIS`→`PLT`, `SIS`→`CON`, `SIS`→`VER`, `CON`→`ENT`,
`ENT`→`VER`— están materializadas con sus once campos y validadas contra el mismo esquema que
las diecisiete de [`../circuitos/`](../circuitos/00-CIRCUITOS.md). Su sede definitiva es ese
directorio; mientras no estén allí viven en el paquete, y el catálogo funde las dos fuentes
por `id` con el corpus mandando, de modo que trasladarlas no rompe nada.

## 6 · `Continúa` tiene DOS modos, y el de por defecto no toca el estado

```text
PLAN        pasos 1 a 6 de `b.14`. Determinista, sin Owner, y NO modifica el estado
EJECUCIÓN   añade el paso 7, y sólo cuando no queda ninguna decisión humana pendiente. Con
            una pendiente levanta `DECISION_DEL_OWNER_PENDIENTE` en vez de elegir por el Owner
```

El paso 2 REPARA lo que es suyo y ESCALA lo que no, y la frontera no la traza este contrato:

```text
REPARA      la espera que dejó de ser viable, que `b.8` obliga a convertir en bloqueo · los
            derivados divergentes de su `source_revision`, que se REGENERAN y no se
            sincronizan · las proyecciones con huella rota, que se recompilan
ESCALA      las reconciliaciones pendientes, cuya salida `g.9` reserva a una transición
            explícita de la autoridad · las transacciones MARCADAS · la deriva no
            transaccional · los artefactos que un paquete dice haber producido y no están
SÓLO        las celdas de cobertura vencidas. §7.4 lo dice con esas palabras: no se abre
REPORTA     trabajo
```

**Las DOS ramas del paso 2 se LEEN, no se reimplementan.** `COMPLETAR` o `MARCAR conflicto`
—con la reversión acotada a lo especulativo local— están en `Almacen.recuperar()` y las
ejecuta `Runtime.abrir()` antes de despachar. `Continúa` lee el informe y dice qué rama se
tomó. Reimplementarlas sería una segunda recuperación.

**«Vencida» se decide por HUELLA y nunca por reloj.** Una celda vence cuando cambia alguno de
los identificadores de su sujeto (§9.6), no cuando pasa un plazo: un plazo exige leer el
reloj, y un artefacto derivado que lea el reloj deja de dar bytes idénticos entre dos
ejecuciones, contra `I-g3`.

**La propiedad central:** dos ejecuciones consecutivas sin cambios producen el MISMO plan byte
a byte y NO mueven `revision_id` ni `cid_raiz`. Por eso el plan no lleva la instancia del
runtime, ni el directorio de trabajo, ni ninguna ruta de la máquina.

## 7 · Los CUATRO macrocircuitos son composiciones del MISMO motor

```text
LA DEFINICIÓN   vive en el kernel como DATO derivado de la tabla de §18, y la batería
                ANALIZA esa tabla en el documento y falla si dejan de coincidir
POR QUÉ NO SE   `11-ARQ` no viaja al proyecto instalado. Un runtime que necesitara ese
LEE EN CALIENTE documento para arrancar no arrancaría en ningún producto gobernado
EL EJECUTOR     una clase, parametrizada por su definición, sin una sola rama por circuito.
                Los cuatro entran por el MISMO punto de despacho, que es observable, y la
                batería lo mide en las cuatro ejecuciones
QUÉ NO SE       compartir motor no aplana las rutas: cada uno conserva su disparador, sus
APLANA          precondiciones, sus gates, su rollback, su reanudación y su cierre
```

**La AUTORIDAD sobre un producto es un objeto durable tomado por comparación e intercambio.**
Dos macrocircuitos distintos —o dos ejecuciones distintas del mismo— sobre el mismo producto
son incompatibles, y de dos procesos reales que compitan exactamente uno la consigue.

```text
ALTERNATIVA   un fichero de bloqueo en el plano operacional
DESCARTADA
POR QUÉ       el plano operacional es reconstruible y fabricable por cualquiera —es el
              ataque que le costó la vía rápida al lease—, así que un bloqueo ahí no prueba
              nada. Un cerrojo TOMADO prueba que hay alguien; uno LIBRE no prueba nada
ALTERNATIVA   una matriz de compatibilidad por pares
DESCARTADA
POR QUÉ       los cuatro operan sobre el producto ENTERO, y razonar caso por caso sobre
              solapamientos que nadie ha decidido es decidirlos, y eso no es de `F6`
```

## 8 · La `FASE 0`: un contrato, cuatro invocaciones, y un soporte propio

Los SEIS identificadores del sujeto, y el nº 2 se acuña EL ÚLTIMO:

```text
1 producto o instalación
2 ejecución del macrocircuito — HUELLA del disparador y de los otros cinco. No consume
  contador, no abre iniciativa, no escribe canónico
3 revisión del kernel
4 revisión de esquemas y contratos aplicables
5 configuración y fuentes relevantes
6 huella de la evidencia
```

Falta uno y FALLA nombrándolo: la regla 7 es un mínimo, y omitir la huella de la evidencia
convierte cualquier reutilización posterior en una presunción.

**El SOPORTE DURABLE DE LA FASE 0** cuelga del control repo, es ANTERIOR a `estado/` y
contiene la declaración, su dosier y su celda, y NADA del macrocircuito.

```text
ALTERNATIVA   escribir la declaración en `estado/`
DESCARTADA
POR QUÉ       `estado/` nace en `INS-0`, `A0`, `M0` o `U0`, DESPUÉS de esta fase: escribir
              ahí antes es imposible, y pretenderlo oculta que la fase no tenía soporte
ALTERNATIVA   no escribirla y recalcularla
DESCARTADA
POR QUÉ       «exactamente una por ejecución» sería indemostrable: no habría nada que contar
POR QUÉ NO ES es INMUTABLE y direccionado por contenido. Se escribe una vez; escribir lo
UN SEGUNDO    mismo otra vez produce los MISMOS bytes en la MISMA ruta, y escribir algo
SISTEMA DE    distinto bajo el mismo sujeto es `DOS_DECLARACIONES`. No tiene diario, no tiene
ESTADO        revisiones y no admite mutación. El único ejecutor de mutaciones CANÓNICAS
              sigue siendo el `Almacen`, y aquí no hay estado canónico del macrocircuito
```

**INCORPORAR no es CERTIFICAR.** La primera fase que crea `estado/` incorpora la declaración a
`estado/cobertura/` como su primer acto, sin reemitirla, y con la MISMA huella. Una huella
distinta es OTRO sujeto y se rechaza.

**Si el gate BLOQUEA no hay nada que incorporar y nada que deshacer.** La frontera no es «no
escribir nada»: es no escribir nada DEL MACROCIRCUITO.

## 9 · Qué demuestra, y dónde

```text
T195–T202   `pruebas/test_ciclo.py`            48 casos · encuadre, taxonomía, `b.16`, las
                                               cuatro vías, el gate de composición, `C4`,
                                               planificación, despacho, gates, `C5`, cierre,
                                               trabajo derivado, analizador y determinismo
T203–T205   `pruebas/test_continua.py`         24 casos · los siete pasos, las ocho
                                               comprobaciones del paso 2, los DIEZ escenarios
                                               con proceso y estado reales —incluido un
                                               `SIGKILL` de verdad— y la propiedad central
T206–T209   `pruebas/test_macrocircuitos.py`   30 casos · la tabla de §18 analizada y
                                               contrastada, la `FASE 0` compartida, las ONCE
                                               filas `X-S1`–`X-S11`, los cuatro extremo a
                                               extremo con caso positivo y negativo, el punto
                                               único de despacho y la exclusión de autoridad
                                               con DOS PROCESOS REALES
```

Punto ejecutable: [`ads_ciclo.py`](ads_ciclo.py), con `encuadrar`, `componer`, `materializar`,
`planificar`, `ciclo`, `continuar` y `macrocircuito`, y códigos de salida `0` éxito · `1`
error tipado · `2` uso incorrecto.

## 10 · Lo que este contrato NO cubre

```text
NO CUBRE   la ejecución REAL de una capacidad. El ciclo compone, materializa, planifica,
           despacha y cierra; lo que una capacidad hace dentro de su paquete lo decide su
           método, y este contrato no lo toca
NO CUBRE   la evaluación automática de una condición de la vía 3 ni de una composición de
           `C4`. Las dos se DECLARAN, y juzgarlas es decidir contenido
NO CUBRE   las fases de cada macrocircuito más allá de su primera fase tras la `FASE 0`: el
           motor las ejecuta todas por el mismo camino, y la batería recorre extremo a
           extremo la primera de cada uno
NO CUBRE   la materialización de las fuentes por `PLT`, el reparto Git operación a operación
           de `C7`, ni el Integration Set de `ENT`. El ciclo declara sus handoffs; ejecutarlos
           es de otro corte
NO CUBRE   la sede definitiva de las cinco entregas de §8.0, que es `circuitos/` y no este
           paquete
```

**Y nada de esto está CERTIFICADO.** Implementado y probado no es certificado: la
certificación la emite un juicio independiente, y no quien construyó.
