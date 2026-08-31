# SÉPTIMO GATE DE CERTIFICACIÓN DE F4c — VÁLIDO, INSUFICIENTE, Y `C-L.5` CERTIFICADA

> **Veredicto del adjudicador `FF`: `F4c` ES INSUFICIENTE PARA F5.**
> **`F4c` NO se cierra y sigue ABIERTA. `F5` NO queda autorizada. Ningún hallazgo se ha**
> **corregido en esta pasada.**
>
> **EL GATE ES VÁLIDO, por tercera vez consecutiva.**
>
> **Y `C-L.5` QUEDA CERTIFICADA POR COBERTURA**, por primera vez desde que el CUARTO GATE la
> reabrió. Es un ACTO del adjudicador, con las dos restas derivadas por él y publicadas con su
> comando, y **con su alcance dicho**: certifica COBERTURA, y **no certifica suficiencia, ni
> profundidad, ni ningún hallazgo como superado**.

## 0 · Qué es este documento

Registro **LITERAL** de los tres dictámenes del séptimo gate independiente sobre la candidata
`f8fc037a998316081a7e9b9563398d118982ce60`, publicada en
`review/f4c-alcance-derivado-candidate-20260831`. Los tres se transcriben **enteros y sin
suavizar**, en §A, §B y §C.

Lo escrito antes de §A lo escribe el **coordinador**, que no es ninguno de los tres
participantes y **que no ha juzgado nada**. Los tres dictámenes **no pasaron por su mano**: se
concatenaron desde los ficheros que sus autores escribieron, y este documento publica sus
SHA-256.

```text
DICTAMEN DEL REVISOR `S1`
  1400 lineas   SHA-256  c9be8d19bf15472433372a3191299a9c2cd0ee919c1f5005af4592fba18302c5
DICTAMEN DEL REVISOR `S2`
  1169 lineas   SHA-256  fe8168a0d0f29884195cacec280cda4d3ee4fbbc23a5aff5369b77271a66e468
ADJUDICACIÓN DE `FF`
  1539 lineas   SHA-256  43dcfb8efbf94a373ff47e4f877d0553a8cba4be76611f9e711f41f024129f40
EL SOBRE DE ANCLA, leído por los tres
   196 lineas   SHA-256  dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2
```

## 1 · EL GATE ES VÁLIDO, Y `FF` LO MIDE ANTES DE NADA

Los **dos bloques de sobre embebidos** por los revisores son **byte a byte el fichero**: mismo
SHA-256, `diff` vacío. Reproducen además los dos digest de universo, el SHA-256 del manifiesto
leído del commit del gate, los cuatro del emisor y el derivador en los dos commits, y la sede
canónica del Owner con sus tres resoluciones. **Ninguno de los dos disparadores de invalidez
que la regla de cierre nombra se dispara.**

## 2 · `C-L.5` QUEDA CERTIFICADA, Y ES LA PRIMERA VEZ EN TRES GATES

```text
OBLIGATORIO − ASIGNADO   ∅   por igualdad de conjuntos y en las DOS direcciones, sobre el
                             árbol de la candidata. Sobre el árbol del gate falta sólo el
                             propio manifiesto, que es PUNTO FIJO (`DD-19`)
ASIGNADO − LEÍDO         0   y 0, sobre los manifiestos de lectura de los DOS revisores,
                             con las uniones de rangos verificadas por el adjudicador
```

`FF` declara que **el obstáculo que `EE` nombró está RETIRADO** —el §6 del manifiesto ya no
copia: deriva— y que **no queda ninguna medición pendiente: queda un acto**. Lo hace, y acota
lo que certifica y lo que no.

> **Y lo dice él, no el coordinador:** «*La sede del ESTADO de `C-L.5` es UNA —la clasificación
> vigente del `CHECKPOINT`— y este acto es el que esa sede tiene que recoger. **NO lo escribo
> yo: yo no corrijo el repositorio.***»

## 3 · EL DÉCIMO ÁRBOL, Y ESTA VEZ SON DOS EJES DISTINTOS

`EE-01` derivó **QUÉ CONJUNTO** se examina —todo lo que existe hoy y no existía en la revisión
base, confirmado o no— y con eso cerró las cinco variantes del noveno árbol, que `FF`
reprodujo COMMITEADAS y **siguen en rojo**. Pero quedaron dos ejes que ese remedio no cubre:

```text
EJE 1 · LA CODIFICACIÓN     `EE-11` puso `-z` en tres de las CUATRO lecturas de Git y dejó
                            una sin él. Un fichero con una letra castellana en su ruta llega
                            al commit con **38/38**, digest bit a bit idéntico, y `G-23`
                            publica «6 ficheros … todos enumerados» sobre SIETE

EJE 2 · LA MUTACIÓN         `EE-01` derivó QUÉ CONJUNTO se examina, **no QUÉ PROPIEDAD**. Un
                            fichero que YA EXISTÍA en la revisión base no es una ampliación,
                            y por tanto **modificarlo no lo somete a ninguna condición**:
                            `FF` derivó y midió la clase entera y son **OCHO ficheros** —
                            `.gitignore`, `README.md`, `START_HERE.md`, la directiva del
                            Owner, el prompt de arranque y las TRES evidencias reejecutadas—
                            en los que una sentencia de cierre de `F4c` da **38/38**,
                            `EXIT=0`, `porcelain` vacío y **el digest del sobre bit a bit el
                            anclado**. Y **no crea ningún fichero**, de modo que los cinco
                            controles positivos de la tanda no lo tocan
```

## 4 · LOS CATORCE HALLAZGOS, Y NINGUNA DECISIÓN VUELVE AL OWNER

```text
BLOQUEANTE   2        GRAVE   3        MEDIO   6        MENOR   3        TOTAL  14

POR CLASE
  A · coherencia interna, corregible dentro de `F4c`   14
  B · exige una decisión NUEVA del Owner                0
  C · actor privilegiado, contratado para `F6`          0

POR ÁRBOL
  DE LA CANDIDATA   13        DEL APARATO DEL GATE   1        DEL SOBRE   0

REINCIDENCIAS   13 de 14 llevan identificador de una clase ya dictaminada en los documentos
                25, 26 o 27. **NUEVE viven DENTRO de un remedio de la tanda que este gate
                juzga.**
```

**Ninguna fusión, y ningún hallazgo cae**: `FF` reprodujo los catorce de cero, en veintiséis
clones desechables. **Es la CUARTA vez consecutiva que ninguna decisión vuelve al Owner.**

## 5 · LA CONDICIÓN DE SALIDA QUE `EE` DEJÓ ESCRITA — NO SE CUMPLE

`EE` fijó que «se cierran instancias y no clases» pasaría a **DEUDA REGISTRADA** cuando el
perímetro se derivara **y** las promesas dijeran lo que el código hace.

```text
MITAD 1 · el perímetro DERIVADO          SE CUMPLE. `DD-01` y `EE-01` resisten
MITAD 2 · las promesas                   NO SE CUMPLE, en SEIS sedes — y CUATRO de ellas
                                         las escribió o las ENSANCHÓ esta misma tanda
```

**No pasa a deuda.**

## 6 · LO QUE CONSTA A FAVOR, PORQUE ES VERDAD

```text
· **`C-L.5` CERTIFICADA**, por primera vez desde el cuarto gate, con su alcance dicho
· los CINCO controles positivos de la tanda **reproducen COMMITEADOS y son contingentes**:
  el adjudicador los volvió verdes añadiendo su enlace. **La tanda dice la verdad en ellos**
· las dos aritméticas del manifiesto **DERIVAN**, y las fuentes sin fila van enumeradas con
  su razón: `EE-02` está aplicado
· el agotamiento de las 67 filas cumple la regla que el §5 escribe: `EE-08` cerrado
· `EE-09`, `EE-15`, `EE-19` cerrados; `EE-17` deriva bien el ALCANCE —29/38 sin `.git`,
  los nueve exactos—
· el perímetro de `DD-01` resiste symlinks, ficheros vacíos, ordinales Unicode y
  `.gitattributes`
· la reincidencia `U-02`→`X-06`→`DD-18` **NO se repite**
· `X63` NO se presenta como prueba ejecutada ni como certificación presente en ninguna sede
· CERO amplificación de la sede canónica del Owner
· ninguno de los catorce es de clase `C`, ninguno exige arquitectura nueva y ninguno vuelve
  al Owner
```

## 7 · QUÉ FALLA HOY, Y LO QUE ESTE DOCUMENTO NO HACE

Falla que **`A` —coherencia interna— sigue sin estar demostrada**: hay hoy commits ordinarios,
sin un solo flag, que meten una sentencia de cierre de `F4c` en el corpus con la batería en
verde y el digest del sobre idéntico, y salen por donde el remedio de la última tanda no llegó
— por la codificación, y por la mutación de lo que ya existía.

**ESTE DOCUMENTO NO CORRIGE NADA.** El gate se registra, se valida y se publica sin tocar
ninguno de sus hallazgos, que es lo que la disciplina de este expediente exige. **Y `C-L.5`
sigue figurando ABIERTA en la clasificación vigente del `CHECKPOINT`**: recoger ahí el acto de
`FF` es trabajo de la tanda siguiente, y **la tanda siguiente no está autorizada en este
encargo**. Queda dicho aquí en vez de hacerse a medias.

---

## §A · DICTAMEN DEL REVISOR `S1` — TRANSCRIPCIÓN LITERAL

# INFORME `S1` — REVISOR INDEPENDIENTE · SÉPTIMO GATE DE CERTIFICACIÓN DE F4c

Revisor: `S1`. Dominio: protocolo, transacciones, recuperación, fuentes de verdad, Git, identidad, pruebas y DERIVADORES.
Repositorio auditado: `/home/jose/ads-kernel` — **no se ha modificado ni un byte**. Todo ataque se ejecutó sobre un clon en
`/tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/f4c/s1work/clon` (y clones desechables derivados de él).

Fecha del informe: 2026-08-31.

---

## §0 · EL SOBRE Y SUS SEIS OBLIGACIONES

### §0.1 · El sobre, embebido ENTERO y byte a byte

Ruta del sobre (canal EXTERNO al repositorio auditado):
`/tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/f4c/SOBRE-7.txt`

```
SOBRE DE ANCLA · emitido por el coordinador ANTES de crear a ningún revisor
==============================================================================
  REPOSITORIO             git@github.com:JoseLopezGonzalez/ads-kernel.git
  ARBOL DE TRABAJO        `git status --porcelain` VACÍO al emitir, y eso es todo lo
                          que prueba: no había modificaciones VISIBLES para `git
                          status`. Ver la obligación 5 y los SHA-256 del emisor
  TODO LO DE ABAJO SE LEE DE COMMITS con `git show <commit>:<ruta>`. Ni un byte
  del directorio de trabajo de quien emite
------------------------------------------------------------------------------
  REF REMOTA CANDIDATA    refs/heads/review/f4c-alcance-derivado-candidate-20260831
  COMMIT CANDIDATO        f8fc037a998316081a7e9b9563398d118982ce60
  ARBOL CANDIDATO         fe0aa25d7c67a2b8269e60be5e1ba91fc3005e35
  REF REMOTA DEL GATE     refs/heads/gate/f4c-certificacion-7-20260831
  COMMIT DEL GATE         08f6da6e655d19eb9078fbd7284594162e727d3f
  ARBOL DEL GATE          137783c97f83a545939558caec626258f1b67964
  RUTA DEL MANIFIESTO     docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md
  SHA-256 DEL MANIFIESTO  f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff   (en el commit del gate)
  ASIGNACIONES            15   DERIVADAS de las 12 filas de reparto del manifiesto,
                          no recibidas por parámetro
------------------------------------------------------------------------------
LOS DOS ARBOLES, CADA UNO DERIVADO DE SU PROPIO COMMIT CON SU PROPIO DERIVADOR.
El derivador es FILA DE SU PROPIO UNIVERSO y el commit del gate lo toca: por eso el
sobre publica LOS DOS y no mezcla ni un campo. El gate anterior yuxtapuso el árbol
de la candidata con las cifras del árbol del gate, y eran insatisfacibles.

                          CANDIDATA                                                         GATE
  COMMIT                  f8fc037a998316081a7e9b9563398d118982ce60                          08f6da6e655d19eb9078fbd7284594162e727d3f
  SHA-256 DEL DERIVADOR   7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad  7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad
  SHA-256 DEL EMISOR      4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996  4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996
  FUENTES OBLIGATORIAS    79                                                                80
  LINEAS OBLIGATORIAS     77679                                                             77941
  DIGEST DEL UNIVERSO     8c75317fb63e8c645da251968cc6c31a3f91a793a2579f9c14b87c723b67a5f0  1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b


  SHA-256 DEL EMISOR QUE HA CORRIDO ESTE SOBRE: 4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996
  COINCIDE con el del commit del gate. El revisor puede rehacer este contraste:
    git show 08f6da6e655d19eb9078fbd7284594162e727d3f:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum

  RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: 2
    docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md  AUSENTE → f3d7d0bf6d10
    docs/evolucion/00-INDICE.md  89b74fcc16f4 → 7523cc2540f7

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
  git show f8fc037a998316081a7e9b9563398d118982ce60:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O17`/)} p' | sha256sum

  ── `O18` → ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
  git show f8fc037a998316081a7e9b9563398d118982ce60:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O18`/)} p' | sha256sum

  ── `O19` → cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8
  git show f8fc037a998316081a7e9b9563398d118982ce60:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O19`/)} p' | sha256sum

  ── LA SEDE ENTERA → db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
  git show f8fc037a998316081a7e9b9563398d118982ce60:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
==============================================================================
  EMITIDO                 2026-08-31 18:32:41 +0200
  EMISOR                  Jose Lopez Gonzalez (jose@congeladosbrisamar.es), coordinador nombrado del septimo gate
  DECISION QUE LO EXIGE   O18 · alternativa (b) · propagada por D108
  ENTREGA                 este sobre se entrega a cada revisor DENTRO de su encargo
                          y ANTES de que empiece a leer. NO se obtiene leyendo el
                          repositorio que se audita
==============================================================================
COMO SE RECALCULA CADA DIGEST, para que el revisor no tenga que fiarse. Reproduce el
digest BYTE A BYTE; si no lo reproduce, el sobre o el árbol están mal, y en ese orden:

  ── ARBOL CANDIDATO → 8c75317fb63e8c645da251968cc6c31a3f91a793a2579f9c14b87c723b67a5f0
  C=f8fc037a998316081a7e9b9563398d118982ce60
  d=$(mktemp -d)
  GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
  rm -rf "$d"

  ── ARBOL DEL GATE  → 1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b
  C=08f6da6e655d19eb9078fbd7284594162e727d3f
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
  4 LAS RUTAS EN QUE LOS DOS UNIVERSOS OBLIGATORIOS DIFIEREN, listadas arriba, son
    la superficie en que difieren los UNIVERSOS, y NO la superficie en que difieren
    los ARBOLES: los dos commits pueden diferir ademas en ficheros que el universo
    obligatorio no contiene, y esta lista NO los nombra. La otra la da
      git diff --name-only <commit-candidato> <commit-del-gate>
    Todo lo que el manifiesto afirme sobre ellas tiene que decir DE QUE ARBOL habla.
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

Huella del propio sobre, para que quien lea este informe pueda comprobar que lo transcribí sin tocarlo:

```console
$ sha256sum /tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/f4c/SOBRE-7.txt
dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2  /tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/f4c/SOBRE-7.txt
$ wc -lc /tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/f4c/SOBRE-7.txt
  196 14734 /tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/f4c/SOBRE-7.txt
```

### §0.2 · Las SEIS OBLIGACIONES, ejecutadas

Entorno declarado y usado en todo el informe:

```console
$ export PYTHONPATH=<scratchpad>/py312-libs
$ export PATH=<scratchpad>/bin:$PATH
$ python3 -V
Python 3.12.14
$ which python3
<scratchpad>/bin/python3
```

Árbol de ataque (NUNCA el repositorio auditado):

```console
$ git clone -q /home/jose/ads-kernel <scratchpad>/f4c/s1work/clon
$ cd <scratchpad>/f4c/s1work/clon && git cat-file -t f8fc037a998316081a7e9b9563398d118982ce60
commit
$ git cat-file -t 08f6da6e655d19eb9078fbd7284594162e727d3f
commit
```

Estado del repositorio auditado en el instante en que empecé (leído, no escrito):

```console
$ git rev-parse HEAD && git status --porcelain | head -20
08f6da6e655d19eb9078fbd7284594162e727d3f
(salida vacía: ninguna línea de porcelain)
```

**Dato de contexto, no hallazgo todavía:** el `HEAD` del repositorio auditado ES el commit del gate,
y la rama local que lo lleva es `refs/heads/fix/f4c-perimetro-por-naturaleza-20260831`. La rama
`refs/heads/gate/f4c-certificacion-7-20260831` **no existe localmente**; existe
`refs/remotes/origin/gate/f4c-certificacion-7-20260831` en el mismo commit. El sobre habla de
«REF REMOTA», así que esto es coherente.

```console
$ cd /home/jose/ads-kernel && git for-each-ref --format='%(refname) %(objectname)' | grep -Ei 'certificacion-7|alcance-derivado'
refs/remotes/origin/gate/f4c-certificacion-7-20260831 08f6da6e655d19eb9078fbd7284594162e727d3f
refs/remotes/origin/review/f4c-alcance-derivado-candidate-20260831 f8fc037a998316081a7e9b9563398d118982ce60
```

Parentesco y árboles, contrastados contra los campos del sobre:

```console
$ git log --format='%H %P %s' -3 08f6da6e655d19eb9078fbd7284594162e727d3f
08f6da6e655d19eb9078fbd7284594162e727d3f f8fc037a998316081a7e9b9563398d118982ce60 docs(gate): manifiesto previo del septimo gate, con las dos aritmeticas DERIVADAS
f8fc037a998316081a7e9b9563398d118982ce60 98cdb7a1fcbe808d12208fc3a5ba4cdf7f31fb3c fix(f4c): derivar el ALCANCE de la guarda, y los 19 del sexto gate
98cdb7a1fcbe808d12208fc3a5ba4cdf7f31fb3c ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759 docs(gate): sexto gate de certificacion de F4c, VALIDO e INSUFICIENTE

$ git rev-parse f8fc037a998316081a7e9b9563398d118982ce60^{tree} 08f6da6e655d19eb9078fbd7284594162e727d3f^{tree}
fe0aa25d7c67a2b8269e60be5e1ba91fc3005e35
137783c97f83a545939558caec626258f1b67964
```

| campo del sobre | valor publicado | valor recalculado | ¿reproduce? |
|---|---|---|---|
| ÁRBOL CANDIDATO | `fe0aa25d7c67a2b8269e60be5e1ba91fc3005e35` | `fe0aa25d7c67a2b8269e60be5e1ba91fc3005e35` | SÍ |
| ÁRBOL DEL GATE | `137783c97f83a545939558caec626258f1b67964` | `137783c97f83a545939558caec626258f1b67964` | SÍ |

---

#### OBLIGACIÓN 1 — recalcular LOS DOS DIGEST DE UNIVERSO con la receta publicada

Ejecutado literalmente con la receta del sobre, sobre el clon:

```console
$ for C in f8fc037a998316081a7e9b9563398d118982ce60 08f6da6e655d19eb9078fbd7284594162e727d3f; do
    d=$(mktemp -d)
    GIT_INDEX_FILE="$d/idx" git read-tree "$C"
    GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
    python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
      while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
      awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
    rm -rf "$d"
  done
f8fc037a998316081a7e9b9563398d118982ce60 DIGEST= 8c75317fb63e8c645da251968cc6c31a3f91a793a2579f9c14b87c723b67a5f0
  RUTAS= 79
  LINEAS= 77679
08f6da6e655d19eb9078fbd7284594162e727d3f DIGEST= 1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b
  RUTAS= 80
  LINEAS= 77941
```

| magnitud | CANDIDATA publicada | CANDIDATA recalculada | GATE publicada | GATE recalculada |
|---|---|---|---|---|
| DIGEST DEL UNIVERSO | `8c75317f…3b67a5f0` | `8c75317fb63e8c645da251968cc6c31a3f91a793a2579f9c14b87c723b67a5f0` | `1674c65d…6b9ce8fb3b` | `1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b` |
| FUENTES OBLIGATORIAS | 79 | 79 | 80 | 80 |
| LÍNEAS OBLIGATORIAS | 77679 | 77679 | 77941 | 77941 |

**LOS DOS DIGEST REPRODUCEN BYTE A BYTE. La obligación 1 no aborta el gate.** Sigo leyendo.

---

#### OBLIGACIÓN 2 — leer el manifiesto EN EL COMMIT DEL GATE y comparar su SHA-256

```console
$ git show 08f6da6e655d19eb9078fbd7284594162e727d3f:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md | sha256sum
f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff  -
$ git show 08f6da6e655d19eb9078fbd7284594162e727d3f:docs/…/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md | wc -l
260
$ git show f8fc037a998316081a7e9b9563398d118982ce60:docs/…/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md
fatal: path '…' exists on disk, but not in 'f8fc037a998316081a7e9b9563398d118982ce60'
```

Publicado: `f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff`. **REPRODUCE.**
El manifiesto NO existe en la candidata, que es exactamente lo que el sobre dice en «RUTAS EN QUE LOS
DOS UNIVERSOS DIFIEREN» (`AUSENTE → f3d7d0bf6d10`). Toda mi lectura del manifiesto es del commit del gate.

---

#### OBLIGACIÓN 5 — recalcular el SHA del EMISOR y del DERIVADOR en los DOS commits

```console
$ for c in f8fc037a998316081a7e9b9563398d118982ce60 08f6da6e655d19eb9078fbd7284594162e727d3f; do
    git show $c:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum
    git show $c:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum
  done
f8fc037… emisor    4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996
f8fc037… derivador 7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad
08f6da6… emisor    4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996
08f6da6… derivador 7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad
```

Los cuatro coinciden con los cuatro campos del sobre. **REPRODUCEN.** Y el sobre dice explícitamente
lo que esto NO prueba (que el binario que corrió fuese ése, dado `git update-index --skip-worktree`):
tomo esa declaración como correcta y no la convierto en hallazgo — es `Z-11` ya registrado.

---

#### OBLIGACIÓN 6 — recalcular los digest de la SEDE CANÓNICA DEL OWNER

```console
$ for c in f8fc037a998316081a7e9b9563398d118982ce60 08f6da6e655d19eb9078fbd7284594162e727d3f; do
    git show $c:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
    for o in O17 O18 O19; do
      git show $c:docs/owner/ADS-OWNER-RESOLUCIONES.md | awk -v k="^# \`$o\`" '/^# /{p=($0~k)} p' | sha256sum
      … | wc -l
    done
  done
```

| objeto | publicado | CANDIDATA recalculado | líneas | GATE recalculado | líneas |
|---|---|---|---|---|---|
| SEDE ENTERA | `db46edd2…aa018d4a` | `db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a` | — | idéntico | — |
| `O17` | `0cc5b9b5…ec4e6125` | `0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125` | 85 | idéntico | 85 |
| `O18` | `ab9d9447…16ed0353` | `ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353` | 111 | idéntico | 111 |
| `O19` | `cb2487fc…cce69ea8` | `cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8` | 78 | idéntico | 78 |

**Los cuatro digest reproducen en LOS DOS commits, y los recuentos de líneas (85 · 111 · 78) coinciden
con los que el sobre declara DERIVADOS.** «LOS DOS COMMITS PUBLICAN LA MISMA SEDE, byte a byte»: cierto.

---

#### OBLIGACIÓN 4 — usar las RUTAS DIVERGENTES, y no confundirlas con el diff de árboles

El sobre publica 2 rutas divergentes **DE UNIVERSO** y advierte que el diff de ÁRBOLES es otro.
Lo comprobé, y la advertencia es literalmente cierta:

```console
$ git diff --name-only f8fc037a998316081a7e9b9563398d118982ce60 08f6da6e655d19eb9078fbd7284594162e727d3f
docs/evolucion/00-INDICE.md
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md
kernel/operativo/pruebas/evidencia/fuentes-salida.txt
kernel/operativo/pruebas/evidencia/negativos-salida.txt
kernel/operativo/pruebas/evidencia/referencias-salida.txt
```

5 rutas difieren entre árboles; sólo 2 difieren entre universos obligatorios. Las 3 restantes
(`kernel/operativo/pruebas/evidencia/*-salida.txt`) están FUERA del universo obligatorio, y el sobre
lo anticipa en su obligación 4 en vez de esconderlo. **Esto es un acierto del sobre 7 y lo registro
como tal**, no como hallazgo. Uso estas rutas en §2 y §3.

---

#### OBLIGACIÓN 3 — cada fila contra SU árbol; la del propio derivador primero

Se ejecuta en §2.1. Adelanto el resultado del contraste de la fila del derivador, que es la que
`U-02` y `X-06` falsearon dos gates seguidos: **en el manifiesto 7 esa fila declara `798` líneas y
`7d72b061…fca7a9ad`, y los DOS árboles dan `798` y `7d72b061…fca7a9ad`** (comando en §2.1). No reincide.

---

### §0.3 · VEREDICTO DEL PASO 0

**Las seis obligaciones se cumplen: los 2 digest de universo, el SHA del manifiesto, los 4 SHA de
emisor/derivador, los 4 digest de la sede del Owner y las 2 rutas divergentes REPRODUCEN todos.
El gate NO es inválido por el sobre.** Procedo a leer y a atacar.

---

## §1 · MANIFIESTO DE LECTURA

Todas las huellas se recalcularon **sobre el COMMIT**, no sobre el árbol de trabajo, con

```console
$ git show <commit>:<ruta> | sha256sum      # y | wc -l para las líneas
```

Salvo indicación en contra, el árbol de referencia de mi lote es el **COMMIT CANDIDATO**
`f8fc037a998316081a7e9b9563398d118982ce60` (el objeto que este gate juzga, §2 del manifiesto 7);
en las nueve fuentes de mi lote las huellas coinciden ADEMÁS en el commit del gate, y lo hago constar.

| # | ruta | líneas | SHA-256 recalculado (candidata) | ¿= lote? | ¿= gate? | rangos leídos | unión | LEÍDO ÍNTEGRO |
|---|---|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11708 | `82aca794e824a6ddca2aefc3808908d08ddd1871d4c4f1750d5d232f7ee33b69` | SÍ | SÍ | L1–L5200 (mi alcance) | L1–L5200 | SÍ, EN MI ALCANCE (L5201–L11708 son de `S2`) |
| 2 | `docs/evolucion/27-SEXTO-GATE-DE-CERTIFICACION-F4C.md` | 3946 | `d81b56366e5062ffe0abcd55ba2ef52ddbc3fadf073ea5a280e6cfc15b87ef26` | SÍ | SÍ | L1–L3946 (el ÚLTIMO que abrí) | L1–L3946 | SÍ |
| 3 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 652 | `7876a2bb81b38c764d1bec924e972fb15df30d78058ef299c8adeff087a14255` | SÍ | SÍ | L1–L652 | L1–L652 | SÍ |
| 4 | `docs/evolucion/verificacion/README.md` | 386 | `6c5064a31261cc0672698833a62e9cdf40d85d42a809b08d15fe1b86d0a92065` | SÍ | SÍ | L1–L200 · L200–L386 | L1–L386 | SÍ |
| 5 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 3957 | `22c454e7b090ff4e1962a36eea6c304e874c50a98a9f2c501c02f1644907f664` | SÍ | SÍ | L1–L3957 | L1–L3957 | SÍ |
| 6 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 798 | `7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad` | SÍ | SÍ | L1–L400 · L400–L798 | L1–L798 | SÍ |
| 7 | `docs/evolucion/verificacion/emitir-sobre-de-ancla.py` | 725 | `4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996` | SÍ | SÍ | L1–L240 · L240–L500 · L500–L725 | L1–L725 | SÍ |
| 8 | `.../manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md` | 278 | `528dd68fc81134c16f874ab5803996ec50ee838241fd95470a9e07dd66770b2c` | SÍ | SÍ | L1–L278 | L1–L278 | SÍ |
| 9 | `.../manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md` | 292 | `41a4ff29d11c1edf26e6370ea7bcf8cf1ee24d75895336d991b6c12fa4251924` | SÍ | SÍ | L1–L292 | L1–L292 | SÍ |

**FUERA DE LOTE, abiertas y DECLARADAS** (el encargo me autoriza a abrir el `CHECKPOINT` para
verificar; las demás las abrí para contrastar, y digo qué leí de cada una y para qué):

| ruta | árbol | SHA-256 recalculado | qué leí | para qué |
|---|---|---|---|---|
| `.../manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md` | **GATE** | `f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff` | L1–L260 ÍNTEGRO | es el manifiesto que juzgo (obligación 2 y §2.1, §2.5) |
| `docs/owner/ADS-OWNER-RESOLUCIONES.md` | los dos | `db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a` | los tres bloques `O17`·`O18`·`O19` por digest, no por lectura íntegra | obligación 6 |
| `docs/evolucion/00-INDICE.md` | los dos | cand `89b74fcc…`, gate `7523cc2540f7…` | sólo los ENLACES, por `grep`/derivación | discriminante de `G-29` (§3) |
| `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | gate | (lote de `S2`) | sólo el «PARTE DE LA TANDA POSTERIOR AL SEXTO GATE» | verificar `EE-01`..`EE-19`, como el encargo autoriza |
| `docs/rediseno/CHECKPOINT-OPERATIVO.md` | gate | (lote de nadie: fuente AGOTADA, fila 28) | sólo el bloque «EXCEPCIÓN EXACTA DEL KERNEL» | contrastar `G-23` (§3, ataque J) |

### §1.4 · LA RESTA `ASIGNADO − LEÍDO`, contra mi propio interés

```text
ASIGNADO A `S1` (manifiesto 7, §4, columna `revisor`, filas con S1)
  fila 2   11-ARQUITECTURA-INTEGRADA.md        L1-L5200        5200 líneas
  fila 3   27-SEXTO-GATE-DE-CERTIFICACION-F4C  ÍNTEGRO         3946
  fila 5   CORRIGENDUM-DICTAMENES-INMUTABLES   ÍNTEGRO          652
  fila 6   verificacion/README.md              ÍNTEGRO          386
  fila 7   comprobar-correccion-gate-de-cierre ÍNTEGRO         3957
  fila 8   derivar-universo-obligatorio.py     ÍNTEGRO          798
  fila 9   emitir-sobre-de-ancla.py            ÍNTEGRO          725
  fila 10  manifiesto 6                        ÍNTEGRO          278
  fila 11  manifiesto 6B                       ÍNTEGRO          292
                                               TOTAL ASIGNADO  16234 líneas

LEÍDO                                          TOTAL LEÍDO     16234 líneas
ASIGNADO − LEÍDO                               0 líneas · 0 fuentes
```

**Declaro contra mi propio interés:** la resta es CERO en líneas, y digo exactamente qué
significa mi lectura del documento 11. Leí **L1–L5200 línea a línea**; NO leí L5201–L11708,
que no es mi alcance y es de `S2`. Por tanto **toda afirmación mía sobre el documento 11 se
limita a L1–L5200**, y donde cito `C-L.5` o `§11.4` lo hago por localización explícita dentro
de ese rango o declarándolo derivado del código que lo lee. No he leído el `CHECKPOINT`
íntegro ni `DECISIONES-Y-CONTRADICCIONES.md` ni `00-INDICE.md` íntegros: no son míos, y lo que
uso de ellos va acotado arriba y en el hallazgo que lo cite.

---
## §2 · HALLAZGOS

Clases, las del propio gate: **A** = defecto de coherencia interna del corpus o del instrumento,
cerrable dentro de `F4c` sin decisión del Owner · **B** = exige una decisión NUEVA del Owner ·
**C** = actor privilegiado, **NO exigible en `F4c`** por `O18`. **Ninguno de los míos es `B` ni `C`:**
todos mis ataques usan `git add -A && git commit` **sin un solo flag**, no reescriben `HEAD`, refs
ni la revisión base, no editan la batería, su README ni el derivador, y no mienten al runner.

### §2.1 · La OBLIGACIÓN 3 primero: la fila del propio derivador, y las 79 filas

```console
$ M=docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md
$ git show 08f6da6…:$M | grep -n 'derivar-universo-obligatorio'
| 8 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 798 |
    `7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad` | v | **S1** | S1 |
$ for c in f8fc037 08f6da6; do git show $c:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum; \
    git show $c:docs/evolucion/verificacion/derivar-universo-obligatorio.py | wc -l; done
7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad  -
798
7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad  -
798
```

**LA CLASE `U-02` → `X-06` → `DD-18` NO REINCIDE.** La fila 8 casa contra los DOS árboles.

Y las 79 filas (§4 + §5), contrastadas contra el árbol que su §2 y su §6 declaran —el de la
CANDIDATA— y contra ningún otro:

```console
$ (extraer las 79 filas del manifiesto EN EL COMMIT DEL GATE y, para cada una,
   git show f8fc037:<ruta> | sha256sum  y  | wc -l)
filas §4 = 12   filas §5 = 67   total = 79
lineas §4 = 29117   lineas §5 = 48562   suma = 77679
DISCREPANCIAS contra el ARBOL DE LA CANDIDATA: 0
DISCREPANCIAS contra el ARBOL DEL GATE:        1
    ('§4', '1', 'docs/evolucion/00-INDICE.md', 'SHA gate 7523cc2540f7 != fila 89b74fcc16f4')
