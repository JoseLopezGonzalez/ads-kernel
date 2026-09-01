# GATE DE VERIFICACIÓN DE LOS DOCE `HH2` — **VÁLIDO**, `C-L.5 CERTIFICADA` e `INSUFICIENTE PARA F5`

> **DOCUMENTO INMUTABLE.** Una vez commiteado no se edita: los errores de hecho que contenga
> se acotan en
> [`CORRIGENDUM-DICTAMENES-INMUTABLES.md`](verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md).
>
> **LO QUE ESTE GATE ESTRENA, y no había ocurrido en once gates:** su adjudicador **CERTIFICA
> LA COBERTURA** midiendo las seis condiciones de `O21` §4 una a una, **mientras devuelve
> INSUFICIENCIA**, y publica la prueba contrafáctica en las dos direcciones de que no ha
> condicionado una declaración a la otra. Es exactamente lo que `O21` vino a hacer posible.
>
> **Y este gate NO corrige nada.** La OPCIÓN C sigue activada; este documento sólo registra.

## 0 · Qué se juzgó, y sobre qué

```text
CANDIDATA          review/f4c-doce-hallazgos-o21-candidate-20260901 = 909a7a1473c73230…
TREE SHA           44585ff8c5ad81d3c2aca0d502613344bb3399dd
BASE DEL RANGO     eafd2ee46852dd69d4704c21b73c4f7a54f36155 — un solo commit sobre ella
RAMA DEL GATE      gate/f4c-verificacion-doce-20260901 = 154a66b89c166a16ce9dd203fb17fb54cd5fe147
MANIFIESTO         verificacion/manifiestos/F4C-ASIGNACION-GATE-VERIFICACION-DOCE-20260901.md
                   SHA-256 4b022c1be1d5e2e73d13cde3d8d9e92effb55488dcf41fb90f71cc731b9ed88c
                   316 líneas · commiteado ANTES de que existiera ningún revisor
SOBRE DE ANCLA     emitido UNA vez, 315 líneas, a un fichero FUERA del repositorio auditado,
                   ANTES de crear a ningún agente. SHA-256
                   6d987dbd3fda10d11c403b6c9283138efc73ab92fb9b6bc6afcb5e2ea63cb532
UNIVERSO           88 fuentes · 93831 líneas sobre la candidata · 89 · 94149 sobre el gate,
                   DERIVADOS por cada uno de los tres agentes y no leídos
AGENTES            revisores `JA` y `JB` en PARALELO y SIN VERSE · adjudicador `JC`, que no
                   vio nada hasta que los dos cerraron. **Sus marcas se DERIVARON del
                   expediente** —53 consumidas, barridas de los documentos de gate y de
                   todos los manifiestos— y no se eligieron de memoria
QUÉ TRAÍA          los DOCE hallazgos `HH2-01`…`HH2-12` del documento 31, aplicados con el
                   remedio que ese gate adjudicó, en CINCO ficheros
```

## 1 · EL VEREDICTO, LITERAL

```text
EL GATE ES VÁLIDO                     Las siete obligaciones del sobre reproducen para los
                                      tres, hay UN SOLO sobre físico y los tres publican
                                      valores idénticos en sus trece magnitudes ancladas

C-L.5 CERTIFICADA PARA ESTE GATE      las SEIS condiciones de `O21` §4, SATISFECHAS y
                                      medidas una a una. Ligada a la tupla de seis
                                      elementos de `O21` §5, y NO transferible

INSUFICIENTE PARA F5                  `F4c` sigue ABIERTA · `F5` sigue NO AUTORIZADA

NADA VUELVE AL OWNER                  clase A 7 · B 0 · C 0, por octava vez consecutiva
```

**LAS DOS DECLARACIONES SE EMITIERON POR SEPARADO**, y el adjudicador publica la prueba
contrafáctica **en las dos direcciones**: si el hallazgo vivo estuviera cerrado, la cobertura
seguiría certificada y el veredicto sería suficiente; si un revisor hubiera dejado un tramo
sin abrir, la cobertura se abriría y el veredicto seguiría siendo insuficiente. **Cada
declaración es invariante ante la otra.**

## 2 · Los DOCE, y su cierre individual

```text
CERRADO        11   HH2-01 · HH2-02 · HH2-03 · HH2-04 · HH2-05 · HH2-06 ·
                    HH2-07 · HH2-09 · HH2-10 · HH2-11 · HH2-12
FALLIDO         1   HH2-08 — severidad SUBIDA de MENOR a GRAVE por el adjudicador
NO APLICABLE    0
```

**LOS DOS QUE DECIDIERON EL VEREDICTO ANTERIOR ESTÁN CERRADOS**, y los tres agentes los
verificaron **por ejecución y no por lectura**: `HH2-01`, el BLOQUEANTE, y `HH2-02`, el GRAVE.
El adjudicador construyó además su propio control negativo —revertir el comando y comprobar
que la batería sigue en verde— y su propio control positivo —plantar un árbol nuevo y ver que
el conjunto crece de cuatro a cinco sin editar un solo campo—.

**`HH2-10` se declara CERRADO contra la conclusión de uno de los revisores**, y el adjudicador
razona por qué en cuatro puntos reproducidos. **No se resolvió por mayoría en ningún punto.**

## 3 · Lo que queda vivo, y el recuento se DERIVA

> Una fila por identificador. **La cifra no se escribe al lado de la tabla**: sale de ella.
>
> ```bash
> awk '/^## 5 · MATRIZ CONSOLIDADA DE LO QUE QUEDA VIVO/{t=1} t&&/^\*\*RECUENTO/{exit} \
>      t&&/^\| \*\*`/' docs/evolucion/32-GATE-VERIFICACION-DOCE-HH2-F4C.md \
>   | sed -E 's/^\| \*\*`([A-Z0-9-]+)`\*\*.*/\1/' | sort -u | wc -l
> ```
>
> Se ancla en **la matriz consolidada del adjudicador**, y toma **el identificador de cabecera
> de cada fila** —no todos los que la fila mencione—, porque el adjudicador declara
> expresamente que `JB-01` y `HH2-08` **son el mismo objeto** y que no lo cuenta dos veces.
> Barrer identificadores sueltos daría OCHO; las filas son SIETE.
>
> **NINGUNO SE DECLARA SUPERADO, y ninguno se corrige en este documento.** Un gate no corrige.

## 4 · DICTAMEN ÍNTEGRO DEL REVISOR `JA` — remedios, trazabilidad, Git y comprobaciones dirigidas


**Contexto limpio.** No he escrito nada de este corpus, no he aplicado ninguna corrección y no he participado en ningún gate anterior. **No he modificado el repositorio auditado**: `git status --porcelain` → 0 al abrir y al cerrar; `git rev-parse HEAD` → `154a66b89c166a16ce9dd203fb17fb54cd5fe147`; el `reflog` no registra ninguna operación mía; cero ramas, cero commits, cero referencias. Todo lo adversarial se hizo en un clon desechable bajo `scratchpad/JA-clon/`, **ya eliminado**. Intérprete: Python 3.12.14.

# 1 · CUMPLIMIENTO DEL SOBRE — las siete obligaciones

**OBLIGACIÓN 1 · recalcular los DOS digest antes de leer nada. CUMPLIDA, y fue lo primero.**

| árbol | fuentes | líneas | digest recalculado por mí | ¿= sobre? |
|---|---|---|---|---|
| CANDIDATA `909a7a1` | **88** | **93831** | `d59af7003cf3d93a4ddc5f3a1ead90d60be15480e02b1ff18e40606824583ab6` | **SÍ** |
| GATE `154a66b8` | **89** | **94149** | `c8983f7cff882ff9c3f2e395baa3d22ec5ab0cad9e34c82ac70d993937c0ed86` | **SÍ** |

Las seis cifras las **derivé**, no las leí. **El gate NO es inválido por esta vía.** Los dos `tree` SHA reproducen: `44585ff8c5ad81d3c2aca0d502613344bb3399dd` y `fb2c4c10429989721fe48c2758e122948360349d`.

**OBLIGACIÓN 2 · el manifiesto, EN EL COMMIT DEL GATE. CUMPLIDA.** `git show 154a66b8:…B.md | sha256sum` → `4b022c1be1d5e2e73d13cde3d8d9e92effb55488dcf41fb90f71cc731b9ed88c`, idéntico al sobre. **316 líneas, leídas íntegras del commit.** Sobre la candidata el mismo `git show` responde `fatal: Not a valid object name`, que es lo que el sobre declara.

**OBLIGACIÓN 3 · cada fila contra SU árbol, y la del derivador PRIMERO. CUMPLIDA**, sobre **las 88 filas** (8 de §4 + 80 de §5), contrastando SHA-256 **y** recuento de líneas.

- **LA FILA DEL DERIVADOR, mirada primero** —§5 fila 23, 857 líneas, `fc8adef3a8baf223fd8bc9ae9403b2e5430c6c5f4cc09e83803d301b920fd0be`—: **EXACTA en los DOS commits. NO reincide `U-02`/`X-06`, por séptima vez.**
- **CERO discrepancias contra el árbol de la CANDIDATA.** Suma de la columna «líneas» de las 88 filas = **93831**, exactamente el universo derivado.
- Contra el árbol del GATE discrepa **una sola** fila: `00-INDICE.md` (255/`6339aa806335` frente a 257/`4045a607c409`), y **es la que el sobre publica y la que §6 del manifiesto declara con su razón**.

**OBLIGACIÓN 4 · las dos superficies de diferencia NO son la misma. CUMPLIDA, y el sobre dice la verdad.**

    UNIVERSOS que difieren     2   00-INDICE.md · el manifiesto de este gate
    ÁRBOLES que difieren       5   las dos de arriba + los tres ficheros de evidencia

Las tres extra son evidencia reejecutada, fuera del universo obligatorio. **El sobre no las nombra y advierte expresamente de que no las nombra.** Sin hallazgo.

**OBLIGACIÓN 5 · qué prueba y qué no el `porcelain` vacío. CUMPLIDA.** Emisor `f915a840…30d20a` y derivador `fc8adef3…0fd0be` idénticos en los dos commits. Comprobé además que **no hay ni una entrada con `skip-worktree` ni `assume-unchanged`** (`git ls-files -v | grep -v '^H '` → vacío), que es la puerta que `Z-11` nombra. **Asumo la limitación que el sobre declara.**

**OBLIGACIÓN 6 · la sede canónica y toda paráfrasis. CUMPLIDA.**

| | recalculado | líneas | ¿= sobre, en los dos commits? |
|---|---|---|---|
| sede entera | `ebfef288de70d1ec6d58306720440b9a4c706197cc66f99b92e54a147678fc9a` | 559 | **SÍ** |
| `O17` | `0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125` | 85 | **SÍ** |
| `O18` | `ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353` | 111 | **SÍ** |
| `O19` | `d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632` | 81 | **SÍ** |
| `O20` | `ebc5b2cd159336c5be5b7557d624082fbe15a7b7cff7ee912dbebf4e354612af` | 110 | **SÍ** |
| `O21` | `e9dd2fb9e780e505ede8334a1795a102d85a1187de946bf6d2aa0799e7b20810` | 112 | **SÍ** |

**Los dos commits publican la misma sede byte a byte.** El contraste de paráfrasis **produce DOS hallazgos**, los dos dentro de los doce: `11-ARQ`:**9288** reproduce la obligación de `O21` §3 **sin su precondición** —sede L485: «Para un gate **válido**:»—, y `11-ARQ`:**9720**, dentro del bloque `### D109` que proyecta `O20`, escribe «los **nueve** gates» donde el texto canónico de `O20` (sede L443) escribe «los **ocho** gates».

**OBLIGACIÓN 7 · el TEXTO ÍNTEGRO de `O19` viaja en el sobre. CUMPLIDA.** Recorté el bloque —sobre L155-235, delimitadores en L154 y L236—, quité la sangría y `sha256sum`: **81 líneas · `d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632`**. Es el digest publicado a su lado. Lo comparé además **byte a byte** con el bloque extraído del commit auditado: `diff` **sin salida, IDÉNTICOS**. Son las 81 de 81 líneas: **no es un resumen**. Comprobé la receta **sin ejecutar el emisor**.

**Ninguna de las siete falla. El gate NO es inválido por el sobre, y sigo.**

# 2 · MANIFIESTO DE LECTURA

