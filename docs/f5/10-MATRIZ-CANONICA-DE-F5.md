# 10 · LA MATRIZ CANÓNICA DE `F5`

**Una fila por obligación de `F5`, con su estado inequívoco.** Ésta es la versión legible;
la que los controles leen es [`MATRIZ-F5.yml`](MATRIZ-F5.yml), y **las dos se escriben
juntas**.

> **QUÉ ES.** Un artefacto **DERIVADO**. Cada fila cita la sede superior de la que sale y
> **no crea autoridad**. No es norma, no es un gate y **no aprueba nada**.
>
> **LOS CENSOS DE ESTE DOCUMENTO SE DERIVAN, y se dice exactamente cuáles.** El de
> presiones lo deriva del árbol el control `F6` de [`validar-f5.py`](validar-f5.py), que se
> pone rojo si la sede crece y la matriz no la cubre. Los de entregables y criterios los
> fijan `F2` y `F3` contra una tupla cerrada. **Los demás recuentos de este documento se
> obtienen con los comandos de §4 y no se escriben aquí**: la tabla de §3 es la fuente, y
> contar sus filas a mano al lado de la propia tabla sería la clase de defecto que el corpus
> tiene abierta.

```bash
# el censo VIGENTE, derivado de su sede única
grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | grep -vc 'RETIRADA\|FUSIONADA'
# las filas de esta matriz
grep -c '^  - id: F5-OB-' docs/f5/MATRIZ-F5.yml
```

---

## 1 · El vocabulario de estados, y por qué es cerrado

**Toda fila queda ubicada en exactamente uno.** No existe una categoría vaga como
«pendiente»: una obligación sin ubicación inequívoca **es el defecto**, y el control `F5`
del validador lo comprueba contra el vocabulario declarado.

```text
DETERMINADO_Y_EJECUTABLE                        la autoridad vigente fija un único
                                                resultado, y F5 puede ejecutarlo sin acto
                                                nuevo del Owner
BORRADOR_DETERMINADO_PENDIENTE_DE_APROBACIÓN    el contenido técnico es único y está
                                                preparado, pero el Owner debe ratificarlo
ELECCIÓN_REAL_DEL_OWNER                         existen dos o más salidas legítimas y
                                                ninguna autoridad vigente impone una
BLOQUEADO_POR_OTRA_DECISIÓN                     no puede cerrarse hasta resolver otra
                                                decisión del mismo paquete
DEUDA_DE_F6                                     no pertenece a F5 y no se implementa ahora
FUERA_DE_ALCANCE                                no pertenece a F5 ni bloquea sus entregables
```

### 1.1 · Por qué NINGUNA fila de presión es `DETERMINADO_Y_EJECUTABLE`

**Y es un resultado, no un descuido.** El criterio de aceptación `A2` lo impide por
definición: «ninguna enmienda se aplica sin aprobación expresa del Owner, y ninguna se
aplica silenciosamente sobre material aprobado». **Todas las presiones vigentes viven en
material APROBADO.** Luego lo determinado puede ser el **contenido**; **el acto nunca lo
es**.

**Lo `DETERMINADO_Y_EJECUTABLE` de este macrobloque no son las presiones: es la
infraestructura de `F5`** —el estado de fase, esta matriz, la estructura de trabajo, la
trazabilidad y los controles—, y está **ejecutado**, no pendiente.

---

## 2 · Los siete entregables y sus siete criterios

| entregable | qué es | autoridad | filas |
|---|---|---|---|
| **`F5-A`** | resolver, una a una, las presiones vigentes | el Owner, sobre propuesta redactada | `OB-05`…`OB-17`, `OB-23` |
| **`F5-B`** | la sección `(g)`: disposición física del estado durable | el Owner | `OB-01` |
| **`F5-C`** | el gobierno Git del control repo, dentro de `(g)` | el Owner | `OB-02` |
| **`F5-D`** | la norma que habilita la raíz externa de confianza | el Owner | `OB-03` |
| **`F5-E`** | las correcciones editoriales sobre material aprobado | `F5`, con aprobación del Owner | `OB-16`, `OB-18`…`OB-21` |
| **`F5-F`** | la nota de vigencia en el documento de trabajo del Owner | el Owner | `OB-22` |
| **`F5-G`** | las reglas constitucionales presionadas por los macrocircuitos | el Owner | `OB-04` |

**Los siete criterios de aceptación**, con la evidencia que los haría verificables:

