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

**La cifra vigente, DERIVADA, con su comando** —`Z2-11`: esta entrada publicaba «hoy da
**ONCE**» sin decir de dónde, en un documento cuya cabecera promete que toda cifra va con su
comando. La sede real de los escenarios es §11.5 del documento 11, que es lo que el documento
13 estaba contando:

```bash
awk '/^## 11\.5 /{f=1;next} /^## 11\.6 /{f=0} f' \
    docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | grep -cE '^\| `NP-[0-9]+`'   # → 11
```

```text
escenarios negativos vigentes en §11.5   11   (`NP-1` … `NP-11`)
lo que el documento 13 confirmó como errata   DIEZ
lo que el documento 12 decía cuando se escribió la errata   SEIS
```

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

## 10 · Manifiesto del CUARTO GATE (4B) · «cada fila declara el árbol» es falso para su §4

**Sede:** `verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md`
**L78–L79**: «*Todo derivado del árbol del gate, nada copiado. **Cada fila declara el árbol
contra el que se contrasta**, y el sobre publica las rutas en que los dos árboles difieren*».

**Lo que dice el árbol**, derivado de las CABECERAS de las dos tablas, con su comando:

```bash
M=docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md
sed -n '81p'  "$M" | tr '|' '\n' | sed 's/^ *//;s/ *$//' | grep -n .   # cabecera de §4
sed -n '113p' "$M" | tr '|' '\n' | sed 's/^ *//;s/ *$//' | grep -n .   # cabecera de §5
sed -n '81p'  "$M" | grep -ciE 'árbol|arbol|tree'                       # → 0
```

```text
COLUMNAS DE §4   #  ·  ruta  ·  líneas  ·  SHA-256  ·  `1bis`  ·  revisor  ·  relevo
                 columnas que NOMBRAN un árbol:  0
COLUMNAS DE §5   #  ·  ruta  ·  líneas  ·  SHA-256  ·  `1bis`  ·  lectura íntegra certificada en
                 y ESA última columna sí lo nombra, fila a fila: «documento **22**, L1583 ·
                 árbol `4d231ee`»
```

**Qué se sigue.** El TITULAR de §2 del manifiesto —«70 fuentes · 58 796 líneas **—sobre el
árbol del GATE—**»— **es honesto y el adjudicador `AA` verificó las 70 filas contra ese
árbol**: la reincidencia `U-02`→`X-06` está rota y eso no se toca aquí. Lo que no se sostiene
es la promesa **POR FILA** para la §4: sus filas no declaran árbol porque no tienen columna
donde hacerlo. **NO SE PUEDE** citar L78–L79 para sostener que una fila de la §4 dice de qué
árbol habla; **SÍ SE PUEDE** citarla para la §5, que sí lo hace. Lo levantó `Z2-09`≡`Z-12`.
Es la regla de §14 —acotar el titular **y** la fila— aplicada al revés que en §6: aquí el
titular está bien y la promesa por fila no se cumple.

## 11 · Manifiesto del CUARTO GATE (4B) · 52 de sus 54 agotamientos citan documentos que su §4 no asigna a nadie

**Sede:** el mismo manifiesto, **§5**, sus 54 filas, columna «lectura íntegra certificada en».

**Lo que dice el árbol**, derivado de las dos tablas del propio manifiesto:

```bash
M=docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md
sed -n '115,200p' "$M" | awk -F'|' '/^\|/{print $7}' \
  | grep -oE 'documento \*\*[0-9]+\*\*' | sort | uniq -c        # 11 → 21 · 41 → 22 · 2 → 23
sed -n '83,112p' "$M" \
  | grep -cE '21-GATE-INDEPENDIENTE-DE-CIERRE|22-GATE-INDEPENDIENTE-DE-CERTIFICACION'   # → 0
```

```text
DOCUMENTOS QUE CITAN LAS 54 FILAS DE §5     documento 21   11
                                            documento 22   41
                                            documento 23    2
                                                          ────
                                                            54
RUTAS DE §4 (reparto para LECTURA ÍNTEGRA)  documentos 21 y 22 asignados a alguien:  0
                                            (§4 asigna 23 y 24, no 21 ni 22)
```

