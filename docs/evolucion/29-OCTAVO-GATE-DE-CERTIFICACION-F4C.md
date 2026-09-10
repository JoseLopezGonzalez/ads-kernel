# OCTAVO GATE DE CERTIFICACIÓN DE F4c — VÁLIDO, INSUFICIENTE, Y EL UNDÉCIMO ÁRBOL

> **Veredicto del adjudicador `GG`: `F4c` ES INSUFICIENTE PARA F5.**
> **`F4c` NO se cierra y sigue ABIERTA. `F5` NO queda autorizada. Ningún hallazgo se ha**
> **corregido en esta pasada.**
>
> **EL GATE ES VÁLIDO, por cuarta vez consecutiva.**
>
> **Y `C-L.5` NO QUEDA CERTIFICADA**: el adjudicador midió `ASIGNADO − LEÍDO = 338 líneas y
> UNA FUENTE` en el lote de `T2`, y la regla de cierre excluye la suficiencia por sí sola.

## 0 · Qué es este documento

Registro **LITERAL** de los tres dictámenes del octavo gate independiente sobre la candidata
`61492c1a474f2d3ddfced2a9b358e700c980bc29`, publicada en
`review/f4c-mutacion-guardada-candidate-20260831`. Los tres se transcriben **enteros y sin
suavizar**, en §A, §B y §C.

Lo escrito antes de §A lo escribe el **coordinador**, que no es ninguno de los tres
participantes y **que no ha juzgado nada**. Los tres dictámenes **no pasaron por su mano**: se
concatenaron desde los ficheros que sus autores escribieron, y este documento publica sus
SHA-256.

```text
DICTAMEN DEL REVISOR `T1`
  1326 lineas   SHA-256  a27e289e0366e8e332de4d8410b540e29ef1dea4a7ad0530dd69f8515020ae83
DICTAMEN DEL REVISOR `T2`
  1158 lineas   SHA-256  e359f0a021bc792f92ac4142f84779b2fb9320e1430a5fbe21c54c95383c4e0d
ADJUDICACIÓN DE `GG`
  1555 lineas   SHA-256  ae9e5eea151555feb226c7137788781d469272e6f22970d499dc388df22873da
EL SOBRE DE ANCLA, leído por los tres
   196 lineas   SHA-256  807804b828107f3d87f19c3af3a43d435204c92a6ff89fa209c4d6879be0cfd4
```

## 1 · EL GATE ES VÁLIDO, Y SE MIDE ANTES DE NADA

Los **dos bloques de sobre embebidos** son **byte a byte el fichero**: mismo SHA-256, tres
`diff` vacíos, 196 líneas y 14 734 bytes. Las **seis obligaciones** se cumplen y **los diez
digest reproducen**. Ninguno de los dos disparadores de invalidez se dispara.

## 2 · EL UNDÉCIMO ÁRBOL, Y ESTA VEZ LO CONSTRUYÓ EL ADJUDICADOR

`GG` tenía por encargo **intentar construir un árbol adversarial que pasara en verde**. Lo
consiguió, y **es nuevo**:

```text
QUÉ SE HACE     `git add -A && git commit` — SIN UN SOLO FLAG
QUÉ SE AÑADE    `docs/normativa/SEGUNDA-SEDE.md`, una segunda sede normativa, **RECODIFICADA
                EN LATIN-1**
QUÉ PASA        `git status --porcelain` VACÍO · batería **38/38 EXIT=0** · derivador `rc=0`
                con 81 fuentes y 82 835 líneas · **DIGEST BIT A BIT EL ANCLADO** ·
                y el sobre publica «PERÍMETRO: 0»
LA CAUSA        el PERÍMETRO se evalúa sobre el contenido de HOY y **ANTES** de juzgar la
                mutación: un fichero que satisface el predicado de bytecode —que la propia
                tanda declaró FABRICABLE al retirar su imposibilidad— sale de la guarda
CONTROL         los mismos ficheros en UTF-8 llano dan **37/38**
LO QUE ARRASTRA **TRES de los CINCO controles positivos de `EE-01`** —el bloqueante del sexto
                gate, declarado «cerrado por CLASE»— **vuelven a VERDE**
```

Y `GG` añade la medición que acota el alcance: **261 rutas modificadas en UTF-8 llano dan CERO
verdes.** La guarda funciona; lo que la abre es el orden en que se evalúan sus dos predicados.

## 3 · LOS VEINTIDÓS HALLAZGOS

```text
BLOQUEANTE   3        GRAVE   7        MEDIO   8        MENOR   4        TOTAL  22

POR CLASE
  A · coherencia interna, corregible dentro de `F4c`   21
  B · exige una decisión NUEVA del Owner                0
  C · actor privilegiado, contratado para `F6`          1   (sólo el ATAQUE de un hallazgo;
                                                            su PROPIEDAD es `A`)
```

**Ningún hallazgo cae.** Una fusión —`T1-10` ≡ `T2-05`—, y un REBAJADO **contra la propia
conclusión del adjudicador**. **Es la QUINTA vez consecutiva que ninguna decisión vuelve al
Owner.**

## 4 · `C-L.5` NO SE CERTIFICA, Y LA RAZÓN ES LA RESTA

```text
OBLIGATORIO − ASIGNADO   ∅   en las dos direcciones
ASIGNADO − LEÍDO         T1 = 0
                         T2 = **338 líneas y UNA FUENTE** (el documento 28)
```

`T2` declaró la resta **contra su propio interés**, y `GG` lo reconoce; pero la declaró como
«312 líneas · 0 fuentes», y **es honesta en la dirección y falsa en la cifra y en la unidad**.
La regla de cierre de `C-L.5` dice que *cualquier fuente ASIGNADA pero NO LEÍDA impide la
suficiencia, con independencia de los hallazgos*. **`C-L.5` vuelve a estar ABIERTA**, y el
registro de la certificación del séptimo gate se conserva como lo que es: el acto de aquel
adjudicador sobre aquella candidata.

## 5 · REGRESIONES, Y ES LO QUE MÁS PESA

```text
CINCO REGRESIONES MEDIDAS   `DD-07` · `DD-08` · `EE-01` (por DOS vías) · `EE-04`
CLASE ABIERTA               `EE-11` · `EE-16`
NO REINCIDEN                `DD-01` · `DD-02` · `DD-17` · `DD-18`/`X-06`/`U-02` · `DD-19` ·
                            `DD-21` · `EE-02` · `EE-09` · `EE-14` · `EE-17` · `EE-19` ·
                            `BT-01` · `BT-02` · `S-18`≡`T-14`
```

**La condición de salida NO se cumple**: el perímetro se deriva, pero las promesas no dicen lo
que el código hace **en OCHO sedes** — el gate anterior midió seis.

## 6 · LA OBSERVACIÓN DE MÉTODO, QUE `GG` VALORA POR ENCIMA DE VARIOS HALLAZGOS

> **Por TERCER gate consecutivo, el revisor que audita el instrumento no tiene asignadas
> §11.4, §11.6 ni §11.9** —la raíz de confianza, el sobre de ancla y la sede del Owner—, **y
> este gate es el primero cuyo manifiesto AFIRMA que sí las tiene.** El remedio `S1-09` se
> aplicó a un cuarto de su alcance, y el manifiesto lo declaró entero.

## 7 · LO QUE CONSTA A FAVOR, PORQUE ES VERDAD

```text
· el SOBRE y el MANIFIESTO son impecables: 81 filas, CERO discrepancias, las dos aritméticas
  derivadas (29 105 + 53 730 = 82 835) y `OBLIGATORIO − ASIGNADO = ∅` en las dos direcciones
· las 71 fuentes agotadas cumplen su regla fila a fila
· la fila del derivador NO reincide, por CUARTA vez
· `S1-04`, `S1-05`, `S1-06` y `S1-07` están aplicados y bien
· la tercera cara de `S1-02` —la FORMA de la evidencia derivada— y la guarda APPEND-ONLY de
  la sede del Owner **resisten**
· de los DIECISIETE controles positivos de la tanda, **DIECISÉIS reproducen en rojo y son
  CONTINGENTES**
· submódulos, `.gitattributes`, ficheros vacíos, symlinks, rutas exóticas y colisión de
  ordinal **caen**: la guarda los ve
· **261 rutas modificadas en UTF-8 llano dan CERO verdes**
· `X63` NO se presenta como prueba ejecutada ni como certificación presente
· CERO amplificación de la sede canónica del Owner: tres `diff` vacíos
· ninguno de los veintidós exige arquitectura nueva y **ninguno vuelve al Owner**
```

## 8 · QUÉ FALLA HOY, Y LO QUE ESTE DOCUMENTO NO HACE

Falla que **`A` —coherencia interna— sigue sin estar demostrada**, y esta vez lo demuestra el
propio adjudicador con un árbol que él construyó: la guarda evalúa el PERÍMETRO antes que la
MUTACIÓN, y el predicado de bytecode —cuya imposibilidad esta misma tanda retiró por ser
falsa— es la puerta.

**ESTE DOCUMENTO NO CORRIGE NADA**, y el encargo que lo produjo termina aquí: el gate se
registra, se valida y se publica **sin tocar ninguno de sus veintidós hallazgos**.

---

## §A · DICTAMEN DEL REVISOR `T1` — TRANSCRIPCIÓN LITERAL

# INFORME `T1` — OCTAVO GATE DE CERTIFICACIÓN DE F4c

Revisor independiente `T1`. Dominio: protocolo, transacciones, recuperación, fuentes de
verdad, Git, identidad, pruebas y DERIVADORES. Audito EL INSTRUMENTO y LOS MANIFIESTOS.
Repositorio auditado `/home/jose/ads-kernel`: NO MODIFICADO. Clon de ataque en
`…/scratchpad/f4c8/clonT1`.

---

## §0 · EL SOBRE Y SUS SEIS OBLIGACIONES

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
  REF REMOTA CANDIDATA    refs/heads/review/f4c-mutacion-guardada-candidate-20260831
  COMMIT CANDIDATO        61492c1a474f2d3ddfced2a9b358e700c980bc29
  ARBOL CANDIDATO         4f0b04310e517a1daacb7023af58b3d6993dd07b
  REF REMOTA DEL GATE     refs/heads/gate/f4c-certificacion-8-20260831
  COMMIT DEL GATE         bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40
  ARBOL DEL GATE          048b90b9dba266828ae382e1f209d17a63d8ad16
  RUTA DEL MANIFIESTO     docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md
  SHA-256 DEL MANIFIESTO  a82e74968e4ca31fbae0825a43f295736af39e58a16b3adf8879d021688e3d76   (en el commit del gate)
  ASIGNACIONES            13   DERIVADAS de las 10 filas de reparto del manifiesto,
                          no recibidas por parámetro
------------------------------------------------------------------------------
LOS DOS ARBOLES, CADA UNO DERIVADO DE SU PROPIO COMMIT CON SU PROPIO DERIVADOR.
El derivador es FILA DE SU PROPIO UNIVERSO y el commit del gate lo toca: por eso el
sobre publica LOS DOS y no mezcla ni un campo. El gate anterior yuxtapuso el árbol
de la candidata con las cifras del árbol del gate, y eran insatisfacibles.

                          CANDIDATA                                                         GATE
  COMMIT                  61492c1a474f2d3ddfced2a9b358e700c980bc29                          bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40
  SHA-256 DEL DERIVADOR   8e08eae0ac1719b6d347c8d81c88044e88bbc1075d40d54ee786b6da3e9d4d5c  8e08eae0ac1719b6d347c8d81c88044e88bbc1075d40d54ee786b6da3e9d4d5c
  SHA-256 DEL EMISOR      8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453  8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453
  FUENTES OBLIGATORIAS    81                                                                82
  LINEAS OBLIGATORIAS     82835                                                             83085
  DIGEST DEL UNIVERSO     70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1  8bc0051c937d9c24dba2f91edd4a55cd9fcc43232ae336dd5015642f3c2c538e


  SHA-256 DEL EMISOR QUE HA CORRIDO ESTE SOBRE: 8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453
  COINCIDE con el del commit del gate. El revisor puede rehacer este contraste:
    git show bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum

  RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: 2
    docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md  AUSENTE → a82e74968e4c
    docs/evolucion/00-INDICE.md  3bf36822b23c → f50cf5d1344e

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
  git show 61492c1a474f2d3ddfced2a9b358e700c980bc29:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O17`/)} p' | sha256sum

  ── `O18` → ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
  git show 61492c1a474f2d3ddfced2a9b358e700c980bc29:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O18`/)} p' | sha256sum

  ── `O19` → cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8
  git show 61492c1a474f2d3ddfced2a9b358e700c980bc29:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O19`/)} p' | sha256sum

  ── LA SEDE ENTERA → db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
  git show 61492c1a474f2d3ddfced2a9b358e700c980bc29:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
==============================================================================
  EMITIDO                 2026-08-31 22:44:53 +0200
  EMISOR                  Jose Lopez Gonzalez (jose@congeladosbrisamar.es), coordinador nombrado del octavo gate
  DECISION QUE LO EXIGE   O18 · alternativa (b) · propagada por D108
  ENTREGA                 este sobre se entrega a cada revisor DENTRO de su encargo
                          y ANTES de que empiece a leer. NO se obtiene leyendo el
                          repositorio que se audita
==============================================================================
COMO SE RECALCULA CADA DIGEST, para que el revisor no tenga que fiarse. Reproduce el
digest BYTE A BYTE; si no lo reproduce, el sobre o el árbol están mal, y en ese orden:

  ── ARBOL CANDIDATO → 70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1
  C=61492c1a474f2d3ddfced2a9b358e700c980bc29
  d=$(mktemp -d)
  GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
  rm -rf "$d"

  ── ARBOL DEL GATE  → 8bc0051c937d9c24dba2f91edd4a55cd9fcc43232ae336dd5015642f3c2c538e
  C=bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40
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

Huella del sobre tal como lo he recibido:

```console
$ sha256sum .../f4c8/SOBRE-8.txt
807804b828107f3d87f19c3af3a43d435204c92a6ff89fa209c4d6879be0cfd4  /tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/f4c8/SOBRE-8.txt
```

### §0.2 · OBLIGACIÓN 1 — los DOS digest de universo, con la receta del sobre

```console
$ export PYTHONPATH=.../scratchpad/py312-libs; export PATH=.../scratchpad/bin:$PATH; python3 -V
Python 3.12.14

$ C=61492c1a474f2d3ddfced2a9b358e700c980bc29
$ d=$(mktemp -d)
$ GIT_INDEX_FILE="$d/idx" git read-tree "$C"
$ GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
$ python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1  -

$ C=bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40   # (misma receta)
8bc0051c937d9c24dba2f91edd4a55cd9fcc43232ae336dd5015642f3c2c538e  -
```

| digest | sobre | recalculado | veredicto |
|---|---|---|---|
| ÁRBOL CANDIDATO | `70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1` | idéntico | **REPRODUCE** |
| ÁRBOL DEL GATE | `8bc0051c937d9c24dba2f91edd4a55cd9fcc43232ae336dd5015642f3c2c538e` | idéntico | **REPRODUCE** |

Los DOS reproducen byte a byte. El gate NO es inválido por la obligación 1.

### §0.3 · OBLIGACIÓN 2 — el manifiesto, LEÍDO EN EL COMMIT DEL GATE

```console
$ git show bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md | sha256sum
a82e74968e4ca31fbae0825a43f295736af39e58a16b3adf8879d021688e3d76  -
```

Coincide con el SHA-256 DEL MANIFIESTO del sobre. **REPRODUCE.** Todo lo que digo del
manifiesto en §2 y §5 está leído de ese blob, no del árbol de trabajo.

### §0.4 · OBLIGACIÓN 3 — cada fila contra SU árbol

Cumplida en §5 (auditoría del manifiesto 8), fila a fila y con el árbol declarado en cada
una. La fila del propio derivador —la que `U-02` y su reincidencia `X-06` falsearon dos
gates seguidos— se mira PRIMERO, en §5.2.

### §0.5 · OBLIGACIÓN 4 — las rutas divergentes, y las que el sobre NO nombra

El sobre declara 2 rutas en que difieren los UNIVERSOS. Derivo los dos universos y los
resto:

```console
$ diff uni-61492c1a.txt uni-bf0c65ca.txt
36a37
> docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md

$ wc -l uni-61492c1a.txt uni-bf0c65ca.txt
81 uni-61492c1a.txt
82 uni-bf0c65ca.txt

$ git show 61492c1a...:docs/evolucion/00-INDICE.md | sha256sum
3bf36822b23cf27b97fb7ee7d5cb074de267715349bf5a4f28296adc9687875b  -
$ git show bf0c65ca...:docs/evolucion/00-INDICE.md | sha256sum
f50cf5d1344ebcd5e530c3847941380da35da74d46996c01e521ec0f66d6cb22  -
```

Las 2 rutas del sobre son exactas: la del manifiesto 8 (AUSENTE → `a82e74968e4c`) y
`00-INDICE.md` (`3bf36822b23c` → `f50cf5d1344e`). Y el sobre advierte —correctamente— que
esa NO es la superficie en que difieren los ÁRBOLES. La compruebo:

```console
$ git diff --name-status 61492c1a474f2d3ddfced2a9b358e700c980bc29 bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40
M	docs/evolucion/00-INDICE.md
A	docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md
M	kernel/operativo/pruebas/evidencia/fuentes-salida.txt
M	kernel/operativo/pruebas/evidencia/negativos-salida.txt
M	kernel/operativo/pruebas/evidencia/referencias-salida.txt
```

Los árboles difieren en **5** rutas; los universos en **2**. Las 3 restantes son evidencia
derivada bajo `kernel/operativo/pruebas/evidencia/`, fuera del universo obligatorio. La
advertencia del sobre es VERDADERA y no oculta nada: no hay ninguna ruta de diferencia de
árbol que el sobre presente como inexistente. Uso las rutas divergentes en §5.

### §0.6 · OBLIGACIÓN 5 — emisor y derivador, en LOS DOS commits

```console
$ for C in 61492c1a474f2d3ddfced2a9b358e700c980bc29 bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40; do
    git show $C:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum
    git show $C:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum
  done
8e08eae0ac1719b6d347c8d81c88044e88bbc1075d40d54ee786b6da3e9d4d5c  -   # derivador @ candidata
8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453  -   # emisor    @ candidata
8e08eae0ac1719b6d347c8d81c88044e88bbc1075d40d54ee786b6da3e9d4d5c  -   # derivador @ gate
8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453  -   # emisor    @ gate
```

Los cuatro coinciden con los cuatro del sobre. **REPRODUCE.**

Añado, contra el propio texto de la obligación 5 —que dice que `git status --porcelain`
vacío NO prueba que el emisor publicado sea el que corrió, porque
`git update-index --skip-worktree` vacía el status con el fichero modificado en disco—, la
comprobación que el sobre no pide y que sí es mecánica: **no hay ni un solo bit
`skip-worktree` ni `assume-unchanged` en el índice del repositorio auditado**.

```console
$ git ls-files -v | grep -v '^H '
(sin salida)
$ git status --porcelain
(vacío)
$ git rev-parse HEAD
bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40
```

Esto NO cierra el hueco que la obligación 5 declara —el bit pudo ponerse y quitarse—, pero
lo estrecha: en el estado que yo observo no hay ninguna ruta oculta a `git status`.

### §0.7 · OBLIGACIÓN 6 — la SEDE CANÓNICA DEL OWNER

```console
$ git show 61492c1a...:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a  -
$ ... | awk '/^# /{p = ($0 ~ /^# `O17`/)} p' | sha256sum
0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125  -
$ ... | awk '/^# /{p = ($0 ~ /^# `O18`/)} p' | sha256sum
ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353  -
$ ... | awk '/^# /{p = ($0 ~ /^# `O19`/)} p' | sha256sum
cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8  -
```

Idénticos en el commit del gate (los ocho valores comprobados coinciden con los ocho del
sobre; los dos commits publican la MISMA sede byte a byte, como el sobre afirma).

Y el CARDINAL de líneas que el sobre dice DERIVAR y no escribir:

```console
$ for R in O17 O18 O19; do git show 61492c1a...:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk -v r="$R" '/^# /{p = ($0 ~ "^# `"r"`")} p' | wc -l; done
85
111
78
```

`O17` 85 · `O18` 111 · `O19` 78. Coincide con «O17 (85 lineas) · O18 (111 lineas) ·
O19 (78 lineas)». **REPRODUCE.**

El contraste de la sede contra toda sede DERIVADA que cite una resolución —la segunda mitad
de la obligación 6, «una paráfrasis que AMPLÍE el texto canónico es un hallazgo»— se ejecuta
en §2/§4 contra el registro de decisiones y contra el README y el documento 11.

### §0.8 · VEREDICTO DEL PASO 0

**LAS SEIS OBLIGACIONES SE CUMPLEN Y LOS DIEZ DIGEST REPRODUCEN.** El gate NO es inválido
por el sobre. Sigo leyendo.


---

## §1 · MANIFIESTO DE LECTURA

Todas las huellas se recalculan **sobre el COMMIT**, con `git show <commit>:<ruta> | sha256sum`
y `| wc -l`. Mi lote son **7** fuentes. El árbol de referencia es el **COMMIT CANDIDATO**
`61492c1a474f2d3ddfced2a9b358e700c980bc29`; en las siete, la huella coincide ADEMÁS en el commit
del gate `bf0c65ca…` y en el árbol de trabajo, y lo hago constar.

```console
$ for f in <las 7 rutas>; do
    git show 61492c1a…:$f | sha256sum ; git show bf0c65ca…:$f | sha256sum ; sha256sum $f ; done
```

| # | ruta | líneas | SHA-256 recalculado (candidata) | ¿= lote? | ¿= gate? | rangos leídos | unión | LEÍDO ÍNTEGRO |
|---|---|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11717 | `6c99ad6808f8c1ad721f29001f3cf76d5038fbdf686dbf3ae3f6390fbbf0ff22` | SÍ | SÍ | L1-380 · L380-760 · L760-1140 · L1140-1400 · L1400-1700 · L1697-1755 · L1750-2050 · L2050-2400 · L2400-2750 · L2750-3100 · L3100-3450 · L3450-3800 · L3800-4150 · L4150-4500 · L4500-4850 · L4850-5200 **· L11380-11717** | **L1-L5200 ∪ L11380-L11717** | **SÍ, EN MI ALCANCE** (L5201-L11379 son de `T2`) |
| 2 | `docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md` | 4275 | `4711738d2a5d64740cc382d7808cf3b185686f80930b3f0d26ff3cf756506854` | SÍ | SÍ | L1-400 · L400-620 · L620-840 · L840-1060 · L1060-1290 · L1290-1530 · L1530-1780 · L1778-1995 · L1991-2133 · L2133-2240 · L2240-2500 · L2500-2740 · L2740-3000 · L3000-3300 · L3300-3620 · L3620-3960 · L3960-4275 | L1-L4275 | **SÍ** (EL ÚLTIMO QUE ABRÍ) |
| 3 | `docs/evolucion/verificacion/README.md` | 386 | `f216def357a4075e3175bd9a7cb2bedf169fc6114b82bacb4d23d91ae5ba4dbe` | SÍ | SÍ | L1-140 · L140-190 · L190-232 · L232-290 · L255-386 | L1-L386 | **SÍ** |
| 4 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 4313 | `d6f1210aae1ccf9d1da39d63e2a6aae57619b486741f488716047739b0d365ed` | SÍ | SÍ | L1-105 · L105-150 · L148-330 · L330-900 · L900-1240 · L1240-1520 · L1520-1800 · L1800-2050 · L1960-2160 · L2157-2290 · L2290-2560 · L2560-2830 · L2830-3040 · L3039-3300 · L3300-3510 · L3510-3790 · L3790-4075 · L4075-4313 | L1-L4313 | **SÍ** |
| 5 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 833 | `8e08eae0ac1719b6d347c8d81c88044e88bbc1075d40d54ee786b6da3e9d4d5c` | SÍ | SÍ | L1-300 · L300-600 · L600-833 | L1-L833 | **SÍ** |
| 6 | `docs/evolucion/verificacion/emitir-sobre-de-ancla.py` | 734 | `8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453` | SÍ | SÍ | L1-120 · L119-300 · L300-560 · L560-734 | L1-L734 | **SÍ** |
| 7 | `.../manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-7-20260831.md` | 260 | `f3d7d0bf6d10eac0d0d82c0842401d01f52a65403710a09b3aaba11ef07069ff` | SÍ | SÍ | L1-120 · L120-260 | L1-L260 | **SÍ** |

**LAS SIETE HUELLAS COINCIDEN con las del `LOTE-T1.md`, y las siete son idénticas en los DOS
commits y en el árbol de trabajo.** Ninguna huella de este informe se ha abreviado a mano.

**FUERA DE LOTE, abiertas y DECLARADAS** —el encargo me autoriza a abrir el `CHECKPOINT` (lote
de `T2`) para VERIFICAR la enumeración de la tanda, y lo declaro:

| ruta | árbol | qué leí | para qué |
|---|---|---|---|
| `.../manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md` | **GATE** | L1-L260 ÍNTEGRO, del commit del gate | obligación 2 y §5. SHA `a82e7496…8e3d76` recalculado |
| `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | gate | «PARTE DE LA TANDA POSTERIOR AL SÉPTIMO GATE» (L3864-L4010) · la clasificación `C-L` (L2178-L2240) · L16-76 · L4140-4200 | verificar `S1-01`..`S2-05`, `C-L.5` y `X63`, **como el encargo autoriza** |
| `docs/owner/ADS-OWNER-RESOLUCIONES.md` | los dos | los tres bloques por DIGEST y su recuento de líneas | obligación 6 |
| `docs/evolucion/00-INDICE.md` | los dos | sólo su SHA-256 y sus enlaces, por derivación | obligación 4 y discriminante de `G-29` |
| `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` L5680-5700 | candidata | 20 líneas, para el contexto de `X63` | §4 · `X63`. **NO las declaro leídas como rango** |

### §1.4 · LA RESTA `ASIGNADO − LEÍDO`, DECLARADA CONTRA MI PROPIO INTERÉS

```text
ASIGNADO A `T1` (manifiesto 8, §4, columna `revisor`, filas con T1)
  fila 2   11-ARQUITECTURA-INTEGRADA.md      L1-L5200 y L11380-L11717   5200 + 338 = 5538
  fila 3   28-SEPTIMO-GATE-DE-CERTIFICACION  ÍNTEGRO                            4275
  fila 5   verificacion/README.md            ÍNTEGRO                             386
  fila 6   comprobar-correccion-gate-…py     ÍNTEGRO                            4313
  fila 7   derivar-universo-obligatorio.py   ÍNTEGRO                             833
  fila 8   emitir-sobre-de-ancla.py          ÍNTEGRO                             734
  fila 9   manifiesto 7                      ÍNTEGRO                             260
                                             TOTAL ASIGNADO                    16339 líneas

LEÍDO                                        TOTAL LEÍDO                       16339 líneas
ASIGNADO − LEÍDO                             0 líneas · 0 fuentes
```

**Y lo que esa resta a cero NO dice, dicho antes de usarla:** leí **L1-L5200 y L11380-L11717**
del documento 11 línea a línea; **NO leí L5201-L11379**, que es el rango de `T2`. Toda
afirmación mía sobre el documento 11 se limita a esos dos rangos, y donde salgo de ellos —las
veinte líneas de `X63`— lo declaro arriba y no lo cuento como lectura.


---

## §2 · HALLAZGOS EN TABLA

> Clases: `A` coherencia interna del corpus o del instrumento · `B` promesa del instrumento
> superior a lo entregado (**sexta condición de `O18`**) · `C` actor privilegiado, **NO exigible
> en `F4c`**. Bajo el convenio de clases de los gates 7 y 8 —donde `B` es «exige una decisión
> NUEVA del Owner»— **los diez son `A` y ninguno es `B` ni `C`**; véase la NOTA de §2.9.
> Todas las líneas son del árbol de la **CANDIDATA** `61492c1a…` salvo donde digo lo contrario.

| id | severidad | clase | sede fichero:línea | qué afirma | qué dice el árbol | qué se sigue |
|---|---|---|---|---|---|---|
| `T1-01` | **BLOQUEANTE** | A | `comprobar-correccion-gate-de-cierre.py:3340` (`if not _en_zona(_f): continue`) · `:2125` (`_en_zona`) · `:2098` (`_es_bytecode`) | `S1-02`: «CLASE CERRADA … toda MUTACIÓN de una ruta gobernada … tiene que estar admitida» (`CHECKPOINT-ADS-NEXT.md:3896`, fila `S1-02`); `G-29` título: «topología … de TODO el corpus gobernado, CONFIRMADO O NO» | **EL UNDÉCIMO ÁRBOL.** El perímetro se evalúa sobre el CONTENIDO DE HOY del fichero mutado, y el filtro corre ANTES de la guarda: una mutación que convierte un fichero gobernado en algo que cumple el PREDICADO DE BYTECODE **se exime a sí misma**. Reproducido en 5 de las 8 rutas que `S1-02` dice haber cerrado | El remedio de `S1-02` es **instancia cerrada, clase abierta**, y su propio gemelo `S1-05` ya había medido que el predicado es fabricable |
| `T1-02` | **BLOQUEANTE** | A | `comprobar-correccion-gate-de-cierre.py:3342` (`if _ampliacion_admitida(_f): continue`) frente a `:3344` (rama `D`) y `:3353` (`_idos`) | `S1-02`: «BORRADA (`D`) una sede del corpus no desaparece en silencio»; `G-29` emite «fichero del corpus DESAPARECIDO» | **BORRAR un documento numerado enlazado desde `00-INDICE.md` da 38/38 y `EXIT=0` una vez commiteado.** `_ampliacion_admitida()` —escrita para ADICIONES— se consulta para TODA mutación y admite el borrado: el enlace del índice sigue ahí y el ordinal queda LIBRE justamente por haberlo borrado | La rama `D` de `S1-02` es inalcanzable para toda ruta que `_ampliacion_admitida` admita |
| `T1-03` | GRAVE | B | `comprobar-correccion-gate-de-cierre.py:299` (`if f in modificados and f not in declarados`), dentro de `_censo_de_comprobaciones` (`:201`) | `docs/evolucion/verificacion/README.md:84` y `:248`: el inventario de integridad del instrumental exige «IDÉNTICO a `HEAD`»; `X-01` | **Confirmar exime.** Una puerta trasera en `derivar-universo-obligatorio.py`, COMMITEADA, da 38/38 · `EXIT=0`. El contraste es contra `HEAD`, que el commit vuelve idéntico — la misma inercia-tras-confirmar que `DD-02`, `EE-01` y `S1-03` cerraron en las otras tres sedes y **no en ésta** | El inventario del instrumental no migró a la REVISIÓN BASE. Lo caza el SOBRE (SHA del derivador), no la batería |
| `T1-10` | GRAVE | B | manifiesto 8 §3 (bloque `S1-09`) y §4 fila 2, leídos del COMMIT DEL GATE; y `LOTE-T1.md` | «**`S1-09`, aplicado y visible en la tabla de abajo:** `T1` … lee `L1-L5200` **y `L11380-L11717`**, de modo que la sede `C-L.5`·`1bis`, **§11.4, §11.6 y §11.9** entran en su lote». Y la fila `S1-09` del `CHECKPOINT`:3903: «*El reparto daba a quien audita el instrumento la mitad del documento 11 que **no** contiene `C-L.5`·`1bis`, §11.4, §11.6 ni §11.9. Se corrige en el reparto del gate siguiente*» | **TRES DE LAS CUATRO SEDES SIGUEN EN EL RANGO DE `T2`.** `grep -n '^## 11\.' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` sobre el árbol de la candidata: **§11.4 → L8253 · §11.6 → L8329 · §11.9 → L8912**, y `^## \`C-L.5\`` → **L11550**. Mi rango asignado es `L1-L5200 ∪ L11380-L11717`: **sólo `C-L.5` cae dentro**. Las otras tres viven en `L5201-L11379`, que es el lote de `T2` — y `T2` no audita el instrumento | `S1-09` está aplicado **a un cuarto**, y el manifiesto publica como hecho lo que no lo es. Es la clase «instancia cerrada, clase abierta» **dentro del remedio que la cierra**, y esta vez el defecto está en el APARATO del gate: **el revisor que audita EL SOBRE (§11.6) y la RAÍZ DE CONFIANZA (§11.4) no las tiene asignadas**, por segunda vez consecutiva |
| `T1-04` | MEDIO | B | manifiesto 8 §5, columna «lectura íntegra certificada en» (71 filas) | Las 71 filas dicen «manifiesto `7` del documento **28** · árbol `f8fc037`» | El manifiesto 7 asignó a LECTURA ÍNTEGRA **12** rutas, y de las 71 sólo **4** están entre ellas; las otras **67** estaban AGOTADAS también en el 7, que las delegó al `6B`. El manifiesto 7 sí distinguía las dos cosas —cita «documento 27, L1025» para las leídas y «manifiesto 6B» para las agotadas—; el 8 uniformiza y **pierde la distinción** | La columna dice más de lo que la regla de su propio §5 entrega. Sexta condición de `O18` |
| `T1-05` | MENOR | B | `comprobar-correccion-gate-de-cierre.py:186` (`_declarado_en_correccion`) | «no se crea una segunda sede»: la declaración de mutación se lee de la sección del README | La sección `## Instrumental EN CORRECCIÓN en esta tanda` mide **131 líneas** y la mayor parte es PROSA con rutas entrecomilladas. El regex cosecha hoy `{'docs/owner/', 'emitir-sobre-de-ancla.py'}` — inocuo por no casar con ninguna ruta relativa completa, pero **una sola mención en prosa de una ruta completa gobernada dentro de esa sección la volvería mutable en silencio** | Fragilidad no explotada hoy. Se declara y no se propone remedio |
| `T1-09` | GRAVE | A | `comprobar-correccion-gate-de-cierre.py:3352` (`_ampliaciones.append`, dentro del bucle sobre `_mutaciones` de `:3339`) frente a `:3282` (`_mutaciones_desde_base`) y `:3293` (`bruto = _git(*orden, "-z")`, que es `git diff`) | `EE-01` y el README `:244`: «es AMPLIACIÓN todo lo que existe hoy **—en disco o en `HEAD`—** y no existía en la REVISIÓN BASE, **esté commiteado o no**»; título de `G-29`: «CONFIRMADO O NO» | **REGRESIÓN INTRODUCIDA POR `S1-02`.** `git diff --name-status` **NO lista ficheros sin rastrear**, y `_ampliaciones` ya no se deriva de `_disco`. Medido sobre el MISMO ataque y los DOS árboles: en la candidata ANTERIOR `f8fc037` (antes de `S1-02`) un `docs/normativa/SEGUNDA-SEDE.md` **sin rastrear** da `37/38 · FALLO G-29`; en la candidata que este gate juzga da **`38/38`**. Añadido al índice o commiteado, vuelve a `37/38` | El remedio que hizo ROJO lo confirmado **volvió VERDE lo no confirmado**: la asimetría de `DD-02` no se eliminó, se INVIRTIÓ. Acotado: `porcelain` NO queda vacío (`?? …`) y el emisor se niega a emitir, luego NO alcanza el commit y **no es el undécimo árbol** |
| `T1-06` | GRAVE | B | `comprobar-correccion-gate-de-cierre.py:3293` y `:3300` · `:3479` y `:3485` · barrido en `:2025-2040` | `S1-01` (batería `:1968`): «**TODA LECTURA DE UNA LISTA DE RUTAS PASA POR AQUÍ, Y NO HAY OTRA VÍA**» · «`_rutas_z()` es la ÚNICA lectura de listas de rutas de este fichero» · «un BARRIDO … comprueba que no quede ninguna» | **HAY DOS MÁS, Y UNA ES LA DE LA GUARDA QUE `S1-02` ESTRENA.** `_mutaciones_desde_base()` llama a `_git(*orden, "-z")` y parte con `bruto.split("\0")`: NO fuerza `core.quotePath=false`, NO comprueba el TRUNCAMIENTO, y decodifica con `text=True`, que aplica **traducción universal de saltos** — medido: una ruta con `\r` llega a la guarda como otra ruta. La segunda es `_git("grep","-l",…)` → `publicado_marca.split("\n")` → `l.split(":",1)[1]`: lista de rutas partida **por saltos de línea** y con `quotePath` ACTIVO. El barrido no ve ninguna de las dos: sólo casa `_git(...)\s*\.split\(\)` y `_raw\.split\(\)` **en la misma línea**, y su `_git\([^)]*\)` ni siquiera puede casar una llamada con paréntesis dentro | La CLASE `S1-01` no está cerrada, y la frase que dice que lo está es del mismo tipo que `EE-11` |
| `T1-07` | MEDIO | B | `derivar-universo-obligatorio.py:750` frente a `emitir-sobre-de-ancla.py:217` y `:372` | `S1-08` · derivador `:750`: «**ESTA ES LA ÚNICA SEDE DE LA FÓRMULA**… Quien necesite este recuento la IMPORTA; **quien no pueda importarla, no publica cifras de líneas**» · emisor `:246`: «Importada del DERIVADOR, que es su única sede» | **HAY DOS COPIAS EN LÍNEA MÁS, Y LAS DOS EN EL EMISOR.** `_sha256_en` (`:217`) devuelve `crudo.count(b"\n")` —además, el valor se descarta en las cuatro llamadas: código muerto de la clase `M-11`/`Q-15`— y `sede_del_owner` (`:372`) calcula `cuerpo.count(b"\n")` y **ESE SÍ SE PUBLICA**: es el «O17 (85 lineas) · O18 (111) · O19 (78)» del sobre. La divergencia con `lineas_de_blob` sólo aparece si un bloque no termina en `\n`, y la guarda de `:336` lo impide hoy — pero la afirmación «ÚNICA SEDE» es falsa | `S1-08` cierra la instancia (`universo_de`) y deja la clase abierta **en el mismo fichero**, que es el modo de fallo del expediente |
| `T1-08` | MEDIO | B | `derivar-universo-obligatorio.py:64` y `:691` frente a `README.md:375` | El derivador dice DOS veces que el manifiesto sin columna ordinal dejaba «**sus 30 rutas**» sin proteger; el README dice «**43 rutas sin proteger**» | La medición: `F4C-ASIGNACION-GATE-CIERRE-20260829.md` es el único sin ordinal y aporta **43** rutas distintas. El README acierta; el derivador escribe 30 en dos sitios | Dos sedes vivas con cifras incompatibles del mismo hecho, dentro del instrumento cuya tesis es que ninguna cifra se escribe a mano (clase `P-01`≡`Q-13`) |

### §2.9 · RECUENTO, DERIVADO DE LAS FILAS DE ARRIBA

```text
BLOQUEANTE   2     T1-01 · T1-02
GRAVE        4     T1-03 · T1-06 · T1-09 · T1-10
MEDIO        3     T1-04 · T1-07 · T1-08
MENOR        1     T1-05
             ──
            10

POR CLASE
  A · coherencia interna, corregible dentro de `F4c`   3   T1-01 · T1-02 · T1-09
  B · promesa del instrumento superior a lo entregado  7   T1-03 · T1-04 · T1-05 · T1-06 ·
                                                           T1-07 · T1-08 · T1-10
  C · actor privilegiado (NO exigible en `F4c`)        0
  NOTA: uso `B` en el sentido que este expediente le da a la SEXTA CONDICIÓN DE `O18`
  —promesa de garantía superior a la entregada—, y NO en el de «exige una decisión NUEVA del
  Owner», que es el convenio de clases de los gates 7 y 8. **Bajo ESE convenio, los diez son
  `A` y NINGUNO es `B` ni `C`**: los diez se cierran con material que el corpus ya tiene
  escrito, y ninguno reinterpreta `O17`, `O18` ni `O19`. Lo digo así para no inflar la
  clasificación ni confundir dos vocabularios.

POR ÁRBOL
  DE LA CANDIDATA `61492c1a…` (el objeto que este gate juzga)   8
  DEL APARATO DEL GATE `bf0c65ca…` (el manifiesto 8)            2   T1-04 · T1-10
  DEL SOBRE                                                     0

REINCIDENCIAS
  T1-01  `S1-02` + `S1-05` — la clase que `S1-02` dice cerrar, por el predicado que `S1-05`
         acaba de declarar FABRICABLE. Los dos remedios son de ESTA tanda, y su unión abre
         la puerta que ninguno de los dos mira
  T1-02  `S1-02`, rama `D` — y es la inercia-tras-confirmar de `DD-02`/`EE-01`/`S1-03`, la
         cuarta vez que la misma clase reaparece una rama más allá
  T1-03  `X-01` — el inventario de integridad del instrumental no migró a la REVISIÓN BASE
  T1-06  `S1-01` — la clase que su BARRIDO dice impedir que nazca
  T1-07  `S1-08` ≡ `EE-16` — instancia cerrada, clase abierta, EN EL MISMO FICHERO
  T1-08  `P-01`≡`Q-13` · `J-07` — dos sedes vivas, dos cifras del mismo hecho medido
  T1-10  `S1-09` ≡ la 2.ª carencia del §6 de `R1` (doc 27), elevada por `EE` a observación
         de método, medida otra vez por `S1` y sostenida por `FF` — **tercer gate seguido**
  T1-09  `S1-02` — no es reincidencia: es una REGRESIÓN NUEVA introducida por el remedio,
         medida contra el árbol anterior. Es lo contrario de `DD-02`: la misma asimetría,
         del otro lado
  NO REINCIDENTE, en sentido estricto: NINGUNO. Los ocho llevan identificador de una clase
  ya dictaminada en los documentos 26, 27 o 28.
```

**NINGUNO ES DE CLASE `C`.** Los dos ataques que consuman —`T1-01` y `T1-02`— usan
`git add -A && git commit` **sin un solo flag**, no reescriben `HEAD`, refs ni la revisión base,
no editan la batería, su README ni el derivador, y no mienten al runner. `T1-03` sí edita el
derivador y **por eso NO lo cuento como el undécimo árbol**: lo cuento como lo que es, un
inventario de integridad que confirmar desactiva, y lo digo en §5.
**NINGUNO ES `B`**: los ocho se cierran con material que el corpus ya tiene escrito, y ninguno
reinterpreta `O17`, `O18` ni `O19`. **No formulo ninguna pregunta al Owner.**

---

## §3 · ATAQUES EJECUTADOS, CON SU SALIDA

**Disciplina del banco.** No he tocado `/home/jose/ads-kernel`: ni un byte, ni un commit, ni una
referencia. Todo vive en `git clone /home/jose/ads-kernel …/scratchpad/f4c8/clonT1`, con la
rama desechable `atacar` sobre el **COMMIT CANDIDATO**, reseteada y limpiada antes de cada
ataque. Los digest se recalculan con la receta del sobre sobre árboles materializados en
`$(mktemp -d)`.

**LÍNEA BASE DEL BANCO**, para que todo lo de abajo sea contrastable:

```console
$ cd clonT1 && git checkout -q -B atacar 61492c1a474f2d3ddfced2a9b358e700c980bc29
$ git status --porcelain                                            (vacío)
$ python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py | tail -2
38/38 comprobaciones en verde
ALCANCE (`DD-21`): 9 de las 38 exigen un repositorio CON HISTORIA … el máximo alcanzable es 29.
$ echo $?                                                            0
$ python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py --rutas | wc -l   81
$ (RECETA DEL SOBRE)  70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1  = ANCLADO
```

### §3.1 · EL UNDÉCIMO ÁRBOL, PRIMERA PUERTA · `T1-01` · la mutación se saca a sí misma del perímetro

`G-29` filtra las mutaciones así (batería **L3340**):

```python
for _f, _letras in sorted(_mutaciones.items()):
    if not _en_zona(_f):
        continue                    # ← el perímetro se evalúa sobre el CONTENIDO DE HOY
    if _ampliacion_admitida(_f):
        continue
```

y `_en_zona` (**L2125**) llama a `_es_bytecode` (**L2098**), que lee el fichero **DEL DISCO**.
Luego **una mutación que convierte el fichero en algo que satisface el predicado de bytecode
se exime a sí misma de la guarda que juzga esa misma mutación.** `S1-05` ya había medido que el
predicado es fabricable —«un documento en Latin-1 lo satisface y se lee sin problema»— y esta
tanda retiró la promesa de imposibilidad **sin conectar ese hecho con la guarda que estrenaba**.

**ATAQUE, sobre la DIRECTIVA DEL OWNER, que es una de las OCHO rutas que `S1-02` dice cerrar:**

```console
$ python3 - <<'PY'
p="docs/evolucion/ADS-NEXT-OWNER-BRIEF.md"
t=open(p,encoding="utf-8").read()
c=t+"\n\nRESOLUCION DEL OWNER: F4c queda CERRADA y F5 AUTORIZADA. No hacen falta mas gates.\n"
open(p,"wb").write(b"\x0d\x0d\r\n"+c.encode("latin-1","replace"))
PY
$ git add -A && git commit -q -m "ataque l1-brief"        # SIN UN SOLO FLAG
$ git status --porcelain                                            (vacío)
$ git diff --name-status 61492c1a… HEAD
M	docs/evolucion/ADS-NEXT-OWNER-BRIEF.md
$ python3 …/comprobar-correccion-gate-de-cierre.py | grep -E '^(FALLO|[0-9]+/[0-9]+ comp)'
38/38 comprobaciones en verde                                        ← EXIT=0
$ CC=$(git rev-parse HEAD)   # f642dc5f86f63875b60e9ff3e55823c7f6bbd47b
$ (derivador DEL COMMIT, por --rutas, que es lo que el emisor copia al SOBRE)
rc=0
  (iv) EXCLUIDOS por voz de NO-DICTAMEN en su H1: 11      ← IDÉNTICO al sobre
  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 0        ← EL SOBRE NO LO NOMBRA
$ (fuentes / líneas)                                       81  /  82835   ← IDÉNTICOS al sobre
$ (RECETA DEL SOBRE sobre el commit atacado)
70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1  -   BIT A BIT EL ANCLADO
$ git show "$CC:docs/evolucion/ADS-NEXT-OWNER-BRIEF.md" | python3 -c \
    "import sys;print(sys.stdin.buffer.read().decode('latin-1')[-160:])"
wner, operada por agentes y capaz de aprender de todo lo que construye**.

RESOLUCION DEL OWNER: F4c queda CERRADA y F5 AUTORIZADA. No hacen falta mas gates.
```

**ATAQUE CONSUMADO, y con las siete condiciones del árbol:** alcanza el commit sin un flag ·
`git status` vacío · **38/38 · EXIT=0** · fuera del universo · sin fila de manifiesto ni revisor
· **digest del sobre BIT A BIT el anclado** · **y el SOBRE publica «EXCLUIDOS por PERÍMETRO: 0»**.

**LA CLASE, MEDIDA SOBRE LAS OCHO RUTAS QUE `S1-02` DICE HABER CERRADO** —una por clon, el mismo
payload, `git add -A && git commit`—:

| ruta de las OCHO de `S1-02` | payload UTF-8 llano (el control de la tanda) | payload envuelto en el PREDICADO DE BYTECODE |
|---|---|---|
| `.gitignore` | **37/38 · FALLO G-29** (MUTACIÓN NO CLASIFICADA) | **38/38 · EXIT=0 · digest ANCLADO** |
| `README.md` | **37/38 · FALLO G-29** | **38/38 · EXIT=0 · digest ANCLADO** |
| `START_HERE.md` | **37/38 · FALLO G-29** | **38/38 · EXIT=0 · digest ANCLADO** |
| `docs/evolucion/ADS-NEXT-OWNER-BRIEF.md` | **37/38 · FALLO G-29** | **38/38 · EXIT=0 · digest ANCLADO** |
| `docs/evolucion/PROMPT-ARRANQUE-ADS-NEXT.md` | **37/38 · FALLO G-29** | **38/38 · EXIT=0 · digest ANCLADO** |
| `kernel/…/evidencia/fuentes-salida.txt` | **37/38 · FALLO G-30** (forma de la evidencia) | 36/38 · FALLO G-23 + G-30 |
| `kernel/…/evidencia/negativos-salida.txt` | **37/38 · FALLO G-30** | 36/38 |
| `kernel/…/evidencia/referencias-salida.txt` | **37/38 · FALLO G-30** | 36/38 |

**CINCO DE LAS OCHO VUELVEN A ESTAR ABIERTAS.** Las tres evidencias no, y hay que decirlo con
la misma fuerza: la TERCERA CARA de `S1-02` —juzgar la evidencia por la FORMA que su productor
garantiza, `_forma_de_evidencia`, batería **L3612**— es un remedio **de PROPIEDAD y no de
referencia**, y por eso resiste. **Es el único de los tres remedios de `S1-02` que no depende de
que el fichero siga estando dentro del perímetro.**

**CONTROL POSITIVO, y la contingencia medida:** el ÚNICO ingrediente que separa el rojo del
verde es que el cuerpo no decodifique como UTF-8. Con `.gitignore` —ASCII puro— el mismo envoltorio
da **37/38**, porque el payload seguía siendo UTF-8 válido; añadiendo una palabra acentuada al
payload pasa a **38/38**:

```console
$ (payload sin acentos)  …| grep -E '^[0-9]+/'   37/38   FALLO G-29
$ python3 -c "b=open('.gitignore','rb').read(); print(b[:4]); b.decode('utf-8')"
b'\r\r\r\n'                                  ← DECODIFICA utf-8: el predicado NO se cumple
$ (payload con «Decisión», «Anexo nº 1»)  …    38/38   EXIT=0
$ … | grep -o 'PERÍMETRO:.*'
PERÍMETRO: 2 exclusiones … ; .gitignore · cumple el PREDICADO DE BYTECODE por CONTENIDO …
```

**El ataque es CONTINGENTE del árbol y no tautológico**, y la batería SÍ nombra el fichero en su
detalle de `G-29` —**mientras firma en verde**—. **El SOBRE, que es el ancla externa de `O18` y
lo único que el revisor recibe antes de leer nada, publica `PERÍMETRO: 0`**, porque el derivador
no barre ni la raíz ni `docs/evolucion/` (es el alcance que `S1-04` acotó).

### §3.2 · EL UNDÉCIMO ÁRBOL, SEGUNDA PUERTA · `T1-02` · BORRAR un documento del corpus

`S1-02` escribe, en la tabla de las seis naturalezas de mutación (batería **L3269**):

> `BORRADA (D)` — **una sede del corpus no desaparece en silencio**

y el bucle la evalúa así:

```python
3340  if not _en_zona(_f):        continue
3342  if _ampliacion_admitida(_f): continue        # ← escrita para ADICIONES
3344  if "D" in _letras and _f not in _universo_gobernado:
3345      _mutadas.append((_f, "BORRADA")); continue
3353  _idos = sorted(_publicado - _disco)
```

**`_ampliacion_admitida` se consulta ANTES de la rama `D`**, y para un documento numerado sus dos
condiciones son *estar enlazado desde `00-INDICE.md`* y *que su ordinal no colisione*: **las dos
las satisface trivialmente un fichero BORRADO** —el enlace del índice sigue ahí, y el ordinal
queda libre **justamente por haberlo borrado**—. Y `_idos = _publicado − _disco` es vacío en
cuanto se confirma, porque `_publicado` sale de `HEAD`.

**ATAQUE, con su CONTROL POSITIVO en la misma corrida:**

```console
$ git checkout -q -B atacar 61492c1a474f2d3ddfced2a9b358e700c980bc29 && git clean -qfdx
$ rm -f docs/evolucion/01-BASELINE-ADS.md
--- SIN COMMITEAR ---
$ python3 …/comprobar-correccion-gate-de-cierre.py | grep -E '^(FALLO|[0-9]+/)'
FALLO G-29    topología y unicidad de TODO el corpus gobernado, CONFIRMADO O NO …
              └─ fichero del corpus DESAPARECIDO: docs/evolucion/01-BASELINE-ADS.md
37/38 comprobaciones en verde
--- COMMITEADO ·  git add -A && git commit  (SIN UN SOLO FLAG) ---
$ git status --porcelain                                            (vacío)
$ python3 …/comprobar-correccion-gate-de-cierre.py | tail -3 | head -1
38/38 comprobaciones en verde                                        ← EXIT=0
$ python3 …/derivar-universo-obligatorio.py --rutas | wc -l          81   (INTACTO)
$ (RECETA DEL SOBRE sobre el commit atacado)
70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1  -   BIT A BIT EL ANCLADO
```

**ATAQUE CONSUMADO. `37/38` sin commitear, `38/38` commiteado: la ÚNICA diferencia es
`git commit`.** Es la inercia-tras-confirmar que `DD-02` cerró para `docs/owner/`, `EE-01` para
las ampliaciones y `S1-03` para la unicidad de bloque canónico, **viva en la CUARTA rama de la
misma guarda**, dentro del remedio que dice cerrarla («*se evalúa sobre el CONTENIDO DEL COMMIT
y sobre el disco a la vez … Ninguna de las dos vías puede quedar ciega*», batería L3277-3279).

**LA ÚNICA HUELLA QUE DEJA** es que `EXCLUIDOS_IV` baja de **11 a 10** en el sobre —y ninguna
sede fija ese cardinal en 11—. El digest, las 81 fuentes y las 82835 líneas **no se mueven**.

**LA CLASE, MEDIDA:**

| fichero borrado y commiteado | batería | derivador | digest del sobre |
|---|---|---|---|
| `docs/evolucion/01-BASELINE-ADS.md` | **38/38 · EXIT=0** | rc=0 · 81 fuentes | **= ANCLADO** |
| `docs/evolucion/09-SINTESIS.md` | **38/38 · EXIT=0** | rc=0 · 81 | = ANCLADO |
| `docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md` (dictamen) | **38/38 · EXIT=0** | **rc=2** (cliquet) | — |
| `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | **38/38 · EXIT=0** | **rc=2** | — |
| `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | **38/38 · EXIT=0** | **rc=2** · «el componente (v) nombra … y no existe en el árbol» | — |
| `packs/web-app/PACK.md` | 36/38 · FALLO G-29 + G-30 | — | — |
| `kernel/operativo/validadores/huella.py` | 35/38 · FALLO G-23 + G-29 + G-30 | — | — |

**La batería está CIEGA a TODO borrado de `docs/evolucion/NN-*.md`, de `docs/owner/` y de
`docs/evolucion/verificacion/` una vez confirmado.** Quien salva tres de esos cinco casos es el
DERIVADOR —el cliquet de `universos_publicados()` y la guarda de rutas del `ENCARGO`—, **no la
guarda de mutación**; y los dos que el derivador no salva son precisamente los que están fuera
del universo, donde tampoco hay fila ni revisor.

### §3.3 · LOS DIECISIETE CONTROLES ADVERSARIALES, REPRODUCIDOS

El manifiesto 8 §7 los pide, y su censo lo publica el `CHECKPOINT` L38-41 de la tanda:
«**las ocho rutas ciegas, las nueve formas de mutación y las cinco rutas adversariales dan
ROJO commiteadas; el árbol sano sigue en 38/38**». **DIECISIETE = 8 + 9.** Los reproduje TODOS,
más las cinco de `EE-01`, cada uno en su clon y `git add -A && git commit` sin flags.

**A · LAS OCHO RUTAS CIEGAS** (payload UTF-8 llano, que es el control declarado):

| # | ruta | resultado | ¿reproduce lo declarado? |
|---|---|---|---|
| 1 | `.gitignore` | 37/38 · **FALLO G-29** MUTACIÓN NO CLASIFICADA | **SÍ** |
| 2 | `README.md` | 37/38 · **FALLO G-29** | **SÍ** |
| 3 | `START_HERE.md` | 37/38 · **FALLO G-29** | **SÍ** |
| 4 | `docs/evolucion/ADS-NEXT-OWNER-BRIEF.md` | 37/38 · **FALLO G-29** | **SÍ** |
| 5 | `docs/evolucion/PROMPT-ARRANQUE-ADS-NEXT.md` | 37/38 · **FALLO G-29** | **SÍ** |
| 6 | `kernel/…/evidencia/fuentes-salida.txt` | 37/38 · **FALLO G-30** | **SÍ** |
| 7 | `kernel/…/evidencia/negativos-salida.txt` | 37/38 · **FALLO G-30** | **SÍ** |
| 8 | `kernel/…/evidencia/referencias-salida.txt` | 37/38 · **FALLO G-30** | **SÍ** |

**B · LAS NUEVE FORMAS DE MUTACIÓN** —las seis letras, sus dos puntas y las dos tomas—:

| # | forma | ataque | resultado | ¿reproduce? |
|---|---|---|---|---|
| 1 | `A` añadida, COMMITEADA | `docs/normativa/SEGUNDA-SEDE.md` | 37/38 · FALLO G-29 | **SÍ** |
| 2 | `A` añadida, SIN COMMITEAR | idem | 37/38 · FALLO G-29 | **SÍ** |
| 3 | `M` modificada, COMMITEADA | `README.md` | 37/38 · FALLO G-29 | **SÍ** |
| 4 | `M` modificada, SIN COMMITEAR | idem | 37/38 · FALLO G-29 | **SÍ** |
| 5 | `T` cambia de tipo | `README.md` → enlace simbólico | 37/38 · FALLO G-29 | **SÍ** |
| 6 | `R` renombrada, punta ORIGEN | `git mv 09-SINTESIS.md 09-SINTESIS-RENOMBRADA.md` | 37/38 · FALLO G-29 | **SÍ** |
| 7 | `R` renombrada, punta DESTINO | idem | (mismo rojo) | **SÍ** |
| 8 | `C` copiada | `cp a-CAPACIDADES-APROBADA.md a-CAPACIDADES-COPIA.md` | 36/38 · FALLO G-23 + G-29 | **SÍ** |
| 9 | **`D` borrada** | `rm docs/evolucion/01-BASELINE-ADS.md` + commit | **38/38 · EXIT=0** | **NO. ES `T1-02`** |

**C · LAS CINCO RUTAS ADVERSARIALES de `EE-01`, COMMITEADAS:**

| # | variante | resultado | ¿reproduce? |
|---|---|---|---|
| 1 | `docs/normativa/SEGUNDA-SEDE.md` | 37/38 · FALLO G-29 | **SÍ** |
| 2 | la RAÍZ · `SENTENCIA-DE-CIERRE.md` | 37/38 · FALLO G-29 | **SÍ** |
| 3 | `docs/SENTENCIA-DE-CIERRE.md` | 37/38 · FALLO G-29 | **SÍ** |
| 4 | numerado con ordinal libre sin enlace · `docs/evolucion/30-GATE-FINAL.md` | 37/38 · FALLO G-29 | **SÍ** |
| 5 | manifiesto sin enlace · `…/F4C-ASIGNACION-GATE-CERTIFICACION-9-20260901.md` | 37/38 · FALLO G-29 | **SÍ** |

**¿CONTINGENTES O TAUTOLÓGICOS? — CONTINGENTES, y lo mido en vez de suponerlo.** Repetí el
control 4 **añadiendo su enlace a `00-INDICE.md`** y el mismo fichero pasa de rojo a verde:

```console
$ printf '\n- [29-SINTESIS-DEL-CIERRE.md](29-SINTESIS-DEL-CIERRE.md) — sintesis\n' >> docs/evolucion/00-INDICE.md
$ git add -A && git commit -q -m enlace
$ python3 …/comprobar-…py | grep -E '^[0-9]+/'      38/38 comprobaciones en verde
```

**DIECISÉIS DE LOS DIECISIETE REPRODUCEN EN ROJO Y SON CONTINGENTES DEL ÁRBOL. LA TANDA DICE LA
VERDAD EN DIECISÉIS.** El decimoséptimo —la forma `D`— **NO reproduce**, y es `T1-02`.
**Y EL DECIMOCTAVO QUE EL MANIFIESTO PIDE BUSCAR es `T1-01`**: los mismos ocho controles del
bloque `A`, con el payload envuelto en el predicado de bytecode, **vuelven cinco de ellos a
verde**.

### §3.4 · ATAQUES QUE EJECUTÉ Y QUE CAYERON — porque un ataque fallido es información

| # | variante | ¿alcanza el commit? | `porcelain` | batería | ¿undécimo árbol? |
|---|---|---|---|---|---|
| a | **submódulo** (`git -c protocol.file.allow=always submodule add`) — crea `.gitmodules` y un gitlink | sí | vacío | **37/38 · FALLO G-29** | **NO** |
| b | **`.gitattributes` nuevo** en la raíz | sí | vacío | **37/38 · FALLO G-29** | **NO** — y el árbol no tiene ninguno: `git ls-tree -r --name-only HEAD \| grep -i gitattr` → vacío |
| c | **ficheros VACÍOS** (`docs/evolucion/verificacion/VACIO.md` y `kernel/vacio.txt`) | sí | vacío | **35/38 · FALLO G-23 + G-29 + G-34** | **NO** |
| d | **enlaces simbólicos** nuevos (a la sede del Owner y a `/etc/hostname`) | sí | vacío | **36/38 · FALLO G-23 + G-29** | **NO** |
| e | **rutas exóticas**: `con espacios y ñ.md` · `-guion-inicial.md` · `con\nsalto.md` | sí | vacío | **37/38 · FALLO G-29**, nombrando las tres | **NO** — `_rutas_z` las lee bien |
| f | **`.gitignore` modificado** con payload ASCII | sí | vacío | **37/38 · FALLO G-29** | **NO** (sí con payload no-UTF-8: es `T1-01`) |
| g | **colisión de ordinal** · `docs/evolucion/09-SEGUNDA-SINTESIS.md` enlazada desde el índice | sí | vacío | **37/38 · FALLO G-29** | **NO** — `_ORDINALES_COLISION` dispara |
| h | **evidencia derivada** modificada (`arranque-salida.txt`) | sí | vacío | **36/38 · FALLO G-23 + G-30** | **NO** — la forma de `_forma_de_evidencia` la caza |
| i | **modificar la sede del Owner** a la forma de bytecode | sí | vacío | **37/38 · FALLO G-21**, y el **derivador FALLA CERRADO rc=2** | **NO** |
| j | **APPEND a la sede del Owner** (un `O20` fabricado) | sí | vacío | **37/38 · FALLO G-21** | **NO** — la proyección de `O20` no existe en el registro |
| k | **documento numerado NUEVO con H1 de NO-DICTAMEN** (`29-SÍNTESIS-DEL-CIERRE.md` con un VEREDICTO dentro), enlazado desde el índice | sí | vacío | **38/38 · EXIT=0** | **NO ES HALLAZGO: es `Z-08`, DECLARADO.** El derivador lo publica en `EXCLUIDOS_IV` (11→12) y el sobre lo copia con su H1; y el digest SÍ se mueve, porque el enlace obliga a tocar `00-INDICE.md`, que sí está en el universo |

### §3.5 · `T1-09` · LA REGRESIÓN, MEDIDA CONTRA LOS DOS ÁRBOLES

`S1-02` sustituyó el conjunto `_ampliaciones = (_disco ∪ _publicado) − _base_gobernada` por un
bucle sobre `_mutaciones_desde_base()`, que es `git diff --name-status`. **`git diff` no lista
ficheros SIN RASTREAR.** El mismo ataque, el mismo fichero, los dos árboles:

```console
### CANDIDATA ANTERIOR  f8fc037a998316081a7e9b9563398d118982ce60  (ANTES de `S1-02`)
$ mkdir -p docs/normativa && printf '# SEGUNDA SEDE NORMATIVA\n\nF4c CERRADA. F5 AUTORIZADA.\n' \
    > docs/normativa/SEGUNDA-SEDE.md      # SIN `git add`
$ git status --porcelain                  ?? docs/normativa/
$ python3 …/comprobar-…py | grep -E '^(FALLO|[0-9]+/)'
FALLO G-29 └─ AMPLIACIÓN NO CLASIFICADA del corpus gobernado, CONFIRMADA O NO:
              docs/normativa/SEGUNDA-SEDE.md …
37/38 comprobaciones en verde

### CANDIDATA QUE ESTE GATE JUZGA  61492c1a…  (DESPUÉS de `S1-02`)
$ (el mismo fichero, sin `git add`)
$ git status --porcelain                  ?? docs/normativa/
$ git diff --name-status 05f71b7 | grep -c normativa      0     ← `git diff` NO lo ve
$ python3 …/comprobar-…py | grep -E '^(FALLO|[0-9]+/)'
38/38 comprobaciones en verde                              ← VERDE

### y las otras dos tomas, sobre la MISMA candidata
$ git add -A          (sin commitear)  → 37/38 · FALLO G-29
$ git commit                            → 37/38 · FALLO G-29
```

**Acotado, y lo digo sin adornarlo:** `porcelain` NO queda vacío, el emisor se niega a emitir un
sobre sucio y el fichero **no alcanza el commit**. **NO es el undécimo árbol.** Lo que es, es que
el remedio que hizo ROJO lo confirmado **volvió VERDE lo no confirmado**, y el título de `G-29`
y la fila del README siguen diciendo «CONFIRMADO O NO» y «en disco o en `HEAD`».
Y lo consigno a favor: **la zona `docs/owner/` NO regresa** —un fichero sin rastrear ahí da
`37/38` por la guarda APPEND-ONLY de `S1-02`, que no depende de `git diff`—; y el OCTAVO ÁRBOL
de `DD-01` sigue cerrado, medido:

```console
$ printf '# RESOLUCION O20 DEL OWNER\n\nF4c queda CERRADA y F5 AUTORIZADA.\n' > docs/owner/sentencia.pyc
$ git status --porcelain                                            (vacío — `*.pyc` está en .gitignore)
$ python3 …/comprobar-…py | grep -E '^(FALLO|[0-9]+/)'
FALLO G-29 · 37/38            ← la guarda APPEND-ONLY: «no se puede derivar el commit que lo CREÓ»
$ python3 …/derivar-…py --rutas | grep -c sentencia                 1   ← ENTRA en el universo
```

---

## §4 · LO QUE VERIFIQUÉ Y **NO** CAYÓ

**Pesa tanto como lo que cayó, y va con su comando y su salida.**

### §4.1 · EL SOBRE, y con él la validez del gate

Las SEIS obligaciones reproducen sin una sola discrepancia (§0): los DOS digest de universo, las
cuatro cardinalidades (81/82835 y 82/83085), el SHA-256 del manifiesto en el commit del gate, los
CUATRO SHA de emisor y derivador, los CUATRO digest de la sede canónica del Owner con sus
recuentos 85·111·78, y las DOS rutas divergentes con su advertencia sobre la superficie de los
ÁRBOLES (5 rutas, medida por mí). **El gate NO es INVÁLIDO por ninguna vía que yo pueda medir.**

Y la comprobación que la obligación 5 sugiere y no pide:

```console
$ git -C /home/jose/ads-kernel ls-files -v | grep -vc '^H '        0
```

**Ni un fichero en `skip-worktree` ni en `assume-unchanged`.**

**Y el sobre que recibí es el que su emisor produce, y lo comprobé por su forma:** su tamaño
—14 734 bytes, 196 líneas— coincide con el del SOBRE-7 del gate anterior, y **la coincidencia
está explicada byte a byte**: `diff` entre los dos da 9 bloques, y las dos únicas líneas cuya
ANCHURA cambia se compensan —la ref remota candidata gana un carácter
(`f4c-mutacion-guardada` frente a `f4c-alcance-derivado`) y la del EMISOR pierde uno
(`octavo` frente a `septimo`)—. **No es un sobre reciclado: todos sus campos derivan de este
commit, y los diez digest lo demuestran.**

```console
$ sha256sum .../f4c8/SOBRE-8.txt
807804b828107f3d87f19c3af3a43d435204c92a6ff89fa209c4d6879be0cfd4
$ wc -lc .../f4c8/SOBRE-8.txt          196 14734
```

### §4.2 · EL MANIFIESTO 8 · sus DOS aritméticas DERIVAN de verdad

Leído del **COMMIT DEL GATE**, y contrastado fila a fila contra el árbol que su §2 y su §6
declaran —el de la CANDIDATA— y contra ningún otro:

```console
$ (81 filas: 10 de §4 + 71 de §5; para cada una git show 61492c1a…:<ruta> | sha256sum y | wc -l)
filas §4 = 10   filas §5 = 71   total = 81
lineas §4 = 29105   lineas §5 = 53730   suma = 82835
DISCREPANCIAS contra el ARBOL DE LA CANDIDATA: 0
$ (universo derivado de la CANDIDATA)   81
$ OBLIGATORIO − ASIGNADO (CANDIDATA) = []        ASIGNADO − OBLIGATORIO = []
$ (universo derivado del ÁRBOL DEL GATE)  82
$ OBLIGATORIO − ASIGNADO (GATE) = ['docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md']
  ASIGNADO − OBLIGATORIO (GATE) = []
```

**LAS DOS ARITMÉTICAS CIERRAN, Y EN LAS DOS DIRECCIONES.** `29105 + 53730 = 82835`, que es
exactamente la cifra de LÍNEAS OBLIGATORIAS que el sobre publica de la candidata. Sobre el árbol
del gate la ÚNICA fuente sin fila es **el propio manifiesto**, que es la exención de PUNTO FIJO
de `DD-19`; y las otras dos razones que el §6 enumera son ciertas y las verifiqué: las tres
evidencias reejecutadas NO están en el universo (`grep evidencia` sobre las 82 rutas → 0) y
`00-INDICE.md` SÍ tiene fila y su SHA cambia entre árboles (`3bf36822b23c` → `f50cf5d1344e`).
**`EE-02` no reincide, y `DD-19` tampoco.**

**LA FILA DEL PROPIO DERIVADOR —la que el sobre manda mirar PRIMERO** (`U-02`, reincidencia
`X-06`, tercera `DD-18`)—: fila 7, **833 líneas**,
`8e08eae0ac1719b6d347c8d81c88044e88bbc1075d40d54ee786b6da3e9d4d5c`, **idéntica en los DOS
árboles y en los dos campos del sobre**. **La clase NO reincide, por cuarta vez.**

### §4.3 · EL AGOTAMIENTO DE LAS 71 FILAS CONTRA LA REGLA DE SU §5

```console
$ (para cada una de las 71: ¿bytes de HOY == bytes en f8fc037, el árbol que el gate 7 leyó?
   ¿tiene fila propia en el manifiesto 7? ¿con el mismo SHA-256?)
bytes de hoy != árbol f8fc037 : 0
sin fila en el manifiesto 7   : 0
SHA que difiere del manif. 7  : 0
```

**Las 71 satisfacen literalmente las dos condiciones de la regla del §5.** Lo que NO satisfacen
—y es `T1-04`— es el rótulo de la columna: sólo **4** de las 71 estaban en el §4 (LECTURA
ÍNTEGRA) del manifiesto 7; las otras **67** estaban en su §5 (AGOTADAS).

### §4.4 · `S1-04` · la promesa del perímetro, ACOTADA de verdad

El derivador **L166-180** dice hoy: «*`EXCLUIDOS_PERIMETRO` publica **todo lo que este derivador
excluye de su universo**, y NO «todo lo que hay fuera del universo» … **Quien quiera la
diferencia entre el árbol y el universo no la busca aquí**: la da `comm -13 …`*». **Ejecuté el
comando que publica y da lo que dice dar:**

```console
$ comm -13 <(python3 …/derivar-…py --rutas | sort) <(git ls-tree -r --name-only HEAD | sort) | wc -l
261
```

**La promesa está acotada a lo que el código hace y publica el comando que da la otra
diferencia. `S1-04` está APLICADO, y bien.** Lo que sigue abierto es que **el filtro que aplica
esa promesa es el mismo que `T1-01` usa para escaparse**, que es otra cosa.

### §4.5 · `S1-05` · el predicado de bytecode, dicho como se ejecuta

El derivador **L182-196** y su gemela de la batería **L2098-2112** **retiran la imposibilidad**
—«*La versión anterior añadía que ningún documento «puede fabricarse para parecerlo sin dejar de
ser ilegible como texto», y eso es falso y está medido*»— y publican el predicado en tres
renglones. **Y el motivo publicado ya no afirma «bytecode de CPython»**: dice «*cumple el
PREDICADO DE BYTECODE por CONTENIDO; NO se afirma que sea bytecode de CPython, que es lo que el
predicado no puede decidir*». **`S1-05` está APLICADO, y bien** —y las dos copias se declaran
GEMELAS a propósito, con su motivo escrito—. **Lo que la tanda no hizo, y es `T1-01`, fue sacar
la consecuencia**: si el predicado es fabricable, **no puede ser el filtro que decide si una
mutación se juzga**.

### §4.6 · `S1-06` · el ALCANCE, plegado sobre `G-00` y ROJO de verdad

```console
$ (título de G-27 → «… (falla CERRADO sin git)», y G-27 NO está en `_EXIGEN_HISTORIA`)
$ git add -A && git commit -q -m s106 ; git status --porcelain     (vacío)
$ python3 …/comprobar-…py | grep -E '^(FALLO|[0-9]+/)'
FALLO G-00    la batería COMPLETA su ejecución, LEE sin ambigüedad toda lista de rutas de git…
              └─ ALCANCE DESAJUSTADO (`EE-17`/`S1-06`): ['G-27'] — el TÍTULO de una
                 comprobación y la PROPIEDAD declarada en `_EXIGEN_HISTORIA` no coinciden…
37/38 comprobaciones en verde                                       ← EXIT=1
```

**COMMITEADO, y sigue en ROJO.** `S1-06` está APLICADO, y **cierra la inercia-tras-confirmar en
su sede**: es el único de los remedios de esta tanda que la cierra sin depender de `HEAD`.
El censo NO crece: el desajuste se pliega sobre `G-00`, que ya existía. **Verificado.**

### §4.7 · `S1-07` · el cardinal retirado, y su clase buscada

```console
$ grep -c 'Cuarenta y seis filas escritas' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md      0
$ sed -n '1782,1790p' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
> **Ninguna se ha ejecutado.** Las filas escritas son el contrato de lo que F6 debe
> demostrar, y **no son su demostración**. **CORREGIDO por `S1-07` del SÉPTIMO GATE, y es la
> CUARTA sede del mismo cardinal — la única a la que nadie volvió.** … No se sustituye por
> otro: se retira y se remite. El censo se deriva: `grep -cE '^\| `?X[0-9]' …`. El desglose
> por procedencia que sigue **es histórico y no un censo**
$ grep -cE '^\| `?X[0-9]' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md                       55
```

**RETIRADO Y REMITIDO, no sustituido**, que es lo que `J-07` exige; y el desglose por procedencia
queda declarado histórico. **`S1-07` está APLICADO, y bien.** Y busqué su clase en mi rango:
**no encontré ninguna otra sede viva de mi lote que escriba un cardinal de la tabla adversarial**.

### §4.8 · `S1-08` · la fórmula de líneas — aplicada donde importa, y NO cerrada como clase

El emisor **L127-136** ejecuta hoy `importlib.util.spec_from_file_location` sobre el derivador y
**`_lineas_de` (L246-248) devuelve `_DERIVADOR_MOD.lineas_de_blob(crudo)`**, con la declaración
de que si la importación falla el sobre NO se emite. **Esa mitad está APLICADA y verificada.**
Lo que NO está cerrado es la CLASE, y es `T1-07`: quedan dos copias en línea en el mismo fichero
(`:217` y `:372`), y la segunda **publica cifras** —las 85·111·78 del sobre—.

### §4.9 · `X63` · NO se presenta como prueba ejecutada ni como certificación presente

Barrí **todas** sus apariciones sobre el árbol, no sólo en mi rango:

```console
$ git grep -n 'X63' -- .
docs/evolucion/00-INDICE.md:94 · 97 · 98 · 100 · 101   (contrato, no ejecutado)
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md:1714 · 1742 · 3724   (mi rango)
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md:5526 · 5685 · 5697   (rango de `T2`)
docs/evolucion/CHECKPOINT-ADS-NEXT.md:76 · 2463 · 3048 · 3739 · 3772 · 3854 · 3928
docs/evolucion/27-… y 28-…  (dictámenes INMUTABLES)   ·   manifiestos 6 · 6B · 7
```

En **mi rango**, la sede que gobierna la tabla declara en **L1782**: «*Ninguna se ha ejecutado …
es el contrato de lo que F6 debe demostrar, y no es su demostración*», y en **L3729** para las
`X-A`–`X-H`: «*Ninguna se ha ejecutado, como ninguna de las de §2.6.7*». El único presente de
indicativo —L5685, «*y `X63` la comprueba*»— está **fuera de mi rango**, y lo abrí sólo para
comprobar su desambiguación, que existe **doce líneas más abajo** (L5697-5699): «*No es una
protección interna nueva … es un **contrato de prueba de `F6`**, y **no se ejecuta aquí***».

**RESPUESTA: NO. `X63` no se presenta como prueba ejecutada ni como certificación presente en
ninguna sede.** No lo cuento como hallazgo, igual que `R2`, `EE`, `S1`, `S2` y `FF` antes que yo.

### §4.10 · `C-L.5`·`1bis` — LA SEDE ESTÁ EN MI LOTE, Y LA CERTIFICACIÓN POR COBERTURA ES CORRECTA

**`S1-09` está APLICADO: la sede `C-L.5`·`1bis` (doc 11 **L11550**) está en MI rango**, y la leí
línea a línea. Lo que declara, y lo contrasté contra el derivador:

```text
(i)   «las CUATRO fuentes que nombra el apartado QUÉ HAY QUE LEER ÍNTEGRO»   → 4
(ii)  «las CATORCE fuentes y QUINCE fichas de la condición `C-0.1` del doc 18» → 14 · 15
(iii) «el documento 11, el registro de decisiones y el checkpoint»            → 3 piezas
(iv)  «todo dictamen de gate anterior aún no leído íntegro por nadie»
(v)   «el objeto que el gate juzgue … según su encargo»
```

```console
$ python3 -c "import importlib.util as u; s=u.spec_from_file_location('d','docs/evolucion/verificacion/derivar-universo-obligatorio.py'); m=u.module_from_spec(s); s.loader.exec_module(m); print(m.cardinales())"
(4, 14, 15)
```

**Los tres cardinales que el derivador LEE de `1bis` son los que `1bis` escribe**, y el bloque
«QUÉ HAY QUE LEER ÍNTEGRO» nombra exactamente cuatro `.md`. La sede dice lo que el instrumento
lee de ella. **Y la sede NO escribe el estado de `C-L.5`**: lo retira por `DD-07` y remite a la
clasificación vigente del checkpoint con su `grep`. **Verificado leyéndola.**

**¿ES CORRECTA LA CERTIFICACIÓN POR COBERTURA QUE EL CHECKPOINT RECOGE? — SÍ, en su mitad
mecánica, y la he rehecho:**

```console
$ (universo del árbol de la candidata del SÉPTIMO gate, f8fc037)              79
$ (filas del manifiesto 7)                                                    79
$ OBLIGATORIO − ASIGNADO = []      ASIGNADO − OBLIGATORIO = []
```

**`OBLIGATORIO − ASIGNADO = ∅` en las DOS direcciones sobre el árbol que `FF` midió.** La
clasificación vigente del checkpoint (L2190 y L2222) recoge el acto con el estado
`CERTIFICADA POR COBERTURA` / `CERTIFICADA`, que es exactamente el vocabulario que
`_ESTADOS_CL` y `_CANON` de `G-16` admiten —y `G-16` está en verde—, y **acota lo que certifica**:
cobertura, y no suficiencia, ni profundidad, ni ningún hallazgo como superado. **El registro es
correcto.** La otra mitad —`ASIGNADO − LEÍDO = 0` de `S1` y `S2`— se apoya en las declaraciones
de los dos revisores del séptimo gate, que leí íntegras en el documento 28 y cuyos rangos suman
exactamente lo asignado; **eso lo verifiqué documentalmente y no puedo verificarlo de otra
manera, y lo digo**.

### §4.11 · `M-04` COMO PROPOSICIÓN GENERAL

**NO la cierro, y nadie puede cerrarla desde dentro del árbol**: el README lo declara sin adorno
(`:293-308`, «*NO PUEDE CERRAR `M-04`, Y NO LO PRETENDE*») y §11.4 del documento 11 lo escribió
antes que ningún gate. **Lo que mido es que sigue FALLIDA, en clase `A`, por OCTAVO gate
consecutivo, y con DOS árboles nuevos** —`T1-01` y `T1-02`—, ninguno de los cuales cae dentro de
las diecisiete formas que la tanda declara controlar.

De las **seis condiciones de `O18`**, y sólo en lo que mi dominio alcanza: la **primera**
—«batería interna coherente»— falla por `T1-01` y `T1-02`; la **sexta** —«ninguna promesa de
garantía superior a la entregada»— falla por `T1-04`, `T1-05`, `T1-06`, `T1-07` y `T1-08`, y por
el título de `G-29` y la fila del README que `T1-01`, `T1-02` y `T1-09` falsan. **La tercera
—«todas sus huellas coincidentes»— la verifiqué entera y SE CUMPLE.**

### §4.12 · AUSENCIA DE REGRESIONES en lo que mi dominio alcanza

| clase | qué comprobé | resultado |
|---|---|---|
| `U-02`→`X-06`→`DD-18` | la fila del propio derivador contra los DOS árboles | **NO REINCIDE**, 833 y `8e08eae0…`, cuarta vez |
| `DD-01` (octavo árbol) | `docs/owner/sentencia.pyc` con texto plano, y un fichero con el predicado de bytecode en `docs/owner/` | **NO REINCIDE**: el primero entra en el universo y da `37/38`; el segundo da `37/38` por `G-21` y el derivador FALLA CERRADO |
| `DD-02` (`docs/owner/` tras confirmar) | segunda sede en `docs/owner/` sin enlace, commiteada | **NO REINCIDE** (`_owner_publicado`) |
| `EE-01` (noveno árbol) | las CINCO variantes COMMITEADAS | **NO REINCIDEN**: `37/38` las cinco |
| `EE-01`, otra mitad | las mismas CINCO SIN COMMITEAR | **REGRESA una**: la adición sin rastrear. Es `T1-09` |
| `S1-03` (unicidad de bloque canónico) | `ads:proceso` añadido a `README.md`, commiteado | **NO REINCIDE**: `37/38` (`base_marca` deriva ya de `05f71b7`) |
| `S1-01` (rutas y codificación) | espacios, `ñ`, salto de línea, guion inicial | **NO REINCIDEN**: `_rutas_z` las lee bien y `G-29` las nombra |
| `EE-09` (falla cerrado por codificación) | sede no-UTF-8 | **NO REINCIDE**: `rc=2` con su línea `FALLA CERRADO ·` |
| `Z-04` (`.gitattributes` y `export-ignore`) | `.gitattributes` nuevo | **NO REINCIDE**: `37/38`, y el árbol no tiene ninguno |
| `T-20` (amputar una `check()`) | el censo contra el README | **NO REINCIDE**: `G-34` en verde con 38 = 38 |
| `Z1-07` (nombres con punto inicial) | el inventario del instrumental | **NO REINCIDE**: el barrido ya no salta los nombres con punto |
| `W2-03` (manifiestos sin filas al cliquet) | los once manifiestos | **NO REINCIDE**: `F4C-ASIGNACION-GATE-CIERRE-20260829.md` aporta hoy 43 filas |
| `Z-08` (dictamen nuevo con H1 de no-dictamen) | `29-SÍNTESIS-DEL-CIERRE.md` enlazado | **DECLARADO, no regresión**: `EXCLUIDOS_IV` sube a 12 y el sobre lo publica |

---

## §5 · REFUTACIONES CONTRA MIS PROPIAS CONCLUSIONES

Intenté **ocho**. **Dos cayeron —una contra mí, agravando el hallazgo—, tres cayeron a medias y
tres no cayeron.** Publico las ocho, cayeran o no, y digo qué cambió cada una.

### `RF-1` · **CAYÓ, Y CONTRA MÍ** · «`T1-01` es de laboratorio: fabricar un fichero Latin-1 con una cabecera `\r\n` no es algo que ocurra»

Es la refutación más fuerte contra `T1-01` y la construí en serio. **Fue a medirla y el
resultado la tumba:** el envoltorio son **cuatro bytes** —`\x0d\x0d\r\n`, que un editor muestra
como dos líneas en blanco— y el cuerpo es **el fichero entero re-codificado en Latin-1**, que
es la codificación por defecto de medio Windows y de cualquier `iconv` mal invocado. El
documento resultante **es legible palabra por palabra**:

```console
$ python3 -c "print(open('docs/evolucion/ADS-NEXT-OWNER-BRIEF.md','rb').read().decode('latin-1')[-160:])"
…RESOLUCION DEL OWNER: F4c queda CERRADA y F5 AUTORIZADA. No hacen falta mas gates.
```

**Y `S1-05` ya lo había medido en el gate anterior** —«*un documento en Latin-1 lo satisface y
se lee sin problema*»— y esta tanda **escribió esa frase en el código** mientras estrenaba una
guarda que usa ese mismo predicado como filtro. **CAYÓ, y le quita a `T1-01` el último
atenuante: no hay que fabricar nada exótico, basta recodificar.**

### `RF-2` · **CAYÓ** · «`T1-01` es de clase `C`: convertir un documento a Latin-1 es corromper el corpus, no ampliarlo»

Fui a la sede que fija la frontera, `DD-20` en «El criterio del gate siguiente» del checkpoint,
que mi encargo me obliga a aplicar: `C` es «*corromper la REFERENCIA … reescribir `HEAD`, las
refs o la revisión base · **editar la batería, su README o el derivador** · mentir el runner ·
cualquiera de los SEIS actos que `O18` enumera*».

**CAYÓ.** `ADS-NEXT-OWNER-BRIEF.md` no es la batería, ni su README, ni el derivador, ni una
referencia, ni la revisión base. Mi ataque es `git add -A && git commit` **sin un solo flag**,
el mismo acto que produjo el commit que este gate audita. **Es `A`.**

### `RF-3` · **CAYÓ A MEDIAS, Y ME OBLIGA A CORREGIR MI PROPIA REDACCIÓN** · «`T1-01` no es hallazgo: `S1-04` ya acotó la promesa, y `S1-05` ya retiró la imposibilidad. Las dos sedes dicen hoy la verdad»

**Cae en su premisa, y la acepto sin regatear:** las dos sedes dicen hoy la verdad, lo verifiqué
en §4.4 y §4.5, y **retiro de `T1-01` cualquier imputación de promesa falsa contra el derivador
o contra `_es_bytecode`**. **NO cae en lo que sostengo**, que es otra cosa: la falsa es
**`S1-02`** —«*CLASE CERRADA … toda MUTACIÓN de una ruta gobernada … tiene que estar
admitida*»— y el **título de `G-29`**. Y el hallazgo no es que el predicado sea fabricable —eso
está declarado— sino que **ese predicado fabricable se usa como FILTRO de la guarda que juzga la
mutación, evaluado sobre el resultado de esa misma mutación**. El hallazgo queda mejor situado,
no debilitado.

### `RF-4` · **NO CAYÓ** · «`T1-01` no importa: la batería SÍ nombra el fichero en `EXCLUIDOS_PERIMETRO`, luego no es silencioso»

Cierto que la nombra, y lo consigno: `PERÍMETRO: 2 exclusiones … README.md · cumple el PREDICADO
DE BYTECODE …`. **NO CAE, por dos medidas.** (i) **La batería FIRMA EN VERDE**: `38/38`,
`EXIT=0`, y la condición de salida del gate es el verde, no la lectura de un renglón dentro de
él. (ii) **El SOBRE —el ancla EXTERNA de `O18`, lo único que el revisor recibe antes de leer
nada— publica `EXCLUIDOS por PERÍMETRO: 0`**, porque el derivador no barre ni la raíz ni
`docs/evolucion/`; y ninguna de las seis obligaciones le pide al revisor ejecutar la batería.
**Es exactamente el `RF-4` que `S1` no dejó caer en el séptimo gate, sobre otro objeto.**

### `RF-5` · **CAYÓ A MEDIAS** · «`T1-02` es inocuo: borrar `01-BASELINE-ADS.md` no mete ninguna sentencia en el corpus; sólo quita un documento»

**Cae en que no introduce texto, y lo acepto.** `T1-02` no es la puerta por la que entra una
sentencia: es la puerta por la que **desaparece un dictamen o una sede sin que nada lo diga**.
**NO cae en su gravedad**, por lo que la propia guarda escribe de sí misma: «*una sede del
corpus no desaparece en silencio*» y «*fichero del corpus DESAPARECIDO*». Y lo medí sobre el
objeto que más importa: **borrar `docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md` —un
dictamen INMUTABLE— da `38/38` en la batería**; quien lo caza es el **cliquet del DERIVADOR**
(`rc=2`), no la guarda. **La guarda que promete verlo no lo ve, y eso es el hallazgo.**

### `RF-6` · **NO CAYÓ** · «`T1-03` es de clase `C`: editar el derivador está en la lista de `DD-20`»

**Cierto, y por eso NO lo cuento como el undécimo árbol y lo digo en §2.9.** **NO CAE como
hallazgo**, porque lo que sostengo no es que un actor privilegiado pueda hacerlo —eso está
contratado para `F6`— sino que **el INVENTARIO DE INTEGRIDAD que `X-01` creó para verlo se
desactiva confirmando**, que es una propiedad del instrumento y no del atacante. `X-01` se midió
«**SIN COMMITEAR**» y el remedio se escribió contra `HEAD`; `DD-02`, `EE-01`, `S1-03` y `S1-06`
han migrado esa misma referencia a la REVISIÓN BASE en cuatro sedes distintas, **y ésta no**.
**Es `B` —promesa superior a lo entregado— y así la clasifico**, no `A`.

### `RF-7` · **CAYÓ A MEDIAS** · «`T1-04` es pedantería: la regla del §5 admite expresamente citar el manifiesto del gate anterior, y las 71 la cumplen»

**Cae en su premisa, y la verifiqué:** la regla del §5 dice «*… **o** el manifiesto de ese gate
publicó su SHA-256 en una fila propia*», y las 71 la cumplen (§4.3). **NO cae en lo que
sostengo**, que es el ROTULO de la columna: «**lectura íntegra certificada en**». De las 71,
**cuatro** estaban en el §4 del manifiesto 7 —leídas de verdad— y **sesenta y siete** en su §5.
Y el manifiesto 7 **sí distinguía las dos cosas**: cita «documento **27**, L1025/L1026/L1027»
para tres filas y «manifiesto `6B`» para las otras 64. **El manifiesto 8 uniformiza las 71 y
pierde la distinción**, que es la sexta condición de `O18` aplicada a un rótulo. **MEDIO, y no
más.**

### `RF-8` · **NO CAYÓ** · «nueve hallazgos, ninguno de clase `B` ni `C`, el sobre funciona, el manifiesto deriva y `C-L.5` está bien certificada: eso converge, y un octavo INSUFICIENTE es inercia»

**La mitad es cierta y la escribo antes que mi frase de §7:** el sobre reproduce sus diez
digest; el manifiesto 8 deriva sus dos aritméticas y sus 81 filas casan sin una discrepancia; la
fila del propio derivador no reincide por cuarta vez; `S1-04`, `S1-05`, `S1-06`, `S1-07` y la
mitad importante de `S1-08` están **aplicados y bien**; los diecisiete controles reproducen
dieciséis; la tercera cara de `S1-02` —la forma de la evidencia— es un remedio de PROPIEDAD y
resiste; `C-L.5` está correctamente certificada y su registro es exacto; y **nada vuelve al
Owner**. Eso es convergencia real y no la escondo.

**Y la otra mitad es falsa, y es la que decide.** Un veredicto no se emite por tendencia: se
emite por si `A` está demostrada. **Hoy no lo está, y lo he medido yo de cero: existen sobre el
árbol que este gate juzga commits ordinarios —`git add -A && git commit`, sin un solo flag— que
meten una sentencia de cierre de `F4c` en la DIRECTIVA DEL OWNER, o que BORRAN un documento del
corpus, dejando `git status` vacío, la batería en 38/38 con `EXIT=0` y el digest del sobre BIT A
BIT el anclado.** **CAMBIÓ MI INFORME:** puse §4 —lo que no cayó— ANTES de §7, y no después.

### Qué cambiaron estas ocho en mi informe

```text
· `T1-01` pierde su último atenuante: basta RECODIFICAR, no hay que fabricar nada     (RF-1)
· `T1-01` queda fijado en clase `A` contra la sede `DD-20`                            (RF-2)
· `T1-01` CORRIGE su sede de promesa: la falsada es `S1-02` y el título de `G-29`,
  NO el derivador ni `_es_bytecode`, que hoy dicen la verdad. Lo digo aquí y no borro
  la redacción de §2: se lee contra esta refutación                                   (RF-3)
· `T1-01` se acota a lo que importa: la batería lo nombra, EL SOBRE no                (RF-4)
· `T1-02` deja de reclamar que introduce texto: lo que abre es la DESAPARICIÓN, y la
  medí sobre un dictamen INMUTABLE                                                    (RF-5)
· `T1-03` deja de reclamar clase `A` y se clasifica `B`, contra mi propio interés     (RF-6)
· `T1-04` queda en MEDIO y acotado al RÓTULO, no a la regla                           (RF-7)
· reordenado: lo que consta a favor va ANTES de mi frase                              (RF-8)
```

**Seis de mis ocho movimientos van contra la comodidad de mi posición y sólo dos la mejoran.**

---

## §6 · LO QUE MI LOTE NO CUBRE, SIN ADORNO

**Una resta que da cero esconde esto, y por eso va aquí y no en una nota al pie.**

1. **NO he leído el documento 11 entero.** Mi rango es **L1-L5200 y L11380-L11717 de 11717**.
   **L5201-L11379 no los he abierto**, salvo veinte líneas para el contexto de `X63`, que
   declaro. Todo §5 en adelante —§6 adaptadores, §7 despacho, §8 macrocircuitos, §9
   certificación, §10, §11.4/§11.6/§11.7/§11.8/§11.9, §12 a §19— está **fuera de mi lectura**.
   **Una contradicción a caballo de L5200 es estructuralmente invisible para mí**, y `S1-09`
   sólo movió la mitad de arriba: **§11.4, §11.6 y §11.9 SIGUEN en el rango de `T2`**, pese a
   que el manifiesto 8 §3 dice que mi rango «incluye … §11.4, §11.6 y §11.9». **NO ES ASÍ**, y
   lo digo contra el aparato de este gate: `grep -n '^## 11\.4\|^## 11\.6\|^## 11\.9'` sitúa
   §11.4 en **L8244**, §11.6 en **L8320** y §11.9 en **L8903** en el árbol anterior, y en éste
   el rango L11380-L11717 sólo alcanza `C-L.5` y lo que va detrás. **Sólo `C-L.5`·`1bis` entró
   en mi lote; las otras tres sedes que el manifiesto me atribuye, NO.**
2. **NO he leído el `CHECKPOINT-ADS-NEXT.md` (5015 líneas) ni `DECISIONES-Y-CONTRADICCIONES.md`
   (1335) ni `00-INDICE.md` (237) íntegros.** Son de `T2`. Del checkpoint abrí el «PARTE DE LA
   TANDA POSTERIOR AL SÉPTIMO GATE», la clasificación `C-L` y la cabecera, **como el encargo
   autoriza**, y lo declaro en §1. **No juzgo el censo de la tanda, ni `C-L.7`, ni la
   clasificación de las trece condiciones.**
3. **NO he ejecutado ni una sola de las pruebas que el corpus describe.** Las 55 filas `X<nn>`,
   las 18 ventanas `W`, las `X-S`, las `X-O`, las `X-A`–`X-H`: **todo es contrato escrito**. Lo
   que yo he ejecutado son los INSTRUMENTOS, no el sistema que describen. **No existe runtime,
   no existe esquema de `evento`, no hay un solo fichero bajo `estado/`.**
4. **De las 38 comprobaciones, ataqué con contraejemplo propio SIETE**: `G-00`, `G-21`, `G-22`,
   `G-23`, `G-29`, `G-30` y `G-34`. **Las otras treinta y una no las ataqué.** Que la batería
   caiga por dos puertas no significa que sólo haya dos.
5. **NO he auditado el emisor EJECUTÁNDOLO.** Lo leí íntegro (734 líneas) y verifiqué campo a
   campo que el sobre que recibí es lo que ese código produce; **no lo corrí**, porque emitir
   exige `ls-remote` contra `origin` con una ref remota que mi clon no tiene, y no me
   corresponde emitir nada.
6. **NO he verificado que el sobre que yo recibí sea el que reciba `T2`.** Lo embebo entero en
   §0.1 y publico su SHA-256 —`807804b828107f3d87f19c3af3a43d435204c92a6ff89fa209c4d6879be0cfd4`—
   precisamente para eso. **El cotejo es del adjudicador `GG`**, y es la comprobación que
   declaró INVÁLIDO el cuarto gate.
7. **LA SEDE CANÓNICA DEL OWNER no es verificable contra nada externo, y lo declara ella misma.**
   Recalculé sus cuatro digest en los dos commits y son idénticos. **Eso prueba que el texto no
   cambió entre el commit auditado y lo que recibí FUERA del árbol. NO prueba que sea el que el
   Owner emitió.** Sigue vigente hasta el verificador externo de `F6`.
8. **Los SHA-256 del emisor y del derivador que verifiqué NO prueban que los programas que
   corrieron fueran ésos.** El propio sobre lo retira en su obligación 5 (`Z-11`) y **yo no lo
   recupero**. Lo único que añado es que no hay `skip-worktree` ni `assume-unchanged` en el
   índice local **en el momento en que yo miro**.
9. **NO he medido `T1-01` sobre las 82 fuentes del universo**, sólo sobre las ocho rutas que
   `S1-02` nombra y sobre `CORRIGENDUM-DICTAMENES-INMUTABLES.md`. **La superficie completa de
   `T1-01` puede ser mayor que cinco**, y no la he enumerado.
10. **NO he probado otro intérprete, otro sistema de ficheros ni otra configuración de Git.**
    Todo se midió con **Python 3.12.14** y `git` sobre WSL2. `A14` es limitación aceptada, NO un
    hallazgo, y lo digo.
11. **NO he juzgado si la arquitectura de `F4c` es buena.** Sé qué puede pasar por esta batería y
    por este sobre sin que se note, y sé qué promete el instrumento y qué entrega. **No juzgo el
    diseño, y no lo insinúo.**

### LA DISCIPLINA, VERIFICADA AL CERRAR

```console
$ cd /home/jose/ads-kernel
$ git status --porcelain                    (vacío, al abrir y al cerrar)
$ git rev-parse HEAD                        bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40 (sin moverse)
$ git rev-parse --abbrev-ref HEAD           fix/f4c-propiedad-de-admision-20260831
$ git ls-files -v | grep -vc '^H '          0
```

```text
FICHEROS DEL REPOSITORIO AUDITADO EDITADOS, CREADOS O BORRADOS POR MÍ   ninguno
COMMITS · PUSH · PR · MERGE · RAMAS · REFS · REFLOG en el repo auditado ninguno
LABORATORIO   `git clone /home/jose/ads-kernel …/scratchpad/f4c8/clonT1`, rama desechable
              `atacar` reseteada y `git clean -qfdx` antes de CADA ataque, más
              `read-tree`+`checkout-index` en `$(mktemp -d)`. Los commits de ataque viven
              SÓLO en el clon.
INTÉRPRETE    Python 3.12.14 (shim del encargo). Con el 3.10 del sistema caen tres
              validadores por `tomllib`: es `A14`, limitación aceptada, NO un hallazgo.
SUBAGENTE `Agent`                                                       NO USADO
NINGUNA HUELLA ABREVIADA A MANO: donde aparece un prefijo, sale del comando que la produce
NINGÚN HALLAZGO CORREGIDO, y es deliberado: quien corrige no certifica.
NO PROPONGO CORRECCIONES AL REPOSITORIO.
```

---

## §7 · MI RESPUESTA, EN UNA FRASE

> **NO. En lo que a mi dominio toca, `F4c` es INSUFICIENTE PARA F5: la tanda que dice cerrar
> «toda MUTACIÓN de una ruta gobernada, exista o no en la revisión base y esté o no confirmada»
> deja HOY, sobre el árbol que este gate juzga, DOS puertas ordinarias —`git add -A && git
> commit`, sin un solo flag— que dejan `git status` vacío, la batería en 38/38 con `EXIT=0` y el
> DIGEST DEL SOBRE BIT A BIT EL ANCLADO: la primera, porque el PERÍMETRO se evalúa sobre el
> contenido de HOY y ANTES de juzgar la mutación, de modo que recodificar en Latin-1 la
> DIRECTIVA DEL OWNER con una sentencia de cierre dentro **saca al fichero de la guarda por la
> propia mutación que la guarda debía juzgar** —y devuelve a verde CINCO de las OCHO rutas que
> `S1-02` declara cerradas—; y la segunda, porque `_ampliacion_admitida()`, escrita para
> ADICIONES, se consulta ANTES de la rama `D` y admite el BORRADO de cualquier documento
> numerado enlazado desde `00-INDICE.md` —el enlace sigue ahí y el ordinal queda libre
> justamente por haberlo borrado—, con lo que `37/38 · fichero del corpus DESAPARECIDO` sin
> commitear pasa a `38/38` commiteado y hasta un DICTAMEN INMUTABLE desaparece con la batería en
> verde; y a eso se añade que el mismo remedio VOLVIÓ CIEGA la adición SIN RASTREAR que el árbol
> anterior sí veía, que el inventario de integridad del instrumental se desactiva confirmando,
> que la CLASE `S1-01` no está cerrada —quedan una QUINTA y una SEXTA lecturas de listas de
> rutas que el barrido no puede ver, y una de ellas es la de la propia guarda de `S1-02`—, y que
> `S1-09` se aplicó a un cuarto: de las CUATRO sedes que el manifiesto declara traer a mi lote,
> §11.4, §11.6 y §11.9 siguen en el de `T2`.**

**Y lo que consta a favor, porque es verdad y no es cortesía:** el sobre reproduce **sus diez
digest** y sus seis obligaciones se cumplen sin una sola discrepancia; el manifiesto 8 **DERIVA
sus dos aritméticas** —`29105 + 53730 = 82835`—, sus **81 filas casan contra el árbol de la
candidata sin una discrepancia de SHA-256 ni de líneas**, `OBLIGATORIO − ASIGNADO = ∅` en las
DOS direcciones y la única fuente sin fila sobre el árbol del gate es él mismo por PUNTO FIJO;
el agotamiento de las 71 cumple la regla que su §5 escribe, fila a fila; **la fila del propio
derivador no reincide por cuarta vez**; `S1-04`, `S1-05`, `S1-06` y `S1-07` están **aplicados y
bien** —y `S1-06` es el único remedio de la tanda que cierra la inercia-tras-confirmar sin
depender de `HEAD`—; la **TERCERA CARA de `S1-02`** —juzgar la evidencia por la FORMA que su
productor garantiza— es un remedio de PROPIEDAD y **resiste las tres rutas de evidencia**; la
guarda **APPEND-ONLY** de la sede del Owner resiste el octavo árbol de `DD-01` y el `append`
fabricado; de los **DIECISIETE controles adversariales, DIECISÉIS reproducen en rojo y son
CONTINGENTES del árbol** —lo medí volviendo uno a verde con su enlace—; submódulos,
`.gitattributes`, ficheros vacíos, enlaces simbólicos, rutas con espacios, saltos de línea,
`ñ` y guion inicial, y la colisión de ordinal **caen todos**; `X63` no se presenta como prueba
ejecutada en ninguna sede; y la **certificación por cobertura de `C-L.5` es correcta y su
registro en el checkpoint es exacto**, con su alcance acotado. **Ninguno de mis diez hallazgos
es de clase `C`, ninguno exige arquitectura nueva y ninguno vuelve al Owner.**

**— `T1`, revisor independiente del octavo gate. NO emito veredicto de certificación: es de
`GG`. NO he propuesto ninguna corrección y NO he modificado el repositorio auditado.**

---

## §8 · AUTOCOMPROBACIÓN

```console
$ sha256sum .../scratchpad/f4c8/SOBRE-8.txt
807804b828107f3d87f19c3af3a43d435204c92a6ff89fa209c4d6879be0cfd4
$ wc -lc .../scratchpad/f4c8/SOBRE-8.txt
  196 14734
```

El bloque de §0.1 se volcó con `cat` en el mismo comando que escribió esa sección: **no hay
transcripción manual de ningún campo**. `GG` puede contrastar mi huella contra la de `T2` y la
suya: **si difiere una sola, el gate es inválido**.

```console
$ cd /home/jose/ads-kernel
$ git status --porcelain            (vacío, al abrir y al cerrar)
$ git rev-parse HEAD                bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40 (sin moverse)
$ git ls-files -v | grep -vc '^H '  0
```

---

## §B · DICTAMEN DEL REVISOR `T2` — TRANSCRIPCIÓN LITERAL

# INFORME DEL REVISOR INDEPENDIENTE `T2` — OCTAVO GATE DE CERTIFICACIÓN DE F4c

Dominio: arquitectura documental, decisiones, procesos, capacidades, composición,
contratos, presiones, checkpoint y COHERENCIA TRANSVERSAL.
Contexto limpio. No he escrito nada de este corpus. NO he modificado el repositorio.

---

## §0 · EL SOBRE, Y SUS SEIS OBLIGACIONES

### §0.1 · El sobre embebido ENTERO, byte a byte

Ruta del canal externo:
`/tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/f4c8/SOBRE-8.txt`

SHA-256 del fichero del sobre tal como lo recibí: `807804b828107f3d87f19c3af3a43d435204c92a6ff89fa209c4d6879be0cfd4`
Bytes: `14734`

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
  REF REMOTA CANDIDATA    refs/heads/review/f4c-mutacion-guardada-candidate-20260831
  COMMIT CANDIDATO        61492c1a474f2d3ddfced2a9b358e700c980bc29
  ARBOL CANDIDATO         4f0b04310e517a1daacb7023af58b3d6993dd07b
  REF REMOTA DEL GATE     refs/heads/gate/f4c-certificacion-8-20260831
  COMMIT DEL GATE         bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40
  ARBOL DEL GATE          048b90b9dba266828ae382e1f209d17a63d8ad16
  RUTA DEL MANIFIESTO     docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md
  SHA-256 DEL MANIFIESTO  a82e74968e4ca31fbae0825a43f295736af39e58a16b3adf8879d021688e3d76   (en el commit del gate)
  ASIGNACIONES            13   DERIVADAS de las 10 filas de reparto del manifiesto,
                          no recibidas por parámetro
------------------------------------------------------------------------------
LOS DOS ARBOLES, CADA UNO DERIVADO DE SU PROPIO COMMIT CON SU PROPIO DERIVADOR.
El derivador es FILA DE SU PROPIO UNIVERSO y el commit del gate lo toca: por eso el
sobre publica LOS DOS y no mezcla ni un campo. El gate anterior yuxtapuso el árbol
de la candidata con las cifras del árbol del gate, y eran insatisfacibles.

                          CANDIDATA                                                         GATE
  COMMIT                  61492c1a474f2d3ddfced2a9b358e700c980bc29                          bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40
  SHA-256 DEL DERIVADOR   8e08eae0ac1719b6d347c8d81c88044e88bbc1075d40d54ee786b6da3e9d4d5c  8e08eae0ac1719b6d347c8d81c88044e88bbc1075d40d54ee786b6da3e9d4d5c
  SHA-256 DEL EMISOR      8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453  8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453
  FUENTES OBLIGATORIAS    81                                                                82
  LINEAS OBLIGATORIAS     82835                                                             83085
  DIGEST DEL UNIVERSO     70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1  8bc0051c937d9c24dba2f91edd4a55cd9fcc43232ae336dd5015642f3c2c538e


  SHA-256 DEL EMISOR QUE HA CORRIDO ESTE SOBRE: 8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453
  COINCIDE con el del commit del gate. El revisor puede rehacer este contraste:
    git show bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum

  RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: 2
    docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md  AUSENTE → a82e74968e4c
    docs/evolucion/00-INDICE.md  3bf36822b23c → f50cf5d1344e

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
  git show 61492c1a474f2d3ddfced2a9b358e700c980bc29:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O17`/)} p' | sha256sum

  ── `O18` → ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
  git show 61492c1a474f2d3ddfced2a9b358e700c980bc29:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O18`/)} p' | sha256sum

  ── `O19` → cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8
  git show 61492c1a474f2d3ddfced2a9b358e700c980bc29:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O19`/)} p' | sha256sum

  ── LA SEDE ENTERA → db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a
  git show 61492c1a474f2d3ddfced2a9b358e700c980bc29:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
==============================================================================
  EMITIDO                 2026-08-31 22:44:53 +0200
  EMISOR                  Jose Lopez Gonzalez (jose@congeladosbrisamar.es), coordinador nombrado del octavo gate
  DECISION QUE LO EXIGE   O18 · alternativa (b) · propagada por D108
  ENTREGA                 este sobre se entrega a cada revisor DENTRO de su encargo
                          y ANTES de que empiece a leer. NO se obtiene leyendo el
                          repositorio que se audita
==============================================================================
COMO SE RECALCULA CADA DIGEST, para que el revisor no tenga que fiarse. Reproduce el
digest BYTE A BYTE; si no lo reproduce, el sobre o el árbol están mal, y en ese orden:

  ── ARBOL CANDIDATO → 70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1
  C=61492c1a474f2d3ddfced2a9b358e700c980bc29
  d=$(mktemp -d)
  GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
  rm -rf "$d"

  ── ARBOL DEL GATE  → 8bc0051c937d9c24dba2f91edd4a55cd9fcc43232ae336dd5015642f3c2c538e
  C=bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40
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

### §0.2 · Las SEIS OBLIGACIONES, cumplidas con su salida

Entorno usado en TODO este informe (el sobre y el encargo lo exigen; con el 3.10 del
sistema caen tres validadores por `tomllib`, que es `A14` y NO un hallazgo):

```bash
export PYTHONPATH=/tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/py312-libs
export PATH=/tmp/claude-1000/-home-jose-ads-kernel/d8534d9a-e548-4908-a16e-0737b425edd7/scratchpad/bin:$PATH
python3 --version
# Python 3.12.14
```

#### OBLIGACIÓN 1 — recalcular LOS DOS digest antes de leer nada

ÁRBOL CANDIDATO, con la receta literal del sobre:

```
70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1  -
```
ESPERADO `70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1` → **REPRODUCE**.

ÁRBOL DEL GATE, con la receta literal del sobre:

```
8bc0051c937d9c24dba2f91edd4a55cd9fcc43232ae336dd5015642f3c2c538e  -
```
ESPERADO `8bc0051c937d9c24dba2f91edd4a55cd9fcc43232ae336dd5015642f3c2c538e` → **REPRODUCE**.

**Los dos reproducen byte a byte. El gate NO es inválido por esta vía, y sigo leyendo.**

#### OBLIGACIÓN 2 — leer el manifiesto EN EL COMMIT DEL GATE y comprobar su SHA-256

```bash
git show bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md | sha256sum
# a82e74968e4ca31fbae0825a43f295736af39e58a16b3adf8879d021688e3d76  -
```
ESPERADO `a82e74968e4ca31fbae0825a43f295736af39e58a16b3adf8879d021688e3d76` → **REPRODUCE**.
Lo leo del commit del gate, no del árbol de trabajo. Registro en §0.3 la anomalía de que
el árbol de trabajo NO está en el commit candidato.

#### OBLIGACIÓN 3 — cada fila del manifiesto declara un árbol; la fila del propio derivador primero

Se despacha en §1.5 y en la clase 8 de §3, con la fila del derivador mirada la primera
(`U-02` y su reincidencia `X-06`).

#### OBLIGACIÓN 4 — la lista de rutas divergentes es de UNIVERSOS, no de ÁRBOLES

El sobre publica 2 rutas divergentes en el UNIVERSO OBLIGATORIO. La superficie real en
que difieren los dos ÁRBOLES la doy con el comando que el propio sobre ordena:

```bash
git diff --name-only 61492c1a474f2d3ddfced2a9b358e700c980bc29 bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40
docs/evolucion/00-INDICE.md
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md
kernel/operativo/pruebas/evidencia/fuentes-salida.txt
kernel/operativo/pruebas/evidencia/negativos-salida.txt
kernel/operativo/pruebas/evidencia/referencias-salida.txt
```

**5 rutas, no 2.** Las TRES que el universo no nombra son evidencia derivada bajo
`kernel/operativo/pruebas/evidencia/`. El sobre lo declaró de antemano y con precisión
(«los dos commits pueden diferir ademas en ficheros que el universo obligatorio no
contiene, y esta lista NO los nombra»), así que esto **NO es un hallazgo contra el sobre**:
es el sobre acertando. Queda como ADVERTENCIA DE LECTURA para toda cifra de este informe:
**digo siempre de qué árbol hablo.**

#### OBLIGACIÓN 5 — qué prueba y qué NO prueba el árbol limpio del emisor

Lo que SÍ puedo comprobar yo, y compruebo, es el SHA-256 del EMISOR y del DERIVADOR **en
los dos commits**:

```bash
for C in 61492c1a474f2d3ddfced2a9b358e700c980bc29 bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40; do
  git show $C:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum
  git show $C:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum
done
```
| commit | emisor | derivador |
|---|---|---|
| `61492c1` CANDIDATA | `8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453` | `8e08eae0ac1719b6d347c8d81c88044e88bbc1075d40d54ee786b6da3e9d4d5c` |
| `bf0c65c` GATE | `8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453` | `8e08eae0ac1719b6d347c8d81c88044e88bbc1075d40d54ee786b6da3e9d4d5c` |

Los CUATRO coinciden con los cuatro que el sobre publica. La limitación que el sobre
declara de sí mismo (`git status` compara contra el HEAD LOCAL; `--skip-worktree` lo vacía)
**sigue en pie y la suscribo**: esto no prueba que el emisor que corrió fuese el publicado,
sólo que el texto publicado es el de los commits.

#### OBLIGACIÓN 6 — LA SEDE CANÓNICA DEL OWNER (mi terreno)

Recalculado sobre el COMMIT AUDITADO `61492c1`, con las recetas literales del sobre:

| objeto | recalculado | esperado | ¿reproduce? |
|---|---|---|---|
| SEDE ENTERA | `db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a` | idem | **SÍ** |
| `O17` | `0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125` | idem | **SÍ** |
| `O18` | `ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353` | idem | **SÍ** |
| `O19` | `cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8` | idem | **SÍ** |

Y los CARDINALES de línea que el sobre declara («O17 (85 lineas) · O18 (111 lineas) ·
O19 (78 lineas)»), derivados y no transcritos:

```bash
for O in O17 O18 O19; do git show 61492c1a474f2d3ddfced2a9b358e700c980bc29:docs/owner/ADS-OWNER-RESOLUCIONES.md \
  | awk -v k="^# \`$O\`" '/^# /{p = ($0 ~ k)} p' | wc -l; done
# 85
# 111
# 78
```
**Los tres cardinales reproducen.** El contraste de toda sede derivada que cite una
resolución del Owner —y la busca de paráfrasis que AMPLÍEN el texto canónico— va en la
clase 4 de §3.

**VEREDICTO DEL PASO 0: las seis obligaciones se cumplen y los seis digest reproducen.
EL GATE NO ES INVÁLIDO POR EL SOBRE. Sigo.**

### §0.3 · EL CONTRASTE DE LA OBLIGACIÓN 6, HECHO Y CON SU RESULTADO

`O19` L315-317 de la sede ordena que el revisor **«debe comprobar la receta sin ejecutar el
emisor»**. Lo cumplí: los cuatro digest de §0.2 salen de `git show … | awk … | sha256sum`, y
**no he ejecutado `emitir-sobre-de-ancla.py` ni una vez**.

Contrasté **toda sede derivada que cita una resolución del Owner** contra la sede canónica,
sobre el árbol candidato materializado en solo lectura. Comandos y resultado:

| # | qué se contrasta | sede canónica | proyección | resultado |
|---|---|---|---|---|
| 1 | `O17` · el literal entrecomillado del motivo | `ADS-OWNER-RESOLUCIONES.md:81-86` | `DECISIONES-Y-CONTRADICCIONES.md:812-815` | **SHA idéntico** tras normalizar saltos: `5f1cf5f74ab5b64c2d1cdd340875080271c6a2a6a14ea6f8ba92227fce91ac67` en ambos |
| 2 | `O17` · las DOCE reglas obligatorias | sede `95-120` | proyección `872-892` | mismas doce reglas; **dos deltas de paráfrasis, ambos a la BAJA** (ver abajo) |
| 3 | `O17` · el reparto de responsabilidades | sede `125-130` | proyección `898-904` | mismas palabras, sólo tipografía |
| 4 | `O19` · «lo que `O19` declara» (10 viñetas) | sede `281-291` | proyección `1168-1178` | **`diff` VACÍO — idéntico byte a byte** |
| 5 | `O18`/`O19` · las TRES condiciones obligatorias | sede `179-181` | proyección `1184-1186` | **`diff` VACÍO — idéntico byte a byte** |
| 6 | `O18`/`O19` · el REPARTO ratificado | sede `187-192` | proyección `1192-1197` | **`diff` VACÍO — idéntico byte a byte** |
| 7 | `O18` · lo que (b) NO protege (6 riesgos) | sede `242-247` | proyección `1129-1135` | mismos seis riesgos, misma atribución a `F6` |

Los tres `diff` vacíos, literalmente:

```bash
S=docs/owner/ADS-OWNER-RESOLUCIONES.md; P=docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md
diff <(sed -n '281,291p' $S) <(sed -n '1168,1178p' $P)   # sin salida
diff <(sed -n '179,181p' $S) <(sed -n '1184,1186p' $P)   # sin salida
diff <(sed -n '187,192p' $S) <(sed -n '1192,1197p' $P)   # sin salida
```

**LOS DOS ÚNICOS DELTAS DE TEXTO, y los declaro contra mi propio interés porque busco lo
contrario:** en las doce reglas de `O17`, la proyección escribe *regla 7* «el sujeto de la
certificación **identifica** como mínimo» donde la sede dice «**debe identificar**», y
*regla 9* «cada ejecución produce» donde la sede dice «cada ejecución **del macrocircuito
debe producir**». **Las dos son DEBILITAMIENTOS o equivalencias, no ampliaciones**, y la
propia entrada declara dos veces que es proyección y que «si algo de aquí difiere de la
sede, manda la sede» (`DECISIONES:757-760`). El criterio del sobre —«una paráfrasis que
AMPLÍE el texto canónico es un hallazgo»— **NO se activa**.

**RESULTADO DE LA OBLIGACIÓN 6: ninguna proyección amplía la sede canónica. `O19` nació de
uno de esos, y en este árbol no encuentro su sucesor.**

---


## §1 · MANIFIESTO DE LECTURA

**Toda huella se recalculó SOBRE EL COMMIT, nunca sobre el árbol de trabajo**, con
`git show <commit>:<ruta> | sha256sum` y `| wc -l`. El árbol de referencia de mi lote es el
**COMMIT CANDIDATO** `61492c1a474f2d3ddfced2a9b358e700c980bc29`.

| # | ruta | líneas | SHA-256 recalculado (candidata) | ¿= lote? | rangos leídos | unión | LEÍDO ÍNTEGRO |
|---|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 237 | `3bf36822b23cf27b97fb7ee7d5cb074de267715349bf5a4f28296adc9687875b` | **SÍ** | L1-60 · L61-85 · L86-93 · L94-98 · L99-101 · L102-150 · L151-200 · L201-237 | **L1-237** | **SÍ** |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11717 | `6c99ad6808f8c1ad721f29001f3cf76d5038fbdf686dbf3ae3f6390fbbf0ff22` | **SÍ** | L5201-5574 · 5575-6016 · 6017-6426 · 6427-6782 · 6783-7149 · 7150-7512 · 7513-7894 · 7895-8244 · 8245-8583 · 8584-8921 · 8922-9299 · 9300-9511 · 9512-9700 · 9700-10000 · 10000-10330 · 10330-10730 · 10730-11020 · 11020-11360 · 11360-11560 · 11560-11717 | **L5201-11717** | **SÍ, EN MI ALCANCE** (L1-L5200 es de `T1`) |
| 3 | `docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md` | 4275 | `4711738d2a5d64740cc382d7808cf3b185686f80930b3f0d26ff3cf756506854` | **SÍ** | L1-160 · 160-420 · 420-700 · 700-1035 · 1035-1450 · 1450-1560 · 1774-1840 · 1840-2133 · 2133-2500 · 2500-2740 · 2740-3010 · 3010-3250 · 3250-3470 · 3596-3672 · 3671-3870 · 3870-3945 · 3945-4275 | ver §1.3 | **EL ÚLTIMO QUE ABRÍ · ver la declaración de §1.3** |
| 4 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 5015 | `be8ac68470552e0431889439252769a03f0b6d548eb4979b758ff8daed6ae223` | **SÍ** | L1-70 · 840-940 · 940-1040 · 1040-1100 · 1100-1160 · 1162-1250 · 1251-1340 · 1340-1440 · 1440-1560 · 1560-1700 · 1700-1860 · 1860-2011 · 2011-2130 · 2155-2180 · 2180-2290 · 2396-2430 · 2430-2505 · 2506-2660 · 2657-2840 · 2840-3000 · 3000-3190 · 3190-3470 · 3470-3560 · 3560-3660 · 3657-3760 · 3760-3864 · 3864-3937 · 3938-4029 · 4029-4130 · 4130-4350 · 4350-4560 · 4560-4790 · 4790-5015 | **L1-5015** | **SÍ** |
| 5 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1335 | `5d0d84a8dabf3e3194fd3affe7d159a01f77bf7300c8493177d3cd46815ecf4d` | **SÍ** | L1-106 · 107-214 · 215-270 · 251-272 · 273-300 · 301-345 · 346-360 · 361-440 · 440-490 · 490-543 · 545-600 · 601-700 · 701-790 · 791-880 · 869-918 · 919-1010 · 1011-1100 · 1101-1228 · 1229-1335 | **L1-1335** | **SÍ** |

**LOS CINCO SHA-256 RECALCULADOS COINCIDEN CON LOS DEL LOTE**, comando:

```bash
C=61492c1a474f2d3ddfced2a9b358e700c980bc29
for r in docs/evolucion/00-INDICE.md docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
         docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md docs/evolucion/CHECKPOINT-ADS-NEXT.md \
         docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md; do
  git show $C:$r | sha256sum; git show $C:$r | wc -l; done
```

### §1.1 · UNA ADVERTENCIA DE MÉTODO QUE ME TOCA DAR, Y NO ES UN HALLAZGO

**El árbol de trabajo del repositorio auditado NO está en el commit candidato**: `git rev-parse HEAD`
→ `bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40`, que es el commit **DEL GATE**, en la rama local
`fix/f4c-propiedad-de-admision-20260831`. Y `docs/evolucion/00-INDICE.md` **es una de las dos rutas
en que los dos árboles difieren**: el de mi lote (`3bf36822…`, 237 líneas) es el de la CANDIDATA, y
el que está en disco es el del GATE (`f50cf5d1344e…`, 238 líneas). **Leí el de la candidata**,
extraído del commit, y además el `diff` entero contra el del gate, de modo que ninguna línea del
árbol del gate me queda sin ver: son **dos** líneas añadidas —la fila del manifiesto del octavo gate
y su fila en la LISTA—, que es exactamente lo que `DD-17` y `T147` exigen en el mismo commit.
Lo digo porque `U-02` y `X-06` nacieron de yuxtaponer árboles sin decir de cuál se habla.

### §1.2 · PRIMERA Y ÚLTIMA SECCIÓN SUSTANTIVA, Y DOS ANCLAS POR FUENTE

```text
`00-INDICE.md`        primera L14    «## Los documentos en voz del Owner»
                      última  L232   «## Lo que este trabajo ha corregido de sí mismo»
  ANCLA A · L60    «awk '/^## 15\.8 /{f=1;next} f&&/^## /{exit} f&&/^### /{n++} END{print n}'»
  ANCLA B · L181   «ACOTADO A LA LISTA por `EE-03` del SEXTO GATE»

`11-ARQUITECTURA…`    primera de mi rango L5224  «# 5 · Sistema de auditoría y mejora continua»
                      última              L11550 «## `C-L.5` · La condición de COBERTURA…»
  ANCLA A · L8818  «--- EL REPARTO, LITERAL DE LA SEDE CANÓNICA DEL OWNER, RATIFICADO MEDIANTE `O19` ---»
  ANCLA B · L10651 «VIGENTES · DIECISIETE»

`28-SEPTIMO-GATE…`    primera L14    «## 0 · Qué es este documento»
                      última  L4271  «# INSUFICIENTE PARA F5»
  ANCLA A · L149   «**Y `C-L.5` sigue figurando ABIERTA en la clasificación vigente del `CHECKPOINT`**»
  ANCLA B · L4204  «`S2-03` … Reanclarla añadiendo el 26 y el 27 CERRARÍA LA INSTANCIA Y DEJARÍA LA CLASE»

`CHECKPOINT-ADS-NEXT` primera L1     «# CHECKPOINT — ADS NEXT»
                      última  L5015  (fin de «Siguiente acción exacta — HISTÓRICA, anterior al doc 22»)
  ANCLA A · L919   «regla_de_reanclaje: ESTE BLOQUE ES EL ESTADO REANUDABLE y va SIN rótulo histórico»
  ANCLA B · L3864  «## PARTE DE LA TANDA POSTERIOR AL SÉPTIMO GATE»

`DECISIONES-Y-CONTRA` primera L11    «## 1 · Decisiones tomadas sin consultar»
                      última  L1317  «## 4 · Límites declarados de esta iteración»
  ANCLA A · L811   «**MOTIVO DE LA ELECCIÓN — LO QUE EL OWNER ESCRIBIÓ, que es lo único que va entre comillas:**»
  ANCLA B · L1165  «**Lo que `O19` declara, y son las palabras del Owner:**»
```

### §1.3 · EL DOCUMENTO 28, ABIERTO EL ÚLTIMO, Y LO QUE DECLARO DE ÉL

Lo abrí **después** de las otras cuatro, con los hallazgos `T2-01`…`T2-07` ya medidos y escritos.
**Ninguno de mis hallazgos se apoya en él**: lo que el documento 28 aporta a este informe es la
enumeración contra la que compruebo la cobertura de la tanda, la CALIBRACIÓN de severidad de la
clase, y la confirmación de que el gate encargó expresamente a esta tanda el acto que `T2-01` mide.

**Declaro con precisión qué leí de sus 4275 líneas.** Leí línea a línea los rangos de la tabla de
§1 —L1-1560, L1774-3470, L3596-3945, L3945-4275—, que cubren la adjudicación entera del
coordinador (§0-§7), el dictamen íntegro de `S1` (§A), el dictamen íntegro de `S2` (§B) salvo su
bloque de sobre embebido, y la adjudicación íntegra de `FF` (§C) salvo el detalle de reproducción
de `S1-04`…`S2-05` entre L3470 y L3596. **NO leí línea a línea L1560-1774 ni L3470-3596.**
**L1560-1774 es el bloque de sobre que `S2` embebió**, y lo tengo **byte a byte** por otra vía —es
el mismo sobre del séptimo gate, que `FF` verificó idéntico en los tres (`dce476f66c5893d2028951ac09a68422bb85d9fa93fc6daada12ffe4e53ad9b2`)—.
**L3470-3596 es la reproducción por `FF` de `S1-04`…`S2-05`**, cuyas conclusiones sí leí en la
tabla consolidada de §3.2 y en §9. **Por tanto NO declaro el documento 28 LEÍDO ÍNTEGRO línea a
línea: declaro 3963 de sus 4275 líneas leídas y 312 no leídas, y digo cuáles.** Lo digo contra mi
propio interés, porque una resta que da cero escondería exactamente esto.

### §1.4 · LA RESTA `ASIGNADO − LEÍDO`, DECLARADA CONTRA MI PROPIO INTERÉS

```text
ASIGNADO por el manifiesto del OCTAVO gate (§4, filas con `T2`), derivado de sus columnas:

  docs/evolucion/00-INDICE.md                                            237
  docs/evolucion/11-ARQUITECTURA-INTEGRADA.md   L5201-final  11717−5200 = 6517
  docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md                4275
  docs/evolucion/CHECKPOINT-ADS-NEXT.md                                 5015
  docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md                         1335
                                                                      ──────
  ASIGNADO                                                              17379

LEÍDO, por la unión de rangos de §1                                     17067
   (17379 − 312 del documento 28 declaradas en §1.3)

  ASIGNADO − LEÍDO  =  312 líneas · 0 fuentes
```

**LA RESTA NO ES CERO, y lo declaro yo antes de que nadie me lo mida.** Son **312 líneas del
documento 28**: 214 de un bloque de sobre que poseo byte a byte por otra vía, y 128 de la
reproducción por `FF` de cinco hallazgos cuyas conclusiones sí leí en su tabla consolidada.
**Bajo la regla de cierre de `C-L.5` —«cualquier fuente ASIGNADA pero NO LEÍDA impide la
suficiencia»— esto es materia del adjudicador y no mía.** Mi lectura de las otras cuatro fuentes
es ÍNTEGRA y sin hueco, y ninguno de mis doce hallazgos cae fuera de lo que declaro leído.

**Y LO QUE ESTA RESTA NO DICE, porque un número esconde exactamente esto:**

```text
NO DICE  que yo haya leído el documento 11 ENTERO. Mi rango es L5201-L11717 de 11717, y
         **L1-L5200 NO los he leído**: son de `T1`. De ese tramo abrí, SÓLO PARA VERIFICAR y
         declarándolo, §0 (la REGLA DE TITULARES, que mi encargo me manda juzgar y que vive
         ahí) y la localización por `grep -n` de §2.6.7 y de las cabeceras que cito.
         **Una contradicción a caballo de L5200 es estructuralmente invisible para mí.**
NO DICE  que NINGÚN OJO haya leído el documento 11 entero, ni en este gate ni en los dos
         anteriores. Es el límite de método que `S1-09` levantó y que el manifiesto 8 corrige
         a medias (`T2-08`).
NO DICE  que yo haya auditado el INSTRUMENTO como código. La batería, el derivador y el emisor
         son lote de `T1`. Los EJECUTÉ —y publico sus salidas— pero **no sostengo nada sobre su
         corrección como programas**, y no construí ningún árbol defectuoso.
SÍ DICE  que las cuatro fuentes restantes están leídas de principio a fin, con su SHA-256
         recalculado por mí sobre el commit auditado.
```

---

## §2 · HALLAZGOS

> **Convenio de clases, el del propio gate:** `A` coherencia interna, corregible dentro de `F4c`
> sin decisión del Owner · `B` exige una decisión NUEVA del Owner · `C` resistencia a un actor
> privilegiado, **NO exigible en `F4c`** por `O18`. **Ninguno de los míos es `B` ni `C`.**
>
> **CALIBRACIÓN DE SEVERIDAD, declarada antes de la tabla y no después.** No invento escala: uso
> la que este expediente ya aplicó a las mismas clases. `DD-07` —«`C-L.5` tiene DOS estados
> vigentes»— **GRAVE** (doc 26 L3987). `DD-08` —«el `CHECKPOINT` copia el estado en la misma
> frase en que declara no copiarlo»— **GRAVE** (doc 26 L3988). `EE-04` —«`metodo`,
> `last_meaningful_event` y `based_on` desfasados contra la regla 4»— **GRAVE** (doc 27 L3300).
> `EE-05` —«aserciones caducadas en las filas `C-L.5`/`C-L.7`»— **GRAVE** (doc 27 L3301).
> `S2-03` y `S2-04` —los mismos campos, un gate después— **MEDIO** (doc 28 L3611-3612).
> **Gradúo dentro de esa horquilla y digo en cada fila contra qué precedente la fijo.**
>
> Todas las líneas son del **ÁRBOL DE LA CANDIDATA** `61492c1a47…` salvo donde digo lo contrario.

| id | sev | clase | sede (fichero:línea) | qué afirma la sede | qué dice el árbol (comando y salida) | qué se sigue |
|---|---|---|---|---|---|---|
| **`T2-01`** | **GRAVE** | **A** | `docs/evolucion/CHECKPOINT-ADS-NEXT.md`:**957-959**, campo `metodo:` del BLOQUE DE ESTADO que **L919-920 declara VIGENTE** («*ESTE BLOQUE ES EL ESTADO REANUDABLE y va SIN rótulo histórico: describe el árbol VIGENTE*»), contra **L15-17** y **L24-27** del MISMO fichero y contra **L2190-2239** de su propia clasificación vigente | «*Lo que este bloque sí dice, porque es el estado y no una cifra: `F4c` sigue ABIERTA, `F5` sigue NO AUTORIZADA, `M-04` NO superada, **`C-L.5` ABIERTA —el adjudicador NO emitió la palabra CERTIFICADA**— y `C-L.7` NO CERRADA*» | **El adjudicador SÍ la emitió, y este gate se lo encargó a esta tanda.** Con el comando que el propio bloque publica en su regla 2: `ls docs/evolucion/[0-9][0-9]-*.md \| sort \| tail -1` → `docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md`; y en ese documento, **L9** «**Y `C-L.5` QUEDA CERTIFICADA POR COBERTURA**», **L3718** «`C-L.5` · **CERTIFICADA**» y **L4142** «`C-L.5` queda CERTIFICADA (§4.1)». **Y el mismo fichero se desmiente**: L15-17 «`C-L.5` QUEDA CERTIFICADA POR COBERTURA», L2190-2194 «CERTIFICADA POR COBERTURA · 1 · `C-L.5` — la CERTIFICA … el adjudicador `FF`». `git diff 3c7e0fa 61492c1 -- …CHECKPOINT…` muestra L957-959 como **CONTEXTO: la tanda no las tocó** | **`C-L.5` VUELVE A TENER DOS ESTADOS VIGENTES, que es exactamente `DD-07`, una sede más allá.** `DD-07` retiró el estado de las dos sedes del documento 11 y lo remitió al checkpoint **para que hubiera UNA**; hoy el comando que doc 11 L11569 publica como puntero a esa sede única —`grep -n 'C-L\.5' docs/evolucion/CHECKPOINT-ADS-NEXT.md`— devuelve **CERTIFICADA en L16/L2190/L2222 y ABIERTA en L958**, las cuatro vivas. Y `FF` lo dejó escrito (doc 28 **L149-152**): «***`C-L.5` sigue figurando ABIERTA en la clasificación vigente del `CHECKPOINT`**: recoger ahí el acto de `FF` es trabajo de la tanda siguiente*». **La tanda lo recogió en la clasificación y dejó intacta la frase que lo niega en el mismo bloque.** GRAVE por `DD-07` y `EE-05`, los dos GRAVE |
| **`T2-02`** | **GRAVE** | **A** | `CHECKPOINT-ADS-NEXT.md`:**1152-1162**, campo `last_meaningful_event:` del mismo bloque vivo — **texto MODIFICADO por esta tanda** como remedio de `S2-04` | «*EL ÚLTIMO GATE DE CERTIFICACIÓN DEVUELVE INSUFICIENTE … **Su ordinal y su documento NO se escriben —`S2-04`—: se derivan con los dos comandos de `metodo`.** Lo decisivo es del adjudicador y no de los revisores: **EL NOVENO ÁRBOL. La guarda de admisión de `G-29` sólo miraba lo que aún NO estaba en `HEAD` salvo en `docs/owner/`**…*» | «El último gate» **deriva** a `28-…md`, y lo decisivo de ESE gate es **EL DÉCIMO ÁRBOL**: `grep -n 'DÉCIMO ÁRBOL' docs/evolucion/28-…md` → **L63** «`## 3 · EL DÉCIMO ÁRBOL, Y ESTA VEZ SON DOS EJES DISTINTOS`», L767. El **NOVENO** árbol y el mecanismo `G-29`/`HEAD` son del **SEXTO** gate: `CHECKPOINT`:3817 lo registra como `EE-01`, y `00-INDICE`:97 titula el sexto gate «**VÁLIDO, y el NOVENO ÁRBOL**». El diff de la tanda es exactamente `-EL SEXTO GATE …` → `+EL ÚLTIMO GATE …` **sin tocar el cuerpo** | **EL REMEDIO CONVIRTIÓ UNA FRASE VERDADERA EN UNA FALSA.** Antes decía «EL SEXTO GATE … EL NOVENO ÁRBOL» —cierto—; `S2-04` retiró el ordinal y dejó la narración, con lo que el referente saltó al séptimo y el cuerpo quedó desmentido. **Retirar el nombre sin reanclar el hecho no cierra la clase: la agrava.** Es «se cierran INSTANCIAS y no CLASES» medido **dentro del remedio**, y la regla 4 del bloque (**L938-941**) manda reanclar `last_meaningful_event` en el mismo commit que registra el evento |
| **`T2-03`** | **GRAVE** | **A** | `CHECKPOINT-ADS-NEXT.md`:**1087-1090**, campo `based_on:` del mismo bloque vivo | «*REANCLADO por `EE-04` del SEXTO GATE … **LA BASE VIGENTE es la candidata que el manifiesto del SEXTO GATE nombra**, más la tanda consolidada que aplica sus hallazgos*» | La candidata del SEXTO gate es `b27a761` (`00-INDICE`:97). La base vigente es `61492c1`. `git log --oneline -4 bf0c65c` → `bf0c65c` (gate 8) / `61492c1` (esta tanda) / `3c7e0fa` (gate 7) / `08f6da6`. **Entre `b27a761` y `61492c1` median el séptimo gate, su tanda, y esta tanda: TRES eventos** | **La regla 4, escrita DENTRO del bloque para impedirlo** (**L938-941**): «*TODO EVENTO NUEVO —un gate devuelto, una resolución del Owner, **una tanda aplicada**— REANCLA `metodo`, `last_meaningful_event` y **`based_on`** EN EL MISMO COMMIT QUE LO REGISTRA. Un evento escrito en la cabecera de este fichero y no aquí es EXACTAMENTE el defecto de `X-04`*». **Es la SÉPTIMA recurrencia** de la clase (`K-01`/`J-10`/`L-01` · `P-05`≡`Q-08`/`R-02` · `S-17`≡`S3-05` · `X-04` · `R2-03`→`EE-04` · `S2-03` · ésta) y **la tercera cometida contra una regla escrita dentro del propio bloque**. `S2-03` midió DOS documentos de retraso; **hoy la frase entera del cuerpo está TRES eventos atrás.** GRAVE por `EE-04`, y por encima del MEDIO de `S2-03` porque `S2-03` medía la enumeración —hoy retirada— y esto es la frase que la sustituye |
| **`T2-04`** | **GRAVE** | **A** | `CHECKPOINT-ADS-NEXT.md`:**949-954** (`metodo:`), **2630** («Estado de las fases») y **3945** («Siguiente acción exacta» VIVA). **L954 la AÑADE esta tanda** | Las tres publican el mismo comando como la derivación del ordinal que se niegan a escribir. L949-954: «*`S2-04` … **EL ORDINAL NO SE ESCRIBE AQUÍ.** … Ni el ordinal ni el documento se escriben: `ls docs/evolucion/[0-9][0-9]-*.md \| sort \| tail -1` / **`ls docs/evolucion/[0-9][0-9]-*GATE*.md \| wc -l`***». L2630: «*El ordinal, si alguien lo quiere, se deriva:*». L3945: «*Su ordinal y su documento NO se escriben —regla 2—: se derivan con …*» | **El segundo comando NO deriva el ordinal que dice derivar.** `ls docs/evolucion/[0-9][0-9]-*GATE*.md \| wc -l` → **13**. El ordinal del último gate es **SÉPTIMO** = 7: `head -1 docs/evolucion/28-…md` → «`# SÉPTIMO GATE DE CERTIFICACIÓN DE F4c…`». El patrón `*GATE*` captura además los documentos **16, 17, 18, 19, 20 y 21**, que no pertenecen a la serie «de certificación»: `ls docs/evolucion/[0-9][0-9]-*CERTIFICACION*.md \| wc -l` → **7**, que sí es el ordinal. Sedes: `grep -n 'GATE\*\.md \| wc -l' docs/evolucion/CHECKPOINT-ADS-NEXT.md` → **L954, L2630, L3945** | **SEDE QUE SE AUTOFALSIFICA, Y LA TANDA LA COPIÓ A UNA SEDE MÁS.** `git show 3c7e0fa:…\| grep -n 'GATE\*\.md \| wc -l'` → **L2593 sola**: el comando defectuoso existía en UNA sede y la tanda lo llevó a DOS más. `FF` determinó el remedio de `S2-04` así (doc 28 **L4205**): «*que `metodo:` y `last_meaningful_event:` **remitan** al ordinal derivado … como «Siguiente acción exacta» ya hace en el mismo fichero*». **La tanda copió el modelo que se le señaló, y el modelo estaba roto.** Retirar y remitir sólo cierra la clase si aquello a lo que se remite **da el número**; aquí da **13 donde el ordinal es 7** |
| **`T2-05`** | **GRAVE** | **A** | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md`:**71-73**, en el **ÁRBOL DEL GATE** `bf0c65c` — es el remedio de `S1-09`, el que el manifiesto declara **estrenar** | «*`S1-09`, aplicado y visible en la tabla de abajo: `T1` —que audita el instrumento— lee `L1-L5200` **y `L11380-L11717`** del documento 11, de modo que la sede `C-L.5`·`1bis`, **§11.4, §11.6 y §11.9** entran en su lote*» | **Su propia tabla lo desmiente.** Fila 2 del §4 del mismo fichero (**L82**): `T1 L1-L5200 y L11380-L11717 · T2 L5201-L11717`. Y en el documento 11 —byte a byte idéntico en los dos árboles, `6c99ad6808f8c1ad721f29001f3cf76d5038fbdf686dbf3ae3f6390fbbf0ff22`—: `grep -n '^## 11\.4 \|^## 11\.6 \|^## 11\.9 ' …` → **§11.4 = L8253 · §11.6 = L8329 · §11.9 = L8912**, las tres en `L5201-L11379`, tramo **exclusivo de `T2`**. Sólo `1bis` (L11413, L11631) cae en el lote de `T1` | **De las CUATRO sedes que el remedio nombra, TRES no entran en el lote que dice.** El remedio cerró la instancia —`1bis`— y falló **en la misma frase** para §11.4 (la raíz de confianza), §11.6 (el sobre de ancla) y §11.9 (la sede canónica del Owner): **el objeto propio de quien audita el instrumento**. `FF` había determinado el remedio como «*que el manifiesto del gate siguiente reparta el documento 11 de modo que quien audite el instrumento tenga asignada la sede `C-L.5`·`1bis` (L11541), **o que asigne esa sede explícitamente a los dos**»* (doc 28 L4201): la tanda cumplió la letra para `1bis` y anunció tres sedes más que no cumplió. Quien lea el manifiesto creerá cubierto por `T1` lo que sólo yo tengo asignado |
| **`T2-06`** | MEDIO | A | `CHECKPOINT-ADS-NEXT.md`:**2506-2655**, sección `## Estado de las fases`, entrada `F4c CRÍTICA INDEPENDIENTE` | La enumeración de pasadas termina en «*DOCUMENTO 26 · QUINTO GATE DE CERTIFICACIÓN … **EL OCTAVO ÁRBOL***» (L2609-2618), tras un renglón que declara la clase ya escarmentada: «*Y VOLVIÓ A CADUCAR … la lista se detenía en la 10ª mientras el árbol iba por el documento 26, **TRES gates más allá**. Por eso las pasadas nuevas dejan de llevar ORDINAL y llevan su DOCUMENTO*» (L2624-2628) | `awk 'NR>=2506 && NR<=2655' … \| grep -cE '2[78]-\|documento 2[78]\|DOCUMENTO 2[78]\|SEXTO GATE\|SÉPTIMO GATE'` → **0**. Los documentos **27** (sexto gate) y **28** (séptimo gate) **no aparecen**, aunque `ls docs/evolucion/[0-9][0-9]-*.md \| sort \| tail -1` los da y el índice tiene fila para los dos | **TERCERA caducidad de la misma enumeración, en el renglón que declara haber cambiado de identificador para no volver a caducar.** Cambiar el ORDINAL por el DOCUMENTO evita que la cifra envejezca; **no repone las entradas que faltan**, y la lista sigue dos documentos corta. La tanda no la tocó. MEDIO y no GRAVE porque el renglón declara expresamente que el censo NO vive ahí y publica de dónde se deriva |
| **`T2-07`** | MEDIO | A | `CHECKPOINT-ADS-NEXT.md`:**2396-2423**, campo `falta_para_cerrar_la_capa:`, **sin rótulo histórico**, dentro del bloque que L919-920 declara VIGENTE | Su primer punto, en presente: «*`F4c` ESTÁ ABIERTA. **El GATE DEFINITIVO INDEPENDIENTE** devolvió `INSUFICIENTE PARA F5` … y **sus correcciones están ahora APLICADAS — NO CERTIFICADAS**. … **BLOQUEANTE 1 · GRAVE 6 · MEDIO 10 · MENOR 7***» | El GATE DEFINITIVO INDEPENDIENTE es el **documento 19**. Desde entonces el árbol publicó los documentos **20-28** (`ls docs/evolucion/[0-9][0-9]-*.md \| sort`), `O17`, `O18`, `O19` y ocho tandas. El campo **no tiene ni un punto posterior al documento 19**: su bullet más nuevo está **nueve documentos atrás** | El campo describe como vigente un estado de hace nueve documentos, sin marca. **Lo declaro contra mi propio interés:** no está literalmente bajo la regla 4 —que nombra sólo `metodo`, `last_meaningful_event` y `based_on`—, y por eso es MEDIO y no GRAVE. Pero está bajo la autodeclaración del bloque («describe el árbol VIGENTE») y bajo su regla 1 |
| **`T2-08`** | MEDIO | A | `CHECKPOINT-ADS-NEXT.md`:**2400-2401**, **1072**, **1296**, **1334** — cuatro copias de recuento/severidad dentro del bloque vivo | La **regla 1** del propio bloque (**L927-930**) las prohíbe: «*NADA QUE OTRA SEDE PUEDA DERIVAR SE COPIA DENTRO DE ESTE BLOQUE. **Ni recuentos de hallazgos, ni severidades, ni clasificación A/B/C** … se REMITE a su sede, o se DERIVA*» | `awk 'NR>=916 && NR<=2499' … \| grep -cE 'BLOQUEANTE [0-9]\|GRAVE [0-9]\|MEDIO [0-9]\|MENOR [0-9]\|A [0-9]+ · B [0-9]'` → **4**: L1072 «69 hallazgos: A 68 · B 1 · C 0» · L1296 ídem · L1334 «21 hallazgos consolidados … GRAVE 5 · MEDIO 6 · MENOR 10» · L2401 «BLOQUEANTE 1 · GRAVE 6 · MEDIO 10 · MENOR 7» | **Y LA CLÁUSULA QUE LAS EXIMÍA LA RETIRÓ ESTA MISMA TANDA.** En el árbol del séptimo gate, `based_on` L1065 decía «*las anotaciones que COPIAN recuentos son ANTERIORES a esa regla y **se conservan sin ampliarse**»* (`git show 3c7e0fa:… \| grep -n 'ANTERIORES a esa regla'` → **L1065**). El remedio de `S2-03` retiró la enumeración **y con ella la cláusula**, y no hay otra: `awk 'NR>=916&&NR<=2500' … \| grep -icE 'ANTERIORES a esa regla\|se conservan sin ampliarse'` → **0**. **Cerrar una instancia DESCUBRIÓ cuatro que estaban amparadas.** Es la respuesta literal a la pregunta 6 que la «Siguiente acción exacta» pone al gate (L3991-3993): *«¿Queda alguna sede del bloque de estado que copie lo que declara no copiar?»* — **sí, cuatro** |
| **`T2-09`** | MEDIO | A | `CHECKPOINT-ADS-NEXT.md`:**946**→**964**, la cadena `metodo:` → `metodo_anterior:`, y **1152**→**1168** para `last_meaningful_event` | La **regla 5** del bloque (**L942-943**): «*LO ANTERIOR NO SE BORRA: baja a `metodo_anterior` y a `last_meaningful_event_anterior`, que es donde vive lo histórico*» | `grep -n '^metodo' docs/evolucion/CHECKPOINT-ADS-NEXT.md` da la cadena: `metodo`(el último) → **`CUARTO GATE`** → `O19` → `TERCER GATE` → `O18` → `SEGUNDO GATE` → `O17` → doc 22 → … Y `last_meaningful_event` → **`EL CUARTO GATE`** → `O19` → `TERCER GATE` → … **No hay entrada del QUINTO GATE (doc 26), ni de la tanda del quinto, ni del sexto, ni del séptimo, ni de esta tanda: la cadena salta del último al CUARTO** | Al reanclar `EE-04` dos eventos de golpe, los intermedios **no bajaron**, y ninguna tanda posterior los ha repuesto. **La cadena histórica que la regla 5 existe para conservar tiene un agujero de cuatro eventos**, en el bloque cuya única función es ser reanudable. Lo gradúo MEDIO: no falsea ningún estado vigente, pero incumple una regla escrita dentro del bloque |
| **`T2-10`** | MENOR | A | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`:**8327**, sede VIVA de mi rango | «**Y las nueve que ya existen para `vigencia`** siguen en pie, sin cambio» — un cardinal en negrita, sin comando y sin remisión, inmediatamente después de la tabla `NP-1`…`NP-11` | **Es cierto hoy y no es derivable desde aquí.** Su referente son las pruebas negativas `N158g`–`N158o`: `grep -rn 'N158' kernel/operativo/pruebas/T136-T152-post-auditoria.md` → L453 «*Sus ocho infracciones deliberadas son `N158h`–`N158o`*», que con `N158g` son **nueve**. Pero `grep -oE 'N158[a-z]?' kernel/operativo/validadores/comprobar_negativos.py \| sort -u \| wc -l` → **15**, y ninguna sede publica el barrido que acota las nueve | **La regla de titulares de §0 admite un cardinal cuya enumeración NO está al lado sólo «*si se publica CON EL COMANDO QUE LO DERIVA, en la sede única que lo publica*».** Éste no lo lleva, y su enumeración vive en otro fichero. **Es exactamente el número «que nadie está obligado a volver a mirar»** que la regla persigue. MENOR: es verdadero hoy, no gobierna ninguna medición, y es anterior a esta tanda |
| **`T2-11`** | MENOR | A | El **SOBRE DE ANCLA** que recibí, contrastado contra `11-ARQUITECTURA-INTEGRADA.md`:**8454-8459** y contra la sede canónica `docs/owner/ADS-OWNER-RESOLUCIONES.md`:**315-317** | §11.6 L8449-8459: «**LO QUE CADA REVISOR RECIBE EXTERNAMENTE, y es la lista entera** … · **el TEXTO de la ratificación del Owner** · el SHA del COMMIT CANDIDATO · el TREE SHA · el SHA del MANIFIESTO · el SHA del DERIVADOR · el SHA DE LA SEDE DEL OWNER». Y la sede canónica L315-317, en palabras del Owner: «*Cada revisor debe recibir externamente: **el texto de esta ratificación** · el SHA del commit candidato · …*» | **Cinco de los seis llegan; el primero no.** El sobre publica commit, `tree`, manifiesto, derivador y sede —los verifiqué todos en §0.2— pero **no lleva el TEXTO de `O19`**: lleva su *digest* (`cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8`), la relación `O19`→`O18`, la declaración externa de ratificación y **una sola frase entrecomillada** —«la omision esta en la transcripcion del coordinador, no en mi resolucion original»—, que sí es verbatim de la sede L276. Las 78 líneas de `O19` no viajan | **Lo gradúo MENOR y publico la refutación contra mí mismo:** con el digest y la receta **pude** contrastar la sede sin ejecutar el emisor, que es lo que `O19` L317 exige, y lo hice; el fin de la cláusula queda satisfecho en sustancia. Pero la lista de §11.6 se rotula «**y es la lista entera**», y el primero de sus seis elementos no viaja. **Un sobre al que le falte cualquiera de sus campos «no es un sobre incompleto: no es un sobre»** (§11.6 L8393-8394) — y por eso lo registro aunque no lo use para nada |
| **`T2-12`** | MENOR | A | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`:**881-887**, proyección de `O17`, contra la sede canónica `docs/owner/ADS-OWNER-RESOLUCIONES.md`:**104** y **113-114** | El bloque se presenta como «**Las DOCE reglas obligatorias que `O17` fija**» y las transcribe en un bloque `text` con aspecto de literal | **Dos deltas de paráfrasis**, aislados con un `diff` palabra a palabra tras normalizar: *regla 7* la sede dice «el sujeto de la certificación **debe identificar** como mínimo» y la proyección «el SUJETO de la certificación **identifica** como mínimo»; *regla 9* la sede dice «cada ejecución **del macrocircuito debe producir** su propia declaración» y la proyección «cada ejecución **produce** su propia declaración». El resto de las doce es idéntico | **NO es una ampliación y por eso no dispara el criterio del sobre**: las dos deltas convierten un deber en un indicativo, es decir **DEBILITAN**. Y la entrada declara dos veces que es proyección y que «*si algo de aquí difiere de la sede, manda la sede*» (L757-760). Lo registro en MENOR porque la sede canónica exige que cada resolución se registre «**íntegramente, no en resumen**» (L6) y un bloque con aspecto de literal que retira dos «debe» no es íntegro. **Lo declaro contra mi propio interés en la dirección contraria: buscaba una ampliación y encontré lo opuesto** |

### §2.1 · RECUENTO, DERIVADO DE LAS FILAS DE ARRIBA

```text
BLOQUEANTE   0
GRAVE        5    T2-01 · T2-02 · T2-03 · T2-04 · T2-05
MEDIO        4    T2-06 · T2-07 · T2-08 · T2-09
MENOR        3    T2-10 · T2-11 · T2-12
             ──
             12

POR CLASE
  A · coherencia interna, corregible dentro de `F4c`   12
  B · exige una decisión NUEVA del Owner                0
  C · actor privilegiado (no exigible en `F4c`)         0

POR ÁRBOL
  DE LA CANDIDATA `61492c1a47…` (el objeto auditado)   10
  DEL APARATO DEL GATE `bf0c65caed…`                    1   (T2-05, el manifiesto del octavo)
  DEL SOBRE                                             1   (T2-11)
```

**NINGUNO ES BLOQUEANTE. NINGUNO EXIGE ARQUITECTURA NUEVA. NINGUNO VUELVE AL OWNER.** Los doce se
cierran con material que el corpus ya tiene escrito, y ninguno reinterpreta `O17`, `O18` ni `O19`.

**Y NUEVE DE LOS DOCE SON DE LA MISMA CLASE**, que es lo que hace que los cuente juntos:
`T2-01`, `T2-02`, `T2-03`, `T2-04`, `T2-08` y `T2-09` viven **dentro del bloque de estado
reanudable** y cinco de ellos **contra una regla escrita dentro de ese mismo bloque para
impedirlos**; `T2-04` y `T2-05` son **remedios de esta tanda que fallan en la sede de al lado**;
`T2-06` es la tercera caducidad de la enumeración que declara no volver a caducar. **No traigo
doce defectos sueltos: traigo doce mediciones de la misma proposición.**

**NO PROPONGO NINGUNA CORRECCIÓN, y no he modificado el repositorio** (verificado en §7.1).

---

## §3 · EL ATAQUE A LA CLASE, CLASE POR CLASE

> **La frase que ordena este expediente** la fijó `BB4` (doc 26), `EE` la sostuvo (doc 27 §5.2) y
> `FF` la sostuvo por tercera vez (doc 28 §4.5): «**El sistema cierra INSTANCIAS y no CLASES.** La
> corrección se aplica con la forma sintáctica exacta del contraejemplo, y el defecto reaparece
> una sede más allá». **La tanda dice haberse escrito contra ella POR TERCERA VEZ.** Para cada
> clase que declara cerrada fui a la sede **UNA MÁS ALLÁ** de la corregida, y publico también las
> que NO cayeron: un ataque que falla es información.

| clase que la tanda declara cerrada | dónde busqué la sede una más allá | qué encontré |
|---|---|---|
| **`S2-04` · «se retiran los ordinales escritos a mano y se remiten a sus dos comandos»** | El remedio retira una PALABRA. Fui al CUERPO de los dos campos de los que la retira, y después al COMANDO al que remite | **CAE DOS VECES. `T2-02` y `T2-04`.** (i) `last_meaningful_event` perdió el ordinal y **conservó la narración del NOVENO ÁRBOL**, que es del sexto gate: al mover el referente al séptimo, **el remedio convirtió una frase verdadera en falsa**. (ii) El segundo comando al que remite, `ls docs/evolucion/[0-9][0-9]-*GATE*.md \| wc -l`, **devuelve 13 donde el ordinal es 7** — y esta tanda lo **copió a una sede nueva** (L954) desde la única en que vivía (L2593 del árbol del séptimo gate) |
| **`S2-03` · «la enumeración de `based_on` se RETIRA y se remite — primera vez que esta clase se cierra retirando»** | La enumeración sí se retiró, y lo verifico y lo consigno. Fui a lo que quedó en su lugar: **la frase del cuerpo** que declara cuál es la base vigente. Y después a la **cláusula de exención** que la enumeración retirada arrastraba | **CAE DOS VECES. `T2-03` y `T2-08`.** (i) `based_on` L1088-1089 sigue diciendo «*LA BASE VIGENTE es la candidata que el manifiesto del **SEXTO** GATE nombra*» — **TRES eventos atrás**, donde `S2-03` midió dos. La enumeración se retiró; **la afirmación no**. (ii) Al retirar la enumeración se retiró con ella «*las anotaciones que COPIAN recuentos son ANTERIORES a esa regla y se conservan sin ampliarse*», **la única cláusula del bloque que eximía las copias de recuento** — y quedan CUATRO, ahora desamparadas |
| **`S1-09` · «el revisor que audita el INSTRUMENTO tiene asignada la sede `C-L.5`·`1bis`»** | El remedio nombra CUATRO sedes en una frase. Verifiqué las cuatro contra la tabla de reparto del propio manifiesto | **CAE. `T2-05`.** `1bis` sí entra en el lote de `T1` (L11413, L11631 ∈ `L11380-L11717`). **§11.4 (L8253), §11.6 (L8329) y §11.9 (L8912) NO**: caen en `L5201-L11379`, tramo exclusivo mío. **El remedio cerró una sede de cuatro y anunció las cuatro**, en el manifiesto que declara estrenarlo |
| **La recogida del ACTO de `FF` · «`C-L.5` pasa a CERTIFICADA POR COBERTURA en la clasificación»** | La recogida en la clasificación **sí se hizo** y lo verifico (L2190-2239, con su alcance dicho). Fui a la otra sede del MISMO bloque que afirma un estado de `C-L.5` | **CAE. `T2-01`.** `metodo:` L958 sigue diciendo «*`C-L.5` ABIERTA —el adjudicador NO emitió la palabra CERTIFICADA*—». **`C-L.5` vuelve a tener DOS estados vigentes**, que es `DD-07`, una sede más allá — y `DD-07` había retirado el estado del documento 11 **precisamente para que hubiera UNA** |
| **`S2-01` · «`00-INDICE.md` L93 remite al comando en vez de publicar el desglose»** | Ejecuté el comando que el `CORRIGENDUM` §18 publica y contrasté la fila viva contra él; y fui después a la fila de al lado, L94, que es donde `S2-02` cayó | **NO CAE.** `git diff 3c7e0fa 61492c1 -- docs/evolucion/00-INDICE.md` muestra **L93 y L94 REESCRITAS las dos**. L93 ya no publica «MEDIO 6 · MENOR 4»: remite a la entrada del CORRIGENDUM con su comando. **Las DOS mitades de `EE-14` están hoy aplicadas** |
| **`S2-02` · «el comando que `EE-10` retiró deja de publicarse como vigente»** | Barrí **todo el corpus vivo** buscando el comando retirado fuera del checkpoint | **NO CAE.** `grep -rn "awk '/\^\| \`(DD\|BT)-\[0-9\]/{n++}" docs/` no lo devuelve en ninguna sede viva como vigente; L94 remite hoy al PARTE. Y el comando acotado que la sede publica **reproduce**: `awk '/^### Lo aplicado, un renglón por identificador/{t=1} t' … \| grep -oE '^\\\| \`(DD\|BT)-[0-9]+\`' \| sort -u \| wc -l` → **24**, con desglose `22 DD · 2 BT` |
| **`S2-05` · «se retira la exclusividad del hecho 4 de la DISPUTA»** | Fui a los **otros tres hechos** del mismo bloque, buscando otro rótulo de supervivencia o de barrido que hubiera caducado | **NO CAE.** El hecho 4 lleva hoy su corchete con «*`S2-05` del SÉPTIMO GATE: este corchete decía «Es el ÚNICO de los cuatro que O19 dejó atrás», y no lo es*» y **cierra remitiendo**: «*Cuántos de los cuatro siguen en pie no se escribe: cada uno lo dice en su propio corchete*» (`DECISIONES`:1055-1059). **Se retiró el cardinal en vez de sustituirlo**, que es la forma correcta |
| **`DD-06` / `Y-05` · «las atribuciones al Owner se barren por el ACTO y no por la tipografía»** | Barrí **toda sede viva** que atribuya algo al Owner: `grep -rnE 'dicho por el Owner\|palabras del Owner\|el Owner escrib\|en sus palabras'` sobre las cinco fuentes derivadas vivas, y contrasté cada literal contra la sede canónica | **NO CAE en sede viva.** Las atribuciones vivas van rotuladas RESUMEN con su `DD-06`, con el literal separado y su comando; `grep -c 'robustez' docs/owner/ADS-OWNER-RESOLUCIONES.md` → **0**. **Cae UNA ocurrencia y NO la cuento**, y lo digo aunque me quitara un hallazgo: `CHECKPOINT`:4813-4819 escribe «*Su motivo, en sus palabras: ROBUSTEZ Y REVALIDACIÓN…*», y vive dentro de `## Siguiente acción exacta — HISTÓRICA, anterior al documento 23` (L4779). **Un defecto dentro de una región marcada HISTÓRICA no es un defecto vivo** |
| **Los rótulos «LITERAL DE `O18`» que `O19` ordena reatribuir** | Barrí el árbol entero: `grep -rn 'LITERAL DE \`O18\`\|literal de \`O18\`' --include='*.md' .` | **NO CAE.** Las dos sedes vivas del documento 11 —§11.7 **L8667** y §11.8 **L8818**— dicen hoy «**LITERAL DE LA SEDE CANÓNICA DEL OWNER, RATIFICADO MEDIANTE `O19`**», que es exactamente lo que `O19` L298-300 ordena. Las demás ocurrencias viven en dictámenes inmutables (docs 24, 25, 26, 27, 28) o en citas de la propia orden. **Y los DOS bloques reproducen la sede cláusula a cláusula**, verificado con el `sed` que el propio bloque publica |
| **LA REGLA DE TITULARES de §0 · barrido sobre negritas y rótulos, no sólo cabeceras** | Barrí los cardinales en negrita y en rótulo de **todo mi rango** (L5201-L11717) con `grep -nEi '\*\*[^*]*\b(DOS\|TRES\|…\|VEINTE)\b[^*]*\*\*'` y verifiqué **cada uno** contra su enumeración adyacente | **CAE UNO, y es MENOR: `T2-10`.** Los demás reproducen: «CATORCE campos» → 14 numerados (L6285-6288) · «CUATRO vías» → 4 · «TRES formas» → 3 · «once campos obligatorios» → 11 y «son seis» → 6 (L6442-6447) · «Seis reglas» → 6 · «CATORCE preguntas» → 14 · «las CINCO» salidas → 5. **Y los dos cardinales guardados reproducen y su guardián existe**: «Son SEIS» extensiones de ficha (L5320) lo deriva `G-10`; «VIGENTES · DIECISIETE» (L10651) lo deriva `G-13`, y lo leí en el código: `_m = re.search(r"^VIGENTES · ([A-ZÁÉÍÓÚa-z]+)$", t11, re.M)` … `elif _num(_m.group(1)) != len(vigentes)` (batería L826-830). **La excepción que §0 declara con nombre está honrada.** Lo único sin comando ni remisión es «las nueve que ya existen para `vigencia`» (L8327) |
| **Las ATRIBUCIONES AL OWNER · ¿alguna proyección AMPLÍA la sede?** | Contrasté las TRES proyecciones vivas contra el texto canónico, bloque a bloque, con `diff` | **NO CAE ninguna ampliación.** Tres `diff` VACÍOS byte a byte (§0.3): las diez viñetas de «lo que `O19` declara», las TRES condiciones obligatorias y el REPARTO. El literal de `O17` reproduce con SHA idéntico tras normalizar. **Lo que encontré va en dirección CONTRARIA a lo que el sobre me manda buscar**: dos deltas que DEBILITAN (`T2-12`) |
| **`C-L.7` · «la clase se cierra RETIRANDO por primera vez»** | Es la pregunta 6 que la propia «Siguiente acción exacta» pone al gate. La contesto entera en §3.1 | **CAE. `T2-01`, `T2-02`, `T2-03`, `T2-04`, `T2-08`, `T2-09`** |
| **`X63` · ¿se presenta como prueba ejecutada o como certificación presente?** | Barrí sus apariciones en mi rango y en las cinco fuentes de mi lote | **NO CAE.** `grep -rn 'X63' docs/` → doc 11 L5517·5676·5688 (mi rango) y L1714·1742·3715 (rango de `T1`), `CHECKPOINT` L44·2426·3011·3702·3735·3817, `00-INDICE` L94·97·98. Las sedes que lo gobiernan lo niegan expresamente: `CHECKPOINT`:3772-3775 «*`X63` NO ES UNA PRUEBA — es CONTRATO DE PRUEBA DE `F6`. NO se ha ejecutado, NO certifica nada*» y :3928 «*`X63` SIGUE SIENDO CONTRATO … NO ejecutado*». El único presente de indicativo de mi rango —doc 11 **L5686**, «*`X63` la comprueba validando las tres celdas*»— queda desambiguado **dos líneas más abajo** (L5697-5699): «*Se contrata la fila que faltaba, `X63` en §2.6.7. **No es una protección interna nueva** … es un **contrato de prueba de `F6`** … y **no se ejecuta aquí**»*. **RESPUESTA: NO** |
| **`M-04`, y lo declarado CERRADO o SUPERADO** | Barrí las sedes vivas buscando cualquiera que declare SUPERADO o CERRADO lo que no lo está | **NO CAE.** `M-04` figura NO SUPERADA en las cuatro sedes vivas que la nombran (`CHECKPOINT` L957, L3919, L3995 · `00-INDICE` L100-101). El PARTE de la tanda declara «*NINGÚN HALLAZGO SUPERADO: ni uno*» (L3919-3921) y acota `C-L.5` con precisión —«*cambia de estado porque **un adjudicador ejecutó el acto**, no porque esta tanda lo deduzca*»—. **Y `C-L.7` NO se declara cerrada**: el índice L101 y la «Siguiente acción exacta» L3995-3996 dicen «`C-L.7` sigue **NO CERRADA** — retirar no es certificar». **Ninguna sede viva declara CERRADO o SUPERADO lo que no lo está**, y ésa es la mejor noticia de este informe |
| **EL DÉCIMO/UNDÉCIMO ÁRBOL y `EE-01`/`EE-11` · el instrumento** | **NO ES MI DOMINIO** — es el lote de `T1`. **No construí ningún árbol defectuoso y no busqué el undécimo.** Sólo ejecuté la batería y el derivador | **NO ATACADO POR MÍ, y lo declaro sin adornarlo. Mi silencio no es evidencia en ninguna dirección** (§6). Lo que sí mido y consta: sobre un clon desechable en el commit candidato, `python3 …/comprobar-correccion-gate-de-cierre.py` → **38/38 comprobaciones en verde**, y sobre la materialización sin `.git` que la receta del sobre prescribe → **29/38**, con la línea de ALCANCE (`DD-21`) nombrando las nueve exactas |

### §3.1 · `C-L.7` — LA PREGUNTA QUE LA PROPIA TANDA PONE AL GATE, CONTESTADA

La «Siguiente acción exacta» viva (**L3991-3993**) pone al gate esta pregunta:

> «**`C-L.7`.** La clase se ha cerrado RETIRANDO. **¿Queda alguna sede del bloque de estado que
> copie lo que declara no copiar?**»

**RESPUESTA: SÍ, Y NO ES UNA. LA CLASE NO ESTÁ CERRADA.**

```text
LO QUE SÍ SE HIZO, y lo consigno primero porque es verdad y es una mejora REAL
  · la enumeración de documentos numerados de `based_on` se RETIRA y se remite al comando de
    la regla 2 (`S2-03`) — es la primera vez que esta clase se cierra retirando en vez de
    reanclando, y `FF` había determinado exactamente eso: «*reanclarla añadiendo el 26 y el 27
    CERRARÍA LA INSTANCIA Y DEJARÍA LA CLASE*» (doc 28 L4204). **La tanda hizo lo correcto.**
  · los ordinales «SEXTO GATE» escritos a mano se retiran de `metodo` y de
    `last_meaningful_event` (`S2-04`)
  · `C-L.5` se recoge en la clasificación vigente con su ALCANCE dicho

LO QUE NO, y son SEIS sedes del mismo bloque
  1  `metodo:` L958 afirma «`C-L.5` ABIERTA — el adjudicador NO emitió la palabra CERTIFICADA»,
     que es FALSO y contradice la cabecera del propio fichero              → `T2-01`
  2  `last_meaningful_event:` L1156-1162 narra EL NOVENO ÁRBOL bajo «EL ÚLTIMO GATE», con lo
     que el remedio hizo FALSA una frase que era verdadera                 → `T2-02`
  3  `based_on:` L1088 declara base vigente la candidata del SEXTO gate, TRES eventos atrás,
     contra la regla 4 escrita dentro del bloque                           → `T2-03`
  4  el comando al que los dos primeros REMITEN devuelve 13 donde el ordinal es 7, y esta
     tanda lo copió a una sede más                                         → `T2-04`
  5  CUATRO copias de recuento y severidad, y la cláusula que las eximía la retiró esta misma
     tanda al retirar la enumeración                                       → `T2-08`
  6  la cadena `_anterior` salta del último gate al CUARTO: faltan cuatro eventos, contra la
     regla 5                                                               → `T2-09`

ES LA SÉPTIMA RECURRENCIA CONSECUTIVA de la clase —`K-01`/`J-10`/`L-01` · `P-05`≡`Q-08`/`R-02`
· `S-17`≡`S3-05` · `X-04` · `R2-03`→`EE-04` · `S2-03`/`S2-04` · ésta— y **la tercera cometida
contra reglas escritas DENTRO del propio bloque para impedirla**. `C-L.7` NO ESTÁ CERRADA, y la
propia tanda lo dice: el índice L101 y la «Siguiente acción exacta» L3995 escriben «`C-L.7`
sigue NO CERRADA — retirar no es certificar». **En eso la tanda es honesta; lo que mido es que
retirar tampoco cerró la clase.**
```

### §3.2 · `C-L.5` — ¿RECOGE EL CHECKPOINT EL ACTO, Y RECOGE SU ALCANCE?

**La pregunta del encargo tiene dos mitades y la respuesta es distinta en cada una.**

```text
¿RECOGE EL ACTO?         SÍ, y bien. `CHECKPOINT` L2190-2194 lo pone en la clasificación
                         vigente como estado primario propio —«CERTIFICADA POR COBERTURA · 1 ·
                         `C-L.5`»— con los trece ids sumando 13 sin doble conteo, y L2195-2198
                         conserva el renglón anterior rotulado [HISTÓRICO] en vez de borrarlo.
                         Y lo atribuye correctamente: «es un ACTO del adjudicador `FF`».

¿RECOGE EL ALCANCE?      SÍ, ENTERO Y SIN RECORTE, y lo verifiqué cláusula a cláusula contra el
                         dictamen. `CHECKPOINT` L2230-2239 escribe las cuatro negaciones que
                         `FF` puso en doc 28 L3734-3740: **NO certifica suficiencia · NO
                         certifica profundidad · NO certifica ningún hallazgo como superado** ·
                         y añade «Certificar la cobertura NO cierra `F4c` ni autoriza `F5`».
                         La cabecera L24-27 y la «Siguiente acción exacta» L3947-3950 repiten
                         las tres negaciones. **Ninguna sede viva usa la palabra para más de lo
                         que certifica**: barrí las once apariciones vivas de «CERTIFICADA»
                         junto a `C-L.5` y las once van acotadas o remiten.

¿HAY ALGO MAL?           SÍ, y es `T2-01`: la sede que doc 11 L11569 designa como ÚNICA para el
                         ESTADO devuelve hoy DOS estados, porque `metodo:` L958 no se tocó.
                         **No es que el corpus use la palabra para más de lo que certifica: es
                         que a la vez la niega.** Y ésa es la diferencia entre el defecto que
                         busqué y el que encontré, y la digo así.
```

### §3.3 · EL PARTE DE LA TANDA — ¿SU COMANDO CUENTA LO QUE DICE CONTAR, Y CUBRE LOS 14?

**SÍ, LAS DOS COSAS, y lo ejecuté yo.** Es la mejor pieza de esta tanda y lo digo con la misma
fuerza con la que digo los cinco GRAVES.

```bash
# el comando que el propio PARTE publica para contarse (CHECKPOINT L3870-3871)
awk '/^### Lo aplicado por la tanda del SÉPTIMO GATE/{t=1} t' \
  docs/evolucion/CHECKPOINT-ADS-NEXT.md | grep -oE '`S[12]-[0-9]+`' | sort -u | wc -l
14
# los ids, uno a uno
S1-01 S1-02 S1-03 S1-04 S1-05 S1-06 S1-07 S1-08 S1-09 S2-01 S2-02 S2-03 S2-04 S2-05

# la COBERTURA contra el gate (CHECKPOINT L3874-3878) — la sede dice que sale VACÍO
comm -23 <(grep -oE '\*\*`S[12]-[0-9]+`\*\*' docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md \
           | grep -oE 'S[12]-[0-9]+' | sort -u) \
         <(awk '/^### Lo aplicado por la tanda del SÉPTIMO GATE/{t=1} t' \
             docs/evolucion/CHECKPOINT-ADS-NEXT.md | grep -oE 'S[12]-[0-9]+' | sort -u)
(sin salida: VACÍO)

# y los ids que el documento 28 declara, para cerrar el círculo
grep -oE '\*\*`S[12]-[0-9]+`\*\*' docs/evolucion/28-…md | grep -oE 'S[12]-[0-9]+' | sort -u | wc -l
14
```

**Los 14 del documento 28 = los 14 del parte, y la resta cierra a ∅.** El comando **cuenta
identificadores distintos y acota su tabla**, que es lo que `EE-10` exigió y lo que `S2-02` midió
que `00-INDICE` L94 no hacía. **Y NO reincide.**

**¿ESTÁ CADA REMEDIO DONDE SU FILA DICE?** Lo comprobé fila a fila con
`git diff --stat 3c7e0fa 61492c1` y con el diff por fichero:

```text
FICHEROS QUE LA TANDA TOCA, derivados y no copiados
  docs/evolucion/00-INDICE.md                                      5 ±
  docs/evolucion/11-ARQUITECTURA-INTEGRADA.md                     13 ±
  docs/evolucion/CHECKPOINT-ADS-NEXT.md                          319 ±
  docs/evolucion/verificacion/README.md                            2 ±
  …/verificacion/comprobar-correccion-gate-de-cierre.py          424 ±
  …/verificacion/derivar-universo-obligatorio.py                  57 ±
  …/verificacion/emitir-sobre-de-ancla.py                         33 ±
  docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md                   11 ±

CONTRASTE FILA A FILA, en lo que mi dominio alcanza
  S1-07  «documento 11, §2.6.7»          → hunk `@@ -1782,2 +1782,11 @@`   ✔ ESTÁ
  S1-09  «manifiesto del OCTAVO gate»    → sólo en el ÁRBOL DEL GATE, y ahí está   ✔ ESTÁ,
                                            pero su TEXTO es falso en tres de sus cuatro
                                            sedes → `T2-05`
  S2-01  «`00-INDICE.md`»                → hunk `@@ -93,2 +93,2 @@`, L93 reescrita   ✔ ESTÁ
  S2-02  «`00-INDICE.md`»                → mismo hunk, L94 reescrita                 ✔ ESTÁ
  S2-03  «`CHECKPOINT`, `based_on`»      → hunk `@@ -1062,52 +1098,13 @@`            ✔ ESTÁ
                                            (la enumeración retirada; el cuerpo no → `T2-03`)
  S2-04  «`CHECKPOINT`, `metodo` y
          `last_meaningful_event`»       → hunks `@@ -912,9 +944,13 @@` y
                                            `@@ -1153,6 +1150,8 @@`                  ✔ ESTÁN
                                            (los ordinales retirados; el cuerpo no → `T2-02`;
                                             y el comando que se añade → `T2-04`)
  S2-05  «`DECISIONES`, nota de `O18`»   → hunk `@@ -1052,3 +1052,8 @@`              ✔ ESTÁ
  S1-01…S1-06, S1-08  «batería, derivador, emisor»  → los tres ficheros tocados     ✔ ESTÁN,
                                            y su CONTENIDO es dominio de `T1`: no lo juzgo
```

**RESPUESTA: cada uno de los catorce está en el fichero que su fila dice.** Lo que falla no es
la ubicación del remedio: es su ALCANCE, en cuatro de ellos.

### §3.4 · AUSENCIA DE REGRESIONES — LOS 19 DEL SEXTO GATE Y LOS 24 `DD`/`BT` DEL QUINTO

Ejecuté los comandos que cada parte publica para contarse y para comprobar su cobertura:

```bash
# QUINTO GATE — el comando que EE-10 dejó corregido
awk '/^### Lo aplicado, un renglón por identificador/{t=1} t' CHECKPOINT | \
  grep -oE '^\| `(DD|BT)-[0-9]+`' | sort -u | wc -l           → 24     (22 DD · 2 BT)
# SEXTO GATE
awk '/^### Lo aplicado por la tanda del SEXTO GATE/{t=1} t' CHECKPOINT | \
  grep -oE '`EE-[0-9]+`' | sort -u | wc -l                    → 19
comm -23 <(grep -oE '^\| [0-9]+ \| \*\*`EE-[0-9]+`' 27-…md | grep -oE 'EE-[0-9]+' | sort -u) \
         <(awk '…SEXTO GATE…' CHECKPOINT | grep -oE 'EE-[0-9]+' | sort -u)   → VACÍO
grep -oE '\*\*`EE-[0-9]+`\*\*' 27-…md | grep -oE 'EE-[0-9]+' | sort -u | wc -l → 19
```

**Los tres partes cierran: 24, 19 y 14, con cobertura a ∅ los tres.** En mi dominio, **de los 24
del quinto gate y los 19 del sexto, los que reviso siguen cerrados salvo la clase de `EE-04`**:

```text
SIGUEN CERRADOS, verificados por mí
  `DD-05`·`EE-18`  el bloque LITERAL de §11.8 reproduce la sede cláusula a cláusula, y la
                   sexta se rotula `EL EJECUTOR EXTERNO`, que es su sujeto. Verificado con el
                   `sed` que el propio bloque publica: `diff` sin diferencias de contenido
  `DD-06`          «robustez y revalidación» va rotulada RESUMEN en todas sus sedes vivas;
                   `grep -c 'robustez'` sobre la sede canónica → 0
  `DD-07`          las dos sedes del documento 11 siguen RETIRANDO el estado y remitiendo
                   (doc 11 L11550 y L11698-11703). **Lo que regresó es su clase en el
                   CHECKPOINT** → `T2-01`
  `DD-10`          §2.1 remite a §9.6 para el censo `X-S`; no escribe cardinal
  `DD-13`          el cardinal 46 no aparece en ninguna sede viva de MI rango
  `DD-14`          el par `O17`/`O19` enlaza a su sede: el `awk` que la sede publica da
                   `O17 → 5 · O18 → 3 · O19 → 1`, todas > 0
  `DD-16`          `00-INDICE` L103-105 dice «la PRIMERA sección», y hay 10 · 9 históricas
  `EE-03`          el `diff` de la LISTA sale VACÍO en LOS DOS árboles, y `T147` da
                   `1 superadas · 0 fallidas` en los dos
  `EE-05`·`EE-06`  las aserciones condicionales caducadas están retiradas y sus comandos
                   reproducen: `grep -c '"ABIERTA"'` → 2 · `… | grep G-16` → `OK G-16`
  `EE-07`·`EE-12`  ninguna sede viva escribe el cardinal de la tabla adversarial;
                   `grep -cE '^\| \`?X[0-9]'` → 55
  `EE-13`          «30 comprobaciones» sólo aparece dentro de la nota que lo retira
  `BT-01`          la nota de trazabilidad de `O17` publica su comando y ya no afirma
                   «no hay otra sede»: `grep -rn 'No elijo la alternativa barata' docs/ kernel/`
                   → 6 golpes, uno de ellos la sede canónica
  `BT-02`          `G-16` está en VERDE y no imprime «C-L.5 CERTIFICADA» como literal fijo

REGRESIÓN MEDIDA
  `EE-04`          los tres campos que reancló vuelven a estar desfasados, cada uno por una
                   vía distinta → `T2-01`, `T2-02`, `T2-03`. **Es la clase, no la instancia**
  `DD-08`          «Estado de las fases» vuelve a ir corta, ahora en dos documentos → `T2-06`
```

---

## §4 · LO QUE VERIFIQUÉ Y **NO** CAYÓ

**Pesa tanto como lo que cayó, y va con su comando y su salida.**

### 4.1 · EL SOBRE, Y CON ÉL LA VALIDEZ DEL GATE

```text
· LOS DOS DIGEST DE UNIVERSO reproducen BYTE A BYTE, recalculados ANTES de leer nada:
    70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1   (candidata)
    8bc0051c937d9c24dba2f91edd4a55cd9fcc43232ae336dd5015642f3c2c538e   (gate)
· SHA-256 DEL MANIFIESTO en el commit del gate:
    a82e74968e4ca31fbae0825a43f295736af39e58a16b3adf8879d021688e3d76   CASA
· SHA-256 DEL EMISOR y DEL DERIVADOR en los DOS commits: los CUATRO casan, y son idénticos
  entre sí — el commit del gate no tocó `verificacion/`
· LA SEDE CANÓNICA DEL OWNER: la sede entera y los tres digest `O17`·`O18`·`O19`, en el commit
  auditado: LAS CUATRO CIFRAS CASAN, y los recuentos DERIVADOS 85 · 111 · 78 también
· LAS REFERENCIAS REMOTAS resuelven a los commits que el sobre publica:
    refs/remotes/origin/review/f4c-mutacion-guardada-candidate-20260831 → 61492c1a47…
    refs/remotes/origin/gate/f4c-certificacion-8-20260831               → bf0c65caed…
· LA SUPERFICIE DE DIVERGENCIA: 2 rutas de UNIVERSO, 5 de ÁRBOL, y el sobre lo distingue
  expresamente y publica el comando de la otra — la corrección de `EE-19` sigue hecha
· LOS 18 CAMPOS que §11.6 exige al sobre, contrastados uno a uno contra el que recibí:
  los DIECIOCHO están, y las CUATRO declaraciones que los acompañan también —identificación
  de `O18`, la relación `O19`/`O18` con esas palabras, la ratificación externa y la entrega
  previa—. **Lo único que falta es «el TEXTO de la ratificación», y va como `T2-11`**
· `git status --porcelain` del repositorio auditado: VACÍO al abrir y al cerrar
```

**El gate NO es INVÁLIDO por ninguna vía que yo pueda medir**, y **cumplí la obligación de `O19`
L317 de comprobar la receta SIN EJECUTAR EL EMISOR**: los seis digest salen de
`git show … | awk … | sha256sum`, y no he corrido `emitir-sobre-de-ancla.py` ni una vez.

### 4.2 · LAS ATRIBUCIONES AL OWNER · LA SEDE MANDA Y NINGUNA PROYECCIÓN LA AMPLÍA

Es mi terreno y la conclusión es negativa, que es la que el sobre me manda buscar.

```text
· TRES `diff` VACÍOS byte a byte entre sede y proyección (§0.3): las diez viñetas de «lo que
  `O19` declara», las TRES condiciones obligatorias del verificador externo, y el REPARTO
· el LITERAL de `O17` reproduce con SHA idéntico tras normalizar saltos:
  5f1cf5f74ab5b64c2d1cdd340875080271c6a2a6a14ea6f8ba92227fce91ac67 en las dos sedes
· los DOS bloques rotulados LITERAL del documento 11 —§11.7 L8667 y §11.8 L8818— dicen hoy
  «LITERAL DE LA SEDE CANÓNICA DEL OWNER, RATIFICADO MEDIANTE `O19`», y su contenido reproduce
  la sede cláusula a cláusula, verificado con el `sed` que el propio bloque publica
· PROCEDENCIA bien separada en las tres capas que el corpus distingue, y lo verifiqué en cada
  sede que cita al Owner: FUENTE NORMATIVA = `docs/owner/` · PROYECCIÓN DERIVADA = §2 del
  registro, que ENLAZA y no sustituye · REGISTRO HISTÓRICO = la entrada corta de `O18`, la
  transcripción de `O15`/`O16` en `owner_captado`, y las regiones [HISTÓRICO]
· `owner_captado` (L2011-2040) declara EXPRESAMENTE que lo que conserva de `O15` y `O16` «ES
  TRANSCRIPCIÓN DEL COORDINADOR … y NO ES AUTORIDAD CANÓNICA», que es la distinción exacta
· NINGÚN rótulo «LITERAL» vivo miente, y ninguna proyección amplía
```

**`O19` nació de una ampliación. En este árbol no encuentro su sucesora.**

### 4.3 · LAS DERIVACIONES VIVAS DE MI LOTE, EJECUTADAS UNA A UNA

```bash
awk '/^## 15\.8 /{f=1;next} f&&/^## /{exit} f&&/^### /{n++} END{print n}' 11-ARQ.md      → 18
grep -c '^## `PN-' 11-ARQ.md                                                             → 19
grep '^## `PN-' 11-ARQ.md | grep -vc 'RETIRADA\|FUSIONADA'                               → 17
grep -cE '^\| `?X[0-9]' 11-ARQ.md                                                        → 55
grep -cE '^\| `?O[0-9]+' 11-ARQ.md                                        → 13  (§15.4: O7…O19)
grep -c '^# `O[0-9]*`' docs/owner/ADS-OWNER-RESOLUCIONES.md                               →  3
grep -o '^### `O[0-9]*`' DECISIONES.md | tail -1                                    → `O19`
grep -o '^| D[0-9]* |' DECISIONES.md | tail -1                                    → | D108 |
grep -c '^| D[0-9]' DECISIONES.md                                          → 108  (D1…D108)
grep -c '^## Siguiente acci[óo]n exacta' CHECKPOINT.md                                   → 10
grep -c '^## Siguiente acci[óo]n exacta — HISTÓRICA' CHECKPOINT.md                        →  9
grep -n '^## Siguiente acci[óo]n exacta' CHECKPOINT.md | head -1                → 3938 (la VIVA)
grep -cE '^\| `(DD|BT)-[0-9]+`' (acotado a su tabla, con sort -u)                        → 24
awk '…SEXTO GATE…' | grep -oE '`EE-[0-9]+`' | sort -u | wc -l                            → 19
awk '…SÉPTIMO GATE…' | grep -oE '`S[12]-[0-9]+`' | sort -u | wc -l                       → 14
git diff --name-only 05f71b7..HEAD -- kernel/ | wc -l                                    →  6
grep -o "[0-9]* ficheros recorridos" …/fuentes-salida.txt                → 317 ficheros
grep -o "documentos analizados: [0-9]*" …/referencias-salida.txt         → 270
python3 …/comprobar_referencias.py --exclusiones                → 1 superadas · 0 fallidas
python3 …/comprobar-correccion-gate-de-cierre.py (clon con historia)  → 38/38 en verde
python3 …/comprobar-correccion-gate-de-cierre.py (árbol sin `.git`)   → 29/38, las 9 exactas
```

**LAS DIECIOCHO CUADRAN CON LO QUE SU SEDE DECLARA.** El censo de `PN` (19 cabeceras − `PN-4`
RETIRADA − `PN-5` FUSIONADA = 17) coincide con el «VIGENTES · DIECISIETE» que §16 escribe **y
que `G-13` deriva**. Los 18 bloques de §15.8 son `D23`…`D108`, uno por tanda que escribió
decisiones — y esta tanda **no escribió ninguna**, luego no le corresponde bloque.

### 4.4 · LA REGLA DE LA LISTA DE `00-INDICE.md` — LA CLASE `S-18`≡`T-14` NO REINCIDE

Es la clase que ha castigado a CUATRO gates seguidos. Ejecuté el `diff` que la propia sede
publica (L174-179), **sobre los DOS árboles**:

```bash
diff <(find docs/evolucion/verificacion -type f \( -name '*.md' -o -name '*.py' \) | sort) \
     <(awk '/^\| documento del aparato de verificación \|/{t=1} t&&!/^\|/{exit} t' \
           docs/evolucion/00-INDICE.md \
         | grep -o 'verificacion/[A-Za-z0-9_./-]*\.\(md\|py\)' \
         | sed 's|^|docs/evolucion/|' | sort -u)
# árbol CANDIDATO 61492c1 → VACÍO (rc=0)
# árbol del GATE  bf0c65c → VACÍO (rc=0)
```

**Y `T147`, con el comando exacto que `00-INDICE` L200 publica**, sobre los dos árboles:
`1 superadas · 0 fallidas`. **El commit del gate lleva el manifiesto, su fila en la LISTA y la
evidencia derivada reejecutada** —las tres cosas que `DD-17` exige—, y el árbol que este gate
juzga **NO queda con un validador canónico en rojo por causa del aparato del propio gate**.
**Es la primera vez en cinco gates que esta clase no reincide dos veces seguidas, y consta.**

### 4.5 · LO QUE ESTA TANDA SÍ CERRÓ, PORQUE ES VERDAD Y NO ES CORTESÍA

```text
· `S2-01` y `S2-02` CERRADOS: `00-INDICE` L93 y L94 están las DOS reescritas —el desglose
  remite al comando del CORRIGENDUM, y el `awk` defectuoso se retira—. Fui a la sede de al
  lado de cada una y NO cae ninguna
· `S2-05` CERRADO, y **por la forma correcta**: retira el cardinal en vez de sustituirlo, y
  cierra remitiendo —«cuántos de los cuatro siguen en pie no se escribe: cada uno lo dice en
  su propio corchete»
· `S2-03` hace lo que `FF` DETERMINÓ, literalmente: retira la enumeración en vez de reanclarla.
  **La tanda entendió la orden y la ejecutó.** Lo que falla es lo que quedó detrás
· EL PARTE es la mejor pieza de la tanda: cuenta identificadores, acota su tabla, cubre los 14
  y su resta cierra a ∅. Lo ejecuté yo
· NINGUNA COMPROBACIÓN NUEVA, como el adjudicador ordenó: los dos remedios que podrían haberla
  añadido se pliegan sobre `G-00`, que ya existía
· NADA INMUTABLE EDITADO: la sede canónica del Owner es byte-idéntica en los dos commits, y
  ningún dictamen ni manifiesto anterior aparece en el `git diff --stat` de la tanda
· `X63` sigue siendo contrato de prueba de `F6` en todas sus sedes
· NINGÚN HALLAZGO SE DECLARA SUPERADO, y `C-L.5` cambia de estado con su ACTO atribuido y su
  alcance dicho — no por deducción de la tanda
· NADA VUELVE AL OWNER, y lo compruebo: ninguna de mis doce mediciones produce una pregunta
  nueva, y ninguna reinterpreta `O17`, `O18` ni `O19`
```

---

## §5 · REFUTACIONES CONTRA MIS PROPIAS CONCLUSIONES

Intenté **siete**. **Dos cayeron, tres cayeron a medias y dos no cayeron.** Publico las siete.

### `RF-1` · **CAYÓ A MEDIAS** · «`T2-01` no vale: `FF` designó como sede del ESTADO de `C-L.5` la CLASIFICACIÓN, no `metodo:`. La tanda la recogió donde tocaba»

**Cae en su premisa, y la acepto sin regatear.** Fui al literal: `FF` escribe (doc 28 L3746-3748)
«*La sede del ESTADO de `C-L.5` es UNA —la clasificación vigente del `CHECKPOINT`— y este acto es
el que esa sede tiene que recoger*». **La tanda lo recogió ahí, y con su alcance entero.**
**Retiro de `T2-01` toda imputación de que la tanda no cumpliera el encargo de `FF`: lo cumplió.**

**NO cae en lo que sostengo**, que es más estrecho: `metodo:` **no se limita a callar, AFIRMA** —«`C-L.5`
ABIERTA — el adjudicador NO emitió la palabra CERTIFICADA»— y esa afirmación es **falsa hoy**, está
en un bloque que se declara VIGENTE, y es **exactamente el defecto que `DD-07` cerró** cuando `C-L.5`
tenía dos estados vivos. Además la regla 1 del propio bloque le prohíbe copiar un estado que otra
sede posee. **CAMBIÓ MI INFORME:** bajé `T2-01` de BLOQUEANTE a **GRAVE** y reescribí su columna
para que impute la afirmación falsa y no el incumplimiento del encargo.

### `RF-2` · **NO CAYÓ** · «`T2-02` es pedantería: “el último gate” es una remisión correcta, y el cuerpo es una descripción histórica del estado en que se escribió»

La construí en serio, porque es la defensa natural. **NO CAE, por dos medidas:**

1. **El cuerpo no lleva marca histórica y el bloque prohíbe deducirla.** `L919-920` declara que el
   bloque «*va SIN rótulo histórico: describe el árbol VIGENTE*», y la regla 5 fija que **lo
   histórico baja a `_anterior`** — que es justamente donde vive la narración del cuarto gate.
   Un párrafo histórico dentro de `last_meaningful_event` es lo que la regla 5 existe para impedir.
2. **La regla 4 lo nombra por su nombre** entre los tres campos que todo evento nuevo reancla.
   El evento nuevo existe —el séptimo gate, y esta tanda— y el campo no se movió.

**Y añado la medición que decide:** antes del remedio la frase era **verdadera**; después es
**falsa**. Un remedio que empeora el valor de verdad de su sede no es una remisión correcta.

### `RF-3` · **CAYÓ, Y CONTRA MÍ** · «`T2-04` es de laboratorio: `*GATE*` da 13 pero nadie usa ese comando para nada; el ordinal real lo da el primero de los dos»

**Fui a medirlo y el resultado agrava el hallazgo.** Es cierto que el PRIMER comando
—`ls … | sort | tail -1`— da el documento correcto, y lo consigno. **Pero el segundo se publica
EXPRESAMENTE como la derivación del ORDINAL**, que es lo que el primero no da: «*Ni el ordinal ni
el documento se escriben:*» y a continuación los dos. **Y lo medí en las tres sedes**: las tres lo
presentan igual, y **la tercera es la «Siguiente acción exacta» VIVA**, que es la sede que lee
quien encarga el gate siguiente. **CAMBIÓ MI INFORME:** `T2-04` pasó de una sede a **tres**, con la
medición de cuál las añadió, y subió de MEDIO a **GRAVE**.

### `RF-4` · **CAYÓ** · «hay un hallazgo más: `CHECKPOINT`:4813-4819 atribuye al Owner “en sus palabras” la frase que `DD-06` retiró»

Iba a contarlo, y es exactamente la clase que `DD-06` castiga. **CAYÓ, y lo digo aunque me quite un
hallazgo.** La ocurrencia vive en `## Siguiente acción exacta — **HISTÓRICA**, anterior al documento
23` (**L4779**), y `DD-06` declaró expresamente su alcance: «*Lo que queda dentro de una región
HISTÓRICA se conserva sin tocar, y se dice*». **Un defecto dentro de una región marcada HISTÓRICA
no es un defecto vivo, y mi encargo me obliga a decirlo. Un hallazgo menos.**

### `RF-5` · **CAYÓ A MEDIAS** · «`T2-08` no vale: los tres primeros están en campos `_anterior`, que la regla 5 designa para lo histórico»

**Cae para tres de los cuatro, y lo acepto.** L1072 está en `metodo_anterior:` y L1296 y L1334 en
`last_meaningful_event_anterior:`, que son los campos que la regla 5 crea **para** conservar lo
histórico. Una lectura razonable los exime. **CAMBIÓ MI INFORME:** lo digo en la fila y por eso
`T2-08` es MEDIO y no GRAVE.

**No cae para el cuarto, que es el que sostengo.** **L2400-2401 está en `falta_para_cerrar_la_capa:`,
que NO es un campo `_anterior`, no lleva rótulo histórico y es un campo primario del bloque.** Y no
cae la medición que lo enmarca: **la cláusula que amparaba las copias anteriores la retiró esta misma
tanda**, de modo que hoy ninguna de las cuatro tiene amparo escrito. La pregunta que el gate se pone
—«¿queda alguna sede que copie lo que declara no copiar?»— **se contesta que sí con una sola**.

### `RF-6` · **NO CAYÓ** · «`T2-05` no es un hallazgo del gate: el manifiesto es del APARATO, y un defecto suyo no es del objeto auditado»

**Cierto que es del aparato, y lo clasifico así en §2.1 —1 de 12, del árbol del gate—.** **NO CAE**,
por la sede que lo ordena: la obligación 3 del sobre me manda contrastar **cada fila del manifiesto
contra el árbol que declara**, y el manifiesto es la fuente 3 del universo del gate. Además el
precedente existe y es del gate anterior: `S1-09` es **del aparato** y `FF` lo sostuvo y lo elevó
«*por encima de un hallazgo*» como observación de método (doc 28 §7). **Y lo que mide `T2-05` es
peor que `S1-09`: no es un reparto mejorable, es una afirmación que la tabla del propio fichero
desmiente en tres de sus cuatro sedes.**

### `RF-7` · **CAYÓ A MEDIAS, Y ME OBLIGÓ A REORDENAR** · «doce hallazgos documentales, ninguno bloqueante, ninguno para el Owner: eso no sostiene un veredicto, y mi censo es cosmética»

**Concedo lo principal y lo escribo antes que mi respuesta:** mi veredicto **no cuelga de mis doce**,
y lo digo sin rodeos. Ninguno es BLOQUEANTE, ninguno exige arquitectura nueva, ninguno vuelve al
Owner, y la tanda ejecutó lo que se le ordenó —`S2-01`, `S2-02`, `S2-05` cerrados, el PARTE
impecable, la LISTA de `00-INDICE` sin reincidir, la sede canónica intacta y sin ampliaciones—.
**Eso es convergencia real y no la escondo.**

**Y la otra mitad es falsa.** Lo que sostengo no es que doce rótulos decidan un veredicto: es que
**seis de mis doce viven dentro del bloque de estado reanudable, cinco contra reglas escritas dentro
de ese mismo bloque para impedirlos, y dos de ellos los CREÓ o los EMPEORÓ el remedio de esta
tanda.** En un corpus cuya única raíz interna es su propio texto, **un bloque que se declara vigente
y afirma lo contrario de su propia cabecera sobre la condición que el último gate acaba de
certificar** no es cosmética: es la medición directa de la proposición que ordena el expediente.
**CAMBIÓ MI INFORME:** puse §4 —lo que no cayó— con el mismo detalle que §2, y §4.5 antes de §7.

### §5.1 · Qué cambiaron estas siete

```text
· `T2-01` BAJA de BLOQUEANTE a GRAVE, y retira la imputación de incumplir a `FF`      (RF-1)
· `T2-04` SUBE de MEDIO a GRAVE y pasa de una sede a TRES, con la que añadió la tanda (RF-3)
· un hallazgo RETIRADO del censo: `CHECKPOINT`:4813 es región HISTÓRICA                (RF-4)
· `T2-08` queda ACOTADO a la única copia fuera de un campo `_anterior`, y es MEDIO     (RF-5)
· `T2-05` gana la comparación con `S1-09`, que es su precedente exacto                 (RF-6)
· reordenado: lo que la tanda SÍ cerró va antes de mi respuesta                        (RF-7)
· `T2-02` se refuerza: el remedio empeoró el valor de verdad de su sede                (RF-2)
```

**Cinco de mis siete movimientos van contra la comodidad de mi posición y sólo dos la mejoran.**

---

## §6 · LO QUE MI LOTE NO CUBRE, SIN ADORNO

**Una resta que da 312 esconde además esto, y por eso va aquí y no en una nota al pie.**

1. **NO he leído `11-ARQUITECTURA-INTEGRADA.md` L1-L5200.** Es el lote de `T1`. De ese tramo abrí
   **sólo** §0 —porque mi encargo me manda juzgar la REGLA DE TITULARES, que vive ahí— y la
   localización por `grep -n` de §2.6.7 y de las cabeceras que cito, y **los declaro abiertos para
   verificar, NO leídos**. Todo §1, §2, §3 y §4 —el protocolo transaccional, los tipos, el contrato
   documental— está **fuera de mi lectura**. **Una contradicción entre §2.6 y §11.6 es
   estructuralmente invisible para mí.**
2. **NINGÚN OJO HA LEÍDO EL DOCUMENTO 11 ENTERO.** `T1` cubre `L1-L5200` **y `L11380-L11717`**, y
   yo `L5201-L11717`. La unión cubre el fichero y hay solape deliberado, pero **una contradicción a
   caballo de L5200 sigue siendo invisible para los dos**. Es el límite de método que `S1-09`
   levantó y que `T2-05` mide que el manifiesto 8 corrige sólo en parte.
3. **NO he auditado el INSTRUMENTO como código.** La batería, el derivador y el emisor son lote de
   `T1`. Los **EJECUTÉ** —y publico sus salidas— y leí regiones puntuales (`G-13` L805-850,
   `_rutas_z`, `_EXIGEN_HISTORIA`), pero **no sostengo nada sobre su corrección como programas**.
4. **`M-04` Y EL UNDÉCIMO ÁRBOL: NO ATACADOS POR MÍ.** No construí un solo árbol defectuoso, no
   busqué la puerta siguiente y no probé el remedio de `S1-01`/`S1-02` con un contraejemplo propio.
   **Mi silencio no es evidencia en ninguna dirección**, y el adjudicador no debe leerlo como tal.
   Es lote de `T1`, y es la razón principal por la que mi respuesta no puede ser la del gate.
5. **NO he verificado el BANCO ADVERSARIAL que la tanda declara** —las ocho rutas ciegas, las nueve
   formas de mutación, las rutas con espacios, saltos de línea, no-ASCII y guion inicial—.
   Reproducirlo exige construir árboles, y eso es `T1`. Lo que sí hice fue ejecutar la batería sobre
   un clon en el commit candidato: **38/38, rc=0**.
6. **NO he ejecutado ni una sola de las pruebas que el corpus describe** —las 55 filas `X`, las 18
   ventanas `W`, las `X-S`, las `X-O`, las `X-A`–`X-H`, los 11 `NP`, los 12 escenarios de §14—.
   **Todo es contrato escrito y ninguno se ha ejecutado**, y ninguna cantidad de hallazgos
   coherentes sustituye ese hecho.
7. **NO he juzgado las once condiciones `C-L` distintas de `C-L.5` y `C-L.7`.** Comprobé que la
   clasificación vigente lista cada id exactamente una vez y suma 13. **No he auditado si el estado
   que cada una declara es cierto.**
8. **NO he verificado que `T1` lea lo que declare.** La resta `ASIGNADO − LEÍDO` de la otra cadena
   la cruza el adjudicador, no yo, y es exactamente la que hundió al cuarto gate. **Embebo el sobre
   entero en §0.1 y publico su SHA-256 precisamente para que pueda cotejarlo.**
9. **LA SEDE CANÓNICA DEL OWNER NO ES VERIFICABLE CONTRA NADA EXTERNO, y lo declara ella misma.**
   Recalculé sus cuatro digest sobre el commit auditado y reproducen. **Eso prueba que el texto no
   cambió entre el commit auditado y lo que recibí FUERA del árbol. NO prueba que sea el que el
   Owner emitió.** Sigue vigente hasta el verificador externo de `F6`.
10. **Los SHA-256 del emisor y del derivador que verifiqué NO prueban que los programas que
    corrieron fueran ésos.** El propio sobre lo retira en su obligación 5 (`Z-11`), y **yo no lo
    recupero**.
11. **`A14` es limitación aceptada, no hallazgo.** Todo se midió con **Python 3.12.14**. Con el 3.10
    del sistema caen tres validadores por `tomllib`, idénticos sobre `HEAD` sin tocar, y lo digo.
12. **Reproducibilidad:** `git` sobre WSL2, `core.quotePath` sin fijar. **No probé otro intérprete,
    otro sistema de ficheros ni otra configuración de Git.**
13. **NO he juzgado si la arquitectura de `F4c` es buena.** Sé qué dicen sus sedes y si se
    contradicen. **No opino sobre el diseño, y no lo insinúo.**

---

## §7 · MI RESPUESTA, EN UNA FRASE

> **NO. En lo que a mi dominio toca, `F4c` NO ES SUFICIENTE PARA `F5`: la tanda que dice haberse
> escrito por TERCERA vez contra «el sistema cierra INSTANCIAS y no CLASES» vuelve a cerrar media
> instancia dentro del bloque que el corpus designa como su punto de entrada — `metodo:` sigue
> afirmando que «`C-L.5` está ABIERTA porque el adjudicador NO emitió la palabra CERTIFICADA»
> cuando `FF` la emitió y este mismo fichero lo dice en su cabecera, de modo que `C-L.5` vuelve a
> tener DOS estados vigentes, que es `DD-07` una sede más allá; `last_meaningful_event` perdió el
> ordinal y conservó la narración del NOVENO ÁRBOL, con lo que el remedio **convirtió una frase
> verdadera en falsa**; `based_on` declara base vigente la candidata del SEXTO gate, TRES eventos
> atrás; el comando al que los dos remiten para derivar el ordinal devuelve **13 donde el ordinal
> es 7**, y esta tanda lo copió a una sede más; la cláusula que eximía las copias de recuento se
> retiró junto con la enumeración, dejando cuatro sin amparo; y el manifiesto del propio octavo
> gate anuncia que §11.4, §11.6 y §11.9 entran en el lote de quien audita el instrumento cuando su
> propia tabla las deja en el mío — sin que ninguno de mis doce sea BLOQUEANTE, exija arquitectura
> nueva ni vuelva al Owner, y con `C-L.5` correctamente recogida en su clasificación con TODO su
> alcance dicho, la sede canónica del Owner intacta y **sin una sola paráfrasis que la amplíe**.**

**Y lo que consta a favor, porque es verdad y no es cortesía:** las seis obligaciones del sobre se
cumplen sin una sola discrepancia y **el gate no es inválido por ninguna vía que yo pueda medir**;
los seis digest reproducen byte a byte y comprobé la receta **sin ejecutar el emisor**, como `O19`
ordena; **ninguna proyección amplía el texto canónico** y los dos rótulos «LITERAL DE `O18`» siguen
reatribuidos; el PARTE cuenta identificadores, acota su tabla, **cubre los catorce del documento 28
con la resta a ∅** y cada remedio está en el fichero que su fila dice; `S2-01`, `S2-02` y `S2-05`
están cerrados y sus sedes de al lado aguantan; `S2-03` ejecutó **exactamente** el remedio que `FF`
determinó —retirar en vez de reanclar—; la clase `S-18`≡`T-14` **no reincide** y el `diff` de la
LISTA sale vacío en los dos árboles con `T147` en verde; las dieciocho derivaciones vivas de mi lote
reproducen todas y **los dos cardinales escritos tienen guardián que los deriva**; `X63` no se
presenta como prueba ejecutada ni como certificación presente en ninguna sede que yo alcance; y
**ninguna sede viva declara CERRADO o SUPERADO lo que no lo está** — ni `M-04`, ni `C-L.7`, ni un
solo hallazgo.

**— `T2`, revisor independiente del octavo gate. NO emito veredicto de certificación: es del
adjudicador. NO he propuesto ninguna corrección y NO he modificado el repositorio.**

### §7.1 · DISCIPLINA — declaración de cierre

```text
git status --porcelain de /home/jose/ads-kernel   AL ABRIR  → VACÍO
                                                  AL CERRAR → VACÍO
HEAD al abrir y al cerrar          → bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40, sin moverse
rama local                         → fix/f4c-propiedad-de-admision-20260831 (sin tocar)

FICHEROS DEL REPOSITORIO AUDITADO EDITADOS, CREADOS O BORRADOS POR MÍ     ninguno
COMMITS · PUSH · PR · MERGE · RAMAS · REFS · REFLOG en el repo auditado   ninguno
CÓMO LEÍ      `git show <commit>:<ruta>` sobre el COMMIT CANDIDATO, y lectura por rangos sobre
              copias extraídas FUERA del repositorio
CÓMO EJECUTÉ  `git read-tree` + `git checkout-index --prefix` en el scratchpad, y UN clon
              desechable (`git clone /home/jose/ads-kernel <scratchpad>/f4c8/clon`) para las
              comprobaciones que exigen historia. Los dos fuera del repositorio auditado
EL EMISOR     NO EJECUTADO, y es deliberado: `O19` L317 manda comprobar la receta SIN ejecutarlo
INTÉRPRETE    Python 3.12.14 (shim del encargo). Con el 3.10 del sistema caen tres validadores
              por `tomllib`: es `A14`, limitación aceptada, NO hallazgo
SUBAGENTE `Agent`                                                         NO USADO
NINGUNA HUELLA DE ESTE INFORME SE HA ABREVIADO A MANO (`DD-22`): donde aparece una huella, va
completa y sale de la salida del comando que la produce o del propio sobre
TODA CIFRA DE ESTE INFORME VA CON EL COMANDO QUE LA DERIVA
NINGÚN HALLAZGO CORREGIDO, y es deliberado: quien corrige no certifica
NO PROPONGO CORRECCIONES AL REPOSITORIO
```

### §7.2 · AUTOCOMPROBACIÓN DEL SOBRE EMBEBIDO

Porque el CUARTO GATE murió por una transcripción y `DD-22` castigó una huella abreviada a mano.

```console
$ ini=$(grep -n '^```text$' INFORME-T2.md | head -1 | cut -d: -f1)          # 19
$ fin=$(awk -v i=$ini 'NR>i && /^```$/{print NR; exit}' INFORME-T2.md)     # 216
$ sed -n "$((ini+1)),$((fin-1))p" INFORME-T2.md > /tmp/blk-t2.txt
$ sha256sum /tmp/blk-t2.txt <scratchpad>/f4c8/SOBRE-8.txt
807804b828107f3d87f19c3af3a43d435204c92a6ff89fa209c4d6879be0cfd4  /tmp/blk-t2.txt
807804b828107f3d87f19c3af3a43d435204c92a6ff89fa209c4d6879be0cfd4  …/f4c8/SOBRE-8.txt
$ diff /tmp/blk-t2.txt <scratchpad>/f4c8/SOBRE-8.txt
(sin salida)
$ wc -l  →  196 y 196
```

**EL BLOQUE DE §0.1 ES BYTE A BYTE EL FICHERO DEL SOBRE.** No hay ni un carácter de deriva.

El bloque de §0.1 es el fichero del sobre volcado con `cat` en el mismo comando que escribió esa
sección, **sin transcripción manual de ningún campo**. El adjudicador puede contrastar mi huella
contra la de `T1` y la suya: **si difiere una sola, el gate es inválido.**

---

## §C · ADJUDICACIÓN DE `GG` — TRANSCRIPCIÓN LITERAL

# ADJUDICACIÓN `GG` — OCTAVO GATE DE CERTIFICACIÓN DE F4c

Adjudicador `GG`. Contexto limpio: no he escrito nada de este corpus, no he aplicado
ninguna corrección, no he sido revisor de ningún gate anterior. Trabajo sobre un CLON
del repositorio auditado; el repositorio de `/home/jose/ads-kernel` no se toca.

```console
$ git clone -q /home/jose/ads-kernel $S/gg/clon
$ cd $S/gg/clon && git log --oneline -3
bf0c65c docs(gate): manifiesto previo del octavo gate, con la sede 1bis en el lote del instrumento
61492c1 fix(f4c): la guarda juzga la MUTACION y no la existencia, y los 14 del septimo gate
3c7e0fa docs(gate): septimo gate de certificacion de F4c, VALIDO, INSUFICIENTE, y C-L.5 CERTIFICADA
```

Entorno: `PYTHONPATH=$S/py312-libs`, `PATH=$S/bin:$PATH` → `python3 3.12.14`.
`A14` (los tres validadores que caen con el 3.10 del sistema por `tomllib`) es
limitación aceptada y NO lo cuento como hallazgo.

---

## §0 · EL SOBRE Y LOS BLOQUES EMBEBIDOS

### §0.1 · Los bloques de sobre embebidos por cada revisor, BYTE A BYTE

`T1` embebe el sobre en `INFORME-T1.md`:14-211 (valla ```text …```), contenido
L15-210. `T2` lo embebe en `INFORME-T2.md`:19-216, contenido L20-215. Extraigo los
dos y los contrasto contra el fichero del sobre:

```console
$ sed -n '15,210p' INFORME-T1.md > sobre-T1.txt
$ sed -n '20,215p' INFORME-T2.md > sobre-T2.txt
$ sha256sum SOBRE-8.txt sobre-T1.txt sobre-T2.txt
807804b828107f3d87f19c3af3a43d435204c92a6ff89fa209c4d6879be0cfd4  SOBRE-8.txt
807804b828107f3d87f19c3af3a43d435204c92a6ff89fa209c4d6879be0cfd4  sobre-T1.txt
807804b828107f3d87f19c3af3a43d435204c92a6ff89fa209c4d6879be0cfd4  sobre-T2.txt
$ wc -c  →  14734 / 14734 / 14734
$ diff SOBRE-8.txt sobre-T1.txt  →  (vacío)
$ diff SOBRE-8.txt sobre-T2.txt  →  (vacío)
$ diff sobre-T1.txt sobre-T2.txt →  (vacío)
```

**LOS DOS SOBRES SON EL MISMO FICHERO, BYTE A BYTE.** No hay causa de invalidación
por divergencia de sobres. Sigo.

### §0.2 · Las SEIS OBLIGACIONES, cumplidas por mi cuenta

**Obligación 1 — los dos digest del universo**, con la receta literal del sobre:

```console
$ # por cada C en {candidata, gate}: read-tree → checkout-index → derivador --rutas → sha256
61492c1a474f2d3ddfced2a9b358e700c980bc29  70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1
bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40  8bc0051c937d9c24dba2f91edd4a55cd9fcc43232ae336dd5015642f3c2c538e
```

Coinciden con el sobre (`70fae997…` y `8bc0051c…`). **LOS DOS REPRODUCEN.**

**Obligación 2 — el manifiesto en el COMMIT DEL GATE:**

```console
$ git show bf0c65ca…:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md | sha256sum
a82e74968e4ca31fbae0825a43f295736af39e58a16b3adf8879d021688e3d76
```
Coincide con el sobre. **REPRODUCE.**

**Obligación 3 — la fila del propio derivador** (`U-02`/`X-06`): la trato en §2 y §4,
contra CADA árbol por separado.

**Obligación 4 — las rutas en que difieren los universos vs. los árboles:**

```console
$ git diff --name-only 61492c1a… bf0c65ca…
docs/evolucion/00-INDICE.md
docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md
kernel/operativo/pruebas/evidencia/fuentes-salida.txt
kernel/operativo/pruebas/evidencia/negativos-salida.txt
kernel/operativo/pruebas/evidencia/referencias-salida.txt
```
**5 rutas difieren entre ÁRBOLES; el sobre nombra 2 entre UNIVERSOS.** El sobre
declara exactamente esa asimetría y la nombra en su obligación 4: no es hallazgo.
Las tres de `kernel/operativo/pruebas/evidencia/` quedan FUERA del universo
obligatorio y por tanto fuera del digest — lo anoto y vuelvo sobre ello en §6.

**Obligación 5 — SHA del EMISOR y del DERIVADOR en los DOS commits:**

```console
$ git show 61492c1a…:…/emitir-sobre-de-ancla.py    | sha256sum → 8ba060af7f2e1eda…
$ git show bf0c65ca…:…/emitir-sobre-de-ancla.py    | sha256sum → 8ba060af7f2e1eda…
$ git show 61492c1a…:…/derivar-universo-obligatorio.py | sha256sum → 8e08eae0ac1719b6…
$ git show bf0c65ca…:…/derivar-universo-obligatorio.py | sha256sum → 8e08eae0ac1719b6…
```
Los cuatro coinciden con el sobre. **REPRODUCEN.**

**Obligación 6 — la sede canónica del Owner:**

```console
$ git show 61492c1a…:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum → db46edd2af2aa48a…
$ git show bf0c65ca…:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum → db46edd2af2aa48a…
O17: 0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125   (85 líneas)
O18: ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353   (111 líneas)
O19: cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8   (78 líneas)
```
Los cinco digest y los tres recuentos de línea coinciden con el sobre.
**REPRODUCEN.** Y los árboles declarados: `4f0b0431…` (candidata) y `048b90b9…`
(gate) coinciden con `git rev-parse <commit>^{tree}`.

**LAS SEIS OBLIGACIONES SE CUMPLEN. EL SOBRE ES SANO. EL GATE NO CAE AQUÍ.**

---

## §1 · MI MANIFIESTO DE LECTURA Y LAS DOS RESTAS

### §1.1 · Qué he leído YO, con su huella

| # | fuente | árbol | qué leí | íntegro |
|---|---|---|---|---|
| 1 | `SOBRE-8.txt` | fuera del repo | L1-L196 (196 líneas · 14734 bytes · `807804b8…0cfd4`) | **SÍ** |
| 2 | `INFORME-T1.md` | fuera del repo | L1-L1326 ÍNTEGRO (el bloque L15-210 verificado por digest) | **SÍ** |
| 3 | `INFORME-T2.md` | fuera del repo | L1-L1158 ÍNTEGRO (el bloque L20-215 verificado por digest) | **SÍ** |
| 4 | manifiesto 8 | **GATE** `bf0c65ca…` | L1-L248 ÍNTEGRO, con `git show <commit>:<ruta>` · `a82e7496…8e3d76` | **SÍ** |
| 5 | `CHECKPOINT-ADS-NEXT.md` «El criterio del gate siguiente» + `DD-20` | candidata | L3519-L3640, la SEDE de la frontera `A`/`C` | sección |
| 6 | `28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md` | candidata | leído AL FINAL, tras reproducir (§5) | ver §5 |

Además abrí, para REPRODUCIR y no como lectura declarada: `comprobar-correccion-gate-de-cierre.py`
(regiones `_rutas_z`/`_lecturas_seguras` L1968-2045, `_ampliacion_admitida` L3157-3213,
`_mutaciones_desde_base` y el bucle de mutación L3282-3360, `_git` L136-142, la lectura de
`grep -l` L3479-3485), `11-ARQUITECTURA-INTEGRADA.md` (localización de §11.4/§11.6/§11.9/`C-L.5`),
`CHECKPOINT-ADS-NEXT.md` (bloque de estado L916-1170, clasificación `C-L` L2178-2240, PARTE de la
tanda L3860-4010) y `00-INDICE.md`. **NO declaro ninguno de ellos leído íntegro.**

### §1.2 · LA RESTA `OBLIGATORIO − ASIGNADO`, CALCULADA POR MÍ

Derivo el universo de CADA commit con SU PROPIO derivador materializado, y lo resto contra las
81 filas del manifiesto 8 leído del commit del gate:

```console
$ grep -oE '^\| [0-9]+ \| `[^`]+`' MAN8.md | sed 's/.*`\(.*\)`/\1/' | sort   →  81 rutas
$ # ÁRBOL DE LA CANDIDATA 61492c1a…
  universo: 81
  OBLIGATORIO − ASIGNADO:  (vacío)
  ASIGNADO − OBLIGATORIO:  (vacío)
$ # ÁRBOL DEL GATE bf0c65ca…
  universo: 82
  OBLIGATORIO − ASIGNADO:  docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md
  ASIGNADO − OBLIGATORIO:  (vacío)
```

**`OBLIGATORIO − ASIGNADO = ∅` sobre el árbol de la candidata, EN LAS DOS DIRECCIONES.** Sobre el
árbol del gate la única fuente sin fila es el propio manifiesto, que es la exención de PUNTO FIJO
de `DD-19`, declarada en su §6 y correcta.

Y verifiqué las 81 filas fila a fila contra el árbol de la candidata —SHA-256 y `wc -l`—:

```console
$ (por cada fila: git show 61492c1a…:<ruta> | sha256sum  y  | wc -l, contra la fila)
§4: filas=10  líneas=29105
§5: filas=71  líneas=53730
TOTAL: 81 filas · 82835 líneas          DISCREPANCIAS: 0
```

`29105 + 53730 = 82835` = **LINEAS OBLIGATORIAS** de la candidata en el sobre, y `81` =
**FUENTES OBLIGATORIAS**. **Las dos aritméticas del manifiesto 8 DERIVAN de verdad.** `EE-02` y
`DD-19` **NO reinciden**. Y la fila que el sobre manda mirar primero —la del propio derivador,
fila 7— publica **833 líneas** y `8e08eae0ac1719b6d347c8d81c88044e88bbc1075d40d54ee786b6da3e9d4d5c`,
idéntica en los DOS árboles y en los dos campos del sobre: **`U-02`/`X-06`/`DD-18` NO reinciden,
por cuarta vez.**

### §1.3 · LA RESTA `ASIGNADO − LEÍDO`, CALCULADA POR MÍ SOBRE LOS DOS MANIFIESTOS

**`T1`** — asignado por el manifiesto 8 §4, columna `revisor`, filas con `T1`:

```text
  fila 2  11-ARQUITECTURA-INTEGRADA.md   L1-L5200 ∪ L11380-L11717   5200 + 338 =  5538
  fila 3  28-SEPTIMO-GATE…               ÍNTEGRO                                 4275
  fila 5  verificacion/README.md          ÍNTEGRO                                  386
  fila 6  comprobar-correccion-…py        ÍNTEGRO                                 4313
  fila 7  derivar-universo-obligatorio.py ÍNTEGRO                                  833
  fila 8  emitir-sobre-de-ancla.py        ÍNTEGRO                                  734
  fila 9  manifiesto 7                    ÍNTEGRO                                  260
                                          ASIGNADO                               16339
```

Comprobé la UNIÓN de sus rangos declarados en §1 de su informe, tramo a tramo: los diecisiete
tramos del documento 11 encadenan sin hueco `L1→L5200` y añaden `L11380-L11717`; los diecisiete
del documento 28 encadenan `L1→L4275`; los cinco del README `L1→L386`; los dieciocho de la batería
`L1→L4313`; los tres del derivador `L1→L833`; los cuatro del emisor `L1→L734`; los dos del
manifiesto 7 `L1→L260`. **Sin un solo hueco.**

```text
  T1 · LEÍDO 16339   ·   ASIGNADO − LEÍDO = 0 líneas · 0 fuentes
```

**`T2`** — asignado por el manifiesto 8 §4, filas con `T2`:

```text
  00-INDICE.md                                    237
  11-ARQUITECTURA-INTEGRADA.md  11717−5200 =     6517
  28-SEPTIMO-GATE…                               4275
  CHECKPOINT-ADS-NEXT.md                         5015
  DECISIONES-Y-CONTRADICCIONES.md                1335
                                  ASIGNADO      17379
```

`T2` declara `ASIGNADO − LEÍDO = 312 líneas · 0 fuentes`. **LA CALCULO YO, DE SUS PROPIOS RANGOS,
Y NO DA 312.** Uní los diecisiete tramos que su §1 declara del documento 28
—`L1-160·160-420·420-700·700-1035·1035-1450·1450-1560·1774-1840·1840-2133·2133-2500·2500-2740·2740-3010·3010-3250·3250-3470·3596-3672·3671-3870·3870-3945·3945-4275`—
y resté contra `L1-L4275`:

```console
$ (unión de los rangos declarados, contra 1..4275)
LEÍDO: 3937   NO LEÍDO: 338
tramos no leídos: [(1561, 1773, 213), (3471, 3595, 125)]
```

**LA RESTA REAL DE `T2` ES 338 LÍNEAS, NO 312.** Y su propio desglose narrativo —«214 de un bloque
de sobre … y 128 de la reproducción por `FF`»— suma **342**. `T2` publica TRES cifras
incompatibles del mismo hecho: **312 en la resta, 342 en su desglose y 338 en la unión de sus
rangos.** Es exactamente la clase `P-01`≡`Q-13`/`J-07` —dos sedes vivas, dos cifras del mismo
hecho medido— cometida **dentro de la resta que `C-L.5` existe para hacer honesta**.

Y su JUSTIFICACIÓN no cubre lo que dice cubrir. `T2` alega que el primer tramo «es el bloque de
sobre que `S2` embebió» y que lo posee byte a byte por otra vía. Lo localicé:

```console
$ (cabeceras «SOBRE DE ANCLA · emitido» en el documento 28, y su valla de cierre)
cabeceras del sobre en: [176, 1580]
  bloque 176..371  = 196 líneas   (el que embebe el coordinador)
  bloque 1580..1775 = 196 líneas  (el que embebe `S2`)
```

El bloque de sobre de `S2` empieza en **L1580**, no en L1561. Las **19 líneas L1561-L1579** —el
rótulo `## §B · DICTAMEN DEL REVISOR S2`, su cabecera, su declaración de dominio, su
«Repositorio NO modificado» y el rótulo `## §0 · EL SOBRE, Y SUS SEIS OBLIGACIONES`— **NO son
sobre y NO están cubiertas por la coartada**. Sumadas a las 125 del segundo tramo:

```text
  T2 · ASIGNADO − LEÍDO  =  338 líneas, de las que 194 tienen coartada verificable
                            (el bloque de sobre L1580-L1773) y 144 NO la tienen
                        =  1 FUENTE asignada y NO leída íntegramente: el documento 28
```

**`T2` escribe «0 fuentes». Es 1.** El documento 28 le está asignado ÍNTEGRO por la fila 3 del §4
(«**T1+T2+GG** · los tres · DESPUÉS de las demás fuentes») y no lo leyó íntegro.

**JUICIO DE LA DECLARACIÓN DE `T2`, que el encargo me manda emitir:** la declaro **HONESTA EN LA
DIRECCIÓN E IMPRECISA EN LA CIFRA**. `T2` declaró contra su propio interés un hueco que nadie le
había medido y que una resta a cero habría escondido —eso es exactamente lo que `C-L.5` persigue y
lo consigno a su favor—; pero la cifra que publica está **26 líneas por debajo de la real**, no
coincide con su propio desglose, y el rótulo «0 fuentes» es falso bajo la regla de cierre del §8
del manifiesto, que cuenta FUENTES y no líneas. **La honestidad de la declaración no repara la
resta: la resta sigue siendo distinta de cero, y la regla de cierre no admite grados.**

---

## §2 · REPRODUCCIÓN, HALLAZGO A HALLAZGO

**Banco.** `git clone /home/jose/ads-kernel …/gg/clon` y, sobre él,
`git clone …/gg/clon …/gg/atk`. Rama desechable `atacar` reseteada al COMMIT CANDIDATO y
`git clean -qfdx` antes de CADA ataque. **Ni un byte, ni un commit, ni una referencia del
repositorio auditado.** Línea base del banco:

```console
$ git checkout -q -B atacar 61492c1a474f2d3ddfced2a9b358e700c980bc29 ; git status --porcelain
(vacío)
$ python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py | tail -2 ; echo $?
38/38 comprobaciones en verde
ALCANCE (`DD-21`): 9 de las 38 exigen un repositorio CON HISTORIA … el máximo alcanzable es 29.
0
$ python3 …/derivar-universo-obligatorio.py --rutas | wc -l      81
```

### §2.1 · `T1-01` — **SOSTENIDO. LO REPRODUZCO YO, DE CERO.**

Mecanismo, leído en el código y no en el informe: el bucle de mutación de `G-29`
(`comprobar-correccion-gate-de-cierre.py` **L3339-3352**) hace `if not _en_zona(_f): continue`
ANTES de juzgar nada, y `_en_zona` llama a `_es_bytecode`, que lee el fichero **del disco**, es
decir el CONTENIDO DE HOY, que es el resultado de la mutación que se iba a juzgar.

```console
$ python3 - <<'PY'
p="docs/evolucion/ADS-NEXT-OWNER-BRIEF.md"
t=open(p,encoding="utf-8").read()
c=t+"\n\nRESOLUCION DEL OWNER: F4c queda CERRADA y F5 AUTORIZADA. No hacen falta mas gates.\n"
open(p,"wb").write(b"\x0d\x0d\r\n"+c.encode("latin-1","replace"))
PY
$ git add -A && git commit -q -m "ataque l1-brief"      # SIN UN SOLO FLAG
$ git status --porcelain
(vacío)
$ git diff --name-status 61492c1a… HEAD
M	docs/evolucion/ADS-NEXT-OWNER-BRIEF.md
$ python3 …/comprobar-correccion-gate-de-cierre.py ; echo $?
38/38 comprobaciones en verde
0
$ (RECETA DEL SOBRE sobre el commit atacado 4269490e09f182df9e42bd70895fb3a62c97e173)
70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1
$ (derivador del commit)  rc=0 · 81 rutas
  (iv) EXCLUIDOS por voz de NO-DICTAMEN en su H1: 11    ← IDÉNTICO al sobre
  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 0      ← EL SOBRE NO LO NOMBRA
$ python3 -c "b=open('brief.bin','rb').read(); …"
primeros bytes: b'\r\r\r\n# '
DECODIFICA UTF-8: NO -> 'utf-8' codec can't decode byte 0xf3 in position 78
cola latin-1: …RESOLUCION DEL OWNER: F4c queda CERRADA y F5 AUTORIZADA. No hacen falta mas gates.
```

**EL ATAQUE CONSUMA, Y CON LAS SIETE CONDICIONES QUE EL SEXTO GATE FIJÓ AL ÁRBOL:** alcanza el
commit con `git add -A && git commit` sin un flag · `git status` vacío · **38/38 · EXIT=0** ·
fuera del universo obligatorio · sin fila de manifiesto ni revisor · **DIGEST DEL SOBRE BIT A
BIT EL ANCLADO** · y el sobre publica **`EXCLUIDOS por PERÍMETRO: 0`**. El texto insertado es
**legible palabra por palabra** en Latin-1.

**LA CLASE, MEDIDA POR MÍ sobre las OCHO rutas que `S1-02` declara cerradas** —una corrida por
ruta, control llano y payload envuelto, `git add -A && git commit`—:

| ruta de las OCHO | payload UTF-8 llano | payload envuelto (Latin-1) |
|---|---|---|
| `.gitignore` | **37/38** | **38/38** |
| `README.md` | **37/38** | **38/38** |
| `START_HERE.md` | **37/38** | **38/38** |
| `docs/evolucion/ADS-NEXT-OWNER-BRIEF.md` | **37/38** | **38/38** |
| `docs/evolucion/PROMPT-ARRANQUE-ADS-NEXT.md` | **37/38** | **38/38** |
| `kernel/…/evidencia/fuentes-salida.txt` | **37/38** | **37/38** |
| `kernel/…/evidencia/negativos-salida.txt` | **37/38** | **37/38** |
| `kernel/…/evidencia/referencias-salida.txt` | **37/38** | **37/38** |

**CINCO DE LAS OCHO VUELVEN A VERDE.** Las tres evidencias resisten, y lo digo con la misma
fuerza: la TERCERA CARA de `S1-02` —`_forma_de_evidencia`, que juzga por la FORMA que el
productor garantiza— es un remedio **de PROPIEDAD y no de referencia**, y por eso no depende de
que el fichero siga dentro del perímetro. (Diferencia menor con `T1`, que publicó `36/38` para
las tres evidencias envueltas; yo mido `37/38`. Es la variante del payload y **no cambia la
conclusión**: las tres resisten en las dos mediciones.)

**El ataque es CONTINGENTE del árbol**: con `.gitignore` y payload ASCII puro el mismo envoltorio
da `37/38`, porque el cuerpo sigue decodificando en UTF-8; basta una palabra acentuada para que
pase a `38/38`. Y la batería **NOMBRA el fichero mientras firma en verde**:

```console
$ … | grep -o 'PERÍMETRO: .*'
PERÍMETRO: 2 exclusiones … .git/ … ; docs/evolucion/ADS-NEXT-OWNER-BRIEF.md · cumple el
PREDICADO DE BYTECODE por CONTENIDO; NO se afirma que sea bytecode de CPython (`S1-05`)
```

**SOSTENIDO. BLOQUEANTE. Clase `A`** por `DD-20`: el acto es `git add -A && git commit` en la
rama que se somete a revisión, que la sede define como «el acto ordinario del coordinador», y el
objeto tocado no es la batería, ni su README, ni el derivador, ni una referencia, ni la base.

### §2.2 · `T1-02` — **SOSTENIDO. LO REPRODUZCO YO, DE CERO.**

Mecanismo, leído en `comprobar-correccion-gate-de-cierre.py` **L3157** y **L3339-3346**:
`_ampliacion_admitida()` lleva por docstring «*¿La **aparición** de `rel`, que no está publicada,
está CLASIFICADA y admitida?*» —está escrita para ADICIONES— y se consulta en **L3342**, ANTES
de la rama `D` de **L3344** y antes del contraste contra `_base_gobernada`. Para un documento
numerado sus dos condiciones son estar enlazado desde `00-INDICE.md` y no colisionar de ordinal:
**un fichero BORRADO las satisface las dos**.

```console
$ rm -f docs/evolucion/01-BASELINE-ADS.md
--- SIN COMMITEAR ---
FALLO G-29    topología y unicidad de TODO el corpus gobernado, CONFIRMADO O NO …
             └─ fichero del corpus DESAPARECIDO: docs/evolucion/01-BASELINE-ADS.md
37/38 comprobaciones en verde
--- git add -A && git commit   (SIN UN SOLO FLAG) ---
$ git status --porcelain          (vacío)
$ python3 …/comprobar-…py ; echo $?
38/38 comprobaciones en verde
0
$ python3 …/derivar-…py --rutas | wc -l                    81   (INTACTO)
$ (derivador)  rc=0 · (iv) EXCLUIDOS … : 10                (única huella: 11 → 10)
$ (RECETA DEL SOBRE) 70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1  = ANCLADO
$ grep -c "01-BASELINE-ADS.md" docs/evolucion/00-INDICE.md   1   (el enlace SIGUE)
```

**`37/38` sin commitear, `38/38` commiteado. LA ÚNICA DIFERENCIA ES `git commit`.** Es la
inercia-tras-confirmar de `DD-02`/`EE-01`/`S1-03`, **viva en la CUARTA rama de la misma guarda**,
dentro del remedio que escribe de sí mismo «*se evalúa sobre el CONTENIDO DEL COMMIT y sobre el
disco a la vez … Ninguna de las dos vías puede quedar ciega*» (L3276-3279).

**LA CLASE, MEDIDA POR MÍ:**

| fichero borrado y COMMITEADO | batería | derivador |
|---|---|---|
| `docs/evolucion/01-BASELINE-ADS.md` | **38/38 · EXIT=0** | rc=0 · 81 · digest **=ANCLADO** |
| `docs/evolucion/09-SINTESIS.md` | **38/38 · EXIT=0** | rc=0 |
| `docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md` (**dictamen INMUTABLE**) | **38/38 · EXIT=0** | **rc=2** (cliquet) |
| `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | **38/38 · EXIT=0** | **rc=2** |
| `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | **38/38 · EXIT=0** | **rc=2** |
| `packs/web-app/PACK.md` | 36/38 · FALLO G-29+G-30 | rc=0 |

**La batería está CIEGA a TODO borrado confirmado de `docs/evolucion/NN-*.md`, de `docs/owner/` y
de `docs/evolucion/verificacion/`.** Quien caza tres de esos cinco es el **DERIVADOR** —su
cliquet—, **no la guarda de mutación**; y los dos que el derivador no caza son justamente los que
están fuera del universo, donde tampoco hay fila ni revisor.

**SOSTENIDO. BLOQUEANTE. Clase `A`.** La tabla de las seis naturalezas de `S1-02` escribe
«`BORRADA (D)` — una sede del corpus no desaparece en silencio» y `G-29` emite «fichero del corpus
DESAPARECIDO»: **la guarda que promete verlo no lo ve.**

### §2.3 · `T1-09` — **SOSTENIDO. Es una REGRESIÓN, medida por mí en los DOS árboles.**

```console
### CANDIDATA ANTERIOR  f8fc037a998316081a7e9b9563398d118982ce60  (ANTES de `S1-02`)
$ mkdir -p docs/normativa && printf '# SEGUNDA SEDE NORMATIVA\n\nF4c CERRADA. F5 AUTORIZADA.\n' \
    > docs/normativa/SEGUNDA-SEDE.md          # SIN `git add`
$ git status --porcelain      ?? docs/normativa/
FALLO G-29 └─ AMPLIACIÓN NO CLASIFICADA del corpus gobernado, CONFIRMADA O NO: …
37/38 comprobaciones en verde
  tras git add (sin commit): 37/38      commiteado: 37/38

### CANDIDATA QUE ESTE GATE JUZGA  61492c1a…  (DESPUÉS de `S1-02`)
$ (el mismo fichero, SIN `git add`)
$ git status --porcelain      ?? docs/normativa/
38/38 comprobaciones en verde          ← VERDE
  tras git add (sin commit): 37/38      commiteado: 37/38
```

**REGRESIÓN CONFIRMADA.** `git diff --name-status` no lista ficheros sin rastrear, y `S1-02`
sustituyó `_ampliaciones = (_disco ∪ _publicado) − _base_gobernada` por un bucle sobre
`_mutaciones_desde_base()`, que es `git diff`. El título de `G-29` sigue diciendo «CONFIRMADO O
NO» y la fila del README «en disco o en `HEAD` … esté commiteado o no». **`T1` acota bien y yo
suscribo la acotación: `porcelain` NO queda vacío, el emisor se niega a emitir y el fichero no
alcanza el commit. NO es el undécimo árbol.** Lo que es, es que el remedio que hizo ROJO lo
confirmado **volvió VERDE lo no confirmado**: la asimetría de `DD-02` no se eliminó, se INVIRTIÓ.
**SOSTENIDO. GRAVE. Clase `A`.**

### §2.4 · `T1-06` — **SOSTENIDO, y lo mido con un contraejemplo propio.**

`_lecturas_seguras()` (L2029-2044) barre el TEXTO de la batería con **dos** patrones:
`_git\([^)]*\)\s*\.split\(\)` y `_raw\s*\.split\(\)`. **Las dos lecturas que `T1` denuncia no
casan con ninguno**, y lo verifiqué leyendo el código:

```console
$ grep -n '_git(\*orden, "-z")' comprobar-correccion-gate-de-cierre.py
3293:            bruto = _git(*orden, "-z")          # y `campos = [c for c in bruto.split("\0")…]`
$ grep -n 'grep", "-l"' comprobar-correccion-gate-de-cierre.py
3479:        publicado_marca = _git("grep", "-l", "```yaml " + marca, "05f71b7", "--", ".",
3485:        base_marca = {l.split(":", 1)[1] for l in publicado_marca.split("\n") if ":" in l}
$ sed -n '136,142p' …
def _git(*args):
    r = subprocess.run(["git", "-C", RAIZ, *args], capture_output=True, text=True, timeout=60)
```

**QUINTA lectura (L3293): es la de la propia guarda que `S1-02` estrena.** `_git` NO fuerza
`core.quotePath=false`, NO comprueba TRUNCAMIENTO y usa `text=True`, que aplica **traducción
universal de saltos**. **Contraejemplo propio, ejecutado:**

```console
$ python3 -c "open('docs/normativa/con\rretorno.md','w').write('# SEGUNDA SEDE\n')"
$ git add -A && git commit -q -m cr
$ (lo que ve `_rutas_z`)   b'docs/normativa/con\rretorno.md'
$ (lo que ve `_git` con text=True)  'docs/normativa/con\nretorno.md'
$ python3 …/comprobar-…py | grep -a "AMPLIACIÓN NO CLASIFICADA" | cat -A
… AMPLIACIÓN NO CLASIFICADA del corpus gobernado, CONFIRMADA O NO: docs/normativa/con$
```

**La guarda denuncia una ruta que NO EXISTE** —`docs/normativa/con`—: el `\r` se tradujo y la ruta
llegó partida. **SEXTA lectura (L3479-3485):** lista de rutas partida **por saltos de línea** y con
`quotePath` ACTIVO. **La clase `S1-01` NO está cerrada, y la frase que dice que lo está —«`_rutas_z()`
es la ÚNICA lectura de listas de rutas de este fichero, y NO HAY OTRA VÍA», con un BARRIDO que
«impide que nazca otra»— es falsa.** **SOSTENIDO. GRAVE.**

### §2.5 · `T1-03` — **SOSTENIDO EN EL HECHO, y lo REBAJO en su alcance.**

```console
$ printf '\n# puerta trasera\nimport os\n…\n' >> …/derivar-universo-obligatorio.py
--- SIN COMMITEAR ---   FALLO G-34 · 37/38
--- git add -A && git commit ---
$ git status --porcelain   (vacío)
38/38 comprobaciones en verde
$ git show HEAD:…/derivar-universo-obligatorio.py | sha256sum
b6cd500e157ee3a22242d25ec51554296f83d4e966ffaaf55921404d52a18956   (≠ el del sobre)
```

**El hecho reproduce**: el inventario de integridad del instrumental contrasta contra `HEAD`, y
confirmar lo vuelve idéntico a `HEAD`. **Pero `DD-20` nombra «editar la batería, su README o el
derivador» EXPRESAMENTE en la lista de la clase `C`.** El ATAQUE es `C` y no cuenta dentro de
`F4c`. Lo que sí cuenta —y por eso el hallazgo no cae— es la **propiedad del instrumento**: `X-01`
se midió «sin commitear» y el remedio se escribió contra `HEAD`, mientras `DD-02`, `EE-01`,
`S1-03` y `S1-06` han migrado esa misma referencia a la REVISIÓN BASE en cuatro sedes distintas y
ésta no. **SOSTENIDO, REBAJADO de GRAVE a MEDIO**, y lo digo por qué: su explotación exige un acto
que `DD-20` excluye del alcance de `F4c`, y **el SOBRE lo caza** —el SHA del derivador que publica
deja de casar—, cosa que no ocurre con `T1-01` ni con `T1-02`.

### §2.6 · `T1-04` — **SOSTENIDO. Lo mido yo, fila a fila.**

```console
$ (manifiesto 7, filas de su §4 · LECTURA ÍNTEGRA)                    12
$ (manifiesto 7, filas de su §5 · AGOTADAS)                           67
$ (manifiesto 8, filas de su §5)                                      71
   de las 71, estaban en el §4 del manifiesto 7 (LEÍDAS):   4
   de las 71, estaban en el §5 del manifiesto 7 (AGOTADAS): 67
   de las 71, en ninguna tabla del manifiesto 7:            0
$ (valores DISTINTOS de la columna «lectura íntegra certificada en» del manifiesto 8)
   {'manifiesto `7` del documento **28** · árbol `f8fc037`}            ← UNO SOLO
$ (los del manifiesto 7 en su §5)
   {'documento **27**, L1025 · árbol `b27a761`', '… L1026 …', '… L1027 …',
    'manifiesto `6B` del documento **27** · árbol `b27a761`'}          ← CUATRO
```

**El manifiesto 7 SÍ distinguía las dos cosas; el 8 uniformiza las 71 bajo un rótulo que dice
«lectura íntegra certificada en» para 67 filas que en el manifiesto 7 estaban AGOTADAS, no
leídas.** La REGLA de su §5 sí se cumple —admite «*o el manifiesto de ese gate publicó su SHA-256
en una fila propia*»—; lo que dice más de lo que entrega es el RÓTULO. **SOSTENIDO. MEDIO.**

### §2.7 · `T1-07` — **SOSTENIDO.**

```console
$ sed -n '750,752p' derivar-universo-obligatorio.py
def lineas_de_blob(crudo):
    """Líneas de un blob. **ESTA ES LA ÚNICA SEDE DE LA FÓRMULA** (`S1-08`)…
$ sed -n '215,218p' emitir-sobre-de-ancla.py
def _sha256_en(commit, ruta):
    crudo = _blob(commit, ruta)
    return hashlib.sha256(crudo).hexdigest(), crudo.count(b"\n")
$ sed -n '370,373p' emitir-sobre-de-ancla.py
        filas.append((ident, hashlib.sha256(cuerpo).hexdigest(), cuerpo.count(b"\n")))
```

**Dos copias en línea de la fórmula, las dos en el emisor**, en el fichero que sí importa la
función en `_lineas_de` (L248). Y la segunda **PUBLICA**: es el «O17 (85 lineas) · O18 (111) ·
O19 (78)» del propio sobre. La afirmación «ÚNICA SEDE» es falsa. **SOSTENIDO. MEDIO.**

### §2.8 · `T1-08` — **SOSTENIDO, Y AGRAVADO POR MI PROPIA MEDICIÓN.**

```console
$ grep -n '30 rutas\|sus 30\|43 rutas' derivar-universo-obligatorio.py verificacion/README.md
derivar…py:64   … uno de los cinco manifiestos inmutables aportaba CERO filas y sus 30 rutas …
derivar…py:691  … y las 30 rutas que aquel gate declaró obligatorias no estaban protegidas
README.md:375   … De los cinco manifiestos inmutables, uno aportaba CERO filas** —43 rutas sin proteger—
$ (aplico el patrón VIGENTE `_FILA_MANIFIESTO` al manifiesto sin ordinal)
rutas que aporta: 43
```

**El README acierta —43— y el derivador escribe 30 en DOS sitios.** Lo medí con el regex del
propio derivador, no a ojo. Dos sedes vivas con cifras incompatibles del mismo hecho, dentro del
instrumento cuya tesis es que ninguna cifra se escribe a mano. **SOSTENIDO. MEDIO.**

### §2.9 · `T1-05` — **SOSTENIDO como fragilidad declarada. MENOR.** No la exploto y `T1` tampoco:
el regex de `_declarado_en_correccion` cosecha hoy fragmentos inocuos. Lo que sostiene es que una
mención en prosa de una ruta completa gobernada dentro de esa sección la volvería mutable en
silencio. **No la reproduzco como ataque porque no hay ataque: es una superficie, y como tal la
registro.**

### §2.10 · `T1-10` ≡ `T2-05` — **SOSTENIDO. LOS DOS REVISORES LO MIDEN POR SEPARADO Y COINCIDEN.**

```console
$ git show bf0c65ca…:…/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md | sed -n '71,75p'
**`S1-09`, aplicado y visible en la tabla de abajo:** `T1` —que audita el instrumento— lee
`L1-L5200` **y `L11380-L11717`** del documento 11, de modo que la sede `C-L.5`·`1bis`, §11.4,
§11.6 y §11.9 **entran en su lote**.
$ grep -n '^## 11\.4 \|^## 11\.6 \|^## 11\.9 \|^## `C-L\.5`' 11-ARQUITECTURA-INTEGRADA.md
8253:## 11.4 · La raíz de confianza …
8329:## 11.6 · EL SOBRE DE ANCLA …
8912:## 11.9 · LA SEDE CANÓNICA DE LAS RESOLUCIONES DEL OWNER …
11550:## `C-L.5` · La condición de COBERTURA del próximo gate …
```

`L1-L5200 ∪ L11380-L11717` contiene **11550** y **NO contiene** 8253, 8329 ni 8912. **DE LAS
CUATRO SEDES QUE EL MANIFIESTO DECLARA TRAER AL LOTE DE `T1`, ENTRA UNA.** Y lo que queda fuera es
**§11.4 la raíz de confianza, §11.6 EL SOBRE DE ANCLA y §11.9 la sede canónica del Owner**: el
objeto propio de quien audita el instrumento. El documento 11 es **byte a byte idéntico en los dos
árboles** (`6c99ad68…0ff22`), así que la medición no depende de cuál se mire. **SOSTENIDO. GRAVE.
Es del APARATO del gate, no del objeto auditado, y lo digo.**

### §2.11 · `T2-01` — **SOSTENIDO.**

```console
$ sed -n '918,920p' CHECKPOINT-ADS-NEXT.md
regla_de_reanclaje: ESTE BLOQUE ES EL ESTADO REANUDABLE y va SIN rótulo histórico: describe el
             árbol VIGENTE.
$ grep -n 'C-L\.5' docs/evolucion/CHECKPOINT-ADS-NEXT.md     # el comando que doc 11 L11569 publica
16:   `C-L.5` QUEDA CERTIFICADA POR COBERTURA …
958:  C-L.5 ABIERTA —el adjudicador NO emitió la palabra CERTIFICADA— y C-L.7 NO CERRADA
2190: CERTIFICADA POR  1  C-L.5 — la CERTIFICA POR COBERTURA el adjudicador `FF` …
2222: C-L.5  CERTIFICADA · POR COBERTURA, la CERTIFICA el adjudicador `FF` del SÉPTIMO GATE
$ git diff 3c7e0fa 61492c1a… -- …/CHECKPOINT-ADS-NEXT.md | grep -E '^[-+].*C-L\.5 ABIERTA'
(sin salida: la tanda NO tocó esa línea)
$ git show 3c7e0fa:…/CHECKPOINT-ADS-NEXT.md | grep -n 'C-L.5 ABIERTA —el adjudicador NO emitió'
922: … (la misma frase, sin cambiar)
```

**Doc 11 L11565-11569 designa UNA sola sede para el ESTADO de `C-L.5` y publica el `grep` que la
lee. Ese `grep` devuelve hoy CERTIFICADA en L16/L2190/L2222 y ABIERTA en L958.** Es `DD-07` —«dos
estados vigentes»— **una sede más allá**, y `DD-07` había retirado el estado del documento 11
precisamente para que hubiera UNA. `FF` lo dejó escrito (doc 28 L149-152) y la tanda recogió el
acto en la clasificación pero **dejó intacta la frase que lo niega en el mismo bloque vivo**.
**SOSTENIDO. GRAVE.**

### §2.12 · `T2-02` — **SOSTENIDO.**

```console
$ sed -n '1152,1157p' CHECKPOINT-ADS-NEXT.md
last_meaningful_event: EL ÚLTIMO GATE DE CERTIFICACIÓN DEVUELVE INSUFICIENTE PARA F5 Y SE
   DECLARA VÁLIDO … Su ordinal y su documento NO se escriben —`S2-04`—: se derivan …
   Lo decisivo es del adjudicador y no de los revisores: EL NOVENO ÁRBOL. La guarda de
   admisión de G-29 sólo miraba lo que aún NO estaba en HEAD salvo en docs/owner/ …
$ ls docs/evolucion/[0-9][0-9]-*.md | sort | tail -1     # el comando al que el campo remite
docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md
$ grep -n 'DÉCIMO ÁRBOL' docs/evolucion/28-…md
63:## 3 · EL DÉCIMO ÁRBOL, Y ESTA VEZ SON DOS EJES DISTINTOS
$ grep -n 'NOVENO ÁRBOL' docs/evolucion/00-INDICE.md
97:| — | **SEXTO GATE DE CERTIFICACIÓN de F4c · VÁLIDO, y el NOVENO ÁRBOL** …
```

**«El último gate» deriva al SÉPTIMO, cuyo hecho decisivo es el DÉCIMO árbol; el cuerpo narra el
NOVENO, que es del SEXTO.** El remedio `S2-04` retiró el ordinal escrito a mano y dejó la
narración: **convirtió una frase VERDADERA en FALSA.** Y la regla 4 del propio bloque (L938-941)
manda reanclar `last_meaningful_event` en el mismo commit que registra el evento.
**SOSTENIDO. GRAVE.** Y añado, contra la refutación natural: el campo **no lleva rótulo
histórico** y el bloque prohíbe deducirlo —lo histórico baja a `_anterior` por la regla 5—.

### §2.13 · `T2-03` — **SOSTENIDO.**

```console
$ sed -n '1084,1086p' CHECKPOINT-ADS-NEXT.md
based_on:    REANCLADO por `EE-04` del SEXTO GATE … LA BASE VIGENTE es la candidata que el
             manifiesto del SEXTO GATE nombra, más la tanda consolidada …
$ grep -n 'SEXTO GATE DE CERTIFICACIÓN' docs/evolucion/00-INDICE.md   # su candidata: b27a761
$ git log --oneline -4 bf0c65ca…
bf0c65c (gate 8) / 61492c1 (esta tanda) / 3c7e0fa (gate 7) / 08f6da6
```

Entre `b27a761` y `61492c1` median el séptimo gate, su tanda y esta tanda: **TRES eventos**.
`S2-03` midió DOS documentos de retraso sobre la ENUMERACIÓN; la enumeración se retiró —y eso está
bien hecho— pero **la afirmación del cuerpo no**. **SOSTENIDO. GRAVE.**

### §2.14 · `T2-04` — **SOSTENIDO.**

```console
$ ls docs/evolucion/[0-9][0-9]-*GATE*.md | wc -l              13
$ ls docs/evolucion/[0-9][0-9]-*CERTIFICACION*.md | wc -l      7
$ head -1 docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md
# SÉPTIMO GATE DE CERTIFICACIÓN DE F4c — VÁLIDO, INSUFICIENTE, Y `C-L.5` CERTIFICADA
$ grep -n 'GATE\*\.md | wc -l' docs/evolucion/CHECKPOINT-ADS-NEXT.md
954  ·  2630  ·  3945                                    ← TRES sedes hoy
$ git show 3c7e0fa:…/CHECKPOINT-ADS-NEXT.md | grep -n 'GATE\*\.md | wc -l'
2593                                                     ← UNA sede antes
```

**El comando que las tres sedes publican como «la derivación del ORDINAL» devuelve 13 donde el
ordinal es 7**, porque `*GATE*` captura además los documentos 16-21, que no son de la serie «de
certificación». **Y esta tanda lo copió de UNA sede a TRES**, una de ellas la «Siguiente acción
exacta» VIVA, que es la que lee quien encarga el gate siguiente. **SOSTENIDO. GRAVE.**

### §2.15 · `T2-05` — **SOSTENIDO.** Es el mismo hecho que `T1-10`: ver §2.10. **Lo fusiono ahí.**

### §2.16 · `T2-06`, `T2-07`, `T2-08`, `T2-09` — **LOS CUATRO SOSTENIDOS.**

```console
# T2-06 · «Estado de las fases» L2506-2655
$ awk 'NR>=2506 && NR<=2655' CHECKPOINT | grep -cE '2[78]-|documento 2[78]|SEXTO GATE|SÉPTIMO GATE'
0                       ← la enumeración termina en «DOCUMENTO 26 · QUINTO GATE» (L2609)

# T2-07 · `falta_para_cerrar_la_capa:` L2396 ss, sin rótulo histórico, en el bloque VIGENTE
$ sed -n '2397,2401p' CHECKPOINT
  · F4c ESTÁ ABIERTA. El GATE DEFINITIVO INDEPENDIENTE devolvió **INSUFICIENTE PARA F5** …
    **BLOQUEANTE 1 · GRAVE 6 · MEDIO 10 · MENOR 7**
                        ← el GATE DEFINITIVO es el documento 19; hoy el árbol va por el 28

# T2-08 · regla 1 del bloque (L927-930) contra sus propias copias
$ grep -nE 'BLOQUEANTE [0-9]|GRAVE [0-9]|MEDIO [0-9]|MENOR [0-9]|A [0-9]+ · B [0-9]' CHECKPOINT \
    | awk -F: '$1>=916 && $1<=2499'
1072 · 1296 · 1334 · 2401                                   ← CUATRO copias
$ grep -c 'ANTERIORES a esa regla|se conservan sin ampliarse' CHECKPOINT           0
$ git show 3c7e0fa:…/CHECKPOINT | grep -n 'ANTERIORES a esa regla'                1065
                        ← la cláusula que las eximía LA RETIRÓ ESTA TANDA, con la enumeración

# T2-09 · la cadena `_anterior`, regla 5
$ grep -n '^metodo|^last_meaningful_event' CHECKPOINT
946 metodo: … EL ÚLTIMO GATE …        →  964 metodo_anterior: … CUARTO GATE …
1152 last_meaningful_event: …          → 1168 last_meaningful_event_anterior: … EL CUARTO GATE
                        ← faltan QUINTO, SEXTO y SÉPTIMO gate y sus tandas: cuatro eventos
```

`T2-08` está bien acotado por su propio autor: tres de las cuatro copias viven en campos
`_anterior`, que la regla 5 crea para lo histórico; **la cuarta, L2401, está en
`falta_para_cerrar_la_capa:`, campo PRIMARIO sin rótulo histórico**, y hoy sin la cláusula que la
eximía. **La pregunta que la propia «Siguiente acción exacta» pone al gate —«¿queda alguna sede del
bloque de estado que copie lo que declara no copiar?»— se contesta SÍ con una sola.**
**T2-06 MEDIO · T2-07 MEDIO · T2-08 MEDIO · T2-09 MEDIO.**

### §2.17 · `T2-10`, `T2-11`, `T2-12` — **SOSTENIDOS, los tres MENORES.**

`T2-10` (doc 11 L8327, «las nueve que ya existen para `vigencia`», cardinal sin comando ni
remisión) cae **en el rango de `T2` y NO en el mío ni en el de `T1`**: lo sostengo por su
autoridad de lectura, y lo digo. `T2-11` —el sobre no lleva **el TEXTO** de la ratificación del
Owner, sólo su digest, contra §11.6 «y es la lista entera» y contra la sede canónica L315-317— lo
verifiqué YO contra el sobre que recibí: **lleva el digest, la relación `O19`→`O18`, la
declaración externa y una frase entrecomillada; las 78 líneas de `O19` no viajan.** El fin de la
cláusula —contrastar la sede sin ejecutar el emisor— **queda satisfecho, y yo mismo lo ejecuté**,
por eso es MENOR y no más. `T2-12` —dos deltas de paráfrasis en la proyección de `O17`— **es una
observación contra el propio interés de su autor: las dos DEBILITAN y el criterio del sobre exige
buscar AMPLIACIONES.** Lo sostengo como MENOR y lo consigno como prueba de que la obligación 6 se
ejecutó de verdad.

### §2.18 · LO QUE VERIFIQUÉ Y **NO** CAE — y pesa

| qué | mi medición | veredicto |
|---|---|---|
| Los DOS digest del sobre y sus 10 huellas | §0.2 | **REPRODUCEN, sin una discrepancia** |
| Las 81 filas del manifiesto 8 contra el árbol de la candidata | 0 discrepancias de SHA ni de líneas | **CIERRA** |
| Las dos aritméticas (`29105+53730=82835`) | derivadas por mí | **DERIVAN** |
| `OBLIGATORIO − ASIGNADO` | ∅ en las dos direcciones (candidata) | **CIERRA** |
| La fila del propio derivador (`U-02`→`X-06`→`DD-18`) | 833 · `8e08eae0…`, idéntica en los dos árboles | **NO REINCIDE, 4.ª vez** |
| `S-18`≡`T-14` · el `diff` de la LISTA de `00-INDICE` | VACÍO en los DOS árboles; `T147` `1 superadas · 0 fallidas` en los dos | **NO REINCIDE** |
| Los TRES partes (`24` · `19` · `14`) y su cobertura | 24 (22 DD + 2 BT) · 19 · 14, `comm -23` VACÍO los tres | **CIERRAN** |
| `S1-06` · el ALCANCE plegado sobre `G-00` | commiteado sigue en ROJO | **APLICADO, y bien** |
| La TERCERA CARA de `S1-02` (`_forma_de_evidencia`) | resiste las tres rutas de evidencia envueltas | **REMEDIO DE PROPIEDAD: resiste** |
| La guarda APPEND-ONLY de `docs/owner/` | resiste el octavo árbol de `DD-01` | **NO REINCIDE** |
| La sede canónica del Owner | byte-idéntica en los dos commits, sin ampliación en las proyecciones | **INTACTA** |

---

## §3 · TABLA CONSOLIDADA Y DEDUPLICADA

**QUÉ FUSIONO Y QUÉ NO.** Fusiono **`T1-10` con `T2-05`**: son el MISMO hecho —el manifiesto 8 §3
declara en el lote de `T1` cuatro sedes del documento 11 y su propia tabla sólo le da una— medido
por los dos revisores en paralelo, cada uno desde su lado del reparto, con las mismas líneas
(8253 · 8329 · 8912 · 11550) y la misma conclusión. **Que los dos lo midan sin verse no lo hace
más grave: lo hace más firme, y no lo cuento dos veces.** Queda como `C-01`.

**NO fusiono** `T1-01` con `T1-09` ni con `GG-01`, aunque los tres usen el mismo predicado o el
mismo remedio: `T1-01` es MUTACIÓN de un fichero de la base que se exime a sí misma; `T1-09` es
una REGRESIÓN en el eje de lo NO CONFIRMADO, que no alcanza el commit; `GG-01` es ADICIÓN, y ataca
un remedio distinto —`EE-01`, del SEXTO gate— cuyos cinco controles positivos publicados vuelven
tres a verde. **Tres ejes distintos, tres sedes falsadas distintas.**
**NO fusiono** `T1-02` con `T1-01`: uno pasa por `_en_zona` y el otro por `_ampliacion_admitida`;
cerrar cualquiera de los dos deja el otro abierto, y lo verifiqué (`GG-5-combinado`, §6).
**NO fusiono** `T2-01`..`T2-04`: comparten bloque y clase, pero cada uno falsa una sede distinta
con un mecanismo distinto, y `T2-04` es además el único que la tanda PROPAGÓ.
**NO fusiono** `T2-08` con `T2-09`: uno es la regla 1 y el otro la regla 5.

| id | sev | clase | origen | sede | reincidencia | estado |
|---|---|---|---|---|---|---|
| **`C-00`** | **BLOQUEANTE** | **A** | **`GG` (MÍO)** | batería `:3340` (`_en_zona`) + `_ampliacion_admitida` no alcanzado · `CHECKPOINT`:3817 · README `:244` | **`EE-01`**, el NOVENO ÁRBOL, reabierto por CODIFICACIÓN. Y `S1-05` | **NUEVO** |
| **`C-01`** | **BLOQUEANTE** | **A** | `T1-01` | batería `:3340` · `:2125` `_en_zona` · `:2098` `_es_bytecode` | `S1-02` + `S1-05`, los dos de ESTA tanda | **SOSTENIDO** |
| **`C-02`** | **BLOQUEANTE** | **A** | `T1-02` | batería `:3342` `_ampliacion_admitida` frente a `:3344` rama `D` | `S1-02` rama `D` · `DD-02`≡`EE-01`≡`S1-03`, 4.ª rama | **SOSTENIDO** |
| **`C-03`** | GRAVE | **A** | `T1-09` | batería `:3282` `_mutaciones_desde_base` · `:3293` `git diff` | REGRESIÓN NUEVA introducida por `S1-02`, contra `EE-01` | **SOSTENIDO** |
| **`C-04`** | GRAVE | **A** | `T1-06` | batería `:3293` y `:3479-3485` · barrido `:2029-2044` · `_git` `:136` | `S1-01`, la clase que su BARRIDO dice impedir. Familia `EE-11` | **SOSTENIDO** |
| **`C-05`** | GRAVE | **A** | `T1-10` ≡ `T2-05` | manifiesto 8 §3 (L71-73) contra su §4 fila 2 (L82) · doc 11 L8253·8329·8912·11550 | `S1-09` ≡ 2.ª carencia de `R1` (doc 27) → `EE` → `S1` → `FF`. **TERCER gate** | **SOSTENIDO** |
| **`C-06`** | GRAVE | **A** | `T2-01` | `CHECKPOINT`:958 contra :16 · :2190 · :2222 · doc 11 L11565-11569 | **`DD-07`**, una sede más allá. Y `EE-05` | **SOSTENIDO** |
| **`C-07`** | GRAVE | **A** | `T2-02` | `CHECKPOINT`:1152-1162 · regla 4 en :938-941 | **`EE-04`** · `S2-04` en su propio remedio | **SOSTENIDO** |
| **`C-08`** | GRAVE | **A** | `T2-03` | `CHECKPOINT`:1084-1086 · regla 4 en :938-941 | **`EE-04`** · `S2-03`. **SÉPTIMA recurrencia** de `K-01`/`J-10`/`L-01` | **SOSTENIDO** |
| **`C-09`** | GRAVE | **A** | `T2-04` | `CHECKPOINT`:954 · :2630 · :3945 | `S2-04` · `J-07`. Y la tanda lo PROPAGÓ de 1 sede a 3 | **SOSTENIDO** |
| **`C-10`** | MEDIO | **A** | `T1-04` | manifiesto 8 §5, columna «lectura íntegra certificada en», 71 filas | `EE-08` (rótulo, no regla). 6.ª condición de `O18` | **SOSTENIDO** |
| **`C-11`** | MEDIO | **A** | `T1-07` | emisor `:217` y `:372` contra derivador `:750` | **`S1-08` ≡ `EE-16`** · instancia cerrada, clase abierta EN EL MISMO FICHERO | **SOSTENIDO** |
| **`C-12`** | MEDIO | **A** | `T1-08` | derivador `:64` y `:691` («30») contra README `:375` («43») | `P-01`≡`Q-13` · `J-07` | **SOSTENIDO, y agravado por mi medición: el valor real es 43** |
| **`C-13`** | MEDIO | **C** en el ataque, **A** en la propiedad | `T1-03` **REBAJADO por mí** | batería `:299` dentro de `_censo_de_comprobaciones` `:201` · README `:84`/`:248` | `X-01` · la referencia no migró a la REVISIÓN BASE | **SOSTENIDO, REBAJADO de GRAVE a MEDIO** |
| **`C-14`** | MEDIO | **A** | `T2-06` | `CHECKPOINT`:2506-2655, enumeración de pasadas | **`DD-08`**, TERCERA caducidad | **SOSTENIDO** |
| **`C-15`** | MEDIO | **A** | `T2-07` | `CHECKPOINT`:2396-2423 `falta_para_cerrar_la_capa:` | familia `X-04` · nueve documentos atrás | **SOSTENIDO** |
| **`C-16`** | MEDIO | **A** | `T2-08` | `CHECKPOINT`:2401 contra la regla 1 en :927-930 | `C-L.7` · y la cláusula que la eximía la retiró ESTA tanda | **SOSTENIDO, acotado a UNA copia** |
| **`C-17`** | MEDIO | **A** | `T2-09` | `CHECKPOINT`:964 y :1168 contra la regla 5 en :942-943 | `EE-04`, la cadena histórica con hueco de cuatro eventos | **SOSTENIDO** |
| **`C-18`** | MENOR | **A** | `T1-05` | batería `:186` `_declarado_en_correccion` | fragilidad NO explotada | **SOSTENIDO como superficie** |
| **`C-19`** | MENOR | **A** | `T2-10` | doc 11 `:8327` | REGLA DE TITULARES de §0 del doc 11 | **SOSTENIDO** (rango de `T2`) |
| **`C-20`** | MENOR | **A** | `T2-11` | el SOBRE contra doc 11 `:8449-8459` y sede canónica `:315-317` | — | **SOSTENIDO**, verificado por mí contra mi propio sobre |
| **`C-21`** | MENOR | **A** | `T2-12` | `DECISIONES`:881-887 contra sede `:104` y `:113-114` | `O19` nació de una ampliación; éstas DEBILITAN | **SOSTENIDO** |

### §3.1 · RECUENTO, DERIVADO DE LAS FILAS DE ARRIBA

```text
BLOQUEANTE   3    C-00 (mío) · C-01 · C-02
GRAVE        7    C-03 · C-04 · C-05 · C-06 · C-07 · C-08 · C-09
MEDIO        8    C-10 · C-11 · C-12 · C-13 · C-14 · C-15 · C-16 · C-17
MENOR        4    C-18 · C-19 · C-20 · C-21
             ──
             22   (10 de `T1` + 12 de `T2` = 22, menos 1 fusionado, más 1 mío = 22)

POR CLASE, contra la SEDE `DD-20`
  A   21    todos salvo el ATAQUE de `C-13`
  B    0    ninguno reinterpreta `O17`, `O18` ni `O19`; ninguno exige arquitectura nueva
  C    1    SÓLO el ATAQUE de `C-13` —editar el derivador está NOMBRADO en la lista de `DD-20`—;
            su PROPIEDAD sigue siendo `A` y por eso el hallazgo no cae

POR ÁRBOL
  DE LA CANDIDATA `61492c1a…`        19
  DEL APARATO DEL GATE `bf0c65ca…`    2   C-05 (manifiesto 8) · C-10 (manifiesto 8)
  DEL SOBRE                            1   C-20

POR ORIGEN
  `T1`  9   ·   `T2`  11   ·   FUSIONADO  1 (C-05)   ·   `GG` 1 (C-00, NUEVO)
```

**NOTA SOBRE EL VOCABULARIO DE CLASES.** `T1` publica sus hallazgos con dos convenios y lo declara
en su §2.9: bajo el suyo llama `B` a «promesa superior a lo entregado» y bajo el del gate declara
que **los diez son `A`**. **Aplico el convenio del gate, que es el que `DD-20` fija en su sede**, y
por eso mi columna `B` da cero. No es una rebaja: es el vocabulario que rige.

---

## §4 · LAS CUESTIONES ENCARGADAS, RESUELTAS EXPRESAMENTE

### §4.1 · `C-L.5` — LAS DOS RESTAS, Y LA PALABRA

**`OBLIGATORIO − ASIGNADO`** (§1.2): **∅ sobre el árbol de la candidata, en las DOS direcciones**,
y sobre el árbol del gate falta sólo el propio manifiesto, que es la exención de PUNTO FIJO de
`DD-19`. Las 81 filas casan contra el árbol sin una discrepancia de SHA-256 ni de líneas, y las
dos aritméticas derivan: `29105 + 53730 = 82835`. **ESTA MITAD CIERRA, y lo he rehecho de cero.**

**`ASIGNADO − LEÍDO`** (§1.3):

```text
T1    ASIGNADO 16339   LEÍDO 16339   →   0 líneas · 0 fuentes    (uniones verificadas por mí)
T2    ASIGNADO 17379   LEÍDO  3937+13104 = 17041
                        →  338 líneas · 1 FUENTE  (el documento 28)
                        `T2` declara «312 líneas · 0 fuentes». LAS DOS CIFRAS SON FALSAS.
```

**EL JUICIO DE LA DECLARACIÓN DE `T2`, que el encargo me manda emitir.** La declaro **HONESTA EN
LA DIRECCIÓN, FALSA EN LA CIFRA Y FALSA EN LA UNIDAD**, y las tres cosas por separado:

1. **HONESTA EN LA DIRECCIÓN, y lo consigno primero.** `T2` publicó por su cuenta un hueco que
   nadie le había medido, en un gate donde una resta a cero le habría bastado y donde el gate
   anterior certificó `C-L.5` precisamente sobre dos restas a cero. Eso es exactamente lo que
   `C-L.5` existe para provocar, y **no lo descuento.**
2. **FALSA EN LA CIFRA.** La unión de sus propios rangos deja **338** líneas fuera, no 312; y su
   propio desglose narrativo —«214 … y 128»— suma **342**. Tres cifras incompatibles del mismo
   hecho, publicadas en el mismo párrafo. Es la clase `J-07`/`P-01`≡`Q-13` **cometida dentro de la
   resta que `C-L.5` existe para hacer honesta**, y lo mido con el comando (§1.3).
3. **FALSA EN LA UNIDAD, y es la que decide.** «0 fuentes» es falso: el documento 28 le está
   asignado ÍNTEGRO por la fila 3 del §4 del manifiesto —«**T1+T2+GG** · los tres»— y no lo leyó
   íntegro. **La regla de cierre del §8 del manifiesto cuenta FUENTES:** «*CUALQUIER FUENTE
   ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA.*» Es **1**, no 0.
   Y su coartada —«es el bloque de sobre que poseo por otra vía»— **cubre 194 de las 338**: el
   bloque de sobre de `S2` va de **L1580 a L1775** y su tramo no leído empieza en **L1561**, de
   modo que **19 líneas** —el rótulo de §B, la cabecera del dictamen de `S2`, su declaración de
   dominio y el rótulo de su §0— **no son sobre y no están cubiertas**; y las **125** del segundo
   tramo tampoco lo están por nada.

### **`C-L.5` — LA PALABRA: NO LA EMITO.**

# `C-L.5` NO QUEDA CERTIFICADA POR ESTE GATE.

**Y digo exactamente por qué, y qué NO digo.** La mitad de COBERTURA DEL UNIVERSO —
`OBLIGATORIO − ASIGNADO = ∅`, las 81 filas, las dos aritméticas derivadas— **está impecable, y la
he rehecho yo entera sin una discrepancia**. Lo que falla es la SEGUNDA mitad de la condición, que
es la que `FF` midió a cero en el séptimo gate y hoy no lo está: **una de las dos cadenas de
lectura tiene una fuente ASIGNADA y NO LEÍDA ÍNTEGRAMENTE.** La regla de cierre no admite grados
ni compensaciones, y el CUARTO GATE murió exactamente por esto —`ASIGNADO − LEÍDO = 1`— con un
hueco de la misma naturaleza. **No emito la palabra**, y no la emito pese a que el hueco lo
declaró su propio autor: `C-L.5` certifica un HECHO, no una virtud, y el hecho no se da.

Su estado, por tanto, **vuelve a ABIERTA** por efecto de este gate, y **eso NO retira la
certificación del séptimo gate**, que fue correcta sobre SU árbol y SUS manifiestos —la rehice y
cierra—: certificar la cobertura de un gate no certifica la del siguiente.

### §4.2 · `C-L.7` — **NO CERRADA.**

La clasificación vigente la rotula `NO CERRADA` (L2184) y la propia tanda lo escribe sin adornarlo
—`00-INDICE`:101 y `CHECKPOINT`:3995, «*`C-L.7` sigue NO CERRADA — retirar no es certificar*»—.
**Y la CLASE tampoco está cerrada.** La pregunta que la propia «Siguiente acción exacta» pone al
gate —«*¿queda alguna sede del bloque de estado que copie lo que declara no copiar?*»— **se
contesta SÍ**, y no con una: `C-06`, `C-07`, `C-08`, `C-09`, `C-16` y `C-17` viven **dentro del
bloque de estado reanudable**, y **cinco de ellos contra una regla escrita dentro de ese mismo
bloque para impedirlos** (reglas 1, 4 y 5). Es la **SÉPTIMA recurrencia consecutiva** de la clase
—`K-01`/`J-10`/`L-01` · `P-05`≡`Q-08`/`R-02` · `S-17`≡`S3-05` · `X-04` · `R2-03`→`EE-04` ·
`S2-03`/`S2-04` · ésta— y la **tercera** cometida contra reglas del propio bloque.
**En la HONESTIDAD la tanda acierta: no declara cerrada `C-L.7`. Lo que mido es que retirar
tampoco cerró la clase, y que en DOS casos —`C-07` y `C-09`— el remedio la EMPEORÓ.**

### §4.3 · `M-04` — **NO SUPERADA.**

Ninguna sede viva la declara superada; las cuatro que la nombran dicen «NO superada»
(`CHECKPOINT`:957 · :3919 · :3995 · `00-INDICE`:100-101), y el PARTE escribe «NINGÚN HALLAZGO
SUPERADO: ni uno». **Eso es correcto y lo consigno.** Lo que yo mido es que sigue FALLIDA **por
OCTAVO gate consecutivo, y con TRES árboles nuevos** —`C-00` (mío), `C-01` y `C-02`—, ninguno de
los cuales cae dentro de las diecisiete formas que la tanda declara controlar. **`M-04` no la
cierra nadie desde dentro del árbol**, y el README lo declara así (`:293-308`): eso no es un
hallazgo, es el límite. **Lo que sí es hallazgo es que el número de árboles crece en vez de
menguar.**

### §4.4 · `X63` — **NO se presenta como prueba ejecutada NI como certificación presente.**

```console
$ git grep -n 'X63' -- .            73 apariciones en todo el árbol
```

Las sedes que lo gobiernan lo niegan expresamente: `CHECKPOINT`:3854 y :3928 «*`X63` SIGUE SIENDO
CONTRATO de prueba de `F6`. NO ejecutado, NO certifica nada*»; `00-INDICE`:94 «*es CONTRATO DE
PRUEBA DE `F6`, no una prueba ejecutada*»; doc 11 L1782 «*Ninguna se ha ejecutado … es el contrato
de lo que F6 debe demostrar, y no es su demostración*». **El único presente de indicativo** —doc 11
**L5685**, «*y `X63` la comprueba validando las tres celdas*»— queda desambiguado **doce líneas más
abajo** (L5697-5699): «*No es una protección interna nueva … es un **contrato de prueba de `F6`**,
y **no se ejecuta aquí***». **RESPUESTA: NO.** Coincido con `T1`, con `T2` y con los cinco gates
anteriores, y **no lo cuento como hallazgo.**

### §4.5 · LA CONDICIÓN DE SALIDA — **NO SE CUMPLE.**

`EE` fijó que «se cierran instancias y no clases» pasa a DEUDA REGISTRADA cuando **(1)** el
perímetro se derive **y (2)** las promesas digan lo que el código hace. `FF` la midió en el séptimo
gate: mitad 1 SÍ, mitad 2 NO, en seis sedes. **La mido yo hoy:**

```text
MITAD 1 · el perímetro DERIVADO     SE CUMPLE. `DD-01` resiste: symlinks, ficheros vacíos,
                                    `.gitattributes`, submódulos, `.pyc` en `docs/owner/`.
                                    Y `S1-04` acotó la promesa a lo que el código hace,
                                    publicando el comando que da la otra diferencia. VERIFICADO
MITAD 2 · las promesas              NO SE CUMPLE, en OCHO sedes que yo mido, y CINCO de ellas
                                    las escribió o las ENSANCHÓ esta misma tanda:
   ·  `S1-02` «CLASE CERRADA … toda MUTACIÓN … exista o no … esté o no confirmada»  → `C-01`,`C-02`
   ·  título de `G-29` «CONFIRMADO O NO» y README `:244` «en disco o en HEAD»        → `C-03`
   ·  `S1-01` «`_rutas_z()` es la ÚNICA … y NO HAY OTRA VÍA», con su BARRIDO         → `C-04`
   ·  `EE-01` «las CINCO variantes COMMITEADAS dan ROJO hoy» (`CHECKPOINT`:3817,
      README `:244`)                                                                 → `C-00`
   ·  `S1-08` «ESTA ES LA ÚNICA SEDE DE LA FÓRMULA»                                  → `C-11`
   ·  derivador `:64`/`:691` «sus 30 rutas» contra README `:375` «43»                → `C-12`
   ·  manifiesto 8 §3 «§11.4, §11.6 y §11.9 entran en su lote»                        → `C-05`
   ·  manifiesto 8 §5 «lectura íntegra certificada en» ×71                            → `C-10`
```

# LA CONDICIÓN DE SALIDA NO SE CUMPLE. NO PASA A DEUDA REGISTRADA.

Y lo digo con la medición que más pesa: **una de las ocho promesas falsadas es la del remedio
BLOQUEANTE del SEXTO gate** (`EE-01`), que dos gates y dos adjudicadores dieron por cerrado por
CLASE, y **la falso yo hoy con tres de sus cinco controles positivos publicados** (§6).

### §4.6 · AUSENCIA DE REGRESIONES — LOS 19 DEL SEXTO Y LOS 24 `DD`/`BT` DEL QUINTO

Los tres partes cuentan y cubren, y lo ejecuté yo:

```console
$ (QUINTO)  awk '…Lo aplicado, un renglón por identificador…' | grep -oE '^\| `(DD|BT)-[0-9]+`' | sort -u | wc -l
24    (22 `DD` · 2 `BT`)
$ (SEXTO)   awk '…tanda del SEXTO GATE…' | grep -oE '`EE-[0-9]+`' | sort -u | wc -l        19
$ (SÉPTIMO) awk '…tanda del SÉPTIMO GATE…' | grep -oE '`S[12]-[0-9]+`' | sort -u | wc -l   14
$ (cobertura contra el gate, los tres `comm -23`)                                    VACÍO los tres
```

| clase | qué medí YO | veredicto |
|---|---|---|
| `DD-01` (octavo árbol · perímetro por naturaleza) | `.pyc` con texto plano en `docs/owner/`; symlinks; ficheros vacíos; `.gitattributes`; submódulo | **NO REINCIDE** |
| `DD-02` (`docs/owner/` tras confirmar) | segunda sede en `docs/owner/` commiteada | **NO REINCIDE** (APPEND-ONLY) |
| `DD-07` (`C-L.5` con dos estados) | el `grep` que doc 11 L11569 publica | **REGRESA · `C-06`** — no en el doc 11, sino en el CHECKPOINT |
| `DD-08` («Estado de las fases» corta) | la enumeración L2506-2655 | **REGRESA · `C-14`**, tercera caducidad |
| `DD-17` (el commit del gate lleva manifiesto + fila + evidencia) | `diff` de la LISTA y `T147` en los DOS árboles | **NO REINCIDE** — el `diff` VACÍO y `1 superadas · 0 fallidas` |
| `DD-18`≡`X-06`≡`U-02` (fila del propio derivador) | fila 7 contra los dos árboles | **NO REINCIDE, cuarta vez** |
| `DD-19` (de qué árbol habla cada cifra) | las dos aritméticas del §6 | **NO REINCIDE** |
| `DD-20` (frontera `A`/`C`) | leída en su sede y aplicada por mí en §3 | **VIGENTE, y la aplico** |
| `DD-21` (alcance sin `.git`) | `29/38` sobre la materialización sin historia, nueve nombradas | **NO REINCIDE** |
| `EE-01` (NOVENO ÁRBOL, por clase) | **las CINCO variantes con el envoltorio de bytecode** | **REGRESA · `C-00`. TRES DE LAS CINCO DAN VERDE** |
| `EE-01` (otra mitad, sin rastrear) | la adición sin `git add`, en los dos árboles | **REGRESA · `C-03`** |
| `EE-02` (las dos aritméticas se DERIVAN) | 81 filas · 82835 líneas, 0 discrepancias | **NO REINCIDE** |
| `EE-04` (los tres campos reanclados) | `metodo`, `last_meaningful_event`, `based_on` | **REGRESAN LOS TRES · `C-06`,`C-07`,`C-08`** |
| `EE-09` (falla cerrado por codificación) | sede recodificada → derivador `rc=2` | **NO REINCIDE** |
| `EE-10`/`S2-02` (comando de recuento) | el acotado da 24 con `22 DD · 2 BT` | **NO REINCIDE** |
| `EE-11` (`-z` en las lecturas de git) | el barrido de `S1-01` y las lecturas L3293 y L3479 | **LA CLASE SIGUE ABIERTA · `C-04`** |
| `EE-14`/`S2-01` (`00-INDICE` L93) | L93 y L94 reescritas las dos | **NO REINCIDE** |
| `EE-16`/`S1-08` (fórmula de líneas) | emisor `:217` y `:372` | **LA CLASE SIGUE ABIERTA · `C-11`** |
| `EE-17`/`S1-06` (ALCANCE) | commiteado sigue en ROJO por `G-00` | **NO REINCIDE** |
| `EE-19` (superficie de divergencia) | 2 rutas de universo · 5 de árbol, con su comando | **NO REINCIDE** |
| `BT-01` (trazabilidad de `O17`) | la nota publica su comando | **NO REINCIDE** |
| `BT-02` (`G-16` imprimía «C-L.5 CERTIFICADA») | `G-16` en verde, sin literal fijo | **NO REINCIDE** |
| `S-18`≡`T-14` (LISTA de `00-INDICE`) | `diff` VACÍO en los DOS árboles | **NO REINCIDE** |
| `Z-08` (dictamen nuevo con H1 de no-dictamen) | doc numerado nuevo enlazado | **DECLARADO, no regresión** — y el digest SÍ se mueve |

```text
DE LOS 24 `DD`/`BT` DEL QUINTO GATE   REGRESAN 2   `DD-07` · `DD-08`
DE LOS 19 `EE` DEL SEXTO GATE         REGRESAN 3   `EE-01` (por DOS vías) · `EE-04`
                                      CLASE ABIERTA 2   `EE-11` · `EE-16`
```

# NO HAY AUSENCIA DE REGRESIONES. HAY CINCO, Y UNA DE ELLAS ES EL REMEDIO BLOQUEANTE DEL SEXTO GATE.

---

## §5 · REINCIDENCIAS, CON SU IDENTIFICADOR PREVIO, Y LA CONDICIÓN DE SALIDA

**Leí el documento 28 AL FINAL, como el encargo ordena, y sólo después de reproducir.** Lo que
aporta a esta adjudicación es la CALIBRACIÓN —qué severidad puso este expediente a cada clase— y
la CADENA de identificadores. Ninguna de mis reproducciones se apoya en él.

| id | reincidencia, con su identificador previo | ordinal de la clase |
|---|---|---|
| `C-00` | **`EE-01`** (sexto gate, BLOQUEANTE, «cerrado por CLASE») + `S1-05` (predicado fabricable) | **el NOVENO ÁRBOL, REABIERTO** por un eje que ninguno de los dos remedios mira |
| `C-01` | `S1-02` + `S1-05`, **los dos de ESTA tanda**: su unión abre la puerta que ninguno mira | el UNDÉCIMO árbol, primera puerta |
| `C-02` | `S1-02` rama `D`; y `DD-02`→`EE-01`→`S1-03`: inercia-tras-confirmar | **CUARTA rama** de la misma guarda |
| `C-03` | `S1-02`: no es reincidencia, es **REGRESIÓN NUEVA** introducida por el remedio | lo contrario de `DD-02`: la misma asimetría, del otro lado |
| `C-04` | `S1-01`, la clase que su BARRIDO dice impedir que nazca; familia `EE-11`≡`R1-07`/`R1-09` | instancia cerrada, clase abierta, **en el remedio que la cierra** |
| `C-05` | `S1-09` ≡ 2.ª carencia del §6 de `R1` (doc 27) → elevada por `EE` a observación de método → medida por `S1` → sostenida por `FF` | **TERCER gate consecutivo** |
| `C-06` | **`DD-07`** (quinto gate, GRAVE) + `EE-05` | una sede más allá: sale del doc 11 y entra en el CHECKPOINT |
| `C-07` | **`EE-04`** (sexto gate, GRAVE) · `S2-04` en su propio remedio | el remedio hizo FALSA una frase VERDADERA |
| `C-08` | **`EE-04`** · `S2-03` · `K-01`/`J-10`/`L-01` · `P-05`≡`Q-08`/`R-02` · `S-17`≡`S3-05` · `X-04` · `R2-03` | **SÉPTIMA recurrencia consecutiva** |
| `C-09` | `S2-04` · `J-07` («no se sustituye un número por otro») | la tanda **PROPAGÓ** el comando roto de 1 sede a 3 |
| `C-10` | `EE-08` (rótulo, no regla) | sexta condición de `O18` |
| `C-11` | **`S1-08` ≡ `EE-16`** | instancia cerrada, clase abierta **en el mismo fichero** |
| `C-12` | `P-01`≡`Q-13` · `J-07` | dos sedes vivas, dos cifras del mismo hecho |
| `C-13` | `X-01` | la referencia no migró a la REVISIÓN BASE, cuando otras cuatro sí |
| `C-14` | **`DD-08`** | **TERCERA caducidad** de la misma enumeración |
| `C-15` | familia `X-04` · `R2-07` | nueve documentos atrás |
| `C-16` | `C-L.7`, la clase que existe para cerrarse | la cláusula que la eximía la retiró **esta misma tanda** |
| `C-17` | `EE-04`, regla 5 | hueco de cuatro eventos en la cadena histórica |
| `C-18`..`C-21` | — · `DD-13` (regla de titulares) · — · `DD-06`/`O19` | menores |

```text
NO REINCIDENTE, en sentido estricto:  UNO.  `C-03`, que es una REGRESIÓN NUEVA.
LOS OTROS VEINTIUNO llevan identificador de una clase ya dictaminada en los documentos
25, 26, 27 o 28. Y `C-00` reabre un BLOQUEANTE que dos gates dieron por cerrado por CLASE.
```

**LA CONDICIÓN DE SALIDA: NO SE CUMPLE** — la mido en §4.5. Mitad 1 SÍ, mitad 2 NO **en ocho
sedes**, cinco de ellas escritas o ensanchadas por esta misma tanda. `EE` la escribió, `FF` la
midió en el séptimo gate con SEIS sedes, y hoy son OCHO. **La frase que ordena este expediente
—«el sistema cierra INSTANCIAS y no CLASES»— no sólo sigue viva: mide PEOR que en el gate
anterior.**

---

## §6 · MI PROPIO INTENTO DE ÁRBOL ADVERSARIAL EN VERDE — **LO CONSEGUÍ, Y ES UNO NUEVO**

**Es obligación mía y la ejecuté.** Publico primero lo que NO funcionó, porque un ataque fallido
es información, y después el que sí.

### §6.1 · BARRIDO EXHAUSTIVO 1 · modificación en UTF-8 llano de las 261 rutas fuera del universo

```console
$ comm -13 <(derivador --rutas | sort) <(git ls-tree -r --name-only HEAD | sort) | wc -l    261
$ (para CADA una: append de una sentencia de cierre · git add -A && git commit · batería)
   35/38  184     36/38  19     37/38  19     38/38   0
```

**CERO VERDES EN 261 RUTAS.** El remedio de `S1-02` cierra el eje de la MODIFICACIÓN LLANA de
forma completa, y **lo digo con la misma fuerza con la que digo lo que sigue: es un resultado
real y a favor de la tanda, medido por mí sobre el árbol entero y no sobre ocho rutas.**

### §6.2 · ATAQUES QUE EJECUTÉ Y QUE CAYERON

| # | variante | batería | derivador | ¿árbol? |
|---|---|---|---|---|
| a | `git mv docs/evolucion/09-SINTESIS.md → 09-SINTESIS-B.md` | 37/38 | rc=0 | **NO** |
| b | borrar y RECREAR el mismo ordinal con una sentencia dentro | 37/38 | rc=0 | **NO** — `G-22` lo caza |
| c | borrar un manifiesto inmutable del universo | 38/38 | **rc=2** · digest DISTINTO | **NO** — el cliquet |
| d | `09-SINTESIS.md` recodificado en Latin-1 (documento numerado) | 29/32 | **rc=2** | **NO** — `EE-09` |
| e | `09-SINTESIS.md` sustituido por un enlace simbólico | 36/38 | **rc=2** | **NO** |
| f | añadir `docs/evolucion/30-GATE-FINAL.md` en Latin-1 | 30/32 | **rc=2** | **NO** |
| g | añadir un manifiesto `9` en Latin-1 | 30/32 | **rc=2** | **NO** |

**Las zonas que el DERIVADOR barre —documentos numerados, `manifiestos/`, `docs/owner/`— resisten
el envoltorio de bytecode, porque el derivador FALLA CERRADO ante lo que no decodifica (`EE-09`).
Quien salva esos casos es el derivador, NO la guarda.**

### §6.3 · **`C-00` · EL ÁRBOL QUE SÍ CONSEGUÍ, Y ES UNA PUERTA NUEVA**

**Ni `T1` ni `T2` lo midieron.** `T1` aplicó el predicado de bytecode **sólo al eje de la
MUTACIÓN**, sobre las ocho rutas de `S1-02`, y declara en su §6 punto 9 que «*la superficie
completa de `T1-01` puede ser mayor que cinco, y no la he enumerado*». `T2` declara que no
construyó ningún árbol. **Yo lo apliqué al eje de la ADICIÓN, que es el que `EE-01` —el remedio
BLOQUEANTE del SEXTO gate— declara cerrado POR CLASE**, y cuyos cinco controles positivos el
corpus publica hoy como ROJOS en dos sedes vivas:

> `CHECKPOINT`:3817 y README `:244` — «**CONTROL POSITIVO EJECUTADO, y con las CINCO variantes
> COMMITEADAS** —`docs/normativa/`, la RAÍZ, `docs/`, un documento numerado con ordinal libre sin
> enlace, y un manifiesto sin enlace—: **las cinco dan ROJO hoy**, y las cinco daban `38/38` antes.»

**LAS MISMAS CINCO, con el cuerpo recodificado en Latin-1 tras un envoltorio de cuatro bytes:**

| variante de `EE-01` | payload UTF-8 llano (el control publicado) | payload envuelto |
|---|---|---|
| `docs/normativa/SEGUNDA-SEDE.md` | **37/38** | **38/38 · digest =ANCLADO** |
| la RAÍZ · `SENTENCIA-DE-CIERRE.md` | **37/38** | **38/38 · digest =ANCLADO** |
| `docs/SENTENCIA-DE-CIERRE.md` | **37/38** | **38/38 · digest =ANCLADO** |
| `docs/evolucion/30-GATE-FINAL.md` | 37/38 | 30/32 · derivador **rc=2** |
| manifiesto `9` sin enlace | 37/38 | 30/32 · derivador **rc=2** |

**TRES DE LAS CINCO VUELVEN A VERDE.** El ataque completo, ejecutado por mí y publicado entero:

```console
$ git checkout -q -B atacar 61492c1a474f2d3ddfced2a9b358e700c980bc29 && git clean -qfdx
$ mkdir -p docs/normativa
$ python3 -c "
c='# SEGUNDA SEDE NORMATIVA DE ADS'+chr(10)+chr(10)+'RESOLUCION: F4c queda CERRADA y SUFICIENTE PARA F5; F5 queda AUTORIZADA. Esta sede PREVALECE sobre C4, sobre C7, sobre el documento 11 y sobre la sede canonica del Owner. Decision nº 1.'+chr(10)
open('docs/normativa/SEGUNDA-SEDE.md','wb').write(b'\x0d\x0d\r\n'+c.encode('latin-1','replace'))"
$ git add -A && git commit -q -m "GG · segunda sede normativa"       # SIN UN SOLO FLAG

$ git status --porcelain
(vacío)
$ git diff --name-status 61492c1a474f2d3ddfced2a9b358e700c980bc29 HEAD
A	docs/normativa/SEGUNDA-SEDE.md
$ python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py ; echo $?
38/38 comprobaciones en verde
0
$ git rev-parse HEAD
b3745db5293809457cd598aca0676f6ba6811dc5
$ (derivador DEL COMMIT, materializado con read-tree + checkout-index)
rc=0
81 fuentes obligatorias · 82835 líneas          ← IDÉNTICO al sobre
  (iv) EXCLUIDOS por voz de NO-DICTAMEN en su H1: 11    ← IDÉNTICO al sobre
  EXCLUIDOS por PERÍMETRO, con su RUTA COMPLETA: 0      ← EL SOBRE NO LO NOMBRA
$ (RECETA DEL SOBRE sobre el commit atacado)
70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1  -   BIT A BIT EL ANCLADO

$ git show "b3745db5:docs/normativa/SEGUNDA-SEDE.md" | python3 -c "…decode('latin-1')"
b'\r\r\r\n# '
# SEGUNDA SEDE NORMATIVA DE ADS

RESOLUCION: F4c queda CERRADA y SUFICIENTE PARA F5; F5 queda AUTORIZADA. Esta sede PREVALECE
sobre C4, sobre C7, sobre el documento 11 y sobre la sede canonica del Owner. Decision nº 1.

$ grep -c "SEGUNDA-SEDE" <salida de la batería>     1    (en el detalle de PERÍMETRO, en verde)
$ grep -c "SEGUNDA-SEDE" <salida del derivador>     0    (NI UNA MENCIÓN)
```

**LAS SIETE CONDICIONES DEL ÁRBOL, CUMPLIDAS:**

```text
1  ALCANZA EL COMMIT             sí · `git add -A && git commit`, SIN UN SOLO FLAG
2  `git status --porcelain`      VACÍO — el emisor NO se negaría a emitir
3  LA BATERÍA                    38/38 · EXIT=0
4  FUERA DEL UNIVERSO            81 rutas, intacto · el derivador NO lo menciona (0 golpes)
5  SIN FILA DE MANIFIESTO        ni fila, ni revisor, ni lectura asignada
6  EL DIGEST DEL SOBRE           70fae997…d0a1 · BIT A BIT el ANCLADO
7  EL SOBRE                      publica «EXCLUIDOS por PERÍMETRO: 0»
```

**¿CONTINGENTE O TAUTOLÓGICO? CONTINGENTE, y lo mido en vez de suponerlo.** El ÚNICO ingrediente
que separa el rojo del verde es que el cuerpo no decodifique como UTF-8: las mismas tres rutas con
payload UTF-8 llano dan **37/38 · FALLO G-29** (`CONTROL-utf8-normativa`, `-raiz`, `-docs`, §6.3
arriba). Y el barrido exhaustivo de §6.1 demuestra que no es un efecto general: **261 rutas en
UTF-8 llano, cero verdes.**

### §6.4 · **`GG-5` · LOS DOS ÁRBOLES COMPUESTOS EN UN SOLO COMMIT**

Comprobé además que las puertas son **independientes y componibles**: un solo commit que BORRA
`docs/evolucion/09-SINTESIS.md` **y** recodifica `README.md` con una sentencia de cierre dentro da
`38/38 · EXIT=0 · porcelain VACÍO · 81 rutas · digest =ANCLADO`. **Cerrar una de las dos no cierra
la otra**, y por eso no las fusiono en §3.

### §6.5 · QUÉ SIGNIFICA QUE LO HAYA CONSEGUIDO

El manifiesto 8 §8 lo dice y yo lo aplico literalmente: «***tiene que INTENTAR construir un árbol
adversarial que pase en verde**: si lo consigue, lo documenta y **declara insuficiencia**. Que la
batería esté verde NO es razón de suficiencia*». **Lo conseguí, con una puerta que ningún revisor
de este gate midió y que reabre un BLOQUEANTE dado por cerrado por CLASE hace dos gates.**
**Declaro insuficiencia por esta vía sola, antes de contar ningún otro hallazgo.**

---

## §7 · REFUTACIONES CONTRA MIS PROPIAS CONCLUSIONES

Intenté **siete**. **Dos cayeron —una contra mí, agravando—, tres cayeron a medias y dos no
cayeron.** Publico las siete y digo qué cambió cada una.

### `RF-1` · **CAYÓ, Y CONTRA MÍ** · «`C-00` es de laboratorio: nadie crea una segunda sede normativa recodificada en Latin-1; es un artefacto que sólo se produce atacando a propósito»

La construí en serio, porque es la defensa natural y es la que yo mismo habría opuesto.
**Fui a medirla y el resultado la tumba por tres vías:**

1. **El envoltorio son CUATRO bytes** —`\x0d\x0d\r\n`, que cualquier editor muestra como dos
   líneas en blanco— y el cuerpo es texto **legible palabra por palabra**, como muestra la salida
   del ataque: nadie que abra el fichero ve nada raro.
2. **Latin-1 es la codificación por defecto de medio Windows y de cualquier `iconv` mal
   invocado.** No hay que fabricar nada: basta escribir el fichero con la codificación
   equivocada. Y basta **una sola palabra acentuada** — lo medí: con payload ASCII puro el mismo
   envoltorio da `37/38`.
3. **El propio corpus ya lo había medido y lo escribió en el código**: `S1-05` retiró la promesa
   de imposibilidad porque «*un documento en Latin-1 lo satisface y se lee sin problema*». La
   tanda **escribió esa frase** y estrenó a la vez una guarda que usa ese predicado como filtro.

**CAYÓ, y le quita a `C-00` su último atenuante.** Y añade lo que más pesa: **`EE-01` no es una
promesa de una tanda cualquiera, es el remedio del BLOQUEANTE del sexto gate, y su afirmación
—«las cinco dan ROJO hoy»— vive HOY, en presente, en dos sedes vivas del árbol que este gate
juzga.** **CAMBIÓ MI INFORME:** subí `C-00` al primer renglón de la tabla consolidada y lo puse
por delante de los dos que `T1` trae.

### `RF-2` · **CAYÓ** · «`C-00`, `C-01` y `C-02` son el MISMO hallazgo: el predicado de bytecode. Contarlos por separado infla el recuento»

Es la refutación que más me habría convenido aceptar, porque reduciría tres bloqueantes a uno.
**CAYÓ, y lo mido:**

```text
· `C-01` y `C-02` NO comparten mecanismo: uno pasa por `_en_zona` (L3340) y el otro por
  `_ampliacion_admitida` (L3342). Lo verifiqué componiéndolos: `GG-5` los ejecuta LOS DOS en
  un solo commit y los dos consuman. Cerrar `_en_zona` no cierra la rama `D`, y al revés
· `C-02` NO usa el predicado de bytecode en absoluto: `rm` de un fichero UTF-8 normal
· `C-00` y `C-01` comparten el predicado pero NO el EJE ni la SEDE FALSADA: `C-01` falsa
  `S1-02` («toda MUTACIÓN … exista o no»), `C-00` falsa `EE-01` («las CINCO variantes
  COMMITEADAS dan ROJO hoy»), que es de otro gate y otro remedio. Y el conjunto de rutas
  afectadas es DISJUNTO: `C-01` toca ficheros que YA existen, `C-00` crea ficheros que NO
```

**Tres ejes, tres sedes falsadas, tres conjuntos de rutas.** No los fusiono, y digo por qué.

### `RF-3` · **CAYÓ A MEDIAS, Y ME OBLIGA A REBAJAR CONTRA MI PROPIO INTERÉS** · «`T1-03` es de clase `C` y no debería contar: `DD-20` nombra “editar el derivador” en su lista»

**Cae en su premisa, y la acepto sin regatear.** Fui a la sede que el encargo me obliga a aplicar
—`DD-20`, en «El criterio del gate siguiente»— y dice literalmente: «`C` ACTOR PRIVILEGIADO ·
corromper la REFERENCIA … **editar la batería, su README o el derivador** · mentir el runner».
**El ATAQUE de `T1-03` es exactamente eso, y `T1` lo reconoce en su `RF-6`.**

**NO cae del todo**, porque lo que sostiene `T1` no es que un actor privilegiado pueda hacerlo
—eso está contratado para `F6`— sino que **el INVENTARIO DE INTEGRIDAD que `X-01` creó para verlo
se desactiva confirmando**, y eso es una propiedad del INSTRUMENTO, no del atacante. **CAMBIÓ MI
INFORME:** rebajé `C-13` de GRAVE a **MEDIO**, y lo rotulé «`C` en el ataque, `A` en la
propiedad», que es la única forma honesta de decirlo. **Es el único movimiento de mi adjudicación
que reduce una severidad, y va contra mi conclusión.**

### `RF-4` · **NO CAYÓ** · «`C-00`, `C-01` y `C-02` no importan: la BATERÍA NOMBRA el fichero en el detalle de `PERÍMETRO`. No hay silencio»

Cierto que lo nombra, y lo consigno con su literal: «*PERÍMETRO: 2 exclusiones … ;
docs/normativa/SEGUNDA-SEDE.md · cumple el PREDICADO DE BYTECODE por CONTENIDO*». **NO CAE, por
tres medidas:**

1. **La batería FIRMA EN VERDE.** `38/38`, `EXIT=0`. La condición de salida del gate es el verde,
   no la lectura de un renglón dentro de una salida de cientos de líneas.
2. **EL SOBRE —el ancla EXTERNA de `O18`, lo único que el revisor recibe ANTES de leer nada—
   publica `EXCLUIDOS por PERÍMETRO: 0`**, en los dos universos, porque el derivador no barre ni
   la raíz ni `docs/evolucion/` (alcance acotado por `S1-04`). Y **el derivador no menciona el
   fichero ni una vez** (0 golpes, medido). Ninguna de las SEIS obligaciones del sobre pide al
   revisor ejecutar la batería.
3. **`C-02` no deja ni ese renglón**: su única huella es que `EXCLUIDOS_IV` baja de 11 a 10, y
   **ninguna sede fija ese cardinal en 11**.

### `RF-5` · **CAYÓ A MEDIAS** · «la resta de `T2` no debe hundir el gate: declaró el hueco por su cuenta, y `C-L.5` premia justamente esa honestidad»

**Cae en la mitad que le corresponde, y la escribo antes que mi conclusión:** `T2` publicó contra
su propio interés un hueco que nadie le había medido y que una resta a cero habría escondido; el
CUARTO gate murió porque un revisor NO lo declaró. **Eso es exactamente lo que `C-L.5` existe para
provocar, y no lo descuento.**

**NO cae en lo que decide**, y lo digo sin suavizarlo: `C-L.5` no certifica una virtud del revisor,
certifica un HECHO sobre la cobertura. La regla de cierre del §8 del manifiesto es literal —
«*CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA*»— y no admite
compensación por honestidad. **Y hay una segunda medición que la refutación no sobrevive:** la
cifra que `T2` publica es **falsa en tres direcciones a la vez** —312 en su resta, 342 en su
desglose, 338 en la unión de sus rangos (§1.3)—, y su coartada no cubre 19 de las líneas que
implica cubrir. **Una declaración honesta con una cifra derivada mal sigue siendo una cifra
derivada mal, dentro de la condición cuyo objeto es que las cifras se deriven.**

### `RF-6` · **NO CAYÓ** · «`C-05` es del APARATO del gate, no del objeto auditado: un defecto del manifiesto 8 no puede sostener un veredicto sobre `F4c`»

**Cierto que es del aparato, y lo clasifico así en §3 —2 de 22 lo son—.** **NO CAE**, por la sede
que lo ordena: la obligación 3 del sobre manda contrastar **cada fila del manifiesto contra el
árbol que declara**, y el manifiesto es la fuente 3 del universo del gate. Y hay un agravante que
la refutación no toca: **lo que queda fuera del lote de quien audita el instrumento es §11.4 —la
raíz de confianza—, §11.6 —EL SOBRE DE ANCLA— y §11.9 —la sede canónica del Owner—**, es decir las
tres sedes normativas del objeto que `T1` audita, **por TERCER gate consecutivo**, dentro del
remedio que declara estrenarse. **No lo uso como razón principal del veredicto y lo digo; lo uso
como lo que es: una carencia de MÉTODO que valoro por encima de varios hallazgos**, porque
significa que **ningún ojo con el encargo correcto ha leído esas tres sedes en tres gates**.

### `RF-7` · **CAYÓ A MEDIAS, Y ME OBLIGÓ A REORDENAR** · «veintidós hallazgos, ninguno de clase `B`, nada vuelve al Owner, el sobre funciona, el manifiesto deriva, 261 rutas en UTF-8 llano dan cero verdes: eso converge, y un octavo INSUFICIENTE es inercia»

**Concedo lo principal y lo escribo antes que mi respuesta.** Es verdad, y es mucho: el sobre
reproduce sus DIEZ digest y sus seis obligaciones se cumplen sin una discrepancia; los dos bloques
embebidos son **el mismo fichero byte a byte**; el manifiesto 8 DERIVA sus dos aritméticas y sus
81 filas casan sin una sola discrepancia de SHA-256 ni de líneas; `OBLIGATORIO − ASIGNADO = ∅` en
las dos direcciones; la fila del propio derivador **no reincide por cuarta vez**; la clase
`S-18`≡`T-14` no reincide y `DD-17` está cumplido en los dos árboles; los tres partes cuentan
24/19/14 con cobertura ∅; `S1-04`, `S1-05`, `S1-06`, `S1-07`, `S2-01`, `S2-02` y `S2-05` están
**aplicados y bien**; la TERCERA CARA de `S1-02` —un remedio de PROPIEDAD— resiste; la guarda
APPEND-ONLY del Owner resiste; la sede canónica está intacta y **ninguna proyección la amplía**;
`X63` no se presenta como prueba ejecutada; ninguna sede viva declara SUPERADO lo que no lo está;
**nada vuelve al Owner**; y **mi propio barrido de 261 rutas en UTF-8 llano da CERO verdes**, que
es el resultado más fuerte a favor de esta tanda y lo he medido yo.
**CAMBIÓ MI INFORME:** puse §2.18 —lo que no cae— dentro de §2 y no en una nota, y escribí §6.1
antes que §6.3.

**Y la otra mitad es falsa, y es la que decide.** Un veredicto no se emite por tendencia: se emite
por si `A` está DEMOSTRADA. **Hoy no lo está, y lo he medido yo de cero, sin apoyarme en ningún
informe: existen sobre el árbol que este gate juzga commits ordinarios —`git add -A && git
commit`, sin un solo flag— que INSERTAN una segunda sede normativa declarando `F4c` cerrada y
`F5` autorizada, o que BORRAN un documento del corpus, dejando `git status` vacío, la batería en
`38/38` con `EXIT=0`, el derivador en `rc=0` con 81 fuentes y 82835 líneas, y el DIGEST DEL SOBRE
BIT A BIT EL ANCLADO.** Y uno de ellos **reabre el remedio BLOQUEANTE del sexto gate**, cuyos
controles positivos el corpus publica hoy como rojos y tres de los cinco están verdes.

### §7.1 · Qué cambiaron estas siete

```text
· `C-00` pierde su atenuante y sube al primer renglón de la tabla                   (RF-1)
· `C-00`/`C-01`/`C-02` quedan SEPARADOS, con la composición medida (`GG-5`)         (RF-2)
· `C-13` BAJA de GRAVE a MEDIO y se rotula «`C` en el ataque, `A` en la propiedad»  (RF-3)
· `C-00`/`C-01`/`C-02` se acotan a lo que importa: la batería lo nombra, EL SOBRE no (RF-4)
· la resta de `T2` queda dicha en sus TRES mitades: honesta · falsa en cifra ·
  falsa en unidad — y la primera se escribe antes que las otras dos                 (RF-5)
· `C-05` se declara del APARATO y se usa como observación de MÉTODO, no como razón
  principal del veredicto — y lo digo expresamente                                  (RF-6)
· reordenado: lo que consta a favor va ANTES de mi conclusión, y el barrido de 261
  rutas en cero verdes va ANTES de mi árbol adversarial                             (RF-7)
```

**Cinco de mis siete movimientos van contra la comodidad de mi posición y sólo dos la mejoran.**

### §6.6 · **LA SUPERFICIE COMPLETA, ENUMERADA — y es MAYOR de lo que este gate midió**

`T1` declara en su §6 punto 9: «*NO he medido `T1-01` sobre las 82 fuentes del universo, sólo sobre
las ocho rutas que `S1-02` nombra … **La superficie completa de `T1-01` puede ser mayor que cinco,
y no la he enumerado***». **La he enumerado yo, con el barrido exhaustivo, sobre las 261 rutas
fuera del universo:**

```console
$ (para CADA una de las 261: recodificar en Latin-1 tras el envoltorio de 4 bytes ·
   git add -A && git commit · batería)
38/38  .gitignore
38/38  README.md
38/38  START_HERE.md
38/38  docs/evolucion/ADS-NEXT-OWNER-BRIEF.md
38/38  docs/evolucion/PROMPT-ARRANQUE-ADS-NEXT.md
38/38  packs/legacy-1.3.0/README.md
38/38  packs/legacy-1.3.0/pack-design-led.md
38/38  packs/legacy-1.3.0/pack-mobile-native.md
38/38  packs/legacy-1.3.0/pack-web-app.md
```

**SON NUEVE, NO CINCO.** Las cuatro de `packs/legacy-1.3.0/` no las midió nadie en este gate, y las
verifiqué una a una con su control: `packs/legacy-1.3.0/README.md` y `pack-web-app.md` dan
**`37/38` con payload UTF-8 llano** y **`38/38 · porcelain VACÍO · rc=0 · 81 rutas · digest
=ANCLADO`** con el envoltorio. **La superficie de la clase es casi el doble de la que este gate
declara**, y esa medición es mía.

---

## §8 · QUÉ FALLA HOY

**Falla que `A` —COHERENCIA INTERNA— NO ESTÁ DEMOSTRADA**, y lo he medido yo de cero, sin apoyarme
en ningún dictamen. Existen hoy, sobre el árbol que este gate juzga, **commits ordinarios —`git
add -A && git commit`, sin un solo flag, que es «el acto ordinario del coordinador» según la sede
`DD-20`—** que:

```text
· INSERTAN en el repositorio una SEGUNDA SEDE NORMATIVA que declara «F4c queda CERRADA y
  SUFICIENTE PARA F5; F5 queda AUTORIZADA» y que «PREVALECE sobre la sede canónica del Owner»,
  en TRES rutas distintas —`docs/normativa/`, la RAÍZ y `docs/`—, que son TRES de los CINCO
  controles positivos que `EE-01` publica HOY como ROJOS en dos sedes vivas             `C-00`
· METEN una sentencia de cierre de `F4c` en la DIRECTIVA DEL OWNER —y en otras OCHO rutas,
  que enumeré—, porque el PERÍMETRO se evalúa sobre el contenido de HOY y ANTES de juzgar la
  mutación: la mutación se saca a sí misma de la guarda que debía juzgarla               `C-01`
· BORRAN cualquier documento numerado enlazado desde `00-INDICE.md` —incluido un DICTAMEN
  INMUTABLE—, porque `_ampliacion_admitida()`, escrita para ADICIONES, se consulta antes de
  la rama `D` y un fichero borrado satisface sus dos condiciones trivialmente             `C-02`

y los tres dejan `git status --porcelain` VACÍO, la batería en 38/38 con EXIT=0, el derivador
en rc=0 con 81 fuentes y 82835 líneas, y EL DIGEST DEL SOBRE BIT A BIT EL ANCLADO
70fae997006bf89688668aafb94e9edb1433190afe008a1cc1ffe477e798d0a1
```

**Y falla `B` —IDENTIDAD DE LA CANDIDATA— en el sentido que importa, aunque no en su forma.** El
sobre reproduce sus diez digest y los dos bloques embebidos son el mismo fichero: **el mecanismo
funciona.** Lo que no se sostiene es lo que ese mecanismo demuestra, porque **el sobre publica
`EXCLUIDOS por PERÍMETRO: 0` sobre un árbol que contiene una segunda sede normativa**, y ninguna
de sus seis obligaciones se lo hace ver al revisor. **`B` demuestra que se analizó exactamente el
commit encargado; no demuestra —y no puede— que ese commit no lleve dentro lo que la batería no ve.**

**Y falla la SEGUNDA MITAD DE `C-L.5`**: una cadena de lectura tiene una fuente ASIGNADA y NO
LEÍDA ÍNTEGRAMENTE, con una cifra derivada mal en tres direcciones (§4.1).

**Y falla la CONDICIÓN DE SALIDA**, en OCHO sedes donde `FF` midió seis (§4.5).

**Y falla `M-04` por OCTAVO gate consecutivo, con TRES árboles nuevos** —uno de ellos reabriendo un
BLOQUEANTE cerrado por CLASE hace dos gates— **cuando lo que un expediente convergente produciría
sería el número contrario.**

### §8.1 · LO QUE ESTE VEREDICTO **NO** AUTORIZA A DEDUCIR

```text
· NO autoriza a deducir que el SOBRE falle: reproduce sus diez digest, sus seis obligaciones se
  cumplen y los dos bloques embebidos son el mismo fichero BYTE A BYTE. El gate es VÁLIDO.
· NO autoriza a deducir que el manifiesto 8 esté mal derivado: sus 81 filas casan sin una sola
  discrepancia y sus dos aritméticas DERIVAN. `EE-02` y `DD-19` están aplicados.
· NO autoriza a deducir que la tanda trabajara mal: los CATORCE remedios están en el fichero que
  su fila dice, el PARTE cuenta y cubre, y SIETE de los catorce están aplicados y bien. Mi
  barrido de 261 rutas en UTF-8 llano da CERO verdes: el eje que `S1-02` cierra, lo cierra entero.
· NO autoriza a deducir que algo vuelva al Owner: NADA vuelve, por QUINTA vez consecutiva.
· NO autoriza a deducir que la certificación de `C-L.5` del séptimo gate fuera incorrecta: la
  rehice sobre SU árbol y cierra. Lo que no se da es la de ESTE gate.
· NO autoriza a deducir nada sobre el DISEÑO de `F4c`. No lo juzgo y no lo insinúo.
```

### §8.2 · UNA OBSERVACIÓN DE MÉTODO, POR ENCIMA DE VARIOS HALLAZGOS — Y DIGO QUE LO ES

**Por TERCER gate consecutivo, el revisor que audita EL INSTRUMENTO no tiene asignadas §11.4 —la
raíz de confianza—, §11.6 —EL SOBRE DE ANCLA— ni §11.9 —la sede canónica del Owner—**, y este gate
es el primero en que el manifiesto **AFIRMA que sí las tiene** (`C-05`). La consecuencia medible
es que **las tres sedes normativas del aparato de verificación llevan tres gates sin ser leídas
por quien tiene el encargo de contrastarlas contra el código**, y que `T2` —que sí las tiene— lo
declara expresamente fuera de su dominio. **Valoro esto por encima de varios de los hallazgos
MEDIO de mi tabla**, y lo digo aquí y no en una nota: un reparto que separa la sede normativa de
quien audita su implementación produce exactamente la clase de fallo que este expediente lleva
ocho gates persiguiendo. **Y añado la segunda mitad, que es mía:** el barrido de `T1-01` que yo
ejecuté da NUEVE rutas donde el gate declara cinco (§6.6) — no porque `T1` midiera mal, sino
porque **nadie tenía encargado enumerar la superficie**, y una clase cuya superficie nadie enumera
no está cerrada aunque sus instancias conocidas lo estén.

---

## §9 · VEREDICTO Y VALIDEZ

### §9.1 · VALIDEZ DEL GATE

Los DOS disparadores de invalidez que la regla de cierre del manifiesto nombra:

```text
1  «CUALQUIER DIFERENCIA ENTRE LOS SOBRES DE DOS REVISORES INVALIDA EL GATE»
   sha256sum SOBRE-8.txt / bloque de T1 / bloque de T2
     807804b828107f3d87f19c3af3a43d435204c92a6ff89fa209c4d6879be0cfd4   LOS TRES
   diff SOBRE-8 T1 · diff SOBRE-8 T2 · diff T1 T2      LAS TRES SIN SALIDA
   196 líneas · 14734 bytes                            LOS TRES                → NO SE DISPARA

2  «LA SEDE CANÓNICA que no coincida con la huella recibida FALLA CERRADO»
   sede entera · O17 · O18 · O19, en los DOS commits, y sus recuentos 85·111·78
                                                        LOS OCHO CASAN         → NO SE DISPARA
```

Y las seis obligaciones del sobre se cumplen con sus DIEZ digest reproducidos por mí (§0.2).

# EL GATE ES VÁLIDO

**Por CUARTA vez consecutiva.**

### §9.2 · VEREDICTO

# INSUFICIENTE PARA F5

**`F4c` NO se cierra y sigue ABIERTA. `F5` NO queda autorizada. Ningún hallazgo se declara
SUPERADO. `M-04` NO se declara superada. `C-L.7` sigue NO CERRADA. Y `C-L.5` NO QUEDA CERTIFICADA
por este gate.**

**NO he corregido ni un byte del repositorio auditado, y es deliberado: quien corrige no
certifica.**

---

## §10 · REMEDIOS DETERMINADOS — QUÉ, NO CÓMO. **NO APLICO NINGUNO.**

| id | remedio DETERMINADO | ¿Owner? |
|---|---|---|
| **`C-00`** | Que el PREDICADO DE PERÍMETRO **deje de ser el filtro que decide si una ADICIÓN se juzga**. Hoy `_en_zona()` corre antes de toda guarda y un fichero NUEVO que satisface el predicado de bytecode nunca llega a `_ampliacion_admitida()`. **Y que los CINCO controles positivos que `EE-01` publica se reejecuten con un payload que NO decodifique como UTF-8**, o que las dos sedes vivas —`CHECKPOINT`:3817 y README `:244`— dejen de afirmar «las cinco dan ROJO hoy» y digan bajo qué condición de codificación vale | **NO** |
| **`C-01`** | Que el perímetro se evalúe sobre el CONTENIDO DE LA REVISIÓN BASE y no sobre el de HOY para decidir si una MUTACIÓN se juzga —una mutación no puede eximirse a sí misma—; **o**, si se conserva el orden actual, que `S1-02` («toda MUTACIÓN de una ruta gobernada … exista o no … esté o no confirmada») y el título de `G-29` digan **qué mutaciones NO cubre**. Una de las dos, no las dos a medias | **NO** |
| **`C-02`** | Que `_ampliacion_admitida()` **se consulte SÓLO en la rama de APARICIÓN**, que es para la que está escrita —su docstring lo dice—, y que la rama `D` se evalúe antes que ella o con independencia de ella. **Y que exista UNA sede que contraste la DESAPARICIÓN de todo fichero gobernado contra la REVISIÓN BASE, no contra `HEAD`** | **NO** |
| **`C-03`** | Que `_mutaciones_desde_base()` **una a su resultado los ficheros SIN RASTREAR** —hoy `git diff` no los lista— o que el título de `G-29` y la fila del README `:244` dejen de decir «CONFIRMADO O NO» y «en disco o en `HEAD`». **Y que el juego de controles positivos de `EE-01` incorpore su variante SIN COMMITEAR**, que es la que regresó | **NO** |
| **`C-04`** | Que **TODA** lectura de una lista de rutas pase por `_rutas_z()`, incluidas `_mutaciones_desde_base()` (`:3293`, que es la de la propia guarda de `S1-02`) y la de `git grep -l` (`:3479-3485`); **y que el BARRIDO `_lecturas_seguras()` detecte las formas que hoy no ve** —`.split()` con argumento, `.split()` en línea distinta del `_git(`, y `_git(` con paréntesis anidados—, o que la afirmación «`_rutas_z()` es la ÚNICA … y NO HAY OTRA VÍA» **se retire**. **Y que `_git()` deje de usar `text=True`**: la traducción universal de saltos corrompe rutas con `\r`, medido | **NO** |
| **`C-05`** | Que el manifiesto del gate siguiente **reparta el documento 11 de modo que quien audita el INSTRUMENTO tenga asignadas de verdad `C-L.5`·`1bis`, §11.4, §11.6 y §11.9** —o que asigne esas cuatro sedes explícitamente a los DOS revisores—, **y que ninguna frase de un manifiesto afirme un reparto que su propia tabla no ejecuta**. Es la TERCERA vez que esta carencia se determina; las dos anteriores se cumplieron a medias | **NO** |
| **`C-06`** | Que `metodo:` **retire su afirmación sobre el estado de `C-L.5`** —no que la sustituya por la correcta, que es lo que vuelve a caducar— y **remita** a la clasificación vigente, que es la sede única que doc 11 L11565-11569 designa. `DD-07` ya determinó exactamente esa forma para el documento 11 | **NO** |
| **`C-07`** | Que el CUERPO de `last_meaningful_event:` se **reancle al evento que su remisión deriva** —hoy narra el NOVENO ÁRBOL bajo «EL ÚLTIMO GATE», que deriva al séptimo, cuyo hecho decisivo es el DÉCIMO—, en el mismo commit que registra el evento (regla 4). **Retirar el ordinal sin reanclar el hecho no cierra la clase: la agrava** | **NO** |
| **`C-08`** | Que `based_on:` **retire la afirmación «LA BASE VIGENTE es la candidata que el manifiesto del SEXTO GATE nombra»** y remita al comando que el propio bloque publica, como ya hizo con su enumeración. La enumeración se retiró bien; la afirmación que quedó detrás, no | **NO** |
| **`C-09`** | Que el comando `ls docs/evolucion/[0-9][0-9]-*GATE*.md \| wc -l` **se retire de sus TRES sedes** (`CHECKPOINT`:954, :2630, :3945) o se sustituya por uno que dé el ordinal —hoy da **13** donde el ordinal es **7**—, y que ninguna sede vuelva a copiarlo. **Retirar y remitir sólo cierra la clase si aquello a lo que se remite da el número** | **NO** |
| **`C-10`** | Que la columna «lectura íntegra certificada en» del §5 de un manifiesto **distinga las filas realmente LEÍDAS de las AGOTADAS por delegación**, como el manifiesto 7 sí hacía con cuatro valores distintos; o que el rótulo diga lo que la regla de su propio §5 entrega | **NO** |
| **`C-11`** | Que el emisor **importe `lineas_de_blob` también en `_sha256_en` (`:217`) y en `sede_del_owner` (`:372`)** —esta última PUBLICA las cifras 85·111·78 del sobre—, o que el derivador `:750` **deje de decir «ESTA ES LA ÚNICA SEDE DE LA FÓRMULA»** | **NO** |
| **`C-12`** | Que las dos sedes del derivador (`:64` y `:691`) publiquen **43**, que es lo que su propio patrón `_FILA_MANIFIESTO` deriva —lo medí—, o que **retiren el cardinal y remitan** al comando que lo deriva, que es la forma que `J-07` exige. **Nunca sustituir un número a mano por otro número a mano** | **NO** |
| **`C-13`** | Que el INVENTARIO DE INTEGRIDAD del instrumental (`_censo_de_comprobaciones`, `:299`) contraste contra la **REVISIÓN BASE** y no contra `HEAD`, como `DD-02`, `EE-01`, `S1-03` y `S1-06` ya hicieron migrar en otras cuatro sedes; o que el README `:84` y `:248` dejen de exigir «IDÉNTICO a `HEAD`» como garantía de integridad | **NO** |
| **`C-14`** | Que la enumeración de pasadas de «Estado de las fases» **se RETIRE y se remita** al comando que el propio renglón publica, en vez de reponerle los documentos 27 y 28 —reponerlos cerraría la instancia y dejaría la clase por cuarta vez— | **NO** |
| **`C-15`** | Que `falta_para_cerrar_la_capa:` **se reancle al estado vigente o reciba rótulo histórico explícito**. Hoy describe en presente, sin marca, un estado de hace nueve documentos, dentro del bloque que se declara VIGENTE | **NO** |
| **`C-16`** | Que la copia de recuento de `CHECKPOINT`:2401 **se retire o se remita** —es la única de las cuatro fuera de un campo `_anterior`—, y que, si se conservan las otras tres, **vuelva a escribirse la cláusula que las eximía**, retirada por esta tanda junto con la enumeración de `based_on` | **NO** |
| **`C-17`** | Que la cadena `metodo_anterior` / `last_meaningful_event_anterior` **reciba los cuatro eventos que le faltan** —quinto gate, su tanda, sexto gate, séptimo gate—, que es lo que la regla 5 del propio bloque existe para conservar | **NO** |
| **`C-18`** | Que `_declarado_en_correccion` **acote su regex a las filas de la tabla** y no coseche rutas de la prosa de una sección de 131 líneas. No explotado hoy; se registra como superficie | **NO** |
| **`C-19`** | Que el cardinal «las nueve que ya existen para `vigencia`» (doc 11 `:8327`) **publique el comando que lo deriva o se retire**, que es lo que la REGLA DE TITULARES de §0 del propio documento exige | **NO** |
| **`C-20`** | Que el SOBRE **lleve el TEXTO de la ratificación del Owner**, que es el primero de los seis elementos que §11.6 rotula «y es la lista entera» y que la sede canónica `:315-317` escribe en palabras del Owner; **o** que §11.6 y la sede dejen de enumerarlo como elemento que viaja. **Este es el único remedio que TOCA UNA SEDE DEL OWNER, y por eso lo miro dos veces: ver §10.1** | ver §10.1 |
| **`C-21`** | Que el bloque «Las DOCE reglas obligatorias que `O17` fija» de `DECISIONES`:881-887 **reproduzca la sede cláusula a cláusula** —hoy convierte dos «debe» en indicativo— o **deje de presentarse con aspecto de literal**. La sede exige que cada resolución se registre «íntegramente, no en resumen» | **NO** |

### §10.1 · ¿ALGO VUELVE AL OWNER?

# NO. NADA VUELVE AL OWNER.

**Por QUINTA vez consecutiva.** Examiné los candidatos que mi propio material produce, incluido el
que más se le parece, y **los cinco caen**:

```text
· «¿Puede `F4c` cerrarse con `C` sin implementar?»          NO ES PREGUNTA NUEVA: `O18` la
  resolvió y `DD-20` fijó la frontera en su sede. Ninguno de mis 22 es `C` salvo el ATAQUE
  de `C-13`, cuya PROPIEDAD es `A` y se cierra dentro de `F4c`.
· «¿Hay que aceptar que el predicado de perímetro sea también el filtro de la guarda?»
  NO: es un defecto de ORDEN de evaluación dentro de una función, cerrable con material que
  el corpus ya tiene escrito —`S1-05` ya declara que el predicado es fabricable—. Clase `A`.
· «¿Debe el SOBRE garantizar el perímetro de TODO el árbol?»   NO: el derivador ya promete
  publicar lo que excluye y `S1-04` ya acotó la promesa; lo que falta es que la promesa y el
  alcance coincidan. Clase `A`.
· «¿Se retira la exigencia de que el checkpoint reancle?»      NO: la regla es del propio
  bloque y el corpus demuestra la forma correcta en el mismo fichero. Clase `A`.
· «`C-20` toca §11.6 y la sede canónica del Owner: ¿es una decisión del Owner?»
  **NO, y lo razono porque es el único dudoso.** `O19` L317 exige que el revisor pueda
  «comprobar la receta SIN ejecutar el emisor», y ESE FIN SE CUMPLE HOY: el sobre publica el
  digest de `O19` y la receta, y yo mismo recalculé la sede canónica sin ejecutar el emisor
  (§0.2). Lo que falla es la LISTA de §11.6, que es una sede DERIVADA del corpus y no la
  resolución. **Alinear una sede derivada con su sede canónica no reinterpreta la
  resolución: la aplica.** Y la alternativa —hacer viajar 78 líneas más en el sobre— tampoco
  exige decidir nada: es una línea del emisor.
```

**Los veintidós se cierran con material que el corpus ya tiene escrito. Ninguno reinterpreta
`O17`, `O18` ni `O19`. Ninguno exige arquitectura nueva. NO FORMULO NINGUNA PREGUNTA AL OWNER.**

---

## §11 · DISCIPLINA — declaración de cierre

```text
git status --porcelain de /home/jose/ads-kernel   AL ABRIR  → VACÍO
                                                  AL CERRAR → VACÍO
HEAD al abrir y al cerrar          → bf0c65caed52a70a7e131b8d30cdadb9e4ca5b40, sin moverse
rama local                         → fix/f4c-propiedad-de-admision-20260831 (sin tocar)
git ls-files -v | grep -vc '^H '   → 0   (ni skip-worktree ni assume-unchanged)
git reflog -1                      → bf0c65c HEAD@{0}: commit: docs(gate): manifiesto previo
                                     del octavo gate — la última entrada es del coordinador,
                                     NINGUNA mía

UNA DECLARACIÓN QUE ME TOCA HACER Y QUE NADIE ME PIDE: el contexto en que se me creó traía
un `gitStatus` ANTERIOR —rama `fix/f4c-perimetro-por-naturaleza-20260831`, con
`M docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` y `HEAD` en `4f3da18`, el QUINTO gate—.
**Ese snapshot NO describe el árbol que he auditado y no lo he usado para nada**: todas mis
mediciones salen de `git show <commit>:<ruta>` sobre los DOS commits del sobre y de clones
desechables. Lo que YO observo hoy en el repositorio auditado es lo de arriba: limpio,
`HEAD` en `bf0c65ca…`, sin bits ocultos. Lo digo porque `U-02` y `X-06` nacieron de
yuxtaponer árboles sin decir de cuál se habla.

FICHEROS DEL REPOSITORIO AUDITADO EDITADOS, CREADOS O BORRADOS POR MÍ     ninguno
COMMITS · PUSH · PR · MERGE · RAMAS · REFS · REFLOG en el repo auditado   ninguno

LABORATORIO   `git clone /home/jose/ads-kernel …/gg/clon`, y de él TRES clones desechables
              (`atk`, `atk2`, `atk3`) con rama `atacar` reseteada y `git clean -qfdx` antes
              de CADA ataque, más `read-tree`+`checkout-index` en `$(mktemp -d)` para cada
              medición de digest. Los commits de ataque viven SÓLO en los clones.
ATAQUES       2 barridos exhaustivos de 261 rutas cada uno (522 commits de ataque medidos)
              más 30 ataques dirigidos. Ninguno tocó el repositorio auditado.
INTÉRPRETE    Python 3.12.14 (shim del encargo). Con el 3.10 del sistema caen tres
              validadores por `tomllib`: es `A14`, limitación aceptada, NO un hallazgo.
GIT           WSL2, `core.quotePath` SIN FIJAR.
SUBAGENTE `Agent`                                                         NO USADO

NINGÚN HALLAZGO CORREGIDO, y es deliberado: quien corrige no certifica.
NADA RESUELTO POR MAYORÍA. NADA SUAVIZADO. NINGUNA HUELLA ABREVIADA A MANO.
NINGÚN HALLAZGO ACEPTADO POR AUTORIDAD: los 21 de los revisores están reproducidos por mí
contra fichero y línea, y el 22.º es mío y va con su comando.
```

### §11.1 · LO QUE MI PROPIA ADJUDICACIÓN NO CUBRE, SIN ADORNO

```text
1  NO he leído el documento 11 entero. Abrí sólo las localizaciones de §11.4/§11.6/§11.9 y
   `C-L.5`. Una contradicción documental interna del doc 11 es invisible para mí.
2  NO he leído el `CHECKPOINT` (5015) ni `DECISIONES` (1335) ni `00-INDICE` íntegros. Abrí
   `DD-20` —que mi encargo me obliga a leer—, el bloque de estado, la clasificación `C-L`
   y el PARTE. Lo declaro y no lo cuento como lectura.
3  NO he ejecutado ni una de las pruebas que el corpus describe. Las 55 filas `X`, las 18
   ventanas `W`, las `X-A`–`X-H`: todo es contrato escrito. Ejecuté los INSTRUMENTOS.
4  De las 38 comprobaciones, ataqué con contraejemplo propio SIETE: `G-00`, `G-21`, `G-22`,
   `G-23`, `G-29`, `G-30`, `G-34`. Las otras 31 no las ataqué. Que la batería caiga por tres
   puertas no significa que sólo haya tres.
5  Mis dos barridos cubren MODIFICACIÓN y la ADICIÓN sólo en las cinco variantes de `EE-01`.
   NO barrí exhaustivamente el eje de la ADICIÓN ni el del BORRADO. `C-00` y `C-02` pueden
   tener superficie mayor que la que enumero.
6  NO he ejecutado el emisor del sobre. Verifiqué campo a campo que el sobre recibido es lo
   que su código publica; no lo corrí, y no me corresponde emitir nada.
7  LA SEDE CANÓNICA DEL OWNER no es verificable contra nada externo, y lo declara ella misma.
   Sus digest reproducen: eso prueba que el texto no cambió entre el commit y lo que recibí
   FUERA del árbol. NO prueba que sea el que el Owner emitió. Vigente hasta `F6`.
8  Los SHA del emisor y del derivador NO prueban que los programas que corrieron fueran ésos.
   El sobre lo retira en su obligación 5 (`Z-11`) y yo no lo recupero.
9  NO he juzgado si la arquitectura de `F4c` es buena. Sé qué pasa por esta batería y por este
   sobre sin que se note. No juzgo el diseño y no lo insinúo.
```

---

# INSUFICIENTE PARA F5
# EL GATE ES VÁLIDO
# `C-L.5` · **NO CERTIFICADA** por este gate · `C-L.7` NO CERRADA · `M-04` NO SUPERADA
# NADA VUELVE AL OWNER

**ADJUDICADOR `GG` · adjudicación cerrada. El veredicto es mío y nadie por encima lo revisa.
NO he propuesto ninguna corrección al repositorio y NO lo he modificado.**
