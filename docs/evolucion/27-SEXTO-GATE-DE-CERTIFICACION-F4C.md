# SEXTO GATE DE CERTIFICACIÓN DE F4c — VÁLIDO, INSUFICIENTE, Y EL NOVENO ÁRBOL

> **Veredicto del adjudicador `EE`: `F4c` ES INSUFICIENTE PARA F5.**
> **`F4c` NO se cierra y sigue ABIERTA. `F5` NO queda autorizada. Ningún hallazgo se ha**
> **corregido en esta pasada.**
>
> **Y EL GATE ES VÁLIDO, por segunda vez consecutiva.** El remedio de la entrega —el sobre
> emitido UNA vez a un fichero fuera del repositorio auditado— vuelve a funcionar, y esta vez
> el adjudicador lo midió comparando los TRES bloques byte a byte.

## 0 · Qué es este documento

Registro **LITERAL** de los tres dictámenes del sexto gate independiente sobre la candidata
`b27a761bb3eb6b0b1b3db2344b7184ef4b993309`, publicada en
`review/f4c-clase-cerrada-candidate-20260831`. Los tres se transcriben **enteros y sin
suavizar**, en §A, §B y §C.

Lo escrito antes de §A lo escribe el **coordinador**, que no es ninguno de los tres
participantes y **que no ha juzgado nada**. Los tres dictámenes **no pasaron por su mano**: se
concatenaron desde los ficheros que sus autores escribieron, y este documento publica sus
SHA-256 para que cualquiera lo compruebe.

```text
DICTAMEN DEL REVISOR `R1`
  1421 lineas   SHA-256  0ad6bc011556165277b9ffb900303f16a3cb4cf5d3f08d4fb242f752e84b04bd
DICTAMEN DEL REVISOR `R2`
   999 lineas   SHA-256  cd59d4ac169837be6517b03ab009f727ba6b9b17539fe948b049ea18edb1a645
ADJUDICACIÓN DE `EE`
  1344 lineas   SHA-256  eb7264b1d6fd3efa133a7454aaec027d883fc687a8a828db2989ec33bd022b44
EL SOBRE DE ANCLA, leído por los tres
   194 lineas   SHA-256  731c282ac3305827f1e09ee4da0b7dc2f94be824e997d37376497616a0f0554c
```

## 1 · EL GATE ES VÁLIDO, Y ESO SE MIDE ANTES DE NADA

El cuarto gate murió porque el coordinador **transcribió el sobre a mano** y las cinco
transcripciones difirieron en ocho campos. Desde el quinto el sobre **no se transcribe**: se
emite UNA vez a un fichero fuera del repositorio auditado y cada revisor lee de ahí.

`EE` no lo dio por bueno: **comparó los tres bloques** —el que embebió `R1`, el que embebió
`R2` y el fichero— y son **byte a byte el mismo**, con `diff` vacío y el mismo SHA-256.
Recalculó además los dos digest de universo con la receta publicada, el SHA-256 del
manifiesto en el commit del gate, el del emisor y el del derivador en los DOS commits, y la
sede canónica del Owner con sus tres resoluciones. **Todo reproduce.** Y comprobó que no
hubiera ningún fichero en `skip-worktree` ni en `assume-unchanged`.

**Ninguno de los dos disparadores de invalidez que la regla de cierre nombra se dispara.**

## 2 · EL NOVENO ÁRBOL, Y LO ENCONTRÓ UN REVISOR Y LO REPRODUJO EL ADJUDICADOR

El gate anterior encontró el OCTAVO ÁRBOL en el PERÍMETRO y `DD-01` lo cerró **por clase**:
`.git` anclado a la raíz, poda sobre la ruta completa, bytecode por contenido, y todo lo
excluido publicado con su ruta. **Ese remedio funciona, resistió cinco variantes y `EE` lo
declara un éxito con todas sus letras.**

**El noveno árbol no está en el perímetro: está en la GUARDA DE ADMISIÓN, que es el remedio
del gate anterior.** `DD-02` hizo que la admisión de `docs/owner/` se evaluara sobre el
CONTENIDO DEL COMMIT. Se cerró **esa zona**, y sólo esa: para todo el resto del corpus
gobernado la guarda sigue mirando únicamente **lo que aún no está en `HEAD`**.

```text
QUÉ SE HACE     `git add -A && git commit` — SIN UN SOLO FLAG, sin `-f`, sin fontanería
QUÉ SE AÑADE    una SEGUNDA SEDE NORMATIVA que declara `F4c` CERRADA y `F5` AUTORIZADA
DÓNDE           fuera de `docs/owner/`: en `docs/normativa/`, en `docs/` o en la RAÍZ
QUÉ PASA        `git status --porcelain` VACÍO · la batería **38/38 EN VERDE** · el universo
                obligatorio **intacto en 76** · CERO menciones en las cinco salidas del
                aparato · y el digest del universo **BIT A BIT el que este gate ANCLA**
QUIÉN LO HIZO   `R1` lo encontró y lo midió; **`EE` lo reprodujo por su cuenta, dos veces y
                con dos ficheros distintos**, en un clon desechable fuera del árbol auditado
```

Y con ello **la SEXTA CONDICIÓN DE `O18` vuelve a fallar**, por segundo gate consecutivo: el
título de `G-29` promete «*topología y unicidad de TODO el corpus gobernado: sin ampliaciones
sin clasificar … y sin segundas sedes*», y esa comprobación da verde sobre una segunda sede
sin clasificar recién confirmada.

## 3 · LA CIRCULARIDAD SE HA MOVIDO POR QUINTA VEZ, Y `EE` LA LOCALIZA

```text
gates 21-23   estaba en `HEAD`
gate 24       en el EMISOR                     — la cerró `O18`/`O19`
gate 25       en la ENTREGA, el canal humano   — la cerró el sobre a fichero. FUNCIONA
gate 26       en el PERÍMETRO                  — la cerró `DD-01`. FUNCIONA
gate 27       en la GUARDA DE ADMISIÓN, que es el remedio del gate anterior
```

> «Los cinco remedios fueron correctos. Ninguno fue suficiente, **porque cada uno cerró el
> punto donde la circularidad estaba y no la propiedad que la produce**: que la definición de
> QUÉ se verifica y de QUÉ se admite sean objetos del árbol verificado.» — `EE`

Y `EE` precisa lo que eso NO significa: esa propiedad es lo que `O18` contrata para `F6` como
`C`, **pero su manifestación de hoy es `A`**, porque la guarda existe, es interna, y **su
alcance está escrito una zona a la vez en vez de derivado**.

## 4 · LA COBERTURA CIERRA A ∅, Y NO ES UNA DE LAS RAZONES

```text
OBLIGATORIO − ASIGNADO   0   sobre el árbol de la CANDIDATA, en las dos direcciones
ASIGNADO − LEÍDO         0   los dos revisores entregaron manifiesto de TODAS sus fuentes,
                             con rangos cuya unión cubre cada fichero, y `EE` verificó las
                             uniones una a una
```

`C-L.5` **no se reabre por cobertura**. Y `EE` **NO emite la palabra CERTIFICADA**, y dice por
qué: el §6 del manifiesto publica `OBLIGATORIO − ASIGNADO = 1` sobre el árbol del gate y son
**2** —la exención de punto fijo cubre al manifiesto EN CURSO y no al que sustituye—, de modo
que el aparato de cobertura publica un cardinal falso. **Es `EE-02`, y es del aparato, no del
objeto.**

## 5 · LOS DIECINUEVE HALLAZGOS, Y NINGUNA DECISIÓN VUELVE AL OWNER

```text
                 DEL OBJETO   DEL APARATO   DEL SOBRE   TOTAL
  BLOQUEANTE          1             0            0         1
  GRAVE               5             1            0         6
  MEDIO               6             1            0         7
  MENOR               4             0            1         5
                 ──────────────────────────────────────────────
                     16             2            1        19

POR CLASE
  A · coherencia interna, corregible dentro de `F4c`     19
  B · exige una decisión NUEVA del Owner                  0
  C · resistencia a un actor privilegiado, contratada     0
```

`EE` recibió **21 afirmaciones** de los dos revisores, sostuvo **19** y **ninguna cayó**: las
dos que faltan son deduplicaciones que él mismo justifica. Examinó **cuatro candidatos a clase
`B`** y **los cuatro caen**. **Es la TERCERA vez consecutiva que ninguna decisión queda
pendiente del Owner.**

## 6 · LO QUE CONSTA A FAVOR, PORQUE ES VERDAD

```text
· `DD-17` está ROTO, y es la PRIMERA VEZ EN SEIS GATES: el commit del manifiesto deja el
  árbol en 13/13, con `T147` SUPERADA y CERO ficheros de evidencia sucios, en los DOS árboles
· `DD-01` es un ÉXITO y cerró su clase: el perímetro resistió las cinco variantes de ataque
· el SOBRE funciona, y esta vez se midió comparando los tres bloques byte a byte
· las 76 filas del manifiesto casan sin una discrepancia de SHA-256 ni de líneas
· las dos restas de cobertura cierran a ∅, verificadas por el adjudicador
· `X63` NO se presenta como prueba ejecutada ni como certificación presente en ninguna de
  sus ocho sedes
· `DD-06` no amplía la sede canónica del Owner en ninguna de sus sedes
· los censos de `PN`, `X-S`, `X-O`, §15.8, `D1`–`D108`, `O1`–`O19` y la excepción del kernel
  DERIVAN correctos
· el razonamiento de `C-L.5` de la tanda es CORRECTO y NO una evasión: `DD` no escribió
  «CERTIFICADA» ni una sola vez como acto suyo, y la tanda hizo bien en no ponerlo por él
· ninguno de los diecinueve exige arquitectura nueva, y ninguno vuelve al Owner
```

> «**NO falla por la tanda.** La tanda aplicó los remedios que se le ordenaron, con la
> extensión que se le ordenó, y en `DD-17` hizo lo que cinco gates no hicieron. **El defecto
> está en el ALCANCE de un remedio, no en su ejecución.**» — `EE`

## 7 · QUÉ FALLA HOY, EN LAS PALABRAS DEL GATE

> **`A` —COHERENCIA INTERNA— NO ESTÁ DEMOSTRADA.** Sobre el árbol que este gate juzga existe
> hoy un commit ordinario que añade al corpus una segunda sede normativa declarando `F4c`
> cerrada y `F5` autorizada, deja `git status` vacío, pasa **38/38**, no aparece en ninguna
> salida del aparato y produce **el digest que este gate ancla, bit a bit**.

Y la observación de método que `EE` valora por encima de varios hallazgos:

> **Quince de los diecinueve son REINCIDENCIAS, y diez llevan el remedio ya escrito por un
> gate anterior.** La condición de salida que `DD` dejó fijada —«se cierran instancias y no
> clases» pasa a deuda registrada si el perímetro se deriva **y** las promesas dicen lo que el
> código hace— **se cumple en su primera mitad y no en la segunda**.

---

## §A · DICTAMEN DEL REVISOR `R1` — TRANSCRIPCIÓN LITERAL

# INFORME DEL REVISOR INDEPENDIENTE `R1` — SEXTO GATE DE CERTIFICACIÓN DE F4c

Dominio: protocolo · transacciones · recuperación · fuentes de verdad · Git · identidad · pruebas · DERIVADORES.
Contexto limpio. No he escrito nada de este corpus, no he aplicado ninguna corrección, no he participado en gate anterior alguno.
NO he modificado el repositorio: todas mis operaciones son de lectura o sobre copias en `$(mktemp -d)` fuera del árbol auditado.

---

## §0 EL SOBRE

### §0.1 El sobre embebido ENTERO, byte a byte

Fichero: `/tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/f4c/SOBRE-6B.txt`

SHA-256 del fichero del sobre tal como lo recibí: `731c282ac3305827f1e09ee4da0b7dc2f94be824e997d37376497616a0f0554c`
Líneas: 194

```text
SOBRE DE ANCLA · emitido por el coordinador ANTES de crear a ningún revisor
==============================================================================
  REPOSITORIO             git@github.com:JoseLopezGonzalez/ads-kernel.git
  ARBOL DE TRABAJO        `git status --porcelain` VACÍO al emitir, y eso es todo lo
                          que prueba: no había modificaciones VISIBLES para `git
                          status`. Ver la obligación 5 y los SHA-256 del emisor
  TODO LO DE ABAJO SE LEE DE COMMITS con `git show <commit>:<ruta>`. Ni un byte
  del directorio de trabajo de quien emite
------------------------------------------------------------------------------
  REF REMOTA CANDIDATA    refs/heads/review/f4c-clase-cerrada-candidate-20260831
  COMMIT CANDIDATO        b27a761bb3eb6b0b1b3db2344b7184ef4b993309
  ARBOL CANDIDATO         0a0992a3b46dc7fa67f1321a86ac4a9e776e2472
  REF REMOTA DEL GATE     refs/heads/gate/f4c-certificacion-6b-20260831
  COMMIT DEL GATE         ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759
  ARBOL DEL GATE          e945584aa3e52ca44f0ad79e6a235df3b4f63cb5
  RUTA DEL MANIFIESTO     docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md
  SHA-256 DEL MANIFIESTO  41a4ff29d11c1edf26e6370ea7bcf8cf1ee24d75895336d991b6c12fa4251924   (en el commit del gate)
  ASIGNACIONES            19   DERIVADAS de las 16 filas de reparto del manifiesto,
                          no recibidas por parámetro
------------------------------------------------------------------------------
LOS DOS ARBOLES, CADA UNO DERIVADO DE SU PROPIO COMMIT CON SU PROPIO DERIVADOR.
El derivador es FILA DE SU PROPIO UNIVERSO y el commit del gate lo toca: por eso el
sobre publica LOS DOS y no mezcla ni un campo. El gate anterior yuxtapuso el árbol
de la candidata con las cifras del árbol del gate, y eran insatisfacibles.

                          CANDIDATA                                                         GATE
  COMMIT                  b27a761bb3eb6b0b1b3db2344b7184ef4b993309                          ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759
  SHA-256 DEL DERIVADOR   77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b  77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b
  SHA-256 DEL EMISOR      f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715  f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715
  FUENTES OBLIGATORIAS    76                                                                78
  LINEAS OBLIGATORIAS     72592                                                             73164
  DIGEST DEL UNIVERSO     68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b  33c27bd79da8154d1c04edf5df61cd8bfa078a53dc8cfda9316d88725ee6c34c


  SHA-256 DEL EMISOR QUE HA CORRIDO ESTE SOBRE: f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715
  COINCIDE con el del commit del gate. El revisor puede rehacer este contraste:
    git show ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum

  RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: 3
    docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md  AUSENTE → 528dd68fc811
    docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md  AUSENTE → 41a4ff29d11c
    docs/evolucion/00-INDICE.md  6eacea232af0 → ff0a9993c393

LO QUE EL COMPONENTE (iv) DEL DERIVADOR DEJA FUERA DEL UNIVERSO, con su H1, tal como
el derivador de cada commit lo publica. Un universo que encoge lo dice, y lo dice
aqui: un dictamen nuevo cuyo H1 lleve una voz de NO-DICTAMEN sale del universo con
`rc=0`, y el revisor tiene que poder verlo sin ejecutar nada (`Z-08`, `Z-13`).

  ── CANDIDATA
    (iv) EXCLUIDOS por voz de NO-DICTAMEN en su H1: 11
          00-INDICE.md                                   # ADS NEXT — ÍNDICE DE LA INICIATIVA
          01-BASELINE-ADS.md                             # BASELINE — QUÉ ES ADS HOY, COMPROBADO
          02-MAPA-DIRECTIVA.md                           # MAPA — LA DIRECTIVA DEL OWNER CONTRA EL ADS QUE EXISTE
          03-INVARIANTES.md                              # INVARIANTES — LO QUE NO SE MODIFICA EN SILENCIO
          04-PLAN-DE-INVESTIGACION.md                    # PLAN DE INVESTIGACIÓN — QUÉ HAY QUE SABER ANTES DE CERRAR ARQUITECTURA
          05-CANDIDATOS.md                               # INVENTARIO DE CANDIDATOS — MINERÍA DE PROYECTOS REALES
          06-CONTRASTE.md                                # CONTRASTE — LOS 29 CANDIDATOS CONTRA EL CORPUS DE ADS
          07-DECISION-MULTIREPO.md                       # LA DECISIÓN MULTI-REPO — QUÉ CAMBIA, Y LA CONTRADICCIÓN QUE NO PUEDO RESOLVER
          08-EVIDENCIA-MULTIREPO.md                      # 08 — QUÉ ESTÁ DEMOSTRADO DE LA IMPLEMENTACIÓN MULTI-REPO
          09-SINTESIS.md                                 # F3 — SÍNTESIS
          11-ARQUITECTURA-INTEGRADA.md                   # F4 — ARQUITECTURA INTEGRADA
    EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 0

  ── GATE
    (iv) EXCLUIDOS por voz de NO-DICTAMEN en su H1: 11
          00-INDICE.md                                   # ADS NEXT — ÍNDICE DE LA INICIATIVA
          01-BASELINE-ADS.md                             # BASELINE — QUÉ ES ADS HOY, COMPROBADO
          02-MAPA-DIRECTIVA.md                           # MAPA — LA DIRECTIVA DEL OWNER CONTRA EL ADS QUE EXISTE
          03-INVARIANTES.md                              # INVARIANTES — LO QUE NO SE MODIFICA EN SILENCIO
          04-PLAN-DE-INVESTIGACION.md                    # PLAN DE INVESTIGACIÓN — QUÉ HAY QUE SABER ANTES DE CERRAR ARQUITECTURA
          05-CANDIDATOS.md                               # INVENTARIO DE CANDIDATOS — MINERÍA DE PROYECTOS REALES
          06-CONTRASTE.md                                # CONTRASTE — LOS 29 CANDIDATOS CONTRA EL CORPUS DE ADS
          07-DECISION-MULTIREPO.md                       # LA DECISIÓN MULTI-REPO — QUÉ CAMBIA, Y LA CONTRADICCIÓN QUE NO PUEDO RESOLVER
          08-EVIDENCIA-MULTIREPO.md                      # 08 — QUÉ ESTÁ DEMOSTRADO DE LA IMPLEMENTACIÓN MULTI-REPO
          09-SINTESIS.md                                 # F3 — SÍNTESIS
          11-ARQUITECTURA-INTEGRADA.md                   # F4 — ARQUITECTURA INTEGRADA
    EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 0
==============================================================================
LA SEDE CANONICA DE LAS RESOLUCIONES DEL OWNER, QUE `O19` ORDENA ANCLAR AQUI.
`O19` traslada la AUTORIDAD CANONICA de la parafrasis del coordinador a esta sede:
el registro de decisiones pasa a ser una PROYECCION DERIVADA de ella. Todo lo de
abajo se lee DEL COMMIT, no del arbol de trabajo de quien emite.

  RUTA DE LA SEDE         docs/owner/ADS-OWNER-RESOLUCIONES.md
  RESOLUCIONES ANCLADAS   3, DERIVADAS de la sede y no escritas: O17 (85 lineas) · O18 (111 lineas) · O19 (78 lineas)
  EXIGIDAS POR `O19`      O17 · O18 · O19   sin una sola de ellas NO HAY SOBRE

                          CANDIDATA (COMMIT AUDITADO)                                       GATE
  SHA-256 DE LA SEDE      db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a  db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
  DIGEST DE `O17`         0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125  0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125
  DIGEST DE `O18`         ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353  ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
  DIGEST DE `O19`         cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8  cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8

  LOS DOS COMMITS PUBLICAN LA MISMA SEDE, byte a byte.

  RELACION ENTRE RESOLUCIONES, dicha por el Owner y no derivada por el emisor:
    `O19` REVISA LA PROYECCION INCOMPLETA DE `O18`. NO revisa su contenido ni su
    diseño: `O18` NO vuelve a someterse a eleccion. La entrada corta de `O18` en el
    registro de decisiones se conserva como REGISTRO HISTORICO de una transcripcion
    incompleta, y la proyeccion ENLAZA a la sede.

  DECLARACION EXTERNA, que es la razon de que esto viaje en el sobre y no se lea
  del arbol: EL TEXTO ANCLADO ARRIBA ES LA RESOLUCION RATIFICADA POR EL OWNER.
  `O19` ratifica el texto AMPLIO de `O18` —sus tres condiciones obligatorias y su
  reparto— y declara que «la omision esta en la transcripcion del coordinador, no en
  mi resolucion original». A partir de `O19`, lo que una sede derivada rotule como
  literal lo es DE LA SEDE CANONICA, no de la parafrasis.

  COMO SE RECALCULA CADA DIGEST DE RESOLUCION, sobre el COMMIT AUDITADO:

  ── `O17` → 0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125
  git show b27a761bb3eb6b0b1b3db2344b7184ef4b993309:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O17`/)} p' | sha256sum

  ── `O18` → ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
  git show b27a761bb3eb6b0b1b3db2344b7184ef4b993309:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O18`/)} p' | sha256sum

  ── `O19` → cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8
  git show b27a761bb3eb6b0b1b3db2344b7184ef4b993309:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O19`/)} p' | sha256sum

  ── LA SEDE ENTERA → db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
  git show b27a761bb3eb6b0b1b3db2344b7184ef4b993309:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
==============================================================================
  EMITIDO                 2026-08-31 16:44:03 +0200
  EMISOR                  Jose Lopez Gonzalez (jose@congeladosbrisamar.es), coordinador nombrado del sexto gate
  DECISION QUE LO EXIGE   O18 · alternativa (b) · propagada por D108
  ENTREGA                 este sobre se entrega a cada revisor DENTRO de su encargo
                          y ANTES de que empiece a leer. NO se obtiene leyendo el
                          repositorio que se audita
==============================================================================
COMO SE RECALCULA CADA DIGEST, para que el revisor no tenga que fiarse. Reproduce el
digest BYTE A BYTE; si no lo reproduce, el sobre o el árbol están mal, y en ese orden:

  ── ARBOL CANDIDATO → 68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b
  C=b27a761bb3eb6b0b1b3db2344b7184ef4b993309
  d=$(mktemp -d)
  GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
  rm -rf "$d"

  ── ARBOL DEL GATE  → 33c27bd79da8154d1c04edf5df61cd8bfa078a53dc8cfda9316d88725ee6c34c
  C=ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759
  d=$(mktemp -d)
  GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
  rm -rf "$d"
==============================================================================
OBLIGACIONES DEL REVISOR, que son parte del sobre y no cortesía:
  1 RECALCULE LOS DOS DIGEST con la receta de arriba, antes de leer nada. Si uno solo
    no reproduce, el gate es INVALIDO y se dice, sin seguir leyendo.
  2 LEA EL MANIFIESTO EN EL COMMIT DEL GATE, no en el árbol de trabajo, y compruebe
    su SHA-256 contra el de arriba.
  3 CADA FILA DEL MANIFIESTO DECLARA UN ARBOL. Contrástela contra ESE árbol y contra
    ningún otro. La fila del propio derivador es la que el gate anterior falseó dos
    gates seguidos (`U-02`, y su reincidencia `X-06`): mírela primero.
  4 LAS RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN, listadas arriba, son la superficie
    exacta en que la candidata y el gate no son el mismo objeto. Todo lo que el
    manifiesto afirme sobre ellas tiene que decir DE QUE ARBOL habla.
  5 ESTE EMISOR SE NIEGA A EMITIR SI `git status --porcelain` NO VIENE VACIO, y eso
    es TODO lo que esa negativa prueba: que no habia modificaciones VISIBLES para
    `git status` al emitir. NO prueba que el emisor y el derivador que corrieron sean
    los publicados —`git status` compara contra el HEAD LOCAL, y
    `git update-index --skip-worktree` lo vacia con el fichero modificado en disco—.
    LO QUE SI PUEDE COMPROBAR USTED es el SHA-256 DEL EMISOR y el DEL DERIVADOR que
    este sobre publica de los DOS commits: recalculelos con `git show <commit>:<ruta>`
    y contrastelos. `Z-11` midio que la frase anterior —«un sobre existente es, por
    construccion, un sobre limpio»— era falsa, y se retira.
  6 RECALCULE LOS DIGEST DE LA SEDE CANONICA DEL OWNER y contrastelos con toda sede
    derivada que cite una resolucion suya. La AUTORIDAD es la sede; el registro de
    decisiones es una PROYECCION. Una parafrasis que AMPLIE el texto canonico es un
    hallazgo, y `O19` nacio exactamente de uno.
==============================================================================
LO QUE ESTE SOBRE **NO** GARANTIZA, y `O18` lo declara:
  compromiso del canal del Owner · compromiso simultaneo del repositorio y del
  coordinador · robo de credenciales · reescritura autorizada de ramas remotas ·
  manipulacion del ejecutor externo · falsificacion de identidad.
  Esos riesgos son del VERIFICADOR EXTERNO que `O18` contrata para `F6`, y que es
  condicion previa a la adopcion permanente de PesquerApp.
  Y LA SEDE CANONICA DEL OWNER NO ES MECANICAMENTE VERIFICABLE CONTRA UNA FUENTE
  EXTERNA AL SISTEMA, y lo declara el propio Owner. `O19` TRASLADA LA AUTORIDAD de
  la parafrasis del coordinador a `docs/owner/` y este sobre publica su huella, pero
  quien pueda escribir el repositorio puede escribir la sede: lo que el sobre prueba
  es que el texto no ha cambiado entre el commit auditado y lo que el revisor
  recibio FUERA del arbol, NO que sea el que el Owner emitio. Es la limitacion que
  `O18` declara de si misma —garantia TRANSITORIA y LIMITADA— y SIGUE VIGENTE hasta
  el verificador externo real de `F6`.
```

### §0.2 Las SEIS OBLIGACIONES DEL REVISOR, cumplidas con su salida

Entorno declarado y usado en todo el informe:

```
export PYTHONPATH=/tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/py312-libs
export PATH=/tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/bin:$PATH
$ python3 -VV
Python 3.12.14 (main, Aug 25 2026, 14:00:49) [Clang 22.1.3 ]
```

#### OBLIGACIÓN 1 — los DOS digest de universo, recalculados ANTES de leer nada

Ejecuté la receta del sobre, literal, sobre los dos commits.

```
$ git status --porcelain
(vacío)
$ git rev-parse HEAD
ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759
$ git rev-parse b27a761...^{tree}   → 0a0992a3b46dc7fa67f1321a86ac4a9e776e2472   (= sobre L12)
$ git rev-parse ce2cb42...^{tree}   → e945584aa3e52ca44f0ad79e6a235df3b4f63cb5   (= sobre L15)

=== DIGEST ARBOL CANDIDATO ===
68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b  -
=== DIGEST ARBOL DEL GATE ===
33c27bd79da8154d1c04edf5df61cd8bfa078a53dc8cfda9316d88725ee6c34c  -
```

Sobre L32: `68ee8f1b…` / `33c27bd7…`. **LOS DOS REPRODUCEN BYTE A BYTE.** El gate NO es inválido por esta vía.

Nota adicional, contra mi propio interés y a favor del emisor: el sobre (obligación 5) advierte
que `git status` vacío no prueba que no haya modificaciones ocultas por `skip-worktree`. Lo
comprobé yo:

```
$ git ls-files -v | grep -v '^H '
(ninguno: todos H)
```

No hay ni un fichero con bit `S` (skip-worktree) ni `h` (assume-unchanged) en el índice local.

#### OBLIGACIÓN 2 — el manifiesto LEÍDO EN EL COMMIT DEL GATE

```
$ git show ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md | sha256sum
41a4ff29d11c1edf26e6370ea7bcf8cf1ee24d75895336d991b6c12fa4251924  -
```

Sobre L17: `41a4ff29d11c1edf26e6370ea7bcf8cf1ee24d75895336d991b6c12fa4251924`. **CASA.**

Y el manifiesto `6` (el sustituido, que el sobre nombra como ruta que difiere):

```
$ git show ce2cb42…:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md | sha256sum
528dd68fc81134c16f874ab5803996ec50ee838241fd95470a9e07dd66770b2c  -
```

Sobre L40 lo abrevia a `528dd68fc811`; el prefijo de 12 casa (`cut -c1-12` → `528dd68fc811`).

#### OBLIGACIÓN 4 — las rutas en que los dos universos DIFIEREN

Derivé los DOS universos con su propio derivador y los contrasté ruta a ruta y huella a huella:

```
$ diff <(uni b27a761) <(uni ce2cb42)
1c1
< docs/evolucion/00-INDICE.md 6eacea232af0be841614b85b62cc0e212b032a85d275c57d1b1e981db73ef7a6
---
> docs/evolucion/00-INDICE.md ff0a9993c393d39f8adc33c96cde8b73c7d842fb216a2c72b356710e326373f0
31a32,33
> …/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md 528dd68fc811…
> …/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md 41a4ff29d11c…
```

**Exactamente 3 rutas, exactamente las que el sobre L39-L42 publica, con los mismos prefijos de huella.**
Cardinales: 76 rutas en la candidata, 78 en el gate (sobre L30: 76 / 78). **CASA.**

Y el diff COMPLETO entre los dos commits —no sólo el universo— es de SEIS ficheros:

```
$ git diff --name-only b27a761 ce2cb42
docs/evolucion/00-INDICE.md
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md
kernel/operativo/pruebas/evidencia/fuentes-salida.txt
kernel/operativo/pruebas/evidencia/negativos-salida.txt
kernel/operativo/pruebas/evidencia/referencias-salida.txt
```

Las TRES últimas NO están en el universo obligatorio y por tanto NO figuran entre las «rutas en
que los dos universos difieren». Son la evidencia reejecutada del remedio `DD-17` (265→267
documentos analizados en `T147`, 312→314 ficheros en `T161`), consistente con haber añadido dos
manifiestos. Lo consigno porque un revisor que sólo lea la línea «RUTAS EN QUE LOS DOS UNIVERSOS
DIFIEREN: 3» podría creer que los dos commits difieren en tres ficheros, y difieren en seis. El
sobre dice «universos» y es literalmente exacto; la lectura apresurada es mía, no suya.

#### OBLIGACIÓN 5 — SHA-256 del EMISOR y del DERIVADOR en los DOS commits

```
-- b27a761bb3eb6b0b1b3db2344b7184ef4b993309
  emisor    f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715
  derivador 77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b
-- ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759
  emisor    f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715
  derivador 77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b
```

Sobre L28-L29 y L35. **LOS CUATRO CASAN.** El sobre no miente en este campo, y lo que declara que
NO prueba (L167-L175) es correcto y está bien acotado.

#### OBLIGACIÓN 6 — la SEDE CANÓNICA DEL OWNER, recalculada con la receta del sobre

```
-- b27a761… (COMMIT AUDITADO)            -- ce2cb42… (GATE)
  sede  db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a   (idéntico en los dos)
  O17   0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125   85 líneas
  O18   ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353  111 líneas
  O19   cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8   78 líneas
```

Sobre L85 y L89-L92. **LAS OCHO CIFRAS CASAN, y los recuentos de líneas 85·111·78 también.**
Los dos commits publican la misma sede byte a byte, como el sobre afirma en L94.
El contraste contra las sedes DERIVADAS que citan resoluciones del Owner va en §2 y §4.

#### VEREDICTO DEL PASO 0

Las seis obligaciones se cumplen sin una sola discrepancia numérica. **El gate NO es INVÁLIDO
por el sobre**, que es lo contrario de lo que ocurrió en el cuarto. Sigo.

---


---

## §1 MANIFIESTO DE LECTURA

Método: extraje cada fuente **del commit auditado** con
`git show b27a761…:<ruta> > <scratch>/work/<f>` y leí de esa copia; el SHA-256 de la columna
«recalculado» es el de `git show b27a761…:<ruta> | sha256sum`, y el recuento de líneas el de
`| wc -l`. Ninguna huella se abrevia a mano (`DD-22`): donde aparece abreviada va con
`cut -c1-N` o con el comando que la produce.

| # | ruta | líneas | SHA-256 recalculado por mí | rangos leídos | unión | ÍNTEGRO |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11682 | `2d89dbe3725b8487e3d60721ac1f5ebd6704882a7472ce2f8a64daa6d2f06a79` | L1-340 · 341-1100 · 1101-1740 · 1741-2360 · 2361-2980 · 2981-3600 · 3601-4220 · 4221-4820 · 4821-5210 | **[1, 5210]** | **SÍ para mi rango asignado L1–L5200** |
| 2 | `docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md` | 4526 | `e2c34215d92937fb467b1ffdb4e6654f66198ead4dac8128c411469bf86c297e` | (§1.3) | — | **SÍ** |
| 3 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 562 | `02649f623df65e3955a4030831386e01dd3d2e4c20ed05609eb889a1a9caab6a` | L1-170 · 170-420 · 420-562 | [1, 562] | **SÍ** |
| 4 | `docs/evolucion/verificacion/README.md` | 386 | `a3d343f4e155a232c7f751fdac8bafd2e5ed49023a38033762273426c2622930` | L1-120 · 120-225 · 226-240 · 239-252 · 250-386 | [1, 386] | **SÍ** |
| 5 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 3873 | `ec9b948af5a901276dff46c7eff1e54f55e5032de386b78287d747519e87ff1d` | L1-300 · 290-350 · 350-629 · 600-672 · 672-1001 · 1002-1451 · 1452-1911 · 1912-2361 · 2362-2811 · 2812-2891 · 2880-2935 · 2932-2945 · 2940-3075 · 3070-3136 · 3135-3544 · 3545-3754 · 3750-3873 | [1, 3873] | **SÍ** |
| 6 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 787 | `77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b` | L1-200 · 200-470 · 470-787 | [1, 787] | **SÍ** |
| 7 | `docs/evolucion/verificacion/emitir-sobre-de-ancla.py` | 688 | `f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715` | L1-240 · 240-470 · 470-688 | [1, 688] | **SÍ** |
| 8 | `…/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` | 119 | `b1c29244dfedc139ff7e80a6167d200803d054f25554c75f31303fea5687a434` | L1-119 | [1, 119] | **SÍ** |
| 9 | `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` | 240 | `c64a0ec4731e6d27751469e84cbcc33104bfe535c42efe4f98533f4d84a0b970` | L1-240 | [1, 240] | **SÍ** |
| 10 | `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` | 316 | `fc4d1c2fdedbcb13be512e88303e21eddbeb194f6cc38b8e50fa0612dad08bbc` | L1-280 · 281-316 | [1, 316] | **SÍ** |
| 11 | `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md` | 210 | `ac9e0edd59cf3e1b783b42ce0fc052e1eb28af7d5d66e218709d76589f724988` | L1-210 | [1, 210] | **SÍ** |
| 12 | `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md` | 221 | `fc4902591eff43bc6736f626fdf2dd1bef7c4f193b1be31f3ddf26f436adb599` | L1-80 · 80-124 · 125-167 · 168-221 | [1, 221] | **SÍ** |
| 13 | `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md` | 193 | `0f08b961c31f03bbedbae700fa67029ac87b6b962067b39b3e504fe28e8d1939` | L1-100 · 101-154 · 155-193 | [1, 193] | **SÍ** |

**LOS TRECE SHA-256 CASAN CON LOS QUE MI TABLA DE LOTE DECLARA, uno a uno, y los trece
recuentos de líneas también.** Comando:
`while read -r ruta lin sha; do git show b27a761…:$ruta | sha256sum; git show …| wc -l; done`.
Salida: 13 filas «CASA», cero «DISCREPA».

**ANCLAS VERIFICABLES** (dos regiones separadas por fuente, para el documento más largo y el
instrumental, que es lo que mi encargo cubre):

```
doc 11    L376  «# 2 · Disposición física del estado — la primera decisión»
          L5195 «# 5 · Sistema de auditoría y mejora continua»
batería   L1942 `_EXCLUIDO_RAIZ = re.compile(r"^\.git(?:/|$)")`
          L3873 `sys.exit(_informe())`
derivador L165  `_EXCLUIDO_RAIZ = re.compile(r"^\.git(?:/|$)")`
          L787  `sys.exit(main())`
emisor    L130  `SEDE_OWNER = "docs/owner/ADS-OWNER-RESOLUCIONES.md"`
          L688  `sys.exit(main())`
```

**FUENTES QUE ABRÍ PARA VERIFICAR Y QUE NO SON LECTURA ASIGNADA MÍA — declarado como el
encargo manda.** Las abrí acotadas, para reproducir una cifra o una cita, y **NO declaro
lectura íntegra de ninguna**; su lectura íntegra corresponde a `R2`:

```
docs/evolucion/CHECKPOINT-ADS-NEXT.md          la sección «PARTE DE LA TANDA POSTERIOR AL
                                               QUINTO GATE» (L3560-3625) y el barrido de `X63`.
                                               ABIERTA PARA VERIFICAR, no como lectura asignada
docs/evolucion/00-INDICE.md                    L92-96, la fila de la tanda y las dos filas del
                                               sexto gate. ABIERTA PARA VERIFICAR
