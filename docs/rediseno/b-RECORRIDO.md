# SECCIÓN (b) — RECORRIDO, ESTADOS Y COMPOSICIÓN DE PROCESOS

> **ESTADO: propuesta.** No se ha modificado `kernel/` ni `packs/`.
> Depende de la sección (a), aprobada el 2026-08-25.

Primero el modelo general. Las rutas concretas se **derivan** de él en b.13, no se copian
de la tabla ilustrativa de a.6.

---

## b.1 — Item, proceso y paquete

Tres cosas distintas que v1–v4 usaban sin separar del todo.

```text
PROCESO    el MOLDE. De clase, no de instancia. Vive en el kernel o en un pack.
           Dice qué capacidades pueden intervenir en un item de esa naturaleza,
           con qué condiciones de activación, gates y condición de cierre.

ITEM       la COSA sobre la que se trabaja. Identidad persistente en el proyecto.
           Existe aunque nadie esté trabajando en él. Tiene naturaleza, enunciado,
           dosier de anclaje, propietario global, prioridad y estado global.

RUTA       la INSTANCIA del proceso para ESTE item: un grafo de paquetes.
           Un item tiene exactamente una ruta vigente, versionada r1, r2, r3…

PAQUETE    la UNIDAD DE TRABAJO Y DE CUSTODIA. Un nodo del grafo.
           Es lo único que aparece en la cola de un equipo.
```

```text
PROCESO (clase)
   └── instancia ──> ITEM ── compone ──> RUTA r_n ── nodos ──> PAQUETES
```

**Regla de proceso único:** un item tiene **exactamente un proceso** en cada momento.
Si su naturaleza cambia durante el recorrido, DSP decide entre dos salidas, nunca ambas:

```text
La intención original SOBREVIVE     → cambia el proceso del MISMO item, con traza
                                      (un DEF que era un GAP)
Hace falta un resultado DISTINTO    → nace un ITEM NUEVO, enlazado al original
                                      (un FEA que destapa un INC)
```

**Nunca dos procesos sobre el mismo item.** Es la regla que impide que un item se
convierta en un contenedor de trabajo heterogéneo sin dueño.

---

## b.2 — Estados de paquete

El vocabulario que ve un equipo en su tablero. Cierra la lista provisional de a.9.

```text
propuesto              existe en el grafo; aún no despachable
listo                  despachable: dependencias cerradas
en curso               una capacidad tiene custodia y está trabajando
esperando-capacidad    listo, pero el equipo ha alcanzado su concurrencia declarada
esperando-dependencia  espera el resultado de otro paquete YA EN MARCHA
esperando-owner        espera decisión, juicio o validación del Owner
esperando-externo      espera algo fuera del sistema: proveedor, dispositivo, medición
bloqueado              espera algo que AÚN NO EXISTE y que nadie está produciendo
devuelto               emitió DEVOLUCIÓN; espera a que la capa anterior se corrija
cerrado                gate cumplido, capa depositada
cancelado              no seguirá fabricándose, con motivo escrito
```

### La distinción que hace útil el vocabulario

```text
esperando-dependencia   se resuelve SOLO, esperando. No genera trabajo.
bloqueado               NO se resuelve solo. GENERA TRABAJO: hay que crear el
                        desbloqueador (una decisión, un dato, una capacidad).
```

Confundirlas es lo que produce colas que parecen vivas y llevan semanas muertas. DSP las
trata de forma opuesta en la selección de trabajo (b.10) y ante la cola vacía (b.12).

### APARCADO no es un estado de paquete

`aparcado` es **global del item** y se proyecta sobre todos sus paquetes: los vuelve no
despachables y así aparecen en los tableros, **conservando intacto su estado real y su
checkpoint**. Al retomarlo, cada paquete vuelve exactamente al estado que tenía. Nada se
recalcula ni se reinicia.

---

## b.3 — Estados globales del item

```text
encuadrado      existe, anclado, con naturaleza y ruta compuesta
activo          al menos un paquete en curso o listo
en espera       ningún paquete despachable, pero nada lo impide estructuralmente
                (todo en esperando-capacidad, esperando-owner o esperando-externo)
bloqueado       al menos un paquete bloqueado y ninguno despachable
en desacuerdo   hay un conflicto, un veto o un freno escalado sin resolver
aparcado        el Owner ha retirado la atención. Congela todo. DECLARADO.
cerrado         condición de cierre de b.9 cumplida
cancelado       no seguirá. DECLARADO.
```

