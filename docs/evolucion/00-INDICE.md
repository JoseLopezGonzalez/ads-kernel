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
| 23.5 | diseño integrado | [`11-ARQUITECTURA-INTEGRADA.md`](11-ARQUITECTURA-INTEGRADA.md) | **entregada y CORREGIDA NUEVE VECES**: el modelo integrado, la disposición física del estado, cuatro tipos de estado nuevos, los cuatro macrocircuitos con la **sede canónica de composición de ruta**, y **ONCE** presiones normativas vigentes. **NO certificada** |
| — | crítica independiente de F4, y su aplicación | [`12-CRITICA-INDEPENDIENTE-F4.md`](12-CRITICA-INDEPENDIENTE-F4.md) | **entregada**: nueve bloques de hallazgos sobre F4, las correcciones aplicadas y `D23`–`D33` |
| — | segunda crítica independiente de F4 | [`13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md`](13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md) | **entregada**: veredicto de INSUFICIENCIA por revisor independiente con contexto limpio — dos hallazgos BLOQUEANTES, siete GRAVES y catorce nuevos. Correcciones aplicadas y `D34`–`D45`. **`F4c` sigue ABIERTA**: exige una TERCERA revisión independiente |
| — | devolución técnica previa a la tercera revisión | [`14-DEVOLUCION-TECNICA-PREVIA-F4C.md`](14-DEVOLUCION-TECNICA-PREVIA-F4C.md) | **entregada**: auditoría externa de Codex sobre el árbol remoto real — tres BLOQUEANTES, dos GRAVES, cuatro MEDIOS y dos MENORES, más un resto NO reproducido. **NO certifica `F4c`**: es revisión técnica, no veredicto de suficiencia. **Dos de sus prescripciones quedaron revisadas** por una corrección técnica posterior (`D52`, `D53`), y otras dos por una **SEGUNDA corrección técnica** (`D55`, `D56`) |

| — | **TERCERA REVISIÓN INDEPENDIENTE de F4c** | [`15-TERCERA-REVISION-INDEPENDIENTE-F4C.md`](15-TERCERA-REVISION-INDEPENDIENTE-F4C.md) | **entregada**: emitida por un revisor con contexto limpio que no escribió F4 ni aplicó ninguna de sus correcciones, sobre el árbol `df05929`. **Veredicto: INSUFICIENTE PARA F5** — DOS BLOQUEANTES, ocho GRAVES, cinco MEDIOS y siete MENORES, más quince hallazgos que intentó y NO pudo reproducir. **`F4c` NO se cierra y sigue ABIERTA.** Sus 22 hallazgos reproducibles quedan corregidos en una TANDA INTEGRADA posterior —`D64`–`D68`, `PN-11` y `PN-12`—, que **no modifica este documento**: el juicio es histórico e inmutable. Que estén corregidos no los da por bien resueltos |

| — | **GATE FINAL INDEPENDIENTE de F4c** | [`16-GATE-FINAL-INDEPENDIENTE-F4C.md`](16-GATE-FINAL-INDEPENDIENTE-F4C.md) | **entregado**: TRES agentes con contexto limpio —revisor A, revisor B y adjudicador C— sobre el árbol `a713590`. C verificó los **33 hallazgos uno a uno contra su fichero y su línea**, sin resolver por mayoría. **Su recuento en prosa —29 adjudicados y 13 medios— es erróneo**: su propia tabla da **32 y 16**, 31 distintos, y el documento 17 lo fija (`F-12`). El documento 16 **no se corrige**: es histórico e inmutable, y lo que se reancla es esta proyección. **Veredicto: INSUFICIENTE PARA F5** por DOS razones independientes: la cobertura del corpus quedó incompleta —su prosa dice **dieciocho** fuentes obligatorias sin abrir y su propia enumeración lista **DIECINUEVE**, que son las que el documento 17 cubrió— y hay **cuatro BLOQUEANTES y seis GRAVES confirmados**. **`F4c` NO se cierra y sigue ABIERTA; F5 NO queda autorizada.** Ningún hallazgo se corrigió en esa pasada |

| — | **COMPLEMENTO DE COBERTURA del gate · NIVEL 0** | [`17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md`](17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md) | **entregado**: cierra el requisito `0.1` del gate. TRES agentes con contexto limpio —revisores D y E en paralelo, adjudicador F— leen **las diecinueve fuentes obligatorias** que nadie había abierto (**8 310 líneas**). **`C5` NO resuelve `B-2`**, y la razón es estructural. **Ningún hallazgo retirado ni rebajado; ninguna severidad movida.** DOCE hallazgos nuevos, y el recuento real fijado: **32 adjudicados** —no 29— más 12 nuevos = **44 abiertos**. **`F4c` sigue ABIERTA y el veredicto vigente sigue siendo INSUFICIENTE PARA F5** |

| — | **TANDA INTEGRADA DE CORRECCIÓN del gate** | `11-ARQUITECTURA-INTEGRADA.md` · `DECISIONES-Y-CONTRADICCIONES.md` · `CHECKPOINT-ADS-NEXT.md` | **aplicada, y NO certificada**: cierra los **43 hallazgos distintos** —**44 filas**: 4 BLOQUEANTES, 6 GRAVES, 20 MEDIOS y 14 MENORES— derivados de los identificadores del documento 17. **Los seis GRAVES y tres de los cuatro BLOQUEANTES quedan `CORREGIDO_EN_F4`**; el cuarto, `B-2`, tiene su arquitectura corregida y su estado primario es `PRESION_LISTA_PARA_F5`, porque lo que le queda es la enmienda `PN-13` que sólo el Owner aprueba. Recuento derivado, **un estado primario por hallazgo**: **31 corregidos · 1 presión para F5 · 2 contrato completo para F6 · 8 externos con propietario · 1 histórico = 43**. Decisiones `D71`–`D86`; presiones vigentes **ONCE**, con `PN-13` como única nueva. **No crea documento numerado**: la corrección vive en el documento 11, y los documentos 15, 16 y 17 permanecen **inmutables**. **`F4c` sigue ABIERTA y el veredicto vigente sigue siendo INSUFICIENTE PARA F5**: lo aplicó quien lo recibió |

| — | **GATE DE CIERRE INDEPENDIENTE de F4c** | [`18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md`](18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md) | **emitido**: TRES agentes con contexto limpio —revisores `G` y `H` en paralelo, adjudicador `I`— sobre el árbol `0a4b3a0` y el rango de corrección `7e99388…0a4b3a0`. `I` adjudicó **las 43 filas una a una**, sin resolver por mayoría, y corrigió a los dos revisores. **Veredicto: INSUFICIENTE PARA F5**, por DOS razones independientes: **catorce fuentes obligatorias sin lectura sustantiva** —diez de ellas de las diecinueve que el primer gate ya omitió, y el documento 15 asignado a los dos revisores y leído por ninguno— y **DIEZ de las 43 filas FALLIDAS**, con 28 hallazgos consolidados de los que **SEIS los introdujo la propia tanda de corrección**. **`F4c` NO se cierra y sigue ABIERTA; F5 NO queda autorizada.** Ningún hallazgo se corrigió en esta pasada |

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
