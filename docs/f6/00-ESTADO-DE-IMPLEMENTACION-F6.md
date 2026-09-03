# `F6` · ESTADO DE IMPLEMENTACIÓN

**Qué es este documento.** El registro de **qué está implementado y probado de `F6`, qué no,
y qué lo bloquea**, más las **decisiones técnicas** que `F6` ha tomado bajo la autoridad que
`O24` §2 le reconoce. Es **DERIVADO**: no crea autoridad, no aprueba nada y no certifica
nada.

**Qué NO es.** No es un plan —el plan ya existe y es
[`05-PLAN-DE-IMPLEMENTACION-F5-F6.md`](../canonico/05-PLAN-DE-IMPLEMENTACION-F5-F6.md), y
este documento **no lo repite**—. No es norma: la norma de esta materia es la sección
[`(g)`](../rediseno/g-ESTADO-DURABLE-APROBADA.md). No es la sede del estado de las fases:
ésa es [`03-GOBIERNO-Y-AUTORIDAD.md`](../canonico/03-GOBIERNO-Y-AUTORIDAD.md) §6. Y no es la
sede de lo CONSTRUIDO frente a lo DISEÑADO: ésa es
[`04-CONTRATOS-TECNICOS.md`](../canonico/04-CONTRATOS-TECNICOS.md) §1.

**Acto habilitante:** la resolución `O24`, en la
[sede canónica del Owner](../owner/ADS-OWNER-RESOLUCIONES.md).

> **Y LA TABLA DE `(g)` NO SE TOCA.** `(g)` §17 lleva una tabla que dice «NO CONSTRUIDO» de
> sus tres contratos derivados. **Esa tabla describe el estado EN EL MOMENTO DE SU
> APROBACIÓN**, que es el 2026-09-02, y `(g)` es norma aprobada, no un ledger de
> implementación: editarla para «corregirla» sería reescribir material aprobado por una
> razón que no es normativa. El estado vigente se registra AQUÍ, fuera de `(g)`, y quien lea
> aquella tabla ha de leerla con su fecha.

---

## 1 · El censo de contratos de `F6` NO se escribe: se deriva

```bash
# los contratos del VERIFICADOR DE ADMISIÓN, con su reparto por clasificación
grep -cE '^\| `V6-[0-9]+` \|' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
grep -oE '^\| `V6-[0-9]+`.*\| (`CONTRATO_[A-Z_]+`)' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
  | grep -oE 'CONTRATO_[A-Z_]+' | sort | uniq -c
# los contratos DERIVADOS que la sección (g) nombra
grep -nE '^\| \*\*contrato de' docs/rediseno/g-ESTADO-DURABLE-APROBADA.md
# el conjunto de ÁRBOLES ADVERSARIALES de §20.5, que tampoco se enumera
grep -nE '^## [0-9]+ · EL [A-ZÁÉÍÓÚ]+ ÁRBOL' docs/evolucion/[0-9][0-9]-*.md
```

**Dos familias, y confundirlas sería el error.** Los `V6-*` son los puntos del **verificador
de admisión** (`F6-A`), y su sede es `11-ARQ` §20.1. Los **contratos derivados** son los tres
que `g.17` nombra, y su norma es la sección `(g)`. Ninguna de las dos se copia aquí.

## 2 · La cadena crítica, y dónde está este corte

```text
(g) APROBADA  →  ESTADO DURABLE  →  RUNTIME  →  VERIFICADOR Y RAÍZ EXTERNA  →  CERTIFICACIÓN
     `O23`         corte 1           corte 2         ESTE MACROBLOQUE            `F6-J`
                                                                                    │
                                                                                    ▼
                                                                        PRIMERA ADOPCIÓN REAL
                                                                          — PesquerApp —
```

**Este macrobloque construye el último eslabón antes de la certificación**, y sólo ése. El
grafo de dependencias completo vive en
[`05-PLAN-DE-IMPLEMENTACION-F5-F6.md`](../canonico/05-PLAN-DE-IMPLEMENTACION-F5-F6.md) §3.

## 3 · Clasificación por contrato

**Vocabulario cerrado**, y ninguna fila usa una categoría vaga:

```text
IMPLEMENTADO_Y_PROBADO           hay código ejecutable y pruebas ejecutadas en verde
PARCIAL                          hay código ejecutable que cubre PARTE del contrato, y se
                                 dice exactamente qué parte y qué queda
NO_IMPLEMENTADO                  no hay código. El contrato está escrito y nada más
BLOQUEADO_POR_DEPENDENCIA        falta otro contrato de F6 que va antes
BLOQUEADO_POR_DECISION_DEL_OWNER falta un acto del Owner, DECLARADO y con su condición
EXTERNO                          su sujeto vive fuera de este repositorio
PENDIENTE_DE_CERTIFICACIÓN       está implementado y probado, y espera el juicio
                                 independiente que `F6-J` emitirá. NO es «certificado»
```

