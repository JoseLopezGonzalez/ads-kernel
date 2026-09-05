# ADJUDICACIÓN · GATE DE CERTIFICACIÓN FINAL DE `F6` · 2026-09-05

```text
CANDIDATA        c2437214c9353185d6b90b8fe86178302d4cf349
TREE             bb5b674aef387dbb92485d922cd6042acbb85d69
BASE             769a8b6dfd2dd71aab69f35893da46bf35356168
ÁRBOL JUZGADO    …/scratchpad/gate-congelado   ·   `git status --porcelain` VACÍO · 252 commits
INTÉRPRETE       /home/jose/.local/bin/python3.12
LABORATORIO      …/scratchpad/adj-work/  (copias mías: `arbol/`, `suite/`, `puerta/repo`)
```

Se me crea después de que los tres revisores hayan cerrado. No he visto nada de su trabajo
hasta ahora, y ellos no me han visto a mí. **No he corregido nada, no he escrito en ningún
árbol del repositorio y no he ejecutado ninguna orden `git` que escriba.** Todo lo que exigía
escribir se hizo sobre copias mías, y cada una vuelve a `git status --porcelain` vacío al
terminar el experimento.

---

## 1 · ¿ES VÁLIDO EL GATE? — **SÍ, por cobertura**

No lo doy por bueno porque lo diga el coordinador. Lo he vuelto a medir yo, con el instrumento
del árbol congelado, sobre los tres manifiestos de lectura.

```console
$ /home/jose/.local/bin/python3.12 gate-congelado/docs/evolucion/verificacion/comprobar-cobertura-de-gate.py \
      --manifiesto MANIFIESTO.json --lectura LECTURA-REV-1.json LECTURA-REV-2.json LECTURA-REV-3.json \
      --raiz gate-congelado
COBERTURA DEL GATE · candidata c2437214c9353185d6b90b8fe86178302d4cf349
  ORIGEN DEL CONJUNTO OBLIGATORIO · derivada-del-arbol
           base 769a8b6dfd2d · candidata c2437214c935 · rutas derivadas del árbol: 119
  REV-1    asignadas  87 · leídas sin hueco  87 · sin abrir   0 · con huecos   0
           líneas asignadas  55204 · sin leer      0 · cerrado declarado: sí
  REV-2    asignadas  86 · leídas sin hueco  86 · sin abrir   0 · con huecos   0
           líneas asignadas  55203 · sin leer      0 · cerrado declarado: sí
  REV-3    asignadas  86 · leídas sin hueco  86 · sin abrir   0 · con huecos   0
           líneas asignadas  55208 · sin leer      0 · cerrado declarado: sí
  OBLIGATORIO − ASIGNADO                 ∅
  ASIGNADO − LEÍDO                       ∅
  LÍNEAS ASIGNADAS − LÍNEAS LEÍDAS       ∅
  FUENTES MODIFICADAS − LEÍDAS ÍNTEGRAS  ∅
  COBERTURA COMPLETA
EXIT=0
```

**Y no me he quedado en la salida.** Un instrumento verde sobre un manifiesto amañado no mide
nada, y la cuarta resta de este programa es amañable (§3, hallazgo `R1-10`, que confirmo). Lo
que he comprobado a mano, y es lo que sostiene la validez:

```console
$ (derivación propia con `git diff --name-status -M -C -z 769a8b6 c2437214` sobre el congelado)
derivado del árbol      119
declarado `modificadas` 119
derivado − modificadas  []
modificadas − derivado  []
```

Es decir: **el campo `modificadas` del manifiesto —el único que alimenta la cuarta resta— es
exactamente el conjunto derivado del árbol, ni una ruta de menos.** La cuarta resta opera
sobre 119 rutas reales y sale vacía, de modo que las 119 fuentes que el corte modificó están
leídas ÍNTEGRAS por un solo revisor cada una, sin delegación y sin compensación entre lotes.
La puerta que el instrumento deja abierta **no está usada aquí**, y lo he verificado en vez de
suponerlo.

Y el propio instrumento pasa sus autopruebas sobre el árbol congelado:

```console
$ … comprobar-cobertura-de-gate.py --autopruebas --raiz gate-congelado
  26 controles · 0 sin detectar        EXIT=0
```
—incluidos los tres controles de `G-07` sobre un repositorio Git REAL y las dos puertas
traseras que el auditor independiente abrió.

**Conclusión de validez.** `O27` §5 condiciona la llegada a adjudicación a que `ASIGNADO −
LEÍDO` sea vacío para todo revisor. Lo es, para los tres, y las otras tres restas también.
**El gate es VÁLIDO por cobertura y adjudica.** Es lo primero de este expediente que hay que
decir sin rebaja: los dos gates anteriores cayeron aquí —seis fuentes sin abrir el 2026-09-03;
50 de 84 ficheros y el 60,9 % de las líneas el 2026-09-04— y **éste no cae**.

### 1 bis · Lo que NO acredita esta validez, dicho sin redondear

