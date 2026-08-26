# ENMIENDA E1 a la SECCIÓN (a) — `ENC` como decimoquinta capacidad base

```text
identificador   E1
enmienda a      docs/rediseno/a-CAPACIDADES-APROBADA.md
fecha           2026-08-26
autoridad       Owner
motivo          resolución del hallazgo A-01 de la auditoría independiente
origen          docs/rediseno/AUDITORIA-INDEPENDIENTE-LOCAL.md §A-01
                docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md §C1 y §O1
estado          APROBADA
```

> **Qué es este documento.** La sección (a) permanece **íntegra y sin reescribir**. Esta
> enmienda es el único texto que la modifica, y lo hace por sustitución explícita: cada
> apartado dice qué texto de (a) sustituye y qué texto pasa a regir. Un lector de (a) que
> llegue a cualquiera de los cinco puntos de abajo debe leer aquí.
>
> **Lo que esta enmienda NO hace:** no altera ninguna otra decisión de (a), no cambia la
> autoridad de ninguna otra capacidad, no toca los frenos, ni el contrato de veto, ni la
> condición de paralelismo, ni el checkpoint, ni las pruebas T01–T25.

---

## E1.0 — La decisión

`ENC · ENCUADRE` queda aprobada como **decimoquinta capacidad base del kernel**, con código
reservado `ENC`, sin prefijo de espacio de nombres.

**Motivo.** El trabajo que `ENC` ejecuta es **semántico y conversacional**, y (a) afirma en
a.3 que `DSP` no tiene autoridad sobre el contenido de ninguna capa. Alojar dentro de `DSP`
un trabajo que escucha, interpreta, conversa, hace brainstorming, mide incertidumbre y da
forma profesional a una intención convertiría a `DSP` en una capacidad con trabajo de
contenido, lo que contradice su propia ficha. La contradicción no se resuelve moviendo
carpetas: se resuelve reconociendo que son dos capacidades distintas.

Lo que `ENC` hace, y por lo que merece ficha propia:

```text
[ ] recibe la expresión original del Owner, por cualquier canal
[ ] conserva literalmente lo dicho, con fecha y canal, antes de interpretar nada
[ ] identifica el anclaje contra lo que ya existe, incluido lo que NO existe
[ ] conversa, pregunta y hace brainstorming mientras la intención no esté madura
[ ] distingue la naturaleza: comentario · observación · nota · idea · orden · decisión ·
    candidato · y el tipo de proceso propuesto cuando lo hay
[ ] convierte una expresión suficientemente comprendida en uno o varios encuadres
    profesionales de los que DSP puede hacer nacer items
[ ] puede terminar legítimamente SIN crear ningún item
```

**Descartadas expresamente**, y no se reabren: devolver `ENC` dentro de `DSP`; declararla
`local:ENC` o extensión de pack.

### Texto de (a) que sustituye

| en (a) | decía | pasa a decir |
|---|---|---|
| a.0, bloque de tres niveles | «14 base, extensible» | «**15** base, extensible» |
| a.3, título | «El catálogo · 14 capacidades» | «El catálogo · **15** capacidades» |
| a.4, «Colisión de identificador» | «El kernel reserva los **catorce** códigos de tres letras» | «El kernel reserva los **quince** códigos de tres letras» |

El resto de a.4 —prefijo obligatorio para toda extensión de pack o de profile, imposibilidad
de sombrear una capacidad del kernel, colisión de autoridad— **queda intacto y sigue rigiendo
sin cambio alguno**. `ENC` no es una extensión: es catálogo base, y por eso no lleva prefijo.

---

## E1.1 — La frontera entre `ENC` y `DSP`

`ENC` **comprende y da forma profesional a la intención**.
`DSP` es el **runtime mecánico de despacho y coordinación**.

```text
ENC · ENCUADRE                          DSP · DESPACHO
─────────────────────────────────────   ─────────────────────────────────────
escucha al Owner                        registra
conserva la expresión literal           mantiene identidad y coherencia de estado
ancla contra lo existente               aplica eventos autorizados
conversa, pregunta, hace brainstorming   compone y recompone rutas
mide la incertidumbre                   genera proyecciones y vistas derivadas
clasifica la naturaleza                 despacha paquetes
formula el encuadre                     vigila estados, dependencias y frenos
entrega el encuadre a DSP               hace nacer el item del encuadre entregado
```

**Prohibiciones recíprocas, que son la frontera:**

```text
DSP NO interpreta por sí mismo el contenido de producto, de diseño ni de dominio
DSP NO decide semánticamente una cancelación
DSP NO sustituye el trabajo conversacional de ENC
DSP NO reescribe la interpretación, el resultado perseguido ni la evidencia de cierre

ENC NO crea items: entrega encuadres
ENC NO compone rutas, ni crea paquetes, ni despacha
ENC NO tiene autoridad de contenido sobre ninguna capa posterior
ENC NO decide en materia de autoridad del Owner: prepara y pregunta
```

**Memoria: sin duplicación.** El **índice de lo existente** es memoria propia de `ENC`, y
deja de serlo de `DSP`.

