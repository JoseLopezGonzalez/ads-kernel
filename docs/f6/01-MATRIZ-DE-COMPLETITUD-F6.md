# `F6` · MATRIZ DE COMPLETITUD

**Qué es este documento.** El censo COMPLETO de las obligaciones que forman `F6`, derivado
de sus fuentes canónicas, con el estado **medido** de cada una antes y después de este
corte, y la **resta** que dice si queda algo dentro. Es **DERIVADO**: no crea autoridad, no
aprueba nada y no certifica nada. La sede del estado por contrato sigue siendo
[`00-ESTADO-DE-IMPLEMENTACION-F6.md`](00-ESTADO-DE-IMPLEMENTACION-F6.md) §3, y ésta es su
contabilidad.

> **La regla que gobierna cada fila, y no admite lectura blanda.** Una fila NO se declara
> implementada por tener documentación, ni por tener una prueba que sólo inspeccione texto.
> **La columna de evidencia es un fichero real bajo
> [`kernel/operativo/pruebas/evidencia/`](../../kernel/operativo/pruebas/evidencia/) o un
> `Tnnn` concreto**, y esa evidencia es la salida de una EJECUCIÓN. Y
> `IMPLEMENTADO_Y_PROBADO` **no es CERTIFICADO**: la certificación la emite `F6-J`, que es un
> juicio independiente y no de quien construyó.

## 0 · Cómo se deriva el universo, y por qué no se escribe

```bash
# los contratos del verificador de admisión
grep -cE '^\| `V6-[0-9]+` \|' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
# los entregables de F6
sed -n '82,91p' docs/canonico/05-PLAN-DE-IMPLEMENTACION-F5-F6.md
# los apartados de la sección (g)
grep -oE '^## `g\.[0-9]+`' docs/rediseno/g-ESTADO-DURABLE-APROBADA.md
# los contratos DERIVADOS que g.17 nombra
grep -nE '^\| \*\*contrato de' docs/rediseno/g-ESTADO-DURABLE-APROBADA.md
# los hallazgos externos con propietario y fase
awk '/^## Lo que esta fase NO puede corregir/,/^### /' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
  | grep -oE '^\| `F-[0-9]+`' | grep -oE 'F-[0-9]+' | sort -u
# los del octavo gate contratados para F6
awk '/^### La tabla de los 22/{t=1} t' docs/evolucion/CHECKPOINT-ADS-NEXT.md \
  | grep -E 'CONTRATO_COMPLETO_PARA_F6' | grep -oE '^\| `C-[0-9]+`'
# el conjunto de ÁRBOLES ADVERSARIALES de V6-15
grep -nE '^## [0-9]+ · EL [A-ZÁÉÍÓÚ]+ ÁRBOL' docs/evolucion/[0-9][0-9]-*.md
```

**Vocabulario de la columna de estado.** El mismo que declara
[`00-ESTADO-DE-IMPLEMENTACION-F6.md`](00-ESTADO-DE-IMPLEMENTACION-F6.md) §3, y ninguna fila
usa una categoría vaga: `IMPLEMENTADO_Y_PROBADO` · `PARCIAL` · `NO_IMPLEMENTADO` ·
`BLOQUEADO_POR_DEPENDENCIA` · `BLOQUEADO_POR_DECISION_DEL_OWNER` · `EXTERNO` ·
`PENDIENTE_DE_CERTIFICACIÓN`.

**Vocabulario de la columna «pendiente».** `INTERNO` es obligación de `F6` construible aquí.
`EXTERNO` es materia que una norma vigente asigna a otra fase o autoridad, **y la fila cita
la fuente literal**. `LÍMITE DE ANFITRIÓN` es mecanismo construido cuya demostración depende
de lo que la máquina ofrece, y se separa en §4 sin convertirlo en cumplimiento universal.

---

## 1 · Los entregables `F6-A` … `F6-J`

**Sede:** [`05-PLAN-DE-IMPLEMENTACION-F5-F6.md`](../canonico/05-PLAN-DE-IMPLEMENTACION-F5-F6.md)
§2.1, líneas 82–91.

| obligación | fuente normativa exacta | propietario | estado inicial medido | evidencia ejecutable existente | pendiente | acción de este corte | estado final medido |
|---|---|---|---|---|---|---|---|
| **`F6-A`** verificador de admisión, con sus diecinueve puntos | `11-ARQ` §20.1 | `SIS` especifica · `PLT` implementa · `VER` dosier | IMPLEMENTADO_Y_PROBADO | `evidencia/admision-salida.txt` · `evidencia/arboles-salida.txt` · `evidencia/raiz-externa-salida.txt` · `T182`–`T190`, `T210`–`T213`, `T217`–`T220` | — | verificado, no reabierto | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |
| **`F6-B`** raíz externa de confianza con ejecutor sin identidad de escritura | `11-ARQ` §11.8 · `O18` · `O25` | Owner acepta · `SEG` gobierna | IMPLEMENTADO_Y_PROBADO | `evidencia/raiz-externa-salida.txt` · `evidencia/identidad-salida.txt` · `T217`–`T220`, `T192`, `T225` | **ACTO DEL OWNER EMITIDO Y CONDICIONADO** — `O26`, 2026-09-04. Ya NO es «límite de anfitrión»: lo que faltaba era un acto del Owner, y existe. Lo que sigue pendiente es la COMPROBACIÓN de sus ocho condiciones por un gate independiente VÁLIDO sobre un SHA exacto | la fila se reclasifica: se retira «límite de anfitrión» y se nombra `O26` por lo que es. **No se declara satisfecho `B3`**, y `O26` **no se presenta como certificación** | IMPLEMENTADO_Y_PROBADO · **ACEPTACIÓN ARQUITECTÓNICA CONDICIONADA** · PENDIENTE_DE_CERTIFICACIÓN |
| **`F6-C`** gobierno Git del control repo | `O16` · `g.14` | `SIS` | IMPLEMENTADO_Y_PROBADO | `evidencia/gobierno-git-salida.txt` · `evidencia/multimaquina-salida.txt` · `T187`, `T221`, `T222` | — | verificado | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |
| **`F6-D`** runtime y dispatcher | `11-ARQ` §7 | `PLT` | PARCIAL — faltaba el **paso 4 de `C4`** | `evidencia/runtime-salida.txt` · `evidencia/ciclo-salida.txt` · `evidencia/continua-salida.txt` · `T182`–`T186`, `T195`–`T205` | — | el paso 4 de `C4` y la política de `C2` los cierra la batería `agentes` (`T226`–`T235`) del **corte paralelo**, medida en verde en esta pasada; NO es trabajo de este agente y se atribuye a quien lo hizo | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |
| **`F6-E`** disposición física del estado | `11-ARQ` §2 · `g.1`–`g.13` | `SIS` | IMPLEMENTADO_Y_PROBADO | `evidencia/estado-durable-salida.txt` · `evidencia/estado-e2e-salida.txt` · `T172`–`T181` | — | verificado | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |
| **`F6-F`** los cuatro macrocircuitos y su `FASE 0` | `11-ARQ` §8 y §9.6 | `SIS` | IMPLEMENTADO_Y_PROBADO en su alcance | `evidencia/macrocircuitos-salida.txt` · `T206`–`T209` | **EXTERNO** — el recorrido extremo a extremo de TODAS las fases de `A` y `U`. Fuente literal en §3 de este documento | delimitado con cita; no se reclasifica ni se vacía | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |
| **`F6-G`** arquitectura de adaptadores, sus cuatro piezas | `11-ARQ` §6 | `PLT` | IMPLEMENTADO_Y_PROBADO | `evidencia/adaptadores-salida.txt` · `evidencia/sesion-nueva-salida.txt` · `T191`, `T223`, `T224` | **EXTERNO** — el NIVEL `soportado`. Fuente literal en §3 | nivel REAL conservado (`compatible`), derivado y no escrito | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |
| **`F6-H`** hallazgos externos con propietario y fase `F6` | `11-ARQ` §19 | `SIS` · `ENC` · `DIS` | **PARCIAL** — el inventario anterior enumeró las nueve filas `F-nn` de la tabla de externos y **omitió las CUATRO obligaciones de fase `F6` de la misma sede**: `CONTRATO 1`, `CONTRATO 1bis`, `CONTRATO 2` y `D104`. La sede de `F6-H` es «`11-ARQ` §19», la SECCIÓN ENTERA | las nueve filas `F-nn` sí la tenían; las cuatro obligaciones NO tenían ninguna | INTERNO | el inventario se AMPLÍA a las cuatro obligaciones —§2.2— y su universo deja de escribirse: lo deriva `derivar-universo-obligatorio.py --obligaciones` | **PARCIAL** — tres de las cuatro cerradas y probadas; `D104` materializa CINCO de sus NUEVE pares. **NO se marca completa mientras las tres restas del universo no estén vacías** · PENDIENTE_DE_CERTIFICACIÓN |
| **`F6-I`** guarda de versión mínima de Python | `11-ARQ` §19 · `06-DEUDA` §4 (`A14`) | `PLT` | IMPLEMENTADO_Y_PROBADO | `evidencia/estado-durable-salida.txt` · `T172` | — | verificado | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |
| **`F6-J`** la CERTIFICACIÓN | `O20` §3 | juicio INDEPENDIENTE | BLOQUEADO_POR_DEPENDENCIA | — | **no es construcción: es un ACTO** | nada; su precondición —que exista lo que hay que certificar— queda cumplida | BLOQUEADO_POR_DEPENDENCIA |

