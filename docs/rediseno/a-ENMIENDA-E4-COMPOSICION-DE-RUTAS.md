# ENMIENDA `E4` a las SECCIONES (a) y (b) — composición de rutas: participantes y capacidad competente

```text
identificador   E4
enmienda a      docs/rediseno/b-RECORRIDO-APROBADA.md
                docs/rediseno/a-CAPACIDADES-APROBADA.md
fecha           2026-09-02
autoridad       Owner
motivo          dar productor al dictamen de verificación en la ruta de auditoría; admitir
                dominio, seguridad y diseño en la puesta en marcha de un producto nuevo; y
                sustituir un método nombrado donde corresponde una capacidad
origen          docs/owner/ADS-OWNER-RESOLUCIONES.md · O23 §7
                docs/evolucion/11-ARQUITECTURA-INTEGRADA.md · §16 PN-8, PN-13, PN-14
estado          APROBADA
```

> **Qué es este documento.** Las secciones `(a)` y `(b)` permanecen **íntegras y sin
> reescribir**. Esta enmienda es el único texto que las modifica. Los tres apartados de
> abajo son **tres decisiones distintas del Owner** que se aplican en **un solo acto**
> porque afectan a la misma tabla: agruparlas evita tres pasadas sobre material aprobado y
> **no** las convierte en una sola decisión.
>
> **Lo que esta enmienda NO hace:** no añade ninguna capacidad al catálogo, no cambia
> ninguna obligación de proceso, no altera qué exige una participación, y no toca los
> derivados del kernel — eso es trabajo de `F6`, y en ese orden.

---

## `E4.0` — La decisión

```text
1  VERIFICACIÓN entra como participante CONDICIONAL en la ruta de auditoría, y es la
   PRODUCTORA del dictamen que esa ruta necesita
2  DOMINIO, SEGURIDAD y DISEÑO entran como participantes CONDICIONALES en los procesos por
   los que se pone en marcha un producto nuevo, cuando la materia del descubrimiento
   requiera sus capacidades
3  donde una tabla de participación colocó un MÉTODO, pasa a nombrarse la CAPACIDAD
   competente con su condición de participación
```

**Descartadas expresamente**, y no se reabren: nombrar otro productor del dictamen distinto
de verificación; sacar el descubrimiento de dominio y diseño del paso de puesta en marcha; y
conservar el método como participante declarando que designa a la capacidad.

## `E4.1` — La ruta de AUDITORÍA gana el productor de su dictamen

### Texto de `b.16` que AMPLÍA · fila `AUD`, L895

```text
DECÍA          obligatorias: INV
               condicionales: DOM `C-DOM` · SEG `C-SEG` · DIS/Reconstrucción `C-DIS` ·
                              PRD sólo si produce una decisión de producto

PASA A DECIR   obligatorias: INV
               condicionales: DOM `C-DOM` · SEG `C-SEG` · DIS `C-DIS` ·
                              VER `C-VER` · PRD sólo si produce una decisión de producto
```

**Y la precisión que le da sentido, porque sin ella la fila no resuelve nada:**

```text
VER es la PRODUCTORA del DICTAMEN en la ruta de auditoría. Una celda de cobertura sólo
alcanza `verificado` CON EVIDENCIA cuando ese dictamen existe. Ninguna otra capacidad lo
produce, y su ausencia deja la celda sin evidencia posible.
```

### Texto de `b.16` que AMPLÍA · el vocabulario de condiciones

**`b.16` exige que toda condicional lleve su CONDICIÓN DE ACTIVACIÓN escrita y COMPROBABLE**,
y su bloque de vocabulario se autodeclara «declarado una vez, reutilizado en todas las
rutas». Introducir `C-VER` en una fila sin declararlo ahí dejaría un identificador **usado y
sin definir**. Se añade al bloque:

```text
C-VER   la auditoría debe producir una celda de cobertura VERIFICADA, es decir con su
        DICTAMEN como evidencia. El inventario, la detección y la propuesta NO la
        activan
```

> **Las condiciones de `DOM`, `SEG` y `DIS` NO se inventan:** son `C-DOM`, `C-SEG` y `C-DIS`,
> ya declaradas en ese mismo bloque, y esta enmienda las reutiliza sin redefinirlas.

## `E4.2` — La puesta en marcha de un producto NUEVO admite a dominio, seguridad y diseño

