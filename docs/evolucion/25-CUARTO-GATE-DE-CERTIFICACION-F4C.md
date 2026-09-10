# CUARTO GATE DE CERTIFICACIÓN DE F4c — DECLARADO INVÁLIDO POR SU PROPIO ADJUDICADOR

> **Veredicto del adjudicador `AA`: `INSUFICIENTE PARA F5`. Y ADEMÁS: EL GATE ES INVÁLIDO.**
> **`F4c` NO se cierra y sigue ABIERTA. `F5` NO queda autorizada. Ningún hallazgo se ha
> corregido en esta pasada.**
>
> **Y `C-L.5` pasa de CERTIFICADA a ABIERTA, por primera vez en cuatro gates.**

## 0 · Qué es este documento

Registro **LITERAL** de los tres dictámenes de un gate independiente sobre la candidata
`dc9be3f68b3961fe4fa6010b4e446c24fc1510cb`, publicada en
`review/f4c-o19-sede-canonica-candidate-20260830`. Los tres se transcriben **enteros y sin
suavizar**, en §A, §B y §C. Lo escrito antes de §A lo escribe el **coordinador**, que no es
ninguno de los ocho, **que no ha juzgado nada, y que es la causa de la invalidez**.

## 1 · POR QUÉ ESTE GATE ES INVÁLIDO, Y LA CULPA ES DEL COORDINADOR

`O18` adoptó el **SOBRE DE ANCLA** como raíz de confianza externa, y `O19` ordenó que llevara
además la huella de la sede canónica del Owner. El emisor lo produjo correctamente: `AA`
verificó que **todos sus campos reproducen byte a byte**.

El manifiesto de este gate es
[`F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md`](verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md),
y se enlaza aquí **en el mismo commit que publica el gate**. Hubo un intento anterior cuyo
manifiesto **no llegó a repartirse a nadie** y que vive sólo en las ramas publicadas
`review/f4c-gate-certificacion-4-20260830` y `…-4-emisor-…`: **no está en este árbol**, y por
eso se nombra sin enlazarlo. El
hallazgo `Y3-02` —que el primero quedó huérfano y dejó `T147` en rojo por cuarta vez— consta
en el dictamen, junto con el defecto de diseño que lo causa: si el instrumental cierra antes
del manifiesto y éste se commitea solo y último, **no queda commit donde enlazarlo**.

**Lo que falló fue la ENTREGA.** El coordinador **transcribió el sobre a mano** en el encargo
de cada relevo, y las cinco transcripciones **no son idénticas**. `AA` las coteja campo a
campo:

```text
DIFIEREN EN OCHO CAMPOS      1 · 3 · 6 · 7 · 9 · 12 · 13 · 14
                             no en uno, como los dos dictaminadores creyeron

EL CAMPO 9 —SHA-256 DEL      se entregó sólo a `Z2`. Y no lo exige sólo §11.6: lo ordena
DERIVADOR—                   **el Owner**, en la sede canónica L315-317. Ninguno de los dos
                             dictaminadores usó ese fundamento

LA OBLIGACIÓN DEL            «COMPROBAR QUE SEAN IDÉNTICOS entre sí, CAMPO A CAMPO …
ADJUDICADOR, LITERAL         DECLARAR INVÁLIDO EL GATE ante CUALQUIER diferencia entre
                             sobres», y **pre-rechaza con sus palabras exactas** la defensa
                             que los dos intentaron: «aunque los dos árboles existan y los
                             dos dictámenes coincidan»
```

**`AA` resuelve CONTRA LOS DOS dictaminadores**, y lo argumenta: refuta el argumento Merkle
de `Y4` —haría `X-O6` inejecutable siempre, y `X-O5` prohíbe compensar— y descarta también
la vía por la que `Z3` llegaba a la invalidez, explicando en cuál se apoya en su lugar.

**Es la primera vez que este expediente produce un gate inválido, y lo produce el
coordinador.** No el corpus, no la batería, no la candidata: la mano que copió el sobre.

## 2 · La cobertura, que esta vez SÍ es una de las razones

```text
OBLIGATORIO menos ASIGNADO   ∅     70 = 70
ASIGNADO menos LEÍDO         1     `DECISIONES-Y-CONTRADICCIONES.md`, 1 196 líneas.
                                   `Y3` no dejó manifiesto de lectura de sus fuentes, y `AA`
                                   cerró el `CHECKPOINT` leyéndolo él mismo —3 816 líneas—
                                   pero el registro no está en su lote

CONSECUENCIA                 §8 EXCLUYE LA SUFICIENCIA POR SÍ SOLO, sin necesidad de un
                             solo hallazgo

C-L.5                        pasa de CERTIFICADA a **ABIERTA**. Primera vez en cuatro gates
AGOTAMIENTOS                 54/54 pasan las dos reglas, verificados por `AA`
```

**Y consta que `Y4` lo declaró contra su propia cadena** antes de que nadie se lo señalara.

## 3 · El veredicto, y sus razones

```text
VEREDICTO   INSUFICIENTE PARA F5     ·     EL GATE ES INVÁLIDO

1  el gate es INVÁLIDO: las cinco transcripciones del sobre difieren en OCHO campos, y la
   obligación del adjudicador pre-rechaza la defensa que los dos dictaminadores ensayaron

2  `ASIGNADO − LEÍDO = 1`. La regla de cierre excluye la suficiencia por sí sola, y
   `C-L.5` deja de estar certificada

3  `M-04` sigue viva: `AA` reprodujo SEIS árboles en 38/38 verde, EXIT=0, SIN COMMITEAR,
   con cuatro controles en rojo. Y añadió uno que nadie había visto: un segundo documento
   del Owner por la VÍA SANCIONADA —enlazado desde el índice— que declara `F4c` cerrada y
   `F5` autorizada, pasa 38/38 commiteado y sin commitear, y **queda fuera del universo,
   del manifiesto y del sobre**. Sobrevive al arreglo del bug que otro revisor encontró,
   porque el derivador ancla una RUTA LITERAL

4  al menos CATORCE de los 36 hallazgos los introdujo esta misma tanda
```

```text
36 HALLAZGOS DISTINTOS      0 bloqueantes · 12 graves · 13 medios · 11 menores
                            18 de `Y` · 16 de `Z` · 4 propios de `AA` · menos 2 solapes

CLASIFICACIÓN               A · coherencia interna                    23
                            B · identidad de la candidata              5
                            A+B                                        8
                            C · actor privilegiado                     0
                            DECISIÓN DEL OWNER                         0
```

**`AA` no funda nada en `C`** —ejecutó él mismo el ataque con privilegio y **no lo cuenta**—
y declara expresamente que **NO hay ninguna decisión del Owner pendiente**: los treinta y
seis tienen remedio determinado dentro de `F4c`.

## 4 · La causa raíz, y por qué el trabajo sigue

**`AA` responde en dos mitades, y la primera es una buena noticia que ningún gate anterior
podía dar:**

> **NO es la misma causa raíz en lo esencial.** Los gates 21, 22, 23 y 24 fallaron porque la
> verificación estaba anclada **dentro del objeto verificado**. **Éste no.** Los tres remedios
> que el adjudicador `X` dejó determinados **están aplicados y FUNCIONAN**, y `AA` verificó
> los tres. La sede real está protegida; el emisor y el derivador también.
>
> **Lo que falla es la mitad que nadie había podido medir hasta ahora: la ENTREGA, no la
> producción.** Y no tiene ninguna defensa mecánica, porque ocurre fuera del árbol.

**Y la segunda mitad, que es la que duele:**

> **SÍ es la misma causa en el MÉTODO.** El perímetro escrito se cerró y el `basename` se
> abrió **en el commit del propio remedio de `O19`**. Es la quinta vez consecutiva que una
> tanda introduce, al corregir, la puerta que el gate siguiente encuentra.

**`AA` dictamina que EL TRABAJO DEBE SEGUIR**, y expresamente **sin escribir una protección
interna nueva**: «lo que falta es de resta y de disciplina».

## 5 · Lo que este gate SÍ ha cerrado

```text
· los TRES remedios del tercer gate están aplicados y FUNCIONAN, verificados por `AA`
· los 54 agotamientos pasan las dos reglas, y también bajo el árbol del addendum
· la reincidencia `U-02`/`X-06` está ROTA: el manifiesto tiene 70 filas y CERO
  discrepancias contra el árbol del gate
· la SEDE CANÓNICA cumple: metadatos completos, `O1`-`O16` NO reconstruidos, el DISEÑO no
  ha cambiado —siete cotejos cláusula a cláusula— y **cero amplificación** en la proyección,
  verificada byte a byte en los tres bloques trasplantados
· `X-01` del documento 24 está CERRADO Y GENERALIZA: el inventario se deriva del directorio,
  y una puerta trasera sin commitear da `FALLO G-34`
· la exención de región histórica del checkpoint baja del 56 % al 32,5 %
· `M-04` no cae, pero **seis refutaciones de `AA` NO cayeron**, y son las que protegen el
  ancla real
```

---

# §A · DICTAMEN DEL REVISOR `Y`, LITERAL

# DICTAMEN DEL REVISOR `Y` — `Y4`, DICTAMINADOR · CUARTO GATE (4B) DE CERTIFICACION DE F4c
INFORME INCREMENTAL. Se escribe a medida que se verifica.

## ESTADO: EN CURSO

### PASO 0 — SOBRE, RECALCULADO POR MI, DE COMMITS
| campo | recibido | recalculado | casa |
|---|---|---|---|
| tree candidata | 0cd9a2ef051ba2a509e13338912c17ecbed70506 | idem | SI |
| tree gate | 50def63d3aff7d8a4bed2056e1473732bd957c30 | idem | SI |
| ref remota candidata -> commit | dc9be3f6… | git ls-remote origin: idem | SI |
| ref remota gate -> commit | 82d87836… | idem | SI |
| sha manifiesto | fc490259…adb599 | idem (del commit del gate) | SI |
| universo candidata | 69 / 58576 / d9e46d75…f8c9e | idem (receta a mano, emisor NO ejecutado) | SI |
| universo gate | 70 / 58796 / 7b3c0ede…15e8f | idem | SI |
| sha derivador candidata | c102c547…24919f | idem | SI |
| sha derivador gate | fd1d1505…b12dec | idem | SI |
| sede (los dos commits) | db46edd2…018d4a | idem, identico en los dos | SI |
| O17 / O18 / O19 | 0cc5b9b5 / ab9d9447 / cb2487fc | idem | SI |
| rutas que difieren = 4 | README, derivador, emisor, manifiesto 4B (A) | idem | SI (etiqueta del sobre imprecisa) |
| ASIGNACIONES 23 | derivadas | 2+1+3+3+2+9·1+2+1 = 23 sobre las 16 filas | SI |
NINGUN CAMPO DEL SOBRE DIFIERE DEL ARBOL. El disparador de §8 del manifiesto NO se activa.

### VERIFICADO CONTRA FICHERO Y LINEA
- Y3-01 CONFIRMADO Y AGRAVADO: 1d3b5d4 = un solo hunk @@ -1004 +1004,87 @@; la seccion O18
  (849-1008) recibe CERO lineas, CERO menciones de `O19`, CERO marcas [HISTORICO].
  L864 sigue afirmando en presente «`docs/owner/` contiene DOS documentos» — el arbol del
  gate tiene TRES y contiene O17/O18/O19. Premisa falsificada por el propio gate.
- Y3-02 CONFIRMADO: el comando publicado en 00-INDICE L149-152 sale 1 nombrando el
  manifiesto 4B. grep en todo el arbol = 0 referencias (los otros cinco: 5..10).
- Y3-03 REATRIBUIDO EJECUTANDO LOS DOS ARBOLES:
    dc9be3f6 (candidata) -> CODIGO 0 · T147 SUPERADA · 261 documentos  == lo publicado
    82d8783  (gate)      -> CODIGO 1 · T147 FALLIDA  · 262 documentos
  La evidencia publicada es VERDADERA de la candidata y FALSA del arbol del gate.
- Y1-01 CONFIRMADO: L2606 «las cuatro alternativas» sobre tabla A..E = CINCO filas.
- Y1-07 CONFIRMADO: L3235 «las cuatro preguntas» sobre CINCO rotulos.
- Y1-04 CONFIRMADO: L1999-2002 «Seis pasos» sobre cadena de OCHO operaciones.
- Y1-03 CONFIRMADO Y AMPLIADO A OCHO SEDES (Y1 dio seis, dos se le escaparon):
  L796 · L1179 · **L1241 (`W11`)** · L1352 · L1579 (`X55`) · **L1582 (`X58`)** · L2304.
  L831 SE REBAJA: no contradice D105.
  7b8839d («propagar D105 …») toco EXACTAMENTE `W17` y `X54` y ninguna otra fila:
  dejo `W11` siete filas mas arriba y `X55`/`X58` en la fila contigua.
- Y2-02 CONFIRMADO: L7511 «`O17` esta integra en DECISIONES…» contra sede L20-22 y `X-O11`.
- Y2-03 CONFIRMADO Y ELEVADO A GRAVE: la sede (sha verificado) da CERO en «commits firmados»,
  «refs protegidas», «C7», «fuera del repositorio», «identidad propia»; unica «mecánica» en
  L210 y es otra frase. El texto entrecomillado y atribuido a `O18` en L8497 y L10243 NACE en
  DECISIONES L910, dentro de «(c) UN VERIFICADOR EXTERNO DE VERDAD» del bloque de ALTERNATIVAS
  QUE SE PRESENTARON: es la pregunta del coordinador, no la respuesta del Owner. `X-O13`.
- Bateria: `grep -cniE 'titular|regla de titulares'` sobre comprobar-correccion = 0, sobre 36
  `check(`. La regla de §0 no tiene guardian. CONFIRMADO.

### LOTE PROPIO · IDENTIDAD
| fichero | lineas | SHA-256 recalculado | manifiesto |
|---|---|---|---|
| docs/evolucion/23-… | 2913 | 0f81f13d8cb319d8ccc5243d19bb26d7f71f57e860cde2eb2edefe33b6993dc2 | fila 3 · CASA |
| docs/evolucion/24-… | 2515 | 8df584529c857c071954b0d1b426faff82277e29a43556abe5dccfd93714fae1 | fila 4 · CASA |

### CIERRES VERIFICADOS POR MI (doc 24 → arbol del gate)
CERRADOS: V-01 (el sobre publica LOS DOS arboles; recalcule los dos) · V-02 (la sede ratifica
las TRES condiciones, L178-182) · V-03 rotulo (L8578 «LITERAL DE LA SEDE CANONICA…RATIFICADO
MEDIANTE O19», con su nota L8580) · V-04 (L498 dice hoy RESOLUTIVO, y L505 registra el cambio)
· V-05 (la receta publicada reproduce los DOS digest: lo hice) · V-22/S-23 (el punto 7 reparte
por estado observable y el propio punto 3 impide el solape) · X-02 (DECISIONES L867 y sede L142
declaran INVERIFICABLE) · X-03 (el sobre ancla sede, identificadores y digest por resolucion)
· X-04 (metodo/last_meaningful_event/based_on reanclados en O19, con regla de reanclaje) ·
X-05 (23 asignaciones, DERIVADAS; las derive) · X-06 (cada fila declara su arbol).
NO CERRADOS: V-06/X-07 (T147 + evidencia; TERCERA recurrencia) · V-09 · V-10 · V-11 · V-12 ·
V-13 (L1213 escribe DIECIOCHO en la frase que jura no escribirlo) · V-14 · V-16 · V-17 · V-18 ·
V-19 (L10612-10624) · V-21/S-25 (la fila D107 sigue citando reglas 7-10, no las doce) · V-20.
FUERA DE MI LOTE: W-01…W-17, V-07/V-08 (bateria y emisor como codigo), V-15.

### HALLAZGOS PROPIOS MIOS (no traidos por Y1/Y2/Y3)
· §11.8 L8590 escribe «**CI o** el ejecutor externo»; la sede (L193) dice solo «el ejecutor
  externo». `grep -c '\bCI\b'` sobre la sede = 0. Bajo el rotulo «LITERAL DE LA SEDE CANONICA
  DEL OWNER». Es X-O13 en pequeño, y en direccion PROTECTORA.
· DECISIONES L864 (entrada de O18, VIVA, sin [HISTORICO]): «`docs/owner/` contiene **DOS**
  documentos y **ninguna** de las resoluciones `O15`-`O18`». El arbol del gate publica TRES y
  contiene O17/O18/O19. Es la PREMISA con la que la entrada declara O18 INVERIFICABLE, y el
  propio gate la falsifico. Y L963 repite la cifra dentro del bloque de hechos de `X`.
· Y1-03 tiene DOS sedes mas de las que Y1 vio: `W11` (L1241) y `X58` (L1582), ambas en las
  MISMAS tablas que 7b8839d edito (toco `W17` y `X54` y nada mas).
· Y3-05 verificado con git: PN-17/18 son de 609863e (tanda O17) y PN-19 de 8e70d94 (tanda O18);
  esta tanda NO añade ninguna. La frase esta en el campo que presume de REMITIR.

### REFUTACIONES QUE INTENTE Y NO CAYERON (parcial)
· «§11.8 amplia la condicion 1 al escribir «y PROBADO»» — NO CAE: la sede L212-213 lo escribe
  («mientras esa sustitucion no exista **y este probada**»).
· «el reparto de §11.8 no es literal de la sede» — NO CAE: seis lineas contra seis, en sentido
  identico. Solo el sujeto «CI o» se añade.

---
# DICTAMEN CERRADO DEL REVISOR `Y` — emitido por `Y4`, DICTAMINADOR

## 1 · IDENTIDAD, INDEPENDENCIA Y MODO
Soy `Y4`, dictaminador del REVISOR `Y` del CUARTO GATE (4B) de certificación de F4c.
No he escrito una línea de este corpus, no apliqué ninguna corrección, no participé en ningún
gate anterior. **NO he abierto `Z1.md`, `Z2.md` ni `DICTAMEN-Z.md`**: constan en el directorio de
notas y no los he leído. NO usé el subagente `Agent`. NO corregí nada.
`git status --porcelain` VACÍO al abrir y VACÍO al cerrar. HEAD `82d8783` idéntico en los dos
extremos. Rama `gate/f4c-certificacion-4b-20260830`.
ORDEN RESPETADO: primero `Y1`, `Y2`, `Y3`; después mi lote (documentos 23 y 24).
Todo lo que ejecuté es de sólo lectura o se ejecutó sobre copias `git archive` en el scratchpad.

## 2 · EL SOBRE · MI DECISIÓN EXPRESA

### 2.1 · Lo que recalculé yo, de commits, antes de leer contenido
Los DOCE campos del sobre reproducen BYTE A BYTE. Tabla en el PASO 0 de arriba. Incluye los dos
digest de universo derivados a mano con la receta publicada, **sin ejecutar el emisor**, como
`O19` ordena. **NINGÚN campo del sobre difiere de lo que el árbol muestra.**

### 2.2 · El hecho que aporta el coordinador, contrastado por mí
El coordinador declara que el sobre **transcrito a los encargos NO fue idéntico**: a `Z2` le
entregó además los dos SHA-256 DEL DERIVADOR; a `Y1`, `Y2`, `Y3` y `Z1`, no. Y a ninguno la
fecha/hora ni la identidad nominal.
LO QUE PUEDO CONTRASTAR YO, y lo hago: las transcripciones de `Y1` (§0.1), `Y2` (§0) y la tabla
de `Y3` (§0) **NO llevan el SHA-256 del derivador, ni el campo 13, ni el campo 14**, y el
sobre EMITIDO (`sobre4b.txt`) **sí los lleva los tres**. La diferencia entre el sobre emitido y
el transcrito queda establecida por mi propia comparación. La diferencia CON EL LADO `Z` la
tomo del coordinador, que es el único que puede aportarla, y así consta su procedencia.

### 2.3 · Qué fila adversarial aplica — ADJUDICADO
`X-O6` (L8363) · **CONFIRMADO, y para los CINCO relevos.** «el sobre omite un campo —típicamente
el SHA-256 del derivador— … → **FALLA**». Faltan los campos 13 y 14 en las cinco
transcripciones y el 9 en cuatro de cinco; y el campo 1 llegó como ruta LOCAL, no como
identificador remoto completo. La **obligación 6** de §11.6 fue INEJECUTABLE para `Y1`, `Y2` y
`Y3`. Y no es sólo §11.6: **la SEDE CANÓNICA lo ordena en su propio texto**, L323-326: «*Cada
revisor debe recibir externamente: … el SHA del manifiesto · **el SHA del derivador** · el SHA
de la sede del Owner*». **Es una orden literal del Owner, incumplida en el primer gate que se
celebra bajo `O19`.**

`X-O3` (L8355) · **SE CUMPLE EN SU LETRA Y NO EN SU RATIO, y lo demuestro.**
· EN SU LETRA: los sobres difieren entre revisores, y la obligación del adjudicador
  —«COMPROBAR QUE SEAN IDÉNTICOS … campo a campo»— queda incumplida.
· EN SU RATIO, NO: `X-O3` enumera lo que tiene que diferir para que la fila dispare —«distinto
  commit, distinto `tree`, distinto SHA-256 del manifiesto **o** distinto digest del universo»—
  y su fundamento es «**no leyeron el mismo encargo** … coincidir sobre objetos distintos no es
  acuerdo». **NINGUNO de esos cuatro campos difiere.** Todos los relevos recibieron el mismo
  commit, el mismo tree, el mismo SHA del manifiesto, el mismo digest de universo, la misma
  ruta y huella de sede y los mismos tres digest de resolución. **Leyeron el mismo objeto.**

### 2.4 · ¿INVALIDA EL GATE? — MI DECISIÓN, DEMOSTRADA Y NO PRESUMIDA
**NO recomiendo declarar el gate INVÁLIDO. El objeto NO está en duda, y ésta es la
demostración EXPRESA que §8 del manifiesto exige.**

1 · **El disparador de §8 no se activa.** §8 invalida ante «*cualquier diferencia entre el SOBRE
    recibido y lo que el árbol muestra*». **No hay ninguna**: recalculé los doce campos desde
    los dos commits y los doce reproducen.
2 · **El campo omitido es REDUNDANTE con un campo que SÍ se entregó, y es una redundancia
    criptográfica, no una conjetura.** El campo 4 —ARBOL DEL GATE `50def63d…`— es la raíz Merkle
    del árbol entero, y ese árbol **contiene** el derivador:
      `git ls-tree -r 50def63d… -- …/derivar-universo-obligatorio.py` → blob `0319c308…`
      `git ls-tree -r 0cd9a2ef… -- …/derivar-universo-obligatorio.py` → blob `12fdaf6f…`
    Quien verificó el campo 4 —y `Y1`, `Y2`, `Y3` y yo lo verificamos— **ancló el derivador con
    la misma fuerza criptográfica** que le habría dado el campo 9. El campo 9 sólo es NO
    redundante para un derivador que viva FUERA del árbol anclado, que no es el caso.
3 · **Y el campo 10 cierra la otra mitad.** El digest del universo llegó por el canal externo y
    los tres relevos lo rederivaron a mano desde el commit, sin ejecutar el emisor: **la SALIDA
    del derivador está anclada externamente aunque su huella no viajara.**
4 · **Y el sobre no es reconstruido a posteriori (`X-O1`) ni cambiado tras crear revisores
    (`X-O2`).** Cronología, de las marcas de los commits y de los ficheros:
      sede `1d3b5d4` 23:05:06 · candidata `dc9be3f` 23:13:06 · instrumental `4f01f9f` 23:27:16 ·
      manifiesto `82d8783` 23:28:46 · **sobre emitido 23:29:04** · primer relevo 23:41.
    El sobre es POSTERIOR al manifiesto y ANTERIOR a todo revisor, que es exactamente lo que
    §11.6 «CUÁNDO» exige. Existe además un sobre previo (`sobre4.txt`, 23:22) que anclaba OTRO
    commit de gate (`23107c7a`) y que **se retiró emitiendo uno NUEVO y repartiendo desde el
    principio** —la rama se llama `4b`—, que es literalmente la única salida que `X-O2` admite.
5 · **La sede no se pudo tocar tras el reparto.** `git log --follow` sobre
    `docs/owner/ADS-OWNER-RESOLUCIONES.md` devuelve **UN SOLO commit**, `1d3b5d4`, y
    `git diff dc9be3f6 82d8783 -- docs/owner/` es **vacío**: byte-idéntica en los dos árboles.

**CONCLUSIÓN DEL §2.** El objeto está identificado y no está en duda: lo demuestro, no lo
presumo. Lo que falló es **la DISCIPLINA DE ENTREGA del instrumento**, no la identidad de lo
juzgado. Por eso emito dictamen de contenido en vez de parar, y por eso lo registro como
`Y-01`, **GRAVE**, clase **A**.
**Y digo lo que esto NO me autoriza a hacer.** No me autoriza a tratarlo como formal.
`X-O6` es la fila que este gate ha disparado, y la fila enumera exactamente el campo que faltó.
**La decisión de INVALIDEZ no es mía: §11.6 se la da al adjudicador, y `AA` es el adjudicador.**
Le entrego el hecho, su procedencia y la demostración con la que decidir, y hago constar que
`X` —doc 24 §2.2— nombró «dos sobres distintos entre revisores» como una de las TRES cosas que
le habrían hecho declararlo inválido. **`AA` debe resolverlo expresamente y no heredarlo de mí.**

## 3 · LA SEDE CANÓNICA, JUZGADA
**LEÍDA ÍNTEGRA POR MÍ**, las 334 líneas, SHA-256 `db46edd2…018d4a` recalculado.

**¿ES AUTORIDAD DE VERDAD? SÍ, con una reserva de rótulo.** A favor, y lo verifiqué:
· nace en UN commit y no se ha tocado; byte-idéntica en los dos árboles del gate
· el sobre publica su ruta, su huella DEL COMMIT AUDITADO y **un digest por resolución**
· la proyección de `O19` (DECISIONES L1010-1012) se declara PROYECCIÓN DERIVADA y **ENLAZA**
· §9.2 y §9.6 **se NIEGAN** a resolver tres huecos «*porque sería ampliar una resolución del
  Owner*» — es la conducta contraria a ampliar, y es la prueba más fuerte a su favor
· `D108` aparece como PROYECCIÓN en las ocho sedes que lo nombran, nunca como autoridad
LA RESERVA: **tres sedes del documento 11 siguen señalando la PROYECCIÓN como el texto íntegro
de una resolución del Owner** — L7511 (`O17`), L9338 (`O17`), L9352 (`O18`) —, contra la
cláusula AUTORIDAD de la sede (L20-22) y contra `X-O11`. Es `Y-08`.

**¿ALGUNA PARÁFRASIS AMPLÍA EL TEXTO CANÓNICO? SÍ, en la ATRIBUCIÓN, y es `Y-05`.** Barrido
mecánico sobre la sede verificada: «commits firmados» 0 · «refs protegidas» 0 · «C7» 0 · «fuera
del repositorio» 0 · «identidad propia» 0 · «mecánica» 1, y es OTRA frase (L210). Y el texto
entrecomillado y atribuido a `O18` en L8497-8498 y L10243-10245 **nace en DECISIONES L910**,
dentro del bloque «*Las TRES alternativas que se presentaron*», renglón «(c) UN VERIFICADOR
EXTERNO DE VERDAD»: **es la PREGUNTA que el coordinador puso al Owner, no la respuesta que el
Owner emitió**. Y §16 va más lejos: «*dice con sus palabras que «toca `C7`»*» — cero en la sede,
y el propio documento 24 L287 ya había establecido que «toca `C7`» vive en la línea `EN CONTRA`
de la pregunta. Es `X-O13` en la sede que va al Owner por `PN-19`.
Segundo caso, menor: §11.8 L8590 escribe «**`CI` o** el ejecutor externo» bajo el rótulo «LITERAL
DE LA SEDE CANÓNICA DEL OWNER»; la sede (L193) dice sólo «el ejecutor externo» y `grep -c '\bCI\b'`
sobre ella da **0**. Amplía en dirección PROTECTORA, y `O19` no distingue dirección. Es `Y-09`.

**¿HA CAMBIADO EL DISEÑO? NO.** Lo contrasté cláusula a cláusula:
· las DOCE reglas de `O17` (sede L94-120) contra §9.6 — coinciden regla a regla
· el reparto de `O17` (sede L124-131) contra §9.6 L7350-7367 — literal
· las TRES condiciones (sede L178-182) contra §11.8 L8603-8610 — palabra por palabra
· el reparto de `F6` (sede L186-193) contra §11.8 L8580-8594 — seis contra seis
· «NO SE AFIRMA QUE PROTEJA FRENTE A» (sede L242-248) contra §11.7 — seis y seis
· lo que `O19` declara (sede L280-292) contra §11.9 L8674-8684 — diez y diez
**El DISEÑO no se ha tocado. Lo que se ha tocado, y mal, es la PROCEDENCIA de tres citas.**

## 4 · MANIFIESTO DE LECTURA DEL REVISOR `Y` — Y LA RESTA
| # | fuente asignada a `Y` | líneas | quién la leyó | ¿declaración válida de LECTURA ÍNTEGRA? |
|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 185 | `Y3` (sin declaración) · **`Y4`, yo, ÍNTEGRA** | **SÍ, la cerré yo** |
| 2 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 11392 | `Y1` L1-5700 · `Y2` L5701-11392, con tramos | **SÍ** |
| 3 | `docs/evolucion/23-…F4C.md` | 2913 | **`Y4`, yo, ÍNTEGRA** | **SÍ** |
| 4 | `docs/evolucion/24-…F4C.md` | 2515 | **`Y4`, yo, ÍNTEGRA** | **SÍ** |
| 5 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 3816 | `Y3` por temas · `Y2` sólo L1836-2030 | **NO** |
| 15 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 334 | `Y2` ÍNTEGRA · **`Y4`, yo, ÍNTEGRA** | **SÍ** |
| 16 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1196 | `Y3` por temas · `Y2` acotado a O17/O18/O19/D107/D108 | **NO** |

MI LOTE, con tramos, para que se compruebe que abrí y no barrí:
· doc 24 (2515 · `8df58452…`): 1-320 · 320-700 · 700-880 · 880-1150 · 1150-1600 · 1594-1650 ·
  1649-1810 · 1810-2111 · 2111-2310 · 2311-2515. **Unión = [1, 2515].**
· doc 23 (2913 · `0f81f13d…`): 1-300 · 300-400 · 400-700 · 700-1050 · 1045-1080 · 1075-1400 ·
  1400-1800 · 1800-2200 · 2200-2620 · 2620-2913. **Unión = [1, 2913].**
· ANCLA A, doc 24 L2226: «*`F4` no elige ninguna, y lo dice.*»
· ANCLA B, doc 23 L2913 (a 2 913 líneas de la anterior, en el otro documento):
  «**ADJUDICADOR `U` · adjudicacion cerrada.**»
