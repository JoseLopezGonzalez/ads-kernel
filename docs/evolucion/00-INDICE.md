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
| 23.5 | diseño integrado | [`11-ARQUITECTURA-INTEGRADA.md`](11-ARQUITECTURA-INTEGRADA.md) | **entregada y CORREGIDA DOCE VECES** —el recuento se DERIVA de los bloques de §15.8, y la corrección del gate de cierre es la decimotercera—: el modelo integrado, la disposición física del estado, cuatro tipos de estado nuevos, los cuatro macrocircuitos con la **sede canónica de composición de ruta** y el reparto Git citado de `C7`, y **DOCE** presiones normativas vigentes. **NO certificada** |
| — | crítica independiente de F4, y su aplicación | [`12-CRITICA-INDEPENDIENTE-F4.md`](12-CRITICA-INDEPENDIENTE-F4.md) | **entregada**: nueve bloques de hallazgos sobre F4, las correcciones aplicadas y `D23`–`D33` |
| — | segunda crítica independiente de F4 | [`13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md`](13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md) | **entregada**: veredicto de INSUFICIENCIA por revisor independiente con contexto limpio — dos hallazgos BLOQUEANTES, siete GRAVES y catorce nuevos. Correcciones aplicadas y `D34`–`D45`. **`F4c` sigue ABIERTA**: exige una TERCERA revisión independiente |
| — | devolución técnica previa a la tercera revisión | [`14-DEVOLUCION-TECNICA-PREVIA-F4C.md`](14-DEVOLUCION-TECNICA-PREVIA-F4C.md) | **entregada**: auditoría externa de Codex sobre el árbol remoto real — tres BLOQUEANTES, dos GRAVES, cuatro MEDIOS y dos MENORES, más un resto NO reproducido. **NO certifica `F4c`**: es revisión técnica, no veredicto de suficiencia. **Dos de sus prescripciones quedaron revisadas** por una corrección técnica posterior (`D52`, `D53`), y otras dos por una **SEGUNDA corrección técnica** (`D55`, `D56`) |

| — | **TERCERA REVISIÓN INDEPENDIENTE de F4c** | [`15-TERCERA-REVISION-INDEPENDIENTE-F4C.md`](15-TERCERA-REVISION-INDEPENDIENTE-F4C.md) | **entregada**: emitida por un revisor con contexto limpio que no escribió F4 ni aplicó ninguna de sus correcciones, sobre el árbol `df05929`. **Veredicto: INSUFICIENTE PARA F5** — DOS BLOQUEANTES, ocho GRAVES, cinco MEDIOS y siete MENORES, más quince hallazgos que intentó y NO pudo reproducir. **`F4c` NO se cierra y sigue ABIERTA.** Sus 22 hallazgos reproducibles quedan corregidos en una TANDA INTEGRADA posterior —`D64`–`D68`, `PN-11` y `PN-12`—, que **no modifica este documento**: el juicio es histórico e inmutable. Que estén corregidos no los da por bien resueltos |

| — | **GATE FINAL INDEPENDIENTE de F4c** | [`16-GATE-FINAL-INDEPENDIENTE-F4C.md`](16-GATE-FINAL-INDEPENDIENTE-F4C.md) | **entregado**: TRES agentes con contexto limpio —revisor A, revisor B y adjudicador C— sobre el árbol `a713590`. C verificó los **33 hallazgos uno a uno contra su fichero y su línea**, sin resolver por mayoría. **Su recuento en prosa —29 adjudicados y 13 medios— es erróneo**: su propia tabla da **32 y 16**, 31 distintos, y el documento 17 lo fija (`F-12`). El documento 16 **no se corrige**: es histórico e inmutable, y lo que se reancla es esta proyección. **Veredicto: INSUFICIENTE PARA F5** por DOS razones independientes: la cobertura del corpus quedó incompleta —su prosa dice **dieciocho** fuentes obligatorias sin abrir y su propia enumeración lista **DIECINUEVE**, que son las que el documento 17 cubrió— y hay **cuatro BLOQUEANTES y seis GRAVES confirmados**. **`F4c` NO se cierra y sigue ABIERTA; F5 NO queda autorizada.** Ningún hallazgo se corrigió en esa pasada |

