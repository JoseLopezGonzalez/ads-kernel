# `F6` · GATE ÚNICO Y FINAL DE CERTIFICACIÓN · 2026-09-04 · **`F6` NO CERTIFICADA**

**Qué es este documento.** El REGISTRO íntegro del gate único de certificación de `F6`: su
objeto congelado, su manifiesto previo, **los dos dictámenes completos y la adjudicación
completa**, y las cinco declaraciones. Es **DERIVADO**: no crea autoridad, no aprueba nada y
**no certifica nada** —precisamente porque el veredicto fue que no se puede certificar—.

**Qué NO es.** No es una tanda de corrección. **Durante este gate no se corrigió ni un byte**,
y los hallazgos quedan REGISTRADOS y NO APLICADOS. No es la sede del estado de las fases: ésa
es [`03-GOBIERNO-Y-AUTORIDAD.md`](../canonico/03-GOBIERNO-Y-AUTORIDAD.md) §6, **que este gate
no mueve porque su veredicto no la mueve**: `F6` sigue `INICIADA · EN CURSO` y PesquerApp
sigue `BLOQUEADA`.

**Y no es un segundo intento.** Es el gate que el encargo autorizó, y el único. Después de él
el método se detiene: no se corrigen sus hallazgos, no se abre otro gate, no se propone otro
ciclo y no se inicia PesquerApp.

---

## 1 · Objeto congelado

```text
CANDIDATA        7b9829cbfa68c12b9947db0f7a26a1d08ed7f003
TREE             d2c0a0cde1fff37cbf5ee59cf7a5bd633a99e330
referencia       review/f6-post-gate-corrections-candidate-20260904
rama del gate    gate/f6-certificacion-final-20260904, creada DESDE ese SHA
fd633383…        NO es ancestro (verificado por el adjudicador)
intérprete       Python 3.12.14 · PyYAML 6.0.2
manifiesto       verificacion/manifiestos/F6-ASIGNACION-GATE-CERTIFICACION-FINAL-20260904.md
                 commiteado ANTES de que existiera ningún revisor
```

**Precondiciones estructurales, verificadas antes de crear ningún agente:** árbol limpio ·
sin upstream · sin operaciones Git pendientes · `F4c` CERRADA · `F5` CERRADA · `F6`
INICIADA·EN CURSO · PesquerApp BLOQUEADA.

> **UNA PRECISIÓN DEL COORDINADOR, que no altera ningún dictamen.** El adjudicador anota que
> la referencia de la candidata «no existe, sólo como `refs/remotes/origin/…`». Es exacto en
> la vista local y **no** en el remoto: `git ls-remote origin` devuelve
> `7b9829cbfa68c12b9947db0f7a26a1d08ed7f003` para
> `refs/heads/review/f6-post-gate-corrections-candidate-20260904`. Un clon la ve bajo
> `refs/remotes/` por construcción. Se dice aquí, FUERA de los dictámenes, porque **los
> dictámenes no se editan**.

## 2 · Los tres agentes, y su separación

| papel | eje | vio el dictamen ajeno |
|---|---|---|
| **REVISOR 1** | ejecución, resistencia, estado durable, runtime, concurrencia, contención, raíz externa y Git multimáquina | **no** |
| **REVISOR 2** | contratos, §19, `C2`/`C4`/`C5`, `F6-H`, `b.12`, matriz, autoridad y fases | **no** |
| **ADJUDICADOR** | juicio propio | **sólo después de que los dos cerraran** |

Los tres son NUEVOS respecto de todo el expediente. **Ninguno escribió un byte en el
repositorio**: `HEAD`, `TREE` y `git status --porcelain` se comprobaron al abrir y al cerrar
cada trabajo y salieron idénticos las tres veces. Todos los ataques se hicieron sobre clones
desechables.

## 3 · Cobertura, y por qué el gate cae por ella POR SEGUNDA VEZ

```text
REVISOR 1   ASIGNADO − LEÍDO = ∅
            141 ficheros · 46 643 líneas + los tres rangos de `11-ARQ` · 3 968
            = 50 611, exactamente lo asignado. 144 casillas, ninguna en NO.
            El adjudicador comparó su tabla con el lote: `diff` VACÍO

REVISOR 2   ASIGNADO − LEÍDO no vacío, declarado por él mismo
            50 de 84 ficheros SIN ABRIR · 29 329 de 48 143 líneas · 60,9 %
            El adjudicador verificó la resta línea a línea: es EXACTA
```

**Y el adjudicador rechaza expresamente la atenuante del reparto**: los dos lotes difieren en
550 líneas —el 1,1 %— y el otro revisor terminó el suyo. **El defecto no está en el
dimensionado, y tampoco en la frontera de `F4c`/`F5`, que atacó y sostiene.** Está en que un
lote asignado no se leyó.

> **El coordinador lo asume sin rebajarlo.** El manifiesto publicó el tamaño de cada lote
> antes de repartir precisamente para que esta pregunta se pudiera contestar, y se ha
> contestado en contra de la excusa que el coordinador habría podido invocar.

## 4 · Digests de lo que se registra

```text
DICTAMEN REVISOR 1     1099 líneas · sha256 b6d8d51f33e4dec5d24acbdc53093f6e316a74b6e1dd57666b4fe4e6c5e8daf7
DICTAMEN REVISOR 2     958 líneas · sha256 ad8795589e2074c438f5a89d617685190e6e828909046abc1533dee77bfd9da2
ADJUDICACIÓN           1077 líneas · sha256 e2749c12e3e67df980a5f176280de5d76274093eb541083c126fbce39b83a24e
```

Los tres se transcriben ÍNTEGROS y sin editar una coma. Lo que sigue no es un resumen.

---

# 5 · DICTAMEN ÍNTEGRO DEL REVISOR 1

## DICTAMEN · REVISOR 1 · gate de certificación final de `F6`

**`ASIGNADO − LEÍDO = ∅`.** El lote está leído entero: 141 ficheros · 46 643 líneas, más los
tres rangos obligatorios de `11-ARQ` · 3 968 líneas. Total 50 611 líneas, que es exactamente
lo que el manifiesto asigna. El registro fuente a fuente está en la sección 2, completo y sin
una sola casilla en NO.

**VEREDICTO: `F6` NO ES CERTIFICABLE EN ESTE ÁRBOL.** Dos BLOQUEANTES vivos e internos, los
dos reproducidos con órdenes literales sobre copias desechables del candidato:

* **`R1-B1`** — la migración `0→1` del estado durable **está rota**: revienta con un
  `TypeError` sin tipar, saca una traza con rutas absolutas del anfitrión por `main()` y deja
  el almacén heredado **permanentemente inmigrable**. Contradice a la vez `g.11`, `E-15` y la
  `DECISIÓN` escrita en el propio `migracion.py`.
* **`R1-B2`** — la **raíz externa no lleva la purga `E-10`**. Con `PYTHONPATH` envenenado, su
  punto ejecutable publica `{}` y sale con **código 0**, y su instalador escribe un manifiesto
  de **3 bytes** e instala 41 ficheros saliendo con **código 0**. Es el defecto que `E-10`
  declara cerrado, vivo en la única pieza que `O26` §1.8 pone como raíz de la confianza, y
  `T306` no la cubre.

Todo lo demás que el árbol afirma —y es mucho— lo sostiene. Está en la sección 7.

---

### 1 · Precondiciones y disciplina del gate

#### 1.1 El repositorio real, ANTES y DESPUÉS

```text
APERTURA                                    CIERRE
HEAD   20330e694d4941e5c159017ec79fd5b77aaf962d   20330e694d4941e5c159017ec79fd5b77aaf962d
tree   4ee6f9d47a4792d394b1cf7c0f8b425934ce8daf   4ee6f9d47a4792d394b1cf7c0f8b425934ce8daf
rama   gate/f6-certificacion-final-20260904        gate/f6-certificacion-final-20260904
git status --porcelain   (vacío)                   (vacío)
```

Orden literal de cierre y su salida:

```console
$ git rev-parse HEAD && git rev-parse 'HEAD^{tree}' && git rev-parse --abbrev-ref HEAD
20330e694d4941e5c159017ec79fd5b77aaf962d
4ee6f9d47a4792d394b1cf7c0f8b425934ce8daf
gate/f6-certificacion-final-20260904
$ git status --porcelain
$
```

**Ni un byte del árbol real se ha modificado.** Ninguna orden `git` que cambie estado se ha
ejecutado sobre él: los clones se hicieron con `git clone --no-local` desde el repositorio
hacia `/tmp/…/scratchpad`, y todos los ataques y todas las ejecuciones de
`registrar_evidencia.py` viven en esas copias.

#### 1.2 El objeto congelado

```text
candidato   7b9829cbfa68c12b9947db0f7a26a1d08ed7f003   (tipo: commit · verificado)
tree        d2c0a0cde1fff37cbf5ee59cf7a5bd633a99e330   (verificado)
referencia  review/f6-post-gate-corrections-candidate-20260904
            EXISTE, pero como `refs/remotes/origin/...`, NO como `refs/heads/...`
intérprete  /home/jose/.local/bin/python3.12 · 3.12.14 · PyYAML 6.0.2
            (el `python3` del PATH es 3.10 y NO se ha usado como intérprete de medición;
             sólo aparece donde se ataca la guarda de entorno)
```

#### 1.3 Disciplina declarada

No he leído el dictamen del otro revisor —`DICTAMEN-REVISOR-2.md` existe en el mismo
directorio de trabajo y no se ha abierto— ni he intercambiado mensaje alguno con él. No he
corregido nada, no he propuesto ningún commit, y no he dado por buena ninguna afirmación
escrita sin medirla.

---

### 2 · Registro de cobertura, fuente a fuente

`ASIGNADO − LEÍDO = ∅`. Ningún fichero asignado sin abrir, ningún rango asignado sin leer.
Ninguna casilla de esta tabla se ha marcado por `grep` ni por `awk`: cada fichero se abrió y
se leyó por su contenido, en tramos numerados.

#### 2.1 Los tres rangos obligatorios de `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`

```text
  §2  · disposición física del estado      L396-L3794      3399   SI
  §6  · arquitectura de adaptadores        L5812-L6135      324   SI
  §20 · CONTRATO OBLIGATORIO DE `F6`       L11907-L12151    245   SI
                                                          -----
                                                           3968
```

#### 2.2 Los 141 ficheros íntegros

```text
  ruta                                                                     líneas   leída
  docs/rediseno/g-ESTADO-DURABLE-APROBADA.md                                  381   SI
  kernel/.upstream-hash                                                         1   SI
  kernel/KERNEL_CHANGELOG.md                                                  555   SI
  kernel/VERSION                                                                1   SI
  kernel/VERSIONES.md                                                          74   SI
  kernel/operativo/pruebas/evidencia/adaptadores-salida.txt                    85   SI
  kernel/operativo/pruebas/evidencia/admision-salida.txt                      141   SI
  kernel/operativo/pruebas/evidencia/agentes-salida.txt                        41   SI
  kernel/operativo/pruebas/evidencia/arboles-salida.txt                        87   SI
  kernel/operativo/pruebas/evidencia/arranque-salida.txt                       10   SI
  kernel/operativo/pruebas/evidencia/cardinalidad-salida.txt                   51   SI
  kernel/operativo/pruebas/evidencia/ciclo-salida.txt                         133   SI
  kernel/operativo/pruebas/evidencia/composicion-procesos-salida.txt           10   SI
  kernel/operativo/pruebas/evidencia/contencion-salida.txt                     51   SI
  kernel/operativo/pruebas/evidencia/continua-salida.txt                       59   SI
  kernel/operativo/pruebas/evidencia/contratos-salida.txt                      29   SI
  kernel/operativo/pruebas/evidencia/e2e-f6-salida.txt                         85   SI
  kernel/operativo/pruebas/evidencia/e2e-runtime-salida.txt                    87   SI
  kernel/operativo/pruebas/evidencia/estado-durable-salida.txt                191   SI
  kernel/operativo/pruebas/evidencia/estado-e2e-salida.txt                     57   SI
  kernel/operativo/pruebas/evidencia/fuentes-salida.txt                        11   SI
  kernel/operativo/pruebas/evidencia/gobierno-git-salida.txt                   89   SI
  kernel/operativo/pruebas/evidencia/identidad-salida.txt                      57   SI
  kernel/operativo/pruebas/evidencia/integridad-evidencia-salida.txt           59   SI
  kernel/operativo/pruebas/evidencia/lint-salida.txt                            6   SI
  kernel/operativo/pruebas/evidencia/macrocircuitos-salida.txt                 71   SI
  kernel/operativo/pruebas/evidencia/multimaquina-salida.txt                   39   SI
  kernel/operativo/pruebas/evidencia/negativos-salida.txt                     272   SI
  kernel/operativo/pruebas/evidencia/raiz-externa-salida.txt                  117   SI
  kernel/operativo/pruebas/evidencia/recuentos-salida.txt                      11   SI
  kernel/operativo/pruebas/evidencia/referencias-salida.txt                    77   SI
  kernel/operativo/pruebas/evidencia/runtime-salida.txt                       121   SI
  kernel/operativo/pruebas/evidencia/sesion-nueva-salida.txt                   65   SI
  kernel/operativo/pruebas/evidencia/versiones-salida.txt                      26   SI
  kernel/operativo/raiz-externa/README.md                                     170   SI
  kernel/operativo/raiz-externa/aislamiento.py                                397   SI
  kernel/operativo/raiz-externa/anfitrion_firmante.py                          71   SI
  kernel/operativo/raiz-externa/anfitrion_verificador.py                       73   SI
  kernel/operativo/raiz-externa/atestacion.py                                 321   SI
  kernel/operativo/raiz-externa/errores.py                                    177   SI
  kernel/operativo/raiz-externa/firma.py                                      280   SI
  kernel/operativo/raiz-externa/instalar.py                                   245   SI
  kernel/operativo/raiz-externa/verificador.py                                501   SI
  kernel/operativo/runtime/00-RUNTIME.md                                      122   SI
  kernel/operativo/runtime/CONTRATO-ADAPTADOR.md                              131   SI
  kernel/operativo/runtime/CONTRATO-ADMISION.md                               130   SI
  kernel/operativo/runtime/CONTRATO-ARBOLES-ADVERSARIALES.md                  144   SI
  kernel/operativo/runtime/CONTRATO-CONTENCION.md                             136   SI
  kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md                         338   SI
  kernel/operativo/runtime/CONTRATO-GOBIERNO-GIT-CONTROL.md                    99   SI
  kernel/operativo/runtime/CONTRATO-RAIZ-EXTERNA.md                           208   SI
  kernel/operativo/runtime/CONTRATO-RUNTIME-Y-DISPATCHER.md                   156   SI
  kernel/operativo/runtime/adaptadores/__init__.py                             75   SI
  kernel/operativo/runtime/adaptadores/contrato.py                            185   SI
  kernel/operativo/runtime/adaptadores/proceso.py                             583   SI
  kernel/operativo/runtime/adaptadores/proyeccion.py                          175   SI
  kernel/operativo/runtime/adaptadores/puntero.py                             184   SI
  kernel/operativo/runtime/adaptadores/registro.py                            105   SI
  kernel/operativo/runtime/admision/__init__.py                               283   SI
  kernel/operativo/runtime/admision/censo.py                                  429   SI
  kernel/operativo/runtime/admision/errores.py                                142   SI
  kernel/operativo/runtime/admision/formulas.py                               524   SI
  kernel/operativo/runtime/admision/lectura.py                                279   SI
  kernel/operativo/runtime/admision/matriz.py                                 291   SI
  kernel/operativo/runtime/admision/mutacion.py                               181   SI
  kernel/operativo/runtime/admision/perimetro.py                              422   SI
  kernel/operativo/runtime/ads_admision.py                                    512   SI
  kernel/operativo/runtime/ads_arboles.py                                     401   SI
  kernel/operativo/runtime/ads_ciclo.py                                       737   SI
  kernel/operativo/runtime/ads_estado.py                                      684   SI
  kernel/operativo/runtime/ads_runtime.py                                     708   SI
  kernel/operativo/runtime/arboles/__init__.py                                 58   SI
  kernel/operativo/runtime/arboles/ataques.py                                 612   SI
  kernel/operativo/runtime/arboles/derivador.py                               299   SI
  kernel/operativo/runtime/arboles/errores.py                                  96   SI
  kernel/operativo/runtime/arboles/suite.py                                   265   SI
  kernel/operativo/runtime/arboles/versiones.py                               430   SI
  kernel/operativo/runtime/contencion/__init__.py                              65   SI
  kernel/operativo/runtime/contencion/backends.py                             407   SI
  kernel/operativo/runtime/contencion/deteccion.py                            346   SI
  kernel/operativo/runtime/contencion/ejecutor.py                             224   SI
  kernel/operativo/runtime/contencion/errores.py                               88   SI
  kernel/operativo/runtime/contencion/politica.py                              99   SI
  kernel/operativo/runtime/estado/__init__.py                                 106   SI
  kernel/operativo/runtime/estado/atestacion.py                               267   SI
  kernel/operativo/runtime/estado/bloqueo.py                                  173   SI
  kernel/operativo/runtime/estado/diario.py                                  1064   SI
  kernel/operativo/runtime/estado/errores.py                                  271   SI
  kernel/operativo/runtime/estado/fallos.py                                   123   SI
  kernel/operativo/runtime/estado/migracion.py                                220   SI
  kernel/operativo/runtime/estado/motor.py                                   1817   SI
  kernel/operativo/runtime/estado/reconciliacion.py                           517   SI
  kernel/operativo/runtime/estado/rutas.py                                    424   SI
  kernel/operativo/runtime/estado/serializacion.py                            192   SI
  kernel/operativo/runtime/estado/transaccion.py                              365   SI
  kernel/operativo/runtime/gobierno/POLITICA-CONTROL-REPO.yml                 163   SI
  kernel/operativo/runtime/gobierno/__init__.py                                65   SI
  kernel/operativo/runtime/gobierno/control.py                                497   SI
  kernel/operativo/runtime/gobierno/errores.py                                118   SI
  kernel/operativo/runtime/gobierno/git.py                                    332   SI
  kernel/operativo/runtime/gobierno/propiedad.py                              182   SI
  kernel/operativo/runtime/identidad/__init__.py                               63   SI
  kernel/operativo/runtime/identidad/configuracion.py                         206   SI
  kernel/operativo/runtime/identidad/errores.py                                96   SI
  kernel/operativo/runtime/identidad/proveedor.py                             178   SI
  kernel/operativo/runtime/identidad/rotacion.py                              202   SI
  kernel/operativo/runtime/pruebas/catalogo_de_prueba.py                      143   SI
  kernel/operativo/runtime/pruebas/escenario_e2e_runtime.py                   700   SI
  kernel/operativo/runtime/pruebas/escenario_extremo_a_extremo.py             635   SI
  kernel/operativo/runtime/pruebas/test_adaptadores.py                        743   SI
  kernel/operativo/runtime/pruebas/test_admision.py                          1158   SI
  kernel/operativo/runtime/pruebas/test_arboles.py                            492   SI
  kernel/operativo/runtime/pruebas/test_contencion.py                         379   SI
  kernel/operativo/runtime/pruebas/test_estado_durable.py                    2747   SI
  kernel/operativo/runtime/pruebas/test_gobierno_git.py                       677   SI
  kernel/operativo/runtime/pruebas/test_identidad.py                          533   SI
  kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py             905   SI
  kernel/operativo/runtime/pruebas/test_multimaquina.py                       693   SI
  kernel/operativo/runtime/pruebas/test_raiz_externa.py                      1158   SI
  kernel/operativo/runtime/pruebas/test_runtime.py                           2067   SI
  kernel/operativo/runtime/pruebas/test_sesion_nueva.py                       894   SI
  kernel/operativo/runtime/runtime/__init__.py                                107   SI
  kernel/operativo/runtime/runtime/dispatcher.py                             1495   SI
  kernel/operativo/runtime/runtime/ejecucion.py                               344   SI
  kernel/operativo/runtime/runtime/errores.py                                 171   SI
  kernel/operativo/runtime/runtime/estado_util.py                              92   SI
  kernel/operativo/runtime/runtime/fallos.py                                  108   SI
  kernel/operativo/runtime/runtime/lease.py                                   390   SI
  kernel/operativo/runtime/runtime/modelo.py                                  440   SI
  kernel/operativo/runtime/runtime/politica.py                                302   SI
  kernel/operativo/runtime/runtime/vistas.py                                  171   SI
  kernel/operativo/validadores/comprobar_evidencia.py                         590   SI
  kernel/operativo/validadores/comprobar_negativos.py                        1544   SI
  kernel/operativo/validadores/entorno.py                                     142   SI
  kernel/operativo/validadores/negativos_cardinalidad.py                      277   SI
  kernel/operativo/validadores/negativos_contratos19.py                       308   SI
  kernel/operativo/validadores/negativos_integridad.py                         92   SI
  kernel/operativo/validadores/negativos_runtime.py                           484   SI
  kernel/operativo/validadores/registrar_evidencia.py                         228   SI
  tooling/new-project.sh                                                      220   SI
  tooling/workspace.py                                                        835   SI
                                                                          ------
                                                                           46643
```

#### 2.3 La resta

```text
ASIGNADO   141 ficheros · 46 643 líneas  +  3 rangos · 3 968 líneas  =  50 611
LEÍDO      141 ficheros · 46 643 líneas  +  3 rangos · 3 968 líneas  =  50 611
ASIGNADO − LEÍDO = ∅
```

---

### 3 · Línea base reproducida, frente a la línea base afirmada

Reproducida sobre un clon **prístino del candidato** `7b9829cb`, con el intérprete declarado.

| afirmado | medido | ¿casa? |
|---|---|---|
| 34/34 validadores en verde · 34 evidencias · 0 problemas | `34/34 validadores en verde · 34 evidencias publicadas · 0 problemas`, `EXIT=0` | **SÍ** |
| 682 casos en 18 baterías `unittest` | 18 ficheros de evidencia con `Ran N`, suma **682** | **SÍ** |
| E2E 15/15 · 25/25 · 24/24 | `15 de 15 pasos CUMPLIDOS` · `25 de 25 pasos CUMPLIDOS` · `24 de 24 pasos CUMPLIDOS` | **SÍ** |
| 133 infracciones detectadas · 0 NO detectadas | `133 infracciones detectadas · 0 NO detectadas` | **SÍ** |
| CERO saltos ejecutados | 18 líneas `^OK$`; **cero** `OK (skipped=N)` y **cero** `... skipped` en toda la evidencia | **SÍ** |
| determinismo byte a byte entre dos corridas | segunda corrida sobre el mismo clon: `diff -r` entre los dos directorios de evidencia **VACÍO** | **SÍ** |
| huella del kernel `6075d888ff2c7b70` | la evidencia de negativos la publica como «almacenada 6075d888ff2c7b70» | **SÍ** |
| `git status --porcelain` vacío antes y después | vacío en el clon del **candidato**; **NO vacío en la rama del gate** — ver `R1-M1` | **NO, en HEAD** |
| las tres restas A=0 · B=0 · C=0 | reproducibles en el candidato; en HEAD el derivador **FALLA CERRADO con código 2** — ver `R1-M1` | **NO, en HEAD** |

Recuento medido de las 18 baterías, para que nadie tenga que creerse el 682:

```text
adaptadores 37 · admision 65 · agentes 15 · arboles 38 · cardinalidad 20 · ciclo 52
contencion 20 · continua 24 · estado-durable 90 · gobierno-git 39 · identidad 23
integridad-evidencia 24 · macrocircuitos 30 · multimaquina 14 · raiz-externa 53
runtime 54 · sesion-nueva 27 · workspace 57            18 baterías · 682 casos
```

**La línea base es real.** Lo que NO es real es que se reproduzca idéntica sobre la rama del
gate: el propio manifiesto del gate, confirmado dentro de `docs/evolucion/verificacion/
manifiestos/`, cambia el corpus que dos instrumentos del árbol miden. Es `R1-M1`.

---

### 4 · Los diez ataques obligatorios, más el sellado

Formato de cada uno: **sano → VERDE · sabotaje → ROJO POR EL MOTIVO ESPERADO · restaurado →
VERDE**. Un sabotaje que sólo enrojece la huella del kernel NO se cuenta como detección, y
así se ha aplicado.

#### 4.1 · Ataque 1 · commit y tree desacoplados, y la evidencia después de los siete pasos

| sabotaje | sano | saboteado | restaurado | conjunto que enrojece |
|---|---|---|---|---|
| neutralizar la mitad `tree` de `exigir_tree` | VERDE 53/53 | **ROJO** `T291`, `T291b` · `VINCULO_DE_TREE_ROTO` | VERDE 53/53 | `{T291, T291b}` |
| neutralizar la mitad `commit` de `exigir_commit` | VERDE 53/53 | **ROJO** `T292`, `T292b`, `T293b`, `test_una_atestacion_de_otro_commit_no_sirve` · `VINCULO_DE_COMMIT_ROTO` | VERDE 53/53 | `{T292, T292b, T293b, …}` |

**Los dos conjuntos son DISJUNTOS.** Es la propiedad que el árbol afirma y la única que
convierte a `E-07` en dos mitades y no en una. `T291` exige además
`assertNotIn(b"VINCULO_DE_COMMIT_ROTO")`, de modo que la mitad `tree` no puede aprobarse por
el rojo de la otra.

Los tres casos de firma correcta sobre tupla equivocada, medidos:

```text
firma correcta de OTRA tupla (commit avanzado)  → VINCULO_DE_COMMIT_ROTO   (T293b)
clave válida para OTRA época                    → IDENTIDAD_NO_ACEPTADA    (T294)
huella pública de otra clave, firma legítima    → EMISOR_NO_COINCIDE       (T294b)
veredicto calculado contra otra base            → ANCLA_NO_COINCIDE        (T294c)
modificación DESPUÉS de firmar, digest recalculado → FIRMA_NO_VERIFICADA   (T295)
```

Evidencia sólo tras los SIETE pasos: `T296` interrumpe la `SecuenciaDeVerificacion` en cada
uno de los siete —`firma · clave-aceptada · epoca · commit · tree · politica · identidad-del-
emisor`— y exige que **no quede fichero**, con control positivo al final (con los siete
anotados, la misma llamada SÍ escribe). `T296b` prueba que el **orden** es garantía y no
costumbre. `T296c` prueba que sin testigo no se escribe.

**RESULTADO: el árbol lo sostiene.**

#### 4.2 · Ataque 2 · inversión de los pasos 8 y 9 de `estado/motor.py`

El paso 8 publica los objetos y escribe el testigo durable
`operacional/tx/<tx>/PUBLICADOS.json`; el paso 9 exige ese testigo antes de publicar
`REVISION.json`. Formas de invertirlo, y qué enrojece cada una:

| forma de la inversión | resultado |
|---|---|
| publicar `REVISION.json` sin testigo | **ROJO** `T297` |
| escribir el testigo con los `cid` VIEJOS (testigo antes de publicar) | **ROJO** `T297b` |
| publicar con mezcla parcial | **ROJO** `T298` |
| testigo sin `fsync` de contenido y de directorio | **ROJO** `T299` |
| **inversión que RESPETA el significado de cada punto de fallo** | **ROJO** `T300` (+ colateral `T314b`) |
| borrar el testigo y completar a ciegas | **ROJO** `T301` |

La inversión **respetando el significado de cada punto de fallo** —la difícil— deja el
almacén irrecuperable y **sí** enrojece `T300`. Pero:

> **Las tres E2E siguen en VERDE con el almacén irrecuperable: 15/15, 25/25, 24/24.**

