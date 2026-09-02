# SECCIÓN (b) — RECORRIDO, ESTADOS Y COMPOSICIÓN DE PROCESOS

> **ESTADO: APROBADA** por el Owner el 2026-08-25.
> No se ha modificado `kernel/` ni `packs/`. La sección (a) permanece intacta.
> Con (a) + (b) queda aprobada una **especificación mínima para construir el kernel**
> —catálogo de capacidades, custodia, concurrencia, frenos, recorrido, estados y
> transiciones—, **no un kernel construido**. Las pruebas `T26-T74` son contratos de
> conformidad definidos, no ejecutados.

> ## ENMIENDAS VIGENTES — leer junto a este documento
>
> Este texto **no se reescribe**. Lo que rige es esta sección **leída junto a sus
> enmiendas**, que sustituyen puntos concretos por decisión posterior del Owner.
>
> | | enmienda | fecha | qué sustituye |
> |---|---|---|---|
> | **E2** | [`a-ENMIENDA-E2-MULTIREPO.md`](a-ENMIENDA-E2-MULTIREPO.md) — un producto ADS son varias fuentes gobernadas por un repositorio de control | 2026-08-26 | la reanudación multi-fuente y la relación item/rama/PR |
> | **E3** | `a-ENMIENDA-E3-ARRANQUE-Y-POLITICA.md` — el trabajo que nace por política | 2026-09-02 | amplía b.15.1 con la TERCERA VÍA de nacimiento del trabajo |
> | **E4** | `a-ENMIENDA-E4-COMPOSICION-DE-RUTAS.md` — participantes de ruta y capacidad competente | 2026-09-02 | las filas `AUD`, `SIS` e `INV` de b.16 |
> | **E5** | `a-ENMIENDA-E5-CORRECCIONES-EDITORIALES.md` — correcciones editoriales que no cambian ninguna norma | 2026-09-02 | una cita a un predicado en b.7, y la numeración de las reglas de recomposición |
> | **E6** | `a-ENMIENDA-E6-REANUDACION.md` — la reanudación distingue lo publicado de lo especulativo | 2026-09-02 | el desenlace del paso 2 de b.14 |
>
> **Y una sección NUEVA, del mismo grado normativo que este documento**, que ocupa la
> materia que `a.9` delegó:
> `g-ESTADO-DURABLE-APROBADA.md`, aprobada por `O23`.
>
> Los puntos afectados llevan la marca `[E3]`, `[E4]`, `[E5]` o `[E6]` en el texto de abajo.
> **El inventario de enmiendas NO se escribe a mano: se deriva** con
> `ls -1 docs/rediseno/a-ENMIENDA-E*.md`.>
> **Por qué las enmiendas nuevas y la sección `(g)` se NOMBRAN y no se ENLAZAN aquí:** la
> lista de lo que viaja con el kernel a un proyecto instalado vive en el tooling, que es
> DERIVADO. `F5` toca la fuente; alinear el derivado es de `F6`. Enlazarlas antes de que
> viajen dejaría **enlaces rotos en todo proyecto instalado**, que es justamente lo que la
> conformidad del arranque comprueba. **Se derivan:** `ls -1 docs/rediseno/a-ENMIENDA-E*.md`.
>
> **Este bloque no existía**, y `(b)` estaba enmendada sin decirlo en ninguna parte de su
> propio texto. Lo crea `E5` `E5.4`.

Primero el modelo general. Las rutas concretas se **derivan** de él en b.16.

---

## b.1 — Proceso, item, ruta, paquete

```text
PROCESO    el MOLDE. De clase. Vive en el kernel o en un pack.
ITEM       la COSA sobre la que se trabaja. Identidad persistente en el proyecto.
RUTA       la INSTANCIA del proceso para ESTE item: un grafo versionado r1, r2, r3…
PAQUETE    la UNIDAD DE TRABAJO Y DE CUSTODIA. Un nodo del grafo. Lo único que
           aparece en la cola de un equipo.
```

### Qué determina el proceso

> **El proceso lo determina el RESULTADO PERSEGUIDO por el item, no las capacidades
> que se usan para obtenerlo.**

Ésta es la regla de la que dependen las demás. Una investigación que construye un
prototipo **sigue siendo una investigación**, porque su salida comprometida es
conocimiento, no software productivo.

La identidad de un proceso **no** viene dada sólo por su secuencia de capacidades. La
determinan seis cosas, y dos procesos pueden compartir grafo y seguir siendo distintos:

```text
INTENCIÓN            qué se persigue
CONDICIÓN DE ENTRADA qué tiene que ser cierto para que este proceso sea el adecuado
ENCUADRE             qué dosier de anclaje exige antes de componer ruta
EVIDENCIA NECESARIA  qué hay que demostrar para poder cerrar
CRITERIO DE CIERRE   cuándo está terminado
MÉTRICAS Y APRENDIZAJE  qué mide y qué deja al sistema
```

**No se inventan estaciones artificiales para diferenciar procesos.**

### Regla de proceso único

Un item tiene **exactamente un proceso** en cada momento. Si su resultado perseguido
cambia durante el recorrido:

```text
La intención original SOBREVIVE     → cambia el proceso del MISMO item, con traza
Hace falta un resultado DISTINTO    → nace un ITEM NUEVO, enlazado al original
```

Nunca dos procesos sobre el mismo item. Pero esto **no** limita qué capacidades puede
activar una ruta: ver `CON:experimental` en b.16.

---

## b.2 — Estados de paquete

```text
propuesto              existe en el grafo; aún no despachable
listo                  despachable: dependencias cerradas
en curso               una capacidad tiene custodia y está trabajando
esperando-capacidad    listo, pero el equipo ha agotado sus execution_slots
esperando-dependencia  espera el resultado de otro paquete VIVO y VIABLE (b.8)
esperando-owner        espera decisión, juicio o validación del Owner
esperando-externo      espera algo fuera del sistema: proveedor, dispositivo, medición
bloqueado              espera algo que AÚN NO EXISTE y que nadie está produciendo
devuelto               emitió DEVOLUCIÓN; espera a que se corrija la capa anterior
cerrado                gate cumplido, capa depositada
cancelado              su EJECUCIÓN se detuvo, con motivo escrito.
                       TERMINAL NO ES RESUELTO: la obligación a la que servía queda
                       huérfana mientras no sea SATISFECHA ni RETIRADA (b.3)
```

### La distinción que hace útil el vocabulario

```text
esperando-dependencia   se resuelve SOLO, esperando. NO genera trabajo.
bloqueado               NO se resuelve solo. GENERA TRABAJO: hay que crear el
                        desbloqueador.
```

Confundirlas produce colas que parecen vivas y llevan semanas muertas. DSP las trata de
forma opuesta en b.12 y b.15. Una espera que deja de ser viable **DEBE** convertirse en
bloqueo (b.8): no puede quedar muerta en silencio.

### `aparcado` no es un estado de paquete

Es **global del item** y se proyecta sobre todos sus paquetes: los vuelve no
despachables y así aparecen en los tableros, **conservando intacto el estado real y el
checkpoint de cada uno**. Al retomar, cada paquete vuelve exactamente al estado que
tenía. Nada se recalcula ni se reinicia.

---

## b.3 — Vigencia de la capa: distinta de la ejecución del paquete

> **Ejecutar un paquete y que su resultado siga valiendo son dos cosas distintas.**
> Un paquete cerrado sigue históricamente cerrado: el trabajo ocurrió. Lo que puede
> cambiar después es la **vigencia de su capa**.

Toda capa depositada lleva su propio estado, independiente del estado del paquete:

```text
vigente      puede sostener integración y cierre
sustituida   el resultado anterior SE CONSERVA, con enlace a la capa que lo reemplaza
invalidada   su resultado ya NO puede usarse
```

Reglas:

1. **Cancelar un paquete** detiene su **ejecución**. No es lo mismo que invalidar una capa.
2. **Invalidar una capa** declara que su resultado ya no puede usarse. El paquete sigue
   cerrado en el histórico.
3. **Sustituir una capa** conserva el resultado anterior y enlaza la nueva.
4. **Nunca se reescribe un paquete cerrado como si no hubiera terminado.**
5. **La integración y el cierre sólo pueden apoyarse en capas `vigente`** (b.10).
6. Una recomposición que invalide una capa **DEBE** crear el trabajo necesario para
   reemplazarla, o justificar por escrito que ya no es necesaria (b.9).

### Obligaciones del proceso, y qué significa satisfacerlas

> **Terminar la ejecución no es lo mismo que satisfacer el proceso.** Un paquete
> `cancelado` es ejecución terminada; no dice nada sobre si el resultado existe.

