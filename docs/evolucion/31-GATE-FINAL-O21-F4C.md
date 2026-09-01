# GATE FINAL DE `F4c`, EL PRIMERO BAJO `O21` — **VÁLIDO**, `C-L.5 ABIERTA` e `INSUFICIENTE PARA F5`

> **DOCUMENTO INMUTABLE.** Una vez commiteado no se edita: los errores de hecho que contenga
> se acotan en
> [`CORRIGENDUM-DICTAMENES-INMUTABLES.md`](verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md).
>
> **Y ES EL ÚLTIMO GATE DE ESTA SERIE.** El manifiesto lo dijo antes de repartir, para que
> ningún revisor pudiera pensar que suavizar algo abría un camino. **Después de este veredicto
> el método se detiene**, y §10 registra por qué y con qué consecuencia exacta.

## 0 · Qué se juzgó, y sobre qué

```text
CANDIDATA          review/f4c-o21-semantica-de-cl5-candidate-20260901 = f232d1aab53a8c6d…
TREE SHA           4ced788caab8e0cfc59cd4fa894d9015848565e4
RAMA DEL GATE      gate/f4c-final-o21-20260901 = 2e31452cf8ed80e757d4bb23c5afdc1ff4819556
MANIFIESTO         verificacion/manifiestos/F4C-ASIGNACION-GATE-FINAL-O21-20260901B.md
                   SHA-256 4a27b5ef2146753afa5ab8c1c6fc95b195d97e493a28af642ebf97c5ef5090f8
                   commiteado ANTES de que existiera ningún revisor
SOBRE DE ANCLA     emitido UNA vez a un fichero FUERA del repositorio auditado, 316 líneas,
                   ANTES de crear a ningún agente. Los tres leyeron de ahí y ninguno lo
                   transcribió a mano
UNIVERSO           85 fuentes · 92110 líneas sobre la candidata · 87 · 92699 sobre el gate,
                   los cuatro DERIVADOS por cada uno de los tres y no leídos
AGENTES            revisores `W1` y `W2` en PARALELO y SIN VERSE · adjudicador `WA`, que no
                   vio nada hasta que los dos cerraron. Ninguno de los tres ha escrito este
                   corpus, aplicado ninguna corrección ni participado en gate anterior
QUÉ TRAÍA          `O21` del Owner, registrada en la SEDE CANÓNICA —append-only— y
                   proyectada; y los DIECISÉIS hallazgos del documento 30 aplicados
```

## 1 · EL VEREDICTO, LITERAL

```text
EL GATE ES VÁLIDO                     por sexta vez consecutiva. Las siete obligaciones
                                      del sobre reproducen para los tres, los dos sobres
                                      coinciden, y la sede canónica coincide con la huella
                                      recibida externamente

C-L.5 ABIERTA                         CONDICIÓN INCUMPLIDA: la 5 — `ASIGNADO − LEÍDO` no
                                      es vacío. Las otras CINCO se cumplen y quedan medidas

INSUFICIENTE PARA F5                  `F4c` sigue ABIERTA · `F5` sigue NO AUTORIZADA

NADA VUELVE AL OWNER                  clase A 12 · B 0 · C 0, por séptima vez consecutiva
```

**Las DOS declaraciones se emitieron POR SEPARADO, y el adjudicador escribe que no condicionó
ninguna a la otra**, que es lo que `O21` §2 y §8 le exigen. Lo dice con una prueba
contrafáctica en su §7: si el segundo revisor hubiera leído sus seis fuentes íntegras, la
cobertura estaría certificada **y el veredicto seguiría siendo INSUFICIENTE**; y si el
hallazgo bloqueante no existiera, la cobertura seguiría ABIERTA.

**Es la PRIMERA VEZ en todo el expediente que un adjudicador declara la cobertura ABIERTA
nombrando la condición exacta que falla**, y es exactamente lo que `O21` vino a hacer posible.

## 2 · Los DOCE hallazgos consolidados, y el recuento se DERIVA

> Uno por identificador. **La cifra no se escribe al lado de la tabla**: sale de ella.
>
> ```bash
> awk '/^\| \*\*`HH2-/' docs/evolucion/31-GATE-FINAL-O21-F4C.md \
>   | grep -oE 'HH2-[0-9]+' | sort -u | wc -l
> ```
>
> **NINGUNO SE DECLARA SUPERADO, y ninguno se corrige en este documento.** Un gate no corrige.

## 3 · DICTAMEN ÍNTEGRO DEL REVISOR `W1` — el APARATO


Contexto limpio: no he escrito nada de este corpus, no he aplicado ninguna corrección, no he participado en ningún gate anterior y no he visto nada de `W2`. **No he modificado el repositorio auditado**: `git status --porcelain` → 0 líneas al abrir y al cerrar; `git rev-parse HEAD` → `2e31452cf8ed80e757d4bb23c5afdc1ff4819556`; el `reflog` no registra ninguna operación mía. Los árboles adversariales viven en un clon bajo `scratchpad/W1-adv/`, con su propio `origin` bare, **fuera de `/home/jose/ads-kernel`**. Anoto contra mi interés que la rama activa hoy es `fix/f4c-propiedad-de-admision-20260831`, distinta de la del snapshot de apertura de mi sesión (`fix/f4c-perimetro-por-naturaleza-20260831`): **no la he movido yo**, y el reflog lo muestra.

## 1 · CUMPLIMIENTO DEL SOBRE — las siete obligaciones

**OBLIGACIÓN 1 · recalcular los DOS digest antes de leer nada.** CUMPLIDA, y fue lo primero que hice.

| árbol | digest recalculado por mí | ¿= sobre? | fuentes | líneas |
|---|---|---|---|---|
| CANDIDATA `f232d1a` | `ca0cacc0cbe1328dbbf7a962192d1fd616aaa0d3f0fdba272492fd8f88f22ba5` | **SÍ** | 85 | 92110 |
| GATE `2e31452` | `a50329e13f3e9cd9f10fa7d9d7701d03dc5cf81369a90cd2940597ac2e0462a5` | **SÍ** | 87 | 92699 |

Las cuatro cifras las **derivé**, no las leí. Ningún digest falla → **el gate no es inválido por esta vía.**

**OBLIGACIÓN 2 · el manifiesto, en el COMMIT DEL GATE.** CUMPLIDA. `git show 2e31452:…/F4C-ASIGNACION-GATE-FINAL-O21-20260901B.md | sha256sum` → `4a27b5ef2146753afa5ab8c1c6fc95b195d97e493a28af642ebf97c5ef5090f8`, idéntico al sobre. Leído íntegro (304 líneas) del commit, nunca del árbol de trabajo.

**OBLIGACIÓN 3 · cada fila contra SU árbol, y la del derivador primero.** CUMPLIDA, mecánicamente sobre las **86 filas** (11 de §4 + 75 de §5). **Cero discrepancias** de SHA-256 y de línea. **La fila del derivador —§4 fila 6, 857 líneas, `fc8adef3a8baf223fd8bc9ae9403b2e5430c6c5f4cc09e83803d301b920fd0be`— es EXACTA en los dos commits: NO reincide, por sexta vez.** Sólo dos filas no casan contra los dos árboles a la vez, y las dos son correctas: `00-INDICE.md` casa **sólo con la candidata** (el sobre publica `4d2077f37355 → 063c62a5c933`), y la fila 11 —el manifiesto anterior— casa **sólo con el árbol del gate**, que es lo que su propia celda declara.

**OBLIGACIÓN 4 · las dos superficies de diferencia no son la misma.** CUMPLIDA. `git diff --name-only f232d1a 2e31452` → **6 rutas**; el sobre publica **3** de universo. Las otras tres son `kernel/operativo/pruebas/evidencia/{fuentes,negativos,referencias}-salida.txt`, evidencia reejecutada, y el §6 del manifiesto las declara fuera del universo con su razón. **Las dos sedes coinciden y ninguna esconde las otras tres.**

**OBLIGACIÓN 5 · qué prueba y qué no el `porcelain` vacío.** CUMPLIDA. Emisor `f915a840fae8b1553082ccbf381551b8a3abb10dd515a64d314a32772e30d20a` y derivador `fc8adef3…0fd0be` **idénticos en los dos commits y en el árbol de trabajo**. Asumo la limitación que el sobre declara: eso prueba que los ficheros PUBLICADOS son los de los commits, **no que sean los que se EJECUTARON**.

**OBLIGACIÓN 6 · la sede canónica, y toda paráfrasis.** CUMPLIDA. Sede entera `ebfef288de70d1ec6d58306720440b9a4c706197cc66f99b92e54a147678fc9a` y los cinco digests (`O17` 85 · `O18` 111 · `O19` 81 · `O20` 110 · `O21` 112 líneas) **reproducen byte a byte en los dos commits y contra el sobre**. Y verifiqué además que **`O20` conserva su texto**: su digest sobre `f232d1a` da `c3804cdec674b140a508f84a1b19a463efe27cd31b108b443271d34dab1906f3`, exactamente el que el gate anterior ancló. **Encontré UNA paráfrasis que amplía, y va como `W1-07`.**

**OBLIGACIÓN 7 · el TEXTO ÍNTEGRO de `O19` viaja en el sobre.** **CUMPLIDA, y es lo mejor de esta tanda.** Recorté el bloque entre las dos líneas de guiones (sobre L156-236), le quité la sangría de dos espacios y le pasé `sha256sum`:

    d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632   ·   81 líneas

**Es exactamente el `DIGEST DE O19` publicado a su lado, el que la receta reproduce y el que recalculé del commit auditado.** No es un resumen: son las 81 líneas íntegras. **El gate anterior midió 2 de 62 líneas sustantivas; éste entrega 81 de 81.** `C-20` está materialmente cerrado en su instancia — y abierto en su clase, que es `W1-03`.

**Ninguna de las siete falla. El gate NO es inválido por el sobre, y sigo.**

## 2 · DECLARACIÓN DE COBERTURA REAL, CONTRA MI PROPIO INTERÉS

**`ASIGNADO − LEÍDO` = ∅ en mi lote.** Rangos exactos, sin hueco:

| ruta asignada | alcance | rangos leídos | ¿ÍNTEGRO? |
|---|---|---|---|
| `11-ARQUITECTURA-INTEGRADA.md` | `L1-L5200` | 1-520 · 520-1039 · 1040-1579 · 1580-2139 · 2139-2698 · 2699-3258 · 3259-3818 · 3819-4378 · 4379-4938 · 4939-5200 | **SÍ** |
| `11-ARQUITECTURA-INTEGRADA.md` | `L7700-L12071` | 7700-8399 · 8400-9018 · 9019-9578 · 9579-10078 · 10079-10617 · 10618-11076 · 11077-11475 · 11476-11865 · 11863-12071 | **SÍ** |
| `comprobar-correccion-gate-de-cierre.py` (4345) | íntegro | 1-700 · 700-1449 · 1450-2249 · 2250-3049 · 3050-3749 · 3750-4345 | **SÍ** |
| `derivar-universo-obligatorio.py` (857) | íntegro | 1-857 | **SÍ** |
| `emitir-sobre-de-ancla.py` (791) | íntegro | 1-791 | **SÍ** |
| `F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md` (256) | íntegro | 1-256 | **SÍ** |
| `docs/owner/ADS-OWNER-RESOLUCIONES.md` (559) | íntegro | 1-559 | **SÍ** |
| `30-GATE-ARQUITECTONICO-FINAL-F4C.md` (3084) | íntegro, **EL ÚLTIMO** | 1-519 · 520-919 · 920-1239 · 1240-1319 · 1320-1718 · 1719-2118 · 2119-2333 · 2330-2509 · 2510-2905 · 2905-3084 | **SÍ** |

**Y el manifiesto `B` que rige** (304 líneas), leído íntegro del commit del gate antes de nada.

**QUÉ NO HE LEÍDO, y no lo reclamo.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **`L5201-L7699`** —2 499 líneas, §5 a §9.5— es de `W2` y **no he leído ni una línea de él**.

**LECTURAS FUERA DE MI LOTE, declaradas para que se descuenten.** Abrí tramos puntuales de fuentes que son de `W2` y **ninguna la declaro leída íntegra**: `CHECKPOINT-ADS-NEXT.md` L30-50, L4145-4170, L4535-4550 y filas sueltas de la matriz; `DECISIONES-Y-CONTRADICCIONES.md` L545-546 y L865-880; `00-INDICE.md` L98-112; extractos por `grep` de los documentos 26-29. **Ningún hallazgo mío se funda ÚNICAMENTE en una de ellas**, y los dos que las citan (`W1-01`, `W1-08`) tienen su sede principal dentro de mi lote. Además ejecuté `grep`/`wc` sobre el fichero **entero** del documento 11 —lo que toca el tramo de `W2`—; eso son recuentos, no lectura, y no lo cuento como cobertura.

**Lo que no puedo comprobar, y lo digo:** que el emisor y el derivador que CORRIERON sean los publicados; y que la sede canónica sea el texto que el Owner emitió. Las dos son la limitación TRANSITORIA que `O18` declara de sí misma.

## 3 · HALLAZGOS

| id | sev. | clase | sede · fichero:línea | qué dice | por qué está mal | qué lo probaría |
|---|---|---|---|---|---|---|
| **`W1-01`** | **BLOQUEANTE** | **A** | `11-ARQUITECTURA-INTEGRADA.md`:**12047-12054** (§20.5) y **11939** (`V6-15`) · contra `30-…`:**2962** (remedio adjudicado de `H-06`) | §20.5 publica un comando bajo el rótulo «**EL CONJUNTO. Es la sede**», y `V6-15` declara que su ENTRADA es «el conjunto **derivado** de los **árboles adversariales** publicados por el SEXTO, SÉPTIMO y OCTAVO gate … El conjunto no se escribe: se deriva (§20.5)» | **El comando deriva OTRO OBJETO.** Ejecutado por mí, devuelve **74 identificadores de HALLAZGO** de los documentos 27/28/29 —`EE-01…EE-19`, `R1-01…R1-09`, `S1-01…S1-09`, `S2-01…S2-05`, `C-00…C-21`, `T2-01…T2-12`—, no árboles. De los 74, **a lo sumo tres** denotan árboles (`EE-01` el noveno, chk:4093 · el décimo, doc 28 · `T1-01` el undécimo, doc29:1). Los otros ~71 son defectos de redacción (`C-05`, `C-10`, `EE-02`, `R1-02`…) que **no pueden «volver a dar ROJO»**. Con eso el escenario negativo —«cada uno … vuelve a dar ROJO, uno a uno; **ni uno menos**»— y el cierre `entrada − suite = ∅ ∧ suite − entrada = ∅` pasan a ser **medibles y no satisfacibles**, y quien construya `V6-15` **sigue teniendo que ELEGIR**, que es exactamente lo que `H-06` denunciaba. **Y la SEGUNDA mitad del remedio adjudicado no se aplicó: se le CAMBIÓ LA FASE.** Doc 30:2962 exige «que el OCTAVO árbol (`DD-01`, quinto gate, doc 26), REPRODUCIDO, **tenga fixture contratado**», con **propietario `SIS`** y **fase `F4c`**. §20.5 lo convierte en «DEUDA DE INVENTARIO», **propietario `VER`**, **FASE `F6`**. Es el disparador literal del §7 del manifiesto: «se le ha cambiado la fase para ablandarlo» | Ejecutar el comando de §20.5 —74 líneas— y contrastarlo con la enumeración de árboles del checkpoint (L4003 `DD-01` · L4093 `EE-01` · doc29:1 `T1-01`). Y `sed -n '12056,12071p'` del documento 11 contra `sed -n '2962p'` del documento 30 |
| **`W1-02`** | **GRAVE** | **A** | `11-ARQUITECTURA-INTEGRADA.md`:**11012-11017** (§18), contra **10874-10926** del mismo §18 | El grafo gana el **nodo 9** y la **arista `9 → 8`** con «IMPLEMENTADO **Y** CERTIFICADO». Pero 130 líneas más abajo, el bloque que ENUNCIA la condición de entrada del paso 8 sigue diciendo, sin tocar: «SE CONFIRMA EL RESTO **1…8**» y «**el paso 8 exige la BASE COMPLETA ACORDADA de los pasos 0 a 7**, y no un MVP» | **`H-02` está cerrado en el dibujo y abierto en la frase que el adjudicador señaló como la razón de graduarlo GRAVE.** Doc 30:2730-2734 (`R-3`) lo escribe con todas las letras: «*Lo que no cae es que §18 no calla: **ENUNCIA una condición de entrada para su paso 8 —«la BASE COMPLETA ACORDADA de los pasos 0 a 7»— y esa base no contiene el verificador**. Una sede que escribe la condición equivocada es peor que una que no escribe ninguna. Si §18 callara, lo bajaría a MENOR.*» **La sede tiene ahora DOS enunciados de la misma condición y no dicen lo mismo**; quien planifique `F6` desde el bloque en prosa sigue llegando al paso 8 sin el nodo 9 | `sed -n '11005,11023p'` → cero menciones de `verificador`, `nodo 9`, `raíz externa`, `§20` o `V6-`; contra `sed -n '10874,10926p'`, que sí las lleva |
| **`W1-03`** | **GRAVE** | **A** | `emitir-sobre-de-ancla.py`:**698** y **:143** · `11-ARQUITECTURA-INTEGRADA.md`:**8447-8454** (campo 18) | El emisor transporta el texto de **`O19` y de ninguna otra**: `_o19 = cuerpos_c.get(b"O19".decode("ascii"))`. El campo 18 de §11.6 nombra igualmente «TEXTO ÍNTEGRO DE LA RATIFICACIÓN **`O19`**» | **`C-20` está cerrado por INSTANCIA y abierto por CLASE.** Los campos 17 y 19 **sí** se derivan —«TODAS las que la SEDE contenga»— y el propio fichero declara en `:141` que «la lista **no se escribe**: sale de la sede». El texto, no. **Árbol adversarial `A8`, ejecutado:** añadí a la sede una resolución `O22` que ordena expresamente que **su** texto viaje externamente, con su proyección enlazada. El emisor la ancló con su digest, **no transportó su texto**, salió `rc=0`, y la batería dio **38/38 · EXIT=0**. **Ninguna sede lo dice.** La obligación del Owner que `C-20` nombra —«toda resolución cuyo texto ordene entregar externamente»— sigue sin guardián | Reproducir `A8`: `scratchpad/W1-adv/t`, rama `adv8`. `grep -c 'Cada revisor debe recibir externamente, ademas de lo que'` sobre el sobre emitido → **0**; `grep 'DIGEST DE O22'` → presente |
| **`W1-04`** | **GRAVE** | **A** | `comprobar-correccion-gate-de-cierre.py` — **ausencia**: `grep 'V6-\|§20\|CONTRATO_CONSTRUIBLE'` → **0** | La batería no comprueba **nada** de §20. `O20` convierte §20 en el contrato de `F6`, §20.3 escribe reglas que «no admiten lectura blanda» —«**ningún contrato BLOQUEADO cuenta como CONSTRUIBLE. No se suman**»; «ninguno de los tres puede presentarse como implementado»— y ninguna es ejecutable | **La sección que este gate tiene que juzgar en su punto 8 es puramente declarativa.** Tres árboles adversariales, los tres commiteados, los tres **38/38 · EXIT=0**: **`A3`** convierte el único `CONTRATO_BLOQUEADO_POR_DEPENDENCIA` (`V6-16`) en `CONTRATO_CONSTRUIBLE` y el comando derivado de §20.3 pasa a publicar «19 CONTRATO_CONSTRUIBLE» · **`A4`** sustituye el criterio EXACTO de cierre de `V6-19` por «que `F6` lo valore razonablemente cuando lo construya» —interpretación humana no normada, el disparador literal del §7— · **`A9`** reescribe la cabecera de §20 y §20.2 como «**ESTA SECCIÓN ESTÁ IMPLEMENTADA Y EJECUTADA: el verificador de `F6` está construido y CERTIFICADO**». **Los tres en verde** | Ramas `adv3`, `adv4`, `adv9` del clon. `python3 …/comprobar-correccion-gate-de-cierre.py` → `38/38 comprobaciones en verde` en las tres |
| **`W1-05`** | **MEDIO** | **A** | `comprobar-…py`:**2243**, **2283**, **3009** (`H-11`) · `derivar-…py`:**502-547** (`H-13`) | Los dos remedios están **materialmente aplicados** hoy: los tres rótulos atribuyen el APPEND-ONLY a `O19`, y las cláusulas del `ENCARGO` describen esta tanda | **Cerrados por INSTANCIA, no por CLASE.** **Árbol `A1`:** revertí los tres rótulos a `O20` —dejando `grep -c 'H-11'` en **0**— y la batería dio **38/38 · EXIT=0**. **Árbol `A2`:** devolví dos cláusulas del `ENCARGO` a las del octavo gate («los 24 hallazgos del documento 21», «el emisor … que este gate ESTRENA») y el derivador siguió dando **87 fuentes** y la batería **38/38 · EXIT=0**. `componente_v()` (derivador :647-651) sólo comprueba que la cláusula **no esté vacía**; nada mide que un rótulo atribuya a la resolución correcta ni que el encargo describa el gate en curso | Ramas `adv` y `adv2` del clon |
| **`W1-06`** | **MEDIO** | **A** | `emitir-sobre-de-ancla.py`:**394** (`_MARCAS`) y **:405-441** · contra `11-ARQUITECTURA-INTEGRADA.md`:**8428** (campo 12) | El emisor valida que la marca de revisor case con `^[A-Z]{1,2}[0-9]?$` y cuenta las asignaciones. `X-05` se declara cerrado porque «el emisor no adivina a quién se asignó una fuente» | **Valida la FORMA de la marca, no su EXISTENCIA.** **Árbol `A5`:** reasigné `CHECKPOINT-ADS-NEXT.md` —**5 691 líneas**, la segunda fuente más grande— a un revisor `Q9` que este gate no tiene. El emisor salió **`rc=0`** publicando «`ASIGNACIONES 16`», la batería **38/38**, y `OBLIGATORIO − ASIGNADO = 0` **sigue cerrando**. El campo 12 del sobre publica un número que en sustancia es falso: 15 asignaciones reales y una a nadie. La condición 4 de `C-L.5` se satisface con una fuente que no lee nadie; sólo la resta `ASIGNADO − LEÍDO`, que calcula una persona, lo cazaría | Rama `adv5b` del clon; sobre emitido en `scratchpad/W1-adv/sobre-a5.txt` |
| **`W1-07`** | **MENOR** | **A** | `11-ARQUITECTURA-INTEGRADA.md`:**9288** (§15.4, fila `O21`) · `00-INDICE.md`:**110** · **manifiesto `B` §8, L269-273** — contra la sede `O21` §3 | Las tres escriben la obligación como «**cumplidas las seis condiciones el adjudicador DEBE certificar**», sin precondición | **Paráfrasis que AMPLÍA el texto canónico**, que es lo que la obligación 6 del sobre manda señalar y de lo que nació `O19`. `O21` §3 en la sede dice: «**Para un gate válido:** … si se cumplen las seis condiciones … el adjudicador **debe** declarar». `D110` (dec:546) y el checkpoint **sí** conservan «sobre un gate válido»; las tres de arriba **no**. Leídas literalmente obligan a certificar cobertura también sobre un gate **INVÁLIDO**, que `O21` no dice y que §11.6 contradice («un gate inválido no produce veredicto, ni a favor ni en contra»). **Y una de las tres es el §8 del manifiesto que rige ESTE gate** | `awk` sobre la sede → «Para un gate **válido**:» en su §3; `grep -c 'gate válido'` → dec **1**, chk **2**, doc 11 **0**, `00-INDICE` **0**, manifiesto `B` **0** |
| **`W1-08`** | **MENOR** | **A** | `CHECKPOINT-ADS-NEXT.md`:**4157** y **:4161** (bloque VIVO de `M-04`) | «Su mitad arquitectónica está contratada en §20 del documento 11, con **dieciocho** puntos» · «que `F6` implemente los **dieciocho** puntos» | **Cardinal caducado en el mismo commit que lo caducó.** `grep -cE '^\| `V6-[0-9]+` \|'` sobre §20.1 → **19**: esta tanda estrenó `V6-19` por `C-11`. `H-14` retiró el cardinal de tres sedes —dec:545, chk:4543, `00-INDICE`:104— y **no de ésta**, dos bloques por encima, en el mismo fichero. Es la clase `C-16`/`J-07`/`H-16`, viva. *(Sede en el lote de `W2`; la cito con línea y no la declaro leída íntegra.)* | `sed -n '4155,4162p' docs/evolucion/CHECKPOINT-ADS-NEXT.md` contra el `grep -c` de §20.1 |
| **`W1-09`** | **LEVE** | **A** | `emitir-sobre-de-ancla.py`:**714-717** | El bloque de `O19` se delimita con dos líneas de 76 guiones y sangría de dos espacios, y la instrucción al revisor es «recorte el bloque de abajo **entre las dos lineas de guiones**» | **El marco no tiene invariante.** Ninguna guarda comprueba que el texto transportado no contenga esa misma secuencia, ni que ninguna línea empiece por dos espacios que la retirada de sangría se comería. Hoy no colisiona —lo verifiqué: el digest reproduce—, y **falla en la dirección segura** (un revisor extraería un texto cuyo digest no reproduce y declararía el gate INVÁLIDO). Por eso es LEVE. Pero un marco sin invariante en el artefacto que `O19` pone el PRIMERO de los seis es una promesa sin guarda | Recortar el bloque y hashearlo, como hice: reproduce `d86a9455…` hoy; ninguna línea del emisor lo comprueba |

**Recuento:** BLOQUEANTE 1 · GRAVE 3 · MEDIO 2 · MENOR 2 · LEVE 1 = **9**. Clase **A 9 · B 0 · C 0**. **Ninguno se funda en que el verificador de `F6` no esté implementado**, y ninguno vuelve al Owner.

## 4 · LOS CATORCE PUNTOS

**1 · Los DIECISÉIS hallazgos `H-01`…`H-16`.** Contrasté los dieciséis remedios de doc 30 §9 contra el árbol de hoy. **Catorce están materialmente aplicados** y lo verifiqué uno a uno: `H-01`(c) el sobre transporta las 81 líneas de `O19` y su digest reproduce · `H-03` `O20` y `O21` tienen fila en §15.4 (L9287-9288) · `H-04` los bloques `### D109` (L9696) y `### D110` (L9725) existen · `H-05` la mitad `F6` de `C-11` se enruta a `V6-19`, que **sí** contiene la fórmula de líneas · `H-07` §20 cita `PN-19` **siete veces** y enlaza §11.8 **dos** · `H-08` los campos 17 y 19 y el paso `6bis` dicen «todas las que la sede contenga» · `H-09`/`H-10` los fragmentos huérfanos y «las tres» están retirados · `H-11` los tres rótulos dicen `O19` · `H-12` §19 y §2.1 censan la familia `V6-<nn>` · `H-13` las cláusulas del `ENCARGO` describen esta tanda · `H-14` las tres sedes retiran «once campos cada uno» y §20 acota su FUENTE · `H-15` el barrido del marcador incrustado → **0** · `H-16` los cardinales están retirados. **DOS no lo están:** `H-02` sólo en la mitad del grafo (`W1-02`) y `H-06` con la derivación del objeto equivocado y la segunda mitad del remedio cambiada de fase (`W1-01`).

