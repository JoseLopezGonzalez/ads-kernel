# 03 · GOBIERNO Y AUTORIDAD

Quién manda sobre qué, qué es vigente y qué es evidencia, y en qué estado exacto está cada
fase. **Este documento es la ÚNICA sede del estado de las fases dentro del corpus
canónico.**

Antes: [`02-MODELO-OPERATIVO.md`](02-MODELO-OPERATIVO.md).

---

## 1 · La jerarquía de autoridad

**De mayor a menor. Cuando dos fuentes difieren, manda la de arriba.**

| # | nivel | qué es | dónde vive |
|---|---|---|---|
| 1 | **RESOLUCIONES DEL OWNER** | la autoridad canónica. Palabras emitidas o ratificadas por el Owner, íntegras y no en resumen | [`docs/owner/ADS-OWNER-RESOLUCIONES.md`](../owner/ADS-OWNER-RESOLUCIONES.md) |
| 2 | **MATERIAL APROBADO** | la especificación normativa que el Owner aprobó: (a) capacidades y (b) recorrido, con sus enmiendas `E1` y `E2`, y la arquitectura multirrepositorio aprobada | [`docs/rediseno/`](../rediseno/README.md) · [`docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md`](../owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md) |
| 3 | **CONTRATOS Y ESQUEMAS DEL KERNEL** | la instanciación ejecutable del nivel 2. Lo amplía y lo cita; **no lo contradice** | [`kernel/operativo/`](../../kernel/operativo/00-INDICE.md) |
| 4 | **ARQUITECTURA ENTREGADA POR `F4c`** | el diseño integrado, los contratos de `F6` y las presiones normativas para `F5`. **Es DERIVADA**: donde proyecta una resolución, manda la resolución | [`11-ARQUITECTURA-INTEGRADA.md`](../evolucion/11-ARQUITECTURA-INTEGRADA.md) |
| 5 | **PROYECCIONES Y REGISTROS DERIVADOS** | el registro de decisiones, los índices, los checkpoints y las vistas. **Una paráfrasis nunca amplía la autoridad del texto canónico** | [`DECISIONES-Y-CONTRADICCIONES.md`](../rediseno/DECISIONES-Y-CONTRADICCIONES.md) · [`00-INDICE.md`](../evolucion/00-INDICE.md) · [`CHECKPOINT-ADS-NEXT.md`](../evolucion/CHECKPOINT-ADS-NEXT.md) |
| — | **EVIDENCIA DE PROCESO** | gates, dictámenes, manifiestos, corrigenda y salidas de validador. **NO es normativa en ningún grado** | [`docs/evolucion/`](../evolucion/00-INDICE.md) · `kernel/operativo/pruebas/evidencia/` |

**Este corpus canónico ocupa el nivel 3 en su función editorial**: consolida, clasifica y
enlaza. **No crea autoridad.** Si algo de aquí contradijera a un nivel superior, el defecto
está aquí.

## 2 · Las resoluciones del Owner, y por qué son APPEND-ONLY

```text
LA SEDE          docs/owner/ADS-OWNER-RESOLUCIONES.md, creada por la propia resolución que
                 ordenó crearla, porque el corpus había perdido la capacidad de comprobar
                 qué había dicho el Owner

APPEND-ONLY      las entradas NO se editan ni se borran. Una resolución posterior REVISA a
                 la anterior sin borrarla, y la anterior se conserva

CADA ENTRADA     identificador · fecha · procedencia · texto · alcance · relaciones de
                 revisión

LA PROYECCIÓN    el registro de decisiones es una PROYECCIÓN DERIVADA. Ninguna paráfrasis
                 sustituye a la sede, y ninguna puede ampliar su autoridad

CÓMO NACE UNA    primero se materializa en la sede, con su texto completo; después se
                 proyecta; la proyección ENLAZA a la resolución canónica
```

**Qué contiene la sede NO se enumera aquí: se deriva.**

```bash
grep -oE '^# `O[0-9]+`' docs/owner/ADS-OWNER-RESOLUCIONES.md
```

> **Las resoluciones anteriores a la creación de la sede no se reconstruyen ni se
> inventan.** Se conservan en su registro histórico —sección 2 de
> [`DECISIONES-Y-CONTRADICCIONES.md`](../rediseno/DECISIONES-Y-CONTRADICCIONES.md)— hasta
> que exista una ratificación expresa o una fuente primaria verificable. Es una orden del
> Owner y se cumple literalmente: **un implementador que necesite una de ellas la lee ahí,
> y sabe que su procedencia es un registro y no la sede.**

**Comprobación mecánica del carácter append-only**, que ya ejecuta la batería del corpus:
el contenido de hoy tiene que **empezar por** el contenido de la versión que creó el
fichero, derivada de la historia. La referencia **no es `HEAD`: es el nacimiento**, de modo
que confirmar una alteración no la vuelve legítima.

## 3 · Vigente, histórico y evidencia

