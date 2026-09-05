# DICTAMEN `REV-1` — GATE DE CERTIFICACIÓN FINAL DE `F6` · 2026-09-05

Revisor `REV-1`, contexto limpio. **No he escrito ni una línea de este corpus, no he aplicado
ninguna corrección, no he participado en ningún gate anterior y no he visto nada de `REV-2` ni
de `REV-3`.** Juzgo el árbol CONGELADO en `…/scratchpad/gate-congelado` (candidata
`c2437214c9353185d6b90b8fe86178302d4cf349`, tree `bb5b674`, base `769a8b6`). **No he leído
`/home/jose/ads-kernel`** y no he modificado ningún árbol del repositorio: todo lo que exige
escribir se hizo sobre copias mías bajo `…/scratchpad/rev1-work/`.

Intérprete: `/home/jose/.local/bin/python3.12` (Python 3.12).

---

## 1 · VEREDICTO — las dos proposiciones, por separado y sin mezclarlas

```text
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  `F6 ESTÁ COMPLETAMENTE IMPLEMENTADA`   ·   NO                           │
  │  `F6 QUEDA CERTIFICADA`                 ·   NO                           │
  └──────────────────────────────────────────────────────────────────────────┘
```

**Las dos respuestas son independientes, y lo digo expresamente porque el corpus castiga la
confusión.** La primera la niego por **un hallazgo GRAVE reproducido por mí sobre el motor de
estado** (§4.1): una invariante que el corpus declara CERRADA es evadible en dos transiciones
a través del canal oficial. La segunda la niego por una razón **distinta y anterior**, que no
depende de ninguno de mis hallazgos: **el propio aparato del árbol publica que sus tres restas
vacías NO acreditan lo que `O26` §5.1 y §5.2 le piden acreditar**, y ninguna otra medición del
árbol las acredita (§4.2). Si mañana el hallazgo GRAVE estuviera cerrado, la segunda seguiría
siendo NO; si `O26` §5.1/§5.2 estuvieran acreditadas por otra vía, la primera seguiría siendo
NO mientras la invariante sea evadible.

**Y lo que NO fundamenta este dictamen, dicho antes que las razones:** no falla por cobertura
—la mía cierra a ∅ y el manifiesto de este gate es el más limpio del expediente (§3)—; no falla
porque el verificador externo no exista —existe, está construido, lo he leído entero y lo he
visto ejercitado en procesos reales—; no falla por ninguna comparación con gates anteriores; y
**no he corregido nada**, que es deliberado: quien corrige no certifica.

---

## 2 · LA LÍNEA BASE, REPRODUCIDA — no creída

Ejecuté la suite entera sobre una **copia** del árbol congelado
(`…/rev1-work/arbol`), con el intérprete del encargo:

```console
$ python3.12 kernel/operativo/validadores/registrar_evidencia.py     # sobre MI copia
…
OK   cobertura-de-gate      código   0  publicada  …
38/38 validadores en verde · 38 evidencias publicadas · 0 problemas
EXIT=0
```

**Y la evidencia que produce mi corrida es BYTE A BYTE la que el árbol publica:**

```console
$ diff -rq …/rev1-work/arbol/kernel/operativo/pruebas/evidencia \
           …/gate-congelado/kernel/operativo/pruebas/evidencia
(sin salida)
```

Eso es más de lo que la línea base afirma y hay que decirlo primero: **la evidencia publicada
no es una captura antigua; es exactamente lo que el código produce hoy.**

| línea del coordinador | ¿reproduce? | cómo lo medí |
|---|---|---|
| `38/38 validadores en verde · 38 evidencias · 0 problemas` | **SÍ** | corrida completa sobre mi copia, `EXIT=0` |
| `170 infracciones detectadas · 0 NO detectadas` | **SÍ** | `negativos-salida.txt:347` |
| `582 bloques canónicos · 0 errores · 0 avisos` | **SÍ** | `lint-salida.txt:7` |
| `314 escenarios · 254 contrastados · 0 divergencias · 0 en prueba-ejecutada` | **SÍ** | `grep -c '^| \[T' REGISTRO-generado.md` → **314**; `evidencia-salida.txt` → `contrastados 254 · no contrastables 60 · divergencias 0`; `grep -c 'prueba-ejecutada' REGISTRO-generado.md` → **0** |
| `universo obligatorio: 58 obligaciones · A=0 · B=0 · C=0` | **SÍ** | `universo-obligaciones-salida.txt:28` y sus tres restas |
| `inventario de aislamiento: 58 puntos ejecutables · 58 con guarda · 0 sin guarda` | **SÍ, y NO SE PUBLICA EN NINGUNA EVIDENCIA** | derivado por mí con la función del propio corpus (§4.5) |
| `huella 854dfa1b99be3824 · almacenada = calculada · estable en dos cálculos` | **SÍ** | dos cálculos consecutivos, mismo valor |

**Las siete líneas son ciertas.** La séptima y la sexta necesitan una advertencia que va en
§4.2 y §4.5, y que no es sobre su verdad sino sobre lo que acreditan.

---

## 3 · LO QUE CONSTA A FAVOR, MEDIDO POR MÍ

Va antes que los hallazgos porque es verdad y porque un dictamen que sólo publica lo que rompe
no permite pesar lo que no rompió.