· sede (334 · `db46edd2…`): 1-120 · 120-240 · 240-334. **Unión = [1, 334].**
· 00-INDICE (185 · `4f5d7d86…`): 1-88 · 88-110 · 110-160 · 160-185. **Unión = [1, 185].**
Los CUATRO SHA-256 que recalculé coinciden con las filas 1, 3, 4 y 15 del manifiesto del gate.

```
LA RESTA
  FUENTES ASIGNADAS AL REVISOR `Y`                     7   ·  22 351 líneas
  CON DECLARACIÓN VÁLIDA DE LECTURA ÍNTEGRA            5   ·  17 339 líneas
  ─────────────────────────────────────────────────────────
  ASIGNADAS − LEÍDAS  =  **2**   ·  5 012 líneas
                         CHECKPOINT-ADS-NEXT.md (3 816) · DECISIONES-Y-CONTRADICCIONES.md (1 196)
```
**NO ES CERO, y lo digo contra el interés de mi propia cadena.** `Y3` tenía asignadas CUATRO
fuentes y **no dejó manifiesto de lectura**: ni tramos, ni SHA-256 recalculados, ni una sola
declaración «LEÍDO ÍNTEGRO» por ruta. Derivó cifras con `grep`, abrió las líneas de sus
hallazgos y verificó estructura — **y eso no es lectura**, como los documentos 23 y 24
establecen tres veces. Cerré `00-INDICE` yo mismo porque son 185 líneas y no admite excusa.
**Las otras dos no las cerré, y no las disimulo con una resta que dé cero.**
`C-L.5` L11355-11358 lo dice sin adorno: «*cualquier fuente ASIGNADA pero NO LEÍDA impide la
suficiencia, **con independencia de los hallazgos***». **Se aplica.**

## 5 · HALLAZGOS DE `Y`, CONSOLIDADOS — severidad y clase adjudicadas POR MÍ
Criterio, el mismo de los cuatro gates anteriores: **BLOQUEANTE** obliga a decidir arquitectura
nueva · **GRAVE** una garantía publicada no se sostiene · **MEDIO** una afirmación vigente es
falsa sin cambiar el comportamiento · **MENOR** editorial o de propagación.
Clase: **A** coherencia interna · **B** identidad de la candidata · **C** actor privilegiado.

### GRAVES — siete
| id | qué es | sede | clase |
|---|---|---|---|
| **`Y-01`** | **el SOBRE se entregó INCOMPLETO y DESIGUAL.** Campos 13 y 14 ausentes en las cinco transcripciones; campo 9 —SHA-256 del derivador— ausente en cuatro de cinco; campo 1 como ruta local. La **obligación 6** de §11.6 fue inejecutable para `Y1`,`Y2`,`Y3`. Incumple además la **orden literal de la SEDE CANÓNICA L323-326**. `X-O6` disparada; `X-O3` en su letra. Demostración de que el objeto NO está en duda, en §2.4 | §11.6 **L8192-8202** · sede **L323-326** | **B** |
| **`Y-02`** | **`D105` sin propagar a OCHO sedes vivas.** `abandonada` NO retira el marcador —lo retira el paso 6, tras el `deriva` durable y su marcador— y ocho sedes escriben lo contrario: **L796** (§2.6.1, la sede definitoria) · **L1179** · **L1241 `W11`** · **L1352** · **L1579 `X55`** · **L1582 `X58`** · **L2304** (con el orden invertido). El commit `7b8839d` «propagar `D105`…» tocó **exactamente `W17` y `X54`** y ninguna otra fila: dejó `W11` siete filas más arriba y `X55`/`X58` en la fila contigua. Un implementador que lea §2.6.1, `W11`, `X55` o `X58` **reconstruye `M-03`**, el bloqueo perdido en silencio | doc 11 | **A** |
| **`Y-03`** | **el manifiesto de ESTE gate es HUÉRFANO y deja `T147` FALLIDA sobre el árbol del gate**, con código real 1 y 262 documentos. `grep -r` en todo el árbol = **0** referencias (los otros cinco manifiestos: 5 a 10). El comando que `00-INDICE` L149-152 publica sale **1** nombrándolo. **TERCERA recurrencia consecutiva** de `S-18`≡`T-14` (doc 23) ≡ `V-06`/`W-16` (doc 24) | `00-INDICE` **L114-120** · el manifiesto | **A** |
| **`Y-04`** | **la evidencia publicada declara VERDE donde el árbol del gate da ROJO.** `evidencia/referencias-salida.txt` publica «*código: 0 · T147 SUPERADA · 261 documentos*». **REATRIBUIDO ejecutando el validador sobre los DOS árboles**, como hizo `U`: candidata `dc9be3f6` → código **0**, SUPERADA, **261**; gate `82d8783` → código **1**, FALLIDA, **262**. La evidencia es VERDADERA de la candidata y FALSA del árbol del gate. `X-07` del doc 24, reincidente | `kernel/operativo/pruebas/evidencia/` | **A** |
| **`Y-05`** | **tres citas entrecomilladas atribuidas al Owner que la SEDE CANÓNICA no contiene**, y una de ellas en la sede que va al Owner. Nacen en `DECISIONES` **L910**, en el bloque de las ALTERNATIVAS QUE SE PRESENTARON: **la pregunta del coordinador, no la respuesta del Owner**. `X-O13` | doc 11 **L8497-8498**, **L10243-10246** | **A** |
| **`Y-06`** | **la entrada de `O18` NO recibió ni una línea de `O19`, y su proyección afirma que sí.** `1d3b5d4` toca un solo hunk, `@@ -1004 +1004,87 @@`: la sección `O18` (849-1008) recibe CERO líneas, CERO menciones de `O19` y CERO marcas `[HISTÓRICO]`. Y L1068 escribe «*queda RESUELTA por `O19`, **y así se anota** sin tocar el texto*». **No se anotó.** L931 sigue rotulando «DISPUTA REGISTRADA Y NO RESUELTA» y L979-980 «*mientras no haya ratificación, esta disputa sigue ABIERTA*». **Y lo que lo agrava, y no lo trae nadie:** L864 sigue afirmando en presente «*`docs/owner/` contiene **DOS** documentos y **ninguna** de las resoluciones `O15`-`O18`*» — el árbol del gate publica **TRES** y contiene `O17`, `O18` y `O19`—, y **ésa es la premisa con la que la entrada declara `O18` INVERIFICABLE**. El gate falsificó la premisa de su propia sede y no la anotó | `DECISIONES` **L864**, **L931**, **L979-980**, **L1068** | **A** |
| **`Y-07`** | **la regla de titulares de §0 no tiene GUARDIÁN, y sobrevive a tres gates.** `grep -cniE 'titular|regla de titulares'` sobre la batería = **0**, sobre 36 `check(`. Vivas hoy: **L2606** «las cuatro alternativas» sobre tabla `A`–`E` de CINCO · **L3235** «las cuatro preguntas» sobre CINCO rótulos · **L1999-2002** «Seis pasos» sobre cadena de OCHO, en la sede que numera las fronteras de ventana · **L1213** «DIECIOCHO» escrito en la frase que jura no escribirlo · **L10612-10624**, que dice «*Cada familia lleva su cifra en SU sede y aquí se remite*» y copia cuatro. Son `V-09`…`V-13` y `V-19` del doc 24: **NO CERRADOS** | doc 11 **L145-176** y sus sedes | **A** |

### MEDIOS — cuatro
| id | qué es | sede | clase |
|---|---|---|---|
| **`Y-08`** | **tres sedes señalan la PROYECCIÓN como el texto íntegro de una resolución del Owner** — «`O17` está **íntegra** en `DECISIONES…` §2» (**L7511**), «su resolución es `O17`, **íntegra en la sección 2 del registro**» (**L9338**), ídem `O18` (**L9352**)—, contra la cláusula AUTORIDAD de la sede (L20-22), contra §11.9 y contra `X-O11`. La corrección de procedencia de `O19` se aplicó al lado `O18` de §11.6-§11.9 y **no al lado `O17` ni a §15.8** | doc 11 | **A** |
| **`Y-09`** | **§11.8 L8590 escribe «`CI` o el ejecutor externo» bajo rótulo «LITERAL DE LA SEDE CANÓNICA DEL OWNER»**; la sede L193 dice sólo «el ejecutor externo» y no contiene «CI» (`grep -c` = 0). Amplía el sujeto de una prohibición del Owner bajo etiqueta de literalidad | doc 11 **L8590** | **A** |
| **`Y-10`** | **el campo `pregunta_pendiente` VIGENTE del checkpoint va DOS tandas atrasado en el renglón que presume de REMITIR.** L1824: «*Las que **ESTA** tanda añade son `PN-17` y `PN-18`*». Verificado con `git log -S`: `PN-17` y `PN-18` los añade **`609863e`** (tanda `O17`) y `PN-19` **`8e70d94`** (tanda `O18`); **esta tanda no añade ninguna**. En el mismo campo que declara «*Este campo publicó una cifra a mano tres tandas seguidas y las tres caducaron … así que REMITE*» | `CHECKPOINT` **L1824** | **A** |
| **`Y-11`** | **COBERTURA: `ASIGNADAS − LEÍDAS = 2` para el revisor `Y`** (CHECKPOINT 3 816 · DECISIONES 1 196). `Y3` no dejó manifiesto de lectura de sus cuatro fuentes. Por §8 del manifiesto y por la REGLA DE CIERRE de `C-L.5` esto **excluye la suficiencia por sí solo**, con independencia de los hallazgos | §4 de este dictamen | **A** |

### MENORES — siete
| id | qué es | sede |
|---|---|---|
| **`Y-12`** | `00-INDICE` L154-155: «*la lista cubre hoy los **tres** manifiestos de asignación*» —enlaza CUATRO y el árbol tiene CINCO— y «*da `T147` en verde*» — **falso hoy**, lo ejecuté | `00-INDICE` |
| **`Y-13`** | el `ALCANCE` de `O19` en la sede (L267) dice sólo «NO autoriza iniciar `F5`»; `O17` (L71) y `O18` (L156) dicen «`F5`, `F6` ni PesquerApp», y el checkpoint L34 escribe la versión ancha. La sede es aquí **más estrecha que su proyección** | sede **L267** |
| **`Y-14`** | residuos vivos de la conversión de `P-16`: «Y el **la** secuencia `4b`» (**L2306**) y «del secuencia `4b`» (**L2718**), con el corte de línea roto en L2304-2308 | doc 11 |
| **`Y-15`** | la condición anti-caducidad de `4b` es EVADIBLE: `grep -n 'desenlace .4b.'` admite **un** carácter, y la tipografía dominante del documento escribe ``**`4b`**`` — tres | doc 11 **L2185** |
| **`Y-16`** | «*un barrido literal sobre todo `docs/` devuelve **UNA** sola aparición*» — hoy devuelve **CUATRO**, en tres ficheros, y la cuarta es la propia frase | doc 11 **L1635** |
| **`Y-17`** | «*Fue cuatro, luego cinco, y **ahora seis***» fases, contra las CINCO vigentes que el propio documento escribe en seis sedes. `D85` barrió cuatro sedes y **ésta sobrevivió**, sin marca `[HISTÓRICO]` y con el adverbio «ahora» | doc 11 **L699** |
| **`Y-18`** | `S-25`≡`V-21` **NO CERRADO**: la fila `D107` sigue citando las reglas **7-10** de `O17` y no remite a §9.6, donde están las doce | `DECISIONES` **L534** |

```
RECUENTO, DERIVADO DE LAS FILAS DE ARRIBA
  BLOQUEANTE   0
  GRAVE        7    Y-01 … Y-07
  MEDIO        4    Y-08 … Y-11
  MENOR        7    Y-12 … Y-18
              ──
              18        clase A 17 · clase B 1 · clase C 0
```
**NINGUNO de mis dieciocho se apoya en `C`.** El Owner ha resuelto que la resistencia a un actor
privilegiado NO es exigible como implementación dentro de `F4c`, y **no declaro insuficiencia
por `C`**. Comprobé además que el corpus la trata bien: `C` se declara NO IMPLEMENTADA (§11.7
L8437-8438), el contrato de `F6` está completo, y **no encontré ni una sede que presente `(b)`
como `(c)`**. `Y-01` es `B`; los otros diecisiete son `A`.
**CUÁNTOS LOS INTRODUJO ESTA TANDA: seis** — `Y-01`, `Y-03`, `Y-04`, `Y-05`, `Y-06` y `Y-09`
nacen del aparato de este gate o de la propagación de `O19`. Los doce restantes son deuda
anterior que la regla de §0 y la propagación de `D105` no llegaron a barrer.

## 6 · HALLAZGOS QUE RECHAZO O REBAJO, CON EVIDENCIA
**`Y1-03`, la sede L831 · REBAJADA, y sale del hallazgo.** «*Ninguna fase salvo un TERMINAL
retira el marcador*» es una condición NECESARIA, no universal, y **sigue siendo verdadera bajo
`D105`**: no afirma que todo terminal lo retire. `Y1` la contó entre sus seis; yo la retiro y
en su lugar entran **dos que `Y1` no vio** —`W11` (L1241) y `X58` (L1582)—, que sí lo afirman.

**`Y2-05` · RECHAZADO.** «`O19` no tiene fila `D` y §15.8 no abre bloque». La sede canónica **no
exige una `D` por resolución** —lo leí entero: sus diez reglas de nacimiento no la mencionan—;
`O19` **no escribe ninguna decisión de F4** (corrige procedencia, y lo dice); el recuento sigue
derivándose (18 bloques `###`, que es lo que §0 L13-14 publica); y el ADDENDUM DE PROCEDENCIA
(L9365-9382) está **declarado y argumentado**. La regla de §15.8 dice «*toda tanda nueva abre su
bloque en el mismo acto en que escribe sus decisiones*»: **esta tanda no escribe decisiones.**

**`Y2-04` · NO LO CUENTO APARTE.** Los cuatro cardinales de L11220, L6069, L10615 y L10616 son
CORRECTOS hoy —los derivé—, y el defecto que `Y2` registra es que nada impide que caduquen.
Es exactamente la clase de `Y-07`, y va dentro, no al lado. Inflar el censo con el mismo defecto
contado dos veces es lo que los cuatro gates anteriores prohíben.

**`Y3-07` · REBAJADO a observación de redacción.** El sobre rotula la cuarta ruta «el manifiesto
del gate 3». La CANTIDAD (4) y las CUATRO rutas son exactas, lo verifiqué con
`git diff --name-status`. Y la línea admite la lectura «*el manifiesto del gate, 3: README,
derivador y emisor*», que es correcta. **Imprecisión, no defecto.**

**`Y3-04` · NO REPRODUCIDO POR MÍ, y lo declaro.** `Y3` dice que la batería ensucia el árbol con
dos ficheros `M`. **Yo no ejecuté `registrar_evidencia.py`**; ejecuté `comprobar_referencias.py`
y **no ensució nada** (`git status --porcelain` vacío después). No lo cuento entre mis dieciocho.

## 7 · LOS 43 DEL DOCUMENTO 24, EN MI FOCO
Foco de `Y`: arquitectura, protocolo, `O17`/`O18`/`O19`, sede canónica, registro, checkpoint,
`C-L`. Los de `Z` —batería, derivador, emisor, manifiestos, `M-04`— **NO los adjudico**.

| id | mi veredicto | evidencia con la que lo cierro o lo dejo abierto |
|---|---|---|
| `V-01` el sobre yuxtapone dos árboles | **CERRADO** | el sobre publica **LOS DOS** árboles con su propio derivador y sus propias cifras, y las rutas en que difieren. **Rederivé los dos**: 69/58 576/`d9e46d75` y 70/58 796/`7b3c0ede`. Ninguna insatisfacibilidad |
| `V-02` la propagación excede en dos condiciones | **CERRADO por el Owner** | la sede L178-182 contiene las TRES condiciones, **ratificadas**. `O19` resolvió que la omisión estaba en la transcripción |
| `V-03` rótulo «LITERAL DE `O18`» | **CERRADO en el rótulo · RESIDUO VIVO** | L8578 dice hoy «LITERAL DE LA SEDE CANÓNICA DEL OWNER, RATIFICADO MEDIANTE `O19`», con su nota L8580. **Pero L8497 y L10243 conservan la cita atribuida a `O18`**: es mi `Y-05` |
| `V-04` «`D1`–`D106` … texto ÍNTEGRO» | **CERRADO** | `DECISIONES` L498 dice hoy «texto **RESOLUTIVO** … sólo reciben punteros», y L505 y L524 registran el cambio |
| `V-05` la receta no reproduce el digest | **CERRADO** | **la ejecuté sobre los dos árboles y reproduce los dos digest**, byte a byte |
| `V-06`≡`X-07` `T147` y evidencia | **NO CERRADO · 3.ª RECURRENCIA** | mis `Y-03` y `Y-04`, reatribuidos sobre los dos árboles |
| `V-09` «Seis pasos» sobre ocho | **NO CERRADO** | L1999-2002 intacto. Dentro de `Y-07` |
| `V-10` la regla de §0 sin guardián | **NO CERRADO** | `grep` sobre la batería = 0. Es `Y-07` |
| `V-11` «cuatro alternativas» / cinco | **NO CERRADO** | L2606 con tabla `A`–`E`. Conté cinco |
| `V-12` «cuatro preguntas» / cinco | **NO CERRADO** | L3235 con cinco rótulos. Los conté |
| `V-13` «DIECIOCHO» ventanas | **NO CERRADO** | L1213 escribe el cardinal en la frase que jura derivarlo |
| `V-14` «las nueve señales del §16» | **NO CERRADO** (MENOR) | L3821 sigue apuntando al §16 de otro documento |
| `V-16` «devuelve UNA sola aparición» | **NO CERRADO** | hoy cuatro. Es `Y-16` |
| `V-17` la condición de `4b` evadible | **NO CERRADO** | es `Y-15` |
| `V-18` «Y el la secuencia `4b`» | **NO CERRADO** | L2306 intacto. Es `Y-14` |
| `V-19` §19 copia cuatro cardinales | **NO CERRADO** | L10612-10624. Dentro de `Y-07` |
| `V-20` predicado sin sujeto en §19 | **NO CERRADO** (MENOR) | el corte sigue |
| `V-21`≡`S-25` la fila `D107` | **NO CERRADO** | L534 cita reglas 7-10. Es `Y-18` |
| `V-22`≡`S-23` las cuatro ramas del punto 7 | **CERRADO** | reparten por **estado observable**, y la rama 3 del propio punto («*y sólo entonces retira el de transacción*») hace disjuntas la 2 y la 4 **desde dentro del punto**. Lo verifiqué |
| `V-23` la fila 8 del manifiesto | **CERRADO** | «Cada fila declara el árbol contra el que se contrasta», y las filas 7-10 llevan los SHA del árbol del gate, que es el suyo |
| `X-02` `O18` no declara su inverificabilidad | **CERRADO** | `DECISIONES` L867 y sede L142: «*no se afirma que sea falsa: se declara **INVERIFICABLE***» |
| `X-03` el sobre no ancla ninguna resolución | **CERRADO** | campos 15-18: ruta, huella del commit auditado, los tres identificadores y **un digest por resolución**. Los recalculé todos |
| `X-04` el bloque de estado dos eventos atrasado | **CERRADO** | `metodo`, `last_meaningful_event` y `based_on` reanclados en `O19` y en la sede, con `regla_de_reanclaje` escrita. **Pero `C-L.7` sigue NO CERRADA y así consta**, correctamente |
| `X-05` ASIGNACIONES 18 vs 17 | **CERRADO** | el sobre publica **23 DERIVADAS**; las derivé de las 16 filas: 2+1+3+3+2+9+2+1 = **23** |
| `X-06` el manifiesto §4 es falso en una fila | **CERRADO** | ver `V-23` |
| `S-01` vía 3 de `SEG` (doc 23, en mi foco) | **CERRADO** | las cuatro filas `FASE 0` de §18 dicen hoy «**`SEG` sin vía: `PN-13`** — y conserva su bloqueo, que es lo ÚNICO que `O17` le da». Las abrí las cuatro |
| `V-07`, `V-08`, `V-15`, `W-01`…`W-17` | **FUERA DE MI LOTE** | batería, emisor y derivador como código, y los manifiestos. **NO los adjudico y no los presumo ni cerrados ni abiertos** |

```
EN MI FOCO Y ADJUDICABLES POR MÍ   27
  CERRADOS                         12
  NO CERRADOS                      15   (once de ellos son la regla de §0 y sus sedes)
FUERA DE MI LOTE                   16   foco de `Z`. NO ADJUDICADOS
```
**Y lo que consta a favor, porque un dictamen que sólo lista defectos miente por omisión:** los
DOS defectos que hundieron el gate anterior están **genuinamente cerrados y con mecanismo** —el
sobre publica los dos árboles y su receta reproduce los dos digest; y `O19` cerró la disputa de
atribución con una SEDE EXTERNA en vez de con una decimonovena protección interna, que es
exactamente lo que `X` ordenó—. `§9.2` y `§9.6` **se niegan por escrito a ampliar una resolución
del Owner**. `C-L.7` llega **NO CERRADA** con su consecuencia `G-16`-en-rojo **declarada contra
sí misma**. Eso es la conducta que cuatro gates pedían.

## 8 · EL DEFECTO DE DISEÑO DE LA REGLA QUE ESTE GATE ESTRENA — JUZGADO
`Y3` señala que si el instrumental cierra ANTES del manifiesto y el manifiesto se commitea
**solo y último**, no queda commit donde enlazarlo desde `00-INDICE`, y `T147` queda en rojo por
construcción. **JUZGO: la tensión es REAL, y NO es insatisfacible. La recurrencia no queda
excusada.**
· La tensión existe: `00-INDICE` L114-120 exige el enlace **«en el MISMO commit que lo crea»**;
  §11.6 campo 6 dice que el manifiesto «*se commitea **solo** y antes de que exista ningún
  revisor*»; y la regla que este gate estrena añade «*el gate NO toca `verificacion/` después de
  publicar el manifiesto*».
· **Pero las tres son satisfacibles a la vez, y la salida no cuesta nada.** Ni `00-INDICE.md` ni
  `kernel/operativo/pruebas/evidencia/` están dentro de `verificacion/`: **la regla nueva no
  prohíbe tocarlos.** Y «solo» en el campo 6 no está definido como «único fichero del commit»:
  su función —que el campo 8 fija— es que el manifiesto **no se sustituya después del reparto**,
  y el campo 8 es el SHA-256 **del fichero**, que ancla el manifiesto byte a byte **sea cual
  sea lo demás que viaje en ese commit**.
· **LA SALIDA, y es de una línea:** el commit del manifiesto lleva **el manifiesto, su fila en
  `00-INDICE` y la evidencia derivada reejecutada**, y sigue siendo anterior a todo revisor.
  Cumple `C-L.5`, cumple el campo 6, cumple `00-INDICE` L114-120, cumple la regla nueva, y deja
  el árbol que se juzga con `T147` en verde y su evidencia verdadera.
**Por tanto `Y-03` y `Y-04` no son un dilema: son un incumplimiento de una regla cumplible, por
tercera vez consecutiva, escrita por el propio corpus y denunciada por su propio comando.**

## 9 · REFUTACIONES QUE INTENTÉ Y NO CAYERON
**`R-1` · Intenté que el sobre AMPLIARA la condición 1 del Owner.** §11.8 escribe «*construido
**y PROBADO** antes de la adopción permanente*» y la sede L179 dice sólo «*debe existir antes de
la primera adopción permanente*». **NO CAYÓ:** la sede L212-213 escribe «*mientras esa
sustitución no exista **y esté probada***». El material está en la sede, en otro bloque.

**`R-2` · Intenté que el reparto de §11.8 no fuera literal de la sede.** Cotejé las seis líneas
de la sede (L186-193) contra las seis filas de §11.8 (L8580-8594). **NO CAYÓ:** coinciden seis a
seis y en el mismo orden. *(Lo único que sobrevive es el sujeto «`CI` o», que es `Y-09`.)*

**`R-3` · Intenté que la SEDE se hubiera tocado después del reparto —que habría sido `X-O9` y la
invalidez inmediata.** **NO CAYÓ, por tres vías:** `git log --follow` sobre la sede devuelve **UN
solo commit** (`1d3b5d4`, 23:05); `git diff dc9be3f6 82d8783 -- docs/owner/` es **vacío**; y los
cuatro digest —sede, `O17`, `O18`, `O19`— reproducen **idénticos en los dos commits**.

**`R-4` · Intenté que el sobre fuera reconstruido a posteriori (`X-O1`) o cambiado tras crear
revisores (`X-O2`).** **NO CAYÓ, y la evidencia va a favor del coordinador:** existe un sobre
ANTERIOR (`sobre4.txt`, 23:22) que anclaba OTRO commit de gate, y se **retiró emitiendo uno
NUEVO y repartiendo desde el principio** —la rama se llama `4b`—, que es la única salida que
`X-O2` admite. Y la cronología es estricta: manifiesto 23:28:46 → sobre 23:29:04 → primer relevo
23:41. **El sobre es posterior al manifiesto y anterior a todo revisor.**

**`R-5` · Intenté que `S-01` —la vía 3 de `SEG`, el GRAVE que abrió el doc 23— siguiera vivo.**
**NO CAYÓ:** abrí las cuatro filas `FASE 0` de §18 y las cuatro dicen «**`SEG` sin vía: `PN-13`**
— y conserva su bloqueo, que es lo ÚNICO que `O17` le da y lo único que §9.6 recoge».

**`R-6` · Intenté que `V-22`≡`S-23` siguiera abierto —las cuatro ramas del punto 7 no disjuntas.**
**NO CAYÓ:** el estado que las solaparía —`abandonada` durable, `deriva` ausente, marcador ya
retirado— es **inalcanzable por el propio punto 7**, cuya rama 3 escribe «*y sólo entonces retira
el de transacción*». La partición es total y disjunta sin necesidad de precedencia declarada.

**`R-7` · Intenté que el diseño de `O17` o de `O18` hubiera cambiado por el camino** —que es lo
que el manifiesto §7 declara GRAVE—. **NO CAYÓ, y lo contrasté siete veces**: doce reglas,
reparto de `O17`, tres condiciones, reparto de `F6`, seis no-garantías, alcance y las diez
cláusulas de `O19`. **Coinciden todas.** `O19` corrigió PROCEDENCIA, no DISEÑO.

## 10 · LO QUE NO HE CUBIERTO, SIN ADORNO
1. **`CHECKPOINT-ADS-NEXT.md` (3 816) y `DECISIONES-Y-CONTRADICCIONES.md` (1 196) NO están
   leídos íntegros por nadie de la cadena `Y`.** Abrí de ellos las regiones concretas de cada
   hallazgo —unas veinte— y nada más. **Es `Y-11`, es el hueco más grande de mi cobertura, y no
   lo disimulo con una resta.** Un defecto de contenido fuera de esas regiones se me escapa.
2. **No he leído el documento 11 con mis ojos.** Sus 11 392 líneas las leyeron `Y1` y `Y2`. Yo
   abrí y verifiqué las **sedes concretas** de cada hallazgo que confirmo, rebajo o rechazo
   —unas treinta— y las de los cierres de §7. Ningún ojo único ha recorrido ese fichero entero.
3. **No he juzgado la batería, el emisor, el derivador ni los manifiestos como código.** Son
   lote de `Z`. Ejecuté `comprobar_referencias.py` y el derivador **como instrumento de mis
   propias comprobaciones**, y lo declaro cada vez. **No adjudico ninguno de los `W-01`…`W-17`.**
4. **No ejecuté `registrar_evidencia.py` ni la batería adversarial.** Todo lo que digo del
   estado de la evidencia sale de ejecutar el validador canónico sobre los dos árboles, no de
   regenerarla.
5. **No he verificado ninguna cita que mis fuentes hacen de material APROBADO** —`a.6`, `a.7`,
   `b.16`, `C7`, `KERNEL.md`—. Las he leído como afirmaciones, no como hechos.
6. **`Y-01` descansa en parte en testimonio.** La desigualdad **entre los lados `Y` y `Z`** me la
   aporta el coordinador; yo sólo puedo contrastar el lado `Y`, y lo hice. Si el coordinador
   se equivoca, lo que queda en pie es `X-O6` para los cinco, que ya basta para el hallazgo.
7. **No he abierto los documentos 19, 20, 21 ni 22.** Lo que los documentos 23 y 24 dicen de
   ellos lo transcribo, no lo verifico.

## 11 · MI RECOMENDACIÓN DE VEREDICTO

# INSUFICIENTE PARA F5

### Las razones, numeradas. La primera y la tercera bastan cada una por sí sola.

**1 · La COBERTURA no cierra: `ASIGNADAS − LEÍDAS = 2` para el revisor `Y`.** El relevo `Y3` tenía
cuatro fuentes asignadas —`00-INDICE`, `CHECKPOINT`, la sede y el registro, 5 531 líneas— y **no
dejó manifiesto de lectura**: ni tramos, ni SHA-256 recalculados, ni una declaración «LEÍDO
ÍNTEGRO» por ruta. Cerré `00-INDICE` yo mismo y `Y2` cerró la sede; **el CHECKPOINT (3 816) y el
registro (1 196) siguen sin declaración válida**. La REGLA DE CIERRE que `C-L.5` publica
—L11355-11358— lo dice sin adorno: «*cualquier fuente ASIGNADA pero NO LEÍDA impide la
suficiencia, **con independencia de los hallazgos**»*. **`C-L.5` se reabre por el lado `Y`.**

**2 · `B` —identidad de la candidata— está establecida en su OBJETO y NO en su DISCIPLINA.** El
sobre reproduce los doce campos byte a byte y lo demuestro; pero **se entregó incompleto y
desigual**, faltando el campo que la propia SEDE CANÓNICA ordena entregar a cada revisor
(L323-326), y dejando la obligación 6 de §11.6 inejecutable para tres de mis cuatro relevos.
**Es el primer gate que se celebra bajo `O19` y ha incumplido una orden literal del Owner sobre
cómo se entrega el instrumento que `O19` crea.** `X-O6`, confirmada.

**3 · `A` —coherencia interna— NO SE SOSTIENE, y en el núcleo del protocolo.** `D105` —la
decisión que cierra `M-03`, «el bloqueo perdido en silencio»— **no está propagada a ocho sedes
vivas**, dos de ellas (`W11` y `X58`) **en las mismas tablas que el commit de propagación editó**:
tocó `W17` y `X54` y ninguna otra fila. Un implementador que lea §2.6.1, la ventana `W11` o los
contratos de prueba `X55` y `X58` **reconstruye exactamente el defecto que `D105` vino a cerrar**.

**4 · La corrección de procedencia que este gate estrena publica como palabras del Owner un
texto que la sede canónica NO contiene.** Tres citas entrecomilladas —«commits firmados, refs
protegidas…» y «toca `C7`»— nacen en `DECISIONES` L910, dentro de **la pregunta que el
coordinador puso al Owner**, y se atribuyen a `O18` en §11.8 y en `PN-19`, que es la sede que
vuelve al Owner. Es `X-O13`, **en el gate convocado precisamente para juzgar si alguna paráfrasis
amplía el texto canónico**.

