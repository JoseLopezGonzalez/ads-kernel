# 07 · GUÍA OPERATIVA DE `F6`

**La única guía vigente para construir, ejecutar, validar y diagnosticar `F6` sin
reconstruir su estado leyendo la sucesión de gates.** La exige `O30` §8, en la
[sede canónica del Owner](../owner/ADS-OWNER-RESOLUCIONES.md).

Antes: [`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](06-DEUDA-Y-LIMITACIONES-VIGENTES.md).

> **QUÉ ES.** Un mapa de entrada para un implementador NUEVO: qué es `F6`, dónde vive cada
> pieza, con qué comando se ejecuta y se valida, y qué hacer cuando algo sale rojo.
>
> **QUÉ NO ES.** No es norma, no es un gate, no certifica nada y **no crea autoridad**. No es
> sede de estado de fase, no es sede de lo construido, no es sede de deuda y no es la
> cronología del expediente —de eso ya hay bastante—. Cada una de esas cuatro cosas tiene su
> sede, y aquí se **remite**.
>
> **Y NO COPIA NINGÚN RECUENTO.** Donde hace falta una cifra, esta guía publica el comando
> que la deriva. La regla no es estética: este corpus ha arrastrado cinco veces cifras
> caducadas escritas a mano, y `T360` —en
> [`validadores/comprobar_recuentos.py`](../../kernel/operativo/validadores/comprobar_recuentos.py)—
> existe por eso.

---

## 0 · Las cuatro cosas que esta guía mantiene separadas

```text
NORMA           lo aprobado por el Owner y lo que instancia. Manda. No se resume aquí
IMPLEMENTACIÓN  el código que ejecuta la norma, con su contrato derivado al lado
EVIDENCIA       lo que una ejecución produjo: baterías, escenarios, gates, dictámenes
HISTORIA        cómo se llegó hasta aquí. Se conserva, se cita y NO se usa como manual
```

**Un documento de gate no es fuente normativa y no es manual operativo.** La regla y su
alcance viven en [`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md) §4.1.

## 1 · Propósito y fronteras de `F6`

**`F6` construye el último eslabón antes de la certificación:** el sistema que EJECUTA la
norma de ADS —estado durable, runtime y despacho, gobierno Git del repositorio de control,
verificador de admisión, adaptadores, raíz externa de confianza y contención— sobre un
producto real.

```text
DENTRO DE F6   el motor de estado durable · el runtime y su dispatcher · el ciclo de §7.2 y
               los cuatro macrocircuitos · el gobierno Git del CONTROL repo · el verificador
               de admisión · los adaptadores · la identidad y la raíz externa · la contención

FUERA DE F6    la especificación normativa, que es de (a), (b) y (g) y sólo se enmienda
               el diseño del producto y su stack
               la CERTIFICACIÓN, que es un acto independiente y NO de quien construye
               la primera adopción real —PesquerApp—, que necesita una orden separada
```

El alcance por fases y el grafo de dependencias están en
[`05-PLAN-DE-IMPLEMENTACION-F5-F6.md`](05-PLAN-DE-IMPLEMENTACION-F5-F6.md); la norma de la
materia, en la sección [`(g)`](../rediseno/g-ESTADO-DURABLE-APROBADA.md), aprobada por `O23`.

## 2 · Componentes implementados — dónde se lee, y por qué no se lee aquí

**Esta guía no publica una tabla de implementación.** Habría dos y una de ellas envejecería.

| lo que buscas | su ÚNICA sede |
|---|---|
| qué está CONSTRUIDO y qué sólo DISEÑADO | [`04-CONTRATOS-TECNICOS.md`](04-CONTRATOS-TECNICOS.md) §1 |
| el reparto contrato a contrato de `F6`, con su clasificación cerrada | [`docs/f6/00-ESTADO-DE-IMPLEMENTACION-F6.md`](../f6/00-ESTADO-DE-IMPLEMENTACION-F6.md) §3 |
| obligación a obligación, con su condición de cierre | [`docs/f6/01-MATRIZ-DE-COMPLETITUD-F6.md`](../f6/01-MATRIZ-DE-COMPLETITUD-F6.md) |
| deuda viva, con propietario, fase y condición de cierre | [`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](06-DEUDA-Y-LIMITACIONES-VIGENTES.md) |
| el estado de las fases | [`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md) §6 |

