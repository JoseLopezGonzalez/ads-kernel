# RATIFICACIÓN DE LA CERTIFICACIÓN INCREMENTAL BAJO `O22` — **VERIFICACIÓN SUSTITUTIVA, LECTURA INTEGRAL COMPLETA**

> **DOCUMENTO INMUTABLE.** Una vez commiteado no se edita: los errores de hecho que contenga
> se acotan en
> [`CORRIGENDUM-DICTAMENES-INMUTABLES.md`](verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md).
>
> **QUÉ ES.** El registro de una **VERIFICACIÓN SUSTITUTIVA**. La certificación anterior, la
> de `KD`, quedó **PROCEDIMENTALMENTE INSUFICIENTE** porque su autor declaró contra sí mismo
> que **no había leído íntegras cuatro de las cinco fuentes modificadas**, y `O22` §3 exige
> lectura íntegra. El Owner ordenó una verificación **completa y sustitutiva** —no
> complementaria—, y esto la registra.
>
> **QUÉ NO ES.** No es un gate. No es una tanda de corrección. **No corrige nada**: ni el
> coordinador ni el verificador han tocado un solo hallazgo, y la candidata `196de03` sigue
> byte a byte como estaba.

## 0 · Qué se ratifica, y sobre qué

```text
OBJETO DE CERTIFICACIÓN   196de0368f89a902f0ade59e1024d3e2fe2ab841
                          review/f4c-o22-delta-hh2-08-candidate-20260901
                          **NO se ha tocado por esta orden**, y sigue siendo el único objeto

GATE COMPLETO             9d4ebe60c58354219b34d2df0ca97299f6980ec1 · documento 32
CANDIDATA ORIGINAL        909a7a1473c732308306805da9144b4ff9fc0977
CIERRE PROVISIONAL        7109e45764d71cb638ebbcae1ea8813cd9a74bf5 · documento 33
                          **NO es la candidata**: registra el juicio de `KD` y nada más

VERIFICADOR SUSTITUTIVO   `LE`, agente independiente ÚNICO, nunca usado, de contexto limpio.
                          **SUSTITUYE a `KD` a todos los efectos de `O22`**; no complementa
                          su lectura parcial, y tiene prohibido sumarla a la suya
                          `O22` §4 le prohíbe corregir nada, y no ha corregido nada:
                          `porcelain` vacío y `HEAD` sin mover, al abrir y al cerrar

LECTURA INTEGRAL          **22 420 de 22 420 líneas**, en la versión de `196de03`, de la
                          primera a la última, en rangos contiguos publicados fichero a
                          fichero, sin `grep`, sin delegación y sin sumar nada de `KD`
```

## 1 · POR QUÉ LA CERTIFICACIÓN DE `KD` FUE INSUFICIENTE, y se registra sin adorno

**`KD` no falló por deshonestidad: falló por procedimiento, y lo dijo él mismo.** Su informe
declara, contra su propio interés:

> *«`O22` §3 escribe «leer ÍNTEGRAMENTE todas las fuentes MODIFICADAS», y bajo una lectura
> maximalista de esa frase, cuatro de las cinco fuentes modificadas no las he abierto de punta
> a punta. Lo declaro; no lo escondo.»*

**`O22` §3 no admite lectura maximalista ni minimalista: dice ÍNTEGRAMENTE.** Por tanto:

```text
`DELTA HH2-08 CERTIFICADO`        de `KD`  ->  procedimentalmente NO DEMOSTRADO
`C-L.5 CERTIFICADA POR DELTA`     de `KD`  ->  NO satisfacía `O22` §5
`SUFICIENTE PARA F5 POR COMPOSICIÓN` de `KD` -> sin efectos, hasta esta ratificación
```

**Y consta a favor del método, porque es lo que lo hizo corregible:** la insuficiencia se
detectó **por la declaración del propio verificador**, no por una auditoría externa. Es la
misma mecánica que hizo medible la condición 5 de `C-L.5` dos gates atrás. **Un verificador
que declara su propia carencia es lo que permite sustituirlo.**

## 2 · LAS CUATRO DECLARACIONES DE `LE`, LITERALES

```text
LECTURA INTEGRAL COMPLETA

DELTA HH2-08 CERTIFICADO

C-L.5 CERTIFICADA POR DELTA

SUFICIENTE PARA F5 POR COMPOSICIÓN
```

**Las cuatro son positivas, y sólo por eso hay suficiencia.** `LE` no podía emitir la última
sin las tres anteriores, y no podía emitir la segunda sin la primera.

