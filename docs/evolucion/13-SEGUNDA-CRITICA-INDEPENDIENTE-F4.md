# SEGUNDA CRÍTICA INDEPENDIENTE DE F4, Y SU APLICACIÓN

> **Procedencia, con los tres papeles separados.** Es la misma disciplina que el
> [documento 12](12-CRITICA-INDEPENDIENTE-F4.md) fijó, y se repite porque sigue siendo lo
> que impide que una fase se certifique a sí misma.
>
> ```text
> QUIÉN EMITIÓ EL JUICIO      un REVISOR INDEPENDIENTE con contexto limpio, que NO escribió
>                             F4 y NO aplicó la primera crítica. Leyó el corpus por su
>                             cuenta y verificó cada cita contra el fichero original.
>
> QUIÉN LO TRANSCRIBE         el autor material de F4, que es también quien aplicó la
>                             primera crítica. Sus hallazgos y veredictos se conservan
>                             LITERALMENTE, incluidos los que le contradicen y los que
>                             señalan defectos que él introdujo al corregir.
>
> QUIÉN APLICA LAS            el mismo. Y por eso NO puede certificar que las superó.
> CORRECCIONES
> ```
>
> **`F4c` NO queda cerrada por este documento.** El revisor emitió un veredicto explícito de
> **INSUFICIENCIA** —dos hallazgos BLOQUEANTES y siete GRAVES—, y las correcciones que siguen
> las escribió quien las recibió. Cerrar `F4c` exige que un revisor independiente examine el
> resultado corregido y emita un veredicto de suficiencia. **Ese veredicto no está aquí.**

## Verificación de las citas antes de transcribir

El transcriptor **no** puede juzgar el juicio, y **sí** debe comprobar que no transcribe un
error de hecho. Se verificaron contra el fichero original, una a una, las once afirmaciones
de las que dependen los veredictos más graves. **Las once resultaron exactas:**

```text
C7 línea 170            `aplica_a: "todo item cuyos paquetes escribieron en una o más
                        fuentes"`                                             EXACTA
b.3 vocabulario         `vigente | sustituida | invalidada` — NO `retirada`   EXACTA
b.3 obligación_retirada predicado sobre OBLIGACIONES, no sobre capas          EXACTA
b.14 paso 2             «completar o revertir (a.9)»                          EXACTA
E2.6                    «varias sources»                                      EXACTA
b.16 fila AUD           obligatorias: INV. `VER` no figura, ni condicional    EXACTA
§2 y reconciliación     `reconciliacion-pendiente` aparece 4 veces en el
                        documento —líneas 845, 879, 1837 y 2177— y §2 abarca
                        las líneas 213-759: NINGUNA está dentro de §2         EXACTA
§3.5 frente a §9.2      diez valores de `estado` frente a siete               EXACTA
§11.2                   titulada «Tres huellas» y define DOS más un artefacto EXACTA
doc 12 §5.7             los tres ejemplos están en §5.6                       ERRATA CONFIRMADA
doc 12 «SEIS escenarios» §11.5 tiene DIEZ                                     ERRATA CONFIRMADA
```

Las dos últimas son erratas **del transcriptor de la primera crítica**, no del diseño. Se
corrigen en este documento y en el 12.

---

# 1 · Veredicto global del revisor

**Se transcribe literal.**

> **`F4c` NO es cerrable. Es mejor que `F4` entregada, y sigue sin ser una base válida.** La
> primera crítica atacó bien y sus nueve bloques están, en su mayoría, materialmente
> corregidos: el manifiesto plegado en `evento` es correcto, la partición de `cobertura` en
> `sujeto·aspecto·responsables·criterio` es correcta, la matriz de fuentes de verdad ahora
> respeta `a.9`, la función `Q0`–`Q9` es genuinamente total y disjunta —lo he verificado
> estado a estado contra `b.4`, y **es cierta**—, y `D23`–`D33` conservan la historia sin
> reescribirla. Pero el protocolo transaccional, que es la pieza que la primera crítica
> declaró «no ejecutable», **sigue sin serlo por dos defectos distintos de los que se
> corrigieron**: la lista de `fsync` obligatorios omite el `fsync` de directorio para los
> ficheros canónicos, con lo que §2.6 vuelve a cometer exactamente el error que §2.6.6
> nombra y presume de haber nombrado —y produce corrupción silenciosa, no detectada por
> ninguna de las diecisiete filas adversariales—; y `fase: conflicto` se declara TERMINAL
> sin conectarse jamás con `reconciliacion-pendiente`, de modo que **el protocolo de §2 nunca
> emite el único estado del que depende `b.4` P0**, y una colisión tras aplicar 2 de 5
> ficheros produce un repositorio que el sistema declara sano. A eso se suma que §9.5
> contradice frontalmente el texto vigente de `C7` —lo he verificado literalmente— mientras
> §15.7 declara `C7` «REUTILIZADO»; que el puntero de §6.7 obliga a escribir en las fuentes
> en fases donde §8.1 y §8.2 lo prohíben expresamente; que §3.7 atribuye a `b.3` un
> vocabulario que `b.3` no contiene; y que la arquitectura se apoya en un artefacto —«el
> contrato del aspecto»— que se referencia tres veces, sostiene la familia documental entera,
> duplica `responsables` con la celda, y **no está definido, no tiene esquema, no tiene dueño
> y no está en el recuento de §3.8**: es el mismo modo de fallo que la primera crítica
> encontró con el manifiesto de transacción, reproducido en otro sitio y no detectado. La
> dirección de `F4` sigue siendo aceptable y no la discuto. Su §2 y su §5 no lo son.

## El cuadro de severidades

```text
BLOQUEANTES · DOS      E · fsync de directorio omitido en los canónicos
                       B · `conflicto` terminal que nunca emite reconciliación

GRAVES · SIETE         A · no hay regla de lectura durante la ventana
                       C · identidad por contenido circular y sin serialización
                       H · §9.5 contradice el texto vigente de C7
                       I · el puntero escribe en fuentes fuera de todo circuito
                       K · la recuperación local publica en remoto sin autoridad
                       N-1 · «el contrato del aspecto» no existe
                       N-6 · las obligaciones de iniciativa invocan predicados
                             que no existen

MEDIOS · TRECE         D · F · G(residuos) · J · N-2 · N-3 · N-4 · N-5 · N-7 · N-8 ·
                       N-9 · N-10 · N-11
