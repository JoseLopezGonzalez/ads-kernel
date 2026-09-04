# MANIFIESTO PREVIO DE ASIGNACIÓN — GATE ÚNICO Y FINAL DE CERTIFICACIÓN DE `F6` · 2026-09-04

> **EMITIDO ANTES DE REPARTIR, y commiteado ANTES de que exista ningún revisor.** Una vez
> commiteado no se modifica. Es la condición que el encargo pone por delante de todo: *«antes
> de crear revisores: deriva el universo obligatorio; escribe y confirma un manifiesto previo
> mínimo; asigna cada fuente; exige cobertura íntegra de todo lo asignado»*.
>
> **ÉSTE ES EL ÚNICO GATE AUTORIZADO.** Después de su veredicto el método se detiene,
> cualquiera que sea el resultado: **no se corrigen sus hallazgos, no se abre otro gate, no se
> propone otro ciclo y no se inicia PesquerApp.** Se dice aquí, antes de repartir, para que
> ningún revisor pueda pensar que suavizar algo abre un camino, ni que endurecerlo lo cierra.
>
> **POR QUÉ EL GATE ANTERIOR NO FUE VÁLIDO, y qué se hace distinto.** El del 2026-09-03 cayó
> por COBERTURA: su revisor 1 declaró `ASIGNADO − LEÍDO ≠ ∅` con seis fuentes o rangos sin
> abrir, entre ellas `CONTRATO-RAIZ-EXTERNA.md` —elemento expreso de su lote— y `11-ARQ` §9.6
> entera, un rango asignado explícitamente. Aquí se corrige por donde falló: **el lote se
> dimensiona antes de repartir y se publica su tamaño en líneas**, para que «no me dio tiempo»
> sea una decisión del coordinador al asignar y no un descubrimiento del revisor al terminar.

## 1 · Objeto congelado del gate

```text
COMMIT CANDIDATO   7b9829cbfa68c12b9947db0f7a26a1d08ed7f003
TREE SHA           d2c0a0cde1fff37cbf5ee59cf7a5bd633a99e330
REFERENCIA REMOTA  refs/heads/review/f6-post-gate-corrections-candidate-20260904
RAMA DEL GATE      gate/f6-certificacion-final-20260904, creada sobre ese commit exacto
FECHA              2026-09-04
INTÉRPRETE         Python 3.12.14 · PyYAML 6.0.2
`fd633383…`        NO es ancestro, verificado

QUÉ TRAE           `O26` del Owner, inscrita LITERAL en la sede canónica append-only y
                   proyectada en `D115` y en `06-DEUDA` §3; la corrección finita de
                   `E-01`…`E-16` con `E-17` y `E-18` registrados y no maquillados; y la
                   pasada ÚNICA de corrección tras una auditoría adversarial independiente,
                   que cerró dos bloqueantes del aparato de medida y construyó el SELLADO
                   del diario de `g.7`, que no existía y que el propio auditor dio por hecho

ESTADO DECLARADO   `F4c` CERRADA · `F5` CERRADA · **`F6` INICIADA · EN CURSO** ·
                   **`F6` NO CERTIFICADA** · **PesquerApp BLOQUEADA**
                   `O26` acepta la ARQUITECTURA bajo OCHO condiciones y **NO certifica
                   ninguna candidata**. El criterio `B3` **NO** está declarado satisfecho.
```

## 2 · La línea base que el coordinador afirma, y que cada revisor debe REPRODUCIR

```text
34/34 validadores en verde · 34 evidencias publicadas · 0 problemas
682 casos en 18 baterías `unittest` · 3 escenarios E2E de 15/15, 25/25 y 24/24 pasos
133 infracciones deliberadas detectadas · 0 NO detectadas
CERO saltos ejecutados en las 34 evidencias
determinismo: dos corridas seguidas producen evidencia byte a byte idéntica
huella del kernel: 6075d888ff2c7b70
git status --porcelain VACÍO antes y después de la corrida
las TRES RESTAS del universo obligatorio: A=0 · B=0 · C=0
```

**Ninguna de esas cifras se cree: se reproduce.** Un revisor que no pueda reproducir una de
ellas lo dice con el comando y su salida, y eso es un hallazgo.

## 3 · El universo asignado, y su frontera DICHA

El universo del gate es la UNIÓN de dos poblaciones, y ninguna se elige a mano:

```text
(a) TODO componente modificado en los TRES CORTES de `F6` y en la corrección actual,
    derivado con `git diff --name-only 99b06d36..HEAD`      216 rutas, todas vivas
(b) las SEDES NORMATIVAS contra las que se juzga `F6`        11-ARQ (por rangos) ·
    `(g)` · `(b)` · `(a)` · la sede del Owner · `03-GOBIERNO` · `04-CONTRATOS` ·
    `05-PLAN` · `06-DEUDA` · `FUENTES-CANONICAS.yml` · `CHECKPOINT-ADS-NEXT` ·
    `C1`, `C2`, `C4`, `C5` · `DECISIONES-Y-CONTRADICCIONES` · el registro del gate anterior
```

**LA FRONTERA, DICHA Y NO CALLADA.** Quedan FUERA del lote los documentos históricos de los
gates de `F4c` —`16-` a `32-`— y los de `F5`, que el derivador de fuentes sí incluye en su
universo documental de 92 fuentes. **Se excluyen con su razón: `F4c` está CERRADA por
composición de dos juicios independientes y su cobertura la cerraron sus propios gates; este
gate juzga `F6`.** Un revisor que necesite uno de ellos para sostener un hallazgo lo abre y lo
dice; lo que no puede es callar que lo necesitó. La exclusión es del COORDINADOR, va firmada
aquí antes de repartir, y es atacable: si el adjudicador la considera material, el gate cae
por cobertura, y así debe ser.

## 4 · REGLA DE COBERTURA — literal, y sin atenuantes

```text
ASIGNADO − LEÍDO = ∅        para los DOS revisores

NO SE ADMITE                · fuente asignada sin abrir
                            · rango asignado sin leer
                            · `grep` o `awk` contados como lectura
                            · cobertura histórica delegada para un fichero MODIFICADO
                            · adjudicación si un revisor declara cobertura incompleta

SI UN REVISOR NO PUEDE      el gate es NO VÁLIDO. Su lectura NO se sustituye con la del
TERMINAR SU LOTE            adjudicador. Decirlo a tiempo es lo correcto; callarlo, no
```

**El tamaño de cada lote se publica aquí, en líneas, antes de repartir.** Si es inasumible, el
defecto es del reparto y del coordinador que lo firmó, no del revisor que lo declara.

## 5 · Lote del REVISOR 1 — ejecución, resistencia, estado durable, runtime, concurrencia, contención, raíz externa y Git multimáquina

```text
50611 líneas · 141 ficheros íntegros · más los rangos de `11-ARQ` de abajo

RANGOS DE `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, ÍNTEGROS Y OBLIGATORIOS
  §2  · disposición física del estado          L396-L3794     3399
  §6  · arquitectura de adaptadores            L5812-L6135     324
  §20 · CONTRATO OBLIGATORIO DE `F6`           L11907-L12151   245
