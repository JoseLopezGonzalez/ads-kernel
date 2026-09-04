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

## 10 · Qué demuestra este contrato, y dónde

**Las nueve condiciones observables de `g.16` tienen escenario positivo y negativo**, y ambos
son obligatorios. Su ejecución vive en la batería del motor y en el escenario extremo a
extremo, registrados en el manifiesto canónico de validadores:
[`validadores.yaml`](../validadores/validadores.yaml). El área y su índice:
[`00-RUNTIME.md`](00-RUNTIME.md).