```

Esa única discrepancia es **la que el propio manifiesto anuncia** en su §6 («*el índice SÍ es
fuente obligatoria y SÍ tiene fila: su SHA-256 cambia entre los dos árboles*») y **la que el
sobre publica** como ruta divergente. **No es un hallazgo.**

### §2.2 · La tabla

| id | severidad | clase | sede (fichero:línea) | qué afirma | qué dice el árbol (comando y salida) | qué se sigue |
|---|---|---|---|---|---|---|
| **`S1-01`** | **BLOQUEANTE** | **A** | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` **L1920-1921** (`_tocados_raw = _git("diff","--name-only","05f71b7")` · `tocados = _tocados_raw.split()`), contra el comentario **L1922-1929** que lo declara corregido, y contra la fila `EE-11` del `CHECKPOINT` **L3790** | `EE-11`, en la sede del parte: «**La salida de git deja de partirse por blancos.** `.split()` sobre `ls-tree`/`diff` fallaba de dos maneras a la vez … **Con `-z` desaparecen las dos**». Y el comentario L1922-1929, dos líneas por debajo del `.split()` que sobrevive: «*Esto hacía `.split()` sobre `git ls-tree --name-only` **y sobre `git diff --name-only`**, y las dos cosas fallaban a la vez … Con `-z` y `\0` desaparecen los dos*» | `_rutas_z` (L1930-1935) se aplica a **tres** lecturas (`diff HEAD`, `ls-tree 05f71b7`, `ls-tree HEAD`, L1937-1942). **La cuarta —`_tocados_raw`, L1920, un `git diff --name-only`— conserva `.split()`.** De ella salen `tocados` → `prohibidos` de `G-23` (L2238-2239), `_kern`/`_kern_ev`/`_kern_dir` (L2259-2261), el contraste de prosa del checkpoint (L2277-2291) y la guarda de `G-22` de L2135. **ATAQUE EJECUTADO** (§3.5): `kernel/operativo/pruebas/evidencia/SENTENCIÑA.txt`, con `git add -A && git commit`. `git diff --name-only 05f71b7` emite `"kernel/operativo/pruebas/evidencia/SENTENCI\303\221A.txt"` —CITADA por `core.quotePath`—, la cadena **no empieza por `kernel/`** y desaparece de `_kern`. Salida: `git status --porcelain` VACÍO · **`38/38 comprobaciones en verde`** · `OK G-23 └─ 6 ficheros de kernel = 3 directos + 3 de evidencia derivada, **todos enumerados en el checkpoint**` —y son SIETE— · universo 80 rutas, **INTACTO** · `EXCLUIDOS por PERÍMETRO: 1` (sólo `.git/`) · DIGEST `1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b`, **BIT A BIT el anclado en el sobre**. **CONTROL POSITIVO**: el MISMO fichero con nombre ASCII (`SENTENCIA-F4C.txt`) da `FALLO G-23 · 37/38 · el checkpoint NO enumera … Git deriva (7,3,4)`. La ÚNICA diferencia es el carácter no-ASCII | **ES EL DÉCIMO ÁRBOL, y es una REINCIDENCIA LITERAL de `R1-09`/`EE-11`, en el remedio de `EE-11`.** Cumple las siete condiciones que el sexto gate exigió al noveno: alcanza el commit · `git status` vacío · **38/38** · fuera del universo · sin fila de manifiesto ni revisor · digest del sobre idéntico · silencioso en las cinco salidas del aparato. Y añade una octava, peor: **`G-23` publica un recuento FALSO —«6 … todos enumerados»— y lo firma en verde**, que es exactamente el modo de fallo `T-05` que el propio comentario de `EE-11` invoca («la comprobación NOMBRA el fichero en su detalle y sigue imprimiendo verde»), aquí agravado porque **ni siquiera lo nombra** |
| **`S1-02`** | **BLOQUEANTE** | **A** | `comprobar-correccion-gate-de-cierre.py` **L3110-3128** (`_base_gobernada` · `_universo_gobernado = _disco \| _publicado` · `_ampliaciones` · `_idos`), su título **L3204** y la fila del README **L244** (`G-29`) | `EE-01`, fila del `CHECKPOINT` **L3780**: «**EL NOVENO ÁRBOL, cerrado por CLASE.** La guarda de admisión **se evalúa contra la REVISIÓN BASE y no contra `HEAD`**: es AMPLIACIÓN todo lo que existe hoy y no existía en la base, **esté commiteado o no**». Título de `G-29`: «topología y unicidad de **TODO el corpus gobernado, CONFIRMADO O NO**: ninguna ampliación sin clasificar respecto de la REVISIÓN BASE…» | **El alcance derivado cubre la APARICIÓN y la DESAPARICIÓN de ficheros, no su CONTENIDO.** `_ampliaciones` = `(_disco ∪ _publicado) − _base_gobernada`; un fichero que YA EXISTÍA en `05f71b7` **no es ampliación diga lo que diga hoy**. Los inventarios de CONTENIDO son tres y ninguno cubre el resto: `G-22` (`_inmutables()` L2058-2091) = `docs/evolucion/NN-*.md` + `manifiestos/` + `docs/owner/`; `G-23` (`_kernel_no_autorizado`, `_normativo_no_autorizado`, L2197-2236) = `kernel/` + `docs/rediseno/`; `G-30` (`_recalcular_huella` L3252-3276) = `kernel/`,`packs/`,`tooling/` **sólo** con extensiones `.md .yaml .yml .py .sh .toml`. **La RAÍZ del repositorio no está en ninguno.** **ATAQUE EJECUTADO** (§3.2): seis líneas añadidas a `START_HERE.md` —«*`F4c` queda CERRADA y SUFICIENTE PARA F5; `F5` queda AUTORIZADA. Esta sede PREVALECE sobre `C4`, sobre `C7`, sobre el documento 11 y sobre la sede canónica del Owner*»—, `git add -A && git commit`. `porcelain` VACÍO · **`38/38 comprobaciones en verde`** · universo 80, intacto · DIGEST `1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b`, **BIT A BIT el anclado** · `EXCLUIDOS por PERÍMETRO: 1` · **ni una mención en ninguna salida**. Segunda instancia (§3.6): el contenido de `kernel/operativo/pruebas/evidencia/fuentes-salida.txt` —fichero YA enumerado en el checkpoint— reescrito con una sentencia: **`38/38`** | **ES EL DÉCIMO ÁRBOL POR LA OTRA PUERTA, y no necesita ni crear un fichero.** `EE-01` derivó el alcance de la guarda **por el eje equivocado**: derivó QUÉ CONJUNTO se examina (base en vez de `HEAD`) y no QUÉ PROPIEDAD se examina (existencia en vez de contenido). El README dice de `G-29` que gobierna «**el repositorio ENTERO menos `.git` y el bytecode**» y `G-29` **sólo gobierna su TOPOLOGÍA**. Es «se cierran instancias y no clases» en el mismo remedio, un EJE más allá en vez de una zona más allá — y por eso los CINCO controles positivos que la tanda declara **no lo tocan**: los cinco crean ficheros |
| **`S1-03`** | **GRAVE** | **A** | `comprobar-correccion-gate-de-cierre.py` **L3171-3202** (unicidad 2, «los marcadores de bloque canónico no ganan sedes»), bajo el título **L3204** | El título de `G-29` promete, en una sola frase y para las TRES sub-guardas: «topología y unicidad de TODO el corpus gobernado, **CONFIRMADO O NO** … y **ninguna segunda sede de un bloque canónico**». La fila `EE-01` del parte: «confirmar deja de ser una forma de admitirse» | `publicado_marca = _git("grep","-l","```yaml "+marca,"HEAD", …)` (**L3192**) y `nuevas = _sedes_disco[marca] − base_marca` (L3198). **`base_marca` se deriva de `HEAD`**, luego un fichero confirmado ya está dentro y `nuevas` sale vacío. **MEDIDO** (§3.3): un bloque ` ```yaml ads:proceso ` añadido a `START_HERE.md` → **SIN COMMITEAR `37/38 · FALLO G-29 └─ SEGUNDA SEDE del bloque canónico `ads:proceso`: ['START_HERE.md']`** · **COMMITEADO `38/38 comprobaciones en verde`**, `porcelain` vacío | **Es la asimetría `DD-02`/`EE-01` VIVA en la sub-guarda de al lado, y la denunció `R1` en su `RF-4` del sexto gate** («*descubre que el segundo control tiene la MISMA inercia … Son DOS guardas de `G-29`, no una, y las dos miden contra `HEAD`*»). `EE-01` corrigió la primera y **no la segunda**, y el título —que es UNO para las tres— pasó a decir «CONFIRMADO O NO» de las tres. **La sexta condición de `O18` —«ninguna promesa de seguridad superior a la realmente entregada»— vuelve a fallar, en la misma comprobación y en el mismo renglón** |
| **`S1-04`** | **GRAVE** | **A** | `derivar-universo-obligatorio.py` **L173-175** y el docstring de `_excluidos()` **L736-741**; sus únicas vías de llenado, **L238** (`_resolver`) y **L560** (`_barrer`) | L173-175: «**Y mientras algo quede fuera, se PUBLICA con su ruta**: `EXCLUIDOS_PERIMETRO` lo emite por todos los modos, como `EXCLUIDOS_IV` hace con el componente (iv). **Una exclusión silenciosa es la puerta**; una exclusión publicada es una línea que el revisor lee». L739-741: «*Mientras algo se excluya, se dice cuál y por qué: una exclusión silenciosa es el octavo árbol*» | `grep -n '_excluido(\|_podar(' derivar-universo-obligatorio.py` → definiciones en L205/L218 y **sólo dos llamadas cada una**: L235/L238 dentro de `_resolver()` y L557/L560 dentro de `_barrer()`. `_resolver` recorre el árbol entero pero **sólo evalúa `_excluido` sobre los ficheros cuyo BASENAME es uno de los cuatro del componente (i)** —derivados: `ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md`, `16-GATE-FINAL-INDEPENDIENTE-F4C.md`, `17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md`, `18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md`—; `_barrer` sólo recorre las DOS zonas, `docs/owner` y `docs/evolucion/verificacion/manifiestos`. **Todo lo demás del repositorio nunca llega a `_excluido`.** **ATAQUE EJECUTADO** (§3.4): `docs/normativa/SENTENCIA.md` fabricado con la cabecera que `_es_bytecode` exige y texto **Latin-1** dentro, commiteado. Batería **`38/38`**, y su `G-29` **sí** lo nombra (`PERÍMETRO: 2 … docs/normativa/SENTENCIA.md · bytecode de CPython, por CONTENIDO`); **el DERIVADOR publica `EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 1` — sólo `.git/`—**, y el sobre copia exactamente eso. DIGEST idéntico | **La promesa del derivador es FALSA fuera de dos zonas, y es justo la promesa sobre la que `R1` del sexto gate cerró su variante `V4`** («*pasa la batería y no mueve el digest **pero NO ES SILENCIOSO**: el sobre lo publicaría con su ruta completa … Ése es exactamente el remedio que `DD-01` prescribió, y **funciona**»). Funciona **sólo dentro de `docs/owner/`**, que es donde `R1` lo plantó. **Instancia cerrada, clase abierta**, y el objeto que se degrada es EL SOBRE: el revisor recibe «PERÍMETRO: 0» sobre un árbol que excluye un documento |
| **`S1-05`** | **MEDIO** | **A** | `derivar-universo-obligatorio.py` **L182-202** (`_es_bytecode`, docstring L183-189) y su gemela en la batería **L1987-2007**; contra `_leer` **L138-148** (`EE-09`) | Docstring de `_es_bytecode`: «Se exigen las TRES cosas, de modo que ningún documento puede parecerlo por accidente —**ni fabricarse para parecerlo sin dejar de ser ilegible como texto, que es justamente no ser un documento**—». En la batería, L1992-1993: «*no puede fabricarse para parecerlo sin dejar de ser **legible** como texto — que es, exactamente, dejar de ser un documento*» | El predicado es: 4 bytes de cabecera, `cabecera[2:4] == b"\r\n"`, `cabecera[1] <= 0x1F`, y que los primeros 65540 bytes **no decodifiquen como UTF-8**. **No-UTF-8 ≠ ilegible.** Fabricado y medido (§3.4): `b"\x0d\x0a\x0d\x0a" + texto.encode("latin-1")` con `decisi\xf3n` dentro. `iconv -f latin1 -t utf-8 docs/owner/SENTENCIA-LATIN1.md \| head -3` → «SENTENCIA DEL OWNER / F4c queda CERRADA y SUFICIENTE PARA F5…», **perfectamente legible**. Y el motivo que el instrumento publica de él es **«bytecode de CPython, por CONTENIDO»**, que es falso: no lo es. Con ese fichero bajo `docs/owner/` la batería da **`38/38`**, el fichero queda FUERA de `_publicado` y por tanto **fuera del bucle `_owner_publicado` de `DD-02` (L3144-3155) y fuera de `_inmutables()` de `G-22`** | **La misma propiedad —no decodificar como UTF-8— significa «FALLA CERRADO, una sede que el corpus no puede leer no se interpreta» en `_leer` (`EE-09`, L139-148) y «no es corpus, se cae del perímetro» en `_es_bytecode`, a 40 líneas de distancia y en el mismo fichero.** Cuál de las dos se aplica lo decide **un prefijo de cuatro bytes**. La docstring promete una imposibilidad que no existe, y el motivo publicado es una afirmación falsa sobre el fichero. Es la sexta condición de `O18` dentro del remedio `DD-01` |
| **`S1-06`** | **MEDIO** | **A** | `comprobar-correccion-gate-de-cierre.py` **L123-131** (comentario de `EE-17`) y **L354-362** (`_desajuste`, que sólo se imprime) | Comentario L130-131: «el TÍTULO se CONTRASTA contra ella: **si divergen en un solo identificador, es ROJO y se nombra**. El título deja de ser el discriminante y pasa a ser lo contrastado». Fila `EE-17` del parte, `CHECKPOINT` L3795: «el TÍTULO se contrasta contra ella: si divergen en un identificador, **se dice**» | `_desajuste` se calcula en L357 y se **imprime** en L359-362; `verde` se calcula en L341 **sobre `RES`** y el retorno es `0 if verde == len(RES)` (L371). **El desajuste no llama a `check()` y no toca ni el recuento ni el código de salida.** MEDIDO (§3.7): añadido «(falla CERRADO sin git)» al título de `G-27`, que NO está en `_EXIGEN_HISTORIA`, y **commiteado** → `38/38 comprobaciones en verde` · `EXIT=0` · y debajo, impresa, la línea `ALCANCE · DESAJUSTE (EE-17): ['G-27'] — el TÍTULO y la PROPIEDAD declarada no coinciden` | El comentario del código —que es la sede del remedio— dice **ROJO** y el código dice **impreso**. Sin commitear el árbol sí sale en rojo, pero **por `G-34`** (instrumental modificado y no declarado), no por el desajuste; **una vez confirmado, `G-34` calla y el desajuste queda en una línea decorativa**. Es la MISMA forma de inercia-tras-confirmar que `EE-01` dice haber cerrado, dentro de otro remedio de la misma tanda |
| **`S1-07`** | **MEDIO** | **A** | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L1782-1786** (dentro de mi rango L1–L5200), contra **L1739-1742** del mismo bloque | L1782: «**Ninguna se ha ejecutado.** **Cuarenta y seis** filas escritas es el contrato de lo que F6 debe demostrar, y no es su demostración», seguida en L1783-1786 del desglose «Trece … siete (`X47`–`X53`) … cinco (`X54`–`X58`) … tres (`X59`–`X61`) … una (`X62`)». Cuarenta líneas más arriba, **L1739-1742**: «*el cardinal NO se escribe aquí: **se DERIVA*** —`grep -cE '^\| \`X[0-9]{2}\` \|' …`— … **Corregido por `DD-13` del QUINTO GATE: esta frase escribía «cuarenta y seis», y `X63` la dejó caducada en el acto**» | El comando que el propio documento publica, ejecutado sobre el árbol de la candidata: `grep -cE '^\| \`X[0-9]{2}\` \|' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` → **47**; ids únicos → **47**. Y el desglose no cierra: `13+7+5+3+1 = 29`, más las 17 originales = **46**. Verificado que la línea es VIVA: la marca `[HISTÓRICO]` más cercana (L1772) cierra dentro de su propio bloque vallado, que termina en L1780. Y verificado que sobrevive a la tanda: `git show <C>:… \| grep -c 'Cuarenta y seis filas escritas'` → **1** en `b27a761`, `98cdb7a`, `f8fc037` y `08f6da6`, con `git diff --stat b27a761 f8fc037 -- …11-ARQ…` → `36 ++++----` (la tanda SÍ tocó el fichero) | **Es la TERCERA instancia del cardinal `46`, en la sede DEFINITORIA, y la tanda cerró las otras dos.** `EE-07`/`EE-12` retiraron el `46` de las dos sedes del `CHECKPOINT` —hoy L2426 «*y hoy son **más**: `X63` la añadió la tanda*» y L3009 `[HISTÓRICO · EE-12]`—, y **`EE` escribió con todas las letras** (doc 27 L3151-3152) que era «*EL MISMO cardinal que `DD-13` retiró del documento 11 EN ESTA MISMA TANDA … **y que quedó vivo una sede más allá**»*. Nadie miró la sede de la que se retiró. **La sede que gobierna el contrato de prueba de `F6` publica hoy un cardinal que su propio comando desmiente, cuarenta líneas por debajo de la nota que declara ese cardinal caducado.** Es `DD-13` ≡ `EE-07` ≡ `EE-12` una sede más allá, en la dirección contraria a la que se miró |
| **`S1-08`** | **MENOR** | **A** | `emitir-sobre-de-ancla.py` **L234-242** (`_lineas_de`) y **L294-299** (el comentario de `EE-16`), contra `derivar-universo-obligatorio.py` **L726-733** (`metricas`) | Comentario L297-299: «dos implementaciones de la misma derivación acaban divergiendo, que es lo que este corpus persigue en todas partes. **Se usa UNA, y es la del derivador, que es la sede de las métricas del universo**». Fila `EE-16` del parte: «El recuento de líneas **deriva de una sola sede**» | El emisor **sigue definiendo su propia función** (`def _lineas_de(crudo):`, L234) y **no importa nada del derivador**: `re.findall(r"^import (\w+)\|^from (\S+)", emisor)` → `argparse, datetime, hashlib, os, re, shutil, subprocess, sys, tempfile`. Siguen siendo **DOS implementaciones**; lo que cambió es que hoy coinciden. Evaluadas las dos sobre `b""`, `b"a"`, `b"a\n"`, `b"a\nb"`: IGUAL, IGUAL, IGUAL, IGUAL | **El remedio a «dos implementaciones divergen» fue escribir una tercera copia idéntica, no crear una sede.** La afirmación «se usa UNA» es falsa como está escrita, y el riesgo que el propio comentario nombra sigue exactamente donde estaba. **LATENTE**: hoy coinciden y no hay ficheros vacíos (`git ls-tree -r -l <C> \| awk '$4==0' \| wc -l` → 0 en los DOS árboles), y por eso es MENOR y no MEDIO |
| **`S1-09`** | **MENOR** | **A** | El manifiesto **`F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md` §4, fila 2** (`11-ARQUITECTURA-INTEGRADA.md` · **S1 L1-L5200** · S2 L5201-final) contra su §3 (`REVISOR S1 … Audita EL INSTRUMENTO —batería, derivador y emisor— y los manifiestos`) | El reparto asigna a `S1` el dominio «protocolo … y DERIVADORES» y «EL INSTRUMENTO … y los manifiestos», y le da del documento 11 el rango **L1–L5200** | Las sedes NORMATIVAS del instrumento que `S1` audita viven **todas** en la otra mitad: `grep -n '^## \`C-L\.5\`\|^## 11\.4 \|^## 11\.6 \|^## 11\.9 ' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` → **11541** (`C-L.5` · la sede de `1bis`, de la que el derivador LEE sus cardinales), **8244** (§11.4, la raíz de confianza), **8320** (§11.6, **EL SOBRE DE ANCLA**), **8903** (§11.9, la sede canónica del Owner). **Las cuatro están en L5201–L11708, el rango de `S2`** | **El revisor que audita el derivador no tiene asignada la sede de la que el derivador deriva.** Yo verifiqué el derivador contra `1bis` **ejecutándolo** —falla cerrado si la sede no dice lo que dice—, no leyéndola, y lo declaro en §1.4 y en §6. Es EXACTAMENTE la limitación que `R1` del sexto gate puso la SEGUNDA de su §6 («*la carencia más incómoda de mi lote*») y que `EE` elevó a OBSERVACIÓN DE MÉTODO por encima de tres hallazgos: **el manifiesto 7 no la corrigió y repartió igual.** MENOR, y es del APARATO del gate, no del objeto auditado |

### §2.3 · Recuento, DERIVADO de las filas de arriba

```text
BLOQUEANTE   2     S1-01 · S1-02
GRAVE        2     S1-03 · S1-04
MEDIO        3     S1-05 · S1-06 · S1-07
MENOR        2     S1-08 · S1-09
             ─
             9

POR CLASE    A 9  ·  B 0  ·  C 0
POR ÁRBOL    DE LA CANDIDATA `f8fc037` (el objeto auditado)   8   S1-01 … S1-08
             DEL APARATO DEL GATE `08f6da6`                   1   S1-09
             DEL SOBRE                                        0
```

**NINGUNO ES DE CLASE `C`.** Los cuatro ataques que consuman —`S1-01`, `S1-02`, `S1-03`,
`S1-04`— usan `git add -A && git commit` sin un solo flag, que es la frontera que `DD-20` fija
y que `EE` reconfirmó en su `RF-1` del sexto gate. **NINGUNO ES DE CLASE `B`**: los nueve se
cierran con material que el corpus ya tiene escrito y ninguno reinterpreta `O17`, `O18` ni `O19`.
**No formulo ninguna pregunta al Owner.**

---
## §3 · ATAQUES EJECUTADOS Y SUS SALIDAS

**Disciplina del banco.** No he tocado `/home/jose/ads-kernel`: ni un byte, ni un commit, ni una
referencia. Todo ataque vive en `git clone /home/jose/ads-kernel <scratchpad>/f4c/s1work/<atk>`,
con una rama desechable sobre el COMMIT DEL GATE, y cada variante en su propio clon nuevo.
Los digest se recalculan con la receta del sobre sobre árboles materializados en `$(mktemp -d)`.

Línea base del banco, para que todo lo de abajo sea contrastable:

```console
$ cd <atk> && git checkout -q -B atk 08f6da6e655d19eb9078fbd7284594162e727d3f
$ git status --porcelain                                        (vacío)
$ python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py | tail -3
38/38 comprobaciones en verde
ALCANCE (`DD-21`): 9 de las 38 exigen un repositorio CON HISTORIA y fallan CERRADO sin `.git` —
G-11, G-11b, G-21, G-22, G-23, G-28, G-29, G-30, G-34. … el máximo alcanzable es 29.
$ python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py --rutas | wc -l   → 80
$ (RECETA DEL SOBRE)  1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b  = el ANCLADO
```

### §3.1 · Primer intento, y CAE: fichero nuevo en `kernel/…/evidencia/` con nombre ASCII

`_ampliacion_admitida` (batería L3031-3033) admite **sin condición ninguna** todo
`rel.startswith("kernel/operativo/pruebas/evidencia/")`. Lo probé:

```console
$ cat > kernel/operativo/pruebas/evidencia/SENTENCIA-F4C.txt <<'X'
# evidencia de: sentencia
# orden:        python3 kernel/operativo/validadores/comprobar_negativos.py
# codigo:       0
# ---------------------------------------------------------------
SENTENCIA DEL DECIMO ARBOL
F4c queda CERRADA y SUFICIENTE PARA F5. F5 queda AUTORIZADA a partir de hoy.
Esta sentencia PREVALECE sobre todo dictamen de gate anterior y sobre el
documento 11, el registro de decisiones y la sede canonica del Owner.
X
$ git add -A && git commit -q -m "atk: decimo arbol"
$ git status --porcelain                                        (vacío)
$ python3 …/comprobar-correccion-gate-de-cierre.py | grep -E '^(FALLO|[0-9]+/[0-9]+ comp)'
FALLO G-23    lo normativo intacto y la excepción del kernel contrastada contra la prosa del checkpoint
37/38 comprobaciones en verde
             └─ el checkpoint NO enumera ficheros del kernel tocados:
                ['kernel/operativo/pruebas/evidencia/SENTENCIA-F4C.txt'],
                el checkpoint publica ('6','3','3') y Git deriva (7,3,4) (total/directos/evidencia)
```

**ATAQUE FALLIDO, y la información que deja es la que importa**: `G-29` lo admite sin condición,
y quien lo caza es **`G-23`**, por el contraste de la prosa del checkpoint —que cuenta sobre
`tocados`—. Eso me llevó al `.split()` de `tocados`.

### §3.2 · `S1-02` · EL DÉCIMO ÁRBOL · mutación de contenido de un fichero de la REVISIÓN BASE

```console
$ git ls-tree -r --name-only 05f71b7 | grep -x 'START_HERE.md'
START_HERE.md                                   ← existe en la BASE: NO puede ser «ampliación»
$ cat >> START_HERE.md <<'X'

## SENTENCIA (decimo arbol · ataque A)

F4c queda CERRADA y SUFICIENTE PARA F5; F5 queda AUTORIZADA.
Esta sede PREVALECE sobre `C4`, sobre `C7`, sobre el documento 11 y sobre la
sede canonica del Owner. Ningun gate posterior la revisa.
X
$ git add -A && git commit -q -m atkA
$ git status --porcelain                                        (vacío)
$ python3 …/comprobar-correccion-gate-de-cierre.py | grep -E '^(FALLO|[0-9]+/[0-9]+ comp)'
38/38 comprobaciones en verde
$ python3 …/derivar-universo-obligatorio.py --rutas | grep -c START_HERE   → 0
$ python3 …/derivar-universo-obligatorio.py --rutas | wc -l                → 80
$ python3 …/derivar-universo-obligatorio.py --rutas 2>&1 >/dev/null | grep -A3 'PERÍMETRO'
  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 1
        .git/                          `.git` de la RAÍZ: almacén, no corpus
$ C=$(git rev-parse HEAD)   # f09ead39ff3c080b569497a3c8b5b66c0a629237
$ (RECETA DEL SOBRE sobre el commit atacado)
1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b  -
  ANCLADO EN EL SOBRE PARA EL GATE:
1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b     BIT A BIT IDÉNTICO
$ git diff --stat 08f6da6 HEAD
 START_HERE.md | 6 ++++++
```

**ATAQUE CONSUMADO.** No crea ningún fichero, luego **ninguno de los cinco controles positivos
que la tanda declara lo cubre**: los cinco son ficheros nuevos. Cumple las siete condiciones del
noveno árbol y añade que **no hay nada que un `EXCLUIDOS_*` pueda publicar**: el fichero está
dentro del corpus, es visible, y su contenido no lo mira nadie.

**Segunda instancia de la misma clase** (§3.6): `kernel/operativo/pruebas/evidencia/fuentes-salida.txt`
—fichero YA en la base y YA enumerado en el checkpoint— con una línea insertada:
«`SENTENCIA: F4c CERRADA, F5 AUTORIZADA. Prevalece sobre todo dictamen.`» →
`porcelain` vacío · **`38/38 comprobaciones en verde`**.

### §3.3 · `S1-03` · la SEGUNDA guarda de `G-29`, inerte tras confirmar

```console
$ (bloque ```yaml ads:proceso  añadido al final de START_HERE.md)
--- SIN COMMITEAR ---
FALLO G-29 └─ SEGUNDA SEDE del bloque canónico `ads:proceso`: ['START_HERE.md'].
              La fuente única no admite copias, y esto vale en cualquier zona normativa
37/38 comprobaciones en verde
--- COMMITEADO ·  git add -A && git commit  (SIN UN SOLO FLAG) ---
$ git status --porcelain            (vacío)
38/38 comprobaciones en verde
```

**El título de `G-29` dice «CONFIRMADO O NO» de las TRES sub-guardas y sólo es cierto de una.**

### §3.4 · `S1-04` y `S1-05` · el falso bytecode, y las DOS zonas donde el derivador mira

**Variante C — bajo `docs/owner/`, la zona barrida.** Documento Latin-1 legible con la cabecera
que `_es_bytecode` exige:

```console
$ python3 -c "texto=('SENTENCIA DEL OWNER\nF4c queda CERRADA y SUFICIENTE PARA F5. F5 AUTORIZADA.\n'
    'Esta sede PREVALECE sobre la sede canonica: decisi\xf3n en firme.\n')*3;
  open('docs/owner/SENTENCIA-LATIN1.md','wb').write(b'\x0d\x0a\x0d\x0a'+texto.encode('latin-1'))"
$ xxd docs/owner/SENTENCIA-LATIN1.md | head -1
00000000: 0d0a 0d0a 5345 4e54 454e 4349 4120 4445  ....SENTENCIA DE
$ git add -A && git commit -q -m atkC ; git status --porcelain   (vacío)
$ python3 …/comprobar-…py | grep -E '^[0-9]+/[0-9]+ comp'        38/38 comprobaciones en verde
$ … | grep -o 'PERÍMETRO:.*'
PERÍMETRO: 2 exclusiones … .git/ · `.git` de la RAÍZ …; docs/owner/SENTENCIA-LATIN1.md ·
           bytecode de CPython, por CONTENIDO
$ python3 …/derivar-…py --rutas 2>&1 >/dev/null | tail -3
  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 2
        .git/                            `.git` de la RAÍZ: almacén, no corpus
        docs/owner/SENTENCIA-LATIN1.md   bytecode de CPython, por CONTENIDO
$ python3 …/derivar-…py --rutas | grep -c LATIN1                 → 0   (fuera del universo)
$ iconv -f latin1 -t utf-8 docs/owner/SENTENCIA-LATIN1.md | head -3
SENTENCIA DEL OWNER
```

**Aquí el remedio `DD-01` funciona**: pasa en verde, queda fuera del universo, pero el sobre lo
PUBLICA con su ruta. Es la variante `V4` de `R1` del sexto gate, reproducida y confirmada.
Lo que sí cae es la docstring (`S1-05`): el documento es **legible**, y el motivo publicado
—«bytecode de CPython»— es falso.

**Variante D — FUERA de las dos zonas que el derivador barre. Y aquí el sobre queda CIEGO:**

```console
$ mkdir -p docs/normativa
$ python3 -c "texto=('SENTENCIA NORMATIVA\nF4c CERRADA. F5 AUTORIZADA. PREVALECE SOBRE TODO.\n'
    'Firmado: el Owner, decisi\xf3n en firme.\n')*5;
  open('docs/normativa/SENTENCIA.md','wb').write(b'\x0d\x0a\x0d\x0a'+texto.encode('latin-1'))"
$ git add -A && git commit -q -m atkD ; git status --porcelain   (vacío)
$ python3 …/comprobar-…py | grep -E '^[0-9]+/[0-9]+ comp'        38/38 comprobaciones en verde
$ … | grep -o 'PERÍMETRO:.*'
PERÍMETRO: 2 exclusiones … ; docs/normativa/SENTENCIA.md · bytecode de CPython, por CONTENIDO
$ ### PERO LO QUE VIAJA EN EL SOBRE ES ESTO:
$ python3 …/derivar-universo-obligatorio.py --rutas 2>&1 >/dev/null | tail -3
  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 1
        .git/                            `.git` de la RAÍZ: almacén, no corpus
$ python3 …/derivar-…py --rutas | wc -l                          → 80
$ (RECETA DEL SOBRE)  1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b  = ANCLADO
```

**El sobre publicaría «EXCLUIDOS por PERÍMETRO: 1» sobre un árbol que excluye un documento que
declara `F4c` cerrada.** La batería lo nombra; el ancla externa, no.

### §3.5 · `S1-01` · EL DÉCIMO ÁRBOL POR `EE-11`: una ruta no-ASCII en el kernel

```console
$ cat > "kernel/operativo/pruebas/evidencia/SENTENCIÑA.txt" <<'X'
# evidencia de: sentencia
# orden:        python3 kernel/operativo/validadores/comprobar_negativos.py
# codigo:       0
# ---------------------------------------------------------------
SENTENCIA · DECIMO ARBOL (via EE-11 no cerrado)
F4c queda CERRADA y SUFICIENTE PARA F5. F5 queda AUTORIZADA.
Esta sede PREVALECE sobre todo dictamen de gate, sobre el documento 11 y
sobre la sede canonica del Owner.
X
$ git add -A && git commit -q -m atkJ
$ git status --porcelain                                          (vacío)
$ git diff --name-only 05f71b7 | grep -i sentenci
"kernel/operativo/pruebas/evidencia/SENTENCI\303\221A.txt"        ← CITADA por core.quotePath
$ python3 …/comprobar-correccion-gate-de-cierre.py | grep -E '^(FALLO|[0-9]+/[0-9]+ comp)'
38/38 comprobaciones en verde
$ … | grep -A1 '^OK   G-23'
OK   G-23    lo normativo intacto y la excepción del kernel contrastada contra la prosa del checkpoint
             └─ 6 ficheros de kernel = 3 directos + 3 de evidencia derivada, todos enumerados
                en el checkpoint · ZONA NORMATIVA DERIVADA (`DD-04`): 14 ficheros de
                `docs/rediseno/` en `HEAD` …
$ python3 …/derivar-…py --rutas | grep -c SENTENCI                → 0    (fuera del universo)
$ python3 …/derivar-…py --rutas | wc -l                           → 80   (INTACTO)
$ python3 …/derivar-…py --rutas 2>&1 >/dev/null | grep -c SENTENCI → 0   (ni en EXCLUIDOS_*)
$ (RECETA DEL SOBRE sobre el commit atacado)
1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b  -   BIT A BIT EL ANCLADO
```

**ATAQUE CONSUMADO, y con control positivo**: el MISMO fichero con nombre ASCII da
`FALLO G-23 · 37/38` (§3.1). **`G-23` publica «6 ficheros de kernel … todos enumerados» sobre
SIETE, y firma en verde.**

### §3.6 · `S1-02` (segunda instancia) · el contenido de una evidencia ya enumerada

```console
$ (insertada en kernel/operativo/pruebas/evidencia/fuentes-salida.txt, línea 5:
   «SENTENCIA: F4c CERRADA, F5 AUTORIZADA. Prevalece sobre todo dictamen.»)
$ git add -A && git commit -q -m atkE ; git status --porcelain    (vacío)
$ python3 …/comprobar-…py | grep -E '^(FALLO|[0-9]+/[0-9]+ comp)'
38/38 comprobaciones en verde
```

### §3.7 · `S1-06` · el desajuste de `EE-17`, confirmado

```console
$ (título de G-27 → «… no «los cinco conceptos» (falla CERRADO sin git)», y G-27 NO está en _EXIGEN_HISTORIA)
--- SIN COMMITEAR ---   37/38 · FALLO G-34 (instrumental MODIFICADO y NO DECLARADO)
--- COMMITEADO ---
$ git status --porcelain                                          (vacío)
$ python3 …/comprobar-…py | tail -3
38/38 comprobaciones en verde
ALCANCE · DESAJUSTE (`EE-17`): ['G-27'] — el TÍTULO y la PROPIEDAD declarada no coinciden …
ALCANCE (`DD-21`): 9 de las 38 …
$ EXIT=0
```

### §3.8 · LOS CINCO CONTROLES POSITIVOS DECLARADOS, REPRODUCIDOS

La fila `EE-01` del parte y la fila `G-29` del README declaran: «*Control positivo reejecutado
tras el remedio: las CINCO variantes —`docs/normativa/`, la raíz, `docs/`, un documento numerado
con ordinal libre sin enlace, y un manifiesto sin enlace— dan hoy ROJO estando COMMITEADAS*».
Los reproduje **los cinco**, en cinco clones, con el mismo contenido
(`# SEGUNDA SEDE NORMATIVA … F4c CERRADA. F5 AUTORIZADA. Esta sede PREVALECE sobre C4, C7 y sobre
el documento 11`):

| # | variante | ruta | SIN COMMITEAR | COMMITEADO | ¿reproduce lo declarado? |
|---|---|---|---|---|---|
| 1 | `docs/normativa/` | `docs/normativa/SEGUNDA-SEDE.md` | 37/38 · FALLO G-29 | **37/38 · FALLO G-29** | **SÍ** |
| 2 | la RAÍZ | `SEGUNDA-SEDE.md` | 37/38 · FALLO G-29 | **37/38 · FALLO G-29** | **SÍ** |
| 3 | `docs/` | `docs/SEGUNDA-SEDE.md` | 37/38 · FALLO G-29 | **37/38 · FALLO G-29** | **SÍ** |
| 4 | numerado, ordinal libre, sin enlace | `docs/evolucion/28-SEGUNDA-SEDE-NORMATIVA.md` | 37/38 · FALLO G-29 | **37/38 · FALLO G-29** | **SÍ** |
| 5 | manifiesto sin enlace | `…/manifiestos/F4C-FALSO-MANIFIESTO.md` | 37/38 · FALLO G-29 | **37/38 · FALLO G-29** | **SÍ** |

Detalle idéntico en los cinco, con la ruta nombrada:
`AMPLIACIÓN NO CLASIFICADA del corpus gobernado, CONFIRMADA O NO: <ruta>. … El alcance de esta
guarda se DERIVA contra la REVISIÓN BASE y no contra `HEAD` (`EE-01`): confirmar un fichero NO lo
exime de la condición de su zona`.

**¿SON CONTINGENTES DEL ÁRBOL O TAUTOLÓGICOS? — CONTINGENTES, y lo medí en vez de suponerlo.**
Tomé el control 4 y le añadí **su enlace en `00-INDICE.md`**, replicando la fila de un documento
ya enlazado:

```console
$ (añadida a 00-INDICE.md una fila con  [`28-SEGUNDA-SEDE-NORMATIVA.md`](28-SEGUNDA-SEDE-NORMATIVA.md))
$ git add -A && git commit -q -m enlace
$ python3 …/comprobar-…py | grep -E '^(FALLO|[0-9]+/[0-9]+ comp)'
38/38 comprobaciones en verde
```

**El MISMO fichero pasa de `37/38` a `38/38` sólo por su enlace.** La guarda depende del árbol,
no es una tautología, y el control positivo es legítimo. **La tanda dice la verdad en los cinco.**

**Y LA SEXTA PUERTA, que el manifiesto pide buscar, existe y son CUATRO** (`S1-01` … `S1-04`):
las cinco variantes declaradas comparten una premisa —**crear un fichero**— y tres de mis cuatro
ataques no la usan o la usan por un camino que `tocados` no ve.

### §3.9 · ATAQUES QUE EJECUTÉ Y QUE CAYERON — porque un ataque fallido es información

| # | variante | ¿alcanza el commit? | `git status` | batería | universo | ¿DÉCIMO ÁRBOL? |
|---|---|---|---|---|---|---|
| F | **enlace simbólico** nuevo en la raíz a una sede (`RESOLUCIONES.md -> docs/owner/ADS-OWNER-RESOLUCIONES.md`) | sí | vacío | **37/38 · FALLO G-29** | — | **NO** |
| G | **fichero VACÍO** nuevo en la raíz (`VACIO.txt`) | sí | vacío | **37/38 · FALLO G-29** | — | **NO** |
| H | **documento numerado con ordinal UNICODE** (`docs/evolucion/٢٨-SENTENCIA.md`, dígitos árabes; `\d\d` de Python los casa) | sí | vacío | **37/38 · FALLO G-29** | — | **NO** — `_ENLAZADOS_INDICE` es ASCII y nunca puede admitirlo |
| I | **`.gitattributes` nuevo en la raíz** | sí | vacío | **37/38 · FALLO G-29** | — | **NO** — y el árbol no tiene ninguno: `git ls-tree -r --name-only 08f6da6 \| grep -i gitattr` → vacío |
| — | **submódulos** | — | — | — | — | **NO PROCEDE**: `git ls-files -s \| awk '$1==160000'` → vacío, sin `.gitmodules` |
| — | **rutas con espacio o no-ASCII preexistentes** | — | — | — | — | **NO HAY**: `git ls-tree -r --name-only 08f6da6 \| LC_ALL=C grep '[^ -~]\| '` → vacío |
| — | **fichero nuevo en `docs/evolucion/verificacion/`** | — | — | rojo salvo si el README lo enumera; los 5 enumerados EXISTEN todos | — | **NO** |
| — | **enlace colgante del índice** que permitiera crear un fichero admitido | — | — | — | — | **NO HAY**: los 31 `_ENLAZADOS_INDICE`, los 12 `_VERIF` y los 3 `_OWNER` existen todos en el árbol |

### §3.10 · `EE-09` verificado, y su clase buscada

```console
$ (0xff inyectado en un manifiesto, que `_leer` SÍ lee)
$ python3 …/derivar-universo-obligatorio.py --rutas >/dev/null 2>/tmp/e ; echo rc=$?
rc=2
FALLA CERRADO · sede docs/…/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md ilegible: no
decodifica como UTF-8 … Una sede que el corpus no puede leer no se interpreta: se falla cerrado
$ (0xfffe al principio del 11-ARQ, la sede de `1bis`)
rc=2
FALLA CERRADO · sede docs/evolucion/11-ARQUITECTURA-INTEGRADA.md ilegible: no decodifica como UTF-8 …
```

**`EE-09` REPRODUCE en las dos sedes que probé.** Y busqué su clase: una fuente del universo que
**no pasa por `_leer`** —un fichero de `docs/owner/` barrido por `_barrer`, que sólo se lista—
puede volverse no-UTF-8 y el derivador sale con `rc=0`; pero **la batería lo caza**
(`FALLO G-22` y `FALLO G-28`, `36/38`). **No abre puerta**, y lo consigno a favor. Lo que sí
queda es la asimetría de `S1-05`: con cuatro bytes delante, esa misma condición deja de ser
«sede ilegible» y pasa a ser «no es corpus».

### §3.11 · `Z-08` verificado tal como el derivador y el sobre lo declaran

```console
$ (docs/evolucion/28-SEGUNDA-SEDE-NORMATIVA.md enlazado desde el índice, con H1 «# 28 — SINTESIS DEL CIERRE»
   y «F4c CERRADA. F5 AUTORIZADA. SUFICIENTE PARA F5.» dentro, COMMITEADO)