MENORES · TRES         N-12 · N-13 · N-14
RECHAZADOS · SIETE     ver §4
```

---

# 2 · Los once candidatos, adjudicados

## `A` · Visibilidad durante una transacción — **CONFIRMADO · GRAVE**

**Lo que dice el revisor.** «Desde `confirmada` puede creerse lo que lee» es una
**descripción del estado del diario**, no una regla dirigida a ningún lector. El documento no
contiene, en ninguna sección, una obligación de lectura. La única entidad que comprueba es el
runtime, en `Continúa` paso 2. **Todo lector que no sea el runtime —y `R1` existe precisamente
para que los haya— lee sin barrera.**

Y añade un agravante que el Owner no nombra: **el marcador es «sin contenido»**. Un humano que
lo encuentre sabe que hay algo en vuelo y **no sabe qué ficheros**. Para saberlo tiene que
recorrer el diario y localizar el `preparada` de esa `tx`. *«Es decir: la condición de
fiabilidad de `R1` sólo se evalúa reproyectando el diario — que es exactamente el coste que
§2.2 usa para descartar la alternativa C. `F4` paga el coste de C sin haber elegido C, y no lo
dice.»*

**Media objeción del Owner, refutada:** `b.14 Continúa` **sí** está cubierto. §7.4 añade la
comprobación y los pasos 1–4 son deterministas. La reanudación no reanuda desde estado parcial.

**Prescripción.** Regla de lectura normativa del mismo rango que la de escritura · dar
contenido al marcador · marcar el `tx` en la cabecera de cada canónico afectado durante la
ventana · declarar que **no hay aislamiento de lecturas**, sino **detectabilidad de la
ventana**, y cualificar la casilla `R3` de §2.2.

**Prueba adversarial `X18`.** Suspender el ejecutor entre el fichero 3 y el 4 con `SIGSTOP`;
un lector tercero debe declarar «transacción `TX-…` abierta; estas cinco rutas no son
fiables», nombrando las cinco, **sin recorrer el diario completo**.

## `B` · `conflicto` y reconciliación — **CONFIRMADO · BLOQUEANTE**

**El hecho decisivo, comprobado por barrido:** `reconciliacion-pendiente` aparece cuatro veces
en el documento y **ni una sola vez en §2**. El protocolo transaccional nunca lo emite. `b.4`
P0 lo define como *«transición multiarchivo incompleta: el estado NO es fiable»* y le da
precedencia absoluta, y §2 no tiene ninguna instrucción que lo ponga.

Las tres consecuencias se siguen mecánicamente del texto:

```text
1  `conflicto` es terminal ⇒ la tx TIENE evento terminal ⇒ deja de «señalar que hay algo en
   vuelo» ⇒ por W8 el marcador se retira, y §2.9 no lo recrearía
2  `Continúa` paso 2 pregunta «¿hay transacciones sin evento terminal?» → NO.
   El sistema declara el arranque limpio
3  los ficheros aplicados quedan aplicados, los no aplicados sin aplicar, y `R3` garantiza
   que así se queden. El estado es incoherente y NADIE LO MARCA
```

> *«Ésta es la contradicción más grave de `F4c`, porque invierte el propósito de la
> corrección: la primera crítica exigió que la tercera caja "NUNCA se resuelva sola", y `F4c`
> lo consiguió a costa de que el sistema deje de saber que hay algo que resolver.»*

Y la semántica está incompleta en cuatro puntos más: **quién** resuelve —«se escala» no nombra
autoridad—; **qué se bloquea**; **cómo se conserva el contenido divergente** —vive sólo en el
disco, sin huella en ningún evento, luego quien resuelva puede destruirlo sin constancia—; y
**qué evento cierra la reconciliación**, dado que `conflicto` ya era el terminal.

**Prescripción.** `conflicto` deja de ser terminal y pasa a **abierto y absorbente**, cerrado
sólo por `fase: reconciliada` · §2 **emite** la bandera que `b.4` P0 consume · el marcador no
se borra · el evento `conflicto` registra hash observado y copia íntegra de lo divergente ·
autoridad y bloqueo declarados · corregir `W8`, que hoy trata «terminal» como «cerrada».

**Prueba adversarial `X19`.** Aplicar 2 de 5, modificar el 4 externamente, recuperar,
**reiniciar y ejecutar `Continúa`**: debe detenerse en `reconciliacion-pendiente` nombrando
ítems y fichero divergente, **antes** de regenerar derivados y **antes** de seleccionar
trabajo. Borrar el marcador a mano y repetir: diagnóstico idéntico.

## `C` · Identidad por contenido — **CONFIRMADO · GRAVE**

Cuatro defectos, y ninguno mitigado en el texto:

```text
1  CIRCULARIDAD        `id` es campo del evento y a la vez huella del evento, y no se dice
                       que se excluya. Como está escrito, no es implementable
2  `TX-<huella>` SIN   «comparte forma con el evento» dice cómo se ve, no qué se hashea. Un
   DEFINIENDUM         `tx` no tiene contenido propio —§2.5 lo declara— luego no hay nada de
                       lo que sacar su huella
3  SIN SERIALIZACIÓN   orden de claves, indentación, `\n` frente a `\r\n`, normalización
   CANÓNICA            Unicode, listas y mapas: nada fijado. Y §2.11 admite que el formato
                       PUEDE cambiar «a un formato de línea» — lo que cambiaría TODOS los
                       identificadores y rompería `predecesor`
4  LA IDEMPOTENCIA     por `predecesor`. Reemitir tras una caída lo hace con un `predecesor`
   PROMETIDA ES FALSA  distinto —el diario creció— luego produce OTRO id y OTRO fichero
