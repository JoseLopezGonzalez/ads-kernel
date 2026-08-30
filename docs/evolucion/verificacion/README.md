# Verificación mecánica de la corrección del GATE DE CIERRE

**Qué es.** La batería que comprueba, sobre el árbol y no sobre lo que el texto afirma de
sí mismo, que las correcciones aplicadas a `F4c` están hechas y que el corpus gobernado no
se puede alterar en silencio.

**Qué NO es.** No es un gate, y no certifica nada. La escribe quien aplica la corrección,
que es exactamente lo que `F4c` lleva doce tandas sin poder aceptar como prueba. Su valor es
otro: **hace refutable** cada afirmación de la tanda.

```bash
python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py
```

Sale con `0` si todas las comprobaciones están en verde, con `1` si alguna falla y con `2`
si la batería no pudo completar su ejecución. El número de comprobaciones **se deriva de las
que se ejecutan y se CONTRASTA contra la tabla de abajo**, que es su sede: `G-34` compara los
dos conjuntos en las dos direcciones, de modo que **amputar una llamada `check()` da ROJO y
la que falta aparece nombrada**.

> Antes esto decía, como virtud, que «el número de comprobaciones no se escribe en ningún
> sitio». Era falso como virtud: el segundo gate de certificación amputó la llamada de
> `G-31` y la batería imprimió **`36/36 comprobaciones en verde`** sin que la que faltaba
> apareciera en el informe (`T-20`). Un censo que sale de lo que quedó no es un censo.

> **Portabilidad.** La batería deriva su raíz de `__file__` —tres niveles por encima de
> `docs/evolucion/verificacion/`— y **de nada más**. No usa el cwd y no codifica la ruta de
> ninguna máquina. Si la estructura esperada no aparece bajo la raíz derivada, **falla con
> diagnóstico y código 2** en vez de adivinar.

## Los ficheros de este directorio

```text
comprobar-correccion-gate-de-cierre.py   la batería
derivar-universo-obligatorio.py          el derivador del universo obligatorio de un gate
emitir-sobre-de-ancla.py                 el emisor del SOBRE DE ANCLA de un gate (`O18`)
README.md                                esto
CORRIGENDUM-DICTAMENES-INMUTABLES.md     correcciones sobre dictámenes que no se editan
manifiestos/                             los manifiestos de asignación de cada gate
```

El instrumental de este directorio está enumerado aquí a propósito: `G-29` compara los
ficheros del corpus contra los publicados y **sólo admite una ampliación de
`verificacion/` si este README la enumera**. Las rutas que cuentan para esa comparación son
`docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py`,
`docs/evolucion/verificacion/derivar-universo-obligatorio.py`,
`docs/evolucion/verificacion/emitir-sobre-de-ancla.py`,
`docs/evolucion/verificacion/README.md` y
`docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md`.
Los manifiestos y todo lo que cuelgue de `manifiestos/` son **inmutables** y no se amplían
por esta vía: los fija `G-22`.

## Instrumental EN CORRECCIÓN en esta tanda

**Ésta es la sede de la declaración, y `G-34` la lee.** El inventario de integridad del
instrumental exige que cada fichero de `verificacion/` esté **enumerado aquí, publicado en
`HEAD` e IDÉNTICO a `HEAD`**. Un instrumento modificado y **no declarado** en esta tabla es
ROJO: es la puerta de `X-01`, por la que tres líneas sin commitear en el emisor producían un
sobre idéntico al honesto sobre un corpus corrupto con la batería en 38/38.

**Y la declaración CADUCA SOLA:** declarar aquí un fichero que ya coincide con `HEAD` es
también ROJO. Esta tabla **se vacía en el mismo commit que confirma los cambios**; si no se
vacía, `G-34` lo dice. Una exención que sobrevive a la tanda que la justificaba es una
puerta abierta.

**LA TABLA NO ESTÁ VACÍA: la tanda de `O19` está EN CURSO.** Los tres ficheros de abajo
difieren de `HEAD` porque esta tanda los está corrigiendo, y la declaración **se retira en el
mismo commit que confirma los cambios**. Si sobrevive a ese commit, `G-34` lo dice.

**LA TABLA ESTÁ VACÍA, y es lo que debe estar.** Los cambios de la tanda de `O19` —la
sede canónica del Owner— quedaron confirmados en el mismo commit que vació esta sección.
Ningún fichero de `verificacion/` difiere de `HEAD`.

