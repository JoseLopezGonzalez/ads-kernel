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

## Los dos documentos del Owner

Están escritos en **voz del Owner**, no en el lenguaje canónico del corpus. Se conservan
literales: reescribirlos para que cumplieran el vocabulario del kernel sería reescribir la
orden. Por eso quedan declarados en
[`exclusiones.yaml`](../../kernel/operativo/validadores/exclusiones.yaml) como exentos de
vocabulario, y **sólo de eso**: sus enlaces se comprueban como los de cualquier documento.

| | |
|---|---|
| [`ADS-NEXT-OWNER-BRIEF.md`](ADS-NEXT-OWNER-BRIEF.md) | la directiva maestra: veintiséis apartados de visión, requisitos y criterios |
| [`PROMPT-ARRANQUE-ADS-NEXT.md`](PROMPT-ARRANQUE-ADS-NEXT.md) | el prompt de arranque que ordena ejecutarla, y en qué orden |

## Lo que la directiva ordena antes de diseñar nada

El apartado 23 del brief prohíbe saltar a implementar features. Exige cuatro trabajos
previos. Éstos son sus artefactos, y su estado:

| | trabajo | artefacto | estado |
|---|---|---|---|
| 23.1 | baseline del ADS actual | [`01-BASELINE-ADS.md`](01-BASELINE-ADS.md) | **entregado**, con evidencia ejecutada |
| 23.2 | mapa de la directiva contra ADS | [`02-MAPA-DIRECTIVA.md`](02-MAPA-DIRECTIVA.md) | **entregado** |
| — | decisiones que no se modifican en silencio | [`03-INVARIANTES.md`](03-INVARIANTES.md) | **entregado** |
| — | plan de investigación y protocolo de minería | [`04-PLAN-DE-INVESTIGACION.md`](04-PLAN-DE-INVESTIGACION.md) | **entregado** |
| 23.3 | minería de proyectos reales | [`05-CANDIDATOS.md`](05-CANDIDATOS.md) | **primera pasada entregada**: PesquerApp, frontend y backend. Q3 respondida, Q1 con indicios |
| 23.4 | síntesis | — | no iniciada: Q1 exige un proyecto independiente |
| 23.5 | diseño integrado | — | no iniciada: depende de 23.4 |

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