### Texto de `b.16` que AMPLÍA · filas `SIS` e `INV`

```text
FILA `SIS`   DECÍA          condicionales: ENT obligatorio si modifica el runtime ·
                                           APR `C-APR`
             PASA A DECIR   condicionales: ENT obligatorio si modifica el runtime ·
                                           APR `C-APR` ·
                                           DOM:condiciones `C-DOM` · SEG:condiciones
                                           `C-SEG` · DIS `C-DIS`

FILA `INV`   DECÍA          condicionales: CON:experimental cuando la evidencia exija
                                           construir · PRD o ARQ según destino declarado ·
                                           APR `C-APR`
             PASA A DECIR   condicionales: CON:experimental cuando la evidencia exija
                                           construir · PRD o ARQ según destino declarado ·
                                           APR `C-APR` ·
                                           DOM `C-DOM` · SEG `C-SEG` · DIS `C-DIS`
```

**La condición de activación, declarada:**

```text
DOM, SEG y DIS entran CUANDO LA MATERIA DEL DESCUBRIMIENTO LO REQUIERA — es decir, cuando el
paso de descubrimiento de producto, dominio y diseño de una instalación nueva tenga que
establecer modelo de dominio, condiciones de seguridad o sistema de diseño.

NO entran por defecto, y ampliar un proceso por conveniencia sigue estando prohibido.
```

**Alcance, y no se pasa de ahí:** el paso de descubrimiento de una instalación nueva y el
paso de arranque que incorpora el dictamen de seguridad. **No alcanza a las rutas que ya
declaran esas participaciones por otras vías**, que no se tocan.

## `E4.3` — La capacidad competente sustituye al método

### Texto de `b.16` que SUSTITUYE · fila `AUD`, L895

```text
DICE           DIS/Reconstrucción `C-DIS`
PASA A DECIR   DIS `C-DIS`
```

### Texto de `a.6` que SUSTITUYE · L495

```text
DICE           AUD  INV ∥ DOM ∥ SEG ∥ DIS/Reconstrucción → [PRD si hay decisión de
               producto] → APR
PASA A DECIR   AUD  INV ∥ DOM ∥ SEG ∥ DIS → [PRD si hay decisión de producto] → APR
```

### Y la precisión que impide que el defecto vuelva

```text
UNA RUTA NOMBRA CAPACIDADES, NO MÉTODOS. Cuál de los métodos de una capacidad se ejecuta lo
calcula la ESCALA DE NOVEDAD, y la ruta no lo predetermina.

Nombrar un método en una tabla de participación PREDETERMINA lo que la escala prohíbe
predeterminar, y por eso se corrige en la fuente y no sólo en el derivado.
```

> **Por qué había que tocar la fuente aprobada y no bastaba corregir el kernel.** La misma
> cadena vivía en material aprobado. Corregir sólo el derivado habría dejado la fuente
> diciendo lo contrario, y la comprobación mecánica «contra la fuente» habría seguido
> fallando. **`F5` toca la fuente; `F6` toca el derivado, y en ese orden.**

## `E4.4` — Impacto

```text
SOBRE (b)     b.16 recibe una participación condicional nueva en tres filas, y una
              sustitución de identificador en una. Ningún texto de regla cambia
SOBRE (a)     a.6 recibe la misma sustitución de identificador. Nada más
SOBRE LAS      la composición que la tabla deriva pasa a ser verificable mecánicamente
COMPOSICIONES  CONTRA LA FUENTE, que es lo que hoy no se podía hacer
SOBRE F6      F6 alinea los derivados del kernel que nombran el método donde va la
              capacidad. EL ORDEN IMPORTA: primero la fuente, después el derivado
```

## `E4.5` — Trazabilidad

| presión | qué resuelve | apartado |
|---|---|---|
| `PN-8` | el productor del dictamen en la ruta de auditoría | `E4.1` |
| `PN-13` | dominio, seguridad y diseño en la puesta en marcha de un producto nuevo | `E4.2` |
| `PN-14` | la capacidad competente en lugar del método, en las DOS sedes aprobadas | `E4.3` |

**Prueba posterior:** que una celda de cobertura pueda alcanzar `verificado` CON EVIDENCIA;
que el paso de descubrimiento pueda abrir con dominio y diseño; y que ninguna tabla de
participación de `(a)` ni de `(b)` nombre un método donde corresponde una capacidad.