docs/evolucion/21-…-F4C.md · 22 · 23 · 25 · 26 las LÍNEAS CITADAS por el §5 del manifiesto `6B`,
                                               una por fila, para comprobar la regla 1 del
                                               agotamiento. Lectura ACOTADA a esas 60 líneas
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  no abierta
```

Nota sobre el documento 26: es fuente ASIGNADA a mí y la abro **la última**, como el manifiesto
`6B` fila 3 ordena («los tres · DESPUÉS de las demás fuentes»). Su lectura y su resultado están
en §1.3.

### §1.3 EL DOCUMENTO 26, ABIERTO EL ÚLTIMO

Lo abrí **después** de haber cerrado mi juicio sobre las otras doce fuentes y de haber
ejecutado los diez ataques de §3, como la fila 3 del manifiesto `6B` ordena («los tres ·
DESPUÉS de las demás fuentes»).

```
ruta      docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md
líneas    4526
SHA-256   e2c34215d92937fb467b1ffdb4e6654f66198ead4dac8128c411469bf86c297e   (recalculado por mí)
tramos    L1-490 · L490-1009 · L1010-1569 · L1570-2129 · L2130-2689 · L2690-3249 ·
          L3250-3809 · L3810-4369 · L4370-4526
unión     [1, 4526]     LEÍDO ÍNTEGRO
ancla A   L3662  «# **SÍ. Y ES ESTRICTAMENTE PEOR QUE LOS SIETE ANTERIORES.**»
ancla B   L4524  «# F4c ES INSUFICIENTE PARA F5»
```

**QUÉ CAMBIÓ EN MI JUICIO AL LEERLO, dicho contra mi propio interés.** Tres cosas, y ninguna es
cosmética:

**1 · `R1-01` NO ES UNA CLASE NUEVA: ES `DD-02` LITERALMENTE, UNA ZONA MÁS ALLÁ.** El §4.3 del
documento 26 mide, con estas palabras y estas cifras:

> ```
> docs/owner/SEDE.md  **SIN COMMITEAR**   →  **37/38 · FALLO G-29**   (lo que `CC3` midió)
> docs/owner/SEDE.md  **COMMITEADA**      →  **38/38 EN VERDE**       (nadie lo había medido)
> ```
> «**La guarda de admisión de `G-29` sobre `docs/owner/` … es INERTE sobre cualquier fichero que
> ya esté en `HEAD`.**»

Mi medición de §3.2 es **byte por byte la misma frase**, sobre `docs/normativa/` en vez de sobre
`docs/owner/`: `37/38` sin commitear, `38/38` commiteada. **`DD` diagnosticó la inercia de la
guarda; el remedio que ordenó en su fila `DD-02` la acotó a una zona** —«*que la admisión de
`G-29` **sobre `docs/owner/`** se evalúe contra el CONTENIDO DEL COMMIT*»— y la tanda lo aplicó
**exactamente como se le ordenó**. Eso es justo decirlo, y lo digo. Pero es también, palabra por
palabra, lo que `BB4` diagnosticó en L209-211 y lo que la propia tanda declara haber corregido:

> **`BB4`, doc 26 L209:** «**El sistema cierra INSTANCIAS y no CLASES.** La corrección se aplica
> con la forma sintáctica exacta del contraejemplo, y el defecto reaparece una sede más allá».
>
> **`00-INDICE.md` L94, la fila de esta tanda, en el árbol auditado:** «**CORRECCIÓN POSTERIOR
> AL QUINTO GATE · el perímetro por CONTENIDO, y la CLASE en vez de la instancia**».

**La tanda se rotula a sí misma «la CLASE en vez de la instancia» y cierra `DD-02` como
instancia.** Ése es el peso exacto de `R1-01`, y no lo infla: lo sitúa.

**2 · `DD` MANDÓ BUSCAR EN EL PERÍMETRO, Y EL PERÍMETRO AGUANTÓ.** §10.6, punto 1: «*Que alguien
busque la NOVENA puerta en el mismo sitio que yo: el perímetro. Yo miré una de sus tres
cláusulas. **Nadie ha mirado los enlaces simbólicos, los nombres Unicode confusables, los
submódulos ni los permisos**»*. **Miré los cuatro** (§3, tabla): los símbolicos caen por la
batería, los Unicode caen (aunque por accidente, `R1-09`), no hay submódulos, y los permisos no
sobreviven a `checkout-index`. **El perímetro de `DD-01` está cerrado y hay que decirlo con la
misma fuerza con que digo lo demás.** El noveno árbol salió de otro sitio.

**3 · MI `R1-02` REPRODUCE Y AGRAVA `DD-19`, Y AHORA SÉ POR QUÉ.** `DD-19` dice que
`OBLIGATORIO − ASIGNADO = 0` sobre el árbol del gate es inalcanzable «*en todos los gates
siguientes*», y `DD` corrige a `BB4` en la palabra: «*computacionalmente inalcanzable, no
imposible*». Correcto para el manifiesto EN CURSO. **Lo que ni `DD` ni `BB4` podían prever es
que un gate publicara DOS manifiestos** —el `6` sustituido y el `6B` que se reparte—, y que el
primero **no es un punto fijo de nada**: existe, es inmutable, su SHA-256 es `528dd68f…` y podía
llevar fila. `DD-19` daba la salida correcta —«*publicar las DOS aritméticas*»— y el manifiesto
`6B` la aplicó **copiando el cardinal en vez de derivarlo**.

**LO QUE NO CAMBIÓ.** Nada de lo que ya había medido. Los nueve hallazgos de §2 estaban escritos
antes de abrir el documento 26, y ninguno se apoya en él: los sostengo por mi comando y mi
salida, no por lo que otro gate dijo.


### §1.4 LA RESTA · `ASIGNADO − LEÍDO`

```
ASIGNADO A `R1` por el manifiesto 6B, §4, columna `revisor`:  13 fuentes
   · 11 ÍNTEGRAS  (filas 5,6,7,8,9,10,11,12,13,14,15)
   · 1 POR RANGO  (fila 2, documento 11, L1–L5200)
   · 1 COMPARTIDA (fila 3, documento 26, los tres, DESPUÉS de las demás)

LEÍDO ÍNTEGRAMENTE POR MÍ:  13 de 13

ASIGNADO − LEÍDO = 0
```

Contra mi propio interés, y sin adornarlo:

```
LO QUE ESTA RESTA NO DICE   que yo haya leído el documento 11 ENTERO. Mi rango es L1–L5200 de
                            11682, y **L5201–L11682 NO los he leído**: son de `R2`. Una
                            contradicción entre §2.6 y §11.6 —o entre §5.2 y §17— es
                            estructuralmente invisible para mí, y lo digo aquí y no en una nota
                            al pie. El propio manifiesto lo declara en su L106: «ningún ojo
                            único recorre esas 11682 líneas seguidas»
LO QUE TAMPOCO DICE         que haya leído la sección `C-L.5` · `1bis`, que vive en L11515 del
                            documento 11 — **fuera de mi rango**. La he abierto para VERIFICAR
                            el derivador contra su sede, y así lo declaro, pero su lectura
                            íntegra es de `R2`
LO QUE SÍ DICE              que las 13 fuentes que el manifiesto me asigna están leídas de
                            principio a fin en la parte que me asigna, con su SHA-256
                            recalculado por mí sobre el commit auditado y con sus rangos
                            publicados arriba para que cualquiera los recomponga
```

---

## §2 HALLAZGOS QUE SOSTENGO

Clases: **A** = defecto de coherencia interna del corpus o del instrumento, cerrable sin
decisión del Owner · **B** = exige una decisión del Owner · **C** = actor privilegiado,
**NO exigible en `F4c`** por `O18`, y ninguno de los míos lo es.

| id | sev | clase | sede (fichero:línea) | qué afirma la sede | qué dice el árbol (comando y salida) | qué se sigue |
|---|---|---|---|---|---|---|
| **`R1-01`** | **BLOQUEANTE** | **A** | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` **L3038** (`_nuevos = sorted(f for f in _disco - _publicado …)`) y **L3107-3118** (unicidad 2), con su título en **L3120** y su fila del README en **L244** | Título de `G-29`: «topología y unicidad de TODO el corpus gobernado: **sin ampliaciones sin clasificar**, sin gemelos y **sin segundas sedes**». README L244: «**Ninguna ampliación sin clasificar**, ningún gemelo byte a byte, y ningún marcador de bloque canónico … con sedes nuevas». `DD-02` (L3046-3060) declara cerrado que la guarda «era INERTE sobre todo fichero ya en `HEAD`» | **Los DOS controles siguen siendo inertes sobre lo commiteado fuera de `docs/owner/`.** Reproducido con el contraejemplo LITERAL del cuarto gate: `docs/normativa/C8-SEGUNDA-SEDE-NORMATIVA.md`, que declara contradecir a `C4` y `C7` y prevalecer sobre los dos, **con un bloque `ads:proceso` dentro**. `SIN COMMITEAR → 37/38 FALLO G-29 · AMPLIACIÓN NO CLASIFICADA`. `git add -A && git commit` → `git status --porcelain` VACÍO · **`38/38 comprobaciones en verde`** · `derivar-…py --rutas \| wc -l → 76` (universo INTACTO) · RECETA DEL SOBRE → `68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b`, **BIT A BIT el digest anclado**. Segunda variante, `docs/normativa/ADS-SENTENCIA-DE-CIERRE-F4C.md` («PREVALECE SOBRE TODO … `F4c` CERRADA y `F5` AUTORIZADA»): idéntico resultado | **ES EL NOVENO ÁRBOL, y es de clase `A`.** Cumple las seis condiciones que el quinto gate exigió al octavo: alcanza el commit · `git status` vacío · **38/38** · fuera del universo · sin fila de manifiesto ni revisor · digest del sobre idéntico. `DD-02` cerró la INSTANCIA (`docs/owner/`) y dejó la CLASE abierta: es exactamente el diagnóstico de `BB4` —«el sistema cierra INSTANCIAS y no CLASES»— reproducido en el remedio que decía haberlo curado. Y el título de `G-29` y la fila L244 del README son, hoy, **afirmaciones falsas del instrumento** |
| **`R1-02`** | **GRAVE** | **A** | `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md` **L222-230**, §6, bloque «SOBRE EL ÁRBOL DEL GATE — `DD-19`» | «`OBLIGATORIO menos ASIGNADO  1` … **la fuente que sobra es ESTE manifiesto** … Cerrarla a cero exigiría que este fichero contuviera su propio SHA-256. **No es un defecto de esta tanda: es una propiedad del corpus**» | `comm -23 <(rutas del universo del gate) <(las 76 rutas del manifiesto)` → **2**, no 1: `…-6-20260831.md` **y** `…-6B-20260831.md`. La primera es el manifiesto SUSTITUIDO, **278 líneas**, `528dd68fc81134c16f874ab5803996ec50ee838241fd95470a9e07dd66770b2c` — un fichero DISTINTO, cuyo SHA-256 es perfectamente escribible y al que **nada le impide tener fila**. El universo del gate son 78 fuentes y el manifiesto tiene 76 filas | La cifra está **entendida en uno**, y la justificación de punto fijo **no cubre** a la fuente que falta. Es la cifra que `DD-19` creó para no volver a mentir sobre el árbol del gate, y es errónea en su primer uso. **La causa es mecánica**: se copió el «1» de la entrada §15 del CORRIGENDUM —donde ERA correcto, porque el quinto gate publicó UN manifiesto— sin volver a derivarlo sobre un gate que publica DOS. El §16 del propio CORRIGENDUM lo prohíbe con estas palabras: «**TODA CIFRA … VA CON SU COMANDO** … Ninguna se copia». Consecuencia material: **una fuente obligatoria de 278 líneas del árbol del gate no está asignada a nadie**, y ninguna sede lo dice |
| **`R1-03`** | **MEDIO** | **A** | el mismo manifiesto `6B`, **L142-145**, preámbulo del §5 | «ESTE MANIFIESTO APLICA LA REGLA MÁS ESTRICTA QUE EL ÁRBOL SOSTIENE: una fuente sólo se agota si **su SHA-256 de HOY coincide byte a byte con el que publicó el gate que la certificó**» | Abrí las 60 líneas citadas. **51 de 60** publican el SHA-256 completo e idéntico. **5** lo publican truncado a 16 hex —filas 13, 14, 55, 56, 57—, y son prefijo correcto (verificado con `cut -c1-16`: `0f81f13d8cb319d8`, `8df584529c857c07`, `315b2790cb66bb4c`, `750d39a29f05e7f2`, `1716bd3d8b48107d`). **2** publican un **blob id de Git** y no un SHA-256 —filas 18 y 19, doc 26 L1972-1973: `24da5be1…` y `b0766d5d…`, que `git ls-tree 8c9ca9c` confirma como los blobs—. Y **2 no publican NINGUNA huella**: fila 15 (doc 26 L1978, columna «—») y fila 16 (doc 22 L2642, cuya tabla no tiene columna de huella) | La regla LITERAL que el manifiesto se atribuye **es insatisfacible para 2 de sus 60 filas** y sólo satisfacible con otra función hash o con 16 hex para 7 más. **La cobertura NO está rota**: verifiqué las 60 contra el árbol que cada una cita y la regla 2 real —«los BYTES idénticos a los del árbol que ESE gate leyó»— se cumple en las 60, con 0 incumplimientos. Lo que falla es **la descripción que el manifiesto hace de su propio rigor**, que es la clase exacta que la entrada §5 del CORRIGENDUM ya acotó para el `ADDENDUM 1` — y que aquí reincide en un manifiesto nuevo |
| **`R1-04`** | **MEDIO** | **A** | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` **L131-137** (`_leer`), contra su cabecera **L52-58** | «**FALLA CERRADO** — Si una sede no se puede leer … **sale con código 2 y diagnóstico**. Nunca adivina … **Y eso se EJECUTA, no se promete**» | `_leer()` es `except OSError as e: raise SedeIlegible(...)`. Una sede que exista y **no sea UTF-8** lanza `UnicodeDecodeError`, que es `ValueError` y **no** `OSError`: sale sin capturar, con **traza y código 1**, sin la línea `FALLA CERRADO ·`. Contraste directo: la batería, en la MISMA situación, sí la captura —`_motivo_ilegible`, batería L63: `except UnicodeDecodeError: return "no es UTF-8"`— | El derivador promete un modo de fallo que **una de sus lecturas no ejecuta**, y es **la misma clase que `T-22` cerró en el fichero de al lado**: «la única rama del derivador que existe para fallar cerrado era la única que no fallaba cerrado». Hoy es LATENTE —no hay ninguna sede no-UTF-8— y por eso no es GRAVE; pero el `rc=1` que produciría hace que la RECETA del sobre, que canaliza `2>/dev/null`, entregue una lista de rutas VACÍA y un digest de la cadena vacía sin decir por qué |
| **`R1-05`** | **MENOR** | **A** | `docs/evolucion/verificacion/emitir-sobre-de-ancla.py` **L217-222** | «`git read-tree` … y `git checkout-index -a --prefix` materializan **el árbol del commit y nada más** —**no consultan `.gitattributes`** y no pueden honrar `export-ignore`—» | **MEDIDO, y la primera mitad es falsa.** Con un `.gitattributes` commiteado que dice `docs/owner/ADS-OWNER-RESOLUCIONES.md text eol=crlf`: `grep -c $'\r'` sobre el blob → **0**; sobre el fichero materializado por `read-tree`+`checkout-index` → **334**. `sha256sum` del blob `db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a`; del materializado `31d8b08b059377dcbf158764e3ee109740d94f38325c67a296e7bc7e5f52c4a6` | `checkout-index` **sí** consulta `.gitattributes`. La segunda mitad —«no pueden honrar `export-ignore`»— es cierta, y el remedio de `Z-04` se sostiene; lo que sobra es la generalización. Queda abierta una divergencia estructural que el sobre no acota: **el derivador VE el árbol materializado y el digest MIDE el blob**, de modo que `.gitattributes` puede separarlos. **No he conseguido armar un ataque con ella** y lo digo: el árbol no tiene ningún `.gitattributes` (`git ls-files '.gitattributes' '*/.gitattributes'` → vacío) y las conversiones que Git admite sin configuración local no alcanzan la cabecera de 4 bytes que `_es_bytecode` exige |
| **`R1-06`** | **MENOR** | **A** | emisor **L275** frente a derivador **L719-722** (`metricas`) | Las dos sedes cuentan «líneas» de la misma fuente: el sobre publica `LINEAS OBLIGATORIAS` y el manifiesto publica la columna `líneas` | Emisor: `crudo.count(b"\n") + (0 if crudo.endswith(b"\n") else 1)`. Derivador: `n = crudo.count(b"\n"); if crudo and not crudo.endswith(b"\n"): n += 1`. **Divergen en el fichero VACÍO**: emisor **1**, derivador **0**. Comprobado ejecutando las dos funciones sobre `b""`, `b"a"`, `b"a\n"`, `b"a\nb"`: sólo el vacío diverge | Dos sedes de la misma derivación que no coinciden en un caso. **LATENTE**: `git ls-tree -r -l b27a761 \| awk '$4==0'` → **0 ficheros vacíos** en todo el árbol. Si mañana entra uno en el universo, el `LINEAS OBLIGATORIAS` del sobre y el total del manifiesto diferirán en 1 y ninguna comprobación lo dirá |
| **`R1-07`** | **MENOR** | **A** | batería **L1897-1903** (`tocados = _tocados_raw.split()`, `_mod_head = set(_mod_head_raw.split())`, `_head_arbol = set(_head_arbol_raw.split())`) | Es la sede única de la que salen `_publicado`, `_INMUTABLES` y los tres contrastes contra `HEAD` y contra la base | `git ls-tree -r --name-only` separa rutas por **salto de línea**, no por espacios. `.split()` sin argumento parte por CUALQUIER blanco, luego una ruta del corpus con un espacio se convierte en **dos entradas falsas** en `_publicado` | El discriminante que gobierna «qué está publicado» **no deriva de la salida real de Git** para una clase de nombres. **Falla LOUD** —la ruta real aparece en `_nuevos` y los dos fragmentos en `_idos`, los dos en ROJO—, luego no es una puerta; pero es un defecto de derivación en la sede de la que todo lo demás cuelga. LATENTE: `git ls-tree -r --name-only b27a761 \| grep -c ' '` → **0** |
| **`R1-08`** | **MENOR** | **A** | batería **L337** (`_con_git = [i for i, t, _, _ in RES if "sin git" in t]`) y README **L63-65** | «El censo NO se escribe aquí: la batería lo **DERIVA de los títulos** de sus propias comprobaciones» | Cierto, y **la medición coincide exactamente**: 9 rojas sin `.git`, las nueve nombradas, 29 verdes (§3.4). Pero el discriminante es la **subcadena `"sin git"` en el título**: una comprobación que exija historia y cuyo título no la lleve queda mal contada, y **eso ya pasó** — `DD-21` existe porque `G-34` era «la NOVENA … sin declararlo» | Es DERIVACIÓN sobre una **convención de redacción**, no sobre la propiedad. Hoy no hay discrepancia y por eso `DD-21` no cae; lo consigno como fragilidad de la misma familia que el resto del expediente y no como falsedad presente |
| **`R1-09`** | **MEDIO** | **A** | batería **L1902-1903** (`_head_arbol = set(_head_arbol_raw.split())`) y su uso en **L3060** (`_owner_publicado`) y **L2088** (`_INMUTABLES`) | `_publicado` es «el conjunto publicado del corpus», derivado de `git ls-tree -r --name-only HEAD`, y de él cuelgan `G-22`, `G-28`, `G-29` y la guarda `DD-02` | **`git ls-tree --name-only` CITA Y ESCAPA toda ruta no-ASCII**, porque `core.quotePath` vale `true` por defecto y el árbol no lo fija (`git config --get core.quotePath` → sin valor). Medido, plantando `docs/normativa/SEDE-VIGENTE-е.md` (con `е` cirílica U+0435): `git ls-tree -r --name-only HEAD` devuelve `"docs/normativa/SEDE-VIGENTE-\320\265.md"` —con comillas y octales—, y `git -c core.quotePath=false ls-tree …` devuelve la ruta real. Salida de la batería: `FALLO G-29 └─ AMPLIACIÓN NO CLASIFICADA …: docs/normativa/SEDE-VIGENTE-е.md; fichero del corpus **DESAPARECIDO**: "docs/normativa/SEDE-VIGENTE-\320\265.md"` | La misma ruta produce **dos diagnósticos, uno de ellos FALSO**: declara DESAPARECIDO un fichero que existe. Y las consecuencias silenciosas importan más: la cadena citada **no empieza por `docs/owner/`** —empieza por `"`—, de modo que **una ruta no-ASCII bajo `docs/owner/` NO entraría en `_owner_publicado`, que es exactamente el bucle de `DD-02`**, ni en el contraste de `_INMUTABLES` contra `HEAD`. Hoy es LATENTE —`git ls-tree -r --name-only b27a761 \| grep -c '^"'` → **0**— y por eso no es GRAVE. El remedio es `-z` o `core.quotePath=false`, y es de la misma familia que `R1-07` |

**RECUENTO, derivado de las filas de arriba y no escrito:**

```
BLOQUEANTE   1     R1-01
GRAVE        1     R1-02
MEDIO        3     R1-03 · R1-04 · R1-09
MENOR        4     R1-05 · R1-06 · R1-07 · R1-08
             ─
             9

POR CLASE    A 9  ·  B 0  ·  C 0
```

**NINGUNO DE LOS NUEVE ES DE CLASE `C`**, y lo digo expresamente porque el encargo lo exige:
ninguno requiere reescribir `HEAD`, ni las refs, ni la revisión base, ni editar la batería o su
README, ni mentir el runner. `R1-01` se construye con `git add -A` y `git commit` **sin un solo
flag**, que es el acto ordinario del autor de una tanda en su propia rama — y es la formulación
de clase que `DD` fijó en su `D-3` contra la sede canónica y que `DD-20` manda escribir.

**NINGUNO ES DE CLASE `B`.** Los nueve se cierran con material que el corpus ya tiene escrito, y
ninguno reinterpreta `O17`, `O18` ni `O19`. **No formulo ninguna pregunta al Owner.**

---


---

## §3 ATAQUES EJECUTADOS Y SUS SALIDAS

**Disciplina del banco de pruebas.** No he tocado el repositorio auditado. Todo ataque se
ejecuta sobre `git clone /home/jose/ads-kernel <scratch>/atk/clone`, en `HEAD` desprendido en
`b27a761…` (la CANDIDATA), y entre ataque y ataque se restaura con
`git checkout -q -f b27a761… && git clean -qfdx`. Verificación final del repositorio auditado
al cierre del informe, en §4.

Línea base del banco, para que todo lo de abajo sea contrastable:

```
$ cd <atk>/clone && git rev-parse HEAD
b27a761bb3eb6b0b1b3db2344b7184ef4b993309
$ python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py --rutas   → rc=0 · 76 rutas
$ (digest de la receta sobre el árbol de trabajo)                               → 68ee8f1b…  = el ANCLADO
```

### §3.1 EL NOVENO ÁRBOL · variante A — directorio SIMBÓLICO dentro de una ZONA DEL ENCARGO

**Hipótesis.** `_barrer()` (derivador L536-551) y `_ficheros_zona()` (batería L2920-2930) recorren
el árbol con `os.walk(...)`, cuyo `followlinks` por defecto es `False`. Un enlace simbólico a
DIRECTORIO se clasifica en `dirs` —`entry.is_dir()` sigue el enlace— y NO se desciende. Su
contenido es, por construcción, invisible para los dos instrumentos, y `_excluido()` nunca se
llama sobre él: no puede salir en `EXCLUIDOS_PERIMETRO`.

```
$ mkdir -p docs/owner-anexos
$ cat > docs/owner-anexos/ADS-OWNER-SENTENCIA-DE-CIERRE.md   # «declaro F4c CERRADA y F5 AUTORIZADA»
$ ln -s ../owner-anexos docs/owner/ANEXOS
$ git add -A && git commit -m "docs(owner): anexos del Owner"      → eb7d030
$ git status --porcelain                                           → VACÍO
$ head -3 docs/owner/ANEXOS/ADS-OWNER-SENTENCIA-DE-CIERRE.md
# `O20` — RESOLUCIÓN DEL OWNER · CIERRE DE `F4c` Y AUTORIZACIÓN DE `F5`
$ git ls-files -s docs/owner
120000 2bbc66b… 0  docs/owner/ANEXOS
```

DERIVADOR — **completamente ciego**:

```
$ python3 …/derivar-universo-obligatorio.py --rutas          → rc=0, 76 rutas
$ diff base-rutas.txt A-rutas.txt                            → (SIN DIFERENCIA)
  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 1
        .git/                    `.git` de la RAÍZ: almacén, no corpus
$ grep -c -i 'anexo\|sentencia'  en rutas y en stderr        → 0 y 0
```

DIGEST por la RECETA DEL SOBRE, sobre el commit atacado:

```
68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b  -
ANCLADO EN EL SOBRE PARA LA CANDIDATA: 68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b
  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 0    ← el sobre saldría IDÉNTICO
```

BATERÍA — **y aquí el ataque CAE**:

```
$ python3 …/comprobar-correccion-gate-de-cierre.py           → rc=1, 37/38
FALLO G-29 └─ SEGUNDA SEDE EN `docs/owner/`, YA CONFIRMADA EN `HEAD` y SIN ENLACE desde
              `00-INDICE.md`: docs/owner/ANEXOS. […] ; fichero del corpus DESAPARECIDO: docs/owner/ANEXOS
```

**RESULTADO: ataque FALLIDO, y la información que deja es la que importa.** El DERIVADOR es
ciego a la clase entera —universo idéntico, digest bit a bit idéntico, `EXCLUIDOS_PERIMETRO` en
cero— y quien lo caza es la BATERÍA, y sólo porque el enlace cae DENTRO de `docs/owner/`, la
única zona a la que `DD-02` llegó. `_ENLAZADOS_INDICE_OWNER` (batería L2968-2971) exige que la
ruta acabe en `.md`, de modo que un enlace llamado `ANEXOS` no puede admitirse nunca: la
denuncia es robusta para esta zona. Eso me llevó a mirar la zona de al lado.

### §3.2 EL NOVENO ÁRBOL · variante D — SEGUNDA SEDE NORMATIVA COMMITEADA FUERA DE `docs/owner/`

**Hipótesis, leída del código y no adivinada.** `G-29` calcula
`_nuevos = sorted(f for f in _disco - _publicado if not _ampliacion_admitida(f))`
(batería L3038). `_ampliacion_admitida()` **sólo se consulta para lo que NO está en `HEAD`**.
`DD-02` corrigió eso añadiendo un segundo bucle —`_owner_publicado`, L3060-3069— que reevalúa la
admisión sobre `git ls-tree -r HEAD docs/owner/`. Ese bucle está acotado a `docs/owner/` y a
ninguna otra zona. Luego, para TODO el resto del «corpus gobernado» —que el README declara que
es el repositorio entero—, la guarda sigue siendo **inerte sobre cualquier fichero ya
commiteado**.

```
$ git checkout -f b27a761 && git clean -fd
$ mkdir -p docs/normativa
$ cat > docs/normativa/ADS-SENTENCIA-DE-CIERRE-F4C.md <<'X'
# SENTENCIA DE CIERRE DE `F4c` — PREVALECE SOBRE TODO

Esta sede **PREVALECE SOBRE TODO** el corpus. Declara **`F4c` CERRADA** y
**`F5` AUTORIZADA**. La condición de cobertura `C-L.5` queda sin efecto y
ningún gate de certificación posterior es exigible.
X
$ git add -A && git commit -m "docs: sentencia"        → 7938fc9
$ git status --porcelain                               → VACÍO
```

```
$ python3 …/derivar-universo-obligatorio.py --rutas    → rc=0
$ diff base-rutas.txt D-rutas.txt                      → UNIVERSO IDÉNTICO (76 rutas)
  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 1  (sólo `.git/`)

$ python3 …/comprobar-correccion-gate-de-cierre.py     → rc=0
  (NINGÚN FALLO)
  38/38 comprobaciones en verde

$ (RECETA DEL SOBRE sobre el commit atacado)
68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b  -
ANCLADO: 68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b
```

Y LA MITAD QUE LO IDENTIFICA COMO LA MISMA CLASE QUE `DD-02`, **el mismo fichero, byte a byte**:

```
##### SIN COMMITEAR #####
FALLO G-29 └─ AMPLIACIÓN NO CLASIFICADA del corpus gobernado, rastreada o no:
              docs/normativa/ADS-SENTENCIA-DE-CIERRE-F4C.md. […]
37/38 comprobaciones en verde

##### COMMITEADO #####
38/38 comprobaciones en verde
```

**RESULTADO: ATAQUE CONSUMADO. Es el NOVENO ÁRBOL.** Cumple una a una las condiciones que el
quinto gate exigió al octavo: alcanza el commit · deja `git status` vacío · pasa **38/38** ·
no entra en el universo · no recibe fila de manifiesto ni revisor · no aparece en
`EXCLUIDOS_IV` ni en `EXCLUIDOS_PERIMETRO` · y **produce el digest que el sobre ancla, BIT A
BIT IDÉNTICO**. Va como `R1-01`, BLOQUEANTE, en §2.

### §3.3 `DD-11` · ¿sigue siendo tautológico el mutante? — ATAQUE DE FALSABILIDAD

La aserción viva es `_fase0_conforme(_b_mutilado) == [_FALTA_CONTRATO]` (batería L3781): se
mutan las líneas de §8.1 que contienen `gate:sistema-conforme` y se exige que la denuncia sea
EXACTAMENTE una y sea la suya. Medí los seis predicados de `_fase0_conforme()` contra §8.1 real
(L6555-L6743 del documento 11) para localizar el predicado más frágil:

```
predicado      nº de líneas de §8.1 que lo satisfacen   ¿todas llevan la cadena gatillo?
FASE 0          6   [6560,6562,6581,6624,6626,6629]      no
contrato        2   [6564, 6626]                         SÍ
Estructural     2   [6560, 6629]                         no
antes-mut       1   [6563]                               no    ← el frágil
BLOQUEA         3   [6566,6607,6623]                     no
no-heredada     2   [6560, 6629]                         no
```

`antes-mut` se sostiene sobre UNA SOLA línea, la 6563, **pegada a una línea gatillo (6564)**.
Falsación ejecutada — cambio de UNA línea del CORPUS, ni una del instrumento:

```
$ # L6563: se le añade la cadena gatillo al final
  «… ANTERIOR a toda mutación canónica y a todo intento de (`gate:sistema-conforme`)»
$ python3 …/comprobar-correccion-gate-de-cierre.py
FALLO G-33    los macrocircuitos DERIVADOS producen su Estructural en FASE 0; sus pruebas
              negativas ANCLADAS EN EL ÁRBOL y sus fixtures del evaluador se cuentan POR SEPARADO…
37/38 comprobaciones en verde
```

**`DD-11` SE SOSTIENE.** La prueba negativa es hoy genuinamente CONTINGENTE del árbol: un corpus
una línea distinto la pone en rojo sin que nadie la ataque, que es literalmente lo que el README
promete de ella. Ya no es el fixture sintético disfrazado que `DD` midió con 200 000 textos
aleatorios. No cae.

### §3.4 `DD-21` · el ALCANCE publicado, contra la medición real sin `.git`

El ALCANCE **se DERIVA**, no se escribe: `_con_git = [i for i, t, _, _ in RES if "sin git" in t]`
(batería L337). Medición sobre árbol materializado con la receta del sobre, SIN `.git`:

```
$ d=$(mktemp -d); GIT_INDEX_FILE=$d/idx git read-tree b27a761
$ GIT_INDEX_FILE=$d/idx git checkout-index -a --prefix=$d/t/
$ ls -a $d/t   →  .gitignore README.md START_HERE.md docs kernel packs tooling   (sin .git)
$ (cd $d/t && python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py)
29/38 comprobaciones en verde
FALLOS: G-11 G-11b G-21 G-22 G-23 G-28 G-29 G-30 G-34   (recuento: 9)
ALCANCE (`DD-21`): 9 de las 38 … — G-11, G-11b, G-21, G-22, G-23, G-28, G-29, G-30, G-34.
                   Las otras 29 son propiedades del ÁRBOL DESNUDO … el máximo alcanzable es 29.
```

**`DD-21` CASA EXACTAMENTE**: 9 rojas, las nueve nombradas y ninguna más, y 29 verdes, que es el
máximo que publica. No cae. Lo único que anoto —y es fragilidad, no falsedad— va como `R1-06`.

### §3.5 LOS CUATRO CONTROLES POSITIVOS, REPRODUCIDOS

**`DD-01`** · documento con NOMBRE de bytecode bajo `docs/owner/`, con texto plano dentro, **que
alcanza el commit de verdad**. Aviso metodológico: `.gitignore` L2 es `*.pyc`, de modo que un
`git add -A` NO lo añade y el ataque se queda sin commitear sin que nadie lo note; hay que usar
`git add -f`. Lo hice:

```
$ printf '# SENTENCIA DEL OWNER — `F4c` CERRADA y `F5` AUTORIZADA\n…' > docs/owner/sentencia.pyc
$ git add -f docs/owner/sentencia.pyc && git commit -m sentencia
$ git ls-tree -r HEAD --name-only | grep pyc   → docs/owner/sentencia.pyc
$ git status --porcelain                       → VACÍO
$ python3 …/comprobar-…py   → 37/38 · FALLO G-29
   └─ SEGUNDA SEDE EN `docs/owner/`, YA CONFIRMADA EN `HEAD` Y SIN ENLACE desde `00-INDICE.md`:
      docs/owner/sentencia.pyc …—`DD-02`—…
$ python3 …/derivar-…py --rutas | wc -l        → 77      (era 76)
$ …                                            → docs/owner/sentencia.pyc   ENTRA EN EL UNIVERSO
$ (RECETA)  1b996d67c8beb24756ea4fb30cba45cf315f25fe4ab9362021f5a387383fec38
   ANCLADO: 68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b   ← EL DIGEST CAMBIA
```

Y la otra mitad, el bytecode DE VERDAD, excluido por CONTENIDO y **publicado con su ruta**:

```
$ py_compile → docs/owner/real.pyc   (cabecera b'\xcb\r\r\n')
  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 2
        .git/                 `.git` de la RAÍZ: almacén, no corpus
        docs/owner/real.pyc   bytecode de CPython, por CONTENIDO
```

**`DD-01` reproduce en sus dos mitades y es CONTINGENTE.** El octavo árbol está cerrado.

**`DD-02`** · reproducido dentro de `DD-01` arriba: la segunda sede COMMITEADA en `docs/owner/`
da hoy `37/38` con su ruta nombrada, y el quinto gate la midió en `38/38`. **Reproduce, y es
contingente** — pero sólo para `docs/owner/`: véase §3.2.

**`DD-04`** · `docs/rediseno/00-MAPA.md` reescrito declarando que prevalece y deja `O17`·`O18`·
`O19` sin efecto, **commiteado**:

```
$ python3 …/comprobar-…py   → 37/38
FALLO G-23  lo normativo intacto y la excepción del kernel contrastada contra la prosa del checkpoint
            └─ docs/rediseno/00-MAPA.md
```

**Reproduce y es contingente**: la zona se deriva de `docs/rediseno/` en `HEAD`, no de un regex
de seis patrones; un fichero nuevo en esa zona nace protegido.

**`DD-12`** · una SÉPTIMA extensión de ficha añadida a la enumeración de §5.2:

```
$ (§5.2 enumera hoy 6: ENT ARQ PLT SEG DSP ENC → se le añade `capacidades/ZZZ/`)
$ python3 …/comprobar-…py   → 37/38   (sólo G-10)
FALLO G-10 └─ §5.2: su enumeración da 7 fichas (ENT, ARQ, PLT, SEG, DSP, ENC, ZZZ) y su titular
              no dice «Son SIETE»; §16: no dice «SIETE» sobre un censo derivado de 7; §16: no
              nombra `ZZZ`; §17: escribe `+6` y el censo derivado de §5.2 da 7; §17: no nombra `ZZZ`
```

**Reproduce, y es el más limpio de los cuatro**: ROJO en las TRES sedes a la vez, nombrando la
ficha, con una sola comprobación caída y ningún cardinal escrito en el código.

**Conclusión sobre la pregunta que se me hizo** —«¿son de verdad contingentes del árbol, o son
tautológicos como lo era el de `DD-11`?»—: **los cuatro son contingentes del árbol y ninguno es
tautológico.** Los cuatro caen a mi favor en §4, no en §2.

### §3.6 EL MANIFIESTO · obligación 3, fila a fila, contra el árbol que cada fila declara

El manifiesto `6B` rotula sus dos tablas «SOBRE EL ÁRBOL DE LA CANDIDATA» (§2 L59, §6 L214).
Contrasté las **76 filas** —§4 y §5 juntas— contra ESE árbol y contra ningún otro:

```
$ (extraer las 76 filas del manifiesto en el commit del gate, y para cada una
   git show b27a761:<ruta> | sha256sum   y   | wc -l)
DISCREPANCIAS: 0
```

**Y LA FILA DEL PROPIO DERIVADOR, que el sobre manda mirar PRIMERO** (`U-02`, reincidencia
`X-06`, tercera instancia `DD-18`): fila 8, `derivar-universo-obligatorio.py`, **787 líneas**,
`77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b`. Casa contra el árbol de la
candidata **y** contra el del gate —el gate no tocó el derivador— y casa con los dos campos del
sobre. **La clase `U-02`→`X-06`→`DD-18` NO reincide en este manifiesto.**