**EL MANIFIESTO DE ESTE GATE ES EL MÁS LIMPIO DEL EXPEDIENTE, y lo he medido entero.** El gate
inmediatamente anterior (`docs/f6/gate-definitivo/00-REGISTRO-DEL-GATE.md`) se declaró **NO
VÁLIDO** porque el coordinador asignó a un revisor la línea `12153` de un fichero de `12152`
líneas y dejó las líneas `1-94` sin asignar a nadie. **Ninguna de las dos cosas ocurre aquí:**

```console
$ (por cada una de las 209 filas de MANIFIESTO.json: wc -l y sha256sum contra el árbol congelado;
   y por cada fuente obligatoria, las líneas que ningún revisor tiene asignadas)
PROBLEMAS DE FORMA DEL MANIFIESTO: 0
FUENTES OBLIGATORIAS CON LINEAS SIN ASIGNAR: 0
OBLIGATORIO − ASIGNADO (fuentes): []
ASIGNADO − (obligatorio ∪ modificadas): []
(obligatorio ∪ modificadas) − ASIGNADO: []
modificadas SIN ninguna asignación íntegra: 0
REV-1 fuentes 87 lineas 55204 · REV-2 fuentes 86 lineas 55203 · REV-3 fuentes 86 lineas 55208
```

Es decir: **las 209 filas casan en `wc -l` y en SHA-256 contra el árbol congelado sin una sola
discrepancia; ningún rango excede su fichero; ninguna línea del universo obligatorio queda sin
asignar; y las 119 fuentes MODIFICADAS están todas asignadas a lectura ÍNTEGRA de alguien** —
que es la cuarta resta de `comprobar-cobertura-de-gate.py`, y la que en un manifiesto
deshonesto sería fácil de burlar (§4.9).

**Y lo demás que verifiqué y no cae:**

```text
· EL ESCENARIO `T225` ES REAL, y lo he leído entero (1 905 líneas). Veinticuatro pasos sobre
  repositorios Git de verdad, un remoto bare con dos clones, DOS PROCESOS independientes,
  claves Ed25519 efímeras fuera de todo repositorio, un adaptador que mata de verdad, una
  caída inyectada con código 70 y una raíz externa que atesta desde fuera. Ningún mock hace
  de pieza principal, y el paso 24 son CUATRO controles negativos que ponen roja la propia
  prueba si se sabotea lo que declara proteger
· LA RAÍZ EXTERNA ESTÁ CONSTRUIDA Y ES SEPARABLE. Leí `verificador.py` entero: proceso y
  paquete aparte, `sys.path` que apunta a la INSTALACIÓN y jamás al árbol verificado, firma
  asimétrica Ed25519 delegada en el anfitrión, siete pasos en orden con testigo, evidencia
  fuera del árbol, `G-A9` implementado —el árbol se autodeclara VERDE y la atestación lo
  DESMIENTE— y `6 bis`: se VERIFICA lo que se acaba de firmar, que cierra el caso en que el
  anfitrión firma con una clave que el anillo no acepta
· EL CATÁLOGO NEGATIVO ES SERIO. `negativos_integridad.py` y `negativos_contratos19.py`
  declaran su infracción, su prueba imputada Y **el diagnóstico esperado**: sin `espera`, una
  prueba se daría por detectada porque falló, sin comprobar que falló POR ESO
· EL GOBIERNO GIT SE PRUEBA POR SUS DOS MITADES. `G-A8` IMPOSIBLE —el hook rechaza el forzado
  también en la forma de TRES argumentos, que era la puerta— y DETECTABLE —quitado el hook, el
  linaje denuncia el forzado incluso tapado por un commit legítimo posterior—, con controles
  positivos para que la protección no consista en no dejar hacer nada
· LOS CARDINALES DEL APARATO SE DERIVAN. `comprobar_recuentos.py` retiró la lista literal
  `AFIRMACIONES` y la sustituyó por reglas `(patrón de sede, derivación)`, con `T270`
  ejerciendo la propiedad sobre una sede fabricada que ninguna lista podría contener
· NINGUNA SEDE VIVA PRESENTA DEUDA DE `F6` COMO IMPLEMENTADA. Lo barrí y no encontré ninguna
```

---

## 4 · HALLAZGOS, POR GRAVEDAD

Cada uno lleva **la orden literal y su salida literal**, la sede, por qué importa y **el
remedio que cierra la CLASE** — no la instancia.

---

### GRAVE 1 · `G-04` se declara CERRADO y su invariante es evadible en dos transiciones por el canal oficial

**Sede.** `docs/f6/05-MATRIZ-CIERRE-G01-G08.md` §5, fila `G-04`, que dice:

> «**CERRADO** por `A2` · la invariante de `b.12` se interpone en la PUERTA y en el
> `AlmacenVigilado`; **la prioridad de un paquete existente no se mueve en ninguna transición
> del runtime**.»

**El código, leído por mí** —`kernel/operativo/runtime/runtime/estado_util.py`,
`exigir_inmutables_del_paquete`—:

```python
for campo in CAMPOS_INMUTABLES_DEL_PAQUETE:          # ("prioridad",)
    if campo not in anterior or campo not in contenido:
        continue                                     # ← LA PUERTA
    if contenido[campo] == anterior[campo]:
        continue
    raise PrioridadInmutable(...)
```

**HECHO REPRODUCIDO, sobre un almacén real y por el canal oficial del runtime** (script en
`…/rev1-work/ataque_g04.py`, ejecutado sobre una copia mía):

