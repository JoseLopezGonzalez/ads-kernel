# 05 · PLAN DE IMPLEMENTACIÓN DE `F5` Y `F6`

Qué significa exactamente cada fase, qué entrega, en qué orden se construye y qué la
bloquea.

> **ESTE DOCUMENTO ES UN PLAN, y por tanto NO ES SEDE DE ESTADO.** Describe qué entrega cada
> fase, en qué orden y qué la bloquea; **no dice qué está construido y qué no**. Eso tiene
> una sola sede —[`04-CONTRATOS-TECNICOS.md`](04-CONTRATOS-TECNICOS.md) §1— y este documento
> **remite a ella**. El estado de las FASES tiene la suya, distinta:
> [`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md), y este documento **no lo repite
> ni lo modifica**.
>
> **Qué decía esta nota hasta el 2026-09-04, y por qué era falsa.** Decía «**Nada de lo que
> describe está implementado. Ninguna de sus filas se puede citar como capacidad
> existente.**» Para entonces `F6` tenía construidos, ejecutados y con evidencia publicada el
> motor de estado durable, el runtime y el dispatcher, el gobierno Git del control repo, el
> verificador de admisión, los adaptadores, la identidad, el ciclo de `§7.2`, los
> macrocircuitos y la raíz externa. Una nota de cautela que niega lo que el árbol tiene deja
> de proteger de nada: **gasta el crédito con el que después dice que algo NO está**. Por eso
> ahora remite en vez de declarar, y `T360` lo comprueba.
>
> **Lo que la nota SÍ tenía que decir, y sigue diciendo:** un plan describe alcance, no
> capacidad; y **nada de lo que este documento nombra está CERTIFICADO**, que es una
> afirmación distinta de «está construido» y sólo la puede emitir un juicio independiente.
>
> **NO FIJA CALENDARIOS.** El corpus no sostiene ninguno, y este documento no inventa uno.

---

## 1 · Qué es `F5`, exactamente

**`F5` es la fase de ENMIENDA NORMATIVA. Es la única fase con autoridad para editar material
aprobado**, y por eso todo lo que exige tocar (a), (b), sus enmiendas o un documento en voz
del Owner cae aquí.

**`F5` no construye software.** Redacta norma, la lleva al Owner y registra su aprobación.

### 1.1 · Entregables de `F5`

| # | entregable | por qué es de `F5` | autoridad |
|---|---|---|---|
| **F5-A** | **Resolver, una a una, las PRESIONES NORMATIVAS VIGENTES**: para cada una, o una enmienda aprobada, o una retirada motivada | todas viven en material APROBADO, y `F4` no puede elegir por el Owner | **el Owner**, sobre propuesta redactada |
| **F5-B** | **La sección `(g)`**: la disposición física del estado durable —ficheros, fragmentación, transacciones, event log y recuperación— aprobada como sección normativa o como enmienda que la sustituya | es la presión que **bloquea TODO el estado durable**, y por tanto casi todo `F6` | **el Owner** |
| **F5-C** | **La norma de gobierno Git del REPOSITORIO DE CONTROL**, en esa misma sección `(g)` | hoy **no tiene sede normativa**. El Owner ya resolvió DÓNDE vivirá y que su contrato derivado lo materializa `F6`; `C7` no se modifica y sigue gobernando las fuentes | **el Owner** |
| **F5-D** | **La norma que habilita la RAÍZ EXTERNA DE CONFIANZA**: identidad de escritura SEPARADA del runtime y evidencia FUERA del árbol comprobado | ninguna sede aprobada las contempla, y sin ellas uno de los contratos de `F6` está **BLOQUEADO POR DEPENDENCIA** | **el Owner** |
| **F5-E** | **Las CORRECCIONES EDITORIALES obligatorias sobre material aprobado**: una checklist verificable de restos que **no cambian ninguna norma** —una cita mal puesta, una lista mal numerada, una grafía con dos variantes y un recuento de marcas de remisión— | sólo `F5` puede tocar (b) y (a) | `F5`, con aprobación del Owner |
| **F5-F** | **La nota de vigencia en el documento de trabajo del Owner** que reconcilie su «no implementar sin diseño previo» con lo que los contratos multirrepositorio **ya implementan** | es el documento del Owner: la nota es suya | **el Owner** |
| **F5-G** | **La decisión sobre las reglas del kernel constitucional que el diseño de macrocircuitos PRESIONA** —el gate de salida del circuito de arranque, su timebox, sus entregables y sus prohibiciones— | el material aprobado **no contiene ninguna derogación válida** de esas reglas: **siguen vigentes hasta que `F5` decida regla a regla** | **el Owner** |

**El censo de presiones NO se escribe: se deriva de su única sede.**

```bash
# presiones VIGENTES (excluye las marcadas RETIRADA o FUSIONADA)
grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | grep -vc 'RETIRADA\|FUSIONADA'
# y la lista, con su identificador
grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | grep -v 'RETIRADA\|FUSIONADA'
```

**Sede única de las presiones, con qué presiona cada una, qué texto vigente, qué materia
mínima hay que aprobar, qué se puede construir sin ella y qué bloquea:**
[`11-ARQUITECTURA-INTEGRADA.md` §16](../evolucion/11-ARQUITECTURA-INTEGRADA.md).
**Sede de la checklist editorial y de los externos con propietario:** su §19.

### 1.2 · Criterios de aceptación de `F5`

```text
A1  cada presión VIGENTE tiene, o una ENMIENDA APROBADA con fecha y autoridad, o una
    RETIRADA MOTIVADA. Ninguna queda «pendiente» sin acto
A2  ninguna enmienda se aplica sin aprobación expresa del Owner, y ninguna se aplica
    silenciosamente sobre material aprobado
A3  la sección `(g)` existe, está aprobada y cubre las materias que su fuente le reservó
A4  la norma de identidad separada y evidencia externa existe, y el contrato que dependía
    de ella deja de estar BLOQUEADO POR DEPENDENCIA
A5  la checklist editorial está aplicada entera, con la prueba posterior que cada fila fija
A6  NINGÚN hallazgo vivo se declara SUPERADO por haberse redactado una enmienda
A7  la batería del corpus sigue en verde, y la huella del kernel no cambia salvo donde una
    enmienda aprobada lo ordene
```

### 1.3 · Qué NO es `F5`

```text
NO IMPLEMENTA       ni una línea de runtime, verificador, adaptador ni estado persistido
NO CERTIFICA        nada. Redactar la norma de una prueba no es la prueba
NO DESBLOQUEA       PesquerApp. La cadena pasa obligatoriamente por `F6`
```

## 2 · Qué es `F6`, exactamente

**`F6` es la fase de CONSTRUCCIÓN Y CERTIFICACIÓN.** Implementa lo que `F4c` dejó
contratado y lo que `F5` deja normado, **y lo CERTIFICA**.

### 2.1 · Entregables de `F6`

| # | entregable | sede del contrato |
|---|---|---|
| **F6-A** | **El VERIFICADOR DE ADMISIÓN**, con todos los puntos que debe demostrar: lecturas Git inequívocas y con separación segura, fallo CERRADO ante codificación inválida o truncamiento, censo derivado de lecturas, juicio sobre la MUTACIÓN y no sobre la existencia, cobertura de las seis letras de mutación, comparación de revisión base / `HEAD` / índice / árbol de trabajo, imposibilidad de que la regla de admisión se excluya a sí misma, y cero falsos verdes **y** cero falsos rojos | [`11-ARQ` §20.1](../evolucion/11-ARQUITECTURA-INTEGRADA.md) |
| **F6-B** | **La RAÍZ EXTERNA DE CONFIANZA**, con ejecutor que **no comparte identidad de escritura con el runtime**. Es obligación del Owner aceptarla o rechazarla, y es indelegable | `11-ARQ` §11.8 · resolución `O18` en la [sede canónica](../owner/ADS-OWNER-RESOLUCIONES.md) |
| **F6-C** | **El contrato de gobierno Git del REPOSITORIO DE CONTROL**, derivado de la sección `(g)` que `F5` redacta. Es un contrato NUEVO e independiente: no es el de fuentes con otro nombre, y el de fuentes no se modifica | resolución `O16`, registrada en [`DECISIONES-Y-CONTRADICCIONES.md`](../rediseno/DECISIONES-Y-CONTRADICCIONES.md) §2 |
| **F6-D** | **El RUNTIME y el DISPATCHER**: ciclo, fallos, reintentos, bloqueo, pausa, la orden de reanudación y las vistas derivadas | `11-ARQ` §7 |
| **F6-E** | **La DISPOSICIÓN FÍSICA DEL ESTADO** que `F5` apruebe: instantáneas, eventos, protocolo transaccional, concurrencia, identidad, versionado, migración y sellado | `11-ARQ` §2 |
| **F6-F** | **Los cuatro MACROCIRCUITOS** y su `FASE 0` compartida, con el contrato de conformidad estructural | `11-ARQ` §8 y §9.6 |
| **F6-G** | **La ARQUITECTURA DE ADAPTADORES**: definición neutral, proyecciones generadas, huella con validador de deriva y prueba de humo en sesión nueva | `11-ARQ` §6 |
| **F6-H** | **Los hallazgos EXTERNOS con propietario y fase `F6`**, que tocan kernel, esquemas, circuitos y pruebas | `11-ARQ` §19 |
| **F6-I** | **La guarda de versión mínima de Python en el tooling**, comprobada ANTES de correr, para que un intérprete antiguo no suba a la capa de certificación como defecto del producto | `11-ARQ` §19 |
| **F6-J** | **La CERTIFICACIÓN** de todo lo anterior, que es lo que desbloquea la primera adopción real | resolución `O20` §3, última responsabilidad |

**El censo de contratos de `F6` NO se escribe: se deriva.**

```bash
# cuántos contratos publica la sede
grep -cE '^\| `V6-[0-9]+` \|' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
# y su reparto por clasificación
grep -oE '^\| `V6-[0-9]+`.*\| (`CONTRATO_[A-Z_]+`)' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
  | grep -oE 'CONTRATO_[A-Z_]+' | sort | uniq -c
```

> **Los tres estados de un contrato, y por qué son tres:**
>
> ```text
> ESTRUCTURALMENTE COMPLETO   todos los campos tienen texto. Es el suelo, no el techo
> CONSTRUIBLE                 además es coherente consigo mismo y ejecutable con las
>                             normas VIGENTES, sin volver a decidir arquitectura
> BLOQUEADO POR DEPENDENCIA   sería construible salvo por una norma que OTRA fase tiene
>                             que emitir, DECLARADA, ENLAZADA y con condición exacta de
>                             desbloqueo
> ```
>
> **Ninguno de los tres significa implementado.** «Se puede construir» y «está construido»
> son afirmaciones distintas, y confundirlas es exactamente la deuda que sigue viva.
> Sede: `11-ARQ` §20.3.

### 2.2 · Criterios de aceptación de `F6`

```text
B1  cada contrato de la sede está IMPLEMENTADO y EJECUTADO, con su escenario positivo y su
    escenario negativo, y su evidencia publicada
B2  la suite completa da CERO FALSOS VERDES y CERO FALSOS ROJOS, medidos y publicados
B3  la raíz externa existe, la acepta el Owner, y su ejecutor NO comparte identidad de
    escritura con el runtime
B4  el verificador se incluye en su propio universo: una mutación de sí mismo o de su regla
    de admisión da ROJO
B5  ningún contrato se declara cerrado por un verde de la batería interna del corpus
B6  la certificación la emite un juicio independiente, y NO quien construyó
```

## 3 · Orden de construcción y dependencias

**El grafo es de DEPENDENCIAS, no de items. Crear items es trabajo de `F6`.** Su sede es
[`11-ARQ` §18](../evolucion/11-ARQUITECTURA-INTEGRADA.md), y esto es su lectura:

```text
  [0] ENTRADAS DE VALIDADORES        independiente · barato · PROTEGE TODO LO DEMÁS
       └─ puede ir EN PARALELO con todo lo de abajo

  [1] DISPOSICIÓN FÍSICA DEL ESTADO  ── BLOQUEADA hasta que `F5` apruebe la sección (g)
       ├─ [3] INICIATIVA Y DOSIER
       ├─ [4] CERTIFICACIÓN            [4b] el esquema de NIVEL es norma que viaja con el
       │                                    release: NO depende de [1]
       ├─ [6] SUJETO AUDITABLE Y COBERTURA
       │        └─ su APERTURA bloqueada por dos presiones de `F5`
       └─ [7] RUNTIME

  [2] CONTRATO DE ADAPTADOR Y VALIDADOR DE DERIVA   independiente del estado
  [5] PIEZAS DE PACK                                 independientes de todo

  [9] VERIFICADOR DE `F6` Y RAÍZ EXTERNA DE CONFIANZA
       `F6` lo IMPLEMENTA **y lo CERTIFICA**
       uno de sus contratos cuelga además de una norma que emite `F5`
                    │
                    │  9 → 8, y es la única arista que importa aquí
                    ▼
  [8] PRIMERA ADOPCIÓN REAL — PesquerApp
       depende de [9] IMPLEMENTADO **Y** CERTIFICADO
       su ESTADO VIGENTE y las condiciones que lo acompañan: 03-GOBIERNO-Y-AUTORIDAD.md §6
```

### 3.1 · Qué puede ir en paralelo

```text
EN PARALELO DESDE EL PRIMER DÍA   [0] entradas de validadores · [2] contrato de adaptador ·
                                  [5] piezas de pack · [4b] el esquema de nivel
EN PARALELO DENTRO DE `F5`        las presiones que NO son la de la sección (g) pueden
                                  redactarse a la vez; la de la sección (g) es la que
                                  abre el camino de [1]
EN SERIE, SIN EXCEPCIÓN           (g) aprobada → [1] → [3][4][6][7] → [9] → certificación → [8]
```

## 4 · Cortes verticales ejecutables

**Un corte vertical es un trozo que se puede construir, probar y cerrar entero, sin esperar
al resto.** Éstos son los que el grafo de dependencias permite hoy:

| corte | qué entra | qué demuestra al terminar | depende de |
|---|---|---|---|
| **V1 · Guarda de entorno** | la comprobación de versión mínima del intérprete en el tooling, antes de correr, con su código de salida y su mensaje | que un entorno insuficiente falla RUIDOSAMENTE y no como defecto del producto | nada |
| **V2 · Lectura Git segura** | el canal único de lectura de listas de rutas: separación segura, decodificación estricta, detección de truncamiento y censo derivado de invocaciones | los primeros puntos del verificador de admisión, con sus fixtures de codificación y de nombre | nada |
| **V3 · Admisión por MUTACIÓN** | el juicio sobre las seis letras de mutación, contra revisión base / `HEAD` / índice / árbol de trabajo, con las dos puntas de renombrado | que existir en la base no exime, y que confirmar no exime | V2 |
| **V4 · Auto-inclusión del instrumento** | que la definición de lo verificado y la regla de admisión no puedan excluirse a sí mismas | el punto que cierra la clase de ataque más repetida del expediente | V3 |
| **V5 · Matriz adversarial completa** | la suite entera de escenarios positivos y negativos, con su medición de falsos verdes y falsos rojos | el criterio de aceptación `B2` | V2 · V3 · V4 |
| **V6 · Raíz externa** | el ejecutor externo, su identidad separada y su evidencia fuera del árbol | el punto que hoy está BLOQUEADO POR DEPENDENCIA | **`F5`** (norma habilitante) · V5 |
| **V7 · Contrato de adaptador y huella de proyección** | definición neutral, proyección generada, huella y validador de deriva, prueba de humo en sesión nueva | el primer adaptador CERTIFICABLE | nada |
| **V8 · Estado durable mínimo** | instantánea, evento y protocolo transaccional con sus dos ramas de reanudación | que la reanudación no deja mezclas parciales publicables | **`F5`** (sección `(g)`) |

**Los cortes `V1`, `V2`, `V3`, `V4`, `V5` y `V7` no necesitan ninguna decisión nueva del
Owner.** Los cortes `V6` y `V8` sí: su norma habilitante es entregable de `F5`, **y `F5` ya
la emitió** — la sección [`(g)`](../rediseno/g-ESTADO-DURABLE-APROBADA.md), aprobada por
`O23`.

> **Y una lectura que hay que cerrar, porque el texto de arriba la permite.** **No necesitar
> una decisión del Owner NO es estar autorizado a empezar.** Los ocho cortes son trabajo de
> `F6`, y `F6` **exige `F5` CERRADA** —ver
> [`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md) §7—. Que un corte esté
> desbloqueado significa que **nada le falta para poder construirse**, no que pueda
> construirse ya.