**2 · Las OCHO CAUSAS INDEPENDIENTES: ¿por CLASE o por INSTANCIA?** Es la pregunta que mejor discrimina y la respondo con árboles ejecutados, no con lectura. **Cerradas por CLASE, medido:** `AA-01` —planté un segundo documento del Owner por la vía sancionada y **entra en el universo** (88 fuentes), exigiendo fila y revisor (`A7`)—; `S1-02`/`DD-02`/`EE-01` —la guarda juzga la mutación y confirmar no exime, y el falso dictamen sin enlace da **37/38 · FALLO `G-29`** (`A6`)—; `DD-01` —el perímetro es por naturaleza y publica sus 23 exclusiones con ruta—. **Cerradas sólo por INSTANCIA, medido:** `H-11` y `H-13` (`W1-05`, árboles `A1`/`A2`, 38/38) · `C-20` (`W1-03`, árbol `A8`, 38/38) · `H-02` (`W1-02`) · `H-06` (`W1-01`). **Y una causa entera sin guardián: §20** (`W1-04`, árboles `A3`/`A4`/`A9`, 38/38 los tres). **El modo de fallo del expediente —cerrar la instancia y dejar viva la clase— sigue presente en cinco de las ocho.**

**3 · `O21` y la independencia entre certificar cobertura y declarar suficiencia.** La independencia está **bien escrita** en la sede (`O21` §2 y §7), bien propagada en `D110` y bien instrumentada en el §8 del manifiesto, que separa las dos declaraciones y prohíbe condicionar la primera a la segunda. **Pero la proyección SÍ dice más de lo que la sede resuelve**, y en tres sedes: `W1-07`. La sede condiciona la obligación a «**Para un gate válido**»; §15.4, `00-INDICE` y el propio §8 del manifiesto la reproducen sin esa precondición.

**4 · `C-L.5` por sus SEIS condiciones, sobre ESTE gate.** (1) **corpus obligatorio DEFINIDO** → **SÍ**, derivado y recalculado por mí: 85 fuentes / 92 110 líneas sobre la candidata. (2) **manifiesto previo de ASIGNACIÓN publicado** → **SÍ**, commiteado en `2e31452` antes de que yo existiera, SHA verificado. (3) **manifiestos posteriores de LECTURA publicados** → **el mío es §2 de este dictamen**; no he visto el de `W2` ni la adjudicación, luego **no puedo medirla**. (4) **`OBLIGATORIO − ASIGNADO` = vacío** → **SÍ**, ∅ en las dos direcciones sobre la candidata (85 = 85); sobre el árbol del gate la única fuente sin fila es el manifiesto `B` mismo, exención de punto fijo declarada en su §6. **Con la advertencia de `W1-06`: esta resta es satisfacible con una fuente asignada a un revisor inexistente.** (5) **`ASIGNADO − LEÍDO` = vacío** → **∅ en mi lote**, con rangos enumerados en §2. (6) **revisores independientes que declaran contra su propio interés** → **cumplida por mi parte**. **Cinco medibles por mí se cumplen; la 3 y la mitad de la 5 son del adjudicador.**

**5 · `C-20` y el CONTENIDO REAL DEL SOBRE.** `O19` L315-317 enumera seis cosas. **Las recibo las seis**: el TEXTO de la ratificación (sobre L156-236, **81 de 81 líneas**, digest verificado), el SHA del commit candidato (L11), el tree SHA (L12), el SHA del manifiesto (L17), el SHA del derivador (L28) y el SHA de la sede del Owner (L89). **Medición pedida: 81 de 81 líneas sustantivas de `O19` están materialmente en el sobre. El gate anterior midió 2 de 62.** Y comprobé la receta **sin ejecutar el emisor**, con `git show` + `awk` + `sha256sum`. **`C-20` está cerrado en su instancia.** Su clase, no: `W1-03`.

**6 · `V6-15` en §20.1 y §20.5.** **Entrada, escenario negativo y criterio de cierre describen ahora el MISMO conjunto** —los tres remiten a §20.5— y en eso el remedio funciona. **Pero ejecuté el comando que §20.5 publica y deriva el objeto equivocado**: 74 identificadores de hallazgo, no árboles adversariales. **No hay un cardinal escrito disfrazado; hay una derivación que deriva otra cosa**, que es peor porque es mecánica y nadie la ejecutó. Es `W1-01`.

**7 · `V6-16` y `PN-19` (§20.4).** **CORRECTO, y lo digo sin reserva.** La dependencia está **DECLARADA** («CONTRATO DEPENDIENTE `V6-16`, y sólo él»), **ENLAZADA** a su sede (`PN-19` en §16, contrato largo en §11.8 con ancla) y con **CONDICIÓN EXACTA de desbloqueo** en tres incisos numerados —(i) identidad de escritura separada con su titular, (ii) dónde vive la evidencia fuera del árbol, (iii) quién la custodia—, más fase `F5`, propietario el Owner, qué bloquea y qué no. **No es una etiqueta.** §20 cita `PN-19` siete veces. **No encuentro defecto en este punto.**

**8 · Los contratos de §20 y su CLASIFICACIÓN SEMÁNTICA.** Derivado por mí: **19 filas**, todas con **10 celdas** —las 10 de la cabecera— y **ninguna vacía**. Reparto: **18 `CONTRATO_CONSTRUIBLE` · 1 `CONTRATO_BLOQUEADO_POR_DEPENDENCIA`** (`V6-16`). **Ningún BLOQUEADO se cuenta como construible** y **ninguno se presenta como implementado**: §20 lo niega cinco veces y el corpus lo repite en siete sedes. **`V6-19`, revisado con dureza:** tiene los diez campos, y su criterio de cierre es **exacto y medible** —«**cero** definiciones de una fórmula compartida fuera de su sede única, **medido por derivación del código**; y si la importación de la sede falla, el instrumento **NO emite**»—; el segundo inciso además ya tiene implementación de referencia (emisor :129-135). **`V6-19` es correcto.** **La clasificación es correcta hoy y no está guardada por nada** (`W1-04`), y **`V6-15` sigue sin ser construible** (`W1-01`).