> **Regla de derivación:** el estado global es **calculado**, no escrito a mano.
>
> ```text
> estado_global = f(estados de paquete)   ⊕   banderas DECLARADAS {aparcado, cancelado}
> ```
>
> Sólo `aparcado` y `cancelado` se declaran; el resto se deriva. Así el estado global
> **no puede divergir de la realidad de los paquetes**: si diverge, es un defecto de
> cálculo, no una discrepancia a interpretar. Hereda la disciplina de artefacto derivado
> de a.9 — un solo ejecutor, regeneración determinista.

---

## b.4 — Transiciones: quién puede ejecutar cada una

Ninguna transición es ejecutable por quien no la tiene declarada aquí. Toda transición
escribe un evento con su atribución completa (los cinco conceptos de a.9).

| transición | quién | precondición |
|---|---|---|
| — → `propuesto` | DSP | al componer o recomponer la ruta |
| `propuesto` → `listo` | DSP | dependencias de entrada cerradas |
| `listo` → `en curso` | DSP (despacho) | pasa las seis condiciones de a.5 y la concurrencia del equipo |
| `en curso` → `cerrado` | la capacidad con custodia | **gate cumplido**, capa depositada |
| `en curso` → `devuelto` | la capacidad con custodia | freno de devoluciones no agotado (a.7) |
| `en curso` → `bloqueado` | la capacidad con custodia | **debe nombrar qué lo desbloquearía** |
| `en curso` → `esperando-*` | la capacidad con custodia | **checkpoint escrito** (gate de suspensión) |
| `en curso` → `cancelado` | PRD o DSP si es interno; **propuesta al Owner** si él lo pidió | motivo escrito |
| `esperando-*` → `en curso` | DSP | desapareció la espera; se recarga el checkpoint |
| `bloqueado` → `listo` | DSP | el desbloqueador existe y está cerrado |
| cualquiera → `aparcado` | **sólo el Owner** | orden explícita (tablero o lenguaje natural) |
| `aparcado` → estado anterior | **sólo el Owner** | orden explícita. **DSP nunca desaparca** |
| ítem → `cerrado` | **el propietario global**, verificado por DSP | condición de cierre de b.9 |
| ruta r_n → r_n+1 | **sólo DSP** | disparador de b.8, con motivo escrito |

**Tres reglas duras:**

1. Una capacidad **NO PUEDE** mover un paquete que no tiene en custodia.
2. DSP **NO PUEDE** cerrar, devolver ni cancelar por contenido: sólo mueve por estado.
3. El Owner **NO NECESITA** ejecutar ninguna transición para gobernar: emite órdenes y
   DSP las ejecuta (a.9). Aparcar y retomar son las únicas que le pertenecen en exclusiva.

---

## b.5 — La ruta como grafo

La ruta es un **grafo dirigido de paquetes** que **crece durante la ejecución**. No es un
plan fijo trazado al principio.

**Aristas tipadas:**

```text
A → B    SECUENCIA        B necesita la capa cerrada de A
A ⊳ B    DESBLOQUEO       A produce lo que B necesita; B PUEDE prepararse antes
A ⇄ B    GATE CONJUNTO    A y B se critican mutuamente; NINGUNO cierra solo
A ∥ B    (no es arista)   ausencia de arista + seis condiciones de a.5 cumplidas
A ⟿ B    CONSULTA         B es una consulta solicitada por A; no transfiere custodia
```

**Regla de aciclicidad:** el grafo **DEBE** ser acíclico, salvo por los `⇄` declarados
explícitamente, que se modelan como **un gate compartido entre dos paquetes**, no como un
ciclo de aristas. DSP **DEBE** rechazar una composición que introduzca un ciclo implícito.

**Crecimiento del grafo:** añadir nodos es normal y se traza (ARQ descomponiendo, una
consulta que se convierte en trabajo propio). **Quitar un nodo que ya depositó capa no
existe**: eso es una cancelación con motivo, y la capa depositada permanece en el
histórico del item.