**Y el universo contra el que se mide no se escribe: se deriva.**

```bash
/home/jose/.local/bin/python3.12 docs/evolucion/verificacion/derivar-universo-obligatorio.py --obligaciones
```

> **`IMPLEMENTADO_Y_PROBADO` no es `CERTIFICADO`.** Es la confusión que más veces ha
> reaparecido en este expediente. Ninguna tabla de implementación, ni un verde de la batería,
> ni esta guía, certifican nada.

## 3 · Arquitectura del runtime

**Todo lo que ejecuta vive bajo `kernel/operativo/runtime/`, y ese directorio tiene su propio
índice:** [`00-RUNTIME.md`](../../kernel/operativo/runtime/00-RUNTIME.md). Es la entrada
técnica; esta sección sólo dice cómo está partido y dónde está el contrato de cada parte.

| parte | qué hace | contrato derivado |
|---|---|---|
| `estado/` | transacción, diario, reconciliación, migración, bloqueo, rutas, atestación y puntos de fallo | [`CONTRATO-ESTADO-DURABLE.md`](../../kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md) |
| `runtime/` | trabajo elegible, autoridad temporal, despacho, reintentos y vistas derivadas | [`CONTRATO-RUNTIME-Y-DISPATCHER.md`](../../kernel/operativo/runtime/CONTRATO-RUNTIME-Y-DISPATCHER.md) |
| `ciclo/` · `macrocircuitos/` | las ocho etapas de `§7.2`, `Continúa` de `§7.4` y los cuatro macrocircuitos con su `FASE 0` | [`CONTRATO-CICLO-Y-MACROCIRCUITOS.md`](../../kernel/operativo/runtime/CONTRATO-CICLO-Y-MACROCIRCUITOS.md) |
| `gobierno/` | propiedad de refs, concesión y prohibición de forzar sobre el repositorio de CONTROL | [`CONTRATO-GOBIERNO-GIT-CONTROL.md`](../../kernel/operativo/runtime/CONTRATO-GOBIERNO-GIT-CONTROL.md) |
| `admision/` | los cortes del verificador de admisión: lectura segura, juicio por mutación, perímetro y matriz | [`CONTRATO-ADMISION.md`](../../kernel/operativo/runtime/CONTRATO-ADMISION.md) |
| `adaptadores/` | interfaz, adaptador local real, proyección y validador de deriva | [`CONTRATO-ADAPTADOR.md`](../../kernel/operativo/runtime/CONTRATO-ADAPTADOR.md) |
| `identidad/` | la identidad del firmante y del verificador, y su ciclo de vida | [`CONTRATO-RAIZ-EXTERNA.md`](../../kernel/operativo/runtime/CONTRATO-RAIZ-EXTERNA.md) |
| `arboles/` | el derivador del conjunto de árboles adversariales y su suite de regresión | [`CONTRATO-ARBOLES-ADVERSARIALES.md`](../../kernel/operativo/runtime/CONTRATO-ARBOLES-ADVERSARIALES.md) |
| `contencion/` | detección de mecanismos del anfitrión, política, ejecutor y fallo cerrado | [`CONTRATO-CONTENCION.md`](../../kernel/operativo/runtime/CONTRATO-CONTENCION.md) |
| `pruebas/` | las baterías y los escenarios extremo a extremo | — |

**El censo de módulos y de baterías no se escribe: se deriva.**

```bash
ls -1 kernel/operativo/runtime/*.py           | xargs -n1 basename   # puntos ejecutables
ls -1 kernel/operativo/runtime/estado/*.py    | xargs -n1 basename   # el motor, fichero a fichero
ls -1 kernel/operativo/runtime/pruebas/test_*.py kernel/operativo/runtime/pruebas/escenario_*.py
```

## 4 · Estado durable, diario, recuperación y reconciliación

