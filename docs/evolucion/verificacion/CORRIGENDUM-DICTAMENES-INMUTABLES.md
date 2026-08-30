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
SHA-256 completos en §4 y §5      0
apariciones de «LEÍDO ÍNTEGRO»    0
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
L76–L85:

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

**Lo que dice el árbol**, derivado de las cabeceras de `ADS-PENDIENTES`:

```text
última sección antes de `# BLOQUE D`   §17
luego el BLOQUE C es                   §13–§17
```

**Qué se sigue.** El documento 20 acierta y el 19 no. Un gate que hubiera tomado el rango del
documento 19 como universo habría dejado **dos secciones enteras sin leer**, y ninguna
comprobación lo habría dicho. El universo obligatorio de los gates posteriores **no se toma de
este rango**: se deriva con `derivar-universo-obligatorio.py`, que toma el fichero completo.

## 4 · Documento 13 · una «ERRATA CONFIRMADA» que hoy está superada

**Sede:** `13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md` **L42** y **L618**, que fijan
«ERRATA CONFIRMADA · DIEZ» sobre una cifra que el documento 12 hoy da como **ONCE**.

**Qué se sigue.** La verificación del documento 13 fue correcta **cuando se hizo**, y quedó
superada por una corrección posterior sin que nada lo marcara. No se corrige el dictamen: se
marca aquí que **su cifra describe un estado anterior del corpus**, y que la vigente es la del
documento 12.

## 5 · `ADDENDUM 1` del gate de certificación · describe de más su propia evidencia

**Sede:** `verificacion/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` **L77–L79**,
que afirma que las doce fuentes que siguen AGOTADAS tienen en el documento 21 «su ruta, sus
líneas y **su SHA-256**».

**Lo que dice el árbol.** Tres de las doce publican en el documento 21 **sólo los primeros
hexadecimales**, no el digest completo:

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

## 6 · Regla general que este documento deja escrita

```text
UN DICTAMEN NO SE EDITA. Si contiene un error de hecho, se registra en este corrigendum con
su sede, la cifra derivada del árbol y lo que se sigue. Añadir una entrada aquí NO cambia
ningún veredicto y NO reabre ninguna adjudicación.

UNA FRASE DE UN DICTAMEN CON ENTRADA EN ESTE CORRIGENDUM NO PUEDE CITARSE como fundamento
de otra afirmación sin citar también la entrada que la acota.
```