```console
$ python3.12 ataque_g04.py
prioridad inicial: 50
--- control: intento DIRECTO 50 -> 999 (debe caer) ---
  RECHAZADO: PRIORIDAD_INMUTABLE
--- PASO 1: BORRAR el campo `prioridad` ---
  CONFIRMADO. paquete durable tiene prioridad?: False
--- PASO 2: volver a ESCRIBIR prioridad = 999 ---
  CONFIRMADO. prioridad durable AHORA: 999
```

**Por qué importa.** El control positivo funciona —el salto directo `50 → 999` se RECHAZA—, y
por eso la fila se pudo escribir de buena fe. Pero la guarda compara **campo a campo entre dos
diccionarios**, y la ausencia del campo es su punto ciego por construcción: el paso 1 pasa
porque `campo not in contenido`, y el paso 2 pasa porque `campo not in anterior`. **Dos
transiciones ordinarias, ninguna bandera, ningún privilegio, y la prioridad —que `b.12`
declara autoridad EXCLUSIVA del Owner y que el despacho usa como primer criterio de orden—
queda movida en el estado durable.** `comprobar_paquete`, que sí rechazaría un objeto sin el
campo, sólo se invoca en los caminos de LECTURA (`vistas.py`, `dispatcher.py`); `Almacen.aplicar`
no lo llama. Y ninguna de las veinte pruebas `T400`–`T419` ejercita el borrado del campo: lo
comprobé leyéndolas enteras.

**Remedio que cierra la CLASE** —no esta instancia—: que la invariante deje de compararse
campo a campo entre dos diccionarios y pase a exigir **la PRESENCIA del campo en el objeto
resultante** siempre que estuviera en el anterior, de modo que **desaparecer sea una mutación
como cualquier otra**; y que el sabotaje imputado a la invariante sea el de **dos
transiciones**, no el del salto directo — una propiedad cuyo único sabotaje es el caso fácil no
está probada contra el caso que la derrota.

---

### GRAVE 2 · el propio aparato publica que `A=0 · B=0 · C=0` NO acredita `O26` §5.1 ni §5.2, y ninguna otra medición del árbol las acredita

**Éste es el hallazgo que decide la segunda proposición, y no es mío: es del instrumento.**

`O26` §5 —sede canónica, `docs/owner/ADS-OWNER-RESOLUCIONES.md`— condiciona la COMPETENCIA de
un gate para declarar `F6 CERTIFICADA` a demostrar **simultáneamente** cinco cosas. Las dos
primeras son «que no queden obligaciones internas de `F6` sin implementar» y «que no queden
propiedades críticas sin una prueba capaz de fallar».

**Lo que la evidencia publicada dice de sí misma**, literal, en
`kernel/operativo/pruebas/evidencia/universo-obligaciones-salida.txt`:

```text
  A · sin COBERTURA DECLARADA: ningún `cubre` con validador la nombra 0
      NO demuestra `O26` §5.1 —«no quedan obligaciones internas sin
      implementar»—. Mide TRAZABILIDAD DECLARADA: … Un `cubre` es una
      declaración escrita, y este aparato no sabe si lo declarado está
      construido

  B · con cobertura y SIN NI UN SABOTAJE imputado que la ponga roja 0
      NO demuestra `O26` §5.2 … Contraejemplo medido y vivo: `V6-12` figuraba
      con `B=0` mientras el append-only de la sede del Owner más allá del
      prefijo del nacimiento no tenía sabotaje ninguno (`ADJ-B3`)

  C · con cobertura y SIN FICHERO DE EVIDENCIA presente en el árbol 0
      NO demuestra que la evidencia sea VIGENTE ni que describa el árbol de hoy
```

**Y la sede pivotal se contradice consigo misma sobre esto.**
`docs/f6/01-MATRIZ-DE-COMPLETITUD-F6.md`:207-213 escribe la equivalencia:

```text
O26 §5.1  que no queden obligaciones internas de F6 sin implementar        → RESTA A
O26 §5.2  que no queden propiedades críticas sin una prueba capaz de fallar → RESTA B
O26 §5.3  que todas las obligaciones tengan trazabilidad hasta evidencia    → RESTA C
```

y el **mismo fichero**, línea 375, la niega:

> «las tres restas vacías eran ciertas y **no acreditan lo que `O26` §5.1 y §5.2 les piden
> acreditar**. Un cero verdadero sobre un criterio que no mide lo que dice medir sigue sin ser
> una certificación.»

**Por qué importa, y por qué basta por sí solo para la segunda proposición.** Certificar `F6`
exige **demostrar** las cinco condiciones, no medir tres restas y llamarlas por su nombre. Hoy
el árbol tiene **una medición verdadera de otra cosa** (trazabilidad declarada, existencia de
al menos un sabotaje imputado, presencia de un fichero) y **ninguna medición de lo que `O26`
§5.1 y §5.2 exigen**. Un adjudicador que certificara sobre `A=0·B=0·C=0` estaría emitiendo
exactamente la «promesa de seguridad superior a la realmente entregada» que `O18` prohíbe — y
el árbol se lo dice él mismo, en su propia evidencia, en el commit que se somete a este gate.