**El tiempo lógico es la REVISIÓN, no el reloj.** Una escritura se publica bajo
*compare-and-swap* sobre la revisión esperada, de modo que dos escritores no pueden confirmar
la misma revisión, y el orden contractual —preparar, publicar, confirmar— se conserva.

```text
TRANSACCIÓN     prepara fuera de sitio y publica con un reemplazo atómico
DIARIO          registra la intención antes del efecto; detecta corrupción, truncamiento,
                sustitución y retirada de cola
RECUPERACIÓN    reanuda desde el diario; repetirla es IDEMPOTENTE y no duplica efectos
RECONCILIACIÓN  sólo se cierra por una transición autorizada y auditable, nunca por
                observación ni por un arreglo manual
MIGRACIÓN       versiona el formato, usa errores tipados y falla CERRADA ante un formato
                desconocido o un estado imposible
```

El mecanismo exacto, con sus puntos de fallo controlados y lo que expresamente NO cubre, está
en [`CONTRATO-ESTADO-DURABLE.md`](../../kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md)
y en [`CONTRATO-RUNTIME-Y-DISPATCHER.md`](../../kernel/operativo/runtime/CONTRATO-RUNTIME-Y-DISPATCHER.md).

## 5 · Dispatcher, agentes, modelos, slots e inanición

**El dispatcher decide QUÉ es elegible y QUIÉN tiene la autoridad temporal para ejecutarlo;
no decide quién ocupa un rol.** Eso lo deciden la política de modelos de
[`C2`](../../kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md) y la materialización de
[`C4`](../../kernel/operativo/contratos/C4-MATERIALIZACION.md).

```text
ELEGIBILIDAD    se deriva del estado durable, no de una lista escrita a mano
AUTORIDAD       es TEMPORAL y se concede por revisión; caduca y se puede retirar
SLOTS           `execution_slots` corta por AGENTE, que es su unidad. Lo que no cabe QUEDA
                EN COLA: está PROHIBIDO reducir la composición declarada para que quepa
MODELO          se elige por la política de C2 rol a rol, y los descartados se publican
                con el motivo y la regla que los produjo
INANICIÓN       es una VISTA derivada —quién lleva más esperando—, y la antigüedad se mide
                con el reloj LÓGICO. Adelantar por antigüedad NO altera ninguna prioridad
                contractual, ni directamente ni por una secuencia de transiciones
```

## 6 · Gobierno Git del repositorio de control

**El repositorio de CONTROL tiene propiedad declarada por ref, concesión explícita y
prohibición de forzar**, y la prohibición se demuestra en sus dos mitades: **imposible** —el
hook rechaza el forzado, incluido el OID nulo— y **detectable** —el linaje durable denuncia un
forzado aunque alguien hubiera quitado el hook—. La serialización se ejerce entre escritores
locales **y entre máquinas**, con remoto *bare*, dos clones y dos identidades distintas.

Sede: [`CONTRATO-GOBIERNO-GIT-CONTROL.md`](../../kernel/operativo/runtime/CONTRATO-GOBIERNO-GIT-CONTROL.md)
y la política en `kernel/operativo/runtime/gobierno/POLITICA-CONTROL-REPO.yml`. El gobierno
Git del PRODUCTO —multi-fuente— es otra cosa y vive en
[`C7`](../../kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md).

## 7 · Raíz externa, firma, aislamiento y contención

**La raíz externa vive FUERA del árbol que juzga, y por eso no viaja dentro de `runtime/`:**
su paquete es `kernel/operativo/raiz-externa/`, y se instala fuera del árbol verificado.

```text
FIRMA           ASIMÉTRICA. El verificador NO tiene la clave privada
ATESTACIÓN      ligada SIMULTÁNEAMENTE al SHA del commit y a su tree
SEPARACIÓN      firmante y verificador son componentes distintos, y el ejecutor de la raíz
                no comparte capacidad de escritura sobre el control repo con el runtime
CICLO DE VIDA   rotación, solapamiento por épocas, retirada y revocación
FALLO CERRADO   clave desconocida, firma inválida, commit o tree incorrectos, ausencia de
                proveedor y contaminación del entorno terminan en rojo, nunca en degradación
```