---

## b.6 — Ciclo de vida completo

**CREACIÓN.** Un disparador entra por DSP/Encuadre: frase del Owner, defecto, evento
externo, hallazgo de una capacidad, item nacido del uso real. DSP escribe la ficha con el
dosier de anclaje, asigna naturaleza y proceso, compone la ruta r1 y crea los paquetes en
`propuesto`. Prioridad por defecto `normal` (regla del kernel, no decisión inventada).

**ACTIVACIÓN.** DSP promueve a `listo` los paquetes con dependencias cerradas y despacha
según b.10. La activación **no requiere al Owner** salvo que el proceso declare un punto
obligatorio (a.8).

**SUSPENSIÓN.** Salir de `en curso` sin cerrar. **Requiere checkpoint escrito** — es el
gate de suspensión de a.10. Motivos: fin de sesión, espera, transferencia, corte del
Owner. La suspensión **conserva la custodia**.

**APARCADO.** Sólo el Owner. Congela el item completo conservando estados y checkpoints.
Reglas duras que se repiten aquí porque es donde más se incumplen:

```text
· el sistema NO propone desaparcar, cerrar ni "limpiar" por antigüedad
· un item aparcado NO consume capacidad ni frena a otros
· si OTRO item depende de uno aparcado, DSP lo REPORTA al Owner y nunca desaparca:
  la decisión de prioridad es suya, pero debe ver su consecuencia
```

**BLOQUEO.** La capacidad con custodia declara `bloqueado` **nombrando qué lo
desbloquearía**. Un bloqueo sin desbloqueador nombrado es un defecto, no un bloqueo.
El desbloqueador puede ser: una decisión (→ `esperando-owner` si es del Owner), un dato
(→ item de investigación), otro item, o una capacidad no materializada (→ a.4).

**DEVOLUCIÓN.** A la capacidad concreta, nombrando qué falta. Sujeta al freno de 2 y a la
detección de ciclos multiparte (a.7). La capa devuelta **no se borra**: se marca
insuficiente y se conserva.

**CANCELACIÓN.** Motivos legítimos de a.2. **Cancelar no borra**: el item queda con su
motivo y sus capas. Si el Owner lo pidió explícitamente, se **propone**, no se ejecuta.

**CIERRE.** Ver b.9.

---

## b.7 — Dependencias

**Intra-item** — las aristas del grafo (b.5).

**Inter-item** — tipadas, y **nunca crean custodia compartida**:

```text
requiere      A no puede cerrar sin que B cierre
desbloquea    B produce el desbloqueador de A
duplica       A y B son lo mismo → uno se cancela con enlace al vigente
supersede     A sustituye a B
deriva de     A nació del recorrido de B (típico de lo que reentra desde el uso real)
```

Reglas:

1. Un **ciclo de dependencias entre items** es un defecto que DSP **DEBE** detectar y
   escalar. No se resuelve eligiendo uno.
2. Una dependencia sobre un item **aparcado** convierte al dependiente en `bloqueado` y
   **DSP lo reporta al Owner**. Sigue sin desaparcar nada.
3. Una dependencia sobre un item **cancelado** es un defecto de la ruta: obliga a
   recomposición (b.8), no a esperar indefinidamente.

---

## b.8 — Recomposición de ruta

**Quién: sólo DSP.** Disparadores:

```text
· una capacidad la pide, con motivo escrito
· la naturaleza del item cambia (b.1)
· una orden del Owner ("esto no debería pasar por diseño")
· un freno disparado: devoluciones agotadas o ciclo detectado (a.7)
· una dependencia nueva descubierta, o una que apuntaba a algo cancelado
```

Reglas:

1. La recomposición **nunca borra capas ya depositadas**.
2. Los paquetes ya `cerrado` siguen cerrados; su capa sigue siendo válida salvo
   invalidación explícita, que es una cancelación con motivo.
3. La ruta pasa a `r_n+1` y la traza registra **qué cambió y por qué** — mismo formato de
   `activadas` / `no activadas` de a.6.
4. Recomponer **no reinicia el trabajo en curso**: un paquete `en curso` que sigue
   existiendo en la ruta nueva conserva su custodia y su checkpoint.