| # | ruta · alcance asignado | líneas | SHA-256 **recalculado por mí** | ¿ÍNTEGRA? | primera sección sustantiva | última sección sustantiva | dos anclas de regiones separadas |
|---|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **`L1-L5200`** | 12103 | `e65c9c02572ce63d47f68673b3c9d083e85dc56f8c5ccd40e53afb4cf02a69ec` | **SÍ, en mi alcance** | L95 `# 0 · Resumen ejecutivo` | L5126 `## 4.3 · Las doce áreas de O8` | L426 «LA FAMILIA `X`… `V6-<nn>` Sede: §20.1» · L4415 «La frontera real, y es UN solo criterio» |
| 2 | `docs/evolucion/30-GATE-ARQUITECTONICO-FINAL-F4C.md` | 3084 | `712058b2467287d7ca51380cf305e84ac311f141d1c12ec0649c8b901aee6503` | **SÍ, ÍNTEGRA** | L13 `## 0 · Qué es este documento` | L3050 `## DISCIPLINA — cierre del adjudicador` | L2962 fila `H-06` de §9 · L2854 «la MATRIZ ADVERSARIAL no especifica una clase reproducida» |
| 3 | `docs/evolucion/31-GATE-FINAL-O21-F4C.md` | 783 | `d184e9528ce38356235d726385eb4cb795d3a75daaaf0e19450fb33c57616eba` | **SÍ, ÍNTEGRA** | L11 `## 0 · Qué se juzgó, y sobre qué` | L761 `## 7 · Estado exacto…` | L518 fila `HH2-01` de §4 · L575-596 §6, el `git blame` de quién introdujo cada uno |
| 4 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` **`L1-L2900`** | 5923 | `1ddaba90c0140c07f3d04712d4269fd390ff9feb7402d2d2bc054fac12799f98` | **SÍ, en mi alcance** | L14 «Estado de la fase, en una línea» | L2806 `falta_para_cerrar_la_capa:` | L1010-1054 reglas 7 y 8 · L2526 fila `C-L.5` de la CLASIFICACIÓN VIGENTE |
| 5 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 683 | `c0cc2ee5bb5397888f3cbf4c91c088600d2e7d1bd5db0b88001cbeb58d86760c` | **SÍ, ÍNTEGRA** | L16 `## 1 · Documento 20…` | L651 `## 20 · Regla general…` | L620-649 §19, la entrada de `HH2-08` · L460 §14, `DD-18` |
| 6 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 559 | `ebfef288de70d1ec6d58306720440b9a4c706197cc66f99b92e54a147678fc9a` | **SÍ, ÍNTEGRA** | L14 `## Reglas de esta sede` | L545 `## Nota de trazabilidad de O21` | L485 `O21` §3 «Para un gate **válido**:» · L443 nota de `O20`, «los **ocho** gates» |

Más el **manifiesto** (316, `4b022c1b…`) leído íntegro del commit del gate, y el **sobre** (315, `6d987dbd3fda10d11c403b6c9283138efc73ab92fb9b6bc6afcb5e2ea63cb532`) leído entero antes que nada.

### `ASIGNADO − LEÍDO` = ∅ EN MI LOTE

**Documento 11 `L1-L5200`:** 1-330 · 330-730 · 730-1150 · 1150-1600 · 1599-2059 · 2058-2518 · 2518-2978 · 2978-3438 · 3438-3898 · 3898-4358 · 4358-4808 · 4808-5208. **CHECKPOINT `L1-L2900`:** 1-420 · 421-840 · 841-1260 · 1261-1680 · 1681-2100 · 2101-2520 · 2521-2910. Documentos 30, 31, corrigendum y sede: `L1` a su última línea.

### DECLARACIÓN CONTRA MI PROPIO INTERÉS

- **`11-ARQUITECTURA-INTEGRADA.md` `L5201-L12103` NO es mío y NO he leído ni una línea de él como lectura.** Es de `JB`.
- **`CHECKPOINT-ADS-NEXT.md` `L2901-L5923` NO es mío y NO lo he leído como lectura.** Es de `JB`.
- **LECTURAS FUERA DE MI LOTE, declaradas, y NINGUNA la cuento como íntegra:** `CHECKPOINT` L4156-4162, L4230-4246, L4540-4646 · `11-ARQ` L9261-9298, L9696-9760, L11005-11036, L11940-11960, L12041-12103 · `00-INDICE.md` L31-35, L104-110, L145-200 · `DECISIONES` L491, L545-600, L592, L1373 · `26-QUINTO-GATE` L55-90 y L3981 · `comprobar-…py` por `grep`, sin leerlo. **Ningún hallazgo mío se funda ÚNICAMENTE en material fuera de mi lote:** los dos que citan tramos ajenos —`HH2-08` y `HH2-10`— tienen su sede probatoria en la **sede canónica** y en el **CORRIGENDUM**, que sí son míos y sí están leídos íntegros, y los reproduje con comandos derivados.
- **`grep`, `awk`, `wc` y barridos mecánicos NO los cuento como lectura.**
- **Lo que no puedo comprobar:** que el emisor y el derivador que **corrieron** sean los publicados; y que la sede canónica sea el texto que el Owner **emitió**. Limitación TRANSITORIA que `O18` declara.

**`ASIGNADO − LEÍDO` = ∅** para mi lote.

# 3 · EL DIFF · `eafd2ee` → `909a7a1`

`git rev-list --count eafd2ee..909a7a1` → **1**, y su padre es exactamente `eafd2ee`.

    M  docs/evolucion/00-INDICE.md                                       9+   2-
    M  docs/evolucion/11-ARQUITECTURA-INTEGRADA.md                      72+  40-
    M  docs/evolucion/CHECKPOINT-ADS-NEXT.md                           129+  23-
    M  docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md  32+   1-
    M  docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md                     46+   0-
                                             5 ficheros · 288 inserciones · 66 supresiones

- **EXACTAMENTE CINCO FICHEROS, y son los cinco declarados.**
- **CERO altas, CERO bajas, CERO renombrados, CERO copias**, con detección forzada. Los cinco son `M`, modo `100644` → `100644`.
- **NADA FUERA DE ALCANCE.** Ni un documento de gate, ni un manifiesto, ni la sede del Owner, ni `kernel/`, ni `packs/`, ni evidencia derivada, ni un solo `.py`.
- **La sede canónica del Owner es byte a byte idéntica en `eafd2ee`, `909a7a1` y `154a66b8`.**

**EL SEXTO FICHERO, `verificacion/README.md` — verificado, y la declaración de la tanda es EXACTA.** Su SHA-256 es `f216def357a4075e3175bd9a7cb2bedf169fc6114b82bacb4d23d91ae5ba4dbe` **en los tres commits**. **La cifra publicable es CINCO**, y el manifiesto del gate dice CINCO (§1) y acierta.

# 4 · LOS DOCE, UNO POR UNO

> Cobertura previa: `comm -23 <(los doce del §4 del doc 31) <(la tabla de la tanda)` → **VACÍO**; la tabla tiene **12** identificadores únicos. Ninguno se declara SUPERADO en ninguna sede.

### `HH2-01` · **BLOQUEANTE** · **CERRADO**

**(a) §20.5 deriva ÁRBOLES y no identificadores de hallazgo.** Ejecuté el comando literal de `11-ARQ`:**12074**:

    26-QUINTO-GATE…:59:   ## 2 · EL OCTAVO ÁRBOL, QUE LO ENCONTRÓ EL ADJUDICADOR…
    27-SEXTO-GATE…:49:    ## 2 · EL NOVENO ÁRBOL, Y LO ENCONTRÓ UN REVISOR…
    28-SEPTIMO-GATE…:63:  ## 3 · EL DÉCIMO ÁRBOL, Y ESTA VEZ SON DOS EJES DISTINTOS
    29-OCTAVO-GATE…:41:   ## 2 · EL UNDÉCIMO ÁRBOL, Y ESTA VEZ LO CONSTRUYÓ EL ADJUDICADOR

**Cuatro ÁRBOLES, cero identificadores de hallazgo.** El comando anterior devolvía **75**; lo reproduje en el clon y el contraste es total.

**(b) Cabecera e identificador estable.** La cabecera es el identificador y el documento inmutable la sede. **Ninguno lo escribe §20.5.**

**(c) Entrada, conjunto, escenario negativo y cierre remiten al MISMO conjunto.** `11-ARQ`:**11947**: ENTRADA «el conjunto **derivado** de los ÁRBOLES ADVERSARIALES que un gate publicó **con cabecera propia**… son ÁRBOLES, no identificadores de hallazgo»; NEGATIVO «**cada uno** de los ÁRBOLES del conjunto derivado, **REPRODUCIDO**, vuelve a dar ROJO»; CIERRE «las dos restas **sobre el mismo conjunto de ÁRBOLES**».

**(d) `DD-01` pertenece al conjunto.** El comando devuelve `26-QUINTO-GATE…:59`, y `26-…:3981` es la fila de `DD-01` que dice «EL OCTAVO ÁRBOL». La fila de `V6-15` lo nombra: «—el OCTAVO, `DD-01`, documento 26, **INCLUIDO**—».

**(e) Conserva `SIS` y `F4c`.** §20.5: «QUIÉN ESPECIFICA **`SIS`**, y su fase es **`F4c`**». La fila: «**Especifica `SIS` en `F4c`; construye `F6`**». Contrastado contra **`30-…`:2962**, que leí íntegro: «`SIS` especifica · **`F4c`** · al Owner **NO**». **Coincide exactamente.**

**(f) NO existe deuda viva que lo desplace.** El bloque `DEUDA DE INVENTARIO · VER · F6` está **retirado**. Las únicas apariciones vivas están en el documento 31 (inmutable, narra el defecto) y en `CHECKPOINT`:4568, bajo el epígrafe de la tanda ANTERIOR, cuya sucesora declara que la deuda se retira.

**(g) NO aparece cardinal manual.** La única cifra de §20.5 —«setenta y cinco identificadores»— describe **lo que devolvía el comando RETIRADO**.

**(h) Reproducible.** Reproducido dos veces, salida idéntica.

**VEREDICTO: `HH2-01` CERRADO.**

### `HH2-02` · **GRAVE** · **CERRADO**

**El defecto, REPRODUCIDO en la BASE.** El comando anterior sobre `eafd2ee` → **0 líneas**. Sobre la candidata también 0, lo que confirma que el defecto era del comando y no del texto.

**El remedio, VERIFICADO.** El comando nuevo (`CHECKPOINT`:1015-1017) → **14 campos**: `actualizado · based_on · falta_para_cerrar_la_capa · freshness · last_meaningful_event · last_meaningful_event_anterior · metodo · metodo_anterior · owner_captado · pregunta_pendiente · procedencia_de_la_critica · rama_de_trabajo · regla_de_reanclaje · siguiente`.

- **ENTRA DENTRO DE LA VALLA:** abre en L972, el ancla `^actualizado:` está en **L974** —dentro—, y el `exit` dispara en **L2929**, el cierre de esa misma valla.
- **NO devuelve vacío por construcción**, y el texto añade la guarda «**Antes de usarlo, compruébese que devuelve campos**».
- **DERIVA LOS CATORCE REALES**, los mismos que `W2` derivó a mano en el gate anterior.

**VEREDICTO: `HH2-02` CERRADO.** Las tres pruebas adversariales van en §5 y sus dos residuos —que NO son el remedio adjudicado— en §6.

### `HH2-03` · **GRAVE** · **CERRADO**
`11-ARQ`:**11012-11036**. `SE CONFIRMA EL RESTO` incorpora «**9 verificador de `F6` y raíz externa**» entre el 7 y el 8, y la glosa dice «la BASE COMPLETA ACORDADA **de los pasos 0 a 7 Y DEL NODO 9**». Añade «**ESTA ES LA ÚNICA CONDICIÓN DE ENTRADA DEL PASO 8 QUE ESTA SECCIÓN ENUNCIA**» y regla de desempate. Las **dos únicas** apariciones de «pasos 0 a 7» son la glosa corregida y la nota que narra el defecto. El grafo no se ha tocado.

### `HH2-04` · MEDIO · **CERRADO**
`CHECKPOINT`:**2864**, verificado con `cat -A`: el comando termina en fin de línea y **es ejecutable**. La prosa vive en su propio párrafo (L2869-2871).

### `HH2-05` · MEDIO · **CERRADO** (su instancia; residuo de clase en §6)
`CHECKPOINT`:**2843-2845**: rótulo histórico añadido y **recuento suelto** —«CUATRO BLOQUEANTES» ya no existe en el fichero—. Y el **ALCANCE queda NORMADO**: regla 8 en **1044-1054**, con sus dos anclas y «una viñeta sin rótulo se lee como VIGENTE».