Y el conjunto de filas ES el universo, no un subconjunto elegido:

```
$ diff <(las 76 rutas del manifiesto, ordenadas) <(derivador --rutas sobre b27a761, ordenado)
  IDENTICO
$ (suma de la columna «líneas»)   76 filas → 72592 · filas 1-16 → 29855 · filas 17-76 → 42737
  manifiesto L215-217 declara     72592 · 29855 · 42737
```

**Las tres aritméticas del árbol candidato derivan sin residuo.**

### §3.7 EL AGOTAMIENTO de las 60 fuentes · regla 1 y regla 2 del §5

REGLA 2 —bytes idénticos a los del árbol que ESE gate leyó— contrastada en las 60:

```
$ para cada fila: git show <árbol citado>:<ruta> | sha256sum  ==  SHA declarado ?
INCUMPLIMIENTOS REGLA 2: 0
```

REGLA 1 —fila propia con `LEÍDO ÍNTEGRO`, citada con documento y línea— abriendo las 60 líneas
citadas:

```
INCUMPLIMIENTOS REGLA 1: 0
```

Muestra de lo que hay en las líneas citadas, para que conste que son FILA PROPIA y no una
declaración de conjunto:

```
doc 22 L1583  | 12 | `docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md` | 336 | `202ac1af…` | `Q3` | **LEÍDO ÍNTEGRO** |
doc 21 L381   | 2 | `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` · 1257 · `8243034f…` | **LEÍDO ÍNTEGRO** | …
doc 25 L1735  | 15 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 334 | `db46edd2…` | **LEÍDO ÍNTEGRO** L1-L334 |
```

**Las dos reglas se cumplen en las 60.** Lo que NO se cumple es la formulación MÁS ESTRICTA que
el propio §5 se atribuye (L142-145) — va como `R1-03` en §2.

### §3.8 EL CORRIGENDUM §14 y §15, REPRODUCIDOS

§14 (`DD-18`) publica: candidata `8c9ca9c` → 74 fuentes · 66 747 líneas; gate `5ed7a3b` → 75 ·
66 940; diferencia +1 fuente · +193 líneas, y la fuente que falta es el manifiesto en curso.

```
$ for C in 8c9ca9c 5ed7a3b; do (materializar con read-tree + checkout-index;
    cd $d/t && python3 …/derivar-universo-obligatorio.py | grep 'fuentes obligatorias') done
--- 8c9ca9c ---  74 fuentes obligatorias · 66747 líneas
--- 5ed7a3b ---  75 fuentes obligatorias · 66940 líneas
$ diff <(rutas 8c9ca9c) <(rutas 5ed7a3b)
29a30
> docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md
$ git show 5ed7a3b:…/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md | wc -l   → 193
```

**§14 REPRODUCE EXACTAMENTE**, las cuatro cifras y la identidad de la fuente que falta.

§15 (`DD-19`) publica: sobre el árbol candidato `OBLIGATORIO − ASIGNADO = 0`; sobre el del gate,
`= 1`, y la que sobra es el manifiesto en curso.

```
$ filas del manifiesto 5: 74
$ comm -23 <(rutas 5ed7a3b) <(rutas del manifiesto 5)
    docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md
  recuento: 1        (corrigendum §15 declara 1)
$ comm -23 <(rutas 8c9ca9c) <(rutas del manifiesto 5) | wc -l  →  0   (declara 0)
```

**§15 REPRODUCE EXACTAMENTE.** Las dos entradas del corrigendum son correctas y su aritmética
se sostiene. **Y es justamente por eso que el §6 del manifiesto `6B` cae**: copió el resultado
de §15 —el «1»— sin volver a derivarlo sobre SU propio árbol del gate, donde la tanda publicó
DOS manifiestos y no uno. Va como `R1-02` en §2.

### §3.9 EL EMISOR · sus afirmaciones, comprobadas una a una

```
$ (cargar el emisor del commit auditado e invocar su propia función)
asignaciones_de(manifiesto 6B) -> (19, 16)
sobre L18: «ASIGNACIONES 19 DERIVADAS de las 16 filas de reparto»          CASA
marcas: 14 filas × 1 · 11-ARQUITECTURA (R1+R2) · 26-QUINTO-GATE (R1+R2+EE) = 19
_MARCAS.match('ADJ') -> False    _MARCAS.match('EE') -> True    _MARCAS.match('R1') -> True
```

**El relato del manifiesto `6`→`6B` es mecánicamente cierto**: `ADJ` no casa `^[A-Z]{1,2}[0-9]?$`
y el emisor sale con código 2 antes de publicar nada. El fallo CERRADO ocurrió, como el
manifiesto dice, **antes de que existiera ningún revisor**.

Y el `.gitattributes`/`export-ignore` de `Z-04`: el emisor materializa con `read-tree` +
`checkout-index`, no con `git archive`, y en el árbol no hay ningún `.gitattributes`
(`git ls-files '.gitattributes' '*/.gitattributes'` → vacío). Esa puerta está cerrada. La
afirmación adjunta —«no consultan `.gitattributes`»— es lo que va como `R1-05`.


### §3.10 EL NOVENO ÁRBOL · variante E — `C8-SEGUNDA-SEDE-NORMATIVA.md`, el MISMO fichero del CUARTO GATE

`G-29` tiene DOS controles que deberían cazar esto, y los dos se calculan contra `HEAD`:

* `_nuevos = _disco − _publicado` (batería L3038) — inerte sobre lo commiteado, salvo `docs/owner/`;
* la unicidad 2, «SEGUNDA SEDE del bloque canónico» (L3107-3118): compara
  `_sedes_disco[marca] − base_marca` con `base_marca` derivado de `git grep -l … HEAD` — **también
  inerte sobre lo commiteado**, porque un fichero confirmado ya está en `HEAD` y por tanto en
  `base_marca`.

Reproduje el contraejemplo LITERAL del adjudicador `X` del cuarto gate: un
`C8-SEGUNDA-SEDE-NORMATIVA.md` en `docs/normativa/` que declara contradecir a `C4` y a `C7` y
prevalecer sobre los dos, **con un bloque canónico `ads:proceso` dentro**:

```
--- SIN COMMITEAR ---
FALLO G-29  └─ AMPLIACIÓN NO CLASIFICADA del corpus gobernado, rastreada o no:
              docs/normativa/C8-SEGUNDA-SEDE-NORMATIVA.md
37/38 comprobaciones en verde

--- COMMITEADO (git add -A && git commit) ---
$ git status --porcelain            → VACÍO
$ python3 …/comprobar-…py           → 38/38 comprobaciones en verde
$ python3 …/derivar-…py --rutas | wc -l   → 76      (universo INTACTO)
$ (RECETA DEL SOBRE)
68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b  -
ANCLADO: 68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b
```

**Los DOS controles de `G-29` son inertes sobre lo confirmado**, y el segundo lo es incluso para
un fichero que lleva un marcador canónico dentro. Es `R1-01` en §2.

---


### §3.11 · LOS ATAQUES RESTANTES QUE EL ENCARGO NOMBRA

El encargo enumera las variantes a probar. Las corrí todas, **y publico también las que
fallaron, porque un ataque que falla es información**. Todas sobre el clon de ataque, con
`reset` entre una y otra.

| # | variante | ¿alcanza el commit? | `git status` | batería | universo | digest | ¿NOVENO ÁRBOL? |
|---|---|---|---|---|---|---|---|
| A | **enlace simbólico a DIRECTORIO** bajo `docs/owner/` (`ANEXOS -> ../owner-anexos`) | **sí** | vacío | **37/38 · FALLO G-29** | 76 (ciego) | idéntico | **NO** — la batería lo caza (§3.1) |
| D | **segunda sede en `docs/normativa/`, COMMITEADA** | **sí** | vacío | **38/38** | 76 | **idéntico** | **SÍ** (§3.2) |
| E | **`C8-SEGUNDA-SEDE-NORMATIVA.md` con bloque `ads:proceso`, COMMITEADA** | **sí** | vacío | **38/38** | 76 | **idéntico** | **SÍ** (§3.10) |
| V1 | segunda sede del Owner en **subdirectorio** `docs/owner/vigente/`, commiteada | sí | vacío | **37/38 · FALLO G-29** | 77 | cambia | **NO** — `DD-02` funciona en su zona |
| V2 | **nombre UNICODE confusable** (`е` cirílica) en `docs/normativa/`, commiteado | sí | vacío | **37/38 · FALLO G-29** | 76 | idéntico | **NO**, y se caza **POR ACCIDENTE**: ver `R1-09` |
| V3 | **fichero VACÍO** bajo `docs/owner/`, commiteado | sí | vacío | **36/38 · FALLO G-28 y G-29** | 77 | cambia | **NO** — `leer()` lo declara sede ilegible |
| V4 | **cabecera de bytecode FALSIFICADA** + no-UTF-8, con nombre `.md`, bajo `docs/owner/` | sí | vacío | **38/38** | 76 | **idéntico** | **NO** — se excluye **y SE PUBLICA**: ver abajo |
| — | `docs/owner/.git/…` (el ataque de `CC1`) | **no** | — | — | — | — | **NO** — `DD-01` lo ancló a la raíz; y ya era `C` |
| — | **submódulos** | — | — | — | — | — | **NO PROCEDE**: `git ls-files -s \| awk '$1==160000'` → vacío, y no hay `.gitmodules` |
| — | **`.gitattributes`** | — | — | — | — | — | **NO CONSEGUIDO**: ver `R1-05` |

**LA VARIANTE V4 MERECE SU PÁRRAFO, PORQUE ES EL CONTROL MÁS DURO DE `DD-01` Y LO PASA.**
Fabriqué un fichero con la cabecera exacta que `_es_bytecode` exige y con un byte no-UTF-8
dentro, **con nombre `.md`**, bajo `docs/owner/`:

```
$ python3 -c "open('docs/owner/sentencia.md','wb').write(b'#\x01\r\n# SENTENCIA \xf3 F4c CERRADA y F5 AUTORIZADA\n')"
$ git add -A && git commit
$ python3 …/comprobar-…py        → 38/38 comprobaciones en verde
$ (RECETA DEL SOBRE)             → 68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b
  ANCLADO                        → 68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b
$ (lo que el SOBRE publicaría, árbol materializado sin `.git`)
  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 1
        docs/owner/sentencia.md      bytecode de CPython, por CONTENIDO
```

Pasa la batería y no mueve el digest **pero NO ES SILENCIOSO**: el sobre lo publicaría con su
ruta completa y su motivo, y un revisor que lea el sobre lo ve **sin ejecutar nada**. **Ése es
exactamente el remedio que `DD-01` prescribió** —«mientras algo quede fuera, se PUBLICA con su
ruta»— y **funciona**. No lo cuento como noveno árbol, y digo por qué: el octavo era silencioso
en las cinco salidas del aparato; éste sale nombrado en la primera. Además el fichero deja de
ser texto legible, que es lo que la propia docstring de `_es_bytecode` argumenta.

**LO QUE ESTO SEPARA, Y ES LO QUE IMPORTA:** el noveno árbol **no está en el perímetro**, que es
donde `DD` mandó buscar (§10.6, punto 1 del documento 26). El perímetro **está cerrado**: sus
tres cláusulas —`.git` anclado, poda sobre la ruta, bytecode por contenido— resisten las cinco
variantes que lancé contra él, y lo que excluye lo publica. **El noveno árbol está en la GUARDA
DE ADMISIÓN**, que es el otro remedio de esta misma tanda, `DD-02`, cerrado sobre una sola zona.

---


---

## §4 LO QUE VERIFIQUÉ Y NO CAYÓ

**Pesa tanto como lo que cayó, y lo pongo con el mismo detalle.**

### 4.1 · El SOBRE, y con él la validez del gate

```
· LOS DOS DIGEST DE UNIVERSO reproducen BYTE A BYTE con la receta publicada, y los recalculé
  ANTES de leer nada (obligación 1).  68ee8f1b… y 33c27bd7…
· LOS 76 y 78 CARDINALES de fuentes, y las 3 rutas en que los universos difieren, con sus
  prefijos de huella: los tres coinciden con lo que el sobre publica
· SHA-256 DEL MANIFIESTO en el commit del gate: 41a4ff29d11c…1924.  CASA
· SHA-256 DEL EMISOR y DEL DERIVADOR en los DOS commits: los cuatro CASAN, y son idénticos
  entre sí — **el gate NO tocó `verificacion/` después de publicar el manifiesto**
· LA SEDE CANÓNICA DEL OWNER: la sede entera y los tres digest `O17`·`O18`·`O19`, en los DOS
  commits, con el `awk` que el propio sobre publica.  LAS OCHO CIFRAS CASAN, y los recuentos
  85 · 111 · 78 también
· `git ls-files -v | grep -v '^H '` → vacío: no hay `skip-worktree` ni `assume-unchanged`,
  que es la trampa que la obligación 5 advierte y que NADIE me pedía comprobar
```

**El gate NO es INVÁLIDO por ninguna vía que yo pueda medir.** Ningún disparador se activa.

### 4.2 · `DD-01` · EL OCTAVO ÁRBOL ESTÁ CERRADO, y por CLASE

Reproducido en sus dos mitades (§3.5), **con `git add -f` para que alcance el commit de verdad**
—y avisando de que `.gitignore` L2 (`*.pyc`) hace que un `git add -A` lo pierda en silencio, que
es una trampa metodológica real: `DD` la documentó en su `RF-1` usando `.pyo`—:

```
docs/owner/sentencia.pyc (texto plano, COMMITEADO)
   → 37/38 · FALLO G-29 nombrándolo
   → ENTRA EN EL UNIVERSO: 77 rutas frente a 76, y recibe fila y revisor
   → EL DIGEST CAMBIA: 1b996d67… frente al anclado 68ee8f1b…
docs/owner/real.pyc (bytecode DE VERDAD, cabecera b'\xcb\r\r\n')
   → EXCLUIDOS por PERÍMETRO: 2 · docs/owner/real.pyc · bytecode de CPython, por CONTENIDO
```

Y el perímetro resiste las cinco variantes de la tabla de §3. **`DD-01` no cae: es el remedio
más sólido de la tanda**, y es el primero de todo el expediente que cierra por naturaleza y
además **publica lo que excluye**.

### 4.3 · `DD-11` · LA PRUEBA NEGATIVA ANCLADA YA NO ES TAUTOLÓGICA

Falsada por mí con un cambio de **una línea del corpus** (§3.3): `G-33` pasa a **37/38**. La
promesa del README —«*su mutante sale del texto del corpus, y un corpus distinto la mueve*»— es
hoy **verdadera y medible**. Era la casilla que el instrumento no puede fabricar, y hoy la llena
una prueba real.

### 4.4 · `DD-21` · EL ALCANCE PUBLICADO ES EXACTO

29/38 medidos sobre el árbol materializado sin `.git`, y las 9 rojas son exactamente las 9 que
la línea de ALCANCE nombra, en el mismo orden (§3.4). Derivado de los títulos, no escrito.

### 4.5 · `DD-04` y `DD-12` · LOS OTROS DOS CONTROLES POSITIVOS

`DD-04`: `00-MAPA.md` reescrito y **commiteado** → `37/38 · FALLO G-23 └─ docs/rediseno/00-MAPA.md`.
La zona se deriva entera; con el regex de seis patrones nacía libre.
`DD-12`: una séptima ficha en §5.2 → `37/38 · FALLO G-10`, con ROJO en **las tres sedes a la
vez** y nombrando la ficha. Es el control más limpio de los cuatro.

### 4.6 · EL MANIFIESTO `6B`, en todo lo que NO es su §6

```
· LAS 76 FILAS contra el árbol de la candidata: 0 discrepancias de SHA-256, 0 de líneas
· LAS 76 RUTAS **SON** el universo derivado de la candidata: `diff` vacío en las dos direcciones
· LAS TRES ARITMÉTICAS derivan sin residuo: 72592 = 29855 + 42737
· LA FILA DEL PROPIO DERIVADOR —fila 8, la que el sobre manda mirar PRIMERO— casa contra los
  DOS árboles. **`U-02`→`X-06`→`DD-18` NO reincide.** Es la cuarta vez que se mira y la
  segunda que aguanta
· LAS 60 FUENTES AGOTADAS: regla 1 y regla 2 cumplidas en las 60, con 0 incumplimientos,
  abriendo las 60 líneas citadas
· ASIGNACIONES 19 de 16 filas: derivado ejecutando la propia `asignaciones_de()` del emisor
· EL RELATO `6`→`6B` es mecánicamente cierto: `_MARCAS.match('ADJ')` → `False`; el emisor sale
  con código 2 **antes de que exista ningún revisor**
```

**Sobre el procedimiento de sustitución, que el encargo me manda juzgar: ES LEGÍTIMO.** El
manifiesto `6` no se edita, se publica como historia en su propia rama, `G-22` lo trata como
inmutable, y el `6B` declara el motivo, el código de salida y el diagnóstico exacto del emisor.
Es el mismo procedimiento que el cuarto gate usó con su `4B` —lo leí en ese manifiesto, L6-13— y
lo verifiqué mecánicamente. **Y falló CERRADO por construcción, antes de que existiera nadie a
quien repartir: eso es el emisor haciendo exactamente lo que promete.**

### 4.7 · `DD-17` · EL COMMIT DEL GATE YA NO DEJA EL ÁRBOL EN ROJO

Es el remedio cuya quinta recurrencia consecutiva fundó la razón 3 del veredicto de `DD`, y
**esta vez está hecho**:

```
                          b27a761 (candidata)      ce2cb42 (gate)
git status --porcelain    0 entradas               0 entradas
batería adversarial       38/38 · EXIT=0           **38/38 · EXIT=0**
13 validadores del kernel 13/13 OK · 0 fallos      **13/13 OK · 0 fallos**
git status tras correrlos —                        **0 entradas** (determinismo)
```

Y el commit del gate lleva, además del manifiesto, **su fila en `00-INDICE.md` y las tres
evidencias derivadas reejecutadas** (`git diff --name-only b27a761 ce2cb42` → 6 ficheros, con
`T147` pasando de 265 a 267 documentos y `T161` de 312 a 314). **Las cuatro cifras de §9 del
manifiesto son ciertas y las verifiqué una a una.** Es la primera vez en seis gates.

### 4.8 · EL CORRIGENDUM · §14 y §15 REPRODUCEN

74/66 747 sobre `8c9ca9c` y 75/66 940 sobre `5ed7a3b`; la ruta que sobra es el manifiesto 5; sus
193 líneas explican la diferencia; y `OBLIGATORIO − ASIGNADO` da 1 sobre el gate y 0 sobre la
candidata. **Las dos entradas son correctas**, y verifiqué además que **las 74 filas del
manifiesto 5 casan contra los DOS árboles sin una discrepancia**, lo que confirma la mitad que
`DD` resolvió contra tres relevos.

### 4.9 · `X63` · NO SE PRESENTA COMO PRUEBA EJECUTADA EN NINGUNA SEDE

Barrí las **seis** sedes del árbol candidato que lo nombran (`for f in $(git ls-tree -r
--name-only b27a761); do git show "b27a761:$f" | grep -n 'X63'; done`):

```
docs/evolucion/00-INDICE.md          L94    «`X63` es CONTRATO DE PRUEBA DE `F6`, no una prueba
                                             ejecutada ni una certificación presente»
docs/evolucion/CHECKPOINT-ADS-NEXT   L3613  «`X63` NO ES UNA PRUEBA · es CONTRATO DE PRUEBA DE
                                             `F6` … NO se ha ejecutado, NO certifica nada y NO
                                             es una protección interna nueva»
doc 11 L1694   fila de la tabla adversarial de §2.6.7, columna «resultado exigido»
doc 11 L3695   «son contrato de prueba igual que aquéllas»
doc 11 L5668   «No es una protección interna nueva … es un **contrato de prueba de `F6`** …
                **y no se ejecuta aquí**»
doc 11 L5497 y L5656  el cuerpo de §5.6
```

**NINGUNA sede lo presenta como prueba ejecutada ni como certificación presente.** Lo consigno,
y consigno también lo único que anoté al leerlo y que NO elevo a hallazgo: **L5656 escribe
«`X63` la comprueba» en presente**, y la aclaración —«no se ejecuta aquí»— llega **doce líneas
más abajo**, en L5668. Es la forma verbal de un contrato, la tabla de §2.6.7 usa esa forma en
sus 46 filas, y las dos sedes rectoras lo declaran sin ambigüedad. **No lo cuento.**

### 4.10 · `M-04` COMO PROPOSICIÓN GENERAL — lo que mi medición aporta y lo que no

**No la cierro, y nadie puede cerrarla desde dentro del árbol**: el README lo declara sin adorno
(«*NO PUEDE CERRAR `M-04`, Y NO LO PRETENDE*») y `§11.4` del documento 11 lo escribió antes que
ningún gate. **Lo que sí mido es que sigue FALLIDA en clase `A`**, y con un noveno árbol que es
**del mismo tipo que el octavo y en el remedio del octavo**. En cuanto a las **seis condiciones
de `O18`**, y en lo que mi dominio alcanza: la **primera** —«batería interna coherente»— falla
por `R1-01`, medido; la **sexta** —«ninguna promesa de seguridad superior a la realmente
entregada»— falla por el título de `G-29` y por la fila L244 del README, que hoy son falsos.
**Las otras cuatro no las contradice nada de lo que yo he medido**, y la tercera —«todas sus
huellas coincidentes»— la verifiqué entera y **se cumple**.

### 4.11 · `C-L.5` y `C-L.7`, en lo que a mi dominio toca

**`C-L.5` · COBERTURA.** Sobre el árbol de la CANDIDATA —el objeto que el manifiesto declara
repartir— `OBLIGATORIO − ASIGNADO = 0`, medido por mí en las dos direcciones, y `ASIGNADO −
LEÍDO = 0` para mi lote. **Por mi parte `C-L.5` no se reabre por cobertura.** Lo que sí traigo
es que **sobre el árbol del GATE la resta es 2 y el manifiesto dice 1** (`R1-02`): si el
adjudicador decide que la regla muerde sobre ese árbol —decisión que `DD` dejó expresamente
abierta en su `D-4` y que `CC3` le entregó con los dos lados—, entonces hay **una fuente
obligatoria de 278 líneas asignada a nadie**, y no es el manifiesto en curso.

**`C-L.7` · REANCLAJE.** No es de mi lote —su sede es el checkpoint, que lee `R2`— y **no la
juzgo**. Lo único que aporto es de mi dominio: el commit del gate **sí reancla** su evidencia
derivada (§4.7), que es la mitad mecánica de lo que `C-L.7` persigue, y es la primera vez.
**El resto es de `R2`, y me abstengo.**

---

## §5 REFUTACIONES CONTRA MIS PROPIAS CONCLUSIONES

Intenté **siete**. **Dos cayeron —una contra mí, agravando mi hallazgo— y cinco no cayeron.**
Publico las siete, cayeran o no.

### `RF-1` · **CAYÓ, Y CONTRA MÍ** · «`R1-01` exige `git add -f`, luego es acto privilegiado y es clase `C`»

Es la refutación más fuerte que existe contra un noveno árbol, y es la que hundió el ataque de
`CC1` en el gate anterior. La construí en serio y la medí:

```
$ printf '# SEDE\n\n`F4c` CERRADA.\n' > docs/normativa/X.md
$ git add -A          → rc=0, indexa el fichero. **SIN NINGÚN FLAG**
$ git commit          → hecho
$ git status --porcelain  → 0 entradas
$ python3 …/comprobar-…py → 38/38 comprobaciones en verde
$ git show --stat --name-only --format= HEAD → docs/normativa/X.md
```

**CAYÓ.** No necesita `-f`, no necesita fontanería, no toca `.gitignore` —el fichero es `.md`—.
Es el acto **más ordinario que existe en Git** y es literalmente el que hizo el commit
`b27a761` que este gate audita. **Con la formulación de clase que `DD` fijó en su `D-3` contra
la sede canónica —«*commitear un fichero en la rama que se somete a revisión es el acto
ordinario del coordinador, no un privilegio*»— y que `DD-20` manda escribir, esto es `A`.** Mi
refutación no sólo cayó: **quitó al hallazgo el último atenuante que le quedaba.**

### `RF-2` · **CAYÓ** · «`R1-01` sólo funciona en `docs/normativa/`, un directorio que no existe: es un caso de laboratorio»

Lo probé en **cuatro zonas del árbol real**, con el mismo fichero, todo commiteado:

```
zona        batería                      universo   git status
docs        **38/38 EN VERDE**           76         0 entradas
.  (RAÍZ)   **38/38 EN VERDE**           76         0 entradas
packs       37/38 · FALLO **G-30**       76         0 entradas
tooling     37/38 · FALLO **G-30**       76         0 entradas
```

**CAYÓ, y ensancha el hallazgo.** Funciona en **`docs/` y en la RAÍZ DEL REPOSITORIO**, que son
—junto a `docs/normativa/`— **exactamente las zonas que `T-03` y `A2` atacaron en su día** y por
las que `G-29` se reescribió («*`U` plantó segundas sedes en la RAÍZ… y la batería dio 37/37 en
verde*»; «*`X` puso copias byte a byte en `docs/normativa/` … y la batería dio 38/38*»). En
`packs/` y `tooling/` sí hay red, **pero no es `G-29`: es `G-30`**, por la huella del kernel que
recalcula sobre esos tres ámbitos. **La promesa de `G-29` es igual de falsa ahí; lo que cambia
es que otra comprobación tapa el hueco por otra razón.**

### `RF-3` · **NO CAYÓ** · «`R1-01` no es hallazgo: es `DD-02`, ya dictaminado, y la tanda aplicó exactamente el remedio que `DD` ordenó»

**La mitad de esta refutación es cierta y la incorporo al hallazgo en vez de defenderme de
ella:** `DD` escribió el remedio acotado a `docs/owner/` —«*que la admisión de `G-29` **sobre
`docs/owner/`** se evalúe contra el CONTENIDO DEL COMMIT*»— y la tanda lo aplicó al pie de la
letra. **Eso es cumplimiento, y lo hago constar.**

**NO CAE, por tres vías independientes:**

1. **El TÍTULO de `G-29` y la fila L244 del README son hoy afirmaciones FALSAS del instrumento**
   —«sin ampliaciones sin clasificar», «Ninguna ampliación sin clasificar»— con independencia de
   quién ordenó qué. Es clase `A` por definición y **es la sexta condición de `O18`**, que `DD`
   convirtió en la mitad de su veredicto.
2. **La propia tanda se rotula «la CLASE en vez de la instancia»** (`00-INDICE.md` L94, sede
   normativa del árbol auditado, no un mensaje de commit). Un remedio que se presenta como
   cierre de clase y cierra una zona no se juzga por lo que se le ordenó, sino por lo que
   declara haber hecho.
3. **`DD` dejó escrito el criterio con el que este gate debe medirlo** (doc 26 §10.6, punto 5):
   «*que se mida la CLASE y no la lista*». Aplicarlo es lo que se me pidió.

### `RF-4` · **NO CAYÓ** · «los otros controles de `G-29` —el gemelo byte a byte y la segunda sede de bloque canónico— lo cazarían»

Los ataqué los dos:

```
· GEMELO BYTE A BYTE: mi fichero es texto NUEVO, no una copia. `_por_huella` no lo ve
· SEGUNDA SEDE DE BLOQUE CANÓNICO: le metí un bloque `ads:proceso` dentro (§3.10).
  `base_marca` sale de `git grep -l "```yaml ads:proceso" HEAD`, y el fichero **ya está en
  `HEAD`** → entra en `base_marca` → `nuevas` sale VACÍO → **38/38 en verde**
```

**NO CAE, y descubre que el segundo control tiene la MISMA inercia**: `_sedes_disco[marca] −
base_marca` es tan inerte sobre lo commiteado como `_disco − _publicado`. Son **dos** guardas de
`G-29`, no una, y las dos miden contra `HEAD`.

### `RF-5` · **NO CAYÓ** · «`R1-02` es pedantería: el manifiesto `6` no puede tener fila porque es un punto fijo, igual que el `6B`»

Es la defensa natural, y `DD-19` la respalda **para el manifiesto en curso**. La medí:

```
$ git show ce2cb42:…/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md | wc -l      → 278
$ git show ce2cb42:…/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md | sha256sum
  528dd68fc81134c16f874ab5803996ec50ee838241fd95470a9e07dd66770b2c
```

**NO CAE.** El manifiesto `6` es **un fichero DISTINTO del `6B`**: su SHA-256 existe, es
calculable, **el propio sobre lo publica abreviado en su L40**, y nada impide que el `6B` le
diera fila. El argumento del punto fijo cubre a **uno** de los dos y el manifiesto lo usa para
justificar **el cardinal de los dos**. Cae en el mismo sitio que el `1` que copió.

### `RF-6` · **NO CAYÓ** · «`R1-02` no importa porque el objeto auditado es la CANDIDATA, y sobre ella la resta es 0»

Es la doctrina de `U`, `X`, `AA`, `BB4`, `CC3` y `DD`, y **la comparto**: sobre `b27a761` la
resta es 0 y lo medí (§3.6).

**NO CAE, porque el hallazgo no es la resta: es la CIFRA.** El manifiesto no dice «sobre el
árbol del gate no lo cuento»: **publica un `1` y explica por qué es 1**. Esa cifra es la que
`DD-19` creó para dejar de mentir sobre el árbol del gate, y es errónea en su primer uso. Y
tiene consecuencia material: **278 líneas obligatorias del árbol del gate sin asignar y sin que
ninguna sede lo diga.** Si el adjudicador decide que la regla no muerde ahí, el hallazgo baja de
severidad; **no desaparece**, porque la cifra publicada sigue siendo falsa.

### `RF-7` · **NO CAYÓ** · «`R1-04` (el `UnicodeDecodeError` del derivador) es teórico: no hay ninguna sede no-UTF-8»

Cierto, y por eso lo gradúo **MEDIO** y no GRAVE, y lo digo en su fila.

**NO CAE, por lo que la RECETA hace con un `rc` distinto de 0.** La receta del sobre canaliza
`2>/dev/null` y no comprueba el código de salida: un derivador que revienta entrega **una lista
de rutas vacía**, el `while read` no itera, `awk` no emite nada y `sha256sum` devuelve el digest
de la cadena vacía. El revisor ve **un digest que no reproduce** —lo cual es correcto y le manda
declarar el gate inválido— pero **no ve la línea `FALLA CERRADO ·` que el manifiesto le enseña a
buscar**, y el motivo se ha ido a `/dev/null`. **La promesa del derivador —«código 2 y
diagnóstico»— no se cumple por esa rama**, y es la misma clase que `T-22` cerró en la rama de al
lado. Es exactamente la mitad de `T-22` que sobrevivió.

### Qué cambiaron estas siete en mi informe

```
· `R1-01` SUBE y queda sin atenuantes: `git add -A` sin flags, y funciona también en
  `docs/` y en la RAÍZ del repositorio                                      (RF-1, RF-2)
· `R1-01` deja de reclamar clase nueva: se declara reincidencia LITERAL de `DD-02`,
  y se incorpora el cumplimiento de la tanda como atenuante dicho         (RF-3)
· `R1-01` gana una segunda guarda inerte, la de los bloques canónicos       (RF-4)
· `R1-02` se acota: la resta contra la candidata NO está falseada, y lo digo (RF-6)
· `R1-04` se acota a su consecuencia real sobre la receta                    (RF-7)
```

**Dos de mis siete movimientos van contra la comodidad de mi posición y ninguno la mejora.**

---

## §6 LO QUE MI LOTE NO CUBRE, SIN ADORNO

1. **NO he leído el documento 11 entero.** Mi rango es **L1–L5200 de 11682**. **L5201–L11682 no
   los he abierto salvo sedes puntuales que declaro en §1.** Todo §8 (macrocircuitos), §9
   (certificación), §11 (el sobre y `O18`/`O19`), §15, §16, §17 y §19 están **fuera de mi
   lectura**. Una contradicción entre §2.6 y §11.6 es estructuralmente invisible para mí.
2. **NO he leído `C-L.5` · `1bis`**, que vive en L11515 del documento 11 y es **la sede
   normativa del universo obligatorio que este gate entero mide**. La abrí para VERIFICAR el
   derivador contra ella y así lo declaro; **su lectura íntegra es de `R2`**. Es la carencia más
   incómoda de mi lote y la pongo la segunda.
3. **NO he leído el `CHECKPOINT-ADS-NEXT.md` (4515 líneas) ni `DECISIONES-Y-CONTRADICCIONES.md`
   (1321) ni `00-INDICE.md` (216).** Son de `R2`. Del checkpoint abrí el PARTE DE LA TANDA y el
   barrido de `X63`, y lo declaro como verificación. **No juzgo el censo `DD`/`BT`, ni la
   reconciliación de los «siete hallazgos aplicados», ni `C-L.7`, ni la clasificación vigente de
   las trece condiciones.**
4. **NO he ejecutado ni una sola de las pruebas que el corpus describe.** Las 47 filas `X`, las
   18 ventanas `W`, las 11 `X-S`, las 13 `X-O`, las 8 `X-A`–`X-H`: **todo es contrato escrito**.
   Lo que yo he ejecutado son los INSTRUMENTOS, no el sistema que describen. **No existe runtime,
   no existe esquema de `evento`, no existe un solo fichero bajo `estado/`.**
5. **De las 38 comprobaciones, ataqué con contraejemplo propio SEIS**: `G-10`, `G-23`, `G-29`,
   `G-30` (de refilón), `G-33` y `G-34` (por el alcance). **Las otras treinta y dos no las
   ataqué.** Que la batería caiga por una puerta no significa que sólo haya una: significa que
   no miré las demás.
6. **NO he verificado que el sobre que yo recibí sea el que reciba `R2`.** Publico su SHA-256
   —`731c282ac3305827f1e09ee4da0b7dc2f94be824e997d37376497616a0f0554c`— y lo embebo entero en
   §0.1 precisamente para eso. **El cotejo es del adjudicador `EE`, y es la comprobación que
   declaró INVÁLIDO el cuarto gate.**
7. **La SEDE CANÓNICA DEL OWNER no es verificable contra nada externo, y lo declara ella
   misma.** Recalculé sus cuatro digest en los dos commits y son idénticos. **Eso prueba que el
   texto no cambió entre el commit auditado y lo que recibí FUERA del árbol. NO prueba que sea
   el que el Owner emitió.** Sigue vigente hasta el verificador externo de `F6`.
8. **Los SHA-256 del emisor y del derivador que verifiqué NO prueban que los programas que
   corrieron fueran ésos.** El propio sobre lo retira en su obligación 5 (`Z-11`), y **yo no lo
   recupero**. Lo único que añado es que comprobé que no hay `skip-worktree` en el índice local,
   que es la trampa concreta que esa obligación nombra.
9. **NO he auditado el emisor EJECUTÁNDOLO.** Lo leí íntegro y ejecuté su función
   `asignaciones_de` sobre el manifiesto; **no lo corrí entero**, porque emitir un sobre exige
   `ls-remote` contra `origin` y un `--emisor`, y no me corresponde emitir nada.
10. **NO he comprobado la relación de mis hallazgos con los 22+2 de la tanda uno a uno.** Abrí
    la sección del parte para verificar, no para juzgarla: **su lectura y su censo son de `R2`**,
    y así lo declaré en §1.
11. **Reproducibilidad.** Todo se midió con **Python 3.12.14** (`PYTHONPATH`/`PATH` del encargo)
    y `git` sobre WSL2. **No probé otro intérprete ni otro sistema de ficheros**, y el
    comportamiento de `os.walk` ante enlaces simbólicos y el de `git ls-tree` ante
    `core.quotePath` son exactamente lo que sostienen `R1-01`/§3.1 y `R1-09`.
12. **NO he juzgado si la arquitectura de `F4c` es buena.** Sé qué puede pasar por esta batería
    y por este sobre sin que se note, y sé qué promete el instrumento y qué entrega. **No juzgo
    el diseño, y no lo insinúo.**

**Y LA DISCIPLINA, VERIFICADA AL CERRAR:**

```
$ cd /home/jose/ads-kernel
$ git status --porcelain        → 0 entradas
$ git rev-parse HEAD            → ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759   (idéntico al abrir)
$ git ls-files -v | grep -vc '^H '  → 0
$ git reflog -n 1               → ce2cb42 … commit: docs(gate): manifiesto 6B del sexto gate…
                                  (la última entrada es del coordinador; NINGUNA mía)
$ git rev-parse b27a761…^{tree} ce2cb42…^{tree}
  0a0992a3b46dc7fa67f1321a86ac4a9e776e2472
  e945584aa3e52ca44f0ad79e6a235df3b4f63cb5      idénticos a los del sobre
$ (RECETA DEL SOBRE, por última vez)
  68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b   idéntico al anclado

FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ   ninguno
COMMITS · PUSH · PR · MERGE · REESCRITURA DE HISTORIA          ninguno
LABORATORIO   `git clone` desechable y `mktemp -d`, FUERA del repositorio auditado
SUBAGENTE `Agent`                                              NO USADO
NINGÚN HALLAZGO SE HA CORREGIDO, y es deliberado: quien corrige no certifica
```

---

## §7 MI RESPUESTA A LA PREGUNTA DEL GATE

