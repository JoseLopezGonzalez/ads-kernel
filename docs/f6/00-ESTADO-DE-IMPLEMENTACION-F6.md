# `F6` · ESTADO DE IMPLEMENTACIÓN

**Qué es este documento.** El registro de **qué está implementado y probado de `F6`, qué no,
y qué lo bloquea**, más las **decisiones técnicas** que `F6` ha tomado bajo la autoridad que
`O24` §2 le reconoce. Es **DERIVADO**: no crea autoridad, no aprueba nada y no certifica
nada.

**Qué NO es.** No es un plan —el plan ya existe y es
[`05-PLAN-DE-IMPLEMENTACION-F5-F6.md`](../canonico/05-PLAN-DE-IMPLEMENTACION-F5-F6.md), y
este documento **no lo repite**—. No es norma: la norma de esta materia es la sección
[`(g)`](../rediseno/g-ESTADO-DURABLE-APROBADA.md). No es la sede del estado de las fases:
ésa es [`03-GOBIERNO-Y-AUTORIDAD.md`](../canonico/03-GOBIERNO-Y-AUTORIDAD.md) §6. Y no es la
sede de lo CONSTRUIDO frente a lo DISEÑADO: ésa es
[`04-CONTRATOS-TECNICOS.md`](../canonico/04-CONTRATOS-TECNICOS.md) §1.

**Acto habilitante:** la resolución `O24`, en la
[sede canónica del Owner](../owner/ADS-OWNER-RESOLUCIONES.md).

---

## 1 · El censo de contratos de `F6` NO se escribe: se deriva

```bash
# los contratos del VERIFICADOR DE ADMISIÓN, con su reparto por clasificación
grep -cE '^\| `V6-[0-9]+` \|' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
grep -oE '^\| `V6-[0-9]+`.*\| (`CONTRATO_[A-Z_]+`)' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
  | grep -oE 'CONTRATO_[A-Z_]+' | sort | uniq -c
# los contratos DERIVADOS que la sección (g) nombra
grep -nE '^\| \*\*contrato de' docs/rediseno/g-ESTADO-DURABLE-APROBADA.md
```

**Dos familias, y confundirlas sería el error.** Los `V6-*` son los puntos del **verificador
de admisión** (`F6-A`), y su sede es `11-ARQ` §20.1. Los **contratos derivados** son los tres
que `g.17` nombra, y su norma es la sección `(g)`. Ninguna de las dos familias se copia aquí.

## 2 · La cadena crítica, y dónde está este corte

```text
(g) APROBADA  →  ESTADO DURABLE  →  RUNTIME  →  VERIFICADOR Y RAÍZ EXTERNA  →  CERTIFICACIÓN
     `O23`         ESTE CORTE         siguiente        cortes V2–V6              `F6-J`
                                                                                    │
                                                                                    ▼
                                                                        PRIMERA ADOPCIÓN REAL
                                                                          — PesquerApp —
```

**Este macrobloque construye el primer eslabón después de la norma**, y sólo ése. El grafo
de dependencias completo vive en
[`05-PLAN-DE-IMPLEMENTACION-F5-F6.md`](../canonico/05-PLAN-DE-IMPLEMENTACION-F5-F6.md) §3.

## 3 · Clasificación por contrato

**Vocabulario cerrado**, y ninguna fila usa una categoría vaga:

```text
IMPLEMENTADO_Y_PROBADO           hay código ejecutable y pruebas ejecutadas en verde
PARCIAL                          hay código ejecutable que cubre PARTE del contrato, y se
                                 dice exactamente qué parte y qué queda
NO_IMPLEMENTADO                  no hay código. El contrato está escrito y nada más
BLOQUEADO_POR_DEPENDENCIA        falta otro contrato de F6 que va antes
BLOQUEADO_POR_DECISION_DEL_OWNER falta un acto del Owner, DECLARADO y con su condición
EXTERNO                          su sujeto vive fuera de este repositorio
```

