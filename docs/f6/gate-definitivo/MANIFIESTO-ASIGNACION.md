# MANIFIESTO PREVIO DE ASIGNACIÓN — GATE DEFINITIVO DE CERTIFICACIÓN DE `F6` · 2026-09-04

> **EMITIDO ANTES DE REPARTIR, y commiteado EN LA RAMA DEL GATE antes de que exista ningún
> revisor.** Una vez commiteado no se modifica.
>
> **Y ESTA VEZ VIVE FUERA DE LA CANDIDATA, que es `O27` §4 y es el remedio de `ADJ-GT1` y de
> `H-04`.** Los dos gates anteriores escribieron su manifiesto DENTRO del árbol que auditaban,
> y el efecto se midió: el acto de convocar el gate cambió el corpus que dos instrumentos del
> gate miden, y la línea base dejó de reproducirse sobre la rama del gate. Aquí la candidata
> es un SHA congelado que este documento **no toca**, y toda validación del producto se
> ejecuta sobre su checkout extraído con `git archive`, sin `.git` y sin este manifiesto
> dentro.

## 1 · Objeto congelado

```text
CANDIDATA        2ae0a93888a425cf85ba38d0ac054d069bbbe7d6
REFERENCIA       refs/heads/review/f6-final-candidate-after-c35791b-20260904
                 comprobada contra el REMOTO con `git ls-remote`, no contra la vista local
                 —`ADJ-GT4` del gate anterior, que confundió `refs/remotes/` con inexistencia—
RAMA DEL GATE    gate/f6-certificacion-definitiva-20260904, creada DESDE ese SHA
CHECKOUT         extraído con `git archive <sha> | tar -x`, SIN `.git` y SIN este manifiesto
INTÉRPRETE       Python 3.12.14 · PyYAML 6.0.2
`fd633383…`      NO es ancestro, NO se lee y NO se publica
```

## 2 · La línea base que el coordinador afirma, y que cada revisor debe REPRODUCIR

**Sobre el checkout congelado de la candidata**, no sobre esta rama:

```text
36/36 validadores en verde · 36 evidencias publicadas · 0 problemas
158 infracciones deliberadas detectadas · 0 NO detectadas
195 escenarios contrastados contra su evidencia · 72 no contrastables · 0 divergencias
universo obligatorio 58 · A=0 · B=0 · C=0 · 12 sabotajes del derivador sin fallo
comprobador de cobertura · 11 controles · 0 sin detectar
huella del kernel 7196ce99457a77d4, calculada = anclada
determinismo: dos corridas seguidas dan evidencia byte a byte idéntica
```

**Ninguna cifra se cree: se reproduce.** Un revisor que no pueda reproducir una lo dice con
el comando y su salida, y eso es un hallazgo.

## 3 · El universo, y cómo se reparte

El universo es la unión de **(a)** los **239 componentes modificados** en los tres cortes de
`F6` y en las dos correcciones posteriores —derivados con `git diff --name-only`, no elegidos—
y **(b)** las sedes normativas contra las que se juzga `F6`. `11-ARQ` entera se reparte por
secciones entre los tres, con inicio y fin de cada rango.

**Cada fichero lleva su SHA-256 y su número de líneas**, medidos sobre el checkout congelado.
Un revisor que lea un fichero cuyo SHA no case está leyendo otra cosa, y el comprobador lo
cuenta como NO leído.

```text
REV-1   40630 líneas   (-5.4 % sobre la media)
REV-2   40623 líneas   (-5.4 % sobre la media)
REV-3   47534 líneas   (+10.7 % sobre la media)
media   42929 líneas · ninguna diferencia de carga supera el 15 %
```

## 4 · COBERTURA BLOQUEANTE, NO DECLARATIVA — `O27` §5

Esto es lo que cambia respecto de los dos gates anteriores, y no es una promesa: es un
programa.

```text
docs/evolucion/verificacion/comprobar-cobertura-de-gate.py

  OBLIGATORIO − ASIGNADO                = ∅
  ASIGNADO − LEÍDO                      = ∅
  LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS      = ∅
  FUENTES MODIFICADAS − LEÍDAS ÍNTEGRAS = ∅
```