```text
1  NO HAY SOBRE DE ANCLA. `emitir-sobre-de-ancla.py` —que vive en el árbol y lo he leído—
   documenta que el sobre se emite UNA vez, fuera del repositorio, y se entrega a cada revisor
   DENTRO de su encargo y ANTES de leer nada. El `ENCARGO-REVISOR.md` de este gate no lo
   incluye, ningún revisor lo recibió y no existe ningún sobre en el scratchpad de esta sesión
   (`find … -iname "*ancla*" -o -iname "*sobre*"` → vacío; los que hay son de gates anteriores,
   en otras sesiones). **Consecuencia exacta:** nada externo al árbol ancla que el congelado
   sea `c2437214…`, ni que el `MANIFIESTO.json` sea el emitido antes de crear a los revisores.
   Lo comprobado es interno: el congelado dice de sí mismo `HEAD = c2437214…`,
   `HEAD^{tree} = bb5b674…`, `status` vacío y 252 commits de historia.
   **ES DEFECTO DEL COORDINADOR**, no de la candidata, y así lo consigno.
2  LA CUARTA RESTA DEL INSTRUMENTO ES AMAÑABLE POR CONSTRUCCIÓN (§3 · `R1-10`, reproducido
   por mí). Aquí está LATENTE y verificado inerte, pero el gate SIGUIENTE no tiene por qué
   estarlo. También es del instrumento del coordinador.
3  EL INSTRUMENTO MIDE DECLARACIONES DE TRAMOS, no lectura humana. Casa el SHA-256 de cada
   fuente contra el árbol y hace la aritmética de cobertura línea a línea; no puede probar que
   un tramo declarado se haya comprendido. `REV-1` declara por su cuenta —contra su propio
   interés— que en cinco ficheros un filtro de pantalla le ocultó entre dos y treinta renglones
   del prólogo `G-03`/`E-10` ya recorrido. Lo peso como él pide: el mecanismo está verificado
   idéntico por digest en los 58 puntos, el recorrido fue con `sed`, y no muevo su resta.
4  `REV-3` DECLARA UNA DESVIACIÓN: ejecutó `git checkout -- kernel/KERNEL.md` dentro de SU
   copia de experimentos. El encargo lo prohíbe. La declara él mismo, en su §4.2, con la fecha
   y el remedio (desde entonces restaura con `cp` y verifica `sha256sum` y `status` vacío).
   No afecta al árbol congelado, no afecta a ninguna reproducción posterior suya —las he
   rehecho yo por mi cuenta— y **no invalida su lote ni su dictamen**. Se registra.
```

---

## 2 · LA LÍNEA BASE DEL COORDINADOR — reproducida por mí, y CIERTA

Los tres revisores la reproducen entera y ninguno encuentra un número falso. Yo tampoco. La
he vuelto a medir sobre el árbol congelado y sobre una copia mía:

| línea | ¿reproduce? | medido por mí |
|---|---|---|
| `38/38 validadores en verde · 38 evidencias · 0 problemas` | **SÍ** | corrida completa de `registrar_evidencia.py` sobre `…/adj-work/suite` — **y más que eso: ver el recuadro** |
| `170 infracciones detectadas · 0 NO detectadas` | **SÍ** | `negativos-salida.txt:347` |
| `582 bloques canónicos · 0 errores · 0 avisos` | **SÍ** | `lint-salida.txt:7` |
| `314 escenarios · 254 contrastados · 0 divergencias · 0 en prueba-ejecutada` | **SÍ** | `grep -c '^| \[T' REGISTRO-generado.md` → 314 · mi corrida de `comprobar_evidencia.py` → `contrastados 254 · no contrastables 60 · divergencias 0` · `grep -c prueba-ejecutada` → 0 |
| `58 obligaciones · A=0 · B=0 · C=0` | **SÍ** | `derivar-universo-obligatorio.py --obligaciones` → `TOTAL 58`, las tres restas a cero |
| `58 puntos ejecutables · 58 con guarda · 0 sin guarda` | **SÍ** | `inventariar_el_arbol()` del propio corpus |
| `huella 854dfa1b99be3824 · almacenada = calculada · estable en dos cálculos` | **SÍ** | dos cálculos consecutivos, mismo valor; `kernel/.upstream-hash` idéntico |

**Y hay un hecho que va MÁS ALLÁ de lo que la línea base afirma, y que mide por sí solo lo que
esta candidata sí ha conseguido.** Lancé la suite entera sobre una copia PRISTINA del árbol
congelado y comprobé después qué había quedado escrito:

```console
$ /home/jose/.local/bin/python3.12 kernel/operativo/validadores/registrar_evidencia.py   # sobre …/adj-work/suite
38/38 validadores en verde · 38 evidencias publicadas · 0 problemas
EXIT=0

$ git -C …/adj-work/suite status --porcelain        # tras publicar las 38 evidencias
(vacío)
$ diff -rq …/adj-work/suite/kernel/operativo/pruebas/evidencia \
           …/gate-congelado/kernel/operativo/pruebas/evidencia
SIN DIFERENCIAS
```

**La evidencia publicada en la candidata no es una captura antigua: es, byte a byte, lo que el
código produce hoy, y la corrida es determinista hasta el punto de no ensuciar el árbol.**
`REV-1` lo afirmó y lo he reproducido por mi cuenta.

**Las siete líneas son verdaderas.** Hay que decirlo antes que nada de lo que sigue, porque es
lo que separa a esta candidata de las anteriores: **no hay una sola cifra falsa en la línea
base.** Lo que falla no es la veracidad de los números; es lo que los números acreditan y lo
que el árbol declara cerrado sin estarlo.

---

## 3 · HALLAZGOS VERIFICADOS, UNO A UNO

Los tres revisores traen **27 hallazgos**. Los he reproducido todos con la orden que cada uno
da. Resultado global: **27 confirmados en su hecho central · 0 rechazados por entero ·
4 sub-afirmaciones rechazadas · 5 cifras o referencias corregidas.** Tres se solapan entre
revisores (nº 2 = nº 22; nº 4 = nº 15 = nº 24; nº 7 = nº 16), de modo que los **defectos
distintos son 23** — y que tres revisores sin verse encuentren el mismo tres veces es, en sí
mismo, un dato sobre lo que el árbol publica de sí.

### 3.1 · Tabla