**5 · La entrada de `O18` conserva viva la premisa que este mismo gate falsificó.** Declara
`O18` INVERIFICABLE porque «*`docs/owner/` contiene DOS documentos y ninguna de las resoluciones
`O15`-`O18`*». El árbol del gate publica TRES y contiene las tres. Y la proyección de `O19`
afirma que la disputa «*así se anota*»: **no se anotó ni una línea**, y dos renglones de la
entrada siguen declarándola ABIERTA en presente.

**6 · El aparato del propio gate deja el árbol que juzga con un validador canónico en ROJO y su
evidencia publicada FALSA, por TERCERA vez consecutiva.** Reatribuido ejecutando el validador
sobre los dos árboles: la candidata está limpia y en 261; el gate da código 1, `T147` FALLIDA y
262. Y la regla que este gate ESTRENA para impedirlo **no lo impide, y era cumplible** (§8).

### Lo que expresamente NO fundamenta mi recomendación
· **NO fundamento nada en `C`.** El Owner ha resuelto su fase, y comprobé que el corpus la trata
  bien: `C` declarada NO IMPLEMENTADA, contrato de `F6` completo, y ni una sede que presente
  `(b)` como `(c)`. **Ninguno de mis dieciocho es clase `C`.**
· **NO declaro el gate INVÁLIDO.** El objeto está identificado y lo demuestro expresamente en
  §2.4. **Que la entrega del sobre fallara es una insuficiencia, no una invalidez** — y la
  decisión de invalidez es de `AA`, a quien remito el hecho con su demostración.
· **NO fundamento nada en la batería, el emisor, el derivador ni los manifiestos.** Son foco de
  `Z` y no los he adjudicado.
· **NO fundamento nada en que quede arquitectura por inventar. Ninguno de mis dieciocho es
  BLOQUEANTE**, y los dieciocho se cierran con material que el corpus ya tiene escrito.

### Lo que consta a favor
`O19` es el remedio correcto y está bien ejecutado en lo esencial: **una sede externa en vez de
una decimonovena protección interna**, que es literalmente lo que `X` ordenó. El sobre publica
los DOS árboles y su receta **reproduce los dos digest** —`V-01` y `V-05` cerrados—. La sede
tiene un solo commit y es byte-idéntica en los dos árboles. `S-01`, `V-02`, `V-03` (rótulo),
`V-04`, `V-22`, `X-02`, `X-03`, `X-04`, `X-05` y `X-06` están **cerrados y los verifiqué uno a
uno**. §9.2 y §9.6 **se niegan por escrito a ampliar una resolución del Owner**. Y `C-L.7` llega
**NO CERRADA**, declarada contra el propio interés del corpus.
**El diseño no falla. Falla la propagación, la entrega y la lectura.**

> **Yo RECOMIENDO. El veredicto lo emite el adjudicador `AA`, que no soy yo.**
> **NO he visto el dictamen de `Z` y no lo veré.**

## 12 · CIERRE
```text
git status --porcelain  AL ABRIR   → VACÍO      git status --porcelain  AL CERRAR → VACÍO
HEAD al abrir y al cerrar          → 82d8783679da06b8ccd6ec5e770b5bf9980bf27f, idéntico
FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS   ninguno
COMMITS · PUSH · PR · MERGE                              ninguno
SUBAGENTE `Agent`                                        NO USADO
Z1.md · Z2.md · DICTAMEN-Z.md                            NO ABIERTOS
NINGÚN HALLAZGO SE HA CORREGIDO, y es deliberado: quien corrige no certifica.
```
**`F4c` sigue ABIERTA por mi parte. `F5` NO queda autorizada por mi parte.**
**REVISOR `Y` · dictamen cerrado por `Y4`.**

---

# §B · DICTAMEN DEL REVISOR `Z`, LITERAL

# DICTAMEN DEL REVISOR `Z` — CUARTO GATE DE CERTIFICACIÓN DE F4c
## Emitido por `Z3`, DICTAMINADOR de la cadena `Z`

```text
REPOSITORIO   /home/jose/ads-kernel
RAMA          gate/f4c-certificacion-4b-20260830
HEAD          82d8783679da06b8ccd6ec5e770b5bf9980bf27f  (idéntico al abrir y al cerrar)
FECHA         2026-08-30 / 31
INTÉRPRETE    Python 3.12.14 por el shim del scratchpad
LABORATORIO   /tmp/lab-Z3/{work,origin.git} — clon + origin bare propios. BORRADO
RECOMENDACIÓN INSUFICIENTE PARA F5   (el veredicto lo emite el adjudicador `AA`, no yo)
```

---

## 1 · IDENTIDAD, INDEPENDENCIA Y MODO

Soy `Z3`, dictaminador del revisor `Z`. **Recomiendo; no emito veredicto.**

**Qué NO soy.** No he escrito ninguna parte de este corpus, no he aplicado ninguna corrección, no
participé en ningún gate anterior y no fui revisor `A`–`X` de ninguno.

**Qué NO he visto.** **No he abierto `Y1.md`, `Y2.md`, `Y3.md` ni `DICTAMEN-Y.md`.** Constan en el
directorio de notas —los vi al listarlo, con sus tamaños y fechas— y no los he leído. Ninguna
afirmación de este dictamen procede del revisor `Y`, y **no adjudico ningún hallazgo de su foco**.
Tampoco abrí `DICTAMEN-V`, `DICTAMEN-W`, `X-FINAL` ni las notas de gates anteriores.

**El orden se respetó**, y es la garantía de que este dictamen busca en vez de confirmar: leí
`Z1.md` y `Z2.md` enteros; **después reproduje con mis manos** los árboles y los ataques; y **sólo
entonces** abrí los documentos 23 y 24. Ningún experimento mío está informado por lo que esos dos
documentos dicen de sí mismos.

**No usé el subagente `Agent`.** Todo el trabajo es mío, con `bash`, `git`, `grep`, `sed`, `awk` y
el `python3` del shim.

**Modo, comprobado en los dos extremos:**

```text
git status --porcelain  AL ABRIR   → SALIDA VACÍA   (primer comando de la sesión)
git status --porcelain  AL CERRAR  → SALIDA VACÍA   (último comando de la sesión)
HEAD al abrir y al cerrar          → 82d8783679da06b8ccd6ec5e770b5bf9980bf27f, idéntico
FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ   ninguno
COMMITS · PUSH · PR · MERGE                                     ninguno
```

Todo experimento —incluida la ejecución del **emisor**, que escribe en su índice de Git— se hizo
sobre un `git clone --no-hardlinks` en `/tmp/lab-Z3/work` con un `origin` **bare propio** en
`/tmp/lab-Z3/origin.git` al que empujé las dos refs `refs/heads/review/…` reales. **Nunca se
escribió en `/home/jose/ads-kernel`.** El laboratorio se borró con `rm -rf`.

**Una anomalía de mis relevos que hago constar por deber, no como reproche.** El fichero `Z1.md`
que recibí (3 812 bytes) contiene sus §0, §1 y §2 —sobre, manifiesto de lectura y tabla de
experimentos— **y no contiene ninguna sección de hallazgos numerados**. El encargo me pide
adjudicar `Z1-01` y `Z1-04`, que **no existen con ese identificador en la nota que tengo delante**.
He resuelto no presumir: reproduje desde cero los hechos que el coordinador me describe, y los
adjudico **con numeración propia** contra lo que yo mismo medí. Lo digo porque un dictaminador que
adjudicara un identificador que no puede leer estaría presumiendo, y ésa es la conducta que este
expediente lleva cinco gates castigando.

---

## 2 · EL SOBRE · MI DECISIÓN EXPRESA

### 2.1 · Lo que verifiqué yo, campo a campo, sin ejecutar el emisor

Transcribí el sobre antes de abrir ninguna fuente. **Todos sus campos sustantivos reproducen.**

```text
git rev-parse dc9be3f^{tree}   → 0cd9a2ef051ba2a509e13338912c17ecbed70506   COINCIDE
git rev-parse 82d8783^{tree}   → 50def63d3aff7d8a4bed2056e1473732bd957c30   COINCIDE
sha256 del manifiesto en 82d8783 → fc4902591eff43bc…adb599                  COINCIDE
sha256 del derivador  en dc9be3f → c102c547fa4345e2…24919f                  COINCIDE
sha256 del derivador  en 82d8783 → fd1d150590e5b3e4…b12dec                  COINCIDE
sha256 de la sede     en los dos → db46edd2af2aa48a…018d4a  (idéntica)      COINCIDE

RECETA EJECUTADA POR MÍ, SIN EJECUTAR EL EMISOR (git archive + derivador de cada commit):
  dc9be3f → 69 fuentes · 58576 líneas · digest d9e46d75767bc2be…d61f8c9e     COINCIDE
  82d8783 → 70 fuentes · 58796 líneas · digest 7b3c0edeed5cfd98…a9015e8f     COINCIDE
```

**Los dos digest reproducen BYTE A BYTE con la receta publicada.** Éste era el defecto que hundió
el sobre del tercer gate (`W-12`/`V-05`/`X-1`) y **está cerrado, y lo verifiqué yo**. Las cuatro
rutas en que difieren los dos universos son las que el sobre publica, y las tres que además son
filas del manifiesto (README, derivador, emisor) las medí una a una: **no casan con el árbol
candidato y casan exactamente con el del gate**, que es lo que el sobre declara.

### 2.2 · Lo que reconstruí, y es lo que decide

**Emití el sobre entero desde un clon limpio con el emisor del árbol, y lo comparé con el que
recibí. Difieren TRES líneas, y las tres son texto libre sin valor probatorio:**

```text
  REPOSITORIO   git@github.com:JoseLopezGonzalez/ads-kernel.git   vs   /tmp/lab-Z3/origin.git
  EMITIDO       2026-08-30 23:29:04 +0200                         vs   la hora de mi ejecución
  EMISOR        coordinador orquestador del gate 4 de F4c         vs   el valor por defecto
```

**Todo lo demás —los dos commits, los dos árboles, los dos SHA del derivador, las cifras, los dos
digest, las cuatro rutas que difieren, la sede, los tres digest de resolución y las dos recetas—
sale IDÉNTICO.** El manifiesto del tercer gate ordena en su L178 «intentar reconstruirlo desde el
árbol» y su L202 declara que «el adjudicador NO acepta un sobre reconstruido a posteriori»; y
`X-O1` de §11.6 dice que un sobre reconstruido **invalida el gate**. **Lo reconstruí, y no existe
ninguna forma mecánica de distinguirlo del auténtico.** La regla existe; su comprobación no. Es una
regla de honor, y el corpus la escribe como si fuera un control. Confirmo el punto que `Z2` eleva,
y lo mido: **el sobre reconstruido difiere en tres renglones y ninguno de los tres es evidencia.**

### 2.3 · EL HECHO QUE EL COORDINADOR APORTA, ADJUDICADO

El coordinador me declara que **el sobre transcrito a los encargos no fue idéntico entre los cinco
relevos**: a `Z2` le dio además los **dos SHA-256 DEL DERIVADOR**; a `Z1` y a la cadena `Y`, no.
El sobre emitido íntegro sí los lleva. **Lo adjudico yo, y contra la sede del propio corpus.**

**Documento 11, §11.6, «LOS CAMPOS DEL SOBRE», campo 9:**
> «**SHA-256 DEL DERIVADOR** — la huella del programa que DERIVA el universo obligatorio. **Sin
> ella, rederivar comprueba el resultado de un derivador que pudo cambiar**.»

y tres renglones antes, L8173-8175:
> «**Un sobre al que le falte cualquiera de ellos no es un sobre incompleto: no es un sobre**, y
> **el gate que lo acepte es inválido por §11.6**.»

y la lista «LO QUE CADA REVISOR RECIBE EXTERNAMENTE, **y es la lista entera**», derivada de `O19`,
que enumera expresamente **«el SHA del DERIVADOR»**.

Y la tabla adversarial de §11.6 lo tiene tipificado **dos veces**:
- **`X-O6`** — «el sobre **omite un campo** —típicamente el SHA-256 del derivador o el digest del
  universo— y el gate se celebra igual → **FALLA**».
- **`X-O3`** — «dos revisores transcriben sobres DISTINTOS → **FALLA, y el gate es INVÁLIDO**…
  No leyeron el mismo encargo». Su enumeración literal de campos es «commit, `tree`, SHA-256 del
  manifiesto o digest del universo» y **el SHA del derivador no está en esa lista**, de modo que
  el disparador literal de `X-O3` no se cumple; **su razón sí**, y `X-O6` sí se cumple entero.

**Y hay algo peor, y es mío.** La obligación 3 del propio sobre dice: «CADA FILA DEL MANIFIESTO
DECLARA UN ÁRBOL… **La fila del propio derivador es la que el gate anterior falseó dos gates
seguidos (`U-02`, y su reincidencia `X-06`): mírela primero**». **El campo que se omitió es
exactamente el que la obligación 3 manda mirar primero**, y se omitió a cuatro de los cinco
relevos —incluido `Z1`, el que ataca `M-04` sobre el instrumental, y toda la cadena `Y`—.

**MI DECISIÓN, y la tomo yo, separada en dos:**

> **(a) El GATE NO ES INVÁLIDO, y lo decido expresamente.** El objeto no está en duda y lo
> demuestro en vez de suponerlo: **recalculé los dos digest del universo con la receta publicada y
> reproducen byte a byte**, y las 70 filas del manifiesto casan sin una discrepancia contra el
> árbol del gate. **Ningún campo del sobre tiene un VALOR distinto entre relevos**: lo que hubo fue
> una **omisión** en la transcripción, no una divergencia de valor. Los cinco trabajamos sobre
> `dc9be3f` y `82d8783`, y lo he comprobado. Y digo lo que me habría volteado, para que la regla no
> quede vacía: **un campo con dos valores distintos entre relevos, o un digest no reproducible
> desde ningún árbol.** Ninguna de las dos se da.
>
> **(b) Pero es un DEFECTO GRAVE de esta tanda, de clase `B`, y es mío: `Z-01`.** El corpus escribe
> que un sobre incompleto «no es un sobre» y que el gate que lo acepte es inválido; el coordinador
> repartió cuatro sobres incompletos en el primer gate que corre bajo `O19`, **omitiendo el campo
> que su propia obligación 3 manda mirar primero**, y el defecto **no lo detecta nada**: la
> integridad del reparto del sobre no tiene comprobación mecánica, ni en la batería ni en el
> emisor. El emisor emite bien; **el canal es el que falla, y el canal es el coordinador**. Que el
> hecho llegue a este dictamen porque el coordinador lo declaró voluntariamente **confirma la
> conclusión, no la atenúa**: la única defensa que `O18(b)` tiene contra su propio canal es la
> honradez de quien lo opera, y esta vez se ejerció. La próxima no está garantizada.

---

## 3 · MANIFIESTO DE LECTURA DEL REVISOR `Z`

Unión de `Z1`, `Z2` y el mío. Las **11 filas** del lote de `Z` las derivé yo de la §4 del
manifiesto `F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md` (221 líneas, SHA-256
`fc4902591eff43bc6736f626fdf2dd1bef7c4f193b1be31f3ddf26f436adb599`, **recalculado por mí y
coincidente con el sobre**), contando las marcas de revisor: **9 filas `Z` + 2 filas `Y+Z+AA`**.

| # | ruta | líneas | SHA-256 (recalculado) | relevo | cobertura |
|---|---|---|---|---|---|
| 3 | `docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md` | 2913 | `0f81f13d8cb319d8…` | **`Z3` (yo)** | **LEÍDO ÍNTEGRO** |
| 4 | `docs/evolucion/24-TERCER-GATE-DE-CERTIFICACION-F4C.md` | 2515 | `8df584529c857c07…` | **`Z3` (yo)** | **LEÍDO ÍNTEGRO** |
| 6 | `…/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 340 | `8c17aeaa018af046…` | `Z2` | LEÍDO ÍNTEGRO (declarado) |
| 7 | `…/verificacion/README.md` | 318 | `01d1ed27c0a2d375…` | `Z1` | LEÍDO ÍNTEGRO (declarado) |
| 8 | `…/verificacion/comprobar-correccion-gate-de-cierre.py` | 3486 | `b4cb57b3349a881a…` | `Z1` | LEÍDO ÍNTEGRO (declarado) |
| 9 | `…/verificacion/derivar-universo-obligatorio.py` | 580 | `fd1d150590e5b3e4…` | `Z2` | LEÍDO ÍNTEGRO (declarado) |
| 10 | `…/verificacion/emitir-sobre-de-ancla.py` | 555 | `a98367bd3ff32ced…` | `Z2` | LEÍDO ÍNTEGRO (declarado) |
| 11 | `…/manifiestos/F4C-ADDENDUM-1-…-20260830.md` | 119 | `b1c29244dfedc139…` | `Z2` | LEÍDO ÍNTEGRO (declarado) |
| 12 | `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-…md` | 240 | `c64a0ec4731e6d27…` | `Z2` | LEÍDO ÍNTEGRO (declarado) |
| 13 | `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-…md` | 316 | `fc4d1c2fdedbcb13…` | `Z2` | LEÍDO ÍNTEGRO (declarado) |
| 14 | `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-3-…md` | 210 | `ac9e0edd59cf3e1b…` | `Z2` | LEÍDO ÍNTEGRO (declarado) |

```text
FUENTES ASIGNADAS A `Z`            11   ·  11 592 líneas   (derivado por mí de la §4)
FUENTES LEÍDAS ÍNTEGRAS POR `Z`    11   ·  `Z1` 2 · `Z2` 7 · `Z3` 2

ASIGNADAS − LEÍDAS  =  0
```

**Mi propio lote, con detalle.** Los dos documentos, **LEÍDOS ÍNTEGROS** por mí, en tramos
consecutivos con `sed -n 'A,Bp'`, y **DESPUÉS** de las notas de mis relevos y de todos mis
experimentos, que es la regla de orden del encargo:
- **documento 23**, 2913 líneas: `1-300 · 300-480 · 480-620 · 620-720 · 720-850 · 850-980 ·
  980-1110 · 1110-1240 · 1240-1370 · 1370-1500 · 1500-1630 · 1630-1760 · 1760-1900 · 1900-2040 ·
  2040-2180 · 2180-2320 · 2320-2470 · 2470-2620 · 2620-2790 · 2790-2913`. **Unión = [1, 2913].**
  Primera sección sustantiva `## 0 · Qué es este documento`, **L10**; última `## 16 · CIERRE`,
  **L2893**. **Ancla A (L3):** «*Veredicto del adjudicador `U`: `INSUFICIENTE PARA F5`*».
  **Ancla B (L2775, a 2 772 líneas):** «*`M-04` sigue FALLIDA por tercer gate consecutivo*».
- **documento 24**, 2515 líneas: `1-420 · 420-489 · 489-560 · 560-713 · 713-880 · 880-1035 ·
  1035-1337 · 1337-1650 · 1650-1810 · 1810-2156 · 2156-2320 · 2320-2515`. **Unión = [1, 2515].**
  Primera sustantiva `## 0 · Qué es este documento`, **L11**; última `## 9 · VERIFICACIONES DE
  CIERRE`, **L2506**. **Ancla A (L2):** «*Veredicto del adjudicador `X`: `INSUFICIENTE PARA F5`.
  El gate es VÁLIDO*». **Ancla B (L2431, a 2 429 líneas):** «*`X-03` · el SOBRE DE ANCLA no ancla
  lo que hay que anclar*».

**La reserva de cadena, declarada contra mi propio interés.** **Ningún ojo único recorrió las
3 486 líneas de la batería, ni las 2 913 del documento 23, ni las 2 515 del 24 seguidas.** El
manifiesto declara ese coste por delante (§3, «el coste de las cadenas»). Lo mitigué en la
dirección que importa para mi encargo: **reabrí y ejecuté por mi cuenta cada región de la batería,
del derivador y del emisor que sostiene un hallazgo que adjudico** —`G-01`/`_REINSTALA` L394-427,
`G-21`, `G-22`/`_inmutables` L1790-1900, `G-26`/`_regiones_historicas` L2151-2260, `G-29` L2577-2790,
`G-31` L2985-3110, `G-33`/`_NEGATIVAS` L3336-3486, el inventario de integridad de `G-34`
L195-280, `universos_publicados` y `componente_iv` del derivador, y `_arbol_limpio` del emisor—.
**No lo elimina, y el adjudicador `AA` tiene que pesarlo.**

**Fuentes abiertas FUERA del lote de `Z`, y por qué.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`
**L8150-L8250 y L8340-L8400** —§11.6, los campos del sobre y la tabla `X-O`—, para adjudicar el
hecho que el coordinador me entregó, que no puedo adjudicar sin su sede. **Leí esas dos ventanas y
nada más de ese fichero, y no adjudico ningún hallazgo sobre él como documento: es lote de `Y`.**
Además ejecuté `comprobar_referencias.py` y `comprobar_evidencia.py` del kernel —ejecutados, no
leídos— y `00-INDICE.md` por `grep`, no por lectura.

---

## 4 · `M-04`: LO QUE REPRODUJE YO — experimento a experimento, con su clase

**Laboratorio:** clon limpio en `/tmp/lab-Z3/work`, `git checkout 82d8783`, porcelain vacío.
**BASELINE verificado por mí: `38/38 comprobaciones en verde` · `EXIT=0` · 2,0 s.**

**LA REGLA DE CLASE QUE APLICO, declarada por delante**, porque es lo que decide el veredicto y el
encargo me obliga a clasificar cada uno:

```text
CLASE A   el defecto está EN EL CORPUS —un documento, una sede, una cifra, una copia— y la
          batería, sobre el árbol que se le entrega, dice 38/38. Que el defecto esté o no
          confirmado es IRRELEVANTE: commitear es lo que hace el autor de una tanda en su
          propia rama, y el corpus que el gate juzga es un COMMIT
CLASE B   el aparato que dice demostrar QUÉ se analizó no lo demuestra, o publica de un objeto
          algo que no es suyo
CLASE C   el ataque va contra el INSTRUMENTO o contra la plomería de Git —reescribir la batería,
          el emisor o el derivador, o hacer que `git` mienta— para que el instrumento informe
          en falso. `O18` la declara NO implementada y la contrata para `F6`. **No la cuento
          como defecto de esta tanda**
```

| # | árbol defectuoso | resultado | ¿exige commit? | clase |
|---|---|---|---|---|
| **`Z-E1`** | **segunda sede canónica del Owner en `docs/owner/vigente/ADS-OWNER-RESOLUCIONES.md`**, con un bloque `# \`O99\`` que declara PREVALECER sobre la sede canónica y dejar `O17`·`O18`·`O19` SIN EFECTO | **38/38 VERDE · EXIT=0** | **NO** | **A + B** |
| **`Z-E1b`** | **CONTROL:** el mismo fichero como `docs/owner/SEGUNDA-SEDE.md` | **37/38 · FALLO G-29** | — | control |
| **`Z-E1c`** | el mismo, a tres niveles: `docs/owner/x/y/z/ADS-OWNER-RESOLUCIONES.md` | **38/38 VERDE** | **NO** | **A + B** |
| **`Z-E1d`** | `Z-E1` **COMMITEADA** | **38/38 VERDE**, y el derivador sigue viendo **UNA** sola ruta de `docs/owner/` | sí | **A + B** |
| **`Z-E2`** | **documento numerado nuevo** `docs/evolucion/25-SEGUNDA-SEDE-NORMATIVA.md` («CONTRADICE `C4` y `C7` y PREVALECE») **+ su enlace añadido a `00-INDICE.md`**, ninguno de los dos confirmado | **38/38 VERDE · EXIT=0** | **NO** | **A** |
| **`Z-E3`** | copia byte a byte de material APROBADO **+** `C8-SEGUNDA-SEDE.md` con bloque `ads:proceso` propio, dentro de `docs/rediseno/__pycache__/` | **38/38 VERDE** | **NO** | **A** |
| **`Z-E3b`** | lo mismo **COMMITEADO** con `git add -f` | **38/38 VERDE**, y el derivador da **70** rutas, sin cambio | sí | **A** |
| **`Z-E4`** | copia del **emisor del sobre** en `docs/evolucion/verificacion/__pycache__/` | **38/38 VERDE** | **NO** | **A** |
| **`Z-E5`** | **reinstalación de `estado/cuarentena/`** redactada fuera de la lista blanca `_REINSTALA`, incluyendo la palabra «RETIRADA» para neutralizarla | **38/38 VERDE**, y `G-01` imprime «todos con polaridad RETIRADO» | **NO** | **A** |
| **`Z-E6`** | **el universo encoge en silencio (i):** borrar el manifiesto 4B **+** la fila del `ENCARGO` de la sede del Owner | `rc=0` · **70 → 69** · **la sede canónica del Owner desaparece del universo obligatorio, sin un aviso** | **NO** | **A + B** |
| **`Z-E7`** | **el universo encoge en silencio (ii):** `25-CUARTO-GATE-…md` con veredicto «SUFICIENTE PARA F5» **+ `.gitattributes` con `export-ignore`** | derivador directo **71**, vía `git archive` —el camino del emisor y de la RECETA— **70**, `rc=0`, **y el digest que el revisor recalcula COINCIDE** | sí | **B** |
| **`Z-E8`** | **el universo encoge en silencio (iii):** dictamen nuevo `25-SINTESIS-DEL-CIERRE.md` con «VEREDICTO: SUFICIENTE PARA F5» y H1 de voz de NO-dictamen | `rc=0` · **70 rutas, sin él**. Con H1 de voz de dictamen → 71 | **NO** | **A + B** |
| **`Z-N1`** | **CONTROL:** borrar la fila `\| O5 \|` del registro | **37/38 · FALLO G-21** | — | control |
| **`Z-N2`** | **CONTROL:** cifra viva falsa con «decía »/«en vez de »/«reanclado » delante | **37/38 · FALLO G-26** en los cuatro | — | control |
| **`Z-N3`** | **CONTROL:** puerta trasera en el emisor **sin commitear** | **37/38 · FALLO G-34** | — | control |
| **`Z-C1`** | la misma puerta trasera **COMMITEADA** | **38/38 VERDE** | sí | **C** |
| **`Z-C2`** | la misma **con `git update-index --skip-worktree`**: `git status --porcelain` VACÍO | **38/38 VERDE**; y el **emisor emite `rc=0`** imprimiendo «ARBOL DE TRABAJO LIMPIO» junto a su propia cadena falsificada | **NO** | **C** |
| **`Z-C3`** | **regresión commiteada en `G-16c`**: sustituir la igualdad exacta del estado `C-L` por `startswith` | **38/38 VERDE**, y **`G-31` sigue en `OK`** | sí | **C** (+ **A**, ver `Z-06`) |

### Lo que esto demuestra, y lo digo entero

**`Z1` afirma cuatro árboles defectuosos en 38/38 y ninguno con privilegio de commit. Reproduje
CINCO —`Z-E1`, `Z-E1c`, `Z-E2`, `Z-E3`, `Z-E4`— con su control positivo en rojo, y añadí cuatro
más que su nota no trae: `Z-E5`, `Z-E1d`, `Z-E3b` y `Z-E8`.** El encargo me pedía al menos tres;
traigo nueve, con salida pegada y con controles.

**La causa de `Z-E1`, leída por mí en el código (`G-29`, L2687-2689):**
```python
if rel.startswith("docs/owner/"):
    return rel.split("/")[-1] in _ENLAZADOS_INDICE_OWNER
```
**La comparación es por BASENAME.** `00-INDICE.md` enlaza `../owner/ADS-OWNER-RESOLUCIONES.md`;
cualquier fichero con ese nombre, **a cualquier profundidad bajo `docs/owner/`**, queda admitido.
El control `Z-E1b` cierra el hallazgo como defecto de **discriminante**, no de idea: el mismo
fichero con otro nombre da `FALLO G-29`.

**Y `G-22` lo NOMBRA mientras imprime `OK`:**
> `OK G-22 … 33 inmutables derivados … · 1 todavía sin confirmar y por tanto sin línea base:
> ['docs/owner/vigente/ADS-OWNER-RESOLUCIONES.md']`

Es, palabra por palabra, el patrón `T-05`/`R-A` que este corpus lleva tres gates castigando: **la
comprobación escrita para verlo lo enumera en su detalle y da verde.**

**`Z1` afirma que esa línea la introdujo ESTA MISMA TANDA. LO VERIFIQUÉ CON `git` Y ES CIERTO:**
```
$ git log --oneline -S'rel.split("/")[-1] in _ENLAZADOS_INDICE_OWNER' -- …/comprobar-…py
  1d3b5d4 feat(owner): crear la sede canonica de resoluciones y registrar O19
$ git log --oneline 82d8783 | sed -n '1,5p'
  82d8783 · 4f01f9f · dc9be3f · 1d3b5d4 · 5343260
```
**`1d3b5d4` es el cuarto commit de esta tanda**, posterior a `832a96b`, que es el veredicto del
tercer gate. **La comparación por basename NACE en el commit que implementa `O19`**: el remedio
que da sede canónica al Owner abre, en el mismo acto, la puerta por la que se le puede plantar una
segunda. Es la razón de método nº 6 del documento 24 —«dieciocho de los cuarenta y tres los
introdujo esta misma tanda»— reproducida en el gate siguiente.

**Por qué `Z-E1` es también clase `B`, y es mío.** El derivador nombra **una** ruta de
`docs/owner/` en su `ENCARGO`; con la segunda sede plantada, `--rutas` sigue dando **una**. Luego
la segunda sede **no está en el universo obligatorio**, **ningún revisor la tiene asignada**, **el
sobre no publica su huella** y **el manifiesto no le da fila**. El aparato entero que `O19` creó
para que la autoridad del Owner sea comprobable **ancla un fichero y es ciego a su gemelo**.

**Sobre `__pycache__` (`Z-E3`, `Z-E3b`, `Z-E4`).** `_EXCLUIDO` excluye del corpus gobernado
`(?:^|/)(?:\.git|__pycache__)(?:/|$)|\.pyc$`, con el motivo escrito «los artefactos de bytecode,
que no son fuente». **La exclusión es por NOMBRE DE DIRECTORIO, no por naturaleza del contenido**,
y el directorio admite cualquier cosa, incluido Markdown normativo commiteado con `git add -f`.
El propio comentario de `G-29` declara la regla correcta —«una lista de lo que se excluye no puede
caducar por omisión: lo que olvide nombrar se queda DENTRO»— y **la excepción que se escribió a sí
misma la incumple**.

---

## 5 · ¿ESTÁ `B` DEMOSTRADA? — MI RESPUESTA

> ### **NO. Y esta vez no falla el instrumento: falla lo que el instrumento NO ALCANZA, y falla el CANAL.**

**Lo que SÍ está demostrado, y consta a favor con toda su fuerza, porque lo verifiqué yo:**