Todo proceso declara sus **obligaciones**: los resultados que deben existir para que su
intención esté cumplida. Cada paquete de la ruta vigente **sirve** a una o más
obligaciones.

> **Producir lo que una obligación exigía y decidir que ya no forma parte del alcance son
> resultados DISTINTOS.** Si se llaman igual, el sistema puede informar de que entregó
> algo que en realidad se eliminó. Por eso son dos predicados, y sólo uno significa que el
> resultado existe.

```text
obligación_resuelta(o)  ≡  obligación_satisfecha(o)  Ó  obligación_retirada(o)


obligación_satisfecha(o) ≡
     existe una CAPA VIGENTE que produce el resultado exigido
     Ó existe OTRA capa vigente ENLAZADA que lo cubre explícitamente
                                              → EL RESULTADO EXISTE

obligación_retirada(o)   ≡
     una RECOMPOSICIÓN APROBADA declara que la obligación dejó de ser necesaria,
     IDENTIFICA QUIÉN TUVO AUTORIDAD para retirarla,
     y EXPLICA CÓMO AFECTA al resultado perseguido
                                              → EL RESULTADO NO EXISTE, y consta
```

**Reglas obligatorias:**

```text
· cancelar el paquete NO satisface ni retira la obligación
· una capa `invalidada` NO satisface una obligación
· una capa `sustituida` satisface sólo a través de la capa que la reemplaza
· cerrar todos los paquetes NO resuelve nada por sí mismo
· una RETIRADA conserva siempre la obligación original y su motivo en el histórico
· el CIERRE exige que todas las obligaciones vigentes estén RESUELTAS (b.10)
· el INFORME DE CIERRE distingue cuántas quedaron SATISFECHAS y cuántas RETIRADAS
· una obligación RETIRADA NUNCA puede aparecer como funcionalidad, evidencia
  o resultado entregado
· si retirar una obligación CAMBIA MATERIALMENTE el resultado perseguido, se activa
  la regla de b.1 —cambio de proceso o item nuevo—. NO puede ocultarse como una
  recomposición rutinaria
```

Una obligación **ni satisfecha ni retirada** queda **`obligación_huérfana`**: la señal de
que la ejecución terminó y el resultado no existe **ni consta que se decidiera
eliminarlo**. La función de estado global (b.4) y el cierre (b.10) la usan como entrada.

---

## b.4 — El estado global como función total

El estado global es **calculado**, nunca escrito a mano.

```text
estado_global(item) → (estado, motivo)
```

**Vocabulario de estados globales:**

```text
encuadrado                existe, con ruta compuesta, sin paquetes todavía
activo                    hay trabajo despachado o despachable
en espera                 nada despachable, pero nada estructural lo impide
bloqueado                 falta crear algo que aún no existe
en desacuerdo             conflicto, veto o freno escalado sin resolver
aparcado                  el Owner ha retirado la atención. DECLARADO.
cancelando                cancelación global en curso: aún hay paquetes abiertos
cancelado                 cancelación global completada. DECLARADO + verificado.
reconciliacion-pendiente  transición multiarchivo incompleta: el estado NO es fiable
cerrado                   condiciones de b.10 cumplidas
```

### Precedencia mecánica

Se evalúa en orden. Gana la primera que se cumple.

```text
P0   `reconciliacion_pendiente` — transición multiarchivo incompleta,
     INCLUIDA una cancelación a medias                    → reconciliacion-pendiente
     Mientras esto sea cierto, ningún otro cálculo es fiable. Va PRIMERO.

P1   bandera `cancelado`  Y  ∃ paquete ABIERTO            → cancelando
P2   bandera `cancelado`  Y  ningún paquete abierto       → cancelado
P3   bandera `aparcado`                                   → aparcado
P4   ∃ desacuerdo abierto o freno escalado (a.7)          → en desacuerdo
P5   ∃ paquete `en curso`                                 → activo
P6   ∃ paquete `listo`                                    → activo
P7   ∃ paquete `propuesto` con TODAS sus dependencias
     cerradas y vigentes                                  → activo
                                                            motivo: pendiente de promoción
P8   ∃ paquete `bloqueado`                                → bloqueado
P9   ∃ `esperando-*` · `devuelto` · `propuesto` con
     dependencias abiertas                                → en espera
P10  TODOS los paquetes terminales (`cerrado`|`cancelado`):

       ∃ obligación_huérfana (b.3) — ni satisfecha ni retirada:
          · el trabajo de reemplazo es identificable      → bloqueado
                                              motivo: obligación huérfana sin reemplazo
          · se espera decisión sobre RETIRARLA o
            abandonar el item                             → en espera
                                              motivo: obligación huérfana sin decisión

       TODAS las obligaciones RESUELTAS (satisfechas o retiradas):
          · integración semántica no declarada            → en espera
                                              motivo: integración pendiente
          · declarada, `learning_candidate` sin resolver  → en espera
                                              motivo: aprendizaje pendiente
          · ambas resueltas                               → cerrado

P11  conjunto de paquetes vacío                           → encuadrado
```

**`abierto`** = cualquier estado de paquete que no sea `cerrado` ni `cancelado`.

### Totalidad

Los once estados de paquete de b.2 quedan cubiertos: `en curso` por P5 · `listo` por P6 ·
`propuesto` por P7 y P9 · `bloqueado` por P8 · los cuatro `esperando-*` y `devuelto` por
P9 · `cerrado` y `cancelado` por P10. P0–P3 cubren banderas e inconsistencia; P11, el caso
vacío. **No existe combinación válida sin resultado, y ninguna produce dos.**

### Los casos frontera, resueltos explícitamente

| combinación | resultado |
|---|---|
| cerrados junto a propuestos | `activo` (P7) si las dependencias del propuesto están cerradas y vigentes; `en espera` (P9) si no |
| cancelados junto a activos | `activo` (P5/P6) — cancelar un paquete no detiene el item |
| desacuerdo junto a bloqueo | `en desacuerdo` (P4) — hay algo que **resolver**, y domina sobre lo que sólo hay que esperar |
| **todos terminales, obligación huérfana** | **`bloqueado` o `en espera` (P10). NUNCA `cerrado`** — cancelar todos los paquetes ni produce el resultado ni lo retira del alcance |
| todos terminales, obligaciones RETIRADAS con justificación | sigue evaluando P10 → puede llegar a `cerrado`, y el informe dirá cuántas fueron retiradas |
| todos terminales, integración pendiente | `en espera · integración pendiente` (P10) |
| todos terminales, learning pendiente | `en espera · aprendizaje pendiente` (P10) |
| aparcado con paquetes bloqueados | `aparcado` (P3). **El bloqueo se sigue reportando**: aparcar oculta el trabajo, no la información |
| **cancelado con paquetes aún abiertos** | **`cancelando` (P1), nunca `cancelado`** — no existe un `cancelado` estable con trabajo oculto debajo |
| cancelado con capas históricas | `cancelado` (P2). Las capas conservan vigencia e histórico (b.3) |
| **cancelación multiarchivo interrumpida** | **`reconciliacion-pendiente` (P0)** — la bandera de cancelación **no** la oculta |

`aparcado` y `cancelado` son modificadores dominantes **salvo frente a P0**: una
inconsistencia de estado no puede quedar tapada por una bandera.

---

## b.5 — Transiciones: quién puede ejecutar cada una

Ninguna transición es ejecutable por quien no la tiene declarada aquí. Toda transición
escribe un evento con su atribución completa (los cinco conceptos de a.9).

| transición | quién | precondición |
|---|---|---|
| — → `propuesto` | DSP | al componer o recomponer la ruta |
| `propuesto` → `listo` | DSP | dependencias de entrada cerradas con capa **vigente** |
| `listo` → `en curso` | DSP (despacho) | seis condiciones de a.5 y capacidad disponible (b.11) |
| `en curso` → `cerrado` | la capacidad con custodia | **gate cumplido**, capa depositada |
| `en curso` → `devuelto` | la capacidad con custodia | freno de devoluciones no agotado (a.7) |
| `en curso` → `bloqueado` | la capacidad con custodia | **debe nombrar qué lo desbloquearía** |
| `en curso` → `esperando-*` | la capacidad con custodia | **checkpoint escrito** (gate de suspensión) |
| `en curso` → `cancelado` | **autoridad** según b.7; **ejecutor** DSP | decisión de cancelación autorizada + motivo escrito |
| item → `cancelando` | la autoridad de b.7; ejecutor DSP | orden de cancelación global aceptada |
| `cancelando` → `cancelado` | DSP | ningún paquete abierto; checkpoints y capas conservados |
| `esperando-*` → `en curso` | DSP | desapareció la espera; se recarga el checkpoint |
| `esperando-dependencia` → `bloqueado` | DSP | la dependencia dejó de ser viable (b.8) |
| `bloqueado` → `listo` | DSP | el desbloqueador existe y cerró con capa vigente |
| capa → `sustituida` / `invalidada` | la capacidad **propietaria de esa capa**, o el Owner en materia suya | motivo escrito + trabajo de reemplazo o justificación (b.3) |
| cualquiera → `aparcado` | **sólo el Owner** | orden explícita |
| `aparcado` → estado anterior | **sólo el Owner** | orden explícita. **DSP nunca desaparca** |
| item → `cerrado` | **el propietario global** declara la integración; DSP verifica las cinco condiciones | b.10 — **terminación Y satisfacción**, no sólo estados terminales |
| ruta r_n → r_n+1 | **sólo DSP** | disparador de b.9, con motivo escrito |