| # | revisor · id | hecho | veredicto |
|---|---|---|---|
| 1 | `REV-1` GRAVE 1 | `G-04`: la invariante de `b.12` es evadible en DOS transiciones por el canal oficial | **CONFIRMADO** — reproducido íntegro |
| 2 | `REV-1` GRAVE 2 | `A=0·B=0·C=0` no acredita `O26` §5.1/§5.2, y nada más lo acredita | **CONFIRMADO** en lo que decide · framing corregido (§3.3) |
| 3 | `REV-1` GRAVE 3 | el contraste contra `HEAD` (`D-05`) no alcanza a 6 de las 38 evidencias | **CONFIRMADO** — reproducido, incluido el ataque |
| 4 | `REV-1` MOD 4 | §5 de la matriz publica `23 controles` y `56 de 56`; §6 registra `26` y `58` | **CONFIRMADO** |
| 5 | `REV-1` MOD 5 | el cardinal del inventario no lo publica ninguna evidencia; las sedes dicen «nueve» y «56» | **CONFIRMADO** |
| 6 | `REV-1` MOD 6 | «veintiún pasos» sobrevive en la sede normativa y en su derivado; se declaró «corregida» | **CONFIRMADO** |
| 7 | `REV-1` MOD 7 | cinco sedes afirman en presente que doce escenarios «han BAJADO a `prueba-ejecutada`» | **CONFIRMADO** |
| 8 | `REV-1` MEN 8 | «1 869 bytes» escrito 23 veces; el mecanismo son 1 879 | **CONFIRMADO** |
| 9 | `REV-1` MEN 9 | la batería del expediente anterior está en ROJO (`32/38`) y ninguna sede lo publica | **CONFIRMADO · y AGRAVADO** (§3.3) |
| 10 | `REV-1` MEN 10 | la cuarta resta del comprobador es amañable por construcción; LATENTE aquí | **CONFIRMADO** — reproducido en repositorio sintético |
| 11 | `REV-1` OBS 11 | no se emitió sobre de ancla | **CONFIRMADO** — y es del coordinador |
| 12 | `REV-2` GRAVE 1 | `M-04` está declarada **NO SUPERADA**, fase `F6`, y las tres restas la cuentan en verde | **CONFIRMADO** |
| 13 | `REV-2` GRAVE 2 | `C-L.7` sigue **NO CERRADA** con componente de fase `F6`, fuera de toda resta | **CONFIRMADO** |
| 14 | `REV-2` GRAVE 3 | la sede que declara todo cerrado está fuera del universo obligatorio y de la huella | **CONFIRMADO en parte** · dos sub-afirmaciones **RECHAZADAS** (§3.3) |
| 15 | `REV-2` SERIO 1 | el cardinal `56` caducado en tres sedes, una de ellas el `entonces:` de `T380` | **CONFIRMADO** · sub-afirmación 3 **RECHAZADA** (§3.3) |
| 16 | `REV-2` SERIO 2 | cinco sedes declaran en presente un estado de escenario que el árbol no tiene | **CONFIRMADO** (= nº 7) |
| 17 | `REV-2` MOD 1 | `D-03` relaja el régimen de integridad del material APROBADO, y nada lo cubre | **CONFIRMADO** |
| 18 | `REV-2` MOD 2 | prosa caducada dentro del módulo que aplica el remedio (`vigilar_append_only`) | **CONFIRMADO** · distancia corregida |
| 19 | `REV-2` MEN 1 | el manifiesto del gate anterior prohíbe que exista este gate; no consta acto que lo levante | **CONFIRMADO** como texto |
| 20 | `REV-3` H1 | la sede del Owner es el único sitio cuyo CONTENIDO EN DISCO nadie juzga | **CONFIRMADO** — con su control del control · acotado (§3.3) |
| 21 | `REV-3` H2 | la huella no cubre `docs/`: ni la sede del Owner ni la matriz de cierre | **CONFIRMADO** |
| 22 | `REV-3` H3 | ninguna medida de la candidata mide `O26` §5.1 ni §5.2 | **CONFIRMADO** (= nº 2) |
| 23 | `REV-3` H4 | la comprobación 3 de `comprobar_integridad.py` está declarada y no está escrita | **CONFIRMADO** · cardinal corregido |
| 24 | `REV-3` H5 | §5 de la matriz publica dos cardinales que su propio §6 corrige | **CONFIRMADO** (= nº 4) |
| 25 | `REV-3` H6 | sobrevive una segunda definición de «append-only», la del PREFIJO, en `validar-f5.py` | **CONFIRMADO** |
| 26 | `REV-3` H7 | la equivalencia «`#!` ⟺ INVOCABLE» declarada es falsa para 80 ficheros, y `T330b` los EXIGE | **CONFIRMADO** |
| 27 | `REV-3` H8 | `RETIRADAS_DE_LA_RUTA` se asigna dos veces en `negativos_runtime.py` | **CONFIRMADO** · cardinal corregido |

### 3.2 · Las tres reproducciones que deciden, con su orden y su salida

**(A) `G-04` es evadible en dos transiciones — `REV-1` GRAVE 1.** El árbol declara esta fila
**CERRADA** en `docs/f6/05-MATRIZ-CIERRE-G01-G08.md` §5: «*la prioridad de un paquete existente
no se mueve en ninguna transición del runtime*». Corrí el guión de `REV-1` sobre MI copia,
usando `rt.almacen` —el `AlmacenVigilado`, que es el canal oficial—:

```console
$ /home/jose/.local/bin/python3.12 ataque_g04.py
prioridad inicial: 50
--- control: intento DIRECTO 50 -> 999 (debe caer) ---
  RECHAZADO: PRIORIDAD_INMUTABLE
--- PASO 1: BORRAR el campo `prioridad` ---
  CONFIRMADO. paquete durable tiene prioridad?: False
--- PASO 2: volver a ESCRIBIR prioridad = 999 ---
  CONFIRMADO. prioridad durable AHORA: 999
```