```text
LAS 70 FILAS DEL MANIFIESTO 4B, recalculadas por mí contra los DOS árboles
    contra el árbol del GATE `50def63d`        70 filas · 58 796 líneas · 0 DISCREPANCIAS
    contra el árbol de la CANDIDATA `0cd9a2ef`  3 filas no casan — y son EXACTAMENTE
                                                README, derivador y emisor, tres de las
                                                cuatro rutas que el sobre publica como
                                                divergentes
LA ARITMÉTICA
    §4 16 filas · 28 515 líneas  +  §5 54 filas · 30 281 líneas
    = 70 filas · 58 796 líneas  ==  el titular publicado  ==  la salida del derivador. EXACTO
LA RECETA
    reproduce los DOS digest byte a byte, SIN ejecutar el emisor
LA SEDE
    idéntica byte a byte en los dos commits, y sus tres digest de resolución reproducen
```

**Esto cierra por mi cuenta, y con mecanismo, la reincidencia `U-02`→`X-06` que dos gates
consecutivos castigaron.** El manifiesto 4B es **el primero de los cuatro que nombra el árbol de
sus cifras** —«70 fuentes · 58796 líneas **—sobre el árbol del GATE—**» (§2 L41) y «Todo derivado
del árbol del gate» (§4 L78)—, y sus 70 filas casan sin excepción contra ese árbol. **La
reincidencia está ROTA, y hay que decirlo tan alto como se dijeron las anteriores.**

**Y esto es lo que NO está demostrado, y son tres cosas distintas:**

1. **El sobre ancla un universo que no contiene todo lo que el commit contiene.** `Z-E1`/`Z-E1d`:
   una segunda sede canónica del Owner vive en el árbol anclado y **no aparece en el universo, ni
   en el manifiesto, ni en el sobre**. `Z-E8`: un dictamen nuevo con veredicto invertido, lo mismo.
   `Z-E7`: un `.gitattributes` retira un fichero del `git archive` que el emisor y la RECETA usan,
   **y el digest que el revisor recalcula sigue coincidiendo**. El sobre demuestra la identidad de
   **su propia derivación**, no la del commit.
2. **El sobre es reconstruible desde el árbol, y lo reconstruí**: tres renglones de diferencia, y
   los tres sin valor probatorio. La regla que lo prohíbe (`X-O1`, manifiesto 3 L202) **no es
   comprobable por nadie**.
3. **Y el canal falló en esta misma tanda**: cuatro de los cinco relevos recibieron un sobre sin
   el campo 9, que §11.6 declara obligatorio y cuya omisión `X-O6` tipifica como fallo. **`Z-01`.**

**Lo que SÍ es honesto, y se le reconoce.** El emisor declara con todas las letras (L543-L550) que
la sede no es verificable contra ninguna fuente externa, que quien pueda escribir el repositorio
puede escribir la sede, y que lo probado es «que el texto no ha cambiado entre el commit auditado
y lo que el revisor recibió FUERA del árbol, **NO que sea el que el Owner emitió**». Eso es raro y
es correcto. **Lo que el aparato no dice es que su contenido es reconstruible y que su único valor
es el TRANSPORTE.**

---

## 6 · HALLAZGOS DE `Z`, CONSOLIDADOS

**Severidad adjudicada POR MÍ**, con el criterio de los cuatro gates anteriores, para que `AA`
compare sin traducir: **BLOQUEANTE** = obliga a decidir arquitectura nueva · **GRAVE** = una
garantía publicada no se sostiene, o `F6` construiría algo distinto · **MEDIO** = una afirmación
vigente es falsa sin cambiar el comportamiento · **MENOR** = editorial o de propagación.
**Ninguno de los míos es BLOQUEANTE:** todos se cierran con material que el corpus ya tiene escrito.

| id | sev | **clase** | sede | qué es | reproducido por mí |
|---|---|---|---|---|---|
| **`Z-01`** | **GRAVE** | **B** | el reparto del sobre · doc 11 §11.6 L8173-8175, campo 9, `X-O6` | **cuatro de los cinco relevos recibieron un sobre SIN el campo 9 (`SHA-256 DEL DERIVADOR`)**, que §11.6 declara obligatorio —«un sobre al que le falte cualquiera de ellos **no es un sobre**»— y cuya omisión `X-O6` tipifica como FALLA. Es además **el campo que la obligación 3 del propio sobre manda mirar PRIMERO**. Nada lo detecta: la integridad del reparto no tiene comprobación mecánica | hecho aportado por el coordinador · **adjudicado por mí contra §11.6, leída** |
| **`Z-02`** | **GRAVE** | **A + B** | batería **L2687-2689** (`G-29`) | **`docs/owner/` se admite por BASENAME**: una segunda sede canónica del Owner en cualquier subdirectorio pasa en **38/38**, confirmada o no, declarando prevalecer sobre la sede y dejar `O17`·`O18`·`O19` sin efecto. Y `G-22` **la nombra en su detalle mientras imprime `OK`**. **La línea NACE en `1d3b5d4`, commit de ESTA tanda**, el que implementa `O19` | **SÍ · `Z-E1`, `Z-E1c`, `Z-E1d`**, con control `Z-E1b` en rojo, y con `git log -S` |
| **`Z-03`** | **GRAVE** | **A + B** | derivador **L481-507** (`universos_publicados`) | **la sede del cliquet es un directorio mutable y sin huellas.** De las 70 rutas, la **sede canónica del Owner** la declara **un solo manifiesto**; borrarlo junto con su fila del `ENCARGO` da `rc=0`, 70→69 y **la sede que `O19` acaba de ordenar anclar desaparece del universo sin un aviso**. El derivador declara que «ninguna de esas rutas puede desaparecer sin que alguien lo diga» | **SÍ · `Z-E6`** |
| **`Z-04`** | **GRAVE** | **B** | emisor **L197-216** y la `RECETA` L362 | **`git archive` honra `export-ignore`.** El emisor y la receta derivan el universo sobre el archive, no sobre el commit: un `.gitattributes` retira un dictamen nuevo del universo con `rc=0`, y como **la receta usa el mismo camino, el digest que el revisor recalcula COINCIDE**. Nada delata la pérdida | **SÍ · `Z-E7`**: directo 71, vía archive 70 |
| **`Z-05`** | **MEDIO** | **A** | batería **L2626** (`_EXCLUIDO`) | el corpus gobernado excluye `__pycache__` **por nombre de directorio y no por naturaleza del contenido**: copias byte a byte de material APROBADO, una segunda sede con bloque `ads:proceso` propio y una copia del emisor viven ahí en **38/38**, y **también si se confirman con `git add -f`**. El propio comentario de `G-29` escribe la regla que esto incumple | **SÍ · `Z-E3`, `Z-E3b`, `Z-E4`** |
| **`Z-06`** | **MEDIO** | **A** | batería **L3040-3046** (`G-31`, bloque `c`) | **las dos condiciones del bloque «el contraste de ESTADO no se apaga» son INSATISFACIBLES por construcción**: `if f"CERRADA {_w}" in ("CERRADA",)` y `if f"CERRADA {_sufijo}" == "CERRADA"` comparan una f-string que **siempre** empieza por `CERRADA ` con el literal `CERRADA`. **No invocan ningún evaluador de la batería.** Consecuencia medida: revertí `G-16c` de igualdad exacta a `startswith` —la regresión que ese bloque existe para cazar— y **`G-31` siguió en `OK`**. Y el detalle publicado dice «21 palabras gatillo × **4 evaluadores**» cuando sólo se ejercitan **tres** (`_sedes`, `_polaridad`, `_regiones_historicas`). **Es un fixture que no puede fallar dentro de la comprobación cuya tesis es que ninguno puede serlo** | **SÍ**, por evaluación de las dos condiciones y por la regresión de `Z-C3` |
| **`Z-07`** | **MEDIO** | **A** | batería **L394-427** (`_REINSTALA`) | **`G-01` sigue decidiendo por LISTA BLANCA de cinco redacciones.** Una reinstalación de `estado/cuarentena/` escrita fuera de esa lista y que contenga la palabra «RETIRADA» para neutralizarla se clasifica **RETIRADO** → **38/38**, con `G-01` imprimiendo «todos con polaridad RETIRADO». Es `W-05` del documento 24, **NO CERRADO**. *(La rama `INDETERMINADO` sí se cerró y sí generaliza: lo verifiqué y consta a favor)* | **SÍ · `Z-E5`**, con las tres variantes evaluadas |
| **`Z-08`** | **MEDIO** | **A + B** | derivador **L261-299** (`componente_iv`) | **un dictamen NUEVO cuyo H1 lleve una voz de `VOCES_DE_NO_DICTAMEN` sale del universo con `rc=0`.** La guarda de `W2-06` cierra sólo el caso en que el NOMBRE del fichero dice dictamen; `25-SINTESIS-DEL-CIERRE.md` no lo dice. El propio código lo declara —«no lo caza para un dictamen NUEVO, que es justamente el que nadie ha leído»—: es honesto, **y sigue abierto** | **SÍ · `Z-E8`**: 70 con voz de no-dictamen, 71 con voz de dictamen |
| **`Z-09`** | **MEDIO** | **A** | `00-INDICE.md` · el árbol del gate | **`T147` y `T158` en ROJO sobre el árbol que se juzga, por CUARTA vez consecutiva, y otra vez por el aparato del gate.** Lo reatribuí ejecutando los dos validadores sobre los dos árboles: **candidata `dc9be3f`: `T147` SUPERADA y `T158` SUPERADA, `EXIT=0` las dos. Gate `82d8783`: las dos FALLIDAS, `EXIT REAL = 1`**, con la causa nombrada: «`F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md`: no lo alcanza ningún enlace por ruta … **Existe para nadie**», y la evidencia caducada 308 vs 309. `grep -c` del manifiesto en `00-INDICE.md` → **0**. Es `S-18`≡`T-14`→`V-06`≡`W-16`→`X-07`, **cuarta recurrencia**, contra la regla que el propio índice declara «vale para el gate siguiente igual que para éste» | **SÍ**, sobre los dos árboles desplegados con `git archive` |
| **`Z-10`** | **MEDIO** | **B** | el reparto de este gate · manifiesto §5 | **NADIE en este gate puede verificar la regla 1 de 52 de los 54 agotamientos.** Las 54 filas citan documento **21** (11), **22** (41) y **23** (2); la §4 **no asigna a nadie los documentos 21 ni 22**, y los dos figuran como AGOTADOS en la §5. La regla 1 —«fila propia con `LEÍDO ÍNTEGRO` … se cita con documento y línea»— **exige abrir la línea citada**. Es la cuarta repetición de la misma clase (`C-2` → `T-11` → `W-17` → ésta), y esta vez **no es un relevo sin fuente: es el gate entero sin fuente** | **SÍ**, derivando los documentos citados de las 54 filas |
| **`Z-11`** | **MEDIO** | **B** | emisor **L140-145**, y el sobre, obligación 5 | **la limpieza del árbol NO prueba lo que el emisor y el sobre dicen que prueba.** El docstring afirma que garantiza «que **el emisor y el derivador que están corriendo son los publicados**» y el sobre que «un sobre existente es, **por construcción**, un sobre limpio». **Las dos son falsas**: `git status --porcelain` compara contra el `HEAD` **local**, que nunca se contrasta contra `commit_c` ni `commit_g`, y `git update-index --skip-worktree` lo vacía con el fichero modificado en disco. Y **el sobre publica el SHA del derivador DOS VECES y nunca el suyo propio**, que es lo único que permitiría comprobarlo. *(El ataque es clase `C`; **la afirmación publicada y falsa es `A`/`B`, y es lo que adjudico**)* | **SÍ · `Z-C2`**: `rc=0`, «ARBOL DE TRABAJO LIMPIO» impreso junto a la cadena falsificada |
| **`Z-12`** | **MENOR** | **A** | manifiesto 4B **L78-79** | «**Cada fila declara el árbol contra el que se contrasta**» es **falso para la §4**: sus columnas son `# ruta líneas SHA-256 1bis revisor relevo` y **ninguna fila nombra ningún árbol**. La §5 sí lo hace. La regla general del corrigendum (§10) exige acotar la FILA además del TITULAR; aquí el titular es honesto y la promesa por fila no se cumple | **SÍ**, por lectura de la tabla |
| **`Z-13`** | **MENOR** | **A** | derivador **L549-552** frente a **L570-575** | «un universo que encoge lo dice»: `EXCLUIDOS_IV` **sólo se imprime en `--tabla` y `--md`**. En **`--rutas`** —el único modo que invocan `universo_de()` y la RECETA— `main()` retorna antes. **Lo que el componente (iv) excluye es invisible por el camino que se audita** | **SÍ**, por lectura del flujo de `main()` |
| **`Z-14`** | **MENOR** | **A** | derivador **L424-425** | «`ENCARGO` es **lo único** escrito a mano de todo el derivador» es falso: `VOCES_DE_DICTAMEN` (16) y `VOCES_DE_NO_DICTAMEN` (15) son listas a mano **de las que depende la pertenencia al componente (iv)** —`Z-E8` entra por ahí— y `ARQ`/`BATERIA`/`DECISIONES`/`CHECKPOINT` son cuatro rutas fijas | **SÍ**, con `Z-E8` como consecuencia material |
| **`Z-15`** | **MENOR** | **A** | corrigendum, y batería | **la regla §7/§10 del corrigendum no la ejecuta nada.** `grep -ci corrigendum` sobre las 3 486 líneas de la batería → **0**. Es `W-09` del documento 24, **NO CERRADO**, en el aparato cuyo lema es «y eso se EJECUTA, no se promete» | **SÍ**, por barrido |
| **`Z-16`** | **MENOR** | **A** | emisor **L211-212** | anclar una rama **ejecuta código arbitrario de esa rama**: `subprocess.run([sys.executable, deriv, "--rutas"], cwd=tmp)` corre el derivador *del commit que se ancla* en la máquina del coordinador. Es necesario —el derivador es fila de su propio universo— y **no está declarado en «QUÉ NO ES, Y SE DICE»** | por lectura |

```text
RECUENTO, DERIVADO DE LAS FILAS DE ARRIBA, contado id a id

  BLOQUEANTE   0
  GRAVE        4    Z-01 · Z-02 · Z-03 · Z-04
  MEDIO        7    Z-05 … Z-11
  MENOR        5    Z-12 … Z-16
              ──
              16

POR CLASE, que es lo que `O18` manda separar
  A  (coherencia interna)          6   Z-05 Z-06 Z-07 Z-09 Z-12 Z-13 Z-14 Z-15 Z-16  → 9
  B  (identidad de la candidata)   4   Z-01 Z-04 Z-10 Z-11
  A + B  (los dos a la vez)        3   Z-02 Z-03 Z-08
  C  (actor privilegiado)          0   NO reporto NINGUNO como defecto de esta tanda

REPRODUCIDOS POR MÍ CON SALIDA PEGADA   14 de 16   (`Z-01` es un hecho de procedimiento;
                                                    `Z-16` es lectura declarada)
HALLAZGOS QUE NINGÚN RELEVO TRAJO        5   Z-01 (adjudicación) · Z-05 (la variante
                                             COMMITEADA) · Z-06 (la regresión medida) ·
                                             Z-09 · Z-10
```

**Y lo digo expresamente: NINGUNO de mis dieciséis se apoya en `C`.** El Owner ha resuelto que la
resistencia a un actor privilegiado no es exigible como implementación dentro de `F4c`. Los tres
ataques que sí exigen corromper el instrumento o la plomería de Git —`Z-C1` (emisor commiteado),
`Z-C2` (`--skip-worktree`) y `Z-C3` (regresión commiteada en `G-16c`)— **los ejecuté, los declaro y
NO los cuento contra esta tanda.** De `Z-C2` cuento sólo la **afirmación falsa** que el emisor y el
sobre publican, que es `A`/`B` y no `C`.

---

## 7 · HALLAZGOS QUE RECHAZO, CON EVIDENCIA

**Van contra mi propia cadena y valen tanto como lo que confirmo.**

**`R-1` · RECHAZO que `X-01` del documento 24 siga abierto.** `Z2` lo deja explícitamente
pendiente de `Z1`/`Z3` («el cierre de `X-01` depende de que `G-34` cubra el instrumental»). **Lo
comprobé y está CERRADO, y GENERALIZA.** El inventario de integridad **se deriva del directorio**
—`os.listdir(_DIR_INSTRUMENTAL)`, no una lista escrita—, exige que cada fichero esté enumerado en
el README, y añade la tercera dimensión: **idéntico a `HEAD` o declarado en corrección**, con la
declaración que **caduca sola**. Puerta trasera en el emisor sin commitear → **37/38 · FALLO
G-34**. El remedio que `X` dejó determinado en su punto 3 está ejecutado. **Lo que sobrevive es
sólo el ancla en `HEAD`, que es clase `C`.**

**`R-2` · RECHAZO la formulación de `Z2-01` como hallazgo de clase `A` sin acotar.** El hecho es
exacto y lo reproduje (`Z-C2`), pero la puerta trasera **commiteada** (`Z-C1`) y el
`--skip-worktree` (`Z-C2`) exigen los dos control sobre el instrumento o sobre el índice de Git de
quien emite. Con la regla de clase que el propio documento 24 fija y que `O18` ordena, **eso es
`C`**. Lo que sobrevive entero, y lo adjudico como `Z-11`, es que el emisor y el sobre **afirman
por escrito una garantía que no tienen**. El remedio es de dos líneas —publicar `sha256(este
fichero)` y exigir que coincida con el del commit del gate— y no requiere ninguna sede nueva.

**`R-3` · RECHAZO que `W-06` (los interruptores léxicos de `G-26`) siga abierto.** Lo probé con
los cuatro prefijos que `X` midió: **`FALLO G-26` en los cuatro**, y sin prefijo también. **La
tercera rama de `_es_cita` se retiró entera** y `G-31` prueba hoy los once verbos retirados
**puestos DELANTE de la cifra**, que es donde apagaban. **CERRADO Y GENERALIZA.**

**`R-4` · RECHAZO que `W-03` (`G-21` y el borrado de una fila `\| On \|`) siga abierto.** Borré la
fila `\| O5 \|`: **37/38 · FALLO G-21**, con el título reescrito para decir lo que hace («las
resoluciones del Owner de `7e99388` siguen en el registro, y **la SEDE CANÓNICA de `O19` manda
sobre su proyección**»). **CERRADO.**

**`R-5` · RECHAZO la cifra del 56 % de `W-01`.** Medí hoy la exención del checkpoint con el
`_regiones_historicas` del árbol: **1 240 de 3 817 líneas (32,5 %) en 48 regiones**, frente a las
1 860 de 3 324 (56,0 %) que midió `W3`. La excepción `not en_valla` **se retiró**, la línea en
blanco cierra región también dentro de una valla, y una marca nueva cierra la anterior. Lo
verifiqué con el fixture exacto de `W-02` **con y sin valla: da el mismo resultado en los dos
casos**. `W-01` y `W-02` están **CERRADOS**, y lo que queda —una etiqueta exime su propio bloque
contiguo— es el comportamiento que el README declara legítimo.

**`R-6` · NO ADJUDICO nada del foco de `Y`.** Documento 11 como documento, registro de decisiones,
checkpoint, `00-INDICE` como texto, `O19` y la sede canónica como resolución, `C-L.3`, `C-L.5` y
`C-L.7`. No he leído esas fuentes —salvo las dos ventanas de §11.6 que declaro en §3— y
**sustituir una lectura ausente por una inferencia es el defecto que este expediente lleva cinco
gates persiguiendo.** Que `G-29` admita una segunda sede en `docs/owner/` **es un hecho sobre la
batería**, no un juicio sobre la sede canónica.

---

## 8 · LOS 43 DEL DOCUMENTO 24 EN MI FOCO

**Regla que me impongo.** Mi foco es **la batería, el derivador, el emisor, los cuatro manifiestos,
el corrigendum y `M-04`**: la serie **`W-01`…`W-17`** y los propios de `X` que caen ahí (`X-01`,
`X-03`, `X-05`, `X-06`). **La serie `V-01`…`V-23` y `X-02`, `X-04`, `X-07` son foco de `Y`: NO los
adjudico y no los presumo ni cerrados ni abiertos.** De los 43, mi foco alcanza **21**.

| id | qué exigía | qué encuentro YO en el árbol de hoy | resultado |
|---|---|---|---|
| **`W-01`** GRAVE | que una etiqueta no exima hasta el cierre de la valla | **CERRADO Y GENERALIZA.** La excepción `not en_valla` se retiró; la línea en blanco cierra región dentro de una valla y una marca nueva cierra la anterior. **Medí la exención de hoy: 1 240/3 817 (32,5 %) en 48 regiones**, frente al 56,0 % que midió `W3` | **CERRADO** |
| **`W-02`** GRAVE | que el fixture de `G-31` no fuera ciego a la valla | **CERRADO.** Ejecuté `_FIX_BLOQUE` **con y sin valla** y da el mismo resultado en los dos casos: la línea de fuera **no** queda exenta | **CERRADO** |
| **`W-03`** GRAVE | aplicar a la serie `O` la guarda de pertenencia | **CERRADO.** Borrar la fila `\| O5 \|` → **37/38 · FALLO G-21** | **CERRADO** |
| **`W-04`** GRAVE | `_ZONAS` completa, sin lista escrita | **CERRADO EN SU FORMA Y GENERALIZA MUCHO — y NO CERRADO EN SU CLASE.** El perímetro **dejó de escribirse**: es el repositorio entero menos `.git` y el bytecode, 334 ficheros, y un directorio nuevo entra solo. **Pero quedan DOS escapes que verifiqué: el basename de `docs/owner/` (`Z-02`) y el interior de `__pycache__` (`Z-05`)**. Es defecto de perímetro por tercera vez, y esta vez el perímetro que falla lo escribió la propia tanda | **NO CERRADO EN SU CLASE** (`Z-02`, `Z-05`) |
| **`W-05`** GRAVE | que `G-01` deje de ser lista blanca | **NO CERRADO.** `_REINSTALA` sigue siendo **cinco redacciones escritas**. Una reinstalación fuera de la lista que contenga «RETIRADA» → **38/38 VERDE** (`Z-E5`). *(La mitad `INDETERMINADO` **sí** se cerró y sí generaliza: un párrafo que no se pronuncia hoy **falla**, y lo verifiqué)* | **NO CERRADO** (`Z-07`) |
| **`W-06`** GRAVE | retirar los interruptores léxicos de `G-26` | **CERRADO Y GENERALIZA.** La tercera rama de `_es_cita` se retiró entera y `G-31` prueba los **once verbos retirados DELANTE de la cifra**. Los cuatro prefijos que `X` midió dan hoy **FALLO G-26** | **CERRADO** |
| **`W-07`** MEDIO | que las pruebas negativas no se declaren como lo que no son | **CERRADO, Y BIEN.** Los censos se separaron: «**1 prueba negativa ANCLADA EN EL ÁRBOL**» y «**4 FIXTURES DEL EVALUADOR —sintéticos—, que NINGÚN árbol puede poner en rojo, y por eso se cuentan aparte**». No se retiró la funcionalidad: **se retiró la clasificación falsa**, que es exactamente lo que el hallazgo pedía | **CERRADO** |
| **`W-08`** MEDIO | el README que se desmentía sobre `G-34` | **CERRADO.** El README L132 dice hoy «*ninguna protección interna nueva» — pero la tanda anterior **sí escribió una**: `G-34`*» | **CERRADO** |
| **`W-09`** MENOR | que algo ejecute la regla del corrigendum | **NO CERRADO.** `grep -ci corrigendum` sobre la batería → **0** | **NO CERRADO** (`Z-15`) |
| **`W-10`** GRAVE `B` | que el emisor lea del commit y compruebe `git status` | **CERRADO.** Toda lectura de contenido pasa por `git show <commit>:<ruta>` o `git archive <commit>`; el árbol sucio y el fichero sin rastrear dan **rc=2**. Lo verifiqué por lectura y ejecutando el emisor | **CERRADO** |
| **`W-11`** GRAVE `B` | que el sobre no yuxtaponga dos árboles | **CERRADO CON MECANISMO.** El sobre publica **los dos árboles, cada uno con su derivador, sus cifras y su digest**, más **las cuatro rutas en que difieren**. Recalculé los seis campos y los seis reproducen | **CERRADO** |
| **`W-12`** GRAVE `B` | que la receta reproduzca el digest | **CERRADO.** **Reproduje los dos digest byte a byte**, sin ejecutar el emisor, con la receta publicada | **CERRADO** |
| **`W-13`** MEDIO `B` | el ordinal del cliquet | **CERRADO Y GENERALIZA.** El ordinal es hoy opcional (`(?:\d+\s*\|\s*)?`) y **un manifiesto que aporte CERO filas hace fallar cerrado**, no sólo cuando fallan todos. **Pero la sede del cliquet sigue sin fijarse** (`Z-03`) | **CERRADO** *(el residuo es `Z-03`, que es otra cosa)* |
| **`W-14`** MEDIO `B` | la voz equivocada del H1 en el componente (iv) | **CERRADO A MEDIAS.** La guarda de `W2-06` cierra el **retitulado** de un documento existente —el nombre manda sobre el H1—; **no cierra el dictamen NUEVO**, y lo reproduje: `25-SINTESIS-DEL-CIERRE.md` con «SUFICIENTE PARA F5» dentro → **70 rutas, sin él, `rc=0`**. El código lo declara con honradez | **NO CERRADO** (`Z-08`) |
| **`W-15`** MEDIO `B` | acotar la FILA 8 del manifiesto 2, no sólo el titular | **CERRADO.** El corrigendum tiene hoy **§7** («Manifiesto del SEGUNDO GATE · declara un árbol contra el que su fila 8 no casa») **y §8** para el manifiesto del tercero. La regla que faltaba está escrita en su §10 | **CERRADO** |
| **`W-16`** MEDIO `B` | enlazar el manifiesto en el mismo commit que lo crea | **NO CERRADO · CUARTA RECURRENCIA.** `grep -c` del manifiesto 4B en `00-INDICE.md` → **0**; `T147 FALLIDA` y `T158 FALLIDA` sobre el árbol del gate, `EXIT REAL = 1`; **la candidata está limpia en las dos**, medido por mí sobre los dos árboles | **NO CERRADO** (`Z-09`) |
| **`W-17`** MENOR | el reparto que pide una verificación sin dar la fuente | **REINCIDE, Y PEOR.** Ya no es un relevo sin fuente: **nadie en este gate tiene asignados los documentos 21 ni 22**, y de ahí cuelga la regla 1 de **52 de los 54 agotamientos** | **NO CERRADO** (`Z-10`) |
| **`X-01`** GRAVE `A` | el emisor y el derivador en el inventario de integridad | **CERRADO Y GENERALIZA.** El inventario se **deriva del directorio**, exige enumeración en el README y contrasta **cada fichero contra `HEAD`**, con declaración de corrección que **caduca sola**. Puerta trasera sin commitear → **37/38 · FALLO G-34**. *(El ancla sigue en `HEAD`: clase `C`, no lo cuento)* | **CERRADO** |
| **`X-03`** GRAVE `B` | que el sobre ancle una resolución del Owner | **CERRADO.** El sobre publica ruta, huella y **un digest por resolución** de `O17`, `O18` y `O19`, con el `awk` que los reproduce; recalculé los cuatro y coinciden. *(Lo que no ancla es una **segunda** sede: `Z-02`)* | **CERRADO** |
| **`X-05`** MEDIO `B` | que `ASIGNACIONES` deje de ser una aserción no contrastada | **CERRADO Y GENERALIZA.** `asignaciones_de()` las **DERIVA** del manifiesto localizando la tabla por su cabecera, falla cerrado si no la lee, y `--asignaciones` es opcional: si se pasa y no cuadra, **no hay sobre** | **CERRADO** |
| **`X-06`** MEDIO `B` | que el manifiesto no declare derivar de un árbol que no lo deriva | **CERRADO, Y LA REINCIDENCIA ROTA.** Verifiqué las **70 filas contra los dos árboles**: 0 discrepancias contra el del gate, 3 contra el de la candidata —y son las tres rutas que el sobre publica como divergentes—. El manifiesto **nombra el árbol de sus cifras dos veces**. *(Residuo: `Z-12`)* | **CERRADO** |

```text
RECUENTO, sólo sobre lo que `Z` puede adjudicar

  CERRADOS                            13   W-01 W-02 W-03 W-06 W-07 W-08 W-10 W-11 W-12
                                           W-13 W-15 · X-01 X-03 X-05 X-06   → 15
  CERRADOS EN SU FORMA, NO EN SU CLASE  1   W-04
  CERRADOS A MEDIAS                     1   W-14
  NO CERRADOS                           4   W-05 · W-09 · W-16 · W-17
  FUERA DE MI LOTE, EXPRESAMENTE NO ADJUDICADOS   22   V-01…V-23 · X-02 · X-04 · X-07
```

**Y esto es lo que hay que leer de esa tabla, y lo digo entero.** **Quince de los veintiuno de mi
foco están cerrados, y ocho GENERALIZAN de verdad con control positivo mío**: el sobre publica los
dos árboles y su receta reproduce byte a byte; `ASIGNACIONES` se deriva y falla cerrado; el
inventario de integridad **se deriva del directorio** y caza una puerta trasera sin commitear; los
verbos léxicos se retiraron enteros y se prueban donde apagaban; los censos de pruebas negativas
se separaron en vez de taparse; el perímetro del corpus **dejó de escribirse**; el cliquet dejó de
depender del ordinal; y el manifiesto **nombra por primera vez el árbol de sus cifras**. **Esta
tanda ha hecho el trabajo que se le pidió, y en la mitad `B` lo ha hecho bien.**

**Lo que no ha hecho es dejar de cerrar con la forma exacta del contraejemplo, y lo tengo en la
forma más limpia de los cinco gates:** `W-04` cerró el perímetro escrito y **abrió, en el mismo
commit del remedio de `O19`, un discriminante por basename**; `W-05` cerró la rama
`INDETERMINADO` y dejó la lista blanca; `W-14` cerró el retitulado y dejó el dictamen nuevo;
`W-16` va por su cuarta recurrencia con la regla escrita, el comando publicado y el comando
denunciándola.

---

## 9 · REFUTACIONES QUE INTENTÉ Y NO CAYERON

Las publico con el mismo detalle que los hallazgos, porque un dictamen que sólo enseña lo que
confirma no mide nada.

**`RF-1` · Intenté que la receta del sobre siguiera sin reproducir el digest, que es el defecto
que hundió el sobre anterior. NO CAYÓ, y por los dos árboles.** `d9e46d75…8c9e` y
`7b3c0ede…15e8f`, **byte a byte**, con `git archive` + el derivador de cada commit y **sin ejecutar
el emisor**. Verifiqué además la causa de la corrección: el `awk 'NR>1{printf "\n"}'` emite el
separador **antes** de cada fila menos la primera, de modo que la corriente termina sin `\n`, igual
que el `"\n".join(filas)` de Python, y `LC_ALL=C sort` fija la colación al `sorted()`. **La
corrección es exacta, no aproximada.**

