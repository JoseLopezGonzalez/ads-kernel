# DICTAMEN — REV-2 · GATE DE CERTIFICACIÓN FINAL DE `F6` · 2026-09-05

```text
CANDIDATA        c2437214c9353185d6b90b8fe86178302d4cf349
TREE             bb5b674aef387dbb92485d922cd6042acbb85d69
ÁRBOL JUZGADO    …/scratchpad/gate-congelado   ·   `git status --porcelain` VACÍO
BASE             769a8b6
INTÉRPRETE       /home/jose/.local/bin/python3.12  (Python 3.12)
LOTE             86 fichas · 80 ficheros · 55 203 líneas
LEÍDO            55 203 de 55 203   ·   `ASIGNADO − LEÍDO = ∅`   ·   cerrado: true
```

Identidad del árbol comprobada antes de leer nada:

```console
$ git -C <congelado> rev-parse HEAD HEAD^{tree}
c2437214c9353185d6b90b8fe86178302d4cf349
bb5b674aef387dbb92485d922cd6042acbb85d69
$ git -C <congelado> status --porcelain
(vacío)
```

---

# 1 · VEREDICTO

Las dos proposiciones se responden por separado y no se mezclan.

## (a) `F6 ESTÁ COMPLETAMENTE IMPLEMENTADA` — **NO**

No por lo que el aparato no mide, sino por lo que la propia sede canónica del corpus
declara. `docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md` §3 dice de `M-04`, con esas
palabras, **`ESTADO **NO SUPERADA**`**, `FASE **F6**`, y que lo que la cierra es «*que `F6`
implemente TODOS los puntos del contrato del verificador **y los EJECUTE***». La misma sede
mantiene `C-L.7` en **NO CERRADA** con componente de fase `F6`. Una fase cuya propia sede de
deuda declara no superada la obligación que la bloquea no está completamente implementada.

Lo que sí queda acreditado, y consta a favor: la línea base del coordinador se reproduce
ENTERA y exacta (§2), las tres restas salen vacías, y no hay ninguna obligación del universo
sin al menos un escenario en `prueba-superada` (medido, §2).

## (b) `F6 QUEDA CERTIFICADA` — **NO**

`O26` §5 exige demostrar **simultáneamente** cinco cosas. Sobre esta candidata:

| condición de `O26` §5 | estado según lo reproducido |
|---|---|
| 5.1 no quedan obligaciones internas sin implementar | **NO DEMOSTRADA.** `A=0` mide TRAZABILIDAD DECLARADA, y el propio instrumento lo publica pegado a la cifra |
| 5.2 no quedan propiedades críticas sin prueba capaz de fallar | **NO DEMOSTRADA.** `B=0` mide EXISTENCIA DE AL MENOS UN SABOTAJE, no cobertura propiedad a propiedad; el instrumento lo publica |
| 5.3 trazabilidad hasta evidencia ejecutable | **SÍ**, en el sentido acotado que `C` mide: 58/58 con fichero de evidencia presente |
| 5.4 la implementación satisface las ocho condiciones de `O26` §1 | **NO ACREDITADA POR MÍ.** Ver §4: no la he podido ejercer |
| 5.5 no existen bloqueantes internos vivos | **NO.** `M-04` está declarada NO SUPERADA y «bloquea `F6`» en su sede canónica; `C-L.7` está NO CERRADA con fase `F6` |

Con 5.5 en NO, la competencia que `O26` §5 concede no se activa. `O26` §8 fija la
consecuencia: la aceptación arquitectónica permanece, **`F6` sigue ABIERTA y PesquerApp
sigue BLOQUEADA**.

---

# 2 · LA LÍNEA BASE, REPRODUCIDA

Reproducida en su totalidad sobre una COPIA del árbol congelado (`…/rev2-trabajo/arbol`,
`diff -rq` contra el congelado: sólo `__pycache__` generado por mis propias corridas). No se
escribió en el árbol congelado ni en `/home/jose/ads-kernel`.