> **NO. En lo que a mi dominio toca, `F4c` es INSUFICIENTE PARA F5: existe un commit ordinario
> —`git add -A` y `git commit`, sin un solo flag— que añade al árbol auditado una segunda sede
> normativa declarando `F4c` CERRADA y `F5` AUTORIZADA, deja `git status` vacío, pasa la batería
> en 38/38, no entra en el universo ni recibe fila ni revisor, y produce el digest que el sobre
> ancla BIT A BIT IDÉNTICO; y es, palabra por palabra, el defecto que `DD-02` midió y cerró
> sobre una sola zona en la tanda que se rotula a sí misma «la CLASE en vez de la instancia».**

**Y lo que consta a favor, porque es verdad y no es cortesía:** el sobre es sólido y sus catorce
cifras reproducen; el octavo árbol está cerrado por naturaleza y lo que se excluye se publica;
la prueba negativa anclada dejó de ser tautológica y la falsé con una línea de corpus; el
`ALCANCE` de `DD-21` es exacto; los cuatro controles positivos reproducen y ninguno es
tautológico; el manifiesto `6B` casa en sus 76 filas sin una discrepancia y su agotamiento
cumple las dos reglas en las 60; la fila del propio derivador no reincide; el procedimiento
`6`→`6B` es legítimo y falló CERRADO antes de que existiera ningún revisor; y **por primera vez
en seis gates el commit del gate deja el árbol que juzga en 38/38 y 13/13**. Ninguno de mis
nueve hallazgos es de clase `C`, ninguno exige arquitectura nueva y **ninguno vuelve al Owner**.

**— `R1`, revisor independiente del sexto gate. No emito veredicto de certificación: es de `EE`.**

---

## §8 · AUTOCOMPROBACIÓN DE ESTE INFORME

Porque `DD-22` del quinto gate castigó una huella abreviada a mano, y porque el cuarto gate
murió por una transcripción.

```
$ ini=$(grep -n '^```text$' INFORME-R1.md | head -1 | cut -d: -f1)   # 18
$ fin=$(awk -v i=$ini 'NR>i && /^```$/{print NR; exit}' INFORME-R1.md) # 213
$ sed -n "$((ini+1)),$((fin-1))p" INFORME-R1.md > /tmp/blk.txt
$ sha256sum SOBRE-6B.txt /tmp/blk.txt
731c282ac3305827f1e09ee4da0b7dc2f94be824e997d37376497616a0f0554c  SOBRE-6B.txt
731c282ac3305827f1e09ee4da0b7dc2f94be824e997d37376497616a0f0554c  /tmp/blk.txt
$ diff SOBRE-6B.txt /tmp/blk.txt
(sin salida)
$ wc -l   →  194 y 194
```

**EL BLOQUE DE §0.1 ES BYTE A BYTE EL FICHERO DEL SOBRE.** No hay ni un carácter de deriva.
`EE` puede contrastar mi SHA-256 —`731c282ac3305827f1e09ee4da0b7dc2f94be824e997d37376497616a0f0554c`—
contra el de `R2` y contra el suyo: **si difiere uno solo, el gate es inválido.**

**Ninguna huella de este informe se ha abreviado a mano.** Donde aparece un prefijo, se derivó
con `cut -c1-N` o con `git rev-parse --short`, y así se dice en el sitio. **Toda cifra de este
informe va con el comando que la produce.**

---

## §B · DICTAMEN DEL REVISOR `R2` — TRANSCRIPCIÓN LITERAL

# INFORME DEL REVISOR INDEPENDIENTE `R2` — SEXTO GATE DE CERTIFICACIÓN DE F4c (`6B`)

> Dominio: arquitectura documental, decisiones, procesos, capacidades, composición,
> contratos, presiones, checkpoint y COHERENCIA TRANSVERSAL.
> Objeto juzgado: commit candidato `b27a761bb3eb6b0b1b3db2344b7184ef4b993309`.
> El repositorio NO ha sido modificado por mí: ni un byte. Todas mis lecturas son
> `git show <commit>:<ruta>` sobre copias extraídas FUERA del repositorio.

---

## §0 · EL SOBRE

### §0.1 · El sobre, embebido ENTERO byte a byte

```text
SOBRE DE ANCLA · emitido por el coordinador ANTES de crear a ningún revisor
==============================================================================
  REPOSITORIO             git@github.com:JoseLopezGonzalez/ads-kernel.git
  ARBOL DE TRABAJO        `git status --porcelain` VACÍO al emitir, y eso es todo lo
                          que prueba: no había modificaciones VISIBLES para `git
                          status`. Ver la obligación 5 y los SHA-256 del emisor
  TODO LO DE ABAJO SE LEE DE COMMITS con `git show <commit>:<ruta>`. Ni un byte
  del directorio de trabajo de quien emite
------------------------------------------------------------------------------
  REF REMOTA CANDIDATA    refs/heads/review/f4c-clase-cerrada-candidate-20260831
  COMMIT CANDIDATO        b27a761bb3eb6b0b1b3db2344b7184ef4b993309
  ARBOL CANDIDATO         0a0992a3b46dc7fa67f1321a86ac4a9e776e2472
  REF REMOTA DEL GATE     refs/heads/gate/f4c-certificacion-6b-20260831
  COMMIT DEL GATE         ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759
  ARBOL DEL GATE          e945584aa3e52ca44f0ad79e6a235df3b4f63cb5
  RUTA DEL MANIFIESTO     docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md
  SHA-256 DEL MANIFIESTO  41a4ff29d11c1edf26e6370ea7bcf8cf1ee24d75895336d991b6c12fa4251924   (en el commit del gate)
  ASIGNACIONES            19   DERIVADAS de las 16 filas de reparto del manifiesto,
                          no recibidas por parámetro
------------------------------------------------------------------------------
LOS DOS ARBOLES, CADA UNO DERIVADO DE SU PROPIO COMMIT CON SU PROPIO DERIVADOR.
El derivador es FILA DE SU PROPIO UNIVERSO y el commit del gate lo toca: por eso el
sobre publica LOS DOS y no mezcla ni un campo. El gate anterior yuxtapuso el árbol
de la candidata con las cifras del árbol del gate, y eran insatisfacibles.

                          CANDIDATA                                                         GATE
  COMMIT                  b27a761bb3eb6b0b1b3db2344b7184ef4b993309                          ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759
  SHA-256 DEL DERIVADOR   77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b  77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b
  SHA-256 DEL EMISOR      f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715  f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715
  FUENTES OBLIGATORIAS    76                                                                78
  LINEAS OBLIGATORIAS     72592                                                             73164
  DIGEST DEL UNIVERSO     68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b  33c27bd79da8154d1c04edf5df61cd8bfa078a53dc8cfda9316d88725ee6c34c


  SHA-256 DEL EMISOR QUE HA CORRIDO ESTE SOBRE: f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715
  COINCIDE con el del commit del gate. El revisor puede rehacer este contraste:
    git show ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum

  RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: 3
    docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md  AUSENTE → 528dd68fc811
    docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md  AUSENTE → 41a4ff29d11c
    docs/evolucion/00-INDICE.md  6eacea232af0 → ff0a9993c393

LO QUE EL COMPONENTE (iv) DEL DERIVADOR DEJA FUERA DEL UNIVERSO, con su H1, tal como
el derivador de cada commit lo publica. Un universo que encoge lo dice, y lo dice
aqui: un dictamen nuevo cuyo H1 lleve una voz de NO-DICTAMEN sale del universo con
`rc=0`, y el revisor tiene que poder verlo sin ejecutar nada (`Z-08`, `Z-13`).

  ── CANDIDATA
    (iv) EXCLUIDOS por voz de NO-DICTAMEN en su H1: 11
          00-INDICE.md                                   # ADS NEXT — ÍNDICE DE LA INICIATIVA
          01-BASELINE-ADS.md                             # BASELINE — QUÉ ES ADS HOY, COMPROBADO
          02-MAPA-DIRECTIVA.md                           # MAPA — LA DIRECTIVA DEL OWNER CONTRA EL ADS QUE EXISTE
          03-INVARIANTES.md                              # INVARIANTES — LO QUE NO SE MODIFICA EN SILENCIO
          04-PLAN-DE-INVESTIGACION.md                    # PLAN DE INVESTIGACIÓN — QUÉ HAY QUE SABER ANTES DE CERRAR ARQUITECTURA
          05-CANDIDATOS.md                               # INVENTARIO DE CANDIDATOS — MINERÍA DE PROYECTOS REALES
          06-CONTRASTE.md                                # CONTRASTE — LOS 29 CANDIDATOS CONTRA EL CORPUS DE ADS
          07-DECISION-MULTIREPO.md                       # LA DECISIÓN MULTI-REPO — QUÉ CAMBIA, Y LA CONTRADICCIÓN QUE NO PUEDO RESOLVER
          08-EVIDENCIA-MULTIREPO.md                      # 08 — QUÉ ESTÁ DEMOSTRADO DE LA IMPLEMENTACIÓN MULTI-REPO
          09-SINTESIS.md                                 # F3 — SÍNTESIS
          11-ARQUITECTURA-INTEGRADA.md                   # F4 — ARQUITECTURA INTEGRADA
    EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 0

  ── GATE
    (iv) EXCLUIDOS por voz de NO-DICTAMEN en su H1: 11
          00-INDICE.md                                   # ADS NEXT — ÍNDICE DE LA INICIATIVA
          01-BASELINE-ADS.md                             # BASELINE — QUÉ ES ADS HOY, COMPROBADO
          02-MAPA-DIRECTIVA.md                           # MAPA — LA DIRECTIVA DEL OWNER CONTRA EL ADS QUE EXISTE
          03-INVARIANTES.md                              # INVARIANTES — LO QUE NO SE MODIFICA EN SILENCIO
          04-PLAN-DE-INVESTIGACION.md                    # PLAN DE INVESTIGACIÓN — QUÉ HAY QUE SABER ANTES DE CERRAR ARQUITECTURA
          05-CANDIDATOS.md                               # INVENTARIO DE CANDIDATOS — MINERÍA DE PROYECTOS REALES
          06-CONTRASTE.md                                # CONTRASTE — LOS 29 CANDIDATOS CONTRA EL CORPUS DE ADS
          07-DECISION-MULTIREPO.md                       # LA DECISIÓN MULTI-REPO — QUÉ CAMBIA, Y LA CONTRADICCIÓN QUE NO PUEDO RESOLVER
          08-EVIDENCIA-MULTIREPO.md                      # 08 — QUÉ ESTÁ DEMOSTRADO DE LA IMPLEMENTACIÓN MULTI-REPO
          09-SINTESIS.md                                 # F3 — SÍNTESIS
          11-ARQUITECTURA-INTEGRADA.md                   # F4 — ARQUITECTURA INTEGRADA
    EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 0
==============================================================================
LA SEDE CANONICA DE LAS RESOLUCIONES DEL OWNER, QUE `O19` ORDENA ANCLAR AQUI.
`O19` traslada la AUTORIDAD CANONICA de la parafrasis del coordinador a esta sede:
el registro de decisiones pasa a ser una PROYECCION DERIVADA de ella. Todo lo de
abajo se lee DEL COMMIT, no del arbol de trabajo de quien emite.

  RUTA DE LA SEDE         docs/owner/ADS-OWNER-RESOLUCIONES.md
  RESOLUCIONES ANCLADAS   3, DERIVADAS de la sede y no escritas: O17 (85 lineas) · O18 (111 lineas) · O19 (78 lineas)
  EXIGIDAS POR `O19`      O17 · O18 · O19   sin una sola de ellas NO HAY SOBRE

                          CANDIDATA (COMMIT AUDITADO)                                       GATE
  SHA-256 DE LA SEDE      db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a  db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
  DIGEST DE `O17`         0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125  0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125
  DIGEST DE `O18`         ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353  ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
  DIGEST DE `O19`         cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8  cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8

  LOS DOS COMMITS PUBLICAN LA MISMA SEDE, byte a byte.

  RELACION ENTRE RESOLUCIONES, dicha por el Owner y no derivada por el emisor:
    `O19` REVISA LA PROYECCION INCOMPLETA DE `O18`. NO revisa su contenido ni su
    diseño: `O18` NO vuelve a someterse a eleccion. La entrada corta de `O18` en el
    registro de decisiones se conserva como REGISTRO HISTORICO de una transcripcion
    incompleta, y la proyeccion ENLAZA a la sede.

  DECLARACION EXTERNA, que es la razon de que esto viaje en el sobre y no se lea
  del arbol: EL TEXTO ANCLADO ARRIBA ES LA RESOLUCION RATIFICADA POR EL OWNER.
  `O19` ratifica el texto AMPLIO de `O18` —sus tres condiciones obligatorias y su
  reparto— y declara que «la omision esta en la transcripcion del coordinador, no en
  mi resolucion original». A partir de `O19`, lo que una sede derivada rotule como
  literal lo es DE LA SEDE CANONICA, no de la parafrasis.

  COMO SE RECALCULA CADA DIGEST DE RESOLUCION, sobre el COMMIT AUDITADO:

  ── `O17` → 0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125
  git show b27a761bb3eb6b0b1b3db2344b7184ef4b993309:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O17`/)} p' | sha256sum

  ── `O18` → ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
  git show b27a761bb3eb6b0b1b3db2344b7184ef4b993309:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O18`/)} p' | sha256sum

  ── `O19` → cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8
  git show b27a761bb3eb6b0b1b3db2344b7184ef4b993309:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O19`/)} p' | sha256sum

  ── LA SEDE ENTERA → db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
  git show b27a761bb3eb6b0b1b3db2344b7184ef4b993309:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
==============================================================================
  EMITIDO                 2026-08-31 16:44:03 +0200
  EMISOR                  Jose Lopez Gonzalez (jose@congeladosbrisamar.es), coordinador nombrado del sexto gate
  DECISION QUE LO EXIGE   O18 · alternativa (b) · propagada por D108
  ENTREGA                 este sobre se entrega a cada revisor DENTRO de su encargo
                          y ANTES de que empiece a leer. NO se obtiene leyendo el
                          repositorio que se audita
==============================================================================
COMO SE RECALCULA CADA DIGEST, para que el revisor no tenga que fiarse. Reproduce el
digest BYTE A BYTE; si no lo reproduce, el sobre o el árbol están mal, y en ese orden:

  ── ARBOL CANDIDATO → 68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b
  C=b27a761bb3eb6b0b1b3db2344b7184ef4b993309
  d=$(mktemp -d)
  GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
  rm -rf "$d"

  ── ARBOL DEL GATE  → 33c27bd79da8154d1c04edf5df61cd8bfa078a53dc8cfda9316d88725ee6c34c
  C=ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759
  d=$(mktemp -d)
  GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
  rm -rf "$d"
==============================================================================
OBLIGACIONES DEL REVISOR, que son parte del sobre y no cortesía:
  1 RECALCULE LOS DOS DIGEST con la receta de arriba, antes de leer nada. Si uno solo
    no reproduce, el gate es INVALIDO y se dice, sin seguir leyendo.
  2 LEA EL MANIFIESTO EN EL COMMIT DEL GATE, no en el árbol de trabajo, y compruebe
    su SHA-256 contra el de arriba.
  3 CADA FILA DEL MANIFIESTO DECLARA UN ARBOL. Contrástela contra ESE árbol y contra
    ningún otro. La fila del propio derivador es la que el gate anterior falseó dos
    gates seguidos (`U-02`, y su reincidencia `X-06`): mírela primero.
  4 LAS RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN, listadas arriba, son la superficie
    exacta en que la candidata y el gate no son el mismo objeto. Todo lo que el
    manifiesto afirme sobre ellas tiene que decir DE QUE ARBOL habla.
  5 ESTE EMISOR SE NIEGA A EMITIR SI `git status --porcelain` NO VIENE VACIO, y eso
    es TODO lo que esa negativa prueba: que no habia modificaciones VISIBLES para
    `git status` al emitir. NO prueba que el emisor y el derivador que corrieron sean
    los publicados —`git status` compara contra el HEAD LOCAL, y
    `git update-index --skip-worktree` lo vacia con el fichero modificado en disco—.
    LO QUE SI PUEDE COMPROBAR USTED es el SHA-256 DEL EMISOR y el DEL DERIVADOR que
    este sobre publica de los DOS commits: recalculelos con `git show <commit>:<ruta>`
    y contrastelos. `Z-11` midio que la frase anterior —«un sobre existente es, por
    construccion, un sobre limpio»— era falsa, y se retira.
  6 RECALCULE LOS DIGEST DE LA SEDE CANONICA DEL OWNER y contrastelos con toda sede
    derivada que cite una resolucion suya. La AUTORIDAD es la sede; el registro de
    decisiones es una PROYECCION. Una parafrasis que AMPLIE el texto canonico es un
    hallazgo, y `O19` nacio exactamente de uno.
==============================================================================
LO QUE ESTE SOBRE **NO** GARANTIZA, y `O18` lo declara:
  compromiso del canal del Owner · compromiso simultaneo del repositorio y del
  coordinador · robo de credenciales · reescritura autorizada de ramas remotas ·
  manipulacion del ejecutor externo · falsificacion de identidad.
  Esos riesgos son del VERIFICADOR EXTERNO que `O18` contrata para `F6`, y que es
  condicion previa a la adopcion permanente de PesquerApp.
  Y LA SEDE CANONICA DEL OWNER NO ES MECANICAMENTE VERIFICABLE CONTRA UNA FUENTE
  EXTERNA AL SISTEMA, y lo declara el propio Owner. `O19` TRASLADA LA AUTORIDAD de
  la parafrasis del coordinador a `docs/owner/` y este sobre publica su huella, pero
  quien pueda escribir el repositorio puede escribir la sede: lo que el sobre prueba
  es que el texto no ha cambiado entre el commit auditado y lo que el revisor
  recibio FUERA del arbol, NO que sea el que el Owner emitio. Es la limitacion que
  `O18` declara de si misma —garantia TRANSITORIA y LIMITADA— y SIGUE VIGENTE hasta
  el verificador externo real de `F6`.
```

SHA-256 del fichero del sobre tal como lo recibí:

```text
731c282ac3305827f1e09ee4da0b7dc2f94be824e997d37376497616a0f0554c  /tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/f4c/SOBRE-6B.txt
```

### §0.2 · Las SEIS OBLIGACIONES, cumplidas con salida

#### OBLIGACIÓN 1 — recalcular LOS DOS DIGEST DE UNIVERSO, antes de leer nada

Receta ejecutada literalmente la del sobre, sobre cada commit, con su propio derivador
extraído de ese mismo commit a un directorio temporal fuera del repositorio.

```bash
for C in b27a761bb3eb6b0b1b3db2344b7184ef4b993309 ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759; do
d=$(mktemp -d)
GIT_INDEX_FILE="$d/idx" git read-tree "$C"
GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
  while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
  awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
rm -rf "$d"; done
```

```text
COMMIT b27a761bb3eb6b0b1b3db2344b7184ef4b993309  FUENTES=76  LINEAS=72592  DIGEST=68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b
COMMIT ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759  FUENTES=78  LINEAS=73164  DIGEST=33c27bd79da8154d1c04edf5df61cd8bfa078a53dc8cfda9316d88725ee6c34c
```

| campo | sobre | recalculado | ¿reproduce? |
|---|---|---|---|
| DIGEST UNIVERSO CANDIDATA | `68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b` | idéntico | **SÍ** |
| DIGEST UNIVERSO GATE | `33c27bd79da8154d1c04edf5df61cd8bfa078a53dc8cfda9316d88725ee6c34c` | idéntico | **SÍ** |
| FUENTES CANDIDATA / GATE | 76 / 78 | 76 / 78 | **SÍ** |
| LÍNEAS CANDIDATA / GATE | 72592 / 73164 | 72592 / 73164 | **SÍ** |
| TREE CANDIDATO | `0a0992a3b46dc7fa67f1321a86ac4a9e776e2472` | `git rev-parse b27a761^{tree}` → idéntico | **SÍ** |
| TREE GATE | `e945584aa3e52ca44f0ad79e6a235df3b4f63cb5` | `git rev-parse ce2cb42^{tree}` → idéntico | **SÍ** |

**LOS DOS DIGEST REPRODUCEN BYTE A BYTE. El gate NO es inválido por la obligación 1.**

#### OBLIGACIÓN 2 — el manifiesto EN EL COMMIT DEL GATE

```bash
git show ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md | sha256sum
41a4ff29d11c1edf26e6370ea7bcf8cf1ee24d75895336d991b6c12fa4251924  -
```

Coincide con el del sobre. **Leído del commit, no del árbol de trabajo.** 292 líneas.

#### OBLIGACIÓN 3 — cada fila del manifiesto contra EL ÁRBOL QUE DECLARA

El manifiesto declara en §1 que el objeto del reparto es el árbol de la CANDIDATA
(`0a0992a…`), y en §6 rotula CADA cifra con su árbol. Extraje las 76 filas (16 de §4 +
60 de §5) y contrasté ruta, líneas y SHA-256 contra los DOS árboles:

```text
filas extraidas: 76
docs/evolucion/00-INDICE.md  CAND:OK  GATE:SHA-DIFF/LIN(218)
TOTAL desviaciones CAND=0 GATE=1
```

**LAS 76 FILAS REPRODUCEN, RUTA POR RUTA, LÍNEA POR LÍNEA Y BYTE POR BYTE, SOBRE EL
ÁRBOL DE LA CANDIDATA — que es el árbol que declaran.** La única fila que no reproduce
sobre el árbol del GATE es `00-INDICE.md`, y ésa es exactamente una de las tres rutas
que el sobre publica como divergentes, y el propio manifiesto la anuncia en su preámbulo
(«este commit lleva CUATRO cosas y no una: el manifiesto, **su fila en `00-INDICE.md`**,
la evidencia derivada reejecutada y el registro»). **No es un hallazgo.**

La fila del PROPIO DERIVADOR —la que el sobre me manda mirar primero por `U-02`/`X-06`—
es la fila 8 de §4: `docs/evolucion/verificacion/derivar-universo-obligatorio.py`, 787
líneas, `77ffb37b…`. Reproduce sobre los DOS árboles:

```bash
git show b27a761…:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum
77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b  -
git show ce2cb42…:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum
77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b  -
```

Y la aritmética de §6 se sostiene sobre el árbol que declara:
`16 + 60 = 76` fuentes = FUENTES OBLIGATORIAS de la candidata;
`29855 + 42737 = 72592` = LÍNEAS OBLIGATORIAS de la candidata. **CIERRA A CERO.**
Sobre el árbol del GATE la resta declarada es `1` y es correcta: 78 − 76 asignadas − 1
(el `…-6-20260831.md`, el manifiesto retirado) = ... y aquí hay que ser exacto, ver §2.

#### OBLIGACIÓN 4 — la superficie en que candidata y gate no son el mismo objeto

```bash
diff <(universo candidata) <(universo gate)
31a32,33
> docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md
> docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md
```

más `docs/evolucion/00-INDICE.md`, que existe en los dos con contenido distinto
(`6eacea232af0…` → `ff0a9993c393…`). **Son las 3 que el sobre publica, exactas.**

PERO el árbol completo difiere en SEIS rutas, no en tres:

```bash
git diff --name-status b27a761… ce2cb42…
M	docs/evolucion/00-INDICE.md
A	docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md
A	docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md
M	kernel/operativo/pruebas/evidencia/fuentes-salida.txt
M	kernel/operativo/pruebas/evidencia/negativos-salida.txt
M	kernel/operativo/pruebas/evidencia/referencias-salida.txt
```

Las tres de `evidencia/` NO están en el universo obligatorio (`grep evidencia` sobre el
listado de rutas del derivador → nada). Su diferencia es el recuento de ficheros del
corpus, que se movió al añadir los dos manifiestos: `312 → 314` ficheros recorridos,
`265 → 267` documentos analizados. Es coherente y está anunciado. Lo anoto en §2 como
MENOR de precisión de redacción del sobre, no como defecto del corpus.

#### OBLIGACIÓN 5 — SHA-256 del EMISOR y del DERIVADOR en los DOS commits

```text
EMISOR    b27a761…  f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715
DERIVADOR b27a761…  77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b
EMISOR    ce2cb42…  f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715
DERIVADOR ce2cb42…  77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b
```

**Los CUATRO coinciden con los del sobre.** Y `git status --porcelain` sobre el árbol de
trabajo actual vino VACÍO en mi sesión — con la salvedad que el propio sobre declara:
eso sólo prueba que no hay modificaciones VISIBLES para `git status`. No lo uso como
prueba de nada más.

#### OBLIGACIÓN 6 — la SEDE CANÓNICA DEL OWNER

```text
SEDE b27a761… db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
  O17 b27a761… 0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125  (85 líneas)
  O18 b27a761… ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353  (111 líneas)
  O19 b27a761… cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8  (78 líneas)
SEDE ce2cb42… db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
  O17 ce2cb42… 0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125  (85 líneas)
  O18 ce2cb42… ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353  (111 líneas)
  O19 ce2cb42… cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8  (78 líneas)
```

**Los OCHO digest coinciden con el sobre, y los dos commits publican la misma sede byte a
byte, como el sobre afirma.** Los recuentos de líneas (85 · 111 · 78) también coinciden.
El barrido de sedes derivadas que atribuyen algo al Owner está en §2 y §3.

**VEREDICTO DE §0: EL GATE ES VÁLIDO por sus seis obligaciones de ancla. Sigo.**

---

## §1 · MANIFIESTO DE LECTURA

Todas las fuentes se extrajeron del COMMIT CANDIDATO `b27a761…` a un directorio fuera del
repositorio (`…/scratchpad/f4c/cand/`) con `git show <commit>:<ruta>`. **No leí ni un byte del
árbol de trabajo**, que en mi sesión estaba en el commit del GATE y por tanto publica un
`00-INDICE.md` DISTINTO (218 líneas, `ff0a9993c393…`) del que se me asignó.

| # | ruta | líneas | SHA-256 recalculado | ¿casa con el lote? | rangos leídos | unión | ÍNTEGRO |
|---|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 216 | `6eacea232af0be841614b85b62cc0e212b032a85d275c57d1b1e981db73ef7a6` | SÍ | L1–72 · L73–112 · L108–167 · L167–216 | L1–216 | **SÍ** |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11682 | `2d89dbe3725b8487e3d60721ac1f5ebd6704882a7472ce2f8a64daa6d2f06a79` | SÍ | ver §1.4 | ver §1.4 | **NO — ver §1.4** |
| 3 | `docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md` | 4526 | `e2c34215d92937fb467b1ffdb4e6654f66198ead4dac8128c411469bf86c297e` | SÍ | ver §1.4 | ver §1.4 | ver §1.4 |
| 4 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 4515 | `979fdcba16c7c53f0cf77f7dcbe724c2025aac007e88038a5172b03d0b70a648` | SÍ | ver §1.4 | ver §1.4 | ver §1.4 |
| 5 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1321 | `789b3fd62831dd4bee642f74bf7296b865fd1c427115a497cd673416cdd08cea` | SÍ | ver §1.4 | ver §1.4 | ver §1.4 |

Comando que las recalcula, todas de una vez:

```bash
for r in docs/evolucion/00-INDICE.md docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
         docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md \
         docs/evolucion/CHECKPOINT-ADS-NEXT.md docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md; do
  echo -n "$r "; git show b27a761bb3eb6b0b1b3db2344b7184ef4b993309:$r | sha256sum
done
```

**Los cinco SHA-256 reproducen exactamente los que el lote declara, y los cinco recuentos de
líneas también.**

### §1.2 · Los RANGOS leídos, y su unión

| ruta | rangos leídos, en el orden en que los leí | unión | ¿cubre lo asignado? |
|---|---|---|---|
| `00-INDICE.md` | L1–72 · L73–112 · L108–167 · L167–216 | **L1–216** | **SÍ, ÍNTEGRO** |
| `11-ARQUITECTURA-INTEGRADA.md` | L5201–5480 · 5480–5760 · 5760–6060 · 6060–6350 · 6350–6650 · 6650–6900 · 6900–6936 · 6935–7340 · 7340–7720 · 7720–8110 · 8110–8480 · 8480–8610 · 8600–8720 · 8718–8792 · 8780–8830 · 8830–8930 · 8930–9200 · 9200–9500 · 9500–9660 · 9660–10100 · 10100–10500 · 10500–10625 · 10620–10930 · 10930–11320 · 11310–11345 · 11340–11682 | **L5201–11682** | **SÍ, ÍNTEGRO sobre el rango asignado** |
| `26-QUINTO-GATE-…F4C.md` | L1–215 · 215–470 · 470–900 · 900–1260 · 1256–1305 · 1300–1560 · 1560–1990 · 1990–2400 · 2400–2900 · 2900–3400 · 3396–3455 · 3450–3760 · 3760–3980 · 3981–4045 · 4045–4526 | **L1–4526** | **SÍ, ÍNTEGRO** |
| `CHECKPOINT-ADS-NEXT.md` | L1–330 · 331–700 · 701–950 · 955–1135 · 1135–1274 · 1271–1312 · 1309–1470 · 1470–1700 · 1700–1950 · 1950–2110 · 2100–2280 · 2280–2390 · 2386–2540 · 2537–2760 · 2760–2935 · 2935–3135 · 3135–3350 · 3350–3393 · 3393–3516 · 3515–3625 · 3622–3752 · 3752–3980 · 3980–4280 · 4280–4515 | **L1–4515** | **SÍ, ÍNTEGRO** |
| `DECISIONES-Y-CONTRADICCIONES.md` | L1–120 · 120–330 · 330–545 · 545–760 · 760–935 · 935–1140 · 1140–1321 | **L1–1321** | **SÍ, ÍNTEGRO** |

**El documento 26 lo abrí EL ÚLTIMO**, cuando ya tenía formado el juicio sobre las otras
cuatro fuentes, como el lote ordena. Ninguno de mis hallazgos `R2-01`…`R2-10` se apoya en
él; `R2-11` nace de cotejarlo contra la proyección viva, que es exactamente lo que abrirlo el
último permite.

### §1.3 · Primera y última sección sustantiva, y DOS anclas de regiones separadas por fuente

```text
`00-INDICE.md`            primera  L14  «## Los documentos en voz del Owner»
                          última   L211 «## Lo que este trabajo ha corregido de sí mismo»
  ANCLA A · L128   «se enlaza desde la lista de abajo en el MISMO commit que lo crea»
  ANCLA B · L216   «hallazgo real es que la línea 2.0 nunca recogió lo que la 1.3.0 ya gobernaba»

`11-ARQUITECTURA…`        primera de mi rango  L5232 «## 5.2 · Aspectos y capacidades…»
                          última               L11515 «## `C-L.5` · La condición de COBERTURA…»
  ANCLA A · L8809  «Y UNA PROHIBICIÓN    el ejecutor externo no puede compartir la identidad…»
  ANCLA B · L10672 «EL TOTAL SE DERIVA … DIECINUEVE; menos PN-4 RETIRADA y PN-5 FUSIONADA…»

`26-QUINTO-GATE…`         primera  L10  «## 0 · Qué es este documento»
                          última   L4526 «**ADJUDICADOR `DD` · adjudicación cerrada…**»
  ANCLA A · L209   «**El sistema cierra INSTANCIAS y no CLASES.**»
  ANCLA B · L4013  «### 6.4 · RECUENTO, DERIVADO DE LAS FILAS»

`CHECKPOINT-ADS-NEXT.md`  primera  L2386 «## Estado de las fases» (todo lo anterior es el
                                   bloque de cabecera + el bloque de estado estructurado)
                          última   L4419 «## Siguiente acción exacta — HISTÓRICA, anterior
                                   al documento 22»
  ANCLA A · L873   «no aquí es EXACTAMENTE el defecto de X-04, y no cuenta como registrado»
  ANCLA B · L3542  «LOS SEIS DEL GATE, verificables en el propio documento 11:»

`DECISIONES-Y-CONTRA…`    primera  L11   «## 1 · Decisiones tomadas sin consultar»
                          última   L1303 «## 4 · Límites declarados de esta iteración»
  ANCLA A · L447   «La batería sigue teniendo **30 comprobaciones**: `G-15` se corrige en su sitio.»
  ANCLA B · L1188  «“LITERAL DE `O18`” cuando la fila corta de `O18` no lo contenía…»
```

### §1.4 · LA RESTA · `ASIGNADO − LEÍDO`

```text
ASIGNADO POR EL MANIFIESTO `6B` §4, filas 1, 2 (mitad R2), 3, 4 y 16

  docs/evolucion/00-INDICE.md                          216
  docs/evolucion/11-ARQUITECTURA-INTEGRADA.md  L5201–final     11682 − 5200 =  6482
  docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md       4526
  docs/evolucion/CHECKPOINT-ADS-NEXT.md                       4515
  docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md               1321
                                                            ──────
  ASIGNADO                                                    17060

LEÍDO ÍNTEGRO, por la unión de rangos de §1.2                 17060

  ASIGNADO − LEÍDO  =  **0**
```

**Y lo declaro CONTRA MI PROPIO INTERÉS, con las tres reservas que me obligan a matizarlo:**

1. **La unión de mis rangos cubre las 17 060 líneas, y eso es un hecho de mis comandos, no de
   mi memoria.** Cada rango es una invocación de `sed -n 'a,bp'` o de `Read` con `offset`/
   `limit` sobre el fichero extraído del commit candidato.
2. **De `11-ARQUITECTURA-INTEGRADA.md` L1–L5200 abrí regiones puntuales para verificar
   —§0, §2.1, §2.6.5, §2.6.7, §2.9— y NO las declaro leídas.** No cuentan como cobertura
   mía y no cuentan contra la de `R1`.
3. **Abrí además, fuera de mi lote y sólo para verificar**: `docs/owner/ADS-OWNER-RESOLUCIONES.md`
   (íntegro, 334 líneas, porque la obligación 6 me obliga), el manifiesto `6B` **en el commit
   del gate** (íntegro, 292 líneas, porque la obligación 2 me obliga), el manifiesto `-6-`
   (sólo su recuento de líneas), el derivador y el emisor (sólo su SHA-256 en los dos
   commits), la batería (regiones `G-10` L595-660 y `_ESTADOS_CL` L1470-1500), el
   `CORRIGENDUM` (sólo su índice de entradas) y el `README` de `verificacion/` (sólo su censo
   de `G-`). **Ninguno lo declaro leído.**

---

## §2 · HALLAZGOS QUE SOSTENGO

> **Convenio de clases**, el del propio gate: `A` coherencia interna · `B` identidad de la
> candidata · `C` resistencia a un actor privilegiado. `C` **no es exigible dentro de `F4c`**
> y no clasifico nada ahí.
> **Todas las líneas son del árbol de la CANDIDATA `b27a761…`** salvo donde digo lo contrario.