| contrato | sede | clasificación | qué lo cierra |
|---|---|---|---|
| **contrato de ESTADO DURABLE** (`g.1`–`g.13`) | [`g.17`](../rediseno/g-ESTADO-DURABLE-APROBADA.md) · derivado en [`CONTRATO-ESTADO-DURABLE.md`](../../kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md) | **IMPLEMENTADO_Y_PROBADO** · PENDIENTE_DE_CERTIFICACIÓN | — |
| **`A14` · guarda de entorno** (corte `V1` · `F6-I`) | [`06-DEUDA`](../canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md) §4 | **IMPLEMENTADO_Y_PROBADO** · PENDIENTE_DE_CERTIFICACIÓN | — |
| **`FD-3` · la especificación normativa viaja al proyecto instalado** | [`06-DEUDA`](../canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md) §10 bis | **IMPLEMENTADO_Y_PROBADO** · PENDIENTE_DE_CERTIFICACIÓN | — |
| **contrato de GOBIERNO GIT DEL CONTROL REPO** (`g.14`) | [`g.17`](../rediseno/g-ESTADO-DURABLE-APROBADA.md) · derivado en [`CONTRATO-GOBIERNO-GIT-CONTROL.md`](../../kernel/operativo/runtime/CONTRATO-GOBIERNO-GIT-CONTROL.md) | **IMPLEMENTADO_Y_PROBADO** · PENDIENTE_DE_CERTIFICACIÓN — la serialización entre MÁQUINAS y la publicación a un remoto, que era lo pendiente, se demuestra con remoto bare, dos clones, dos procesos e identidades distintas en `T221`–`T222` | — |
| **contrato de RAÍZ EXTERNA DE CONFIANZA** (`g.15`) · **`V6-16`** | [`g.17`](../rediseno/g-ESTADO-DURABLE-APROBADA.md) · `11-ARQ` §11.8 · `O25` | **IMPLEMENTADO_Y_PROBADO** · PENDIENTE_DE_CERTIFICACIÓN — paquete e instalación separados FUERA del árbol, proceso ejecutor propio, firma **ASIMÉTRICA** Ed25519 con `ssh-keygen -Y`, ciclo de vida completo de la identidad —rotación, solapamiento por épocas, retirada y revocación— en el anillo Y en el punto ejecutable, y la independencia MEDIDA con identidad distinta y montaje de sólo lectura | — · su **custodia productiva** sigue siendo `EXTERNO`, ver la última fila |
| **`V6-01`…`V6-19` · verificador de admisión** (`F6-A`) | `11-ARQ` §20.1 · derivado en [`CONTRATO-ADMISION.md`](../../kernel/operativo/runtime/CONTRATO-ADMISION.md) | **IMPLEMENTADO_Y_PROBADO** · PENDIENTE_DE_CERTIFICACIÓN — **los diecinueve**. `V6-15` y `V6-16`, que eran los dos que faltaban, quedan construidos, y el veredicto ya **no publica ninguna lista `fuera_de_alcance`**: publica la PROCEDENCIA de cada uno | — |
| **`V6-15` · árboles adversariales** | `11-ARQ` §20.5 · derivado en [`CONTRATO-ARBOLES-ADVERSARIALES.md`](../../kernel/operativo/runtime/CONTRATO-ARBOLES-ADVERSARIALES.md) | **IMPLEMENTADO_Y_PROBADO** · PENDIENTE_DE_CERTIFICACIÓN — el conjunto se DERIVA de las cabeceras publicadas, con su documento y su hallazgo; cada árbol se materializa en un repositorio real, se reproduce contra su versión histórica vulnerable, y la vigente lo rechaza POR LA PROPIEDAD. `entrada − suite = ∅` y `suite − entrada = ∅` | — |
| **`F6-D` · runtime y dispatcher** | `11-ARQ` §7 · derivado en [`CONTRATO-RUNTIME-Y-DISPATCHER.md`](../../kernel/operativo/runtime/CONTRATO-RUNTIME-Y-DISPATCHER.md) y en [`CONTRATO-CICLO-Y-MACROCIRCUITOS.md`](../../kernel/operativo/runtime/CONTRATO-CICLO-Y-MACROCIRCUITOS.md) | **IMPLEMENTADO_Y_PROBADO** · PENDIENTE_DE_CERTIFICACIÓN — las OCHO etapas del `§7.2`, incluidas la **declaración de acoplamiento** del paquete durable con `lee_fuentes` y `escribe_fuentes` (`E2.2`) y la **condición COMPUESTA de paralelismo** de `a.5` con sus seis condiciones, más el **freno de devoluciones** de `a.7`, que se ACUMULA. Y `Continúa` de `§7.4` con sus siete pasos, sus diez escenarios y su idempotencia medida · y los SIETE pasos de `C4`, incluidos los DOS que faltaban: el **paso 4** —política de `C2` aplicada rol a rol, modelo elegido y descartados **con el motivo y la regla que los produjo**— y el **paso 1**, que LEE el paquete de verdad —capacidad responsable, modo derivado de los pasos del método, objetivo, nivel de calidad con sus gates, y declaración de acoplamiento normalizada— y falla cerrado por siete rutas. `execution_slots` corta por **AGENTE** y ya no puede separar un par que la composición declara `combinables`. Batería `agentes`, `T226`–`T239` y `T249`, con **once sabotajes** que la ponen roja | — · lo único que NO se ejecuta de `C4` es la derivación del CARDINAL de agentes por rol desde la prosa del campo `agentes` de la composición, que exigiría reglas léxicas sobre texto libre; «1 por defecto, siempre» y la prohibición de varios agentes sin integrador SÍ se ejecutan |
| **`F6-F` · los cuatro macrocircuitos** | `11-ARQ` §8, §9.6 y §18 | **IMPLEMENTADO_Y_PROBADO** · PENDIENTE_DE_CERTIFICACIÓN — los cuatro DERIVADOS de la tabla de §18, ejecutados por un motor ÚNICO parametrizado, con `FASE 0` compartida, sus seis identificadores de sujeto, su soporte durable propio y las once filas adversariales `X-S1`–`X-S11` | **NADA que sea obligación interna de `F6`.** El recorrido de TODAS las fases de `A` y de `U` extremo a extremo **es el nodo 8 del §18** —«PRIMERA ADOPCIÓN REAL `O14` · `O15` PesquerApp … **BLOQUEADA por 9** … sin MVP, sin piloto desechable y sin adopción parcial»—, y §14 lo dice de sus doce escenarios: «Lo que NO demuestran: que funcionen. Para eso hace falta el piloto de `O14`». Hacerlo ahora sería el piloto desechable que §20.2 prohíbe. Se recorre la primera fase de los cuatro, y la composición de las trece filas se comprueba una a una |
| **`F6-G` · arquitectura de adaptadores** (corte `V7`) | `11-ARQ` §6 · derivado en [`CONTRATO-ADAPTADOR.md`](../../kernel/operativo/runtime/CONTRATO-ADAPTADOR.md) | **IMPLEMENTADO_Y_PROBADO** · PENDIENTE_DE_CERTIFICACIÓN — las CUATRO piezas, incluida la **pieza 4**: la prueba de humo en sesión nueva, con sus diez pasos, su repetición desde otra sesión limpia y los cuatro desenlaces de §6.7 | el **NIVEL** que §6.5 asigna se DERIVA y hoy sale **`compatible`**, no `soportado`: no existe celda `certificacion/integrado`, cuyas **cinco** pruebas §9.1 fija sobre **fuentes reales** —`workspace check`, comandos del producto, CI ejecutable, trabajo multi-fuente y `integration-set`—, y eso es otra vez el nodo 8 del §18, BLOQUEADO por el nodo 9. **La certificación de `F6` NO exige ese nivel**: `F6-G` contrata las cuatro piezas, y las cuatro están. `T224` comprueba que con la celda presente la derivación SÍ llega a `soportado`, de modo que lo que falta es EVIDENCIA y no maquinaria. **No se presupone**, se deriva |
| **`FD-5` · aislamiento de procesos** | [`06-DEUDA`](../canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md) · derivado en [`CONTRATO-CONTENCION.md`](../../kernel/operativo/runtime/CONTRATO-CONTENCION.md) | **IMPLEMENTADO_Y_PROBADO en este anfitrión** · PENDIENTE_DE_CERTIFICACIÓN — con la política de contención, hijo, nieto y bisnieto haciendo `setsid` NO sobreviven a la cancelación; con el backend simple, el que se sale del grupo SÍ sobrevive, y esa pareja de pruebas es la que impide presentar el débil como fuerte. **Y ahora también A TRAVÉS DEL ADAPTADOR y con la POLÍTICA real**, que es donde la deuda está escrita: `T247` ejerce CADA backend fuerte disponible —tres en este anfitrión— y `T248` comprueba que sin ninguno el adaptador **no ejecuta**, en vez de degradar | **NO se declara cerrado para un anfitrión CUALQUIERA**: la contención fuerte depende del anfitrión. Donde no haya ninguno de los mecanismos, lo demostrado es la DETECCIÓN y el FALLO CERRADO. `cgroup v2` está presente y **NO se pudo ejercer** aquí: el subgrupo se crea y la tarea no entra. **Comprobado otra vez en este corte y sigue siendo cierto**: `cgroup.kill` disponible, subárbol delegado `user@1000.service`, y `errno 5` (EIO) al migrar la tarea. El reparto entre lo portable y lo local está en la [matriz de completitud](01-MATRIZ-DE-COMPLETITUD-F6.md) §4 |
| **`F6-H` · hallazgos externos con propietario y fase `F6`** | `11-ARQ` §19 | **PARCIAL** · **rebajado por el [GATE DE CERTIFICACIÓN del 2026-09-03](02-GATE-DE-CERTIFICACION-FINAL-20260903.md)**, que derivó §19 ENTERA y encontró que la sección contiene, además de las filas `F-nn`, cuatro obligaciones con «FASE `F6`» escrita —`CONTRATO 1`, `CONTRATO 1bis`, `CONTRATO 2` y el bloque `D104`— que este inventario NO recogía y que NO están cumplidas. Lo que sigue siendo cierto: **«el resto de su lista» ya no existe: la lista está ENUMERADA una a una** en la [matriz de completitud](01-MATRIZ-DE-COMPLETITUD-F6.md) §2. Las OCHO filas de `11-ARQ` §19 con fase `F6` quedan cerradas —`F-01` mitad de `F6`, `F-02`, `F-04`, `F-05` (i), `F-06`, `F-07`, `F-10` y `F-11`—, cada una con prueba ejecutable propia —`T240`–`T246`— y con **catorce sabotajes** que la ponen ROJA al reintroducir el defecto. Las siete filas `CONTRATO_COMPLETO_PARA_F6` de la matriz de los 22 cierran por los `V6-*` que ellas mismas nombran, y `A14`, `FD-3`, `S1-02`, `FD-5` y `FD-6` están cada una con su evidencia | **`F-08` NO es de `F6`**: su fase es `F5` y su propietario es el Owner —`11-ARQ` §19—, y `O23` §10 ya emitió su nota de vigencia |
| **`F6-J` · CERTIFICACIÓN** | `O20` §3 | **BLOQUEADO_POR_DEPENDENCIA** · el juicio independiente **YA SE EMITIÓ** el 2026-09-03 y su veredicto fue **`F6 NO CERTIFICADA`** sobre un gate declarado **NO VÁLIDO** por cobertura incompleta de uno de sus dos revisores. Sede: [`02-GATE-DE-CERTIFICACION-FINAL-20260903.md`](02-GATE-DE-CERTIFICACION-FINAL-20260903.md) | los siete pendientes internos de su resta `A`, las seis propiedades de su resta `B`, las cuatro de su resta `C`, **un gate posterior VÁLIDO**, y el acto del Owner que `O18` reserva y que `F6-B` declara indelegable. **Ya NO es cierto que «ya existe lo que hay que certificar»** |
| **custodia productiva de la clave de firma** | `FD-1` · `O25` §2 | **EXTERNO** al repositorio, y **decidido**: identidad de servicio dedicada del verificador externo, con un proveedor de secretos del anfitrión | que exista ese proveedor en el anfitrión de la instalación. En este árbol la clave es un fichero `0600` fuera de todos los repositorios, generado efímero y destruido al terminar; **eso no es custodia productiva y `O25` §5 lo dice** |