| afirmación del coordinador | reproducido | resultado |
|---|---|---|
| 38/38 validadores en verde · 38 evidencias · 0 problemas | `python3.12 kernel/operativo/validadores/registrar_evidencia.py` | **`38/38 validadores en verde · 38 evidencias publicadas · 0 problemas`**, `exit 0`, 22 m 58 s |
| 170 infracciones detectadas · 0 NO detectadas | `evidencia/negativos-salida.txt` | **`170 infracciones detectadas · 0 NO detectadas`** |
| 582 bloques canónicos · 0 errores · 0 avisos | `evidencia/lint-salida.txt` | **`bloques canónicos: 582 · identificadores: 582 · errores: 0 · avisos: 0`** |
| 314 escenarios · 254 contrastados · 0 divergencias · 0 en `prueba-ejecutada` | `REGISTRO-generado.md` | **314 · 254 · «Ninguna divergencia» · `PRUEBA EJECUTADA 0`** |
| 58 obligaciones · A=0 · B=0 · C=0 | `derivar-universo-obligatorio.py --obligaciones` | **`TOTAL 58`** (5+8+19+16+3+7) · **A 0 · B 0 · C 0**, `exit 0` |
| 58 puntos ejecutables · 58 con guarda · 0 sin guarda | `inventariar_el_arbol()` de `test_integridad_y_evidencia.py` | **`puntos ejecutables: 58 · excluidos: 87 · PUNTOS_SIN_GUARDA_ADMITIDOS: 0`** |
| huella `854dfa1b99be3824` · almacenada = calculada · estable | `huella.py` dos veces · `kernel/.upstream-hash` | **`854dfa1b99be3824`** las dos veces; almacenada idéntica |

**Comprobación añadida, no pedida:** ninguna de las 58 obligaciones queda cubierta sólo por
escenarios no superados —cruzando el universo contra `REGISTRO-generado.md`: `obligaciones
SIN ni un escenario en PRUEBA SUPERADA: 0`—.

**La línea base es verdadera. Y no acredita la certificación**, por lo que sigue.

---

# 3 · HALLAZGOS

## GRAVE 1 · `M-04` está declarada NO SUPERADA en su sede canónica, y `O26` §5.5 lo convierte en impedimento de certificación

**Hecho reproducido.**

```console
$ sed -n '/^## 3 · `M-04`/,/^## 4 ·/p' docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md
QUÉ ES         la proposición general de que un árbol defectuoso puede pasar en verde. Ocho
               gates encontraron ONCE árboles adversariales distintos

ESTADO         **NO SUPERADA**
…
FASE           **`F6`**

QUÉ LA CIERRA  que `F6` implemente TODOS los puntos del contrato del verificador **y los
               EJECUTE**, con cero falsos verdes y cero falsos rojos, medidos y publicados

QUÉ NO LA      ningún verde de la batería interna del corpus · ninguna tanda de corrección ·
CIERRA         ningún gate de `F4c` · escribir el contrato de una prueba
```

El título de la propia sección es «`M-04` — la deuda que **bloquea `F6`** y bloquea
PesquerApp». Y la misma sede añade, sobre el acto de `O26`: «**`B3` NO queda satisfecho por
este acto.** Queda satisfecho su conyunto de autoridad, y el resto —*la raíz externa existe*
y *su ejecutor NO comparte identidad de escritura con el runtime*— sigue siendo materia de
comprobación del gate».

**Dónde.** `docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md` §3, y `docs/owner/ADS-OWNER-RESOLUCIONES.md` `O26` §5.5 y §8.

**Por qué importa, y es lo central de este dictamen.** `M-04` **está dentro** del universo
obligatorio y sale con `A=B=C=0`:

```console
$ derivar-universo-obligatorio.py --obligaciones | grep '^M-04'
M-04             deuda   T275                         N275                   evidencia/composicion-procesos-salida.txt
```