**Freno de recomposición.** Recomponer es barato y por eso puede volverse un sustituto de
decidir. Propuesta numérica, coherente con los frenos de a.7:

```text
MAX_RECOMPOSICIONES_SIN_AVANCE = 3
Tres recomposiciones consecutivas sin que ningún paquete cierre → DSP detiene el item
y escala, con las tres justificaciones enfrentadas. Es señal del modo de fallo (b).
```

*Este número necesita tu autoridad: ver decisiones abiertas.*

---

## b.9 — Cierre del item

Tres condiciones, **todas**:

```text
[ ] todos los paquetes están en `cerrado` o `cancelado`
[ ] el PROPIETARIO GLOBAL declara la integración semántica completa
    (no basta con que su parte terminara — regla de a.5)
[ ] learning_candidate resuelto:  none | <enlace>
```

La tercera es donde aterriza la corrección de APR: **la comprobación de aprendizaje se
ejecuta en el cierre del item, como condición, SIN crear un paquete APR.** APR recibe
paquete sólo si `learning_candidate ≠ none`, o ante incidente, revisión de circuito o
promoción.

DSP **verifica** las tres y calcula el estado; **no declara** la segunda: esa es del
propietario global.

---

## b.10 — Selección del siguiente trabajo

El algoritmo del dispatcher. **Determinista y explicable**: mismo estado ⇒ misma
selección, y siempre queda escrito por qué ese y no otro.

```text
1 FILTRAR    paquetes en `listo`, de items no aparcados ni cancelados
2 EXCLUIR    los que violan alguna de las SEIS CONDICIONES de a.5 frente al frente
             de trabajo ya en curso
3 EXCLUIR    los de equipos que han alcanzado su CONCURRENCIA declarada
4 FRENOS     racha SIS · devoluciones agotadas · ciclo detectado ·
             reconciliacion_pendiente (a.9) → si hay, se atiende ANTES de despachar
5 ORDENAR    estrictamente, en este orden:
             a) prioridad declarada     urgente > normal > fondo
             b) desbloquea a más paquetes (grado de salida en el grafo)
             c) antigüedad de espera
             d) id del paquete           ← desempate determinista, sin azar
6 DESPACHAR  el primero. El resto del frente se despacha si hay ejecutores libres.
7 EXPLICAR   escribir qué se eligió, por qué, y qué se excluyó y por qué
```

**Concurrencia de equipo.** Todo equipo materializado declara su `concurrencia`: cuántos
paquetes puede tener `en curso` a la vez. **Sin declaración, el valor es 1** — conservador
y visible; subirlo es una decisión consciente del proyecto, no un descuido. La
concurrencia entre equipos distintos no tiene límite del kernel: es el modo normal (a.9).

**El paso 7 es obligatorio.** Un dispatcher que elige sin explicar es una caja negra, y
volvemos a la constitución interpretable que este rediseño existe para eliminar.

---

## b.11 — Cómo entra una orden en lenguaje natural

**Regla fundacional:** una orden en lenguaje natural produce **exactamente el mismo tipo
de evento** que una orden escrita en `## ÓRDENES`. No hay dos clases de comando. El
camino natural añade un solo paso: la interpretación.

**Catálogo de intenciones reconocidas** (extensible por pack):

```text
CONSULTAR          estado, riesgos, qué necesita atención, qué ha cambiado
CREAR              item nuevo: gap · feature · defecto · pregunta · deuda
PRIORIZAR          cambiar prioridad
APARCAR / RETOMAR
DECIDIR            responder a un `esperando-owner`
JUZGAR             aceptar o rechazar en USO
CAMBIAR DIRECCIÓN  G51
CANCELAR
RECOMPONER         "esto no debería pasar por diseño"
CONTINUAR          → b.12
```

