# `F6` · MATRIZ DEL DELTA SOBRE EL PRIMER GATE VÁLIDO

**Base:** `review/f6-certificacion-final-insuficiente-20260905` = `8c87158`.
**Objeto juzgado:** candidata `c2437214c9353185d6b90b8fe86178302d4cf349`, tree `bb5b674`.
**Autoridad:** `O28`, inscrita como apéndice puro en la sede canónica.

Los **27 hallazgos** que el adjudicador verificó, agrupados en `P1`…`P7` **sin perder ni un
identificador**. Tres se solapan entre revisores (`#2`=`#22`, `#4`=`#15`=`#24`, `#7`=`#16`),
de modo que los **defectos distintos son 23**.

Esta matriz se escribe **antes** de tocar nada. La columna «estado final» se rellena al
cerrar, y no antes: una matriz que se completa por adelantado no mide, promete.

---

## `P1` · INVARIANTES Y ESTADO PRODUCTIVO

| id | sev | sede | reproducción | efecto posible | remedio adjudicado | prop. | prueba | inicial |
|---|---|---|---|---|---|---|---|---|
| **`#1`** `REV-1` GRAVE 1 | GRAVE | `runtime/runtime/estado_util.py:169-172` | por el canal oficial `rt.almacen`: salto directo `50→999` RECHAZADO; **borrar `prioridad` (paso 1) y reescribirla `=999` (paso 2): ambas CONFIRMADAS**, prioridad durable = 999 | **evasión de autoridad** y mutación prohibida del estado durable | la guarda `if campo not in anterior or campo not in contenido: continue` deja pasar el alta y la baja del campo. Cerrar los CUATRO cuadrantes (presente/ausente × antes/después) | `PLT` | sabotaje que ejerza las DOS transiciones, no sólo el salto directo | ABIERTO |

**Por qué el sabotaje anterior no lo cazó, dicho:** §6 de `05-MATRIZ` registra que el auditor
independiente «dio por bien cerrado» `G-04` porque reinsertó el sabotaje de `R1-H02` y salió
`[PRIORIDAD_INMUTABLE] … de 50 a 60`. Ése es el **salto directo**, el caso fácil. Una
propiedad cuyo único sabotaje es el caso que no la derrota **no está probada**.

---

## `P2` · INTEGRIDAD, HUELLA Y AUTORIDAD

