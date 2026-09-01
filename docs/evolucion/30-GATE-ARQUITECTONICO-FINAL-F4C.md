# GATE ARQUITECTÓNICO FINAL DE `F4c` — VÁLIDO, INSUFICIENTE, Y EL PRIMERO BAJO `O20`

> **Veredicto del adjudicador `HH`: `F4c` ES INSUFICIENTE PARA F5.**
> **`F4c` NO se cierra y sigue ABIERTA. `F5` NO queda autorizada. Ningún hallazgo se ha**
> **corregido en esta pasada.**
>
> **EL GATE ES VÁLIDO, por quinta vez consecutiva.**
>
> **Y NO FALLA PORQUE EL VERIFICADOR DE `F6` NO ESTÉ IMPLEMENTADO.** Esa ausencia es
> ESPERADA, está DECLARADA, y `O20` la fija. **Ninguna de las razones del veredicto es
> ésa**, y el adjudicador lo dice expresamente.

## 0 · Qué es este documento

Registro **LITERAL** de los tres dictámenes del **primer gate emitido bajo `O20`** sobre la
candidata `7aeed6aa3a3eae1133f57a08d757020e62197b3d`, publicada en
`review/f4c-o20-frontera-de-fase-candidate-20260901`. Los tres se transcriben **enteros y sin
suavizar**, en §A, §B y §C.

Lo escrito antes de §A lo escribe el **coordinador**, que no es ninguno de los tres
participantes y **que no ha juzgado nada**.

```text
DICTAMEN DEL REVISOR `U1`
   713 lineas   SHA-256  cbbfe770dc442835c158c883b585f238fa759430bba806617102b2a57b743ef4
DICTAMEN DEL REVISOR `U2`
   906 lineas   SHA-256  303978ba13277cd12e6f4ea2204d64178ed0423d572987fbf8474ad76c103afb
ADJUDICACIÓN DE `HH`
  1313 lineas   SHA-256  5329a05bbf0474091fc73944cd68c8cdc538ab5ed7e0f80ad08dc81200d620f7
EL SOBRE DE ANCLA, leído por los tres
   201 lineas   SHA-256  c39de894c21f25a22ef5789cfa0a5a097ff3e440ffa7e8c9d654caa969792282
```

## 1 · EL GATE ES VÁLIDO

Los **dos bloques de sobre embebidos** son **byte a byte el fichero** —`cmp` sin
diferencias—, las **seis obligaciones** reproducen, y las **83 filas del manifiesto casan
contra su árbol, incluida la del propio derivador**, que no reincide por quinta vez. Ninguno
de los dos disparadores de invalidez se dispara.

## 2 · QUÉ CAMBIÓ EN ESTE GATE, Y POR QUÉ IMPORTA

`O20` movió la frontera: **`F4c` produce la arquitectura; `F6` implementa y certifica el
verificador.** Con esa frontera, el gate tenía prohibido declarar insuficiencia por la
ausencia del verificador, y tenía **siete supuestos** por los que sí debía declararla.

> **Se disparan CINCO de los SIETE. Ninguno es «el verificador no está implementado».** — `HH`

## 3 · LOS DIECIOCHO CONTRATOS DE `F6` — 18/18 COMPLETOS EN SUS CAMPOS, 16/18 CONSTRUIBLES

```text
CAMPOS            18 de 18 llevan los ONCE: fuente · propietario · implementador · fase ·
                  entrada · salida · evidencia · escenario positivo · escenario negativo ·
                  condición de bloqueo · criterio exacto de cierre
CONSTRUIBLES      16 de 18 se pueden construir **sin volver a decidir arquitectura**
LOS DOS QUE NO    `V6-15` **se contradice consigo mismo**: su escenario negativo exige «los
                  ONCE árboles» y su entrada y su criterio de cierre sólo cubren TRES gates
                  `V6-16` su norma habilitante es `PN-19`, cuya fase es **`F5`**, y §20 no
                  la cita: la asignación de fase deja de ser inequívoca, contra `O20` §1
```

## 4 · EL HALLAZGO SUAVIZADO, Y ES LA RAZÓN QUE MÁS PESA

Los dos revisores lo trajeron por vías distintas y el adjudicador lo confirmó **con una pieza
que ninguno de los dos había traído**:

```text
QUÉ SE MOVIÓ      `C-20` —el SOBRE no lleva el TEXTO de la ratificación que `O19` exige en
                  la sede canónica y que §11.6 repite— se clasificó
                  CONTRATO_COMPLETO_PARA_F6, con `V6-16` y `V6-17` como prueba de cierre
POR QUÉ ES        **ninguna de esas dos filas contiene esa obligación**, de modo que `F6`
SUAVIZARLO        podría cerrarlas enteras con el defecto intacto
LA PIEZA QUE      **§11.6 da al emisor la fase «YA, para el PRÓXIMO gate de `F4c`»**. No era
LO DECIDE         de `F6`: el corpus ya le había puesto fase, y era ésta
MEDIDO            en el sobre de este mismo gate: **2 de 62 líneas sustantivas de `O19`
                  presentes, y son un separador y una palabra suelta**
```

Y el adjudicador **resolvió contra sí mismo** la refutación obligatoria —«`C-20` es de `F6`
porque el emisor es implementación»—: **cae por cuatro vías de sede**, entre ellas que `O20`
§6 habla de «implementación **del verificador**» y que diferirlo reinstauraría la
circularidad que `O18` cerró.

## 5 · EL RECUENTO

```text
BLOQUEANTE   1        GRAVE   6        MEDIO   3        MENOR   3        LEVE   3
                                                                        TOTAL  16

De 24 entradas de los dos revisores, 8 pares fusionados y 16 consolidados.

POR CLASE
  A · coherencia interna, corregible dentro de `F4c`   16
  B · exige una decisión NUEVA del Owner                0
  C · actor privilegiado, contratado para `F6`          0
```

El adjudicador **reclasificó a `A` las cuatro que un revisor había marcado `C`**, contra la
sede que fija la frontera: `C` es corromper la REFERENCIA, y ninguna lo hace. **Ocho de
dieciséis son reincidencias, dos literales** —`P-26` y `P-03`, ésta por tercera vez.

## 6 · LO QUE CONSTA A FAVOR, PORQUE ES VERDAD

```text
· **NINGUNA sede presenta deuda de `F6` como implementación existente.** El corpus dice lo
  contrario en siete sitios, incluido el manifiesto justo después de publicar «38/38»
· **NINGUNA decisión arquitectónica queda OCULTA**: donde hay dos salidas, hay una `PN` con
  materia mínima, propietario, fase y prueba que falla hoy. `PN-19` la declara entera
· **PesquerApp NO puede iniciarse**: seis sedes normativas la bloquean
· la MATRIZ de los 22 tiene los veintidós identificadores exactos, **un estado primario
  cada uno**, sumas derivadas, cobertura vacía en las dos direcciones y **ninguno superado**
· `C-L.5` ABIERTA · `C-L.7` NO CERRADA · `M-04` NO SUPERADA: **los tres correctos**
· cobertura: `OBLIGATORIO − ASIGNADO = ∅` y `ASIGNADO − LEÍDO = ∅`
· `X63` no se presenta como ejecutado en ninguna de sus ocho sedes
· cero amplificación de la sede canónica del Owner
· **`S1-09` está aplicado ENTERO por primera vez**: §11.4, §11.6, §11.7, §11.8 y §11.9
  caen dentro del lote de quien audita el instrumento, y las leyó
· de una veintena de comandos publicados en sedes vivas, **sólo uno se autofalsifica**
· la fila del derivador NO reincide, por QUINTA vez
```

## 7 · QUÉ FALLA HOY

Falla que **un hallazgo cambió de fase en vez de cerrarse**, y que **dos de los dieciocho
contratos no se pueden construir tal como están escritos**: uno se contradice consigo mismo,
y el otro depende de una norma cuya fase es `F5` sin citarla. Y falla que **tres sedes de
registro —§15.4, §15.8 y §18— no recogieron `O20`, `D109` ni el verificador**, siendo §18 la
sede del ORDEN DE CONSTRUCCIÓN de `F6` cuyo paso 8 es PesquerApp.

**Nada de eso es la ausencia del verificador**, y el adjudicador lo separa expresamente.

## 8 · AL OWNER NO VUELVE NADA, CON UNA PRECISIÓN QUE `HH` HACE CONSTAR

Ninguno de los dieciséis es de clase `B`. **Pero `HH` deja escrito** que el remedio de `C-20`
tiene dos ramas y que **la segunda —que §11.6 y la sede dejen de enumerar ese elemento— SÍ
exigiría al Owner**, porque esa lista vive en `O19` dentro de una sede **append-only**. El
remedio determinado toma la primera, y **con ella nada vuelve al Owner**.

---

## §A · DICTAMEN DEL REVISOR `U1` — TRANSCRIPCIÓN LITERAL

# INFORME `U1` — REVISOR INDEPENDIENTE · GATE ARQUITECTÓNICO FINAL DE `F4c`

Fecha 2026-09-01 · Dominio: arquitectura del verificador y de la raíz de confianza, y COMPLETITUD de los contratos entregados a `F6`.
Frontera de certificación aplicada: `O20` — objeto = SUFICIENCIA ARQUITECTÓNICA, no implementación.

---

# §0 · EL SOBRE Y SUS SEIS OBLIGACIONES

## §0.1 · El sobre recibido, íntegro y byte a byte

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
  REF REMOTA CANDIDATA    refs/heads/review/f4c-o20-frontera-de-fase-candidate-20260901
  COMMIT CANDIDATO        7aeed6aa3a3eae1133f57a08d757020e62197b3d
  ARBOL CANDIDATO         0a8f5804e37bfb4ea05deabd18659cd2864f1d73
  REF REMOTA DEL GATE     refs/heads/gate/f4c-arquitectonico-final-20260901
  COMMIT DEL GATE         ebd52d9125fb740c1c7a7606f82876b8433ef6a8
  ARBOL DEL GATE          06257a734e15af67142759029ae429839716d2ea
  RUTA DEL MANIFIESTO     docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md
  SHA-256 DEL MANIFIESTO  ff4116703b648586bae866cd259f37f7800088e8fe2148b4f4224b466322fc13   (en el commit del gate)
  ASIGNACIONES            14   DERIVADAS de las 9 filas de reparto del manifiesto,
                          no recibidas por parámetro
------------------------------------------------------------------------------
LOS DOS ARBOLES, CADA UNO DERIVADO DE SU PROPIO COMMIT CON SU PROPIO DERIVADOR.
El derivador es FILA DE SU PROPIO UNIVERSO y el commit del gate lo toca: por eso el
sobre publica LOS DOS y no mezcla ni un campo. El gate anterior yuxtapuso el árbol
de la candidata con las cifras del árbol del gate, y eran insatisfacibles.

                          CANDIDATA                                                         GATE
  COMMIT                  7aeed6aa3a3eae1133f57a08d757020e62197b3d                          ebd52d9125fb740c1c7a7606f82876b8433ef6a8
  SHA-256 DEL DERIVADOR   0eca7103833110c32b4d2fda23acf54a04c905e40e98b6fda102e5d2dd5f312e  0eca7103833110c32b4d2fda23acf54a04c905e40e98b6fda102e5d2dd5f312e
  SHA-256 DEL EMISOR      8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453  8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453
  FUENTES OBLIGATORIAS    83                                                                84
  LINEAS OBLIGATORIAS     87898                                                             88156
  DIGEST DEL UNIVERSO     d12b64b91ad313557df6bdf1c2a38f2ccb2d8a264b3f12553ada8e3a56ed551f  868fb198e8b7699fc2b1161d76b29f804a911e2e6e8ba6e7712a7596bbef464d


  SHA-256 DEL EMISOR QUE HA CORRIDO ESTE SOBRE: 8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453
  COINCIDE con el del commit del gate. El revisor puede rehacer este contraste:
    git show ebd52d9125fb740c1c7a7606f82876b8433ef6a8:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum

  RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: 2
    docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md  AUSENTE → ff4116703b64
    docs/evolucion/00-INDICE.md  1077403f421f → 0c6587c2298a

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
  RESOLUCIONES ANCLADAS   4, DERIVADAS de la sede y no escritas: O17 (85 lineas) · O18 (111 lineas) · O19 (81 lineas) · O20 (107 lineas)
  EXIGIDAS POR `O19`      O17 · O18 · O19   sin una sola de ellas NO HAY SOBRE

                          CANDIDATA (COMMIT AUDITADO)                                       GATE
  SHA-256 DE LA SEDE      4e4081efb29dcd2f095879b07104e4e169a46b497d11213256541fd6599a4e3a  4e4081efb29dcd2f095879b07104e4e169a46b497d11213256541fd6599a4e3a
  DIGEST DE `O17`         0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125  0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125
  DIGEST DE `O18`         ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353  ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
  DIGEST DE `O19`         d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632  d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632
  DIGEST DE `O20`         c3804cdec674b140a508f84a1b19a463efe27cd31b108b443271d34dab1906f3  c3804cdec674b140a508f84a1b19a463efe27cd31b108b443271d34dab1906f3

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
  git show 7aeed6aa3a3eae1133f57a08d757020e62197b3d:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O17`/)} p' | sha256sum

  ── `O18` → ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
  git show 7aeed6aa3a3eae1133f57a08d757020e62197b3d:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O18`/)} p' | sha256sum

  ── `O19` → d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632
  git show 7aeed6aa3a3eae1133f57a08d757020e62197b3d:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O19`/)} p' | sha256sum

  ── `O20` → c3804cdec674b140a508f84a1b19a463efe27cd31b108b443271d34dab1906f3
  git show 7aeed6aa3a3eae1133f57a08d757020e62197b3d:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O20`/)} p' | sha256sum

  ── LA SEDE ENTERA → 4e4081efb29dcd2f095879b07104e4e169a46b497d11213256541fd6599a4e3a
  git show 7aeed6aa3a3eae1133f57a08d757020e62197b3d:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
==============================================================================
  EMITIDO                 2026-09-01 08:19:24 +0200
  EMISOR                  Jose Lopez Gonzalez (jose@congeladosbrisamar.es), coordinador nombrado del gate arquitectonico final
  DECISION QUE LO EXIGE   O18 · alternativa (b) · propagada por D108
  ENTREGA                 este sobre se entrega a cada revisor DENTRO de su encargo
                          y ANTES de que empiece a leer. NO se obtiene leyendo el
                          repositorio que se audita
==============================================================================
COMO SE RECALCULA CADA DIGEST, para que el revisor no tenga que fiarse. Reproduce el
digest BYTE A BYTE; si no lo reproduce, el sobre o el árbol están mal, y en ese orden:

  ── ARBOL CANDIDATO → d12b64b91ad313557df6bdf1c2a38f2ccb2d8a264b3f12553ada8e3a56ed551f
  C=7aeed6aa3a3eae1133f57a08d757020e62197b3d
  d=$(mktemp -d)
  GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
  rm -rf "$d"

  ── ARBOL DEL GATE  → 868fb198e8b7699fc2b1161d76b29f804a911e2e6e8ba6e7712a7596bbef464d
  C=ebd52d9125fb740c1c7a7606f82876b8433ef6a8
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

SHA-256 del sobre tal como lo recibí: `c39de894c21f25a22ef5789cfa0a5a097ff3e440ffa7e8c9d654caa969792282`

## §0.2 · LAS SEIS OBLIGACIONES, CUMPLIDAS UNA A UNA

**OBLIGACIÓN 1 · RECALCULAR LOS DOS DIGEST ANTES DE LEER NADA.** Cumplida. Receta del sobre, literal, sobre cada commit con su propio derivador extraído de ese mismo commit:

```bash
C=7aeed6aa3a3eae1133f57a08d757020e62197b3d   # y después C=ebd52d9125fb740c1c7a7606f82876b8433ef6a8
d=$(mktemp -d); GIT_INDEX_FILE="$d/idx" git read-tree "$C"
GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
  while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
  awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
```

| árbol | digest recalculado por mí | digest del sobre | ¿reproduce? | fuentes | líneas |
|---|---|---|---|---|---|
| CANDIDATA `7aeed6a` | `d12b64b91ad313557df6bdf1c2a38f2ccb2d8a264b3f12553ada8e3a56ed551f` | idéntico | **SÍ** | 83 | 87898 |
| GATE `ebd52d9` | `868fb198e8b7699fc2b1161d76b29f804a911e2e6e8ba6e7712a7596bbef464d` | idéntico | **SÍ** | 84 | 88156 |

Y los `tree` SHA que el sobre publica también reproducen: `git rev-parse <commit>^{tree}` da `0a8f5804e37bfb4ea05deabd18659cd2864f1d73` y `06257a734e15af67142759029ae429839716d2ea`, que son los dos ANCLADOS. **Las cuatro cifras del sobre —83 · 87898 · 84 · 88156— las he DERIVADO, no leído.** El gate NO es inválido por este concepto y sigo.

**OBLIGACIÓN 2 · LEER EL MANIFIESTO EN EL COMMIT DEL GATE Y COMPROBAR SU SHA-256.** Cumplida.

```bash
git show ebd52d9125fb740c1c7a7606f82876b8433ef6a8:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md | sha256sum
→ ff4116703b648586bae866cd259f37f7800088e8fe2148b4f4224b466322fc13
```

Coincide con el sobre. Y el mismo `git show` sobre el commit CANDIDATO responde `fatal: path ... exists on disk, but not in '7aeed6a...'`, que es exactamente lo que el sobre declara en su lista de rutas divergentes (`AUSENTE → ff4116703b64`). **He leído el manifiesto del COMMIT, no del árbol de trabajo.**

**OBLIGACIÓN 3 · CADA FILA CONTRA EL ÁRBOL QUE DECLARA, Y LA FILA DEL DERIVADOR PRIMERO.** Cumplida. El manifiesto §2 (L42) declara que su objeto es el ÁRBOL DE LA CANDIDATA. Contrasté **las 83 filas** —9 de §4 y 74 de §5— contra `7aeed6a`, línea y SHA-256:

```bash
while IFS=$'\t' read -r r l s; do
  al=$(git show "$C:$r" | wc -l); as=$(git show "$C:$r" | sha256sum | cut -d' ' -f1)
  [ "$al" != "$l" ] || [ "$as" != "$s" ] && echo "DISCREPA $r"
done < filas.tsv
→ FILAS_DISCREPANTES_CONTRA_ARBOL_CANDIDATO=0
```

**LA FILA DEL PROPIO DERIVADOR, MIRADA PRIMERO** —la que `U-02` falseó y `X-06` reincidió—: fila 6 de §4, `docs/evolucion/verificacion/derivar-universo-obligatorio.py`, declara **846 líneas** y `0eca7103833110c32b4d2fda23acf54a04c905e40e98b6fda102e5d2dd5f312e`. Recalculado sobre la candidata: **846** y `0eca7103833110c32b4d2fda23acf54a04c905e40e98b6fda102e5d2dd5f312e`. **NO REINCIDE. La fila del derivador es cierta esta vez, y lo digo aunque no me convenga como hallazgo.**

**OBLIGACIÓN 4 · LAS RUTAS EN QUE DIFIEREN LOS UNIVERSOS NO SON LAS RUTAS EN QUE DIFIEREN LOS ÁRBOLES.** Cumplida, y el sobre dice la verdad al distinguirlas.

```bash
git diff --name-only 7aeed6aa3a3eae1133f57a08d757020e62197b3d ebd52d9125fb740c1c7a7606f82876b8433ef6a8
→ docs/evolucion/00-INDICE.md
  docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md
  kernel/operativo/pruebas/evidencia/fuentes-salida.txt
  kernel/operativo/pruebas/evidencia/negativos-salida.txt
  kernel/operativo/pruebas/evidencia/referencias-salida.txt
```

**LOS ÁRBOLES DIFIEREN EN CINCO RUTAS; LOS UNIVERSOS OBLIGATORIOS SÓLO EN DOS.** Las tres restantes son evidencia reejecutada, que no es fuente obligatoria. El sobre **NO las nombra y advierte expresamente de que no las nombra**, remitiendo al `git diff` que acabo de correr; el manifiesto §6 (L192) las declara con su razón: «LA EVIDENCIA REEJECUTADA no son fuentes obligatorias: no entran en el universo». **Las dos sedes coinciden y ninguna esconde las otras tres. No es hallazgo.**

**OBLIGACIÓN 5 · QUÉ PRUEBA Y QUÉ NO PRUEBA EL `git status` VACÍO — Y LOS SHA DEL EMISOR Y DEL DERIVADOR.** Cumplida, y recalculada de los DOS commits, que es lo único que el sobre me permite comprobar:

| pieza | commit CANDIDATO | commit del GATE | ¿= sobre? |
|---|---|---|---|
| `emitir-sobre-de-ancla.py` | `8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453` | idéntico | **SÍ** |
| `derivar-universo-obligatorio.py` | `0eca7103833110c32b4d2fda23acf54a04c905e40e98b6fda102e5d2dd5f312e` | idéntico | **SÍ** |

**Y asumo la limitación que el propio sobre declara y que `Z-11` midió:** que estas huellas coincidan prueba que el emisor y el derivador PUBLICADOS son los que están EN LOS COMMITS. **NO prueba que sean los que se EJECUTARON.** `git update-index --skip-worktree` vacía `git status` con el fichero modificado en disco. La retirada de la frase «un sobre existente es, por construcción, un sobre limpio» es correcta y este informe no la resucita.

**OBLIGACIÓN 6 · RECALCULAR LOS DIGEST DE LA SEDE CANÓNICA Y CONTRASTARLOS CON TODA SEDE DERIVADA.** Cumplida. Sobre los DOS commits, con la receta `awk` del sobre:

| | CANDIDATA | GATE | sobre | ¿reproduce? | líneas derivadas |
|---|---|---|---|---|---|
| SEDE ENTERA | `4e4081ef…9a4e3a` | idéntico | idéntico | **SÍ** | 444 |
| `O17` | `0cc5b9b5…4e6125` | idéntico | idéntico | **SÍ** | **85** |
| `O18` | `ab9d9447…ed0353` | idéntico | idéntico | **SÍ** | **111** |
| `O19` | `d86a9455…ddf632` | idéntico | idéntico | **SÍ** | **81** |
| `O20` | `c3804cde…1906f3` | idéntico | idéntico | **SÍ** | **107** |

Las cuatro longitudes que el sobre declara —85 · 111 · 81 · 107— las he DERIVADO con el mismo `awk`, no leído. **Los dos commits publican la misma sede byte a byte, como el sobre afirma.** `O19` exige `O17`·`O18`·`O19` y las tres están; `O20` está y es la resolución que fija la frontera de este gate.

**Y el contraste de PARÁFRASIS que la obligación 6 me manda hacer:** barrí las sedes derivadas que citan `O20` —`00-INDICE.md` L104, `DECISIONES-Y-CONTRADICCIONES.md` `D109` L545, `CHECKPOINT-ADS-NEXT.md`, y §20 del documento 11— contra el texto canónico. **§20 se rotula a sí misma PROYECCIÓN DERIVADA y declara que si difiere de la sede manda la sede** (doc 11 L11723-11726). No he encontrado ninguna paráfrasis que AMPLÍE la autoridad del texto canónico de `O20`. La única discrepancia de precisión que sí encontré va como hallazgo `U1-03`, y es de RECUENTO DE CAMPOS, no de autoridad.

## §0.3 · VEREDICTO SOBRE LA VALIDEZ DEL GATE

**EL GATE ES VÁLIDO.** Los dos digest de universo reproducen byte a byte, los dos `tree` SHA reproducen, el manifiesto reproduce en el commit del gate y está ausente del candidato como se declara, las 83 filas reproducen contra el árbol que declaran, la fila del derivador **no reincide**, el emisor y el derivador reproducen en los dos commits, y la sede canónica y sus cuatro resoluciones reproducen en los dos commits y contra el sobre. **Ninguna de las seis obligaciones falla, y por tanto sigo leyendo.**

---
# §1 · MI MANIFIESTO DE LECTURA, Y LAS RESTAS

**Todo lo que sigue se lee del COMMIT DEL GATE `ebd52d9125fb740c1c7a7606f82876b8433ef6a8` con `git show <commit>:<ruta>`.** No he leído un solo byte del directorio de trabajo para emitir juicio, y no he escrito ni un byte en el repositorio: `git status --porcelain` sigue vacío y no he creado rama, commit ni referencia.

## §1.1 · Las seis fuentes de mi lote, con su SHA-256 RECALCULADO por mí

```bash
for f in <las 6 rutas>; do git show ebd52d9…:$f | sha256sum; git show ebd52d9…:$f | wc -l; done
```

| # | ruta | líneas decl. | líneas recalc. | SHA-256 recalculado | ¿= lote? | alcance asignado | **¿LEÍDO ÍNTEGRO EN MI ALCANCE?** |
|---|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11791 | **11791** | `4ad648c17b0e753fcd0373bcbe8922e76593e0968f9c36a9a8ae693fecf0c815` | **SÍ** | `L1–L5200` **y** `L8200–L11791` | **SÍ** |
| 2 | `docs/evolucion/29-OCTAVO-GATE-DE-CERTIFICACION-F4C.md` | 4197 | **4197** | `0b9064490c8dd68ec7c50ed87778d31ab8ab5360c966642113367a0eeba2e5ac` | **SÍ** | ÍNTEGRO · EL ÚLTIMO | **SÍ** |
| 3 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 4339 | **4339** | `29a754dac385115b773a43f4b714872540aee4236875c42126f9d4f97f906db0` | **SÍ** | ÍNTEGRO | **SÍ** |
| 4 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 846 | **846** | `0eca7103833110c32b4d2fda23acf54a04c905e40e98b6fda102e5d2dd5f312e` | **SÍ** | ÍNTEGRO | **SÍ** |
| 5 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-8-20260831.md` | 248 | **248** | `a82e74968e4ca31fbae0825a43f295736af39e58a16b3adf8879d021688e3d76` | **SÍ** | ÍNTEGRO | **SÍ** |
| 6 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 444 | **444** | `4e4081efb29dcd2f095879b07104e4e169a46b497d11213256541fd6599a4e3a` | **SÍ** | ÍNTEGRO · SEDE CANÓNICA | **SÍ** |

**LAS SEIS HUELLAS COINCIDEN con las del `LOTE-U1.md`, y ninguna la he abreviado a mano.** La 6 coincide además con la del SOBRE en los DOS commits, que es la comprobación de `O19`.

## §1.2 · `ASIGNADO − LEÍDO`, declarado CONTRA MI PROPIO INTERÉS

```text
ASIGNADO − LEÍDO = ∅
```

**Documento 11**, los dos tramos asignados, por rangos consecutivos y sin hueco: `L1-400 · L400-800 · L800-1200 · L1200-1600 · L1600-2000 · L2000-2400 · L2400-2800 · L2800-3200 · L3200-3600 · L3600-4000 · L4000-4400 · L4400-4800 · L4800-5200` ∪ `L8200-8560 · L8560-8912 · L8912-9280 · L9280-9660 · L9660-10060 · L10060-10460 · L10460-10760 · L10758-11080 · L11080-11360 · L11360-11560 · L11560-11700 · L11700-11791`. **Unión = `L1-L5200` ∪ `L8200-L11791`, que es exactamente mi alcance.** `L5201-L8199` **NO los he leído y NO los reclamo**: son de `U2` por el §4 del manifiesto, y lo digo aunque cite dos veces —`L5685` y `L5697`— una región de `U2` a la que entré para comprobar `X63`, entrada que declaro aquí y que no convierte ese tramo en leído.

**Documentos 2, 3, 4, 5 y 6**: leídos ÍNTEGROS, `L1` a su última línea.

**Y declaro TRES lecturas fuera de mi lote**, que hago constar para que el adjudicador pueda descontarlas: `CHECKPOINT-ADS-NEXT.md` `L3985-4060` y `L4052-4060` (la MATRIZ DE CIERRE, que es de `U2`), `DECISIONES-Y-CONTRADICCIONES.md` `L545` y sus cabeceras `### \`O` (que es de `U2`), y los documentos 27 y 28, agotados, para contar menciones. **Ninguna de esas fuentes la declaro leída íntegra, y ningún hallazgo mío se funda ÚNICAMENTE en ellas.**

## §1.3 · `OBLIGATORIO − ASIGNADO`, RECALCULADA POR MÍ SOBRE LOS DOS ÁRBOLES