---

## 2 · `F6-H` · el inventario UNO A UNO, que antes decía «el resto de su lista»

**Sede (a):** `11-ARQ` §19, tabla «Lo que esta fase NO puede corregir, con su propietario y
su fase» — nueve filas. **Sede (b):** `06-DEUDA` §7 y §8, con la matriz de los 22 de
`CHECKPOINT-ADS-NEXT.md`. **Sede (c):** `06-DEUDA` §4 y §10 bis.

**Criterio aplicado, fila a fila:** **A** construible y de `F6` → se implementa y se prueba
AHORA · **B** ya implementado → se aporta la ejecución concreta · **C** de otra fase o
autoridad → se demuestra con cita literal · **D** exige decisión REAL del Owner → sólo si se
demuestran a la vez las cuatro condiciones.

### 2.1 · Las nueve filas de `11-ARQ` §19

| obligación | fuente normativa exacta | propietario | estado inicial medido | evidencia ejecutable existente | pendiente | acción de este corte | estado final medido |
|---|---|---|---|---|---|---|---|
| **`F-01`** · mitad de `F6` | `11-ARQ` §19 fila `F-01`: «después, **F6** actualiza `01-PROCESOS.md` L434 y `00-CIRCUITOS.md` L166». Su mitad de `F5` está **RESUELTA**: `docs/f5/40-DISPOSICION-DE-LAS-PRESIONES.md` L40 —«`PN-14` \| **RESUELTA** \| `O23` §7 \| `E4` `E4.3`»— y la enmienda `E4.3` sustituye la cadena en `b.16` L895 y `a.6` L495 | `SIS` | **abierta**: las dos líneas del kernel seguían diciendo `DIS/Reconstruccion` | ninguna | **A** · INTERNO | `01-PROCESOS.md` L434 y `00-CIRCUITOS.md` L166 pasan a decir `DIS`, en el orden que `E4.4` fija —«primero la fuente, después el derivado»— | **IMPLEMENTADO_Y_PROBADO** · `T240` · `evidencia/contratos-salida.txt` · sabotaje `N240` |
| **`F-02`** | `11-ARQ` §19 fila `F-02`, puntos (1)–(5) | `SIS` | **abierta**: `capacidad` y `capacidad_productora` eran `{tipo: texto, min: 3}` | ninguna | **A** · INTERNO | `esquemas/proceso.yaml` los tipa `ref_a: capacidad`; sufijo `:<variante>` **opcional y TIPADO** contra las cinco variantes declaradas; `/` deja de ser válido; `OWNER` se declara en el campo propio `autoridad_productora`; y una capacidad productora que fija el ENCARGO se declara con `capacidad_productora_derivada` en vez de entrar como prosa | **IMPLEMENTADO_Y_PROBADO** · `T240` · sabotajes `N240b`, `N240c`, `N240d` |
| **`F-04`** | `11-ARQ` §19 fila `F-04`: «`grado_inicial: alta` en el escenario, conservando `grado: media`, y que `T75` compruebe la coincidencia con el grado del paso 5» | `ENC` con `SIS` | **abierta a medias**: `esquemas/encuadre.yaml` ya exigía `grado_inicial`, y el ESCENARIO declaraba `grado_inicial: media` mientras su paso 5 medía `GRADO GLOBAL = ALTA`. `T75` no lo comprobaba | ninguna sobre la coincidencia | **A** · INTERNO | el escenario pasa a `grado_inicial: alta` conservando `grado: media`, con el motivo reescrito; `T75` gana la cláusula en `entonces` y en `falla_si`; y la coincidencia se COMPRUEBA ejecutando | **IMPLEMENTADO_Y_PROBADO** · `T244` · sabotaje `N244` |
| **`F-05`** (i) | `11-ARQ` §19 fila `F-05` · el QUÉ viaja lo declara §8.0 | `SIS` | IMPLEMENTADO en el macrobloque 3 (`circuitos/entregas-de-8-0.md`) y **sin prueba que lo sostuviera** | ninguna | **B** · INTERNO | se le da la ejecución que le faltaba: las cinco entregas se contrastan contra el bloque «`SIS` y `PLT`, dicho aparte» de §8.0 y contra los campos que `C5` exige | **IMPLEMENTADO_Y_PROBADO** · `T243` · sabotaje `N243` |
| **`F-06`** | `11-ARQ` §19 fila `F-06` | `DIS` | **abierta**: `cuando: "DIS cierra su capa y el item continúa hacia verificación"`, sin estación, y la entrega no decía de qué pasada procedía el dictamen | ninguna | **A** · INTERNO | el `cuando` se ancla a la **estación 11**, `REVISIÓN DE FIDELIDAD`, que es la SEGUNDA pasada del gate visual y hasta la cual el gate de diseño no cierra; la entrega nombra la pasada de cada dictamen y la estación 8 del de usabilidad; y se añade un `rechaza_si` para el dictamen que llegue con `fidelidad` pendiente | **IMPLEMENTADO_Y_PROBADO** · `T241` · sabotajes `N241`, `N241b` |
| **`F-07`** | `11-ARQ` §19 fila `F-07`, con sede en `docs/owner/*` **y** `validadores/exclusiones.yaml` | `SIS`, con el Owner para el valor | **abierta**: la distinción aprobada/trabajo vivía sólo en prosa | ninguna | **A** · INTERNO · con una DESVIACIÓN declarada, ver abajo | mecanismo cerrado: toda ruta de `docs/owner/` declara su autoridad con motivo, el valor se **DERIVA** de la clase que `docs/canonico/FUENTES-CANONICAS.yml` asigna, y un documento sin declaración da ROJO en vez de pasar por omisión | **IMPLEMENTADO_Y_PROBADO** · `T242` · sabotajes `N242`, `N242b`, `N242c` |
| **`F-08`** | `11-ARQ` §19 fila `F-08`: propietario «el **Owner**: es su documento», fase **`F5`** | el Owner | CERRADA por `F5` | la NOTA DE VIGENCIA de `O23` §10, al principio de `ADS-IDEAS-PENDIENTES-MULTIREPO.md` | **C** · EXTERNO a `F6` | ninguna: no es de `F6` y ya está emitida | CERRADA por `F5` · fuera del alcance de `F6` |
| **`F-10`** | `11-ARQ` §19 fila `F-10` | `ENC` | **abierta**: la cabecera afirmaba «catorce bloques, **uno por clase de expresión**» | ninguna | **A** · INTERNO | la aposición se retira y se dice por qué es falsa —catorce formas frente a nueve clases—; los DOS cardinales se derivan del corpus y `comprobar_recuentos.py` los vigila | **IMPLEMENTADO_Y_PROBADO** · `T245` · sabotaje `N245` |
| **`F-11`** | `11-ARQ` §19 fila `F-11` | `SIS` | **abierta**: la cabecera decía «las pruebas T75 a T84» | ninguna | **A** · INTERNO | la cabecera enumera `T75`–`T80` y `T154`–`T157` y declara dónde viven `T81`–`T85`; la comprobación EXPANDE los rangos y contrasta contra los identificadores que el fichero contiene de verdad | **IMPLEMENTADO_Y_PROBADO** · `T246` · sabotaje `N246` |