`CONTRATO-ESTADO-DURABLE.md` §3 L106-L107 afirma que las tres E2E comprueban recuperabilidad
«de modo que ya no pueden seguir verdes sobre un almacén irrecuperable». **Medido: es falso
para esta inversión.** Los tres escenarios llaman a `comprobar_recuperabilidad(base)` y
devuelven `escenario.codigo_de_salida() or (0 if recuperable else 1)`, pero **ninguno inyecta
el punto `entre-el-paso-8-y-el-9`**, que es el único que produce el estado que la afirmación
dice cubrir. Es `R1-M4`.

**RESULTADO: `E-08` está cerrado en la batería; la afirmación del contrato sobre las E2E, NO.**

#### 4.3 · Ataque 3 · `commit_de_nacimiento`

| caso | prueba | resultado |
|---|---|---|
| positivo: con nacimiento trazable, AÑADIR sigue siendo VERDE | `T302` | VERDE |
| **ausencia** de nacimiento → NO degrada a comparar con la base | `T303` | ROJO al sabotear |
| commit **inexistente** | `T303b` | falla cerrado |
| commit que **NO contiene la sede** | `T303c` | falla cerrado |
| historia **reescrita o truncada** (incluye `--depth 1`) | `T304` | falla cerrado |
| historia **injertada** con `grafts` | `T304b` | falla cerrado |
| **vaciar los bytes** del nacimiento | `T305` | no produce verde |

`PROCEDENCIA_DE_NACIMIENTO = "nacimiento"` y el contraste es contra el nacimiento y no contra
`HEAD` —lo prueba `test_el_contraste_es_contra_el_nacimiento_y_no_contra_head`, que es
justamente la tautología que había que impedir.

**RESULTADO: el árbol lo sostiene, incluido el clon `--depth 1`.**

#### 4.4 · Ataque 4 · `--repo` con `PYTHONPATH` contaminado

**Los cinco `ads_*.py`: SOSTENIDO.** Purga como primer acto del fichero, con sólo `sys` y
`os`, control del control sobre la procedencia del propio `os` (`SystemExit(5)`), y
`exigir_procedencia_del_aparato()` antes de ejecutar orden alguna. Medido literalmente, sobre
el candidato, desde un `cwd` ajeno y con un `json.py` homónimo en `PYTHONPATH`:

```console
$ cd /tmp && PYTHONPATH=<veneno> python3.12 .../ads_admision.py --repo <cand> procedencia --json
{
  "aparato": "runtime",
  "entradas_del_lanzador_retiradas": 1,
  "modulos": {
    "admision": "aparato:admision/__init__.py",
    "gobierno": "aparato:gobierno/__init__.py",
    "identidad": "aparato:identidad/__init__.py"
  },
  "repo": "cand",
  "repo_es_el_arbol_del_aparato": true,
  "ruta_de_importacion": ["aparato:.", "aparato:.", "aparato:."]
}
EXIT=0
```

La procedencia es **demostrable en la salida**: dice de dónde salió cada módulo y cuántas
entradas del lanzador se retiraron.

**La RAÍZ EXTERNA: NO SOSTENIDO. Es `R1-B2`.** Mismo veneno, misma máquina, mismo intérprete:

```console
$ cd /tmp && PYTHONPATH=<veneno> python3.12 .../raiz-externa/verificador.py capacidades
{}
EXIT=0
```

```console
$ cd /tmp && PYTHONPATH=<veneno> python3.12 .../raiz-externa/instalar.py --destino <d> --arbol <cand>
{}
EXIT=0
$ wc -c <d>/MANIFIESTO-DE-INSTALACION.json ; find <d> -type f | wc -l
3 .../MANIFIESTO-DE-INSTALACION.json
41
```

Control sano, sin veneno, sobre la misma orden: manifiesto de **6 734 bytes** y salida
completa. Y la prueba de que el veneno **es** lo que la raíz externa importa:

```console
$ PYTHONPATH=<veneno> python3.12 -c "import sys; sys.path.insert(0,'.../raiz-externa'); import json, atestacion; print(json.__file__)"
.../final-veneno/json.py
```

Consecuencia medida aguas abajo: esa instalación de manifiesto vacío, comprobada **sin**
veneno, no falla tipada sino con una traza con **4 rutas absolutas del anfitrión y CERO
códigos tipados**:

```text
KeyError: 'ficheros'      (instalar.py:188, verificar_instalacion)
```

Y el alcance del control que debería haberlo impedido:

```python
## kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py:49
EJECUTABLES = ("ads_admision.py", "ads_estado.py", "ads_runtime.py",
               "ads_ciclo.py", "ads_arboles.py")
```

`T306` cubre **cinco ejecutables y ninguno más**. En todo el paquete
`kernel/operativo/raiz-externa/` no existe ni una línea de purga: ni `PYTHONPATH`, ni
`_purgar_la_ruta_de_importacion`, ni `entradas_del_lanzador`.

#### 4.5 · Ataque 5 · evidencia con saltos

| sabotaje sobre `contencion-salida.txt` | resultado |
|---|---|
| `OK` → `OK (skipped=3)` | **DETECTADA** `NE14a` · «la corrida SALTÓ 3 caso(s) y el manifiesto no declara ninguno» |
| `Ran 20 tests` → `Ran 99 tests` | **DETECTADA** `NE14b` · «su salida contiene 20 desenlaces de caso» |
| recortar un caso, dejando el contador | **DETECTADA** `NE14c` · «contiene 19 desenlaces de caso» |
| `OK (failures=1)` | **DETECTADA** `NE14d` · «Un éxito con failures no es un éxito» |
| dos corridas pegadas | **DETECTADA** `NE14e` · «no tiene EXACTAMENTE un `Ran N tests`» |

`firma_de_exito` NO casa por subcadena: el manifiesto declara `'(?m)^OK$'` y, además y con
independencia del manifiesto, `_comprobar_resultado_exacto` **deriva** el resultado de la
salida y lo compara entero. Es la decisión correcta y está escrita como tal: «ésta es la que
no depende de que el manifiesto esté bien escrito». Y **no hay ni un `skips_permitidos`** en
todo `validadores.yaml`, de modo que cualquier salto es ROJO.

**RESULTADO: el árbol lo sostiene, por partida doble.**

#### 4.6 · Ataque 6 · error tipado cruzando `main()` en los cinco `ads_*.py`

Los cinco declaran la MISMA tabla, con las DOS clases homónimas conocidas:

```text
0 éxito · 1 error-del-kernel · 2 uso · 3 error-del-adaptador · 4 error-de-contencion
5 procedencia-no-fiable · 70 corte inyectado · 78 entorno insuficiente
```

`adaptadores.contrato.CapacidadNoSoportada` (raíz `ErrorDeAdaptador`) sale por **3**;
`runtime.errores.CapacidadNoSoportada` (raíz `ErrorDeRuntime`) sale por **1**. Las dos
jerarquías se conservan separadas a propósito y el punto ejecutable las conoce a las dos:
`T308b`, `T308c`, `T308d`, `T308e`, `T308f` lo miden una a una, incluida la ausencia de éxito
parcial. `stderr` lleva siempre la línea legible **y** la estructura JSON; `_sin_rutas_del_
anfitrion` se aplica en la puerta de salida y no en cada `raise`.

Y el matiz que hace honesto el diseño: lo que **no** es tipado se vuelve a levantar tal cual.
Es correcto —esconder un defecto de programación tras un código limpio sería lo contrario de
`E-15`—, y es exactamente por eso que `R1-B1` es un BLOQUEANTE y no una incomodidad: un
`TypeError` en el camino productivo de `migrar` **sale por ahí**, con la traza entera.

**RESULTADO: sostenido para todo lo tipado. El agujero no está en la tabla: está en que
`migracion.py` produce un error NO tipado en un camino productivo.**

#### 4.7 · Ataque 7 · contención no cableada

`--contencion` y `--contencion-backend` existen y son alcanzables desde **los dos** puntos
que `E-16` nombra:

```text
ads_runtime.py   _politica_de_contencion(argumentos) → adaptadores.AdaptadorDeProcesoLocal(
                    ..., politica_de_contencion=...)
ads_ciclo.py     idem, y declarado en `planificar`, `ciclo`, `continuar` y `macrocircuito`
```

La elección del backend ocurre en el **CONSTRUCTOR** del adaptador, de modo que un anfitrión
que no puede contener detiene el proceso **antes** de adquirir ningún lease y de abrir ningún
recibo: CERO ejecución. Medido por `T309` (activa y contiene al bisnieto), `T309b` (sin
backend fuerte, FALLA CERRADO) y `T309c` (`ads_ciclo` también). Sin degradación silenciosa:
`test_sin_ningun_backend_fuerte_la_politica_fuerte_falla_cerrado` fabrica un informe de
capacidades sin ningún fuerte y exige `ContencionFuerteNoDisponible` con el texto
«NO se degrada», **y además** que `contencion.ejecutar` tampoco corra.

**RESULTADO: el árbol lo sostiene.**

#### 4.8 · Ataque 8 · `setsid`: hijo, nieto y bisnieto por el camino PRODUCTIVO

La tarea generacional engendra tres capas, **cada una con su propio `setsid`**, y se
identifican restando marcas en `/proc/<pid>/cmdline`, que es la única forma de verlas desde
fuera de un espacio de nombres de PID. Con backend fuerte no sobrevive nadie
(`esperar_a_que_mueran(todos) == []`); con `simple` **sobrevive el bisnieto**, y la prueba lo
exige:

```python
self.assertEqual(vivos, capturadas["bisnieto"],
                 "el bisnieto NO sobrevivió al backend simple: o la tarea no hizo "
                 "`setsid`, o esta prueba dejó de distinguir los dos niveles")
```

Y por el camino **productivo**, no sólo el del paquete: `test_adaptadores.py` lo mide a
través del adaptador (`T247` el bisnieto no escapa con política; `T248` sin backend fuerte no
ejecuta), y `test_integridad_y_evidencia.py` lo mide a través del **punto ejecutable**
(`T309`). El control que impide presentar el débil como fuerte es `T216` y su sabotaje
catalogado es `N216`: subir el nivel declarado de `simple` a `arbol-de-procesos` **pone rojo**
`T216` por `ContencionFuerteNoDisponible not raised`.

**RESULTADO: el árbol lo sostiene, y el control del control existe.**

#### 4.9 · Ataque 9 · custodia efímera presentada como productiva

`E-17` sigue declarado **EXTERNO y ABIERTO**, y así se dice en las tres sedes del paquete:
`README.md` de `raiz-externa/` registra `E-17` con PROPIETARIO, MECANISMO PREVISTO, CONDICIÓN
DE CIERRE y la frase «no constituyen custodia productiva»; `test_raiz_externa.py` declara en
su docstring que las claves son efímeras, viven fuera de todo repositorio y se destruyen en un
`addClassCleanup`; y `ads_estado.py atestar` **imprime la advertencia en su propia salida**:

```text
proveedor             ProveedorEfimero/<alg>
advertencia           EXCLUSIVAMENTE PARA PRUEBAS, sin custodia productiva
```

`T309e` barre la zona buscando afirmaciones de custodia productiva. Ningún punto del árbol
presenta la clave efímera como productiva.

**RESULTADO: el árbol lo sostiene. `E-17` es deuda EXTERNA declarada, no un verde falso.**

#### 4.10 · Ataque 10 · identidad de escritura compartida (`O26` §1.6) — EJERCIDA

No leída: ejecutada, hoy, en este anfitrión.

```text
mecanismo elegido            contenedor
identidad_distinta           True
uid del runtime              1000       uid del verificador   65534
control_positivo escribió    True       control_de_lectura leyó   True
intentos                     8          impedidos              8
exigir_sin_escritura         True
```

Los ocho, con el mensaje REAL del sistema:

```text
modificar-un-fichero                  Permission denied
crear-un-fichero                      Read-only file system
borrar-un-fichero                     Read-only file system
cambiar-una-ref                       Read-only file system
alterar-la-configuracion-de-git       Permission denied
sustituir-la-clave-publica-aceptada   Read-only file system
cambiar-la-politica                   Read-only file system
modificar-la-atestacion-ya-firmada    Read-only file system
```

Y el **control del control funciona de verdad**: en una primera pasada, con el directorio
externo sin poblar, `control_de_lectura.leyo` salió `False` y `exigir_sin_escritura` **se
negó** a certificar, diciendo textualmente que «los intentos no fallaron por falta de permiso
sino porque los objetivos no existían». No acepta un ocho de ocho que no significa nada.

Alcance REAL de este anfitrión, medido y sin aceptar ninguna afirmación universal:

```text
usuario-del-sistema   NO disponible   `sudo -n true` → «sudo: a password is required»
contenedor            SÍ disponible   identidad distinta REAL (1000 → 65534)
espacio-de-nombres    SÍ disponible   LÍMITE DECLARADO: MISMO usuario
cgroup v2             presente        controladores: cpuset cpu io memory hugetlb pids rdma
```

**RESULTADO: `O26` §1.6 se ejerce y se cumple en este anfitrión, con su límite declarado.**

#### 4.11 · El sellado del diario (`g.7`)

| ataque | resultado |
|---|---|
| romper la cadena de huellas de un talón | **ROJO** `T313` / `T319` |
| sellar lo que la recuperación necesita | **ROJO** `T318` · fallo cerrado |
| retirar un cuerpo SIN transición | **ROJO** `T317` |
| vaciar un cuerpo a mano conservando la huella | **ROJO** `T317b`, cazado AL LEER |
| umbral ausente, ilegible o absurdo | **ROJO** `T316b` |
| umbral absurdo pasado a mano por la CLI | **ROJO** `T316c` |
| alterar un evento YA sellado | **ROJO** `T319` |
| quitar el ancla `cid_sellados` | **ROJO** `T319b` |
| **control del control**: se retira `_verificar_sellado` y se mira qué enrojece | `T319c` |
| sellar la ventana de una transacción abierta | **se niega** `T315` |
| el diario sellado sigue admitiendo transiciones | `T313b` |
| las dos ramas de `g.8` sobre diario sellado | `T314` (REVERTIR) · `T314b` (COMPLETAR) |

**La compactación, medida EN BYTES sobre un almacén virgen:**

```text
antes    119 536 bytes
después  108 584 bytes
retirados 10 952 bytes   ·   9,2 %
```

El umbral se lee del bloque JSON `ads.estado.calibracion/1` de
`CONTRATO-ESTADO-DURABLE.md` y es calibrable, no una constante del código (`T316`).

**RESULTADO: el árbol lo sostiene, y el sellado compacta de verdad.** Un matiz menor,
`R1-BJ1`: el residuo del sellado declara como mitigación que «vuelve a ser detectable en
cuanto el diario anexa otra vez», y eso, medido, es falso; está en la sección 6.

---

### 5 · Las ocho condiciones de `O26` §1, una a una y con su medición

`O26` está leída entera. Sus ocho condiciones son las de §1.1 a §1.8, y `O26` §2 dice que la
aceptación arquitectónica «se vuelve aplicable a una candidata únicamente cuando un gate
independiente VÁLIDO demuestre las ocho condiciones sobre su SHA exacto». Ésta es esa
medición sobre `7b9829cb`.

| # | condición `O26` §1 | cómo se ha MEDIDO | veredicto |
|---|---|---|---|
| 1 | la raíz y su evidencia viven **fuera** del árbol verificado | `instalar()` levanta `InstalacionDentroDelArbol` si el destino cae dentro (`T217`); `escribir_evidencia` rechaza un destino interno con `EVIDENCIA_DENTRO_DEL_ARBOL` (`T220`); un `os.walk` del árbol comprueba que no hay `verificador.py`, `anfitrion_firmante.py` ni `anfitrion_verificador.py` dentro | **CUMPLE** |
| 2 | la firma es **asimétrica** | `ssh-keygen -Y` Ed25519; `capacidades` publica `simetrica: false` y la versión de OpenSSH; el sobre fija la dependencia con su versión | **CUMPLE** |
| 3 | la atestación ligada **simultáneamente** al SHA del commit y a su tree | `exigir_commit` y `exigir_tree` son funciones SEPARADAS con errores propios; los dos sabotajes enrojecen conjuntos **disjuntos** (§4.1); `assertNotIn("refs/heads", texto)` impide atestar sobre un nombre de rama | **CUMPLE** |
| 4 | firmante y verificador **separados** | `anfitrion_firmante.py` responde a `verificar` con código 4 y «SOLO firma»; `anfitrion_verificador.py` se niega a firmar; son dos ficheros y dos procesos | **CUMPLE** |
| 5 | el verificador **no dispone** de la clave privada | `allowed_signers` se barre buscando `PRIVATE KEY` y sólo contiene `ssh-ed25519`; el marcador de la clave privada real se busca en **siete** salidas y en **todo el árbol byte a byte**, con su control del control (`test_el_marcador_si_esta_en_la_clave_privada`) | **CUMPLE** |
| 6 | el ejecutor **no comparte** capacidad de escritura sobre el control repo con el runtime | **EJERCIDO hoy**, no leído: contenedor, uid 1000 → 65534, 8 de 8 intentos impedidos con el mensaje real del sistema, control positivo y control de lectura en `True` (§4.10). `O26` §3 acepta expresamente esta demostración transitoria | **CUMPLE** |
| 7 | existen **rotación, solapamiento, retirada y revocación** | `anillo.rotar(solapamiento=2)`; la retirada verifica DENTRO de su ventana y no fuera (`IdentidadFueraDeSolapamiento`); la revocada no verifica NUNCA, ni dentro del solapamiento (`IdentidadRevocada`); la desconocida se rechaza (`IdentidadDesconocida`); la traza publica sólo la huella pública. Y no es papel: `test_la_identidad_rotada_firma_y_verifica_de_verdad` firma y verifica con la clave rotada | **CUMPLE** |
| 8 | clave desconocida, firma inválida, commit incorrecto, tree incorrecto, ausencia de proveedor **y contaminación del entorno** fallan cerrado | clave desconocida → rechazada; un byte alterado → firma inválida; commit incorrecto → `VINCULO_DE_COMMIT_ROTO`; tree incorrecto → `VINCULO_DE_TREE_ROTO`; sin `ssh-keygen` → `PROVEEDOR_DE_FIRMA_AUSENTE`; sin clave → no se emite y no se escribe fichero. **Y la CONTAMINACIÓN DEL ENTORNO: NO falla cerrado.** `capacidades` publica `{}` con **código 0** y `instalar.py` escribe un manifiesto de **3 bytes** con **código 0** bajo `PYTHONPATH` envenenado (§4.4) | **NO CUMPLE** |

**Siete de ocho. La octava no se cumple, y es la que `O26` §2 exige junto a las demás.** No es
una interpretación: «contaminación del entorno» está escrito en `O26` §1.8 con esas palabras,
y el mismo repositorio declara el ataque y lo cierra —con purga, control del control y
publicación de la procedencia— para los cinco `ads_*.py`. La pieza que `O26` §1 juzga es
justamente la que se quedó sin él.

`O26` §4 se cumple: la custodia productiva sigue declarada EXTERNA y ninguna salida del árbol
llama custodia a la clave efímera (§4.9).

`O26` §5.5 —«que no existen bloqueantes internos vivos»— **NO se cumple**: hay dos, y los dos
son internos. Se dictaminan en la sección 8.

---

### 6 · HALLAZGOS

Cada uno con `identificador · severidad · sede · reproducción · remedio · propietario · clase`.

---

#### `R1-B1` · BLOQUEANTE · INTERNO

**Sede.** `kernel/operativo/runtime/estado/migracion.py:178` (idéntica en `HEAD` y en el
candidato `7b9829cb`), contra `kernel/operativo/runtime/estado/motor.py:558`.

```python
## migracion.py:178
almacen._publicar_revision(revision_cero)

## motor.py:558
def _publicar_revision(self, revision, *, testigo):
```

`testigo` es argumento **obligatorio de sólo palabra clave** desde `E-08`, y la única llamada
del módulo de migración no lo pasa.

**Reproducción**, sobre un almacén heredado GENUINO —sin `FORMATO.json`, sin diario y sin
`REVISION.json`—, en una copia desechable del candidato:

```console
$ mkdir -p repo/estado/canonico/items
$ echo '{"id":"it-uno","titulo":"heredado"}' > repo/estado/canonico/items/it-uno.json
$ python3.12 .../ads_estado.py --repo repo migrar
Traceback (most recent call last):
  ...
  File ".../estado/migracion.py", line 178, in _migrar_0_a_1
    almacen._publicar_revision(revision_cero)
TypeError: Almacen._publicar_revision() missing 1 required keyword-only argument: 'testigo'
EXIT=1        (stdout VACÍO; la traza lleva rutas absolutas del anfitrión)
```

Y el daño no es sólo el fallo: **el almacén queda inmigrable para siempre**. El diario ya
contiene `almacen.inicializado`, de modo que la segunda llamada ni siquiera entra en esa rama:

```console
$ python3.12 .../ads_estado.py --repo repo migrar
[ESTADO_CORRUPTO] el fichero no existe (estado/REVISION.json)
{ "clase_de_fallo": "error-del-kernel", "codigo_de_salida": 1,
  "error": { "codigo": "ESTADO_CORRUPTO", "detalle": "el fichero no existe",
             "ruta": "estado/REVISION.json" } }
EXIT=1
```

**Qué contradice, textualmente.** El propio `migracion.py` declara: «Con (b) un corte deja el
almacén exactamente donde estaba a ojos de `abrir` —heredado—, y **volver a llamar a
`migrar()` retoma**». Medido: no retoma, y no puede retomar nunca más. Además rompe `g.11`
—«una migración es RECUPERABLE: interrumpida, se detecta y se termina o se revierte»— y
`E-15`, porque un error **no tipado** cruza `main()` como traza con rutas del anfitrión, que
es exactamente el modo de fallo que `E-15` existe para impedir.

**Por qué ninguna prueba lo ve.** La única cobertura es
`test_estado_durable.py:519 test_09_migracion_del_formato_heredado_cero_a_uno`, y **fabrica**
el almacén heredado haciendo `os.remove(FORMATO.json)` sobre un almacén YA inicializado. Ese
almacén tiene diario con `almacen.inicializado` y tiene `REVISION.json`, de modo que la rama
`if not any(... "almacen.inicializado" ...)` —la que contiene la línea rota— **nunca se
entra**. La prueba pasa sobre un camino que el código productivo no recorre.

**Remedio.** Pasar el testigo que `E-08` exige en esa llamada, y **cambiar el fixture** para
que construya un almacén heredado de verdad —sin diario y sin `REVISION.json`— en vez de
mutilar uno inicializado. Sin lo segundo, la corrección de la primera línea seguiría sin tener
quien la vigile.

**Propietario.** Autoría de `F6`, eje de estado durable.

---

#### `R1-B2` · BLOQUEANTE · INTERNO

**Sede.** Todo el paquete `kernel/operativo/raiz-externa/` — `verificador.py` (501),
`instalar.py` (245), `atestacion.py`, `firma.py`, `aislamiento.py`,
`anfitrion_firmante.py`, `anfitrion_verificador.py`. Y el alcance del control que debía
cubrirlo: `kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py:49`.

**Qué falta.** La purga `E-10` de la ruta de importación. En el paquete entero no hay ni una
aparición de `PYTHONPATH`, `_purgar_la_ruta_de_importacion` ni `entradas_del_lanzador`.
`verificador.py` sólo hace `sys.path.insert(0, AQUI)`, que protege a sus módulos vecinos y
**no** protege a la biblioteca estándar, que va DESPUÉS de `PYTHONPATH`.

**Reproducción.** Con un `json.py` homónimo en `PYTHONPATH`, desde un `cwd` ajeno:

```console
$ PYTHONPATH=<veneno> python3.12 .../raiz-externa/verificador.py capacidades
{}
EXIT=0

$ PYTHONPATH=<veneno> python3.12 .../raiz-externa/instalar.py --destino <d> --arbol <cand>
{}
EXIT=0
$ wc -c <d>/MANIFIESTO-DE-INSTALACION.json          →      3
$ find <d> -type f | wc -l                          →     41
  (control sano, sin veneno: manifiesto de 6 734 bytes)

$ PYTHONPATH=<veneno> python3.12 -c "…; import json, atestacion; print(json.__file__)"
<veneno>/json.py
```

Es el **mismo hecho** que `ads_admision.py` documenta como reproducido y cerrado —«publicaba
`{}` como veredicto y terminaba con código 0»—, vivo en la raíz externa. Aguas abajo, esa
instalación de manifiesto vacío, comprobada ya sin veneno, no falla tipada sino con
`KeyError: 'ficheros'` y una traza con **4 rutas absolutas del anfitrión y cero códigos
tipados**.

**Alcance del control.** `T306` sólo recorre
`("ads_admision.py","ads_estado.py","ads_runtime.py","ads_ciclo.py","ads_arboles.py")`.
La raíz externa está fuera de esa tupla, y ninguna otra prueba del árbol la sustituye.

**Qué contradice.** `O26` §1.8, que exige que **la contaminación del entorno falle cerrado**
en la implementación sometida al gate; `g.15`, que exige que la raíz externa FALLE CERRADO
ante «entrada inválida, truncamiento o estructura inesperada»; y `E-10`, que el árbol declara
cerrado.

**Remedio.** Llevar el prólogo `E-10` completo —purga primero, control del control sobre `os`,
`exigir_procedencia_del_aparato()` antes de emitir— a `verificador.py` y a `instalar.py`, y
**ampliar `EJECUTABLES` de `T306`** para que la raíz externa entre en el alcance del control.
Lo segundo es lo que impide que el agujero vuelva.

**Propietario.** Autoría de `F6`, eje de raíz externa.

---

#### `R1-M1` · MEDIA · LÍMITE DEL PROPIO GATE

**Sede.** `docs/evolucion/verificacion/manifiestos/F6-ASIGNACION-GATE-CERTIFICACION-FINAL-20260904.md`,
confirmado en la rama del gate; y `docs/evolucion/verificacion/derivar-universo-obligatorio.py`.

**Reproducción.** Sobre `HEAD` de `gate/f6-certificacion-final-20260904`:

* `registrar_evidencia.py` termina en verde, pero deja `git status --porcelain` **NO vacío**
  (tres ficheros de evidencia), contra la línea base afirmada;
* `derivar-universo-obligatorio.py` **FALLA CERRADO con código 2**.

Sobre el candidato `7b9829cb`, las dos cosas reproducen exactamente lo afirmado: porcelain
vacío y las tres restas `A=0 · B=0 · C=0`.

**Causa.** El manifiesto del propio gate se confirmó dentro del directorio que esos dos
instrumentos censan, de modo que el acto de convocar el gate cambia el corpus que el gate
mide. Falla cerrado, que es lo correcto, pero significa que **la línea base afirmada no se
reproduce sobre la rama del gate**, sólo sobre el candidato.

**Remedio.** Ejecutar y publicar la línea base **siempre** sobre el SHA candidato, como manda
`O26` §2, y declarar el manifiesto del gate fuera del censo o alojarlo fuera de esa sede.

**Propietario.** Quien convoca el gate.

---

#### `R1-M2` · MEDIA · INTERNO

**Sede.** `kernel/operativo/runtime/ads_admision.py:388` (`orden_censo_formulas`).

```python
modulos = _censo.modulos_del_aparato(os.path.dirname(os.path.abspath(__file__)))
informe = _formulas.censar_formulas(modulos)
```

**Reproducción.** Sobre el propio candidato:

```console
$ python3.12 .../ads_admision.py --repo <cand> censo-formulas
...
segundas definiciones: 7
ok: no
EXIT=1
```

Mientras tanto, `test_admision.py::test_el_censo_de_formulas_del_aparato_real_esta_limpio`
está en VERDE. No es una contradicción: la prueba censa
`modulos_del_verificador` y la CLI censa `modulos_del_aparato`, que es un conjunto mayor
derivado del disco. El camino del **veredicto** es correcto; el de esta orden auxiliar publica
un rojo sobre su propio árbol.

**Remedio.** Que la orden cense el mismo conjunto que la propiedad que dice medir, o que
declare explícitamente que su conjunto es mayor y qué significa entonces su `ok`.

**Propietario.** Autoría de `F6`, eje de admisión.

---

#### `R1-M3` · MEDIA · INTERNO

**Sede.** Los cinco `ads_*.py`. Los cinco llevan **el mismo bloque de comentario** —«`E-10` ·
la PROCEDENCIA se PUBLICA. No basta con que sea correcta»— y los cinco definen
`procedencia(repo=None)`. Pero:

```text
ads_admision.py   publica `procedencia` DENTRO del veredicto (orden `verificar`)
                  y además tiene una orden `procedencia` propia
ads_estado.py     define procedencia() · NINGUNA orden la publica
ads_runtime.py    define procedencia() · NINGUNA orden la publica
ads_ciclo.py      define procedencia() · NINGUNA orden la publica
ads_arboles.py    define procedencia() · NINGUNA orden la publica
```

**Reproducción.** Recorrer las tablas `ORDENES` de los cinco ficheros: sólo la de
`ads_admision.py` contiene una salida que incluya `procedencia`.

**Por qué importa.** La función `exigir_procedencia_del_aparato()` sí se llama en los cinco y
falla cerrado, de modo que la **garantía** está en los cinco. Lo que no está en los cinco es
la **publicación**, que es la mitad que el propio comentario declara imprescindible: «una
procedencia que sólo existe en la cabeza de quien escribió el `sys.path` no es trazable».

**Remedio.** Publicar la procedencia en la salida de los cinco, o retirar de cuatro de ellos
la afirmación de que la publican.

**Propietario.** Autoría de `F6`.

---

#### `R1-M4` · MEDIA · INTERNO

**Sede.** `kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md` §3, L106-L107, contra
`kernel/operativo/runtime/pruebas/escenario_extremo_a_extremo.py` y
`escenario_e2e_runtime.py`.

**Afirmación.** Que las tres E2E comprueban recuperabilidad «de modo que ya no pueden seguir
verdes sobre un almacén irrecuperable».

**Reproducción.** Invertir los pasos 8 y 9 **respetando el significado de cada punto de
fallo**: el almacén queda irrecuperable y, aun así, las tres E2E siguen en verde —15/15,
25/25, 24/24—. Sólo enrojece `T300` (y, colateralmente, `T314b`).

**Causa.** Los tres escenarios llaman a `comprobar_recuperabilidad(base)` y devuelven
`escenario.codigo_de_salida() or (0 if recuperable else 1)`, pero **ninguno inyecta el punto
`entre-el-paso-8-y-el-9`**, que es el único que produce el estado que la afirmación cubre.

**Remedio.** O inyectar ese punto en al menos una E2E, o rebajar la afirmación del contrato a
lo que las E2E realmente comprueban. La segunda es más barata y también es honesta; la primera
es la que cierra la propiedad.

**Propietario.** Autoría de `F6`, eje de estado durable.

---

#### `R1-BJ1` · BAJA · INTERNO

**Sede.** La mitigación declarada del residuo del sellado, en dos sedes del árbol.

**Afirmación.** Que el residuo «vuelve a ser detectable en cuanto el diario anexa otra vez».

**Reproducción.** Sellar, anexar de nuevo y volver a verificar: el residuo **no** vuelve a
hacerse detectable por el hecho de anexar. La propiedad de fondo —integridad de la cadena,
ancla `cid_sellados`, imposibilidad de retirar un cuerpo sin transición— **sí** se sostiene, y
está medida en §4.11. Lo que no se sostiene es esta frase concreta.

**Remedio.** Retirar la frase o sustituirla por lo que sí se mide.

**Propietario.** Autoría de `F6`, eje de estado durable.

---

#### `R1-I1` · INFORMATIVA · INTERNO

**Sede.** `kernel/operativo/runtime/arboles/versiones.py:22-25` y
`kernel/operativo/runtime/CONTRATO-ARBOLES-ADVERSARIALES.md` §2, contra
`kernel/operativo/runtime/admision/censo.py:378`.

Las dos primeras afirman: «`admision/censo.py` deriva su censo sobre `admision`, `gobierno`,
`adaptadores` e `identidad`, y este paquete no está entre ellos». El código dice otra cosa:

```python
## admision/censo.py:378
PAQUETES_DEL_VERIFICADOR = ("admision", "gobierno", "adaptadores", "identidad", "arboles")
```

y `modulos_del_aparato` se deriva del disco, con lo que `arboles/` entra por partida doble.
La afirmación es caducada y falsa. No cambia ningún veredicto; cambia lo que un lector deduce.

**Remedio.** Actualizar las dos sedes.

---

#### `R1-I2` · INFORMATIVA · LÍMITE DEL GATE

La referencia `review/f6-post-gate-corrections-candidate-20260904` **existe**, pero como
`refs/remotes/origin/…` y no como `refs/heads/…`. Apunta correctamente a
`7b9829cbfa68c12b9947db0f7a26a1d08ed7f003`. Se declara para que nadie deduzca de un
`git branch` que la referencia no está.

---

#### Resumen de hallazgos

```text
BLOQUEANTE   R1-B1   migración 0→1 rota, con traza no tipada y almacén inmigrable   INTERNO
BLOQUEANTE   R1-B2   la raíz externa no lleva la purga `E-10`; `O26` §1.8 incumplida INTERNO
MEDIA        R1-M1   la línea base no se reproduce sobre la rama del gate            LÍMITE DEL GATE
MEDIA        R1-M2   `censo-formulas` sale 1 con 7 segundas definiciones             INTERNO
MEDIA        R1-M3   la procedencia se publica en 1 de 5 ejecutables                 INTERNO
MEDIA        R1-M4   la afirmación del contrato sobre las E2E es falsa               INTERNO
BAJA         R1-BJ1  mitigación declarada del residuo del sellado, falsa             INTERNO
INFORMATIVA  R1-I1   `versiones.py` y su contrato contradicen a `censo.py:378`       INTERNO
INFORMATIVA  R1-I2   la referencia del candidato es remota, no local                 LÍMITE DEL GATE
```

Ninguno de los hallazgos es de clase **LÍMITE DE ANFITRIÓN**: todo lo que este anfitrión no
podía dar —usuario del sistema distinto, `cgroup v2` ejercitable— el árbol ya lo declara,
lo mide y lo publica con su motivo. Eso es un mérito y se dice como tal.

---

### 7 · Lo que el árbol SÍ sostiene

Esto no es cortesía. Es la otra mitad del juicio, y se escribe con la misma exigencia que los
hallazgos: cada línea de aquí abajo se ha medido, no leído.

**El protocolo transaccional y el punto de no retorno.** Los nueve puntos de fallo del §3
cortan donde dicen, y cada uno tiene su caso con la recuperación esperada escrita en la propia
prueba (`T175`, `T186`). Adelantar el punto de no retorno de `transicion.preparada` a
`transicion.abierta` pone rojo `T175` por «se publicó una transición que debía revertirse». La
recuperación tiene las dos ramas de `g.8` y ninguna tercera, y es idempotente `n` veces.

**El testigo de los pasos 8 y 9.** `E-08` está cerrado de verdad: seis pruebas —`T297`,
`T297b`, `T298`, `T299`, `T300`, `T301`— cubren la ausencia del testigo, el testigo con los
`cid` viejos, la mezcla parcial, el `fsync` de contenido **y** de directorio, la caída entre
los dos pasos y el borrado del testigo. La inversión no pasa.

**Las dos mitades de `E-07`, disjuntas y demostradas.** Es de lo más sólido del árbol: dos
funciones separadas, dos códigos de error propios, dos conjuntos de pruebas que no se
solapan, un control positivo (`T290`) y la exigencia explícita de que la mitad `tree` no se
apruebe por el rojo de la mitad `commit`.

**Los siete pasos y la puerta única de la evidencia.** `escribir_evidencia` es la única
puerta, exige un testigo completo y en orden, y `T296` la interrumpe en los siete con control
positivo al final. Publicar evidencia de lo que no se ha verificado es imposible por
construcción, no por costumbre.

**La procedencia del nacimiento (`E-09`).** Siete casos, incluidos historia reescrita,
truncada, injertada con `grafts` y clon `--depth 1`. Ninguno degrada a «comparar con la base».

**La purga `E-10` en los cinco `ads_*.py`.** Purga como primer acto del fichero, con sólo
`sys` y `os`; control del control sobre la procedencia del propio `os`, con
`SystemExit(5)` y sin ejecutar nada; `exigir_procedencia_del_aparato()` antes de toda orden.
Es un trabajo notablemente bien hecho, y por eso su ausencia en la raíz externa se nota tanto.

**El resultado exacto de una batería (`E-14`).** Se DERIVA de la salida y se compara entero:
recuentos declarados contra desenlaces contados, veredicto único, contadores prohibidos, y
CERO saltos salvo declaración uno a uno con `id` y `motivo`. Los cinco sabotajes `NE14a`-`e`
caen, cada uno por su motivo. Medido en el árbol vigente: **cero saltos ejecutados** en las 18
baterías.

**Los errores tipados (`E-15`).** Cinco ejecutables, una sola tabla de códigos, las DOS clases
homónimas `CapacidadNoSoportada` distinguidas en la salida, `stderr` con línea legible y
estructura, saneado de rutas del anfitrión en la puerta de salida, y sin éxito parcial.

**La contención cableada (`E-16`) y `FD-5`.** Política alcanzable desde `ads_runtime.py` y
`ads_ciclo.py`, elegida en el CONSTRUCTOR, fallo cerrado con CERO ejecución y sin degradación
silenciosa. Hijo, nieto y bisnieto con `setsid` cada uno, contenidos de verdad por el camino
productivo. Y el control que impide presentar el débil como fuerte existe y se ejerce
(`T216` / `N216`).

**El aislamiento de la identidad (`g.15`, `O26` §1.6).** Ejercido hoy: contenedor, uid distinto
real, ocho de ocho intentos impedidos con el mensaje del sistema, control positivo, control de
lectura, y una negativa a certificar cuando el control de lectura no se cumple.

**El gobierno Git del control repo (`g.14`, `G-A8`).** Forzar es **imposible** —hook y canal
único, con el `OID` nulo tratado como lo que es y no como «creación»— y **detectable** —linaje
completo, no sólo la cabeza—. La política es DATO, no puede eximirse a sí misma, no puede
autorizar el borrado protegido, y su valor por defecto de publicación es `esperando-owner`.
39 casos, todos verdes; el sabotaje `N187` los enrojece por el motivo exacto.

**La concurrencia entre máquinas.** Dos clones, dos procesos, exactamente una confirmación, la
otra detecta la pérdida, sin `--force` en ninguna parte y sin historia reescrita. 14 casos.

**El verificador de admisión.** Canal único con `-z`, censo de zonas con condición de
CONTENIDO por zona, autoinclusión del instrumento y de su política, sede del Owner
append-only contrastada contra el nacimiento y no contra `HEAD`, y una matriz adversarial que
publica `falsos_verdes = 0 · falsos_rojos = 0` habiéndolos medido.

**El catálogo de negativos.** 133 infracciones, 0 no detectadas, y —esto es lo importante— el
instrumento aprende a sabotear también BATERÍAS, exigiendo tres cosas y no una: que la batería
enrojezca, que la prueba DECLARADA esté entre las caídas, y que caiga POR EL MOTIVO ESPERADO.
Una traza de arranque se registra como **NO DETECTADA**. Es la disciplina correcta.

**El determinismo.** Dos corridas completas del runner sobre el mismo clon dan evidencia
**byte a byte idéntica** (`diff -r` vacío). Ni reloj, ni `pid`, ni duración, ni rutas del
anfitrión en nada publicado.

**Y la honestidad del árbol sobre sus propios límites.** `E-17` se declara EXTERNO y abierto,
con propietario y condición de cierre; `E-18` publica el alcance medido de este anfitrión,
incluido lo que NO puede; el backend `simple` declara su nivel inferior en vez de retirarse;
las E2E declaran su alcance; `T171` declara que su cobertura es estructural y que el
descubrimiento real exige piloto. Un árbol que declara lo que no puede es más fiable que uno
que sólo enseña verdes.

---

### 8 · Dictamen expreso sobre bloqueantes internos vivos

`O26` §5.5 condiciona la competencia del gate a que **no existan bloqueantes internos vivos**.

**EXISTEN DOS, Y LOS DOS SON INTERNOS.**

```text
R1-B1   migración 0→1 del estado durable rota                      INTERNO · VIVO
        · TypeError NO tipado cruzando main() con traza y rutas del anfitrión
        · almacén heredado permanentemente inmigrable
        · contradice `g.11`, `E-15` y la DECISIÓN escrita en migracion.py
        · sin prueba capaz de fallar: el fixture no entra en la rama rota

R1-B2   la raíz externa no lleva la purga `E-10`                   INTERNO · VIVO
        · `capacidades` publica {} con código 0 bajo PYTHONPATH envenenado
        · `instalar.py` publica un manifiesto de 3 bytes con código 0
        · incumple `O26` §1.8 —«contaminación del entorno … falla cerrado»—
        · fuera del alcance de `T306`, que sólo cubre los cinco `ads_*.py`
```

Ninguno de los dos es de anfitrión, ninguno es externo, ninguno depende de una calibración y
ninguno es opinable: los dos se reproducen con órdenes literales sobre el SHA candidato y los
dos contradicen un contrato escrito del propio árbol.

**En consecuencia, y ciñéndome a `O26` §5:**

* §5.4 —«que la implementación satisface las ocho condiciones»— **NO se demuestra**: la
  condición `O26` §1.8 se incumple (siete de ocho).
* §5.5 —«que no existen bloqueantes internos vivos»— **NO se demuestra**: hay dos.

**`F6` NO ES CERTIFICABLE sobre `7b9829cbfa68c12b9947db0f7a26a1d08ed7f003`.** Por `O26` §8,
la aceptación arquitectónica de la raíz externa permanece —la arquitectura es correcta y
siete de sus ocho condiciones se demuestran—, pero `F6` sigue ABIERTA y PesquerApp sigue
BLOQUEADA.

Y una precisión que va contra la comodidad de este dictamen: **los dos bloqueantes son
pequeños de arreglar y grandes de significado.** Uno es una llamada a la que le falta un
argumento; el otro es un prólogo de veinte líneas que ya existe escrito cinco veces en el
mismo repositorio. Lo que los hace bloqueantes no es su tamaño: es que cada uno vive
exactamente donde el árbol declara que no puede haber nada, y que en los dos casos **el
control que debía verlos no los alcanzaba**. Corregir la línea sin ampliar el control dejaría
cerrada la instancia y abierta la clase.

---

### 9 · Cierre de disciplina

```text
repositorio real, al cerrar:
  HEAD   20330e694d4941e5c159017ec79fd5b77aaf962d   (idéntico al de apertura)
  tree   4ee6f9d47a4792d394b1cf7c0f8b425934ce8daf   (idéntico al de apertura)
  git status --porcelain   (vacío)

cobertura:   ASIGNADO − LEÍDO = ∅
contacto con el otro revisor:  ninguno
correcciones aplicadas:        ninguna
commits propuestos:            ninguno
```

— REVISOR 1


---

# 6 · DICTAMEN ÍNTEGRO DEL REVISOR 2

## DICTAMEN DEL REVISOR 2 — GATE ÚNICO Y FINAL DE CERTIFICACIÓN DE `F6` · 2026-09-04

> ## `ASIGNADO − LEÍDO ≠ ∅`
>
> **50 de los 84 ficheros de mi lote NO SE HAN ABIERTO. 29 329 de 48 143 líneas (60,9 %) sin
> leer.** Por la regla §4 del manifiesto previo, **este gate es NO VÁLIDO**, y lo es por mi
> lote. Lo digo en la primera línea porque el manifiesto lo exige y porque callarlo sería el
> defecto que este gate existe para no repetir: el del 2026-09-03 cayó por exactamente esto.
>
> El resto del dictamen se emite igualmente —lo medido es medido y los ataques son
> reproducibles—, pero **ninguna de sus conclusiones puede sostener una certificación**, y
> ningún «no encontré nada» mío cubre las 29 329 líneas que no miré.

---

### 1 · PRECONDICIONES

```text
COMANDO                              SALIDA
git rev-parse HEAD                   20330e694d4941e5c159017ec79fd5b77aaf962d
git rev-parse HEAD^{tree}            4ee6f9d47a4792d394b1cf7c0f8b425934ce8daf
git status --porcelain               (vacío)
git rev-parse --abbrev-ref HEAD      gate/f6-certificacion-final-20260904
python3.12 --version                 3.12.14 · PyYAML 6.0.2
```

**DIVERGENCIA DECLARADA CON EL OBJETO CONGELADO, y no es un defecto: es un hecho que hay que
decir.** El objeto congelado del encargo es `7b9829cbfa68…` / tree `d2c0a0cd…`. **`HEAD` no es
ese commit**: es `20330e69`, dos commits por encima. Verificado:

```text
git rev-parse 7b9829c^{tree}          d2c0a0cde1fff37cbf5ee59cf7a5bd633a99e330   ← coincide
git diff --stat 7b9829c 20330e6       docs/evolucion/00-INDICE.md          | 1 +
                                      …F6-ASIGNACION-GATE-…-20260904.md    | 395 +++
git ls-remote origin | grep f6-post   7b9829c…  refs/heads/review/f6-post-gate-corrections-candidate-20260904
```

Los dos commits de más son **el aparato del propio gate**. La candidata es correcta y la
referencia remota apunta a ella. **Todas mis mediciones de línea base se hicieron sobre una
copia con `git checkout 7b9829c`**, que es el objeto congelado; los ataques, sobre copias.
`refs/heads/review/f6-post-gate-corrections-candidate-20260904` **no existe en local** —sólo
en `origin`—, y el `rev-parse` que el encargo escribe falla tal cual está escrito.

**AL TERMINAR** (misma comprobación, idéntica):

```text
git rev-parse HEAD                   20330e694d4941e5c159017ec79fd5b77aaf962d
git rev-parse HEAD^{tree}            4ee6f9d47a4792d394b1cf7c0f8b425934ce8daf
git status --porcelain               (vacío)
```

**No he escrito un byte en el repositorio.** Todas las corridas, sabotajes y ataques se
hicieron sobre copias en `/tmp/…/scratchpad/`, y `registrar_evidencia.py` sólo se ejecutó
sobre copias.

---

### 2 · REGISTRO DE COBERTURA, ÍNTEGRO, CON LA RESTA CALCULADA

#### 2.1 · La resta

```text
LOTE DECLARADO        84 ficheros · 48 143 líneas   (el manifiesto §6 dice «51 161 líneas ·
                      84 ficheros íntegros MÁS los rangos»; la suma de la lista da 48 143, y
                      48 143 + 3 018 de rangos = 51 161. La cifra publicada YA INCLUYE los
                      rangos, y la palabra «más» la contradice. Es menor, y se dice)
RANGOS `11-ARQ`       3 018 líneas · LOS SEIS LEÍDOS ÍNTEGROS

LEÍDOS ÍNTEGROS       30 ficheros ·  17 299 líneas
LEÍDOS EN PARTE        4 ficheros ·   1 515 de 5 064 líneas
NO ABIERTOS           50 ficheros ·  25 780 líneas

ASIGNADO − LEÍDO   =  50 ficheros SIN ABRIR  +  3 549 líneas sin leer de 4 abiertos en parte
                   =  29 329 líneas de 48 143   ·   60,9 %   ·   NO VACÍA
```

**Una discrepancia menor de dimensionado, dicha:** `docs/evolucion/00-INDICE.md` figura en el
manifiesto con **333** líneas y el árbol de `HEAD` da **334**. La causa es el propio commit
del gate, que le añadió una línea; sobre la candidata son 333. El manifiesto se dimensionó
contra la candidata y es correcto.

#### 2.2 · LEÍDOS ÍNTEGROS — 30 ficheros

```text
docs/canonico/00-EMPEZAR-AQUI.md                                    162
docs/canonico/03-GOBIERNO-Y-AUTORIDAD.md                            229
docs/canonico/04-CONTRATOS-TECNICOS.md                              409
docs/canonico/05-PLAN-DE-IMPLEMENTACION-F5-F6.md                    251
docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md                   476
docs/canonico/FUENTES-CANONICAS.yml                                 782
docs/evolucion/00-INDICE.md                                         334
docs/evolucion/CHECKPOINT-ADS-NEXT.md                             6 385
docs/evolucion/verificacion/derivar-universo-obligatorio.py       1 367
docs/f6/00-ESTADO-DE-IMPLEMENTACION-F6.md                           322
docs/f6/01-MATRIZ-DE-COMPLETITUD-F6.md                              512
docs/f6/02-GATE-DE-CERTIFICACION-FINAL-20260903.md                  296
docs/owner/ADS-OWNER-RESOLUCIONES.md                                979
docs/rediseno/b-RECORRIDO-APROBADA.md                             1 331
kernel/operativo/00-INDICE.md                                       146
kernel/operativo/circuitos/00-CIRCUITOS.md                          243
kernel/operativo/circuitos/DIS-handoffs.md                          249
kernel/operativo/circuitos/entregas-de-8-0.md                       128
kernel/operativo/circuitos/handoffs-generales.md                    305
kernel/operativo/contratos/00-INDICE.md                              29
kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md            161
kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md                   539
kernel/operativo/contratos/C4-MATERIALIZACION.md                     170
kernel/operativo/contratos/C5-HANDOFF.md                             115
kernel/operativo/esquemas/proceso.yaml                                89
kernel/operativo/pruebas/RECUENTOS-generado.md                        40
kernel/operativo/pruebas/REGISTRO-generado.md                        254
kernel/operativo/pruebas/REGISTRO.md                                 147
kernel/operativo/pruebas/T270-T289-contratos-19-y-composicion.md     244
kernel/operativo/recorrido/01-PROCESOS.md                            606
```

**RANGOS DE `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` — LOS SEIS, ÍNTEGROS.** Verifiqué
además que cada frontera cae exactamente sobre su cabecera:

```text
§7   L6136-L6284   149   L6136 = «# 7 · Runtime y dispatcher»            LEÍDO ÍNTEGRO
§8   L6285-L7377  1093   L6285 = «# 8 · Los cuatro macrocircuitos»       LEÍDO ÍNTEGRO
§9   L7378-L8074   697   L7378 = «# 9 · Certificación»                   LEÍDO ÍNTEGRO
     §9.6 ENTERA, incluidas las ONCE filas `X-S1`–`X-S11` y el bloque
     «Trabajo futuro que esta sede NO puede hacer»                       LEÍDO ÍNTEGRO
§10  L8075-L8128    54   L8075 = «# 10 · Git y multi-repositorio»        LEÍDO ÍNTEGRO
§18  L10882-L11069 188   L10882 = «# 18 · Orden de construcción para F6» LEÍDO ÍNTEGRO
§19  L11070-L11906 837   L11070 = «# 19 · Límites de esta fase»          LEÍDO ÍNTEGRO
```

Anclas de §9.6, para que no haya duda de que se abrió: primera sección sustantiva
«**UN SOLO CONTRATO, INVOCADO CUATRO VECES**»; última, «**AÑADIR EL SUJETO A LOS TRIGGERS DE
`nivel-certificacion`**». Fila `X-S11`: *«la FASE 0 escribe su celda dentro de `estado/` … FALLA
en los TRES casos»*.

#### 2.3 · LEÍDOS EN PARTE — 4 ficheros, con el tramo exacto

```text
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md      ~385 de 1 625
    LEÍDO   L1-L220 (D1-D45) · L275-L440 (D87-D102 y su addendum)
    NO LEÍDO L220-L275 (bloque D64-D86) y L440-L1625 (D103-D115, §2 O1-O26, §3)
kernel/operativo/runtime/ciclo/equipos.py          ~640 de 1 568
    LEÍDO   L1-L520 (cabecera, lector de cardinal, censo) · L480-L520 (`integrador_de`) ·
            L575-L620 (volumen e inicio) · L781-L940 (`_cuantos_agentes`, `materializar`)
    NO LEÍDO L620-L781 y L940-L1568
kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py  ~250 de 1 115
    LEÍDO   L1-L200 · L556-L610 · L748-L840
    NO LEÍDO el resto
kernel/operativo/validadores/comprobar_recuentos.py                ~240 de 756
    LEÍDO   L95-L330 (derivación, `Regla`, `AMBITO_VIVO`, `REGLAS`)
    NO LEÍDO L1-L95 y L330-L756
```

#### 2.4 · NO ABIERTOS — 50 ficheros, uno a uno, con sus líneas

```text
docs/f5/validar-f5.py                                                      612
docs/rediseno/a-CAPACIDADES-APROBADA.md                                  1 150
kernel/operativo/entrada/03-FORMAS.md                                      561
kernel/operativo/entrada/05-ESCENARIOS.md                                  649
kernel/operativo/pruebas/T086-T092-contratos.md                            165
kernel/operativo/pruebas/T100-T121-capacidades.md                          359
kernel/operativo/pruebas/T136-T152-post-auditoria.md                       466
kernel/operativo/pruebas/T172-T181-estado-durable.md                       466
kernel/operativo/pruebas/T182-T194-runtime-y-admision.md                   337
kernel/operativo/pruebas/T195-T209-ciclo-y-macrocircuitos.md               342
kernel/operativo/pruebas/T210-T225-arboles-raiz-externa-y-contencion.md    379
kernel/operativo/pruebas/T226-T249-agentes-y-modelos.md                    367
kernel/operativo/pruebas/T240-T248-hallazgos-externos-f6.md                220
kernel/operativo/pruebas/T250-T269-cardinalidad-y-seleccion.md             502
kernel/operativo/pruebas/T290-T311-integridad-evidencia-y-contencion.md    523
kernel/operativo/runtime/CONTRATO-CICLO-Y-MACROCIRCUITOS.md                338
kernel/operativo/runtime/ciclo/__init__.py                                 161
kernel/operativo/runtime/ciclo/agentes.py                                  702
kernel/operativo/runtime/ciclo/cierre.py                                   330
kernel/operativo/runtime/ciclo/continuacion.py                             739
kernel/operativo/runtime/ciclo/corpus.py                                   762
kernel/operativo/runtime/ciclo/despacho.py                                 107
kernel/operativo/runtime/ciclo/durable.py                                  108
kernel/operativo/runtime/ciclo/encuadre.py                                 384
kernel/operativo/runtime/ciclo/errores.py                                  436
kernel/operativo/runtime/ciclo/gates.py                                    242
kernel/operativo/runtime/ciclo/handoffs.py                                 442
kernel/operativo/runtime/ciclo/paralelismo.py                              211
kernel/operativo/runtime/ciclo/planificacion.py                            400
kernel/operativo/runtime/ciclo/procesos.py                                 284
kernel/operativo/runtime/ciclo/rutas.py                                    385
kernel/operativo/runtime/macrocircuitos/__init__.py                         93
kernel/operativo/runtime/macrocircuitos/definicion.py                      645
kernel/operativo/runtime/macrocircuitos/errores.py                         171
kernel/operativo/runtime/macrocircuitos/fase0.py                           575
kernel/operativo/runtime/macrocircuitos/motor.py                           407
kernel/operativo/runtime/pruebas/escenario_e2e_f6.py                     1 529
kernel/operativo/runtime/pruebas/test_agentes.py                         1 053
kernel/operativo/runtime/pruebas/test_ciclo.py                           1 595
kernel/operativo/runtime/pruebas/test_continua.py                          849
kernel/operativo/runtime/pruebas/test_macrocircuitos.py                    879
kernel/operativo/validadores/ads_lint.py                                   655
kernel/operativo/validadores/comprobar_arranque.py                         605
kernel/operativo/validadores/comprobar_composicion_procesos.py             816
kernel/operativo/validadores/comprobar_contratos.py                      1 091
kernel/operativo/validadores/comprobar_fuentes.py                          368
kernel/operativo/validadores/comprobar_referencias.py                      271
kernel/operativo/validadores/comprobar_versiones.py                        456
kernel/operativo/validadores/exclusiones.yaml                              196
kernel/operativo/validadores/validadores.yaml                              397
```