**Qué se sigue.** La **regla 1** del agotamiento —«fila propia con `LEÍDO ÍNTEGRO` … se cita
con documento y línea»— exige **abrir la línea citada** para comprobarla. En este gate nadie
tenía asignados los documentos 21 ni 22, de modo que **52 de los 54 agotamientos no eran
verificables por ningún revisor de este gate desde dentro de su lote**. No se sigue que sean
falsos —el adjudicador `AA` los verificó uno a uno contra los tres árboles que citan y los dio
**54/54 PLENOS**—: se sigue que **el manifiesto no puede citarse como prueba de que el gate
los verificó**, sino de que un adjudicador lo hizo. Lo levantó `Z-10`, y `AA` lo adjudicó
rechazando su formulación y aceptando su fondo. Es la cuarta repetición de `C-2`→`T-11`→`W-17`.

## 12 · Este corrigendum · su cabecera afirma una INMUTABILIDAD que el árbol desmiente

**Sede:** la cabecera de este mismo documento: «*Los dictámenes de gate y los manifiestos de
reparto son **INMUTABLES**: una vez publicados **no se editan**…*».

**Lo que dice el árbol**, con su comando:

```bash
git log --oneline -- docs/evolucion/19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md
```

```text
d868bcb  fix(f4c): aplicar la tanda de correccion del gate definitivo — D96–D102, PN-15, …
652ab8e  docs(f4c): gate definitivo independiente
                                                    → DOS commits: el documento 19 SE EDITÓ
                                                      después de publicarse
docs/evolucion/20-…-F4C.md   1 commit
docs/evolucion/21-…-F4C.md   1 commit
```

**Qué se sigue.** «No se editan» está escrito como si fuera un HECHO MEDIDO del árbol, y **no
lo es: es una REGLA**, y el documento 19 la incumple en el propio historial. La regla sigue en
pie y `G-22` la EJECUTA hoy —contrasta cada dictamen contra `HEAD` y contra la revisión base,
y editar uno da ROJO—, pero `G-22` nació después del documento 19. **Lo que se acota es el
tiempo verbal**: la inmutabilidad es lo que este corpus EXIGE desde que existe el inventario
de `G-22`, no lo que puede afirmar de todo su pasado. Quien cite la cabecera para sostener que
ningún dictamen ha cambiado nunca, cita mal. Lo levantó `Z2-12`.

## 13 · Documento 25 · el gate que lo publica está DECLARADO INVÁLIDO por su propio adjudicador, y eso se cita entero o no se cita

**Sede:** `25-CUARTO-GATE-DE-CERTIFICACION-F4C.md`, §2 de la adjudicación de `AA` y su §15.

**Lo que dice el árbol**, con su comando:

```bash
grep -c 'INSUFICIENTE PARA F5' docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md   # → 10
grep -n 'el GATE ES INVÁLIDO\|este gate es además INVÁLIDO' \
     docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md | head -3
```

```text
VEREDICTO EMITIDO      INSUFICIENTE PARA F5   ·  la cadena aparece 10 veces en el
                       documento: los TRES titulares —`Y4`, `Z3` y `AA`— y sus recapitulaciones
VALIDEZ DEL GATE       DECLARADA INVÁLIDA por el adjudicador `AA`, §2: los cinco sobres
                       ENTREGADOS difieren en los campos 1, 3, 6, 7, 9, 12, 13 y 14
LO QUE `AA` DICE DE SU PROPIO VEREDICTO   «las razones 2, 3 y 4 son independientes de la
                       invalidez y bastan cada una por sí sola»
```

**Qué se sigue.** El documento 25 es a la vez un veredicto y la declaración de que el
procedimiento que lo produjo no fue válido. **NO SE PUEDE** citar su `INSUFICIENTE PARA F5`
como un veredicto de un gate válido, ni citar su invalidez para retirarle fuerza a las razones
2, 3 y 4, que su propio adjudicador declara independientes. **SÍ SE PUEDE** citar cada
hallazgo suyo por separado: están reproducidos con salida y con controles. La entrada existe
para que ninguna sede derivada escoja la mitad que le convenga.

## 14 · Manifiesto del QUINTO GATE · rotula «sobre el árbol del GATE» dos cifras que son de la CANDIDATA — `DD-18`

**Sede:** `verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md` **§2**
—«`UNIVERSO DERIVADO 74 fuentes · 66 747 líneas —sobre el árbol del GATE—`»— y su **§6**,
que repite las dos cifras en la resta de totales.

**Lo que dice el árbol.** Las dos cifras se derivan sobre los DOS árboles con el mismo
derivador, materializando cada commit como prescribe la RECETA DEL SOBRE. **Ninguna se
copia:**

