# ADS · EMPEZAR AQUÍ

**Ésta es la puerta de entrada del corpus canónico vigente de ADS.** Si vas a implementar
`F5` o `F6`, empieza en este documento y no en ningún otro.

> **QUÉ ES ESTE CORPUS.** Una edición canónica del estado VIGENTE de ADS, consolidada sobre
> el commit que cierra `F4c`. No sustituye a ninguna fuente: **la reordena, la clasifica y
> la enlaza**, de modo que un agente nuevo pueda entender el sistema y prepararlo para
> construir sin leer la historia de `F4c`.
>
> **QUÉ NO ES.** No es un gate, no es una certificación, no es una decisión nueva y no
> corrige deuda. No reabre `F4c`, no inicia `F5`, no inicia `F6` y no desbloquea PesquerApp.
> **No introduce ni una sola decisión arquitectónica.**

---

## 1 · Qué es ADS

**ADS —Autonomous Development System— es la constitución operativa de una organización de
agentes de IA que desarrolla software bajo gobierno humano.** No es una plantilla de
código, ni un framework, ni un agente: es el conjunto de contratos, roles, métodos,
procesos y verificadores con los que esa organización trabaja.

Tres frases que lo delimitan:

```text
1  ADS gobierna un PRODUCTO, no un repositorio. El producto puede estar repartido entre
   varios repositorios Git independientes, y ADS vive en uno de control aparte.

2  ADS no ejecuta trabajo: DECLARA quién puede hacer qué, con qué autoridad, siguiendo qué
   procedimiento, entregando qué evidencia y cerrando por qué gate. Los agentes ejecutan.

3  Todo lo que ADS afirma tiene que ser COMPROBABLE por alguien que no lo escribió. Ésa es
   la propiedad de la que dependen las demás.
```

## 2 · Qué problema resuelve

```text
EL PROBLEMA        Un equipo de agentes de IA sin organización declarada produce trabajo
                   que nadie puede auditar: no se sabe quién decidió qué, con qué
                   autoridad, ni qué evidencia sostiene una entrega. El coste no aparece
                   en el primer encargo; aparece cuando hay que corregir el décimo.

LO QUE ADS APORTA  · una CAPACIDAD por materia, con autoridad y veto declarados
                   · un ROL con procedimiento escrito y gate de salida, no criterio libre
                   · un RECORRIDO por resultado perseguido, no por capacidades usadas
                   · una ENTREGA entre equipos con comprobación previa a la custodia
                   · un ESTADO persistido con fuente única por verdad
                   · un gobierno GIT explícito, multi-repositorio y con autoridad por fuente
                   · VERIFICADORES ejecutables que hacen caer al corpus cuando se contradice

LO QUE NO RESUELVE ADS no elige el stack, no diseña el producto y no sustituye al Owner en
                   las decisiones que (a) y (b) le reservan.
```

## 3 · El orden exacto de lectura

**Lee estos documentos en este orden. Son todos los que necesitas.**

| # | documento | qué te da |
|---|---|---|
| 1 | este documento | qué es ADS, qué leer y qué no |
| 2 | [`01-MODELO-DEL-SISTEMA.md`](01-MODELO-DEL-SISTEMA.md) | las piezas del sistema y sus fronteras |
| 3 | [`02-MODELO-OPERATIVO.md`](02-MODELO-OPERATIVO.md) | cómo circula el trabajo, de la frase del Owner al cierre |
| 4 | [`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md) | quién manda sobre qué, y el estado vigente de las fases |
| 5 | [`04-CONTRATOS-TECNICOS.md`](04-CONTRATOS-TECNICOS.md) | qué contratos existen, dónde están y qué está construido |
| 6 | [`05-PLAN-DE-IMPLEMENTACION-F5-F6.md`](05-PLAN-DE-IMPLEMENTACION-F5-F6.md) | qué hay que construir, en qué orden |
| 7 | [`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](06-DEUDA-Y-LIMITACIONES-VIGENTES.md) | qué sigue abierto y qué lo cierra |
| — | [`FUENTES-CANONICAS.yml`](FUENTES-CANONICAS.yml) | el registro: una sede por materia, con su autoridad |

Después de estos siete, **las únicas lecturas necesarias son las fuentes técnicas que
ellos enlazan expresamente** —contratos, esquemas, validadores y código—, y sólo la que
necesites para lo que vayas a construir.

## 4 · Qué NO necesitas consultar para implementar

**Ninguno de estos documentos es lectura necesaria para construir `F5` o `F6`.** Se
conservan porque son evidencia de proceso y trazabilidad, no porque haya que leerlos:

```text
NO NECESARIO       los documentos numerados de gate de docs/evolucion/
                   los manifiestos de asignación y de lectura
                   los dictámenes de revisores y adjudicadores
                   el corrigendum de dictámenes inmutables
                   los checkpoints y partes de tanda
                   el registro histórico de correcciones de F4c
```

