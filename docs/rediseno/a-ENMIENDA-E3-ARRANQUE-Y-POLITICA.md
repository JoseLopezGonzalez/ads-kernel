# ENMIENDA `E3` a las SECCIONES (a) y (b) — el gate constitucional de arranque, y el trabajo que nace por política

```text
identificador   E3
enmienda a      docs/rediseno/a-CAPACIDADES-APROBADA.md
                docs/rediseno/b-RECORRIDO-APROBADA.md
fecha           2026-09-02
autoridad       Owner
motivo          fijar, regla a regla, la disposición de las reglas constitucionales del
                circuito de arranque frente al diseño de macrocircuitos; y reconocer la
                tercera vía de nacimiento del trabajo que la política aprobada ya autoriza
origen          docs/owner/ADS-OWNER-RESOLUCIONES.md · O23 §5 y §6
                docs/evolucion/11-ARQUITECTURA-INTEGRADA.md · §16 PN-15, PN-2, PN-3
estado          APROBADA
```

> **Qué es este documento.** Las secciones `(a)` y `(b)` permanecen **íntegras y sin
> reescribir**. Esta enmienda es el único texto que las modifica, y lo hace por sustitución
> y ampliación explícitas: cada apartado dice qué texto de la fuente afecta y qué pasa a
> regir. Un lector de `(a)` o `(b)` que llegue a cualquiera de los puntos de abajo debe leer
> aquí.
>
> **Lo que esta enmienda NO hace:** no deroga ninguna regla constitucional, no altera el
> gate de salida del circuito de arranque, no autoriza a ningún agente a crear trabajo fuera
> de una política aprobada, no toca la sección `(g)`, no implementa nada y no inicia `F6`.

---

## `E3.0` — La decisión

**Se CONSERVA el gate constitucional de arranque, y el circuito de instalación que el diseño
de macrocircuitos describe queda SUBORDINADO a él.** Permanecen vigentes su plazo, sus diez
entregables obligatorios y sus cuatro prohibiciones.

**Y se reconoce expresamente una TERCERA VÍA de nacimiento del trabajo:** la apertura
automática por una política previamente aprobada.

**Descartadas expresamente**, y no se reabren: sustituir el gate constitucional por el gate
del circuito nuevo; y hacer que la apertura automática opere sin política vigente.

## `E3.1` — Las cuatro reglas constitucionales, una por una

**La forma de esta tabla no es una elección de estilo.** La prueba posterior de la presión
que originó esta enmienda exige **una fila por cada regla, que la nombre y declare su
disposición**. Una declaración global no la satisface.

### Texto de `a.11` que AMPLÍA

`a.11` es la única lista que deroga o ajusta reglas de la línea anterior. **Su texto actual
no se toca**, y se le añade esta fila:

| regla | disposición | qué pasa a regir |
|---|---|---|
| **`G20`** macrocircuitos | **CONSERVADA ÍNTEGRA** | el diseño de macrocircuitos los DESCRIBE; no los deroga ni los sustituye |
| **`G21`** gates entre circuitos | **CONSERVADA ÍNTEGRA** | incluida su reserva expresa de que el gate de salida del circuito inicial **lo fija la constitución y NO es negociable por el sistema** |
| **`G22`** gate fijo del circuito 0 | **CONSERVADA ÍNTEGRA** | su **plazo**, sus **DIEZ entregables obligatorios** y sus **CUATRO prohibiciones** siguen vigentes, uno a uno, sin excepción |
| **`G23`** línea base de producto | **CONSERVADA ÍNTEGRA** | sin cambio |

**Ninguna de las cuatro queda derogada, sustituida, ajustada ni pendiente.** Las cuatro se
CONSERVAN, y esta tabla lo declara **una fila por regla**, que es la forma que su prueba
posterior exige.

### Y la regla de subordinación que la acompaña

```text
EL CIRCUITO DE INSTALACIÓN que el diseño de macrocircuitos describe es la INSTRUMENTACIÓN
del gate constitucional del circuito inicial, y NO su sustituto.

CONSECUENCIAS, y son tres:
  1  una instalación real satisface el gate constitucional. Sus pasos intermedios NO lo
     sustituyen y NO lo relajan
  2  las salidas del circuito de instalación se CORRESPONDEN con los diez entregables
     obligatorios. La correspondencia se demuestra entregable a entregable, y demostrarla
     es trabajo de `F6`
  3  el plazo y las cuatro prohibiciones se aplican al circuito completo
```

> **Por qué el sistema no podía decidir esto.** La regla conservada declara que el criterio
> que aprueba la existencia del sistema lo fija la constitución **y no el sistema**, porque
> un sistema no puede definir sin conflicto de interés los criterios que aprueban su propia
> existencia. Por eso esta disposición la emite el Owner y no `F4` ni `F5`.

## `E3.2` — La tercera vía de nacimiento del trabajo