```text
VIGENTE      describe el sistema tal como es HOY, y se puede citar para construir.
             Son los niveles 1 a 4 de la jerarquía, y este corpus canónico.

HISTÓRICO    describe un estado ANTERIOR. Puede contener frases que hoy son falsas, y eso
             NO es un defecto mientras su carácter histórico sea inequívoco y quede fuera
             del camino de implementación. No se edita para «arreglarlo»: se rotula.

EVIDENCIA    registra QUÉ SE COMPROBÓ, POR QUIÉN y CON QUÉ RESULTADO, en una fecha, sobre
             un árbol concreto. Es inmutable por diseño. **No dice qué hay que construir.**

DERIVADA     se REGENERA desde una fuente canónica. Editarla a mano es el defecto.
             Ejemplos: los recuentos generados, el registro de pruebas y la evidencia de
             los validadores.
```

**La clasificación fichero a fichero está en
[`FUENTES-CANONICAS.yml`](FUENTES-CANONICAS.yml)**, que es su única sede y es validable
mecánicamente.

## 4 · Gates, revisiones y manifiestos — qué son y qué alcance tienen

**Un gate de `F4c` es un juicio independiente sobre un árbol concreto, en una fecha
concreta.** Su aparato es: un **manifiesto de ASIGNACIÓN** publicado antes de que exista
ningún revisor · **manifiestos de LECTURA** por revisor, declarados contra su propio
interés · revisores en paralelo que no se ven · un **adjudicador** que no resuelve por
mayoría · y un **sobre de ancla** externo al árbol, recibido antes de leer.

```text
LO QUE UN GATE PRODUCE     un VEREDICTO sobre una candidata, una declaración de COBERTURA,
                           y una lista de hallazgos con sede, severidad y remedio

LO QUE UN GATE NO PRODUCE  norma. Un gate no decide arquitectura, no crea contratos, no
                           enmienda material aprobado y no habla del futuro
```

### 4.1 · REGLA ANTI-NORMATIVIDAD DE LOS GATES

> **Ningún documento de gate, dictamen, manifiesto, corrigendum o checkpoint puede
> invocarse como fuente normativa para implementar.**
>
> **Ni siquiera cuando dice algo verdadero.** Si un gate afirma una obligación, esa
> obligación tiene una sede en los niveles 1 a 4 de §1, y **es esa sede la que se cita y la
> que manda**. Si no la tiene, entonces la obligación no existe todavía y quien la necesite
> la lleva al Owner como decisión nueva.
>
> **Consecuencias prácticas, y son tres:**
>
> ```text
> 1  un implementador NO necesita leer ningún gate, y este corpus lo demuestra enlazando
>    cada obligación a su sede de nivel 1 a 4
> 2  un hallazgo VIVO no vive en el gate que lo encontró como norma, sino en
>    06-DEUDA-Y-LIMITACIONES-VIGENTES.md como DEUDA, con su sede de evidencia citada
> 3  un verde de la batería interna NO demuestra que nada esté construido ni certificado, y
>    nadie puede citarlo para eso
> ```
>
> **Por qué existe esta regla:** el expediente de `F4c` consumió doce gates, y en varios de
> ellos el aparato del propio gate cometió el defecto que ese gate existía para verificar.
> Un aparato de verificación que se convierte en fuente de verdad reintroduce por la puerta
> de atrás la circularidad que el Owner cerró dos veces —una para el MECANISMO y otra para
> la FASE—.

## 5 · Reglas Git y protección de materiales

```text
HISTORIA          lineal. No se hace amend, rebase, squash, reset, merge, cherry-pick ni
                  force sobre material publicado

PUBLICACIÓN       cada trabajo se publica en una referencia `review/...` NUEVA, con refspec
                  explícito. Una referencia publicada no se reescribe

SEDE DEL OWNER    APPEND-ONLY, comprobado contra el COMMIT QUE LA CREÓ y no contra `HEAD`

DOCUMENTOS        los documentos numerados de gate, los manifiestos publicados y los
INMUTABLES        dictámenes NO se editan nunca. Un error de hecho en uno de ellos se
                  ACOTA en el corrigendum de dictámenes inmutables, que existe para eso

MATERIAL          (a), (b), `E1`, `E2` y la arquitectura multirrepositorio aprobada sólo se
APROBADO          modifican por enmienda, y la fase con autoridad para editarlos es `F5`

KERNEL, PACKS     su modificación cambia la HUELLA y la detecta `kernel-status.sh`. Editar
Y TOOLING         un validador para relajar una regla sería un fork invisible, y por eso
                  los validadores entran en la huella

ADMISIÓN          una AMPLIACIÓN del corpus —un fichero nuevo— sólo es legítima si su zona
                  la clasifica con una condición EJECUTADA. Confirmar un fichero NO lo
                  exime de la condición de su zona
```

**La zona `docs/canonico/` se admite bajo esa misma disciplina**, y su condición es que
**cada fichero esté enlazado por su ruta completa desde
[`docs/evolucion/00-INDICE.md`](../evolucion/00-INDICE.md)**. Un fichero plantado en
`docs/canonico/` sin ese enlace es rojo.