### `HH2-06` · MEDIO · **CERRADO**
`00-INDICE.md`:**35**. Deja de enumerar y deriva. Ejecutado, devuelve las cinco.

### `HH2-07` · MENOR · **CERRADO**
Las dos apariciones de «dieciocho» de la base (L4242, L4246) **han desaparecido** y se remiten al comando, que devuelve **19**. **Se retira y se remite; no se sustituye.**

### `HH2-08` · MENOR · **FALLIDO**

El remedio (`31-…`:525) nombra **TRES** sedes:

| sede | ¿corregida en `909a7a1`? |
|---|---|
| `00-INDICE.md`:**107** | **SÍ** |
| manifiesto `B` §8 | **NO se toca, y es correcto**: inmutable, y su diferencia va al CORRIGENDUM |
| **`11-ARQ`:9288 (§15.4, fila `O21`)** | **NO. INTACTA.** |

    awk '/^## 15\.4 /{f=1;next} /^## 15\.5 /{f=0} f' 11-ARQ | grep -ci 'gate v.lido'   → 0
    awk '/^## 15\.4 /{f=1;next} /^## 15\.5 /{f=0} f' 11-ARQ | grep -c 'DEBE certificar' → 1
    grep -n 'gate VÁLIDO\|gate válido' 11-ARQ                                          → 9739 (UNA sola)

La fila sigue diciendo, **en los tres árboles y en la línea 9288 en los tres**: «…cumplidas sus seis condiciones el adjudicador DEBE certificar…». `git diff eafd2ee 909a7a1 -- 11-ARQ` produce **cuatro hunks** y **ninguno toca 9200-9299**.

**Lo que la tanda corrigió es una CUARTA sede que el gate no nombró:** `11-ARQ`:**9739**, en el bloque `### D110` de **§15.8**.

**Y el remedio introduce otro defecto, en la sede que existe para no contenerlo.** `CORRIGENDUM`:**646-649**: «Las otras dos sedes… —**§15.4 del documento 11** y la fila del índice— **sí son editables y están corregidas**». **Es falso, y es la única afirmación de esa entrada sin el comando que la derive**, contra la cabecera del propio documento. La misma afirmación falsa está en `CHECKPOINT`:**4636** y en el mensaje del commit.

Confirmación independiente: la marca `HH2-08` aparece en `CORRIGENDUM` y en `CHECKPOINT`, y **no aparece ni en `11-ARQUITECTURA-INTEGRADA.md` ni en `00-INDICE.md`**.

**VEREDICTO: `HH2-08` FALLIDO.** Es a la vez *remedio parcial*, *paráfrasis que amplía el texto canónico* y *remedio que introduce otro defecto*.

### `HH2-09` · MENOR · **CERRADO**
`### D107` (491) · `### D108` (**545**) · `### D109` (**568**) · `### D110` (**581**), los tres nuevos con origen, resolución y fecha. **Y se escribe la regla que `S-19` no estableció** (L553). **Cierra la clase.**

### `HH2-10` · MENOR · **FALLIDO** (parcial)

| sede | estado |
|---|---|
| `CHECKPOINT`:974-975 | **Ya estaba retirada en la BASE**: la retiró el commit del gate anterior |
| `CHECKPOINT`:1285 | **CORREGIDA.** Se retira y se remite, no se sustituye |
| **`11-ARQ`:9720** | **INTACTA en los tres árboles.** «ninguno de **los nueve** gates le elevó esta pregunta» |

Agravante verificado contra la sede: **L9720 vive dentro del bloque `### D109`, que es la PROYECCIÓN de `O20`**, y el texto canónico de `O20` —sede L443— dice «**los ocho** gates». «Los nueve» es el cardinal de `O21`. **La proyección copia el cardinal de la resolución equivocada.**

La fila `HH2-10` del checkpoint (L4646) declara como sede «doc 11 §15.8», y el único cambio ahí es el de `HH2-08` en L9739. **Ningún cambio corresponde a `HH2-10` en el documento 11.**

**VEREDICTO: `HH2-10` FALLIDO en su mitad de propagación.**

### `HH2-11` · LEVE · **CERRADO**
`CHECKPOINT`:**2306-2310**. Comprobado contra los cinco `ALCANCE`: `O17` L71, `O18` L156, `O20` L352 dicen las tres; **`O19` L267 dice sólo `F5`**; `O21` L464-465 dice las tres. **La nueva formulación es verdadera para las cinco.**

### `HH2-12` · MENOR · **CERRADO**
El comando del índice sobre los **dos** árboles → **diff SIN SALIDA en los dos**. Los dos manifiestos anteriores entran en la LISTA, y **el aparato de ESTE gate no reincide**. Primera vez en la serie que la regla se cumple en los dos árboles a la vez.

## RECUENTO, DERIVADO

    CERRADO         10   HH2-01 · HH2-02 · HH2-03 · HH2-04 · HH2-05 · HH2-06 ·
                         HH2-07 · HH2-09 · HH2-11 · HH2-12
    FALLIDO          2   HH2-08 (MENOR) · HH2-10 (MENOR, mitad de propagación)
    NO APLICABLE     0

**LOS DOS QUE DECIDIERON EL VEREDICTO ANTERIOR ESTÁN CERRADOS**, verificados por ejecución. **Ningún hallazgo suavizado cambiándolo de fase**: `HH2-01` va en la dirección contraria. **Ninguna formulación histórica reescrita.** **Ningún cardinal manual nuevo**: barrí las 288 líneas añadidas.

# 5 · LOS DOS CONTROLES

## 5.1 · CONTROL NEGATIVO OBLIGATORIO de `HH2-01`

Clon desechable, `checkout 909a7a1`, rama `ja-adv`. Baseline **38/38 · EXIT=0**. Sustituí en `11-ARQ`:12074 el comando vigente por **el anterior**, dejando intacto el rótulo.

    conjunto derivado tras la mutación   75 identificadores  (C-00 C-01 C-02 C-03 …)
    BATERÍA                              38/38 comprobaciones en verde · EXIT=0

**LA BATERÍA NO LO DETECTA.** Ninguna de las 38 menciona `§20`, `V6-`, `ÁRBOL` ni `CONTRATO_CONSTRUIBLE`. **Lo que SÍ lo detecta es la comprobación de PROPIEDAD que este encargo exige**: correr el comando y mirar el TIPO de objeto. **El control negativo funciona por derivación humana y no por instrumento.**

**CONTROL POSITIVO añadido.** Planté un `32-GATE-FICTICIO.md` con la cabecera `## 2 · EL DUODÉCIMO ÁRBOL…`. El comando lo devuelve **sin editar un solo campo**: el conjunto pasa de 4 a 5. **Es lo que §20.5 promete.**

**Restaurado y clon eliminado**, `porcelain` = 0 y HEAD = `154a66b8`.

**Lo que este control mide:** que **el remedio de `HH2-01` es correcto y su propiedad comprobable**, y que **nada mecánico lo guarda** — lo segundo es la mitad de implementación de `M-04`, que `O20` manda a `F6`; **no lo uso como razón de insuficiencia.**

## 5.2 · LAS TRES PRUEBAS de `HH2-02`

**PRUEBA A · una copia introducida ES DETECTADA.** Inyecté en `regla_de_reanclaje` «*y quedan vivos **los 12 hallazgos** del gate anterior*» → **DETECTADA, 1 salida.**

**PRUEBA B · el árbol vigente produce CERO.** Barrido sobre la candidata → **0**. Sobre la BASE `eafd2ee` → **6**, entre ellas las dos que `HH2-10` nombraba. **El barrido discrimina.** Y lo comprobé con un **segundo implementador** —semántica literal de la regla 8—: también **0**.

**PRUEBA C · mover el texto o cambiar las anclas.**

| variante | campos | qué significa |
|---|---|---|
| **MOVER**: 100 líneas antes del bloque | **14** · barrido 0 | ancla de CONTENIDO, no de línea. **No se rompe** |
| **CAMBIAR EL ANCLA**: `actualizado:` → `actualizado_x:` | **0** | falla **ruidosamente**, y la guarda obliga a mirarlo. **Detectable** |
| **VALLA ANIDADA sin sangría dentro del bloque** | **5** de 14 · barrido 0 | **TRUNCA EN SILENCIO** y la guarda pasa, porque 5 > 0 |

**Contra el interés de mi propio veredicto:** el control **no es tautológico** ante movimiento ni ante cambio de ancla, pero admite **truncación silenciosa** ante una valla sin sangría. Hoy no ocurre: de L972 a L2929 no hay ni una línea que empiece por ` ``` `. Es residuo del instrumento, no del remedio adjudicado.

# 6 · HALLAZGOS NUEVOS

Aplico el límite del §7. Traigo **dos**, los dos consecuencia directa de un remedio de esta tanda. **No abro auditoría ilimitada.**

### `JA-01` · MENOR · el barrido mecánico de la regla 7 **enmudece** tras el primer rótulo histórico de viñeta, contra la regla 8 que el MISMO commit escribe
**Sede:** `CHECKPOINT`:**1033-1038** contra **1044-1054**. **Contrato incumplido:** la propia regla 8. **Reproducido:** la bandera `h` se activa con el rótulo y **sólo se reinicia al cambiar de campo**. Inyecté «los 12 hallazgos» en `falta_para_cerrar_la_capa` **después** de la viñeta rotulada → **0 salidas: NO la detecta**. **Alcance:** quedan mudas ~1 030 de ~1 955 líneas. **¿Lo introdujo `909a7a1`?** **SÍ**, las dos mitades nacen en este commit. **Lo que NO afirmo:** no oculta ninguna violación viva — reimplementado con la semántica correcta, la candidata devuelve **0** igual. Es **falsa promesa latente**, no falso verde actual.

### `JA-02` · LEVE · el extractor **trunca en silencio** ante una valla sin sangría
**Sede:** `CHECKPOINT`:**1015-1017**. **Contrato incumplido:** la guarda «compruébese que devuelve campos» **no distingue 14 de 5**. **Reproducido:** inserté ` ```text ` sin sangría; pasa de **14 a 5** y la guarda **pasa igual**. **¿Lo introdujo `909a7a1`?** **SÍ.** **Estado hoy:** inocuo.

**MI PONDERACIÓN, contra mi propio interés.** Ninguno falsea una sede, ninguno oculta una violación viva, y **ninguno es el remedio adjudicado de `HH2-02`**, que está cumplido. El barrido y la regla 8 son **añadidos voluntarios**, y el propio texto declara que «**NINGUNO DE LOS DOS COMANDOS CIERRA `C-L.7`**». Por el precedente de `WA` al hacer caer `W1-04`, `W1-05` y `W1-09`, **NO fundo mi recomendación en ninguno de los dos** y **no los cuento**.

**Y declaro lo que NO he encontrado:** ninguna sede presenta deuda de `F6` como implementación existente; PesquerApp sigue bloqueada y ninguna línea añadida la autoriza; la sede canónica es byte a byte idéntica; ningún documento de gate, dictamen ni manifiesto tocado; ningún hallazgo declarado SUPERADO; ningún contrato nuevo, tipo nuevo ni decisión arquitectónica nueva en las 288 líneas añadidas.

# 7 · MI RECOMENDACIÓN

# INSUFICIENTE PARA F5

**La razón, en una línea:** **`HH2-08` está FALLIDO** — `11-ARQ`:**9288** sigue byte a byte como estaba y reproduce la obligación de `O21` §3 **sin la precondición «para un gate válido»** que la sede canónica escribe en L485, mientras el `CORRIGENDUM` §19 afirma en L646-649 que **sí** está corregida, sin el comando que su propia cabecera exige; **y `HH2-10` está FALLIDO en su mitad de propagación**, con `11-ARQ`:**9720** conservando «los nueve gates» dentro del bloque que proyecta `O20`, cuyo texto canónico dice «los ocho».

**Se dispara un supuesto del §7, y sólo uno:** *remedio que introduce otro defecto*, en su forma más incómoda — una sede derivada que afirma falsamente haber aplicado un remedio, dentro del documento cuyo objeto es señalar afirmaciones falsas.

**Declaro lo que NO he usado:** que el verificador de `F6` no esté implementado; que sus contratos no estén ejecutados; que PesquerApp no haya comenzado; que no exista runtime; que la batería no certifique nada de `F6`; ni un verde ni un rojo de esa batería. Y no he contado `JA-01` ni `JA-02`.