> **La desviación de `F-07`, dicha en vez de callada.** El remedio pide el campo «en cada
> fichero de `docs/owner/`». **Dos de los tres no lo admiten sin romper otra norma vigente**:
> `FUENTES-CANONICAS.yml` los clasifica `AUTORIDAD_SUPERIOR`, y la condición de contenido que
> el verificador de admisión aplica a esa clase es `append-only-contra-el-nacimiento`
> (`runtime/admision/perimetro.py`, `CONDICIONES_DE_ZONA`). Insertar una línea de metadatos en
> la cabecera de un fichero append-only **no es un añadido: es una reescritura de lo
> publicado**, y `V6-12` la da en ROJO por diseño —«alterar una letra de lo publicado da
> **ROJO**, aunque esté confirmado»—.
>
> **Y aquí esta fila decía de más, hasta que la auditoría independiente lo midió.** Decía
> «sólo un resultado es conforme con las dos normas a la vez». **Es falso, y se comprobó
> EJECUTANDO el verificador sobre copias**: el campo en la CABECERA da ROJO `V6-12`
> —`SEDE_DEL_OWNER_ALTERADA`, código 1—, pero AÑADIRLO AL FINAL de los dos ficheros
> append-only sale `INDETERMINADO`, sin hallazgo, porque añadir es precisamente lo que
> append-only permite; y el tercer fichero, `ADS-IDEAS-PENDIENTES-MULTIREPO.md`, es
> `NO_APLICABLE_A_IMPLEMENTACION`, cuya condición es `DECLARADA` y no append-only, de modo
> que admite el campo dentro. **Hay al menos tres resultados conformes, no uno.**
>
> **Lo que sí se sostiene, y es lo que decide.** La elección entre esos tres no altera
> ningún comportamiento normativo: las tres declararían el mismo valor, derivado de la misma
> clase canónica, y ninguna cambia qué es autoridad aprobada y qué es trabajo. Es materia de
> MECANISMO, que `O24` §2 reconoce a `F6`, y **no de decisión del Owner** —el criterio para
> parar exige que dos resultados conformes alteren comportamiento NORMATIVO, y aquí no lo
> alteran—. Se elige `validadores/exclusiones.yaml`, que es la otra sede que la propia fila
> `F-07` nombra, por dos razones dichas: **es la única de las tres que no escribe un solo
> byte en un documento del Owner**, y es la que ya recorre el validador. El valor tampoco se
> elige: se deriva de la clase canónica, y `T242` da ROJO si alguien escribe otro.

### 2.2 · Las siete filas `CONTRATO_COMPLETO_PARA_F6` de la matriz de los 22

**Sede:** `06-DEUDA` §8 · matriz de `CHECKPOINT-ADS-NEXT.md`. **Su prueba de cierre son
contratos concretos del verificador, nombrados fila a fila en la propia matriz**, y por eso
esta tabla no inventa criterio: se limita a resolver cada fila contra los `V6-*` que ella
misma nombra.

| obligación | contratos que la cierran, según la matriz | propietario | estado inicial medido | evidencia ejecutable existente | pendiente | acción de este corte | estado final medido |
|---|---|---|---|---|---|---|---|
| **`C-00`** | `V6-05` · `V6-09` · `V6-11` · `V6-15` · `V6-18` | `PLT` implementa · `SIS` propietario | IMPLEMENTADO_Y_PROBADO | `evidencia/admision-salida.txt` (`T188`–`T190`) · `evidencia/arboles-salida.txt` (`T210`–`T213`) | — | verificado | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |
| **`C-01`** | `V6-05` · `V6-11` · `V6-13` · `V6-18` | idem | IMPLEMENTADO_Y_PROBADO | `evidencia/admision-salida.txt` (`T188`–`T190`) | — | verificado | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |
| **`C-02`** | `V6-06` · `V6-14` · `V6-18` | idem | IMPLEMENTADO_Y_PROBADO | `evidencia/admision-salida.txt` (`T188`, `T190`) | — | verificado | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |
| **`C-03`** | `V6-07` · `V6-08` · `V6-18` | idem | IMPLEMENTADO_Y_PROBADO | `evidencia/admision-salida.txt` (`T188`, `T190`) | — | verificado | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |
| **`C-04`** | `V6-01` · `V6-02` · `V6-03` · `V6-04` | idem | IMPLEMENTADO_Y_PROBADO | `evidencia/admision-salida.txt` (`T188`, censo de lecturas) | — | verificado | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |
| **`C-13`** | `V6-08` · `V6-11` · `V6-16` · `V6-17` | idem | IMPLEMENTADO_Y_PROBADO | `evidencia/admision-salida.txt` · `evidencia/raiz-externa-salida.txt` (`T217`–`T220`) | — | verificado | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |
| **`C-18`** | `V6-04` · `V6-10` · `V6-11` | idem | IMPLEMENTADO_Y_PROBADO | `evidencia/admision-salida.txt` (`T188`, `T189`) | — | verificado | IMPLEMENTADO_Y_PROBADO · PENDIENTE_DE_CERTIFICACIÓN |

> **Lo que este cierre NO dice.** `06-DEUDA` §8 declara «**Ninguno SUPERADO**, y su resolución
> lo prohíbe expresamente». Lo que esta tabla registra es que **el contrato que la matriz les
> asigna está construido y ejecutado**; declararlos SUPERADOS es un acto de `F6-J`, no de esta
> contabilidad.

### 2.3 · `A14`, `FD-3`, `S1-02`, `FD-5`, `FD-1` y `FD-6`

**Sede:** `06-DEUDA` §4 y §10 bis.