| id | sev | clase | sede (fichero:línea) | qué afirma la sede | qué dice el árbol (comando y salida) | qué se sigue |
|---|---|---|---|---|---|---|
| `R2-01` | **GRAVE** | A | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md`:69-70 y :223-226 (en el commit del GATE `ce2cb42…`) | §2: «la diferencia estructural es exactamente **+1 fuente: este fichero**». §6: «SOBRE EL ÁRBOL DEL GATE · OBLIGATORIO menos ASIGNADO **1** … la fuente que sobra es ESTE manifiesto» | La diferencia es **+2** y las fuentes sin asignar sobre el árbol del gate son **DOS**. `comm -23 <(universo gate) <(76 rutas asignadas)` → `…-6-20260831.md` **y** `…-6B-20260831.md`. Y el derivador da 76 (candidata) frente a **78** (gate): 78 − 76 = 2 | El apartado que `DD-19` creó para dejar de rotular mal las cifras publica **un cardinal falso sobre el árbol que dice describir**, y lo publica en el único sitio donde el gate declara la aritmética del árbol del gate. El propio preámbulo del manifiesto reconoce que el `…-6-` existe y queda publicado; §6 lo ignora al restar. Es la MISMA CLASE que `DD-18`/`DD-19` —un cardinal de manifiesto que su propio universo desmiente— reaparecida en el manifiesto del gate siguiente |
| `R2-02` | **GRAVE** | A | `docs/evolucion/00-INDICE.md`:126-132 (la regla) y :134-146 (la lista) | «Todo documento que `C-L.5` obligue a publicar —manifiesto de asignación, manifiestos de lectura, addenda y corrigenda— **se enlaza desde la lista de abajo en el MISMO commit que lo crea**», y :145 registra que el manifiesto `4B` «**Faltaba en ESTA lista**: sólo estaba enlazado desde la fila del gate … TERCERA recurrencia de `S-18`≡`T-14`» | `F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md` **no está en la lista**. `sed -n '134,146p' 00-INDICE.md \| grep -o 'verificacion/[A-Za-z0-9_./-]*\.\(md\|py\)' \| sort -u` → 11 rutas, **sin** el `-5-`. Sólo aparece en L93, la fila del gate: `grep -n 'CERTIFICACION-5-20260831' 00-INDICE.md` → **93** y nada más | **CUARTA recurrencia de la misma clase, viva en la candidata**, dentro de la lista que documenta las tres anteriores. Y el comando que la sede publica para comprobarse (:163-166) **no puede detectarla**: hace `grep` sobre el fichero ENTERO, no sobre la lista, de modo que un enlace desde la fila del gate lo satisface. Verificado: ese `diff` sale **VACÍO** sobre la candidata. El instrumento pasa en verde sobre la violación de la regla que dice guardar |
| `R2-03` | **GRAVE** | A | `docs/evolucion/CHECKPOINT-ADS-NEXT.md`:851-877 (`regla_de_reanclaje`, regla 4 en L871-874), :878 (`metodo`), :1001 (`based_on`), :1101 (`last_meaningful_event`) | `regla_de_reanclaje` regla 4: «TODO EVENTO NUEVO —un gate devuelto, una resolución del Owner, **una tanda aplicada**— REANCLA `metodo`, `last_meaningful_event` y `based_on` EN EL MISMO COMMIT QUE LO REGISTRA. **Un evento escrito en la cabecera de este fichero y no aquí es EXACTAMENTE el defecto de `X-04`, y no cuenta como registrado**». Y :851 «ESTE BLOQUE ES EL ESTADO REANUDABLE … describe el árbol VIGENTE» | El bloque va **UN EVENTO ATRASADO**. `grep -n '^metodo:\|^last_meaningful_event:' CHECKPOINT-ADS-NEXT.md` → L878 «**CUARTO** GATE DE CERTIFICACIÓN DEVUELTO … TANDA DE APLICACIÓN DE SUS HALLAZGOS EN CURSO» y L1101 «EL **CUARTO** GATE DE CERTIFICACIÓN DEVUELVE INSUFICIENTE … sobre la candidata `dc9be3f`». La lista de `based_on` (L1001-1080) termina en `25-CUARTO-GATE-…`: **el documento 26 no está**. `rama_de_trabajo` (L1095-1097) nombra «la candidata del CUARTO gate» como el snapshot que sí se nombra. Mientras tanto la cabecera (L14-50) y «Siguiente acción exacta» (L3622s) SÍ describen el QUINTO gate y esta tanda | La condición `C-L.7` —«el checkpoint reancla su estado en cada tanda»— **vuelve a estar FALSADA sobre el árbol que este gate juzga**, y por la forma exacta que su propia regla tipifica: el evento está en la cabecera y no en el bloque. Es la **QUINTA recurrencia** de la clase (`K-01`/`J-10`/`L-01` · `P-05`≡`Q-08`/`R-02` · `S-17`≡`S3-05` · `X-04` · ésta), y la primera cometida contra una regla escrita DENTRO del propio bloque para impedirla. Respuesta a la pregunta 7 del manifiesto: **NO reancla** |
| `R2-04` | **GRAVE** | A | `docs/evolucion/CHECKPOINT-ADS-NEXT.md`:2174-2181 (fila `C-L.5`, L2148-2205) y :2240-2245 (fila `C-L.7`, L2206-2271) | Fila `C-L.5` (L2174): «**MIENTRAS el primero devuelva 0, `G-16` dará ROJO** sobre esta clasificación … el vocabulario de estados primarios del instrumento **no conoce «ABIERTA»** … El remedio —«ABIERTA» en `_ESTADOS_CL` y en `_CANON`— vive en `docs/evolucion/verificacion/`, que este registro NO escribe; **en cuanto ese fichero lo incorpore**, el primer comando deja de dar 0». Fila `C-L.7` (L2240-2245): «**LO QUE ES VERDAD HOY, ejecutado sobre este árbol y no supuesto** … Lo que hoy la pone en rojo es OTRA cosa, y es la fila de `C-L.5`: **el vocabulario no conoce «ABIERTA»**» | **Falso en la candidata, y ya lo era en el árbol del quinto gate.** `git show b27a761…:docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py \| grep -c '"ABIERTA"'` → **2**; sobre `8c9ca9c` → **2**. La sede del vocabulario, batería L1479: `_ESTADOS_CL = ("CORREGIDAS EN F4c", "NO CERRADA", "ABIERTA", "REGISTRADAS PARA F5", "CONTRATADA PARA F6", "MIXTA POR DESGLOSE", "CERTIFICADA POR")`, y el comentario L1470-1478 dice que fue el CUARTO gate quien obligó a añadirlo | Es **`AA-02` otra vez**: una «consecuencia declarada» redactada en forma de autocrítica que **era falsa en el commit que la escribió** y sigue siéndolo. La fila de `C-L.7`, tres párrafos más abajo, narra ese mismo defecto para «NO CERRADA», declara haberlo cerrado y **remite a la fila de `C-L.5` como si allí siguiera vivo el rojo** — cerrando la INSTANCIA y dejando la CLASE en pie **en el mismo bloque y a 50 líneas**. Es literalmente la frase de `BB4`, medida en la sede que la cita |
| `R2-05` | **MEDIO** | A | `docs/evolucion/CHECKPOINT-ADS-NEXT.md`:3535-3556 (la reconciliación de «siete hallazgos aplicados») | «hecha **mecánicamente** y no por lectura … LOS SEIS DEL GATE, **verificables en el propio documento 11**: `DD-05 DD-07 DD-09 DD-10 DD-13 DD-14` — `grep -c 'DD-0[579]\|DD-1[034]' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`» | El comando **no cuenta identificadores: cuenta LÍNEAS**. Ejecutado sobre la candidata devuelve **23**, no 6 (`grep -o … \| sort -u \| wc -l` sí devuelve 6). Y el criterio que publica —«verificables en el propio documento 11»— lo satisfacen **SIETE** ids, no seis: `grep -o 'DD-[0-9][0-9]' 11-ARQUITECTURA-INTEGRADA.md \| sort -u` → `DD-05 DD-07 DD-09 DD-10 **DD-12** DD-13 DD-14`, y `DD-12` tiene corrección viva en §0, L195 | La reconciliación se declara mecánica y **no lo es en ninguna de sus dos mitades**: el comando publicado devuelve otro número, y el criterio publicado selecciona otro conjunto. La CONCLUSIÓN —retirar el cardinal en vez de sustituirlo— sigue en pie y es correcta; lo que no se sostiene es la comprobabilidad que el parte se atribuye, que es justo lo que `J-07`/`DD-13` exigen. Una cifra sin comando no es refutable; una cifra con un comando que cuenta otra cosa, tampoco |
| `R2-06` | **GRAVE** | A | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`:154-168 (§0, la regla de titulares) | «**No tiene GUARDIÁN.** La batería de corrección no la comprueba, y **el cardinal de esta afirmación tampoco se escribe: se DERIVA**, con `grep -cniE 'titular\|regla de titulares' docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` … **mientras ese comando devuelva 0, esta regla no tiene ni una comprobación mecánica**» | El comando devuelve **2** sobre la candidata. `git show b27a761…:…/comprobar-correccion-gate-de-cierre.py \| grep -niE 'titular\|regla de titulares'` → L608 «el modo de fallo que **la regla de titulares** de §0 persigue — y §0 nombra a `G-10` como su …» y L640 `f"su **titular** no dice «Son {_letra}»"`. Sobre el árbol del quinto gate `8c9ca9c` devolvía **0** | **Lo rompió esta misma tanda.** `DD-12` reescribió `G-10` para que DERIVE el censo de fichas y comprobara su titular; ese cambio hace que la derivación publicada en §0 —doce líneas más arriba de la excepción que `DD-12` precisa— **devuelva un valor que contradice la afirmación que ampara**. Y no es sólo el proxy: `G-10` hoy sí comprueba mecánicamente UN titular (L640), luego «la batería de corrección no la comprueba» es materialmente inexacto. La sede que este gate tiene que juzgar (pregunta 2 del manifiesto) **se autofalsifica con su propio comando**, en el commit que la tocó |

| `R2-07` | **GRAVE** | A | `docs/evolucion/CHECKPOINT-ADS-NEXT.md`:2344-2345, campo `falta_para_cerrar_la_capa` del BLOQUE DE ESTADO VIGENTE (L849-2385), **sin rótulo histórico** | «NADA PROBADO: las **46** filas de la tabla adversarial de §2.6.7 —**derivadas por conteo, no escritas a mano**; `X62` la añade **esta tanda** por `J-03`—» | Son **47**. El comando que la propia sede del documento 11 publica: `grep -cE '^\| \`X[0-9]{2}\` \|' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` → **47**; ids únicos → **47**. Y `X62` la añadió la tanda del gate definitivo, no ésta | **`DD-13` retiró este mismo cardinal del documento 11 EN ESTA MISMA TANDA** —11-ARQ:1722: «esta frase escribía «cuarenta y seis», y `X63` la dejó caducada en el acto»— y lo dejó vivo, con el mismo valor caducado, **una sede más allá**. La sede se autodescribe como «derivada por conteo, no escrita a mano» mientras escribe el número a mano. Y el barrido de `DD-13` no podía verlo: su patrón es `^\*\*.*<cardinal>` —titulares en negrita— y esto vive dentro de un bloque ```text``` |
| `R2-08` | **MEDIO** | A | `docs/evolucion/CHECKPOINT-ADS-NEXT.md`:2907-2926, bloque rotulado **«CIFRAS VIGENTES, DERIVADAS de la tabla de abajo y no copiadas de ningún resumen»** | «FILAS ADVERSARIALES **46** filas físicas · **46** ids únicos en §2.6.7» y «`PN-17` y `PN-18` son las que añade **esta tanda**, por `P-07` y `P-08`» | Filas adversariales: **47** (comando de `R2-07`). Y `git log --oneline -S'## \`PN-17\`' -- docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` → `609863e` (tanda de `O17`); `PN-18` → `609863e`; `PN-19` → `8e70d94` (tanda de `O18`). **Esta tanda no añadió ninguna presión** | Dos hechos caducados dentro del rótulo que promete lo contrario. El segundo es **la clase exacta de `Y-10`** del documento 25 —«las que ESTA tanda añade son `PN-17` y `PN-18`», declarada falsa y corregida en `pregunta_pendiente` (L1993-1999)—, **corregida en una sede y viva en la otra**. El propio bloque narra que caducó tres veces «bajo el rótulo CIFRAS VIGENTES, DERIVADAS» y vuelve a hacerlo |

| `R2-09` | **MEDIO** | A | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`:447, glosa de `D103` (fichero declarado «**Registro vivo**», L4) | «**La batería sigue teniendo 30 comprobaciones**: `G-15` se corrige en su sitio» — en presente y sin marca histórica | `git show b27a761…:docs/evolucion/verificacion/README.md \| grep -o 'G-[0-9]\+[a-z]*' \| sort -u \| wc -l` → **40**; y el manifiesto del gate §9 declara **38/38** de la batería. Ninguno es 30 | Es **`S-16`≡`S3-06` una sede más allá**. Aquel hallazgo retiró «30/30» del CHECKPOINT y lo sustituyó por el comando; la frase gemela del registro de decisiones —en presente, sin acotar y sin comando— sobrevivió a tres gates. La instancia se cerró, la clase no |
| `R2-10` | **MENOR** | A | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`:8789-8811, bloque «EL REPARTO, **LITERAL DE LA SEDE CANÓNICA DEL OWNER**» | «**Un bloque rotulado LITERAL es la sede, cláusula a cláusula, y nada más**; lo que este documento aporta va DEBAJO, con su propio rótulo» (:8797-8799, remedio de `DD-05`) | El bloque (L8809-8811) rotula la sexta cláusula como «**Y UNA PROHIBICIÓN DE IDENTIDAD**». La sede no la nombra así: `sed -n '/^· SIS define el contrato/,/^· el ejecutor externo/p' docs/owner/ADS-OWNER-RESOLUCIONES.md` devuelve seis viñetas planas, la sexta «· el ejecutor externo no puede compartir la identidad de escritura del runtime ADS». Los cinco primeros rótulos SÍ son el sujeto de su cláusula (`SIS`, `PLT`, `VER`, `SEG`, EL OWNER); el sexto es una **caracterización añadida** | El CONTENIDO de las seis cláusulas reproduce la sede exactamente —lo comprobé con el `sed` que el propio bloque publica—, así que **no hay amplificación de contenido**. Lo que hay es una glosa de rótulo dentro del bloque que `DD-05` acaba de limpiar de glosas, en la cláusula siguiente a las que limpió. Es la clase, una cláusula más allá; MENOR porque nada de lo que la sede dice queda ampliado ni recortado |

| `R2-11` | **MEDIO** | A | `docs/evolucion/00-INDICE.md`:93 (sede VIVA de la candidata), heredado de `docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md`:156-159 y :4013-4021 (documento INMUTABLE) | 00-INDICE:93 publica «**22 hallazgos: BLOQUEANTE 0 · GRAVE 12 · MEDIO 6 · MENOR 4**». Doc 26 §6.4 lo titula «**RECUENTO, DERIVADO DE LAS FILAS**» y da `DEL APARATO: GRAVE 2 · MEDIO 3 · MENOR 1` | **Derivado de las filas del propio `DD`**: `grep -oE '^\| \*\*\`DD-[0-9]{2}\`\*\* \| \*\*[A-ZÁÉÍÓÚ ]+\*\*' 26-…md \| sed … \| sort \| uniq -c` → **GRAVE 12 · MEDIO 4 · MEDIO ESTRUCTURAL 1 · MENOR 5**. Del aparato (`DD-17`..`DD-22`): `DD-17` GRAVE, `DD-18` GRAVE, `DD-19` MEDIO ESTRUCTURAL, `DD-20` MEDIO, `DD-21` MENOR, `DD-22` MENOR → **GRAVE 2 · MEDIO 2 · MENOR 2**, no `2 · 3 · 1`. Total real: **12 · 5 · 5**, no `12 · 6 · 4` | El bloque que se rotula «DERIVADO DE LAS FILAS» **no está derivado de sus filas**, y una sede VIVA lo copia. Es la clase de `F-12` (doc 16: «su tabla da 32 y 16, su prosa dice 29 y 13») y la de `L` en el doc 19 («cinco graves» con seis ids), que el corpus resolvió **sin tocar el documento inmutable, reanclando la PROYECCIÓN VIVA y publicando la entrada en el CORRIGENDUM**. Aquí no se hizo ninguna de las dos: el `CORRIGENDUM` (`git show b27a761:…/CORRIGENDUM-DICTAMENES-INMUTABLES.md \| grep '^## '`) tiene 16 entradas y ninguna sobre el recuento del documento 26 — sus §14 y §15 son sobre el MANIFIESTO del quinto gate. **Ningún revisor del quinto gate ni esta tanda derivaron el recuento del dictamen que aplican** |
| `R2-12` | **MENOR** | A | El SOBRE, obligación 4, y `docs/evolucion/00-INDICE.md`:60 y :148-150 (nota de método) | El sobre: «RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: **3** … son **la superficie exacta en que la candidata y el gate no son el mismo objeto**» | Los UNIVERSOS difieren en 3 rutas — verificado, y reproduce. Pero los **ÁRBOLES** difieren en **SEIS**: `git diff --name-status b27a761… ce2cb42…` añade `kernel/operativo/pruebas/evidencia/{fuentes,negativos,referencias}-salida.txt`, que **no pertenecen al universo obligatorio** (`grep evidencia <rutas del derivador>` → nada) | La frase del sobre es verdadera de los UNIVERSOS y **falsa de los OBJETOS**: hay tres rutas más en que candidata y gate no son el mismo objeto, y son precisamente las que `DD-17` obliga a reejecutar. No induce a error a un revisor disciplinado —el propio commit lo anuncia— pero **el sobre publica como «superficie exacta» una superficie que es subconjunto propio de la real**. Lo declaro contra el instrumento que me ancla, no contra la candidata |


### §2.1 · Recuento de mis hallazgos, derivado de las filas de arriba

```text
BLOQUEANTE   0
GRAVE        6    R2-01 · R2-02 · R2-03 · R2-04 · R2-06 · R2-07
MEDIO        4    R2-05 · R2-08 · R2-09 · R2-11
MENOR        2    R2-10 · R2-12
             ──
            12

POR CLASE
  A · coherencia interna, corregible dentro de `F4c`   12
  B · identidad de la candidata                         0
  C · actor privilegiado                                0   (no exigible en `F4c`)
DECISIÓN DEL OWNER                                      0
```

**Ninguno es BLOQUEANTE. Ninguno exige arquitectura nueva. Ninguno vuelve al Owner.**
Los doce se cierran con material que el corpus ya tiene escrito.

**A qué árbol pertenece cada uno** —el sobre obliga a decirlo—:

```text
DE LA CANDIDATA `b27a761` (objeto auditado)   R2-02 · R2-03 · R2-04 · R2-05 · R2-06 ·
                                              R2-07 · R2-08 · R2-09 · R2-10 · R2-11
DEL APARATO DEL GATE `ce2cb42`                R2-01 (manifiesto 6B)
DEL SOBRE                                     R2-12
```

**Diez de mis doce son del objeto auditado.** No mezclo: `R2-01` no cuenta contra la
candidata, y que la candidata esté limpia no absuelve al manifiesto.

---

## §3 · EL ATAQUE A LA CLASE

> La frase que ordena esta tanda es de `BB4`, doc 26 L209-211: «**El sistema cierra
> INSTANCIAS y no CLASES.** La corrección se aplica con la forma sintáctica exacta del
> contraejemplo, y el defecto reaparece una sede más allá». **La tanda dice haberse escrito
> contra ella.** Para cada clase que dice haber cerrado, fui a la sede UNA MÁS ALLÁ.

| clase que la tanda declara cerrada | dónde busqué la sede una más allá | qué encontré |
|---|---|---|
| **`DD-13` · la regla de titulares, barrida ahora sobre `^\*\*.*<cardinal>` y no sólo sobre `^#`** —remedio literal que `BB1` recomendó y `DD` ordenó (doc 26 §10.6 punto 2)— | El patrón nuevo sigue siendo **una FORMA SINTÁCTICA** (negrita al principio de línea). Busqué el mismo defecto **fuera de esa forma**: cardinales escritos junto a su enumeración **dentro de bloques ```` ```text ```` de campos estructurados** | **CAE. `R2-07` y `R2-08`.** `CHECKPOINT`:2344 escribe «las **46** filas de la tabla adversarial —derivadas por conteo, no escritas a mano—» cuando son **47**, y :2926 escribe «**46** filas físicas · **46** ids únicos» bajo el rótulo «CIFRAS VIGENTES, DERIVADAS … y no copiadas de ningún resumen». **Es EL MISMO cardinal que `DD-13` retiró del documento 11 en esta misma tanda** (11-ARQ:1722). El barrido no podía verlo porque no es un titular en negrita |
| **`DD-06` · las atribuciones al Owner, barridas «por el ACTO y no por la tipografía»** | Barrí TODA sede que atribuya algo al Owner: `grep -nE '«[^»]{15,}»'` filtrado por `owner\|O1[789]` sobre las cuatro fuentes; comparé el bloque LITERAL de §11.8 contra la sede con el `sed` que él mismo publica; recalculé `grep -c robustez` sobre la sede | **NO CAE en su sustancia.** Las cuatro apariciones vivas de «robustez…» están rotuladas RESUMEN con su `DD-06`; las históricas van marcadas. El reparto LITERAL reproduce la sede **cláusula a cláusula** con el `sed` publicado. **Cae sólo un residuo MENOR:** el bloque LITERAL rotula la sexta cláusula «**Y UNA PROHIBICIÓN DE IDENTIDAD**», caption que la sede no tiene — `R2-10`. Es la misma clase (una glosa dentro de un bloque LITERAL), una cláusula más allá de las que `DD-05` limpió |
| **`DD-08` / `C-L.7` · el checkpoint reancla su estado en cada tanda** | Fui al bloque que la propia `regla_de_reanclaje` designa como sede del reanclaje —`metodo`, `last_meaningful_event`, `based_on`— en vez de a la cabecera que `DD-08` corrigió | **CAE, y es lo más grave que traigo. `R2-03`.** La cabecera SÍ está reanclada al quinto gate; el BLOQUE DE ESTADO, no: `metodo:` y `last_meaningful_event:` nombran el **CUARTO** gate y `based_on` termina en el documento **25**. La regla 4, escrita dentro del propio bloque, dice: «*Un evento escrito en la cabecera de este fichero y no aquí es EXACTAMENTE el defecto de `X-04`*». **La instancia (`DD-08`, la cabecera) se cerró; la clase (`C-L.7`, el bloque) no** |
| **`DD-12` · `G-10` deriva de verdad, y §0 precisa su excepción** | Fui a la OTRA afirmación de §0 que depende del mismo instrumento: la derivación que publica para sostener «no tiene guardián» | **CAE. `R2-06`.** `grep -cniE 'titular\|regla de titulares' <batería>` devolvía **0** sobre el árbol del quinto gate —así lo midió `BB4` en `BB-13`— y devuelve **2** sobre la candidata, porque el `G-10` nuevo comprueba un titular (L640) y su comentario nombra la regla (L608). §0 sigue diciendo «*mientras ese comando devuelva 0*». **La tanda cerró `DD-12` y falsificó, en el mismo commit, la derivación de §0 doce líneas más arriba de la viñeta que `DD-12` precisa** |
| **`DD-19` · «de qué árbol habla cada cifra», con las DOS aritméticas publicadas** | Apliqué la regla al primer caso nuevo: un gate cuyo commit publica **DOS** manifiestos (el retirado `-6-` y el efectivo `-6B-`) | **CAE. `R2-01`.** La regla se escribió para la instancia —«la diferencia es exactamente **el manifiesto en curso**»— y el manifiesto `6B` la aplicó literalmente: «+1 fuente: este fichero», «OBLIGATORIO menos ASIGNADO **1**». Sobre el árbol del gate sobran **DOS**. Es exactamente la sexta recurrencia que `BB4` predijo (doc 26 §6.4: «*si nadie toca el enunciado, el gate 6 registrará una sexta reincidencia*») — con el agravante de que **sí se tocó el enunciado**, y aun así falla, porque se tocó para el caso conocido |
| **`S-18`≡`T-14` → `Y-03`≡`Z-09` · el manifiesto se enlaza desde la LISTA de `00-INDICE`** | La lista documenta tres recurrencias y su corrección. Fui al manifiesto SIGUIENTE al corregido: el `-5-20260831` | **CAE. `R2-02`.** El `-5-` sólo está enlazado desde la fila del gate (L93), que es literalmente el defecto que L145 describe para el `4B`. Y el comando que la sede publica para autocomprobarse **no puede detectarlo**: hace `grep` sobre el fichero entero. Lo ejecuté: sale VACÍO |
| **`AA-02` · «una consecuencia declarada que era FALSA en el commit que la escribió»** | La fila `C-L.7` narra el caso «NO CERRADA» y lo declara cerrado. Fui a la fila gemela, `C-L.5`, con el mismo párrafo condicional | **CAE. `R2-04`.** `grep -c '"ABIERTA"' <batería>` devuelve **2** en la candidata y devolvía **2** ya en el árbol del quinto gate. La fila `C-L.5` sigue diciendo «*mientras ese comando devuelva 0, `G-16` dará ROJO … en cuanto ese fichero lo incorpore*», y la fila `C-L.7`, 50 líneas más abajo, remite a ella como si el rojo siguiera vivo. **`AA-02` cerrado para «NO CERRADA», vivo para «ABIERTA», en el mismo bloque** |
| **`S-16`≡`S3-06` · «30/30» retirado del checkpoint y sustituido por el comando** | Fui a la frase gemela en el registro de decisiones | **CAE. `R2-09`.** `DECISIONES`:447 sigue diciendo, en presente y sin acotar, «La batería sigue teniendo **30 comprobaciones**». Hoy el README censa **40** ids y el manifiesto declara **38/38** |
| **`DD-01` · el perímetro por NATURALEZA (el octavo árbol)** | **NO ES MI DOMINIO** — es el instrumento, lote de `R1`. No construí ningún árbol y no busqué el noveno | **NO ATACADA POR MÍ, y lo declaro.** Mi silencio no es evidencia en ninguna dirección (§6) |
| **`DD-05` · el bloque LITERAL es la sede cláusula a cláusula** | Coteje las seis cláusulas contra la sede con el `sed` publicado | **NO CAE en el contenido.** Las seis reproducen exactamente, en el mismo orden, sin recorte ni ampliación. Sólo el rótulo de la sexta es añadido (`R2-10`, MENOR) |
| **`DD-09` · el barrido de clase de `D105`** | Barrí las sedes que afirman qué retira el marcador, fuera de las tres que `DD-09` nombra | **NO CAE.** No encontré ninguna sede viva con la forma previa dentro de mi rango |
| **`DD-10` · el censo de `X-S` deja de escribirse y remite** | `grep -rn 'X-S9'` sobre las cuatro fuentes + doc 11 | **NO CAE.** Las once filas existen (`grep -cE '^\| \`X-S[0-9]+\`'` → 11) y las apariciones de «`X-S1`–`X-S9`» sobreviven **sólo** en regiones históricas: `00-INDICE`:88 (fila del gate del doc 22), `CHECKPOINT`:365/979/1217/4335 (`[ESTADO ANTERIOR]`, `metodo_anterior`, `last_meaningful_event_anterior`, «Siguiente acción exacta — HISTÓRICA») y en el propio doc 26, inmutable |
| **`DD-16` · el puntero del índice a «la PRIMERA sección titulada»** | Comprobé el puntero y su derivación | **NO CAE.** `00-INDICE`:96-106 remite a la PRIMERA y publica el comando; `grep -c '^## Siguiente acci[óo]n exacta' CHECKPOINT` → **8**, y las históricas son **7**, coherente con la cabecera |
| **`DD-17` · el commit del manifiesto lleva CUATRO cosas y no una** | Lo ejecuté sobre los DOS árboles, que es lo que `DD` pidió al gate siguiente (doc 26 §10.6 punto 3) | **NO CAE, y es el mejor resultado de la tanda.** Ver §4 |

---

## §4 · LO QUE VERIFIQUÉ Y NO CAYÓ

**Pesa tanto como lo que cayó, y va con su comando.**

### 4.1 · `DD-17`, la QUINTA recurrencia, está ROTA — y lo ejecuté yo en los dos árboles

Es la regla que cinco gates seguidos incumplieron y cuyo remedio de una línea `Y4` dejó
escrito, `BB4` citó y `DD` ejecutó pidiendo que el gate 6 lo hiciera. **Lo hizo.**

```bash
git show --stat ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759
 docs/evolucion/00-INDICE.md                                 |   3 +-
 …/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md          | 292 +++++
 kernel/operativo/pruebas/evidencia/fuentes-salida.txt       |   2 +-
 kernel/operativo/pruebas/evidencia/negativos-salida.txt     |   2 +-
 kernel/operativo/pruebas/evidencia/referencias-salida.txt   |   2 +-
 5 files changed
```

Y ejecutado por mí en checkouts aislados fuera del repositorio (`read-tree` +
`checkout-index`), con Python 3.12.14:

```text
                                       CANDIDATA b27a761      GATE ce2cb42
comprobar_referencias.py --exclusiones  T147 SUPERADA          T147 SUPERADA
                                        1 superadas·0 fallidas 1 superadas·0 fallidas
registrar_evidencia.py                  13/13 · 0 problemas    13/13 · 0 problemas
ficheros de evidencia que la batería
reescribe sobre su propio árbol         0                      0
```

**Sobre el árbol del gate anterior, `DD` midió `12/13`, `T147` FALLIDA y DOS ficheros de
evidencia sucios. Sobre éste, ninguno de los tres. La quinta recurrencia consecutiva de
`S-18`≡`T-14` está rota en su consecuencia mecánica.** (Que la LISTA del índice siga sin
enlazar el `-5-` es `R2-02`, y es otra cosa: `T147` no lo ve porque L93 lo enlaza.)

### 4.2 · El sobre y su ancla — reproducen enteros

Los dos digest de universo, las dos cifras de fuentes y de líneas, los dos trees, el
SHA-256 del manifiesto en el commit del gate, el del EMISOR y el del DERIVADOR en los DOS
commits, la sede canónica entera y los tres digest de resolución con sus tres recuentos de
líneas: **reproducen todos, sin una diferencia**. Y las **76 filas del manifiesto** casan
contra el árbol de la candidata **sin una discrepancia de ruta, de líneas ni de SHA-256**.
La fila del propio derivador —la que el sobre manda mirar PRIMERO— es idéntica en los dos
árboles: **`U-02`/`X-06` sigue sin reincidir**.

### 4.3 · Las derivaciones vivas que el corpus publica, ejecutadas una a una

```bash
awk '/^## 15\.8 /{f=1;next} f&&/^## /{exit} f&&/^### /{n++} END{print n}' 11-ARQ.md   → 18
grep -c '^## `PN-' 11-ARQ.md                                                          → 19
grep '^## `PN-' 11-ARQ.md | grep -vc 'RETIRADA\|FUSIONADA'                            → 17
awk '/^\| `(DD|BT)-[0-9]/{n++} END{print n}' CHECKPOINT.md                            → 24
awk '/^\| `DD-[0-9]/{n++} END{print n}' CHECKPOINT.md                                 → 22
awk '/^\| `BT-[0-9]/{n++} END{print n}' CHECKPOINT.md                                 →  2
grep -c '^## Siguiente acci[óo]n exacta' CHECKPOINT.md                                →  8   (7 históricas + 1 vigente)
grep -c '^## Siguiente acci[óo]n exacta — HISTÓRICA' CHECKPOINT.md                    →  7
grep -cE '^\| `X-S[0-9]+`' 11-ARQ.md                                                  → 11
grep -cE '^\| `X-O[0-9]+`' 11-ARQ.md                                                  → 13
grep -cE '^\| `?O[0-9]+' 11-ARQ.md                                                    → 13   (§15.4: O7…O19)
git diff --name-only 05f71b7 b27a761 -- kernel/                                       →  6 ficheros, los seis enumerados
```

**Todas cuadran con lo que su sede declara.** El censo de `PN` de §16 (19 cabeceras menos
`PN-4` RETIRADA y `PN-5` FUSIONADA = 17) es exacto, y su rango vivo `PN-6`–`PN-19` termina
en la última cabecera vigente, que es lo que la garantía de §16 exige.

### 4.4 · `PN-18` — los recuentos que dice derivar, se derivan

Ejecutados sobre un checkout aislado de la candidata:

```text
grep -c 'VER:decisión' docs/rediseno/b-RECORRIDO-APROBADA.md   → 12   (la sede dice 12)
grep -rn 'VER:decisión' kernel/ | wc -l                        →  3   (la sede dice 3)
grep -rn 'VER:decision' kernel/ packs/ | wc -l                 → 14   (la sede dice 14)
grep -rn ':revisión' kernel/ | wc -l                           →  0   (la sede dice 0)
grep -rn ':revision' kernel/ | wc -l                           →  0   (la sede dice 0)
```

**Los cinco reproducen exactamente**, y `3 + 14 = 17` cuadra con «las diecisiete del kernel
y los packs». Es la sede que mejor cumple la disciplina que el corpus predica.

### 4.5 · La matriz de los 43 hallazgos — su recuento SÍ está derivado de sus filas

```text
estados primarios contados sobre las filas de CHECKPOINT:2945-3005
  31 CORREGIDO_EN_F4 · 2 PRESION_LISTA_PARA_F5 · 2 CONTRATO_COMPLETO_PARA_F6 ·
   7 EXTERNO_CON_PROPIETARIO · 1 HISTORICO_NO_APLICABLE  =  43
severidades: BLOQUEANTE 4 · GRAVE 6 · MEDIO 20 · MENOR 13  =  43 filas
```

Coincide fila a fila con lo que el bloque «RECUENTO DERIVADO DE LAS 43 FILAS» publica.
**Contraste con `R2-11`: aquí sí está derivado, y por eso la excepción destaca.**

### 4.6 · Las atribuciones al Owner — la sede canónica manda y las proyecciones no la amplían

- `grep -c 'robustez' docs/owner/ADS-OWNER-RESOLUCIONES.md` → **0**, y las cuatro sedes vivas
  que usan la frase la rotulan RESUMEN con su `DD-06`, con el literal separado y su comando.
- El censo de proyecciones que enlazan a la sede, con el `awk` que `DD-14` publica:
  `O17 → 5 · O18 → 3 · O19 → 1`, y `O7`–`O14`, `O15`, `O16` → 0, que es lo correcto
  (`O1`–`O16` no se registran en la sede, por orden literal del Owner).
- `grep -rn 'No elijo la alternativa barata' docs/` → **cuatro golpes**, uno de ellos la sede
  canónica: la afirmación de `BT-01` de que el literal ya es contrastable es cierta.
- El reparto LITERAL de §11.8 y los diez puntos de «Lo que `O19` declara» de la proyección
  reproducen la sede **cláusula a cláusula**. **Cero amplificación de contenido.**

### 4.7 · `X63` NO se presenta como prueba ejecutada ni como certificación presente

Barrí las SEIS apariciones de `X63` en todo el árbol de la candidata
(`00-INDICE`:94 · `CHECKPOINT`:3580, :3613 · `11-ARQ`:1694, :3695, :5497, :5656, :5668):

- `11-ARQ`:1694 es una **fila de §2.6.7**, cuya cabecera de sección declara que todas son
  contratos no ejecutados; `11-ARQ`:3695 y §19 la cuentan entre lo **ESCRITO, no ejecutado**.
- `11-ARQ`:5668: «*es un **contrato de prueba de `F6`** … **y no se ejecuta aquí***».
- `CHECKPOINT`:3613: «*`X63` **NO ES UNA PRUEBA** … **NO se ha ejecutado, NO certifica nada**
  y NO es una protección interna nueva*».
- `00-INDICE`:94: «*`X63` es CONTRATO DE PRUEBA DE `F6`, **no una prueba ejecutada ni una
  certificación presente***».

**Ninguna sede lo presenta como ejecutado.** La única frase con tensión es `11-ARQ`:5656
—«y **`X63`** la comprueba validando las tres celdas…»—, en presente; pero es el mismo
tiempo verbal con que el documento escribe TODAS sus filas `X<nn>` («`X47` comprueba…»),
y queda desambiguada doce líneas más abajo en el mismo bloque. **No lo cuento como hallazgo.**

### 4.8 · `M-04` y el estado de `F4c` — nada se declara CERRADO ni SUPERADO indebidamente

Barrido sobre las cuatro fuentes vivas: `M-04` aparece siempre como **NO superada / FALLIDA /
sigue viva**; `F4c` siempre **ABIERTA**; `F5` siempre **NO AUTORIZADA**; el PARTE declara
expresamente «NINGÚN HALLAZGO SUPERADO … ni uno». **No encontré ni una sede viva que
declare CERRADO o SUPERADO algo que no lo esté.** El único «CERRADO» que la tanda escribe
—«`AA-01` CERRADO y generalizando», «`AA-05` CERRADO»— es **transcripción del veredicto
del quinto gate**, que sí los declaró cerrados, y va atribuida a él.

### 4.9 · La excepción exacta del kernel — derivada y correcta

```bash
git diff --name-only 05f71b7 b27a761 -- kernel/     → 6 ficheros
  kernel/.upstream-hash · kernel/operativo/entrada/02-CIRCUITO.md ·
  kernel/operativo/validadores/comprobar_negativos.py ·
  kernel/operativo/pruebas/evidencia/{fuentes,negativos,referencias}-salida.txt
```

Los seis, uno a uno, son los que `CHECKPOINT`:3250-3280 enumera. **`3 directos + 3 de
evidencia derivada = 6`, y la cifra la deriva `G-23`.**

### 4.10 · El documento 26, cotejado donde el corpus lo cita

- Los **22** identificadores `DD-01`…`DD-22` del dictamen están **todos** en el PARTE de la
  tanda, más `BT-01` y `BT-02`. **La enumeración es completa.**
- Doc 26 escribe, literal, «`C-L.5` **no se reabre por cobertura**» (L142 y L4380) y
  «`C-L.5` **no se reabre por la resta en este gate**. Se reabre —o no— por lo demás»
  (L3536) y «`C-L.5` **no se reabre por nada que yo traiga**» (L4443). Barrí las **once**
  apariciones de `CERTIFICADA` en el documento —`grep -n 'CERTIFICADA' 26-…md`— y **las
  once son CITAS**: de las dos sedes defectuosas que `BB-06`/`DD-07` denuncian, del
  checkpoint que `BB-07`/`DD-08` denuncian, o de la reapertura que el documento 25 hizo.
  **`DD` no escribe esa palabra como acto suyo ni una sola vez.** La premisa de la que
  parte la decisión de la tanda es cierta.
- La prosa de `DD` cruza mal sus propios identificadores en tres puntos (§`D-1` llama `DD-17`
  al rótulo del manifiesto, §`D-3` llama `DD-07` a la promesa, §5.6 enumera «`DD-16`, `DD-17`,
  `DD-18`» como los tres del aparato, que en su tabla son seis). **La tanda resolvió esto
  correctamente: su PARTE sigue la TABLA de `DD`, no su prosa.** Lo consigno porque el
  contraste importa para `R2-11`: la tanda cotejó los ids y no cotejó el recuento.


### 4.11 · `C-L.5` · el razonamiento de la tanda es CORRECTO, no una evasión

El manifiesto me pregunta esto expresamente. **Contesto: es CORRECTO.**

```text
LO QUE EL QUINTO GATE MIDIÓ    `OBLIGATORIO − ASIGNADO = 0` contra el objeto que el
                               manifiesto declara repartir · `ASIGNADO − LEÍDO = 0`