Es decir: la resta la cuenta como cubierta —tiene `cubre` con validador, tiene un sabotaje
imputado y tiene fichero de evidencia— **mientras su propia sede la declara NO SUPERADA**.
Ésta es la demostración literal, sobre esta candidata y sin construir nada, de la advertencia
del gate anterior: *un `A=0 · B=0 · C=0` verdadero NO acredita lo que `O26` §5.1 y §5.2 le
piden*. No es una objeción teórica: hay una obligación concreta que las tres restas declaran
en verde y cuya sede normativa dice que no está superada.

**Remedio que cierra la CLASE** (no la instancia): que la derivación del universo cruce cada
obligación contra el **ESTADO que su sede declara** —como ya hace `T350` con el `estado:` de
cada escenario contra su evidencia— y publique una cuarta resta, `D · obligaciones cuya SEDE
las declara no superadas / no cerradas`. Mientras el instrumento sólo mire `cubre`,
`sabotajes` y `evidencia`, una obligación puede salir en verde con su sede diciendo lo
contrario, y ninguna cifra del tablero lo delatará.

---

## GRAVE 2 · `C-L.7` sigue NO CERRADA, tiene componente de fase `F6`, y ninguna de las tres restas la mide

**Hecho reproducido.**

```console
$ grep -n 'C-L.7' docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md
74:| **`C-L.7`** | **NO CERRADA** | … | `SIS` | **`F5`** la especificación · **`F6`** el
   instrumento | **sólo un gate independiente posterior puede cerrarla.** Barrer no es
   certificar, y el corpus lo dice de sí mismo |
```

Y la misma sede, líneas 99-102:

> «**Y una razón añadida por la que `C-L.7` sigue abierta, derivada por el último
> verificador:** el barrido mecánico de su regla **es incompleto POR CAJA DE LETRA** …, de
> modo que **su verde no prueba lo que dice probar**.»

Su población ha CRECIDO dentro de esta misma candidata: `KD-02` (L50), `LE-02` (L52) y `OC-1`
(L455) se registran como instancias nuevas de la clase.

**Dónde.** `docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md` §2 y §10.

**Por qué importa.** El derivador la publica **fuera** del universo de obligaciones, por
frontera declarada:

```console
$ derivar-universo-obligatorio.py --obligaciones | sed -n '/condiciones de cierre `C-L`/,+4p'
  condiciones de cierre `C-L` con fase `F6` (3)  ·  OTRO censo: `06-DEUDA` §2, heredado de `F4c` y `F5`
      C-L.10   fase declarada: **`F6`**
      C-L.13   fase declarada: **`F6`**
      C-L.7    fase declarada: **`F5`** la especificación · **`F6`** el instrumento
```

La frontera está DECLARADA y es discutible —que es exactamente lo que el derivador dice que
pretende—, y aquí se discute: una condición de cierre con **componente de fase `F6`** y
estado **NO CERRADA** es, para `O26` §5.5, indistinguible de un bloqueante interno vivo. Que
viva en «otro censo» explica por qué `A=B=C=0` no la ve; no explica por qué no cuenta.

**Remedio de CLASE.** Que las condiciones `C-L` cuya celda de fase nombre `F6` entren en el
universo obligatorio como un componente más —con su criterio de pertenencia declarado, igual
que `deuda`—, o que `--obligaciones` publique una resta propia para ellas. Hoy se publican
como información y no restan.

---

## GRAVE 3 · La sede que declara CERRADOS los trece defectos está FUERA del universo obligatorio, del manifiesto, de la huella y del sobre

**Hecho reproducido.**

```console
$ derivar-universo-obligatorio.py --rutas | grep "docs/f6"
docs/f6/01-MATRIZ-DE-COMPLETITUD-F6.md
$ derivar-universo-obligatorio.py --rutas | grep -c "docs/f6"
1
$ ls -1 docs/f6/
00-ESTADO-DE-IMPLEMENTACION-F6.md
01-MATRIZ-DE-COMPLETITUD-F6.md
02-GATE-DE-CERTIFICACION-FINAL-20260903.md
03-GATE-DE-CERTIFICACION-FINAL-20260904.md
04-MATRIZ-DE-HALLAZGOS-DEL-GATE-20260904.md
05-MATRIZ-CIERRE-G01-G08.md
gate-definitivo
$ huella.py --listar | grep -c "^docs/"
0
```