| obligación | fuente normativa exacta | propietario | estado inicial medido | evidencia ejecutable existente | pendiente | acción de este corte | estado final medido |
|---|---|---|---|---|---|---|---|
| **`A14`** guarda de entorno | `06-DEUDA` §4 · `11-ARQ` §19 | `PLT` | CERRADA | `evidencia/estado-durable-salida.txt` · `T172` | — | verificada | IMPLEMENTADO_Y_PROBADO |
| **`FD-3`** la especificación normativa viaja | `06-DEUDA` §10 bis | `PLT` · `SIS` | CERRADA | `evidencia/arranque-salida.txt` · `T148`, `T171` | — | verificada | IMPLEMENTADO_Y_PROBADO |
| **`S1-02`** contenido y no sólo topología | `06-DEUDA` §10 bis · doc. 28 §3.2 y §3.6 | `PLT` · `VER` | CERRADA | `evidencia/admision-salida.txt` · `evidencia/e2e-runtime-salida.txt` paso 22 · `T188`, `T189` | — | verificada | IMPLEMENTADO_Y_PROBADO |
| **`FD-5`** aislamiento de procesos | `06-DEUDA` §10 bis · `CONTRATO-ADAPTADOR.md` §2 | `PLT` | IMPLEMENTADO_Y_PROBADO **en el paquete**, y sin medición equivalente A TRAVÉS DEL ADAPTADOR | `evidencia/contencion-salida.txt` · `T214`–`T216` | INTERNO en su mitad de adaptador · LÍMITE DE ANFITRIÓN en el resto (§4) | se mide otra vez, y ahora **por el adaptador y con la política real**: hijo, nieto y bisnieto con `setsid`, con CADA backend fuerte disponible; y sin backend fuerte el adaptador **no ejecuta** | **IMPLEMENTADO_Y_PROBADO en este anfitrión** · `T247`, `T248` · `evidencia/adaptadores-salida.txt` |
| **`FD-1`** custodia de la clave de firma | `O25` §2 y §5 · `g.15` | Owner decidió · `SEG` gobierna | mitad de decisión CUMPLIDA; custodia productiva EXTERNA | `evidencia/raiz-externa-salida.txt` · `evidencia/identidad-salida.txt` · `T192`, `T220`, `T225` | **EXTERNO** · `O25` §5: «Las claves efímeras están permitidas únicamente en pruebas y **no constituyen custodia productiva**» | se verifica que la fila lo dice con precisión y **no** se sustituye por una clave efímera de prueba | **EXTERNO**, con el fallo cerrado sin proveedor válido implementado y probado |
| **`FD-6`** ventana entre ejecutar y escribir el recibo | `06-DEUDA` §10 bis: «**no tiene cierre por diseño**: con un proceso externo cualquiera no existe "exactamente una vez"» | `PLT` | DECLARADA con su límite, y la ambigüedad DETECTADA | `evidencia/adaptadores-salida.txt` · `T191` | **EXTERNO por diseño**, con la cita de arriba | verificado: la segunda invocación que encuentra el recibo abierto devuelve `ambiguo` | IMPLEMENTADO_Y_PROBADO en lo exigible · sin cierre por diseño |

### 2.4 · `M-04` y `FD-2`, `FD-4`

| obligación | fuente normativa exacta | propietario | estado inicial medido | evidencia | pendiente | acción | estado final medido |
|---|---|---|---|---|---|---|---|
| **`M-04`** | `06-DEUDA` §3: «QUÉ LA CIERRA — que `F6` implemente TODOS los puntos del contrato del verificador **y los EJECUTE**, con cero falsos verdes y cero falsos rojos, medidos y publicados» | `PLT` · `SIS` · `VER` · Owner | los diecinueve implementados y ejecutados; `falsos_verdes = 0` y `falsos_rojos = 0` medidos en `T190` | `evidencia/admision-salida.txt` · `T190` | la ACEPTACIÓN es del Owner y es indelegable (`O18`) | verificado; no se declara SUPERADA, porque declararlo es acto de `F6-J` | condición de cierre CUMPLIDA en lo construible · el juicio es de `F6-J` |
| **`FD-2`** | `06-DEUDA` §10 bis: «**NO se corrige aquí, y no puede corregirse aquí**: editar la entrada rompería el carácter append-only» | el Owner | abierta | — | **EXTERNO**, con la cita | ninguna | abierta, **fuera de `F6`** |
| **`FD-4`** | `06-DEUDA` §10 bis: «**NO se corrige aquí, y no puede corregirse aquí**: editar `(g)` sería reabrir `F5`, y `O24` §5 lo prohíbe expresamente» | el Owner | abierta | — | **EXTERNO**, con la cita | ninguna | abierta, **fuera de `F6`** |

---

### 2.5 · Las CUATRO obligaciones de fase `F6` que la sede de `F6-H` declara, y que el inventario anterior OMITIÓ

> **Éste es el defecto de cobertura de `F6-H`, dicho sin rodeos.** La sede de `F6-H` es
> «`11-ARQ` §19», **la sección entera**. El inventario de §2.1 enumeró las nueve filas
> `F-nn` de una de sus tablas y se declaró completo, dejando fuera las CUATRO obligaciones
> que la MISMA sección declara con propietario, fase `F6` y condición de cierre literal.
> Una de ellas —`D104`— exige materializar en el kernel, y el árbol tenía **cero
> instancias** de lo que exige. Un inventario que se declara completo sobre un universo
> elegido a mano es verdadero por construcción, que es el defecto `P-08`.
>
> **El remedio no es escribir aquí las cuatro filas que faltaban**: eso deja la quinta
> omisión esperando. El universo se DERIVA, y su derivador falla cerrado si una sede no se
> puede leer o si un componente encoge:
>
> ```bash
> python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py --obligaciones
> ```