| | criterio | evidencia prevista |
|---|---|---|
| `A1` | cada presión vigente tiene enmienda aprobada o retirada motivada; ninguna queda pendiente sin acto | barrido que derive el censo vigente y exija, para **cada** identificador, un acto con fecha y autoridad |
| `A2` | ninguna enmienda sin aprobación expresa, y ninguna silenciosa sobre material aprobado | por cada cambio en material aprobado, que el acto cite una resolución que exista en la sede canónica, comprobada contra su **nacimiento** |
| `A3` | `(g)` existe, está aprobada y cubre las materias que su fuente le reservó | la lista de materias reservadas, cerrada por el acto del Owner, contrastada apartado a apartado |
| `A4` | la norma de identidad separada y evidencia externa existe, y el contrato deja de estar bloqueado | que el contrato pase a construible **sin que ningún otro campo de su fila cambie**, más la prueba negativa de atestación externa |
| `A5` | la checklist editorial aplicada entera, con la prueba que cada fila fija | las cuatro pruebas posteriores, una por fila, ejecutadas |
| `A6` | ningún hallazgo vivo se declara superado por haberse redactado una enmienda | que el censo de hallazgos vivos **no encoja**, y que las deudas mayores sigan en su estado |
| `A7` | la batería sigue en verde y la huella del kernel no cambia salvo donde una enmienda lo ordene | el runner canónico con código cero, los controles negativos, y la huella comparada — **registrando la versión de intérprete usada** |

> **Cautela declarada sobre `A7`.** El corpus advierte que con un intérprete antiguo varias
> comprobaciones fallan **por el entorno y no por el producto**, y que el runner
> correctamente no republica esa evidencia, de modo que la cobertura publicada puede quedar
> describiendo un corpus anterior. La guarda que lo impediría es **contrato y no código**, y
> es de `F6`. Por eso un verde de `A7` debe registrar con qué intérprete se obtuvo.

---

## 3 · La matriz

**`D` = decisión del Owner necesaria.**

### 3.1 · Las obligaciones de `F5`