## 6 · ESTADO VIGENTE DE LAS FASES

> **ÉSTA ES LA ÚNICA SEDE DEL ESTADO DE FASE DENTRO DEL CORPUS CANÓNICO.** Ningún otro
> documento de `docs/canonico/` lo copia. Su fuente es el acto que lo declaró, citado en
> cada fila.

| fase u objeto | estado | quién lo declaró |
|---|---|---|
| **`F4c`** | **CERRADA**, por COMPOSICIÓN: un gate completo VÁLIDO más una verificación incremental del delta con LECTURA INTEGRAL COMPLETA. **No la cerró el coordinador**: la cierra la composición de dos juicios independientes | [`34-RATIFICACION-DE-LA-CERTIFICACION-INCREMENTAL-O22.md`](../evolucion/34-RATIFICACION-DE-LA-CERTIFICACION-INCREMENTAL-O22.md) §10, sobre [`33-CIERRE-DE-F4C-POR-COMPOSICION-O22.md`](../evolucion/33-CIERRE-DE-F4C-POR-COMPOSICION-O22.md) |
| **`F5`** | **INICIADA · EN CURSO.** El Owner emitió el acto de inicio, que la autorización documental no sustituía. Su área de trabajo, su matriz de obligaciones y su paquete único de decisiones están preparados; **ninguna presión está resuelta y ninguna enmienda está aprobada** | el acto del Owner, registrado en [`docs/f5/01-ACTO-DE-INICIO-DE-F5.md`](../f5/01-ACTO-DE-INICIO-DE-F5.md). La autorización previa: [`34-RATIFICACION-…`](../evolucion/34-RATIFICACION-DE-LA-CERTIFICACION-INCREMENTAL-O22.md) §10 |
| **`F6`** | **NO INICIADA.** Su contrato está ESCRITO; **ninguno de sus puntos está implementado, ejecutado ni certificado** | ídem |
| **PesquerApp** | **BLOQUEADA.** Sin MVP, sin piloto desechable y sin adopción parcial, hasta que `F6` implemente **y CERTIFIQUE** sus contratos. El cierre de `F4c` **no la desbloquea** | resolución del Owner `O20` §8, en la [sede canónica](../owner/ADS-OWNER-RESOLUCIONES.md) |
| **`C-L.5`** | **CERTIFICADA** para el gate del documento 32 por su adjudicador, y **CERTIFICADA POR DELTA** para la candidata del delta. **No se transfiere** a ninguna otra candidata ni a ningún otro gate | `O21` §5 y §6 · `O22` §5 |
| **`C-L.7`** | **NO CERRADA** | doc 34 §10 · ver [`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](06-DEUDA-Y-LIMITACIONES-VIGENTES.md) |
| **`M-04`** | **NO SUPERADA** | ídem |

**Y tres cosas que el cierre de `F4c` expresamente NO hizo:**

```text
NO DECLARÓ SUPERADO NADA    ni un hallazgo vivo, ni `M-04`, ni `C-L.7`
NO REVISÓ NINGUNA           las resoluciones conservan íntegro su texto, y la sede sigue
RESOLUCIÓN DEL OWNER        siendo APPEND-ONLY
NO ABRIÓ OTRO CICLO         no se convoca otro gate y no se propone otra tanda de
                            corrección
```

## 7 · Qué cambia el estado de una fase

```text
INICIAR `F5`        es un acto del OWNER, y **ya se emitió**. Ningún documento, ningún
                    corpus y ningún agente lo sustituía, y ninguno lo sustituyó: el acto
                    consta y está registrado. Su estado vigente es §6

INICIAR `F6`        exige `F5` cerrada. Los contratos de `F6` están escritos y no
                    implementados

DESBLOQUEAR         exige que `F6` implemente **y CERTIFIQUE** el verificador de admisión y
PesquerApp          la raíz externa de confianza. La cadena es
                    `F6` → certificación → adopción, y no admite atajos

CERRAR UN HALLAZGO  exige un ACTO COMPETENTE que lo declare. Ni este corpus, ni una tanda
                    de corrección, ni un verde de la batería cierran nada por sí mismos
```

## 8 · Contradicciones conocidas que siguen abiertas, y quién las resuelve

**Existe una contradicción REGISTRADA entre dos documentos de `docs/owner/`** sobre la misma
pregunta multirrepositorio: uno es **decisión aprobada para implementación** y el otro es
**documento de trabajo** que declara materia abierta. **No se resuelve por lectura**, está
registrada con las dos posturas escritas en
[`07-DECISION-MULTIREPO.md`](../evolucion/07-DECISION-MULTIREPO.md), y **su reconciliación
tiene propietario declarado —el Owner— y está inscrita como deuda** en
[`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](06-DEUDA-Y-LIMITACIONES-VIGENTES.md).

**No es una contradicción entre dos autoridades superiores vigentes**: la precedencia está
resuelta y consta —manda la decisión aprobada, y `C6` y `C7` son su instanciación—; lo que
queda vivo es una **nota de vigencia pendiente** en el documento de trabajo, no una
elección sin hacer.