La causa es del código, `runtime/estado_util.py:169-172`: `if campo not in anterior or campo
not in contenido: continue`. El paso 1 pasa por la segunda mitad, el paso 2 por la primera.
Verifiqué además las dos cosas que `REV-1` afirma y que sostienen el hallazgo:
`comprobar_paquete` —que sí rechazaría el objeto sin campo— **no lo llama `Almacen.aplicar`**:
sólo aparece en `dispatcher.py` y `vistas.py`, caminos de LECTURA; y **ninguna prueba del árbol
borra el campo** (`grep` de `pop("prioridad"` sobre `kernel/` → vacío).

**Y hay una corroboración que agrava, y que sale del propio documento que se juzga.** §6 de la
matriz escribe, entre lo que el auditor independiente «*dio por bien cerrado sin reservas*»:
«`G-04` —*reinsertó el sabotaje exacto de `R1-H02` y salió `[PRIORIDAD_INMUTABLE] … de 50 a
60`*—». Es decir: el único sabotaje que se le opuso fue **el salto directo**, que es el caso
fácil. **Una propiedad cuyo único sabotaje es el caso que no la derrota no está probada.**

**(B) La sede del Owner se reescribe y los cuatro sellos siguen verdes — `REV-3` H1 y H2.**
Sobre mi copia, cambié el TÍTULO de `O26` —la resolución que otorga competencia a este gate—
por su contrario:

```console
$ git status --porcelain
 M docs/owner/ADS-OWNER-RESOLUCIONES.md
$ … ads_admision.py --repo . verificar --base 769a8b6      # SANO:      mutaciones 119 · hallazgos 119
$ … ads_admision.py --repo . verificar --base 769a8b6      # ALTERADO:  mutaciones 120 · hallazgos 119
$ … ads_admision.py … | grep -c "ADS-OWNER-RESOLUCIONES"
0
$ … huella.py --raiz .            854dfa1b99be3824   (= kernel/.upstream-hash)
$ … validar-f5.py | grep append   append_only : contra 1d3b5d41: OK
$ … comprobar_integridad.py       T150  SUPERADA · 1 superadas · 0 fallidas
```

**El verificador VE la mutación —119 → 120— y no la JUZGA: los hallazgos se quedan en 119.** Y
el control del control confirma que el juez es correcto y el canal no: alimentando
`sede.juzgar` con los bytes del disco,

```console
juicio sobre los bytes de HEAD  : []
juicio sobre los bytes del DISCO: ('ENTRADA_ALTERADA', 'O26',
  'la entrada `O26` no coincide BYTE A BYTE con la que se introdujo en el commit
   6db4605b7f67 (3317 bytes → 3306 bytes)…')
```

La causa está en `admision/__init__.py:108-111`: `actual = canal.contenido("HEAD", ruta)`, y
sólo si `HEAD` no tiene el fichero se miran los bytes del disco. Y en `perimetro.py:366-371`
la sede sale por su rama con `continue`, de modo que tampoco cae en `INMUTABLE`/`DECLARADA`,
que son las que sí contrastan el árbol de trabajo **en las otras 29 zonas**. `AMBITOS =
("kernel", "packs", "tooling")` (`huella.py:209`) deja `docs/` entero fuera del sello.

**(C) Seis evidencias fuera del contraste, y dos editadas en verde — `REV-1` GRAVE 3.**

```console
$ (derivando los escenarios con `Lint` igual que hace `comprobar_evidencia.py`)
escenarios: 314 · evidencias publicadas: 38 · citadas por escenarios: 32
NO citadas por ningún escenario: ['cobertura-de-gate-salida.txt', 'lint-salida.txt',
 'negativos-salida.txt', 'universo-obligaciones-salida.txt', 'universo-obligatorio-salida.txt',
 'universo-rutas-salida.txt']
```

Las seis que quedan fuera publican **cuatro de las siete líneas de la línea base**. Y la
consecuencia se mide, no se argumenta: edité `582→9` en `lint-salida.txt` y `170→3` en
`negativos-salida.txt`, sobre mi copia, y

```console
T158  SUPERADA  La evidencia publicada demuestra lo que el informe afirma
T350  SUPERADA  El estado declarado de cada escenario lo sostiene su evidencia
          cobertura del contraste: … divergencias 0 · contraste contra el blob de HEAD: EJERCIDO
EXIT=0
T150  SUPERADA  (la huella no se mueve: las evidencias no entran en ella)
```

«EJERCIDO» sin cardinal, sobre 32 de 38, y las 6 descubiertas son justamente las que ningún
escenario sostiene por otra vía.

### 3.3 · Lo que RECHAZO, con su motivo

Ningún hallazgo cae entero. Caen cuatro sub-afirmaciones y cinco cifras. Se registran porque
un adjudicador que sólo suma cargos no adjudica.