**Remedio que cierra la CLASE.** O bien las tres restas **miden lo que sus rótulos prometen**
—§5.1 exige construcción, no `cubre` declarado; §5.2 exige cobertura de propiedad a propiedad,
no «al menos un sabotaje imputado»—, o bien **§2.6 de la matriz retira la equivalencia** y
declara qué medición SÍ acredita cada una de las cinco condiciones de `O26` §5, con su comando.
Lo que no puede sostenerse es lo de hoy: una sede que iguala restas y condiciones a doscientas
líneas de otra que dice que no son lo mismo.

---

### GRAVE 3 · el canal de contraste contra `HEAD` (`D-05`) no alcanza a las SEIS evidencias que publican cuatro líneas de la línea base

**Sede.** `kernel/operativo/validadores/comprobar_evidencia.py`, `_contrastar_contra_head`
(L944), que construye el conjunto a contrastar así:

```python
por_evidencia = {}
for datos in escenarios:
    evidencia = (datos.get("evidencia") or "").strip()
    if evidencia:
        por_evidencia.setdefault(os.path.basename(evidencia), []).append(datos)
for nombre in sorted(por_evidencia):        # ← sólo lo que algún escenario CITA
```

**HECHO REPRODUCIDO:**

```console
$ (evidencias publicadas en pruebas/evidencia/ frente a las citadas por algún `evidencia:`)
evidencias publicadas : 38
citadas por escenarios: 32
NO citadas por ningun escenario: ['cobertura-de-gate-salida.txt', 'lint-salida.txt',
  'negativos-salida.txt', 'universo-obligaciones-salida.txt',
  'universo-obligatorio-salida.txt', 'universo-rutas-salida.txt']
```

**Y las seis que quedan fuera son, exactamente, las que publican cuatro de las siete líneas de
la línea base de este gate:** `582 bloques canónicos` (`lint`), `170 infracciones detectadas`
(`negativos`), `TOTAL 58 obligaciones · A=0 · B=0 · C=0` (`universo-obligaciones`) y
`26 controles · 0 sin detectar` (`cobertura-de-gate`).

**Por qué importa.** `T350` publica en la evidencia «contraste contra el blob de `HEAD`:
**EJERCIDO**» sin decir **sobre cuántas de las 38**. Un lector razonable —y un adjudicador—
entiende que la garantía cubre la evidencia publicada; cubre 32 de 38, y las 6 descubiertas son
justamente las que nadie contrastaría por otra vía, porque no las sostiene ningún escenario.
**Lo comprobé yo, sobre una copia mía** (`…/rev1-work/d05/`): edité a mano `582→9` en
`lint-salida.txt` y `170→3` en `negativos-salida.txt`, y la corrida dio `T158 SUPERADA ·
T350 SUPERADA · EXIT=0`, con el canal declarando «EJERCIDO» y `T150 SUPERADA` —la huella no
se mueve, porque las evidencias no entran en la huella del corpus—.

**Remedio que cierra la CLASE.** Que el conjunto a contrastar se DERIVE **del directorio de
evidencia**, no de las citas de los escenarios —una evidencia que nadie cita es exactamente la
que nadie mira—; y que la nota de `T350` publique **el cardinal contrastado sobre el total**,
de modo que «EJERCIDO» deje de poder significar «sobre las que alguien citó».

---

### MODERADO 4 · §5 de la matriz pivotal publica DOS cardinales que su propio §6 registra como corregidos

**Sede.** `docs/f6/05-MATRIZ-CIERRE-G01-G08.md`, §5, filas `G-01` y `G-03`.

```console
$ sed -n '86p' docs/f6/05-MATRIZ-CIERRE-G01-G08.md
| **`G-01`** | **CERRADO** · … | `comprobar-cobertura-de-gate.py --autopruebas` · 23 controles · 0 sin detectar |

$ grep -n 'controles' kernel/operativo/pruebas/evidencia/cobertura-de-gate-salida.txt
33:  26 controles · 0 sin detectar

$ sed -n '133p' docs/f6/05-MATRIZ-CIERRE-G01-G08.md        # §6, fila 3, del MISMO documento
| **3** GRAVE | `G-07` **no se ejercía**: los 23 controles … | tres controles nuevos … | 26 controles · 0 sin detectar, y la sonda del auditor mide ahora **8 llamadas a `git`** |
```

```console
$ sed -n '88p' docs/f6/05-MATRIZ-CIERRE-G01-G08.md
| **`G-03`** | **CERRADO** por `A1` · … alcanza a **56 de 56** puntos ejecutables del inventario derivado … |

$ python3.12 -c "…import test_integridad_y_evidencia as m; p,e=m.inventariar_el_arbol(); print(len(p))"
58

$ sed -n '135p' docs/f6/05-MATRIZ-CIERRE-G01-G08.md        # §6, fila 5, del MISMO documento
| **5** SERIO | «56 de 56» era 56 sobre un inventario que **no veía una clase entera** … |
```

**Por qué importa.** Es el documento que este gate tiene que juzgar, y sus dos secciones se
desmienten: **§6 registra la corrección del cardinal que §5 sigue publicando**. No es una
errata cualquiera: `G-01` y `G-03` son dos de las ocho condiciones cuyo cierre esta matriz
afirma, y el cardinal que publican es la prueba que ofrecen de ese cierre. Un lector que se
detenga en §5 —que es donde está el veredicto— se lleva los dos números que §6 declara
caducados.