**Lo que consta a FAVOR:** el sobre reproduce sus siete obligaciones y transporta las **81 de 81 líneas** de `O19` · **las 88 filas del manifiesto casan sin una discrepancia** y **la fila del derivador no reincide por séptima vez** · el alcance es exactamente el declarado · **el BLOQUEANTE y el GRAVE anteriores están CERRADOS y verificados por ejecución**, con `DD-01` dentro y `SIS`/`F4c` recuperados como doc30:2962 adjudicó · el conjunto de `V6-15` crece solo, y lo probé · el control de `C-L.7` deriva sus catorce campos y delata una inyección · **diez de doce cerrados, y `HH2-09` cierra su CLASE** · el aparato de este gate cumple por primera vez la regla del índice en los dos árboles · ningún hallazgo declarado superado.

**Sobre `C-L.5` no me pronuncio: es del adjudicador.** Le dejo medido: `OBLIGATORIO − ASIGNADO = ∅` en las dos direcciones sobre la candidata (88 = 88); sobre el árbol del gate el único hueco es **el propio manifiesto**, exención de PUNTO FIJO de `DD-19`; y **`ASIGNADO − LEÍDO = ∅` en mi lote**.

**Yo recomiendo; adjudica otro. No he corregido nada y el clon está eliminado.**

`JA`, revisor independiente. Cierro.

## 5 · DICTAMEN ÍNTEGRO DEL REVISOR `JB` — suficiencia arquitectónica, contratos, fases y estado


**No he modificado el repositorio auditado.** `git status --porcelain` vacío al abrir y al cerrar; `git rev-parse HEAD` = `154a66b89c166a16ce9dd203fb17fb54cd5fe147`; cero ediciones, cero commits, cero push. Los dos clones desechables vivieron bajo `scratchpad/JB-clon*/` y están **borrados**.

# 1 · CUMPLIMIENTO DEL SOBRE — las siete obligaciones

**OBLIGACIÓN 1 · recalcular los DOS digest antes de leer nada. CUMPLIDA**, y fue mi primer acto.

| árbol | digest recalculado por mí | ¿= sobre? |
|---|---|---|
| CANDIDATA `909a7a1` | `d59af7003cf3d93a4ddc5f3a1ead90d60be15480e02b1ff18e40606824583ab6` | **SÍ** |
| GATE `154a66b` | `c8983f7cff882ff9c3f2e395baa3d22ec5ab0cad9e34c82ac70d993937c0ed86` | **SÍ** |

**El gate no es INVÁLIDO por esta vía**, y sigo.

**OBLIGACIÓN 2 · el manifiesto, EN EL COMMIT DEL GATE. CUMPLIDA.** `sha256sum` → `4b022c1be1d5e2e73d13cde3d8d9e92effb55488dcf41fb90f71cc731b9ed88c`, idéntico al sobre. **316 líneas, leído íntegro del commit**, nunca del árbol de trabajo.

**OBLIGACIÓN 3 · cada fila contra SU árbol, y la del derivador primero. CUMPLIDA.** Miré primero la fila 23 de §5 —`derivar-universo-obligatorio.py`, 857 líneas, `fc8adef3a8baf223fd8bc9ae9403b2e5430c6c5f4cc09e83803d301b920fd0be`—: **es EXACTA en los DOS commits. NO reincide `U-02`/`X-06`, por séptima vez.** Comprobé mis seis filas de §4 contra la candidata: las seis casan en líneas y en SHA-256. La fila 1 (`00-INDICE.md`, 255 líneas, `6339aa806335…`) es la de la candidata, **no la del gate** (257, `4045a607c409…`) — que es exactamente lo que el sobre publica.

**OBLIGACIÓN 4 · las dos superficies de diferencia no son la misma. CUMPLIDA.** El sobre publica **2** rutas de universo; `git diff --name-only 909a7a1 154a66b` devuelve **5**: las 2 más los tres ficheros de evidencia, que §6 del manifiesto declara fuera del universo con su razón. **El sobre advierte de esta distinción expresamente.**

**OBLIGACIÓN 5 · qué prueba y qué no el `porcelain` vacío. CUMPLIDA.** Emisor `f915a840fae8b1553082ccbf381551b8a3abb10dd515a64d314a32772e30d20a` y derivador `fc8adef3…0fd0be` idénticos en los dos commits. **Asumo la limitación que el propio sobre declara** (`Z-11`).

**OBLIGACIÓN 6 · la sede canónica y toda paráfrasis. CUMPLIDA, y de aquí sale mi hallazgo principal.**

| | recalculado sobre `909a7a1` | líneas | ¿= sobre? |
|---|---|---|---|
| sede entera | `ebfef288de70d1ec6d58306720440b9a4c706197cc66f99b92e54a147678fc9a` | 559 | **SÍ** |
| `O17` | `0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125` | 85 | **SÍ** |
| `O18` | `ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353` | 111 | **SÍ** |
| `O19` | `d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632` | 81 | **SÍ** |
| `O20` | `ebc5b2cd159336c5be5b7557d624082fbe15a7b7cff7ee912dbebf4e354612af` | 110 | **SÍ** |
| `O21` | `e9dd2fb9e780e505ede8334a1795a102d85a1187de946bf6d2aa0799e7b20810` | 112 | **SÍ** |

Los dos commits publican la misma sede **byte a byte**. Contrasté `O21` contra **todas** sus proyecciones: **encuentro UNA que AMPLÍA el texto canónico, que el gate anterior ya había nombrado por fichero y línea, y que esta tanda declara corregida sin estarlo.** Es `JB-01`.

**OBLIGACIÓN 7 · el TEXTO ÍNTEGRO de `O19` viaja en el sobre. CUMPLIDA.** Recorté el bloque (sobre `L153`–`L235`), le quité la sangría —comprobé programáticamente que **toda** línea no vacía la lleva— y `sha256sum`: **81 líneas · `d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632`**. **Son las 81 de 81 líneas: no es un resumen.** Y **no lo di por bueno leyéndolo del árbol auditado**.

### VEREDICTO SOBRE LA VALIDEZ: **el gate es VÁLIDO en todo lo que puedo medir.**

# 2 · MANIFIESTO DE LECTURA

| # | ruta | líneas | SHA-256 recalculado por mí | alcance | ¿ÍNTEGRA? |
|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | **255** | `6339aa806335ce93d91cc66fa4ecb1231a285e7934f39f527ba909c08c54e187` | íntegro | **SÍ, L1–L255** |
| 1b | `00-INDICE.md` (árbol del GATE) | **257** | `4045a607c409e9a6ceb2c3fea75a66f4a6b5fbb2edf14ce143be5fa6e61159f9` | obligación 4 | **SÍ**, por `diff` íntegro: difiere en dos filas y las leí las dos enteras |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | **12103** | `e65c9c02572ce63d47f68673b3c9d083e85dc56f8c5ccd40e53afb4cf02a69ec` | `L5201`→final | **SÍ, L5201–L12103, sin hueco** |
| 3 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | **5923** | `1ddaba90c0140c07f3d04712d4269fd390ff9feb7402d2d2bc054fac12799f98` | `L2901`→final | **SÍ, L2901–L5923, sin hueco** |
| 4 | `docs/evolucion/31-GATE-FINAL-O21-F4C.md` | **783** | `d184e9528ce38356235d726385eb4cb795d3a75daaaf0e19450fb33c57616eba` | íntegro | **SÍ, L1–L783** |
| 5 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | **1495** | `c8cb3a5ca5a73627f8836cf222d32d28abdf3308d182c0f8e67feee94ddfa1e9` | íntegro | **SÍ, L1–L1495** |
| 6 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | **559** | `ebfef288de70d1ec6d58306720440b9a4c706197cc66f99b92e54a147678fc9a` | íntegro · SEDE | **SÍ, L1–L559** |
| 7 | manifiesto (commit `154a66b`) | **316** | `4b022c1be1d5e2e73d13cde3d8d9e92effb55488dcf41fb90f71cc731b9ed88c` | íntegro | **SÍ, L1–L316** |

**Rangos exactos abiertos:** doc 11 `5201-6000·6001-6800·6801-7600·7601-8400·8401-9100·9101-9620·9621-10080·10081-10560·10561-11040·11041-11600·11601-11900·11901-12103`. CHECKPOINT `2901-3500·3501-4100·4101-4540·4541-4960·4961-5460·5461-5923`. Doc 31 `1-230·231-430·431-630·631-783`. DECISIONES `1-120·121-250·251-370·371-600·600-800·800-1050·1050-1290·1288-1495`. Sede `1-200·200-445·445-559`. Manifiesto `1-170·171-316`.

**PRIMERA Y ÚLTIMA SECCIÓN SUSTANTIVA, y dos anclas de regiones separadas:**

| fuente | primera | última | ancla A | ancla B |
|---|---|---|---|---|
| `00-INDICE` | «Los documentos en voz del Owner» (L14) | «Lo que este trabajo ha corregido de sí mismo» (L250) | L35, fila de la sede reescrita por `HH2-06` | L173-174, las dos filas de manifiesto de `HH2-12` |
| doc 11 `L5201+` | `# 5 · Sistema de auditoría y mejora continua` (L5236) | `## 20.5 · De dónde sale el conjunto de fixtures de V6-15` (L12044) | L7772-7790, contrato `gate:sistema-conforme` de §9.6 | L11934-11954, las 19 filas `V6-01`…`V6-19` |
| `CHECKPOINT` `L2901+` | «Estado de las fases» (L2936) | «Siguiente acción exacta — HISTÓRICA, anterior al documento 22» (L5827) | L4342-4365, la tabla de los 22 | L4629-4640, el parte `HH2-01`…`HH2-12` |
| doc 31 | «§0 · Qué se juzgó, y sobre qué» (L11) | «§7 · Estado exacto…» (L761) | L518-529, la matriz consolidada | L571-596, el reparto de procedencia |
| `DECISIONES` | «§1 · Decisiones tomadas sin consultar» (L11) | «§4 · Límites declarados» (L1477) | L545-566, el epígrafe de `D108` (`HH2-09`) | L1347-1386, la entrada `O21` de §2 |
| sede del Owner | «Reglas de esta sede» (L15) | `# O21 · C-L.5 deja de ser un acto discrecional` (L447) | L108-124, las doce reglas de `O17` | L487-497, §3 de `O21`, «Para un gate **válido**» |
| manifiesto | §1 «Objeto del reparto» (L18) | §10 «La validación de ESTE commit» (L302) | §4, tabla de reparto (L87-96) | §7, las dieciocho preguntas (L216-257) |

### DECLARACIÓN CONTRA MI PROPIO INTERÉS

1. **`ASIGNADO − LEÍDO = ∅` en mi lote.** Las seis fuentes asignadas leídas íntegras, más el manifiesto. No hay tramo sin abrir.
2. **Leí FUERA de mi lote, y lo declaro.** `CHECKPOINT` **`L972`–`L2900`** —el bloque reanudable entero, la `regla_de_reanclaje` con sus ocho reglas y la CLASIFICACIÓN VIGENTE de las `C-L`— **es del lote de `JA`**, y lo abrí porque el punto 4 de mi encargo me obliga a recorrer los catorce campos y **su sede está ahí, no en mi rango**. Lo declaro como lectura dirigida de material ajeno, **no como cobertura mía.** También abrí el `CORRIGENDUM` §19-§20 (L618-660) y el documento 30 (L2962), y **ninguno lo declaro leído íntegro**. **Ningún hallazgo mío se funda ÚNICAMENTE en lectura ajena.**
3. **Mi encargo y el §4 del manifiesto afirman un reparto que el árbol no sostiene**: es `JB-03`.
4. **Lo que NO puedo comprobar:** que el emisor y el derivador que CORRIERON sean los publicados; y que la sede canónica sea el texto que el Owner emitió. Limitación TRANSITORIA que `O18` declara.

**`ASIGNADO − LEÍDO` = ∅.**

# 3 · LOS DIECIOCHO PUNTOS

**1 · `O21` conserva su texto y su autoridad. → DEFECTO (`JB-01`).** El texto canónico **no se ha tocado**. **APPEND-ONLY COMPROBADO**: `git log --diff-filter=A` da un solo commit de creación (`1d3b5d4`), y los dos posteriores son apéndices puros —`@@ -334,0 +335,110 @@` y `@@ -444,0 +445,115 @@`—: **cero borrados, cero modificaciones de líneas anteriores.** Pero `O21` §3 condiciona su obligación —«**Para un gate válido:**…»— y **`11-ARQ`:9288 (§15.4, fila `O21`) sigue reproduciéndola SIN esa precondición, byte a byte idéntica a la base**, mientras el `CORRIGENDUM` §19 y el parte del `CHECKPOINT` afirman que está corregida.