> **Y la regla que impide leer esta tabla al revés.** `IMPLEMENTADO_Y_PROBADO` **no es
> CERTIFICADO**. La certificación de `F6` la emite un juicio independiente, y **no quien
> construyó** —criterio `B6`—. Nada de esta tabla desbloquea PesquerApp.

**Cómo se reparten las nueve condiciones de `g.16`.** `(g)` §16 dice que una implementación
satisface **la sección** cuando **las nueve** se demuestran sobre un árbol real, con
escenario positivo y negativo. El reparto es éste, y **las nueve están demostradas**:

```text
contrato de ESTADO DURABLE  ·  g.1–g.13   →  G-A1 · G-A2 · G-A3 · G-A4 · G-A5 · G-A6 · G-A7
                                              las SIETE, en T173–T179

contrato de GOBIERNO GIT    ·  g.14       →  G-A8  DEMOSTRADA en sus DOS mitades: IMPOSIBLE
DEL CONTROL REPO                              —el hook rechaza el forzado en sus tres formas,
                                              incluido el OID nulo— y DETECTABLE —el linaje
                                              DURABLE denuncia un forzado aunque el hook se
                                              hubiera quitado—. Y entre MÁQUINAS, con remoto
                                              bare, dos clones y dos procesos: T187, T221, T222

contrato de RAÍZ EXTERNA    ·  g.15       →  G-A9  DEMOSTRADA con una raíz externa REAL: un
DE CONFIANZA                                  árbol que se autodeclara VERDE es DESMENTIDO
                                              por una atestación firmada ASIMÉTRICAMENTE,
                                              emitida por un proceso separado con identidad
                                              que NO puede escribir en el árbol. T220, T225
```

