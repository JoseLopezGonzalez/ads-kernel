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

## 3 · La matriz, después de `O23`

**Las quince decisiones están resueltas.** Ninguna fila espera ya al Owner.

### 3.1 · Reparto de estados

```text
APLICADO_POR_O23        24   la decisión existe, y su artefacto también
EJECUTADO_EN_F5          7   trabajo que no necesitaba al Owner, hecho en esta fase
DEUDA_DE_F6              3   frontera declarada: no pertenece a F5
FUERA_DE_ALCANCE         2   ídem
```

**El reparto NO se escribe: se deriva** con `python3 docs/f5/validar-f5.py`.

### 3.2 · Las obligaciones, por entregable

| entregable | filas | artefacto que lo completa |
|---|---|---|
| **`F5-A`** | `OB-05`…`OB-17`, `OB-23`…`OB-31` | [`E3`](../rediseno/a-ENMIENDA-E3-ARRANQUE-Y-POLITICA.md) · [`E4`](../rediseno/a-ENMIENDA-E4-COMPOSICION-DE-RUTAS.md) · [`E6`](../rediseno/a-ENMIENDA-E6-REANUDACION.md) · `O23` §7–§10 · el [acta de disposición](40-DISPOSICION-DE-LAS-PRESIONES.md) |
| **`F5-B`** | `OB-01` | la sección [`(g)`](../rediseno/g-ESTADO-DURABLE-APROBADA.md), `g.0`–`g.18` |
| **`F5-C`** | `OB-02` | `(g)` `g.14` |
| **`F5-D`** | `OB-03` | `(g)` `g.15` |
| **`F5-E`** | `OB-16`, `OB-18`…`OB-21` | [`E5`](../rediseno/a-ENMIENDA-E5-CORRECCIONES-EDITORIALES.md) · `O23` §8 |
| **`F5-F`** | `OB-22` | la nota de vigencia en [el documento de trabajo del Owner](../owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md), en sus **cuatro** sedes |
| **`F5-G`** | `OB-04` | `E3` `E3.1`, con **una fila por regla** |

### 3.3 · Las siete que no necesitaban al Owner, y qué cerraron de verdad

**Ésta es la columna que importa, y se dice sin adornarla.**

| fila | qué se hizo | ¿cierra el hallazgo? |
|---|---|---|
| `OB-24` | la viñeta retiró su enumeración y remite | **CONDICIÓN CUMPLIDA.** El cierre lo adjudica su sede, que lo sigue publicando VIVO |
| `OB-25` | la entrada recuperó la precondición | **CONDICIÓN CUMPLIDA**, ídem |
| `OB-26` | el comando publicado reproduce lo que anota | **CONDICIÓN CUMPLIDA**, ídem |
| `OB-27` | los tres campos retiraron sus cardinales | **NO.** Su instrumento es de `F6`, y son instancias de una clase que **sólo un gate independiente posterior** puede cerrar |
| `OB-28` | la especificación, en [`50-…`](50-ESPECIFICACIONES-DE-INSTRUMENTO.md) `ESP-1` y `ESP-2` | **NO.** El instrumento es de `F6` |
| `OB-29` | la especificación de clase, `ESP-3` | **NO, y su cierre no es de `F5` ni de `F6`** |
| `OB-30` | el cardinal deja de anclar dos comandos publicados | **NO.** Las seis siguen registradas |

**NINGUNA de las siete cierra su hallazgo, y eso es lo correcto.** Tres CUMPLEN su condición
de cierre y cuatro ni siquiera eso —su instrumento es de `F6`, o su cierre es de un gate—.
**Cumplir una condición no es cerrar un hallazgo:** el cierre lo adjudica su sede, y declararlo
aquí por haber cambiado un texto es exactamente lo que `A6` prohíbe.

### 3.4 · Las filas de frontera · lo que NO es de `F5`

| id | qué es | estado |
|---|---|---|
| `OB-F1` | los externos con fase `F6` | **DEUDA_DE_F6** |
| `OB-F2` | los diecinueve contratos de `F6`, **ninguno implementado** | **DEUDA_DE_F6** |
| `OB-F3` | la guarda de entorno y la deuda que bloquea la adopción | **DEUDA_DE_F6** |
| `OB-F4` | las dos decisiones DEFERIDAS | **FUERA_DE_ALCANCE** |
| `OB-F5` | la deuda del corpus canónico con fase `F6` | **FUERA_DE_ALCANCE** |

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
NO AFIRMA   que ningún hallazgo vivo esté cerrado. Tres CUMPLEN su condición de cierre, y
            el cierre lo adjudica su sede, no esta matriz
NO AFIRMA   que ninguna norma esté IMPLEMENTADA. `F5` emite norma; construir es `F6`
NO AFIRMA   que `F5` esté cerrada. Su cierre exige un acto posterior y expreso del Owner
NO AFIRMA   que ningún hallazgo vivo esté superado
NO AFIRMA   que nada de F6 esté construido, ejecutado ni certificado
```