```

```text
  docs/rediseno/g-ESTADO-DURABLE-APROBADA.md                                381
  kernel/.upstream-hash                                                       1
  kernel/KERNEL_CHANGELOG.md                                                555
  kernel/VERSION                                                              1
  kernel/VERSIONES.md                                                        74
  kernel/operativo/pruebas/evidencia/adaptadores-salida.txt                  85
  kernel/operativo/pruebas/evidencia/admision-salida.txt                    141
  kernel/operativo/pruebas/evidencia/agentes-salida.txt                      41
  kernel/operativo/pruebas/evidencia/arboles-salida.txt                      87
  kernel/operativo/pruebas/evidencia/arranque-salida.txt                     10
  kernel/operativo/pruebas/evidencia/cardinalidad-salida.txt                 51
  kernel/operativo/pruebas/evidencia/ciclo-salida.txt                       133
  kernel/operativo/pruebas/evidencia/composicion-procesos-salida.txt         10
  kernel/operativo/pruebas/evidencia/contencion-salida.txt                   51
  kernel/operativo/pruebas/evidencia/continua-salida.txt                     59
  kernel/operativo/pruebas/evidencia/contratos-salida.txt                    29
  kernel/operativo/pruebas/evidencia/e2e-f6-salida.txt                       85
  kernel/operativo/pruebas/evidencia/e2e-runtime-salida.txt                  87
  kernel/operativo/pruebas/evidencia/estado-durable-salida.txt              191
  kernel/operativo/pruebas/evidencia/estado-e2e-salida.txt                   57
  kernel/operativo/pruebas/evidencia/fuentes-salida.txt                      11
  kernel/operativo/pruebas/evidencia/gobierno-git-salida.txt                 89
  kernel/operativo/pruebas/evidencia/identidad-salida.txt                    57
  kernel/operativo/pruebas/evidencia/integridad-evidencia-salida.txt         59
  kernel/operativo/pruebas/evidencia/lint-salida.txt                          6
  kernel/operativo/pruebas/evidencia/macrocircuitos-salida.txt               71
  kernel/operativo/pruebas/evidencia/multimaquina-salida.txt                 39
  kernel/operativo/pruebas/evidencia/negativos-salida.txt                   272
  kernel/operativo/pruebas/evidencia/raiz-externa-salida.txt                117
  kernel/operativo/pruebas/evidencia/recuentos-salida.txt                    11
  kernel/operativo/pruebas/evidencia/referencias-salida.txt                  77
  kernel/operativo/pruebas/evidencia/runtime-salida.txt                     121
  kernel/operativo/pruebas/evidencia/sesion-nueva-salida.txt                 65
  kernel/operativo/pruebas/evidencia/versiones-salida.txt                    26
  kernel/operativo/raiz-externa/README.md                                   170
  kernel/operativo/raiz-externa/aislamiento.py                              397
  kernel/operativo/raiz-externa/anfitrion_firmante.py                        71
  kernel/operativo/raiz-externa/anfitrion_verificador.py                     73
  kernel/operativo/raiz-externa/atestacion.py                               321
  kernel/operativo/raiz-externa/errores.py                                  177
  kernel/operativo/raiz-externa/firma.py                                    280
  kernel/operativo/raiz-externa/instalar.py                                 245
  kernel/operativo/raiz-externa/verificador.py                              501
  kernel/operativo/runtime/00-RUNTIME.md                                    122
  kernel/operativo/runtime/CONTRATO-ADAPTADOR.md                            131
  kernel/operativo/runtime/CONTRATO-ADMISION.md                             130
  kernel/operativo/runtime/CONTRATO-ARBOLES-ADVERSARIALES.md                144
  kernel/operativo/runtime/CONTRATO-CONTENCION.md                           136
  kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md                       338
  kernel/operativo/runtime/CONTRATO-GOBIERNO-GIT-CONTROL.md                  99
  kernel/operativo/runtime/CONTRATO-RAIZ-EXTERNA.md                         208
  kernel/operativo/runtime/CONTRATO-RUNTIME-Y-DISPATCHER.md                 156
  kernel/operativo/runtime/adaptadores/__init__.py                           75
  kernel/operativo/runtime/adaptadores/contrato.py                          185
  kernel/operativo/runtime/adaptadores/proceso.py                           583
  kernel/operativo/runtime/adaptadores/proyeccion.py                        175
  kernel/operativo/runtime/adaptadores/puntero.py                           184
  kernel/operativo/runtime/adaptadores/registro.py                          105
  kernel/operativo/runtime/admision/__init__.py                             283
  kernel/operativo/runtime/admision/censo.py                                429
  kernel/operativo/runtime/admision/errores.py                              142
  kernel/operativo/runtime/admision/formulas.py                             524
  kernel/operativo/runtime/admision/lectura.py                              279
  kernel/operativo/runtime/admision/matriz.py                               291
  kernel/operativo/runtime/admision/mutacion.py                             181
  kernel/operativo/runtime/admision/perimetro.py                            422
  kernel/operativo/runtime/ads_admision.py                                  512
  kernel/operativo/runtime/ads_arboles.py                                   401
  kernel/operativo/runtime/ads_ciclo.py                                     737
  kernel/operativo/runtime/ads_estado.py                                    684
  kernel/operativo/runtime/ads_runtime.py                                   708
  kernel/operativo/runtime/arboles/__init__.py                               58
  kernel/operativo/runtime/arboles/ataques.py                               612
  kernel/operativo/runtime/arboles/derivador.py                             299
  kernel/operativo/runtime/arboles/errores.py                                96
  kernel/operativo/runtime/arboles/suite.py                                 265
  kernel/operativo/runtime/arboles/versiones.py                             430
  kernel/operativo/runtime/contencion/__init__.py                            65
  kernel/operativo/runtime/contencion/backends.py                           407
  kernel/operativo/runtime/contencion/deteccion.py                          346
  kernel/operativo/runtime/contencion/ejecutor.py                           224
  kernel/operativo/runtime/contencion/errores.py                             88
  kernel/operativo/runtime/contencion/politica.py                            99
  kernel/operativo/runtime/estado/__init__.py                               106
  kernel/operativo/runtime/estado/atestacion.py                             267
  kernel/operativo/runtime/estado/bloqueo.py                                173
  kernel/operativo/runtime/estado/diario.py                                1064
  kernel/operativo/runtime/estado/errores.py                                271
  kernel/operativo/runtime/estado/fallos.py                                 123
  kernel/operativo/runtime/estado/migracion.py                              220
  kernel/operativo/runtime/estado/motor.py                                 1817
  kernel/operativo/runtime/estado/reconciliacion.py                         517
  kernel/operativo/runtime/estado/rutas.py                                  424
  kernel/operativo/runtime/estado/serializacion.py                          192
  kernel/operativo/runtime/estado/transaccion.py                            365
  kernel/operativo/runtime/gobierno/POLITICA-CONTROL-REPO.yml               163
  kernel/operativo/runtime/gobierno/__init__.py                              65
  kernel/operativo/runtime/gobierno/control.py                              497
  kernel/operativo/runtime/gobierno/errores.py                              118
  kernel/operativo/runtime/gobierno/git.py                                  332
  kernel/operativo/runtime/gobierno/propiedad.py                            182
  kernel/operativo/runtime/identidad/__init__.py                             63
  kernel/operativo/runtime/identidad/configuracion.py                       206
  kernel/operativo/runtime/identidad/errores.py                              96
  kernel/operativo/runtime/identidad/proveedor.py                           178
  kernel/operativo/runtime/identidad/rotacion.py                            202
  kernel/operativo/runtime/pruebas/catalogo_de_prueba.py                    143
  kernel/operativo/runtime/pruebas/escenario_e2e_runtime.py                 700
  kernel/operativo/runtime/pruebas/escenario_extremo_a_extremo.py           635
  kernel/operativo/runtime/pruebas/test_adaptadores.py                      743
  kernel/operativo/runtime/pruebas/test_admision.py                        1158
  kernel/operativo/runtime/pruebas/test_arboles.py                          492
  kernel/operativo/runtime/pruebas/test_contencion.py                       379
  kernel/operativo/runtime/pruebas/test_estado_durable.py                  2747
  kernel/operativo/runtime/pruebas/test_gobierno_git.py                     677
  kernel/operativo/runtime/pruebas/test_identidad.py                        533
  kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py           905
  kernel/operativo/runtime/pruebas/test_multimaquina.py                     693
  kernel/operativo/runtime/pruebas/test_raiz_externa.py                    1158
  kernel/operativo/runtime/pruebas/test_runtime.py                         2067
  kernel/operativo/runtime/pruebas/test_sesion_nueva.py                     894
  kernel/operativo/runtime/runtime/__init__.py                              107
  kernel/operativo/runtime/runtime/dispatcher.py                           1495
  kernel/operativo/runtime/runtime/ejecucion.py                             344
  kernel/operativo/runtime/runtime/errores.py                               171
  kernel/operativo/runtime/runtime/estado_util.py                            92
  kernel/operativo/runtime/runtime/fallos.py                                108
  kernel/operativo/runtime/runtime/lease.py                                 390
  kernel/operativo/runtime/runtime/modelo.py                                440
  kernel/operativo/runtime/runtime/politica.py                              302
  kernel/operativo/runtime/runtime/vistas.py                                171
  kernel/operativo/validadores/comprobar_evidencia.py                       590
  kernel/operativo/validadores/comprobar_negativos.py                      1544
  kernel/operativo/validadores/entorno.py                                   142
  kernel/operativo/validadores/negativos_cardinalidad.py                    277
  kernel/operativo/validadores/negativos_contratos19.py                     308
  kernel/operativo/validadores/negativos_integridad.py                       92
  kernel/operativo/validadores/negativos_runtime.py                         484
  kernel/operativo/validadores/registrar_evidencia.py                       228
  tooling/new-project.sh                                                    220
  tooling/workspace.py                                                      835
