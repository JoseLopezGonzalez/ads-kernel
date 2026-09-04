# CONTRATO DERIVADO · ESTADO DURABLE

**Qué es.** El **contrato derivado** que la sección
[`(g)`](../../../docs/rediseno/g-ESTADO-DURABLE-APROBADA.md) `g.17` nombra y **deja sin
escribir**: rutas, nombres de fichero, serialización, algoritmos, bloqueos, protocolo
transaccional y migración del estado durable. Lo construye `F6` bajo la autoridad que
`O24` §2 le reconoce.

**Qué NO es.** **No es norma.** No modifica ninguna invariante de `(g)`, no la reinterpreta
y no la amplía. Donde este contrato y `(g)` difieran, **manda `(g)`**, y el defecto está
aquí. Tampoco es la sede del estado de construcción: ésa es `docs/canonico/04-CONTRATOS-TECNICOS.md`
§1, **nombrada y no enlazada a propósito**, porque este fichero viaja a cada proyecto
instalado y el corpus consolidado del kernel no.

**Su condición de evolución** es la de `g.0`, y son cinco, comprobadas juntas: preserva
todas las invariantes · mantiene compatibilidad o declara migración explícita · no rebaja
durabilidad, integridad, auditabilidad ni recuperación · conserva la separación entre
estado canónico, registros auxiliares y evidencia · supera las pruebas positivas y negativas
de este contrato. **Cumplidas las cinco, el mecanismo cambia sin volver al Owner.**

---

## 1 · Disposición física

**Raíz del almacén:** `<control-repo>/estado/`. Los tres componentes durables de `g.1` viven
en el repositorio de control, y el estado global **referencia** revisiones de otras fuentes:
nunca las copia.

```text
estado/
  FORMATO.json                    versión del ALMACÉN. Un lector que no la entienda para
  REVISION.json                   el ÚNICO punto de publicación atómica de una transición
  canonico/<dominio>/<id>.json    ESTADO CANÓNICO — se lee con `cat`, sin reproyectar
  diario/DIARIO.jsonl             DIARIO CANÓNICO — append-only, encadenado por hash
  reconciliacion/REGISTRO.jsonl   REGISTRO OPERATIVO AUXILIAR — append-only, encadenado
  reconciliacion/conflictos/<tx>/ copia ÍNTEGRA de lo divergente cuando la recuperación MARCA
  operacional/                    NO es estado durable: bloqueo y zona de preparación
```

**`operacional/` no se versiona y es reconstruible**, y por eso `estado/.gitignore` lo
excluye. Es lo que hace cierto, y no sólo prometido, que **la rama canónica nunca contiene
estado parcial** (`g.14`).

> **Los tres componentes son TRES ESTRUCTURAS, no tres nombres.** Formato distinto —JSON
> indentado frente a JSONL—, semántica distinta, cadena de integridad distinta y escritor
> distinto. Colapsarlos rompe `I-g7`, y una prueba lo comprueba sobre disco.

## 2 · Serialización, y por qué ésta

| decisión | alternativas descartadas | por qué |
|---|---|---|
| **JSON** para el estado canónico, con `sort_keys`, `ensure_ascii=False`, `indent=2` y salto final | YAML · TOML · SQLite · formato binario propio | YAML y TOML añaden dependencia o carecen de escritor estándar; SQLite y un binario **rompen `I-g1`**: el estado dejaría de leerse sin herramienta. JSON está en la biblioteca estándar, se lee con `cat` y con `sort_keys` produce **bytes idénticos** para el mismo contenido, que es lo que `I-g3` exige |
| **JSONL** para el diario y para el registro auxiliar | un único JSON reescrito entero en cada evento | reescribir el fichero completo en cada evento convierte un `append` en una transacción, y un truncamiento dejaría el diario ilegible entero. Una línea por evento se **añade** con `O_APPEND`, y un truncamiento se detecta como línea incompleta y **no** invalida las anteriores |
| **`sha256` sobre el contenido** como identidad (`cid`) | contador · ruta · marca de tiempo | `g.5` lo fija: la identidad se DERIVA DEL CONTENIDO. Un contador se reusa tras una recuperación; una ruta cambia al renombrar |
| **`os.replace` + `fsync` de fichero y de directorio** | escritura directa · copia y borrado | `os.replace` es atómico en POSIX y en Windows. Sin `fsync` del **directorio**, el renombrado puede perderse en un corte aunque el contenido esté en disco: es el fallo clásico y por eso se hace explícito |
| **`fcntl.flock`** para el bloqueo entre escritores | fichero centinela con PID · directorio como cerrojo | un centinela con PID **no se libera si el proceso muere**, y arreglarlo a mano es la vía por la que alguien acaba borrando un bloqueo vivo. El SO libera el `flock` al morir el proceso: un bloqueo abandonado se reclama solo, sin heurística de caducidad |
| **CAS sobre la revisión base** | último escritor gana · bloqueo optimista sin comparación | «el último gana» permite **dos éxitos para la misma revisión**, que es exactamente lo que `g.6` prohíbe |