**2 · `C-L.5` por sus SEIS condiciones de `O21` §4. MEDIDAS, no deducidas.**

    1  corpus obligatorio DEFINIDO ...................... SATISFECHA
         candidata 88/93831 · gate 89/94149, y los dos digest reproducen
    2  manifiesto previo de ASIGNACIÓN publicado ........ SATISFECHA
         commiteado en 154a66b antes de que yo existiera, SHA verificado, con su fila
         en 00-INDICE en el MISMO commit (DD-17)
    3  manifiestos posteriores de LECTURA publicados .... PARCIAL, y sólo el mío puedo medir
    4  OBLIGATORIO menos ASIGNADO = vacío ............... SATISFECHA sobre la CANDIDATA
         88 fuentes derivadas = 88 filas (8 de §4 + 80 de §5). Sobre el árbol del GATE el
         único hueco es el propio manifiesto, exención de PUNTO FIJO de DD-19 declarada
         por adelantado en su §6
    5  ASIGNADO menos LEÍDO = vacío ..................... VACÍO EN MI LOTE
    6  revisores INDEPENDIENTES que declaran contra su
       propio interés qué leyeron ....................... CUMPLIDA POR MI PARTE

**Cinco medibles por mí se cumplen. No emito la palabra: `O21` §3 se la asigna al adjudicador, y mi recomendación de insuficiencia no es —ni debe leerse como— una razón para no certificar cobertura.**

**3 · Cobertura y suficiencia se adjudican INDEPENDIENTEMENTE. → CORRECTO, con la salvedad de `JB-01`.** Bien escrita en la sede (`O21` §2, §7, §8) y bien instrumentada: §9 del manifiesto separa las dos declaraciones; `D110`(i)-(ii) y el `CHECKPOINT` L2567 la conservan **con** su precondición. **Lo que falla es §15.4 del documento 11.**

**4 · `C-L.7` por CLASE. → CERRADA EN SU INSTRUMENTO Y NO CERRADA COMO CLASE (`JB-02`).** El comando de la **regla 7** **devuelve 14 campos, no el conjunto vacío: `HH2-02` está materialmente cerrado.** El barrido mecánico nuevo **sale VACÍO**. Recorrí los CATORCE:

| # | campo | L | ¿copia? | ¿fragmento? | ¿histórico rotulado? |
|---|---|---|---|---|---|
| 1 | `actualizado` | 974 | **no** (`HH2-10`) | no | n/a |
| 2 | `regla_de_reanclaje` | 978 | no | no | n/a — deriva 14 campos, barrido vacío |
| 3 | `metodo` | 1055 | **no** | no | n/a |
| 4 | `metodo_anterior` ×15 | 1086…1273 | sí, y es su sitio | no | **SÍ** |
| 5 | `based_on` | 1275 | **no** | **no** | n/a |
| 6 | `rama_de_trabajo` | 1333 | **no** | no | **SÍ** |
| 7 | `freshness` | 1349 | no | no | **SÍ** |
| 8 | `last_meaningful_event` | 1352 | **no** — «los NUEVE» RETIRADO (`HH2-10`) | no | n/a |
| 9 | `last_meaningful_event_anterior` ×15 | 1377…1645 | sí, y es su sitio | no | **SÍ** |
| 10 | `procedencia_de_la_critica` | 1648 | n/a | no | **SÍ** — campo entero, regla 8 |
| 11 | `owner_captado` | 2287 | **no** | no | **SÍ** (`HH2-11`) |
| 12 | `pregunta_pendiente` | 2327 | **no** | no | **SÍ** |
| 13 | `siguiente` | 2359 | **no** | no | **SÍ** |
| 14 | `falta_para_cerrar_la_capa` | 2806 | **SÍ: `JB-02`** | **no** (`HH2-04`) | **SÍ** (`HH2-05`) |

**Trece de los catorce pasan.** El decimocuarto conserva una **viñeta VIGENTE** (`L2889-2891`) que **enumera cinco familias adversariales donde §19 del documento 11 enumera ocho**: omite `X-S`, `X-O` y **`V6-<nn>`**.

**5 · `M-04`. → ESTADO CORRECTAMENTE SUSTENTADO.** `CHECKPOINT`:4276-4307 la declara **NO SUPERADA**, con el cardinal **RETIRADO** y remitido (`HH2-07`), su mitad de implementación en `F6`, y escribe que **no la cierra ningún verde de la batería interna**. **Sin defecto.**

**6 · `V6-15` es coherente y CONSTRUIBLE. → CORRECTO. `HH2-01` cerrado por sus dos mitades.** *Mitad primera:* ejecuté el comando y devuelve **ÁRBOLES**: `26:59` · `27:49` · `28:63` · `29:41`. **Entrada, escenario negativo y cierre remiten al mismo comando.** *Mitad segunda:* §20.5 escribe «QUIÉN ESPECIFICA: **`SIS`**, y su fase es **`F4c`**» y «El OCTAVO árbol —`DD-01`, documento 26— **ESTÁ DENTRO**», con la **DEUDA de `VER`/`F6` RETIRADA**. **Sin defecto.**

**7 · El conjunto es HOMOGÉNEO y DERIVABLE. → SÍ, medido.** 4 líneas, `rc=0`, un árbol por documento. §20.5 declara **qué NO alcanza** y **cómo entrarían solos**. **Sin defecto.**

**8 · `V6-16` declara `PN-19`. → CORRECTO, sin reserva.** §20.4 declara CONTRATO DEPENDIENTE, NORMA, SEDE, **FASE `F5` — no `F6`**, **PROPIETARIO el Owner**, y **CONDICIÓN EXACTA en tres incisos numerados**. **No es una etiqueta.**

**9 · `V6-19` contiene MATERIALMENTE la obligación de `C-11`. → SÍ.** No la nombra: **la contiene**. Entrada «hoy, la del recuento de líneas de un blob», positivo que exige coincidencia **en todo caso frontera, incluido el fichero VACÍO**, negativo que da ROJO ante una segunda definición **aunque hoy coincida**, cierre **exacto y medible**. **Sin defecto.**

**10 · Clasificación semántica. → CORRECTA.** **19 filas, 18 `CONSTRUIBLE` · 1 `BLOQUEADO_POR_DEPENDENCIA`**, las 19 con **10 celdas** y **ninguna vacía**. El único bloqueado cumple los tres requisitos de §20.3. **Sin defecto.**

**11 · Ningún bloqueado se cuenta como construible. → CORRECTO.** «**No se suman**». **18 + 1 = 19.**

**12 · Ninguno se presenta como implementado. → CORRECTO.** **Todas las coincidencias son negaciones o condicionales.** **Sin defecto** — y la limitación real es que **nada mecánico lo impide**, que es la mitad de implementación de `M-04`: **no la uso como razón.**

**13 · §18 en TODOS sus enunciados. → CORRECTO. `HH2-03` cerrado.** El grafo lleva el nodo 9 y la arista; **y el bloque en prosa dice ahora lo mismo** (L11012-11028), con regla de desempate escrita.

**14 · PesquerApp depende de que `F6` implemente Y certifique. → CORRECTO.** La cadena resiste en la sede (`O20` §8) y en **nueve sedes vivas**. **Mi barrido en dirección contraria no devuelve ninguna que la autorice.**

**15 · No queda arquitectura oculta. → CORRECTO.** `PN-13` a `PN-19`: las siete con fuentes, alcance, qué bloquea y qué no, condición de reversión y prueba que **FALLA HOY**. Donde hay salidas incompatibles, **el corpus declara que elegir es del Owner y no elige**.

**16 · Ningún hallazgo suavizado por cambio de fase. → CORRECTO, y en el caso decisivo va en la dirección contraria.** `HH2-01` **devuelve** la mitad del remedio de `H-06` a `SIS`/`F4c`. **Ningún hallazgo se declara SUPERADO.**

**17 · Ningún material protegido modificado. → CORRECTO, medido.** CERO. La sede sigue append-only; `HH2-08` respeta la frontera para su tercera sede.

**18 · ¿Los cinco ficheros son SUFICIENTES? → NO.** Once de los doce están materialmente aplicados, y dos **contra el objeto real**. Pero **`HH2-08` nombra tres sedes y una de las dos editables no se tocó**: `11-ARQ`:9288 es **byte a byte idéntica a la base**. La precondición se añadió a `§15.8`/`D110` (L9739), **una sede distinta que el gate no nombró**. **`HH2-08` no está cerrado, y dos sedes vigentes afirman que sí.**

# 4 · HALLAZGOS

### `JB-01` · **GRAVE** · clase **A** · **INTRODUCIDO POR `909a7a`** (por omisión y por afirmación falsa)

**Sede.** Defecto no corregido: `11-ARQUITECTURA-INTEGRADA.md`:**9288** (§15.4, fila `O21`). Afirmaciones falsas que lo tapan, ambas de `909a7a`: `CHECKPOINT-ADS-NEXT.md`:**4636** y `CORRIGENDUM`:**§19**. Sede canónica: `ADS-OWNER-RESOLUCIONES.md`:**487-497**.

**Qué dice.** §15.4 L9288: «…**no es discrecional** —cumplidas sus seis condiciones el adjudicador DEBE certificar…—», **sin precondición alguna**. `CHECKPOINT`:4636: «Las **dos sedes editables recuperan la precondición**». `CORRIGENDUM` §19: «§15.4 del documento 11 y la fila del índice— sí son editables y **están corregidas**».

**Por qué está mal.** **(i) `HH2-08` no está cerrado en una de sus dos sedes editables**, nombrada por fichero y línea y **byte a byte idéntica a la base**. **(ii) La sede superviviente AMPLÍA el texto canónico**: leída literalmente obliga a certificar cobertura **sobre un gate INVÁLIDO**, que `O21` no dice y que §11.6 contradice. Es la obligación 6 del sobre, la cláusula 9 de §11.9 y el escenario `X-O13`. **Es la clase de la que nació `O19`.** **(iii) Dos sedes VIGENTES afirman que está corregida**, una de ellas el `CORRIGENDUM`, cuyo objeto es señalar errores de hecho. La corrección se aplicó a una **sede que el gate no nombró y que no llevaba el defecto**.

**Qué lo probaría.**

    sed -n '9288p' 11-ARQ | grep -c 'gate VÁLIDO'                    → 0
    grep -n 'sobre un gate VÁLIDO' 11-ARQ                            → sólo 9739 (§15.8)
    diff <(git show eafd2ee:…|grep '^| `O21`') <(git show 909a7a1:…|grep '^| `O21`')  → sin salida
    awk '/^# /{p=($0~/^# `O21`/)} p' sede | grep -c 'Para un gate'   → 1

`git blame` sobre `CHECKPOINT`:4636 → **`909a7a14`**. Sobre `11-ARQ`:9288 → `07a6975e`, **y `909a7a` no lo tocó**.

**Remedio, y NO pertenece a `F6`.** Restituir la precondición en §15.4 L9288, o retirar de esa celda la formulación y remitir a la sede; y corregir las dos afirmaciones falsas. **Es una frase.**

**Residuo de la misma clase, declarado y NO contado aparte:** la entrada `O21` de §2 de `DECISIONES`:**1373** reproduce igualmente la obligación sin la precondición. **No la elevo a hallazgo propio** porque su encabezado declara ser proyección derivada y porque ningún gate la nombró. **Es la cuarta instancia viva de la clase.**

### `JB-02` · **MENOR** · clase **A** · **PREEXISTENTE** (`f8fc037`); **`909a7a` no lo introdujo y su barrido no lo vio**

**Sede.** `CHECKPOINT-ADS-NEXT.md`:**2889-2891**, viñeta de `falta_para_cerrar_la_capa`, **sin rótulo y por tanto VIGENTE** por la regla 8 nueva.

**Qué dice.** «NADA PROBADO: las filas de la tabla adversarial de §2.6.7, las ventanas `W1`–`W17`, las comprobaciones `X-A`–`X-H`, los escenarios negativos de §11.5 y los escenarios de §14 están ESCRITOS.»

**Por qué está mal.** Enumeración viva al lado de una sede que crece, contra la **regla 1**. §19 del documento 11 enumera **ocho** familias; la viñeta omite **tres**, y entre ellas **`V6-<nn>`**, que `H-12` metió expresamente en ese inventario. Clase `J-07`/`H-10`/`HH2-06`, viva **dentro del campo que el parte declara barrido campo a campo**. No lo detecta el barrido mecánico porque busca **cardinales**, y aquí el defecto es una **enumeración sin cardinal**.

