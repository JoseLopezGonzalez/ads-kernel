# ADS NEXT — índice de la iniciativa

La directiva del Owner que ordena la siguiente evolución de ADS, y los trabajos que esa
directiva exige **antes** de cerrar ninguna arquitectura objetivo.

```text
docs/rediseno/     la ESPECIFICACIÓN NORMATIVA vigente — (a), (b) y su enmienda E1.
                   Aprobada. Nada de aquí la modifica.
docs/evolucion/    la DIRECTIVA del Owner y el trabajo previo que ordena: baseline,
                   mapa, invariantes, plan de investigación y minería.
kernel/operativo/  el CONTENIDO OPERATIVO construido sobre (a) y (b).
```

## Los documentos en voz del Owner

Están escritos en **voz del Owner**, no en el lenguaje canónico del corpus. Se conservan
literales: reescribirlos para que cumplieran el vocabulario del kernel sería reescribir la
orden. Por eso quedan exentos de vocabulario en
[`exclusiones.yaml`](../../kernel/operativo/validadores/exclusiones.yaml), y **sólo de eso**:
sus enlaces se comprueban como los de cualquier documento.

> **`docs/owner/` es su destino canónico**, fijado por la resolución `O10`. La exención pasa a
> ser **por ubicación** en vez de fichero a fichero, que es el remedio manual que ya había
> fallado cinco veces. Los dos documentos multi-repo ya viven ahí. La directiva, su prompt y
> el documento de pendientes siguen en `docs/evolucion/` con su exención propia, y su
> migración está declarada pendiente en `exclusiones.yaml`.

| | |
|---|---|
| [`ADS-NEXT-OWNER-BRIEF.md`](ADS-NEXT-OWNER-BRIEF.md) | la directiva maestra: veintiséis apartados de visión, requisitos y criterios |
| [`PROMPT-ARRANQUE-ADS-NEXT.md`](PROMPT-ARRANQUE-ADS-NEXT.md) | el prompt de arranque que ordena ejecutarla, y en qué orden |
| [`ADS-ARQUITECTURA-MULTIREPO-APROBADA.md`](../owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md) | **decisión aprobada para implementación**: un producto ADS son varios repositorios gobernados por un repositorio ADS de control |
| [`ADS-IDEAS-PENDIENTES-MULTIREPO.md`](../owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md) | documento de trabajo: ideas consolidadas y cuestiones que el Owner declara abiertas |
| [`ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md`](ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md) | **material temporal de evolución**: qué quedó aceptado, qué sigue propuesto y qué debe sintetizarse tras F2. No es normativa vigente ni autoriza a implementar su contenido |

> **`ARQUITECTURA` e `IDEAS` se contradicen sobre la misma pregunta**, y la contradicción no
> se resuelve por lectura. Está registrada, con las dos posturas escritas, en
> [`07-DECISION-MULTIREPO.md`](07-DECISION-MULTIREPO.md).

## Lo que la directiva ordena antes de diseñar nada

El apartado 23 del brief prohíbe saltar a implementar features. Exige cuatro trabajos
previos. Éstos son sus artefactos, y su estado:

| | trabajo | artefacto | estado |
|---|---|---|---|
| 23.1 | baseline del ADS actual | [`01-BASELINE-ADS.md`](01-BASELINE-ADS.md) | **entregado**, con evidencia ejecutada |
| 23.2 | mapa de la directiva contra ADS | [`02-MAPA-DIRECTIVA.md`](02-MAPA-DIRECTIVA.md) | **entregado** |
| — | decisiones que no se modifican en silencio | [`03-INVARIANTES.md`](03-INVARIANTES.md) | **entregado** |
| — | plan de investigación y protocolo de minería | [`04-PLAN-DE-INVESTIGACION.md`](04-PLAN-DE-INVESTIGACION.md) | **entregado** |
| 23.3 | minería de proyectos reales | [`05-CANDIDATOS.md`](05-CANDIDATOS.md) | **cerrada**: PesquerApp, frontend y backend, única fuente externa madura de esta fase |
| — | contraste de cada candidato contra el corpus | [`06-CONTRASTE.md`](06-CONTRASTE.md) | **entregado**: 29 veredictos y seis problemas arquitectónicos registrados |
| — | la decisión multi-repo del Owner, y su contradicción | [`07-DECISION-MULTIREPO.md`](07-DECISION-MULTIREPO.md) | **entregado**: registrada, y resuelta por el Owner |
| — | **mandato multi-repositorio** | `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` · `C6` · `C7` | **implementado**, y después corregido: release 2.0.0-alpha.6 |
| — | qué está demostrado de la implementación, y qué no | [`08-EVIDENCIA-MULTIREPO.md`](08-EVIDENCIA-MULTIREPO.md) | **entregado**: `CA-1`–`CA-17` y §100, criterio a criterio, con su grado de evidencia |
| 23.4 | síntesis | [`09-SINTESIS.md`](09-SINTESIS.md) | **entregada**: seis hallazgos, resolución propuesta para `X1`–`X5`, tres contradicciones nuevas y el destino de cada propuesta |
| — | crítica independiente de la síntesis, y la puerta correctiva que abre | [`10-CRITICA-INDEPENDIENTE-F3.md`](10-CRITICA-INDEPENDIENTE-F3.md) | **entregada**: seis hallazgos sobre F3, las resoluciones `O7`–`O14` del Owner y el defecto de vigencia de `T158` |
| 23.5 | diseño integrado | [`11-ARQUITECTURA-INTEGRADA.md`](11-ARQUITECTURA-INTEGRADA.md) | **entregada y después CORREGIDA** por devolución independiente: el modelo integrado, la disposición física del estado, cuatro tipos de estado nuevos, los cuatro macrocircuitos y cuatro presiones normativas vigentes. **NO certificada** |
| — | crítica independiente de F4, y su aplicación | [`12-CRITICA-INDEPENDIENTE-F4.md`](12-CRITICA-INDEPENDIENTE-F4.md) | **entregada**: nueve bloques de hallazgos sobre F4, las correcciones aplicadas y `D23`–`D33`. **Pendiente de SEGUNDA revisión independiente**: quien aplicó la crítica es quien la recibió |

El registro reanudable de todo ello es
[`CHECKPOINT-ADS-NEXT.md`](CHECKPOINT-ADS-NEXT.md). **Basta decir «Continúa»**: la
siguiente acción exacta está al final de ese fichero.

## Lo que este directorio NO es

```text
NO es una enmienda a (a) ni a (b)      esas se aprueban por su propio proceso, y este
                                       directorio registra la presión que la directiva
                                       ejerce sobre ellas — no la resuelve por su cuenta
NO es la arquitectura objetivo         la directiva prohíbe cerrarla antes de la minería
NO es kernel construido                nada de aquí añade una línea ejecutable al sistema
```

## Relación con el trabajo anterior

[`docs/rediseno/README.md`](../rediseno/README.md) fijaba como siguiente trabajo el
**piloto en un proyecto real**, y el checkpoint de aquella iniciativa lo detalla paso a
paso. La directiva no lo cancela: lo **amplía y lo reordena**, porque la minería exige
entrar en esos mismos proyectos reales antes de instalarles nada. Cuál de los dos ocurre
primero está resuelto en [`04-PLAN-DE-INVESTIGACION.md`](04-PLAN-DE-INVESTIGACION.md), y el
motivo por el que ese trabajo no choca con el freno de racha `SIS` está en
[`03-INVARIANTES.md`](03-INVARIANTES.md).

## Lo que este trabajo ha corregido de sí mismo

El contraste con el corpus desmintió tres afirmaciones de las fases anteriores. Están
listadas, con su fuente, en [`06-CONTRASTE.md`](06-CONTRASTE.md) — y corregidas en el
documento donde se escribieron. La más importante: el gobierno Git no estaba ausente, y el
hallazgo real es que la línea 2.0 nunca recogió lo que la 1.3.0 ya gobernaba.