```bash
for C in 8c9ca9c $(git rev-parse gate/f4c-certificacion-5-20260831); do
  D=$(mktemp -d)
  GIT_INDEX_FILE=$D.idx git read-tree "$C"
  GIT_INDEX_FILE=$D.idx git checkout-index -a -f --prefix="$D/"
  ( cd "$D" && python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py \
      | grep 'fuentes obligatorias' )
done
```

```text
ÁRBOL DE LA CANDIDATA   8c9ca9c   74 fuentes · 66 747 líneas   ← lo que el manifiesto PUBLICA
ÁRBOL DEL GATE          5ed7a3b   75 fuentes · 66 940 líneas   ← lo que el manifiesto ROTULA
DIFERENCIA                        +1 fuente · +193 líneas
LA FUENTE QUE FALTA               el propio manifiesto en curso, que entró en el universo
                                  cuando `AA-01` convirtió `manifiestos/` en ZONA BARRIDA
```

**Qué se sigue.** Las cifras **son correctas del árbol de la CANDIDATA**, que es el objeto
que el gate juzga; lo falso es el rótulo. **NO SE PUEDE** citar §2 ni §6 de ese manifiesto
para afirmar nada del árbol del GATE. **SÍ SE PUEDE** citarlas para el árbol candidato, que
es de lo que hablan. **El manifiesto no se edita**, y por eso esto vive aquí: es la vía que
la regla §14 de este documento prescribe, y que la clase de §6, §7 y §8 —dos manifiestos
anteriores, mismo defecto, misma fila— hizo necesaria.

**Y consta la agravante:** es la **TERCERA instancia** de la clase `U-02`→`X-06`, que el
adjudicador `AA` declaró **ROTA** un gate antes, **en el campo que el sobre manda mirar
PRIMERO**. La corrección de una instancia no cerró la clase.

## 15 · Manifiesto del QUINTO GATE · `OBLIGATORIO − ASIGNADO = 0` sobre el árbol del gate es INALCANZABLE, y lo será en todos los siguientes — `DD-19`

**Sede:** el mismo manifiesto, **§6**, renglón `OBLIGATORIO menos ASIGNADO   0`.

**Lo que dice el árbol.** El remedio de `AA-01` —convertir `manifiestos/` en ZONA BARRIDA—
metió **el manifiesto en curso dentro de su propio universo**, y §5.4 obliga a que cada fila
publique el SHA-256 de su fuente. Un manifiesto no puede contener su propia huella: fijarla
la cambia. Por tanto, **sobre el árbol del GATE la resta no puede dar cero**, y no por un
descuido de esta tanda:

```text
SOBRE EL ÁRBOL DE LA CANDIDATA   OBLIGATORIO − ASIGNADO = 0     ALCANZABLE, y es lo medido
SOBRE EL ÁRBOL DEL GATE          OBLIGATORIO − ASIGNADO = 1     INALCANZABLE por construcción
                                 la fuente que sobra es el manifiesto en curso
```

**Qué se sigue.** **NO SE PUEDE** leer «`OBLIGATORIO − ASIGNADO = 0`» como una propiedad del
árbol del gate: es una propiedad del árbol de la CANDIDATA, y sólo ahí es satisfacible.
**SÍ SE PUEDE** exigirla del árbol candidato, que es el objeto del reparto.

**LO QUE SE CORRIGE HACIA ADELANTE, y es la primera de las tres vías que `DD` ofrece —«la
primera cuesta una palabra»:** desde el gate siguiente **todo manifiesto ROTULA EXPLÍCITAMENTE
DE QUÉ ÁRBOL habla cada cifra**, y **publica LAS DOS aritméticas** —la del árbol candidato y
la del árbol del gate— en vez de una sola sin rótulo. La regla vive en «El criterio del gate
siguiente» del `CHECKPOINT-ADS-NEXT.md`, que es su sede, y **este corrigendum no la crea: la
registra**.

**No se toca el derivador para que se excluya a sí mismo**, que era la tercera vía: un
instrumento que se saca del universo que deriva es exactamente la clase de perímetro escrito
que `DD-01` acaba de cerrar un piso más abajo.

## 16 · Manifiesto del SEXTO GATE (`6B`) · su resta sobre el árbol del gate publica `1` y son `2` — `EE-02`

**Sede:** `verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md`, **§2**
—«la diferencia estructural es exactamente **+1 fuente: este fichero**»— y **§6**, renglón
`OBLIGATORIO menos ASIGNADO  1`.

