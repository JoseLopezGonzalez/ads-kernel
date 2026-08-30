# CORRIGENDUM EXTERNO A DICTÁMENES INMUTABLES

> **Qué es.** Los dictámenes de gate y los manifiestos de reparto son **INMUTABLES**: una vez
> publicados no se editan, porque un juicio que se retoca deja de ser un juicio. Pero algunos
> contienen **errores de hecho verificables**, y dejarlos sin señalar hace que el corpus se
> apoye en ellos. Este documento los señala **sin tocarlos**.
>
> **Qué NO es.** No corrige ningún dictamen, no cambia ningún veredicto, no reabre ninguna
> adjudicación y no altera el estado de ninguna condición. Cada entrada dice qué afirma la
> sede, qué dice el árbol, y **qué se sigue de la diferencia** — que muchas veces es: nada,
> salvo que no se puede citar esa frase para sostener otra cosa.
>
> **Cómo se lee.** Toda cifra de este documento se DERIVA del árbol en el momento de
> escribirla, y se dice con qué comando. Ninguna se copia.

## 1 · Documento 20 · afirma tener manifiestos de lectura por fichero, y no los tiene

**Sede:** `20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md` **L127–L129**.
**Afirma** que los revisores publicaron manifiestos «fichero a fichero, ruta, SHA-256 …
`LEÍDO ÍNTEGRO`», y que están «transcritos íntegros en §4 y §5».

**Lo que dice el árbol**, derivado sobre el cuerpo de §4 y §5 de ese documento:

```text
COMANDO (desde docs/evolucion/)                                          RESULTADO
awk '/^## 4 · Dictamen literal del REVISOR M/,/^## 6 /' \
    20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md | grep -cE '[0-9a-f]{64}'      0
awk '/^## 4 · Dictamen literal del REVISOR M/,/^## 6 /' \
    20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md | grep -c 'LEÍDO ÍNTEGRO'      0
```

**Qué se sigue.** El documento 20 declara su cobertura **en AGREGADO** —y lo hace con
honestidad: su revisor `N` enumera qué leyó y qué no—, pero **no por ruta**. Por tanto:

```text
NO SE PUEDE  citar L368, L372 ni L638 del documento 20 para declarar AGOTADA la lectura de
             una ruta concreta. No la nombran
SÍ SE PUEDE  citarlo para lo que sí dice: que un revisor independiente leyó íntegro su lote
YA REMEDIADO el GATE del documento 22 lo detectó por boca de su relevo `Q3` y publicó el
             `ADDENDUM 1`, que devolvió las 21 fuentes afectadas a lectura íntegra. La
             cobertura de aquel gate se cerró con `ASIGNADO − LEÍDO = ∅`
```

**Y consta la agravante que el propio documento 20 escribe trece líneas más allá:** su
adjudicador `O` declara en **L651** la regla de cierre «NO CERTIFICABLE POR MÍ» y en **L656**
«`C-L.5` queda ABIERTA en forma». Apoyar un agotamiento en ese gate era doblemente frágil.

## 2 · Documento 20 · la aritmética con que se retira una razón de veredicto es falsa

**Sede:** `20-…-F4C.md` **L628**. El adjudicador `O` retira la quinta razón de veredicto del
revisor `N` diciendo que el total declarado por `M` «sólo cuadra incluyéndolo».

**Lo que dice la aritmética**, con las nueve partidas que el propio documento enumera en
L76–L85. **La suma no se escribe: se deriva**, y éste es el comando, desde `docs/evolucion/`:

```bash
sed -n '77,85p' 20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md \
  | cut -c1-37 | grep -oE '[0-9]+ *$' | tr -d ' ' | paste -sd+ | bc      # → 26392
grep -o 'LOTE DE M · [0-9  ]*líneas' 20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md
```

```text
       9058
       1152
       1898
        677
       1132
       1288
       1590
        862
       8735
                                     ────────
                            suma      26392
                            declarado 26 411
                            DIFERENCIA  19 líneas
```