LO QUE EL QUINTO GATE ESCRIBIÓ «`C-L.5` no se reabre por cobertura» — y nada más
LO QUE LA TANDA HIZO           dejarla ABIERTA con la medición registrada, y decir por qué
                               no pone la palabra
```

**Por qué es correcto y no evasión, y va con la regla del propio corpus delante:**

1. **`C-L.5` es una condición cuyo estado sólo se mueve por un ACTO del adjudicador.** El
   documento 25 la reabrió «*como adjudicación expresa … no como consecuencia del
   veredicto*» (doc 26, `BB-06`). Simétricamente, cerrarla exige un acto expreso.
2. **`DD` tuvo la ocasión de escribirla y no la escribió.** Verificado: las once apariciones
   de `CERTIFICADA` en su documento son citas ajenas (§4.10). Un coordinador que dedujera la
   palabra de las cifras del adjudicador estaría **derivando un acto de una medición**.
3. **El corpus tiene esto tipificado dos veces y lo castigó las dos.** `Q-06` cerró el
   mutante «escribir CERTIFICADA para poner la batería en verde»; `AA-02` castigó una
   consecuencia declarada a partir de un condicional. Escribir la palabra aquí sería
   exactamente eso.
4. **La tanda no se escuda: publica la medición completa** (`CHECKPOINT`:2184-2205, párrafo
   «LO QUE EL QUINTO GATE MIDIÓ, Y POR QUÉ ESTE RENGLÓN NO SE MUEVE») **y traslada la
   pregunta a este gate**, en «Siguiente acción exacta» punto 7. Una evasión no publica la
   medición que la contradiría.

**Es la conducta correcta. No lo cuento como hallazgo, y lo digo con la misma fuerza con que
digo lo que sí cuento.**

### 4.12 · La coherencia transversal entre las cuatro sedes — sin contradicción viva salvo las nombradas

Coteje, estado por estado, `00-INDICE` · `CHECKPOINT` · `11-ARQ` · `DECISIONES`:

```text
`F4c` ABIERTA                    coincide en las cuatro
`F5` NO AUTORIZADA               coincide en las cuatro
`M-04` NO superada               coincide en las cuatro
`C-L.5` ABIERTA                  coincide: CHECKPOINT (clasificación vigente) es la sede
                                 única, `11-ARQ` §C-L.5 RETIRA su estado y remite (`DD-07`),
                                 `00-INDICE` no lo publica
`C-L.7` NO CERRADA               coincide en las cuatro
la serie `D1`–`D108`             108 ids, de 1 a 108, SIN HUECOS ni duplicados
la serie `O1`–`O19`               19 ids, de 1 a 19, SIN HUECOS; `O1`–`O16` NO en la sede
                                 canónica, por orden literal del Owner, y §11.9 lo declara
```

Derivado, no leído:

```bash
python3 -c "import re,io; s=io.open('docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md',encoding='utf-8').read();
 ds=sorted({int(m) for m in re.findall(r'^\| D(\d+) ',s,re.M)});
 os_=sorted({int(m) for m in re.findall(r'^\| O(\d+) ',s,re.M)});
 print(len(ds),[i for i in range(1,109) if i not in ds], len(os_),[i for i in range(1,20) if i not in os_])"
→ 108 []  19 []
```

**Las contradicciones vivas que encontré son las DOCE que sostengo en §2, y ninguna más.**

---

## §5 · REFUTACIONES CONTRA MIS PROPIAS CONCLUSIONES

Intenté **ocho**. **Tres cayeron** —y una de ellas retiró un hallazgo entero de mi censo—;
cinco no. Publico las ocho, cayeran o no.

### `RF-1` · **CAYÓ · «`R2-01` no es un hallazgo: el `-6-` no cuenta porque fue retirado»**

La defensa natural del coordinador. El manifiesto `6B` declara que el `-6-` «*queda publicado
como historia, no se mueve y no se edita*», luego podría sostenerse que no es una fuente
asignable y que la resta de §6 habla sólo de manifiestos vivos.

**NO CAE.** El universo obligatorio **no distingue manifiestos vivos de retirados**: es la
salida del derivador, y `manifiestos/` es ZONA BARRIDA entera desde `AA-01`. Lo verifiqué:

```bash
comm -23 <universo del gate> <las 76 rutas asignadas>
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md
```

**Son DOS, y el `-6-` está tan dentro del universo como el `6B`.** Y el propio §2 del
manifiesto no dice «los manifiestos vivos»: dice «**+1 fuente: este fichero**», que es una
afirmación sobre el árbol y es falsa. **Se sostiene.**

### `RF-2` · **CAYÓ A MEDIAS · «`R2-01` es del aparato, luego no cuenta contra la candidata»**

**Cae en su primera mitad y la acepto**: `R2-01` es del árbol del gate y **no cuenta contra
el objeto auditado**. Lo reparto así en §2.1, y quien quiera fundar insuficiencia de la
candidata **no puede hacerlo con `R2-01`**.

**No cae en la segunda**, y es la doctrina que `BB4` y `DD` fijaron: el defecto del aparato
mide la disciplina del gate que viene a certificar. Y aquí hay un agravante propio: **la regla
que se incumple es la que esta misma tanda escribió** (`DD-19`), en el primer caso que la
puso a prueba.

### `RF-3` · **CAYÓ · «`R2-06` es una nimiedad: el comando es un proxy, no la afirmación»**

Intenté demostrar que §0 sólo usa el `grep` como indicador y que la afirmación de fondo
—«la regla de titulares no tiene guardián»— sigue siendo cierta.

**CAYÓ CONTRA MÍ, y el hallazgo sale peor.** Fui al código:

```bash
git show b27a761…:…/comprobar-correccion-gate-de-cierre.py | sed -n '630,645p'
                falta.append(f"§5.2: su enumeración da {_n} fichas ({', '.join(_EXT_FICHA)}) y "
                             f"su titular no dice «Son {_letra}»")
```

**`G-10` comprueba HOY, mecánicamente, que un titular concreto diga el cardinal que su
enumeración deriva.** Es literalmente una comprobación mecánica sobre un titular. Luego
«**La batería de corrección no la comprueba**» no es sólo un proxy caducado: es
materialmente inexacto para el caso que §0 declara su única excepción. **Sube, no baja.**

### `RF-4` · **NO CAYÓ · «`R2-03` es benevolente con el resto del checkpoint: si el bloque va atrasado, TODO el fichero lo está»**

Intenté agravarlo hasta decir que el checkpoint entero describe el cuarto gate.
**NO CAE, y cae contra mi agravamiento:** la cabecera (L14-50), «Estado de las fases»
(L2489-2503), la clasificación vigente de `C-L` (L2107-2271) y «Siguiente acción exacta»
(L3622-3750) **SÍ** están reancladas al quinto gate y a esta tanda, verificado sede a sede.
**El defecto está acotado al bloque estructurado, y es exactamente por eso que es `X-04`**:
la clase se define como «el evento está en la cabecera y no en el bloque».

### `RF-5` · **NO CAYÓ · «`R2-07`/`R2-08` caen porque `falta_para_cerrar_la_capa` es histórico»**

La salida más cómoda: si el campo estuviera dentro de una región `[HISTÓRICO]`, no sería
defecto vivo, y mi propia disciplina me obliga a decirlo. **Lo comprobé línea a línea.**

```text
CHECKPOINT L2327  · **[HISTÓRICO · el censo del momento de esa tanda]** TRECE PRESIONES…
CHECKPOINT L2341  · NADA CONSTRUIDO: …                       ← viñeta NUEVA, sin marca
CHECKPOINT L2344  · NADA PROBADO: las **46** filas …          ← viñeta NUEVA, sin marca
```

La marca `[HISTÓRICO]` **abre y cierra dentro de su propia viñeta `·`**, y las dos viñetas
siguientes no la heredan. Y el bloque de L2907-2926 lleva el rótulo contrario:
«**CIFRAS VIGENTES, DERIVADAS … y no copiadas de ningún resumen**». **NO CAE.**

### `RF-6` · **CAYÓ · «hay una decimotercera: §16 escribe DIECINUEVE y DIECISIETE junto a su enumeración»**

Iba a contarlo como violación de la regla de titulares: §16 (L10680-10684) escribe los dos
cardinales al lado de la lista de `PN`.

**CAYÓ.** §0 declara esa excepción con nombre y apellidos: «*un cardinal cuya enumeración NO
está al lado y que se publica **con el comando que lo deriva**, en la sede única que lo
publica —**así está §16**—*». Y los dos números **reproducen** (`grep -c '^## \`PN-'` → 19;
menos RETIRADA/FUSIONADA → 17). **Retirado de mi censo. Un hallazgo menos.**

### `RF-7` · **CAYÓ A MEDIAS · «`R2-11` no es mío: el defecto está en un documento INMUTABLE»**

Cierto en su mitad, y lo declaro: **el error aritmético vive en el documento 26, que es
histórico e inmutable, y por mi propia disciplina un defecto dentro de material inmutable no
es un defecto vivo.** Por eso **no lo cuento contra el documento 26**.

**No cae en la otra mitad**, y es la que sostengo: `00-INDICE`:93 **es una sede VIVA de la
candidata** y publica el reparto erróneo; y el corpus tiene procedimiento escrito para
exactamente esto —no tocar el inmutable, reanclar la proyección viva, entrada en el
CORRIGENDUM— que ejecutó dos veces (`F-12` para el doc 16, el corrigendum externo para el
doc 19) **y que aquí no ejecutó**. Lo mantengo, y en MEDIO y no en GRAVE por esa mitad.

### `RF-8` · **NO CAYÓ · «`R2-02` cae porque `T147` está en verde: la regla se cumple en su fin»**

La defensa más fuerte contra `R2-02`. Si el fin de la regla es que ningún documento sea
huérfano, y `T147` pasa, la regla se cumple.

**NO CAE, por dos vías.** (i) **La regla no dice eso.** Dice «*se enlaza desde la **lista de
abajo**… No se resuelve añadiéndolo a `exclusiones.yaml`: una exclusión **apaga** `T147` en
vez de cumplirlo*» — distingue expresamente el fin del medio. (ii) **El corpus ya juzgó esta
defensa y la rechazó**: L145 registra que el `4B` «*sólo estaba enlazado desde la fila del
gate*» y lo cuenta como TERCERA recurrencia, con `T147` en el mismo estado. Aceptarla ahora
sería cambiar de criterio en el sexto gate, que es lo que el expediente castiga.

### Qué cambiaron estas ocho en mi informe

```text
· un hallazgo RETIRADO del censo (RF-6): §16 está amparada por la excepción de §0
· `R2-06` SUBE de proxy caducado a inexactitud material (RF-3), contra mi propia refutación
· `R2-01` queda REPARTIDO al aparato y no cuenta contra la candidata (RF-2)
· `R2-11` queda ACOTADO a la proyección viva y NO se imputa al documento inmutable (RF-7)
· `R2-03` queda ACOTADO al bloque estructurado, contra mi propio agravamiento (RF-4)
```

**Cuatro de los cinco movimientos van contra el interés de mi propio censo.**

---

## §6 · LO QUE MI LOTE NO CUBRE, SIN ADORNO

**Una resta que da cero esconde esto, y por eso va aquí y no en una nota al pie.**

1. **NO he leído `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` L1–L5200.** Es el lote de
   `R1`. De ese tramo abrí **sólo** las sedes puntuales que sostienen lo que afirmo —§0
   (L150-240), §2.1 (L394-470), §2.6.5 (L1313-1400), §2.6.7 (L1680-1760), §2.9 (L3688-3700),
   §5.2 (L5195-5200)— y las declaro **abiertas para verificar, no leídas**. Un defecto en las
   otras ~5000 líneas se me escapa, y `R1` es quien lo vería.
2. **NO he auditado el INSTRUMENTO como código.** La batería (3873 líneas), el derivador
   (787) y el emisor (688) son lote de `R1`. Los ejecuté y leí regiones puntuales —`G-10`
   L595-660, `_ESTADOS_CL` L1470-1500, `_estado_casa`, `_EXCLUIDO`, `NORMATIVO`—. **No
   sostengo nada sobre su corrección como programas.**
3. **`M-04` como proposición general: NO ATACADA POR MÍ.** No construí un solo árbol
   defectuoso y no busqué el noveno. **Mi silencio no es evidencia en ninguna dirección**, y
   el adjudicador no debe leerlo como tal. Es lote de `R1`.
4. **El CORRIGENDUM, el README de `verificacion/` y los siete manifiestos anteriores: no
   leídos.** Los abrí sólo para dos comprobaciones puntuales (el índice de entradas del
   corrigendum, el censo de `G-` del README). Son lote de `R1`.
5. **No puedo verificar que `R1` lea lo que declare.** La resta `ASIGNADO − LEÍDO` de la otra
   cadena la cruza el adjudicador, no yo, y es exactamente la que hundió al cuarto gate.
6. **No he ejecutado ni una sola de las pruebas que el corpus describe** —las 47 filas
   `X<nn>`, las 18 ventanas `W`, las 11 `X-S`, las 13 `X-O`, las 8 `X-A`–`X-H`, los 11
   escenarios `NP`, los 12 de §14—. **Todo es contrato escrito y ninguno se ha ejecutado**, y
   ninguna cantidad de hallazgos coherentes sustituye ese hecho.
7. **No he juzgado las otras doce condiciones `C-L`.** Verifiqué el estado de `C-L.5` y de
   `C-L.7` con su medición; de las once restantes **sólo comprobé que la clasificación
   vigente lista cada id exactamente una vez y suma 13**. No he auditado si el estado que cada
   una declara es cierto.
8. **La sede canónica del Owner no es verificable contra nada externo, y lo declara ella
   misma.** Recalculé sus cuatro digest y son idénticos en los dos commits. **Eso prueba que
   el texto no cambió entre el commit auditado y lo que recibí fuera del árbol. NO prueba que
   sea el que el Owner emitió.** Sigue vigente hasta el verificador externo de `F6`.
9. **Los SHA-256 del emisor y del derivador que verifiqué NO prueban que los binarios que
   corrieron fueran ésos.** El propio sobre lo retira (`Z-11`) y yo no lo recupero.
10. **No he juzgado si la arquitectura es buena.** Sé qué dicen sus sedes y si se
    contradicen. **No opino sobre el diseño, y no lo insinúo.**
11. **`A14` es limitación aceptada, no hallazgo.** Con el `python3` 3.10 del sistema caen
    `arranque`, `fuentes` y `workspace` por `tomllib`. Todo lo que ejecuté fue con **Python
    3.12.14**, y lo digo.
12. **Reproducibilidad:** todo se midió con Python 3.12.14 y `git` sobre WSL2. No probé otro
    intérprete ni otro sistema de ficheros.

---

## §7 · MI RESPUESTA A LA PREGUNTA DEL GATE

> **NO. En lo que a mi dominio toca, `F4c` NO ES SUFICIENTE PARA `F5`: la tanda que dice
> haberse escrito contra «el sistema cierra INSTANCIAS y no CLASES» vuelve a cerrar
> instancias, y lo mido en seis clases distintas —el checkpoint no reancla su bloque de
> estado (`C-L.7`, quinta recurrencia de `X-04`, contra una regla escrita dentro del propio
> bloque), el manifiesto del gate publica un cardinal falso sobre el árbol que él mismo
> nombra en el apartado que `DD-19` creó para eso, §0 se autofalsifica con su propio comando
> por culpa del remedio de `DD-12`, el cardinal que `DD-13` retiró del documento 11 sigue
> vivo en dos sedes del checkpoint rotuladas «VIGENTES, DERIVADAS», la fila `C-L.5` conserva
> intacto el defecto `AA-02` que su fila gemela declara cerrado, y el manifiesto del quinto
> gate sigue sin enlazarse desde la lista que documenta las tres recurrencias anteriores de
> esa misma clase— sin que ninguno de los doce sea BLOQUEANTE, exija arquitectura nueva ni
> vuelva al Owner, y con `DD-17` —la quinta recurrencia que cinco gates no pudieron romper—
> ROTA y verificada por mí en los dos árboles.**


---

## §8 · DISCIPLINA — declaración de cierre

```text
git status --porcelain   AL ABRIR   →  VACÍO
git status --porcelain   AL CERRAR  →  VACÍO
git status --porcelain --untracked-files=all  AL CERRAR  →  VACÍO
HEAD al abrir y al cerrar           →  ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759, idéntico
FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ   ninguno
COMMITS · PUSH · PR · MERGE · RAMAS                             ninguno
CÓMO LEÍ                            `git show <commit>:<ruta>` a copias FUERA del
                                    repositorio, en el scratchpad. Ni un byte del árbol
                                    de trabajo, que además está en el commit del GATE y
                                    publica un `00-INDICE.md` distinto del asignado
CÓMO EJECUTÉ                        checkouts aislados (`git read-tree` + `git
                                    checkout-index --prefix`) en directorios temporales
                                    fuera del repositorio, borrados al terminar
INTÉRPRETE                          Python 3.12.14 (shim del encargo). Con el 3.10 del
                                    sistema caen `arranque`, `fuentes` y `workspace` por
                                    `tomllib`: es `A14`, limitación aceptada, NO hallazgo
SUBAGENTE `Agent`                   NO USADO
NINGÚN HALLAZGO CORREGIDO           y es deliberado: quien corrige no certifica.
                                    NO propongo correcciones al repositorio
```

**REVISOR `R2` · informe cerrado.**
**No emito veredicto de certificación: es del adjudicador `EE`.**

---

## §C · ADJUDICACIÓN DE `EE` — TRANSCRIPCIÓN LITERAL

# ADJUDICACIÓN `EE` — SEXTO GATE DE CERTIFICACIÓN DE F4c

Adjudicador `EE`. Contexto limpio. No he escrito nada de este corpus, no he aplicado
ninguna corrección, no he sido revisor de ningún gate anterior. **No he modificado
un solo byte del repositorio auditado**; todo árbol escribible que he necesitado lo
he creado fuera, en el scratchpad.

Fecha de adjudicación: 2026-08-31.

---

## §0 · EL SOBRE, Y LA COMPROBACIÓN DE LOS BLOQUES EMBEBIDOS

### §0.0 · Entorno y estado del repositorio auditado

```
$ export PYTHONPATH=.../scratchpad/py312-libs; export PATH=.../scratchpad/bin:$PATH
$ python3 -V
Python 3.12.14
$ git rev-parse HEAD
ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759
$ git status --porcelain
(vacío)
$ git ls-files -v | grep -v '^H '
(vacío)   # ni un fichero en skip-worktree ni assume-unchanged: la obligación 5 del
          # sobre queda comprobada por su lado comprobable
```

`A14` (los tres validadores que caen con el `tomllib` del Python 3.10 del sistema) es
limitación aceptada y no la cuento como hallazgo.

### §0.1 · Obligación 1 — LOS DOS DIGEST DE UNIVERSO, recalculados con la receta del sobre

```
$ for C in b27a761... ce2cb42...; do d=$(mktemp -d)
  GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum ; rm -rf "$d"; done

DIGEST b27a761 (CANDIDATA) = 68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b   RUTAS = 76
DIGEST ce2cb42 (GATE)      = 33c27bd79da8154d1c04edf5df61cd8bfa078a53dc8cfda9316d88725ee6c34c   RUTAS = 78
```

**Los dos reproducen BIT A BIT** los del sobre (`68ee8f1b…`, `33c27bd7…`), y también
las dos cardinalidades de FUENTES OBLIGATORIAS que el sobre publica (76 / 78).

### §0.2 · Obligación 2 — el manifiesto, leído EN EL COMMIT DEL GATE

```
$ git show ce2cb42...:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md | sha256sum
41a4ff29d11c1edf26e6370ea7bcf8cf1ee24d75895336d991b6c12fa4251924
```
Coincide con el SHA-256 del sobre.

### §0.3 · Obligación 5 — emisor y derivador, recalculados de LOS DOS commits

```
EMISOR    b27a761 f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715
DERIVADOR b27a761 77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b
EMISOR    ce2cb42 f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715
DERIVADOR ce2cb42 77ffb37bd3b559246b1ebcc58fe99e37c7119b13005ec8be1fa563439bcb3f6b
```
Los cuatro coinciden con el sobre.

### §0.4 · Obligación 6 — la sede canónica del Owner

```
SEDE  b27a761 / ce2cb42 = db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a  (idéntica en ambos)
O17   0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125   85 líneas
O18   ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353  111 líneas
O19   cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8   78 líneas
```
Los cuatro digest y los tres cardinales de líneas reproducen. La sede es byte a byte
la misma en los dos commits, como el sobre declara.

### §0.5 · LA COMPROBACIÓN QUE INVALIDA EL GATE SI FALLA — los bloques embebidos

`R1` embebe el sobre en `INFORME-R1.md` líneas 19–212 (dentro del fence abierto en 18).
`R2` lo embebe en `INFORME-R2.md` líneas 16–209 (fence abierto en 15). Extraídos:

```
$ sha256sum sobre-R1.txt sobre-R2.txt SOBRE-6B.txt
731c282ac3305827f1e09ee4da0b7dc2f94be824e997d37376497616a0f0554c  sobre-R1.txt
731c282ac3305827f1e09ee4da0b7dc2f94be824e997d37376497616a0f0554c  sobre-R2.txt
731c282ac3305827f1e09ee4da0b7dc2f94be824e997d37376497616a0f0554c  SOBRE-6B.txt
$ diff sobre-R1.txt SOBRE-6B.txt && diff sobre-R2.txt SOBRE-6B.txt && diff sobre-R1.txt sobre-R2.txt
IDENTICO / IDENTICO / IDENTICO   (194 líneas los tres)
```

**LOS DOS REVISORES EMBEBIERON EL MISMO SOBRE, BYTE A BYTE, Y ES ESTE FICHERO.**
No hay divergencia de sobres. El gate NO se invalida por esta vía y sigo adelante.

_(continúa)_

---

## §1 · MI MANIFIESTO DE LECTURA Y LAS DOS RESTAS

### §1.1 · Qué he leído yo

Como adjudicador, el manifiesto `6B` me asigna **una** fuente de lectura: la fila 3,
`docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md` («los tres · DESPUÉS de las demás
fuentes»). Lo he abierto **el último**, después de reproducir todos los hallazgos.

Además he leído íntegros, porque el encargo me los da:

```
/tmp/.../scratchpad/f4c/SOBRE-6B.txt                                194 líneas · 731c282a…
/tmp/.../scratchpad/f4c/informes/INFORME-R1.md                     1421 líneas
/tmp/.../scratchpad/f4c/informes/INFORME-R2.md                      999 líneas
git show ce2cb42:…/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md  292 líneas · 41a4ff29…
docs/evolucion/25-…  y  docs/evolucion/26-…                (leídos AL FINAL, como se me ordena)
```

Y he abierto **acotado, para verificar y no como lectura**, las regiones que cada hallazgo
me obliga a mirar: `00-INDICE.md`, `CHECKPOINT-ADS-NEXT.md`, `11-ARQUITECTURA-INTEGRADA.md`,
`DECISIONES-Y-CONTRADICCIONES.md`, la batería, el derivador, el emisor, el `CORRIGENDUM`, el
`README` de `verificacion/` y la sede del Owner. **No declaro lectura íntegra de ninguna de
ellas**, y lo digo aquí y no en una nota al pie.

### §1.2 · LAS DOS RESTAS DE ESTE GATE, derivadas por mí

**Cómo derivo `ASIGNADO`** (las 76 filas del manifiesto, §4 + §5, extraídas del commit del
gate y no transcritas):

```
$ git show ce2cb42:…/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md \
    | grep -oP '^\| *[0-9]+ *\| `\K[^`]+' | LC_ALL=C sort > asignado.txt
$ wc -l asignado.txt        →  76
```

**`OBLIGATORIO − ASIGNADO`:**

```
$ comm -23 univ-b27a761.txt asignado.txt          # ÁRBOL DE LA CANDIDATA
(vacío)                                            →  0
$ comm -13 univ-b27a761.txt asignado.txt          # y ninguna fila sobra
(vacío)                                            →  0

$ comm -23 univ-ce2cb42.txt asignado.txt          # ÁRBOL DEL GATE
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md
                                                   →  2
```

**SOBRE EL ÁRBOL DE LA CANDIDATA —el objeto que este gate juzga— `OBLIGATORIO − ASIGNADO = 0`,
exactamente. SOBRE EL ÁRBOL DEL GATE, `= 2`, y el manifiesto `6B` §6 publica `1`.** Esto es
`R1-02` ≡ `R2-01`, y lo resuelvo en §2.

La fuente que el manifiesto no cuenta:

```
$ git show ce2cb42:…/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md | wc -l      → 278
$ git show ce2cb42:…/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md | sha256sum
528dd68fc81134c16f874ab5803996ec50ee838241fd95470a9e07dd66770b2c
```
Es un fichero **distinto** del manifiesto en curso, **inmutable**, **de 278 líneas**, y su
SHA-256 es perfectamente escribible dentro del `6B`. **La justificación de PUNTO FIJO de
`DD-19` no le alcanza.**

### §1.3 · `ASIGNADO − LEÍDO`, sobre los manifiestos de lectura de `R1` y `R2`

Reparto declarado por el manifiesto `6B` §4 (16 filas):

```
R1  filas 2(L1–L5200) 3 5 6 7 8 9 10 11 12 13 14 15                          = 13 fuentes
R2  filas 1 2(L5201–final) 3 4 16                                            =  5 fuentes
EE  fila 3                                                                   =  1 fuente
UNIÓN de las filas cubiertas                                                 = 16 de 16
```

`R1` declara 13 de 13 íntegras y publica sus rangos; `R2` declara 5 de 5 y publica los suyos.
**Verifiqué las dos uniones aritméticamente**, no por lectura de su prosa:

```
R1 · doc 11    rangos [1,340][341,1100][1101,1740][1741,2360][2361,2980][2981,3600]
               [3601,4220][4221,4820][4821,5210]      UNIÓN = [1,5210] ⊇ [1,5200]   CUBRE
R2 · doc 11    26 rangos de [5201,5480] a [11340,11682], encadenados sin hueco
               UNIÓN = [5201,11682]                                                 CUBRE
   R1 ∪ R2 sobre el doc 11 = [1,11682] = el fichero entero (11682 líneas)           CUBRE
R1 · doc 26    [1,490][490,1009][1010,1569][1570,2129][2130,2689][2690,3249]
               [3250,3809][3810,4369][4370,4526]      UNIÓN = [1,4526]              CUBRE
R2 · doc 26    15 rangos de [1,215] a [4045,4526]     UNIÓN = [1,4526]              CUBRE
R2 · CHECKPOINT 24 rangos                             UNIÓN = [1,4515]              CUBRE
R2 · 00-INDICE  4 rangos                              UNIÓN = [1,216]               CUBRE
R2 · DECISIONES 7 rangos                              UNIÓN = [1,1321]              CUBRE
R1 · las 11 fuentes instrumentales · rangos publicados, unión = [1,n] en las once   CUBRE
```

**Las 16 filas del reparto quedan cubiertas y ninguna unión deja hueco.**

```
ASIGNADO − LEÍDO = 0
```

**Y digo lo que esta resta NO dice**, porque el corpus ya fue castigado por no decirlo:
no dice que ningún ojo haya recorrido el documento 11 entero —`R1` cubre L1–L5200 y `R2`
L5201–L11682, y una contradicción a caballo de L5200 es estructuralmente invisible para los
dos—. El propio manifiesto lo declara en su L106 y los dos revisores lo declaran contra su
propio interés. **Lo consigno como LÍMITE DE MÉTODO del gate, no como hallazgo.**

_(continúa)_

---

## §2 · REPRODUCCIÓN, HALLAZGO A HALLAZGO

**Disciplina del banco.** No he tocado `/home/jose/ads-kernel`: ni un byte, ni un commit, ni
una referencia. Todo ataque se ejecuta en
`git clone /home/jose/ads-kernel …/scratchpad/f4c/clon-EE`, con `HEAD` desprendido en la
candidata y `git checkout -f b27a761 && git clean -qfdx` entre uno y otro. Los digest se
calculan con la receta del sobre sobre árboles materializados en `$(mktemp -d)`.

Línea base del banco:
```
$ cd clon-EE && git rev-parse HEAD                                  b27a761…
$ python3 …/comprobar-correccion-gate-de-cierre.py                  38/38 · rc=0
$ python3 …/derivar-universo-obligatorio.py --rutas | wc -l         76
```

### `R1-01` · **SOSTENIDO · BLOQUEANTE · clase `A`** — EL NOVENO ÁRBOL

Lo reproduje **yo**, en el clon desechable, en sus dos variantes.

**Variante D — segunda sede normativa en `docs/normativa/`:**

```
$ mkdir -p docs/normativa && cat > docs/normativa/ADS-SENTENCIA-DE-CIERRE-F4C.md <<'X'
# SENTENCIA DE CIERRE DE `F4c` — PREVALECE SOBRE TODO
Esta sede **PREVALECE SOBRE TODO** el corpus. Declara **`F4c` CERRADA** y
**`F5` AUTORIZADA**. La condición de cobertura `C-L.5` queda sin efecto y
ningún gate de certificación posterior es exigible.
X

##### SIN COMMITEAR #####
FALLO G-29 └─ AMPLIACIÓN NO CLASIFICADA del corpus gobernado, rastreada o no:
              docs/normativa/ADS-SENTENCIA-DE-CIERRE-F4C.md
37/38 comprobaciones en verde

##### COMMITEADO ·  git add -A && git commit  (SIN UN SOLO FLAG) #####
$ git status --porcelain                                     []      VACÍO
$ python3 …/comprobar-correccion-gate-de-cierre.py           38/38 comprobaciones en verde
$ python3 …/derivar-universo-obligatorio.py --rutas | wc -l  76      UNIVERSO INTACTO
$ commit atacado                                             cce139c84bbd2f8b5fbeabd0969c28b48017c690
$ (RECETA DEL SOBRE sobre el commit atacado)
  68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b
  ANCLADO EN EL SOBRE PARA LA CANDIDATA:
  68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b     BIT A BIT IDÉNTICO
$ EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 0
$ (la sede atacada en cualquier salida del derivador)         0 ocurrencias
```

**Variante E — el mismo fichero del CUARTO GATE, `C8-SEGUNDA-SEDE-NORMATIVA.md`, con un
bloque canónico `ads:proceso` dentro** (el segundo control de `G-29`, el de unicidad de
bloque canónico, es igual de inerte):

```
--- SIN COMMITEAR ---   FALLO G-29 · 37/38
--- COMMITEADO ---      git status []  ·  38/38 comprobaciones en verde  ·  universo 76
                        digest 68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b
```

**CUMPLE LAS SEIS CONDICIONES que el quinto gate exigió al octavo árbol:** alcanza el commit ·
`git status` vacío · **38/38** · fuera del universo obligatorio · sin fila de manifiesto ni
revisor asignado · **produce el digest que el sobre ancla, bit a bit**. Y añado una séptima que
mido yo: **no aparece en NINGUNA de las salidas del aparato** —ni en `EXCLUIDOS_IV`, ni en
`EXCLUIDOS_PERIMETRO`, ni en el sobre que el emisor produciría—. **Es silencioso en las cinco
salidas.**

**CLASE `A`, y la frontera está fijada en su sede.** `DD-20`, en «El criterio del gate
siguiente» de `CHECKPOINT-ADS-NEXT.md` (L3445-3480), dice literalmente:

> «`A` COHERENCIA INTERNA — el defecto está EN EL CORPUS y la batería lo da por bueno. **Que
> el fichero esté o no CONFIRMADO es IRRELEVANTE: el objeto que un gate juzga es un COMMIT, y
> confirmar es lo que hace el coordinador en su propia rama de revisión**»
> «`C` ACTOR PRIVILEGIADO — corromper la REFERENCIA … reescribir `HEAD`, las refs o la
> revisión base · editar la batería, su README o el derivador · mentir el runner · cualquiera
> de los SEIS actos que `O18` enumera»

Mi ataque usa `git add -A && git commit`, **sin un solo flag**. No reescribe `HEAD`, ni refs,
ni la base; no toca la batería, su README ni el derivador; no miente el runner; y no es
ninguno de los seis actos de `O18`. **Es clase `A`, cuenta, y no se descarta por estar
confirmado.**

**ES LA MISMA CLASE QUE `DD-02` DEL QUINTO GATE, UNA ZONA MÁS ALLÁ.** `DD-02` diagnosticó que
la guarda de admisión de `G-29` es **inerte sobre todo fichero ya en `HEAD`**, y el remedio se
acotó a `docs/owner/` (el bucle `_owner_publicado`, batería L3060-3069). Fuera de esa zona la
guarda sigue inerte, y el «corpus gobernado» que el título de `G-29` reclama es el repositorio
entero. **La tanda que se rotula a sí misma «la CLASE en vez de la instancia» (`00-INDICE.md`
L94) cerró `DD-02` como INSTANCIA.**

Y hay una consecuencia que agrava y que no es retórica: **el título de `G-29` y la fila L244
del README son hoy afirmaciones FALSAS del instrumento** —«topología y unicidad de TODO el
corpus gobernado: sin ampliaciones sin clasificar … y sin segundas sedes»—. Eso es la **sexta
condición de `O18`**: ninguna promesa de seguridad superior a la realmente entregada.

### `R1-02` ≡ `R2-01` · **SOSTENIDO · GRAVE · clase `A`** — y **SON UN SOLO HALLAZGO**

Los dos afirman el mismo defecto sobre el mismo objeto: el cardinal del §6 del manifiesto `6B`
sobre el árbol del gate. **`R2-01` añade una segunda sede del mismo error** (§2 L69-70, «la
diferencia estructural es exactamente **+1 fuente: este fichero**»), que `R1-02` no cita. Es la
MISMA cifra errónea en dos apartados del MISMO fichero. **Cuenta UNO**, con dos sedes.

El encargo me advierte de «cifras distintas»: **no las hay.** Los dos miden `2`, y yo también:

```
$ comm -23 <(universo del árbol del gate, 78 rutas) <(76 rutas asignadas por el manifiesto)
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md
   →  2      El manifiesto §6 publica  1
$ 78 − 76 = 2                                El manifiesto §2 publica  +1
```

La fuente que sobra y que la justificación de punto fijo **no cubre**:
```
$ git show ce2cb42:…/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md | wc -l         278
$ git show ce2cb42:…/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md | sha256sum
  528dd68fc81134c16f874ab5803996ec50ee838241fd95470a9e07dd66770b2c
```
Es un fichero **distinto** del `6B`, inmutable, y su SHA-256 **es escribible dentro del `6B`**.
El argumento de `DD-19` —«un manifiesto no puede contener su propio SHA-256»— alcanza al `6B` y
**no al `-6-`**. Consecuencia material: **una fuente obligatoria de 278 líneas del árbol del
gate no está asignada a nadie, y ninguna sede lo dice.**

Agravante que sostengo con la cita: el §16 del propio `CORRIGENDUM` ordena «TODA CIFRA VA CON
SU COMANDO … Ninguna se copia», y este cardinal se copió de la entrada §15 —donde ERA correcto,
porque el quinto gate publicó UN manifiesto—. **Es el apartado que `DD-19` creó para dejar de
mentir sobre el árbol del gate, y es erróneo en su primer uso.**

### `R1-03` · **SOSTENIDO · MEDIO · clase `A`**

El §5 del manifiesto `6B` (L142-145) se atribuye «la REGLA MÁS ESTRICTA QUE EL ÁRBOL SOSTIENE:
una fuente sólo se agota si **su SHA-256 de HOY coincide byte a byte con el que publicó el gate
que la certificó**». Abrí las líneas citadas por las filas que `R1` nombra:

```
fila 15 → doc 26 L1978   | 8 | `…25-CUARTO-GATE…` | 2754 | — | LEÍDO ÍNTEGRO…      SIN HUELLA
fila 16 → doc 22 L2642   | 1 | `…ADS-PENDIENTES…` | L380 | ✓ LEÍDO ÍNTEGRO |      SIN COLUMNA DE HUELLA
fila 18 → doc 26 L1972   | 2 | `docs/owner/ADS-ARQUITECTURA…` | 3343 | `24da5be1…` (blob)
fila 19 → doc 26 L1973   | 3 | `docs/owner/ADS-IDEAS…`        |  597 | `b0766d5d…` (blob)
fila 13 → doc 25 L878    `0f81f13d8cb319d8…`     16 hex
fila 14 → doc 25 L879    `8df584529c857c07…`     16 hex
filas 55/56/57 → doc 21 L1056-1058   `315b2790cb66bb4c` `750d39a29f05e7f2` `1716bd3d8b48107d`  16 hex
```

**La regla LITERAL es insatisfacible para 2 de sus 60 filas** (no hay huella ninguna que
comparar) **y sólo satisfacible con otra función hash o con 16 hex para 7 más.** La COBERTURA
no está rota —la regla 2 real se cumple en las 60, y lo verifiqué—; lo que falla es **la
descripción que el manifiesto hace de su propio rigor**. Es la clase de la entrada §5 del
`CORRIGENDUM` («describe de más su propia evidencia»), reincidente en un manifiesto nuevo.

### `R1-04` · **SOSTENIDO · MEDIO · clase `A`**

La cabecera del derivador (L52-58) promete: «Si una sede no se puede leer … **sale con código 2
y diagnóstico** … **Y eso se EJECUTA, no se promete**». `_leer()` (L131-137) captura sólo
`OSError`. Un `UnicodeDecodeError` es `ValueError`. **Lo ejecuté**, sobre `ARQ`, que `_leer` sí
lee:

```
$ python3 -c "d=open('docs/evolucion/11-ARQUITECTURA-INTEGRADA.md','rb').read();
             open(…,'wb').write(d[:200]+b'\xff\xfe'+d[200:])"