### Texto de `b.15.1` que AMPLÍA

El texto vigente reconoce que el trabajo nace de **una entrada del Owner** o de **un
desbloqueador dentro del alcance ya autorizado**. **Ese texto no se toca**, y se le añade
una tercera vía:

```text
TERCERA VÍA · APERTURA AUTOMÁTICA POR POLÍTICA APROBADA

  El trabajo PUEDE nacer de una POLÍTICA PREVIAMENTE APROBADA que lo abre de forma
  automática. No exige una petición individual del Owner.

  EXIGE, y las cuatro son condiciones y no recomendaciones:
    1  POLÍTICA VIGENTE, aprobada antes de que el trabajo nazca
    2  TRAZABILIDAD: qué política lo abrió, cuándo, y bajo qué disparador
    3  LÍMITES declarados: alcance, prioridad, presupuesto, umbrales y caducidad
    4  POSIBILIDAD DE SUSPENSIÓN, en cualquier momento y sin condiciones

  FUERA DE ESOS LÍMITES NO CREA TRABAJO. Detectar e inventariar sigue SIN crear trabajo.
```

### La frontera con `E3.1`, que es la que impide el atajo

```text
LA APERTURA AUTOMÁTICA NO ELUDE EL GATE CONSTITUCIONAL.

Una política aprobada decide QUÉ TRABAJO NACE y CUÁNDO. No decide qué gate lo aprueba, no
relaja el gate del circuito inicial, y no puede autorizar la salida de un circuito cuyo
gate la constitución reserva. Un trabajo nacido por política atraviesa EXACTAMENTE los
mismos gates que un trabajo nacido por petición del Owner.
```

## `E3.3` — La regla de ejecución desatendida, AJUSTADA y no levantada

### Texto de `a.11` que AMPLÍA

La regla constitucional que limita la ejecución desatendida **no queda levantada en
bloque**. Se le añade a la fila de reglas AJUSTADAS:

| | |
|---|---|
| **Ajustadas** | **`G03` se ajusta AL ALCANCE EXACTO que una política aprobada autoriza, y sólo a él.** Fuera de ese alcance, `G03` sigue vigente sin modificación. Lo que la política no declara, no queda autorizado |

## `E3.3 bis` — La regla de diario que estaba PENDIENTE deja de estarlo

### Texto de `a.11` que PRECISA · fila «PENDIENTES, no derogadas»

`a.11` declaraba `G26`/JOURNAL **PENDIENTE** con una condición escrita: «eso se decide al
diseñar memoria, eventos y recuperación en la sección `(g)`, **no ahora por inferencia**».

**Esa condición se ha cumplido.** La sección `(g)` existe, está aprobada por `O23` §2, y su
apartado `g.7` fija el DIARIO CANÓNICO —qué registra, qué sostiene, qué NO es, su sellado y
la retirada de cuerpos sellados—.

```text
PASA A REGIR   `G26` / JOURNAL deja de estar PENDIENTE y queda RESUELTA POR `(g)` `g.7`.
               El texto anterior SE CONSERVA, porque registra por qué estuvo pendiente y
               bajo qué condición dejaría de estarlo.
```

> **Por qué esto es parte de `PN-1` y no un extra.** La presión que exige la sección `(g)`
> presiona **dos** puntos de `(a)`: `a.9`, que delega la disposición física, y `a.11`, que
> declara esta regla pendiente «hasta diseñar memoria, eventos y recuperación en la sección
> `(g)`». Aprobar `(g)` sin tocar esta fila dejaría a `(a)` diciendo que la materia sigue
> sin decidir el mismo día en que se decide.

## `E3.4` — Impacto

```text
SOBRE (a)     a.11 recibe una fila nueva de reglas CONSERVADAS y una ampliación de la fila
              de reglas AJUSTADAS. Ningún texto anterior se retira
SOBRE (b)     b.15.1 recibe la tercera vía. Ningún texto anterior se retira
SOBRE (g)     ninguno. Esta enmienda no toca la disposición del estado durable
SOBRE F6      F6 actualiza la constitución en prosa, la guía de arranque y el resto de
              derivados, y demuestra la correspondencia entregable a entregable.
              EL ORDEN IMPORTA: primero la fuente, después el derivado
```

## `E3.5` — Trazabilidad

| presión | qué resuelve | apartado |
|---|---|---|
| `PN-15` | la disposición de las cuatro reglas constitucionales, regla a regla | `E3.1` |
| `PN-2` | la vía normativa de la política de recurrencia como fuente de trabajo | `E3.2` |
| `PN-3` | el ajuste acotado de la regla de ejecución desatendida | `E3.3` |

**Prueba posterior:** que `a.11` nombre `G20`, `G21`, `G22` y `G23` y declare la disposición
de cada una; que nombre `G03` y declare su ajuste; y que `b.15.1` declare la tercera vía con
sus cuatro condiciones.