**Remedio que cierra la CLASE.** Que las celdas de prueba de §5 **no escriban cardinales**:
que publiquen el comando que los deriva, como el corpus exige desde `J-07`. Sustituir `23` por
`26` y `56` por `58` cerraría la instancia y dejaría la clase: el día siguiente en que el
inventario crezca, la matriz volverá a mentir sola.

---

### MODERADO 5 · el cardinal del inventario de aislamiento no lo publica ninguna evidencia, y las dos sedes vivas que lo escriben dicen «nueve» y «56»

**HECHO REPRODUCIDO**, con la función del propio corpus:

```console
$ python3.12 -c "import test_integridad_y_evidencia as m; p,e=m.inventariar_el_arbol(); …"
puntos ejecutables: 58
excluidos: 87
con purga: 58
sin purga: 0
```

**Y lo que las sedes vivas escriben:**

```console
$ grep -n 'nueve' kernel/operativo/pruebas/T290-T311-integridad-evidencia-y-contencion.md
576:El inventario resultante son **nueve** puntos ejecutables: los cinco `ads_*.py` y
581:en los nueve, y una prueba lo verifica por digest: copiado, no adaptado.
593:  - "el inventario alcanza las dos zonas y contiene los nueve puntos ejecutables"
595:  - "los nueve llevan el mismo prólogo `E-10`, byte a byte"

$ grep -n 'ALCANCE SON 56' kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py
1956:        DESDE `D-01`, EL ALCANCE SON 56 Y NO 35. …

$ grep -rn 'de 56\|58 puntos' kernel/operativo/pruebas/evidencia/
(sin salida — ninguna evidencia publica el cardinal)
```

**La línea 593 es el `entonces:` de un bloque `ads:escenario`**, es decir la afirmación
normativa de `T330`, y dice **nueve** sobre 58. **Y la que lo mide no comprueba el cardinal:**

```console
$ sed -n '2018p' kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py
        self.assertGreaterEqual(len(puntos), 50)
```

Un suelo, no el cardinal publicado.

**Por qué importa, y cuál es la causa mecánica.** El corpus tiene un guardián para esto
—`comprobar_recuentos.T151`— y **no puede verlo**: leí su diccionario `REGLAS` entero y **no
hay ninguna regla para el objeto «puntos ejecutables»**; `derivar()` tampoco lo cuenta, y
`RECUENTOS-generado.md` no lo publica. De modo que el cardinal de la propiedad que `G-03` cierra
—y que la línea base publica como `58 · 58 · 0`— vive sólo en prosa, en dos sedes, y las dos
están caducadas. Es el defecto exacto que el `CONTRATO 1bis` de §19 existe para cerrar («un tipo
tipado sin censo es `N-04` otra vez»), aplicado a un objeto que no es un bloque tipado.

**Remedio que cierra la CLASE.** Que el inventario de puntos ejecutables **se publique en la
evidencia de `T330`/`T380` con su cardinal derivado**, y que ninguna sede lo escriba a mano —ni
en prosa ni en el `entonces:` de un escenario—. Corregir «nueve» por «58» cerraría la instancia
y dejaría la clase: no hay hoy ninguna comprobación que impida que vuelva a caducar.

---

### MODERADO 6 · una corrección declarada «corregida» que sólo se aplicó a una de sus tres sedes, y la tercera es un derivado

**Sede.** `docs/f6/00-ESTADO-DE-IMPLEMENTACION-F6.md`:249, tabla «Lo que SÍ encontró, y se
corrigió en la única pasada de corrección»:

```text
| la cabecera del escenario decía «veintiún pasos» y el escenario tiene veinticuatro
| CORRECCIÓN DETERMINADA | corregida |
```

**HECHO REPRODUCIDO:**

```console
$ grep -rn 'veintiún pasos\|veinticuatro pasos' kernel/ docs/f6/
kernel/operativo/runtime/pruebas/escenario_e2e_f6.py:34:  … los veinticuatro pasos …
kernel/operativo/runtime/pruebas/escenario_e2e_f6.py:38:  … los veinticuatro pasos …
kernel/operativo/runtime/pruebas/escenario_e2e_f6.py:328: """Los veinticuatro pasos. …"""
kernel/operativo/pruebas/T210-T225-…md:21:  … `escenario_e2e_f6.py` —veintiún pasos— …
kernel/operativo/pruebas/T210-T225-…md:373: nombre: El escenario … con sus veintiún pasos
kernel/operativo/pruebas/REGISTRO-generado.md:172: | [T225](…) | El escenario … con sus veintiún pasos | …

$ tail -3 kernel/operativo/pruebas/evidencia/e2e-f6-salida.txt | head -1
24 de 24 pasos CUMPLIDOS
```

**Por qué importa.** La línea 373 no es prosa: es el campo `nombre:` del bloque
`ads:escenario` de `T225`, y por eso el cardinal falso **se propaga solo** a
`REGISTRO-generado.md`, que es un DERIVADO. La corrección se aplicó al fichero de código —tres
veces— y no a la sede normativa ni, por tanto, a su derivado; y el documento de estado la
declara «corregida». Es la clase que el expediente gradúa GRAVE cuando la comete un
`CORRIGENDUM` (`HH2-08`): **una afirmación de haber aplicado un remedio que el árbol desmiente.**