**Devuelve 0 sólo si las cuatro son vacías, y NO SE CREA AL ADJUDICADOR mientras no devuelva
0 para los tres revisores.** La unidad es la LÍNEA y no el fichero: cada revisor declara los
TRAMOS que leyó y su suma tiene que cubrir el fichero entero, de modo que «lo abrí» deja de
valer por «lo leí» y una búsqueda no puede colarse como lectura —no produce tramos contiguos
que cubran dos mil líneas—.

**Lo que NO cuenta como lectura**, y el comprobador lo hace cumplir: `grep` · `awk` ·
búsquedas · `diff` · ejecutar pruebas · **lo leído por otro agente**. Un revisor que declare
una fuente fuera de su lote no compensa nada, y así está medido.

**`OBLIGATORIO` se deriva del ÁRBOL** —las 239 modificadas— y el manifiesto sólo puede
AMPLIARLO. Esto se dice porque la primera versión de este instrumento tenía ahí una
TAUTOLOGÍA: `obligatorio − obligatorio`, con un manifiesto vacío dando cobertura completa. Lo
encontró la auditoría del 2026-09-04 (`H-06`) y está corregido, con cuatro autopruebas nuevas
que ejercen los casos vacuos.

## 5 · Lote del REVISOR 1 — código y ejecución

Estado durable, migración, runtime, dispatcher, `b.12`, `C2`/`C4`/`C5`, concurrencia,
recuperación, `Continúa`, macrocircuitos y contención.

```text
67 ficheros ÍNTEGROS · 8 rangos de `11-ARQ` · 40630 LÍNEAS EN TOTAL

RANGOS DE `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, ÍNTEGROS Y OBLIGATORIOS
  §1    L248   -L395        148 líneas
  §2    L396   -L3794      3399 líneas
  §4    L4948  -L5235       288 líneas
  §7    L6136  -L6284       149 líneas
  §8    L6285  -L7377      1093 líneas
  §14   L9155  -L9182        28 líneas
  §15   L9183  -L9785       603 líneas
  §17   L10853 -L10881       29 líneas