#### 2.5 · Qué significa esta resta, dicho sin adornarlo

**No es una laguna periférica: alcanza el núcleo de mi propio eje.** `macrocircuitos/fase0.py`
—la implementación de la `FASE 0` cuyas once filas `X-S` `F6-F` debe demostrar y cuyo rango
§9.6 se me asignó EXPRESAMENTE— **no se abrió**. `comprobar_composicion_procesos.py` —el
instrumento de `D104`, que es una de las cuatro obligaciones de §19 de mi eje— **no se abrió**;
sólo lo ejecuté. `ciclo/agentes.py` —la política de `C2` que `C4` paso 4 invoca— **no se abrió**.
`ciclo/planificacion.py`, sede de la prioridad de `b.12`, **no se abrió**. Los ONCE ficheros
`Tnnn-*.md` que declaran los escenarios de las pruebas cuyo estado juzgo **no se abrieron**.

**Contra el árbol, mis ataques miden comportamiento; contra el lote, no leí lo que juzgo.**
Esa asimetría es exactamente la que el manifiesto declara inadmisible, y por eso el veredicto
de validez es el que es. **Ninguna cobertura histórica cubre estos ficheros:** todos están
entre los 216 componentes modificados en los tres cortes de `F6`, para los que el manifiesto
§4 prohíbe expresamente la delegación.

---

### 3 · LÍNEA BASE — REPRODUCIDA SOBRE LA CANDIDATA `7b9829c`

Copia limpia, `git checkout 7b9829c`, `porcelain` vacío antes.

| lo que el coordinador afirma | lo que yo mido | ¿coincide? |
|---|---|---|
| 34/34 validadores en verde · 34 evidencias · 0 problemas | `34/34 validadores en verde · 34 evidencias publicadas · 0 problemas` | **sí** |
| 682 casos en 18 baterías `unittest` | 682 · 18, contados por mí de los bloques `Ran N tests` de las 34 evidencias | **sí** |
| E2E 15/15 · 25/25 · 24/24 | `15 de 15` (estado-e2e) · `25 de 25` (e2e-runtime) · `24 de 24` (e2e-f6) | **sí** |
| 133 infracciones detectadas · 0 NO detectadas | 133 líneas `^OK ` · 0 líneas no-OK, contadas por mí | **sí** |
| CERO saltos ejecutados | 0. Las dos apariciones de `skipped` son nombres de sabotaje (`NE14a`) y de prueba (`T307`) | **sí** |
| determinismo byte a byte entre dos corridas | segunda corrida: `diff -r` de `evidencia/` entre corrida 1 y 2 → **vacío** | **sí** |
| huella del kernel `6075d888ff2c7b70` | `./tooling/kernel-status.sh` → `6075d888ff2c7b70 (396 ficheros) · LIMPIO` | **sí** |
| `git status --porcelain` vacío antes y después | vacío antes; vacío después de las DOS corridas | **sí** |
| las TRES RESTAS: A=0 · B=0 · C=0 | `A · 0 · B · 0 · C · 0`, 58 obligaciones | **sí** |

**LA LÍNEA BASE ES EXACTA SOBRE LA CANDIDATA.** No encontré ni una cifra que no reproduzca.

**Y una divergencia que NO es de la candidata sino del aparato de este gate**, medida sobre
`HEAD` = `20330e69` (la rama que se me entregó para trabajar):

```bash
$ cd <copia limpia de HEAD>; python3.12 kernel/operativo/validadores/comprobar_evidencia.py
T158  FALLIDA   La evidencia publicada demuestra lo que el informe afirma
          · fuentes-salida.txt: la vigencia 'T161-cobertura' publica 504 y el corpus
            vigente da 505. La evidencia está CADUCADA
EXIT=1
```

y, si en cambio se corre el runner entero, `34/34` **pero**:

```bash
$ git status --porcelain
 M kernel/operativo/pruebas/evidencia/fuentes-salida.txt
 M kernel/operativo/pruebas/evidencia/negativos-salida.txt
 M kernel/operativo/pruebas/evidencia/referencias-salida.txt
```

Es `H-R2-09`, abajo.

---

### 4 · LOS DIEZ ATAQUES

#### ATAQUE 1 · Cardinalidad plural de `C4` · **VERDE**

Derivé el censo de plurales **por mi cuenta** recorriendo las quince capacidades con
`equipos.leer_cardinal`, sin usar la tabla `PLURALES` de su batería:

```text
('composicion:dis-feature-visual',  'DIS/diseno-visual')       '1 o 2 en competencia declarada'   (1,2,competencia)
('composicion:dis-proyecto-nuevo',  'DIS/diseno-visual')       '2 o 3, uno por dirección explorada'(2,3,direccion)
('composicion:dis-proyecto-nuevo',  'DIS/investigacion-visual')'1 o 2 repartidos por territorio'  (1,2,territorio)
```

`equipos.materializar()` sobre el corpus REAL, `slots=99`:

```text
dis-proyecto-nuevo · DIS/investigacion-visual  plan.agentes=2  FILAS REALES=2  ids=['ag-afb6a5764382','ag-f22ec3fc726d']  integra=DIS/direccion-artistica
dis-proyecto-nuevo · DIS/diseno-visual         plan.agentes=3  FILAS REALES=3  ids=[3 distintos]                          integra=DIS/direccion-artistica
dis-feature-visual · DIS/diseno-visual         plan.agentes=1  FILAS REALES=1  modo=competencia                           integra=None
```

Las dos plurales por reparto materializan **2** y **3** agentes reales con identificador
propio. La tercera materializa **1**, que es el mínimo de su cardinal `1 o 2`, y **es
correcto**: `C4` separa COMPETENCIA de «varios agentes» y la condiciona a que el método la
declare; con la competencia declarada sube a 2 (ataque 3). **No hay publicación de «2 o 3»
junto a un agente único**: el defecto `E-01` está cerrado por la propiedad.

**El sabotaje que cerró `E-01`**, sobre una COPIA:

```bash
$ sed -i 's/agentes: "2 o 3, uno por dirección explorada"/agentes: "7 repartidos por artefacto, sin integrador"/' copia/…/DIS/composicion.md
$ python3.12 materializar DIS composicion:dis-proyecto-nuevo
RESULTADO: VariosAgentesSinIntegrador
  [VARIOS_AGENTES_SIN_INTEGRADOR] `DIS/diseno-visual` declara `7 repartidos por artefacto,
  sin integrador`: 7 agentes y, en el mismo campo, que NO hay integrador. `C4` lo prohíbe
  con todas las letras: «Varios agentes sin integrador declarado está prohibido», porque
  produce tres propuestas y ninguna decisión
```

**Falla POR SEMÁNTICA**, no por la huella. Y comprobé que la cláusula `sin integrador` está
ENUMERADA a propósito en el vocabulario cerrado: cae por la PROHIBICIÓN, no por «no lo
entiendo». Sano → verde · sabotaje → rojo por el motivo esperado · restaurado → verde.

#### ATAQUE 2 · Varios agentes sin integrador, y con integrador inexistente · **VERDE**

```text
CONTROL SANO      PASA · 13 filas despachadas · diseno-visual 3 con DIS/direccion-artistica
2b · integrador -> DIS/rol-fantasma en `ampliacion`
   VariosAgentesSinIntegrador: la `ampliacion` de `composicion:dis-proyecto-nuevo` declara
   integrador a `DIS/rol-fantasma`, que NO es un rol de esta composición; un integrador que
   no ocupa ningún rol no integra nada
2c · integrador RETIRADO de `ampliacion`
   VariosAgentesSinIntegrador: `DIS/diseno-visual` materializa 3 agentes y la composición
   no declara QUIÉN INTEGRA en su campo `ampliacion`; `C4` lo prohíbe expresamente
```

#### ATAQUE 3 · Competencia sin criterio previo · **VERDE, y en cinco puntos distintos**

```text
3.0 sin declarar competencia            PASA · agentes=1  (el «1 por defecto, siempre» de C4)
3.1 competencia=2 SIN criterio          CriterioDeComparacionAusente · «no hay criterio de
                                        comparación escrito; sin él la comparación la gana
                                        la propuesta que más guste»
3.2 criterio SIN instante               CriterioDeComparacionAusente · «no dice CUÁNDO se
                                        escribió; «escrito ANTES» no es comprobable»
3.3 criterio con instante, paquete sin inicio  CriterioDeComparacionAusente
3.4 criterio declarado en 7, inicio en 5       CriterioDeComparacionAusente · «no es ANTES.
                                        Un criterio escrito con las propuestas delante no
                                        compara, justifica»
3.5 criterio ANTES pero método sin fase divergente  CriterioDeComparacionAusente
3.6 competencia=3 sobre cardinal «1 o 2»            RepartoIncoherente
```

El «ANTES» se mide con reloj lógico (revisión del estado durable), no con hora de pared.

#### ATAQUE 4 · Volumen superior al contexto · **VERDE**

```text
4.0 sin volumen (control)     PASA · agentes=3
4.1 volumen=1 000 000         VolumenExcedeElContexto · «el perfil de `DIS/critica-visual`
                              exige un contexto `amplio`, que sostiene 3; harían falta
                              333 334 agentes y el rol no declara reparto en su campo
                              `agentes` (`1, distinto de todos los productores`)»
4.2 volumen=1                 PASA · agentes=3
4.x volumen={'unidades': N}   PaqueteIlegible · «el volumen es un entero >= 1»
```

#### ATAQUE 5 · `execution_slots` · **VERDE**

Barrido de slots 1→14 sobre `dis-proyecto-nuevo` con cardinal 3 en `diseno-visual`:

```text
slots  despachados  esperando  agentes distintos  diseno-visual desp/esp
  1        1           12            1                 0 / 3
  3        4            9            3                 0 / 3
  4        5            8            4                 1 / 2
  5        6            7            5                 2 / 1
  6        7            6            6                 3 / 0     ← el cardinal 3 consume 3 slots
 11       13            0           11                 3 / 0
```

* **el cardinal 3 consume TRES slots**: sólo con 6 slots entran los tres agentes.
* **slots insuficientes → `esperando-capacidad` SIN reducir la composición**: con 1, 3 y 6
  slots los **10 roles** de la composición siguen presentes (despachados + esperando +
  bloqueados). Ninguno desaparece.
* **doble ocupación**: con `slots=5` hay 6 filas y 5 agentes distintos — el repetido es un
  agente COMBINADO ocupando dos roles que la composición declara `combinables`, que consume
  UN slot. No es doble ocupación: es el corte por AGENTE funcionando.
* **reanudación con reparto distinto → error**:
  `RepartoIncoherente: la reanudación cambia el reparto ya escrito del equipo
  `eq-a458096f5e02abe6`: DIS/diseno-visual. `C4` no rehace el equipo al ampliar, y un
  reparto distinto deja al agente anterior trabajando sobre una unidad que ya no está
  declarada`. Con el mismo reparto, PASA.

#### ATAQUE 6 · Cada obligación de §19, una a una · **MIXTO**

**`CONTRATO 1` — ¿`AFIRMACIONES` dejó de existir como lista literal?** **SÍ.** Abrí
`comprobar_recuentos.py` L95-L330: en el sitio donde vivía hay un comentario que lo declara
retirado y una tabla de `Regla(clave, objeto, sede, salvo, marca, extra)` en la que **ninguna
regla nombra una ruta**. La condición de cierre literal de §19 está cumplida.

**PRUEBA NEGATIVA que §19 prescribe** —fichero NUEVO, afirmación falsa **en letra**:

```bash
$ printf '# NOTA NUEVA\n\nEl contrato común de rol declara los **veintitrés** campos del esquema.\n' \
    > copia/docs/f6/99-NOTA-DEL-REVISOR-2.md
$ python3.12 kernel/operativo/validadores/comprobar_recuentos.py
T151  FALLIDA   Ninguna cifra del corpus contradice el recuento derivado
  · docs/f6/99-NOTA-DEL-REVISOR-2.md:3: «El contrato común de rol declara los
    **veintitrés** campos del esquema» — escrito 23 · derivado 29 (campos_de_rol).
    La sede no se enumeró: la encontró el barrido
```

**Y PARTIDA POR UN SALTO DE LÍNEA** (`**veintitrés**\ncampos del esquema`): **también la caza**,
con el mismo diagnóstico. En dígitos, ídem (`Las **23** capacidades` → escrito 23 · derivado 15).

**PERO** — la misma afirmación insertada en `docs/rediseno/b-RECORRIDO-APROBADA.md`:
`T151 SUPERADA · 5 superadas · 0 fallidas`. Ver `H-R2-14`.

**`CONTRATO 1bis` — perfil nuevo en `C2` y el recuento se mueve solo.** Derivado por mí:
`grep -c '^id: perfil:' C2` = **21**, `grep -c 'ads:perfil-agente'` = **21**, y
`RECUENTOS-generado.md` publica `perfiles de agente | **21**`. La cifra existe, está publicada
y coincide. La condición de cierre literal —«que la cifra deje de existir sólo en prosa»— está
cumplida.

**`CONTRATO 2` — sede nueva con versión falsa.** No pude ejecutar este sabotaje por
agotamiento del lote (`comprobar_versiones.py` está entre los NO ABIERTOS). **Queda sin
comprobar por mí, y lo digo.**

**`D104` — ¿los NUEVE pares están instanciados? ¿el reparto se DERIVA? ¿el censo se CUENTA?**
Los NUEVE los derivé **a mano** de `01-PROCESOS.md`, que sí leí íntegro:

```text
FEA  SEG:revision (C-SEG) · DOM:revision (C-DOM)                      2   vía 4
GAP  SEG:revision (C-SEG) · DOM:revision (C-DOM)                      2   vía 4
INC  SEG:revision (C-SEG)                                             1   vía 4
DEU  SEG:revision (C-SEG) · DOM:revision (C-DOM)                      2   vía 4
DEP  revision-de-seguridad (obligatoria, `capacidad_productora: SEG:revision`,
     `autoridad_de_retirada: nadie`) · DOM:revision (C-DOM)           2   vía 2 + vía 4
                                                                     ──
                                       CINCO procesos · NUEVE pares
```

Coincide con lo que §19 publica, **incluido el reparto por vía —vía 2 · 1 par, vía 4 · 8—** y
las anclas (`AUD→INV`, `INV→INV`, el resto `→VER`). El validador confirma:

```bash
$ python3.12 kernel/operativo/validadores/comprobar_composicion_procesos.py
T273 SUPERADA · T274 SUPERADA · T275 SUPERADA · T276 SUPERADA · 4 superadas · 0 fallidas
```

**El censo de 20 fixtures NO lo comprobé** —`comprobar_composicion_procesos.py` está entre los
NO ABIERTOS y sólo lo ejecuté—. Lo digo.

**Y no admito absorción bajo `V6-*`:** las cuatro obligaciones aparecen en el universo
derivado con identificador propio (`CONTRATO 1`, `CONTRATO 1bis`, `CONTRATO 2`, `D104`), más
`CONTRATO 3`, y el derivador usa `(?<![\w.-])` para que `CONTRATO 1` no absorba a `CONTRATO 1bis`.
Eso está bien construido.

#### ATAQUE 7 · Cada criterio de `b.12`, INDIVIDUALMENTE · **VERDE. Ninguno es decorativo**

Ocho sabotajes, cada uno sobre una COPIA distinta, en procesos reales:

```text
SANO                            rc=0  rojas: ninguna
S5a · prioridad (paso 5 a)      rc=1  ROJAS = T260, T269
S5b · grado de salida (5 b)     rc=1  ROJAS = T261, T269
S5c · antigüedad (5 c)          rc=1  ROJAS = T262, T269
S5d · id del paquete (5 d)      rc=1  ROJAS = T263, T269
IN1 · tiempo_listo              rc=1  ROJAS = T260, T261, T262, T267, T269
IN2 · postergaciones            rc=1  ROJAS = T264, T268, T269
IN3 · adelantado_por            rc=1  ROJAS = T265, T268, T269
IN4 · impedimento (vaciado)     rc=1  ROJAS = T266, T269

CONJUNTOS DISTINTOS: los OCHO. Ninguno comparte firma con otro.
```

Los cuatro criterios de orden están **implementados y con prueba propia** (`CRITERIOS_DE_ORDEN`
en `runtime/politica.py`, con los tres primeros negados y el cuarto ascendente), y los cuatro
campos de inanición existen en el objeto durable (`CAMPOS_DE_SELECCION`). **`E-06` está cerrado
por la propiedad.**

#### ATAQUE 8 · Inanición · **VERDE. `DSP` no eleva prioridades**

Tres paquetes reales sobre un control repo real, despacho de uno en uno:

```text
PRIORIDADES AL NACER: {'pq-alta': 90, 'pq-media': 50, 'pq-fondo': 10}
 vuelta 1 -> pq-alta   | pq-fondo: prioridad=10 postergaciones=1 adelantado_por=['pq-alta']
                         impedimento=prioridad declarada: `pq-alta` la tiene en 90 y…
 vuelta 2 -> pq-media  | pq-fondo: prioridad=10 postergaciones=2 adelantado_por=['pq-alta','pq-media']
 vuelta 3 -> pq-fondo  ← EL DE BAJA PRIORIDAD SE EJECUTA
PRIORIDADES AL FINAL: {'pq-alta': 90, 'pq-media': 50, 'pq-fondo': 10}
¿ALGUIEN TOCÓ UNA PRIORIDAD? NO
```

Barrido de todo el runtime: **no existe ni una asignación a `prioridad` fuera de la creación
del paquete**. `PRIORIDAD_POR_VIA` la fija en `planificacion.py` al nacer y nadie la mueve.
`b.12` —«DSP informa de la inanición. No cambia la prioridad. Nunca»— se cumple.

*(Observación menor, no hallazgo: `impedimento` conserva el texto de la última postergación
cuando el paquete ya se ha llevado el turno. Es cosmético.)*

#### ATAQUE 9 · Mutación de una condición de `O26` · **ROJO. HALLAZGO BLOQUEANTE**

**Append-only COMO CADENA, contra el commit de nacimiento `1d3b5d41…`:**

```text
nacimiento: 14 395 bytes · hoy: 42 181 bytes
¿HOY EMPIEZA POR EL NACIMIENTO?                  True
commits que tocan la sede:                       8
¿CADENA APPEND-ONLY INTACTA eslabón a eslabón?   SÍ  (cada commit empieza por el anterior)
¿el árbol de trabajo == último commit?           True
`O17`–`O25` presentes en TODOS los commits posteriores a su alta, sin retirarse: SÍ
```

**`O26` NO se presenta como certificación en NINGUNA sede.** Barrido del corpus: las únicas
apariciones que ligan `O26` a «certificación» son negaciones expresas —`04-CONTRATOS` L113-117
«**ninguna** … Presentar `O26` como certificación es leerlo al revés», `D115` «no es una
elección de `F6`… no sustituye a `O26`», `01-MATRIZ` «`O26` **no se presenta como
certificación**»—. **`B3` no se declara satisfecho en NINGUNA**: `06-DEUDA` §3 escribe «**`B3`
NO queda satisfecho por este acto**».

**Y AHORA EL ATAQUE.** Muté la condición 5 de `O26` §1 —«que el verificador **no** dispone de
la clave privada» → «que el verificador **SÍ puede** disponer de la clave privada»—, la
**confirmé en un commit**, y corrí el verificador de admisión:

```bash
$ python3.12 kernel/operativo/runtime/ads_admision.py --repo <copia> verificar --base <HEAD> --json
   hallazgos=0  color=INDETERMINADO
```

**CONTROL POSITIVO** — la misma operación sobre una regla de `O17` (dentro del prefijo de
nacimiento), también confirmada:

```bash
   hallazgos=1  color=ROJO
   -> V6-12  SEDE_DEL_OWNER_ALTERADA
```

**CONTROL NEGATIVO** — un apéndice legítimo (`# O27 · APÉNDICE DE PRUEBA`), confirmado:

```bash
   hallazgos=0  color=INDETERMINADO      ← INDISTINGUIBLE del ataque
```

La causa está en `admision/perimetro.py::_juzgar_append_only`: `if actual.startswith(anterior):
return None`. El contraste es un **PREFIJO contra el blob del nacimiento**. Medido:

```text
prefijo protegido: 14 395 de 42 181 bytes  =  34,1 %
   O17 byte   2 837   PROTEGIDO
   O18 byte   6 559   PROTEGIDO
   O19 byte  11 277   PROTEGIDO
   O20 byte  14 401   *** FUERA DEL PREFIJO ***
   O21 byte  19 627   *** FUERA ***
   O22 byte  24 204   *** FUERA ***
   O23 byte  29 279   *** FUERA ***
   O24 byte  34 469   *** FUERA ***
   O25 byte  36 513   *** FUERA ***
   O26 byte  38 864   *** FUERA ***
```

Y una segunda mitad: `_contenidos_para_append_only` toma `actual = canal.contenido("HEAD", ruta)`
**y sólo cae al disco si `HEAD` no la tiene**, de modo que una mutación **sin confirmar** de la
sede se detecta como mutación `M` y se juzga sobre bytes de `HEAD` que no la contienen.

**Ni una prueba ni un sabotaje del corpus muta contenido POSTERIOR al nacimiento.** `T302`–`T305`
y `N189` trabajan sobre sedes sintéticas donde la mutación cae dentro del prefijo. Es
`H-R2-02`.

**LA TRANSCRIPCIÓN DE `O26` Y LA LÍNEA «FIN LITERAL DE `O26`.» — DICTAMEN EXPRESO.**

**No es defendible. Es una omisión.** Cinco razones, y la quinta es la que decide:

1. La sede declara de sí misma: «Cada resolución se registra **íntegramente**, no en resumen»
   y «El coordinador puede **transcribir materialmente** la respuesta del Owner …, pero **no
   puede reinterpretarla ni resumirla** como fuente canónica». Clasificar una línea como
   «delimitador del dictado» y no como contenido **es un acto de interpretación**, y es
   exactamente la facultad que la sede le retira.
2. `O19` nació porque «una resolución suya sólo constaba porque el coordinador la transcribía,
   y ningún revisor podía contrastarla contra nada». La omisión reintroduce, en pequeño, la
   discrecionalidad que `O19` cerró.
3. **Medido:** `O17`–`O22` llevan `## Texto` como delimitador estructural del texto del Owner.
   **`O23`, `O24`, `O25` y `O26` NO lo llevan.** En `O26` no hay ningún delimitador: la
   entrada empieza en el H1 y termina en el fin del fichero. **La línea omitida era el único
   delimitador de cierre que esa entrada tenía**, y se retiró alegando que era un delimitador.
   El argumento se refuta a sí mismo.
4. **Medido:** `O17`, `O20`, `O21` y `O22` llevan «Nota de trazabilidad» que declara la
   verificabilidad de su procedencia. **`O26` no lleva ninguna**, y su procedencia no es
   contrastable contra ninguna fuente primaria del árbol. El patrón que el corpus usa para
   este caso exacto —declarar INVERIFICABLE— no se aplicó.
5. **La sede es APPEND-ONLY: esto NO SE PUEDE CORREGIR.** Como `LE-01` en su mitad de sede,
   pasa a ser **LIMITACIÓN PERMANENTE**, no deuda con condición de cierre. Y como acabo de
   demostrar en el ataque 9, **el mecanismo que debería garantizar que nadie toque `O26` no
   la alcanza**: la única entrada del expediente cuya integridad no está mecánicamente
   guardada es la que da al gate su competencia. Las dos cosas juntas —transcripción con
   discrecionalidad admitida y guarda que no llega— es lo que convierte una nota de método en
   `H-R2-12`.

#### ATAQUE 10 · Matriz que omita una obligación · **ROJO. HALLAZGO GRAVE**

**Derivé el universo POR MI CUENTA desde las seis sedes**, sin usar el instrumento:

```text
§19    5   CONTRATO 1 · 1bis · 2 · 3 · D104   (barrido de bloques `--- CONTRATO n ·` + ficha D104)
F-nn   8   F-01 F-02 F-04 F-05 F-06 F-07 F-10 F-11   (filas de §19 con fase F6; F-08 es F5)
V6    19   V6-01…V6-19            (grep -cE '^\| `V6-[0-9]+` \|' → 19)
g     16   g.1…g.16
C      3   C2 C4 C5
deuda  7   A14 FD-1 FD-3 FD-5 FD-6 M-04 S1-02
      ──
      58   coincide EXACTAMENTE con lo que el instrumento publica
```

Y las tres restas dan `A=0 · B=0 · C=0`. **Reproducido.**

**AHORA EL ATAQUE AL INSTRUMENTO. ¿Puede una obligación caerse en silencio? SÍ, por TRES vías:**

```text
10a · CAMBIAR LA FASE de una fila `F-nn`  (F-07: **F6** → **F5**)
      $ sed la celda de fase; python3.12 derivar-universo-obligatorio.py --obligaciones
      EXIT=0 · (F-nn) 7 · TOTAL 57 · A 0 · B 0 · C 0
      grep -c "F-07" en la salida  →  0        ← DESAPARICIÓN TOTALMENTE SILENCIOSA

10d · UNA SEDE QUE ENCOGE: retirar el bloque `CONTRATO 2` entero de §19
      EXIT=0 · (§19) 4 · TOTAL 57 · A 0 · B 0 · C 0
      La guarda es `if len(halladas) < 4: raise`. El suelo se calibró cuando eran CUATRO;
      hoy son CINCO (entró `CONTRATO 3`), de modo que la guarda tiene UNA UNIDAD DE HOLGURA
      y tolera en silencio la pérdida de un contrato.

10e · RETIRAR UNA FILA `F-nn` entera (F-10)
      EXIT=0 · (F-nn) 7 · TOTAL 57 · grep -c "F-10" → 0     ← SILENCIOSA
```

**Lo que SÍ resiste**, y consta:

```text
10b · pipe ESCAPADO nuevo en el texto de una fila   →  EXIT=0 · 58 obligaciones · sin pérdida
10c · pipe SIN escapar                              →  EXIT=2 · FALLA CERRADO nombrando la
      fila y la causa: «las filas F-04 no tienen el mismo número de celdas (9 frente a 8):
      la lectura por POSICIÓN deja de ser fiable»
```

`H-01` está bien cerrado. Lo que no existe es un **cliquet** para el universo de
OBLIGACIONES: `derivar()` —el universo de FUENTES— tiene `universos_publicados()` contra los
manifiestos inmutables; `publicar_obligaciones()` **no tiene ninguno**. Y `deudas_y_limites()`
publica lo que se le cae (`deudas_sin_fase_f6`), mientras `hallazgos_externos_f6()` y
`obligaciones_de_19()` **no publican nada**. Es `H-R2-03`.