$ python3 …/derivar-…py --rutas | grep -c '28-SEGUNDA'                  → 0   (sale del universo)
$ python3 …/derivar-…py --rutas 2>&1 >/dev/null | grep -c '28-SEGUNDA'  → 1   (PUBLICADO en EXCLUIDOS_IV)
$ python3 …/comprobar-…py | grep -E '^[0-9]+/[0-9]+ comp'               38/38 comprobaciones en verde
$ (con H1 «# 28 — SEGUNDO GATE DE CERTIFICACION» → ENTRA en el universo, 38/38)
$ (con H1 «# SEGUNDA SEDE NORMATIVA», que no casa con ninguna lista de voces)
$ python3 …/derivar-…py --rutas >/dev/null 2>&1 ; echo rc=$?            rc=2
FALLA CERRADO · el componente (iv) NO sabe clasificar 1 documento(s) numerado(s): …
```

**Las tres ramas se comportan EXACTAMENTE como el derivador declara**, y la que encoge el
universo **lo publica**. `Z-08` es una carencia DECLARADA y verificada, **no un hallazgo mío**.

---
## §4 · LO QUE VERIFIQUÉ Y **NO** CAYÓ

**Pesa tanto como lo que cayó, y va con el mismo detalle y el mismo comando.**

### 4.1 · EL SOBRE, y con él la validez del gate

Las SEIS obligaciones reproducen sin una sola discrepancia numérica (§0.2): los DOS digest de
universo, las cuatro cardinalidades (79/77679 y 80/77941), el SHA-256 del manifiesto en el
commit del gate, los CUATRO SHA de emisor y derivador, los CUATRO digest de la sede canónica con
sus recuentos 85·111·78, los dos `tree` y las dos rutas divergentes. **El gate NO es INVÁLIDO
por ninguna vía que yo pueda medir.**

Y una comprobación que nadie me pidió y que la obligación 5 sugiere:

```console
$ git ls-files -v | grep -vc '^H '
0
```

**Ni un fichero en `skip-worktree` ni en `assume-unchanged`** en el índice local del repositorio
auditado, que es la trampa concreta que `Z-11` nombra.

### 4.2 · EL MANIFIESTO 7 · sus DOS aritméticas DERIVAN de verdad

Es lo que `EE-02` exige y lo que el manifiesto declara en su §6. **Lo verifiqué en las dos
direcciones y sobre los DOS árboles:**

```console
$ comm -23 <(universo de f8fc037, 79 rutas) <(las 79 filas del manifiesto)   → ∅
$ comm -13 <(universo de f8fc037, 79 rutas) <(las 79 filas del manifiesto)   → ∅
        OBLIGATORIO − ASIGNADO (CANDIDATA)  =  0   ·  ASIGNADO − OBLIGATORIO = 0
$ comm -23 <(universo de 08f6da6, 80 rutas) <(las 79 filas del manifiesto)
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md
$ comm -13 …                                                                  → ∅
        OBLIGATORIO − ASIGNADO (GATE)  =  1   ·  y es EL MANIFIESTO EN CURSO, y sólo él
$ (aritmética de líneas)  29117 (§4, 12 filas) + 48562 (§5, 67 filas) = 77679 = LÍNEAS
                          OBLIGATORIAS de la candidata que el sobre publica
```

**LAS DOS ARITMÉTICAS CIERRAN.** Y el §6 hace exactamente lo que `EE-02` ordenó: **no escribe la
resta del árbol del gate; enumera las fuentes sin fila, una a una, con su razón.** Las tres que
enumera son las tres correctas:

```text
ESTE MANIFIESTO           punto fijo · INEVITABLE          → verificado: es la única que sobra
LA EVIDENCIA REEJECUTADA  `fuentes-`, `negativos-`, `referencias-salida.txt`
                          «NO son fuentes obligatorias: no entran en el universo y por tanto no
                          restan»                          → verificado: `grep evidencia` sobre
                          las 80 rutas del universo del gate → 0
LA FILA DE `00-INDICE.md` «su SHA-256 cambia entre los dos árboles»
                          → verificado: es la única fila que no casa contra el árbol del gate
```

**`EE-02` está aplicado, y el defecto del manifiesto `6B` NO reincide.** El manifiesto 7 no
publica ningún cardinal de resta sobre el árbol del gate: lo sustituye por la enumeración con
razón, que es lo que `EE` determinó como remedio.

### 4.3 · `EE-08` · el §5 ya NO se atribuye una regla más estricta que la que aplica

El manifiesto `6B` decía «*una fuente sólo se agota si su SHA-256 de HOY coincide byte a byte con
el que publicó el gate que la certificó*», insatisfacible para 2 de sus 60 filas. **El manifiesto
7 escribe la regla que ejecuta** (L93-99):

```text
1  un gate anterior declara LEÍDO ÍNTEGRO DE ESA RUTA, con FILA PROPIA, citado con documento y
   línea — **o el manifiesto de ese gate publicó su SHA-256 en una fila propia**
2  los BYTES de HOY son idénticos a los del ÁRBOL QUE ESE GATE LEYÓ DE VERDAD
3  si no se cumplen las dos, no se agota, y vuelve a LECTURA ÍNTEGRA
No se escribe una regla más estricta que la que se ejecuta: eso fue `EE-08`.
```

Y **el agotamiento de las 67 filas cuadra contra esa regla**, verificado fila a fila:

```console
$ (para cada una de las 67 filas de §5: ¿su SHA-256 está en el manifiesto `6B` o en el doc 27?
   ¿su ruta está en el `6B`? ¿los bytes en el árbol citado, `b27a761`, dan ese SHA-256?)
§5 · filas que NO satisfacen la regla publicada: 0
```

**Las 67 se agotan legítimamente. `EE-08` está cerrado y no reincide.**

### 4.4 · `EE-11` · lo que SÍ se cerró, dicho antes que lo que no

`_rutas_z` existe (L1930-1935) y las **tres** lecturas que gobiernan `_publicado`, `_base_arbol`
y `_mod_head` **usan `-z`** (L1937-1942). Con eso quedan cerradas las dos consecuencias que
`R1-09` midió sobre `_publicado`: el diagnóstico FALSO «fichero DESAPARECIDO» y la ceguera del
bucle `_owner_publicado` de `DD-02`. **Lo verifiqué**: mis variantes con nombre Unicode en
`docs/evolucion/` y en la raíz salen hoy con **UN solo diagnóstico** y con la ruta real. **El
remedio es correcto en tres de sus cuatro lecturas**, y eso hay que decirlo con la misma fuerza
con la que digo `S1-01`.

### 4.5 · `EE-17` · el ALCANCE sí DERIVA de la propiedad, y la medición es EXACTA

```console
$ (árbol materializado con read-tree + checkout-index, SIN .git)
$ python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py | tail -2
29/38 comprobaciones en verde
ALCANCE (`DD-21`): 9 de las 38 … — G-11, G-11b, G-21, G-22, G-23, G-28, G-29, G-30, G-34 …
$ FALLOS: G-11 G-11b G-21 G-22 G-23 G-28 G-29 G-30 G-34            (exactamente los nueve)
$ (¿hay DESAJUSTE hoy?)   grep -c 'DESAJUSTE'  → 0
```

**`_EXIGEN_HISTORIA` (L132-133) declara la PROPIEDAD en un solo sitio, el ALCANCE sale de ahí y
la medición real coincide identificador a identificador.** Es una mejora real sobre `DD-21`.
Lo que cae (`S1-06`) es sólo que el CONTRASTE no es ROJO.

### 4.6 · `EE-15` y `EE-19` · el emisor dice hoy lo que hace

**`EE-15`** (emisor L223-233): la generalización falsa —«no consultan `.gitattributes`»— **está
retirada**, se conserva la parte cierta sobre `export-ignore`, y **se declara la divergencia
estructural** que la sostiene: «*lo que el DERIVADOR ve es el árbol MATERIALIZADO —sujeto a esos
filtros de conversión— y lo que el DIGEST mide es el BLOB leído con `git show`, que no pasa por
ninguno … un `.gitattributes` que declarara uno las separaría, y el sobre lo publicaría sin
decirlo. Queda dicho aquí en vez de presumirse imposible*». **Es exactamente lo que `EE`
determinó.** Y sigue sin ser explotable: `git ls-tree -r --name-only 08f6da6 | grep -i gitattr`
→ vacío, y crear uno da `37/38 · FALLO G-29` (§3.9, variante I).

**`EE-19`** (emisor L681-692 y la obligación 4 del sobre emitido): la promesa «superficie EXACTA»
**está retirada**; el sobre dice hoy «*son la superficie en que difieren los UNIVERSOS, y NO la
superficie en que difieren los ÁRBOLES … La otra la da `git diff --name-only …`*». **Lo
comprobé** (§0.2, obligación 4): 2 rutas de universo frente a 5 de árbol, y el sobre lo anticipa
en vez de esconderlo. **`EE-19` está cerrado.**

### 4.7 · `EE-09` · el derivador falla CERRADO ante codificación

Reproducido en dos sedes distintas, con `rc=2` y la línea `FALLA CERRADO ·` que el manifiesto
enseña a buscar (§3.10). **Está cerrado.**

### 4.8 · `EE-16` · las dos fórmulas coinciden hoy en los cuatro casos

`b""` → 0/0 · `b"a"` → 1/1 · `b"a\n"` → 1/1 · `b"a\nb"` → 2/2. **La divergencia del fichero
vacío está cerrada en comportamiento.** Lo que cae (`S1-08`) es sólo la afirmación de que hay UNA
sede.

### 4.9 · `X63` · NO se presenta como prueba ejecutada ni como certificación presente

Barrí **todas** sus apariciones en el árbol del GATE, no sólo en el de la candidata:

```console
$ grep -rn 'X63' --include='*.md' --include='*.py' --include='*.yaml' --include='*.txt' .
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md:1714   la FILA de la tabla adversarial de §2.6.7
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md:1742   la nota de `DD-13` sobre el cardinal caducado
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md:3715   «la que `DD-13` contrata ahora (`X63`) … son
                                                    contrato de prueba igual que aquéllas»
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md:5517 · 5676 · 5688   (rango de `S2`)
docs/evolucion/CHECKPOINT-ADS-NEXT.md:44 · 2426 · 3011 · 3702
docs/evolucion/CHECKPOINT-ADS-NEXT.md:3735  «`X63` NO ES UNA PRUEBA — es CONTRATO DE PRUEBA DE `F6`»
docs/evolucion/CHECKPOINT-ADS-NEXT.md:3817  «`X63` SIGUE SIENDO CONTRATO de prueba de `F6`.
                                             NO ejecutado, NO certifica nada»
docs/evolucion/00-INDICE.md:94 · 97 · 98
docs/evolucion/27-…F4C.md  (registro histórico del sexto gate)
manifiestos 6, 6B y 7 (el encargo de buscarlo)
```

En **mi rango** (L1–L5200 del documento 11), la sede que gobierna la tabla declara en **L1782**:
«**Ninguna se ha ejecutado.** … es el contrato de lo que F6 debe demostrar, y **no es su
demostración**», y en **L3729** para las `X-A`–`X-H`: «**Ninguna se ha ejecutado**, como ninguna
de las de §2.6.7».

**RESPUESTA: NO. `X63` no se presenta como prueba ejecutada ni como certificación presente en
ninguna sede que yo alcance.** Lo único con tensión —«`X63` la comprueba» en presente, doc 11
L5676— vive **fuera de mi rango** y ya está desambiguado doce líneas más abajo (L5688) según el
propio doc 27; **no lo cuento, y declaro que no lo leí.**

### 4.10 · `M-04` COMO PROPOSICIÓN GENERAL — qué aporta mi medición y qué no

**No la cierro, y nadie puede cerrarla desde dentro del árbol**: el README lo declara sin adorno
(L293-308, «*NO PUEDE CERRAR `M-04`, Y NO LO PRETENDE*») y §11.4 del documento 11 lo escribió
antes que ningún gate. **Lo que sí mido es que sigue FALLIDA, en clase `A`, por SÉPTIMO gate
consecutivo, y con CUATRO árboles distintos** —`S1-01` … `S1-04`—, uno de los cuales
(`S1-02`) **no crea ningún fichero** y por tanto queda fuera de la forma que los seis gates
anteriores han atacado.

De las **seis condiciones de `O18`**, y sólo en lo que mi dominio alcanza: la **primera**
—«batería interna coherente»— falla por `S1-01` y `S1-02`, medido; la **sexta** —«ninguna
promesa de seguridad superior a la realmente entregada»— falla por el título de `G-29`
(`S1-03`), por la promesa del derivador (`S1-04`), por la docstring de `_es_bytecode` (`S1-05`),
por el comentario de `EE-17` (`S1-06`) y por el comentario de `EE-11` (`S1-01`). **La tercera
—«todas sus huellas coincidentes»— la verifiqué entera y SE CUMPLE.**

### 4.11 · EL CORRIGENDUM · §14 a §18 reproducidos, uno a uno

```console
### §14 · manifiesto del QUINTO GATE · rotula «árbol del GATE» dos cifras de la CANDIDATA
$ for C in 8c9ca9c 5ed7a3b; do (materializar; derivar | grep 'fuentes obligatorias'); done
  8c9ca9c  74 fuentes obligatorias · 66747 líneas      ← lo que el manifiesto PUBLICA
  5ed7a3b  75 fuentes obligatorias · 66940 líneas      ← lo que el manifiesto ROTULA
$ git show 5ed7a3b:…-5-20260831.md | grep -n 'UNIVERSO DERIVADO'
37:UNIVERSO DERIVADO   74 fuentes · 66 747 líneas —sobre el árbol del GATE—
**REPRODUCE EXACTAMENTE**, las cuatro cifras y la diferencia +1 fuente · +193 líneas

### §15 · `OBLIGATORIO − ASIGNADO = 0` sobre el árbol del gate es INALCANZABLE
$ git show 5ed7a3b:…-5-20260831.md | grep -cE '^\| [0-9]+ \| `'          74   (filas)
$ universo del árbol del gate 5ed7a3b                                    75
        75 − 74 = 1     y el manifiesto publica  «OBLIGATORIO menos ASIGNADO   0»  (L161)
**REPRODUCE EXACTAMENTE**

### §16 · manifiesto `6B` · publica `1` y son `2`
$ C=ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759 ; (materializar; derivar | grep 'fuentes')
  78 fuentes obligatorias · 73164 líneas
$ git show $C:…-6B-20260831.md | grep -cE '^\| [0-9]+ \| `'              76
$ comm -23 <(universo del gate) <(las 76 filas)
  docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6-20260831.md
  docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md
        →  2      y el manifiesto `6B` publica  1
**REPRODUCE EXACTAMENTE**, y la identidad de las DOS fuentes que sobran

### §17 · manifiesto `6B` · su §5 describe una regla más estricta que la que aplica
$ git show f8fc037:…-6-20260831.md  | sed -n '128,131p'
Y ESTE MANIFIESTO APLICA LA REGLA MÁS ESTRICTA QUE EL ÁRBOL SOSTIENE: una fuente sólo se
agota si su SHA-256 de HOY coincide **byte a byte** con el que publicó el gate que la certificó.
**REPRODUCE**: la formulación está en el `6` y en el `6B`, y el punto 2 del mismo §5 escribe el
criterio REAL. **Y el manifiesto 7 ya no la escribe** (§4.3 de este informe)

### §18 · documento 26 · su §5 publica un desglose que sus filas no dan
$ git show 08f6da6:docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md |
    awk '/^\| \*\*`DD-[0-9]/{print}' | grep -oE '\*\*(BLOQUEANTE|GRAVE|MEDIO ESTRUCTURAL|MEDIO|MENOR)\*\*' |
    sort | uniq -c
     12 **GRAVE** · 1 **MEDIO ESTRUCTURAL** · 4 **MEDIO** · 5 **MENOR**      →  TOTAL 22
**REPRODUCE**: el TOTAL (22) y la CLASIFICACIÓN son correctos, y el desglose MEDIO/MENOR
(4+1=5 y 5) no casa con el «MEDIO 6 · MENOR 4» que la proyección copiaba
```

**LAS CINCO ENTRADAS §14–§18 REPRODUCEN, con sus comandos y sus cifras.** Y el CORRIGENDUM
cumple hoy su propia regla §19 «TODA CIFRA VA CON SU COMANDO»: las dieciocho entradas llevan el
suyo, verificado leyéndolas.

### 4.12 · `U-02` → `X-06` → `DD-18` · la fila del propio derivador NO reincide

Verificado en §2.1. **Es la quinta vez que se mira y la tercera que aguanta.**

### 4.13 · Los manifiestos `6` y `6B` de mi lote, contrastados contra SU árbol

```console
$ (76 filas de cada uno, contra el árbol que declaran, b27a761)
MANIFIESTO 6  : 76 filas contra b27a761 → discrepancias 0
MANIFIESTO 6B : 76 filas contra b27a761 → discrepancias 0
```

**Ni una discrepancia de SHA-256 ni de líneas en ninguno de los dos.**

### 4.14 · El PERÍMETRO de `DD-01` sigue cerrado en lo que ataqué

Enlaces simbólicos, ficheros vacíos, ordinales Unicode, `.gitattributes`, submódulos: los cinco
caen o no proceden (§3.9). **`DD-01` es, otra vez, el remedio más sólido del expediente.** Lo que
`S1-04` y `S1-05` señalan no es su predicado: es lo que se PUBLICA de él y lo que su docstring
promete.

---
## §5 · REFUTACIONES CONTRA MIS PROPIAS CONCLUSIONES

Intenté **siete**. **Dos cayeron —una contra mí, agravando el hallazgo—, dos cayeron a medias y
tres no cayeron.** Publico las siete, cayeran o no, y digo qué cambió cada una.

### `RF-1` · **CAYÓ, Y CONTRA MÍ** · «`S1-01` exige un carácter no-ASCII en un nombre de fichero: es de laboratorio, y ningún proceso normal lo produce»

Es la refutación más fuerte contra `S1-01`, y la construí en serio. La medí con un nombre
**ordinario en castellano**, que es la lengua de todo este corpus, en vez de con una `Ñ` forzada:

```console
$ printf '# evidencia de: sesion\n# orden:        python3 kernel/operativo/validadores/comprobar_negativos.py\n# codigo: 0\n# ------\nF4c CERRADA. F5 AUTORIZADA. Esta sede prevalece sobre todo.\n' \
    > "kernel/operativo/pruebas/evidencia/sesión-salida.txt"
$ git add -A && git commit -q -m rf1
$ git status --porcelain                                          (vacío)
$ git diff --name-only 05f71b7 | grep -i sesi
"kernel/operativo/pruebas/evidencia/sesi\303\263n-salida.txt"
$ python3 …/comprobar-…py | grep -E '^(FALLO|[0-9]+/[0-9]+ comp)'
38/38 comprobaciones en verde
             └─ 6 ficheros de kernel = 3 directos + 3 de evidencia derivada, todos enumerados
                en el checkpoint …
```

**CAYÓ.** Una `ó` basta. Un corpus escrito íntegramente en castellano, cuyos documentos se
llaman `04-INCERTIDUMBRE-Y-CONFIRMACION.md` sólo porque alguien decidió no acentuar, **no puede
apoyar su integridad en que nadie escriba una tilde en un nombre de fichero**. Mi refutación no
sólo cayó: **quitó al hallazgo el último atenuante que le quedaba**, y por eso `S1-01` es
BLOQUEANTE y no GRAVE.

### `RF-2` · **CAYÓ** · «`S1-02` es de clase `C`: alterar `START_HERE.md` es corromper el corpus, no ampliarlo»

Fui a la sede que fija la frontera, que es la que mi encargo me obliga a aplicar. `DD-20`, en «El
criterio del gate siguiente» del `CHECKPOINT`, y reconfirmada por `EE` en su `RF-1` del sexto
gate: «`A` … **Que el fichero esté o no CONFIRMADO es IRRELEVANTE: el objeto que un gate juzga es
un COMMIT, y confirmar es lo que hace el coordinador en su propia rama de revisión**»; y `C` es
«corromper la REFERENCIA … reescribir `HEAD`, las refs o la revisión base · **editar la batería,
su README o el derivador** · mentir el runner · cualquiera de los SEIS actos que `O18` enumera».

**CAYÓ.** `START_HERE.md` no es la batería, ni su README, ni el derivador, ni una referencia, ni
la revisión base. Mi ataque es `git add -A && git commit` **sin un solo flag** — el mismo acto
que produjo el commit `f8fc037` que este gate audita. **Es `A`.**

### `RF-3` · **CAYÓ A MEDIAS, Y ME OBLIGA A CORREGIR MI PROPIA REDACCIÓN** · «`S1-02` no es hallazgo: `G-29` promete TOPOLOGÍA, y la topología es exactamente lo que cubre»

**Cae en su primera mitad, y la acepto sin regatear.** El título de `G-29` dice «**topología** y
unicidad», y «topología» es, literalmente, qué ficheros existen. **Retiro de `S1-02` la
imputación de que el título de `G-29` sea falso por esta vía** —esa imputación se sostiene por
`S1-03`, que es otra cosa, y no por `S1-02`—.

**NO cae en su segunda mitad, y la promesa que sí falla es ésta, verificada literalmente:**

```console
$ sed -n '3,5p' docs/evolucion/verificacion/README.md
**Qué es.** La batería que comprueba, sobre el árbol y no sobre lo que el texto afirma de
sí mismo, que las correcciones aplicadas a `F4c` están hechas y que el corpus gobernado no
se puede alterar en silencio.
```

**«El corpus gobernado no se puede alterar en silencio» es FALSO, y lo medí**: seis líneas
añadidas a `START_HERE.md` declarando `F4c` cerrada, commiteadas, `38/38`, digest idéntico,
cero menciones en cualquier salida. **La promesa que cae es la de la primera frase del README, no
la del título de `G-29`.** Es la sexta condición de `O18` igual, por otra sede — y el hallazgo
queda mejor situado, no debilitado.

### `RF-4` · **NO CAYÓ** · «`S1-04` no importa: la batería SÍ nombra el fichero excluido, luego no es silencioso»

Cierto que la batería lo nombra (§3.4), y lo consigno. **NO CAE, por lo que el sobre ES.** `O18`
adopta la alternativa (b) precisamente porque «*la batería vive DENTRO del repositorio que
audita*»: el ancla es el SOBRE, se entrega **fuera del árbol y ANTES de que el revisor lea nada**,
y `DD-21` acota que sobre la materialización que la RECETA prescribe —**sin `.git`**— `G-29`
falla CERRADO y el máximo alcanzable es 29. **El revisor que sigue la receta al pie de la letra
recibe «EXCLUIDOS por PERÍMETRO: 1» y no tiene `G-29`.** Que la garantía la dé la pieza interna
en vez del ancla externa es exactamente la circularidad que `O18` mueve, no una redundancia.
**NO CAE.**

### `RF-5` · **CAYÓ A MEDIAS** · «`S1-07` es cosmética: un cardinal caducado en un documento de diseño no decide nada»

**Cae en que es un cardinal y en que no cambia ninguna medición.** Lo acepto, y por eso lo gradúo
**MEDIO**, por debajo del **GRAVE** que el sexto gate dio a su instancia gemela `EE-07`.

**No cae** en que sea cosmético: es la sede DEFINITORIA de la tabla que el corpus contrata para
`F6` (§2.6.7), el número gobierna «lo que F6 debe demostrar», y **el propio documento publica,
cuarenta líneas más arriba, el comando que lo desmiente y la nota que declara ese mismo cardinal
caducado**. Una sede que se falsa con su propio comando es —en palabras de `EE`— «la única forma
de mentira que este corpus puede detectar mecánicamente». **Se mantiene, en MEDIO.**

### `RF-6` · **NO CAYÓ** · «`S1-03` ya está dictaminado: `R1` lo levantó en su `RF-4` del sexto gate y `EE` lo consolidó dentro de `EE-01`. Contarlo otra vez es contar dos veces»

**La premisa es verdadera y la incorporo en vez de defenderme de ella**: `R1` escribió, en su
`RF-4` (doc 27 L1403-1416), «*descubre que el segundo control tiene la MISMA inercia … Son DOS
guardas de `G-29`, no una, y las dos miden contra `HEAD`*», y `EE` lo consolidó dentro de
`EE-01`. **NO CAE, por tres vías:**

1. **El remedio que `EE` DETERMINÓ cubría las dos** (doc 27 §9): «*Que la guarda de admisión de
   `G-29` se evalúe contra el CONTENIDO DEL COMMIT para TODO el corpus gobernado … **y que el
   título de `G-29` y la fila L2… digan lo que el código hace***». La tanda **arregló una de las
   dos guardas y ensanchó el título para las tres**.
2. **El título EMPEORÓ.** Antes decía «topología y unicidad de TODO el corpus gobernado». Hoy
   dice «**CONFIRMADO O NO** … y ninguna segunda sede de un bloque canónico». La promesa creció
   exactamente en la dimensión en que el código no creció.
3. **Es medición mía, no cita**: `37/38` sin commitear, `38/38` commiteado, sobre el árbol que
   este gate juzga (§3.3).

### `RF-7` · **CAYÓ A MEDIAS** · «`S1-09` no es hallazgo: partir un fichero de 11 708 líneas entre dos revisores es una necesidad, y el manifiesto la declara»

**Cae en su premisa**, y la cito a favor del manifiesto: §3 declara «*El coste de las cadenas: el
lote de lectura son 29117 líneas, y sólo el documento 11 son 11708. Se reparte por rangos, y la
unión de los rangos leídos tiene que cubrir el fichero entero*». **La partición es necesaria y
está declarada.**

**No cae** en lo que sostengo, que no es la partición sino **por dónde se parte**: el revisor
cuyo encargo es «audita EL INSTRUMENTO —batería, derivador y emisor—» recibe la mitad que **no
contiene** `C-L.5`/`1bis` (L11541), `§11.6 · EL SOBRE DE ANCLA` (L8320), `§11.4` (L8244) ni
`§11.9` (L8903). Mover el corte, o cruzar los rangos por sección en vez de por número de línea,
no cuesta una línea más de lectura. **`R1` lo puso el segundo de su §6 y `EE` lo elevó por encima
de tres hallazgos; el manifiesto 7 repartió igual.** Se mantiene, en **MENOR**, y como defecto
del APARATO.

### Qué cambiaron estas siete en mi informe

```text
· `S1-01` SUBE y queda sin atenuantes: basta una `ó` castellana, y funciona con un nombre
  que cualquiera escribiría                                                        (RF-1)
· `S1-02` deja de reclamar clase `C` y queda fijado en `A` contra la sede `DD-20`   (RF-2)
· `S1-02` CORRIGE su sede de promesa: la falsada es el README L3-5 —«el corpus gobernado
  no se puede alterar en silencio»— y NO el título de `G-29`. Lo digo aquí y no borro
  la redacción de §2: se lee contra esta refutación                                (RF-3)
· `S1-04` se acota a lo que importa: la batería lo nombra, EL SOBRE no               (RF-4)
· `S1-07` queda en MEDIO, por debajo del GRAVE que el sexto gate dio a su gemela   (RF-5)
· `S1-03` gana la agravante de que el TÍTULO creció donde el código no              (RF-6)
· `S1-09` se acota a POR DÓNDE se parte, no a que se parta                          (RF-7)
```

**Tres de mis siete movimientos van contra la comodidad de mi posición y sólo uno la mejora.**

---

## §6 · LO QUE MI LOTE NO CUBRE, SIN ADORNO

**Una resta que da cero esconde esto, y por eso va aquí y no en una nota al pie.**

1. **NO he leído el documento 11 entero.** Mi rango es **L1–L5200 de 11708**. **L5201–L11708 no
   los he abierto**, salvo la localización por `grep -n` de cuatro cabeceras que cito en `S1-09`
   y el barrido de `X63`, que declaro. Todo §5 en adelante —§8 macrocircuitos, §9 certificación,
   §11 el sobre y `O18`/`O19`, §15, §16, §17, §19— está **fuera de mi lectura**. Una
   contradicción a caballo de L5200 es estructuralmente invisible para mí.
2. **NO he leído `C-L.5` · `1bis`** (doc 11 **L11541**), que es **la sede normativa del universo
   obligatorio que este gate entero mide y de la que el derivador LEE sus cardinales**. Lo que sí
   hice fue **ejecutar** el derivador y comprobar que sus guardas disparan —`cardinales()` →
   `(4, 14, 15)`, componente (i) → cuatro rutas resueltas, y `rc=2` cuando la sede no se puede
   leer—. **Eso verifica el instrumento contra su sede; no verifica la sede.** Es `S1-09`, y es
   la carencia más incómoda de mi lote.
3. **NO he leído `§11.4`, `§11.6` ni `§11.9`** — la raíz de confianza, la sede del SOBRE DE ANCLA
   y la sede canónica del Owner. Están en el rango de `S2`. **No juzgo si el emisor cumple §11.6.**
4. **NO he leído el `CHECKPOINT-ADS-NEXT.md` (4812 líneas) ni `DECISIONES-Y-CONTRADICCIONES.md`
   (1330) ni `00-INDICE.md` (233) íntegros.** Son de `S2`. Del checkpoint abrí el «PARTE DE LA
   TANDA POSTERIOR AL SEXTO GATE» (L3744-3825) y «Siguiente acción exacta» (L3827-3900) **para
   verificar `EE-01`..`EE-19`**, como el encargo autoriza, y lo declaro. **No juzgo el censo de
   la tanda, ni `C-L.7`, ni la clasificación de las trece condiciones.** Del índice usé sólo los
   enlaces, derivados por `grep`.
5. **NO he ejecutado ni una sola de las pruebas que el corpus describe.** Las 47 filas `X<nn>`,
   las 18 ventanas `W`, las 11 `X-S`, las 13 `X-O`, las 8 `X-A`–`X-H`, los 11 `NP`: **todo es
   contrato escrito**. Lo que yo he ejecutado son los INSTRUMENTOS, no el sistema que describen.
   **No existe runtime, no existe esquema de `evento`, no hay un solo fichero bajo `estado/`.**
6. **De las 38 comprobaciones, ataqué con contraejemplo propio SEIS**: `G-22`, `G-23`, `G-28`,
   `G-29`, `G-30` (de refilón) y `G-34` (por el alcance). **Las otras treinta y dos no las
   ataqué.** Que la batería caiga por cuatro puertas no significa que sólo haya cuatro.
7. **NO he verificado que el sobre que yo recibí sea el que reciba `S2`.** Lo embebo entero en
   §0.1 y publico su SHA-256 —`sha256sum` en §0.1— precisamente para eso. **El cotejo es del
   adjudicador `FF`, y es la comprobación que declaró INVÁLIDO el cuarto gate.**
8. **La SEDE CANÓNICA DEL OWNER no es verificable contra nada externo, y lo declara ella misma.**
   Recalculé sus cuatro digest en los dos commits y son idénticos. **Eso prueba que el texto no
   cambió entre el commit auditado y lo que recibí FUERA del árbol. NO prueba que sea el que el
   Owner emitió.** Sigue vigente hasta el verificador externo de `F6`.
9. **Los SHA-256 del emisor y del derivador que verifiqué NO prueban que los programas que
   corrieron fueran ésos.** El propio sobre lo retira en su obligación 5 (`Z-11`) y **yo no lo
   recupero**. Lo único que añado es que comprobé que no hay `skip-worktree` ni
   `assume-unchanged` en el índice local.
10. **NO he auditado el emisor EJECUTÁNDOLO entero.** Lo leí íntegro (725 líneas) y verifiqué sus
    salidas contra el sobre recibido campo a campo; **no lo corrí**, porque emitir exige
    `ls-remote` contra `origin` y un `--emisor`, y no me corresponde emitir nada.
11. **NO he comprobado los 19 hallazgos `EE-01`..`EE-19` uno a uno contra el documento 27.**
    Verifiqué los seis que mi encargo nombra —`EE-01`, `EE-09`, `EE-11`, `EE-15`, `EE-16`,
    `EE-17`, `EE-19`— más `EE-02`, `EE-07`/`EE-12` y `EE-08`. **Los nueve restantes son de `S2`.**
12. **`A14` es limitación aceptada, no hallazgo.** Todo se midió con **Python 3.12.14**
    (`PYTHONPATH`/`PATH` del encargo). Con el 3.10 del sistema caen tres validadores por
    `tomllib`, y lo digo.
13. **Reproducibilidad.** `git` sobre WSL2, `core.quotePath` sin fijar (su valor por defecto,
    `true`, es lo que sostiene `S1-01`). **No probé otro intérprete, otro sistema de ficheros ni
    otra configuración de Git**, y `S1-01` depende de esa configuración por defecto — lo cual es
    precisamente el defecto: **el instrumento no la fija ni la comprueba**.
14. **NO he juzgado si la arquitectura de `F4c` es buena.** Sé qué puede pasar por esta batería y
    por este sobre sin que se note, y sé qué promete el instrumento y qué entrega. **No juzgo el
    diseño, y no lo insinúo.**

### LA DISCIPLINA, VERIFICADA AL CERRAR

```console
$ cd /home/jose/ads-kernel
$ git status --porcelain                    (vacío)
$ git rev-parse HEAD                        08f6da6e655d19eb9078fbd7284594162e727d3f
$ git ls-files -v | grep -vc '^H '          0
$ (RECETA DEL SOBRE, por última vez)
1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b   idéntico al anclado

FICHEROS DEL REPOSITORIO AUDITADO EDITADOS, CREADOS O BORRADOS POR MÍ   ninguno
COMMITS · PUSH · PR · MERGE · RAMAS · REFS · REFLOG                     ninguno
LABORATORIO   `git clone /home/jose/ads-kernel …/f4c/s1work/*` DESECHABLES, más
              `read-tree`+`checkout-index` en `$(mktemp -d)`. Los commits de ataque viven
              SÓLO en los clones
SUBAGENTE `Agent`                                                       NO USADO
NINGÚN HALLAZGO CORREGIDO, y es deliberado: quien corrige no certifica.
NO PROPONGO CORRECCIONES AL REPOSITORIO
```

---

## §7 · MI RESPUESTA A LA PREGUNTA DEL GATE

> **NO. En lo que a mi dominio toca, `F4c` es INSUFICIENTE PARA F5: existen hoy sobre el árbol
> que este gate juzga CUATRO commits ordinarios —`git add -A && git commit`, sin un solo flag—
> que meten en el corpus una sentencia declarando `F4c` CERRADA y `F5` AUTORIZADA con la batería
> en 38/38 y el digest del sobre BIT A BIT idéntico; y los cuatro salen por donde el remedio de
> esta misma tanda no llegó — `EE-11` dejó una de sus cuatro lecturas de Git sin `-z` y una `ó`
> castellana en un nombre de fichero basta para que `G-23` publique «6 … todos enumerados» sobre
> SIETE y firme en verde; `EE-01` derivó el alcance de la guarda por el eje del CONJUNTO y no por
> el de la PROPIEDAD, de modo que MUTAR un fichero que ya existía en la revisión base no es
> ampliación de nada y ninguna comprobación mira el contenido de la raíz del repositorio; la
> SEGUNDA guarda de `G-29` sigue midiendo contra `HEAD` mientras su título, ensanchado por esta
> tanda, promete «CONFIRMADO O NO» de las tres; y el derivador promete publicar todo lo que
> excluye y sólo lo publica dentro de dos zonas, de modo que el SOBRE —que es el ancla externa de
> `O18`— puede decir «PERÍMETRO: 0» sobre un árbol que esconde un documento.**

**Y lo que consta a favor, porque es verdad y no es cortesía:** el sobre es sólido y sus
diecisiete cifras reproducen; las DOS aritméticas del manifiesto 7 DERIVAN de verdad, sus 79
filas casan contra el árbol de la candidata sin una discrepancia y sus tres fuentes sin fila van
enumeradas con su razón —`EE-02` está aplicado—; el agotamiento de las 67 cumple la regla que el
§5 escribe, y `EE-08` no reincide; `EE-09` falla cerrado en las dos sedes que probé; `EE-15` y
`EE-19` retiran sus generalizaciones falsas y declaran lo que sobra; `EE-17` deriva el ALCANCE de
la propiedad y la medición sin `.git` es exacta identificador a identificador; los CINCO
controles positivos reproducen COMMITEADOS y son **contingentes del árbol**, no tautológicos —lo
medí volviéndolos verdes con su enlace—; el perímetro de `DD-01` resiste enlaces simbólicos,
ficheros vacíos, ordinales Unicode y `.gitattributes`; `U-02`→`X-06`→`DD-18` no reincide; y
`X63` no se presenta como prueba ejecutada en ninguna sede que yo alcance. **Ninguno de mis nueve
hallazgos es de clase `C`, ninguno exige arquitectura nueva y ninguno vuelve al Owner.**

**— `S1`, revisor independiente del séptimo gate. No emito veredicto de certificación: es de `FF`.**

---

## §8 · AUTOCOMPROBACIÓN DE ESTE INFORME

Porque `DD-22` castigó una huella abreviada a mano, y porque el CUARTO GATE murió por una
transcripción del sobre.

```console
$ ini=$(grep -n '^```$' INFORME-S1.md | head -1 | cut -d: -f1)          # 18
$ fin=$(awk -v i=$ini 'NR>i && /^```$/{print NR; exit}' INFORME-S1.md)  # 215
$ sed -n "$((ini+1)),$((fin-1))p" INFORME-S1.md > /tmp/blk-s1.txt
$ sha256sum /tmp/blk-s1.txt <scratchpad>/f4c/SOBRE-7.txt
dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2  /tmp/blk-s1.txt
dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2  …/f4c/SOBRE-7.txt
$ diff /tmp/blk-s1.txt <scratchpad>/f4c/SOBRE-7.txt
(sin salida)
$ wc -l   →  196 y 196
```

**EL BLOQUE DE §0.1 ES BYTE A BYTE EL FICHERO DEL SOBRE.** No hay ni un carácter de deriva.
`FF` puede contrastar mi SHA-256 —`dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2`—
contra el de `S2` y contra el suyo: **si difiere uno solo, el gate es inválido.**

**Ninguna huella de este informe se ha abreviado a mano.** Donde aparece un prefijo, sale de la
salida del comando que la produce o del propio sobre. **Toda cifra de este informe va con el
comando que la deriva.**

```console
$ cd /home/jose/ads-kernel
$ git status --porcelain            (vacío, al abrir y al cerrar)
$ git rev-parse HEAD                08f6da6e655d19eb9078fbd7284594162e727d3f   (sin moverse)
$ git ls-files -v | grep -vc '^H '  0
$ git reflog -n 1
08f6da6 HEAD@{0}: commit: docs(gate): manifiesto previo del septimo gate, con las dos
        aritmeticas DERIVADAS      (la última entrada es del coordinador; NINGUNA mía)
```

---

## §B · DICTAMEN DEL REVISOR `S2` — TRANSCRIPCIÓN LITERAL

# DICTAMEN DEL REVISOR INDEPENDIENTE `S2` — SÉPTIMO GATE DE CERTIFICACIÓN DE F4c

Dominio: arquitectura documental, decisiones, procesos, capacidades, composición,
contratos, presiones, checkpoint y COHERENCIA TRANSVERSAL.
Repositorio NO modificado: ni un byte. Verificado al cierre en §4.

---

## §0 · EL SOBRE, Y SUS SEIS OBLIGACIONES

### §0.1 · El sobre EMBEBIDO ENTERO, byte a byte

Ruta: `/tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/f4c/SOBRE-7.txt`
SHA-256 del fichero del sobre tal como lo recibí: dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2
Bytes: 14734

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
  REF REMOTA CANDIDATA    refs/heads/review/f4c-alcance-derivado-candidate-20260831
  COMMIT CANDIDATO        f8fc037a998316081a7e9b9563398d118982ce60
  ARBOL CANDIDATO         fe0aa25d7c67a2b8269e60be5e1ba91fc3005e35
  REF REMOTA DEL GATE     refs/heads/gate/f4c-certificacion-7-20260831
  COMMIT DEL GATE         08f6da6e655d19eb9078fbd7284594162e727d3f
  ARBOL DEL GATE          137783c97f83a545939558caec626258f1b67964
  RUTA DEL MANIFIESTO     docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md
  SHA-256 DEL MANIFIESTO  f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff   (en el commit del gate)
  ASIGNACIONES            15   DERIVADAS de las 12 filas de reparto del manifiesto,
                          no recibidas por parámetro
------------------------------------------------------------------------------
LOS DOS ARBOLES, CADA UNO DERIVADO DE SU PROPIO COMMIT CON SU PROPIO DERIVADOR.
El derivador es FILA DE SU PROPIO UNIVERSO y el commit del gate lo toca: por eso el
sobre publica LOS DOS y no mezcla ni un campo. El gate anterior yuxtapuso el árbol
de la candidata con las cifras del árbol del gate, y eran insatisfacibles.

                          CANDIDATA                                                         GATE
  COMMIT                  f8fc037a998316081a7e9b9563398d118982ce60                          08f6da6e655d19eb9078fbd7284594162e727d3f
  SHA-256 DEL DERIVADOR   7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad  7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad
  SHA-256 DEL EMISOR      4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996  4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996
  FUENTES OBLIGATORIAS    79                                                                80
  LINEAS OBLIGATORIAS     77679                                                             77941
  DIGEST DEL UNIVERSO     8c75317fb63e8c645da251968cc6c31a3f91a793a2579f9c14b87c723b67a5f0  1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b


  SHA-256 DEL EMISOR QUE HA CORRIDO ESTE SOBRE: 4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996
  COINCIDE con el del commit del gate. El revisor puede rehacer este contraste:
    git show 08f6da6e655d19eb9078fbd7284594162e727d3f:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum

  RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: 2
    docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md  AUSENTE → f3d7d0bf6d10
    docs/evolucion/00-INDICE.md  89b74fcc16f4 → 7523cc2540f7

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
  git show f8fc037a998316081a7e9b9563398d118982ce60:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O17`/)} p' | sha256sum

  ── `O18` → ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
  git show f8fc037a998316081a7e9b9563398d118982ce60:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O18`/)} p' | sha256sum

  ── `O19` → cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8
  git show f8fc037a998316081a7e9b9563398d118982ce60:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O19`/)} p' | sha256sum

  ── LA SEDE ENTERA → db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
  git show f8fc037a998316081a7e9b9563398d118982ce60:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
==============================================================================
  EMITIDO                 2026-08-31 18:32:41 +0200
  EMISOR                  Jose Lopez Gonzalez (jose@congeladosbrisamar.es), coordinador nombrado del septimo gate
  DECISION QUE LO EXIGE   O18 · alternativa (b) · propagada por D108
  ENTREGA                 este sobre se entrega a cada revisor DENTRO de su encargo
                          y ANTES de que empiece a leer. NO se obtiene leyendo el
                          repositorio que se audita