`docs/f6/05-MATRIZ-CIERRE-G01-G08.md` es **el documento que el encargo manda atacar** —el que
declara `G-01`…`G-08`, `D-01`…`D-05` y los trece defectos CERRADOS— y no es fuente
obligatoria: ningún revisor está obligado a leerlo, no tiene fila de manifiesto y su huella
no viaja en el sobre. Lo mismo vale para `00-`, `02-`, `03-`, `04-` y para el expediente
completo del gate anterior en `docs/f6/gate-definitivo/` (7 891 líneas, incluidos el
manifiesto de asignación, los tres manifiestos de lectura y el registro del gate).

**Dónde.** `docs/evolucion/verificacion/derivar-universo-obligatorio.py`, lista `ENCARGO`
(única fila `docs/f6`: la constante `UNIVERSO`) · `kernel/operativo/validadores/huella.py`,
`AMBITOS = ("kernel", "packs", "tooling")`.

**Por qué importa.** Es **la CLASE del hallazgo 6 de la auditoría independiente**, cerrada
sólo en su instancia. Aquel hallazgo midió `--rutas | grep -c "docs/f6"` → `0` y el remedio
metió en el `ENCARGO` **la sede que gobierna el universo** —correcto— y añadió una guarda que
comprueba que siga entrando. Pero la propiedad que el hallazgo enunciaba era más ancha:
*ninguna sede que gobierne el juicio del gate puede vivir fuera del perímetro auditado*. Hoy
el documento que declara todo cerrado, y el registro del gate del que se derivan los trece
defectos, viven fuera. La consecuencia es concreta y no hipotética: **es en esa zona donde he
encontrado el cardinal caducado de SERIO 1**, y ninguna guarda del corpus lo alcanza.

Y hay un segundo efecto medible: esa misma zona ya está consumiendo la exención mayoritaria
del control de veracidad de sedes.

```console
$ cat kernel/operativo/pruebas/evidencia/recuentos-salida.txt | grep "alcance:"
alcance: líneas eximidas por ser transcripción de consola: 164, en 2 sede(s) —
docs/f6/gate-definitivo/00-REGISTRO-DEL-GATE.md (151), kernel/operativo/pruebas/T380-T399-aislamiento.md (13).
```

151 de las 164 líneas que `T360` exime las aporta un documento de gate que no es fuente
obligatoria y que la huella no cubre.

**Remedio de CLASE.** Declarar `docs/f6` como **ZONA DEL ENCARGO barrida** —exactamente como
`docs/owner` y `docs/evolucion/verificacion/manifiestos`, con sus anclas exigidas—, de modo
que un documento nuevo del área de `F6` entre solo el día que se publica y no haya fila que
borrar. Alternativamente, si `O27` §4 obliga a que los documentos del gate vivan fuera de la
candidata, entonces el remedio es el simétrico: que NO estén en el árbol de la candidata. Hoy
están dentro del árbol y fuera del universo, que es la peor de las dos combinaciones.

---

## SERIO 1 · El cardinal del inventario de aislamiento está caducado en las tres sedes que lo publican, incluida la condición de aceptación del propio `T380`

**Hecho reproducido.**

```console
$ python3.12 -c "import importlib.util,sys; sys.argv=['x'];
  spec=importlib.util.spec_from_file_location('tie','kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py');
  m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m);
  p,e=m.inventariar_el_arbol(); print('puntos ejecutables:',len(p)); print('excluidos:',len(e))"
puntos ejecutables: 58
excluidos: 87

$ grep -n "56" kernel/operativo/pruebas/T380-T399-aislamiento.md
37:ejecutables y 110 exclusiones** a **56 y 89**, sobre los mismos 145 ficheros `.py`, y **nada
47:**56 de 56**, y los puntos sin guarda admitidos son **CERO**.
81:  - "los 56 puntos ejecutables de las nueve zonas del kernel, tooling y docs llevan la guarda, sin una sola exencion"

$ grep -n "56 de 56" docs/f6/05-MATRIZ-CIERRE-G01-G08.md
88:| **`G-03`** | **CERRADO** … alcanza a **56 de 56** puntos ejecutables del inventario derivado …
```