| obligación | fuente normativa exacta | propietario | estado inicial medido | evidencia ejecutable existente | pendiente | acción de este corte | estado final medido |
|---|---|---|---|---|---|---|---|
| **`CONTRATO 1`** · derivar el censo `AFIRMACIONES` | `11-ARQ` §19: «que `AFIRMACIONES` **deje de existir como lista literal** y que la cobertura del validador sea derivada. Mientras exista la lista, la condición NO está cerrada, aunque `T151` salga verde» | `PLT` | **abierta**: `comprobar_recuentos.py` L107–133 era una lista literal de `(ruta, patrón, clave)`; no cubría `contratos/00-INDICE.md`:7 ni `pruebas/T086-T092-contratos.md`:14, que dicen «veintiocho campos» sobre un esquema de 29, y `T151` salía SUPERADA | ninguna sobre la cobertura | **A** · INTERNO | la lista se retira; la cobertura se DESCUBRE barriendo el corpus vivo en dígitos y en letra, con reglas `(patrón de sede, derivación)` que no nombran ninguna ruta | **IMPLEMENTADO_Y_PROBADO** · `T151` y `T270` · sabotajes `N270`, `N270b`, `N270c`. **Y `T151` está en ROJO sobre tres sedes vivas que publican una cifra que el corpus desmiente, todas fuera de la zona de este corte**: es la PRUEBA POSITIVA que §19 prescribe |
| **`CONTRATO 1bis`** · los perfiles de agente, que nadie censa (`N-04`) | `11-ARQ` §19: «que la cifra deje de existir sólo en prosa» | `PLT` | **abierta**: `RECUENTOS-generado.md` contaba roles, métodos, prompts, composiciones, gates, rúbricas, vetos, formas, niveles de novedad y clases de entrada, y NO los `ads:perfil-agente` de `C2`, que son **21** | ninguna | **A** · INTERNO | el conjunto de tipos canónicos se deriva de los ESQUEMAS del árbol: cada tipo recibe censo por existir, y uno nuevo queda contado el día que nace | **IMPLEMENTADO_Y_PROBADO** · `T271` · sabotaje `N271`, que introduce un perfil nuevo en `C2` y comprueba que el recuento se mueve solo |
| **`CONTRATO 2`** · ampliar `T152` a toda sede que publique versión | `11-ARQ` §19: «que ninguna sede VIVA publique una versión o un recuento obsoleto, y que el alcance de `T152` sea derivado» | `PLT` | **abierta**: `T152` recorría **sólo `README.md` y `START_HERE.md`**, y por eso pasaba en verde mientras `kernel/operativo/00-INDICE.md` declaraba `KERNEL.md` «1.3.0» siendo 1.5.0 | ninguna sobre el alcance | **A** · INTERNO | el alcance se DESCUBRE por barrido y la versión vigente se resuelve contra `kernel/VERSIONES.md`, su sede única; los remedios se REPORTAN por clase de sede sin decidirlos | **IMPLEMENTADO_Y_PROBADO** · `T152` y `T272` · sabotajes `N272`, `N272b`. **`T152` está en ROJO sobre `kernel/operativo/00-INDICE.md`**, que es la PRUEBA POSITIVA prescrita |
| **`D104`** · instanciar los pares `<CAP>:revision` | `11-ARQ` §19, ficha `D104`: «**F6 MATERIALIZA; no elige la forma**», con el error `composicion-incompleta` que «no es un aviso: impide el cierre del gate de composición» | `SIS` | **abierta**: **cero** instancias de `:revision` en todo `kernel/operativo/` y **cero** validadores que lo comprobaran | ninguna | **A** · INTERNO | se materializan **CINCO** de los NUEVE pares del catálogo —los de `SEG`— en `recorrido/01-PROCESOS.md`, con su herencia y su posición; se añaden a `circuitos/` las dos instancias de handoff de la ENTREGA DE VUELTA; y el gate de composición se construye entero: cuatro vías, discriminante estructural, ancla en sus dos ramas, regla por item, los tres repartos y un censo de **20 fixtures** contrastado contra su sede | **PARCIAL** · `T273`–`T276` · sabotajes `N273`…`N273f`, `N275`, `N276`. **Los CUATRO pares de `DOM` NO están**: `esquemas/proceso.yaml` no admite la variante `DOM:revision` y ampliar ese conjunto es un ACTO NORMATIVO cuya sede es el esquema. `T273` los publica uno a uno y **el gate de composición no cierra** |

> **`CONTRATO 3` no está en esta tabla, y se dice por qué.** Es la guarda de versión de
> intérprete, tiene fase `F6` y **ya tiene sede propia en esta matriz**: es `F6-I`,
> implementada en `validadores/entorno.py` y probada por `T172`. Se comprueba, no se
> supone. **Con una divergencia declarada**: §19 le prescribe el código de salida **2** y la
> implementación usa el **78** (`EX_CONFIG`), con su motivo escrito —el 2 es «me han
> invocado mal»—. La sede del código es `entorno.py`; §19 es histórico y no se enmienda.
> **Y una trazabilidad que falta**: ningún escenario nombra `CONTRATO 3` en su `cubre`, de
> modo que el derivador del universo lo publica en la resta **A**. La cadena existe por
> `A14`; lo que falta es el nombre.

### 2.6 · Las TRES RESTAS, derivadas — y por qué esta matriz no las escribe

`O26` §5 fija las cinco condiciones bajo las que un gate independiente VÁLIDO puede declarar
`F6 CERTIFICADA`. Sus tres primeras son, literalmente, las tres restas:

```text
O26 §5.1  que no queden obligaciones internas de F6 sin implementar        → RESTA A
O26 §5.2  que no queden propiedades críticas sin una prueba capaz de fallar → RESTA B
O26 §5.3  que todas las obligaciones tengan trazabilidad hasta evidencia    → RESTA C
```

**Las tres se DERIVAN y esta matriz no publica su contenido**, porque un estado escrito
caduca cada vez que el árbol se mueve. Se leen ejecutando el derivador, que las publica con
nombre y no sólo con cardinal:

```bash
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py --obligaciones
```

**Mientras las tres no estén vacías, `F6-H` no se marca completa y `F6` no se certifica.**

---

## 3 · Las tres deudas que había que CLASIFICAR, con su cita

### 3.1 · El recorrido de TODAS las fases de `A` y de `U` · **NO es obligación interna de `F6`**

Tres citas literales, y las tres apuntan al mismo sitio:

```text
`11-ARQ` §14   «Ninguno se ha ejecutado. Son recorridos arquitectónicos, y sirven para una
               sola cosa: demostrar que las piezas encajan sin contradecirse. El piloto sigue
               pendiente.» … «Lo que NO demuestran: que funcionen. Para eso hace falta el
               piloto de `O14`.»
               Y su escenario 2 es, literalmente, «adopción de PesquerApp».

`11-ARQ` §18   «8 · PRIMERA ADOPCIÓN REAL  O14 · O15  PesquerApp  PERMANENTE, no un montaje
               desechable  ── BLOQUEADA por 9 ──  sin MVP, sin piloto desechable y sin
               adopción parcial»

`11-ARQ` §20.2 «LA CONDICIÓN PREVIA A PesquerApp es que `F6` los implemente **y los
               certifique**. Hasta entonces PesquerApp está BLOQUEADA, sin MVP, sin piloto
               desechable y sin adopción parcial»
```

**La consecuencia, sin adornarla.** El macrocircuito `A` es «adopción profunda de un producto
existente» (§8.2): recorrerlo extremo a extremo **es** el escenario 2, y el escenario 2 es el
nodo 8 del grafo de construcción, que §18 declara **BLOQUEADO por el nodo 9** —el verificador
y la raíz externa— hasta que esté **implementado Y certificado**. Ejecutarlo ahora sería
exactamente el «piloto desechable» y la «adopción parcial» que §20.2 prohíbe. **No se
reclasifica para vaciar la resta: se demuestra que la norma vigente lo pone después de
`F6-J`.** Lo que `F6-F` sí contrata —«los cuatro MACROCIRCUITOS y su `FASE 0` compartida, con
el contrato de conformidad estructural»— está construido y ejecutado.

### 3.2 · Los siete árboles sin cabecera · **`V6-15` NO exige fixtures para los once**

`11-ARQ` §20.5, literal:

```text
QUÉ NO ALCANZA   los árboles adversariales anteriores al OCTAVO. **Ninguna sede los publica
                 con cabecera propia**, y por eso el comando no los devuelve. No se les
                 inventa aquí un identificador ni una fase: se dice que no están y por qué
CÓMO ENTRARÍAN   si un gate futuro los publicara con la misma cabecera en un documento suyo,
                 **entrarían solos** …
MIENTRAS NO      `V6-15` es CONSTRUIBLE sobre el conjunto que su entrada entrega, y **no se
ENTREN           puede citar** como «cubre los once árboles»
```

Y la fila de `V6-15` define su entrada como «el conjunto **derivado** de los ÁRBOLES
ADVERSARIALES que un gate publicó **con cabecera propia** en su documento inmutable», con su
cierre medido sobre **ese mismo conjunto**: `entrada − suite = ∅` **y** `suite − entrada = ∅`.