Ésas son las ocho condiciones de `O26` §1, y se ejercen sobre la candidata por su canal real:

```bash
/home/jose/.local/bin/python3.12 docs/evolucion/verificacion/ejercer-o26-condiciones.py
```

**La contención es otra materia y tiene su propio contrato.** Alcanza al proceso **y a sus
descendientes**, incluidos los que intenten escapar creando una sesión nueva con `setsid`.
Sede: [`CONTRATO-CONTENCION.md`](../../kernel/operativo/runtime/CONTRATO-CONTENCION.md) ·
identidad y custodia: [`CONTRATO-RAIZ-EXTERNA.md`](../../kernel/operativo/runtime/CONTRATO-RAIZ-EXTERNA.md).

## 8 · Verificador de admisión

**Juzga la MUTACIÓN efectiva, no la existencia de un fichero**, lee por un canal único y
seguro, deriva el perímetro en vez de declararlo, **se incluye a sí mismo** en lo que juzga y
falla cerrado ante cualquier cambio fuera del universo permitido.

```bash
/home/jose/.local/bin/python3.12 kernel/operativo/runtime/ads_admision.py --repo <dir> verificar --base <rev>
/home/jose/.local/bin/python3.12 kernel/operativo/runtime/ads_admision.py --repo <dir> censo-zonas
```

Sede: [`CONTRATO-ADMISION.md`](../../kernel/operativo/runtime/CONTRATO-ADMISION.md), donde
está además su deuda declarada.

## 9 · El catálogo `K01`–`K24`

**El universo crítico de la certificación de `F6` es un catálogo CERRADO de veinticuatro
invariantes arquitectónicos.** Su fuente normativa —y la única que puede cambiarlo— es `O30`
§2, en la [sede canónica del Owner](../owner/ADS-OWNER-RESOLUCIONES.md). **Esta guía no lo
copia**: si el corpus publica además una sede propia del catálogo, se enlaza desde aquí y la
fuente normativa sigue siendo la misma. Dos listas de invariantes serían dos verdades.

```text
CERRADO         un verificador sólo puede proponer `K25` demostrando un efecto material que
                no se pueda adscribir honestamente a ninguno de los veinticuatro. Cambiar la
                redacción, la ruta, el nombre de una prueba o la instancia NO crea invariante

EVIDENCIA       cada `Knn` necesita las ocho piezas de `O30` §3: fuente normativa, mecanismo,
                canal productivo ejercido, caso sano, prueba adversarial capaz de ponerlo
                rojo, resultado esperado del sabotaje, evidencia reproducible y vínculo al
                commit y al tree juzgados

COMPARTIR       una misma prueba adversarial puede cubrir varios invariantes SÓLO con las
                cuatro condiciones de `O30` §3. No se exige un mutante por cláusula
```

**Y el cardinal tampoco se escribe aquí.** Se deriva de la sede:

```bash
grep -cE '^- `K[0-9]{2}` ·' docs/owner/ADS-OWNER-RESOLUCIONES.md
```

> **La unidad de medida anterior quedó corregida.** `O30` §1 rechaza expresamente la
> clasificación de criticidad por coincidencias léxicas y la exigencia de un sabotaje por
> cláusula. Las mediciones de `O26-SAB` **siguen siendo evidencia histórica de lo que aquel
> instrumento contó**, y **ya no gobiernan** la certificación. Que no gobiernen no las
> declara falsas ni satisfechas: cambia con qué se decide.

## 10 · Instalación y actualización

**Un ADS Project gobierna un PRODUCTO, no un repositorio**, y se crea con el tooling del
kernel. El procedimiento completo, paso a paso, está en
[`START_HERE.md`](../../START_HERE.md); el mapa del repositorio, en
[`README.md`](../../README.md).