## 3 · LA LECTURA INTEGRAL, QUE ES LA RAZÓN DE ESTA RATIFICACIÓN

| # | fichero (en `196de03`) | líneas | SHA-256 | estado |
|---|---|---|---|---|
| 1 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | **665** | `174b6d896b6c14c1e3a370897b23e70683d34050067a3030dc9b234d566a207c` | **`LEÍDO ÍNTEGRO`** |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | **12 136** | `19db9e624bcb84493dd0044c227c15e90755faedb3a97b202714c9159eb26f4a` | **`LEÍDO ÍNTEGRO`** |
| 3 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | **6 157** | `279ad130e9520b1179808844dccae4d8f6a205c017bb8f4c664cbb9397773a71` | **`LEÍDO ÍNTEGRO`** |
| 4 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | **721** | `e20d6ec8a56b6e74808940336d571c3fea41510722c4a91f555da67b41017537` | **`LEÍDO ÍNTEGRO`** |
| 5 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | **1 557** | `d9b3dda318080d53336b77641acb14e4ffebc980f90c72bb42d03bf46a782a36` | **`LEÍDO ÍNTEGRO`** |
| 6 | `docs/evolucion/32-GATE-VERIFICACION-DOCE-HH2-F4C.md` | **881** | `1237245e828546fa3e641376651475196a265507060858bfeb7213f777ed5203` | **`LEÍDO ÍNTEGRO`** |
| 7 | manifiesto `B` del gate de `O21` | **303** | `4a27b5ef2146753afa5ab8c1c6fc95b195d97e493a28af642ebf97c5ef5090f8` | **`LEÍDO ÍNTEGRO`** |

**TOTAL: 22 420 de 22 420.** Cada fichero con su primera y su última sección sustantiva
citadas por título y línea, **dos anclas internas de regiones separadas** que prueban el paso
por el medio y no sólo por los extremos, y la lista de rangos contiguos que lo cubren sin
hueco. **Ningún tramo omitido, y así lo declara fichero a fichero.**

> **El cardinal no se escribe al lado de esta tabla: sale de ella.**
>
> ```bash
> for p in <las siete rutas>; do git show 196de03:$p | wc -l; done | paste -sd+ | bc
> ```

## 4 · LOS DIECINUEVE PUNTOS, VERIFICADOS DE NUEVO SIN ACEPTAR A `KD` POR AUTORIDAD

```text
 1  el gate del documento 32 fue VÁLIDO ....................... SÍ, y lo declara su propio
                                                                adjudicador `JC`, ANTES de
                                                                medir la cobertura
 2  `C-L.5` certificada para el gate completo ................. SÍ, con su tupla de `O21` §5
 3  `HH2-08` fue el ÚNICO bloqueo ............................. SÍ · CERRADO 11 · FALLIDO 1
 4  el adjudicador publicó el contrafactual ................... SÍ, cita literal, en las dos
                                                                direcciones
 5  el defecto EXISTE en `909a7a1` ............................ REPRODUCIDO: §15.4 -> 0
 6  el defecto DESAPARECE en `196de03` ........................ DEMOSTRADO: §15.4 -> 1, con
                                                                diff palabra a palabra
 7  §15.4 contiene MATERIALMENTE «para un gate VÁLIDO» ........ SÍ, en posición gobernante de
                                                                la obligación
 8  el checkpoint describe correctamente la corrección ........ SÍ
 9  el corrigendum acota el manifiesto inmutable .............. SÍ, con las CUATRO
                                                                afirmaciones exigidas
10  el manifiesto es byte a byte idéntico ..................... SÍ, en los CUATRO objetos y
                                                                en la copia de trabajo
11  `O22` es APPEND-ONLY y no rebaja el criterio .............. SÍ: append puro de 106 líneas,
                                                                CERO supresiones. No rebaja
12  los 346 blobs no modificados son idénticos ................ SÍ, comprobado BLOB A BLOB
13  los cinco blobs modificados son los permitidos ............ SÍ, `O22` §2
14  no existe otro cambio sustantivo .......................... NINGUNO, probado en negativo
15  los once `HH2` cerrados siguen cerrados ................... SÍ
16  los seis no bloqueantes siguen registrados ................ SÍ, ninguno SUPERADO
17  `F6` no se presenta como implementada ..................... EN NINGUNA SEDE
18  PesquerApp sigue BLOQUEADA ................................ SÍ, barrido en las DOS
                                                                direcciones, cero
                                                                autorizaciones
19  `F5` NO ha sido iniciada .................................. NO INICIADA. Autorizar no es
                                                                iniciar
```