| — | **COMPLEMENTO DE COBERTURA del gate · NIVEL 0** | [`17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md`](17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md) | **entregado**: cierra el requisito `0.1` del gate. TRES agentes con contexto limpio —revisores D y E en paralelo, adjudicador F— leen **las diecinueve fuentes obligatorias** que nadie había abierto (**8 310 líneas**). **`C5` NO resuelve `B-2`**, y la razón es estructural. **Ningún hallazgo retirado ni rebajado; ninguna severidad movida.** DOCE hallazgos nuevos, y el recuento real fijado: **32 adjudicados** —no 29— más 12 nuevos = **44 abiertos**. **`F4c` sigue ABIERTA y el veredicto vigente sigue siendo INSUFICIENTE PARA F5** |

| — | **TANDA INTEGRADA DE CORRECCIÓN del gate** | `11-ARQUITECTURA-INTEGRADA.md` · `DECISIONES-Y-CONTRADICCIONES.md` · `CHECKPOINT-ADS-NEXT.md` | **aplicada, y NO certificada**: cierra los **43 hallazgos distintos** —**44 filas**: 4 BLOQUEANTES, 6 GRAVES, 20 MEDIOS y 14 MENORES— derivados de los identificadores del documento 17. **Los seis GRAVES y tres de los cuatro BLOQUEANTES quedan `CORREGIDO_EN_F4`**; el cuarto, `B-2`, tiene su arquitectura corregida y su estado primario es `PRESION_LISTA_PARA_F5`, porque lo que le queda es la enmienda `PN-13` que sólo el Owner aprueba. Recuento derivado, **un estado primario por hallazgo**: **31 corregidos · 1 presión para F5 · 2 contrato completo para F6 · 8 externos con propietario · 1 histórico = 43**. Decisiones `D71`–`D86`; presiones vigentes **ONCE**, con `PN-13` como única nueva —cifras de aquella tanda; las vigentes hoy son las de la fila de abajo—. **No crea documento numerado**: la corrección vive en el documento 11, y los documentos 15, 16 y 17 permanecen **inmutables**. **`F4c` sigue ABIERTA y el veredicto vigente sigue siendo INSUFICIENTE PARA F5**: lo aplicó quien lo recibió |

| — | **GATE DE CIERRE INDEPENDIENTE de F4c** | [`18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md`](18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md) | **emitido**: TRES agentes con contexto limpio —revisores `G` y `H` en paralelo, adjudicador `I`— sobre el árbol `0a4b3a0` y el rango de corrección `7e99388…0a4b3a0`. `I` adjudicó **las 43 filas una a una**, sin resolver por mayoría, y corrigió a los dos revisores. **Veredicto: INSUFICIENTE PARA F5**, por DOS razones independientes: **catorce fuentes obligatorias sin lectura sustantiva** —diez de ellas de las diecinueve que el primer gate ya omitió, y el documento 15 asignado a los dos revisores y leído por ninguno— y **DIEZ de las 43 filas FALLIDAS**, con 28 hallazgos consolidados de los que **SEIS los introdujo la propia tanda de corrección**. **`F4c` NO se cierra y sigue ABIERTA; F5 NO queda autorizada.** Ningún hallazgo se corrigió en esta pasada |
| — | **CORRECCIÓN DEL GATE DE CIERRE** | `11-ARQUITECTURA-INTEGRADA.md` · `DECISIONES-Y-CONTRADICCIONES.md` · `CHECKPOINT-ADS-NEXT.md` · `00-INDICE.md` | **aplicada, y NO certificada.** Es la **DÉCIMA** tanda: cierra los **28 hallazgos consolidados** `I-01`–`I-28` del documento 18, más la fila `A7` —una de las diez FALLIDAS, sin número `I-nn` porque es fila de matriz—. Las ocho GRAVES: `I-01` retira `estado/cuarentena/` y la lleva a `.ads/run/quarantine/` **sin crear una tercera fuente de verdad**; `I-02` da al marcador de `deriva` las cinco piezas de disciplina y cambia la NORMA de §2.6.8; `I-03` limpia la capa B de las dos reglas que `D64` retiró; `I-04` corrige en cinco sedes el reparto Git contra `C7:80-92`; `I-05` §14; `I-06` las SEIS extensiones de ficha; `I-07` el gate de `INS-5` en §18; `I-08` registra `<CAP>:revision` como contrato F6. Decisiones **`D87`–`D95`**, todas revisoras; **`D67` RESTAURADA byte a byte al texto de `7e99388`**. Presiones vigentes **DOCE**, con **`PN-14`** como única nueva —de reclasificar `F-01`, cuya cadena está en material APROBADO—. Matriz recalculada: **31 · 2 · 2 · 7 · 1 = 43**, con `F-01` de externo a presión F5. **No crea documento numerado**, y los documentos 15, 16, 17 y **18** permanecen **inmutables**. **`F4c` sigue ABIERTA y el veredicto vigente sigue siendo INSUFICIENTE PARA F5**: lo aplicó quien lo recibió, por décima vez |

