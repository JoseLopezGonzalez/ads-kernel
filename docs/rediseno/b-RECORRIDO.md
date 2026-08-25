# SECCIÓN (b) — RECORRIDO, ESTADOS Y COMPOSICIÓN DE PROCESOS

> **ESTADO: propuesta v2.** No se ha modificado `kernel/` ni `packs/`.
> Depende de la sección (a), aprobada el 2026-08-25 y **no modificada** por esta sección.

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
cancelado              su EJECUCIÓN se detuvo, con motivo escrito
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

---

## b.4 — El estado global como función total

El estado global es **calculado**, nunca escrito a mano. La función **DEBE** producir
exactamente un resultado para cualquier combinación válida de paquetes.

```text
estado_global(item) → (estado, motivo)
```

**Precedencia mecánica. Se evalúa en orden; gana la primera que se cumple.**

```text
P0  bandera `cancelado`                                    → cancelado
P1  bandera `aparcado`                                     → aparcado
P2  ∃ desacuerdo abierto o freno escalado (a.7)            → en desacuerdo
P3  ∃ paquete `en curso`                                   → activo
P4  ∃ paquete `listo`                                      → activo
P5  ∃ paquete `propuesto` con TODAS sus dependencias cerradas → activo
                                                             motivo: pendiente de promoción
P6  ∃ paquete `bloqueado`                                  → bloqueado
P7  ∃ paquete `esperando-*` · `devuelto` · `propuesto` con
    dependencias abiertas                                  → en espera
P8  todos los paquetes en `cerrado` o `cancelado`:
      integración semántica NO declarada                   → en espera
                                                             motivo: integración pendiente
      declarada, `learning_candidate` sin resolver         → en espera
                                                             motivo: aprendizaje pendiente
      ambas resueltas                                      → cerrado
P9  conjunto de paquetes vacío                             → encuadrado
```

**Totalidad:** los once estados de paquete de b.2 quedan cubiertos por P3–P8; P0, P1 y P9
cubren las banderas y el caso vacío. No existe combinación sin resultado.

**Los siete casos que esta función resuelve explícitamente:**

| combinación | resultado |
|---|---|
| cerrados junto a propuestos | `activo` si las dependencias del propuesto están cerradas (P5); `en espera` si no (P7) |
| cancelados junto a activos | `activo` (P3/P4) — cancelar un paquete no detiene el item |
| desacuerdo junto a bloqueo | `en desacuerdo` (P2) — hay algo que **resolver**, y domina sobre lo que sólo hay que esperar |
| todos cerrados, integración pendiente | `en espera · integración pendiente` (P8) |
| todos cerrados, learning pendiente | `en espera · aprendizaje pendiente` (P8) |
| aparcado con paquetes bloqueados | `aparcado` (P1). **El bloqueo se sigue reportando**: aparcar oculta el trabajo, no la información |
| cancelado con capas históricas | `cancelado` (P0). Las capas conservan su vigencia y su histórico (b.3) |

`aparcado` y `cancelado` son **modificadores dominantes**, pero la función sigue siendo
completa, determinista y comprobable.

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
| `en curso` → `cancelado` | PRD o DSP si es interno; **propuesta al Owner** si él lo pidió | motivo escrito |
| `esperando-*` → `en curso` | DSP | desapareció la espera; se recarga el checkpoint |
| `esperando-dependencia` → `bloqueado` | DSP | la dependencia dejó de ser viable (b.8) |
| `bloqueado` → `listo` | DSP | el desbloqueador existe y cerró con capa vigente |
| capa → `sustituida` / `invalidada` | la capacidad **propietaria de esa capa**, o el Owner en materia suya | motivo escrito + trabajo de reemplazo o justificación (b.3) |
| cualquiera → `aparcado` | **sólo el Owner** | orden explícita |
| `aparcado` → estado anterior | **sólo el Owner** | orden explícita. **DSP nunca desaparca** |
| item → `cerrado` | **el propietario global** declara; DSP verifica | b.10 |
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
> ciclo.** Un `devuelto` sin paquete de corrección deja al item en `en espera` (P7)
> cuando en realidad hay trabajo que hacer, y es un defecto de despacho, no un estado
> legítimo.

**CANCELACIÓN.** Detiene la **ejecución**, no borra el histórico. Si el Owner lo pidió, se
**propone**, no se ejecuta.

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
   **DEBE** crear el trabajo de reemplazo o justificar que ya no hace falta.
3. La ruta pasa a `r_n+1`, con traza de **qué cambió y por qué** (formato de a.6).
4. Recomponer **no reinicia el trabajo en curso**: un paquete `en curso` que sobrevive en
   la ruta nueva conserva su custodia y su checkpoint.

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