**Remedio, y NO pertenece a `F6`.** Retirar la enumeración y remitir a §19. Es una línea.

### `JB-03` · **LEVE** · clase **A**, y es **DEL APARATO DE ESTE GATE**

**Sede.** El manifiesto (commit `154a66b`), **§3 L80-82** y **§4 fila 5**.

**Por qué está mal.** **(i)** La **CLASIFICACIÓN VIGENTE de las `C-L`** vive en `CHECKPOINT`:**2468-2796**, **fuera** del rango `L2901+` asignado a `JB` y **dentro** del asignado a `JA`. Igual la `regla_de_reanclaje` (L978-1053). **El manifiesto afirma un reparto que su propio árbol no da**, que es literalmente `C-05` —el remedio que ese manifiesto declara aplicar—. **(ii)** El rango publicado, `L2901-L6021`, excede el fichero, que tiene **5923**.

**Consecuencia real, acotada.** Lo cubrí igual, leyendo fuera de lote y declarándolo. **No invalida el gate y no altera ninguna resta**: el universo se asigna por FUENTE y no por rango, y `OBLIGATORIO − ASIGNADO` sigue vacío. **Es la quinta vez que el aparato de un gate incumple una regla que ese mismo aparato escribe.**

**Introducido por.** El commit del gate `154a66b`.

**Recuento:** GRAVE **1** · MENOR **1** · LEVE **1** = **3**. Clase **A 3 · B 0 · C 0**. **Nada vuelve al Owner.** **Ninguno se funda en que el verificador de `F6` no esté implementado**, ni en ninguno de los otros cinco supuestos excluidos. **No he usado ningún verde ni ningún rojo de la batería como fundamento.**

# 5 · MI RECOMENDACIÓN

# INSUFICIENTE PARA F5

**La razón, en una línea:** `HH2-08` no está cerrado —§15.4 del documento 11 sigue, byte a byte como en la base, reproduciendo la obligación de `O21` **sin la precondición «para un gate válido»**, es decir **ampliando el texto del Owner en la sede que el gate nombró por fichero y línea**— y **dos sedes vigentes escritas por esta misma tanda declaran que sí lo está**.

**Se disparan dos supuestos del §7:** *obligación ausente* y *remedio que introduce otro defecto*.

**Lo que consta a FAVOR:** el sobre reproduce las siete obligaciones y transporta las **81 de 81 líneas** de `O19`; la fila del derivador **no reincide por séptima vez**; **el BLOQUEANTE `HH2-01` está cerrado por sus DOS mitades y contra el objeto real** —§20.5 deriva **ÁRBOLES** y `DD-01` recupera **`SIS`/`F4c`**—; **`HH2-02` está cerrado**: el comando **deriva 14 campos** y **trece de los catorce pasan las tres preguntas**; **`HH2-03` está cerrado en los DOS enunciados de §18**; la sede es **APPEND-ONLY comprobado**; los 19 contratos tienen sus 10 celdas y su clasificación es correcta; **`V6-19` contiene materialmente `C-11`**; **§20.4 declara su única dependencia entera**; **PesquerApp bloqueada en nueve sedes**; ninguna deuda de `F6` presentada como implementada; **ningún hallazgo SUPERADO**; **no queda arquitectura oculta**; **ningún material protegido tocado**.

**Sobre `C-L.5` no me pronuncio: es del adjudicador.** He medido sus seis condiciones: **cinco medibles por mí se cumplen y `ASIGNADO − LEÍDO` es ∅ en mi lote.** `O21` §8 le prohíbe negar la certificación por haber encontrado estos tres defectos, y `O21` §2 le prohíbe deducir una declaración de la otra.

**Yo recomiendo; adjudica otro. No he corregido nada.**

## 6 · ADJUDICACIÓN ÍNTEGRA DE `JC`

Contexto limpio: no he escrito nada de este corpus, no he aplicado ninguna corrección, no he participado en ningún gate anterior. **Cero ediciones, cero commits, cero push.** Todo lo adversarial vivió en `scratchpad/JC-clon/`, **ya eliminado**. No decido por mayoría: cada afirmación que sostengo la he reproducido contra fichero y línea.

## 1 · VALIDEZ DEL GATE — las siete obligaciones, reproducidas por mí

| # | obligación | mi reproducción | ¿cumple? |
|---|---|---|---|
| **1** | los DOS digest antes de leer nada | candidata `909a7a1` → **88 / 93831 / `d59af700…83ab6`** · gate `154a66b8` → **89 / 94149 / `c8983f7c…c0ed86`**, con el derivador extraído de **su propio commit** vía `read-tree`+`checkout-index`. Trees `44585ff8…` y `fb2c4c10…` | **SÍ** |
| **2** | manifiesto **en el commit del gate** | `sha256sum` → `4b022c1be1d5…d88c`, **316 líneas**, idéntico al sobre. Leído íntegro del commit | **SÍ** |
| **3** | cada fila contra **SU** árbol, la del derivador primero | fila 23 de §5 —`derivar-universo-obligatorio.py`, **857** líneas, `fc8adef3…0fd0be`— **EXACTA en los DOS commits: NO reincide `U-02`/`X-06`, séptima vez**. Las **88** filas contra la candidata: **cero discrepancias**; suma de la columna «líneas» = **93831**. Contra el árbol del gate discrepa **una sola**, `00-INDICE.md`, **la que el sobre publica** | **SÍ** |
| **4** | las dos superficies **no** son la misma | universos que difieren: **2** · `git diff --name-only`: **5** (las 2 + los tres `evidencia/*-salida.txt`). §6 del manifiesto los declara fuera del universo, y el sobre **advierte expresamente** | **SÍ** |
| **5** | qué prueba y qué no el `porcelain` vacío | emisor y derivador **idénticos en los dos commits**. Además `git ls-files -v \| grep -v '^H '` → **vacío**: ni un `skip-worktree` ni un `assume-unchanged`, la puerta que `Z-11` nombra | **SÍ** |
| **6** | sede canónica y **toda** paráfrasis | sede `ebfef288…78fc9a` / **559** · `O17` **85** · `O18` **111** · `O19` **81** · `O20` **110** · `O21` **112**, **los seis reproducen en los DOS commits**. Y en `eafd2ee` la sede es **byte a byte la misma**. El contraste produce hallazgo | **SÍ** |
| **7** | el TEXTO ÍNTEGRO de `O19` viaja en el sobre | recorté sobre **L155-235**, quité la sangría —`grep -vc '^  \|^$'` → **0**— y `sha256sum`: **81 líneas · `d86a9455…fddf632`**. `diff` contra el bloque del commit auditado: **SIN SALIDA, idénticos**. Son las **81 de 81**. Comprobado **sin ejecutar el emisor** | **SÍ** |

**Contraste de los dos sobres.** Hay **un solo sobre físico** (`6d987dbd3fda…cb532`, 315 líneas, fuera del repositorio). `JA` y `JB` publican **valores idénticos** en las trece magnitudes ancladas. **No hay diferencia entre sobres → §9 no invalida el gate.**

> Dos inexactitudes de cita, sin consecuencia: `JB` sitúa el bloque de `O19` en «L153-L235» (son **L155-L235**; publica 81 líneas y el digest correcto — lapsus de cita, no otro sobre). `JA` deriva «75 identificadores» donde el documento 31 escribió 74: **`JA` acierta**, yo derivo **75**.

### EL GATE ES VÁLIDO. Ninguna de las siete falla, y lo declaro ANTES de medir la cobertura.

## 2 · LA COBERTURA DE LOS DOS REVISORES — las dos restas, derivadas

    SOBRE LA CANDIDATA 909a7a1     obligatoria sin fila ... vacío
                                   fila sin obligación .... vacío        88 = 88
    SOBRE EL ÁRBOL DEL GATE        obligatoria sin fila ... 1
                                     el propio manifiesto: exención de PUNTO FIJO de DD-19,
                                     declarada POR ADELANTADO en su §6. Cubre a ESE fichero
                                     y a ningún otro

| fuente | asignado | declarado leído | ¿hueco? |
|---|---|---|---|
| `11-ARQ` (12103) | `JA` L1-L5200 · `JB` L5201-L**12104** | `JA` 1→5208 · `JB` 5201→**12103** | **∅** |
| `CHECKPOINT` (5923) | `JA` L1-L2900 · `JB` L2901-L**6021** | `JA` 1→2910 · `JB` 2901→**5923** | **∅** |
| `00-INDICE` · `DECISIONES` | `JB` íntegras | L1-255 · L1-1495, SHA recalculados | **∅** |
| `30` · `CORRIGENDUM` | `JA` íntegras | L1→3084 · L1→683 | **∅** |
| `31` · sede | los tres | `JA` L1→783 · `JB` L1→783 · `JB` sede L1→559 · **yo, sede 559 y doc 31 783** | **∅** |

Los dos rangos del manifiesto **exceden su fichero**: es sobreescritura, no hueco. **`ASIGNADO − LEÍDO = ∅` en los dos lotes y en el mío.**

## 3 · HALLAZGO POR HALLAZGO DE LOS DOS REVISORES