```text
RECHAZO 1 · `REV-2` GRAVE 3 · «`05-MATRIZ-CIERRE-G01-G08.md` … no tiene fila de manifiesto:
   ningún revisor está obligado a leerlo».  ES FALSO Y LO MIDO:
     MANIFIESTO.json → REV-1 · docs/f6/05-MATRIZ-CIERRE-G01-G08.md · 153 líneas · rango None
     LECTURA-REV-1.json → leído [[1, 153]]
     y la ruta figura ADEMÁS en el campo `modificadas`, de modo que la CUARTA resta le exige
     lectura íntegra por un solo revisor — y sale vacía.
   El documento que este gate manda atacar estaba asignado y se leyó entero. `REV-2`
   generalizó desde su propio lote —donde en efecto no estaba— a todo el gate.

RECHAZO 2 · `REV-2` GRAVE 3 · «… y del sobre».  NO SOSTIENE NADA: no se emitió sobre de ancla
   para NINGUNA fuente de este gate (§1 bis). El renglón no distingue a `docs/f6` de
   `kernel/`, y por tanto no prueba la asimetría que el hallazgo alega.

RECHAZO 3 · `REV-2` SERIO 1, punto 3 · «`T360` no alcanza a `docs/f6`».  ES FALSO:
     comprobar_recuentos.py:442  (r"^docs/f6/", "el registro VIVO de `F6`…")   ← AMBITO_VIVO
   y `05-MATRIZ-CIERRE-G01-G08.md` no casa con ninguno de los dos patrones de
   `FUERA_DEL_AMBITO` (que sólo excluyen las actas `\d\d-GATE-…-\d{8}.md` y las matrices de
   hallazgos fechadas). `T360` SÍ barre esa sede. Lo cierto es lo otro: la barre y **no ve**
   estos cardinales, porque `T360` juzga que ninguna sede viva NIEGUE una pieza construida, y
   un cardinal caducado no niega nada. El hecho del hallazgo se sostiene; su causa mecánica,
   no. La corrección importa porque el remedio que `REV-2` propone —meter la zona en el
   perímetro— ya está aplicado y no habría cerrado nada.

RECHAZO 4 · `REV-1` MENOR 9, su ATENUANTE · «`G-23`, `G-29` y `G-30` fallan CERRADO por falta
   de `.git` en mi copia, y no los cuento».  NO SE SOSTIENE, Y VA CONTRA LA CANDIDATA:
   mi copia SÍ tiene `.git` con las 252 revisiones de historia, y los tres siguen fallando con
   detalle sustantivo —`G-23`: el checkpoint no enumera los ficheros del kernel tocados;
   `G-29`: ampliación no clasificada del corpus gobernado (`docs/f5/00-INDICE-F5.md`,
   `docs/f5/01-ACTO-DE-INICIO-DE-F5.md`, …); `G-30`: cabeceras de evidencia que su productor
   no escribió—. La batería publica **32/38 · EXIT=1** con SEIS fallos sustantivos, no tres.
   `REV-1` fue más benévolo con la candidata de lo que los hechos permiten.

CORRECCIONES DE CIFRA (el hallazgo se sostiene; el número, no)
   · `REV-3` H4: `IMPRESCINDIBLES` tiene NUEVE entradas, no diez.
   · `REV-3` H8: son SIETE los puntos que publican `entradas_del_lanzador_retiradas`, no seis.
   · `REV-3` H2: `AMBITOS` está en `huella.py:209`, no en `:208`.
   · `REV-2` MOD 2: `APROBADA_POR_ENMIENDA` se declara 326 líneas más arriba (`:106` frente a
     `:432`), no «30 líneas más arriba».
   · `REV-1` GRAVE 2, el FRAMING: «la sede pivotal se contradice consigo misma». Con precisión:
     `01-MATRIZ-DE-COMPLETITUD-F6.md` §2.6 (L207-213) escribe la equivalencia
     `O26 §5.1 → RESTA A`, y la frase que la niega (L375) vive DENTRO de una cita en bloque que
     REGISTRA la lección del gate del 2026-09-03, no en la voz propia del documento; y la
     oración operativa de §2.6 enuncia sólo una condición NECESARIA («mientras las tres no
     estén vacías … `F6` no se certifica»). La tensión textual existe y es real, pero es más
     débil de lo que el hallazgo la presenta. **Lo que decide no es la contradicción entre dos
     párrafos: es que el INSTRUMENTO publica hoy, pegado a sus propios ceros, que no demuestran
     `O26` §5.1 ni §5.2 — y eso lo he reproducido.**

ACOTACIÓN, no rechazo · `REV-3` H1. El agujero está acotado al ÁRBOL DE TRABAJO. Una
   alteración COMETIDA sí entra por `canal.contenido("HEAD", ruta)` y `sede.juzgar` la caza
   —lo verifiqué alimentándolo con esos bytes—, y `O27` §4 manda que la validación se ejecute
   sobre un checkout congelado del SHA, donde `HEAD` y disco coinciden. **Nada de lo que este
   gate midió está contaminado por ese hueco.** Lo que no se salva es la propiedad: `V6-12`
   dice juzgar el contenido de la sede y no lo juzga donde el resto del verificador sí juzga,
   y `M-04` —«un árbol defectuoso puede pasar en verde»— es obligación viva de este mismo
   universo. `REV-3` lo declaró él mismo como límite en su §4.1, y acierta al presumirlo.
```

### 3.4 · Contradicciones entre dictámenes

**No hay ninguna.** Los tres coinciden en las dos proposiciones y en el sentido de todo lo que
se solapa. Donde tres se solapan —`A/B/C` no acredita `O26` §5.1/§5.2 (`R1-2`, `R3-H3`, y la
tabla de `REV-2` §1(b))— los tres lo derivan de la misma salida del instrumento, y la salida
la he reproducido yo. Donde se solapan dos —los cardinales `23`/`56` de §5 (`R1-4`, `R2-S1`,
`R3-H5`) y las cinco notas «han BAJADO» (`R1-7`, `R2-S2`)— coinciden en el hecho y difieren
sólo en la gravedad asignada; **resuelvo por la medición, no por la autoridad**: son defectos
de VERACIDAD DE SEDE sobre propiedades que el árbol SÍ tiene construidas (58 puntos, 58 con
guarda, 0 sin guarda; 26 controles, 0 sin detectar), y por tanto no tumban ninguna propiedad
—los gradúo SERIOS, con la agravante de que una de las sedes falsas es la fila `G-03` del
documento que declara el cierre y otra es el `entonces:` de `T380`, su condición de aceptación.

Las tres divergencias de gravedad, resueltas:

```text
· «56 de 56» y «23 controles»:  REV-1 MODERADO · REV-2 SERIO · REV-3 SERIO   →  SERIO.
  La propiedad de fondo NO está rota. Lo que está roto es la veracidad de la sede que la
  publica, y una de ellas es la condición de aceptación de la prueba que la mide.
· «han BAJADO a prueba-ejecutada»: REV-1 MODERADO · REV-2 SERIO  →  MODERADO.
  La subida de estado es legítima y está contrastada (254 contrastados · 0 divergencias);
  lo falso es sólo la prosa que la explica, y no sostiene ninguna garantía.
· la batería del expediente anterior:  REV-1 MENOR  →  se mantiene MENOR en gravedad, pero
  con el alcance corregido (RECHAZO 4): seis fallos, no tres, y ninguna sede publica su rojo.
```