| contrato | sede | clasificación | qué lo cierra |
|---|---|---|---|
| **contrato de ESTADO DURABLE** (`g.1`–`g.13`) | [`g.17`](../rediseno/g-ESTADO-DURABLE-APROBADA.md) · derivado en [`CONTRATO-ESTADO-DURABLE.md`](../../kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md) | **IMPLEMENTADO_Y_PROBADO** | — |
| **`A14` · guarda de entorno** (corte `V1` · `F6-I`) | [`06-DEUDA`](../canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md) §4 | **IMPLEMENTADO_Y_PROBADO** | — |
| **`FD-3` · la especificación normativa viaja al proyecto instalado** | [`06-DEUDA`](../canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md) §10 bis | **IMPLEMENTADO_Y_PROBADO** | — |
| **contrato de GOBIERNO GIT DEL CONTROL REPO** (`g.14`) | [`g.17`](../rediseno/g-ESTADO-DURABLE-APROBADA.md) | **PARCIAL** | la tabla de propiedad del control repo, la serialización entre máquinas y la prohibición ejecutable de forzar referencias (`G-A8`) |
| **contrato de RAÍZ EXTERNA DE CONFIANZA** (`g.15`) | [`g.17`](../rediseno/g-ESTADO-DURABLE-APROBADA.md) · `11-ARQ` §11.8 · `O25` | **PARCIAL** — ya **NO** bloqueado por decisión del Owner: `O25` fija titularidad, custodia y autoridad administrativa | que el contrato se ejecute **FUERA** del árbol verificado con una identidad que no pueda escribir en él, con un proveedor productivo real del anfitrión. `O25` §6 dice él mismo que no la declara implementada ni certificada |
| **`V6-01`…`V6-19` · verificador de admisión** (`F6-A`) | `11-ARQ` §20.1 | **NO_IMPLEMENTADO** | los cortes `V2`–`V5` del plan |
| **`F6-D` · runtime y dispatcher** | `11-ARQ` §7 | **NO_IMPLEMENTADO** — su dependencia `[1]` **ya no bloquea** | el corte siguiente |
| **`F6-F` · los cuatro macrocircuitos** | `11-ARQ` §8 y §9.6 | **NO_IMPLEMENTADO** | corte propio |
| **`F6-G` · arquitectura de adaptadores** (corte `V7`) | `11-ARQ` §6 | **NO_IMPLEMENTADO** | corte propio, independiente de todo |
| **`F6-H` · hallazgos externos con propietario y fase `F6`** | `11-ARQ` §19 | **PARCIAL** — `A14` y `FD-3` cerrados en este corte | el resto de su lista |
| **`F6-J` · CERTIFICACIÓN** | `O20` §3 | **BLOQUEADO_POR_DEPENDENCIA** | que exista lo que hay que certificar, y un juicio independiente que no sea quien construyó |
| **custodia productiva de la clave de firma** | `FD-1` · `O25` §2 | **EXTERNO** al repositorio, y **decidido**: identidad de servicio dedicada del verificador externo, con un proveedor de secretos del anfitrión | que exista ese proveedor en el anfitrión de la instalación. **No es materia del repositorio**, y por eso queda EXTERNO aunque la decisión ya esté tomada |

> **Y la regla que impide leer esta tabla al revés.** `IMPLEMENTADO_Y_PROBADO` **no es
> CERTIFICADO**. La certificación de `F6` la emite un juicio independiente, y **no quien
> construyó** —criterio `B6`—. Nada de esta tabla desbloquea PesquerApp.

**Cómo se reparten las nueve condiciones de `g.16`, para que la primera fila no se lea de
más.** `(g)` §16 dice que una implementación satisface **la sección** cuando **las nueve** se
demuestran sobre un árbol real. La sección **NO está satisfecha entera**, y esta tabla no
dice que lo esté: dice que lo está el **primero de sus tres contratos derivados**. El reparto
es éste, y cada condición cae en un contrato y en uno solo:

```text
contrato de ESTADO DURABLE  ·  g.1–g.13   →  G-A1 · G-A2 · G-A3 · G-A4 · G-A5 · G-A6 · G-A7
                                              las SIETE demostradas sobre árbol real, con
                                              escenario positivo y negativo, en T173–T179

contrato de GOBIERNO GIT    ·  g.14       →  G-A8   NO demostrada. La rama canónica no
DEL CONTROL REPO                              contiene estado parcial —la zona operacional
                                              queda fuera del versionado—, pero la
                                              imposibilidad POR POLÍTICA de forzar una
                                              referencia, y su detección, son del corte
                                              siguiente. Por eso ese contrato es PARCIAL

contrato de RAÍZ EXTERNA    ·  g.15       →  G-A9   NO demostrada con una raíz externa real.
DE CONFIANZA                                  Existe la interfaz, sus proveedores
                                              intercambiables y su fallo cerrado; la
                                              atestación se prueba con un proveedor EFÍMERO
                                              DE PRUEBAS, que no es una custodia productiva.
                                              Por eso ese contrato es PARCIAL, y `FD-1` sigue
                                              abierta
```

> **La consecuencia, dicha contra el propio interés:** mientras `G-A8` y `G-A9` no se
> demuestren, **la sección `(g)` no está satisfecha**, y nadie puede citar la primera fila de
> la tabla para afirmar lo contrario.