Tres condiciones, **todas**:

```text
[ ] todos los paquetes están en `cerrado` o `cancelado`
[ ] TODAS las capas sobre las que se apoya la integración están `vigente`
    — ningún cierre puede sostenerse sobre una capa `invalidada`
[ ] el PROPIETARIO GLOBAL declara la integración semántica completa
[ ] learning_candidate resuelto:  none | <enlace>
```

La última es donde aterriza la corrección de APR: **la comprobación de aprendizaje se
ejecuta en el cierre, como condición, SIN crear paquete APR.** APR recibe paquete sólo si
`learning_candidate ≠ none`, o ante incidente, revisión de circuito o promoción.

DSP **verifica**; **no declara** la integración semántica: esa es del propietario global.

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

```text
1 RECONSTRUIR   leer el estado canónico completo.
                NO leer el kernel entero. NO depender de ninguna conversación.
2 VERIFICAR     contrastar lo declarado contra la realidad del repo:
                · ¿existen los artefactos que los paquetes dicen haber producido?
                · ¿hay transiciones multiarchivo incompletas? → completar o revertir (a.9)
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
     → el trabajo real es CREAR EL DESBLOQUEADOR. DSP lo propone; si implica alcance
       nuevo, la propuesta va a PRD o al Owner. DSP no la ejecuta.
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

---

## b.16 — Derivación de las rutas por tipo de proceso

### Regla de derivación

```text
1 PROPIETARIO GLOBAL  la capacidad cuya capa DEFINE el resultado perseguido
2 OBLIGATORIAS        aquellas sin cuya capa el resultado NO EXISTIRÍA
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
| **INV** investigación | INV | INV | **CON:experimental** cuando la evidencia exija construir · PRD o ARQ según destino declarado · APR `C-APR` |
| **DEU** deuda técnica | ARQ | ARQ · CON · VER | DOM/SEG:condiciones · ENT `C-ENT` · **USO `C-USO`** · APR `C-APR` |
| **DEP** dependencia | PLT | **SEG:condiciones ⊳ CON** · VER | DOM:condiciones `C-DOM` · ENT `C-ENT` · ARQ si el cambio de versión altera contratos. *SEG antes de construir es obligatorio aquí (G28)* |
| **AUD** auditoría de proyecto existente | quien declare el encargo | INV | DOM `C-DOM` · SEG `C-SEG` · DIS/Reconstrucción `C-DIS` · PRD **sólo si produce una decisión de producto**. *Puede cerrar en APR sin pasar por PRD: su resultado legítimo es conocimiento e items nuevos* |
| **DIR** cambio de dirección (G51) | según la regla de arriba | ARQ(radio de impacto) · **OWNER obligatorio** · CON · VER | DIS `C-DIS` · ENT `C-ENT` · USO `C-USO` · APR `C-APR`. *El Owner va DESPUÉS del radio de impacto: decidir sin coste medido es decidir a ciegas* |
| **SIS** evolución del sistema | SIS | SIS · CON · VER | **ENT obligatorio si modifica el runtime** (activación segura y reversible) · APR `C-APR`. Sujeto al freno de racha SIS (a.7) |

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

### Lo que la derivación produce

```text
DEF  activa DIS por C-DIS, sin volverse FEA · no activa PRD salvo cambio de proceso
DEP  no activa PRD ni DIS; SEG va ANTES de construir
INV  activa CON:experimental sin dejar de ser INV, y PUEDE cerrar sin segundo item
DEU  PUEDE activar USO sin cambiar de proceso
AUD  no activa CON, y puede cerrar en APR sin pasar por PRD
INC  es el único con APR obligatorio
DIR  el propietario global NUNCA lo elige DSP
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

T33 CIERRE             Ningún item cerrado sin las condiciones de b.10, incluida la
                       declaración de integración semántica del propietario global.

T34 APARCADO           Ningún item aparcado desaparcado por el sistema. Toda dependencia
    RESPETADO          sobre un item aparcado fue REPORTADA al Owner.

T35 ORDEN NATURAL      Una orden natural produce el mismo tipo de evento que una del
                       tablero. Ninguna orden unívoca y reversible pidió confirmación.

T36 CONTINÚA           Desde repo frío, sin conversación previa: DSP reconstruye,
                       verifica, reporta breve y retoma desde el checkpoint exacto.

T37 COLA VACÍA         Con la cola vacía el sistema NO inventó trabajo: recorrió las ocho
                       salidas de b.15 en orden.

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
```