**9 · El ORDEN DE CONSTRUCCIÓN de `F6` hasta PesquerApp.** El **nodo 9** existe (§18 L10874-10882) con §20 · §11.8 · `O18`(b)(c) · `O20` y la remisión a `PN-19`/§20.4; la **arista `9 → 8`** existe (L10884-10886 y L10920-10926) con «IMPLEMENTADO **Y** CERTIFICADO» y las tres exclusiones. **Y sin embargo el punto falla**, porque el bloque en prosa de la misma sede sigue enunciando la condición de entrada del paso 8 como «los pasos 0 a 7»: `W1-02`.

**10 · AUSENCIA DE ARQUITECTURA OCULTA detrás de una obligación de `F6`.** **No encuentro defecto, y esto es lo que comprobé.** Recorrí `PN-13`, `PN-15`, `PN-16`, `PN-17`, `PN-18` y `PN-19`: las seis llevan fuentes enfrentadas, texto vigente, materia mínima, alcance, qué bloquea, qué **no** bloquea, condición de reversión, propietario, fase y prueba posterior que **FALLA HOY**. Donde hay dos salidas incompatibles —`PN-16`, `PN-17`, `PN-19`— el corpus **declara que elegir es del Owner** y no elige. Y §20.4 saca a la luz la única dependencia de otra fase. **Ninguna decisión está escondida detrás de una obligación de `F6`.**

**11 · Que NINGUNA DEUDA DE `F6` se presente como implementada.** **No encuentro defecto.** Barrí `docs/` buscando afirmaciones de existencia del verificador o de un `V6-<nn>`: **todas las coincidencias son negaciones**. §20 lo niega en su cabecera, en §20.0, en §20.2 (tres veces) y en §20.3; el manifiesto lo niega en su §9 justo después de publicar «38/38»; el README de `verificacion/` y el checkpoint lo repiten. **`X63` sigue siendo contrato de prueba en todas sus sedes.** Lo único que anoto es que **nada mecánico lo impide** (`W1-04`, árbol `A9`).

**12 · Que PesquerApp SIGA BLOQUEADA.** **No encuentro defecto.** Nueve ficheros llevan el bloqueo, con las mismas tres exclusiones —«sin MVP, sin piloto desechable y sin adopción parcial»—: la sede canónica `O20` §8, §20.0, §20.2, §11.8, §18 nodo 8 y arista 9→8, `PN-19`, `D109`(vi), el checkpoint, el índice y los dos manifiestos. **Ninguna sede la autoriza, la abre ni la programa**; la única coincidencia de mi barrido en dirección contraria es la frase del propio doc 30 que dice «*no digo que PesquerApp esté desbloqueada*». **Lo que falla es la prosa de §18**, y eso es `W1-02`, no una autorización.

**13 · AUSENCIA DE REGRESIONES en `O20` y en la MATRIZ DE LOS 22.** **No encuentro defecto.** El texto canónico de `O20` sobre la candidata da `c3804cde…1906f3`, **exactamente el que el gate anterior ancló**: no se ha reescrito. La matriz tiene hoy **22 identificadores exactos**, `sort -u` = 22 filas, **un estado primario cada uno**, y la única redistribución —**15 `CORREGIDO_EN_F4c` + 7 `CONTRATO_COMPLETO_PARA_F6`**, antes 14 + 8— es `C-20` volviendo a `F4c`, que es el remedio de `H-01` aplicado. **Ningún hallazgo se declara SUPERADO**: los 24 golpes de `SUPERAD` en la matriz son, uno a uno, negaciones. La cobertura contra el documento 29 sigue cerrando.

**14 · `M-04` como PROPOSICIÓN GENERAL.** **Un árbol defectuoso SÍ pasa la batería en verde, y lo he medido nueve veces.** Detalle en §5.

## 5 · ÁRBOLES ADVERSARIALES QUE CONSTRUÍ, Y SU RESULTADO

Todos en un clon bajo `scratchpad/W1-adv/t`, con `origin` propio bare. **Todos COMMITEADOS**, que es la forma dura. Baseline reproducido: **38/38 · EXIT=0**.

| # | árbol | superficie | resultado | ¿nuevo? |
|---|---|---|---|---|
| `A1` | revertir los **tres rótulos** de `H-11` a `O20` | los tres rótulos de la batería | **38/38 · EXIT=0** | **SÍ** · `W1-05` |
| `A2` | devolver dos cláusulas del **`ENCARGO`** al octavo gate | texto del encargo del derivador | **38/38 · EXIT=0** · 87 fuentes | **SÍ** · `W1-05` |
| `A3` | `V6-16` de `BLOQUEADO_POR_DEPENDENCIA` a **`CONSTRUIBLE`** | §20.3 | **38/38 · EXIT=0**; el comando derivado publica «19 CONSTRUIBLE» | **SÍ** · `W1-04` |
| `A4` | vaciar el **criterio EXACTO de cierre de `V6-19`** por juicio humano | §20.1 | **38/38 · EXIT=0** | **SÍ** · `W1-04` |
| `A5` | asignar el **CHECKPOINT (5 691 líneas) a un revisor inexistente `Q9`** | emisor | emisor **`rc=0`**, «ASIGNACIONES 16»; batería **38/38** | **SÍ** · `W1-06` |
| `A6` | dictamen falso `31-SINTESIS-DE-CIERRE.md` («F4c CERRADA Y F5 AUTORIZADA») **sin enlace** | derivador (iv) + `G-29` | **37/38 · FALLO `G-29`**; publicado en `EXCLUIDOS_IV` | **NO** · guarda funciona |
| `A6b` | el mismo, **enlazado desde `00-INDICE`** (vector `Z-08` puro) | derivador (iv) | **38/38**, fuera del universo (87), **pero el digest del universo CAMBIA** y `EXCLUIDOS_IV` lo publica con su H1 | **NO** · declarado y visible |
| `A7` | **segundo documento del Owner** que declara `F4c` cerrada, por la vía sancionada | derivador (v), zona `docs/owner` | **entra en el universo**: 88 fuentes. Exige fila y revisor | **NO** · `AA-01` cerrado por CLASE |
| `A8` | resolución **`O22`** que ordena que su propio texto viaje externamente | emisor, `C-20` | emisor **`rc=0`** anclando su digest y **sin transportar su texto**; batería **38/38** | **SÍ** · `W1-03` |
| `A9` | §20 declarada **IMPLEMENTADA Y CERTIFICADA** | §20.0 y §20.2 | **38/38 · EXIT=0** | **SÍ** · `W1-04` |

**Seis árboles nuevos que pasan en verde.** **`M-04` no está superada, y la superficie que esta tanda ha tocado es exactamente donde están cinco de los seis.** Lo digo también en descargo: las tres guardas que gates anteriores cerraron por clase —`AA-01`, `DD-02`/`EE-01`/`S1-02`, `DD-01`— **resistieron mis ataques**, y la de `Z-08` se comporta exactamente como el derivador declara.

## 6 · MI RECOMENDACIÓN

# INSUFICIENTE PARA F5

**La razón, en una línea:** `V6-15` sigue sin poder construirse —§20.5 publica como «EL CONJUNTO» un comando que deriva **74 identificadores de hallazgo** donde su entrada nombra árboles adversariales, y la mitad del remedio adjudicado de `H-06` que exigía fixture para el octavo árbol en fase `F4c` se ha convertido en deuda de `F6`—, `H-02` está cerrado en el grafo de §18 y abierto en la frase que el adjudicador señaló como su razón de ser, y `C-20` está cerrado en su instancia con el emisor anclando `O19` por su nombre.

**Se disparan cuatro de los siete supuestos del §7:** falta CRITERIO DE CIERRE efectivo en un contrato (`W1-01`) · un hallazgo se ha cambiado de fase para ablandarlo (`W1-01`, la deuda de `DD-01`: `SIS`/`F4c` → `VER`/`F6`) · la matriz adversarial no especifica una clase reproducida (`W1-01`) · una obligación depende de interpretación humana no normada (`W1-01`, elegir qué columna gobierna). **Ninguna de mis razones es que el verificador de `F6` no esté implementado.**

**Sobre `C-L.5` no me pronuncio: no es mío.** `O21` la hace no discrecional y la liga a una tupla que incluye los manifiestos de lectura de los dos revisores; yo sólo puedo medir cinco de sus seis condiciones y las cinco se cumplen en mi lote. **La certificación la emite el adjudicador, y `O21` le prohíbe negarla por haber encontrado estos nueve defectos.**

**Y lo que consta a favor, porque es verdad:** el sobre es el mejor de los diez —transporta las 81 líneas de `O19` y las siete obligaciones reproducen— · las 86 filas del manifiesto casan sin una discrepancia y **la fila del derivador no reincide por sexta vez** · las dos aritméticas derivan y cierran contra el universo anclado · catorce de los dieciséis remedios están materialmente aplicados · `V6-19` es un contrato correcto · §20.4 declara su dependencia entera · PesquerApp está bloqueada en nueve sedes · ningún hallazgo se declara superado · `O20` conserva su texto · y ninguna sede presenta deuda de `F6` como implementación existente.

**Yo recomiendo; adjudica otro.**

## 4 · DICTAMEN ÍNTEGRO DEL REVISOR `W2` — la ARQUITECTURA DOCUMENTAL


**Ángulo: la ARQUITECTURA DOCUMENTAL.** No he escrito nada de este corpus, no he aplicado ninguna corrección, no he participado en ningún gate anterior y no he visto a ningún otro revisor. **No he modificado ni un byte del repositorio**: cero ediciones, cero commits. `git status --porcelain` sigue vacío.

## 1 · CUMPLIMIENTO DEL SOBRE — las siete obligaciones, una a una

Leí el sobre **antes que nada**, desde `/tmp/.../scratchpad/SOBRE-DE-ANCLA-GATE-FINAL-O21-20260901.txt`, fuera del árbol auditado.

**OBLIGACIÓN 1 — recalcular los dos digest de universo.** Ejecuté las dos recetas íntegras, cada árbol con su propio derivador extraído de su propio commit:

| árbol | fuentes | líneas | digest recalculado | ¿reproduce? |
|---|---|---|---|---|
| CANDIDATA `f232d1a` | **85** | **92110** | `ca0cacc0cbe1328dbbf7a962192d1fd616aaa0d3f0fdba272492fd8f88f22ba5` | **SÍ** |
| GATE `2e31452` | **87** | **92699** | `a50329e13f3e9cd9f10fa7d9d7701d03dc5cf81369a90cd2940597ac2e0462a5` | **SÍ** |

Los dos reproducen byte a byte. **El gate no es inválido por esta vía.**

**OBLIGACIÓN 2 — leer el manifiesto EN EL COMMIT DEL GATE y comprobar su SHA-256.** Lo leí con `git show 2e31452…:…B.md`, **nunca del directorio de trabajo**. Recalculado: `4a27b5ef2146753afa5ab8c1c6fc95b195d97e493a28af642ebf97c5ef5090f8` — **coincide**. Lo leí **entero, 303 líneas**.

**OBLIGACIÓN 3 — cada fila contra SU árbol, y la del derivador primero.** Miré primero la fila 6 (`derivar-universo-obligatorio.py`), que es la que `U-02` y `X-06` falsearon dos gates seguidos: `fc8adef3a8baf223fd8bc9ae9403b2e5430c6c5f4cc09e83803d301b920fd0be` en **los dos** commits — **correcta, sin falseo**. Después contrasté **las 86 filas** (11 de §4 + 75 de §5) contra los dos árboles:

- 85 filas reproducen exactamente sobre la **CANDIDATA**;
- la fila 11 está **AUSENTE de la candidata** y presente en el gate — **y la fila lo dice**;
- la fila 1 (`00-INDICE.md`, 245 líneas, `4d2077f3…`) es la de la **CANDIDATA**; sobre el árbol del gate difiere (247 líneas, `063c62a5…`), y **el sobre publica esa diferencia**.

Derivé además los conjuntos: sobre la candidata, `universo − manifiesto = ∅` y el único sobrante del manifiesto es la fila 11 declarada; sobre el gate, el único hueco es **el propio manifiesto `B`**, que §6 declara como exención de PUNTO FIJO de `DD-19`. **La aritmética de §6 la derivé y cierra**: 10 filas / 29348 líneas + 75 filas / 62762 líneas = **85 / 92110**.

**OBLIGACIÓN 4 — la superficie de diferencia REAL entre los árboles.** El sobre lista 3 rutas en que difieren los UNIVERSOS y advierte que no son las mismas que las de los ÁRBOLES. Ejecuté `git diff --name-only`: los árboles difieren en **6** rutas — las 3 del universo **más** los tres ficheros de evidencia. **El sobre no miente: advierte de esto exactamente y §6 del manifiesto las nombra.** Sin hallazgo.

**OBLIGACIÓN 5 — no fiarse de `git status`, comprobar emisor y derivador en los dos commits.** Recalculados con `git show <commit>:<ruta>`: emisor `f915a840…30d20a` en los dos, derivador `fc8adef3…0fd0be` en los dos — coinciden. Hago constar que **esto no prueba que el emisor y el derivador que CORRIERON sean los publicados** (`Z-11`).

**OBLIGACIÓN 6 — digest de la sede canónica y contraste contra toda sede derivada.**

| | recalculado | ¿coincide? |
|---|---|---|
| sede entera | `ebfef288de70d1ec6d58306720440b9a4c706197cc66f99b92e54a147678fc9a` | **SÍ** |
| `O17` (85 líneas) | `0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125` | **SÍ** |
| `O18` (111) | `ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353` | **SÍ** |
| `O19` (81) | `d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632` | **SÍ** |
| `O20` (110) | `ebc5b2cd159336c5be5b7557d624082fbe15a7b7cff7ee912dbebf4e354612af` | **SÍ** |
| `O21` (112) | `e9dd2fb9e780e505ede8334a1795a102d85a1187de946bf6d2aa0799e7b20810` | **SÍ** |

Los dos commits publican la misma sede byte a byte. Contrasté las paráfrasis: **encuentro UNA que amplía** (`W2-08`).

**OBLIGACIÓN 7 — el TEXTO ÍNTEGRO de `O19` viaja en el sobre, y su `sha256sum` reproduce.** **CUMPLIDA, y es lo primero que hice.** Recorté el bloque entre las dos líneas de guiones, retiré la sangría de dos espacios, y le pasé `sha256sum`: **81 líneas**, `d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632`. **Reproduce exactamente el digest publicado a su lado.** Lo que recibí es **el TEXTO, no un resumen**. **No lo di por bueno leyéndolo del árbol auditado.** **`C-20` está materialmente cerrado en lo que a mí me consta**, y así lo hago constar a favor.

**VEREDICTO SOBRE LA VALIDEZ: el gate es VÁLIDO en todo lo que puedo medir.** Las siete obligaciones se cumplen.

## 2 · DECLARACIÓN DE COBERTURA REAL — CONTRA MI PROPIO INTERÉS

Todas las lecturas las hice **del commit candidato `f232d1a`**, no del directorio de trabajo. **Hago constar que el árbol de trabajo está posicionado en el commit del GATE (`2e31452`)**, y que por tanto `00-INDICE.md` en disco es la versión del gate (247 líneas), no la que este gate juzga (245).

SHA-256 recalculados por mí, uno a uno, y **los seis coinciden con el manifiesto §4**.

| # | ruta | líneas | SHA-256 recalculado | qué leí ÍNTEGRO | qué NO leí |
|---|---|---|---|---|---|
| 1 | `00-INDICE.md` | 245 | `4d2077f3…646fc910` | **L1–L245, las 245** | — pero **con truncamiento**: ver nota (a) |
| 2 | `11-ARQUITECTURA-INTEGRADA.md` `L5201-L12071` | 12071 | `1303d98c…1aaf9859` | §15.4 `L9261-9300` · §20 entero `L11883-12071` · `C-L.5` `L11692-11882` · §18 `L10849-10945` · §17 `L11104-11200` · §19 `L11026-11060` · §11.6 parcial `L8341-8700` · mapa de secciones de todo el rango | **NO LEÍ ÍNTEGRO EL RANGO.** Sin abrir: `L5216-8340` casi entero, `L8701-9260`, `L9301-9780`, §16 `L9781-11025` salvo `PN-19`, `L11201-11691` |
| 3 | `30-GATE-…-FINAL-F4C.md` | 3084 | `712058b2…01aee6503` | §3 `L2330-2420` · §9 `L2953-3050` · mapa de encabezados entero | **NO ÍNTEGRO.** Sin abrir: los dos dictámenes `U1` y `U2` casi enteros (`L143-1769`) y la adjudicación `L1770-2329`, `L2421-2952` |
| 4 | `CHECKPOINT-ADS-NEXT.md` | 5691 | `d9cf16af…1ff7b02f4` | cabecera `L1-60` · bloque reanudable parcial · `L960-1310` · `L2189-2300` · `L2678-2793` · matriz `L4170-4340` | **NO ÍNTEGRO.** Sin abrir: `L61-959`, `L1311-1553`, `L1576-2188`, `L2301-2677`, `L2794-4169`, `L4341-5691` |
| 5 | `DECISIONES-Y-CONTRADICCIONES.md` | 1449 | `4fd82ebe…1f4466645` | `L491-563` · `L1242-1345` · filas `D108`/`D109`/`D110` enteras · mapa de encabezados entero | **NO ÍNTEGRO.** Sin abrir: `L1-490`, `L564-1241`, `L1346-1449` |
| 6 | `ADS-OWNER-RESOLUCIONES.md` | 559 | `ebfef288…7678fc9a` | **L1–L559, ÍNTEGRO.** `L260-337` (`O19`) verificado por digest desde el sobre | **nada** |