**La prueba más fuerte de que el delta no se extralimitó la escribe `LE` en negativo:**
verificó **uno por uno** que los seis hallazgos no bloqueantes **siguen materialmente
defectuosos** en la candidata. *«Ninguna deuda se cerró de tapadillo.»*

## 5 · LOS CUATRO HALLAZGOS VIVOS DE ESTA VERIFICACIÓN, ADJUDICADOS POR `LE`

> **`LE` los adjudicó de forma independiente, sin suavizar ninguno por ser menor**, razonando
> su efecto sobre las condiciones exactas de `O22` §2, §3, §5, §6 y §7. **Ninguno alcanza la
> vara de un BLOQUEO**, y por eso `O22` §7 no se activa.

| id | sede · fichero:línea de `196de03` | qué dice, y por qué está mal | adjudicación de `LE` |
|---|---|---|---|
| **`KD-01`** | `CHECKPOINT`:**4811-4812** | Un bloque rotulado «Se comprueba, no se declara» publica `grep -c 'para un gate VÁLIDO'` sobre el `CORRIGENDUM` y lo anota `# -> >=1`. **Ejecutado literalmente devuelve `0`**: la línea usa `grep -c` sensible a caja donde el `CORRIGENDUM` escribe versales. **Una sede publica un autocontrol que no comprueba** | **NO BLOQUEANTE.** No invalida la evidencia de cierre. La afirmación sostenida —que las tres sedes editables coinciden— **es verdadera, y `LE` la derivó por otro medio**; el defecto está en el instrumento, no en el hecho, y **el comando no participa en la cadena probatoria** de `HH2-08`, de `C-L.5` ni de la composición. Misma clase que `JA-01`, que el gate 32 graduó MENOR |
| **`KD-02`** | `CHECKPOINT`:**1074-1076**, campo `metodo:` **VIGENTE** | «LOS **SEIS** HALLAZGOS NO BLOQUEANTES … **sin copiar su recuento**». Copia un recuento que otra sede deriva, dentro del bloque reanudable, **contra la regla 1 y en la misma oración en que dice no copiarlo** | **NO BLOQUEANTE.** Es una **instancia nueva de la clase `C-L.7`, que YA estaba declarada NO CERRADA antes del delta** —`LE` lo derivó del documento 32 y del árbol de `9d4ebe6`—. `O22` §7 habla de otro **bloqueo**, no de otra instancia de deuda ya inscrita. Es **menos grave que `JB-02`**, de su misma clase, porque su cardinal es CORRECTO; y el contrafactual del adjudicador se emitió **con esa deuda en pie** |
| **`LE-01`** | sede canónica **:651 y :653** · proyecciones en `11-ARQ`:**9759** y `DECISIONES`:**1424-1425** | La nota de trazabilidad de `O22` dice «**noventa fuentes**» donde el documento 32 deriva **88 / 89**, y «precondición de **siete palabras**» donde la precondición canónica tiene **cuatro** (`Para un gate válido:`). Dos proyecciones lo reproducen | **NO BLOQUEANTE · LEVE.** Vive en una **nota de trazabilidad**, cuya función declarada es registrar por qué el Owner resolvió, no fijar una cantidad normativa. **Nada depende de esas cifras**: ni una condición de `O22`, ni la reparación de `HH2-08`, ni el traslado de `C-L.5`, ni la composición. Su origen es el **texto del propio Owner en sede APPEND-ONLY**, que `O22` §4 prohíbe corregir; las proyecciones hacen lo que deben: reproducir fielmente |
| **`LE-02`** | `CHECKPOINT`:**1064** y **:1408**, campos VIGENTES | Dos cardinales más que otra sede deriva —«en sus **tres** sedes EDITABLES», «por **UN SOLO** bloqueo»— escritos dentro del bloque reanudable contra la regla 1; en el segundo caso a dos líneas de la declaración de no copiar el recuento | **NO BLOQUEANTE.** Idéntica clase, idéntica adjudicación y idéntico razonamiento que `KD-02`: instancias de `C-L.7`, que ya estaba NO CERRADA. Los cardinales son correctos; el defecto es de forma |

**Y un hallazgo DERIVADO que ningún gate anterior publicó, y que `LE` deja escrito contra su
propia argumentación:** el **barrido mecánico de la regla 7 es incompleto POR CAJA DE LETRA**.
`LOS SEIS HALLAZGOS` escapa; `LOS SEIS hallazgos` es cazado. En sus palabras: *«el verde de
ese barrido sobre la candidata no prueba lo que dice probar. Esto debilita, aunque no anula,
el instrumento sobre el que `C-L.7` descansa, y debilita también el peso que yo mismo he dado
a que el barrido salga vacío. Lo digo expresamente porque juega contra mi propia
argumentación.»* **`C-L.7` sigue NO CERRADA, y esto es una razón más para que lo siga
estando.**

