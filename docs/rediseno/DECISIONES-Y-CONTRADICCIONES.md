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