**(a) Nota contra mi interés sobre `00-INDICE.md`:** abrí las 245 líneas, pero mi volcado truncó las filas largas de tabla a 260 caracteres. Leí en su longitud completa `L35`, `L60`, `L85`, `L88`, `L89`, `L90`, `L104`, `L106`, `L107`. **Las demás filas largas las leí truncadas**, y un defecto escondido en su cola no lo habría visto.

**LA RESTA, dicha sin adorno: `ASIGNADO − LEÍDO ≠ ∅` PARA MI LOTE.** De las seis fuentes asignadas he leído íntegra **UNA** — la sede canónica del Owner. Las otras cinco las he leído **por secciones dirigidas y por barridos mecánicos sobre el fichero completo**, que no es lo mismo que lectura íntegra y no lo presento como tal.

**Bajo la regla de cierre de `C-L.5` mi propia cobertura EXCLUYE la suficiencia**, con independencia de los hallazgos. Lo digo yo, contra mí, antes de que nadie lo mida.

**¿Entré en algo que no me tocaba?** **SÍ, y lo declaro.** Mi rango de doc 11 es `L5201-L12071`, pero leí `L432-450` (§2.1) y `L4129`, `L5133-5156`: esos tramos son de `W1`. Leí también fragmentos de `comprobar-correccion-gate-de-cierre.py` (`L861-867`, `L1828-1829`), `emitir-sobre-de-ancla.py` y `derivar-universo-obligatorio.py`, que son de `W1`, y del documento 29 y del manifiesto del gate anterior. **No los leí íntegros ni pretendo agotarlos**, y no fundo ningún hallazgo en una lectura parcial de material ajeno.

## 3 · HALLAZGOS

| id | sev. | clase | sede · fichero:línea | qué dice | por qué está mal | qué lo probaría |
|---|---|---|---|---|---|---|
| **`W2-01`** | **GRAVE** | **A** | `docs/evolucion/CHECKPOINT-ADS-NEXT.md`:**1013-1014** | Regla 7 de `regla_de_reanclaje` publica el comando que deriva el conjunto de campos del bloque, y dice «**el conjunto de campos se DERIVA del propio bloque en vez de escribirse**» | **El comando devuelve CERO líneas.** El guarda `!f` selecciona lo que está **FUERA** de las vallas de código, y el bloque reanudable vive **DENTRO** de una valla ```` ```text ```` (`L972`–`L2793`). El instrumento que esta tanda escribió **para cerrar `C-L.7` por CLASE en vez de por instancia** deriva el conjunto vacío: quien lo ejecute concluye que no hay campos que barrer y da la clase por cerrada sin haber mirado ninguno. Es un **falso verde escrito dentro de la garantía** | El comando de la regla 7 seguido de `wc -l` → **0**. Con `f` en vez de `!f` → **14** campos |
| **`W2-02`** | MEDIO | **A** | `CHECKPOINT-ADS-NEXT.md`:**1285** · y `11-ARQUITECTURA-INTEGRADA.md`:**9720** | Campo **VIGENTE** `last_meaningful_event`: «ningún gate le elevó pregunta: **los NUEVE** declararon que ninguna decisión volvía a él». Doc 11 §15.8: «ninguno de **los nueve** gates le elevó esta pregunta» | Es un **cardinal vivo escrito a mano dentro del bloque**, contra su regla 1 y su regla 2. **Y es literalmente una sustitución**: el campo anterior decía «los **ocho**», y esta tanda escribió «los **NUEVE**» encima, que es «sustituir un número caducado por otro» — lo que `J-07` prohíbe. Caduca en el décimo gate, y ya se propagó a una segunda sede | `git show 7aeed6a:…CHECKPOINT… \| grep 'declararon que ninguna'` → «los ocho»; `sed -n '1285p'` sobre la candidata → «los NUEVE» |
| **`W2-03`** | MEDIO | **A** | `CHECKPOINT-ADS-NEXT.md`:**2734** | Campo `falta_para_cerrar_la_capa`, tras declarar «**No se sustituye por otro** … se retira y se remite. El censo se deriva:», la línea siguiente fusiona el comando `ls docs/evolucion/[0-9][0-9]-*.md \| sort` con la prosa que le seguía | **Es un FRAGMENTO de una retirada anterior que se quedó sin su salto de línea.** El comando así publicado **no es ejecutable**. Es exactamente la pregunta 2 de la regla 7, **dentro del párrafo que presume de haber retirado bien un cardinal**. Lo introdujo el remedio de `C-16` en `7aeed6a` y **esta tanda, que dice barrer la clase, no lo vio** | `sed -n '2734p' … \| cat -A`; `git blame -L 2734,2734` → `7aeed6a` |
| **`W2-04`** | MEDIO | **A** | `CHECKPOINT-ADS-NEXT.md`:**2715-2735** | Viñeta sin rótulo alguno, dentro del bloque declarado VIGENTE: «F4c ESTÁ ABIERTA, **y ahora** con el GATE FINAL INDEPENDIENTE ejecutado y devuelto: INSUFICIENTE PARA F5 … **CUATRO BLOQUEANTES, SEIS GRAVES**» | El GATE FINAL INDEPENDIENTE es el **documento 16**: catorce documentos atrás. La viñeta lo describe **en presente («ahora»), sin rótulo histórico**, y **copia un recuento** que la regla 2 remite al documento del gate. **`C-15` del octavo gate es literalmente esto**, y su remedio rotuló **una sola viñeta**, dejando la siguiente intacta: **instancia cerrada, clase abierta**. Y el alcance del rótulo de `L2686` **no está normado** | Las únicas apariciones de `HISTÓRICO` entre `L2678` y `L2793` son `L2686` y `L2736`; entre ellas hay cinco viñetas más, y `L2715` reabre en presente. `git blame -L 2715,2715` → `7c7856c`, 2026-08-28 |
| **`W2-05`** | MEDIO | **A** | `docs/evolucion/00-INDICE.md`:**35** (candidata **y** árbol del gate) | «`ADS-OWNER-RESOLUCIONES.md` … **Contiene `O17`, `O18` —texto amplio RATIFICADO— y `O19`**, con su texto íntegro y no en resumen» | **La sede publica CINCO**: `O17 O18 O19 O20 O21`. Es una **enumeración viva escrita al lado de una sede que crece**, y es **exactamente la clase de `H-10`** —el mismo defecto, la misma sede citada, el mismo verbo «contiene»— que este gate adjudicó y esta tanda cerró **en `owner_captado` y en ningún otro sitio**. `O20` y `O21` se registraron el 2026-09-01; **ninguna de las dos tandas tocó esta fila**. El índice sabe la regla y la aplica cuatro veces en el mismo fichero (`L60`, `L118-119`, `L167-169`, `L197-199`) — aquí no. **No consta registrado en el documento 30, ni en el checkpoint, ni en el documento 11**: es un hallazgo vivo y nuevo | `grep -oE '^# `O[0-9]+`' docs/owner/ADS-OWNER-RESOLUCIONES.md` → **5**, contra los tres que la fila nombra |
| **`W2-06`** | MEDIO | **A** | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`:**491** (epígrafe) y **544**, **545**, **546** (filas) | El único encabezado que cubre las filas `D108`, `D109` y `D110` es `### D107 · la propagación de O17`, cuyo preámbulo describe **otro origen**: el documento 22, adjudicador `R`, 69 hallazgos | **Es la recurrencia literal de `S-19`.** `S-19` se cerró **moviendo `D107`** y **no estableciendo la regla**: `D108`, `D109` y `D110` se archivaron después en esa misma estructura. Hoy **§15.8 del documento 11 sí da bloque propio a las cuatro** —es el remedio de `H-04`, aplicado— y **el registro de decisiones no da ninguno a tres de ellas**. La asimetría que `S-19` denunció **sigue exactamente igual, tres veces** | `grep -n '^### '` → el último de la sección 1 es `491: ### D107`, y la sección 2 empieza en `550`. Contra §15.8, que sí tiene bloques propios para las cuatro |
| **`W2-07`** | MENOR | **A** | `00-INDICE.md`:**147-165** **sobre el ÁRBOL DEL GATE `2e31452`** | La regla del propio índice (`L139-145`): «Todo documento que `C-L.5` obligue a publicar —**manifiesto de asignación**…— **se enlaza desde la lista de abajo en el MISMO commit que lo crea**» | El commit del gate publica **dos** manifiestos de asignación y **no añade ninguno a la LISTA**: los enlaza sólo desde su fila del registro de pasadas. **Eso es lo que `EE-03` acotó.** El `diff` que el propio índice publica como prueba **sale NO VACÍO** sobre el árbol del gate. Por el precedente `S-18`/`T-14`, es imputable **al GATE y no a la candidata**, y `T147` sigue en verde — pero **la regla escrita se incumple, y la incumple el aparato de este mismo gate** | El comando de `L182-187` sobre `2e31452` devuelve `18,19d17`; sobre `f232d1a` sale **vacío** |
| **`W2-08`** | LEVE | **A** | `CHECKPOINT-ADS-NEXT.md`:**2208-2209** | `owner_captado`: «**NINGUNA de ellas autoriza iniciar F5, F6 ni PesquerApp, y cada una lo declara en su propio texto**» | **Una paráfrasis que amplía el texto canónico.** `O17`, `O18`, `O20` y `O21` sí declaran las tres en su `ALCANCE`. **`O19` no**: su `ALCANCE` dice «**NO autoriza iniciar `F5`**» y **nada sobre `F6` ni PesquerApp**. La afirmación universal «cada una lo declara en su propio texto» es falsa para una de las cinco. La versión correcta ya está dos renglones más abajo (`L2238`) | `awk` sobre `O19` en la sede + `grep -n 'F6\|PesquerApp'` → sin resultados |
| **`W2-09`** | LEVE | **A** | `CHECKPOINT-ADS-NEXT.md`:**974-975**, y **1108** · **1148** · **1173** · **1190** | `actualizado:` (campo VIGENTE, reescrito por esta tanda): «reanclado por la TANDA DE `O21` y de **los 16** del GATE ARQUITECTÓNICO FINAL». En `metodo_anterior`: «los **treinta y seis** hallazgos», «CERTIFICADA por **CUARTA** vez consecutiva», «**ocho** agentes», «**diez** agentes» | Recuentos de hallazgos copiados **dentro** del bloque, contra su regla 1 y su regla 2. No caducan, porque los documentos de gate son inmutables — **pero la regla del bloque es categórica y esta misma tanda la honra literalmente a cuatro líneas de distancia** (`L1067-1068`). Que `actualizado` —campo vigente, recién escrito— copie «los 16» mide que **el barrido de clase no se hizo campo a campo** | `sed -n '974,975p'` y `sed -n '1108p'`; contra `regla_de_reanclaje` reglas 1 y 2, `L984-991` |

**No he encontrado nada, y lo digo expresamente, en los puntos 1, 2, 9, 10, 11, 12 y 14** de la lista de catorce, y en `O21` contrastada contra sus proyecciones (punto 3), salvo lo ya dicho en `W2-05` y `W2-08`.

## 4 · LOS CATORCE PUNTOS, UNO A UNO

**1 · Los DIECISÉIS hallazgos `H-01`…`H-16`.** Contrasté el remedio escrito en §9 del documento 30 contra el árbol de hoy, **uno a uno**. **Los dieciséis están APLICADOS, no sólo declarados.** Lo más significativo: `H-01` — **el sobre transporta materialmente el texto de `O19`, 81 líneas, y su digest reproduce**; fila `C-20`: `CORREGIDO_EN_F4c`, propietario `PLT`, fase `F4c`. **`H-02`** — §18 gana el nodo 9 con la arista `9 → 8` (`11-ARQ:10917-10926`). **`H-03`** — `O20` tiene fila en §15.4 (`11-ARQ:9287`), y `O21` también. **`H-04`** — §15.8 abre bloque propio para `D109` **y** `D110`. **`H-05`** — nace `V6-19` (`11-ARQ:11943`). **`H-06`** — §20.5 retira el cardinal y remite al conjunto derivado, **declarando la deuda de inventario con propietario `VER` y fase `F6`**. **`H-07`** — §20.4 declara la dependencia con sede, fase `F5`, propietario Owner y condición exacta. **`H-08`** — el campo 17 dice «**TODAS las que la SEDE contenga**». **`H-09`** y **`H-10`** — los dos fragmentos de `based_on` retirados; `owner_captado` deriva. **`H-14`**, **`H-15`** (barrido del marcador → **0**), **`H-16`** — aplicados. **Nada suavizado, nada escondido, ninguna fase cambiada para ablandar.**

**2 · Las OCHO CAUSAS INDEPENDIENTES — ¿por CLASE o por INSTANCIA?** **Ésta es la pregunta que este expediente falla, y vuelve a fallarla.** Cinco causas se cerraron por clase de verdad: `H-08` sustituyó el enumerado por «todas las que la sede contenga»; `H-06` y `H-14` retiraron cardinales **sin sustituirlos**; `H-07` normó los tres requisitos de una dependencia bloqueada; `H-05` creó una regla general de sede única de fórmulas. **Tres se cerraron por INSTANCIA:** la clase `J-07`/`H-10` se cerró en `owner_captado` y **se dejó viva en `00-INDICE.md:35`** (`W2-05`) y **se reintrodujo** en `last_meaningful_event` (`W2-02`) y en `actualizado` (`W2-09`); la clase `C-15` se cerró en una viñeta y **se dejó viva en la siguiente** (`W2-04`); la clase `S-19` se cerró para `D107` y **está viva para `D108`, `D109` y `D110`** (`W2-06`). Y por encima de todas: **la clase `C-L.7` misma se declaró barrida con un instrumento que no funciona** (`W2-01`).

**3 · `O21` contra todas sus proyecciones.** Leí el texto **íntegro** en la sede (`L448-559`) y lo contrasté con `DECISIONES` entrada `O21` (`L1301-1341`) y fila `D110` (`L546`), `11-ARQ` §15.4 (`L9288`) y §15.8, `00-INDICE.md:107` y el `CHECKPOINT`. **Ninguna proyección amplía ni debilita `O21`.** Los diez puntos están, la tupla de seis elementos está, la prohibición de negarse está, y todas las sedes repiten que **`O21` no declara suficiente a `F4c`, no corrige los dieciséis y no autoriza `F5`, `F6` ni PesquerApp**. **APPEND-ONLY: COMPROBADO, no creído.** `git log --diff-filter=A` da un solo commit de creación (`1d3b5d4`). Los dos commits posteriores que tocan la sede son `7aeed6a` (`@@ -334,0 +335,110 @@`) y `07a6975` (`@@ -444,0 +445,115 @@`): **cero borrados, cero modificaciones de líneas anteriores, apéndice puro al final en los dos casos.**

**4 · `C-L.7` COMO CLASE COMPLETA.** Ver §5. **Es donde este expediente vuelve a fallar.**

**5 · `C-L.5` por sus SEIS condiciones sobre ESTE gate.** No adjudico; **mido**: (1) corpus obligatorio **DEFINIDO** → **SATISFECHA**, lo derivé yo: 85/92110 y 87/92699. (2) manifiesto previo de **ASIGNACIÓN** publicado → **SATISFECHA**, manifiesto `B` commiteado a las 13:08:12, SHA verificado, y el sobre emitido a las 13:08:33 — **los dos antes de que yo existiera**. (3) manifiestos posteriores de **LECTURA** publicados → **PARCIAL**; el mío va en §2 con ruta, líneas, SHA-256 recalculado y tramos no abiertos. (4) `OBLIGATORIO − ASIGNADO = ∅` → **SATISFECHA, derivada por mí sobre los dos árboles**; candidata ∅, gate sólo el propio manifiesto `B` con su exención declarada. (5) `ASIGNADO − LEÍDO = ∅` → **NO SATISFECHA PARA MI LOTE**, por mi propia declaración de §2. (6) revisores **INDEPENDIENTES** que declaran **contra su propio interés** → **SATISFECHA por mi parte**. **Su estado en la CLASIFICACIÓN VIGENTE es `ABIERTA`** (`chk:2383`, `2424`), y el manifiesto §1 lo declara igual. **No hay suavizado.**