**Tres reglas duras:**

1. Una capacidad **NO PUEDE** mover un paquete que no tiene en custodia.
2. **DSP no cierra, no devuelve y no cancela por contenido.** Sólo mueve por estado.
3. El Owner **no necesita** ejecutar transiciones para gobernar: emite órdenes y DSP las
   ejecuta. Aparcar y retomar son las únicas suyas en exclusiva.

---

## b.6 — La ruta como grafo

Grafo dirigido de paquetes que **crece durante la ejecución**. No es un plan fijo.

```text
A → B    SECUENCIA        B necesita la capa cerrada y VIGENTE de A
A ⊳ B    DESBLOQUEO       A produce lo que B necesita; B PUEDE prepararse antes
A ⇄ B    GATE CONJUNTO    A y B se critican mutuamente; NINGUNO cierra solo
A ⟿ B    CONSULTA         B es una consulta solicitada por A; no transfiere custodia
A ∥ B    (no es arista)   ausencia de arista + seis condiciones de a.5 cumplidas
```

**Aciclicidad:** el grafo **DEBE** ser acíclico salvo por los `⇄` declarados, que se
modelan como **gate compartido entre dos paquetes**, no como ciclo de aristas. DSP
**DEBE** rechazar una composición que introduzca un ciclo implícito.

**Crecimiento:** añadir nodos es normal y se traza. **Quitar un nodo que ya depositó capa
no existe**: eso es cancelación de ejecución (b.2) o cambio de vigencia de la capa (b.3),
nunca un borrado.

---

## b.7 — Ciclo de vida

**CREACIÓN.** Un disparador entra por DSP/Encuadre. DSP escribe la ficha con el dosier de
anclaje, asigna resultado perseguido y proceso, compone r1 y crea los paquetes en
`propuesto`. Prioridad por defecto `normal` (regla del kernel, a.9).

**ACTIVACIÓN.** DSP promueve a `listo` y despacha según b.12. No requiere al Owner salvo
punto obligatorio declarado (a.8).

**SUSPENSIÓN.** Salir de `en curso` sin cerrar. **Requiere checkpoint escrito** — gate de
suspensión de a.10. Conserva la custodia.

**APARCADO.** Sólo el Owner. Congela el item conservando estados y checkpoints.

```text
· el sistema NO propone desaparcar, cerrar ni "limpiar" por antigüedad
· un item aparcado NO consume capacidad ni frena a otros
· si OTRO item depende de uno aparcado, DSP lo REPORTA y nunca desaparca
· agotar owner_attention_slots NUNCA aparca nada (b.11)
```

**BLOQUEO.** La capacidad con custodia declara `bloqueado` **nombrando qué lo
desbloquearía**. Un bloqueo sin desbloqueador nombrado es un defecto, no un bloqueo.

**DEVOLUCIÓN.** A la capacidad concreta, nombrando qué falta. Sujeta al freno de 2 y a la
detección de ciclos multiparte (a.7). La capa devuelta **no se borra**: pasa a
`invalidada` o `sustituida` según b.3, y siempre por decisión de su capacidad propietaria.

> **Toda devolución obliga a DSP a crear o reabrir el paquete de corrección en el mismo
> ciclo.** Un `devuelto` sin paquete de corrección deja al item en `en espera` (P9) `[E5]`
> cuando en realidad hay trabajo que hacer, y es un defecto de despacho, no un estado
> legítimo.

**CANCELACIÓN.** Detiene la **ejecución**; no borra el histórico y **no satisface ninguna
obligación** (b.3).

#### Autoridad, orden y ejecución son tres cosas distintas

```text
DSP  PUEDE ser EJECUTOR TÉCNICO de una cancelación.
DSP  NUNCA posee por sí mismo la AUTORIDAD SEMÁNTICA para decidirla.

LA CAPACIDAD CON CUSTODIA   emite decisión o PROPUESTA de cancelación, conforme a su
                            gate, su veto y su ámbito de autoridad
EL PROPIETARIO GLOBAL       decide cómo afecta esa cancelación a la ruta y al
                            resultado perseguido
EL OWNER                    interviene cuando la cancelación afecta a materia
                            reservada, decisión estratégica, un resultado que él pidió
                            expresamente, o una acción difícilmente reversible
DSP CANCELA MECÁNICAMENTE   sólo al ejecutar una orden ya autorizada o una
                            recomposición ya aprobada que retira el paquete de la ruta
```

#### Cancelación de paquete no es cancelación global del item

```text
DE PAQUETE   detiene ese paquete. La obligación a la que servía queda HUÉRFANA (b.3)
             salvo retirada aprobada. No cierra nada por sí misma.

GLOBAL       transición coherente y recuperable, en DOS pasos:
             `cancelando`  →  se detienen o reconcilian TODOS los paquetes abiertos
             `cancelado`   →  sólo cuando no queda ninguno abierto
```

Reglas duras de la cancelación global:

1. **NO** puede quedar un item `cancelado` mientras conserva paquetes ejecutándose en
   silencio. El estado intermedio es `cancelando`, y es visible.
2. Se **conservan todos los checkpoints** y **todas las capas históricas** con su
   vigencia. Cancelar no borra.
3. Si existe una **operación de contención que no puede detenerse con seguridad** —una
   recuperación, un rollback en curso—, **DEBE separarse en un item ENLAZADO que sigue
   activo**. Nunca se esconde trabajo activo debajo de un item globalmente cancelado.
4. Una inconsistencia durante la cancelación multiarchivo aparece como
   `reconciliacion_pendiente` (b.4), **no queda oculta** por la bandera de cancelación.

**CIERRE.** Ver b.10.

---

## b.8 — Dependencias, y por qué una espera no puede quedar muerta

**Intra-item:** las aristas del grafo (b.6).

**Inter-item**, tipadas, y **nunca crean custodia compartida**:

```text
requiere      A no puede cerrar sin que B cierre
desbloquea    B produce el desbloqueador de A
duplica       A y B son lo mismo → uno se cancela con enlace al vigente
supersede     A sustituye a B
deriva de     A nació del recorrido de B
```

### Viabilidad de la espera *(regla obligatoria)*

> `esperando-dependencia` **sólo se sostiene mientras el item o paquete enlazado sea
> VIABLE**: existe, no está cancelado, no está aparcado indefinidamente, y sigue en
> situación de producir el resultado requerido.

En cuanto deja de cumplirse, DSP **DEBE** reevaluar y convertir la situación en una de
tres, con motivo escrito:

```text
BLOQUEO           el resultado sigue haciendo falta y hay que crear otro productor
RECOMPOSICIÓN     la ruta puede llegar al resultado por otro camino
CANCELACIÓN       justificada: el resultado ya no hace falta
```

**Una espera no puede quedar muerta en silencio.** La comprobación de viabilidad se
ejecuta en cada ciclo de reconciliación y en el paso 2 de `Continúa` (b.14).

**Otras reglas:**

1. Un **ciclo de dependencias entre items** es un defecto que DSP **DEBE** detectar y
   escalar. No se resuelve eligiendo uno.
2. Una dependencia sobre un item **aparcado** convierte al dependiente en `bloqueado` y
   **DSP lo reporta al Owner**, sin desaparcar nada.
3. Una dependencia sobre un item **cancelado** obliga a recomposición.

---

## b.9 — Recomposición y avance material

**Quién: sólo DSP.** Disparadores: una capacidad la pide con motivo · el resultado
perseguido cambia · una orden del Owner · un freno disparado (a.7) · una dependencia
nueva o dejada de ser viable (b.8).

Reglas:

1. La recomposición **nunca borra capas depositadas**. Puede **provocar** un cambio de
   vigencia (b.3), pero **DSP no invalida capas por sí mismo**: eso es autoridad
   semántica, que no tiene (b.5). DSP **solicita** la invalidación a la capacidad
   propietaria de esa capa, y hasta que ésta responda la capa sigue `vigente`.
   Si la capacidad propietaria no está materializada, la solicitud escala al Owner.