FICHEROS ÍNTEGROS · ruta · líneas · sha256 (12 primeros)
  kernel/operativo/runtime/adaptadores/__init__.py                             75  22882a8044d3
  kernel/operativo/runtime/adaptadores/contrato.py                            185  732d68a045d3
  kernel/operativo/runtime/adaptadores/proceso.py                             583  dbb1e5ef3bd5
  kernel/operativo/runtime/adaptadores/proyeccion.py                          175  a4cd3aa3cb11
  kernel/operativo/runtime/adaptadores/puntero.py                             184  6f1c7149ff3a
  kernel/operativo/runtime/adaptadores/registro.py                            105  19a2fce801a0
  kernel/operativo/runtime/ads_ciclo.py                                       771  a9e95ed44188
  kernel/operativo/runtime/ads_estado.py                                      711  1de6f0bbeec9
  kernel/operativo/runtime/ads_runtime.py                                     738  5bb5120d7b62
  kernel/operativo/runtime/ciclo/__init__.py                                  161  5459ca465d81
  kernel/operativo/runtime/ciclo/agentes.py                                   702  70fb7d5eb514
  kernel/operativo/runtime/ciclo/cierre.py                                    330  8623565762b1
  kernel/operativo/runtime/ciclo/continuacion.py                              739  f0f3af64226c
  kernel/operativo/runtime/ciclo/corpus.py                                    762  1fef062bd5f6
  kernel/operativo/runtime/ciclo/despacho.py                                  107  8b6e586772a1
  kernel/operativo/runtime/ciclo/durable.py                                   108  5a4c742471c9
  kernel/operativo/runtime/ciclo/encuadre.py                                  384  17272e2b7130
  kernel/operativo/runtime/ciclo/equipos.py                                  1568  e357f39534a4
  kernel/operativo/runtime/ciclo/errores.py                                   436  b760279a7145
  kernel/operativo/runtime/ciclo/gates.py                                     242  f344b251d79d
  kernel/operativo/runtime/ciclo/handoffs.py                                  442  518edd29c5e5
  kernel/operativo/runtime/ciclo/paralelismo.py                               211  4605d638fb84
  kernel/operativo/runtime/ciclo/planificacion.py                             400  2a85d17e8a41
  kernel/operativo/runtime/ciclo/procesos.py                                  284  6155d1f8fea3
  kernel/operativo/runtime/ciclo/rutas.py                                     385  fde521c1f01f
  kernel/operativo/runtime/contencion/__init__.py                              65  0bcd686312a3
  kernel/operativo/runtime/contencion/backends.py                             407  332cef1db4ec
  kernel/operativo/runtime/contencion/deteccion.py                            346  4340479e494a
  kernel/operativo/runtime/contencion/ejecutor.py                             224  247e7ce31ca2
  kernel/operativo/runtime/contencion/errores.py                               88  7ce37a9728d8
  kernel/operativo/runtime/contencion/politica.py                              99  688a953c6f55
  kernel/operativo/runtime/estado/__init__.py                                 106  f5de8af7aec0
  kernel/operativo/runtime/estado/atestacion.py                               267  7adbddb49c3e
  kernel/operativo/runtime/estado/bloqueo.py                                  173  b7fb332d09a1
  kernel/operativo/runtime/estado/diario.py                                  1064  d2a61a32f705
  kernel/operativo/runtime/estado/errores.py                                  271  998364bc25e5
  kernel/operativo/runtime/estado/fallos.py                                   123  69c8f5974183
  kernel/operativo/runtime/estado/migracion.py                                506  9ce3c594bb9a
  kernel/operativo/runtime/estado/motor.py                                   1817  384129559160
  kernel/operativo/runtime/estado/reconciliacion.py                           517  d77d09fa966a
  kernel/operativo/runtime/estado/rutas.py                                    424  18e0add349e9
  kernel/operativo/runtime/estado/serializacion.py                            192  77d8d727e85e
  kernel/operativo/runtime/estado/transaccion.py                              365  d5061f91fae6
  kernel/operativo/runtime/macrocircuitos/__init__.py                          93  baf2ba9714e9
  kernel/operativo/runtime/macrocircuitos/definicion.py                       645  dac5af0cc668
  kernel/operativo/runtime/macrocircuitos/errores.py                          171  ea30a207589f
  kernel/operativo/runtime/macrocircuitos/fase0.py                            575  25b7dc23ee08
  kernel/operativo/runtime/macrocircuitos/motor.py                            407  05fabf577179
  kernel/operativo/runtime/pruebas/escenario_extremo_a_extremo.py             729  602b5f5fd006
  kernel/operativo/runtime/pruebas/test_adaptadores.py                        743  3ab3961a175f
  kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py          1115  1dc4dbc77010
  kernel/operativo/runtime/pruebas/test_ciclo.py                             1602  f62b8a1fb764
  kernel/operativo/runtime/pruebas/test_contencion.py                         379  3ccd135a5da3
  kernel/operativo/runtime/pruebas/test_continua.py                           849  4e1d065d6e88
  kernel/operativo/runtime/pruebas/test_estado_durable.py                    3173  c2daaa0bc171
  kernel/operativo/runtime/pruebas/test_macrocircuitos.py                     879  a9829744aa59
  kernel/operativo/runtime/pruebas/test_runtime.py                           2071  904b131f1b71
  kernel/operativo/runtime/runtime/__init__.py                                107  33571dc2e212
  kernel/operativo/runtime/runtime/dispatcher.py                             1495  9b0ea3170d64
  kernel/operativo/runtime/runtime/ejecucion.py                               344  a5580ba3f1ad
  kernel/operativo/runtime/runtime/errores.py                                 171  135d7c762f13
  kernel/operativo/runtime/runtime/estado_util.py                              92  65a8d32293ca
  kernel/operativo/runtime/runtime/fallos.py                                  108  aa967873db34
  kernel/operativo/runtime/runtime/lease.py                                   390  a0907180674c
  kernel/operativo/runtime/runtime/modelo.py                                  440  b4620fffaa0d
  kernel/operativo/runtime/runtime/politica.py                                302  e88ca7d273df
  kernel/operativo/runtime/runtime/vistas.py                                  171  d1614cd02e64