```text
1 INTERPRETAR   el agente propone: intención + objetivo + parámetros
2 ANCLAR        DSP resuelve a qué item o paquete se refiere, usando el ÍNDICE DE LO
                EXISTENTE. El Owner NUNCA tiene que nombrar un id: "retoma el gap"
                debe bastar.
3 CLASIFICAR    unívoca y reversible   → se aplica DIRECTAMENTE, sin confirmar
                ambigua o irreversible → eco de confirmación en UNA línea
4 EVENTO        mismo formato que la orden del tablero:
                autoridad=Owner · ordenante=Owner · escritor del comando=<agente> ·
                ejecutor=DSP · base · evento
5 APLICAR       pipeline idéntico al de a.9
```

**Criterios comprobables, no juicio del agente de turno:**

```text
AMBIGUA       el anclaje del paso 2 devuelve más de un candidato con igual puntuación
IRREVERSIBLE  cae en materia reservada (G05) · cancela algo · toca un item ya cerrado
```

Todo lo demás se aplica directamente. Pedir confirmación por sistema convierte al Owner
en un botón de OK, que es el cuello de botella que a.8 acaba de eliminar.

---

## b.12 — `Continúa`

```text
1 RECONSTRUIR   leer el estado canónico completo.
                NO leer el kernel entero. NO depender de ninguna conversación.
2 VERIFICAR     contrastar lo declarado contra la realidad del repo:
                · ¿existen los artefactos que los paquetes dicen haber producido?
                · ¿hay transiciones multiarchivo incompletas? → completar o revertir (a.9)
                · ¿hay `reconciliacion_pendiente`? → resolverla antes de nada
                · ¿hay derivados divergentes de su source_revision? → regenerar
3 CONSUMIR      procesar las órdenes pendientes de los tableros (protocolo de a.9)
4 SELECCIONAR   aplicar b.10
5 REPORTAR      UNA vez, en pocas líneas: qué retoma · por qué ese y no otro ·
                qué espera decisión tuya · qué está aparcado
6 CARGAR        entregar el control a la capacidad con custodia: cargar su checkpoint,
                comprobar `based_on`, revalidar SÓLO la parte afectada si cambió (a.10)
7 TRABAJAR      la capacidad continúa desde su paso exacto
```

**Reglas:**

1. Los pasos 1–4 son **deterministas y no requieren al Owner**.
2. El paso 5 es **obligatorio y breve**: debes saber qué se retoma antes de que se
   retome. **No se te pide permiso.**
3. Si el paso 2 encuentra una inconsistencia que no puede resolverse sin decidir, DSP
   **para y escala**. **Nunca inventa estado.**
4. `Continúa` **no significa "haz todo lo pendiente"**: despacha el frente y trabaja lo
   que haya ejecutores para trabajar.

---

## b.13 — Qué ocurre cuando no hay trabajo listo

El caso que más sistemas resuelven mal, porque fabrican trabajo para parecer productivos.

```text
1 ¿hay paquetes BLOQUEADOS?
     → el trabajo real es CREAR EL DESBLOQUEADOR. DSP lo propone; si implica alcance
       nuevo, la propuesta va a PRD o al Owner, no la ejecuta DSP.
2 ¿hay `esperando-owner`?
     → presentar EL LOTE (G36), agrupado y ordenado por coste de set-up. Nunca de uno
       en uno.
3 ¿hay `esperando-externo`?
     → decirlo: qué se espera, de quién, desde cuándo.
4 ¿hay items APARCADOS?
     → LISTARLOS. Sin proponer desaparcarlos, sin insinuarlo, sin ordenarlos por
       antigüedad como reproche. Regla dura de a.2.
5 ¿hay deuda registrada, aprendizajes sin promover, auditoría vencida?
     → proponer, CON el freno de racha SIS aplicado.
6 nada de lo anterior
     → DECIRLO. "No hay trabajo listo" es una respuesta correcta y completa.
```

> **REGLA DURA: el sistema NO DEBE fabricar trabajo para parecer productivo.**
> Inventar una refactorización, una mejora de tooling o una auditoría no pedida cuando la
> cola está vacía es la forma más común del modo de fallo (b) de a.7.

---

## b.14 — Derivación de las rutas por tipo de proceso

No se copian de la tabla ilustrativa de a.6. Se **derivan** aplicando siempre la misma
regla, para que un tipo nuevo se construya igual y sin criterio nuevo.

### Regla de derivación