| id | veredicto mío | severidad **adjudicada por mí** | mi reproducción |
|---|---|---|---|
| **`JA` · `HH2-08` FALLIDO** | **SOSTENIDO** | **GRAVE** (el gate lo graduó MENOR; **subo, y digo por qué**) | ver §4 |
| **`JA` · `HH2-10` FALLIDO** | **CAÍDO** | — | **Rechazo la conclusión.** Ver §4 |
| **`JA-01`** enmudecimiento del barrido | **SOSTENIDO** | **MENOR** | Reproducido y **medido más fino que `JA`**: la bandera `h` sólo se reinicia al cambiar de campo. Mudas **1094** líneas — pero **638 son LEGÍTIMAS** (`procedencia_de_la_critica` lleva su rótulo **en la línea de apertura**, que por regla 8 alcanza el campo entero). El defecto real son **447**, y **435 están en `siguiente`**. **Inyecté «los 12 hallazgos» en L2400 → 0 detecciones.** `JA` sobreestimó el alcance; el defecto es real |
| **`JA-02`** truncación silenciosa | **SOSTENIDO** | **LEVE** | Inserté ` ```text ` sin sangría en L1100: los campos pasan de **14 a 4** y la guarda **pasa igual**. Contra-pruebas: mover 100 líneas → **14**; cambiar el ancla → **0**, falla ruidosamente |
| **`JB-01`** | **SOSTENIDO — es el mismo objeto que `HH2-08`** | **GRAVE** | No lo cuento dos veces |
| **`JB-02`** enumeración viva incompleta | **SOSTENIDO**, con **una corrección** | **MENOR** | §19 enumera **SIETE** familias vivas, **no ocho** como escribe `JB`. La sustancia es exacta: **omite `X-S`, `X-O` y `V6-<nn>`**. La viñeta **no lleva rótulo** → **VIGENTE por la regla 8**. `git blame` → **`f8fc037a`, PREEXISTENTE** |
| **`JB-03`** el manifiesto afirma un reparto que su árbol no da | **SOSTENIDO, las dos mitades** | **LEVE** | **(i)** la **CLASIFICACIÓN VIGENTE** vive en `CHECKPOINT`:**2468-2796**, **entera dentro de `L1-L2900`, que es de `JA`**, y §3 y §4 fila 5 se la atribuyen a `JB`. Es literalmente **`C-05`**. **(ii)** los rangos **exceden el fichero**. **No altera ninguna resta** |

### Dos hallazgos que traigo yo

| id | sede | qué | severidad | procedencia |
|---|---|---|---|---|
| **`JC-01`** | **el manifiesto de ESTE gate, §9 L283-285** | Reproduce la obligación de `O21` §3 **sin la precondición**. `grep -c 'gate válido'` → **0**, **exactamente la medición que el `CORRIGENDUM` §19 publica del manifiesto anterior**. Es la **segunda vez consecutiva** que el manifiesto de un gate comete el defecto que ese gate existe para verificar, y esta vez lo comete **el mismo commit que publica la entrada del corrigendum que lo nombra** | **MENOR** | **APARATO DE ESTE GATE** |
| **`JC-02`** | `DECISIONES`:**1373** (§2, entrada `O21`) | Reproduce la obligación sin la precondición, mientras **L592 (`D110`) del mismo fichero SÍ la conserva**. El fichero dice la misma norma de dos maneras. `git blame` → **`07a6975e`** | **LEVE** | **PREEXISTENTE** |

**Censo derivado de la clase «paráfrasis que pierde la precondición de `O21` §3»:**

    CONSERVAN   CHECKPOINT:2567 · 00-INDICE:107 (corregida por esta tanda) ·
                11-ARQ:9739 §15.8/D110 (añadida por esta tanda) · DECISIONES:592 D110
    PIERDEN     11-ARQ:9288 §15.4 fila O21  <- LA SEDE QUE EL GATE NOMBRÓ. INTACTA
                DECISIONES:1373 §2                                   <- JC-02
                manifiesto B §8  <- inmutable, correctamente derivado al CORRIGENDUM
                manifiesto de ESTE gate §9                           <- JC-01

## 4 · LOS DOCE `HH2`, UNO POR UNO — mi adjudicación

### `HH2-01` · BLOQUEANTE · **CERRADO**
Ejecuté el comando literal: devuelve **CUATRO ÁRBOLES y cero identificadores de hallazgo** (26:59 OCTAVO · 27:49 NOVENO · 28:63 DÉCIMO · 29:41 UNDÉCIMO). El comando **retirado** devuelve **75**. La cabecera es el identificador estable y el documento inmutable la sede: **§20.5 no escribe ninguno de los dos**. La fila `V6-15` remite entrada, escenario negativo y las dos restas **al mismo conjunto de ÁRBOLES**. **`DD-01` está dentro y nombrado.** §20.5 escribe «QUIÉN ESPECIFICA **`SIS`**, y su fase es **`F4c`**» — contrastado contra `30-…`:**2962**: «`SIS` especifica · **`F4c`** · al Owner **NO**». **Coincide.** La `DEUDA` `VER`/`F6` está **retirada**. **Cero cardinales escritos.**
**Control positivo mío:** planté `32-GATE-FICTICIO.md` con la cabecera; el conjunto pasa de **4 a 5 sin editar un campo**.
**Control negativo mío:** revertí el comando al anterior, **commiteado**, y la batería dio **38/38 · EXIT=0**. **Nada mecánico lo guarda** — mitad de implementación de `M-04`, que `O20` manda a `F6`: **no la uso como razón**.

### `HH2-02` · GRAVE · **CERRADO**
**Defecto reproducido:** el comando de la base devuelve **0** sobre la base **y** sobre la candidata — el defecto era del comando, no del texto. **Remedio verificado:** el nuevo deriva **14 campos reales**. **Entra en la valla:** abre en **972**, ancla en **974**, `exit` en **2929**. **No es tautológico:** **0 sobre la candidata** y **6 sobre la base** —**discrimina**—, y mi control positivo lo **delata con 1 salida**.

### `HH2-03` · GRAVE · **CERRADO**
`SE CONFIRMA EL RESTO` incorpora «**9 verificador de `F6` y raíz externa**»; la glosa dice «**de los pasos 0 a 7 Y DEL NODO 9**»; se escribe «**ESTA ES LA ÚNICA CONDICIÓN DE ENTRADA DEL PASO 8**» y la regla de desempate.

### `HH2-04` · MEDIO · **CERRADO**
`cat -A` → `…| sort$`: el comando es ejecutable; la prosa vive en su propio párrafo.

### `HH2-05` · MEDIO · **CERRADO** en su instancia
Rótulo histórico con su alcance, y el recuento **soltado y remitido**. «CUATRO BLOQUEANTES» pasa de **1 a 0**. El ALCANCE queda **NORMADO** por la regla 8. *Residuos de la clase, vivos: `JB-02` y `JA-01`.*

### `HH2-06` · MEDIO · **CERRADO**
Deja de enumerar y remite. Ejecutado: devuelve **`O17` `O18` `O19` `O20` `O21`**.

### `HH2-07` · MENOR · **CERRADO**
Las dos apariciones de la base **han desaparecido**; el censo derivado da 19. **Se retira y se remite; no se sustituye.**

### `HH2-08` · **FALLIDO** · **severidad adjudicada por mí: GRAVE**

| sede | estado |
|---|---|
| `00-INDICE.md`:**107** | **CORREGIDA** |
| manifiesto `B` §8 | **NO se toca, y es correcto**: inmutable, su diferencia va al `CORRIGENDUM` |
| **`11-ARQ`:9288 (§15.4, fila `O21`)** | **INTACTA.** `diff` de la fila entre `eafd2ee` y `909a7a1` → **SIN SALIDA** |

    awk '/^## 15\.4 /{f=1;next} /^## 15\.5 /{f=0} f' 11-ARQ | grep -ci 'gate v.lido'   -> 0
    grep -n 'gate VÁLIDO' 11-ARQ  (candidata)                                          -> 9739, UNA sola
    grep -n 'gate VÁLIDO' 11-ARQ  (base)                                               -> ninguna
    git diff eafd2ee 909a7a1 -- 11-ARQ  -> 4 hunks: @9736 @11010 @11936 @12030.
                                           NINGUNO toca 9200-9299

**Lo que la tanda corrigió es una CUARTA sede que el gate no nombró:** `11-ARQ`:**9739**, en `### D110` de **§15.8** (§15.4 = L9261-9297). **`11-ARQ`:9288 nunca se tocó.**

**Y el remedio introduce otro defecto, en la sede que existe para no contenerlo.** `CORRIGENDUM`:**646-649** afirma que §15.4 «**está corregida**». **Es falso**, y es **la única afirmación de esa entrada sin el comando que la derive**, contra la cabecera del propio documento. La misma afirmación está en `CHECKPOINT`:**4636**. `git blame` → **`909a7a14`** en las dos. La marca `HH2-08` **no aparece ni en `11-ARQ` ni en `00-INDICE`**.

**Por qué subo de MENOR a GRAVE.** El gate anterior graduó MENOR *la ausencia de una precondición*. Lo que yo gradúo es **un objeto distinto**: una **afirmación falsa de haber aplicado un remedio**, publicada en el `CORRIGENDUM`, cuyo único objeto es señalar afirmaciones falsas, y sin el comando que su cabecera exige. A eso se suma que el documento 11 queda con **dos enunciados vivos de la misma obligación que no dicen lo mismo** — la estructura idéntica que este expediente graduó **GRAVE** en `HH2-03`. Se disparan **dos** supuestos del §7.

### `HH2-09` · MENOR · **CERRADO**
`### D108` (545) · `### D109` (568) · `### D110` (581), con origen, resolución y fecha. **Y se escribe la regla que `S-19` no estableció.** **Cierra la clase.**

### `HH2-10` · MENOR · **CERRADO** — **rechazo el FALLIDO de `JA`**

| sede del gate | estado reproducido |
|---|---|
| `CHECKPOINT`:974-975 | **Ya retirada en la BASE** |
| `CHECKPOINT`:1285 → cand. 1352-1357 | **CORREGIDA.** En la base decía «los **NUEVE** declararon» en campo **VIGENTE**; en la candidata esa frase **ya no existe** y sólo sobrevive la histórica en `_anterior`, que es su sitio por la regla 5 |
| `11-ARQ`:**9720** | **INTACTA** («ninguno de **los nueve** gates le elevó esta pregunta») |

**El remedio adjudicado —«que los campos VIGENTES del bloque retiren y remitan sus cardinales»— está CUMPLIDO ÍNTEGRAMENTE.** `11-ARQ`:9720 no es un campo ni está en el bloque.

**Y el argumento nuevo de `JA` no sostiene un defecto.** (1) **El número es VERDADERO**: los ocho gates de certificación son los documentos 22-29; el noveno es el 30; `D109` se escribe después del noveno. (2) **No es una cita de `O20`**: la frase abre con «Lo que F4 NO ha elegido aquí», voz propia de F4 en un bloque rotulado DERIVADO. (3) **No AMPLÍA autoridad**: un cardinal de gates no es una obligación; contrástese con `HH2-08`, donde suprimir «para un gate válido» **ensancha materialmente una obligación**. (4) El adjudicador `WA` ya lo midió así, y **eso reproduzco**: sede L553 dice «los **nueve** gates».

**Residuo que anoto y no elevo:** `CHECKPOINT`:4638 lista «doc 11 §15.8» como sede del remedio de `HH2-10`, y allí no se cambió nada por él. Es un **puntero engañoso**, no una afirmación falsa: su prosa es verdadera.

### `HH2-11` · LEVE · **CERRADO**
Contrastado contra los cinco `ALCANCE`: `O17`, `O18`, `O20` y `O21` nombran las tres; **`O19` dice sólo `F5`**. La nueva formulación **es verdadera para las cinco**.

### `HH2-12` · MENOR · **CERRADO en los DOS árboles**

    909a7a1  -> DIFF SIN SALIDA
    154a66b8 -> DIFF SIN SALIDA      <- el aparato de ESTE gate añadió su manifiesto a la LISTA

**Primera vez en la serie que la regla del índice se cumple en los dos árboles a la vez.**

### RECUENTO, DERIVADO DE LAS DOCE ADJUDICACIONES

    CERRADO        11   HH2-01 HH2-02 HH2-03 HH2-04 HH2-05 HH2-06
                        HH2-07 HH2-09 HH2-10 HH2-11 HH2-12
    FALLIDO         1   HH2-08 (GRAVE, severidad subida por el adjudicador)
    NO APLICABLE    0

**Los DOS que decidieron el veredicto anterior están CERRADOS y verificados por ejecución.** Ningún hallazgo suavizado por cambio de fase: `HH2-01` va **en la dirección contraria**. **Ninguno declarado SUPERADO.**

## 5 · MATRIZ CONSOLIDADA DE LO QUE QUEDA VIVO

| id | sev. | clase | sede · fichero:línea | remedio EXACTO — QUÉ, no cómo | **procedencia** |
|---|---|---|---|---|---|
| **`HH2-08`** (=`JB-01`) | **GRAVE** | **A** | `11-ARQ`:**9288** · `CORRIGENDUM`:**646-649** · `CHECKPOINT`:**4636** · canónico: sede **L485** | Que **§15.4 conserve la precondición «para un gate válido»**, o que retire de esa celda la formulación y remita a la sede; **y que las dos afirmaciones de haberla aplicado digan lo que el árbol da**, con el comando que la cabecera del corrigendum exige | **MIXTO**: residuo **PREEXISTENTE** + **INTRODUCIDO por `909a7a`** (las dos afirmaciones falsas) |
| **`JA-01`** | MENOR | **A** | `CHECKPOINT`:**1033-1038** contra **1044-1054** | Que el barrido **implemente la regla 8 que el mismo commit escribe** | **INTRODUCIDO por `909a7a`** |
| **`JB-02`** | MENOR | **A** | `CHECKPOINT`:**2889-2891** | Que la viñeta **retire la enumeración y remita a §19** | **PREEXISTENTE** |
| **`JC-01`** | MENOR | **A** | manifiesto de este gate, **§9 L283-285** | Que el manifiesto **reproduzca `O21` §3 con su precondición**, o remita a la sede | **APARATO DE ESTE GATE** |
| **`JA-02`** | LEVE | **A** | `CHECKPOINT`:**1015-1017** | Que la guarda **distinga 14 de 4**, no «>0» | **INTRODUCIDO por `909a7a`** |
| **`JB-03`** | LEVE | **A** | manifiesto, **§3 L80-82** y **§4 filas 2 y 5** | Que **§4 no atribuya a un rango contenido que ese rango no contiene**, y que ningún rango exceda su fichero | **APARATO DE ESTE GATE** |
| **`JC-02`** | LEVE | **A** | `DECISIONES`:**1373** contra **592** | Que la entrada **conserve la precondición** o remita, como ya hace `D110` | **PREEXISTENTE** |

**RECUENTO, DERIVADO DE LAS SIETE FILAS:** GRAVE **1** · MENOR **3** · LEVE **3** = **7**. Clase **A 7 · B 0 · C 0**.
**Por procedencia:** PREEXISTENTE **2** · INTRODUCIDO por `909a7a` **2** · APARATO DE ESTE GATE **2** · MIXTO **1** · **deuda LEGÍTIMA de `F5`/`F6`: 0**.

## 6 · LAS DIECIOCHO PREGUNTAS

