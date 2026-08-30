# Decisiones, contradicciones y límites del kernel operativo


Registro vivo de la iteración que construye el contenido operativo (pasos 1 a 6) sobre
las secciones aprobadas (a) y (b). Tres partes: **decisiones tomadas** (reversibles, y por
qué se tomaron sin consultar), **decisiones que pertenecen al Owner** (agrupadas, no
interrumpen el trabajo) y **contradicciones detectadas** contra el material normativo.

---

## 1 · Decisiones tomadas sin consultar

Criterio para no consultar: reversible, dentro del alcance ya autorizado, y sin cambiar
autoridad ni semántica de (a) o (b) — la regla de b.15.1 aplicada a este trabajo.

| # | decisión | motivo | cómo se revierte |
|---|---|---|---|
| D1 | El contenido operativo vive en `kernel/operativo/`, no dentro de `KERNEL.md` | `KERNEL.md` es prosa constitucional de 1.3.0; mezclar ambos crearía dos fuentes de la misma verdad | mover el árbol; nada depende de su ruta salvo el índice |
| D2 | Formato canónico = bloques ` ```yaml ads:<tipo> ` dentro de Markdown | cumple las dos exigencias a la vez: legible por el Owner, no ambiguo para la máquina | cambiar el extractor de `ads_lint`; los datos no cambian |
| D3 | Los tres packs de 1.3.0 pasan a `packs/legacy-1.3.0/` | evita dos packs de web app compitiendo por la misma verdad | `git mv` inverso |
| D4 | `pack-design-led` **se promueve al kernel** en vez de reescribirse como pack | la excelencia visual dejó de ser propiedad de una clase de proyecto: es requisito central del kernel (enunciado del paso 3) | volver a extraerlo a un pack |
| D5 | Los packs nuevos son **directorios**, no ficheros sueltos | un pack aporta roles, métodos, gates y pruebas: no cabe en un fichero sin volverse ilegible | — |
| D6 | La numeración de pruebas nuevas empieza en **T75** | continúa T01–T74 sin renumerar nada aprobado | — |
| D7 | El rol que atiende al Owner se llama **`ENC` · Encuadre** como capacidad y `ENC/interlocutor` como rol | (a) sitúa Encuadre como función de DSP; separarlo como capacidad propia se explica en la contradicción C1 | ver C1 |
| D8 | `kernel/VERSION` pasa a `2.0.0-alpha.1` | hay contenido de kernel 2.0 real en el repositorio; dejarlo en 1.3.0 haría que `kernel-status.sh` mintiera | — |
| D9 | La composición del producto vive en `SOURCES.toml`, y **ningún otro documento la repite** | el mandato la declara fuente única; copiarla en `PROJECT.md` obligaría a editar dos sitios cada vez que cambie una URL | borrar el manifiesto y declarar las fuentes en prosa; se perdería la validación mecánica |
| D10 | Los dos contratos nuevos son **`C6` y `C7`**, transversales, en vez de una capacidad nueva de Git | el 8.2 del mandato avisa de que repartir Git entre `PLT`, `ENT`, `DSP` y `CON` es el problema; una capacidad más lo repartiría otra vez. Un contrato transversal declara la propiedad **operación a operación** sin crear un equipo | fundir ambos en uno, o mover su contenido a las fichas de capacidad |
| D11 | `source` y `component` **no** son tipos canónicos con bloque `ads:` | duplicarían `SOURCES.toml`, que el mandato declara fuente única. Sí lo es `integration-set`, porque es evidencia nueva y no vive en el manifiesto | añadir los esquemas si aparece una necesidad que el manifiesto no cubra |
| D12 | El alcance de fuentes de un paquete se declara como **dos campos más de la declaración de acoplamiento** de `a.5`, no como artefacto nuevo | `a.5` ya declara que los nombres definitivos se fijan más adelante, y el mandato pide adaptar el formato existente en vez de introducir uno | renombrarlos al cerrar la sección (g) |
| D13 | Las pruebas de `workspace.py` viven en `tooling/tests/` y el manifiesto de validadores gana un campo `dir` | prueban tooling, no el corpus; meterlas en `validadores/` las habría mezclado con las pruebas de conformidad. Sin el campo `dir` habrían quedado fuera de la evidencia | mover el fichero y quitar el campo |
| D14 | La huella de integridad cubre ahora `.toml` | `SOURCES.toml` es contenido vendorizado del kernel: sin cubrirlo, editar la plantilla sería un fork invisible, que es el hallazgo A-04 otra vez | quitar la extensión de `huella.py` |
| D15 | `kernel/KERNEL.md` sube a **1.4.0** en vez de quedar congelada | `K-1` y `G29` cambian de alcance, y un lector que sólo abra la constitución leería el modelo retirado. La política de versiones ya preveía que la línea histórica suba «cuando cambia ella» | revertir el texto y dejar la revisión sólo en `E2` |

### `D16`–`D22` · decisiones de la arquitectura integrada

Tomadas al diseñar cómo encajan todos los subsistemas. **Ninguna está construida**, y ninguna
enmienda material aprobado: lo que sí presiona queda enumerado, sin redactarse, en la sección
de presiones normativas de la iniciativa ADS NEXT — que vive en `docs/evolucion/` y **no se
enlaza desde aquí**, porque este fichero viaja a un proyecto instalado y aquel directorio no.

| # | decisión | por qué, y qué alternativa se descartó | qué cambia si el Owner decide otra cosa |
|---|---|---|---|
| D16 | El estado canónico son **ficheros de texto** en el repositorio de control, acompañados de un **diario de eventos** append-only y de un **manifiesto de transacción** para las transiciones multiarchivo | `a.9` exige que el estado operativo SEA los ficheros, legibles sin informe intermedio, y a la vez que toda transición multiarchivo sea recuperable e idempotente. Sólo ficheros no cumple lo segundo —`a.9` lo dice: Git no convierte N escrituras en una transacción—. **SQLite canónico** y **event sourcing puro** cumplen lo segundo y rompen lo primero: uno es ilegible sin herramienta, el otro obliga a reproyectar para leer | volver a sólo ficheros deja la atomicidad sin resolver; ir a base de datos exige enmendar el requisito del Owner en `a.9` |
| D17 | El diario de eventos **es** el `JOURNAL` que `a.11` dejó pendiente | dos registros de lo que pasó son la duplicidad que `I5` prohíbe. `a.11` ya anticipaba que el runtime «probablemente necesite un event log que PUEDA sustituirlo» | mantener `G26` como pieza aparte obligaría a decir qué guarda cada uno y a sincronizarlos |
| D18 | Se añaden **cuatro tipos canónicos y ni uno más**: `iniciativa`, `adaptador`, `cobertura`, `evento` | cada uno pasa la prueba de necesidad: ningún tipo existente los aloja sin mentir sobre su sujeto. Todo lo demás —findings, causas raíz, campañas, excepciones, certificación, matriz— se compone, se deriva o reutiliza | añadir tipos es barato de escribir y caro de mantener; quitarlos exige demostrar dónde vive su sujeto |
| D19 | El **sujeto auditable** es una referencia tipada `(clase, ancla, ruta)` declarada en la celda de cobertura, no un tipo propio | un tipo obligaría a un registro paralelo de pantallas, flujos y formularios que nadie mantendría al día. Declararlo en `SOURCES.toml` deformaría un manifiesto que es fuente única de otra cosa, que es lo que `D11` ya rechazó | un tipo propio permitiría inventario exhaustivo, a cambio de un registro que envejece |
| D20 | El **contrato documental** se compone de `ads:memoria` —gobierno— más `cobertura` —vigencia—, sin tipo nuevo | siete de sus campos ya existen en `memoria` con ese significado. Una metadata especializada los duplicaría; generalizar `memoria` convertiría un tipo con sujeto claro en un cajón con dos | cualquiera de las otras dos vías obliga a decidir qué pasa con los campos que ya existen |
| D21 | La **certificación** es `cobertura` con `clase: instalacion`, una celda por nivel | mismo sujeto, mismo ciclo, misma caducidad y los mismos triggers de invalidación que cualquier otra celda | un tipo propio permitiría campos específicos, a cambio de otro registro con su propio ciclo |
| D22 | El estado de una `iniciativa` es **derivado** de sus items, y una iniciativa **no anida** en otra | un estado editable sobre lo mismo que ya calcula `b.4` es una segunda verdad. La anidación convierte la vista del Owner en un cálculo sobre un árbol de profundidad arbitraria | permitir anidación exige decidir cómo se propaga el estado y cómo se lee sin perderse |

### `D23`–`D33` · decisiones de la devolución independiente sobre la arquitectura integrada

Una revisión independiente que **no escribió** la arquitectura integrada devolvió nueve
bloques de hallazgos. `D23`–`D33` son las decisiones que los resuelven, y **corrigen o
sustituyen** a las de arriba.

> **`D16`–`D22` no se reescriben, y no es un descuido.** Están tomadas, y su texto es la
> prueba de qué se decidió y con qué argumento. Corregir una decisión reescribiéndola borra
> que se tomó — y ésa es exactamente la vía que `O7`–`O14` evitaron al entrar sin tocar
> `O1`–`O6`. Cada fila de abajo declara **qué decisión anterior queda revisada**.
>
> **Ninguna está construida**, y ninguna enmienda material aprobado. Lo que sí presiona
> queda enumerado, sin redactarse, en la sección de presiones normativas de la iniciativa
> ADS NEXT — que vive en `docs/evolucion/` y **no se enlaza desde aquí**, por el mismo motivo
> que `D16`–`D22`: este fichero viaja a un proyecto instalado y aquel directorio no.

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D23 | El **manifiesto de transacción deja de ser un artefacto propio**. Una transacción es una **secuencia de eventos inmutables** que comparten un identificador `tx` y se distinguen por su campo `fase`: `preparada`, `confirmada`, `derivada`, `abortada`, `conflicto` | **D16** | `D16` contaba el manifiesto como pieza aparte sin aplicarle la prueba de tipo nuevo. Aplicada: su sujeto y su autoridad son los del evento, y su «ciclo propio» era que **cambiaba de fase** — es decir, que había que reescribirlo. Reescribir el registro que debe sobrevivir a una caída era el defecto, no la propiedad. Además el manifiesto se borraba al cerrar, dejando el campo `evento.tx` apuntando a un artefacto inexistente. La alternativa —conservar el manifiesto y no borrarlo— resolvía el segundo defecto y no el primero | volver a un artefacto con fases obliga a decidir cómo se reescribe de forma recuperable, que es lo que no se sabía resolver |
| D24 | Los identificadores de evento son **direccionados por contenido y NO monotónicos**. El orden se recupera de dos campos: `orden` dentro de la transacción, y `predecesor` como cadena verificable | **D16** y su esquema de identidad | la forma anterior era `EV-<nnnnnn>` monotónico, con la afirmación de que «dos emisores concurrentes no colisionan jamás porque cada evento es un fichero nuevo». **Es falsa**: un id monotónico se calcula leyendo el mayor y sumando uno, y dos emisores que lo hacen a la vez eligen el mismo número; que el fichero sea nuevo no genera su nombre. De las dos vías admisibles —serializar la generación bajo el ejecutor único, o usar ids resistentes a colisión— se elige la segunda: no depende de un lock que sólo existe en una máquina, y emitir dos veces el mismo evento produce el mismo fichero. **Lo que se pierde se declara**: el orden total entre máquinas no se afirma | serializar bajo el ejecutor único devuelve ids legibles y monotónicos, a cambio de no funcionar con dos máquinas sobre el mismo control repo |
| D25 | `cobertura` separa **`sujeto`** (qué se audita), **`aspecto`** (qué propiedad se juzga, con namespace tipado), **`responsables`** (qué capacidades responden, una `lider`) y **`criterio`** (contra qué se juzga) | **D18**, en la forma de `cobertura` | el campo único `dimension` se definía como «la capacidad que la posee», y con eso auditar la accesibilidad de una pantalla y auditar su responsive eran **la misma celda**: `DIS` posee las dos. No podían tener estados, caducidades ni verificadores distintos. Y las doce áreas documentales y los cuatro niveles de certificación —que no son capacidades— entraban en ese mismo campo sin namespace. Tres universos en un campo sin tipo es una colisión semántica, no una economía | volver al campo único exige decidir cómo se registran por separado dos aspectos de la misma capacidad |
| D26 | La **certificación sigue siendo `cobertura`** para el ESTADO, **y exige además** un esquema de **clase** `nivel-certificacion` que aloja pruebas, propietario, crítico, **jerarquía** e invalidación | **D21**, confirmada en su conclusión y corregida en su fundamento | `D21` acierta en que el sujeto, el ciclo y la caducidad son los de cualquier celda. Lo que no vio es que un nivel es además una **norma**: qué pruebas exige, quién puede ser su crítico y **qué nivel presupone**. Meterlo en la celda obligaría a repetirlo en cada instalación y permitiría que dos discrepasen sobre qué exige «Integrado». Meterlo en `gate` daría a todos los gates dos campos que sólo usa la certificación. El precedente del esquema de clase ya existe en el corpus: `nivel-novedad.yaml` | un tipo propio de certificación permitiría campos específicos, a cambio de otro registro con su propio ciclo — que es lo que `D21` rechazó y sigue rechazándose |
| D27 | **`memoria` se GENERALIZA**, y se declara: su sujeto pasa de «una sección del corpus persistente de un equipo» a «cualquier documento gobernado». `capa` pasa a **condicional** —sólo la declara conocimiento que viaja con un release— y se añade `plano`, obligatorio, con los cinco planos de ciclo de vida | **SUSTITUYE a D20** | `D20` afirmaba composición **sin** generalizar `memoria`, y a la vez el diseño ampliaba su descripción «de sección del corpus de un equipo a documento gobernante en general». Se hacían las dos cosas y sólo se contaba una. La composición es real y se conserva —`memoria` gobierna, `cobertura` da vigencia—; la generalización también, y ahora se dice. `capa` no puede admitir un cuarto valor sin fabricar la cuarta capa de conocimiento que `X1` mantiene deferida: por eso se hace condicional y el ciclo de vida se declara aparte | volver a `D20` obliga a decir dónde vive el gobierno de un documento cuyo sujeto no es la memoria de un equipo |
| D28 | **`adaptador.nivel` desaparece** como campo. Se separan `compatibilidad_declarada` (editable), `capacidades_del_entorno` (editable) y **nivel alcanzado, DERIVADO** de las celdas de certificación del adaptador | **D18**, en la forma de `adaptador` | `soportado` era a la vez un campo que alguien escribe y una conclusión que exige prueba de humo ejecutada más certificación Integrada. Editable y derivado a la vez es la segunda verdad que `I5` prohíbe, y además **un campo editable no caduca** mientras una certificación sí: un adaptador podía seguir diciendo `soportado` después de que un cambio de arranque invalidara su nivel Operativo | conservar el campo obliga a un mecanismo que lo sincronice con las celdas, que es la sincronización que `I5` existe para no necesitar |
| D29 | El estado de una `iniciativa` es una **función total con precedencia mecánica** `Q0`–`Q9`, y **no se persiste** en ningún fichero canónico: vive sólo en el dosier derivado | **D22**, confirmada y completada | `D22` acierta en que es derivado y en que no anida. Lo que faltaba: los cinco estados anteriores **se solapaban** —«tiene items vivos» y «todos sus items vivos están bloqueados» son ciertas a la vez— y dejaban sin cubrir la iniciativa sin items, las mezclas, las cancelaciones, los desacuerdos y las obligaciones huérfanas. Y `D22` no decía **dónde** aparece el estado derivado; escribirlo en `00-iniciativa.md`, que es canónico y editable, habría creado la segunda verdad que la propia decisión evita | persistirlo exige una zona regenerable y no editable dentro del canónico, con la disciplina de dos zonas de `a.9` |
| D30 | El **soporte durable mínimo de `estado/` nace en N0** de la instalación —la iniciativa, el diario y el checkpoint—, no en N3 | el recorrido de instalación | la iniciativa de instalación nacía en N0 y su soporte durable en N3, luego entre ambas fases **no estaba persistida**: vivía en la conversación, y la reanudación se declaraba «repitiendo el paso». Son tres ficheros, y su coste es menor que el de un recorrido de siete fases que no se puede reanudar en sus tres primeras | crear `estado/` más tarde obliga a aceptar que la instalación depende del chat hasta N3 |
| D31 | La **clave de caché de la vigencia de evidencia es el CONTENIDO**, con tres huellas separadas —semántica, de entorno y artefacto de salida—. **Nunca el SHA de Git** | el mecanismo de vigencia general | la clave por revisión de Git es **ciega al árbol sucio**: mismo `HEAD`, contenido distinto, veredicto servido de caché. Y en el trabajo normal —editar y comprobar— el árbol sucio es el caso permanente. La huella anterior cubría sólo el corpus: cambiar un helper importado cambiaba trece veredictos y ninguna huella. El SHA se conserva como dato informativo, y no participa en la clave | volver a la clave por revisión reintroduce el defecto que el propio mecanismo existe para cerrar |
| D32 | La **aplicabilidad de la certificación Integrada depende del número de fuentes** declaradas: la prueba multi-fuente no aplica a productos de 0 ni de 1 fuente, y una prueba no aplicable se registra con motivo **y evidencia** y no bloquea | el contrato de certificación | `C6` `N4` admite **0..N** fuentes, y la Integrada exigía sin condición «trabajo multi-fuente verificado como conjunto». Juntas, bloqueaban **para siempre** a todo producto de un solo repositorio y a toda instalación recién hecha. Reinterpreta la precondición de `O12`, que es resolución del Owner, y por eso genera una presión normativa en vez de darse por aprobada | exigir la prueba sin condición deja fuera del sistema a la mayoría de los productos |
| D33 | La secuencia de migración es **M5 certifica · M6 retira · M7 verifica** | el recorrido de migración | la lista de fases ponía la retirada antes de la certificación y el rollback afirmaba lo contrario: dos secuencias incompatibles en el mismo documento, y una de ellas retiraba material antes de certificar su sustituto. Certificar y verificar responden preguntas distintas —«¿funciona lo nuevo?» y «¿dependía algo de lo viejo?»— y la segunda **sólo se puede responder después de retirar**, de modo que fundirlas era lo que producía la contradicción | fundir M5 y M7 devuelve la ambigüedad; invertir M5 y M6 retira antes de saber si el sustituto funciona |


### `D34`–`D45` · decisiones de la SEGUNDA devolución independiente

Un revisor independiente con contexto limpio —que **no escribió la arquitectura integrada y
no aplicó la primera crítica**— emitió un veredicto de **INSUFICIENCIA**: dos hallazgos
BLOQUEANTES, siete GRAVES y catorce nuevos. `D34`–`D45` son las decisiones que los resuelven.

> **`D16`–`D33` no se reescriben**, por el mismo motivo que `D16`–`D22` no se reescribieron
> al aplicar la primera crítica. Cada fila declara qué queda revisado.
>
> **Ninguna está construida.** Y dos de ellas —`D40` y `D45`— corrigen defectos que la
> PRIMERA corrección introdujo o no vio, lo que es la razón por la que las revisiones
> independientes se encadenan en vez de darse por buenas.

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D34 | La secuencia de escritura de un canónico es **`escribir temporal → fsync(temporal) → rename → fsync(DIRECTORIO)`**, y el `fsync` de directorio es **obligatorio también para los canónicos** | **D16** y `D23` | F4c exigía `fsync` de directorio en el evento `preparada` y en el `confirmada`, y **no** en los ficheros canónicos — y ordenaba el `fsync` del fichero DESPUÉS del `rename`. Es el error que su propia garantía 3 nombraba como «el error clásico», cometido en los ficheros que **son** el estado. La alternativa —confiar en que el sistema de ficheros ordene— no es una alternativa: es el defecto | ninguna: quitar el `fsync` de directorio reintroduce la pérdida silenciosa |
| D35 | **`fase: conflicto` NO es terminal**: es **abierta y absorbente**, emite la bandera `reconciliacion_pendiente` que `b.4` P0 consume, conserva copia íntegra de lo divergente, declara autoridad y alcance de bloqueo, y sólo la cierra `fase: reconciliada` | **D23** | siendo terminal, la transacción **tenía** evento terminal: el marcador se retiraba por `W8`, `Continúa` declaraba el arranque limpio, y los derivados se regeneraban sobre estado incoherente. **`reconciliacion-pendiente` no aparecía ni una vez en todo §2**, luego `b.4` P0 —cuya única razón de existir es este caso— nunca se disparaba. La primera crítica exigió que la tercera caja no se resolviera sola, y se consiguió a costa de que el sistema dejara de saber que había algo que resolver | volver a terminal exige decir quién marca el estado incoherente, que es lo que faltaba |
| D36 | Existe una **comprobación de integridad post-terminal**: al arrancar, toda transacción con evento terminal dentro de la última ventana de commit verifica sus `hash_posterior_esperado` | **D23** | sin ella, `D34` depende de que la implementación no tenga defectos. Con ella, el fallo silencioso se detecta. Es barata: son las transacciones desde el último commit, no el diario entero | quitarla devuelve el sistema a confiar en la implementación |
| D37 | **Contrato de identidad** completo en §2.8: representación canónica independiente del formato, campos incluidos y excluidos con `identidad_v`, `tx` definido sobre el cuerpo de `preparada` menos `id`/`tx`/`predecesor`, `id` definido sobre el evento menos `id`, y regla de reintento por `tx` | **D24** | `D24` eligió ids direccionados por contenido y **no dijo qué contenido**. `id` era campo del evento y a la vez su huella —circular—; `tx` no tenía definiendum; no había serialización canónica, luego dos implementaciones producirían identificadores distintos. Y la idempotencia prometida era **falsa**: `predecesor` cambia tras una caída, luego reemitir produce otro `id`. Se declara: la idempotencia vive en `tx`, no en `id` | volver a ids monotónicos reintroduce la colisión que `D24` cerró |
| D38 | **`fase: abortada` se RETIRA.** Cuatro registros de transacción, no cinco | **D23** | su ventana de alcanzabilidad era `[preparada durable, primer fichero tocado)`, que es exactamente el dominio de `W3` — y `W3` manda completar. Antes del punto de compromiso no hay registro que pueda llevar esa fase. Era **formalmente definida y operacionalmente inalcanzable**, y un estado muerto en un enum normativo se paga en el esquema, en la implementación y en las pruebas. Se buscó una causa de aborto que sobreviviera y no la hay | darle un disparador exige mover el punto de compromiso, y `R3` obliga a que la decisión sea determinista, luego en la práctica se vuelve a «completar siempre» |
| D39 | **Regla de lectura** para TODO lector: antes de leer el estado canónico se comprueba `estado/tx/`; con marcador, las rutas que declara son NO FIABLES. El marcador lleva contenido, y cada canónico afectado lleva `tx_abierta` en su cabecera. Lo que se garantiza es **detectabilidad, no aislamiento** | **D16** y `D23` | F4c decía «desde `confirmada` puede creerse lo que lee» y eso era una descripción del diario, no una regla dirigida a nadie. Sin ella, todo lector que no fuera el runtime leía una mezcla sin saberlo — y `R1` existe precisamente para que haya lectores que no son el runtime. Además el marcador «sin contenido» obligaba a **reproyectar el diario** para saber qué ficheros estaban en vuelo, que es el coste con el que §2.2 descarta el event sourcing puro | ofrecer aislamiento real exige versiones múltiples de cada canónico, y con ellas un almacén que `R1` no admite |
| D40 | El marcador `estado/tx/*.abierta` **se excluye de Git**: vive en el árbol durable y **no viaja** | **D23** | la garantía 6 enunciaba como propiedad normal que los marcadores llegan a un clon «porque están versionados», y la regla de commit declara ese estado **imposible salvo por defecto del runtime**. Y aplicando el criterio de §2.4 al marcador —¿sobrevive a un clon nuevo?— la respuesta es no: es un acelerador. F4c violaba su propio criterio de clasificación. Se conserva en `estado/tx/` y no en `.ads/run/` porque `D39` exige que sea legible sin herramienta junto al estado que califica | moverlo a `.ads/run/` es coherente con §2.4 y pierde la legibilidad que `D39` necesita |
| D41 | El **push NO es automático en recuperación**: el commit local sí —es recuperación—, el push pasa a decisión. Y se declara que **el gobierno Git del control repo no existe** en `C7` ni en ninguna parte | **D16** | `W9`/`W10` decían «se hace el commit» y «se hace el push» en voz impersonal, sin ninguno de los cinco conceptos de `a.9`, sin política de rama pese a `G29`, y sin ramal de fallo. El push **publica** en infraestructura del Owner, y §8.1 ya declara que ADS no reescribe historia publicada: la asimetría entre ser escrupuloso en el rollback y automático en la recuperación no estaba argumentada. Y la tabla de propiedad de `C7` gobierna las FUENTES: ninguna fila alcanza el control repo, luego §7.6 era falsa para las dos operaciones que se automatizaban | automatizar el push devuelve la publicación implícita |
| D42 | `cobertura` gana **`evaluacion_de_pruebas`** —aplicabilidad, motivo, evidencia y resultado **por prueba**— y `verificador` se parte en **`auditor`** y **`verificador_de_correccion`** | **D25** y `D32` | la `aplicabilidad` de la celda es del par `(sujeto, aspecto)`, y `D32` y `PN-6` exigen evaluarla prueba a prueba. F4c la metía «dentro del criterio», que es una norma de CLASE compartida — y la evidencia de inaplicabilidad es un dato de ESTE producto y ESTA revisión. Y `verificador` significaba el auditor en un apartado y el verificador de la corrección en otro: el mismo campo con dos sentidos, que es lo que la partición de `dimension` existía para impedir | fundirlos devuelve la polisemia; quitar `evaluacion_de_pruebas` deja el veredicto de Integrado sin sede |
| D43 | Nace **`contrato-de-aspecto`**, esquema de CLASE, con el reparto de responsables **por defecto**, criterio, pruebas, caducidad y triggers de una familia. La celda declara sólo la **desviación**. El recuento pasa de 24 a **25** | **D25** y `D26` | «el contrato del aspecto» se invocaba TRES veces como sede normativa y **no existía**: sin esquema, sin dueño, sin la prueba de §3.1 y fuera del recuento — en un apartado que presume de calcularlo. Es el mismo modo de fallo que la primera crítica encontró con el manifiesto de transacción, reproducido y no detectado. Y `responsables` estaba declarado en la celda **y** en él: dos sedes editables para la misma verdad, que es el defecto corregido en `ultima_verificacion_real` y reintroducido aquí | meterlo en `gate` da a todos los gates campos que sólo usa la cobertura; meterlo en la celda obliga a repetirlo en cada producto |
| D44 | El **documento gobernado tiene ciclo propio de CUATRO valores**: `vigente · sustituida · derogada · refutada`. **No es el de `b.3`** | **SUSTITUYE la parte de `D27`** que fijaba `memoria.estado` | `D27` escribía `vigente | sustituida | retirada` y lo atribuía a `b.3` **dos veces**. `b.3` dice `vigente | sustituida | INVALIDADA`, y `retirada` en `b.3` es un predicado sobre OBLIGACIONES — precisamente la confusión contra la que `b.3` advierte con estas palabras: «si se llaman igual, el sistema puede informar de que entregó algo que en realidad se eliminó». Un documento derogado sin reemplazo **no podía escribirse con ningún valor válido** y se quedaba `vigente`. Y `refutada` es distinta de `derogada` porque obliga a revisar lo que se apoyó en el documento | reutilizar los tres de `b.3` fuerza una elección entre significados incompatibles |
| D45 | Los **predicados de obligación de una `iniciativa` se definen a su nivel**: satisfecha ≡ existe una capa vigente **de alguno de sus items** enlazada explícitamente; retirada ≡ decisión registrada con autoridad y efecto. **Consume `b.3`, no la reutiliza** | **D29** | `D29` declaró la función `Q0`–`Q9` total, y su rama `Q9` invocaba los predicados de `b.3`, que se apoyan en CAPA VIGENTE y RECOMPOSICIÓN APROBADA — objetos que una iniciativa no tiene: no tiene paquetes, ni capas, ni ruta. **Toda obligación de iniciativa era huérfana desde que se escribía y `Q9` devolvía `bloqueada` para siempre**: una iniciativa con obligaciones nunca podía cerrar, y la función «total» no era computable en su última rama | definirlos en `b.3` a nivel de iniciativa sería enmendar (b); la vía elegida es la que `PN-4` validó al retirarse |


### `D46`–`D51` · decisiones de la devolución técnica previa a la tercera revisión

Una **auditoría externa de Codex sobre el árbol remoto real** —el commit `7ebdd8a`— devolvió
once hallazgos: tres BLOQUEANTES, dos GRAVES, cuatro MEDIOS y dos MENORES. No es un veredicto
independiente de suficiencia: es una **revisión técnica previa**, y **no certifica `F4c`**.

> **`D16`–`D45` no se reescriben.** Cada fila declara qué queda revisado. Y tres de estos
> hallazgos son defectos que las DOS correcciones anteriores introdujeron: la disciplina de
> encadenar revisiones se sostiene precisamente porque cada tanda encuentra lo que la
> anterior no vio.

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D46 | El autómata transaccional tiene **CINCO fases y DOS rutas**, con `derivada` como **único cierre terminal**: normal `preparada→confirmada→derivada`, y de conflicto `preparada→conflicto→reconciliada→derivada` | **D38**, y con ella `D23` y `D35` | `D38` decía «cuatro registros, no cinco» al retirar `abortada`, y no contó que `D35` había **añadido** `reconciliada`. El resultado eran cinco formulaciones incompatibles del mismo autómata: el título de §2.6.1 decía cuatro, §2.6.2 decía cinco, §3.6 conservaba `abortada` y omitía `reconciliada`, y la integridad post-terminal trataba `confirmada` como terminal mientras el marcador seguía abierto. **La alternativa —hacer terminal a `confirmada`— dejaba los derivados sin regenerar**, que es el defecto `4` | volver a cuatro fases exige decidir dónde se regeneran los derivados tras un conflicto |
| D47 | El diseño de vigencia de `P-08` tiene **DOS huellas** —semántica y de entorno— y un **artefacto de salida que las contiene**. El artefacto **no es una tercera huella** | **D31** | `D31` decía «tres huellas separadas», y §11.2 define dos más un artefacto que las lleva en campos separados. Lo detectó primero el segundo revisor (`N-13`) y sobrevivió a su corrección en los resúmenes vigentes. La distinción que importa —poder decir «el veredicto vale, pero se obtuvo con otro intérprete»— la dan las DOS huellas, y no se pierde nada al contar bien | ninguna: contar tres donde hay dos no aporta ninguna capacidad |
| D48 | La detectabilidad de una transacción abierta **NO escribe nada en el contenido canónico**. Se sostiene sobre la regla de lectura, el marcador con `tx` y rutas, y el diario | **D39** | `D39` exigía `tx_abierta` en la cabecera de cada canónico. Rompía seis cosas: el contenido con la cabecera **no casa con el `hash_posterior_esperado`** que `preparada` declara; retirarlo exige una segunda escritura de todos los ficheros; esa retirada es otra transición multiarchivo; el paso APLICAR describe una sola escritura; CONFIRMAR no retira cabeceras; y «lo escribe al preparar» contradice que PREPARAR no toque ningún canónico. **La alternativa —definir dos hashes y dos escrituras con su recuperación completa— duplica el protocolo para comprar una legibilidad que el marcador ya da** | conservar `tx_abierta` obliga a declarar dos hashes por fichero y la recuperación de la segunda escritura |
| D49 | `reconciliacion_pendiente` es un **PREDICADO DERIVADO** —«existe `conflicto` sin `reconciliada` ni `derivada` que nombre ese item»—, no una bandera que se escriba | **D35** | `D35` decía que la transacción marca la bandera «dentro de una transacción propia», y la transacción original sigue abierta: su marcador bloquea, y `X08` declara que un segundo ejecutor **no arranca**. **El protocolo necesitaba abrir una transacción para registrar el estado que impide abrir transacciones.** El evento `conflicto` ya nombra los items afectados, luego el predicado es derivable sin mutar nada | persistir la bandera exige declarar una excepción transaccional completa que no colisione con el bloqueo |
| D50 | El **marcador de transacción es OPERACIONAL**, y vive bajo `estado/tx/` por una **excepción de ruta declarada**, no por su naturaleza | **D40** | `D40` lo dejaba «no versionado, reconstruible, en el árbol durable y sin viajar»: una **tercera categoría informal** que §2.4 no tiene, y que además hacía falsa su propia frase «todo `estado/` es durable y versionado». Se clasifica como operacional —responde «no» a la pregunta de §2.4— y se declara por qué está donde está: la regla de lectura obliga a mirarlo antes de leer el estado, y un aviso que vive donde nadie mira no es un aviso | moverlo a `.ads/run/tx/` es coherente con la naturaleza y pierde la descubribilidad que `D39` necesita |
| D51 | **Reparto de dominio entre los dos esquemas de clase**: `contrato-de-aspecto` cubre `calidad` y `documental`; la certificación usa **exclusivamente** `nivel-certificacion` | **D43** y `D26` | `D43` dio a `contrato-de-aspecto` la familia `certificacion`, y `nivel-certificacion` ya declaraba para ella pruebas, propietario, crítico, jerarquía, invalidación y criterio: **dos normas editables para el mismo aspecto**, que es el defecto que `D43` existía para cerrar en otro sitio. **La alternativa —que `nivel-certificacion` especialice o componga el contrato de aspecto— exige decidir campo a campo cuál gana**, y el reparto de dominio no deja ningún campo que pueda discrepar | componer los dos esquemas devuelve la pregunta de qué campo manda |


### `D52`–`D54` · decisiones de la corrección técnica posterior sobre el protocolo

Una **corrección técnica sobre el protocolo transaccional**, posterior a la devolución
técnica previa y **anterior a la tercera revisión independiente**. No es esa revisión, y **no
certifica `F4c`**. Dos de sus tres hallazgos son BLOQUEANTES, y los tres están en texto que
las correcciones anteriores escribieron.

> **`D16`–`D51` no se reescriben.** Cada fila declara qué queda revisado.

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D52 | El autómata transaccional tiene **SEIS fases**. La ruta de conflicto gana una **intención durable previa**, `reconciliacion-preparada`, que declara la decisión, su autoridad, la base observada, el mecanismo reproducible, el hash final, el orden total y los derivados pendientes **ANTES de tocar ningún canónico** | **D46**, y con ella `D35` | `D46` unificó cinco formulaciones en un autómata de cinco fases, y dejó la ruta de conflicto **sin recuperación**: `reconciliada` declaraba la decisión Y la daba por aplicada, luego una caída entre decidir y emitir dejaba el diario sin la decisión, sin su mecanismo y sin el resultado esperado. **El `preparada` original no sirve de respaldo**: declara el `hash_posterior_esperado` de la transacción, y la decisión puede ser «conservar lo divergente» o «un tercer contenido». La alternativa —conservar cinco fases y meter la decisión dentro de `conflicto`— obliga a que `conflicto` narre en futuro, que es lo que la regla de lectura del diario prohíbe | volver a cinco fases deja la reconciliación sin punto de compromiso, que es el defecto |
| D53 | Lo que se descubre **después** de que una transacción cerró **no es una fase suya**: es un evento **`deriva`**, sin `fase` y sin `tx` propio, que la REFERENCIA sin reabrirla. Reparar exige una **transacción nueva** con su propia intención durable, y **nada se restaura desde Git automáticamente** | **D34** y `D46` | `D34` creó la comprobación de integridad post-terminal y la hizo emitir `conflicto`; `D46` hizo terminal a `derivada`. Juntas producían **una transición que sale del terminal**, que la propia tabla de transiciones declara defecto. La alternativa —reabrir la transacción cerrada— rompe que el diario sea append-only y que `derivada` signifique algo | permitir la transición desde `derivada` obliga a decir qué significa entonces «terminal» |
| D54 | El tipo `evento` declara un **contrato CONDICIONAL por fase**: campos obligatorios, prohibidos, predecesora admitida, hash que gobierna, payload recuperable, autoridad y condición exacta para emitir la siguiente | **D23**, en la forma de `evento` | el contrato anterior tenía un `afecta` genérico y un `resultado` descrito para dos fases. **No podía representar** el `hash_observado` de un conflicto, la copia íntegra de lo divergente, la decisión de una reconciliación, su `hash_final` ni los derivados pendientes. Un esquema derivado de él aceptaría un `conflicto` sin copia de lo divergente y una reconciliación sin resultado reproducible, y §2.6 declara que las dos cosas son defectos | un contrato genérico vuelve a hacer inexpresable lo que el protocolo narra |

### `D55`–`D57` · decisiones de la SEGUNDA corrección técnica sobre el protocolo

Una **segunda corrección técnica**, posterior a `D52`–`D54` y **anterior a la tercera
revisión independiente**. No es esa revisión, y **no certifica `F4c`**. Sus tres hallazgos
—`H1`, `H2` y `H3`— están en texto que la corrección técnica ANTERIOR escribió, que es el
tercer encadenamiento consecutivo en el que eso ocurre.

> **`D16`–`D54` no se reescriben.** Cada fila declara qué queda revisado.

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D55 | Las garantías del protocolo se reparten en **TRES CAPAS** con dueño declarado: **A** esquema estructural del evento —campos, enums, tipos, forma de hashes, exclusión de payloads y coherencia interna—, **B** validador semántico del diario —identidad y unicidad de `tx`, predecesores, transiciones admitidas, continuidad de hashes, ninguna fase posterior a `derivada`, número de iteraciones, terminalidad, correspondencia intención/hecho y consistencia del autómata completo— y **C** runtime y pruebas de caída —orden efectivo de escritura, `fsync` del evento y del directorio antes del primer canónico, locks, comparación contra el disco y roll-forward idempotente— | **D54**, y con ella `D46` y `D23` | `D54` enunció cuatro reglas como *«reglas que un esquema derivado debe hacer cumplir»*, y **tres de las cuatro son incomprobables por un esquema**: un esquema estructural valida un evento AISLADO, no recorre el diario, no reconstruye el autómata y no observa el orden real de `fsync` y `rename`. Atribuirle una propiedad histórica o física **no la proporciona: la deja sin dueño**, y nadie construye después el mecanismo que sí la daría. La alternativa —un «esquema» que abra el diario— no es un esquema: es el validador B con otro nombre, y confundirlos es lo que produjo el defecto | fundir las tres capas en una devuelve exactamente la atribución falsa que se corrige |
| D56 | La recuperación clasifica cada fichero contra la **ÚLTIMA FASE DURABLE que gobierna su ruta**, no contra el síntoma: base y resultado los fija la **intención durable vigente** —`preparada`, o `reconciliacion-preparada` para las rutas que reconcilió—. `conflicto` **sólo** se emite con una **transacción abierta** y un fichero que no casa **ni con la base ni con el resultado**. Un canónico revertido bajo una transacción abierta **se reaplica de forma idempotente**, y si `confirmada` ya era durable **se REEMITE** tras reaplicar: reemitir una fase no es una transición. Un marcador huérfano o un árbol publicado incoherente es **`fallo` de publicación** o **`deriva`**, nunca `conflicto` | **D34**, `D36`, `D35` y `D53` | `W12a` mandaba emitir `conflicto` ante un canónico revertido a su `hash_previo`, y §2.6.4, `W3` y `W4` mandan lo contrario: casar con el hash previo es **NO APLICADO**, y NO APLICADO se completa hacia delante. El mismo estado observable recibía dos clasificaciones incompatibles según por qué ventana se entrara, y la que ganaba escalaba a una persona un resultado que sigue siendo **determinista**. Y la regla del clon emitía `conflicto` sin que existiera transacción abierta alguna en esa instalación, que es una fase de una transacción que allí no hay. La alternativa —hacer `conflicto` el destino de todo síntoma— borra la única distinción que hace recuperable el protocolo | volver a clasificar por síntoma reintroduce las dos lecturas del mismo disco |
| D57 | `tipo` y `fase` son **DOS EJES**, y se declara la matriz: `tipo` nombra el acontecimiento, `fase` su participación en una transacción. Los **siete tipos que escriben estado canónico** —`orden`, `transicion`, `integracion`, `certificacion`, `migracion`, `sellado`, `retirada-de-cuerpo`— llevan `fase` y `tx` **obligatorios** y son ortogonales a las seis fases; `deriva` y `fallo` **no llevan ninguna de las dos, nunca**. Cada tipo declara además su **sujeto**. Formas válidas: **7 × 6 + 2 = 44** | **D54** y `D23` | el contrato condicional de `D54` cubría el eje `fase` —seis fases más `deriva` y `fallo`, ocho filas— y se resumía como «las ocho formas de evento», cuando el enum de `tipo` tiene **NUEVE** valores y siete de ellos quedaban **sin contrato**. Un esquema derivado de ahí no sabría si un `sellado` puede llevar `fase`, ni si un `fallo` puede llevar `tx`. **No se crea ningún tipo nuevo y no se fusiona ninguno**: la prueba de §3.1 no llega a plantearse, porque los nueve valores son valores de un enum del tipo `evento`, no tipos candidatos. El recuento de §3.8 no cambia | declarar una sola dimensión vuelve a dejar siete tipos sin contrato |

### `D58`–`D59` · decisiones de la TERCERA comprobación técnica

Una **comprobación técnica acotada** sobre `D55`–`D57`, posterior a ellas y **anterior a la
tercera revisión independiente**. No es esa revisión, y **no certifica `F4c`**. Sus dos
hallazgos están en texto que la corrección ANTERIOR escribió — el **cuarto** encadenamiento
consecutivo.

> **`D16`–`D57` no se reescriben.** Cada fila declara qué queda revisado.

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D58 | **Emitir y RESTAURAR son operaciones distintas, y `confirmada → confirmada` NO EXISTE.** Si `confirmada` no llegó a ser durable se emite **una sola vez** (`W5`, `W13`); si ya es durable, la recuperación reaplica los canónicos desde `preparada` y **no emite ninguna fase nueva**, siguiendo con los derivados y `derivada`. Volver a materializar un fichero de evento perdido es **restauración idempotente del MISMO evento** direccionado por contenido —mismo `id`, mismo cuerpo, mismo `predecesor`—, y no altera la cadena ni hace crecer el diario. `preparada`, `confirmada`, `reconciliada` y `derivada` aparecen **exactamente una vez** por `tx`; sólo `conflicto` y `reconciliacion-preparada` son **repetibles**, y sólo porque el contrato las declara así con `iteracion` como discriminador y tope de tres | **D56**, y con ella `D37` en su lectura | `D56` llamó «reemisión» a *«un evento NUEVO, con `id` propio, mismo `tx` y MISMA `fase`»*, y eso **contradice §2.8 punto 5**, que ya decía que si la fase existe la operación es una **NO-OPERACIÓN**. Admitirlo creaba una secuencia `confirmada → confirmada` que el autómata de §2.6.1 no tiene y que ninguna transición admite: el diario habría afirmado dos veces el mismo hecho, y la cardinalidad de cada fase habría dejado de ser comprobable. La alternativa —declarar `confirmada` formalmente repetible— exige darle un discriminador y decir qué significan dos, y no significa nada distinto: el hecho es el mismo | admitir la fase de hecho duplicada devuelve el defecto y rompe la cardinalidad por `tx` |
| D59 | **El recuento se separa por ejes, y la matriz es la MÍNIMA demostrada tipo a tipo.** `tipo` tiene **9** valores; las fases transaccionales son **SEIS** —`deriva` y `fallo` son valores de `tipo`, no de `fase`—; los estados del campo `fase` son **SIETE** contando su ausencia. **`orden` es CONDICIONAL**: lleva `fase` y `tx` si y sólo si el consumo produce al menos una escritura canónica. Combinaciones válidas **45**, prohibidas **18**, sobre un espacio de **63**. Y se declara que **escribir los eventos del propio diario NO abre otra transacción**: la frontera es AÑADIR frente a MODIFICAR, no «estar bajo `estado/`» | **D57**, y con ella `D54` | `D57` contó **ocho filas de una tabla como si fueran ocho valores del eje `fase`** —metiendo `deriva` y `fallo` en el eje equivocado— y derivó un **producto cartesiano** `7 × 6 + 2 = 44` **sin demostrarlo tipo a tipo**. Al demostrarlo: `a.9` describe consumos de orden que **no aplican y no modifican el estado canónico** —base inexistente tras un rebase, agotamiento de `MAX_CAS_RETRIES`—, luego `orden` no puede exigir transacción siempre. La alternativa —conservar el cartesiano porque «cierra el contrato»— es exactamente el error que `D18` y §3.8 prohíben: fijar un número antes de aplicar la prueba. **Ningún tipo se crea ni se fusiona, y §3.8 no cambia** | volver al cartesiano obliga a declarar transaccional un evento que no escribe nada canónico |

### `D60`–`D61` · decisiones de la CUARTA comprobación técnica

Comprobación **estrictamente acotada** sobre `D58`–`D59`, anterior a la tercera revisión
independiente. No es esa revisión, y **no certifica `F4c`**. Sus dos hallazgos están, otra
vez, en texto que la comprobación ANTERIOR escribió: **quinto encadenamiento consecutivo**.

> **`D16`–`D59` no se reescriben.** Cada fila declara qué queda revisado.

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D60 | **La cardinalidad de cada fase es CONDICIONAL A LA RUTA y al cierre**, no absoluta. `confirmada` y `reconciliada` son **mutuamente excluyentes**; `derivada` es 1 si cerró y **0** si sigue abierta. Ruta normal cerrada: `preparada` 1 · `confirmada` 1 · `conflicto` 0 · `reconciliacion-preparada` 0 · `reconciliada` 0 · `derivada` 1. Ruta de conflicto cerrada: `preparada` 1 · `confirmada` 0 · `conflicto` = `reconciliacion-preparada` = `k` ∈ {1,2,3} · `reconciliada` 1 · `derivada` 1. Ruta de conflicto **agotada y abierta**: `conflicto` **4** · `reconciliacion-preparada` **3** · `reconciliada` 0 · `derivada` 0, marcador abierto y escalado. Y el contador queda cerrado: `iteracion` empieza en **1**, la comparten `conflicto(i)` y su `reconciliacion-preparada(i)`, incrementa sólo al abrir un `conflicto` nuevo, **el tercer `conflicto` SÍ recibe decisión**, y el cuarto es el **marcador de parada** sin decisión | **D58** | `D58` declaró que *«`preparada`, `confirmada`, `reconciliada` y `derivada` aparecen exactamente una vez por `tx`»*, y **ninguna transacción real puede cumplirlo**: la ruta normal no tiene `reconciliada`, la de conflicto no tiene `confirmada`, y una transacción agotada no tiene `derivada`. Un invariante que nada satisface no es comprobable, y el validador semántico habría rechazado todo diario válido. Además el tope estaba dicho de tres formas —«tope de TRES iteraciones», «a la tercera se detiene», «`iteracion` = 3 → se detiene»— sin definir dónde empieza el contador ni si el tercer conflicto recibe decisión. **La alternativa —callar el cuarto `conflicto` para que no haya «cuarta iteración»— contradice §2.6.4**: la clasificación produce `conflicto` ante divergencia real, y un hecho observado no se calla | volver a un invariante absoluto lo hace insatisfacible otra vez |
| D61 | **La frontera que exige `tx` es UN criterio, y no es «añadir frente a modificar»:** una escritura canónica exige transacción **si y sólo si** toca **más de un fichero canónico** o **sustituye contenido previo**. No la exige la escritura que sea **un solo fichero, nuevo y direccionado por su contenido**, porque ahí el nombre es la verificación. En consecuencia **`sellado` NO es transaccional** —añade un único fichero `SL-<huella>` que nunca se reemplaza—, **`retirada-de-cuerpo` SÍ lo es** —sustituye el cuerpo de un evento por su lápida—, y los eventos del propio diario no abren recursión **por el criterio general**, no por una excepción escrita para ellos. Regímenes: **5** siempre transaccionales, **1** condicional (`orden`), **3** siempre no transaccionales (`sellado`, `deriva`, `fallo`). Recuento derivado: **40** válidas · **23** prohibidas · **63** de espacio | **D59**, y con ella `D57` | `D59` afirmaba a la vez que `sellado` *«sólo AÑADE un fichero»*, que la frontera era *«AÑADIR frente a MODIFICAR»* y que `sellado` exige `tx` **siempre**. **Las tres no pueden ser ciertas juntas**: con esa frontera, `sellado` cae del lado que no la exige, igual que añadir un `preparada`. La frontera era falsa y tapaba que `sellado` estaba mal clasificado. Comprobado contra §2.9: sellar **no edita ni borra eventos** —retirar un cuerpo es un acto separado—, **no escribe índices** —son derivados— y **no toca el item** —cerrarlo es un `transicion`—. La alternativa —conservar la `tx` «por prudencia»— mantiene un contrato que el propio texto desmiente, y deja sin dueño la pregunta de qué separa de verdad las dos clases de escritura | volver a la frontera de añadir/modificar reintroduce la contradicción, y con ella la clasificación falsa de `sellado` |

**El recuento de `§3.8` NO cambia**, y por el mismo motivo que en `D57` y `D59`: `sellado` no
deja de ser un valor del enum de `tipo` del artefacto `evento`. Lo que cambia es su régimen
transaccional, no su existencia como tipo. **`O15` queda intacta.**

### `D62` · decisión de la QUINTA comprobación técnica

Comprobación de **un solo punto** sobre `D60`. No es la tercera revisión independiente, y **no
certifica `F4c`**. Su hallazgo está, otra vez, en texto que la comprobación anterior escribió:
**sexto encadenamiento consecutivo**.

> **`D16`–`D61` no se reescriben.**

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D62 | **OBSERVACIÓN e INTENTO son dos conceptos con dos contadores, y no uno.** `conflicto` lleva `observacion` ∈ 1..4, `intentos_consumidos` ∈ 0..3 con `intentos_consumidos` = `observacion` − 1, y `agotado: true` **únicamente** en la cuarta observación — y con él **no admite ninguna `reconciliacion-preparada`**. `reconciliacion-preparada` lleva `intento` ∈ 1..3 y `resuelve`, el `id` del `conflicto` que atiende; **nunca existe un `intento: 4`**. **`MAX_CAS_RETRIES = 3` limita INTENTOS, no OBSERVACIONES**, y la cuarta observación registra el **fracaso del tercer intento** sin silenciarlo. Máximos: **4 observaciones · 3 intentos**. Los totales de eventos **no cambian**: 3 · 5 · 7 · 9 · 8 | **D60** | `D60` usó **un solo campo `iteracion`** para numerar dos cosas distintas, y de ahí salieron seis afirmaciones que no pueden ser ciertas a la vez: que empieza en 1, que la comparten `conflicto(i)` y `reconciliacion-preparada(i)`, que incrementa al abrir un conflicto, que el máximo es 3, que la ruta agotada termina en `conflicto(4)`, y que ese cuarto «no es una cuarta iteración». **Un campo que vale 4 bajo un máximo de 3 no es un contador: son dos contadores con un solo nombre.** La alternativa —callar la cuarta observación para que el contador no pase de 3— contradice §2.6.4, que produce `conflicto` ante toda divergencia real, y dejaría el diario afirmando tres intentos sin decir cómo acabó el tercero | volver a un contador único reintroduce las seis afirmaciones incompatibles |

### `D63` · decisión de la SEXTA comprobación técnica

Comprobación acotada sobre la semántica de sellado y retirada de cuerpo. No es la tercera
revisión independiente, y **no certifica `F4c`**. **Séptimo encadenamiento consecutivo.**

> **`D16`–`D62` no se reescriben. `O15` queda íntegra.**

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D63 | **La lápida es una EXCEPCIÓN TIPADA al algoritmo de identidad, las garantías son TRES y no una, la retirada exige FUENTE DE RECUPERACIÓN comprobada, el diario físico NO es estrictamente append-only, y sólo una DEPENDENCIA SEMÁNTICA VIVA bloquea la retirada.** Un evento con `cuerpo_retirado: true` no se somete a `EV-H(evento MENOS id)`: se valida su estructura y su vínculo con el sellado. Nivel 1 continuidad estructural · Nivel 2 consistencia del compromiso · Nivel 3 verificación completa, que **exige el cuerpo original** desde un `localizador` —`revision`, `ruta`, `hash_esperado`— cuya recuperación se **comprobó y registró antes** de retirar. Una referencia estructural `predecesor` **no** bloquea; una dependencia que necesita leer el cuerpo **sí** | **`D37`** en la regla de identidad · **`D61`** en la frontera y en el append-only · y la semántica de sellado de `D16`/`D23` | El contrato afirmaba `id = EV-H(evento MENOS id)` **y** que la lápida conserva el mismo `id`: tras retirar, ese `id` **ya no puede recalcularse desde el fichero**, y la identidad por contenido deja de ser verificable por la regla ordinaria. Además prometía de más —«la huella demuestra que el cuerpo existió y cuál era», «recomputar la cadena», «sigue siendo verificable»—: una huella es un COMPROMISO, y sin preimagen no prueba contenido ni posesión. Y la regla «no puede retirarse un evento al que apunte cualquier evento vivo» hacía **inalcanzable la propia operación**, porque cada evento apunta al anterior por `predecesor`. Por último, «sustituir no es editar» era falso: **sustituir un cuerpo edita físicamente un fichero existente**. La alternativa —debilitar la regla de identidad para que la lápida la cumpla— rompería la identidad de todos los eventos íntegros para acomodar el caso excepcional | volver a un algoritmo único de identidad deja la lápida sin forma válida de validarse; volver a «cualquier evento vivo» vuelve a hacer imposible retirar |

**Lo que NO cambia, y se comprueba:** `sellado` sigue siendo **no transaccional** y
direccionado por contenido; `retirada-de-cuerpo` sigue siendo **transaccional**; la matriz
sigue en **9 tipos · 6 fases · 40 válidas · 23 prohibidas**; las cardinalidades y los
contadores de conflicto no cambian; **no aparece ninguna transición nueva**; y el recuento de
`§3.8` sigue igual. **`O15` permanece intacta.**

### `D64` en adelante · decisiones de la TANDA INTEGRADA que cierra la tercera revisión

La **tercera revisión independiente** devolvió `F4c` con veredicto de **INSUFICIENTE PARA
F5**: dos BLOQUEANTES, ocho GRAVES, cinco MEDIOS y siete MENORES. Su juicio se conserva
íntegro e inmutable en `docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md`. Estas
decisiones son la **corrección conjunta** de sus hallazgos reproducibles.

> **`D16`–`D63` no se reescriben. `O15` queda intacta.**

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D64 | **La ruta de conflicto se COLAPSA.** Se retiran `reconciliacion-preparada`, `reconciliada`, los contadores `intento`, `intentos_consumidos` y la bandera `agotado`, y las nueve ventanas `R1`–`R9`. El autómata queda en **CINCO fases** —`preparada`, `confirmada`, `conflicto`, `abandonada`, `derivada`—, **seis transiciones** y **DOS terminales**, y **todo terminal retira el marcador**. `conflicto` es una OBSERVACIÓN bloqueante con **DOS salidas**: si la divergencia cesa, la transacción se completa hacia delante; si no, la autoridad emite `abandonada`, que cierra sin completar, retira el marcador y emite un `deriva` con `causa: abandono-de-transaccion` que **conserva el bloqueo acotado a los items nombrados**. La reparación es una **transacción NUEVA** que, al cerrar, resuelve ese `deriva`. `observacion` se conserva **sin tope**: numera estados divergentes distintos, no reintentos | **`D35`**, `D46`, `D52`, `D60` y `D62`, y con ellas la justificación de `D38` | **`B1`**: desde `conflicto(observacion: 4, agotado: true)` **no existía ninguna transición admisible**, el marcador no se retiraba nunca y, por la regla de commit, el control repo no volvía a commitear jamás **para todo el producto**, por un solo conflicto sobre un solo fichero. **`G2`**: la ruta larga resolvía con tres fases, tres contadores y una bandera el mismo problema que §2.6.11 resuelve con un evento sin fase y una transacción nueva — y su único argumento, que la intención original gobierna, no se sostenía porque el `hash_final` la SUSTITUÍA. Se comprobó garantía a garantía que **no se pierde ninguna**. **`M5`**: el tope tomaba `MAX_CAS_RETRIES` de `a.9` **suprimiendo su quinto paso**, que es una salida; ahora los tres mecanismos de reintento están separados con su nombre, contador, salida y autoridad. La alternativa —añadir una transición de salida al estado agotado— conserva un mecanismo desproporcionado y sólo rodea el defecto | reinstaurar la ruta larga devuelve el estado sin salida y la duplicación de mecanismos |
| D65 | **El gobierno Git del REPOSITORIO DE CONTROL se escribe**, con su tabla de propiedad —quién pide, ejecuta, bloquea y verifica commit, push, rama, PR, CI, rollback y retirada—. **`main` del control repo es la rama canónica y NO recibe `G29`**, que `E2.4` conserva por source; lo que la protege es un único escritor, commits sólo entre transacciones y push bajo autoridad. **PR y merge no se usan para el estado**, sí para el material revisable. La publicación es **actualización optimista contra la revisión conocida**, con rechazo non-fast-forward a `fallo` y escalado, y **`--force` prohibido salvo procedimiento extraordinario del Owner**. La «política de publicación» deja de ser una sede inexistente y pasa a ser **`adaptador.publicacion_control_repo`**, con tres valores y `esperando-owner` por defecto — y **ninguna política autoriza publicar una recuperación**. De las cuatro alternativas de aislamiento se elige la mínima: **diario para recuperar, Git para publicar**, sin dos mecanismos para el mismo estado de recuperación | **`D41`**, que declaró el hueco, y la regla 3 de §2.6.10 | **`B2`**: el texto prometía no rellenar el hueco por inferencia y lo rellenaba tres reglas después invocando `G29` para el control repo, que `E2.4` acota a las fuentes. Con `main` protegida, sin rama de trabajo, sin PR y sin política definida, **ningún commit de `estado/` podía llegar a publicarse**, y caían las garantías 5 y 6 de §2.6.6, la reconstrucción de §2.9, la condición previa de toda `retirada-de-cuerpo` y la permanencia de `O15`. **`M1`**: la política alternativa se invocaba una sola vez en todo el corpus y no existía. Rama o worktree por transacción se descarta porque saca el estado en vuelo del árbol que `R1` obliga a leer sin herramienta y crea un SEGUNDO mecanismo de recuperación. **La sede normativa NO se crea aquí**: queda registrada como `PN-11` para F5, y `C7` no se toca | volver a invocar `G29` para el control repo bloquea toda escritura del runtime |
| D66 | **`a.9` se cita como `a.9` lo escribe, y CONCEPTO no es CAMPO.** Los cinco conceptos son `propietario del campo` · `autoridad` · `ordenante` · `escritor del comando` · `ejecutor de mutación`. De ellos, **cuatro son campos del evento y el propietario del campo SE DERIVA** de la matriz de §1.3; `actor_atribuido` se conserva como campo obligatorio pero **declarado aparte**, porque pertenece a otra lista de `a.9`. Y **`fallo` recibe una semántica CERRADA**: `sujeto`, `operacion` con enum cerrado, `causa`, `estado_observado`, `recuperable`, `autoridad_requerida`, `accion_siguiente`, `evidencia`, y **`tx_afectada` como REFERENCIA** más `referencias[]` con commit, rama y remoto | **`D23`** en la forma de `evento`, y `D54` en su contrato condicional | **`G1`**: F4 sustituía `propietario del campo` por `actor_atribuido` y presentaba el resultado como «los cinco de `a.9` sin confundirlos», que es literalmente lo que `a.9` advierte que no se haga; y esa lista era el conjunto de campos obligatorios de todo evento, invocado seis veces y convertido en condición de validación por `X39`. **`G3`**: `fallo` prohibía `tx` mientras cuatro pasajes normativos y dos filas adversariales le exigían nombrar un `tx` y un commit — `X15` y `X28` **no eran satisfacibles**. La alternativa de persistir también el propietario del campo se descarta: sería una segunda sede editable de lo que §1.3 ya fija, y `I5` lo prohíbe | volver a la lista anterior reintroduce una cita que su fuente no respalda |
| D67 | **Los cuatro macrocircuitos se MAPEAN a los procesos de `b.16`**, fase a fase, con proceso canónico, **propietario global tomado de `b.16` y no elegido**, participantes, entrada, salida, gate y estado persistido. **No se crea ningún proceso nuevo**: instalar, migrar y actualizar son `proceso:SIS`; inventariar y reconstruir, `proceso:INV`; retirar lo heredado, `proceso:DEU`; propagar y certificar, `proceso:DEP`. «Su plantilla de ruta» deja de sugerir un artefacto inexistente y pasa a ser esa tabla. **§8.3 gana `LEE`, `ESCRIBE`, `AUTORIDAD`, `EJECUTOR` y el gobierno de su retirada destructiva** —`M6` como source changes bajo `C7`, por fuente, con las cuatro condiciones y `INTEGRACIÓN PARCIAL`—. **§8.4 gana `ESTADO`**, con la instantánea de `U3` declarada DURABLE y versionada en `estado/instantaneas/`, y una reanudación que no depende del chat. Y **`N0` crea el item real `SIS-001`**, no un `items/INI-001-paq/` que violaba §2.8, §2.3 y `D45` | **`D30`**, `D32`, `D33` y `D45` en su lectura | **`G6`**: tres de los cuatro macrocircuitos no nombraban proceso, y la ruta, las obligaciones, el propietario global y los gates se DERIVAN del proceso — F6 habría tenido que elegirlo, y eso es una decisión arquitectónica. **`G4`**: §8.3 era el único con un paso destructivo sobre repositorios ajenos y no declaraba qué escribía, ni invocaba `C7`, ni trataba N fuentes. **`G5`**: `U` es el circuito con más superficie de estado y no declaraba ninguna sede, y la instantánea de `U3` no tenía ni ubicación ni plano. **`G7`**: `N0` creaba un paquete que pertenecía a una iniciativa, y `D45` lo declara imposible | crear un proceso nuevo obliga a pasar la prueba de §3.1 y a entrar en el recuento |
| D68 | **La taxonomía documental se alinea LITERALMENTE con las doce áreas del `§5.18`** que `O8` resuelve: se restituye **«mapa documental»** como área 1 y **«arquitectura actual y dirección arquitectónica» vuelve a ser UNA**, no dos. Las condicionales pasan a ser las CATORCE que `§5.18` enumera, y la taxonomía queda declarada en tres clases —obligatorias, condicionales, ampliaciones— con lo que se puede fusionar y lo que no se puede omitir. El área 1 se declara **DERIVADA** de los bloques `ads:memoria` y las celdas de cobertura documental, y esa precisión se registra como **`PN-12`** | **`D26`** y `D43` en la proyección de las áreas | **`G8`**: F4 declaraba doce áreas que **no eran las doce de `O8`** — eliminaba el punto 1 y partía el 5 en dos, conservando el número y no el conjunto. «Mapa documental» aparecía **una sola vez en todo el repositorio**, en `§5.18`, y F4 no lo mencionaba ni para retirarlo. Cada área es un `contrato-de-aspecto:documental/<area>`, luego F6 habría construido doce contratos para las áreas equivocadas, y `§5.23` se habría quedado sin la sede que necesita. **`O8` NO se reescribe**: se corrige la cita y se registra la precisión como presión | volver a partir «arquitectura» da dos contratos donde `O8` fija uno |
| D69 | **Se separa el estado ESTABLE del ESPECULATIVO, y `abandonada` pasa a ser REVERSIÓN LOCAL VERIFICADA.** Estable es el último commit aceptado de la rama canónica: verdad publicable, reconstruible desde otro clon, **nunca con una transacción parcialmente aplicada**. Especulativo son las escrituras posteriores a `preparada` y anteriores al terminal: **nadie las ha visto**, no entran en ningún commit ordinario, y por eso revertirlas no destruye trabajo de nadie. Arrancar una transacción exige **worktree limpio, `HEAD` conocido, sin solape, intención causal PUBLICADA, revisión base declarada, hashes previos y capacidad comprobada de restaurar**. `abandonada` es **inalcanzable** hasta CAPTURAR la divergencia, DETENER, RESTAURAR todos los canónicos afectados a la revisión base —incluidos los que ya alcanzaron su posterior—, VERIFICAR byte a byte, y sólo entonces CERRAR. El commit posterior lleva **la base consistente más el incidente**, y **ningún `hash_posterior_esperado`**. Si no se puede preservar o verificar, la transacción **permanece abierta y no se publica nada** | **`D64`** en la semántica de `abandonada`, y `D16`/`D23` en la de «roll-forward only» | La comprobación adversarial previa al gate encontró que `abandonada` retiraba el marcador **dejando el conjunto parcial publicable**, y que «el item queda bloqueado» no lo salvaba: el bloqueo es sobre el despacho y el commit era lo que el marcador impedía. Un conjunto parcial **no es consistente porque cada `rename` sea atómico**. Y «roll-forward only» era cierto para el estado PUBLICADO y se aplicaba también al ESPECULATIVO, que nadie ha visto — el contenido anterior **está en la revisión base**, que Git ya conserva, luego no se duplica nada. Con esto `abandonada` **ES la rama REVERTIR de `b.14`**, y no hay un tercer desenlace. La prohibición de revertir automáticamente lo YA PUBLICADO sigue entera | volver a cerrar sin restaurar publica una mezcla parcial |
| D70 | **La recuperación se declara en TRES niveles, y se retira toda promesa de reanudación distribuida.** **A** misma máquina y mismo disco: recuperación EXACTA, puede continuar, restaurar o abandonar. **B** otra máquina con la transacción **ya cerrada y publicada**: recuperación completa desde Git, incluido el incidente con su divergencia conservada. **C** otra máquina con la transacción **abierta y no publicada**: **no existe reanudación exacta** — se REINICIA desde la última intención publicada y la revisión base, y se pierde toda observación que sólo existiera en la máquina perdida. Se declara la limitación aceptada y que soportar lo contrario exigiría publicar un checkpoint aislado, capacidad **no construida y no incluida**. Y se corrige la comparación de alternativas: **un worktree o rama transaccional NO contradice `R1`** —`R1` exige ficheros de texto legibles sin informe intermedio, no que estén en el worktree principal—: se descarta por **coste y duplicación de mecanismos**, y entran en la comparación la cuarentena y el reinicio desde intención publicada | **`D65`** en su comparación de alternativas, y la contención de `D64` | La comprobación adversarial encontró que «otra máquina reanuda clonando el control repo» es **imposible** para una transacción abierta: sus eventos no están commiteados —la regla de commit lo impide—, el marcador no viaja (`D50`) y las escrituras especulativas tampoco. Las cuatro afirmaciones —diario para recuperar, Git para publicar, commits sólo entre transacciones, reanudación desde otra máquina— **no eran compatibles**, y la cuarta era la falsa. Además el descarte del worktree invocaba `R1` sin fundamento, verificado contra `E2.1` literal. También se acota el paralelismo: **un único ejecutor por worktree**, ninguna segunda transacción canónica concurrente, y el paralelismo real por varios worktrees queda como capacidad futura | prometer reanudación distribuida sin publicar checkpoints aislados vuelve a ser falso |

### `D71`–`D86` · las decisiones de la TANDA INTEGRADA DE CORRECCIÓN del gate final

El **GATE FINAL INDEPENDIENTE** (`docs/evolucion/16-…`) y su **COMPLEMENTO DE COBERTURA**
(`docs/evolucion/17-…`) dejaron **44 hallazgos abiertos, 43 distintos** —4 BLOQUEANTES, 6
GRAVES, 20 MEDIOS y 14 MENORES—, adjudicados uno a uno contra su fichero y su línea por
agentes con contexto limpio. Sus juicios se conservan **íntegros e inmutables**: estas
decisiones son la corrección, no una reescritura de aquéllos.

> **`D16`–`D70` no se reescriben. `O15` y `O16` quedan intactas.**

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D71 | **`abierta(tx)` es un predicado ÚNICO, NOMBRADO y con sede: §2.6.1.** `abierta(tx) ≡ ∃ preparada durable con ese tx ∧ ¬∃ evento de ese tx con fase ∈ {derivada, abandonada}`. Lo evalúa el **validador semántico del diario**, no el esquema; `estado/tx/<TX>.abierta` lo acelera y no lo define. Las **siete** sedes que decidían si una transacción sigue abierta REMITEN aquí y ninguna lo redeclara | **`D46`** y `D64` en su proyección: «`derivada` es el único terminal» dejó de ser cierto cuando `abandonada` pasó a ser terminal | `A2`, BLOQUEANTE: tres sedes seguían afirmando terminal único, luego una transacción `abandonada` satisfacía «sin `derivada`» — **el marcador no se retiraba nunca**, la regla de lectura la seguía declarando en vuelo y la regla de commit seguía bloqueando el control repo. La alternativa —corregir las tres frases— deja el predicado sin sede y el defecto se repite a la siguiente decisión | volver a redeclararlo en cada sede reintroduce la divergencia |
| D72 | **`deriva.causa` es un enum CERRADO de TRES valores con UNA sede: §3.6.** `posterior-al-cierre` · `sin-transaccion` · `abandono-de-transaccion`. `tx_afectada` es **obligatorio** con la primera y la tercera y **prohibido** con la segunda. §2.6.11 pasa a GLOSAR y declara expresamente que si difieren manda §3.6 | **`D53`** y `D64`, que añadieron el tercer valor sin llevarlo a la sede del contrato | `A1`, BLOQUEANTE: §3.6 declaraba DOS valores y una condición de `tx_afectada` que §2.6.11 y la capa A del validador ya desmentían. Un esquema derivado de §3.6 **habría rechazado el `deriva` que `abandonada` obliga a emitir**, que es el que conserva el bloqueo. La alternativa —dejar el enum en §2.6.11— pone el contrato del evento fuera de §3.6, que es de donde F6 deriva el esquema | volver a dos valores hace inalcanzable `abandonada` |
| D73 | **§7.4 paso 2 recoge LAS DOS RAMAS de `a.9`**, con el predicado de `D71`: COMPLETAR, o MARCAR conflicto cuyas dos salidas son `confirmada` y `abandonada` —y `abandonada` restaura lo especulativo local a `revision_base` y lo verifica byte a byte—. Ninguna cierra dejando mezcla parcial publicable. `PN-7` deja de presionar por «una rama ausente» y pasa a presionar por una **precisión**: (b) no distingue estado PUBLICADO de ESPECULATIVO | **`D69`** en su proyección sobre §7.4 y sobre el resumen de §16 | `A3`, GRAVE: `D69` dio a `abandonada` su rama de reversión, y §7.4 y el resumen de §16 se quedaron diciendo que §2.6 «elimina el ramal de reversión por completo». Un lector tenía **dos contratos incompatibles** sobre el mismo paso. La alternativa —retirar `PN-7`— es falsa: la desviación respecto de la LETRA de `b.14` sigue existiendo | volver a la formulación vieja reintroduce la contradicción con `D69` |
| D74 | **La COMPOSICIÓN DE RUTA gana sede canónica en §8.0, y no se crea ningún tipo.** La composición es un conjunto de **items ENLAZADOS** agrupados por una `iniciativa`, porque `b.1` fija que un item tiene exactamente un proceso. Una capacidad entra por **CUATRO vías y no hay una quinta**: propietaria global, obligatoria, condicional con condición comprobable, o **item propio enlazado** bajo el proceso que sí la declara —regla que `b.16` ya escribe para `AUD` y para `DIR`—. Y se separan de la ruta dos formas de estar presente que no son participar: **EJECUTOR** (`PLT` bajo `C7`, `a.5`) y **AUTORIDAD** (el Owner en los gates), más el **ENCUADRE** previo (`ENC`, que `b.16` no declara en ningún proceso). Se declara el gate de composición, la evidencia, la comprobación de entrada y salida por capacidad, y el error `composicion-incompleta`. **`C5` NO es el vehículo**: materializa entregas entre capacidades que ya participan | **`D67`** en su columna de participantes | `B-2`, BLOQUEANTE, con la conclusión adjudicada del NIVEL 0 sobre `C5`: `D67` asignó procesos sin comprobar que admitieran a los participantes ya declarados, y trece no tenían por dónde entrar. El hueco cubría **cinco** capacidades. La alternativa —inventar instancias de handoff— la cierra el NIVEL 0: siete de las diecisiete instancias disparan sobre el criterio `C-<CAP>` que el proceso declara, luego el handoff presupone la ruta. La alternativa de ensanchar `b.16` es normativa y su sitio es `PN-13` | volver a listar participantes sin vía devuelve las trece entradas sin vehículo |
| D75 | **`A2`–`A7` es `proceso:AUD`, en items ENLAZADOS uno por conclusión**, con propietario global **DERIVADO por item** —`01-PROCESOS.md` L419 prohíbe asignarlo a mano—: las ocho reconstrucciones de `A6` son ocho conclusiones independientes con propietarias distintas, que es literalmente el caso que `b.16` resuelve para `AUD`. `INV` es su **única obligatoria** y ejecuta sin responder de la conclusión (`a.5`). La tabla de §18 se reescribe con la vía de cada capacidad, se separan ejecutor y autoridad, se rotula `U5a` y `U5b`, **`SEG` y `CON` entran en `U5b` como OBLIGATORIAS de `proceso:DEP`** —`G28` hace irretirable a `SEG`—, `ARQ` entra en la migración por el `plan-tecnico` de su item `DEU`, y **`U6` deja de ser `O12`**: una actualización no arranca programación, luego revalida el nivel vigente | **`D67`** en el proceso de `A2`–`A7`, en los participantes de `U5b` y en el gate de `U6` | `B-1`, BLOQUEANTE: §8.2 y §18 asignaban procesos incompatibles a las mismas fases, y la elección determina qué condicionales existen. `G-1`: `U5b` es `proceso:DEP` y `SEG` es obligatoria que **nadie puede retirar**, y no figuraba. `G-2`: `ARQ` faltaba y `cambio-construido` no nombraba a `CON`. `M-3`: `U6` tenía dos gates distintos en dos sedes. `m-4`: `U5a` no estaba rotulada. La alternativa —elegir `AUD` y asignarle un propietario a mano— la prohíbe `01-PROCESOS.md` L419 | volver a `proceso:INV` deja a `DOM`, `SEG` y `DIS` sin vía en la adopción |
| D76 | **`N5` produce el BASELINE y la CLASIFICACIÓN DE DESCONOCIDOS CRÍTICOS de la instalación, y el Owner lo aprueba** como gate propio de `N5` — la misma disposición que `A3` en la adopción. Cada desconocido queda clasificado como resuelto, acotado con su portador, o deferido con su motivo | **`D67`** en los gates de `N` | `G-3`, GRAVE: `N7 = O12` y `O12` exige **las tres** —Integrada, baseline aprobado y ningún desconocido crítico sin clasificar—, y **ninguna fase de `N` producía las dos últimas**: el gate era invocable y no satisfacible. La alternativa —registrarlo como presión normativa y preguntar al Owner— le llevaría una pregunta que su propia resolución sobre la adopción ya responde en `A3`. No reinterpreta `O12`: le da el productor que le faltaba | quitarle el productor devuelve un gate que no se puede superar |
| D77 | **Las doce áreas documentales reciben IDENTIFICADOR**: `aspecto:documental/mapa-documental`, `identidad-de-producto`, `baseline-funcional`, `dominio-y-glosario`, **`arquitectura`** —una, no dos—, `tecnologias-y-desarrollo`, `direccion-de-ingenieria`, `calidad-y-pruebas`, `seguridad-y-riesgos`, `despliegue-y-operacion`, `decisiones` y `evolucion-documental`. **No se inventan**: se derivan del patrón `^memoria:[a-z0-9-]+$` de `esquemas/memoria.yaml`, que ya tiene doce ejemplares trabajados y el mismo reparto de campos. Las CATORCE condicionales **no** reciben identificador aquí | **`D68`** en la proyección de las doce áreas, y el ejemplo de §5.6/§5.7 | `G-4`, GRAVE: §5.7 afirma que cada área resuelve a un `contrato-de-aspecto:documental/<area>`, **ninguna tenía identificador declarado**, y el único ejemplo del corpus usaba `arquitectura-actual` —la mitad partida que `D68` ya había retirado—. F6 habría inventado doce, y dos productos habrían inventado doce distintos. La alternativa —dar contrato editable también a «dirección visual» y «sistema de diseño»— crea la SEGUNDA SEDE que `I5` prohíbe: ya tienen sede canónica y su contrato se compila desde ella | inventar identificadores fuera del patrón rompe la comprobación que `memoria.yaml` ya hace |
| D78 | **Un `deriva` sin reparar lleva su propio marcador legible**: `estado/deriva/<ID>.abierta`, con el `id` del evento, las rutas y los items que bloquea, y su causa. Se crea con el evento y **se retira cuando una `derivada` lo referencia en `resuelve_deriva`**. Reconstruible desde el diario por `bloqueado_por_deriva(item)`, fuera de Git por la excepción de ruta de §2.4, y sin identidad propia: el paso 4 de §3.1 sigue dando COMPONER | **`D64`** en la regla de lectura, paso `2bis` | `A8`, MEDIO: el paso `2bis` obliga a TODO lector a mirar los `deriva` sin reparar, y encontrarlos exigía recorrer `estado/eventos/` entero — **exactamente el coste que el párrafo anterior acababa de rechazar para el marcador de transacción**, por el mismo `R1`. La regla era ejercible por el runtime y no por un lector humano. La alternativa —rehacer la justificación del marcador— deja la asimetría escrita y no la explica | quitarlo devuelve una regla que sólo el runtime puede ejercer |
| D79 | **El desenlace `4b` lo cierra un ACTO DE AUTORIDAD DEL OWNER, y son dos**: (i) autorizar la CUARENTENA de lo divergente en `estado/cuarentena/<TX>/`, con su hash en el `conflicto`, con lo que el desenlace 4 vuelve a ser alcanzable; (ii) declarar IRRECUPERABLE el estado especulativo local y ordenar el cierre, con `abandonada` registrando el `estado_observado[]` de todas las rutas tal como están y el commit de incidente **excluyendo las divergentes**. Ninguna es automática, ninguna la toma el runtime, y `X58` deja de afirmar terminación por construcción | **`D69`** en la alcanzabilidad de `abandonada`, y `X58` | `A9`, MEDIO: `4b` retenía el marcador **para siempre** sin ninguna autoridad nombrada que pudiera cerrarlo, mientras `X58` afirmaba que «ninguna transacción puede quedar reteniéndolo para siempre». Era la misma clase de estado sin salida que `D64` acababa de retirar, un piso más abajo. La alternativa —sólo corregir `X58`— deja el bloqueo sin quien lo levante | sin las dos salidas, `4b` vuelve a ser retención indefinida |
| D80 | **Un finding producido por el sistema tiene CLASE, FORMA y RAMA propias**: `entrada:finding-de-auditoria` (décima clase), `forma:finding` (decimoquinta forma) y una rama del algoritmo de `03-FORMAS` **anterior a su cláusula de cierre**, que se activa cuando la entrada trae `sujeto`, `aspecto` y `evidencia` de una celda de cobertura. Su SUJETO es esa celda, no el Owner, y su salida es un encuadre `listo-para-dsp` o un descarte con motivo, **nunca una ficha de vivero** | **`D67`** y el remedio 3.11 del gate, que resultó insuficiente | `M-6`, MEDIO: todo el aparato de entrada tiene UN SOLO SUJETO, el Owner —nueve clases sobre su expresión, catorce formas sobre su expresión— y `03-FORMAS` cierra con «11 en otro caso → `forma:idea-inmadura`», que **manda al vivero todo finding de un `AUD`**. «Añadir `capacidades/ENC/` a las extensiones de ficha» no cerraba nada: sin clase, sin forma y sin rama, la extensión no tenía dónde aterrizar. La construcción es de F6; el contrato queda aquí | sin la rama, el algoritmo sigue mandando los findings al vivero |
| D81 | **El contenido del BASELINE de `A3` es el §6.2 de la directiva, literalmente**: sus CATORCE preguntas, sin reordenar. Cada respuesta lleva **evidencia** —ruta, revisión y qué se observó— y **grado**: OBSERVADO, DERIVADO o DECLARADO, con el patrón de `diseno/03-ESCALA-DE-NOVEDAD.md`, que ya evalúa «mirando el producto, no interpretando». «No se pudo determinar» es respuesta admisible con motivo; el silencio no. Y §15.2 **desglosa el apartado 6** en sus cinco subapartados | **`D67`** en el gate de `A3`, y `m3` en la tabla de §15.2 | `M-9`, MEDIO: `A3` era «BASELINE con evidencia» y su gate «aprobado por el Owner», **sin decir de qué**, mientras §15.2 trazaba el apartado 6 entero en una fila — lo que hacía invisible que `6.2` tiene contenido exigible. F6 habría inventado el contenido de un gate que el Owner aprueba. La alternativa —escribir catorce preguntas propias— duplica una lista que la directiva ya fijó | inventar el contenido del baseline lo saca del control del Owner |
| D82 | **Cada macrocircuito declara cuántos ITEMS compone y cómo le afecta el FRENO 3 de `a.7`.** Los items líderes son las FILAS de §18 —N 2, A 4, M 2, U 4—, más los enlazados de la vía 4. Y el freno: en `N` y en `A` **el antecedente es falso** —no hay items de producto listos antes de `N7`/`A10`—, y en `A` además sólo dos de sus cuatro líderes son `SIS`; en `M` y en `U` cae la cláusula literal «NO APLICA mientras el objetivo explícito sea construir o migrar el propio kernel/runtime». **Ninguno necesita excepción del Owner ni agruparse en menos items** | **`D67`** en la composición de los cuatro macrocircuitos | `M-7`, MEDIO: `a.7` FRENO 3 detiene el tercer item `SIS` consecutivo si hay producto listo, los cuatro macrocircuitos componen más de dos items y son mayoritariamente `SIS`, y §8 no decía ni cuántos ni cómo. El tercer item de `N` se habría detenido sin que nadie hubiera previsto por qué. La alternativa —pedir excepción al Owner— le lleva una pregunta que la propia cláusula de `a.7` ya responde | no declararlo devuelve un freno que dispara donde nadie lo esperaba |
| D83 | **Los dos espacios de nombres colisionados se deshacen, con UNA prueba común.** `R<n>` estaba dos veces —los ocho requisitos de §2.1 y las nueve ventanas de reconciliación—: las ventanas, **retiradas por `D64`**, pasan a `RC-1`–`RC-9`, y dejan de contarse entre lo escrito y no ejecutado, donde §19 las inflaba. `N<n>` estaba **tres** veces —los catorce principios de `C6`, los cinco niveles de la escala de novedad y las ocho fases de instalación—: se renombran **las fases**, `INS-0`…`INS-7`, por ser el espacio más nuevo y el único que esta fase puede renombrar sin tocar norma ni kernel | **`D64`** en el inventario de §19 y §2.9, y `D67` en la nomenclatura de §8.1 | `M-8` ≡ `A11` y `F-03`: un lector que encontrara `R1` o `N4` no podía saber a cuál se refería, y §19 contaba como pendientes nueve ventanas que ya no existen. La alternativa —renombrar `C6` o la escala de novedad— toca un contrato y kernel canónico anterior | volver a `N0`–`N7` reintroduce la tercera colisión |
| D84 | **Lo que protege la rama canónica del control repo es el CAS de Git**, no «un único escritor». La actualización de referencia sólo avanza desde la revisión conocida y un `push` non-fast-forward se rechaza; **«un único escritor» es una regla LOCAL por worktree** (`R5`) y no dice nada de dos máquinas empujando a la vez | **`D65`** en su lista de protecciones | `A12`, MENOR: la lista de protecciones de la rama canónica mezclaba una garantía distribuida con una regla local, y con ella se justificaba no aplicar `G29`. La justificación es correcta; el argumento, no | volver a invocar «un único escritor» promete serialización entre máquinas que no se da |
| D85 | **Los tres recuentos del eje `fase` se recalculan tras `D64`: CINCO fases, SEIS estados del campo —con la ausencia—, SIETE filas de la tabla.** `D59` los fijó en seis, siete y ocho cuando el autómata tenía seis fases; `D64` lo dejó en cinco y los tres números se quedaron atrás. `D57` y `D59` conservan su texto | **`D59`**, en su proyección tras `D64` | `A6`, MEDIO: el mismo documento afirmaba «seis fases» en cuatro sedes y «CINCO fases» en otras tres. Un recuento que se calcula se mueve cuando cambia lo contado; éste no se había movido | volver a seis contradice el enum vigente |
| D86 | **`C5` se registra como REUTILIZADO CON EXCEPCIÓN NOMBRADA**, con la misma disciplina que `C6` y `C7`. En la tensión entre `C5` L36 —«todo handoff entre capacidades se declara con su forma»— y `circuitos/00-CIRCUITOS.md` L238 —«los declarados son los que hoy existen»— **manda `00-CIRCUITOS`**, por el mapa de fuente única del índice operativo, que asigna «entregas entre capacidades» a `circuitos/`. `C5` L36 se lee acotada a la FORMA | **nada anterior**: §15.7 simplemente no registraba la excepción | `F-05`, MENOR: §15.7 aplicó a `C6` y a `C7` la disciplina de nombrar su excepción y registrar su defecto, y a `C5` no — pese a tener una tensión del mismo tipo. Es la adjudicación del NIVEL 0 del gate, escrita donde corresponde. La alternativa —crear las instancias que faltan para que la lectura fuerte sea cierta— la desactiva `00-CIRCUITOS` L238 | sin registrarla, la asimetría entre los tres contratos queda sin explicar |

### `D87`–`D95` · las decisiones de la CORRECCIÓN DEL GATE DE CIERRE INDEPENDIENTE

El **GATE DE CIERRE INDEPENDIENTE** —dos revisores con contexto limpio, `G` y `H`, en
paralelo y sin verse, y un adjudicador `I` que recibió los dos dictámenes ya cerrados—
emitió **INSUFICIENTE PARA F5** por dos razones independientes: la cobertura no cumplió
—catorce fuentes obligatorias sin lectura sustantiva, el documento 15 entre ellas— y **diez
de las 43 filas resultaron FALLIDAS**. Su juicio se conserva íntegro e inmutable en
`docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md`. Estas decisiones son la corrección
de sus 28 hallazgos consolidados.

> **`D1`–`D86` conservan su texto, y `O1`–`O16` quedan intactas.** La única fila tocada es
> **`D67`**, que se **RESTAURA al texto exacto que tenía en `7e99388`**: la tanda anterior la
> reescribió en el mismo commit en que declaraba que `D16`–`D70` no se reescriben (`I-16`).
> La corrección que aquella reescritura llevaba **no se pierde**: vive en `D89`, que es una
> decisión revisora y no una edición del registro histórico.

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D87 | **`estado/cuarentena/<TX>/` queda RETIRADA de la arquitectura vigente.** La cuarentena temporal —cuando hace falta preservar contenido divergente antes de restaurar— vive en **`.ads/run/quarantine/<TX>/`**: OPERACIONAL, LOCAL, ignorada por Git y **NO canónica**. Se crea **ANTES de restaurar**, se **verifica POR HASH** contra lo registrado en el `conflicto`, y se **elimina SÓLO después del terminal, de su verificación y del commit del incidente**. **NO es fuente de verdad** —lo es la copia íntegra que el `conflicto` lleva en su cuerpo— y **NO se usa como garantía de reanudación distribuida**. Si el contenido no puede conservarse o no puede publicarse: **`SEG` BLOQUEA la publicación**, el **Owner PUEDE ACEPTAR EXPRESAMENTE la pérdida de la preimagen**, el incidente conserva **hash, clasificación, autoridad, motivo y alcance**, y **nunca se publica el contenido prohibido**. Se mantiene la limitación ya aceptada: perder la máquina durante una transacción abierta puede perder evidencia operacional no publicada | **`D79`** en el plano de la cuarentena del acto (i) del desenlace `4b`. `D79` **no se reescribe**: su acto de autoridad sigue siendo el mismo, y lo que cambia es dónde vive lo que preserva | `I-01`, GRAVE: `estado/cuarentena/` no tenía plano en §1.2 ni en §2.4, ni fila en §1.3, ni entrada en el árbol de §2.3, ni `.gitignore`, ni fila de reconstrucción en §2.9, ni ciclo, ni fila adversarial. Por el criterio vigente de §2.4 quedaba **durable y versionada**, y entonces el acto (i) **publicaba en `main` exactamente el material que existe para preservar cuando `SEG` prohíbe publicarlo**. Y §2.6.10 descarta la alternativa D porque «crea una tercera ubicación con su ciclo y su plano, que §2.4 no tiene» — objeción que se aplicaba palabra por palabra a la ruta nueva. La alternativa —darle plano propio bajo `estado/`— **crea la tercera fuente de verdad que `D50` eliminó**, y por eso se descarta | volver a `estado/cuarentena/` reintroduce una ubicación de estado sin plano, sin ciclo y sin prueba |
| D88 | **El marcador de `deriva` gana las CINCO piezas de disciplina del marcador de transacción.** `estado/deriva/<ID>.abierta` pasa a estar: clasificado como OPERACIONAL en §2.4, como **SEGUNDA excepción de ruta** junto a `estado/tx/`; listado en el árbol de §2.3; excluido de Git en positivo; con **fila de reconstrucción en §2.9** —desde `bloqueado_por_deriva(item)`—; y con **fila adversarial** (`X59`, `X60`). **Lo CREA el paso E de §2.6.9**, en el mismo acto que el evento, y **lo RETIRA la transacción cerrada que lo resuelve**. Sin identidad ni autoridad propias, y **NUNCA fuente de verdad**. Y **la NORMA de §2.6.8 pasa a consultar los DOS MARCADORES**, no a recorrer el diario | **`D78`**, que declaró el marcador e invocó una excepción de ruta que no lo cubría, y **`D64`** en la redacción del paso `2bis` | `I-02`, GRAVE: la excepción invocada nombraba **sólo** `estado/tx/`, luego por el criterio vigente el marcador **viajaba a Git**; un clon nuevo lo recibía y declaraba NO FIABLES rutas sin ningún mecanismo que le dijera si seguían sin reparar. **Un caché versionado que nadie regenera con sede declarada ES una segunda verdad**, y `I5` lo prohíbe. Y `A8` exigía literalmente «sujeto a la misma disciplina que el marcador»: el otro tiene cinco piezas y éste no tenía ninguna. Además **la regla que el lector ejecuta no había cambiado**: seguía mandando recorrer `estado/eventos/`, que es el coste con el que §2.2 descarta la alternativa C. La alternativa —rehacer la justificación del marcador en vez de completarlo— deja la asimetría escrita y sin explicar | quitarle cualquiera de las cinco piezas devuelve un caché versionado sin regenerador |
| D89 | **La capa B del validador semántico pierde las dos reglas que `D64` retiró, y el predicado tiene UNA sede que nadie redeclara.** (i) La TERMINALIDAD se reescribe sobre los DOS terminales: toda transacción cerrada tiene **exactamente uno**, `derivada` **o** `abandonada`. (ii) La regla «#observaciones = #intentos … y en la AGOTADA ese `+1` es el `conflicto` con `agotado: true`» **se retira**: era inconstruible. (iii) **§2.6.4 paso 1 deja de redeclarar** el predicado y REMITE. (iv) El censo de sedes se DERIVA: son **NUEVE** vigentes, con §2.6.5 y §2.6.11 dentro, §2.6.9 fuera y §3.6 —la capa evaluadora— incluida. Y (v) el registro recoge aquí, como decisión revisora, lo que la reescritura de `D67` llevaba: `A2`–`A7` es **`proceso:AUD`** con `INV` de obligatoria, y **propagar a las fuentes es `proceso:DEP`** — no «propagar y certificar», porque certificar es `proceso:SIS` | **`D71`** en su censo, **`D64`** en las reglas que retiró y no se retiraron de la capa B, y **`D67`** en su resumen de procesos —que `D75` ya había corregido en §18— | `I-03`, GRAVE, e `I-09`, MEDIO: la capa B es la sede que `D71` designa para EVALUAR `abierta(tx)`, y conservaba **la afirmación exacta que causó `A2`** —«exactamente un `derivada` por transacción cerrada»—: un validador construido de esa lista **habría rechazado toda transacción abandonada**, y habría intentado comprobar una regla que exige contar un campo que el esquema no tiene. Y el censo era falso en dos de sus siete entradas mientras su «ninguna lo redeclara» lo desmentía §2.6.4. La alternativa para (v) —volver a editar `D67`— es la que produjo `I-16`: se descarta | volver a partir la terminalidad sobre `derivada` reintroduce la causa de `A2` |
| D90 | **Quién ejecuta cada operación Git lo fija `C7`, y §8 lo CITA en vez de reescribirlo.** `PLT` **materializa la fuente** (`C7:82`) y **retira ramas abandonadas** (`C7:92`); **rama, worktree, commit, push y PR los solicita y los ejecuta LA CAPACIDAD CON CUSTODIA, ella misma** (`C7:83`–`C7:86`) —en §8 es `CON`, obligatoria por `cambio-construido` en `SIS`, `DEU` y `DEP`—; **`SEG` puede BLOQUEAR el push** ante secreto detectado (`C7:85`); **`ENT` ejecuta el merge y DECLARA LA CONVERGENCIA** (`C7:88`–`C7:89`); **CI verifica cada fuente**; y el **Owner conserva su autoridad donde `C7` la exige**. `PLT` **NO se convierte en participante de la ruta** por ejecutar la materialización. Y `PN-13` conserva **únicamente** el residuo real: la composición de `INS-5` y de `A9` | **`D74`**, en el dispositivo `EJECUTOR` con el que cerraba la mitad `PLT` del bloqueante `B-2` | `I-04`, GRAVE: §8.0 atribuía a `PLT` «cada source change —rama, commit, push, PR y CI POR FUENTE», y de las siete operaciones `C7` le da **DOS**. No era sólo divergencia con el contrato: F4 **se desmentía a sí misma** —§1.3 da el `integration-set` a `ENT` como autoridad y ejecutor, §7.2 escribe «`ENT` declara convergencia», §7.6 remite a `C7` «de las fuentes»— y la entrega «de `PLT` a `VER`» hacía viajar una convergencia que nunca fue suya. La fila existía en §8.3 y **esta cadena la generalizó a cinco sedes y la promovió a dispositivo de cierre de un BLOQUEANTE**. La alternativa —tocar `C7`— la prohíbe esta fase, y `PN-11`/`C8` van primero. **No hacía falta: `C7:80-92` ya decía quién** | volver a atribuir a `PLT` los source changes reabre la mitad `PLT` de `B-2` |
| D91 | **Abrir una `iniciativa` de campaña NO se da por implícito.** `C1` L118 fija que la autoridad de un rol es SIEMPRE subconjunto de la de su capacidad, y **ninguna de las quince fichas menciona `iniciativa` ni `campaña`**. Se registra la EXTENSIÓN DE FICHA para F6 en cada capacidad que pueda ser **líder de cobertura**, y **el conjunto se DERIVA de los `contrato-de-aspecto` (§5.7)** —la capacidad `lider` de cada aspecto, o la única responsable cuando hay una sola—, **no se escribe a mano** | **`D80`** y el remedio de `M-5`, que aplicó la regla de `C1` a `DSP` y no al abridor de campañas | `I-14`, MEDIO: `M-5` pedía las dos mitades —«nombrar el actor de `APERTURA` y de `CAMPAÑA`, y declarar si esa apertura cabe o no en la autoridad»—, y sólo se hizo la primera. La alternativa —escribir a mano la lista de capacidades líderes— crea la **segunda sede editable** que `I5` prohíbe, y queda desactualizada en cuanto un aspecto cambie de líder | dar la autoridad por implícita reproduce el defecto que `M-5` denunció |
| D92 | **`DOM` y `SEG` participan DOS veces, y la segunda se registra como contrato completo para F6.** Donde un proceso activa `<CAP>:condiciones` **antes de `CON`**, existe también **`<CAP>:revision` después de `VER`**, que revisa lo construido. Se aplica **a TODOS los procesos donde esos condicionales existen**, no sólo a `DEU` y a `DEP`, y el conjunto se DERIVA con un barrido de `:condiciones`. **F4 NO modifica `01-PROCESOS.md`**: §19 declara la edición exacta, su propietario (`SIS`), su fase (F6) y su prueba —una comprobación que exija el par para cada `:condiciones`—, y el `GATE DE COMPOSICIÓN` de §8.0 pasa a comprobar contra `b.16` | **nada anterior**: es un hueco que ningún revisor había registrado hasta el gate de cierre | `I-08`, GRAVE: `b.16` L834–836 y `a.6` L502–503 lo dicen dos veces —la cita decía **L504–505**, dos líneas más abajo, y era falsa **en origen**: (a) no se ha modificado desde antes de `D92`. Corregido por `Q-34` del documento 22; `D98` ya citaba bien—, y un barrido sobre `kernel/operativo/` devuelve **cero instancias** de `:revision`. Los tres tramos donde falta —`A8`, `M6`–`M7` y `U5b`— son **los tres que escriben en las fuentes del producto**. **NO es decisión nueva del Owner y NO se registra como presión**: `b.16` ya lo exige; lo que falta es instanciarlo en el kernel derivado, que es F6 | no registrarlo devuelve un gate de composición que da por completa una ruta a la que le falta una participación que (b) exige |
| D93 | **`F-01` se RECLASIFICA de externo de F6 a presión lista para F5, y nace `PN-14`.** La formulación `DIS/Reconstruccion` aparece también en material APROBADO —`b.16` L895, proceso `AUD`, y `a.6` L495, composición ilustrativa—, que §17 declara intocable por F4 **y por F6**. La presión pide sustituir, en los puntos aprobados, `DIS/Reconstruccion` por la capacidad **`DIS`** con **`C-DIS`**, y declarar que **el método concreto lo calcula la escala de novedad**; después, **F6** actualiza `01-PROCESOS.md` y `00-CIRCUITOS.md`. `F-01` queda `PRESION_LISTA_PARA_F5` con `requiere_f5: sí` y `requiere_f6: sí`. **Aquí no se redacta ninguna enmienda** | **`D67`** en la sede del remedio de `F-01`, y §19 en su clasificación | `F-01` FALLIDA en el gate de cierre: la sede nombraba `01-PROCESOS.md` y `00-CIRCUITOS.md` y **omitía (a) y (b)**. Ejecutado tal como estaba escrito, el kernel diría `DIS` y su fuente normativa seguiría diciendo `DIS/Reconstrucción`: se cambia el derivado y se deja la fuente, que es el modo de fallo que §15.7 registra para `C7` — y la verificación mecánica «contra la fuente» que el checkpoint invoca como motivo **seguiría fallando**. La alternativa —declarar que `DIS/Reconstruccion` y `DIS` designan al mismo participante— es legítima y más barata, y queda escrita como **condición de reversión** de `PN-14`: elegir es del Owner | tratarlo como externo de F6 deja un remedio que no alcanza su fin declarado |
| D94 | **Las condicionales de `§5.18` son TRECE, y el recuento se DERIVA.** Contadas una a una sobre `ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` L788–790: UX e investigación · dirección visual · sistema de diseño · arquitectura de datos detallada · integraciones · cumplimiento regulatorio · modelo de amenazas avanzado · observabilidad · continuidad · analítica · dispositivos · internacionalización · gobierno de IA = **TRECE**. Las doce OBLIGATORIAS son las de L775–786, y **son las que reciben identificador** `aspecto:documental/<area>`; las trece condicionales **no lo reciben**, por el motivo que `D77` escribe y que no cambia | **`D68`** y **`D77`**, que dicen «CATORCE» en su texto. **Ninguna de las dos se reescribe**: son `D64`–`D86` y conservan sus palabras, como todo el registro | `I-15`, MEDIO: `M-1` es exactamente el hallazgo «catorce frente a trece», y su condición de cierre era «TRECE en las tres sedes». Las tres sedes del documento 11 se corrigieron —§4.3 L4320, L4353 y su tabla— y **la cuarta, escrita de cero en la misma tanda, reintrodujo la cifra defectuosa** en el registro que es la fuente de trazabilidad. No es editorial: es un **recuento**, y un recuento que se declara derivado se deriva. La alternativa —editar `D68` y `D77`— es la que produjo `I-16`, y se descarta | volver a CATORCE reintroduce el hallazgo que `M-1` cerró |
| D95 | **La regla 1 de §2.6.10 usa «los CINCO CAMPOS de procedencia» de §3.6**, no «los cinco conceptos de `a.9`». Los cinco campos son `ordenante` · `autoridad` · `escritor_del_comando` · `ejecutor` · `actor_atribuido`; el quinto CONCEPTO de `a.9` es el **propietario del campo**, que **se DERIVA** de §1.3 y no se persiste, y `actor_atribuido` pertenece a **otra** lista de `a.9`. Es `D66` propagado a la sede que le faltaba | **`D66`**, en su propagación. `D66` decidió bien y no se reescribe: lo que faltaba era llevarlo a la sexta sede | `A7`, MEDIO, **FALLIDA en el gate de cierre**: la tercera revisión nombró «`X39` y la regla 1 de §2.6.10» como los dos sitios que convierten la cita falsa en condición de validación, y «uno se corrigió; el otro no». El texto era **byte a byte idéntico al base**, y la línea siguiente dice «la ausencia de cualquiera de los cinco es un FALLO DEL VALIDADOR» — es decir, **es** una condición de validación, que es el sentido literal de su condición de cierre. El documento sabía escribirlo bien: lo hacía en las otras cinco sedes. La alternativa —declarar que `evento` lleva `actor_atribuido` ADEMÁS de los cinco conceptos— es la que `D66` ya descartó por crear una segunda sede editable de lo que §1.3 fija | volver a llamarlos «los cinco conceptos de `a.9`» reintroduce una cita que su fuente no respalda |

> **El espacio de nombres `INS-0`…`INS-7`, y su excepción histórica declarada (`I-12`).** La
> proyección **NORMATIVA VIGENTE** de las fases de instalación es **`INS-0`…`INS-7`**, y su
> sede es §8.1 y la tabla de §18. `D83` la fijó, y la prueba que declara —«ningún
> identificador `<PREFIJO><n>` se usa con dos significados distintos»— se comprueba **sobre
> el corpus vigente**, no sobre el registro de decisiones.
>
> **`D32`, `D67`, `D76` y `D82` conservan `N<n>` en su texto, y es deliberado.** El registro
> es historia: dice qué se decidió y con qué palabras se decidió, y `D16`–`D86` no se
> reescriben — que es exactamente la disciplina que `I-16` demostró rota y que `D87`–`D93`
> restauran. Reescribirlos para uniformar la nomenclatura destruiría la trazabilidad que este
> fichero existe para dar, y sería el mismo gesto que produjo `I-16`.
>
> **La regla, en una frase, y es la misma que `X47` aplica al enum de `fase`:** la proyección
> normativa vigente es UNA —`INS-0`…`INS-7`—, y las citas históricas son MUCHAS y están
> marcadas como tales. Lo que la prueba de `D83` comprueba es la primera. `C6` `N1`–`N14` y
> la escala de novedad `N0`–`N4` siguen intactos y siguen siendo los suyos.

---

### `D96`–`D102` · las decisiones de la CORRECCIÓN DEL GATE DEFINITIVO INDEPENDIENTE

El **GATE DEFINITIVO INDEPENDIENTE** —dos revisores con contexto limpio, `J` y `K`, en
paralelo y sin verse, y un adjudicador `L` que recibió los dos dictámenes ya cerrados—
emitió **INSUFICIENTE PARA F5** por **seis** razones independientes: cobertura incompleta
—~8 700 líneas de fuentes centrales que ningún revisor abrió—, un BLOQUEANTE arquitectónico
(`J-01`), **SEIS** GRAVES abiertos, un contrato F6 que aún exigía decidir arquitectura
(`K-02`), una contradicción con `G20`–`G23` sin presión F5 (`K-06`) y un checkpoint no
vigente. `L` verificó cada afirmación material contra su fichero y su línea, **sin resolver
por mayoría**, y **rechazó** `J-09`, la base externa de `K-03` y su propio agravamiento de
`K-11`. Su juicio se conserva íntegro e inmutable en
`docs/evolucion/19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md`. Estas decisiones son la corrección
de sus **24 hallazgos consolidados** —25 planteados menos `J-09`, rechazado—, derivados fila
a fila de la adjudicación y no de ningún total escrito a mano.

> **`D1`–`D95` conservan su texto ÍNTEGRO, y `O1`–`O16` quedan intactas.** Esta tanda **no
> toca ni una fila preexistente del registro**. A `O16` se le AÑADE su procedencia —que es lo
> que `L-02` exigía— **sin modificar su texto resolutivo ni crear una `O17`**: registrar de
> dónde viene una resolución no es reescribirla.

> **Y una parte de `C-L.7` se dejó SIN CORREGIR deliberadamente durante el gate**, y consta:
> `K-01`, `J-10` y `L-01` caen sobre el propio checkpoint, que estaba entre los ficheros que
> el gate podía tocar. Sus recuentos caducados se dejaron intactos y se escribió por qué —
> corregirlos durante el gate habría vuelto a hacer que quien recibe sea quien aplica. **Se
> corrigen ahora**, que es la tanda que corresponde.

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D96 | **`revision_base` es campo OBLIGATORIO de `preparada` en §3.6, se registra o referencia de forma comprobable en `conflicto` y en `abandonada`, y ENTRA en el cómputo de `tx` de §2.8.** Identifica la **revisión publicada y consistente** desde la que parte la transacción, y **NO es `base`**: `base` es la huella de las ENTRADAS sobre las que se decidió, `revision_base` es el PUNTO DEL HISTORIAL contra el que se restaura y se verifica byte a byte. Y con ello queda cerrada la colisión de identidad: la transacción original parte de la revisión ANTERIOR al incidente; el incidente cerrado SE PUBLICA, produciendo revisión nueva; la reparación parte de ESA revisión; luego su `revision_base`, y con él su `tx`, son **distintos**. La idempotencia de una misma intención sobre la MISMA base se conserva intacta | **`D69`**, en su propagación. `D69` introdujo `revision_base` y decidió bien; lo que faltaba era llevarlo a §3.6 y a §2.8. `D69` **no se reescribe** | `J-01`, **BLOQUEANTE**, y `J-02`, GRAVE. `revision_base` era condición 5 de arranque (§2.5), ancla exacta de la restauración (§2.6.9), lo que hace ALCANZABLE `abandonada` —«INALCANZABLE hasta haber RESTAURADO todas sus rutas a `revision_base` y haberlo verificado byte a byte»— y el sostén de «`main` nunca contiene estado parcial» y de la rama REVERTIR de `PN-7`. Y tenía **cero apariciones en §3.6** (L3589–4269): un esquema derivado literalmente de esa sección **aceptaba un `preparada` sin él**. Es la clase exacta de `A1` —que el gate final graduó BLOQUEANTE— invertida. **La alternativa descartada: introducir un nonce, un timestamp o cualquier aleatoriedad** para distinguir las dos transacciones. Se descarta porque destruiría la propiedad por la que `tx` se definió así — ser reproducible por dos implementaciones — y porque el dato que hacía falta **ya era necesario** por §2.5, §2.6.9 y §2.6.11: sólo faltaba declararlo | retirar `revision_base` de §3.6 devuelve un contrato de evento que no puede representar el dato del que dependen su segundo terminal y su garantía de no publicar mezclas parciales |
| D97 | **`PN-15`: `G20`, `G21`, `G22` y `G23` de `kernel/KERNEL.md` 1.5.0 quedan registradas como PRESIONADAS y pendientes de F5, NO derogadas por F4.** §17 gana una **fila propia para `kernel/KERNEL.md`** que lo declara, y la fila de `START_HERE.md` gana la reserva correspondiente. **Hasta que F5 decida regla a regla qué se conserva, ajusta o sustituye, las cuatro SIGUEN VIGENTES**, y §17 deja de poder leerse como si el Circuito 0 de §8.1 fuera una sustitución normativa ya consumada | **nada anterior.** No revisa ninguna decisión: registra una presión que faltaba. **No renumera ninguna `PN`** | `K-06`, GRAVE (agravado por `L` desde MEDIO, y una de las seis razones del veredicto). `G20`, `G21` y `G23` tienen **cero** apariciones en el documento 11, en (a), en (b) y en `E2`; `G22` tiene UNA, como cita de apoyo. **▲ ESTA FRASE DE EVIDENCIA ESTÁ ACOTADA, y sobre el documento 11 es FALSA hoy: ver el «ADDENDUM DE ALCANCE Y FECHA» inmediatamente debajo de esta tabla. La RESOLUCIÓN de `D97` no se toca y sigue siendo correcta.** `a.11` —«la ÚNICA lista que deroga o ajusta reglas», según `PN-3`— **no las nombra en ninguna de sus cinco filas**, y `E2.4` demuestra que **lo no nombrado sobrevive**. Mientras tanto §17 declara las rutas A y B de `START_HERE` «sustituidas por §8.1 y §8.2», y §8.1 define un gate distinto **sin timebox, sin los diez entregables y sin las cuatro prohibiciones** de `G22` — cuyo texto dice de sí mismo que **NO es negociable por el sistema**. **La alternativa descartada: decidir aquí qué reglas sobreviven.** Se descarta por dos motivos: `a.11` es material APROBADO y F4 no lo toca, y `G21` reserva expresamente esa decisión a la constitución **y no al sistema** — resolverlo F4 por su cuenta sería incurrir justo en el conflicto de interés que esa regla nombra | si el Owner decide que `G20`–`G23` se conservan intactas, §8.1 se subordina a `G22` y `INS-0`…`INS-7` pasa a instrumentar ese gate en vez de sustituirlo. No exige rediseñar §8 |
| D98 | **La regla que `D92` entrega a F6 se REFORMULA sobre PARTICIPACIÓN SEMÁNTICA, y el barrido léxico de `:condiciones` queda RETIRADO como criterio de derivación.** Si `DOM` o `SEG` participan en un proceso **por cualquier vía** —propietaria, obligatoria, condicional o item enlazado con `capacidad_productora` tipada— **y** su aportación establece condiciones o restricciones **antes de construir o antes de modificar fuentes**, ese proceso necesita su `<CAP>:revision` después de `VER`. La revisión **hereda la obligatoriedad y la `autoridad_de_retirada`** de la participación de la que deriva. §19 fija ahora datos de entrada, algoritmo de derivación paso a paso, salida esperada, casos positivos, contraejemplos, el error `composicion-incompleta` y la prueba que **tiene que fallar hoy** nombrando `proceso:DEP → SEG:revision AUSENTE` | **`D92`**, que decidió bien el QUÉ y mal el CÓMO. `D92` **no se reescribe**: su texto queda como lo escribió el gate de cierre, y lo que cambia es la regla de derivación que entregaba a F6 | `K-02`, GRAVE (agravado por `L`, y la cuarta razón del veredicto). El barrido de `:condiciones` es correcto en su cuenta —4 `DOM:condiciones` + 4 `SEG:condiciones`— **y no alcanza a `proceso:DEP`**, donde `SEG` participa por la OBLIGATORIA `condiciones-de-seguridad` (`capacidad_productora: "SEG"`, `autoridad_de_retirada: nadie` por `G28`), luego la cadena `SEG:condiciones` **no aparece en `DEP`**; ni a `proceso:AUD`, cuya notación no está tipada. Y **`U5b` ES `proceso:DEP`**, uno de los tres tramos que `D92` nombra como «los tres que escriben en las fuentes del producto»: **la regla no llegaba al tramo que ella misma señalaba**. La prueba prescrita reproducía el punto ciego — pasaría en verde sobre un árbol sin `SEG:revision` en `DEP`. **Y su causa es una corrección anterior:** `D75` cerró `G-1` moviendo `SEG` a obligatorias en `DEP`, eliminando sin verlo la cadena de la que `D92` dependería después. La norma aprobada está escrita sobre el HECHO y no sobre la notación: `a.6`:502–503, «DOM y SEG aportan condiciones antes de construir y revisan después». **La alternativa descartada: añadir `DEP` y `AUD` a mano a la lista del barrido.** Se descarta porque es exactamente el censo escrito a mano que `D102` retira, y porque dejaría el mismo agujero abierto para el siguiente proceso que participe por una vía nueva | volver al barrido léxico devuelve una regla que no alcanza el tramo más expuesto, y una prueba que pasa en verde sobre el árbol defectuoso |
| D99 | **El gate de `M7` exige las CINCO salidas verdes: build, pruebas, CI, despliegue y COMPORTAMIENTO AGENTIC.** Se alinean las tres sedes de §8.3 —`EVIDENCIA`, `GATES` y `M7 VERIFICAR`— y se escribe por qué la quinta no es optativa | **nada anterior en el registro.** Alinea §8.3 consigo misma | `K-03`, GRAVE. Contradicción **interna** del documento 11, verificada en cuatro sedes: §8.2 L6186 dice cinco, `EVIDENCIA` decía cuatro, `GATES` decía «las cuatro salidas verdes» y `M7 VERIFICAR` decía «los cinco». **`M6` es el único paso destructivo** y retira de cada fuente el kernel, los packs y la organización de ADS: build, pruebas, CI y despliegue pasarían **igualmente** en una fuente a la que le han quitado su organización ADS, luego **la única de las cinco que interroga precisamente lo que `M6` retira era la que el gate omitía**. `L` **corrigió la base que `K` le dio**: `K` la anclaba en «la directiva del Owner, `ADS-PENDIENTES` §5.6», y ese documento se autodeclara «no es todavía especificación normativa» (L3–L6). El hallazgo sobrevive entero como contradicción interna; **no** activa la regla de contradicción contra fuente normativa, y así se registra. **La alternativa descartada: bajar las otras dos sedes a cuatro.** Se descarta porque dejaría el único paso destructivo con un gate que no cubre su propio riesgo | volver a cuatro reabre el hallazgo en su forma exacta |
| D100 | **El `hash_previo` de la transacción de reparación es el `hash_observado` que el evento `deriva` registró, para las TRES causas del enum** —`posterior-al-cierre`, `sin-transaccion` y `abandono-de-transaccion`—, sin excepción. Y **el ancla de la restauración NO es `hash_previo`: es `revision_base`**, que es un dato distinto y lleva nombre distinto | **nada anterior.** Unifica dos formulaciones que convivían en §2.6.9 y §2.6.11 | `J-04`, MEDIO. §2.6.9 decía «`hash_previo` = lo que hay en la base restaurada» y §2.6.11 «= el `hash_observado` que la deriva registró». **Coinciden sólo para `abandono-de-transaccion`**: para `sin-transaccion` y `posterior-al-cierre` **no hay base restaurada**, y divergen. La formulación general correcta es la de §2.6.11. Cae dentro de §2, que es lo que `PN-1` propone aprobar como sección (g). **La alternativa descartada: conservar las dos y decir que se eligen por causa.** Se descarta porque usar el mismo nombre para dos conceptos es precisamente lo que produjo la ambigüedad, y porque el segundo concepto **ya tiene nombre propio** desde `D96` | volver a dos formulaciones deja el contrato de la reparación sin definiendum único para dos de sus tres causas |
| D101 | **§6.7 recibe FILA ADVERSARIAL PROPIA, `X62`**, y deja de reasignar su comprobación a `X51`. Cubre que la adopción **no escriba en ninguna fuente antes de `A8`, incluidos los punteros de adaptador**, más la propagación a tres fuentes con `main` protegida y el caso de fusionar dos de tres. El recuento de la tabla pasa a **cuarenta y seis filas y cuarenta y seis identificadores**, derivado y propagado a las seis sedes que lo publican | **nada anterior.** `X51` conserva su escenario intacto | `J-03`, MEDIO. `X51` es «editar un canónico fuera del protocolo, sin transacción abierta, y arrancar → se declara deriva no transaccional», y no tiene nada que ver con las tres comprobaciones de §6.7. `M2` había señalado que `X32`–`X34` se citaban y **no existían**, y el remedio de entonces las reasignó a una fila **existente pero ajena** — que es peor que la referencia rota, porque pasa desapercibida. **Se elige fila propia (salida A) y NO contrato de prueba F6 (salida B)** porque el escenario se expresa entero con el contrato de hoy —`git status`, `git log` y la ausencia de puntero sobre tres fuentes— y **no exige ningún runtime que no exija ya cualquier otra de las cuarenta y seis** | retirar `X62` devuelve §6.7 a una comprobación que su fila no cubre |
| D102 | **Los censos escritos a mano se DERIVAN, y queda el contrato F6 completo para hacerlo.** Tres contratos con entradas, algoritmo, salida, propietario, fase, condición de cierre y pruebas positiva y negativa: (1) derivar el censo `AFIRMACIONES` de `comprobar_recuentos.py`, que hoy es una lista literal de sedes; (2) ampliar `T152` a **toda sede que publique versión**, descubierta por barrido y no enumerada, con **remedios distintos por sede** —F6 para el kernel derivado, F5 para el título de `a.11` que es material aprobado, y **nota sin reescritura** para `O2`, que es del Owner—; (3) la **guardia de versión de intérprete** en el punto de entrada del runner y en los tres validadores que importan `tomllib`, con exit code **2** reservado a «no se pudo ejecutar». **Ocho defectos quedan como casos de regresión obligatorios**: `J-05`, `J-06`, `J-07`, `K-01`, `K-04`, `K-07`, `K-10` y `K-11`. **Aquí no se implementa ninguno de los tres** | **nada anterior.** Es el registro de una causa raíz que doce hallazgos comparten | `J-05` + `J-06` + `K-07`, y detrás de ellos `J-07`, `K-01`, `K-04`, `K-10`, `K-11` y `L-01`. Los tres revisores, **sin verse**, aislaron la misma causa desde mitades opuestas del corpus, y `L` la contó: `A6`, `A10`, `M-1`, `m-1`, `F-10`, `E-10` y los suyos son la misma clase, repetida. `T151` sale SUPERADA mientras dos sedes vivas dicen «veintiocho campos» donde `rol.yaml` tiene 29; `T152` sale SUPERADA porque **sólo recorre `README.md` y `START_HERE.md`**. Es lo que el propio corpus condena en `comprobar_fuentes.py`: «nunca una lista escrita a mano, que es lo que envejece» — **y no se lo había aplicado a sí mismo**. Y sobre la guardia, dicho sin rodeos: **evidencia verde generada bajo 3.11 NO demuestra que el runner sea ejecutable bajo 3.10** — bajo 3.10.12 da 10/13 con exit 1, y los tres validadores que fallan dejan intacta la evidencia anterior, por lo que `T158` sale SUPERADA **en un entorno donde nada se reprodujo**. **La alternativa descartada: añadir a mano las sedes que faltan a `AFIRMACIONES` y a `T152`.** Se descarta porque cierra ocho hallazgos y deja abierta la causa que los produjo: la sede número nueve nacerá sin cobertura, igual que las ocho anteriores | volver a censos enumerados devuelve la clase de defecto que doce tandas han producido |

> **ADDENDUM DE ALCANCE Y FECHA, registrado por `P-05` del documento 22. No reescribe `D97`,
> no retira la fila y no toca su RESOLUCIÓN, que sigue siendo correcta.**
>
> El adjudicador `R` dictaminó expresamente, y con esas palabras, que la frase de evidencia de
> arriba **no funciona como registro histórico suficientemente identificado, sino como
> CONTRADICCIÓN VIGENTE**: está escrita en presente, no dice de qué material ni de qué fecha
> habla, y **el propio commit que la escribió la falsificó**. La misma frase sí se acotó en el
> documento 11; aquí se quedó intacta. Se acota ahora, con el remedio que este mismo fichero
> ya usó dos veces —`D94` y `D106`(iii)—:
>
> ```text
> QUÉ SIGUE SIENDO CIERTO, y es lo que `D97` decidió
>   `a.11` —la ÚNICA lista que deroga o ajusta reglas— NO nombra `G20`-`G23` en ninguna de
>   sus cinco filas, y `E2.4` demuestra que lo no nombrado SOBREVIVE. Verificado hoy.
>   Por tanto las cuatro SIGUEN VIGENTES y quedan PRESIONADAS, no derogadas. La resolución
>   de `D97` no se toca
>
> SOBRE QUÉ MATERIAL vale el barrido, y es lo que faltaba decir
>   sobre el material APROBADO, que es el único que puede derogarlas: (a), (b) y `E2`.
>   NO sobre el documento 11, que es material de F4 y no deroga nada
>
> LA CIFRA, DERIVADA Y CONTRASTADA — y sólo sobre el material que PUEDE derogar
>   (a)            G20 0 · G21 0 · G22 1 · G23 0
>   (b)            G20 0 · G21 0 · G22 0 · G23 0
>   `E2`           G20 0 · G21 0 · G22 0 · G23 0
>     estas tres NO son literales sueltos: `G-13` de la batería las RECALCULA fichero a
>     fichero en cada ejecución —`\bG2[0-3]\b` sobre (a), (b) y `E2`— y las contrasta
>     contra el barrido que §16·`PN-15` del documento 11 publica. Si el árbol se mueve,
>     la batería enrojece. Se comprueban a mano con
>       for f in docs/rediseno/a-CAPACIDADES-APROBADA.md \
>                docs/rediseno/b-RECORRIDO-APROBADA.md \
>                docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md; do
>         for g in G20 G21 G22 G23; do printf '%s %s ' "$g" "$(grep -cw $g $f)"; done
>         echo "  <- $f"
>       done
>
>   documento 11   RETIRADA. Aquí NO va ninguna cifra, y es deliberado
>     [ESTADO ANTERIOR · esta línea publicaba `G20 12 · G21 10 · G22 16 · G23 13` bajo el
>      rótulo «DERIVADA HOY». Eran ciertas en el commit que las escribió, `78ec1cc`, y
>      CADUCARON en el commit siguiente —`609863e`, el mismo día— cuando la propagación de
>      `O17` amplió el documento 11. **Nada las derivaba y nada las contrastaba:** `G-13`
>      deja el documento 11 fuera a propósito, porque sus apariciones son documentales y
>      contarlas no prueba nada sobre la derogación. Es `S-06`≡`S3-03` del documento 23.]
>     La cifra viva, si alguien la necesita, se DERIVA en el acto y no se copia aquí:
>       for g in G20 G21 G22 G23; do \
>         echo "$g $(grep -cw $g docs/evolucion/11-ARQUITECTURA-INTEGRADA.md)"; done
>     Y la sede primaria ya hizo lo correcto y este addendum lo deshizo: `PN-15` del
>     documento 11 escribe «el documento 11 las nombra **muchas veces**», sin número y
>     deliberadamente, para que no envejezca. **Se vuelve a esa disciplina: poner otro
>     número a mano es exactamente el defecto que este addendum existía para cerrar.**
>
> POR QUÉ NO SE REESCRIBE LA FILA
>   porque el registro es historia y una decisión no se edita para que envejezca bien.
>   Se acota, se fecha y se deriva. Es lo que `D106`(iii) hizo con `O16`
> ```
>
> **Fecha de este addendum: 2026-08-30.** Su afirmación «su cifra se deriva del árbol
> en cada lectura» **era falsa cuando se escribió** —eran cuatro literales—, y se corrige
> aquí en vez de repetirse: de las cuatro cifras, las tres del material APROBADO las
> **recalcula `G-13` en cada ejecución de la batería**, y la del documento 11 queda
> **RETIRADA**. Lo que quede escrito a mano en este bloque se corrige retirándolo o
> dándole un contraste mecánico, **nunca sustituyendo un número por otro**.



> **Lo que esta tanda NO hizo, y consta.** No cerró `C-L.5` —la condición de cobertura del
> próximo gate—, porque aplicar correcciones no es leer lo que no se leyó y quien aplica no
> puede certificar su propia cobertura. No redactó ninguna enmienda normativa. No creó `C8`.
> No tocó `C7`, ni (a), ni (b), ni `E1`, ni `E2`, ni `K-1`, ni `C4`. No implementó runtime,
> adaptadores, migraciones, packs ni PesquerApp. Y **no emitió ningún juicio de suficiencia**:
> las correcciones están **APLICADAS, no certificadas**, `F4c` sigue **ABIERTA** y **F5 sigue
> NO autorizada**.

---

### `D103` · decisión de la CORRECCIÓN TÉCNICA sobre la derivación de `<CAP>:revision`

Corrección **estrictamente acotada** sobre la candidata publicada
`review/f4c-post-gate-candidate-20260829`. No es un gate, no es una revisión general y no
abre fase: corrige un defecto de la corrección anterior. **`D98` NO se reescribe**: su texto
queda como lo escribió la tanda del gate definitivo, y lo que cambia es la regla que
entregaba a F6.

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D103 | **La derivación de `<CAP>:revision` se hace SÓLO sobre campos ESTRUCTURADOS, y en DOS NIVELES que no se suman.** (i) **El segundo barrido léxico queda retirado**: la capacidad base se normaliza desde `condicionales[].capacidad`, `obligatorias[].capacidad_productora` y `propietario_global` resuelto para el item —tomando el segmento anterior a `:` y a `/`—, y **`capa_exigida` y `condicion` NO se analizan buscando palabras**. La norma de `a.6` y `b.16` se aplica a **toda participación efectiva** de `DOM` o `SEG`, sea cual sea su vía —propietaria, obligatoria, condicional o item enlazado—, y la revisión hereda **activación, obligatoriedad y `autoridad_de_retirada`** de la participación de origen. (ii) **NIVEL A · derivación estática del catálogo**: `FEA`, `GAP`, `INC`, `DEU` y `DEP` → **CINCO procesos y NUEVE pares**, incluido expresamente **`DEP → SEG`** por la obligatoria `condiciones-de-seguridad`. (iii) **NIVEL B · derivación por item**: `proceso:AUD` **no tiene cardinalidad estática**; por cada item se resuelve su propietario efectivo y se exige `DOM:revision` si es `DOM`, `SEG:revision` si es `SEG`, y **ninguna de las dos** si es cualquier otra capacidad. **Un item aporta CERO O UN par, nunca los dos**, y varios items `AUD` se evalúan independientemente. **`{DOM, SEG}` es el espacio de variantes, no un total simultáneo ni un décimo par fijo** | **`D98`**, en su algoritmo y en su cardinalidad. `D98` decidió bien el CRITERIO —participación por cualquier vía— y lo contradijo en su propio algoritmo. `D98` **no se reescribe** | Dos defectos, y el segundo es de la misma clase que el primero. **(1) El barrido léxico volvía por la puerta de atrás:** `D98` lo retiraba del criterio y el paso 3 de su algoritmo lo reintroducía, marcando una participación como condicionante si su `capa_exigida` o su `condicion` **contenía en texto libre** «ANTES de construir», o «aporta condiciones», o «propietaria de una conclusión que restringe». Es inferencia por cadenas: una redacción distinta la deja ciega, que es exactamente lo que `K-02` demostró que ocurre. **(2) La cardinalidad publicada era insatisfacible:** `D98` decía «**seis procesos, diez pares exigidos, diez ausentes**». Derivado de los campos estructurados, el catálogo da **cinco procesos y nueve pares**; el décimo salía de contar `proceso:AUD` como si aportara uno FIJO. No lo aporta: su `propietario_global` está declarado «DERIVADO del encargo» y `01-PROCESOS.md` L419 **prohíbe expresamente asignarlo a mano**, luego el par depende de quién resulte propietario del item concreto y puede no existir. Publicar diez obliga a que exista SIEMPRE un par de `AUD`, cuando lo correcto es que existan tantos como items `AUD` con propietario `DOM` o `SEG` haya — cero, uno o muchos. **Y `G-15` pasaba en verde sobre las dos cosas**, porque comprobaba la presencia de palabras en el documento y no ejecutaba la derivación. **La alternativa descartada: contar `AUD` como un par fijo y dejar el total en diez.** Se descarta porque mezcla un catálogo estático con una regla dinámica por item: ninguna de las dos lecturas resultantes es comprobable, y F6 tendría que **decidir** cuál vale — que es justo lo que `K-02` cerró | volver a inferir por texto libre devuelve la ceguera que `K-02` demostró; volver a un total de diez devuelve una cardinalidad que ningún árbol puede satisfacer |

> **Y `G-15` se corrige con ella.** Deja de buscar palabras y pasa a **ejecutar la
> derivación**: parsea los diez bloques `ads:proceso`, normaliza `DOM`/`SEG` desde los campos
> estructurados, deriva el conjunto estático **sin lista manual**, comprueba que la proyección
> publicada coincide con lo derivado, verifica que `(DEP, SEG)` está, verifica que `AUD` está
> declarado como regla **dinámica por item** y no incluido en un total estático, y corre
> **tres fixtures** —propietario `DOM` → `{DOM}`, propietario `SEG` → `{SEG}`, propietario
> `PRD` → `∅`—. **El nueve no está escrito en la prueba: se deriva y se compara con la cifra
> publicada.** La batería sigue teniendo **30 comprobaciones**: `G-15` se corrige en su sitio.

> **Qué NO hace esta corrección.** No toca `01-PROCESOS.md` ni ningún fichero del kernel. No
> implementa F6. No modifica `D98`, `PN-15`, `O16` ni los dictámenes de los documentos 15–19.
> No crea documento 20, no abre gate y no inicia F5, F6 ni PesquerApp. **Las correcciones
> siguen APLICADAS y NO certificadas**, `F4c` sigue **ABIERTA**, **F5 sigue NO autorizada** y
> **`C-L.5` sigue pendiente** del gate independiente que vendrá después.

---

### `D104`–`D106` · las decisiones de la CORRECCIÓN DEL GATE DE COBERTURA Y CIERRE

El **GATE INDEPENDIENTE DE COBERTURA Y CIERRE** —dos revisores con contexto limpio, `M` y `N`,
en paralelo y sin verse, y un adjudicador `O` que recibió los dos dictámenes ya cerrados—
emitió **INSUFICIENTE PARA F5** por seis razones, con **21 hallazgos consolidados y CERO
rechazados**: GRAVE 5 · MEDIO 6 · MENOR 10. Fue **la primera pasada que leyó íntegras las
cuatro fuentes que `C-L.5` nombra**, y las leyó por triplicado. Su juicio se conserva íntegro
e inmutable en `docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md`.

> **`D1`–`D103` conservan su texto ÍNTEGRO, y `O1`–`O16` quedan intactas.** Esta tanda no toca
> ni una fila preexistente. `O16` recibe un **addendum de cronología** —no una reescritura y no
> una cita nueva—, que es lo que `M-07` exigía.

> **Y lo que esta tanda NO puede hacer, dicho por delante: certificar.** Quien aplica estas
> correcciones es el mismo que escribió `D98` y `D103`, las dos que el gate acaba de declarar
> insuficientes. **Que `D104` alcance esta vez sólo lo puede decir un gate independiente.**

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D104 | **La derivación de `<CAP>:revision` se hace sobre CUATRO VÍAS TIPADAS y un discriminante ESTRUCTURAL, sin leer una sola palabra de texto libre.** (i) **Las cuatro vías**, determinadas por el CAMPO y la FORMA del valor: **1 · PROPIETARIA** (`propietario_global` resuelve a `DOM`/`SEG`), **2 · OBLIGATORIA** (`obligatorias[].capacidad_productora` desnuda), **3 · CONDICIONAL** (`condicionales[].capacidad` desnuda), **4 · ITEM PROPIO ENLAZADO TIPADO** (referencia `<CAP>:<aspecto>` o `<CAP>/<metodo>`). (ii) **Toda la inferencia que queda es UNA prueba de pertenencia**: se normaliza la base tomando el segmento anterior al primer `:` y al primer `/`, y se comprueba si pertenece al conjunto de las QUINCE, derivado de los directorios de `capacidades/`. **`capa_exigida`, `condicion`, `criterio_de_satisfaccion` y `autoridad_de_retirada` NO se leen.** (iii) **El discriminante estático/dinámico es estructural**: un proceso tiene propietario ESTÁTICO si y sólo si su `propietario_global` **es exactamente uno de los quince identificadores**, por igualdad de cadena contra un conjunto derivado del árbol. Derivado hoy: estáticos `FEA` `GAP` `INC` `INV` `DEU` `DEP` `SIS`; por item `DEF` `AUD` `DIR`, **los tres por la misma regla y sin excepción escrita para ninguno**. (iv) **El ANCLA DE POSICIÓN** es la obligatoria de `VER` si el proceso la declara, y su ÚLTIMA obligatoria si no: **ya no se exige `VER` donde no hay `VER`**. (v) **La regla por item suma DOS aportaciones**: el propietario efectivo (vía 1) **y** los condicionales de `DOM`/`SEG` que el item activa (vías 3 y 4). Para `proceso:AUD` eso significa que un item puede exigir `∅`, `{DOM}`, `{SEG}` **o `{DOM, SEG}`**. (vi) **La cifra estática no se escribe: se deriva**, y ejecutada hoy sigue dando **CINCO procesos y NUEVE pares**, con `(DEP, SEG)` por la vía 2 y los otros ocho por la vía 4 | **`D103`**, en su algoritmo, en su discriminante, en su ancla y en su regla por item. `D103` acertó al separar los dos niveles y al negarse a publicar un décimo par fijo, y eso se conserva. `D103` **no se reescribe** | **Cuatro defectos concurrentes del gate de cobertura, los cuatro reproducidos.** **`O-01`**: el criterio nombraba cuatro vías y el algoritmo derivaba dos — **la participación PROPIETARIA no estaba implementada en ningún nivel**, demostrado con fixture en verde. **`M-01`**: la **participación CONDICIONAL se perdía en `proceso:AUD`**, que declara `DOM` y `SEG` como condicionales —`b.16` L895, material APROBADO— y que `D98` había nombrado como hueco; el nivel A lo excluía entero y el nivel B sólo miraba el propietario. **`N-02`**: `propietario_global` es `{tipo: texto}` en `esquemas/proceso.yaml` L23 y en tres de los diez procesos contiene una frase — **el barrido léxico no se había retirado, había migrado de `capa_exigida` a `propietario_global`**, y la partición se decidía buscando la palabra «DERIVADO». **`N-01`**: el nivel B exigía la revisión «posterior a `VER`» en `AUD`, que **junto a `INV` es uno de los dos únicos procesos sin `VER`**, y excluía `DIR` —que sí lo tiene y también deriva su propietario— con una afirmación no derivable. **La alternativa descartada: parchear el discriminante añadiendo `DIR` y `DEF` a mano a la lista de dinámicos.** Se descarta porque es el censo enumerado que `D102` contrata para retirar, y porque dejaría el mismo agujero abierto para el proceso once | volver a un discriminante por palabra devuelve la ceguera que `K-02`, `D98` y `D103` produjeron tres veces; volver a exigir «tras `VER`» devuelve una prescripción imposible en `AUD` |
| D105 | **La referencia entre `abandonada` y su `deriva` se INVIERTE, y el cierre gana durabilidad paso a paso.** (i) **`deriva_emitida` queda PROHIBIDO en `abandonada`**; el `deriva` gana **`abandonada_id`**, obligatorio con `causa: abandono-de-transaccion` y prohibido con las otras dos. **El que llega después nombra al que ya existe**, y con eso `id(abandonada)` deja de depender de `id(deriva)`. (ii) **El paso E de §2.6.9 pasa a tener seis pasos ordenados y durables**: `abandonada` → `fsync` fichero y directorio → `deriva` → **`fsync` fichero y directorio, obligatorio y nuevo** → marcador del `deriva` → **y sólo entonces** retirada del marcador de transacción. (iii) **El commit sigue bloqueado hasta el paso 6**: mientras el marcador de transacción esté puesto, no se publica un cierre cuyo bloqueo no es durable. (iv) **El arranque COMPLETA el `deriva` ausente, de forma idempotente**: su cuerpo es una FUNCIÓN del `abandonada` durable, luego dos arranques emiten el mismo evento direccionado por contenido. El paso 0 de §2.6.4 sustituye su prohibición anterior por esta regla, **conservándola donde sí valía**: no se inventan derivas nuevas por arranque, se completa el que un `abandonada` durable ya exige. (v) **Nueva ventana `W17`** para la caída entre los dos, y el recuento de ventanas pasa a **DIECIOCHO, derivado de las filas**. (vi) **La justificación de exhaustividad se retira**: decía que la única escritura de un abandono era un evento del diario, y tras `D78`/`D88` son cinco efectos. (vii) **La capa B invierte el sentido de su regla 3**: recorre el diario buscando el `deriva` que apunta, en vez de seguir un puntero desde el `abandonada`. (viii) **La retirada del marcador deja de ser simétrica** entre los dos terminales, y `W8` lo dice | **`D69`**, **`D78`**, **`D79`** y **`D88`** en su propagación al paso E y a la lista de `fsync`. Ninguna se reescribe: las cuatro decidieron bien y lo que faltaba era llevarlas hasta aquí | **Tres hallazgos concurrentes, los tres reproducidos.** **`M-02`**: `id(abandonada)` incluía `deriva_emitida` = `id(deriva)`; el `deriva` se emite después, luego su `predecesor` es el `abandonada` y su `id` lo incluye. **Circular, y ninguna sede lo resolvía** — `grep` sobre «circularidad» devuelve seis líneas y ninguna toca ésta, mientras §2.8 declara del caso que sí cerró: «incluirlo es la circularidad que F4c no resolvía». **El segundo terminal del protocolo, y el único que revierte sin publicar mezcla parcial, NO SE PODÍA EMITIR.** **`M-03`**: el evento `deriva` no estaba en ninguna de las dos listas de `fsync` —ni entre los cuatro obligatorios ni entre los cuatro excusados—, el marcador de transacción se retiraba antes de que fuera durable, el paso 0 tenía PROHIBIDO reemitirlo, y ninguna de las diecisiete ventanas cubría la caída entre los dos eventos. **`O-03`**: y como la capa B exige que ese `deriva` exista, el resultado no era sólo bloqueo perdido en silencio, sino un `abandonada` durable con referencia colgante que **el propio validador declara defectuoso para siempre, sin ruta de reparación**. **Las tres alternativas se compararon en §2.6.9 antes de elegir**, y se descartaron dos: (A) que el `abandonada` conozca el `id` del `deriva` es el defecto mismo; (C) un evento de identidad previa compra lo mismo que (B) añadiendo un evento al camino crítico, una ventana más y una regla más — y `D64` ya retiró maquinaria por ese motivo exacto. **(B) es la mínima: no añade ningún evento, ningún tipo y ningún campo al `abandonada`; mueve una referencia de sitio y le da `fsync`** | volver a la referencia desde `abandonada` devuelve una identidad no construible; retirar el marcador antes del `fsync` del `deriva` devuelve el bloqueo perdido en silencio; volver a prohibir la emisión por arranque devuelve el diario irreparable |
| D106 | **Tres correcciones documentales que cambian lo que alguien tiene que hacer, y por eso son decisión y no erratas.** (i) **La PRUEBA POSTERIOR de `PN-15` deja de ser una disyunción.** Decía «una fila en `a.11` **o** una fila en §17», y afirmaba que pasar en verde hoy sería imposible — pero **la fila de §17 la escribió `D97` en el mismo commit que la presión**, con lo que la prueba pasaba en verde el día que nacía. La disyunción se retira: **la prueba exige una fila en `a.11`, que es material APROBADO y sólo F5 puede escribir**, y por tanto **sólo pasa cuando F5 haya tomado y materializado la decisión normativa real**. La fila de §17 registra la presión y **registrar no es resolver**. (ii) **`C-L.5` pasa a exigir DOS manifiestos publicados y no uno**: el de **ASIGNACIÓN**, emitido por el coordinador ANTES de repartir y con el revisor de cada fuente, y el de **LECTURA**, emitido por cada revisor DESPUÉS. La regla de cierre —«cualquier fuente ASIGNADA pero no leída impide la suficiencia»— se evalúa cruzando los dos, y **sin ellos el adjudicador debe declararla NO CERTIFICABLE**. (iii) **`O16` gana un ADDENDUM DE CRONOLOGÍA** que fija desde cuándo está respaldada: la formulación se registró el 2026-08-28, el Owner confirmó el 2026-08-29, y **sólo desde esa confirmación es resolución del Owner**. No se reescribe `O16`, no se inventa ninguna cita y no se retira la fila | **`D97`** en su prueba prescrita, y **`C-L.5`** en su evidencia exigible. Ninguna se reescribe: `D97` decidió bien la presión y falló en la prueba que le puso | **`M-05`**: la prueba de `PN-15` era satisfecha por la fila que su propia decisión añadía, y el cuerpo de la presión lo decía en pasado —«§17 **no tenía** fila»— mientras declaraba la prueba infalible. **Es una contradicción dentro de una sola decisión.** **`O-04`**: los tres revisores del gate declararon con honestidad qué leyeron y qué no, y **ninguno declaró qué se le había asignado**, con lo que su adjudicador no pudo certificar la cláusula más dura de `C-L.5` y tuvo que declararla no certificable. **`M-07`**: la fila `| O16 |` entró en el registro el 2026-08-28 y la procedencia fecha la consulta el 2026-08-29; ninguna sede reconciliaba las dos fechas, y `L-02` pedía atribuibilidad demostrable. **La alternativa descartada para (iii): fechar la procedencia el 28 para que cuadrara.** Se descarta porque sería inventar una confirmación que el Owner no dio ese día, que es exactamente el defecto que `L-02` señalaba | volver a la disyunción devuelve una prueba que se satisface sola; volver a un solo manifiesto devuelve una regla de cierre que su propio adjudicador no puede evaluar |

---

### `D107` · la propagación de `O17` — DERIVADA de una resolución del Owner, NO elegida por F4

**Esta decisión NO pertenece a la tanda de arriba, y por eso deja de estar archivada en ella.**
`D104`–`D106` cierran el **GATE INDEPENDIENTE DE COBERTURA Y CIERRE** —documento 20, revisores
`M` y `N`, adjudicador `O`, 21 hallazgos—. `D107` viene de otra pasada y de otro origen:
materializa **`O17`**, la resolución que el Owner dictó el **2026-08-30** respondiendo a la
ÚNICA clase `B` del **GATE INDEPENDIENTE DE CERTIFICACIÓN** —documento 22, adjudicador `R`, 69
hallazgos—, y está registrada en §2 de este mismo fichero.

> **La fila estaba como ÚLTIMA de la tabla de `D104`–`D106`**, bajo un epígrafe que no la
> nombra y un preámbulo que describe otro gate, otro adjudicador, otro recuento y otra
> declaración de integridad —`D1`–`D103`, cuando lo que `D107` declara es `D1`–`D106`—. Quien
> buscara «qué decidió la tanda de `O17`» por los epígrafes no la encontraba. Es `S-19` del
> documento 23. **§15.8 del documento 11 ya le daba bloque propio; la sede histórica no.**
> **La fila se mueve ENTERA y VERBATIM, byte a byte: no se reescribe ni una letra de ella.**

> **`D1`–`D106` conservan su texto RESOLUTIVO y `O1`–`O17` quedan intactas: sólo reciben
> punteros, encabezados y notas de alcance.** **Y nada de esto lo eligió F4**: el Owner decide
> en `O17` y `D107` sólo propaga, declarándose DERIVADA. **Aplicar no es certificar**: quien
> propaga es quien recibió el documento 22, y **ningún hallazgo se declara SUPERADO aquí**.

> **RECONCILIACIÓN DE ESTE PREÁMBULO CON LO QUE DE VERDAD SE HIZO — `V3-02`+`V3-03`
> fusionados y rebajados a MEDIO por el adjudicador `X` del documento 24. Se DECLARA, no se
> retira y no se reescribe ninguna decisión.** Este preámbulo decía «**conservan su texto
> ÍNTEGRO**», y **esa fórmula era falsa en el commit mismo que la escribió**. Lo que se hizo,
> commit a commit, verificado con `git blame` sobre este fichero:
>
> ```text
> celda de `D97`   commit `8c3afe7` «retirar las cifras que caducaron y remitir donde antes
>                  se copiaba» — EL MISMO COMMIT que escribió esta declaración. Recibe el
>                  marcador «▲ ESTA FRASE DE EVIDENCIA ESTÁ ACOTADA…», que es un PUNTERO al
>                  addendum que la acota. Remedio de `S-20` del documento 23
>
> celda de `D92`   commit `78ec1cc` «registrar O17 del Owner, su propagacion D107 y acotar
>                  D97» — corrige una CITA que era falsa EN ORIGEN (`a.6` L504-505 → L502-503)
>                  y añade una glosa. **El cambio va ANUNCIADO en el mensaje de su propio
>                  commit**: no hubo ocultación, y el adjudicador lo hace constar
> ```
>
> **Ninguna resolución se tocó.** Las dos ediciones son **un puntero y una corrección de
> cita**; el texto **resolutivo** de `D92` y de `D97` está intacto, comprobado con
> `git diff --word-diff` por el revisor `V`. La fórmula correcta —la que `00-INDICE` L87 y L88
> ya usaban en este mismo árbol— es «**conservan su texto RESOLUTIVO: sólo reciben punteros,
> encabezados y notas de alcance**», y es la que queda escrita arriba. **La declaración de
> integridad de este registro pasa a ser verdadera; el defecto no era un cambio oculto, sino
> una fórmula que decía más de lo que se cumplía.** Y consta, porque el adjudicador lo hace
> constar contra el propio interés de `F4`: **este defecto lo creó el remedio de `S-20`** —
> cerrar un hallazgo abrió otro, que es el patrón que tres gates llevan nombrando. **Ningún
> hallazgo se declara SUPERADO por esta reconciliación.**

| # | decisión | qué revisa | por qué, y qué alternativa se descartó | cómo se revierte |
|---|---|---|---|---|
| D107 | **PROPAGACIÓN DE `O17`. No es una elección de F4c: es la materialización de una resolución del Owner, y se declara DERIVADA.** Los cuatro macrocircuitos —instalación §8.1, adopción §8.2, migración §8.3 y actualización §8.4— ganan una **FASE 0 de CERTIFICACIÓN ESTRUCTURAL** como precondición propia, anterior a toda mutación canónica y a todo intento de elevarse. La fase invoca **un único contrato compartido**, `gate:sistema-conforme`, que deja de tener una sola aparición definitoria y pasa a tener **productor, sujeto, evidencia, vigencia y condición de invalidación**. `SIS` es propietario y productor; `VER` produce el dosier; `PLT` ejecuta la maquinaria cuando el contrato se la atribuya; `SEG` conserva su bloqueo. El **sujeto** lleva los seis identificadores de la regla 7 de `O17`, y su **huella** es lo que permite la reutilización de evidencia de la regla 8 —idéntica en todas sus entradas— sin que ninguna ejecución deje de emitir su propia declaración (reglas 9 y 10). La cadena de §9.2 se conserva íntegra y su regla dura deja de ser inaplicable | **`O17`**, que es su única fuente. No revisa ninguna decisión de F4c y **no renumera nada**: `D1`–`D106` y `O1`–`O16` intactas | **`P-06`** del documento 22, GRAVE nº 2, verificado por el adjudicador `R` barriendo §8.1, §8.2, §8.3 y §8.4: `gate:sistema-conforme` aparecía UNA vez en todo el documento 11, y era su definición. **La alternativa descartada NO la descartó F4**: la descartó el Owner, y son (a) y (c) de `O17`. Lo que F4 aporta aquí es **exclusivamente el reparto de la elección (b) por las sedes vigentes**, y por eso esta fila se declara derivada | revertir `O17` deja otra vez `O12` insatisfacible por cualquier recorrido, que es el estado que el gate del documento 22 declaró GRAVE |
| D108 | **PROPAGACIÓN DE `O18`. No es una elección de F4c: es la materialización de una resolución del Owner, y se declara DERIVADA. No sustituye a `O18`.** (i) **El SOBRE DE ANCLA** pasa a ser requisito de todo gate de `F4c`: el coordinador lo emite y lo entrega **a cada revisor dentro de su encargo, por un canal externo al repositorio, ANTES de que empiece a leer**, con repositorio, referencia remota de la candidata, SHA del commit, SHA del árbol, referencia del gate, commit del manifiesto previo, ruta y SHA-256 del manifiesto, SHA-256 del derivador, digest del universo derivado, número de fuentes y de asignaciones, fecha y hora, identidad del emisor, la mención de `O18` y la declaración de entrega previa. **No se obtiene leyendo el repositorio que se audita.** (ii) **Cada revisor**, antes de leer contenido semántico, transcribe literalmente el sobre, resuelve la referencia con `git ls-remote`, comprueba commit y árbol, recalcula el SHA-256 del manifiesto y del derivador, rederiva el universo, **compara todo contra el sobre, falla CERRADO ante cualquier diferencia** e incluye el resultado en su manifiesto de lectura. (iii) **El adjudicador** recibe los sobres que los revisores declaran, comprueba que sean idénticos, verifica los cálculos por su cuenta, **declara INVÁLIDO el gate ante cualquier diferencia**, y **no acepta ni un sobre reconstruido a posteriori desde el árbol ni un sobre cambiado después de crear revisores**. (iv) El sobre **NO sustituye** el manifiesto previo —que se sigue commiteando solo y antes de crear revisores—, ni los manifiestos de lectura, ni las dos restas, ni la revisión independiente, ni la adjudicación contra las fuentes: **es su raíz documental externa**. (v) Se registra el **CONTRATO DEL VERIFICADOR EXTERNO DEL CONTROL REPO** para `F6`, completo y sin implementar, con propietario, ejecutor, autoridad, fase, pruebas y condición de cierre | **`O18`**, que es su única fuente. No revisa ninguna decisión de F4c y **no renumera nada**: `D1`–`D107` y `O1`–`O17` intactas | la raíz que el segundo gate identificó y que **§11.4 del documento 11 ya había declarado**: la verificación se anclaba en referencias internas al árbol auditado. `U` reprodujo **seis árboles defectuosos en verde**, dos de ellos puertas nuevas, y midió que **el coste marginal de encontrar la siguiente no estaba subiendo**. **Las alternativas NO las descartó F4**: las ponderó el Owner, y son (a) —rechazada— y (c) —diferida a `F6` con condición dura—. Lo que F4 aporta aquí es **exclusivamente el reparto de la elección por las sedes vigentes** | retirar el sobre devuelve la verificación a una raíz que el propio árbol puede redefinir, que es el estado que tres gates consecutivos declararon insuficiente |

---

## 2 · Decisiones que pertenecen al Owner

**Ninguna bloquea el trabajo.** Todas tienen un valor por defecto ya implementado y
declarado; cambiarlas es una orden, no un rediseño.

| # | decisión | por defecto implementado | qué cambia si el Owner decide otra cosa |
|---|---|---|---|
| O1 | ~~¿`ENC` es capacidad propia o sigue siendo una función de `DSP`?~~ **RESUELTA** | El Owner la aprobó como decimoquinta capacidad base el 2026-08-26: [enmienda E1](a-ENMIENDA-E1-ENC.md). Materialización **bajo demanda**, no permanente. | nada: la decisión está tomada y enmendada en (a) |
| O2 | Convivencia de `KERNEL.md` 1.3.0 con el kernel operativo | conviven; 1.3.0 arranca proyectos, `operativo/` es lo que el runtime consumirá | reescribir `KERNEL.md` como índice delgado sobre `operativo/` es un item `SIS` que aún no existe |
| O3 | Umbral de anclaje y margen de ambigüedad de b.13 | `umbral 0.60` · `margen 0.15`, declarados en `entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md` §3, **como provisionales y calibrables por uso real** | son parámetros; cambiarlos no toca contratos |
| O4 | Presupuesto de exploración de Diseño | `DIS/Fundacion` sin techo de sesiones; `DIS/Evolucion` con exploración proporcional a la novedad, medida por la tabla de novedad | subir o bajar el número mínimo de direcciones exploradas |
| O5 | Quién puede levantar el veto de excelencia visual | sólo el Owner, y sólo tras ver las alternativas exploradas | delegarlo en `DIS/direccion-artistica` |
| O6 | Idioma de los artefactos operativos | castellano, como (a) y (b) | traducir es mecánico y no afecta a los identificadores |

### `O7`–`O14` · resueltas por el Owner el 2026-08-27, tras la crítica independiente de F3

A diferencia de `O1`–`O6`, éstas **no tenían valor por defecto implementado**: son las
preguntas que la síntesis de la iniciativa ADS NEXT elevó al Owner, y que su crítica
independiente reformuló. Fijan dirección para F4; **ninguna está construida**, y ninguna
enmienda (a), (b), `E1`, `E2` ni `K-1`.

> **Aquí no se enlaza esa iniciativa, y no es un descuido.** `docs/evolucion/` es historia
> del repositorio del kernel y **no viaja a un proyecto instalado**; este fichero sí. Un
> enlace a `09-SINTESIS.md` o a `10-CRITICA-INDEPENDIENTE-F3.md` quedaría roto en toda
> organización que instale ADS, que es el mismo motivo por el que `C6` no enlaza la decisión
> del Owner que lo originó y por el que las auditorías tampoco viajan. Quien lea esto dentro
> del repositorio del kernel los encuentra en `docs/evolucion/`.

| # | decisión | lo resuelto | qué cambia si el Owner decide otra cosa |
|---|---|---|---|
| O7 | ¿puede el sistema abrir trabajo de auditoría sin petición del Owner? | **política revocable de auditoría recurrente.** Detectar e inventariar es automático y **no crea trabajo**. Abrir auditorías se autoriza por evento, riesgo, recurrencia y caducidad **dentro de la política aprobada**. Las correcciones mecánicas y locales se ejecutan sólo en campañas y umbrales preautorizados, con pruebas y `VER` independiente. Producto, UX, arquitectura, seguridad, datos y comportamiento crítico **conservan sus gates y su autoridad**. Una única decisión declara alcance, prioridad, presupuesto, umbrales y revocación | revocar la política devuelve el sistema a proponer y esperar. `G03` no queda levantado en bloque: sólo lo que la política declara |
| O8 | ¿dónde cae el mínimo documental de un producto? | **las doce áreas semánticas del §5.18**, obligatorias como MATERIA y no como ficheros. Compactables físicamente, con profundidad proporcional a tamaño, naturaleza y riesgo. Las condicionales se activan por aplicabilidad, y «no aplicable» exige motivo registrado. Reanudación, decisiones seguras y gates son **comprobaciones** del mínimo, no su única razón | subir o bajar el número de áreas obligatorias, o su profundidad exigida por perfil de producto |
| O9 | ¿trae la distribución catálogo o equipo materializado? | **catálogo completo y estructura preconfigurada.** `C4` gobierna la materialización: `DSP` y `SIS` permanentes, `ENC` y las demás bajo demanda. No es una decisión nueva: es la lectura de `a.4`, `E1` y su contrato derivado `C4` que la síntesis no hizo | la regla vive en `a.4` —«DSP y SIS se materializan siempre»—, con `E1` confirmando que siguen siendo dos y que `ENC` no se añade. Cambiar `DSP`/`SIS` **presiona `a.4`** y exige enmienda normativa; hacer permanente a `ENC` **contradice `E1`** y exige enmendarlo. `C4` es contrato **derivado**: se actualiza después, y **no se enmienda**. Aquí no se propone ninguna enmienda |
| O10 | ¿dónde vive el material normativo en voz del Owner? | **`docs/owner/`** como destino canónico. La clasificación pasa a ser por **ubicación y metadata de autoridad**, en vez de una exención manual por fichero. El material temporal de evolución **no se retira todavía** | mover el directorio, o volver a la exención por fichero — que es lo que falló cinco veces |
| O11 | ¿cómo se llama la unidad amplia, y qué es? | **`iniciativa`.** Tipo o artefacto canónico de **coordinación**, con identidad, estado durable, alcance, gates y dosier vivo **derivado**. **No es un proceso nuevo**: compone rutas, items y paquetes existentes | elegir otro nombre es mecánico. Convertirla en proceso sí sería un rediseño, y contradiría `H1` |
| O12 | ¿qué certificación permite empezar a trabajar? | **Integrada + baseline aprobado + ningún desconocido crítico sin clasificar.** La certificación **Completa** es lo que permite declarar una instalación o adopción terminada y plenamente certificada | exigir Completa para empezar bloquearía todo producto sin runtime; exigir sólo Estructural dejaría entrar sin saber si el sistema arranca |
| O13 | ¿qué entornos agentic entran en la primera matriz? | **Claude Code y Codex** son el primer **objetivo** de soporte y certificación. **Hoy no hay ningún adaptador certificado**, y ninguno de los dos lo estará hasta superar una **prueba de humo real** en sesión nueva. **Cursor y Gemini** figuran desde el diseño en nivel compatible o genérico hasta superar la suya. **Fallback genérico obligatorio** para proveedores no certificados. **Ningún soporte se declara sin ejecución real: fijar el objetivo no es alcanzarlo** | añadir o quitar entornos de la matriz. Lo que no cambia es la regla: sin prueba de humo ejecutada, no hay nivel certificado |
| O14 | ¿qué producto se usa para el piloto? | **PesquerApp**, en clones y workspace aislados, **sin modificar ramas productivas**. Debe probar adopción multi-repo de un producto existente, `T169`, `T170`, `CA-10`, `CA-11`, el §100 y los límites de fan-out. **No se ejecuta todavía**: queda seleccionado, con sus condiciones escritas | elegir otro producto exigiría uno con historia real y varios repositorios. `gym-wear` sigue retirado como fuente contaminada, y esa retirada era para la minería, no para el piloto |

**Procedencia:** las ocho llegan de la revisión independiente de F3 y de la respuesta del
Owner a ella, el 2026-08-27. `O7` cierra `X6`, `O8` cierra `X7` y `O9` cierra `X8`; `O10`
cierra la ubicación de `P-07`, que era la parte que la síntesis había dejado al Owner.

### `O16` · resolución POSTERIOR del Owner — la sede del gobierno Git del control repo

La tercera revisión independiente devolvió `B2` —el gobierno Git del control repo no tiene
sede normativa—, y `PN-11` lo registró como presión. **El Owner resuelve dónde vivirá**, sin
reescribir `O1`–`O15` y sin autorizar todavía su redacción:

| # | decisión | qué precisa | qué cambia si el Owner decide otra cosa |
|---|---|---|---|
| O16 | El gobierno Git del **repositorio de control** tendrá su **autoridad normativa en la futura sección `(g)`**, y F6 derivará de ella un **contrato independiente `C8`** | `PN-11`, dándole sede | ampliar `C7` en su lugar choca con `E2.4`, que lo conserva **por source** por decisión del Owner |

```text
1  AUTORIDAD NORMATIVA      la sección `(g)`, que `PN-1` ya exige crear. **No se añade una
                            norma nueva**: se añade un apartado a una que ya hay que escribir

2  CONTRATO DERIVADO        `C8`, independiente, materializado en F6. Gobierna ÚNICAMENTE el
                            control repo

3  `C7` NO CAMBIA           sigue gobernando las SOURCES, y sigue sin tocarse

4  NO SE COPIA LA TABLA     `C8` no es `C7` con otro nombre: el sujeto es distinto —estado
   DE `C7`                  emitido por un ejecutor único, no código revisado— y hay que
                            aplicarle la prueba a ese sujeto, no heredar sus filas

5  QUIÉN HACE QUÉ           **F5 redacta la norma** en `(g)`; **F6 materializa y valida
                            `C8`**. Separar fuente normativa de contrato derivado es lo que
                            evita la duplicidad que `D51` ya corrigió una vez

6  QUÉ NO AUTORIZA          **no autoriza iniciar F5.** Fija la sede para cuando F5 arranque,
                            y nada más. `C8` NO se crea ahora y `C7` NO se modifica
```

**Procedencia** — registrada por la corrección del GATE DEFINITIVO INDEPENDIENTE (`L-02`,
GRAVE). `O16` era **la única de las dieciséis resoluciones del Owner sin fecha, sin cita y
sin entrada en `owner_captado`**, mientras el corpus demuestra exactamente eso para las
quince restantes y en el mismo fichero. Se registra ahora, y se registra **honestamente**:

```text
FECHA                    2026-08-29

QUÉ SE LE EXPLICÓ        se le presentó al Owner esta formulación, redactada por el sistema:
AL OWNER
                         «El gobierno Git del repositorio global de control de ADS tendrá su
                         autoridad normativa en la sección (g); F6 derivará de ella un
                         contrato independiente C8; C7 seguirá gobernando únicamente los
                         repositorios fuente del producto.»

RESPUESTA DEL OWNER      «ok, confirmamos»
— Y ESTO SÍ ES CITA
LITERAL SUYA

QUÉ RELACIÓN HAY         **el párrafo largo NO es cita del Owner: lo redactó el sistema y se
ENTRE LAS DOS COSAS      lo presentó para que decidiera.** Lo literal del Owner son esas dos
                         palabras, y lo que confirman es la formulación presentada. Se dice
                         así, y no al revés, porque atribuirle al Owner como cita textual un
                         párrafo que no escribió sería exactamente el defecto que `L-02`
                         señala — una resolución que el corpus no puede atribuir

QUÉ ALCANZA LA           la CONFIRMACIÓN alcanza a los tres extremos de la formulación
CONFIRMACIÓN             presentada: sede en (g) · `C8` derivado en F6 · `C7` intacto y
                         acotado a las fuentes. Los seis puntos desarrollados arriba son la
                         ELABORACIÓN de esos tres por el sistema, no seis decisiones
                         separadas del Owner

QUÉ NO ALCANZA           **no autoriza iniciar F5**, no autoriza redactar (g) y no autoriza
                         crear `C8`. Sigue diciendo lo mismo que decía
```

> **ADDENDUM DE CRONOLOGÍA, registrado por `M-07`. No reescribe `O16` y no añade ninguna
> cita.** El gate de cobertura derivó del historial que **la fila `| O16 |` entró en el
> registro el 2026-08-28**, en el commit `a713590`, y que **la procedencia de arriba se añadió
> el 2026-08-29**, en `d868bcb`, declarando esa misma fecha para la consulta al Owner. Las dos
> cosas son ciertas y ninguna sede las reconciliaba. Se reconcilian aquí, y sin inventar nada:
>
> ```text
> 2026-08-28   la FORMULACIÓN queda REGISTRADA en el registro de decisiones, redactada por
>              el sistema, como la sede que `PN-11` necesitaba. En ese momento **no estaba
>              confirmada por el Owner**, y el registro no lo decía
> 2026-08-29   el Owner responde **«ok, confirmamos»** a la formulación que se le presenta
>              — cita literal suya, la única de este bloque
> DESDE ESA    y **sólo desde esa confirmación**, `O16` queda respaldada como RESOLUCIÓN DEL
> CONFIRMACIÓN OWNER. Entre el 28 y el 29 fue una formulación registrada a la espera de
>              confirmación, y así consta ahora
> ```
>
> **Qué NO se hace, y por qué.** No se reescribe `O16` —es material del Owner y su texto
> resolutivo no se toca—, no se inventa una cita del 28 que nadie dijo, y no se retira la
> fila. Lo que faltaba era **decir desde cuándo está respaldada**, y `L-02` pedía
> exactamente atribuibilidad demostrable: la procedencia la da, y este addendum da su fecha
> de efecto.

> **Por qué esto cierra `L-02` y no lo maquilla.** El hallazgo no era que la decisión
> estuviera inventada: era que **el corpus no podía demostrar que el Owner la tomara**,
> mientras lo demostraba para las quince restantes. `O16` es lo que da sede a `PN-11`, que
> nació del BLOQUEANTE `B2` de la tercera revisión, y una resolución no atribuible no puede
> cerrar una presión de ese origen. Lo que faltaba era el registro, y es lo que se añade —
> **sin tocar el texto resolutivo de `O16` y sin crear una `O17`**: registrar de dónde viene
> una resolución no es reescribirla. La alternativa que `L` dejaba abierta —retirar `O16` y
> devolver `PN-11` a la lista de presiones sin sede— **no se toma**, porque la resolución
> existe y ahora es atribuible.

### `O15` · resolución POSTERIOR del Owner sobre `O14` — la adopción de PesquerApp es PERMANENTE

**`O14` no se reescribe.** Su texto queda arriba tal como el Owner lo resolvió el 2026-08-27,
y sigue siendo cierto en lo que dijo: el producto elegido, las condiciones de aislamiento y
que no se ejecuta todavía. Lo que `O15` fija es **lo que `O14` no decía**, y que la palabra
«piloto» dejaba abierto a la lectura contraria.

| # | decisión | qué revisa | lo resuelto |
|---|---|---|---|
| O15 | **PesquerApp será la PRIMERA ADOPCIÓN REAL, PERMANENTE y COMPLETA de ADS** | **`O14`**, que la llamaba «piloto» sin decir si el resultado se conserva | ver los nueve puntos de abajo |

```text
1  PRIMERA ADOPCIÓN REAL      no es un ensayo. Es la primera vez que ADS gobierna un
   PERMANENTE Y COMPLETA      producto de verdad, y el resultado SE QUEDA.

2  EL REPOSITORIO GLOBAL      el control repo ADS de PesquerApp nace como REPOSITORIO DE
   ADS NACE DEFINITIVO        CONTROL DEFINITIVO. No se crea para eliminarlo, reemplazarlo
                              ni rehacerlo después de una prueba.

3  QUÉ PROTEGEN LOS CLONES    los clones, ramas y worktrees aislados de `O14` protegen LAS
   Y WORKTREES AISLADOS       FUENTES y LAS RAMAS PRODUCTIVAS durante la adopción. Eso es
                              aislamiento del producto, y **no convierte el repositorio de
                              control ADS en desechable**. Son dos cosas distintas y `O14`
                              las dejaba juntas.

4  QUÉ TIENE QUE ESTAR        la BASE COMPLETA ACORDADA, no un MVP reducido. Antes de la
   ANTES                      adopción se implementa lo acordado, y lo que falte se dice
                              antes de empezar, no durante.

5  QUÉ SE COMPLETA            las garantías que SÓLO puedan demostrarse contra un producto
   DURANTE                    real se completan durante la adopción. Es lo que la columna de
                              uso real existe para llenar, y no hay otra vía.

6  CÓMO ENTRAN LOS            por MIGRACIONES y EVOLUCIÓN VERSIONADA sobre la instalación
   DEFECTOS Y MEJORAS         permanente. El recorrido de §8.3 y el de §8.4 son la vía; no
                              se rehace la instalación para incorporar un arreglo.

7  RECONSTRUIR O SUSTITUIR    exigiría una MIGRACIÓN EXPLÍCITA, AUTORIDAD y EVIDENCIA.
   EL REPOSITORIO DE          **Nunca será el procedimiento normal**, y ningún defecto
   CONTROL                    encontrado durante la adopción lo autoriza por sí solo.

8  QUÉ SIGNIFICA «PILOTO»     si el término se conserva —y se conserva en `O14`, en §14, en
   A PARTIR DE AQUÍ           §18 y en el checkpoint, porque no se reescribe historia—,
                              significa PRIMERA ADOPCIÓN REAL y CASO INICIAL DE
                              CERTIFICACIÓN. **No significa prueba provisional.**

9  QUÉ NO AUTORIZA ESTO       **NO autoriza iniciar la adopción.** `O15` fija qué será esa
                              adopción cuando ocurra; no la abre, no la programa y no
                              levanta ninguna de las condiciones que `O14` escribió ni
                              ninguna de las ocho presiones normativas vigentes.
```

**Qué cambia si el Owner decide otra cosa:** volver a una adopción desechable obliga a
declarar qué se hace con el estado producido —eventos, cobertura, certificación e historia—
cuando el repositorio de control se tira, y esa pregunta no tiene hoy respuesta escrita. Es
exactamente el vacío que `O15` cierra.

---

### `O17` · resolución del Owner sobre EL NIVEL ESTRUCTURAL Y SU PRODUCTOR — 2026-08-30

**Procedencia: respuesta expresa del Owner del 2026-08-30**, a la consulta que el GATE
INDEPENDIENTE DE CERTIFICACIÓN —documento 22— formuló como su única clase `B`. La pregunta y
sus tres alternativas están redactadas palabra por palabra en §13 de la adjudicación de `R`,
dentro de ese documento. **Nada de esto lo eligió F4.**

**El vacío que resuelve.** §9.2 encadena `estructural ◀── operativo ◀── integrado ◀── completo`
y fija una REGLA DURA: *un nivel no se declara por argumento ni por haber pasado el anterior*.
Pero `gate:sistema-conforme` tenía **una sola aparición en todo el documento 11, y era su
propia definición**: ninguna fase de ninguno de los cuatro macrocircuitos lo producía. Sin
celda de Estructural verificada y vigente, ni la Operativa ni la Integrada eran alcanzables, y
con ellas **`O12` no era satisfacible por ningún recorrido**. Es el GRAVE nº 2 del documento 22.

| # | decisión | qué revisa | lo resuelto |
|---|---|---|---|
| O17 | **EL NIVEL ESTRUCTURAL SE PRODUCE AL INICIO DE CADA MACROCIRCUITO, COMO PRECONDICIÓN PROPIA DE ESA EJECUCIÓN** | **nada anterior se reescribe.** Da productor al nivel que no lo tenía, y con ello hace **satisfacible `O12`**, que hasta hoy no lo era. `O1`–`O16` conservan íntegramente su texto | las tres alternativas comparadas, la elegida y su motivo, abajo |

**Las TRES alternativas que se le presentaron, y por qué se descarta cada descartada:**

```text
(a) QUE LO PRODUZCA LA INSTALACIÓN, como primer paso de `INS`, antes de cualquier otro nivel
    A FAVOR    la más barata y la que menos toca
    DESCARTADA porque un producto ya instalado NO revalidaría su Estructural cuando cambie
               el kernel: adopción, migración y actualización correrían sobre una estructura
               certificada en otro momento y quizá contra otra revisión

(b) QUE LO PRODUZCA CADA MACROCIRCUITO AL ARRANCAR, como precondición propia   ← ELEGIDA
    A FAVOR    la más segura, y hace `O12` satisfacible desde CUALQUIER entrada
    COSTE      añade un gate a los cuatro recorridos y encarece migración y actualización.
               **El Owner acepta expresamente ese coste**

(c) QUE DEJE DE SER UN NIVEL CERTIFICABLE y pase a precondición de arranque no certificada
    A FAVOR    la que menos maquinaria deja en pie
    DESCARTADA porque obliga a reescribir §9.2 y la definición de «nivel alcanzado», y
               **cambia el contenido de `O12`**, que es resolución del propio Owner
```

**MOTIVO DE LA ELECCIÓN, en las palabras del Owner:** *robustez y revalidación permanente por
encima del ahorro operativo*. «No elijo la alternativa barata de certificarlo sólo durante la
instalación. Quiero que instalación, adopción, migración y actualización comprueben la
estructura vigente antes de continuar. La prioridad es una base sólida y permanente, aunque
suponga más comprobaciones y consumo de recursos.»

> **NOTA DE TRAZABILIDAD SOBRE ESTE MOTIVO — `S-26` del documento 23. Se DECLARA, no
> se retira y no se sustituye.** Las tres alternativas de arriba **sí** son verbatim de
> §13 de la adjudicación de `R`, dentro del documento 22, y ahí se cotejan palabra por
> palabra. **La cita del motivo NO está en §13 y no puede estarlo**: §13 contiene la
> PREGUNTA, redactada antes de que hubiera respuesta. **De dónde viene:** de la respuesta
> expresa del Owner del **2026-08-30**, recogida al registrarla aquí. **Y no hay otra
> sede:** `grep -rn 'No elijo la alternativa barata' docs/ kernel/` devuelve **una sola
> línea, ésta**; el checkpoint y `00-INDICE` la parafrasean citándola de aquí y **no son
> sede independiente**. Por tanto: **no se afirma que sea falsa — se declara
> INVERIFICABLE**, porque ningún gate puede contrastarla contra nada. `O16` recibió un
> ADDENDUM DE CRONOLOGÍA por `M-07`/`L-02` exactamente para dar atribuibilidad
> demostrable; `O17` declara procedencia y fecha, y lo que le falta —trazabilidad de la
> respuesta— queda dicho aquí en vez de presumirse resuelto.

**Las DOCE reglas obligatorias que `O17` fija:**

```text
 1  cada ejecución de un macrocircuito produce EXACTAMENTE UNA certificación Estructural
    propia
 2  se produce ANTES de cualquier mutación canónica del macrocircuito y ANTES de intentar
    elevarse a Operativa, Integrada o Completa
 3  superar una ejecución anterior NO certifica automáticamente la actual
 4  un nivel superior NO implica por sí mismo que Estructural siga vigente
 5  si Estructural FALLA, el macrocircuito se BLOQUEA antes de mutar estado
 6  los cuatro macrocircuitos invocan EL MISMO CONTRATO y EL MISMO MECANISMO COMPARTIDO.
    No se crean cuatro implementaciones divergentes
 7  el SUJETO de la certificación identifica como mínimo: producto o instalación ·
    ejecución del macrocircuito · revisión del kernel · revisión de schemas y contratos
    aplicables · configuración y fuentes relevantes · huella de la evidencia
 8  puede REUTILIZARSE evidencia material anterior ÚNICAMENTE si se demuestra que todas sus
    entradas y huellas siguen IDÉNTICAS
 9  aun cuando la evidencia pueda reutilizarse, cada ejecución produce SU PROPIA declaración
    Estructural, vinculada a ESA ejecución
10  la reutilización NUNCA puede consistir en copiar una certificación anterior ni en
    presumirla vigente
11  la cadena queda:  Estructural → Operativa → Integrada → Completa
12  cada nivel conserva PRODUCTOR, EVIDENCIA, SUJETO, VIGENCIA y CONDICIÓN DE INVALIDACIÓN
    propios
```

**El REPARTO DE RESPONSABILIDADES que el Owner decide:**

```text
SIS   PROPIETARIO Y PRODUCTOR de la declaración Estructural
VER   produce el DOSIER o evidencia verificadora, SIN apropiarse de la decisión final
PLT   ejecuta la MAQUINARIA TÉCNICA cuando el contrato vigente le atribuya esa ejecución
SEG   conserva su capacidad de BLOQUEO cuando la estructura incumpla seguridad

EL PROPIETARIO DE CADA MACROCIRCUITO no puede sustituir a `SIS` en la certificación,
pero DEBE EXIGIRLA antes de continuar
```

**Qué NO autoriza `O17`.** **No autoriza iniciar `F5`**, ni `F6`, ni la adopción de PesquerApp.
No levanta ninguna de las condiciones `C-L` abiertas, no cierra `F4c` y no deroga ninguna
presión vigente. Fija QUÉ tiene que producirse y QUIÉN lo produce; **construirlo es trabajo de
las fases siguientes**, y su contrato queda escrito para que lo sea.

**Qué cambia si el Owner decide otra cosa:** volver a (a) reabre el hueco de revalidación —una
instalación vieja corriendo sobre un kernel nuevo—; ir a (c) obliga a reescribir §9.2 y a
redefinir `O12`, que es materia suya.


---

### `O18` · resolución del Owner sobre LA RAÍZ DE CONFIANZA DE LA VERIFICACIÓN — 2026-08-30

**Procedencia: respuesta expresa del Owner del 2026-08-30**, a la consulta que el SEGUNDO GATE
DE CERTIFICACIÓN —documento 23— formuló como su única clase `B`, y que **no era un hallazgo:
era la raíz** de las tres insuficiencias consecutivas. La pregunta y sus tres alternativas están
en §13 de la adjudicación de `U`, dentro de ese documento. **Nada de esto lo eligió F4.**

> **NOTA DE TRAZABILIDAD SOBRE ESTA RESOLUCIÓN — `X-02` del documento 24, GRAVE. Se
> DECLARA, no se retira y no se sustituye.** Las tres alternativas de abajo **sí** son
> verbatim de §13 de la adjudicación de `U`, dentro del documento 23, y ahí se cotejan
> palabra por palabra. **Lo que el Owner RESPONDIÓ no está en §13 y no puede estarlo**: §13
> contiene la PREGUNTA, redactada antes de que hubiera respuesta. **De dónde viene:** de la
> **respuesta expresa del Owner del 2026-08-30**, recogida al registrarla aquí — el rechazo
> literal de `(a)`, la adopción de `(b)` para cerrar `F4c` y la condición con que `(c)` queda
> obligada en `F6`. **Y no hay otra sede en el árbol donde viva esa respuesta en su propia
> mano:** `docs/owner/` contiene **DOS** documentos y **ninguna** de las resoluciones
> `O15`–`O18`; el checkpoint, `00-INDICE` y §11.8 del documento 11 la parafrasean citándola
> de aquí y **no son sede independiente**. Por tanto: **no se afirma que sea falsa — se
> declara INVERIFICABLE**, porque **ningún gate puede contrastarla contra nada**.
>
> `O17` recibió esta misma declaración como remedio de `S-26`, y el documento 23 la cerró
> «con honradez». **`O18` —la resolución que existe precisamente porque el corpus descubrió
> que no puede verificarse a sí mismo— no la llevaba**, y el TERCER GATE DE CERTIFICACIÓN lo
> registró como `X-02`: una regresión del remedio de `S-26` aplicada a la resolución
> siguiente. **Queda escrita aquí, y NO depende de lo que el Owner ratifique**: el
> adjudicador `X` resolvió expresamente que ésta es la única parte que `F4` sí puede hacer
> por sí misma, diga lo que diga el Owner. `O18`(b) ancla commit, árbol, manifiesto,
> derivador y universo, **y no ancla ninguna resolución del Owner** — eso es `X-03`, y es
> clase `B`.

**El vacío que resuelve.** La batería vive **dentro** del repositorio que audita y decide si algo
está «intacto» comparándolo contra referencias que **también viven ahí** —`HEAD`, la revisión
base, `kernel/.upstream-hash` y su propio README—. Quien puede escribir el repositorio puede
escribir la referencia, y puede amputar la batería. **El propio corpus lo había declarado en
§11.4 del documento 11** —«*si el runner miente, nada dentro del repositorio lo detecta*»— y lo
había dejado abierto; ningún gate lo había llevado al Owner.

| # | decisión | qué revisa | lo resuelto |
|---|---|---|---|
| O18 | **RESOLUCIÓN ESCALONADA: (b) ANCLA DOCUMENTAL EXTERNA PARA CERRAR `F4c`, Y (c) VERIFICADOR EXTERNO REAL COMO CONDICIÓN OBLIGATORIA DE `F6`. La alternativa (a) queda EXPRESAMENTE RECHAZADA** | **nada anterior se reescribe.** `O1`–`O17` conservan íntegramente su texto. Da raíz de confianza a un mecanismo que no la tenía, y fija la fase de cada garantía | las tres alternativas, el rechazo, la adopción, la obligación y la razón de secuenciación, abajo |

**Las TRES alternativas que se presentaron, conservadas literalmente:**

```text
(a) DECLARAR EL LÍMITE Y DEJAR DE MEDIRLO
    `M-04` deja de ser criterio de aceptación de `F4c` y pasa a limitación declarada con
    propietario y fase. La batería retira toda promesa de «intacto»
    A FAVOR    es gratis, es honesto, y desbloquea `F5` hoy
    EN CONTRA  el corpus queda sin ninguna defensa contra una alteración deliberada
    ── RECHAZADA EXPRESAMENTE POR EL OWNER ──────────────────────────────────────────────
    «No acepto retirar la garantía ni asumir como solución definitiva que una alteración
    deliberada sea indetectable.»

(b) DARLE UN ANCLA FUERA DEL ÁRBOL, DENTRO DE LO QUE F4 ALCANZA
    el ENCARGO de cada revisor le entrega el commit y las huellas por un canal que el
    repositorio no reescribe. El revisor verifica contra lo que RECIBIÓ, no contra el árbol
    A FAVOR    barato, documental, y cierra la mayor parte del ataque
    EN CONTRA  el ancla pasa a ser el Owner, y no hay forma mecánica de comprobarla
    ── ADOPTADA PARA CERRAR `F4c`, Y DECLARADA TRANSITORIA ──────────────────────────────

(c) UN VERIFICADOR EXTERNO DE VERDAD
    commits firmados, refs protegidas y ejecución de la batería fuera del repositorio, con
    identidad propia, cuyo resultado no se escribe en el árbol
    A FAVOR    es lo único que cierra la clase
    EN CONTRA  es infraestructura y credenciales, toca `C7`, y es trabajo de `F6`
    ── OBLIGATORIA EN `F6`, Y CONDICIÓN PREVIA A PesquerApp ─────────────────────────────
```

**LA RAZÓN DE SECUENCIACIÓN, y el bloqueo circular que evita.** Exigir que la infraestructura de
(c) exista antes de cerrar `F4c` produce una dependencia circular que el Owner declara
inaceptable:

```text
`F4c` bloquea `F5`  ·  `F5` precede a `F6`  ·  `F6` construiría el verificador
pero `F4c` permanecería abierta hasta que `F6` lo construyera
```

**Por tanto, y en este orden:** `F4c` puede certificarse mediante el ancla documental de (b);
la limitación residual **se declara expresamente**; `F6` **debe sustituir** esa confianza
documental por verificación externa mecánica; y **PesquerApp no puede iniciar su adopción
permanente mientras esa sustitución no exista y esté probada**.

> **DISPUTA REGISTRADA Y NO RESUELTA — el alcance de la condición previa de `(c)`.
> `X-02`/§6 del documento 24. NO se resuelve aquí, y `F4` no la resuelve.** Se registran
> **los hechos que el gate estableció y que nadie discute**, sin retirar nada de la
> propagación y sin escribir ni una palabra dentro de esta resolución:
>
> ```text
> 1  ESTA SEDE dice UNA condición previa · las SEDES QUE PROPAGAN dicen TRES
>    `O18` en su entrada de §2 escribe de `(c)`: «OBLIGATORIA EN `F6`, Y CONDICIÓN PREVIA
>    A PesquerApp». Barrido del fichero entero: CERO apariciones de «ADS operativo»,
>    CERO de «certificar adaptadores», CERO reparto `SIS`/`PLT`/`VER`/`SEG`.
>    SEIS sedes del corpus escriben TRES: «…a la adopción permanente de PesquerApp, a
>    declarar ADS operativo y a certificar adaptadores».
>    Y §11.8 del documento 11 rotula «EL REPARTO, LITERAL DE `O18`» un reparto de
>    capacidades que esta entrada NO contiene. El adjudicador RECHAZA ESE RÓTULO,
>    y NO rechaza el contenido
>
> 2  HAY CORROBORACIÓN PARCIAL, CONTEMPORÁNEA, E INDEPENDIENTE DE §11.8
>    el mensaje del commit que TRANSCRIBE `O18` —`bcee159`, primero de la tanda, cuyo
>    único trabajo declarado es registrar la resolución— YA ESCRIBE LAS TRES CONDICIONES:
>    «(c) OBLIGATORIA en `F6`: … condicion previa a la adopcion permanente de PesquerApp,
>     a declarar ADS operativo y a certificar adaptadores.»
>    Es UN COMMIT ANTERIOR a la propagación, que es `8e70d94`
>
> 3  HAY UNA ANOMALÍA DE FORMA, Y APUNTA EN SENTIDO CONTRARIO PARA EL REPARTO
>    la entrada de `O17` SÍ registra DENTRO de su propia entrada de §2 la sección
>    «El REPARTO DE RESPONSABILIDADES que el Owner decide». Ésa es la forma que el corpus
>    estableció, y la entrada de `O18` NO la tiene.
>    Y el reparto rotulado «LITERAL DE `O18`» NO aparece en `bcee159`: NACE en `8e70d94`,
>    el commit de propagación. Tiene, por tanto, un estatus probatorio DISTINTO del de
>    las dos condiciones: para el reparto el adjudicador declara INDETERMINADO
>
> 4  NO EXISTE SEDE DEL OWNER EN SU PROPIA MANO
>    `docs/owner/` contiene DOS documentos y ninguna de las resoluciones `O15`–`O18`.
>    El sobre de ancla de `O18`(b) no ancla ninguna resolución del Owner (`X-03`)
> ```
>
> **POR QUÉ NO SE CORRIGE AQUÍ.** El adjudicador `X` resolvió que la disputa es
> **INDECIDIBLE desde el árbol** y que **NINGUNA de las dos vías de remedio es ejecutable
> por `F4`**: recortar la propagación sería que `F4` **borrase contenido que el coordinador
> afirma del Owner**; completar esta entrada sería que `F4` **escribiese palabras dentro de
> una resolución del Owner**, y eso es `G21` de `KERNEL.md`. Por eso **la propagación NO se
> recorta y esta entrada NO se completa**, y consta que ninguna de las dos posturas queda
> declarada vencedora.
>
> **QUEDA PENDIENTE DEL OWNER, COMO RATIFICACIÓN Y NO COMO ELECCIÓN DE DISEÑO.** La pregunta
> exacta, con sus tres alternativas —ratificar el texto AMPLIO, ratificar el texto ESTRICTO,
> o ratificar Y DAR SEDE en `docs/owner/`—, está en **§13 de la adjudicación de `X`, dentro
> del documento 24**, `docs/evolucion/24-TERCER-GATE-DE-CERTIFICACION-F4C.md`. **Mientras no
> haya ratificación, esta disputa sigue ABIERTA**, y **ningún hallazgo se declara SUPERADO
> por haberla registrado**: registrar no es corregir.

**(b) ES UNA GARANTÍA TRANSITORIA Y EXPLÍCITAMENTE LIMITADA.** No se presenta como otra cosa.

```text
LO QUE (b) AÑADE      · una referencia que el árbol NO puede redefinir unilateralmente
                        durante el gate
                      · detección de que el árbol auditado no coincide con el encargado
                      · detección de que el manifiesto fue sustituido después del reparto

LO QUE (b) NO         · compromiso del canal del Owner
PROTEGE, Y SE DICE    · compromiso simultáneo del repositorio y del coordinador
                      · robo de credenciales
                      · reescritura autorizada de ramas remotas
                      · manipulación del ejecutor externo
                      · falsificación de identidad
                      ESOS RIESGOS PERTENECEN AL VERIFICADOR EXTERNO DE `F6`
```

**Qué NO autoriza `O18`.** **No autoriza iniciar `F5`, ni `F6`, ni PesquerApp.** No cierra `F4c`
por sí misma —eso lo hace un gate independiente— y no deroga ninguna presión vigente.

**Qué cambia si el Owner decide otra cosa:** volver a (a) retira una garantía que el Owner ha
rechazado retirar; exigir (c) dentro de `F4c` reinstala el bloqueo circular que esta resolución
existe para evitar.


---

## 3 · Contradicciones detectadas contra (a) y (b)

Se registran; **no se modifican (a) ni (b)**. Cada una lleva una propuesta de cambio
mínima que el Owner puede aceptar o rechazar.

### C1 · Encuadre: función de DSP en (a), y sin embargo necesita rol, método y memoria propios

**Qué dice (a).** a.3 sitúa *Encuadre* como una de las cuatro funciones de `DSP`, junto a
Enrutamiento, Estado y Supervisión, y describe `DSP` como *«implementación software/runtime
primero»*, sin autoridad sobre el contenido de ninguna capa.

**Qué exige el paso 1.** Un rol que escucha, conversa, hace brainstorming, consulta
especialistas, mide incertidumbre y ayuda al Owner a descubrir lo que quiere. Eso no es
runtime: es trabajo de contenido, con método, memoria y checkpoint.

**Contradicción real:** si el trabajo conversacional vive dentro de `DSP`, entonces `DSP`
tiene trabajo de contenido, y (a) afirma que no lo tiene.

**Propuesta de cambio mínima (una frase en a.3):**

```text
DSP · DESPACHO — Encuadre
  ANTES:  «Encuadre — id, enunciado de una línea […] Se apoya en el índice de lo existente»
  DESPUÉS: añadir «El TRABAJO CONVERSACIONAL del encuadre —escuchar, interpretar,
           conversar, medir incertidumbre— lo ejecuta la capacidad ENC, que entrega a DSP
           un encuadre listo. DSP conserva la ficha, el anclaje mecánico y el índice de
           lo existente.»
```

**Cómo se ha continuado sin la decisión:** `ENC` se ha construido como capacidad completa
con los doce campos; su ficha declara `deriva_de: a.3 DSP/Encuadre`. Si el Owner prefiere
la lectura estricta de (a), el contenido de `capacidades/ENC/` se mueve bajo `DSP/` sin
reescribir un solo rol ni método. **El trabajo no dependía de la decisión.**

### C2 · «El gate no es un juicio: es una lista» frente a la excelencia visual

**Qué dice (a).** a.1: *«GATE — lista COMPROBABLE […] No es un juicio: es una lista. Si
hiciera falta juicio, ese juicio es otra capacidad activada, no una aprobación oculta.»*

**Qué exige el paso 3.** *«La excelencia no puede reducirse a una puntuación automática.
Usa rúbricas y evidencia, pero conserva crítica profesional y juicio del Owner donde
corresponda.»*

**Contradicción aparente, resuelta sin cambiar (a).** El juicio no se mete dentro del
gate: se materializa como **rol independiente** —`DIS/critica-visual`— cuya salida es un
artefacto. El gate `gate:excelencia-visual` sigue siendo una lista comprobable, y lo que
comprueba es que **exista** ese artefacto, con veredicto explícito, ejes puntuados,
evidencia enlazada y desacuerdos registrados. Es exactamente lo que a.1 ordena: *«ese
juicio es otra capacidad activada»*.

**No se propone cambio a (a).** Se registra porque es el punto donde más fácil sería
introducir una aprobación oculta, y la revisión adversarial debe volver aquí.

### C3 · `C-DIS` de b.16 no distingue superficie nueva de superficie tocada

**Qué dice (b).** `C-DIS` se activa cuando el item *«toca una superficie que un humano
percibe […] O altera la experiencia de un flujo existente»*.

**Problema operativo.** Esa condición es binaria y `DIS` tiene tres procedimientos
distintos (`Fundacion`, `Reconstruccion`, `Evolucion`) más una escala de exploración.
Aplicada tal cual, una corrección de espaciado dentro de un patrón vigente convoca el
mismo procedimiento que una pantalla nueva.

**Resuelto sin tocar (b):** `C-DIS` sigue decidiendo **si** `DIS` se activa. Cuál de sus
métodos se ejecuta y cuánta exploración exige lo decide la **tabla de novedad** de
[`kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md`](../../kernel/operativo/diseno/03-ESCALA-DE-NOVEDAD.md),
que es contenido de método, no condición de ruta. **No hay contradicción; hay un hueco que
el kernel operativo rellena.**

### C4 · `owner_attention_slots: 1` frente a una conversación de fundación de Diseño

**Qué dice (b).** b.11 fija `owner_attention_slots` por defecto en 1.

**Tensión.** `DIS/Fundacion` es explícitamente una conversación larga y repetida con el
Owner. Mientras dure, ningún otro paquete puede consumir su atención, y el paso 3 prohíbe
limitar artificialmente las sesiones necesarias.

**Resuelto sin tocar (b):** b.11 ya separa atención de ejecución, y su regla 4 lo dice con
todas las letras. `DIS/Fundacion` declara sus puntos de atención como **sesiones
delimitadas** —no como ocupación continua del slot— de modo que entre sesión y sesión el
slot queda libre. Está implementado en el método: cada punto de atención abre y cierra.

**Límite honesto:** si el Owner quiere conversar con dos equipos a la vez, `owner_attention_slots`
es un parámetro de proyecto, no una regla del kernel. Ese cambio es suyo (O6 no lo cubre;
se decide en el PROFILE).

---

## 4 · Límites declarados de esta iteración

> **Actualizado el 2026-08-26 por la implementación multi-repositorio.** Los límites de
> abajo son los de la iteración que construyó el kernel operativo. Lo que la implementación
> del mandato multi-repo añadió —`C6`, `C7`, `E2`, `SOURCES.toml`, `workspace.py` y sus
> pruebas— **no cambia ninguno de ellos**: sigue sin haber runtime, sigue sin haber piloto
> en un proyecto real, y las pruebas que exigen runtime siguen en `contrato-definido`.

```text
NO se ha implementado el dispatcher ni el runtime          — encargo explícito del Owner
NO se ha instalado el kernel en gym-wear                   — encargo explícito
NO se ha empezado el pack ERP                              — encargo explícito
NO se han diseñado las secciones (c) a (i) en abstracto    — (c) y (d) quedan cubiertas
                                                             PARCIALMENTE y de forma
                                                             operativa, no como sección
NINGUNA prueba que requiera runtime puede superarse hoy    — registro en pruebas/REGISTRO.md
La coherencia PROSA↔BLOQUE dentro de un mismo fichero no
  es comprobable automáticamente                           — la cubre la revisión adversarial
```