**Remedio que cierra la CLASE.** Que el `nombre:` de un escenario **no lleve cardinales del
objeto que la prueba recorre** —que se deriven o se remitan—, y que la fila de una corrección
no pueda declararse «corregida» sin enumerar **todas** las sedes que su hallazgo nombró, con el
comando que demuestra que ninguna queda.

---

### MODERADO 7 · cinco sedes vivas afirman en presente que doce escenarios «han BAJADO a `prueba-ejecutada`», y los doce están publicados como `prueba-superada`

**HECHO REPRODUCIDO:**

```console
$ grep -rn 'BAJADO' kernel/operativo/pruebas/*.md
T159-T170-multirepo.md:18:  **`H-02` · `T162`…`T168` han BAJADO a `prueba-ejecutada` …
T172-T181-estado-durable.md:7: **`H-02` · `T180` y `T181` han BAJADO a `prueba-ejecutada` …
T182-T194-runtime-y-admision.md:10: **`H-02` · `T193` ha BAJADO a `prueba-ejecutada` …
T210-T225-…md:10: **`H-02` · `T225` ha BAJADO a `prueba-ejecutada` …
T290-T311-…md:12: **`H-02` · `T301` ha BAJADO a `prueba-ejecutada` …

$ (por cada uno de los doce: el `estado:` de su bloque y su fila en el REGISTRO derivado)
T162 bloque=prueba-superada registro=**PRUEBA SUPERADA**
T163 … T164 … T165 … T166 … T167 … T168 … T180 … T181 … T193 … T225 … T301
   los DOCE: bloque=prueba-superada registro=**PRUEBA SUPERADA**
```

**Y el propio corpus lo dice por el otro lado**, en `negativos_contratos19.py`, docstring de
`m_h02_un_escenario_sube_de_estado_sin_contraste`:

> «Cerrada `D-02`, su ejecutor publica el veredicto nominal y `T162` declara `prueba-superada`
> con todo el derecho: **ya no hay ningún escenario en el estado que este sabotaje
> reintroducía**, y por eso dejó de encajar.»

**Por qué importa.** La subida de estado es LEGÍTIMA —lo verifiqué: las evidencias nombran hoy
a los doce— y el defecto está sólo en el texto. Pero ese texto es la sede que registra el
remedio de `H-02`, uno de los once hallazgos de la auditoría independiente que §6 de la matriz
declara cerrados, y hoy **dice en presente lo contrario de lo que su propio fichero publica en
sus bloques**. Nada mecánico lo ve: `comprobar_evidencia` contrasta el `estado:` del bloque
contra la evidencia, nunca la prosa que lo encabeza.

**Remedio que cierra la CLASE.** Que una nota que describe un estado pasado **lleve su rótulo
histórico**, como el corpus exige en el bloque reanudable del checkpoint; y que la nota de un
remedio **remita al `estado:` derivado** en vez de afirmar un estado que el mismo fichero
publica de otra manera.

---

### MENOR 8 · un cardinal escrito a mano, replicado en 23 sedes, es falso

```console
$ grep -rln 'aa219465a6dd6a04' --include=*.py --include=*.md . | wc -l
23
$ grep -rn 'aa219465a6dd6a04' --include=*.py . | head -1
tooling/workspace.py:…      ejecutables del árbol (digest `aa219465a6dd6a04`, 1 869 bytes) …
$ python3.12 -c "…p,_=m.inventariar_el_arbol(); print(len(p[next(iter(p))]['mecanismo'].encode()))"
1879
```

El **digest es correcto** —`aa219465a6dd6a04`, idéntico en los 58 puntos, verificado por mí—;
el tamaño no: son **1 879 bytes**, no 1 869. `T330` comprueba que el digest sea único y **no
comprueba el tamaño**, así que nada lo ve. Es MENOR porque no cambia ninguna garantía; se
consigna porque está escrito 23 veces en un corpus cuya tesis es que ninguna cifra se escribe a
mano, y porque va **al lado de un digest que sí es cierto**, que es lo que le da crédito.
**Remedio de clase:** retirar el tamaño del recital y dejar sólo el digest, que es lo que la
prueba comprueba.

---

### MENOR 9 · el instrumento del expediente anterior está en ROJO sobre el árbol congelado, y ninguna sede lo publica

```console
$ python3.12 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py   # sobre MI copia
FALLO G-13  … └─ barrido de `PN-15`: publica 1 en (a) y el fichero deriva 3
FALLO G-15  … └─ reparto por vía 2: publica 1 y el catálogo deriva 0; reparto por vía 4:
                 publica 8 y el catálogo deriva 9; árbol real: `(DEP, SEG)` no se deriva
                 por la vía obligatoria
FALLO G-21  … └─ `O23` vive en la SEDE CANÓNICA y NO tiene proyección `### `O23`` en el
                 registro de decisiones … `O24` … idem
FALLO G-23 · FALLO G-29 · FALLO G-30
32/38 comprobaciones en verde
```

**Acoto lo que sostengo, y lo que NO.** `G-23`, `G-29` y `G-30` fallan **CERRADO por falta de
`.git`** en mi copia —la propia batería lo declara: «9 de las 38 exigen un repositorio CON
HISTORIA»—, y **no los cuento**. `G-13` y `G-15` **no** están en esa lista y fallan por
divergencia de cardinales derivados. `G-21` corre y falla por FORMA: verifiqué que `O23`…`O27`
**sí están proyectadas**, como filas `D112`–`D116` de la sección 1 del registro, cada una
rotulada «PROPAGACIÓN DE `Onn` … se declara DERIVADA»; lo que falta es el bloque
`### \`Onn\`` de la sección 2, que `O17`–`O22` sí tienen. **Corrijo aquí una lectura mía
anterior que era más grave y era falsa: la proyección existe.**