| ruta | por qué difiere de `HEAD` |
|---|---|

> **`emitir-sobre-de-ancla.py` y por qué su salida NO vive aquí.** Lo exige `O18`, que adoptó
> la alternativa (b) —**un ancla documental EXTERNA al árbol auditado**— para poder cerrar
> `F4c` sin el bloqueo circular de esperar al verificador externo de `F6`.
>
> **Qué hace hoy, tras el tercer gate de certificación, y es distinto de lo que hacía:**
>
> · **Se niega a emitir con el árbol de trabajo sucio.** `git status --porcelain` tiene que
>   venir vacío. Un sobre sucio no se emite.
> · **Lee cada byte del COMMIT**, con `git show <commit>:<ruta>`, y ejecuta **el derivador
>   de ESE commit** sobre el árbol desplegado con `git archive`. Ni una lectura del
>   directorio de trabajo de quien emite. Antes `_universo()` leía con `io.open(RAIZ/ruta)`
>   y el digest publicado no correspondía a ningún commit.
> · **Publica los DOS árboles** —el de la candidata y el del gate—, cada uno con su
>   derivador, sus fuentes, sus líneas y su digest derivados de su propio commit, **y las
>   rutas en que difieren**. El sobre del gate anterior yuxtaponía el `tree` de la candidata
>   con las cifras del árbol del gate y eran **mutuamente insatisfacibles**: 65 fuentes /
>   53 354 líneas frente a 67 / 53 772. La causa no era un descuido — **el derivador es fila
>   de su propio universo** y el commit del manifiesto lo toca.
> · **Publica una receta que reproduce cada digest byte a byte**, y se verificó
>   ejecutándola. La anterior canalizaba `echo … | sha256sum`, que añade un salto final que
>   el digest no lleva: fallaba **sobre todo árbol, sano o corrupto**, y una regla de parada
>   alimentada por un falso positivo universal no distingue nada.
> · **Deriva `ASIGNACIONES`** de la columna `revisor` del reparto de lectura del manifiesto,
>   leído del commit del gate. Antes se recibía por CLI y no se contrastaba contra nada: era
>   el único campo sin contrastar y era el único falso —publicó 18 donde el manifiesto
>   da 17—. Si se pasa `--asignaciones`, tiene que coincidir con lo derivado.
> · **Escribe las OBLIGACIONES DEL REVISOR dentro del sobre**: recalcular los dos digest
>   antes de leer nada, leer el manifiesto en el commit del gate, y contrastar cada fila
>   contra el árbol que ESA fila declara.
>
> **Falla cerrado con código 2** ante cualquiera de esas cosas.
>
> **Su salida no se publica como fichero de este directorio, y es deliberado**: el
> coordinador la copia dentro del ENCARGO de cada revisor, por un canal que el repositorio
> no reescribe. **Un sobre que el revisor leyera del árbol dejaría de ser externo y no
> valdría para nada** — sería la misma circularidad que `§11.4` del documento 11 describe,
> movida de sitio. Por eso el adjudicador tiene prohibido aceptar un sobre reconstruido a
> posteriori desde el árbol.
>
> **Y lo que el sobre NO garantiza va escrito DENTRO del propio sobre**, no en una nota
> aparte: compromiso del canal del Owner · compromiso simultáneo del repositorio y del
> coordinador · robo de credenciales · reescritura autorizada de ramas remotas ·
> manipulación del ejecutor externo · falsificación de identidad. Esos riesgos son del
> **verificador externo que `O18` contrata para `F6`**, y que es condición previa a la
> adopción permanente de PesquerApp.