| # | pregunta | mi respuesta |
|---|---|---|
| 1 | ¿los DOCE aparecen exactamente una vez? | **SÍ.** 12 únicos, 12 filas, `comm` contra §4 del documento 31 → **vacío** |
| 2 | ¿`HH2-01` cerrado POR PROPIEDAD? | **SÍ.** 4 ÁRBOLES, 0 identificadores. Cabecera = identificador, sede = documento inmutable. Control positivo: 4→5 |
| 3 | ¿`HH2-02` con control NO TAUTOLÓGICO? | **SÍ.** Entra en la valla, deriva **14**, discrimina (**0**/**6**) y **delata una copia introducida** |
| 4 | ¿`HH2-03`…`HH2-12` cerrados? | **NUEVE de DIEZ.** Falla **`HH2-08`** |
| 5 | ¿queda algún remedio PARCIAL? | **SÍ, uno: `HH2-08`** |
| 6 | ¿algún remedio introdujo un DEFECTO NUEVO? | **SÍ, tres.** Las dos afirmaciones falsas; `JA-01`; `JA-02` |
| 7 | ¿algún hallazgo SUAVIZADO por cambio de fase? | **NO.** `HH2-01` va en dirección contraria. **Ninguno SUPERADO** |
| 8 | ¿`C-L.5` se certifica conforme a `O21`? | **SÍ.** Las seis medidas una a una en §7(A) |
| 9 | ¿`C-L.7` queda cerrada? | **NO**, y el corpus lo dice de sí mismo. Su **instrumento** está reparado; su **clase** no |
| 10 | ¿`M-04` superada o con deuda? | **DEUDA, correctamente sustentada.** Mi control negativo lo confirma — y **no lo uso como razón** |
| 11 | ¿`V6-15` es CONSTRUIBLE? | **SÍ.** Mismo tipo de objeto en los tres campos, `SIS`/`F4c`, `DD-01` dentro, y el conjunto crece solo |
| 12 | ¿`V6-16` declara `PN-19` y su dependencia de `F5`? | **SÍ.** FASE `F5`, PROPIETARIO el Owner, condición exacta en tres incisos. **No es una etiqueta** |
| 13 | ¿`V6-19` contiene MATERIALMENTE `C-11`? | **SÍ.** Cierre **exacto y medible** |
| 14 | ¿contratos de `F6` completos y bien clasificados? | **SÍ.** **19 filas · 10 celdas · 0 vacías** · **18 + 1 = 19** |
| 15 | ¿queda alguna decisión ARQUITECTÓNICA sin tomar? | **Ninguna OCULTA.** Donde hay salidas incompatibles, el corpus **declara que elegir es del Owner y no elige** |
| 16 | ¿PesquerApp sigue BLOQUEADA? | **SÍ.** **Once ficheros** la bloquean, incluida la sede `O20` §8 |
| 17 | ¿alguna deuda de `F6` como implementación? | **NO.** Todas las coincidencias son negaciones |
| 18 | ¿puede cerrarse `F4c` sin ejecutar `F6`? | **En principio SÍ** —`O20` movió la frontera—, **pero HOY NO**: `HH2-08` está FALLIDO y dejó dos afirmaciones falsas vivas |

## 7 · LAS DOS DECLARACIONES, SEPARADAS

Leí `O21` **íntegra en la sede canónica** (L448-559) antes de emitirlas. `O21` §2 me prohíbe deducir una de la otra; §8 me prohíbe negar la primera por haber encontrado defectos.

### (A) COBERTURA — las seis condiciones de `O21` §4, medidas una a una

    1  corpus obligatorio DEFINIDO ...................... SATISFECHA
         derivado por mí con el derivador de CADA commit: 88/93831 y 89/94149
    2  manifiesto previo de ASIGNACIÓN publicado ........ SATISFECHA
         commiteado ANTES de que existiera ningún revisor, SHA verificado, con su
         fila en 00-INDICE en el MISMO commit (DD-17)
    3  manifiestos posteriores de LECTURA publicados .... SATISFECHA
         §2 de JA y §2 de JB, los dos con ruta, líneas, SHA-256 RECALCULADO, alcance,
         primera y última sección sustantiva, dos anclas y rangos enumerados
    4  OBLIGATORIO − ASIGNADO = vacío ................... SATISFECHA
         vacío en las DOS direcciones sobre la candidata (88 = 88), derivada por mí.
         Sobre el árbol del gate el único hueco es el propio manifiesto: exención de
         PUNTO FIJO de DD-19, declarada POR ADELANTADO
    5  ASIGNADO − LEÍDO = vacío ......................... SATISFECHA
         vacío en el lote de JA, en el de JB y en el mío. Los rangos cubren doc 11
         (1-5200 + 5201-12103) y CHECKPOINT (1-2900 + 2901-5923) SIN HUECO
    6  revisores INDEPENDIENTES que declaran contra su
       propio interés qué leyeron ....................... SATISFECHA
         los dos declaran qué NO leyeron, qué leyeron FUERA de lote sin contarlo,
         que grep/awk/wc no son lectura, y qué NO pueden comprobar

**Las seis se cumplen. Certifico, y no es discrecional:**

### `C-L.5 CERTIFICADA PARA ESTE GATE`

**TUPLA a la que queda ligada** (`O21` §5, sus seis elementos):

    tree SHA candidato        44585ff8c5ad81d3c2aca0d502613344bb3399dd
    commit candidato          909a7a1473c732308306805da9144b4ff9fc0977
    SHA del manifiesto de
    asignación                4b022c1be1d5e2e73d13cde3d8d9e92effb55488dcf41fb90f71cc731b9ed88c
    SHA de los manifiestos
    de lectura                JA  81ff95128cad82e8ffadcc6af5780ccd62d93c86cfb8663658b8b0cea623b755
                              JB  5911593b530fea100fa82b628ed955e586fdd2e38df34685f4df823542b82167
    identificador del gate    gate/f4c-verificacion-doce-20260901 = 154a66b89c166a16ce9dd203fb17fb54cd5fe147
    identidad del adjudicador JC

**No se transfiere** a otra candidata ni a otro gate (`O21` §6).

### (B) SUFICIENCIA

### `INSUFICIENTE PARA F5`

**La razón, en una línea:** **`HH2-08` está FALLIDO** — `11-ARQ`:**9288** sigue byte a byte como en la base, reproduciendo la obligación de `O21` §3 **sin la precondición «para un gate válido»** que la sede escribe en L485, en la sede que el gate nombró por fichero y línea; **y dos sedes vivas escritas por esta misma tanda afirman que sí está corregida**, una de ellas el `CORRIGENDUM`, cuyo objeto es señalar afirmaciones falsas, y sin el comando que su propia cabecera exige.

**Se disparan dos supuestos del §7:** *remedio que introduce otro defecto* · *contradicción vigente*.

### Que no he condicionado una a la otra, con prueba contrafáctica en las dos direcciones

- **Si `HH2-08` estuviera cerrado** y nada más cambiara: las seis condiciones seguirían igual → **`C-L.5` seguiría CERTIFICADA**, y el veredicto sería **SUFICIENTE**. La cobertura es **invariante** ante el hallazgo.
- **Si `JB` hubiera dejado sin abrir un tramo de su lote**: la condición 5 fallaría → **`C-L.5 ABIERTA: condición 5`**, y el veredicto **seguiría siendo INSUFICIENTE**. La suficiencia es **invariante** ante la medida de cobertura.

**Y declaro lo que NO he usado como razón:** que el verificador de `F6` no esté implementado · que sus contratos no estén ejecutados · que PesquerApp no haya comenzado · que no exista runtime · que `M-04`, `V6-15`/`F6` o `PN-19`/`F5` sean deudas · que la batería no certifique nada de `F6`. **Ni un verde ni un rojo de esa batería funda nada.** Tampoco fundo la insuficiencia en `JA-01`, `JA-02`, `JB-02`, `JB-03`, `JC-01` ni `JC-02`: **ninguno pasa el límite del §7**. **Los cuento como vivos; no los cuento como razón.**

## 8 · ¿VUELVE ALGO AL OWNER?

**NO. Clase A 7 · B 0 · C 0.** **Nada vuelve al Owner, por octava vez consecutiva.** Los siete tienen sede, línea, contrato incumplido, procedencia por `git blame` y un remedio que **no pertenece a `F6`**.

## 9 · QUÉ CONSTA A FAVOR

- **El sobre reproduce sus SIETE obligaciones** y transporta **las 81 de 81 líneas de `O19`**, byte a byte idénticas al commit auditado, comprobadas sin ejecutar el emisor.
- **Las 88 filas del manifiesto casan contra la candidata sin una sola discrepancia**, y la suma de su columna «líneas» **es** el universo derivado. **La fila del derivador no reincide, por séptima vez.**
- **Las dos restas cierran**, y el único hueco es la exención de punto fijo declarada por adelantado.
- **Los dos hallazgos que decidieron el veredicto anterior están CERRADOS y verificados por ejecución**, con control negativo y control positivo míos.
- **`HH2-01` recupera `SIS`/`F4c` exactamente como `30-…`:2962 lo adjudicó, y mete a `DD-01` dentro.** Va **en la dirección contraria** a suavizarse.
- **`HH2-09` cierra su CLASE**, no su instancia: escribe la regla que `S-19` no estableció tras tres recaídas.
- **`HH2-12` cumple en los DOS árboles** — primera vez en la serie.
- **La sede canónica es APPEND-ONLY comprobado**: un solo commit de creación y dos apéndices puros, **cero borrados**; y es **byte a byte idéntica en `eafd2ee`, `909a7a1` y `154a66b8`**.
- **El alcance es exactamente el declarado**: cinco ficheros, los cinco `M`, **cero altas, bajas, renombrados y copias**. El sexto candidato es **idéntico en los tres commits**: la cifra publicable **es CINCO**.
- **Los 19 contratos** tienen sus 10 celdas y ninguna vacía; **`V6-19` contiene materialmente `C-11`**; **§20.4 declara su única dependencia entera**.
- **PesquerApp bloqueada en once sedes**; mi barrido en dirección contraria no devuelve **ninguna** que la autorice.
- **Ninguna deuda de `F6` como implementada**, **ningún hallazgo SUPERADO**, **ninguna decisión arquitectónica oculta**.
- Y contra el interés del veredicto: **de los doce, once están CERRADOS**, y el único FALLIDO se repara con **una frase y dos correcciones de hecho**.

`JC`, adjudicador. **No he corregido nada, el clon está eliminado y el repositorio auditado queda como lo encontré.**

---

## 7 · Estado exacto en que queda el expediente

**Esta sección la escribe el coordinador de verificación, no el gate.** El adjudicador cerró
en §6 y no participa de lo que sigue.

```text
`F4c`                     ABIERTA
`F5`                      NO AUTORIZADA
`F6`                      NO INICIADA. Su contrato está escrito —§20 del documento 11— y
                          ninguno de sus puntos implementado, ejecutado ni certificado
PesquerApp                BLOQUEADA. Sin MVP, sin piloto desechable y sin adopción parcial
`C-L.5`                   **CERTIFICADA PARA ESTE GATE**, por el acto de su adjudicador y
                          ligada a la tupla de `O21` §5. NO se transfiere a otra candidata
                          ni a otro gate
`C-L.7`                   NO CERRADA. Su INSTRUMENTO está reparado —`HH2-02` cerrado—; su
                          CLASE no
`M-04`                    NO SUPERADA, con deuda correctamente sustentada y asignada
LOS 22 DE `O20`           su matriz sigue cerrando, ninguno SUPERADO
LOS 16 DEL DOCUMENTO 30   catorce aplicados, dos a medias, ninguno SUPERADO
LOS 12 DEL DOCUMENTO 31   ONCE CERRADOS · UNO FALLIDO, ninguno SUPERADO
LO QUE QUEDA VIVO         siete, todos clase `A`, con sede, línea, remedio y procedencia
EL MÉTODO                 DETENIDO. La OPCIÓN C sigue activada, y este gate no la levanta
```

**QUÉ NO HACE ESTE DOCUMENTO.** No corrige ningún hallazgo. No declara superado ninguno. No
cierra `F4c`. No autoriza `F5`. No inicia `F5`, `F6` ni PesquerApp. No levanta la OPCIÓN C. No
reabre el método de corrección iterativa. **Registra un veredicto y para.**

**Y UNA COSA QUE ES DEL GATE Y NO DEL COORDINADOR, y por eso se transcribe literal:**
*«De los doce, once están CERRADOS, y el único FALLIDO se repara con una frase y dos
correcciones de hecho.»* Y esta otra, que el adjudicador escribe sobre sí mismo: *«Si el
hallazgo estuviera cerrado, la cobertura seguiría CERTIFICADA y el veredicto sería SUFICIENTE.
Si un revisor hubiera dejado sin abrir un tramo de su lote, la cobertura se abriría y el
veredicto seguiría siendo INSUFICIENTE. Cada declaración es invariante ante la otra.»*