```

**Prescripción.** Un contrato de identidad en cinco apartados: representación canónica
publicada **como pseudocódigo, no como prosa** · campos incluidos y excluidos, con `id`
excluido por construcción y versionado del algoritmo (`identidad_v: N`) ·
`tx = TX-H(cuerpo de preparada MENOS id, tx, predecesor)`, que depende sólo de la intención
declarada y sobrevive a una reemisión · `id = EV-H(evento MENOS id)` con `predecesor`
**incluido**, y **la consecuencia declarada: reemitir NO es idempotente por id** —la
idempotencia se afirma sobre `tx`— · regla de reintento: buscar en el diario un evento con el
mismo `tx` y la misma `fase` antes de reemitir.

**Pruebas `X20`–`X22`.** Dos implementaciones independientes del serializador deben producir el
mismo `tx` y el mismo `id` · preparar, matar antes del `rename`, reintentar, y comprobar que
sólo existe **un** `tx` · cambiar el formato de presentación y comprobar que **ningún
identificador cambia**; si cambian, §2.11 y §2.8 son incompatibles.

## `D` · Punto de compromiso y `abortada` — **CONFIRMADO · MEDIO**

> *«La ventana de alcanzabilidad de `abortada` es exactamente `[preparada durable, primer
> fichero tocado)`, y esa ventana es exactamente el dominio de `W3`, que manda completar.
> Antes de que `preparada` sea durable no existe registro que pueda llevar `fase: abortada`.
> Por tanto `abortada` es un estado formalmente definido y operacionalmente inalcanzable.»*

El revisor buscó una causa de aborto que sobreviva y **no la hay**: el no-determinismo se
detecta al preparar (`X16`); la divergencia antes de aplicar es `conflicto` por §2.6.4; la
pérdida del lock devuelve al arranque, que aplica `W3`.

*«Un estado muerto en un enum normativo es deuda que se paga tres veces»* — está en el enum de
§3.6, en `D23`, y `F6` escribirá pruebas para él.

**Prescripción (preferida): RETIRAR `abortada`.** Cuatro estados, no cinco, con una decisión
que revise `D23` y una frase que diga por qué no existe.

## `E` · Durabilidad de los ficheros canónicos — **CONFIRMADO · BLOQUEANTE**

**El defecto es doble, no simple:**

```text
(a) FALTA EL fsync DE      los puntos (1) y (3) de la lista de obligatorios lo exigen
    DIRECTORIO             literalmente («y su directorio»); el punto (2), NO. §2.6.3 paso 3
                           lo confirma: «fsync del fichero», sin directorio.
                           `F4c` comete, en el punto donde más importa —los ficheros que SON
                           el estado—, el error que su propia garantía 3 acaba de nombrar
                           como «el error clásico»

(b) EL ORDEN ES            «escribir temporal + rename, y fsync del fichero» sincroniza
    INCORRECTO             DESPUÉS del rename. La secuencia correcta es
                           `escribir temporal → fsync(temporal) → rename → fsync(directorio)`
```

**Por qué es BLOQUEANTE: el fallo resultante es silencioso.** La recuperación clasifica
ficheros **sólo cuando encuentra una `tx` sin evento terminal**. Si `confirmada` sobrevivió
—y sobrevive: lleva sus dos `fsync`— la `tx` es terminal, `W6` sólo regenera derivados y
**nadie vuelve a comparar los hashes de los canónicos**. *«El diario afirma un cambio que el
disco no tiene, y el sistema no tiene un solo mecanismo que lo desmienta.»*

**Y ninguna de las diecisiete filas lo detecta:** `X01`–`X03` matan el **proceso**, no la
máquina; `X05`/`X06` requieren manipulación externa; **ninguna corta la corriente**.

**Prescripción.** Reescribir §2.6.3 paso 3 con la secuencia correcta · corregir el punto (2)
para que diga «y su directorio» · declarar que los directorios afectados pueden ser **varios**
y que se sincronizan todos · permitir y nombrar la agrupación de `fsync` por directorio ·
**añadir una comprobación de integridad post-terminal** que verifique los
`hash_posterior_esperado` de toda `tx` terminal dentro de la última ventana de commit — *«es
lo único que convierte el fallo silencioso en fallo detectado»*.

**Pruebas `X25`–`X26`.** Corte de alimentación forzado tras el `rename` de `confirmada`: los
cinco canónicos deben casar con su hash posterior · inyectar la reversión de dos canónicos con
`confirmada` presente y comprobar que el arranque **lo detecta y los nombra**.

## `F` · Marcadores y clones — **CONFIRMADO · MEDIO**

> *«La garantía 6 enuncia como propiedad normal del sistema ("los marcadores sí, porque están
> versionados") un estado que la regla de Git, dos párrafos después, declara imposible salvo
> por defecto del runtime.»*

Y aplicando el criterio de §2.4 al propio marcador —*¿sobrevive a un clon nuevo?*— la
respuesta es **no**: §2.9 dice que es reconstruible y «un acelerador, no una verdad», luego
**por el criterio del propio documento es operacional y su sitio es `.ads/run/`**. *«`F4c`
viola su propio criterio de clasificación en la única pieza a la que ese criterio debería
aplicarse sin discusión.»*

`X15` ya trata el caso como **evidencia diagnóstica de un defecto**, que es la lectura
correcta; la garantía 6 lo trata como **fuente**, que es la incorrecta.

**Prescripción.** Declarar durable sólo el diario y los canónicos · declarar en positivo que
nada de `estado/tx/` llega a Git · reclasificar el marcador (moverlo a `.ads/run/tx/`, o
conservarlo en `estado/tx/` **excluido de Git**) · reescribir la garantía 6 · corregir la
condición de reconstrucción de §2.9.

## `G` · Migración M5–M7 — **PARCIAL: premisa REFUTADA, residuos REALES · MEDIO**

**El revisor rechaza la premisa del Owner, y lo dice sin suavizarlo porque se le pidió:**

> *«El Owner sostiene que "el contrato sigue afirmando sin matiz que el sustituto funciona por
> sí solo". **No lo hace.** Dice literalmente lo contrario, con las palabras exactas de la
> objeción: M5 se responde en coexistencia, y la coexistencia **tapa** la dependencia oculta.
> La corrección `D33` es sólida en su núcleo, y la lectura del Owner sobre este punto es
> errónea.»*

**Cinco residuos que sí son reales:** «la certificación de M5 NO se pierde» choca con
«Revalidada en M7» y suspende sin decir por qué el mecanismo que §6.5 celebra · el **alcance
residual** de M5 no está declarado, pudiendo expresarse como `parcial` · **restaurar M6 no
revalida nada** —devuelve ficheros, no CI ni permisos, y §9.3 dice que cambiar CI invalida
Integrado— · la dependencia oculta **no tiene proceso** («un item nuevo» ¿de cuál de las diez
rutas?) · **no hay condición para reintentar M6**, luego el circuito admite un bucle
M6→M7→M6 indefinido.

## `H` · Contradicción con `C7` — **CONFIRMADO · GRAVE**

> *«He leído `C7` completo. Línea 170, dentro del bloque `ads:gate`:*
> `aplica_a: "todo item cuyos paquetes escribieron en una o más fuentes"`*.*
> *La lectura del Owner sobre el texto de `C7` es LITERALMENTE EXACTA.»*

Tres hechos, en orden:

```text
1  EL OWNER CITA `C7` CON     con una sola fuente escrita, el gate APLICA y su comprobación
   EXACTITUD                  `existe-integration-set` EXIGE un Integration Set

