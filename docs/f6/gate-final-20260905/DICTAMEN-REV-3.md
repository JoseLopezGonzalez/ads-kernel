# DICTAMEN DE `REV-3` · GATE DE CERTIFICACIÓN FINAL DE `F6` · 2026-09-05

**Candidata juzgada:** `c2437214c9353185d6b90b8fe86178302d4cf349`, tree `bb5b674`, base `769a8b6`.
**Árbol juzgado:** el congelado en `…/scratchpad/gate-congelado`. No se ha leído
`/home/jose/ads-kernel`.
**Intérprete de todas las órdenes de este dictamen:** `/home/jose/.local/bin/python3.12`.
**Lote:** 86 fichas · 55 208 líneas. **Leídas: 55 208 de 55 208.** `cerrado: true` en
`LECTURA-REV-3.json`.

---

## 1 · VEREDICTO

Las dos proposiciones se juzgan por separado y no se mezclan.

### `F6 ESTÁ COMPLETAMENTE IMPLEMENTADA` — **NO**

No por impresión: porque **ninguna de las medidas que la candidata publica mide esa
proposición**, y porque hay al menos una obligación del universo de `F6` —`V6-12`— cuya
implementación no alcanza al objeto que dice proteger.

El propio aparato de la candidata lo dice de sí mismo (HALLAZGO 3), y a eso se suman
HALLAZGO 1 —`V6-12` no juzga el contenido de la sede del Owner allí donde vive— y
HALLAZGO 4 —la comprobación 3 de `comprobar_integridad.py` está declarada y no existe—.
Un aparato en el que la etiqueta dice lo que el código no hace no acredita implementación
completa: acredita que alguien lo escribió.

### `F6 QUEDA CERTIFICADA` — **NO**

`O26` §5 pide, entre otras cosas, que no queden obligaciones internas sin implementar
(§5.1) y que no queden propiedades críticas sin una prueba capaz de fallar (§5.2). La
candidata no aporta ninguna medida de eso —lo dice su propio derivador, literalmente— y
sí aporta la contraria: sobre este árbol se puede reescribir la resolución `O26` del Owner
—la que otorga competencia a este gate— y los cuatro instrumentos de sellado siguen en
verde (HALLAZGO 1, reproducción compuesta). `M-04` —«se puede construir un árbol defectuoso
que pase en verde»— es obligación **de este mismo universo de 58** y está viva y medida.

No certifico. Y no es un «casi»: mientras el asiento de las resoluciones del Owner esté
fuera de las dos redes que este corpus tiene para sellar contenido, el gate no puede
afirmar sobre qué texto ha juzgado.

---

## 2 · LA LÍNEA BASE DEL COORDINADOR, REPRODUCIDA

Reproducida sobre copias mías (`R3-work/arbol`, `R3-work/exp`), no sobre el árbol congelado.
**Toda la línea base es cierta.** Que sea cierta es justamente lo que hace falta decir antes
de los hallazgos: no hay ni un número falso; lo que falla es lo que los números **no** miden.

```text
$ /home/jose/.local/bin/python3.12 kernel/operativo/validadores/registrar_evidencia.py
  38/38 validadores en verde · 38 evidencias publicadas · 0 problemas

$ /home/jose/.local/bin/python3.12 kernel/operativo/validadores/registro_pruebas.py
  314 escenarios · …/kernel/operativo/pruebas/REGISTRO-generado.md
  contraste del estado: 254 contrastados · 60 no contrastables · 0 divergencias
  no contrastables por estado declarado: contrato-definido 56 · validador-implementado 4

$ /home/jose/.local/bin/python3.12 docs/evolucion/verificacion/derivar-universo-obligatorio.py --obligaciones
  TOTAL 58 obligaciones
  A · sin COBERTURA DECLARADA … 0
  B · con cobertura y SIN NI UN SABOTAJE imputado que la ponga roja 0
  C · con cobertura y SIN FICHERO DE EVIDENCIA presente en el árbol 0

$ /home/jose/.local/bin/python3.12 kernel/operativo/validadores/huella.py --raiz .
  854dfa1b99be3824
$ cat kernel/.upstream-hash
  854dfa1b99be3824

$ (inventario derivado, invocando `inventariar_el_arbol()` de test_integridad_y_evidencia.py)
  puntos ejecutables: 58
  con guarda: 58
  sin guarda: 0
```