**6 · CARDINALES VIVOS (`J-07`).** Barrí toda cifra escrita al lado de su enumeración en mis fuentes y **ejecuté el comando que cada sede publica**. Reproducen: PN vigentes **17**, bloques de §15.8 **20**, versiones históricas del checkpoint **12**, `V6` en §20.1 **19**, `X-S` **11**, `X-O` **13**, las **TRECE** condicionales de §5.18, los **CATORCE** campos de §8.0, y «**NUEVE filas y los externos son SIETE**» de §17 — **este último lo verifiqué expresamente porque un `grep` ingenuo da ocho, y hacer de eso un hallazgo habría sido inventarlo**. **Caducados o mal remitidos: `W2-05`, `W2-02`, `W2-09`.** Y sobre la pregunta expresa del encargo: **SÍ, esta tanda sustituyó un número caducado por otro** — «los ocho» → «los NUEVE» en el campo vigente `last_meaningful_event`, y lo propagó a §15.8.

**7 · La MATRIZ DE LOS 22, y la clasificación semántica.** **CIERRA, y la derivé con los tres comandos que ella misma publica.** 22 filas, `C-00`…`C-21` **exactamente una vez cada uno**. Reparto derivado: **15 `CORREGIDO_EN_F4c` · 7 `CONTRATO_COMPLETO_PARA_F6`**. **Ninguno declarado SUPERADO.** Los que bloquean `F6` **y** PesquerApp: **7**. La cobertura contra el documento 29 **sale vacía en las dos direcciones**. Su sección de clasificación semántica (`chk:4306-4315`) **es coherente con §20.3** (`11-ARQ:11959-12001`). **Sin hallazgo.**

**8 · §15.4 y §15.8 — la cobertura, derivada y no creída.** §15.4 tiene **una fila por resolución**: `O7`…`O21`, quince. Derivé la resta en las dos direcciones y **sale vacía**. §15.8 tiene **un bloque por propagación**, `D107`–`D110` incluidos. **Cierra.** (Que el registro histórico no dé epígrafe a tres de ellas es `W2-06`.)

**9 · Ninguna deuda de `F6` presentada como implementada.** **No encuentro ninguna.** §20 lo dice cuatro veces; §20.3 «**ninguno de los tres** puede presentarse como implementado»; §20.2 y §20.0; la matriz «`CONTRATO_COMPLETO_PARA_F6` **NO significa** corregido, ni implementado, ni ejecutado, ni certificado». El manifiesto §9 lo repite contra su propio interés tras publicar 38/38.

**10 · PesquerApp SIGUE BLOQUEADA, y por cuántas sedes.** **Sí, y por OCHO sedes que lo dicen expresamente.** Las tres fórmulas de `O20` §8 se reproducen literalmente. **No veo por dónde podría iniciarse antes de certificar `F6`.**

**11 · Ausencia de arquitectura oculta.** **No encuentro ninguna.** El único candidato real es `V6-16`, y **no está oculto**: §20.4 lo declara con sede, fase `F5`, propietario y condición de desbloqueo en tres puntos. Los diecinueve contratos llevan clasificación en todas sus filas, y **18 `CONSTRUIBLE` + 1 `BLOQUEADO` = 19**, sin suma.

**12 · Ausencia de regresiones.** **No encuentro ninguna.** Los ocho puntos de `O20` siguen escritos; `M-04` no se cierra; `C-L.7` sigue `NO CERRADA`; `C-L.5` sigue `ABIERTA`; los remedios anteriores que verifiqué siguen aplicados. La única reintroducción es la de `W2-02`, y es un cardinal, no una regresión de regla.

**13 · El ÍNDICE.** Sobre la **candidata**, su LISTA cubre `verificacion/` **entero**: el `diff` sale vacío. Sobre el **árbol del gate**, no (`W2-07`). Verifiqué `L106` contra §8 del documento 30 y `L107` contra `O21` en la sede, sin ampliación. **La excepción es `L35`** (`W2-05`).

**14 · TRAZABILIDAD hasta PesquerApp.** Seguí la cadena entera y **no consigo romperla**: `O18` → `O20` §3 y §8 → `D109`(vi) → §20.1 → §20.2 y §20.4 → §18 nodo 9 → arista 9→8 → paso 8 PesquerApp → §8.2 FASE 0. **Cada eslabón tiene sede, propietario, fase y condición de cierre.** El punto que antes rompía la cadena —§18 sin el nodo del verificador— es `H-02`, **y está reparado**. Además la cadena está **redundada**.

## 5 · EL BARRIDO DE `C-L.7` — LA TABLA CAMPO A CAMPO

**El conjunto de campos NO lo derivé con el comando de la regla 7, porque ese comando devuelve el conjunto vacío (`W2-01`).** Lo derivé invirtiendo su guarda —`f` en lugar de `!f`— y acotándolo al bloque vigente `L972`–`L2793`. **Son CATORCE nombres de campo distintos.** Los recorrí **todos**.

| # | campo | línea | ¿copia recuento, ordinal, estado o enumeración que otra sede publica? | ¿queda FRAGMENTO sin su frase? | ¿lo histórico está ROTULADO? |
|---|---|---|---|---|---|
| 1 | `actualizado` | 974 | **SÍ** — «**los 16** del GATE ARQUITECTÓNICO FINAL» · `W2-09` | no | n/a (vigente) |
| 2 | `regla_de_reanclaje` | 976 | no | no | n/a — **su regla 7 publica un comando que devuelve CERO · `W2-01`** |
| 3 | `metodo` | 1018 | **no** — ordinal retirado, comando de `C-09` retirado, estado de las `C-L` remitido | no | n/a (vigente) |
| 4 | `metodo_anterior` ×15 | 1054…1205 | **SÍ, parcialmente** — «treinta y seis», «CUARTA», «ocho agentes», «diez agentes» · `W2-09` | no | **SÍ** — el nombre del campo es el rótulo |
| 5 | `based_on` | 1207 | **no** — base retirada, documentos remitidos, **y las resoluciones se DERIVAN** (L1233) | **no** — los dos fragmentos de `H-09` **están retirados y la retirada va declarada** (L1213-1221). Verificado | n/a |
| 6 | `rama_de_trabajo` | 1265 | **no** — remitidas a Git | no | **SÍ** — L1274-1277 |
| 7 | `freshness` | 1281 | no | no | **SÍ** |
| 8 | `last_meaningful_event` | 1284 | **SÍ** — «**los NUEVE**», **sustituyendo al «ocho» anterior**, en el campo VIGENTE · `W2-02` | no | n/a (vigente) |
| 9 | `last_meaningful_event_anterior` ×15 | 1307…1551 | **SÍ** — L1308 «los **ocho** declararon» | no | **SÍ** — el nombre del campo |
| 10 | `procedencia_de_la_critica` | 1554 | **no** | no | n/a |
| 11 | `owner_captado` | 2189 | **no** — `H-10` aplicado: retira «O17, O18 y O19» y **deriva** (L2197) | no | **SÍ** — L2210 · pero L2208-2209 **amplía** `O19` · `W2-08` |
| 12 | `pregunta_pendiente` | 2226 | **no** — última resolución retirada y remitida, censo de PN remitido | no | **SÍ** — y la frase **no se sustituye por otra cifra: se retira** |
| 13 | `siguiente` | 2258 | **no** — retirado y remitido | no | **SÍ** — L2269 |
| 14 | `falta_para_cerrar_la_capa` | 2678 | **SÍ** — L2717 «**CUATRO BLOQUEANTES, SEIS GRAVES**» | **SÍ** — L2734, comando inejecutable · `W2-03` | **NO** — L2715-2735 en presente **sin rótulo** · `W2-04` |

**RESULTADO DEL BARRIDO: `C-L.7` NO ESTÁ CERRADA COMO CLASE.** Nueve de los catorce campos pasan las tres preguntas limpiamente, y hay que decir a favor que **eso es mucho más de lo que ningún gate anterior había medido**: `based_on`, `pregunta_pendiente`, `siguiente` y `rama_de_trabajo` están hoy retirados y remitidos con disciplina real, y `H-09` y `H-10` están cerrados de verdad en su sede. **Pero cuatro campos fallan**, **el último falla las tres preguntas a la vez**, y **la garantía que la tanda escribió DENTRO del bloque para que el barrido no dependiera de que alguien se acordase es un comando que no barre nada.**

## 6 · MI RECOMENDACIÓN

# INSUFICIENTE PARA F5

**La razón, en una línea:** `C-L.7` se declara barrida **como clase** con un comando que devuelve el conjunto vacío (`W2-01`), y el barrido real que ese comando debía hacer destapa cuatro campos que siguen copiando cardinales, un fragmento que corrompe un comando publicado y una viñeta histórica sin rotular dentro del bloque vigente — más tres clases (`J-07`/`H-10`, `C-15`, `S-19`) cerradas por instancia y vivas en `00-INDICE.md:35`, en `chk:2715` y en las tres filas `D108`-`D110` del registro.

**Y con independencia de los hallazgos, mi propia cobertura ya excluye la suficiencia:** cinco de mis seis fuentes asignadas no están leídas íntegras. Lo declaro yo, contra mí.

**Sobre la COBERTURA (`C-L.5`) no me pronuncio: `O21` §3 se la asigna al adjudicador**, y le hago constar que de las seis condiciones **verifiqué satisfechas la 1, la 2 y la 4 por derivación propia**, que cumplo la 6, y que **la 5 falla por mi lote y lo digo yo**. `O21` §8 le prohíbe negarse a certificar por haber encontrado otros defectos, y `O21` §2 le prohíbe deducir una declaración de la otra: **mi recomendación de insuficiencia no es, ni debe leerse como, una razón para no certificar cobertura.**

**Lo que consta a favor, porque es verdad:** el sobre es impecable en las siete obligaciones y **`C-20` está materialmente cerrado**; la sede canónica es **append-only comprobado, no declarado**; los dieciséis remedios del documento 30 **están aplicados uno a uno**; la matriz de los 22 **cierra en las dos direcciones sin un solo `SUPERADO`**; §15.4 y §15.8 **cierran su cobertura derivada**; ninguna deuda de `F6` se presenta como implementada; y **PesquerApp está bloqueada por ocho sedes y por una cadena que no consigo romper**. Ninguno de mis hallazgos es «el verificador de `F6` no está implementado»: **los nueve son defectos documentales de `F4c`**, y ninguno es clase `B` — **nada vuelve al Owner.**

**Yo recomiendo; adjudica otro.** No he corregido nada.

## 5 · ADJUDICACIÓN ÍNTEGRA DE `WA`

**Entorno declarado.** No he escrito nada de este corpus, no he aplicado ninguna corrección, no he participado en ningún gate anterior. **No he modificado ni un byte**: `git status --porcelain` vacío al abrir y al cerrar, `git rev-parse HEAD` = `2e31452cf8ed80e757d4bb23c5afdc1ff4819556`, cero ediciones y cero commits; el `reflog` no registra ninguna operación mía. Leí los dos dictámenes enteros **antes** de tocar el árbol. Todo lo que juzgo lo leí **del commit** con `git show`.

Anoto una corrección al margen: el snapshot de apertura de mi encargo decía `M docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` y rama `fix/f4c-perimetro-por-naturaleza-20260831`. **Los dos son datos caducados del prompt, no del árbol**: `git diff --stat` sale vacío y la rama real es `fix/f4c-propiedad-de-admision-20260831`, cuyo `checkout` está en `HEAD@{10}`, **anterior a los tres commits del gate**. Es la misma discrepancia que `W1` declaró contra su interés. **Nadie movió nada.**

## 1 · VALIDEZ DEL GATE — LAS SIETE OBLIGACIONES, REPRODUCIDAS POR MÍ

**OBLIGACIÓN 1 · recalcular los DOS digest antes de leer nada. CUMPLIDA.** Ejecuté las dos recetas íntegras, cada árbol con **su propio derivador extraído de su propio commit**:

| árbol | fuentes | líneas | digest recalculado | ¿= sobre? |
|---|---|---|---|---|
| CANDIDATA `f232d1a` | **85** | **92110** | `ca0cacc0cbe1328dbbf7a962192d1fd616aaa0d3f0fdba272492fd8f88f22ba5` | **SÍ** |
| GATE `2e31452` | **87** | **92699** | `a50329e13f3e9cd9f10fa7d9d7701d03dc5cf81369a90cd2940597ac2e0462a5` | **SÍ** |

Las seis cifras derivadas, ninguna leída. **No hay invalidez por esta vía.**

**OBLIGACIÓN 2 · el manifiesto, EN EL COMMIT DEL GATE. CUMPLIDA.** `git show 2e31452:…B.md | sha256sum` → `4a27b5ef2146753afa5ab8c1c6fc95b195d97e493a28af642ebf97c5ef5090f8`, idéntico al sobre. Leído íntegro del commit. **Son 303 líneas** —el fichero termina en salto de línea, verificado con `xxd`—. `W2` publica 303 y acierta; **`W1` publica 304 y se equivoca**. Es inmaterial y no toca ningún campo del sobre, pero lo hago constar porque adjudico reproducciones, no impresiones.

**OBLIGACIÓN 3 · cada fila contra SU árbol, y la del derivador primero. CUMPLIDA**, mecánicamente sobre las **86 filas** (11 de §4 + 75 de §5), contrastando SHA-256 **y** recuento de líneas contra los DOS commits.

- **La fila del derivador —§4 fila 6, 857 líneas, `fc8adef3…0fd0be`— es EXACTA en los dos commits.** No reincide `U-02`/`X-06`, por sexta vez.
- **Sólo dos filas no casan contra los dos árboles a la vez, y las dos son correctas:** `00-INDICE.md` casa con la **candidata** (`4d2077f3…`/245) y no con el gate (`063c62a5…`/247) — **el sobre publica exactamente esa diferencia**; fila 11 (el manifiesto anterior) está **AUSENTE de la candidata** y presente en el gate — **y la propia celda lo declara**.
- **Cero discrepancias no declaradas.** Los dos revisores lo miden igual que yo.

**OBLIGACIÓN 4 · las dos superficies de diferencia no son la misma. CUMPLIDA.** `git diff --name-only f232d1a 2e31452` → **6 rutas**; el sobre publica **3** de universo. Las otras tres son los ficheros de evidencia reejecutada, y el §6 del manifiesto las declara fuera del universo con su razón. **El sobre advierte de esto expresamente en su obligación 4. Ninguna sede esconde nada.**

**OBLIGACIÓN 5 · qué prueba y qué no el `porcelain` vacío. CUMPLIDA.** Emisor `f915a840…30d20a` y derivador `fc8adef3…0fd0be` **idénticos en los dos commits y en el árbol de trabajo**. Asumo la limitación que el sobre declara: prueba que los publicados son los de los commits, **no que sean los que se EJECUTARON** (`Z-11`).

**OBLIGACIÓN 6 · la sede canónica y toda paráfrasis. CUMPLIDA.** Sede entera y las cinco resoluciones, recalculadas por mí sobre los **dos** commits:

| | recalculado | líneas | ¿= sobre, en los dos commits? |
|---|---|---|---|
| sede entera | `ebfef288…7678fc9a` | 559 | **SÍ** |
| `O17` | `0cc5b9b5…4e6125` | 85 | **SÍ** |
| `O18` | `ab9d9447…6ed0353` | 111 | **SÍ** |
| `O19` | `d86a9455…fddf632` | 81 | **SÍ** |
| `O20` | `ebc5b2cd…4612af` | 110 | **SÍ** |
| `O21` | `e9dd2fb9…7b20810` | 112 | **SÍ** |

Paráfrasis que amplían el texto canónico: **encuentro TRES sedes con una misma ampliación** (`W1-07`) y **una afirmación universal falsa** (`W2-08`).

**OBLIGACIÓN 7 · el TEXTO ÍNTEGRO de `O19` viaja en el sobre. CUMPLIDA, y es lo mejor de esta tanda.** Recorté el bloque entre las dos líneas de guiones (sobre L156-236), retiré la sangría de dos espacios y lo comparé **byte a byte** contra el bloque extraído del commit auditado:

    81 líneas · d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632  (sobre)
    81 líneas · d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632  (f232d1a)
    diff → SIN SALIDA. IDÉNTICOS.

**No es un resumen: son las 81 de 81 líneas.** El gate anterior midió 2 de 62 líneas sustantivas. Comprobé además la receta **sin ejecutar el emisor**.

### ¿Divergen los sobres de los dos revisores?

**NO.** Contrasté campo a campo lo que cada uno publica del sobre —digests de los dos universos, fuentes, líneas, SHA del manifiesto, SHA del emisor y del derivador en los dos commits, huella de la sede y las cinco de resolución, las 3 rutas de universo frente a las 6 de árbol, `ASIGNACIONES 16`, digest y recuento del bloque de `O19`—: **coinciden entre sí y con el fichero.** Leyeron el mismo sobre y no lo transcribieron a mano.