2  `C7` EXTRALIMITA A `E2.6`  `E2.6` dice «VARIAS sources»; `C7` dice «UNA O MÁS». `C7`
                              declara derivar de `E2`. La lectura de F4 sobre `E2.6` es la
                              CORRECTA; el texto erróneo es el de `C7`

3  `F4c` NO DETECTA LA        §9.5 hace inaplicable el Integration Set con 1 fuente, §7.2
   COLISIÓN Y ENCIMA LA       dice «cuando hubo varias fuentes», y §15.7 declara `C7`
   NIEGA                      «REUTILIZADO» —«entra sin cambio»—. Las tres no pueden ser
                              ciertas a la vez. F4c reutiliza un contrato al que contradice
```

**Reproducción.** Producto de un repositorio. `FEA-021` escribe en su única fuente. Al cerrar,
el validador evalúa `aplica_a` → verdadero. `existe-integration-set` → no hay. `C7` dice: *«El
item no cierra.»* *«El producto de un repositorio —"la mayoría de los productos del mundo", en
palabras de la propia §9.5— no puede cerrar ni un solo item. Y el defecto es peor que el que
`D32` corrigió: `D32` bloqueaba la certificación inicial; éste bloquea cada cierre de item,
para siempre.»*

**Y el revisor responde explícitamente a si es presión normativa: NO lo es.**

> *«`C7` es material DERIVADO de `E2`. Su corrección está completamente determinada por
> `E2.6` y NO requiere decisión del Owner ni enmienda de material aprobado. Es un DEFECTO DE
> DERIVADO, con prescripción cerrada, y su sitio es `F6`. Lo que sí debe hacer `F4` HOY es
> registrarlo, porque §15.7 afirma hoy que `C7` entra "REUTILIZADO", sin cambio, y eso es
> falso.»*

**Prescripción.** `aplica_a: "todo item cuyos paquetes escribieron en MÁS DE UNA fuente"` ·
con una sola fuente la evidencia es su **source change** en el checkpoint · un Integration Set
monofuente es **opcional como gate y recomendado como ancla de restauración**, porque
`restaura_a` es obligatorio en su esquema y la pregunta «¿qué restauro?» sigue teniendo
sentido · corregir §15.7, §10.2 y §9.5 · las pruebas `T159`–`T170` deben incluir el caso de
una fuente.

## `I` · Puntero en las fuentes — **CONFIRMADO en los tres puntos · GRAVE**

**`I.1` cardinalidad.** El campo es singular y `C6` `N7` declara que *«componente y fuente NO
tienen cardinalidad 1:1 obligatoria»*, con el caso MONOREPO explícito. El campo singular
reintroduce la equivalencia que `C6` retira y que `E2.0` declara formulación RETIRADA — que
es exactamente lo que el campo singular hace. → el campo pasa a **lista derivada de
`SOURCES.toml`**.

> **Dos precisiones del transcriptor, y las dos van contra el revisor.** (1) El revisor
> atribuye esa frase a **§6.6**, y §6.6 es «Cambio de proveedor» y no dice nada de eso: la
> fuente real es `C6`, en su párrafo sobre los tres conceptos. La misattribución es
> exactamente el defecto que este mismo revisor persigue en `J`, `N-8` y `N-9`, y se corrige
> en vez de propagarse. (2) Su formulación literal **no puede transcribirse**: `T161` la
> detecta como formulación retirada por `E2.0`, y el corpus no la conserva ni siquiera para
> negarla. Se parafrasea, y se dice que se parafrasea.
>
> **Y una observación que el hallazgo destapa:** `C6` sí conserva esa formulación —para
> declararla prohibida— y `T161` **no la detecta**, porque allí queda partida por un salto de
> línea y el recorrido de `T161` es por líneas. Es un hueco real de `T161`, encontrado por
> accidente al aplicar esta corrección. No se arregla aquí —es `kernel/operativo/`— y queda
> registrado para F6.

**`I.2` descubrimiento.** La lógica de recorrer hermanos y comparar remotos *«está declarada,
pero como prosa, no como contrato»*: no tiene campo en §3.4, luego un adaptador conforme puede
omitirla y seguir validando. Y *«NO está probada, y `F4` afirma que sí»*: §6.4 enumera cuatro
comprobaciones, **ninguna** de las cuales abre el entorno sobre una fuente. *«Es una remisión
que no llega a ninguna parte.»* El revisor añade, sin que se le pida, que la regla asume
**permiso para ejecutar `git` en directorios hermanos**, y que confundir «no encontrado» con
«no se pudo comprobar» reintroduce el defecto que §11.2 corrige en `P-08`.

**`I.3` ciclo Git — y es más grave de lo que el Owner formula.** *«La contradicción no es sólo
con `U0`–`U6`: es con §8.1 y §8.2, dentro del propio `F4`.»*

```text
EL PUNTERO ES UNA         luego U5 «recompilar proyecciones» ESCRIBE EN LAS FUENTES, sin una
PROYECCIÓN (literal)      sola precondición, gate, evidencia ni rollback por fuente

§8.1 SE AUTOCONTRADICE    los adaptadores se eligen en N2 y sus proyecciones se compilan
                          antes de N6; pero ESCRIBE dice «las fuentes sólo desde N6»

§8.2 SE AUTOCONTRADICE    la adopción declara modo NO DESTRUCTIVO y «ESCRIBE NADA en las
DE FORMA MÁS SERIA        fuentes hasta A8». La especialización es A5. Un adaptador con
                          puntero obliga a commitear en un producto ajeno con historia,
                          TRES FASES antes de que exista autorización de escritura

`C6` RESPONDE QUE NO      a su propia pregunta frontera: el puntero no deja de ser cierto si
A SU PROPIA FRONTERA      cambia el código de al lado, luego su sitio sería el control repo.
                          Ponerlo en la fuente es una EXCEPCIÓN, y hay que declararla

`C7` LO GOBIERNA Y NADIE  un puntero recompilado por `PLT` durante U5 no tiene item, ni
LO INVOCA                 paquete, ni custodia, ni checkpoint, ni rama, ni PR — y `main`
                          está protegida, luego ni siquiera puede empujarse