| id | sev | sede | reproducción | efecto posible | remedio adjudicado | prop. | prueba | inicial |
|---|---|---|---|---|---|---|---|---|
| **`#20`** `REV-3` H1 | GRAVE | `runtime/admision/__init__.py:108-111` · `admision/perimetro.py:366-371` | se reescribe el TÍTULO de `O26` en DISCO: `ads_admision` ve `mutaciones 119→120` y **hallazgos se queda en 119**; `grep -c ADS-OWNER-RESOLUCIONES` → `0`. Control del control: `sede.juzgar` sobre los bytes del disco SÍ devuelve `ENTRADA_ALTERADA · O26` | **evasión de autoridad**, **falso verde sobre obligación crítica** | `actual = canal.contenido("HEAD", ruta)`: el disco sólo se mira si `HEAD` no tiene el fichero, y la sede sale por `continue` antes de las ramas `INMUTABLE`/`DECLARADA` que sí contrastan el árbol en las otras **29** zonas. Juzgar HEAD **e** índice **y** disco | `PLT` | los nueve ataques del §5 del encargo | ABIERTO |
| **`#21`** `REV-3` H2 | GRAVE | `validadores/huella.py:209` | `AMBITOS = ("kernel","packs","tooling")`: alterando a la vez la sede del Owner y `05-MATRIZ`, la huella sigue siendo `854dfa1b99be3824` | **falsificación de evidencia** · norma modificable sin mover el sello | separar HUELLA DEL KERNEL y **SELLO DEL PRODUCTO**, derivando de las fuentes qué material normativo se sella, con exclusiones motivadas y sin autorreferencia | `PLT` | los ocho ataques del §6 del encargo | ABIERTO |
| **`#23`** `REV-3` H4 | SERIO | `validadores/comprobar_integridad.py` | la «comprobación 3» está DECLARADA («sensible al contenido y a la ruta») y **no está escrita**: el código llama `huella.calcular` dos veces y compara determinismo. `IMPRESCINDIBLES` tiene **nueve** entradas escritas a mano, todas en `kernel/`+`tooling/` | falso verde: las dos defensas declaradas contra estrechar la huella no ven el estrechamiento de `#21` | implementar lo prometido, o corregir la declaración en la sede editable competente. No puede quedar declarada sin código | `PLT` | positivo, negativo y sabotaje específico | ABIERTO |
| **`#25`** `REV-3` H6 | SERIO | `docs/f5/validar-f5.py` | sobrevive la definición de append-only por **PREFIJO** (`hoy.startswith(orig)`), la que `O27` §3 sustituyó. No está entre los 38 validadores ni dentro de la huella, y da `OK` sobre la sede alterada de `#20` | **falso verde** sobre la sede que otorga competencia | una sola definición de append-only, por ENTRADA CERRADA, en todas las sedes que la aplican | `SIS` | sabotaje que borre `O20`–`O27` y las sustituya | ABIERTO |
| **`#17`** `REV-2` MOD 1 | MODERADO | `FUENTES-CANONICAS.yml` · `admision/perimetro.py` | `D-03` relajó `KERNEL.md`, `(a)`, `(b)` y `E1` de `APPEND_ONLY` a `DECLARADA` y **nada cubre la reescritura**; el fichero afirma «ninguna de las dos abre un falso verde» y no publica el sabotaje que lo demuestre | falso verde sobre material aprobado | dar a cada clase su regla de integridad **con su sabotaje**, no sólo con su motivo | `SIS` | los siete casos del §11 del encargo `F6·CIERRE FINAL` | ABIERTO |
| **`#3`** `REV-1` GRAVE 3 | GRAVE | `validadores/comprobar_evidencia.py` | el contraste contra `HEAD` alcanza **32 de 38** evidencias: sólo mira lo que algún escenario CITA. Las 6 descubiertas publican **cuatro de las siete líneas de la línea base**. Editando `582→9` y `170→3`: `T158/T350 SUPERADA · EXIT=0`, canal declarando «EJERCIDO» | **falsificación de evidencia** sin que nada enrojezca | el contraste recorre las evidencias PUBLICADAS —derivadas de `validadores.yaml`—, no sólo las citadas; y publica el cardinal, no sólo «EJERCIDO» | `PLT` | los ocho ataques de `D-05` sobre las seis descubiertas | ABIERTO |

---

## `P3` · MEDICIÓN DE `O26`

| id | sev | sede | reproducción | efecto posible | remedio adjudicado | prop. | prueba | inicial |
|---|---|---|---|---|---|---|---|---|
| **`#2`**=**`#22`** `REV-1` GRAVE 2 · `REV-3` H3 | GRAVE | `derivar-universo-obligatorio.py` · salida de `universo-obligaciones` | el propio instrumento publica, pegado a sus ceros, que `A=0` «NO demuestra `O26` §5.1» y `B=0` «NO demuestra §5.2», con contraejemplo vivo (`V6-12`/`ADJ-B3`). **Ninguna otra medición del árbol los acredita** | **obligación interna de `F6` que NO está implementada**, presentada como acreditada | `O28` §3 fija el significado operativo. Implementar **`O26-IMPL`** y **`O26-SAB`** como comprobaciones distintas, que no reutilicen `A`/`B`/`C` | `PLT` | pendientes de las dos = ∅, publicados individualmente | ABIERTO |
| **`#10`** `REV-1` MEN 10 | MENOR·LATENTE | `comprobar-cobertura-de-gate.py` | la cuarta resta es **amañable por construcción**: declarando `modificadas` de menos, la resta sale vacía. Reproducido en repositorio sintético. **En este gate NO se usó** — el adjudicador verificó 119 = 119 ruta a ruta | falso verde de cobertura en un gate futuro | el conjunto se deriva EXCLUSIVAMENTE de `git diff --name-status -M -C -z`; ni manifiesto ni coordinador lo proporcionan | `PLT` | los once casos del §10 del encargo | ABIERTO |
| **`#11`** `REV-1` OBS 11 | OBSERVACIÓN | procedimiento del gate | **no se emitió sobre de ancla**: nada externo ancla el congelado ni el manifiesto. Es del **coordinador** | sin ancla externa, la línea base sólo se sostiene sobre sí misma | emitir el sobre ANTES de crear al verificador, firmado por la raíz externa | `coordinador` | verificación de firma antes de entregarlo | ABIERTO |

---

## `P4` · `M-04` Y `C-L.7`