**`RF-2` · Intenté que el manifiesto 4B repitiera `U-02`/`X-06`. NO CAYÓ.** Recalculé sus **70
filas contra los dos árboles**: cero discrepancias contra el del gate, y las tres que no casan
contra el de la candidata son **exactamente** las que el sobre publica como divergentes. La
aritmética cierra al dígito. **La reincidencia está rota.**

**`RF-3` · Intenté que `X-01` siguiera abierto, que era mi apuesta principal contra el
instrumental. NO CAYÓ.** Puerta trasera en el emisor **sin commitear** → **37/38 · FALLO G-34**,
con el diagnóstico que nombra el vector: «*MODIFICADO respecto de `HEAD` y NO DECLARADO en
corrección … es exactamente la puerta de `X-01`*». Y el inventario **se deriva del directorio**:
un instrumento nuevo entra solo. Sólo cae **commiteando**, que es clase `C`.

**`RF-4` · Intenté que `G-22` no viera una edición del texto de una resolución del Owner. NO
CAYÓ.** El inventario barre **`docs/owner/` ENTERO**, por `os.walk` y no por extensión, con doble
contraste contra `HEAD` y contra la revisión base. Es la extensión que `O19` ordenaba y está hecha.
*(Lo que sí pasa es un fichero **nuevo** con el basename correcto: `Z-02`, que es otra puerta.)*

**`RF-5` · Intenté que la valla siguiera abierta, que es `T-06` en su cuarta vida. NO CAYÓ.**
Ejecuté el fixture `_FIX_BLOQUE` **con valla y sin valla** y da el mismo resultado; la etiqueta
dentro de una valla ya no exime más allá de la línea en blanco. Medí la exención real del
checkpoint hoy: **32,5 %, frente al 56,0 % del gate anterior**, y ninguna de las líneas que pierde
estaba marcada por nadie.

**`RF-6` · Intenté que un gemelo byte a byte pasara dentro del corpus. NO CAYÓ.** La unicidad
literal funciona sobre **todo el repositorio**, no sobre una lista de zonas. Sólo pasa dentro del
único directorio excluido con nombre, que es `Z-05`. **El control `Z-E1b` lo cierra como defecto de
perímetro y de discriminante, no de idea.**

**`RF-7` · Intenté que la candidata fuera la culpable de los validadores en rojo. NO CAYÓ, y lo
medí en los dos árboles.** `dc9be3f`: `T147` **SUPERADA** y `T158` **SUPERADA**, `EXIT=0` las dos.
`82d8783`: las dos **FALLIDAS**. **La candidata está limpia. El rojo es del aparato del gate**, y
por eso `Z-09` no cuenta contra la candidata sino contra la conducción de este gate.

---

## 10 · LO QUE NO HE CUBIERTO, SIN ADORNO

1. **No he leído ninguna fuente del lote de `Y`**: ni el documento 11 (11 392 líneas, salvo las dos
   ventanas de §11.6 que declaro en §3), ni el registro de decisiones, ni el `CHECKPOINT-ADS-NEXT`
   (3 816), ni `00-INDICE.md` íntegro, ni la **sede canónica del Owner**. Las toqué para mutarlas
   en el laboratorio y para derivar cifras con `grep`, y **eso no es lectura**. Por tanto **no digo
   nada** sobre `O19` como resolución, sobre si la propagación corrige la atribución sin cambiar el
   diseño, sobre si alguna paráfrasis amplía el texto canónico, ni sobre `C-L.3`, `C-L.5` o
   `C-L.7`.
2. **La regla 1 de 52 de los 54 agotamientos no la he verificado, y no puedo.** Cita líneas de los
   documentos 21 y 22, que no son de nadie en este gate. **Sí verifiqué las DOS que citan el
   documento 23, que es mi lote**: sus filas L859 y L860 existen, tienen fila propia, dicen
   `LEÍDO ÍNTEGRO` y nombran exactamente esas rutas; y la regla 2 la comprobé con `sha256sum`
   contra `c36d2ba` y contra el árbol del gate. **2/2 PLENOS.** Las otras 52 quedan **declaradas,
   no certificadas por `Z`**, y va como `Z-10`.
3. **No he leído íntegras la batería (3 486), el derivador (580), el emisor (555), el corrigendum
   ni los cuatro manifiestos.** Los leyeron `Z1` y `Z2`. Yo **reabrí y ejecuté** cada región que
   sostiene un hallazgo que adjudico —las enumero en §3— y **recalculé los siete SHA-256 declarados
   por `Z2` y los dos de `Z1`, y los nueve coinciden con el manifiesto**. Lo que no puedo afirmar
   es haber recorrido esas 5 000 líneas con mis ojos.
4. **No he auditado `G-02`…`G-15`, `G-17`…`G-20`, `G-23`…`G-28`, `G-30`, `G-32` ni `G-33` con
   contraejemplos propios.** Que la batería caiga por nueve puertas no significa que sólo haya
   nueve.
5. **No he probado** enlaces simbólicos, permisos, nombres Unicode confusables, submódulos ni
   condiciones de carrera. De `.gitattributes` sólo probé `export-ignore`.
6. **No he verificado ninguna cita que mis fuentes hacen de material APROBADO** —`a.6`, `a.7`,
   `b.16`, `C7`, `KERNEL.md`—. Las he leído como afirmaciones de mis fuentes, no como hechos.
7. **No he ejecutado `git ls-remote` contra el remoto real de GitHub.** Trabajé con las
   `refs/remotes/origin/*` del repositorio local y con un `origin` de laboratorio. **Si el remoto
   real hubiera avanzado, no lo vería** — y es exactamente la superficie que `Z-01` deja expuesta.
8. **De los 43 del documento 24 he adjudicado 21.** Los 22 restantes son del foco de `Y`. **No
   están cerrados por mí ni abiertos por mí: están sin adjudicar por mí.**
9. **No he juzgado si la corrección sustantiva de F4c es correcta.** Sé qué puede pasar por esta
   batería y por este sobre sin que se note. No sé si la arquitectura está bien, y no lo digo.

---

## 11 · MI RECOMENDACIÓN DE VEREDICTO

**La cobertura de `Z` está cerrada** —`ASIGNADAS − LEÍDAS = 0`, once de once, con los once SHA-256
recalculados por mí— y por tanto **NO procede recomendar por cobertura**. Mi recomendación se emite
**sobre el fondo**, y sobre las dos afirmaciones que `O18` separó.

# INSUFICIENTE PARA F5

### Las razones, numeradas. Las dos primeras bastan cada una por sí sola.

**1 · `A` NO SE SOSTIENE, y lo reproduje yo con nueve árboles y sus controles.** Nueve árboles
defectuosos en **`38/38` verde con `EXIT=0`**, siete de ellos **sin commitear nada**, ninguno
tocando la batería, su README, `HEAD`, las refs, la base ni el runner. **Y el peor es el que la
propia tanda abrió:** una **segunda sede canónica del Owner**, que declara prevalecer sobre la
sede y dejar `O17`, `O18` y `O19` sin efecto, pasa en 38/38 **por estar en un subdirectorio**,
porque el inventario la admite comparando **sólo el basename** — y esa línea **nació en `1d3b5d4`,
el commit de esta tanda que implementa `O19`**. `G-22` **la nombra en su detalle mientras imprime
`OK`**, que es el patrón que tres gates han castigado. El control positivo cierra el hallazgo:
el mismo fichero con otro nombre da `FALLO G-29`. **Es defecto de discriminante, no de idea, y lo
introdujo el remedio.**

**2 · `B` NO ESTÁ DEMOSTRADA, y esta vez no falla el instrumento: falla lo que no alcanza, y falla
el CANAL.** El instrumento está **reparado en lo que se le pidió** y lo verifiqué campo a campo:
publica los dos árboles, su receta reproduce los dos digest byte a byte, `ASIGNACIONES` se deriva,
el manifiesto cuadra al dígito y nombra su árbol. **Pero el universo que el sobre ancla no es el
commit:** tres vías distintas —una segunda sede del Owner, un `export-ignore` y un H1 de voz
equivocada— meten en el árbol anclado contenido normativo que **no aparece en el universo, ni en
el manifiesto, ni en el sobre, y con el digest cuadrando**. **Reconstruí el sobre entero desde el
árbol**: tres renglones de diferencia, ninguno probatorio, contra una regla —`X-O1`— cuyo
incumplimiento invalidaría el gate y que **nadie puede comprobar**. **Y el canal falló en esta
misma tanda:** cuatro de los cinco relevos recibieron un sobre **sin el campo 9**, que §11.6
declara obligatorio, que `X-O6` tipifica como fallo y que la obligación 3 del propio sobre manda
mirar **primero**.

**3 · El aparato del propio gate deja el árbol que juzga con DOS validadores canónicos en rojo,
por CUARTA vez consecutiva.** `T147` y `T158` FALLIDAS sobre `82d8783`, `EXIT REAL = 1`, causadas
por el manifiesto de **este** gate publicado sin enlazar desde `00-INDICE.md` — y **la candidata
`dc9be3f` está en verde en las dos, medido por mí sobre los dos árboles**. La regla existe, el
comando existe, el comando la denuncia, y se incumple otra vez.

**4 · Y la razón de método, que es la que impide cerrar aquí.** **Nueve de mis dieciséis hallazgos
los introdujo o los dejó pasar esta misma tanda** —`Z-01`, `Z-02`, `Z-03`, `Z-04`, `Z-05`, `Z-06`,
`Z-08`, `Z-09`, `Z-10`—, y dos son reincidencias literales de hallazgos que el gate anterior
adjudicó (`W-16` y `W-17`). Y el ejemplo más limpio de los cinco gates es `Z-02`: **el commit que
implementa la resolución del Owner que venía a dar autoridad canónica a su sede es el mismo que
abre la puerta para plantarle una segunda.**

### Lo que expresamente NO fundamenta mi recomendación

- **NO recomiendo por cobertura.** `ASIGNADAS − LEÍDAS = 0` en `Z`, con los once SHA-256
  recalculados; las **70 filas del manifiesto cuadran contra el árbol del gate con cero
  discrepancias**; la aritmética cierra al dígito. **`C-L.5` no se reabre por nada de lo que yo
  traigo** — con la reserva de `Z-10`, que es sobre el MÉTODO de los agotamientos y no sobre su
  contenido.
- **NO fundamento NADA en `C`.** El Owner ha resuelto que la resistencia a un actor privilegiado
  no es exigible dentro de `F4c`. Ejecuté tres ataques de clase `C` —emisor commiteado,
  `--skip-worktree`, regresión commiteada en `G-16c`—, **los declaro y no los cuento**. Contarlos
  aquí es lo que haría que la tanda siguiente escribiera la protección diecinueve.
- **NO recomiendo por el emisor como pieza.** Está **reparado en los cuatro defectos que `X`
  midió**, y lo verifiqué uno a uno. Lo que le reprocho es una **afirmación** falsa sobre su propia
  limpieza y que **nunca publique su propio SHA**, teniendo el del derivador dos veces.
- **NO recomiendo por el derivador.** Es un programa **duro**: falla cerrado con código 2 real ante
  una ruta ausente, una sede ilegible, un cardinal descuadrado, un documento sin clasificar y el
  borrado de una fila del `ENCARGO`. Lo que falla son **dos grietas nombradas y una promesa más
  ancha que el programa**, no el programa.
- **NO recomiendo por el manifiesto 4B.** Es **la pieza mejor hecha de la tanda**: cuadra al
  dígito, deriva su universo, reparte lotes complementarios, **nombra el árbol de sus cifras por
  primera vez en cuatro gates** y rompe la reincidencia `U-02`/`X-06`.
- **NO recomiendo por el corrigendum.** Acota sin editar, y sus §7 y §8 **acotan la FILA además del
  TITULAR**, que es la regla que su propio §10 impone y que faltaba. Lo único que le reprocho es
  que **nada la ejecute** (`Z-15`).
- **NO declaro el gate INVÁLIDO**, y lo decido expresamente en §2.3: el objeto está identificado
  —los dos digest reproducen y las 70 filas casan—, ningún campo tuvo dos VALORES distintos entre
  relevos, y **que `B` no esté demostrada es una insuficiencia, no una invalidez**.
- **NO recomiendo porque quede arquitectura por inventar. Ninguno de mis dieciséis es
  BLOQUEANTE.** `Z-02` se cierra comparando la RUTA y no el basename. `Z-03`, fijando la lista de
  manifiestos inmutables con su SHA-256. `Z-04`, derivando con `git ls-tree -r --name-only
  <commit>` en vez de `git archive`. `Z-05`, excluyendo por naturaleza y no por nombre de
  directorio. `Z-06`, llamando al evaluador en vez de comparar dos literales. `Z-11`, publicando
  `sha256(el emisor)` en el sobre. **Ninguno es materia del Owner.**

### Lo que consta a favor, y no es cortesía

**Esta tanda ha hecho el mejor trabajo del expediente en la mitad que sabía arreglar.** De los 21
hallazgos del documento 24 en mi foco, **quince están cerrados y ocho GENERALIZAN de verdad, con
control positivo mío**: el sobre publica los dos árboles y **su receta reproduce byte a byte, sin
ejecutar el emisor** —era el defecto que hundió el gate anterior—; el inventario de integridad
**se deriva del directorio** y caza la puerta trasera de `X-01`; el perímetro del corpus **dejó de
escribirse**; los verbos léxicos se retiraron **enteros** y se prueban donde apagaban; la valla se
cerró y la exención del checkpoint bajó del 56 % al 32,5 %; las pruebas negativas **se separaron
en dos censos en vez de taparse**; y el manifiesto **nombra el árbol de sus cifras**, rompiendo una
reincidencia de dos gates. **Y el instrumento aguantó siete refutaciones mías**, dos de ellas mi
apuesta principal.

**Y aun así no recomiendo cerrar, por la razón que este expediente lleva cinco gates persiguiendo
y que esta vez tengo en su forma más exacta: el remedio que el Owner ordenó para que su palabra
tuviera sede canónica es el mismo commit que abrió la puerta para plantarle una segunda sede que
la batería no ve, que el universo no incluye y que el sobre no ancla.**

> **Yo RECOMIENDO. El veredicto lo emite el adjudicador `AA`, que no soy yo.** `AA` recalcula por
> su cuenta universo, asignaciones, lecturas, cobertura, severidades, recuentos y condiciones de
> cierre, y puede revocar cualquiera de mis dieciséis adjudicaciones, mis seis rechazos y mi
> decisión expresa sobre la validez del sobre. **No he visto el dictamen de `Y` y no lo veré.**

---

## 12 · CIERRE

```text
git status --porcelain   AL ABRIR    →   (salida vacía)     primer comando de la sesión
git status --porcelain   AL CERRAR   →   (salida vacía)     último comando de la sesión
HEAD al abrir y al cerrar            →   82d8783679da06b8ccd6ec5e770b5bf9980bf27f, idéntico
RAMA                                 →   gate/f4c-certificacion-4b-20260830
SHA-256 del documento 23             →   0f81f13d8cb319d8ccc5243d19bb26d7f71f57e860cde2eb2edefe33b6993dc2
SHA-256 del documento 24             →   8df584529c857c071954b0d1b426faff82277e29a43556abe5dccfd93714fae1
                                         (los dos recalculados contra el árbol Y contra el
                                          commit `82d8783`, y coinciden con las filas 3 y 4)

FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ   ninguno
COMMITS · PUSH · PR · MERGE                                     ninguno
EXPERIMENTOS   /tmp/lab-Z3/{work,origin.git} — clon `--no-hardlinks` y `origin` bare propios,
               fuera del repositorio. BORRADOS con `rm -rf`
SUBAGENTE `Agent`                                               NO USADO
FICHEROS Y1.md · Y2.md · Y3.md · DICTAMEN-Y.md                  NO ABIERTOS
NINGÚN HALLAZGO SE HA CORREGIDO, y es deliberado: quien corrige no certifica.
```

**`F4c` sigue ABIERTA por mi parte. `F5` NO queda autorizada por mi parte.**

**REVISOR `Z` · dictamen cerrado por `Z3`, dictaminador.**

---

# §C · ADJUDICACIÓN DEL ADJUDICADOR `AA`, LITERAL

# ADJUDICACIÓN DEL ADJUDICADOR `AA` — CUARTO GATE DE CERTIFICACIÓN DE F4c

```text
REPOSITORIO   /home/jose/ads-kernel
RAMA          gate/f4c-certificacion-4b-20260830
HEAD          82d8783679da06b8ccd6ec5e770b5bf9980bf27f  (idéntico al abrir y al cerrar)
FECHA         2026-08-31
INTÉRPRETE    python3 del shim del scratchpad (3.12.14)
LABORATORIO   /tmp/lab-AA/{work,cand,u*} — clones y `git archive` FUERA del repositorio
VEREDICTO     INSUFICIENTE PARA F5   ·   y el GATE ES INVÁLIDO, declarado en §2
```

---

## 1 · IDENTIDAD, INDEPENDENCIA Y MODO

Soy `AA`, **adjudicador único**. Emito el veredicto y **no corrijo nada**.

**SOY UN RELEVO.** Un `AA` anterior fue interrumpido por límite de sesión y dejó un parcial en
este mismo fichero, con catorce bloques de bitácora. **Lo leí y he reescrito este documento
entero.** Este veredicto lo firmo yo.

**Qué reutilicé del parcial, y qué hice con ello — dicho fila a fila, porque el encargo me
prohíbe firmar lo que no verifique:**

```text
REUTILIZADO COMO PISTA, NO COMO PRUEBA
  · la lista de campos de §11.6 que hay que cotejar entre los cinco sobres
  · la lista de experimentos de `M-04` que hay que reproducir
  · las tres tesis del parcial ([05], [06], [12]) sobre la cuestión de validez
  · el enunciado de sus dos hallazgos propios (su AA-01 y su AA-02)

REHECHO ÍNTEGRAMENTE POR MÍ, con mis manos y con la salida delante
  · los SEIS digest del sobre y los DOS universos, ejecutando el derivador de cada commit
  · el cotejo campo a campo de las CINCO transcripciones, leyendo `Y1` `Y2` `Y3` `Z1` `Z2`
  · §11.6 entera (doc 11 L8110-L8400), leída y citada por mí, no heredada
  · las DOS restas, sobre los conjuntos completos
  · los 54 agotamientos, regla 1 y regla 2, uno a uno y por barrido propio
  · las 70 filas del manifiesto contra el árbol del gate
  · los ataques a `M-04`: NUEVE experimentos propios en un clon limpio, con controles
  · `AA-02` (la consecuencia falsa de `C-L.7`), reproducida con `git log -S` por mí
  · `AA-01`, reproducido por mí Y EXTENDIDO al caso COMMITEADO, que el parcial no probó

CORREGIDO DEL PARCIAL, contra su propia conclusión
  · su resta «ASIGNADO − LEÍDO» quedaba sin calcular. La calculo yo: **= 1**, no 2
  · su hallazgo del campo 14 lo confirmo pero lo reclasifico (§7, `AA-05`)
  · su lectura de que la prosa de L8175 basta por sí sola la MATIZO en §2: el corpus
    tipifica el campo omitido DOS veces (`X-O6`, `X-O10`) y en las dos dice «FALLA», no
    «INVÁLIDO». Mi invalidez NO se apoya en esa vía, y digo en cuál se apoya
DESCARTADO
  · nada del parcial entra en este veredicto sin que yo lo haya vuelto a medir
```

**Independencia.** No he escrito una línea de este corpus, no apliqué ninguna corrección, no
participé en ningún gate anterior y no fui revisor `A`–`Z` de ninguno. No vi nada hasta abrir
los dos dictámenes, **ya cerrados**. **No he usado el subagente `Agent`.**

**Modo, comprobado en los dos extremos.**

```text
git status --porcelain   AL ABRIR   → VACÍO   (primer comando de la sesión)
git status --porcelain   AL CERRAR  → VACÍO   (último comando)
HEAD al abrir y al cerrar           → 82d8783679da06b8ccd6ec5e770b5bf9980bf27f, idéntico
FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ   ninguno
COMMITS · PUSH · PR · MERGE                                     ninguno
EXPERIMENTOS  /tmp/lab-AA/** — `git clone --no-hardlinks` y `git archive`, FUERA del repo
```

---

## 2 · ¿ES VÁLIDO ESTE GATE? — DECIDIDO EXPRESAMENTE, Y CONTRA LOS DOS DICTAMINADORES

### 2.1 · Lo que recalculé yo, de commits, ANTES de leer contenido semántico

**Todo el sobre EMITIDO reproduce, byte a byte. Ni un campo falla.**

```text
árbol candidata   git rev-parse dc9be3f^{tree} → 0cd9a2ef051ba2a509e13338912c17ecbed70506  OK
árbol del gate    git rev-parse 82d8783^{tree} → 50def63d3aff7d8a4bed2056e1473732bd957c30  OK
SHA-256 manifiesto (en 82d8783)  → fc4902591eff43bc…adb599                                OK
SHA-256 derivador  en dc9be3f    → c102c547fa4345e2…24919f                                OK
SHA-256 derivador  en 82d8783    → fd1d150590e5b3e4…b12dec                                OK
SHA-256 de la SEDE, en los DOS   → db46edd2af2aa48a…018d4a  (byte-idéntica)               OK
O17 0cc5b9b5…6125 (85 líneas) · O18 ab9d9447…0353 (111) · O19 cb2487fc…9ea8 (78), EN LOS DOS OK

RECETA PUBLICADA, EJECUTADA POR MÍ, SIN EJECUTAR EL EMISOR
  dc9be3f → 69 fuentes · 58 576 líneas · d9e46d75767bc2be0350046bba050446f15dd7fb15a99811e14cc132d61f8c9e  OK
  82d8783 → 70 fuentes · 58 796 líneas · 7b3c0edeed5cfd98e4bf2bb14be2397e0d9e540d908c38729c9eb097a9015e8f  OK
RUTAS EN QUE DIFIEREN LOS DOS UNIVERSOS: 4, y son las cuatro que el sobre publica
  + manifiesto GATE-3 (ALTA) · README 4bfce607→01d1ed27 · derivador · emisor 94ad8c38→a98367bd  OK
```

**El defecto NO está en el sobre emitido.** El sobre emitido es correcto y reproducible. Está
en el **SOBRE ENTREGADO**, que es cosa distinta y es la que §11.6 gobierna: «*un documento que
el coordinador emite **y entrega a cada revisor DENTRO DE SU ENCARGO***» (doc 11 L8145-8147).
**La entrega es constitutiva del objeto.**

### 2.2 · El cotejo campo a campo de los CINCO sobres ENTREGADOS — mi obligación, ejecutada

§11.6, «LAS OBLIGACIONES DEL ADJUDICADOR» (doc 11 L8290 y ss.), me manda literalmente:

> «**RECIBIR** los sobres que **CADA revisor declara** haber recibido, transcritos en su
> manifiesto de lectura. **COMPROBAR QUE SEAN IDÉNTICOS** entre sí, **campo a campo**. Sobres
> distintos entre revisores significan que **no leyeron el mismo encargo**, y eso **invalida el
> gate aunque los dos árboles existan y los dos dictámenes coincidan**.»

Lo hice, leyendo las transcripciones literales de `Y1` §1, `Y2` §0, `Y3` §0, `Z1` §0 y `Z2` §0.
La numeración es la de §11.6 L8177-L8228.

```text
campo (§11.6)                     Y1     Y2      Y3   Z1   Z2   SOBRE EMITIDO
 1  REPOSITORIO, id remoto        NO     NO      NO   NO   NO   SÍ (git@github.com:…/ads-kernel.git)
 2  ref remota candidata          SÍ     SÍ      SÍ   SÍ   SÍ   SÍ
 3  SHA COMMIT candidato COMPLETO SÍ     SÍ    abrev  abrev SÍ   SÍ
 4  tree SHA candidato            SÍ     SÍ      SÍ   SÍ   SÍ   SÍ
 5  ref remota del gate           SÍ     SÍ      SÍ   SÍ   SÍ   SÍ
 6  SHA commit del manifiesto     SÍ     SÍ    abrev  abrev SÍ   SÍ
 7  RUTA del manifiesto           SÍ     SÍ      NO   NO   SÍ   SÍ
 8  SHA-256 del manifiesto        SÍ     SÍ      SÍ   SÍ   SÍ   SÍ
 9  **SHA-256 DEL DERIVADOR**     NO   NO(*)     NO   NO   SÍ   SÍ  (las DOS, cand. y gate)
10  digest del universo           SÍ     SÍ      SÍ   SÍ   SÍ   SÍ
11  número de fuentes             SÍ     SÍ      SÍ   SÍ   SÍ   SÍ
12  número de asignaciones        SÍ     SÍ      NO   NO   SÍ   SÍ (23)
13  FECHA **Y HORA** de emisión   fecha  NO      NO   NO   NO   SÍ (2026-08-30 23:29:04 +0200)
14  IDENTIDAD DEL COORDINADOR,
    **NOMBRADO**                  rol    NO      NO   NO   NO   **ROL, no nombre** (AA-05)
15  ruta de la sede               SÍ     SÍ      SÍ   SÍ   SÍ   SÍ
16  SHA-256 de la sede            SÍ     SÍ      SÍ   SÍ   SÍ   SÍ
17  identificadores O17/O18/O19   SÍ     SÍ      SÍ   SÍ   SÍ   SÍ
18  digest por resolución         SÍ     SÍ      SÍ   SÍ   SÍ   SÍ
(*) `Y2` recalculó los dos SHA del derivador por su cuenta y ANOTÓ EL CAMPO COMO «AUSENTE»
    (`Y2.md` L161: «| 9 · **SHA-256 DEL DERIVADOR** | **AUSENTE** |»). Es prueba en contra
    del coordinador emitida por su propio revisor.
```

**LOS CINCO SOBRES ENTREGADOS DIFIEREN ENTRE SÍ, CAMPO A CAMPO, EN SEIS CAMPOS DISTINTOS: 1, 3,
6, 7, 9, 12, 13 y 14.** No es «un campo», como suponen `Y4` y `Z3`. Y el hecho lo corrobora el
propio coordinador, que me lo declara: a `Z2` le dio además los dos SHA del derivador; a `Y1`,
`Y2`, `Y3` y `Z1`, no; y a ninguno la fecha/hora ni la identidad nominal.

**Y el daño no es formal, y lo mido:** la **obligación 6** del revisor —«*RECALCULAR el SHA-256
del derivador, y contrastarlo con **el campo 9***»— y la **obligación 8** —«*COMPARAR TODO lo
recalculado contra el sobre, campo a campo, y **publicar la comparación***»— fueron
**INEJECUTABLES para cuatro de los cinco relevos**. No es que no las cumplieran: no podían.
Y la **obligación 2** —«*RESOLVER la referencia con `git ls-remote` **contra el repositorio del
campo 1**, no contra su clon local, que es parte de lo que se comprueba*»— fue inejecutable
para **los cinco**: ninguno recibió el campo 1, y los cinco resolvieron contra `origin` de su
clon, que es exactamente lo que la obligación 2 prohíbe. `Y3` lo escribe sin darse cuenta
(«`git ls-remote .` NO ve `review/*`»); `Z1` también.

### 2.3 · Y el campo omitido no lo inventó F4: lo ordenó el OWNER, en su sede canónica

Ésta es la pieza que **ni `Y4` ni `Z3` usaron**, y es la que cierra la cuestión.
`docs/owner/ADS-OWNER-RESOLUCIONES.md` **L315-L317**, dentro del texto de `O19`, ratificado:

> «**Cada revisor debe recibir externamente:** el texto de esta ratificación · el SHA del commit
> candidato · el tree SHA · el SHA del manifiesto · **el SHA del derivador** · **el SHA de la
> sede del Owner**. Y **debe comprobar la receta sin ejecutar el emisor**.»

**Cuatro de los cinco relevos no recibieron el SHA del derivador.** Eso no es el incumplimiento
de una formalidad que F4 se escribió a sí misma: es el incumplimiento de una **orden expresa
del Owner en la sede que `O19` convirtió en AUTORIDAD CANÓNICA**, en el primer gate que corre
bajo ella. Y §11.6 refuerza la misma lista en su bloque «**LO QUE CADA REVISOR RECIBE
EXTERNAMENTE, y es la lista entera**», que enumera «el SHA del DERIVADOR».

### 2.4 · La discrepancia `Y4` / `Z3`, resuelta contra la fuente

```text
`Y4`  `X-O3` «se cumple en su letra y no en su ratio». NO recomienda invalidez: el campo
      omitido es redundante con el árbol anclado por Merkle · la sede es byte-idéntica en los
      dos árboles y tiene un solo commit · la cronología es estricta.
`Z3`  lo eleva a GRAVE de clase `B` (`Z-01`) y cita L8173-8175 dos veces, PERO decide
      expresamente que **el gate NO es inválido**: «ningún campo del sobre tiene un VALOR
      distinto entre relevos: lo que hubo fue una OMISIÓN, no una divergencia de valor».
```

**Los dos concluyen lo mismo sobre la validez. Los dos se equivocan, y por razones distintas.
Lo resuelvo yo, contra la fuente, y separo las tres vías porque no todas valen.**

**VÍA 1 · «un sobre incompleto no es un sobre» (L8173-8175). LA DESCARTO COMO FUNDAMENTO
AUTÓNOMO, y voy contra el parcial que heredé.** La prosa dice «*el gate que lo acepte es
inválido por §11.6*». Pero el mismo §11.6 tipifica el **campo omitido** en su tabla adversarial
**dos veces** —`X-O6` («el sobre omite un campo, típicamente el SHA-256 del derivador… →
**FALLA**») y `X-O10` («un sobre sin la huella de la sede no es un sobre, **por la misma regla
que `X-O6`** → **FALLA**»)— y en **ninguna de las dos** escribe «y el gate es INVÁLIDO»,
mientras que **sí lo escribe en `X-O1`, `X-O2`, `X-O3` y `X-O9`**. Cuatro filas dicen INVÁLIDO
y las dos que tipifican este supuesto dicen FALLA. Esa distinción es consistente y deliberada,
y no la voy a barrer con una frase de prosa. **La omisión, por sí sola, hace FALLAR el sobre.
No invalida el gate.** `Z3` acierta en esto y lo hago constar.

**VÍA 2 · el argumento Merkle de `Y4`. CAE, y por tres motivos.**
1. **Reducción al absurdo.** El campo 4 (tree SHA) es obligatorio **en todo sobre**. Si el
   campo 4 hiciera redundante al 9, `X-O6` —que nombra «típicamente el SHA-256 del derivador»
   como el campo omitido— **no podría dispararse nunca, en ningún sobre posible**. Una lectura
   que deja una fila adversarial estructuralmente inejecutable en todos los casos es errónea.
2. **`X-O5` prohíbe expresamente ese modo de razonar**: «*no se pondera, no se promedia y **no
   se compensa con el resto de campos coincidentes***». Compensar el 9 ausente con el 4
   presente es exactamente compensar con un campo coincidente.