### EL GATE ES VÁLIDO

Ninguna de las siete obligaciones falla, los dos sobres coinciden, y la sede canónica coincide con la huella recibida. **VÁLIDO por sexta vez consecutiva.**

### UN DEFECTO DEL DICTAMEN DE `W1` QUE TENGO QUE SEÑALAR, PORQUE ES UNA REPRODUCCIÓN FALSA

`W1`, en su obligación 6, escribe que «`O20` conserva su texto: su digest sobre `f232d1a` da `c3804cde…1906f3`, exactamente el que el gate anterior ancló».

**Es falso, y se contradice con su propia frase anterior.** Medido por mí: el bloque `O20` sobre `f232d1a` da `ebc5b2cd…4612af` (110 líneas) y sobre `7aeed6a` da `c3804cde…1906f3` (107 líneas). `c3804cde` es el digest que el documento **30** ancló sobre el árbol **`7aeed6a`**, no sobre la candidata. `W1` no lo recalculó: lo leyó del gate anterior.

**Su CONCLUSIÓN, sin embargo, es correcta, y la establezco por mi cuenta con la prueba que él no dio:** `diff` de las primeras 444 líneas de la sede entre los dos commits → **sin salida**; y el `diff` del bloque `O20` entre los dos árboles → sólo `107a108,110`, que son una línea en blanco, un separador y otra línea en blanco. El texto de `O20` **no ha cambiado**. Lo que cambió es la **ventana de extracción**: al añadirse `O21` en apéndice, el `awk` que corta «desde `# O20` hasta el siguiente `# `» dejó de terminar en EOF y absorbió el separador. La sede es **append-only comprobado**, como `W2` midió bien. *Anoto como observación —no como hallazgo, porque ningún revisor lo planteó— que el digest por resolución es dependiente de frontera y cambia sin que su texto cambie: un revisor que contraste el ancla de un gate con la del siguiente concluirá una regresión que no existe.*

## 2 · LA COBERTURA DE LOS DOS REVISORES, DERIVADA POR MÍ

### `OBLIGATORIO − ASIGNADO` — derivada, no creída

Extraje mecánicamente las 86 rutas del manifiesto y las resté contra el universo derivado de cada commit:

    CANDIDATA f232d1a   universo 85 · asignado 86
      OBLIGATORIO − ASIGNADO  =  vacío
      ASIGNADO − OBLIGATORIO  =  F4C-ASIGNACION-GATE-FINAL-O21-20260901.md   (fila 11, declarada)

    GATE 2e31452        universo 87 · asignado 86
      OBLIGATORIO − ASIGNADO  =  F4C-ASIGNACION-GATE-FINAL-O21-20260901B.md  (el propio manifiesto)
      ASIGNADO − OBLIGATORIO  =  vacío

**Vacío sobre la candidata, que es el objeto del gate.** Sobre el árbol del gate el único hueco es **el manifiesto `B` mismo**, exención de PUNTO FIJO de `DD-19` declarada por adelantado en su §6, que cubre a ese fichero y a ningún otro. **La aritmética de §6 también deriva**: 10 filas/29348 líneas + 75 filas/62762 líneas = 85/92110. **Condición 4: SATISFECHA.**

### `ASIGNADO − LEÍDO` — medida contra las declaraciones de los dos

**Lote de `W1`: vacío.** Declara rangos enumerados y sin hueco para `11-ARQ` `L1-L5200` y `L7700-L12071`, y **íntegras** las seis restantes de su lote, más el manifiesto `B` del commit. Declara además, contra su interés, lecturas puntuales fuera de lote sin reclamarlas como íntegras. **No encuentro hueco en su declaración.**

**Lote de `W2`: NO VACÍO, y lo declara él antes que nadie.** De sus seis fuentes asignadas, **una** íntegra —la sede del Owner, 559 líneas—. Derivando su propia tabla de tramos sin abrir:

| fuente | asignado | sin abrir, por su declaración |
|---|---|---|
| `11-ARQ` `L5201-L12071` | 6 871 | ≈ **5 900** |
| `30-GATE-…F4C.md` | 3 084 | ≈ **2 719** |
| `CHECKPOINT` | 5 691 | ≈ **4 859** |
| `DECISIONES` | 1 449 | ≈ **1 272** |
| `00-INDICE` | 245 | 0 líneas, **pero con las filas largas truncadas a 260 caracteres**, y él lo declara |
| sede del Owner | 559 | **0 · ÍNTEGRA** |

**`ASIGNADO − LEÍDO` ≈ 14 750 líneas y CINCO FUENTES en el lote de `W2`.** No es una estimación mía sobre su silencio: es la resta de su propia enumeración, hecha contra su propio interés y antes de que nadie la midiera. **Condición 5: NO SATISFECHA.**

**Mi propia cobertura, contra mi interés.** Leí **íntegras** las dos fuentes que me toca leer —la sede del Owner (559, con `O20` y `O21` línea a línea) y el manifiesto `B` del commit del gate (303)— y **no declaro íntegro** el documento 30: leí su mapa de encabezados entero y, en su longitud completa, §0-§8 (L1-140), §6 `R-1` a `R-5` (L2664-2762), §7-§8 (L2846-2952), §9 entero (L2953-3050), §2.6 y §2.9, §3.2, §4.1, §5.7 y las filas que cité. **Los dictámenes `U1` y `U2` transcritos (L143-1769) NO los abrí íntegros.** Lo digo yo, y cuenta.

## 3 · HALLAZGO POR HALLAZGO — LOS DIECIOCHO

### Los nueve de `W1`

**`W1-01` — SOSTENIDO · severidad adjudicada BLOQUEANTE.** Es el que decide, y lo reproduje por sus dos mitades.

*Mitad primera — el comando deriva OTRO OBJETO.* `V6-15` (doc11:**11939**) declara que su ENTRADA es «el conjunto **derivado** de los **árboles adversariales** publicados por el SEXTO, SÉPTIMO y OCTAVO gate … **El conjunto no se escribe: se deriva** (§20.5)». **Ejecuté el comando de §20.5 (doc11:12047-12054), literal:** devuelve **75 IDENTIFICADORES DE HALLAZGO** —`EE-01…EE-19`, `R1-01…R1-09`, `S1-01…S1-09`, `S2-01…S2-05`, `C-00…C-21`, `T2-01…T2-12`—. **Son 75, no 74** —`W1` yerra el recuento por uno; corrijo la cifra y sostengo el hallazgo—. **Y no son árboles.** Verificado contra las filas: `C-05` es un hallazgo sobre el reparto de un manifiesto (doc29:3379), `C-10` sobre una columna de rótulo (doc29:3384), `EE-02` sobre la aritmética de un §6 (doc27:3885). Los árboles reales de esos tres gates son **tres**: el NOVENO (`EE-01`, doc 27, chk:4093), el DÉCIMO (doc 28) y el UNDÉCIMO (`T1-01`/`T1-02`, doc29:41, 681, 772) — y `T1-*` **ni siquiera aparece en la salida del comando**. El escenario negativo —«**cada uno** de los árboles del conjunto derivado vuelve a dar ROJO, uno a uno; **ni uno menos**»— y el cierre por las dos restas son **insatisfacibles** sobre 75 identificadores de los que unos 72 son defectos de redacción que no tienen rojo que dar. **Quien construya `V6-15` sigue teniendo que ELEGIR, que es exactamente lo que `H-06` denunciaba.** La lectura caritativa —«el conjunto son los hallazgos, no los árboles»— no está disponible: la propia celda dice «árboles adversariales» y §20.5 razona sobre «los once» todo el rato.

*Mitad segunda — la fase cambiada.* Doc30:**2962** adjudica: «Y que **el OCTAVO árbol (`DD-01`, quinto gate, doc 26), REPRODUCIDO, tenga fixture contratado** en alguna de las dieciocho filas» · **propietario `SIS`** · **fase `F4c`**. Doc11:**12056-12071** lo convierte en «**DEUDA DE INVENTARIO**» · **propietario `VER`** · **FASE `F6`**, y además la ensancha de un árbol nombrado a «los árboles de los gates anteriores al SEXTO». **Inventariar árboles con identificador y publicarlos en una sede derivable NO es implementar el verificador de admisión ni la raíz externa**, que es lo único que `O20` §3 y §6 mandan a `F6`. **La frontera de `O20` no ampara este movimiento.** Que esté declarado impide llamarlo *escondido*; no impide llamarlo lo que el §7 del manifiesto nombra: **«se le ha cambiado la fase para ablandarlo»**.

Se disparan **tres** supuestos del §7 del manifiesto. **BLOQUEANTE.**

**`W1-02` — SOSTENIDO · GRAVE.** Reproducido literalmente. Doc11:**11012-11013**: «SE CONFIRMA EL RESTO **1** estado · 2 adaptadores · 3 iniciativa · 4 certificación · 5 pack · **6** cobertura · **7** runtime · **8** primera adopción real» — **el nodo 9 no está**. Doc11:**11014-11017**: «el paso 8 exige la BASE COMPLETA ACORDADA de **los pasos 0 a 7**, y no un MVP». `sed -n '11005,11023p'` → **cero** menciones de `verificador`, `nodo 9`, `raíz externa`, `§20` o `V6-`. Y 130 líneas más arriba, doc11:**10874-10886**, el grafo **sí** lleva el nodo 9 y la arista «BLOQUEA 8 mientras 9 no esté IMPLEMENTADO **Y** CERTIFICADO». **La misma sede enuncia dos veces la condición de entrada del paso 8 y no dice lo mismo.** El adjudicador anterior graduó `H-02` GRAVE **por esta frase exacta** (doc30:2730-2734, verificado literal). §18 no calla. **GRAVE.**

**`W1-03` — CAÍDO.** Reproduzco el hecho: `emitir-sobre-de-ancla.py:698` es literalmente `_o19 = cuerpos_c.get(b"O19".decode("ascii"))`, y el campo 18 de §11.6 se titula «TEXTO ÍNTEGRO DE LA RATIFICACIÓN `O19`». **Pero el hecho no es un defecto.** (i) **Ninguna norma vigente ordena transportar otro texto**: `O19` L214-216, en la sede, dice «el texto de **esta** ratificación», y ninguna de las cinco resoluciones ordena que su propio texto viaje. (ii) **Ninguna sede queda falsada**: los campos 17 y 19 sí derivan «TODAS las que la SEDE contenga» porque `H-08` los alcanzaba; el 18 nombra `O19` **por diseño**. (iii) La «clase» que invoca **no está escrita en ninguna sede**: el propio `W1` escribe «Ninguna sede lo dice», que es la confesión de que no hay regla incumplida. (iv) Su única prueba es un árbol adversarial contra una `O22` **que no existe**. **Cae. Observación válida de ingeniería, no hallazgo de `F4c`.**

**`W1-04` — CAÍDO como defecto de `F4c` · reclasificado CLASE `C`.** El hecho es cierto y lo reproduje: la batería no menciona §20. **Pero §20 no dice nada falso, y `W1` lo concede**: ejecuté el comando que §20.3 publica y da **18 `CONTRATO_CONSTRUIBLE` + 1 `CONTRATO_BLOQUEADO_POR_DEPENDENCIA` = 19**, ninguno sumado, ninguno presentado como implementado. El defecto que `W1` señala es **«nada mecánico impide que mañana se falsee»**, probado con árboles que pasan la batería en verde. **Eso es, literalmente, la mitad de implementación de `M-04`**, y `O20` §4-§6 la manda a `F6`. El propio adjudicador anterior lo escribió en doc30:2990-2994. **Un hallazgo cuya única reparación es endurecer el instrumento contra un falso verde no puede fundar este gate. Cae.**

**`W1-05` — CAÍDO · CLASE `C`.** `W1` concede que los dos remedios están **materialmente aplicados** —lo verifiqué—. Lo que sostiene el hallazgo es que **revertirlos pasa 38/38**. Mismo razonamiento que `W1-04`: no hay sede falsa, hay un guardián inexistente. **Cae.**

**`W1-06` — CAÍDO.** Reproduje el texto: §11.6 campo 12 (doc11:**8428**) dice, entero, «**cuántas asignaciones publica el manifiesto previo**». Eso es **exactamente** lo que el emisor computa, y con un manifiesto que asigne a un revisor inexistente el número **sigue siendo literalmente verdadero**. **Ninguna sede afirma lo que `W1` dice que el campo afirma.** Y el propio `W1` reconoce que la resta `ASIGNADO − LEÍDO` **lo cazaría**: el sistema normativo no queda derrotado. **Cae.**

**`W1-07` — SOSTENIDO · MENOR.** Reproducido en las cuatro sedes. **Canónico**, sede L485-491: «**Para un gate válido:** — si se cumplen las seis condiciones … el adjudicador **debe** declarar». **Conservan la precondición:** `D110` (dec:**546**) y el checkpoint (chk:2439). **La pierden TRES sedes vivas:** doc11:**9288** · `00-INDICE`:**107** —no 110, `W1` yerra la línea; la corrijo y sostengo— · y **el §8 del manifiesto `B` L270-273**, que rige ESTE gate. **Leídas literalmente obligan a certificar cobertura sobre un gate INVÁLIDO**, que `O21` no dice. **MENOR.**

**`W1-08` — SOSTENIDO · MENOR.** Reproducido. chk:**4156-4157** y chk:**4161** dicen «**dieciocho** puntos»; el censo derivado de §20.1 da **19**. **El cardinal es FALSO HOY**, dentro del bloque de `M-04` y bajo el rótulo «SU ESTADO HOY». `H-14` retiró el cardinal de tres sedes y no de ésta. `W1` lo cita con línea y **declara expresamente que no leyó esa fuente íntegra**: la disciplina es correcta y el hecho es reproducible sin ella. **MENOR.**

**`W1-09` — CAÍDO.** Reproduje la receta: el bloque recortado da `d86a9455…` byte a byte. **Ninguna sede promete un invariante sobre el marco**, el fallo sería en dirección segura, y la reparación es endurecer un instrumento. **Cae.**

### Los nueve de `W2`

**`W2-01` — SOSTENIDO · GRAVE.** Es el segundo que decide, y lo ejecuté: el comando de la regla 7 devuelve **0** líneas; con `f` en vez de `!f`, **14**. **El comando que la regla 7 publica devuelve el CONJUNTO VACÍO.** La guarda `!f` selecciona lo que está **FUERA** de las vallas de código, y el bloque reanudable vive **DENTRO** de una valla abierta en `L972`. La regla 7 (chk:1008-1017) dice que «la comprobación es de **CLASE** y no de instancia … **el conjunto de campos se DERIVA del propio bloque en vez de escribirse**». **La garantía que esta serie escribió DENTRO del bloque para que el barrido no dependiera de que alguien se acordase no barre nada**, y quien la ejecute concluye que no hay campos y da la clase por cerrada. **Es un falso verde escrito dentro de la garantía, y no tiene nada que ver con el verificador de `F6`.** `W2` hizo lo correcto: derivó los 14 campos invirtiendo la guarda y los recorrió todos. **GRAVE.**

**`W2-02` — SOSTENIDO · MENOR** (`W2` propone MEDIO; rebajo, y digo por qué). Reproducido: chk:**1285** «los **NUEVE** declararon», en el campo VIGENTE; propagado a doc11:**9720**. Y es **literalmente una sustitución**: en `7aeed6a` el mismo campo decía «los **ocho**», y hoy ese texto vive correctamente en `last_meaningful_event_anterior` (chk:1308) por la regla 5. **`J-07` prohíbe sustituir un cardinal caducado por otro**, y §20.5 de esta misma serie lo escribe. *(La receta de `W2` no devuelve nada porque la frase está partida en dos líneas; su hecho es correcto, su comando no lo reproduce, y lo hago constar.)* **Rebajo a MENOR porque el número es VERDADERO hoy y reproduce el texto canónico del propio Owner** —`O21`, nota de trazabilidad, sede L553-554—: ninguna sede queda falsada. Lo que queda vivo es la regla 1 del bloque, y eso es real.

**`W2-03` — SOSTENIDO · MEDIO.** Reproducido con `cat -A`. chk:**2734** lleva un comando y la prosa que le seguía **fundidos en una línea, sin el salto**. **El comando así publicado no es ejecutable**, y está dentro del párrafo que presume de haber retirado bien un cardinal por `C-16`. Es la **pregunta 2 de la regla 7** fallando dentro de la sede que la escribe. `git blame` → **`7aeed6a`**: lo introdujo el remedio de `C-16` de la serie anterior, **y esta serie, que declara barrer la clase, no lo vio** — porque el instrumento del barrido devuelve vacío. **MEDIO.**

**`W2-04` — SOSTENIDO · MEDIO.** Reproducido. Entre `L2678` y `L2793` las **únicas** apariciones de `HISTÓRICO` son `L2686` y `L2736`. Entre ellas hay cinco viñetas sin rótulo, y la de `L2715` **reabre en presente** describiendo el documento **16**, quince documentos atrás, con su recuento copiado. Dos defectos a la vez, y **el ALCANCE del rótulo de `L2686` no está normado**. `git blame` → `7c7856c`. **MEDIO.**