```bash
./tooling/new-project.sh mi-producto web-app        # crea el ADS Project y su commit inicial
python3 tooling/workspace.py check                  # ¿está bien declarado, y qué hay en disco?
python3 tooling/workspace.py init                   # clona lo que falte; reutiliza lo que hay
python3 tooling/workspace.py status                 # una línea por fuente
./tooling/kernel-status.sh                          # ¿ha divergido la copia del kernel?
```

**La actualización no se hace editando la copia congelada del kernel.** Si hace falta otro
comportamiento, la vía es un **override declarado** en el `PROFILE`; `kernel-status.sh`
detecta la divergencia sobre `kernel/`, `packs/` y `tooling/`, **incluidos los validadores en
Python**, porque relajar una regla editando `ads_lint.py` sería un fork invisible.

## 11 · Comandos de ejecución y validación

**Requisito de entorno, y no se puede relajar.** La guarda vive en
`kernel/operativo/validadores/entorno.py` y corre **antes** que nada. Un entorno insuficiente
termina con código **`78`**, distinto del `1` de «una comprobación no pasó»: un entorno que no
llega **no puede confundirse con un producto roto**. En esta máquina el intérprete que cumple
es `/home/jose/.local/bin/python3.12`.

```bash
# el motor de estado durable, sobre un repositorio de control
/home/jose/.local/bin/python3.12 kernel/operativo/runtime/ads_estado.py --repo <dir> inicializar
/home/jose/.local/bin/python3.12 kernel/operativo/runtime/ads_estado.py --repo <dir> verificar

# el runtime: trabajo elegible, autoridad y despacho por un adaptador real
/home/jose/.local/bin/python3.12 kernel/operativo/runtime/ads_runtime.py --repo <dir> --instancia runtime-A elegibles
/home/jose/.local/bin/python3.12 kernel/operativo/runtime/ads_runtime.py --repo <dir> --instancia runtime-A --adaptador-local <espacio> ciclo

# el ciclo de §7.2 y el derivador de árboles adversariales
/home/jose/.local/bin/python3.12 kernel/operativo/runtime/ads_ciclo.py --ayuda
/home/jose/.local/bin/python3.12 kernel/operativo/runtime/ads_arboles.py suite
```

**La batería no se enumera aquí: se descubre.** La lista canónica de qué se ejecuta, qué se
espera de cada componente y qué evidencia publica es
[`validadores/validadores.yaml`](../../kernel/operativo/validadores/validadores.yaml), y quien
la ejecuta y publica su evidencia es el runner —**no un bucle de shell escrito a mano**, que
es exactamente el defecto que lo hizo existir—:

```bash
# el corpus: todos los validadores del manifiesto, con su evidencia publicada
/home/jose/.local/bin/python3.12 kernel/operativo/validadores/registrar_evidencia.py

# los dos que cualquier cambio documental tiene que dejar en verde
/home/jose/.local/bin/python3.12 kernel/operativo/validadores/ads_lint.py
/home/jose/.local/bin/python3.12 kernel/operativo/validadores/comprobar_referencias.py

# el runtime: cada batería y cada escenario extremo a extremo
ls -1 kernel/operativo/runtime/pruebas/test_*.py kernel/operativo/runtime/pruebas/escenario_*.py \
  | xargs -n1 /home/jose/.local/bin/python3.12
```

> **Un verde de la batería del CORPUS no dice nada sobre si el runtime funciona, y al
> revés.** Son dos aparatos distintos: los validadores comprueban la consistencia del corpus;
> las baterías de `runtime/pruebas/` administran el estado de un producto.

## 12 · Diagnóstico de fallos

```text
CÓDIGO 78            entorno insuficiente. NO es un defecto del producto: es un intérprete
                     por debajo del mínimo declarado. Se corrige el intérprete, no el código

CÓDIGO 5             procedencia no fiable en el arranque. Falta la guarda de aislamiento
                     junto al punto ejecutable o en el `validadores/` de un ancestro

CÓDIGO 1             una comprobación no pasó. Se lee la salida, que nombra la prueba

ERROR TIPADO         todo fallo del motor sale por una clase con un `codigo` ESTABLE en
                     MAYÚSCULAS, más `detalle`, `ruta` y un `contexto` ordenado. El código
                     es el contrato: una prueba lo compara sin depender del texto castellano

NUNCA                `except Exception: pass`, ni un `assert` como control de flujo, ni una
                     degradación silenciosa cuando falta aislamiento, firma, identidad,
                     backend o capacidad. La ausencia de una capacidad se dice y falla
```