```

## 6 · Lote del REVISOR 2 — seguridad y evidencia

Raíz externa, `O26`, firma, commit/tree, identidad, `--repo`, contaminación, `V6-15`,
admisión, Git multimáquina, evidencias, skips y sabotajes.

```text
103 ficheros ÍNTEGROS · 10 rangos de `11-ARQ` · 40623 LÍNEAS EN TOTAL

RANGOS DE `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, ÍNTEGROS Y OBLIGATORIOS
  §0    L95    -L247        153 líneas
  §3    L3795  -L4947      1153 líneas
  §5    L5236  -L5811       576 líneas
  §6    L5812  -L6135       324 líneas
  §10   L8075  -L8128        54 líneas
  §11   L8129  -L9013       885 líneas
  §12   L9014  -L9092        79 líneas
  §13   L9093  -L9154        62 líneas
  §16   L9786  -L10852     1067 líneas
  §20   L11907 -L12153      247 líneas

FICHEROS ÍNTEGROS · ruta · líneas · sha256 (12 primeros)
  kernel/operativo/pruebas/evidencia/adaptadores-salida.txt                    85  61413762896d
  kernel/operativo/pruebas/evidencia/admision-salida.txt                      199  61d850dde5ad
  kernel/operativo/pruebas/evidencia/agentes-salida.txt                        41  4aca40608352
  kernel/operativo/pruebas/evidencia/arboles-salida.txt                        87  54e186973ed2
  kernel/operativo/pruebas/evidencia/arranque-salida.txt                       10  c230c158e872
  kernel/operativo/pruebas/evidencia/cardinalidad-salida.txt                   51  c7fc4c208e88
  kernel/operativo/pruebas/evidencia/ciclo-salida.txt                         133  f30cff1138e8
  kernel/operativo/pruebas/evidencia/cobertura-de-gate-salida.txt              17  5513424a4610
  kernel/operativo/pruebas/evidencia/composicion-procesos-salida.txt           10  2ab67f7c7b5f
  kernel/operativo/pruebas/evidencia/contencion-salida.txt                     51  11083c1dc97d
  kernel/operativo/pruebas/evidencia/continua-salida.txt                       59  6c0de76aed0f
  kernel/operativo/pruebas/evidencia/contratos-salida.txt                      29  9d45c739504c
  kernel/operativo/pruebas/evidencia/e2e-f6-salida.txt                         92  eb035a2b1821
  kernel/operativo/pruebas/evidencia/e2e-runtime-salida.txt                    90  dd248e3a8347
  kernel/operativo/pruebas/evidencia/estado-durable-salida.txt                211  b86a60b6530d
  kernel/operativo/pruebas/evidencia/estado-e2e-salida.txt                     60  8ac0bb377756
  kernel/operativo/pruebas/evidencia/evidencia-salida.txt                       9  fbf18f87e1d8
  kernel/operativo/pruebas/evidencia/fuentes-salida.txt                        11  0ec558d48266
  kernel/operativo/pruebas/evidencia/gobierno-git-salida.txt                   89  7cba1194ffb1
  kernel/operativo/pruebas/evidencia/identidad-salida.txt                      57  c2bf7657a339
  kernel/operativo/pruebas/evidencia/integridad-evidencia-salida.txt           81  7dc1c9783462
  kernel/operativo/pruebas/evidencia/lint-salida.txt                            6  e05afa1ca8a0
  kernel/operativo/pruebas/evidencia/macrocircuitos-salida.txt                 71  b768a5c91e3f
  kernel/operativo/pruebas/evidencia/multimaquina-salida.txt                   39  bcb806526604
  kernel/operativo/pruebas/evidencia/negativos-salida.txt                     322  498ad171736b
  kernel/operativo/pruebas/evidencia/raiz-externa-salida.txt                  117  9e70beddb184
  kernel/operativo/pruebas/evidencia/recuentos-salida.txt                      13  f709244ef33d
  kernel/operativo/pruebas/evidencia/referencias-salida.txt                    77  4e002b5304ef
  kernel/operativo/pruebas/evidencia/runtime-salida.txt                       121  68a5a2829853
  kernel/operativo/pruebas/evidencia/sesion-nueva-salida.txt                   65  90575451daa1
  kernel/operativo/pruebas/evidencia/universo-obligatorio-salida.txt           34  c9c714e1cde2
  kernel/operativo/pruebas/evidencia/versiones-salida.txt                      26  4ad3d2371d41
  kernel/operativo/raiz-externa/README.md                                     190  275341e9d145
  kernel/operativo/raiz-externa/aislamiento.py                                412  feadff20ab98
  kernel/operativo/raiz-externa/anfitrion_firmante.py                         217  fc152e6122ca
  kernel/operativo/raiz-externa/anfitrion_verificador.py                      219  88ab95c5db86
  kernel/operativo/raiz-externa/atestacion.py                                 336  88920271c4f2
  kernel/operativo/raiz-externa/errores.py                                    192  d60c602c36b0
  kernel/operativo/raiz-externa/firma.py                                      295  82840e2c54b2
  kernel/operativo/raiz-externa/instalar.py                                   537  b7a3beba9d90
  kernel/operativo/raiz-externa/verificador.py                                717  d73b3d58e5af
  kernel/operativo/runtime/admision/__init__.py                               319  cd7538d3bf5c
  kernel/operativo/runtime/admision/censo.py                                  429  fded1e352061
  kernel/operativo/runtime/admision/errores.py                                154  b3b7ca6f79e3
  kernel/operativo/runtime/admision/formulas.py                               524  d14f1bb4e08e
  kernel/operativo/runtime/admision/lectura.py                                310  afe2f5547758
  kernel/operativo/runtime/admision/matriz.py                                 291  080ed2af96a2
  kernel/operativo/runtime/admision/mutacion.py                               181  1aec6f55a0e2
  kernel/operativo/runtime/admision/perimetro.py                              542  67195acc651c
  kernel/operativo/runtime/admision/sede.py                                   589  13b16bf0e992
  kernel/operativo/runtime/ads_admision.py                                    532  559f2af29699
  kernel/operativo/runtime/ads_arboles.py                                     440  5e272b4f1567
  kernel/operativo/runtime/arboles/__init__.py                                 58  5fc15c67f41a
  kernel/operativo/runtime/arboles/ataques.py                                 612  9871135db142
  kernel/operativo/runtime/arboles/derivador.py                               299  2c2a8edb0bb0
  kernel/operativo/runtime/arboles/errores.py                                  96  18a8805b182c
  kernel/operativo/runtime/arboles/suite.py                                   265  957bf8e41a03
  kernel/operativo/runtime/arboles/versiones.py                               440  c9ba73354531
  kernel/operativo/runtime/gobierno/POLITICA-CONTROL-REPO.yml                 163  bf854c079e5b
  kernel/operativo/runtime/gobierno/__init__.py                                65  2490d89513df
  kernel/operativo/runtime/gobierno/control.py                                497  0b5846289c16
  kernel/operativo/runtime/gobierno/errores.py                                118  5f7ce36fe899
  kernel/operativo/runtime/gobierno/git.py                                    332  2c2c9d405058
  kernel/operativo/runtime/gobierno/propiedad.py                              182  8315fe5703a9
  kernel/operativo/runtime/identidad/__init__.py                               63  3f630adff421
  kernel/operativo/runtime/identidad/configuracion.py                         206  048cd2837d0f
  kernel/operativo/runtime/identidad/errores.py                                96  ee295ac124dc
  kernel/operativo/runtime/identidad/proveedor.py                             178  2df2a26357f3
  kernel/operativo/runtime/identidad/rotacion.py                              202  1ab7239989f4
  kernel/operativo/runtime/pruebas/catalogo_de_prueba.py                      143  0116dcf6bede
  kernel/operativo/runtime/pruebas/escenario_e2e_runtime.py                   792  8ce3355445de
  kernel/operativo/runtime/pruebas/test_admision.py                          1625  ae303172ab76
  kernel/operativo/runtime/pruebas/test_arboles.py                            492  ebf27123d741
  kernel/operativo/runtime/pruebas/test_gobierno_git.py                       677  c7ee9c723c1a
  kernel/operativo/runtime/pruebas/test_identidad.py                          533  3d01b287f476
  kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py            1893  73fedd5d80ef
  kernel/operativo/runtime/pruebas/test_multimaquina.py                       693  b3e4e22f901e
  kernel/operativo/runtime/pruebas/test_raiz_externa.py                      1158  e6b6d23f2abf
  kernel/operativo/runtime/pruebas/test_sesion_nueva.py                       894  f67367d0da35
  kernel/operativo/validadores/ads_lint.py                                    741  5ea0502ebd53
  kernel/operativo/validadores/composicion_packs.py                           242  ba5f37f66cc4
  kernel/operativo/validadores/comprobar_arranque.py                          691  6003578b0cdc
  kernel/operativo/validadores/comprobar_composicion_procesos.py              902  0ae757fa1ec0
  kernel/operativo/validadores/comprobar_contratos.py                        1177  d7574cc6a230
  kernel/operativo/validadores/comprobar_evidencia.py                         904  4e13e0d78cd2
  kernel/operativo/validadores/comprobar_fuentes.py                           454  1028e9f37fa2
  kernel/operativo/validadores/comprobar_integridad.py                        195  01021d9e3e77
  kernel/operativo/validadores/comprobar_negativos.py                        1630  2151c112d75b
  kernel/operativo/validadores/comprobar_packs.py                             326  b9858d2a89a7
  kernel/operativo/validadores/comprobar_prompts.py                           290  d7fd857a0c75
  kernel/operativo/validadores/comprobar_recuentos.py                        1279  2abe68340e44
  kernel/operativo/validadores/comprobar_referencias.py                       357  4a8dc5344709
  kernel/operativo/validadores/comprobar_versiones.py                         542  eca300ace1f1
  kernel/operativo/validadores/entorno.py                                     228  29ad84bb7210
  kernel/operativo/validadores/exclusiones.yaml                               196  71ca67abf25d
  kernel/operativo/validadores/huella.py                                      186  1f23ebb2153c
  kernel/operativo/validadores/negativos_cardinalidad.py                      363  a216ba3d0118
  kernel/operativo/validadores/negativos_contratos19.py                       549  598d57179bc2
  kernel/operativo/validadores/negativos_integridad.py                        221  1338990b041f
  kernel/operativo/validadores/negativos_runtime.py                           696  902feaa954f0
  kernel/operativo/validadores/registrar_evidencia.py                         314  1b1fe96f34bf
  kernel/operativo/validadores/registro_pruebas.py                            550  f4f1b11dcb7b
  kernel/operativo/validadores/validadores.yaml                               429  eed4dcef0667
```