También reproducidos: 170 infracciones detectadas · 0 NO detectadas; 582 bloques canónicos ·
0 errores · 0 avisos; huella estable en dos cálculos; árbol byte-idéntico tras la corrida.

Y una comprobación mecánica del lote antes de leerlo, contra el árbol congelado:

```text
$ (recuento del lote contra el árbol: sha256, total de líneas y encaje de cada rango)
  fichas 86 lineas 55208
  DISCREPANCIAS: 0
```

---

## 3 · HALLAZGOS, POR GRAVEDAD

### HALLAZGO 1 · GRAVE · la sede de las resoluciones del Owner es el único sitio del árbol cuyo CONTENIDO EN DISCO nadie juzga

**Dónde.** `kernel/operativo/runtime/admision/__init__.py:106-112` y
`kernel/operativo/runtime/admision/perimetro.py:366-371`.

**Hecho reproducido.** Sobre una copia mía del árbol congelado (`R3-work/exp`, `HEAD` =
candidata, `git status` limpio), reescribo el TÍTULO de la resolución `O26` —la que otorga
competencia a este gate— dejándolo decir lo contrario de lo que dice:

```text
antes:  # `O26` · ACEPTACIÓN CONDICIONADA DE LA RAÍZ EXTERNA Y COMPETENCIA DEL GATE FINAL
ahora:  # `O26` · ACEPTACIÓN INCONDICIONAL Y CERTIFICACIÓN AUTOMÁTICA DE `F6`
```

```text
$ git status --porcelain
 M docs/owner/ADS-OWNER-RESOLUCIONES.md

$ /home/jose/.local/bin/python3.12 docs/f5/validar-f5.py | grep -i append
  append_only                       : contra 1d3b5d41: OK

$ /home/jose/.local/bin/python3.12 kernel/operativo/validadores/huella.py --raiz .
854dfa1b99be3824
   almacenada: 854dfa1b99be3824

$ /home/jose/.local/bin/python3.12 kernel/operativo/validadores/comprobar_integridad.py
T150  SUPERADA  La huella de integridad cubre a los validadores y detecta su edición
1 superadas · 0 fallidas

$ /home/jose/.local/bin/python3.12 kernel/operativo/runtime/ads_admision.py --repo . verificar --base 769a8b6 | grep -c "ADS-OWNER-RESOLUCIONES"
0
```

**El control del control, que es lo que convierte esto en un hallazgo y no en una sospecha.**
La MISMA clase de mutación en el árbol de trabajo, sobre un fichero de otra zona, SÍ se caza:

```text
$ printf 'LINEA COLADA POR REV-3\n' >> docs/evolucion/13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md
$ /home/jose/.local/bin/python3.12 kernel/operativo/runtime/ads_admision.py --repo . verificar --base 769a8b6
veredicto     ROJO
base          769a8b6dfd2d
mutaciones    120
zonas         30  sin condición: 0  sin zona: 0
hallazgos     120
  V6-10  MUTACION_NO_DECLARADA  docs/evolucion/13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md
      la zona `EVIDENCIA` tiene contenido INMUTABLE … y ha mutado con la letra M contra la
      referencia indice. Ninguna declaración de admisión levanta esta condición
```

Con la sede del Owner alterada, en cambio, el recuento de **mutaciones** sube de 119 a 120
—el verificador VE que el fichero ha cambiado— y el de **hallazgos** se queda en 119. Ve la
mutación y no la juzga.

**Y el juicio no es el culpable: lo es el canal que le da los bytes.** Alimentando
`sede.juzgar` con los bytes alterados a mano, el juez de `O27` §3 acierta a la primera:

```text
$ (invocando sede.derivar_libro + sede.juzgar sobre los mismos bytes alterados)
juicio SANO     : []
juicio ALTERADO : [{'codigo': 'ENTRADA_ALTERADA', 'identificador': 'O26',
  'causa': 'la entrada `O26` no coincide BYTE A BYTE con la que se introdujo en el commit
  6db4605b7f67 (3317 bytes → 3306 bytes). Da igual si el cambio es una condición, una fecha
  o un espacio: lo publicado se conserva'}]
```

**Por qué.** El canal:

```python
# admision/__init__.py, _contenidos_para_append_only
actual = canal.contenido("HEAD", ruta)
if actual is None:
    actual = canal.contenido_en_disco(ruta)
```

Los bytes del disco sólo se miran cuando `HEAD` **no tiene** el fichero. La sede del Owner
existe en `HEAD`, luego el juicio `append-only` se hace siempre contra `HEAD` y nunca contra
lo que hay. Y en `perimetro.juzgar` la sede sale por su rama con `continue`, de modo que
tampoco cae después en las ramas `INMUTABLE`/`DECLARADA`, que son las que sí contrastan el
árbol de trabajo para todas las demás zonas.

**Por qué importa.** No es un caso de laboratorio: es la clase `M-04`, que este mismo
universo de 58 obligaciones registra como deuda VIVA. El objeto sobre el que se puede
mentir sin que salte nada es precisamente el que dice quién puede certificar `F6` y bajo qué
condiciones. Y la asimetría no es una frontera de diseño («el gate juzga un COMMIT», `DD-20`)
sino una incoherencia del propio instrumento: la candidata SÍ juzga el árbol de trabajo en
las otras 29 zonas.

**Remedio que cierra la CLASE.** Que `_contenidos_para_append_only` devuelva las DOS
procedencias —los bytes de `HEAD` y los del disco— y que `_juzgar_append_only` exija que
coincidan antes de juzgar nada, con su código propio cuando difieran («la sede en disco no
es la sede que se va a juzgar»). Y su sabotaje mecanizado en `comprobar_negativos.py`:
alterar la sede en el árbol de trabajo tiene que poner roja a `V6-12`. Mientras el sabotaje
no exista, `B=0` seguirá contando `V6-12` como cubierta —que es literalmente el
contraejemplo que el propio derivador cita en el rótulo de la resta B.

---

### HALLAZGO 2 · GRAVE · la huella no cubre `docs/`, y por tanto no cubre ni la sede del Owner ni el documento que reclama el cierre de `F6`

**Dónde.** `kernel/operativo/validadores/huella.py:208` —
`AMBITOS = ("kernel", "packs", "tooling")`.

**Hecho reproducido.**

```text
$ /home/jose/.local/bin/python3.12 kernel/operativo/validadores/huella.py --raiz .
854dfa1b99be3824
$ printf '\nENTRADA FALSA DE REV-3\n' >> docs/owner/ADS-OWNER-RESOLUCIONES.md
$ printf '\nLINEA FALSA DE REV-3\n'   >> docs/f6/05-MATRIZ-CIERRE-G01-G08.md
$ /home/jose/.local/bin/python3.12 kernel/operativo/validadores/huella.py --raiz .
854dfa1b99be3824
$ cat kernel/.upstream-hash
854dfa1b99be3824
```

**Por qué importa.** La línea base publica «huella `854dfa1b99be3824` · almacenada =
calculada» como si sellara el árbol. Sella `kernel/`, `packs/` y `tooling/`. Quedan fuera:
la sede de las resoluciones del Owner, `docs/f6/05-MATRIZ-CIERRE-G01-G08.md` —el documento
donde la candidata reclama el cierre de `G-01`…`G-08` y `D-01`…`D-05`—, todos los gates de
`docs/evolucion/`, y `docs/canonico/`. En un corpus donde **la prosa es la norma** —lo dice
§6 de esa misma matriz—, la mitad normativa del árbol no está sellada por nada. Ni el
alcance está declarado en la línea base ni el nombre «huella del árbol» lo sugiere.