**Lo que dice el árbol.** Las dos cifras se derivan sobre el árbol del gate, materializado
como prescribe la RECETA DEL SOBRE. **Ninguna se copia:**

```bash
C=ce2cb4299fa04bc1c491f7bce2a4d0fbd87e4759
d=$(mktemp -d)
GIT_INDEX_FILE="$d/idx" git read-tree "$C"
GIT_INDEX_FILE="$d/idx" git checkout-index -a -f --prefix="$d/t/"
( cd "$d/t" && python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py \
    | grep 'fuentes obligatorias' )
git show "$C:docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-6B-20260831.md" \
  | grep -cE '^\| [0-9]+ \| `'
rm -rf "$d"
```

```text
UNIVERSO DEL ÁRBOL DEL GATE     78 fuentes
FILAS DE REPARTO DEL MANIFIESTO 76
OBLIGATORIO − ASIGNADO           2      ← el manifiesto publica 1
LAS DOS QUE SOBRAN
  …-6B-20260831.md   el manifiesto EN CURSO. Su exención es real: no puede contener su
                     propio SHA-256, y es lo que `DD-19` fija
  …-6-20260831.md    el manifiesto SUSTITUIDO. **NO es punto fijo**: existe en el commit
                     antes de que se escriba el `6B`, su SHA-256 se puede publicar sin
                     alterarlo, y **278 líneas obligatorias quedaron sin asignar a nadie**
```

**Qué se sigue.** **NO SE PUEDE** citar el §2 ni el §6 del manifiesto `6B` para afirmar que
sobre el árbol del gate falta exactamente una fuente. **SÍ SE PUEDE** citarlos para el árbol
de la CANDIDATA, donde la resta cierra a `0` y está verificada por el adjudicador.

**Y consta la agravante, que es lo que hace que esta entrada exista:** `DD-19` escribió la
regla —«todo manifiesto rotula de qué árbol habla cada cifra y publica las dos aritméticas»—
y **el primer manifiesto que la aplica la incumple en su primer uso**, no por copiar del
gate anterior sino por **razonar mal la exención**: la exención de punto fijo cubre al
manifiesto EN CURSO y a ningún otro fichero. `BB4` había predicho la sexta reincidencia de
esta clase, y ésta es.

**LO QUE SE CORRIGE HACIA ADELANTE:** desde el gate siguiente, el §6 de todo manifiesto
**DERIVA las dos aritméticas con su comando en vez de copiarlas**, y toda fuente que quede
sin fila **lleva su razón derivada y publicada**, una a una. La regla vive en «El criterio
del gate siguiente» del `CHECKPOINT-ADS-NEXT.md`.

## 17 · Manifiesto del SEXTO GATE (`6B`) · el preámbulo de su §5 describe una regla más estricta que la que aplica — `EE-08`

**Sede:** el mismo manifiesto, **§5**, preámbulo: «*una fuente sólo se agota si su SHA-256 de
HOY coincide **byte a byte** con el que publicó el gate que la certificó*».

**Lo que dice el árbol.** La regla que el manifiesto REALMENTE aplica —y que es la correcta,
y la que §5 punto 2 escribe— es que los bytes sean idénticos **a los del árbol que ESE gate
leyó de verdad**. Dos de sus sesenta filas no pueden satisfacer la versión estricta del
preámbulo, porque el gate que las certificó **no publicó un SHA-256 para ellas**: su
manifiesto las anotó con `—` en la columna de huella.

**Qué se sigue.** **NO SE PUEDE** citar el preámbulo del §5 como si describiera el criterio
ejecutado. **SÍ SE PUEDE** citar el punto 2 de ese mismo §5, que es el criterio real y el que
se aplicó. **El agotamiento de las sesenta filas NO queda en duda**: el adjudicador verificó
las setenta y seis filas contra el árbol de la candidata sin una discrepancia. Lo que falla es
la DESCRIPCIÓN, y es la clase de la entrada §5 de este corrigendum —«describe de más su propia
evidencia»—, una sede más allá.

## 18 · Documento 26 · su §5 publica un desglose por severidad que sus propias filas no dan — `EE-14`

**Sede:** `26-QUINTO-GATE-DE-CERTIFICACION-F4C.md`, §5, bloque de recuento por severidad y
origen. **El documento es INMUTABLE y NO se toca.**

**Lo que dice el árbol.** El desglose se deriva de la tabla de hallazgos del propio documento:

```bash
awk '/^\| \*\*`DD-[0-9]/{print}' docs/evolucion/26-QUINTO-GATE-DE-CERTIFICACION-F4C.md |
  grep -oE '\*\*(BLOQUEANTE|GRAVE|MEDIO ESTRUCTURAL|MEDIO|MENOR)\*\*' | sort | uniq -c