**Ninguna de estas decisiones es norma nueva.** Todas son mecanismo, y `g.0` las sitúa en
este contrato expresamente.

## 3 · Protocolo transaccional

**Una transición multiarchivo es una TRANSACCIÓN** (`g.3`), y se observa como tal: o se ve
entera, o no se ve. El orden es éste, y no admite reordenación:

```text
 1  bloqueo exclusivo de escritor
 2  leer REVISION.json y comparar con la base declarada   → REVISION_OBSOLETA si no casa
 3  validar la transición: rutas, versión de esquema y forma
 4  DIARIO ← transicion.abierta            + fsync        ← la ventana pasa a ser DETECTABLE
 5  escribir los objetos en operacional/tx/<tx>/
 6  fsync de cada temporal y del directorio de preparación
 7  DIARIO ← transicion.preparada          + fsync        ← PUNTO DE NO RETORNO
 8  os.replace de cada temporal → canonico/<ruta>, y fsync del directorio destino,
    y TESTIGO DURABLE `operacional/tx/<tx>/PUBLICADOS.json` + fsync de contenido y de
    directorio                                             ← el paso 8 deja HUELLA
 9  EXIGIR el testigo del paso 8 y contrastarlo con el disco; sólo entonces
    REVISION.json.tmp → fsync → os.replace → fsync dir      ← PUNTO DE PUBLICACIÓN
10  DIARIO ← transicion.confirmada         + fsync
11  limpiar la zona de preparación —y con ella el testigo, que es ESPECULATIVO LOCAL
12  liberar el bloqueo y devolver el resultado
```

**Lo que hace que esto sea atómico y no sólo ordenado:** el paso 9 es el único que publica.
Antes de él, `REVISION.json` sigue nombrando la base, y **ninguna lectura ve la transición**
aunque los ficheros ya estén en su sitio. Detectar la ventana **no depende de haber
presenciado el fallo**: se lee el diario y se compara con el disco.

**Y el ORDEN de 8 y 9 deja de depender de que el código esté escrito en cierto orden**
—corrección de `E-08`, 2026-09-04—. Antes, el único guardián del orden era el orden de las
líneas: invertirlos dejaba el almacén IRRECUPERABLE y las tres baterías de extremo a extremo
seguían en VERDE, porque ninguna comprobaba la recuperabilidad de lo que dejaban escrito. La
garantía es ahora OBSERVABLE E INVARIANTE, y no una convención:

```text
EL PASO 8 ESCRIBE  un testigo durable con el `cid` OBSERVADO EN DISCO de cada ruta
                   publicada —no el planeado: un testigo que copiara el plan diría
                   «publiqué esto» sin haber publicado nada—
EL PASO 9 EXIGE    encontrar ese testigo y que case con el disco. Sin testigo, o con un
                   testigo que no case, el paso 9 NO publica: falla cerrado
DÉCIMO PUNTO       `entre-el-paso-8-y-el-9`, inyectable, con su prueba de caída y su
DE FALLO           recuperación posterior por la rama COMPLETAR
LA RAMA COMPLETAR  reejecuta 8, 9 y 10 de forma idempotente, y por tanto REESCRIBE el
                   testigo antes de volver a exigirlo
LOS TRES E2E       comprueban la RECUPERABILIDAD del almacén al terminar, de modo que ya
                   no pueden seguir verdes sobre un almacén irrecuperable
```

## 4 · Recuperación — las dos ramas de `g.8`, y no hay una tercera

```text
sólo `abierta`     → REVERTIR. Nada de canonico/ se tocó. Se verifica BYTE A BYTE que cada
                     ruta implicada sigue casando con la base; si casa, se descarta la zona
                     de preparación —que es ESPECULATIVO LOCAL— y se anota la reversión

`preparada`        → COMPLETAR. Se reejecutan 8, 9 y 10 de forma IDEMPOTENTE: cada objeto
                     preparado se verifica contra su `cid` antes de publicarse, y un destino
                     que ya contiene el `cid` esperado se salta. **El testigo del paso 8 se
                     REESCRIBE en la reejecución**, con los `cid` observados en ese momento:
                     completar no puede apoyarse en el testigo de un intento anterior, ni
                     saltarse la exigencia del paso 9 por venir de la recuperación

nada casa          → MARCAR. Copia ÍNTEGRA de lo divergente en reconciliacion/conflictos/,
                     y la salida la decide LA AUTORIDAD, no el runtime
```