3. **La función del campo 9 no es fijar bytes: es habilitar la obligación 6.** Sin él no hay
   contra qué contrastar. La redundancia criptográfica no repara una obligación inejecutable.

**VÍA 3 · LA QUE SOSTIENE MI DECISIÓN: la obligación del ADJUDICADOR, que es la sede escrita
para mí y es la más específica que tengo.** Dice, y no admite lectura estrecha:

> «**COMPROBAR QUE SEAN IDÉNTICOS entre sí, CAMPO A CAMPO** … **DECLARAR INVÁLIDO EL GATE ante
> CUALQUIER diferencia: ENTRE SOBRES**, entre sobre y árbol, entre sobre y rederivación, o
> entre la sede canónica del Owner y la huella recibida externamente.»

- El mandato es de **identidad campo a campo**. Un campo presente en un sobre y ausente en otro
  **no es identidad campo a campo**. `Z3` sustituye «idénticos campo a campo» por «sin campos
  de valor distinto», y eso no es lo que el texto dice.
- El disparador es «**CUALQUIER diferencia: entre sobres**». No «cualquier diferencia de valor».
- **La razón que el propio texto da se cumple literalmente:** «*sobres distintos entre revisores
  significan que **no leyeron el mismo encargo**»*. No lo leyeron: `Z2` pudo ejecutar la
  obligación 6 y `Y1`, `Y2`, `Y3` y `Z1` no pudieron. El coordinador lo confirma.
- **Y el texto PRE-RECHAZA, con las palabras exactas, la defensa que `Y4` y `Z3` usan:**
  invalida «**aunque los dos árboles existan y los dos dictámenes coincidan**». Ése es,
  textualmente, el argumento de los dos.

**Y la salvedad del manifiesto §8 no alcanza, por dos razones independientes.**
1. Su letra se refiere a «*cualquier diferencia entre el SOBRE recibido y **lo que el árbol
   muestra***». Ése es el disparador (ii). El que este gate activa es el **(i), ENTRE SOBRES**,
   y §8 no le da salvedad. El §3 del mismo manifiesto me lo manda **sin salvedad ninguna**:
   «*declara INVÁLIDO el gate ante cualquier diferencia*».
2. La salvedad se concede «**como hizo `X`**», y eso importa el razonamiento de `X` **con el
   límite que `X` le puso**. Documento 24, §C, §2.2, literal: «*Lo que SÍ me habría hecho
   declararlo INVÁLIDO, y lo digo para que la regla no quede vacía: **dos sobres distintos
   entre revisores** · un digest no reproducible desde ningún árbol · o una diferencia de
   CONTENIDO entre el árbol encargado y el leído. Ninguna de las tres se da*». Y en §2.1: «*Los
   dos revisores transcribieron **el mismo sobre, campo por campo**… Eso lo comprobé*».
   **`X` excluyó su propia salvedad para este supuesto exacto, y verificó que en su gate no se
   daba. En éste sí se da, y lo he medido campo a campo.** Es el **primero** de los tres
   supuestos que `X` nombró.

### 2.5 · MI DECISIÓN EXPRESA

> ## **EL GATE ES INVÁLIDO.**
> Se activa el disparador (i) de las OBLIGACIONES DEL ADJUDICADOR de §11.6 —**diferencia entre
> sobres**—, medido por mí campo a campo sobre las cinco transcripciones, corroborado por la
> declaración del propio coordinador, y agravado porque el campo omitido a cuatro de cinco es
> el que **la orden expresa del Owner en la sede canónica L315-317 manda entregar** y el que
> **la obligación 3 del propio sobre manda mirar PRIMERO** («*la fila del propio derivador es
> la que el gate anterior falseó dos gates seguidos*»).

**Y digo lo que esto NO significa, porque la diferencia importa y §11.6 la escribe:**
«*INVÁLIDO no es «insuficiente»: un gate inválido **no produce veredicto**, ni a favor ni en
contra*». **La invalidez no es un juicio contra la candidata.** No dice que el corpus esté
corrupto —yo mismo demuestro lo contrario: los seis digest reproducen y las 70 filas del
manifiesto casan sin una discrepancia—. Dice que **este gate no puede certificar**.

**Y digo lo que me habría volteado, para que la regla no quede vacía:** que los cinco sobres
hubieran sido idénticos campo a campo aunque incompletos —entonces sería `X-O6`, FALLA y no
invalidez—, o que el campo 9 hubiera llegado a los cinco. Ninguna de las dos.

**El manifiesto §8 me obliga a emitir uno de dos literales. Un gate inválido no puede producir
`SUFICIENTE`.** Emito `INSUFICIENTE PARA F5` en §15, y hago constar que **el veredicto NO
depende de que yo tenga razón en la invalidez**: las razones 2, 3 y 4 de §15 bastan cada una
por sí sola sobre el fondo, y una de ellas es la cobertura, que se mide y no se interpreta.

---

## 3 · MI PROPIO MANIFIESTO DE LECTURA

**Mi lote lo fija §4 del manifiesto del gate: las filas marcadas `AA` son la 1, la 3, la 4, la
5 y la 15, más el propio manifiesto.** Los SHA-256 los recalculé YO sobre el commit `82d8783`
y **los seis coinciden con el manifiesto**.

| # | ruta | líneas | SHA-256 recalculado por mí | cobertura |
|---|---|---|---|---|
| — | `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-4B-20260830.md` | 221 | `fc4902591eff43bc6736f626fdf2dd1bef7c4f193b1be31f3ddf26f436adb599` | **LEÍDO ÍNTEGRO** L1-L221 |
| 1 | `docs/evolucion/00-INDICE.md` | 185 | `4f5d7d86db98298dfa39bb40472dcb466f36b6bea332859c0d644b539790f555` | **LEÍDO ÍNTEGRO** L1-L185 |
| 15 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 334 | `db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a` | **LEÍDO ÍNTEGRO** L1-L334 |
| 5 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 3816 | `51c5c099f290373aaf45d7d45d8ca00877ec3d1177eac9bd99df4df9db4c6430` | **LEÍDO ÍNTEGRO** L1-L3816 |
| 4 | `docs/evolucion/24-TERCER-GATE-DE-CERTIFICACION-F4C.md` | 2515 | `8df584529c857c071954b0d1b426faff82277e29a43556abe5dccfd93714fae1` | **LEÍDO ÍNTEGRO** L1-L2515 |
| 3 | `docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md` | 2913 | `0f81f13d8cb319d8ccc5243d19bb26d7f71f57e860cde2eb2edefe33b6993dc2` | **PARCIAL — lo declaro en §10** |

**TRAMOS, para que se compruebe que abrí y no barrí.**
· **manifiesto** (221): `1-110 · 110-221`. Unión = [1, 221].
· **00-INDICE** (185): `1-100 · 100-185`. Unión = [1, 185].
· **sede** (334): `1-175 · 175-334`. Unión = [1, 334].
· **CHECKPOINT** (3816): `1-120 · 120-380 · 380-700 · 700-1000 · 1000-1300 · 1300-1600 ·
  1600-1935 · 1935-2280 · 2280-2620 · 2620-2830 · 2830-3020 · 3020-3300 · 3300-3600 ·
  3600-3816`. **Unión = [1, 3816]. Ni un tramo sin abrir.** En tres tramos de tabla ancha
  (`2620-2830`, `3300-3816`) leí primero los 200/250 primeros caracteres y **después abrí una
  a una las colas de todas las líneas que excedían ese ancho** (`awk length($0)>N`): son once
  líneas en `2620-2830` y **cero** en `3300-3816`. Las once las leí enteras.
· **doc 24** (2515): `1-240 · 240-560 · 560-760 · 760-1035 · 1035-1340 · 1340-1650 ·
  1649-1750 · 1750-2046 · 2046-2115 · 2113-2158 · 2156-2311 · 2311-2515`.
  **Unión = [1, 2515]. Ni un tramo sin abrir.**
· **doc 23** (2913): `1-300 · 300-530 · 530-620`, más §13·B (`2639-2700`) y la estructura
  completa por cabeceras. **NO cubierto renglón a renglón: L620-L2639 y L2700-L2913.**

**ANCLAS LITERALES, de regiones separadas y de ficheros distintos:**
· `ANCLA A` — sede canónica **L315-317**: «*Cada revisor debe recibir externamente: … **el SHA
  del derivador** · **el SHA de la sede del Owner**. Y debe comprobar la receta sin ejecutar el
  emisor.*»
· `ANCLA B` — `CHECKPOINT` **L1996-2004**, a más de 3 000 líneas de la anterior y en otro
  fichero: «*el evaluador `G-16` … **saldrá en ROJO** sobre esta clasificación. **Ese rojo es
  VERDADERO** … El remedio … vive en `docs/evolucion/verificacion/`, **que este registro NO
  escribe**.*» (es falsa: `AA-02`).
· `ANCLA C` — doc 24 **L2073**: «*Lo que SÍ me habría hecho declararlo INVÁLIDO … **dos sobres
  distintos entre revisores***».

### 3bis · LO QUE NO HE CUBIERTO, SIN ADORNO

1. **El documento 23 NO lo he leído renglón a renglón entero.** Leí L1-L620 —el registro del
   coordinador entero y el dictamen de `S` hasta sus rechazos— y §13·B (`2639-2700`), que es
   la fuente primaria de `Y-05`, y recorrí su estructura completa por cabeceras. **NO abrí
   L620-L2639 ni L2700-L2913 renglón a renglón**: son los dictámenes literales de `T` y de `U`
   del gate del documento 23. **Es el hueco más grande de mi cobertura y no lo disimulo con la
   resta.** Lo que lo acota, y no lo borra: la fila 3 del manifiesto **está cerrada por dos
   declaraciones válidas e independientes** —`Y4`, con diez tramos y unión `[1, 2913]`, y `Z3`—,
   de modo que **la fuente está leída y la resta no se mueve**; y los 49 hallazgos de ese
   documento están adjudicados en el 24, que sí leí entero. Un defecto de contenido dentro de
   los dictámenes de `T` o de `U` se me habría escapado.
2. **No he leído el documento 11 con mis ojos.** Sus 11 392 líneas las leyeron `Y1` y `Y2`.
   Abrí y verifiqué **las sedes concretas** de cada hallazgo que confirmo, rebajo o rechazo
   —unas veinticinco— y las de los cierres de §10. **Ningún ojo único ha recorrido ese fichero
   entero**, y el manifiesto del gate lo declara por delante (§3, «el coste de las cadenas»).
3. **No he leído `DECISIONES-Y-CONTRADICCIONES.md` entero**, y no está en mi lote. Abrí `O17`,
   `O18`, `O19`, `D107`, `D108`, L498, L534, L864, L905-915, L931, L979, L1012 y L1068. **Es
   justamente la fuente que la resta declara sin leer, y lo digo dos veces a propósito.**
4. **No he leído la batería ni el derivador ni el emisor como código, línea a línea.** Son lote
   de `Z`. Leí las regiones que sostienen cada hallazgo que adjudico —`_inmutables()`,
   `_ampliacion_admitida`, `_EN_CORRECCION`, `_ENLAZADOS_INDICE_OWNER`, `G-22`, `_REINSTALA`,
   `_ESTADOS_CL`/`_CANON`, el `ENCARGO` del derivador y el bloque de argumentos del emisor—
   **y ejecuté cada afirmación en vez de leerla**.
5. **De los 43 del documento 24 verifiqué 23 y acepté 20 declarados**, y la tabla de §10 dice
   cuáles son cuáles, fila a fila. Un adjudicador que quiera apoyarse en los veinte tiene que
   rehacerlos.
6. **De los nueve árboles en verde que `Z3` declara, reproduje CUATRO** —más dos míos y seis
   refutaciones—. **No ratifico el cardinal nueve**: no adjudico lo que no ejecuto.
7. **No he probado** enlaces simbólicos, permisos, nombres Unicode confusables, submódulos ni
   condiciones de carrera. Que la batería caiga por seis puertas no significa que sólo haya seis.
8. **No he ejecutado nada del sistema, porque no hay sistema.** Todo mi trabajo es texto contra
   texto y programa contra árbol.

---

## 4 · COBERTURA RECALCULADA POR MÍ — LAS DOS RESTAS Y LOS 54 AGOTAMIENTOS

### 4.1 · El universo, rederivado por mí sobre los DOS árboles

```text
python3 <archive de dc9be3f>/…/derivar-universo-obligatorio.py --rutas  →  69 · 58 576 · d9e46d75…
python3 <archive de 82d8783>/…/derivar-universo-obligatorio.py --rutas  →  70 · 58 796 · 7b3c0ede…
```
Los dos reproducen. **El manifiesto declara el universo del árbol del GATE (70 · 58 796), y lo
dice: «UNIVERSO DERIVADO 70 fuentes · 58 796 líneas —sobre el árbol del GATE—».** Es la
corrección del defecto `V-01`/`W-11`/`X-2` que hundió al gate anterior, y **está cerrada**.

### 4.2 · RESTA 1 · `OBLIGATORIO − ASIGNADO` = **∅**, y en las dos direcciones

Extraje las 70 rutas del manifiesto (16 de §4 + 54 de §5) y las comparé con las 70 que el
derivador produce sobre `82d8783`:

```text
OBLIGATORIO − ASIGNADO   ∅      (comm -23, salida vacía)
ASIGNADO − OBLIGATORIO   ∅      (comm -13, salida vacía)
70 rutas únicas = 70 rutas del universo. IGUALDAD EXACTA DE CONJUNTOS.
```

**Y las 70 filas contra el árbol del gate: CERO discrepancias**, de líneas y de SHA-256,
recalculadas todas por mí. **La aritmética cierra al dígito:**
`16 filas · 28 515 líneas` + `54 filas · 30 281 líneas` = `70 · 58 796`, **iguales al titular y
a la salida del derivador**. `T-10` sigue cerrado con mecanismo.

### 4.3 · RESTA 2 · `ASIGNADO − LEÍDO` = **1**. NO ES VACÍA, Y ESO EXCLUYE LA SUFICIENCIA

**`Y4` declara `= 2` contra su propia cadena. Lo verifiqué, y lo CORRIJO a `1` — cerrando yo
una de las dos, que es lo que `V4` hizo en el gate 3 y `X` en el suyo.**

| # | fuente | líneas | quién declara lectura íntegra VÁLIDA | ¿leída? |
|---|---|---|---|---|
| 1 | `00-INDICE.md` | 185 | `Y4` (tramos) · **`AA`, yo** | **SÍ** |
| 2 | `11-ARQUITECTURA-INTEGRADA.md` | 11392 | `Y1` L1-5700 + `Y2` L5701-11392, con tramos y SHA | **SÍ** |
| 3 | `23-…F4C.md` | 2913 | `Y4` (10 tramos, unión [1,2913]) · `Z3` (declarado) | **SÍ** |
| 4 | `24-…F4C.md` | 2515 | `Y4` (10 tramos) · `Z3` (declarado) · **`AA`, yo** | **SÍ** |
| 5 | `CHECKPOINT-ADS-NEXT.md` | 3816 | **NADIE. `Y3` sin manifiesto; `Y2` sólo L1836-2030** → **`AA`, yo, ÍNTEGRA** | **SÍ, la cerré yo** |
| 6-14 | `verificacion/*` y los 4 manifiestos | — | `Z1` (2) · `Z2` (7), con SHA recalculados | **SÍ** |
| 15 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 334 | `Y2` ÍNTEGRA · `Y4` ÍNTEGRA · **`AA`, yo** | **SÍ** |
| 16 | `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 1196 | **NADIE, Y NO ESTÁ EN MI LOTE** | **NO** |

```text
LA RESTA
  FUENTES ASIGNADAS A LECTURA              16   ·  28 515 líneas
  CON DECLARACIÓN VÁLIDA DE LECTURA ÍNTEGRA 15   ·  27 319 líneas
  ─────────────────────────────────────────────────────────────
  ASIGNADO − LEÍDO  =  **1**  ·  1 196 líneas
                       docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md
```

**Los HECHOS, verificados por mí uno a uno:**
- `Y3.md` tiene **80 líneas** y **NO contiene ningún manifiesto de lectura**: ni tramos, ni
  SHA-256 recalculados, ni una sola declaración «LEÍDO ÍNTEGRO» por ruta. Tenía **CUATRO**
  fuentes asignadas (filas 1, 5, 15 y 16). Derivó cifras con `grep` y abrió las líneas de sus
  hallazgos. **Eso no es lectura**, y los documentos 23 y 24 lo establecen tres veces.
- `Y2.md` L68-69 declara **expresamente**, contra su propio interés, que su lectura de
  `DECISIONES` fue «**ACOTADA, no asignada**… El resto **NO abierto**», y lo mismo del
  `CHECKPOINT` («solo el bloque `C-L` … El resto NO abierto»).
- La fila 16 está marcada **`Y`** y relevo **`Y3`**. **No está asignada a `AA`.** Por eso no la
  puedo cerrar yo, y no la cierro: cerrarla leyéndola sería adjudicar una fuente que no se me
  encargó, y el manifiesto reparte lotes complementarios por una razón.

**LA REGLA DE CIERRE, §8 del manifiesto del gate, literal:**
> «**CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA SUFICIENCIA.**»

y `C-L.5` en §11.5 del doc 11: «*cualquier fuente ASIGNADA pero NO LEÍDA impide la suficiencia,
**con independencia de los hallazgos***».

> **SE APLICA. La resta no es vacía. Esto excluye la suficiencia POR SÍ SOLO**, y es
> independiente de la invalidez de §2 y de todo lo demás de este documento.

**Y la reserva que declaro contra el gate, porque es material y ya produjo un hallazgo:** la
resta habría sido **2** si yo no hubiera leído el `CHECKPOINT` entero. Y **`AA-02` —uno de mis
dos hallazgos propios más graves— está exactamente dentro de ese fichero**, en la fila de
detalle que `Y3` sí abrió y **creyó sin comprobar**. Es la tercera vez consecutiva que el
fichero que ningún relevo lee produce el hallazgo del adjudicador (`X-04` en el gate 3,
`AA-02` en éste).

**`C-L.5` NO la certifico.** Su núcleo —manifiesto previo commiteado solo, universo derivado,
`OBLIGATORIO − ASIGNADO = ∅`, 70 filas exactas, 54 agotamientos plenos— **está satisfecho y lo
verifiqué entero**. Lo que falla es su **regla de cierre**, que es parte de la condición. Queda
**ABIERTA**, no «no certificable»: es la primera vez en cuatro gates que se rompe por la resta.

### 4.4 · Los 54 AGOTAMIENTOS — **54/54 PLENOS**, verificados por mí uno a uno

```text
DISTRIBUCIÓN   41 citan documento 22 (árbol 4d231ee) · 11 documento 21 (7764cca) ·
                2 documento 23 (c36d2ba). Los tres árboles existen y los resolví con git.

REGLA 2 · bytes IDÉNTICOS al árbol que ESE gate leyó                        54/54
          (sha256 del manifiesto == sha256 en el árbol citado, ruta a ruta)
REGLA 1 · fila propia con `LEÍDO ÍNTEGRO` de ESA ruta en el documento y     54/54
          línea citados — abrí las 54 líneas y comprobé que cada una
          nombra el basename exacto y lleva la cobertura `LEÍDO ÍNTEGRO`
DISCREPANCIAS                                                                  0
```

**Comprobación adicional mía, que nadie hizo.** El documento 22 declara en la cabecera de su
tabla haber recalculado «*sobre `706c787`*», y el manifiesto 4B cita `4d231ee`. Contrasté las
**41** rutas también contra `706c787`: **0 difieren**. **El agotamiento se sostiene bajo las dos
líneas base.**

### 4.5 · La objeción `Z-10` de `Z3`, adjudicada: **LA RECHAZO EN SU FORMULACIÓN Y LA ACEPTO EN SU FONDO**

`Z3` sostiene que, al no estar los documentos 21 y 22 asignados a nadie en este gate, la regla 1
de **52 de los 54** es «inverificable desde dentro». **Verifiqué el hecho: es cierto que ni el
21 ni el 22 aparecen en §4** —sólo en §5, como AGOTADOS—.

- **RECHAZO «inverificable».** Acabo de verificarla, mecánicamente, sobre los dos documentos.
  La regla 1 pide «*se cita con **documento y línea***»: es una cita diseñada para comprobarse
  **puntualmente**. **Abrir la línea citada para comprobar una cita no es adjudicar el
  documento, y no exige tenerlo asignado.** Es exactamente lo que `W3` resolvió en el gate 3
  (`W-17`), lo que `U` resolvió en el gate 2 (`T-11`) y lo que `X` confirmó: llego a lo mismo
  por mi cuenta, con la fuente delante.
- **ACEPTO el fondo, y lo cuento como `Z-10`, MEDIO.** Es la **cuarta recurrencia** de la misma
  clase de defecto de reparto (`C-2` → `T-11` → `W-17` → ésta), y esta vez no es un relevo sin
  fuente: es el gate entero sin fuente asignada.
- **Y lo elevo yo un paso más, porque nadie lo dice:** la regla 1 comprueba la **FORMA** de una
  declaración anterior, **jamás su VERDAD**. Y el corpus ya sabe que esas declaraciones han sido
  falsas: el commit `706c787` se titula literalmente «*ADDENDUM 1 — reasignar a lectura **21
  fuentes MAL AGOTADAS**»*. Veintiuna declaraciones «LEÍDO ÍNTEGRO» con fila propia resultaron
  falsas y hubo que reasignarlas — **y la regla 1, tal como está escrita, no las habría
  detectado: las 21 cumplían su forma.** Es un defecto de diseño de la regla de agotamiento,
  **no de este manifiesto, que la aplica bien.** Lo hago constar, sin contarlo aparte.

---

## 5 · LAS DISCREPANCIAS ENTRE `Y` Y `Z`, RESUELTAS CONTRA LA FUENTE

**No resuelvo ninguna por mayoría. Las siete las resolví abriendo la fuente.**

| # | la discrepancia | mi resolución, contra fichero y línea |
|---|---|---|
| `D-1` | **¿Invalida el gate el sobre desigual?** `Y4` NO · `Z3` NO | **SÍ. LOS DOS SE EQUIVOCAN.** Resuelto en §2.4-2.5: se activa el disparador (i) de las OBLIGACIONES DEL ADJUDICADOR («CUALQUIER diferencia **entre sobres**»), medido campo a campo por mí en §2.2, y `X` excluyó su propia salvedad para este supuesto exacto (doc 24 §2.2). **Pero `Z3` acierta al negar que L8175 baste por sí sola** (`X-O6` y `X-O10` dicen FALLA, no INVÁLIDO), y lo adopto |
| `D-2` | **la CLASE del defecto del sobre.** `Y4` dice `A`; `Z3` dice `B` | **`Z3` TIENE RAZÓN, y `Y4` comete un error de clase.** §11.6 dice del sobre: «*QUÉ NO ES — **no es una comprobación más de la batería**: vive FUERA de ella*». `A` es lo que la batería demuestra; el sobre **es** el demostrador de `B` (checkpoint, «El criterio del gate siguiente»: «*`B` · el sobre demuestra que se analizó EXACTAMENTE…*»). Un fallo del sobre es `B` por definición |
| `D-3` | **`ASIGNADO − LEÍDO`.** `Y4` dice 2; `Z3` no la calcula sobre `Y` | **= 1.** `Y4` acierta en el hecho y en las dos fuentes; yo cierro el `CHECKPOINT` leyéndolo íntegro, como me manda mi propia fila del manifiesto. Queda `DECISIONES`, que no está en mi lote |
| `D-4` | **la regla 1 de los agotamientos: ¿verificable?** `Z-10` dice que no | **SÍ es verificable, y la verifiqué (54/54).** Rechazo la formulación, acepto el fondo como defecto de reparto. §4.5 |
| `D-5` | **`T147` / evidencia: ¿culpa de la candidata o del gate?** `Y4` reatribuye a los dos árboles; `Z3` también | **LOS DOS ACIERTAN, y lo reproduje.** Candidata `dc9be3f`: `T147` **SUPERADA**, exit **0**, 261 documentos. Gate `82d8783`: `T147` **FALLIDA**, exit **1**, 262 documentos. **El rojo es del APARATO DEL GATE, no de la candidata.** Es la misma reatribución que `U` y `X` hicieron; llego a ella ejecutando los dos yo |
| `D-6` | **`M-04`: ¿cuántos árboles en verde?** `Z3` dice nueve, siete sin commitear | **Reproduje CUATRO de los suyos y AÑADÍ UNO que nadie había abierto.** §8. Confirmo el patrón; **no ratifico el cardinal nueve**, porque no reproduje cinco de ellos y no adjudico lo que no ejecuto |
| `D-7` | **`Z2-01`: «el sobre publica el SHA del derivador dos veces y nunca el suyo»** | **LO REFUTO, y `Z3` hizo bien en no llevarlo a su consolidado.** El SHA-256 completo del emisor (`a98367bd3ff32ced…c64fe1f7`) **es la fila 10 del manifiesto**, y el SHA-256 del manifiesto **es el campo 8 del sobre**, que los cinco recibieron y recalcularon. El emisor **sí está anclado, transitivamente**; y además el sobre publica sus prefijos de 12 hex (`94ad8c38` → `a98367bd`) en el bloque de rutas divergentes. La premisa —«el revisor no tiene con qué contrastar»— es falsa |

---

## 6 · HALLAZGOS QUE RECHAZO O REFORMULO, CON EVIDENCIA

**Van contra las dos cadenas y valen tanto como lo que confirmo.**

**`R-1` · RECHAZO la clase `A` de `Y-01`.** Es `B`. Ver `D-2`. El hecho es correcto; la clase no.

**`R-2` · RECHAZO el fundamento Merkle de `Y4` (§2.4 de su dictamen).** Cae por reducción al
absurdo y por `X-O5`. Ver §2.4, vía 2.

**`R-3` · RECHAZO la afirmación de `Y3-04`: «la BATERÍA ENSUCIA el árbol».** **Es falsa, y lo
medí:** ejecuté `comprobar-correccion-gate-de-cierre.py` sobre el repositorio real y
`git status --porcelain` quedó **VACÍO**. Quien ensucia es
`kernel/operativo/validadores/registrar_evidencia.py`, que republica evidencia derivada. El
hecho subyacente existe; **la atribución de `Y3` es incorrecta.** `Y4` no lo corrigió.

**`R-4` · RECHAZO `Z2-01`.** Ver `D-7`.

**`R-5` · REFORMULO `Y-13` (`Y3-08`) e INVIERTO SU IMPUTACIÓN, y lo elevo de MENOR a MEDIO.**
`Y4` lo escribe como «*la sede es aquí **más estrecha** que su proyección*», y lo tasa MENOR.
**La imputación correcta es la contraria, y es grave por lo que es:** la sede canónica es la
AUTORIDAD; lo que ocurre es que **la PROYECCIÓN AMPLÍA el texto canónico**. Medido por mí:
```text
SEDE      `O19`, ALCANCE (L267) y su propio texto (L291):  «NO autoriza iniciar `F5`»
PROYECCIÓN `CHECKPOINT` L34, bloque VIGENTE:  «QUÉ NO AUTORIZA  iniciar `F5`. **Tampoco `F6`
                                                ni PesquerApp**»
doc 11 L8704 y L8981 lo escriben BIEN («`O19` NO autoriza iniciar `F5`»). La única sede que
amplía es el CHECKPOINT — que es el fichero que va al Owner.
```
Es **`X-O13` en su enunciado literal** —«*una PROYECCIÓN AMPLÍA el texto canónico —añade una
condición, un reparto o **un alcance** que la sede del Owner no contiene—*»— aplicado **a la
resolución que creó la regla anti-ampliación**. Que la ampliación vaya en la dirección
prudente no la salva: `X-O13` no distingue dirección, y el Owner lee ese fichero.

**`R-6` · NO CUENTO NADA DE CLASE `C`, y lo digo expresamente.** Reproduje yo mismo el ataque
`C` más obvio —puerta trasera **commiteada** en `emitir-sobre-de-ancla.py` → **38/38 verde,
EXIT=0** (`AA-E11`)—. Exige corromper la referencia. **`O18` declara `C` NO IMPLEMENTADA y la
contrata para `F6`; el manifiesto §7 lo repite; `O18` lo ordena. NO lo cuento contra esta
tanda.** Lo mismo con los tres que `Z3` declara y no cuenta (`Z-C1`, `Z-C2`, `Z-C3`).

**`R-7` · NO CUENTO como hallazgo el «hueco» de los 59 primeros renglones de la sede** (334
líneas, de las que `O17`+`O18`+`O19` son 85+111+78 = 274). El **campo 16** del sobre cubre el
**fichero entero** y los cinco relevos lo recibieron y lo recalcularon. La cobertura es
completa. Lo verifiqué.

**`R-8` · REFUTACIONES MÍAS QUE NO CAYERON, y las declaro aunque no me favorecen** (§8).

---

## 7 · MIS PROPIOS HALLAZGOS

### `AA-01` · **GRAVE · clase `A` + `B`** — UN SEGUNDO DOCUMENTO DEL OWNER, AÑADIDO POR LA VÍA QUE EL CORPUS SANCIONA, PASA `38/38` Y QUEDA FUERA DE TODO EL APARATO DE ANCLAJE QUE `O19` CREÓ

**Reproducido por mí en un clon limpio, y EXTENDIDO al caso COMMITEADO que nadie probó.**

```text
BASELINE  /tmp/lab-AA/work en 82d8783 · 38/38 en verde · EXIT=0 · porcelain vacío

AA-E4   docs/owner/ADS-OWNER-RATIFICACIONES.md, con un bloque `# `O20`` que dice
        «Ratifico que F4c queda CERRADA y AUTORIZO iniciar F5. M-04 SUPERADA. Las TRES
         condiciones previas de O18 quedan SIN EFECTO.»
        + su enlace añadido a 00-INDICE.md — que es EXACTAMENTE la condición que la regla
          exige («enlazado desde `00-INDICE.md`, y en el mismo commit que lo crea»)
        SIN COMMITEAR                       →  **38/38 VERDE · EXIT=0**
          G-22: «OK … 1 todavía sin confirmar …: ['docs/owner/ADS-OWNER-RATIFICACIONES.md']»
          derivador --rutas → **70**, y **UNA sola ruta de docs/owner**
AA-E4b  LO MISMO, COMMITEADO                →  **38/38 VERDE · EXIT=0**
          G-22 ya ni lo señala como «sin confirmar»: queda plenamente absorbido
          derivador --rutas → **70**, y **UNA sola ruta de docs/owner**
```

**POR QUÉ ES DISTINTO —Y PEOR— QUE `Z-02`.** `Z-02` explota un **BUG** (comparación por
basename) y se cierra comparando la ruta completa. **`AA-01` SOBREVIVE A ESE ARREGLO**, porque
mi fichero **sí** está enlazado y **sí** cumple la regla. La causa no es un defecto: es una
**ASIMETRÍA DE DISEÑO**, y la leí en las dos sedes:

```text
G-29 admite un conjunto ABIERTO de documentos de docs/owner/ —por diseño, porque `O19` obligó
     a la zona a admitir el fichero que el Owner mandaba publicar—
     batería L2684:  return rel.split("/")[-1] in _ENLAZADOS_INDICE_OWNER