2. Los paquetes ya `cerrado` siguen cerrados. Si su capa se invalida, la recomposición
   **DEBE** crear el trabajo de reemplazo o **RETIRAR expresamente la obligación** (b.3),
   identificando quién tuvo autoridad y cómo afecta al resultado perseguido. Dejar la
   obligación huérfana bloquea el cierre (b.10).
3. La ruta pasa a `r_n+1`, con traza de **qué cambió y por qué** (formato de a.6).
4. Recomponer **no reinicia el trabajo en curso**: un paquete `en curso` que sobrevive en
   la ruta nueva conserva su custodia y su checkpoint.
5. **Una retirada que cambia materialmente el resultado perseguido NO es una recomposición
   rutinaria**: activa la regla de b.1 —cambio de proceso o item nuevo—. Recomponer no
   puede ser la vía silenciosa para reducir el alcance.

### `avance_material` *(definición formal)*

Existe **avance material** cuando, desde la recomposición anterior, ha ocurrido **al
menos una** de estas siete:

```text
[ ] se satisface un gate
[ ] se resuelve una decisión pendiente
[ ] se produce evidencia nueva utilizable
[ ] se elimina o se satisface una dependencia
[ ] se cierra un paquete con una capa válida
[ ] un checkpoint registra progreso semántico verificable
[ ] se reduce explícitamente una incertidumbre que condicionaba la ruta
```

**NO cuentan como avance material:** cambiar nombres · reordenar nodos · reformular
texto · añadir paquetes sin evidencia nueva.

### Freno

```text
MAX_RECOMPOSICIONES_SIN_AVANCE = 3
```

Tras tres recomposiciones consecutivas sin avance material, DSP **detiene la
recomposición** y escala mostrando, obligatoriamente:

```text
· las TRES versiones de ruta
· qué cambió en cada una
· POR QUÉ no produjo avance material
· la decisión o contradicción concreta que impide continuar
```

Es señal del modo de fallo (b) de a.7: recomponer es barato, y por eso puede convertirse
en un sustituto de decidir.

---

## b.10 — Cierre del item

> **Cerrar paquetes no es producir el resultado.** Si el cierre sólo exigiera que todos
> los paquetes estuvieran en estado terminal, cancelarlos todos cerraría un item cuyo
> resultado nunca existió. Terminación de la ejecución y satisfacción del proceso son
> condiciones separadas, y hacen falta las dos.

Un item cierra cuando se cumplen **todas** estas condiciones:

```text
[ ] TERMINACIÓN   ningún paquete de la RUTA VIGENTE continúa abierto
                  (abierto = cualquier estado que no sea `cerrado` ni `cancelado`)

[ ] RESOLUCIÓN    todas las OBLIGACIONES VIGENTES del proceso RESUELTAS según b.3:
                    · SATISFECHAS — existe capa vigente que produce el resultado, Ó
                    · RETIRADAS   — recomposición aprobada, con autoridad identificada
                                    y efecto sobre el resultado explicado
                  → cero `obligación_huérfana`

[ ] VIGENCIA      ninguna obligación se apoya en una capa `invalidada`

[ ] INTEGRACIÓN   el PROPIETARIO GLOBAL declara la integración semántica completa

[ ] APRENDIZAJE   learning_candidate resuelto:  none | <enlace>
```

La última es donde aterriza la corrección de APR: **la comprobación de aprendizaje se
ejecuta en el cierre, como condición, SIN crear paquete APR.** APR recibe paquete sólo si
`learning_candidate ≠ none`, o ante incidente, revisión de circuito o promoción.

DSP **verifica** las cinco condiciones; **no declara** la integración semántica ni la
retirada de una obligación: la primera es del propietario global, la segunda pertenece a
la recomposición aprobada.

> Un item con todos sus paquetes cancelados y ninguna retirada aprobada **no puede
> cerrar**. Su salida legítima es `cancelado`, `bloqueado` o `en espera` según la decisión
> que quede registrada — **nunca `cerrado`**.

### El informe de cierre distingue lo entregado de lo eliminado

```text
CIERRE — <ITEM-ID>
obligaciones SATISFECHAS:  N   ← el resultado existe
obligaciones RETIRADAS:    M   ← se decidió que dejaban de formar parte del alcance
                                 cuál · quién tuvo autoridad · cómo afecta al resultado
```

**Una obligación retirada NUNCA se reporta como funcionalidad, evidencia ni resultado
entregado.** Un informe que sume `N+M` y lo presente como entregado es un defecto de
conformidad, no un redondeo.

---

## b.11 — Capacidad: dos límites, no uno

Un límite único por equipo contradice el objetivo del sistema. Son dos cosas distintas:

```text
execution_slots         capacidad del equipo para trabajo AUTÓNOMO en paralelo
                        POR DEFECTO: auto

  El runtime calcula la concurrencia efectiva a partir de:
    · agentes disponibles
    · límites declarados del proyecto
    · recursos
    · las seis condiciones de compatibilidad de a.5

  FALLBACK SEGURO = 1  si el runtime NO PUEDE DEMOSTRAR que dos paquetes son
                       compatibles, o desconoce los recursos disponibles.

owner_attention_slots   conversaciones o decisiones simultáneas que requieren
                        atención DIRECTA del Owner
                        POR DEFECTO: 1
```

**Reglas:**

1. Agotar `execution_slots` deja los demás en `esperando-capacidad`.
2. Agotar `owner_attention_slots` deja los demás en `esperando-owner`.
3. **Ninguno de los dos aparca nada.** Un item sólo se aparca por decisión del Owner.
4. **Que Diseño esté conversando con el Owner sobre un feature NO impide que otros
   agentes de Diseño investiguen, documenten decisiones ya tomadas o preparen propuestas
   de otro item.** Consumir atención del Owner y consumir capacidad de ejecución son
   consumos distintos de recursos distintos.

> Un gap y un feature **deben** poder progresar en Diseño al mismo tiempo, aunque sólo uno
> esté consumiendo la atención conversacional del Owner.

---

## b.12 — Selección del siguiente trabajo, e inanición

**Determinista y explicable**: mismo estado ⇒ misma selección, y siempre queda escrito por
qué ése y no otro.

```text
1 FILTRAR    paquetes `listo`, de items no aparcados ni cancelados
2 EXCLUIR    los que violan alguna de las SEIS CONDICIONES de a.5 frente al frente
             de trabajo ya en curso
3 EXCLUIR    los que exceden `execution_slots` u `owner_attention_slots` (b.11)
4 FRENOS     racha SIS · devoluciones agotadas · ciclo detectado ·
             recomposiciones sin avance · reconciliacion_pendiente (a.9)
             → si hay, se atiende ANTES de despachar
5 ORDENAR    estrictamente, en este orden:
             a) prioridad declarada      urgente > normal > fondo
             b) desbloquea a más paquetes (grado de salida en el grafo)
             c) antigüedad de espera
             d) id del paquete            ← desempate determinista, sin azar
6 DESPACHAR  el primero. El resto del frente, si hay ejecutores libres.
7 EXPLICAR   qué se eligió, por qué, y qué se excluyó y por qué
```

El paso 7 es obligatorio. Un dispatcher que elige sin explicar es una caja negra.

### Detección de inanición *(visible, sin tocar la prioridad)*

La prioridad sigue siendo **autoridad exclusiva del Owner**. El sistema **NO DEBE** elevar
prioridades por su cuenta. Pero un paquete que nunca se despacha tiene que **verse**.

Por cada paquete `listo` no despachado, DSP mantiene y muestra:

```text
tiempo_listo     desde cuándo está listo sin despacharse
postergaciones   cuántas veces fue postergado en el paso 5
adelantado_por   qué items lo adelantaron
impedimento      qué recurso, límite o condición lo impide
```

> **DSP informa de la inanición. No cambia la prioridad. Nunca.**

---

## b.13 — Órdenes en lenguaje natural

Una orden en lenguaje natural produce **exactamente el mismo tipo de evento** que una
orden escrita en `## ÓRDENES`. No hay dos clases de comando.

**Catálogo de intenciones** (extensible por pack): `CONSULTAR` · `CREAR` · `PRIORIZAR` ·
`APARCAR/RETOMAR` · `DECIDIR` · `JUZGAR` · `CAMBIAR DIRECCIÓN` · `CANCELAR` ·
`RECOMPONER` · `CONTINUAR`.