> **Lo que esta batería NO puede cerrar, y `O18` lo resuelve por otra vía.** `M-04` —«se
> puede construir un árbol defectuoso que pase en verde»— **no es satisfacible desde dentro
> del árbol**, y el corpus lo había declarado en `§11.4` del documento 11 antes de que
> ningún gate lo dijera: *«si el runner miente, nada dentro del repositorio lo detecta».*
> **Ninguna comprobación nueva de este fichero cierra esa clase**, y añadir una más «sólo
> movería la circularidad de sitio».
>
> **Y aquí este README decía algo falso, y se corrige.** Decía que «esta tanda **NO** escribe
> ninguna protección interna nueva» — pero la tanda anterior **sí escribió una**: `G-34`
> nació entonces, del hallazgo `T-20`, y el censo pasó de 37 a 38 comprobaciones. Negarlo
> mientras la tabla de abajo la publica era una contradicción dentro del mismo fichero.
>
> **Lo que es cierto de ESTA tanda, y se comprueba contando la tabla:** el censo sigue en
> **38** y **no se ha escrito ninguna comprobación nueva**. Lo hecho es **ensanchar el
> perímetro de las que ya existen** —`G-29` al repositorio entero, `G-34` al instrumental
> que produce el ancla, `G-21` y `G-11b` a las filas que DESAPARECEN, `G-26` a lo que queda
> dentro de una valla— y **retirar un interruptor léxico** de `_es_cita`. El adjudicador `X`
> lo ordenó con todas las letras: «NO se escriba una decimonovena protección sistémica».

## Qué comprueba cada una