**Medido hoy:** el comando de §20.5 devuelve cuatro árboles —OCTAVO (doc. 26, `DD-01`),
NOVENO (doc. 27, `R1-01`), DÉCIMO (doc. 28, `S1-01`/`S1-02`) y UNDÉCIMO (doc. 29,
`T1-01`/`T1-02`)— y la suite deriva exactamente esos cuatro. **No se crean fixtures para los
siete restantes**, y no por comodidad: §20.5 lo prohíbe expresamente —«No se les inventa aquí
un identificador ni una fase»— y §20.5 cierra con «**Y NO SE SUSTITUYE UN CARDINAL POR
OTRO**». Derivar identificadores estables para ellos sería inventarlos.

### 3.3 · El nivel de los adaptadores · **`compatible` es el nivel REAL, y `F6` no exige `soportado`**

`11-ARQ` §6.5 define el nivel como DERIVADO —«NIVEL ALCANZADO Y VIGENTE · **NO ES UN
CAMPO**»— y fija qué celdas sostienen cada valor:

```text
soportado    «`certificacion/operativo` verificado y vigente, con la prueba de humo
             EJECUTADA como evidencia, más `certificacion/integrado` verificado y vigente»
compatible   «`certificacion/estructural` verificado: existe adaptador, existe proyección y
             su huella casa»
```

Y `11-ARQ` §9.1 dice qué exige `Integrado`: «las **cinco** de `nivel-certificacion:integrado`:
`workspace check` **sobre fuentes reales** · comandos del producto · CI ejecutable · trabajo
multi-fuente verificado como conjunto · `integration-set` producido», con propietario `PLT` y
crítico «`VER` independiente». **Esas cinco exigen un producto real con sus fuentes**, que es
otra vez el nodo 8 del §18, BLOQUEADO por el nodo 9. Exigir `soportado` para certificar `F6`
sería pedir que `F6` presuponga la adopción que su propia certificación desbloquea.

**Qué contrata `F6-G`, literal:** «la ARQUITECTURA DE ADAPTADORES: definición neutral,
proyecciones generadas, huella con validador de deriva y prueba de humo en sesión nueva». Las
cuatro piezas están construidas y ejecutadas (`T191`, `T223`, `T224`). **El nivel derivado
sigue siendo `compatible` y se conserva como REAL**; `T224` comprueba además que con la celda
`certificacion/integrado` presente la derivación SÍ llega a `soportado`, de modo que lo que
falta es evidencia y no maquinaria.

---

## 4 · Límites de anfitrión, separados de lo portable

**La regla de esta sección:** una limitación local **no se convierte en cumplimiento
universal**, y una propiedad portable no se rebaja por lo que esta máquina no dé. Las cinco
columnas se dicen por separado, y lo medido es de esta pasada.

| materia | mecanismo implementado | backend / vía EJERCIDA aquí | NO ejercitable aquí, con su motivo medido | propiedad PORTABLE | propiedad certificable SÓLO en este anfitrión |
|---|---|---|---|---|---|
| **`FD-5`** contención | política por NIVEL exigido, cinco backends sondeados con motivo publicado, enchufada al ADAPTADOR, y **fallo cerrado** sin contención fuerte | **tres**, los tres a través del adaptador y con la política real: `espacio-de-nombres-de-pid`, `systemd-scope` y `contenedor`. Con los tres, hijo, nieto y bisnieto con `setsid` → **0 supervivientes**. Con `simple` → **3 supervivientes**, uno por generación | **`cgroup-v2`**: presente —`cgroup.kill` disponible y subárbol delegado `user@1000.service`— y **NO ejercitable**: el subgrupo se crea y la tarea **no entra**, `errno 5` (EIO) al migrar. **Sigue siendo cierto en esta pasada** | que sin backend fuerte **NO se ejecuta** —`ContencionFuerteNoDisponible`, no un aviso—; que el nivel se PIDE y no se deduce; que el `simple` declara su alcance inferior en el resultado; y que la detección publica el motivo de cada «no disponible» | que hijo, nieto y bisnieto con `setsid` no sobrevivan. Depende de que el anfitrión ofrezca **al menos un** backend fuerte. Donde no haya ninguno, lo demostrable es la DETECCIÓN y el FALLO CERRADO, y eso es lo que se afirma |
| **raíz externa · identidad de sistema** | firma asimétrica Ed25519 con `ssh-keygen -Y`, dos programas separados, anillo con épocas, rotación, retirada y revocación | contenedor y espacio de nombres, con identidad distinta y montaje de sólo lectura | **una IDENTIDAD DE SISTEMA dedicada**: `sudo -n true` responde «sudo: a password is required». Requisito exacto: `sudo` sin contraseña o una cuenta de servicio creada por quien administre la máquina | que el ejecutor NO comparta identidad de escritura con el runtime, y que sin verificación de lo firmado no se escriba evidencia | la independencia demostrada con una cuenta de sistema propia |
| **custodia de la clave** | fallo cerrado sin proveedor válido (`O25` §2), clave fuera de todos los repositorios | fichero `0600` fuera de todos los repositorios, **efímero y destruido al terminar** | un **proveedor de secretos del anfitrión**. `O25` §5: «Las claves efímeras están permitidas únicamente en pruebas y **no constituyen custodia productiva**» | el contrato de ciclo de vida completo y el rechazo de claves desconocidas o revocadas | **ninguna**: la custodia productiva es EXTERNA al repositorio y no se declara aquí |

---

## 5 · LA RESTA

```text
obligaciones internas de F6 − implementadas y probadas
```

**Universo de la resta.** Las obligaciones que las fuentes canónicas asignan a `F6` y que son
CONSTRUIBLES aquí: `F6-A`, `F6-B`, `F6-C`, `F6-D`, `F6-E`, `F6-F`, `F6-G`, `F6-H`, `F6-I` ·
`V6-01`…`V6-19` · `g.1`…`g.16` y los tres contratos derivados de `g.17` · `C2`, `C4` y `C5`
donde el ciclo los invoca · `C-00`, `C-01`, `C-02`, `C-03`, `C-04`, `C-13`, `C-18` · `A14`,
`FD-3`, `S1-02`, `FD-5`, `FD-6` · `F-01`, `F-02`, `F-04`, `F-05` (i), `F-06`, `F-07`, `F-10`,
`F-11` · y la condición de cierre de `M-04`.

```text
RESULTADO DE LA RESTA   ∅   (VACÍA)      ← REFUTADO. Ver el aviso inmediatamente debajo
```