**Qué se sigue.** La conclusión de `O` **puede seguir siendo correcta por otras razones**
—`M` declaró el documento 11 en su lote—, pero **el argumento aritmético con que la sostiene
no se sostiene**. No se puede citar esa frase como prueba de que una lectura ocurrió. El total
del revisor `N`, en cambio, **sí cuadra exacto** y se ha verificado.

## 3 · Documento 19 · define mal el BLOQUE C de `ADS-PENDIENTES`

**Sede:** `19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md` **L310** y **L898–L899**, que lo definen
como **§13–§15**.

**Lo que dice el árbol**, derivado de las cabeceras de `ADS-PENDIENTES`, con su comando:

```bash
awk '/^# BLOQUE C /{f=1} /^# BLOQUE D /{f=0} f && /^## [0-9]+\./' \
    docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md | tail -1
```

```text
última sección antes de `# BLOQUE D`   ## 17. Decisiones pendientes sobre esta unidad
luego el BLOQUE C es                   §13–§17
```

**Qué se sigue.** El documento 20 acierta y el 19 no. Un gate que hubiera tomado el rango del
documento 19 como universo habría dejado **dos secciones enteras sin leer**, y ninguna
comprobación lo habría dicho. El universo obligatorio de los gates posteriores **no se toma de
este rango**: se deriva con `derivar-universo-obligatorio.py`, que toma el fichero completo.

## 4 · Documento 13 · una «ERRATA CONFIRMADA» que hoy está superada

**Sede:** `13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md` **L46** y **L628**, que fijan
«ERRATA CONFIRMADA · DIEZ» sobre una cifra que el documento 12 hoy da como **ONCE**.

> **Localización corregida.** Esta entrada citaba **L42** y **L618**. Las líneas reales son
> **L46** y **L628**, derivadas con
> `grep -n 'ERRATA CONFIRMADA' 13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md` y con
> `sed -n '628p'`. Lo levantó `T2-06` del segundo gate de certificación (`T-21`). **La
> sustancia de la entrada no cambia**; lo que estaba mal era dónde mirar, en un documento
> cuya cabecera promete que ninguna cifra se copia.

**Qué se sigue.** La verificación del documento 13 fue correcta **cuando se hizo**, y quedó
superada por una corrección posterior sin que nada lo marcara. No se corrige el dictamen: se
marca aquí que **su cifra describe un estado anterior del corpus**, y que la vigente es la del
documento 12.

## 5 · `ADDENDUM 1` del gate de certificación · describe de más su propia evidencia

**Sede:** `verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` **L77–L79**,
que afirma que las doce fuentes que siguen AGOTADAS tienen en el documento 21 «su ruta, sus
líneas y **su SHA-256**».

**Lo que dice el árbol.** Tres de las doce publican en el documento 21 **sólo los primeros
hexadecimales**, no el digest completo. El largo se deriva, no se cuenta a ojo:

```bash
sed -n '1056,1058p' docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md \
  | grep -oE '`[0-9a-f]+`' | awk '{print length($0)-2}'          # → 16, 16, 16