**NINGUNO DE LOS CUATRO SE CORRIGE, y se dice por qué:** corregirlos cambiaría la candidata a
la que la certificación queda ligada por `O21` §5 y `O22` §5, y `O22` §7 no deja otro ciclo.
**Quedan vivos, con sede, prueba y severidad adjudicada.**

## 6 · POR QUÉ, CON TODO ESO EN CONTRA, LA DECLARACIÓN ES POSITIVA — en palabras de `LE`

> *«Porque la vara del §7 es un BLOQUEO, y en el vocabulario que este expediente ha sostenido
> doce gates seguidos un bloqueo es un GRAVE de clase A que funda insuficiencia. Los cuatro
> hallazgos registrados pertenecen, uno a uno, a clases que el adjudicador del gate 32 graduó
> MENOR o LEVE sobre hechos iguales o peores, y sobre las que declaró expresamente: «ninguno
> pasa el límite del §7. Los cuento como vivos; no los cuento como razón.»*
>
> *Aplicar hoy una vara más dura a la misma clase sería alterar el criterio de suficiencia, que
> es exactamente lo que `O22` §8 prohíbe — y lo prohíbe en las dos direcciones, no sólo hacia
> abajo.»*

## 7 · QUÉ CONSTA EN CONTRA, transcrito sin recortar

- *«**`KD-01` es un defecto real:** una sede vigente publica un comando de autocomprobación
  anotado `>= 1` que devuelve `0`. Un lector que ejecute el bloque «Se comprueba, no se
  declara» encontrará que **no comprueba**. Que la afirmación sostenida sea verdadera no repara
  el instrumento.»*
- *«**`KD-02` es un defecto real y agravado:** el campo `metodo:` vigente copia un recuento
  derivable y **declara en la misma oración que no lo copia**.»*
- *«He derivado que **el barrido de la regla 7 es incompleto por caja de letra** … el verde de
  ese barrido no prueba lo que dice probar.»*
- *«**`LE-02`:** la clase `C-L.7` no sólo sigue abierta: **el delta ha añadido población a
  ella**.»*
- *«**`LE-01`:** el delta introduce dos cifras retóricas que el árbol no da, y dos proyecciones
  las copian.»*
- *«El rótulo «las tres sedes editables» designa **tres tríos distintos** en tres sitios, dos de
  ellos a doce líneas uno de otro, e incluye `00-INDICE.md`, que era un blob **idéntico** antes
  y después y que nunca estuvo defectuoso.»*
- *«**La composición se apoya, por construcción, en un gate que yo no he vuelto a ejecutar.** He
  leído su documento íntegro y he verificado que su blob es idéntico en los dos árboles, pero
  **no he reejecutado sus 88 fuentes** … **Quien lea este informe debe saber que la cobertura de
  las 346 fuentes no modificadas se traslada por identidad de blob, no por relectura.** Es lo
  que `O22` §5 autoriza, y lo digo sin adornarlo.»*
- *«**`C-L.7` sigue NO CERRADA** y ningún comando de este expediente puede cerrarla: sólo un
  gate independiente posterior. Mi certificación **no la cierra ni la mejora**.»*

## 8 · QUÉ CONSTA A FAVOR

- *El defecto está reparado **donde el gate dijo, y sólo donde dijo**, verificado por diff
  palabra a palabra y no por conteo de cadenas.*
- *El alcance es **demostrablemente mínimo**: 5 blobs modificados de 351, **346 idénticos
  comprobados blob a blob**, cero altas, cero bajas, cero renombrados.*
- *`O22` es un **append puro** de 106 líneas con **0 supresiones**.*
- *El **manifiesto inmutable no se tocó**, y el remedio se ejecutó por la vía que el corpus tiene
  prevista para lo inmutable.*
- ***Ninguna deuda se cerró de tapadillo**, verificado en negativo uno por uno.*
- ***Ningún estado se suavizó.***
- *Siete de los ocho autocontroles publicados por el delta **reproducen literalmente**.*
- ***Todo lo afirmado está derivado por `LE`**, sin usar ni una conclusión de `KD` por
  autoridad.*

## 9 · QUÉ DECLARA `LE` NO HABER USADO COMO RAZÓN