> ## ⚠ ESTA RESTA FUE REFUTADA POR EL GATE DE CERTIFICACIÓN DEL 2026-09-03
>
> **Y no se corrige aquí, se registra.** El gate único e independiente de certificación
> —[`02-GATE-DE-CERTIFICACION-FINAL-20260903.md`](02-GATE-DE-CERTIFICACION-FINAL-20260903.md)—
> derivó el universo por su cuenta, **sin aceptar este documento como verdadero**, y encontró
> que **las tres restas están NO VACÍAS**. Su encargo prohibía expresamente corregir nada, de
> modo que lo que sigue es el registro del hallazgo y no su remedio.
>
> **Por qué esta resta salió vacía sin serlo, dicho con precisión.** Su universo declara
> «`F-01`, `F-02`, `F-04`, `F-05` (i), `F-06`, `F-07`, `F-10`, `F-11`» — las OCHO **filas** de
> `11-ARQ` §19 con fase `F6`. Y las ocho están cerradas: eso es cierto y el gate lo verificó una
> a una. **Pero §19 no es una tabla: es una sección**, y contiene ADEMÁS cuatro obligaciones con
> «FASE **`F6`**» escrita que no son filas `F-nn` —`CONTRATO 1`, `CONTRATO 1bis`, `CONTRATO 2` y
> el bloque `D104`—, ninguna de las cuales entró en este universo. La afirmación de exhaustividad
> que este corte publicó —«una **fila** de §19 omitida: ninguna»— **es cierta y es insuficiente:
> lo omitido no eran filas**. Y `05-PLAN` §2.1 ya lo advertía sin que nadie lo leyera así:
> define `F6-H` con sede «`11-ARQ` §19», la sección entera, y `F6-I` **es** el `CONTRATO 3` de
> esa misma sección.
>
> **Las tres restas del gate, derivadas por su adjudicador:**
>
> ```text
> A · obligaciones internas SIN implementación                    NO VACÍA · 7
>     A1  C4 «Cuántos agentes por rol» · la cardinalidad y la semántica no se derivan de la
>         composición, que es la sede que C4 designa. Medido sobre las TRES composiciones
>         reales que declaran varios agentes: se materializa UNO, sin error y sin aviso
>     A2  §19 CONTRATO 1    · AFIRMACIONES sigue siendo lista literal
>     A3  §19 CONTRATO 1bis · el censo de perfiles no se publica
>     A4  §19 CONTRATO 2    · T152 no barre toda sede que publique versión
>     A5  §19 D104          · cero instancias de <CAP>:revision, cero validadores
>     A6  b.12 paso 5   · faltan (b) grado de salida y (c) antigüedad de espera
>     A7  b.12 inanición · faltan tiempo_listo, postergaciones, adelantado_por
>
> B · implementaciones SIN prueba capaz de fallar                 NO VACÍA · 6
>     el ORDEN de los pasos 8 y 9 de estado/motor.py · las DOS mitades de exigir_vinculo por
>     separado · la degradación de V6-12 con commit_de_nacimiento=None · la procedencia del
>     sys.path en el camino productivo --repo · la declaración prohibida de varios agentes
>
> C · obligaciones SIN trazabilidad hasta evidencia               NO VACÍA · 4
>     el criterio B3 del plan —«la acepta el Owner»— sin acto · las cuatro obligaciones de §19
>     ausentes de este universo · 04-CONTRATOS-TECNICOS.md, la ÚNICA SEDE del estado de
>     construcción, desmentida por el árbol y contradictoria consigo misma · y la fila F6-B de
>     este documento, que registra un «límite de anfitrión» donde lo que falta es un acto del Owner
> ```
>
> **Lo que el gate SÍ confirmó de este documento**, y se dice porque callarlo sería la otra
> forma de mentir: la línea base es exacta y reproducible byte a byte en otro checkout; los
> diecinueve `V6-*` tienen correspondencia ejecutada e inequívoca, **incluidos los tres que
> §6.1 declara no citados por nombre**; `V6-15` deriva su conjunto y crece solo; las ocho filas
> `F-nn` están cerradas con negativos que se ponen rojos por el motivo esperado; y las
> exclusiones argumentadas de §3.1, §3.2 y §3.3 se sostienen sobre sus citas literales.

**Y lo que la resta NO barre, dicho para que nadie la lea como más de lo que es.** Quedan
fuera del universo, cada uno con su fuente literal en este documento:

```text
F6-J                    NO es construcción: es el ACTO de un juicio INDEPENDIENTE, y `O20`
                        §3 y el criterio `B6` lo reservan a quien no construyó. Su
                        precondición —que exista lo que hay que certificar— está cumplida

F-08                    fase `F5`, propietario el Owner (`11-ARQ` §19). CERRADA por `O23` §10

FD-2 · FD-4             `06-DEUDA` §10 bis: «NO se corrige aquí, y no puede corregirse aquí»

recorrido extremo a     nodo 8 del §18, BLOQUEADO por el nodo 9 hasta que `F6` esté
extremo de A y U        implementado **y certificado**  (§3.1)

nivel `soportado`       exige `certificacion/integrado`, cuyas cinco pruebas necesitan un
de un adaptador         producto real con sus fuentes: nodo 8 otra vez  (§3.3)

custodia productiva     EXTERNA al repositorio por decisión del Owner: `O25` §2
de la clave

los siete árboles sin   §20.5 los deja FUERA del conjunto que `V6-15` mide, y prohíbe
cabecera publicada      inventarles identificador  (§3.2)

cgroup v2 EJERCIDO      límite de este anfitrión, medido y publicado  (§4)
identidad de sistema
```

> **Y la regla que impide leer esta resta al revés.** Que la resta salga vacía significa que
> **no queda obligación interna de `F6` sin construir y sin ejecutar**. No significa que `F6`
> esté certificada, ni que PesquerApp se desbloquee. `IMPLEMENTADO_Y_PROBADO` no es
> `CERTIFICADO`, y el único que puede convertir lo uno en lo otro es `F6-J`.

---

## 6 · El censo FILA A FILA de `V6-01`…`V6-19` y de `g.1`…`g.16`

**Por qué existe, y quién la pidió.** La auditoría independiente de este corte encontró
que §5 declaraba a los diecinueve `V6-*` y a las dieciséis `g.N` dentro del universo de la
resta **y no los enumeraba fila a fila**: sólo aparecían como columna de cierre de las
siete filas `C-*`, y `V6-12` y `V6-19` no aparecían ni ahí. Verificó que la cobertura
existía, pero la contabilidad no, y **ésa es exactamente la forma de «lista parcial» que
este corte declara haber erradicado en `F6-H`**. Se subsana aquí.

Los dos censos se DERIVAN, y ningún cardinal se escribe:

```bash
grep -cE '^\| `V6-[0-9]+` \|' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
grep -oE '^## `g\.[0-9]+`' docs/rediseno/g-ESTADO-DURABLE-APROBADA.md
```

### 6.1 · Los `V6-*` del verificador de admisión (`F6-A`)

**La última columna dice la verdad incómoda.** No todos los contratos se CITAN por su
identificador dentro de una prueba: algunos se ejercen por la propiedad, dentro de la
batería del módulo que los implementa. Se distingue, en vez de presentar las dos cosas
como si fueran la misma.