```bash
{ sed -n '76,84p' MANIF; sed -n '104,177p' MANIF; } | awk -F'|' '{gsub(/[` ]/,"",$3); print $3}' | sort -u > asignado.txt   # 83 rutas
comm -23 <(derivar --rutas sobre <commit> | sort -u) asignado.txt
```

| árbol | obligatorio | asignado | `OBLIGATORIO − ASIGNADO` | `ASIGNADO − OBLIGATORIO` |
|---|---|---|---|---|
| CANDIDATA `7aeed6a` | 83 | 83 | **∅ · CERO FUENTES SIN ASIGNAR** | **∅** |
| GATE `ebd52d9` | 84 | 83 | **1** — `…/F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md` | **∅** |

**La única fuente sin fila sobre el árbol del gate es EL PROPIO MANIFIESTO**, y su §6 (L189-191) la declara ANTES de que yo la encontrase, como «exención de PUNTO FIJO de `DD-19`, y cubre a ESTE fichero y a NINGÚN OTRO». **No hay ninguna otra.** El manifiesto §6 L197 se compromete a que «CUALQUIER OTRA FUENTE SIN FILA sobre el árbol del gate es un DEFECTO de este manifiesto», y **no la hay**. La resta cierra.

## §1.4 · LAS DOS ARITMÉTICAS DEL MANIFIESTO, DERIVADAS CONTRA SU PROPIA TABLA (`C-05`)

El manifiesto §6 afirma cuatro cifras. **Las he derivado de sus tablas §4 y §5, no leído:**

```bash
sed -n '76,84p'   MANIF | awk -F'|' '{gsub(/ /,"",$4); s+=$4; n++} END{print n, s}'   → 9  28847
sed -n '104,177p' MANIF | awk -F'|' '{gsub(/ /,"",$4); s+=$4; n++} END{print n, s}'   → 74 59051
sed -n '104,177p' MANIF | grep -c '\*\*LEÍDA\*\*'                                     → 3
sed -n '104,177p' MANIF | grep -c '\*\*DELEGADA\*\*'                                  → 71
```

| lo que §6 AFIRMA | lo que su §4/§5 DA | ¿coincide? |
|---|---|---|
| ASIGNADAS A LECTURA **9 · 28847 líneas** | 9 filas · 28847 | **SÍ** |
| ASIGNADAS COMO AGOTADAS **74 · 59051 líneas** | 74 filas · 59051 | **SÍ** |
| «de ellas **3 LEÍDAS y 71 DELEGADAS**» | 3 y 71 | **SÍ** |
| `OBLIGATORIO − ASIGNADO` **0** sobre la candidata | ∅ (§1.3) | **SÍ** |

**Y el cierre aritmético, que nadie escribe y que derivo yo:** `9 + 74 = 83` fuentes y `28847 + 59051 = 87898` líneas, **que son EXACTAMENTE las 83 fuentes y las 87898 líneas del ÁRBOL DE LA CANDIDATA** que el sobre ancla y que yo rederivé. **Las dos aritméticas del manifiesto DERIVAN, y `EE-02` está cumplido.**

**`C-05` — «el reparto se comprueba contra la propia tabla y ninguna frase afirma lo que la tabla no dé», COMPROBADO.** La frase del manifiesto L66-69 afirma que `U1` lee `L1-L5200` y `L8200-L11791`, que `U2` lee `L5201-L11791` y que la sede canónica la leen los tres. **Su §4 lo DA**: fila 2 escribe ese reparto palabra por palabra y fila 8 escribe «los tres». **La frase no afirma nada que la tabla no dé**, y el propio manifiesto añade la regla de desempate correcta —«si difieren, manda §4»—. **No es hallazgo.**

**`C-10` — la columna de agotamiento distingue LEÍDA de DELEGADA, Y ES CIERTA.** Las tres `LEÍDA` son `28-SEPTIMO-GATE`, `verificacion/README.md` y `emitir-sobre-de-ancla.py`, con procedencia «documento 29, L537 · L538 · L541». **Lo comprobé contra el documento 29**: su tabla de manifiesto de lectura en L534-541 declara `LEÍDO ÍNTEGRO` **SÍ** para las tres, en las filas 2, 3 y 6, con sus rangos enumerados. **Las tres son ciertas.** Y las 71 `DELEGADA` llevan el rótulo honesto —«**Nadie declaró haberla leído íntegra en ese gate**»—, que es exactamente lo que `C-10` exigía y lo contrario de lo que un rótulo inflado diría. **No es hallazgo, y es a favor del manifiesto.**

---
# §2 · HALLAZGOS

**Ninguno de los diez de abajo se funda en que el verificador de `F6` no esté implementado.** Esa ausencia es ESPERADA, está DECLARADA y `O20` la fija; no la cuento, no la ponderé y no la uso. Todos son defectos ARQUITECTÓNICOS o DOCUMENTALES, que `O20` §6 mantiene bloqueando `F4c`.

| id | severidad | clase | sede fichero:línea | qué afirma esa sede | qué dice el árbol, con comando y salida | qué se sigue |
|---|---|---|---|---|---|---|
| **`U1-01`** | **BLOQUEANTE** | **A** | `docs/evolucion/CHECKPOINT-ADS-NEXT.md`:4076 · contra `docs/owner/ADS-OWNER-RESOLUCIONES.md`:315-317 y `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`:8449 | `C-20` —«el SOBRE debe llevar el TEXTO de la ratificación del Owner»— se clasifica `CONTRATO_COMPLETO_PARA_F6`, fase `F6`, `prueba_de_cierre = V6-16 · V6-17` | **(a)** `O19`, SEDE CANÓNICA L315-317: «Cada revisor debe recibir externamente: **el texto de esta ratificación** · el SHA del commit candidato · el tree SHA · el SHA del manifiesto · el SHA del derivador · el SHA de la sede del Owner». **(b)** §11.6 L8449 lo repite como «la lista entera». **(c)** El sobre que YO he recibido tiene **201 líneas** y el texto canónico de `O19` tiene **81**; `grep` de cuatro frases exclusivas de `O19` sobre el sobre da **NO, NO, NO, NO**. **(d)** `V6-16` (doc 11:11775) contrata la RAÍZ EXTERNA de ejecución y `V6-17` (11776) el digest interno frente al ancla. `sed -n '11775,11776p' \| grep -ci 'sobre de ancla\|ratificaci\|texto del Owner'` → **0**. **Aviso de método, contra mi propio interés:** el barrido ingenuo que incluye `sobre` a secas devuelve **1**, y ese golpe es la PREPOSICIÓN —«los dos coinciden **sobre** un árbol sano», en `V6-17`—, no el SOBRE DE ANCLA. Lo verifiqué con `grep -oi` antes de afirmarlo. **Ninguna de las dos filas menciona el sobre, la ratificación ni el texto del Owner** | **Un incumplimiento VIVO de una orden del Owner sobre el sobre de ESTE gate está aparcado como deuda de `F6` bajo dos contratos que no lo contienen.** No es un defecto de IMPLEMENTACIÓN del verificador —es el ancla documental de `O18(b)`, que existe para cerrar `F4c`—, luego `O20` §6 no autoriza diferirlo. Y su CRITERIO DE CIERRE apunta a contratos ajenos: `F6` puede cerrar `V6-16` y `V6-17` enteros **sin que `C-20` quede cerrado** |
| **`U1-02`** | **GRAVE** | **A** | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`:10758-10896 (§18, «Orden de construcción para F6») | §18 es el GRAFO DE DEPENDENCIAS de `F6`. L10882-10883: «SE CONFIRMA EL RESTO 1 estado · 2 adaptadores · 3 iniciativa · 4 certificación · 5 pack · 6 cobertura · 7 runtime · **8 primera adopción real**». L10884-10887: «**el paso 8 exige la BASE COMPLETA ACORDADA de los pasos 0 a 7**» | `sed -n '10758,10896p' … \| grep 'O20\|verificador\|raíz externa\|V6-\|O18\|O19'` → **NINGUNA coincidencia**. §18 no tiene nodo para «implementar y certificar el verificador de admisión y la raíz externa», que es la PRIMERA y la SEGUNDA responsabilidad que `O20` §3 da a `F6`. Y §15.4:9248 designa **§18** como una de las tres sedes de `O15` (la adopción de PesquerApp) | **La sede que fija QUÉ construye `F6` y EN QUÉ ORDEN no contiene la mayor obligación que `O20` le da**, y enumera como base del paso 8 —PesquerApp PERMANENTE— unos pasos 0-7 entre los que el verificador NO está. El bloqueo existe en §11.8:8866 y en §20.2:11787, pero **la sede del ORDEN DE CONSTRUCCIÓN lo desmiente por omisión**, y es la que un `F6` lee para planificar |
| **`U1-03`** | **GRAVE** | **A** | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`:9227-9261 (§15.4) | L9233-9236, regla declarada de la propia tabla: «esta tabla contiene **UNA FILA POR RESOLUCIÓN** del Owner, derivada de las cabeceras `### \`O` de la sección 2 de `DECISIONES-Y-CONTRADICCIONES.md` … **Una resolución sin fila aquí es el defecto**» | `comm -23 <(grep -oE '^### \`O[0-9]+\`' DECISIONES \| grep -oE 'O[0-9]+' \| sort -u) <(sed -n '9238,9261p' doc11 \| grep -oE '^\| \`O[0-9]+\`' \| grep -oE 'O[0-9]+' \| sort -u)` → **`O20`**. El registro tiene `### \`O20\`` en `DECISIONES`:1237; §15.4 va de `O7` a `O19` | **`O20` —la resolución que cambia la frontera de certificación y que crea §20 entera— no tiene fila en la tabla cuyo objeto declarado es «dónde queda cada resolución del Owner».** Es el defecto por la regla que la propia sede escribe, y es exactamente la clase que `P-26` corrigió aquí para `O16` |
| **`U1-04`** | **GRAVE** | **A** | `docs/evolucion/verificacion/derivar-universo-obligatorio.py`:767 y `docs/evolucion/CHECKPOINT-ADS-NEXT.md`:4098-4101 | Las dos sedes afirman que la unificación de la fórmula de líneas en sus TRES usos «es trabajo de `F6` y **va contratado en `V6-04`** de §20 del documento 11» / «la unificación de la fórmula en las tres sedes es trabajo de `F6`, y **va en `V6-04`**» | `V6-04` (doc 11:11763) contrata, palabra por palabra: «**Inventario DERIVADO de todas las lecturas Git; ninguna vía paralela oculta** … el censo se DERIVA del código; **cero** lecturas fuera del canal». `sed -n '11763p' \| grep -ci 'línea\|fórmula\|blob'` → **0**. Y `sed -n '11760,11777p' \| grep -i 'fórmula'` → **ninguno de los DIECIOCHO** la menciona | **La obligación residual de `C-11` está asignada a un contrato cuyo objeto es OTRO.** `F6` puede cerrar `V6-04` entero —derivar el censo de lecturas Git— y la divergencia de la fórmula de líneas en tres sedes seguiría viva **sin contrato que la reclame**. Es `O20` §1 incumplido: la asignación no es inequívoca |
| **`U1-05`** | **MEDIO** | **A** | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`:9310-9662 (§15.8) | L9324-9327, regla 2 de la propia sede: «EL RECUENTO DE CORRECCIONES SE DERIVA DE LOS BLOQUES `###` DE ESTA SECCIÓN … **Toda tanda nueva abre su bloque en el mismo acto en que escribe sus decisiones: no abrirlo es lo que rompió la derivación dos veces**». Y L13-14 de la cabecera del documento remite aquí | `sed -n '9310,9662p' \| grep -cE '^### '` → **18**, de `D23`–`D33` a **`D108`**. `grep -n 'D109'` sobre §15.8 → **NADA**. `grep -n 'D109'` sobre el documento 11 ENTERO → **una sola línea, la 11723**, dentro de §20 y como cita de procedencia. `D107` (propagación de `O17`) tiene bloque en L9605 y `D108` (propagación de `O18`) en L9620 | **La tanda de `O20` no ha abierto su bloque**, mientras las dos tandas homólogas sí lo hicieron. El cardinal «dieciocho» de la cabecera es cierto HOY **sólo porque falta el bloque**, que es la forma exacta en que `P-03` describió el defecto: «la sede de la que la cifra decía derivarse estaba incompleta en dos tandas, luego la cifra no derivaba de nada». **Reincidencia de clase, una tanda después** |
| **`U1-06`** | **MEDIO** | **A** | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`:8449-8466 (§11.6, campos 17 y 18) y su obligación `6bis` | Campo 17: «`O17`, `O18` y `O19`, **nombrados uno a uno**». Campo 18: «un digest **por resolución**». Obligación `6bis`: «los digests del texto canónico de **`O17`, `O18` y `O19`** contra el campo 18» | `sed -n '8329,8627p' … \| grep 'O20'` → **NINGUNA mención de `O20` en toda §11.6**. Lo mismo en §11.9: `sed -n '8912,8980p' \| grep 'O20'` → ninguna. **El INSTRUMENTO es más general que la ARQUITECTURA**: `emitir-sobre-de-ancla.py`:67 dice «**todas** las que la sede contenga, y se EXIGEN al menos `O17`, `O18` y `O19`», y `RESOLUCIONES_EXIGIDAS = ("O17","O18","O19")` (:143) | **La REGLA arquitectónica del sobre ancla menos resoluciones de las que el gate necesita.** Un sobre que publicara sólo `O17`·`O18`·`O19` satisface §11.6 al pie de la letra y **no anclaría `O20`**, que es la resolución que define lo que este gate juzga. Hoy no ocurre porque el emisor deriva todas; la sede que `F6` y los gates futuros leen sigue diciendo tres. **A favor, y consta: mi sobre SÍ trae `O20` con su digest, y lo he verificado** |
| **`U1-07`** | **MEDIO** | **C** | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py`:2243, :2283 y :3009 | Tres bloques rotulados **`` `O20`. ``** en la posición donde este fichero pone identificadores de hallazgo, y el detalle que la batería IMPRIME en su informe dice «se juzgan APPEND-ONLY y NO byte a byte **(`O20`)**» | El texto canónico de `O20` NO contiene esa norma: `awk '/^# /{p=($0~/^# \`O20\`/)} p' sede \| grep -i 'append\|byte\|inmutab\|nacimiento'` → **una sola línea, la 105 de `O20`**, y es su nota de trazabilidad describiendo que la SEDE es append-only, no una regla sobre el inventario. La fuente real es `O19` y las reglas propias de la sede — **y el propio fichero lo dice bien en :3395: «`O19` declara esa zona APPEND-ONLY»** | **Una sede derivada atribuye a `O20` una propiedad normativa que `O20` no contiene**, y lo IMPRIME en el informe que un revisor lee. Es la clase de la que nació `O19` —cláusula 9: «una paráfrasis nunca puede ampliar la autoridad del texto canónico»— y la que `Y-05`/`X-O13` cerraron para `(c)`. **En descargo: la propiedad es CIERTA y su fuente correcta está citada 1 100 líneas más abajo; lo que falla es el rótulo** |
| **`U1-08`** | **MEDIO** | **C** | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`:11774 (`V6-15`) | Escenario NEGATIVO: «**los once árboles** vuelven a dar ROJO, uno a uno». ENTRADA: «documentos 27, 28 y 29». Criterio de cierre: «**cada** control de los tres gates presente, con su identificador de origen» | `O20`, sede canónica L361: «**Ocho gates** independientes han encontrado **once árboles** adversariales». Los documentos 27, 28 y 29 son los gates **sexto, séptimo y octavo** — tres de los ocho. Y el censo de los once **no existe**: `git grep -i 'once árboles'` sobre todo el corpus da **4 golpes** (doc 11:11735, doc 11:11774, `CHECKPOINT`:3998, sede:361), **los cuatro narrativos y ninguno enumerativo** | **La columna del escenario negativo exige una cantidad que su propia columna de ENTRADA no puede suministrar**, y el conjunto de los once no está enumerado con identificadores en ninguna sede. El criterio EXACTO de cierre sí es derivable —los controles de tres documentos nombrados—, luego `V6-15` **se puede construir**; lo que no cuadra es su escenario negativo con su entrada. **Lo digo como defecto de PRECISIÓN del contrato, no como imposibilidad de construirlo** |
| **`U1-09`** | **MENOR** | **C** | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`:10901-10913 (§19, «NADA ESTÁ PROBADO») y :432-439 (§2.1, las poblaciones del prefijo `X`) | §19 enumera las familias de contrato de prueba: «las filas de la tabla adversarial de §2.6.7, los escenarios negativos de §11.5, las comprobaciones `X-A`–`X-H` de §2.9, las filas `X-S` de la FASE 0 de §9.6 y las filas `X-O` del SOBRE DE ANCLA de §11.6». §2.1 L431-439 censa CINCO poblaciones de identificadores de prueba | Ninguna de las dos nombra la familia **`V6-01`–`V6-18`**, que §20 crea. `git grep -n 'V6-'` sobre el documento 11 → **sólo L11760-11777**, la propia tabla | **La familia de contratos de prueba más nueva del documento no entra en las dos sedes que censan las familias.** No esconde nada —§20 declara su propia no ejecución tres veces— y por eso es MENOR; pero es la misma clase que `DD-10`/`DD-13` cerraron aquí cuando faltaba `X-O` |
| **`U1-10`** | **MENOR** | **C** | `docs/evolucion/verificacion/derivar-universo-obligatorio.py`:494-536 (`ENCARGO`, componente v) | El componente (v) es «el objeto que **ESTE** gate juzga, según SU encargo», y sus cláusulas se leen en el informe del gate | Las cláusulas siguen siendo las del OCTAVO gate: `:495-496` mete el documento 21 por «los 24 hallazgos del documento 21 · `M-04` · `Q-01` `Q-04` `Q-05`», y `:506-507` mete el emisor por «`O18` · el emisor del SOBRE DE ANCLA, **que este gate estrena** y debe refutar» — el sobre se estrenó cuatro gates atrás | **La cláusula que el revisor «lee en el informe del gate» describe otro encargo.** Sólo AÑADE rutas y todas las guardas se cumplen —el universo no encoge—, por eso es MENOR; pero el campo existe para decir POR QUÉ una fuente está en el universo de ESTE gate, y no lo dice |

---
# §3 · LOS DIECIOCHO CONTRATOS DE `F6`, UNO POR UNO

## §3.0 · Los ONCE CAMPOS: cuáles son de fila y cuáles son globales

`00-INDICE.md`:104 y `D109`(iii) afirman que los dieciocho llevan «**fuente, propietario, implementador, fase, entrada, salida, evidencia, escenario positivo, escenario negativo, condición de bloqueo y criterio exacto de cierre**». **Lo he contrastado contra la tabla, y el reparto es éste:**

```text
DE FILA, uno por contrato · SIETE   entrada · salida · evidencia · escenario POSITIVO ·
   (columnas 3-9 de la tabla         escenario NEGATIVO · condición de BLOQUEO ·
    de doc 11 L11758-11777)          criterio EXACTO de cierre

GLOBALES, uno para los dieciocho · CUATRO
   FUENTE          doc 11:11723-11726 — «TODO LO DE ESTA SECCIÓN ES DERIVADO DE `O20`,
                   VÍA `D109`», con la SEDE CANÓNICA nombrada y la regla de precedencia
                   («si difiere de la sede, manda la sede»)
   PROPIETARIO     doc 11:11753 — «Propietario global de la especificación: `SIS`»
   IMPLEMENTADOR   doc 11:11753 — «Implementador: `PLT`», con `VER` el dosier y `SEG` el
                   bloqueo, y el **Owner** como autoridad de aceptación indelegable
   FASE            doc 11:11755 — «**Fase de TODOS: `F6`.**»
```

**VEREDICTO SOBRE EL RECUENTO: los once campos ESTÁN.** Cuatro son globales, y su atribución es INEQUÍVOCA —«Fase de TODOS», «Propietario global»—, luego alcanzan a cada uno de los dieciocho sin ambigüedad. **No lo cuento como hallazgo**, y lo digo expresamente porque la lectura literal de «cada uno con…» invita a buscar once columnas y sólo hay nueve.

## §3.1 · Los dieciocho, con veredicto de COMPLETITUD

**Criterio que aplico a cada uno, y es el que `O20` §1 y el manifiesto §7 fijan:** ¿tiene los once campos? ¿es su criterio de cierre EXACTO y MEDIBLE sin interpretación humana? ¿se puede construir **sin volver a decidir arquitectura**?

| # | los once campos | criterio de cierre, ¿EXACTO y medible? | ¿construible sin decidir arquitectura? | **VEREDICTO** | qué le falta |
|---|---|---|---|---|---|
| `V6-01` | **SÍ**, 7 de fila + 4 globales | **SÍ** · «**cero** lecturas de lista con separador contenible» — es un censo con umbral 0 | **SÍ**. La solución ya está decidida y escrita: `_rutas_z()` del instrumento (`comprobar-…`:1999-2022) es la forma de referencia | **COMPLETO** | — |
| `V6-02` | **SÍ** | **SÍ** · «**todas** las lecturas con `-z`; ninguna decodificación laxa» — universal con contraejemplo único | **SÍ**. `-z`, `core.quotePath=false`, `errors="strict"` y control de truncamiento están escritos | **COMPLETO** | — |
| `V6-03` | **SÍ** | **SÍ** · «los **tres** casos producen ROJO y **nombran la causa**» — tres casos enumerados en la propia fila | **SÍ** | **COMPLETO** | — |
| `V6-04` | **SÍ** | **SÍ** · «el censo se DERIVA del código; **cero** lecturas fuera del canal» | **SÍ** | **COMPLETO EN SU OBJETO** | **Nada suyo. Pero DOS sedes le atribuyen una obligación AJENA** —la unificación de la fórmula de líneas— **que su texto no contiene: es `U1-04`** |
| `V6-05` | **SÍ** | **SÍ** · «**cero** rutas gobernadas exentas por preexistencia» | **SÍ**. `S1-02` ya fijó que la guarda juzga la MUTACIÓN y no la existencia | **COMPLETO** | — |
| `V6-06` | **SÍ** | **SÍ** · «las **seis** letras cubiertas; `R` y `C` por sus dos puntas» — cardinal cerrado y explícito | **SÍ** | **COMPLETO** | — |
| `V6-07` | **SÍ** | **SÍ** · «cada comprobación **declara** su referencia, y la declarada es la usada» — contraste declarado/usado, mecánico | **SÍ**. Los cuatro estados están nombrados: revisión base, `HEAD`, índice, árbol de trabajo | **COMPLETO** | — |
| `V6-08` | **SÍ** | **SÍ** · «**cero** comprobaciones cuyo veredicto MEJORE al confirmar» — es una propiedad monótona, medible | **SÍ**. Es la clase «inercia-tras-confirmar», ya diagnosticada cuatro veces | **COMPLETO** | — |
| `V6-09` | **SÍ** | **SÍ** · «**cero** rutas gobernadas sin guarda por su antigüedad» | **SÍ** | **COMPLETO** | — |
| `V6-10` | **SÍ** | **SÍ** · «el censo de zonas se DERIVA; **cero** zonas sin condición» | **SÍ**. El perímetro derivado ya existe: repositorio entero menos `.git` de la raíz y bytecode por contenido | **COMPLETO** | — |
| `V6-11` | **SÍ** | **SÍ** · «**cero** rutas del propio verificador exentas» | **SÍ**. La propiedad de auto-inclusión está enunciada sin ambigüedad | **COMPLETO** | — |
| `V6-12` | **SÍ** | **SÍ** · «el contraste se hace contra el **commit de creación**» — la referencia es única y derivable con `git log --diff-filter=A` | **SÍ**. Y ya existe implementación de referencia en `comprobar-…`:3400-3424 | **COMPLETO** | — |
| `V6-13` | **SÍ** | **SÍ** · «las **seis** formas con fixture positivo y negativo» — las seis van enumeradas en la propia fila | **SÍ** | **COMPLETO** | — |
| `V6-14` | **SÍ** | **SÍ** · «las **seis** con fixture positivo y negativo», enumeradas en la fila | **SÍ** | **COMPLETO** | — |
| `V6-15` | **SÍ** | **SÍ, y sólo el criterio** · «**cada** control de los tres gates presente, con su identificador de origen» — derivable de tres documentos NOMBRADOS | **SÍ** | **COMPLETO EN SU CRITERIO, INCOHERENTE EN SUS COLUMNAS** | Su escenario NEGATIVO exige «los **once** árboles» y su ENTRADA sólo da tres de los ocho gates; los once no se enumeran en ninguna sede. **Es `U1-08`** |
| `V6-16` | **SÍ** | **SÍ** · «el ejecutor **NO comparte identidad de escritura** con el runtime ADS (`O18`)» — es una propiedad binaria y verificable | **SÍ para lo que dice.** §11.8:8764-8899 lleva el contrato LARGO —dieciséis exigencias duras, reparto, autoridad, fase y condición de cierre— | **COMPLETO, PERO NO ENLAZADO** | §20 **no cita §11.8 ni una vez** (`sed -n '11721,11791p' \| grep '11\.8'` → nada). Un `F6` que construyera la raíz externa **desde §20** entregaría una fila donde §11.8 exige dieciséis condiciones. **Ver §3.2** |
| `V6-17` | **SÍ** | **SÍ** · «**cero** afirmaciones de integridad sostenidas sólo por el propio árbol» | **SÍ** | **COMPLETO, PERO NO ENLAZADO** | Lo mismo que `V6-16`, y además `C-20` le cuelga una obligación que no contiene: **es `U1-01`** |
| `V6-18` | **SÍ** | **SÍ, y es el más duro de los dieciocho** · «`falsos_verdes = 0` **y** `falsos_rojos = 0`, **medidos y publicados**» | **SÍ** | **COMPLETO** | — |

**RECUENTO DEL VEREDICTO, derivado de la tabla de arriba:** **18 de 18 tienen los once campos. 18 de 18 tienen criterio de cierre EXACTO y medible sin interpretación humana. 18 de 18 se pueden construir sin volver a decidir arquitectura.** Los defectos que sí encuentro —`U1-01`, `U1-04`, `U1-08`— **no son de los contratos: son de lo que OTRAS sedes les cuelgan encima y de la coherencia interna de una columna.**

## §3.2 · La raíz externa de confianza: ¿la cubren `V6-16` y `V6-17`?

**Respuesta: SÍ está su arquitectura COMPLETA, y NO está en §20 — está en §11.8, y §20 no la enlaza.**

```text
DÓNDE ESTÁ COMPLETA   §11.6 (8329-8626) el ancla documental de `O18(b)`, con sus 18 campos,
                      las obligaciones del revisor, las del adjudicador, lo que NO sustituye
                      y trece filas adversariales `X-O1`-`X-O13`
                      §11.7 (8627-8720) el ALCANCE HONESTO: `A` coherencia interna
                      IMPLEMENTADA · `B` identidad de la candidata IMPLEMENTADA Y TRANSITORIA ·
                      `C` resistencia a actor privilegiado **NO IMPLEMENTADA**, con sus seis
                      exclusiones LITERALES de la sede canónica
                      §11.8 (8722-8910) el CONTRATO del verificador externo: DIECISÉIS
                      exigencias duras —ejecución fuera, identidad propia, credenciales
                      separadas, firma verificable, protección de referencias, `force push`
                      prohibido Y DETECTADO, ancestry y fast-forward, descarga por SHA,
                      entorno limpio, verificación de hashes, resultado FUERA del árbol,
                      atestación vinculada al commit y al `tree` SHA, revocación y rotación,
                      SEPARACIÓN DE PODERES, recuperación, y SEIS pruebas negativas de
                      manipulación—, más PROPIETARIO `SIS`, EJECUTOR `PLT`, AUTORIDAD el
                      Owner, FASE `F6` OBLIGATORIA y CONDICIÓN DE CIERRE escrita
                      §11.9 (8912-8977) la regla de procedencia, con sus diez cláusulas
                      §16 `PN-19` (10517-10646) la presión sobre material APROBADO, con
                      materia mínima, propietario, fase, qué bloquea, qué NO, condición de
                      reversión y prueba posterior que FALLA HOY

QUÉ COBERTURA DAN     `V6-16` cubre la PRIMERA exigencia —ejecución desde fuera— y la
`V6-16` y `V6-17`     PROHIBICIÓN DE IDENTIDAD, que es la cláusula del Owner
                      `V6-17` cubre que ningún digest propio baste como prueba de sí mismo
                      **Las dos son CORRECTAS y ninguna de las dos es COMPLETA frente a
                      §11.8**: de las dieciséis exigencias duras, estas dos filas alcanzan
                      dos y media

QUÉ FALTA, EXACTO     **NO falta la arquitectura: falta el ENLACE.** §20 se presenta como
                      «el CONTRATO OBLIGATORIO DE `F6`» y como escrito «completo para que se
                      pueda construir sin volver a decidir nada», y **no remite a §11.8 en
                      ninguna de sus 71 líneas**. La MATRIZ DE CIERRE sí lo hace —la fila
                      `C-20` cita «§20 doc 11 · §11.6 · `O18`»— pero la matriz vive en el
                      checkpoint, no en el contrato
```

**Por qué NO lo elevo a insuficiencia por sí solo, y lo razono contra mi propio interés:** el manifiesto §7 exige insuficiencia si «falta una REGLA necesaria para construirlo». **La regla NO falta**: está entera en §11.8, con propietario, fase y condición de cierre, y §11.7 declara sin adorno qué está y qué no. Lo que falta es que §20 la ENLACE. Un `F6` que lea el corpus la encuentra; un `F6` que lea sólo §20 construye de menos. **Lo registro como defecto de completitud del ENLACE, no de la arquitectura**, y es lo que sostiene el veredicto «COMPLETO, PERO NO ENLAZADO» de las dos filas.

## §3.3 · ¿Cubren los dieciocho los OCHO puntos de `O20`? Contraste literal

| lo que `O20` §3 encarga a `F6` (sede canónica L382-392) | contrato(s) de §20 que lo cubren | ¿cubierto? |
|---|---|---|
| implementar el **VERIFICADOR DE ADMISIÓN** | `V6-05` `V6-09` `V6-10` `V6-11` + `V6-18` | **SÍ** |
| implementar la **RAÍZ EXTERNA DE CONFIANZA** que `O18` y `O19` ya exigen | `V6-16` `V6-17`, con §11.8 como contrato largo | **SÍ, con la salvedad del ENLACE (§3.2)** |
| cerrar las **LECTURAS GIT SEGURAS** | `V6-01` `V6-02` `V6-03` `V6-04` | **SÍ** |
| comprobar **MUTACIONES de ficheros nuevos y preexistentes** | `V6-05` `V6-08` `V6-09` | **SÍ** |
| tratar **CODIFICACIONES NO UTF-8** | `V6-02` `V6-03` `V6-13` | **SÍ** |
| comprobar **`A`, `M`, `D`, `R` y CAMBIOS DE TIPO** | `V6-06` `V6-14` (y las dos añaden `C`, que `O20` no nombra: **amplía en la dirección segura**) | **SÍ** |
| impedir que **LA DEFINICIÓN DE LO VERIFICADO Y LA REGLA DE ADMISIÓN se excluyan a sí mismas** | `V6-11` | **SÍ** |
| ejecutar la **MATRIZ ADVERSARIAL COMPLETA** | `V6-15` `V6-18` | **SÍ en el criterio**, con la incoherencia de columnas de `U1-08` |
| **CERTIFICAR** la implementación antes de declarar ADS operativo o iniciar la adopción de PesquerApp | §20.0:11746-11748 y §20.2:11787-11789 | **SÍ en §20**, y **NO en §18: es `U1-02`** |

**Los NUEVE encargos de `O20` §3 están cubiertos.** El único que se rompe fuera de §20 es el noveno, y se rompe en la sede del orden de construcción.

## §3.4 · ¿Queda alguna CLASE REPRODUCIDA sin contrato?

**Contraste mecánico de los 22 hallazgos del octavo gate contra la matriz de cierre, con el comando que el propio checkpoint publica:**

```bash
comm -23 <(grep -oE '^\| \*\*`C-[0-9]+`\*\*' docs/evolucion/29-…md | grep -oE 'C-[0-9]+' | sort -u) \
         <(awk '/^### La tabla de los 22/{t=1} t' docs/evolucion/CHECKPOINT-ADS-NEXT.md | grep -oE 'C-[0-9]+' | sort -u)
→ VACÍO
awk '/^### La tabla de los 22/{t=1} t' … | grep -oE '^\| `C-[0-9]+`' | sort -u | wc -l   → 22
… | grep -oE '\| (CORREGIDO_EN_F4c|CONTRATO_COMPLETO_PARA_F6|…) \|' | sort | uniq -c
→   8 CONTRATO_COMPLETO_PARA_F6      14 CORREGIDO_EN_F4c
```

**Los 22 están, cada uno con UN estado primario, y la cobertura contra el documento 29 sale VACÍA en la dirección que importa.** Y de los dieciocho contratos, **`V6-12` es el único que ningún hallazgo de los 22 cita** —lo verifiqué contrato a contrato—: **no es un defecto**, porque `V6-12` deriva de `O19` y de la sede, no del octavo gate.

**LA CLASE QUE SÍ QUEDA MAL COLGADA es la de `U1-01` y `U1-04`:** dos hallazgos con estado primario asignado **cuya `prueba_de_cierre` nombra contratos que no los contienen.** No es que la clase no tenga contrato: es que el contrato que se le atribuye es otro.

---
# §4 · LO QUE VERIFIQUÉ Y **NO** CAYÓ

**Lo escribo porque es verdad, y porque un informe que sólo publica lo que encuentra no permite pesar lo que no encontró.**

## §4.1 · `X63` y los contratos de `F6` anteriores NO se presentan como ejecutados

```bash
git grep -n 'X63' <commit del gate> -- docs/ kernel/
```

Ocho sedes. **Ninguna lo presenta como prueba ejecutada.** `00-INDICE.md`:94 dice «**`X63` es CONTRATO DE PRUEBA DE `F6`, no una prueba ejecutada ni una certificación presente**»; :98 y :101 lo repiten. Doc 11:1714 es su fila de contrato en §2.6.7; :5697-5699 dice «es un **contrato de prueba de `F6`** … **y no se ejecuta aquí**». **La única forma verbal en presente —«y `X63` la comprueba» en :5685— es la que el SEXTO GATE ya señaló (doc 27:1304) porque su aclaración llega doce líneas después; sigue igual, y no la cuento como hallazgo nuevo porque su clase ya está registrada y su sede está en el lote de `U2`.** El resto de familias —`X-A`–`X-H` (doc 11:3738-3741), `X-O1`–`X-O13` (:8571-8573), `NP-1`–`NP-11`, `X-S`— llevan todas su «**ninguna se ha ejecutado**» y su «**escribir el contrato de una prueba no es la prueba**».

## §4.2 · Ninguna sede presenta deuda de `F6` como implementación existente

Barrí el instrumento y sus sedes. **Lo contrario de lo que buscaba es lo que encontré:**

```text
verificacion/README.md:7-9   «**Qué NO es.** No es un gate, y no certifica nada. La escribe
                             quien aplica la corrección, que es exactamente lo que `F4c`
                             lleva doce tandas sin poder aceptar como prueba»
README.md:53-78              acota qué certifica un «N/N en verde» y qué NO: nueve de las
                             comprobaciones exigen repositorio CON HISTORIA y **fallan
                             CERRADO** sobre la materialización que la receta del sobre
                             prescribe. «**Un verde sobre el árbol desnudo NO es el verde que
                             un gate certifica**»
README.md:182-187            «**Lo que esta batería NO puede cerrar** … `M-04` **no es
                             satisfacible desde dentro del árbol**»
doc 11:11728-11731           «**NADA DE ESTA SECCIÓN SE HA EJECUTADO, Y NINGUNO DE SUS PUNTOS
                             ESTÁ IMPLEMENTADO** … y aquí se dice en la sección entera y no
                             sólo en una línea»
doc 11:11782-11789 (§20.2)   «NINGUNO … está implementado, ejecutado ni certificado»
                             «NINGUNO PUEDE CITARSE como capacidad existente, ni en un dosier,
                             ni en un informe, ni ante el Owner»
                             «NINGÚN VERDE DE LA BATERÍA INTERNA demuestra que alguno de ellos
                             esté construido»
manifiesto del gate:250-254  publica «38/38 en verde · EXIT=0» y a continuación: «**Y ESTAS
                             CIFRAS NO PRUEBAN QUE LOS CONTRATOS DE `F6` ESTÉN IMPLEMENTADOS**»
derivador:76-83              declara lo que NO cierra: «un documento numerado NUEVO cuyo H1
                             lleve una voz de NO-DICTAMEN y cuyo NOMBRE no diga dictamen …
                             **sale del universo con `rc=0`**» — y el sobre lo copia
```

**`git grep 'V6-'` fuera del documento 11** devuelve sólo el checkpoint (matriz de cierre y `M-04`) y una línea del derivador. **Ninguna es una afirmación de existencia.** No he encontrado un solo verde presentado como prueba de que un contrato de `F6` esté implementado, y lo digo tras buscarlo expresamente.

## §4.3 · La frontera de PesquerApp está escrita en DOS sedes normativas

`O20` §8 (sede canónica L419-420) · doc 11 §11.8:8866-8869 («construido **y PROBADO** antes de la **adopción permanente**») · §20.0:11746-11748 · §20.2:11787-11789 («sin MVP, sin piloto desechable y sin adopción parcial») · `PN-19`:10611-10615 · `00-INDICE.md`:104. **El bloqueo existe, es explícito y se repite.** Lo que `U1-02` denuncia **no es que falte el bloqueo: es que la sede del ORDEN DE CONSTRUCCIÓN lo omite y enumera una base sin él.** La distinción es mía y la mantengo.

## §4.4 · El remedio `S1-09` está aplicado ENTERO esta vez

El octavo gate (doc 29:108-113) midió que «**por TERCER gate consecutivo, el revisor que audita el instrumento no tiene asignadas §11.4, §11.6 ni §11.9**, y este gate es el primero cuyo manifiesto AFIRMA que sí las tiene. El remedio `S1-09` se aplicó a **un cuarto de su alcance**». **Esta vez no:** mi rango es `L1-L5200` ∪ `L8200-L11791`, y §11.4 está en **8253**, §11.6 en **8329**, §11.7 en **8627**, §11.8 en **8722** y §11.9 en **8912**. **Las cinco caen dentro de mi lote, y las he leído.** El manifiesto 8 daba a `T1` `L1-L5200` ∪ `L11380-L11717`, que no las contenía. **`C-05` está aplicado y es cierto.**

## §4.5 · El manifiesto y el sobre, impecables en lo que puedo medir

**83 filas contra el árbol que declaran: CERO discrepancias en línea y en SHA-256.** **La fila del derivador NO reincide, por quinta vez.** Las dos aritméticas DERIVAN de sus tablas y cierran contra las cifras del sobre (`9+74=83`, `28847+59051=87898`). `C-10` está aplicado y la columna LEÍDA/DELEGADA es **cierta**: las tres `LEÍDA` se corresponden con las filas 2, 3 y 6 del manifiesto de lectura de `T1` en el documento 29 (L537, L538, L541), donde `LEÍDO ÍNTEGRO` dice **SÍ**. Las 71 `DELEGADA` llevan el rótulo honesto —«**Nadie declaró haberla leído íntegra en ese gate**»—, que dice MENOS de lo que el manifiesto 8 decía con su «lectura íntegra certificada en». **Es una mejora medible, y consta.**

## §4.6 · La sede canónica del Owner no está amplificada

Obligación 6 cumplida. Contrasté las sedes derivadas que citan `O20` —`00-INDICE.md`:104, `D109` (`DECISIONES`:545), §20 del documento 11— contra el texto canónico. **§20 se rotula a sí misma PROYECCIÓN DERIVADA y publica su regla de precedencia** (11723-11726). **No he encontrado ninguna paráfrasis que AMPLÍE la autoridad de `O20`.** La única discrepancia de atribución que sí encontré es `U1-07`, y es de RÓTULO en el instrumento, no de contenido normativo.

## §4.7 · La arquitectura sustantiva que leí, y que NO cae

Leí íntegros §2 —protocolo transaccional, cinco fases, dos terminales, las diecisiete ventanas, las tres cajas, el contrato de identidad, la lápida y sus tres niveles de garantía—, §3 —los cuatro tipos, la matriz `tipo`×`fase` con su partición `34+20=54`, las tres capas de validación—, §4, §11 entero, §12-§19 y §20. **No he encontrado dos soluciones arquitectónicas incompatibles sin decidir.** Donde hay dos salidas posibles, el corpus **registra la presión y declara que elegir es del Owner** —`PN-13`, `PN-16`, `PN-17`, `PN-18`, `PN-19`, cada una con materia mínima, alcance, qué bloquea, qué NO bloquea, condición de reversión, propietario, fase y prueba posterior que FALLA HOY—. **Eso no es arquitectura sin decidir: es una decisión identificada, acotada y remitida a quien tiene autoridad.** `D104` —las cuatro vías de `<CAP>:revision`, con su algoritmo paso a paso, su discriminante estructural, sus dos salidas, sus contraejemplos, su error y sus 20 fixtures— es el ejemplo de lo que un contrato de `F6` completo parece.