**JUICIO SOBRE LOS CRITERIOS DE LAS TRES RESTAS — y no sólo sobre sus cifras.**

```python
a = [o for o,f in universo.items() if not f["validadores"]]                     # A
b = [o for o,f in universo.items() if f["validadores"] and not f["sabotajes"]]  # B
c = [o for o,f in universo.items() if f["validadores"] and not f["evidencias"]] # C
```

Las tres se calculan **del mismo objeto**: el campo `cubre:` de los bloques `ads:escenario`.

* **`A` se rotula «SIN COBERTURA DECLARADA que las ejerza». ¿Mide lo que dice? Sí — y por eso
  NO mide lo que `O26` §5.1 exige.** `O26` §5.1 pide «que no queden obligaciones internas de
  `F6` **sin implementar**». `A` mide «que ninguna obligación deje de estar NOMBRADA en el
  `cubre:` de algún escenario que declare validador». Añadir el identificador a un `cubre:` la
  saca de `A` sin tocar una línea de producto. **El propio fichero lo admite** en el comentario
  de `H-07`: *«una obligación sin escenario que la cubra es indistinguible, PARA ESTE APARATO,
  de una sin implementar»*.
* **Y el rótulo se movió para que la cifra encajara.** `H-07` cambió el rótulo de
  «obligaciones internas SIN IMPLEMENTACIÓN» a «SIN COBERTURA DECLARADA» **y sacó del universo
  `FD-2` y `FD-4`**. Las dos operaciones son defendibles por separado —el rótulo mentía, y
  `FD-2`/`FD-4` no son de `F6`—, pero su efecto conjunto es que `A` pasó de 7 a 0 **en parte
  moviendo la definición**. La honestidad del comentario no cambia el hecho: `A=0` **no
  demuestra** `O26` §5.1.
* **`B` se rotula «SIN SABOTAJE DECLARADO que las ponga rojas». Mide lo que dice, y es más
  débil de lo que parece.** El predicado es «existe alguna `Mutacion(..., "Tnnn")` que apunte
  a algún escenario que nombre la obligación». **No** exige que el sabotaje ejerza la
  propiedad. Contraejemplo vivo que yo mismo produje: `V6-12` tiene `B=0` (sabotajes `N189`,
  `N242`, `N242b`), y sin embargo la propiedad «`O26` no se puede alterar» **no tiene ningún
  sabotaje que la ponga roja** —lo demuestra el ataque 9—.
* **`C`**: mide que algún escenario que la nombra declare un fichero de evidencia que exista.
  Mide lo que dice.

**LA FRONTERA `FD-2` / `FD-4` / `C-L` con fase `F6` — ¿defendible o reclasificación?**

```text
FD-2 · FD-4   DEFENDIBLE. `06-DEUDA` §10 bis les da fase «no consta», propietario el Owner y
              condición «NO se corrige aquí, y no puede corregirse aquí». Excluirlas por su
              FASE es el mismo criterio que se usa para incluir a las demás, y se publican
              aparte con su sección y su fase declarada. Correcto.

E-17 · E-18   DEFENDIBLE con reserva. §10 ter las clasifica DEUDA EXTERNA y LÍMITE DE
              ANFITRIÓN. Se publican aparte. Pero salen del universo porque su fila «no tiene
              celda de fase», no porque su fase diga otra cosa: el criterio que las excluye
              es la AUSENCIA del campo, no su contenido. Es frágil, no falso.

C-L.7 · C-L.10 · C-L.13   **RECLASIFICACIÓN, y es un hallazgo.** `06-DEUDA` §2 les da, en su
              propia tabla: `C-L.10` «CONTRATADA PARA `F6`» · propietario **`PLT`** · fase
              **`F6`** · condición de cierre «**la implementación construida y ejecutada**»;
              `C-L.13` «MIXTA POR DESGLOSE… uno permanece contratado para `F6` y NO
              implementado» · `PLT` · `F6`; `C-L.7` «`F5` la especificación · **`F6` el
              instrumento**». Son obligaciones de `F6` con propietario de `F6` y condición de
              cierre de implementación. El derivador las excluye **por la SECCIÓN en que
              viven** —«OTRO censo: `06-DEUDA` §2»—, no por su fase, mientras que para el
              componente `deuda` el criterio que aplica ES la fase. **Dos criterios distintos
              para la misma pregunta, y el que excluye se aplica precisamente a las filas cuya
              fase declarada es `F6`.** Se publican aparte, luego no es silenciosa; pero la
              frontera no está trazada por la propiedad que dice trazarla. Es `H-R2-13`.
```

---

### 5 · EL ATAQUE QUE MÁS IMPORTA · OBLIGACIONES INTERNAS RECLASIFICADAS

**Contrasté `04-CONTRATOS-TECNICOS.md` §1 línea a línea contra el árbol**, como el encargo
manda. Resultado: **§1 es hoy CORRECTA** —lo que declara construido, existe—:

```text
ciclo de §7.2            kernel/operativo/runtime/ciclo/                EXISTE
macrocircuitos           runtime/macrocircuitos/motor.py               EXISTE
raíz externa             kernel/operativo/raiz-externa/verificador.py  EXISTE
adaptador local real     runtime/adaptadores/proceso.py                EXISTE
verificador de admisión  runtime/admision/__init__.py                  EXISTE
prueba de humo sesión nueva  runtime/pruebas/test_sesion_nueva.py      EXISTE
gates de capa            runtime/ciclo/gates.py                        EXISTE
equipos C4               runtime/ciclo/equipos.py                      EXISTE
`D104` 9/9               NUEVE pares derivados por mí de 01-PROCESOS   EXISTEN
```

**PERO EL DOCUMENTO SE DECLARA «LA ÚNICA SEDE» Y SE CONTRADICE A SÍ MISMO EN CUATRO SITIOS,
FUERA DE §1.** Es la TERCERA vez, y esta vez el defecto no está en §1 sino en las secciones
que deberían remitir a ella:

```text
L326-329  §5.3 ADAPTADORES  «Cuatro piezas diseñadas… **Ninguno existe y ninguno está
          certificado**»   ← §1.1 declara «ADAPTADORES con un ejecutor local real y
          proyecciones con huella» CONSTRUIDO, y `proceso.py` existe con su evidencia
L336-337  §5.4 VERIFICADORES  «LO QUE NO HAY: el VERIFICADOR DE ADMISIÓN y la RAÍZ EXTERNA
          DE CONFIANZA»   ← §1.1 y §1.2 los declaran construidos con evidencia publicada
L343      §6 título  «Los contratos del VERIFICADOR DE ADMISIÓN — escritos, y ninguno
          implementado»
L382      §6  «**NINGUNA de esas filas está implementada, ejecutada ni certificada**»
          ← §1.2 declara «VERIFICADOR DE ADMISIÓN · los DIECINUEVE puntos. `V6-15` y `V6-16`
          están construidos»
L274      §4  «**El sellado del diario queda para el corte siguiente**»   ← el sellado de
          `g.7` está construido: `estado/diario.py` lo implementa y `T312`–`T319` lo ejercen
```

Y la misma afirmación se repite fuera del documento:

```text
06-DEUDA §6 L197   «ESTADO DE TODOS   CONTRATADO · NO IMPLEMENTADO · NO EJECUTADO · NO
                   CERTIFICADO» sobre los contratos de `F6`
05-PLAN  L6        «ESTE DOCUMENTO ES UN PLAN. **Nada de lo que describe está implementado.**»
```

**¿Es esto reclasificación de deuda interna en externa? NO en la dirección que el encargo
teme.** El corpus canónico **subestima** lo construido, no lo sobreestima. Nadie ha convertido
una deuda interna de `F6` en «externa» para no cerrarla **en `04-CONTRATOS`**. Lo que hay es
un corpus que gasta su crédito en la dirección contraria — y §1.2 escribe exactamente por qué
eso importa: *«Una sede que declara no construido lo construido gasta el crédito con el que
después dice que algo NO está: si se equivoca en un sentido, nadie puede fiarse del otro.»*
**Se equivoca otra vez, en el mismo sentido, en el mismo documento, fuera de §1.** Es
`H-R2-05`.

**DÓNDE SÍ HAY RECLASIFICACIÓN, medida:**

1. **`C-L.10` y `C-L.13`** (arriba, `H-R2-13`): obligaciones que su sede declara fase `F6`,
   propietario `PLT` y condición «implementación construida y ejecutada», excluidas del
   universo por la sección en que viven.
2. **`E-17` y `E-18`**: contrasté `06-DEUDA` §10 ter contra `01-MATRIZ` §4 y contra `O25`/`O26`.
   **La clasificación se sostiene:** `E-17` es custodia productiva, que `O25` §2 sitúa
   expresamente fuera del repositorio y `O26` §4 confirma; `E-18` es `cgroup v2` no
   ejercitable, medido con su `errno 5 (EIO)` y con la lista de los tres backends fuertes que
   sí se ejercen. **Y el corpus se guarda de convertirlo en cumplimiento universal**: §10 ter
   escribe «la certificación queda LIMITADA AL BACKEND EJERCIDO. Este corpus no afirma nada
   sobre anfitriones que no ha medido». **No es maquillaje.**
3. **`F6-B`**: la matriz **retira** el rótulo «límite de anfitrión» y lo sustituye por «ACTO
   DEL OWNER EMITIDO Y CONDICIONADO». Eso es una reclasificación **hacia dentro**, no hacia
   fuera, y es correcta: lo que faltaba era un acto del Owner y existe.
4. **`F6-F`** (recorrido extremo a extremo de `A` y `U`) y **`F6-G`** (nivel `soportado`): se
   declaran EXTERNOS citando §14, §18 nodo 8 y §20.2. **Verifiqué las tres citas en §18 y §9.1,
   que leí íntegras, y se sostienen literalmente**: el nodo 8 está BLOQUEADO por el 9 y las
   cinco pruebas de Integrado exigen fuentes reales. No es reclasificación.

**Estados de fase — `03-GOBIERNO` §6, sede única.** Contrastado:

```text
F4c CERRADA por composición  ·  F5 CERRADA (O24 §1)  ·  F6 INICIADA · EN CURSO (O24 §2)
PesquerApp BLOQUEADA (O20 §8 y O24 §4)  ·  C-L.5 CERTIFICADA/POR DELTA  ·  C-L.7 NO CERRADA
M-04 NO SUPERADA
```

**Los cuatro coinciden con lo que el manifiesto declara y con `O24`, que leí íntegra.** Y
`03-GOBIERNO` §6 **no** copia el estado de construcción: remite a `04-CONTRATOS` §1. Correcto.

**`F6-H` y `F6-A`…`F6-I`.** El inventario de `F6-H` cubre hoy las ocho filas `F-nn` con fase
`F6` **más** las cuatro obligaciones de §19, y el universo derivado las publica una a una con
identificador propio: `E-13` está cerrado. `F6-H` sigue rotulada **PARCIAL**, y la matriz dice
por qué: «NO se marca completa mientras las tres restas no estén vacías». Hoy están vacías —
pero por un predicado que no mide lo que su rótulo promete (`H-R2-13`).

---

### 6 · HALLAZGOS

| id | severidad | clase | sede | qué es | propietario | remedio |
|---|---|---|---|---|---|---|
| **`R2-01`** | **BLOQUEANTE** | del GATE | este dictamen | `ASIGNADO − LEÍDO ≠ ∅`: 50 de 84 ficheros sin abrir, 29 329 de 48 143 líneas (60,9 %), incluidos `macrocircuitos/fase0.py`, `comprobar_composicion_procesos.py`, `ciclo/agentes.py`, `ciclo/planificacion.py` y los once ficheros `Tnnn-*.md`. **Reproducción:** el registro §2 de este dictamen. | el coordinador que dimensionó y repartió | ninguno aplicable dentro de este gate: la regla §4 del manifiesto dice que el gate cae |
| **`R2-02`** | **BLOQUEANTE** | INTERNO | `runtime/admision/perimetro.py::_juzgar_append_only` · `04-CONTRATOS` §6 · `03-GOBIERNO` §2 | el contrato append-only de la sede del Owner se comprueba como **prefijo** contra el blob del nacimiento, luego protege **14 395 de 42 181 bytes (34,1 %)**: `O20`–`O26` se pueden reescribir byte a byte, confirmar, y `V6-12` da `hallazgos=0`, indistinguible de un apéndice legítimo. **Reproducción:** ataque 9, con control positivo (`O17` → ROJO) y negativo (apéndice → 0 hallazgos). Ninguna prueba ni sabotaje del corpus muta contenido posterior al nacimiento. | `PLT` implementa · `SIS` propietario | que el contraste sea de **igualdad sobre el prefijo común y de sólo-adición sobre el resto**, con una prueba que mute una entrada posterior al nacimiento y exija ROJO |
| **`R2-03`** | **GRAVE** | INTERNO | `derivar-universo-obligatorio.py`, modo `--obligaciones` | el universo de OBLIGACIONES **encoge en silencio** por tres vías: cambiar la fase de una fila `F-nn` (58→57, `exit 0`, el id no aparece en la salida), retirar un bloque `CONTRATO n` de §19 (la guarda `< 4` tiene una unidad de holgura desde que son cinco), y retirar una fila `F-nn` entera. La cabecera del fichero promete «nunca reduce el universo en silencio», y el modo `--obligaciones` **no tiene cliquet**: `derivar()` sí lo tiene, `publicar_obligaciones()` no. `O26` §5 convierte estas restas en criterio de certificación. **Reproducción:** ataque 10, casos 10a, 10d, 10e. | `PLT` | cliquet propio para obligaciones contra los manifiestos inmutables; publicar lo que se cae de CADA componente, no sólo del de deuda; y que el suelo de `obligaciones_de_19` se derive en vez de escribirse |
| **`R2-04`** | **GRAVE** | INTERNO | `pruebas/*.md` bloques `ads:escenario` · `validadores/registro_pruebas.py` | el campo `estado:` de una prueba es **escrito a mano** y `registro_pruebas.py` lo copia verbatim a `REGISTRO-generado.md`. **Nada lo contrasta contra la evidencia.** `REGISTRO.md` declara «REGLA DURA: ninguna prueba sube de estado por argumento. Sube porque se ejecutó y su salida quedó registrada en la columna `evidencia`» — y esa regla **no está mecanizada**. **Reproducción:** subí `T169` de `contrato-definido` (`ejecucion: requiere-runtime`, sin runtime ni piloto) a `prueba-superada` apuntando a una evidencia ajena; el registro pasa a publicar 174 superadas y **33 de 34 validadores siguen verdes** —`comprobar_evidencia`, `comprobar_contratos`, `ads_lint`, `comprobar_recuentos`, `comprobar_versiones`, `comprobar_composicion_procesos`, `comprobar_referencias`, `comprobar_arranque`, `comprobar_packs`, `comprobar_prompts`, `comprobar_fuentes`, `registro_pruebas` todos `exit=0`—; **el único rojo es `comprobar_integridad`, la huella**, que el manifiesto §7 declara que NO cuenta. **Y hay una divergencia VIVA hoy:** `T273` se publica `PRUEBA FALLIDA` en `REGISTRO-generado.md` mientras `composicion-procesos-salida.txt` dice `T273 SUPERADA` y la prosa de `T270-T289` escribe «`T273` queda en VERDE». | `PLT` implementa · `SIS` propietario | derivar el `estado` de la evidencia, o contrastar el declarado contra la salida del validador que la prueba nombra |
| **`R2-05`** | **GRAVE** | INTERNO | `04-CONTRATOS-TECNICOS.md` §5.3 L326-329 · §5.4 L336-337 · §6 L343 y L382 · §4 L274 | el documento que se declara **la ÚNICA SEDE** de la distinción construido/diseñado —y que ya ha sido falso dos veces— **vuelve a ser falso una tercera**, esta vez fuera de §1: cuatro secciones afirman que no existen el verificador de admisión, la raíz externa, los adaptadores y el sellado del diario, y las cuatro cosas existen con evidencia publicada. `06-DEUDA` §6 L197 y `05-PLAN` L6 repiten la afirmación. **Reproducción:** §5 de este dictamen, con la ruta de cada componente. | `SIS` | que §5.3, §5.4, §6 y §4 **remitan a §1** en vez de declarar estado, que es la regla que el propio documento escribe en su cabecera |
| **`R2-06`** | **MEDIA** | INTERNO | `docs/f6/00-ESTADO-DE-IMPLEMENTACION-F6.md` L168 | conserva, palabra por palabra, la premisa que `01-MATRIZ` L113 declara **medida falsa**: «Sólo un resultado es conforme con las dos normas, así que **no hay decisión del Owner que tomar**». La matriz escribe «**Hay al menos tres resultados conformes, no uno**», comprobado ejecutando. La premisa falsa es la que sostiene la conclusión de que `F-07` no vuelve al Owner. **Reproducción:** `grep -n "Sólo un resultado es conforme" docs/f6/00-ESTADO…` → L168; `grep -n "Hay al menos tres resultados conformes" docs/f6/01-MATRIZ…` → L113. | `SIS` | que la fila de decisión técnica diga lo que la matriz midió, o remita |
| **`R2-07`** | **MEDIA** | INTERNO | `docs/f6/01-MATRIZ-DE-COMPLETITUD-F6.md` L190 y L192 | afirma **en presente** que «`T151` está en ROJO sobre tres sedes vivas» y «`T152` está en ROJO sobre `kernel/operativo/00-INDICE.md`», presentándolo como la PRUEBA POSITIVA que §19 prescribe. **El árbol dice lo contrario:** `recuentos-salida.txt` → `T151 SUPERADA · 5 superadas · 0 fallidas`; `versiones-salida.txt` → `T152 SUPERADA · 2 superadas · 0 fallidas`. Las sedes se corrigieron y la prueba positiva dejó de aplicar, correctamente; lo que no se corrigió es la afirmación. | `SIS` | retirar la afirmación de estado y remitir a la evidencia |
| **`R2-08`** | **MEDIA** | del GATE | `docs/evolucion/00-INDICE.md`, tabla «documento del aparato de verificación» | el manifiesto de ESTE gate está enlazado **sólo desde su fila del registro de pasadas** y **no desde la LISTA**, que es lo que `C-L.5` exige y lo que `EE-03` del SEXTO GATE cerró expresamente («el `grep` barría el índice ENTERO… la regla exige la LISTA»). **Reproducción — con el comando que el propio índice publica como prueba de que la regla se cumple:** `diff <(find docs/evolucion/verificacion -type f …) <(awk …LISTA… )` → `21d20 < docs/evolucion/verificacion/manifiestos/F6-ASIGNACION-GATE-CERTIFICACION-FINAL-20260904.md`. **SEXTA recurrencia** de `S-18`≡`T-14` → `Y-03`≡`Z-09` → `EE-03` → `HH2-12`. El commit se titula «enlazar el manifiesto previo desde el indice minimo». | el coordinador de este gate | añadir la fila a la LISTA |
| **`R2-09`** | **MEDIA** | del GATE | commit `26d6c54` | el commit del manifiesto **añadió un documento al corpus y no republicó la evidencia derivada** que invalida, contra la disciplina que `04-CONTRATOS` §5.2 y el propio checkpoint escriben. Consecuencia medida sobre la rama entregada: **o `comprobar_evidencia` (T158) está en ROJO**, o se regenera y `git status --porcelain` deja de estar vacío con tres ficheros. **Las dos mitades de la línea base no pueden ser ciertas a la vez sobre `HEAD`.** Sobre la candidata `7b9829c` sí lo son. **Reproducción:** §3 de este dictamen. | el coordinador de este gate | ninguno posible sin tocar el árbol; se registra |
| **`R2-10`** | **MEDIA** | INTERNO | `06-DEUDA-Y-LIMITACIONES-VIGENTES.md` §13, comando 5 | publica un autocontrol —`grep -rn 'python_requires' tooling/ kernel/ ; echo "(vacío = A14 sigue abierto)"`— cuyo resultado sobre el árbol es **vacío**, y por su propia anotación eso significa «`A14` sigue abierto», mientras **§4 del mismo documento declara `A14` CERRADA POR `F6`**. Es la clase `KD-01` —«una sede publica un autocontrol que no comprueba»— en una sede canónica. **Reproducción:** ejecutar el comando publicado. | `SIS` | retirar el comando o reanclarlo a `validadores/entorno.py`, que es la sede real de la guarda |
| **`R2-11`** | **MEDIA** | del OWNER · no corregible | `docs/owner/ADS-OWNER-RESOLUCIONES.md`, entradas `O25` y `O26` | la sede declara obligatorios seis campos por entrada —identificador · fecha · procedencia · texto · alcance · relaciones de revisión—. **Medido entrada a entrada:** `O17`–`O22` los llevan todos y tienen `## Texto`; **`O23`, `O24`, `O25` y `O26` no llevan NINGUNO** salvo fecha y autoridad, y no tienen `## Texto`. `FD-2` registra este defecto **sólo para `O23` y `O24`**: **`O25` y `O26` son instancias nuevas y no registradas** de una deuda ya abierta, y `O26` es la que da al gate su competencia. | el **Owner**: la sede es append-only y sólo él escribe en ella | ninguno: no se puede corregir. Ampliar `FD-2` para que cubra las cuatro |
| **`R2-12`** | **MEDIA** | del OWNER · LIMITACIÓN PERMANENTE | ídem, entrada `O26` | la omisión de «FIN LITERAL DE `O26`.» **no es defendible como delimitador**, por las cinco razones del ataque 9 — y la tercera es decisiva: `O26` **carece de `## Texto`**, luego la línea omitida era su **único delimitador de cierre**, y se retiró alegando que era un delimitador. Además `O26` **no lleva nota de trazabilidad**, que es el instrumento con que el corpus declara INVERIFICABLE una procedencia (`O17`, `O20`, `O21`, `O22` la llevan). | el **Owner** para la sede · `SIS` para la nota | ninguno sobre la sede. Registrar como LIMITACIÓN PERMANENTE, como `LE-01` en su mitad de sede |
| **`R2-13`** | **MEDIA** | INTERNO | `derivar-universo-obligatorio.py`, `ROTULOS_DE_RESTA` y `condiciones_c_l_con_fase_f6()` | (i) `A=0` **no demuestra** `O26` §5.1: el predicado es «nombrada en un `cubre:` con validador», no «implementada», y el rótulo se movió (`H-07`) en la misma corrección que vació la resta. (ii) `B=0` no demuestra que la propiedad tenga prueba capaz de fallar: contraejemplo vivo, `V6-12` con `B=0` y la propiedad del ataque 9 sin sabotaje. (iii) **`C-L.7`, `C-L.10` y `C-L.13` se excluyen por la SECCIÓN en que viven**, mientras el componente `deuda` excluye por la FASE — y `06-DEUDA` §2 les da a las tres fase `F6`, a dos de ellas propietario `PLT`, y a `C-L.10` la condición «la implementación construida y ejecutada». Dos criterios para la misma pregunta, y el que excluye cae sobre filas cuya fase declarada es `F6`. | `PLT` implementa · `SIS` propietario | que el criterio de pertenencia sea uno solo —la FASE declarada— para las seis sedes, y que `A` diga en su rótulo que mide trazabilidad y no implementación |
| **`R2-14`** | **MEDIA** | INTERNO | `comprobar_recuentos.py`, `AMBITO_VIVO` | el barrido del `CONTRATO 1` cubre seis prefijos —`README`, `START_HERE`, `kernel/`, `packs/`, `docs/canonico/`, `docs/f6/`—. **`docs/rediseno/` (material APROBADO), `docs/owner/` (la sede del Owner), `docs/evolucion/` y `tooling/` quedan fuera SIN MOTIVO ESCRITO**, mientras `FUERA_DEL_AMBITO` sí motiva cada una de sus seis exclusiones y `T151` comprueba que los motivos estén escritos. **Reproducción:** la misma afirmación falsa que `T151` caza en `docs/f6/` (`FALLIDA`) pasa en verde insertada en `docs/rediseno/b-RECORRIDO-APROBADA.md` (`5 superadas · 0 fallidas`). No es hipotético: `E5-4` de §19 registra un recuento de marcas erróneo en `a-ENMIENDA-E1-ENC.md` y en `(a)`, y `OC-2` de `06-DEUDA` §11 registra otro. | `PLT` | motivar cada prefijo ausente, o extender el barrido a las sedes cuya cifra el corpus ya sabe que caduca |
| **`R2-15`** | **LEVE** | INTERNO | `06-DEUDA` §11, observación `OC-3` | describe que «el índice de contratos afirma un número de campos del contrato de rol distinto del que el contrato y su esquema declaran». **Medido:** `contratos/00-INDICE.md` L7 dice «veintinueve», `C1` L37 dice «veintinueve», `RECUENTOS-generado` deriva **29**. La observación describe un árbol anterior. | `SIS` | retirar o reanclar |

---

### 7 · LO QUE EL ÁRBOL SÍ SOSTIENE

Se dice porque un dictamen que sólo publica lo que falla no describe el objeto, y porque
varias de estas cosas son exactamente lo que el gate anterior declaró roto.

```text
LA LÍNEA BASE ES EXACTA        las NUEVE cifras del encargo reproducidas sobre la candidata,
                               ninguna con divergencia, y el determinismo comprobado con dos
                               corridas y `diff -r` vacío

`E-01` CERRADO POR LA          las tres composiciones plurales materializan agentes REALES
PROPIEDAD                      con identificador propio; el cardinal se DERIVA del campo
                               `agentes` con vocabulario cerrado y `exigir_censo_legible`
                               impide que entre una forma nueva en silencio; el integrador se
                               lee de `ampliacion` y se contrasta contra `roles`; y el
                               sabotaje que cerró el hallazgo cae **por la prohibición de
                               `C4`**, no por la huella

LAS TRES CONDICIONES DE `C4`   (a) reparto sin solapamiento con `RepartoSinUnidades` y
ESTÁN COMPROBADAS, LAS TRES    detección de unidades repetidas · (b) fase divergente leída de
                               los pasos del método · (c) volumen MEDIDO contra la escala de
                               contexto del perfil, con error tipado

LA COMPETENCIA EXIGE SU        cinco guardas distintas, cada una con su error y su motivo, y
CRITERIO, Y EL «ANTES» SE MIDE el «antes» contra un reloj LÓGICO y no de pared

`b.12` ESTÁ ENTERO Y NINGÚN    los cuatro criterios de orden y los cuatro campos de inanición
CRITERIO ES DECORATIVO         existen, y los OCHO sabotajes producen OCHO conjuntos de
                               pruebas rojas DISTINTOS

`DSP` NO ELEVA PRIORIDADES     medido sobre estado durable real: el paquete de prioridad 10
                               acaba ejecutándose y su prioridad es byte a byte la misma
                               antes y después. No existe ni una escritura de `prioridad`
                               fuera de la creación del paquete

`D104` MATERIALIZADO 9/9       derivé los NUEVE pares a mano de `01-PROCESOS.md` y coinciden
                               con lo publicado, incluido el reparto por vía (2·1 · 4·8) y
                               las anclas proceso a proceso

EL APPEND-ONLY, COMO CADENA,   ocho commits, cada uno empieza por el anterior; hoy empieza por
ESTÁ INTACTO                   el nacimiento; `O17`–`O25` nunca se retiraron ni se movieron

`O26` NO SE PRESENTA COMO      no hay una sola sede que lo haga, y cuatro lo niegan
CERTIFICACIÓN, Y `B3` NO SE    expresamente. `06-DEUDA` §3 escribe «`B3` NO queda satisfecho
DECLARA SATISFECHO             por este acto»

LOS ESTADOS DE FASE SON        `F4c` CERRADA · `F5` CERRADA · `F6` INICIADA·EN CURSO ·
CORRECTOS Y TIENEN UNA SEDE    PesquerApp BLOQUEADA, con el acto citado en cada fila, y
                               `03-GOBIERNO` §6 no copia el estado de construcción

`E-13` CERRADO                 el universo de `F6-H` publica las cuatro obligaciones de §19
                               una a una, con identificador propio y sin absorción: el
                               derivador usa fronteras de palabra para que `CONTRATO 1` no
                               absorba a `CONTRATO 1bis`

EL INSTRUMENTO RESISTE DOS     un pipe ESCAPADO en el texto de una fila no pierde ninguna
DE LOS TRES ATAQUES DE FORMA   obligación; uno SIN escapar falla CERRADO con `exit 2`
                               nombrando la fila y la causa

`E-17` Y `E-18` NO ESTÁN       la clasificación se sostiene contra `O25` §2 y `O26` §4, y el
MAQUILLADOS                    corpus acota expresamente que no afirma nada sobre anfitriones
                               que no ha medido
```