**Dónde.** `kernel/operativo/pruebas/T380-T399-aislamiento.md` L37, L47 y **L81 — que es la
cláusula `entonces` del escenario `T380`, es decir su condición de aceptación** — y
`docs/f6/05-MATRIZ-CIERRE-G01-G08.md` §5, fila `G-03`.

**Por qué importa.** El remedio del **hallazgo 5** del auditor invirtió la carga de la prueba
y ensanchó la clase de «punto ejecutable»; el inventario pasó de 56 a 58 y de 89 a 87
exclusiones. Nadie actualizó las tres sedes. El resultado es que:

1. la fila `G-03` de la matriz de cierre —el documento que este gate juzga— publica un
   cardinal que el árbol desmiente;
2. el `entonces` de `T380` afirma sobre el árbol algo falso, y `T380` sale VERDE, porque la
   prueba **deriva** el número y no lo contrasta contra su propio enunciado;
3. ningún validador lo caza: `comprobar_recuentos.py` no tiene regla para «puntos
   ejecutables», y `T360` no alcanza a `docs/f6`.

Es, palabra por palabra, la clase que el corpus persigue con el nombre de `J-07` —«un cardinal
al lado de su enumeración»— reproducida **dentro del remedio del hallazgo que la corrigió**,
igual que el hallazgo 10 del auditor («48 componentes donde había 49, reproducido dentro de la
matriz que registra su corrección»).

La propiedad de fondo NO está rota: 58 puntos, 58 con guarda, 0 admitidos sin ella. Lo que
está roto es la veracidad de las sedes que lo publican.

**Remedio de CLASE.** Los cardinales del inventario se **retiran** de la prosa y del
`entonces`, y se remiten a la derivación —que es lo que el propio corpus decidió en `J-07`,
`D102` y el hallazgo 10—; y `T380` gana una comprobación que contrasta **su propio enunciado**
contra el inventario derivado, de modo que un cardinal escrito en su ficha lo ponga rojo.

---

## SERIO 2 · Cinco sedes declaran en presente un estado de escenario que el árbol no tiene

**Hecho reproducido.**

```console
$ grep -rn "han BAJADO a .prueba-ejecutada\|ha BAJADO a .prueba-ejecutada" kernel/operativo/pruebas/
T172-T181-estado-durable.md:7:  `T180` y `T181` han BAJADO a `prueba-ejecutada`
T159-T170-multirepo.md:18:      `T162`…`T168` han BAJADO a `prueba-ejecutada`
T182-T194-runtime-y-admision.md:10: `T193` ha BAJADO a `prueba-ejecutada`
T210-T225-arboles-raiz-externa-y-contencion.md:10: `T225` ha BAJADO a `prueba-ejecutada`
T290-T311-integridad-evidencia-y-contencion.md:12: `T301` ha BAJADO a `prueba-ejecutada`

$ grep -c "estado: prueba-ejecutada" -r kernel/operativo packs
0
$ grep -A2 "PRUEBA EJECUTADA" kernel/operativo/pruebas/REGISTRO-generado.md | head -1
| PRUEBA EJECUTADA | 0 |
```

Los once escenarios que las cinco notas declaran «bajados» están hoy en `prueba-superada` y
contrastados: `D-02` les añadió la línea de veredicto nominal (`T180  SUPERADA …`,
`T193  SUPERADA …`) y volvieron a ser contrastables. Las notas de `H-02` no se retiraron.

**Dónde.** Los cinco ficheros de `kernel/operativo/pruebas/` citados arriba, todos ellos
fuentes obligatorias del corpus operativo.