```

## 6 · Lote del REVISOR 2 — contratos, §19, C2/C4/C5, F6-H, b.12, matriz, autoridad y fases

```text
51161 líneas · 84 ficheros íntegros · más los rangos de `11-ARQ` de abajo

RANGOS DE `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, ÍNTEGROS Y OBLIGATORIOS
  §7  · runtime y dispatcher                   L6136-L6284     149
  §8  · los cuatro macrocircuitos              L6285-L7377    1093
  §9  · certificación, CON §9.6 ENTERA         L7378-L8074     697
  §10 · Git y multi-repositorio                L8075-L8128      54
  §18 · orden de construcción para `F6`        L10882-L11069   188
  §19 · límites de esta fase                   L11070-L11906   837
```

> **`11-ARQ` §9.6 va EXPRESAMENTE en este lote y entera.** Es la sede de las filas `X-S` de la
> `FASE 0` que `F6-F` debe demostrar, y es uno de los rangos que el gate anterior asignó y NO
> se leyó. Se nombra aquí para que su omisión no pueda pasar como descuido.

```text
  docs/canonico/00-EMPEZAR-AQUI.md                                          162
  docs/canonico/03-GOBIERNO-Y-AUTORIDAD.md                                  229
  docs/canonico/04-CONTRATOS-TECNICOS.md                                    409
  docs/canonico/05-PLAN-DE-IMPLEMENTACION-F5-F6.md                          251
  docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md                         476
  docs/canonico/FUENTES-CANONICAS.yml                                       782
  docs/evolucion/00-INDICE.md                                               333
  docs/evolucion/CHECKPOINT-ADS-NEXT.md                                    6385
  docs/evolucion/verificacion/derivar-universo-obligatorio.py              1367
  docs/f5/validar-f5.py                                                     612
  docs/f6/00-ESTADO-DE-IMPLEMENTACION-F6.md                                 322
  docs/f6/01-MATRIZ-DE-COMPLETITUD-F6.md                                    512
  docs/f6/02-GATE-DE-CERTIFICACION-FINAL-20260903.md                        296
  docs/owner/ADS-OWNER-RESOLUCIONES.md                                      979
  docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md                            1625
  docs/rediseno/a-CAPACIDADES-APROBADA.md                                  1150
  docs/rediseno/b-RECORRIDO-APROBADA.md                                    1331
  kernel/operativo/00-INDICE.md                                             146
  kernel/operativo/circuitos/00-CIRCUITOS.md                                243
  kernel/operativo/circuitos/DIS-handoffs.md                                249
  kernel/operativo/circuitos/entregas-de-8-0.md                             128
  kernel/operativo/circuitos/handoffs-generales.md                          305
  kernel/operativo/contratos/00-INDICE.md                                    29
  kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md                 161
  kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md                        539
  kernel/operativo/contratos/C4-MATERIALIZACION.md                          170
  kernel/operativo/contratos/C5-HANDOFF.md                                  115
  kernel/operativo/entrada/03-FORMAS.md                                     561
  kernel/operativo/entrada/05-ESCENARIOS.md                                 649
  kernel/operativo/esquemas/proceso.yaml                                     89
  kernel/operativo/pruebas/RECUENTOS-generado.md                             40
  kernel/operativo/pruebas/REGISTRO-generado.md                             254
  kernel/operativo/pruebas/REGISTRO.md                                      147
  kernel/operativo/pruebas/T086-T092-contratos.md                           165
  kernel/operativo/pruebas/T100-T121-capacidades.md                         359
  kernel/operativo/pruebas/T136-T152-post-auditoria.md                      466
  kernel/operativo/pruebas/T172-T181-estado-durable.md                      466
  kernel/operativo/pruebas/T182-T194-runtime-y-admision.md                  337
  kernel/operativo/pruebas/T195-T209-ciclo-y-macrocircuitos.md              342
  kernel/operativo/pruebas/T210-T225-arboles-raiz-externa-y-contencion.md    379
  kernel/operativo/pruebas/T226-T249-agentes-y-modelos.md                   367
  kernel/operativo/pruebas/T240-T248-hallazgos-externos-f6.md               220
  kernel/operativo/pruebas/T250-T269-cardinalidad-y-seleccion.md            502
  kernel/operativo/pruebas/T270-T289-contratos-19-y-composicion.md          244
  kernel/operativo/pruebas/T290-T311-integridad-evidencia-y-contencion.md    523
  kernel/operativo/recorrido/01-PROCESOS.md                                 606
  kernel/operativo/runtime/CONTRATO-CICLO-Y-MACROCIRCUITOS.md               338
  kernel/operativo/runtime/ciclo/__init__.py                                161
  kernel/operativo/runtime/ciclo/agentes.py                                 702
  kernel/operativo/runtime/ciclo/cierre.py                                  330
  kernel/operativo/runtime/ciclo/continuacion.py                            739
  kernel/operativo/runtime/ciclo/corpus.py                                  762
  kernel/operativo/runtime/ciclo/despacho.py                                107
  kernel/operativo/runtime/ciclo/durable.py                                 108
  kernel/operativo/runtime/ciclo/encuadre.py                                384
  kernel/operativo/runtime/ciclo/equipos.py                                1568
  kernel/operativo/runtime/ciclo/errores.py                                 436
  kernel/operativo/runtime/ciclo/gates.py                                   242
  kernel/operativo/runtime/ciclo/handoffs.py                                442
  kernel/operativo/runtime/ciclo/paralelismo.py                             211
  kernel/operativo/runtime/ciclo/planificacion.py                           400
  kernel/operativo/runtime/ciclo/procesos.py                                284
  kernel/operativo/runtime/ciclo/rutas.py                                   385
  kernel/operativo/runtime/macrocircuitos/__init__.py                        93
  kernel/operativo/runtime/macrocircuitos/definicion.py                     645
  kernel/operativo/runtime/macrocircuitos/errores.py                        171
  kernel/operativo/runtime/macrocircuitos/fase0.py                          575
  kernel/operativo/runtime/macrocircuitos/motor.py                          407
  kernel/operativo/runtime/pruebas/escenario_e2e_f6.py                     1529
  kernel/operativo/runtime/pruebas/test_agentes.py                         1053
  kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py        1115
  kernel/operativo/runtime/pruebas/test_ciclo.py                           1595
  kernel/operativo/runtime/pruebas/test_continua.py                         849
  kernel/operativo/runtime/pruebas/test_macrocircuitos.py                   879
  kernel/operativo/validadores/ads_lint.py                                  655
  kernel/operativo/validadores/comprobar_arranque.py                        605
  kernel/operativo/validadores/comprobar_composicion_procesos.py            816
  kernel/operativo/validadores/comprobar_contratos.py                      1091
  kernel/operativo/validadores/comprobar_fuentes.py                         368
  kernel/operativo/validadores/comprobar_recuentos.py                       756
  kernel/operativo/validadores/comprobar_referencias.py                     271
  kernel/operativo/validadores/comprobar_versiones.py                       456
  kernel/operativo/validadores/exclusiones.yaml                             196
  kernel/operativo/validadores/validadores.yaml                             397
```