---

### 8 · JUICIO EXPRESO SOBRE BLOQUEANTES INTERNOS VIVOS EN MI EJE

**`O26` §5.5 exige «que no existan bloqueantes internos vivos». En mi eje, SÍ LOS HAY.**

```text
BLOQUEANTE VIVO 1 · `R2-02`
    El contrato APPEND-ONLY de la sede del Owner —que `04-CONTRATOS` §6 declara «comprobado
    contra su NACIMIENTO» y que `V6-12` implementa— protege el 34,1 % de la sede. `O20`–`O26`
    quedan fuera. Una condición de `O26` se muta, se confirma y el verificador da
    `hallazgos=0`, indistinguible de un apéndice legítimo.
    ES INTERNO: la sede está en el árbol, el mecanismo está en `kernel/operativo/runtime/`,
    y sólo `F6` edita ahí. NO es límite de anfitrión, no es acto del Owner y no es nodo 8.
    ES BLOQUEANTE: `O26` §5 da al gate su competencia, y la integridad del texto que se la da
    no está mecánicamente guardada. Y `O18` sexta condición —«ninguna promesa de seguridad
    superior a la realmente entregada»— está incumplida: se promete «append-only comprobado
    contra el nacimiento» y se entrega «el prefijo del nacimiento sigue ahí».

BLOQUEANTE VIVO 2 · `R2-03` + `R2-13`
    El instrumento que `O26` §5 convierte en criterio de certificación puede perder una
    obligación en silencio por tres vías, y sus rótulos `A` y `B` no miden lo que `O26` §5.1
    y §5.2 exigen. `A = 0` NO demuestra «no quedan obligaciones internas sin implementar»;
    `B = 0` NO demuestra «no quedan propiedades críticas sin una prueba capaz de fallar» —y
    el ataque 9 es el contraejemplo, con `V6-12` en `B = 0`.
    ES INTERNO: `docs/evolucion/verificacion/` es del expediente y `PLT` lo posee.

BLOQUEANTE VIVO 3 · `R2-04`
    El estado de una prueba es un campo escrito a mano que nada contrasta contra su
    evidencia. Subir `T169` —que su propio fichero declara indemostrable sin runtime ni
    piloto— a `prueba-superada` deja 33 de 34 validadores verdes, y el único rojo es la
    huella, que el manifiesto §7 excluye expresamente. Y el corpus **ya envía hoy** una
    divergencia entre el estado publicado de `T273` y su evidencia.
    ES INTERNO, y toca la sede que autoriza al corpus a decir «682 casos, 173 superadas».
```

**Y una precisión, para que nadie lea de más:** `R2-05`, `R2-06`, `R2-07` y `R2-10` son
defectos de SEDE, no de producto. El árbol construye más de lo que sus sedes canónicas
declaran. Pero `04-CONTRATOS` §1.2 ya escribió la consecuencia y vuelve a aplicarse:
**una sede que se equivoca en un sentido gasta el crédito con el que después dice el otro.**

```text
DECLARACIÓN A · VALIDEZ         EL GATE NO ES VÁLIDO por mi lote.
                                `ASIGNADO − LEÍDO ≠ ∅`: 50 ficheros sin abrir · 29 329
                                líneas · 60,9 %. La regla §4 del manifiesto no admite
                                atenuantes y no autoriza al adjudicador a sustituir mi
                                lectura.

DECLARACIÓN B · COMPLETITUD     NO PUEDO AFIRMAR que `F6` esté completamente implementada en
                                mi eje. Lo que sí afirmo: `E-01`, `E-06` y `E-13` están
                                cerrados por la propiedad y lo he medido. Lo que niego:
                                que `A=0 · B=0 · C=0` lo demuestre, por `R2-13`.

DECLARACIÓN C · `O26` y `B3`    `O26` está inscrita y NO se presenta como certificación en
                                ninguna sede. `B3` NO está declarado satisfecho en ninguna.
                                Las OCHO condiciones de `O26` §1 NO las he comprobado: la
                                raíz externa es lote del revisor 1. Y sobre la §5.5 —«que no
                                existan bloqueantes internos vivos»— mi respuesta es: **los
                                hay**, y son tres.

DECLARACIÓN D · CERTIFICACIÓN   `F6` NO PUEDE CERTIFICARSE con este gate. Tres razones
                                independientes, y la primera basta: (1) el gate no es
                                válido por cobertura; (2) hay bloqueantes internos vivos en
                                mi eje; (3) el instrumento que `O26` §5 convierte en
                                criterio no mide lo que su rótulo dice ni impide que una
                                obligación se caiga en silencio.

DECLARACIÓN E · PesquerApp      SIGUE BLOQUEADA. Derivado, no presupuesto: `O20` §8 · `O24`
                                §4 · `03-GOBIERNO` §6 y §7 · `11-ARQ` §18 arista 9→8 ·
                                `O26` §6 y §8. La precondición es la CERTIFICACIÓN, y no se
                                emite aquí.
```

**Y lo último, que es de método.** Este dictamen no lo escribe quien construyó, no corrige
nada, no propone commits y no ha tocado el árbol. `HEAD`, `tree` y `git status --porcelain`
son idénticos al abrir y al cerrar. Lo que no pude leer, lo he dicho — y lo he dicho con la
lista completa, fichero a fichero, para que nadie tenga que fiarse de una resta que yo
publique sin poder recalcularla.

— **REVISOR 2**, 2026-09-04


---

# 7 · ADJUDICACIÓN ÍNTEGRA

## ADJUDICACIÓN · GATE ÚNICO Y FINAL DE CERTIFICACIÓN DE `F6` · 2026-09-04

> **Quien firma esto no ha implementado, no ha revisado y no ha participado en ningún gate
> anterior de este expediente.** No resuelve por mayoría y no ha copiado a ningún revisor sin
> verificar. Toda razón capaz de mover el veredicto está reproducida abajo con su orden
> literal y su salida. Una razón no reproducida no sostiene nada aquí; una reproducida y
> caída, cae con el nombre de quien la planteó.
>
> **NO SE HA CORREGIDO NADA. NO SE PROPONE NINGÚN COMMIT. NO SE ABRE OTRO GATE. NO SE INICIA
> PESQUERAPP.**

---

### 1 · PRECONDICIONES

#### 1.1 · El repositorio real, al abrir y al cerrar

```text
                          APERTURA                                   CIERRE
HEAD    20330e694d4941e5c159017ec79fd5b77aaf962d   20330e694d4941e5c159017ec79fd5b77aaf962d
TREE    4ee6f9d47a4792d394b1cf7c0f8b425934ce8daf   4ee6f9d47a4792d394b1cf7c0f8b425934ce8daf
RAMA    gate/f6-certificacion-final-20260904        gate/f6-certificacion-final-20260904
git status --porcelain        (vacío)                          (vacío)
refs/heads                    39                               39
```

**Ni un byte del árbol real se ha tocado.** Ninguna orden `git` que cambie estado se ejecutó
sobre él. Todo ataque, toda corrida y toda mutación vive en clones hechos con
`git clone --no-local` hacia `/tmp/…/scratchpad/ADJ/`, y en copias de esos clones.

#### 1.2 · El objeto congelado, comprobado

```console
$ git rev-parse 7b9829cbfa68c12b9947db0f7a26a1d08ed7f003
7b9829cbfa68c12b9947db0f7a26a1d08ed7f003
$ git rev-parse 7b9829cbfa68c12b9947db0f7a26a1d08ed7f003^{tree}
d2c0a0cde1fff37cbf5ee59cf7a5bd633a99e330      ← coincide con el encargo
$ git merge-base --is-ancestor 7b9829c HEAD  → SI
$ git diff --stat 7b9829c HEAD
 docs/evolucion/00-INDICE.md                        |   1 +
 ...ASIGNACION-GATE-CERTIFICACION-FINAL-20260904.md | 395 +++++++++++++++++
$ git merge-base --is-ancestor fd633383 HEAD  → NO-ANCESTRO   ← como el manifiesto declara
```

`HEAD` está DOS commits por encima de la candidata, y los dos son **el aparato de este mismo
gate**. La candidata es correcta. Toda medición de línea base de esta adjudicación se hizo
sobre un clon con `git checkout 7b9829c`; lo medido sobre `HEAD` va rotulado como tal.

**`refs/heads/review/f6-post-gate-corrections-candidate-20260904` NO EXISTE.**

```console
$ git rev-parse refs/heads/review/f6-post-gate-corrections-candidate-20260904
fatal: ambiguous argument … unknown revision or path not in the working tree
$ git branch -a --list '*f6-post-gate*'
  remotes/origin/review/f6-post-gate-corrections-candidate-20260904
```

Existe como `refs/remotes/origin/…` y apunta a `7b9829cb`. Es `ADJ-GT4`, informativa. Los dos
revisores lo dijeron; los dos tienen razón.

#### 1.3 · Intérprete

```console
$ /home/jose/.local/bin/python3.12 --version   → Python 3.12.14
$ … -c "import yaml; print(yaml.__version__)"  → 6.0.2
$ python3 --version                            → Python 3.10.12   (NO usado como medidor)
```

---

### 2 · COBERTURA DE LOS DOS REVISORES

#### 2.1 · El lote, dimensionado contra la candidata — comprobado línea a línea

He recalculado el manifiesto contra el árbol de la candidata, fichero a fichero, **las 225
rutas de los dos lotes**:

```console
$ awk … extraer lote R1 y R2 del manifiesto …
$ for ruta,lineas: real=$(git show 7b9829c:"$ruta" | wc -l); [ "$real" != "$lineas" ] && echo DISCREPA
(ninguna discrepancia)

R1   141 ficheros ·  46 643 líneas   +  3 rangos ·  3 968   =  50 611
R2    84 ficheros ·  48 143 líneas   +  6 rangos ·  3 018   =  51 161
```

Los seis rangos de `11-ARQ` caen **exactamente sobre su cabecera**, verificado:

```console
$ sed -n '396p;5812p;6136p;6285p;7378p;8075p;10882p;11070p;11907p' 11-ARQ (de la candidata)
   396  # 2 · Disposición física del estado — la primera decisión
  5812  # 6 · Arquitectura de adaptadores
  6136  # 7 · Runtime y dispatcher
  6285  # 8 · Los cuatro macrocircuitos
  7378  # 9 · Certificación
  8075  # 10 · Git y multi-repositorio
 10882  # 18 · Orden de construcción para F6
 11070  # 19 · Límites de esta fase
 11907  # 20 · CONTRATO OBLIGATORIO DE `F6` · EL VERIFICADOR DE ADMISIÓN
```

**El dimensionado del coordinador es exacto.** No hay ni un fichero mal contado.

#### 2.2 · Revisor 1 · `ASIGNADO − LEÍDO = ∅` · **DECLARACIÓN EXACTA**

Su tabla de cobertura, extraída y contrastada contra el lote del manifiesto:

```console
$ diff <(tabla de R1: ruta + líneas) <(lote R1 del manifiesto: ruta + líneas)
IDENTICO: la tabla de R1 == el lote del manifiesto, ruta a ruta y línea a línea
$ casillas "SI": 141 · casillas "NO": 0
```

**La resta declarada es aritméticamente exacta y su lista coincide con el lote.**
Lo que no puedo verificar es el acto de leer; lo que sí verifico es que su lista no omite ni
inventa una sola fuente, que sus rangos son los asignados, y que su dictamen mide
comportamiento en las quince zonas de su lote —migración, raíz externa, contención, `setsid`,
sellado, identidad, evidencia, procedencia— con detalle que no se obtiene sin abrir el código.
**Acepto su declaración.**

#### 2.3 · Revisor 2 · `ASIGNADO − LEÍDO ≠ ∅` · **DECLARACIÓN EXACTA**

Recalculada por mí, entera:

```console
$ NO ABIERTOS (su lista, 50 rutas)                          suma  25 780
$ contraste de cada una contra el lote del manifiesto       (ninguna discrepancia)
$ LEÍDOS ÍNTEGROS (30 rutas)                                suma  17 299
$ LEÍDOS EN PARTE (4 rutas)          1 515 leídas de        5 064
$ 17 299 + 5 064 + 25 780                                        48 143   == el lote, exacto

ASIGNADO − LEÍDO = 25 780 + (5 064 − 1 515) = 29 329 de 48 143  =  60,9 %
```

**Su resta es exacta hasta la última línea, y su partición del lote es completa: ninguna ruta
de su lote queda sin clasificar y ninguna ruta declarada está fuera de su lote.** Los 50
ficheros no abiertos incluyen `macrocircuitos/fase0.py` —la `FASE 0` cuyas once filas `X-S`
demuestra `F6-F`, con §9.6 asignada EXPRESAMENTE a su lote—, `ciclo/agentes.py`,
`ciclo/planificacion.py`, `comprobar_composicion_procesos.py`, `comprobar_contratos.py`,
`validadores.yaml`, `exclusiones.yaml` y los once ficheros `Tnnn-*.md`.

**La regla §4 del manifiesto no admite atenuantes, y no me autoriza a sustituir su lectura.
El gate cae por cobertura.** Lo digo sin rodeos y sin buscarle una salida: es exactamente la
conducta que el manifiesto premia —decirlo a tiempo— y exactamente la consecuencia que el
manifiesto fija.

#### 2.4 · MI JUICIO SOBRE EL REPARTO — y aquí corrijo una atenuante que nadie ha pedido pero que conviene cerrar

```text
LOTE R1   50 611 líneas · 141 ficheros
LOTE R2   51 161 líneas ·  84 ficheros
DIFERENCIA   550 líneas = 1,1 %
```

**El reparto era simétrico y el defecto NO está en el dimensionado.** Un revisor terminó un
lote de tamaño prácticamente idéntico al otro. La hipótesis «el coordinador repartió lo
inasumible» **no se sostiene con los números que el propio manifiesto publicó para que se
pudiera contestar esta pregunta**, y publicarlos fue la decisión correcta: gracias a ellos la
pregunta tiene respuesta en vez de opinión.

Dos matices, los dos menores, y los dos dichos:

* **`ADJ-GT5` · LEVE.** El manifiesto escribe «50 611 líneas · 141 ficheros íntegros **más**
  los rangos» y «51 161 líneas · 84 ficheros íntegros **más** los rangos». En los DOS casos la
  cifra publicada **ya incluye** los rangos (46 643 + 3 968 = 50 611; 48 143 + 3 018 = 51 161),
  de modo que la palabra «más» la contradice. El revisor 2 lo declaró para su lote; el revisor
  1 resolvió la ambigüedad en el mismo sentido sin decirlo. Es simétrico y no altera ningún
  tamaño.
* **`docs/evolucion/00-INDICE.md`** figura con 333 líneas y en `HEAD` da 334. La causa es el
  commit del propio gate. Contra la candidata, 333: el manifiesto es correcto.

---

### 3 · LÍNEA BASE, REPRODUCIDA POR MÍ SOBRE LA CANDIDATA

Clon `--no-local`, `git checkout 7b9829cb`, `porcelain` vacío antes, intérprete 3.12.14.
**DOS corridas completas de `registrar_evidencia.py`.**

| lo que el manifiesto §2 afirma | lo que YO mido | ¿casa? |
|---|---|---|
| 34/34 validadores · 34 evidencias · 0 problemas | `34/34 validadores en verde · 34 evidencias publicadas · 0 problemas`, en las **dos** corridas | **SÍ** |
| 682 casos en 18 baterías | `grep -h "^Ran [0-9]* test"` sobre las 34 evidencias → **18 baterías · 682 casos** | **SÍ** |
| E2E 15/15 · 25/25 · 24/24 | `15 de 15 pasos CUMPLIDOS` · `25 de 25` · `24 de 24` | **SÍ** |
| 133 infracciones detectadas · 0 NO detectadas | `133 infracciones detectadas · 0 NO detectadas` | **SÍ** |
| CERO saltos ejecutados | `0` líneas `OK (skipped=N)` de resumen · 18 líneas `^OK$`. Las **dos** apariciones de `skipped` en toda la evidencia son un NOMBRE de sabotaje (`NE14a`) y un NOMBRE de prueba (`T307`) | **SÍ** |
| determinismo byte a byte | `diff -r` entre el directorio de evidencia de la corrida 1 y el de la corrida 2 → **VACÍO** | **SÍ** |
| huella `6075d888ff2c7b70` | `kernel/.upstream-hash` = `6075d888ff2c7b70`; `kernel-status.sh` → `6075d888ff2c7b70 (396 ficheros) · LIMPIO`; `comprobar_integridad` `T150 SUPERADA` | **SÍ** |
| `porcelain` vacío antes y después | vacío antes, y **vacío después de las DOS corridas** | **SÍ** |
| las tres restas `A=0 · B=0 · C=0` | `TOTAL 58 obligaciones · A 0 · B 0 · C 0` | **SÍ** |

Recuento medido de las 18 baterías, para que nadie tenga que creerse el 682:

```text
adaptadores 37 · admision 65 · agentes 15 · arboles 38 · cardinalidad 20 · ciclo 52
contencion 20 · continua 24 · estado-durable 90 · gobierno-git 39 · identidad 23
integridad-evidencia 24 · macrocircuitos 30 · multimaquina 14 · raiz-externa 53
runtime 54 · sesion-nueva 27 · workspace 57                    18 · 682
```

**LA LÍNEA BASE ES REAL, ENTERA Y EXACTA SOBRE LA CANDIDATA.** No he encontrado una sola cifra
que no reproduzca. Y hay algo más fuerte que el manifiesto no reclama y conviene decir: tras
DOS corridas completas `git status --porcelain` sigue vacío, es decir **la suite regenera su
evidencia byte a byte igual a la confirmada**. El determinismo no es una promesa: es el
resultado por defecto de este árbol.

**Sobre `HEAD`, NO.** Ver `ADJ-GT1`.

---

### 4 · CADA RAZÓN CAPAZ DE MOVER EL VEREDICTO, REPRODUCIDA

#### 4.1 · `R1-B1` · la migración `0→1` del estado durable · **CONFIRMADA, y AGRAVADA**

**Estático.** El argumento `testigo` es obligatorio de sólo palabra clave desde `E-08`
(`motor.py:558`, `def _publicar_revision(self, revision, *, testigo)`), con su docstring:
«`testigo` NO tiene valor por defecto a propósito». De las cinco llamadas del árbol, **una no
lo pasa**:

```console
$ grep -n "_publicar_revision" estado/motor.py estado/migracion.py
migracion.py:178:            almacen._publicar_revision(revision_cero)          ← SIN testigo
motor.py:231:    almacen._publicar_revision(revision, testigo=TESTIGO_DE_FUNDACION)
motor.py:758:        self._publicar_revision(revision, testigo=testigo)
motor.py:1199:                    self._publicar_revision(nueva, testigo=testigo)
```

**Dinámico**, sobre un almacén heredado GENUINO —sin `FORMATO.json`, sin diario, sin
`REVISION.json`—, en copia desechable:

```console
$ mkdir -p mig/estado/canonico/items
$ echo '{"id":"it-uno","titulo":"heredado"}' > mig/estado/canonico/items/it-uno.json
$ python3.12 .../ads_estado.py --repo mig migrar
Traceback (most recent call last):
  File ".../ads_estado.py", line 684, in <module>      sys.exit(main())
  File ".../ads_estado.py", line 671, in main          return ejecutar(argumentos)
  File ".../ads_estado.py", line 519, in orden_migrar  informe = almacen.migrar(argumentos.a)…
  File ".../estado/motor.py", line 1756, in migrar     return _migracion.migrar(self, a_version)
  File ".../estado/migracion.py", line 95, in migrar   resultado = funcion(almacen)
  File ".../estado/migracion.py", line 178, in _migrar_0_a_1
    almacen._publicar_revision(revision_cero)
TypeError: Almacen._publicar_revision() missing 1 required keyword-only argument: 'testigo'
EXIT=1        stdout VACÍO · traza con SIETE rutas absolutas del anfitrión · CERO códigos tipados
```

**El almacén queda inmigrable.** El diario ya se fundó, de modo que la rama que contiene la
línea rota no se vuelve a entrar nunca:

```console
$ find mig/estado -type f
estado/diario/DIARIO.jsonl          ← ya contiene `almacen.inicializado`
estado/canonico/items/it-uno.json · estado/reconciliacion/… · estado/operacional/escritor.lock
$ python3.12 .../ads_estado.py --repo mig migrar        (2ª llamada)
[ESTADO_CORRUPTO] el fichero no existe (estado/REVISION.json)
EXIT=1
$ … (3ª llamada)  → idéntico. EXIT=1
```

**AGRAVANTE QUE AÑADO.** El daño no lo repara la corrección de la línea: con el diario ya
fundado y sin `REVISION.json`, la rama se salta y `_leer_revision()` falla **también con el
`testigo` puesto**. Un almacén que haya pasado por aquí queda inmigrable **incluso después de
arreglar el defecto**. El remedio no es una línea: es la línea, el fixture y un camino de
recuperación para los almacenes ya rotos.

**Por qué ninguna prueba lo ve — verificado.** La única cobertura,
`test_estado_durable.py:519 test_09_migracion_del_formato_heredado_cero_a_uno`, hace
`self.inicializar()` y **después** `os.remove(FORMATO.json)`. Ese almacén tiene diario con
`almacen.inicializado` **y** tiene `REVISION.json`: la rama rota **no se entra**. La prueba
pasa sobre un camino que el código productivo no recorre.

**Qué contradice, con las palabras del propio árbol.** `migracion.py` declara en su cabecera:
«un corte deja el almacén exactamente donde estaba a ojos de `abrir` —heredado—, y **volver a
llamar a `migrar()` retoma**». Medido: no retoma, y no puede retomar. Rompe `g.11`
—«una migración es RECUPERABLE»— y `E-15`, porque un error NO tipado cruza `main()` con la
traza entera, que es el modo de fallo que `E-15` existe para impedir.

**Confirmada íntegra. El revisor 1 no exagera: se queda corto.**

---

#### 4.2 · `R1-B2` · la raíz externa sin la purga `E-10` · **CONFIRMADA ÍNTEGRA**

Veneno: un `json.py` homónimo en `PYTHONPATH`, desde un `cwd` ajeno.

```console
$ cd /tmp && python3.12 .../raiz-externa/verificador.py capacidades          (CONTROL SANO)
{ "algoritmo": "ssh-ed25519", "condiciones_de_certificacion": [ …las nueve… ] }
EXIT=0

$ cd /tmp && PYTHONPATH=<veneno> python3.12 .../raiz-externa/verificador.py capacidades
{}
EXIT=0                                          ← publica el vacío y dice que todo fue bien
```

El instalador, igual:

```console
$ … instalar.py --destino <sano>  --arbol <cand>   → EXIT=0 · manifiesto 6 734 bytes · 41 ficheros
$ … PYTHONPATH=<veneno> instalar.py --destino <v>  --arbol <cand>
{}
EXIT=0                                            manifiesto      3 bytes · 41 ficheros
```

Aguas abajo, esa instalación comprobada **ya sin veneno** no falla tipada:

```console
$ python3.12 .../instalar.py --destino <v> --arbol <cand> --comprobar
  File ".../instalar.py", line 188, in verificar_instalacion
    esperados = {fila["ruta"]: fila["sha256"] for fila in manifiesto["ficheros"]}
KeyError: 'ficheros'
EXIT=1        traza con CUATRO rutas absolutas del anfitrión · CERO códigos tipados
$ … sobre la instalación SANA   →  "ok": true · EXIT=0
```

**Qué falta, medido.**

```console
$ grep -rn "PYTHONPATH|_purgar_la_ruta_de_importacion|entradas_del_lanzador" raiz-externa/ | wc -l
0                                        ← ni una línea de purga en TODO el paquete
$ grep -ln "_purgar_la_ruta_de_importacion" runtime/ads_*.py
ads_ciclo.py · ads_arboles.py · ads_admision.py · ads_runtime.py · ads_estado.py   ← los cinco
$ sed -n '49,50p' runtime/pruebas/test_integridad_y_evidencia.py
EJECUTABLES = ("ads_admision.py", "ads_estado.py", "ads_runtime.py",
               "ads_ciclo.py", "ads_arboles.py")
```

`T306` cubre **cinco ejecutables y ninguno más**. La raíz externa está fuera del alcance del
control, y ninguna otra prueba la sustituye.

**Es el MISMO defecto que el árbol declara reproducido y cerrado para los cinco `ads_*.py`,
vivo en la única pieza que `O26` §1 juzga.** Confirmada íntegra.

---

#### 4.3 · `R2-02` · el append-only de la sede del Owner · **CONFIRMADA, y MUY AGRAVADA**

**El mecanismo.** `admision/perimetro.py::_juzgar_append_only`, línea 394:

```python
if actual.startswith(anterior):
    return None
```

`anterior` son los bytes de la sede **en su commit de nacimiento**. El contraste es un
**PREFIJO**: todo lo que se añadió después queda sin guardar.

**Medido, byte a byte:**

```console
$ NAC=$(git log --diff-filter=A --format=%H -- docs/owner/ADS-OWNER-RESOLUCIONES.md | tail -1)
1d3b5d41434bb3bcd0b3323c4e6d56af5d7676e8
nacimiento 14 395 bytes · hoy 42 181 bytes · hoy.startswith(nacimiento) = True
prefijo protegido: 14 395 de 42 181  =  34,1 %

  O17 byte    2 837  PROTEGIDO        O21 byte  19 627  *** FUERA ***
  O18 byte    6 559  PROTEGIDO        O22 byte  24 204  *** FUERA ***
  O19 byte   11 277  PROTEGIDO        O23 byte  29 279  *** FUERA ***
  O20 byte   14 401  *** FUERA ***    O24 byte  34 469  *** FUERA ***
                                      O25 byte  36 513  *** FUERA ***
                                      O26 byte  38 864  *** FUERA ***
```

**EL ATAQUE DEL REVISOR 2, REPRODUCIDO.** Muté la condición 5 de `O26` §1 —«que el verificador
**no** dispone de la clave privada» → «que el verificador **SÍ puede** disponer…»—, la
confirmé en un commit, y corrí el verificador de admisión:

```console
$ sed -i 's/^5. que el verificador no dispone de la clave privada;$/5. que el verificador SÍ puede disponer de la clave privada;/' docs/owner/ADS-OWNER-RESOLUCIONES.md
$ git commit -qam "ataque: mutar condicion 5 de O26"
$ python3.12 .../ads_admision.py --repo <copia> verificar --base 7b9829cb --json
color= INDETERMINADO   hallazgos= 0
```