```

```text
00-INDICE.md                                         doc 21 L1056   16 hex publicados de 64  prefijo correcto: sí
02-CIRCUITO.md                                       doc 21 L1057   16 hex publicados de 64  prefijo correcto: sí
04-INCERTIDUMBRE-Y-CONFIRMACION.md                   doc 21 L1058   16 hex publicados de 64  prefijo correcto: sí
```

**Qué se sigue, y es poco pero hay que decirlo.** La **regla 2** del agotamiento —bytes
idénticos— **se cumple igual**: los tres prefijos publicados son prefijo del SHA-256 completo
de la candidata, verificado arriba, y el adjudicador `R` recalculó los doce contra el árbol.
Lo que falla es **la descripción que el addendum hace de su propia evidencia**, no la
evidencia. Lo encontró el dictaminador `Q4`. El addendum **no se edita**: se corrige aquí.

## 6 · Manifiesto del SEGUNDO GATE DE CERTIFICACIÓN · su titular de líneas se contradice con sus propias dos subsumas

**Sede:** `verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md`
**L36** —«`UNIVERSO DERIVADO   64 fuentes · 47 728 líneas`»— y **L173** —«`LÍNEAS
OBLIGATORIAS     47 728`»—, dentro del bloque §6 que publica «las DOS restas de `1bis`».

**Lo que dice el árbol.** Las tres cifras se derivan, y **dos de ellas están en el propio
manifiesto**:

```text
COMANDO                                                       RESULTADO
python3 …/derivar-universo-obligatorio.py    (árbol c36d2ba)  64 fuentes · 48 138 líneas
suma de la columna «líneas» de las 12 filas de su §4                     21 530
suma de la columna «líneas» de las 52 filas de su §5                     26 608
                                                                       ────────
21 530 + 26 608                                                          48 138
titular publicado en su §2 (L36) y en su §6 (L173)                       47 728
                                                                       ────────
DIFERENCIA                                                                  410
git show c36d2ba:…/derivar-universo-obligatorio.py | wc -l                  410
```

**El manifiesto se contradice DENTRO de su propia §6**: sus dos subsumas —las que él mismo
publica, fila a fila— suman **48 138**, y su titular dice **47 728**, dos renglones más
arriba. Las 64 filas están bien y los dos subtotales están bien; **lo que no deriva de nada
es el titular**.

**De dónde salen las 410 líneas de diferencia.** Son exactamente el recuento de
`derivar-universo-obligatorio.py`, que es la fuente que el commit `6b5d3e6` añadió al
`ENCARGO` **y que el propio §2 del manifiesto presenta como novedad**: «*el propio
derivador, que pasa a juzgarse a sí mismo*». **El titular es una copia de una ejecución
anterior a esa ampliación, no una derivación**, en el documento cuya tesis es que «el
universo no se escribe: se deriva».

**Qué se sigue.**

```text
NO SE PUEDE  citar «47 728 líneas» de este manifiesto como el tamaño del universo
             obligatorio de ese gate. La cifra derivada es 48 138, y el propio manifiesto
             la contiene desagregada
SÍ SE PUEDE  citar sus 64 filas, sus dos subtotales y sus dos restas: ninguna cambia. El
             adjudicador `U` recalculó las 64 filas contra el árbol sin una discrepancia
NO CAMBIA    ningún veredicto, ninguna asignación y ninguna cobertura: la resta
             `OBLIGATORIO − ASIGNADO = ∅` se calcula sobre FUENTES, no sobre líneas
YA REMEDIADO en la fuente: el derivador publica el total en cada ejecución. Copiarlo a un
             titular es lo que lo hizo caducar, y por eso este corrigendum recomienda **no
             publicar el titular**, no corregirlo
```

**El manifiesto es INMUTABLE y no se edita**: se acota aquí. Lo levantó `T3` como hallazgo
propio (`T-10`) y el adjudicador `U` lo confirmó y lo agravó, porque la contradicción es
interna al mismo bloque.

## 7 · Manifiesto del SEGUNDO GATE DE CERTIFICACIÓN · declara un árbol contra el que su fila 8 no casa

> **Lo levanta `W2-05` del tercer gate de certificación (documento 24).** La entrada §6 de
> este mismo corrigendum ya acotó el TITULAR de líneas de ese manifiesto **y no acotó la
> fila**, ni dijo contra qué árbol casa la tabla. Eso es lo que se completa aquí.

**Sede:** `verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` **L79**
—«*Todo derivado del árbol `2451141c40e1bba7823528edd2df073af92a4037`, nada copiado*»— y la
**fila 8** de esa misma tabla, que declara `derivar-universo-obligatorio.py` con **410
líneas** y SHA-256 `6753a245…`.

**Lo que dice el árbol.** Las 64 filas se contrastan una a una contra los dos commits en
juego —el de la CANDIDATA, cuyo árbol el manifiesto declara, y el del propio MANIFIESTO—:

```text
COMANDO                                                                RESULTADO
git rev-parse e3163967^{tree}                                          2451141c40e1bba7…
git show e3163967:docs/evolucion/verificacion/derivar-universo-obligatorio.py | wc -l    402
git show e3163967:…/derivar-universo-obligatorio.py | sha256sum        fa245924cbe33e1c…
git show c36d2ba:…/derivar-universo-obligatorio.py  | wc -l            410
git show c36d2ba:…/derivar-universo-obligatorio.py  | sha256sum        6753a245103dcc5a…