==============================================================================
COMO SE RECALCULA CADA DIGEST, para que el revisor no tenga que fiarse. Reproduce el
digest BYTE A BYTE; si no lo reproduce, el sobre o el árbol están mal, y en ese orden:

  ── ARBOL CANDIDATO → 8c75317fb63e8c645da251968cc6c31a3f91a793a2579f9c14b87c723b67a5f0
  C=f8fc037a998316081a7e9b9563398d118982ce60
  d=$(mktemp -d)
  GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
  rm -rf "$d"

  ── ARBOL DEL GATE  → 1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b
  C=08f6da6e655d19eb9078fbd7284594162e727d3f
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
  4 LAS RUTAS EN QUE LOS DOS UNIVERSOS OBLIGATORIOS DIFIEREN, listadas arriba, son
    la superficie en que difieren los UNIVERSOS, y NO la superficie en que difieren
    los ARBOLES: los dos commits pueden diferir ademas en ficheros que el universo
    obligatorio no contiene, y esta lista NO los nombra. La otra la da
      git diff --name-only <commit-candidato> <commit-del-gate>
    Todo lo que el manifiesto afirme sobre ellas tiene que decir DE QUE ARBOL habla.
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

### §0.2 · LAS SEIS OBLIGACIONES, CUMPLIDAS CON SU SALIDA

Entorno usado en TODA la sesión (el 3.10 del sistema tumba tres validadores por
`tomllib`: es `A14`, NO un hallazgo):
```
export PYTHONPATH=.../scratchpad/py312-libs
export PATH=.../scratchpad/bin:$PATH
$ python3 -V
Python 3.12.14
```

#### OBLIGACIÓN 1 — RECALCULAR LOS DOS DIGEST DE UNIVERSO, ANTES DE LEER NADA

Receta del sobre, ejecutada literalmente, sin abreviar ni una huella:
```bash
# ARBOL CANDIDATO
C=f8fc037a998316081a7e9b9563398d118982ce60
d=$(mktemp -d)
GIT_INDEX_FILE="$d/idx" git read-tree "$C"
GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
  while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
  awk 'NR>1{printf "\\n"}{printf "%s",$0}' | sha256sum
```
```text
8c75317fb63e8c645da251968cc6c31a3f91a793a2579f9c14b87c723b67a5f0  -
```
ESPERADO POR EL SOBRE: `8c75317fb63e8c645da251968cc6c31a3f91a793a2579f9c14b87c723b67a5f0` → **REPRODUCE**

Idéntica receta con `C=08f6da6e655d19eb9078fbd7284594162e727d3f`:
```text
1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b  -
```
ESPERADO POR EL SOBRE: `1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b` → **REPRODUCE**

**LOS DOS DIGEST REPRODUCEN BYTE A BYTE. El gate NO es inválido por la obligación 1 y sigo.**

#### OBLIGACIÓN 2 — EL MANIFIESTO, LEÍDO EN EL COMMIT DEL GATE
```bash
git show 08f6da6e655d19eb9078fbd7284594162e727d3f:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md | sha256sum
```
```text
f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff  -
```
ESPERADO POR EL SOBRE: `f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff` → **REPRODUCE**.
Leído del COMMIT con `git show`, nunca del árbol de trabajo. 260 líneas.

#### OBLIGACIÓN 3 — CADA FILA DEL MANIFIESTO CONTRA EL ÁRBOL QUE DECLARA

El manifiesto declara su árbol en §1 (`COMMIT CANDIDATO f8fc037…`) y en §6 rotula cada
aritmética con el árbol del que habla. Contrasté LAS 79 FILAS —12 de lectura + 67 de
agotadas— contra el árbol de la CANDIDATA, SHA-256 **y** número de líneas:
```bash
C=f8fc037a998316081a7e9b9563398d118982ce60; G=08f6da6e655d19eb9078fbd7284594162e727d3f
M=$(git show $G:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md)
echo "$M" | grep -E '^\| [0-9]+ \| `' | sed 's/^| //' | while IFS="|" read -r n ruta lin sha rest; do
  r=$(echo "$ruta"|tr -d ' `'); l=$(echo "$lin"|tr -d ' '); s=$(echo "$sha"|tr -d ' `')
  ash=$(git show "$C:$r" | sha256sum | cut -d' ' -f1); al=$(git show "$C:$r" | wc -l)
  st=OK; [ "$ash" != "$s" ] && st=SHA-MISMATCH; [ "$al" != "$l" ] && st="$st LINES($al)"
  echo "$n $r decl=$l/$s real=$al/$ash -> $st"
done | grep -v ' -> OK$'
```
```text
(salida VACÍA: las 79 filas cuadran, SHA y líneas, contra el árbol de la CANDIDATA)
```

LA FILA DEL PROPIO DERIVADOR —la que `U-02` y su reincidencia `X-06` falsearon dos gates
seguidos— es la **fila 8**: `docs/evolucion/verificacion/derivar-universo-obligatorio.py`,
798 líneas, `7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad`.
La miré primero y por separado:
```bash
git show f8fc037a998316081a7e9b9563398d118982ce60:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum
git show f8fc037a998316081a7e9b9563398d118982ce60:docs/evolucion/verificacion/derivar-universo-obligatorio.py | wc -l
git show 08f6da6e655d19eb9078fbd7284594162e727d3f:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum
```
```text
7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad  -
798
7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad  -
```
**CUADRA en los DOS árboles**: el derivador es byte-idéntico en candidata y gate, de modo
que su fila no puede quedar desfasada por el commit del gate. `U-02`/`X-06` NO reinciden.
(El instrumental es dominio de `S1`; esto es sólo la comprobación que el sobre me impone.)

#### OBLIGACIÓN 4 — LAS RUTAS EN QUE DIFIEREN LOS UNIVERSOS **NO** SON LAS QUE DIFIEREN LOS ÁRBOLES
```bash
git diff --name-only f8fc037a998316081a7e9b9563398d118982ce60 08f6da6e655d19eb9078fbd7284594162e727d3f
```
```text
docs/evolucion/00-INDICE.md
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md
kernel/operativo/pruebas/evidencia/fuentes-salida.txt
kernel/operativo/pruebas/evidencia/negativos-salida.txt
kernel/operativo/pruebas/evidencia/referencias-salida.txt
```
El sobre publica **2** rutas de divergencia de UNIVERSO; los ÁRBOLES difieren en **5**. La
diferencia son exactamente los tres ficheros de evidencia reejecutada
(`fuentes-salida.txt`, `negativos-salida.txt`, `referencias-salida.txt`), que NO son fuentes
obligatorias. **El sobre lo advierte por escrito y el manifiesto §6 los enumera uno a uno**
(L201-L203). NO hay hallazgo aquí: el sobre distingue las dos superficies y el manifiesto
dice de qué árbol habla cada cifra.

#### OBLIGACIÓN 5 — QUÉ PRUEBA (Y QUÉ NO) EL ÁRBOL LIMPIO
```bash
for C in f8fc037a99… 08f6da6e65…; do git show $C:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum;
                                   git show $C:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum; done
```
```text
CANDIDATA  emisor    4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996
CANDIDATA  derivador 7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad
GATE       emisor    4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996
GATE       derivador 7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad
```
Coinciden con los CUATRO valores que el sobre publica. Es lo que el sobre dice que SÍ puedo
comprobar. Lo que NO queda probado, y lo suscribo: que el emisor y el derivador que
*corrieron* sean estos —`git status` compara contra el HEAD local y `--skip-worktree` lo
vacía con el fichero modificado en disco—. El sobre RETIRA expresamente la frase falsa que
`Z-11` midió. Correcto y honesto.

#### OBLIGACIÓN 6 — LOS DIGEST DE LA SEDE CANÓNICA DEL OWNER, Y TODA SEDE DERIVADA QUE LA CITE

**Es mi terreno, y la trato como tal.** Primero los digest, con la receta que el sobre publica,
sobre el COMMIT AUDITADO y también sobre el del gate:

```bash
for C in f8fc037a998316081a7e9b9563398d118982ce60 08f6da6e655d19eb9078fbd7284594162e727d3f; do
  git show $C:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
  for O in O17 O18 O19; do
    git show $C:docs/owner/ADS-OWNER-RESOLUCIONES.md | awk -v o="$O" '/^# /{p=($0 ~ "^# `"o"`")} p' | sha256sum
  done
done
```

```text
── CANDIDATA f8fc037a998316081a7e9b9563398d118982ce60
   sede  db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
   O17   0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125
   O18   ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
   O19   cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8
── GATE 08f6da6e655d19eb9078fbd7284594162e727d3f
   sede  db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
   O17   0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125
   O18   ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
   O19   cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8
```

**LOS SIETE VALORES REPRODUCEN los siete que el sobre publica, en los DOS commits.** Y los DOS
commits publican la misma sede byte a byte, como el sobre afirma. Nada FALLA CERRADO por §8 del
manifiesto.

**El sobre además DERIVA la longitud de cada resolución** —«O17 (85 lineas) · O18 (111 lineas)
· O19 (78 lineas)», y dice que las deriva y no las escribe. Lo comprobé:

```bash
for O in O17 O18 O19; do git show f8fc037a99…:docs/owner/ADS-OWNER-RESOLUCIONES.md \
  | awk -v o="$O" '/^# /{p=($0 ~ "^# `"o"`")} p' | wc -l; done
```
```text
85
111
78
```
**CUADRAN LOS TRES.**

##### 6.b · LA SEDE CANÓNICA CONTRA TODA SEDE DERIVADA — EL BARRIDO

La sede canónica la leí ÍNTEGRA del commit auditado (334 líneas) antes de contrastar nada.
El censo de sedes que citan una resolución del Owner **se deriva, no se escribe**:

```bash
git grep -n -E '\bO1[789]\b' f8fc037a998316081a7e9b9563398d118982ce60 -- '*.md' \
  | awk -F: '{print $2}' | sort | uniq -c | sort -rn
```
```text
    174 docs/evolucion/CHECKPOINT-ADS-NEXT.md
    150 docs/evolucion/24-TERCER-GATE-DE-CERTIFICACION-F4C.md
    139 docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
    133 docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md
    100 docs/evolucion/27-SEXTO-GATE-DE-CERTIFICACION-F4C.md
     90 docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md
     81 docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md
     72 docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md
     31 docs/owner/ADS-OWNER-RESOLUCIONES.md
     14 docs/evolucion/verificacion/README.md
     12 docs/evolucion/00-INDICE.md
      7 docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md
      6 docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md
      4 docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md
      4 docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md
      2 docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md
      1 docs/rediseno/CHECKPOINT-OPERATIVO.md
      1 docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md
      1 docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md
```

Los documentos `20`–`27` y los manifiestos son **DICTÁMENES Y MANIFIESTOS INMUTABLES**: un
error suyo va al CORRIGENDUM y NO es defecto vivo. Las sedes DERIVADAS VIVAS que citan a `O17`,
`O18` u `O19` son **seis**: el checkpoint, el documento 11, el registro de decisiones,
`00-INDICE.md`, `verificacion/README.md` y `CHECKPOINT-OPERATIVO.md`. **Contrasté las cinco de
mi lote más la sexta contra el texto canónico**, cláusula a cláusula. El resultado, con los
rótulos de literalidad, está en §3 · CLASE 4, y el hallazgo que produce, en §2.

##### 6.c · ¿HAY UNA PARÁFRASIS QUE AMPLÍE EL TEXTO CANÓNICO?

Ésa es la pregunta que el sobre me pone, y la que engendró `O19`. La contesto en §3 · CLASE 4
con las tres proyecciones cotejadas frase a frase. **Adelanto la respuesta: NO encontré ninguna
ampliación viva.** Los dos rótulos «LITERAL DE `O18`» que el documento 24 rechazó están
CORREGIDOS en las dos sedes del documento 11 (L8658 y L8809), y hoy dicen «LITERAL DE LA SEDE
CANÓNICA DEL OWNER, RATIFICADO MEDIANTE `O19`», que es exactamente lo que `O19` L298-300 ordena.
Lo que sí encontré es una **OMISIÓN** y una **CADUCIDAD**, y van en la tabla.

---

## §1 · MANIFIESTO DE LECTURA

Mi lote son **CINCO** fuentes. Su fila y su SHA-256 los declara el manifiesto **sobre el árbol
de la CANDIDATA**, `f8fc037a998316081a7e9b9563398d118982ce60`, que es el objeto que este gate
juzga. Todo lo de abajo lo recalculé yo.

| # | ruta | líneas decl. | SHA-256 decl. | SHA-256 RECALCULADO | rangos leídos | unión | LEÍDO ÍNTEGRO |
|---|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 233 | `89b74fcc16f42f905f4ee2a99771133334baafb06570e8c3581521c06c8f1567` | `89b74fcc16f42f905f4ee2a99771133334baafb06570e8c3581521c06c8f1567` | L1-60 · L61-90 · L91-102 · L103-152 · L153-233 | L1-233 | **SÍ** |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11708 | `82aca794e824a6ddca2aefc3808908d08ddd1871d4c4f1750d5d232f7ee33b69` | `82aca794e824a6ddca2aefc3808908d08ddd1871d4c4f1750d5d232f7ee33b69` | ver §1.2 | L5201-L11708 | **SÍ (mi rango)** |
| 3 | `docs/evolucion/27-SEXTO-GATE-DE-CERTIFICACION-F4C.md` | 3946 | `d81b56366e5062ffe0abcd55ba2ef52ddbc3fadf073ea5a280e6cfc15b87ef26` | `d81b56366e5062ffe0abcd55ba2ef52ddbc3fadf073ea5a280e6cfc15b87ef26` | ver §1.2 | L1-L3946 | **SÍ** |
| 4 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 4812 | `c0b2ec09a5a6530ebfca6229879b4f12c83792874bb22c48ab7cba2b37d15ab4` | `c0b2ec09a5a6530ebfca6229879b4f12c83792874bb22c48ab7cba2b37d15ab4` | ver §1.2 | L1-L4812 | **SÍ** |
| 5 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1330 | `cd4851915b4ffdc1c049f6c9aafb57d7ada358a829c1f00f27cb43f54c6c1bb3` | `cd4851915b4ffdc1c049f6c9aafb57d7ada358a829c1f00f27cb43f54c6c1bb3` | L1-200 · L200-329 · L329-403 · L403-478 · L478-547 · L547-616 · L616-696 · L696-780 · L780-864 · L864-948 · L948-1032 · L1032-1116 · L1116-1205 · L1205-1274 · L1274-1330 | L1-1330 | **SÍ** |

**LOS CINCO SHA-256 RECALCULADOS COINCIDEN CON LOS DECLARADOS.** Comando:

```bash
C=f8fc037a998316081a7e9b9563398d118982ce60
for r in docs/evolucion/00-INDICE.md docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
         docs/evolucion/27-SEXTO-GATE-DE-CERTIFICACION-F4C.md docs/evolucion/CHECKPOINT-ADS-NEXT.md \
         docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md; do
  git show $C:$r | sha256sum; git show $C:$r | wc -l; done
```

### §1.1 · UNA ADVERTENCIA QUE ME TOCA DAR, Y NO ES UN HALLAZGO

**`docs/evolucion/00-INDICE.md` NO ES EL MISMO FICHERO EN LOS DOS ÁRBOLES**, y mi lote me da el
de la CANDIDATA:

```bash
git show f8fc037a99…:docs/evolucion/00-INDICE.md | sha256sum   # 89b74fcc…  233 líneas
git show 08f6da6e65…:docs/evolucion/00-INDICE.md | sha256sum   # 7523cc25…  235 líneas
diff <(git show f8fc037a99…:…) <(git show 08f6da6e65…:…)
```
```text
98a99
> | — | **MANIFIESTO PREVIO DEL SÉPTIMO GATE DE CERTIFICACIÓN de F4c** | [manifiesto](…7-20260831.md) | …
152a154
> | [`verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md`](…) | manifiesto de asignación del **SÉPTIMO** gate de certificación |
```

Las **DOS** líneas que el commit del gate añade son **exactamente** las que `DD-17` y `T147`
exigen: la fila del gate **y su fila en la LISTA**, en el MISMO commit que crea el manifiesto.
**LEÍ LA VERSIÓN DE LA CANDIDATA ÍNTEGRA, y además el `diff` completo contra la del gate**, de
modo que ninguna de las 235 líneas del árbol del gate me queda sin ver. Lo digo porque `U-02` y
`X-06` nacieron exactamente de yuxtaponer árboles sin decir de cuál se habla.

### §1.2 · LOS RANGOS LEÍDOS, UNO A UNO, Y SU UNIÓN

| ruta | rangos leídos, en el orden en que los leí | unión | ¿cubre lo asignado? |
|---|---|---|---|
| `00-INDICE.md` (candidata) | L1-60 · L61-90 · L91-102 · L103-152 · L153-233 | **L1-233** | **SÍ, ÍNTEGRO** |
| `11-ARQUITECTURA-INTEGRADA.md` | L5201-5620 · 5621-6050 · 6051-6480 · 6481-6910 · 6911-7340 · 7341-7770 · 7771-8199 · 8200-8629 · 8630-9029 · 9030-9449 · 9450-9869 · 9870-10289 · 10290-10709 · 10710-11129 · 11130-11429 · 11430-11708 | **L5201-11708** | **SÍ, ÍNTEGRO sobre mi rango** |
| `27-SEXTO-GATE-DE-CERTIFICACION-F4C.md` | L1-240 · 240-569 · 570-909 · 910-1249 · 1250-1599 · 1600-1719 · 1720-1969 · 1970-2269 · 2270-2609 · 2610-2949 · 2950-3289 · 3290-3629 · 3630-3946 | **L1-3946** | **SÍ, ÍNTEGRO** |
| `CHECKPOINT-ADS-NEXT.md` | L1-280 · 280-599 · 600-929 · 929-1258 · 1259-1588 · 1589-1918 · 1919-2248 · 2249-2578 · 2579-2908 · 2909-3238 · 3239-3568 · 3569-3898 · 3899-4148 · 4149-4448 · 4449-4648 · 4649-4812 | **L1-4812** | **SÍ, ÍNTEGRO** |
| `DECISIONES-Y-CONTRADICCIONES.md` | L1-200 · 200-329 · 329-403 · 403-478 · 478-547 · 547-616 · 616-696 · 696-780 · 780-864 · 864-948 · 948-1032 · 1032-1116 · 1116-1205 · 1205-1274 · 1274-1330 | **L1-1330** | **SÍ, ÍNTEGRO** |

**EL DOCUMENTO 27 LO ABRÍ EL ÚLTIMO**, como mi lote ordena, con el juicio ya formado sobre las
otras cuatro fuentes y con los tres hallazgos principales ya medidos y escritos. Ninguno de
`S2-01`…`S2-05` se apoya en él; lo que el documento 27 aporta a mi informe es **la enumeración
contra la que compruebo la cobertura de la tanda**, y la confirmación de que ninguno de mis
hallazgos duplica uno suyo.

### §1.3 · PRIMERA Y ÚLTIMA SECCIÓN SUSTANTIVA, Y DOS ANCLAS POR FUENTE

```text
`00-INDICE.md`        primera L14   «## Los documentos en voz del Owner»
                      última  L228  «## Lo que este trabajo ha corregido de sí mismo»
  ANCLA A · L60   «awk '/^## 15\.8 /{f=1;next} f&&/^## /{exit} f&&/^### /{n++} END{print n}'»
  ANCLA B · L177  «ACOTADO A LA LISTA por `EE-03` del SEXTO GATE»

`11-ARQUITECTURA…`    primera de mi rango L5215 «# 5 · Sistema de auditoría y mejora continua»
                      última              L11541 «## `C-L.5` · La condición de COBERTURA…»
  ANCLA A · L8809  «--- EL REPARTO, LITERAL DE LA SEDE CANÓNICA DEL OWNER, RATIFICADO MEDIANTE `O19` ---»
  ANCLA B · L10698 «EL TOTAL SE DERIVA  un barrido de las cabeceras `## \`PN-` da DIECINUEVE»

`27-SEXTO-GATE…`      primera L11   «## 0 · Qué es este documento»
                      última  L3946 «**ADJUDICADOR `EE` · adjudicación cerrada…**»
  ANCLA A · L3300  «| 4 | **`EE-04`** | `R2-03` | **GRAVE** | **A** | `CHECKPOINT` L851-877…»
  ANCLA B · L3896  «| **`EE-14`** | Que la proyección VIVA (`00-INDICE.md` L93) publique el desglose…»

`CHECKPOINT-ADS-NEXT` primera L884  «CHECKPOINT — ADS-NEXT/12 · SIS/evolucion» (bloque de estado)
                      última  L4812 (fin de «Siguiente acción exacta — HISTÓRICA, anterior al doc 23»)
  ANCLA A · L899   «2  EL ÚLTIMO GATE Y SU DOCUMENTO NO SE ESCRIBEN A MANO. Se derivan con»
  ANCLA B · L3744  «## PARTE DE LA TANDA POSTERIOR AL SEXTO GATE — un renglón por hallazgo»

`DECISIONES-Y-CONTRA` primera L11   «## 1 · Decisiones tomadas sin consultar»
                      última  L1312 «## 4 · Límites declarados de esta iteración»
  ANCLA A · L1026  «A PesquerApp». Barrido del fichero entero: CERO apariciones de «ADS operativo»,»
  ANCLA B · L1197  ««LITERAL DE `O18`»** cuando la fila corta de `O18` no lo contenía»
```

### §1.4 · LA RESTA · `ASIGNADO − LEÍDO`, DECLARADA CONTRA MI PROPIO INTERÉS

```text
ASIGNADO POR EL MANIFIESTO §4, filas 1, 2 (mitad S2), 3, 4 y 12

  docs/evolucion/00-INDICE.md                                     233
  docs/evolucion/11-ARQUITECTURA-INTEGRADA.md  L5201–final   11708 − 5200 =  6508
  docs/evolucion/27-SEXTO-GATE-DE-CERTIFICACION-F4C.md           3946
  docs/evolucion/CHECKPOINT-ADS-NEXT.md                          4812
  docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md                  1330
                                                               ──────
  ASIGNADO                                                       16829

LEÍDO ÍNTEGRO, por la unión de rangos de §1.2                    16829

  ASIGNADO − LEÍDO  =  0
```

**Y LO QUE ESTA RESTA NO DICE, porque un cero esconde exactamente esto:**

```text
NO DICE que yo haya leído el documento 11 ENTERO. Mi rango es L5201–L11708 de 11708, y
        **L1–L5200 NO los he leído**: son de `S1`. De ese tramo abrí, SÓLO PARA VERIFICAR y
        declarándolo aquí, §0 (L1-262, porque mi encargo me manda juzgar la REGLA DE
        TITULARES, que vive ahí) y §2.6.7 (L1657-1716, para X63). **NO los declaro leídos.**
        Una contradicción entre §2.6 y §11.6 es estructuralmente invisible para mí.

NO DICE que el documento 11 lo haya leído ENTERO ningún ojo. Es el LÍMITE DE MÉTODO que el
        sexto gate declaró y que este gate hereda: `S1` cubre L1–L5200 y yo L5201–L11708.

TAMPOCO DICE que yo haya auditado el INSTRUMENTO. La batería, el derivador y el emisor son
        lote de `S1`. Los EJECUTÉ —y publico sus salidas— y leí regiones puntuales
        (`_ESTADOS_CL`, `G-10`, `_leer`), pero **no sostengo nada sobre su corrección como
        programas**, y no construí ningún árbol defectuoso.

SÍ DICE que las CINCO fuentes que el manifiesto me asigna están leídas de principio a fin en
        la parte que me asigna, con su SHA-256 recalculado por mí sobre el commit auditado y
        con los rangos publicados arriba para que cualquiera los recomponga.

FUERA DE MI LOTE, abiertas SÓLO PARA VERIFICAR y NO declaradas leídas:
  `docs/owner/ADS-OWNER-RESOLUCIONES.md`  ÍNTEGRA (334 líneas) — me obliga la obligación 6
  el manifiesto del séptimo gate EN EL COMMIT DEL GATE  ÍNTEGRO (260) — obligación 2
  `docs/evolucion/verificacion/CORRIGENDUM-…md`  §14-§19 y su índice
  `docs/evolucion/verificacion/README.md` · la batería · el derivador · el emisor · (a) · (b)
  `E2` · `01-PROCESOS.md` · `C1` · `C2` · `kernel/KERNEL.md` · `kernel/operativo/00-INDICE.md`
  — todos ACOTADOS a la línea que cada afirmación mía necesita.
