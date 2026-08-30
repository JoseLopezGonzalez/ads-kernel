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
si la batería no pudo completar su ejecución. **El número de comprobaciones no se escribe
en ningún sitio**: la batería lo publica al final, derivado de las que ejecuta.

> **Portabilidad.** La batería deriva su raíz de `__file__` —tres niveles por encima de
> `docs/evolucion/verificacion/`— y **de nada más**. No usa el cwd y no codifica la ruta de
> ninguna máquina. Si la estructura esperada no aparece bajo la raíz derivada, **falla con
> diagnóstico y código 2** en vez de adivinar.

## Los ficheros de este directorio

```text
comprobar-correccion-gate-de-cierre.py   la batería
derivar-universo-obligatorio.py          el derivador del universo obligatorio de un gate
README.md                                esto
CORRIGENDUM-DICTAMENES-INMUTABLES.md     correcciones sobre dictámenes que no se editan
manifiestos/                             los manifiestos de asignación de cada gate
```

El instrumental de este directorio está enumerado aquí a propósito: `G-29` compara los
ficheros del corpus contra los publicados y **sólo admite una ampliación de
`verificacion/` si este README la enumera**. Las rutas que cuentan para esa comparación son
`docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py`,
`docs/evolucion/verificacion/derivar-universo-obligatorio.py`,
`docs/evolucion/verificacion/README.md` y
`docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md`.
Los manifiestos y todo lo que cuelgue de `manifiestos/` son **inmutables** y no se amplían
por esta vía: los fija `G-22`.

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
| `G-08` | §8.0–§8.4 y §18 citan `C7` operación a operación | `I-04` |
| `G-09` | §18 lleva el gate de `INS-5`, su salida y los tres productores de `O12` | `I-07` |
| `G-10` | **seis** extensiones de ficha en §5.2, §16 y §17 | `I-06` |
| `G-11` · `G-11b` | `D67` idéntica byte a byte a la de `7e99388`, y `D1`–`D86` intactas. **Las dos fallan CERRADO sin Git**, y la guarda de base vacía se evalúa sobre el texto crudo, no sobre `split("\n")`, que nunca podía dispararla | `I-16` · `Q-01` · `Q-22` |
| `G-12` | `PN-14` presente, con sus campos, y **sin enmienda redactada** | `F-01` |
| `G-13` | el censo de presiones, derivado de sus cabeceras menos las marcadas, y el barrido de `PN-15` sobre el material APROBADO | `I-11` · `P-06` |
| `G-14` | `F-01` reclasificado, con `requiere_f5` y `requiere_f6` | `F-01` |
| `G-15` | `<CAP>:revision` derivado por las CUATRO vías con un lector que respeta **indentación y escalares de bloque**; procedencia conservada **y contrastada contra §19**; ancla normalizada; conjunto vigilado derivado de una **declaración estructurada** de la ficha; y **unicidad de proyección comprobada por tres caminos**, no por una redacción | `I-08` · `Q-02` · `Q-03` · `Q-05` · `Q-09` · `Q-10` · `Q-11` · `Q-12` · `Q-28` |
| `G-16` · `G-16b` | un estado primario por hallazgo, ninguno compuesto, con el **cardinal de la matriz leído de su propia cabecera**; y las condiciones `C-L` contrastadas contra su fila de detalle **por IGUALDAD EXACTA del estado** | matriz · `Q-06` · `Q-11` · `Q-14` · protección 3 |
| `G-17` · `G-17b` | los recuentos publicados coinciden con los derivados, y la matriz de trazabilidad trae sus ids una sola vez, con severidad adjudicada y sin declarar SUPERADO ninguno | matriz · `Q-11` |
| `G-18` | vallas Markdown balanceadas en los cuatro ficheros en corrección | higiene |
| `G-19` | cero párrafos largos duplicados en esos cuatro | higiene |
| `G-20` | el registro `D` es una serie **continua desde `D1`, sin huecos y sin repetir**. El tope se **deriva de la última fila**: no se exige ningún `Dnn` concreto | trazabilidad · `Q-25` |
| `G-21` | `O1`–`O16` intactas frente a `7e99388`, y falla CERRADO sin Git | trazabilidad |
| `G-22` | **el inventario de inmutables se DERIVA del árbol** —todo documento numerado de `docs/evolucion/` más todos los manifiestos, menos los cuatro ficheros en corrección— y cada uno se contrasta contra `HEAD` **y** contra la revisión base. No hay ningún rango escrito, y el documento 23 nace protegido | `Q-23` · `Q-26` · protecciones 1 y 7 |
| `G-23` | lo normativo intacto y la excepción del kernel **contrastada contra la prosa del checkpoint**, que ya no enumera nada a mano; y el punto de entrada **remite** en vez de copiar | alcance · `M-06` · `R-02` |
| `G-24` | las fuentes y las fichas de `C-0.1`/`C-0.2` **se LEEN** en UTF-8 y son exactamente ésas, con el catálogo de capacidades derivado **una sola vez** y compartido con `G-15` | cobertura · `Q-27` |
| `G-25` | los cuatro macrocircuitos declaran sus **catorce** campos | `I-21` |
| `G-26` | recuentos derivados en cuatro planos, con las citas históricas reconocidas por **etiqueta estructural de región** y no por una palabra en la línea | higiene · `P-01` · `Q-04` · `Q-07` · `P-05` · protección 2 |
| `G-27` | la regla 1 de §2.6.10 usa «los cinco **CAMPOS**» | `A7` |
| `G-28` | **ningún documento de gate cambia de VEREDICTO, POLARIDAD o ESTADO en silencio**: el censo de las tres familias se deriva del documento y se contrasta contra su versión publicada | protección 8 |
| `G-29` | **topología y unicidad de TODO el corpus gobernado** —`kernel/`, `docs/rediseno/`, `docs/evolucion/`—: ninguna ampliación sin clasificar, ningún gemelo byte a byte, y ningún marcador de bloque canónico —derivado, no escrito— con sedes nuevas | `Q-02` · `M-04` · protecciones 5 y 9 |
| `G-30` | **la excepción del kernel por CONTENIDO y CLASIFICACIÓN**: cada excepción tiene clase, ningún fichero del kernel difiere de lo publicado, no queda comodín sobre el directorio de evidencia, y **la huella se RECALCULA** aquí en vez de creerse la del árbol | `Q-05` · protección 6 |
| `G-31` | **ninguna comprobación se apaga escribiendo una palabra**: las palabras gatillo se pegan al mismo dato y se exige que recuentos, polaridad, comparación de estado y marca histórica no cambien de veredicto | protección 10 |
| `G-32` | **todos** los niveles de certificación —derivados de la tabla de §9.1— tienen PRODUCTOR declarado en §9.1 y en §9.2, y la cadena de §9.2 se deriva de su propia línea | `O17` regla 12 · protección 11 |
| `G-33` | los macrocircuitos se **derivan de §8** y cada uno produce su Estructural en **FASE 0** antes de toda mutación; con **tres pruebas negativas ejecutadas**: omitir Estructural, reutilizar evidencia con una huella distinta, y elevarse sin Estructural vigente de esa ejecución | `O17` · `D107` · protecciones 12 a 15 |

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
`G-33` SON DE CONTRATO      contra un sistema. Lo que `G-33` ejecuta son las REGLAS de `O17`
                            sobre fixtures sintéticos: que el evaluador sepa decir que no.
                            Escribir el contrato de una prueba no es la prueba

NO PROTEGE CONTRA UNA       `G-29` admite un documento numerado nuevo en `docs/evolucion/`,
MARCA HISTÓRICA FALSA       porque publicarlo es el producto legítimo de un gate; y
                            `_regiones_historicas` cree a una etiqueta `[HISTÓRICO]` puesta
                            al principio de un bloque. Lo que se ha cerrado es que **una
                            palabra suelta dentro de una frase** apague un control; declarar
                            histórico un bloque entero sigue siendo posible, y es visible
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