| | qué comprueba | de qué hallazgo sale |
|---|---|---|
| `G-00` | que la batería **complete su ejecución y emita informe**. Cualquier sede ilegible o excepción no prevista se convierte en esta fila en ROJO, con el fichero y el motivo, en vez de un `traceback` sin informe | `Q-24` |
| `G-01` | cero `estado/cuarentena/` **vigente**, juzgado por **POLARIDAD** —un párrafo que reinstala la ruta manda sobre uno que la retira, y el silencio es INDETERMINADO y falla— y anclado en la fila `D87` del registro, que es su sede canónica | `I-01` · protección 4 |
| `G-02` | `.ads/run/quarantine/` clasificado en §2.4, listado en §2.3, con su ciclo, el bloqueo de `SEG` y la aceptación de pérdida del Owner | `I-01` |
| `G-03` | `estado/deriva/` con sus **siete** piezas | `I-02` |
| `G-04` | predicado `abierta(tx)` **único**: ninguna sede fuera de §2.6.1 lo redeclara | `I-03` · `I-09` |
| `G-05` | cero reglas de `#intentos` / `agotado` **vigentes** en la capa B | `I-03` |
| `G-06` | la capa B declara **dos** terminales, no uno | `I-03` |
| `G-07` | cero atribuciones «`PLT` para cada source change» | `I-04` |
| `G-08` | las sedes de §8 —**derivadas de las subsecciones del documento 11**, no escritas— y §18 citan `C7` operación a operación | `I-04` · `T-17` |
| `G-09` | §18 lleva el gate de `INS-5`, su salida y los tres productores de `O12` | `I-07` |
| `G-10` | **seis** extensiones de ficha en §5.2, §16 y §17 | `I-06` |
| `G-11` · `G-11b` | `D67` idéntica byte a byte a la de `7e99388`, y `D1`–`D86` intactas. **Las dos fallan CERRADO sin Git**, y la guarda de base vacía se evalúa sobre el texto crudo, no sobre `split("\n")`, que nunca podía dispararla. **Esa guarda ya no es sólo suya**: `G-22` y `G-28` la comparten. **Y el contraste MIRA LO QUE NO ESTÁ**: una fila de la base que ya no existe es una DESAPARICIÓN nombrada, y una duplicada también. La guarda era `if ob and ac and ob[0] != ac[0]`, y borrar una fila entera la hacía invisible | `I-16` · `Q-01` · `Q-22` · `T-05` · `A1` |
| `G-12` | `PN-14` presente, con sus campos, y **sin enmienda redactada** | `F-01` |
| `G-13` | el censo de presiones, derivado de sus cabeceras menos las marcadas, y el barrido de `PN-15` sobre el material APROBADO | `I-11` · `P-06` |
| `G-14` | `F-01` reclasificado, con `requiere_f5` y `requiere_f6` | `F-01` |
| `G-15` | `<CAP>:revision` derivado por las CUATRO vías con un lector que respeta **indentación y escalares de bloque**; procedencia conservada **y contrastada contra §19**; ancla normalizada; conjunto vigilado derivado de una **declaración estructurada** de la ficha; y **unicidad de proyección comprobada por tres caminos**, no por una redacción | `I-08` · `Q-02` · `Q-03` · `Q-05` · `Q-09` · `Q-10` · `Q-11` · `Q-12` · `Q-28` |
| `G-16` · `G-16b` | un estado primario por hallazgo, ninguno compuesto, con el **cardinal de la matriz leído de su propia cabecera**; y las condiciones `C-L` contrastadas contra su fila de detalle **por IGUALDAD EXACTA del estado**. El canon de estados admite **`NO CERRADA`** desde que `X-04` falsó `C-L.7`: **una condición puede volver a abrirse y el instrumento tiene que saber decirlo**. El canon es VOCABULARIO ADMITIDO, no presencia obligatoria — lo obligatorio es que las trece tengan estado, ninguna dos, la suma trece, y que **ningún estado que una fila de detalle use falte del resumen** | matriz · `Q-06` · `Q-11` · `Q-14` · `X-04` · protección 3 |
| `G-17` · `G-17b` | los recuentos publicados coinciden con los derivados, y la matriz de trazabilidad trae sus ids una sola vez, con severidad adjudicada y sin declarar SUPERADO ninguno | matriz · `Q-11` |
| `G-18` | vallas Markdown balanceadas en los cuatro ficheros en corrección | higiene |
| `G-19` | cero párrafos largos duplicados en esos cuatro | higiene |
| `G-20` | el registro `D` es una serie **continua desde `D1`, sin huecos y sin repetir**. El tope se **deriva de la última fila**: no se exige ningún `Dnn` concreto | trazabilidad · `Q-25` |
| `G-21` | **las resoluciones del Owner que `7e99388` publica siguen en el registro**, con su texto, sin duplicar y **sin DESAPARECER**, y falla CERRADO sin Git. **Y desde `O19`, la SEDE CANÓNICA manda sobre su proyección**: la sede tiene que poder leerse —si no, ROJO—, cada resolución que publica tiene su proyección `### `Onn`` en el registro, y las nacidas **desde la resolución que la propia sede declara como su origen** —«esta sede nace por `Onn`», DERIVADO, no escrito aquí— **ENLAZAN a la sede** y **no amplían su texto en ninguna valla**: cada bloque citado en la proyección tiene que estar LITERALMENTE en la sede. `O19` nació de una proyección que decía MENOS de lo que el Owner había resuelto | Borrar la fila `\| O5 \|` daba `38/38` verde e imprimía «ninguna difiere»: la guarda no comparaba lo que no estaba, y el cardinal que hacía de red tampoco lo veía porque **el registro crece** —17 ≥ 16 se cumple con una resolución menos— | trazabilidad · `A1` |
| `G-22` | **el inventario de inmutables se DERIVA del árbol** —todo documento numerado de `docs/evolucion/`, todos los manifiestos y, desde `O19`, **`docs/owner/` ENTERO**, menos los cuatro ficheros en corrección— y cada uno se contrasta contra `HEAD` **y** contra la revisión base. No hay ningún rango escrito. Un documento numerado nuevo **nace ADMITIDO por `G-29` y queda protegido aquí en cuanto se confirma**; y una salida de `git ls-tree HEAD` **vacía con éxito** ya no se interpreta como «nada cambió»: falla CERRADO. El detalle dice cuántos inmutables nacieron después de la revisión base y por tanto se contrastan sólo contra `HEAD`. **La zona `docs/owner/` entra en ESTE inventario y no en uno nuevo**: mismo id, mismo doble contraste, mismo perímetro derivado, y el directorio se barre ENTERO en vez de por extensión. Hasta `O19` nadie miraba su CONTENIDO —`G-29` veía nacer y desaparecer ficheros, y editar el texto de una resolución del Owner no lo veía nadie—, y desde `O19` esa zona es la AUTORIDAD CANÓNICA: material del Owner que **no puede alterarse en silencio**. **Y la sede es APPEND-ONLY, con lo que eso implica aquí, dicho para que no sorprenda:** una entrada nueva del Owner deja la sede MODIFICADA respecto de `HEAD` y `G-22` la da en ROJO hasta que se confirma. Es lo que se quiere —material del Owner sin confirmar no pasa por vigente en silencio— y quien la añada responde de ello en el mismo commit | `Q-23` · `Q-26` · `T-05` · `O19` · protecciones 1 y 7 |
| `G-23` | lo normativo intacto y la excepción del kernel **contrastada contra la prosa del checkpoint**, que ya no enumera nada a mano; y el punto de entrada **remite** en vez de copiar | alcance · `M-06` · `R-02` |
| `G-24` | las fuentes y las fichas de `C-0.1`/`C-0.2` **se LEEN** en UTF-8 y son exactamente ésas, con el catálogo de capacidades derivado **una sola vez** —`_CAPS_DIRS`— y compartido con `G-15`: `G-24` lo recomputaba por su cuenta y ahora lo consume | cobertura · `Q-27` · `T-16` |
| `G-25` | los cuatro macrocircuitos declaran sus **catorce** campos | `I-21` |
| `G-26` | recuentos derivados en cuatro planos, con las citas históricas reconocidas por **etiqueta estructural de región** y no por una palabra en la línea; y la región **cierra al terminar el bloque que la etiqueta encabeza** —encabezado, valla de código, línea en blanco **también dentro de una valla**, salida de la cita, o **la marca siguiente**—, de modo que una etiqueta ya no exime lo que queda **fuera de su bloque**. La excepción `not en_valla` dejaba **1 899 de 3 562 líneas del checkpoint (53 %) exentas de todo control de cifra sin que nadie atacara nada**; retirada, bajan a 1 229. **Y la tercera rama de `_es_cita`, la de los VERBOS, se retiró entera**: «decía », «en vez de » o «reanclado » delante de una cifra viva falsa apagaban esta comprobación, y ninguna comprobación puede depender de una palabra. Quedan las dos formas ESTRUCTURALES de citar: «…» y la etiqueta de región | higiene · `P-01` · `Q-04` · `Q-07` · `P-05` · `T-06` · `A3` · `A4` · protección 2 |
| `G-27` | la regla 1 de §2.6.10 usa «los cinco **CAMPOS**» | `A7` |
| `G-28` | **ningún documento de gate cambia de VEREDICTO, POLARIDAD o ESTADO en el árbol de trabajo sin que se diga**: el censo de las tres familias se deriva del documento y se contrasta **contra su versión en `HEAD`**. Una salida de `git ls-tree HEAD` vacía con éxito, o CERO documentos contrastados, dan ROJO en vez de `OK`. **Lo que NO ve, y se dice: un cambio ya CONFIRMADO**, porque su referencia es `HEAD` y `HEAD` la escribe quien confirma | protección 8 · `T-05` |
| `G-29` | **topología y unicidad de TODO el corpus gobernado, y el perímetro YA NO SE ESCRIBE: es el repositorio ENTERO menos `.git` y el bytecode**, con la exclusión declarada y con motivo. Era una lista de siete zonas, y una lista escrita caduca: copias **byte a byte** del material APROBADO y del registro en `docs/normativa/` —un directorio que no existía— y en la raíz de `docs/` daban **38/38 verde**, mientras el mismo gemelo dentro de una zona listada daba `FALLO G-29`. La zona normativa para los marcadores canónicos también se deriva: **todo el corpus menos `docs/evolucion/`**, donde el bloque es CITA. Ninguna ampliación sin clasificar, ningún gemelo byte a byte, y ningún marcador de bloque canónico —derivado, no escrito— con sedes nuevas. Un documento numerado nuevo **ya no se admite en blanco**: tiene que estar **enlazado desde `00-INDICE.md`** —la regla que el propio índice escribió— y **no repetir ordinal**. **`docs/owner/` no admitía NINGUNA ampliación**, y `O19` ordenó crear ahí la sede canónica: se admite con la MISMA condición —enlazada desde `00-INDICE.md`, en el mismo commit que la crea—, de modo que una segunda sede plantada en esa zona sin enlazar sigue siendo ROJA, y su contenido queda después bajo `G-22` | `Q-02` · `M-04` · `T-03` · `O19` · protecciones 5 y 9 |
| `G-30` | **la excepción del kernel por CONTENIDO y CLASIFICACIÓN**: cada excepción tiene clase, y **cada clase impone una regla sobre el contenido que no es «ser igual a `HEAD`»** —un CÓDIGO DE VALIDADOR tiene que definir mutaciones y **cuadrar con la EVIDENCIA que él mismo publica**, una EVIDENCIA DERIVADA tiene que declarar la orden que la produce, y una HUELLA tiene que ser una huella—. La huella **se RECALCULA** aquí, y **reanclarla ya no lava una mutilación**: el vaciado se ve en el contenido | `Q-05` · `T-01` · protección 6 |
| `G-31` | **ninguna comprobación se apaga escribiendo una palabra ni una etiqueta fuera de sitio**: las palabras gatillo se pegan al mismo dato y se exige que recuentos, polaridad, comparación de estado y marca histórica no cambien de veredicto; dos fixtures exigen que una etiqueta **no exima una línea que está fuera de su cita ni el bloque siguiente al suyo**; y **los once VERBOS RETIRADOS de `_es_cita` se prueban uno a uno, puestos DELANTE de la cifra**, que es donde apagaban. La lista de gatillos eran las palabras de `T-06` y **ninguna de las que apagaban de verdad**: la comprobación que existe para cazar interruptores léxicos no probaba el que había | protección 10 · `T-06` · `A3` |
| `G-32` | **todos** los niveles de certificación —derivados de la tabla de §9.1— tienen PRODUCTOR declarado en §9.1 y en §9.2, y la cadena de §9.2 se deriva de su propia línea. **Y la fila `O17` se LEE**: si deja de resolver que el Estructural se produce al inicio de cada macrocircuito, o si su regla 12 deja de decir lo que aquí se comprueba, esto es ROJO | `O17` regla 12 · `T-08` · protección 11 |
| `G-34` | **el CENSO de comprobaciones cuadra con su SEDE**: los identificadores que esta tabla publica y los que la batería ejecuta se contrastan en las **dos direcciones**, de modo que **amputar una llamada `check()` da ROJO** y la que falta aparece nombrada en el informe. **Y el INVENTARIO DE INTEGRIDAD del instrumental, DERIVADO del directorio y no escrito**: todo fichero de `verificacion/` tiene que estar **enumerado en este README, publicado en `HEAD` e IDÉNTICO a `HEAD`, o DECLARADO en corrección** en la sección de arriba — y la declaración **caduca sola**, porque declarar un fichero que ya coincide con `HEAD` también es ROJO. Cubría dos ficheros en dos dimensiones y dejaba fuera **al emisor y al derivador, que son los que producen el ANCLA**: con tres líneas sin commitear en el emisor se emitía un sobre idéntico al honesto sobre un corpus corrupto, y una puerta trasera en el derivador desarmaba el cliquet, las dos con la batería en 38/38 | `T-20` · `X-01` |
| `G-33` | los macrocircuitos se **derivan de §8** y cada uno produce su Estructural en **FASE 0** antes de toda mutación; con **DOS censos separados, y ésa es la corrección**: **una prueba negativa ANCLADA EN EL ÁRBOL** —su mutante sale del texto del corpus, y un corpus distinto la mueve— y **cuatro FIXTURES DEL EVALUADOR**, sintéticos, que cazan una amputación del evaluador pero que **NINGÚN árbol puede poner en rojo**. Se comprobó por barrido exhaustivo: sus aserciones se cumplen para toda cadena y todo conjunto de identificadores no vacíos. Contarlos juntos bajo «pruebas negativas ejecutadas» decía de ellos algo que no es cierto; no se retiran, se cuentan aparte. Cada par lleva **su CONTROL en verde y su MUTANTE en rojo**, para que ninguno pueda ser un fixture que no falle. **Y `O17` y su propagación se LEEN**: las doce reglas, con su cardinal derivado de la frase que las anuncia, y la fila del registro que declara a `O17` su única fuente, buscada **por lo que dice y no por su número** | `O17` · `D107` · `T-08` · `T-09` · protecciones 12 a 15 |