**Lo publicado no se restaura nunca de forma automática.** La reversión está acotada a lo
especulativo local, y se verifica byte a byte antes de emitirse.

## 5 · Concurrencia

```text
· los escritores se SERIALIZAN con flock exclusivo, con reintentos acotados
· agotar los reintentos NO modifica el estado canónico: escribe el registro auxiliar de
  `g.9` y devuelve un error tipado
· la comparación de la revisión base impide DOS ÉXITOS para la misma revisión
· la bifurcación entre máquinas se DETECTA comparando linaje; su resolución NO se decide
  aquí, y `g.6` la deja declarada como materia calibrable
```

## 6 · Reconciliación

El registro auxiliar es **append-only y encadenado por hash**. Una **apertura** identifica
producto, repositorio, item, intento, causa y **momento lógico** —número de secuencia del
diario y revisión, nunca reloj de pared, que rompería `I-g3`—. `reconciliacion_pendiente`
**se deduce**: hay apertura sin resolución.

**Se retira por una sola vía**: una transición explícita de reconciliación, que escribe la
resolución en el registro **dentro de la misma transacción** que la explica en el diario.

**Y una cadena de huellas NO basta, aunque lo parezca.** Detecta que una línea se modifique y
que se quite una del medio, pero **no que se quite la última**: el prefijo que queda sigue
perfectamente encadenado. Ése era el agujero, y por él una pendencia nacida de **reintentos
agotados** —la única que el runtime abre de verdad, y que **no puede** dejar evento en el
diario porque quien agota los reintentos nunca obtuvo el cerrojo del escritor— se cerraba
borrando una línea, con `verificar` y `auditar` diciendo `ok`.

Se cierra con una **cabeza durable**, `reconciliacion/CABEZA.json`, que guarda la última
secuencia y su huella y se publica de forma atómica tras cada anexado, **bajo el bloqueo
propio del registro y nunca el del escritor**. Quitar la cola contradice la cabeza, y eso es
detectable siempre. La comprobación vive en el **camino de lectura**, no sólo en la
verificación: deducir la pendencia de un registro al que le falta la cola no es deducirla de
forma inequívoca, y `g.9` exige que lo sea.

> **Las dos alternativas descartadas, y por qué.** Anotar toda apertura en el diario rompe
> `g.6`: el que agota los reintentos no tiene el cerrojo. Anclar la huella del registro en
> `REVISION.json` haría depender el estado canónico del registro auxiliar, que es el colapso
> exacto que `I-g7` prohíbe. La cabeza vive en la materia del registro, no es el log: es un
> puntero monótono a su extremo.
>
> **Y el residuo, dicho en vez de callado.** Entre el `fsync` de una línea y el reemplazo de
> la cabeza hay una ventana de **un anexado**; tolerarla es obligatorio, porque si no
> cualquier corte dejaría el registro inservible. Quien borrase la última línea exactamente
> en esa ventana no sería detectado, y la detección vuelve en cuanto el registro anexa otra
> vez o el almacén se recupera. Falsificar a la vez el log y su cabeza sigue sin ser
> detectable **desde dentro del árbol**, que es literalmente lo que `g.5` advierte y lo que
> `g.15` reserva a la raíz externa.

## 6 bis · Sellado del diario — la mitad de `g.7` que faltaba

`g.7` escribe cinco puntos sobre el diario. Los tres primeros —registrar los eventos con
orden reconstruible, sostener la recuperación de `g.8`, no ser la sede del estado— los
instancia el §3 y los ejercita la batería del motor. **Los dos últimos son éstos, y hasta la
corrección de 2026-09-04 no existían ni en el código ni en este contrato:**

```text
· el SELLADO compacta el diario conservando lo que el estado y la auditabilidad exigen; su
  umbral es parámetro CALIBRABLE del contrato derivado
· retirar el cuerpo de un evento sellado exige una transición explícita y auditable
```

**Qué compacta.** El **CUERPO** de un evento, y jamás su **ESLABÓN**. Un evento sellado
—un **talón**— conserva `esquema`, `secuencia`, `tipo`, `previo` y `huella` exactamente como
se escribieron, más `transaccion`, `resultado` y `registro` cuando los llevaba, y sustituye
todo lo demás por un resumen:

```text
{"esquema":"ads.estado/1","secuencia":5,"tipo":"transicion.confirmada","transaccion":"tx-3",
 "resultado":"sha256:…","sellado":{"esquema":1,"cuerpo":"sha256:…","retirados":["autor",
 "base","clase","motivo","operaciones"]},"previo":"sha256:…","huella":"sha256:…"}
```

**El diario NO pierde ni una línea.** Quitar líneas rompería tres cosas a la vez: la
comprobación `secuencia == índice + 1`, el `previo` de la siguiente y la comparación del
recuento de líneas con el `diario_secuencia` que `REVISION.json` publica. Sellar deja el
fichero con el mismo número de líneas, en el mismo orden y con las mismas huellas.

**Qué conserva, y por qué eso y no menos.**

```text
LO QUE EL ESTADO EXIGE   ningún evento de una transacción SIN evento terminal se sella: es
                         la ventana de `g.8`, y sus dos ramas —REVERTIR con la `abierta`,
                         COMPLETAR con la `preparada`— leen ese cuerpo entero
LO QUE LA AUDITORÍA      `transicion.preparada` NO se sella NUNCA: `auditar()` reproyecta
EXIGE                    `raiz` con su `operaciones` y reproduce `cid_raiz` desde el origen.
                         `almacen.inicializado` tampoco: es donde arranca el linaje
LO QUE LA AUTORIDAD      ningún evento de una transacción MARCADA se sella: su salida la
TIENE PENDIENTE          decide la autoridad y su cuerpo sigue siendo prueba viva
LO QUE SIGUE DICIENDO    un talón dice QUÉ fue (`tipo`) y CUÁNDO (`secuencia`, que es el
CADA TALÓN               momento LÓGICO; `I-g3` veda el reloj), y qué se le retiró
```

Se sellan, por tanto, `transicion.abierta`, `transicion.confirmada`,
`transicion.revertida`, los dos eventos de reconciliación y `migracion.aplicada`: **dos de
cada tres eventos del camino feliz**, que es donde está la masa del fichero.

**Cómo sigue siendo verificable.** La huella de un talón **no se recalcula** —su contenido
es justamente lo que se ha retirado, y pedir la misma huella de menos bytes es pedir una
preimagen—. Se conserva, y se **ancla**: el evento `diario.sellado` que explica la retirada
declara `cid_sellados`, el `cid` de la lista ordenada de pares `[secuencia, cid del talón
entero]` de **todos** los talones del diario. Ese evento se encadena y se huella como
cualquier otro. **El ancla cubre el talón entero y no tres campos suyos**, y la primera
versión sí cubría sólo tres: `T319` la puso roja demostrando que cambiar el `resultado`
conservado de un talón, o REPONER en él un campo que nunca tuvo, se colaba entero.

```text
EDITAR UN TALÓN          el `cid` recalculado no casa con el anclado           → DIARIO_CORRUPTO
VACIAR UN CUERPO A MANO  hay talones y ningún `diario.sellado` que los explique → DIARIO_CORRUPTO
REHACER EL ANCLA         cambia la huella del evento de sellado y rompe el `previo`
                         del siguiente evento                                  → DIARIO_CORRUPTO
```

> **El residuo, dicho y no callado.** Falsificar **a la vez** un talón y el evento de sellado
> que lo ancla, **cuando ese evento es la última línea del diario**, no es detectable desde
> dentro del árbol. Es el mismo residuo que el §6 declara para la cola del registro auxiliar,
> vuelve a ser detectable en cuanto el diario anexa una línea más, y es literalmente lo que
> `g.5` advierte y `g.15` reserva a la raíz externa.

**El umbral, y dónde se calibra.** El umbral es el número de eventos de **cola** que el
sellado deja intactos, y se declara **aquí**, que es la sede que `g.7` le da. Se cambia
editando este bloque, sin tocar una línea de código:

```json
{
  "esquema": "ads.estado.calibracion/1",
  "sellado_umbral_eventos": 64
}
```

**Por qué 64 y no otro.** El mínimo de corrección es **3** —una transacción entera del
camino feliz son `abierta`, `preparada` y `confirmada`, y una cola más corta que una
transacción no deja legible ni la última—, y por debajo de ese mínimo el umbral se rechaza.
Se elige **64** porque deja unas veintiuna transacciones completas al final del fichero,
veinte veces el peor caso que la recuperación puede necesitar, y sigue siendo una cola que
una persona lee con `tail` sin herramienta. **No se elige el mínimo**: un umbral pegado a su
límite convierte cualquier error de cálculo en la pérdida de la ventana que protege.

**El umbral no tiene valor por omisión.** Ausente, ilegible, declarado dos veces, no entero,
cero, negativo o menor que el mínimo → `UMBRAL_DE_SELLADO_INVALIDO`, y **no se sella**. Un
motor que se inventa el umbral cuando no lo encuentra convierte esta sede en decorado.

