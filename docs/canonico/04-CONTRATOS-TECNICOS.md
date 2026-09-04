# 04 · CONTRATOS TÉCNICOS

El inventario de lo implementable: qué contratos existen, dónde está cada uno, qué está
CONSTRUIDO y qué sólo está DISEÑADO.

> **ESTE DOCUMENTO NO COPIA NINGÚN CONTRATO.** Cada uno tiene una sola sede, y aquí se
> enlaza y se explica su papel. Copiar un contrato en dos sitios crea una segunda verdad que
> envejece sin que nadie lo note.

Antes: [`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md).

---

## 1 · LO CONSTRUIDO Y LO DISEÑADO — la sede de esta distinción

> **ÉSTA ES LA ÚNICA SEDE de la distinción entre construido y diseñado dentro del corpus
> canónico.** Los demás documentos remiten aquí.

### 1.1 · CONSTRUIDO, versionado y ejecutable hoy

```text
kernel/operativo/     el corpus operativo entero: esquemas, contratos, capacidades, roles,
                      métodos, prompts, composiciones, entrada, diseño, recorrido,
                      circuitos, plantillas, pruebas y validadores
kernel/operativo/     el MOTOR DE ESTADO DURABLE de `F6` y su contrato derivado: estado
runtime/              canónico, diario canónico y registro operativo auxiliar como TRES
                      estructuras separadas · protocolo transaccional atómico y durable ·
                      recuperación con sus dos ramas · bloqueo entre escritores ·
                      integridad por contenido con fallo cerrado · versionado y migración
                      explícita · interfaz de atestación externa con proveedores
                      intercambiables. Con punto ejecutable y batería propia. Evidencia
                      publicada: `evidencia/estado-durable-salida.txt` y
                      `evidencia/estado-e2e-salida.txt`
                      Y SOBRE ÉL, el segundo corte: RUNTIME Y DISPATCHER con autoridad
                      temporal, reintentos y vistas derivadas · GOBIERNO GIT del control
                      repo con su tabla de propiedad y `G-A8` en sus dos mitades ·
                      VERIFICADOR DE ADMISIÓN `V2`–`V5`, que cierra `S1-02` ·
                      ADAPTADORES con un ejecutor local real y proyecciones con huella ·
                      IDENTIDAD de firma externa según `O25`. Evidencia publicada:
                      `evidencia/runtime-salida.txt` · `evidencia/gobierno-git-salida.txt` ·
                      `evidencia/admision-salida.txt` · `evidencia/adaptadores-salida.txt` ·
                      `evidencia/identidad-salida.txt` · `evidencia/e2e-runtime-salida.txt`
packs/                los packs instalables y su regla de precedencia
tooling/              creación de proyecto · materialización del workspace multi-fuente ·
                      huella e integridad · preparación de la recompilación de proyecciones
validadores           ejecutables, con manifiesto canónico, evidencia publicada y una
                      batería de CONTROLES NEGATIVOS que muta copias temporales del
                      repositorio y exige que la comprobación señalada FALLE
guarda de entorno     la versión mínima del intérprete, declarada una vez y comprobada
                      ANTES de correr, con código de salida propio. Cierra `A14` —que es
                      el CONTRATO 3 de `11-ARQ` §19—. **Y una divergencia declarada**: §19
                      prescribe para esa guarda el código de salida **2** y `entorno.py`
                      usa el **78** (`EX_CONFIG`), con su motivo escrito: el 2 es «me han
                      invocado mal». La sede del código es `entorno.py`; §19 no se enmienda
kernel/operativo/     el CICLO de `§7.2` entero —encuadre, composición de rutas,
runtime/ciclo/        materialización de equipos con `C4`, gates de capa con su censo
                      derivado, handoffs, cierre, continuación y planificación—, con punto
                      ejecutable `ads_ciclo.py`. Evidencia: `evidencia/ciclo-salida.txt`
kernel/operativo/     instalación, adopción, migración y actualización.
runtime/              Evidencia: `evidencia/macrocircuitos-salida.txt`
macrocircuitos/
kernel/operativo/     la RAÍZ EXTERNA como PAQUETE SEPARADO, con instalador y anfitrión
raiz-externa/         firmante. Evidencia: `evidencia/raiz-externa-salida.txt`
la PRUEBA DE HUMO     `runtime/pruebas/test_sesion_nueva.py`, en un proceso nuevo de verdad,
EN SESIÓN NUEVA       con el NIVEL alcanzado DERIVADO de las celdas de cobertura.
                      Evidencia: `evidencia/sesion-nueva-salida.txt`
las CUATRO            de las obligaciones de fase `F6` de `11-ARQ` §19: el censo derivado
OBLIGACIONES DE §19   (CONTRATO 1), el censo de perfiles de agente (CONTRATO 1bis), el
                      alcance derivado de `T152` (CONTRATO 2) y el gate de composición de
                      `D104`, con `composicion-incompleta` como error que impide cerrar.
                      Evidencia: `evidencia/composicion-procesos-salida.txt`.
                      **Lo que de `D104` NO está materializado se dice en §1.2**
```

> **Y la frontera, para que no se lea de más.** `kernel/operativo/runtime/` **administra el
> estado de un producto**; los validadores comprueban la **consistencia del corpus**. Son
> cosas distintas, y un verde de la segunda **no dice nada** sobre la primera. Ninguna de las
> dos está CERTIFICADA: la certificación de `F6` la emite un juicio independiente y **no
> quien construyó**.

### 1.2 · DISEÑADO Y NO CONSTRUIDO

> **ESTA SECCIÓN ERA FALSA, y lo era en los DOS SENTIDOS.** Se corrige aquí, que es su
> única sede. Decía «NO CONSTRUIDO» de siete cosas que el árbol construye y cuya evidencia
> el propio repositorio publica —el ciclo de `§7.2`, la materialización de equipos, los
> gates de capa, los macrocircuitos, la prueba de humo en sesión nueva, la raíz externa y
> los dos últimos puntos del verificador de admisión—, **y se contradecía con su propia
> §1.1** en la misma página: §1.1 declaraba «ADAPTADORES con un ejecutor local real» y §1.2
> decía «no hay ninguno». El caso más citable era el verificador de admisión: esta sección
> afirmaba que «todo veredicto los publica en su lista `fuera_de_alcance`» cuando
> `runtime/admision/__init__.py` publica hoy `"fuera_de_alcance": {}` **y conserva el campo
> vacío a propósito**, para que «no queda nada fuera» no se confunda con «ya nadie lo
> publica».
>
> **Lo que un documento así rompe no es la redacción: es la lectura.** Una sede que declara
> no construido lo construido gasta el crédito con el que después dice que algo NO está: si
> se equivoca en un sentido, nadie puede fiarse del otro. Por eso la corrección va en los
> dos, y lo que sigue debajo es **más corto y más duro** que lo que sustituye.
>
> **Cómo se comprueba cada línea de esta sección, sin creerle nada a este documento**: cada
> fila nombra su punto ejecutable o su fichero de evidencia; se abre y se ejecuta.

```text
ADAPTADORES DE            existe el CONTRATO, existe un adaptador LOCAL DE PROCESO real, y
    PROVEEDOR             el NIVEL alcanzado se DERIVA de las celdas de cobertura, no se
                          declara. Lo que NO existe es ningún adaptador de PROVEEDOR, y
                          por eso el nivel derivado es `compatible` y nunca `soportado`:
                          no hay ninguna celda `certificacion/integrado` que lo sostenga
`D104` · LOS PARES        `F6` materializa CINCO de los NUEVE pares `<CAP>:revision` que el
    `DOM:revision`        catálogo de `11-ARQ` §19 deriva. Los cuatro de `DOM` NO están, y
                          la razón no es que falte trabajo: `esquemas/proceso.yaml` no
                          admite la variante `DOM:revision`, y ampliar ese conjunto es un
                          ACTO NORMATIVO cuya sede es el esquema. `T273` los publica uno a
                          uno con el error `composicion-incompleta`, que **impide el cierre
                          del gate de composición**
LAS TRES RESTAS DEL       el universo obligatorio de `F6` se deriva —`derivar-universo-`
    UNIVERSO DE `F6`      `obligatorio.py --obligaciones`— y sus tres restas NO están
                          vacías. Mientras no lo estén, `F6` no está completa, y el número
                          exacto no se escribe aquí: se ejecuta
CERTIFICACIÓN DE `F6`     **ninguna.** Implementado y probado NO es certificado. `O26`
                          acepta la ARQUITECTURA bajo OCHO condiciones y **NO certifica
                          ninguna candidata**: su aceptación sólo se vuelve aplicable
                          cuando un gate independiente VÁLIDO demuestre las ocho sobre un
                          SHA exacto. Presentar `O26` como certificación es leerlo al revés
```

**Lo que SÍ está construido y esta sección decía que no, con dónde comprobarlo.** No se
mueve a §1.1 en silencio: se dice que se movió y por qué, para que quien recuerde la
versión anterior sepa que cambió el árbol y no la redacción.

```text
EL CICLO DE `§7.2`        `kernel/operativo/runtime/ciclo/` — encuadre, rutas, equipos,
                          gates, handoffs, cierre, continuación y planificación, con punto
                          ejecutable `ads_ciclo.py`. Evidencia: `evidencia/ciclo-salida.txt`
EQUIPOS MATERIALIZADOS    `runtime/ciclo/equipos.py` ejecuta los siete pasos y las siete
                          prohibiciones de `C4` sobre las composiciones REALES del corpus
GATES DE CAPA             `runtime/ciclo/gates.py`, con el censo DERIVADO de los bloques
                          `ads:gate` del corpus y las seis piezas de `§7.2` aplicadas
LOS MACROCIRCUITOS        `runtime/macrocircuitos/motor.py`.
                          Evidencia: `evidencia/macrocircuitos-salida.txt`
LA PRUEBA DE HUMO         `runtime/pruebas/test_sesion_nueva.py`, en un proceso nuevo de
    EN SESIÓN NUEVA       verdad. Evidencia: `evidencia/sesion-nueva-salida.txt`
RAÍZ EXTERNA              `kernel/operativo/raiz-externa/`, PAQUETE SEPARADO con su
                          instalador y su anfitrión firmante.
                          Evidencia: `evidencia/raiz-externa-salida.txt`
VERIFICADOR DE ADMISIÓN   los DIECINUEVE puntos. `V6-15` y `V6-16` están construidos, y el
                          veredicto publica su PROCEDENCIA en vez de su ausencia
```

> **Qué dejó de estar aquí, y por qué.** «ESTADO PERSISTIDO — no existe ningún directorio de
> estado en el árbol» era cierto hasta el primer corte de `F6` y **ha dejado de serlo**. El
> reparto entre `F6` construido y `F6` pendiente, contrato a contrato, tiene su registro en
> [`docs/f6/00-ESTADO-DE-IMPLEMENTACION-F6.md`](../f6/00-ESTADO-DE-IMPLEMENTACION-F6.md),
> que es DERIVADO de esta sede y no la sustituye. **Derivado quiere decir que no publica
> ningún estado propio**: cuando esta sección se mueve, aquél remite y no se reescribe.

**El reparto de las pruebas entre «escrita» y «ejecutada» NO se escribe: se deriva de su
sede honesta.**

```bash
sed -n '1,25p' kernel/operativo/pruebas/REGISTRO-generado.md
```

**Sede del vocabulario de estados de prueba y de la regla que impide subir de estado por
argumento:** [`pruebas/REGISTRO.md`](../../kernel/operativo/pruebas/REGISTRO.md).

## 2 · Los contratos transversales

**Sede única, con su índice y las garantías que dan juntos:**
[`kernel/operativo/contratos/00-INDICE.md`](../../kernel/operativo/contratos/00-INDICE.md).
**Ningún contrato declara un campo `propietario` explícito: NO CONSTA**, y este documento no
inventa uno. La autoridad de cada materia se lee de la especificación aprobada y de la ficha
de la capacidad correspondiente.

| id | sede | qué fija | entradas → salidas | error característico |
|---|---|---|---|---|
| **C1** | [`C1-EQUIPO-ROL-AGENTE-METODO.md`](../../kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md) | los siete conceptos y el contrato común de rol | perfil de agente → prompt → método → memoria consultada → gate → checkpoint → memoria actualizada | **un rol que declare menos campos que el esquema NO es materializable, y el instalador DEBE rechazarlo** |
| **C2** | [`C2-AGENTES-Y-MODELOS.md`](../../kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md) | perfiles neutrales de proveedor, asignación determinista, combinación y relevo | perfil del rol + catálogo de modelos del producto → asignación registrada, con los modelos descartados y el motivo de cada descarte | si ningún modelo cumple y el perfil no permite degradar, el paquete queda BLOQUEADO nombrando qué capacidad de modelo falta. **No se ocupa el rol a medias** |
| **C3** | [`C3-METODO-EJECUTABLE.md`](../../kernel/operativo/contratos/C3-METODO-EJECUTABLE.md) | qué hace ejecutable a un método, con sus reglas | disparador, carga y preguntas iniciales → artefactos, salida y aprendizaje | devolución · bloqueo · cancelación. **Una comprobación no anotada es una comprobación no hecha**, y un paso NUNCA se salta por decisión del agente |
| **C4** | [`C4-MATERIALIZACION.md`](../../kernel/operativo/contratos/C4-MATERIALIZACION.md) | el algoritmo determinista de materialización, ampliación y retirada de equipos | paquete + composiciones instaladas → el equipo escrito, con qué condición lo eligió y qué roles quedaron fuera y por qué | si ninguna condición se cumple es un DEFECTO DEL CATÁLOGO y se escala. **Lo que no cabe en los slots espera; NO se reduce la composición para que quepa** |
| **C5** | [`C5-HANDOFF.md`](../../kernel/operativo/contratos/C5-HANDOFF.md) | la forma de la entrega entre capacidades y de la devolución | artefactos localizables + checkpoint → custodia transferida, o rechazo con motivo | una devolución sin sus campos **se rechaza como devolución**. A través de la frontera de un repositorio se entrega por REFERENCIA a la revisión exacta, nunca por copia |
| **C6** | [`C6-PRODUCTO-FUENTES-Y-WORKSPACE.md`](../../kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md) | qué es una fuente, un componente y un workspace, y dónde vive cada verdad de un producto multirrepositorio | el manifiesto de composición → el gate de conformidad del workspace | el paquete no se despacha; una fuente ausente deja el trabajo esperando dependencia; un directorio ocupado por otro repositorio es ERROR y **no se resuelve automáticamente** |
| **C7** | [`C7-GOBIERNO-GIT-MULTI-SOURCE.md`](../../kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md) | quién pide, ejecuta, bloquea y verifica cada operación Git, y cómo converge un cambio repartido | paquetes con sus fuentes declaradas → el conjunto de integración y su gate de convergencia | el item NO cierra; si una fuente quedó sin integrar el estado es INTEGRACIÓN PARCIAL, y **la capacidad de entrega no puede declarar el item cerrado** |

**Invariantes transversales que atraviesan varios contratos, y su sede:**

```text
AUTORIDAD SILENCIOSA    lo que no está declarado como decidible NO se decide. Actuar fuera
                        es defecto de conformidad aunque el resultado sea bueno       · C1
SUBCONJUNTO             la autoridad de un rol es SIEMPRE un subconjunto de la de su
                        capacidad. Si necesitara más, el defecto está en el catálogo · C1
INDEPENDENCIA           ningún agente ocupa a la vez un rol productor y su crítico, ni dos
                        roles con veto sobre la misma materia, ni dos declarados
                        independientes. Ante conflicto, MANDA la independencia      · C2·C4
NEUTRALIDAD             ningún fichero del kernel ni de un pack nombra proveedor, modelo
                        comercial ni herramienta de marca como requisito                · C2
DETERMINISMO            mismo paquete y misma composición instalada producen el mismo
                        equipo                                                          · C4
MEMORIA                 nunca se retira. Las memorias no mueren; los equipos sí         · C4
FRONTERA DE CUSTODIA    quien recibe comprueba ANTES de tomar custodia                  · C5
SIN CREDENCIALES        ninguna salida —texto, informe, error o traza— reproduce una
                        credencial                                                  · C6
TODO O NADA             la materialización no empieza mientras el manifiesto tenga
                        cualquier error estático                                        · C6
ESTADO FUERA DE RAMA    el estado del producto no vive en ninguna rama: se calcula en el
                        repositorio de control                                          · C7
```

## 3 · Esquemas: la forma de cada objeto

**Sede del lenguaje canónico —cómo se escribe un bloque, qué tipos hay, qué restricciones
admite un campo y cómo se valida—:**
[`esquemas/00-LENGUAJE.md`](../../kernel/operativo/esquemas/00-LENGUAJE.md).
**Sede de la forma de cada tipo:** un fichero por tipo en
`kernel/operativo/esquemas/<tipo>.yaml`.

**El censo NO se escribe: se deriva.**

```bash
ls -1 kernel/operativo/esquemas/*.yaml | xargs -n1 basename | sed 's/\.yaml$//'
```

**Los que un implementador de `F5`/`F6` necesitará antes que ningún otro:**

| esquema | modela | por qué importa ahora |
|---|---|---|
| `esquema.yaml` | el meta-esquema; se valida contra sí mismo | es el suelo del validador estructural |
| `rol.yaml` | el contrato común de rol | fija los campos que hacen materializable un rol |
| `metodo.yaml` | el procedimiento ejecutable | exige la **prueba de reanudación** como campo obligatorio |
| `proceso.yaml` | el molde de los diez procesos | **no existe un tipo `obligación` aparte, y es deliberado**: la obligación se DERIVA del proceso, y tenerla en dos sitios sería tener dos verdades |
| `gate.yaml` | una lista comprobable de salida | cada comprobación declara si es automatizable |
| `composicion.yaml` | qué roles se materializan y cuáles NO pueden compartir agente | es lo que consume el algoritmo de materialización |
| `perfil-agente.yaml` | exigencia de capacidades de modelo, **sin marca** | es la pieza de neutralidad de proveedor |
| `handoff.yaml` | la entrega entre dos capacidades | forma; las instancias viven en los circuitos |
| `memoria.yaml` | una sección del corpus persistente de un equipo | fija autoridad, caducidad y **qué significa que esté vacía** |
| `integration-set.yaml` | la combinación exacta de revisiones probada junta | es la pieza que hace la integración multi-fuente EVIDENCIADA y no ficticia |
| `escenario.yaml` | una prueba de conformidad, con su estado honesto | es lo que impide que una prueba suba de estado por argumento |

> **Identificadores.** Su gramática es parte del lenguaje canónico y **no se reformula
> aquí**: capacidad, pack, rol, método, gate y el resto tienen su patrón declarado en
> [`00-LENGUAJE.md`](../../kernel/operativo/esquemas/00-LENGUAJE.md), y cada esquema lo
> repite como restricción ejecutable de su campo `id`.

## 4 · Estado, persistencia, reanudación, concurrencia y recuperación

**Cuidado con la frontera: de esta materia hay una parte CONSTRUIDA y otra DISEÑADA.**

| materia | estado | sede |
|---|---|---|
| formato del **checkpoint** que permite reanudar sin hablar con el emisor | **plantilla construida**; su formato normativo vive en la especificación aprobada | [`plantillas/CHECKPOINT.md`](../../kernel/operativo/plantillas/CHECKPOINT.md) |
| **prueba de reanudación** obligatoria en todo método | **construida y comprobada**: es campo obligatorio del esquema y un validador exige que cite un escenario que existe | `esquemas/metodo.yaml` · [`validadores/`](../../kernel/operativo/validadores/validadores.yaml) |
| **relevo de agente** sin perder identidad ni memoria | **contrato construido**, sin runtime que lo ejecute | [`C2`](../../kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md) |
| **reanudación multi-fuente**: qué sabe el checkpoint de cada fuente | **contrato construido**; su prueba está escrita y **no ejecutada** | [`C7`](../../kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md) |
| **memoria** persistente de un equipo | **tipo construido**; hoy sólo una capacidad lo usa con bloques declarados, el resto lo declara en prosa dentro de su ficha | `esquemas/memoria.yaml` · [`diseno/01-MEMORIA-DE-DISENO.md`](../../kernel/operativo/diseno/01-MEMORIA-DE-DISENO.md) |
| **disposición física** del estado durable: instantáneas, eventos, transacciones, concurrencia, identidad, versionado, migración y sellado | **CONSTRUIDA y con batería ejecutada** —evidencia en `evidencia/estado-durable-salida.txt`—; su norma es la sección `(g)`, aprobada, y su mecanismo el contrato derivado. **El sellado del diario queda para el corte siguiente**, y su umbral es parámetro calibrable | [`g`](../rediseno/g-ESTADO-DURABLE-APROBADA.md) · [`CONTRATO-ESTADO-DURABLE.md`](../../kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md) |
| **eventos** como tipo canónico | **DISEÑADO, sin esquema en el kernel** | `11-ARQ` §3.6 |
| **recuperación** tras interrupción, con sus dos ramas y sin mezclas parciales publicables | **CONSTRUIDA y probada matando procesos en las nueve fronteras del protocolo** —evidencia en `evidencia/estado-durable-salida.txt`—; ver [`02-MODELO-OPERATIVO.md`](02-MODELO-OPERATIVO.md) §7 | [`g.8`](../rediseno/g-ESTADO-DURABLE-APROBADA.md) · `11-ARQ` §2.6 y §7.4 |

## 5 · Runtime, runners, adaptadores y verificadores

### 5.1 · Lo ejecutable hoy, y cómo se invoca

| pieza | qué es | invocación |
|---|---|---|
| **el runner canónico** | descubre los validadores del manifiesto, los invoca por ruta completa, captura salida, error y código **por separado**, publica de forma atómica y **NO publica una ejecución con código distinto de cero** | `python3 kernel/operativo/validadores/registrar_evidencia.py` |
| **validador estructural** | esquema de cada bloque, unicidad de identificadores, resolución de referencias, enlaces relativos y vocabulario prohibido — **los enlaces y el vocabulario, en TODO el repositorio** | `python3 kernel/operativo/validadores/ads_lint.py` |
| **controles negativos** | copia el repositorio a un temporal, introduce una infracción deliberada y **exige que la comprobación señalada FALLE, y por el motivo esperado**. Una traza no cuenta como detección | `python3 kernel/operativo/validadores/comprobar_negativos.py` |
| **materializador de workspace** | comprueba y materializa las fuentes declaradas | `python3 tooling/workspace.py {check\|init\|status}` |
| **integridad del kernel vendorizado** | compara la huella almacenada con la calculada; **no recalcula el hash por su cuenta** | `./tooling/kernel-status.sh` |
| **creación de proyecto** | crea el workspace con su repositorio de control e instala los packs pedidos. La especificación normativa que viaja se DERIVA del árbol, no se escribe | `./tooling/new-project.sh <nombre> [packs]` |
| **motor de estado durable** | administra el estado canónico, el diario y el registro auxiliar de un repositorio de control, con transacciones atómicas y recuperación | `python3 kernel/operativo/runtime/ads_estado.py --repo <dir> <orden>` |
| **guarda de entorno** | declara la versión mínima del intérprete y la comprueba ANTES de correr, con código de salida propio | `python3 kernel/operativo/validadores/entorno.py` |

**El manifiesto canónico de validadores —qué hay, qué se espera de cada uno, su firma de
éxito y su regla de vigencia— es
[`validadores/validadores.yaml`](../../kernel/operativo/validadores/validadores.yaml)**, y
es la única sede de esa lista.

> **Requisito de entorno, y es real:** parte del tooling lee el manifiesto de composición con
> la biblioteca TOML de la biblioteca estándar, que **exige un intérprete moderno**; y los
> validadores necesitan el lector de YAML. Con un intérprete antiguo, varias comprobaciones
> fallan por el entorno y **no por el producto** — y, peor, el runner correctamente NO
> republica su evidencia, de modo que la cobertura publicada puede quedar describiendo un
> corpus anterior. **La guarda que lo impide ya es código**, y se comprueba antes de correr:
> [`validadores/entorno.py`](../../kernel/operativo/validadores/entorno.py), con `A14`
> cerrada en [`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](06-DEUDA-Y-LIMITACIONES-VIGENTES.md).

### 5.2 · Evidencia: por qué es determinista y cómo se comprueba

```text
LA EVIDENCIA LA PUBLICA   el runner, y sólo si la ejecución terminó con código cero
NUNCA SE EDITA A MANO     editarla es el defecto que su existencia previene
ES DETERMINISTA           los generados no llevan hora de pared ni duración: mismo estado
                          canónico produce bytes idénticos
CÓMO SE COMPRUEBA         se regenera y el árbol tiene que quedar LIMPIO
Y ADEMÁS                  una cifra publicada que el corpus ya no da se detecta como
                          evidencia CADUCADA, aunque su cabecera, su código y su firma
                          sigan siendo correctos
LA DISCIPLINA             la evidencia derivada se republica en el MISMO commit que cambia
                          el corpus
```

### 5.3 · Adaptadores

**Cuatro piezas diseñadas: definición canónica neutral · proyecciones generadas · huella con
validador de deriva · prueba de humo en sesión nueva.** Sede:
[`11-ARQ` §6](../evolucion/11-ARQUITECTURA-INTEGRADA.md). **Ninguno existe y ninguno está
certificado**; los objetivos de soporte los fijó el Owner y fijar un objetivo no es
alcanzarlo.

### 5.4 · Verificadores

```text
LO QUE HAY HOY      una batería interna que comprueba la CONSISTENCIA DEL CORPUS, con sus
                    controles negativos y su evidencia publicada

LO QUE NO HAY       el VERIFICADOR DE ADMISIÓN y la RAÍZ EXTERNA DE CONFIANZA, que son
                    contrato obligatorio de `F6`

Y LA REGLA          un verde de la batería interna **NO demuestra** que el verificador de
                    `F6` esté construido ni certificado. Nadie puede citarlo para eso
```

## 6 · Los contratos del VERIFICADOR DE ADMISIÓN — escritos, y ninguno implementado

> **Dos familias, y confundirlas sería el error.** Esta sección es la del **verificador de
> admisión**, `F6-A`. Los **contratos DERIVADOS** que la sección `(g)` nombra en su `g.17`
> —estado durable, gobierno Git del control repo y raíz externa— son **otra familia**, con
> otra sede, y el primero de ellos **ya está construido**: ver §1 de este mismo documento.
> Que una familia avance no mueve a la otra.

**Sede única:** [`11-ARQ` §20](../evolucion/11-ARQUITECTURA-INTEGRADA.md). Cada contrato
declara, en su fila: qué debe demostrar `F6` · entrada · salida · evidencia · escenario
POSITIVO · escenario NEGATIVO · condición de BLOQUEO · criterio EXACTO de cierre ·
clasificación.

**Reparto de responsabilidades declarado para esa sección:** la especificación es propiedad
de la capacidad de sistema; la implementación, de la de plataforma; el dosier independiente,
de la de verificación; el bloqueo por seguridad, de la de seguridad; **y la autoridad de
aceptación es del Owner, que la resolución que la creó declara INDELEGABLE**.

**Qué materias cubren, sin copiar sus filas:** lecturas Git inequívocas y con separación
segura · fallo CERRADO ante codificación inválida, truncamiento o estructura inesperada ·
censo de lecturas DERIVADO del código · admisión juzgada sobre la MUTACIÓN y no sobre la
existencia · las seis letras de mutación, con las dos puntas de renombrado y copia ·
comparación de revisión base, cabecera, índice y árbol de trabajo · un cambio ya confirmado
no queda exento · ficheros nuevos y preexistentes · todas las zonas del corpus con condición
declarada · **la regla de admisión no puede excluirse a sí misma** · el contrato
append-only de la sede del Owner comprobado contra su NACIMIENTO · matrices de codificación
y de mutación con fixture positivo y negativo · los árboles adversariales publicados como
fixtures obligatorios · ejecución desde una raíz externa · ningún digest calculado por el
propio árbol basta como prueba de su integridad · **cero falsos verdes y cero falsos rojos**
· y una sola sede por fórmula compartida entre instrumentos.

**El censo y su reparto por clasificación NO se escriben: se derivan.**

```bash
grep -cE '^\| `V6-[0-9]+` \|' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
grep -oE '^\| `V6-[0-9]+`.*\| (`CONTRATO_[A-Z_]+`)' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
  | grep -oE 'CONTRATO_[A-Z_]+' | sort | uniq -c
```

> **NINGUNA de esas filas está implementada, ejecutada ni certificada**, y su propia sede lo
> dice de sí misma. El significado exacto de cada clasificación —y por qué «se puede
> construir» y «está construido» son afirmaciones distintas— está en `11-ARQ` §20.3, y este
> corpus lo resume en
> [`05-PLAN-DE-IMPLEMENTACION-F5-F6.md`](05-PLAN-DE-IMPLEMENTACION-F5-F6.md).

**Un contrato más, escrito para `F6` y fuera de esa sección:** el contrato del **verificador
externo del repositorio de control**, registrado COMPLETO y **no implementado**, en
`11-ARQ` §11.8. Su norma habilitante es entregable de `F5`.

## 7 · Objetos que TODAVÍA NO tienen esquema, y son trabajo de construcción

**Esto no es deuda oculta: es alcance declarado.** Los siguientes objetos están definidos en
prosa o en contrato, y **no tienen fichero de esquema** en el kernel:

```text
equipo · item · paquete · checkpoint · circuito
iniciativa · adaptador · cobertura · evento
contrato-de-aspecto · nivel-certificacion
```

El vocabulario de estados de un paquete **sí existe**, pero vive dentro del esquema del
encuadre y no en un esquema propio: quien construya el tipo `paquete` lo encontrará ahí.

**Consecuencia práctica para `F6`:** crear estos esquemas es parte de la construcción, y
cada uno debe entrar en el lenguaje canónico y en el validador estructural en el mismo
movimiento — **un bloque canónico escrito fuera de las zonas que el validador recorre
quedaría sin validar en silencio**.