```text
SÍNTOMA                                  →  DÓNDE MIRAR PRIMERO
un validador «pasa» sin haber corrido    →  la firma de éxito del componente en validadores.yaml
la huella cambia sin tocar nada          →  contaminación del entorno; kernel-status.sh y la guarda
el adaptador no ejecuta                  →  contención: no hay backend fuerte y falla CERRADO
un enlace del corpus se rompe            →  comprobar_referencias.py nombra fichero, línea y ruta
una cifra del corpus no cuadra           →  no se corrige la cifra: se sustituye por su comando
```

## 13 · Límites externos, dichos sin universalizarlos

**Un límite del anfitrión se registra con exactitud y no se convierte en una ley general.** Si
existe un backend disponible capaz de ejercer una condición, hay que usarlo.

```text
CUSTODIA PRODUCTIVA   EXTERNA por resolución competente. En este árbol la clave de firma es
DE LA CLAVE           un fichero `0600` fuera de los repositorios, generado efímero. Eso NO
                      es custodia productiva, y ninguna salida puede afirmar que lo sea.
                      PROPIETARIO: el Owner. CIERRE: una instalación real que firme contra un
                      proveedor de secretos del anfitrión, con rotación y revocación EJERCIDAS

CONTENCIÓN FUERTE     depende del anfitrión. Donde no haya ninguno de los mecanismos, lo
                      demostrado es la DETECCIÓN y el FALLO CERRADO, y se dice así en vez de
                      prometer un aislamiento que ese anfitrión no puede dar

USUARIO DEL SISTEMA   la identidad sin escritura se demuestra con contenedor o con espacio de
DEDICADO              nombres. Una cuenta de servicio dedicada es aprovisionamiento del
                      anfitrión: REQUISITO DE INFRAESTRUCTURA, no deuda de este código

NIVEL DE ADAPTADOR    el nivel se DERIVA, no se presupone. La evidencia que lo subiría exige
                      fuentes reales, y eso es la primera adopción real, que está bloqueada
```

El registro completo, con propietario, fase y condición de cierre de cada uno, vive en
[`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](06-DEUDA-Y-LIMITACIONES-VIGENTES.md), que es su sede.

## 14 · Estado de certificación — la remisión, y lo que es cierto hoy

**La sede del estado de las fases es
[`03-GOBIERNO-Y-AUTORIDAD.md`](03-GOBIERNO-Y-AUTORIDAD.md) §6, y esta guía no la duplica.**
Un implementador nuevo necesita ese estado antes de tocar nada, y por eso esta guía dice
CÓMO LEERLO, no cuál es: escribirlo aquí crearía una segunda sede mutable que ningún
validador contrasta —el sello detectaría el cambio, pero no la contradicción—, que es
justo lo que `O30` §8 prohíbe. Se deriva:

```bash
$ sed -n '/^## 6 /,/^## 7 /p' docs/canonico/03-GOBIERNO-Y-AUTORIDAD.md
```

**Quién puede cambiarlo, y con qué prueba.** Sólo **un verificador independiente**, y sólo si
concurren TODAS las condiciones de `O30` §7: `K01`–`K24` satisfechas, ninguna obligación
interna de `F6` sin implementar, las ocho condiciones de `O26` ejercidas y satisfechas,
`M-04 SUPERADA`, `C-L.7 CERRADA`, ningún defecto BLOQUEANTE o GRAVE que invalide el objeto o
su evidencia, identidad exacta del commit y el tree juzgados, y sobre de ancla emitido antes
de crear al verificador.

> **`M-04` y `C-L.7` no se cierran con una etiqueta escrita por quien implementa** —`O30`
> §6—: el verificador independiente los juzga y emite su veredicto **por separado y con
> causa**. Su estado vigente NO se escribe aquí por lo dicho arriba: su sede es
> [`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](06-DEUDA-Y-LIMITACIONES-VIGENTES.md), y se lee
> con `grep -n 'M-04\|C-L.7' docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md`.