```

---

## §2 · HALLAZGOS QUE SOSTENGO

> **Convenio de clases**, el del propio gate: `A` coherencia interna, corregible dentro de
> `F4c` · `B` exige una decisión NUEVA del Owner · `C` resistencia a un actor privilegiado,
> **NO exigible en `F4c`** por `O18`. **Ninguno de los míos es `B` ni `C`.**
> Todas las líneas son del **árbol de la CANDIDATA `f8fc037a99…`** salvo donde digo lo contrario.

| id | sev | clase | sede (fichero:línea) | qué afirma la sede | qué dice el árbol (comando y salida) | qué se sigue |
|---|---|---|---|---|---|---|
| **`S2-01`** | **GRAVE** | **A** | `docs/evolucion/00-INDICE.md`:**93** —sede VIVA, sin rótulo histórico—, contra `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md`:**597-619** (§18, escrita por ESTA tanda) y contra el remedio que `EE` determinó en `docs/evolucion/27-…F4C.md`:**3896** | `EE-14`, remedio determinado, **dos mitades**: «*Que la **proyección VIVA (`00-INDICE.md` L93)** publique el desglose **derivado de las filas del documento 26**, y que el error del documento inmutable se acote **con una entrada en el `CORRIGENDUM`***». Y el CORRIGENDUM §18, que la tanda escribe, cierra con la regla: «*toda sede derivada que reproduzca ese desglose lo publica **con el comando que lo deriva de las filas**, o remite*» | **La mitad (a) NO se aplicó, y la fila es byte-idéntica a la que el gate falsó.** `git show b27a761:00-INDICE.md \| grep 'QUINTO GATE…VÁLIDO' \| sha256sum` y lo mismo sobre `f8fc037` → **`aa99111e0ec72478a7af24b68927ed4c81a5537c588a5d3c14b8c256e65fb605` los dos**. La fila sigue publicando `22 hallazgos: BLOQUEANTE 0 · GRAVE 12 · **MEDIO 6 · MENOR 4**`. El comando que el propio CORRIGENDUM §18 publica, ejecutado: `awk '/^\| \*\*\`DD-[0-9]/{print}' 26-…md \| grep -oE '\*\*(BLOQUEANTE\|GRAVE\|MEDIO ESTRUCTURAL\|MEDIO\|MENOR)\*\*' \| sort \| uniq -c` → **12 GRAVE · 4 MEDIO · 1 MEDIO ESTRUCTURAL · 5 MENOR**. Ni `6/4` ni ninguna agregación de esas filas lo da: con `MEDIO ESTRUCTURAL` dentro de MEDIO son **12·5·5**. Y L93 **no lleva el comando ni remite**: `sed -n '93p' \| grep -c 'awk\|grep\|se deriva\|remite'` → **0** | **`EE-14` está aplicado a MEDIAS, y la mitad omitida es la sede que el adjudicador nombró por fichero y línea.** El diff de la tanda sobre `00-INDICE.md` es `18 inserciones · 1 supresión` y **no toca L93**. Peor: la regla que la tanda escribe en CORRIGENDUM §18 —«con el comando que lo deriva, o remite»— es incumplida **en el mismo commit** por la sede que esa entrada existe para corregir. Y la fila de la propia tanda, `00-INDICE.md`:98, declara «`EE-02`, `EE-08` y `EE-14` **van al CORRIGENDUM**», presentando `EE-14` como saldado por la mitad (b) sola |
| **`S2-02`** | **MEDIO** | **A** | `docs/evolucion/00-INDICE.md`:**94** —sede VIVA— contra `docs/evolucion/CHECKPOINT-ADS-NEXT.md`:**3644-3652**, la nota de `EE-10` escrita por ESTA tanda | L94 publica, como forma de contar el censo de la tanda anterior: «*el censo **no se escribe**: lo publica el **PARTE DE LA TANDA** del checkpoint … y **se cuenta con** `awk '/^\| \`(DD\|BT)-[0-9]/{n++} END{print n}' docs/evolucion/CHECKPOINT-ADS-NEXT.md`*» | **Es, byte a byte, el comando que la misma tanda declara defectuoso.** `CHECKPOINT`:3644-3652: «*El comando anterior contaba **filas de cualquier tabla del fichero** con `awk '/^\| \`(DD\|BT)-[0-9]/{n++}'` … **contaba filas y no identificadores distintos** … y **no acotaba la tabla***», y lo sustituye por la forma acotada con `sort -u`. Ejecutados los dos hoy: viejo → **24**; nuevo → **24**. La fila L94 es **idéntica** en `b27a761` y en la candidata: `sha256sum` → `e28a95d1d13b4cf8b2a3b847639c047edd4d1506324d0a7e863f16f3d98d0961` en los dos | **Instancia cerrada, clase abierta, en el mismo commit.** El único otro sitio donde vive el comando viejo es `CHECKPOINT`:3645, y allí va **citado como retirado**. En `00-INDICE.md`:94 vive **como el comando vigente**, presentado con «se cuenta con». Hoy coincide por accidente —no hay ids repetidos ni filas `DD`/`BT` fuera de esa tabla—: es **LATENTE**, y por eso MEDIO y no GRAVE. Es la clase de `BB4` medida sobre el remedio de `EE-10` |
| **`S2-03`** | **MEDIO** | **A** | `docs/evolucion/CHECKPOINT-ADS-NEXT.md`:**1051-1135**, campo `based_on:` del BLOQUE DE ESTADO declarado VIGENTE (L884-1168), contra la **regla 4** escrita dentro del bloque en L906-909 | Regla 4: «*TODO EVENTO NUEVO —un gate devuelto, una resolución del Owner, **una tanda aplicada**— REANCLA `metodo`, `last_meaningful_event` y **`based_on`** EN EL MISMO COMMIT QUE LO REGISTRA*». Y `EE-04`, fila del PARTE (`CHECKPOINT`:3783): «*`metodo`, `last_meaningful_event` y **`based_on`** … Los tres **REANCLADOS**»* | **`based_on` está reanclado en su PREÁMBULO y no en su cuerpo.** Su enumeración de documentos numerados sigue terminando en el **25**: `awk 'NR>=1051 && NR<=1136' CHECKPOINT \| grep -o 'docs/evolucion/[0-9][0-9]-[^ ]*\.md' \| sort -u` → 09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,**25** — y `ls docs/evolucion/[0-9][0-9]-*.md \| sort` da además **26 y 27**. `grep -n '27-SEXTO-GATE' CHECKPOINT` → sólo L19 (cabecera) y L3757 (un comando). **Faltan DOS documentos, no uno**: era 1 cuando `R2-03` lo midió | **`EE-04` está aplicado a medias en el tercero de sus tres campos.** `R2-03` nombró esto en su evidencia con estas palabras —«*la lista de `based_on` … termina en `25-CUARTO-GATE-…`: **el documento 26 no está***»— y `EE` lo sostuvo. **Atenuante, y lo digo:** el bloque declara en L1064-1066 que «*la enumeración de abajo se conserva por comodidad de lectura*» y publica el comando que la deriva; esa cláusula **ya estaba en `8c9ca9c`** y no impidió que `R2-03` cayera ni que `EE` lo sostuviera. Por eso MEDIO y no GRAVE |
| **`S2-04`** | **MEDIO** | **A** | `docs/evolucion/CHECKPOINT-ADS-NEXT.md`:**914**, **924**, **1051-1052**, **1155** (bloque de estado VIGENTE) y **3830** («Siguiente acción exacta», vigente), contra la **regla 2** escrita dentro del bloque en L899-902 | Regla 2: «***EL ÚLTIMO GATE Y SU DOCUMENTO NO SE ESCRIBEN A MANO.** Se derivan con `ls docs/evolucion/[0-9][0-9]-*.md \| sort \| tail -1`*» | **El ordinal del último gate está escrito a mano SEIS veces dentro del bloque vigente.** `awk 'NR>=884 && NR<=1168' CHECKPOINT \| grep -n 'SEXTO GATE'` → 6 ocurrencias (L886, 914, 924, 1051, 1052, 1155 del fichero). Y el comando que la propia regla publica lo **deriva**: `ls docs/evolucion/[0-9][0-9]-*.md \| sort \| tail -1` → `docs/evolucion/**27-SEXTO**-GATE-DE-CERTIFICACION-F4C.md`. El diff del remedio lo muestra sin ambigüedad: `-metodo: … CUARTO GATE …` → `+metodo: … **SEXTO** GATE …`, y lo mismo en `last_meaningful_event` | **El remedio de `EE-04` cerró la INSTANCIA sustituyendo un ordinal escrito a mano por otro ordinal escrito a mano** — que es exactamente lo que la regla 2, escrita dentro del bloque, prohíbe, y exactamente lo que el corpus prohíbe desde `J-07` («no se sustituye un número por otro»). El propio `metodo:` lo hace en la misma frase en que invoca la regla: «*SEXTO GATE DE CERTIFICACIÓN DEVUELTO … **Su documento NO se escribe aquí —regla 2—**: se deriva con `ls …`*» — aplica la regla a la mitad que dice «su documento» y la incumple en la mitad que dice «el último gate». **Caducará en el gate siguiente por la misma vía** |
| **`S2-05`** | **MENOR** | **A** | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`:**1024-1029** (hecho 1 de la «DISPUTA REGISTRADA Y NO RESUELTA»), contra **L1052-1054**, donde el hecho 4 lleva su `[HISTÓRICO]` | Hecho 1: «*`O18` en su entrada de §2 escribe de `(c)`… **Barrido del fichero entero: CERO apariciones de «ADS operativo», CERO de «certificar adaptadores», CERO reparto `SIS`/`PLT`/`VER`/`SEG`***». Y el hecho 4 declara, con su corchete: «*Es **el ÚNICO de los cuatro** que `O19` dejó atrás*» | **El barrido del fichero entero ya no da cero, y la proyección de `O19` lo rompió.** `grep -c 'ADS operativo' DECISIONES` → **4** (L1026, 1029, 1038 y **L1180**); `grep -c 'certificar cualquier adaptador'` → **1** (L1181); `grep -c 'SIS define el contrato de conformidad'` → **1** (L1187). Las tres apariciones nuevas viven en **la proyección de `O19`** (L1176-1193), añadida a este mismo fichero después de que el hecho 1 se escribiera | **La afirmación de que el hecho 4 es «el ÚNICO de los cuatro» que caducó es falsa: el hecho 1 también.** Es la clase `BT-01` —una afirmación caducada que lleva su propio refutador en el mismo bloque— una viñeta más allá de la que se marcó. **MENOR y lo acoto sin adornarlo:** la RESOLUCIÓN de la disputa no cambia, la NOTA DE ALCANCE de L1072-1114 declara la ratificación dada, y el sentido de fondo del hecho 1 —que la entrada CORTA de `O18` no contiene las tres condiciones— **sigue siendo cierto**. Lo que es falso es el barrido tal como está escrito, y el rótulo que lo declara superviviente |

### §2.1 · RECUENTO, DERIVADO DE LAS FILAS DE ARRIBA

```text
BLOQUEANTE   0
GRAVE        1    S2-01
MEDIO        3    S2-02 · S2-03 · S2-04
MENOR        1    S2-05
             ──
              5

POR CLASE
  A · coherencia interna, corregible dentro de `F4c`   5
  B · exige una decisión NUEVA del Owner               0
  C · actor privilegiado (no exigible en `F4c`)        0

POR ÁRBOL
  DE LA CANDIDATA `f8fc037a99…` (el objeto auditado)   5
  DEL APARATO DEL GATE `08f6da6e65…`                   0
  DEL SOBRE                                            0
```

**LOS CINCO SON DEL OBJETO AUDITADO. NINGUNO ES BLOQUEANTE. NINGUNO EXIGE ARQUITECTURA NUEVA.
NINGUNO VUELVE AL OWNER.** Los cinco se cierran con material que el corpus ya tiene escrito, y
ninguno reinterpreta `O17`, `O18` ni `O19`.

**Y LOS CINCO SON DE LA MISMA CLASE**, que es lo que hace que los cuente juntos: **`S2-01` y
`S2-02` son remedios de esta tanda aplicados a una sede y no a la de al lado; `S2-03` y `S2-04`
son el remedio de `EE-04` cerrando su instancia y dejando su clase; `S2-05` es un rótulo de
supervivencia que sobrevivió a lo que declara.** No traigo cinco defectos sueltos: traigo cinco
mediciones de la misma proposición.

**NO PROPONGO NINGUNA CORRECCIÓN, y no he modificado el repositorio** (verificado en §8).

---

## §3 · EL ATAQUE A LA CLASE, CLASE POR CLASE

> La frase que ordena este expediente la fijó `BB4` (doc 26 L209-211) y `EE` la sostuvo por
> segunda vez (doc 27 §5.2): «**El sistema cierra INSTANCIAS y no CLASES.** La corrección se
> aplica con la forma sintáctica exacta del contraejemplo, y el defecto reaparece una sede más
> allá». **La tanda dice haberse escrito contra ella POR SEGUNDA VEZ.** Para cada clase que
> declara cerrada fui a la sede UNA MÁS ALLÁ de la corregida, y publico también las que NO
> cayeron: un ataque que falla es información.

| clase que la tanda declara cerrada | dónde busqué la sede una más allá | qué encontré |
|---|---|---|
| **`EE-14` · «la proyección VIVA publica el desglose derivado, y el inmutable se acota en el CORRIGENDUM»** | El remedio tiene DOS mitades y la tanda publicó la (b). Fui a la (a): la sede que `EE` nombra por fichero y línea, `00-INDICE.md` L93 | **CAE. `S2-01`.** L93 es **byte-idéntica** entre `b27a761` (el árbol que el gate falsó) y la candidata —`sha256sum` de la fila: `aa99111e…` en los dos—. Sigue publicando `MEDIO 6 · MENOR 4`; la derivación de las filas del doc 26 da `12 GRAVE · 4 MEDIO · 1 MEDIO ESTRUCTURAL · 5 MENOR`. Y **no lleva el comando ni remite**, que es la regla que el propio CORRIGENDUM §18 escribe en el mismo commit |
| **`EE-10` · «el comando cuenta IDENTIFICADORES y acota la tabla»** | El comando retirado es `awk '/^\| \`(DD\|BT)-[0-9]/{n++} END{print n}'`. Barrí TODO el corpus vivo buscándolo fuera del checkpoint | **CAE. `S2-02`.** `00-INDICE.md` L94 lo publica **verbatim**, en una fila viva, con la fórmula «**se cuenta con**». Es la única sede que lo presenta como vigente: la otra ocurrencia (`CHECKPOINT`:3645) lo cita **como retirado**. Fila idéntica en los dos árboles: `e28a95d1…`. LATENTE (los dos dan 24 hoy) |
| **`EE-04` · «`metodo`, `last_meaningful_event` y `based_on` REANCLADOS»** | Fui campo por campo. `metodo` y `last_meaningful_event` sí. Fui al tercero, y dentro de él al cuerpo y no al preámbulo | **CAE DOS VECES. `S2-03` y `S2-04`.** (i) `based_on` está reanclado en su preámbulo y su **enumeración sigue terminando en el documento 25**: faltan **26 y 27**, cuando `R2-03` midió que faltaba **uno**. (ii) El reanclaje se hizo **escribiendo «SEXTO GATE» a mano**, seis veces en el bloque vigente, contra la regla 2 escrita dentro de él —«EL ÚLTIMO GATE Y SU DOCUMENTO NO SE ESCRIBEN A MANO»— y en la misma frase que la invoca para la otra mitad |
| **`BT-01` · «una afirmación caducada que lleva su propio refutador al lado, en la entrada de `O17`»** | Fui al bloque gemelo del mismo fichero: la «DISPUTA REGISTRADA Y NO RESUELTA» de la entrada de `O18`, que también publica un barrido y también marca lo que caducó | **CAE. `S2-05`.** El hecho 4 lleva su `[HISTÓRICO]` y declara ser «**el ÚNICO de los cuatro** que `O19` dejó atrás». El hecho 1 —«Barrido del fichero entero: CERO apariciones de «ADS operativo»…»— también caducó: hoy `grep -c 'ADS operativo'` sobre ese fichero da **4**, y tres de las apariciones nuevas las puso la proyección de `O19` **en ese mismo fichero** |
| **`EE-01` · «la guarda de admisión se DERIVA contra la REVISIÓN BASE, y no contra `HEAD`»** | **NO ES MI DOMINIO** — es el instrumento, lote de `S1`, y `EE` lo declaró clase `A` del aparato. **No construí ningún árbol defectuoso y no busqué el décimo.** Lo único que hice fue leer el remedio y ejecutar la batería | **NO ATACADA POR MÍ, y lo declaro sin adornarlo. Mi silencio no es evidencia en ninguna dirección** (§6). Lo que sí mido y consta: `python3 …/comprobar-correccion-gate-de-cierre.py` → **38/38 · rc=0** sobre el árbol del gate, con la línea de ALCANCE derivada |
| **`EE-03` · «los manifiestos se enlazan desde la LISTA, y el comando de autocomprobación se ACOTA A LA LISTA»** | Ejecuté el `diff` que la sede publica, sobre los DOS árboles, y comprobé que el comando acotado ya no es satisfacible desde una fila histórica | **NO CAE.** Sobre el árbol del gate el `diff` sale **VACÍO** (rc=0) y la LISTA cubre las 15 rutas de `find docs/evolucion/verificacion -type f …`, el manifiesto del séptimo gate incluido. Sobre la candidata también sale vacío. Y `T147` da `1 superadas · 0 fallidas` en los dos árboles |
| **`EE-05` · «se retiran las DOS aserciones condicionales caducadas de `C-L.5` y `C-L.7` y se publica el comando»** | Barrí la clase entera: toda sede viva con la forma «mientras … devuelva» / «en cuanto … incorpore» | **NO CAE.** `grep -rn 'MIENTRAS ese comando\|mientras ese comando\|en cuanto ese fichero\|mientras el primero devuelva'` sobre las cuatro fuentes vivas devuelve **dos golpes, y los dos son citas de lo retirado**: `CHECKPOINT`:3784 (la fila `EE-05` del PARTE) y `11-ARQ`:165 (la nota de `EE-06`). Y los comandos que las sustituyen reproducen: `grep -c '"ABIERTA"'` → **2**; `… \| grep G-16` → **`OK G-16`** |
| **`EE-06` · «§0 deja de decir “mientras ese comando devuelva 0”»** | Ejecuté el comando que §0 publica y leí lo que §0 afirma hoy | **NO CAE.** `grep -cniE 'titular\|regla de titulares' <batería>` → **2** (L632 y L664), y §0 ya **no** afirma que devuelva 0: dice «*Lo que NO puede escribirse es qué devolverá*» y separa `LO QUE SÍ HAY` de `LO QUE NO HAY`. La sede dejó de autofalsificarse |
| **`EE-07` · `EE-12` · «los dos cardinales 46 se RETIRAN y se REMITEN»** | Barrí el cardinal en todas las sedes vivas, dentro y fuera de bloques ```` ```text ```` , que es la forma que el barrido de `DD-13` no veía | **NO CAE.** Los dos renglones llevan hoy su `[HISTÓRICO]` y publican `grep -cE '^\| \`?X[0-9]'`, que da **55**. **Ninguna sede viva escribe un cardinal de la tabla adversarial.** Verificado también que la atribución «`PN-17` y `PN-18` las añade esta tanda» está retirada |
| **`EE-13` · «la glosa de `D103` retira el cardinal y publica el comando»** | Fui a la frase gemela en las otras sedes vivas del mismo registro y del checkpoint | **NO CAE.** `grep -n '30 comprobaciones' DECISIONES` → **una sola línea, L448**, y está dentro de la nota que la declara retirada («*este renglón decía…*»). El censo se publica hoy con `python3 …\|tail -3` |
| **`EE-18` · «el rótulo de la sexta cláusula del bloque LITERAL es el SUJETO de la cláusula»** | Coteje **las seis** cláusulas contra la sede con el `sed` que el propio bloque publica, y barrí todos los rótulos de literalidad del corpus vivo | **NO CAE.** El `sed` publicado devuelve las seis viñetas de la sede y el bloque las reproduce **cláusula a cláusula, en el mismo orden, sin recorte ni ampliación**; la sexta se rotula hoy `EL EJECUTOR EXTERNO`, que es su sujeto. Y la glosa del coordinador vive abajo, en un bloque propio rotulado «NO ES LITERAL DE LA SEDE» |
| **`EE-19` · «el sobre dice de qué difieren los UNIVERSOS y publica el comando de los ÁRBOLES»** | Leí el sobre de este gate y ejecuté las dos superficies | **NO CAE.** El sobre de hoy escribe «*son la superficie en que difieren los **UNIVERSOS**, y **NO** la superficie en que difieren los **ÁRBOLES***» y publica `git diff --name-only <cand> <gate>`. Ejecutado: **5** rutas de árbol frente a **2** de universo, y la diferencia son las tres evidencias derivadas. La formulación del sexto gate está corregida |
| **`DD-06` / `Y-05` · «las atribuciones al Owner se barren por el ACTO y no por la tipografía»** | Barrí TODA sede que atribuya algo al Owner, con `grep -rn 'LITERAL\|verbatim\|palabra por palabra\|en sus palabras\|palabras del Owner'` sobre las seis sedes derivadas vivas | **NO CAE en sede viva.** Las cuatro apariciones vivas de «robustez y revalidación…» van rotuladas RESUMEN con su `DD-06`, con el literal separado y su comando; `grep -c 'robustez' <sede canónica>` → **0**. **Cae UNA ocurrencia, y NO la cuento: `CHECKPOINT`:4610 escribe «Su motivo, en sus palabras: ROBUSTEZ Y REVALIDACIÓN…», y vive dentro de `## Siguiente acción exacta — HISTÓRICA, anterior al documento 23` (L4576), con su `[HISTÓRICO]` en L4571 y L4579. Un defecto dentro de una región marcada HISTÓRICA no es un defecto vivo, y lo digo aunque me quitara un hallazgo.** |
| **La REGLA DE TITULARES de §0 · el barrido sobre negritas y rótulos** | Barrí los cardinales vivos derivables de mi rango y de mi lote —§15.8, `PN`, `X<nn>`, `X-S`, `X-O`, `O` de §15.4, las quince capacidades, los diez procesos, las seis extensiones de ficha, los perfiles de agente, `DOM/SEG:condiciones`, `VER:decisión`, `G20`-`G23`— y no sólo sobre `^#` ni sobre `^\*\*` | **NO CAE nada nuevo.** Los quince cardinales que derivé **reproducen todos** (§4.3). El único cardinal escrito junto a su enumeración que encontré es `DIECINUEVE`/`DIECISIETE` en §16 L10642 y L10698, **amparado por la excepción que §0 declara con nombre** —«*un cardinal … que se publica con el comando que lo deriva, en la sede única que lo publica —**así está §16**—*»— y los dos reproducen |

### §3.1 · LO QUE ESTE ATAQUE SEPARA, Y ES LO QUE IMPORTA

```text
LA MITAD QUE SE CUMPLE   de las doce clases que la tanda declara cerradas y que caen en mi
                         dominio, **OCHO aguantan el ataque a la sede de al lado**, y tres de
                         ellas —`EE-07`/`EE-12`, `EE-13`, `EE-18`— son exactamente las que el
                         sexto gate midió como «una sede más allá». **Esta vez se barrió la
                         clase y no la instancia, y hay que decirlo con la misma fuerza.**

LA MITAD QUE NO          **CUATRO caen, y las cuatro por el mismo mecanismo**: un remedio de
                         DOS mitades del que se aplica una (`EE-14`), un comando retirado que
                         sobrevive en la sede vecina (`EE-10`), un campo reanclado en su
                         preámbulo y no en su cuerpo (`EE-04`), y un ordinal escrito a mano
                         para sustituir a otro ordinal escrito a mano (`EE-04` otra vez).

Y LO QUE NO PUEDO DECIR  **no sé si hay un DÉCIMO ÁRBOL.** No lo busqué: es dominio de `S1`.
                         Lo que sí digo es que la frase de `BB4` sigue teniendo instancias
                         vivas en el dominio documental, y que las cuatro que traigo están
                         **dentro de los remedios de esta tanda**, no fuera de ellos.
```

---

## §4 · LO QUE VERIFIQUÉ Y NO CAYÓ

**Pesa tanto como lo que cayó, y va con su comando y su salida.**

### 4.1 · EL SOBRE, Y CON ÉL LA VALIDEZ DEL GATE

```text
· LOS DOS DIGEST DE UNIVERSO reproducen BYTE A BYTE con la receta publicada, recalculados
  ANTES de leer nada:  8c75317fb63e8c645da251968cc6c31a3f91a793a2579f9c14b87c723b67a5f0
                       1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b
· SHA-256 DEL MANIFIESTO en el commit del gate:
  f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff   CASA
· SHA-256 DEL EMISOR y DEL DERIVADOR en los DOS commits: los CUATRO casan, y son idénticos
  entre sí — el commit del gate NO tocó `verificacion/`
· LA SEDE CANÓNICA DEL OWNER: la sede entera y los tres digest `O17`·`O18`·`O19`, en los DOS
  commits: LAS OCHO CIFRAS CASAN, y los recuentos DERIVADOS 85 · 111 · 78 también
· LA SUPERFICIE DE DIVERGENCIA: 2 rutas de UNIVERSO, 5 de ÁRBOL, y el sobre lo distingue
  expresamente — la corrección de `EE-19` está hecha
· `git status --porcelain` VACÍO y `git ls-files -v | grep -vc '^H '` → 0: ningún fichero en
  `skip-worktree` ni `assume-unchanged`, que es la trampa que la obligación 5 advierte
```

**El gate NO es INVÁLIDO por ninguna vía que yo pueda medir.** Ninguno de los disparadores que
§8 del manifiesto nombra se activa.

### 4.2 · EL MANIFIESTO · las 79 filas contra el árbol que declaran

```text
$ (las 79 filas de §4 y §5, contrastadas ruta a ruta contra el árbol de la CANDIDATA,
   SHA-256 y número de líneas)
DISCREPANCIAS: 0

$ suma de la columna «líneas»:  lectura 29117 · agotadas 48562 · total 77679
  manifiesto §6 declara         29117 · 48562, y el sobre declara 77679          CIERRA
$ universo del árbol del GATE   80 fuentes · 77941 líneas
  80 − 79 = 1 (el propio manifiesto) · 77941 − 77679 = 262 = 260 + 2 (00-INDICE)  CIERRA
```

**Y LA FILA DEL PROPIO DERIVADOR —la que el sobre manda mirar PRIMERO** (`U-02`, reincidencia
`X-06`, tercera instancia `DD-18`)—: fila 8, **798 líneas**,
`7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad`, **idéntica en los DOS
árboles y en los dos campos del sobre**. **La clase NO reincide, por tercera vez.**

**Y `EE-02` está cerrado en su primer uso posterior:** el §6 de este manifiesto **DERIVA** las
dos aritméticas con su comando en vez de copiarlas, y **enumera una a una** las fuentes sin
fila del árbol del gate con su razón —el propio manifiesto (punto fijo), las tres evidencias
(no obligatorias) y la fila de `00-INDICE.md` (que sí la tiene)—. Lo comprobé: sobre el árbol
del gate la única fuente sin fila **es el manifiesto en curso**, y ningún otro fichero se
acoge a la exención.

### 4.3 · LAS DERIVACIONES VIVAS, EJECUTADAS UNA A UNA

```bash
awk '/^## 15\.8 /{f=1;next} f&&/^## /{exit} f&&/^### /{n++} END{print n}' 11-ARQ.md    → 18
grep -c '^## `PN-' 11-ARQ.md                                                           → 19
grep '^## `PN-' 11-ARQ.md | grep -vc 'RETIRADA\|FUSIONADA'                             → 17
grep -cE '^\| `?X[0-9]' 11-ARQ.md                                                      → 55
grep -cE '^\| `?O[0-9]+' 11-ARQ.md                                    → 13  (§15.4: O7…O19)
ls -1 kernel/operativo/capacidades/ | wc -l                                            → 15
grep -c '^id: proceso:' kernel/operativo/recorrido/01-PROCESOS.md                      → 10
grep -c '^id: perfil:'  kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md             → 21
grep -c 'DOM:condiciones' 01-PROCESOS.md · 'SEG:condiciones'                        → 4 · 4
grep -rn ':revision' kernel/ | wc -l · ':revisión'                                  → 0 · 0
grep -c 'VER:decisión' b-RECORRIDO-APROBADA.md                                         → 12
grep -rn 'VER:decisión' kernel/ | wc -l · 'VER:decision' kernel/ packs/            → 3 · 14
grep -c '^## Siguiente acci[óo]n exacta' CHECKPOINT.md                                 →  9
awk '…/^### Lo aplicado por la tanda del SEXTO GATE/…' | grep -oE '`EE-[0-9]+`'|sort -u|wc -l → 19
```

**Las quince cuadran con lo que su sede declara.** El censo de `PN` (19 cabeceras − `PN-4`
RETIRADA − `PN-5` FUSIONADA = 17) es exacto y su rango vivo `PN-6`–`PN-19` termina en la última
cabecera vigente. Los cardinales que §16 escribe —DIECINUEVE y DIECISIETE— están amparados por
la excepción que §0 declara **con nombre** y reproducen los dos.

### 4.4 · EL PARTE DE LA TANDA · su comando cuenta lo que dice contar, y CUBRE LOS 19

```bash
# los identificadores que la tanda aplica
awk '/^### Lo aplicado por la tanda del SEXTO GATE/{t=1} t' CHECKPOINT.md |
  grep -oE '`EE-[0-9]+`' | sort -u | wc -l
→ 19    (EE-01 … EE-19, sin hueco)

# la COBERTURA contra el gate — la sede dice que sale VACÍO
comm -23 <(grep -oE '^\| [0-9]+ \| \*\*`EE-[0-9]+`' 27-…F4C.md | grep -oE 'EE-[0-9]+' | sort -u) \
         <(awk '/^### Lo aplicado por la tanda del SEXTO GATE/{t=1} t' CHECKPOINT.md \
           | grep -oE 'EE-[0-9]+' | sort -u)
→ (VACÍO)
```

**Los 19 del documento 27 están cubiertos, uno a uno, y la resta sale vacía.** Y la advertencia
del parte es cierta y verificable: hay **18 filas** para 19 identificadores porque `EE-07` y
`EE-12` comparten fila, exactamente como el propio parte declara. **El comando de este parte
cuenta identificadores distintos y acota la tabla** —es el remedio de `EE-10`— y **mide lo que
la frase dice que mide**. Es la mitad de `EE-10` que sí se aplicó, y es correcta.

**Y cada remedio está donde la fila dice que está**, comprobado uno a uno en las sedes de mi
dominio: `EE-03` (los tres manifiestos en la LISTA, y el `diff` acotado vacío), `EE-05` (las
dos filas retiradas y con su comando), `EE-06` (§0 reescrita), `EE-07`/`EE-12` (los dos
cardinales retirados con su `[HISTÓRICO]`), `EE-13` (la glosa de `D103` remitiendo),
`EE-18` (`EL EJECUTOR EXTERNO` como sujeto de la sexta cláusula), `EE-19` (el sobre distingue
universos de árboles), `EE-02`/`EE-08`/`EE-14` (CORRIGENDUM §16, §17 y §18, que existen y
llevan su comando). **Las excepciones son las cuatro de §2**, y sólo `EE-14` deja media sede
sin tocar.

### 4.5 · LAS ATRIBUCIONES AL OWNER · la sede manda y las proyecciones NO la amplían

Ésta es la obligación 6, y la respondo con el cotejo cláusula a cláusula:

```text
· `grep -c 'robustez' docs/owner/ADS-OWNER-RESOLUCIONES.md` → 0, y las CUATRO sedes vivas que
  usan la frase la rotulan RESUMEN con su `DD-06`, con el literal separado y su comando
· EL LITERAL DE `O17`: `sed -n '/^No elijo la alternativa barata/,/^recursos\.$/p'` sobre la
  sede devuelve el párrafo íntegro, y el registro (L811-815) y el checkpoint (L387-391) lo
  reproducen **palabra por palabra**
· EL REPARTO LITERAL de §11.8 (11-ARQ L8824-8829) contra
  `sed -n '/^· SIS define el contrato/,/^· el ejecutor externo/p'` sobre la sede:
  **las SEIS cláusulas reproducen, en el mismo orden, sin recorte ni ampliación**
· LO QUE (b) NO PROTEGE de §11.7 (L8670-8675) contra el bloque «Alcance de la garantía
  documental, dicho por el Owner» de la sede (L242-248): **los SEIS riesgos, exactos**
· LAS TRES CONDICIONES OBLIGATORIAS y EL REPARTO de la proyección de `O19`
  (DECISIONES L1176-1193) contra la sede (L179-193): **reproducen cláusula a cláusula**
· LAS DOCE REGLAS de `O17` (DECISIONES L872-892) contra la sede (L95-120): **reproducen**;
  y el reparto (L898-904) contra la sede (L125-131): **reproduce**
· LOS RÓTULOS «LITERAL DE `O18`» que `O19` ordena reatribuir: **corregidos en las DOS sedes**
  de §11.7 (L8658) y §11.8 (L8809), que hoy dicen «LITERAL DE LA SEDE CANÓNICA DEL OWNER,
  RATIFICADO MEDIANTE `O19`». `DD-14` cerró el par entero
· EL CENSO DE PROYECCIONES QUE ENLAZAN A SU SEDE, con el `awk` que el registro publica:
  `O17 → 5 · O18 → 3 · O19 → 1`, y `O7`–`O14`/`O15`/`O16` → 0, que es lo correcto porque el
  Owner ordenó que `O1`–`O16` NO se registren en la sede
```

**NO ENCONTRÉ NINGUNA PARÁFRASIS QUE AMPLÍE EL TEXTO CANÓNICO. CERO amplificación de
contenido, en las tres resoluciones y en las seis sedes derivadas vivas.** Lo que sí encontré
es una **OMISIÓN** —la proyección de `O17` en el registro no reproduce el párrafo final de la
sede, «*Si alguna atribución técnica más concreta ya está inequívocamente fijada…*» (sede
L133-135)—. **NO la cuento como hallazgo, y digo por qué:** una omisión no es una ampliación,
la entrada se declara PROYECCIÓN y enlaza a la sede en cinco sitios, y `O19` ordenó que la
autoridad sea la sede precisamente para que una proyección incompleta no gobierne. La regla que
el sobre me da es «*una paráfrasis que AMPLÍE el texto canónico es un hallazgo*», y ésta no
amplía. **Lo consigno para el adjudicador y no lo inflo.**

### 4.6 · `X63` · NO se presenta como prueba ejecutada ni como certificación presente

Barrí **todas** sus apariciones vivas —`git grep -n 'X63'` sobre el árbol, descontando los
dictámenes 20–27 y los manifiestos, que son inmutables—:

```text
00-INDICE:94   «`X63` es CONTRATO DE PRUEBA DE `F6`, no una prueba ejecutada ni una
                certificación presente»                                          CORRECTO
00-INDICE:97   «`X63` no se presenta como prueba ejecutada en ninguna de sus ocho sedes» CORRECTO
00-INDICE:98   «`X63` sigue siendo CONTRATO DE PRUEBA DE `F6`, no ejecutado»      CORRECTO
CHECKPOINT:44 · :3702 · :3735 · :3817   las cuatro lo declaran contrato NO ejecutado CORRECTO
11-ARQ:1714    la fila de §2.6.7, cuya sección declara que ninguna se ha ejecutado CORRECTO
11-ARQ:1742 · :3715 · :5517 · :5688     contrato, nota histórica y subjuntivo      CORRECTO
11-ARQ:5676    «y **`X63`** la comprueba validando las tres celdas…»              ← PRESENTE
11-ARQ:5688    doce líneas más abajo: «es un contrato de prueba de `F6` … y **no se
               ejecuta aquí**»                                                   DESAMBIGUADO
```

**RESPUESTA: NO. Ninguna sede lo presenta como ejecutado ni como certificación presente.** El
único presente de indicativo (L5676) es la voz con que el documento escribe **todas** sus filas
`X<nn>`, y queda desambiguado doce líneas más abajo en el mismo bloque y por tres sedes que lo
niegan expresamente. **No lo cuento**, exactamente como `R2` y `EE` decidieron antes que yo,
y por la misma razón.

### 4.7 · `M-04`, y lo que queda declarado CERRADO o SUPERADO

Barrido sobre las cinco fuentes vivas: **`M-04` aparece siempre como NO superada / FALLIDA /
sigue viva**; **`F4c` siempre ABIERTA**; **`F5` siempre NO AUTORIZADA**; el PARTE declara
«NINGÚN HALLAZGO SUPERADO … ni uno», y el bloque «Lo que esta tanda NO ha hecho» lo repite.
**No encontré ni una sede viva que declare CERRADO o SUPERADO algo que no lo esté.** Los
«CERRADO» que la tanda escribe —`AA-01`, `AA-05`, `DD-01` «cerró su clase»— son transcripción
de veredictos ajenos y van atribuidos a ellos. **`M-04` no la mido: no construí ningún árbol
defectuoso, es dominio de `S1`, y mi silencio no es evidencia en ninguna dirección.**

### 4.8 · `C-L.5` · **NO ES UNA EVASIÓN, Y LO DIGO CON CLARIDAD**

El manifiesto me pide resolverlo expresamente. **Mi respuesta: dejarla ABIERTA es CORRECTO, y
la de este gate es la SEGUNDA vez que lo es por la misma razón, no una evasión que se perpetúa.**

```text
LO QUE LOS DOS GATES MIDIERON   quinto (doc 26 §4): las dos restas a ∅
                                sexto (doc 27 §4): las dos restas a ∅
LO QUE NINGUNO ESCRIBIÓ         la palabra CERTIFICADA
POR QUÉ NO LA ESCRIBIÓ `EE`     lo dice él, en doc 27 §4.1, y son TRES razones, **la primera
                                material**: el §6 del manifiesto `6B` publicaba un cardinal
                                FALSO sobre la aritmética de cobertura que se le pedía
                                certificar (`EE-02`), y **certificar apoyándose en una
                                medición que acababa de refutar sería certificar una refutación**
```

**Y lo que decide que no es evasión es que la condición de cierre que `EE` escribió ES
ALCANZABLE, ESTÁ DETERMINADA, Y ESTA TANDA LA HA CUMPLIDO** (doc 27 §4.1, «QUÉ LA CERRARÍA»):

```text
«un manifiesto cuyo §6 DERIVE las dos aritméticas con su comando en vez de copiarlas, y en el
 que el manifiesto sustituido o bien lleve fila, o bien quede excluido con una razón DERIVADA
 y publicada. Con eso, y sin nada más, la cobertura queda certificable.»
```

**Lo comprobé sobre el manifiesto del séptimo gate, y las dos mitades están hechas:** su §6
publica los comandos que derivan las dos aritméticas (L174-186) y **enumera una a una**, con su
razón, las fuentes sin fila del árbol del gate (L198-209), declarando que la exención de punto
fijo «cubre a ESTE fichero y a NINGÚN OTRO». Y esta vez **no hay manifiesto sustituido**.

**CONCLUSIÓN, y es la que el manifiesto me pide emitir en mi dominio:** dejarla ABIERTA fue
correcto en los dos gates —certificar es un ACTO del adjudicador y no una consecuencia que un
coordinador deduzca de una medición, y el corpus castigó esa deducción dos veces (`Q-06`,
`AA-02`)—; **y NO es una evasión que se perpetúa, porque el obstáculo que `EE` nombró está
retirado en el aparato de ESTE gate.** Lo que queda es un acto, y el acto es del adjudicador
`FF`, no mío ni del coordinador. **Yo no la certifico —no me corresponde— y dejo medido que
el impedimento que la mantenía abierta ya no está.**

### 4.9 · `C-L.7` · **NO. NO REANCLA POR PRIMERA VEZ CONTRA LA REGLA ESCRITA DENTRO DE ÉL**

El manifiesto pregunta: «*El bloque de estado dice REANCLAR por primera vez contra la regla
escrita dentro de él. ¿Es cierto? ¿O vuelve a haber una sede que copia lo que declara no
copiar?*». **Mi respuesta, medida:**

```text
LO QUE SÍ SE HIZO   `metodo:` y `last_meaningful_event:` describen hoy el SEXTO gate y esta
                    tanda; lo anterior bajó a `_anterior` como la regla 5 ordena; el preámbulo
                    de `based_on` se reancló. Sobre eso, la regla 4 se cumple: el evento está
                    en el bloque y no sólo en la cabecera. **Es una mejora real sobre `R2-03`.**

LO QUE NO           (i) `based_on` está reanclado en su PREÁMBULO y su ENUMERACIÓN sigue
                    terminando en el documento **25**: faltan **26 y 27**. Es `S2-03`, y es la
                    misma evidencia que `R2-03` publicó, con un documento MÁS de retraso.
                    (ii) El reanclaje se hizo **escribiendo el ordinal del último gate a mano**,
                    seis veces, contra la regla 2 del propio bloque. Es `S2-04`.

POR TANTO           **SÍ vuelve a haber una sede que copia lo que declara no copiar**, y es el
                    propio bloque: copia el ORDINAL DEL ÚLTIMO GATE, que su regla 2 manda
                    derivar, y copia una LISTA DE DOCUMENTOS que su regla 1 manda no copiar y
                    que además está desactualizada en dos.
                    **`C-L.7` NO está cerrada, y por mi parte tampoco se acerca a estarlo por
                    esta vía: el remedio sustituyó un ordinal a mano por otro ordinal a mano.**
```

### 4.10 · COHERENCIA TRANSVERSAL entre las cinco sedes

Coteje, estado por estado, `00-INDICE` · `CHECKPOINT` · `11-ARQ` · `DECISIONES` · el
manifiesto:

```text
`F4c` ABIERTA                    coincide en las cinco
`F5` NO AUTORIZADA               coincide en las cinco
`M-04` NO superada               coincide en las cinco
`C-L.5` ABIERTA                  coincide: la sede única es la CLASIFICACIÓN VIGENTE del
                                 checkpoint (L2175-2201); `11-ARQ` §C-L.5 RETIRA su estado y
                                 remite con su `grep` (`DD-07`); `00-INDICE` no lo publica
`C-L.7` NO CERRADA               coincide en las cinco
la clasificación de las 13 `C-L` 7 + 1 + 2 + 1 + 1 + 1 = 13, cada id EXACTAMENTE UNA VEZ
la serie `D1`–`D108`             108 ids, sin huecos ni duplicados
la serie `O1`–`O19`               19 ids, sin huecos; `O1`–`O16` NO en la sede canónica, por
                                 orden literal del Owner, y §11.9 lo declara
las 79 filas del manifiesto      = el universo derivado de la candidata, `diff` vacío
```

**Las contradicciones vivas que encontré son las CINCO que sostengo en §2, y ninguna más.**

---

## §5 · REFUTACIONES CONTRA MIS PROPIAS CONCLUSIONES

Intenté **ocho**. **Dos cayeron, dos cayeron a medias, cuatro no cayeron.** Publico las ocho.

### `RF-1` · **CAYÓ A MEDIAS · «`S2-01` es falso: `00-INDICE.md` L93 no inventa una cifra, TRANSCRIBE fielmente la que el documento 26 publica en su §6.4»**

**Es cierto y lo compruebo, y va contra la comodidad de mi hallazgo:**

```text
$ sed -n '/RECUENTO, DERIVADO DE LAS FILAS/,/^```$/p' 26-…F4C.md
                 DEL OBJETO   DEL APARATO   TOTAL
  GRAVE              10             2         12
  MEDIO               3             3          6
  MENOR               3             1          4
$ 00-INDICE.md:93   «22 hallazgos: BLOQUEANTE 0 · GRAVE 12 · MEDIO 6 · MENOR 4»
```

**El índice NO inventa: copia.** Acepto eso y lo escribo en el hallazgo. **Y no cae la otra
mitad, que es la que sostengo:** el documento 26 es INMUTABLE y su defecto interno **no es un
defecto vivo** —lo digo yo, no me lo conceden—; lo vivo es que una sede derivada **reproduzca
ese desglose desnudo**, que es precisamente lo que la entrada §18 del CORRIGENDUM, **escrita
por esta tanda en este commit**, prohíbe con estas palabras: «*toda sede derivada que reproduzca
ese desglose lo publica **con el comando que lo deriva de las filas**, o remite*». L93
reproduce, sin comando y sin remisión. **Y `EE` lo determinó nombrando la sede y la línea.**
`S2-01` se mantiene, **acotado**: no es una cifra inventada, es una cifra **copiada de un
inmutable en una sede viva contra la regla que el mismo commit escribe**.

### `RF-2` · **CAYÓ A MEDIAS · «`S2-01` no es un hallazgo nuevo: es `EE-14` sin cerrar, y los hallazgos del gate anterior no se recuentan»**

**Cae, y lo acepto: `S2-01` NO es un defecto nuevo.** Es `EE-14` **aplicado a medias**, y así lo
rotulo. **No cae en lo que importa, y es lo contrario de un atenuante:** el manifiesto de este
gate me encarga expresamente comprobar «*¿Está cada remedio donde la fila dice que está?*», y la
respuesta para `EE-14` es **no en la mitad que el adjudicador nombró por fichero y línea**. Un
remedio a medias no es un hallazgo menor que uno nuevo: es la clase que este expediente lleva
seis gates midiendo. **Lo mantengo, y lo rotulo como lo que es.**

### `RF-3` · **NO CAYÓ · «`S2-02` es inocuo: los dos comandos dan 24 hoy, luego no hay ninguna afirmación falsa»**

**Cierto, y por eso lo gradúo MEDIO y lo declaro LATENTE en su propia fila.** `awk` viejo → 24;
`awk` nuevo acotado → 24. **NO CAE**, por lo que la propia tanda escribió al retirarlo: el
defecto no es el número, es que **el comando no mide lo que la frase dice que mide**
—`CHECKPOINT`:3644-3652, palabras de la tanda—. Una cifra con un comando que cuenta otra cosa
no es refutable, que es la exigencia de `J-07` aplicada al instrumento de la reconciliación.
Y la coincidencia de hoy es **accidental**: se rompe con un id repetido en dos filas o con una
fila `DD`/`BT` en cualquier otra tabla del fichero.

### `RF-4` · **NO CAYÓ · «`S2-03` cae: el bloque declara que la enumeración se conserva “por comodidad de lectura”, dice que NO es sede y publica el comando que la deriva»**

Es la defensa más fuerte contra `S2-03` y la construí en serio. **NO CAE, por dos medidas:**

1. **La cláusula ya estaba, y no salvó a nadie.** `git show 8c9ca9c:CHECKPOINT-ADS-NEXT.md |
   grep -n 'comodidad de lectura'` → **L964**, presente en el árbol del quinto gate. `R2-03`
   cayó igual, con esa cláusula delante, y `EE` lo sostuvo como `EE-04`.
2. **La regla 4 nombra `based_on` explícitamente** entre los tres campos que todo evento nuevo
   reancla, y el PARTE declara «*Los tres REANCLADOS*». El preámbulo lo está; el cuerpo, no.
   **Con dos documentos de retraso donde `R2-03` midió uno.**

### `RF-5` · **NO CAYÓ · «`S2-04` cae: la regla 2 se refiere al DOCUMENTO —el número—, no al nombre ordinal del gate»**

Fui al texto literal, que es lo que decide. **NO CAE:** la regla dice «**EL ÚLTIMO GATE Y SU
DOCUMENTO** NO SE ESCRIBEN A MANO. **Se derivan con** `ls docs/evolucion/[0-9][0-9]-*.md | sort
| tail -1`» — **dos conjuntos, un solo comando**, y ese comando devuelve
`27-**SEXTO**-GATE-DE-CERTIFICACION-F4C.md`: **el ordinal está DENTRO de lo que la regla manda
derivar.** Y el propio `metodo:` lo demuestra: escribe «SEXTO GATE» a mano **en la misma frase**
en que dice «*Su documento NO se escribe aquí —regla 2—*». Aplica su regla a un conjunto y la
incumple en el otro. Miré además la lista de excepciones que el bloque se reserva —«*lo que este
bloque sí dice, porque es el estado y no una cifra: `F4c` ABIERTA, `F5` NO AUTORIZADA, `M-04`,
`C-L.5`, `C-L.7`*»— y **el ordinal del gate no está en ella.**

### `RF-6` · **CAYÓ · «`S2-05` cae: todo el bloque de la DISPUTA es registro histórico de lo que el documento 24 estableció, luego un defecto dentro de él no es vivo»**

La construí porque mi propia disciplina me obliga a intentarla. **CAYÓ A MI FAVOR y no la
cuento como caída del hallazgo, sino como su acotación** — y explico la diferencia. El bloque
**no lleva rótulo histórico como bloque**: sólo el hecho 4 lleva su `[HISTÓRICO]`, y lo lleva
diciendo «*Es el **ÚNICO** de los cuatro que `O19` dejó atrás*». **Esa afirmación es lo que
falla**, y no puede ser histórica porque es la que fecha a las demás. **Pero acepto y escribo
la acotación:** la RESOLUCIÓN de la disputa no cambia, la NOTA DE ALCANCE de L1072-1114 declara
que la ratificación llegó, y el **sentido de fondo** del hecho 1 —que la entrada CORTA de `O18`
no contiene las tres condiciones— **sigue siendo cierto**. Por eso es MENOR y no más.

### `RF-7` · **CAYÓ · «hay un sexto hallazgo: `CHECKPOINT`:4610 atribuye al Owner “en sus palabras” la frase que `DD-06` retiró»**

Iba a contarlo, y es exactamente la clase que `DD-06` castiga. **CAYÓ, y lo digo aunque me
quite un hallazgo.** La ocurrencia vive en `## Siguiente acción exacta — **HISTÓRICA**, anterior
al documento 23` (L4576), con su `[HISTÓRICO]` en L4571 y con L4579 declarando que «*todo lo que
sigue hasta el final de esta sección es el texto ANTERIOR*». **Un defecto dentro de una región
marcada HISTÓRICA no es un defecto vivo, y mi encargo me obliga a decirlo.** Retirado de mi
censo. **Un hallazgo menos.**

### `RF-8` · **NO CAYÓ · «los cinco son cosmética documental, y un veredicto no puede colgar de rótulos y cardinales»**

**No cae, y no porque yo defienda mi censo, sino por lo que los cinco son.** Concedo lo
principal: **mi veredicto no cuelga de ellos y no sostengo que la arquitectura sea insuficiente
por mis cinco.** Lo que sostengo es más estrecho y más duro: **cuatro de los cinco son remedios
de ESTA tanda aplicados a una sede y no a la de al lado**, y uno de ellos —`S2-01`— deja sin
tocar la sede que el adjudicador nombró por fichero y línea mientras el mismo commit escribe la
regla que esa sede incumple. **En un corpus que se audita por su propio texto, un remedio que
declara cerrar una clase y cierra media instancia no es cosmética: es la medición de la
proposición que ordena el expediente.**

### §5.1 · Qué cambiaron estas ocho en mi informe

```text
· un hallazgo RETIRADO del censo (RF-7): `CHECKPOINT`:4610 es región HISTÓRICA
· `S2-01` queda ACOTADO: el índice COPIA, no inventa — y eso es exactamente lo que la
  regla del CORRIGENDUM §18 prohíbe (RF-1)
· `S2-01` deja de reclamar novedad: se rotula «`EE-14` aplicado a medias» (RF-2)
· `S2-02` queda declarado LATENTE en su propia fila, y por eso es MEDIO (RF-3)
· `S2-05` queda ACOTADO al rótulo de supervivencia, no a la resolución (RF-6)
```

**Cinco de mis seis movimientos van contra el interés de mi propio censo, y ninguno lo mejora.**

---

## §6 · LO QUE MI LOTE NO CUBRE, SIN ADORNO

**Una resta que da cero esconde esto, y por eso va aquí y no en una nota al pie.**

1. **NO he leído `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` L1–L5200.** Es el lote de `S1`.
   De ese tramo abrí **sólo** §0 (L1-262, porque mi encargo me manda juzgar la REGLA DE
   TITULARES, que vive ahí) y §2.6.7 (L1657-1716, para `X63`), y **los declaro abiertos para
   verificar, NO leídos**. Todo §1, §2, §3 y §4 —el protocolo transaccional, los tipos, el
   contrato documental— está **fuera de mi lectura**. Una contradicción entre §2.6 y §11.6 es
   estructuralmente invisible para mí.
2. **NINGÚN OJO HA LEÍDO EL DOCUMENTO 11 ENTERO**, ni en este gate ni en el anterior. `S1`
   cubre L1–L5200 y yo L5201–L11708. **Una contradicción a caballo de L5200 es invisible para
   los dos y para el adjudicador.** Es el límite de método que `EE` declaró y que este gate
   hereda sin cambiarlo.
3. **NO he auditado el INSTRUMENTO como código.** La batería, el derivador y el emisor son lote
   de `S1`. Los EJECUTÉ —y publico sus salidas— y leí regiones puntuales; **no sostengo nada
   sobre su corrección como programas**.
4. **`M-04` y el DÉCIMO ÁRBOL: NO ATACADOS POR MÍ.** No construí un solo árbol defectuoso, no
   busqué la puerta siguiente y no probé el remedio de `EE-01` con un contraejemplo propio.
   **Mi silencio no es evidencia en ninguna dirección**, y el adjudicador no debe leerlo como
   tal. Es lote de `S1`, y es la razón principal por la que mi veredicto no puede ser el del
   gate.
5. **NO he verificado los CINCO CONTROLES POSITIVOS que la tanda declara commiteados.**
   Ejecutar cinco variantes commiteadas exige construir cinco árboles, y eso es `S1`. Lo que sí
   hice fue ejecutar la batería sobre el árbol del gate —38/38, rc=0— y leer el remedio.
6. **NO he ejecutado ni una sola de las pruebas que el corpus describe** —las 55 filas `X`, las
   18 ventanas `W`, las `X-S`, las `X-O`, las `X-A`–`X-H`, los 11 `NP`, los 12 escenarios de
   §14—. **Todo es contrato escrito y ninguno se ha ejecutado**, y ninguna cantidad de
   hallazgos coherentes sustituye ese hecho.
7. **NO he juzgado las once condiciones `C-L` distintas de `C-L.5` y `C-L.7`.** Sólo comprobé
   que la clasificación vigente lista cada id exactamente una vez y suma 13. **No he auditado
   si el estado que cada una declara es cierto.**
8. **NO he verificado que `S1` lea lo que declare.** La resta `ASIGNADO − LEÍDO` de la otra
   cadena la cruza el adjudicador `FF`, no yo, y es exactamente la que hundió al cuarto gate.
   Publico el SHA-256 del sobre que recibí y lo embebo entero en §0.1 precisamente para eso.
9. **LA SEDE CANÓNICA DEL OWNER NO ES VERIFICABLE CONTRA NADA EXTERNO, y lo declara ella
   misma.** Recalculé sus cuatro digest en los dos commits y son idénticos. **Eso prueba que el
   texto no cambió entre el commit auditado y lo que recibí FUERA del árbol. NO prueba que sea
   el que el Owner emitió.** Sigue vigente hasta el verificador externo de `F6`.
10. **Los SHA-256 del emisor y del derivador que verifiqué NO prueban que los programas que
    corrieron fueran ésos.** El propio sobre lo retira en su obligación 5 (`Z-11`), y **yo no
    lo recupero**; lo único que añado es que comprobé que no hay `skip-worktree` en el índice.
11. **NO he juzgado si la arquitectura es buena.** Sé qué dicen sus sedes y si se contradicen.
    **No opino sobre el diseño, y no lo insinúo.**
12. **`A14` es limitación aceptada, no hallazgo.** Todo lo que ejecuté fue con **Python
    3.12.14**, y lo digo. Con el 3.10 del sistema caen `arranque`, `fuentes` y `workspace` por
    `tomllib`, idénticas sobre `HEAD` sin tocar.
13. **Reproducibilidad:** todo se midió con Python 3.12.14 y `git` sobre WSL2. No probé otro
    intérprete ni otro sistema de ficheros.

---

## §7 · MI RESPUESTA, EN UNA FRASE

> **NO. En lo que a mi dominio toca, `F4c` NO ES SUFICIENTE PARA `F5`: la tanda que dice
> haberse escrito por SEGUNDA vez contra «el sistema cierra INSTANCIAS y no CLASES» vuelve a
> cerrar media instancia en cuatro de sus propios remedios —`EE-14` deja intacta, byte a byte,
> la sede que el adjudicador nombró por fichero y línea, mientras el mismo commit escribe en el
> CORRIGENDUM la regla que esa sede incumple; el comando que `EE-10` retira sigue publicado
> como vigente en `00-INDICE.md` L94; y `EE-04` reancla `based_on` en su preámbulo dejando su
> enumeración dos documentos atrás y sustituye un ordinal escrito a mano por otro ordinal
> escrito a mano contra la regla 2 escrita dentro del propio bloque, con lo que `C-L.7` sigue
> NO CERRADA y el bloque vuelve a copiar lo que declara no copiar— sin que ninguno de mis cinco
> sea BLOQUEANTE, exija arquitectura nueva ni vuelva al Owner, y con `C-L.5` correctamente
> ABIERTA y no evadida: dejarla abierta fue correcto las dos veces, y el impedimento que `EE`
> nombró para no certificarla —un §6 que copiaba en vez de derivar— **está retirado en el
> manifiesto de este gate**, de modo que lo que queda es un ACTO del adjudicador y no una
> medición pendiente.**

**Y lo que consta a favor, porque es verdad y no es cortesía:** las seis obligaciones del sobre
se cumplen sin una sola discrepancia numérica y el gate **no es inválido por ninguna vía que yo
pueda medir**; las 79 filas del manifiesto casan sin una discrepancia y **la fila del propio
derivador no reincide por tercera vez**; `EE-02` está cerrado en su primer uso posterior —el §6
DERIVA las dos aritméticas y enumera una a una las fuentes sin fila—; `EE-03`, `EE-05`, `EE-06`,
`EE-07`/`EE-12`, `EE-13`, `EE-18` y `EE-19` **aguantan el ataque a la sede de al lado**, y tres
de ellos son precisamente los que el sexto gate midió como «una sede más allá»; las quince
derivaciones vivas de mi lote reproducen todas; **no hay ni una paráfrasis que amplíe la sede
canónica del Owner**, y los dos rótulos «LITERAL DE `O18`» están reatribuidos; `X63` no se
presenta como prueba ejecutada en ninguna de sus sedes; ninguna sede viva declara CERRADO o
SUPERADO lo que no lo está; y el PARTE cubre los diecinueve del documento 27 con la resta a
vacío y con un comando que **sí** mide lo que dice medir.

**— `S2`, revisor independiente del séptimo gate. NO emito veredicto de certificación: es del
adjudicador `FF`. NO he propuesto ninguna corrección y NO he modificado el repositorio.**

---

## §8 · DISCIPLINA — declaración de cierre

```text
git status --porcelain   AL ABRIR   →  VACÍO
git status --porcelain   AL CERRAR  →  VACÍO
HEAD al abrir y al cerrar           →  08f6da6e655d19eb9078fbd7284594162e727d3f, idéntico
git ls-files -v | grep -vc '^H '    →  0  (ni skip-worktree ni assume-unchanged)
FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ    ninguno
COMMITS · PUSH · PR · MERGE · RAMAS · REFS                      ninguno
CÓMO LEÍ      `git show <commit>:<ruta>` y lectura por rangos sobre el árbol de trabajo, que
              está en el commit del GATE; el `00-INDICE.md` que se me asigna lo extraje del
              COMMIT CANDIDATO a una copia fuera del repositorio, y publiqué el `diff` entero
              contra el del gate para no dejar ni una línea sin ver
CÓMO EJECUTÉ  checkouts aislados (`git read-tree` + `git checkout-index --prefix`) en
              directorios temporales fuera del repositorio, borrados al terminar
INTÉRPRETE    Python 3.12.14 (shim del encargo). Con el 3.10 del sistema caen `arranque`,
              `fuentes` y `workspace` por `tomllib`: es `A14`, limitación aceptada, NO hallazgo
SUBAGENTE `Agent`                                               NO USADO
NINGUNA HUELLA DE ESTE INFORME SE HA ABREVIADO A MANO (`DD-22`): donde aparece un prefijo, va
con el comando que lo produce, y las huellas completas van completas
NINGÚN HALLAZGO CORREGIDO, y es deliberado: quien corrige no certifica
```

### §8.1 · AUTOCOMPROBACIÓN DEL SOBRE EMBEBIDO

Porque el cuarto gate murió por una transcripción y el manifiesto lo exige.

```bash
sha256sum /tmp/.../scratchpad/f4c/SOBRE-7.txt
dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2  SOBRE-7.txt
```

**El bloque de §0.1 es el fichero del sobre, volcado con `cat` en el mismo comando que escribió
esta sección, sin transcripción manual de ningún campo.** `FF` puede contrastar mi huella contra
la de `S1` y la suya: **si difiere una sola, el gate es inválido.**

---

## §C · ADJUDICACIÓN DE `FF` — TRANSCRIPCIÓN LITERAL

# ADJUDICACIÓN `FF` — SÉPTIMO GATE DE CERTIFICACIÓN DE F4c

Adjudicador: `FF`. Contexto limpio. No he escrito ni una línea del corpus auditado, no he aplicado
ninguna corrección, no he sido revisor de ningún gate anterior.

**El repositorio auditado `/home/jose/ads-kernel` NO se ha modificado.** Todo ataque y toda derivación
se han hecho sobre un clon desechable en
`/tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/ff/repo-FF`
y sobre clones hijos de él.

Fecha: 2026-08-31.

---

## §0 · EL SOBRE, SUS SEIS OBLIGACIONES, Y LOS BLOQUES EMBEBIDOS

### §0.0 · Comprobación previa: los bloques de sobre que cada revisor embebió

Extraigo el bloque literal de cada informe y lo contrasto BYTE A BYTE contra el fichero del sobre.

```console
$ sed -n '19,214p' INFORME-S1.md > s1sobre.txt      # bloque entre las cercas ``` de las líneas 18 y 215
$ sed -n '18,213p' INFORME-S2.md > s2sobre.txt      # bloque entre las cercas ```text/``` de las líneas 17 y 214
$ sha256sum SOBRE-7.txt s1sobre.txt s2sobre.txt
dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2  SOBRE-7.txt
dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2  s1sobre.txt
dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2  s2sobre.txt
$ diff SOBRE-7.txt s1sobre.txt && echo IDENTICO
IDENTICO
$ diff SOBRE-7.txt s2sobre.txt && echo IDENTICO
IDENTICO
$ diff s1sobre.txt s2sobre.txt && echo IDENTICO
IDENTICO
```

**Los dos revisores embebieron EL MISMO sobre, y es EL sobre.** 196 líneas, mismo SHA-256.
No hay causa de invalidez por divergencia de sobres. Sigo.

### §0.1 · Obligación 1 — RECALCULAR LOS DOS DIGEST (hecho por mí, en el clon)

```console
$ for C in f8fc037a...ce60 08f6da6e...727d3f; do
    d=$(mktemp -d); GIT_INDEX_FILE="$d/idx" git read-tree "$C"
    GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
    python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
      while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
      awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum ; rm -rf "$d"; done

f8fc037a998316081a7e9b9563398d118982ce60  8c75317fb63e8c645da251968cc6c31a3f91a793a2579f9c14b87c723b67a5f0
08f6da6e655d19eb9078fbd7284594162e727d3f  1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b
```

Coinciden con el sobre, LOS DOS. Cardinales y líneas, también derivados por mí:

| magnitud | candidata (sobre) | candidata (FF) | gate (sobre) | gate (FF) |
|---|---|---|---|---|
| fuentes obligatorias | 79 | **79** | 80 | **80** |
| líneas obligatorias | 77679 | **77679** | 77941 | **77941** |
| árbol | fe0aa25d…3005e35 | **fe0aa25d7c67a2b8269e60be5e1ba91fc3005e35** | 137783c9…1f67964 | **137783c97f83a545939558caec626258f1b67964** |

### §0.2 · Obligación 2 — EL MANIFIESTO EN EL COMMIT DEL GATE

```console
$ git show 08f6da6e...:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md | sha256sum
f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff  -
```
Coincide. Lo leo del commit, nunca del árbol de trabajo.

### §0.3 · Obligación 4 — LAS DOS SUPERFICIES DE DIFERENCIA

El sobre publica 2 rutas en que difieren los UNIVERSOS, y ADVIERTE que ésa no es la superficie
en que difieren los ÁRBOLES. La derivo:

```console
$ git diff --name-only f8fc037a998316081a7e9b9563398d118982ce60 08f6da6e655d19eb9078fbd7284594162e727d3f
docs/evolucion/00-INDICE.md
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md
kernel/operativo/pruebas/evidencia/fuentes-salida.txt
kernel/operativo/pruebas/evidencia/negativos-salida.txt
kernel/operativo/pruebas/evidencia/referencias-salida.txt
```

**5 rutas en los árboles, 2 en los universos.** El sobre lo dice por adelantado y da el comando exacto
para obtener la otra: el sobre es honesto aquí. Las 3 rutas extra son evidencia de pruebas, fuera del
universo obligatorio. Anoto que el commit del gate TOCA evidencia de pruebas, no sólo el manifiesto:
lo verifico en §2 al examinar la fila del propio derivador.

### §0.4 · Obligación 5 — EL EMISOR Y EL DERIVADOR, DE LOS DOS COMMITS

```console
$ git show f8fc037a...:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum
7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad
$ git show 08f6da6e...:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum
7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad
$ git show f8fc037a...:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum
4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996
$ git show 08f6da6e...:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum
4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996
```
Los cuatro coinciden con el sobre.

### §0.5 · Obligación 6 — LA SEDE CANÓNICA DEL OWNER

```console
$ git show f8fc037a...:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
$ git show 08f6da6e...:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
$ ... | awk '/^# /{p = ($0 ~ /^# `O17`/)} p' | sha256sum
0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125
$ ... O18   ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
$ ... O19   cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8
```
Los cinco coinciden. La sede es byte-idéntica en los dos commits, como el sobre declara.

### §0.6 · Obligación 3 — CADA FILA DECLARA UN ÁRBOL

Se cumple en §2. Anticipo el estado del árbol de trabajo del repositorio auditado en el momento
en que empiezo:

```console
$ git -C /home/jose/ads-kernel status --porcelain    # vacío
$ git -C /home/jose/ads-kernel rev-parse HEAD
08f6da6e655d19eb9078fbd7284594162e727d3f
$ git -C /home/jose/ads-kernel rev-parse --abbrev-ref HEAD
fix/f4c-perimetro-por-naturaleza-20260831
```

**HECHO DE MÉTODO, que registro y valoro en §7:** la rama de trabajo local
`fix/f4c-perimetro-por-naturaleza-20260831` está EN el commit del gate `08f6da6e`. Es decir, el
coordinador confirmó el commit del gate en la rama que se somete a revisión. Bajo `DD-20`/`Z3`
—que leo íntegra antes de clasificar, §3— eso es el acto ordinario del coordinador y NO un
privilegio. Lo dejo anotado, no lo convierto en hallazgo.

**VEREDICTO DEL §0: EL SOBRE REPRODUCE ÍNTEGRO. SUS SEIS OBLIGACIONES ESTÁN CUMPLIDAS POR MÍ.
LOS BLOQUES EMBEBIDOS SON EL MISMO FICHERO. EL GATE NO ES INVÁLIDO POR ESTA VÍA.**

---

## §1 · MI MANIFIESTO DE LECTURA, Y LAS DOS RESTAS

### §1.1 · Lo que YO he leído, y de qué árbol

Salvo indicación en contra leo del **COMMIT CANDIDATO** `f8fc037a…ce60`, que el §2 del
manifiesto declara «el objeto que este gate juzga», con `git show <commit>:<ruta>`.

| ruta | árbol | líneas | SHA-256 recalculado por mí | qué leí |
|---|---|---|---|---|
| `INFORME-S1.md` (fuera del repo) | — | 1400 | — | **ÍNTEGRO** |
| `INFORME-S2.md` (fuera del repo) | — | 1169 | — | **ÍNTEGRO** |
| `SOBRE-7.txt` (fuera del repo) | — | 196 | `dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2` | **ÍNTEGRO** |
| `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md` | **GATE** | 260 | `f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff` | **ÍNTEGRO** |
| `docs/evolucion/27-SEXTO-GATE-DE-CERTIFICACION-F4C.md` | candidata | 3946 | `d81b56366e5062ffe0abcd55ba2ef52ddbc3fadf073ea5a280e6cfc15b87ef26` | **ÍNTEGRO** — es MI fila (fila 3, «los tres · DESPUÉS de las demás fuentes») |
| `docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md` | candidata | 4526 | `e2c34215d92937fb467b1ffdb4e6654f66198ead4dac8128c411469bf86c297e` | su índice, §5, §6.4 y las 22 filas `DD` — **derivadas, no leídas íntegras**, y lo declaro |
| `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | candidata | 4812 | `c0b2ec09a5a6530ebfca6229879b4f12c83792874bb22c48ab7cba2b37d15ab4` | «El criterio del gate siguiente» + `DD-20` + `DD-19` (L3482-3600) · el PARTE (L3744-3825) · el bloque de estado (L884-1168) · la clasificación `C-L` (L2175-2205) · L3640-3655. **NO íntegro** |
| `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | candidata | 11708 | `82aca794e824a6ddca2aefc3808908d08ddd1871d4c4f1750d5d232f7ee33b69` | §2.6.7 L1735-1790 · `C-L.5` L11535-11560 · barridos. **NO íntegro** |
| `docs/evolucion/00-INDICE.md` | **los dos** | 233 / 235 | `89b74fcc…1567` / `7523cc25…` | L91-101, L93 y L94 byte a byte. **NO íntegro** |
| `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | candidata | 1330 | `cd4851915b4ffdc1c049f6c9aafb57d7ada358a829c1f00f27cb43f54c6c1bb3` | L1020-1058 y L1174-1194. **NO íntegro** |
| `…/verificacion/comprobar-correccion-gate-de-cierre.py` | candidata | 3957 | `22c454e7b090ff4e1962a36eea6c304e874c50a98a9f2c501c02f1644907f664` | L120-135 · L338-372 · L1915-1945 · L3105-3210. **NO íntegro** — pero lo **EJECUTÉ** 25 veces |
| `…/verificacion/derivar-universo-obligatorio.py` | candidata | 798 | `7d72b061f660bc627c7956a55f40fed301548f77f067857f807fac1afca7a9ad` | L166-205 · L722-748. **NO íntegro** — **EJECUTADO** |
| `…/verificacion/emitir-sobre-de-ancla.py` | candidata | 725 | `4354999a281cfadce0f5458394268626c54fb1975a1e340e0abdd3b867fc4996` | L232-244 · L292-302. **NO íntegro** |
| `…/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | candidata | 652 | `7876a2bb81b38c764d1bec924e972fb15df30d78058ef299c8adeff087a14255` | §18 y §19 (L597-625). **NO íntegro** |
| `…/verificacion/README.md` | candidata | 386 | `6c5064a31261cc0672698833a62e9cdf40d85d42a809b08d15fe1b86d0a92065` | la fila `G-29` (L244) y las vecinas. **NO íntegro** |
| `docs/owner/ADS-OWNER-RESOLUCIONES.md` | **los dos** | — | `db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a` | los tres bloques por DIGEST (obligación 6) |

**DECLARO CONTRA MI PROPIO INTERÉS:** el manifiesto me asigna **UNA** fila —la 3, el documento
27— y la he leído **ÍNTEGRA**. Todo lo demás lo he abierto **para reproducir**, acotado a la
línea que cada afirmación necesita, y lo digo fuente a fuente arriba. **No declaro leído
íntegro nada que no lo esté.**

### §1.2 · LA PRIMERA RESTA · `OBLIGATORIO − ASIGNADO`, derivada por mí

```console
$ grep -oE '^\| [0-9]+ \| `[^`]+`' MANIF7.md | sed 's/.*`\(.*\)`/\1/' | LC_ALL=C sort -u > filas.txt
$ wc -l < filas.txt                                                    79
$ grep -cE '^\| [0-9]+ \| `' MANIF7.md      # el comando que el propio §6 publica
79
$ (universo derivado del ÁRBOL DE LA CANDIDATA, materializado con la receta) → univ-cand.txt
$ wc -l < univ-cand.txt                                                79
$ comm -23 univ-cand.txt filas.txt          # OBLIGATORIO − ASIGNADO   (vacío)
$ comm -13 univ-cand.txt filas.txt          # ASIGNADO − OBLIGATORIO   (vacío)
```

**`OBLIGATORIO − ASIGNADO = ∅` sobre el árbol de la CANDIDATA, EN LAS DOS DIRECCIONES.**
No es «0 fuentes»: es **igualdad de conjuntos**, ruta a ruta.

```console
$ (universo del ÁRBOL DEL GATE) → univ-gate.txt ;  wc -l                80
$ comm -23 univ-gate.txt filas.txt
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md
$ comm -13 univ-gate.txt filas.txt                                     (vacío)
```

**Sobre el árbol del GATE la única fuente sin fila es EL PROPIO MANIFIESTO**, que es la
exención de PUNTO FIJO que `DD-19` fija y que el §6 declara «cubre a ESTE fichero y a NINGÚN
OTRO». **NO HAY NINGUNA OTRA**, y el §6 me encargaba expresamente decirlo si la hubiera.
**`EE-02` NO REINCIDE.**

Y las 79 filas, contrastadas por mí contra el árbol que su §2 declara:

```console
$ (para cada una de las 79 filas: git show <cand>:<ruta> | sha256sum  y  | wc -l)
DISCREPANCIAS contra el ARBOL DE LA CANDIDATA: 0
DISCREPANCIAS contra el ARBOL DEL GATE:        1
  fila 1  docs/evolucion/00-INDICE.md: lineas 235 vs 233 | sha 7523cc2540f7 vs 89b74fcc16f4
$ (suma de líneas)  §4 = 29117   §5 = 48562   TOTAL = 77679  = las LINEAS OBLIGATORIAS del sobre
```

La única discrepancia es la que **el manifiesto §6 anuncia** y **el sobre publica**. No es
hallazgo. **La fila 8 —el propio derivador, la que `U-02` y `X-06` falsearon dos gates
seguidos— casa contra los DOS árboles: 798 líneas y `7d72b061…fca7a9ad`. NO REINCIDE.**

### §1.3 · LA SEGUNDA RESTA · `ASIGNADO − LEÍDO`, derivada por mí sobre los DOS manifiestos

```text
`S1`  filas 2 (L1-L5200) · 3 · 5 · 6 · 7 · 8 · 9 · 10 · 11
      5200 + 3946 + 652 + 386 + 3957 + 798 + 725 + 278 + 292      ASIGNADO  16234
      unión de rangos declarados en su §1                          LEÍDO     16234
                                                         ASIGNADO − LEÍDO   0

`S2`  filas 1 · 2 (L5201-final) · 3 · 4 · 12
      233 + 6508 + 3946 + 4812 + 1330                              ASIGNADO  16829
      unión de rangos declarados en su §1.2                        LEÍDO     16829
                                                         ASIGNADO − LEÍDO   0

COBERTURA DEL DOCUMENTO 11, que es donde un reparto por rangos puede dejar un hueco
      S1 L1–L5200  +  S2 L5201–L11708  =  11708  de 11708           SIN HUECO Y SIN SOLAPE

TOTAL DE LAS 12 FILAS DE LECTURA         29117 líneas   = el §4 del manifiesto, DERIVADO
```

**`ASIGNADO − LEÍDO = ∅` para los dos revisores, y la unión de sus rangos cubre las doce filas
de lectura sin un solo hueco.** Lo verifiqué además **materialmente**, y no sólo por
declaración: cada hallazgo que sostengo cae DENTRO del rango que su autor declara leído
—`S1-07` en L1782 (rango `S1`), `S2-01`/`S2-02` en `00-INDICE` (lote `S2`), `S2-03`/`S2-04` en
el `CHECKPOINT` (lote `S2`), `S2-05` en `DECISIONES` (lote `S2`), los seis del instrumento en el
lote `S1`—. **Ninguno de los catorce se apoya en una fuente que su autor no tuviera asignada.**

### §1.4 · LO QUE ESTAS DOS RESTAS **NO** DICEN, y lo digo antes de usarlas

```text
NO DICEN que el documento 11 lo haya leído un solo ojo: son DOS mitades y DOS lectores, y una
         contradicción a caballo de L5200 es invisible para los dos. Es `S1-09`.
NO DICEN que yo haya leído íntegras las trece fuentes que abrí: sólo el documento 27 lo está.
NO DICEN que los revisores leyeran de verdad lo que declaran. Lo que SÍ verifiqué es que sus
         SHA-256 recalculados coinciden con el árbol, que sus rangos cubren lo asignado, y que
         cada afirmación suya cae dentro de su rango — que es todo lo que un adjudicador puede
         medir sin repetir la lectura entera, y lo digo sin adornarlo.
SÍ DICEN que la COBERTURA de este gate cierra a ∅ en las dos restas y en las dos direcciones,
         que la aritmética del §6 DERIVA en vez de copiarse, y que ninguna fuente obligatoria
         quedó fuera del reparto por otra razón que la exención de punto fijo.
```

---

## §2 · REPRODUCCIÓN, HALLAZGO A HALLAZGO

**Banco de pruebas.** `git clone /home/jose/ads-kernel <scratchpad>/ff/repo-FF`, y de él un
`base` en `git checkout -B atk 08f6da6e…`, copiado a un directorio nuevo por cada ataque.
**Ni un byte del repositorio auditado.** Línea base del banco, medida por mí:

```console
$ git status --porcelain                                          (vacío)
$ python3 …/comprobar-correccion-gate-de-cierre.py | grep -E '[0-9]+/[0-9]+ comp'
38/38 comprobaciones en verde
$ python3 …/comprobar-correccion-gate-de-cierre.py >/dev/null ; echo $?        0
$ python3 …/derivar-universo-obligatorio.py --rutas | wc -l                   80
$ (RECETA DEL SOBRE)  1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b  = ANCLADO
```

---

### `S1-01` · **SOSTENIDO** · BLOQUEANTE · el décimo árbol por la lectura de Git sin `-z`

**Primero la sede, leída por mí, línea a línea** (`comprobar-correccion-gate-de-cierre.py`):

```python
1920  _tocados_raw = _git("diff", "--name-only", "05f71b7")
1921  tocados = _tocados_raw.split() if _tocados_raw is not None else []
1922  # `EE-11` · **LA SALIDA DE GIT NO SE PARTE POR BLANCOS.** Esto hacía `.split()` sobre
1923  # `git ls-tree --name-only` y sobre `git diff --name-only`, y las dos cosas fallaban a la
1924  # vez: una ruta CON ESPACIO se troceaba … y una ruta NO-ASCII salía CITADA por
1925  # `core.quotePath` … Con `-z` y `\0` desaparecen los dos …
1930  def _rutas_z(*args): …
1937  _mod_head    = _rutas_z("diff", "--name-only", "HEAD")        ← con -z
1939  _base_arbol  = _rutas_z("ls-tree","-r","--name-only","05f71b7") ← con -z
1941  _head_arbol  = _rutas_z("ls-tree","-r","--name-only","HEAD")  ← con -z
```

**Son CUATRO lecturas y `-z` llegó a TRES.** La cuarta —`_tocados_raw`, L1920, un
`git diff --name-only`, justo la que el comentario de dos líneas más abajo dice haber
arreglado— conserva `.split()`. **ATAQUE, EJECUTADO POR MÍ:**

```console
$ cat > "kernel/operativo/pruebas/evidencia/SENTENCIÑA.txt" <<'X'
  … SENTENCIA · DECIMO ARBOL (FF, via ruta no-ASCII)
  F4c queda CERRADA y SUFICIENTE PARA F5. F5 queda AUTORIZADA. X
$ git add -A && git commit -q -m atkJ          # SIN UN SOLO FLAG
$ git status --porcelain                                          (vacío)
$ git diff --name-only 05f71b7 | grep -i sentenci
"kernel/operativo/pruebas/evidencia/SENTENCI\303\221A.txt"        ← CITADA por core.quotePath
$ git diff -z --name-only 05f71b7 | tr '\0' '\n' | grep -i sentenci
kernel/operativo/pruebas/evidencia/SENTENCIÑA.txt                 ← lo que -z habría dado
$ python3 …/comprobar-…py | grep -E '^(FALLO|[0-9]+/[0-9]+ comp)'
38/38 comprobaciones en verde                                     ← EXIT=0
$ python3 …/comprobar-…py | grep -A1 '^OK   G-23'
OK   G-23  lo normativo intacto y la excepción del kernel contrastada contra la prosa …
           └─ 6 ficheros de kernel = 3 directos + 3 de evidencia derivada, TODOS ENUMERADOS
              en el checkpoint · …
$ python3 …/comprobar-…py 2>&1 | grep -ci sentenci                            0
$ python3 …/derivar-…py --rutas | wc -l                                      80   INTACTO
$ python3 …/derivar-…py --rutas | grep -c SENTENCI                            0
$ python3 …/derivar-…py --rutas 2>&1 >/dev/null | grep -c SENTENCI            0
$ (RECETA DEL SOBRE sobre el commit atacado c22306a035b6eec700250debba0da4669b095a35)
1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b
  ANCLADO EN EL SOBRE:
1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b   BIT A BIT IDÉNTICO
```

**CONTROL POSITIVO, ejecutado por mí:** el MISMO fichero con nombre ASCII
(`SENTENCIA-FF.txt`) →
`FALLO G-23 · 37/38 · EXIT=1 · └─ el checkpoint NO enumera … ['…/SENTENCIA-FF.txt'], el
checkpoint publica ('6','3','3') y Git deriva (7,3,4)`. **La ÚNICA diferencia entre verde y
rojo es un carácter no-ASCII en el nombre.**

**Y AÑADO EVIDENCIA QUE `S1` NO TRAE, y agrava el hallazgo.** El comentario de `EE-11` y la
fila del `CHECKPOINT`:3790 afirman que `-z` hace desaparecer **LAS DOS** formas de fallo. Medí
la otra —la ruta CON ESPACIO— sobre `_tocados_raw`:

```console
$ cat > "kernel/operativo/pruebas/evidencia/SENTENCIA FINAL.txt" <<'X' … X
$ git add -A && git commit -q -m sp2 ; git status --porcelain      (vacío)
$ python3 …/comprobar-…py | grep -A1 '^FALLO G-23'
FALLO G-23 …
   └─ el checkpoint NO enumera ficheros del kernel tocados:
      ['kernel/operativo/pruebas/evidencia/SENTENCIA'],  ← RUTA QUE NO EXISTE
      el checkpoint publica ('6','3','3') y Git deriva (7,3,4)
37/38 comprobaciones en verde
```

**El `.split()` trocea la ruta y el instrumento NOMBRA UN FICHERO QUE NO EXISTE** — que es,
literalmente, «el diagnóstico FALSO» que la fila `EE-11` del parte declara eliminado. **Las DOS
formas de fallo que `EE-11` dice haber cerrado siguen abiertas en `_tocados_raw`: una en
silencio y la otra con un diagnóstico falso.**

**QUÉ SE SIGUE.** Es el DÉCIMO ÁRBOL: alcanza el commit con `git add -A && git commit` sin un
flag · `git status` vacío · **38/38 · EXIT=0** · fuera del universo · sin fila ni revisor ·
**digest del sobre bit a bit el anclado** · silencio total. Y añade que **`G-23` publica un
recuento FALSO —«6 … todos enumerados»— sobre SIETE, y lo firma en verde**: la familia `T-05`,
aquí agravada porque **ni siquiera lo nombra**.

**LA CONTINGENCIA QUE MIDO Y QUE `S1` SÓLO DECLARA:**

```console
$ git config core.quotePath false ; python3 …/comprobar-…py | grep -E '^(FALLO|[0-9]+/)'
FALLO G-23 …
37/38 comprobaciones en verde
```

**El ataque depende de `core.quotePath`, cuyo valor POR DEFECTO es `true`.** El instrumento
**ni lo fija ni lo comprueba**, y los dos revisores y yo corrimos con el valor por defecto.
Eso no rebaja el hallazgo: lo precisa, y añade que la corrección de la batería depende hoy de
una variable de entorno que ninguna comprobación ancla. **BLOQUEANTE, clase `A`.**

---

### `S1-02` · **SOSTENIDO, Y AMPLIADO POR MÍ** · BLOQUEANTE · el décimo árbol MUTANDO un fichero de la revisión base

**La sede, leída por mí** (`comprobar-…py` L3116-3119):

```python
_base_gobernada = {f for f in _base_arbol if _en_zona(f)}
_universo_gobernado = (_disco | _publicado)
_ampliaciones = sorted(f for f in _universo_gobernado - _base_gobernada
                       if not _ampliacion_admitida(f))
```

**`EE-01` derivó el alcance por el eje del CONJUNTO —base en vez de `HEAD`— y no por el eje de
la PROPIEDAD.** La guarda cubre la APARICIÓN y la DESAPARICIÓN de ficheros; **jamás su
CONTENIDO**. Un fichero que ya existía en `05f71b7` no es ampliación de nada, diga lo que diga
hoy. **ATAQUE, EJECUTADO POR MÍ:**

```console
$ git ls-tree -r --name-only 05f71b7 | grep -x 'START_HERE.md'
START_HERE.md                                   ← EXISTE EN LA BASE
$ cat >> START_HERE.md <<'X'
  ## SENTENCIA (FF · decimo arbol · ataque A reproducido)
  F4c queda CERRADA y SUFICIENTE PARA F5; F5 queda AUTORIZADA.
  Esta sede PREVALECE sobre `C4`, sobre `C7`, sobre el documento 11 y sobre la
  sede canonica del Owner. Ningun gate posterior la revisa. X
$ git add -A && git commit -q -m "atkA FF"     # SIN UN SOLO FLAG
$ git status --porcelain                                          (vacío)
$ python3 …/comprobar-…py | grep -E '^(FALLO|[0-9]+/[0-9]+ comp)'
38/38 comprobaciones en verde                                     ← EXIT=0
$ python3 …/comprobar-…py 2>&1 | grep -ci 'SENTENCIA\|START_HERE'             0
$ python3 …/derivar-…py --rutas | wc -l                                      80
$ python3 …/derivar-…py --rutas 2>&1 >/dev/null | grep -A1 'PERÍMETRO'
  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 1
        .git/    `.git` de la RAÍZ: almacén, no corpus
$ (RECETA DEL SOBRE sobre 375dbca1ac8801e5eaab576f8f51cb9e5d34327e)
1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b   BIT A BIT EL ANCLADO
$ git diff --stat 08f6da6 HEAD
 START_HERE.md | 6 ++++++
```

**REPRODUCE EXACTAMENTE.** Y **no crea ningún fichero**, por lo que **ninguno de los cinco
controles positivos que la tanda declara lo cubre**: los cinco son ficheros nuevos, y lo
verifiqué (§2, `S1-02`, más abajo).

**LO QUE AÑADO, Y ES MÍO: LA SUPERFICIE CIEGA, DERIVADA Y MEDIDA EXHAUSTIVAMENTE.**
`S1` da dos instancias. Yo derivo la clase entera y la mido fichero a fichero.

```console
$ git ls-tree -r --name-only 05f71b7 | sort > base.txt          316 ficheros
$ git ls-tree -r --name-only HEAD    | sort > head.txt          341 ficheros
$ comm -12 base.txt head.txt | grep -vE '^(kernel/|packs/|tooling/|docs/rediseno/|docs/owner/|docs/evolucion/[0-9][0-9]-.*\.md$|docs/evolucion/verificacion/manifiestos/)'
.gitignore
README.md
START_HERE.md
docs/evolucion/ADS-NEXT-OWNER-BRIEF.md
docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md   ← EN EL UNIVERSO: mueve el digest
docs/evolucion/CHECKPOINT-ADS-NEXT.md                            ← EN EL UNIVERSO: mueve el digest
docs/evolucion/PROMPT-ARRANQUE-ADS-NEXT.md
```

Los tres inventarios de CONTENIDO son `G-22` (`docs/evolucion/NN-*.md` + `manifiestos/` +
`docs/owner/`), `G-23` (`kernel/` + `docs/rediseno/`) y `G-30` (`kernel/`,`packs/`,`tooling/`
**sólo** con `.md .yaml .yml .py .sh .toml`). **La RAÍZ del repositorio no está en ninguno.**
Medí **una por una, con un clon por fichero**, todas las candidatas:

| ruta | batería tras `git add -A && git commit` | `porcelain` | digest del sobre |
|---|---|---|---|
| `.gitignore` | **38/38** | vacío | **= ANCLADO** |
| `README.md` | **38/38** | vacío | **= ANCLADO** |
| `START_HERE.md` | **38/38** | vacío | **= ANCLADO** |
| `docs/evolucion/ADS-NEXT-OWNER-BRIEF.md` | **38/38** | vacío | **= ANCLADO** |
| `docs/evolucion/PROMPT-ARRANQUE-ADS-NEXT.md` | **38/38** | vacío | **= ANCLADO** |
| `kernel/operativo/pruebas/evidencia/fuentes-salida.txt` | **38/38** | vacío | **= ANCLADO** |
| `kernel/operativo/pruebas/evidencia/negativos-salida.txt` | **38/38** | vacío | — |
| `kernel/operativo/pruebas/evidencia/referencias-salida.txt` | **38/38** | vacío | — |
| `kernel/VERSION` | 37/38 | vacío | — |
| las OTRAS DIEZ evidencias del kernel (`arranque`, `contratos`, `evidencia`, `integridad`, `lint`, `packs`, `prompts`, `recuentos`, `versiones`, `workspace`) | 37/38 cada una | vacío | — |

```console
$ for f in <las 13 evidencias del kernel>; do (clon nuevo; sed -i '5i SENTENCIA FF…' "$f";
    git add -A && git commit -q -m p; python3 …/comprobar-…py | grep -oE '^[0-9]+/[0-9]+ comp'); done
arranque 37/38 · contratos 37/38 · evidencia 37/38 · fuentes 38/38 · integridad 37/38 ·
lint 37/38 · negativos 38/38 · packs 37/38 · prompts 37/38 · recuentos 37/38 ·
referencias 38/38 · versiones 37/38 · workspace 37/38
```

**LA SUPERFICIE CIEGA ES DE OCHO FICHEROS, EXACTAMENTE, Y LA HE MEDIDO ENTERA:**

```text
.gitignore · README.md · START_HERE.md · docs/evolucion/ADS-NEXT-OWNER-BRIEF.md ·
docs/evolucion/PROMPT-ARRANQUE-ADS-NEXT.md · kernel/operativo/pruebas/evidencia/
{fuentes,negativos,referencias}-salida.txt

Los ocho: existían en la revisión base · ningún inventario mira su contenido · están FUERA
del universo obligatorio. Reescribirlos con cualquier texto deja `porcelain` VACÍO, la batería
en 38/38 con EXIT=0, y el DIGEST DEL SOBRE BIT A BIT EL ANCLADO.
Y las tres últimas son, precisamente, las TRES que el commit del gate reejecuta por `DD-17`.
```

**QUÉ SE SIGUE.** Es el DÉCIMO ÁRBOL **por la otra puerta, y no necesita crear un fichero**.
El README dice de `G-29` que gobierna «el repositorio ENTERO menos `.git` y el bytecode» y
`G-29` gobierna **sólo su TOPOLOGÍA**. Es «se cierran instancias y no clases» **un EJE más
allá** en vez de una zona más allá, dentro del remedio que decía haberlo curado.
**BLOQUEANTE, clase `A`.**

---

### `S1-03` · **SOSTENIDO** · GRAVE · la SEGUNDA guarda de `G-29`, inerte tras confirmar

**La sede, leída por mí** (`comprobar-…py` L3190-3200):

```python
publicado_marca = _git("grep","-l","```yaml "+marca,"HEAD","--",".", …)
base_marca = {l.split(":",1)[1] for l in publicado_marca.split("\n") if ":" in l}
nuevas = sorted(_sedes_disco[marca] - base_marca)
```

**`base_marca` se deriva de `HEAD`.** Un fichero confirmado ya está dentro, y `nuevas` sale
vacío. **MEDIDO POR MÍ:**

```console
$ printf '\n## SEGUNDA SEDE DEL BLOQUE CANONICO (FF)\n\n```yaml ads:proceso\nid: sentencia\n```\n' >> START_HERE.md
--- SIN COMMITEAR ---
FALLO G-29 └─ SEGUNDA SEDE del bloque canónico `ads:proceso`: ['START_HERE.md'] …
37/38 comprobaciones en verde
--- git add -A && git commit  (SIN UN SOLO FLAG) ---
$ git status --porcelain                                          (vacío)
38/38 comprobaciones en verde                                     EXIT=0
```

**REPRODUCE EXACTAMENTE.** Y añado la agravante que la reproducción documental me da:
**`EE-01` nombró esta sede en su propia fila.** Doc 27 §3.2, fila 1: «sede: batería L3038 **y
L3107-3118** · título de `G-29` L3120 · README L244» — **`L3107-3118` ES la unicidad 2**. Y
`R1`, en su `RF-4` del sexto gate (doc 27 L1415): «*Son **dos** guardas de `G-29`, no una, y
las dos miden contra `HEAD`*». **El remedio se aplicó a UNA de las DOS sedes que el propio
hallazgo enumera**, y el título —que es UNO para las tres sub-guardas— se ENSANCHÓ a
«CONFIRMADO O NO», y el README L244 lo repite. **La segunda mitad del remedio `EE-01` —«que el
título de `G-29` y la fila L244 del README digan lo que el código hace»— no sólo no se cumple:
se incumple MÁS que antes, porque la promesa creció y el código no.**
**GRAVE, clase `A`.**

---

### `S1-04` · **SOSTENIDO** · GRAVE · el derivador promete publicar todo lo que excluye, y sólo lo hace en dos zonas

**Las dos sedes de la promesa, leídas por mí:** derivador L173-175 —«**Y mientras algo quede
fuera, se PUBLICA con su ruta** … Una exclusión silenciosa es la puerta»— y la docstring de
`_excluidos()` L738-740 —«*Mientras algo se excluya, se dice cuál y por qué: una exclusión
silenciosa es el octavo árbol*»—. **Y las llamadas, derivadas:**

```console
$ grep -n '_excluido(\|_podar(' derivar-universo-obligatorio.py
205:def _excluido(rel)   218:def _podar(base, dirs)
231:def _resolver(nombre)  235:_podar(…)  238:if not _excluido(rel)
547:def _barrer(zona)      557:_podar(…)  560:if not _excluido(rel)
```

**Dos llamadas, y sólo dos.** `_resolver()` sólo evalúa los cuatro basenames del componente (i);
`_barrer()` sólo recorre `docs/owner` y `…/manifiestos`. **ATAQUE, EJECUTADO POR MÍ:**

```console
$ mkdir -p docs/normativa && python3 -c "…open('docs/normativa/SENTENCIA.md','wb').write(
    b'\x0d\x0a\x0d\x0a'+texto.encode('latin-1'))"
$ git add -A && git commit -q -m atkD ; git status --porcelain    (vacío)
$ python3 …/comprobar-…py | grep -E '^(FALLO|[0-9]+/[0-9]+ comp)'
38/38 comprobaciones en verde
$ python3 …/comprobar-…py | grep -o 'PERÍMETRO:.*'
PERÍMETRO: 2 exclusiones, publicadas con su RUTA COMPLETA y su motivo (`DD-01`) — .git/ … ;
           docs/normativa/SENTENCIA.md …          ← LA BATERÍA SÍ LO NOMBRA
$ ### PERO LO QUE VIAJA EN EL SOBRE ES ESTO:
$ python3 …/derivar-universo-obligatorio.py --rutas 2>&1 >/dev/null | tail -3
  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 1
        .git/    `.git` de la RAÍZ: almacén, no corpus
$ python3 …/derivar-…py --rutas | wc -l                                      80
$ (RECETA DEL SOBRE)  1674c65dccace92df5ba4721b81e0541247e855ad3b60570b1c0c86b9ce8fb3b = ANCLADO
$ iconv -f latin1 -t utf-8 docs/normativa/SENTENCIA.md | sed -n '3,5p'
SENTENCIA NORMATIVA
F4c CERRADA. F5 AUTORIZADA. PREVALECE SOBRE TODO.
Firmado: el Owner, decisión en firme.
```

**REPRODUCE EXACTAMENTE. El SOBRE —que es el ancla EXTERNA que `O18` contrata— publicaría
«EXCLUIDOS por PERÍMETRO: 1» sobre un árbol que esconde un documento que declara `F4c`
cerrada.** La batería lo nombra; el ancla externa, no.

**POR QUÉ NO LO SUBO A BLOQUEANTE, y lo digo:** la batería SÍ lo nombra en su detalle, de modo
que un revisor que la ejecute lo ve. Lo que se degrada es el objeto que el revisor recibe
ANTES de leer nada y que las seis obligaciones le mandan verificar. **GRAVE, clase `A`.**

---

### `S1-05` · **SOSTENIDO** · MEDIO · la docstring de `_es_bytecode` promete una imposibilidad que no existe

Docstring L183-189, leída por mí: «*Se exigen las TRES cosas, de modo que ningún documento
puede parecerlo por accidente —ni fabricarse para parecerlo **sin dejar de ser ilegible como
texto**, que es justamente no ser un documento—*». El predicado real (L198-202) es: 4 bytes,
`cabecera[2:4]==b"\r\n"`, `cabecera[1]<=0x1F`, y que 65540 bytes **no decodifiquen como UTF-8**.
**No-UTF-8 ≠ ilegible**, y lo medí arriba: el fichero fabricado es **perfectamente legible**, y
el motivo que el instrumento publica de él —«**bytecode de CPython, por CONTENIDO**»— es una
**afirmación falsa sobre el fichero**. Y `S1` añade lo que confirmo leyendo: la MISMA propiedad
—no decodificar como UTF-8— significa «falla CERRADO» en `_leer` (`EE-09`, L138-148) y «no es
corpus» en `_es_bytecode`, a cuarenta líneas, y lo que decide cuál se aplica son **cuatro
bytes de prefijo**. **MEDIO, clase `A`.** Sexta condición de `O18`.

---

### `S1-06` · **SOSTENIDO** · MEDIO · el desajuste de `EE-17` dice ROJO y sólo imprime

**Las dos sedes, leídas por mí.** Comentario L130-131: «*el TÍTULO se CONTRASTA contra ella:
si divergen en un solo identificador, **es ROJO y se nombra**»*. Fila `EE-17` del parte
(`CHECKPOINT` L3795): «*si divergen en un identificador, **se dice**»*. Y el código, L355-362:
`_desajuste` se calcula y se **imprime**; `verde` se calcula sobre `RES` y el retorno es
`0 if verde == len(RES)`. **`_desajuste` no llama a `check()`.** MEDIDO POR MÍ:

```console
$ (título de G-27 → «… «los cinco conceptos» (falla CERRADO sin git)», y G-27 NO está en _EXIGEN_HISTORIA)
--- SIN COMMITEAR ---  FALLO G-34 (instrumental MODIFICADO y NO DECLARADO) · 37/38
--- git add -A && git commit ---
$ git status --porcelain                                          (vacío)
38/38 comprobaciones en verde
ALCANCE · DESAJUSTE (`EE-17`): ['G-27'] — el TÍTULO y la PROPIEDAD declarada no coinciden …
$ EXIT=0
```

**REPRODUCE EXACTAMENTE.** El comentario dice ROJO; el código dice impreso. Y **la misma
inercia-tras-confirmar** que `EE-01` dice haber cerrado: sin commitear sale rojo por `G-34`
—no por el desajuste—; confirmado, `G-34` calla y el desajuste es una línea decorativa.
**MEDIO, clase `A`.**

---

### `S1-07` · **SOSTENIDO** · MEDIO · el cardinal `46` vivo en la sede DEFINITORIA del contrato de `F6`

```console
$ grep -cE '^\| `X[0-9]{2}` \|' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md     47
$ (ids únicos)                                                                 47
$ grep -n 'Cuarenta y seis\|el cardinal NO se escribe aquí' <doc 11>
1739:> **Tantas filas físicas como identificadores únicos, y el cardinal NO se escribe aquí: se
1742:>  QUINTO GATE**: esta frase escribía «cuarenta y seis», y `X63` la dejó caducada en el acto.
1782:> **Ninguna se ha ejecutado.** Cuarenta y seis filas escritas es el contrato de lo que F6 …
```

**Cuarenta líneas separan la nota que declara ese cardinal CADUCADO de la frase que lo escribe.**
Y el desglose que la sigue no cierra: `13+7+5+3+1 = 29`, más las 17 originales = **46**, no 47.

**VERIFIQUÉ QUE LA LÍNEA ES VIVA** —la valla ```` ```text ```` del bloque histórico va de L1758
a L1780, y la marca `[HISTÓRICO]` más cercana (L1772) muere dentro de ella—, **y que sobrevive
a la tanda**:

```console
$ for c in b27a761 98cdb7a f8fc037 08f6da6; do git show $c:<doc 11> | grep -c 'Cuarenta y seis filas escritas'; done
1  1  1  1
$ git diff --stat b27a761 f8fc037 -- <doc 11>
 docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | 36 +++++++++++++++++++++++++----
```

**La tanda TOCÓ el fichero 36 líneas y dejó el cardinal.** Es la CUARTA sede de la misma cifra:
`DD-13` la retiró de doc 11 L1739-1742 · `R2-07`→`EE-07` de `CHECKPOINT`:2344 · `R2-08`→`EE-12`
de `CHECKPOINT`:2907 · **y nadie volvió a la sede de la que `DD-13` la retiró, cuarenta líneas
abajo.** **MEDIO, clase `A`.**

---

### `S1-08` · **SOSTENIDO** · MENOR · «se usa UNA» y son DOS implementaciones

```console
$ sed -n '234,242p' emitir-sobre-de-ancla.py
def _lineas_de(crudo):
    """Líneas de un blob, con la MISMA fórmula que el derivador (`EE-16`)."""
    n = crudo.count(b"\n") ; if crudo and not crudo.endswith(b"\n"): n += 1 ; return n
$ sed -n '297,299p' emitir-sobre-de-ancla.py
# … dos implementaciones de la misma derivación acaban divergiendo … **Se usa UNA, y es la
# del derivador, que es la sede de las métricas del universo.**
$ grep -nE '^(import|from) ' emitir-sobre-de-ancla.py
argparse · datetime · hashlib · os · re · shutil · subprocess · sys · tempfile   ← NO importa el derivador
$ sed -n '726,733p' derivar-universo-obligatorio.py     # def metricas(rel): la MISMA fórmula, otra vez
```

**El remedio a «dos implementaciones divergen» fue escribir una TERCERA copia idéntica, no
crear una sede.** «Se usa UNA» es falso como está escrito; el riesgo que el comentario nombra
sigue exactamente donde estaba. **LATENTE** —hoy coinciden y no hay ficheros vacíos—, y por eso
**MENOR, clase `A`.**

---

### `S1-09` · **SOSTENIDO** · MENOR · el revisor que audita el derivador no tiene asignada la sede de la que el derivador deriva

```console
$ (manifiesto 7 §4 fila 2)  11-ARQUITECTURA-INTEGRADA.md · S1 L1-L5200 · S2 L5201-final
$ grep -n '^## `C-L\.5`' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md            11541
```

**`C-L.5`·`1bis` —la sede normativa del universo obligatorio, de la que el derivador LEE sus
cardinales— vive en L11541, en el rango de `S2`; y `S2` declara expresamente que NO auditó el
instrumento.** `S1` lo suplió **ejecutando** el derivador (falla cerrado si la sede no dice lo
que dice), que verifica el instrumento contra su sede pero **no verifica la sede**. Es del
APARATO del gate, no del objeto. **MENOR, clase `A`.** Y lo valoro más abajo (§7) como
observación de método.

---

### `S2-01` · **SOSTENIDO** · GRAVE · `EE-14` aplicado a medias, y la sede omitida es la que el adjudicador nombró por fichero y línea

**El remedio, leído por mí en el commit** (doc 27 L3896): «*Que **la proyección VIVA
(`00-INDICE.md` L93)** publique el desglose derivado de las filas del documento 26, **y** que
el error del documento inmutable se acote con una entrada en el `CORRIGENDUM`*». **DOS mitades.**

```console
$ for c in b27a761 f8fc037 08f6da6; do git show $c:docs/evolucion/00-INDICE.md | sed -n '93p' | sha256sum; done
aa99111e0ec72478a7af24b68927ed4c81a5537c588a5d3c14b8c256e65fb605
aa99111e0ec72478a7af24b68927ed4c81a5537c588a5d3c14b8c256e65fb605
aa99111e0ec72478a7af24b68927ed4c81a5537c588a5d3c14b8c256e65fb605
```

**BYTE-IDÉNTICA en los TRES árboles**, incluido `b27a761`, que es el que el gate anterior falsó.
Sigue publicando `**22 hallazgos: BLOQUEANTE 0 · GRAVE 12 · MEDIO 6 · MENOR 4**`. Y la
derivación —con el comando que **el propio `CORRIGENDUM` §18 publica**—:

```console
$ awk '/^\| \*\*`DD-[0-9]/{print}' docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md |
    grep -oE '\*\*(BLOQUEANTE|GRAVE|MEDIO ESTRUCTURAL|MEDIO|MENOR)\*\*' | sort | uniq -c
     12 **GRAVE**   1 **MEDIO ESTRUCTURAL**   4 **MEDIO**   5 **MENOR**      (22 filas)
$ sed -n '93p' 00-INDICE.md | grep -cE 'awk|grep |se deriva|remite'            0
$ git diff --stat b27a761 f8fc037 -- docs/evolucion/00-INDICE.md
 docs/evolucion/00-INDICE.md | 19 +++++++++++++++++--   (18 inserciones · 1 supresión, y NO tocan L93)
```

`MEDIO 6 · MENOR 4` **no lo da ninguna agregación de esas filas**: con `MEDIO ESTRUCTURAL`
dentro de MEDIO son `12·5·5`; separado, `12·4·1·5`. Y L93 **no lleva el comando ni remite**.

**Y LA AGRAVANTE, que verifico:** el `CORRIGENDUM` §18 —**escrito por esta misma tanda, en este
mismo commit**— cierra con la regla «*toda sede derivada que reproduzca ese desglose lo publica
**con el comando que lo deriva de las filas**, o remite*». **`00-INDICE.md`:93 es exactamente
esa sede derivada, y la incumple en el commit que escribe la regla.** Y la fila `EE-14` del
PARTE (`CHECKPOINT`:3792) declara como sede del remedio «`CORRIGENDUM` §18» **a secas**,
presentando la mitad (b) como el remedio entero. **GRAVE, clase `A`.**

---

### `S2-02` · **SOSTENIDO** · MEDIO · el comando que `EE-10` retira, publicado como vigente en la sede de al lado

```console
$ sed -n '94p' 00-INDICE.md | grep -oE '.{40}se cuenta con.{120}'
… una fila por identificador, y se cuenta con `awk '/^\| `(DD|BT)-[0-9]/{n++} END{print n}'
  docs/evolucion/CHECKPOINT-ADS-NEXT.md`. …
$ for c in b27a761 f8fc037; do git show $c:…00-INDICE.md | sed -n '94p' | sha256sum; done
e28a95d1d13b4cf8b2a3b847639c047edd4d1506324d0a7e863f16f3d98d0961   (los dos)
$ sed -n '3644,3650p' CHECKPOINT-ADS-NEXT.md
> > **PRECISADO por `EE-10` del SEXTO GATE.** El comando anterior contaba **filas de
> > cualquier tabla del fichero** con `awk '/^\| `(DD|BT)-[0-9]/{n++}'` … **contaba filas y
> > no identificadores distintos** … y **no acotaba la tabla** …
$ awk '/^\| `(DD|BT)-[0-9]/{n++} END{print n}' CHECKPOINT-ADS-NEXT.md              24   (el viejo)
$ grep -oE '^\| `(DD|BT)-[0-9]+`' CHECKPOINT-ADS-NEXT.md | sort -u | wc -l         24   (el nuevo)
```

**REPRODUCE.** La única otra ocurrencia del comando viejo (`CHECKPOINT`:3645) va **citada como
retirada**; en `00-INDICE.md`:94 vive **como el comando vigente**, con la fórmula «se cuenta
con», en una fila viva y byte-idéntica a la del árbol que el gate anterior falsó. **Hoy los dos
dan 24 por accidente: es LATENTE, y por eso MEDIO y no GRAVE.** Clase `A`.

---

### `S2-03` · **SOSTENIDO** · MEDIO · `based_on` reanclado en su preámbulo y no en su cuerpo

```console
$ sed -n '906,909p' CHECKPOINT-ADS-NEXT.md
   4  TODO EVENTO NUEVO —un gate devuelto, una resolución del Owner, una tanda aplicada—
      REANCLA `metodo`, `last_meaningful_event` y `based_on` EN EL MISMO COMMIT QUE LO REGISTRA
$ awk 'NR>=1051 && NR<=1136' CHECKPOINT | grep -o 'docs/evolucion/[0-9][0-9]-[^ `)]*\.md' | sort -u | tail -1
docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md
$ git ls-tree -r --name-only f8fc037 | grep -E '^docs/evolucion/[0-9][0-9]-.*\.md$' | sort | tail -2
docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md
docs/evolucion/27-SEXTO-GATE-DE-CERTIFICACION-F4C.md
$ grep -n '27-SEXTO-GATE' CHECKPOINT-ADS-NEXT.md            19 (cabecera) · 3757 (un comando)
```

**REPRODUCE. Faltan DOS documentos, no uno**: `R2-03` midió que faltaba el 26; hoy faltan el 26
**y** el 27. **El defecto EMPEORÓ mientras su remedio se declaraba aplicado.** Atenuante, que
verifico y digo: L1064-1066 declara que «*la enumeración de abajo se conserva por comodidad de
lectura*» y publica el comando que la deriva — pero esa cláusula **ya estaba en `8c9ca9c`** y no
impidió que `R2-03` cayera ni que `EE` lo sostuviera. **MEDIO, clase `A`.**

---

### `S2-04` · **SOSTENIDO, CON LA CIFRA MATIZADA POR MÍ** · MEDIO · un ordinal a mano sustituido por otro ordinal a mano

```console
$ sed -n '899,901p' CHECKPOINT-ADS-NEXT.md
   2  EL ÚLTIMO GATE Y SU DOCUMENTO NO SE ESCRIBEN A MANO. Se derivan con
          ls docs/evolucion/[0-9][0-9]-*.md | sort | tail -1
$ awk 'NR>=884 && NR<=1168 && /SEXTO GATE/ {print NR}' CHECKPOINT-ADS-NEXT.md
886 · 914 · 924 · 1051 · 1052 · 1155
$ ls docs/evolucion/[0-9][0-9]-*.md | sort | tail -1
docs/evolucion/27-SEXTO-GATE-DE-CERTIFICACION-F4C.md      ← el comando SÍ lo deriva
```

**REPRODUCE, y MATIZO LA CIFRA contra `S2`, porque el detalle importa.** De las **seis**
ocurrencias, **DOS son los campos que la regla 2 gobierna** —L914 `metodo:` «SEXTO GATE DE
CERTIFICACIÓN DEVUELTO» y L1155 `last_meaningful_event:` «EL SEXTO GATE DE CERTIFICACIÓN
DEVUELVE…»— y **cuatro son atribuciones de procedencia** («reanclado por `EE-04` del SEXTO
GATE»), cuyo estatus bajo la regla 2 es discutible. **El hallazgo se sostiene sobre las DOS
primeras y no necesita las otras cuatro.** Y es alcanzable: la sede «Siguiente acción exacta»
(L3830-3834) **demuestra la forma correcta en el mismo fichero** —«*Su documento NO se escribe
aquí: se deriva con `ls …`*»— y la aplica a la mitad que dice «su documento» mientras la
incumple en la mitad que dice «el último gate», **en la misma frase**. **MEDIO, clase `A`.**

---

### `S2-05` · **SOSTENIDO** · MENOR · un rótulo de supervivencia que no sobrevivió

```console
$ sed -n '1024,1029p' DECISIONES-Y-CONTRADICCIONES.md
   1  … Barrido del fichero entero: CERO apariciones de «ADS operativo», …
$ sed -n '1052,1054p' DECISIONES-Y-CONTRADICCIONES.md
   [HISTÓRICO … Es el ÚNICO de los cuatro que O19 dejó atrás: hoy la sede existe …]
$ grep -n 'ADS operativo' DECISIONES-Y-CONTRADICCIONES.md
1026 · 1029 · 1038 · 1180        →  grep -c = 4, no 0
$ grep -n 'certificar cualquier adaptador' …        1181
$ grep -n 'SIS define el contrato de conformidad' … 1187      (L1176-1193 = proyección de `O19`)
```

**REPRODUCE, y añado un dato que `S2` no publica y que lo agrava:** L1029 y L1038 están **dentro
del propio bloque**, de modo que el barrido «del fichero entero: CERO» **ya era falso en el
commit que lo escribió**; L1180-1187 son las que puso después la proyección de `O19`. La
afirmación de que el hecho 4 es «**el ÚNICO de los cuatro**» que caducó es falsa: el hecho 1
también. **Y acoto sin adornarlo, como `S2` hace:** el sentido de fondo del hecho 1 —que la
entrada CORTA de `O18` no contiene las tres condiciones— **sigue siendo cierto**; lo falso es
el barrido tal como está escrito y el rótulo que lo declara superviviente. **MENOR, clase `A`.**

---

### LO QUE NO CAE, Y LO REPRODUJE YO PARA COMPROBARLO

```console
LOS CINCO CONTROLES POSITIVOS COMMITEADOS. Reproduje LOS CINCO, uno por clon, con
`git add -A && git commit` y `porcelain` vacío en los cinco:
  docs/normativa/SEGUNDA-SEDE.md                          → 37/38  FALLO G-29
  SEGUNDA-SEDE.md en la RAÍZ                              → 37/38  FALLO G-29
  docs/SEGUNDA-SEDE.md                                    → 37/38  FALLO G-29
  docs/evolucion/28-SEGUNDA-SEDE-NORMATIVA.md             → 37/38  FALLO G-29
  …/manifiestos/F4C-FALSO-MANIFIESTO.md                   → 37/38  FALLO G-29
  detalle en los cinco: `AMPLIACIÓN NO CLASIFICADA del corpus gobernado, CONFIRMADA O NO: <ruta>`
LA TANDA DICE LA VERDAD EN LOS CINCO CONTROLES POSITIVOS. Los que declara rojos, lo son, y lo
he medido yo. **Lo que los cinco comparten es una premisa —CREAR UN FICHERO— y es exactamente
la premisa que `S1-02` no usa.**

EL MANIFIESTO 7 · sus DOS aritméticas DERIVAN (§1.2), sus 79 filas casan sin una
  discrepancia contra el árbol de la candidata, y la única fuente sin fila sobre el árbol del
  gate es él mismo. `EE-02` NO REINCIDE.
LA FILA DEL PROPIO DERIVADOR · 798 y `7d72b061…` en los DOS árboles. `U-02`→`X-06`→`DD-18`
  NO REINCIDE, por tercera vez que aguanta.
EL SOBRE · sus diecisiete cifras reproducen, y los dos bloques embebidos son EL MISMO fichero.
`EE-19` · el sobre distingue hoy la superficie de los UNIVERSOS (2) de la de los ÁRBOLES (5)
  y publica el comando. Ejecutado: 5 rutas, tres de ellas evidencia derivada. NO REINCIDE.
`EE-09` · el derivador falla CERRADO ante codificación. Verificado por `S1`, ejecutado.
`EE-03` · los 79 = el universo, y el manifiesto del séptimo gate está en la LISTA. NO CAE.
```

---

## §3 · TABLA CONSOLIDADA Y DEDUPLICADA

### §3.1 · QUÉ FUSIONO Y QUÉ NO, y por qué

```text
NO FUSIONO `S1-01` con `S1-02`, aunque los dos produzcan EL DÉCIMO ÁRBOL.
   Sedes distintas (L1920 `.split()` · L3116-3119 `_ampliaciones`), remedios distintos
   (`EE-11` · `EE-01`), y PRECONDICIONES OPUESTAS: uno CREA un fichero con nombre no-ASCII;
   el otro NO CREA NINGUNO. Cerrar uno no cierra el otro, y eso es la prueba de que son dos.

NO FUSIONO `S1-02` con `S1-03`, aunque los dos vivan en `G-29`.
   `S1-02` es el EJE de la primera guarda (existencia en vez de contenido); `S1-03` es la
   REFERENCIA de la segunda (`HEAD` en vez de la base). Son dos guardas y dos defectos.

NO FUSIONO `S1-04` con `S1-05`. `S1-04` es el ALCANCE de la publicación de exclusiones —vale
   para cualquier motivo de exclusión, no sólo el bytecode—; `S1-05` es el PREDICADO y su
   docstring. Cerrar el alcance deja la docstring falsa, y al revés.

NO FUSIONO `S2-01` con `S2-02`, aunque vivan en `00-INDICE.md` L93 y L94.
   Remedios distintos (`EE-14` · `EE-10`) y defectos distintos (desglose no derivado · comando
   retirado presentado como vigente).

NO FUSIONO `S2-03` con `S2-04`, aunque los dos midan `EE-04`. Reglas distintas del mismo
   bloque (regla 4 · regla 2) y campos distintos. Los cerraría la misma tanda, no el mismo acto.

FUSIONES ENTRE `S1` y `S2`: NINGUNA. Los dominios no se solapan: los nueve de `S1` son del
   instrumento y del documento 11 L1-L5200; los cinco de `S2` son documentales y del
   `CHECKPOINT`/`00-INDICE`/`DECISIONES`. No hay un solo par que mida la misma sede.

CAÍDOS: NINGUNO. Los catorce reproducen contra fichero y línea.
REBAJADOS: NINGUNO en severidad. UNO en su CIFRA: `S2-04` (seis ocurrencias → dos que la
   regla 2 gobierna sin discusión, y el hallazgo se sostiene sobre esas dos).
```

### §3.2 · LOS CATORCE

| id | sev | clase | sede | reincidencia, con identificador | estado |
|---|---|---|---|---|---|
| **`S1-01`** | **BLOQUEANTE** | **A** | batería L1920-1921 vs comentario L1922-1929 · `CHECKPOINT`:3790 | **SÍ · `EE-11`**, en su propio remedio. Y `R1-07`+`R1-09` (doc 27). Familia `T-05` · `R-A`. Y **`M-04`, séptimo gate** | **SOSTENIDO** |
| **`S1-02`** | **BLOQUEANTE** | **A** | batería L3116-3119 (`_ampliaciones`) · título L3204 · README L244 | **SÍ · `EE-01`** (que es `DD-02`, que es `BB4`): instancia cerrada, clase abierta, **un EJE más allá**. Y **`M-04`, séptimo gate** | **SOSTENIDO Y AMPLIADO** (8 ficheros medidos) |
| **`S1-03`** | **GRAVE** | **A** | batería L3190-3200 (unicidad 2) bajo el título L3204 · README L244 | **SÍ · `EE-01`**, cuya PROPIA FILA nombra `L3107-3118`; y `R1`/`RF-4` del sexto gate lo dijo con todas las letras. **6.ª condición de `O18`** | **SOSTENIDO** |
| **`S1-04`** | **GRAVE** | **A** | derivador L173-175 y L738-740 vs L238 y L560 | **SÍ · `DD-01`**: instancia cerrada (`docs/owner/`, la variante `V4` de `R1`), clase abierta fuera de las dos zonas barridas. **6.ª condición de `O18`** | **SOSTENIDO** |
| **`S1-05`** | **MEDIO** | **A** | derivador L182-202 (`_es_bytecode`) y gemela en batería L1987-2007 | parcial · misma familia que `EE-09` (dos lecturas de la misma propiedad). **6.ª condición de `O18`** | **SOSTENIDO** |
| **`S1-06`** | **MEDIO** | **A** | batería L130-131 (comentario `EE-17`) vs L355-371 | **SÍ · `EE-17`**, en su propio remedio; y es la inercia-tras-confirmar de `EE-01`/`DD-02`. **6.ª condición de `O18`** | **SOSTENIDO** |
| **`S1-07`** | **MEDIO** | **A** | doc 11 L1782 contra L1739-1742 del mismo bloque | **SÍ · `DD-13` ≡ `R2-07`→`EE-07` ≡ `R2-08`→`EE-12`**. CUARTA sede del mismo cardinal, y la única a la que nadie volvió | **SOSTENIDO** |
| **`S1-08`** | **MENOR** | **A** | emisor L234-242 y L294-299 vs derivador L726-733 | **SÍ · `EE-16`**, cuyo remedio fue una tercera copia y no una sede. LATENTE | **SOSTENIDO** |
| **`S1-09`** | **MENOR** | **A** | manifiesto 7 §4 fila 2 contra su §3 | **SÍ** · la limitación que `R1` puso la SEGUNDA de su §6 (doc 27) y que `EE` elevó a observación de método. **El manifiesto 7 repartió igual** | **SOSTENIDO** |
| **`S2-01`** | **GRAVE** | **A** | `00-INDICE.md`:93 vs `CORRIGENDUM` §18 y doc 27 L3896 | **SÍ · `EE-14`** aplicado a medias; y `EE-14` era ya la clase de `F-12` (doc 16) y de `L` (doc 19) | **SOSTENIDO** |
| **`S2-02`** | **MEDIO** | **A** | `00-INDICE.md`:94 vs `CHECKPOINT`:3644-3652 | **SÍ · `EE-10`** (que es `J-07`/`DD-13`): instancia cerrada, clase abierta **en el mismo commit**. LATENTE | **SOSTENIDO** |
| **`S2-03`** | **MEDIO** | **A** | `CHECKPOINT`:1051-1136 contra la regla 4 en L906-909 | **SÍ · `EE-04`** (que es `K-01`/`J-10`/`L-01` · `P-05`≡`Q-08`/`R-02` · `S-17`≡`S3-05` · `X-04` · `DD-08` · `R2-03`). **SEXTA recurrencia, y PEOR: dos documentos de retraso donde había uno** | **SOSTENIDO** |
| **`S2-04`** | **MEDIO** | **A** | `CHECKPOINT`:914 y :1155 (y cuatro atribuciones) contra la regla 2 en L899-902 | **SÍ · `EE-04`** y **`J-07`** («no se sustituye un número por otro») | **SOSTENIDO, cifra matizada** |
| **`S2-05`** | **MENOR** | **A** | `DECISIONES`:1024-1029 contra :1052-1054 | **SÍ · `BT-01`**, una viñeta más allá | **SOSTENIDO** |

### §3.3 · RECUENTO, DERIVADO DE LAS FILAS DE ARRIBA

```text
BLOQUEANTE   2     S1-01 · S1-02
GRAVE        3     S1-03 · S1-04 · S2-01
MEDIO        6     S1-05 · S1-06 · S1-07 · S2-02 · S2-03 · S2-04
MENOR        3     S1-08 · S1-09 · S2-05
             ──
            14

POR CLASE
  A · coherencia interna, corregible dentro de `F4c`   14
  B · exige una decisión NUEVA del Owner                0
  C · actor privilegiado, contratado para `F6`          0

POR ÁRBOL
  DE LA CANDIDATA `f8fc037a…` (el objeto que el gate juzga)   13
  DEL APARATO DEL GATE `08f6da6e…`                             1   (S1-09, el reparto)
  DEL SOBRE                                                    0

REINCIDENCIAS   13 de 14 llevan identificador de una clase ya dictaminada en los documentos
                25, 26 o 27. La única que no es `S1-05`, y aun ésa es la misma familia que
                `EE-09`. NUEVE viven DENTRO de un remedio de la tanda que este gate juzga:
                `EE-01` (×2: S1-02, S1-03) · `EE-11` · `EE-14` · `EE-10` · `EE-04` (×2) ·
                `EE-16` · `EE-17`.
```

### §3.4 · POR QUÉ NINGUNO ES `C`, Y LO DIGO CON SU SEDE

Leí la sede que fija la frontera antes de clasificar: `CHECKPOINT-ADS-NEXT.md`, sección «El
criterio del gate siguiente», subsección **`DD-20`** (L3534-3572). Su literal:

> `A` COHERENCIA INTERNA — el defecto está EN EL CORPUS y la batería lo da por bueno. **Que el
> fichero esté o no CONFIRMADO es IRRELEVANTE: el objeto que un gate juzga es un COMMIT, y
> confirmar es lo que hace el coordinador en su propia rama de revisión**
>
> `C` ACTOR PRIVILEGIADO — corromper la REFERENCIA contra la que se compara: reescribir `HEAD`,
> las refs o la revisión base · editar la batería, su README o el derivador · mentir el runner
> · cualquiera de los SEIS actos que `O18` enumera
>
> CONSECUENCIA — un árbol defectuoso **COMMITEADO** que la batería no ve es clase `A`, cuenta,
> y no se descarta por estar confirmado

**Los cuatro ataques que consuman —`S1-01`, `S1-02`, `S1-03`, `S1-04`— usan `git add -A && git
commit` SIN UN SOLO FLAG**, no reescriben `HEAD`, ni las refs, ni la revisión base; no editan
la batería, su README ni el derivador; no mienten al runner; y ninguno es uno de los seis actos
de `O18`. **Los catorce son clase `A`. NINGUNO ES `C`. NINGUNO ES `B`: los catorce se cierran
con material que el corpus ya tiene escrito, y ninguno reinterpreta `O17`, `O18` ni `O19`.**

Y anoto, por la misma sede: **que la rama local `fix/f4c-perimetro-por-naturaleza-20260831` esté
en el commit del gate NO es un hallazgo.** `Z3`, que es la formulación que rige, lo dice
expresamente: confirmar en la rama que se somete a revisión es **el acto ordinario del
coordinador**.

---

## §4 · LAS CINCO CUESTIONES QUE EL MANIFIESTO ME ENCARGA

### §4.1 · `C-L.5` — LAS DOS RESTAS, Y LA PALABRA

**Las dos restas de ESTE gate, derivadas por mí en §1.2 y §1.3, sin fiarme de nadie:**

```text
OBLIGATORIO − ASIGNADO   ∅   sobre el árbol de la CANDIDATA, EN LAS DOS DIRECCIONES,
                             igualdad de conjuntos ruta a ruta: 79 = 79, comm vacío
                             en los dos sentidos
                         Sobre el árbol del GATE: la ÚNICA fuente sin fila es EL PROPIO
                             MANIFIESTO — la exención de PUNTO FIJO de `DD-19`, declarada,
                             enumerada con su razón, y no extendida a ningún otro fichero.
                             NO HAY NINGUNA OTRA, y el §6 me encargaba decirlo si la hubiera.

ASIGNADO − LEÍDO         ∅   `S1`  16234 − 16234 = 0
                             `S2`  16829 − 16829 = 0
                             y la unión de sus rangos cubre las DOCE filas de lectura, con el
                             documento 11 cubierto entero (5200 + 6508 = 11708) sin hueco ni
                             solape. Verificado además MATERIALMENTE: los catorce hallazgos
                             caen dentro del rango que su autor declara leído.
```

**Y AHORA EL ACTO, QUE ES MÍO Y QUE NADIE HARÁ POR MÍ.**

Tres gates seguidos midieron las dos restas a ∅ y ninguno escribió la palabra. **El quinto no
la escribió y `DD` hizo bien**: la condición se había reabierto por `ASIGNADO − LEÍDO = 1` del
cuarto gate y el aparato aún no estaba limpio. **El sexto no la escribió y `EE` dijo por qué,
con una razón MATERIAL y no una cautela**: el §6 del manifiesto `6B` publicaba
`OBLIGATORIO − ASIGNADO = 1` sobre el árbol del gate **y eran 2**, de modo que certificar la
cobertura habría sido apoyarse en una medición que ese mismo gate acababa de refutar
(`EE-02`). **Y `EE` dejó escrito, con todas las letras, qué la cerraría** (doc 27 §4.1):

> «*un manifiesto cuyo §6 DERIVE las dos aritméticas con su comando en vez de copiarlas, y en
> el que el manifiesto sustituido o bien lleve fila, o bien quede excluido con una razón
> DERIVADA y publicada. Con eso, y sin nada más, la cobertura queda certificable.*»

**MEDÍ LAS DOS MITADES SOBRE EL MANIFIESTO DE ESTE GATE, Y LAS DOS ESTÁN HECHAS.**
(i) Su §6 (L174-186) **publica los comandos** y no copia las cifras; las derivé yo y salen.
(ii) Su §6 (L198-209) **enumera una a una** las fuentes sin fila del árbol del gate con su
razón, declara que la exención de punto fijo «cubre a ESTE fichero y a NINGÚN OTRO», y —lo
comprobé— **no hay ninguna otra**. Y en este gate **no hay manifiesto sustituido**: el `6B` no
tiene sucesor que lo desplace, y las dos aritméticas cierran sin necesitar la exención.

**El obstáculo que `EE` nombró está RETIRADO. Las dos restas dan ∅. El aparato que las mide no
publica ni un cardinal falso. No queda ninguna medición pendiente: queda un acto. Lo hago.**

# `C-L.5` · **CERTIFICADA**

**CERTIFICADA POR COBERTURA por el adjudicador `FF` del SÉPTIMO GATE**, sobre el árbol de la
candidata `f8fc037a998316081a7e9b9563398d118982ce60`, con las dos restas derivadas por mí y
publicadas con su comando en §1.2 y §1.3.

**Y DIGO EXACTAMENTE QUÉ CERTIFICO Y QUÉ NO, porque una palabra sin alcance es lo que este
expediente lleva seis gates persiguiendo:**

```text
CERTIFICO   que el universo obligatorio de la candidata está ÍNTEGRAMENTE ASIGNADO, que las
            79 filas casan con el árbol sin una discrepancia de SHA-256 ni de líneas, que lo
            asignado a cada revisor está cubierto por los rangos que declara, que el documento
            11 queda cubierto entero entre los dos, y que la única fuente sin fila sobre el
            árbol del gate es el propio manifiesto por PUNTO FIJO.

NO CERTIFICO  la SUFICIENCIA de `F4c` — es otra pregunta y la respondo en §8, y la respondo NO.
NO CERTIFICO  la PROFUNDIDAD de la lectura: `C-L.5` es una condición de COBERTURA. Que dos
              mitades del documento 11 tengan dos lectores distintos es `S1-09`, y sigue vivo.
NO CERTIFICO  ningún hallazgo como SUPERADO. Ninguno lo está.
NO CERTIFICO  que los revisores leyeran lo que declaran. Certifico que lo asignado y lo
              declarado leído coinciden, que sus huellas reproducen, y que cada afirmación
              suya cae dentro de su rango. Es lo que un adjudicador puede medir, y lo digo así.

Y CONSTA     que ésta es la QUINTA certificación de `C-L.5` del expediente —las cuatro
             anteriores en los documentos 21, 22, 23 y 24, derivadas por mí de las filas 84,
             86, 87 y 91 de `00-INDICE.md`— y la PRIMERA desde que el CUARTO GATE (documento
             25) la pasó de CERTIFICADA a ABIERTA por `ASIGNADO − LEÍDO = 1`.
             La sede del ESTADO de `C-L.5` es UNA —la clasificación vigente del `CHECKPOINT`,
             L2175-2201— y este acto es el que esa sede tiene que recoger. NO lo escribo yo:
             yo no corrijo el repositorio.
```

### §4.2 · `C-L.7` — ¿CERRADA O NO?

**NO ESTÁ CERRADA, y no se acerca por la vía que se ha usado.**

`C-L.7` es «el checkpoint reancla su estado en cada tanda». La medí yo:

```text
LO QUE SÍ SE HIZO   `metodo:` y `last_meaningful_event:` describen hoy el SEXTO gate y esta
                    tanda, y lo anterior bajó a sus campos `_anterior` como la regla 5 ordena.
                    Sobre eso, la regla 4 se cumple, y es una mejora REAL sobre `R2-03`.

LO QUE NO           (i) `based_on` reanclado en su PREÁMBULO y no en su CUERPO: su enumeración
                        termina en el documento **25** y faltan el **26** y el **27**. Es
                        `S2-03`, reproducido por mí, y **faltaban UNO cuando `R2-03` lo midió:
                        hoy faltan DOS. El defecto EMPEORÓ mientras su remedio se declaraba
                        aplicado.**
                    (ii) El reanclaje se hizo **sustituyendo un ordinal escrito a mano por otro
                        ordinal escrito a mano**, contra la regla 2 escrita DENTRO del bloque,
                        y en la misma frase que la invoca para la otra mitad. Es `S2-04`.
```

**RESPUESTA: `C-L.7` NO ESTÁ CERRADA.** Es la **SEXTA recurrencia consecutiva** de la clase
(`K-01`/`J-10`/`L-01` · `P-05`≡`Q-08`/`R-02` · `S-17`≡`S3-05` · `X-04` · `R2-03`→`EE-04` · ésta)
y **la segunda cometida contra una regla escrita dentro del propio bloque para impedirla**.
Y añado lo que la respuesta obliga a decir: **el bloque vuelve a copiar lo que declara no
copiar**, que es la forma exacta del defecto original.

### §4.3 · `M-04` — ¿SUPERADA O NO?

**NO SUPERADA. Séptimo gate consecutivo, y esta vez con CUATRO árboles defectuosos, DOS de
ellos reproducidos por mí de cero en un clon desechable.**

`M-04` es la proposición general —que el corpus no pueda darse por bueno a sí mismo estando
corrupto—. **No la cierra nadie desde dentro del árbol, y el propio corpus lo declara**
(`verificacion/README.md` L293-308 y §11.4 del documento 11). Lo que un gate puede hacer es
medir si sigue FALLIDA, y lo mido:

```text
SIGUE FALLIDA, y las dos mediciones son mías:
  `S1-01`  crea un fichero con una `Ñ` en el nombre           38/38 · EXIT=0 · digest ANCLADO
  `S1-02`  NO crea ningún fichero: MUTA uno de la base        38/38 · EXIT=0 · digest ANCLADO
           y su superficie ciega son OCHO ficheros, medidos uno a uno por mí
Y las otras dos, también reproducidas:
  `S1-03`  segunda guarda de `G-29`: 37/38 sin commitear → 38/38 commiteada
  `S1-04`  el SOBRE publica «PERÍMETRO: 1» sobre un árbol que excluye un documento

DE LAS SEIS CONDICIONES DE `O18`, y sólo en lo que este gate alcanza:
  1.ª «batería interna coherente»                         FALLA — `S1-01`, `S1-02`
  6.ª «ninguna promesa de seguridad superior a la
       realmente entregada»                               FALLA — `S1-01` (comentario `EE-11`
       y fila `CHECKPOINT`:3790), `S1-03` (título de `G-29` y README L244), `S1-04`
       (promesa del derivador), `S1-05` (docstring), `S1-06` (comentario `EE-17`),
       `S1-08` («se usa UNA»)
  3.ª «todas sus huellas coincidentes»                    SE CUMPLE — verificada entera por mí
FALLAN LA PRIMERA Y LA SEXTA, que es exactamente el resultado de los dos gates anteriores.
```

### §4.4 · `X63` — ¿SE PRESENTA COMO PRUEBA EJECUTADA O COMO CERTIFICACIÓN PRESENTE?

**NO. En ninguna sede.** Barrí sus apariciones y las clasifiqué:

```console
$ git grep -n 'X63' 08f6da6e -- '*.md' '*.py' '*.txt' '*.yaml'
11-ARQ:1714 · 1742 · 3715 · 5517 · 5676 · 5688   CHECKPOINT:44 · 2426 · 3011 · 3702 · 3735 · 3817
00-INDICE:94 · 97 · 98    doc 27 y manifiestos 6·6B·7 (registro histórico y encargo)
$ sed -n '1782p' 11-ARQ    «**Ninguna se ha ejecutado.** … no es su demostración»
$ sed -n '3735p' CHECKPOINT «`X63` NO ES UNA PRUEBA — es CONTRATO DE PRUEBA DE `F6`»
$ sed -n '3817p' CHECKPOINT «`X63` SIGUE SIENDO CONTRATO de prueba de `F6`. NO ejecutado …»
```

El único presente de indicativo —doc 11 L5676, «y `X63` la comprueba validando las tres
celdas»— es **la voz con que el documento escribe TODAS sus filas `X<nn>`** y queda
desambiguado doce líneas más abajo (L5688: «*es un contrato de prueba de `F6` … y no se ejecuta
aquí*»), además de por tres sedes que lo niegan expresamente. **`R2`, `EE`, `S1` y `S2` llegaron
a la misma conclusión antes que yo, y coincido: NO lo cuento como hallazgo.**

**Pero lo consigno como `EE` lo consignó, y suscribo su formulación:** un presente de indicativo
en la voz del contrato **es la forma exacta en que este corpus ha producido sus cardinales
caducados**. `S1-07` es hoy la prueba de que esa observación no era retórica.

### §4.5 · LA CONDICIÓN DE SALIDA QUE `EE` DEJÓ ESCRITA — ¿SE CUMPLE HOY?

La condición, en su sede (doc 26 §7.4, citada y medida por `EE` en doc 27 §5.2):

> «*si en el gate 6 el perímetro se deriva de verdad **y las cinco promesas dicen lo que el
> código hace**, entonces «se cierran instancias y no clases» pasa a ser deuda registrada*»

**MITAD 1 · «el perímetro se deriva de verdad» — SE CUMPLE, y lo verifiqué yo.**
`DD-01` sigue siendo el remedio más sólido del expediente: probé enlaces simbólicos, ficheros
vacíos, ordinales Unicode, `.gitattributes` y bytecode fabricado, y el perímetro aguanta como
PREDICADO. **Esta mitad sigue cerrada por segundo gate.**

**MITAD 2 · «las promesas dicen lo que el código hace» — NO SE CUMPLE, y lo mido en SEIS sedes.**

```text
1  título de `G-29` (batería L3204) y README L244: «CONFIRMADO O NO» de las TRES sub-guardas,
   y sólo es cierto de UNA. Y esta tanda ENSANCHÓ la promesa mientras arreglaba una de las dos
   sedes que el propio `EE-01` enumera.                                              `S1-03`
2  comentario de `EE-11` (batería L1922-1929) y fila `CHECKPOINT`:3790: «Con `-z` desaparecen
   los dos». Sobreviven LOS DOS en `_tocados_raw`, uno en silencio y otro con diagnóstico
   falso. Medido por mí en las dos formas.                                           `S1-01`
3  derivador L173-175 y docstring L738-740: «mientras algo quede fuera, se PUBLICA con su
   ruta». Sólo dentro de dos zonas.                                                  `S1-04`
4  docstring de `_es_bytecode` L183-189: promete una imposibilidad que fabriqué en un
   comando, y el motivo que publica del fichero es falso.                            `S1-05`
5  comentario de `EE-17` (batería L130-131): «es ROJO y se nombra». Sólo se imprime.  `S1-06`
6  comentario de `EE-16` (emisor L297-299): «Se usa UNA». Son dos.                    `S1-08`
```

**RESPUESTA: NO SE CUMPLE. Por SEGUNDO gate consecutivo, la primera mitad sí y la segunda no.**
Y lo digo con la precisión que el encargo exige: **no es que la mitad 2 siga igual — es que
CUATRO de las seis promesas falsas de hoy son promesas que ESTA TANDA escribió o ensanchó**
(las 1, 2, 5 y 6 nacen de los comentarios `EE-01`/`EE-11`/`EE-17`/`EE-16`). **La frase de `BB4`
—«el sistema cierra INSTANCIAS y no CLASES»— SIGUE SIENDO CIERTA y NO pasa a deuda registrada.**

---

## §5 · REINCIDENCIAS, Y LA CONDICIÓN DE SALIDA

### §5.1 · El recuento, derivado de la tabla de §3.2

```text
REINCIDENCIAS CON IDENTIFICADOR EN LOS DOCUMENTOS 25 · 26 · 27      13 de 14
DENTRO DE UN REMEDIO DE LA TANDA QUE ESTE GATE JUZGA                 9 de 14

  S1-01  EE-11                          — su comentario dice haber cerrado DOS modos de
                                          fallo, y los DOS siguen abiertos en la lectura
                                          que `-z` no alcanzó
  S1-02  EE-01 ← DD-02 ← BB4            — instancia cerrada, clase abierta, UN EJE más allá
  S1-03  EE-01 (su propia fila nombra
         L3107-3118) + R1/RF-4 doc 27   — el remedio se aplicó a UNA de las DOS sedes que el
                                          hallazgo enumera, y el título se ENSANCHÓ
  S1-04  DD-01                          — el PREDICADO cerró por clase; la PUBLICACIÓN no
  S1-05  familia de EE-09               — la misma propiedad, dos lecturas incompatibles
  S1-06  EE-17                          — su comentario dice ROJO y el código imprime
  S1-07  DD-13 ≡ R2-07→EE-07 ≡
         R2-08→EE-12                    — CUARTA sede del cardinal 46, la única a la que
                                          nadie volvió, a 40 líneas de la nota que lo retira
  S1-08  EE-16                          — el remedio fue una tercera copia, no una sede
  S1-09  R1 §6 (2.ª) doc 27, elevada
         por EE a observación de método — el manifiesto 7 repartió igual
  S2-01  EE-14 ← F-12 (doc 16) ·
         L (doc 19)                     — remedio de DOS mitades del que se aplica UNA, y la
                                          omitida es la que el adjudicador nombró por línea
  S2-02  EE-10 ← J-07 · DD-13           — el comando retirado, vivo en la sede de al lado,
                                          EN EL MISMO COMMIT
  S2-03  EE-04 ← R2-03 ← X-04 ←
         S-17≡S3-05 ← P-05≡Q-08/R-02
         ← K-01/J-10/L-01 · DD-08       — SEXTA recurrencia, y PEOR que la quinta
  S2-04  EE-04 · J-07                   — un ordinal a mano por otro ordinal a mano
  S2-05  BT-01                          — una viñeta más allá

NO REINCIDENTE     ninguno en sentido estricto. `S1-05` es lo más cercano a nuevo, y aun así
                   es la familia de `EE-09` en el fichero de al lado.
```

**LA CIFRA QUE IMPORTA, Y ES MÍA:** el sexto gate publicó **15 reincidencias de 19** y `EE` la
valoró por encima de tres hallazgos. **Hoy son 13 de 14, y NUEVE viven dentro de un remedio de
la tanda que se somete a este gate.** La proporción no ha mejorado: **ha empeorado**.

### §5.2 · La condición de salida — resuelta en §4.5

**NO SE CUMPLE.** Mitad 1 (perímetro derivado) SÍ, por segundo gate. Mitad 2 (las promesas
dicen lo que el código hace) NO, en SEIS sedes que enumero en §4.5, **cuatro de ellas escritas
o ensanchadas por esta misma tanda**. **«Se cierran instancias y no clases» NO pasa a deuda
registrada. Sigue siendo un hallazgo vivo, por tercer gate.**

### §5.3 · Y LO QUE ESTA TANDA SÍ CERRÓ, porque es verdad y no es cortesía

```text
· `EE-02` está CERRADO en su primer uso: el §6 del manifiesto 7 DERIVA las dos aritméticas
  con su comando y enumera una a una las fuentes sin fila. Lo derivé yo y sale exacto.
· `EE-03` no reincide: las 79 filas = el universo, el manifiesto del séptimo gate en la LISTA.
· `EE-08` no reincide: el §5 del manifiesto 7 ya no describe una regla más estricta.
· `EE-19` está cerrado: el sobre distingue hoy la superficie de los UNIVERSOS (2) de la de
  los ÁRBOLES (5) y publica el comando. Ejecutado por mí: exacto.
· `U-02`→`X-06`→`DD-18` no reincide: la fila del propio derivador casa contra los DOS árboles.
  Es la tercera vez que aguanta.
· `DD-17` sigue roto: el commit del gate no deja el árbol en rojo, y las tres evidencias
  reejecutadas viajan en el MISMO commit.
· `DD-01` aguanta como PREDICADO: enlaces simbólicos, ficheros vacíos, ordinales Unicode y
  `.gitattributes` caen; los cinco controles positivos COMMITEADOS dan rojo, y los reproduje
  LOS CINCO.
· `EE-07`/`EE-12`, `EE-13`, `EE-18`, `EE-05`, `EE-06` aguantan el ataque a la sede de al lado
  según `S2`, y no encontré nada que lo desmienta.
· EL SOBRE FUNCIONA, y los dos bloques embebidos son el MISMO fichero.
· NINGUNA decisión vuelve al Owner, por CUARTA vez consecutiva.
```

---

## §6 · REFUTACIONES CONTRA MIS PROPIAS CONCLUSIONES

Intenté **siete**. **Dos cayeron, tres cayeron a medias, dos no cayeron.** Publico las siete,
y digo qué cambió cada una.

### `RF-1` · **CAYÓ A MEDIAS, Y ME OBLIGÓ A MEDIR MÁS** · «`S1-01` depende de `core.quotePath`: es un caso de laboratorio, no un defecto del corpus»

**Lo medí en vez de suponerlo.** Con `git config core.quotePath false` el ataque **CAE**:
`FALLO G-23 · 37/38`. **Es contingente de la configuración de Git.**

**Y aun así el hallazgo se sostiene, por tres razones que también medí:** (i) `true` es el valor
**POR DEFECTO** de Git y es con el que corrieron los dos revisores, el coordinador y yo;
(ii) **el instrumento no fija ni comprueba esa variable en ninguna parte** —lo que significa que
la corrección de la batería depende hoy de una variable de entorno que ninguna comprobación
ancla, y eso es en sí un defecto de clase `A`—; y (iii) **la otra forma de fallo de la misma
línea, la ruta CON ESPACIO, NO es contingente de nada**, y produce un **diagnóstico FALSO** que
nombra un fichero inexistente, medido por mí. **CAMBIÓ MI INFORME:** añadí la medición con
`quotePath false` y la del espacio a `S1-01`, y la contingencia queda publicada. **Severidad
mantenida: BLOQUEANTE — y sobre todo porque el veredicto NO cuelga de este hallazgo, sino de
`S1-02`, que no depende de ninguna configuración.**

### `RF-2` · **CAYÓ, Y CONTRA MÍ** · «`S1-02` es exótico: mutar `START_HERE.md` es un caso rebuscado, y no hay tantos ficheros así»

**Fui a medirlo y el resultado agrava el hallazgo.** Derivé la superficie completa —ficheros de
la revisión base, fuera de los tres inventarios de contenido, fuera del universo obligatorio— y
la probé **fichero a fichero, con un clon por fichero**: son **OCHO**, y los ocho dan
**38/38 · `porcelain` vacío · digest del sobre BIT A BIT el anclado**. Y **tres de los ocho son
precisamente las evidencias que el commit del gate reejecuta por `DD-17`**. No es un caso
rebuscado: es una superficie enumerable que nadie había enumerado. **CAMBIÓ MI INFORME:** `S1-02`
pasa de «dos instancias» a «una clase medida exhaustivamente», con su tabla.

### `RF-3` · **CAYÓ** · «`S1-03` no es hallazgo nuevo: `R1` lo levantó en su `RF-4` del sexto gate y `EE` lo absorbió dentro de `EE-01`. Contarlo otra vez es contar dos veces»

**Fui a la fila de `EE-01` y encontré lo contrario de lo que la objeción supone.** La sede que
`EE` publica para `EE-01` es «batería L3038 **y L3107-3118**» — **`L3107-3118` ES la unicidad 2**.
Es decir: `EE-01` **nombró expresamente las dos guardas**, y la tanda arregló una. Eso no
convierte `S1-03` en un doble conteo: lo convierte en **la mitad no aplicada de un remedio cuya
propia fila enumeraba las dos sedes**, que es exactamente la clase que este gate examina.
**CAYÓ, y la refutación me hizo REFORZAR el hallazgo, no rebajarlo.** Sigue siendo un hallazgo
separado de `S1-02` porque el defecto es distinto (referencia contra `HEAD`, no eje del alcance)
y porque cerrar uno no cierra el otro.

### `RF-4` · **NO CAYÓ** · «`S1-04` no importa: la batería SÍ nombra el fichero, luego no es silencioso»

**Es cierto y lo medí: la batería publica `PERÍMETRO: 2` con la ruta completa.** Por eso NO lo
subo a BLOQUEANTE, y lo digo en su sitio. Pero la objeción no lo tumba: lo que se degrada es el
**SOBRE**, que es el ancla EXTERNA que `O18` contrata, el objeto que el revisor recibe **antes**
de leer nada y que sus seis obligaciones le mandan verificar. **El sobre publicaría
«EXCLUIDOS por PERÍMETRO: 1» sobre un árbol que excluye un documento que declara `F4c` cerrada**,
y ninguna de las seis obligaciones le pide al revisor ejecutar la batería. **NO CAYÓ. GRAVE.**

### `RF-5` · **CAYÓ A MEDIAS** · «`S2-04` es pedantería: no se puede escribir `last_meaningful_event` sin nombrar el gate»

**Sí se puede, y el propio fichero lo demuestra.** «Siguiente acción exacta» (L3830-3834)
escribe: «*Su documento NO se escribe aquí: se deriva con `ls docs/evolucion/[0-9][0-9]-*.md |
sort | tail -1`*». **La forma correcta existe, está en el mismo fichero y en la misma frase.**
Lo que **sí** cayó de mi lectura inicial es la CIFRA: de las seis ocurrencias, **cuatro son
atribuciones de procedencia** («reanclado por `EE-04` del SEXTO GATE») cuyo estatus bajo la
regla 2 es discutible, y **dos son los campos que la regla gobierna sin discusión** (L914 y
L1155). **CAMBIÓ MI INFORME:** matizo la cifra y sostengo el hallazgo sobre las dos. Severidad
mantenida en MEDIO.

### `RF-6` · **NO CAYÓ** · «`C-L.5` no puede certificarse en un gate que emite INSUFICIENTE: certificar la cobertura suena a absolver»

**No suena: son dos preguntas distintas, y confundirlas es el error que el corpus castiga.**
`C-L.5` es una condición de **COBERTURA** —¿está todo el universo asignado y todo lo asignado
leído?—; el veredicto es sobre `A`, `B` y `C`. Los documentos 22, 23 y 24 emitieron
**INSUFICIENTE** y **certificaron `C-L.5`** en el mismo dictamen, y ninguno fue absolución. Y la
sede lo separa: `C-L.5` vive en la clasificación de las trece condiciones `C-L`, no en el
veredicto. **NO CAYÓ, y por eso emito la palabra y a la vez emito INSUFICIENTE. Digo además,
para que nadie lo lea al revés, qué NO certifico** (§4.1).

### `RF-7` · **CAYÓ A MEDIAS, Y ME OBLIGÓ A REORDENAR EL VEREDICTO** · «catorce hallazgos, ninguno de clase `B` ni `C`, ninguno para el Owner y la mitad del aparato cerrada: eso es un corpus que converge, y un séptimo INSUFICIENTE es inercia del adjudicador»

**La mitad de la objeción es cierta y la escribo antes que el veredicto:** el sobre funciona por
tercera vez, el manifiesto 7 **cierra `EE-02` en su primer uso** —lo derivé y sale exacto—, la
fila del propio derivador no reincide por tercera vez, `DD-01` aguanta como predicado, los cinco
controles positivos son verdad y los reproduje, y **ninguna decisión vuelve al Owner por cuarta
vez consecutiva**. Eso es convergencia real y no la escondo.

**Y la otra mitad es falsa, y es la que decide.** Un veredicto no se emite por tendencia: se
emite por si `A` está DEMOSTRADA. **Hoy no lo está, y no por autoridad ajena: lo he medido yo,
de cero, en un clon desechable, con `git add -A && git commit` sin un solo flag, y existen sobre
el árbol que este gate juzga OCHO ficheros cuyo contenido puede sustituirse por una sentencia
que declara `F4c` cerrada dejando la batería en 38/38, `EXIT=0`, `git status` vacío y el DIGEST
DEL SOBRE BIT A BIT EL ANCLADO.** Con eso, la pregunta de si converge es irrelevante para el
veredicto: **`A` no está demostrada, y la regla dice que sin `A` no hay suficiencia.**
**CAMBIÓ MI INFORME:** puse §5.3 —lo que sí cerró— ANTES del veredicto, y no después.

### Qué cambiaron estas siete

```text
RF-1  añadí la medición con `core.quotePath false` y la del ESPACIO. Publicada la contingencia.
RF-2  `S1-02` pasó de dos instancias a una CLASE medida exhaustivamente: OCHO ficheros.
RF-3  `S1-03` se REFORZÓ: `EE-01` nombraba las dos sedes en su propia fila.
RF-4  ninguno: `S1-04` queda en GRAVE, con el motivo escrito.
RF-5  matizada la cifra de `S2-04`: seis → dos que la regla gobierna sin discusión.
RF-6  añadido a §4.1 el alcance EXPRESO de lo que certifico y de lo que NO.
RF-7  reordenado: lo que consta a favor va ANTES del veredicto.
NINGUNA me hizo suavizar una severidad, y NINGUNA hizo caer un hallazgo.
```

---

## §7 · QUÉ FALLA HOY, EN MIS PALABRAS

**Antes que nada, lo que sí es verdad**, porque un veredicto que no lo diga primero no es un
veredicto sino una inercia: el sobre funciona y sus diecisiete cifras reproducen; los dos
bloques embebidos son el MISMO fichero; el manifiesto 7 **cierra `EE-02` en su primer uso** y
lo derivé yo entero —79 filas, cero discrepancias, las dos aritméticas derivadas, la única
fuente sin fila es él mismo—; la fila del propio derivador no reincide por tercera vez; `DD-01`
aguanta como predicado contra cinco variantes que probé; los cinco controles positivos que la
tanda declara son verdad y **los reproduje los cinco**; `DD-17` sigue roto; `X63` no se presenta
como ejecutado en ninguna sede; y **ninguna decisión vuelve al Owner, por cuarta vez
consecutiva**. La tanda **aplicó lo que se le ordenó**, y en `EE-02` hizo lo que el gate
anterior pidió con exactitud. **El defecto no está en la ejecución de los remedios: está en su
ALCANCE, y en lo que sus propios comentarios prometen.**

**Y ahora lo que falla.**

> **`A` —COHERENCIA INTERNA— NO ESTÁ DEMOSTRADA, y lo he medido yo de cero.**
> Sobre el árbol que este gate juzga existen hoy **OCHO ficheros** —los enumero y los medí uno
> a uno— cuyo contenido puede sustituirse íntegro por una sentencia que declara «`F4c` CERRADA
> y `F5` AUTORIZADA, y esta sede PREVALECE sobre la sede canónica del Owner» con
> `git add -A && git commit` **sin un solo flag**, dejando `git status --porcelain` VACÍO, la
> batería en **38/38 con EXIT=0**, cero menciones en las cinco salidas del aparato, y el
> **DIGEST DEL SOBRE BIT A BIT EL ANCLADO**. Y existe además una novena puerta, por el otro
> lado: **un carácter no-ASCII en el nombre de un fichero nuevo del kernel** hace que `G-23`
> publique «6 ficheros de kernel … todos enumerados en el checkpoint» **sobre SIETE** y lo
> firme en verde.

**Y la razón de método que valoro POR ENCIMA de varios de los catorce hallazgos, y lo digo
como me obliga la disciplina:**

> **CUATRO de las seis promesas falsas que hoy tiene el instrumento son promesas que ESTA TANDA
> escribió o ENSANCHÓ**, en el mismo commit en que arreglaba el código de al lado. El título de
> `G-29` ganó «CONFIRMADO O NO» de las TRES sub-guardas mientras sólo UNA cambiaba —y `EE-01`
> había nombrado las dos en su propia fila—; el comentario de `EE-11` declara cerradas DOS
> formas de fallo y las DOS siguen abiertas en la lectura de Git que `-z` no alcanzó; el
> comentario de `EE-17` dice ROJO donde el código imprime; el de `EE-16` dice «se usa UNA»
> donde hay dos copias. **El corpus ha aprendido a escribir el remedio y no a acotar la
> promesa**, y ésa es la propiedad que produce la reincidencia, no cada una de sus catorce
> instancias. **Trece de catorce llevan identificador previo; NUEVE viven dentro de un remedio
> de la tanda que se juzga. En el gate anterior eran quince de diecinueve: la proporción no ha
> mejorado, ha empeorado.**

**Segunda observación de método, y también la valoro por encima de un hallazgo:** `S1-09`. **El
revisor que audita el DERIVADOR no tiene asignada la sede de la que el derivador DERIVA**
(`C-L.5`·`1bis`, doc 11 L11541), y el revisor que sí la tiene declara expresamente que no
auditó el instrumento. `R1` puso esta carencia la segunda de su §6 en el sexto gate, `EE` la
elevó a observación de método por encima de tres hallazgos, **y el manifiesto 7 repartió
igual**. Es la única cosa del APARATO de este gate que le impide ver una clase entera, y se
cierra moviendo una línea del reparto.

---

## §8 · VEREDICTO Y VALIDEZ

### §8.1 · LA VALIDEZ, que se decide antes que nada

La regla de cierre del manifiesto (§8) nombra **dos** disparadores de invalidez. Los medí los
dos, y **ninguno se dispara**:

```text
1  «CUALQUIER DIFERENCIA ENTRE LOS SOBRES DE DOS REVISORES INVALIDA EL GATE»
   Extraje los dos bloques embebidos y los comparé BYTE A BYTE contra el fichero:
   `sha256sum` → dce476f6…d9b2 en los TRES · `diff` VACÍO en los TRES pares · 196 líneas.
   NO SE DISPARA.

2  «CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA»
   `ASIGNADO − LEÍDO = ∅` para los dos revisores, con la unión de rangos cubriendo las doce
   filas y el documento 11 entero. NO SE DISPARA.  (Y no es un disparador de INVALIDEZ sino
   de insuficiencia: lo digo para no confundirlos.)

3  «LA SEDE CANÓNICA que no coincida con la huella recibida FALLA CERRADO»
   `db46edd2…d4a` en los DOS commits, y los tres digest de resolución reproducen.
   NO SE DISPARA.
```

Y añado lo que las seis obligaciones me pedían y he hecho: los **dos** digest de universo
reproducen bit a bit; el SHA-256 del manifiesto en el commit del gate reproduce; los **cuatro**
SHA de emisor y derivador en los dos commits reproducen; las **dos** rutas divergentes son las
publicadas y el sobre advierte por adelantado que la superficie de los ÁRBOLES es otra (**5**)
y publica el comando; el árbol de trabajo del repositorio auditado está limpio y en el commit
del gate.

# EL GATE ES VÁLIDO

**Es la tercera vez consecutiva.** El remedio de la ENTREGA —el sobre a un fichero externo,
emitido una vez y no transcrito— vuelve a funcionar, y esta vez lo he medido comparando los
dos bloques byte a byte antes de leer un solo hallazgo.

### §8.2 · EL VEREDICTO

No lo deduzco de que los validadores estén verdes. **Los validadores están verdes en los ocho
árboles corruptos que he construido yo esta tarde**, y eso es precisamente el hallazgo.

# INSUFICIENTE PARA F5

**`F4c` NO se cierra. Sigue ABIERTA. `F5` NO queda autorizada. `M-04` NO está superada.
`C-L.7` NO está cerrada. `C-L.5` queda CERTIFICADA (§4.1). NO he corregido nada.**

**Las razones, en orden. La primera basta por sí sola, y es una medición mía.**

**1 · `A` NO ESTÁ DEMOSTRADA.** `S1-02`, reproducido por mí y extendido a su clase completa:
OCHO ficheros de la revisión base cuyo contenido nadie mira, con `38/38`, `EXIT=0`, `porcelain`
vacío y digest anclado. **No requiere crear ningún fichero, y por eso los cinco controles
positivos que la tanda declara —los cinco reproducidos por mí— no lo tocan.** Y `S1-01`,
también reproducido: una `Ñ` en un nombre y `G-23` publica un recuento falso en verde. **Clase
`A` por la sede que fija la frontera (`DD-20`), y cuenta.**

**2 · LA SEXTA CONDICIÓN DE `O18` NO SE CUMPLE**, por **TERCER** gate consecutivo, y hoy en
**SEIS** sedes que enumero en §4.5 —el título de `G-29`, el README L244, el comentario de
`EE-11`, la promesa del derivador, la docstring de `_es_bytecode`, el comentario de `EE-17` y
el de `EE-16`—. **De las seis condiciones del Owner fallan la primera y la sexta**, que es el
mismo resultado que los dos gates anteriores.

**3 · LA CONDICIÓN DE SALIDA QUE `EE` DEJÓ ESCRITA NO SE CUMPLE.** Mitad 1 sí, mitad 2 no, y
**cuatro de las promesas falsas las escribió o ensanchó esta misma tanda**. «Se cierran
instancias y no clases» **NO pasa a deuda registrada**.

**4 · `C-L.7` VUELVE A ESTAR FALSADA**, por **SEXTA** recurrencia consecutiva, con **DOS**
documentos de retraso donde `R2-03` midió uno, y con el ordinal del último gate escrito a mano
contra la regla escrita dentro del propio bloque.

**5 · UN REMEDIO DE DOS MITADES DEL QUE SE APLICÓ UNA, Y LA REGLA QUE LO PROHÍBE SE ESCRIBIÓ EN
EL MISMO COMMIT.** `S2-01`: `00-INDICE.md`:93 es **byte-idéntica** a la que el gate anterior
falsó —`aa99111e…` en los tres árboles—, mientras el `CORRIGENDUM` §18 de ese mismo commit
escribe «*toda sede derivada que reproduzca ese desglose lo publica con el comando que lo
deriva, o remite*».

### §8.3 · LO QUE ESTE VEREDICTO **NO** AUTORIZA A DEDUCIR

```text
· NO autoriza a deducir que el gate sea inválido: es VÁLIDO, y lo decido primero.
· NO autoriza a deducir que la cobertura falle: `C-L.5` queda CERTIFICADA, y es la primera vez
  en tres gates que alguien emite la palabra.
· NO autoriza a deducir que haga falta arquitectura nueva: los catorce son clase `A`.
· NO autoriza a deducir que algo vuelva al Owner: NADA vuelve, por cuarta vez consecutiva.
· NO autoriza a deducir que la tanda trabajó mal: aplicó lo ordenado y cerró `EE-02` en su
  primer uso. Lo que falla es el ALCANCE de los remedios y la ANCHURA de sus promesas.
· NO autoriza a deducir que el trabajo esté mal encaminado: el sobre funciona por tercera vez,
  el perímetro sigue cerrado por clase, y nadie ha tenido que preguntar nada al Owner.
```

---

## §9 · REMEDIOS DETERMINADOS — QUÉ, NO CÓMO. NO APLICO NINGUNO.

| id | remedio DETERMINADO | ¿Owner? |
|---|---|---|
| **`S1-01`** | Que **las CUATRO** lecturas de Git de la batería usen separación por `NUL`, incluida `_tocados_raw` (L1920), de la que salen `tocados`, `prohibidos` de `G-23`, `_kern`/`_kern_ev`/`_kern_dir` y el contraste de prosa del checkpoint; **y** que el comentario de `EE-11` y la fila `CHECKPOINT`:3790 digan cuántas lecturas cubre el remedio, en el mismo commit en que se corrija el código. **Y que el instrumento FIJE o COMPRUEBE `core.quotePath`** en vez de depender de su valor por defecto | **NO** |
| **`S1-02`** | Que la guarda que gobierna el corpus derive también su **PROPIEDAD** y no sólo su CONJUNTO: que exista **una** sede que contraste el CONTENIDO de todo fichero gobernado contra la revisión base, y que las **OCHO** rutas hoy ciegas —`.gitignore`, `README.md`, `START_HERE.md`, `ADS-NEXT-OWNER-BRIEF.md`, `PROMPT-ARRANQUE-ADS-NEXT.md` y las tres evidencias reejecutadas— **queden cubiertas por una regla derivada, no por una lista**; **y** que el título de `G-29` y la fila `README` L244 digan qué eje cubre la guarda. **Y que el juego de controles positivos incorpore, junto a las cinco variantes que CREAN un fichero, al menos una que sólo MUTE uno de la base** | **NO** |
| **`S1-03`** | Que la **SEGUNDA** guarda de `G-29` —unicidad de bloque canónico, L3190-3200— derive `base_marca` contra **la REVISIÓN BASE** y no contra `HEAD`, como ya hace la primera; y que, mientras eso no ocurra, el título de `G-29` **no diga «CONFIRMADO O NO» de las tres sub-guardas** | **NO** |
| **`S1-04`** | Que el derivador evalúe su predicado de perímetro sobre **TODO** el árbol y no sólo en las dos zonas que hoy lo llaman, de modo que `EXCLUIDOS_PERIMETRO` publique **realmente** todo lo excluido; o, si no, que la promesa de L173-175 y la docstring de `_excluidos()` **digan las dos zonas en que vale**. **El SOBRE no puede publicar un cardinal de perímetro que sea sólo el de dos directorios** | **NO** |
| **`S1-05`** | Que la docstring de `_es_bytecode` **retire la imposibilidad que promete** —«no puede fabricarse sin dejar de ser ilegible»— y diga el predicado que ejecuta; y que el motivo publicado deje de afirmar «bytecode de CPython» de un fichero que no lo es. **Y que se resuelva expresamente qué significa «no decodifica como UTF-8»**, que hoy significa «falla CERRADO» a cuarenta líneas y «no es corpus» aquí | **NO** |
| **`S1-06`** | Que el DESAJUSTE de `EE-17` **llame a `check()`** —o que el comentario L130-131 y la fila `CHECKPOINT`:3795 dejen de decir «es ROJO» y digan «se imprime»—. Una de las dos, no las dos a medias | **NO** |
| **`S1-07`** | Que el cardinal `Cuarenta y seis` de **doc 11 L1782** se **RETIRE y se REMITA** a la sede que lo deriva —nunca se sustituya por `47`—, y que el desglose que lo sigue (`13+7+5+3+1`) se derive o se retire. **Y que el barrido que `DD-13` usó se ejecute sobre la sección ENTERA de §2.6.7 y no sólo sobre titulares en negrita**, porque es su tercera evasión | **NO** |
| **`S1-08`** | Que el emisor **importe** la función del derivador o que el comentario L297-299 **deje de decir «se usa UNA»**. La divergencia está cerrada; la afirmación, no | **NO** |
| **`S1-09`** | Que el manifiesto del gate siguiente **reparta el documento 11 de modo que quien audite el instrumento tenga asignada la sede `C-L.5`·`1bis` (L11541)**, o que asigne esa sede explícitamente a los dos. Es una línea de reparto | **NO** |
| **`S2-01`** | Que `00-INDICE.md`:93 publique el desglose **derivado de las filas del documento 26 con el comando que el `CORRIGENDUM` §18 ya escribe**, o que **remita** — que es la regla que ese mismo commit deja escrita. **El documento 26 no se toca.** Y que la fila `EE-14` del PARTE deje de presentar la mitad (b) como el remedio entero | **NO** |
| **`S2-02`** | Que `00-INDICE.md`:94 **retire el comando que `EE-10` declaró defectuoso** y publique el acotado con `sort -u`, o remita a la sede que lo publica | **NO** |
| **`S2-03`** | Que la enumeración de `based_on` **se retire y se remita** al comando que el propio bloque publica (`ls docs/evolucion/[0-9][0-9]-*.md | sort`), en vez de conservarse «por comodidad de lectura» y caducar cada gate. Reanclarla añadiendo el 26 y el 27 **cerraría la instancia y dejaría la clase**, que es lo que este expediente lleva siete gates midiendo | **NO** |
| **`S2-04`** | Que `metodo:` y `last_meaningful_event:` **remitan** al ordinal derivado en vez de escribirlo, como «Siguiente acción exacta» ya hace en el mismo fichero para la otra mitad de la regla 2 | **NO** |
| **`S2-05`** | Que el hecho 1 de la DISPUTA **acote su barrido** —el alcance correcto es la entrada de `O18`, no «el fichero entero»— y que el corchete del hecho 4 deje de declararse «el ÚNICO de los cuatro» | **NO** |

### §9.1 · ¿ALGO VUELVE AL OWNER?

# NO. NADA VUELVE AL OWNER.

**Por CUARTA vez consecutiva.** Examiné los candidatos que mi material produce y **los cuatro
caen**:

```text
· «¿Puede `F4c` cerrarse con `C` sin implementar?»          NO ES PREGUNTA NUEVA: `O18` la
  resolvió y `DD-20` fijó la frontera. Ninguno de mis catorce es `C`.
· «¿Hay que aceptar la superficie ciega de OCHO ficheros?»  NO: es un defecto de ALCANCE de
  una guarda interna, cerrable con material escrito. Clase `A`.
· «¿Debe el sobre garantizar el perímetro?»                 NO: el derivador ya promete
  publicarlo; lo que falta es que lo haga en todo el árbol. Clase `A`.
· «¿Se retira la exigencia de que el checkpoint reancle?»   NO: la regla es del propio bloque,
  y el corpus ya demuestra la forma correcta en el mismo fichero. Clase `A`.
```

**Los catorce se cierran con material que el corpus ya tiene escrito. Ninguno reinterpreta
`O17`, `O18` ni `O19`. Ninguno exige arquitectura nueva. NO FORMULO NINGUNA PREGUNTA AL OWNER.**

---

## §10 · DISCIPLINA — declaración de cierre

```text
git status --porcelain de /home/jose/ads-kernel   AL ABRIR  → VACÍO
                                                  AL CERRAR → VACÍO
HEAD al abrir y al cerrar          → 08f6da6e655d19eb9078fbd7284594162e727d3f, sin moverse
git ls-files -v | grep -vc '^H '   → 0   (ni skip-worktree ni assume-unchanged)

FICHEROS DEL REPOSITORIO AUDITADO EDITADOS, CREADOS O BORRADOS POR MÍ     ninguno
COMMITS · PUSH · PR · MERGE · RAMAS · REFS · REFLOG en el repo auditado   ninguno

LABORATORIO   `git clone /home/jose/ads-kernel <scratchpad>/ff/repo-FF`, un `base` sobre el
              COMMIT DEL GATE y UN CLON NUEVO POR ATAQUE (26 clones en total), más
              `read-tree`+`checkout-index` en `$(mktemp -d)`. Todos los commits de ataque
              viven SÓLO en los clones desechables.
INTÉRPRETE    Python 3.12.14 (shim del encargo). Con el 3.10 del sistema caen tres validadores
              por `tomllib`: es `A14`, limitación aceptada, NO un hallazgo.
GIT           WSL2, `core.quotePath` SIN FIJAR (valor por defecto `true`), y lo declaro porque
              `S1-01` depende de ello y lo medí en las dos configuraciones.
SUBAGENTE `Agent`                                                         NO USADO

NINGÚN HALLAZGO CORREGIDO, y es deliberado: quien corrige no certifica.
NADA RESUELTO POR MAYORÍA. NADA SUAVIZADO. NINGUNA HUELLA ABREVIADA A MANO.
NINGÚN HALLAZGO ACEPTADO POR AUTORIDAD: los catorce están reproducidos contra fichero y línea.
```

### §10.1 · Autocomprobación del sobre embebido

```console
$ sha256sum <scratchpad>/f4c/SOBRE-7.txt   <bloque de S1>   <bloque de S2>
dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2   los TRES
$ diff SOBRE-7.txt <bloque S1> ; diff SOBRE-7.txt <bloque S2> ; diff <S1> <S2>
(las tres, sin salida)
```

**Y el mío coincide con el de `S1` y con el de `S2`, que publican los dos
`dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2` en sus autocomprobaciones.**

---

# INSUFICIENTE PARA F5
# EL GATE ES VÁLIDO
# `C-L.5` · CERTIFICADA

**ADJUDICADOR `FF` · adjudicación cerrada. El veredicto es mío y nadie por encima lo revisa.**