**Por qué importa.** Son afirmaciones escritas **en presente** sobre el estado del árbol, en
sedes vivas, que el árbol contradice; y son exactamente la clase que `T151`/`T350` existen
para cerrar, con la diferencia de que aquí lo falso no es una cifra ni un campo `estado:`,
sino la prosa que los explica —el mismo hueco que `S-16`, `DD-13` y el ADDENDUM de `D97`
llevan tres gates persiguiendo—. La línea base del coordinador («0 en `prueba-ejecutada`») es
correcta; lo que miente es la explicación.

**Remedio de CLASE.** Que `T350` —que ya cruza `estado:` declarado contra evidencia— extienda
su contraste a las afirmaciones de estado escritas **en la prosa** de la ficha: una nota que
diga «`Tnnn` está en `<estado>`» tiene que casar con el estado derivado, o retirarse y
remitir. Corregir las cinco notas cierra la instancia; el barrido cierra la clase.

---

## MODERADO 1 · `D-03` relaja el régimen de integridad del material APROBADO, y nada del corpus cubre la relajación

**Hecho reproducido.** El motivo que `D-03` declara es CIERTO, y lo he medido:

```console
$ for f in docs/rediseno/a-CAPACIDADES-APROBADA.md docs/rediseno/a-ENMIENDA-E1-ENC.md \
           docs/rediseno/b-RECORRIDO-APROBADA.md kernel/KERNEL.md \
           docs/owner/ADS-OWNER-RESOLUCIONES.md; do … ES PREFIJO DEL NACIMIENTO? …; done
docs/rediseno/a-CAPACIDADES-APROBADA.md   nacimiento 57714 → hoy 61110   ES PREFIJO: False
docs/rediseno/a-ENMIENDA-E1-ENC.md        nacimiento  9843 → hoy 10710   ES PREFIJO: False
docs/rediseno/b-RECORRIDO-APROBADA.md     nacimiento 63053 → hoy 66652   ES PREFIJO: False
kernel/KERNEL.md                          nacimiento 89827 → hoy 94716   ES PREFIJO: False
docs/owner/ADS-OWNER-RESOLUCIONES.md      nacimiento 14395 → hoy 44433   ES PREFIJO: True
```

Los cuatro rojos que `D-03` alega existen, y la sede del Owner sí es prefijo. La decisión
está fundada.

**Dónde.** `kernel/operativo/runtime/admision/perimetro.py`, `CONDICIONES_DE_ZONA` ·
`docs/canonico/FUENTES-CANONICAS.yml`, clase `APROBADA_POR_ENMIENDA`.

**Por qué importa igualmente.** El efecto es que `kernel/KERNEL.md`, `(a)`, `(b)` y `E1` pasan
de `APPEND_ONLY` —régimen que **ninguna declaración de admisión levanta**— a `DECLARADA` —una
mutación de contenido cualquiera se admite con una línea en la declaración—. Material que el
corpus llama APROBADO y que `gate:sistema-conforme` exige no modificar (`sin-modificar-lo-aprobado`:
«diff contra las secciones aprobadas: debe estar vacío») queda, en el eje de INTEGRIDAD, con
el mismo régimen que un fichero de trabajo. Ninguna prueba del corpus ejerce la reescritura
completa de uno de esos cuatro ficheros bajo declaración de admisión.

**Remedio de CLASE.** Un tercer régimen para `APROBADA_POR_ENMIENDA` que exprese lo que la
clase significa —«se amplía por ENMIENDA, y la enmienda es un fichero NUEVO»—: contraste
append-only contra el nacimiento **más** admisión declarada para el delta, o derivación de
entradas cerradas como la que `sede.py` ya implementa para la sede del Owner. Y su sabotaje:
reescribir `kernel/KERNEL.md` entero con la mutación declarada y exigir ROJO.

---

## MODERADO 2 · Prosa caducada dentro del módulo que aplica el remedio