```text
1 PROPIETARIO GLOBAL  la capacidad cuya capa DEFINE el resultado del item
2 OBLIGATORIAS        aquellas sin cuya capa el resultado NO EXISTIRÍA
3 CONDICIONALES       las demás, cada una con su CONDICIÓN DE ACTIVACIÓN escrita y
                      COMPROBABLE. Está prohibido "si aplica".
4 CONDICIÓN DE CIERRE qué debe ser cierto para que el item cierre (b.9)
5 TRAZA               todo lo no activado deja motivo (a.6)
```

### Vocabulario de condiciones — declarado una vez, reutilizado en todas las rutas

```text
C-PRD  el item altera alcance, criterio de éxito, o comportamiento visible no
       especificado previamente
C-DIS  el item modifica una superficie que un humano percibe —visual, interacción,
       texto visible, movimiento, sonido— O altera la experiencia de un flujo existente
C-ARQ  el diagnóstico no es evidente · O toca contratos o estructura · O el radio de
       impacto excede un módulo
C-DOM  toca modelo de dominio, contratos de datos o esquemas
C-SEG  toca autenticación, autorización, datos personales, secretos, red o
       dependencias externas
C-ENT  el resultado debe existir fuera del entorno de desarrollo para ser útil o
       verificable
C-USO  existe una fuente de uso real aplicable —Owner, usuario, operador, dispositivo,
       telemetría, logs— Y el resultado NO es verificable sólo por VER
C-APR  learning_candidate ≠ none
```

### DOM y SEG participan dos veces, y no al mismo tiempo que CON

Corrección aplicada: **no reciben la primera noticia en paralelo con Construcción.**

```text
<CAP>:condiciones   ⊳ CON     aportan RESTRICCIONES ANTES de construir.
                              Consulta. Desbloquea a CON; CON puede prepararse.
<CAP>:revisión      tras VER  revisan lo construido. Consulta o gate conjunto según
                              el nivel de riesgo declarado.
```

Construir primero y consultar después es cómo se producen las migraciones que hay que
rehacer y los fallos de autorización que se descubren en revisión.

### Las diez rutas derivadas

| tipo | propietario global | obligatorias | condicionales |
|---|---|---|---|
| **FEA** capacidad nueva | PRD | PRD · CON · VER | DIS `C-DIS` · ARQ `C-ARQ` · DOM/SEG:condiciones `C-DOM`/`C-SEG` · ENT `C-ENT` · USO `C-USO` · APR `C-APR` |
| **GAP** hueco entre lo implementado y lo pretendido | PRD | PRD · CON · VER | idénticas a FEA. **La diferencia no es la ruta: es el encuadre.** Un GAP entra con el dosier de anclaje señalando qué existe ya y qué se creía que existía |
| **DEF** defecto | ARQ si `C-ARQ`, si no CON | CON · VER | ARQ `C-ARQ` · ENT `C-ENT` · USO `C-USO` · APR `C-APR` · PRD sólo si el diagnóstico revela `C-PRD` → cambio de proceso (b.1) |
| **INC** incidente en uso real | ENT | ENT(contención) · ARQ(diagnóstico) · CON · VER · ENT(reentrega) · **APR obligatorio** | SEG:condiciones `C-SEG` · USO `C-USO`. *APR es obligatorio aquí y sólo aquí: un incidente sin aprendizaje registrado se repite* |
| **INV** investigación | INV | INV | PRD o ARQ según destino declarado · APR `C-APR`. **No activa CON**: si la investigación exige construir, nace un item nuevo |
| **DEU** deuda técnica | ARQ | ARQ · CON · VER | DOM/SEG:condiciones · ENT `C-ENT` · APR `C-APR`. **No activa USO**: la deuda no cambia comportamiento observable; si lo cambia, no era deuda |
| **DEP** dependencia | PLT | SEG:condiciones ⊳ CON · VER | DOM:condiciones `C-DOM` · ENT `C-ENT` · ARQ si el cambio de versión altera contratos. **SEG antes de construir es obligatorio aquí** (G28) |
| **AUD** auditoría de proyecto existente | el que declare el encargo de la auditoría | INV | DOM `C-DOM` · SEG `C-SEG` · DIS/Reconstrucción `C-DIS` · PRD **sólo si la auditoría produce una decisión de producto**. **Una auditoría puede cerrar en APR sin pasar por PRD**: su resultado legítimo es conocimiento y items nuevos |
| **DIR** cambio de dirección (G51) | PRD si es de producto, DIS si es de forma | ARQ(radio de impacto) · **OWNER obligatorio** · CON · VER | DIS `C-DIS` · ENT `C-ENT` · USO `C-USO` · APR `C-APR`. **El Owner va después del radio de impacto**, nunca antes: decidir sin coste medido es decidir a ciegas |
| **SIS** evolución del sistema | SIS | SIS · CON · VER | **ENT obligatorio si el cambio modifica el runtime** (activación segura y reversible, C4) · APR `C-APR`. Sujeto al freno de racha SIS (a.7) |