**Remedio que cierra la CLASE.** Que el ámbito de la huella se DERIVE (todo el árbol menos
exclusiones motivadas y comprobadas, al modo de `MOTIVOS_DE_EXCLUSION` del inventario de
`E-10`) en vez de ser una tupla escrita a mano, y que la línea base publique el ámbito junto
al valor. Un dígito de dieciséis cifras sin su alcance al lado es una cifra que se cree.

---

### HALLAZGO 3 · GRAVE · `A=0 · B=0 · C=0` no acredita `O26` §5.1 ni §5.2, y no hay ninguna otra medida en la candidata que lo haga

**Dónde.** `docs/evolucion/verificacion/derivar-universo-obligatorio.py`, sección «LAS TRES
RESTAS, DERIVADAS — Y LO QUE UNA RESTA VACÍA NO DEMUESTRA».

**Hecho reproducido.** El propio instrumento lo publica, literalmente, debajo de los ceros:

```text
$ /home/jose/.local/bin/python3.12 docs/evolucion/verificacion/derivar-universo-obligatorio.py --obligaciones
  A · sin COBERTURA DECLARADA: ningún `cubre` con validador la nombra 0
      NO demuestra `O26` §5.1 —«no quedan obligaciones internas sin implementar»—. Mide
      TRAZABILIDAD DECLARADA … Un `cubre` es una declaración escrita, y este aparato no sabe
      si lo declarado está construido
  B · con cobertura y SIN NI UN SABOTAJE imputado que la ponga roja 0
      NO demuestra `O26` §5.2 … Contraejemplo medido y vivo: `V6-12` figuraba con `B=0`
      mientras el append-only de la sede del Owner más allá del prefijo del nacimiento no
      tenía sabotaje ninguno (`ADJ-B3`)
  C · con cobertura y SIN FICHERO DE EVIDENCIA presente en el árbol 0
      NO demuestra que la evidencia sea VIGENTE ni que describa el árbol de hoy.
```

**Por qué importa.** El aparato es honesto —esto es un mérito, no un defecto suyo— y por eso
mismo el veredicto es forzoso: **no existe en la candidata ninguna medida de las dos
condiciones que `O26` §5 exige para certificar.** Que las restas salgan a cero es condición
necesaria y notoriamente insuficiente, y el contraejemplo que el propio rótulo de `B` cita
—`V6-12` con `B=0` y sin sabotaje del caso que importa— sigue vivo hoy: es el HALLAZGO 1
de este dictamen.

Medido además por mí, cruzando el universo de 58 contra el estado DERIVADO de los escenarios
que las cubren (coincidencia por prefijo de `cubre`, para no perder las formas `g.2 I-g1`):

```text
sin cobertura declarada: []
cubiertas SOLO por escenarios NO superados: []
con al menos un escenario no superado: 5
    CONTRATO 1     [('T277', 'validador-implementado')]
    CONTRATO 1bis  [('T277', 'validador-implementado')]
    CONTRATO 2     [('T277', 'validador-implementado')]
    D104           [('T277', 'validador-implementado')]
    V6-03          [('T352', 'validador-implementado')]
```

Ninguna obligación queda cubierta SÓLO por escenarios no ejecutados —eso hay que decirlo, y
es buena noticia—, pero cinco de las 58 se apoyan en parte en escenarios que el propio
corpus declara no ejecutados. Y `T277` no es un escenario cualquiera: es *«El universo
obligatorio de F6 se deriva completo y no puede omitir una obligación en silencio»*. El
escenario que garantiza al instrumento que produce los ceros está, él mismo, en
`validador-implementado`.

**Remedio que cierra la CLASE.** Una resta `D` derivada: para cada obligación, el ESTADO
DERIVADO —no el declarado— de cada escenario que la cubre; y la regla de que ninguna
obligación del universo puede apoyarse en un escenario por debajo de `prueba-superada` sin
que eso aparezca en una resta publicada. Y que el informe de certificación no pueda citar
`A/B/C` sin citar a su lado los rótulos que dicen qué NO demuestran.

---

### HALLAZGO 4 · SERIO · la comprobación 3 de `comprobar_integridad.py` está declarada y no está escrita

**Dónde.** `kernel/operativo/validadores/comprobar_integridad.py:13` (declaración) y
`:243-245` (código).