> **Y la consecuencia, dicha con su límite:** las nueve condiciones observables de `g.16`
> están demostradas sobre un árbol real. **Eso NO es la certificación de `(g)` ni la de
> `F6`**: demostrar una condición de aceptación y certificar son actos distintos, y el
> segundo es de `F6-J`.

## 4 · Los validadores documentales NO son el runtime de `F6`

**Se dice porque la confusión es barata y cara de deshacer.** La batería del corpus
—`ads_lint.py`, `comprobar_*.py`, sus controles negativos y su evidencia publicada— comprueba
la **CONSISTENCIA DEL CORPUS**. El runtime de `F6` es otra cosa: **ejecuta**. Un verde de la
batería no dice nada sobre si el motor funciona, y por eso el runtime trae **sus propias
baterías**, registradas en el manifiesto canónico de validadores y con su propia evidencia.

## 5 · Decisiones técnicas de `F6`, con sus alternativas

**Autoridad:** `O24` §2 y `g.0`. Ninguna de estas decisiones es norma nueva, ninguna rebaja
una invariante y **ninguna vuelve al Owner**. Las de los cortes 1 y 2 se leen en sus
contratos derivados. Éstas son las de ESTE macrobloque:

| decisión | alternativas descartadas | por qué |
|---|---|---|
| **la firma de la raíz externa es `ssh-keygen -Y` con Ed25519** | `gpg` · `openssl` · una biblioteca de terceros · seguir con el MAC simétrico | `O25` §5 prohíbe primitivas propias y pide criptografía estándar y un proveedor mantenido. `ssh-keygen` es herramienta del anfitrión, trae espacio de nombres y fichero de firmantes autorizados ya definidos, y **no obliga a escribir protocolo**. `gpg` arrastra anillo con estado, agente y caducidades; `openssl` obligaría a elegir a mano formato y empaquetado. El MAC simétrico está DESCARTADO por lo que es: quien verifica podría firmar, y con eso `V6-16` se cae entero |
| **firmar y verificar son DOS programas** | un binario con dos subórdenes | juntar los dos poderes en una sola ruta ejecutable es exactamente lo que la separación de poderes de `g.13` prohíbe. El firmante se NIEGA a verificar; el verificador no tiene clave privada |
| **la ruta del ciclo se elige por MATERIA y ESTADO declarados** | emparejar palabras del título o de la expresión del Owner | con lo léxico, renombrar un item cambia su proceso y un sinónimo activa una ruta que nadie pidió. `b.1` dice que el proceso lo determina el RESULTADO PERSEGUIDO, que es una declaración del encuadre y no una propiedad estadística de su prosa. Y el par —y no sólo la materia— porque `FEA` y `GAP` sólo se distinguen por el estado del objeto |
| **`b.16` se DERIVA de sus bloques `ads:proceso`; §18 se contrasta contra el documento** | copiar los diez procesos y las trece filas a mano en el kernel | una lista a mano al lado de un documento que cambia envejece en silencio, que es `FD-3` otra vez. `11-ARQ` **no viaja** al proyecto instalado, así que la tabla de §18 se lleva como dato derivado y una prueba comprueba que sigue coincidiendo con el documento |
| **un solo motor de macrocircuito, parametrizado** | cuatro ejecutores, uno por circuito | la regla 6 de `O17` exige el MISMO contrato y el MISMO mecanismo compartido. Con cuatro implementaciones, la `FASE 0` divergiría en cuanto alguien tocara una; con una, las cuatro pasan por el mismo punto de despacho y la batería lo mide |
| **el soporte de la `FASE 0` es propio, inmutable y direccionado por contenido** | escribirlo en `estado/` · no escribirlo | en `estado/` es imposible: nace DESPUÉS de la fase. No escribirlo dejaría indemostrable «exactamente una por ejecución», que es la regla 1 |
| **el censo de `V6-04` barre TAMBIÉN `arboles/`, con su vía histórica DECLARADA** | dejar `arboles/` fuera del censo, que es lo cómodo | `arboles/` reproduce a propósito una lectura de lista sin `-z`, porque ése ES el defecto que `S1-01` fue. Dejar el paquete fuera del censo habría dejado sin enumerar una superficie entera —justo el modo de fallo de `S1-01`—. Se mete dentro, la vía histórica se PUBLICA acotada por `(paquete, módulo)`, y lo que no esté en esa tabla sigue dando ROJO también dentro de `arboles/` |
| **los envoltorios de proceso se DERIVAN por cierre transitivo** | añadir los nombres que se escapaban a la lista `INVOCADORES` · retirar la lista y censar toda mención | una lista de nombres se esquiva escribiendo otro nombre, y así fue: envolver `subprocess.run` en un `_git_historico()` local hacía desaparecer del censo una lectura insegura. Retirar la lista produciría FALSOS ROJOS sobre menciones, y un censo con falsos rojos se acaba desactivando. Derivar qué funciones alcanzan un proceso no depende de que nadie mantenga nada |
| **la contención se enchufa al adaptador por POLÍTICA, y sin política no cambia nada** | activar la contención siempre · dejarla como paquete suelto sin enchufar | activarla siempre convertiría un anfitrión sin `cgroups` ni espacios de nombres en un anfitrión que no puede ejecutar. Dejarla sin enchufar habría dejado `FD-5` cerrado en un paquete y abierto en el adaptador, que es donde la deuda estaba escrita. Con política: contención fuerte o **FALLO CERRADO**, nunca degradación silenciosa |
| **el resolvedor del puntero del control repo vive en el ADAPTADOR** | dejarlo dentro del guion de la prueba de sesión nueva, que es donde nació | allí la capacidad existiría SÓLO mientras corre la prueba: ningún entorno real podría usarla, y §6.7 quedaría con una regla que nadie implementa mientras su prueba pasa en verde |
| **la AUTORIDAD de cada documento del Owner se declara en `exclusiones.yaml` y se DERIVA de su clase canónica** | escribir el campo dentro de cada fichero de `docs/owner/`, que es lo que la fila `F-07` pide literalmente · llevar al Owner la elección del valor | dos de los tres ficheros son `AUTORIDAD_SUPERIOR` en `FUENTES-CANONICAS.yml`, y la condición de contenido de esa clase es **append-only contra el nacimiento**: insertar una línea de metadatos en su cabecera es reescribir lo publicado, y `V6-12` lo da en ROJO. Sólo un resultado es conforme con las dos normas, así que **no hay decisión del Owner que tomar**. Y el valor tampoco se elige: `AUTORIDAD_SUPERIOR → aprobada` y `NO_APLICABLE_A_IMPLEMENTACION → trabajo`, con ROJO si alguien escribe otro. **No se ha alterado un solo byte de ningún documento del Owner** |
| **el sufijo de variante de una capacidad se declara en el propio esquema, y `OWNER` va a un campo de autoridad separado** | dejar `capacidad_productora` como texto libre · admitir cualquier `<CAP>:<algo>` · tratar `OWNER` como la decimosexta capacidad | `F-02` fija el vocabulario entero y `E4.3` ya corrigió la fuente aprobada: sin tipar, nada impide que vuelva a entrar un MÉTODO donde va una capacidad, que es la raíz de `F-01`. Con la variante declarada, ampliar el conjunto pasa a ser un acto normativo con su sede en vez de una cadena nueva en un fichero. `OWNER` no es una de las quince, y resolverlo como `ref` lo convertiría en una |
| **la lista de variantes se resuelve con `variantes_desde` y no con un ancla YAML** | un ancla `&`/`*`, que es lo natural en YAML · repetir la lista dos veces en el mismo fichero | `runtime/ciclo/corpus.py` analiza estos mismos esquemas con un analizador propio de biblioteca estándar —el runtime VIAJA y no puede depender de PyYAML— y ese subconjunto **rechaza anclas, alias y etiquetas**. Un ancla deja el esquema legible para el validador e ILEGIBLE para el runtime, que es la peor de las dos verdades: sólo se descubre ejecutando, y así se descubrió. Repetir la lista crearía dos sitios donde puede divergir |
| **el analizador de los bloques `ads:*` del ciclo es propio y stdlib** | depender de PyYAML en el runtime | `runtime/` VIAJA a cada proyecto instalado: PyYAML pasaría de dependencia de desarrollo a dependencia de todo producto gobernado. La equivalencia **se mide** contra PyYAML sobre los bloques del corpus y sus esquemas |