```text
1 INTERPRETAR   el agente propone: intención + objetivo + parámetros
2 ANCLAR        DSP resuelve el objetivo con el ÍNDICE DE LO EXISTENTE
3 CLASIFICAR    unívoca y reversible   → se aplica DIRECTAMENTE, sin confirmar
                ambigua o irreversible → desambiguación (abajo)
4 EVENTO        autoridad=Owner · ordenante=Owner · escritor del comando=<agente> ·
                ejecutor=DSP · base · evento
5 APLICAR       pipeline idéntico al de a.9
```

### Ambigüedad *(contrato, con valores parametrizables en (g))*

Una orden es **ambigua** cuando ocurre **cualquiera** de estas cuatro:

```text
[ ] el mejor candidato NO SUPERA el umbral mínimo de anclaje
[ ] la diferencia entre los dos mejores NO SUPERA el margen declarado
[ ] falta información necesaria para determinar la transición
[ ] existen varias interpretaciones con CONSECUENCIAS MATERIALES DIFERENTES
```

*Umbral y margen son parámetros del runtime; el contrato vive aquí.*

**Irreversible:** cae en materia reservada (G05) · cancela algo · toca un item ya cerrado.

### Desambiguación sin ids

> **El Owner nunca tiene que escribir un id.** *"Retoma el gap"* debe bastar.

Cuando haga falta desambiguar, se presentan los candidatos por **nombre humano,
naturaleza y estado** — nunca por identificador:

```text
Hay dos que encajan con "el gap":
  · Trazabilidad de lotes en salidas     GAP · aparcado desde el 19/08, en Diseño
  · Cuadre de stock por almacén          GAP · en espera de una decisión tuya
```

Todo lo demás se aplica directamente. Pedir confirmación por sistema convierte al Owner
en un botón de OK.

---

## b.14 — `Continúa`

> `[E2]` La reanudación es MULTI-FUENTE: el checkpoint referencia revisiones de cada fuente y
> **no copia contenido**. Ver [`E2`](a-ENMIENDA-E2-MULTIREPO.md) `E2.3`.

```text
1 RECONSTRUIR   leer el estado canónico completo.
                NO leer el kernel entero. NO depender de ninguna conversación.
2 VERIFICAR     contrastar lo declarado contra la realidad del repo:
                · ¿existen los artefactos que los paquetes dicen haber producido?
                · ¿hay transiciones multiarchivo incompletas? → completar o revertir (a.9)
                  `[E6]` REVERTIR alcanza SÓLO a las escrituras ESPECULATIVAS; lo
                  PUBLICADO no se revierte: se registra el incidente y se ESCALA
                · ¿hay `reconciliacion_pendiente`? → resolverla antes de nada
                · ¿hay derivados divergentes de su source_revision? → regenerar
                · ¿SIGUEN VIABLES todas las `esperando-dependencia`? (b.8)
3 CONSUMIR      procesar las órdenes pendientes de los tableros (protocolo de a.9)
4 SELECCIONAR   aplicar b.12
5 REPORTAR      UNA vez, en pocas líneas: qué retoma · por qué ése y no otro ·
                qué espera decisión tuya · qué está aparcado · qué está en inanición
6 CARGAR        entregar el control a la capacidad con custodia: cargar su checkpoint,
                comprobar `based_on`, revalidar SÓLO la parte afectada si cambió (a.10)
7 TRABAJAR      la capacidad continúa desde su paso exacto
```

1. Los pasos 1–4 son **deterministas y no requieren al Owner**.
2. El paso 5 es **obligatorio y breve**. **No se pide permiso.**
3. Si el paso 2 encuentra una inconsistencia irresoluble sin decidir, DSP **para y
   escala**. **Nunca inventa estado.**
4. `Continúa` **no significa "haz todo lo pendiente"**: despacha el frente y trabaja lo
   que haya ejecutores para trabajar.

---

## b.15 — Cuando no hay trabajo listo

```text
1 ¿hay paquetes BLOQUEADOS?
     → el trabajo real es CREAR EL DESBLOQUEADOR. Ver b.15.1: dentro del alcance ya
       autorizado, DSP lo crea y lo despacha SIN preguntar. Sólo escala el que
       amplía o cambia el alcance.
2 ¿hay `esperando-owner`?
     → presentar EL LOTE (G36), agrupado y ordenado por coste de set-up.
3 ¿hay `esperando-externo`?
     → decirlo: qué se espera, de quién, desde cuándo.
4 ¿hay esperas que han dejado de ser VIABLES? (b.8)
     → reevaluarlas ahora: bloqueo, recomposición o cancelación justificada.
5 ¿hay items APARCADOS?
     → LISTARLOS. Sin proponer desaparcarlos, sin insinuarlo.
6 ¿hay INANICIÓN? (b.12)
     → mostrarla, sin tocar prioridades.
7 ¿hay deuda registrada, aprendizajes sin promover, auditoría vencida?
     → proponer, CON el freno de racha SIS aplicado.
8 nada de lo anterior
     → DECIRLO. "No hay trabajo listo" es una respuesta correcta y completa.
```

> **REGLA DURA: el sistema NO DEBE fabricar trabajo para parecer productivo.**
> Inventar una refactorización, una mejora de tooling o una auditoría no pedida cuando la
> cola está vacía es la forma más común del modo de fallo (b) de a.7.

### b.15.1 — Desbloqueadores: la autonomía es el comportamiento normal

> **AMPLIADA por `[E3]`.** A las dos vías de nacimiento del trabajo que este apartado
> reconoce —una entrada del Owner, y un desbloqueador dentro del alcance ya autorizado— se
> añade una **TERCERA VÍA: la apertura automática por una política previamente aprobada**,
> con sus cuatro condiciones y su frontera con el gate constitucional. El texto sustitutivo
> vive en `E3` `E3.2`, no aquí.

> Que aparezca un paquete adicional **no es motivo para molestar al Owner**. La
> intervención humana aparece por **autoridad o incertidumbre real**, nunca por
> aritmética de la ruta.

**DENTRO DEL ALCANCE YA AUTORIZADO — DSP crea y despacha, sin preguntar.**

Si el desbloqueador cumple **las cinco**:

```text
[ ] es necesario para obtener el resultado YA APROBADO
[ ] no cambia el producto ni el resultado perseguido
[ ] no entra en materia reservada (G05)
[ ] es reversible
[ ] se deriva MECÁNICAMENTE del bloqueo declarado
```

DSP **crea automáticamente** el paquete o item desbloqueador, **recompone la ruta**, lo
**enlaza** y lo **despacha** cuando sea seguro. Todo con la traza de a.6 y b.9.

> DSP **no realiza el trabajo de contenido**: crea y despacha la unidad de trabajo. Quien
> la ejecuta es la capacidad competente. Eso no es autoridad semántica, es despacho.

**QUE AMPLÍA O CAMBIA EL ALCANCE — DSP prepara y escala.**

Si el desbloqueador cumple **cualquiera** de estas:

```text
[ ] introduce un resultado NUEVO
[ ] cambia producto o diseño aprobado
[ ] afecta a materia reservada
[ ] implica coste o riesgo difícilmente reversible
[ ] admite varias soluciones SEMÁNTICAMENTE DIFERENTES
```

DSP **prepara la propuesta** y la envía a la capacidad con autoridad sobre esa materia, o
al Owner si es suya. No la crea por su cuenta.

---

## b.16 — Derivación de las rutas por tipo de proceso

### Regla de derivación

Las capacidades marcadas OBLIGATORIAS definen las **obligaciones** del proceso (b.3): los
resultados que deben existir para que su intención esté cumplida. **Que sus paquetes
terminen no basta: sus obligaciones tienen que quedar satisfechas** (b.10).

```text
1 PROPIETARIO GLOBAL  la capacidad cuya capa DEFINE el resultado perseguido
2 OBLIGATORIAS        aquellas sin cuya capa el resultado NO EXISTIRÍA
                      → cada una genera una OBLIGACIÓN del proceso
3 CONDICIONALES       cada una con su CONDICIÓN DE ACTIVACIÓN escrita y COMPROBABLE.
                      Prohibido "si aplica".
4 CONDICIÓN DE CIERRE b.10
5 TRAZA               todo lo no activado deja motivo (a.6)
```

### Vocabulario de condiciones — declarado una vez, reutilizado en todas las rutas