**Hecho reproducido.** Lo declarado, en la cabecera del módulo:

```text
  3. la huella es sensible al contenido y a la ruta  → mismo contenido en otro sitio
                                                        produce una huella distinta

La (2) y la (3) son las que impiden que alguien «arregle» un fallo de integridad
estrechando la definición de la huella hasta que deje de ver nada.
```

Lo escrito, íntegro, bajo el comentario que lleva ese mismo rótulo:

```python
    # 3 · sensible al contenido y a la ruta
    if huella.calcular(base) != calculada:
        r.fallo("la huella no es determinista: dos cálculos seguidos difieren")
```

Dos cálculos seguidos del MISMO árbol. No mueve un fichero de sitio, no cambia un byte, no
compara dos huellas de contenidos distintos. Es una comprobación de DETERMINISMO —y su
propio mensaje de fallo lo confiesa—, no de sensibilidad. La comprobación 3 declarada no
existe.

Y la (2), que la cabecera empareja con la (3) como la otra defensa contra el estrechamiento,
es una lista escrita a mano de diez ficheros (`IMPRESCINDIBLES`, `:201-211`), los diez
dentro de `kernel/` y `tooling/`. Por construcción no puede notar que `docs/` entero está
fuera del ámbito.

**Por qué importa.** Las dos defensas declaradas contra «estrechar la definición de la
huella hasta que deje de ver nada» son, una, una lista a mano que sólo mira donde ya se
cumple —la forma exacta de `H-03` y de `ADJ-B2`— y la otra, una comprobación que no está.
Y el estrechamiento que ninguna de las dos ve es el HALLAZGO 2. La clase es la que §6 de la
propia matriz llama «la que más caro sale»: *lo que la prosa promete no es lo que el código
ejecuta*.

**Remedio que cierra la CLASE.** Escribir la (3): copiar el árbol a un temporal, mover un
fichero cubierto a otra ruta con el mismo contenido, exigir huella distinta; y cambiar un
byte de un fichero cubierto, exigir huella distinta. Y sustituir `IMPRESCINDIBLES` por un
predicado derivado sobre el ámbito, con sus exclusiones motivadas y comprobadas.

---

### HALLAZGO 5 · SERIO · `§5` de la matriz de cierre publica dos cardinales que su propio `§6` corrige, en el documento que se declara «escrito al terminar»

**Dónde.** `docs/f6/05-MATRIZ-CIERRE-G01-G08.md:86` y `:88`, contra `:133` y `:135` del
mismo fichero. §5 abre diciendo: *«Esta sección se escribe al terminar y no antes: la
columna que importa es la última, y una matriz que se rellena por adelantado no mide,
promete.»*

**Hecho reproducido.**

```text
$ sed -n '86p;88p' docs/f6/05-MATRIZ-CIERRE-G01-G08.md
| **`G-01`** | … | `comprobar-cobertura-de-gate.py --autopruebas` · 23 controles · 0 sin detectar |
| **`G-03`** | … alcanza a **56 de 56** puntos ejecutables del inventario derivado … |

$ /home/jose/.local/bin/python3.12 docs/evolucion/verificacion/comprobar-cobertura-de-gate.py --autopruebas | tail -1
  26 controles · 0 sin detectar

$ (inventariar_el_arbol() sobre el árbol congelado)
  puntos ejecutables: 58 · con guarda: 58 · sin guarda: 0
```

Y el propio §6 del mismo documento ya escribe los números buenos: el hallazgo 3 dice
«26 controles · 0 sin detectar» y el hallazgo 5 dice que «56 de 56» era el recuento
defectuoso, sobre un inventario que no veía una clase entera.

**Por qué importa.** Es `HALL.10` otra vez —«48 componentes donde había 49», reproducido
dentro de la matriz que registra su corrección—, y esta vez dos veces, en la sección que el
`ENCARGO` señala como el sitio donde mirar el cierre. Un lector que crea a §5 se lleva un
`G-03` cerrado sobre 56 puntos y una cobertura ejercida con 23 controles: los dos números
son del árbol de antes de la corrección.