```

**Reproducción.** Tres fuentes, seis punteros, `main` protegida: un PR se fusiona, dos no.
*«El producto queda con punteros de dos versiones distintas, y ninguna pieza del sistema lo
sabe»* — no hay Integration Set porque no hay item, y §6.3 no detecta la deriva porque la
huella se compara contra la definición canónica, que sí se actualizó. **Rollback: no existe.**

**Prescripción.** Declarar el puntero **excepción nombrada** a la frontera de `C6` · toda
escritura de puntero es un **source change gobernado por `C7`**, con paquete, custodia,
checkpoint, rama, PR y CI — *«no hace falta inventar nada: hace falta usarlo»* · partir `U5`
en `U5a` (control repo) y `U5b` (propagación con gate, evidencia por fuente e Integration
Set) · rollback por fuente con estado `INTEGRACIÓN PARCIAL` · **`N2` y `A5` no escriben
punteros**: se propagan en `N6` y en `A8` · declarar que §6.3 sólo detecta deriva si la fuente
está materializada.

## `J` · `memoria.estado` — **CONFIRMADO · MEDIO**

`b.3` define `vigente | sustituida | **invalidada**`. `F4c` escribe
`vigente | sustituida | **retirada**` y **lo atribuye a `b.3` dos veces**, en §3.7 y en §4.2.

**Y no es un desliz de nombre:** *«`retirada` sí existe en `b.3`, aplicado a otro sujeto»* —
`obligación_retirada`, sobre **obligaciones**, no sobre capas. Y `b.3` advierte expresamente:
*«Producir lo que una obligación exigía y decidir que ya no forma parte del alcance son
resultados DISTINTOS. Si se llaman igual, el sistema puede informar de que entregó algo que en
realidad se eliminó.»* *«`F4c` toma la palabra de un sujeto y la pega al ciclo de otro, que es
la confusión concreta contra la que `b.3` avisa con esas palabras.»*

**¿Debe un documento reutilizar la vigencia de `b.3`? NO, y por dos razones.** Los tres
valores describen *si un resultado puede sostener integración y cierre*; un documento
normativo no sostiene ni integra: **obliga**. Y un documento **retirado del corpus** y uno
**cuyo contenido se declara falso** son cosas distintas, y las dos ocurren.

**Reproducción.** `SIS` deroga un documento porque su contenido resultó incorrecto, sin
reemplazo. `sustituida` exige enlace al reemplazo y no lo hay; `retirada` no está en `b.3`;
`invalidada` no está en el enum de `F4`. **El campo no puede escribirse con ningún valor
válido, y el documento derogado se queda `vigente`.**

**Prescripción.** Dejar de atribuirlo a `b.3` · ciclo propio de **cuatro** valores:
`vigente` · `sustituida` (con enlace obligatorio) · `derogada` (deja de ser exigible, sin
reemplazo) · `refutada` (su contenido resultó falso, y obliga a revisar lo que se apoyó en
ella) · extender la tabla de cruces con `cobertura.estado`, y en particular declarar que una
celda `verificado` sobre un documento `refutada` **no es coherente**.

## `K` · Autoridad de commit y push en recuperación — **CONFIRMADO · GRAVE**

Los cinco puntos del Owner, más un sexto que el revisor añade:

```text
1  NO HAY AUTORIZACIÓN    `W9`/`W10` escriben «se hace», en voz impersonal, sin ninguno de
   PREVIA                 los cinco conceptos de `a.9` que §3.6 obliga a registrar

2  RAMAS PROTEGIDAS       no contempladas, pese a ser la política por defecto de `G29`

3  REMOTO AVANZADO        «el remoto estaba atrasado, no roto» es un SUPUESTO, no una
                          comprobación. `E2.7` admite dos máquinas sobre el mismo control repo

4  FALLO DEL PUSH         sin tope de reintentos —§7.3 lo exige—, sin evento `fallo`, sin
                          estado resultante

5  NO ENCAJA CON `C7`, Y  la tabla de `C7` gobierna las operaciones Git DE LAS FUENTES.
   EL PROBLEMA ES MÁS     NINGUNA fila cubre el repositorio de control. Y `W9`/`W10` son
   PROFUNDO               commits y pushes DEL CONTROL REPO. Luego §7.6 —«C7 declara quién
                          pide, ejecuta, bloquea y verifica cada una»— es FALSA exactamente
                          para las dos operaciones que §2.6.5 automatiza. El gobierno Git del
                          control repo es un HUECO DECLARADO POR OMISIÓN en toda la
                          arquitectura, y F4c lo tapa con una remisión que no resuelve

6  (AÑADIDO) PUBLICACIÓN  `W9` es defendible: `git commit` es local. `W10` publica en
   SIN DECIRLO            infraestructura del Owner y es irreversible en el sentido que §8.1
                          declara: «un rollback NO reescribe historia publicada». F4c es
                          escrupuloso con la publicación al hablar de rollback y la ejecuta
                          sin preguntar al hablar de recuperación. La asimetría no está
                          argumentada