| — | **SNAPSHOTS PUBLICADOS Y CORRECCIONES POSTERIORES** | `review/f4c-candidate-20260828-r2` · `review/f4c-candidate-20260828-r3` · `CHECKPOINT-ADS-NEXT.md` | **publicados, y NO certificados.** Son **snapshots preservados**, no «la candidata actual». **`r2` = `1b588ac`**: publica la tanda y corrige `N158g`, que derivaba su fixture de la cifra publicada y dependía del orden del manifiesto; ahora la deriva del corpus vigente. **`r3` = `65cab54`**, POSTERIOR: hace **portable** la batería —calculaba mal la raíz y caía a una ruta codificada, comprobando el repositorio del autor desde cualquier otro clon—, corrige **`G-23`** para que compruebe la excepción exacta en vez de afirmar «kernel intacto», y hace verdadera **`G-24`**, que decía «legibles» y sólo contaba quince. **`r2` NO contiene los arreglos de `r3`.** El **árbol vigente** es sucesor de ambos y está **pendiente de publicación**; su SHA se deriva siempre con `git rev-parse` y `git ls-remote`, nunca de una cifra escrita aquí. Validado con Python 3.11.16: **13/13**, **57/57**, **67 detectadas y 0 NO detectadas**, `T158` **SUPERADA**, `T161` = **293**. El kernel operativo **sustantivo** sigue intacto, con la excepción NOMBRADA —`comprobar_negativos.py`, `.upstream-hash` y evidencia derivada—. **NADA DE ESTO ES ARQUITECTURA.** **`F4c` sigue ABIERTA, `F5` sigue NO AUTORIZADA, no se ha hecho merge en `redesign/kernel-2.0`, y el gate independiente TODAVÍA NO SE HA INICIADO** |

