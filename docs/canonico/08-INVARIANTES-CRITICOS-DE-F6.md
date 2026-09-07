# 08 · INVARIANTES CRÍTICOS DE `F6` — el catálogo `K01`–`K24`, con su prueba

> **QUÉ ES ESTA SEDE.** `O30` §2 fija el universo crítico de `F6` en VEINTICUATRO
> invariantes arquitectónicos y declara el catálogo **CERRADO** para este ciclo. Ésta es la
> sede canónica donde cada uno de ellos queda ligado a lo que `O30` §3 exige: fuente
> normativa, mecanismo implementado, canal productivo, caso sano, prueba adversarial,
> resultado esperado, evidencia reproducible y vínculo al commit y al tree juzgados.
>
> **NO ES LA FUENTE DEL CATÁLOGO.** La sede del catálogo es
> [`docs/owner/ADS-OWNER-RESOLUCIONES.md`](../owner/ADS-OWNER-RESOLUCIONES.md), `O30` §2, y
> está bajo el cliquet de append-only. Aquí no se inscribe, no se amplía y no se reformula
> ningún invariante: se **enlaza** lo que aquella dice con lo que el árbol tiene.
>
> **NO CERTIFICA NADA.** `O30` §7 reserva la declaración de `F6 CERTIFICADA` o `F6 CERRADA`
> a un único verificador independiente, y enumera ocho condiciones de las que este catálogo
> es sólo la primera. Un `estado: SATISFECHO` de aquí abajo significa exactamente
> «`O30` §3 se cumple sobre este invariante, medido», y nada más.

## Cómo se lee, y por qué no hay ningún cardinal escrito

**El conjunto se DERIVA.** Ni esta sede ni su instrumento escriben en ninguna parte cuántos
invariantes hay. El ejecutable
[`docs/evolucion/verificacion/comprobar-invariantes-criticos.py`](../evolucion/verificacion/comprobar-invariantes-criticos.py)
lee las viñetas de `O30` §2, obtiene de ahí el conjunto Y la formulación literal de cada uno,
y contrasta esa derivación con las fichas de abajo **en los dos sentidos**: si falta un `K` da
rojo, si sobra un `K` que la resolución no autoriza da rojo, y si una formulación de aquí no
es la de allí, palabra por palabra, da rojo. El día que el Owner inscriba un `K25` esta sede
quedará roja sola, sin que nadie tenga que acordarse de contar.

**Cada ficha es DATO, no prosa.** Vive en un bloque vallado `ads:invariante` con claves
fijas. Lo que declara se comprueba: las fuentes tienen que existir y decir lo que se les cita;
las rutas de implementación tienen que estar en el árbol; el canal declarado tiene que ser el
que sus sabotajes ejercen de verdad; cada prueba positiva tiene que figurar SUPERADA —y no
saltada— en una evidencia que sea la de ESTE commit y ESTE tree, blob a blob; y cada prueba
adversarial tiene que existir en el catálogo único de mutaciones, nombrar una prueba que esta
misma ficha declara, y **ponerse roja al ejercerla, por el motivo declarado**.

**La prueba compartida.** `O30` §3 admite que un mismo sabotaje acredite a varios invariantes
sólo con cuatro condiciones. Las cuatro están mecanizadas: se ejecuta el mecanismo compartido
—no se lee—, el sabotaje tiene que apuntar a una prueba que el invariante declara, la ficha
tiene que explicar en `vinculo:` qué observación **distinta** demuestra aquí, y el ciclo tiene
que volver rojo por el motivo que el catálogo de mutaciones declara. Sin las cuatro, rojo.

**Un `NO SATISFECHO` es un resultado legítimo.** Esta sede no existe para que salga verde;
existe para que lo que salga sea verdad. El campo `limites:` de cada ficha dice lo que su
prueba **no** demuestra, y está escrito para leerse antes que el `estado:`.

## Los comandos

```console
$ python3 docs/evolucion/verificacion/comprobar-invariantes-criticos.py --autopruebas
$ python3 docs/evolucion/verificacion/comprobar-invariantes-criticos.py
$ python3 docs/evolucion/verificacion/comprobar-invariantes-criticos.py --solo K13
```

El primero ejerce los modos de fallo cerrado sobre el propio juez: un instrumento que no sabe
decir que no, no mide. El segundo deriva, comprueba y **ejecuta** los sabotajes, y es el que
publica evidencia. El tercero mide un solo invariante.

## Lo que este catálogo NO cubre

- las obligaciones funcionales **no críticas** de `O30` §4, que son de `O26-IMPL`;
- las ocho condiciones de `O26` §1, que `O30` §5 manda volver a ejercer y que ejerce
  [`ejercer-o26-condiciones.py`](../evolucion/verificacion/ejercer-o26-condiciones.py);
- `M-04` y `C-L.7`, que `O30` §6 reserva al verificador independiente;
- la certificación de `F6`, que es `O30` §7 y no es de ningún instrumento.

---

# Las fichas

## `K01`

```ads:invariante
id: K01
formulacion: Una transición confirmada sobrevive a caída, reinicio y recuperación.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K01` ·
  - kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md :: ## 4 · Recuperación — las dos ramas de `g.8`, y no hay una tercera