```

**Prescripción.** Separar `W9` de `W10` y **bajar la promesa de `W10`**: el commit local es
recuperación y va sin preguntar; el push **no es recuperación: es publicación**, y pasa a
`esperando-owner` o a la política del producto · **declarar el gobierno Git del control repo**,
que hoy no existe en ninguna parte · los cinco conceptos de `a.9` obligatorios también aquí ·
rama declarada, `main` protegida, push rechazado → evento `fallo`, tope de tres, escalado y
**nunca `--force`** · tres ventanas nuevas en §2.6.5.

---

# 3 · Hallazgos nuevos, fuera de la lista

## `N-1` · «El contrato del aspecto» no existe · **GRAVE**

> *«Es, en mi juicio, el hallazgo más importante fuera de la lista, porque es el mismo modo de
> fallo que la primera crítica descubrió —un artefacto con sujeto y ciclo propios que quedó
> fuera de la prueba del §3.1— reproducido en otra sección y no detectado por la corrección.»*

Se invoca **tres veces** como sede normativa: fija la caducidad de las celdas (§4.2), declara
los responsables de cada área documental (§4.3), y se referencia desde `criterio` como
`contrato:documental/O8` (§5.6). **Y no existe**: sin esquema, sin fichero, sin autoridad, sin
ciclo, sin la prueba del §3.1, y **fuera de los 24 del recuento** — en un §3.8 que abre
presumiendo de que *«el recuento se CALCULA, no se fija de antemano»*.

Aplicándole la prueba honestamente tiene los tres rasgos del paso 4: sujeto propio, autoridad
propia y ciclo propio. *«Probablemente sea, exactamente igual que `nivel-certificacion`, un
segundo esquema de clase, y el recuento debería ser 25, no 24.»*

**Y una `I5` de propina.** `responsables` está declarado como campo de la **celda** (§3.5, y
así se usa en los tres ejemplos) **y** como contenido del **contrato del aspecto** (§4.3).
*«Es literalmente el defecto que la primera crítica encontró con `ultima_verificacion_real`,
corregido allí y reintroducido aquí.»*

## `N-2` · Las tres celdas de §5.6 no caben todas en el contrato · **MEDIO**

El contrato da a la celda **una** `aplicabilidad` sobre el par `(sujeto, aspecto)`. El ejemplo
3b necesita **una aplicabilidad por prueba** y la coloca «DENTRO del criterio» — pero
`criterio` es una **referencia a una norma de clase**, la misma para todas las instalaciones,
y `evidencia_de_inaplicabilidad: SOURCES.toml@a71f3c2` es un dato **de este producto y esta
revisión**: no puede vivir dentro de una norma compartida.

*«La evaluación de inaplicabilidad prueba a prueba —que es lo que `D32` y `PN-6` hacen
imprescindible— no tiene sitio en el contrato. El ejemplo 3b es un contraejemplo de la tesis
que §5.6 dice demostrar.»* Y §9.5 declara que *«LA APLICABILIDAD ES PARTE DEL VEREDICTO»*.

**Prescripción.** Un bloque `evaluacion_de_pruebas` en `cobertura`, con la misma forma que
`integration-set.verificacion` ya usa en el corpus —incluido su `resultado: no-aplica`—, luego
hay precedente y no inventa un patrón.

## `N-3` · §9.2 recorta el enum de `estado` y afirma que no lo toca · **MEDIO**

Diez valores en §3.5, siete en §9.2, y §9.2 declara *«con el contrato de §3.5 sin cambios»*.
*«Los tres que desaparecen no son inocuos: `findings-abiertos` y `corregido-sin-verificar` son
exactamente los dos que §3.5 justifica por `G13`»* — y son los dos estados en los que una
certificación pasa la mayor parte de su vida útil.

## `N-4` · §9.1 y §9.5 enumeran pruebas distintas para el mismo nivel · **MEDIO**

Cuatro pruebas en §9.1, siete en §9.5. *«Un "resumen legible" que omite tres de siete pruebas
no es un resumen: es una segunda lista»* — y `PN-6` fija que «Integrada» significa «todas las
pruebas APLICABLES superadas», de las cuales hay **dos censos distintos**.

Peor: dos de las tres añadidas son comprobaciones de rango **Estructural**, y §9.2 declara que
Integrado **presupone** Estructural. **Y con 0 fuentes la consecuencia es una afirmación
falsa:** las únicas pruebas aplicables serían esas dos, luego una celda `integrado: verificado`
autorizaría a decir que *«fuentes, herramientas, CI, permisos y adaptadores funcionan en el
entorno real»* **sin haber comprobado ninguna de las cinco cosas**. *«§9.5 mitiga con "el
dosier lo dice", pero `O12` no lee el dosier: lee el nivel.»*

**Prescripción.** Una sola lista por nivel, en la clase, y las dos tablas como proyecciones.
Y una regla dura: **un nivel no se alcanza si todas sus pruebas propias resultan no aplicables**.

## `N-5` · «Una instalación nueva tiene CERO fuentes» es falso donde se usa · **MEDIO**

La aplicabilidad se calcula sobre fuentes declaradas en `SOURCES.toml`, que se rellena en
**N2**. La Integrada se certifica en **N7**, después de N2 y de N6. *«Luego en N7 el producto
tiene, por construcción, ≥1 fuente, salvo el caso de un producto sin código. La justificación
de §8.1 es falsa en el único punto donde se invoca»*, y §9.5 la contradice en su propia glosa
(«antes de N6») mientras §8.1 la aplica en N7. El caso de 0 fuentes **existe** —un producto
que no ha declarado ninguna— pero **no es «toda instalación nueva»**.

## `N-6` · Las obligaciones de la `iniciativa` invocan predicados que no existen · **GRAVE**

> *«`Q9` depende de un predicado indefinido, luego la función total de §3.3.1 no es computable
> en su última rama.»*

Los dos predicados de `b.3` están definidos sobre objetos que **una iniciativa no tiene**:
`satisfecha` exige una **capa vigente**, y las capas viven en paquetes, que pertenecen a items
—§3.3 confirma que la iniciativa sólo tiene `items` como referencias—; `retirada` exige una
**recomposición aprobada**, que es `b.9`, definida sobre la **ruta de un item**, y §3.3 no da
campo `ruta` a la iniciativa.

**Conclusión mecánica:** *«toda obligación de iniciativa es huérfana desde que se escribe, y
`Q9` devuelve `bloqueada` para siempre. Una iniciativa con obligaciones nunca puede cerrar. Es
el mismo tipo de bloqueo perpetuo que `D32` corrigió para la Integrada, en otro sitio y sin
detectar.»*

**Prescripción.** Dejar de decir «misma forma que `b.3`» · definir los dos predicados **a
nivel de iniciativa**: satisfecha ≡ *existe una capa vigente **de alguno de sus items**
enlazada explícitamente a la obligación* —la iniciativa no produce capas, las **cita**—;
retirada ≡ *decisión registrada de quien abrió la iniciativa, o del Owner según la materia* ·
registrar la relación con `b.3` como **consumo, no como reutilización**, *«igual que `D29`
hizo, correctamente, con `b.4`»*.

## `N-7` · Las banderas de la iniciativa no tienen semántica de propagación · **MEDIO**

*«`aparcada` es cosmética»*: los items siguen `activo`, `b.12` los sigue seleccionando y
`Continúa` los sigue despachando. Y *«`cancelando` no tiene salida»*: `Q1` da `cancelando`
mientras haya un item vivo, y nada cancela esos items, luego `Q2` es inalcanzable salvo por
acción manual. **Prescripción:** declarar la propagación —como **propuesta en lote** al Owner,
porque §5.4 ya dice que cancelar es autoridad semántica— o declarar que la bandera es sólo
informativa, con la consecuencia escrita.

## `N-8` · §3.2 afirma un mapeo uno a uno con `b.16` que no existe · **MEDIO**

El §20.8 no mapea uno a uno: `SEG` **no es un proceso** de `b.16`; **dos filas no producen
item**; **tres procesos no aparecen** (`INC`, `DEP`, `AUD`); y una fila es ambigua entre dos.
*«El veredicto de §3.2 —`finding` no es un tipo— sigue siendo correcto; lo que es falso es el
argumento con el que lo sostiene. Y como el corpus toma decisiones de tipo por argumento, un
argumento falso es un defecto aunque la conclusión aguante.»*

## `N-9` · §7.4 altera el paso 2 de `b.14` mientras declara conservarlo · **MEDIO · genera presión**

Donde (b) escribe «completar o **revertir**», `F4c` escribe «completar o **marcar
conflicto**», y §2.6 elimina el ramal de reversión. *«La decisión de roll-forward only es
buena y está bien argumentada —lo digo sin reservas—, y satisface la disyunción de `a.9`. Lo
que no es aceptable es hacerlo declarando que el texto de (b) se conserva entero, sin
registrar la desviación en ninguna parte.»* → **`PN-7`**.

## `N-10` · La raíz de confianza de `P-08` se relocaliza, no se elimina · **MEDIO**

La evidencia de `negativos` **la publica el runner**. *«Luego "la corrección del runner la
comprueban unas pruebas cuya evidencia publica el runner" es circularidad desplazada un paso,
no eliminada. La sección lo reconoce cuatro líneas después con toda honestidad; lo que sobra
es la frase "elimina la circularidad de raíz", que contradice a su propia conclusión.»*

Y un hueco de alcance: §11 gobierna los trece validadores y **no dice nada de los dos
generadores**, cuyos artefactos padecen *«exactamente el defecto que `P-08` existe para
cerrar»*. El revisor observa que *«ése es el defecto vivo del repositorio: los dos últimos
commits de esta rama son literalmente "N158g reancla su cifra al corpus con el documento
nuevo"»*.

## `N-11` · `verificador` no tiene ruta que lo produzca, y confunde dos papeles · **MEDIO**

`VER` **no está en la ruta `AUD`** de `b.16`, ni obligatoria ni condicional —la única
obligatoria es `INV`—, y sin embargo las tres celdas de §5.6 declaran `verificador: VER` y
citan un `DICTAMEN`. **Ninguna ruta produce ese dictamen en una auditoría.** Y el campo
significa dos cosas: en §5.3 la verificación de la **corrección**; en §5.6, quien **auditó**.
*«Que es literalmente lo que §5.6 promete que no ocurre.»* → partir el campo, y **`PN-8`**.

## `N-12` · La tabla de ventanas se declara exhaustiva y no lo es · **MENOR**

Faltan al menos cuatro: temporal de `confirmada` a medio escribir —cuyo tratamiento **es
distinto** del de `preparada`, porque los canónicos ya están aplicados—; push parcial o
rechazado; caída durante la creación del marcador; y **caída de máquina**, que no es caída de
proceso y que ninguna fila distingue.

## `N-13` · Overclaims de literalidad y recuentos que ya no casan · **MENOR**

`§1.3` dice «las tres son `a.9` literal» y la primera regla viene de `a.7` · «tres huellas» en
§11.2, en `D31` y en el checkpoint, cuando se definen **dos** más un artefacto que las lleva ·
el documento 12 remite a **§5.7** cuando los ejemplos están en §5.6, y dice **SEIS** escenarios
cuando §11.5 tiene **diez** · §6.3 promete detección de deriva del puntero sin declarar que
sólo puede ejercerla si la fuente está materializada.

## `N-14` · `O11` dice «estado durable» y `F4c` deriva el estado · **MENOR, de método**

La lectura benigna es defendible y probablemente correcta. *«Pero `F4c` registró `PN-6`
precisamente porque reinterpretar la precondición de una resolución del Owner "es materia
suya". La misma vara exige aquí, como mínimo, una frase.»* → **`PN-10`**.

---

# 4 · Hallazgos rechazados

```text
`G` EN SU PREMISA CENTRAL      §8.3 dice literalmente lo contrario de lo que el Owner le
                               atribuye. `D33` es correcta en su núcleo