## 5 bis · La auditoría independiente de este macrobloque, y qué cambió por ella

**Quién.** Un auditor que no construyó nada de este macrobloque, con el encargo de romperlo,
y que **no escribió un byte en el árbol**: sus ataques se hicieron sobre copias, y al
terminar `git status --porcelain` seguía vacío y `HEAD` seguía siendo el mismo commit.

**Lo que intentó y NO consiguió**, que informa tanto como lo que sí: mover una ruta por texto
libre, sinónimo, acento, mayúscula, guion bajo, espacio o espacio de ancho cero —nueve
variantes, nueve rechazos tipados— · que dos macrocircuitos incompatibles corrieran a la vez
—**treinta carreras con procesos reales, treinta veces un solo ganador**— · que dos máquinas
confirmaran a la vez —**veinticinco repeticiones, ninguna doble confirmación**— · forjar una
firma con lo que tiene el verificador · cambiar desde dentro del árbol la autoridad aceptada
—seis vías, seis rechazos— · escribir en el árbol desde la identidad externa —**ocho de ocho
impedidos, con los dos controles del control en verde**— · escapar del aislamiento con
`setsid` · contaminar la sesión nueva con un `PYTHONPATH` envenenado · **repetir un efecto
tras cinco `SIGKILL` en ventanas distintas —cuatro paquetes, cuatro efectos, cero
duplicados—** · encontrar un mock o un fixture que sustituyera comportamiento —cero en las
diecisiete baterías y escenarios— · encontrar `pid`, hora o ruta absoluta en el estado
canónico con el adaptador REAL · y desmentir la huella, que recalculó **con su propia
implementación** sobre 380 ficheros obteniendo el mismo valor.

**Lo que SÍ encontró, y se corrigió en la única pasada de corrección:**