implementacion:
  - kernel/operativo/runtime/estado/motor.py
  - kernel/operativo/runtime/estado/rutas.py
canal:
  - kernel/operativo/runtime/pruebas/test_estado_durable.py
positivas: T175 T299 T300
adversariales: N175 NK01a
resultado: Adelantar el punto de no retorno o quitarle al testigo del paso 8 el `fsync` del DIRECTORIO tiene que poner ROJA la batería del estado durable, y por el motivo declarado: una transición confirmada dejaría de sobrevivir a la caída porque su constancia en disco tendría bytes y no tendría nombre.
evidencia:
  - kernel/operativo/pruebas/evidencia/estado-durable-salida.txt
vinculo:
  - T300 :: `T300` acredita aquí la SUPERVIVENCIA: tras la caída y la recuperación la transición queda COMPLETA y el almacén ÍNTEGRO. La observación es el estado final.
estado: SATISFECHO
limites: El corte se siembra por los puntos de fallo controlados del motor, que son procesos reales pero no un corte de corriente real: lo que se demuestra es que las primitivas de durabilidad se INVOCAN sobre el testigo y el directorio, no que un anfitrión concreto las honre.
```

## `K02`

```ads:invariante
id: K02
formulacion: Una transición no confirmada nunca se publica como estado canónico.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K02` ·
  - kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md :: ## 3 · Protocolo transaccional
implementacion:
  - kernel/operativo/runtime/estado/motor.py
  - kernel/operativo/runtime/estado/transaccion.py
canal:
  - kernel/operativo/runtime/pruebas/test_estado_durable.py
positivas: T174 T297 T298
adversariales: N174 NK02a
resultado: Que el paso 9 deje de exigir que el testigo cubra EXACTAMENTE las rutas del plan, o que la zona de preparación entre en el versionado, tiene que poner roja la batería: una publicación a medias pasaría a ser vigente.
evidencia:
  - kernel/operativo/pruebas/evidencia/estado-durable-salida.txt
estado: SATISFECHO
limites: `NK02a` abre el hueco pero en la fixture de `T298` el canal siguiente —el contraste `cid` a `cid`— detiene igualmente la publicación; lo que cae, y lo que se declara, es que el veredicto deja de NOMBRAR la mezcla parcial. Un plan cuya ruta sobrante ya tuviera el `cid` correcto pasaría entero, y ese caso no tiene prueba propia.
```

## `K03`

```ads:invariante
id: K03
formulacion: La publicación del estado es atómica y conserva el orden contractual entre preparación, publicación y confirmación.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K03` ·
  - kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md :: ## 3 · Protocolo transaccional
  - kernel/operativo/runtime/CONTRATO-RAIZ-EXTERNA.md :: ## 6 bis · El ORDEN de la verificación, y cuándo se puede escribir evidencia
implementacion:
  - kernel/operativo/runtime/estado/motor.py
  - kernel/operativo/raiz-externa/atestacion.py
canal:
  - kernel/operativo/runtime/pruebas/test_estado_durable.py
  - kernel/operativo/runtime/pruebas/test_raiz_externa.py
positivas: T296 T300 T323
adversariales: NK03a NK03b
resultado: Adelantar el punto de corte por delante del testigo del paso 8, o invertir el orden interno de `escribir_evidencia`, tiene que poner rojas sus dos baterías: en el primer caso la caída deja objetos publicados sin constancia; en el segundo queda fichero de evidencia de una verificación cortada.
evidencia:
  - kernel/operativo/pruebas/evidencia/estado-durable-salida.txt
  - kernel/operativo/pruebas/evidencia/raiz-externa-salida.txt
vinculo:
  - T300 :: `T300` acredita aquí el ORDEN: el testigo del paso 8 está en disco y la revisión del 9 NO avanzó. La observación es la frontera entre los dos pasos, leída en el instante del corte y antes de recuperar nada.
estado: SATISFECHO
limites: El orden se comprueba en los dos sitios donde el corpus lo instancia —el almacén durable y la puerta de evidencia de la raíz externa—. No hay una comprobación GENÉRICA de orden contractual que alcance a un tercer mecanismo que se añadiera mañana.
```

## `K04`

```ads:invariante
id: K04
formulacion: Recuperar o reanudar repetidamente es idempotente y no duplica efectos.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K04` ·
  - kernel/operativo/runtime/CONTRATO-RUNTIME-Y-DISPATCHER.md :: ## 3 · Idempotencia del efecto — dos niveles, y no son redundantes
implementacion:
  - kernel/operativo/runtime/adaptadores/proceso.py
  - kernel/operativo/runtime/runtime/dispatcher.py
canal:
  - kernel/operativo/runtime/pruebas/test_adaptadores.py
positivas: T186 T191 T324
adversariales: N191
resultado: Que un recibo ABIERTO deje de dar `ambiguo` tiene que poner roja la batería de adaptadores: el efecto se vuelve a ejecutar al recuperarse, que es exactamente lo que la idempotencia impide.
evidencia:
  - kernel/operativo/pruebas/evidencia/runtime-salida.txt
  - kernel/operativo/pruebas/evidencia/adaptadores-salida.txt
  - kernel/operativo/pruebas/evidencia/estado-durable-salida.txt
estado: SATISFECHO
limites: El sabotaje ejerce el nivel de RECIBO. El segundo nivel de idempotencia —la reejecución de una migración o de una recuperación completas— sólo tiene caso positivo (`T324`, `T186`) y no mutante propio.
```