## 15 · Qué habilita y qué NO habilita el cierre

```text
SI F6 QUEDA CERTIFICADA Y CERRADA
  desaparece EXCLUSIVAMENTE el bloqueo técnico que dependía de completar y certificar F6
  PesquerApp queda:  HABILITADA TÉCNICAMENTE · NO AUTORIZADA · NO INICIADA

LO QUE NO HABILITA
  su adopción, su piloto, su integración y su ejecución necesitan una orden POSTERIOR y
  SEPARADA del Owner. Este ciclo no puede iniciarla

SI F6 NO QUEDA CERTIFICADA
  PesquerApp continúa BLOQUEADA
```

Fuente: `O30` §9. Y `O30` §10 cierra el método: tras el dictamen se registra y se publica el
resultado, **no se corrige la candidata en respuesta al dictamen**, no se abre otro gate, no
se propone otra tanda automática y no se inicia PesquerApp.

## 16 · La historia: los gates como evidencia, y las contradicciones resueltas

**Ninguno de los documentos de esta sección es lectura necesaria para implementar `F6`.** Se
citan como **evidencia histórica** —qué se juzgó, cuándo y con qué resultado—, nunca como
manual operativo, y **no se reescriben ni se fusionan**.

| evidencia | qué dejó dicho |
|---|---|
| [`02-GATE-DE-CERTIFICACION-FINAL-20260903.md`](../f6/02-GATE-DE-CERTIFICACION-FINAL-20260903.md) | `F6 NO CERTIFICADA`, sobre un gate declarado **NO VÁLIDO** por cobertura |
| [`03-GATE-DE-CERTIFICACION-FINAL-20260904.md`](../f6/03-GATE-DE-CERTIFICACION-FINAL-20260904.md) | ídem: **NO VÁLIDO** por cobertura |
| [`gate-final-20260905/00-REGISTRO-DEL-GATE.md`](../f6/gate-final-20260905/00-REGISTRO-DEL-GATE.md) | **el gate ES VÁLIDO** —por primera vez— y aun así **`F6` NO queda certificada** |

**Cómo se resuelven las contradicciones que un lector va a encontrar.** Por **autoridad** y
por **vigencia**, y remitiendo: no se toca ninguno de los documentos citados.

```text
LA TABLA DE `(g)` §17 dice «NO CONSTRUIDO» de sus contratos derivados
  → describe el estado EN LA FECHA DE SU APROBACIÓN. `(g)` es norma aprobada, no un ledger
    de implementación, y editarla por una razón que no es normativa sería reescribirla.
    Vigente: la sede de lo construido, 04-CONTRATOS-TECNICOS.md §1

«LOS DOS GATES SE DECLARARON NO VÁLIDOS» — enumeración anterior al 2026-09-05
  → es exacta para los gates que existían cuando se escribió. El gate del 2026-09-05 SÍ es
    válido, y su veredicto NO certifica. La CONCLUSIÓN de fase no cambia por eso, y su única
    sede sigue siendo 03-GOBIERNO-Y-AUTORIDAD.md §6: `F6` ABIERTA y NO CERTIFICADA

LAS MEDICIONES DE `O26-SAB` frente al catálogo `K01`–`K24`
  → manda `O30` §2 y §1, que es posterior y de autoridad superior. Aquéllas quedan como
    evidencia histórica de lo que aquel instrumento contó

UN GATE QUE PARECE FIJAR NORMA
  → no puede. 03-GOBIERNO-Y-AUTORIDAD.md §4.1 lo prohíbe expresamente
```

> **Y una regla de esta guía contra sí misma.** Si algo de aquí contradijera a una resolución
> del Owner, a la especificación aprobada o a la sede de la materia, **el defecto es de esta
> guía** y se corrige aquí. Esta guía no crea autoridad y no certifica nada.