$ python3 …/derivar-universo-obligatorio.py --rutas > o.txt 2> e.txt ; echo rc=$?
rc=1
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 200: invalid start byte
$ grep -c 'FALLA CERRADO' e.txt        0
$ wc -l < o.txt                        0        ← STDOUT VACÍO
```
Y la batería, en la MISMA situación, **sí** falla cerrado y lo nombra:
```
FALLO G-00 └─ SEDE ILEGIBLE …→ docs/evolucion/11-ARQUITECTURA-INTEGRADA.md: no es UTF-8
```
**El derivador promete un modo de fallo que una de sus lecturas no ejecuta**, y es la misma
clase que `T-22` cerró en el fichero de al lado. Consecuencia que agrava: la RECETA DEL SOBRE
canaliza `2>/dev/null`, luego entregaría **una lista de rutas vacía y el digest de la cadena
vacía**, sin decir por qué. Hoy es LATENTE (no hay sede no-UTF-8) y por eso no es GRAVE.

### `R1-05` · **SOSTENIDO · MENOR · clase `A`**

El emisor (L217-222) afirma que `read-tree` + `checkout-index` «materializan el árbol del
commit y nada más — **no consultan `.gitattributes`** y no pueden honrar `export-ignore`».
**La primera mitad es falsa. Medido:**

```
$ echo 'docs/owner/ADS-OWNER-RESOLUCIONES.md text eol=crlf' > .gitattributes ; git add -A; git commit
$ git show HEAD:docs/owner/ADS-OWNER-RESOLUCIONES.md | grep -c $'\r'          0
$ grep -c $'\r' <materializado por read-tree+checkout-index>                334
$ sha256 blob          db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
$ sha256 materializado 31d8b08b059377dcbf158764e3ee109740d94f38325c67a296e7bc7e5f52c4a6
```
`checkout-index` **sí** consulta `.gitattributes`. La segunda mitad es cierta y el remedio de
`Z-04` se sostiene; lo que sobra es la generalización. Queda abierta la divergencia estructural
—**el derivador VE el árbol materializado y el digest MIDE el blob**—, que hoy no es explotable
porque el árbol no tiene ningún `.gitattributes`. MENOR, y `R1` declara honestamente que no
consiguió armar un ataque con ella.

### `R1-06` · **SOSTENIDO · MENOR · clase `A`** — LATENTE

Emisor L275: `crudo.count(b"\n") + (0 if crudo.endswith(b"\n") else 1)` → sobre `b""` da **1**.
Derivador L719-722: `n = crudo.count(b"\n"); if crudo and not crudo.endswith(b"\n"): n += 1` →
sobre `b""` da **0**. Dos sedes de la misma derivación que divergen en el fichero vacío.
```
$ git ls-tree -r -l b27a761 | awk '$4==0' | wc -l      0    ← ningún fichero vacío hoy
```
LATENTE. MENOR.

### `R1-07` · **SOSTENIDO · MENOR · clase `A`** — LATENTE

Batería L1897-1903: `_publicado`, `_INMUTABLES` y los tres contrastes contra `HEAD` y la base
salen de `.split()` sobre `git ls-tree -r --name-only`, que separa por **salto de línea**;
`.split()` sin argumento parte por cualquier blanco. Una ruta con un espacio se convierte en
dos entradas falsas. Falla LOUD, luego no es una puerta.
```
$ git ls-tree -r --name-only b27a761 | grep -c ' '     0
```
LATENTE. MENOR.

### `R1-08` · **SOSTENIDO como FRAGILIDAD · MENOR · clase `A`**

El `ALCANCE` de `DD-21` se deriva del discriminante `"sin git" in t` sobre los TÍTULOS
(batería L337). Es derivación sobre una **convención de redacción**, no sobre la propiedad, y
`DD-21` existe porque `G-34` era la novena sin declararlo. **Hoy la medición es exacta** —lo
verifiqué: la batería publica 9 rojas sin `.git` y 29 verdes, y el `ALCANCE` las nombra una a
una—. **No es falsedad presente**: lo sostengo como fragilidad, MENOR.

### `R1-09` · **SOSTENIDO · MEDIO · clase `A`** — LATENTE

`git ls-tree --name-only` CITA Y ESCAPA toda ruta no-ASCII (`core.quotePath` vale `true` por
defecto y el árbol no lo fija). Medido plantando `docs/normativa/SEDE-VIGENTE-е.md` con `е`
cirílica U+0435:
```
$ git ls-tree -r --name-only HEAD | grep normativa
"docs/normativa/SEDE-VIGENTE-\320\265.md"
$ git -c core.quotePath=false ls-tree -r --name-only HEAD | grep normativa
docs/normativa/SEDE-VIGENTE-е.md
$ python3 …/comprobar-…py
└─ AMPLIACIÓN NO CLASIFICADA …: docs/normativa/SEDE-VIGENTE-е.md …;
   fichero del corpus DESAPARECIDO: "docs/normativa/SEDE-VIGENTE-\320\265.md"
37/38
```
**Una sola ruta produce DOS diagnósticos y uno de ellos es FALSO**: declara DESAPARECIDO un
fichero que existe. Y la cadena citada **no empieza por `docs/owner/`** —empieza por `"`—, de
modo que una ruta no-ASCII bajo `docs/owner/` no entraría en `_owner_publicado`, que es
exactamente el bucle de `DD-02`. **Comprobé que hoy no abre puerta**: planté la sede no-ASCII
bajo `docs/owner/` y la batería la caza igual (`37/38`, universo 77). Es LATENTE por
`grep -c '^"'` → 0, y por eso MEDIO y no GRAVE.

### `R2-02` · **SOSTENIDO · GRAVE · clase `A`**

```
$ find docs/evolucion/verificacion -type f \( -name '*.md' -o -name '*.py' \) | sort | wc -l    12
$ sed -n '134,146p' 00-INDICE.md | grep -o 'verificacion/…' | sort -u | wc -l                   11
      el que falta:  verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md
$ grep -n 'CERTIFICACION-5-20260831' 00-INDICE.md      →  93,  y nada más
```
La regla de `00-INDICE.md` L126-132 dice «se enlaza **desde la lista de abajo**», y L145
registra que el manifiesto `4B` «**Faltaba en ESTA lista**: sólo estaba enlazado desde la fila
del gate … TERCERA recurrencia de `S-18`≡`T-14`». **El `-5-` está exactamente en esa situación:
CUARTA recurrencia, viva en la candidata, dentro de la lista que documenta las tres
anteriores.** Y el comando que la sede publica para autocomprobarse **no puede verla**, porque
hace `grep` sobre el fichero entero:
```
$ diff <(find … | sort) <(grep -o 'verificacion/…' 00-INDICE.md | sed … | sort -u)
(VACÍO)   ← el instrumento pasa en verde sobre la violación de la regla que dice guardar
```

### `R2-03` · **SOSTENIDO · GRAVE · clase `A`** — y es lo que decide `C-L.7`

```
$ grep -n '^metodo:\|^last_meaningful_event:\|^based_on:' CHECKPOINT-ADS-NEXT.md
878:  metodo:      … CUARTO GATE DE CERTIFICACIÓN DEVUELTO … TANDA … EN CURSO
1001: based_on:    (su lista de documentos numerados termina en 25-CUARTO-GATE-…)
1101: last_meaningful_event: EL CUARTO GATE DE CERTIFICACIÓN DEVUELVE INSUFICIENTE … sobre dc9be3f
$ sed -n '1001,1081p' … | grep 'docs/evolucion/2[0-9]-'   → 20,21,22,23,24,25 ·  EL 26 NO ESTÁ
$ (cabecera L1-60)                                        → SÍ nombra el QUINTO GATE y el doc 26
```
El bloque va rotulado `freshness: vigente` y `regla_de_reanclaje` («ESTE BLOQUE ES EL ESTADO
REANUDABLE y va SIN rótulo histórico: describe el árbol VIGENTE»), y su **regla 4**, escrita
DENTRO del bloque, dice: «TODO EVENTO NUEVO —un gate devuelto, … una tanda aplicada— REANCLA
`metodo`, `last_meaningful_event` y `based_on` EN EL MISMO COMMIT QUE LO REGISTRA. **Un evento
escrito en la cabecera de este fichero y no aquí es EXACTAMENTE el defecto de `X-04`, y no
cuenta como registrado**».

**Han pasado DOS eventos —el quinto gate y esta tanda— y el bloque nombra el CUARTO.**
La clase `K-01`/`J-10`/`L-01` · `P-05`≡`Q-08`/`R-02` · `S-17`≡`S3-05` · `X-04` reincide por
**quinta vez**, y por primera vez **contra una regla escrita dentro del propio bloque para
impedirla**. `DD-08` cerró la cabecera (instancia); el bloque (clase) sigue abierto.

### `R2-04` · **SOSTENIDO · GRAVE · clase `A`**

```
$ grep -c '"ABIERTA"' <batería de la candidata b27a761>      2
$ grep -c '"ABIERTA"' <batería del árbol del quinto gate 8c9ca9c>   2
$ batería L1479  _ESTADOS_CL = ("CORREGIDAS EN F4c","NO CERRADA","ABIERTA",
                                "REGISTRADAS PARA F5","CONTRATADA PARA F6",
                                "MIXTA POR DESGLOSE","CERTIFICADA POR")
$ batería L1470-1478 declara que fue el CUARTO gate quien obligó a añadirlo
```
La fila `C-L.5` del checkpoint (L2174-2182) se presenta como escrita «**SIN COPIAR SU
RESULTADO, que es lo que `AA-02` castigó** … así **no puede caducar ni ser falsa en el commit
que la escribe**», y a continuación afirma en indicativo que «el vocabulario de estados
primarios del instrumento **no conoce «ABIERTA»** y sigue describiendo la clasificación
anterior», y que el remedio llegará «**en cuanto ese fichero lo incorpore**». **Lo incorporó
hace dos gates.** La aserción es FALSA en el commit que la escribe, que es exactamente lo que
la propia sede declara imposible. Y la fila `C-L.7`, cincuenta líneas más abajo, **remite a la
de `C-L.5` como si el rojo siguiera vivo**: la instancia («NO CERRADA») se cerró y la clase
(«ABIERTA») quedó en pie, en el mismo bloque.

### `R2-05` · **SOSTENIDO · MEDIO · clase `A`**

```
$ grep -cE 'DD-0[579]|DD-1[034]' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md      23   (no 6)
$ grep -oE 'DD-[0-9][0-9]' … | sort -u
DD-05 DD-07 DD-09 DD-10 DD-12 DD-13 DD-14                                        7    (no 6)
```
La reconciliación se declara «hecha **mecánicamente** y no por lectura» y publica un comando
que **cuenta LÍNEAS, no identificadores**, y un criterio —«verificables en el propio documento
11»— que selecciona **siete** ids y no seis. **Ninguna de sus dos mitades es mecánica.** La
CONCLUSIÓN (retirar el cardinal en vez de sustituirlo) sigue en pie y es correcta; lo que no se
sostiene es la comprobabilidad que el parte se atribuye.

### `R2-06` · **SOSTENIDO · GRAVE · clase `A`**

```
$ grep -cniE 'titular|regla de titulares' <batería de la candidata>      2
   L608  «el modo de fallo que la regla de titulares de §0 persigue — y §0 nombra a `G-10`…»
   L640  f"su titular no dice «Son {_letra}»"
$ (el mismo comando sobre el árbol del quinto gate 8c9ca9c)              0
```
El §0 del documento 11 (L154-168) dice «**No tiene GUARDIÁN.** La batería de corrección no la
comprueba, y el cardinal de esta afirmación tampoco se escribe: **se DERIVA** … **mientras ese
comando devuelva 0, esta regla no tiene ni una comprobación mecánica**». **Devuelve 2.** Y no
es sólo el proxy: `G-10` hoy comprueba mecánicamente UN titular (L640), luego la aserción
llana «la batería de corrección no la comprueba» es materialmente inexacta. **Lo rompió esta
misma tanda**, con el remedio de `DD-12`, doce líneas por debajo de la viñeta que `DD-12`
precisa. **La sede se autofalsifica con su propio comando, en el commit que la tocó.**

### `R2-07` · **SOSTENIDO · GRAVE · clase `A`**

```
$ grep -cE '^\| `X[0-9]{2}` \|' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md      47
$ (ids únicos)                                                                   47
$ CHECKPOINT L2344 (campo `falta_para_cerrar_la_capa`, dentro del BLOQUE DE ESTADO
  VIGENTE L849-2385, SIN rótulo histórico):
  «NADA PROBADO: las **46** filas de la tabla adversarial de §2.6.7 —derivadas por conteo,
   no escritas a mano; X62 la añade **esta tanda** por J-03—»
```
**Es EL MISMO cardinal que `DD-13` retiró del documento 11 EN ESTA MISMA TANDA** (11-ARQ L1722:
«esta frase escribía "cuarenta y seis", y `X63` la dejó caducada en el acto») **y que quedó vivo
una sede más allá**. La sede se autodescribe «derivada por conteo, no escrita a mano» mientras
escribe el número a mano. El barrido de `DD-13` no podía verlo: su patrón es `^\*\*.*<cardinal>`
y esto vive dentro de un bloque ```` ```text ````. Y «`X62` la añade esta tanda» está caducado.

### `R2-08` · **SOSTENIDO · MEDIO · clase `A`** — **y NO es el mismo hallazgo que `R2-07`**

```
$ CHECKPOINT L2907-2926, bloque rotulado
  «CIFRAS VIGENTES, DERIVADAS de la tabla de abajo y no copiadas de ningún resumen»
  FILAS ADVERSARIALES  46 filas físicas · 46 ids únicos en §2.6.7      → reales 47 · 47
  «`PN-17` y `PN-18` son las que añade **esta tanda**, por `P-07` y `P-08`»
$ git log --oneline -S'## `PN-17`' -- …/11-ARQUITECTURA-INTEGRADA.md | tail -1
609863e  fix(f4c): propagar O17 a los cuatro macrocircuitos y cerrar la clase A del doc 11
$ idem PN-18 → 609863e   ·   PN-19 → 8e70d94 (tanda de O18)
```
**LOS CUENTO POR SEPARADO Y DIGO POR QUÉ.** `R2-07` y `R2-08` comparten el cardinal caducado
`46`, pero **`R2-08` trae una falsedad ADICIONAL e INDEPENDIENTE**: la atribución de `PN-17` y
`PN-18` a «esta tanda» cuando las añadió la tanda de `O17`, dos tandas antes — y ésa es
**exactamente la clase de `Y-10` del documento 25**, corregida en una sede
(`pregunta_pendiente`) y viva en ésta. Un remedio que arregle `R2-07` no arregla eso. **Son
DOS.**

### `R2-09` · **SOSTENIDO · MEDIO · clase `A`**

```
$ DECISIONES-Y-CONTRADICCIONES.md L447, glosa de `D103`, en un fichero declarado
  «Registro vivo» (L4), en PRESENTE y SIN marca histórica:
  «La batería sigue teniendo **30 comprobaciones**: `G-15` se corrige en su sitio»
$ git show b27a761:…/verificacion/README.md | grep -o 'G-[0-9]\+[a-z]*' | sort -u | wc -l   40
$ la batería publica hoy                                                                   38/38
```
Es `S-16`≡`S3-06` **una sede más allá**: aquel hallazgo retiró «30/30» del CHECKPOINT y lo
sustituyó por el comando; la frase gemela del registro de decisiones sobrevivió tres gates.

### `R2-10` · **SOSTENIDO · MENOR · clase `A`**

El bloque de 11-ARQ L8789-8811 se rotula «EL REPARTO, **LITERAL DE LA SEDE CANÓNICA DEL
OWNER**» y su propio remedio de `DD-05` dice «**Un bloque rotulado LITERAL es la sede, cláusula
a cláusula, y nada más**». Ejecuté el `sed` que el propio bloque publica:
```
$ sed -n '/^· SIS define el contrato/,/^· el ejecutor externo/p' docs/owner/ADS-OWNER-RESOLUCIONES.md
· SIS define el contrato de conformidad
· PLT construye y opera la maquinaria externa
· VER produce el dosier independiente
· SEG gobierna credenciales, bloqueo y fallos de confianza
· el Owner conserva la autoridad de aceptar o rechazar la raíz externa
· el ejecutor externo no puede compartir la identidad de escritura del runtime ADS
```
**El CONTENIDO de las seis cláusulas reproduce la sede exactamente: no hay amplificación.** Los
cinco primeros rótulos del bloque son el SUJETO de su cláusula (`SIS`,`PLT`,`VER`,`SEG`,`EL
OWNER`); **el sexto, «Y UNA PROHIBICIÓN DE IDENTIDAD», es una caracterización añadida** que la
sede no contiene. Es una glosa dentro del bloque que `DD-05` acaba de limpiar de glosas, una
cláusula más allá. MENOR, porque nada queda ampliado ni recortado.

### `R2-11` · **SOSTENIDO · MEDIO · clase `A`** — el defecto VIVO es `00-INDICE.md:93`

```
$ doc 26 §6.4, titulado «RECUENTO, DERIVADO DE LAS FILAS»:  GRAVE 12 · MEDIO 6 · MENOR 4
$ derivado de sus 22 filas:
  grep -oE '^\| \*\*`DD-[0-9]{2}`\*\* \| \*\*[A-ZÁÉÍÓÚ ]+\*\*' … | sort | uniq -c
      12 GRAVE · 4 MEDIO · 1 MEDIO ESTRUCTURAL · 5 MENOR      →  12 · 5 · 5
$ filas DD totales: 22        (el total sí cuadra; el desglose MEDIO/MENOR no)
```
**El documento 26 es INMUTABLE y su defecto interno NO es un defecto vivo.** Lo que sí es vivo
es doble, y es lo que sostengo:
1. **`00-INDICE.md` L93 —sede VIVA— copia el desglose falso** «22 hallazgos: BLOQUEANTE 0 ·
   GRAVE 12 · MEDIO 6 · MENOR 4».
2. **El `CORRIGENDUM` no tiene entrada sobre ello**: `git show b27a761:…/CORRIGENDUM…md |
   grep '^## '` → **16 entradas**, y las §14 y §15 son sobre el MANIFIESTO del quinto gate, no
   sobre su recuento. El corpus tiene tipificada la vía para esto (`F-12`, `L` del doc 19):
   no tocar el inmutable, **reanclar la proyección viva y publicar la entrada**. **No se hizo
   ninguna de las dos.**

### `R2-12` · **SOSTENIDO · MENOR · clase `A`** — contra el SOBRE, no contra la candidata

```
$ git diff --name-status b27a761 ce2cb42
M  docs/evolucion/00-INDICE.md
A  …/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md
A  …/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md
M  kernel/operativo/pruebas/evidencia/fuentes-salida.txt
M  kernel/operativo/pruebas/evidencia/negativos-salida.txt
M  kernel/operativo/pruebas/evidencia/referencias-salida.txt        →  SEIS rutas
$ diff <(universo b27a761) <(universo ce2cb42)                      →  DOS rutas (las dos «A»)
$ el sobre publica: «RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: 3»    (las dos «A» + 00-INDICE)
```
La cifra `3` es **verdadera de los UNIVERSOS**, y reproduce. La glosa que la acompaña —«son
**la superficie exacta en que la candidata y el gate no son el mismo objeto**»— es **falsa de
los OBJETOS**: hay tres rutas más, y son precisamente las que `DD-17` obliga a reejecutar.
No induce a error a un revisor disciplinado, pero el sobre publica como «superficie exacta»
un subconjunto propio de la real. MENOR. **No invalida el gate**: los digest, las huellas y los
bytes del sobre reproducen todos, y los tres bloques embebidos son idénticos.

### NADA CAE, Y LO DIGO EXPRESAMENTE

**He reproducido las VEINTIUNA afirmaciones de hallazgo de los dos dictámenes y NINGUNA CAE.**
No sostengo ninguna por autoridad: cada una lleva arriba el comando que la deriva y su salida,
ejecutados por mí. Dos de ellas (`R1-08`, `R1-05`) las sostengo **rebajadas a fragilidad
declarada** en su alcance, tal como sus propios autores las presentaron, y lo digo en su
párrafo.

_(continúa)_

---

## §3 · TABLA CONSOLIDADA Y DEDUPLICADA

### §3.1 · Las dos deduplicaciones que hago, y por qué

**FUSIONO `R1-02` con `R2-01` → un solo hallazgo, `EE-02`.** Son el MISMO cardinal erróneo del
MISMO fichero: `R1-02` cita el §6 (L222-230) y `R2-01` cita además el §2 (L69-70). **Un solo
remedio los cierra los dos.** Cuentan **UNO**.

**FUSIONO `R1-07` con `R1-09` → un solo hallazgo, `EE-11`.** Los dos son el mismo defecto de
derivación en la misma sede (batería L1897-1903): `.split()` sobre la salida de
`git ls-tree -r --name-only`. `R1` los presentó como dos y los llamó «de la misma familia»;
**yo compruebo que UN SOLO REMEDIO los cierra los dos**, y por eso cuentan UNO:

```
$ git ls-tree -r --name-only HEAD | grep normativa
docs/normativa/con espacio.md
"docs/normativa/uni-\320\265.md"          ← el espacio parte, y el no-ASCII se cita
$ git ls-tree -r --name-only -z HEAD | tr '\0' '\n' | grep normativa
docs/normativa/con espacio.md
docs/normativa/uni-е.md                   ← -z arregla LOS DOS a la vez
```
Se fusionan a la severidad ALTA de las dos (MEDIO), no a la baja.

**NO FUSIONO `R2-07` con `R2-08`, y digo por qué.** Comparten el cardinal caducado `46`, pero
`R2-08` trae una falsedad **adicional e independiente** —«`PN-17` y `PN-18` son las que añade
esta tanda», cuando las añadió `609863e`, la tanda de `O17`—, que es la clase de `Y-10` del
documento 25 corregida en una sede y viva en ésta. **Un remedio que corrija el `46` no corrige
la atribución.** Son **DOS**.

**NO FUSIONO `R2-02` con `R2-11`** aunque las dos vivan en `00-INDICE.md`: una es un enlace
ausente de una lista, la otra un desglose de severidades copiado de un inmutable. Nada en
común salvo el fichero. Son **DOS**.

**21 afirmaciones de hallazgo entregadas → 19 hallazgos sostenidos. NINGUNA CAE.**

### §3.2 · La tabla

| # | id `EE` | origen | sev | clase | sede | reincidencia (doc 25 / 26) |
|---|---|---|---|---|---|---|
| 1 | **`EE-01`** | `R1-01` | **BLOQUEANTE** | **A** | batería L3038 y L3107-3118 · título de `G-29` L3120 · README L244 | **SÍ · `DD-02`** cerrado como INSTANCIA (`docs/owner/`); la CLASE queda abierta. Y es `M-04`, sexto gate. Y la **6.ª condición de `O18`** (`DD-03/04/11/12`) |
| 2 | **`EE-02`** | `R1-02`≡`R2-01` | **GRAVE** | **A** | manifiesto `6B` §2 L69-70 y §6 L222-230 (commit del gate) | **SÍ · `DD-18`/`DD-19`**, y su regla nueva falla en su PRIMER uso. `BB4` predijo la 6.ª reincidencia (doc 26 §6.4) |
| 3 | **`EE-03`** | `R2-02` | **GRAVE** | **A** | `00-INDICE.md` L126-132 (regla) y L134-146 (lista) | **SÍ · `S-18`≡`T-14` → `Y-03`≡`Z-09`**. **CUARTA** recurrencia |
| 4 | **`EE-04`** | `R2-03` | **GRAVE** | **A** | `CHECKPOINT` L851-877 (regla 4), L878 `metodo`, L1001 `based_on`, L1101 `last_meaningful_event` | **SÍ · `K-01`/`J-10`/`L-01` · `P-05`≡`Q-08`/`R-02` · `S-17`≡`S3-05` · `X-04` · `DD-08`**. **QUINTA** recurrencia |
| 5 | **`EE-05`** | `R2-04` | **GRAVE** | **A** | `CHECKPOINT` L2174-2182 (`C-L.5`) y L2240-2245 (`C-L.7`) | **SÍ · `AA-02`**, cerrado para «NO CERRADA» y vivo para «ABIERTA», en el mismo bloque |
| 6 | **`EE-06`** | `R2-06` | **GRAVE** | **A** | `11-ARQ` L154-168 (§0, regla de titulares) | **SÍ · `DD-12`**: el remedio de esta tanda falsifica la derivación de §0 doce líneas más arriba |
| 7 | **`EE-07`** | `R2-07` | **GRAVE** | **A** | `CHECKPOINT` L2344-2345, `falta_para_cerrar_la_capa`, en bloque VIGENTE sin rótulo histórico | **SÍ · `DD-13`**: el cardinal retirado del doc 11 EN ESTA MISMA TANDA, vivo una sede más allá |
| 8 | **`EE-08`** | `R1-03` | **MEDIO** | **A** | manifiesto `6B` L142-145, preámbulo del §5 | **SÍ · entrada §5 del `CORRIGENDUM`** («describe de más su propia evidencia») |
| 9 | **`EE-09`** | `R1-04` | **MEDIO** | **A** | derivador L131-137 (`_leer`) contra su cabecera L52-58 | **SÍ · `T-22`**, misma clase en el fichero de al lado |
| 10 | **`EE-10`** | `R2-05` | **MEDIO** | **A** | `CHECKPOINT` L3535-3556 (reconciliación de «siete») | **SÍ · `J-07`/`DD-13`**, la exigencia de cifra con comando |
| 11 | **`EE-11`** | `R1-07`+`R1-09` | **MEDIO** | **A** | batería L1897-1903 (`.split()` sobre `ls-tree`), usos en L2088 y L3060 | parcial · misma familia que `T-05`/`R-A` (la comprobación nombra y da verde) |
| 12 | **`EE-12`** | `R2-08` | **MEDIO** | **A** | `CHECKPOINT` L2907-2926, bloque «CIFRAS VIGENTES, DERIVADAS» | **SÍ · `Y-10`** (doc 25), corregido en `pregunta_pendiente` y vivo aquí; y `Q-12` |
| 13 | **`EE-13`** | `R2-09` | **MEDIO** | **A** | `DECISIONES-Y-CONTRADICCIONES.md` L447 (glosa de `D103`, «Registro vivo») | **SÍ · `S-16`≡`S3-06`**, una sede más allá |
| 14 | **`EE-14`** | `R2-11` | **MEDIO** | **A** | **VIVO:** `00-INDICE.md` L93 · **y la ausencia de entrada en el `CORRIGENDUM`** (heredado de doc 26 §6.4, INMUTABLE) | **SÍ · clase de `F-12`** (doc 16) y de `L` (doc 19) |
| 15 | **`EE-15`** | `R1-05` | **MENOR** | **A** | emisor L217-222 | parcial · `Z-04`, cuyo remedio se sostiene; lo que sobra es la generalización |
| 16 | **`EE-16`** | `R1-06` | **MENOR** | **A** | emisor L275 contra derivador L719-722 | no · LATENTE (0 ficheros vacíos) |
| 17 | **`EE-17`** | `R1-08` | **MENOR** | **A** | batería L337 (`"sin git" in t`) y README L63-65 | **SÍ como fragilidad · `DD-21`** nació de esta convención |
| 18 | **`EE-18`** | `R2-10` | **MENOR** | **A** | `11-ARQ` L8789-8811, bloque LITERAL, sexta cláusula | **SÍ · `DD-05`**, una cláusula más allá de las que limpió |
| 19 | **`EE-19`** | `R2-12` | **MENOR** | **A** | **EL SOBRE**, obligación 4 | no · pero es la 6.ª condición de `O18` aplicada al propio sobre |

### §3.3 · Recuento, derivado de las filas de arriba

```text
BLOQUEANTE   1     EE-01
GRAVE        6     EE-02 · EE-03 · EE-04 · EE-05 · EE-06 · EE-07
MEDIO        7     EE-08 · EE-09 · EE-10 · EE-11 · EE-12 · EE-13 · EE-14
MENOR        5     EE-15 · EE-16 · EE-17 · EE-18 · EE-19
             ──
            19

POR CLASE
  A · coherencia interna corregible dentro de `F4c`     19
  B · exige una decisión NUEVA del Owner                 0
  C · resistencia a un actor privilegiado, `F6`          0

POR ÁRBOL
  DE LA CANDIDATA `b27a761` (el objeto auditado)   16   EE-01 · EE-03 … EE-14 · EE-17 · EE-18
  DEL APARATO DEL GATE `ce2cb42`                    2   EE-02 · EE-08
  DEL SOBRE                                         1   EE-19
```

**NINGUNO ES DE CLASE `C`**, y lo declaro expresamente: ninguno reescribe `HEAD`, las refs ni
la revisión base; ninguno edita la batería, su README ni el derivador; ninguno miente el
runner; ninguno es uno de los seis actos que `O18` enumera como no protegidos.

**NINGUNO ES DE CLASE `B`.** Examiné los cuatro candidatos que mi material produce, y **los
cuatro caen**:

```text
CANDIDATO B1  «La guarda de admisión no puede completarse desde dentro; ¿acepta el Owner una
              garantía acotada?»                              CAE · `O18` ya lo resolvió:
              `C` va a `F6` y `A` es demostrable hoy. Extender el bucle de `DD-02` del
              `docs/owner/` al corpus gobernado es mecánico, no una decisión nueva
CANDIDATO B2  «¿Muerde `C-L.5` sobre el árbol del GATE o sólo sobre la candidata?»
                                                              CAE · es una cuestión de
              adjudicación, y la resuelvo yo en §4. No exige al Owner
CANDIDATO B3  «`M-04` no es satisfacible desde dentro de `F4`; ¿decide el Owner?»
                                                              CAE · ya decidido por `O18` y
              `O19`. El texto del checkpoint que aún dice «PENDIENTE DEL OWNER» (L288-320)
              vive DENTRO de la región marcada «[ESTADO ANTERIOR · antes del TERCER GATE DE
              CERTIFICACIÓN, documento 24]» — **es REGISTRO HISTÓRICO, no defecto vivo**, y
              lo verifiqué antes de contarlo
CANDIDATO B4  «¿Debe certificarse `C-L.5`?»                   CAE · es un ACTO del
              adjudicador, y es mío
```

**NO FORMULO NINGUNA PREGUNTA AL OWNER.** Es la tercera vez consecutiva.

_(continúa)_

---

## §4 · LAS CUATRO CUESTIONES QUE EL MANIFIESTO ME ENCARGA

### §4.1 · `C-L.5` — **NO EMITO LA PALABRA `CERTIFICADA`, Y DIGO POR QUÉ**

**Primero lo que consta a favor, porque es una medición mía y va antes que la negativa:**

```
OBLIGATORIO − ASIGNADO  sobre el ÁRBOL DE LA CANDIDATA (el objeto que este gate juzga)
    comm -23 <(universo b27a761) <(76 rutas del manifiesto)   →  ∅   ·  0
    comm -13 (la dirección contraria: ninguna fila sobra)     →  ∅   ·  0
ASIGNADO − LEÍDO   sobre los manifiestos de lectura de `R1` y `R2`
    16 filas de reparto · 13 declaradas íntegras por `R1` · 5 por `R2` · unión = 16 de 16
    uniones de rangos verificadas aritméticamente, sin hueco  →      ·  0
```

**`C-L.5` NO SE REABRE POR COBERTURA por nada que yo traiga sobre el objeto auditado, y lo
digo con la misma fuerza con que digo lo demás.** Las dos restas cierran a ∅ y las 76 filas
del manifiesto casan contra el árbol de la candidata sin una discrepancia de ruta, de líneas ni
de SHA-256, con sus tres subsumas derivadas (72592 · 29855 · 42737).

**Y AUN ASÍ NO ESCRIBO `CERTIFICADA`. Tres razones, y la primera basta por sí sola.**

**1 · EL APARATO DE COBERTURA DE ESTE GATE PUBLICA UN CARDINAL FALSO SOBRE LA ARITMÉTICA QUE
SE ME PIDE CERTIFICAR.** El §6 del manifiesto `6B` —el apartado que `DD-19` creó **exactamente
para que la aritmética del árbol del gate dejara de estar mal rotulada**— publica
`OBLIGATORIO menos ASIGNADO 1`, y son **2**. Certificar la cobertura apoyándome en un
manifiesto cuya propia aritmética de cobertura acabo de falsar sería certificar una medición
que he refutado. **`EE-02` es un defecto DE LA COBERTURA, no un defecto cualquiera.**

**2 · LA EXENCIÓN DE PUNTO FIJO NO CUBRE A LA SEGUNDA FUENTE.** `DD-19` justifica el residuo
del árbol del gate porque «un manifiesto no puede contener su propio SHA-256». Eso alcanza al
`6B` y **no al `-6-20260831.md`**, que es un fichero distinto, inmutable, de **278 líneas**, con
SHA-256 `528dd68f…` perfectamente escribible dentro del `6B`, y al que **nada le impedía llevar
fila**. Sobre el árbol del gate hay hoy **una fuente obligatoria de 278 líneas leída por nadie,
y ninguna sede lo dice**. `DD` dejó expresamente abierta (su `D-4`) la cuestión de si la regla
muerde sobre ese árbol: **no la voy a cerrar en la dirección que certifica mientras eso sea
verdad.**

**3 · CERTIFICAR ES UN ACTO, Y UN ACTO NO SE DEDUCE DE UNA MEDICIÓN.** «No se reabre por
cobertura» y «CERTIFICADA» no son la misma proposición, y el corpus castigó esa confusión dos
veces (`Q-06`, `AA-02`). El quinto gate midió las dos restas a ∅ y **no escribió la palabra**;
la tanda no la escribió por él, **y hace bien** —lo dictamino expresamente: el razonamiento de
`CHECKPOINT` L2184-2205 es CORRECTO y no es una evasión, porque publica la medición completa
que lo contradiría si fuera evasión—. Yo tengo la potestad de escribirla y **decido no
escribirla**, por 1 y 2.

```
                    C-L.5  ·  QUEDA ABIERTA
```

**QUÉ LA CERRARÍA, para que esto no sea un veto perpetuo** (es remedio determinado, no
aplicado): un manifiesto cuyo §6 **DERIVE** las dos aritméticas con su comando en vez de
copiarlas, y en el que el manifiesto sustituido o bien lleve fila, o bien quede excluido con
una razón **derivada** y publicada. Con eso, y sin nada más, la cobertura queda certificable.

### §4.2 · `C-L.7` — **NO CERRADA**

Es `EE-04`, y lo mido yo:

```
$ grep -n '^metodo:\|^last_meaningful_event:' CHECKPOINT-ADS-NEXT.md
878   metodo:                 …CUARTO GATE… DEVUELTO … TANDA … EN CURSO
1101  last_meaningful_event:  EL CUARTO GATE … DEVUELVE INSUFICIENTE … sobre dc9be3f
$ (based_on, L1001-1081)   su lista termina en 25-CUARTO-GATE-…    ·  EL DOCUMENTO 26 NO ESTÁ
$ (cabecera, L1-60)        SÍ nombra el QUINTO GATE y el documento 26
```

El bloque está rotulado `freshness: vigente` y su `regla_de_reanclaje` lo declara «ESTE BLOQUE
ES EL ESTADO REANUDABLE y va SIN rótulo histórico: describe el árbol VIGENTE». Su **regla 4**,
escrita dentro del propio bloque para impedir esto, dice: «*Un evento escrito en la cabecera de
este fichero y no aquí es EXACTAMENTE el defecto de `X-04`, y no cuenta como registrado*».
**Han pasado DOS eventos —el quinto gate y esta tanda— y el bloque nombra el CUARTO.**

**`C-L.7` NO ESTÁ CERRADA. El checkpoint NO reancla su estado en cada tanda. Es la QUINTA
recurrencia de la clase, y la primera cometida contra una regla escrita dentro del propio
bloque.** `DD-08` cerró la CABECERA —la instancia—; el BLOQUE —la clase— sigue abierto.

### §4.3 · `M-04` — **NO SUPERADA. FALLIDA, y la falsé yo mismo**

`M-04` es la proposición «**se puede construir un árbol defectuoso que pase la batería en
verde**». **La construí:**

```
commit atacado   cce139c84bbd2f8b5fbeabd0969c28b48017c690   (clon desechable, fuera del
                                                             repositorio auditado)
qué contiene     docs/normativa/ADS-SENTENCIA-DE-CIERRE-F4C.md, que declara `F4c` CERRADA,
                 `F5` AUTORIZADA y `C-L.5` sin efecto
cómo se crea     git add -A && git commit          SIN UN SOLO FLAG
git status       VACÍO
batería          38/38 comprobaciones en verde
universo         76 rutas, INTACTO
EXCLUIDOS        0 por perímetro · 0 menciones en cualquier salida del derivador
digest (receta del sobre)
                 68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b