## Lo que esta batería NO comprueba, y se dice

```text
NO EJECUTA NADA DEL         no hay runtime, no hay esquema de `evento`, no hay validador
PROTOCOLO                   del diario y no hay un solo fichero bajo `estado/`. Todo lo que
                            comprueba es TEXTO contra TEXTO, y un contrato coherente no es
                            un sistema que funcione

NO SUSTITUYE AL GATE        no juzga si la arquitectura es SUFICIENTE PARA F5. Comprueba que
                            lo que la tanda dice haber corregido está corregido, que es
                            mucho menos

NO CUBRE EL CONTENIDO       las fuentes y las fichas de `G-24` se comprueban por LECTURA en
DEL CORPUS                  UTF-8 y por comparación de NOMBRES, no por lo que dicen

LAS PRUEBAS NEGATIVAS DE    `X-S1`–`X-S9` son contrato de prueba y **no se han ejecutado**
`G-33` SON DE CONTRATO,     contra un sistema. Y de los CINCO pares control/mutante que
Y CUATRO DE CINCO NO        `G-33` ejecuta, **CUATRO no tocan el árbol**: son fixtures del
TOCAN EL ÁRBOL              EVALUADOR sobre diccionarios sintéticos, y **ningún árbol los
                            pone en rojo** —comprobado por barrido exhaustivo—. Cazan una
                            amputación del evaluador, y nada más. **La única anclada en el
                            árbol es la de la FASE 0**, cuyo mutante sale del texto real del
                            macrocircuito de §8. El informe publica los dos censos por
                            separado desde esta tanda; antes los sumaba (`W2`). Escribir el
                            contrato de una prueba no es la prueba

NO PROTEGE CONTRA UNA       `G-29` admite un documento numerado nuevo en `docs/evolucion/`
MARCA HISTÓRICA FALSA       —enlazado desde `00-INDICE.md` y con ordinal libre—, porque
DENTRO DE SU PROPIO         publicarlo es el producto legítimo de un gate; y
BLOQUE                      `_regiones_historicas` cree a una etiqueta `[HISTÓRICO]` puesta
                            al principio de un bloque. Lo cerrado son DOS cosas: que una
                            **palabra suelta dentro de una frase** apague un control, y que
                            una **etiqueta alcance fuera de su bloque o fuera de su cita**.
                            Lo que sigue siendo posible es declarar histórico **el bloque
                            que la etiqueta encabeza**, y eso es visible al leer

NO VE UN CAMBIO YA          `G-22`, `G-28` y `G-30` contrastan contra `HEAD` y contra la
CONFIRMADO EN LO QUE        revisión base `05f71b7`. Un documento nacido DESPUÉS de esa base
NACIÓ DESPUÉS DE LA         sólo tiene a `HEAD` como referencia, y `HEAD` lo escribe quien
REVISIÓN BASE               confirma. `G-22` publica cuántos están en ese caso; cerrarlo del
                            todo es `M-04` y no se resuelve aquí

NO PUEDE CERRAR `M-04`,     esta batería vive DENTRO del repositorio que audita y compara
Y NO LO PRETENDE            contra referencias que también viven ahí. §11.4 del documento 11
                            lo declaró antes que ningún gate: «*si el runner miente, nada
                            dentro del repositorio lo detecta*». `G-34` cierra dos puertas
                            concretas —que amputar una comprobación no se viera, y que el
                            emisor y el derivador no estuvieran en ningún inventario— y **no
                            cierra la clase**: quien pueda escribir el árbol puede editar la
                            batería, su README y la declaración de instrumental EN
                            CORRECCIÓN a la vez. El segundo gate de certificación llevó la
                            decisión al Owner, y su RATIFICACIÓN sigue pendiente. **Ni esta
                            tanda ni la del documento 24 han escrito una comprobación nueva
                            —el censo sigue en 38—: las dos han ensanchado perímetros. La de
                            `O19` extiende `G-22` a `docs/owner/`, clasifica esa zona en
                            `G-29` y hace que `G-21` mire la sede canónica; la anterior
                            retiró además un interruptor. La tanda que escribió una de
                            verdad fue la de `G-34`, y este README lo negaba**

LA SEDE CANÓNICA DEL        `G-21` comprueba que la proyección ENLACE a la sede y que
OWNER NO SE VERIFICA        **ninguna valla suya amplíe el texto canónico**, y `G-22` que
CONTRA NADA EXTERNO         la sede no cambie en silencio. Ninguna de las dos puede decir
                            que ese texto sea el que el Owner emitió: la sede vive DENTRO
                            del repositorio, y quien pueda escribirlo puede escribirla.
                            **`O19` traslada la AUTORIDAD, no la verificabilidad**, y es la
                            misma limitación que `O18` declara de sí misma. Se cierra con el
                            verificador externo de `F6` y con nada de aquí. Y hay una
                            segunda resta, dicha: **la PROSA de la proyección no se compara
                            palabra a palabra con la sede** — sólo sus vallas, que son la
                            forma en que el registro cita texto resolutivo

EL CAMPO `espera` DE LAS    `G-30` DERIVA y PUBLICA cuántas mutaciones de
MUTACIONES DEL KERNEL       `comprobar_negativos.py` carecen del campo `espera` y son por
NO ES SUYO                  tanto vacuas en potencia (`T-13`): una mutación sin `espera` se
                            da por detectada porque la prueba falló, sin comprobar que falló
                            POR ESO. **El remedio vive en `kernel/`, que esta batería no
                            escribe**: se publica para que sea refutable, no se arregla aquí
```