| — | **GATE DEFINITIVO INDEPENDIENTE de F4c** | [`19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md`](19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md) | **emitido**: TRES agentes con contexto limpio —revisores `J` y `K` en paralelo sin verse, adjudicador `L`— sobre `review/f4c-candidate-20260828-r4` = `0ea0451`. `L` verificó cada afirmación material contra su fichero y su línea, **sin resolver por mayoría**, y rechazó `J-09`, la base externa de `K-03` y su propio agravamiento de `K-11`. **Veredicto: INSUFICIENTE PARA F5**, por SEIS razones independientes: cobertura incompleta —~8 700 líneas de fuentes centrales que ningún revisor abrió—, un BLOQUEANTE arquitectónico (`J-01`, `revision_base` sin sede en §3.6), **SEIS** GRAVES, un contrato F6 que aún exige decidir arquitectura (`K-02`), una contradicción con `G20`–`G23` sin presión F5 (`K-06`) y un checkpoint no vigente. **Derivado de las filas adjudicadas: 25 planteados · 1 RECHAZADO (`J-09`) · 24 consolidados — BLOQUEANTE 1 · GRAVE 6 · MEDIO 10 · MENOR 7.** El texto literal de `L` dice «cinco graves» y enumera seis ids: se conserva intacto y la corrección va en el **corrigendum §12** del propio documento. **`F4c` NO se cierra y sigue ABIERTA; F5 NO queda autorizada.** Ningún hallazgo se corrigió en esa pasada |
| — | **CORRECCIÓN DEL GATE DEFINITIVO** | `11-ARQUITECTURA-INTEGRADA.md` · `DECISIONES-Y-CONTRADICCIONES.md` · `CHECKPOINT-ADS-NEXT.md` · `19-…F4C.md` §12 · `00-INDICE.md` · `entrada/02-CIRCUITO.md` | **APLICADA, NO CERTIFICADA.** `D96`–`D102`, todas revisoras: `revision_base` OBLIGATORIO en §3.6 y participante en `tx` —cierra el BLOQUEANTE `J-01` y el GRAVE `J-02` a la vez, sin nonce ni timestamp—; `PN-15` registra `G20`–`G23` como PRESIONADAS y **pendientes de F5, no derogadas**, con fila propia para `kernel/KERNEL.md` en §17; la regla de `D92` se reformula sobre **participación semántica** y alcanza `SEG` en `proceso:DEP`; las **CINCO** salidas del gate de `M7`; el `hash_previo` de la reparación unificado para las tres causas; `X62` da a §6.7 fila propia —46 filas, derivado—; y quedan contratos F6 completos para derivar los censos manuales y la guardia de intérprete. `O16` gana **procedencia real** —fecha, formulación presentada y respuesta literal del Owner— **sin crear `O17`**. `D1`–`D95` y `O1`–`O16` intactas. **DOCE de las trece condiciones `C-L` cerradas o registradas; `C-L.5` —la COBERTURA— sigue ABIERTA y sólo la cierra un gate nuevo mediante lectura real.** `F4c` sigue **ABIERTA**; F5 sigue **NO autorizada** |
| — | **CORRECCIÓN TÉCNICA SOBRE LA CANDIDATA** | `11-ARQUITECTURA-INTEGRADA.md` · `DECISIONES-Y-CONTRADICCIONES.md` · `CHECKPOINT-ADS-NEXT.md` · batería | **APLICADA, NO CERTIFICADA.** `D103`, acotada y sin abrir gate. `D98` había retirado el barrido léxico de su CRITERIO y lo **reintroducía en su ALGORITMO** —marcaba «condicionante» buscando «ANTES de construir» en texto libre—, y publicaba «seis procesos, diez pares», una cardinalidad **insatisfacible**. Derivado de campos ESTRUCTURADOS, el catálogo da **CINCO procesos y NUEVE pares**, con `(DEP, SEG)` por la obligatoria; y `proceso:AUD` **no tiene cardinalidad estática** —su propietario es DERIVADO por item, luego cada item exige `DOM:revision`, `SEG:revision` o **ninguna**, nunca las dos—. Los dos niveles se separan y **no se suman**. `G-15` pasaba en verde sobre ambos defectos: ahora **ejecuta la derivación** y contrasta la proyección con lo derivado, sin escribir el nueve en la prueba. `D98` no se reescribe; `D1`–`D102` y `O1`–`O16` intactas. Y el checkpoint deja de decir «todos corregidos»: las trece condiciones quedan en **cuatro estados** — 8 corregidas en F4c · 2 registradas para F5 · 2 contratadas para F6 · 1 abierta por cobertura. `F4c` sigue **ABIERTA**; F5 sigue **NO autorizada** |

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