**`W2-05` — SOSTENIDO · MEDIO.** Reproducido. `00-INDICE.md`:**35**, en la candidata **y** en el árbol del gate, enumera tres resoluciones donde la sede publica **cinco**. **Es la clase exacta de `H-10`** —misma sede citada, mismo verbo «contiene»— que este expediente cerró en `owner_captado` y en ningún otro sitio. El contraste es demoledor: **el checkpoint sí aplica la regla** en tres campos distintos, y **la fila del índice, dos renglones después de escribir «una paráfrasis nunca amplía el texto canónico», la incumple**. `git blame` → `1d3b5d4`: el texto es preexistente, **pero su falsedad la causaron los apéndices de `7aeed6a` y `07a6975`**. **MEDIO.**

**`W2-06` — SOSTENIDO · MENOR** (`W2` propone MEDIO; rebajo). Reproducido: el último epígrafe de la sección 1 es `491: ### D107`, cuyo preámbulo describe otro gate, otro adjudicador y otro recuento; entre medias la tabla lleva **`D108`, `D109` y `D110`** sin epígrafe propio. Es la recurrencia literal de `S-19`, y §15.8 del documento 11 **sí** da bloque a las cuatro. **Rebajo a MENOR porque es la severidad que el propio corpus adjudicó a este defecto idéntico**: doc23:610, `S3-01`. **MENOR, con la agravante de ser la tercera vez.**

**`W2-07` — SOSTENIDO · MENOR.** Ejecuté el comando que el propio índice publica sobre los dos árboles: sobre la candidata **sin salida**; sobre el árbol del gate, `18,19d17` con los dos manifiestos. La regla del índice es taxativa y avisa de que quien la incumpla «deja el árbol que juzga con un validador canónico en rojo, **causado por el aparato del propio gate**». Por el precedente `S-18`/`T-14`, es imputable **al GATE y no a la candidata**. **MENOR, y no pesa en la suficiencia de `F4c`**, pero consta: es la quinta vez que el aparato de un gate incumple la regla que ese mismo aparato escribió.

**`W2-08` — SOSTENIDO · LEVE.** Reproducido contra la sede, una por una. Los `ALCANCE` de `O17`, `O18`, `O20` y `O21` niegan las tres autorizaciones; **el de `O19` dice «NO autoriza iniciar `F5`» y nada más**. **La afirmación universal de chk:2208-2209 es falsa para una de las cinco.** La sustancia se mantiene; lo falso es la atribución «cada una lo declara en su propio texto», y la versión correcta ya está treinta líneas más abajo. **LEVE.**

**`W2-09` — SOSTENIDO · LEVE, y lo consolido con `W2-02`.** Reproducido. chk:**974-975**, campo `actualizado` —VIGENTE y reescrito por esta serie—, copia un recuento de hallazgos a doce líneas de la regla 1 que lo prohíbe. Las instancias de `metodo_anterior` son de `8c9ca9c` y viven en un campo cuyo nombre **es** el rótulo histórico. Lo que miden es que **el barrido de clase no se hizo campo a campo** — y no podía hacerse, porque su instrumento devuelve vacío. **LEVE.**

### ¿Son `W1-08` y `W2-02`/`W2-09` el mismo defecto?

**`W1-08` NO es el mismo defecto.** Comparten CLASE —`J-07`— y nada más. Difieren en las tres cosas que hacen de un defecto un defecto: **verdad** —el de `W1-08` es FALSO HOY; los otros son verdaderos—; **sede** —`W1-08` vive fuera del bloque reanudable y por tanto fuera del alcance de la regla 7—; y **procedencia** —`7aeed6a` frente a `07a6975`—. Consolidarlos escondería que uno es una afirmación falsa y los otros no. **Van separados.**

**`W2-02` y `W2-09` SÍ son el mismo defecto**, y los fusiono en `HH2-10`.

## 4 · MATRIZ CONSOLIDADA

| `HH2` | sev. | clase | de | sede · fichero:línea | remedio EXACTO — QUÉ, no cómo |
|---|---|---|---|---|---|
| **`HH2-01`** | **BLOQUEANTE** | **A** | `W1-01` | `11-ARQ`:**11939** (`V6-15`), **12047-12054** (comando), **12056-12071** (deuda) · contra `30-…`:**2962** | Que el conjunto que §20.5 DERIVA **sea el que la ENTRADA de `V6-15` nombra** —árboles adversariales identificados, no hallazgos—, de modo que el escenario negativo y las dos restas de cierre sean satisfacibles sin que nadie elija; **y que la segunda mitad del remedio adjudicado de `H-06` —fixture contratado para el octavo árbol `DD-01`— recupere el propietario y la fase que el gate le adjudicó (`SIS`, `F4c`), o que quien la mueva a `F6` sea quien tenga autoridad para moverla** |
| **`HH2-02`** | **GRAVE** | **A** | `W2-01` | `CHECKPOINT`:**1013-1014** (regla 7) | Que el comando que la regla 7 publica **DERIVE los campos del bloque** en vez del conjunto vacío |
| **`HH2-03`** | **GRAVE** | **A** | `W1-02` | `11-ARQ`:**11012-11017** contra **10874-10886** | Que §18 **enuncie UNA sola condición de entrada para su paso 8**, y que esa condición contenga el nodo 9 |
| **`HH2-04`** | MEDIO | **A** | `W2-03` | `CHECKPOINT`:**2734** | Que el comando publicado **quede separado de la prosa** y sea ejecutable |
| **`HH2-05`** | MEDIO | **A** | `W2-04` | `CHECKPOINT`:**2715-2735** | Que la viñeta **lleve rótulo histórico** y **no copie un recuento** que su regla 2 remite al documento del gate; y que **el ALCANCE de un rótulo histórico quede normado** |
| **`HH2-06`** | MEDIO | **A** | `W2-05` | `00-INDICE.md`:**35** (los dos árboles) | Que la fila **deje de enumerar** las resoluciones de la sede y **remita o derive**, como el checkpoint ya hace en tres campos |
| **`HH2-07`** | MENOR | **A** | `W1-08` | `CHECKPOINT`:**4157**, **4161** | Que el cardinal de los puntos de §20 **se retire y se remita**, no que se sustituya por 19 |
| **`HH2-08`** | MENOR | **A** | `W1-07` | `11-ARQ`:**9288** · `00-INDICE`:**107** · manifiesto `B` §8 **L270-273** | Que las tres **conserven la precondición «para un gate válido»** que `O21` §3 escribe |
| **`HH2-09`** | MENOR | **A** | `W2-06` | `DECISIONES`:**491** (epígrafe) y **544-546** | Que `D108`, `D109` y `D110` **tengan epígrafe propio**, o que la regla que `S-19` no estableció se establezca |
| **`HH2-10`** | MENOR | **A** | `W2-02`+`W2-09` | `CHECKPOINT`:**974-975** y **1285** · propagación `11-ARQ`:**9720** | Que los campos VIGENTES del bloque **retiren y remitan** sus cardinales en vez de sustituirlos, que es lo que sus reglas 1 y 2 ordenan |
| **`HH2-11`** | LEVE | **A** | `W2-08` | `CHECKPOINT`:**2208-2209** | Que la afirmación **deje de ser universal** donde `O19` no la sostiene |
| **`HH2-12`** | MENOR | **A** | `W2-07` | `00-INDICE.md`:**149-167** **sobre `2e31452`** | Que el commit que publica un manifiesto **lo enlace desde la LISTA**, que es la regla que el propio índice escribe |

**RECUENTO, DERIVADO DE LAS DOCE FILAS DE ARRIBA:** BLOQUEANTE **1** · GRAVE **2** · MEDIO **3** · MENOR **5** · LEVE **1** = **12**. Clase **A 12 · B 0 · C 0**.

**CAÍDOS: 5** — `W1-03`, `W1-04`, `W1-05`, `W1-06`, `W1-09`. **Los cinco son de `W1` y los cinco caen por la misma razón estructural**: su única prueba es que un árbol adversarial pasa la batería interna en verde, y esa es la mitad de implementación de `M-04`, que `O20` asigna a `F6` y `V6-18` contrata sin construir. **Ninguno de los cinco identifica una sede que diga algo falso ni una obligación escrita incumplida.** `W1` afirma que «ninguno se funda en que el verificador de `F6` no esté implementado»; **en sustancia, cinco de sus nueve sí**, y ése es el defecto de su dictamen.

**De 18 planteados: 13 sostenidos, 12 consolidados, 5 caídos.**

## 5 · LOS CATORCE PUNTOS DEL §7 DEL MANIFIESTO — MI VEREDICTO

**1 · Los DIECISÉIS `H-01`…`H-16`.** **CATORCE aplicados, DOS a medias.** Verifiqué uno a uno contra doc30 §9. **`H-02` sólo en el grafo (`HH2-03`) y `H-06` con la derivación del objeto equivocado y la segunda mitad cambiada de fase (`HH2-01`).** `W2` afirma «los dieciséis están APLICADOS»: **es falso en dos**. `W1` acierta.

**2 · Las OCHO CAUSAS: ¿por CLASE o por INSTANCIA?** **Es donde el expediente vuelve a fallar, y por tercera vía distinta.** Cerradas por clase: `H-08`, `H-14`, la primera mitad de `H-06`, `H-07` y `H-05`. **Cerradas por INSTANCIA:** `H-02` (`HH2-03`) · `H-06` en su segunda mitad (`HH2-01`) · la clase `J-07`/`H-10`, viva en `00-INDICE`:35 (`HH2-06`), reintroducida en dos campos (`HH2-10`) y falsa en chk:4157 (`HH2-07`) · la clase `C-15` (`HH2-05`) · la clase `S-19` (`HH2-09`). **Y por encima de todas: la clase `C-L.7` se declaró barrida con un instrumento que devuelve el conjunto vacío** (`HH2-02`). **NO.**

**3 · `O21` y la independencia entre certificar y declarar suficiencia.** **La independencia está BIEN ESCRITA y bien instrumentada.** **APPEND-ONLY comprobado, no creído**: cero borrados, cero modificaciones de líneas anteriores. **Pero tres proyecciones dicen más que la sede** (`HH2-08`), y una de las tres es el §8 del manifiesto que me rige.

**4 · `C-L.5` por sus SEIS condiciones.** Medida abajo, en §7(A). **Falla la 5.**

**5 · `C-L.7` como CLASE COMPLETA.** **NO CERRADA, y esta vez con una razón nueva y peor:** el instrumento que la serie escribió DENTRO del bloque para que el barrido fuera de clase **deriva el conjunto vacío** (`HH2-02`). Recorrí los catorce campos que el comando **debería** haber devuelto: nueve pasan las tres preguntas limpiamente —y hay que decir a favor que `based_on`, `pregunta_pendiente`, `siguiente` y `rama_de_trabajo` están hoy retirados y remitidos con disciplina real—, **cuatro fallan**, y **el último falla las tres preguntas a la vez**.

**6 · `C-20` y el CONTENIDO REAL DEL SOBRE.** **CERRADO EN SU INSTANCIA, y es lo mejor de esta serie.** `O19` enumera seis cosas; **las recibo las seis**, y la primera —el TEXTO— viaja entero: **81 de 81 líneas, idénticas byte a byte al commit auditado**. **Sin defecto en este punto**, y la clase que `W1-03` le atribuye no está escrita en ninguna sede.

**7 · `V6-15`: ¿entrada, escenario negativo y cierre describen el MISMO conjunto?** **NO.** Los tres remiten a §20.5 —y en eso el remedio funciona— **pero §20.5 deriva otro objeto**. `HH2-01`. **Es peor que un cardinal escrito, porque es mecánico y nadie lo ejecutó.**

**8 · `V6-16` y `PN-19` (§20.4).** **CORRECTO, sin reserva.** La dependencia está **DECLARADA**, **ENLAZADA** y con **CONDICIÓN EXACTA de desbloqueo** en tres incisos numerados, más fase `F5`, propietario el Owner, qué bloquea y qué no. **No es una etiqueta. Sin hallazgo.**

**9 · Los contratos de §20 y su CLASIFICACIÓN SEMÁNTICA.** Derivado por mí: **19 filas, las 19 con 10 celdas, CERO celdas vacías**; **18 `CONSTRUIBLE` + 1 `BLOQUEADO` = 19**. **Ningún bloqueado se cuenta como construible; ninguno se presenta como implementado.** `V6-19` tiene criterio **exacto y medible**. **La clasificación es CORRECTA HOY.** Lo único que falla es `V6-15`.

**10 · El ORDEN DE CONSTRUCCIÓN hasta PesquerApp.** **FALLA.** El nodo 9 existe y la arista existe — **y la misma sede sigue enunciando la entrada del paso 8 como «los pasos 0 a 7»**. `HH2-03`.

**11 · AUSENCIA DE ARQUITECTURA OCULTA.** **No encuentro defecto.** El único candidato real es `V6-16`, y **no está oculto**. Donde hay dos salidas incompatibles, el corpus **declara que elegir es del Owner y no elige**.

**12 · Que NINGUNA DEUDA DE `F6` se presente como implementada.** **No encuentro defecto.** Barrí el corpus: **todas las coincidencias son negaciones**. El §9 del manifiesto **lo repite contra su propio interés justo después de publicar 38/38**. Ejecuté la batería sobre el árbol del gate: **38/38 · EXIT=0 · `porcelain` vacío después**. **Ese verde no se usa aquí como prueba de nada de `F6`.**

**13 · Que PesquerApp SIGA BLOQUEADA.** **SÍ.** Ocho ficheros la bloquean con las mismas tres exclusiones. **Mi barrido en dirección contraria no devuelve una sola sede que la autorice, la abra o la programe.**

**14 · AUSENCIA DE REGRESIONES en `O20` y en la MATRIZ DE LOS 22.** **No encuentro defecto.** **`O20` conserva su texto** —lo probé con el `diff` de la sede, no con el digest, que es dependiente de frontera—. La matriz: **22 filas, 22 identificadores únicos, un estado primario cada uno**; la cobertura contra el documento 29 **sale vacía en las dos direcciones**; **ningún hallazgo se declara SUPERADO**. §15.4 tiene una fila por resolución y la resta contra la sede cierra; §15.8 tiene veinte bloques, `D107`-`D110` incluidos.

## 6 · LA RESPUESTA A `F` — ¿QUIÉN INTRODUJO CADA UNO?

La serie que registró `O21` y aplicó los dieciséis es **`07a6975`**; el árbol del gate anterior es **`7aeed6a`**. Medido con `git blame` sobre `f232d1a`, no con lectura:

### INTRODUCIDOS POR ESTA SERIE — **5 de los 12**, y entre ellos **el BLOQUEANTE**

| `HH2` | sede | blame |
|---|---|---|
| **`HH2-01`** · **BLOQUEANTE** | `11-ARQ`:11939 · 12047-12054 · 12056-12071 | **`07a6975`** |
| **`HH2-02`** · **GRAVE** | `CHECKPOINT`:1013-1014 | **`07a6975`** |
| **`HH2-08`** · MENOR | `11-ARQ`:9288 · `00-INDICE`:107 | **`07a6975`** · el tercer sitio, el §8 del manifiesto `B`, lo creó **`2e31452`** |
| **`HH2-10`** · MENOR | `CHECKPOINT`:974 y 1285 · `11-ARQ`:9720 | **`07a6975`** |
| **`HH2-11`** · LEVE | `CHECKPOINT`:2208 | **`07a6975`** |

**Los tres hallazgos de mayor severidad que sostengo —el BLOQUEANTE y uno de los dos GRAVES— los escribió esta misma serie**, y los dos primeros están **DENTRO del remedio que venían a aplicar**: `HH2-01` es el remedio de `H-06`, y `HH2-02` es la garantía escrita para cerrar `C-L.7` por clase. **El modo de fallo del expediente —cada pasada introduce defectos en el texto de su propia corrección— se repite, y por primera vez alcanza al remedio de un hallazgo adjudicado y a su propio instrumento de barrido a la vez.**

### PREEXISTENTES — **6 de los 12**

| `HH2` | sede | blame |
|---|---|---|
| **`HH2-03`** · **GRAVE** | `11-ARQ`:11012-11017 | `7a3f11e` / `304fc29d` |
| **`HH2-04`** · MEDIO | `CHECKPOINT`:2734 | **`7aeed6a`** — lo introdujo el remedio de `C-16` de la serie ANTERIOR |
| **`HH2-05`** · MEDIO | `CHECKPOINT`:2715, 2717 | `7c7856c` (2026-08-28) |
| **`HH2-06`** · MEDIO | `00-INDICE`:35 | `1d3b5d4` — **texto preexistente, falsedad CAUSADA por los apéndices de `7aeed6a` y `07a6975`** |
| **`HH2-07`** · MENOR | `CHECKPOINT`:4157, 4161 | **`7aeed6a`** |
| **`HH2-09`** · MENOR | `DECISIONES`:491 | `8c3afe7` — **pero esta serie archivó `D109` y `D110` bajo él**, extendiendo el defecto dos veces |