filas del manifiesto que NO casan contra `e3163967` (árbol DECLARADO)      1  — la fila 8
filas del manifiesto que NO casan contra `c36d2ba`  (commit del MANIFIESTO) 0
```

**Qué se sigue.**

```text
NO SE PUEDE  leer «todo derivado del árbol 2451141c…» al pie de la letra: la tabla entera
             deriva del árbol del COMMIT DEL MANIFIESTO, `c36d2ba`, y contra el árbol que
             declara falla exactamente en una fila — la del propio derivador
SÍ SE PUEDE  usar las 64 filas: son correctas, y lo son contra `c36d2ba`. Hay que decir
             contra qué árbol se contrastan, que es lo que el manifiesto no dice
POR QUÉ PASA no es descuido: **el derivador es fila de su propio universo**, y el commit
             que publica el manifiesto lo toca. Mientras el gate escriba el derivador
             después de publicar la candidata, los dos árboles no pueden coincidir en esa
             fila, y el manifiesto tiene que publicar los DOS o el gate no tocar el
             derivador. El emisor del sobre ya publica los dos
NO CAMBIA    ningún veredicto ni ninguna cobertura: `U` recalculó las 64 filas contra el
             árbol del gate sin una discrepancia, y ahí está el 0 de arriba
```

## 8 · Manifiesto del TERCER GATE DE CERTIFICACIÓN · lo mismo, un gate después, en la misma fila

> **Lo levantan `V-23` y `X-06` del documento 24, y `X` lo eleva expresamente por
> REINCIDENCIA: mismo fichero, misma fila 8, un gate después de que `U-02`/`T-10` lo
> adjudicara.** La entrada §6 de este corrigendum acotó entonces el titular y no la fila; si
> lo hubiera acotado, esta entrada no haría falta.

**Sede:** `verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-20260830.md` **L70**
—«*Todo derivado del árbol `b498f3b8ae8a70510b68feefe592f502cf8e1a86`, nada copiado*»— y la
**fila 8**, que declara `derivar-universo-obligatorio.py` con **496 líneas** y SHA-256
`6f8c98a2…`.

**Lo que dice el árbol:**

```text
COMANDO                                                                RESULTADO
git rev-parse 21f1ccb^{tree}                                           b498f3b8ae8a7051…
git show 21f1ccb:…/derivar-universo-obligatorio.py | wc -l             492
git show 21f1ccb:…/derivar-universo-obligatorio.py | sha256sum         db9c8b69ed9070e8…
git show f2e4d58:…/derivar-universo-obligatorio.py | wc -l             496
git show f2e4d58:…/derivar-universo-obligatorio.py | sha256sum         6f8c98a29edf0c31…

filas del manifiesto que NO casan contra `21f1ccb` (árbol DECLARADO)       1  — la fila 8
filas del manifiesto que NO casan contra `f2e4d58` (commit del MANIFIESTO) 0
suma de la columna «líneas» de sus 13 filas de §4                     23 491
suma de la columna «líneas» de sus 54 filas de §5                     30 281
                                                                    ────────