**Y hay una regla, no una recomendación:** un documento de gate **no puede ser fuente
normativa**. Su sede y su alcance están en
[`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md).

**La única excepción**, y es de consulta puntual y no de lectura: el documento
[`11-ARQUITECTURA-INTEGRADA.md`](../evolucion/11-ARQUITECTURA-INTEGRADA.md) **no es un
gate**: es la arquitectura entregada por `F4c` y contiene los contratos que `F6` debe
construir. Este corpus enlaza sus secciones una a una desde
[`04-CONTRATOS-TECNICOS.md`](04-CONTRATOS-TECNICOS.md) y
[`05-PLAN-DE-IMPLEMENTACION-F5-F6.md`](05-PLAN-DE-IMPLEMENTACION-F5-F6.md); **se entra por
la sección enlazada, no por el principio.**

## 5 · Estado vigente, construido y diseñado — dónde está, y por qué no está aquí

**Este documento NO copia el estado de las fases, ni el inventario de lo construido, ni la
lista de deuda.** Cada uno tiene una sola sede, y copiarla aquí crearía una segunda verdad
que caducaría sola:

| lo que buscas | su ÚNICA sede |
|---|---|
| estado de `F4c`, `F5`, `F6` y PesquerApp | [`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md) |
| qué está CONSTRUIDO y qué sólo DISEÑADO | [`04-CONTRATOS-TECNICOS.md`](04-CONTRATOS-TECNICOS.md) |
| jerarquía de autoridad y precedencia | [`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md) |
| deuda viva, con propietario y condición de cierre | [`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](06-DEUDA-Y-LIMITACIONES-VIGENTES.md) |
| sede canónica de cada materia | [`FUENTES-CANONICAS.yml`](FUENTES-CANONICAS.yml) |

## 6 · Cómo localizar contratos, esquemas y código existente

**El kernel operativo tiene su propio índice, y es la sede de la que cuelga todo lo
construido.** No se reproduce aquí:

| qué buscas | dónde está |
|---|---|
| índice del kernel operativo y mapa de fuente única | [`kernel/operativo/00-INDICE.md`](../../kernel/operativo/00-INDICE.md) |
| los contratos transversales | [`kernel/operativo/contratos/00-INDICE.md`](../../kernel/operativo/contratos/00-INDICE.md) |
| el lenguaje canónico y los tipos | [`kernel/operativo/esquemas/00-LENGUAJE.md`](../../kernel/operativo/esquemas/00-LENGUAJE.md) |
| los esquemas, uno por tipo | `kernel/operativo/esquemas/<tipo>.yaml` |
| las capacidades, sus roles, métodos y prompts | `kernel/operativo/capacidades/<COD>/` |
| los procesos y el cierre de item | [`kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md`](../../kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md) |
| los validadores ejecutables y su manifiesto | [`kernel/operativo/validadores/validadores.yaml`](../../kernel/operativo/validadores/validadores.yaml) |
| el tooling ejecutable | `tooling/workspace.py` · `tooling/new-project.sh` · `tooling/kernel-status.sh` · `tooling/compile-agents.sh` |
| la especificación normativa aprobada | [`docs/rediseno/`](../rediseno/README.md) |
| las resoluciones del Owner | [`docs/owner/ADS-OWNER-RESOLUCIONES.md`](../owner/ADS-OWNER-RESOLUCIONES.md) |

**Ninguna cifra de este corpus se escribe a mano.** Cuando necesites un recuento, derívalo:

```bash
# capacidades del kernel operativo
ls -1d kernel/operativo/capacidades/*/ | wc -l
# contratos transversales
ls -1 kernel/operativo/contratos/C*.md | wc -l
# esquemas de tipo canónico
ls -1 kernel/operativo/esquemas/*.yaml | wc -l
# procesos declarados
grep -c '^id: proceso:' kernel/operativo/recorrido/01-PROCESOS.md
# resoluciones del Owner en su sede canónica
grep -cE '^# `O[0-9]+`' docs/owner/ADS-OWNER-RESOLUCIONES.md
```

## 7 · Qué hacer después de leer

**Lo que viene ahora es CONSTRUIR**, y el orden de construcción está en
[`05-PLAN-DE-IMPLEMENTACION-F5-F6.md`](05-PLAN-DE-IMPLEMENTACION-F5-F6.md). Antes de
escribir una línea, dos lecturas obligadas: qué está ya construido, en
[`04-CONTRATOS-TECNICOS.md`](04-CONTRATOS-TECNICOS.md) §1 —**completar lo que existe, no
duplicarlo**—, y qué contratos quedan y qué los bloquea, en
[`docs/f6/00-ESTADO-DE-IMPLEMENTACION-F6.md`](../f6/00-ESTADO-DE-IMPLEMENTACION-F6.md), y
el juicio independiente que se ha emitido sobre él, en
[`docs/f6/02-GATE-DE-CERTIFICACION-FINAL-20260903.md`](../f6/02-GATE-DE-CERTIFICACION-FINAL-20260903.md)
—veredicto **`F6 NO CERTIFICADA`**, sobre un gate declarado **NO VÁLIDO**—.
El estado vigente de cada fase —y el acto que lo declaró— está en
[`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md) §6, que es su única sede;
**iniciar y cerrar una fase son actos del Owner y no de este corpus**.