| defecto | clasificación | qué se hizo |
|---|---|---|
| el punto ejecutable de la raíz externa **FIRMABA pero no VERIFICABA**: con una clave que el anillo NO acepta, emitía un veredicto VERDE con código 0 y estampaba en la atestación la identidad y la huella de la clave legítima. `comprobar` lo detectaba después, pero detectarlo después no es fallar cerrado | **BLOQUEA LA CANDIDATA** | se **verifica lo que se acaba de firmar**, contra el fichero de firmantes que sólo tiene claves públicas, y sin verificación **no se escribe evidencia**. Reproducido el ataque del auditor: con la clave intrusa, código 1 y cero evidencia; con la legítima, código 0 |
| la regla «`independientes` manda sobre `combinables`» —la prohibición más sensible de `C4`— **se podía borrar entera** y las 48 pruebas seguían verdes: la que la cubría recorría un conjunto VACÍO en el corpus real y su `assertRaises` disparaba la rama trivial | **BLOQUEA LA CANDIDATA** | prueba nueva con el conflicto que el corpus no tiene, **con su control**: sin la declaración de independencia los mismos roles pasan. Verificado que se pone ROJA al sabotear las dos mitades de la regla |
| la independencia AUTOR/REVISOR de los gates era **OPCIONAL**: `if autor and ...`, de modo que los veintidós gates del censo se superaban firmándolos uno mismo con sólo omitir el campo | **BLOQUEA LA CANDIDATA** | `autor` es **obligatorio**, se valida contra las quince capacidades y el Owner, y omitirlo es un error de firma, no un permiso |
| el censo de `V6-04` dejaba fuera **45 de los 82 módulos** del runtime —el 55 %—, incluidos `ciclo/` y `macrocircuitos/`, que este mismo macrobloque creó: la lista de paquetes estaba escrita a mano y envejeció exactamente como su propio comentario advertía | **BLOQUEA LA CANDIDATA** | el criterio deja de ser una lista y pasa a ser una **propiedad del disco**: todo paquete Python del runtime entra, y lo que queda fuera se declara uno a uno con su motivo. Al ensancharlo apareció **una lectura de Git real fuera del canal único** en `ciclo/continuacion.py`, que se corrigió usando el canal en vez de declarar una excepción más |
| `Continúa` publicaba un handoff pendiente **FALSO para siempre**: cada transición re-derivaba el `id`, así que el acuse iba a una ruta nueva y el objeto `emitido` nunca quedaba superado | **BLOQUEA LA CANDIDATA** | la identidad de una entrega se **fija al emitir** y las transiciones la conservan, como ya hacían items y paquetes. Prueba nueva: tras el acuse hay **un solo objeto** en el dominio y `Continúa` deja de reportarlo |
| **dos etapas del `§7.2` no estaban implementadas**: la declaración de acoplamiento con `lee_fuentes`/`escribe_fuentes` (`E2.2`) y la condición COMPUESTA de paralelismo de `a.5`. Y el freno de devoluciones de `a.7` se escribía en cada entrega y **nadie lo sumaba** | **BLOQUEA LA CANDIDATA** | el paquete durable lleva su **declaración de acoplamiento**; `ciclo/paralelismo.py` evalúa **las seis condiciones** y publica cuáles fallaron; y el freno de `a.7` se acumula por item. La prueba ejerce la prohibición central: **cinco casos con escrituras disjuntas que AUN ASÍ no se paralelizan** |
| el `C4` **paso 4** —política de `C2`, modelo elegido, descartados con su motivo— no existe, y `execution_slots` corta por ROLES, de modo que puede separar un par que la composición declara combinable | CORRECCIÓN DETERMINADA · declarada y **no** corregida entonces | **CERRADA en el corte de completitud posterior**, y la afirmación de que «corregirlo exige decidir la política de agentes» resultó ser falsa: la política estaba ENTERA en `C2` y se DERIVÓ, sin decisión del Owner. Ver §5 ter |
| la fila de `FD-5` publicaba una cifra —«tres de cuatro / cero de cinco»— que **ningún instrumento emite** | CORRECCIÓN DETERMINADA | la fila describe ahora lo que la batería MIDE, sin citar un número que nadie publica |
| material de clave Ed25519 residual en `/tmp`, de iteraciones de construcción anteriores a este commit | DEUDA EXTERNA | el código vigente limpia —comprobado también con una corrida ROJA provocada—; barrer el anfitrión es materia de operación, no del repositorio |
| sólo cuatro de los once árboles adversariales tienen cabecera publicada | DEUDA POSTERIOR | es una laguna del CORPUS, no de `F6`: §20.5 dice que quien publique la cabecera entra solo, y el derivador crece con ella —comprobado añadiendo una en una copia— |

> **Y la lección de método que este macrobloque añade a las dos anteriores.** Cinco de los
> seis bloqueantes eran **propiedades que se podían borrar del producto sin que ninguna
> prueba parpadeara**. No fallaban: no podían fallar. La corrección no fue sólo arreglar el
> código, sino **darle a cada una una prueba capaz de ponerse roja**, y comprobarlo
> saboteando el producto a propósito. Una prueba que confirma lo que el código hace, en vez
> de lo que el contrato promete, sigue siendo la forma más cara de tener un verde.

## 5 ter · La auditoría del CORTE DE COMPLETITUD, y qué cambió por ella

**Quién.** Un auditor independiente que no construyó nada de este corte, con el encargo de
romperlo y con diez ataques obligatorios. **No escribió un byte en el árbol**: todos sus
ataques se hicieron sobre copias, y al terminar `HEAD` seguía siendo el mismo commit y
`git status --porcelain` mostraba exactamente los mismos ficheros que antes de empezar.

**Su veredicto: NINGÚN BLOQUEANTE VIVO.** Y lo que NO consiguió informa tanto como lo que
sí: partir un par `combinables` con el corte de slots —barrido de 1 a 10, imposible— · una
colisión de slot con dieciséis procesos reales concurrentes —cero— · un rol despachado sin
agente en las quince capacidades —cero— · una discrepancia en los descartes, que recalculó
**con su propia implementación** sobre los veintiún perfiles —cero— · una obligación de `F6`
ausente del universo de la resta —ninguna— · una fila de §19 omitida en `F6-H` —ninguna, su
derivación coincide exactamente— · refutar la justificación de `F-07` sobre append-only —no
pudo: la cabecera **sí** da ROJO en `V6-12`, y lo ejecutó— · un mock que sustituyera
comportamiento —ninguno— · una marca comercial en `kernel/operativo/` o `packs/` —ninguna—
· variación del E2E entre cuatro `cwd` —salida idéntica— · un gate abierto, una resolución
del Owner alterada o un estado de fase movido —nada—. Recalculó además la huella **con su
propia implementación** sobre 386 ficheros y obtuvo el mismo valor, y contó por su cuenta
casos, baterías y escenarios: las cinco cifras coinciden.