«Q0–Q9 NO ES TOTAL NI          verificado enumerando: los ocho estados VIVOS de `b.4` quedan
DISJUNTA»                      cubiertos por Q0, Q5, Q6, Q7 y los cuatro que Q8 enumera. «Es
                               total», y la precedencia la hace disjunta por construcción.
                               Única imprecisión MENOR: la glosa atribuye a Q1/Q2 la
                               cobertura de `cancelando`/`cancelado` de ITEM, y esos dos se
                               disparan por la bandera de la INICIATIVA

«LAS TRES CELDAS NO CABEN»     rechazado EN SU FORMA GENERAL: los ejemplos 1 y 2 caben
                               limpiamente, campo a campo. Sólo rompe la segunda celda del
                               ejemplo 3, y por la razón concreta de `N-2`

«EL PUNTERO COPIA              §6.7 regla 3 prohíbe explícitamente todo conocimiento y
CONOCIMIENTO A LAS FUENTES»    declara un criterio de tamaño con validador. «El diseño del
                               CONTENIDO del puntero es correcto y respeta `C6` y
                               `CAND-016`». Lo que falla es cardinalidad, resolución y
                               circuito de escritura — no su contenido

«D23–D33 NO DESCRIBEN LO QUE   rechazado SALVO UNA: las once se cotejaron contra el texto
DICE EL DOCUMENTO 11»          vigente y diez son exactas. La única inexacta es `D31`
                               («tres huellas»). «Y la disciplina de no reescribir D16–D22
                               es metodológicamente correcta y bien ejecutada»

«PN-4 SE RETIRÓ SIN            «Es una retirada bien hecha»: el motivo está escrito, es
JUSTIFICACIÓN»                 correcto y es comprobable, y deja explícita la vía de
                               reinstauración. Nota menor: `reconciliacion-pendiente` sí
                               coincide con un estado de `b.4`, lo que debilita —no anula—
                               el argumento «su vocabulario es DISTINTO»