```

**Qué se sigue.** El TOTAL —veintidós— y la CLASIFICACIÓN —`A` 22, `B` 0, `C` 0— **son
correctos y no se discuten**: se derivan de las filas y el adjudicador los sostuvo. Lo que no
casa fila a fila es el reparto entre las columnas «DEL OBJETO» y «DEL APARATO». **NO SE PUEDE**
citar ese desglose por origen como censo derivado. **SÍ SE PUEDE** citar el total, la
clasificación y cada fila.

**Y lo que se corrige es la PROYECCIÓN VIVA, no el documento:** toda sede derivada que
reproduzca ese desglose lo publica **con el comando que lo deriva de las filas**, o remite. El
documento 26 **se conserva intacto**, que es lo que `G-22` custodia y lo que la regla §19 de
este corrigendum prescribe.

## 19 · Manifiesto `B` del GATE FINAL · su §8 pierde la precondición «para un gate válido» de `O21` — `HH2-08`

**Sede:** `manifiestos/F4C-ASIGNACION-GATE-FINAL-O21-20260901B.md`, §8, en el bloque
`(A) COBERTURA`.
**Afirma**: «Si las seis se cumplen, **DEBE** certificar: no es un acto discrecional».

**Lo que dice la SEDE CANÓNICA**, derivado del árbol y no citado de memoria:

```text
COMANDO                                                                       RESULTADO
awk '/^# /{p = ($0 ~ /^# `O21`/)} p' docs/owner/ADS-OWNER-RESOLUCIONES.md |
  grep -c 'Para un gate'                                                             1
grep -c 'gate válido' \
  docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-FINAL-O21-20260901B.md  0
```

`O21` §3 condiciona la obligación: **«Para un gate válido:** … si se cumplen las seis
condiciones … el adjudicador **debe** declarar». El §8 del manifiesto reproduce la obligación
**sin esa precondición**, y leído literalmente obligaría a certificar cobertura también sobre
un gate INVÁLIDO — que `O21` no dice y que §11.6 del documento 11 contradice.

**QUÉ SE SIGUE, y es poco:** nada del gate que corrió bajo ese manifiesto cambia. Su
adjudicador **declaró el gate VÁLIDO antes de medir la cobertura**, de modo que la
precondición se cumplió de hecho y la diferencia no tuvo efecto. **Lo que no se puede hacer es
citar el §8 de ese manifiesto como formulación de `O21`**: la formulación es la de la sede.

**POR QUÉ VA AQUÍ Y NO SE CORRIGE EN EL FICHERO:** los manifiestos son INMUTABLES, y esta es
la sede que el corpus tiene para señalar sus errores de hecho sin tocarlos. Las otras dos
sedes que compartían el defecto —§15.4 del documento 11 y la fila del índice— **sí son
editables y están corregidas**.

## 20 · Regla general que este documento deja escrita

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
entradas no lo llevaban (§9), y la cifra sustantiva de §4 tampoco (§12, por `Z2-11`); las
dos cosas están corregidas. Una cifra sin comando no es refutable.

NINGUNA HUELLA SE ABREVIA A MANO, EN NINGÚN INFORME —`DD-22` del QUINTO GATE—. `CC2`
tecleó `91fe62d3691521…` por `91fe62d369152f…` en la columna abreviada de una fila cuya
columna «recalculado» llevaba el valor completo y correcto: no era transcripción del sobre
—`CC2` lo embebe entero byte a byte 197 líneas más arriba— pero **es la clase exacta que
mató al CUARTO GATE**, donde ocho campos transcritos a mano difirieron entre cinco relevos.
Si una huella se abrevia, se DERIVA: `cut -c1-N`, `git rev-parse --short`, o el propio
comando que la produce. Una mano entre el dato y el informe es la única puerta que el sobre
de ancla no puede cerrar por construcción.

UNA REGLA NO SE ESCRIBE EN TIEMPO DE HECHO MEDIDO. «Los dictámenes no se editan» es lo que
este corpus EXIGE, no lo que su historial dice: el documento 19 se editó después de
publicarse (§12). Lo que se afirme del árbol se deriva del árbol; lo que se exija, se escribe
como exigencia y se dice qué lo ejecuta — aquí, `G-22`.
```