| id | entr. | presión | resultado exigido | dependencia | D | estado | decisión |
|---|---|---|---|---|---|---|---|
| `OB-01` | `F5-B` | `PN-1` | aprobar la disposición física del estado durable como sección `(g)`, o como enmienda que la sustituya | — | **SÍ** | **ELECCIÓN_REAL_DEL_OWNER** | `D-01` |
| `OB-02` | `F5-C` | `PN-11` | un apartado de `(g)` con la tabla de propiedad del control repo y sus decisiones | `OB-01` | **SÍ** | **BLOQUEADO_POR_OTRA_DECISIÓN** | `D-01` |
| `OB-03` | `F5-D` | `PN-19` | una sede que fije identidad de escritura separada, dónde vive la evidencia externa y quién la custodia | — | **SÍ** | **ELECCIÓN_REAL_DEL_OWNER** | `D-02` |
| `OB-04` | `F5-G` | `PN-15` | decidir regla a regla qué se conserva, ajusta o sustituye de las cuatro reglas constitucionales | — | **SÍ** | **ELECCIÓN_REAL_DEL_OWNER** | `D-04` |
| `OB-05` | `F5-A` | `PN-2` | reconocer la política de recurrencia como fuente de trabajo, con alcance, presupuesto y revocación | `OB-06` | **SÍ** | **ELECCIÓN_REAL_DEL_OWNER** | `D-05` |
| `OB-06` | `F5-A` | `PN-3` | ajustar la regla de ejecución desatendida al alcance exacto que la política autoriza | `OB-05` | **SÍ** | **ELECCIÓN_REAL_DEL_OWNER** | `D-05` |
| `OB-07` | `F5-A` | `PN-6` | confirmar qué significa «Integrada» | — | **SÍ** | BORRADOR_DETERMINADO_PENDIENTE_DE_APROBACIÓN | `R-01` |
| `OB-08` | `F5-A` | `PN-7` | distinguir lo publicado de lo especulativo en la reanudación | acopl. `OB-01` | **SÍ** | BORRADOR_DETERMINADO_PENDIENTE_DE_APROBACIÓN | `R-01` |
| `OB-09` | `F5-A` | `PN-9` | confirmar que consumir el resultado no redefine el dominio | — | **SÍ** | BORRADOR_DETERMINADO_PENDIENTE_DE_APROBACIÓN | `R-01` |
| `OB-10` | `F5-A` | `PN-10` | confirmar la lectura de «estado durable» de la iniciativa | — | **SÍ** | BORRADOR_DETERMINADO_PENDIENTE_DE_APROBACIÓN | `R-01` |
| `OB-11` | `F5-A` | `PN-8` | añadir verificación como condicional de la ruta de auditoría, o nombrar otro productor | `OB-12`·`OB-13` | **SÍ** | **ELECCIÓN_REAL_DEL_OWNER** | `D-06` |
| `OB-12` | `F5-A` | `PN-13` | admitir dominio, seguridad y diseño en los dos procesos, o sacar el descubrimiento de ese paso | `OB-11`·`OB-13` | **SÍ** | **ELECCIÓN_REAL_DEL_OWNER** | `D-07` |
| `OB-13` | `F5-A` | `PN-14` | sustituir el método por la capacidad en los dos puntos aprobados, o declarar la equivalencia | `OB-11`·`OB-12` | **SÍ** | **ELECCIÓN_REAL_DEL_OWNER** | `D-09` |
| `OB-14` | `F5-A` | `PN-12` | confirmar que el mapa documental se satisface derivado, o exigirlo escrito | — | **SÍ** | **ELECCIÓN_REAL_DEL_OWNER** | `D-10` |
| `OB-15` | `F5-A` | `PN-17` | declarar qué significa «registrar» al agotar reintentos, y quién es su productor | — | **SÍ** | **ELECCIÓN_REAL_DEL_OWNER** | `D-03` |
| `OB-16` | `F5-E` | `PN-16` | declarar la grafía canónica del primer identificador | `OB-17` | **SÍ** | **ELECCIÓN_REAL_DEL_OWNER** | `D-08` |
| `OB-17` | `F5-A` | `PN-18` | declarar la grafía canónica del segundo identificador | `OB-16` | **SÍ** | **ELECCIÓN_REAL_DEL_OWNER** | `D-08` |
| `OB-18` | `F5-E` | — | corregir la cita a un predicado equivocado | — | **SÍ** | BORRADOR_DETERMINADO_PENDIENTE_DE_APROBACIÓN | `R-02` |
| `OB-19` | `F5-E` | — | renumerar una lista sin tocar una palabra de su texto | tras `OB-11`…`OB-13` | **SÍ** | BORRADOR_DETERMINADO_PENDIENTE_DE_APROBACIÓN | `R-02` |
| `OB-20` | `F5-E` | — | reanclar el recuento de marcas de remisión, sustituyendo el cardinal por su derivación | — | **SÍ** | BORRADOR_DETERMINADO_PENDIENTE_DE_APROBACIÓN | `R-02` |
| `OB-21` | `F5-E` | — | hacer coincidir el inventario de enmiendas vigentes entre sus sedes | — | **SÍ** | BORRADOR_DETERMINADO_PENDIENTE_DE_APROBACIÓN | `R-02` |
| `OB-22` | `F5-F` | — | la nota de vigencia, cubriendo las cuatro afirmaciones equivalentes | — | **SÍ** | BORRADOR_DETERMINADO_PENDIENTE_DE_APROBACIÓN | `R-03` |
| `OB-23` | `F5-A` | — | inscribir las respuestas en la sede canónica append-only del Owner | todas | **SÍ** | **BLOQUEADO_POR_OTRA_DECISIÓN** | `R-04` |

### 3.1 bis · Obligaciones de `F5` que NO necesitan al Owner

**Su fase declarada es `F5` en la sede de deuda viva, y ninguna exige acto del Owner**: sus
sedes son DERIVADAS, no material aprobado. **Ninguna se ejecuta en este macrobloque**, y la
matriz declara fila a fila por qué.

| id | qué exige | propietario | estado | por qué NO se ejecuta aquí |
|---|---|---|---|---|
| `OB-24` | que una enumeración viva retire su lista y remita | `SIS` | DETERMINADO_Y_EJECUTABLE | el encargo ordena **mantener los diez hallazgos vivos en su estado**, y su cierre exige un acto competente que este macrobloque no emite |
| `OB-25` | que una proyección conserve la precondición o remita | `SIS` | DETERMINADO_Y_EJECUTABLE | ídem |
| `OB-26` | que un comando publicado reproduzca el resultado que anota | `SIS` | DETERMINADO_Y_EJECUTABLE | ídem |
| `OB-27` | que dos campos vigentes retiren sus cardinales y remitan | `SIS` | DETERMINADO_Y_EJECUTABLE | ídem, y son instancias de la clase que **sólo un gate independiente posterior** puede cerrar |
| `OB-28` | la **especificación** de la regla de alcance de rótulo y de la guarda de truncamiento | `SIS` en `F5` · `PLT` el instrumento en `F6` | DETERMINADO_Y_EJECUTABLE | ídem. Y redactar la especificación **no cierra el hallazgo**: declararlo cerrado por haberla redactado violaría `A6` |
| `OB-29` | la **especificación** de la regla de clase contra recuentos copiados | `SIS` en `F5` · `PLT` el instrumento en `F6` | DETERMINADO_Y_EJECUTABLE | ídem. Su condición de cierre es expresamente ajena a `F5`: **barrer no es certificar** |
| `OB-30` | la deuda del corpus canónico cuya fase declarada es `F5` | `SIS` | DETERMINADO_Y_EJECUTABLE | el encargo **lo prohíbe** salvo tres condiciones concurrentes, y ninguna se cumple respecto de los artefactos de este macrobloque |
| `OB-31` | **quién cierra `F5`** — ninguna sede vigente lo declara | Owner | **ELECCIÓN_REAL_DEL_OWNER** | es `R-05`, y va al Owner |