---

# §5 · REFUTACIONES CONTRA MÍ MISMO

## `RF-1` · **NO CAYÓ** · «`U1-01` no vale: `C-20` puede diferirse porque `O20` §6 manda a `F6` los defectos de implementación»

`O20` §6 dice, literal: «los defectos de **IMPLEMENTACIÓN DEL VERIFICADOR** pasan a CONTRATOS OBLIGATORIOS de `F6`». `C-20` **no es un defecto de implementación del verificador**: es que el SOBRE —el ancla documental de `O18(b)`, que existe precisamente **para poder cerrar `F4c` sin el verificador**— no lleva un elemento que `O19` ordena que lleve. Diferirlo a `F6` es diferir a `F6` la condición que `O18` adoptó para no depender de `F6`. **Y aunque se admitiera el diferimiento, el defecto persiste: su `prueba_de_cierre` nombra `V6-16` y `V6-17`, y ninguno de los dos contiene la obligación.** La refutación no cae por un lado ni por el otro.

## `RF-2` · **CAYÓ A MEDIAS, Y ME OBLIGA A REBAJAR MI PROPIA REDACCIÓN** · «`U1-01` es de laboratorio: el sobre SÍ trae la declaración externa de la ratificación»

**Es cierto en su mitad, y lo recojo.** Mi sobre trae la DECLARACIÓN EXTERNA («EL TEXTO ANCLADO ARRIBA ES LA RESOLUCION RATIFICADA POR EL OWNER»), trae la RELACIÓN `O19`/`O18`, trae el digest de `O19` y trae **una frase entrecomillada del Owner**. §11.6 tiene esas tres como DECLARACIONES que acompañan a los campos, y **las tres se cumplen**. Lo que NO se cumple es el **primer elemento de la lista distinta** —«LO QUE CADA REVISOR RECIBE EXTERNAMENTE», doc 11:8449— que es **«el TEXTO de la ratificación del Owner»**, y que `O19`:315 ordena con esas palabras. **Rebajo la redacción: no es que el sobre calle la ratificación; es que entrega su DIGEST y su RESUMEN donde la resolución exige su TEXTO.** La severidad la mantengo, porque el remedio ya está determinado por `GG` como `C-20` y el corpus lo aparcó.

## `RF-3` · **CAYÓ** · «`U1-02` es falso: §20.2 y §11.8 bloquean PesquerApp, luego §18 no puede autorizarla»

**Cae, y por eso `U1-02` NO dice que PesquerApp pueda iniciarse.** Lo comprobé y lo escribí en §4.3: el bloqueo existe en seis sedes. Lo que `U1-02` afirma es más estrecho y sigue en pie: **§18 es la sede del ORDEN DE CONSTRUCCIÓN de `F6`, §15.4:9248 la designa sede de `O15`, y no contiene ni el nodo ni la mención.** Un `F6` que planifique desde §18 no encuentra allí la obligación mayor que `O20` le da. **Es un defecto de completitud de esa sede, no una autorización de PesquerApp**, y así queda escrito.

## `RF-4` · **NO CAYÓ** · «`U1-03` es pedantería: `O20` sí está trazada, en `00-INDICE.md` y en `D109`»

Es cierto que `O20` está trazada en el índice y en el registro. **Pero §15.4 no es una sede cualquiera: es la que declara «dónde queda cada resolución del Owner» DENTRO del documento 11, y escribe su propia regla y su propia sanción** —«Una resolución sin fila aquí es el defecto»—. Que el defecto lo declare la sede que lo comete no lo convierte en pedantería: lo convierte en un defecto **auto-declarado y medible con el comando que la sede publica**. Y el precedente es exacto: `P-26` corrigió aquí lo mismo para `O16`.

## `RF-5` · **CAYÓ A MEDIAS** · «`U1-05` no importa: el cardinal “dieciocho” de la cabecera es CIERTO hoy»

**Es cierto, y lo digo en el hallazgo.** `grep -cE '^### '` sobre §15.8 da 18, y la cabecera dice dieciocho. Lo que no cae es la razón: **es cierto PORQUE falta el bloque**. `P-03` describió exactamente esta forma —«la sede de la que la cifra decía derivarse estaba incompleta en dos tandas, luego la cifra no derivaba de nada»— y la sede escribió su remedio como regla: «toda tanda nueva abre su bloque **en el mismo acto** en que escribe sus decisiones». **La tanda de `O20` no lo abrió.** Rebajo la severidad a MEDIO por esta refutación, y no a MENOR, porque `D107` y `D108` sí lo hicieron y la asimetría es la reincidencia.

## `RF-6` · **NO CAYÓ** · «`U1-04` es una errata: `V6-04` habla de “ninguna vía paralela oculta”, y tres sedes de una fórmula son tres vías paralelas»

Lo consideré, y es la lectura más caritativa posible. **No se sostiene contra el texto:** `V6-04` acota su objeto en su primera palabra —«Inventario DERIVADO de todas las **lecturas Git**»—, su entrada es «el código del verificador», su salida es un «censo de **lecturas**», y su criterio de cierre es «**cero lecturas fuera del canal**». **Las cuatro columnas dicen “lectura Git”.** `lineas_de_blob` no es una lectura de Git: cuenta `\n` sobre un blob ya leído. Un `F6` que construyera `V6-04` según su texto **no tocaría la fórmula de líneas**, y el criterio de cierre saldría en verde con la divergencia intacta.

## `RF-7` · **CAYÓ** · «`U1-07` es un hallazgo contra el instrumento, y `O20` saca al instrumento del objeto del gate»

**Cae en su premisa mayor y por eso `U1-07` es clase `C` y MEDIO, no más.** `O20` saca del objeto la IMPLEMENTACIÓN del verificador, no la PROCEDENCIA de una atribución al Owner: esa es la materia de `O19`, que sigue entera y que el manifiesto §7 conserva como criterio («algún hallazgo se ha ESCONDIDO o SUAVIZADO»). Aun así **reconozco que el contenido atribuido es CIERTO**, que el propio fichero cita bien a `O19` en :3395, y que ningún veredicto depende de este rótulo. Lo dejo en MEDIO y no lo uso para el veredicto.

## `RF-8` · **NO CAYÓ** · «diez hallazgos, ninguno de clase `B`, y `O20` prohíbe declarar insuficiente por el verificador no implementado: luego esto es SUFICIENTE»

**Ninguno de mis diez se funda en el verificador no implementado, y lo declaré antes de la tabla.** `U1-01` es un incumplimiento VIVO de una orden del Owner en el sobre de ESTE gate, aparcado bajo contratos ajenos. `U1-04` es una obligación asignada a un contrato que no la contiene. Los dos son exactamente dos de los siete supuestos que el manifiesto §7 declara razón de insuficiencia: «falta **CRITERIO DE CIERRE** en algún contrato» y «algún hallazgo se ha **ESCONDIDO o SUAVIZADO**». **La refutación no cae.**

## `RF-9` · **CAYÓ, Y CONTRA MÍ** · «`U1-08` invalida `V6-15`: sin saber cuáles son los once, la matriz adversarial no especifica una clase reproducida»

**Cae, y lo digo aunque me quitaba el hallazgo más vistoso.** El manifiesto §7 exige insuficiencia si «la MATRIZ ADVERSARIAL **no especifica una clase reproducida**». `V6-15` **sí especifica**: su criterio EXACTO de cierre es «cada control de los tres gates presente, **con su identificador de origen**», y los tres gates son documentos NOMBRADOS cuyos controles llevan identificador —el documento 29 los enumera en su §3.3, «LOS DIECISIETE CONTROLES ADVERSARIALES», tabla por tabla—. **La clase está especificada y `V6-15` se puede construir.** Lo que queda es una incoherencia entre su columna de escenario negativo y su columna de entrada. **Rebajo `U1-08` de lo que iba a ser GRAVE a MENOR-alto, lo dejo en MEDIO por prudencia, y NO lo uso como razón de insuficiencia.**

## `RF-10` · **NO CAYÓ** · «el gate es INVÁLIDO: mi sobre no cumple §11.6, luego no ancla nada»

Lo pensé, y es la refutación más severa que me cabía. **No cae, pero tampoco invalida.** §11.6 y `O19` fijan que el gate FALLA CERRADO si **la sede canónica no coincide con la huella recibida externamente**, y **coincide**: la recalculé en los dos commits y contra los cuatro digests. El disparador de invalidez es la DISCREPANCIA, no la incompletitud de la lista. **Por eso `U1-01` es BLOQUEANTE de la SUFICIENCIA y no de la VALIDEZ**, y el gate es VÁLIDO. Lo digo explícitamente para que el adjudicador no tenga que deducirlo.

---

# §6 · LO QUE MI LOTE NO CUBRE, SIN ADORNO

```text
1  `L5201-L8199` DEL DOCUMENTO 11 —2 999 líneas— son de `U2` y NO los he leído. Ahí viven
   §5 (auditoría, cobertura y `contrato-de-aspecto`), §6 (adaptadores), §7 (runtime), §8
   (los cuatro macrocircuitos) y §9 (certificación, incluida la FASE 0 de `O17` en §9.6).
   **Nada de lo que afirmo depende de ese tramo**, salvo las dos citas de `X63` en :5685 y
   :5697, en las que entré expresamente y que declaro en §1.2. **No juzgo §9.6, que es la
   sede de `O17`, ni la composición de rutas de §8.**

2  `CHECKPOINT-ADS-NEXT.md` (5 339 líneas) es de `U2`. **La MATRIZ DE CIERRE de los 22 vive
   ahí**, y yo la he contrastado sólo con los comandos que ella misma publica y con la
   resta contra el documento 29. **No he leído el checkpoint íntegro y no juzgo el resto de
   su contenido**: ni el bloque de estado, ni `C-L.1`–`C-L.13`, ni los partes de tanda.

3  `DECISIONES-Y-CONTRADICCIONES.md` (1 402 líneas) es de `U2`. He leído `D109` (:545) y he
   derivado sus cabeceras `### \`O`. **No he verificado el resto del registro**, ni la
   coherencia de `D1`–`D108`, ni las proyecciones de `O1`–`O16`.

4  `00-INDICE.md` es de `U2`. Lo he citado (:94, :97, :98, :100, :101, :103, :104) y **no lo
   he leído íntegro**.

5  **NO he intentado construir un árbol adversarial que pase en verde, y no me lo encargaron.**
   `O20` lo saca del objeto de este gate y lo contrata para `F6` en `V6-18`. **Por tanto no
   afirmo nada sobre si existe hoy una puerta más**: el octavo gate encontró la undécima y
   este gate no la ha vuelto a medir. Lo digo para que nadie lea mi silencio como una
   ausencia de puertas.

6  **NO he ejecutado la batería ni el runner.** Las cifras de validación que el manifiesto §9
   publica —38/38, 13/13, `T147` superada— **NO las he reproducido**, y no las uso para nada.
   `O20` §5 dice que un verde suyo no demuestra nada de `F6`, y este informe no se apoya en
   ninguno.

7  **NO he leído los documentos 10 y 12-28**, que el manifiesto declara AGOTADOS. Entré en el
   27 y el 28 sólo para contar menciones de «adversarial», y en el 29 —que sí es de mi lote—
   lo he leído por sus secciones sustantivas y su estructura completa, abriéndolo EL ÚLTIMO
   como el lote ordena.

8  **NO puedo comprobar que el emisor y el derivador que CORRIERON sean los publicados.** El
   propio sobre lo declara en su obligación 5 y `Z-11` lo midió. Lo que sí comprobé son sus
   SHA-256 en los DOS commits, y coinciden.

9  **NO puedo verificar que `O20` sea el texto que el Owner emitió.** El sobre lo declara:
   «quien pueda escribir el repositorio puede escribir la sede». Es la limitación TRANSITORIA
   de `O18` y sigue vigente hasta el verificador externo de `F6`. **Mi anclaje de `O20` prueba
   que el texto no ha cambiado entre el commit auditado y lo que recibí fuera del árbol, y
   NADA MÁS.**

10 `ASIGNADO − LEÍDO = ∅` en mi lote, y lo declaro contra mi propio interés en §1.2. Si el
   adjudicador recalcula y encuentra un tramo que yo no abrí, **la regla de cierre de `C-L.5`
   excluye la suficiencia por sí sola y mi dictamen no la salva.**
```

---

# §7 · MI RESPUESTA, EN UNA FRASE

> **¿Es la arquitectura de `F4c` suficiente para construir, y están completos los contratos de `F6`?**
>
> **La arquitectura es suficiente para construir y los DIECIOCHO contratos de `V6-01` a `V6-18` están completos —once campos, criterio de cierre exacto y ninguno exige volver a decidir arquitectura—, pero los contratos ENTREGADOS a `F6` no lo están: `C-20` aparca como deuda de `F6`, bajo `V6-16` y `V6-17` que no lo contienen, un incumplimiento VIVO de la orden de `O19` sobre el sobre de este mismo gate; `C-11` cuelga de `V6-04` una obligación cuyo objeto `V6-04` no menciona; y §18 —la sede del orden de construcción de `F6`— no contiene el verificador ni la raíz externa y enumera la base de la adopción de PesquerApp sin ellos.**

```text
VEREDICTO           **INSUFICIENTE PARA F5**
VALIDEZ DEL GATE    **VÁLIDO** — los dos digest, los dos árboles, el manifiesto, el emisor,
                    el derivador, la sede canónica y sus cuatro resoluciones reproducen
RAZONES, y son DOS  `U1-01` BLOQUEANTE · `U1-04` GRAVE — las dos son «falta CRITERIO DE
                    CIERRE en algún contrato» y «un hallazgo escondido o suavizado», que el
                    manifiesto §7 declara razón de insuficiencia
                    `U1-02` y `U1-03` GRAVES acompañan, y por sí solas no lo decidirían
LO QUE **NO** ES    **NINGUNA** de mis razones es que el verificador de `F6` no esté
RAZÓN               implementado. Esa ausencia es ESPERADA, está DECLARADA y no la uso
¿ALGO AL OWNER?     **NO.** Ninguno de mis diez es de clase `B`. Los diez se cierran con
                    material que el corpus ya tiene escrito, y ninguno reinterpreta `O17`,
                    `O18`, `O19` ni `O20`
```

## DISCIPLINA — declaración de cierre

```text
NO HE MODIFICADO EL REPOSITORIO        `git status --porcelain` VACÍO al abrir y al cerrar
NI UN COMMIT, NI UNA REFERENCIA        cero commits, cero ramas, cero tags, cero pushes
NO PROPONGO CORRECCIONES               ninguna, y el encargo lo prohíbe
TODA AFIRMACIÓN CON FICHERO Y LÍNEA    y toda cifra con el comando que la deriva
NINGUNA HUELLA ABREVIADA A MANO        las que aparecen son salida de `sha256sum`
`ASIGNADO − LEÍDO`                     ∅, declarado contra mi propio interés en §1.2
NO HE VISTO EL DICTAMEN DE `U2`        ni él el mío
```

---

## §B · DICTAMEN DEL REVISOR `U2` — TRANSCRIPCIÓN LITERAL

# INFORME DEL REVISOR INDEPENDIENTE `U2` — GATE ARQUITECTÓNICO FINAL DE `F4c`

Revisor `U2`. Contexto limpio: no he escrito ninguna fuente de este corpus, no he aplicado
ninguna corrección y no he participado en ningún gate anterior. No he modificado el
repositorio: `git status --porcelain` sigue vacío al cerrar (§4).

## §0 · EL SOBRE, EMBEBIDO ENTERO Y BYTE A BYTE, Y SUS SEIS OBLIGACIONES

### §0.1 · El sobre recibido, literal

~~~text
SOBRE DE ANCLA · emitido por el coordinador ANTES de crear a ningún revisor
==============================================================================
  REPOSITORIO             git@github.com:JoseLopezGonzalez/ads-kernel.git
  ARBOL DE TRABAJO        `git status --porcelain` VACÍO al emitir, y eso es todo lo
                          que prueba: no había modificaciones VISIBLES para `git
                          status`. Ver la obligación 5 y los SHA-256 del emisor
  TODO LO DE ABAJO SE LEE DE COMMITS con `git show <commit>:<ruta>`. Ni un byte
  del directorio de trabajo de quien emite
------------------------------------------------------------------------------
  REF REMOTA CANDIDATA    refs/heads/review/f4c-o20-frontera-de-fase-candidate-20260901
  COMMIT CANDIDATO        7aeed6aa3a3eae1133f57a08d757020e62197b3d
  ARBOL CANDIDATO         0a8f5804e37bfb4ea05deabd18659cd2864f1d73
  REF REMOTA DEL GATE     refs/heads/gate/f4c-arquitectonico-final-20260901
  COMMIT DEL GATE         ebd52d9125fb740c1c7a7606f82876b8433ef6a8
  ARBOL DEL GATE          06257a734e15af67142759029ae429839716d2ea
  RUTA DEL MANIFIESTO     docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md
  SHA-256 DEL MANIFIESTO  ff4116703b648586bae866cd259f37f7800088e8fe2148b4f4224b466322fc13   (en el commit del gate)
  ASIGNACIONES            14   DERIVADAS de las 9 filas de reparto del manifiesto,
                          no recibidas por parámetro
------------------------------------------------------------------------------
LOS DOS ARBOLES, CADA UNO DERIVADO DE SU PROPIO COMMIT CON SU PROPIO DERIVADOR.
El derivador es FILA DE SU PROPIO UNIVERSO y el commit del gate lo toca: por eso el
sobre publica LOS DOS y no mezcla ni un campo. El gate anterior yuxtapuso el árbol
de la candidata con las cifras del árbol del gate, y eran insatisfacibles.

                          CANDIDATA                                                         GATE
  COMMIT                  7aeed6aa3a3eae1133f57a08d757020e62197b3d                          ebd52d9125fb740c1c7a7606f82876b8433ef6a8
  SHA-256 DEL DERIVADOR   0eca7103833110c32b4d2fda23acf54a04c905e40e98b6fda102e5d2dd5f312e  0eca7103833110c32b4d2fda23acf54a04c905e40e98b6fda102e5d2dd5f312e
  SHA-256 DEL EMISOR      8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453  8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453
  FUENTES OBLIGATORIAS    83                                                                84
  LINEAS OBLIGATORIAS     87898                                                             88156
  DIGEST DEL UNIVERSO     d12b64b91ad313557df6bdf1c2a38f2ccb2d8a264b3f12553ada8e3a56ed551f  868fb198e8b7699fc2b1161d76b29f804a911e2e6e8ba6e7712a7596bbef464d


  SHA-256 DEL EMISOR QUE HA CORRIDO ESTE SOBRE: 8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453
  COINCIDE con el del commit del gate. El revisor puede rehacer este contraste:
    git show ebd52d9125fb740c1c7a7606f82876b8433ef6a8:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum

  RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: 2
    docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md  AUSENTE → ff4116703b64
    docs/evolucion/00-INDICE.md  1077403f421f → 0c6587c2298a

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
  RESOLUCIONES ANCLADAS   4, DERIVADAS de la sede y no escritas: O17 (85 lineas) · O18 (111 lineas) · O19 (81 lineas) · O20 (107 lineas)
  EXIGIDAS POR `O19`      O17 · O18 · O19   sin una sola de ellas NO HAY SOBRE

                          CANDIDATA (COMMIT AUDITADO)                                       GATE
  SHA-256 DE LA SEDE      4e4081efb29dcd2f095879b07104e4e169a46b497d11213256541fd6599a4e3a  4e4081efb29dcd2f095879b07104e4e169a46b497d11213256541fd6599a4e3a
  DIGEST DE `O17`         0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125  0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125
  DIGEST DE `O18`         ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353  ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
  DIGEST DE `O19`         d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632  d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632
  DIGEST DE `O20`         c3804cdec674b140a508f84a1b19a463efe27cd31b108b443271d34dab1906f3  c3804cdec674b140a508f84a1b19a463efe27cd31b108b443271d34dab1906f3

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
  git show 7aeed6aa3a3eae1133f57a08d757020e62197b3d:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O17`/)} p' | sha256sum

  ── `O18` → ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353
  git show 7aeed6aa3a3eae1133f57a08d757020e62197b3d:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O18`/)} p' | sha256sum

  ── `O19` → d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632
  git show 7aeed6aa3a3eae1133f57a08d757020e62197b3d:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O19`/)} p' | sha256sum

  ── `O20` → c3804cdec674b140a508f84a1b19a463efe27cd31b108b443271d34dab1906f3
  git show 7aeed6aa3a3eae1133f57a08d757020e62197b3d:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk '/^# /{p = ($0 ~ /^# `O20`/)} p' | sha256sum

  ── LA SEDE ENTERA → 4e4081efb29dcd2f095879b07104e4e169a46b497d11213256541fd6599a4e3a
  git show 7aeed6aa3a3eae1133f57a08d757020e62197b3d:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
==============================================================================
  EMITIDO                 2026-09-01 08:19:24 +0200
  EMISOR                  Jose Lopez Gonzalez (jose@congeladosbrisamar.es), coordinador nombrado del gate arquitectonico final
  DECISION QUE LO EXIGE   O18 · alternativa (b) · propagada por D108
  ENTREGA                 este sobre se entrega a cada revisor DENTRO de su encargo
                          y ANTES de que empiece a leer. NO se obtiene leyendo el
                          repositorio que se audita
==============================================================================
COMO SE RECALCULA CADA DIGEST, para que el revisor no tenga que fiarse. Reproduce el
digest BYTE A BYTE; si no lo reproduce, el sobre o el árbol están mal, y en ese orden:

  ── ARBOL CANDIDATO → d12b64b91ad313557df6bdf1c2a38f2ccb2d8a264b3f12553ada8e3a56ed551f
  C=7aeed6aa3a3eae1133f57a08d757020e62197b3d
  d=$(mktemp -d)
  GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
  rm -rf "$d"

  ── ARBOL DEL GATE  → 868fb198e8b7699fc2b1161d76b29f804a911e2e6e8ba6e7712a7596bbef464d
  C=ebd52d9125fb740c1c7a7606f82876b8433ef6a8
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
~~~

SHA-256 del sobre tal como lo recibí: c39de894c21f25a22ef5789cfa0a5a097ff3e440ffa7e8c9d654caa969792282

### §0.2 · Las seis obligaciones, cumplidas una a una

**OBLIGACIÓN 1 — recalcular LOS DOS digest antes de leer nada.** Hecho, antes de abrir
ninguna fuente, con la receta literal del sobre y con `python3` 3.12.14.

```bash
for C in 7aeed6aa3a3eae1133f57a08d757020e62197b3d ebd52d9125fb740c1c7a7606f82876b8433ef6a8; do
d=$(mktemp -d)
GIT_INDEX_FILE="$d/idx" git read-tree "$C"
GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
  while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
  awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
rm -rf "$d"; done
```

```text
7aeed6aa…  fuentes=83  lineas=87898  digest=d12b64b91ad313557df6bdf1c2a38f2ccb2d8a264b3f12553ada8e3a56ed551f
ebd52d91…  fuentes=84  lineas=88156  digest=868fb198e8b7699fc2b1161d76b29f804a911e2e6e8ba6e7712a7596bbef464d
```

LOS DOS REPRODUCEN BYTE A BYTE, y también reproducen las dos cifras de fuentes y las dos
de líneas que el sobre publica por separado para cada árbol. **El gate NO es inválido por
esta vía.**

**OBLIGACIÓN 2 — leer el manifiesto EN EL COMMIT DEL GATE y comprobar su SHA-256.**

```bash
git show ebd52d9125fb740c1c7a7606f82876b8433ef6a8:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md | sha256sum
→ ff4116703b648586bae866cd259f37f7800088e8fe2148b4f4224b466322fc13
```

Coincide con el sobre. Leído íntegro (256 líneas) desde el commit del gate, nunca del árbol
de trabajo.

**OBLIGACIÓN 3 — cada fila del manifiesto declara un árbol; contrastar contra ESE árbol; y
mirar PRIMERO la fila del propio derivador.**

La fila del derivador es la fila 6 de §4 del manifiesto (L81): SHA-256 declarado
`0eca7103833110c32b4d2fda23acf54a04c905e40e98b6fda102e5d2dd5f312e`, 846 líneas.

```bash
git show 7aeed6aa…:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum
→ 0eca7103833110c32b4d2fda23acf54a04c905e40e98b6fda102e5d2dd5f312e
git show ebd52d91…:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum
→ 0eca7103833110c32b4d2fda23acf54a04c905e40e98b6fda102e5d2dd5f312e
```

**LA FILA DEL DERIVADOR ES VERDADERA EN LOS DOS ÁRBOLES.** El derivador no cambió entre la
candidata y el gate, de modo que la falsificación de `U-02` y su reincidencia `X-06` NO se
repite aquí. Y las 83 filas enteras se comprobaron mecánicamente contra el árbol de la
candidata —que es el que §4 y §5 declaran—:

```bash
awk -F'|' 'NF>6 && $3 ~ /`docs|`kernel/ {gsub(/[` ]/,"",$3);gsub(/ /,"",$4);gsub(/[` ]/,"",$5);print $3"\t"$4"\t"$5}' MANIFIESTO.md \
| while IFS=$'\t' read -r r l h; do
    ah=$(git show "7aeed6aa…:$r"|sha256sum|cut -d' ' -f1); al=$(git show "7aeed6aa…:$r"|wc -l)
    [ "$ah" != "$h" -o "$al" != "$l" ] && echo "MISMATCH $r"; done
→ (sin salida)   83 filas · 0 discrepancias, ni de SHA-256 ni de conteo de líneas
```

**OBLIGACIÓN 4 — las rutas en que difieren los UNIVERSOS no son las rutas en que difieren
los ÁRBOLES.** El sobre publica 2 rutas de divergencia de universo. La divergencia real de
árboles es mayor:

```bash
git diff --name-only 7aeed6aa3a3eae1133f57a08d757020e62197b3d ebd52d9125fb740c1c7a7606f82876b8433ef6a8
→ docs/evolucion/00-INDICE.md
  docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md
  kernel/operativo/pruebas/evidencia/fuentes-salida.txt
  kernel/operativo/pruebas/evidencia/negativos-salida.txt
  kernel/operativo/pruebas/evidencia/referencias-salida.txt
```

5 rutas, de las que 2 son las del universo. Las otras 3 son evidencia reejecutada, y el
manifiesto las nombra explícitamente como fuera del universo en su §6 (L192: «LA EVIDENCIA
REEJECUTADA — no son fuentes obligatorias: no entran en el universo»). **La advertencia del
sobre se cumple: el manifiesto NO afirma nada sobre ellas sin decir de qué árbol habla.**

**OBLIGACIÓN 5 — `git status --porcelain` vacío prueba poco; lo que SÍ se comprueba son los
SHA-256 del emisor y del derivador en LOS DOS commits.**

```bash
git show ebd52d91…:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum
→ 8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453
git show 7aeed6aa…:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum
→ 8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453
```

Coinciden con el sobre y entre sí. Y con el derivador de la obligación 3, los cuatro valores
que el sobre publica en su tabla de dos columnas son ciertos.

**OBLIGACIÓN 6 — recalcular los digest de la SEDE CANÓNICA y contrastar CADA sede derivada
que cite una resolución. Una paráfrasis que AMPLÍE o DEBILITE el texto canónico es un
hallazgo.**

```bash
for C in 7aeed6aa… ebd52d91…; do
  git show $C:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
  for O in O17 O18 O19 O20; do
    git show $C:docs/owner/ADS-OWNER-RESOLUCIONES.md | awk -v o="^# \`$O\`" '/^# /{p=($0~o)} p' | sha256sum; done; done
```

| | esperado (sobre) | candidata | gate | líneas |
|---|---|---|---|---|
| SEDE entera | `4e4081ef…9a4e3a` | idéntico | idéntico | 444 |
| `O17` | `0cc5b9b5…4e6125` | idéntico | idéntico | 85 |
| `O18` | `ab9d9447…6ed0353` | idéntico | idéntico | 111 |
| `O19` | `d86a9455…fddf632` | idéntico | idéntico | 81 |
| `O20` | `c3804cde…1906f3` | idéntico | idéntico | 107 |

**LOS CINCO DIGEST REPRODUCEN, en los dos commits.** Y los cuatro conteos de líneas que el
sobre publica —85 · 111 · 81 · 107— se derivan también. La sede queda ANCLADA: `O17`, `O18`,
`O19` y `O20`. El contraste cláusula a cláusula de la PROYECCIÓN va en §2 (`U2-01`…) y en
§4.

**Ninguna de las seis obligaciones falla. EL GATE NO ES INVÁLIDO.**

## §1 · MANIFIESTO DE LECTURA, Y LA RESTA CONTRA MI PROPIO INTERÉS

**Todo se leyó del COMMIT CANDIDATO `7aeed6aa…`**, extraído con `git show`, y no del árbol de
trabajo. Importa para `00-INDICE.md`, que es una de las dos rutas en que los universos
difieren: el árbol de trabajo (HEAD = commit del gate) publica `0c6587c2298a…`/243 líneas, y
lo que se me asigna es `1077403f421f…`/241, que es el de la candidata. **Leí el de la
candidata**, que es el objeto del gate.

| # | ruta | líneas | SHA-256 recalculado por mí | alcance asignado | LEÍDO |
|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 241 | `1077403f421f5609a6b5393c5f86b77054fc426b7daa64947fc3ed1eb1d69118` ✔ | ÍNTEGRO | ÍNTEGRO |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11791 | `4ad648c17b0e753fcd0373bcbe8922e76593e0968f9c36a9a8ae693fecf0c815` ✔ | `L5201`–`L11791` | ÍNTEGRO |
| 3 | `docs/evolucion/29-OCTAVO-GATE-DE-CERTIFICACION-F4C.md` | 4197 | `0b9064490c8dd68ec7c50ed87778d31ab8ab5360c966642113367a0eeba2e5ac` ✔ | ÍNTEGRO · EL ÚLTIMO | ÍNTEGRO |
| 4 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 5339 | `edba17ec59bf60e85a0c70a3d49b90d3a2641d4baaa3b65e50d65a04b00d6828` ✔ | ÍNTEGRO | ÍNTEGRO |
| 5 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 444 | `4e4081efb29dcd2f095879b07104e4e169a46b497d11213256541fd6599a4e3a` ✔ | ÍNTEGRO | ÍNTEGRO |
| 6 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1402 | `07ddfcbe05f8b56f9846bba38a29a6c5dabc38796d3c4bc3bf075903e453bf01` ✔ | ÍNTEGRO | ÍNTEGRO |

```bash
for f in <las seis>; do git show 7aeed6aa…:$f | sha256sum; git show 7aeed6aa…:$f | wc -l; done
→ los seis SHA-256 y los seis conteos de línea reproducen los del lote, uno a uno
```

**LA RESTA, `ASIGNADO − LEÍDO` = ∅.** Seis fuentes asignadas, seis leídas en su alcance
declarado. Del documento 11 me tocan `L5201`–`L11791`, **6591 líneas**, y las abrí todas por
rangos consecutivos que cubren desde `§4.3` (cola) hasta el final de `§20.2`. Las anclas de
región separada que declaro, para que se pueda comprobar que no salté tramos:

```text
PRIMERA SECCIÓN SUSTANTIVA DE MI RANGO   L5224  «# 5 · Sistema de auditoría y mejora continua»
ANCLA MEDIA 1                            L7718  «## 9.6 · `gate:sistema-conforme` …»
ANCLA MEDIA 2                            L9662  «# 16 · Presiones normativas para F5»
ANCLA MEDIA 3                            L10758 «# 18 · Orden de construcción para F6»
ÚLTIMA SECCIÓN SUSTANTIVA                L11779 «## 20.2 · Lo que esta sección NO dice…»
```

**ORDEN DECLARADO.** El documento 29 se abrió EL ÚLTIMO, como manda el lote. Antes de
abrirlo sólo se ejecutó sobre él **un `grep -oE` de identificadores**, y únicamente porque es
el comando que la propia matriz del checkpoint publica para probar su cobertura (§3); no se
leyó ni una línea de su contenido hasta cerrar las otras cinco fuentes.

**DECLARACIÓN CONTRA MI PROPIO INTERÉS.** Del documento 11 leí `L5201`–`L11791`. **`L1`–`L5200`
NO son míos y NO los he leído**: cuando cito §0 (L13-L14) o §2.6.7 lo hago como CORROBORACIÓN
de una regla que vive dentro de mi rango, y lo digo en cada caso. Ese tramo es de `U1`.

## §2 · HALLAZGOS

> **Convenio de clases, el que `DD-20` fija en su sede** (`CHECKPOINT`:3678-3715 y 3701-3715):
> `A` el defecto está EN EL CORPUS y la batería lo da por bueno —confirmado o no, es
> irrelevante— · `B` exige una decisión NUEVA del Owner · `C` corromper la REFERENCIA contra
> la que se compara, **NO exigible dentro de `F4c`**. **Ninguno de los míos es `B` ni `C`.**
> Todo se mide sobre el ÁRBOL DE LA CANDIDATA `7aeed6aa…` salvo donde digo lo contrario.
>
> **NINGUNO de mis hallazgos dice que el verificador de `F6` no esté implementado.** Esa
> ausencia es esperada, está declarada y no la uso como razón de nada (§4).

| id | severidad | clase | sede fichero:línea | qué afirma | qué dice el árbol, con comando y salida | qué se sigue |
|---|---|---|---|---|---|---|
| **`U2-01`** | **GRAVE** | **A** | `CHECKPOINT-ADS-NEXT.md`:**4076**, fila `C-20` de la MATRIZ DE CIERRE, contra `11-ARQUITECTURA-INTEGRADA.md`:**8453-8459** y contra la SEDE CANÓNICA `docs/owner/ADS-OWNER-RESOLUCIONES.md`:**315-317** | La fila da a `C-20` estado primario `CONTRATO_COMPLETO_PARA_F6`, **fase `F6`**, propietario «`PLT` implementa · Owner acepta» y **prueba de cierre `V6-16` · `V6-17`** | **`C-20` es `T2-11` del documento 29** (`29-…md`:2014): *el SOBRE no lleva el TEXTO de la ratificación del Owner*, que es **el PRIMERO de los seis** de la lista que §11.6 L8453-8459 rotula «**y es la lista entera**» y que la SEDE L315-317 ordena con las palabras del Owner: «*Cada revisor **debe** recibir externamente: **el texto de esta ratificación** · …*». **REPRODUCE EN EL SOBRE DE ESTE MISMO GATE**, el que yo he recibido: `wc -l SOBRE.txt` → **201**; `grep -c 'RATIFICO EL TEXTO AMPLIO'` → **0**; `'LA RATIFICACION QUEDA CERRADA'` → **0**; `'Sobre las seis sedes'` → **0**; `'append-only'` → **0**. Sólo viaja **una** frase entrecomillada (`grep -c 'la omision esta en la transcripcion del coordinador'` → **1**). Y las dos pruebas de cierre asignadas **no lo prueban**: `V6-16` (doc 11 L11775) exige «*la prueba se ejecuta desde una RAÍZ DE CONFIANZA EXTERNA*» y `V6-17` (L11776) «*ningún digest calculado por el mismo árbol basta*» — **ninguna de las dos menciona el contenido del sobre ni el texto del Owner** | **UN HALLAZGO VIVO DE `F4c` SE HA MOVIDO A `F6` CON UN CRITERIO DE CIERRE QUE NO PUEDE CERRARLO.** El sobre lo emite **el coordinador de `F4c`** y §11.6 le da fase «**ya, para el PRÓXIMO gate de `F4c`**» (L8597-8599). `F6` puede implementar y certificar `V6-16` y `V6-17` enteros y el sobre seguirá sin llevar el texto que el Owner ordena entregar. Es a la vez **hallazgo SUAVIZADO al cambiarle la fase** y **contrato sin CRITERIO DE CIERRE**, los dos disparadores que §7 del manifiesto (L223 y L222) nombra |
| **`U2-02`** | **GRAVE** | **A** | `11-ARQUITECTURA-INTEGRADA.md`:**11774**, fila `V6-15` de §20.1 | ENTRADA: «documentos 27, 28 y 29» · QUÉ DEBE DEMOSTRAR: «los controles adversariales del **SEXTO, SÉPTIMO y OCTAVO** gate quedan como FIXTURES OBLIGATORIOS» · CRITERIO EXACTO DE CIERRE: «**cada** control de **los tres gates** presente». Y su ESCENARIO NEGATIVO exige «**los once árboles** vuelven a dar ROJO, uno a uno» | Los once árboles **no viven en tres documentos**. Derivado del propio corpus: `grep -nE 'EL (OCTAVO\|NOVENO\|DÉCIMO\|UNDÉCIMO) [ÁA]RBOL' CHECKPOINT-ADS-NEXT.md` → **OCTAVO** = `DD-01`, QUINTO GATE, **documento 26** (L3854) · **NOVENO** = `EE-01`, SEXTO GATE, doc 27 (L3944) · **DÉCIMO** = SÉPTIMO GATE, doc 28 (L66) · **UNDÉCIMO** = OCTAVO GATE, doc 29 (L4305). Los árboles **1 a 8 son de gates anteriores al sexto**, y **ninguno de sus documentos está en la ENTRADA de `V6-15`** | **LA FILA SE CONTRADICE A SÍ MISMA Y ESTRECHA A `O20`.** `O20` §3 (sede L390) manda «*ejecutar la MATRIZ ADVERSARIAL **COMPLETA**»*; `V6-15` la acota a tres gates. Un `F6` que satisfaga su criterio de cierre al pie de la letra reproduce **3 de los 11** y **el octavo árbol —el del PERÍMETRO, `DD-01`, doc 26— queda fuera del contrato**. Es «**la matriz adversarial no especifica una clase reproducida**», el disparador literal de §7 del manifiesto (L224), y una **paráfrasis que DEBILITA** el texto canónico (obligación 6 del sobre) |
| **`U2-03`** | **GRAVE** | **A** | `11-ARQUITECTURA-INTEGRADA.md`:**11755-11756** («**Fase de TODOS: `F6`**») y **11775-11776** (`V6-16`, `V6-17`), contra **§16 `PN-19`** L10605-10609 y §11.8 L8896-8899 | §20.1 declara para los DIECIOCHO puntos, sin excepción: «**Fase de TODOS: `F6`**. Estado de todos: CONTRATADO, NO IMPLEMENTADO, NO EJECUTADO». §20 entero **no nombra `PN-19` ni una vez** | Barrido sobre §20 (L11721-11791): `grep -nE 'PN-\|F5\|§11\.8\|§11\.6\|C8\|\(g\)'` → **una sola línea**, y es «`O18` declara indelegable» (L11755). **`§20` no cita ninguna sede fuera de `O18`, `O20` y `D109`**: `grep -oE '§[0-9.]+\|`[A-Z]+-[0-9]+`\|`O[0-9]+`\|`D[0-9]+`'` → `` `D109` `` `` `O18` `` `` `O20` ``. Y `PN-19` (L10605-10609) dice de esa misma materia: «FASE **`F5`** decide · **`F6`** construye», PROPIETARIO **el Owner**, y su MATERIA MÍNIMA son las tres cosas que `V6-16` presupone —identidad separada, evidencia fuera del árbol, refs protegidas—, **que «ninguna sede aprobada contempla»** (L10570-10574) | **`V6-16` y `V6-17` llevan fase `F6` en la sede que `O20` designa como EL CONTRATO, y su norma habilitante lleva fase `F5` y propietario el OWNER en otra sede del mismo documento.** `O20` §1 exige «**asignación INEQUÍVOCA de cada obligación a `F5` o a `F6`**» (sede L372): aquí la asignación **no es inequívoca**, y §20 —lo único que un `F6` necesita leer, según su propia cabecera L11729-11730 «*escrito completo para que se pueda construir sin volver a decidir nada*»— **no advierte de la dependencia**. Quien construya `V6-16` desde §20 construye sin norma que lo autorice, que es lo que `PN-19` L10570-10574 llama «que `F6` decida por el Owner» |
| **`U2-04`** | **GRAVE** | **A** | `11-ARQUITECTURA-INTEGRADA.md`:**9238-9252**, tabla de §15.4, contra su propia regla en **9233-9236** | La regla, añadida por `P-26`: «*esta tabla contiene **UNA FILA POR RESOLUCIÓN** del Owner, **derivada de las cabeceras `### \`O` de la sección 2 de `DECISIONES-Y-CONTRADICCIONES.md`**… **Una resolución sin fila aquí es el defecto.**»* Y §11.9 L8954-8955: «**§15.4 sigue llevando una fila por cada resolución REGISTRADA en ella**, que hoy son las de `O7` en adelante» | ```comm -23 <(grep -oE '^### `O[0-9]+`' DEC.md \| grep -oE 'O[0-9]+' \| sort -u) <(awk 'NR>=9238&&NR<=9252' 11.md \| grep -oE '`O[0-9]+`' \| grep -oE 'O[0-9]+' \| sort -u)``` → **`O20`**. Y `grep -cE '^\| `?O[0-9]+' 11.md` —el censo que §11.9 L8963 publica— da **13**: `O7`…`O19`. **`O20` no tiene fila** | **DEFECTO AUTODECLARADO, y REGRESIÓN LITERAL de `P-26`**, que existe porque «*`O16` no tenía fila — en la tabla cuyo objeto es declarar dónde queda cada resolución del Owner*» (L9229-9232). La tanda que registra `O20` no le dio fila en la sede de trazabilidad: **la resolución que cambia la frontera no está trazada en la tabla que traza dónde queda cada resolución** |
| **`U2-05`** | **GRAVE** | **A** | `11-ARQUITECTURA-INTEGRADA.md`:**§15.8**, contra su propia regla 2 en **9324-9327** | La regla, añadida por `P-03` del documento 22: «*EL RECUENTO DE CORRECCIONES SE DERIVA DE LOS BLOQUES `###` DE ESTA SECCIÓN… **Toda tanda nueva ABRE SU BLOQUE EN EL MISMO ACTO EN QUE ESCRIBE SUS DECISIONES**: no abrirlo es lo que rompió la derivación dos veces.*» | ```grep -nE '^### `D[0-9]+' 11.md \| tail -2``` → `### \`D107\`` (L9605) y `### \`D108\`` (L9620). **No existe bloque `### \`D109\`.** ```grep -n 'D109' 11.md``` → **una sola línea, L11723**, y es la cabecera de §20 («DERIVADO DE `O20`, VÍA `D109`»), no un bloque de §15.8. `D109` sí existe en el registro: ```grep -o '^\| D[0-9]* \|' DEC.md \| tail -1``` → `\| D109 \|` | **REGRESIÓN de `P-03`**, exactamente la clase que su remedio nombra: «*no abrirlo es lo que rompió la derivación dos veces*». La tanda de `O20` escribió `D109` en el registro y **no abrió su bloque en §15.8**, que es la sede de la que §0 L13-14 dice derivar el ordinal de correcciones del documento 11 —tramo de `U1`, citado sólo como corroboración— |
| **`U2-06`** | **GRAVE** | **A** | `11-ARQUITECTURA-INTEGRADA.md`:**§18** (L10758-10893), nodo **8 · PRIMERA ADOPCIÓN REAL · PesquerApp** (L10783-10787) y su glosa L10884-10887 | §18 se titula «**Orden de construcción para `F6`**» y es el grafo que un `F6` lee para saber en qué orden construir. Su nodo 8 es «**PesquerApp PERMANENTE, no un montaje desechable**», y su glosa dice: «*el paso 8 exige la **BASE COMPLETA ACORDADA de los pasos 0 a 7**, y no un MVP*» | Barrido sobre §18 entero: ```awk 'NR>=10758&&NR<=10893' 11.md \| grep -niE 'O18\|O19\|O20\|verificador\|ra[ií]z externa\|§11\.8\|§20\|PN-19'``` → **VACÍO**. §18 no nombra `O18`, ni `O19`, ni `O20`, ni el verificador de admisión, ni la raíz externa, ni §11.8, ni §20, ni `PN-19`. Su única condición para el paso 8 son los **pasos 0 a 7**, y **ninguno de ellos es el verificador de `F6`** | **LA ÚNICA SEDE QUE ORDENA LA CONSTRUCCIÓN DE `F6` Y NOMBRA A PesquerApp COMO SU PASO 8 NO LLEVA EL BLOQUEO.** La prohibición sí está escrita en sede normativa —sede canónica `O20` §8, §20.0 L11746-11748, §20.2 L11787-11789, `D109`(vi), checkpoint L44-45, `00-INDICE` L104—, y por eso **no digo que PesquerApp esté desbloqueada**; digo que **quien construya `F6` leyendo su propio orden de construcción llega al paso 8 sin encontrar la condición**, y que la tanda de `O20` no tocó §18. Es el disparador «**PesquerApp PODRÍA INICIARSE antes de certificar `F6`**» en su forma de omisión de sede, no de autorización |
| **`U2-07`** | MEDIO | **A** | `11-ARQUITECTURA-INTEGRADA.md`:**8427-8431** (campo 17 y 18 del SOBRE) y **8484-8488** (obligación `6bis` del revisor); `C-L.5` L11681-11687 | El campo 17 exige «`O17`, `O18` y `O19`, **nombrados uno a uno**» y la obligación `6bis` «*los digests del texto canónico de **`O17`, `O18` y `O19`** contra el campo 18*» | La sede canónica publica **CUATRO** resoluciones: ```grep -o '^# `O[0-9]*`' docs/owner/ADS-OWNER-RESOLUCIONES.md``` → `O17` `O18` `O19` **`O20`**. El sobre de este gate ancla las cuatro y publica los cuatro digest —los cuatro reproducen (§0.2)—, de modo que **el sobre CUMPLE DE MÁS**; lo que no se actualizó es la NORMA | **La sede normativa del sobre no exige anclar `O20`.** Un sobre futuro que ancle sólo `O17`–`O19` satisface §11.6 y `C-L.5` **al pie de la letra** y dejaría fuera la resolución que fija la frontera. Es una REGLA que falta para construir el instrumento —§11.6 es lo que `F6` materializa como «contrato de gate en el kernel» (L8607-8611)—, y la tanda que registró `O20` no la tocó |
| **`U2-08`** | MEDIO | **A** | `CHECKPOINT-ADS-NEXT.md`:**1185-1191**, dentro del campo `based_on:` del BLOQUE DE ESTADO que **L956-957** declara «*ESTE BLOQUE ES EL ESTADO REANUDABLE y va SIN rótulo histórico: describe el árbol VIGENTE*» | Regla 1 del propio bloque (L964-967): «*NADA QUE OTRA SEDE PUEDA DERIVAR SE COPIA DENTRO DE ESTE BLOQUE. **Ni recuentos de hallazgos, ni severidades, ni clasificación A/B/C**, ni número del último documento, ni rama, ni base*». Regla 4 (L975-978): «*TODO EVENTO NUEVO —un gate devuelto, **una resolución del Owner**, una tanda aplicada— REANCLA `metodo`, `last_meaningful_event` y **`based_on`** EN EL MISMO COMMIT QUE LO REGISTRA*» | ```awk 'NR>=1184&&NR<=1208' CHK.md``` devuelve, tras la línea que RETIRA la enumeración (L1181-1184), **un fragmento de columna derecha SIN SUJETO**: «*dictámenes Y y Z, adjudica AA · **GATE INVÁLIDO** · VEREDICTO INSUFICIENTE · **`C-L.5` pasa a ABIERTA** · recuento, severidades y clasificación A/B/C EN EL PROPIO DOCUMENTO: aquí se REMITE y no se copia, por la regla 1*». Su fila izquierda —la ruta del documento 25— la borró el remedio de `S2-03`. Y la enumeración que le sigue (L1195-1207) llega hasta `O18`·`D108` y **no contiene `O19`, `O20` ni `D109`** | **TRES cosas a la vez, y las tres vivas.** (i) Un fragmento **huérfano**, sin sujeto, superviviente del remedio de `S2-03`. (ii) **Copia un estado** —«`C-L.5` pasa a ABIERTA»— en la misma frase en que declara «*aquí se REMITE y no se copia, por la regla 1*», que es literalmente la clase `DD-08`/`C-16`. (iii) Ese estado es el del **CUARTO** gate, que L2296-2299 rotula `[HISTÓRICO]`. Y `based_on` **no se reancló** para `O20`/`D109`, contra la regla 4. `C-08` del octavo gate cerró la INSTANCIA de este mismo campo —«*la base vigente no se nombra: remite*», L1159-1165— y **dejó la clase abierta en el mismo campo**: `C-L.7` sigue **NO CERRADA** por esto |
| **`U2-09`** | MEDIO | **A** | `CHECKPOINT-ADS-NEXT.md`:**2110-2123**, campo `owner_captado:`, dentro del mismo bloque VIGENTE | «*la AUTORIDAD CANÓNICA … es `docs/owner/ADS-OWNER-RESOLUCIONES.md`, **donde viven `O17`, `O18` —texto amplio RATIFICADO— y `O19`** con su texto íntegro*» (L2112-2113) y «***`O17`, `O18` Y `O19` NO SE TRANSCRIBEN AQUÍ*** … **NINGUNA de las tres** autoriza iniciar F5, F6 ni PesquerApp» (L2121-2123) | El comando que el propio fichero publica dos campos más arriba (L1070-1071) lo desmiente: ```grep -o '^# `O[0-9]*`' docs/owner/ADS-OWNER-RESOLUCIONES.md``` → **`O17` `O18` `O19` `O20`**. La enumeración de `owner_captado` va **una resolución corta**, y «las tres» son **cuatro** | **Sede del bloque reanudable que enumera lo que su propio fichero manda DERIVAR, y que caduca con `O20`.** Misma clase que `U2-08` y que `C-06`/`C-07`/`C-08`: el bloque vuelve a escribir lo que declara no escribir, esta vez en el campo cuyo objeto es decir dónde vive lo que el Owner resolvió. Y la frase «ninguna de las tres autoriza iniciar F5, F6 ni PesquerApp» **deja `O20` fuera de la afirmación** — aunque `O20` tampoco autoriza, la sede no lo dice |
| **`U2-10`** | MEDIO | **A** | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`:**545**, fila `D109`(iii); `CHECKPOINT-ADS-NEXT.md`:**4195-4196**; `00-INDICE.md`:**104** | Las tres afirman lo mismo: **§20 del documento 11 tiene DIECIOCHO puntos, «cada uno con FUENTE, propietario, implementador, fase, entrada, salida, evidencia, escenario positivo, escenario negativo, condición de bloqueo y criterio exacto de cierre»** — once campos por punto | La tabla de §20.1 tiene **NUEVE columnas**, y una es el identificador: ```sed -n '11758p' 11.md \| awk -F'\|' '{for(i=2;i<NF;i++)print $i}'``` → `#` · `qué debe demostrar F6` · `entrada` · `salida` · `evidencia` · `escenario POSITIVO` · `escenario NEGATIVO` · `condición de BLOQUEO` · `criterio EXACTO de cierre`. Son **ocho atributos por fila**. `propietario`, `implementador` y `fase` se declaran **GLOBALMENTE** en L11753-11756 y no por punto — lo que es aceptable por cuantificación universal—, pero **`fuente` NO aparece ni por fila ni globalmente por punto**: sólo la cabecera global L11723 («TODO … DERIVADO DE `O20`»). Y `V6-12` no tiene fuente en ninguna de las 22 filas de la matriz: ```comm -23 <(V6 definidos) <(V6 citados por los 22)``` → **`V6-12`** | **UNA FRASE AFIRMA LO QUE LA TABLA NO DA**, en tres sedes vivas a la vez, y es exactamente `C-05` —«*ninguna frase afirma un reparto que su tabla no dé*»— aplicado al contrato en vez de al manifiesto. Ocho de los once campos son por fila, tres son globales, y **`fuente` no existe**. No invalida el contrato; invalida la descripción que tres sedes hacen de él |
| **`U2-11`** | MEDIO | **A** | `CHECKPOINT-ADS-NEXT.md`:**4067**, fila `C-11` de la matriz | Su `prueba_de_cierre`: «*el derivador no dice «ÚNICA SEDE» donde hay tres usos; **la unificación va a `V6-04`**»*, con `implementacion_pendiente` = **sí** y fase «`F4c` la afirmación · `F6` la unificación» | La mitad de `F4c` **está aplicada**: ```grep -n 'ÚNICA SEDE' derivar-universo-obligatorio.py``` → **una sola línea, L763**, y es la nota de corrección en pasado. Pero la mitad de `F6` va a `V6-04`, cuyo criterio de cierre (doc 11 L11763) es «*el censo se DERIVA del código; **cero lecturas fuera del canal único**»* — **un censo de LECTURAS DE GIT**. `C-11` es la fórmula de **RECUENTO DE LÍNEAS**, con dos copias vivas en el emisor: ```grep -n 'count(b"' emitir-sobre-de-ancla.py``` → **L217** y **L372**, y la de L372 **es la que publica** «O17 (85 lineas) · O18 (111) · O19 (81) · O20 (107)» del sobre | **Segunda instancia de la clase de `U2-01`**: una mitad pendiente enrutada a un punto `V6` cuyo criterio de cierre no la cubre. `F6` puede cerrar `V6-04` entero y las tres copias de la fórmula seguirán ahí. **Instrumental: lo señalo y lo dejo a `U1`, que lo tiene asignado** |
| **`U2-12`** | LEVE | **A** | `11-ARQUITECTURA-INTEGRADA.md`:**10901-10913**, §19 «NADA ESTÁ PROBADO» | Enumera las familias de contrato de prueba no ejecutadas y **remite a la sede de cada una**: «*la sede de `X<nn>` es §2.6.7, la de `X-<L>` es §2.9, la de `X-S<n>` es §9.6 y la de `X-O<n>` es §11.6*» | La familia **`V6-<nn>`** de §20.1 —**18 filas**, `grep -cE '^\| \`V6-'` sobre L11760-11777 → **18**— **no aparece en la enumeración**. `grep -n 'V6-' 11.md` fuera de §20.1 → **VACÍO** | §19 es la sede de «nada está probado» y su censo de familias **quedó corto con `O20`**. **No produce una afirmación falsa** —§20.2 L11782 declara su propia no ejecución— y por eso es LEVE; pero es la misma clase que `DD-13` y `EE-07`/`EE-12` corrigieron dos veces en este mismo bloque |
| **`U2-13`** | LEVE | **A** | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`:**872**, nota de remedio de `C-21` | Es una cita en bloque (`> `) de una sola línea de **419 caracteres** | ```awk 'NR==872' DEC.md \| grep -oP '\S > \S' \| wc -l``` → **4**. El marcador de cita `> ` quedó **incrustado a mitad de frase** cuatro veces: «*de la **> sede** en indicativo*», «*nació de una **> proyección**…*», «*la misma clase en **> la** dirección contraria*», «***no se amplía > nada***». Barrido sobre mis seis fuentes: ```grep -cP '^> .*\S > \S'``` → `00-INDICE` **0** · `11` **0** · `CHK` **0** · `SEDE` **0** · `DEC` **1** | Corrupción tipográfica **aislada** y viva, en la nota que aplica `C-21` —el hallazgo cuyo objeto es que una proyección no debilite el texto canónico—. No cambia ninguna obligación. **El remedio de fondo de `C-21` SÍ está aplicado**: el bloque se rotula hoy «RESUMEN DE ESTE REGISTRO, NO LITERAL DE LA SEDE» (L870), que es la segunda rama de su criterio de cierre |
| **`U2-14`** | LEVE | **A** | `CHECKPOINT-ADS-NEXT.md`:**38-42** y `00-INDICE.md`:**104** | Las dos escriben a mano «**catorce** CORREGIDOS EN `F4c`» y «**ocho** CONTRATO COMPLETO PARA `F6`» | La sede que los deriva lo prohíbe: `CHECKPOINT`:4025, cabecera de la matriz — «***El recuento NO se escribe: se DERIVA.***» Hoy los dos cardinales son ciertos: ```awk '/^### La tabla de los 22/{t=1} t' CHK.md \| grep -oE '\| (CORREGIDO_EN_F4c\|CONTRATO_COMPLETO_PARA_F6) \|' \| sort \| uniq -c``` → **8** `CONTRATO_COMPLETO_PARA_F6` · **14** `CORREGIDO_EN_F4c` | **Cardinal copiado fuera de la sede que declara derivarlo.** Es la clase `C-16`/`J-07`/`EE-07` que este expediente lleva cinco gates persiguiendo, aunque aquí la regla 1 del bloque reanudable **no alcanza literalmente** —L38-42 está en la cabecera, no dentro del bloque `regla_de_reanclaje`—. **Es verdadero hoy**, y por eso LEVE: lo que se registra es que caducará con el primer movimiento de la matriz |

### §2.1 · RECUENTO, DERIVADO DE LAS FILAS DE ARRIBA

```text
GRAVE   6   U2-01 · U2-02 · U2-03 · U2-04 · U2-05 · U2-06
MEDIO   5   U2-07 · U2-08 · U2-09 · U2-10 · U2-11
LEVE    3   U2-12 · U2-13 · U2-14
            ──
            14

POR CLASE, con el convenio de `DD-20`
  A  14   todos
  B   0   ninguno exige una decisión NUEVA del Owner. Ninguno reinterpreta `O17`-`O20`
  C   0   ninguno exige corromper la referencia ni reescribir `HEAD`, refs o base

POR ÁRBOL
  DE LA CANDIDATA `7aeed6aa…`   13
  DEL SOBRE                      1   (U2-01, verificado contra el sobre que YO recibí)

NINGUNO ES «EL VERIFICADOR DE `F6` NO ESTÁ IMPLEMENTADO»
  Los seis GRAVES son: un hallazgo movido a `F6` con criterio de cierre que no lo cierra
  (`U2-01`) · una matriz adversarial que no especifica ocho de las once clases reproducidas
  (`U2-02`) · una fase asignada de forma NO inequívoca (`U2-03`) · dos regresiones de
  remedios cerrados por gates anteriores (`U2-04` de `P-26`, `U2-05` de `P-03`) · y la
  sede de construcción de `F6` sin el bloqueo de PesquerApp (`U2-06`).
```

**NINGUNO VUELVE AL OWNER.** Los catorce se cierran con material que el corpus ya tiene
escrito: una fila en §15.4, un bloque en §15.8, una condición en §18, tres identificadores en
§11.6, un rango en `V6-15`, una remisión a `PN-19` en §20, y una reclasificación de `C-20`.
**No formulo ninguna pregunta al Owner, y no propongo ninguna corrección.**

## §3 · LA MATRIZ DE LOS 22, FILA A FILA CONTRA EL DOCUMENTO 29

**Los tres comandos que la propia matriz publica (`CHECKPOINT`:4027-4041), ejecutados por mí:**

```bash
awk '/^### La tabla de los 22/{t=1} t' docs/evolucion/CHECKPOINT-ADS-NEXT.md |
  grep -oE '^\| `C-[0-9]+`' | sort -u | wc -l
→ 22

awk '/^### La tabla de los 22/{t=1} t' docs/evolucion/CHECKPOINT-ADS-NEXT.md |
  grep -oE '\| (CORREGIDO_EN_F4c|CONTRATO_COMPLETO_PARA_F6|REGISTRADO_PARA_F5|EXTERNO_CON_PROPIETARIO|HISTORICO_NO_APLICABLE) \|' |
  sort | uniq -c
→ 8 CONTRATO_COMPLETO_PARA_F6   ·   14 CORREGIDO_EN_F4c        (8 + 14 = 22)

comm -23 <(grep -oE '^\| \*\*`C-[0-9]+`\*\*' docs/evolucion/29-…md | grep -oE 'C-[0-9]+' | sort -u) \
         <(awk '/^### La tabla de los 22/{t=1} t' docs/evolucion/CHECKPOINT-ADS-NEXT.md | grep -oE 'C-[0-9]+' | sort -u)
→ VACÍO
```

**Y la dirección inversa, que la matriz NO publica y yo añado:** ninguna fila de la matriz
nombra un identificador que el documento 29 no tenga —`comm -13` sobre los mismos conjuntos
sale también **VACÍO**—. Los identificadores del documento 29 son, uno a uno,
`C-00 C-01 C-02 C-03 C-04 C-05 C-06 C-07 C-08 C-09 C-10 C-11 C-12 C-13 C-14 C-15 C-16 C-17
C-18 C-19 C-20 C-21`, **veintidós exactos**.

**LOS 22 IDENTIFICADORES ESTÁN, UNO POR FILA, CON UN SOLO ESTADO PRIMARIO. NINGUNO OMITIDO,
NINGUNO FUSIONADO EN SILENCIO, NINGUNO DUPLICADO. LAS SUMAS SE DERIVAN.** Lo confirmo, y
también confirmo que la fusión `T1-10`≡`T2-05` la hizo el adjudicador `GG` en el documento 29
(§3, L3355-3359) **antes** de la matriz, y queda como `C-05`: no es una fusión silenciosa de
esta tanda.

**FILA A FILA, contra la tabla consolidada de `GG` (documento 29 L3372-3395):**

| id | sev/clase en el doc 29 | estado primario en la matriz | fase | ¿coherente con `O20` §6? | contraste |
|---|---|---|---|---|---|
| `C-00` | BLOQUEANTE · A · `GG`, el UNDÉCIMO ÁRBOL, batería `_en_zona` | `CONTRATO_COMPLETO_PARA_F6` | `F6` | **SÍ** | defecto de IMPLEMENTACIÓN del verificador → `F6`. `V6-05·09·11·15·18` cubren mutación, clases nueva/preexistente, auto-exclusión y falsos verdes |
| `C-01` | BLOQUEANTE · A · `T1-01`, predicado de bytecode | `CONTRATO_COMPLETO_PARA_F6` | `F6` | **SÍ** | `V6-13` cubre Latin-1 inválido; `V6-05` la mutación; `V6-11` la auto-exclusión |
| `C-02` | BLOQUEANTE · A · `T1-02`, BORRAR un documento | `CONTRATO_COMPLETO_PARA_F6` | `F6` | **SÍ** | `V6-06` y `V6-14` cubren `D` con sus dos puntas |
| `C-03` | GRAVE · A · `T1-09`, regresión de `S1-02` sobre lo NO confirmado | `CONTRATO_COMPLETO_PARA_F6` | `F6` | **SÍ** | `V6-07` (índice y árbol de trabajo) y `V6-08` (confirmado no exime) |
| `C-04` | GRAVE · A · `T1-06`, dos lecturas Git más | `CONTRATO_COMPLETO_PARA_F6` | `F6` | **SÍ** | `V6-01`…`V6-04`. El censo derivado de lecturas es exactamente `V6-04` |
| `C-05` | GRAVE · A · `T1-10`≡`T2-05`, el manifiesto 8 afirma un reparto que su tabla no da | `CORREGIDO_EN_F4c` · coordinador · `F4c` | `F4c` | **SÍ** | **REMEDIO VERIFICADO POR MÍ, y es de mi lote.** §4 fila 2 del manifiesto de HOY da a `U1` `L1-L5200` **y `L8200-L11791`**; y `grep -n '^## 11\.4 \|^## 11\.6 \|^## 11\.9 \|^## \`C-L\.5\`' 11.md` → **8253 · 8329 · 8912 · 11550**, las cuatro dentro de `L8200-L11791`. **Cierra la clase, no sólo la instancia** |
| `C-06` | GRAVE · A · `T2-01`, `metodo:` afirma un estado de `C-L.5` | `CORREGIDO_EN_F4c` · `SIS` · `F4c` | `F4c` | **SÍ** | **VERIFICADO**: L1003-1010 retira el estado y publica `grep -n 'CLASIFICACIÓN VIGENTE' …`, que resuelve a L2273 y L2519 |
| `C-07` | GRAVE · A · `T2-02`, el cuerpo desmiente su remisión | `CORREGIDO_EN_F4c` | `F4c` | **SÍ** | **VERIFICADO**: `last_meaningful_event` (L1228-1250) narra `O20`, que es su evento, y L1246-1250 lo declara |
| `C-08` | GRAVE · A · `T2-03`, `based_on` tres eventos atrás | `CORREGIDO_EN_F4c` | `F4c` | **SÍ en la instancia** | **INSTANCIA cerrada, CLASE ABIERTA en el mismo campo** — es `U2-08`: el huérfano de L1185-1191 copia «`C-L.5` pasa a ABIERTA» y `based_on` no se reancló para `O20`/`D109` |
| `C-09` | GRAVE · A · `T2-04`, el comando que da 13 donde el ordinal es 7 | `CORREGIDO_EN_F4c` | `F4c` | **SÍ** | **VERIFICADO**: `grep -c 'GATE\*\.md'` → **1**, y esa única línea es L993, la nota que lo cita **en pasado** («aquí se publicaba») al retirarlo. No queda publicado como derivación viva |
| `C-10` | MEDIO · A · `T1-04`, la columna de agotamiento dice más que su regla | `CORREGIDO_EN_F4c` · coordinador · `F4c` | `F4c` | **SÍ** | **VERIFICADO en el manifiesto de HOY**: §5 lleva columna `tipo` con **LEÍDA** / **AGOTADA POR DELEGACIÓN**, y su preámbulo L97-99 lo declara. Derivado: 3 LEÍDAS + 71 DELEGADAS = 74 |
| `C-11` | MEDIO · A · `T1-07`, «ÚNICA SEDE» con tres usos | `CORREGIDO_EN_F4c` + `implementacion_pendiente` sí | `F4c` la afirmación · `F6` la unificación | **PARCIAL** | mitad `F4c` **VERIFICADA** (`grep -n 'ÚNICA SEDE'` → una línea, en pasado). Mitad `F6` enrutada a `V6-04`, **que no la cubre**: es `U2-11` |
| `C-12` | MEDIO · A · `T1-08`, «30» del derivador contra «43» del README | `CORREGIDO_EN_F4c` | `F4c` | **SÍ** | **VERIFICADO**: `grep -n '30 rutas\|sus 30\b'` sobre el derivador → **VACÍO** |
| `C-13` | MEDIO · **C en el ataque, A en la propiedad** · `T1-03` REBAJADO por `GG` | `CONTRATO_COMPLETO_PARA_F6` | `F6` | **SÍ** | `V6-08` es literalmente «*un cambio YA COMMITEADO no queda exento*», que es el hecho de `T1-03`. Y la matriz **no arrastra el «C» del ataque**: le da estado primario por su PROPIEDAD, que es `A`. Correcto |
| `C-14` | MEDIO · A · `T2-06`, la enumeración de pasadas dos documentos corta | `CORREGIDO_EN_F4c` | `F4c` | **SÍ** | **VERIFICADO**: L2714-2731 la retira y remite a `ls docs/evolucion/[0-9][0-9]-*.md \| sort` |
| `C-15` | MEDIO · A · `T2-07`, `falta_para_cerrar_la_capa` nueve documentos atrás | `CORREGIDO_EN_F4c` | `F4c` | **SÍ** | **VERIFICADO**: L2529-2537 describe el estado vigente y baja el texto anterior a `[HISTÓRICO]` |
| `C-16` | MEDIO · A · `T2-08`, cuatro copias de recuento | `CORREGIDO_EN_F4c` | `F4c` | **SÍ, acotado** | **VERIFICADO en la copia que la fila declara**: L2578-2585 retira el recuento y publica su comando. `GG` ya lo declaró «SOSTENIDO, **acotado a UNA copia**» (doc 29 L3390); las otras tres viven en campos `_anterior` |
| `C-17` | MEDIO · A · `T2-09`, hueco de cuatro eventos en la cadena `_anterior` | `CORREGIDO_EN_F4c` | `F4c` | **SÍ** | **VERIFICADO**: L1015-1035 repone los cuatro —quinto gate, su tanda, sexto, su tanda, séptimo, su tanda— en un renglón, sin copiar recuentos |
| `C-18` | MENOR · A · `T1-05`, `_declarado_en_correccion` frágil | `CONTRATO_COMPLETO_PARA_F6` · bloquea `F6` y PesquerApp | `F6` | **SÍ, y ENDURECIDO** | un MENOR «fragilidad no explotada» pasa a bloquear `F6` y PesquerApp. Es un ENDURECIMIENTO, no una rebaja, y `V6-10`/`V6-11` lo cubren |
| `C-19` | MENOR · A · `T2-10`, el cardinal «nueve» sin comando | `CORREGIDO_EN_F4c` | `F4c` | **SÍ** | **VERIFICADO**: doc 11 L8327 retira el cardinal y remite. **Salvedad de etiqueta**: la columna `sede_normativa` dice «doc 11 §0 · `DD-13`» y el remedio vive en **§11.5 L8327**; §0 es la regla, no la sede del remedio |
| `C-20` | MENOR · A · `T2-11`, el sobre no lleva el TEXTO de la ratificación | **`CONTRATO_COMPLETO_PARA_F6`** | **`F6`** | **NO** | **ES `U2-01`.** Defecto de un artefacto de `F4c` —el sobre, que emite el coordinador— movido a `F6` con `V6-16`/`V6-17` como criterio de cierre, **que no lo prueban**. Reproduce en el sobre de este gate |
| `C-21` | MENOR · A · `T2-12`, la proyección de `O17` DEBILITA dos «debe» | `CORREGIDO_EN_F4c` | `F4c` | **SÍ** | **VERIFICADO por la segunda rama de su criterio**: L870 rotula hoy «RESUMEN DE ESTE REGISTRO, **NO LITERAL DE LA SEDE**», y el criterio admite «*reproduce la sede cláusula a cláusula **o no se presenta como literal**»*. La nota que lo aplica tiene una corrupción tipográfica: `U2-13` |

**¿SE HA SUAVIZADO O ESCONDIDO ALGUNO AL CAMBIARLE LA FASE?** **SÍ, uno: `C-20`** (`U2-01`).
Los otros veintiuno reparten bien: los ocho `CONTRATO_COMPLETO_PARA_F6` son, uno a uno,
defectos de la IMPLEMENTACIÓN del verificador interno —lo que `O20` §6 manda mover—, y los
catorce `CORREGIDO_EN_F4c` son documentales o de reparto, corregidos en su sede y verificados
por mí uno a uno arriba. **Ninguno se declara SUPERADO**: la cabecera de la matriz lo prohíbe
(L4049-4050) y ninguna fila lo hace.

**LOS CATORCE CORREGIDOS EN `F4c`, ¿cierran la CLASE o sólo la INSTANCIA?**

```text
CIERRAN LA CLASE   C-05 · C-06 · C-09 · C-10 · C-12 · C-14 · C-15 · C-17 · C-19 · C-21
                   —los diez retiran y remiten, o derivan, en vez de sustituir un valor
                   por otro, que es lo que este expediente exige desde `J-07`—

INSTANCIA CERRADA, C-08   el huérfano de `based_on` sobrevive en el MISMO campo (`U2-08`)
CLASE ABIERTA      C-11   la mitad de `F6` va a un `V6` que no la cubre (`U2-11`)
                   C-16   `GG` ya lo acotó a UNA copia, y así consta en la fila
                   C-07   el cuerpo se reancló, pero `based_on` —su campo hermano bajo la
                          MISMA regla 4— no: ver `U2-08`
```

## §4 · LO QUE VERIFIQUÉ Y **NO** CAYÓ

**4.1 · EL SOBRE, y con él la validez del gate.** Los dos digest de universo reproducen, con
sus dos cifras de fuentes y sus dos de líneas; los cinco digest de la sede reproducen en los
DOS commits; el SHA-256 del manifiesto reproduce; emisor y derivador tienen la misma huella
en los dos commits. **Ninguno de los dos disparadores de invalidez se dispara** (§0.2).

**4.2 · LA FILA DEL PROPIO DERIVADOR, que el sobre manda mirar PRIMERO.** No reincide, por
quinta vez: `0eca7103…` en la candidata y en el gate, idéntica a la que publica §4 fila 6 del
manifiesto. La falsificación de `U-02`/`X-06` **no se repite**.

**4.3 · EL MANIFIESTO ENTERO, mecánicamente.** Las **83 filas** de §4 y §5 casan contra el
árbol de la candidata **sin una sola discrepancia**, ni de SHA-256 ni de conteo de líneas
(comando y salida en §0.2, obligación 3). Y sus dos aritméticas **derivan de verdad**:

```bash
head -9  filas.tsv | cut -f2 | paste -sd+ | bc   → 28847   (§6: «ASIGNADAS A LECTURA 9 · 28847»)
tail -74 filas.tsv | cut -f2 | paste -sd+ | bc   → 59051   (§6: «AGOTADAS 74 · 59051»)
OBLIGATORIO − ASIGNADO sobre la CANDIDATA        → ∅ en las DOS direcciones (83 = 83)
OBLIGATORIO − ASIGNADO sobre el ÁRBOL DEL GATE   → 1, y es EXACTAMENTE el propio manifiesto
```

Esa única diferencia es la **exención de PUNTO FIJO de `DD-19`**, declarada en §6 L189-191, y
`EE-02` se cumple: cada fuente sin fila lleva su razón, una a una. **`DD-17`, `DD-19`,
`EE-02`, `C-05` y `C-10` están aplicados en este manifiesto, y los he comprobado los cinco.**

**4.4 · LA BATERÍA, EJECUTADA POR MÍ SOBRE LOS DOS ÁRBOLES.**

```bash
# árbol del GATE (mi worktree)
python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py  → 38/38 · exit=0
# árbol de la CANDIDATA, en un worktree desechable
git worktree add -q --detach $d 7aeed6aa… && cd $d && python3 …             → 38/38 · exit=0
```

**Y esto NO demuestra nada sobre `F6`**, y lo digo yo antes de que nadie me lo pregunte:
`O20` §5 (sede L402-403) escribe que un verde de la batería **no** demuestra que el
verificador esté construido, y **no lo cito para eso**. Lo cito para lo que sí prueba: que la
candidata no está en rojo por una causa distinta de las que este informe registra.

**4.5 · LAS SEDES QUE PUBLICAN COMANDO, EJECUTADAS UNA A UNA.** Todas las de mi lote:

```text
doc 11 L11569   grep -n 'C-L\.5' CHECKPOINT             → 4 sedes vivas, y NINGUNA discrepa:
                                                          L2289 y L2323 dan ABIERTA; L16/L61
                                                          y L265 están bajo [ESTADO ANTERIOR]
CHK  L1010      grep -n 'CLASIFICACIÓN VIGENTE' CHK     → L2273 (inicio) y L2519 (fin). El
                                                          puntero apunta ARRIBA, como `DD-08` exige
CHK  L969       ls docs/evolucion/[0-9][0-9]-*.md|tail-1 → 29-OCTAVO-GATE-…md
CHK  L973-974   grep -o '^### `O[0-9]*`' DEC | tail -1   → ### `O20`
                grep -o '^| D[0-9]* |' DEC | tail -1     → | D109 |
CHK  L11-12     grep -c '^## Siguiente acci…' CHK        → 11, menos la vigente = 10
CHK  L4258      grep -c '^## Siguiente acci… — HISTÓRICA' → 10.  Las dos cuadran
DEC  L950-951   ls -1 docs/owner/                        → 3 ficheros
                grep -o '^# `O[0-9]*`' …RESOLUCIONES.md  → O17 O18 O19 O20
DEC  L1095      git show 1d3b5d4 -- DECISIONES           → UN solo hunk. La cabecera real es
                                                          `@@ -1004,6 +1004,87 @@`; la sede la
                                                          cita como `@@ -1004 +1004,87 @@`, y
                                                          «y nada más» es CIERTO
doc11 L8830-31  sed -n '/^· SIS define el contrato/,/^· el ejecutor externo/p' SEDE
                                                         → las SEIS cláusulas, byte a byte
                                                           iguales al bloque «LITERAL» de §11.8
doc11 L8963     grep -cE '^\| `?O[0-9]+' 11.md           → 13 (O7…O19). Es `U2-04`
doc11 L11569    y las tres derivaciones de la matriz     → 22 · 14+8 · cobertura VACÍA (§3)
00-IND L178-183 diff <(find verificacion …) <(lista)     → VACÍO
00-IND L204     comprobar_referencias.py --exclusiones   → 1 superadas · 0 fallidas (`T147` verde)
```

**Sólo UNA de todas ellas se autofalsifica**, y es la que registro en `U2-09`
(`owner_captado` contra `grep -o '^# \`O…'`). Las demás **se sostienen**, y varias de ellas
—`C-L.5`, `CLASIFICACIÓN VIGENTE`, el ordinal, `T147`, la lista de `verificacion/`— son
exactamente las que gates anteriores falsaron. **La clase más productiva de este corpus dio,
esta vez, un solo hallazgo.**

**4.6 · LAS ATRIBUCIONES AL OWNER · CERO AMPLIFICACIÓN EN LA DIRECCIÓN PROHIBIDA.** Contrasté
`O20` cláusula a cláusula contra su proyección (`DEC` L1237-1293) y contra `D109` (`DEC` L545):

```text
sede §1 «invariantes · contratos · propietarios · fases · entradas y salidas · condiciones de
        fallo cerrado · matrices adversariales · criterios de aceptación ejecutables · y
        asignación inequívoca de cada obligación a F5 o a F6»
        → D109(i) las reproduce LAS NUEVE, en el mismo orden. IDÉNTICA
sede §3 NUEVE responsabilidades → D109(ii) enumera NUEVE, una a una. IDÉNTICA
sede §4 y §5 batería → D109(iv) y proyección L1287-1290. IDÉNTICAS, y la proyección declara
        expresamente que «esta proyección no puede suavizar» lo que el Owner escribe
sede §6 → proyección L1278-1285, ROTULADA «lectura de este registro sobre el punto 6 de la
        sede, NO literal». Añade una cuarta viñeta —«todo el que permita un falso verde
        bloquea `F6` y bloquea PesquerApp»— que la sede NO contiene
sede §7 → no proyectada explícitamente, y no hace falta: es el criterio del gate
sede §8 → D109(vi) y proyección L1275. IDÉNTICAS, «sin MVP, sin piloto desechable, sin
        adopción parcial»
```

**La única añadida ENDURECE, no debilita**, y va rotulada como lectura no literal en la
proyección. **La registro y NO la cuento como hallazgo**, y digo por qué en §5 (`RF-2`).
`D109`(v) la repite **sin ese rótulo** y declarando «`O20`, que es su única fuente» — lo dejo
dicho para el adjudicador y no lo elevo: no amplía autoridad, no rebaja ninguna exigencia y
la sede manda por su propia cláusula.

**4.7 · `C-L.5`, `C-L.7` y `M-04` BAJO `O20` — su clasificación vigente es CORRECTA.**

```text
C-L.5   ABIERTA.  Sede única: `CHECKPOINT` L2289-2291 y L2323-2334. La REABRE el adjudicador
        `GG` del OCTAVO GATE por `ASIGNADO − LEÍDO = 338 líneas y UNA FUENTE`, y el documento
        29 lo sostiene en §4.1 L3468-3483: «**NO EMITO LA PALABRA**». El manifiesto de este
        gate declara `C-L.5` ABIERTA (L31) y `00-INDICE` L104 igual. **CUATRO sedes, un solo
        estado.** `O20` no la toca y no debe tocarla: es cobertura, no implementación
C-L.7   NO CERRADA, y `CHECKPOINT` L2480-2483 lo razona expresamente contra `O20`: «*`C-L.7`
        es una condición sobre la DISCIPLINA DEL REGISTRO, no sobre la implementación del
        verificador, de modo que sigue siendo `F4c` y sigue bloqueando*». **Es correcto, y es
        la clasificación difícil de este corpus.** Y mis `U2-08` y `U2-09` **la confirman
        viva**: hay dos sedes más del bloque reanudable que copian lo que declaran no copiar
M-04    NO SUPERADA. `CHECKPOINT` L3991-4019 y L4230. `O20` le da FASE y PROPIETARIO —lo que
        le faltaba— y **no la cierra**: «*un gate de `F4c` puede declarar que su ARQUITECTURA
        está completa; no puede declarar superada una implementación que nadie ha escrito*»
        (L4016-4018). **Ninguno de los tres se declara cerrado ni superado sin serlo.**
```

**4.8 · NINGUNA DEUDA DE `F6` SE PRESENTA COMO IMPLEMENTACIÓN EXISTENTE.** Barrido sobre mis
seis fuentes buscando un `V6-<nn>` o el verificador declarado implementado, construido,
ejecutado o certificado: la única coincidencia es `CHECKPOINT`:48, y dice lo contrario —«*NO
demuestra que el verificador de `F6` esté construido ni certificado*»—. §20.2 L11782-11784 lo
escribe entero: «*NINGUNO DE LOS DIECIOCHO está implementado, ejecutado ni certificado*» y
«*NINGUNO PUEDE CITARSE como capacidad existente, ni en un dosier, ni en un informe, ni ante
el Owner*». **`X63` tampoco**: sigue siendo contrato de prueba de `F6` en todas sus sedes.

**4.9 · NINGUNA SEDE AUTORIZA PesquerApp.** Barrido sobre las 105 apariciones de «PesquerApp»
en mis seis fuentes: **ninguna la autoriza, la abre o la programa**. La prohibición está en
sede normativa —`O20` §8 en la SEDE CANÓNICA (L423-426), §20.0 L11746-11748, §20.2
L11787-11789, `D109`(vi), `CHECKPOINT` L44-45 y L4236-4237, `00-INDICE` L104— y las seis dicen
lo mismo, con las mismas tres exclusiones. **La traza está completa; lo que falta es que §18
la lleve**, y eso es `U2-06`.

**4.10 · REGRESIONES en lo que gates anteriores dieron por cerrado y toca mi dominio.**
Comprobé los remedios de `DD-07`, `DD-08`, `DD-13`, `DD-14`, `EE-04`, `EE-05`, `EE-07`,
`EE-12`, `S2-03`, `S2-04` y `S2-05` sobre las sedes que son mías:

```text
NO REINCIDEN   DD-07 (C-L.5 con UN solo estado, verificado con su propio grep)
               DD-13 (los titulares de doc 11 remiten o derivan)
               DD-14 (las CUATRO proyecciones vivas enlazan a su sede. El `awk` de DEC
                      L772-775, ejecutado por mí, da hoy: `O7`–`O14`→0 · `O15`→0 · `O16`→0
                      · **`O17`→6 · `O18`→3 · `O19`→1 · `O20`→2**. Los tres ceros son
                      CORRECTOS: el Owner ordenó que `O1`–`O16` NO se registren en la sede,
                      y §11.9 L8949-8953 lo declara)
               EE-05 (las filas C-L.5 y C-L.7 publican comando, no aserción)
               EE-07 · EE-12 (los cardinales «46» siguen retirados)
               S2-04 (el ordinal no se escribe; su comando roto se cita en pasado)
               S2-05 (el corchete del hecho 4 no reclama exclusividad)
SÍ REINCIDEN   P-26  → `U2-04`, y es literal: una resolución sin fila en §15.4
               P-03  → `U2-05`, y es literal: una tanda sin bloque en §15.8
               S2-03 → `U2-08`, en su residuo: el huérfano que el remedio dejó
               EE-04 → `U2-08` y `U2-09`, por la regla 4 y la regla 1 del mismo bloque
```

## §5 · REFUTACIONES CONTRA MÍ MISMO

**`RF-1` · CAYÓ, Y CONTRA MÍ** — «`U2-01` no vale: el sobre SÍ lleva lo que hace falta, porque
con el digest y la receta el revisor puede contrastar la sede sin ejecutar el emisor, que es
el fin de la cláusula. El fin se cumple; la forma es cosmética».
**Cayó a medias, y la mitad que sobrevive es la que decide.** Es cierto que el fin se cumple
—yo mismo contrasté los cinco digest sin ejecutar el emisor (§0.2)— y el propio `T2` lo
declaró contra sí mismo al graduarlo MENOR. **Pero eso no es lo que registro.** Lo que
registro es que el hallazgo **existe, reproduce hoy, y su criterio de cierre está en `F6` y no
lo prueba**: `V6-16` y `V6-17` pueden certificarse enteros con el sobre exactamente igual.
Si la conclusión correcta es que `C-20` ya no importa, **entonces lo que falta es retirarlo o
declararlo satisfecho en `F4c`, no darle una prueba de `F6` que no lo mide.** El hallazgo se
mantiene, y con la severidad subida de MENOR a GRAVE **no por su contenido sino por su
clasificación**: lo digo así para que nadie lea que agravo el defecto original.

**`RF-2` · CAYÓ** — «la viñeta que `D109`(v) añade a `O20` §6 —«los que permitan un falso
verde bloquean `F6` y PesquerApp»— es una AMPLIACIÓN de la sede, y la obligación 6 dice que
una paráfrasis que amplíe es un hallazgo».
**Cayó, y lo digo entero.** La obligación 6 castiga la ampliación **de autoridad**: `O19`
nació porque una proyección decía MENOS de lo que el Owner resolvió, y `C-21` porque otra
DEBILITABA. Esta viñeta **endurece**, es derivable de `O20` §8 leído con §6, va rotulada como
lectura no literal en la proyección larga, y **no autoriza nada ni releva a nadie**. Elevarla
sería castigar al corpus por ser más estricto que su norma. **La dejo registrada en §4.6 y no
la cuento.**

**`RF-3` · NO CAYÓ** — «`U2-06` es de laboratorio: §18 es un grafo de dependencias técnicas,
no una sede de autorización, y la prohibición está en seis sedes normativas».
**No cayó, y la razón está en el propio §18.** Su nodo 8 no es una dependencia técnica: es
«**PRIMERA ADOPCIÓN REAL · PesquerApp PERMANENTE, no un montaje desechable**», y su glosa
L10884-10887 **sí** enuncia una condición de entrada —«la BASE COMPLETA ACORDADA de los pasos
0 a 7»— citando `O15`. Es decir: §18 **sí** condiciona el paso 8, y la condición que escribe
**no incluye el verificador de `F6`**. Una sede que enuncia la condición equivocada es peor
que una que calla. Y `O20` §1 exige de `F4c` «**asignación inequívoca de cada obligación a
`F5` o a `F6`**»: el orden de construcción de `F6` es exactamente donde eso se lee.

**`RF-4` · CAYÓ A MEDIAS, Y ME OBLIGA A CORREGIR MI PROPIA REDACCIÓN** — «`U2-03` no es un
hallazgo: `PN-19` declara la decisión pendiente con propietario (el Owner), fase (`F5`),
materia mínima y prueba posterior. **No hay ninguna decisión arquitectónica OCULTA.**»
**Cayó en la palabra «oculta», y la retiro.** La decisión **NO está oculta**: `PN-19` la
declara entera, y ésa es la respuesta a la pregunta más importante de mi lote (§7). Lo que
sobrevive, y por eso mantengo el hallazgo con severidad GRAVE, es distinto y más estrecho:
**§20 declara «Fase de TODOS: `F6`» sin excepción y sin remitir a `PN-19`**, de modo que la
asignación de fase **no es inequívoca dentro del contrato**, que es lo que `O20` §1 exige.
Reescribo la columna «qué se sigue» de `U2-03` en esos términos, y **no afirmo que exista una
decisión escondida detrás de una obligación de `F6`**.

**`RF-5` · CAYÓ A MEDIAS** — «`U2-02` exagera: `V6-15` nombra los tres gates cuyos controles
son REPRODUCIBLES hoy, y los ocho árboles anteriores están cubiertos por `V6-01`…`V6-14`, que
son sus clases».
**Cayó para la mayoría, y no para todos.** Es cierto que las clases de los árboles 9, 10 y 11
—codificación, mutación, lectura de listas— tienen punto propio, y que `V6-11` cubre la
auto-exclusión. Pero `V6-15` **no dice «las clases»: dice «los controles … quedan como
FIXTURES OBLIGATORIOS»**, con entrada nombrada y criterio de cierre por gate; y su propio
escenario negativo pide **«los once árboles … uno a uno»**. **Una fila cuyo escenario negativo
exige once y cuyo criterio de cierre exige tres es insatisfacible por su propia letra**, y ésa
es la parte que sostengo. Bajo esa lectura el hallazgo **no es «faltan ocho fixtures»** sino
«**la fila se contradice**», y así queda redactada.

**`RF-6` · NO CAYÓ** — «`U2-04` y `U2-05` son erratas de trazabilidad, no arquitectura: el
gate juzga suficiencia ARQUITECTÓNICA y una fila que falta en una tabla no decide nada».
**No cayó, y la razón la escribe el propio corpus.** Las dos sedes **declaran su propia regla
y declaran que su incumplimiento es el defecto**: §15.4 L9236 «*una resolución sin fila aquí
es el defecto*», §15.8 L9326-9327 «*no abrirlo es lo que rompió la derivación dos veces*». Y
`O20` §6 es taxativo: «*los defectos ARQUITECTÓNICOS o **DOCUMENTALES** siguen bloqueando
`F4c`*». Son documentales, viven en `F4c`, y son **reincidencias literales** de dos remedios
que gates anteriores dieron por cerrados. Lo que sí acepto de la refutación es la severidad:
las gradúo GRAVE **por reincidencia**, no por su contenido, y lo digo en la fila.

**`RF-7` · CAYÓ** — «`U2-13` es una errata de Markdown y no debería figurar en un informe de
gate».
**Cayó, y por eso va como LEVE y no más.** La dejo porque vive en la nota que aplica `C-21`
—el hallazgo cuyo objeto es la fidelidad de una proyección— y porque el barrido que la
encontró es el mismo que buscaba ampliaciones. **No sostiene ninguna conclusión mía.**

**`RF-8` · NO CAYÓ** — «catorce hallazgos, ninguno bloqueante, ninguno de clase `B`, ninguno
vuelve al Owner, el sobre funciona, el manifiesto es impecable, la matriz deriva, los 22 están
uno a uno y los catorce remedios de `F4c` están aplicados: eso converge, y declarar
insuficiencia otra vez es inercia».
**No cayó, y es la refutación que más he trabajado.** Concedo todo lo que enumera —está en §4,
sin adorno—. Pero **la convergencia se mide contra el objeto de ESTE gate, no contra el de los
ocho anteriores**, y el objeto es la SUFICIENCIA ARQUITECTÓNICA. Tres de mis seis GRAVES caen
exactamente sobre los disparadores que el propio manifiesto escribe en su §7: un hallazgo
suavizado al cambiarle la fase (`U2-01`, L223), una matriz adversarial que no especifica una
clase reproducida (`U2-02`, L224) y una fase que no es inequívoca (`U2-03`, contra `O20` §1).
**Ninguno de los tres es «el verificador no está implementado».** Los tres se cierran con
material escrito. Y ninguno vuelve al Owner: **la convergencia es real, y el objeto todavía
no está satisfecho.**

### §5.1 · Qué cambiaron estas ocho en mi informe

```text
RF-1   subo `C-20` de MENOR a GRAVE **por su clasificación, no por su contenido**, y lo digo
RF-2   RETIRO un hallazgo que tenía escrito: la viñeta de `D109`(v) no se cuenta
RF-3   —
RF-4   RETIRO la palabra «oculta» de `U2-03` y reescribo su conclusión. La respuesta a la
       pregunta central de mi lote cambia de signo por esta refutación (§7)
RF-5   REESCRIBO `U2-02`: no es «faltan ocho fixtures», es «la fila se contradice»
RF-6   gradúo `U2-04` y `U2-05` GRAVE por REINCIDENCIA, y lo declaro
RF-7   `U2-13` baja a LEVE
RF-8   —
```

## §6 · LO QUE MI LOTE NO CUBRE, SIN ADORNO

```text
DOC 11 `L1`-`L5200`        NO es mío y NO lo he leído: §0 a §4.3 —la regla de titulares, los
                           tipos canónicos, el protocolo transaccional §2.6 entero, la tabla
                           adversarial §2.6.7, el contrato documental—. Es de `U1`. Cuando
                           cito §0 L13-14 o §2.6.7 lo hago como CORROBORACIÓN de una regla que
                           vive DENTRO de mi rango, y lo digo en cada caso

EL INSTRUMENTAL            `comprobar-correccion-gate-de-cierre.py` (4339 líneas),
                           `derivar-universo-obligatorio.py` (846) y el manifiesto del gate 8
                           NO están en mi lote. Los he EJECUTADO —es mi obligación con las
                           sedes que publican comando— y he leído fragmentos puntuales
                           (`_APPEND_ONLY`, `count(b"\n")`, «ÚNICA SEDE», `GATE*.md`) para
                           medir hallazgos concretos. **No los he auditado, y `U2-11` queda
                           expresamente remitido a `U1`**

EL EMISOR                  no lo he leído ni lo he ejecutado. La obligación 5 sólo pide su
                           SHA-256 en los dos commits, y eso sí lo he hecho. **Que el sobre
                           que recibí sea el que ese programa produce NO lo he comprobado, y
                           no puedo comprobarlo sin ejecutarlo — lo que §11.6 L8461-8464
                           prohíbe expresamente**

LAS 74 FUENTES AGOTADAS    no las he abierto. He verificado sus 74 SHA-256 y sus 74 conteos
                           de líneas contra el árbol de la candidata, y su regla de
                           agotamiento contra el §5 del manifiesto. **Verificar la huella no
                           es leer el contenido**, y si alguna de ellas contradice algo de lo
                           que afirmo, no lo sabría

EL DOCUMENTO 29            leído íntegro y EL ÚLTIMO, pero mi contraste se ha centrado en la
                           tabla consolidada de `GG` (L3372-3420), en los dos dictámenes
                           §2 (L591-648 y L2002-2046) y en §4. Los bancos de ataque §3 y §6
                           los he leído sin reproducir ni uno: **no he ejecutado ningún
                           árbol adversarial**, y por tanto **no aporto ninguna medición
                           propia sobre `M-04`**

LA SEDE CANÓNICA           la he leído íntegra y he recalculado sus cinco digest. **Lo que no
                           puedo comprobar es que sea el texto que el Owner emitió**: el
                           propio sobre lo declara, y sigue siendo la limitación que `O18`
                           declara de sí misma hasta el verificador externo de `F6`

QUÉ NO HE HECHO            no he modificado el repositorio: `git status --porcelain` sigue
                           VACÍO al cerrar, y `git rev-parse HEAD` sigue dando
                           `ebd52d9125fb740c1c7a7606f82876b8433ef6a8`. No he creado ramas, no
                           he commiteado, no he tocado `verificacion/`. **Y NO PROPONGO
                           NINGUNA CORRECCIÓN**: catorce hallazgos, cero remedios redactados

DEFECTOS DENTRO DE         no los cuento, y lo declaro: todo lo que vive bajo `[HISTÓRICO]`,
REGIONES HISTÓRICAS        `[ESTADO ANTERIOR]`, `## Siguiente acción exacta — HISTÓRICA` o un
                           campo `_anterior` **NO es un defecto vivo**. Comprobé la frontera
                           en los tres casos en que dudé: `CHECKPOINT` L16/L61/L265 (bajo
                           `[ESTADO ANTERIOR]`, no cuentan), L4271 (dentro de la primera
                           HISTÓRICA, no cuenta) y `DEC` L1058 (dentro del corchete
                           `[HISTÓRICO]` de L1060, no cuenta). **`U2-08` y `U2-09` NO están
                           en región histórica**, y lo verifiqué con el rótulo del bloque
                           (`CHECKPOINT` L956-957, «SIN rótulo histórico»)
```

## §7 · MI RESPUESTA, EN UNA FRASE

> **La frontera `F4c`/`F6` es COHERENTE en su enunciado y las seis sedes que la escriben dicen
> lo mismo; la clasificación de los 22 está COMPLETA —veintidós identificadores, un estado
> primario cada uno, sumas derivadas, ninguno superado— salvo `C-20`, que es un defecto vivo
> de un artefacto de `F4c` movido a `F6` con un criterio de cierre que no puede cerrarlo; y
> NO queda ninguna decisión arquitectónica OCULTA —`PN-19` declara con propietario, fase y
> prueba la única que falta— pero sí queda una ASIGNACIÓN DE FASE QUE NO ES INEQUÍVOCA,
> porque §20 pone en `F6` dos puntos cuya norma habilitante `PN-19` pone en `F5` sin decirlo,
> y una MATRIZ ADVERSARIAL que exige once árboles y sólo contrata tres.**

**Y lo que se sigue, dicho sin adorno y sin invadir al adjudicador:** los seis GRAVES caen,
uno a uno, sobre los disparadores que el §7 del manifiesto escribe —hallazgo suavizado al
cambiarle la fase, clase adversarial no especificada, asignación de fase no inequívoca,
contrato sin criterio de cierre efectivo, dos regresiones documentales de remedios
cerrados—, y **ninguno de ellos es que el verificador de `F6` no esté implementado**. Los
catorce se cierran con material que el corpus ya tiene escrito y **ninguno vuelve al Owner**.
Quien emite el veredicto es `HH`, y yo no lo emito.

---

## §8 · DISCIPLINA — declaración de cierre

**LAS DOS REFERENCIAS REMOTAS, RESUELTAS CONTRA EL REPOSITORIO Y NO CONTRA MI CLON.** Es la
obligación 2 del revisor en §11.6 L8475-8477, y la hago aunque el sobre no la exija por
separado:

```bash
git ls-remote origin 'refs/heads/gate/f4c-arquitectonico-final-20260901' \
                     'refs/heads/review/f4c-o20-frontera-de-fase-candidate-20260901'
→ ebd52d9125fb740c1c7a7606f82876b8433ef6a8  refs/heads/gate/f4c-arquitectonico-final-20260901
  7aeed6aa3a3eae1133f57a08d757020e62197b3d  refs/heads/review/f4c-o20-frontera-de-fase-candidate-20260901
```

**Las dos resuelven EXACTAMENTE a los SHA que el sobre publica**, y también los `tree`:

```bash
git rev-parse 7aeed6aa…^{tree}  → 0a8f5804e37bfb4ea05deabd18659cd2864f1d73   (sobre: idéntico)
```

**NO HE MODIFICADO EL REPOSITORIO.**

```bash
git status --porcelain   → 0 líneas
git rev-parse HEAD       → ebd52d9125fb740c1c7a7606f82876b8433ef6a8
```

Todo lo que ejecuté fuera de lectura pura se hizo en directorios temporales (`mktemp -d`) o
en un `git worktree --detach` desechable **retirado con `git worktree remove --force` al
terminar**. No he creado ramas, no he commiteado, no he tocado `docs/evolucion/verificacion/`
y no he escrito ni un byte bajo `/home/jose/ads-kernel`. **Mi informe vive fuera del
repositorio auditado.**

**NO PROPONGO NINGUNA CORRECCIÓN.** Catorce hallazgos, cero remedios redactados. Cada fila
dice **qué** está mal y **contra qué sede**, y ninguna dice **cómo** arreglarlo.

**NO EMITO VEREDICTO.** El veredicto es de `HH`, y los dos literales admisibles son
`SUFICIENTE PARA F5` e `INSUFICIENTE PARA F5`. Yo entrego hallazgos con fichero, línea,
comando y salida, y la respuesta de §7 a las tres preguntas que se me encargaron.

**INDEPENDENCIA.** No he escrito ninguna fuente de este corpus, no he aplicado ninguna
corrección, no he participado en ningún gate anterior y no he visto el dictamen de `U1`.

**EL INTÉRPRETE.** `python3 --version` → **Python 3.12.14**, del `PATH` que el encargo fija.
Con el 3.10 del sistema caen tres validadores por `tomllib`: es `A14`, y **no lo cuento como
hallazgo**.

```text
ASIGNADO − LEÍDO = ∅     6 fuentes asignadas · 6 leídas en su alcance declarado
                         doc 11: L5201-L11791 = 6591 líneas, íntegras
                         doc 29: íntegro, y EL ÚLTIMO
HALLAZGOS                14   GRAVE 6 · MEDIO 5 · LEVE 3
CLASE                    A 14 · B 0 · C 0
AL OWNER                 NADA
```

---

## §C · ADJUDICACIÓN DE `HH` — TRANSCRIPCIÓN LITERAL

# ADJUDICACIÓN `HH` — GATE ARQUITECTÓNICO FINAL DE `F4c`

> **Adjudicador `HH`.** Contexto limpio: no he escrito nada de este corpus, no he aplicado
> ninguna corrección, no he sido revisor de ningún gate anterior (`A`..`GG`, `U1`, `U2`) y no
> vi nada de este gate antes de abrir el sobre.
>
> **NO he modificado el repositorio auditado.** Todo lo que sigue se lee con
> `git show <commit>:<ruta>` y con índices temporales fuera del árbol de trabajo
> (`GIT_INDEX_FILE` en `mktemp -d`). No he creado commits, ramas ni referencias.
>
> **Objeto, según `O20` y el §7 del manifiesto: la SUFICIENCIA ARQUITECTÓNICA de `F4c`.** NO
> juzgo la implementación del verificador —es de `F6`— y **no construyo árboles adversariales
> para decidir este gate**.

---

## §0 · EL SOBRE, Y LOS BLOQUES QUE CADA REVISOR EMBEBIÓ

### §0.0 · Entorno declarado

```bash
export PYTHONPATH=.../scratchpad/py312-libs
export PATH=.../scratchpad/bin:$PATH
python3 -V     # → Python 3.12.14
```

`A14` reconocido: con el 3.10 del sistema caerían tres validadores por `tomllib`. **No es
hallazgo y no lo cuento.**

### §0.1 · El sobre que recibí

```bash
sha256sum /tmp/.../f4c9/SOBRE.txt
# → c39de894c21f25a22ef5789cfa0a5a097ff3e440ffa7e8c9d654caa969792282
wc -l  → 201
```

### §0.2 · LAS SEIS OBLIGACIONES, cumplidas por mi cuenta

**OBLIGACIÓN 1 · los dos digest de universo, con la receta del sobre.**

```bash
for C in 7aeed6a... ebd52d9...; do
  d=$(mktemp -d); GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null |
    LC_ALL=C sort |
    while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
    awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
  rm -rf "$d"; done
```

| árbol | fuentes | líneas | digest recalculado | publicado en el sobre | ¿reproduce? |
|---|---|---|---|---|---|
| CANDIDATA `7aeed6a` | **83** | **87898** | `d12b64b91ad313557df6bdf1c2a38f2ccb2d8a264b3f12553ada8e3a56ed551f` | idéntico | **SÍ** |
| GATE `ebd52d9` | **84** | **88156** | `868fb198e8b7699fc2b1161d76b29f804a911e2e6e8ba6e7712a7596bbef464d` | idéntico | **SÍ** |

**OBLIGACIÓN 2 · el manifiesto, leído EN EL COMMIT DEL GATE.**

```bash
git show ebd52d9...:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md | sha256sum
# → ff4116703b648586bae866cd259f37f7800088e8fe2148b4f4224b466322fc13   (256 líneas)
```

Coincide con el sobre. **No lo he leído del árbol de trabajo.**

**OBLIGACIÓN 3 · cada fila del manifiesto contra SU árbol, y la del derivador PRIMERO.**

Las 83 filas del manifiesto (9 de lectura + 74 agotadas) declaran el **árbol de la
candidata**. Las contrasté las 83 contra `7aeed6a`, línea y SHA-256:

```bash
git show ebd52d9...:.../F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md |
  grep -E '^\| [0-9]+ \| `' | sed 's/^| *[0-9]* *| *`\([^`]*\)` *| *\([0-9]*\) *| *`\([0-9a-f]*\)`.*/\1 \2 \3/' |
  while read -r r l s; do
    al=$(git show "7aeed6a...:$r" | wc -l); as=$(git show "7aeed6a...:$r" | sha256sum | cut -d' ' -f1)
    [ "$al" = "$l" ] && [ "$as" = "$s" ] || echo "MISMATCH $r"
  done
# → SIN NINGUNA SALIDA. 83/83 exactas.
```

**La fila del propio derivador —fila 6, `derivar-universo-obligatorio.py`, 846 líneas,
`0eca7103...`— es EXACTA.** El falseo que `U-02` y su reincidencia `X-06` midieron en dos
gates seguidos **NO se reproduce aquí**. Lo digo expresamente porque el sobre me ordena
mirarla primero.

**OBLIGACIÓN 4 · las dos superficies de diferencia, que NO son la misma.**

```bash
git diff --name-only 7aeed6a... ebd52d9...
```

```text
docs/evolucion/00-INDICE.md                                                    ← EN el universo
docs/evolucion/verificacion/manifiestos/F4C-...-FINAL-20260901.md              ← EN el universo
kernel/operativo/pruebas/evidencia/fuentes-salida.txt                          ← FUERA
kernel/operativo/pruebas/evidencia/negativos-salida.txt                        ← FUERA
kernel/operativo/pruebas/evidencia/referencias-salida.txt                      ← FUERA
```

El sobre publica **2** rutas de diferencia de UNIVERSOS y advierte expresamente que los
árboles pueden diferir además en ficheros que el universo no contiene. **Son exactamente esas
3 de evidencia reejecutada, y el §6 del manifiesto las nombra.** El sobre es honesto en este
punto y el manifiesto también. **No hay hallazgo aquí.**

**OBLIGACIÓN 5 · el emisor y el derivador, recalculados de los DOS commits.**

```bash
for C in 7aeed6a ebd52d9; do git show $C:docs/evolucion/verificacion/emitir-sobre-de-ancla.py | sha256sum; done
# 8ba060af7f2e1edab6b9a03038f62d2f4701cd7ba7c8dd182d8c58adb3fa4453   (los dos)
for C in 7aeed6a ebd52d9; do git show $C:docs/evolucion/verificacion/derivar-universo-obligatorio.py | sha256sum; done
# 0eca7103833110c32b4d2fda23acf54a04c905e40e98b6fda102e5d2dd5f312e   (los dos)
```

Los dos coinciden con lo publicado. **Y asumo la limitación que el propio sobre declara y que
`Z-11` midió:** que `git status` viniera vacío al emitir no prueba que el emisor que corrió
fuese el publicado. Lo que sí queda probado es la identidad de los DOS ficheros en los DOS
commits, y eso es lo que afirmo — ni un grado más.

**OBLIGACIÓN 6 · la sede canónica del Owner, digest a digest.**

```bash
git show 7aeed6a...:docs/owner/ADS-OWNER-RESOLUCIONES.md | sha256sum
# 4e4081efb29dcd2f095879b07104e4e169a46b497d11213256541fd6599a4e3a   (444 líneas)
for R in O17 O18 O19 O20; do
  git show 7aeed6a...:docs/owner/ADS-OWNER-RESOLUCIONES.md |
    awk -v r="$R" '/^# /{p=($0 ~ "^# `"r"`")} p' | sha256sum; done
```

| resolución | líneas | digest recalculado | ¿coincide con el sobre? |
|---|---|---|---|
| `O17` | 85 | `0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125` | **SÍ** |
| `O18` | 111 | `ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353` | **SÍ** |
| `O19` | 81 | `d86a9455aa9ede95d20f9c103d4109e747cd20914266a60547b0f050cfddf632` | **SÍ** |
| `O20` | 107 | `c3804cdec674b140a508f84a1b19a463efe27cd31b108b443271d34dab1906f3` | **SÍ** |

Los dos commits publican la misma sede byte a byte. **Ninguna huella FALLA CERRADO.**

### §0.3 · LOS BLOQUES DE SOBRE QUE CADA REVISOR EMBEBIÓ — byte a byte

Es la comprobación que INVALIDA el gate si falla. La hice extrayendo el bloque de cada
informe entre sus vallas y comparando con `cmp`, no a ojo:

```bash
sed -n '13,213p' INFORME-U1.md > /tmp/.../sobre-u1.txt     # valla ``` en 12 y 214
sed -n '12,212p' INFORME-U2.md > /tmp/.../sobre-u2.txt     # valla ~~~ en 11 y 213
sha256sum SOBRE.txt sobre-u1.txt sobre-u2.txt
cmp SOBRE.txt sobre-u1.txt && cmp SOBRE.txt sobre-u2.txt
```

```text
c39de894c21f25a22ef5789cfa0a5a097ff3e440ffa7e8c9d654caa969792282  SOBRE.txt
c39de894c21f25a22ef5789cfa0a5a097ff3e440ffa7e8c9d654caa969792282  sobre-u1.txt
c39de894c21f25a22ef5789cfa0a5a097ff3e440ffa7e8c9d654caa969792282  sobre-u2.txt
U1 IDENTICO
U2 IDENTICO
```

**LOS TRES SOBRES SON EL MISMO FICHERO, BYTE A BYTE.** `U1` lo enmarca con ` ``` ` y `U2` con
`~~~`, y esa valla es del informe, no del sobre. **La regla 2 del §8 del manifiesto —«cualquier
diferencia entre los sobres de dos revisores invalida el gate»— NO se dispara.**

**Observación de método, y la anoto a favor de los revisores:** ninguno de los dos
transcribió el sobre a mano; los dos lo embebieron. Es exactamente lo que el quinto gate
exigió cuando «el sobre deja de transcribirse a mano», y aquí se cumple.

### §0.4 · CONCLUSIÓN DEL §0

**EL GATE ES VÁLIDO en su ancla.** Las seis obligaciones reproducen, los dos digest de
universo reproducen, las 83 filas del manifiesto reproducen contra su árbol declarado, los
cuatro digest de resolución reproducen y los dos sobres embebidos son idénticos al mío. **Sigo
adelante.**

---

## §1 · MI MANIFIESTO DE LECTURA, Y LAS DOS RESTAS

### §1.1 · Qué he leído, y de dónde

```text
LA SEDE CANÓNICA          `docs/owner/ADS-OWNER-RESOLUCIONES.md`, 444 líneas, ÍNTEGRA, del
                          COMMIT CANDIDATO. `O17` · `O18` · `O19` · `O20` con su texto entero
EL MANIFIESTO             256 líneas, ÍNTEGRO, del COMMIT DEL GATE
§20 DEL DOCUMENTO 11      L11721-L11791, ÍNTEGRA — es el contrato que se juzga
LAS SEDES QUE CADA        §11.6 (8329-8626) · §11.7 · §11.8 (8722-8910) · §11.9 · §15.4
HALLAZGO INVOCA           (9227-9261) · §15.8 (9310-9661) · §16 `PN-19` (10517-10728) · §18
                          (10758-10895) · §19 · `C-L.5` · la MATRIZ DE LOS 22 (chk 4021-4100)
                          · `DD-20` (chk 3678-3712) · `C-L.7` · `M-04` · `D109` (dec 545) ·
                          `O20` proyectado (dec 1237-1295)
EL DOCUMENTO 29           al final, y para reproducir la clasificación de origen de los 22,
                          su §10.1 y la tabla consolidada de `GG`
LOS DOS DICTÁMENES        `INFORME-U1.md` (713 líneas) y `INFORME-U2.md` (906), ÍNTEGROS
```

**No he leído íntegras las 83 fuentes del universo, y no lo pretendo:** mi encargo es
adjudicar dos dictámenes reproduciendo sus afirmaciones contra fichero y línea, y eso he
hecho, **hallazgo por hallazgo, sin aceptar ninguno por autoridad.**

### §1.2 · `OBLIGATORIO − ASIGNADO`, calculada por mí

```bash
comm -23 rutas-<commit>.txt asignadas.txt     # asignadas = las 83 filas del manifiesto
```

| árbol | obligatorio | asignado | `OBLIGATORIO − ASIGNADO` | `ASIGNADO − OBLIGATORIO` |
|---|---|---|---|---|
| CANDIDATA `7aeed6a` | 83 | 83 | **∅** | **∅** |
| GATE `ebd52d9` | 84 | 83 | **1** · `…/F4C-ASIGNACION-GATE-ARQUITECTONICO-FINAL-20260901.md` | **∅** |

La única fuente sin fila sobre el árbol del gate es **el propio manifiesto**, y su §6
L189-191 la declara ANTES como exención de PUNTO FIJO de `DD-19`, «y cubre a ESTE fichero y a
NINGÚN OTRO». **No hay ninguna otra.** El compromiso de §6 L197 —«CUALQUIER OTRA FUENTE SIN
FILA sobre el árbol del gate es un DEFECTO de este manifiesto»— **se cumple**.

**Y las dos aritméticas del manifiesto DERIVAN de su propia tabla, no están escritas:**

```bash
head -9  filas.txt | awk '{s+=$2} END{print NR? "":"" , s}'   → 9 filas · 28847
tail -74 filas.txt | awk '{s+=$2} END{print s}'                → 74 filas · 59051
                                                     9+74 = 83   28847+59051 = 87898
```

**83 y 87898 son EXACTAMENTE las cifras del ÁRBOL DE LA CANDIDATA que el sobre ancla y que yo
rederivé en §0.2.** `EE-02` cumplido, `C-05` cumplido contra la propia tabla.

### §1.3 · `ASIGNADO − LEÍDO`

**Es la resta que `C-L.5` convierte en excluyente de la suficiencia, y la calculo con lo
único que puedo: las declaraciones de los dos revisores contra el reparto del §4.**

| fuente | alcance del §4 | quién declara leerla | ¿cubierta? |
|---|---|---|---|
| `00-INDICE.md` (241) | U2 íntegro | `U2` §1 | **SÍ** |
| `11-ARQUITECTURA-INTEGRADA.md` (11791) | U1 `L1-5200`+`L8200-11791` · U2 `L5201-11791` | `U1` §1.2 · `U2` §1 | **SÍ · unión = `L1-L11791`, sin hueco** |
| `29-OCTAVO-GATE` (4197) | los tres, el último | `U1` · `U2` · yo | **SÍ** |
| `CHECKPOINT-ADS-NEXT.md` (5339) | U2 íntegro | `U2` §1 | **SÍ** |
| `comprobar-correccion-gate-de-cierre.py` (4339) | U1 íntegro | `U1` §1.1 | **SÍ** |
| `derivar-universo-obligatorio.py` (846) | U1 íntegro | `U1` §1.1 | **SÍ** |
| `manifiestos/…-CERTIFICACION-8-20260831.md` (248) | U1 íntegro | `U1` §1.1 | **SÍ** |
| `ADS-OWNER-RESOLUCIONES.md` (444) | los tres | `U1` · `U2` · yo | **SÍ** |
| `DECISIONES-Y-CONTRADICCIONES.md` (1402) | U2 íntegro | `U2` §1 | **SÍ** |

```text
ASIGNADO − LEÍDO = ∅       nueve fuentes asignadas, nueve declaradas leídas en su alcance
```

**Y digo exactamente lo que esa cifra prueba y lo que no.** Prueba que **ninguna fuente
asignada quedó sin revisor que declarase haberla leído íntegra en su alcance**, que es lo que
la regla de cierre de `C-L.5` mide. **No prueba** que la lectura fuese exhaustiva: no puedo
auditar una lectura. Lo que sí he podido contrastar es que **los dos declaran sus lecturas
FUERA DE LOTE y no las cuentan como propias** —`U1` §1.2 declara tres entradas al lote de
`U2`; `U2` §6 declara las suyas al instrumental de `U1`—, y que **ningún hallazgo de ninguno
de los dos se funda ÚNICAMENTE en una fuente fuera de su lote**: lo comprobé hallazgo a
hallazgo en §2. **La resta cierra, y no excluye la suficiencia por sí sola.**

### §1.4 · Observación de MÉTODO que valoro POR ENCIMA de un hallazgo, y lo declaro

**El octavo gate reabrió `C-L.5` porque un revisor declaró «312 líneas · 0 fuentes» donde la
resta real era «338 líneas y UNA FUENTE» (chk L2323-2334).** En este gate, **los dos revisores
declaran su resta contra su propio interés, enumeran los rangos consecutivos que la
sostienen, y declaran además las lecturas que hicieron FUERA de su lote sin reclamarlas.**
`U1` llega a declarar que entró en `L5685` y `L5697` —lote de `U2`— «y no convierte ese tramo
en leído». **Eso es exactamente lo que `C-L.5` pide y lo que ningún gate anterior había
entregado limpio.** Lo hago constar como MÉTODO CORRECTO, y pesa a favor del gate aunque no
cambie el veredicto.

---

## §2 · REPRODUCCIÓN, HALLAZGO A HALLAZGO

> **Regla que aplico:** ninguna afirmación se acepta por autoridad. **Lo que no reproduzco
> CAE, y digo por qué.** Reproduje con mis propios comandos, sobre el COMMIT CANDIDATO
> `7aeed6a`, que es el objeto del gate.

### §2.1 · `U1-01` ≡ `U2-01` · `C-20` movido a `F6` con un criterio que no lo cierra — **REPRODUCE ENTERO**

Es el hallazgo declarado BLOQUEANTE por `U1` y GRAVE por `U2`. **Lo he reproducido en las
cinco piezas de que consta, una a una.**

**(a) LO QUE `O19` ORDENA, en la SEDE CANÓNICA, L315-317** — leído del commit, no de una
paráfrasis:

```text
Cada revisor debe recibir externamente: el texto de esta ratificación · el SHA del commit
candidato · el tree SHA · el SHA del manifiesto · el SHA del derivador · **el SHA de la sede
del Owner**. Y **debe comprobar la receta sin ejecutar el emisor.**
```

**(b) LO QUE §11.6 REPITE, doc 11 L8449-8459**, bajo el rótulo «**y es la lista entera**. No
es un resumen del sobre: es lo que tiene que llegarle por el canal externo al repositorio
antes de abrir nada. **Derivado de `O19` y de la sede canónica**»:

```text
· el TEXTO de la ratificación del Owner      ← L8454, el PRIMERO de los seis
· el SHA del COMMIT CANDIDATO · el TREE SHA · el SHA del MANIFIESTO · el SHA del DERIVADOR
· el SHA DE LA SEDE DEL OWNER
```

**(c) LO QUE MI PROPIO SOBRE TRAE — medido, no estimado.** Extraje el texto canónico de `O19`
del commit auditado y conté cuántas de sus líneas no vacías aparecen LITERALMENTE en el sobre
que recibí:

```bash
git show 7aeed6a:docs/owner/ADS-OWNER-RESOLUCIONES.md | awk '/^# /{p=($0~/^# `O19`/)} p' > o19.txt   # 81 líneas
while IFS= read -r l; do [ -z "${l// }" ] && continue; grep -qF -- "$l" SOBRE.txt && hit=$((hit+1)); done < o19.txt
→ líneas no vacías de `O19` = 62 · presentes literalmente en el sobre = 2
```

**Y las dos que coinciden son `---` y la palabra suelta «  incompleta».** Es decir: **CERO
líneas sustantivas.** Las frases exclusivas de `O19`, una a una:

| frase de `O19` | ¿en el sobre? |
|---|---|
| `RATIFICO EL TEXTO AMPLIO` | **NO** |
| `La omisión está en la transcripción del coordinador` | **NO** |
| `Cada revisor debe recibir externamente` | **NO** |
| `debe COMPROBAR LA RECETA` | **NO** |
| `No vuelve a usarse como evidencia primaria` | **NO** |
| `LA RATIFICACIÓN QUEDA CERRADA` | **NO** |
| `Elijo la opción (c)` | **NO** |

**EL SOBRE DE ESTE GATE NO LLEVA EL TEXTO DE LA RATIFICACIÓN.** Lleva su DIGEST, su RECETA de
recálculo, la DECLARACIÓN EXTERNA de que es la resolución ratificada, la RELACIÓN `O19`/`O18`
y **una** frase entrecomillada. **Eso es lo que hay, y no es lo que `O19` L315 ordena
entregar.** `U1` lo rebajó en su `RF-2` a «entrega su DIGEST y su RESUMEN donde la resolución
exige su TEXTO», y **esa redacción es la exacta: la adopto.**

**(d) LO QUE LA MATRIZ HACE CON ÉL, chk L4076** — leído de la tabla, no de la narración:

```text
| `C-20` | CONTRATO_COMPLETO_PARA_F6 | sí | sí | no | SÍ | SÍ | `PLT` implementa · Owner
  acepta | `F6` | `V6-16` · `V6-17` | §20 doc 11 · §11.6 · `O18` |
```

**bloquea_f5 = no · fase = `F6` · prueba_de_cierre = `V6-16` · `V6-17`.**

**(e) LO QUE `V6-16` Y `V6-17` CONTRATAN — leídos enteros, doc 11 L11775 y L11776:**

```text
V6-16  «La prueba se ejecuta desde una RAÍZ DE CONFIANZA EXTERNA al árbol comprobado» ·
       cierre: «el ejecutor NO comparte identidad de escritura con el runtime ADS (`O18`)»
V6-17  «Ningún digest calculado por el mismo árbol basta como prueba de su propia
       integridad» · cierre: «cero afirmaciones de integridad sostenidas sólo por el propio
       árbol»
```

```bash
sed -n '11775,11776p' doc11 | grep -ci 'sobre de ancla\|ratificaci\|texto del Owner'   → 0
```

**NINGUNA DE LAS DOS MENCIONA EL SOBRE, LA RATIFICACIÓN NI EL TEXTO DEL OWNER.** Y recojo el
aviso de método que `U1` se hace a sí mismo, porque lo verifiqué: el barrido ingenuo que
incluye `sobre` a secas devuelve 1 golpe, y **es la preposición** —«los dos coinciden **sobre**
un árbol sano», en `V6-17`—. `U1` lo declaró contra su propio interés antes de afirmar nada.
**Eso es disciplina, y consta.**

**(f) LA PIEZA QUE NINGUNO DE LOS DOS TRAJO, Y QUE ENCUENTRO YO — §11.6 L8595-8603.** La sede
normativa del propio sobre asigna al emisor su **PROPIETARIO y su FASE**, y la fase que le da
NO es `F6`:

```text
EL EMISOR DEL SOBRE,  PROPIETARIO **`PLT`**, que posee el tooling · FASE **ya, para el
MATERIALIZADO         PRÓXIMO gate de `F4c`**, porque sin emisor no hay sobre y sin sobre el
                      gate no cumple `O18`.
```

Y la misma sede, tres renglones más abajo, distingue expresamente lo que **sí** es de `F6`:
«EL SOBRE COMO PARTE DEL CONTRATO DE GATE EN EL KERNEL · FASE **F6**» y «LA SUSTITUCIÓN DE
(b) POR (c) · FASE **F6**». **La sede sabe separar las tres, y pone al emisor en `F4c`.**

**VEREDICTO SOBRE `U1-01` ≡ `U2-01`: REPRODUCE ENTERO, EN LAS SEIS PIEZAS, Y ES MÁS FUERTE DE
LO QUE NINGUNO DE LOS DOS ESCRIBIÓ.** No es sólo que el criterio de cierre no lo cierre: es
que **la fase que la matriz le asigna contradice a la sede normativa del propio artefacto**,
que le da fase `F4c` y propietario `PLT`. **Es un hallazgo SUAVIZADO AL CAMBIARLE LA FASE, en
el sentido literal del §7 del manifiesto (L223), y un contrato SIN CRITERIO DE CIERRE (L222).**

### §2.2 · `U1-02` ≡ `U2-06` · §18 no contiene el verificador, y su paso 8 es PesquerApp — **REPRODUCE**

```bash
awk 'NR>=10758 && NR<=10895' doc11 | grep -ciE 'O20'          → 0
awk 'NR>=10758 && NR<=10895' doc11 | grep -ciE 'V6-'          → 0
awk 'NR>=10758 && NR<=10895' doc11 | grep -ciE 'verificador'  → 0
awk 'NR>=10758 && NR<=10895' doc11 | grep -ciE 'ra[ií]z externa' → 0
awk 'NR>=10758 && NR<=10895' doc11 | grep -c  '§20'           → 0
```

**Cinco ceros.** Y leí el grafo entero: el nodo **8** es «PRIMERA ADOPCIÓN REAL · `O14` ·
`O15` · **PesquerApp PERMANENTE, no un montaje desechable**», y sus dependencias declaradas
son los pasos **0 a 7**, entre los que **no está el verificador de admisión ni la raíz
externa** —que son la PRIMERA y la SEGUNDA responsabilidad que `O20` §3 da a `F6`—.

**Recojo también lo que los dos declaran EN CONTRA de su propio hallazgo, y lo verifiqué:**
la prohibición de PesquerApp **sí existe**, en seis sedes normativas (`O20` §8 sede L423-426 ·
§20.0 L11746-11748 · §20.2 L11787-11789 · §11.8:8866 · `D109`(vi) · `00-INDICE`:104).
**Ninguno de los dos afirma que PesquerApp esté desbloqueada, y yo tampoco.** Lo que se
reproduce es más estrecho y es cierto: **la única sede que ordena la construcción de `F6` y
nombra a PesquerApp como su paso 8 enumera una base que no contiene el verificador.**

### §2.3 · `U1-03` ≡ `U2-04` · `O20` sin fila en §15.4 — **REPRODUCE, y el defecto es AUTODECLARADO**

La regla, escrita por la propia sede (doc 11 L9233-9236, añadida por `P-26`):

```text
esta tabla contiene UNA FILA POR RESOLUCIÓN del Owner, derivada de las cabeceras `### `O` de
la sección 2 de DECISIONES-Y-CONTRADICCIONES.md, y no declara ningún total en su título.
**Una resolución sin fila aquí es el defecto.**
```

```bash
grep -n '^### `O20`' docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md   → 1237
grep -n '^## ' …DECISIONES…                                          → «## 2 · Decisiones que
                                                       pertenecen al Owner» = L549 … L1295
# L1237 está DENTRO de la sección 2: la cabecera EXISTE y la regla la alcanza
sed -n '9238,9261p' doc11 | grep -oE '^\| `O[0-9]+`'   → O7 … O19   (13 filas, sin `O20`)
```

**`O20` tiene cabecera `### \`O20\`` en la sección 2 del registro y NO tiene fila en §15.4.**
Es el defecto por la regla que la propia sede escribe, y es **reincidencia literal de
`P-26`**, que nació de que «`O16` no tenía fila — en la tabla cuyo objeto es declarar dónde
queda cada resolución del Owner».

### §2.4 · `U1-05` ≡ `U2-05` · §15.8 sin bloque para `D109` — **REPRODUCE, y es la TERCERA vez**

La regla 2, escrita por la propia sede (doc 11 L9324-9327, añadida por `P-03`):

```text
EL RECUENTO DE CORRECCIONES SE DERIVA DE LOS BLOQUES `###` DE ESTA SECCIÓN, contados tal como
están, y §0 REMITE aquí en vez de enumerarlos. **Toda tanda nueva abre su bloque EN EL MISMO
ACTO en que escribe sus decisiones: no abrirlo es lo que rompió la derivación DOS VECES.**
```

```bash
sed -n '9310,9661p' doc11 | grep -n '^### ' | tail -2  → «### `D107` · la propagación de `O17`»
                                                          «### `D108` · la propagación de `O18`»
grep -n 'D109' doc11                                    → UNA sola línea: 11723, cabecera de §20
grep -o '^| D[0-9]* |' …DECISIONES… | tail -1           → | D109 |
```

**`D109` existe en el registro (dec L545), es la propagación de `O20`, y NO tiene bloque en
§15.8**, mientras `D107` (propagación de `O17`) y `D108` (propagación de `O18`) —sus dos
homólogas exactas— **sí lo tienen**. La regla dice «lo que rompió la derivación DOS VECES»:
**ésta es la tercera.**

### §2.5 · `U1-04` ≡ `U2-11` · la unificación de la fórmula de líneas va a `V6-04`, que contrata otra cosa — **REPRODUCE**

La matriz, chk L4067, fila `C-11`: fase «`F4c` la afirmación · `F6` la unificación» ·
prueba de cierre «el derivador no dice “ÚNICA SEDE” donde hay tres usos; **la unificación va a
`V6-04`**».

```bash
git show 7aeed6a:…/derivar-universo-obligatorio.py | grep -n 'ÚNICA SEDE'   → 763 (en PASADO: la
                                                    nota de corrección. La mitad `F4c` ESTÁ aplicada)
git show 7aeed6a:…/emitir-sobre-de-ancla.py | grep -n 'count(b"'            → 217 · 372
                                    (dos copias VIVAS; la de 372 publica «85 · 111 · 81 · 107»)
sed -n '11763p' doc11 | grep -ci 'línea\|fórmula\|blob'                     → 0
sed -n '11760,11777p' doc11 | grep -ci 'fórmula'                            → 0
```

**`V6-04` contrata, en sus CUATRO columnas, un censo de LECTURAS DE GIT:** «Inventario
DERIVADO de todas las **lecturas Git**» · entrada «el código del verificador» · salida «censo
de **lecturas**» · cierre «el censo se DERIVA del código; **cero lecturas fuera del canal**».
**`lineas_de_blob` no es una lectura de Git: cuenta `\n` sobre un blob ya leído.** `F6` puede
cerrar `V6-04` entero y las tres copias de la fórmula seguirán vivas **sin contrato que las
reclame**. **`O20` §1 exige «asignación INEQUÍVOCA de cada obligación a `F5` o a `F6`»: ésta
está asignada a un contrato ajeno, que no es asignar.**

### §2.6 · `U2-02` ≡ `U1-08` · `V6-15` exige «los once árboles» y su entrada cubre tres gates — **REPRODUCE, y le doy la razón a `U2`**

`V6-15`, doc 11 L11774, en sus cuatro columnas relevantes:

```text
QUÉ DEBE DEMOSTRAR   «Los controles adversariales del SEXTO, SÉPTIMO y OCTAVO gate quedan
                      como FIXTURES OBLIGATORIOS»
ENTRADA              «documentos 27, 28 y 29»
ESCENARIO NEGATIVO   «**los once árboles** vuelven a dar ROJO, uno a uno»
CIERRE               «**cada** control de **los tres gates** presente, con su identificador»
```

**El censo de los once, DERIVADO por mí del propio corpus:**

```bash
grep -nE 'EL (OCTAVO|NOVENO|DÉCIMO|UNDÉCIMO) ÁRBOL' CHECKPOINT-ADS-NEXT.md doc29
→ OCTAVO   = `DD-01`, QUINTO GATE,  documento 26   (chk:3854, y chk:4464 lo confirma)
  NOVENO   = `EE-01`, SEXTO GATE,   documento 27   (chk:3944)
  DÉCIMO   =          SÉPTIMO GATE, documento 28   (doc29:3239)
  UNDÉCIMO = `T1-01`, OCTAVO GATE,  documento 29   (doc29:1, :41, :681)
```

**El OCTAVO árbol es del QUINTO gate, documento 26, que NO está en la entrada de `V6-15`.** Y
los árboles 1-7 son de gates aún anteriores. **La entrada cubre 3 de los 8 gates y 3 de los 11
árboles.**

```bash
git grep -i 'once árboles'   → 4 golpes (sede:361 · doc11:11735 · doc11:11774 · chk:3998)
                               los CUATRO narrativos. **NINGUNA sede enumera los once.**
```

**AQUÍ DISCREPO DE `U1` Y ADOPTO LA LECTURA DE `U2`, y digo por qué.** `U1`, en su `RF-9`, se
rebajó a sí mismo de GRAVE a MEDIO razonando que «la clase está especificada porque el
criterio de cierre nombra tres documentos». **Ese razonamiento resuelve la fila eligiendo una
de sus dos columnas y descartando la otra — que es exactamente lo que un constructor NO puede
hacer sin volver a decidir.** Una fila cuyo escenario negativo exige **once** y cuyo criterio
de cierre entrega **tres** no es imprecisa: **es insatisfacible por su propia letra**, y quien
la construya tiene que elegir cuál de las dos columnas gobierna. Eso es «una obligación
depende de INTERPRETACIÓN HUMANA NO NORMADA» (§7 L226) y «la MATRIZ ADVERSARIAL no especifica
una clase reproducida» (§7 L224): **la clase del OCTAVO árbol —el perímetro de `DD-01`, con su
control positivo `docs/owner/sentencia.pyc` REPRODUCIDO y ejecutado (chk:3854)— no tiene
fixture contratado en ninguna de las dieciocho filas.** `U1-08` cae en su rebaja; `U2-02` se
sostiene. **La reincorporo como GRAVE.**

### §2.7 · `U2-03` · «Fase de TODOS: `F6`» frente a `PN-19`, cuya fase es `F5` — **REPRODUCE**

```bash
awk 'NR>=11721 && NR<=11791' doc11 | grep -oE '§[0-9.]+|`PN-[0-9]+`|`[OD][0-9]+`|`F5`' | sort -u
→ `D109`  `O18`  `O20`      — y NADA MÁS
```

**§20 entera —las 71 líneas del contrato— no cita `§11.6`, ni `§11.7`, ni `§11.8`, ni
`PN-19`, ni `F5`, ni una sola sede fuera de `O18`, `O20` y `D109`.** Y declara, L11755:
«**Fase de TODOS: `F6`.**»

`PN-19` (doc 11 L10517-10728) dice de esa misma materia: el verificador externo «exige una
identidad de escritura SEPARADA y evidencia FUERA del árbol, y **ninguna sede aprobada las
contempla**» — enfrentadas `C7`, `E2.4`, `KERNEL.md` `G20`-`G23`, (a) y (b) —, y §16 se titula
«**Presiones normativas para F5**».

**Recojo la autocorrección que `U2` se impone en su `RF-4`, y la comparto: la decisión NO está
OCULTA.** `PN-19` la declara entera, con materia mínima, propietario, fase y prueba posterior
que falla hoy. **Lo que reproduce, y es distinto, es que §20 —la sede que se presenta a sí
misma como «escrito completo para que se pueda construir sin volver a decidir nada»
(L11729-11730)— asigna fase `F6` a `V6-16` sin advertir que su norma habilitante es una
presión de `F5` sobre material APROBADO.** `O20` §1 exige «asignación **INEQUÍVOCA** de cada
obligación a `F5` o a `F6`». **Dentro del contrato, no lo es.**

### §2.8 · Los hallazgos que reproduzco pero NO deciden

| id | qué comprobé | ¿reproduce? |
|---|---|---|
| `U1-06` ≡ `U2-07` | §11.6 campo 17 (L8427) «`O17`, `O18` y `O19`, nombrados uno a uno» · campo 18 (L8429) · obligación `6bis` (L8484-8486) «los digests de `O17`, `O18` y `O19`». Y `emitir-sobre-de-ancla.py:143` → `RESOLUCIONES_EXIGIDAS = ("O17","O18","O19")`, con `:141` diciendo «PUBLICA son **todas** las que la sede contenga». **La NORMA exige tres; el INSTRUMENTO publica cuatro** | **SÍ** · un sobre futuro que anclase sólo `O17`-`O19` cumpliría §11.6 al pie de la letra y **no anclaría `O20`**. Hoy no ocurre: mi sobre trae `O20`, y lo verifiqué |
| `U2-08` | chk L1185-1191: fragmento de columna derecha **SIN SUJETO** —su fila izquierda la borró el remedio de `S2-03`— que dice «GATE INVÁLIDO · VEREDICTO INSUFICIENTE · **`C-L.5` pasa a ABIERTA** · … aquí se REMITE y **no se copia, por la regla 1**». Y la enumeración de `based_on` (L1195-1207) llega a `O18`·`D108` y **no contiene `O19`, `O20` ni `D109`**, contra la regla 4 (L975-978). El bloque se rotula VIGENTE, «SIN rótulo histórico» (L956-957) | **SÍ, en las tres partes** |
| `U2-09` | chk L2112-2113 y L2121-2123, campo `owner_captado`: «donde viven `O17`, `O18` … y `O19`» y «**NINGUNA de las tres** autoriza iniciar F5, F6 ni PesquerApp». `grep -o '^# \`O[0-9]*\`' sede` → **`O17` `O18` `O19` `O20`**: son **cuatro** | **SÍ** |
| `U1-09` ≡ `U2-12` | §19 L10901-10913 censa las familias de contrato de prueba y **no nombra `V6-01`-`V6-18`**. `grep -n 'V6-' doc11` fuera de §20.1 → vacío | **SÍ** |
| `U1-07` | `comprobar-…py` L2243, L2283 y L3009 rotulan **`O20`** la regla APPEND-ONLY de la sede, y L2283 **la IMPRIME en el informe**. El texto canónico de `O20` no la contiene; el propio fichero la atribuye bien a `O19` en L3395 | **SÍ** · es la clase de la que nació `O19` («una paráfrasis nunca puede ampliar la autoridad del texto canónico»), aunque el contenido atribuido sea CIERTO |
| `U1-10` | `derivar-…py` L494-536, componente (v) del `ENCARGO`: sigue diciendo «los 24 hallazgos del documento **21**» y «el emisor del SOBRE DE ANCLA, **que este gate estrena**» — el sobre se estrenó cuatro gates atrás | **SÍ** · sólo AÑADE rutas y el universo no encoge |
| `U2-13` | `awk 'NR==872' DECISIONES \| grep -oP '\S > \S' \| wc -l` → **4**. Marcador de cita incrustado a mitad de frase, cuatro veces, en la nota que aplica `C-21` | **SÍ** |
| `U2-14` | chk L38-42 y `00-INDICE`:104 escriben a mano «catorce» y «ocho», donde chk L4025 ordena «**El recuento NO se escribe: se DERIVA**». Derivado: 14 y 8 — **ciertos hoy** | **SÍ, y es verdadero hoy** |

### §2.9 · Lo que CAE

| afirmación | por qué cae |
|---|---|
| **`U2-10`** · «tres sedes dicen “once campos cada uno” y **`fuente` no existe** ni por fila ni globalmente por punto» | **CAE en su parte decisiva.** La FUENTE **sí** está, y globalmente: doc 11 L11723, «TODO LO DE ESTA SECCIÓN ES DERIVADO DE `O20`, VÍA `D109`», con la sede canónica nombrada y su regla de precedencia. Es una **cuantificación universal sobre los dieciocho**, igual que «Propietario global: `SIS`» y «Fase de TODOS: `F6`», que `U2` sí acepta como válidas. **No se puede admitir la cuantificación para tres campos y negarla para el cuarto.** `U1` §3.0 lo resolvió bien. Lo que queda —que la descripción «once campos **cada uno**» invite a buscar once columnas donde hay nueve— es **LEVE y no decide nada**. **Y anoto lo único sustantivo que hay debajo:** `V6-12` deriva de `O19` y de las reglas propias de la sede, **no de `O20`**, de modo que la fuente global es imprecisa para esa fila. Sigue siendo LEVE |
| **`U1-08`** en su REBAJA (`RF-9`) | **CAE la rebaja, no el hecho.** Ver §2.6: `U1` resolvió la contradicción de la fila eligiendo una columna, que es lo que un constructor no puede hacer. **Rige la lectura de `U2-02`** |
| **`U1-01` como causa de INVALIDEZ del gate** | `U1` mismo lo descarta en su `RF-10` y **coincido**: `O19` y §11.6 hacen FALLAR CERRADO al gate si **la sede no coincide con la huella recibida**, y coincide —lo recalculé en los dos commits y en las cuatro resoluciones—. **El disparador de invalidez es la DISCREPANCIA, no la incompletitud de la lista.** El gate es VÁLIDO; el hallazgo es de SUFICIENCIA |
| **`U2` sobre la viñeta añadida por `D109`(v)** | `U2` lo retira él mismo en su `RF-2` y **coincido**: la viñeta ENDURECE («todo el que permita un falso verde bloquea `F6` y PesquerApp»), es derivable de `O20` §6 leído con §8, y la obligación 6 del sobre castiga la ampliación **de autoridad**, no el rigor. **No es hallazgo** |

---

## §3 · TABLA CONSOLIDADA Y DEDUPLICADA

### §3.1 · Qué FUSIONO y qué NO

```text
FUSIONO, y son SEIS PARES · misma sede, mismo hecho, misma regla violada
  H-01  `U1-01` ≡ `U2-01`   `C-20`, chk:4076, contra sede:315-317 y doc11:8449-8459
  H-02  `U1-02` ≡ `U2-06`   §18, doc11:10758-10895
  H-03  `U1-03` ≡ `U2-04`   §15.4, doc11:9227-9261
  H-04  `U1-05` ≡ `U2-05`   §15.8, doc11:9310-9661
  H-05  `U1-04` ≡ `U2-11`   `C-11` → `V6-04`, chk:4067 y doc11:11763
  H-06  `U1-08` ≡ `U2-02`   `V6-15`, doc11:11774  — **con la lectura de `U2`, no la de `U1`**
  H-07  `U1-06` ≡ `U2-07`   §11.6 campos 17/18 y `6bis`, doc11:8427-8429 y 8484-8486
  H-08  `U1-09` ≡ `U2-12`   §19, doc11:10901-10913

NO FUSIONO, y digo por qué
  `U2-03` con `H-01`      distinta sede (§20.1 L11755 frente a chk:4076), distinta regla
                          (`O20` §1 «asignación inequívoca» frente a `O20` §6 «no esconder»)
                          y distinto remedio. **Son dos.**
  `U2-08` con `U2-09`     el mismo bloque, pero distinto campo y distinta regla violada
                          (`based_on` contra la regla 4 · `owner_captado` contra la regla 1).
                          `U2` no las fusionó y hace bien: fusionarlas ocultaría una
  `U2-14` con `H-08`      un cardinal copiado y un censo corto no son el mismo defecto
  `U1-07` con nada        atribución al Owner en el instrumento. Solo
  `U1-10` con nada        cláusula de encargo caducada en el derivador. Solo
  `U2-13` con nada        corrupción tipográfica. Sola
```

**Ocho pares fusionados y ocho hallazgos únicos: `10 + 14 = 24` filas de entrada → `16`
hallazgos consolidados.**

### §3.2 · La tabla

> **CLASE, con la sede que fija la frontera: `DD-20`, chk L3678-3712.** `A` = «el defecto está
> EN EL CORPUS y la batería lo da por bueno; que el fichero esté o no CONFIRMADO es
> IRRELEVANTE: el objeto que un gate juzga es un COMMIT». `B` = exige una decisión NUEVA del
> Owner. `C` = corromper la REFERENCIA contra la que se compara — «es contrato de `F6`, y NO
> es exigible dentro de `F4c`».
>
> **CORRIJO EXPRESAMENTE CUATRO CLASIFICACIONES DE `U1`.** `U1` puso clase `C` a `U1-07`,
> `U1-08`, `U1-09` y `U1-10`. **Ninguno de los cuatro corrompe la referencia**: los cuatro son
> defectos EN EL CORPUS que la batería da por buenos, que es la definición literal de `A` en
> `DD-20`. **Los reclasifico `A`.** No cambia el veredicto y lo digo igual.

| # | fusiona | severidad | clase | sede · fichero:línea | qué falla | REINCIDENCIA |
|---|---|---|---|---|---|---|
| **`H-01`** | `U1-01`≡`U2-01` | **BLOQUEANTE** | **A** | chk:**4076** · sede:**315-317** · doc11:**8449-8459** · doc11:**8595-8603** | `C-20` —el sobre no lleva el TEXTO de la ratificación— pasa a fase `F6` con `V6-16`/`V6-17` de criterio de cierre, **que no lo contienen**, mientras §11.6 da al emisor fase «**ya, para el PRÓXIMO gate de `F4c`**». **Reproduce en el sobre de ESTE gate** | **SÍ** · `C-20` es `T2-11` del octavo gate, SOSTENIDO y clase `A`; su remedio se aparcó en vez de aplicarse |
| **`H-02`** | `U1-02`≡`U2-06` | **GRAVE** | **A** | doc11:**10758-10895** (§18) | La sede del ORDEN DE CONSTRUCCIÓN de `F6` no contiene el verificador ni la raíz externa, y enumera como base de su paso 8 —PesquerApp PERMANENTE— unos pasos 0-7 que no los incluyen | NUEVA · la tanda de `O20` no tocó §18 |
| **`H-03`** | `U1-03`≡`U2-04` | **GRAVE** | **A** | doc11:**9227-9261** (§15.4) | `O20` sin fila en la tabla cuyo objeto es «dónde queda cada resolución del Owner», **contra su propia regla y su propia sanción** | **SÍ** · reincidencia LITERAL de `P-26`, que nació de lo mismo con `O16` |
| **`H-04`** | `U1-05`≡`U2-05` | **GRAVE** | **A** | doc11:**9310-9661** (§15.8) | La tanda de `O20` escribió `D109` en el registro y **no abrió su bloque**, mientras `D107` y `D108` —sus dos homólogas— sí lo hicieron | **SÍ, y es la TERCERA** · la regla de `P-03` dice «no abrirlo es lo que rompió la derivación **dos veces**» |
| **`H-05`** | `U1-04`≡`U2-11` | **GRAVE** | **A** | chk:**4067** · doc11:**11763** | La mitad `F6` de `C-11` —unificar la fórmula de líneas, viva en `emitir…py:217` y `:372`— se enruta a `V6-04`, cuyas cuatro columnas contratan un censo de **lecturas de Git** | **SÍ** · misma forma que `H-01`: obligación colgada de un contrato ajeno |
| **`H-06`** | `U1-08`≡`U2-02` | **GRAVE** | **A** | doc11:**11774** (`V6-15`) | Escenario negativo «los **once** árboles» contra entrada «documentos 27, 28 y 29» y cierre «los **tres** gates». **El OCTAVO árbol es del QUINTO gate, doc 26**, fuera de la entrada; los once no se enumeran en ninguna sede. `O20` §3 manda «matriz adversarial **COMPLETA**» | NUEVA |
| **`H-07`** | `U2-03` | **GRAVE** | **A** | doc11:**11755** contra doc11:**10517-10728** (`PN-19`) | §20 declara «Fase de TODOS: `F6`» y **no cita `PN-19`, `F5`, §11.6, §11.7 ni §11.8 en sus 71 líneas**, mientras la norma habilitante de `V6-16` es una presión de `F5` sobre material APROBADO. `O20` §1 exige asignación **inequívoca** | NUEVA |
| **`H-08`** | `U1-06`≡`U2-07` | MEDIO | **A** | doc11:**8427**, **8429**, **8484-8486** | §11.6 y la obligación `6bis` exigen anclar **tres** resoluciones. Un sobre futuro que anclase sólo `O17`-`O19` cumpliría la norma **y no anclaría `O20`** | NUEVA · el INSTRUMENTO ya deriva todas (`emitir…py:141`); la NORMA no se actualizó |
| **`H-09`** | `U2-08` | MEDIO | **A** | chk:**1185-1191** y **1195-1207** | Fragmento HUÉRFANO sin sujeto, superviviente del remedio de `S2-03`, que **copia un estado** («`C-L.5` pasa a ABIERTA») en la misma frase que dice «aquí se REMITE y no se copia, por la regla 1»; y `based_on` no se reancló para `O19`/`O20`/`D109`, contra la regla 4 | **SÍ** · `C-08` cerró la INSTANCIA en este mismo campo y dejó la CLASE abierta. Mantiene `C-L.7` viva |
| **`H-10`** | `U2-09` | MEDIO | **A** | chk:**2112-2113**, **2121-2123** | `owner_captado` enumera «`O17`, `O18` y `O19`» y dice «**ninguna de las tres**» donde la sede publica **cuatro**, en el campo cuyo objeto es decir dónde vive lo que el Owner resolvió | **SÍ** · clase `C-06`/`C-07`/`C-08`, el bloque vuelve a escribir lo que declara no escribir |
| **`H-11`** | `U1-07` | MENOR | **A** | `comprobar-…py`:**2243**, **2283**, **3009** | Tres rótulos atribuyen a **`O20`** la regla APPEND-ONLY, que `O20` no contiene; `:2283` la IMPRIME en el informe. El propio fichero la atribuye bien a `O19` en `:3395` | **SÍ de CLASE** · es la clase de la que nació `O19` y que `Y-05`/`X-O13` cerraron para `(c)` |
| **`H-12`** | `U1-09`≡`U2-12` | MENOR | **A** | doc11:**10901-10913** (§19) y **432-439** | Las dos sedes que censan las familias de contrato de prueba **no nombran `V6-01`-`V6-18`**, la más nueva | **SÍ de CLASE** · `DD-10`/`DD-13` cerraron lo mismo cuando faltaba `X-O` |
| **`H-13`** | `U1-10` | MENOR | **A** | `derivar-…py`:**494-536** | El componente (v) del `ENCARGO` —«el objeto que **ESTE** gate juzga»— sigue describiendo el OCTAVO gate: documento 21, y «el emisor … **que este gate estrena**» | NUEVA · el universo no encoge y todas las guardas se cumplen |
| **`H-14`** | `U2-10` | LEVE | **A** | dec:**545** · chk:**4195-4196** · `00-INDICE`:**104** | «DIECIOCHO puntos, **cada uno** con … once campos» cuando la tabla da 8 por fila y 3 globales. La FUENTE **sí** está, globalmente (doc11:11723): **es descripción imprecisa, no campo ausente** | **SÍ de CLASE** · `C-05`, «ninguna frase afirma lo que su tabla no dé» |
| **`H-15`** | `U2-13` | LEVE | **A** | dec:**872** | Marcador de cita `> ` incrustado a mitad de frase **cuatro veces** en una línea de 419 caracteres, en la nota que aplica `C-21` | NUEVA · aislada: `grep -cP '^> .*\S > \S'` da 1 en seis fuentes |
| **`H-16`** | `U2-14` | LEVE | **A** | chk:**38-42** · `00-INDICE`:**104** | «catorce» y «ocho» escritos a mano donde chk:4025 ordena «El recuento NO se escribe: se DERIVA». **Ciertos hoy** | **SÍ de CLASE** · `C-16`/`J-07`/`EE-07` |

### §3.3 · Recuento, derivado de la tabla

```text
POR SEVERIDAD     BLOQUEANTE  1   H-01
                  GRAVE       6   H-02 · H-03 · H-04 · H-05 · H-06 · H-07
                  MEDIO       3   H-08 · H-09 · H-10
                  MENOR       3   H-11 · H-12 · H-13
                  LEVE        3   H-14 · H-15 · H-16
                                 ──
                                 16

POR CLASE         A  16   TODOS
                  B   0   **ninguno exige una decisión NUEVA del Owner**
                  C   0   ninguno corrompe la referencia. Las cuatro clases `C` de `U1` las
                          reclasifico `A` contra `DD-20`, y lo declaro en §3.2

REINCIDENCIAS     8 de 16   H-01 · H-03 · H-04 · H-09 · H-10 · H-11 · H-12 · H-16
                  de ellas, DOS son reincidencias LITERALES de un remedio cerrado por un
                  gate anterior sobre la MISMA sede: `H-03` (`P-26`) y `H-04` (`P-03`, y
                  es la TERCERA vez que la regla se rompe)

NINGUNO ES        «el verificador de `F6` no está implementado». Lo verifiqué hallazgo a
                  hallazgo: los dieciséis son defectos ARQUITECTÓNICOS o DOCUMENTALES, que
                  `O20` §6 mantiene expresamente bloqueando `F4c`
```

---

## §4 · LOS DIECIOCHO CONTRATOS DE §20, UNO A UNO

### §4.0 · Los ONCE CAMPOS: dónde vive cada uno

Tres sedes (`D109`(iii) en dec:545, chk:4195-4196, `00-INDICE`:104) afirman que los dieciocho
llevan **fuente · propietario · implementador · fase · entrada · salida · evidencia ·
escenario positivo · escenario negativo · condición de bloqueo · criterio exacto de cierre**.
**Lo he contrastado contra la tabla, columna a columna:**

```bash
sed -n '11758p' doc11 | tr '|' '\n'
→ # · qué debe demostrar `F6` · entrada · salida · evidencia · escenario POSITIVO ·
  escenario NEGATIVO · condición de BLOQUEO · criterio EXACTO de cierre        (9 columnas)
```

```text
DE FILA · 7      entrada · salida · evidencia · escenario POSITIVO · escenario NEGATIVO ·
                 condición de BLOQUEO · criterio EXACTO de cierre
GLOBALES · 4     FUENTE          L11723  «TODO LO DE ESTA SECCIÓN ES DERIVADO DE `O20`, VÍA
                                 `D109`», con sede canónica y regla de precedencia
                 PROPIETARIO     L11753  «Propietario global de la especificación: `SIS`»
                 IMPLEMENTADOR   L11753  «Implementador: `PLT`» (+ `VER` dosier, `SEG`
                                 bloqueo, **Owner** autoridad de aceptación indelegable)
                 FASE            L11755  «Fase de TODOS: `F6`»
```

**LOS ONCE CAMPOS ESTÁN.** Cuatro por cuantificación universal, y su atribución es
inequívoca. **No lo cuento como defecto** — y por eso `U2-10` cae en §2.9.

### §4.1 · Los dieciocho, con mi veredicto de completitud

> **Criterio que aplico, y es el que `O20` §1 y el manifiesto §7 fijan:** ¿tiene los once
> campos? ¿es su criterio de cierre EXACTO y MEDIBLE **sin interpretación humana no
> normada**? ¿se puede **construir sin volver a decidir arquitectura**?

| # | 11 campos | criterio de cierre | ¿medible sin interpretación? | ¿construible sin re-decidir? | **VEREDICTO** |
|---|---|---|---|---|---|
| `V6-01` | SÍ | «**cero** lecturas de lista con separador contenible» | **SÍ** · umbral 0 sobre un censo | **SÍ** | **COMPLETO** |
| `V6-02` | SÍ | «**todas** las lecturas con `-z`; ninguna decodificación laxa» | **SÍ** · universal con contraejemplo único | **SÍ** | **COMPLETO** |
| `V6-03` | SÍ | «los **tres** casos producen ROJO y **nombran la causa**» | **SÍ** · los tres van enumerados en la propia fila | **SÍ** | **COMPLETO** |
| `V6-04` | SÍ | «el censo se DERIVA del código; **cero** lecturas fuera del canal» | **SÍ** | **SÍ** | **COMPLETO EN SU OBJETO** · pero DOS sedes le cuelgan una obligación que su texto no contiene → **`H-05`** |
| `V6-05` | SÍ | «**cero** rutas gobernadas exentas por preexistencia» | **SÍ** | **SÍ** | **COMPLETO** |
| `V6-06` | SÍ | «las **seis** letras cubiertas; `R` y `C` por sus dos puntas» | **SÍ** · cardinal cerrado y explícito | **SÍ** | **COMPLETO** |
| `V6-07` | SÍ | «cada comprobación **declara** su referencia, y la declarada es la usada» | **SÍ** · contraste declarado/usado | **SÍ** · los cuatro estados van nombrados | **COMPLETO** |
| `V6-08` | SÍ | «**cero** comprobaciones cuyo veredicto MEJORE al confirmar» | **SÍ** · propiedad monótona | **SÍ** | **COMPLETO** |
| `V6-09` | SÍ | «**cero** rutas gobernadas sin guarda por su antigüedad» | **SÍ** | **SÍ** | **COMPLETO** |
| `V6-10` | SÍ | «el censo de zonas se DERIVA; **cero** zonas sin condición» | **SÍ** | **SÍ** | **COMPLETO** |
| `V6-11` | SÍ | «**cero** rutas del propio verificador exentas» | **SÍ** | **SÍ** | **COMPLETO** |
| `V6-12` | SÍ, con una salvedad de FUENTE | «el contraste se hace contra el **commit de creación**» | **SÍ** · derivable con `--diff-filter=A` | **SÍ** | **COMPLETO** · salvedad: su fuente real es `O19` y las reglas de la sede, **no `O20`**, y la fuente global de §20 dice `O20`. Es `H-14`, LEVE |
| `V6-13` | SÍ | «las **seis** formas con fixture positivo y negativo» | **SÍ** · las seis van enumeradas | **SÍ** | **COMPLETO** |
| `V6-14` | SÍ | «las **seis** con fixture positivo y negativo» | **SÍ** | **SÍ** | **COMPLETO** |
| `V6-15` | SÍ | «**cada** control de **los tres gates** presente, con su identificador de origen» | **NO** · su ESCENARIO NEGATIVO exige «los **once** árboles» y su ENTRADA da tres gates. **Quien construya tiene que ELEGIR qué columna gobierna** | **NO sin elegir** | **INCOMPLETO · SE CONTRADICE A SÍ MISMO** → **`H-06`** |
| `V6-16` | SÍ | «el ejecutor NO comparte identidad de escritura con el runtime ADS (`O18`)» | **SÍ** · propiedad binaria | **NO desde §20** · su norma habilitante es `PN-19`, presión de **`F5`** sobre material APROBADO, y §20 no la cita ni cita §11.8 | **INCOMPLETO POR ENLACE Y POR FASE** → **`H-07`**; y su contrato largo (§11.8, dieciséis exigencias) **no está enlazado desde §20** |
| `V6-17` | SÍ | «**cero** afirmaciones de integridad sostenidas sólo por el propio árbol» | **SÍ** | **SÍ en su objeto** | **COMPLETO EN SU OBJETO** · pero `C-20` le cuelga una obligación que no contiene → **`H-01`** |
| `V6-18` | SÍ | «`falsos_verdes = 0` **y** `falsos_rojos = 0`, **medidos y publicados**» | **SÍ** · el más duro y el más exacto de los dieciocho | **SÍ** | **COMPLETO** |

### §4.2 · Recuento, y la respuesta directa a la pregunta encargada

```text
CON LOS ONCE CAMPOS                       18 de 18
CON CRITERIO DE CIERRE EXACTO Y MEDIBLE   17 de 18   — falla `V6-15`
CONSTRUIBLES SIN VOLVER A DECIDIR         16 de 18   — fallan `V6-15` y `V6-16`
CON UNA OBLIGACIÓN AJENA COLGADA ENCIMA    2 de 18   — `V6-04` (`H-05`) y `V6-17` (`H-01`)
```

**¿SE PUEDE CONSTRUIR CADA UNO SIN VOLVER A DECIDIR ARQUITECTURA? NO: DOS NO.**

- **`V6-15`** obliga a elegir entre dos columnas incompatibles de su propia fila. Elegir es
  decidir, y `O20` §1 dice que eso es de `F4c`.
- **`V6-16`** exige un ejecutor con identidad de escritura separada y evidencia fuera del
  árbol, y `PN-19` (doc11:10570-10574) declara que **«ninguna sede aprobada las contempla»**,
  con **fase `F5` y propietario el Owner**. §20 no lo dice. **Quien construya `V6-16` leyendo
  sólo §20 —que se presenta como «escrito completo para que se pueda construir sin volver a
  decidir nada»— construye sin norma que lo autorice.**

### §4.3 · Contraste literal contra los NUEVE encargos de `O20` §3

| encargo de `O20` §3 (sede L382-392) | cubierto por | ¿cubierto? |
|---|---|---|
| implementar el VERIFICADOR DE ADMISIÓN | `V6-05` `V6-09` `V6-10` `V6-11` `V6-18` | **SÍ** |
| implementar la RAÍZ EXTERNA DE CONFIANZA de `O18`/`O19` | `V6-16` `V6-17` (+§11.8, no enlazada) | **SÍ en sustancia · NO en enlace ni en fase** (`H-07`) |
| cerrar las LECTURAS GIT SEGURAS | `V6-01`-`V6-04` | **SÍ** |
| comprobar MUTACIONES de ficheros nuevos y preexistentes | `V6-05` `V6-08` `V6-09` | **SÍ** |
| tratar CODIFICACIONES NO UTF-8 | `V6-02` `V6-03` `V6-13` | **SÍ** |
| `A`, `M`, `D`, `R` y CAMBIOS DE TIPO | `V6-06` `V6-14` — y **añaden `C`**, que `O20` no nombra: **amplía en la dirección segura** | **SÍ** |
| impedir la AUTO-EXCLUSIÓN de la definición y la regla | `V6-11` | **SÍ** |
| ejecutar la MATRIZ ADVERSARIAL **COMPLETA** | `V6-15` `V6-18` | **NO** · `V6-15` la acota a 3 de 11 árboles (`H-06`) |
| CERTIFICAR antes de declarar ADS operativo o iniciar PesquerApp | §20.0:11746-11748 · §20.2:11787-11789 | **SÍ en §20 · NO en §18** (`H-02`) |

**Siete de los nueve encargos están cubiertos sin reserva. Dos no: la matriz adversarial
completa y la raíz externa.**

---

## §5 · LAS CUESTIONES ENCARGADAS, RESUELTAS EXPRESAMENTE

### §5.1 · ¿Están COMPLETOS los DIECIOCHO contratos de §20?

**NO. DIECISÉIS SÍ; DOS NO.** El detalle, uno a uno, está en §4.1. Los once campos están en
los dieciocho —cuatro por cuantificación universal—; el criterio de cierre es exacto y
medible en diecisiete; y **dos no se pueden construir sin volver a decidir**: `V6-15`, que se
contradice entre su escenario negativo y su criterio de cierre, y `V6-16`, cuya norma
habilitante es una presión de `F5` que §20 no cita. **Y dos más, `V6-04` y `V6-17`, cargan
obligaciones ajenas que su texto no contiene y que su cierre no puede cerrar.**

### §5.2 · ¿Queda alguna DECISIÓN ARQUITECTÓNICA sin tomar, u OCULTA detrás de una obligación de `F6`?

**OCULTA, NO. SIN TOMAR, UNA — y está declarada, con propietario y fase.**

**Ninguna decisión está escondida.** Lo verifiqué recorriendo las presiones normativas de
§16: `PN-13`, `PN-16`, `PN-17`, `PN-18` y `PN-19` llevan cada una materia mínima, alcance, qué
bloquea, qué NO bloquea, condición de reversión, propietario, fase y prueba posterior que
FALLA HOY. **Eso no es arquitectura sin decidir: es una decisión identificada, acotada y
remitida a quien tiene autoridad.** `U2` retiró expresamente la palabra «oculta» de su
`U2-03` en su `RF-4`, y **hace bien; lo confirmo**.

**Lo que sí queda es peor de nombrar y más fácil de arreglar: `PN-19` —la única decisión
pendiente que un contrato de §20 necesita— tiene fase `F5`, y §20 declara «Fase de TODOS:
`F6`» sin citarla.** No está oculta en el corpus; **está ausente del contrato**. `O20` §7
exige del gate que autorice `F5` que confirme «que las obligaciones pendientes de `F6` **NO
ocultan una decisión arquitectónica**». No la ocultan. Pero `O20` §1 exige además
«**asignación INEQUÍVOCA de cada obligación a `F5` o a `F6`**», y **`V6-16` la tiene
equívoca**. Es `H-07`.

### §5.3 · ¿Se ha ESCONDIDO o SUAVIZADO algún hallazgo al cambiarle la fase?

# **SÍ. UNO: `C-20`.**

Es la pregunta a la que `U1` y `U2` responden que SÍ por dos vías distintas, y **la reproduje
entera en §2.1, con una sexta pieza que ninguno de los dos trajo.** El resumen del hecho:

```text
LO QUE `C-20` ES        `T2-11` del octavo gate: el SOBRE no lleva el TEXTO de la ratificación
                        del Owner, que `O19` L315 ordena y §11.6 L8454 repite como el PRIMERO
                        de «la lista entera». Clase `A`, SOSTENIDO, y su adjudicador lo
                        verificó «contra mi propio sobre» (doc29:3394)
QUÉ SE HIZO CON ÉL      estado `CONTRATO_COMPLETO_PARA_F6` · fase `F6` · bloquea_f5 **no** ·
                        prueba de cierre `V6-16` · `V6-17`
POR QUÉ ES SUAVIZAR     (i) `V6-16` y `V6-17` **no lo contienen**: `F6` los cierra enteros y
                        `C-20` sigue vivo · (ii) `O20` §6 sólo manda a `F6` los defectos de
                        IMPLEMENTACIÓN DEL VERIFICADOR, y éste es DOCUMENTAL, del ancla que
                        `O18(b)` adoptó **para poder cerrar `F4c` sin `F6`** · (iii) **§11.6
                        L8595-8603 le da al emisor fase «ya, para el PRÓXIMO gate de `F4c`»**,
                        y la matriz lo pone en `F6` contra su propia sede normativa ·
                        (iv) **reproduce en el sobre de ESTE gate**, no es histórico
```

**Los otros veintiuno reparten bien**, y lo comprobé fila a fila contra la clasificación de
origen del documento 29: los ocho `CONTRATO_COMPLETO_PARA_F6` son, uno a uno, defectos de la
implementación del verificador interno —que es lo que `O20` §6 manda mover—, y los catorce
`CORREGIDO_EN_F4c` son documentales o de reparto. **Ninguno se declara SUPERADO**, y la
cabecera de la matriz lo prohíbe expresamente (chk:4049-4050).

### §5.4 · ¿Podría PesquerApp iniciarse antes de certificar `F6`?

**NO. LA PROHIBICIÓN ES EXPLÍCITA Y ESTÁ EN SEIS SEDES, Y NINGUNA DE ELLAS FLAQUEA.**

```text
`O20` §8, SEDE CANÓNICA L425-426   «PesquerApp sigue BLOQUEADA hasta que `F6` implemente y
                                   certifique estos contratos. No se autoriza MVP, ni piloto
                                   desechable, ni adopción parcial»
doc 11 §20.0 L11746-11748          «hasta entonces PesquerApp está BLOQUEADA: sin MVP, sin
                                   piloto desechable y sin adopción parcial»
doc 11 §20.2 L11787-11789          «LA CONDICIÓN PREVIA A PesquerApp es que `F6` los
                                   implemente **y los certifique**»
doc 11 §11.8 L8866                 el verificador externo «construido **y PROBADO** antes de
                                   la adopción permanente»
`D109`(vi), dec:545                «PesquerApp queda BLOQUEADA sin MVP, sin piloto
                                   desechable y sin adopción parcial»
`00-INDICE`:104 · chk:44-45        lo mismo, con las mismas tres exclusiones
```

**Y el manifiesto del propio gate lo declara en su §1: «PesquerApp BLOQUEADA».**

**PERO —y es `H-02`— la única sede que ORDENA LA CONSTRUCCIÓN de `F6` y nombra a PesquerApp
como su PASO 8 no lleva la condición.** §18 enuncia una condición de entrada para el paso 8
—«la BASE COMPLETA ACORDADA de los pasos 0 a 7»— y **esa base no contiene el verificador**.
Una sede que enuncia la condición equivocada no es lo mismo que una que calla. **No digo que
PesquerApp esté desbloqueada: digo que quien planifique `F6` desde su propio orden de
construcción llega al paso 8 sin encontrarla, y que la tanda de `O20` no tocó §18.**

### §5.5 · LA MATRIZ DE LOS 22

**Derivada con los tres comandos que la propia matriz publica (chk:4027-4041), corridos por mí:**

```bash
awk '/^### La tabla de los 22/{t=1} t' chk | grep -oE '^\| `C-[0-9]+`' | sort -u | wc -l   → 22
… | grep -oE '\| (CORREGIDO_EN_F4c|CONTRATO_COMPLETO_PARA_F6|REGISTRADO_PARA_F5|
                  EXTERNO_CON_PROPIETARIO|HISTORICO_NO_APLICABLE) \|' | sort | uniq -c
   → 8 CONTRATO_COMPLETO_PARA_F6   ·   14 CORREGIDO_EN_F4c        (8 + 14 = 22)
comm -23 <(ids del doc 29) <(ids de la matriz)   → VACÍO
comm -13 <(ids del doc 29) <(ids de la matriz)   → VACÍO   (la dirección que la matriz no publica)
```

```text
¿UN ESTADO PRIMARIO CADA UNO?   SÍ. 22 identificadores, 22 filas, 8+14=22 estados
¿ALGUNO OMITIDO?                NO. La cobertura contra el documento 29 sale vacía en las
                                DOS direcciones
¿ALGUNO FUSIONADO?              NO en esta tanda. La única fusión —`T1-10`≡`T2-05` → `C-05`—
                                la hizo el adjudicador `GG` en el documento 29 §3 ANTES de
                                la matriz, y consta
¿ALGUNO DUPLICADO?              NO. `sort -u` da 22 sobre 22 filas
¿ALGUNO SUPERADO?               NINGUNO, y la cabecera lo prohíbe (chk:4049-4050)
¿ALGUNO MAL CLASIFICADO?        **SÍ. UNO: `C-20`.** Es `H-01`. Los otros veintiuno están
                                bien, y lo verifiqué fila a fila contra el documento 29
```

**Y anoto dos cosas a favor de la matriz, porque son ciertas:** `C-18` pasa de MENOR
«fragilidad no explotada» a **bloquear `F6` y PesquerApp** —es un ENDURECIMIENTO, no una
rebaja—; y `C-13`, que el documento 29 clasificó «`C` en el ataque, `A` en la propiedad», **no
arrastra el `C`**: la matriz le da estado primario por su PROPIEDAD, que es lo correcto bajo
`DD-20`.

### §5.6 · `C-L.5`, `C-L.7` y `M-04` bajo `O20`

| | estado vigente | ¿correcto? | por qué |
|---|---|---|---|
| **`C-L.5`** | **ABIERTA** | **SÍ** | La REABRE el adjudicador `GG` del octavo gate por `ASIGNADO − LEÍDO = 338 líneas y UNA FUENTE` (chk:2289-2291 y 2323-2334). **Cuatro sedes vigentes, un solo estado**: chk:2289, chk:2323, manifiesto:31, `00-INDICE`:104 — lo verifiqué. `O20` **no la toca y no debe tocarla**: es COBERTURA, no implementación. **Y mi propia resta de §1.3 no la cierra: cerrarla es un ACTO de adjudicador sobre este gate, y yo no la certifico** porque este gate devuelve insuficiencia por otras razones |
| **`C-L.7`** | **NO CERRADA** | **SÍ, y es la clasificación difícil** | chk:2470-2483 lo razona expresamente contra `O20`: «`C-L.7` es una condición sobre la **DISCIPLINA DEL REGISTRO**, no sobre la implementación del verificador, de modo que **sigue siendo `F4c` y sigue bloqueando**». **Es correcto**, y es lo contrario de lo que se le hizo a `C-20`: aquí la tanda **resistió** la tentación de mover una condición documental a `F6`. Y `H-09` y `H-10` **la confirman viva**: dos sedes más del bloque reanudable copian lo que declaran no copiar |
| **`M-04`** | **NO SUPERADA · cambia de FASE, no de ESTADO** | **SÍ** | chk:3991-4019. `O20` le da fase y propietario —lo que le faltaba— y **no la cierra**: «un gate de `F4c` puede declarar que su ARQUITECTURA está completa; **no puede declarar superada una implementación que nadie ha escrito**». Su mitad de implementación **bloquea `F6` y PesquerApp**, y sólo `V6-18` en verde la cerraría. **Ningún verde de la batería interna la cierra, y `O20` §5 lo escribe** |

**Los tres están clasificados correctamente, y ninguno se declara cerrado ni superado sin
serlo.** Es lo mejor de este expediente, y consta.

### §5.7 · COBERTURA

```text
OBLIGATORIO − ASIGNADO     sobre la CANDIDATA  ∅ en las DOS direcciones (83 = 83)
                           sobre el ÁRBOL DEL GATE  1, y es EXACTAMENTE el propio manifiesto,
                           declarado ANTES por su §6 como exención de PUNTO FIJO de `DD-19`
ASIGNADO − LEÍDO           ∅ · nueve fuentes asignadas, nueve declaradas leídas en su alcance,
                           con la unión del documento 11 sin hueco (`L1-L5200` ∪ `L5201-L11791`)
LAS DOS ARITMÉTICAS        DERIVAN de la propia tabla: 9+74=83 · 28847+59051=87898, que son
                           las cifras del árbol de la candidata que el sobre ancla
```

**LA COBERTURA CIERRA. No es razón de insuficiencia en este gate**, y lo digo expresamente
porque lo fue en los dos anteriores.

---

## §6 · REFUTACIONES CONTRA MIS PROPIAS CONCLUSIONES

### `R-1` · **LA OBLIGATORIA** — «`U1-01`/`H-01` no es de `F4c` sino de `F6`, porque el emisor es IMPLEMENTACIÓN»

**CAE, y contra la sede, no contra mi intuición. Cae por CUATRO vías independientes, y basta
cualquiera de ellas.**

**(i) `O20` §6 no dice «implementación»: dice «implementación DEL VERIFICADOR».** Sede
canónica L408-409, literal:

```text
· los defectos ARQUITECTÓNICOS o DOCUMENTALES siguen bloqueando `F4c`
· los defectos de IMPLEMENTACIÓN DEL VERIFICADOR pasan a CONTRATOS OBLIGATORIOS de `F6`
```

El verificador es el objeto que `O20` §3 contrata a `F6`: el VERIFICADOR DE ADMISIÓN y la RAÍZ
EXTERNA. **`emitir-sobre-de-ancla.py` no es ninguno de los dos.** Leer «implementación» a
secas convierte la cláusula en «todo lo que sea código es de `F6`», y entonces `C-11` y `C-12`
—que la misma matriz clasifica `CORREGIDO_EN_F4c` sobre el derivador, que también es código—
estarían mal clasificados. **La matriz no aplica esa lectura a nadie más que a `C-20`.**

**(ii) La sede normativa del propio artefacto le da fase `F4c`.** §11.6 L8595-8603:

```text
EL EMISOR DEL SOBRE, MATERIALIZADO   PROPIETARIO `PLT` · FASE **ya, para el PRÓXIMO gate de
                                     `F4c`**, porque sin emisor no hay sobre y sin sobre el
                                     gate no cumple `O18`
```

Y la misma sede, en los dos renglones siguientes, sí pone en `F6` «EL SOBRE COMO PARTE DEL
CONTRATO DE GATE EN EL KERNEL» y «LA SUSTITUCIÓN DE (b) POR (c)». **La sede sabe distinguir
las tres cosas. La matriz eligió la casilla equivocada.**

**(iii) El objeto de `C-20` no es el emisor: es el CONTENIDO del sobre.** El remedio que el
octavo gate escribió (doc29:4084) tiene dos ramas, y **la segunda no toca una línea de
código**: «*o que §11.6 y la sede dejen de enumerarlo como elemento que viaja*». **Una rama
puramente documental no puede ser un defecto de implementación.**

**(iv) Diferirlo a `F6` reinstaura exactamente la circularidad que `O18` cerró.** `O18` adopta
la opción (b) —el ancla documental— **«PARA CERRAR `F4c`»** (sede L165-166), y su motivo
declarado (L197-213) es que exigir la infraestructura de (c) antes de cerrar `F4c` produce un
bloqueo circular que el Owner **no acepta**. **Diferir a `F6` el cumplimiento de (b) es hacer
que `F4c` dependa de `F6` para cumplir la condición que se adoptó precisamente para no
depender de `F6`.** `O20` lo llama, en su nota de trazabilidad, «la misma clase de bloqueo
circular que `O18` cerró, un piso más abajo».

**Y aunque se admitiera el diferimiento —que no se admite—, el defecto persiste intacto:** su
`prueba_de_cierre` nombra `V6-16` y `V6-17`, y `F6` puede certificar los dos enteros sin que
`C-20` quede cerrado. **`O20` §7 exige del gate que autorice `F5` que confirme «que TODOS los
contratos de `F6` están completos». Éste no lo está.**

### `R-2` · **NO CAE** — «dieciséis hallazgos y CERO de clase `B`: si nada vuelve al Owner y nada exige arquitectura nueva, la arquitectura ES suficiente»

**Es la refutación más fuerte que me cabía, y concedo su premisa entera.** Ninguno de los
dieciséis es `B`, ninguno reinterpreta `O17`-`O20`, ninguno exige arquitectura nueva, y todos
se cierran con material que el corpus ya tiene escrito. **Pero «cero clase `B`» y «suficiente»
no son la misma proposición, y el manifiesto §7 lo escribe: de sus SIETE disparadores de
insuficiencia, sólo uno —«dos soluciones arquitectónicas incompatibles sin decidir»— exigiría
clase `B`.** Los otros seis se disparan con hallazgos de clase `A`, y **cuatro de ellos se
disparan hoy**: falta CRITERIO DE CIERRE (`H-01`, `H-05`), hallazgo SUAVIZADO al cambiarle la
fase (`H-01`), la matriz adversarial no especifica una clase reproducida (`H-06`), y una
obligación depende de INTERPRETACIÓN HUMANA NO NORMADA (`H-06`, `H-07`). **La refutación no cae
por lo que afirma, sino porque su conclusión no se sigue de sus premisas.**

### `R-3` · **CAE A MEDIAS, Y ME OBLIGA A REBAJAR `H-02`** — «`H-02` es de laboratorio: §18 es un grafo de dependencias técnicas y el bloqueo está en seis sedes normativas»

**Cae en su mitad, y la recojo: NO afirmo que PesquerApp esté desbloqueada.** Verifiqué las
seis sedes, una a una, en §5.4, y las seis dicen lo mismo con las mismas tres exclusiones.
**Lo que no cae es que §18 no calla: ENUNCIA una condición de entrada para su paso 8 —«la BASE
COMPLETA ACORDADA de los pasos 0 a 7»— y esa base no contiene el verificador.** Una sede que
escribe la condición equivocada es peor que una que no escribe ninguna. **Mantengo `H-02` como
GRAVE por eso y no por «PesquerApp podría iniciarse», y así queda redactado en §3.2. Si §18
callara, lo bajaría a MENOR.**

### `R-4` · **CAE** — «`H-03` y `H-04` son erratas de trazabilidad, y este gate juzga ARQUITECTURA, no tablas»

**Cae contra el texto de la sede que el propio gate tiene que aplicar.** `O20` §6, primera
viñeta, es taxativo: «los defectos arquitectónicos **o DOCUMENTALES** siguen bloqueando
`F4c`». No hay lectura en la que una fila que falta en la tabla de trazabilidad de las
resoluciones del Owner no sea documental. **Y las dos sedes escriben su propia sanción**:
§15.4 L9236 «una resolución sin fila aquí es el defecto»; §15.8 L9327 «no abrirlo es lo que
rompió la derivación dos veces». **Un defecto que la sede que lo comete declara defecto no
necesita que yo lo califique.** Lo que sí concedo, y lo digo: **por sí solos no decidirían
este gate.** Los gradúo GRAVE por REINCIDENCIA —`P-26` y `P-03`, dos remedios que gates
anteriores dieron por cerrados sobre estas mismas dos sedes—, y no por su contenido.

### `R-5` · **CAE, Y CONTRA MÍ** — «`H-06` exagera: los ocho árboles anteriores están cubiertos por las CLASES de `V6-01`…`V6-14`, y `V6-15` sólo contrata los tres reproducibles hoy»

**Lo trabajé, y es la refutación más caritativa posible. Cae para la mayoría y no para todos.**
Es cierto que las clases de los árboles 9, 10 y 11 —`HEAD` frente a revisión base, codificación
y mutación, lectura de listas— tienen punto propio, y que `V6-11` cubre la auto-exclusión.
**Pero `V6-15` no contrata CLASES: contrata «los CONTROLES … como FIXTURES OBLIGATORIOS», con
entrada nombrada y criterio de cierre por gate.** Y su escenario negativo pide «los once
árboles, **uno a uno**». **Una fila cuyo escenario negativo exige once y cuyo criterio de
cierre entrega tres es insatisfacible por su propia letra**, y quien la construya tendrá que
elegir cuál gobierna. **Bajo esta refutación `H-06` deja de ser «faltan ocho fixtures» y pasa
a ser «la fila se contradice» — que es la formulación de `U2` y no la de `U1`.** Lo reescribo
así, y **mantengo GRAVE**: elegir entre dos columnas de un contrato es decidir arquitectura,
y `O20` §1 dice que decidir es de `F4c`.

### `R-6` · **CAE** — «el gate es INVÁLIDO: el sobre de este gate incumple §11.6, luego no ancla nada»

**Cae, y lo digo expresamente para que nadie lo deduzca al revés.** `O19` (cláusula 8 de «cómo
nace una resolución») y §11.6 hacen FALLAR CERRADO al gate **si la sede canónica no coincide
con la huella recibida externamente**. **Coincide**: la recalculé sobre los dos commits, entera
y resolución a resolución, y las cinco huellas reproducen (§0.2). **El disparador de invalidez
es la DISCREPANCIA, no la incompletitud de la lista de lo que viaja.** `H-01` es un defecto de
SUFICIENCIA, no de VALIDEZ. **El gate es VÁLIDO.**

### `R-7` · **CAE** — «`U1` y `U2` coinciden en cinco pares: eso es convergencia y una convergencia se resuelve por mayoría»

**Cae por el encargo y por el método.** No resuelvo por mayoría, y **no he aceptado ni un solo
hallazgo por coincidencia**: reproduje los dieciséis contra fichero y línea con mis propios
comandos (§2), **hice caer uno entero (`U2-10`) y una rebaja (`U1-08` en su `RF-9`)**, corregí
cuatro clasificaciones de clase de `U1`, y **encontré una pieza que ninguno de los dos trajo
—§11.6 L8595-8603, la fase `F4c` del emisor— que es la que cierra `R-1`**. La coincidencia de
los dos no sostiene nada de lo que escribo; lo sostiene la reproducción.

### `R-8` · **CAE A MEDIAS** — «`H-01` es de laboratorio: el FIN de `O19` se cumple, porque el revisor puede comprobar la receta sin ejecutar el emisor, y eso es lo que la cláusula persigue»

**Cierto en su mitad, y lo recojo contra mí.** `O19` L317 exige que el revisor «debe comprobar
la receta **sin ejecutar el emisor**», y **ese fin se cumple: yo mismo recalculé las cinco
huellas de la sede sin ejecutarlo** (§0.2). Y el propio revisor del octavo gate lo graduó
MENOR por esa razón. **Lo que no cae es lo que registro:** el hallazgo **existe, reproduce
hoy** —el sobre trae 2 de 62 líneas sustantivas de `O19`, y las dos son `---` y una palabra
suelta—, **y su criterio de cierre está en `F6` y no lo mide**. **Si la conclusión correcta es
que `C-20` ya no importa, entonces lo que procede es retirarlo o declararlo satisfecho EN
`F4c` con su razón escrita — no darle una prueba de `F6` que no lo prueba.** Y adopto la
redacción rebajada de `U1`: **no es que el sobre calle la ratificación; es que entrega su
DIGEST y su RESUMEN donde la resolución exige su TEXTO.** La severidad la mantengo por la
CLASIFICACIÓN, no por el contenido.

### `R-9` · **CAE** — «`H-07` no vale: `PN-19` ya declara la decisión con fase `F5` y propietario el Owner, luego la asignación SÍ es inequívoca en el corpus»

**Cae como objeción a la existencia de la decisión, y no como objeción al contrato.** Es
cierto —y lo escribo en §5.2— que **nada está oculto**: `PN-19` la declara entera. **Pero
`O20` §1 no exige que la asignación sea deducible del corpus: exige que sea INEQUÍVOCA.** Y
§20 —la sede que se rotula a sí misma «escrito completo para que se pueda construir **sin
volver a decidir nada**» (L11729-11730)— declara «Fase de TODOS: `F6`» y **no cita `PN-19`,
`F5`, §11.6, §11.7 ni §11.8 en ninguna de sus 71 líneas** (`grep` en §2.7: sólo `D109`, `O18`,
`O20`). **Un contrato que dice de sí mismo que basta, y no basta, es un contrato incompleto.**
Mantengo `H-07` como GRAVE.

### `R-10` · **CAE** — «`O20` cambió la frontera para que este gate pudiera cerrar; devolver INSUFICIENTE por novena vez es inercia y desobedece al Owner»

**Cae, y es la refutación que más me obliga a escribir despacio.** `O20` es explícita sobre lo
que **no** hace (sede L436-439): «**no declara suficiente a `F4c`, no cierra ningún hallazgo,
no autoriza `F5`, `F6` ni PesquerApp**». Y su §7 escribe los cuatro requisitos del gate que
autorice `F5`, entre ellos «que **TODOS** los contratos de `F6` están completos» y «que las
obligaciones pendientes de `F6` NO ocultan una decisión arquitectónica». **Declarar suficiente
con dos contratos incompletos y un hallazgo documental aparcado bajo pruebas que no lo miden
sería desobedecer a `O20`, no obedecerla.** Y lo que la propia resolución exige de mí es lo
contrario de la inercia: **ninguna de mis razones es «el verificador no está implementado»**.
Las cuatro son las que su §7 y el §7 del manifiesto nombran.

### `R-11` · **NO CAE, Y ES LA ÚNICA QUE ME QUITA UN HALLAZGO** — «`H-11` (`U1-07`) es un hallazgo contra el INSTRUMENTO, y `O20` saca el instrumento del objeto del gate»

**No cae del todo, y por eso `H-11` va MENOR y no lo uso para el veredicto.** `O20` §2 saca del
objeto **que `F4c` demuestre que la implementación provisional satisface los contratos**; no
saca la PROCEDENCIA de una atribución al Owner, que es materia de `O19` y sigue entera. **Pero
concedo tres cosas:** el contenido atribuido es CIERTO, el propio fichero lo atribuye bien a
`O19` mil cien líneas más abajo, y ningún veredicto depende de ese rótulo. **Lo dejo MENOR y
declaro que no pesa.**

### §6.1 · Qué cambiaron estas once en mi adjudicación

```text
R-1    CIERRA `H-01` con una cuarta vía que ninguno de los dos revisores trajo (§11.6:8595)
R-2    concedo su premisa entera y muestro por qué su conclusión no se sigue
R-3    REBAJO la redacción de `H-02`: no digo «PesquerApp podría iniciarse», digo «la sede
       del orden de construcción enuncia una condición que no incluye el verificador»
R-4    gradúo `H-03` y `H-04` GRAVE **por REINCIDENCIA** y declaro que solos no decidirían
R-5    REESCRIBO `H-06`: no es «faltan ocho fixtures», es «la fila se contradice»
R-6    declaro expresamente que el gate es VÁLIDO, y por qué
R-7    declaro que no resuelvo por mayoría, y qué hice caer
R-8    adopto la redacción rebajada de `U1` para `H-01` y mantengo la severidad por la
       CLASIFICACIÓN, no por el contenido
R-9    retiro «oculta» de `H-07`, como `U2` ya había hecho contra sí mismo
R-10   escribo por qué la insuficiencia OBEDECE a `O20` en vez de desobedecerla
R-11   `H-11` baja a MENOR y NO pesa en el veredicto
```

---

## §7 · QUÉ FALLA HOY, CONTRA LOS SIETE DISPARADORES DEL §7 DEL MANIFIESTO

| disparador (manifiesto L220-226) | ¿se dispara? | con qué |
|---|---|---|
| falta una **REGLA** necesaria para construirlo | **SÍ** | `H-07` · `V6-16` exige un ejecutor con identidad separada y evidencia fuera del árbol, y `PN-19` declara que **«ninguna sede aprobada las contempla»** — con fase `F5`, que §20 no cita |
| existen **DOS soluciones arquitectónicas incompatibles sin decidir** | **NO** | verificado: `PN-13`, `PN-16`, `PN-17`, `PN-18` y `PN-19` declaran cada alternativa con propietario, fase, materia mínima y prueba que falla hoy. **Ninguno de los dieciséis es clase `B`** |
| falta **PROPIETARIO, FASE o CRITERIO DE CIERRE** en algún contrato | **SÍ, y por dos vías** | `H-01` · `C-20` tiene por criterio de cierre `V6-16`/`V6-17`, **que no lo contienen** · `H-05` · la mitad `F6` de `C-11` tiene por criterio `V6-04`, **cuyas cuatro columnas contratan otra cosa** |
| algún hallazgo se ha **ESCONDIDO o SUAVIZADO** | **SÍ** | `H-01` · `C-20`, defecto DOCUMENTAL del ancla de `O18(b)`, pasa a fase `F6` **contra §11.6 L8595-8603, que le da fase «ya, para el PRÓXIMO gate de `F4c`»** |
| la **MATRIZ ADVERSARIAL no especifica una clase reproducida** | **SÍ** | `H-06` · el OCTAVO árbol (`DD-01`, quinto gate, doc 26) está REPRODUCIDO y **no tiene fixture contratado**: la entrada de `V6-15` cubre 3 de los 8 gates y 3 de los 11 árboles |
| **PesquerApp PODRÍA INICIARSE** antes de certificar `F6` | **NO** | seis sedes normativas la bloquean, con las mismas tres exclusiones (§5.4). **`H-02` es la omisión de la sede del ORDEN DE CONSTRUCCIÓN, no una autorización** |
| una obligación depende de **INTERPRETACIÓN HUMANA NO NORMADA** | **SÍ** | `H-06` · quien construya `V6-15` tiene que ELEGIR si gobierna su escenario negativo (once) o su criterio de cierre (tres) · `H-07` · quien construya `V6-16` tiene que decidir de dónde saca la norma que `PN-19` dice que no existe |
| *(regla de cierre del §8: cualquier fuente asignada y no leída)* | **NO** | `ASIGNADO − LEÍDO = ∅` (§1.3) |
| *(regla de cierre del §8: dos sobres distintos)* | **NO** | los dos sobres embebidos son BYTE A BYTE el mío (§0.3) |
| *(regla de cierre del §8: sede que no coincida con la huella)* | **NO** | las cinco huellas reproducen en los dos commits (§0.2) |

**CINCO de los siete disparadores se disparan.** Y **ninguno de los cinco es «el verificador
de `F6` no está implementado»**, que es la única razón que este gate tiene prohibido usar.

**LO QUE SÍ FUNCIONA, y lo escribo porque un dictamen que sólo publica lo que rompe no permite
pesar lo que no rompió:**

```text
EL SOBRE            las seis obligaciones reproducen. Los dos digest de universo, los dos
                    `tree` SHA, el manifiesto, el emisor, el derivador, la sede entera y sus
                    CUATRO resoluciones. **Los dos sobres embebidos son byte a byte el mío**
EL MANIFIESTO       83 filas contra el árbol que declaran: **CERO discrepancias**, ni de
                    línea ni de SHA-256. **La fila del propio derivador NO reincide**, y era
                    la que dos gates seguidos falsearon. Las dos aritméticas DERIVAN
LA COBERTURA        las dos restas cierran. `OBLIGATORIO − ASIGNADO = ∅` sobre la candidata,
                    y sobre el árbol del gate la única fuente sin fila es el propio
                    manifiesto, declarada ANTES por su §6
LA MATRIZ           22 identificadores, 22 filas, un estado primario cada uno, sumas
                    derivadas, cobertura vacía en las DOS direcciones, **ninguno superado**.
                    **Veintiuno bien clasificados de veintidós**
DIECISÉIS DE 18     contratos completos, con criterio de cierre exacto y construibles sin
                    volver a decidir
LA FRONTERA         `O20` está proyectada sin ampliar ni debilitar su autoridad: `D109` y la
                    proyección reproducen sus nueve puntos y sus nueve responsabilidades, y
                    la única viñeta añadida **ENDURECE** y va rotulada como lectura no literal
NADA SE PRESENTA    ninguna sede presenta deuda de `F6` como implementación existente. §20.2
COMO HECHO          lo escribe tres veces; el manifiesto §9 publica «38/38 en verde» y a
                    continuación «Y ESTAS CIFRAS NO PRUEBAN QUE LOS CONTRATOS DE `F6` ESTÉN
                    IMPLEMENTADOS»
`C-L.5` `C-L.7`     los tres clasificados correctamente, ninguno cerrado ni superado sin
`M-04`              serlo. `C-L.7` es el caso en que la tanda **resistió** mover una
                    condición documental a `F6` — que es lo que a `C-20` no le hizo
LOS DOS REVISORES   declararon sus restas contra su propio interés, con rangos enumerados, y
                    declararon sus lecturas FUERA de lote sin reclamarlas. Es lo que el
                    octavo gate midió que faltaba
```

**La distancia entre este gate y la suficiencia es la más corta de los nueve, y lo digo sin
que eso cambie nada: la suficiencia no se pondera, se cumple o no.**

---

## §8 · VEREDICTO

# INSUFICIENTE PARA F5

# EL GATE ES VÁLIDO

**VÁLIDO** porque las seis obligaciones del sobre reproducen byte a byte, los dos digest de
universo reproducen sobre sus dos árboles con sus propios derivadores, el manifiesto reproduce
en el commit del gate, sus 83 filas reproducen contra el árbol que declaran —incluida la del
propio derivador—, la sede canónica y sus cuatro resoluciones reproducen en los dos commits, y
**los bloques de sobre que los dos revisores embebieron son BYTE A BYTE el fichero que yo
recibí**. Ninguno de los tres disparadores de invalidez del §8 del manifiesto se dispara.

**INSUFICIENTE** por CINCO de los siete disparadores del §7 del manifiesto, sostenidos por
SIETE hallazgos —uno BLOQUEANTE y seis GRAVES— de los cuales **ninguno es que el verificador
de `F6` no esté implementado**:

```text
1  `H-01`  `C-20` —el sobre no lleva el TEXTO de la ratificación, y REPRODUCE en el sobre de
   BLOQ.   ESTE gate— se mueve a fase `F6` con `V6-16`/`V6-17` de criterio de cierre, que no
           lo contienen, **contra §11.6 L8595-8603, que le da fase «ya, para el PRÓXIMO gate
           de `F4c`»**. Es hallazgo SUAVIZADO al cambiarle la fase Y contrato sin criterio de
           cierre. `O20` §6 no autoriza diferir un defecto DOCUMENTAL
2  `H-06`  `V6-15` se contradice: su escenario negativo exige «los ONCE árboles» y su entrada
   GRAVE   y su criterio de cierre dan TRES gates. El OCTAVO árbol —`DD-01`, quinto gate,
           documento 26— está REPRODUCIDO y sin fixture contratado
3  `H-07`  §20 declara «Fase de TODOS: `F6`» sin citar `PN-19`, cuya fase es `F5` y cuya
   GRAVE   materia es la norma que `V6-16` presupone y que «ninguna sede aprobada contempla»
4  `H-05`  la mitad `F6` de `C-11` se enruta a `V6-04`, que contrata un censo de lecturas Git
   GRAVE
5  `H-02`  §18 —el orden de construcción de `F6`— no contiene el verificador ni la raíz
   GRAVE   externa, y enuncia como base de su paso 8, que es PesquerApp, unos pasos 0-7 que
           no los incluyen
6  `H-03`  `O20` sin fila en §15.4, contra su propia regla. REINCIDENCIA LITERAL de `P-26`
   GRAVE
7  `H-04`  `D109` sin bloque en §15.8, contra su propia regla. TERCERA vez que se rompe
   GRAVE
```

**LOS DOS QUE POR SÍ SOLOS BASTARÍAN son `H-01` y `H-06`.** Los otros cinco acompañan, y
`H-03` y `H-04`, solos, no decidirían este gate — lo declaro en `R-4`.

```text
RECUENTO      BLOQUEANTE 1 · GRAVE 6 · MEDIO 3 · MENOR 3 · LEVE 3   =  16
CLASE         A 16 · B 0 · C 0
REINCIDENCIA  8 de 16, y DOS son literales sobre la misma sede que un gate anterior cerró
AL OWNER      **NADA.** Ver §9.3
```

---

## §9 · REMEDIOS DETERMINADOS — **QUÉ**, NO CÓMO. NINGUNO APLICADO

> **No he aplicado ninguno, no he propuesto redacción para ninguno y no he tocado el
> repositorio.** Cada remedio dice **qué tiene que ser cierto**, no cómo escribirlo, y dice
> **quién** y en **qué fase**.

| # | REMEDIO DETERMINADO · qué tiene que ser cierto | propietario | fase | ¿al Owner? |
|---|---|---|---|---|
| **`H-01`** | **(a)** Que `C-20` deje de tener por criterio de cierre dos contratos que no lo contienen, y **(b)** que su FASE sea la que su sede normativa le da —§11.6 L8595-8603, «`PLT` · ya, para el PRÓXIMO gate de `F4c`»—, y **(c)** que el SOBRE lleve el TEXTO de la ratificación que `O19` L315 ordena y §11.6 L8454 enumera como el primero de «la lista entera». **La segunda rama que el octavo gate ofrecía —que §11.6 y la sede DEJEN DE ENUMERARLO— NO está disponible sin el Owner: ver §9.3** | `PLT` construye · `SIS` la clasificación | **`F4c`** | **NO**, si se toma la rama (c). **SÍ**, si alguien quiere la otra |
| **`H-06`** | Que `V6-15` deje de exigir en una columna once árboles y entregar tres en otra: **o su ENTRADA alcanza los once —lo que obliga a ENUMERARLOS con identificador, cosa que hoy ninguna sede hace—, o su escenario negativo dice los que su entrada da**. Y que **el OCTAVO árbol (`DD-01`, quinto gate, doc 26), REPRODUCIDO, tenga fixture contratado** en alguna de las dieciocho filas | `SIS` especifica | **`F4c`** | **NO** |
| **`H-07`** | Que §20 **declare la dependencia**: que `V6-16` —y con él la raíz externa— no puede construirse sin la norma que `PN-19` sitúa en `F5` con propietario el Owner, y que §20 **enlace §11.8**, donde vive su contrato largo de dieciséis exigencias. La FASE de cada punto tiene que ser INEQUÍVOCA dentro del contrato, que es lo que `O20` §1 exige | `SIS` | **`F4c`** | **NO** · `PN-19` ya declara la decisión con propietario y fase; lo que falta es que el contrato la cite |
| **`H-05`** | Que la mitad `F6` de `C-11` —unificar la fórmula de líneas, viva en `emitir…py:217` y `:372`— **tenga un contrato cuyo objeto la contenga**, o que se cierre en `F4c`. Hoy su criterio es `V6-04`, que contrata un censo de lecturas de Git | `SIS` la asignación · `PLT` la unificación | **`F4c`** la asignación | **NO** |
| **`H-02`** | Que §18 —«Orden de construcción para `F6`»— **contenga el nodo del verificador de admisión y de la raíz externa**, y que su paso 8 —PesquerApp— lo lleve entre sus dependencias. Es la primera y la segunda responsabilidad que `O20` §3 da a `F6` | `SIS` | **`F4c`** | **NO** |
| **`H-03`** | Que `O20` **tenga fila en §15.4**, por la regla que la propia sede escribe: una fila por resolución del Owner, derivada de las cabeceras `### \`O` de la sección 2 del registro | `SIS` | **`F4c`** | **NO** |
| **`H-04`** | Que la tanda de `O20` **abra su bloque `### \`D109\`` en §15.8**, como `D107` y `D108` abrieron el suyo, para que el recuento de correcciones vuelva a derivar de los bloques | `SIS` | **`F4c`** | **NO** |
| **`H-08`** | Que §11.6 campo 17, campo 18 y la obligación `6bis` **dejen de fijar tres resoluciones** y digan lo que el instrumento ya hace: **todas las que la sede contenga**. Hoy un sobre que anclase sólo `O17`-`O19` cumpliría la norma y no anclaría `O20` | `SIS` | **`F4c`** | **NO** |
| **`H-09`** | Que el fragmento HUÉRFANO de `based_on` (chk:1185-1191) **tenga sujeto o se retire**, que **deje de copiar un estado** («`C-L.5` pasa a ABIERTA») en la misma frase que declara no copiarlo, y que `based_on` **se reancle para `O19`, `O20` y `D109`**, como manda la regla 4 del propio bloque | `SIS` | **`F4c`** | **NO** |
| **`H-10`** | Que `owner_captado` **deje de enumerar** las resoluciones de la sede y remita o derive, como su propio fichero ordena tres campos más arriba. Hoy dice «las tres» donde hay cuatro | `SIS` | **`F4c`** | **NO** |
| **`H-11`** | Que los tres rótulos de `comprobar-…py` (`:2243`, `:2283`, `:3009`) **atribuyan la regla APPEND-ONLY a `O19`**, que es su fuente y que el propio fichero cita bien en `:3395`, y no a `O20`, que no la contiene. Importa porque `:2283` la IMPRIME en el informe que un revisor lee | `PLT` | **`F4c`** | **NO** |
| **`H-12`** | Que §19 y §2.1 **censen la familia `V6-01`-`V6-18`** entre las familias de contrato de prueba no ejecutadas, como censan `X<nn>`, `X-<L>`, `X-S<n>` y `X-O<n>` | `SIS` | **`F4c`** | **NO** |
| **`H-13`** | Que el componente (v) del `ENCARGO` de `derivar-…py` **describa el encargo de ESTE gate** y no el del octavo: hoy dice «los 24 hallazgos del documento 21» y «el emisor … que este gate ESTRENA» | `PLT` | **`F4c`** | **NO** |
| **`H-14`** | Que las tres sedes que describen §20 **digan lo que su tabla da**: ocho atributos por fila y tres globales, no «once campos cada uno». Y que la FUENTE global de §20 **acote su universalidad**, porque `V6-12` deriva de `O19` y de las reglas de la sede, no de `O20` | `SIS` | **`F4c`** | **NO** |
| **`H-15`** | Que la línea 872 del registro **deje de llevar el marcador de cita `> ` incrustado a mitad de frase** cuatro veces | `SIS` | **`F4c`** | **NO** |
| **`H-16`** | Que «catorce» y «ocho» **se deriven o se remitan** en chk:38-42 y `00-INDICE`:104, como la cabecera de la matriz ordena. Son ciertos hoy y caducan con el primer movimiento de la matriz | `SIS` | **`F4c`** | **NO** |

### §9.1 · Qué NO es un remedio, y lo digo para que nadie lo escriba

**NINGUNO de los dieciséis se cierra implementando el verificador de `F6`.** Los dieciséis se
cierran con material que el corpus ya tiene escrito: una fila en §15.4, un bloque en §15.8, un
nodo en §18, tres identificadores en §11.6, una columna coherente en `V6-15`, una remisión a
`PN-19` y a §11.8 en §20, una reclasificación de `C-20` con su fase, un contrato que contenga
la fórmula de líneas, y siete retiradas o remisiones. **Ninguno exige arquitectura nueva y
ninguno reinterpreta `O17`, `O18`, `O19` ni `O20`.**

### §9.2 · Lo que este gate NO ha hecho, y es deliberado

```text
NO HE CONSTRUIDO NINGÚN ÁRBOL ADVERSARIAL   `O20` lo saca del objeto de este gate y lo
                                            contrata para `F6` en `V6-18`. **Por tanto no
                                            afirmo nada sobre si existe hoy un duodécimo
                                            árbol**, y nadie debe leer mi silencio como una
                                            ausencia de puertas
NO HE EJECUTADO LA BATERÍA                  las cifras del manifiesto §9 —38/38, 13/13,
                                            `T147`— **no las he reproducido y no las uso**.
                                            `O20` §5 dice que un verde suyo no demuestra
                                            nada de `F6`, y esta adjudicación no se apoya en
                                            ninguno
NO HE CORREGIDO NADA                        cero ediciones, cero commits, cero referencias.
                                            `git status --porcelain` sigue vacío
NO PUEDO VERIFICAR                          que la sede canónica sea el texto que el Owner
                                            emitió. El sobre lo declara y `O18` lo declara de
                                            sí misma: **lo que mi anclaje prueba es que el
                                            texto no ha cambiado entre el commit auditado y
                                            lo que recibí FUERA del árbol, y NADA MÁS**.
                                            Sigue vigente hasta el verificador externo de `F6`
NO PUEDO VERIFICAR                          que el emisor y el derivador que CORRIERON sean
                                            los publicados. `Z-11` lo midió y el sobre lo
                                            declara. Lo que sí verifiqué son sus SHA-256 en
                                            los DOS commits
```

### §9.3 · ¿ALGO VUELVE AL OWNER?

# NO. NADA VUELVE AL OWNER.

**Por SEXTA vez consecutiva, y lo razono contra el único candidato real, que es `H-01`.**

El remedio que el octavo gate escribió para `C-20` (doc29:4084) tiene **dos ramas**, y las
distingo porque **no son equivalentes en autoridad**:

```text
RAMA (i)   que el SOBRE lleve el TEXTO de la ratificación
           **NO VUELVE AL OWNER.** Es cumplir una orden que el Owner ya dio, con el
           instrumento que `PLT` ya posee. Cumplir una resolución no la reinterpreta:
           la aplica. Y §11.6 L8595-8603 ya le da propietario y fase, dentro de `F4c`

RAMA (ii)  que §11.6 **y la sede** dejen de enumerarlo como elemento que viaja
           **ESTA SÍ VOLVERÍA AL OWNER, y por eso la declaro NO DISPONIBLE para `F4c`.** La
           lista de los seis elementos no es sólo de §11.6: está en `O19` L315-317, en la
           SEDE CANÓNICA, que es APPEND-ONLY por su propia primera regla y cuyo texto es del
           Owner. **Retirar un elemento de una orden del Owner es revisarla, y sólo el Owner
           revisa una resolución del Owner** (`O19` cláusula 10, y la regla APPEND-ONLY)
```

**El adjudicador del octavo gate resolvió que `C-20` no volvía al Owner (doc29 §10.1) razonando
que «alinear una sede derivada con su sede canónica no reinterpreta la resolución: la
aplica». Ese razonamiento es CORRECTO para la rama (i) y NO lo es para la rama (ii), y su
§10.1 las trata como intercambiables.** Lo hago constar. **Con la rama (i) —que es la que el
remedio determinado toma— nada vuelve al Owner, y por eso mi respuesta es NO.**

**Los otros quince tampoco.** Ninguno es clase `B`, ninguno exige una decisión nueva, ninguno
reinterpreta `O17`, `O18`, `O19` ni `O20`, y todos se cierran con material escrito. **Y
`PN-19`, que sí es una decisión del Owner, ya está formulada, acotada y con fase `F5`: no
vuelve hoy, y `H-07` no pide que vuelva — pide que el contrato la cite.**

---

## DISCIPLINA — declaración de cierre del adjudicador

```text
NO HE MODIFICADO EL REPOSITORIO      `git status --porcelain` vacío al abrir y al cerrar.
                                     Cero commits, cero ramas, cero referencias, cero
                                     escrituras bajo `/home/jose/ads-kernel`. Todo se leyó
                                     con `git show <commit>:<ruta>` y todo lo que necesitó
                                     árbol se hizo con `GIT_INDEX_FILE` en `mktemp -d`
NO HE CORREGIDO NINGÚN HALLAZGO      ni uno, y el encargo lo prohíbe
NO HE RESUELTO POR MAYORÍA           reproduje los dieciséis contra fichero y línea. **Hice
                                     caer `U2-10` entero y la rebaja de `U1-08`**, corregí
                                     CUATRO clasificaciones de clase de `U1`, y traje una
                                     pieza que ninguno de los dos tenía (§11.6 L8595-8603)
NO HE SUAVIZADO                      cinco de los siete disparadores del §7 se disparan, y
                                     así consta
TODA CIFRA CON SU COMANDO            y ninguna huella abreviada a mano: las que aparecen son
                                     salida de `sha256sum`
FUENTE NORMATIVA                     la SEDE CANÓNICA del Owner · §20, §11.6, §11.8, §15.4,
                                     §15.8, §18 del documento 11 · las reglas del bloque
                                     reanudable del checkpoint
PROYECCIÓN DERIVADA                  `D107`, `D108`, `D109`, la sección 2 del registro, §20
                                     (que se rotula a sí misma proyección), la MATRIZ DE LOS 22
REGISTRO HISTÓRICO                   los documentos 10 y 12-29, la entrada corta de `O18`,
                                     los campos `_anterior` y todo lo rotulado `[HISTÓRICO]`
                                     o `[ESTADO ANTERIOR]`, que **no cuento como defecto vivo**
EVIDENCIA                            los recálculos de §0.2, las 83 filas de §0.2 obl. 3, las
                                     dos restas de §1, y los comandos de §2 y §5
OBSERVACIÓN DE MÉTODO                valorada POR ENCIMA de un hallazgo y declarada en §1.4:
                                     los dos revisores declararon sus restas y sus lecturas
                                     fuera de lote contra su propio interés, que es lo que el
                                     octavo gate midió que faltaba
INDEPENDENCIA                        no he escrito nada de este corpus, no he aplicado
                                     ninguna corrección, no he sido revisor de ningún gate
                                     anterior y no vi nada de este gate hasta abrir el sobre
```