## 4 · Los validadores documentales NO son el runtime de `F6`

**Se dice porque la confusión es barata y cara de deshacer.** La batería del corpus
—`ads_lint.py`, `comprobar_*.py`, sus controles negativos y su evidencia publicada— comprueba
la **CONSISTENCIA DEL CORPUS**. El runtime de `F6` es otra cosa: **ejecuta**. Un verde de la
batería no dice nada sobre si el motor de estado durable funciona, y por eso el motor trae
**su propia batería ejecutable**, registrada en el manifiesto canónico de validadores y con
su propia evidencia.

## 5 · Decisiones técnicas de `F6`, con sus alternativas

**Autoridad:** `O24` §2 y `g.0`. Ninguna de estas decisiones es norma nueva, ninguna rebaja
una invariante y **ninguna vuelve al Owner**. Las del estado durable se leen enteras, con sus
alternativas, en el contrato derivado:
[`CONTRATO-ESTADO-DURABLE.md`](../../kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md) §2.
Éstas son las que **no** viven allí porque tocan al repositorio y no al motor:

| decisión | alternativas descartadas | por qué |
|---|---|---|
| **el runtime vive en `kernel/operativo/runtime/`**, dentro del kernel vendorizado | un paquete aparte fuera del kernel · dentro de `tooling/` | el motor tiene que **viajar al proyecto instalado**: es él quien administra el estado de un control repo. `tooling/` es lo ejecutable de FUERA del kernel, y sacarlo del kernel lo dejaría fuera de la huella de integridad, que es la vía silenciosa para forkearlo |
| **la guarda de entorno vive en el kernel y el tooling la importa** | duplicar el número de versión en cada script · ponerla en `tooling/` | la flecha correcta es que el tooling dependa del kernel y no al revés. Repetir el número es el hallazgo `A-12` otra vez |
| **la variable de la guarda sólo puede SUBIR la exigencia** | permitir bajarla para desbloquear un entorno | una guarda que se relaja por entorno no es una guarda: es un interruptor, y el primero que lo use en CI la apaga para todos |
| **la lista de especificación que viaja se DERIVA del árbol** | alargar la lista escrita a mano con `(g)` y `E3`–`E6` | una lista a mano al lado de un directorio que crece sólo puede envejecer mal: ya envejeció una vez, y eso es `FD-3` |
| **la frontera del proyecto instalado se DECLARA en `exclusiones.yaml`** | editar `E5`, que es material APROBADO · embarcar la historia del kernel a cada proyecto | `E5` enlaza tres sedes que a propósito **no viajan**, y dentro del proyecto instalado esos enlaces quedaban rotos. Tocar `E5` sería reabrir `F5`, que `O24` §5 prohíbe; embarcar la historia es lo que el arranque declara no hacer. La declaración **sólo se activa donde la ruta no existe**, de modo que en este repositorio no tolera nada, y una entrada cuya ruta no exista aquí es un FALLO: no sirve para silenciar un enlace roto de verdad |
| **`F17` y `F18` de `validar-f5.py` se ANCLAN al acto y a la evidencia** en vez de retirarse | dejarlos como estaban —quedarían vacíos o darían falso rojo— · borrarlos | un control que se retira cuando la fase avanza no protege nada. `F17` busca el acto del Owner en su sede canónica y sin él sigue en rojo; `F18` exige que toda afirmación de «implementado» cite un fichero de evidencia publicado que exista, y prohíbe «certificado» en cualquier redacción —con cópula, sin ella y en fila de tabla—. **Su ámbito es ACOTADO y se dice**: `docs/f5`, `docs/canonico` y `docs/rediseno`, y NO alcanza a la raíz del repositorio, que es el hallazgo `S1-02`, adjudicado y vivo |

## 5 bis · La auditoría independiente, y qué cambió por ella

**Quién la hizo.** Un auditor que no construyó nada de este corte, con el encargo de
romperlo. No escribió una línea en el árbol: se comprobó al terminar que
`git status --porcelain` seguía vacío.

**Lo que intentó y NO consiguió**, con medios que la batería no usa: perder una transición
confirmada matando el proceso con **120 `SIGKILL` externos en instantes aleatorios**;
publicar una mezcla parcial fabricándola a mano; obtener **doble éxito con 24 escritores
concurrentes**; evitar el fallo cerrado con **siete formas de corrupción del estado y ocho
del diario**; leer un almacén de versión futura o anterior sin fallo cerrado; relajar la
guarda de entorno con **nueve valores distintos**; usar la frontera declarada para silenciar
un enlace roto de verdad; y romper el determinismo —dos almacenes construidos desde rutas y
directorios de trabajo distintos dieron los **siete artefactos durables byte-idénticos**, y
la batería y el escenario dieron bytes idénticos desde tres `cwd` y coincidieron byte a byte
con la evidencia publicada—.