```text
C-PRD   el item altera alcance, criterio de éxito, o comportamiento visible no
        especificado previamente
C-DIS   el item toca una superficie que un humano percibe —visual, interacción, texto
        visible, movimiento, sonido— O altera la experiencia de un flujo existente
C-ARQ   el diagnóstico no es evidente · O toca contratos o estructura · O el radio de
        impacto excede un módulo
C-DOM   toca modelo de dominio, contratos de datos o esquemas
C-SEG   toca autenticación, autorización, datos personales, secretos, red o
        dependencias externas
C-ENT   el resultado debe existir fuera del entorno de desarrollo para ser útil o
        verificable
C-USO   existe una fuente de uso real aplicable —Owner, usuario, operador, dispositivo,
        telemetría, logs— Y el resultado NO es verificable sólo por VER
C-APR   learning_candidate ≠ none
C-VER   la auditoría debe producir una celda de cobertura VERIFICADA, es decir con su
        DICTAMEN como evidencia. El inventario, la detección y la propuesta NO la
        activan                                                              [E4]
```

### DOM y SEG participan dos veces, y nunca a la vez que CON

```text
<CAP>:condiciones   ⊳ CON     RESTRICCIONES ANTES de construir. Consulta.
<CAP>:revisión      tras VER  revisan lo construido. Consulta o gate conjunto.
```

Construir primero y consultar después es cómo se producen las migraciones que hay que
rehacer y los fallos de autorización que se descubren en revisión.

### `CON:experimental` — Construcción dentro de una investigación

El proceso lo determina el **resultado perseguido** (b.1), no las capacidades usadas. Una
ruta `INV` **PUEDE** activar Construcción para producir un spike, un prototipo desechable,
un simulador, un banco de pruebas, instrumentación o código experimental necesario para
obtener evidencia. **El item sigue siendo INV**, porque su salida comprometida es
conocimiento.

`CON:experimental` opera con custodia, gate y checkpoint normales, y estas restricciones:

```text
[ ] el artefacto queda IDENTIFICADO como experimental
[ ] aislamiento respecto al producto
[ ] NO desplegable como funcionalidad productiva
[ ] NO integrable silenciosamente en la rama o la arquitectura productiva
[ ] criterio de DESCARTE O CONSERVACIÓN declarado antes de construir
[ ] evidencia que DEBE producir, declarada antes de construir
[ ] checkpoint y custodia normales
```

> **Un spike NO produce siempre dos items.** Puede terminar únicamente con evidencia y
> cerrar el INV. **Sólo nace un item nuevo —FEA, GAP, DEF, DEU o SIS— cuando se decide
> fabricar o integrar un resultado productivo** a partir de la investigación.

### `DIR` — el propietario global no lo elige DSP

DSP **no tiene autoridad semántica**. Regla, en orden:

```text
1 DIR identifica las DECISIONES CONCRETAS que pretende sustituir
2 Una sola decisión principal      → la capacidad PROPIETARIA DE ESA DECISIÓN
                                     es la propietaria global
3 Varias decisiones SEPARABLES     → se crean items DIR ENLAZADOS, cada uno con su
                                     propietario correspondiente
4 Varias decisiones INSEPARABLES   → el OWNER declara cuál es el criterio principal
                                     de éxito, y con ello la capacidad líder.
                                     Las demás participan mediante GATE CONJUNTO (⇄)
5 DSP APLICA Y REGISTRA la resolución. No decide por interpretación propia.
```

**La ambigüedad se escala, no se resuelve en silencio.**

### Las diez rutas derivadas

| tipo | propietario global | obligatorias | condicionales |
|---|---|---|---|
| **FEA** capacidad nueva | PRD | PRD · CON · VER | DIS `C-DIS` · ARQ `C-ARQ` · DOM/SEG:condiciones `C-DOM`/`C-SEG` · ENT `C-ENT` · USO `C-USO` · APR `C-APR` |
| **GAP** expectativa o calidad ausente respecto a algo existente | PRD | PRD · CON · VER | idénticas a FEA. **Misma plantilla de ruta, proceso distinto** — ver abajo |
| **DEF** defecto | ARQ si `C-ARQ`, si no CON | CON · VER | **DIS `C-DIS`** · ARQ `C-ARQ` · ENT `C-ENT` · USO `C-USO` · APR `C-APR` · PRD sólo si el diagnóstico revela `C-PRD` → cambia el proceso (b.1) |
| **INC** incidente en uso real | ENT | ENT(contención) · ARQ(diagnóstico) · CON · VER · ENT(reentrega) · **APR obligatorio** | SEG:condiciones `C-SEG` · USO `C-USO`. *Único tipo con APR obligatorio: un incidente sin aprendizaje registrado se repite* |
| **INV** investigación | INV | INV | **CON:experimental** cuando la evidencia exija construir · PRD o ARQ según destino declarado · APR `C-APR` · **DOM `C-DOM` · SEG `C-SEG` · DIS `C-DIS`, cuando la materia del descubrimiento lo requiera** `[E4]` |
| **DEU** deuda técnica | ARQ | ARQ · CON · VER | DOM/SEG:condiciones · ENT `C-ENT` · **USO `C-USO`** · APR `C-APR` |
| **DEP** dependencia | PLT | **SEG:condiciones ⊳ CON** · VER | DOM:condiciones `C-DOM` · ENT `C-ENT` · ARQ si el cambio de versión altera contratos. *SEG antes de construir es obligatorio aquí (G28)* |
| **AUD** auditoría de proyecto existente | derivado del encargo — ver abajo | INV | DOM `C-DOM` · SEG `C-SEG` · **DIS `C-DIS`** `[E4]` · **VER `C-VER`, productora del DICTAMEN** `[E4]` · PRD **sólo si produce una decisión de producto**. *Puede cerrar en APR sin pasar por PRD: su resultado legítimo es conocimiento e items nuevos* |
| **DIR** cambio de dirección (G51) | según la regla de arriba | ARQ(radio de impacto) · capacidades propietarias de las decisiones afectadas · **OWNER en el punto de decisión** · registro de decisiones sustituidas · criterio de éxito · **creación de los items derivados** · **`VER:decisión`** | DIS `C-DIS` · `CON:experimental` sólo si hace falta un prototipo PARA DECIDIR · APR `C-APR`. **CON, VER, ENT y USO productivos NO son obligatorios** — ver abajo |
| **SIS** evolución del sistema | SIS | SIS · CON · VER | **ENT obligatorio si modifica el runtime** (activación segura y reversible) · APR `C-APR` · **DOM:condiciones `C-DOM` · SEG:condiciones `C-SEG` · DIS `C-DIS`, cuando la materia del descubrimiento lo requiera** `[E4]`. Sujeto al freno de racha SIS (a.7) |

### `AUD` — el propietario global se deriva del encargo

AUD **no se divide en subtipos**. Lo que se exige es que el **Encuadre declare siete
cosas** antes de componer ruta:

```text
[ ] objeto auditado
[ ] pregunta que debe responder
[ ] resultado perseguido
[ ] consumidor de la conclusión
[ ] materia o decisión sobre la que puede actuar
[ ] evidencia mínima
[ ] criterio de cierre
```

```text
PROPIETARIO GLOBAL = la capacidad responsable de la CONCLUSIÓN PERSEGUIDA,
                     o de la DECISIÓN QUE CONSUMIRÁ esa conclusión
```

Con eso, AUD deja de ser la excepción: sale de la regla general de b.16, como las otras
nueve rutas.

**INV puede ejecutar gran parte de la auditoría sin ser su propietario global.** Ejecutar
el trabajo y responder por la conclusión son cosas distintas (a.5).

```text
Varias conclusiones INDEPENDIENTES con propietarios distintos
   → se divide en items AUD ENLAZADOS, uno por conclusión
Conclusiones INSEPARABLES
   → misma regla que DIR: el OWNER declara el criterio principal y la capacidad líder;
     las demás participan por gate conjunto (⇄). DSP registra y ejecuta, no decide.
```

### `DEF` y Diseño

Un defecto visual, de interacción o de experiencia **puede** requerir Diseño sin requerir
una decisión nueva de Producto. `C-DIS` en `DEF` cubre tres casos:

```text
· determinar cuál era el PATRÓN APROBADO que se ha incumplido
· resolver un caso NO CUBIERTO por el sistema de diseño
· revisar que la corrección RESTAURA la intención visual o de uso
```

> **Un bug visual no se convierte en feature por activar Diseño.** El resultado perseguido
> sigue siendo restaurar un comportamiento esperado, no introducir uno nuevo.

### `DEU` y Uso real

Una deuda técnica **puede** afectar a rendimiento, accesibilidad, estabilidad percibida,
consumo energético o tiempos de respuesta **sin convertirse por ello en feature**. `C-USO`
en `DEU` se activa cuando haya que demostrar:

```text
· ausencia de regresiones perceptibles
· mejora de rendimiento o de accesibilidad
· conservación del flujo
· comportamiento correcto en condiciones reales
```

> La clasificación sigue dependiendo del **resultado perseguido**: reducir deuda y riesgo
> interno, no introducir una capacidad de producto.