## `K05`

```ads:invariante
id: K05
formulacion: La concurrencia no permite dos confirmaciones para la misma revisión.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K05` ·
  - kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md :: ## 5 · Concurrencia
implementacion:
  - kernel/operativo/runtime/estado/motor.py
  - kernel/operativo/runtime/estado/bloqueo.py
canal:
  - kernel/operativo/runtime/pruebas/test_estado_durable.py
positivas: T176 T221 T234
adversariales: N176
resultado: Declarar el agotamiento de reintentos por el camino que NO abre el registro tiene que poner roja la batería: dos escritores dejarían de serializarse con constancia, y el doble éxito para una revisión pasaría inadvertido.
evidencia:
  - kernel/operativo/pruebas/evidencia/estado-durable-salida.txt
  - kernel/operativo/pruebas/evidencia/multimaquina-salida.txt
  - kernel/operativo/pruebas/evidencia/agentes-salida.txt
vinculo:
  - T221 :: `T221` acredita aquí que dos MÁQUINAS sobre la misma autoridad producen UNA sola confirmación: la observación es la exclusión.
estado: SATISFECHO
limites: `T221` mide dos máquinas sobre la misma autoridad y `T234` dos procesos sobre un `execution_slot`, pero el único sabotaje imputado ataca la serialización del almacén. Las otras dos superficies tienen caso positivo y no mutante.
```

## `K06`

```ads:invariante
id: K06
formulacion: Diario, registro y cabezas durables detectan corrupción, truncamiento, sustitución y retirada de cola.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K06` ·
  - kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md :: ## 6 bis · Sellado del diario — la mitad de `g.7` que faltaba
implementacion:
  - kernel/operativo/runtime/estado/diario.py
  - kernel/operativo/runtime/estado/motor.py
canal:
  - kernel/operativo/runtime/pruebas/test_estado_durable.py
positivas: T177 T311 T319
adversariales: N177
resultado: Que el `cid` del objeto canónico deje de contrastarse contra `REVISION.json` tiene que poner roja la batería: la corrupción, el truncamiento y la sustitución dejarían de fallar cerrado.
evidencia:
  - kernel/operativo/pruebas/evidencia/estado-durable-salida.txt
  - kernel/operativo/pruebas/evidencia/integridad-evidencia-salida.txt
estado: SATISFECHO
limites: La retirada de cola del diario la cubre `T319` como caso positivo sobre un diario sellado; el sabotaje imputado ataca el contraste del canónico, que es la vía por la que `T177` la observa.
```

## `K07`

```ads:invariante
id: K07
formulacion: Una reconciliación sólo puede cerrarse mediante una transición autorizada y auditable.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K07` ·
  - kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md :: ## 6 · Reconciliación
implementacion:
  - kernel/operativo/runtime/estado/reconciliacion.py
  - kernel/operativo/runtime/estado/motor.py
canal:
  - kernel/operativo/runtime/pruebas/test_estado_durable.py
positivas: T178 T317 T318
adversariales: N178
resultado: Que la cabeza del registro auxiliar deje de anclar su extremo AL LEER tiene que poner roja la batería: una reconciliación pendiente dejaría de deducirse del registro, y podría retirarse sin transición explícita.
evidencia:
  - kernel/operativo/pruebas/evidencia/estado-durable-salida.txt
estado: SATISFECHO
limites: El sabotaje ataca la DEDUCCIÓN de la pendencia. La autorización de la transición que la cierra tiene caso positivo (`T178`, `T317`) y no mutante propio.
```

## `K08`

```ads:invariante
id: K08
formulacion: Versiones y migraciones preservan integridad, usan errores tipados y fallan cerradas ante formatos desconocidos o estados imposibles.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K08` ·
  - kernel/operativo/runtime/CONTRATO-ESTADO-DURABLE.md :: ## 7 · Versionado y migración
implementacion:
  - kernel/operativo/runtime/estado/migracion.py
  - kernel/operativo/runtime/estado/errores.py
canal:
  - kernel/operativo/runtime/pruebas/test_estado_durable.py
positivas: T179 T320 T321 T325
adversariales: N179 N320 N321
resultado: Abrir una versión de formato desconocida en vez de fallar cerrado, publicar la revisión 0 sin el testigo de `E-08`, o devolver la guarda de la fundación al evento del diario, tienen que poner roja la batería, cada uno por su motivo.
evidencia:
  - kernel/operativo/pruebas/evidencia/estado-durable-salida.txt
estado: SATISFECHO
limites: Los tres sabotajes cubren el formato desconocido y la migración `0→1`. Una migración `1→2` que todavía no existe no está probada, y no puede estarlo.
```

## `K09`

```ads:invariante
id: K09
formulacion: Toda evidencia, atestación o certificación queda ligada conjuntamente al commit y al tree realmente juzgados.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K09` ·
  - kernel/operativo/runtime/CONTRATO-RAIZ-EXTERNA.md :: ## 5 · `G-A9` · un veredicto falseado desde dentro es DESMENTIDO