| id | sev | sede | reproducción | efecto posible | remedio adjudicado | prop. | prueba | inicial |
|---|---|---|---|---|---|---|---|---|
| **`#12`** `REV-2` GRAVE 1 | GRAVE | `06-DEUDA-Y-LIMITACIONES-VIGENTES.md` §3 | `M-04` —«la deuda que **bloquea `F6`**»— figura `ESTADO NO SUPERADA`, `FASE F6`, y «QUÉ NO LA CIERRA: ningún verde de la batería interna». Y sale con `A=B=C=0` en el universo | `O26` §5.5 incumplida: **bloqueante interno vivo** | reproducir el defecto vivo, corregir el CANAL productivo, añadir sabotaje, ejecutar la condición EXACTA de cierre. **No cambiar el rótulo** | `PLT` | la condición de cierre que su sede escribe | ABIERTO |
| **`#13`** `REV-2` GRAVE 2 | GRAVE | `06-DEUDA` · `C-L.7` | **NO CERRADA**, fase «F5 la especificación · F6 el instrumento», población CRECIENTE (`KD-02`, `LE-02`, `OC-1`), y **fuera de las tres restas** por frontera declarada («OTRO censo») | bloqueante interno vivo, invisible a la medición | derivar todas las instancias de la clase, corregir la CLASE, controles de crecimiento, ejecutar su criterio exacto | `SIS` | ausencia de nuevas instancias, demostrada | ABIERTO |

---

## `P5` · APARATO DE CERTIFICACIÓN

| id | sev | sede | reproducción | efecto posible | remedio adjudicado | prop. | prueba | inicial |
|---|---|---|---|---|---|---|---|---|
| **`#26`** `REV-3` H7 | MODERADO | `test_integridad_y_evidencia.py` `T330b` | la equivalencia «`#!` ⟺ INVOCABLE ⟺ mecanismo `E-10`», declarada comprobada **en los dos sentidos sobre el árbol entero**, es falsa para **80** ficheros (138 con shebang, 58 puntos), y `T330b` **EXIGE** con `assertTrue(residuales, …)` que existan | prosa que promete más de lo que el código mide | decir lo que se mide, o medir lo que se dice | `PLT` | la propia prueba, con su enunciado corregido | ABIERTO |
| **`#27`** `REV-3` H8 | LEVE | `validadores/negativos_runtime.py:202,214` | `RETIRADAS_DE_LA_RUTA` se asigna **dos veces**: el testigo publicado queda siempre `[]`. Son **siete** los puntos que publican `entradas_del_lanzador_retiradas` | testigo mudo | una sola asignación | `PLT` | el testigo publica lo retirado de verdad | ABIERTO |
| **`#9`** `REV-1` MEN 9 | MENOR | `comprobar-correccion-gate-de-cierre.py` | la batería del expediente anterior está en **32/38 · EXIT=1** con **SEIS** fallos sustantivos (`G-11`,`G-11b`,`G-21`,`G-22`,`G-23`,`G-28`,`G-29`,`G-30` según alcance) y **ninguna sede publica ese rojo**. La atenuante «faltaba `.git`» fue **RECHAZADA** por el adjudicador: su copia tenía `.git` con 252 revisiones | un rojo que nadie publica | publicar el rojo con su alcance, o cerrar los fallos | `coordinador` | la propia batería, con su resultado publicado | ABIERTO |
| **`#19`** `REV-2` MEN 1 | MENOR | manifiesto inmutable del gate anterior | dice «ÉSTE ES EL ÚNICO GATE AUTORIZADO… no se abre otro gate», y no consta acto del Owner que lo levante | contradicción de autoridad | **`O28` §1 y §2 lo levantan expresamente** al autorizar la verificación por composición | Owner | la propia `O28` | **RESUELTO POR `O28`** |

---

## `P6` · CIFRAS Y CONTRADICCIONES DOCUMENTALES