### `FEA` y `GAP`: misma plantilla, procesos distintos

```text
                FEA                              GAP
INTENCIÓN       introducir capacidad o           reconciliar una expectativa,
                comportamiento NUEVO             necesidad o nivel de calidad
                                                 AUSENTE respecto a algo existente
ENTRADA         no existe todavía                existe algo, y no llega
ENCUADRE        anclaje sobre lo colindante      anclaje sobre LO YA IMPLEMENTADO:
                                                 qué existe, qué se creía que existía
EVIDENCIA       el comportamiento nuevo funciona la distancia entre lo pretendido y
                                                 lo real ha desaparecido
CIERRE          la capacidad existe y se acepta  la expectativa queda satisfecha
APRENDIZAJE     sobre el producto                sobre por qué apareció el hueco
                                                 ← la fuente más valiosa del sistema
```

**Comparten grafo por defecto y siguen siendo procesos distintos.** No se inventan
estaciones artificiales para diferenciarlos.

### `DIR` — decidir no es implementar

El resultado perseguido de un DIR es **decidir y registrar una nueva dirección con
conocimiento de su impacto**. No es implementar todo lo que se deriva de ella. Aplicando
b.1 —el proceso lo determina el resultado perseguido— `CON` y `VER` **productivos dejan de
ser obligatorios**.

**Obligatorio en DIR:**

```text
[ ] análisis del RADIO DE IMPACTO
[ ] participación de las capacidades PROPIETARIAS DE LAS DECISIONES AFECTADAS
[ ] el OWNER en el punto de decisión
[ ] registro de QUÉ DECISIONES ANTERIORES QUEDAN SUSTITUIDAS
[ ] CRITERIO DE ÉXITO de la nueva dirección
[ ] creación de los ITEMS DERIVADOS necesarios
```

```text
[ ] VER:decisión                    ← paquete OBLIGATORIO, ver abajo
```

**No obligatorio:** Construcción productiva, Verificación **de implementación**, Entrega y
Uso real. La ejecución de la dirección aprobada se materializa mediante **items
enlazados** —FEA, GAP, DEU, SIS o el que corresponda— que continúan de forma independiente
y **paralelizable**.

`CON` sólo entra en un DIR como **`CON:experimental`**, cuando el propio proceso declara
que necesita un prototipo **para poder decidir**: produce evidencia, no implementación
productiva. **Ninguna construcción productiva puede vivir dentro de un DIR.**

#### `VER:decisión` — se verifica la decisión, no su implementación

DIR no implementa, pero **su artefacto de decisión sí necesita comprobación independiente
antes de cerrar** (G13). `VER:decisión` no aprueba la preferencia del Owner ni verifica una
implementación que no existe: comprueba que el resultado de DIR es **íntegro, coherente,
trazable y ejecutable**.

```text
[ ] el RADIO DE IMPACTO fue analizado
[ ] están identificadas las DECISIONES SUSTITUIDAS
[ ] las CAPACIDADES AFECTADAS participaron cuando correspondía
[ ] la nueva dirección y su CRITERIO DE ÉXITO están escritos SIN AMBIGÜEDAD
[ ] las CONTRADICCIONES CONOCIDAS están resueltas o registradas
[ ] cada CONSECUENCIA EJECUTABLE está cubierta por un ITEM DERIVADO
[ ] NO existen impactos detectados SIN PROPIETARIO
[ ] los items derivados conservan ENLACES hacia DIR y hacia la decisión que ejecutan
[ ] NINGUNA implementación productiva quedó escondida dentro de DIR
```

**Límites de autoridad de `VER:decisión`:**

```text
NO PUEDE  sustituir la decisión del Owner por su propia preferencia
NO PUEDE  reabrir la dirección por desacuerdo estético, técnico o de producto
SÍ DEVUELVE  si el registro está INCOMPLETO, es CONTRADICTORIO, no cubre el impacto
             conocido, o no puede ejecutarse mediante los items derivados
```

Las **capacidades propietarias de las decisiones sustituidas** confirman por **gate
conjunto (⇄)** que su materia está representada correctamente. Eso **no** les da un veto
general sobre la dirección elegida. Si aparece un **veto no levantable** de los definidos
en (a), se aplica su contrato normal.

#### Ruta conceptual de DIR

```text
radio de impacto
→ participación de las capacidades afectadas
→ decisión del Owner
→ registro de sustituciones y criterio de éxito
→ creación de los items derivados
→ VER:decisión
→ cierre de DIR
```

`CON:experimental` puede existir **antes** de la decisión, cuando haga falta evidencia para
decidir.

> **DIR no es un macro-item que decide, construye y despliega una transformación
> completa.** Serlo dificultaría la custodia, la cancelación parcial, el paralelismo y la
> trazabilidad — las cuatro cosas que este modelo existe para dar.

**DIR cierra** cuando la decisión está tomada, registrada, descompuesta en resultados
ejecutables **y verificada por `VER:decisión`**. Los items derivados siguen su propio
recorrido, de forma independiente y paralelizable.

### Lo que la derivación produce

```text
DEF  activa DIS por C-DIS, sin volverse FEA · no activa PRD salvo cambio de proceso
DEP  no activa PRD ni DIS; SEG va ANTES de construir
INV  activa CON:experimental sin dejar de ser INV, y PUEDE cerrar sin segundo item
DEU  PUEDE activar USO sin cambiar de proceso
AUD  no activa CON, y puede cerrar en APR sin pasar por PRD
INC  es el único con APR obligatorio
DIR  el propietario global NUNCA lo elige DSP · DECIDE, no implementa: la ejecución va
     en items enlazados · su DECISIÓN sí se verifica, con `VER:decisión`
AUD  el propietario global se DERIVA del encargo declarado, no se asigna a mano
SIS  ENT obligatorio si modifica el runtime
GAP  comparte grafo con FEA y es un proceso distinto por intención, entrada, encuadre,
     evidencia, cierre y aprendizaje
```

### Una errata

`C-PRD` falso · `C-DIS` falso (corrige un texto dentro de un patrón vigente, sin proponer
forma nueva) · `C-ARQ` falso · `C-USO` falso:

```text
DEF · errata:   CON → VER  [→ ENT si C-ENT]
```

La misma regla de derivación aplicada a un item pequeño, con la misma traza de
`no activadas`. *Se confirma formalmente en (e).*

---

## b.17 — Pruebas de conformidad de la sección (b)