---

## 4 · LAS DOS PROPOSICIONES, ADJUDICADAS POR SEPARADO

```text
  ┌────────────────────────────────────────────────────────────────────────────┐
  │   `F6 ESTÁ COMPLETAMENTE IMPLEMENTADA`   ·   NO                            │
  │   `F6 QUEDA CERTIFICADA`                 ·   NO                            │
  └────────────────────────────────────────────────────────────────────────────┘
```

Se responden por separado y las razones no se mezclan. **Si mañana cayera la primera razón, la
segunda seguiría en pie por sí sola, y al revés.**

### 4.1 · `F6 ESTÁ COMPLETAMENTE IMPLEMENTADA` — **NO**

No por lo que falta de medir, sino por lo que **está declarado cerrado y no lo está**, y lo he
reproducido yo:

1. **`G-04` se declara CERRADO en §5 de la matriz de cierre y su invariante es evadible en dos
   transiciones ordinarias por el canal oficial** (§3.2 A). Una de las ocho condiciones que la
   candidata afirma haber cerrado no está cerrada, y el único sabotaje que se le opuso —el que
   §6 registra— es el caso que no la derrota.
2. **`V6-12` no juzga el contenido de la sede del Owner allí donde el mismo verificador juzga
   las otras 29 zonas** (§3.2 B). Es obligación del universo de 58 y sale con `A=B=C=0`.
3. **La comprobación 3 de `comprobar_integridad.py` está declarada en la cabecera del módulo y
   no está escrita**: bajo su propio rótulo «sensible al contenido y a la ruta» hay
   `if huella.calcular(base) != calculada` —dos cálculos del MISMO árbol—, y su mensaje de
   fallo confiesa que mide determinismo. Es una de las dos defensas que la cabecera declara
   contra estrechar la huella, y el estrechamiento que ninguna de las dos ve —`docs/` entero
   fuera del ámbito— es el hallazgo 21.
4. **La propia sede canónica lo dice.** `docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md` §3
   titula «`M-04` — la deuda que **bloquea `F6`**», y publica `ESTADO **NO SUPERADA**`, `FASE
   **F6**`, «*QUÉ LA CIERRA: que `F6` implemente TODOS los puntos del contrato del verificador
   **y los EJECUTE***». Y `C-L.7` sigue `NO CERRADA` con componente de fase `F6`, con población
   que ha CRECIDO dentro de esta misma candidata (`KD-02`, `LE-02`, `OC-1`).

**Una fase cuya propia sede de deuda declara no superada la obligación que la bloquea, y tres
de cuyas piezas declaradas cerradas no lo están cuando se las ataca, no está completamente
implementada.**

### 4.2 · `F6 QUEDA CERTIFICADA` — **NO**

`O26` §5 concede la competencia de declarar `F6 CERTIFICADA` sólo a un gate VÁLIDO que
demuestre **simultáneamente** cinco cosas. Este gate ES válido (§1) y **no puede demostrar
tres de las cinco**:

| condición de `O26` §5 | adjudicación | por qué |
|---|---|---|
| 5.1 no quedan obligaciones internas de `F6` sin implementar | **NO DEMOSTRADA** | `A=0` mide TRAZABILIDAD DECLARADA. **Lo publica el propio instrumento, pegado a la cifra**: «*Un `cubre` es una declaración escrita, y este aparato no sabe si lo declarado está construido*». Ninguna otra medición del árbol lo suple |
| 5.2 no quedan propiedades críticas sin una prueba capaz de fallar | **NO DEMOSTRADA** | `B=0` mide EXISTENCIA DE AL MENOS UN SABOTAJE. El instrumento cita su propio contraejemplo (`V6-12`), **que sigue vivo hoy y es el hallazgo 20**. Y hay un segundo, medido por mí: `G-04` tiene sabotaje —el salto directo— y la propiedad se derrota por otro camino |
| 5.3 trazabilidad hasta evidencia ejecutable | **SÍ, en el sentido acotado que `C` mide** | 58/58 con fichero de evidencia presente. Y con la salvedad medida del hallazgo 3: seis de las 38 evidencias no las contrasta nadie contra `HEAD` |
| 5.4 la implementación satisface las OCHO condiciones de `O26` §1 | **NO ACREDITADA** | ninguno de los tres revisores las ejerció, y yo tampoco: exigen contenedor, identidad de sistema separada y proveedor de firma, y `E-18` declara que `cgroup v2` no es ejercitable en este anfitrión. Que la evidencia las afirme y que `T217`–`T220`, `T290`–`T296` y `T330`–`T337` salgan SUPERADAS **no las convierte en demostradas**, y `O26` §2 exige demostrarlas «sobre su SHA exacto» |
| 5.5 no existen bloqueantes internos vivos | **NO** | `M-04` **NO SUPERADA**, fase `F6`, «bloquea `F6`». `C-L.7` **NO CERRADA**, componente `F6`. Ambas en la sede canónica de deuda, ambas dentro de esta candidata |

**Con §5.1, §5.2, §5.4 y §5.5 sin demostrar, la competencia que `O26` §5 concede no se activa,
y ningún hallazgo mío hace falta para llegar ahí: basta con leer lo que el árbol publica de sí
mismo.** `O26` §8 fija la consecuencia y la aplico sin añadir nada:

> **la aceptación arquitectónica PERMANECE, `F6` sigue ABIERTA y PesquerApp sigue BLOQUEADA.**