**Hecho reproducido.** `runtime/admision/perimetro.py`, `vigilar_append_only`, DECISIÓN
segunda, sigue diciendo:

> «Arreglar eso exige partir la clase en el registro canónico —`docs/canonico/FUENTES-CANONICAS.yml`—,
> que no es sede de este módulo: **queda anotado como PETICIÓN**, y entretanto la vigilancia
> permanente se aplica donde su término de comparación es exacto…»

`D-03` ya partió la clase: `APROBADA_POR_ENMIENDA` está declarada 30 líneas más arriba, en el
mismo fichero. La petición está atendida y el texto sigue pidiéndola.

**Por qué importa.** Es menor en consecuencia y es la misma clase que SERIO 2: una sede viva
que describe un estado del árbol anterior al vigente, dentro del fichero que contiene el
remedio. **Remedio:** retirar la petición y remitir a `D-03`.

---

## MENOR 1 · El manifiesto inmutable del gate anterior prohíbe expresamente que exista este gate, y no consta acto que lo levante

**Hecho reproducido.**

```console
$ sed -n '5,11p' docs/evolucion/verificacion/manifiestos/F6-ASIGNACION-GATE-CERTIFICACION-FINAL-20260904.md
> **ÉSTE ES EL ÚNICO GATE AUTORIZADO.** Después de su veredicto el método se detiene,
> cualquiera que sea el resultado: **no se corrigen sus hallazgos, no se abre otro gate, no se
> propone otro ciclo y no se inicia PesquerApp.**
$ sed -n '/## 9 · Lo que este gate NO hará/,+8p' <mismo fichero>
NO ABRIRÁ      ningún ciclo posterior ni ningún segundo gate
```

`O27` —posterior— aclara `O26` y fija la regla de cobertura, y **no levanta** esa cláusula;
ninguna resolución del Owner posterior a `O27` consta en la sede canónica. La candidata que
juzgo es el resultado de una pasada de corrección de los hallazgos de aquel gate, y este gate
es un segundo gate.

**Por qué lo registro como MENOR y no como GRAVE.** No es un defecto del producto ni cambia
ninguna de las dos proposiciones: `F6` no se certifica igualmente. Y el manifiesto que impone
la cláusula es del coordinador, no del Owner, de modo que quien puede levantarla es el Owner y
no yo. Lo dejo escrito porque un método que se detiene y continúa sin acto expreso es
exactamente el tipo de cosa que este expediente registra en vez de callar.

**Remedio.** Que el Owner emita —o que el coordinador exhiba— el acto que autoriza este gate;
o que el gate declare expresamente que actúa sin él.

---

# 4 · LO QUE NO HE PODIDO COMPROBAR, Y POR QUÉ

Se declara entero, porque un alcance sin declarar es el defecto que este proyecto ha visto
más veces.

1. **Las OCHO condiciones de `O26` §1 sobre esta candidata, ejercidas.** No las he ejecutado:
   exigen contenedor, identidad de sistema separada y proveedor de firma, y `E-18` declara —y
   el corpus mide— que `cgroup v2` no es ejercitable en este anfitrión y que la cuenta de
   servicio no está disponible. Lo que sí he comprobado es que la evidencia publicada las
   afirma y que los escenarios `T217`–`T220`, `T290`–`T296` y `T330`–`T337` salen SUPERADAS en
   la corrida de 38/38 que yo mismo lancé. **No convierto eso en «demostradas».**

2. **La corrida de los 38 validadores sobre el ÁRBOL CONGELADO.** Publicar evidencia escribe
   en el árbol, y escribir en el congelado está prohibido. La lancé sobre una copia byte a
   byte (`diff -rq` limpio salvo `__pycache__` mío). No afirmo, por tanto, que el congelado
   quede con `git status` vacío tras correrla; sí que la copia produjo `38/38 · 0 problemas`.

3. **El catálogo de 170 mutaciones, una a una.** He reproducido el agregado
   («170 detectadas · 0 NO detectadas») y he leído las mutaciones que aparecen en la cola de
   la evidencia y en las tablas `SABOTAJES` de `test_agentes.py` y
   `test_cardinalidad_y_seleccion.py`. No he ejercido individualmente las 170.