**Por qué se consigna.** Esta batería **no está en `validadores.yaml`** —lo comprobé: 0
coincidencias— y por tanto no forma parte del `38/38` de la línea base, ni de las obligaciones
de `F6`. Pero **sigue en el universo obligatorio** (`universo-rutas-salida.txt:36`, 4 513
líneas), sigue siendo ejecutable, y **ninguna sede del árbol publica su rojo ni lo declara
esperado o retirado**. **Remedio de clase:** que el corpus declare, en una sede viva, el estado
del instrumento del expediente anterior —vigente, retirado o esperado-en-rojo, con su motivo—,
para que su color deje de ser un dato que sólo aparece si alguien lo ejecuta.

---

### MENOR 10 · la cuarta resta de `comprobar-cobertura-de-gate.py` es burlable por construcción, y está LATENTE en este gate

`comprobar-cobertura-de-gate.py` computa la resta que protege a las fuentes modificadas así:

```python
declarado = set(manifiesto.get("obligatorio") or []) | set(manifiesto.get("modificadas") or [])
…
modificadas = set(manifiesto.get("modificadas") or [])
…
informe["restas"]["modificadas_menos_leidas_integras"] = sorted(modificadas - leidas_integras)
```

La resta 4 se calcula **sólo desde el campo `modificadas` del manifiesto**, nunca desde el
`git diff` que el propio programa sabe derivar (`_modificadas_del_arbol`). **HECHO
REPRODUCIDO** en un repositorio sintético mío: declarando un fichero modificado bajo
`obligatorio` en vez de bajo `modificadas`, un revisor que lee 10 de sus 101 líneas produce
`COBERTURA COMPLETA · EXIT=0`.

**Está LATENTE aquí, y lo digo con la misma fuerza:** el `MANIFIESTO.json` de este gate declara
las 119 modificadas en su campo y **las 119 tienen asignación íntegra** (§3). El defecto es del
instrumento, no de este reparto. **Remedio de clase:** que la resta 4 se calcule contra
`_modificadas_del_arbol()` —lo derivado— y que la lista del manifiesto sirva sólo para
contrastarla, de modo que un manifiesto no pueda decidir de qué se le exime.

---

### OBSERVACIÓN 11 · no he recibido SOBRE DE ANCLA

`docs/evolucion/verificacion/emitir-sobre-de-ancla.py`, que leí entero, documenta que el sobre
es requisito de **todo** gate de esta familia, emitido UNA vez a un fichero **fuera del
repositorio** y entregado a cada revisor **antes de leer nada**, por un canal externo al árbol;
`C-L.5` y los once manifiestos publicados lo repiten. **Mi encargo no lo incluye y no he
recibido ninguno.**

**Qué consecuencia tiene, dicha sin inflarla.** Todo lo que he verificado sale del árbol
congelado y del `MANIFIESTO.json` que vive en el scratchpad: **no tengo ningún ancla externa
contra la que contrastar que el árbol congelado sea el commit `c2437214…`, ni que el manifiesto
sea el que se emitió antes de que yo existiera.** Lo digo como límite de mi dictamen, no como
hallazgo del árbol: el sobre es del aparato del gate y su ausencia la decide el coordinador.

---

## 5 · LO QUE **NO** HE PODIDO COMPROBAR, Y POR QUÉ

Un alcance sin declarar es el defecto que este proyecto ha visto más veces.