**Lo que SÍ encontró, y se corrigió en la única pasada de corrección:**

| defecto | clasificación | qué se hizo |
|---|---|---|
| una reconciliación nacida de **reintentos agotados** se retiraba borrando su última línea, y `verificar` y `auditar` seguían diciendo `ok` — una cadena de huellas no detecta que le quiten la **cola** | **BLOQUEA EL CORTE** | **cabeza durable** del registro, publicada de forma atómica tras cada anexado bajo el bloqueo propio del registro, y comprobada en el **camino de lectura**. Cinco vectores de manipulación, tres caminos de lectura, todos fallan cerrado |
| `G-A5` sólo se cumplía con la ventana cerrada: agotar los reintentos **al recuperar al abrir** no dejaba registro auxiliar | CORRECCIÓN DETERMINADA | la recuperación recibe el mismo tratamiento que la aplicación: error tipado **y** registro `g.9` |
| los errores de cuatro módulos imprimían la **ruta absoluta de la máquina**, contra lo que el propio punto ejecutable declaraba | CORRECCIÓN DETERMINADA | el saneado vive en **un solo punto** —el constructor del error tipado—, no repartido por veinte `raise` que es como se rompió la primera vez |
| `F18` estaba declarado «en todas partes» y era acotado, y su expresión sólo cazaba una redacción de seis | CORRECCIÓN DETERMINADA | se dice su ámbito real, y la expresión caza cópula, ausencia de cópula y fila de tabla. Comprobado con las ocho redacciones que la auditoría usó |
| el bloque reanudable de la iniciativa seguía afirmando `F6 NO INICIADA` | CORRECCIÓN DETERMINADA | reanclado, y **dejando de copiar** el estado de fase: se remite a su única sede |
| la raíz del repositorio no está en ningún inventario de contenido, de modo que la batería pasa con una infracción plantada ahí | **DEUDA DE OTRO CORTE** | es el hallazgo `S1-02`, adjudicado y vivo. Este corte no lo abre ni lo empeora; lo que sí hace es **dejar de sugerir** que lo cubre |
| `O24` se inscribió sin `procedencia` ni `relaciones de revisión` | no corregible aquí | el texto del Owner se transcribe LITERAL: completarlo sería reescribirlo. Registrado en `FD-2` |

**Residuo declarado del arreglo principal**, y se dice en vez de callarlo: entre el `fsync` de
una línea del registro y el reemplazo de su cabeza hay una ventana de **un anexado**, que hay
que tolerar o cualquier corte dejaría el registro inservible; quien borrase la última línea
exactamente en esa ventana no sería detectado, y la detección vuelve en cuanto el registro
anexa otra vez o el almacén se recupera. Y **falsificar a la vez el log y su cabeza sigue sin
ser detectable desde dentro del árbol**: es literalmente lo que `g.5` advierte y lo que `g.15`
reserva a la raíz externa.

**El veredicto del auditor**, una vez aplicada la corrección: el corte sirve como fundamento
permanente.

## 6 · Lo que este corte NO hace

```text
NO INICIA        PesquerApp, ni un MVP, ni un piloto, ni una adopción parcial
NO CERTIFICA     nada: implementado y probado NO es certificado
NO COMPLETA      F6: este es el PRIMER corte, y el plan tiene ocho
NO REABRE        F4c ni F5
NO ELIGE         custodia productiva de claves: FD-1 sigue abierta y sin titular
```

## 7 · El corte siguiente, exacto

```text
1  RUNTIME Y DISPATCHER sobre el motor de estado durable: ciclo, fallos, reintentos,
   bloqueo, pausa, orden de reanudación y vistas derivadas             `F6-D` · 11-ARQ §7
2  el contrato de GOBIERNO GIT DEL CONTROL REPO que falta: tabla de propiedad,
   serialización entre máquinas y G-A8 ejecutable                      `g.14`
3  en paralelo, y sin decisión nueva del Owner: los cortes V2, V3, V4 y V5 del
   verificador de admisión, y el corte V7 de adaptadores               plan §4

Y AGRUPADA PARA EL OWNER, sin detener nada: `FD-1` —titular y custodio de la clave de
firma—, que es la única decisión suya que este corte deja pendiente.
```