### CASO APARTE

**`HH2-12`** lo introdujo **el propio commit del gate `2e31452`**, no la candidata: no es de esta serie ni preexistente, es del aparato de este gate.

## 7 · LAS DOS DECLARACIONES, SEPARADAS

Leí `O21` **íntegra** en la sede canónica (L448-559) antes de emitirlas. `O21` §2 me prohíbe deducir una de la otra y §8 me prohíbe negar la primera por defectos; las emito por separado y en este orden.

### (A) COBERTURA

Mido las seis, una a una, y no las deduzco de nada:

    1  corpus obligatorio DEFINIDO ......................... SATISFECHA
         derivado y recalculado por mí: 85/92110 y 87/92699, con el derivador
         de cada commit extraído de su propio commit
    2  manifiesto previo de ASIGNACION publicado ........... SATISFECHA
         commiteado en 2e31452 antes de que existiera ningún revisor,
         SHA-256 4a27b5ef… verificado contra el sobre
    3  manifiestos posteriores de LECTURA publicados ....... SATISFECHA
         §2 de W1 con rangos enumerados · §2 de W2 con ruta, líneas,
         SHA-256 recalculados y tramos sin abrir · el mío en §2 de arriba
    4  OBLIGATORIO menos ASIGNADO = vacío .................. SATISFECHA
         vacío sobre la candidata, derivada por mí en las dos direcciones;
         sobre el árbol del gate el único hueco es el propio manifiesto B,
         exención de PUNTO FIJO declarada por adelantado en su §6
    5  ASIGNADO menos LEIDO = vacío ........................ **NO SATISFECHA**
         vacío en el lote de W1. En el lote de W2, unas 14 750 líneas y CINCO
         de sus SEIS fuentes asignadas sin lectura íntegra, por su propia
         declaración contra su propio interés
    6  revisores INDEPENDIENTES que declaran contra su
       propio interés qué leyeron ......................... SATISFECHA
         los dos lo hacen, y W2 lo hace en la dirección que le perjudica

**La condición 6 se cumple precisamente por el mismo hecho que hace fallar la 5**, y quiero que conste sin ambigüedad: **`W2` declaró su propia carencia antes de que nadie la midiera, con ruta, tramo y línea.** Eso es exactamente lo que la condición 6 exige y es lo que hace que este gate sea auditable. **Pero la condición 5 no mide honestidad: mide lectura**, y la resta no es vacía. `O21` §3 no me deja compensar una condición con otra.

**No la declaro ABIERTA por haber encontrado defectos** —`O21` §8 me lo prohíbe y no lo hago—, **ni por el veredicto de suficiencia** —`O21` §2 me lo prohíbe y lo emito después—. La declaro ABIERTA porque **conté**, y la cuenta no da cero.

### C-L.5 ABIERTA

**CONDICIÓN INCUMPLIDA: la 5 — `ASIGNADO − LEÍDO` no es vacío.** Cinco fuentes del lote de `W2` —el documento 11 en su rango `L5201-L12071`, el documento 30, el `CHECKPOINT`, el registro de decisiones y, con la reserva del truncamiento de filas largas, el índice— **están asignadas y no leídas íntegras.** Las otras cinco condiciones se cumplen y quedan medidas arriba, para que el gate siguiente parta de ahí y no vuelva a derivarlas.

*No publico tupla: `O21` §5 liga la tupla a la certificación, y no certifico.*

### (B) SUFICIENCIA

### INSUFICIENTE PARA F5

**La razón, en una línea:** `V6-15` sigue sin poder construirse —§20.5 publica bajo el rótulo «EL CONJUNTO. Es la sede» un comando que deriva **75 identificadores de hallazgo** donde su entrada nombra **árboles adversariales**, y la mitad del remedio adjudicado de `H-06` que exigía fixture contratado para el octavo árbol con propietario `SIS` y fase `F4c` se ha convertido en deuda de inventario de `VER` en `F6`—; **la garantía que esta serie escribió dentro del bloque reanudable para cerrar `C-L.7` por CLASE deriva el conjunto vacío**; y `H-02` está cerrado en el grafo de §18 y abierto en la frase que el adjudicador anterior señaló como la razón exacta de su severidad.

**Se disparan CUATRO de los siete supuestos del §7 del manifiesto**, y ninguno de ellos es que el verificador de `F6` no esté implementado:

    · falta CRITERIO DE CIERRE efectivo en un contrato ............ HH2-01
    · un hallazgo se ha cambiado de FASE para ablandarlo .......... HH2-01 (SIS/F4c → VER/F6)
    · la matriz adversarial no especifica una clase reproducida ... HH2-01 (DD-01, el octavo árbol)
    · una obligación depende de INTERPRETACIÓN HUMANA NO NORMADA .. HH2-01 · HH2-02

**Y de forma independiente**, el §8 del manifiesto que rige este gate escribe: «**CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA**». Cinco lo están. **Cualquiera de las dos razones bastaría por sí sola.**

**Declaro expresamente lo que NO he usado para llegar aquí:** que el verificador de `F6` no esté implementado —esa ausencia es ESPERADA y `O20` la fija—; ninguna de las cinco afirmaciones de `W1` que caen por apoyarse en árboles adversariales contra la batería interna; y ningún verde ni ningún rojo de esa batería.

### Y digo lo que `O21` me obliga a decir sobre la relación entre las dos

**No he condicionado ninguna a la otra.** Si `W2` hubiera leído sus seis fuentes íntegras, mi declaración (A) sería `C-L.5 CERTIFICADA PARA ESTE GATE` **y (B) seguiría siendo `INSUFICIENTE PARA F5`**, porque `HH2-01` no depende de la cobertura. Y si `HH2-01` no existiera, (A) seguiría siendo ABIERTA. **Las dos preguntas se han respondido por separado, y sus respuestas no se sostienen la una en la otra.**

## 8 · ¿VUELVE ALGO AL OWNER?

### NO. NADA VUELVE AL OWNER.

**Por séptima vez consecutiva.** Clasifico los doce: **clase `A` 12 · clase `B` 0 · clase `C` 0.** Ninguno exige arquitectura nueva, ninguno reinterpreta `O17`, `O18`, `O19`, `O20` ni `O21`, y los doce se cierran con material que el corpus ya tiene escrito: un comando que derive lo que su entrada nombra, un `!f` que debe ser `f`, una frase de §18, un salto de línea, un rótulo histórico, cinco retiradas o remisiones, tres precondiciones restituidas y tres epígrafes.

**Razono el único candidato real, que es `HH2-01`.** Su remedio tiene dos ramas y sólo una está disponible: **(i) que §20.5 derive lo que `V6-15` nombra y que la segunda mitad de `H-06` recupere su fase adjudicada** —eso es cumplir lo que un gate ya determinó, con material escrito, y **no vuelve al Owner**—; **(ii) revisar el remedio adjudicado del documento 30 para que la deuda sea legítimamente de `F6`** —eso **no lo puede hacer quien aplica**, pero tampoco es del Owner: **es de un gate**, y este gate acaba de negarlo. La rama (i) está disponible, y por eso mi respuesta es NO.

Y **`PN-19`**, que sí es una decisión del Owner, ya está formulada, acotada, con sede, fase `F5` y propietario: **no vuelve hoy, y `HH2-01` no pide que vuelva.**

**Los cinco caídos son, donde tienen sustancia, clase `C`** —obligaciones de `F6` cubiertas por `V6-11`, `V6-15` y `V6-18`—, y por eso este gate no se funda en ninguno.

## 9 · QUÉ CONSTA A FAVOR, PORQUE TAMBIÉN ES INFORMACIÓN

- **El sobre es el mejor de los once, y no por poco.** Las siete obligaciones reproducen; **transporta las 81 de 81 líneas de `O19`** y el `diff` contra el commit auditado sale **sin una sola salida**. El gate anterior midió 2 de 62 líneas sustantivas. `C-20` está **materialmente cerrado** en su instancia.
- **Las 86 filas del manifiesto casan sin una discrepancia**, contra su árbol y con su recuento de líneas. **La fila del derivador NO reincide, por sexta vez.** Las dos filas que no casan contra los dos árboles a la vez lo declaran ellas mismas, y el sobre publica la diferencia.
- **Las dos aritméticas de §6 derivan y cierran** contra el universo anclado, y la exención de punto fijo de `DD-19` se declaró **antes**, se acotó a un fichero, y **es exactamente el único hueco que mi resta encuentra**.
- **La sede canónica es APPEND-ONLY comprobado, no declarado**: líneas 1-444 byte a byte idénticas entre `7aeed6a` y la candidata. **`O20` conserva su texto.**
- **Catorce de los dieciséis remedios están materialmente aplicados**, y varios cerrados por clase de verdad: `H-08` sustituyó un enumerado por una derivación, `H-07` normó los tres requisitos de una dependencia bloqueada, `H-05` creó una regla general de sede única.
- **Los diecinueve contratos de §20 tienen sus diez celdas y ninguna vacía; `V6-19` es un contrato correcto con criterio exacto y medible; §20.4 declara su única dependencia entera.**
- **PesquerApp está bloqueada por ocho sedes** con las mismas tres exclusiones, y **ninguna sede del corpus la autoriza, la abre ni la programa**.
- **Ningún hallazgo se declara SUPERADO. La matriz de los 22 cierra en las dos direcciones. §15.4 y §15.8 cierran su cobertura derivada. Ninguna deuda de `F6` se presenta como implementada**, y el §9 del manifiesto lo repite **contra su propio interés** justo después de publicar 38/38.
- **Nueve de los catorce campos del bloque reanudable pasan las tres preguntas limpiamente**, y eso es más de lo que ningún gate anterior había medido.
- **Y lo que más pesa a favor del método, aunque cueste el veredicto de cobertura: `W2` declaró contra sí mismo, con ruta y tramo, que no había leído cinco de sus seis fuentes, antes de que nadie lo midiera.** Sin esa declaración yo no habría podido medir la condición 5, y `C-L.5` se habría certificado sobre una lectura que no existió. **La sexta condición funcionó exactamente para lo que está escrita.**

**No he corregido nada. No he resuelto por mayoría: de los cinco hallazgos que caen, los cinco venían de un solo revisor y ninguno cayó por estar solo, sino por lo que el árbol dice; y de los doce que sostengo, siete los planteó uno solo. He señalado dos reproducciones falsas de `W1` —el digest de `O20` y el recuento de 74— y una receta que no reproduce de `W2` —el `grep` sobre `7aeed6a`—, y en los tres casos he establecido el hecho por mi cuenta antes de adjudicarlo.**

**`WA`, adjudicador. Cierro.**

---

## 6 · SE ACTIVA LA OPCIÓN C, Y EL MÉTODO QUEDA DETENIDO

**Esta sección la escribe el coordinador, no el gate.** El adjudicador cerró en §5 y no
participa de lo que sigue.

**LA CONDICIÓN QUE LA DISPARA, escrita por el Owner ANTES de que este gate existiera:**
*«Si el gate devuelve insuficiencia por defectos introducidos por esta misma tanda, no
propongas otro ciclo: registra que se activa la opción C y que el método queda detenido.»*

**LA CONDICIÓN SE CUMPLE, y no por interpretación.** El adjudicador respondió expresamente a
esa pregunta —era el punto `F` de su encargo— y la respondió con `git blame`, no con lectura:

```text
INTRODUCIDOS POR ESTA SERIE   5 de los 12, y entre ellos el ÚNICO BLOQUEANTE
                              HH2-01 BLOQUEANTE · HH2-02 GRAVE · HH2-08 · HH2-10 · HH2-11
PREEXISTENTES                 6 de los 12
DEL APARATO DE ESTE GATE      1  ·  HH2-12
```

**Y los dos que deciden el veredicto están DENTRO del remedio que venían a aplicar.**
`HH2-01` es el remedio de `H-06`: la sección que se escribió para que `V6-15` dejara de
contradecirse publica un comando que deriva **identificadores de hallazgo** donde su propia
entrada nombra **árboles adversariales**, y mueve a `F6` la mitad del remedio que el gate
anterior había adjudicado a `F4c` con propietario `SIS`. `HH2-02` es la **garantía escrita
DENTRO del bloque reanudable para cerrar `C-L.7` por CLASE**, y deriva el conjunto vacío.

**Lo dice el adjudicador con sus palabras, y se transcribe porque es el hecho que decide:**
*«El modo de fallo del expediente —cada pasada introduce defectos en el texto de su propia
corrección— se repite, y por primera vez alcanza al remedio de un hallazgo adjudicado y a su
propio instrumento de barrido a la vez.»*

### QUÉ SIGNIFICA LA OPCIÓN C, Y QUÉ NO

```text
QUÉ ES                    el método de corrección iterativa de `F4c` QUEDA DETENIDO. No se
                          abre otro ciclo, no se propone otra tanda y no se convoca otro
                          gate. La decisión de qué hacer a partir de aquí es del Owner

QUÉ **NO** ES             **no es un cierre de `F4c`**: `F4c` queda ABIERTA, con doce
                          hallazgos vivos y su remedio escrito, cada uno con sede, línea y
                          qué —no cómo—
                          **no es una autorización**: `F5`, `F6` y PesquerApp siguen sin
                          autorizar, y PesquerApp sigue BLOQUEADA por ocho sedes
                          **no declara superado nada**: ni uno de los doce, ni `M-04`, ni
                          `C-L.5`, ni `C-L.7`
                          **no revisa ninguna resolución del Owner**: `O17` a `O21`
                          conservan íntegro su texto, y la sede sigue siendo append-only
                          **no descarta el trabajo hecho**: catorce de los dieciséis
                          remedios están materialmente aplicados y así lo mide el gate

QUÉ QUEDA ENTREGADO       el veredicto literal, los doce hallazgos con su remedio exacto, la
                          respuesta a quién introdujo cada uno, las cinco condiciones de
                          cobertura MEDIDAS y la que falla NOMBRADA. El gate siguiente
                          —si el Owner decide que lo haya— no tiene que volver a derivar
                          nada de eso
```

### POR QUÉ LA OPCIÓN C Y NO OTRA COSA, DICHO SIN ADORNO

**Once gates, y el patrón no lo rompe ninguna tanda: cada corrección introduce defectos en
el texto de su propia corrección.** Esta serie lo hizo en el sitio más elocuente posible —el
remedio de un hallazgo adjudicado y el instrumento escrito para barrer una clase—, y **eso es
un dato sobre el MÉTODO, no sobre los hallazgos**. Proponer un duodécimo ciclo sería aplicar
otra vez el procedimiento cuya tasa de reintroducción acaba de medirse. **El Owner escribió la
regla antes de conocer el resultado, y la regla se aplica.**

**Lo que NO se afirma aquí:** que los doce no se puedan corregir. **Once de los doce son
correcciones de una línea o de un párrafo** —un `!f` que debe ser `f`, un salto de línea, un
rótulo histórico, cinco retiradas y remisiones, tres precondiciones restituidas—, y el propio
adjudicador escribe que los doce «se cierran con material que el corpus ya tiene escrito». **Lo
que se afirma es que quien las aplique no debe ser este método, tal como está.**

## 7 · Estado exacto en que queda el expediente

```text
`F4c`                     ABIERTA
`F5`                      NO AUTORIZADA
`F6`                      NO INICIADA. Su contrato está escrito —§20 del documento 11— y
                          ninguno de sus puntos implementado, ejecutado ni certificado
PesquerApp                BLOQUEADA. Sin MVP, sin piloto desechable y sin adopción parcial
`C-L.5`                   ABIERTA, por la condición 5, nombrada
`C-L.7`                   NO CERRADA
`M-04`                    NO SUPERADA
LOS 22 DE `O20`           su matriz sigue cerrando, ninguno SUPERADO
LOS 16 DEL DOCUMENTO 30   catorce aplicados, dos a medias, ninguno SUPERADO
LOS 12 DE ESTE GATE       vivos, con remedio escrito y sin aplicar
EL MÉTODO                 DETENIDO. Opción C activada
```

**Y una última cosa, que es del gate y no del coordinador, y por eso se transcribe literal:**
*«Lo que más pesa a favor del método, aunque cueste el veredicto de cobertura: `W2` declaró
contra sí mismo, con ruta y tramo, que no había leído cinco de sus seis fuentes, antes de que
nadie lo midiera. Sin esa declaración yo no habría podido medir la condición 5, y `C-L.5` se
habría certificado sobre una lectura que no existió. La sexta condición funcionó exactamente
para lo que está escrita.»*