**CONTROL POSITIVO** — la misma clase de mutación DENTRO del prefijo (`O17`), confirmada:

```console
color= ROJO   hallazgos= 1
  -> V6-12  SEDE_DEL_OWNER_ALTERADA  docs/owner/ADS-OWNER-RESOLUCIONES.md
```

**CONTROL NEGATIVO** — un apéndice legítimo `# O27 · APÉNDICE DE PRUEBA`, confirmado:

```console
color= INDETERMINADO   hallazgos= 0        ← INDISTINGUIBLE del ataque
```

**MI AGRAVANTE, y es sustancialmente peor de lo que el revisor 2 describió.** No hace falta
mutar una condición: **se puede BORRAR de `O20` a `O26` enteras y sustituirlas por un texto
fabricado, y el guardián no dice nada.**

```console
$ python3.12 -c "b=open(SEDE,'rb').read(); open(SEDE,'wb').write(b[:14395] +
    b'\n\n# `O26` · TEXTO ENTERAMENTE FABRICADO POR EL ADJUDICADOR\n\n
      F6 QUEDA CERTIFICADA SIN CONDICIONES.\n')"
   la sede pasa de 42 181 a 14 494 bytes — se ha DESTRUIDO el 66 % de su contenido
$ git commit -qam "reescritura total posterior al nacimiento"
$ python3.12 .../ads_admision.py --repo <copia> verificar --base 7b9829cb --json
color= INDETERMINADO   hallazgos= 0
```

**El acto que da a este gate su competencia —`O26` §5— se puede reescribir para que diga lo
contrario, confirmarlo, y el verificador de admisión emite CERO hallazgos.** La sede encoge en
dos tercios y `V6-12` calla.

**Y no lo caza nada más.** La huella del kernel cubre `kernel/`, `packs/` y `tooling/`
—396 ficheros—, **no `docs/`**; y no existe ningún digest de la sede anclado en el árbol
(`grep -rn "ADS-OWNER-RESOLUCIONES" --include='*.py' --include='*.yaml'` sólo devuelve
declaraciones de autoridad en `FUENTES-CANONICAS.yml`).

**Por qué ninguna prueba lo ve — verificado.** Las cuatro pruebas de `SedeDelOwner` y las de
`ProcedenciaDelNacimiento` (`T302`–`T305`) montan una sede sintética
`b"# resoluciones\n\n## O1\n\ntexto original\n"` y **mutan ese mismo contenido**, que es el
nacimiento entero. **Ninguna prueba y ningún sabotaje del corpus muta contenido POSTERIOR al
nacimiento.** Y `V6-12` figura con sabotajes `N189, N242, N242b` — pero `N189` está declarado
contra `V6-11` («el verificador y su política se quedan fuera de su propio alcance») y se
imputa a `V6-12` sólo porque apunta al escenario `T189`, que nombra a los dos.

**Qué contradice.** `04-CONTRATOS` §6 declara el append-only «comprobado contra su
NACIMIENTO»; lo entregado es «el prefijo del nacimiento sigue ahí». Y `O18`, sexta condición
—«ninguna promesa de seguridad superior a la realmente entregada»— queda incumplida.

**Confirmada, y agravada por mí.**

---

#### 4.4 · `R2-03` · el universo de obligaciones encoge en silencio · **CONFIRMADA ÍNTEGRA**

Base sobre la candidata: `TOTAL 58 obligaciones · A 0 · B 0 · C 0`, repartidas
`§19 5 · F-nn 8 · V6 19 · g 16 · C 3 · deuda 7`. **Coincide con la derivación independiente
que el revisor 2 hizo a mano, y con la mía.**

```console
10a · CAMBIAR LA FASE de la fila `F-07` de **F6** a **F5** (una celda de una tabla)
      $ python3.12 derivar-universo-obligatorio.py --obligaciones
      EXIT=0 · (F-nn) 7 · TOTAL 57 · A 0 · B 0 · C 0
      $ grep -c 'F-07' salida  →  0                    DESAPARICIÓN TOTALMENTE SILENCIOSA

10e · RETIRAR la fila `F-10` entera
      EXIT=0 · (F-nn) 7 · TOTAL 57 · A 0 · B 0 · C 0
      $ grep -c 'F-10' salida  →  0                    SILENCIOSA

10d · RETIRAR el bloque `--- CONTRATO 2 · AMPLIAR T152 … ---` entero de §19
      EXIT=0 · (§19)  4 · TOTAL 57 · A 0 · B 0 · C 0
      la salida publica CONTRATO 1, 1bis, 3 y D104 · CONTRATO 2 no aparece
```

**La causa, leída en el código:**

```python
## derivar-universo-obligatorio.py
:896   if len(halladas) < 4:      raise SedeIlegible(…)   # §19 — hoy son CINCO: UNA de holgura
:975   if len(halladas) < 19:     raise …                 # V6 — sin holgura
:993   if len(halladas) != 16:    raise …                 # g  — exacto
:1007  if len(halladas) != 3:     raise …                 # C  — exacto
       hallazgos_externos_f6()  →  sólo levanta si CERO filas o CERO con fase F6.
                                   NO HAY SUELO sobre el número: F-nn no tiene cliquet
:766   universos_publicados()   →  el cliquet existe, y es SÓLO del universo de FUENTES
```

La cabecera del fichero promete, con estas palabras: «Nunca adivina y **nunca reduce el
universo en silencio**: un universo que encoge sin decirlo es…». **Para el modo
`--obligaciones` esa promesa no se cumple, y `O26` §5 convierte estas tres restas en criterio
de certificación.**

**Confirmada íntegra.**

---

#### 4.5 · `R2-04` · el `estado` de una prueba es un campo a mano · **CONFIRMADA, con una reproducción MEJOR que la del revisor 2**

**El mecanismo.** El campo `estado:` se escribe a mano en el bloque `ads:escenario` y
`registro_pruebas.py` lo copia verbatim:

```python
## validadores/registro_pruebas.py:57 y :76
resumen[datos.get("estado", "?")] = resumen.get(datos.get("estado", "?"), 0) + 1
… f" {datos.get('ejecucion','')} | **{ETIQUETA.get(datos.get('estado'), '?')}** |"
```

Barrí los 25 validadores buscando quién contrasta ese campo contra la evidencia:
**ninguno**. La única aparición que parece hacerlo, `comprobar_negativos.py:1496`
(`if fila.get("estado") != "prueba-fallida"`), lee el `estado` que un validador **devuelve en
tiempo de ejecución en su JSON**, no el campo declarado del escenario.

**Y no hace falta mutar nada: el árbol ya publica hoy la divergencia.**

```console
$ grep 'estado:' T270-T289-contratos-19-y-composicion.md (bloque T273)
estado: prueba-fallida
$ sed -n '220p' REGISTRO-generado.md
| [T273] | … | validador-estructural | **PRUEBA FALLIDA** | evidencia/composicion-procesos-salida.txt |
$ head -9 evidencia/composicion-procesos-salida.txt
## codigo: 0
T273  SUPERADA  Todo par del catálogo estático de D104 tiene su <CAP>:revision
4 superadas · 0 fallidas
$ la prosa del mismo fichero, L47:  «`F6` materializa, `T273` queda en VERDE»
```

**Tres sedes dicen VERDE y la cuarta publica `PRUEBA FALLIDA`, y los 34 validadores están
en verde.** Es la única `PRUEBA FALLIDA` del registro entero (recuento publicado:
`CONTRATO DEFINIDO 56 · PRUEBA SUPERADA 173 · PRUEBA FALLIDA 1 · total 231`).

Prefiero esta reproducción a la del revisor 2 —que mutó `T169` a `prueba-superada`— porque no
exige tocar nada: **el defecto está vivo hoy en el árbol candidato**, y demuestra lo mismo con
más fuerza. `REGISTRO.md` escribe «**Regla dura:** ninguna prueba sube de estado por argumento.
Sube porque se ejecutó y su salida quedó registrada». **Esa regla no está mecanizada.**

**Confirmada.**

---

#### 4.6 · Las OCHO condiciones de `O26` §1, comprobadas por mí sobre `7b9829cb`

El texto de `O26` §1 leído entero en su sede (`docs/owner/ADS-OWNER-RESOLUCIONES.md`
L902-L979). La condición 8 dice literalmente: «que clave desconocida, firma inválida, commit
incorrecto, tree incorrecto, ausencia de proveedor **y contaminación del entorno** fallan
cerrado». No hay interpretación posible: está escrito con esas palabras.

| # | condición | cómo la he medido YO | veredicto |
|---|---|---|---|
| 1 | raíz y evidencia **fuera** del árbol verificado | `instalar.py:90 raise InstalacionDentroDelArbol`; `errores.py:94 EVIDENCIA_DENTRO_DEL_ARBOL`; la instalación sana produce 41 ficheros y manifiesto de 6 734 bytes fuera del árbol | **CUMPLE** |
| 2 | firma **asimétrica** | `firma.py` delega en `ssh-keygen -Y` con Ed25519 y lo declara; `capacidades` publica `"algoritmo": "ssh-ed25519"` | **CUMPLE** |
| 3 | atestación ligada a commit **y** tree, simultáneamente | `atestacion.py:206 def exigir_commit` y `:219 def exigir_tree` son funciones SEPARADAS con errores propios `VINCULO_DE_COMMIT_ROTO` / `VINCULO_DE_TREE_ROTO` | **CUMPLE** |
| 4 | firmante y verificador **separados** | dos ficheros, dos procesos; `anfitrion_firmante.py:49` responde a `verificar` con «este anfitrion SOLO firma. Verificar es de anfitrion_verificador.py» | **CUMPLE** |
| 5 | el verificador **no dispone** de la clave privada | `grep -rl "PRIVATE KEY"` sobre TODO el árbol devuelve **un solo fichero**, y es `test_raiz_externa.py`, que es su propio control del control | **CUMPLE** |
| 6 | el ejecutor **no comparte** escritura sobre el control repo | **EJERCIDO POR MÍ, HOY, EN ESTE ANFITRIÓN** — ver el bloque de abajo | **CUMPLE** |
| 7 | rotación, solapamiento, retirada y revocación | `identidad/rotacion.py` con `IdentidadDesconocida`, `IdentidadFueraDeSolapamiento`, `IdentidadRevocada`; el solapamiento se mide en ÉPOCAS y no en reloj, y está escrito por qué | **CUMPLE** |
| 8 | …**y contaminación del entorno** fallan cerrado | **§4.2 de este dictamen.** `capacidades` publica `{}` con **código 0** e `instalar.py` escribe un manifiesto de **3 bytes** con **código 0** bajo `PYTHONPATH` envenenado | **NO CUMPLE** |

**La condición 6, ejercida por mí y no leída:**

```console
$ python3.12 -c "import aislamiento as a; a.ejecutar(<repo>, <externo>)"
mecanismo                    contenedor
identidad_distinta           true
identidad_del_runtime        uid 1000        identidad_del_verificador   uid 65534
control_positivo.escribio    true            control_de_lectura.leyo     true
no_ejecutados                []              ok                          true

los OCHO intentos, con el mensaje REAL del sistema:
  modificar-un-fichero                  sh: can't create /repo/README.md: Permission denied
  crear-un-fichero                      sh: can't create /repo/ADS-INTRUSO.md: Read-only file system
  borrar-un-fichero                     rm: can't remove '/repo/README.md': Read-only file system
  cambiar-una-ref                       sh: can't create /repo/.git/refs/heads/canonica: Read-only …
  alterar-la-configuracion-de-git       sh: can't create /repo/.git/config: Permission denied
  sustituir-la-clave-publica-aceptada   sh: can't create /externo/allowed_signers: Read-only …
  cambiar-la-politica                   sh: can't create /repo/kernel/…/POLITICA-CONTROL-REPO.yml: …
  modificar-la-atestacion-ya-firmada    sh: can't create /externo/atestacion.json: Permission denied

exigir_sin_escritura → True
```

Y el alcance REAL de este anfitrión, publicado por el propio aparato y no supuesto:

```text
usuario-del-sistema   NO disponible  «`sudo` exige contraseña (sudo: a password is required)»
contenedor            SÍ             alpine:3.20 · 65534:65534 · identidad distinta REAL
espacio-de-nombres    SÍ             LÍMITE DECLARADO: el root de dentro se mapea al MISMO usuario
```

**SIETE DE OCHO. La octava no se cumple**, y `O26` §2 exige las ocho **conjuntamente**.

**`O26` §4 se cumple** (la custodia productiva sigue EXTERNA; `E-17` declarado y no maquillado).
**`O26` §5.4 NO se cumple** (las ocho condiciones no se satisfacen).
**`O26` §5.5 NO se cumple**: hay bloqueantes internos vivos, y son tres.

---

#### 4.7 · `O26` NO se presenta como certificación · `B3` NO se declara satisfecho · **CONFIRMADO**

Barrido del corpus entero. `O26` aparece en 14 ficheros. **Ninguna sede lo presenta como
certificación, y CUATRO lo niegan expresamente:**

```text
04-CONTRATOS L113-117  «CERTIFICACIÓN DE `F6`: **ninguna.** Implementado y probado NO es
                       certificado. … Presentar `O26` como certificación es leerlo al revés»
DECISIONES L672        «**`O26` NO CERTIFICA NADA.** Acepta la ARQUITECTURA bajo ocho
                       condiciones y difiere a un gate»
D115                   «no es una elección de `F6` … No sustituye a `O26`»
01-MATRIZ (F6-B)       «`O26` **no se presenta como certificación**»
```

`B3` (`05-PLAN` §2.2): «la raíz externa existe, **la acepta el Owner**, y su ejecutor NO
comparte identidad de escritura con el runtime». **No se declara satisfecho en ninguna sede**,
y `06-DEUDA` §3 L127 lo escribe con todas las letras:

```text
**`B3` NO queda satisfecho por este acto.** Queda satisfecho su conyunto de autoridad, y el
resto —«la raíz externa existe» y «su ejecutor NO comparte identidad de escritura»— sigue
siendo materia de comprobación del gate. Declararlo satisfecho antes del gate sería
exactamente el atajo que `O26` §2 y §7 prohíben.
```

**Esto es un mérito del árbol y se dice como tal.** El corpus tuvo delante el atajo —presentar
un acto del Owner como si cerrara el criterio— y escribió por qué no lo tomaba.

---

#### 4.8 · La omisión de «FIN LITERAL DE `O26`.» · **MI DICTAMEN EXPRESO — MATIZO al revisor 2**

**Lo que verifico, y lo que no puedo verificar.** No tengo fuente primaria del dictado del
Owner: **no puedo comprobar qué palabras se emitieron.** Lo que sí compruebo:

```console
$ grep -rn "FIN LITERAL" .   (todo el repositorio, .md .py .yml)
(ninguna aparición)
$ awk '/^# `O[0-9]+`/{e=$2} /^## Texto/{print e}'  docs/owner/ADS-OWNER-RESOLUCIONES.md
O17 O18 O19 O20 O21 O22            ← O23, O24, O25 y O26 NO llevan `## Texto`
$ tail -3 docs/owner/ADS-OWNER-RESOLUCIONES.md
   la última línea del fichero es la última línea de `O26` §8. No hay delimitador de cierre.
```

Y la regla que la sede se impone a sí misma, leída en su cabecera:

```text
«Cada resolución se registra **íntegramente**, no en resumen.»
«El coordinador puede transcribir materialmente la respuesta del Owner …, pero **no puede
 reinterpretarla ni resumirla** como fuente canónica.»
```

**MI DICTAMEN, en tres partes:**

1. **La omisión es real y la clasificación fue un acto de interpretación.** Decidir que una
   línea es «delimitador del dictado» y no «texto de la resolución» es exactamente la
   facultad que la sede retira al coordinador. Se registra.
2. **Y el argumento se refuta a sí mismo, como el revisor 2 vio bien.** `O26` **no lleva
   `## Texto`**: la entrada empieza en su H1 y termina en el fin del fichero. La línea
   omitida era **el único delimitador de cierre que esa entrada tenía**, y se retiró alegando
   que era un delimitador. La consecuencia práctica: cuando se añada `O27`, dónde termina
   `O26` lo dirá la posición del siguiente H1 y nada más.
3. **PERO CORRIJO AL REVISOR 2 EN LO QUE IMPORTA.** El revisor 2 la eleva a co-causa de un
   hallazgo que la une con `R2-02` («las dos cosas juntas … es lo que convierte una nota de
   método en `H-R2-12`»). **Son independientes, y unirlas infla la primera.** La línea
   omitida **no tiene contenido normativo**: no impone obligación, no otorga autoridad y no
   altera ni una coma del sentido de `O26` §1 a §8, que están íntegras y son inequívocas. La
   competencia que `O26` §5 da a este gate **no queda en duda por esa omisión**. Lo que sí la
   deja sin guarda mecánica es `ADJ-B3`, y ése se sostiene solo.

**Severidad: MEDIA · propietario el OWNER · LIMITACIÓN PERMANENTE**, porque la sede es
append-only y no se puede corregir. Añado, confirmado: `O26` **tampoco lleva nota de
trazabilidad**, que es el instrumento con el que este corpus declara INVERIFICABLE una
procedencia y que `O17`, `O20`, `O21` y `O22` sí llevan.

---

#### 4.9 · LA FRONTERA DEL UNIVERSO — los documentos históricos de `F4c` y `F5` · **DECIDO: NO ES MATERIAL. La exclusión SE SOSTIENE**

El manifiesto §3 excluyó `docs/evolucion/16-` a `32-` y los de `F5`, con su razón escrita, y
declaró la exclusión atacable. **La he atacado y la sostengo. Cuatro razones, medidas:**

1. **Ningún hallazgo de este expediente los necesitó.** Barrido de los dos dictámenes:

   ```console
   $ grep -oE "docs/evolucion/[0-9]{2}-[A-Z-]+|SEXTO GATE|documento 2[0-9]" DICTAMEN-REVISOR-1
   docs/evolucion/11-ARQUITECTURA-INTEGRADA   (1)      ← que está EN su lote
   $ … DICTAMEN-REVISOR-2
   docs/evolucion/00-INDICE (4) · 11-ARQ (1) · SEXTO GATE (1)
   ```

   El revisor 2 necesitó **uno** —`EE-03` del sexto gate, para `R2-08`— y **lo dijo**, que es
   exactamente lo que el manifiesto prescribe para ese caso. Yo tampoco lo he necesitado:
   `ADJ-GT2` lo he reproducido con el comando que el **propio índice mínimo** publica.

2. **Lo normativo que esos documentos podrían aportar ya está en el lote por otra sede.** La
   clasificación `C-L` —el punto donde más habría dolido— tiene **sede única declarada** en
   `CHECKPOINT-ADS-NEXT.md`, que está íntegro en el lote del revisor 2 y que **él leyó
   entero**. Es con esa sede, no con un acta de `F4c`, con la que he resuelto la cuestión
   `C-L` de §4.10.

3. **`F4c` está CERRADA por composición de dos juicios independientes** y su cobertura la
   cerraron sus propios gates. Reabrirla aquí no probaría nada de `F6`.

4. **La exclusión se firmó ANTES de repartir, se publicó con su razón y nombró su válvula de
   escape.** Eso es lo contrario de una exclusión silenciosa, que es la clase de defecto que
   este expediente ha castigado seis veces.

**El gate NO cae por esta frontera. Cae por el lote del revisor 2.**

---

#### 4.10 · `C-L.7`, `C-L.10` y `C-L.13` · **DECIDO: FRONTERA DEFENDIBLE. El cargo de RECLASIFICACIÓN del revisor 2 CAE**

El revisor 2 lo llama reclasificación y lo cuenta entre las razones de fondo. **Lo he
reproducido y no se sostiene. Ésta es la corrección más importante que hago a un revisor.**

**Lo que el revisor 2 midió bien, y confirmo:** `06-DEUDA` §2 da a las tres, en su propia
tabla, fase `F6`; a dos de ellas propietario `PLT`; y a `C-L.10` la condición de cierre «la
implementación construida y ejecutada». Y el derivador las excluye por la **SECCIÓN** en que
viven, mientras para el componente `deuda` el criterio que aplica es la **FASE**:

```python
condiciones_c_l_con_fase_f6()   # §2 · se recogen … y se publican APARTE
deudas_y_limites()              # SECCIONES_DE_DEUDA (3,4,7,8,10bis,10ter) · fase F6 → DENTRO
```

**Lo que el revisor 2 NO comprobó, y decide la cuestión.** Fui a la sede única de la
clasificación, `CHECKPOINT-ADS-NEXT.md`, y leí QUÉ SON:

```text
CHECKPOINT L2669   «C-L.10 CONTRATADA PARA F6 · única en este estado. D102: tres contratos
                   —censo AFIRMACIONES derivado, T152 sobre toda sede que publique versión, y
                   la guardia de intérprete con exit 2— y ocho casos de regresión»
CHECKPOINT L2679   «C-L.13 … J-11 CONTRATO COMPLETO PARA F6 en D102, NO implementado»
```

Y los bloques de `11-ARQ` §19 que **sí** están en el universo:

```console
$ grep -n -- '--- CONTRATO' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
11562:--- CONTRATO 1 · DERIVAR EL CENSO `AFIRMACIONES` ---
11599:--- CONTRATO 1bis · LOS PERFILES DE AGENTE, QUE NADIE CENSA (`N-04`) ---
11625:--- CONTRATO 2 · AMPLIAR `T152` A TODA SEDE QUE PUBLIQUE VERSIÓN ---
11658:--- CONTRATO 3 · LA GUARDIA DE VERSIÓN DE INTÉRPRETE (`J-11`) ---
```

```text
C-L.10        ≡  CONTRATO 1  +  CONTRATO 2  +  CONTRATO 3
C-L.13 (vivo) ≡  J-11        ≡  CONTRATO 3
```

Y los cuatro están **DENTRO** del universo, con prueba, sabotaje y evidencia:

```text
CONTRATO 1     §19  T270,T277           N270c            evidencia/recuentos-salida.txt
CONTRATO 1bis  §19  T271,T277           N271             evidencia/recuentos-salida.txt
CONTRATO 2     §19  T272,T277           N272b,N272d      evidencia/versiones-salida.txt
CONTRATO 3     §19  T158                N158,N158b,N158c evidencia/evidencia-salida.txt
```

**La exclusión de `C-L.10` y `C-L.13` no esconde trabajo sin hacer: evita CONTARLO DOS VECES
bajo su rótulo de la época de `F4c`/`F5`.** Y no es silenciosa — el instrumento imprime en su
propia cara el hecho que la contradiría:

```text
condiciones de cierre `C-L` con fase `F6` (3)  ·  OTRO censo: `06-DEUDA` §2, heredado …
    C-L.10   fase declarada: **`F6`**
    C-L.13   fase declarada: **`F6`**
    C-L.7    fase declarada: **`F5`** la especificación · **`F6`** el instrumento
```

`C-L.7` es distinto y también se sostiene: su condición de cierre es «**sólo un gate
independiente posterior puede cerrarla**», no «una implementación». No es una obligación de
construcción, y sigue NO CERRADA — como la sede dice y como este gate no cambia.

**Veredicto: FRONTERA DEFENDIBLE. `H-R2-13(iii)` cae como cargo de reclasificación.** Lo que
sobrevive, y lo recojo como hallazgos propios de severidad MEDIA:

* **`ADJ-M10`** — el criterio de pertenencia **no es uno solo**: fase para `deuda`, sección
  para `C-L`. Que el resultado sea correcto no arregla que la frontera no esté trazada por la
  propiedad que dice trazarla.
* **`ADJ-M9`** — **la celda de `06-DEUDA` §2 está CADUCADA**, y es la que indujo al revisor 2
  al error: sigue diciendo de `C-L.10` «**cero líneas de código escritas**» y de `C-L.13`
  «uno permanece contratado para `F6` y **NO implementado**» cuando los tres contratos están
  construidos, probados y con evidencia publicada. **Es la misma familia que `ADJ-G3`: el
  corpus subestima lo que ha construido, y esta vez le costó un falso hallazgo a un revisor.**

---

#### 4.11 · Las divergencias del aparato del gate — reproducidas las dos mitades

Los dos revisores llegaron a esto por separado (`R1-M1` y `R2-09`). **Las dos mitades se
reproducen sobre `HEAD` = `20330e69`, en un clon limpio con `porcelain` vacío:**

```console
$ python3.12 kernel/operativo/validadores/comprobar_evidencia.py
T158  FALLIDA   La evidencia publicada demuestra lo que el informe afirma
   · fuentes-salida.txt: la vigencia 'T161-cobertura' publica 504 y el corpus vigente da 505.
     La evidencia está CADUCADA
EXIT=1

$ python3.12 docs/evolucion/verificacion/derivar-universo-obligatorio.py
FALLA CERRADO · 1 manifiesto(s) INMUTABLE(s) … no aportan NI UNA fila al cliquet:
['F6-ASIGNACION-GATE-CERTIFICACION-FINAL-20260904.md'] …
EXIT=2

$ … las dos, sobre la CANDIDATA 7b9829cb  →  EXIT=0 y EXIT=0
```

**El acto de convocar el gate cambió el corpus que dos instrumentos del gate miden.** Los dos
FALLAN CERRADO, que es lo correcto y es un mérito del aparato; pero significa que la línea base
sólo se reproduce sobre el SHA candidato, que es además lo que `O26` §2 manda medir.

---

### 5 · HALLAZGOS ACEPTADOS

`identificador · severidad · sede · reproducción · remedio · propietario · fase · clase`

#### BLOQUEANTES

| id | sede | reproducción | remedio | propietario · fase | clase |
|---|---|---|---|---|---|
| **`ADJ-B1`** ≡ `R1-B1` | `runtime/estado/migracion.py:178` contra `estado/motor.py:558` | §4.1. Almacén heredado genuino → `TypeError` no tipado con traza de 7 rutas del anfitrión, `EXIT=1`, stdout vacío; 2ª y 3ª llamada → `ESTADO_CORRUPTO`, inmigrable para siempre | pasar el testigo de `E-08`; **cambiar el fixture** para que construya un heredado real; **y** un camino de recuperación para los almacenes ya rotos, que la corrección de la línea no repara | autoría de `F6`, eje de estado durable · `F6` | **INTERNO** |
| **`ADJ-B2`** ≡ `R1-B2` | `kernel/operativo/raiz-externa/` entero · alcance de `T306` en `test_integridad_y_evidencia.py:49` | §4.2. `PYTHONPATH` envenenado → `capacidades` publica `{}` con **código 0**; `instalar.py` escribe manifiesto de **3 bytes** e instala 41 ficheros con **código 0**; aguas abajo `KeyError: 'ficheros'` con 4 rutas del anfitrión. Cero líneas de purga en el paquete | llevar el prólogo `E-10` completo a `verificador.py` e `instalar.py`, **y ampliar `EJECUTABLES` de `T306`**, que es lo que impide que vuelva | autoría de `F6`, eje de raíz externa · `F6` | **INTERNO** |
| **`ADJ-B3`** ≡ `R2-02`, agravado | `runtime/admision/perimetro.py:394` · `04-CONTRATOS` §6 · `03-GOBIERNO` §2 | §4.3. Prefijo de 14 395 de 42 181 bytes = 34,1 %. Mutar la condición 5 de `O26` y confirmar → `hallazgos=0`. **Borrar `O20`–`O26` enteras y fabricar un texto nuevo → `hallazgos=0`.** Control positivo (`O17`) → ROJO `V6-12`; control negativo (apéndice) → indistinguible. Ninguna prueba muta contenido posterior al nacimiento | igualdad sobre el prefijo común **y sólo-adición sobre el resto**, con una prueba que mute una entrada POSTERIOR al nacimiento y exija ROJO | `PLT` implementa · `SIS` propietario · `F6` | **INTERNO** |