implementacion:
  - kernel/operativo/raiz-externa/verificador.py
  - kernel/operativo/raiz-externa/atestacion.py
canal:
  - kernel/operativo/runtime/pruebas/test_raiz_externa.py
positivas: T220 T290 T291 T292
adversariales: NK09a
resultado: Retirar el careo entre la autodeclaración del árbol y el color atestado desde fuera tiene que poner roja la batería con `VEREDICTO_DESMENTIDO` ausente: el árbol volvería a poder certificarse a sí mismo.
evidencia:
  - kernel/operativo/pruebas/evidencia/raiz-externa-salida.txt
estado: SATISFECHO
limites: El vínculo commit+tree tiene control positivo y las dos mitades separadas (`T290`, `T291`, `T292`) y un solo mutante, el del careo. La sustitución de la tupla firmada la cubre `T293`, sin mutante propio.
```

## `K10`

```ads:invariante
id: K10
formulacion: Firma, verificación, rotación y revocación fallan cerradas y no confunden claves de prueba con custodia productiva.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K10` ·
  - kernel/operativo/runtime/CONTRATO-RAIZ-EXTERNA.md :: ## 6 · Rotación, solapamiento y revocación · `O25` §5
implementacion:
  - kernel/operativo/runtime/identidad
  - kernel/operativo/raiz-externa/firma.py
canal:
  - kernel/operativo/runtime/pruebas/test_identidad.py
  - kernel/operativo/runtime/pruebas/test_raiz_externa.py
positivas: T192 T217 T218 T294
adversariales: N192 N217
resultado: Permitir que la configuración de confianza viva dentro del árbol, o que una instalación ALTERADA emita veredicto, tiene que poner rojas sus baterías: la custodia productiva dejaría de estar fuera del objeto juzgado.
evidencia:
  - kernel/operativo/pruebas/evidencia/identidad-salida.txt
  - kernel/operativo/pruebas/evidencia/raiz-externa-salida.txt
estado: SATISFECHO
limites: La custodia PRODUCTIVA de claves es externa por resolución competente y este ciclo no la ejerce: lo que se prueba aquí es que una clave efímera de prueba no la sustituye y que la configuración de confianza no cabe dentro del árbol. La revocación tiene caso positivo (`T294`) y no mutante.
```

## `K11`

```ads:invariante
id: K11
formulacion: Autoridad, productor, escritor y custodio permanecen separados conforme a sus contratos.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K11` ·
  - docs/canonico/03-GOBIERNO-Y-AUTORIDAD.md :: # 03 · GOBIERNO Y AUTORIDAD
  - kernel/operativo/runtime/CONTRATO-RAIZ-EXTERNA.md :: ## 3 · La clave privada, y lo que nunca sale
implementacion:
  - kernel/operativo/capacidades
  - kernel/operativo/raiz-externa/verificador.py
canal:
  - kernel/operativo/validadores/comprobar_contratos.py
positivas: T86 T136 T146 T219
adversariales: N136 N146
resultado: Declarar un veto levantable prevaleciente sobre otro, o conceder a un rol lo que su capacidad ESCALA, tiene que poner rojo el validador de contratos por el punto exacto que cada uno rompe.
evidencia:
  - kernel/operativo/pruebas/evidencia/contratos-salida.txt
  - kernel/operativo/pruebas/evidencia/raiz-externa-salida.txt
estado: SATISFECHO
limites: La separación productor/escritor/custodio en la raíz externa tiene caso positivo (`T219`) y no mutante propio: los dos sabotajes imputados atacan la separación de AUTORIDAD entre capacidades y roles.
```

## `K12`

```ads:invariante
id: K12
formulacion: El entorno, la procedencia del código y las rutas de importación no permiten contaminación silenciosa del ejecutable juzgado.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K12` ·
  - kernel/operativo/runtime/CONTRATO-RAIZ-EXTERNA.md :: ### 1 bis · `E-10` en la raíz externa, y por qué el inventario se DERIVA
implementacion:
  - kernel/operativo/validadores/aislamiento_de_arranque.py
  - kernel/operativo/runtime/ads_admision.py
  - kernel/operativo/runtime/ads_ciclo.py
canal:
  - kernel/operativo/runtime/ads_ciclo.py
  - kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py
positivas: T306 T330 T337 T364 T380
adversariales: NK12a NK12b NK12c N330 NG03
resultado: Retirar a un punto ejecutable la guarda y la purga a la vez, retirar la comprobación de procedencia, retirarle la orden que la publica, o dejar sin purga al verificador de la raíz externa, tienen que poner rojo el canal correspondiente, cada uno por su motivo.
evidencia:
  - kernel/operativo/pruebas/evidencia/integridad-evidencia-salida.txt
  - kernel/operativo/pruebas/evidencia/e2e-f6-salida.txt
estado: SATISFECHO
limites: `NK12c` no vive en el catálogo único: `T364` se publica por líneas en un escenario que no es una batería `unittest`, y `comprobar_negativos` no sabe leer ese formato. El ciclo lo ejerce este instrumento contra el mismo mecanismo —la orden `procedencia`—, y eso queda dicho aquí en vez de contarse como cobertura del catálogo.
```