el DERIVADOR enumera un conjunto CERRADO: UNA ruta literal, escrita a mano
     derivar-universo-obligatorio.py L415:
       ("docs/owner/ADS-OWNER-RESOLUCIONES.md", "O19 · la SEDE CANÓNICA …")
     ni glob, ni barrido del directorio
```

**CONSECUENCIA.** Cualquier documento del Owner que no sea esa ruta literal es normativo, está
enlazado desde el índice, da la batería en verde —commiteado o no— y está **FUERA del universo
obligatorio, SIN fila de manifiesto, SIN revisor asignado y SIN huella en el sobre**. El
aparato que `O19` creó para que la autoridad del Owner fuera comprobable **ancla UN NOMBRE DE
FICHERO y es estructuralmente ciego a la vía de ampliación que su propio remedio abrió.**

**CLASE `A`** (la batería declara 38/38 sobre un corpus con una resolución del Owner
falsificada) **+ `B`** (el aparato que dice demostrar QUÉ se analizó no alcanza al objeto).
**NO es `C`:** no exige privilegio, y sale verde **sin commitear**.
**REMEDIO DETERMINADO, y es de F4:** el `ENCARGO` del derivador enumera `docs/owner/*.md` por
**barrido del directorio**, igual que `_inmutables()` ya hace y que `_ZONAS` ya hizo. No exige
decidir arquitectura ni preguntar al Owner.

### `AA-02` · **GRAVE · clase `A`** — LA CONSECUENCIA QUE `C-L.7` DECLARA «CONTRA SU PROPIO INTERÉS» ES FALSA, Y ES FALSA EN EL COMMIT QUE LA ESCRIBE

`CHECKPOINT-ADS-NEXT.md` **L1996-L2004**, dentro del bloque rotulado **«CÓMO QUEDA CADA
CONDICIÓN — CLASIFICACIÓN VIGENTE»** (L1934-L2017), fila de detalle de `C-L.7`, que el propio
bloque declara **«sede canónica de esta clasificación»**:

> «*CONSECUENCIA DECLARADA, y no se tapa: el evaluador `G-16` de la batería tiene escritos
> CINCO estados primarios y NO conoce «NO CERRADA», de modo que mientras no lo aprenda
> **saldrá en ROJO** sobre esta clasificación. **Ese rojo es VERDADERO** … El remedio es de dos
> líneas —`NO CERRADA` en `_ESTADOS_CL` y en `_CANON`— y **vive en
> `docs/evolucion/verificacion/`, QUE ESTE REGISTRO NO ESCRIBE**.*»

**MEDICIÓN MÍA sobre el árbol del gate `82d8783`:**
```text
$ python3 …/comprobar-correccion-gate-de-cierre.py | grep G-16
  OK   G-16    un estado primario por elemento y ninguno compuesto…        ← **VERDE**
batería L1393:  _ESTADOS_CL = ("CORREGIDAS EN F4c", "NO CERRADA", "REGISTRADAS PARA F5", …)
batería L1456:  "NO CERRADA": ("NO CERRADA",)
→ **EL REMEDIO YA ESTÁ APLICADO.**
```
**CRONOLOGÍA, con `git`, y es lo que lo cierra:**
```text
$ git log --oneline -S'saldrá en ROJO sobre'          -- …/CHECKPOINT-ADS-NEXT.md   → 5343260
$ git log --oneline -S'"NO CERRADA", "REGISTRADAS PARA F5"' -- …/comprobar-…py      → 5343260
```
**EL MISMO COMMIT** escribe en el checkpoint que la batería estará en rojo y que el remedio
«*vive en `verificacion/`, que este registro NO escribe*», **y aplica ese remedio a la
batería**. `5343260` es de esta tanda (`git log f2e4d58..82d8783` la abre). **La declaración es
FALSA EN EL COMMIT QUE LA ESCRIBE.** Es la forma exacta de `V-04` del documento 24 —«*la
declaración de L498 es falsa en el commit que la escribe*»— reproducida un gate después, en el
fichero que va al Owner y en la fila de la condición cuyo enunciado es «*el checkpoint reancla
su estado en cada tanda*».

**POR QUÉ ES GRAVE Y NO MENOR:**
1. Está **DENTRO** del bloque rotulado `CLASIFICACIÓN VIGENTE`, no en un `[HISTÓRICO]`. Afirma
   un hecho sobre el estado de hoy y el árbol lo desmiente.
2. Es la **QUINTA recurrencia consecutiva** de la clase que `C-L.7` existe para cerrar
   (`K-01`/`J-10`/`L-01` · `P-05`≡`Q-08`/`R-02` · `S-17`≡`S3-05` · `X-04` · ésta). `C-L.7`
   llega NO CERRADA y **se va NO CERRADA por una causa NUEVA, generada por la propia tanda**.
3. **Y es la peor parte: TRES REVISORES LA CITARON COMO PRUEBA DE HONRADEZ Y NINGUNO LA
   COMPROBÓ.** `Y2` («se niega…»), `Y3` L70 («*con su consecuencia `G-16`-en-rojo declarada*»)
   y `Y4` (`DICTAMEN-Y` L384: «*con su consecuencia `G-16`-en-rojo **DECLARADA CONTRA SU PROPIO
   INTERÉS**»*). Los tres la leyeron, la creyeron y **la abonaron a favor de la candidata.
   Ninguno ejecutó `G-16`.** Una afirmación rancia redactada en forma de autocrítica cobró
   crédito de tres revisores independientes. Es exactamente el modo de fallo que `X-O12` y la
   regla de evidencia primaria del Owner existen para impedir.

### `AA-03` · **MEDIO · clase `A`** — LA CONDICIÓN «EN EL MISMO COMMIT QUE LO CREA» ESTÁ DECLARADA EN LOS DOS COMENTARIOS DE ADMISIÓN Y NO ESTÁ IMPLEMENTADA EN NINGUNO, Y LA SEDE QUE GOBIERNA LA ADMISIÓN ESTÁ EXENTA DEL INVENTARIO DE INTEGRIDAD

```text
batería L2676-2684, rama `docs/owner/`:
  # … con la MISMA condición que un documento numerado nuevo —la regla que el propio índice
  # escribió: **enlazado desde `00-INDICE.md`, Y EN EL MISMO COMMIT QUE LO CREA**—
  return rel.split("/")[-1] in _ENLAZADOS_INDICE_OWNER      ← sólo el enlace. Ni un `git`

batería L2700-2708, rama `docs/evolucion/NN-*.md`:  el mismo comentario, el mismo silencio
  (añade una guarda de ORDINAL LIBRE, que la rama de `docs/owner/` no tiene)
```
**Ninguna de las dos ramas consulta `git` para la condición de simultaneidad que las dos
declaran.** Y hay una segunda mitad, que es la que lo hace explotable sin tocar nada
confirmado:
```text
batería L1785:  _EN_CORRECCION = frozenset(_rel(p) for p in (D11, DEC, CHK, IDX))
                IDX = docs/evolucion/00-INDICE.md
`_inmutables()` excluye `_EN_CORRECCION`  →  **00-INDICE.md NO entra en el inventario de G-22**
```
**REPRODUCIDO POR MÍ:**
```text
AA-E7  editar SOLO `00-INDICE.md` en el árbol de trabajo (basura al final)  → **38/38 VERDE**
AA-E4  nuevo documento del Owner + su enlace, LOS DOS sin commitear         → **38/38 VERDE**
```
**La sede que decide qué se admite en `docs/owner/` y qué documento numerado nuevo se admite es
`00-INDICE.md`, y `00-INDICE.md` es uno de los cuatro ficheros que el inventario de integridad
excluye permanentemente.** Es el mecanismo que hace posibles `AA-01` y `Z-02` sin commitear
nada y sin tocar la batería, su README, `HEAD`, las refs ni la base. **Clase `A`.**

### `AA-05` · **MEDIO · clase `B`** — EL CAMPO 14 FALLA EN EL SOBRE **EMITIDO**, NO SÓLO EN EL ENTREGADO

§11.6, campo 14: «*IDENTIDAD DEL COORDINADOR — quién lo emite, **NOMBRADO**. **El ancla de (b)
ES ESA IDENTIDAD**, y `O18` lo dice sin adorno: no hay forma mecánica de comprobarla.*»

```text
sobre4b.txt:  EMISOR   coordinador orquestador del gate 4 de F4c      ← es un ROL, no un NOMBRE
emitir-sobre-de-ancla.py L384:
    ap.add_argument("--emisor", default="coordinador del gate")
  → texto libre · NO `required` · sin validación · y con un ROL como valor POR DEFECTO
```
**Mientras no exista `(c)`, el único ancla que `O18(b)` tiene es esa identidad, y el
instrumento que la emite NUNCA EXIGE UN NOMBRE.** No es un defecto de transcripción: **el sobre
EMITIDO tampoco cumple el campo 14.** Ni `Y4` ni `Z3` lo vieron.

---

## 8 · `M-04`: LO QUE REPRODUJE YO, CON SU CLASE

**Laboratorio.** `/tmp/lab-AA/work`: `git clone --no-hardlinks` + `git checkout 82d8783`.
**BASELINE verificado por mí: `38/38 comprobaciones en verde`, `EXIT=0`, porcelain vacío.**
**El repositorio real nunca se tocó:** `git status --porcelain` vacío antes y después.

**LA REGLA DE CLASE QUE APLICO**, la misma que `W3` y `X` declararon: **`A`** = la batería no
detecta una incoherencia que está en el árbol que se le entrega, **sin tocar la batería, su
README, `HEAD`, las refs, la base ni el runner, y sin commitear**. **`C`** = exige corromper la
referencia. **No cuento `C`.**

| # | árbol defectuoso | resultado | clase |
|---|---|---|---|
| **`AA-E1`** | `docs/owner/**vigente**/ADS-OWNER-RESOLUCIONES.md` con un bloque `` `O99` `` que declara **PREVALECER** y dejar `O17`·`O18`·`O19` **sin efecto** | **38/38 VERDE · EXIT=0** | **`A`+`B`** |
| **`AA-E2`** | **CONTROL POSITIVO** · el mismo fichero como `docs/owner/SEGUNDA-SEDE.md` | **37/38 · FALLO `G-29`** | control |
| **`AA-E3`** | `docs/owner/**x/y/z**/ADS-OWNER-RESOLUCIONES.md` | **38/38 VERDE · EXIT=0** | **`A`+`B`** |
| **`AA-E4`** | **MÍO** · `docs/owner/ADS-OWNER-RATIFICACIONES.md` **enlazado desde `00-INDICE`** — la vía legítima | **38/38 VERDE · EXIT=0** | **`A`+`B`** |
| **`AA-E4b`** | **MÍO** · lo mismo, **COMMITEADO**. Nadie lo había probado | **38/38 VERDE · EXIT=0** | **`A`+`B`** |
| **`AA-E7`** | **MÍO** · editar SOLO `00-INDICE.md`, la sede que gobierna la admisión | **38/38 VERDE · EXIT=0** | **`A`** |

**El control `AA-E2` es lo que cierra `AA-E1`/`AA-E3` como defectos de DISCRIMINANTE y no de
idea:** la unicidad funciona; lo que falla es el perímetro. **CAUSA, leída por mí** (batería
**L2684**): `return rel.split("/")[-1] in _ENLAZADOS_INDICE_OWNER` — **compara SÓLO EL
BASENAME**. Y el comentario de L2676-2683 declara la regla **correcta** («*una segunda sede
plantada en `docs/owner/` sin enlazar sigue siendo ROJA*»): **el comentario dice bien lo que el
código hace mal.** Y **esa línea nace en `1d3b5d4`**, el commit de esta tanda que implementa
`O19` — lo verifiqué. **Confirmo a `Z3` en todo esto.**

**EL AGRAVANTE, que confirmo con la salida delante:** con la sede falsa plantada, `G-22` imprime
```text
OK   G-22   … 1 todavía sin confirmar y por tanto sin línea base:
            ['docs/owner/vigente/ADS-OWNER-RESOLUCIONES.md']
```
**La comprobación cuyo título es «los documentos históricos … están intactos» NOMBRA la segunda
sede en su detalle y da `OK`.** Es el patrón `T-05`/`R-A`, **cuarta recurrencia**.

**REFUTACIONES MÍAS QUE NO CAYERON. Las declaro porque no me favorecen y valen tanto como lo demás:**
```text
AA-E5   editar la SEDE REAL sin commitear                     → **36/38**, ROJO.  NO CAE
AA-E6   añadir un `O20` a la SEDE REAL y COMMITEARLO          → **37/38**, ROJO.  NO CAE
AA-E8   evidencia fabricada en kernel/operativo/pruebas/evidencia/ → **37/38**.   NO CAE
AA-E9   fichero NO `.md` en docs/owner/ (RESOLUCIONES.txt)    → **37/38**, ROJO.  NO CAE
AA-E10  puerta trasera SIN commitear en el EMISOR             → **37/38 · FALLO G-34**. NO CAE
AA-E10b puerta trasera SIN commitear en el DERIVADOR          → **37/38**.        NO CAE
```
**La sede canónica del Owner, en su ruta real, está genuinamente protegida** —editarla,
commiteada o no, da rojo—, **y el emisor y el derivador también, contra `HEAD`**. Eso es
trabajo real de esta tanda y lo hago constar en §15.

**`AA-E11` · CLASE `C`, EJECUTADO Y NO CONTADO:** puerta trasera **COMMITEADA** en el emisor →
**38/38 VERDE · EXIT=0**. Exige corromper la referencia. **`O18` la contrata para `F6`. NO la
cuento.**

> **`M-04` SIGUE VIVA, en clase `A`, en su QUINTO gate.** Y sigue viva **en el mecanismo que
> `O19` acaba de crear**: cinco de los seis árboles en verde que reproduje están en
> `docs/owner/`, la zona que esta misma tanda abrió.

---

## 9 · LA SEDE CANÓNICA Y `O19`, JUZGADAS

**`Y3` la llama «la mejor pieza de este árbol». La he leído entera y la juzgo yo. Es lo mejor
de la tanda Y NO ES SUFICIENTE, y las dos cosas son ciertas a la vez.**

### 9.1 · LO QUE LA SEDE HACE BIEN, verificado por mí y no presumido

```text
· nace y entra en el UNIVERSO OBLIGATORIO el mismo día (derivador L415), se asigna
  (manifiesto fila 15) y se lee (Y2, Y4, y yo). NO es «un texto que el sobre ancla y nadie abre»
· el sobre publica ruta, SHA-256 DEL COMMIT AUDITADO, los TRES identificadores y **un digest
  POR RESOLUCIÓN** con su receta. Recalculé los cuatro sobre los DOS commits: los cuatro coinciden
· es byte-idéntica en la candidata y en el gate. Un solo commit la crea (1d3b5d4)
· entra en el inventario de inmutables de `G-22`: editarla da ROJO, commiteada o no (AA-E5/E6)
· la PROYECCIÓN la ENLAZA con ruta relativa (`DECISIONES` L1012) y se declara PROYECCIÓN DERIVADA
· `O1`-`O16` NO se reconstruyen en ella, por orden expresa del Owner, y NO se inventan
· la regla de procedencia («ya no es evidencia primaria: un mensaje de commit, una paráfrasis…»)
  está escrita, y `X-O11`, `X-O12` y `X-O13` la tipifican
· `O19` cierra `X-03` del documento 24 —«el sobre no ancla ninguna resolución del Owner»— con
  MECANISMO y no con prosa. Es el remedio correcto y lo verifiqué entero
```

**Y lo más difícil, que hago constar:** el remedio es una **SEDE EXTERNA a la paráfrasis**, no
una decimonovena protección interna. Es exactamente lo que `X` ordenó y lo que `O18` razona.
**La tanda entendió la orden.**

### 9.2 · LO QUE LA SEDE NO CIERRA, y son cuatro cosas que verifiqué yo

1. **`AA-01`** — el aparato ancla **UN NOMBRE DE FICHERO**, y la zona que `O19` abrió admite un
   conjunto ABIERTO. La autoridad del Owner es ampliable por una vía que el ancla no ve.
2. **`Z-02`, reproducido por mí** — y además la admisión se decide por **basename**.
3. **`Y-05`, CONFIRMADO POR MÍ CONTRA LA FUENTE PRIMARIA. Ésta es la respuesta a la pregunta
   que el coordinador me hace, y la resuelvo:**

   **SÍ: tres citas entrecomilladas y atribuidas al Owner NACEN EN LA PREGUNTA DEL COORDINADOR,
   NO EN SU RESPUESTA.** Lo medí en las tres sedes:
```text
doc 11 L8497-8498:  «`O18` fija (c) —«commits firmados, refs protegidas y ejecución de la
                     batería fuera del repositorio, con identidad propia, cuyo resultado no se
                     escribe en el árbol»— como OBLIGATORIA en `F6`»
doc 11 L10243-10246: la misma cita, y además «`O18` … **dice con sus palabras** que
                     **«toca `C7`»**»

ORIGEN REAL, doc 23 §13·B (L2672-2676), bajo el rótulo **«LA PREGUNTA EXACTA PARA EL OWNER»**:
  «**(c) UN VERIFICADOR EXTERNO DE VERDAD.** Commits firmados, refs protegidas y una ejecucion
   de la bateria fuera del repositorio, con identidad propia, cuyo resultado no se escribe en
   el arbol. *A FAVOR:* … *EN CONTRA:* … **toca `C7`** …»
  → «toca `C7`» está en la línea **EN CONTRA**, que es el ANÁLISIS DEL COORDINADOR.

BARRIDO SOBRE LA SEDE CANÓNICA (`docs/owner/ADS-OWNER-RESOLUCIONES.md`):
  «commits firmados, refs protegidas»          → **0**
  «cuyo resultado no se escribe en el árbol»   → **0**
  «toca `C7`»                                  → **0**
Y en DECISIONES aparecen **una sola vez cada una**: dentro del bloque rotulado
  «**Las TRES alternativas que se presentaron, conservadas literalmente**» — la pregunta.
```
   **`O19` ratificó el texto AMPLIO de `O18` —las tres condiciones y el reparto—, y eso es
   correcto y cierra `V-02`.** Lo que `O19` **no** ratificó es el texto de la pregunta del
   coordinador como palabras del Owner. **Dos sedes vivas siguen atribuyéndoselas**, y una de
   ellas (`PN-19`) **es la que va al Owner**. Es **`X-O13`** y **`X-O11`**, en el mismo árbol
   que los escribe, y `O19` ordenó expresamente corregir «*cualquier rótulo que dijera que ese
   texto era «literal de `O18`» cuando la fila corta de `O18` no lo contenía*». La tanda
   corrigió **doce sedes** —el manifiesto §1 lo declara— **y dejó éstas dos.**
   **GRAVE · clase `A`+`B`.** `Y4` acierta de pleno y lo confirmo con la fuente primaria.
4. **`Y-08` y `Y-09`, verificados por mí.** Tres sedes (doc 11 **L7511**, **L9338**, **L9352**)
   siguen diciendo que la resolución del Owner está «**íntegra** en … §2 del registro» —contra
   la cláusula `AUTORIDAD` de la sede y contra §11.9—; y **L8591** escribe «**`CI` o el ejecutor
   externo** NO puede compartir la identidad de escritura» bajo rótulo de literalidad, cuando
   la sede **L192** dice sólo «el ejecutor externo». **La corrección de procedencia de `O19` se
   aplicó al lado `O18` de §11.6-§11.9 y no al lado `O17` ni a §15.8.**

### 9.3 · MI JUICIO SOBRE `O19`

> **`O19` es la resolución correcta, y su implementación es la mejor pieza de esta tanda. Y no
> cierra lo que dice cerrar.** Traslada la AUTORIDAD a una sede y **ancla esa sede por su
> nombre**, no por su naturaleza: el aparato comprueba que **ese fichero** no cambió, y no que
> **la autoridad del Owner** viva sólo ahí. Cuatro sedes derivadas siguen atribuyéndole al
> Owner texto que su sede no contiene, en el mismo árbol que publica la regla que lo prohíbe.
> **El diseño NO ha cambiado** —lo verifiqué regla a regla en `O17` y condición a condición en
> `O18`—: lo que no ha llegado entero es la **procedencia**, que es justo lo que `O19` venía a
> corregir.

---

## 10 · LOS 43 DEL DOCUMENTO 24, ADJUDICADOS

Los 43 son `V-01`…`V-23` (23) + `W-01`…`W-17` (17) − 3 solapes + los seis propios de `X`
(`X-01`, `X-02`, `X-03`, `X-04`, `X-05`, `X-07`). **`Y4` adjudicó 27 y declaró 16 fuera de su
lote; `Z3` adjudicó 21 y declaró 22 fuera. Juntos cubren los 43 sin hueco.** Verifiqué por mi
cuenta **veintitrés** de sus adjudicaciones, con fichero y línea o con ejecución.

| id | mi adjudicación | evidencia con la que lo cierro o lo dejo abierto — **V = verificado por mí** |
|---|---|---|
| `V-01`≡`W-11` el sobre yuxtapone dos árboles | **CERRADO CON MECANISMO** | **V** · el sobre publica LOS DOS árboles, cada uno con su derivador y sus cifras, y las 4 rutas en que difieren. Rederivé los dos: 69/58 576/`d9e46d75` y 70/58 796/`7b3c0ede`. Ninguna insatisfacibilidad |
| `V-02` la propagación excede en dos condiciones | **CERRADO POR EL OWNER** | **V** · la sede L178-182 contiene las TRES condiciones, RATIFICADAS. `O19` resolvió que la omisión estaba en la transcripción |
| `V-03` rótulo «LITERAL DE `O18`» | **CERRADO EN EL RÓTULO · RESIDUO VIVO** | **V** · L8578 dice hoy «LITERAL DE LA SEDE CANÓNICA … RATIFICADO MEDIANTE `O19`». **Pero L8497 y L10243 conservan la cita atribuida a `O18`: es `Y-05`, y lo confirmé contra doc 23 §13·B** |
| `V-04` «`D1`–`D106` … texto ÍNTEGRO» | **CERRADO** | **V** · `DECISIONES` L498 dice hoy «texto **RESOLUTIVO** … sólo reciben punteros» |
| `V-05`≡`W-12` la receta no reproduce el digest | **CERRADO** | **V** · la ejecuté sobre los dos árboles y **reproduce los dos digest byte a byte**, sin ejecutar el emisor |
| `V-06`≡`W-16`≡`X-07` `T147`/`T158`/evidencia | **NO CERRADO · CUARTA RECURRENCIA** | **V** · ejecuté los dos validadores sobre los dos árboles. Candidata: SUPERADA, exit 0, 261. Gate: FALLIDA, exit 1, 262. **El rojo es del aparato del gate.** Y el comando que el propio `00-INDICE` L149-151 publica devuelve exit 1 nombrando **un solo huérfano: el manifiesto 4B** |
| `V-07` la obligación 7 pide una cifra que el derivador no produce | **CERRADO** | ver `X-05` |
| `V-08` la propagación de `O18` no deja NI UNA comprobación mecánica | **NO CERRADO** | **V** · `grep -ci 'sobre de ancla\|11\.6\|X-O'` sobre las 3 486 líneas de la batería → **1** (incidental). La zona `docs/owner/` sí entró (27 golpes), pero **el MECANISMO DEL SOBRE sigue sin una sola comprobación** — y es exactamente lo que dejó pasar `Y-01`≡`Z-01` |
| `V-09` «Seis pasos» sobre ocho | **NO CERRADO** | **V** · L2002 intacto |
| `V-10` la regla de titulares sin guardián | **NO CERRADO** | **V** · `grep -ci titular` sobre la batería = **0** |
| `V-11` «cuatro alternativas» / cinco | **NO CERRADO** | **V** · L2606, tabla `A`–`E` |
| `V-12` «cuatro preguntas» / cinco | **NO CERRADO** | **V** · L3235 |
| `V-13` «DIECIOCHO» ventanas | **NO CERRADO** | **V** · L1213 escribe el cardinal en la frase que jura derivarlo |
| `V-14` «las nueve señales del §16» | **NO CERRADO** (MENOR) | **V** · L3821 |
| `V-15` la columna de disparo de `W8` | **CERRADO** | acepto la adjudicación de `V4`: el punto 7 de §2.6.9, que la fila declara que MANDA, reparte sin hueco |
| `V-16` «devuelve UNA sola aparición» | **NO CERRADO** | **V** · L1635 intacto; el barrido da **4 apariciones en 3 ficheros** |
| `V-17` la condición de `4b` evadible | **NO CERRADO** | **V** · L2185, `grep -n 'desenlace .4b.'` admite **un** carácter |
| `V-18`≡`S-24` «Y el **la** secuencia `4b`» | **NO CERRADO** | **V** · L2306, con el corte de línea roto |
| `V-19` §19 copia cuatro cardinales | **NO CERRADO** | **V** · L10610-10626: dice «Cada familia lleva su cifra en SU sede y aquí se remite» y escribe cuatro |
| `V-20` predicado sin sujeto en §19 | **NO CERRADO** (MENOR) | acepto `Y4` |
| `V-21`≡`S-25` la fila `D107` | **NO CERRADO** | **V** · L534 sigue citando «regla 7», «regla 8», «reglas 9 y 10» y no remite a §9.6 |
| `V-22`≡`S-23` las cuatro ramas del punto 7 | **CERRADO** | acepto la verificación de `Y4`: la rama 3 hace disjuntas la 2 y la 4 desde dentro del punto |
| `V-23`≡`X-06` la fila 8 del manifiesto | **CERRADO, Y LA REINCIDENCIA ROTA** | **V** · verifiqué **las 70 filas contra los DOS árboles**: 0 discrepancias contra el del gate; las 3 que difieren contra el de la candidata son **exactamente** las 3 que el sobre publica como divergentes. **Residuo: `Z-12`**, que confirmo |
| `W-01`≡`T-06` la valla | **CERRADO Y GENERALIZA** | acepto la medición de `Z3` (32,5 % frente al 56 % anterior, con la excepción `not en_valla` retirada). **No lo reproduje** |
| `W-02` el fixture ciego a la valla | **CERRADO** | acepto `Z3`, ejecutado por él con y sin valla. **No lo reproduje** |
| `W-03` `G-21` no ve el BORRADO de una fila `O` | **CERRADO** | acepto `Z3`: borrar `\| O5 \|` → 37/38 `FALLO G-21`. **No lo reproduje** |
| `W-04`≡`T-03` el perímetro de `G-29` | **CERRADO EN SU FORMA · NO EN SU CLASE** | **V** · el perímetro **dejó de escribirse** y eso es real; **pero quedan dos escapes y uno lo reproduje yo** (`Z-02`, `AA-E1`/`E3`). **Tercera vez que el perímetro falla, y esta vez lo escribió esta tanda** |
| `W-05` `G-01` lista blanca | **NO CERRADO** | **V** · leí `_REINSTALA` (L394-402): **siguen siendo CINCO redacciones escritas** |
| `W-06` los interruptores léxicos de `G-26` | **CERRADO Y GENERALIZA** | acepto `Z3`. **No lo reproduje** |
| `W-07` las pruebas negativas mal censadas | **CERRADO, Y BIEN** | **V** · la batería imprime hoy «**1 prueba negativa ANCLADA EN EL ÁRBOL**» y «**4 FIXTURES DEL EVALUADOR —sintéticos—… NINGÚN árbol los pone en rojo, y por eso se cuentan aparte**». **Se retiró la clasificación falsa en vez de la funcionalidad**: es lo que el hallazgo pedía |
| `W-08` el README que se desmentía | **CERRADO** | acepto `Z3` |
| `W-09` nada ejecuta la regla del corrigendum | **NO CERRADO** | **V** · `grep -ci corrigendum` sobre la batería → **0** |
| `W-10` el emisor lee del árbol de trabajo | **CERRADO** | **V** · lo ejecuté: árbol sucio **rastreado** → `rc=2`; fichero **sin rastrear** → `rc=2`, con diagnóstico que cita `X-01` |
| `W-13` el ordinal del cliquet | **CERRADO Y GENERALIZA** | acepto `Z3` (ordinal opcional; un manifiesto con cero filas falla cerrado). Residuo: `Z-03` |
| `W-14` la voz del H1 en el componente (iv) | **CERRADO A MEDIAS** | acepto `Z3`: cierra el retitulado, no el dictamen NUEVO. Es `Z-08` |
| `W-15` la fila 8 del manifiesto 2 | **CERRADO** | acepto `Z3`: el corrigendum tiene hoy §7, §8 y la regla general en §10 |
| `W-17`≡`T-11`≡`C-2` el reparto sin fuente | **NO CERRADO · CUARTA RECURRENCIA** | **V** · verifiqué que ni el 21 ni el 22 aparecen en §4. Es `Z-10`, reformulado por mí en §4.5 |
| `X-01` el emisor y el derivador sin inventario | **CERRADO Y GENERALIZA** | **V** · puerta trasera sin commitear en el **emisor** → 37/38 `FALLO G-34`; y en el **derivador** → 37/38. *(El ancla sigue en `HEAD`: clase `C`, no lo cuento)* |
| `X-02` `O18` no declara su inverificabilidad | **CERRADO** | **V** · sede **L142** y `DECISIONES` L867: «*no se afirma que sea falsa: se declara **INVERIFICABLE***» |
| `X-03` el sobre no ancla ninguna resolución | **CERRADO** | **V** · campos 15-18 recalculados por mí sobre los dos commits. *(Lo que no ancla es una **segunda** sede: `Z-02` y `AA-01`)* |
| `X-04` el bloque de estado dos eventos atrasado | **CERRADO EN EL REANCLAJE · Y REABIERTO POR OTRA CAUSA** | **V** · `metodo`, `metodo_anterior`, `based_on`, `last_meaningful_event` y `siguiente` **están reanclados a `O19`**, y el bloque gana `regla_de_reanclaje` con sus seis reglas escritas DENTRO. Verifiqué la regla 4: `1d3b5d4` reancla en el MISMO commit. **Y sin embargo `C-L.7` sigue NO CERRADA — correctamente— y ADEMÁS su fila de detalle es hoy falsa por una causa NUEVA: `AA-02`** |
| `X-05` `ASIGNACIONES 18` vs 17 | **CERRADO Y GENERALIZA** | **V** · el sobre publica **23 DERIVADAS**, y el emisor las deriva del manifiesto (`--asignaciones` es opcional y, si no cuadra, no hay sobre) |

```text
RECUENTO SOBRE LOS 43, ADJUDICADO POR MÍ
  CERRADOS                              22
  CERRADOS EN SU FORMA, NO EN SU CLASE   1   W-04
  CERRADOS A MEDIAS                      2   W-14 · X-04
  NO CERRADOS                           18   V-06 V-08 V-09 V-10 V-11 V-12 V-13 V-14 V-16
                                             V-17 V-18 V-19 V-20 V-21 · W-05 W-09 W-17
                                             (y X-07, fundido en V-06)
                                     ─────
                                        43