**Lo que SÍ encontró, y se corrigió en la única pasada de corrección:**

| defecto | clasificación | qué se hizo |
|---|---|---|
| **el `C4` PASO 1 no se ejecutaba.** `paquete` y `metodo` entraban por la firma como cadenas opacas y salían intactas; ninguna de las cinco materias que el paso nombra —capacidad responsable, modo, objetivo, nivel de calidad exigido, declaración de acoplamiento— se leía en ningún sitio, y el E2E rotulaba «PASO 1» una aserción de ida y vuelta de dos cadenas | CORRECCIÓN DETERMINADA | el paso 1 **resuelve las cinco contra sus sedes** —el método contra `capacidades/<CAP>/metodos/`, el nivel contra los bloques `ads:nivel-novedad`, el acoplamiento contra `runtime.modelo`— y **tiene efecto**: el nivel aporta sus `gates_obligatorios` al equipo escrito y el modo decide si cabe una fase divergente. Siete rutas de FALLO CERRADO nuevas, y `C4` «1 agente por defecto, siempre; varios NUNCA sin integrador» pasa a ejecutarse. `T236`, y el E2E mide lo que el contrato pide |
| **la exigencia del agente COMBINADO se podía bajar al MÍNIMO** eje a eje sin que ninguna prueba parpadeara: un modelo SIN VISIÓN ocupaba un rol que la exige, con los treinta y un validadores en verde. Era el más grave de los tres borrables | CORRECCIÓN DETERMINADA | `T237`: la exigencia combinada es el MÁXIMO en los siete ejes contra los dos perfiles de origen, las herramientas se UNEN, y se mide sobre el catálogo real que ningún agente combinado queda por debajo de ningún perfil que ocupa. Sabotaje que lo pone rojo |
| **el techo de coste combinado (`min`) era borrable**: cambiarlo a `max` no ponía nada rojo, y combinar un rol barato con uno caro hacía desaparecer el techo del barato | CORRECCIÓN DETERMINADA | `T238`, sobre tres parejas de perfiles reales, con su sabotaje |
| **el EJE DOMINANTE divergía de `C2` en dos de los veintiún perfiles, y no lo probaba nada.** `C2` dice «el declarado en `exige` con nivel `maximo`»; la implementación generalizaba a «el tope de su eje», y como la escala de `vision` no tiene `maximo`, `vision` se adelantaba a un eje que sí lo pedía. El valor equivocado se PUBLICABA en el registro auditable, y el docstring afirmaba que las dos formas coincidían | CORRECCIÓN DETERMINADA | se vuelve a la LETRA de `C2`; el caso que `C2` no contempla —un perfil sin ningún `maximo`— se resuelve con su misma regla de desempate y se marca `DERIVADO` en el motivo publicado. `T239` recalcula la regla sobre los veintiuno sin usar la implementación, y exige que `vision` no sea nunca el eje dominante |
| **el registro de `C4` paso 7 se autocontradecía** al romperse una combinación: el mismo par salía publicado con `aplicada: True` y `aplicada: False`, y `comparte_agente_con` nombraba a un compañero con el que NO se compartía agente. `exigir_separacion` —la instrumentación de `G13`— consulta ese campo | CORRECCIÓN DETERMINADA | la ruptura **RETIRA** las entradas que contradice, y `comparte_agente_con` pasa a derivarse del AGENTE realmente asignado y no de la lista. `T249`, con un catálogo HOSTIL real: un modelo por perfil y ninguno que cumpla los dos |
| **la justificación de la desviación de `F-07` se extralimitaba.** Decía «sólo un resultado es conforme con las dos normas a la vez», y el auditor demostró EJECUTANDO que hay al menos tres: la cabecera da ROJO, pero AÑADIR AL FINAL de los dos ficheros append-only sale `INDETERMINADO`, y el tercer fichero admite el campo dentro | CORRECCIÓN DETERMINADA | la fila lo dice ahora con exactitud y explica **por qué la elección sigue siendo de `F6` y no del Owner**: las tres alternativas declararían el mismo valor derivado y ninguna altera comportamiento normativo, luego es MECANISMO (`O24` §2). Se elige la única que no escribe un byte en un documento del Owner |
| **la matriz declaraba `V6-01`…`V6-19` y `g.1`…`g.16` en el universo de la resta y no los enumeraba fila a fila** —`V6-12` y `V6-19` no aparecían en ninguna—. Es la misma forma de «lista parcial» que este corte declara haber erradicado en `F6-H` | CORRECCIÓN DETERMINADA | §6 de la matriz, con las dos familias fila a fila, y **con la verdad incómoda declarada**: se distingue el contrato citado por su identificador dentro de una prueba del que se ejerce por la propiedad dentro de la batería de su módulo, en vez de presentar las dos cosas como si fueran la misma |
| **la evidencia publicada empotraba rutas ABSOLUTAS del anfitrión** y no era reproducible en otro checkout: tres ficheros diferían sólo por dónde estaba el árbol. La causa eran `ResourceWarning: unclosed file` reales, que Python cita por ruta completa | CORRECCIÓN DETERMINADA | se cierran los descriptores **en origen** —la tubería de contención no se cerraba en las rutas de `timeout` y `cancelado`, que son justo las que las pruebas ejercen— y, además, la raíz del checkout se normaliza a `<raiz>` en el único punto por el que pasa toda la evidencia. **Medido: la suite corrida en OTRO checkout, en otra ruta, produce evidencia idéntica byte a byte** |
| la cabecera del escenario decía «veintiún pasos» y el escenario tiene veinticuatro | CORRECCIÓN DETERMINADA | corregida |
| la sección «Cuántos agentes por rol» de `C4` no se ejecutaba: el campo `agentes` es prosa inerte | DEUDA POSTERIOR, y el auditor así la clasificó: este corte contrata el **paso 4**, no esa sección | aun así queda **parcialmente cerrada** por el paso 1: «1 agente por defecto, siempre» y la prohibición de varios agentes sin integrador YA se ejecutan. Lo que sigue sin ejecutarse es la derivación del cardinal desde la prosa del campo, que exigiría reglas léxicas sobre texto libre |
| marcas comerciales en `kernel/KERNEL.md` y `kernel/templates/` | NO ES DEFECTO · fuera del ámbito literal de `C2`, que dice «`kernel/operativo/` ni `packs/`», y excepción declarada en `KERNEL.md` | nada |