Y una advertencia que este expediente ya ha pagado dos veces: **certificar sobre `A=0 · B=0 ·
C=0` sería emitir la «promesa de seguridad superior a la realmente entregada» que `O18`
prohíbe.** Los ceros son verdaderos. No miden lo que sus rótulos prometen, y el instrumento lo
dice él mismo en la salida que este gate reproduce.

---

## 5 · LO QUE CONSTA A FAVOR DE LA CANDIDATA

Un dictamen que sólo acumula cargos no es una adjudicación. Esto es lo que he verificado yo y
que no cae:

```text
1  LA LÍNEA BASE ES ENTERAMENTE VERDADERA. Las siete líneas. Tres revisores independientes la
   reprodujeron y ninguno encontró un número falso; yo tampoco. En un expediente donde un gate
   anterior midió «160 contrastados» sobre un árbol que producía 193, esto no es poco: es lo
   contrario de lo que hundió a las candidatas anteriores.

1 bis  Y POR ENCIMA DE LA LÍNEA BASE: la corrida completa de los 38 validadores sobre una copia
   pristina deja el árbol con `git status --porcelain` VACÍO y el directorio de evidencia
   `SIN DIFERENCIAS` contra el congelado. La evidencia publicada es, byte a byte, lo que el
   código produce hoy. Es la única forma honesta de que una evidencia signifique algo, y esta
   candidata la tiene.

2  EL GATE ES VÁLIDO, Y SU MANIFIESTO ES EL MÁS LIMPIO DEL EXPEDIENTE. Lo he medido: 119 rutas
   derivadas del árbol = 119 declaradas `modificadas`, sin una ruta de diferencia; **259 fichas
   de asignación sobre 209 rutas distintas, las 259 con SHA-256 declarado y las 259 casando
   con el árbol congelado** —y las 237 entradas de los tres manifiestos de lectura, igual:
   `sin sha256: 0 · que NO casan: 0`—; ningún rango que exceda su fichero
   —que es exactamente lo que mató al gate del 2026-09-05—; ninguna línea del universo
   obligatorio sin asignar; y las 119 modificadas leídas ÍNTEGRAS por un solo revisor cada una.
   Los tres lotes cierran a ∅ y los tres declaran `cerrado: true` con la resta verificada.

3  LOS INSTRUMENTOS DEL GATE PASARON SUS PROPIAS AUTOPRUEBAS SOBRE ESTE ÁRBOL: 26 controles ·
   0 sin detectar, incluidos los tres nuevos de `G-07` sobre un repositorio Git REAL —`M`, `A`,
   `D`, renombrado, copia, ruta no ASCII y ruta con salto de línea— y las DOS puertas traseras
   que el auditor independiente había abierto. `G-01`, `G-02` y `G-07` están cerrados de
   verdad, y lo he ejercitado yo, no leído.

4  LA HONESTIDAD DE LOS RÓTULOS ES UN MÉRITO, NO UN DEFECTO. El derivador publica, en su propia
   salida y pegado a sus ceros, qué NO demuestra cada resta, con su contraejemplo nombrado. Es
   la razón por la que el hallazgo que decide la segunda proposición se puede escribir con la
   salida del propio instrumento en vez de con una opinión. Muy pocos aparatos hacen esto.

5  EL CONTROL POSITIVO DE LA INVARIANTE FUNCIONA. El salto directo `50 → 999` se RECHAZA con
   `PRIORIDAD_INMUTABLE`, y por eso la fila `G-04` se pudo escribir de buena fe. Lo que falla es
   el alcance de su sabotaje, no la existencia de la guarda.

6  EL JUEZ DE `O27` §3 ES CORRECTO. `sede.juzgar` acierta a la primera sobre los bytes
   alterados y emite `ENTRADA_ALTERADA` con el commit, el identificador y el delta de bytes.
   El defecto del hallazgo 20 está en el CANAL que le entrega los bytes, no en el juicio.

7  EL ESCENARIO `T225` ES REAL: 24 pasos, 1 905 líneas, repositorios Git de verdad, dos
   procesos, claves Ed25519 efímeras fuera de todo repositorio, caída inyectada y cuatro
   controles negativos en el paso 24. Verificado el cardinal contra la evidencia: `24 de 24
   pasos CUMPLIDOS`.

8  EL CATÁLOGO NEGATIVO DECLARA EL DIAGNÓSTICO ESPERADO (`espera=…`), no sólo que la prueba
   falle: sin eso, una prueba se daría por detectada por fallar, sin comprobar que falló POR
   ESO. 170 infracciones detectadas · 0 NO detectadas.

9  NINGUNA OBLIGACIÓN DEL UNIVERSO QUEDA CUBIERTA SÓLO POR ESCENARIOS NO SUPERADOS. Lo midieron
   dos revisores por separado y lo he cruzado yo: 254 escenarios en PRUEBA SUPERADA, 0 en
   PRUEBA EJECUTADA, 0 divergencias. (Con la salvedad del hallazgo 22: cinco obligaciones se
   apoyan EN PARTE en `T277` y `T352`, que están en `validador-implementado`.)

10 EL INVENTARIO DE AISLAMIENTO ESTÁ BIEN: 58 puntos ejecutables · 58 con guarda · 0 sin
   guarda, con el MECANISMO idéntico byte a byte —un solo digest `aa219465a6dd6a04` sobre los
   58—. La propiedad de fondo NO está rota en ninguno de los hallazgos 4, 5 y 15: lo que está
   caducado es la prosa que la publica.

11 LA CANDIDATA NO ESCONDE SUS LÍMITES. §6 de la matriz de cierre registra los once hallazgos
   del auditor con lo que se hizo y con lo que NO se hizo —el hallazgo 9 dice, con esas
   palabras, «no se finge que se cierra»—, y la fila `G-04` declara por escrito su tercera capa
   como PETICIÓN y no como verde. Esa disciplina es real y hay que consignarla.

12 LOS TRES DICTÁMENES SON HONESTOS. Los tres declaran su alcance sin redondear, uno de ellos
   retira contra su interés una lectura propia anterior que era más grave y era falsa, otro
   declara una desviación disciplinaria que nadie le habría descubierto, y el tercero declara
   las elisiones tipográficas de su lectura. Ninguno infló un hallazgo hasta romperlo: los
   veintisiete reproducen.
```