## `K13`

```ads:invariante
id: K13
formulacion: La sede del Owner es append-only por ENTRADAS COMPLETAS y no puede aprobar una sustitución, truncamiento o reescritura de resoluciones.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K13` ·
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: ## 3 · Protección append-only
  - kernel/operativo/runtime/CONTRATO-ADMISION.md :: ## 5 · El instrumento se incluye a sí mismo · `V6-11` · `V6-12`
implementacion:
  - kernel/operativo/runtime/admision/sede.py
  - kernel/operativo/runtime/admision/perimetro.py
canal:
  - kernel/operativo/runtime/pruebas/test_admision.py
positivas: T340 T342 T343 T344 T345 T349
adversariales: NK13a NK13b NK13c N340 N343
resultado: Reanclar las entradas al último commit, dejar de anotar la ausencia de una entrada cerrada, juzgar el orden como conjunto, volver al prefijo del nacimiento o retirar la comparación byte a byte tienen que poner roja la batería de admisión, cada uno por su motivo y ninguno por el de otro. OBSERVADO: los CINCO, cada uno por el suyo. `N340` volvió a detectarse tras la corrección que `limites` narra —`FAIL T342 · ADJ-B3 literal`— y no queda ningún adversarial de esta ficha sin detectar.
evidencia:
  - kernel/operativo/pruebas/evidencia/admision-salida.txt
estado: SATISFECHO
limites: Las tres formas del ataque que no altera bytes visibles —anclar mal, truncar, permutar— tienen ahora mutante propio con su motivo exacto (`NK13a`, `NK13b`, `NK13c`), y `N343` sigue firme; `NK13b` deja además registrado que la propiedad estaba defendida por DOS canales y que hacen falta los dos para derrotarla.
    LO QUE ESTE INVARIANTE PUBLICÓ COMO INCUMPLIDO DURANTE ESTE CICLO, Y YA NO. Este párrafo es HISTORIA y se conserva entero; el estado vigente es el de `estado:` y `resultado:`, y es SATISFECHO. `N340` —el sabotaje que `ADJ-B3` escribió para `T342`, «el append-only vuelve al PREFIJO del nacimiento»— YA NO PRODUCE SU MOTIVO. Medido sobre el árbol de `HEAD`, sin ninguna edición de este ciclo: la sustitución textual de la mutación ya no encaja con el `perimetro.py` que el hallazgo `#20` reescribió para juzgar la sede en sus TRES capas, y lo que sale es `NameError: name 'capas' is not defined`. Una traza no es una detección: es exactamente el modo de fallo que el campo `espera` existe para descalificar, y por eso `comprobar_negativos` publicó entonces `N340` como NO DETECTADA y este catálogo publicó `K13` como incumplido. Eso fue el estado de aquel momento, no el de hoy.
    CERRADO POR EL COORDINADOR, Y EL DIAGNÓSTICO SE CONSERVA ENTERO. La causa era del coordinador y de este mismo expediente: la corrección del hallazgo `#20` introdujo `capas` DENTRO del tramo que `N340` recorta, sin advertir que un sabotaje cortaba por ahí. El remedio NO ha sido reescribir la mutación —eso habría hecho que dejara de demostrar lo que demostró el día que se escribió, que es lo que `A1` argumentó bien— sino SUBIR lo que los dos regímenes comparten por encima del rótulo que la mutación usa como ancla, de modo que `N340` vuelve a recortar SÓLO el régimen que dice recortar. Medido: `N340` → `detectada: FAIL T342 · ADJ-B3 literal: lo que el prefijo del nacimiento dejaba pasar`, y `test_admision` 101 OK. El párrafo de arriba se conserva porque describe un defecto que existió y que sólo este instrumento vio.
    LO QUE ESO SIGNIFICA, Y LO QUE NO. NO significa que el append-only esté desprotegido: cuatro sabotajes de esta misma ficha lo ponen rojo por su motivo, y el ataque de `ADJ-B3` —borrar entradas posteriores al nacimiento y sustituirlas— sigue teniendo a `N342` en el catálogo. Significa que un mutante DECLARADO dejó de demostrar lo que decía demostrar y nadie lo vio hasta ahora. El remedio NO fue reescribir la mutación —eso se descartó, y se dice por qué: el catálogo de mutaciones es ACUMULATIVO, y una mutación que se reescribe deja de demostrar lo que demostró el día que se escribió; retirarla de esta ficha para que el recuento saliera verde sería elegir los sabotajes que pasan, que es la clase de vaciado que `O30` §4 prohíbe expresamente. Lo que se corrigió fue el `perimetro.py`, que era donde estaba el defecto.