ANCLADO          68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b
                 BIT A BIT IDÉNTICO
```

Con su **control positivo en rojo** (`37/38 · FALLO G-29` sin commitear). **`M-04` sigue viva,
en clase `A`, en su SEXTO gate consecutivo.** Y lo que la mantiene viva ya no es el perímetro
—que está cerrado y generaliza, y lo verifiqué— sino **la guarda de admisión, que es el remedio
del árbol anterior**.

### §4.4 · `X63` — **NO se presenta como prueba ejecutada ni como certificación presente**

Barrí todas sus apariciones vivas en el árbol de la candidata:

```
$ git grep -n 'X63' b27a761 -- docs kernel
00-INDICE.md:94        «**`X63` es CONTRATO DE PRUEBA DE `F6`, no una prueba ejecutada
                        ni una certificación presente.**»                        CORRECTO
CHECKPOINT:3613        «`X63` NO ES UNA PRUEBA — es CONTRATO DE PRUEBA DE `F6` …
                        NO se ha ejecutado, NO certifica nada …»                 CORRECTO
CHECKPOINT:3580        fila de `DD-13`: «se contrata la fila que faltaba»        CORRECTO
11-ARQ:1694            la fila de la tabla adversarial §2.6.7, que es contrato   CORRECTO
11-ARQ:1722            nota histórica sobre el cardinal caducado                 CORRECTO
11-ARQ:3695            «la que `DD-13` contrata ahora (`X63`) … son contrato
                        de prueba igual que aquéllas»                            CORRECTO
11-ARQ:5497            «esa validación es `X63`, no `X52`» — en subjuntivo
                        («tendría que RECHAZAR las tres»)                        CORRECTO
11-ARQ:5656            «y **`X63`** la comprueba validando las tres celdas…»     ← PRESENTE
11-ARQ:5668            doce líneas más abajo: «es un **contrato de prueba de
                        `F6`** … **y no se ejecuta aquí**»                       DESAMBIGUADO
```

Y el inventario que podría inflarlo lo declara al revés: `CHECKPOINT` L2344 —«**NADA PROBADO** …
están ESCRITOS. **Ninguno ejecutado**»—.

**RESPUESTA: NO. `X63` no se presenta en ninguna sede como prueba ejecutada ni como
certificación presente.** El único verbo en presente (11-ARQ L5656) está en la voz de quien
describe un contrato y queda desambiguado doce líneas más abajo por el propio bloque, además
de por dos sedes que lo niegan expresamente. **Lo consigno como OBSERVACIÓN DE MÉTODO —un
presente de indicativo en la voz del contrato es la forma exacta en que este corpus ha
producido cinco cardinales caducados— y NO como hallazgo.**

_(continúa)_

---

## §5 · REINCIDENCIAS, Y LA FRASE DE `BB4`

### §5.1 · El recuento

De mis **19** hallazgos sostenidos, **15 son reincidencias de clases ya dictaminadas** en los
documentos 25 y 26, y de ellas **10 tienen el remedio literalmente escrito por un gate
anterior**. Sólo cuatro no lo son (`EE-11`, `EE-16`, `EE-17` como fragilidad, `EE-19`).

```text
REINCIDENCIA CON IDENTIFICADOR, una por línea
  EE-01  DD-02                          — cerrado como instancia (`docs/owner/`)
  EE-02  DD-18 · DD-19                  — su regla nueva falla en su PRIMER uso
  EE-03  S-18≡T-14 → Y-03≡Z-09          — CUARTA recurrencia
  EE-04  K-01/J-10/L-01 · P-05≡Q-08/R-02 · S-17≡S3-05 · X-04 · DD-08 — QUINTA
  EE-05  AA-02                          — cerrado para «NO CERRADA», vivo para «ABIERTA»
  EE-06  DD-12                          — el remedio rompió la derivación de al lado
  EE-07  DD-13                          — el cardinal retirado del doc 11 en ESTA tanda
  EE-08  CORRIGENDUM §5                 — «describe de más su propia evidencia»
  EE-09  T-22                           — misma clase, fichero de al lado
  EE-10  J-07 · DD-13                   — cifra sin comando que la derive
  EE-12  Y-10 · Q-12                    — corregido en una sede, vivo en la gemela
  EE-13  S-16≡S3-06                     — una sede más allá
  EE-14  F-12 (doc 16) · L (doc 19)     — recuento no derivado de sus filas
  EE-17  DD-21                          — la convención de redacción como discriminante
  EE-18  DD-05                          — una cláusula más allá de las limpiadas
```

### §5.2 · **¿SIGUE SIENDO CIERTA LA FRASE DE `BB4`? — SÍ, Y LO DICTAMINO CONTRA EL CRITERIO QUE EL PROPIO `DD` DEJÓ ESCRITO**

`BB4`, doc 26 L209-211: «**El sistema cierra INSTANCIAS y no CLASES.** La corrección se aplica
con la forma sintáctica exacta del contraejemplo, y el defecto reaparece una sede más allá».

`DD` la confirmó y —esto es lo que decide— **escribió la condición exacta bajo la cual dejaría
de ser un hallazgo vivo y pasaría a ser deuda registrada** (doc 26 §7.4):

> «*si en el gate 6 el perímetro se deriva de verdad **y las cinco promesas dicen lo que el
> código hace**, entonces «se cierran instancias y no clases» pasa a ser deuda registrada y el
> trabajo sigue — porque para entonces se habrá cerrado, por primera vez, una clase entera en
> vez de su instancia.*»

**Mido las dos mitades de esa condición:**

```text
MITAD 1 · «el perímetro se deriva de verdad»           SE CUMPLE, y lo verifiqué yo.
   `DD-01` está cerrado y GENERALIZA: `.git` anclado a la RAÍZ, poda sobre la RUTA COMPLETA,
   bytecode por CONTENIDO, y todo lo excluido PUBLICADO con su ruta. Lo probé con las cinco
   variantes que `DD` mandó mirar —enlaces simbólicos, Unicode confusable, submódulos,
   permisos, bytecode falsificado— y las cinco caen o se publican. **El octavo árbol está
   cerrado por CLASE. Esto es real, es nuevo, y hay que decirlo primero.**

MITAD 2 · «las cinco promesas dicen lo que el código hace»    NO SE CUMPLE, y lo mido.
   El título de `G-29` (batería L3120) reclama «topología y unicidad de **TODO el corpus
   gobernado**: **sin ampliaciones sin clasificar** … y **sin segundas sedes**», y el README
   L244 lo repite. **Acabo de commitear una segunda sede que declara `F4c` cerrada, y la
   comprobación da 38/38 en verde.** Son afirmaciones FALSAS del instrumento, hoy, y son la
   SEXTA CONDICIÓN DE `O18` —«ninguna promesa de seguridad superior a la realmente
   entregada»— fallando por segundo gate consecutivo.
```

**LA CONDICIÓN QUE `DD` FIJÓ NO SE CUMPLE. La frase de `BB4` SIGUE SIENDO CIERTA, y no pasa a
ser deuda registrada.**

Y el caso que la prueba mejor no es ninguno de los quince de arriba: es **`EE-01`**, porque el
defecto sobrevive **dentro del remedio que decía haberlo curado**. `DD-02` diagnosticó, con
estas palabras, que «*la guarda de admisión de `G-29` … es INERTE sobre cualquier fichero que
ya esté en `HEAD`*» —un diagnóstico de CLASE, sin zona— y ordenó el remedio acotado a
`docs/owner/`. La tanda **lo aplicó exactamente como se le ordenó** —y eso es justo decirlo, y
lo digo—, y el defecto reaparece **una zona más allá**, con la misma frase, las mismas cifras
(`37/38` sin commitear, `38/38` commiteado) y el mismo digest. **En un corpus que se rotula a
sí mismo «la CLASE en vez de la instancia» (`00-INDICE.md` L94).**

**Dictamino además la mitad estructural del diagnóstico de `DD`, porque la reproduzco:** el
corrector recibe una lista de sedes con su línea, y esa lista es exhaustiva **del hallazgo** y
no **de la clase**. Cerrar la lista es verificable y barato; derivar la clase es caro y nadie
lo comprueba. **Mientras el gate entregue enumeraciones y no derivaciones, el sexto gate
producirá un séptimo.** No es una impresión: es lo que acabo de medir en quince de diecinueve.

---

## §6 · REFUTACIONES CONTRA MIS PROPIAS CONCLUSIONES

Intenté **siete**. **Tres cayeron, una cayó a medias, tres no cayeron.** Publico las siete.

### `RF-1` · **CAYÓ** · «`EE-01` es clase `C`: exige commitear en la rama que se somete a revisión, y eso es privilegio del coordinador»

**Cae contra la sede, no contra mi opinión.** `DD-20`, en «El criterio del gate siguiente» de
`CHECKPOINT-ADS-NEXT.md` L3445-3480, que es SU SEDE y la que mi encargo me manda leer antes de
clasificar, dice: «`A` … **Que el fichero esté o no CONFIRMADO es IRRELEVANTE: el objeto que un
gate juzga es un COMMIT, y confirmar es lo que hace el coordinador en su propia rama de
revisión**», y enumera `C` como corromper la REFERENCIA más los seis actos de `O18`. Mi ataque
usa `git add -A && git commit` **sin un solo flag**; no toca `HEAD`, refs, base, batería,
README, derivador ni runner. Y la propia sede cierra el argumento: «*lo confirma el propio
`AA`, que clasificó su árbol COMMITEADO `AA-E4b` como `A`+`B`*». **CAE. `EE-01` es `A`.**

### `RF-2` · **NO CAYÓ** · «`EE-01` no es hallazgo: es `DD-02`, ya dictaminado, y la tanda aplicó EXACTAMENTE el remedio que `DD` ordenó. Castigarla por eso es castigarla por obedecer»

**Es la refutación que más me ha costado rechazar, y su premisa es VERDADERA:** la tanda aplicó
el remedio con la extensión exacta que `DD` le ordenó, y lo hizo bien. **Pero no cae, por dos
razones que son medición y no disciplina.**

1. **El objeto que un gate juzga es el ÁRBOL, no la diligencia de la tanda.** «El criterio del
   gate siguiente» exige que `A` esté **DEMOSTRADA**, y `A` es una propiedad del commit. Sobre
   el commit auditado, `A` no está demostrada: existe hoy un árbol que la batería da por bueno
   y que declara cerrada la fase.
2. **`DD` escribió él mismo la condición de salida, y no se cumple.** No estoy inventando un
   listón: `DD` dijo que bastaría con «*el perímetro derivado de verdad Y las cinco promesas
   diciendo lo que el código hace*». La primera mitad se cumple; la segunda no, y su
   incumplimiento es la **sexta condición de `O18`**, que es del Owner y no mía.

**NO CAE.** Lo que sí cambia en mi informe: **dejo escrito, en la fila de `EE-01` y aquí, que
el defecto está en el ALCANCE del remedio —que `DD` ordenó— y no en su ejecución.**

### `RF-3` · **CAYÓ** · «El gate es INVÁLIDO, como el cuarto»

Es la vía más cómoda para negar y por eso la intenté primero. **Cae en todos sus frentes:**

```
los TRES bloques de sobre (R1, R2, el fichero)   sha256 731c282a…  ·  diff VACÍO  ·  194 líneas
los DOS digest de universo                        reproducen bit a bit
FUENTES / LÍNEAS obligatorias 76·72592 / 78·73164  reproducen
SHA-256 del manifiesto en el commit del gate       41a4ff29…  reproduce
EMISOR y DERIVADOR en los DOS commits              f1d5a3a9… y 77ffb37b…  reproducen
sede canónica del Owner y sus tres resoluciones    db46edd2… · 0cc5b9b5… · ab9d9447… · cb2487fc…
                                                   reproducen, con 85·111·78 líneas
git ls-files -v | grep -v '^H '                    ninguno (ni skip-worktree ni assume-unchanged)
```

La regla de cierre del manifiesto nombra dos disparadores de invalidez —divergencia entre los
sobres de dos revisores, y sede canónica que no coincida— **y ninguno se dispara**. **CAE. EL
GATE ES VÁLIDO**, y es la segunda vez consecutiva. `EE-19` (el sobre publica «superficie
exacta» para un subconjunto) es MENOR y no toca ni un digest.

### `RF-4` · **NO CAYÓ** · «`EE-02` es pedantería: el objeto auditado es la CANDIDATA, y sobre ella la resta es 0»

**No cae, por dos razones.** (a) **No sostengo que la cobertura falle sobre la candidata** —lo
digo expresamente en §4.1, y va a favor del corpus—. Sostengo que el aparato de ESTE gate
publica un cardinal falso **en el único sitio donde declara la aritmética del árbol del gate**,
y que ese sitio existe **porque `DD-19` lo creó para impedir exactamente esa clase de error**.
(b) La consecuencia material no es cero: una fuente obligatoria de **278 líneas** del árbol del
gate, inmutable, **leída por nadie**, y ninguna sede lo dice. **Es GRAVE y no BLOQUEANTE
precisamente porque el objeto auditado es la candidata**, y esa distinción ya está hecha.

### `RF-5` · **CAYÓ A MEDIAS** · «Los doce de `R2` son cosmética documental —cardinales caducados, rótulos, glosas— y un veredicto no puede colgar de eso»

**Cae en su primera mitad y no en la segunda.** Cae porque **mi veredicto no cuelga de ellos**:
`EE-01` basta por sí solo y es una medición mía. No cae como descalificación, porque **tres de
ellos no son cosméticos**: `EE-04`, `EE-05` y `EE-06` son sedes que **se autofalsifican con el
comando que ellas mismas publican, en el commit que las escribió**, que es la clase que `AA-02`
tipificó; y `EE-04` decide `C-L.7`, que el manifiesto me encarga resolver expresamente. **Una
sede que publica su propio comando de falsación y falla ese comando no es cosmética: es la
única forma de mentira que este corpus puede detectar mecánicamente.**

### `RF-6` · **CAYÓ** · «`EE` repite el quinto gate con otros números; un gate que sólo confirma al anterior no aporta»

**Cae contra tres hechos que son míos y nuevos:**
1. **El noveno árbol está en OTRO SITIO que el octavo.** El de `DD` estaba en el PERÍMETRO; el
   mío está en la GUARDA DE ADMISIÓN, es decir, **dentro del remedio del octavo**. Y `DD`
   mandó buscar el noveno en el perímetro (§10.6 punto 1) — **el perímetro aguantó las cinco
   variantes, y hay que decirlo con la misma fuerza.**
2. **`DD-17`, la recurrencia que cinco gates consecutivos no rompieron, ESTÁ ROTA**, y lo
   ejecuté yo en los dos árboles: `13/13 validadores en verde · 0 problemas`, `T147` con
   `1 superadas · 0 fallidas`, y `git status --porcelain` **vacío** tras correr el runner,
   **en los DOS commits**. Primera vez en seis gates.
3. **`DD` dejó abierta la aritmética del árbol del gate (`D-4`) y este gate produjo el primer
   caso que la rompe**: un gate que publica DOS manifiestos. Eso no existía cuando `DD` escribió.

**CAE.**

### `RF-7` · **NO CAYÓ** · «Si niego, y el gate 7 encuentra un décimo árbol, el expediente no termina nunca: hay que certificar y registrar la deuda»

**Es la refutación que más me cuesta rechazar, y no cae, por tres razones.**
1. **El criterio no es mío.** «El criterio del gate siguiente» exige `A` **DEMOSTRADA**, y `A`
   es una medición, no una cuota de intentos fallidos. No tengo potestad para cambiarlo: es la
   sede, y `O18` la sostiene.
2. **`O18` no autoriza canjear `A` por deuda.** Lo que `O18` mueve a `F6` es `C`; `A` la
   mantiene **demostrable hoy**. Certificar con `A` sin demostrar sería precisamente la
   «promesa de seguridad superior a la realmente entregada» que su sexta condición prohíbe.
3. **La salida está escrita y es alcanzable.** `DD` la fijó: derivar la CLASE en vez de
   enumerar la lista, y que las promesas digan lo que el código hace. El remedio de `EE-01` es
   **el alcance de un bucle y dos renglones de README**. No es un regreso infinito: es un
   alcance que lleva seis gates cerrándose una zona por vez, y lo que pido es que se cierre
   por derivación en vez de por enumeración — que es, literalmente, lo que el corpus tiene
   escrito desde `P-08`.

**NO CAE.**

### §6.1 · Qué cambiaron estas siete en mi adjudicación

```text
RF-1   confirmó la clase `A` de `EE-01` contra la sede, y con ella el veredicto
RF-2   NO cambió el hallazgo, pero SÍ su redacción: consta que la tanda obedeció,
       y que el defecto está en el ALCANCE que `DD` ordenó
RF-3   me obligó a rehacer los catorce contrastes del sobre antes de escribir «VÁLIDO».
       El gate es válido, y lo digo primero
RF-4   me obligó a separar «la cobertura falla» (NO lo sostengo) de «el aparato de
       cobertura publica un cardinal falso» (SÍ), y esa separación decide §4.1
RF-5   me obligó a distinguir tres autofalsaciones de nueve caducidades, y a decir
       expresamente que el veredicto NO cuelga de las doce de `R2`
RF-6   me obligó a publicar `DD-17` ROTO con mi propia salida, que es el mejor
       resultado de esta tanda y va en §7
RF-7   no cambió el veredicto, y me obligó a escribir en §9 un remedio ACOTADO
       en vez de una exigencia abierta
```

### §6.2 · Dos OBSERVACIONES DE MÉTODO que valoro POR ENCIMA de varios hallazgos, y lo digo

**1 · NINGÚN OJO HA LEÍDO EL DOCUMENTO 11 ENTERO.** Son 11682 líneas, `R1` cubre L1–L5200 y
`R2` L5201–L11682. **Una contradicción a caballo de L5200 —entre §2.6 y §11.6, o entre §5.2 y
§17— es estructuralmente invisible para los dos, y para mí.** El manifiesto lo declara (L106),
los dos revisores lo declaran contra su propio interés, y yo lo declaro aquí y no en una nota
al pie. **Es un LÍMITE DEL GATE, no un hallazgo, y lo valoro por encima de `EE-16`, `EE-17` y
`EE-19` juntos.** Consecuencia que sí extraigo: **un veredicto de SUFICIENTE habría quedado
debilitado por este límite; uno de INSUFICIENTE no lo está**, porque el hallazgo que decide es
una medición que ejecuté, no una lectura que hice.

**2 · EL PRESENTE DE INDICATIVO EN LA VOZ DEL CONTRATO.** `X63` está correctamente declarado
como contrato de `F6` en tres sedes, y aun así una de ellas escribe «**`X63`** la comprueba».
No es un hallazgo —queda desambiguado doce líneas más abajo— pero **es la forma gramatical
exacta con que este expediente ha producido cinco cardinales caducados y dos promesas
excesivas**. Lo dejo dicho como método: en un corpus que se audita por su propio texto, el
tiempo verbal es parte del contrato.

_(continúa)_

---

## §7 · QUÉ FALLA HOY, EN MIS PALABRAS

### §7.1 · Lo que ya NO falla, y va primero porque es verdad y no es cortesía

Todo esto lo verifiqué yo, no lo acepté de nadie:

```text
· EL GATE ES VÁLIDO. Los tres bloques de sobre son BYTE A BYTE el mismo fichero
  (731c282a…, diff vacío, 194 líneas los tres). El remedio que salvó al quinto gate —el sobre
  emitido UNA vez a un fichero fuera del repositorio— vuelve a funcionar. Segunda vez seguida
· LOS DOS DIGEST DE UNIVERSO REPRODUCEN BIT A BIT, con la receta publicada, sin ejecutar el
  emisor, sobre los DOS commits. Y con ellos las cuatro cardinalidades (76·72592 / 78·73164)
· LA SEDE CANÓNICA DEL OWNER es byte-idéntica en los dos commits y sus tres resoluciones
  reproducen con sus tres recuentos de líneas. `O19` funciona
· EL PERÍMETRO ESTÁ CERRADO POR CLASE. `DD-01` generaliza: `.git` anclado a la RAÍZ, poda
  sobre la RUTA COMPLETA, bytecode por CONTENIDO, y **todo lo excluido se PUBLICA con su
  ruta**. Las cinco variantes que `DD` mandó mirar —enlaces simbólicos, Unicode confusable,
  submódulos, permisos, bytecode falsificado con nombre `.md`— o caen o salen nombradas.
  **El octavo árbol está cerrado, y eso es nuevo**
· `DD-17` ESTÁ ROTO, y es el mejor resultado de esta tanda. Cinco gates consecutivos dejaron
  el árbol que juzgaban en rojo por culpa del aparato del propio gate. Ejecutado por mí en
  los DOS árboles: `13/13 validadores en verde · 0 problemas`, `T147` `1 superadas · 0
  fallidas`, `git status --porcelain` VACÍO tras correr el runner. **Primera vez en seis gates**
· LAS 76 FILAS DEL MANIFIESTO casan contra el árbol de la candidata sin UNA discrepancia de
  ruta, de líneas ni de SHA-256, y sus tres subsumas derivan sin residuo (72592·29855·42737)
· LA FILA DEL PROPIO DERIVADOR —la que el sobre manda mirar PRIMERO— es idéntica en los dos
  árboles: `U-02`→`X-06`→`DD-18` NO reincide
· LAS DOS RESTAS CIERRAN A ∅ SOBRE EL OBJETO AUDITADO. `C-L.5` no se reabre por cobertura
· EL PROCEDIMIENTO `6`→`6B` ES LEGÍTIMO: el emisor falló CERRADO con `rc=2` ante la marca
  `ADJ`, **antes de que existiera ningún revisor**, y el manifiesto defectuoso se sustituyó
  publicando otro en vez de reescribirlo
· NINGUNO de mis diecinueve exige arquitectura nueva. NINGUNO vuelve al Owner. NINGUNO es `C`
```

**Ésta sigue siendo una candidata sólida, y el trabajo debe SEGUIR.**

### §7.2 · Y aun así, qué falla

**FALLA UNA COSA, y es una medición, no una impresión: `A` —COHERENCIA INTERNA— NO ESTÁ
DEMOSTRADA.**

Sobre el árbol que este gate juzga existe hoy un commit ordinario —`git add -A` y
`git commit`, sin un solo flag— que **añade al corpus una segunda sede normativa declarando
`F4c` CERRADA y `F5` AUTORIZADA**, deja `git status --porcelain` **vacío**, pasa la batería en
**38/38**, no entra en el universo obligatorio ni en `EXCLUIDOS_PERIMETRO` ni en
`EXCLUIDOS_IV`, no recibe fila de manifiesto ni revisor, **no aparece en ninguna salida del
aparato**, y produce con la receta del propio sobre un **digest bit a bit idéntico al que este
gate ancla**. Con su control positivo en rojo. **Lo construí yo, dos veces, con dos ficheros
distintos, y las dos veces salió igual.**

Y hay una segunda cosa, y es la que explica la primera:

**LA SEXTA CONDICIÓN DEL OWNER NO SE CUMPLE.** `O18`, en su sede canónica: «*ninguna promesa de
seguridad superior a la realmente entregada*». El título de `G-29` reclama «**topología y
unicidad de TODO el corpus gobernado: sin ampliaciones sin clasificar … y sin segundas
sedes**», y el README L244 lo repite. **Acabo de commitear una segunda sede sin clasificar, y
esa comprobación da verde.** Son afirmaciones falsas del instrumento, hoy, en el árbol
auditado. Es la segunda vez consecutiva que esta condición falla, y `DD` la nombró la primera.

**Y LA CIRCULARIDAD SE HA MOVIDO POR QUINTA VEZ.** No la he cerrado, la he localizado:

```text
gates 21-23   estaba en `HEAD`
gate 24       en el EMISOR                     — la cerró `O18`/`O19`
gate 25       en la ENTREGA (el canal humano)  — la cerró el sobre a fichero. FUNCIONA
gate 26       en el PERÍMETRO                  — la cerró `DD-01`. FUNCIONA
**gate 27**   **ESTÁ EN LA GUARDA DE ADMISIÓN**, que es el remedio del gate anterior:
              la guarda decide si un fichero es una ampliación legítima, y **sólo mira lo
              que aún NO está en `HEAD`**, salvo en una zona. Quien confirma, entra
```

**Los cinco remedios fueron correctos. Ninguno fue suficiente, porque cada uno cerró el punto
donde la circularidad estaba y no la propiedad que la produce: que la definición de QUÉ se
verifica y de QUÉ se admite sean objetos del árbol verificado.** Esa propiedad es lo que `O18`
contrata para `F6` como `C`; **pero su manifestación de hoy es `A`, porque la guarda existe, es
interna, y su alcance está escrito una zona a la vez en vez de derivado.**

---

## §8 · VEREDICTO

**EL GATE ES VÁLIDO.** Lo decido en `RF-3`, medido y no supuesto: los tres bloques de sobre son
byte a byte el mismo fichero, los catorce campos del sobre reproducen, los dos digest de
universo reproducen bit a bit, la sede canónica y sus tres resoluciones reproducen, no hay ni
un fichero en `skip-worktree` ni en `assume-unchanged`, y ninguno de los dos disparadores de
invalidez que la regla de cierre nombra se dispara. **Es la segunda vez consecutiva.** El gate,
por tanto, **produce veredicto**, y emito el mío.

# INSUFICIENTE PARA F5

**`F4c` NO se cierra. Sigue ABIERTA. `F5` NO queda autorizada. `M-04` NO está superada.
`C-L.5` queda ABIERTA. `C-L.7` NO está cerrada. NO he corregido nada.**

### Las razones. **La primera basta por sí sola, y es una medición mía.**

**1 · `A` NO ESTÁ DEMOSTRADA. EL NOVENO ÁRBOL.** `EE-01`, reproducido por mí en dos variantes
sobre un clon desechable, con `git add -A && git commit` sin un solo flag, `38/38` en verde,
universo intacto en 76, silencio en las cinco salidas del aparato, y **digest
`68ee8f1bdc5849891d6d4475f4176da28e1e386b04da4cc363d7ad66193d5c4b`, BIT A BIT el anclado**.
Con su control positivo en rojo. Es clase `A` por la sede que fija la frontera (`DD-20`), y
cuenta.

**2 · LA SEXTA CONDICIÓN DE `O18` NO SE CUMPLE**, por segundo gate consecutivo: el título de
`G-29` y la fila L244 del README prometen más de lo que el código entrega, y lo mido con el
mismo commit de la razón 1. **De las seis condiciones del Owner fallan dos: la primera y la
sexta**, que es exactamente el resultado del gate anterior.

**3 · LA CONDICIÓN DE SALIDA QUE `DD` ESCRIBIÓ NO SE CUMPLE.** `DD` fijó que «se cierran
instancias y no clases» pasaría a ser deuda registrada si el perímetro se derivaba **y** las
promesas decían lo que el código hace. **La primera mitad se cumple; la segunda no.** Y quince
de mis diecinueve son reincidencias, diez con el remedio ya escrito por un gate anterior.

**4 · `C-L.7` VUELVE A ESTAR FALSADA SOBRE EL ÁRBOL AUDITADO**, por quinta vez, y por primera
vez contra una regla escrita dentro del propio bloque para impedirlo.

**5 · TRES SEDES SE AUTOFALSIFICAN CON EL COMANDO QUE ELLAS MISMAS PUBLICAN**, en el commit que
las escribió (`EE-04`, `EE-05`, `EE-06`), y una de ellas fue rota **por el remedio de esta
misma tanda**. En un corpus que se audita por su propio texto, ésa es la única forma de mentira
que puede detectarse mecánicamente, y se detecta.

### Lo que expresamente NO fundamenta este veredicto

```text
· NO falla por `C`. Ninguno de mis diecinueve lo es, y no cuento ningún ataque privilegiado.
  El verificador externo sigue contratado, completo y sin implementar, para `F6`
· NO falla por COBERTURA sobre el objeto auditado. Las dos restas cierran a ∅ y lo digo
  primero. Lo que sostengo es que el APARATO de cobertura publica un cardinal falso (`EE-02`)
· NO falla porque el GATE sea inválido. Lo decido VÁLIDO, contra la vía más cómoda de negar
· NO falla por el SOBRE, ni por el EMISOR, ni por el DERIVADOR como programas: los tres
  reproducen, y el sobre es el remedio que funciona
· NO falla por el PERÍMETRO, que está cerrado por clase y resistió las cinco variantes.
  `DD-01` es un éxito y lo digo con la misma fuerza
· NO falla por DISCIPLINA. «Se cierran instancias y no clases» es método y, por sí solo, sería
  deuda. **Lo que niega es su PRODUCTO, y es una medición**
· NO falla por la tanda. La tanda aplicó los remedios que se le ordenaron, con la extensión
  que se le ordenó, y en `DD-17` hizo lo que cinco gates no hicieron. **El defecto está en el
  ALCANCE de un remedio, no en su ejecución**
· NO resuelvo NADA por mayoría, y no hacía falta: los dos dictámenes no discrepan en ningún
  hecho. Donde parecían discrepar (`R1-02` frente a `R2-01`) medí yo y coinciden: **2**
```

---

## §9 · REMEDIOS DETERMINADOS · QUÉ HAY QUE HACER, NO CÓMO

**No aplico ninguno. No he tocado el repositorio auditado: `git status --porcelain` vacío al
abrir y al cerrar, `HEAD` en `ce2cb42` sin moverse, ninguna referencia tocada, ningún commit.**

| id | remedio DETERMINADO | ¿Owner? |
|---|---|---|
| **`EE-01`** | Que la guarda de admisión de `G-29` se evalúe contra **el CONTENIDO DEL COMMIT para TODO el corpus gobernado**, y no sólo para una zona — es decir, que su alcance se **DERIVE** de lo que el instrumento declara gobernar en vez de enumerarse zona a zona; y que el título de `G-29` y la fila L244 del README digan **lo que el código hace**, en el mismo commit en que se corrija el código | **NO** |
| **`EE-02`** | Que el §6 del manifiesto **DERIVE** las dos aritméticas con su comando en vez de copiarlas, y que la fuente sustituida `…-6-20260831.md` **o lleve fila o quede excluida con una razón derivada y publicada**. La exención de punto fijo se aplica al manifiesto EN CURSO y a ningún otro fichero | **NO** |
| **`EE-03`** | Que el manifiesto `-5-` se enlace **desde la LISTA**, y que el comando que la sede publica para autocomprobarse **acote su `grep` a la lista** en vez de al fichero entero — si no, el instrumento seguirá pasando en verde sobre la violación de la regla que dice guardar | **NO** |
| **`EE-04`** | Que `metodo`, `last_meaningful_event` y `based_on` **reanclen al último evento** —el quinto gate y esta tanda—, y que lo anterior baje a sus campos `_anterior` como la regla 5 del propio bloque ordena. `C-L.7` no se cierra hasta que un gate posterior lo verifique | **NO** |
| **`EE-05`** | Que la fila `C-L.5` **retire la aserción caducada** sobre el vocabulario y publique el resultado del comando en vez de su antecedente hipotético; y que la fila `C-L.7` **deje de remitir a ella** como si el rojo siguiera vivo | **NO** |
| **`EE-06`** | Que la derivación de §0 diga lo que su comando devuelve —que `G-10` **sí** comprueba mecánicamente un titular— o que el comando mida la propiedad que la afirmación necesita. Hoy la sede se falsa a sí misma | **NO** |
| **`EE-07`** · **`EE-12`** | Que los dos cardinales `46` de `CHECKPOINT` **se retiren y se remitan** a la sede que los deriva —nunca se sustituyan por `47`, que es lo que el propio corpus prohíbe—, y que la atribución de `PN-17`/`PN-18` se retire o se derive de Git | **NO** |
| **`EE-08`** | Que el §5 del manifiesto **describa la regla que realmente aplica** —bytes idénticos al árbol que ese gate leyó— en vez de una regla más estricta que dos de sus sesenta filas no pueden satisfacer | **NO** |
| **`EE-09`** | Que el derivador **falle CERRADO también ante una sede ilegible por codificación**, como la batería ya hace, para que su cabecera diga lo que ejecuta y la receta del sobre no pueda entregar una lista vacía en silencio | **NO** |
| **`EE-10`** | Que la reconciliación publique un comando que **cuente identificadores** y un criterio que seleccione el conjunto que nombra, o que **retire la pretensión de mecanicidad**. La conclusión (retirar el cardinal) se conserva | **NO** |
| **`EE-11`** | Que la batería **deje de partir la salida de `git ls-tree` por blancos**: con separación por `NUL` desaparecen a la vez el fallo de las rutas con espacio y el de las rutas no-ASCII citadas, y con ellos el diagnóstico falso de «fichero DESAPARECIDO» y la ceguera del bucle de `DD-02` | **NO** |
| **`EE-13`** | Que la glosa de `D103` **remita a la sede que deriva el censo** en vez de escribir un cardinal en presente dentro de un registro vivo | **NO** |
| **`EE-14`** | Que la proyección VIVA (`00-INDICE.md` L93) publique el desglose **derivado de las filas del documento 26**, y que el error del documento inmutable se acote **con una entrada en el `CORRIGENDUM`** — que es la vía que el propio corpus prescribe y que aquí no se usó. **El documento 26 no se toca** | **NO** |
| **`EE-15`** | Que el emisor **retire la afirmación de que `checkout-index` no consulta `.gitattributes`**, que es falsa y medida, conservando la parte cierta sobre `export-ignore`; y que se declare la divergencia estructural entre lo que el derivador VE (el árbol materializado) y lo que el digest MIDE (el blob) | **NO** |
| **`EE-16`** | Que el recuento de líneas del emisor y el del derivador **deriven de una sola sede**, o que su divergencia en el fichero vacío se cierre | **NO** |
| **`EE-17`** | Que el discriminante del `ALCANCE` derive de **la propiedad** (que la comprobación necesite historia) y no de una convención de redacción del título | **NO** |
| **`EE-18`** | Que el rótulo de la sexta cláusula del bloque LITERAL sea el **sujeto de la cláusula**, como los cinco anteriores, o que la caracterización baje al bloque de lectura del coordinador, que es donde `DD-05` la mandó | **NO** |
| **`EE-19`** | Que el sobre diga «superficie en que difieren los UNIVERSOS» o **publique además las rutas en que difieren los ÁRBOLES**. Una de las dos, pero no «superficie exacta» para un subconjunto propio | **NO** |

### ¿ALGUNO VUELVE AL OWNER? — **NO. NINGUNO.**

Los diecinueve se cierran con material que el corpus ya tiene escrito y **ninguno reinterpreta
`O17`, `O18` ni `O19`**. Examiné los cuatro candidatos a clase `B` en §3.3 y los cuatro caen.
**No formulo ninguna pregunta al Owner. Es la tercera vez consecutiva.**

### Y LO QUE ESTE VEREDICTO **NO** AUTORIZA

```text
· NO autoriza escribir una protección interna nueva. `X`, `AA`, `DD` y el Owner lo prohíben
  expresamente. Lo que `EE-01` pide es de RESTA y de ALCANCE: derivar el alcance de una guarda
  que ya existe, y hacer que dos renglones digan lo que el código hace
· NO autoriza tocar los documentos INMUTABLES. El error del documento 26 se acota en el
  CORRIGENDUM y se reancla la proyección viva; el documento no se edita
· NO autoriza declarar SUPERADO ningún hallazgo por haberlo aplicado. Aplicar no es certificar
· NO autoriza tratar `C` como exigible dentro de `F4c`. Sigue contratada para `F6` y sigue
  siendo condición previa a PesquerApp
· NO autoriza deducir que el trabajo está mal encaminado. Está bien encaminado: el sobre
  funciona, el perímetro se cerró por clase, `DD-17` se rompió, y ninguna decisión vuelve al
  Owner por tercera vez
```

---

```text
git status --porcelain   AL ABRIR   →  VACÍO
git status --porcelain   AL CERRAR  →  VACÍO
HEAD al abrir y al cerrar           →  ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759, idéntico
FICHEROS DEL REPOSITORIO AUDITADO EDITADOS, CREADOS O BORRADOS POR MÍ    ninguno
COMMITS · PUSH · MERGE · RAMAS · REFS EN EL REPOSITORIO AUDITADO         ninguno
LABORATORIO   …/scratchpad/f4c/clon-EE — `git clone` DESECHABLE fuera del repositorio
              auditado, más checkouts aislados (`read-tree`+`checkout-index`) en
              `$(mktemp -d)`. Los commits de ataque viven SÓLO en el clon
INTÉRPRETE    Python 3.12.14 (shim del encargo). Con el 3.10 del sistema caen `arranque`,
              `fuentes` y `workspace` por `tomllib`: es `A14`, limitación aceptada, NO hallazgo
SUBAGENTE `Agent`                                                        NO USADO
NINGÚN HALLAZGO CORREGIDO, y es deliberado: quien corrige no certifica
NADA RESUELTO POR MAYORÍA · NADA SUAVIZADO
```

# INSUFICIENTE PARA F5
# EL GATE ES VÁLIDO

**ADJUDICADOR `EE` · adjudicación cerrada. El veredicto es mío y nadie por encima lo revisa.**