**Remedio que cierra la CLASE.** Que ningún cardinal se escriba a mano en la matriz: la
celda remite a la orden que lo deriva —que es lo que la propia fila de `G-05` hace bien y
lo que el hallazgo 10 acordó— y un validador exige que en `docs/f6/` no quede ningún
cardinal literal junto a un identificador de instrumento.

---

### HALLAZGO 6 · SERIO · sobrevive una SEGUNDA definición de «append-only», la del PREFIJO, en un punto que nadie ejecuta y que nada sella

**Dónde.** `docs/f5/validar-f5.py:529-553` (F22).

**Hecho reproducido.**

```python
    r.datos["append_only"] = f"contra {nacimiento[:8]}: " + (
        "OK" if hoy.startswith(orig) else "ROTO")
```

```text
$ /home/jose/.local/bin/python3.12 docs/f5/validar-f5.py | grep -i append
  append_only                       : contra 1d3b5d41: OK

$ grep -c "f5" kernel/operativo/validadores/validadores.yaml
0
$ grep -i "f5" R3-work/reg1.out
(sin salida — `validar-f5.py` no está entre los 38 validadores que la línea base corre)
```

Y su huella: `AMBITOS = ("kernel","packs","tooling")` deja `docs/f5/` fuera (HALLAZGO 2).

**Por qué importa.** `O27` §3 sustituyó el contraste de PREFIJO por el régimen de entradas
cerradas precisamente porque el prefijo aceptó un 34,1 % como «append-only comprobado»
durante cinco pasadas —lo escribe el propio `admision/__init__.py` en su `E-09`—. Aquí queda
la regla vieja, viva, ejecutable, dando «OK» sobre la misma sede, y con el agravante medido
en el HALLAZGO 1: el título de `O26` reescrito le sigue pareciendo `OK`, porque `O26` no
estaba en el commit de nacimiento y el prefijo no lo alcanza. Dos definiciones de la misma
propiedad en dos sedes son dos verdades, que es lo que `V6-19` cierra en el paquete de
admisión por esta misma razón.

**Remedio que cierra la CLASE.** O `F22` llama a `admision.sede.juzgar` —una sola sede de la
definición— o se retira con su motivo escrito. Y un validador que exija que ningún punto
ejecutable del inventario derivado quede fuera del manifiesto de validadores sin declaración
motivada: un ejecutable que nadie corre es un ejecutable cuyo veredicto nadie ha visto.

---

### HALLAZGO 7 · MODERADO · la equivalencia «`#!` ⟺ INVOCABLE», declarada «comprobada EN LOS DOS SENTIDOS sobre el ÁRBOL ENTERO», es falsa para 80 ficheros — y `T330b` EXIGE que lo sea

**Dónde.** `kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py:241` (cabecera
del módulo), `:1943-1946` (docstring de `T330`), `:1977-1988` (el bucle que la comprueba) y
`:2065-2091` (`T330b`).

**Hecho reproducido.** Lo declarado:

```text
        La equivalencia, comprobada EN LOS DOS SENTIDOS sobre el disco y sobre el ÁRBOL
        ENTERO —no sobre dos zonas escritas a mano—:

            lleva `#!`   ⟺   es INVOCABLE   ⟺   lleva el MECANISMO `E-10`
```

Lo comprobado: el bucle del punto 2 de `T330` recorre `for ruta, senales in
sorted(puntos.items())` —los 58 del inventario— y afirma sobre ellos. La dirección
`#! ⟹ INVOCABLE` no se comprueba sobre los excluidos, salvo en la rama
`biblioteca-suelta` de `T330b`.

Medido sobre el árbol congelado:

```text
puntos ejecutables: 58
ficheros .py con shebang en el arbol: 138
con shebang y FUERA del inventario de puntos: 80
excluidos por motivo: {'biblioteca-suelta': 7, 'biblioteca-de-paquete': 80}
residuales (shebang y NO invocable, tolerados por T330b): 80
```

Y `T330b` no sólo los tolera: los EXIGE.