**Qué exige retirar un cuerpo.** Una **transición explícita y auditable**, y aquí eso es
tres cosas juntas: un `autor` y un `motivo` —sin ellos, `RETIRADA_SIN_TRANSICION`—, un evento
`diario.sellado` propio en el diario, y que el cuerpo sea admisible —si la recuperación o la
auditoría todavía lo necesitan, `RETIRADA_NO_ADMISIBLE`—. La retirada **dirigida** de un
evento concreto pasa por las mismas comprobaciones que la compactación por umbral; lo único
que no consulta es el umbral.

**Cómo se invoca.** `ads_estado.py --repo <dir> sellar --autor A --motivo M`, con
`--umbral N` para calibrar la llamada, `--secuencia N` (repetible) para la retirada dirigida
y `--contrato <fichero>` para leer el umbral de otra sede. Los códigos de salida son los
mismos cinco de siempre: un fallo del sellado es un error tipado del kernel, y sale con 1.

**Lo que sellar NO hace.** No publica revisión, no toca `canonico/`, no entra en el linaje y
no se ejecuta solo: no hay compactación automática al abrir ni al aplicar. Toma el **bloqueo
de escritor** —el mismo que `aplicar` y `recuperar`, porque reescribe el fichero en el que
`anexar` escribe— y se **niega** si hay una transacción sin cerrar, aunque la regla de la
ventana ya la protegería evento a evento: `g.8` reserva esa salida a la autoridad.

## 7 · Versionado y migración

```text
· todo objeto durable lleva `esquema: "ads.estado/<n>"`
· una versión desconocida produce FALLO CERRADO, y NO una adivinanza                `g.10`
· `FORMATO.json` versiona el ALMACÉN; su ausencia es la versión 0 heredada
· migrar es EXPLÍCITO: cada migración registrada corre como una transacción normal,
  auditable en el diario y recuperable igual que cualquier otra                     `g.11`
· NO hay migración implícita al leer
```

## 8 · Frontera con la raíz externa

Este contrato **no elige** tecnología de firma, despliegue, claves ni custodia: `g.15` las
reserva al contrato de la raíz externa. Lo que aquí existe es la **interfaz**, con
proveedores intercambiables, un proveedor **efímero exclusivamente para pruebas** y **fallo
cerrado cuando no hay proveedor válido**. La evidencia se escribe **fuera del árbol
verificado**, y escribirla dentro es un error tipado.

**`FD-1` está cerrada como DECISIÓN por `O25`**: la identidad es de la raíz externa de cada
instalación, la autoridad administrativa del Owner y la custodia de una identidad de servicio
dedicada del verificador externo. Este contrato **no la implementa**: su sede es
[`CONTRATO-RAIZ-EXTERNA.md`](CONTRATO-RAIZ-EXTERNA.md). Una clave de prueba **no es** una
solución productiva.

## 9 · Errores, y por qué son tipados

Toda salida de fallo lleva un **código estable** —`REVISION_OBSOLETA`, `ESTADO_CORRUPTO`,
`VERSION_DESCONOCIDA`, `REINTENTOS_AGOTADOS`…— y un detalle legible. Un `except` que traga la
excepción convertiría un defecto en silencio, que es el mismo error con otra forma: **no se
usa en ningún punto del motor**.

**El censo de códigos se DERIVA de las clases, y una clase fuera del censo es un defecto.**
`estado/errores.py` publica `CLASES` y `CODIGOS = tuple(sorted(c.CODIGO for c in CLASES))`,
de modo que la lista no se escribe dos veces. La disciplina que eso impone es real y se
comprobó rompiéndola: `PublicacionEnVuelo` —la clase que distingue la VENTANA DE
PUBLICACIÓN de la corrupción— se declaró sin añadirla a `CLASES`, y durante unas horas el
motor pudo emitir un código que su propia lista cerrada no conocía. **Una clase de error
declarada y no censada es un código que nadie puede tratar**, y por eso el censo se
comprueba: ninguna subclase de `ErrorDeEstado` puede quedar fuera de `CLASES`.

## 10 · Qué demuestra este contrato, y dónde

**Las nueve condiciones observables de `g.16` tienen escenario positivo y negativo**, y ambos
son obligatorios. Su ejecución vive en la batería del motor y en el escenario extremo a
extremo, registrados en el manifiesto canónico de validadores:
[`validadores.yaml`](../validadores/validadores.yaml). El área y su índice:
[`00-RUNTIME.md`](00-RUNTIME.md).