```

## `K14`

```ads:invariante
id: K14
formulacion: El verificador de admisión juzga la mutación efectiva y falla cerrado ante cambios fuera del universo permitido.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K14` ·
  - kernel/operativo/runtime/CONTRATO-ADMISION.md :: ## 3 · Se juzga la MUTACIÓN, no la existencia · `V6-05`–`V6-09`
implementacion:
  - kernel/operativo/runtime/admision/mutacion.py
  - kernel/operativo/runtime/admision/censo.py
  - kernel/operativo/runtime/admision/formulas.py
canal:
  - kernel/operativo/runtime/pruebas/test_admision.py
positivas: T188 T189 T190
adversariales: N188 N189 N190
resultado: Devolver una salida `-z` truncada como completa, dejar al verificador fuera de su propio alcance o romper el caso frontera del fichero vacío tienen que poner roja la batería de admisión por su punto.
evidencia:
  - kernel/operativo/pruebas/evidencia/admision-salida.txt
estado: SATISFECHO
limites: Los tres sabotajes atacan el canal de lectura, el censo y la sede de fórmulas. El fallo cerrado ante un cambio fuera del universo permitido tiene caso positivo en `T190` y su mutante ataca la frontera, no la enumeración del universo.
```

## `K15`

```ads:invariante
id: K15
formulacion: El gobierno Git del control repo serializa correctamente escritores locales y entre máquinas, sin último-escritor-gana silencioso.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K15` ·
  - kernel/operativo/runtime/CONTRATO-GOBIERNO-GIT-CONTROL.md :: ## 4 · `G-A8`, y son DOS mitades
implementacion:
  - kernel/operativo/runtime/gobierno
canal:
  - kernel/operativo/runtime/pruebas/test_gobierno_git.py
positivas: T187 T221 T222
adversariales: N187
resultado: Que el hook vuelva a tomar el `OID` nulo por «creación» tiene que poner roja la batería de gobierno: el forzado de una referencia protegida volvería a pasar, y el último-escritor-gana dejaría de ser detectable.
evidencia:
  - kernel/operativo/pruebas/evidencia/gobierno-git-salida.txt
  - kernel/operativo/pruebas/evidencia/multimaquina-salida.txt
vinculo:
  - T221 :: `T221` acredita aquí que la serialización la impone el GOBIERNO del control repo y no un acuerdo entre las máquinas: la observación es el mecanismo que la produce.
estado: SATISFECHO
limites: El sabotaje ataca la mitad LOCAL de `G-A8`. La mitad entre máquinas tiene caso positivo (`T221`, `T222`) y no mutante propio.
```

## `K16`

```ads:invariante
id: K16
formulacion: La contención fuerte alcanza al proceso y a sus descendientes, incluidos los que intenten escapar mediante `setsid` u otra nueva sesión.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K16` ·
  - kernel/operativo/runtime/CONTRATO-CONTENCION.md :: ## 1 · El vocabulario, CERRADO. Dos niveles, y no hay tercero
implementacion:
  - kernel/operativo/runtime/contencion/backends.py
  - kernel/operativo/runtime/contencion/politica.py
canal:
  - kernel/operativo/runtime/pruebas/test_contencion.py
positivas: T215 T216 T247 T414
adversariales: NK16a NK16b N216
resultado: Quitarle al backend fuerte su espacio de nombres dejando el nivel declarado, quitarle al montaje el `setsid` que hace la prueba discriminante, o declarar el backend débil con nivel de árbol de procesos, tienen que poner roja la batería de contención por tres motivos distintos.
evidencia:
  - kernel/operativo/pruebas/evidencia/contencion-salida.txt
  - kernel/operativo/pruebas/evidencia/adaptadores-salida.txt
vinculo:
  - N216 :: Aquí `N216` se lee como la degradación del NIVEL: el backend débil se presenta como fuerte y por tanto un descendiente que hace `setsid` deja de estar alcanzado. La observación es el ALCANCE de la contención.
  - T216 :: `T216` acredita aquí el LÍMITE MEDIDO del backend débil: es la mitad negativa que hace significar a `T215`, porque sin ella «el bisnieto no escapa» sería compatible con un montaje que no lo intenta.
estado: SATISFECHO
limites: `NK16a` deja registrado que retirar `--kill-child` NO basta: el PID 1 del espacio está en el grupo y el cinturón lo alcanza. `NK16b` mide el MONTAJE y no el producto, porque el objeto de `T414` es el montaje; se dice, en vez de disfrazarlo. El alcance depende del anfitrión: aquí hay espacio de nombres de PID, `systemd-scope` y contenedor, y NO hay `cgroup-v2` ejercible.
```

## `K17`

```ads:invariante
id: K17
formulacion: La ausencia de aislamiento, firma, identidad, backend o capacidad requerida nunca se convierte en degradación silenciosa.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K17` ·
  - kernel/operativo/runtime/CONTRATO-CONTENCION.md :: ## 5 · Lo que este contrato NO alcanza
implementacion:
  - kernel/operativo/runtime/contencion/politica.py
  - kernel/operativo/runtime/contencion/errores.py
canal:
  - kernel/operativo/runtime/pruebas/test_contencion.py
  - kernel/operativo/runtime/pruebas/test_estado_durable.py
positivas: T172 T216 T248
adversariales: N172 N216
resultado: Que la guarda de intérprete pueda RELAJARSE por variable de entorno, o que el backend débil se declare con nivel fuerte, tienen que poner rojas sus baterías: en los dos casos la ausencia de una capacidad requerida se convertiría en degradación silenciosa.
evidencia:
  - kernel/operativo/pruebas/evidencia/estado-durable-salida.txt
  - kernel/operativo/pruebas/evidencia/contencion-salida.txt
  - kernel/operativo/pruebas/evidencia/adaptadores-salida.txt