```python
        self.assertTrue(residuales, "ningún módulo de paquete conserva línea de intérprete "
                                    "residual: si de verdad se retiraron todas, este "
                                    "recuento sobra y esta rama hay que quitarla")
```

**Por qué importa.** No es un agujero en `G-03`: los 80 son inertes al importarse y el
inventario los clasifica bien (`T380` ejerce esa frontera y es un buen control). Es un
defecto de la clase `DD-03`/`S1-04`/`O18` sexta condición —**el rótulo dice lo que el código
no hace**—, y está en el instrumento del que cuelga todo el aislamiento. Un lector que crea
la docstring concluye que en este árbol un `#!` implica guarda: hay 80 contraejemplos, y una
aserción que obliga a que los haya.

**Remedio que cierra la CLASE.** Reescribir la declaración para que diga lo que se comprueba
—`INVOCABLE ⟹ #! ∧ MECANISMO`, y `#! ∧ ¬paquete ⟹ INVOCABLE`— o comprobar la equivalencia
que se declara, retirando los 80 shebangs residuales y volviendo `residuales` en una resta
que tiene que ser VACÍA. Las dos cierran; lo que no cierra es la pareja actual.

---

### HALLAZGO 8 · LEVE · `RETIRADAS_DE_LA_RUTA` se asigna dos veces en `negativos_runtime.py` y el testigo de la purga queda siempre vacío

**Dónde.** `kernel/operativo/validadores/negativos_runtime.py:202` y `:214`.

**Hecho reproducido.**

```text
$ grep -n "^RETIRADAS_DE_LA_RUTA" kernel/operativo/validadores/negativos_runtime.py
202:RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()
214:RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()

$ (importando el módulo con PYTHONPATH puesto)
RETIRADAS_DE_LA_RUTA = []
```

La segunda llamada corre sobre una ruta ya purgada y devuelve la lista vacía, que es la que
queda publicada. El MECANISMO extraído sigue siendo idéntico byte a byte al de los otros 57
puntos —la segunda asignación cae fuera de la ventana `_INICIO`/`_FINAL`—, así que `T330`
punto 3 no lo ve.

**Por qué importa.** Poco, hoy: en este módulo nadie lee ese valor. Pero seis puntos del
árbol publican `"entradas_del_lanzador_retiradas": len(RETIRADAS_DE_LA_RUTA)` como parte de
su procedencia, y aquí ese testigo diría «no se retiró nada» habiendo retirado. Es una línea
duplicada dentro del instrumento que mide `E-10`.

**Remedio.** Retirar la asignación de `:214` y añadir al control de `T330` que el MECANISMO
aparezca exactamente una vez por punto.

---

## 4 · LO QUE NO HE PODIDO COMPROBAR, Y POR QUÉ

Un alcance sin declarar es el defecto que este proyecto ha visto más veces. Éste es el mío,
sin redondear.

1. **Mutaciones COMETIDAS (`commit`) de la sede del Owner.** El HALLAZGO 1 está reproducido
   sobre el árbol de trabajo. No he podido comprobar si una alteración **cometida** de una
   entrada publicada la caza `V6-12` end-to-end, porque el `ENCARGO` prohíbe toda orden `git`
   que escriba y no puedo fabricar el commit. Lo que sí he medido —y acota el hueco por
   arriba y por abajo— es que `sede.juzgar` acierta sobre los bytes alterados, y que el canal
   nunca le entrega los del disco. Presumo, sin haberlo medido, que la vía cometida SÍ se
   caza.
2. **Una desviación mía, declarada.** En una fase temprana de la revisión ejecuté
   `git checkout -- kernel/KERNEL.md` **dentro de mi copia de experimentos**
   (`R3-work/exp`), nunca en el árbol congelado ni en `/home/jose/ads-kernel`. El `ENCARGO`
   prohíbe «ningún `checkout` que mueva un árbol» y ése lo movió. Dejé de usar órdenes `git`
   de escritura en cuanto lo advertí y desde entonces todo se restaura con `cp` desde el
   árbol congelado, verificando `sha256sum` y `git status --porcelain` vacío después de cada
   experimento. No afecta a ninguna reproducción de este dictamen: todas ellas se hicieron
   después, y cada una termina con el árbol de trabajo limpio (queda constancia en las
   salidas: `RESTAURADO`, `ARBOL-EXP-LIMPIO`).