> **Y la lección de método, otra vez, porque volvió a pasar.** Tres de los cinco defectos
> corregibles eran **propiedades que se podían borrar del producto sin que ninguna prueba
> parpadeara**, y las tres vivían en el módulo NUEVO. No es que el código fuera incorrecto:
> lo era. Lo que faltaba era lo que impide que deje de serlo. La tabla de sabotaje pasa de
> **seis a ONCE** entradas, y cada una comprueba en un proceso real, sobre una copia del
> árbol a la que se le ha quitado la regla, que la prueba que la cubre se pone ROJA.

## 6 · Lo que este macrobloque NO hace

```text
NO INICIA        PesquerApp, ni un MVP, ni un piloto, ni una adopción parcial
NO CERTIFICA     nada: implementado y probado NO es certificado
NO CIERRA        F6: la cierra un acto posterior, después de la certificación independiente
NO ABRE          el gate de certificación, que es del macrobloque siguiente
NO REABRE        F4c ni F5
NO EDITA         la tabla de `(g)` §17: es norma aprobada y describe su momento
```

## 7 · Lo que queda, exacto

```text
1  LA CERTIFICACIÓN INDEPENDIENTE de F6, que es `F6-J` y no es de quien construyó
2  el NIVEL `soportado` de un adaptador, que exige una celda `certificacion/integrado` con
   `SOURCES.toml`, CI y permisos certificados. Hoy el nivel derivado es `compatible`
3  `cgroup v2` como backend de contención EJERCIDO, que este anfitrión no permite: el
   subgrupo se crea y la tarea no entra. Requisito exacto: un anfitrión donde
   `echo $$ > <grupo>/cgroup.procs` no devuelva EIO
4  una IDENTIDAD DE SISTEMA dedicada para la raíz externa. Requisito exacto: `sudo` sin
   contraseña o una cuenta de servicio creada por quien administre la máquina. Sin ella,
   la independencia se demuestra con contenedor y espacio de nombres, que es lo que hay
5  la CUSTODIA PRODUCTIVA de la clave, que `O25` §2 deja al proveedor del anfitrión
6  el recorrido extremo a extremo de TODAS las fases de `A` y de `U`, que es el NODO 8
   del `11-ARQ` §18 —la PRIMERA ADOPCIÓN REAL— y que §18 declara BLOQUEADO por el nodo 9
   hasta que `F6` esté implementado Y CERTIFICADO. NO es obligación interna de `F6`

La lista de `F6-H` **ya no está aquí**: se cerró entera, y su inventario uno a uno vive en
la matriz de completitud. Ninguno de los seis puntos de arriba es obligación interna de `F6`
sin construir: los seis son juicio independiente, límite de anfitrión o materia que una norma
vigente pone DESPUÉS de `F6-J`, y cada uno lleva su cita en esa matriz.

NINGUNA decisión del Owner queda pendiente: `O25` cerró la última, y este macrobloque no
ha abierto ninguna.
```

## 8 · La matriz de completitud, y la resta

**Sede:** [`01-MATRIZ-DE-COMPLETITUD-F6.md`](01-MATRIZ-DE-COMPLETITUD-F6.md). Deriva de las
fuentes canónicas TODAS las obligaciones que forman `F6` —los entregables `F6-A`…`F6-J`, los
diecinueve `V6-*`, los apartados de `(g)` y sus tres contratos derivados, `C2`, `C4` y `C5`
donde el ciclo los invoca, las siete filas `CONTRATO_COMPLETO_PARA_F6` de la matriz de los 22,
las filas de `11-ARQ` §19 con fase `F6`, y `A14`, `FD-3`, `S1-02`, `FD-5`, `FD-1` y `FD-6`—,
y publica de cada una su **estado inicial medido**, su **evidencia ejecutable**, si lo
pendiente es INTERNO, EXTERNO o LÍMITE DE ANFITRIÓN, y su **estado final medido**.

```text
obligaciones internas de F6 − implementadas y probadas   =   ∅
```

**Qué NO barre esa resta, y por qué no es un vaciado.** `F6-J` no es construcción: es el ACTO
de un juicio independiente. `F-08`, `FD-2` y `FD-4` no son de `F6` y su fuente lo dice
literalmente. El recorrido extremo a extremo de `A` y `U` y el nivel `soportado` de un
adaptador son el nodo 8 del §18, que §18 pone DESPUÉS de la certificación. La custodia
productiva es EXTERNA por `O25` §2. Los siete árboles sin cabecera están fuera del conjunto
que `V6-15` mide, y §20.5 prohíbe inventarles identificador. Y `cgroup v2` ejercido y una
identidad de sistema dedicada son límites de ESTA máquina, medidos y publicados como tales.

> **Y la regla que impide leer la resta al revés.** Que salga vacía significa que **no queda
> obligación interna de `F6` sin construir y sin ejecutar**. No significa que `F6` esté
> certificada, ni que PesquerApp se desbloquee: eso es `F6-J`, y `F6-J` no lo emite quien
> construyó.