### Texto de (a) que sustituye

En a.3, dentro de la ficha de `DSP`, la función **Encuadre** decía:

> «**Encuadre** — id, enunciado de una línea de lo que de verdad se pide, naturaleza, y
> **dosier de anclaje** […] Se apoya en el **índice de lo existente**, memoria propia de DSP.»

Pasa a decir:

> «**Encuadre** — el **trabajo conversacional y semántico** del encuadre —escuchar,
> conservar la expresión literal, interpretar, anclar, conversar, medir incertidumbre y
> formular— lo ejecuta la capacidad **`ENC`**, que entrega a `DSP` un encuadre en estado
> `listo-para-dsp`. El **índice de lo existente** es memoria propia de `ENC`. `DSP` recibe
> ese encuadre y, a partir de él, escribe la ficha del item, le da identidad persistente y
> compone la ruta. `DSP` **puede devolver** el encuadre a `ENC` por falta de un campo
> estructural que le impida componer ruta; **no puede** cambiar su contenido.»

`DSP` conserva por tanto **tres** funciones propias —Enrutamiento, Estado y Supervisión— más
la **recepción** del encuadre que `ENC` le entrega. Donde a.3 dice «Cuatro funciones», debe
leerse: **Recepción del encuadre · Enrutamiento · Estado · Supervisión**.

---

## E1.2 — Materialización: `ENC` NO es un equipo permanente

> **Aprobar una capacidad en el catálogo no materializa un equipo, y materializar un equipo
> no lo hace permanente.** Son tres cosas distintas y confundirlas produce exactamente el
> defecto que a.4 y T12 existen para impedir.

```text
CAPACIDAD DISPONIBLE          está en el catálogo instalado. No consume nada. No tiene
                              tablero, ni cola, ni agentes. Existir en el catálogo es
                              gratis y no es un equipo.

EQUIPO MATERIALIZADO          tiene tablero, cola, memoria viva y agentes ocupando roles,
                              PORQUE existe trabajo real que lo necesita. Se materializa
                              por la señal de a.4 y se retira por la regla de retirada.

EQUIPO PERMANENTEMENTE        se materializa al instalar y NO se retira nunca, porque sin
ACTIVO                        él no hay sistema operativo. Son DOS: DSP y SIS.
```

**`ENC` es capacidad disponible siempre, y equipo materializado bajo demanda.** Se
materializa cuando existe trabajo real de entrada o de encuadre —una expresión del Owner que
atender, un encuadre en conversación— y **se retira por la regla general de retirada de a.4**
como cualquier otra capacidad. Su **memoria persiste**: el índice de lo existente, el léxico
del Owner, el vivero y las preguntas resueltas sobreviven al equipo, y son lo que permite
rematerializarlo sin que el Owner repita contexto.

Que `ENC` no esté materializada **no cierra la puerta de entrada**: la señal de
materialización de a.4 —«el enrutador necesita activar una capacidad que no tiene equipo»— se
dispara con la primera expresión del Owner, igual que con cualquier otra capacidad.

### Texto de (a) que sustituye

a.4 decía, y **sigue diciendo sin cambio**:

> «**DSP y SIS se materializan siempre.** Sin ellas no hay sistema operativo.»

**Esta enmienda NO añade `ENC` a esa lista.** Se registra aquí expresamente para que ningún
contrato derivado lo haga: los equipos permanentemente activos siguen siendo **dos**.

---

## E1.3 — Impacto

```text
SOBRE (a)     cinco recuentos y dos párrafos, todos enumerados arriba. Ninguna otra
              decisión, autoridad, freno, veto, invariante ni prueba cambia.

SOBRE (b)     ninguno. b.7 «CREACIÓN» dice «Un disparador entra por DSP/Encuadre. DSP
              escribe la ficha...». Con E1.1 esa frase sigue siendo cierta: el encuadre
              ENTRA por la función de recepción de DSP, y DSP escribe la ficha. Lo que E1.1
              precisa es quién produjo el encuadre que entra. NO se enmienda (b).

SOBRE T18     `ENC` deja de ser una extensión sin prefijo: es catálogo base. T18 sigue
   y T23      aplicándose sin cambio a toda capacidad de pack o de profile.

SOBRE T12     ENC entra en el alcance de T12 como cualquier otra capacidad no permanente:
              un equipo ENC materializado sin cola durante dos auditorías es candidato a
              retirarse.

SOBRE EL      quince fichas de capacidad. Los recuentos dejan de escribirse a mano: se
CORPUS        derivan del corpus y se comprueban (ver `validadores/comprobar_recuentos.py`).
```

## E1.4 — Trazabilidad

Esta enmienda **no modifica el fichero de la sección (a)** más allá de un bloque de aviso en
su cabecera que remite aquí. El texto original de (a) permanece legible tal como fue
aprobado el 2026-08-25, y lo que rige es (a) **leída junto a esta enmienda**. Las enmiendas
futuras se numeran `E2`, `E3`… y se listan en el aviso de cabecera de (a).