| contrato | qué exige, en corto | se implementa en | batería que lo ejecuta | ¿citado por su identificador en la prueba? |
|---|---|---|---|---|
| **`V6-01`** | Toda lectura de Git que produzca una lista usa una representación INEQUÍVOCA | `admision/__init__.py` · `admision/errores.py` · `admision/lectura.py` | `admision` | sí |
| **`V6-02`** | Separación por NUL y decodificación estricta, o tratamiento byte a byte | `admision/__init__.py` · `admision/lectura.py` · `gobierno/git.py` | `admision` · `gobierno-git` | **no** · se ejerce por la propiedad |
| **`V6-03`** | Fallo CERRADO ante codificación inválida, truncamiento o estructura inesperada | `admision/__init__.py` · `admision/errores.py` · `admision/formulas.py` | `admision` | **no** · se ejerce por la propiedad |
| **`V6-04`** | Inventario DERIVADO de todas las lecturas Git; ninguna vía paralela oculta | `admision/__init__.py` · `admision/censo.py` · `admision/errores.py` | `admision` | sí |
| **`V6-05`** | La admisión juzga la MUTACIÓN, no la mera existencia del fichero | `admision/__init__.py` · `admision/mutacion.py` · `admision/perimetro.py` | `admision` · `arboles-adversariales` | sí |
| **`V6-06`** | Se cubren A, M, D, T, R y C, incluidas las DOS puntas de renombrados y copias | `admision/lectura.py` · `admision/matriz.py` · `admision/mutacion.py` | `admision` | sí |
| **`V6-07`** | Se comparan revisión base, HEAD, índice y árbol de trabajo, según corresponda | `admision/lectura.py` · `admision/mutacion.py` | `admision` | **no** · se ejerce por la propiedad |
| **`V6-08`** | Un cambio YA COMMITEADO no queda exento | `admision/mutacion.py` · `arboles/ataques.py` | `admision` | sí |
| **`V6-09`** | Se cubren ficheros NUEVOS y PREEXISTENTES | `admision/__init__.py` · `admision/mutacion.py` · `admision/perimetro.py` | `admision` | sí |
| **`V6-10`** | Se cubren TODAS las sedes normativas, instrumentales y de entrada | `admision/__init__.py` · `admision/censo.py` · `admision/errores.py` | `admision` · `e2e-f6` | sí |
| **`V6-11`** | La regla de perímetro y la propiedad de admisión NO pueden excluirse a sí mismas | `admision/__init__.py` · `admision/errores.py` · `admision/perimetro.py` | `admision` | sí |
| **`V6-12`** | La sede del Owner conserva su contrato APPEND-ONLY —fuente: O19, que crea la sede con ese contr | `admision/__init__.py` · `admision/errores.py` · `admision/lectura.py` | `admision` | sí |
| **`V6-13`** | Se prueban UTF-8, Latin-1 inválido, espacios, saltos de línea, guiones y Unicode | `admision/__init__.py` · `admision/matriz.py` | `admision` | sí |
| **`V6-14`** | Se incluyen adición, modificación, borrado, renombrado, copia y cambio de tipo | `admision/__init__.py` · `admision/matriz.py` | `admision` | sí |
| **`V6-15`** | Los ÁRBOLES ADVERSARIALES que su ENTRADA entrega quedan como FIXTURES OBLIGATORIOS | `admision/__init__.py` · `admision/censo.py` · `ads_arboles.py` | `admision` · `arboles-adversariales` · `e2e-f6` | sí |
| **`V6-16`** | La prueba se ejecuta desde una RAÍZ DE CONFIANZA EXTERNA al árbol comprobado | `admision/__init__.py` · `identidad/proveedor.py` | `admision` · `e2e-f6` · `raiz-externa` | sí |
| **`V6-17`** | Ningún digest calculado por el mismo árbol basta como prueba de su propia integridad | `admision/__init__.py` · `admision/errores.py` · `admision/perimetro.py` | `admision` | sí |
| **`V6-18`** | CERO falsos verdes, y los controles sanos SIN falsos rojos | `admision/__init__.py` · `admision/matriz.py` | `admision` | sí |
| **`V6-19`** | Cada FÓRMULA COMPARTIDA por varios instrumentos tiene UNA SOLA SEDE, y sus consumidores la IMPO | `admision/__init__.py` · `admision/censo.py` · `admision/errores.py` | `admision` | sí |

> **Los que NO se citan por su identificador dentro de una prueba son `V6-02` · `V6-03` · `V6-07`.** Se ejercen por
> la PROPIEDAD, dentro de la batería del módulo que los implementa, y su evidencia es la
> de esa batería. **No se presentan como «probados uno a uno por su nombre»**, porque no
> lo están: quien quiera esa trazabilidad nominal tiene aquí dicho dónde falta.

### 6.2 · Las condiciones de la sección `(g)`, `g.1`…`g.16`

**El reparto NO se inventa aquí: lo declara `(g)` §16** y lo recoge
[`00-ESTADO-DE-IMPLEMENTACION-F6.md`](00-ESTADO-DE-IMPLEMENTACION-F6.md) §3. Las nueve
condiciones observables `G-A1`…`G-A9` son la forma en que `(g)` se deja MEDIR, y cada
`g.N` se cierra por la condición que la cubre. `g.0` y `g.17`–`g.18` quedan fuera del
universo y se dice por qué: `g.0` es la frontera entre norma y mecanismo, `g.17` nombra
los contratos derivados —que sí están en la matriz, en §1— y `g.18` es «lo que esta
sección NO hace». Ninguna de las tres es una obligación construible.

| condición | materia | contrato derivado que la cierra | batería que la ejecuta | condición observable |
|---|---|---|---|---|
| **`g.1`** | Componentes obligatorios del estado durable | contrato de ESTADO DURABLE (`g.1`–`g.13`) | `estado-durable` · `estado-e2e` | `G-A1…G-A7` |
| **`g.2`** | Invariantes semánticos | contrato de ESTADO DURABLE (`g.1`–`g.13`) | `estado-durable` · `estado-e2e` | `G-A1…G-A7` |
| **`g.3`** | Atomicidad | contrato de ESTADO DURABLE (`g.1`–`g.13`) | `estado-durable` · `estado-e2e` | `G-A1…G-A7` |
| **`g.4`** | Durabilidad | contrato de ESTADO DURABLE (`g.1`–`g.13`) | `estado-durable` · `estado-e2e` | `G-A1…G-A7` |
| **`g.5`** | Integridad | contrato de ESTADO DURABLE (`g.1`–`g.13`) | `estado-durable` · `estado-e2e` | `G-A1…G-A7` |
| **`g.6`** | Concurrencia | contrato de ESTADO DURABLE (`g.1`–`g.13`) | `estado-durable` · `estado-e2e` | `G-A1…G-A7` |
| **`g.7`** | Diario | contrato de ESTADO DURABLE (`g.1`–`g.13`) | `estado-durable` · `estado-e2e` | `G-A1…G-A7` |
| **`g.8`** | Recuperación | contrato de ESTADO DURABLE (`g.1`–`g.13`) | `estado-durable` · `estado-e2e` | `G-A1…G-A7` |
| **`g.9`** | Reconciliación | contrato de ESTADO DURABLE (`g.1`–`g.13`) | `estado-durable` · `estado-e2e` | `G-A1…G-A7` |
| **`g.10`** | Versionado | contrato de ESTADO DURABLE (`g.1`–`g.13`) | `estado-durable` · `estado-e2e` | `G-A1…G-A7` |
| **`g.11`** | Migración | contrato de ESTADO DURABLE (`g.1`–`g.13`) | `estado-durable` · `estado-e2e` | `G-A1…G-A7` |
| **`g.12`** | Propiedad y autoridad de escritura | contrato de ESTADO DURABLE (`g.1`–`g.13`) | `estado-durable` · `estado-e2e` | `G-A1…G-A7` |
| **`g.13`** | Auditabilidad | contrato de ESTADO DURABLE (`g.1`–`g.13`) | `estado-durable` · `estado-e2e` | `G-A1…G-A7` |
| **`g.14`** | Gobierno Git del REPOSITORIO DE CONTROL | contrato de GOBIERNO GIT DEL CONTROL REPO | `gobierno-git` · `multimaquina` | `G-A8` |
| **`g.15`** | Frontera con la RAÍZ EXTERNA DE CONFIANZA | contrato de RAÍZ EXTERNA DE CONFIANZA | `raiz-externa` · `e2e-f6` | `G-A9` |
| **`g.16`** | Condiciones observables de aceptación | las nueve condiciones observables de aceptación | las tres anteriores | `G-A1…G-A9` |

> **Y la regla que impide leer esta tabla al revés, otra vez.** Que las dieciséis tengan
> fila y batería significa que están IMPLEMENTADAS Y PROBADAS. **No significa que `(g)`
> esté certificada**: demostrar una condición de aceptación y certificar son actos
> distintos, y el segundo es de `F6-J`.