---

## 6 · EL ALCANCE DE LO QUE **YO** NO HE PODIDO COMPROBAR

Un alcance sin declarar es el defecto que este proyecto ha visto más veces. Éste es el mío.

```text
 1 NO TENGO ANCLA EXTERNA. No se emitió sobre de ancla para este gate (§1 bis). Todo lo que
   afirmo sale del árbol congelado y del `MANIFIESTO.json` del scratchpad. Que el congelado sea
   `c2437214…` lo dice el propio congelado; que el manifiesto sea el emitido antes de crear a
   los revisores no lo puede decir nada de lo que tengo.
 2 NO HE LEÍDO NINGÚN LOTE. Mi trabajo es verificar hallazgos, no releer 165 000 líneas. He
   abierto, dirigidamente y por reproducción, `estado_util.py`, `perimetro.py`,
   `admision/__init__.py`, `sede.py`, `comprobar_evidencia.py`, `comprobar_integridad.py`,
   `comprobar_recuentos.py`, `huella.py`, `comprobar-cobertura-de-gate.py` entero,
   `test_integridad_y_evidencia.py` por tramos, `docs/owner/ADS-OWNER-RESOLUCIONES.md` (`O26`
   y `O27`), `06-DEUDA`, `01-MATRIZ` y `05-MATRIZ`. **No declaro cobertura de lectura de nada.**
 3 NO HE EJERCIDO LAS OCHO CONDICIONES DE `O26` §1, por la misma razón que los revisores:
   `E-18` declara que este anfitrión no las admite. Que §5.4 quede NO ACREDITADA es un límite
   compartido, y lo cuento como tal y no como cargo contra la candidata.
 4 NO HE COMPROBADO LAS 170 MUTACIONES UNA A UNA, ni los 314 escenarios, ni los 582 bloques.
   Reproduje los agregados y las seis reproducciones que deciden.
 5 NO HE ATACADO EL ÁRBOL POR MI CUENTA buscando un duodécimo árbol adversarial. Los tres
   ataques que corrí son los que los revisores describen, rehechos por mí sobre mi copia.
   `M-04` sigue siendo deuda declarada, y mi silencio no la cierra ni la agrava.
 6 NO PUEDO MEDIR SI UN TRAMO DECLARADO SE LEYÓ DE VERDAD. El instrumento casa SHA-256 —lo he
   recalculado yo para las 259 fichas y las 237 entradas de lectura, sin una discrepancia— y
   hace la aritmética de líneas; la comprensión no es medible. Los tres manifiestos son consistentes y los
   tres dictámenes citan material repartido por todo su lote, que es el mejor indicio
   disponible, y no es una prueba.
 7 NO HE COMPROBADO LA VÍA COMETIDA del hallazgo 20 con un commit real, porque el encargo
   prohíbe toda orden `git` que escriba. Lo acoté por lectura y por el juicio directo de
   `sede.juzgar`, y la acotación va escrita en §3.3.
 8 REPRODUCIBILIDAD: WSL2, Python 3.12.14, un solo anfitrión, `core.quotePath` sin fijar. No he
   probado otro intérprete, otro sistema de ficheros ni otra configuración de Git. Con el
   `python3` 3.10 del `PATH` caen tres validadores por `tomllib` (`A14`), y no lo cuento.
 9 NO JUZGO SI LA ARQUITECTURA DE `F6` ES BUENA, ni si los remedios propuestos por los
   revisores son los mejores. Adjudico sobre lo que se reproduce.
10 NO HE VERIFICADO LA COMPLETITUD DE LA CLASIFICACIÓN de los trece defectos respecto del
   registro del gate anterior. Es la misma limitación que el auditor independiente declaró.
```

---

## 7 · DISCIPLINA

```text
ÁRBOL JUZGADO                    …/scratchpad/gate-congelado — SÓLO ése, y no se ha tocado
/home/jose/ads-kernel            NO JUZGADO, NO MODIFICADO, NI UNA ORDEN QUE ESCRIBA
FICHEROS DE UN ÁRBOL DEL REPOSITORIO editados, creados o borrados por mí     ninguno
ÓRDENES `git` QUE ESCRIBAN sobre un árbol del repositorio                    ninguna
                                 (`git init` y dos `commit` SÓLO en …/adj-work/puerta/repo,
                                  repositorio sintético mío, fuera de todo árbol del proyecto)
`redesign/kernel-2.0`            NO TOCADA
`fd633383…`                      NO usado, NO leído como fuente, NO publicado
PesquerApp                       NO ARRANCADA
NINGÚN HALLAZGO CORREGIDO        deliberado: quien corrige no adjudica
NINGUNA RESTA REDONDEADA         ni a cero ni al revés
DEFECTOS IMPUTADOS AL COORDINADOR, y dichos: la ausencia de sobre de ancla; la puerta latente
   de la cuarta resta de su comprobador; y —consignado, no adjudicado— la falta de acto que
   autorice un segundo gate que el manifiesto anterior prohíbe expresamente.
```

---

# `F6 ESTÁ COMPLETAMENTE IMPLEMENTADA` — **NO**
# `F6 QUEDA CERTIFICADA` — **NO**

**El gate es VÁLIDO por cobertura, y por eso esta adjudicación existe.** `O26` §8: la
aceptación arquitectónica **permanece**; **`F6` sigue ABIERTA** y **PesquerApp sigue
BLOQUEADA**.

— El ADJUDICADOR, 2026-09-05