```text
 1 NO PUEDO CONTRASTAR EL ÁRBOL CONTRA NADA EXTERNO. No recibí sobre de ancla (§4.11) y el
   árbol congelado no lleva `.git`: no puedo verificar que sea el commit `c2437214…`, ni el
   `tree bb5b674`, ni que la sede del Owner sea el texto que el Owner emitió. Esto último es
   además la limitación TRANSITORIA que `O18` declara de sí misma.
 2 NO HE LEÍDO LOS LOTES DE `REV-2` NI DE `REV-3`, y no he visto sus dictámenes. Los ficheros
   `DICTAMEN-REV-2.md` y `DICTAMEN-REV-3.md` existen en el scratchpad y NO los he abierto: el
   encargo lo prohíbe y su valor depende de que no lo haga. Mi lote son 87 fichas · 55 204
   líneas de un universo de 209 fuentes; **una contradicción entre dos fuentes que no
   comparto con nadie es invisible para mí**.
 3 DEL DOCUMENTO 11 —`11-ARQUITECTURA-INTEGRADA.md`, 12 152 líneas— mi lote son CUATRO tramos
   de 1 200: `1-1200`, `3601-4800`, `7201-8400`, `10801-12000`. **Los leí enteros y no leí
   nada más de ese fichero.** §20 vive en `11883-12071` y §11.6 en `8329+`: los abrí sólo por
   `grep` para localizar citas, y NO los declaro leídos.
 4 `O26` y `O27` NO están en mi lote. Los leí para poder juzgar la segunda proposición —son la
   norma que fija la competencia de este gate— y lo declaro como lectura FUERA DE LOTE. Igual
   `docs/f6/00-ESTADO-DE-IMPLEMENTACION-F6.md`, `01-MATRIZ-DE-COMPLETITUD-F6.md`,
   `docs/f6/gate-definitivo/00-REGISTRO-DEL-GATE.md` y `DECISIONES-Y-CONTRADICCIONES.md`:
   abiertos por tramos, ninguno declarado íntegro, y **ningún hallazgo mío se funda ÚNICAMENTE
   en una lectura fuera de lote** — los tres que citan material ajeno (§4.2, §4.6, §4.9) tienen
   su sede probatoria en la evidencia publicada o en código de mi lote.
 5 NO HE CONSTRUIDO NINGÚN ÁRBOL ADVERSARIAL contra la batería del expediente anterior, ni he
   buscado un duodécimo árbol. `M-04` sigue siendo deuda declarada y **mi silencio no es
   evidencia en ninguna dirección**.
 6 NO HE EJECUTADO la suite `T210`–`T213` de árboles adversariales ni la raíz externa contra
   un anfitrión con contención fuerte: leí su código y su evidencia, y la corrida completa de
   los 38 validadores los cubre, pero **no los he atacado yo**.
 7 LAS TRES RESTAS `A`/`B`/`C` LAS LEÍ, NO LAS RECALCULÉ obligación a obligación. Lo que sí
   verifiqué —y es lo que sostiene §4.2— es lo que el propio instrumento publica sobre lo que
   sus ceros acreditan.
 8 `A14` es limitación aceptada y NO la cuento como hallazgo: con el `python3` 3.10 del PATH
   caen tres validadores por `tomllib`. Todo lo mío se midió con Python 3.12.14.
 9 REPRODUCIBILIDAD: WSL2, `core.quotePath` sin fijar. No probé otro intérprete, otro sistema
   de ficheros ni otra configuración de Git.
10 NO JUZGO SI LA ARQUITECTURA DE `F6` ES BUENA. Sé qué dicen sus sedes, si se contradicen y
   qué resiste cuando se ejecuta. No opino sobre el diseño y no lo insinúo.
```

---

## 6 · COBERTURA — mi resta, contra mi propio interés

```text
ASIGNADO   87 fichas · 79 fuentes distintas · 55 204 líneas
LEÍDO      79 fuentes · 55 204 líneas, con los tramos enumerados en LECTURA-REV-1.json
ASIGNADO − LEÍDO                    0 líneas · 0 fuentes
LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS    0
```

**`cerrado: true`.** Leí con `sed -n 'a,bp'` sobre el árbol congelado y anoté cada tramo al
cerrarlo, no al final de memoria.

**UNA PRECISIÓN QUE VA CONTRA MI INTERÉS Y QUE NADIE ME PIDE.** Mi lote contiene **23 ficheros `.py`**, y
**21 de ellos** llevan el prólogo `G-03`/`E-10` en torno a las líneas `31-189`. Ese prólogo es
**byte a byte el mismo MECANISMO** en todos —lo verifiqué yo: un solo digest
`aa219465a6dd6a04` sobre los 58 puntos ejecutables del árbol—, aunque su recital difiere por
sede. Lo leí íntegro en varias de ellas y, en cinco, la lectura pasó por un filtro que ocultó
entre dos y treinta renglones de ese texto ya recorrido. **Los declaro leídos** porque los
recorrí con `sed` y porque el mecanismo está verificado idéntico por digest, y **lo hago
constar aquí** para que el adjudicador lo pese en vez de descubrirlo.

---

## 7 · DISCIPLINA — declaración de cierre

```text
ÁRBOL JUZGADO          …/scratchpad/gate-congelado — SÓLO ése
/home/jose/ads-kernel   NO LEÍDO, NO TOCADO, NI UNA ORDEN
FICHEROS DE CUALQUIER ÁRBOL DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ    ninguno
ÓRDENES `git` QUE ESCRIBAN                                                        ninguna
`redesign/kernel-2.0`                                                             NO TOCADA
`fd633383…`                                                                       NO usado, NO leído, NO publicado
PesquerApp                                                                        NO arrancada
COMUNICACIÓN CON `REV-2` O `REV-3`                                                NINGUNA
                       sus dictámenes existen en el scratchpad y NO los he abierto
LABORATORIO            …/scratchpad/rev1-work/ — copias mías: `arbol/` (corrida de los 38),
                       `puerta/repo` (repositorio sintético de la resta 4), `d05/` (dos
                       evidencias alteradas), `ataque_g04.py`
INTÉRPRETE             /home/jose/.local/bin/python3.12 · Python 3.12.14
SUBAGENTE `Agent`      NO USADO
NINGÚN HALLAZGO CORREGIDO, y es deliberado: quien corrige no certifica
NINGUNA CIFRA DE ESTE DICTAMEN SIN EL COMANDO QUE LA DERIVA
UNA LECTURA MÍA RETIRADA CONTRA MI PROPIO CENSO: la proyección de `O23`–`O27` SÍ existe (§4.9)
```

---

# `F6 ESTÁ COMPLETAMENTE IMPLEMENTADA` — **NO**
# `F6 QUEDA CERTIFICADA` — **NO**

**`REV-1`, revisor independiente. NO emito veredicto de adjudicación: no es mío. NO he
propuesto ninguna corrección al repositorio y NO lo he modificado.**