titular publicado en su §2 y en su §6                                 53 772
```

**La aritmética confirma de qué árbol habla la tabla.** El titular **53 772 SÍ cuadra** con
sus dos subsumas —a diferencia del manifiesto anterior, donde no cuadraba—, y cuadra
**porque las 67 filas son las del árbol del gate**. Contra el árbol declarado, `b498f3b8`,
las cifras serían **53 768** y **23 487**: cuatro líneas menos, que son exactamente las
cuatro que el commit del manifiesto añadió al derivador.

**Qué se sigue.**

```text
NO SE PUEDE  citar «todo derivado del árbol b498f3b8…» como que las 67 filas describan la
             CANDIDATA. Describen el árbol del gate, `826e6ede` (commit `f2e4d58`), que el
             manifiesto no nombra en ningún sitio
SÍ SE PUEDE  usar las 67 filas y sus dos restas: son correctas contra el árbol del gate, y
             el adjudicador `X` las recalculó sin una discrepancia
REINCIDENCIA es `U-02`/`T-10` otra vez, en el mismo fichero y en la misma fila, un gate
             después. Lo que faltó no fue detectarlo: fue ACOTAR LA FILA cuando se detectó
YA REMEDIADO en la fuente, y no en el texto: `emitir-sobre-de-ancla.py` publica desde esta
             tanda LOS DOS ÁRBOLES con su derivador, sus fuentes, sus líneas y su digest
             derivados cada uno de SU commit, **y la lista de rutas en que difieren**; y
             obliga al revisor, dentro del propio sobre, a contrastar cada fila contra el
             árbol que ESA fila declara
```

## 9 · Este corrigendum incumplía su propia cabecera en cuatro de sus seis entradas

> **Lo levanta `W2-08` del documento 24.** La cabecera promete que «*toda cifra de este
> documento se DERIVA del árbol en el momento de escribirla, y se dice con qué comando*».

**Lo que decía el árbol antes de esta tanda:**

```text
ENTRADA  publica cifras   publica el COMANDO
  §1         sí                 NO
  §2         sí                 NO
  §3         sí                 NO
  §4         sí                 sí   (`grep -n 'ERRATA CONFIRMADA' …`, `sed -n '628p'`)
  §5         sí                 NO
  §6         sí                 sí   (columna COMANDO con `python3 …` y `git show …`)
                                ────
                       CUATRO de SEIS sin comando
```

**Qué se sigue, y qué se ha hecho.** No es un error de hecho —las cifras de las cuatro
entradas se han vuelto a derivar y **ninguna cambia**—: es que el lector no podía
reejecutarlas, que es justamente lo que la cabecera prometía. **Las cuatro entradas llevan
ya su comando**, añadido en esta tanda y verificado ejecutándolo. Es la misma disciplina que
`P-08` impuso al universo obligatorio: una cifra sin comando es una cifra escrita a mano,
aunque quien la escribió la hubiera derivado.

## 10 · Regla general que este documento deja escrita

```text
UN DICTAMEN NO SE EDITA. Si contiene un error de hecho, se registra en este corrigendum con
su sede, la cifra derivada del árbol y lo que se sigue. Añadir una entrada aquí NO cambia
ningún veredicto y NO reabre ninguna adjudicación.

UNA FRASE DE UN DICTAMEN CON ENTRADA EN ESTE CORRIGENDUM NO PUEDE CITARSE como fundamento
de otra afirmación sin citar también la entrada que la acota.

CUANDO SE ACOTA UN TITULAR DERIVADO DE UNA TABLA, SE ACOTA TAMBIÉN LA FILA de la que viene
la diferencia. La entrada §6 acotó el titular de líneas del manifiesto del segundo gate y no
la fila del derivador; el manifiesto siguiente repitió el defecto en esa misma fila, y hubo
que escribir dos entradas más —§7 y §8— para decir lo que una sola habría dicho.

TODA CIFRA DE ESTE DOCUMENTO VA CON SU COMANDO, sin excepción. Cuatro de las seis primeras
entradas no lo llevaban (§9), y una cifra sin comando no es refutable.
```