«PN-1, PN-2, PN-3, PN-6 MAL    las cuatro están correctamente identificadas y acotadas, y la
ENCUADRADAS»                   decisión de no renumerar es correcta
```

---

# 5 · Presiones normativas nuevas — `PN-7` a `PN-10`

**Ninguna se redacta aquí.** Redactarlas es F5, y su puerta es el Owner.

```text
PN-7 · CANDIDATA · b.14 paso 2 dice «completar o revertir»
   QUÉ PRESIONA    (b) b.14 paso 2
   QUÉ CAMBIA      §2.6 elige roll-forward only y retira el ramal de reversión. La
                   disyunción de a.9 lo admite; la enumeración de b.14 no lo dice
   MATERIA MÍNIMA  una frase: «completar, o marcar conflicto y escalar»
   BLOQUEA         nada que no bloquee ya PN-1. Es coherencia, no capacidad
   ORIGEN          hallazgo N-9

PN-8 · CANDIDATA · VER no está en la ruta AUD de b.16
   QUÉ PRESIONA    (b) b.16, fila AUD: obligatorias = INV
   QUÉ CAMBIA      §5.3 y las tres celdas de §5.6 exigen un dictamen de VER con
                   independencia declarada para que una celda llegue a `verificado`
   MATERIA MÍNIMA  añadir VER como condicional de AUD, o que F4 nombre otro productor
   BLOQUEA         que una celda de cobertura alcance `verificado` con evidencia
   ORIGEN          hallazgo N-11

PN-9 · CANDIDATA · obligaciones de iniciativa y los predicados de b.3
   QUÉ PRESIONA    (b) b.3, cuyas definiciones se apoyan en capa vigente y recomposición
                   aprobada — objetos que una iniciativa no tiene
   QUÉ CAMBIA      Q9 de §3.3.1 depende de esos predicados y hoy no es computable
   MATERIA MÍNIMA  probablemente NINGUNA: pueden definirse a nivel de iniciativa en (g),
                   consumiendo b.3 sin redefinirla — la vía por la que PN-4 se retiró.
                   F5 debe CONFIRMARLO, no darlo por hecho
   ORIGEN          hallazgo N-6

PN-10 · CANDIDATA · O11 dice «estado durable» de la iniciativa
   QUÉ PRESIONA    O11, resolución del Owner del 2026-08-27
   QUÉ CAMBIA      §3.3 y D29 derivan el estado y no lo persisten
   MATERIA MÍNIMA  una frase que fije cuál de las dos lecturas rige. Es el mismo trato que
                   PN-6 da a O12, y la simetría lo exige
   ORIGEN          hallazgo N-14
```

**Y lo que explícitamente NO es presión normativa**, dicho por el revisor para que nadie lo
lleve al Owner:

```text
`C7` gate:convergencia-de-fuentes   material DERIVADO de E2. Su corrección está
                                    completamente determinada por E2.6 y NO requiere
                                    decisión del Owner. Es un DEFECTO DE DERIVADO con
                                    prescripción cerrada, y su sitio es F6. Lo que F4 debe
                                    hacer HOY es REGISTRARLO

las cuatro extensiones de ficha     verificado contra b.16: PLT es propietario global de
de §5.2                             DEP y `SEG:condiciones ⊳ CON` es OBLIGATORIO por G28.
                                    Extender fichas con materia que ya está en su alcance
                                    es trabajo de F6, no presión
```

---

# 6 · Límites que el revisor declara no haber podido adjudicar

```text
EL COSTE REAL DEL          tres puntos de fsync por transacción —cuatro tras corregir E—
PROTOCOLO                  y toda transición es una transacción. Si el coste hace inviable
                           el ritmo, la solución no es quitar fsync sino agrupar
                           transiciones, y eso cambia el diseño. Sale del piloto

SI `X09` ES REALIZABLE     el algoritmo de detección de bifurcación no está definido.
                           «X09 está en la tabla adversarial como si fuera comprobable, y
                           no lo es todavía»

SI `plano` Y `capa` SE     el argumento de §1.2 y §4.1 es correcto en el papel. Sólo la
MANTIENEN SEPARADOS        adopción real de un producto dirá si alguien intenta clasificar
                           conocimiento con `plano`

EL PESO DE `indice.sqlite` la presión práctica hacia «leer del índice porque es más
FRENTE A R1                rápido» sólo se mide construyendo. Está bien declarado y no es
                           un defecto hoy

QUÉ NO VERIFICÓ            el contenido íntegro de C1, C2, C3, C4 y C5, ni las quince
                           fichas de capacidad, ni los diez procesos fuera de las filas
                           citadas. «Una afirmación de F4 sobre C1, C3 o C5 podría estar
                           mal y yo no lo habría visto»
```

---

# 7 · Veredicto de suficiencia

**Transcrito literal, y es el que gobierna el estado de la fase.**

> **`F4c` NO puede cerrarse. Hay defectos bloqueantes.**

Y su observación final, que también se transcribe entera porque no es un hallazgo pero sí un
juicio:

> *«`F4c` es un documento honesto: dice repetidamente que nada está construido, que nada está
> probado, que quien aplicó la crítica es quien la recibió, y que la tabla adversarial es el
> contrato de una demostración y no la demostración. Esa disciplina es real y no la discuto.
> Pero la honestidad sobre lo que falta no sustituye a la corrección de lo que está escrito, y
> esta segunda revisión encuentra que **la pieza que la primera crítica declaró no ejecutable
> sigue sin serlo**, por dos defectos nuevos que la corrección introdujo o no vio. El
> diagnóstico de `F4c` sobre sí misma —"pendiente de una segunda revisión independiente"— era
> exactamente el correcto, y el resultado de esa revisión es que la fase no cierra.»*

## Qué se ha aplicado, y qué eso NO acredita

Las doce correcciones que el revisor ordena están aplicadas en
[`11-ARQUITECTURA-INTEGRADA.md`](11-ARQUITECTURA-INTEGRADA.md) y registradas como `D34`–`D45`.
**Las aplicó el autor material de F4, que es quien las recibió.**

```text
QUÉ ESTÁ HECHO        las doce correcciones, escritas
QUÉ NO ESTÁ HECHO     comprobarlas. Ninguna la ha revisado nadie independiente
QUÉ NO ESTÁ PROBADO   ninguna de las pruebas adversariales X18–X46. Están ESCRITAS
QUÉ NO SE HA TOCADO   (a), (b), E1, E2, K-1, C4 — y tampoco C7, cuya corrección queda
                      REGISTRADA con su prescripción cerrada y su trazabilidad a E2.6
ESTADO DE F4c         ABIERTA. Exige una TERCERA revisión independiente que examine el
                      resultado corregido y emita un veredicto explícito de suficiencia
```

**Ese veredicto no está en este documento, y quien lo escribió no puede darlo.**