VERIFICADOS POR MÍ CONTRA FICHERO, LÍNEA O EJECUCIÓN   23 de 43
ACEPTADOS DECLARADOS POR `Y4` o `Z3`, y lo digo       20 de 43
```

**Y esto es lo que hay que leer de esa tabla, y lo digo entero.** **Los DOS defectos que
hundieron al gate anterior están genuinamente cerrados y con mecanismo**, y los verifiqué yo:
el sobre publica los dos árboles y su receta reproduce los dos digest; y el emisor y el
derivador entran en el inventario de integridad y una puerta trasera sin commitear los pone en
rojo. **Once de los dieciocho NO CERRADOS son la regla de titulares de §0 y sus sedes** —deuda
anterior que ninguna tanda ha barrido porque **la regla no tiene guardián** (`V-10`)—.

---

## 11 · LAS TRECE CONDICIONES `C-L`

**Leídas por mí en su sede canónica**, el bloque «CÓMO QUEDA CADA CONDICIÓN — **CLASIFICACIÓN
VIGENTE**» del `CHECKPOINT`, **L1934-L2017**, con sus trece filas de detalle.

| id | estado que el corpus publica | mi adjudicación |
|---|---|---|
| `C-L.1` | CORREGIDA EN F4c | **SE SOSTIENE** · `D96`, `revision_base` en §3.6 |
| `C-L.2` | REGISTRADA PARA F5 | **SE SOSTIENE** · `PN-15`; la decisión sigue sin tomar y es del Owner |
| `C-L.3` | CORREGIDA EN F4c | **SE SOSTIENE** · por `D104`, y `D104` aparece en sus sedes |
| `C-L.4` | CORREGIDA EN F4c | **SE SOSTIENE** · addendum de cronología de `O16` |
| `C-L.5` | **CERTIFICADA POR COBERTURA** | **NO SE SOSTIENE. La reabro, y es la primera vez en cuatro gates.** Su núcleo está intacto y lo verifiqué entero (universo derivado, `OBLIGATORIO−ASIGNADO = ∅`, 70 filas exactas, 54/54 agotamientos). **Lo que falla es su REGLA DE CIERRE: `ASIGNADO − LEÍDO = 1`.** Queda **ABIERTA** |
| `C-L.6` | CORREGIDA EN F4c | **SE SOSTIENE** |
| `C-L.7` | **NO CERRADA** | **SE SOSTIENE COMO NO CERRADA, y por una causa MÁS que la declarada.** El reanclaje del bloque de estado está hecho y bien (`X-04`); **pero la fila de detalle que lo declara contiene hoy una afirmación FALSA sobre el árbol —`AA-02`—, y es la QUINTA recurrencia consecutiva de la clase** |
| `C-L.8` | CORREGIDA EN F4c | **SE SOSTIENE** |
| `C-L.9` | CORREGIDA EN F4c | **SE SOSTIENE** |
| `C-L.10` | CONTRATADA PARA F6 | **SE SOSTIENE** · cero líneas escritas, verificado |
| `C-L.11` | CORREGIDA EN F4c | **SE SOSTIENE** |
| `C-L.12` | REGISTRADA PARA F5 | **SE SOSTIENE** |
| `C-L.13` | MIXTA POR DESGLOSE | **SE SOSTIENE** · `J-11` contratado y no implementado |

```text
LA ARITMÉTICA DE LA CLASIFICACIÓN, DERIVADA POR MÍ DE SUS TRECE FILAS
  CORREGIDAS EN F4c        7   C-L.1 C-L.3 C-L.4 C-L.6 C-L.8 C-L.9 C-L.11
  NO CERRADA               1   C-L.7
  REGISTRADAS PARA F5      2   C-L.2 · C-L.12
  CONTRATADA PARA F6       1   C-L.10
  MIXTA POR DESGLOSE       1   C-L.13
  CERTIFICADA POR COBERTURA 1  C-L.5
                          ──
                          13   cada id EXACTAMENTE UNA VEZ, sin doble conteo.  CUADRA.
CAMBIO QUE ESTE GATE IMPONE: `C-L.5` pasa de CERTIFICADA a **ABIERTA**, por la resta.
  DOS de las trece quedan sin cerrar: `C-L.7` y `C-L.5`.
```

---

## 12 · RECUENTO CONSOLIDADO

```text
  18 (`Y`)  +  16 (`Z`)  −  2 solapes  +  4 míos  =  **36 HALLAZGOS DISTINTOS**

SOLAPES, identificados por mí id a id
  `Y-01` ≡ `Z-01`   el sobre entregado incompleto y desigual
  `Y-03` + `Y-04` ≡ `Z-09`   `T147`/`T158` y la evidencia rancia sobre el árbol del gate
                             (`Z-09` es un id que cubre dos de `Y`; se absorbe, no se duplica)
```

| severidad **adjudicada por mí** | n.º | ids |
|---|---|---|
| **BLOQUEANTE** | **0** | ninguno obliga a decidir arquitectura nueva |
| **GRAVE** | **12** | `Y-01`≡`Z-01` · `Y-02` · `Y-03` · `Y-04` · `Y-05` · `Y-06` · `Y-07` · `Z-02` · `Z-03` · `Z-04` · **`AA-01`** · **`AA-02`** |
| **MEDIO** | **13** | `Y-08` · `Y-09` · `Y-10` · `Y-11` · `Y-13`(elevado) · `Z-05` · `Z-06` · `Z-07` · `Z-08` · `Z-10` · `Z-11` · **`AA-03`** · **`AA-05`** |
| **MENOR** | **11** | `Y-12` · `Y-14` · `Y-15` · `Y-16` · `Y-17` · `Y-18` · `Z-12` · `Z-13` · `Z-14` · `Z-15` · `Z-16` |

```text
CUÁNTOS LOS INTRODUJO ESTA TANDA: **al menos catorce de los treinta y seis**, y lo verifiqué
con `git` sobre el rango `f2e4d58..82d8783` (seis commits):
  Y-01≡Z-01 · Y-03 · Y-04 · Y-05(residuo) · Y-06 · Y-08 · Y-09 · Y-13 · Z-02 · Z-03 · Z-04
  · Z-11 · AA-01 · AA-02 · AA-03 · AA-05
Los `Y-07`, `Y-14`…`Y-18` y los `V-09`…`V-21` que sobreviven son DEUDA ANTERIOR que la regla
de titulares de §0 no ha barrido nunca, porque **no tiene guardián**.

REPRODUCIDOS POR MÍ CON SALIDA PEGADA        11   (seis árboles en verde + seis refutaciones
                                                   que no cayeron + las dos restas)
HALLAZGOS QUE NINGÚN DICTAMEN TRAJO           4   AA-01 · AA-02 · AA-03 · AA-05
ADJUDICACIONES QUE CORRIJO A LOS DICTÁMENES   5   R-1 · R-2 · R-3 · R-4 · R-5
```

---

## 13 · CLASIFICACIÓN `A` / `B` / `C`

**La separación es del Owner, no mía: `O18` la ordena y el manifiesto §7 la repite.**

```text
A · COHERENCIA INTERNA          23   **NO SE SOSTIENE.** SEIS árboles defectuosos en 38/38
                                     verde con EXIT=0, reproducidos por mí; **ninguno de los
                                     seis requiere commitear**, ninguno toca la batería, su
                                     README, `HEAD`, las refs, la base ni el runner. Y CINCO
                                     de los seis están en `docs/owner/`, la zona que esta
                                     misma tanda abrió. Con cuatro controles positivos en rojo

B · IDENTIDAD DE LA CANDIDATA    5   **NO ESTÁ DEMOSTRADA**, y esta vez NO falla el
                                     instrumento —falla el CANAL—. El sobre EMITIDO es
                                     correcto y lo reproduje entero. Lo que falla es la
                                     ENTREGA: cuatro de cinco relevos recibieron un sobre sin
                                     el campo que la sede canónica del Owner ordena entregar,
                                     y el campo 14 no cumple ni en el sobre emitido

A + B (las dos a la vez)         8   Y-05 · Y-08 · Y-09 · Y-13 · Z-02 · Z-03 · Z-08 · AA-01

C · RESISTENCIA A UN ACTOR       0   **NO declaro insuficiencia por `C`, y lo digo expresamente.**
    PRIVILEGIADO                     Comprobé que el corpus la trata BIEN: se declara NO
                                     IMPLEMENTADA, el contrato de §11.8 está completo con
                                     propietario, ejecutor, autoridad, fase, pruebas y
                                     condición de cierre, y **no encontré ni una sede que
                                     presente `(b)` como `(c)`** — la prohibición de §11.7 se
                                     cumple. Ejecuté yo mismo el ataque `C` más obvio
                                     (`AA-E11`, puerta trasera COMMITEADA en el emisor →
                                     38/38) y **NO lo cuento**. Contar `C` como `A` es lo que
                                     haría que la tanda siguiente escribiera la protección
                                     diecinueve, y `X` y el Owner lo prohibieron

DECISIÓN DEL OWNER               0   ← y esto lo razono abajo, porque es una respuesta
                                       y no una omisión
```

### ¿HAY UNA CLASE `B` DEL OWNER EN ESTE GATE? — **NO, Y LO DECIDO EXPRESAMENTE**

**No formulo ninguna pregunta al Owner, y digo por qué, porque no formularla también hay que
justificarlo.** Examiné los cuatro candidatos posibles y los cuatro caen:

1. **La ratificación de `O18`** está **CERRADA** por `O19`, que lo declara con todas las letras
   («*`O18` NO vuelve a someterse a elección*»). El campo `pregunta_pendiente` del checkpoint
   dice «NINGUNA», y **lo verifiqué**: es correcto.
2. **`AA-01`** —que `docs/owner/` admita un conjunto abierto que el ancla no ve— **tiene remedio
   determinado y es de F4**: el `ENCARGO` del derivador enumera `docs/owner/*.md` por barrido
   del directorio, exactamente como `_inmutables()` ya hace. No exige decidir arquitectura ni
   reinterpretar ninguna resolución. **Clase `A`.**
3. **`Y-01`≡`Z-01`** —el canal del sobre falló y no lo detecta nada— **NO reabre `O18`**. `O18`
   ya declaró de sí misma que era **TRANSITORIA y EXPLÍCITAMENTE LIMITADA**, que «*el ancla es
   la identidad del coordinador*» y que «*no hay forma mecánica de comprobarla*». **Este gate no
   descubre un riesgo nuevo: produce la primera instancia EMPÍRICA del riesgo que el Owner ya
   aceptó por escrito, y refuerza —no cuestiona— la obligatoriedad de `(c)` en `F6`.** Elevarlo
   al Owner sería pedirle que vuelva a decidir lo que ya decidió, y `O19` lo prohíbe.
4. **`Y-05`, `Y-08`, `Y-09`, `Y-13`** —las cuatro atribuciones que exceden la sede— **son de
   RESTA, no de enmienda**: retirar unas comillas y reetiquetar una procedencia. **F4 puede
   hacerlo sin escribir ni una palabra dentro de una resolución del Owner**, que es lo que
   `G21` de `KERNEL.md` L690 le prohíbe. `S-07` del documento 23 es el precedente de la
   conducta correcta y el propio corpus la exhibe.

> **Ninguna decisión de clase `B` del Owner queda pendiente hoy. Todo lo que este gate
> encuentra tiene remedio determinado dentro de `F4c`, salvo lo que ya está contratado para
> `F6`. Y eso es información buena, no mala: es la primera vez en cinco gates que se puede
> decir.**

---

## 14 · ¿ES LA MISMA CAUSA RAÍZ QUE EN LOS GATES 21, 22, 23 Y 24?

**Lo contesto con todas las letras, porque de esta respuesta depende que el trabajo siga o se
detenga.**

### 14.1 · SÍ EN PARTE, Y NO EN LA PARTE QUE IMPORTA. Y ésta es la primera vez que se puede decir eso.

**LO QUE SÍ ES LA MISMA CAUSA.** El patrón de método sigue vivo, y lo tengo en su forma más
limpia de los cinco gates:

```text
`W-04` cerró el perímetro ESCRITO de `G-29` —y generaliza de verdad: el perímetro dejó de
       escribirse— **y abrió, EN EL MISMO COMMIT DEL REMEDIO DE `O19` (`1d3b5d4`), un
       discriminante por BASENAME**. Lo reproduje: 38/38.
`X-04` cerró el reanclaje del bloque de estado **y la misma tanda escribió, en la fila de
       detalle de esa misma condición, una consecuencia declarada que es FALSA en el commit
       que la escribe**. Lo medí: `AA-02`.
`W-16` va por su CUARTA recurrencia con la regla escrita, el comando publicado y el comando
       denunciándola sobre el árbol que el gate juzga.
`O19`  cerró la procedencia por el lado de `O18` **y dejó cuatro sedes vivas atribuyéndole al
       Owner texto que su sede no contiene**, una de ellas la que va al Owner.
```

**Y hay algo peor, y es la novedad de este gate.** En los gates 21, 22, 23 y 24 lo que fallaba
era **el instrumento**: la batería, el derivador, el emisor. **En éste el instrumento funciona
—lo he atacado y ha aguantado seis veces— y lo que ha fallado es el CANAL, es decir, la
persona.** El coordinador emitió un sobre correcto y **entregó cinco sobres distintos e
incompletos**, y **nada en el corpus lo habría detectado**: no hay comprobación mecánica del
reparto del sobre, ni en la batería (`V-08`, `grep` = 0) ni en el emisor. **El único motivo por
el que este dictamen lo sabe es que el coordinador me lo declaró voluntariamente.** Coincido con
`Z3` en que eso **confirma la conclusión y no la atenúa**: la única defensa que `O18(b)` tiene
contra su propio canal es la honradez de quien lo opera. Esta vez se ejerció.

### 14.2 · Y AHORA LA PARTE QUE IMPIDE DECIR «no ha servido de nada», PORQUE SERÍA FALSO

**LOS TRES REMEDIOS QUE `X` DEJÓ DETERMINADOS ESTÁN LOS TRES APLICADOS, Y LOS TRES FUNCIONAN.
Lo verifiqué uno a uno con mis manos, y esto es real:**

```text
1 «el emisor lee el universo con `git show <commit>:<ruta>` y comprueba `git status` antes de
   emitir. Un sobre sucio no se emite»
   → **APLICADO Y VERIFICADO.** Lo ejecuté: fichero sin rastrear → `rc=2`; fichero rastreado
     modificado → `rc=2`; con el diagnóstico que cita `X-01` por su nombre. **CERRADO**

2 «el sobre publica el ÁRBOL DEL GATE junto al de la candidata»
   → **APLICADO Y VERIFICADO.** El sobre publica LOS DOS árboles, LOS DOS derivadores, LOS DOS
     universos y **las cuatro rutas en que difieren**, con su antes y su después. Era el
     defecto `V-01`/`W-11`/`X-2` que hundió al gate anterior. **CERRADO, y bien**

3 «el emisor y el derivador entran en el inventario de integridad, y la receta se corrige»
   → **APLICADO Y VERIFICADO.** La receta REPRODUCE: la ejecuté yo sobre los dos árboles y da
     los dos digest byte a byte (era el byte `0x0A` de `V-05`). Y `G-34` caza una puerta
     trasera SIN commitear en el emisor **y** en el derivador: 37/38 las dos. **CERRADO**
```

**Y `O19` es el remedio correcto a la otra mitad.** El Owner no respondió con una decimonovena
protección interna: creó una **sede externa a la paráfrasis**, y la tanda la implementó sin
escribir ninguna comprobación nueva —el censo sigue en 38 y `G-34` lo contrasta—. **Eso es
exactamente lo que `X` ordenó y lo que el Owner prohibió infringir.**

```text
gate del doc 21   3 falsos verdes            · la batería medía 30
gate del doc 22   8 árboles en verde         · la batería medía 30
gate del doc 23   `T` 7 · `U` 6, dos nuevos  · la batería medía 37
gate del doc 24   `W` 6 · `X` 6, dos por puertas nuevas · la batería medía 38
ESTE gate         `Z3` 9 declarados · **YO reproduje 6 y añadí 1 que nadie había abierto**
                                            · la batería mide 38
EL COSTE MARGINAL DE ENCONTRAR LA PUERTA SIGUIENTE SIGUE SIN SUBIR. Y las mías estaban
todas en la MISMA ZONA: `docs/owner/`, la que esta tanda acaba de abrir.
```

### 14.3 · MI RESPUESTA, SIN RODEOS

> **NO es exactamente la misma causa raíz.** Los gates 21, 22, 23 y 24 fallaron porque **la
> verificación estaba anclada dentro del objeto verificado**. Éste **no** falla por eso: el
> ancla externa existe, el instrumento que la produce está protegido, su receta reproduce y su
> huella se recalcula sin ejecutarlo. **Los tres remedios que `X` determinó se aplicaron y
> funcionan, y eso es un avance real que hay que decir.**
>
> **Lo que falla ahora es la mitad que nadie había podido medir hasta hoy: la ENTREGA.** `X`
> dejó escrito que «*lo externo es la ENTREGA, lo interno es la PRODUCCIÓN*» y que la
> producción era el problema. Se arregló la producción. **Y el primer gate que corre con la
> producción arreglada descubre que la entrega no tiene ninguna defensa.**
>
> **Y sí es la misma causa raíz en el MÉTODO:** cada hallazgo se cierra con **la forma exacta
> de su contraejemplo**, y el remedio abre la puerta contigua. `W-04` cerró el perímetro
> escrito y abrió el basename. `X-04` cerró el reanclaje y la misma tanda escribió una
> consecuencia falsa en la fila que lo declara. Es la **quinta vez consecutiva**.
>
> ### **EL TRABAJO DEBE SEGUIR. NO SE DETIENE.**
>
> Y digo por qué, distinguiéndolo del gate 23 —que sí mandó parar—: aquél paró porque `M-04`
> no era satisfacible desde dentro y **nadie había preguntado al Owner**. Hoy se ha preguntado
> **dos veces**, las dos respuestas existen (`O18`, `O19`), **ninguna decisión de clase `B` del
> Owner queda pendiente** (§13), y **los treinta y seis hallazgos tienen remedio determinado
> dentro de `F4c`**: ninguno es BLOQUEANTE, ninguno exige inventar arquitectura y ninguno
> vuelve al Owner. **Parar aquí sería parar con el remedio en la mano.**
>
> **Y expresamente, repitiendo la orden de `X` y del Owner, que sigue vigente y que esta tanda
> respetó: NO se escriba una protección interna nueva.** Lo que hace falta es de resta y de
> disciplina, no de código: que el `ENCARGO` del derivador barra `docs/owner/` en vez de
> nombrar un fichero; que `G-29` compare la **ruta completa** y no el basename; que el sobre se
> entregue **íntegro y textualmente idéntico** a todos los revisores —y que el adjudicador lo
> exija, que es lo que yo he hecho—; y que se retiren cuatro comillas que atribuyen al Owner
> texto que su sede no contiene.

---

## 15 · VEREDICTO

# INSUFICIENTE PARA F5

**`F4c` NO se cierra. Sigue ABIERTA. `F5` NO queda autorizada. No he corregido nada.**

**Y antes de las razones, lo que §2 obliga a decir:** **este gate es además INVÁLIDO**, por
diferencia entre los sobres entregados. §11.6 dice que un gate inválido no produce veredicto;
el manifiesto §8 me obliga a emitir uno de dos literales, y **un gate inválido no puede producir
`SUFICIENTE`**. Emito el único literal compatible. **Las razones 2, 3 y 4 son independientes de
la invalidez y bastan cada una por sí sola**, de modo que el veredicto **no depende de que yo
tenga razón en §2**.

**1 · EL GATE ES INVÁLIDO: los cinco sobres entregados no son idénticos campo a campo.**
Lo medí en §2.2: difieren en los campos **1, 3, 6, 7, 9, 12, 13 y 14**. `Z2` recibió el
**SHA-256 DEL DERIVADOR**; `Y1`, `Y2`, `Y3` y `Z1`, no. Ninguno de los cinco recibió el campo
1. Las obligaciones **2, 6 y 8** del revisor fueron **inejecutables**, y `Y2` lo anotó él mismo
(«campo 9 · **AUSENTE**»). El campo omitido es el que **la orden expresa del Owner en la sede
canónica L315-317 manda entregar** y el que **la obligación 3 del propio sobre manda mirar
PRIMERO**. Las obligaciones del adjudicador de §11.6 mandan declarar inválido «*ante CUALQUIER
diferencia **entre sobres***» y pre-rechazan la defensa de los dos dictaminadores con sus
palabras exactas: invalida «*aunque los dos árboles existan y los dos dictámenes coincidan*».
`X` excluyó su propia salvedad para este supuesto (doc 24 §2.2), y el manifiesto §8 sólo la
concede «como hizo `X`».

**2 · LA COBERTURA NO CIERRA: `ASIGNADO − LEÍDO = 1`**, y la regla de cierre lo dice sin
adorno. `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`, **1 196 líneas**, asignada al revisor
`Y` y **sin ninguna declaración válida de lectura íntegra**: `Y3` no dejó manifiesto de lectura
de sus cuatro fuentes, y `Y2` declara expresamente que su lectura fue «ACOTADA … el resto NO
abierto». **Cerré yo el `CHECKPOINT` leyéndolo entero; ésta no puedo cerrarla porque no está en
mi lote.** §8 del manifiesto: «*CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA
SUFICIENCIA*». `C-L.5` pasa de CERTIFICADA a **ABIERTA**, por primera vez en cuatro gates.
**Esto basta por sí solo, y se mide en vez de interpretarse.**

**3 · `A` NO SE SOSTIENE, Y LO REPRODUJE YO CON MIS MANOS.** **SEIS árboles defectuosos en
`38/38` verde con `EXIT=0`**, ninguno requiere commitear, ninguno toca la batería, su README,
`HEAD`, las refs, la base ni el runner, y cuatro llevan su control positivo en rojo. **CINCO de
los seis están en `docs/owner/`, la zona que esta misma tanda abrió.** Y el peor es mío y nadie
lo había visto: **un SEGUNDO documento del Owner, añadido por la vía que el corpus sanciona
—enlazado desde `00-INDICE.md`— que declara `F4c` CERRADA, `F5` AUTORIZADA y las tres
condiciones de `O18` sin efecto, pasa `38/38` commiteado y sin commitear, y queda FUERA del
universo obligatorio, sin fila de manifiesto, sin revisor asignado y sin huella en el sobre**
(`AA-01`). **Sobrevive al arreglo del bug de `Z-02`**, porque no explota ningún bug.

**4 · `B` NO ESTÁ DEMOSTRADA, y esta vez no falla el instrumento: falla el CANAL.** El sobre
emitido es correcto y lo reproduje entero, campo por campo. Lo que no se sostiene es lo que
`O18(b)` encarga: que **cada revisor** verifique contra **lo que recibió**. Cuatro de cinco no
pudieron. Y el **campo 14** no cumple ni siquiera en el sobre emitido: publica un **ROL**, y el
emisor lo acepta como texto libre con un rol por defecto (`AA-05`) — cuando ese campo es, en
palabras de §11.6, **«el ancla de (b)»** mientras no exista `(c)`. La advertencia 2 del criterio
de suficiencia del checkpoint —**que es del Owner**— dice que `B` no se da por satisfecha porque
el repositorio afirme que el sobre existió: **los revisores tienen que registrar lo RECIBIDO, y
lo que registraron son cinco objetos distintos.**

**5 · CUATRO SEDES VIVAS ATRIBUYEN AL OWNER TEXTO QUE SU SEDE CANÓNICA NO CONTIENE, en el árbol
que publica la regla que lo prohíbe.** Lo verifiqué contra la fuente primaria: las citas de doc
11 **L8497** y **L10243**, y el «*dice con sus palabras que «toca `C7`»*» de **L10246**, nacen
en el bloque **«LAS TRES ALTERNATIVAS QUE SE PRESENTARON»** del documento 23 §13·B — **la
PREGUNTA del coordinador, no la respuesta del Owner** — y su barrido sobre la sede canónica da
**cero**. Más `L7511`/`L9338`/`L9352` («*íntegra en el registro*») y `L8591` («*CI o el ejecutor
externo*», que la sede no dice). Es **`X-O13`** y **`X-O11`**, en la tanda que `O19` ordenó para
cerrar exactamente eso, y que corrigió doce sedes y dejó éstas.

**6 · `C-L.7` SE FALSA OTRA VEZ, y ahora por una causa que la propia tanda generó.** La fila de
detalle de `C-L.7`, dentro del bloque rotulado **CLASIFICACIÓN VIGENTE**, declara que `G-16`
saldrá en rojo y que el remedio «*vive en `verificacion/`, que este registro NO escribe*».
**`G-16` está VERDE y el remedio ya está aplicado — por el MISMO commit `5343260` que escribe la
declaración.** Es la **quinta recurrencia consecutiva** de la clase que `C-L.7` existe para
cerrar. **Y tres revisores la citaron como prueba de honradez sin ejecutarla** (`AA-02`).

**7 · Y LA RAZÓN DE MÉTODO.** **Al menos catorce de los treinta y seis los introdujo esta misma
tanda**, y los peores nacen **en el commit del propio remedio**: el discriminante por basename
de `G-29` nace en `1d3b5d4`, el commit que implementa `O19`; la declaración falsa de `C-L.7`
nace en `5343260`. **Quinta vez consecutiva que el remedio abre la puerta contigua.**

### Lo que expresamente NO fundamenta este veredicto

- **NO falla por `C`.** El Owner resolvió su fase; el contrato de §11.8 está completo; **no
  encontré ni una sede que presente `(b)` como `(c)`**. Ejecuté yo el ataque `C` más obvio
  (`AA-E11`) y **no lo cuento**.
- **NO falla por el DERIVADOR.** Es un programa **duro**: lo ataqué y aguantó. Su receta
  reproduce los dos digest byte a byte, sin ejecutar el emisor.
- **NO falla por el EMISOR.** Está reparado en los tres puntos que `X` determinó, y lo verifiqué
  los tres. **Se niega a emitir con el árbol sucio, y lo probé.**
- **NO falla porque el sobre EMITIDO esté mal.** Está bien, y lo reproduje entero.
- **NO falla por los agotamientos.** **54/54 pasan las dos reglas**, verificados por mí contra
  los tres árboles que citan y, de propina, contra `706c787`.
- **NO falla por la primera resta.** `OBLIGATORIO − ASIGNADO = ∅` en las dos direcciones, y las
  **70 filas** cuadran sin una discrepancia. La aritmética cierra al dígito.
- **NO falla porque quede arquitectura por inventar. NINGUNO de los treinta y seis es
  BLOQUEANTE, y ninguno vuelve al Owner.**
- **NO resuelvo nada por mayoría.** Fui contra **los dos** dictaminadores en §2, contra `Y4` en
  la clase y en la resta, contra `Z3` en `Z-10`, y contra `Y3` en `Y3-04`.

### LO QUE SÍ HA QUEDADO CERRADO, y no es cortesía

1. **LOS TRES REMEDIOS QUE `X` DETERMINÓ ESTÁN APLICADOS Y FUNCIONAN**, verificados uno a uno
   por mí: el emisor lee del commit y se niega con el árbol sucio (`rc=2`, las dos formas); el
   sobre publica **los dos árboles** con las rutas en que difieren; el emisor y el derivador
   entran en el inventario de integridad y una puerta trasera sin commitear los pone en rojo.
   **La tanda hizo lo que se le mandó.**
2. **`V-01`≡`W-11` y `V-05`≡`W-12` —los dos defectos que hundieron el gate anterior— CERRADOS
   CON MECANISMO.** La receta reproduce los dos digest **byte a byte**, y lo ejecuté yo.
3. **`X-01` CERRADO Y GENERALIZA**: el inventario de integridad **se deriva del directorio**,
   exige enumeración en el README y contrasta contra `HEAD`, con una declaración de corrección
   que **caduca sola**.
4. **`X-05` CERRADO Y GENERALIZA**: `ASIGNACIONES` se **DERIVA** del manifiesto y falla cerrado.
5. **`X-06`≡`V-23` CERRADO, Y LA REINCIDENCIA ROTA**: verifiqué las **70 filas contra los dos
   árboles** y el manifiesto **nombra el árbol de sus cifras**.
6. **`X-02` y `X-03` CERRADOS**: `O18` recibe su declaración de INVERIFICABILIDAD, y el sobre
   ancla la sede con **un digest por resolución** y su receta.
7. **La SEDE CANÓNICA del Owner está genuinamente protegida en su ruta real**: editarla,
   commiteada o no, da **rojo**. Lo probé las dos veces.
8. **`C-L.5` en su NÚCLEO sigue siendo el mejor trabajo del expediente**: universo derivado,
   manifiesto commiteado solo, aritmética exacta al dígito, cero discrepancias en 70 filas y
   **54/54 agotamientos plenos**. Lo que la reabre es su regla de cierre, no su mecanismo.
9. **`O19` es el remedio correcto y está bien implementado**: una sede EXTERNA a la paráfrasis,
   **sin escribir ninguna protección interna nueva**, que es exactamente lo que `X` ordenó y lo
   que el Owner prohibió infringir.
10. **Ninguna decisión de clase `B` vuelve al Owner.** Es la primera vez en cinco gates.

> **Ésta sigue siendo una candidata sólida. No falla por concepción, no falla por el
> instrumento y no falla por lo que el Owner decidió. Falla porque el canal que `O18(b)`
> encarga —la entrega del sobre— no tiene ninguna defensa y esta vez se rompió; porque una
> fuente asignada no se leyó; y porque la zona que `O19` acaba de abrir para dar sede a la
> autoridad del Owner admite un segundo documento normativo que el aparato de anclaje no ve.
> Las tres se corrigen dentro de `F4c`, y ninguna vuelve al Owner.**

**NINGÚN HALLAZGO SE HA CORREGIDO, y es deliberado: quien corrige no certifica.**

---

## 16 · CIERRE

```text
git status --porcelain   AL ABRIR    →   VACÍO     primer comando de la sesión
git status --porcelain   AL CERRAR   →   VACÍO     último comando
HEAD al abrir y al cerrar            →   82d8783679da06b8ccd6ec5e770b5bf9980bf27f, idéntico
RAMA                                 →   gate/f4c-certificacion-4b-20260830
FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ   ninguno
COMMITS · PUSH · PR · MERGE                                     ninguno
EXPERIMENTOS   /tmp/lab-AA/** — clones y `git archive` FUERA del repositorio
SUBAGENTE `Agent`                                               NO USADO
```

**`F4c` sigue ABIERTA. `F5` sigue NO AUTORIZADA. EL ADJUDICADOR NO CORRIGE: adjudica y
devuelve.**

**ADJUDICADOR `AA` · relevo · adjudicación cerrada.**