## Cómo se demuestra que una corrección corrige

Cada corrección de esta batería lleva **el contraejemplo que la motivó reproducido**: se
construye el árbol defectuoso sobre una copia en `/tmp`, se comprueba que **antes pasaba en
verde**, se aplica el arreglo y se comprueba que **ahora falla nombrando la causa**. Un
arreglo que no se ha visto fallar antes no se sabe si arregla, y una corrección que sólo
cubre el perímetro exacto de su contraejemplo es el defecto que el GATE INDEPENDIENTE DE
CERTIFICACIÓN —documento 22— castigó con ocho árboles defectuosos en verde.

## El derivador del universo obligatorio

```bash
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py          # tabla
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py --md     # Markdown
python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py --rutas  # sólo rutas
```

Materializa la regla `1bis` de `C-L.5`. **Sus cardinales se LEEN de `1bis`** —cuántas
fuentes tiene el componente (i), cuántas fuentes y cuántas fichas el (ii)— en vez de estar
escritos aquí; exige que las fuentes de `C-0.1` sean **distintas** y no sólo tantas; y los
componentes (iii) y (v) llevan guarda: que la sede siga nombrando sus tres piezas, y que
ninguna fila del encargo esté sin cláusula, repetida o apuntando a una ruta que no existe.
**Falla cerrado con código 2** ante cualquiera de esas cosas.