## 7 · Lote del REVISOR 3 — contratos y completitud

`F6-A`…`F6-J`, `V6-01`…`V6-19`, `g.1`…`g.16`, §19, `F6-H`, matrices, deuda, autoridad, sedes
de estado, `O27` y las tres restas.

```text
76 ficheros ÍNTEGROS · 3 rangos de `11-ARQ` · 47534 LÍNEAS EN TOTAL

RANGOS DE `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, ÍNTEGROS Y OBLIGATORIOS
  §9    L7378  -L8074       697 líneas
  §18   L10882 -L11069      188 líneas
  §19   L11070 -L11906      837 líneas

FICHEROS ÍNTEGROS · ruta · líneas · sha256 (12 primeros)
  docs/canonico/00-EMPEZAR-AQUI.md                                            162  c49efb6ff286
  docs/canonico/03-GOBIERNO-Y-AUTORIDAD.md                                    229  422f59bc9a4c
  docs/canonico/04-CONTRATOS-TECNICOS.md                                      513  901985614611
  docs/canonico/05-PLAN-DE-IMPLEMENTACION-F5-F6.md                            266  873f02bcfbc8
  docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md                           535  b9d2fa56a7c2
  docs/canonico/FUENTES-CANONICAS.yml                                         782  5bf8c624b7b9
  docs/canonico/validar-fuentes-canonicas.py                                  403  c2cd007c8ff8
  docs/evolucion/00-INDICE.md                                                 335  b62cb2659c86
  docs/evolucion/CHECKPOINT-ADS-NEXT.md                                      6385  165ab8cc02aa
  docs/evolucion/verificacion/README.md                                       396  0e766e71cd1b
  docs/evolucion/verificacion/comprobar-cobertura-de-gate.py                  531  91bb13e94a8e
  docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py         4452  5ce35410f545
  docs/evolucion/verificacion/derivar-universo-obligatorio.py                2107  377ede82af9b
  docs/evolucion/verificacion/emitir-sobre-de-ancla.py                        863  eb8bedbeb09d
  docs/evolucion/verificacion/manifiestos/F6-ASIGNACION-GATE-CERTIFICACION-FINAL-20260904.md    395  d61e83bd2b73
  docs/f5/validar-f5.py                                                       691  c8a3e7c43975
  docs/f6/00-ESTADO-DE-IMPLEMENTACION-F6.md                                   322  e2aad9a18613
  docs/f6/01-MATRIZ-DE-COMPLETITUD-F6.md                                      540  b3fcac956856
  docs/f6/02-GATE-DE-CERTIFICACION-FINAL-20260903.md                          296  aec9664573ad
  docs/f6/03-GATE-DE-CERTIFICACION-FINAL-20260904.md                         3237  2d0cff0d49b2
  docs/f6/04-MATRIZ-DE-HALLAZGOS-DEL-GATE-20260904.md                          91  ae96e53409cf
  docs/owner/ADS-OWNER-RESOLUCIONES.md                                       1054  b378b1f7ba1a
  docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md                              1651  712dbd4a935c
  docs/rediseno/a-CAPACIDADES-APROBADA.md                                    1150  235385da2471
  docs/rediseno/b-RECORRIDO-APROBADA.md                                      1331  89023236f0a2
  docs/rediseno/g-ESTADO-DURABLE-APROBADA.md                                  381  c8ba0a933c38
  kernel/.upstream-hash                                                         1  c20b5135019b
  kernel/KERNEL_CHANGELOG.md                                                  555  ec91f4e7c519
  kernel/VERSION                                                                1  c9faae8e7e82
  kernel/VERSIONES.md                                                          74  70ccaa9d4ab9
  kernel/operativo/00-INDICE.md                                               146  189dbc5f35b4
  kernel/operativo/circuitos/00-CIRCUITOS.md                                  243  16d3f2a82644
  kernel/operativo/circuitos/DIS-handoffs.md                                  249  738d7d8b3a54
  kernel/operativo/circuitos/entregas-de-8-0.md                               128  9bd69716d904
  kernel/operativo/circuitos/handoffs-generales.md                            305  b2a486ee08dc
  kernel/operativo/contratos/00-INDICE.md                                      29  48b66b4fa9da
  kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md                   161  825f15a914c1
  kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md                          539  3ee58ca4bc47
  kernel/operativo/contratos/C4-MATERIALIZACION.md                            170  670289180e59
  kernel/operativo/contratos/C5-HANDOFF.md                                    115  af6f1a4c4f5d
  kernel/operativo/entrada/03-FORMAS.md                                       561  821ad781633b
  kernel/operativo/entrada/05-ESCENARIOS.md                                   649  12703dd7fd51
  kernel/operativo/esquemas/proceso.yaml                                       89  f4f016c011a8
  kernel/operativo/pruebas/RECUENTOS-generado.md                               40  295d7fcacf46
  kernel/operativo/pruebas/REGISTRO-generado.md                               306  0e8468ab9352
  kernel/operativo/pruebas/REGISTRO.md                                        147  091735cb4bb9
  kernel/operativo/pruebas/T086-T092-contratos.md                             165  65f4648fe4f5
  kernel/operativo/pruebas/T100-T121-capacidades.md                           359  37ff430cd4e9
  kernel/operativo/pruebas/T136-T152-post-auditoria.md                        466  204174627cbd
  kernel/operativo/pruebas/T159-T170-multirepo.md                             314  a84e6a252fb2
  kernel/operativo/pruebas/T172-T181-estado-durable.md                        691  320938833e75
  kernel/operativo/pruebas/T182-T194-runtime-y-admision.md                    353  391e228c4f30
  kernel/operativo/pruebas/T195-T209-ciclo-y-macrocircuitos.md                342  a81861340cf1
  kernel/operativo/pruebas/T210-T225-arboles-raiz-externa-y-contencion.md     395  6438e8ace5f7
  kernel/operativo/pruebas/T226-T249-agentes-y-modelos.md                     367  ece884dfe884
  kernel/operativo/pruebas/T240-T248-hallazgos-externos-f6.md                 220  07af6639fd48
  kernel/operativo/pruebas/T250-T269-cardinalidad-y-seleccion.md              502  ab29bccd9bcb
  kernel/operativo/pruebas/T270-T289-contratos-19-y-composicion.md            243  f8b6878ef1ef
  kernel/operativo/pruebas/T290-T311-integridad-evidencia-y-contencion.md     739  757b2e215731
  kernel/operativo/pruebas/T340-T359-append-only-y-universo.md                379  aad6fa971ec4
  kernel/operativo/pruebas/T360-T379-sedes-veraces.md                         166  071eb9d36544
  kernel/operativo/recorrido/01-PROCESOS.md                                   606  8a8aa174fa52
  kernel/operativo/runtime/00-RUNTIME.md                                      122  a6ecc5f80696
  kernel/operativo/runtime/CONTRATO-ADAPTADOR.md                              131  ac5e12a1b37d
  kernel/operativo/runtime/CONTRATO-ADMISION.md                               177  dae17547b070
  kernel/operativo/runtime/CONTRATO-ARBOLES-ADVERSARIALES.md                  150  65a30d2610c7
  kernel/operativo/runtime/CONTRATO-CICLO-Y-MACROCIRCUITOS.md                 338  e4c337905424
  kernel/operativo/runtime/CONTRATO-CONTENCION.md                             136  f8b2fc8ebd67
  kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md                         390  6e681b4d3bcf
  kernel/operativo/runtime/CONTRATO-GOBIERNO-GIT-CONTROL.md                    99  3f820ba44848
  kernel/operativo/runtime/CONTRATO-RAIZ-EXTERNA.md                           262  bdcb49a61141
  kernel/operativo/runtime/CONTRATO-RUNTIME-Y-DISPATCHER.md                   156  141c88879e4d
  kernel/operativo/runtime/pruebas/escenario_e2e_f6.py                       1749  b70113b69151
  kernel/operativo/runtime/pruebas/test_agentes.py                           1053  1b288b178666
  tooling/new-project.sh                                                      220  5320a4f65622
  tooling/workspace.py                                                        916  020998fc34fd