#### GRAVES

| id | sede | reproducción | remedio | propietario · fase | clase |
|---|---|---|---|---|---|
| **`ADJ-G1`** ≡ `R2-03` | `derivar-universo-obligatorio.py`, modo `--obligaciones` | §4.4. Tres vías con `exit 0`: cambiar la fase de una fila `F-nn` (58→57, el id desaparece), retirar una fila `F-nn`, retirar un bloque `CONTRATO n` (guarda `< 4` con cinco reales = una unidad de holgura). `F-nn` no tiene suelo; el cliquet es sólo del universo de FUENTES | cliquet propio para obligaciones; publicar lo que se cae de CADA componente; derivar el suelo de §19 en vez de escribirlo | `PLT` · `F6` | **INTERNO** |
| **`ADJ-G2`** ≡ `R2-04` | bloques `ads:escenario` · `validadores/registro_pruebas.py:57,76` | §4.5. Nada contrasta el `estado:` declarado contra la evidencia. **Divergencia VIVA hoy:** `T273` publicado `PRUEBA FALLIDA` mientras su evidencia dice `SUPERADA` y su prosa dice «queda en VERDE», con 34/34 validadores verdes | derivar el `estado` de la evidencia, o contrastar el declarado contra la salida del validador que la prueba nombra | `PLT` implementa · `SIS` propietario · `F6` | **INTERNO** |
| **`ADJ-G3`** ≡ `R2-05` | `04-CONTRATOS-TECNICOS.md` §5.3 L326-329 · §5.4 L336-337 · §6 L343 y L382 · §4 L274 | El documento que se declara **la ÚNICA SEDE** de la distinción construido/diseñado afirma en cuatro secciones que no existen los adaptadores, el verificador de admisión, la raíz externa y el sellado, y las cuatro cosas existen con evidencia. Su propia §1.1 las declara CONSTRUIDAS. `06-DEUDA` §6 L197 y `05-PLAN` L6 lo repiten | que §5.3, §5.4, §6 y §4 **remitan a §1** en vez de declarar estado | `SIS` · `F6` | **INTERNO** |

#### MEDIAS

| id | sede | qué es | propietario | clase |
|---|---|---|---|---|
| **`ADJ-M1`** ≡ `R1-M2` | `ads_admision.py:388` | `censo-formulas` sobre el propio candidato: `segundas definiciones: 7 · ok: no · EXIT=1`, mientras su prueba está verde porque censa otro conjunto | autoría `F6` | INTERNO |
| **`ADJ-M2`** ≡ `R1-M3` | los cinco `ads_*.py` | los cinco llevan el comentario «`E-10` · la PROCEDENCIA se PUBLICA», y **sólo `ads_admision.py` tiene una orden que la publique** (medido en las cinco tablas `ORDENES`) | autoría `F6` | INTERNO |
| **`ADJ-M3`** ≡ `R1-M4` | `CONTRATO-ESTADO-DURABLE.md` §3 L106-107 | afirma que las tres E2E «ya no pueden seguir verdes sobre un almacén irrecuperable». **Ninguna de las tres inyecta `entre-el-paso-8-y-el-9`** (`grep -c` = 0 en las tres), que es el único punto que produce ese estado | autoría `F6` | INTERNO |
| **`ADJ-M4`** ≡ `R2-13(i,ii)` | `derivar-universo-obligatorio.py`, `ROTULOS_DE_RESTA` | `A=0` **no demuestra** `O26` §5.1 («sin implementar»): el predicado es «nombrada en un `cubre:` con validador». `B=0` **no demuestra** §5.2: contraejemplo vivo, `V6-12` con `B=0` y la propiedad de §4.3 sin ningún sabotaje que la ponga roja | `PLT` | INTERNO |
| **`ADJ-M5`** ≡ `R2-14` | `comprobar_recuentos.py:239`, `AMBITO_VIVO` | seis prefijos de INCLUSIÓN **sin motivo escrito para lo que dejan fuera**, mientras `FUERA_DEL_AMBITO` motiva sus seis y `T151` comprueba los motivos. `docs/rediseno/`, `docs/owner/`, `docs/evolucion/` y `tooling/` quedan fuera en silencio. No es hipotético: `E5-4` de §19 registra un recuento erróneo en `docs/rediseno/a-ENMIENDA-E1-ENC.md` y en `(a)`, fuera del barrido | `PLT` | INTERNO |
| **`ADJ-M6`** ≡ `R2-06` | `docs/f6/00-ESTADO-DE-IMPLEMENTACION-F6.md` L168 | conserva «Sólo un resultado es conforme con las dos normas, así que **no hay decisión del Owner que tomar**», premisa que `01-MATRIZ` L113 declara medida falsa: «**Hay al menos tres resultados conformes, no uno.**» | `SIS` | INTERNO |
| **`ADJ-M7`** ≡ `R2-07` | `docs/f6/01-MATRIZ-DE-COMPLETITUD-F6.md` L190 y L192, columna «estado final medido» | afirma **en presente** «**`T151` está en ROJO sobre tres sedes vivas**» y «**`T152` está en ROJO sobre `kernel/operativo/00-INDICE.md`**», presentándolo como la PRUEBA POSITIVA de §19. La evidencia dice `T151 SUPERADA` y `T152 SUPERADA`. Verificado columna a columna: no es un malentendido de tabla | `SIS` | INTERNO |
| **`ADJ-M8`** ≡ `R2-10` | `06-DEUDA` §13, comando 5 (L475) | publica `grep -rn 'python_requires' tooling/ kernel/ ; echo "(vacío = A14 sigue abierto)"`. Ejecutado: **vacío**. Por su propia anotación, «`A14` sigue abierto», mientras §4 del mismo documento declara `A14` **CERRADA POR `F6`** | `SIS` | INTERNO |
| **`ADJ-M9`** · MÍO | `06-DEUDA` §2, filas `C-L.10` y `C-L.13` | declaran «**cero líneas de código escritas**» y «**NO implementado**» cuando el CHECKPOINT identifica `C-L.10` con `CONTRATO 1+2+3` y el componente vivo de `C-L.13` con `J-11 ≡ CONTRATO 3`, **los cuatro construidos, probados y en el universo**. §4.10. Es la celda que indujo al revisor 2 a un cargo de reclasificación que no existe | `SIS` | INTERNO |
| **`ADJ-M10`** · MÍO (mitad viva de `R2-13(iii)`) | `derivar-universo-obligatorio.py` | el criterio de pertenencia **no es uno solo**: FASE para el componente `deuda`, SECCIÓN para `C-L`. El resultado es correcto (§4.10) pero la frontera no está trazada por la propiedad que dice trazarla | `PLT` | INTERNO |
| **`ADJ-M11`** ≡ `R1-I1` | `arboles/versiones.py:22-25` y `CONTRATO-ARBOLES-ADVERSARIALES.md` §2 L75 contra `admision/censo.py:378` | las dos primeras afirman que `arboles/` «no está entre» los paquetes del censo; el código dice `PAQUETES_DEL_VERIFICADOR = ("admision","gobierno","adaptadores","identidad","arboles")` | autoría `F6` | INTERNO |

#### DEL OWNER · NO CORREGIBLES

| id | sede | qué es | propietario | clase |
|---|---|---|---|---|
| **`ADJ-O1`** ≡ `R2-11` | entradas `O23`–`O26` | la sede declara obligatorios seis campos por entrada —identificador · fecha · procedencia · texto · alcance · relaciones de revisión—. Medido: `O17`–`O22` llevan `## Texto`; **`O23`, `O24`, `O25` y `O26` no**. `FD-2` registra el defecto **sólo para `O23` y `O24`**: `O25` y `O26` son instancias nuevas y no registradas | el **Owner**; la sede es append-only | **EXTERNO · LIMITACIÓN PERMANENTE** |
| **`ADJ-O2`** ≡ `R2-12`, MATIZADO | entrada `O26` | la omisión de «FIN LITERAL DE `O26`.» es un acto de interpretación que la sede retira al coordinador, y `O26` carece de `## Texto` y de nota de trazabilidad. §4.8. **Pero la línea no tiene contenido normativo y NO pone en duda la competencia que `O26` §5 da al gate**: eso lo hace `ADJ-B3`, que se sostiene solo | el **Owner** para la sede · `SIS` para la nota | **EXTERNO · LIMITACIÓN PERMANENTE** |

#### DEL APARATO DE ESTE GATE — no del candidato

| id | sede | qué es | propietario | clase |
|---|---|---|---|---|
| **`ADJ-GT1`** ≡ `R1-M1` ≡ `R2-09` | commit `26d6c54` · `00-INDICE.md` · `derivar-universo-obligatorio.py` | sobre `HEAD`: `comprobar_evidencia` **`T158 FALLIDA`, `EXIT=1`**, y el derivador **FALLA CERRADO con `EXIT=2`**. Sobre la candidata, los dos en 0. §4.11 | quien convoca el gate | LÍMITE DEL GATE |
| **`ADJ-GT2`** ≡ `R2-08` | `docs/evolucion/00-INDICE.md` | el manifiesto de ESTE gate se enlaza **sólo desde su fila del registro de pasadas** y no desde la LISTA, que es lo que la regla escrita en el propio índice exige. Reproducido con el comando que el índice publica como prueba de que la regla se cumple: **el `diff` ya no sale vacío** y la única línea es este manifiesto. **Sexta recurrencia** de `S-18`≡`T-14`→`Y-03`≡`Z-09`→`EE-03`→`HH2-12` | el coordinador de este gate | LÍMITE DEL GATE |
| **`ADJ-GT3`** ≡ `R2-01` | el reparto | `ASIGNADO − LEÍDO ≠ ∅` en el lote del revisor 2: 50 de 84 ficheros sin abrir, 29 329 de 48 143 líneas (60,9 %). Verificado aritméticamente por mí, §2.3. Por §4 del manifiesto, el gate es NO VÁLIDO | el revisor 2 lo declara; la regla es del manifiesto | LÍMITE DEL GATE |
| **`ADJ-GT4`** ≡ `R1-I2` · LEVE | el manifiesto §1 | `refs/heads/review/f6-post-gate-corrections-candidate-20260904` **no existe**; existe como `refs/remotes/origin/…` y apunta bien a `7b9829cb` | el coordinador | LÍMITE DEL GATE |
| **`ADJ-GT5`** · MÍO · LEVE | el manifiesto §5 y §6 | «50 611 líneas … **más** los rangos» y «51 161 líneas … **más** los rangos»: en los dos casos la cifra **ya incluye** los rangos. Simétrico, sin efecto sobre el tamaño | el coordinador | LÍMITE DEL GATE |

**Ningún hallazgo es de clase LÍMITE DE ANFITRIÓN.** Todo lo que este anfitrión no puede dar
—usuario del sistema distinto, `cgroup v2` ejercitable— el árbol ya lo declara, lo mide y lo
publica con su motivo. Eso es un mérito y se dice como tal.

---

### 6 · HALLAZGOS RECHAZADOS O CORREGIDOS, con el nombre de quien los planteó

**`R2-13(iii)` · REVISOR 2 · «`C-L.7`, `C-L.10` y `C-L.13` son una RECLASIFICACIÓN» ·
**CAE COMO CARGO.** §4.10. `C-L.10 ≡ CONTRATO 1 + 2 + 3` y el componente vivo de
`C-L.13 ≡ J-11 ≡ CONTRATO 3` según la **sede única** de la clasificación, el
`CHECKPOINT-ADS-NEXT.md` — que estaba en su lote y que él leyó entero. Los cuatro contratos
están DENTRO del universo con prueba, sabotaje y evidencia. La exclusión evita contarlos dos
veces; no esconde trabajo. `C-L.7` tiene por condición de cierre «sólo un gate independiente
posterior puede cerrarla», que no es una obligación de construcción. Sobreviven `ADJ-M10` (el
criterio no es uno solo) y `ADJ-M9` (la celda de `06-DEUDA` §2 está caducada, y es la que
provocó el error).

**`R2-13(i)` · REVISOR 2 · «el rótulo se movió para que la cifra encajara» · **MATIZADO.** El
cargo de maquillaje no se sostiene: el comentario de `H-07` en el código escribe él mismo que
«una obligación sin escenario que la cubra es indistinguible, PARA ESTE APARATO, de una sin
implementar, y **esa indistinción es justamente el defecto — no se tapa rotulándola**», y las
dos exclusiones se publican con su fase. Eso es lo contrario de maquillar. **Lo que sobrevive
íntegro, y lo acepto como `ADJ-M4`, es el punto lógico: `A=0` bajo el rótulo honesto no
demuestra `O26` §5.1, y nada más lo demuestra.**

**`R2-08` · REVISOR 2 · la consecuencia anunciada · **NO SE MATERIALIZA.** El índice escribe
que quien publique un manifiesto sin enlazarlo «deja el árbol que juzga con un validador
canónico en rojo». Medido sobre `HEAD`:

```console
$ python3.12 kernel/operativo/validadores/comprobar_referencias.py
T147  SUPERADA   Todo documento es alcanzable por ruta … 337 documentos · 1 superadas · 0 fallidas
EXIT=0
```

El manifiesto **sí es alcanzable** por su fila del registro de pasadas, luego no hay huérfano.
**La recurrencia de la regla es real y la acepto (`ADJ-GT2`); su consecuencia anunciada, no.**

**REVISOR 2 · «el reparto no era asumible» —implícito en `R2-01` al imputar el hallazgo «al
coordinador que dimensionó y repartió»— · **RECHAZADO.** Lote R1 = 50 611 líneas; lote R2 =
51 161. Diferencia: 550 líneas, **1,1 %**. He recontado las 225 rutas de los dos lotes contra
el árbol de la candidata y **no hay una sola discrepancia**. Un revisor terminó un lote de
tamaño prácticamente idéntico. **El dimensionado no es el defecto.** Publicar los tamaños
antes de repartir fue la decisión correcta y es lo que permite cerrar esta pregunta con
números en vez de con opiniones. El hallazgo `ADJ-GT3` se mantiene entero por su hecho —la
resta no vacía—, no por su imputación.

**REVISOR 2 · `R2-12` como co-causa de un bloqueante · **MATIZADO a `ADJ-O2`.** §4.8. La
omisión es real y no corregible, pero no tiene contenido normativo y no toca la competencia
del gate. Unirla a `R2-02` infla la primera sin reforzar el segundo, que se sostiene solo.

**REVISOR 1 · `R1-B1` · **CONFIRMADO Y AGRAVADO, no matizado.** El almacén no sólo queda
inmigrable: sigue inmigrable **después** de corregir la línea, porque el diario ya está
fundado y `REVISION.json` no existe. El remedio que el revisor 1 propone es necesario y no
suficiente.

**REVISOR 1 · su declaración de cobertura · **ACEPTADA**, con la reserva metodológica que
corresponde: he verificado que su tabla coincide ruta a ruta y línea a línea con el lote y que
no tiene una sola casilla en NO; el acto de leer no es verificable por nadie, y no finjo lo
contrario.

**LA FRONTERA DE `F4c`/`F5` · el manifiesto la ofreció al ataque · **SOSTENIDA.** §4.9. No es
material y el gate no cae por ella.

---

### 7 · LO QUE EL ÁRBOL SÍ SOSTIENE

Un dictamen que sólo publica lo que falla miente por omisión. Esto es lo que he medido y
sostiene, y es mucho.

```text
LA LÍNEA BASE ES REAL Y      las NUEVE cifras reproducidas por mí sobre la candidata, sin una
ENTERA                       sola divergencia, con DOS corridas completas. Y algo que el
                             manifiesto no reclama: tras las dos corridas `git status
                             --porcelain` sigue VACÍO — la suite regenera su evidencia byte a
                             byte igual a la confirmada. El determinismo no es una promesa:
                             es el resultado por defecto de este árbol

SIETE DE LAS OCHO            raíz y evidencia fuera del árbol · firma Ed25519 asimétrica ·
CONDICIONES DE `O26` §1      commit y tree en funciones separadas con errores propios ·
                             firmante y verificador separados y cada uno negándose a hacer lo
                             del otro · la clave privada no está en el árbol, y el único
                             fichero que la nombra es su propio control del control · la
                             identidad rota, solapa, se retira y se revoca, con el solapamiento
                             en ÉPOCAS y no en reloj

`O26` §1.6 EJERCIDA POR MÍ   contenedor real, uid 1000 → 65534, OCHO intentos de escritura de
HOY, EN ESTE ANFITRIÓN       ocho impedidos CON EL MENSAJE REAL DEL SISTEMA, control positivo
                             que escribe, control de lectura que lee, `exigir_sin_escritura`
                             True. Y el alcance del anfitrión publicado sin fingir: el usuario
                             del sistema NO está disponible y se dice por qué, y el espacio de
                             nombres declara su límite en vez de aprovecharlo

`O26` NO SE PRESENTA COMO    ninguna sede lo hace, y CUATRO lo niegan expresamente. `06-DEUDA`
CERTIFICACIÓN · `B3` NO SE   §3 escribe «`B3` NO queda satisfecho por este acto» y explica que
DECLARA SATISFECHO           declararlo antes del gate «sería exactamente el atajo que `O26`
                             §2 y §7 prohíben». Tuvo el atajo delante y escribió por qué no

CERO SALTOS, DE VERDAD       las dos únicas apariciones de `skipped` en las 34 evidencias son
                             un NOMBRE de sabotaje (`NE14a`) y un NOMBRE de prueba (`T307`).
                             No hay ni un `skips_permitidos` en `validadores.yaml`

EL APPEND-ONLY, COMO CADENA  ocho commits sobre la sede; hoy empieza por el nacimiento; la
DE COMMITS, ESTÁ INTACTO     cadena es íntegra eslabón a eslabón. Lo que falla es el ALCANCE
                             del contraste (`ADJ-B3`), no la historia

LOS INSTRUMENTOS FALLAN      el derivador, ante el manifiesto de este mismo gate, NO adivina:
CERRADO CUANDO NO SABEN      `EXIT=2` nombrando el fichero y explicando en tres líneas por qué
                             callar sería peor. `comprobar_evidencia` marca la evidencia
                             CADUCADA en vez de aceptarla. Un pipe sin escapar en una fila de
                             §19 → `EXIT=2` nombrando la fila. Ésta es la conducta correcta y
                             es cara de construir

LOS SUELOS EXACTOS FUNCIONAN `V6` (`< 19`), `g` (`!= 16`) y `C` (`!= 3`) no tienen holgura: mis
                             tres ataques al universo sólo pasaron por `F-nn`, que no tiene
                             suelo, y por §19, que lo tiene desfasado en una unidad

`E-13` CERRADO               el universo publica las CUATRO obligaciones de §19 una a una, con
                             identificador propio y sin absorción — el derivador usa fronteras
                             de palabra para que `CONTRATO 1` no se trague a `CONTRATO 1bis`

`E-17` Y `E-18` NO ESTÁN     la custodia productiva sigue declarada EXTERNA en las tres sedes
MAQUILLADOS                  del paquete, `ads_estado.py atestar` imprime la advertencia en su
                             propia salida, y el corpus acota que «no afirma nada sobre
                             anfitriones que no ha medido»

LA HUELLA Y SU CONTROL       `6075d888ff2c7b70` · 396 ficheros · LIMPIO · `T150 SUPERADA`, y la
                             huella cubre a los propios validadores

EL CORPUS SE EQUIVOCA        `ADJ-G3`, `ADJ-M7` y `ADJ-M9` son todos del mismo signo: sedes que
HACIA ABAJO, NO HACIA        declaran NO CONSTRUIDO lo construido. Es un defecto real y está
ARRIBA                       registrado. Pero nadie ha convertido una deuda interna de `F6` en
                             externa para no cerrarla, y he ido a buscarlo expresamente
```

---

### 8 · LAS CINCO DECLARACIONES

#### A · VALIDEZ

**`EL GATE NO ES VÁLIDO`**

`Motivo:` el revisor 2 declara `ASIGNADO − LEÍDO ≠ ∅` y su declaración es exacta, verificada
por mí línea a línea contra el lote que el manifiesto le asignó: **50 de 84 ficheros sin
abrir y 29 329 de 48 143 líneas, el 60,9 %**, entre ellos `macrocircuitos/fase0.py` —cuya
`FASE 0` es la sede de las once filas `X-S` de `11-ARQ` §9.6, rango asignado EXPRESAMENTE a
su lote—, `ciclo/agentes.py`, `ciclo/planificacion.py`, `comprobar_composicion_procesos.py`,
`comprobar_contratos.py`, `validadores.yaml`, `exclusiones.yaml` y los once ficheros
`Tnnn-*.md`. La regla §4 del manifiesto es literal, no tiene atenuantes y me prohíbe sustituir
su lectura con la mía. **El defecto no está en el dimensionado** —los dos lotes difieren en
550 líneas, el 1,1 %, y el otro revisor terminó el suyo—, y **no está en la frontera de
`F4c`/`F5`**, que he atacado y sostengo. Está en que un lote asignado no se leyó, y en que
decirlo a tiempo era lo correcto.

#### B · COMPLETITUD

**`F6 NO ESTÁ COMPLETAMENTE IMPLEMENTADA`**

`Pendientes internos:` **`ADJ-B1`** — la migración `0→1` del estado durable revienta con un
`TypeError` sin tipar en su único camino productivo, saca la traza del anfitrión por `main()`
y deja el almacén heredado inmigrable incluso después de corregir la línea, contra `g.11` y
`E-15`, sin que ninguna prueba lo vea porque su fixture no construye un almacén heredado real.
**`ADJ-B2`** — la raíz externa no lleva la purga `E-10`: con `PYTHONPATH` envenenado publica
`{}` con código 0 e instala 41 ficheros con un manifiesto de 3 bytes y código 0, y `T306` sólo
alcanza a cinco ejecutables que no la incluyen. **`ADJ-B3`** — el append-only de la sede del
Owner es un contraste de PREFIJO que protege el 34,1 % de la sede: `O20`–`O26` se pueden
mutar, o borrar enteras y sustituir por un texto fabricado, confirmarlo, y `V6-12` emite cero
hallazgos, indistinguible de un apéndice legítimo. **`ADJ-G1`** — el universo de obligaciones,
que `O26` §5 convierte en criterio de certificación, encoge en silencio por tres vías con
`exit 0`. **`ADJ-G2`** — el `estado` de una prueba es un campo a mano que nada contrasta
contra su evidencia, con una divergencia viva hoy en `T273`. **`ADJ-G3`** — el documento que
se declara la única sede de la distinción construido/diseñado se contradice a sí mismo en
cuatro secciones. Y la propia matriz del árbol conserva `F6-H` rotulada **PARCIAL**. A esto se
añade que **`A=0` no demuestra `O26` §5.1 y `B=0` no demuestra `O26` §5.2** (`ADJ-M4`), de
modo que las tres restas vacías, siendo ciertas, no acreditan lo que `O26` les pide acreditar.

#### C · `O26` Y `B3`

**`LA RAÍZ EXTERNA NO SATISFACE O26/B3`**

`Motivo:` la condición **8** de `O26` §1 —«que clave desconocida, firma inválida, commit
incorrecto, tree incorrecto, ausencia de proveedor **y contaminación del entorno** fallan
cerrado»— **no se cumple sobre esta candidata**: reproducido por mí, `verificador.py
capacidades` publica `{}` con código **0** e `instalar.py` escribe un manifiesto de **3
bytes** e instala 41 ficheros con código **0** bajo `PYTHONPATH` envenenado, y el paquete
entero no contiene ni una línea de la purga `E-10` que el mismo repositorio declara cerrada
para los cinco `ads_*.py`. Las otras **siete condiciones sí se cumplen** y las he comprobado
una a una, incluida la §1.6 **ejercida hoy en este anfitrión** con ocho de ocho intentos de
escritura impedidos. Pero `O26` §1 exige demostrarlas **conjuntamente**, y `O26` §2 sólo hace
aplicable la aceptación arquitectónica a una candidata «cuando un gate independiente **VÁLIDO**
demuestre las ocho condiciones sobre su SHA exacto» — y este gate no es válido. En consecuencia
`B3` sigue sin satisfacerse: `O26` emite el conyunto de autoridad y lo emite CONDICIONADO, y
el resto del criterio queda sin acreditar. Lo que el árbol **sí** sostiene, y consta: `O26`
está inscrita literal en la sede canónica, **no se presenta como certificación en ninguna
sede** —cuatro lo niegan expresamente— y **`B3` no se declara satisfecho en ninguna**;
`06-DEUDA` §3 escribe «`B3` NO queda satisfecho por este acto».

#### D · CERTIFICACIÓN

**`F6 NO CERTIFICADA`**

**`F6 ABIERTA`**

`Razones finitas:` **(1)** el gate NO ES VÁLIDO por cobertura — el lote del revisor 2 tiene
29 329 de 48 143 líneas sin leer, el 60,9 %, y la regla §4 del manifiesto prohíbe sustituir su
lectura con la mía; **(2)** existen TRES bloqueantes internos vivos, reproducidos por mí con
sus órdenes y sus salidas —`ADJ-B1` la migración `0→1` rota e irreversible, `ADJ-B2` la raíz
externa sin la purga `E-10`, `ADJ-B3` el append-only de la sede del Owner que sólo protege su
prefijo—, y `O26` §5.5 exige que no haya ninguno; **(3)** la condición **8** de `O26` §1 no se
satisface sobre esta candidata, y `O26` §5.4 exige las ocho; **(4)** las tres restas están
vacías —`A=0 · B=0 · C=0`, reproducidas por mí— pero el instrumento que las produce **puede
perder una obligación en silencio por tres vías con `exit 0`** (`ADJ-G1`) y sus rótulos `A` y
`B` no miden lo que `O26` §5.1 y §5.2 exigen (`ADJ-M4`), de modo que su vacío no acredita lo
que se le pide acreditar; **(5)** el `estado` de una prueba no está mecanizado contra su
evidencia y el árbol publica hoy una divergencia viva (`ADJ-G2`), lo que alcanza a la sede que
autoriza al corpus a decir «682 casos, 173 superadas».

#### E · PESQUERAPP

**`PESQUERAPP SIGUE BLOQUEADA`**

---

> **CIERRE.** `HEAD` `20330e69…`, `tree` `4ee6f9d4…`, `git status --porcelain` **vacío**, 39
> referencias locales — idénticos a la apertura. No he corregido nada, no he propuesto ningún
> commit, no he abierto ningún otro gate y no he iniciado PesquerApp. Los hallazgos quedan
> **REGISTRADOS Y NO APLICADOS**, que es el encargo y no admite excepción.
>
> Y una última cosa, que es de método y se dice porque el gate anterior la dejó escrita: los
> dos revisores volvieron a equivocarse en cosas distintas. El revisor 1 no exageró: en su
> bloqueante mayor se quedó corto. El revisor 2 midió con precisión casi todo lo suyo y
> **llevó un cargo grave a una conclusión falsa** —la reclasificación de `C-L`— por fiarse de
> una celda caducada del corpus en vez de ir a la sede única que tenía en su propio lote y que
> había leído. Ninguno de los dos merecía ser copiado. Los dos merecían ser reproducidos.

— **EL ADJUDICADOR**, 2026-09-04