**Nada de la verificación de `KD`** —ni su lectura, ni sus conclusiones, ni su clasificación—;
**ni el `38/38` ni el `13/13`** de las dos baterías, que ejecutó y publicó declarando que
*«ni un verde ni un rojo de estas dos baterías funda nada de mi veredicto»* y que además
corrieron sobre la copia de trabajo, **que no es la candidata**; **ni el documento 33**, que
registra el juicio de `KD` y cuya lectura como prueba habría sido aceptar por autoridad lo que
tenía prohibido; **ni** que el verificador de `F6` no esté implementado, que PesquerApp no haya
comenzado o que `M-04`, `V6-15`/`F6` y `PN-19`/`F5` sigan siendo deudas; **ni** los seis no
bloqueantes del documento 32; **ni** `KD-01`, `KD-02`, `LE-01` o `LE-02`. **Y no propuso
redacción para ningún hallazgo, ni una vez.**

## 10 · EL ESTADO EN QUE QUEDA EL EXPEDIENTE

```text
LA CERTIFICACIÓN DE `KD`  **PROCEDIMENTALMENTE INSUFICIENTE**, por lectura parcial. Su
                          dictamen se conserva publicado en el documento 33, **intacto y no
                          operativo** — como los manifiestos sustituidos antes que él

`LE`                      **SUSTITUYE a `KD` a todos los efectos de `O22`.** Su verificación
                          es la que sostiene la composición, y es integral

`F4c`                     **CERRADA por composición**, ahora sobre una verificación con
                          LECTURA INTEGRAL COMPLETA

`F5`                      **AUTORIZADA DOCUMENTALMENTE, y NO INICIADA.** Autorizar no es
                          iniciar, y esta orden no la inicia

`F6`                      **NO INICIADA.** Su contrato está escrito —§20 del documento 11— y
                          ninguno de sus puntos implementado, ejecutado ni certificado

PesquerApp                **BLOQUEADA.** Sin MVP, sin piloto desechable y sin adopción
                          parcial, hasta que `F6` implemente **y CERTIFIQUE**

`C-L.5`                   CERTIFICADA para el gate del documento 32 por su adjudicador, y
                          **CERTIFICADA POR DELTA** para `196de03` por `LE`, con la lectura
                          íntegra que `O22` §5 exige. **No se transfiere** a ninguna otra

`C-L.7`                   **NO CERRADA**, y con más razón que antes: `LE` derivó que el
                          barrido de su regla es incompleto por caja de letra

`M-04`                    **NO SUPERADA**
LOS 12 DEL DOCUMENTO 31   **LOS DOCE CERRADOS.** Ninguno SUPERADO
LO QUE QUEDA VIVO         **DIEZ**, todos NO BLOQUEANTES y ninguno SUPERADO: los SEIS del
                          documento 32 —`JA-01`, `JA-02`, `JB-02`, `JB-03`, `JC-01`,
                          `JC-02`— más `KD-01`, `KD-02`, `LE-01` y `LE-02`
EL MÉTODO                 la OPCIÓN C **no se levanta**. No se abre otro ciclo, no se propone
                          otra tanda y no se convoca otro gate
```

## 11 · QUÉ **NO** HACE ESTE DOCUMENTO

```text
NO CORRIGE NADA           ni el verificador —`O22` §4 se lo prohíbe— ni el coordinador. Los
                          diez vivos siguen vivos, y los cuatro de esta verificación también
NO TOCA LA CANDIDATA      `196de03` sigue byte a byte como estaba. El objeto de certificación
                          no se ha movido
NO INICIA `F5`            la autorización es DOCUMENTAL. Nada de `F5` se ha redactado, tocado
                          ni ejecutado
NO INICIA `F6`            ni uno solo de sus contratos está implementado
NO DESBLOQUEA PesquerApp  sigue bloqueada por la cadena `F6` → certificación → adopción
NO DECLARA SUPERADO NADA  ni uno de los diez vivos, ni `M-04`, ni `C-L.7`
NO REVISA NINGUNA         `O17`–`O22` conservan íntegro su texto, y la sede sigue APPEND-ONLY
RESOLUCIÓN DEL OWNER
NO BORRA EL JUICIO DE     el documento 33 se conserva publicado e intacto. Lo que cambia es
`KD`                      su EFECTO, no su texto: queda sustituido, no suprimido
NO ABRE OTRO CICLO        `O22` §7, y la OPCIÓN C sigue sin levantarse
```

**Y una última cosa, que es del verificador y no del coordinador, y por eso se transcribe
literal:** *«Quien lea este informe debe saber que la cobertura de las 346 fuentes no
modificadas se traslada por identidad de blob, no por relectura. Es lo que `O22` §5 autoriza,
y lo digo sin adornarlo.»*