## 5 · Qué necesita decisión del Owner y qué no

```text
NECESITA AL OWNER      toda enmienda sobre material aprobado · la sección (g) · la norma de
                       gobierno Git del control repo · la norma de identidad separada y
                       evidencia externa · la nota de vigencia en su documento de trabajo ·
                       la decisión sobre las reglas constitucionales presionadas ·
                       la ACEPTACIÓN de la raíz externa, que es indelegable ·
                       el INICIO de `F5` y el INICIO de `F6`

NO NECESITA AL OWNER   implementar un contrato ya escrito y clasificado CONSTRUIBLE ·
                       escribir sus fixtures positivos y negativos · publicar su evidencia ·
                       los cortes V1, V2, V3, V4, V5 y V7 · corregir un defecto de kernel
                       que ya tiene propietario y fase asignados
```

## 6 · Qué bloquea PesquerApp

```text
LA CADENA, Y NO ADMITE ATAJOS
  `F5` emite la norma habilitante que falta
      → `F6` IMPLEMENTA el verificador de admisión y la raíz externa de confianza
          → `F6` los CERTIFICA, con cero falsos verdes y cero falsos rojos
              → sólo entonces cabe la PRIMERA ADOPCIÓN REAL

LO QUE NO LA DESBLOQUEA
  el cierre de `F4c` · un verde de la batería interna del corpus · escribir el contrato de
  una prueba · un MVP · un piloto desechable · una adopción parcial

Y ADEMÁS
  la adopción es PERMANENTE y COMPLETA desde el primer día: el repositorio de control nace
  DEFINITIVO, y reconstruirlo después exigiría migración explícita, autoridad y evidencia
```

**Sede del bloqueo:** resolución `O20` §8 y resolución `O18`, en la
[sede canónica del Owner](../owner/ADS-OWNER-RESOLUCIONES.md). Estado vigente:
[`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md).

## 7 · Lo que este plan NO afirma

```text
NO AFIRMA que nada de F5 esté redactado · que nada de F6 esté construido · que ningún
contrato esté ejecutado · que ningún adaptador esté certificado · que exista runtime ·
que exista estado persistido · ni que ningún hallazgo vivo esté superado

Y NO FIJA plazos, sprints ni fechas: el corpus no los tiene, y este documento no los inventa
```

La deuda que sigue viva, con propietario y condición de cierre, está en
[`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](06-DEUDA-Y-LIMITACIONES-VIGENTES.md).