Y su cabecera promete que **«nunca reduce el universo en silencio»**, que hasta ahora era una
frase y ahora es código:

```text
EL CLIQUET DE LOS       toda ruta que un manifiesto INMUTABLE declaró obligatoria tiene que
MANIFIESTOS             seguir saliendo de algún componente. Borrar una fila del `ENCARGO`
                        reducía el universo con `exit 0` y sin un aviso; hoy es código 2 y
                        dice qué ruta y qué manifiesto la declaró

CLASIFICACIÓN TOTAL     todo documento numerado de `docs/evolucion/` tiene que caer en
DEL COMPONENTE (iv)     `VOCES_DE_DICTAMEN` o en `VOCES_DE_NO_DICTAMEN`. El que no case con
                        ninguna **para el derivador**, en vez de caerse del universo sin que
                        nadie se entere — que es lo que pasaba con un `DICTAMEN` nuevo

LA RAMA QUE EXISTE      el diagnóstico de «cardinales que no son numerales legibles» tenía un
PARA FALLAR CERRADO     `%r` con una tupla de tres y reventaba con `TypeError`, traza y
FALLA CERRADO           código **1**, sin la línea `FALLA CERRADO ·` que el manifiesto enseña
                        a buscar. Hoy sale con **2** y con su diagnóstico

CADA MANIFIESTO APORTA  el lector de filas exigía COLUMNA ORDINAL, y el manifiesto del gate
FILAS AL CLIQUET        del documento 21 no la tiene: su tabla empieza por la ruta. **De los
(`W2-03`)               cinco manifiestos inmutables, uno aportaba CERO filas** —43 rutas sin
                        proteger— y la guarda sólo miraba el total, con lo que no podía
                        disparar. Hoy la ruta puede ir en la primera o en la segunda celda, y
                        un manifiesto que no aporte ninguna fila es código **2** con su nombre

UN DICTAMEN NO SE CAE   un documento numerado cuyo H1 casara con una voz de NO-DICTAMEN salía
DEL UNIVERSO PORQUE     del universo con `exit 0`. El cliquet lo caza si algún manifiesto lo
LE CAMBIEN EL TÍTULO    declaró; para el dictamen NUEVO —el que nadie ha leído— no había red.
(`W2-06`)               Hoy **un documento cuyo NOMBRE dice dictamen no puede excluirse por su
                        H1**, y las exclusiones del componente (iv) **se publican con su H1**
                        en la salida de tabla: lo que queda fuera se ve
```
