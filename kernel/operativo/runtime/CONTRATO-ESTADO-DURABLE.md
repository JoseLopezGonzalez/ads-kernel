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
 8  os.replace de cada temporal → canonico/<ruta>, y fsync del directorio destino
 9  REVISION.json.tmp → fsync → os.replace → fsync dir    ← PUNTO DE PUBLICACIÓN
10  DIARIO ← transicion.confirmada         + fsync
11  limpiar la zona de preparación
12  liberar el bloqueo y devolver el resultado
```

**Lo que hace que esto sea atómico y no sólo ordenado:** el paso 9 es el único que publica.
Antes de él, `REVISION.json` sigue nombrando la base, y **ninguna lectura ve la transición**
aunque los ficheros ya estén en su sitio. Detectar la ventana **no depende de haber
presenciado el fallo**: se lee el diario y se compara con el disco.

## 4 · Recuperación — las dos ramas de `g.8`, y no hay una tercera

```text
sólo `abierta`     → REVERTIR. Nada de canonico/ se tocó. Se verifica BYTE A BYTE que cada
                     ruta implicada sigue casando con la base; si casa, se descarta la zona
                     de preparación —que es ESPECULATIVO LOCAL— y se anota la reversión

`preparada`        → COMPLETAR. Se reejecutan 8, 9 y 10 de forma IDEMPOTENTE: cada objeto
                     preparado se verifica contra su `cid` antes de publicarse, y un destino
                     que ya contiene el `cid` esperado se salta

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
Borrar o alterar el registro a mano rompe la cadena y produce **fallo cerrado**.

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

**`FD-1` sigue abierta**: ni titular ni custodio de clave productiva están decididos, y este
contrato **no los decide**. Una clave de prueba **no es** una solución productiva.

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