```

## 8 · Los ataques mínimos, repartidos

```text
REV-1   migración 0→1 real · omisión del testigo · inversión de pasos 8/9 · C4 plural ·
        inanición de `b.12` · contención no cableada · `setsid`
REV-2   commit correcto/tree incorrecto · tree correcto/commit incorrecto · contaminación de
        CADA entrypoint · prueba con skips · manifiesto truncado
REV-3   borrado `O20`–`O27` · modificación de una resolución cerrada · apéndice legítimo
        nuevo · encogimiento del universo · estado de escenario contradictorio · obligación
        eliminada de la matriz
LOS TRES  lote de lectura incompleto · manifiesto dentro del checkout auditado
```

Para cada propiedad: **sano → VERDE · sabotaje → ROJO POR EL MOTIVO ESPERADO · restaurado →
VERDE.** Un sabotaje que sólo pone roja la huella del kernel **NO cuenta**.

## 9 · Lo que este gate NO hará, pase lo que pase

```text
NO CORREGIRÁ   ni un byte. Los hallazgos quedan REGISTRADOS y NO APLICADOS
NO ADJUDICARÁ  mientras el comprobador de cobertura no dé 0 para los TRES revisores
NO SUSTITUIRÁ  la lectura de un revisor por la del adjudicador ni por la de otro revisor
NO INICIARÁ    PesquerApp, ni siquiera si certifica: `O26` §6 lo reserva a una orden expresa
NO ABRIRÁ      ningún ciclo posterior ni ningún segundo gate
NO TOCARÁ      `redesign/kernel-2.0` ni ninguna referencia anterior
```