> **Por qué estas ocho filas existen, dicho contra el interés de quien escribe.** La primera
> versión de esta matriz **no las tenía**, y afirmaba «una fila por obligación de `F5`». Era
> falso: la sede de deuda viva asigna fase `F5` a todas ellas, y sin fila `F5` podría
> cerrarse en verde dejándolas huérfanas entre una fase cerrada y otra que sólo tiene
> asignado el instrumento. **Ninguna se declara superada, y ninguna se ha tocado.**

### 3.2 · Las filas de frontera · lo que NO es de `F5`

**Se declaran para que la separación sea explícita y comprobable, y para que nadie las
arrastre a `F5` por conveniencia.**

| id | qué es | estado | por qué no es de `F5` |
|---|---|---|---|
| `OB-F1` | los externos con propietario y fase `F6`, y la mitad `F6` del que `F5` abre | **DEUDA_DE_F6** | su fase declarada es `F6`. `F5` toca la fuente; `F6` toca el derivado |
| `OB-F2` | los diecinueve contratos de `F6`, uno de ellos bloqueado por dependencia | **DEUDA_DE_F6** | `F5` sólo emite la norma habilitante del bloqueado, que es `OB-03` |
| `OB-F3` | la guarda de versión de intérprete, y la deuda que bloquea `F6` y la adopción | **DEUDA_DE_F6** | las dos son de `F6`, y **ninguna se declara superada aquí** |
| `OB-F4` | las dos decisiones del Owner expresamente DEFERIDAS | **FUERA_DE_ALCANCE** | siguen deferidas y sin fase asignada. Este paquete **no las reabre** |
| `OB-F5` | la deuda del corpus canónico cuya fase declarada es **`F6`** | **FUERA_DE_ALCANCE** | son de `F6`. Las tres cuya fase es `F5` **no están aquí**: tienen fila propia, `OB-30`. Ninguna se declara superada, y **no se abre tanda para corregirlas** |

---

## 4 · Cobertura, y cómo se comprueba

**Ninguna de estas cifras se escribe aquí: se obtiene ejecutando su comando.**

```bash
# el censo VIGENTE de presiones, derivado de su sede única
grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | grep -vc 'RETIRADA\|FUSIONADA'
# las filas de la matriz, y su reparto por estado
python3 docs/f5/validar-f5.py
# las decisiones que el paquete plantea
grep -cE '^## `[DR]-[0-9]{2}`' docs/f5/20-PAQUETE-DE-DECISIONES-DEL-OWNER.md
# los borradores, todos NO APROBADOS
grep -lr 'ESTADO-DEL-BORRADOR: NO_APROBADO' docs/f5/borradores/ | wc -l
```

**Y lo que sí se afirma, porque un control lo sostiene y no una cifra:**

```text
PRESIONES VIGENTES        TODAS tienen fila. Lo deriva del árbol el control F6, que falla
                          si la sede crece y la matriz se queda atrás
ENTREGABLES               los siete, con al menos una fila. Control F2
CRITERIOS                 los siete, declarados. Control F3
DECISIONES                el paquete y la matriz se cubren en LOS DOS SENTIDOS. Control F8:
                          una pregunta sin obligación detrás es una pregunta inventada, y
                          una obligación sin pregunta es una obligación que nadie contesta
FILAS SIN PROPIETARIO     ninguna
FILAS SIN UBICAR          ninguna. El vocabulario de estados es cerrado. Control F5
```

---

## 5 · Lo que esta matriz NO afirma

```text
NO AFIRMA   que ninguna presión esté resuelta. NINGUNA lo está
NO AFIRMA   que ninguna enmienda esté redactada como norma. Hay BORRADORES, no enmiendas
NO AFIRMA   que el Owner haya respondido nada
NO AFIRMA   que ningún hallazgo vivo esté superado
NO AFIRMA   que nada de F6 esté construido, ejecutado ni certificado
```