## 7 · Los VEINTE ataques obligatorios, repartidos

```text
REVISOR 1   9 commit/tree desacoplados · 10 inversión pasos 8/9 · 11 `commit_de_nacimiento=None`
            12 `--repo` con PYTHONPATH contaminado · 13 evidencia con skips
            14 error tipado atravesando `main()` · 15 contención no cableada · 16 `setsid`
            17 custodia efímera presentada como productiva · 18 identidad de escritura compartida
REVISOR 2   1 cardinalidad plural de `C4` · 2 varios agentes sin integrador
            3 competencia sin criterio · 4 volumen superior al contexto · 5 `execution_slots`
            6 cada obligación de §19 · 7 cada criterio de `b.12` · 8 inanición
            19 mutación de una condición de `O26` · 20 matriz que omita una obligación
LOS DOS     para cada propiedad crítica: sano → VERDE · sabotaje → ROJO POR EL MOTIVO
            ESPERADO · restaurado → VERDE. Un sabotaje que sólo pone roja la huella del
            kernel NO cuenta: la huella salta con cualquier edición legítima
```

## 8 · El ADJUDICADOR

Recibe los dos dictámenes **sólo cuando ambos estén cerrados**, y **reproduce personalmente
toda razón capaz de cambiar el veredicto**. No resuelve por mayoría y no copia a nadie sin
verificar: el gate anterior dejó escrito que *«los dos revisores se equivocaron en cosas
distintas y ninguno merece ser copiado sin verificación»*.

Emite CUATRO declaraciones separadas —`A` validez · `B` completitud · `C` `O26` y `B3` ·
`D` certificación— y la `E` de PesquerApp, con las palabras literales que el encargo fija.

## 9 · Lo que este gate NO hará, pase lo que pase

```text
NO CORREGIRÁ   ni un byte. Los hallazgos quedan REGISTRADOS y NO APLICADOS
NO SUSTITUIRÁ  la lectura de un revisor por la del adjudicador
NO INICIARÁ    PesquerApp, ni siquiera si certifica: `O26` §6 lo reserva a una orden expresa
               del Owner que defina producto, repositorios, alcance y condiciones de parada
NO ABRIRÁ      ningún ciclo posterior ni ningún segundo gate
NO TOCARÁ      `redesign/kernel-2.0`, ni ninguna referencia anterior
```