| id | sev | sede | reproducción | remedio adjudicado | prop. | inicial |
|---|---|---|---|---|---|---|
| **`#4`**=**`#15`**=**`#24`** | SERIO | `05-MATRIZ` §5 · `T380-T399` L37/L47/**L81** | §5 publica `23 controles` (son **26**) y `56 de 56` (son **58 de 58**); su propio §6 ya escribe los buenos. Una de las sedes falsas es el `entonces:` de `T380`, su **condición de aceptación** | **retirar y remitir**, o publicar comando derivable. NO sustituir una cifra manual por otra | `coordinador` | ABIERTO |
| **`#5`** `REV-1` MOD 5 | MODERADO | sedes del inventario | el cardinal `58` no está en NINGUNA evidencia, y las dos sedes vivas dicen «nueve» y «56». No hay regla en `comprobar_recuentos` que lo cense | censar el cardinal, o retirarlo | `PLT` | ABIERTO |
| **`#6`** `REV-1` MOD 6 | MODERADO | `T210-T225…md` · `REGISTRO-generado.md` | «veintiún pasos» sobrevive en el `nombre:` de `T225` sobre un escenario de **24**; se declaró «corregida» | corregir el `nombre:` y regenerar el derivado | `PLT` | ABIERTO |
| **`#7`**=**`#16`** | MODERADO | cinco sedes | afirman **en presente** que doce escenarios «han BAJADO a `prueba-ejecutada`»; en el árbol hay **CERO** en ese estado y los doce están `prueba-superada` y contrastados | poner la prosa en pasado, o retirarla | `coordinador` | ABIERTO |
| **`#8`** `REV-1` MEN 8 | MENOR | 23 sitios | «1 869 bytes» replicado 23 veces; el mecanismo mide **1 879** | retirar el cardinal y remitir a la derivación | `PLT` | ABIERTO |
| **`#14`** `REV-2` GRAVE 3 | SERIO **(parcial)** | `05-MATRIZ` · `docs/f6/gate-definitivo/` | **CONFIRMADO en parte**: está fuera de la HUELLA (cae con `#21`). **RECHAZADAS** dos sub-afirmaciones: sí tiene fila de manifiesto (asignada a `REV-1`, leída `[[1,153]]`) y lo del sobre no distingue `docs/f6` de `kernel/` | cae con `#21` (sello del producto) | `PLT` | ABIERTO |
| **`#18`** `REV-2` MOD 2 | MODERADO | `vigilar_append_only` | prosa caducada que aún pide como PETICIÓN lo que `D-03` ya hizo. Se declara **326** líneas más arriba, no 30 | retirar la petición cumplida | `SIS` | ABIERTO |

---

## `P7` · LIMITACIONES EXTERNAS

| id | sev | sede | reproducción | remedio | prop. | inicial |
|---|---|---|---|---|---|---|
| **`O26` §5.4** | BLOQUEANTE | adjudicación §4.2 | **NO ACREDITADA**: ninguno de los tres revisores ejerció las OCHO condiciones de `O26` §1, y el adjudicador tampoco. Exigen contenedor, identidad de sistema separada y proveedor de firma; `E-18` declara que `cgroup v2` no es ejercitable en este anfitrión | **ejercerlas directamente** sobre la candidata delta, produciendo evidencia NUEVA. No darlas por ejercidas porque una evidencia anterior diga «SUPERADA» | `PLT` | ABIERTO |
| **`E-17`** | EXTERNO | — | custodia productiva EXTERNA | sin cambio de clase | Owner | EXTERNO |
| **`E-18`** | LÍMITE | — | limitación de anfitrión | debe seguir diciendo **exactamente** qué backend y qué identidad se ejercieron | `PLT` | LÍMITE |
| **`G-08` bajo carga** | PENDIENTE | `test_contencion.py` | el adjudicador declaró no haberlo ejercido bajo carga; `E-18` limita el anfitrión | protocolo de preparación observable, sin sleeps, bajo carga | `PLT` | ABIERTO |
| **las 170 mutaciones** | PENDIENTE | `comprobar_negativos.py` | nadie las auditó una a una; sólo consta el agregado | publicar cada una con id, propiedad, canal, rojo esperado y observado, motivo y restauración. **El cardinal se deriva, no se escribe** | `PLT` | ABIERTO |


---

## §8 · ESTADO FINAL, escrito al cerrar

### Lo cerrado por el coordinador

| id | estado final | reproducción antes · después | prueba que lo mide |
|---|---|---|---|
| **`#1`** `G-04` | **CERRADO** · los CUATRO cuadrantes. La exención del ALTA sigue viva —`anterior is None`— y deja de concederse a un RENACIMIENTO fabricado borrando el campo un instante antes | ANTES: `PASO 1 CONFIRMADO · PASO 2 CONFIRMADO · prioridad 999`. DESPUÉS: las dos `RECHAZADO: PrioridadInmutable`, y el durable sigue en 50 | `T430`–`T434` (borrar · reintroducir · la evasión ENTERA · los cuatro cuadrantes con su control · dos instancias y reapertura) · negativo **`NG04c`**, que devuelve el `continue` y pone `T432` en rojo |
| **`#20`** `V6-12` | **CERRADO** · se recogen y se juzgan las TRES capas —`HEAD`, índice y árbol de trabajo— en los DOS regímenes, y la divergencia entre capas es hallazgo por sí sola | ANTES: sede reescrita en disco → `mutaciones 119→120 · hallazgos 119`. DESPUÉS: `V6-12 SEDE_DEL_OWNER_ALTERADA … EN 'disco'` | `T435`–`T440`, con `T440` como control del control (árbol intacto y apéndice confirmado, los dos VERDES) · negativo **`N435`** |
| **`#3`** contraste `HEAD` | **CERRADO** · la población son las **38** evidencias que el manifiesto declara, y para las que ningún escenario cita se exige identidad BYTE A BYTE, que es la única garantía que les queda | ANTES: `582→9` y `170→3` editados a mano → `T158/T350 SUPERADA · EXIT=0`. DESPUÉS: las dos evidencias NOMBRADAS y `0 superadas · 2 fallidas` | el propio ataque del revisor, reproducido sobre copia |
| **`#25`** append-only por prefijo | **CERRADO** · `validar-f5.py` deja de llevar su propia definición e IMPORTA el juez de `V6-12`. Si no se puede importar, dice `NO COMPROBADO`: no degrada al prefijo en silencio | ANTES: sobre la sede alterada, `append_only: OK`. DESPUÉS: `ROTO · [ENTRADA_ALTERADA] la entrada 'O26' no coincide BYTE A BYTE…` | el mismo ataque de `#20`, ahora sobre `validar-f5` |
| **`#19`** | **RESUELTO POR `O28`** §1 y §2, que levantan expresamente la prohibición del manifiesto anterior | — | la propia resolución |

### Un defecto del coordinador, encontrado por su propio remedio

`O28` se inscribió la primera vez **sin el delimitador estructural** `\n---\n\n` que
`O27` §3 exige entre entradas, y el canal recién corregido de `#20` lo cazó al instante:
`ESTRUCTURA_ILEGIBLE · entre el final de 'O27' y la entrada siguiente no está el
delimitador estructural declarado`. Se restauró la sede a su digest original
—`b378b1f7…`— y se reinscribió correctamente. **La corrección encontró un defecto de quien
la escribía**, que es exactamente para lo que sirve.

### `M-04` · el bloqueo que `A3` midió y no podía tocar, cerrado por el coordinador

`A3` **paró y explicó el bloqueo**, que era lo correcto, y de paso midió un hecho NUEVO que
ningún revisor había visto: la condición de cierre de `M-04` —«*que `F6` implemente todos los
puntos de §20.1 y los ejecute, con `V6-18` en verde: cero falsos verdes y cero falsos
rojos*»— se calculaba sobre **2 de los 19 puntos**.

```console
$ ads_admision.py --repo . matriz          ANTES
  controles: 24 · falsos_verdes 0 · falsos_rojos 0
  (12 de `V6-13` · 12 de `V6-14` · y ninguna otra familia)
```

Mientras `11-ARQ` §20.1 declara de `V6-18`: entrada «**la suite completa**», evidencia «**la
matriz entera, con sus dos columnas**». Un cero verdadero sobre una población que no es la
declarada no acredita lo que la condición pide — y ésa es literalmente la clase de `M-04`:
«*un árbol defectuoso puede pasar en verde*».

**Cerrado.** La población de puntos se **DERIVA** del código del verificador con `ast` —no se
enumera—, y cada uno tiene que tener tratamiento:

```console
$ ads_admision.py --repo . matriz          DESPUÉS
  controles: 28 · falsos_verdes 0 · falsos_rojos 0 · sin_acreditar []
  puntos emitibles ......... V6-04 V6-05 V6-09 V6-10 V6-11 V6-12 V6-13 V6-14
                             V6-15 V6-16 V6-17 V6-18 V6-19          (13)
  con adversarial propio ... V6-10 V6-11 V6-12 V6-17
  cubiertos por familia .... V6-05 V6-09 V6-13 V6-14 V6-18
  NO ejercibles aquí ....... V6-04 V6-15 V6-16 V6-19   (cada uno CON su motivo)
  SIN TRATAMIENTO .......... []                        ← lo que decide
  ok: True
```

**Y un adversarial no vale por dar rojo: tiene que NOMBRAR su punto.** Un rojo por otro
motivo demuestra que el aparato se queja, no que se queja de esto. Se midió: los ataques de
`V6-04` y `V6-19` daban rojo **por `V6-11`**, y eso los habría dado por buenos.

**Lo que NO se puede ejercer desde aquí, dicho y no fingido.** `V6-04` y `V6-19` censan el
código del **aparato que EJECUTA** —`RUNTIME = dirname(dirname(__file__))`—, no el del árbol
juzgado: un sabotaje escrito en el árbol bajo prueba les es invisible, y sabotear el aparato
durante la pasada es justo lo que `V6-11` impide. `V6-15` y `V6-16` no se emiten como
hallazgo: son líneas de procedencia. Los cuatro quedan declarados con su motivo, y sus
baterías propias sí los ejercen.

**`M-04` sigue SIN registrarse como SUPERADA**, y por la razón que `A3` escribió: su sede
dice «*QUÉ NO LA CIERRA: ningún verde de la batería interna, ninguna tanda de corrección*», y
`O28` §5–§6 reservan el acto certificador al verificador independiente. Lo que aquí se ha
hecho es **quitarle el defecto vivo y darle a su condición de cierre la población que
declara**; declararla superada sería el cierre por rótulo que el encargo prohíbe.

### `C-L.7` · corregida la clase, NO registrada como cerrada

`A3` corrigió el canal productivo —el barrido de la regla 7— y midió que **siete de nueve**
sabotajes escapaban al anterior por la caja de letra: `los doce hallazgos` era rojo y
`los DOCE HALLAZGOS` era verde. Los nueve los caza el corregido, con cuatro controles
negativos que siguen en verde para no comprar sensibilidad con falsos rojos.

**No la registra CERRADA**, y cita su propia condición: «*sólo un gate independiente
posterior puede cerrarla. Barrer no es certificar*». Deja además declarado lo que no cubre:
la lista de sustantivos sigue a mano (`JB-02`), el barrido es por línea, y el alcance del
rótulo histórico es el del campo y no el de la viñeta (`JA-01`).

---

## §9 · LA MEDICIÓN QUE DETIENE EL CICLO

`O28` §3 fija por primera vez el significado operativo de `O26` §5.1 y §5.2, y §8 de este
encargo exige, **antes de verificar**:

```text
O26-IMPL pendientes = ∅
O26-SAB  pendientes = ∅
```

Se construyeron los dos instrumentos y se midió. **No son ∅, y no se redondean.**

```console
$ python3.12 docs/evolucion/verificacion/comprobar-obligaciones-implementadas.py
  `O26-IMPL` · OBLIGACIONES INTERNAS DE `F6` REALMENTE IMPLEMENTADAS
  58 obligaciones medidas · 9 SIN IMPLEMENTAR · 9 faltantes individuales

$ python3.12 docs/evolucion/verificacion/comprobar-propiedades-saboteadas.py
  S1  SABOTAJE IMPUTADO AL ESCENARIO              primeras faltas: 202
  S2  MOTIVO DEL ROJO DECLARADO                   primeras faltas: 2
  S3  CANAL PRODUCTIVO, NO PRUEBA TEXTUAL         primeras faltas: 2
  S4  NO ES SÓLO LA HUELLA GENERAL                primeras faltas: 0
  S5  ALCANCE ESPECÍFICO DE ESTA CLÁUSULA         primeras faltas: 81
  S6  CICLO SANO / SABOTAJE / RESTAURADO          primeras faltas: 13
  342 propiedades críticas medidas · 300 PENDIENTES · 57 obligaciones afectadas
```

**Las dos corridas las repitió el coordinador**, y las dos cifras se reproducen.

### Qué significa, dicho sin adorno

`O26-SAB` mide la unidad correcta: **la cláusula `falla_si`**, no la obligación. Con esa
unidad, **105 escenarios no tienen NI UN sabotaje en el catálogo** (`S1` = 202 faltas), y
44 tienen sabotaje **sin enlace inequívoco** a la propiedad que dicen cubrir (`S5` = 81).

Esto **no es un defecto introducido por el delta**. Es lo que `A=0 · B=0 · C=0` no medía y
el propio instrumento venía advirtiendo: `B=0` significaba «cada obligación tiene AL MENOS
UN sabotaje», no «cada propiedad crítica tiene una prueba capaz de fallar». `O28` §3 dio la
definición exacta, y con ella la respuesta es **300 pendientes de 342**.

Cerrarlos exige escribir del orden de **cien sabotajes nuevos** y declarar el enlace
sabotaje→propiedad, que hoy **no existe en el corpus**. Eso es un cuerpo de trabajo, no una
pasada de corrección.

### La decisión, por la regla que la gobierna

`O28` §4 declara bloqueante «*obligación interna de `F6` sin implementar*»: hay **9**.
§8 de este encargo exige los dos conjuntos vacíos **antes** de verificar.
§14 ordena: «*si queda un defecto bloqueante, no publiques candidata certificable: informa
y PARA*».

```text
NO se publica candidata certificable.
NO se emite el sobre de ancla.
NO se crea el verificador independiente.
F6 sigue ABIERTA · PesquerApp sigue BLOQUEADA.
```

**Aclaración sobre las 9, para que nadie las lea de más ni de menos.** Seis salen de que
`comprobar_recuentos` y `comprobar_evidencia` están hoy en `EXIT=1` por evidencia caducada
—transitorio, se cierra regenerando—. Las otras cinco son reales: `T277` y `T352` declaran
como prueba `derivar-universo-obligatorio.py` **sin modo**, de modo que corre, sale 0 y **no
los nombra**; una batería ajena que pasa no es una condición de cierre ejecutada.

**Aun cerrando las nueve, `O26-SAB` seguiría en 300.** La parada no depende de ellas.

---

# §10 · EL CIERRE `O29` · LA SEGUNDA MEDICIÓN QUE DETIENE EL CICLO

`O29` corrigió el criterio de `O28` §3 —«*una cláusula funcional no se convierte
automáticamente en propiedad crítica por estar formulada como condición de fallo*»— y
autorizó una última verificación por composición. Se hizo el trabajo y se midió. **No pasa.**

## Lo que SÍ quedó cerrado

| pieza | estado |
|---|---|
| **`O26` §1 · las OCHO condiciones** | **8 de 8 EJERCIDAS Y SATISFECHAS**, sobre la candidata y en el perfil declarado. La 6 —que el gate válido dejó NO ACREDITADA— en **contenedor real, UID 4242, sin red, control repo montado de sólo lectura**: los OCHO intentos de escritura IMPEDIDOS por el sistema de ficheros, no por una comprobación del programa. `E-18` estaba **CADUCADO**: se midió el anfitrión antes de creerlo —`cgroup2fs`, docker 29.1.3 con cgroup 2, `unshare` con UID 0 dentro— y sí ofrece el backend fuerte |
| **`O26-IMPL`** | de **16 a 1**. Y las 16 no eran 9: **siete las causaba el fichero nuevo del propio coordinador**, que entró en el inventario sin la purga `E-10` y con la guarda `G-03` divergente en dos escapes (`ú` frente a `ú`). Copiado el mecanismo canónico byte a byte, se cerraron solas |
| **`T277` y `T352`** | declaraban el derivador **sin modo**: corría, salía 0 y no los nombraba. Pasan a `--obligaciones`, que **ejerce** sus guardas y **los nombra**. Descartado `--autopruebas` pese a ser el complemento adversarial exacto: no los nombra, luego no puede ser condición de cierre |
| **`G-08` bajo carga** | `T413` decía «con el débil **Y CON EL FUERTE**» y metía el plan fuerte en un `if` vacío: sustituyendo sólo `fuertes_disponibles` por `[]`, **8 pasadas y VERDE**. Falso verde de la clase que `O29` §6 declara bloqueante. Corregido, y la corrección encontró un SEGUNDO defecto: bajo carga la **observación** confundía generaciones por reutilización de PID. `sesion_confirmada()` lo cierra: 0 colisiones en 30 pasadas |
| **cifras caducadas** | **RETIRADAS y remitidas a su derivación**, nunca sustituidas por otra cifra. Hecho que lo justifica: el árbol pasó de 145 a 149 ficheros `.py` durante la propia sesión |
| **`T147`** | dos documentos «existían para nadie»; enlazados desde la sede que corresponde |

## Lo que NO pasa, y por qué se para

`O29` §5: «*`O26` §5.2 se satisface cuando TODAS las propiedades críticas definidas en §2
tienen una prueba adversarial capaz de fallar*».

```console
$ comprobar-propiedades-saboteadas.py --por-riesgo
  346 propiedades · 336 CRÍTICAS · 118 con prueba adversarial capaz · 218 SIN
  S1 205 (ni un sabotaje) · S2 2 · S3 2 · S4 0 · S6 9
```

**Reclasificar por riesgo apenas descarga**: de 346 a 336 críticas. El alivio de `O29` no
estaba en §2 sino en §5/§6, y aun así quedan **218**.

### El auditor independiente lo revisó en las DOS direcciones, y encontró las dos

**DIRECCIÓN 2 · sobre-clasificación — CONFIRMADA.** El criterio es léxico y el vocabulario
del dominio es el del criterio: **64 de 336 críticas no tienen ni un rastro en su propia
cláusula**, y sin contexto el clasificador sigue diciendo CRÍTICA al 92 %. Muestreo juzgado
a mano de **114 propiedades** —los estratos A y B exhaustivos—: **de 336, entre 236 y 285
son críticas de verdad; punto ≈ 261**. Sobre-clasificación ≈ 75, un 22 %. Con motivos
FALSOS, no sólo clase discutible: `T276` clasificada por «procedencia» cuando ahí nombra
*la categoría de origen de una capacidad*; `T228` por la subcadena «degradacion» dentro del
nombre de campo `degradacion_permitida`; `T227` por «cwd» sobre una función pura.

**DIRECCIÓN 1 · infra-clasificación — DOS hallazgos, y el segundo es el grave.**

1. `T226/f1` rebajada a DOCUMENTAL por casar «prosa», que **en esa cláusula nombra lo
   PROHIBIDO**: «se declara en prosa **en vez de** asignarse y registrarse». La regla era
   ciega a la polaridad de «X en vez de Y», y **26 cláusulas** del universo llevan esa
   construcción. **CERRADO**: la evidencia de la rebaja se busca ahora sólo en `Y`.
2. **Las 71 acreditadas sobre prueba COMPARTIDA sin vínculo declarado.** `O29` §2 admite la
   prueba compartida «*cuando comparten realmente la misma propiedad **y el vínculo se
   declara***». **El corpus no lo declara en ningún caso.** Aplicando §2 al pie de la letra:
   **47 acreditadas de 337, no 118.**

**Y el auditor RECTIFICÓ su propia conclusión intermedia.** Había escrito que la cifra
«sobrestima el riesgo en un 20-25 %»; con `S5` a la vista la retiró: *los errores van en las
dos direcciones y no se cancelan, porque no caen sobre las mismas propiedades*. Corrigiendo
ambas: **40–50 acreditables de ≈261 críticas reales — más del 80 % del riesgo real sin
prueba adversarial admisible bajo `O29` §2.** Peor que el número publicado, no mejor.

### Las quince anclas, comprobadas contra el catálogo real

`T340`, `T344`, `T345` (append-only de la sede del Owner) · `T404`, `T408` (prioridad
inmutable) · `T215`, `T220`, `T296`, `T298`, `T299`, `T300`, `T306`, `T337`, `T364`, `T414`.
**Ninguna tiene sabotaje imputado**, comprobado importando el catálogo (185 mutaciones sobre
79 pruebas). **No es artefacto de nomenclatura**: sus vecinos de las mismas familias sí lo
tienen. De sus 32 propiedades, ~29 son críticas de verdad y nombran mecanismos de `O26` §1.

### Un defecto de conducta del coordinador, que el auditor señaló y consta

Apliqué la corrección de `T226/f1` **mientras la auditoría seguía abierta**, y el auditor lo
detectó por la marca de tiempo del fichero: *«un gate no se puede montar sobre un artefacto
que se mueve en respuesta a su propia auditoría»*. Tiene razón. El parche es correcto y está
acotado —no toca las diez tablas de efecto, y sus seis autopruebas siguen en 0 sin
detectar—, pero **debí esperar al dictamen**. Consta, y el auditor decidió **no reescribir**
su hallazgo aunque estuviera ya corregido: borrarlo habría sido el blanqueo.

## La decisión

`O29` §6 declara bloqueantes «*los defectos críticos descritos en §2*» y «*pruebas que no
ejecutan aquello que afirman*». §8 del encargo ordena: «*si queda un bloqueo material, no
publiques candidata certificable y PARA*».

```text
NO se publica candidata certificable.
NO se emite el sobre de ancla.
NO se crea el verificador independiente final.
F6 sigue ABIERTA · PesquerApp sigue BLOQUEADA.
```

**Y el fondo, que es lo que `O29` §10 manda entregar:** el problema no es el número, es la
**unidad de medida**. Mientras la propiedad crítica sea «una cláusula `falla_si`» y su clase
se derive de las palabras del escenario, cada corrida medirá el léxico del corpus. Las 71 sin
vínculo y las 75 de más son **el mismo defecto por sus dos caras**: *el corpus no declara qué
propiedad prueba cada sabotaje*. Sin esa declaración, ningún recuento —ni 229, ni 218, ni
290— describe el riesgo. Eso es una decisión humana, no otra pasada automática.