```text
T26 PROCESO ÚNICO      Ningún item tiene dos procesos. Un cambio de resultado perseguido
                       produce cambio de proceso con traza, o item nuevo enlazado.

T27 ESTADO TOTAL       Toda combinación válida de estados de paquete produce EXACTAMENTE
                       UN estado global. Se prueban los siete casos de b.4.   [corregida]

T28 AUTORIDAD DE       Ninguna transición ejecutada por quien no la tiene declarada en
    TRANSICIÓN         b.5. Toda transición registra atribución completa.

T29 ACICLICIDAD        Ninguna ruta con ciclos salvo gates conjuntos declarados. Ningún
                       ciclo de dependencias entre items sin escalar.

T30 SUSPENSIÓN         Ningún paquete salió de `en curso` sin cerrar y sin checkpoint.

T31 BLOQUEO ÚTIL       Todo `bloqueado` nombra su desbloqueador. Ningún `bloqueado` usado
                       donde correspondía `esperando-dependencia`, ni al revés.

T32 DESPACHO           Mismo estado ⇒ misma selección, desempate por id incluido. Toda
    DETERMINISTA       selección deja escrito qué se eligió y qué se excluyó, y por qué.

T33 CIERRE             Ningún item cerrado sin las CINCO condiciones de b.10:
                       terminación, satisfacción, vigencia, integración y aprendizaje.
                                                                             [corregida]

T34 APARCADO           Ningún item aparcado desaparcado por el sistema. Toda dependencia
    RESPETADO          sobre un item aparcado fue REPORTADA al Owner.

T35 ORDEN NATURAL      Una orden natural produce el mismo tipo de evento que una del
                       tablero. Ninguna orden unívoca y reversible pidió confirmación.

T36 CONTINÚA           Desde repo frío, sin conversación previa: DSP reconstruye,
                       verifica, reporta breve y retoma desde el checkpoint exacto.

T37 COLA VACÍA         Con la cola vacía el sistema NO inventó trabajo: recorrió las ocho
                       salidas de b.15 en orden. Los bloqueos rutinarios se resolvieron
                       por b.15.1 sin molestar al Owner.                     [corregida]

T38 RECOMPOSICIÓN      Ninguna recomposición borró una capa. Ninguna reinició un paquete
                       `en curso` que sobrevivía en la ruta nueva.

T39 INV AUTOSUFICIENTE Un INV usa `CON:experimental`, produce evidencia y CIERRA SIN
                       generar un segundo item.                                  [nueva]

T40 PROTOTIPO NO       Un artefacto experimental sólo entra en el producto mediante un
    PRODUCTIVO         ITEM NUEVO ENLAZADO. Nunca por integración silenciosa.     [nueva]

T41 AVANCE MATERIAL    Tres recomposiciones CON progreso semántico NO disparan el freno.
                       Tres recomposiciones cosméticas —renombrar, reordenar, reformular,
                       añadir nodos sin evidencia— SÍ lo disparan, y el escalado muestra
                       las tres versiones y por qué no hubo avance.              [nueva]

T42 PARALELISMO        Dos agentes del MISMO equipo trabajan dos paquetes a la vez sin
    INTRAEQUIPO        compartir recursos incompatibles.                          [nueva]

T43 ATENCIÓN ≠         Con `owner_attention_slots` agotado, otros paquetes del mismo
    EJECUCIÓN          equipo siguen avanzando en trabajo autónomo. Nada se aparca
                       automáticamente. Un gap y un feature progresan en Diseño a la vez.
                                                                                  [nueva]

T44 DIR SIN AUTORIDAD  DSP nunca elige el propietario semántico de un DIR. Con decisiones
    DE DSP             inseparables, la elección la declara el Owner.             [nueva]

T45 HISTORIA DE CAPA   Un paquete cerrado conserva su historia cuando su capa pasa a
                       `sustituida`. El resultado anterior sigue enlazado.        [nueva]

T46 CIERRE SOBRE       Ningún cierre ni integración se apoya en una capa `invalidada`.
    CAPA VIGENTE                                                                  [nueva]

T47 DESAMBIGUACIÓN     Una orden natural con candidatos PRÓXIMOS —no sólo empatados—
                       pide desambiguación, y la presenta con nombres humanos,
                       naturaleza y estado. Nunca pide un id.                     [nueva]

T48 DEF VISUAL         Un DEF visual activa DIS por `C-DIS` y NO se convierte en FEA.
                                                                                  [nueva]

T49 DEU CON USO        Una DEU de rendimiento activa USO por `C-USO` sin cambiar de
                       proceso.                                                   [nueva]

T50 ESPERA VIVA        Una dependencia cancelada, aparcada indefinidamente o que dejó de
                       producir su resultado NO permanece como `esperando-dependencia`:
                       DSP la convierte en bloqueo, recomposición o cancelación
                       justificada, con motivo escrito.                           [nueva]

T51 INANICIÓN VISIBLE  Un paquete listo repetidamente postergado aparece con tiempo,
                       postergaciones, quién lo adelantó y qué lo impide — SIN que el
                       sistema haya modificado su prioridad.                      [nueva]

T52 TERMINAL NO ES     Un item con TODOS sus paquetes cancelados y ninguna retirada
    SATISFECHO         aprobada NO PUEDE cerrar. Su resultado no existe.          [nueva]

T53 OBLIGACIÓN         Un paquete cancelado permite el cierre SÓLO si su obligación fue
    RETIRADA           retirada justificadamente en una recomposición aprobada, o está
                       satisfecha por otra capa vigente enlazada.                 [nueva]

T54 CANCELACIÓN SIN    DSP nunca es la autoridad semántica de una cancelación. Toda
    AUTORIDAD DE DSP   cancelación registra autoridad, ordenante y ejecutor por separado.
                                                                                  [nueva]

T55 CANCELACIÓN        Una cancelación global no deja paquetes trabajando ocultos: pasa
    COHERENTE          por `cancelando` y sólo llega a `cancelado` sin paquetes abiertos.
                       Checkpoints y capas históricas se conservan.               [nueva]

T56 CONTENCIÓN         Una operación de rollback o contención que no puede detenerse con
    SUPERVIVIENTE      seguridad sobrevive como ITEM ENLAZADO activo, visible, nunca
                       escondida bajo un item cancelado.                          [nueva]

T57 DESBLOQUEO         Un bloqueo rutinario dentro del alcance aprobado hace que DSP CREE
    AUTÓNOMO           Y DESPACHE su desbloqueador sin consultar a nadie.          [nueva]

T58 DESBLOQUEO QUE     Un desbloqueador que introduce resultado nuevo, cambia alcance,
    ESCALA             toca materia reservada, es difícilmente reversible o admite varias
                       soluciones semánticamente distintas se ESCALA ANTES de crearse.
                                                                                  [nueva]

T59 DIR DECIDE         Un DIR cierra tras producir la decisión, su registro de sustitución
                       y sus items derivados, SIN ejecutar esas implementaciones. [nueva]

T60 DIR SE DESCOMPONE  Una transformación decidida en DIR continúa mediante varios items
                       enlazados, independientes y paralelizables.                [nueva]

T61 AUD DERIVA         Una auditoría obtiene su propietario global de los siete campos del
    PROPIETARIO        encargo, en particular resultado perseguido y consumidor de la
                       conclusión. No se asigna a mano.                           [nueva]

T62 AUD SE DIVIDE      Una auditoría con conclusiones independientes se divide en items
                       AUD enlazados sin generar propiedad ambigua. Si son inseparables,
                       la capacidad líder la declara el Owner.                    [nueva]

T63 TOTALIDAD TRAS     La función de estado global sigue siendo TOTAL y DETERMINISTA tras
    OBLIGACIONES       introducir `obligación_resuelta`: los once casos frontera de b.4
                       producen exactamente un estado cada uno, y P0 no queda tapado por
                       las banderas de aparcado ni de cancelado.              [corregida]

T64 RETIRADA NO ES     Una obligación RETIRADA permite RESOLVER el proceso, pero NO
    SATISFECHA         aparece como satisfecha en ningún artefacto ni informe.    [nueva]

T65 INFORME DE CIERRE  El cierre informa POR SEPARADO obligaciones satisfechas y
                       retiradas. Ningún informe suma ambas como entregado.       [nueva]

T66 HUÉRFANA POR       Cancelar un paquete deja su obligación HUÉRFANA mientras no sea
    CANCELACIÓN        satisfecha ni retirada. El item no cierra.                 [nueva]

T67 RETIRADA           Retirar una obligación que cambia MATERIALMENTE el resultado
    MATERIAL           perseguido activa b.1 —cambio de proceso o item nuevo—, y no se
                       tramita como recomposición rutinaria.                      [nueva]

T68 ROLLBACK           Un rollback SATISFACE `ENT(reentrega)` si restaura realmente el
    SATISFACE          servicio: existe capa vigente que produce el resultado exigido.
                                                                                  [nueva]

T69 NO REENTREGAR      Decidir NO reentregar exige RETIRAR expresamente esa obligación,
    ES RETIRADA        con autoridad identificada. No es equivalente a T68.        [nueva]

T70 DIR SIN VER        Un DIR no cierra sin `VER:decisión` cerrado con capa vigente.
                                                                                  [nueva]

T71 IMPACTO SIN ITEM   `VER:decisión` detecta un impacto conocido SIN item derivado y
                       devuelve el DIR.                                           [nueva]

T72 VER NO DECIDE      `VER:decisión` NO puede rechazar una dirección sólo porque habría
                       elegido otra. Un rechazo por preferencia es un defecto de
                       conformidad.                                               [nueva]

T73 ENLACE DERIVADO    Cada item derivado de un DIR enlaza la DECISIÓN CONCRETA que
                       ejecuta, y el propio DIR.                                  [nueva]

T74 DIR SIN            Una implementación PRODUCTIVA introducida dentro de un DIR hace
    CONSTRUCCIÓN       FALLAR la conformidad. Sólo `CON:experimental` es admisible, y
    PRODUCTIVA         sólo antes de la decisión.                                 [nueva]
```

### Barrido de consistencia

Antes de cerrar la sección se verificó que no queda ninguna afirmación que implique:

```text
[ ] terminal equivale a satisfecho                    → b.2, b.3, b.4 P10, b.10, b.16
[ ] DSP decide contenido                              → b.5, b.7, b.9, b.15.1, b.16
[ ] todo bloqueo necesita aprobación humana           → b.15.1
[ ] DIR debe implementar toda la dirección            → b.16 DIR
[ ] cancelar equivale a invalidar                     → b.3, b.7
[ ] cerrar paquetes equivale a producir el resultado  → b.10
[ ] RETIRADA equivale a SATISFECHA                    → b.3, b.4 P10, b.9, b.10, b.17
[ ] DIR cierra sin verificar su propia decisión       → b.16 VER:decisión
```