vinculo:
  - N216 :: Aquí `N216` se lee como el SILENCIO: lo que se observa no es que el bisnieto escape, sino que la política fuerte se dio por satisfecha sin levantar `ContencionFuerteNoDisponible`. La observación es que la ausencia de capacidad no se declaró.
  - T216 :: `T216` acredita aquí el FALLO CERRADO: pedir contención fuerte donde sólo hay débil no degrada, levanta. Es otra observación sobre la misma batería.
estado: SATISFECHO
limites: Se ejercen la capacidad de contención y la del intérprete. La ausencia de FIRMA y de IDENTIDAD como degradación silenciosa se apoya en `K10` y en `T392`, que aquí no se declara porque su mutante no existe.
```

## `K18`

```ads:invariante
id: K18
formulacion: Enrutamiento, clasificación y selección se basan en datos estructurados y sedes canónicas, no en similitud de prosa.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K18` ·
  - kernel/operativo/runtime/CONTRATO-CICLO-Y-MACROCIRCUITOS.md :: ## 2 · La ruta se compone por MATERIA y ESTADO, nunca por texto libre
implementacion:
  - kernel/operativo/runtime/ciclo
  - kernel/operativo/validadores/composicion_packs.py
canal:
  - kernel/operativo/validadores/comprobar_composicion_procesos.py
  - kernel/operativo/validadores/comprobar_contratos.py
positivas: T227 T240 T276
adversariales: N240 N276
resultado: Nombrar un MÉTODO donde va una CAPACIDAD, o publicar un reparto por vía que no sea el derivado del árbol, tienen que poner rojos sus validadores: la clasificación volvería a decidirse por prosa y no por dato.
evidencia:
  - kernel/operativo/pruebas/evidencia/contratos-salida.txt
  - kernel/operativo/pruebas/evidencia/composicion-procesos-salida.txt
  - kernel/operativo/pruebas/evidencia/agentes-salida.txt
estado: SATISFECHO
limites: El determinismo de la selección de modelo (`T227`) tiene caso positivo y no mutante propio.
```

## `K19`

```ads:invariante
id: K19
formulacion: La política C2/C4 respeta perfil, modelo, cardinalidad, combinaciones, integrador y `execution_slots`.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K19` ·
  - kernel/operativo/runtime/CONTRATO-CICLO-Y-MACROCIRCUITOS.md :: ## 3 bis · `C4` paso 4: quién ocupa cada rol, y qué ocupa un `execution_slot`
implementacion:
  - kernel/operativo/runtime/ciclo
  - kernel/operativo/validadores/negativos_cardinalidad.py
canal:
  - kernel/operativo/validadores/negativos_cardinalidad.py
positivas: T230 T250 T254 T257 T259
adversariales: N250 N250b N250c N250d
resultado: Declarar siete agentes sin integrador, borrar quién integra, estrenar una forma fuera del vocabulario cerrado o esconder del censo una composición plural tienen que poner rojo el validador de cardinalidad, cada uno por su punto.
evidencia:
  - kernel/operativo/pruebas/evidencia/cardinalidad-salida.txt
  - kernel/operativo/pruebas/evidencia/agentes-salida.txt
estado: SATISFECHO
limites: Los cuatro sabotajes ejercen cardinalidad, integrador y vocabulario. `execution_slots` y perfil tienen caso positivo (`T230`, `T257`) y no mutante propio: es la parte de `K19` que se apoya en positivas.
```

## `K20`

```ads:invariante
id: K20
formulacion: La prevención y observación de inanición no modifica la prioridad contractual, ni directamente ni mediante una secuencia de transiciones.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K20` ·
  - kernel/operativo/runtime/CONTRATO-RUNTIME-Y-DISPATCHER.md :: ## 2 · El tiempo lógico es la REVISIÓN, no el reloj
implementacion:
  - kernel/operativo/runtime/runtime/estado_util.py
  - kernel/operativo/runtime/runtime/dispatcher.py
canal:
  - kernel/operativo/runtime/pruebas/test_cardinalidad_y_seleccion.py
positivas: T400 T404 T408 T419
adversariales: NG04 NG04b NK20a NK20b
resultado: Subir la prioridad al postergar, vaciar la lista de campos inmutables, abrir la puerta en la carrera entre dos planificadores o comprobar la invariante DESPUÉS de aplicar tienen que poner roja la batería de cardinalidad, y cada uno por su motivo.
evidencia:
  - kernel/operativo/pruebas/evidencia/cardinalidad-salida.txt
estado: SATISFECHO
limites: `NK20a` cae ya en la primera vuelta, de modo que la mitad que saca la puerta del bucle de reintento no llega a discriminarse por sí sola; queda escrito en su sabotaje. `NK20b` demuestra que el viaje muere EN LA IDA y no al volver.
```

## `K21`

```ads:invariante
id: K21
formulacion: Entregas, acuses, reanudaciones y `Continúa` no pierden ni duplican trabajo confirmado.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K21` ·
  - kernel/operativo/runtime/CONTRATO-CICLO-Y-MACROCIRCUITOS.md :: ## 5 · `C5`: RECHAZO y DEVOLUCIÓN no comparten camino
implementacion:
  - kernel/operativo/runtime/ciclo/handoffs.py