3. **Los 38 validadores por dentro.** He corrido `registrar_evidencia.py` entero sobre una
   copia y he leído entera la salida, pero no he auditado el cuerpo de los 38: leí íntegros
   los que caían en mi lote (`comprobar_arranque`, `comprobar_composicion_procesos`,
   `comprobar_fuentes`, `comprobar_integridad`, `comprobar_negativos`, `registro_pruebas`,
   `negativos_cardinalidad`, `negativos_runtime`). De los demás sólo he mirado lo necesario
   para las reproducciones de arriba.
4. **El catálogo de 170 mutaciones, una a una.** Reproduje el recuento agregado
   —170 detectadas · 0 NO detectadas— y leí entero `comprobar_negativos.py` (1797 líneas) y
   dos de los cuatro catálogos. No he comprobado que cada mutación reintroduzca de verdad el
   defecto que su docstring nombra; para el caso que importa a mi HALLAZGO 1, comprobé que
   **no existe** ninguna que altere la sede del Owner en el árbol de trabajo.
5. **`docs/f6/05-MATRIZ-CIERRE-G01-G08.md` está FUERA de mi lote.** Lo abrí sólo porque el
   `ENCARGO` manda atacar sus §5 y §6, y leí esas dos secciones (líneas 79-153). Las líneas
   1-78 no las he leído. El HALLAZGO 5 se apoya sólo en lo leído.
6. **`G-08` y `G-04` bajo carga**, la tercera capa de la invariante de `b.12` en
   `estado/motor.py` —que la propia matriz declara NO hecha— y los doce ataques de
   `T380`-`T397` ejecutados: los leí enteros, no los corrí. Correrlos exige montar
   instalaciones y envenenar entornos, y varios escriben evidencia.
7. **No he arrancado PesquerApp, no he tocado `redesign/kernel-2.0` y no he leído ni
   publicado `fd633383…`.** No he hablado con `REV-1` ni con `REV-2` ni he leído sus
   salidas parciales, pese a que el entorno me notificó dos veces que estaban corriendo.
8. **El directorio del coordinador se mueve bajo los pies.** Al empezar a escribir existía un
   `DICTAMEN-REV-3.md` de 52 729 bytes con fecha 2026-09-05 01:20 —de una ronda anterior—;
   minutos después, al ir a copiarlo antes de sobrescribirlo, ya no existía. Lo digo porque
   este fichero se escribe en un directorio que no es estable, no porque sospeche de nadie.
9. **La VALIDEZ del gate no la juzgo yo.** Mi manifiesto de lectura declara
   `cerrado: true` con 55 208 de 55 208 líneas; que el gate sea válido por cobertura lo dirá
   `comprobar-cobertura-de-gate.py` sobre los tres manifiestos, no este dictamen.

---

## 5 · UNA NOTA SOBRE LO QUE ESTÁ BIEN

Lo digo porque un dictamen que sólo enumera defectos no informa. La disciplina del **control
del control** está en casi todas las baterías que he leído y no es decorativa: `T382` exige
que el testigo APAREZCA sobre la versión sin guarda antes de exigir que no aparezca por la
vía oficial; `T394` relanza el hijo como lo lanzaba el runner de antes para demostrar que el
veneno funciona; `T380` monta el fichero del auditor en un temporal Y su control inverso.
La honestidad de los rótulos de las tres restas —decir en la propia salida qué NO demuestran
los ceros— es infrecuente y es la razón por la que el HALLAZGO 3 se puede escribir con la
salida del propio instrumento. Y el juicio de `O27` §3 en `admision/sede.py` es correcto:
falla por los bytes que le llegan, no por lo que hace con ellos.

Nada de esto cambia el veredicto. Lo enmarca: lo que le falta a esta candidata no es rigor,
es que dos de sus redes de sellado tienen el mismo agujero y ninguna de las dos lo declara.

— `REV-3`, 2026-09-05