### Lo que esta derivación demuestra

```text
DEF   no activa PRD ni DIS salvo condición cumplida
DEP   no activa PRD ni DIS nunca; SEG va ANTES de construir
INV   no activa CON en absoluto
DEU   no activa USO en absoluto
AUD   no activa CON, y puede cerrar sin PRD
INC   es el único con APR obligatorio
GAP   comparte ruta con FEA y se distingue por el ENCUADRE, no por el recorrido
```

Ninguna ruta es la de otra, y ninguna capacidad aparece "por si acaso".

### Una errata

Aplicando la regla: `C-PRD` falso, `C-DIS` falso (corrige un texto ya aprobado dentro de
un patrón vigente, no propone forma nueva), `C-ARQ` falso, `C-USO` falso.

```text
DEF · errata:   CON → VER  [→ ENT si C-ENT]
```

No es un carril rápido ni una excepción: es **la misma regla de derivación aplicada a un
item pequeño**, con la misma traza de `no activadas`. *Se confirma formalmente en (e).*

---

## b.15 — Pruebas de conformidad de la sección (b)

```text
T26 PROCESO ÚNICO      Ningún item tiene dos procesos. Un cambio de naturaleza produce
                       o cambio de proceso con traza, o item nuevo enlazado. Nunca ambos.

T27 ESTADO DERIVADO    El estado global de todo item coincide con f(estados de paquete)
                       más las banderas declaradas. Divergencia = defecto de cálculo.

T28 AUTORIDAD DE       Ninguna transición ejecutada por quien no la tiene declarada en
    TRANSICIÓN         b.4. Toda transición registra su atribución completa.

T29 ACICLICIDAD        Ninguna ruta contiene ciclos salvo gates conjuntos declarados.
                       Ningún ciclo de dependencias entre items sin escalar.

T30 SUSPENSIÓN         Ningún paquete salió de `en curso` sin cerrar y sin checkpoint.

T31 BLOQUEO ÚTIL       Todo paquete `bloqueado` nombra su desbloqueador. Ningún
                       `bloqueado` usado donde correspondía `esperando-dependencia`.

T32 DESPACHO           Mismo estado ⇒ misma selección (determinismo, incluido el
    DETERMINISTA       desempate por id). Toda selección deja escrito qué se eligió,
                       por qué, y qué se excluyó y por qué.

T33 CIERRE             Ningún item cerrado sin las TRES condiciones de b.9, incluida la
                       declaración de integración semántica del propietario global.

T34 APARCADO           Ningún item aparcado desaparcado por el sistema. Toda dependencia
    RESPETADO          sobre un item aparcado fue REPORTADA al Owner.

T35 ORDEN NATURAL      Una orden en lenguaje natural produce el mismo tipo de evento que
                       una del tablero. Ninguna orden unívoca y reversible pidió
                       confirmación. El Owner no tuvo que nombrar ningún id.

T36 CONTINÚA           Desde un repo frío, sin conversación previa: DSP reconstruye,
                       verifica contra el repo, reporta en pocas líneas y retoma un
                       paquete desde su checkpoint exacto.

T37 COLA VACÍA         Con la cola vacía, el sistema NO inventó trabajo. Recorrió las
                       seis salidas de b.13 en orden y, si no había nada, lo dijo.

T38 RECOMPOSICIÓN      Ninguna recomposición borró una capa depositada. Ninguna reinició
                       un paquete `en curso` que sobrevivía en la ruta nueva.
```