canal:
  - kernel/operativo/runtime/pruebas/test_continua.py
positivas: T203 T204 T205
adversariales: NK21a
resultado: Que el acuse vuelva a derivar la identidad de la entrega del contenido tiene que poner roja la batería de `Continúa`: el acuse escribiría en una ruta lógica nueva, no superaría a la emisión, y `Continúa` reportaría un pendiente falso para siempre.
evidencia:
  - kernel/operativo/pruebas/evidencia/continua-salida.txt
estado: SATISFECHO
limites: El sabotaje ejerce la ENTREGA y su ACUSE. La reanudación y la idempotencia de `Continúa` (`T205`) tienen caso positivo y no mutante propio.
```

## `K22`

```ads:invariante
id: K22
formulacion: La evidencia procede de la ejecución declarada, está vinculada al objeto juzgado y no admite saltos, omisiones o éxitos fabricados.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K22` ·
  - kernel/operativo/pruebas/REGISTRO.md :: # REGISTRO DE CONFORMIDAD — estado real de cada prueba
implementacion:
  - kernel/operativo/validadores/registrar_evidencia.py
  - kernel/operativo/validadores/comprobar_evidencia.py
canal:
  - kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py
  - kernel/operativo/runtime/pruebas/test_runtime.py
  - kernel/operativo/validadores/comprobar_evidencia.py
positivas: T158 T307 T350 T415 T417
adversariales: N158 NH08 N350 NH02 ND02
resultado: Archivar una invocación sin `.py`, dejar de publicar la cobertura del contraste, retirar la sede de la derivación del estado, subir de estado sobre una evidencia que no nombra al escenario, o retirarle a un ejecutor su veredicto nominal, tienen que poner rojos sus canales, cada uno por su motivo.
evidencia:
  - kernel/operativo/pruebas/evidencia/evidencia-salida.txt
  - kernel/operativo/pruebas/evidencia/integridad-evidencia-salida.txt
  - kernel/operativo/pruebas/evidencia/runtime-salida.txt
estado: SATISFECHO
limites: Los cinco sabotajes cubren el archivo, los saltos, la derivación del estado y el ascenso por ejecución ajena. El vínculo de la evidencia al objeto juzgado lo ejerce este mismo instrumento en `C-09` y `C-12`, blob a blob.
```

## `K23`

```ads:invariante
id: K23
formulacion: La huella del kernel y el sello del producto cubren sus ámbitos declarados, se calculan desde el árbol real y no se sustituyen entre sí.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K23` ·
  - kernel/operativo/validadores/validadores.yaml :: componentes:
implementacion:
  - kernel/operativo/validadores/huella.py
  - kernel/operativo/validadores/comprobar_integridad.py
canal:
  - kernel/operativo/validadores/comprobar_integridad.py
positivas: T150
adversariales: N150 NS21a NS23a
resultado: Editar un validador del kernel, alterar una norma vigente dentro de `docs/` o dejar que la huella no mire la RUTA tienen que poner rojo el comprobador de integridad, cada uno por su ámbito: la huella del kernel y el sello del producto cubren ámbitos distintos y no se sustituyen.
evidencia:
  - kernel/operativo/pruebas/evidencia/integridad-salida.txt
estado: SATISFECHO
limites: Los tres sabotajes ejercen el ámbito del kernel, el del producto y la sensibilidad a la ruta. La NO sustitución mutua se observa porque cada sabotaje cae en su ámbito y no en el otro; no hay una prueba que la enuncie por separado.
```

## `K24`

```ads:invariante
id: K24
formulacion: Gates, estados de fase y autoridad impiden declarar éxito, certificación o adopción antes del acto competente.
fuentes:
  - docs/owner/ADS-OWNER-RESOLUCIONES.md :: - `K24` ·
  - docs/canonico/03-GOBIERNO-Y-AUTORIDAD.md :: # 03 · GOBIERNO Y AUTORIDAD
  - kernel/operativo/runtime/CONTRATO-CICLO-Y-MACROCIRCUITOS.md :: ## 4 · Ningún gate es fuente normativa, y se impide por MECANISMO
implementacion:
  - kernel/operativo/runtime/ciclo
  - kernel/operativo/validadores/comprobar_contratos.py
canal:
  - kernel/operativo/validadores/comprobar_contratos.py
  - kernel/operativo/validadores/comprobar_recuentos.py
positivas: T199 T242 T360
adversariales: N242 NG3a
resultado: Devolver la autoridad de los documentos del Owner a la prosa, o dejar que una sede viva niegue una pieza que el árbol tiene construida, tienen que poner rojos sus validadores: en los dos casos se podría declarar un estado que el acto competente no ha dado.
evidencia:
  - kernel/operativo/pruebas/evidencia/ciclo-salida.txt
  - kernel/operativo/pruebas/evidencia/contratos-salida.txt
  - kernel/operativo/pruebas/evidencia/recuentos-salida.txt
estado: SATISFECHO
limites: Los gates se derivan del corpus y fallan cerrado (`T199`), y ninguno es fuente normativa: eso tiene caso positivo y no mutante propio. Lo que sí tiene mutante es la autoridad declarada y la veracidad de las sedes vivas.
```