4. **La afirmación de `06-DEUDA` de que el barrido de `C-L.7` es «incompleto POR CAJA DE
   LETRA».** La cito como hecho declarado por la sede, no como hecho medido por mí: probé la
   caja de letra sobre `comprobar_recuentos.py` (`Los doce…` y `Los DOCE…` producen los dos
   `1 fallidas`, luego ESE barrido sí es insensible a la caja) y no localicé con certeza el
   barrido concreto al que la sede se refiere.

5. **`G-08` bajo carga sostenida y en anfitriones distintos de éste.** `T413` la mide aquí;
   `E-18` declara que la certificación queda limitada al backend ejercido. No he medido nada
   fuera de este anfitrión.

6. **Los ficheros del corpus que NO están en mi lote.** Mi lote son 55 203 líneas de 80
   ficheros. He abierto fuera de él, y lo declaro, `docs/f6/05-MATRIZ-CIERRE-G01-G08.md`
   (153 líneas), `docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md` (§2, §3, §4, §10 ter),
   `kernel/operativo/pruebas/REGISTRO.md` (cabecera), varias evidencias y el listado de
   `docs/f6/gate-definitivo/`. Fueron lecturas dirigidas para sostener hallazgos, no lecturas
   íntegras, y no las cuento como cobertura.

7. **Elisiones tipográficas al leer.** En cuatro lecturas de manifiestos sustituí en pantalla
   las cadenas SHA-256 de 64 hex por `<sha>` y una frase de delegación repetida, para no
   desbordar el canal. Las líneas se abrieron y se recorrieron enteras; lo que no leí carácter
   a carácter fueron esos digest, cuya integridad ya había comprobado mecánicamente al validar
   el lote (86 fichas, 0 discrepancias de SHA).

8. **No he hablado con los otros revisores** ni he leído sus dictámenes, sus lotes ni sus
   manifiestos.

---

# 5 · SOBRE LA COBERTURA

```text
ASIGNADO        86 fichas · 80 ficheros · 55 203 líneas
LEÍDO           55 203 líneas   ·   ASIGNADO − LEÍDO = ∅
DECLARADO       …/scratchpad/LECTURA-REV-2.json  ·  "cerrado": true
```

Integridad del lote comprobada **antes** de leer: los 80 ficheros existen en el árbol
congelado, los 86 prefijos SHA-256 casan con el fichero real, ningún tramo excede el número de
líneas del fichero y no hay solapes entre tramos del mismo fichero. **Este lote no reproduce
`G-01`**, que fue el defecto que mató al gate del 2026-09-05 (una ficha que asignaba la línea
12 153 de un fichero de 12 152 y dejaba 1-94 sin asignar).

---

# 6 · RESUMEN

```text
F6 ESTÁ COMPLETAMENTE IMPLEMENTADA        NO
F6 QUEDA CERTIFICADA                      NO

GRAVE      3     M-04 declarada NO SUPERADA y contada en verde por las restas ·
                 C-L.7 NO CERRADA con fase F6 y fuera de toda resta ·
                 la sede que declara todo cerrado, fuera del universo, de la huella y del sobre
SERIO      2     el cardinal 56 del inventario de aislamiento, caducado en las tres sedes
                 que lo publican, una de ellas el `entonces` de `T380` ·
                 cinco sedes afirman en presente un estado de escenario que el árbol no tiene
MODERADO   2     D-03 relaja el régimen de integridad del material APROBADO sin cobertura ·
                 prosa caducada en `vigilar_append_only`
MENOR      1     no consta acto que autorice este segundo gate

LÍNEA BASE       reproducida ENTERA y exacta, las siete cifras
```

`O26` §8: la aceptación arquitectónica permanece, **`F6` sigue ABIERTA** y **PesquerApp sigue
BLOQUEADA**.

— REV-2
