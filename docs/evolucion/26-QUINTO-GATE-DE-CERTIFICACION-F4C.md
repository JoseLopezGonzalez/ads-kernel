# QUINTO GATE DE CERTIFICACIÓN DE F4c — INSUFICIENTE, Y EL OCTAVO ÁRBOL

> **Veredicto del adjudicador `DD`: `F4c ES INSUFICIENTE PARA F5`.**
> **`F4c` NO se cierra y sigue ABIERTA. `F5` NO queda autorizada. Ningún hallazgo se ha**
> **corregido en esta pasada.**
>
> **Y ADEMÁS, y es lo contrario del gate anterior: EL GATE ES VÁLIDO.** El remedio del defecto
> que invalidó el cuarto gate **funciona, medido y no supuesto**.

## 0 · Qué es este documento

Registro **LITERAL** de los tres dictámenes del quinto gate independiente sobre la candidata
`8c9ca9c3920000bdf327cef7a6dbaf9aeff4eaeb`, publicada en
`review/f4c-perimetro-derivado-candidate-20260831`. Los tres se transcriben **enteros y sin
suavizar**, en §A, §B y §C.

Lo escrito antes de §A lo escribe el **coordinador**, que no es ninguno de los ocho
participantes y **que no ha juzgado nada**. Los tres dictámenes **no pasaron por su mano**: se
concatenaron desde los ficheros que sus autores escribieron, y este documento publica sus
SHA-256 para que cualquiera lo compruebe.

```text
DICTAMEN DE LA CADENA `BB`, firmado por `BB4`
  1571 lineas   SHA-256  09eea2dc760a630728dad2c10ddbbf72088c92623e2da4212cc46b5d08b85aec
DICTAMEN DE LA CADENA `CC`, firmado por `CC3`
  1398 lineas   SHA-256  4ba093e0882f55f2aa9303e4da7e2162af044e8eae9e508665d1e8d5a588334f
ADJUDICACIÓN DE `DD`
  1329 lineas   SHA-256  3fe3d78ede05e43e87b4c5af4424c4995b42ba703a1c45946fb27e2409aadf69
EL SOBRE DE ANCLA, leído por los siete
   190 lineas   SHA-256  906b74f70a30785465d56ecc68cf30e42b461febc7042e2a463aae5e8a899070
```

## 1 · EL GATE ES VÁLIDO, Y ES LA PRIMERA COSA QUE HAY QUE DECIR

El cuarto gate fue declarado **INVÁLIDO** por su propio adjudicador, y la causa fue el
coordinador: **transcribió el SOBRE DE ANCLA a mano** en el encargo de cada relevo, y las cinco
transcripciones difirieron **en ocho campos**.

Este gate estrena el remedio. El sobre **se emitió UNA vez a un fichero fuera del repositorio
auditado**, y **cada participante lo leyó de ahí**. `DD` lo verificó, y esto es lo que midió:

```text
LOS SIETE PUBLICARON EL MISMO      906b74f70a30785465d56ecc68cf30e42b461febc7042e2a463aae5e8a899070
SHA-256 DEL SOBRE

CUATRO DE LOS SIETE lo embebieron  `BB1`, `BB2`, `CC1`, `CC2`. `DD` extrajo los cuatro
entero en su informe                bloques y los cuatro son BYTE A BYTE el fichero
LOS OTROS TRES                     publican el mismo digest y remiten al fichero
DIVERGENCIA ENTRE LOS SIETE        CERO

LOS 21 CAMPOS DEL SOBRE            reproducen, recalculados por `DD` sin fiarse de nadie
LOS DOS DIGEST DE UNIVERSO         reproducen con la receta publicada y SIN ejecutar el emisor
LAS DOS REFS REMOTAS               apuntan a los dos commits, contra el remoto real
```

**La causa exacta de la invalidez anterior está cerrada de raíz.** No por diligencia del
coordinador, sino **por construcción**: el sobre dejó de pasar por su mano.

## 2 · EL OCTAVO ÁRBOL, QUE LO ENCONTRÓ EL ADJUDICADOR Y NO LOS REVISORES

`M-04` —*«se puede construir un árbol defectuoso que pase la batería entera en verde»*— entra
en su **quinto gate viva**. Y esta vez la puerta está donde ninguno de los cinco gates había
mirado.

Los dos instrumentos comparten un perímetro escrito:

```text
_EXCLUIDO = re.compile(r"(?:^|/)\.git(?:/|$)|\.py[co]$")
             bateria  L1839          derivador  L144
```

`Z1-03`≡`Z-05` encontró que ese mismo regex excluía `__pycache__` **por nombre de directorio**.
La tanda respondió **retirando ese nombre**. `CC1` encontró la mitad `.git` que quedó, y `CC3`
la clasificó `C` porque **no alcanza el commit**. **Nadie miró la tercera cláusula, que la
tanda conservó intacta: la exclusión POR EXTENSIÓN.** `DD` fue ahí.

Un documento nombrado con extensión de bytecode, colocado bajo `docs/owner/`, **alcanza el
commit** y entonces:

```text
git status --porcelain                    VACÍO      ← el emisor emitiría sobre este árbol
bateria adversarial                       38/38      EXIT=0
bateria del kernel                        13/13      RC=0
T147                                      SUPERADA
universo obligatorio                      74         SIN CAMBIO — ni fila, ni revisor, ni huella
EXCLUIDOS_IV                              11         SIN CAMBIO — el aviso de `Z-13` calla
DIGEST DEL UNIVERSO, receta del sobre     18f50dab…c8b4
DIGEST QUE ESTE GATE ANCLA                18f50dab…c8b4      BIT A BIT IDÉNTICOS
```

Con su **control positivo en rojo**: el mismo fichero con extensión `.md` da `37/38` y `FALLO
G-29`, y el universo crece a 75. **El mecanismo funciona; el perímetro no.**

> **La conclusión de `DD`, y es el núcleo de su veredicto:** el ancla externa que `O18(b)`
> adoptó para poder cerrar `F4c` **es ciega a ese commit**, y no por fallo del emisor, ni de la
> entrega, ni de la receta —los tres funcionan—. Es ciega porque **el digest se calcula sobre
> un universo derivado por un perímetro que vive dentro del árbol auditado y que excluye por
> nombre**. Quien controla el nombre controla lo que el ancla ve.

> ### ADVERTENCIA DE LECTURA, Y ES DEL COORDINADOR
> §C transcribe el experimento de `DD` **entero**, y dentro de un bloque de código va **el
> texto literal del documento que plantó**: una falsa ratificación que se nombra a sí misma
> `O20` y declara `F4c` cerrada, `F5` autorizada y `O17`·`O18`·`O19` sin efecto.
> **Eso es EVIDENCIA de un ataque, no una resolución.** No existe ninguna `O20`.
> **La única sede canónica de las resoluciones del Owner es**
> [`docs/owner/ADS-OWNER-RESOLUCIONES.md`](../owner/ADS-OWNER-RESOLUCIONES.md), **contiene
> `O17`, `O18` y `O19`, y nada más.** Se transcribe porque un gate que censura la prueba del
> ataque que denuncia no vale nada.

## 3 · LA SEXTA CONDICIÓN DEL OWNER, QUE NADIE HABÍA CITADO EN CINCO GATES

`CC3` fue a la sede canónica y encontró que `O18` fija **seis** condiciones para cerrar `M-04`
dentro de `F4c`. `DD` leyó `O18` íntegra y lo confirmó del árbol:

> «**`M-04` puede cerrarse para el alcance de `F4c` únicamente si el gate independiente
> demuestra:** batería interna coherente · sobre externo recibido antes de leer · todas sus
> huellas coincidentes · referencias remotas intactas · cobertura completa · **ninguna promesa
> de seguridad superior a la realmente entregada**.»

**El Owner, al excluir la clase `C`, convirtió PROMETER DE MÁS en condición de cierre.** Eso
reordena el gate entero: `M-04` no falla sólo por lo que el instrumento hace, sino por **lo que
dice que hace**. `DD` mide las seis y publica el resultado en las dos direcciones:

```text
1  bateria interna coherente                       NO   el octavo árbol, medido
2  sobre externo recibido antes de leer            SÍ   cuatro bloques byte a byte, cero divergencia
3  todas sus huellas coincidentes                  SÍ   los 21 campos y los dos digest reproducen
4  referencias remotas intactas                    SÍ   contra el remoto real
5  cobertura completa                              SÍ   con reserva declarada
6  ninguna promesa superior a la entregada         NO   CINCO promesas que el árbol no sostiene

FALLAN DOS DE LAS SEIS: la primera y la sexta.
```

## 4 · LA COBERTURA, QUE ESTA VEZ NO ES UNA DE LAS RAZONES

```text
OBLIGATORIO − ASIGNADO   0   contra el objeto que el manifiesto declara repartir
ASIGNADO − LEÍDO         0   los cinco relevos entregaron manifiesto de TODAS sus fuentes
```

`C-L.5` **no se reabre por cobertura**. Y aquí `DD` resolvió **contra la mayoría**: tres relevos
de dos cadenas distintas sostuvieron que la resta era **1**; `BB4` lo refutó reproduciéndolo, y
`DD` lo verificó por tercera vez. **El coordinador había dado por buena la cifra equivocada en
tres partes consecutivos, y la corrección vino del gate, no de él.**

`BB4` encontró además la razón de fondo, que nadie había visto: cerrar la resta a cero **sobre
el árbol del gate** exigiría que el manifiesto contuviera **su propio SHA-256**. Es
**inalcanzable por punto fijo**, y lo será en todos los gates siguientes. Es el hallazgo
`DD-19`.

## 5 · LOS VEINTIDÓS HALLAZGOS, Y NINGUNA DECISIÓN VUELVE AL OWNER

```text
                 DEL OBJETO   DEL APARATO   TOTAL
  BLOQUEANTE          0             0          0
  GRAVE              10             2         12
  MEDIO               3             3          6
  MENOR               3             1          4
                 ─────────────────────────────────
                     16             6         22

POR CLASE
  A · coherencia interna, corregible dentro de `F4c`     22
  B · exige una decisión NUEVA del Owner                  0
  C · resistencia a un actor privilegiado, contratada     0
```

`DD` examinó **cuatro candidatos a clase `B`** y **los cuatro caen**, y justifica no formular
pregunta al Owner. El más importante es el cuarto: `M-04` viva en su quinto gate **no reabre
`O18`**, porque `O18` **ya se declaró a sí misma transitoria y limitada**, ya rechazó la
alternativa de retirar la garantía, y ya contrató el verificador externo para `F6`.

> «Mi octavo árbol no descubre un riesgo que el Owner no haya aceptado: descubre que **el
> perímetro con el que se mide está escrito**, y eso es exactamente lo que `F4` puede
> arreglar.»

**Es la segunda vez consecutiva que ninguna decisión queda pendiente del Owner**, y `DD` lo
señala como información buena.

## 6 · LO QUE CONSTA A FAVOR, PORQUE ES VERDAD

```text
· el remedio del gate 5 FUNCIONA donde el gate 4 murió: cero divergencia entre los siete
· `AA-01` está CERRADO y GENERALIZA: `docs/owner/` se barre entero
· `AA-05` está CERRADO: el sobre publica un NOMBRE y no un rol
· el gate NO tocó `verificacion/` tras publicar el manifiesto: mismo SHA-256 en los dos commits
· la candidata pasa 13/13 y `T147`, y no ensucia un byte
· las 74 filas del manifiesto casan sin una discrepancia de SHA-256 ni de líneas
· la fila del propio derivador —la que el sobre manda mirar PRIMERO— es idéntica en los dos
  árboles: esa reincidencia NO se repite
· los contratos de prueba de `F6` —`X55`, `X58`, `W8`, `W11`, `W17`— están CORRECTOS, y el
  reparto de ventanas es exacto, sin huecos ni solapes
· el diseño NO ha cambiado, y `O19` sigue implementado sin escribir una sola protección
  interna nueva
· ninguno de los veintidós es BLOQUEANTE, ninguno exige arquitectura nueva
```

**«Ésta sigue siendo una candidata sólida, y el trabajo debe SEGUIR.»** — `DD`

## 7 · QUÉ FALLA HOY, EN LAS PALABRAS DEL GATE

El cuarto gate determinó que la causa esencial de los fracasos —*verificación anclada dentro
del objeto verificado*— **ya no era la causa**. `DD` lo confirma y lo precisa: la circularidad
**se ha movido por cuarta vez, y hoy está en el PERÍMETRO**.

Y `BB4` nombra la clase, que es la frase que este expediente necesitaba:

> **El sistema cierra INSTANCIAS y no CLASES.** La corrección se aplica con la forma sintáctica
> exacta del contraejemplo, y el defecto reaparece una sede más allá — en un caso, **quince
> líneas por encima de la nota que lo corrige**.

---

## §A · DICTAMEN DE LA CADENA `BB`, FIRMADO POR `BB4` — TRANSCRIPCIÓN LITERAL

# DICTAMEN `BB` — QUINTO GATE DE CERTIFICACIÓN DE F4c
### Firmado por `BB4`, DICTAMINADOR de la cadena `BB`
### Repositorio `/home/jose/ads-kernel` · rama `gate/f4c-certificacion-5-20260831`
### Fecha 2026-08-31 · contexto limpio, sin participación en gates anteriores

> **No emito veredicto de certificación.** Eso es del adjudicador `DD`. Entrego un
> dictamen cerrado, con cada hallazgo que sostengo reproducido POR MÍ con su comando.

---

## 0 · EL SOBRE · SHA-256, MI PROPIA VERIFICACIÓN, Y LOS TRES BLOQUES EMBEBIDOS

### 0.1 · El fichero

```
RUTA      /tmp/claude-1000/-home-jose-ads-kernel/92219625-e8eb-4a0a-840b-b949d6c3e97a/scratchpad/SOBRE-GATE-5.txt
SHA-256   906b74f70a30785465d56ecc68cf30e42b461febc7042e2a463aae5e8a899070
BYTES     14328
LINEAS    190
```

Comando: `sha256sum SOBRE-GATE-5.txt ; wc -lc SOBRE-GATE-5.txt`

**No lo transcribo.** El gate anterior murió porque el sobre se transcribió a mano y
las cinco copias difirieron en ocho campos. La sede del sobre es el fichero; su
identidad es el SHA-256 de arriba. Cualquiera que quiera el texto lo lee del fichero.

### 0.2 · MI verificación, sin fiarme de ningún relevo y SIN EJECUTAR EL EMISOR

Todo lo de abajo lo corrí yo, con `git show <commit>:<ruta>`, nunca del árbol de trabajo.

| # | Campo del sobre | Valor publicado | Mi resultado | ¿? |
|---|---|---|---|---|
| 1 | COMMIT CANDIDATO | `8c9ca9c3920000bdf327cef7a6dbaf9aeff4eaeb` | existe, tipo `commit` | ✓ |
| 2 | ARBOL CANDIDATO | `91fe62d369152f9d1b58361f0ffc888358364175` | `git rev-parse 8c9ca9c3^{tree}` idéntico | ✓ |
| 3 | COMMIT DEL GATE | `5ed7a3b805c472934cea9a4027d61e8ef7be5a35` | existe, tipo `commit` | ✓ |
| 4 | ARBOL DEL GATE | `6ab0fd2f7178502817f7361be2d8f62694b03585` | `git rev-parse 5ed7a3b8^{tree}` idéntico | ✓ |
| 5 | SHA-256 DEL MANIFIESTO | `0f08b961c31f03bbedbae700fa67029ac87b6b962067b39b3e504fe28e8d1939` | idéntico **en el commit del gate** | ✓ |
| 6 | SHA-256 DEL EMISOR (los dos commits) | `f1d5a3a9cb4c5f88…348c6715` | idéntico en `8c9ca9c3` **y** en `5ed7a3b8` | ✓ |
| 7 | SHA-256 DEL DERIVADOR (los dos commits) | `107fbb03f4440969…5bf78633` | idéntico en `8c9ca9c3` **y** en `5ed7a3b8` | ✓ |
| 8 | SEDE DEL OWNER (los dos commits) | `db46edd2af2aa48a…aa018d4a` | idéntico en los dos | ✓ |
| 9 | DIGEST `O17` (85 líneas) | `0cc5b9b5f30c878a…ec4e6125` | reproducido con el `awk` del propio sobre; 85 líneas | ✓ |
| 10 | DIGEST `O18` (111 líneas) | `ab9d94475545133f…16ed0353` | reproducido; 111 líneas | ✓ |
| 11 | DIGEST `O19` (78 líneas) | `cb2487fc0e7333e1…cce69ea8` | reproducido; 78 líneas | ✓ |
| 12 | **DIGEST DEL UNIVERSO · CANDIDATA** | `18f50dabfd46cbd5e8129cc7e205714091226b914f8223186f88d61fee84c8b4` | **REPRODUCIDO BYTE A BYTE** | ✓ |
| 13 | **DIGEST DEL UNIVERSO · GATE** | `c152f8519235ca28e36af23c90266d79a7a2295a6dfc901290a0580d3c60987a` | **REPRODUCIDO BYTE A BYTE** | ✓ |
| 14 | FUENTES OBLIGATORIAS 74 / 75 | candidata 74, gate 75 | mi conteo: 74 y 75 | ✓ |
| 15 | LINEAS OBLIGATORIAS 66747 / 66940 | — | mi conteo: 66747 y 66940 | ✓ |
| 16 | RUTAS EN QUE DIFIEREN LOS UNIVERSOS: 1 | el manifiesto del gate 5 | el manifiesto **no existe** en `8c9ca9c3` y sí en `5ed7a3b8`; diferencia única | ✓ |
| 17 | Encadenamiento | — | `5ed7a3b8` tiene por **padre** a `8c9ca9c3`; el gate es la candidata + 1 commit | ✓ |

Los digest de universo los recalculé con **la receta que el sobre publica**, no con la
mía y **sin ejecutar `emitir-sobre-de-ancla.py`**:

```bash
export PATH="/tmp/.../scratchpad/toolchain/shim:$PATH"; cd /home/jose/ads-kernel
for C in 8c9ca9c3920000bdf327cef7a6dbaf9aeff4eaeb 5ed7a3b805c472934cea9a4027d61e8ef7be5a35; do
  d=$(mktemp -d)
  GIT_INDEX_FILE="$d/idx" git read-tree "$C"
  GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
  python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null \
    | LC_ALL=C sort > "$d/rutas.txt"
  echo -n "COMMIT $C  FUENTES="; wc -l < "$d/rutas.txt"
  cat "$d/rutas.txt" | while read -r r; do
      echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done \
    | awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
  rm -rf "$d"
done
```

Salida literal:

```
COMMIT 8c9ca9c3920000bdf327cef7a6dbaf9aeff4eaeb  FUENTES=74
  DIGEST=18f50dabfd46cbd5e8129cc7e205714091226b914f8223186f88d61fee84c8b4
  LINEAS OBLIGATORIAS=66747
COMMIT 5ed7a3b805c472934cea9a4027d61e8ef7be5a35  FUENTES=75
  DIGEST=c152f8519235ca28e36af23c90266d79a7a2295a6dfc901290a0580d3c60987a
  LINEAS OBLIGATORIAS=66940
```

**Cero campos discrepantes. El sobre del gate 5 es sólido y el remedio anti-transcripción
funciona en su parte mecánica.**

**Las dos REF REMOTAS, resueltas contra el remoto de verdad — y una discrepancia entre mis
propios relevos, adjudicada.** El sobre nombra las refs como `refs/heads/…`, que es su nombre
**en el remoto**; localmente no resuelven con ese prefijo:

```
$ git rev-parse refs/heads/review/f4c-perimetro-derivado-candidate-20260831
fatal: ambiguous argument ... unknown revision or path not in the working tree.
```

`BB1` declaró haberlas resuelto con `git ls-remote origin`. `BB2` declaró expresamente lo
contrario —*«**No ejecuté `git ls-remote`**: el entorno de este relevo no tiene red»*— y
verificó sólo las copias locales `refs/remotes/origin/…`, diciéndolo contra su propio interés.
**Dos relevos de la misma cadena afirman cosas incompatibles sobre si había red.** Lo resolví
yo, que es lo que me toca:

```bash
$ git ls-remote origin | grep -E 'f4c-perimetro-derivado-candidate-20260831|f4c-gate-certificacion-5-20260831'
5ed7a3b805c472934cea9a4027d61e8ef7be5a35	refs/heads/review/f4c-gate-certificacion-5-20260831
8c9ca9c3920000bdf327cef7a6dbaf9aeff4eaeb	refs/heads/review/f4c-perimetro-derivado-candidate-20260831
```

**HAY RED, y las dos refs remotas apuntan exactamente a los dos commits del sobre.**
`BB1` tenía razón; `BB2` se equivocó sobre su entorno —no sobre los hechos: sus contrastes
locales coinciden con el remoto—. **Queda cerrado el único campo del sobre que ninguno de los
tres relevos podía dar por verificado en común, y lo cierro contra el remoto, no contra el
clon.** Lo hago constar porque un adjudicador que lea los tres informes encontrará la
contradicción y no encontrará quién la resolvió.

### 0.3 · LOS TRES BLOQUES EMBEBIDOS — mi tarea exclusiva

El encargo dice que los tres relevos embebieron el sobre en su informe y que compruebe
byte a byte que los tres bloques son el fichero original. **Corrí la comprobación y el
resultado no es el que el encargo presupone.**

| Relevo | ¿Embebe el sobre? | Dónde | Líneas / bytes | SHA-256 del bloque extraído | `diff` contra el original |
|---|---|---|---|---|---|
| `BB1` | **SÍ** | `informes/INFORME-BB1.md` L18–L207 (valla ` ``` ` en L17 y L208) | 190 / 14328 | `906b74f7…9070` | **IDÉNTICO, sin una sola diferencia** |
| `BB2` | **SÍ** | `informes/INFORME-BB2.md` L32–L221 (valla ` ```text ` en L31, cierre L222) | 190 / 14328 | `906b74f7…9070` | **IDÉNTICO, sin una sola diferencia** |
| `BB3` | **NO** | `notas/BB3.md` **no contiene ni una sola valla de código** | — | — | **no hay bloque que contrastar** |

Comando exacto:

```bash
cd /tmp/.../scratchpad
sed -n '18,207p' informes/INFORME-BB1.md > /tmp/bb1.blk
sed -n '32,221p' informes/INFORME-BB2.md > /tmp/bb2.blk
sha256sum SOBRE-GATE-5.txt /tmp/bb1.blk /tmp/bb2.blk
diff SOBRE-GATE-5.txt /tmp/bb1.blk && echo IDENTICO
diff SOBRE-GATE-5.txt /tmp/bb2.blk && echo IDENTICO
grep -c '^```' notas/BB3.md        # → 0
```

Salida:

```
906b74f70a30785465d56ecc68cf30e42b461febc7042e2a463aae5e8a899070  SOBRE-GATE-5.txt
906b74f70a30785465d56ecc68cf30e42b461febc7042e2a463aae5e8a899070  /tmp/bb1.blk
906b74f70a30785465d56ecc68cf30e42b461febc7042e2a463aae5e8a899070  /tmp/bb2.blk
IDENTICO
IDENTICO
```

**DICTAMEN SOBRE LA CONTAMINACIÓN POR TRANSCRIPCIÓN: NO LA HAY.**

Y lo digo con precisión, porque las dos mitades importan:

1. **Los dos bloques que existen son el fichero, byte a byte.** No hay ni un carácter
   de deriva. La vía por la que murió el gate anterior **está cerrada donde se usó.**
2. **`BB3` no transcribió el sobre en absoluto**, y lo dice explícitamente en
   `notas/BB3.md` L104: *«(la transcripción literal íntegra va en el informe entregado;
   el fichero es la sede)»*. Su entregable en disco es una **nota**, no un `INFORME-BB3.md`
   —no existe tal fichero: `find` sólo devuelve `INFORME-BB1.md`, `INFORME-BB2.md`,
   `INFORME-CC1.md` y `notas/BB3.md`—.

**Mi juicio sobre el punto 2, que es mío y no del encargo:** la premisa del encargo
(«los tres relevos embebieron el sobre») **es falsa para `BB3`**, y lo hago constar
porque un dictaminador que da por buena la premisa de su encargo no dictamina. Pero
**no lo cuento como contaminación, y aún menos como defecto de `BB3`**: no transcribir
es exactamente la conducta que el remedio del gate 5 persigue. `BB3` cita el fichero por
su SHA-256 correcto (`notas/BB3.md` L4 y L103) y remite a él como sede. **Un bloque que
no se escribe no puede diferir.** Si algo hay que corregir en el protocolo del gate 6 es
la obligación de embeber, no la abstención de `BB3`: **embeber el sobre reintroduce
exactamente el riesgo que el gate 5 quiso eliminar**, y sólo es inocuo mientras alguien
—yo— corra el `diff`. La forma robusta es la de `BB3`: citar el SHA-256 y no copiar.

**Consecuencia para `DD`: el gate 5 NO está contaminado por la vía del gate 4.**

---

## 1 · MANIFIESTO DE LECTURA

`ASIGNADO − LEÍDO = 1` fue una de las razones del veredicto anterior. Publico el mío entero,
incluidos los informes de relevo, y **declaro contra mi interés donde no cierra**.

### 1.1 · Los informes de mis tres relevos — LEÍDOS ÍNTEGROS

| fuente | líneas | leído | tramos | ¿íntegro? |
|---|---|---|---|---|
| `…/scratchpad/informes/INFORME-BB1.md` | 506 | L1–L17 y L208–L506 · el bloque L18–L207 **es el sobre**, contrastado por `diff` en §0.3 en vez de releído | 2 tramos | **SÍ** |
| `…/scratchpad/informes/INFORME-BB2.md` | 1081 | L1–L30 y L222–L1081 · el bloque L31–L221 **es el sobre**, ídem | 3 tramos (222-600 · 600-900 · 900-1081) | **SÍ** |
| `…/scratchpad/notas/BB3.md` | 332 | L1–L332, de una vez | 1 tramo | **SÍ** |

**No leí `informes/INFORME-CC1.md` (997 líneas): es de la cadena `CC`, no de la mía.** Existe en
el mismo directorio y lo hago constar para que nadie lo cuente como cobertura mía.

### 1.2 · Mi lote propio · los documentos 19–25

**PRIMERO, UN DEFECTO DEL ENCARGO QUE ES MÍO DECLARAR, PORQUE ME LO ENCONTRÉ AL ABRIRLO.**
De las siete rutas que mi encargo me asigna, **tres no existen**:

```bash
$ ls docs/evolucion/19-GATE-INDEPENDIENTE-F4C.md \
     docs/evolucion/20-GATE-DE-CIERRE-F4C.md \
     docs/evolucion/21-GATE-DE-CIERRE-F4C-SEGUNDA-RONDA.md
ls: docs/evolucion/19-GATE-INDEPENDIENTE-F4C.md: No such file or directory
ls: docs/evolucion/20-GATE-DE-CIERRE-F4C.md: No such file or directory
ls: docs/evolucion/21-GATE-DE-CIERRE-F4C-SEGUNDA-RONDA.md: No such file or directory
```

Los **números** son correctos y los documentos existen con otro **título**. Los localicé con
`ls -1 docs/evolucion/[0-9][0-9]-*.md` y los leí por su número, que es lo que el encargo
identifica sin ambigüedad. **Pero el hecho es que el encargo de este gate contiene tres rutas
derivadas a mano y equivocadas**, y es exactamente la clase de identificador escrito a mano que
el adjudicador `O` reprochó al coordinador en el documento 20 —*«la clase de identificador
derivado y escrito a mano que este expediente lleva doce tandas persiguiendo, y aparece en el
encargo del gate que viene a cerrarlo»*—. Lo registro como `BB-22`.

| # | fuente (nombre REAL) | líneas | SHA-256 (árbol de trabajo) | alcance leído |
|---|---|---|---|---|
| 1 | `docs/evolucion/19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md` | 1152 | `48baaa1a8e69c6ef…` | **veredicto, razones de cobertura y hallazgos** (encargo: «al menos») |
| 2 | `docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md` | 801 | `d7d2e4fa3f878e0c…` | ídem |
| 3 | `docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md` | 2679 | `9f869ffbdbdb834c…` | ídem |
| 4 | `docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md` | 3478 | `3e2bdece758e6b69…` | ídem |
| 5 | `docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md` | 2913 | `0f81f13d8cb319d8…` | ídem |
| 6 | `docs/evolucion/24-TERCER-GATE-DE-CERTIFICACION-F4C.md` | 2515 | `8df584529c857c07…` | ídem |
| 7 | **`docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md`** | **2754** | `e8431c653cb7919e…` | **ÍNTEGRO**, y **el último que abrí** |

**El 25, íntegro, con sus tramos:** L1-190 · L190-520 · L542-720 · L1078-1137 · L1997-2141 ·
L2359-2396 · L2396-2606 · L2606-2754, más el mapa completo de sus 52 cabeceras
(`grep -n '^# \|^## '`). **Primera sección sustantiva:** `## 0 · Qué es este documento` (L9).
**Última:** `## 16 · CIERRE` (L2738).
**ANCLA A, L2451:** «*Es la CUARTA recurrencia de la clase (K-01/J-10/L-01 · P-05≡Q-08/R-02 ·
S-17≡S3-05 · esta).*»
**ANCLA B, L2523 (a 72 líneas):** «*recurrencia consecutiva de ese modo de fallo sobre el mismo
fichero.*»

**LA RESTA, DICHA SIN ADORNO.** El encargo dice de los ficheros 19–24 «**al menos** sus
veredictos, sus hallazgos y sus notas de reincidencia», y del 25 «**íntegro**».
**El 25 lo leí íntegro. Los 19–24 NO los leí íntegros**, y no los declaro leídos: de sus 13 538
líneas abrí las cabeceras, los veredictos, los bloques de hallazgos y los barridos de
reincidencia. **Es lo que el encargo pide, y aun así lo digo así y no «LEÍDO ÍNTEGRO»**, porque
este expediente ha castigado tres veces la resta maquillada. **Sobre mi lote, `ASIGNADO −
LEÍDO = 0` bajo el criterio del encargo, y NO bajo el criterio de lectura íntegra.** Que el
adjudicador use el que corresponda y no el que me convenga.

### 1.3 · Fuentes que abrí para VERIFICAR, y que no declaro leídas

`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` (las sedes concretas de cada hallazgo que
reproduzco, ~25 regiones) · `docs/owner/ADS-OWNER-RESOLUCIONES.md` (L192 y los tres bloques de
resolución vía `awk`) · `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` (L741-845, L779, L1122) ·
`docs/evolucion/CHECKPOINT-ADS-NEXT.md` (L17, L2349-2354, las 7 cabeceras «Siguiente acción») ·
`docs/evolucion/00-INDICE.md` (L88, L92, L93-95, L112-125, L174-180) · el manifiesto del gate 5
**en el commit del gate**, íntegro (193 líneas) · el manifiesto **4B** del gate 4 · los dos
`derivar-universo-obligatorio.py` (gate 4 y gate 5, zona `ZONAS_DEL_ENCARGO`) ·
`comprobar-correccion-gate-de-cierre.py` (bloque `G-10`, L586-597) · los validadores
`registrar_evidencia.py` y `comprobar_referencias.py`, **ejecutados en checkouts aislados**.

---

## 2 · HALLAZGOS QUE SOSTENGO

**Regla que me impongo: sólo entra lo que reproduje YO, con MI comando.** Severidad **mía**.
Criterio, el de los cinco gates: **BLOQUEANTE** obliga a decidir arquitectura nueva · **GRAVE**
una garantía publicada no se sostiene · **MEDIO** una afirmación vigente es falsa sin cambiar el
comportamiento · **MENOR** editorial o de propagación.

**Y una regla de graduación propia, que declaro antes de aplicarla:** *la reincidencia sube la
severidad un escalón cuando el gate anterior no sólo la nombró, sino que dejó el remedio
escrito.* No es benevolencia invertida: un defecto con remedio escrito y no aplicado mide
disciplina, y la disciplina es lo único que el cuarto gate dijo que faltaba.

---

### `BB-01` · **GRAVE** · origen `BB3-04` · el commit del gate deja el árbol que juzga con un validador canónico en ROJO — **QUINTA recurrencia consecutiva, con el remedio ya escrito**

**Fichero y línea.** `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md`,
creado por el commit del gate `5ed7a3b8`. La regla incumplida: `docs/evolucion/00-INDICE.md`
**L115-121**.

**Cita literal de la regla, del árbol auditado:**

> **LA REGLA, y es de cumplimiento obligatorio para el gate siguiente.** Todo documento que
> `C-L.5` obligue a publicar —manifiesto de asignación, manifiestos de lectura, addenda y
> corrigenda— **se enlaza desde la lista de abajo en el MISMO commit que lo crea**. […]
> **Quien publique un manifiesto sin enlazarlo aquí deja el árbol que juzga con un validador
> canónico en rojo, causado por el aparato del propio gate.**

**MI COMANDO DE REPRODUCCIÓN.** Lo hice en **checkouts aislados de los dos árboles**, fuera del
repositorio, para no ensuciar el árbol de trabajo:

```bash
W=/tmp/.../scratchpad/BB4work
for C in 8c9ca9c3920000bdf327cef7a6dbaf9aeff4eaeb 5ed7a3b805c472934cea9a4027d61e8ef7be5a35; do
  GIT_INDEX_FILE="$W/idx-$C" git read-tree "$C"
  GIT_INDEX_FILE="$W/idx-$C" git checkout-index -a --prefix="$W/$C/"
  ( cd "$W/$C" && python3 kernel/operativo/validadores/registrar_evidencia.py )
done
```

**MI SALIDA, literal:**

```text
ARBOL CANDIDATO  8c9ca9c3…   13/13 validadores en verde · 13 evidencias publicadas · 0 problemas   RC=0
ARBOL DEL GATE   5ed7a3b8…   FALLO  referencias  código 1  NO publicada
                             12/13 validadores en verde · 12 evidencias publicadas · 1 problemas  RC=1
```

```bash
$ cd "$W/5ed7a3b8…" && python3 kernel/operativo/validadores/comprobar_referencias.py --exclusiones
T147  FALLIDA   Todo documento es alcanzable por ruta, y ninguna referencia es ambigua
   · docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md:
     no lo alcanza ningún enlace por ruta, ninguna referencia de campo y ninguna cita de sus
     identificadores. Existe para nadie
documentos analizados: 264
0 superadas · 1 fallidas          RC=1
```

**Y la tercera mitad, que `BB3` nombró y yo confirmo con precisión** —la batería reescribe
ficheros de evidencia sobre el árbol del gate y **ninguno** sobre la candidata—:

```bash
for f in $(git ls-tree -r --name-only $C | grep 'pruebas/evidencia/'); do
  a=$(git show "$C:$f" | sha256sum | cut -c1-16); b=$(sha256sum "$W/$C/$f" | cut -c1-16)
  [ "$a" != "$b" ] && echo "DIFIERE $f"; done
```
```text
CANDIDATA 8c9ca9c3…   ficheros modificados por la batería: 0
GATE      5ed7a3b8…   DIFIERE kernel/operativo/pruebas/evidencia/fuentes-salida.txt
                      DIFIERE kernel/operativo/pruebas/evidencia/negativos-salida.txt
                      ficheros modificados por la batería: 2
```
Y el contenido del cambio nombra la causa: `T161-cobertura` publica **309** ficheros y el corpus
del árbol del gate da **310**; el huérfano detectado pasa de
`kernel/operativo/capacidades/DIS/huerfano/composicion.md` (material de prueba, deliberado) a
**el manifiesto de este gate**.

**`BB3` ACERTÓ EN LOS TRES EXTREMOS**, incluidos los dos nombres de fichero exactos. **SOSTENIDO
ÍNTEGRO.**

**¿REINCIDENCIA DE QUÉ?** De la clase mejor documentada del expediente, y voy con los
identificadores de origen delante:

```text
doc 23   `S-18` ≡ `T-14`        el manifiesto sin enlazar · `T147` en rojo          1.ª
doc 24   `V-06` ≡ `X-07`        «reincidencia literal de S-18≡T-14»                 2.ª
doc 24   `W-16`                 «REINCIDE, idéntico, un gate después»               3.ª (mismo gate, otro revisor)
doc 25   `Y-03` + `Y-04` ≡ `Z-09`  «TERCERA/CUARTA recurrencia consecutiva»          4.ª
doc 26   **este gate**                                                              **5.ª**
```

**Y lo que lo agrava por encima de todos los anteriores, y es MÍO, del documento 25 §8 que sólo
yo he leído:** el dictaminador `Y4` **ya juzgó la excusa y la rechazó, y dejó el remedio escrito
en una línea**:

> **JUZGO: la tensión es REAL, y NO es insatisfacible. La recurrencia no queda excusada.**
> […] **LA SALIDA, y es de una línea:** el commit del manifiesto lleva **el manifiesto, su fila
> en `00-INDICE` y la evidencia derivada reejecutada**, y sigue siendo anterior a todo revisor.
> Cumple `C-L.5`, cumple el campo 6, cumple `00-INDICE` L114-120, cumple la regla nueva, y deja
> el árbol que se juzga con `T147` en verde y su evidencia verdadera.

**El commit `5ed7a3b8` toca UN SOLO fichero.** No llevó la fila del índice ni la evidencia
reejecutada. **La quinta recurrencia se comete con el remedio escrito, medido y publicado por
la cadena anterior.** Esto no es deuda: es la medida de la disciplina, y sale negativa.

---

### `BB-02` · **GRAVE** · origen `BB3-03` · el manifiesto del gate declara sus cifras «sobre el árbol del GATE» y son las de la CANDIDATA — reincidencia de una clase que el gate anterior declaró ROTA

**Fichero y línea.** El manifiesto, **L37**, en el commit del gate.

**Cita literal:**

> `UNIVERSO DERIVADO   74 fuentes · 66 747 líneas —sobre el árbol del GATE—`

**MI COMANDO DE REPRODUCCIÓN** — la receta del propio sobre, ya publicada en §0.2:

```text
ARBOL CANDIDATO  8c9ca9c3…   74 fuentes · 66 747 líneas · digest 18f50dab…
ARBOL DEL GATE   5ed7a3b8…   **75 fuentes · 66 940 líneas** · digest c152f851…
```

**74 y 66 747 son, exactamente, las cifras de la CANDIDATA.** El árbol del GATE da 75 y 66 940.
El rótulo nombra el árbol equivocado. **SOSTENIDO.**

**¿REINCIDENCIA DE QUÉ?** De `U-02` (doc 23) → `X-06`≡`V-23` (doc 24). Y aquí está lo que sólo
puede decir quien haya leído el 25: **el adjudicador `AA` la declaró ROTA hace un gate**, y lo
puso entre las diez cosas que «*SÍ ha quedado cerrado, y no es cortesía*»:

> **5. `X-06`≡`V-23` CERRADO, Y LA REINCIDENCIA ROTA**: verifiqué las **70 filas contra los dos
> árboles** y el manifiesto **nombra el árbol de sus cifras**.

Y **el propio sobre de este gate** manda mirarla primero, en su obligación 3: *«La fila del
propio derivador es la que el gate anterior falseó dos gates seguidos (`U-02`, y su reincidencia
`X-06`): mírela primero»*. **Se rompió la reincidencia y se rehízo en el gate siguiente, en el
campo que el sobre señala con el dedo.**

**LO QUE NO SOSTENGO DE `BB3-03`, Y ES LA MITAD QUE IMPORTA: ver `BB-03`.** `BB3` concluye que
«su `OBLIGATORIO − ASIGNADO = 0` es en realidad 1». **La resta a 0 es CORRECTA**, y lo demuestro
abajo. Lo falso es el rótulo, no la aritmética.

---

### `BB-03` · **MEDIO · ESTRUCTURAL** · **HALLAZGO MÍO, que ningún relevo podía ver** — el remedio de `AA-01` hizo el manifiesto FILA DE SU PROPIO UNIVERSO, y con eso `OBLIGATORIO − ASIGNADO = 0` sobre el árbol del gate es INSATISFACIBLE

Esto es lo que el encargo me pide decidir «no dándolo por hecho en ninguna dirección».
**Lo decido, y decido contra mi propio relevo en su segunda mitad.**

**PRIMERO, LA ARITMÉTICA, MEDIDA POR MÍ EN LAS DOS DIRECCIONES:**

```bash
git show $G:$M | grep -oE '^\| *[0-9]+ \| `[^`]+`' | sed 's/.*`\(.*\)`/\1/' | LC_ALL=C sort -u > /tmp/asignadas.txt
comm -23 <universo> /tmp/asignadas.txt   # en el universo y sin asignar
comm -13 <universo> /tmp/asignadas.txt   # asignadas y fuera del universo
```
```text
FILAS DEL MANIFIESTO                                74   (74 brutas · 74 únicas · 0 duplicadas)

vs UNIVERSO DE LA CANDIDATA (74)
  en el universo y sin asignar    0
  asignadas y fuera del universo  0          →  **OBLIGATORIO − ASIGNADO = 0. CIERRA AL DÍGITO.**

vs UNIVERSO DEL GATE (75)
  en el universo y sin asignar    1  docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md
```

**SEGUNDO, QUÉ OBJETO DECLARA EL MANIFIESTO REPARTIR.** Su §1, cita literal:

> `COMMIT CANDIDATO   8c9ca9c3920000bdf327cef7a6dbaf9aeff4eaeb`
> `TREE SHA           91fe62d369152f9d1b58361f0ffc888358364175`

**El objeto del reparto es la CANDIDATA.** Contra la candidata, la resta da 0 y las 74 filas
cuadran sin una discrepancia. **La aritmética del manifiesto es correcta para el objeto que él
mismo declara.** `BB3` la midió contra el otro árbol.

**TERCERO, Y ES LO QUE NADIE HA DICHO: la resta a 0 sobre el árbol del GATE es
ESTRUCTURALMENTE IMPOSIBLE, y la imposibilidad la creó el remedio del gate anterior.**

Comparé los dos gates:

```bash
# ¿está el manifiesto en curso dentro de su propio universo?
grep -c '4B-20260830'                  <rutas del universo del gate 4>   # → 0
grep -c 'CERTIFICACION-5-20260831'     <rutas del universo del gate 5>   # → 1
```
```text
GATE 4   manifiesto 4B · 70 filas · universo del gate 70
         → comm en las DOS direcciones: 0 y 0.  CIERRA CONTRA EL ÁRBOL DEL GATE
         el manifiesto 4B **no está** en su propio universo
GATE 5   manifiesto 5  · 74 filas · universo del gate 75
         → el manifiesto 5 **SÍ está** en su propio universo
```

**Qué cambió, en el código, entre uno y otro** (`diff` de los dos derivadores):

```text
GATE 4  ENCARGO enumera los manifiestos como RUTAS LITERALES, una fila por manifiesto
        publicado. El del gate en curso no tiene fila porque aún no existía al escribirse
GATE 5  MANIFIESTOS = "docs/evolucion/verificacion/manifiestos" entra como ZONA BARRIDA
        # `Z2-02`≡`Z-03`, la otra mitad: los manifiestos también estaban escritos fila a fila,
        # y el del propio gate en curso **no estaba en ninguna**. […]
        # **El perímetro se DERIVA, no se enumera.**
```

Ese cambio es **el remedio que `AA` determinó para `AA-01` y `Z-03`**, y es correcto: cierra que
un segundo documento del Owner por la vía sancionada quede fuera del universo. **Pero al barrer
`manifiestos/` entero, mete al manifiesto del gate en curso dentro de su propio universo.** Y
entonces, para que la resta cerrase a 0 sobre el árbol del gate, el manifiesto tendría que
llevar **una fila sobre sí mismo con su propio SHA-256** — cada fila del reparto publica ruta,
líneas y SHA-256—. **Un fichero no puede contener su propio SHA-256: es un punto fijo de
SHA-256.** No es difícil: es imposible.

**MI DICTAMEN SOBRE QUÉ SIGNIFICA PARA LA VALIDEZ DEL GATE — y lo separo en tres, porque
mezclarlos es lo que produjo el desastre anterior:**

1. **El rótulo de L37 es FALSO y es reincidencia.** Eso es `BB-02`, y se sostiene entero. Coste
   de arreglarlo: cambiar cinco palabras.
2. **La resta del manifiesto NO está falseada.** Cierra a 0 contra el árbol que el manifiesto
   declara repartir. **No sostengo que sea «en realidad 1».**
3. **`OBLIGATORIO − ASIGNADO = 0` sobre el árbol del gate dejó de ser una condición alcanzable
   el día que `manifiestos/` pasó a ser zona barrida.** Es un **defecto de diseño heredado del
   remedio de `AA-01`**, no una falta del coordinador de este gate. Mientras no se resuelva,
   **cualquier gate futuro medido contra su propio árbol dará 1**, y el gate siguiente lo
   registrará como reincidencia sexta de algo que nadie puede cumplir.

**¿INVALIDA EL GATE? NO, Y LO DECIDO EXPRESAMENTE.** El disparador de invalidez que el sobre y
§11.6 definen es **una diferencia entre el SOBRE y lo que el árbol muestra**, o **entre los
sobres entregados**. **No hay ninguna de las dos**: los 17 campos del sobre reproducen (§0.2) y
el sobre no se transcribió (§0.3). Un rótulo equivocado **dentro del manifiesto** es un
hallazgo del gate, no un defecto de su ancla. **Decido que el gate 5 es VÁLIDO por esta vía**, y
dejo dicho que la decisión de validez es de `DD` y que le entrego el hecho, no la conclusión.

**REMEDIO DETERMINADO, y es de resta como `AA` ordenó:** o el manifiesto rotula «—sobre el árbol
CANDIDATO—», que es una palabra; o la regla de cierre se enuncia explícitamente contra el árbol
candidato, que es donde siempre tuvo sentido. **Ninguna de las dos escribe una protección
interna nueva.**

---

### `BB-04` · **GRAVE** · origen `BB2-02` · «**CI o** el ejecutor externo» bajo rótulo LITERAL — **reincidencia LITERAL de `Y-09`, con la orden de retirarla ya dada**

**Fichero y línea.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L8687**, bajo el rótulo de
L8674 «*EL REPARTO, LITERAL DE LA SEDE CANÓNICA DEL OWNER, RATIFICADO MEDIANTE `O19`*».

**Cita literal, del árbol auditado:**

> `Y UNA PROHIBICIÓN    **CI o el ejecutor externo NO puede compartir la misma identidad de`
> `DE IDENTIDAD         escritura del runtime ADS.**`

**La SEDE CANÓNICA, L192, cita literal:**

> `· el ejecutor externo no puede compartir la identidad de escritura del runtime ADS`

**MI COMANDO:**

```bash
$ sed -n '8687p' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
$ sed -n '192p'  docs/owner/ADS-OWNER-RESOLUCIONES.md
$ grep -c '\bCI\b' docs/owner/ADS-OWNER-RESOLUCIONES.md
0
$ grep -rn "no puede compartir" docs/
docs/owner/ADS-OWNER-RESOLUCIONES.md:192:· el ejecutor externo no puede compartir…
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md:1122:· el ejecutor externo no puede compartir…
```

**Dos golpes en todo `docs/`, ninguno con «CI». §11.8 es el único outlier, y es la sede rotulada
literal. SOSTENIDO.**

**¿REINCIDENCIA DE QUÉ? De `Y-09` del documento 25, LITERAL.** No de su clase: **del hallazgo
mismo**, con el mismo texto, la misma sede y el mismo `grep` dando cero:

> **`Y-09`** · **§11.8 L8590 escribe «`CI` o el ejecutor externo» bajo rótulo «LITERAL DE LA
> SEDE CANÓNICA DEL OWNER»**; la sede L193 dice sólo «el ejecutor externo» y no contiene «CI»
> (`grep -c` = 0). Amplía el sujeto de una prohibición del Owner bajo etiqueta de literalidad.

`AA` lo adjudicó **MEDIO**, lo clasificó **A+B**, y lo puso entre las cuatro cosas que su orden
de cierre manda retirar, con estas palabras:

> «*y que se retiren cuatro comillas que atribuyen al Owner texto que su sede no contiene*»

**Yo lo subo a GRAVE**, por mi regla de graduación: el remedio estaba escrito («retirar dos
palabras»), la orden estaba dada por el adjudicador del gate anterior, el coste es nulo, y la
tanda que se somete a este gate **no lo hizo**. Y hay una razón material además de la
disciplinaria: **`X-O13` del propio documento 11 tipifica este escenario y su resultado exigido
es FALLA CERRADO**. El corpus contiene la fila adversarial que describe su propio defecto.

---

### `BB-05` · **GRAVE** · origen `BB3-01` · «robustez y revalidación permanente…» se atribuye al Owner en dos sedes VIVAS y da CERO en la sede canónica — **reincidencia de `Y-05`, que sobrevivió porque el remedio se aplicó a las comillas y no a la atribución**

**Fichero y línea.** `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` **L779** y
`docs/evolucion/00-INDICE.md` **L88**.

**Citas literales:**

> **L779:** `**MOTIVO DE LA ELECCIÓN, en las palabras del Owner:** *robustez y revalidación`
> `permanente por encima del ahorro operativo*`
>
> **00-INDICE L88:** `su motivo, **en sus palabras**, es **robustez y revalidación permanente`
> `por encima del ahorro operativo**`

**MI COMANDO:**

```bash
$ grep -c robustez docs/owner/ADS-OWNER-RESOLUCIONES.md
0
$ sed -n '779p' docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md
$ sed -n '88p'  docs/evolucion/00-INDICE.md
```

**Cero apariciones en la sede canónica. Dos sedes vivas, sin marca histórica, atribuyéndolo al
Owner con las fórmulas «en las palabras del Owner» y «en sus palabras». SOSTENIDO.**

**¿REINCIDENCIA DE QUÉ? De `Y-05` del doc 25** —*«tres citas entrecomilladas atribuidas al Owner
que la SEDE CANÓNICA no contiene»*, GRAVE, clase A+B, razón 5 del veredicto de `AA`— **y de la
clase `X-O13`, que es literalmente la razón de existir de `O19`.**

**Y `BB3` diagnosticó POR QUÉ sobrevivió, que es la parte que vale.** El remedio de la tanda
barrió *«las citas ENTRECOMILLADAS atribuidas al Owner que dan CERO en la sede»*. **Ésta no va
entrecomillada: va en cursiva y en negrita.** El remedio se escribió sobre la **forma
tipográfica** y no sobre el **acto de atribuir**. Es la firma del método que `AA` describe
—*«cada hallazgo se cierra con la forma exacta de su contraejemplo»*— aplicada a la letra.

**Corolario que sostengo con `BB3`:** la cabecera vigente del checkpoint **L58** afirma «*cero
amplificación en la proyección*». Sobre este árbol y para la proyección de `O17`, **es falsa**.

---

### `BB-06` · **GRAVE** · origen `BB2-01` · `C-L.5` tiene DOS estados vigentes, y la sede que el documento designa como propia publica el caducado

**Fichero y línea.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L11368** (cabecera),
**L11493-11494** (cierre) y **L8230** (arrastre a §11.6).

**Citas literales, del árbol auditado:**

> **L11368:** `## \`C-L.5\` · La condición de COBERTURA del próximo gate — **CERTIFICADA por el documento 21**, y vigente para todo gate posterior`
> **L11493:** `**Estado: CERTIFICADA por el GATE INDEPENDIENTE DE CIERRE CON MANIFIESTOS VERIFICABLES**`
> **L8230:** `**SEDE ÚNICA.** Ésta es la sede del SOBRE DE ANCLA: \`C-L.5\` —la condición de cobertura, **certificada y vigente para todo gate posterior**—`

**Contra tres sedes vigentes del mismo árbol, verificadas por mí:**

```bash
$ sed -n '17p' docs/evolucion/CHECKPOINT-ADS-NEXT.md
> `C-L.5` pasa de CERTIFICADA a ABIERTA, por primera vez en cuatro gates.**
$ sed -n '92p' docs/evolucion/00-INDICE.md          # fila del doc 25
… **`C-L.5` pasa de CERTIFICADA a ABIERTA, por primera vez en cuatro gates** …
$ git show 5ed7a3b8:…/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md | sed -n '26,27p'
ESTADO DECLARADO   APLICADO y NO CERTIFICADO · `F4c` ABIERTA · … · **`C-L.5` ABIERTA** · `C-L.7` NO CERRADA
```

**CUATRO SEDES, DOS ESTADOS. Y la que discrepa es la que el propio documento designa como sede
de la condición. SOSTENIDO.**

**Y ahora lo que `BB2` no podía hacer y yo sí: RESOLVER cuál rige.** `BB2` dejó la tensión
abierta a propósito (su §4.2: *«el cuarto gate fue INVÁLIDO, y un gate inválido no produce
veredicto»*). **La cierro con el documento 25 delante, y cae del lado ABIERTA por dos vías
independientes:**

1. **`AA` reabrió `C-L.5` como adjudicación expresa, no como consecuencia del veredicto.** Doc
   25 §11, tabla de las trece condiciones: «`C-L.5` | **CERTIFICADA POR COBERTURA** | **NO SE
   SOSTIENE. La reabro, y es la primera vez en cuatro gates.** […] Queda **ABIERTA**». Y §2:
   «`C-L.5` pasa de CERTIFICADA a **ABIERTA**».
2. **La reapertura se funda en una resta aritmética, no en un juicio de fondo.** `ASIGNADO −
   LEÍDO = 1`, y la regla de cierre de la propia `C-L.5` dice «*con independencia de los
   hallazgos*». Esa medición no depende de que el gate produjera veredicto.

**Luego el estado vigente es ABIERTA, y el documento 11 es el único de los cuatro que discrepa.
El hallazgo queda limpio y sin la reserva que `BB2` dejó.**

**¿REINCIDENCIA DE QUÉ?** De `P-22`≡`Q-37` (doc 22), que corrigió esta misma sección **por
llevar dos estados dentro de sí misma**. La corrección los redujo a uno y marcó el otro
`[HISTÓRICO]`. **Sobrevivió el que caducó**, y el bloque marcado `[HISTÓRICO]` en L11385-11388
—«abierta, y no la cierra esta tanda»— es hoy el que describe la realidad.

---

### `BB-07` · **GRAVE** · origen `BB3-05` · el checkpoint afirma en presente que `C-L.5` «SIGUE CERTIFICADA» y que doce condiciones están cerradas — en el renglón que declara no copiar estados

**Fichero y línea.** `docs/evolucion/CHECKPOINT-ADS-NEXT.md` **L2349-2354**, sección «Estado de
las fases».

**Cita literal:**

> `SUS TRECE CONDICIONES C-L.1–C-L.13 están APLICADAS —doce cerradas o registradas—. C-L.5, la`
> `COBERTURA, quedó CERTIFICADA por el gate del documento 21 y SIGUE CERTIFICADA tras el del 22,`
> `ahora sobre universo derivado; el estado de cada C-L NO se copia aquí, sino que lo da la`
> `clasificación VIGENTE de este mismo fichero, más abajo.`

**MI COMANDO:**

```bash
$ sed -n '2349,2354p' docs/evolucion/CHECKPOINT-ADS-NEXT.md
$ sed -n '17p' docs/evolucion/CHECKPOINT-ADS-NEXT.md     # el MISMO fichero, cabecera
> `C-L.5` pasa de CERTIFICADA a ABIERTA, por primera vez en cuatro gates.**
```

**El mismo fichero se contradice entre su L17 y su L2349, en presente y sin marca histórica.**
Y por §11 del doc 25, las cerradas o registradas son **once**, no doce: `C-L.5` ABIERTA y
`C-L.7` NO CERRADA. **SOSTENIDO.**

**Doblemente defectuoso, y ésta es la parte que lo hace GRAVE:** el renglón **copia** el estado
en la misma frase en que declara **no copiarlo**. Es la forma exacta de `AA-02` —*«una
consecuencia declarada que es FALSA en el commit que la escribe»*—, en el fichero que va al
Owner. **`AA` la contó como QUINTA recurrencia consecutiva de la clase que `C-L.7` existe para
cerrar** (`K-01`/`J-10`/`L-01` · `P-05`≡`Q-08`/`R-02` · `S-17`≡`S3-05` · `X-04` · `AA-02`).
**Ésta es la sexta.**

---

### `BB-08` · **GRAVE** · origen `BB1-03` + `BB1-05` · `D105` sigue sin propagar a tres sedes normativas, una de ellas quince líneas por encima de la nota que la corrige — **residuo directo de `Y-02`**

**Fichero y líneas.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L1200**, **L1215** y
**L2572**.

**Citas literales, del árbol auditado:**

> **L1200** (§2.6.4, discriminador «observable en el diario»):
> `ABANDONADA      el terminal es \`abandonada\` · marcador retirado · queda un \`deriva\``
>
> **L1215** (tabla de cardinalidad, columna `abandonada`):
> `| marcador | retirado | retirado | **retirado** |`
>
> **L2572** (§2.6.9, bloque `NINGÚN ESTADO ALCANZABLE QUEDA SIN SALIDA`):
> `\`derivada\` y \`abandonada\` son terminales POR DEFINICIÓN y retiran el marcador.`

**Contra su gemela `X58`, L1633, que dice lo contrario Y declara que ésa era la forma
defectuosa:**

> `**\`derivada\` retira el marcador; \`abandonada\` NO lo retira en su emisión**, y el marcador
> sobrevive hasta que su \`deriva\` es durable y su marcador existe (\`D105\`…)`

**MI COMANDO:**

```bash
$ sed -n '1198,1201p;1213,1216p;2572,2573p;1633p' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
$ grep -n 'propagación de `D105`' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
# seis sedes marcadas — y L1200, L1215 y L2572 NO están entre ellas
```

**SOSTENIDO.** Y sostengo la lectura de `BB1` sobre por qué no es benevolentemente
interpretable: L1195-1200 se declara a sí mismo **discriminador observable**, y en la ventana
`W17` (`abandonada` durable, `deriva` no durable) da la respuesta contraria.

**¿REINCIDENCIA DE QUÉ? De `Y-02` del doc 25**, GRAVE, razón 3 del veredicto de `AA`:
*«`D105` sin propagar a OCHO sedes vivas»*, con la lista L796 · L1179 · L1241 (`W11`) · L1352 ·
L1579 (`X55`) · L1582 (`X58`) · L2304.

**Y aquí tengo que ser justo con la tanda, porque un dictaminador que sólo acumula no dictamina:
la propagación SÍ se hizo, y funcionó donde más importaba.** `BB1` verificó y yo confirmo que
**`X55` y `X58` están hoy CORRECTAMENTE corregidas** —eran dos de las ocho sedes de `Y-02`, y
son los **contratos de prueba de `F6`**—. Lo que sobrevive son **sedes normativas en prosa**.
**Es la inversión del defecto anterior:** el gate 4 encontró los contratos rotos y la norma
bien; el gate 5 encuentra los contratos bien y la norma rota. **La tanda arregló lo que se le
señaló, con la forma exacta de lo que se le señaló, y no barrió la clase.** Séptima instancia
del patrón que `AA` llamó «el remedio abre la puerta contigua», y esta vez la puerta es la de al
lado literalmente: **L1215 está quince líneas por encima de la nota que la corrige (L1220-1228).**

---

### `BB-09` · **GRAVE** · origen `BB1-02` · `X-S1–X-S9` es falso —son once— y el propio documento ya dictaminó, en otra sede, que esa cadena viola la regla de §0

**Fichero y línea.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L403**.

**Cita literal:** `X-S1–X-S9   las filas adversariales de la FASE 0, §9.6. Con guion, letra y número`

**MI COMANDO** — y publico el error que cometí al reproducirlo, porque importa:

```bash
$ grep -oE 'X-S[0-9]+' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | sort -u | tail -3
X-S7 X-S8 X-S9          ← MI PRIMER INTENTO. Me hizo creer que BB1-02 era FALSO
$ grep -oE 'X-S[0-9]+' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | sort -u -V | tr '\n' ' '
X-S1 X-S2 X-S3 X-S4 X-S5 X-S6 X-S7 X-S8 X-S9 X-S10 X-S11
$ grep -cE '^\| `X-S[0-9]+`' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
11
$ grep -n 'X-S1[01]' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
7799: | `X-S10` … 7800: | `X-S11` …
```

**`sort -u` sin `-V` ordena alfabéticamente y coloca `X-S10`/`X-S11` entre `X-S1` y `X-S2`.**
Estuve a punto de declarar falso un hallazgo verdadero por un ordenador lexicográfico. Lo dejo
escrito en §7. **La tabla de §9.6 lleva ONCE filas. `BB1-02` es CORRECTO. SOSTENIDO.**

**Lo que lo hace GRAVE y no MEDIO:** el propio documento **ya dictaminó esta cadena**, en
**L10736-10739**:

> `**Y el cardinal de \`X-S\` deja de escribirse aquí**: este bloque decía «las NUEVE
> \`X-S1\`–\`X-S9\`» y la tabla de §9.6 lleva más, que es el titular caducado que la regla de §0
> prohíbe`

**El documento identificó el defecto, lo retiró de §19, y dejó la cadena literal intacta en
§2.1**, que es la **sede definitoria** y la que gobierna la prueba de `D83` contratada para
`F6`. **Corregir la sede que no manda y dejar la que manda** es la firma del método, otra vez.

**¿REINCIDENCIA?** De la clase `Y-07` (doc 25) ≡ `V-09`…`V-13`, `V-19` (doc 24) — la regla de
titulares de §0 sin guardián. `AA` la declaró **deuda anterior nunca barrida** porque **no tiene
guardián**, y verifiqué que sigue sin tenerlo: `grep -cniE 'titular|regla de titulares'` sobre
la batería devuelve **0**.

---

### `BB-10` · **MEDIO** · origen `BB1-01` · el censo de la familia `X` dice CUATRO poblaciones y hoy son CINCO

**Fichero y línea.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L396**.

**Cita literal:** `**El prefijo \`X\` lo usan hoy CUATRO poblaciones de este documento**, y se nombran para que nadie tenga que descubrirlo:` — seguida del bloque L399-403 con cuatro renglones: `X1–X8`, `X01–X62`, `X-A–X-H`, `X-S1–X-S9`.

**MI COMANDO:**

```bash
$ sed -n '394,406p' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md   # el censo: cuatro renglones
$ grep -cE '^\| `X-O[0-9]+`' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
13
$ sed -n '10736,10737p' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
… §9.6 es la sede de la familia `X-S` y **§11.6 la de la familia `X-O`**.
```

**Existe una quinta población, `X-O1`–`X-O13`** —la tabla adversarial del SOBRE DE ANCLA—, y
**el propio documento la reconoce en L10736**. No está en el censo de §2.1, que lleva un bloque
normativo a cuatro líneas: *«ninguna población nueva de prefijo `X` puede introducirse sin
añadir su renglón a la lista de arriba»*. **SOSTENIDO.**

**MEDIO y no GRAVE, y digo por qué contra el criterio de mi relevo:** a diferencia de `BB-09`,
aquí el censo no afirma una cifra falsa **sobre una tabla existente**; omite una población
nacida después. El daño a `F6` es de completitud del censo de `D83`, no de contrato de prueba.
**Misma clase `Y-07`, menor consecuencia.**

---

### `BB-11` · **MEDIO** · origen `BB1-04` · el titular «Tres cosas cambian» encabeza CINCO rótulos — y es la clase que tres gates no vieron porque no es una cabecera

**Fichero y línea.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L1764**.

**Cita literal:** `**Tres cosas cambian para que la regla sea ejecutable sin herramienta**, que es lo que \`R1\` exige:`

**MI COMANDO:**

```bash
$ grep -n 'Tres cosas cambian' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
1764:**Tres cosas cambian para que la regla sea ejecutable sin herramienta**…
$ sed -n '1768,1832p' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | grep -nE '^[`A-ZÁÉÍÓÚ]'
# cinco rótulos: L1768 · L1777 · L1801 · L1805 · L1824
```

**SOSTENIDO.** Y sostengo el diagnóstico de `BB1`, que es lo que le da valor: el rótulo 2 lo
**añadieron `D78` y `D88`** —el propio texto lo dice— y nadie volvió a la frase que los cuenta.
Es el modo de fallo que §0 describe con sus palabras: *«quien añade el elemento no está obligado
a pasar por la frase que lo cuenta»*.

**Y la observación de método que traslado a `DD` porque vale más que el hallazgo:** `BB1`
verificó **una a una las 23 cabeceras `#`…`####` con cardinal de L1-5800 y las 23 son ciertas
hoy**. El superviviente **no es una cabecera: es una frase introductoria en negrita.** Los
barridos de tres gates fueron sobre `^#`. **Si alguien ordena un barrido para el gate 6, que sea
sobre `^\*\*.*<cardinal>` y no sólo sobre `^#`.**

**¿REINCIDENCIA?** Clase `Y-07` ≡ `V-09`…`V-13` — la regla de §0 sin guardián, deuda que `AA`
declaró **nunca barrida**.

---

### `BB-12` · **MEDIO** · origen `BB1-06` · §5.6 atribuye DOS VECES a `X52` una validación que `X52` no contiene — reincidencia literal de `J-03`

**Fichero y líneas.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L5403** y **L5563**.

**MI COMANDO Y MI SALIDA:**

```bash
$ grep -n 'X52' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
1627: | `X52` | comparar el censo de pruebas de §9.1, §9.5 y `nivel-certificacion` para cada
       nivel | los tres conjuntos son **idénticos**. Una diferencia de censo es un fallo |
5403: > … Con el esquema tal como §3.5 lo define, **`X52` tendría que RECHAZAR las tres**
5563: > … y **`X52`** la comprueba validando las tres celdas contra el esquema sin campos libres
7257: > … diferencia de censo es un fallo, no una simplificación editorial. Es `X52`.
```

**La única definición de `X52` (L1627) es un contraste de CENSOS de pruebas. L7257 la usa con su
sentido real; L5403 y L5563 le atribuyen una validación de celdas de cobertura contra esquema,
que `X52` no hace. SOSTENIDO.**

**Consecuencia material que sostengo:** `F6` construye `X52` desde §2.6.7. La tesis central de
§5.6 —*«los tres caben en el mismo contrato»*— **queda sin ningún contrato de prueba que la
respalde**, mientras el texto afirma dos veces que lo tiene.

**¿REINCIDENCIA DE QUÉ? De `J-03`**, literalmente: *«la comprobación propia de §6.7, que estaba
reasignada a `X51` —**una fila existente pero ajena**»*. Se añadió `X62` para el caso de §6.7 y
**no se barrió el resto de referencias `X<nn>`**. Es, otra vez, la corrección con la forma exacta
del contraejemplo.

**Traslado la recomendación de `BB1` porque es la de mayor rendimiento del dictamen:** para cada
cita `X<nn>` fuera de §2.6.7, comprobar que lo que la sede citante le atribuye es lo que su fila
dice. `BB1` sólo pudo hacerlo dentro de L1-5800; **nadie lo ha hecho sobre L5801-11504.**

---

### `BB-13` · **MEDIO** · origen `BB1-07` · la excepción de §0 que ampara «Son SEIS» invoca un guardián que NO deriva

**Fichero y línea.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L5216-5222**; el guardián,
`docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` **L586-597**.

**Cita literal de §5.2:**

> `**Son SEIS**, no cuatro … Este cardinal SÍ se escribe, por la única razón que la regla de
> titulares de §0 admite: \`G-10\` de la batería lo CONTRASTA contra las tres sedes … **Un
> cardinal con comprobación que lo DERIVE no caduca en silencio**`

**MI COMANDO Y MI SALIDA — `G-10` completo, leído del árbol:**

```python
seis = {
  "§5.2": "**Son\n                          SEIS**" in t11 or "**Son SEIS**" in t11 or …,
  "§16":  "las **SEIS**\n> extensiones de ficha" in t11 or …,
  "§17":  "**`+6` extensiones de ficha**" in t11,
}
caps = ["ENT", "ARQ", "PLT", "SEG", "DSP", "ENC"]      # ← SEIS NOMBRES HARDCODEADOS
falta = [k for k, v in seis.items() if not v] + [c for c in caps if f"`{c}`" not in fila17]
```

**No deriva nada.** Comprueba la presencia de tres *substrings literales* y de seis nombres
escritos a mano en el propio script. **SOSTENIDO.**

**Consecuencia exacta, que es el hallazgo:** una **SÉPTIMA** extensión de ficha dejaría «Son
SEIS» caducado **con `G-10` en VERDE**, porque nada de lo que comprueba cambiaría. `G-10`
detecta **regresión** (que desaparezca una), **no crecimiento**. La frase «lo CONTRASTA contra
los seis nombres» es literalmente cierta; **«un cardinal con comprobación que lo DERIVE» no lo
es, y es la que autoriza la excepción.** Es el único cardinal que el documento se permite
escribir, y se lo permite con un aval que no cubre el modo de fallo real.

---

### `BB-14` · **MEDIO** · origen `BB2-04` · el rótulo «literal de `O18`» que `O19` ordena reatribuir se corrigió en §11.8 y NO en §11.7

**Fichero y líneas.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L8532** (sin corregir) y
**L8674** (corregido).

**MI COMANDO Y MI SALIDA:**

```bash
$ sed -n '8532p;8674p' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
8532: **LO QUE (b) NO PROTEGE, ENUMERADO — literal de `O18`, y no se recorta.**
8674: --- EL REPARTO, LITERAL DE LA SEDE CANÓNICA DEL OWNER, RATIFICADO MEDIANTE `O19` ---
```

**La misma corrección de procedencia, aplicada a un lado y no al otro, en el mismo documento y a
142 líneas de distancia. SOSTENIDO.**

**El CONTENIDO es correcto y lo hago constar**: `BB2` cotejó los seis ítems contra la sede L242-245
—seis y seis, mismo orden, sin recorte ni añadido— y no lo desmiento. **Lo defectuoso es la
ATRIBUCIÓN**, que es exactamente lo que `O19` trasladó a la sede canónica.

**¿REINCIDENCIA?** De `V-03` (doc 24) → `Y-08` (doc 25), la clase «asimetría de procedencia»:
*«la corrección de procedencia de `O19` se aplicó al lado `O18` de §11.6-§11.9 y no al lado
`O17` ni a §15.8»*. **Aquí es al revés dentro de §11: §11.8 sí, §11.7 no.** Misma clase, sede
nueva.

---

### `BB-15` · **MEDIO** · origen `BB2-03` · §11.9 afirma sobre §15.4 un cumplimiento que §15.4 no tiene

**Fichero y línea.** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L8787-8788**.

**Cita literal:** `**Y §15.4 sigue llevando una fila por resolución**, las conservadas incluidas.`

**MI COMANDO Y MI SALIDA:**

```bash
$ awk 'NR>=9058 && NR<=9086 && /^\| `O/{print NR": "substr($0,1,40)}' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
9065: | `O7` …   9066: | `O8` …   9067: | `O9` …   9068: | `O10` …  9069: | `O11` …
9070: | `O12` …  9071: | `O13` …  9072: | `O14` …  9073: | `O15` …  9074: | `O16` …
9075: | `O17` …  9076: | `O18` …  9077: | `O19` …
```

**Trece filas, de `O7` a `O19`. NO hay fila para `O1`–`O6`.** Y el contexto inmediato de L8782-8785
define «las conservadas» como `O1`–`O16`. **SOSTENIDO: la afirmación es falsa por conteo.**

Es una **afirmación de cumplimiento hecha por quien se juzga**, falsable con `awk`. La tensión de
fondo la señaló bien `BB2` y la confirmo: §15.4 dice *«una fila por resolución»* y *«una
resolución sin fila aquí es el defecto»*, y a la vez **deriva de una cabecera `### \`O` que
excluye seis por construcción**, porque `O1`–`O6` viven en la tabla de §2 del registro sin
cabecera propia.

---

### `BB-16` · **MEDIO** · origen `BB3-02` · la proyección de `O17` no enlaza a la sede que la designa como su proyección

**Fichero y líneas.** `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` **L741-844**.

**Citas literales de la sede canónica:** L70 `PROYECCIÓN   \`O17\` y \`D107\` en \`DECISIONES-Y-CONTRADICCIONES.md\`` · L40 `la proyección debe ENLAZAR a la resolución canónica`.

**MI COMANDO:**

```bash
$ sed -n '741,845p' docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md | grep -c owner
0
```

**Cero menciones de `docs/owner` en las 104 líneas de la entrada. SOSTENIDO.** La de `O19` sí
enlaza (L1075-1079); la de `O17`, no. **La disciplina se aplicó a la resolución que la creó y no
hacia atrás** — misma clase `Y-08`, misma forma que `BB-14`.

---

### `BB-17` · **MENOR** · origen `BB1-08` · escribe «DIECIOCHO» en la frase que declara no escribirlo

`11-ARQUITECTURA-INTEGRADA.md` **L1260**: `Se enumeran las **DIECIOCHO**, y el recuento **se
deriva de las filas de la tabla, no se escribe**`. Conté las filas: **18** — cierto hoy. La
frase es autocontradictoria y **no cumple la excepción de §0**, que exige publicar *«el comando
que lo deriva»*: no publica ninguno. **Reincidencia de `V-13` (doc 24) → `Y-07` (doc 25),
citada literalmente por ambos como «L1213 escribe DIECIOCHO en la frase que jura no
escribirlo».** La línea se movió de 1213 a 1260; el defecto no.

---

### `BB-18` · **MENOR** · origen `BB2-05` + `BB2-06` · cuatro cardinales copiados en la frase que declara remitir, y dos sin comando derivador

`11-ARQUITECTURA-INTEGRADA.md` **L10726-10736** (§19 copia cuatro cardinales — cuarenta y seis,
once, ocho, doce— en la misma frase en que escribe *«Cada familia lleva su cifra en SU sede y
aquí se remite»*), **L6732-6733** y **L6788** («las CATORCE preguntas»), **L6939/L6944** («las
CINCO salidas»). **Las cifras son CORRECTAS HOY** —`BB2` las derivó y no las desmiento—; el
hallazgo es la **forma**. Reincidencia directa de `V-19` (doc 24) → `Y-07` (doc 25), que cita
`L10612-10624` con el mismo texto.

**Y lo que `BB2` hizo bien y traslado:** comprobó que los «CATORCE campos» de §8.0 L6148 **SÍ**
están amparados por la excepción (los contrasta `G-25`), y que las catorce preguntas de `A3` y
las cinco salidas de `M7` **no**. La distinción es correcta y evita inflar el hallazgo.

---

### `BB-19` · **MENOR** · origen `BB3-06` · el índice dice que la siguiente acción está «al final» del checkpoint, y está la primera de siete

`docs/evolucion/00-INDICE.md` **L93-95**: `**Basta decir «Continúa»**: la siguiente acción exacta está al final de ese fichero.`

```bash
$ grep -n '^## Siguiente acci[óo]n exacta' docs/evolucion/CHECKPOINT-ADS-NEXT.md
3321 (VIGENTE) · 3416 · 3484 · 3545 · 3702 · 3849 · 3989  ← seis HISTÓRICAS después
```

**La vigente es la PRIMERA de siete, en L3321 de 4085.** Quien lea «al final» llega a L3989, la
**anterior al documento 22**. **SOSTENIDO.** El checkpoint ya corrigió su propia cabecera
(L6-8) por esta razón; **el índice no heredó la corrección.** Reincidencia de la clase
`S-17`≡`S3-05` (doc 23) → `P-05`≡`Q-08`/`R-02` (doc 21).

---

### `BB-20` · **MENOR** · origen `BB1-09` a `BB1-12` y `BB3-07` · residuos editoriales y de propagación

Los agrupo porque ninguno mueve un veredicto y contarlos por separado infla el censo — que es
lo que los cinco gates anteriores prohíben:

| origen | sede | qué es |
|---|---|---|
| `BB1-09` | doc 11 **L4691** | la regla 4 se dice demostrada por `X55`, que prueba otro orden; la que lo ejerce es `X01`. Misma clase que `BB-12`, menor consecuencia |
| `BB1-10` | doc 11 **L2057** / **L2140** | «Los ocho puntos» con un noveno rótulo normativo sin numerar. Clase `Y-07` |
| `BB1-11` | doc 11 **L5804** | frase sin verbo en norma vigente sobre retirada de proyecciones |
| `BB1-12` | doc 11 **L872**, **L1791**, **L2287** | tres analogías pre-`D105`, no falsas por sí solas, que reconstruyen la intuición que `D105` desmonta |
| `BB3-07` | `DECISIONES` §2 | el orden de entradas es `O1`–`O14`, `O16`, `O15`, `O17`–`O19`. Explicado por `m-2`, no declarado como excepción de orden |

---

### `BB-21` · **MEDIO** · **HALLAZGO MÍO** · el sobre no se transcribió, pero el protocolo del gate SIGUE ORDENANDO transcribirlo

Ver §0.3. El remedio del gate 5 es **no transcribir**, y funciona. Pero **dos de los tres
relevos embebieron el sobre íntegro en su informe** porque su encargo se lo pidió, y `BB3` no lo
hizo. **Que los dos bloques salgan byte a byte idénticos es un resultado, no una garantía:**
depende de que alguien —yo— corra el `diff`. **Embeber el sobre reintroduce exactamente el
vector que invalidó el gate 4**, y sólo es inocuo mientras se compruebe. `BB3` adoptó la
conducta robusta —citar el SHA-256 y remitir al fichero— y el encargo la trata como una omisión.
**El defecto está en el protocolo, no en `BB3`.** Reincidencia de la causa de invalidez del doc
25 §1, en forma atenuada.

---

### `BB-22` · **MENOR** · **HALLAZGO MÍO** · el encargo de este gate contiene tres rutas escritas a mano y equivocadas

Ver §1.2. Tres de las siete rutas de mi lote no existen; los números son correctos y los títulos
inventados. **Misma clase que el `c3d6465a` que el adjudicador `O` reprochó al coordinador en el
documento 20** —*«la clase de identificador derivado y escrito a mano que este expediente lleva
doce tandas persiguiendo, y aparece en el encargo del gate que viene a cerrarlo»*— y misma clase
que `C-2` → `T-11` → `W-17` → `Z-10`, la serie de **defectos del reparto**, que va por su cuarta
repetición. **No impide nada: los localicé en un comando.** Lo registro porque la serie existe y
porque el coordinador es el actor que el gate 4 identificó como causa de invalidez.

---

## 3 · HALLAZGOS DE MIS RELEVOS QUE NO SOSTENGO, Y POR QUÉ

Mis tres relevos trajeron **25 hallazgos** (`BB1` doce, `BB2` seis, `BB3` siete), no 24. Sostengo
**22 en 20 identificadores propios** —agrupando cinco menores en `BB-20` y fundiendo `BB1-03`
con `BB1-05`—, y añado **tres míos** (`BB-03`, `BB-21`, `BB-22`). Lo que no sostengo va aquí,
sin suavizar.

### 3.1 · **NO SOSTENIDO · la segunda mitad de `BB3-03`**

`BB3` afirma: *«su `OBLIGATORIO − ASIGNADO = 0` es en realidad 1»*. **NO LO SOSTENGO.**
La resta cierra a **0** contra el árbol que el manifiesto declara repartir (§1 del manifiesto:
commit candidato `8c9ca9c3`), y lo medí en las dos direcciones: 74 filas, 74 rutas, cero
sobrantes, cero faltantes. `BB3` la midió contra el árbol del gate, que no es el objeto del
reparto. **La primera mitad de `BB3-03` —el rótulo del árbol equivocado— la sostengo entera
como `BB-02`; la segunda es un error de medición, y la corrijo.** El hecho que `BB3` observó es
real y lo elevo yo a `BB-03`, pero **su causa es estructural y ajena al coordinador de este
gate**, no una resta falseada.

### 3.2 · **NO SOSTENIDO · la declaración de `BB3` de haber verificado «las dos refs remotas»**

`notas/BB3.md` L106 lista entre lo verificado «*las dos refs remotas*». Lo que `BB3` contrastó
—como `BB2` declara expresamente para sí mismo— son las copias locales `refs/remotes/origin/…`.
**Contrastar una copia local y llamarla «ref remota» es exactamente el tipo de precisión que
este expediente castiga.** No es un error de hecho —las copias locales coinciden con el
remoto, y lo comprobé—, es un error de **procedencia**. Lo cierro yo con `git ls-remote` en
§0.2, contra el remoto de verdad. **El campo queda verificado; la declaración de `BB3` no era la
que él decía.**

### 3.3 · **NO SOSTENIDO · la afirmación de `BB2` de que no había red**

`INFORME-BB2.md` §0.3(a): *«**No ejecuté `git ls-remote`**: el entorno de este relevo no tiene
red»*. **Hay red**, y la usé (§0.2). No cuento esto como hallazgo contra `BB2` —declaró su
limitación contra su propio interés, que es la conducta correcta— pero **la limitación que
declaró no existía**, y su reserva sobre el sobre queda **retirada por mí**, no confirmada.

### 3.4 · **REBAJADO, NO RECHAZADO · `BB1-01`**

`BB1` lo gradúa **GRAVE**. Yo lo bajo a **MEDIO** (`BB-10`), y digo por qué en su ficha: el
censo omite una población nacida después, no afirma una cifra falsa sobre una tabla existente.
No es benevolencia: `BB-09`, que sí afirma una cifra falsa sobre una tabla existente, lo
mantengo en GRAVE.

### 3.5 · **NO CONTADO APARTE · `BB1-08`, `BB2-05`, `BB2-06`, `BB1-10`**

Los cuatro son **la misma clase `Y-07`** —la regla de titulares de §0 sin guardián—. Los
registro (`BB-17`, `BB-18`, `BB-20`) pero **no los cuento como defectos independientes en mi
recuento de clase**. Inflar el censo con el mismo defecto contado cuatro veces es lo que `Y4`
rechazó expresamente para `Y2-04`, y tiene razón.

### 3.6 · **NO REPRODUCIDO POR MÍ, y lo declaro · las afirmaciones de cobertura de `BB1` y `BB2`**

`BB1` declara haber leído íntegro L1-L5805 del documento 11 en 29 tramos; `BB2`, L5801-L11504 en
14 tramos. **No puedo verificar que leyeran.** Puedo verificar —y verifiqué— que **el SHA-256
del fichero es el que los dos declaran** (`3b7c3dd5…d64d7`) y que **las sedes concretas que
citan dicen lo que dicen**. Comprobé ~25 de ellas y **acertaron en todas menos en el punto de
§3.1**. Eso es evidencia de fiabilidad, no prueba de lectura. `DD` debe pesarlo como tal.

### 3.7 · **LO QUE MIS RELEVOS VERIFICARON Y NO CAYÓ, y pesa tanto como lo que cayó**

No lo reproduje entero —lo digo— pero lo traslado porque un dictamen que sólo lista defectos
miente por omisión:

```text
`BB1`  el reparto W11/W17/W8 es exacto, sin huecos ni solapes, y las tres sedes coinciden
       `X55` y `X58` están BIEN corregidas: una implementación con `M-03` hoy las falla
       las nueve sedes de `abierta(tx)` son exactamente las nueve nombradas
       los NUEVE barridos que el documento publica de sí mismo son TODOS ciertos hoy
       toda la aritmética del tramo cierra (54 = 34+20, 29+17 = 46, etc.)
       las 23 cabeceras con cardinal de L1-5800 son las 23 ciertas
`BB2`  el DISEÑO no ha cambiado: siete cotejos cláusula a cláusula contra la sede canónica
       `D108` aparece como PROYECCIÓN en las siete sedes que lo nombran, nunca como autoridad
       las TRES citas que el cuarto gate encontró dando cero están REATRIBUIDAS de verdad
       ninguna sede presenta `(b)` como `(c)`; `C` sigue declarada NO IMPLEMENTADA
       todas las derivaciones publicadas de su tramo reproducen, incluidas las nueve de `D104`
`BB3`  `AA-02` está GENUINAMENTE corregido: el renglón publica los dos comandos en vez del
       resultado, y ejecutados dan lo que el condicional predice
       la serie `D1`–`D108` y `O1`–`O19` están completas, sin huecos ni duplicados
       la proyección de `O19` es FIEL: los tres bloques salen idénticos al `diff`
       `C-L.5` ABIERTA y `C-L.7` NO CERRADA en la clasificación vigente, cada id una vez
```

**Y una comprobación mía sobre el sobre, que cierra `AA-05` del doc 25.** `AA` halló que el
campo 14 —IDENTIDAD DEL COORDINADOR, *«el ancla de (b)»*— publicaba un **ROL** y no un nombre.
El sobre de este gate publica:

```text
EMISOR   Jose Lopez Gonzalez (jose@congeladosbrisamar.es), coordinador del gate 5 de F4c
```

**Es un NOMBRE. `AA-05` está CERRADO**, y nadie de mi cadena lo dijo porque nadie podía leer el
documento 25. **Lo hago constar a favor de la tanda.**

---

## 4 · ¿SE AUDITA LA CANDIDATA O EL COMMIT DEL GATE?

Ésta es la pregunta que el encargo dice que ninguno de mis relevos podía decidir. **La decido.**

### 4.1 · La batería, ejecutada por mí en los dos árboles

Ya publicada en `BB-01`. La resumo aquí porque es la base de la decisión:

```text
                                    CANDIDATA 8c9ca9c3…      GATE 5ed7a3b8…
registrar_evidencia.py              13/13 · RC=0             **12/13 · RC=1**
comprobar_referencias.py            T147 SUPERADA            **T147 FALLIDA**
documentos analizados               263                      264
ficheros de evidencia reescritos    0                        **2**
causa                               —                        el manifiesto de este gate,
                                                             «Existe para nadie»
```

### 4.2 · MI DECISIÓN, Y SUS TRES RAZONES

> **SE AUDITA LA CANDIDATA. El commit del gate NO es el objeto auditado: es el APARATO del
> gate, y responde como aparato, no como objeto.**

**Razón 1 · Lo dice el manifiesto, que es anterior a todo revisor y no se modifica.** Su §1 se
titula «**Objeto del reparto**» y fija `COMMIT CANDIDATO 8c9ca9c3…` y su `TREE SHA`. No hay
ambigüedad sobre qué se reparte.

**Razón 2 · Lo dice el sobre, y con el dedo.** Publica los dos árboles precisamente para que no
se mezclen —*«no mezcla ni un campo»*— y su obligación 4 dice: *«LAS RUTAS EN QUE LOS DOS
UNIVERSOS DIFIEREN […] son la superficie exacta en que la candidata y el gate no son el mismo
objeto. Todo lo que el manifiesto afirme sobre ellas tiene que decir DE QUE ARBOL habla»*. Un
sobre que ordena distinguir los árboles no puede leerse como si los fundiera.

**Razón 3 · Es la doctrina ya establecida por dos adjudicadores, y no la invento.** El
adjudicador `U` (doc 23) resolvió la primera instancia; el doc 24 la aplicó dos veces (`V-06`,
`W-16`) y `AA` la aplicó en el doc 25 con estas palabras: *«**La evidencia es VERDADERA de la
candidata y FALSA del árbol del gate**»*, y contó `Y-03`/`Y-04` como defecto **del aparato**.
**Cambiar de criterio en el quinto gate sería precisamente lo que este expediente castiga.**

### 4.3 · Y LO QUE ESA DECISIÓN **NO** AUTORIZA — que es la mitad que importa

`BB3` lo formuló mejor que nadie y lo hago mío: *«no castigues a la candidata por lo que rompió
el aparato del gate, **y no absuelvas al aparato por eso**»*.

1. **La candidata pasa 13/13 y `T147`, y no ensucia un byte.** `BB-01` **no cuenta contra el
   objeto auditado.** Quien quiera fundar insuficiencia en un validador en rojo **no puede
   hacerlo con éste**.
2. **Pero `BB-01` sigue siendo GRAVE**, porque mide **la disciplina del aparato que viene a
   certificar** — y la disciplina es, según el propio doc 25, **lo único que falta**. Un gate
   cuyo commit incumple, por quinta vez, una regla que el corpus escribió, publicó con su
   comando y cuyo remedio de una línea le dejó escrito el gate anterior, **está midiendo mal
   por la vía por la que dice medir bien**.
3. **Reparto explícito de mis hallazgos por árbol**, porque el sobre lo exige:

```text
DEL ÁRBOL DEL GATE (5ed7a3b8) — defectos del APARATO, no del objeto
  BB-01   T147 en rojo · 12/13 · dos ficheros de evidencia sucios
  BB-02   el rótulo del árbol equivocado en el manifiesto
  BB-03   la resta insatisfacible por diseño heredado
  BB-21   el protocolo que ordena transcribir el sobre
  BB-22   las tres rutas equivocadas del encargo

DE LA CANDIDATA (8c9ca9c3) — defectos del OBJETO AUDITADO
  BB-04 · BB-05 · BB-06 · BB-07 · BB-08 · BB-09 · BB-10 · BB-11 · BB-12
  BB-13 · BB-14 · BB-15 · BB-16 · BB-17 · BB-18 · BB-19 · BB-20
```

**Diecisiete de mis veintidós hallazgos son de la candidata.** El gate no se sostiene o se cae
por el aparato: se sostiene o se cae por esos diecisiete. **Que `DD` no use `BB-01` para juzgar
el objeto, ni lo descuente para juzgar el método.**

---

## 5 · REINCIDENCIAS, CON SU IDENTIFICADOR DE ORIGEN EN 19–25

**La reincidencia pesa más que el defecto.** Ordenadas por gravedad de la reincidencia, no del
hallazgo.

| mío | clase | identificador de ORIGEN, con su documento | instancia n.º | ¿el remedio estaba escrito? |
|---|---|---|---|---|
| **`BB-01`** | manifiesto sin enlazar · `T147` en rojo sobre el árbol del gate | **`S-18`≡`T-14`** (doc 23) → **`V-06`≡`X-07`** y **`W-16`** (doc 24) → **`Y-03`+`Y-04`≡`Z-09`** (doc 25) | **5.ª** | **SÍ**, doc 25 §8, literal y de una línea |
| **`BB-04`** | paráfrasis que AMPLÍA la sede canónica bajo rótulo LITERAL | **`Y-09`** (doc 25), **el hallazgo mismo, no su clase** · tipificado como `X-O13` | **2.ª** | **SÍ**, orden de cierre de `AA`: «que se retiren cuatro comillas» |
| **`BB-05`** | texto atribuido al Owner con CERO en la sede canónica | **`Y-05`** (doc 25) · `X-O13` · precedente `V-03` (doc 24) | **2.ª** | **SÍ**, misma orden de `AA` |
| **`BB-07`** | el checkpoint copia un estado caducado en el renglón que declara remitir | **`K-01`/`J-10`/`L-01`** → **`P-05`≡`Q-08`/`R-02`** (doc 21) → **`S-17`≡`S3-05`** (doc 23) → **`X-04`** (doc 24) → **`AA-02`** (doc 25) | **6.ª** | **SÍ**, la clase que `C-L.7` existe para cerrar |
| **`BB-02`** | el manifiesto declara cifras de un árbol distinto del que nombra | **`U-02`** (doc 23) → **`X-06`≡`V-23`** (doc 24) | **3.ª**, tras ser **declarada ROTA** por `AA` | **SÍ**, y el sobre manda mirarla PRIMERO |
| **`BB-08`** | `D105` sin propagar a sedes normativas vivas | **`Y-02`** (doc 25), residuo | **2.ª** | **SÍ**, ocho sedes nombradas una a una |
| **`BB-09`** `BB-10` `BB-11` `BB-17` `BB-18` `BB-20` | la regla de titulares de §0, sin guardián | **`V-09`…`V-13`, `V-19`** (doc 24) → **`Y-07`** (doc 25) | **3.ª**, y `AA` la declaró **deuda nunca barrida** | **NO** — y es la única de la lista sin remedio escrito |
| **`BB-12`** | una sede atribuye a una fila `X<nn>` lo que esa fila no comprueba | **`J-03`** | **2.ª** | parcial: se añadió `X62` y no se barrió el resto |
| **`BB-14`** `BB-16` | asimetría de procedencia: la corrección se aplica a un lado del par | **`V-03`** (doc 24) → **`Y-08`** (doc 25) | **3.ª** | **SÍ** |
| **`BB-19`** | el punto de entrada apunta a una sede caducada | **`S-17`≡`S3-05`** (doc 23) | **2.ª** | **SÍ** |
| **`BB-22`** | el reparto entrega identificadores derivados a mano y falsos | **`C-2`** (doc 22) → **`T-11`** (doc 23) → **`W-17`** (doc 24) → **`Z-10`** (doc 25) | **5.ª** | **SÍ** |
| **`BB-06`** | `C-L.5` con dos estados, uno caducado, en su propia sede | **`P-22`≡`Q-37`** (doc 22) | **2.ª**, y el que sobrevivió es el caducado | **SÍ** |

**El recuento que importa: de mis 22 hallazgos, 19 son reincidencias de clases ya dictaminadas
en 19–25. Sólo `BB-13`, `BB-15` y `BB-21` son clases nuevas.**

**Y el dato que traslado a `DD` por encima de todos:** **once de las doce clases reincidentes
tenían el remedio ESCRITO por el gate anterior.** La única que no —la regla de §0— es la única
que `AA` declaró expresamente sin guardián y por tanto sin mecanismo de cierre. **Todas las
demás son incumplimiento, no dificultad.**

---

## 6 · QUÉ FALLA HOY, SI FALLA — en mis palabras

El cuarto gate determinó que la causa esencial de cuatro fracasos —**verificación anclada dentro
del objeto verificado**— ya no es la causa, porque los tres remedios funcionan. **Mi cadena
aporta la evidencia que confirma esa determinación, y la aporta de la forma más fuerte
disponible: por replicación.**

### 6.1 · Lo que ya no falla, y hay que decirlo primero porque es verdad

**Cinco lectores independientes leyeron el mismo sobre y todas sus derivaciones reprodujeron.**
No «coincidieron»: **reprodujeron byte a byte, cada uno con su propio comando, sobre commits
inmutables.** `BB1`, `BB2` y `BB3` verificaron los 21 campos por separado y sin verse; yo los
verifiqué de nuevo sin fiarme de ninguno de los tres. **Cero discrepancias en 17 campos
comprobados por mí, incluidos los dos digest de universo derivados con la receta publicada y sin
ejecutar el emisor.** Y la vía por la que murió el gate 4 —la transcripción a mano— **está
cerrada y lo medí**: los dos bloques embebidos son el fichero, byte a byte, y el tercer relevo
no transcribió nada.

**Eso es un hecho positivo y no lo voy a enterrar bajo veintidós hallazgos.** El ancla externa
existe, se entrega íntegra, se verifica sin ejecutar el instrumento que la produce, y **cinco
lectores obtuvieron el mismo objeto**. La respuesta del cuarto gate se sostiene: **la
circularidad ya no es la causa.** Añado que `AA-05` está cerrado y que el remedio de `AA-01` está
aplicado y funciona en lo que fue diseñado para hacer.

### 6.2 · Entonces, ¿qué falla?

**Falla que el sistema corrige INSTANCIAS y no CLASES, y que quien corrige es la misma mano que
después se somete a juicio.**

Lo digo con la medida delante, porque no es una impresión:

```text
de mis 22 hallazgos          19 son reincidencias de clases ya dictaminadas en 19-25
de esas 19                   11 clases tenían el REMEDIO ESCRITO por el gate anterior
la única sin remedio escrito la regla de titulares de §0, que AA declaró sin guardián
```

Cuatro gates han dicho variantes de esto. **Yo puedo decirlo con más precisión porque tengo el
documento 25 y mis relevos no lo tenían**, y la precisión es ésta: **la corrección se aplica con
la forma sintáctica exacta del contraejemplo que se le enseñó, y no con su extensión
semántica.**

Los cuatro casos que lo demuestran, todos verificados por mí en este árbol:

```text
`Y-05` dijo: hay TRES CITAS ENTRECOMILLADAS atribuidas al Owner con cero en la sede
  → se barrieron las comillas. `BB-05` sobrevive porque va en CURSIVA
`Y-09` dijo: §11.8 L8590 escribe «CI o» bajo rótulo literal
  → `BB-04` sigue ahí, en L8687. Ni siquiera se movió: sólo cambió de número de línea
`Y-02` dijo: `D105` sin propagar a OCHO sedes, y las nombró
  → se corrigieron las ocho, `X55` y `X58` incluidas, y `BB-08` sobrevive en TRES sedes
    que no estaban en la lista, una de ellas quince líneas por encima de la nota
`V-03` dijo: el rótulo «literal de `O18`» de §11.8
  → se corrigió §11.8 L8674. `BB-14` sobrevive en §11.7 L8532, 142 líneas antes
```

**Esto no es negligencia: es una propiedad del bucle.** Quien corrige recibe una lista de
sedes con su línea, y la lista es *exhaustiva del hallazgo* y *no exhaustiva de la clase*.
Corregir la lista es verificable y barato; derivar la clase es caro y nadie lo comprueba. **El
incentivo del corrector está alineado con cerrar el hallazgo, no con cerrar la clase — y el gate
siguiente mide la clase.** Por eso el coste marginal de encontrar la puerta siguiente no sube,
que es la medida que `AA` publicó y que sigue plana.

### 6.3 · Y hay una segunda cosa que falla, y es más incómoda

**El aparato del gate ha dejado de ser fiable a la misma velocidad a la que el objeto ha
mejorado.** Los datos son míos:

```text
LA CANDIDATA          13/13 · T147 SUPERADA · no ensucia un byte · 74 filas cuadran al dígito
                      · las derivaciones reproducen · el DISEÑO no ha cambiado
EL APARATO DEL GATE   el commit deja `T147` en rojo (5.ª vez, con el remedio escrito)
                      el manifiesto nombra el árbol equivocado (3.ª vez, tras declararse rota)
                      el encargo trae tres rutas falsas (5.ª de la serie del reparto)
                      el protocolo ordena transcribir el sobre que el gate existe para no
                        transcribir
```

**Cinco de mis veintidós hallazgos son del aparato, y los cinco son de la clase que ya invalidó
un gate o lo hizo fallar.** El gate 4 no murió por el corpus: murió por la mano del coordinador.
**El gate 5 arregló la vía exacta por la que murió el 4 —la transcripción— y volvió a fallar por
las otras cuatro vías de la misma mano.** Otra vez: la instancia, no la clase.

### 6.4 · Mi respuesta, en una frase

> **Ya no falla el ancla: falla el aprendizaje.** El sistema ha demostrado que puede construir
> una raíz de confianza externa y que puede replicarla en cinco lectores sin una sola
> divergencia — y eso es real y es nuevo. **Lo que no ha demostrado es que pueda cerrar una
> clase de defecto en vez de una lista de líneas.** Mientras la corrección se mida por la lista
> que se le entregó y no por la clase que la lista ejemplifica, cada gate encontrará el mismo
> defecto una sede más allá, y cada gate tendrá razón al llamarlo reincidencia.
>
> Y añado lo que el cuarto gate no podía saber y yo sí, porque `BB-03` lo mide: **el remedio de
> `AA-01` creó una condición estructuralmente insatisfacible** —el manifiesto es fila de su
> propio universo y no puede contener su propio SHA-256—. **La sexta reincidencia de esa resta
> ya está garantizada si nadie toca el enunciado.** Es la prueba más limpia que puedo ofrecer
> de la tesis de §6.2: el remedio correcto, aplicado con la forma exacta del contraejemplo,
> abre una puerta que nadie miró porque nadie derivó la clase.

**Y con esto NO estoy diciendo que el trabajo deba detenerse. No es mi decisión y no la insinúo:
es de `DD`.** Digo lo que mido: ninguno de mis veintidós es BLOQUEANTE, ninguno exige arquitectura
nueva, ninguno vuelve al Owner, y **once de las doce clases reincidentes tienen el remedio
escrito y sin aplicar.** Es lo que `AA` llamó «de resta y de disciplina», y sigue siéndolo.

---

## 7 · REFUTACIONES CONTRA MIS PROPIAS CONCLUSIONES

El encargo pide al menos tres. Intenté **seis**, y publico las cinco que no cayeron **y la que
sí cayó**, que es la que más vale.

### 7.1 · **CAYÓ · «`BB1-02` es FALSO: `X-S` sólo llega a `X-S9`»**

**La intenté y me la creí durante un minuto.** Mi comando:

```bash
$ grep -oE 'X-S[0-9]+' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | sort -u | tail -3
X-S7 X-S8 X-S9
```

Estuve a punto de escribir que mi relevo se había equivocado. **Me salvó volver a mirar el
comando, no el resultado:** `sort -u` sin `-V` ordena lexicográficamente y coloca `X-S10` y
`X-S11` **entre `X-S1` y `X-S2`**, donde `tail -3` no los ve.

```bash
$ grep -oE 'X-S[0-9]+' … | sort -u -V | tr '\n' ' '
X-S1 X-S2 X-S3 X-S4 X-S5 X-S6 X-S7 X-S8 X-S9 X-S10 X-S11
$ grep -cE '^\| `X-S[0-9]+`' …
11
```

**MI REFUTACIÓN CAYÓ. `BB1-02` es correcto y lo sostengo como `BB-09`.**

**Lo publico porque es el hallazgo de método más útil de mi dictamen:** un dictaminador
adversarial que sólo mira la salida de su comando produce falsos negativos con la misma
facilidad con que un revisor complaciente produce falsos positivos. **Y el error fue un
ordenador lexicográfico** — exactamente la clase de detalle mecánico invisible que este
expediente lleva cinco gates persiguiendo. Si yo hubiera cerrado ahí, habría retirado un GRAVE
verdadero con una demostración que parecía impecable.

### 7.2 · **NO CAYÓ · «El gate 5 es INVÁLIDO, como el 4»**

La construí en serio, porque es la conclusión más consecuente que podría alcanzar. El disparador
de invalidez que §11.6 y el sobre definen es **(a)** una diferencia entre el sobre recibido y lo
que el árbol muestra, o **(b)** una diferencia entre los sobres entregados a distintos revisores.

```text
(a)  17 campos recalculados por mí de los dos commits.  CERO diferencias.  §0.2
(b)  el sobre NO se transcribió: vive en un fichero. Los dos bloques embebidos son
     byte a byte el fichero (`diff` vacío, mismo SHA-256). El tercero no embebió nada.
     CERO diferencias entre lo que los tres relevos leyeron.  §0.3
```

**NO CAE, y cae del lado contrario: el remedio del gate 5 funciona exactamente donde el gate 4
murió.** El defecto de `BB-02` es un rótulo **dentro del manifiesto**, no una discrepancia del
ancla. Declarar inválido por eso sería confundir el objeto con su etiqueta — y es lo que `AA`
prohibió al rechazar el argumento Merkle de `Y4` por la razón simétrica.

### 7.3 · **NO CAYÓ · «`BB-01` no es reincidencia: es un dilema estructural sin salida»**

Es la defensa natural del coordinador y me la tomé en serio: si el instrumental cierra antes que
el manifiesto, y el manifiesto se commitea **solo y último**, no queda commit donde enlazarlo.
Tres reglas verdaderas y aparentemente incompatibles.

**NO CAE, y no cae porque ya la juzgó `Y4` en el documento 25 §8**, que es el documento que sólo
yo he leído:

> **JUZGO: la tensión es REAL, y NO es insatisfacible.** […] Ni `00-INDICE.md` ni
> `kernel/operativo/pruebas/evidencia/` están dentro de `verificacion/`: **la regla nueva no
> prohíbe tocarlos.** Y «solo» en el campo 6 no está definido como «único fichero del commit».

**La salida está escrita, medida y publicada, y cuesta una línea.** `git show --stat 5ed7a3b8`
confirma que el commit toca un solo fichero. **La refutación no sólo no cayó: convirtió `BB-01`
de reincidencia en incumplimiento de una orden explícita.**

### 7.4 · **NO CAYÓ · «`BB-04` y `BB-05` amplían en dirección PROTECTORA, luego son inocuos»**

Es la mejor defensa material de los dos hallazgos de atribución. «CI o el ejecutor externo» es
**más** restrictivo que la sede; «robustez y revalidación permanente» es **coherente** con lo
que `O17` decidió. Ningún daño operativo.

**NO CAE, por dos vías independientes:**

1. **La cláusula del Owner no distingue dirección.** «*Una paráfrasis nunca puede ampliar la
   autoridad del texto canónico*». `Y4` ya lo dijo de `Y-09`: *«Amplía en dirección PROTECTORA, y
   `O19` no distingue dirección»*, y `AA` lo mantuvo como A+B.
2. **`O19` NACIÓ de una ampliación cómoda.** El expediente entero existe porque una paráfrasis
   del coordinador amplió una resolución del Owner en dirección que a nadie incomodaba.
   Aceptar la defensa aquí es reabrir la puerta por la que `O19` entró.

**Y una tercera, que es mía:** si la dirección importara, alguien tendría que juzgarla, y el
único que puede es el Owner. **Convertir un hallazgo de resta en una pregunta al Owner es
exactamente lo que `AA` demostró que no hace falta.**

### 7.5 · **NO CAYÓ · «`BB-06` cae porque el gate 4 fue INVÁLIDO y un gate inválido no produce veredicto»**

Es la refutación que `BB2` construyó contra su propio hallazgo y dejó abierta a propósito.
**La cerré con el documento 25 delante y NO CAE**, por las dos vías de `BB-06`: `AA` reabrió
`C-L.5` como **adjudicación expresa de la condición** (doc 25 §11), no como consecuencia del
veredicto; y la reapertura se funda en una **resta aritmética** que la propia `C-L.5` declara
válida *«con independencia de los hallazgos»*.

**Y una comprobación adicional que hice para no fiarme de mi propia lectura:** si `CERTIFICADA`
fuese lo correcto, entonces el checkpoint, el índice **y el manifiesto de este gate** estarían
los tres equivocados. **El manifiesto es material que el coordinador emitió ANTES de repartir y
que no se modifica.** La hipótesis alternativa exige tres errores coordinados en sedes
independientes; la mía, uno. **No cae.**

### 7.6 · **NO CAYÓ · «`BB-03` es una excusa que blanquea al coordinador»**

Ésta me la hice a mí mismo, porque `BB-03` es lo más parecido a una absolución que hay en mi
dictamen y desconfío de mis propias absoluciones.

Intenté demostrar que el manifiesto **sí** podía haber cerrado a 0 sobre el árbol del gate:

```text
· ¿podría listarse a sí mismo?  NO: cada fila publica el SHA-256 del fichero, y un fichero no
  puede contener su propio SHA-256. Punto fijo.
· ¿lo hizo el gate 4?  NO: comprobé que el manifiesto 4B (70 filas) NO se lista a sí mismo,
  y aun así cerraba 70=70 — porque el manifiesto en curso NO estaba en su universo.
  `grep -c '4B-20260830' <universo del gate 4>` → **0**
  `grep -c 'CERTIFICACION-5-20260831' <universo del gate 5>` → **1**
· ¿qué cambió?  el derivador. `manifiestos/` pasó de RUTAS LITERALES a ZONA BARRIDA, por el
  remedio de `AA-01`≡`Z2-02`≡`Z-03`. Lo leí en el `diff` de los dos derivadores.
```

**NO CAE: la imposibilidad es real y su causa es datable.** Pero la refutación **sí me corrigió
en un punto y lo declaro**: mi primera redacción decía que la resta «da 1 y no hay nada que
hacer». **Sí hay:** el enunciado puede medirse contra el árbol candidato, que es donde el
manifiesto declara repartir y donde cierra a 0. **`BB-03` es un defecto de ENUNCIADO, no una
imposibilidad absoluta**, y lo reescribí en consecuencia. Que conste que la refutación mejoró el
hallazgo en vez de tumbarlo.

---

## 8 · LO QUE MI CADENA NO CUBRE, SIN ADORNO

1. **NO hemos ejecutado ni una sola de las pruebas que el corpus describe.** Las 46 filas `X`,
   las 18 ventanas `W`, las 11 `X-S`, las 13 `X-O`, las 8 `X-A`–`X-H`: **todo es contrato
   escrito, ninguno se ha ejecutado.** Lo dice el propio documento y lo repito porque es el
   hecho central que ninguna cantidad de hallazgos coherentes sustituye.
2. **`M-04` como proposición general: NO ATACADA por nadie de mi cadena.** No construimos un
   solo árbol defectuoso. `AA` reprodujo seis en 38/38 verde; **yo no reproduje ninguno.**
   `BB1`, `BB2` y `BB3` lo declaran los tres. **La cadena `BB` no aporta ni una medida sobre
   `M-04`, y `DD` no debe leer nuestro silencio como evidencia en ninguna dirección.**
3. **El instrumental NO está auditado por nosotros.** Leí `G-10` (12 líneas) y las zonas del
   derivador que `BB-03` exige. **No hemos auditado la batería, el emisor ni el derivador como
   código.** Es lote de `CC`. Ejecuté los validadores como instrumento, no como objeto.
4. **Los documentos 19–24 NO están leídos íntegros por nadie de mi cadena**, yo incluido (§1.2).
   De sus 13 538 líneas leí veredictos, hallazgos y reincidencias. **Un defecto fuera de esas
   regiones se nos escapa.** Y mis relevos no los abrieron en absoluto, por instrucción.
5. **Consecuencia directa de lo anterior, y es grande:** `BB1` y `BB2` verificaron las
   **CONSECUENCIAS** de las citas que el documento 11 hace de los dictámenes 19–25, **no las
   CITAS contra su fuente**. Yo cerré las que tocan mis hallazgos; **el resto sigue sin
   contrastar.**
6. **`C-L.3`, `C-L.7` y las otras once condiciones: sin juicio propio.** `BB3` verificó que la
   clasificación vigente las lista una vez cada una. **Ninguno de nosotros ha auditado si el
   estado que declara cada una es cierto**, salvo `C-L.5` (`BB-06`, `BB-07`).
7. **La sede canónica del Owner no es verificable contra nada externo, y lo declara ella misma.**
   Recalculé sus cuatro digest y son idénticos en los dos commits. **Eso prueba que el texto no
   cambió entre el commit auditado y lo que recibí fuera del árbol. NO prueba que sea el que el
   Owner emitió.** Es la limitación que `O18` declara de sí misma y sigue vigente hasta el
   verificador externo de `F6`.
8. **La obligación 5 del sobre, en su parte honesta:** verifiqué los SHA-256 del emisor y del
   derivador en los dos commits. **Eso no prueba que los binarios que corrieron fueran ésos.**
   El propio sobre lo retira (`Z-11`) y yo no lo recupero.
9. **No sé si mis relevos leyeron lo que dicen haber leído** (§3.6). Verifiqué el SHA-256 del
   fichero y ~25 de sus citas. Es fiabilidad medida, no lectura probada.
10. **No he juzgado suficiencia, validez formal del gate ni certificación.** `BB-03` contiene mi
    razonamiento sobre la validez **como insumo**, no como decisión. **Es de `DD`.**

---

## 9 · CIERRE PARA EL ADJUDICADOR `DD`

**Lo que te entrego, y en qué orden usarlo:**

1. **El sobre no falla. No falles el gate por ahí.** 17 campos recalculados por mí de commits
   inmutables, los dos digest de universo con la receta publicada y sin ejecutar el emisor, los
   dos árboles por separado, las dos refs contra el remoto de verdad. **Cero discrepancias.** Y
   **la vía que invalidó el gate 4 está cerrada y medida**: los dos bloques embebidos son el
   fichero byte a byte, el tercer relevo no transcribió. **El gate 5 NO está contaminado por la
   vía del gate 4.**
2. **Se audita LA CANDIDATA** (§4), por el manifiesto, por el sobre y por la doctrina que `U` y
   `AA` ya establecieron. **Diecisiete de mis veintidós hallazgos son del objeto auditado; cinco
   son del aparato.** No los mezcles en ninguna dirección: no castigues a la candidata por
   `BB-01`, y no absuelvas al aparato porque la candidata esté limpia.
3. **`BB-01` es lo más grave que traigo, y no por su daño sino por su significado.** Quinta
   recurrencia consecutiva, con el remedio escrito de una línea por el dictaminador del gate
   anterior, cometida por el commit del gate que viene a juzgar la disciplina. **Lo verifiqué en
   los dos árboles yo mismo: candidata 13/13 limpio, gate 12/13 con `T147` en rojo y dos
   ficheros de evidencia sucios.**
4. **`BB-02` es la reincidencia más elocuente**, porque `AA` la declaró ROTA hace un gate y el
   sobre de éste manda mirarla primero. **Pero no la infles: `BB-03` demuestra que su segunda
   mitad no es lo que mi relevo creyó**, y que la resta cierra a 0 contra el objeto declarado.
5. **`BB-03` es mío y es el que más te va a servir a medio plazo.** El remedio de `AA-01` —
   correcto, necesario y bien implementado — hizo del manifiesto una fila de su propio universo,
   y con eso `OBLIGATORIO − ASIGNADO = 0` sobre el árbol del gate **es insatisfacible por punto
   fijo de SHA-256**. **Si nadie toca el enunciado, el gate 6 registrará una sexta reincidencia
   de algo que nadie puede cumplir.** Cuesta una palabra arreglarlo.
6. **`BB-04` y `BB-05` son reincidencias del hallazgo mismo, no de su clase**, con la orden de
   retirarlas ya dada por `AA` y sin coste. Son la clase de la que nació `O19`, en el gate
   convocado para juzgar si alguna paráfrasis amplía el texto canónico.
7. **Lo que consta a favor, y no es cortesía** (§3.7): el DISEÑO no ha cambiado, verificado
   cláusula a cláusula; `D108` nunca aparece como autoridad; las tres citas de `Y-05` están
   reatribuidas de verdad; `X55` y `X58` —los contratos de `F6`— están bien corregidos;
   `AA-02` está genuinamente corregido y lo comprobé por sus dos comandos; **`AA-05` está
   CERRADO** y nadie de mi cadena podía decirlo; las series `D` y `O` están completas; la
   candidata pasa 13/13 sin ensuciar un byte y sus 74 filas cuadran al dígito.
8. **Ninguno de mis veintidós es BLOQUEANTE.** Ninguno exige arquitectura nueva. **Ninguno
   vuelve al Owner.** Los veintidós se cierran con material que el corpus ya tiene escrito, y
   **once de las doce clases reincidentes tienen el remedio literalmente redactado por el gate
   anterior.**
9. **Y mi respuesta a la pregunta central** (§6): la circularidad ya no es la causa, y lo
   demuestro por replicación de cinco lectores. **Lo que falla es que el sistema cierra
   instancias y no clases**, y lo mido: 19 de 22 reincidentes, 11 con remedio escrito, y cuatro
   casos donde la corrección se aplicó con la forma sintáctica exacta del contraejemplo y el
   defecto sobrevivió una sede más allá — una de ellas **quince líneas por encima de la nota que
   la corrige**.
10. **Léeme con desconfianza donde toque.** §7.1 documenta cómo estuve a punto de retirar un
    GRAVE verdadero con una refutación que parecía impecable y era un `sort` mal invocado. Lo
    dejé escrito para que sepas qué clase de error puede haber en lo que no refuté.

```text
git status --porcelain   AL ABRIR    →  VACÍO
git status --porcelain   AL CERRAR   →  VACÍO
HEAD al abrir y al cerrar            →  5ed7a3b805c472934cea9a4027d61e8ef7be5a35, idéntico
RAMA                                 →  gate/f4c-certificacion-5-20260831
FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ   ninguno
COMMITS · PUSH · PR · MERGE                                     ninguno
LA BATERÍA                           →  ejecutada SÓLO en checkouts aislados fuera del
                                        repositorio (`read-tree` + `checkout-index`).
                                        El árbol de trabajo NUNCA pasó por un estado sucio
SUBAGENTE `Agent`                    →  NO USADO
NINGÚN HALLAZGO SE HA CORREGIDO, y es deliberado: quien corrige no certifica
```

> **No emito veredicto de certificación: es de `DD`.**
> **REVISOR `BB` · dictamen cerrado por `BB4`, dictaminador.**


---

## §B · DICTAMEN DE LA CADENA `CC`, FIRMADO POR `CC3` — TRANSCRIPCIÓN LITERAL

# DICTAMEN DE LA CADENA `CC` — QUINTO GATE DE CERTIFICACIÓN DE F4c

**Firmante:** `CC3`, dictaminador de la cadena técnica `CC`.
**Fecha:** 2026-08-31.
**Repositorio:** `/home/jose/ads-kernel` · rama `gate/f4c-certificacion-5-20260831`.
**Independencia:** contexto limpio. No participé en ningún gate anterior.
**Este fichero es el dictamen.** No hay versión resumida que lo sustituya.

---

# 0 · EL SOBRE · SHA-256, MI VERIFICACIÓN, Y LOS BLOQUES EMBEBIDOS DE MIS RELEVOS

## 0.1 · SHA-256 del sobre, tal como lo recibo del fichero

```
906b74f70a30785465d56ecc68cf30e42b461febc7042e2a463aae5e8a899070  SOBRE-GATE-5.txt
14328 bytes · 190 líneas
```

Comando:

```
sha256sum /tmp/.../scratchpad/SOBRE-GATE-5.txt
```

El sobre vive FUERA del repositorio auditado. No lo transcribo a mano en ningún
punto de este dictamen: cuando cito un campo, cito y verifico, no copio para que
otro se fíe. Ésa fue la causa declarada de invalidez del cuarto gate.

## 0.2 · Verificación de cada campo, hecha por mí, sin fiarme de mis relevos

Todas las lecturas con `git show <commit>:<ruta>`. Ni un byte del árbol de trabajo.

| Campo del sobre | Valor del sobre | Mi recálculo | ¿Reproduce? |
|---|---|---|---|
| COMMIT CANDIDATO existe | `8c9ca9c…` | `git cat-file -t` → `commit` | SÍ |
| COMMIT DEL GATE existe | `5ed7a3b…` | `git cat-file -t` → `commit` | SÍ |
| ARBOL CANDIDATO | `91fe62d369152f9d1b58361f0ffc888358364175` | `git rev-parse 8c9ca9c^{tree}` → idéntico | SÍ |
| ARBOL DEL GATE | `6ab0fd2f7178502817f7361be2d8f62694b03585` | `git rev-parse 5ed7a3b^{tree}` → idéntico | SÍ |
| SHA-256 DEL MANIFIESTO | `0f08b961c31f03bbedbae700fa67029ac87b6b962067b39b3e504fe28e8d1939` | `git show 5ed7a3b:docs/.../F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md \| sha256sum` → idéntico | SÍ |
| SHA-256 DEL EMISOR (cand.) | `f1d5a3a9…c6715` | `git show 8c9ca9c:docs/evolucion/verificacion/emitir-sobre-de-ancla.py \| sha256sum` → idéntico | SÍ |
| SHA-256 DEL EMISOR (gate) | `f1d5a3a9…c6715` | idem sobre `5ed7a3b` → idéntico | SÍ |
| SHA-256 DEL DERIVADOR (cand.) | `107fbb03…8633` | `git show 8c9ca9c:docs/evolucion/verificacion/derivar-universo-obligatorio.py \| sha256sum` → idéntico | SÍ |
| SHA-256 DEL DERIVADOR (gate) | `107fbb03…8633` | idem sobre `5ed7a3b` → idéntico | SÍ |
| HEAD de la rama que audito | — | `git rev-parse HEAD` → `5ed7a3b805c472934cea9a4027d61e8ef7be5a35` = COMMIT DEL GATE | SÍ |

**Nota mía sobre el emisor y el derivador:** el sobre publica el MISMO SHA-256 de
emisor y de derivador en los dos commits, y yo lo confirmo. Eso quiere decir que
el commit del gate NO tocó ninguna de las dos herramientas: la única ruta en que
los dos universos difieren es el manifiesto. Lo verifico en 0.4.

## 0.3 · La sede canónica y los tres digest de resolución, con el `awk` del sobre

Comando exacto que corrí, por cada commit y por cada resolución:

```
git show <COMMIT>:docs/owner/ADS-OWNER-RESOLUCIONES.md |
  awk '/^# /{p = ($0 ~ /^# `O17`/)} p' | sha256sum
```

| | Sobre | Mi recálculo sobre `8c9ca9c` (candidata) | Mi recálculo sobre `5ed7a3b` (gate) |
|---|---|---|---|
| SEDE ENTERA | `db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a` | idéntico | idéntico |
| `O17` | `0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125` | idéntico | idéntico |
| `O18` | `ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353` | idéntico | idéntico |
| `O19` | `cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8` | idéntico | idéntico |

**«LOS DOS COMMITS PUBLICAN LA MISMA SEDE, byte a byte»** — CONFIRMADO por mí.

Recuentos de líneas que el sobre declara derivados y no escritos
(`O17` 85 · `O18` 111 · `O19` 78):

```
for O in O17 O18 O19; do git show 8c9ca9c…:docs/owner/ADS-OWNER-RESOLUCIONES.md |
  awk -v o="^# \`$O\`" '/^# /{p=($0~o)} p' | wc -l; done
→ 85 · 111 · 78
```

CONFIRMADO. Los tres. El sobre no infla ni una línea aquí.

## 0.4 · Los dos digest de universo, con la receta publicada, SIN EJECUTAR EL EMISOR

No ejecuté `emitir-sobre-de-ancla.py` en ningún momento. La receta del sobre sí
ejecuta el DERIVADOR, y eso es lo que corrí, extraído de su propio commit a un
directorio temporal fuera del repositorio auditado.

### Árbol candidato

```
C=8c9ca9c3920000bdf327cef7a6dbaf9aeff4eaeb
d=$(mktemp -d …/lab-CC3/candXXXX)
GIT_INDEX_FILE="$d/idx" git read-tree "$C"
GIT_INDEX_FILE="$d/idx" git checkout-index -a --prefix="$d/t/"
python3 "$d/t/docs/evolucion/verificacion/derivar-universo-obligatorio.py" --rutas 2>/dev/null | LC_ALL=C sort |
  while read -r r; do echo "$r $(git show "$C:$r" | sha256sum | cut -d' ' -f1)"; done |
  awk 'NR>1{printf "\n"}{printf "%s",$0}' | sha256sum
```

Salida literal:

```
RUTAS CANDIDATA: 74
18f50dabfd46cbd5e8129cc7e205714091226b914f8223186f88d61fee84c8b4  -
LINEAS=66747
```

Sobre: `18f50dabfd46cbd5e8129cc7e205714091226b914f8223186f88d61fee84c8b4` · 74 · 66747. **REPRODUCE.**

### Árbol del gate

```
C=5ed7a3b805c472934cea9a4027d61e8ef7be5a35    (misma receta)
```

Salida literal:

```
RUTAS GATE: 75
c152f8519235ca28e36af23c90266d79a7a2295a6dfc901290a0580d3c60987a  -
LINEAS=66940
```

Sobre: `c152f8519235ca28e36af23c90266d79a7a2295a6dfc901290a0580d3c60987a` · 75 · 66940. **REPRODUCE.**

### La ruta en que difieren

```
diff rutas-cand.txt rutas-gate.txt
29a30
> docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md
```

**UNA sola ruta, y es el propio manifiesto**, exactamente como el sobre declara
(«RUTAS EN QUE LOS DOS UNIVERSOS DIFIEREN: 1»). Los recuentos cuadran por
aritmética independiente: 75 − 74 = 1 · 66940 − 66747 = 193 líneas, que es el
tamaño del manifiesto en el árbol del gate. Lo compruebo en la sección 6.

**OBLIGACIÓN 1 DEL SOBRE, CUMPLIDA: los dos digest reproducen. El gate NO es
inválido por esta vía.**

## 0.5 · Los bloques embebidos de mis relevos, byte a byte

Mis dos relevos embebieron el sobre en su entrega. Extraje cada bloque por sus
vallas de código y lo comparé con el fichero original.

| Fuente | Vallas | Líneas extraídas | Bytes | SHA-256 | `diff` contra el original |
|---|---|---|---|---|---|
| `SOBRE-GATE-5.txt` (original) | — | 190 | 14328 | `906b74f7…9070` | — |
| `INFORME-CC1.md` líneas 29–218 | 28 ```` ```text ```` / 219 ```` ``` ```` | 190 | 14328 | `906b74f7…9070` | **vacío — IDÉNTICO** |
| `notas/CC2.md` líneas 8–197 | 7 ```` ```text ```` / 198 ```` ``` ```` | 190 | 14328 | `906b74f7…9070` | **vacío — IDÉNTICO** |

```
sed -n '29,218p' informes/INFORME-CC1.md > lab-CC3/sobre-CC1.txt
sed -n '8,197p'  notas/CC2.md            > lab-CC3/sobre-CC2.txt
sha256sum SOBRE-GATE-5.txt lab-CC3/sobre-CC1.txt lab-CC3/sobre-CC2.txt
diff SOBRE-GATE-5.txt lab-CC3/sobre-CC1.txt   → sin salida
diff SOBRE-GATE-5.txt lab-CC3/sobre-CC2.txt   → sin salida
```

**VEREDICTO DE 0.5:** los dos bloques embebidos son byte a byte el fichero
original, incluidos acentos, guiones largos, comillas invertidas y el salto de
línea final. **La patología que invalidó el cuarto gate —cinco copias a mano que
diferían en ocho campos— NO se repite en la cadena `CC`.** Es el único elemento
de este gate del que puedo decir, con prueba criptográfica y no con confianza,
que está resuelto.

---

# 1 · MANIFIESTO DE LECTURA

**Todo leído del COMMIT DEL GATE `5ed7a3b`** con `git show <commit>:<ruta>`, salvo los informes
de mis relevos, que viven fuera del árbol. SHA-256 y recuentos recalculados por mí.

## 1.1 · Mi lote propio

| # | ruta | líneas | SHA-256 recalculado por mí | cobertura |
|---|---|---|---|---|
| 1 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` | 334 | `db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a` | **LEÍDO ÍNTEGRO** · tramos `1-180 · 180-334`. Unión = [1, 334] |
| 2 | `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | 3343 | `24da5be1…` (blob) | **LEÍDO ÍNTEGRO** · `1-340 · 340-900 · 900-1560 · 1560-2250 · 2250-2810 · 2810-3343`. Unión = [1, 3343] |
| 3 | `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | 597 | `b0766d5d…` (blob) | **LEÍDO ÍNTEGRO** · `1-300 · 300-597`. Unión = [1, 597] |
| 4 | `docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md` | 3478 | — | **LEÍDO ÍNTEGRO** · `1-400 · 400-800 · 800-1150 · 1150-1450 · 1450-1750 · 1750-2050 · 2050-2350 · 2350-2650 · 2650-2950 · 2950-3250 · 3250-3478`. Unión = [1, 3478] |
| 5 | `docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md` | 2913 | — | **LEÍDO ÍNTEGRO** · `1-300 · 300-600 · 600-850 · 850-1100 · 1100-1350 · 1350-1600 · 1600-1850 · 1850-2100 · 2100-2350 · 2350-2650 · 2650-2913`. Unión = [1, 2913] |
| 6 | `docs/evolucion/24-TERCER-GATE-DE-CERTIFICACION-F4C.md` | 2515 | — | **LEÍDO ÍNTEGRO** · `1-270 · 270-540 · 540-810 · 810-1080 · 1080-1350 · 1350-1620 · 1620-1890 · 1890-2150 · 2150-2400 · 2400-2515`. Unión = [1, 2515] |
| 7 | `docs/evolucion/verificacion/README.md` | 355 | `d2f2298a…` (coincide con el de `CC1`) | **LEÍDO ÍNTEGRO** · `1-60 · 60-90 · 90-205 · 205-255 · 255-330 · 330-355`. Unión = [1, 355] |
| 8 | `docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md` | 2754 | — | **LEÍDO ÍNTEGRO, Y ES EL ÚLTIMO QUE ABRÍ**, como el encargo manda · `1-270 · 270-540 · 540-810 · 810-1100 · 1100-1330 · 1330-1560 · 1560-1800 · 1800-2040 · 2040-2280 · 2280-2520 · 2520-2754`. Unión = [1, 2754] |

**Listé el directorio `docs/owner/` del commit del gate y contiene TRES ficheros.** No hay un
cuarto: `git ls-tree -r 5ed7a3b docs/owner/` devuelve exactamente esos tres. La sede canónica
la leí **también**, porque es la autoridad contra la que contrasto.

## 1.2 · Los informes de mis relevos

| ruta | líneas | cobertura |
|---|---|---|
| `.../informes/INFORME-CC1.md` | 997 | **LEÍDO ÍNTEGRO** · `1-28` · `29-218` (el sobre embebido, cotejado byte a byte en §0.5) · `219-600` · `600-997`. Unión = [1, 997] |
| `.../notas/CC2.md` | 639 | **LEÍDO ÍNTEGRO** · `1-7` · `8-197` (el sobre embebido) · `198-420` · `420-639`. Unión = [1, 639] |

## 1.3 · Fuentes abiertas FUERA de mi lote, y por qué

- `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` — **NO la leí como
  documento**: es lote de `CC1`. Abrí y ejecuté las regiones que sostienen cada hallazgo que
  adjudico —`_EXCLUIDO` L1826-1841, `_en_zona`, `NORMATIVO` L1984-1990, `_EN_CORRECCION`
  L1848, `_regiones_historicas` L2258-2352, `_fase0_conforme` L3411-3433, `_negativa` L3524-3529—
  **y ejecuté cada afirmación en vez de leerla**. No adjudico nada sobre ella como código.
- `docs/evolucion/verificacion/derivar-universo-obligatorio.py` — ejecutado dentro de la receta
  del sobre y sobre mis copias; abrí su `_EXCLUIDO` L140-144. **No lo leí íntegro:** es lote de `CC2`.
- El manifiesto del gate (193 líneas) — **LEÍDO ÍNTEGRO por mí** para poder derivar `CC2-01`.
  Es la fuente que §6 demuestra que **nadie tenía asignada**.
- `emitir-sobre-de-ancla.py` — **NO ejecutado y no leído**. Sólo recalculé su SHA-256 en los
  dos commits.

## 1.4 · La resta

```text
ASIGNADO A `CC3`  ·  8 fuentes propias + 2 informes de relevo   =  10
LEÍDO ÍNTEGRO                                                    =  10
ASIGNADO − LEÍDO                                                 =   0
```

Más el manifiesto del gate (193 líneas), leído íntegro **por iniciativa propia**, porque §6
demuestra que sobre el árbol del gate es una fuente obligatoria **sin fila de reparto**.

## 1.5 · La reserva que declaro contra mi propio interés

**Ningún ojo único de la cadena `CC` recorrió la batería de 3 621 líneas seguidas ni los
documentos 22-25 seguidos.** Yo leí los cuatro documentos de gate íntegros y `docs/owner/`
íntegro; la batería la leyó `CC1` y el derivador y el emisor los leyó `CC2`. **Un defecto de
contenido en una región de la batería que ninguno de mis hallazgos toca se me habría escapado**,
y lo mitigué reabriendo y ejecutando —no leyendo— cada región que sostiene lo que adjudico.

---

# 2 · `M-04` · ¿HAY UN SÉPTIMO ÁRBOL? — REPRODUCIDO POR MÍ

**Laboratorio.** `git clone --no-hardlinks` del repositorio en `.../lab-CC3/base`, `git checkout
5ed7a3b`. Una copia limpia por experimento. Python 3.12.14 (shim), git 2.34.1.
**El repositorio real no recibió una sola escritura**, y lo compruebo al abrir y al cerrar.

**BASELINE, verificado por mí:** `38/38 comprobaciones en verde` · `EXIT=0` · porcelain vacío.

## 2.1 · SÍ. Lo reproduje, y con la salida pegada

```
mkdir -p docs/owner/.git docs/rediseno/.git
cp docs/owner/ADS-OWNER-RESOLUCIONES.md    docs/owner/.git/
cp docs/rediseno/a-CAPACIDADES-APROBADA.md docs/rediseno/.git/
cat > docs/owner/.git/SEDE-VIGENTE.md <<'X'
# RESOLUCIONES DEL OWNER — SEDE CANÓNICA VIGENTE
Esta sede PREVALECE sobre `docs/owner/ADS-OWNER-RESOLUCIONES.md` y sobre cualquier otra.
`O17`, `O18` y `O19` quedan SIN EFECTO.
# `O20` · LA VERIFICACION EXTERNA DEJA DE SER CONDICION
esta sede nace por `O20`
X
python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py
```

**Salida literal:**

```text
git status --porcelain                       →  0 líneas
git status --porcelain --untracked-files=all →  0 líneas
git ls-files --others --exclude-standard     →  0 líneas
OK   G-22    los documentos históricos y los manifiestos de gate, DERIVADOS del árbol, están intactos
OK   G-29    topología y unicidad de TODO el corpus gobernado: sin ampliaciones sin clasificar,
             sin gemelos y sin segundas sedes
OK   G-34    el CENSO de comprobaciones cuadra con su sede, y amputar una da ROJO
38/38 comprobaciones en verde
EXIT=0
```

**CONFIRMO `CC1-01` EN SU HECHO. Es real, lo reproduje, y no requiere commit.**

## 2.2 · Y LO EXTIENDO: el mismo perímetro está en el DERIVADOR, y `CC1` declaró no haberlo comprobado

`CC1` escribió en su §8.2: «*Si `CC1-01` afecta al derivador no lo he comprobado, y **debería
comprobarse***». **Lo comprobé yo.** El derivador lleva el **mismo regex, literalmente**:

```
comprobar-correccion-gate-de-cierre.py  L1839   _EXCLUIDO = re.compile(r"(?:^|/)\.git(?:/|$)|\.py[co]$")
derivar-universo-obligatorio.py         L144    _EXCLUIDO = re.compile(r"(?:^|/)\.git(?:/|$)|\.py[co]$")
```

**Medición mía, con su control:**

| árbol | `derivador --rutas` | batería |
|---|---|---|
| limpio | **75** | `38/38` |
| segunda sede en `docs/owner/.git/` | **75** — *sin cambio* | `38/38` |
| **CONTROL** · el mismo fichero como `docs/owner/SEDE-VIGENTE.md` | **76** — *la zona crece* | **`37/38`** |

**Consecuencia que nadie de mi cadena midió: el defecto cruza los DOS instrumentos.** Un
fichero plantado ahí no entra en el universo obligatorio, no recibe fila de manifiesto, no
recibe revisor **y no altera el digest que el sobre publica**. El control cierra el hallazgo
como defecto de **perímetro**, no de idea: el mismo fichero con nombre ordinario da `FALLO G-29`
y hace crecer el universo, que es exactamente lo correcto.

## 2.3 · LA PRUEBA QUE DECIDE LA CLASE, Y QUE `CC1` NO HIZO

El objeto que este gate audita **es un COMMIT**. El sobre lee todo con `git show <commit>:<ruta>`
y su receta materializa el árbol con `git read-tree` + `git checkout-index`. Así que la
pregunta que decide la severidad no es «¿pasa la batería?» sino **«¿puede ese fichero llegar al
objeto auditado?»**. La contesté:

```text
git add -f docs/owner/.git/SEDE-VIGENTE.md          → rc=0, y NO indexa nada
git add -A                                          → rc=0, porcelain sigue en 0
git update-index --add  docs/owner/.git/SEDE-…md    → "Ignoring path docs/owner/.git/SEDE-VIGENTE.md"
git update-index --add --cacheinfo 100644,<blob>,…  → "error: Invalid path"  ·  rc=128
git ls-files | grep -c 'owner/.git'                 → 0
```

**Git rechaza la ruta en TODOS los niveles, fontanería incluida.** Sólo `git mktree` +
`git commit-tree`, que no validan nombres, construyen tal commit. Y entonces:

```text
NEWC=$(git commit-tree <árbol fabricado> -p 5ed7a3b -m poison)
git show $NEWC:docs/owner/.git/SEDE-VIGENTE.md      → lo imprime  (el blob existe)
── LA RECETA DEL SOBRE SOBRE ESE COMMIT ──
GIT_INDEX_FILE=$d/idx git read-tree "$NEWC"
    error: invalid path 'docs/owner/.git/SEDE-VIGENTE.md'      rc=128
GIT_INDEX_FILE=$d/idx git checkout-index -a --prefix="$d/t/"
    (no materializa nada: $d/t/docs/owner/ no existe)
python3 "$d/t/…/derivar-universo-obligatorio.py" --rutas       →  0 rutas
```

> **LA CADENA DE ANCLAJE FALLA CERRADO ANTE ESE COMMIT.** El revisor que siga la receta
> obtiene cero rutas y un digest que no reproduce, y la obligación 1 del sobre le ordena
> declarar el gate INVÁLIDO sin seguir leyendo. **El ataque no puede alcanzar el objeto
> auditado en silencio.**

**Y ésta es la diferencia material con `Z1-03`≡`Z-05`, el caso de `__pycache__` que el
comentario cita como precedente:** allí el revisor `Z` **sí** consiguió `git add -f` y el
veneno **entró en un commit**. Aquí no puede. El comentario de la batería trata los dos casos
como el mismo, y **no lo son**.

## 2.4 · MIS TRES RESPUESTAS, QUE ES LO QUE EL ENCARGO ME PIDE

**¿ES REAL?** **SÍ, sin matices.** Reproducido por mí con salida pegada, con su control
positivo en rojo, y extendido al derivador, que nadie había medido.

**¿REQUIERE PRIVILEGIO — Y ES POR TANTO CLASE `C`?** **Hay que partirlo, y es el trabajo del
dictaminador partirlo.**

- **El ATAQUE es, en sus consecuencias, de la familia `C`, y NO es exigible en `F4c`.** Requiere
  escritura sobre el árbol de trabajo del auditado; **no puede llegar al commit** que es el
  objeto juzgado; y si alguien fabrica ese commit con fontanería, **la propia cadena de anclaje
  falla cerrado**. Un fichero que sólo vive en el árbol de trabajo de otro no lo lee ningún
  revisor: el manifiesto reparte rutas de un COMMIT. **Lo que ese ataque compra es que la
  batería diga «38/38» sobre un árbol de trabajo sucio — y el árbol de trabajo no es lo que se
  certifica.** No lo cuento como defecto bloqueante de esta tanda.
- **La PROMESA es clase `A`, y ÉSA SÍ es exigible.** El README publica de `G-29`: «*el perímetro
  **YA NO SE ESCRIBE**: es el repositorio **ENTERO** menos `.git` y el bytecode*» y «*el
  perímetro de exclusión es hoy uno solo y **por NATURALEZA**»*. **Es falso.** `.git` se excluye
  **por su nombre y a cualquier profundidad**, que es escribir un perímetro, no derivarlo. Y el
  comentario que precede a la línea escribe **el argumento que la condena**, sobre `__pycache__`:
  «*Un directorio no es un artefacto de bytecode: **admite cualquier cosa**»* y «*una lista de lo
  que se excluye **no puede caducar por omisión**: lo que olvide nombrar se queda DENTRO*».
  Las dos frases se aplican **palabra por palabra** a `.git`, y la línea las incumple.

**¿ESTÁ DECLARADO EN «LO QUE ESTA BATERÍA NO COMPRUEBA»?** **La CLASE sí; la PROMESA no.** Leí
esa sección íntegra. Declara «`NO PUEDE CERRAR M-04, Y NO LO PRETENDE` … *quien pueda escribir
el árbol puede editar la batería, su README y la declaración de instrumental EN CORRECCIÓN a la
vez*». Eso cubre el ataque. **Lo que no declara —y contradice— es que el perímetro esté
derivado.** Es una promesa incumplida, y `grep` sobre el README confirma que la carencia no
figura en ninguna fila de esa sección.

## 2.5 · Y EL ARGUMENTO QUE SALE DE MI PROPIO LOTE, Y QUE NADIE HA USADO

**La arquitectura APROBADA por el Owner nunca coloca un `.git` dentro del repositorio de
control.** Lo leí íntegro. §3.1 fija la topología estándar como **repos hermanos**, cada uno con
su `.git` **al mismo nivel**; y §4.3 declara expresamente que la topología a **EVITAR** es
justamente la anidada:

> «**Tampoco debe contener clones Git de los repositorios técnicos en su interior.** Debe
> evitarse: `ads/ ├── .git/ └── workspace/ ├── frontend/.git/ └── backend/.git/` **como
> topología ADS estándar.** La forma estándar es de hermanos.»

Y el invariante `I2` lo remata: «*Ninguna source técnica necesita contener ADS para participar*».

> **Se sigue: dentro del repositorio de control, el ÚNICO `.git` legítimo es el de la raíz.**
> Excluirlo «a cualquier profundidad» no sirve a ningún caso que el material APROBADO del Owner
> contemple. **El remedio —anclar la exclusión a la raíz— no sólo es barato: es lo que la
> arquitectura aprobada ya presupone.** Es clase `A` y su remedio está determinado.

## 2.6 · `CC1-02` — REPRODUCIDO

```
docs/rediseno/00-MAPA.md ← encabezado nuevo «SEDE NORMATIVA QUE PREVALECE … `O17` SIN EFECTO»
README.md (raíz)         ← «NORMA RAIZ QUE PREVALECE … `O17`, `O18` y `O19` SIN EFECTO»
python3 …/comprobar-correccion-gate-de-cierre.py
   →  38/38 comprobaciones en verde · EXIT=0
   git status --porcelain →  ` M README.md` · ` M docs/rediseno/00-MAPA.md`
```

**REPRODUCIDO.** `NORMATIVO` (L1986-1990) es un regex de **seis patrones enumerados** que cubre
**4 de los 14** ficheros de `docs/rediseno/` y **ninguno** de la raíz. El README promete de
`G-23` «**lo normativo intacto**», sin matiz. **Y comprobé que la carencia NO está declarada:**
`grep` de `NORMATIVO`, `00-MAPA`, `REVISION-ADVERSARIAL` y `AUDITORIA-INDEPENDIENTE` sobre el
README devuelve **0**. **Atenuante que digo yo:** `git status` sí lo ve, luego el emisor del
sobre se negaría a emitir sobre ese árbol.

## 2.7 · `CC1-03` — REPRODUCIDO EN EL HECHO, Y SUSTANCIALMENTE **DECLARADO**

```
docs/owner/vigente/ADS-OWNER-RESOLUCIONES.md  («esta sede nace por `O20`» · PREVALECE ·
                                               `O17`, `O18` y `O19` SIN EFECTO)
+ una línea en docs/evolucion/00-INDICE.md:
  - [sede vigente del Owner](../owner/vigente/ADS-OWNER-RESOLUCIONES.md)
   →  38/38 comprobaciones en verde · EXIT=0

CONTROL MÍO, que `CC1` no pegó: la MISMA sede SIN el enlace del índice
   →  37/38 · FALLO G-29
```

**El hecho es real y el control lo cierra como defecto de composición.** Pero el detalle de
`G-22` que yo obtuve dice **mucho más** de lo que `CC1` citó:

> `OK G-22 … · 4 EXENTOS y NOMBRADOS, por ser el objeto declarado de esta tanda —**`00-INDICE.md`
> entre ellos, que es la sede que gobierna la ADMISIÓN**—: [...] · 1 todavía sin confirmar y por
> tanto sin línea base: ['docs/owner/vigente/ADS-OWNER-RESOLUCIONES.md']`

Y el README declara las **dos** mitades y además la apertura: «*uno de ellos es `00-INDICE.md`,
**que es la sede que gobierna qué se admite en `docs/owner/`**… Editar sólo `00-INDICE.md`
sigue dando `38/38` y ahora el informe dice que no se ha contrastado. **Que esa exención CADUQUE
… queda ABIERTA y dicha**»*.

> **`CC1` afirma que «en ningún sitio dice que la composición admita una segunda sede canónica
> del Owner en verde». La consecuencia exacta no está escrita; las dos premisas Y la apertura
> del hueco SÍ, en el README y en el propio detalle de la batería.** Es el remedio de `AA-03`
> del documento 25 —«el detalle NOMBRA a sus EXENTOS»— ejecutado. **Lo rebajo a MENOR y digo
> por qué en §5.**

---

# 3 · CLASIFICACIÓN `A` / `B` / `C` DE CADA HALLAZGO QUE SOSTENGO

## 3.1 · La definición que aplico, y de dónde la saco

**No me la invento.** La fijó `O18`, la aplicó `W3` en el documento 24 y la confirmaron `X`,
`Y4`, `Z3` y `AA`. La leí en su sede y la transcribo:

```text
CLASE A   la batería, sobre un árbol que se le entrega, NO detecta una incoherencia que ESTÁ
          en ese árbol — sin que el atacante toque la batería, su README, `HEAD`, las refs, la
          revisión base ni el runner. Es un fallo de COHERENCIA INTERNA
CLASE B   el aparato que dice demostrar QUÉ se analizó no lo demuestra, o publica de un objeto
          algo que no es suyo
CLASE C   el atacante tiene que corromper la REFERENCIA: commitear para que `HEAD` la absorba,
          reescribir la base, editar la batería y su README a la vez, o mentir el runner.
          `O18` la declara NO IMPLEMENTADA y la contrata para `F6`. NO es exigible en `F4c`
```

## 3.2 · LA PRUEBA DEL OWNER QUE NADIE DE MI CADENA CITÓ, Y QUE DECIDE MI CLASIFICACIÓN

Leí `O18` íntegra en la sede canónica. **Contiene el test que el propio Owner fija para cerrar
`M-04` dentro de `F4c`, y son SEIS condiciones:**

> «**`M-04` puede cerrarse para el alcance de `F4c` únicamente si el gate independiente
> demuestra:** batería interna coherente · sobre externo recibido antes de leer · todas sus
> huellas coincidentes · referencias remotas intactas · cobertura completa · **ninguna promesa
> de seguridad superior a la realmente entregada**.»

Y dos bloques antes, el Owner escribe qué NO se afirma —«*`F4c` **NO** afirma resistencia
completa frente a un actor privilegiado*»— y qué **sí** garantiza la batería interna:
«*coherencia interna · detección de regresiones conocidas · derivación de inventarios ·
contradicciones entre fuentes · cambios respecto a referencias recibidas · cumplimiento de
contratos documentales*».

> ### **ESTO ES LO QUE ORDENA MI DICTAMEN, Y LO DIGO CON TODAS LAS LETRAS.**
>
> El Owner **excluyó** la resistencia al actor privilegiado —clase `C`— y **convirtió en
> condición de cierre** que no haya «**ninguna promesa de seguridad superior a la realmente
> entregada**». **Prometer de más no es una objeción de estilo: es uno de los seis requisitos
> que el Owner impone para cerrar `M-04` en `F4c`.**
>
> Por tanto: **la mitad ATAQUE de los hallazgos de mi cadena es `C` y no bloquea. La mitad
> PROMESA es `A` y es exactamente lo que el Owner exige demostrar.** Y **cinco de mis seis
> hallazgos son de promesa.**

## 3.3 · La tabla

| id mío | qué es | **clase** | ¿bloquea? | por qué esa clase |
|---|---|---|---|---|
| **`CC-01`** | el perímetro de exclusión de `.git` está **escrito**, no derivado, en los DOS instrumentos, y el README promete lo contrario | **`A`** *(la promesa)* · el ataque es **`C`** | **la promesa, SÍ** | El ataque exige escritura y **no puede alcanzar el commit**: la cadena de anclaje falla cerrado (§2.3). La promesa —«el perímetro YA NO SE ESCRIBE… por NATURALEZA»— es falsa sobre el árbol y **cae de lleno en la sexta condición de `O18`** |
| **`CC-02`** | `G-23` promete «lo normativo intacto» sobre un regex enumerado que cubre 4 de 14 ficheros, y la carencia **no está declarada** | **`A`** | **SÍ** | La batería, sobre el árbol que se le entrega, no detecta que material APROBADO ha sido reescrito. No toca batería, README, `HEAD`, refs ni base. Es `A` por definición, y es promesa excesiva |
| **`CC-03`** | la única prueba negativa «ANCLADA EN EL ÁRBOL» tiene la mitad MUTANTE **tautológica** | **`A`** | contribuye | Promesa: «*un corpus distinto la mueve*» es falso del veredicto del mutante. No es ataque: es clasificación falsa de un instrumento |
| **`CC-04`** | el manifiesto del gate rotula «—sobre el árbol del GATE—» cifras del árbol de la CANDIDATA, y su `OBLIGATORIO − ASIGNADO = 0` es 1 sobre el árbol que nombra | **`A`** | **NO invalida; sí cuenta** | Es el aparato de cobertura diciendo de un objeto algo que no es suyo. Roza `B`, pero **el sobre —que es el demostrador de `B`— publica los DOS universos correctamente y nombra la ruta divergente**: `B` no falla. Falla la coherencia interna del manifiesto |
| **`CC-05`** | el README enumera los cierres de región de `G-26` sin la excepción que el código aplica a la clase `tanda` | **`A`** | no por sí solo | Promesa incompleta. El mecanismo real está declarado en el comentario del propio código |
| **`CC-06`** | dos párrafos contradictorios vivos en el README, en la nota que declara ese defecto corregido | **`A`** | no | Higiene. Ninguna comprobación depende de esa prosa |

```text
A · COHERENCIA INTERNA          6   los seis que sostengo
B · IDENTIDAD DE LA CANDIDATA   0   NINGUNO. Ver §3.4
C · ACTOR PRIVILEGIADO          0   NO declaro insuficiencia por `C`, y lo digo expresamente
DECISIÓN DEL OWNER              0   ninguna vuelve al Owner
```

## 3.4 · `B` NO FALLA EN ESTE GATE, Y LO DIGO CON LA MISMA FUERZA CON QUE DIGO LO DEMÁS

Es la primera vez en cinco gates que se puede escribir esto, y por eso lo separo:

```text
· el sobre viajó como FICHERO EXTERNO, idéntico para todos por construcción, y lo demuestro:
  los bloques embebidos de mis DOS relevos son BYTE A BYTE el original (§0.5). La causa por la
  que el CUARTO gate fue declarado INVÁLIDO —cinco transcripciones a mano con OCHO campos
  divergentes— está CERRADA de raíz, no mitigada
· los DOS digest de universo reproducen con la receta publicada y SIN ejecutar el emisor
· los dos árboles se publican por separado, cada uno con su propio derivador y sus propias
  cifras, y el sobre NOMBRA la única ruta en que difieren. `U-02`→`X-06`→`Z-12` NO reincide:
  lo miré primero, como manda la obligación 3, y la fila del derivador es IDÉNTICA en los dos
· la sede canónica y sus tres digest reproducen en los DOS commits, con el `awk` publicado
· el emisor y el derivador tienen el MISMO SHA-256 en los dos commits: el gate NO tocó el
  instrumental después de publicar el manifiesto. La regla que el `-4B-` estrenó se cumplió
```

> **`B` ESTÁ DEMOSTRADA.** Ninguno de mis seis hallazgos es `B`, y no lo fuerzo para engordar
> el dictamen. Lo digo porque `B` falló en los gates de los documentos 24 y 25, y esta vez no.

## 3.5 · `C`, ejecutada por mí y NO CONTADA

Ejecuté el ataque de clase `C` más directo y **no lo cuento contra esta tanda**:

```text
árbol fabricado con `git mktree` + `git commit-tree` que contiene docs/owner/.git/SEDE-VIGENTE.md
   git show <commit>:docs/owner/.git/SEDE-VIGENTE.md   → lo imprime
   la RECETA DEL SOBRE sobre ese commit                → read-tree rc=128, 0 rutas · FALLA CERRADO
```

Exige fontanería de Git y **la cadena de anclaje lo caza**. `O18` declara `C` NO IMPLEMENTADA y
la contrata para `F6`. **NO lo cuento. Contar `C` como `A` es lo que haría que la tanda
siguiente escribiera la protección diecinueve, y `X`, `AA` y el Owner lo prohibieron.**

---

# 4 · HALLAZGOS QUE SOSTENGO

**Severidad ADJUDICADA POR MÍ**, con el criterio que los cinco gates anteriores usan y que
transcribo para que `DD` compare sin traducir: **BLOQUEANTE** = obliga a decidir arquitectura
nueva · **GRAVE** = una garantía publicada no se sostiene · **MEDIO** = una afirmación vigente
es falsa sin cambiar el comportamiento · **MENOR** = editorial o de propagación.

**Ninguno de los seis es BLOQUEANTE. Ninguno vuelve al Owner. Los seis se cierran con material
que el corpus ya tiene escrito.**

---

## `CC-01` · **GRAVE** · clase `A` · el perímetro de exclusión sigue ESCRITO, en los DOS instrumentos, y el README publica lo contrario

**ORIGEN.** `CC1-01` (GRAVE). **Reproducido por mí, y EXTENDIDO al derivador**, que `CC1`
declaró expresamente no haber comprobado.

**FICHERO Y LÍNEA.**
· `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` **L1839**
· `docs/evolucion/verificacion/derivar-universo-obligatorio.py` **L144**
· `docs/evolucion/verificacion/README.md` **fila `G-29`**

**CITA LITERAL, las dos idénticas:**

    _EXCLUIDO = re.compile(r"(?:^|/)\.git(?:/|$)|\.py[co]$")

**CITA LITERAL DEL README, fila `G-29`:**

> «*topología y unicidad de TODO el corpus gobernado, y **el perímetro YA NO SE ESCRIBE: es el
> repositorio ENTERO menos `.git` y el bytecode***» … «***El perímetro de exclusión es hoy uno
> solo y por NATURALEZA**: `.git`, que no es corpus, y el bytecode **por su extensión**.*»

**CITA LITERAL DEL COMENTARIO QUE PRECEDE A L1839, que es lo que lo condena:**

> «*Esto decía `(?:^|/)(?:\.git|__pycache__)(?:/|$)|\.pyc$`: excluía un DIRECTORIO POR SU
> NOMBRE… **Un directorio no es un artefacto de bytecode: admite cualquier cosa.*** […] *El
> comentario de `G-29` escribe la regla que esta línea incumplía: «**una lista de lo que se
> excluye no puede caducar por omisión: lo que olvide nombrar se queda DENTRO**».*»

**POR QUÉ ES DEFECTO.** El argumento que el propio comentario escribe se aplica **palabra por
palabra** a `.git`. Un directorio llamado `.git` bajo `docs/owner/` **no es el almacén de git**
y admite cualquier cosa. La corrección retiró `__pycache__` —el caso que un revisor había
explotado— y **dejó el otro nombre intacto**: es cerrar con la forma exacta del contraejemplo,
que es el modo de fallo que cinco gates llevan nombrando. Y el motivo escrito —«no es corpus
sino el almacén contra el que se compara»— es cierto de **UN** directorio y el patrón lo aplica
a **todos**.

**MI COMANDO, y su salida, en §2.1-2.2.** Con su **control positivo**: el mismo fichero con
nombre ordinario → `37/38 · FALLO G-29` y el universo crece de 75 a 76. **Defecto de perímetro,
no de idea.**

**Y EL ARGUMENTO DEL MATERIAL APROBADO, que es mío y sale de mi lote (§2.5):**
`ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` §3.1, §4.3 e invariante `I2` establecen la topología de
**repos hermanos** y declaran **a evitar** la anidada. **Dentro del repositorio de control, el
único `.git` legítimo es el de la raíz.** Excluirlo a cualquier profundidad no sirve a ningún
caso que el Owner haya aprobado.

**SEVERIDAD GRAVE, y por la PROMESA, no por el ataque.** El ataque es `C` en sus consecuencias
—no alcanza el commit, la receta falla cerrado— y **no lo cuento como bloqueante**. Lo GRAVE es
que **una garantía publicada no se sostiene**, que es la definición, y que cae de lleno en la
sexta condición de `O18` para cerrar `M-04` en `F4c`.

**¿REINCIDENCIA DE QUÉ?** De la clase de perímetro que el expediente persigue desde el
documento 22: `Q-04`→`Q-02` (doc 22) · `W-04`/`T-03` (docs 23-24) · `Z-05` + `AA-E1` (doc 25).
**Es la CUARTA vez consecutiva que el perímetro de `G-29` es el hallazgo**, y la primera en que
el mismo defecto se demuestra **también en el derivador**.

**REMEDIO SUGERIDO, que no aplico:** anclar la exclusión de `.git` a la raíz de la ruta
relativa, en los dos ficheros. Dos caracteres.

---

## `CC-02` · **GRAVE** · clase `A` · «lo normativo intacto» sobre un perímetro enumerado que cubre 4 de 14 ficheros, y no está declarado

**ORIGEN.** `CC1-02` (GRAVE). **Reproducido por mí.**

**FICHERO Y LÍNEA.** batería **L1986-L1990**.

**CITA LITERAL:**

    NORMATIVO = (r"a-CAPACIDADES-APROBADA|b-RECORRIDO-APROBADA|"
                 r"a-ENMIENDA-E1|a-ENMIENDA-E2|"
                 r"kernel/operativo/contratos/C4-MATERIALIZACION|"
                 r"kernel/operativo/contratos/C7-GOBIERNO")

**MI COMANDO Y SU SALIDA (§2.6):** reescribí el encabezado de `docs/rediseno/00-MAPA.md` y el
`README.md` de la raíz declarando prevalecer sobre el material APROBADO y dejar `O17`·`O18`·`O19`
sin efecto → **`38/38 comprobaciones en verde` · `EXIT=0`**.

**POR QUÉ ES DEFECTO.** `G-29` clasifica `docs/rediseno/` como zona que **no admite ninguna
ampliación** «*porque es material APROBADO*», pero el **CONTENIDO** de esa zona sólo lo protege
este regex de seis patrones. De los **catorce** ficheros de `docs/rediseno/`, nombra **cuatro**.
El README publica de `G-23` «**lo normativo intacto**», sin matiz. **Y verifiqué que la carencia
no está declarada**: `grep` de `NORMATIVO`, `00-MAPA`, `REVISION-ADVERSARIAL` y
`AUDITORIA-INDEPENDIENTE` sobre el README → **0 golpes**.

**Y es exactamente lo que esta tanda declara haber dejado de hacer.** El README publica como
logro «*cambiar perímetros de enumerados a derivados*». **Éste se quedó enumerado.**

**ATENUANTE QUE DIGO YO, y por eso no es más que GRAVE:** `git status` **sí** lo ve, de modo que
el emisor del sobre se negaría a emitir sobre ese árbol.

**¿REINCIDENCIA DE QUÉ?** De la misma clase de perímetro escrito que `CC-01`, y del hallazgo
`W-05` del documento 24 —«que `G-01` deje de ser lista blanca», declarado **NO CERRADO** por
`Z3` y por `AA`—: **una lista blanca cerrada en un sitio y dejada abierta en otro.**

---

## `CC-03` · **MEDIO** · clase `A` · la única prueba negativa «ANCLADA EN EL ÁRBOL» tiene la mitad MUTANTE tautológica

**ORIGEN.** `CC1-04` (MEDIO). **Reproducido por mí, estructural y empíricamente.**

**FICHERO Y LÍNEAS.** batería **L3524-L3529** y **L3411-L3433**. README **fila `G-33`**.

**CITA LITERAL DEL CÓDIGO:**

    _b_mutilado = "\n".join(l for l in _b_real.split("\n")
                            if "FASE 0" not in l and "gate:sistema-conforme" not in l)
    _g33 += _negativa("macrocircuito que OMITE la FASE 0 Estructural", 13,
                      not _fase0_conforme(_b_real),
                      bool(_fase0_conforme(_b_mutilado)))

**CITA LITERAL DE `_fase0_conforme`, primera cláusula (L3417-3418):**

    if not re.search(r"FASE 0", bloque):
        faltan.append("no declara FASE 0")

**CITA LITERAL DEL README, fila `G-33`:**

> «*una prueba negativa **ANCLADA EN EL ÁRBOL** —su mutante sale del texto del corpus, y **un
> corpus distinto la mueve**—*»

**MI ARGUMENTO ESTRUCTURAL.** `_fase0_conforme` devuelve **una lista de lo que falta**;
`bool(...)` es verdadero si la lista no está vacía. El mutante borra **toda** línea que contenga
`FASE 0`, y la cadena `FASE 0` no contiene salto de línea, luego vive siempre dentro de una
línea. Por tanto `re.search("FASE 0", _b_mutilado)` es `None` **para todo `_b_real`**, la lista
nunca está vacía, y **la mitad MUTANTE es verdadera por construcción, para todo árbol posible.**

**MI COMANDO, ejecutado:** réplica literal de la primera cláusula y de la mutación, barrido
aleatorio de **300 000** textos sintéticos con y sin las dos cadenas gatillo →

```text
textos probados: 300000 · contraejemplos al «el mutante SIEMPRE carece de FASE 0»: 0
```

**LO QUE NO AFIRMO, y lo digo:** el par **sí** es sensible al árbol **por su mitad CONTROL** —un
§8.1 que perdiera la FASE 0 pondría `G-33` en rojo—, y el mutante **sí** caza una amputación de
`_fase0_conforme`. **Lo que falla es la CLASIFICACIÓN**, que es exactamente lo que `W-07` del
documento 24 corrigió en los otros cuatro y no terminó en éste. Por eso MEDIO y no GRAVE.

**¿REINCIDENCIA DE QUÉ?** De `T-09` (doc 23) y `W-07` (doc 24) —«un fixture que no pueda fallar
deja de contar»—, sobreviviendo **en la única prueba que la comprobación presenta como real**.

---

## `CC-04` · **MEDIO** · clase `A` · el manifiesto del gate rotula del árbol del GATE cifras que sólo son ciertas del árbol de la CANDIDATA, y deja UNA fuente obligatoria sin reparto

**ORIGEN.** `CC2-01` + `CC2-02`. **Los FUNDO en uno**, porque son el mismo hecho con dos
consecuencias, y contar dos veces el mismo defecto es lo que los cinco gates anteriores
prohíben. **Derivado por mí, no aceptado.**

**FICHERO Y LÍNEAS.**
`docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md`
**L37** (§2) y **L155-L161** (§6).

**CITAS LITERALES:**

> **L37:** «`UNIVERSO DERIVADO   74 fuentes · 66 747 líneas **—sobre el árbol del GATE—**`»
> **L155-161:** «`FUENTES OBLIGATORIAS 74 · LÍNEAS OBLIGATORIAS 66 747 … OBLIGATORIO menos
> ASIGNADO 0 · CERO FUENTES SIN ASIGNAR`»

**MI DERIVACIÓN, contra los DOS árboles, con la receta del sobre:**

```text
universo(CANDIDATA 8c9ca9c)  74 fuentes · 66 747 líneas · 18f50dab…
universo(GATE     5ed7a3b)   75 fuentes · 66 940 líneas · c152f851…

rutas únicas de las DOS tablas del manifiesto (§4 17 filas + §5 57 filas)   74
  universo(CANDIDATA) − manifiesto   =  ∅
  manifiesto − universo(GATE)        =  ∅        ← ninguna fila fantasma
  universo(GATE) − manifiesto        =  {docs/evolucion/verificacion/manifiestos/
                                          F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md}
CIERRE ARITMÉTICO   66 747 + 193 = 66 940, y 193 = wc -l del propio manifiesto en el gate
SUMA DE LAS DOS TABLAS   = 66 747 = el titular. La aritmética INTERNA es exacta
```

**LAS DOS CONSECUENCIAS, separadas porque el remedio es distinto:**

1. **RÓTULO.** «—sobre el árbol del GATE—» es **FALSO**: sobre ese árbol son 75 / 66 940.
2. **COBERTURA.** Sobre el árbol que el propio §2 nombra, `OBLIGATORIO − ASIGNADO = **1**`, y
   la fuente sin asignar **es el propio manifiesto**. Ningún revisor la tenía. `CC2` la leyó por
   iniciativa propia y yo también.

**MI COMANDO** está pegado arriba. La causa es **estructural y nueva**, y la identificó `CC2`:
al convertir `manifiestos/` en ZONA BARRIDA —que es el remedio correcto de `Z2-02`— **el
manifiesto del gate pasó a ser fuente de su propio universo**, y se escribió con la aritmética
de antes del remedio.

**¿REINCIDENCIA DE QUÉ?** De la clase `U-02` (doc 22) → `X-06` (doc 24) → `Z-12` (doc 25):
manifiesto que rotula un árbol y publica cifras de otro. **Con un agravante y un atenuante, y
digo los dos.** Agravante: el `-4B-` la había **ROTO** —lo verifiqué: sus 70/58 796 sí son su
árbol del gate— y el CORRIGENDUM lo dejó escrito como el ejemplo de lo que se hace bien.
Atenuante: **la fila del propio derivador, que es la que se falseó dos gates seguidos, aquí
casa contra los DOS árboles**, y la miré primero, como manda la obligación 3 del sobre.

**Por qué MEDIO y no GRAVE, y por qué NO invalida el gate: en §6, entero.**

---

## `CC-05` · **MENOR** · clase `A` · el README enumera un cierre de región que el código no aplica a una de sus tres clases

**ORIGEN.** `CC1-05` (MEDIO). **Reproducido por mí, y CORREGIDO EN SU ALCANCE: lo REBAJO.**

**FICHERO Y LÍNEAS.** batería **L2261-L2264** y **L2346-L2350**; README **fila `G-26`**.

**CITAS LITERALES DEL CÓDIGO:**

    _CAMPO_DE_TANDA_PASADA = re.compile(
        r"^[a-z]+(?:ado|ada|ido|ida|to|cho)_(?:en|por|para)_(?:la|el)_[A-Za-z0-9_]+:\s*$")
    _ABRE_CLAVE = re.compile(r"^\S")
    ...
        if (_CIERRA_REGION.match(linea)
                or (clase == "tanda" and _ABRE_CLAVE.match(linea))
                or (not linea.strip() and clase != "tanda")
                or (en_cita and not _LINEA_DE_CITA.match(linea))):

**CITA LITERAL DEL README, fila `G-26`:** «*la región **cierra al terminar el bloque que la
etiqueta encabeza** —encabezado, valla de código, **línea en blanco** también dentro de una
valla, salida de la cita, o **la marca siguiente**—*».

**MI COMANDO, con CINCO variantes y sus controles** — la misma cifra falsa al final del
checkpoint (`las DOCE presiones de §16 vigentes`; el derivado son 17):

| variante | resultado |
|---|---|
| **A** · sin marca *(control)* | **`EXIT=1` · FALLO `G-26`** |
| **B** · marca `corregido_en_la_TANDA_DE_O19:` + cifra INDENTADA | `EXIT=0` · **38/38 VERDE** |
| **C** · lo mismo + **DOS líneas en blanco** entre la marca y la cifra | `EXIT=0` · **38/38 VERDE** |
| **D** · marca `**[HISTÓRICO · …]**` + una línea en blanco | **`EXIT=1` · FALLO `G-26`** |
| **E** · marca de tanda + cifra en **COLUMNA 0** | **`EXIT=1` · FALLO `G-26`** |

**REBAJO DE MEDIO A MENOR, Y DIGO POR QUÉ — es una corrección a mi propio relevo.** `CC1`
escribe que la marca «*exime un bloque de longitud **NO ACOTADA***». **Es falso, y lo demuestro
con el experimento `E`, que `CC1` no corrió:** la región de clase `tanda` **cierra en la
siguiente línea que empieza en columna 0** (`_ABRE_CLAVE`), y la comprobación dispara. El
alcance es **el campo indentado**, exactamente lo que el comentario del propio código declara:
«*su alcance es SU campo, que termina donde empieza la clave siguiente*».

**LO QUE SÍ SOBREVIVE, y es el hallazgo:** la enumeración del README se publica **sin la
excepción**, y para una de las tres clases la línea en blanco **no** cierra nada. **Es promesa
incompleta, no mecanismo oculto:** el código lo declara en su comentario.

**¿REINCIDENCIA DE QUÉ?** De `T-06` (doc 23) → `W-01`/`W-02` (doc 24), la clase de la marca
histórica. **Y aquí consta a favor:** `W-01` se declaró **CERRADO Y GENERALIZA** en el documento
25 y lo sigue estando —la variante `D`, con `[HISTÓRICO]` y línea en blanco, **falla en rojo**—.

---

## `CC-06` · **MENOR** · clase `A` · dos párrafos contradictorios vivos, reincidencia literal de `Z1-06` en la nota que declara `Z1-06` corregido

**ORIGEN.** `CC1-06` (MENOR). **Reproducido por mí.**

**FICHERO Y LÍNEAS.** `docs/evolucion/verificacion/README.md` **L73** y **L78**.

**MI COMANDO Y SU SALIDA:**

```text
grep -n 'LA TABLA NO ESTÁ VACÍA\|LA TABLA ESTÁ VACÍA' README.md
  73:**LA TABLA NO ESTÁ VACÍA: la corrección posterior al CUARTO GATE está EN CURSO.** Los
  78:**LA TABLA ESTÁ VACÍA, y es lo que debe estar.** Los cambios de la tanda posterior al

L66-L71  →  el bloque de cita `>` de `Z1-06`.  Las L73 y L78 están FUERA de la cita: son
            texto vivo del README, no historia
L82-L84  →  la tabla: cabecera, separador y CERO filas de datos
```

**LA NOTA QUE LO CONDENA, cuatro líneas antes (L66-L71), literal:**

> «**`Z1-06`.** *Aquí vivían DOS párrafos consecutivos que se contradecían… **Se retira el que
> había caducado**, y queda uno solo.*»

**POR QUÉ ES DEFECTO.** **No queda uno solo: quedan los dos.** El rótulo caducado volvió a
sobrevivir al commit que vació la tabla, **en el mismo fichero y en la misma sección donde se
declara que eso se corrigió**. El estado real es el de L78; **L73 es falso**.

**SEVERIDAD MENOR** porque ninguna comprobación depende de esa prosa y el estado real se
verifica en una línea. **Lo consigno porque es la TERCERA vez que esta sección envejece igual**,
y porque es la forma exacta de `V-04` (doc 24) y `AA-02` (doc 25): **una declaración de
corrección que es falsa en el fichero que la escribe.**

---

## Recuento, derivado de las filas y no copiado

| severidad | nº | ids |
|---|---|---|
| **BLOQUEANTE** | **0** | — |
| **GRAVE** | **2** | `CC-01` · `CC-02` |
| **MEDIO** | **2** | `CC-03` · `CC-04` |
| **MENOR** | **2** | `CC-05` · `CC-06` |
| | **6** | clase `A` 6 · clase `B` 0 · clase `C` 0 |

**REPRODUCIDOS POR MÍ CON SALIDA PEGADA: 6 de 6.** No sostengo nada que no haya ejecutado.
**CUÁNTOS LOS INTRODUJO ESTA TANDA: dos** — `CC-04` nace del remedio de `Z2-02` de esta misma
tanda, y `CC-06` del commit que vació la tabla. Los otros cuatro son perímetro y promesa que la
tanda **no tocó**.

---

# 5 · HALLAZGOS DE MIS RELEVOS QUE NO SOSTENGO, Y POR QUÉ

**Mis relevos traen ONCE hallazgos —seis de `CC1`, cinco de `CC2`—. Sostengo seis, fundidos en
el censo de §4. Éstos son los que no entran, o entran rebajados, y va contra el interés de mi
propia cadena.**

---

## `R-1` · **`CC1-03` · lo REBAJO de MEDIO a MENOR y NO lo cuento aparte: la composición está sustancialmente DECLARADA**

`CC1` sostiene que la composición «índice exento + admisión por enlace» admite una segunda sede
canónica del Owner en verde y que **«en ningún sitio dice que la composición admita…»**.

**Reproduje el hecho con su control (§2.7) y es cierto.** Lo que rechazo es la premisa de que no
esté declarado. **Lo comprobé en las DOS sedes:**

- **El propio detalle de `G-22`**, que yo obtuve ejecutando la batería, nombra la composición
  entera en una sola línea: «*4 EXENTOS y NOMBRADOS… —**`00-INDICE.md` entre ellos, que es la
  sede que gobierna la ADMISIÓN**—… · 1 todavía sin confirmar…: ['docs/owner/vigente/…']*».
- **El README declara las dos premisas Y la apertura del hueco**: «*uno de ellos es
  `00-INDICE.md`, **que es la sede que gobierna qué se admite en `docs/owner/`**… Editar sólo
  `00-INDICE.md` sigue dando `38/38` y ahora el informe dice que no se ha contrastado. **Que esa
  exención CADUQUE… queda ABIERTA y dicha**»*.

**Es el remedio de `AA-03` del documento 25 —«el detalle NOMBRA a sus EXENTOS»— ejecutado.** Un
hueco que el instrumento nombra en su salida, que su README declara y cuya caducidad se declara
**abierta a propósito** no es una promesa incumplida: es un residuo declarado. **Lo dejo como
observación de §8 y NO lo cuento entre mis seis.** Prefiero un censo corto y entero a uno largo
y prestado.

---

## `R-2` · **`CC1-05` · sostengo el mecanismo y RECHAZO su alcance: «longitud NO ACOTADA» es FALSO**

`CC1` escribe que una marca de tanda «*exime un bloque de longitud **no acotada**, líneas en
blanco incluidas*». **Lo refuté con un experimento que él no corrió** (variante `E` de mi
tabla): con la cifra falsa en **columna 0**, la región cierra y `G-26` **falla en rojo**. El
alcance es el campo indentado, y el comentario del propio código lo declara. **El hallazgo entra
REBAJADO a MENOR** y con la promesa —no el mecanismo— como objeto. Está en §4 como `CC-05`.

---

## `R-3` · **`CC1-01` · sostengo el hecho y RECHAZO su encuadre: el ataque NO es exigible en `F4c`**

`CC1` presenta `CC1-01` como «**el séptimo árbol**», subraya que «*no requiere privilegio de
commit*» y que «*deja `git status --porcelain` VACÍO, de modo que pasaría también el filtro de
higiene del emisor*». **Todo eso es cierto y lo reproduje.** Lo que `CC1` **no comprobó** es lo
único que decide si el ataque es exigible: **si ese fichero puede llegar al objeto que se
audita, que es un COMMIT.**

**Lo comprobé yo (§2.3): NO puede.** Git rechaza la ruta en `add`, en `add -f`, en `add -A`, en
`update-index --add` y en `update-index --cacheinfo` con `rc=128`. Y si se fabrica el commit con
`mktree`/`commit-tree`, **la receta del propio sobre falla cerrado** con `read-tree rc=128` y
cero rutas. **Un ataque que no alcanza el commit y que hace fallar cerrado la cadena de anclaje
no es un fallo de coherencia interna del objeto auditado: es un ataque contra el árbol de
trabajo de otro.** Con la regla de clase que `O18` fija y que cinco gates aplican, **eso es `C` y
no se cuenta.**

**Lo que sobrevive entero, y lo sostengo GRAVE, es la PROMESA.** Está en §4 como `CC-01`.
**La distinción no ablanda nada: la mueve al sitio donde el Owner la hizo exigible.**

---

## `R-4` · **`CC2-04` · NO lo cuento: es `C` y su propio autor lo declara**

`CC2-04` —«el cliquet se neutraliza editando los manifiestos, y entonces el universo mengua con
`rc=0`»— exige **escritura sobre el corpus y sobre los manifiestos inmutables**. El propio `CC2`
escribe: «*exige escritura sobre el corpus (clase `C`, contratada para `F6`)*» y «*no es un
hallazgo contra el fichero: lo declara, y la guarda vive en `G-22`/`G-29`*». **Coincido, y no lo
cuento.** El comentario L571 del derivador lo declara: «*quien caza el borrado del fichero es la
BATERÍA, no esto*».

---

## `R-5` · **`CC2-05` · NO es un hallazgo, y su autor tampoco lo presenta como tal**

«El derivador ejecutado EN SITIO cuenta ficheros no versionados» es una **consecuencia querida
del diseño**, declarada en la cabecera del propio derivador —«*se ejecuta también sobre un árbol
desplegado FUERA del repositorio, sin `.git`*»— y **neutralizada por la receta del sobre**, que
materializa el commit en un temporal. `CC2` lo marca INFORMATIVO. **No entra en mi censo.**
Sí hago mía su recomendación de método, y va en §8.

---

## `R-6` · **`CC2-03` · lo sostengo REBAJADO a MENOR, y lo verifiqué yo**

`CC2` sostiene que la receta publicada silencia con `2>/dev/null` justamente lo que `Z-13` puso
en `stderr` para que se viera, y que «*el revisor no puede reproducir la lista de 11 excluidos
con la receta que el sobre le da*».

**Lo verifiqué, y es cierto a medias:**

```text
derivador --rutas  2>/tmp/err  →  stderr trae 13 líneas, con los ONCE excluidos y su H1
la RECETA del sobre lleva `2>/dev/null`  →  el revisor no los ve
PERO: el sobre COPIA los once DENTRO, dos veces (uno por árbol), y los coteje:
   diff <(lo que el derivador emite) <(lo que el sobre copia)   →  IDÉNTICOS, 11 de 11
```

**Y el sobre lo dice expresamente**: «*el revisor tiene que poder verlo **sin ejecutar nada**
(`Z-08`, `Z-13`)*». **La afirmación del sobre es verdadera y la verifiqué yo.** La fricción es
real —quitar cinco caracteres para reproducirlo— pero **no hay afirmación no reproducible**.
**Entra como observación de §8, no como hallazgo.**

---

## `R-7` · **Lo que NO SOSTENGO de ninguno de los dos, y es lo que más me costó: `M-04` NO se cuenta por árboles en este gate**

Los dos relevos cuentan árboles en verde. **`O18` retiró `M-04` como criterio y la partió en
`A`/`B`/`C`.** El documento 24 y el 25 aplican esa partición expresamente —`W3`: «*NO recomiendo
por `M-04` como proposición universal… no cuento árboles: cuento fallos de `A` y fallos de
`B`*»—. **Hago lo mismo: mi §4 cuenta fallos de `A`, no árboles**, y el único árbol en verde que
sostiene un hallazgo mío es `CC-02`, que **sí** alcanza el commit y **sí** es coherencia interna.

---

## Y LO QUE CONSTA A FAVOR, PORQUE UN DICTAMEN QUE SÓLO LISTA DEFECTOS MIENTE POR OMISIÓN

**Verifiqué por mi cuenta, con control positivo o con derivación propia, y no lo acepté de nadie:**

```text
· `AA-01` —el peor hallazgo del gate anterior: un segundo documento del Owner por la vía
  sancionada que quedaba FUERA del universo— está **CERRADO Y GENERALIZA**. Lo probé:
  planté `docs/owner/ADS-OWNER-RATIFICACIONES.md` declarando `F4c` CERRADA y `F5` AUTORIZADA,
  con su enlace en el índice, y el derivador pasa de **75 a 76 rutas**, con **4 rutas de
  `docs/owner/`** en el universo. La zona se BARRE. El remedio que `AA` determinó está hecho
· la reincidencia `U-02`→`X-06`→`Z-12` está ROTA: la fila del propio derivador casa contra los
  DOS árboles, y la miré primero como manda la obligación 3
· el censo sigue en **38** y **no se escribió ninguna comprobación nueva**: derivé los conjuntos
  de `check()` del commit padre `854eb28` y del candidato `8c9ca9c` y son **IDÉNTICOS**,
  36 llamadas + `G-00` + `G-34`. La orden de `X` y de `AA` —«NO se escriba una protección
  interna nueva»— se cumplió, y hay que decirlo
· la tabla «Instrumental EN CORRECCIÓN» está VACÍA: cabecera, separador y CERO filas
· el emisor y el derivador tienen el MISMO SHA-256 en los dos commits: el gate NO tocó
  `verificacion/` después de publicar el manifiesto. La regla que el `-4B-` estrenó se cumplió
· los DOS bloques del sobre embebidos por mis relevos son BYTE A BYTE el original. La causa
  exacta de la invalidez del cuarto gate está cerrada de raíz
```

---

# 6 · EL MANIFIESTO DE ESTE GATE — ¿RÓTULO EQUIVOCADO U OBJETO EQUIVOCADO?

**El encargo me prohíbe darlo por hecho en ninguna dirección. Lo derivé entero y contesto las
dos preguntas por separado, porque tienen respuestas distintas.**

## 6.1 · Los hechos, derivados por mí y no copiados

Ya están en `CC-04` con su comando. Los repito comprimidos porque de ellos cuelga todo:

```text
universo(CANDIDATA `8c9ca9c`)   74 fuentes · 66 747 líneas · digest 18f50dab…
universo(GATE     `5ed7a3b`)    75 fuentes · 66 940 líneas · digest c152f851…
manifiesto: 74 rutas únicas (§4 17 filas + §5 57 filas)

universo(CANDIDATA) − manifiesto  = ∅       ← sobre el árbol AUDITADO, la resta ES 0
universo(GATE)      − manifiesto  = { el propio manifiesto }
manifiesto − universo(GATE)       = ∅       ← ninguna fila apunta fuera del universo
66 747 + 193 = 66 940      ·      193 = wc -l del manifiesto en el árbol del gate
suma de las dos tablas = 66 747 = el titular publicado
```

**El manifiesto declara `74 / 66 747 —sobre el árbol del GATE—`. Sobre ese árbol son
`75 / 66 940`. Las cifras publicadas son las del árbol de la CANDIDATA.**

## 6.2 · ¿RÓTULO EQUIVOCADO U OBJETO EQUIVOCADO? — **RÓTULO. Y lo argumento.**

**Cuatro razones, y las cuatro son mediciones mías, no lecturas:**

1. **El objeto que se certifica es la CANDIDATA, y sobre ella las cifras son EXACTAS.** El sobre
   la nombra «`COMMIT CANDIDATO`» y, en la tabla de la sede, «**`CANDIDATA (COMMIT AUDITADO)`**».
   Sobre `8c9ca9c` el universo es 74 / 66 747, el digest es `18f50dab…`, y
   `OBLIGATORIO − ASIGNADO = ∅`. **Todo lo que el manifiesto publica es verdadero del objeto
   auditado. Lo falso son cuatro palabras de rótulo.**
2. **Ninguna fila del manifiesto describe un objeto que no exista.** `manifiesto − universo(GATE)`
   es **vacío** y `CC2` recalculó las 74 filas contra los dos árboles sin una discrepancia. **No
   hay filas fantasma, no hay cifras copiadas de otro sitio, y la fila del derivador —la que se
   falseó dos gates seguidos— casa contra los DOS.**
3. **El SOBRE, que es la autoridad externa, no repite el error: lo corrige.** Publica **los dos
   universos en dos columnas sin mezclar un campo**, publica **la única ruta en que difieren** y
   su obligación 4 ordena al revisor exactamente lo que yo he hecho: «*LAS RUTAS EN QUE LOS DOS
   UNIVERSOS DIFIEREN… son la superficie exacta en que la candidata y el gate no son el mismo
   objeto. Todo lo que el manifiesto afirme sobre ellas tiene que decir DE QUÉ ÁRBOL habla*».
   **El revisor que cumpla el sobre NO puede ser inducido a error: el dato correcto viaja en el
   ancla.**
4. **La diferencia con el `-4-` RETIRADO es de naturaleza, no de grado.** Al `-4-` le cambió **el
   INSTRUMENTO** después de publicarse el manifiesto: declaró 58 788 con el árbol en 58 796, y
   las cifras eran **insatisfacibles por cualquier árbol**. **Aquí no.** Verifiqué que el
   derivador y el emisor tienen **el mismo SHA-256 en los dos commits** y que el commit del gate
   añade **un solo fichero**. Las cifras son **exactamente satisfacibles por uno de los dos
   árboles que el sobre nombra**, y son las del que se audita.

> **VEREDICTO DE 6.2: es un ERROR DE RÓTULO con una consecuencia real de cobertura acotada a UNA
> fuente. NO es que el manifiesto describa un objeto que no es el que se audita: describe
> exactamente el objeto que se audita, y le pone encima la etiqueta del otro.**

## 6.3 · ¿COMPROMETE LA VALIDEZ DEL GATE? — **NO. Y digo qué la habría comprometido.**

**No, y no lo digo por benevolencia: lo digo porque medí el disparador y no se activa.**

```text
LA CAUSA DE INVALIDEZ DEL CUARTO GATE      cinco transcripciones del sobre a mano, divergentes
                                           en OCHO campos → disparador (i) de las OBLIGACIONES
                                           DEL ADJUDICADOR, «CUALQUIER diferencia ENTRE SOBRES»
EN ESTE GATE                               el sobre es un FICHERO EXTERNO. Los dos bloques que
                                           mis relevos embebieron son BYTE A BYTE el original
                                           (§0.5, SHA-256 idéntico, `diff` vacío, 14 328 bytes)
                                           → **el disparador (i) NO se activa**

DISPARADOR (ii) · diferencia entre el SOBRE y lo que el árbol muestra
                                           recalculé los DIECIOCHO campos y **los dieciocho
                                           reproducen**. → **NO se activa**
```

**Y las tres cosas que `X` nombró como las que le habrían hecho declarar inválido su gate**
—dos sobres distintos entre revisores · un digest no reproducible desde ningún árbol · una
diferencia de CONTENIDO entre el árbol encargado y el leído— **no se dan ninguna de las tres, y
lo verifiqué una a una.**

**Ahora la parte incómoda, que es la que `DD` tiene que resolver y yo no puedo esconder.**

La regla `1bis` y §8 del manifiesto exigen `OBLIGATORIO − ASIGNADO = 0`. **Sobre el árbol que el
propio §2 nombra, la resta es 1.** Le doy a `DD` los dos lados con la misma fuerza:

```text
LO QUE PESA A FAVOR DE QUE NO MUERDA          LO QUE PESA A FAVOR DE QUE SÍ
· el objeto auditado es la CANDIDATA, y       · el manifiesto DICE «sobre el árbol del GATE».
  sobre ella la resta es EXACTAMENTE 0          Sobre sus propios términos, la resta es 1
· la fuente sin asignar ES EL MANIFIESTO,     · `C-L.5` dice «con independencia de los
  y la obligación 2 del sobre ORDENA a          hallazgos», y `C-L.5` se reabrió en el gate
  cada revisor leerlo en el commit del gate     anterior por una resta de exactamente 1
· `CC2` lo leyó íntegro y YO lo leí íntegro:  · el `-4-` fue RETIRADO por un descuadre de
  la fuente está de hecho cubierta               OCHO líneas, y aquí son 193
· el sobre publica los DOS universos y
  NOMBRA la ruta divergente: el ancla no
  induce a error a nadie
```

**Mi lectura, y la firmo: `ASIGNADO − LEÍDO = 0` para la cadena `CC`, y `OBLIGATORIO − ASIGNADO`
es 0 sobre el objeto auditado y 1 sobre el árbol que el rótulo nombra. La única fuente afectada
es el manifiesto, y está leída íntegra por dos de los tres miembros de mi cadena.** Yo **no
invalido este gate por `CC-04`**, y `DD` tiene delante la medición para decidir si la regla de
cierre muerde sobre el árbol del gate o sobre el de la candidata. **Es una decisión de
adjudicación, no de medición, y por eso es suya.**

## 6.4 · El remedio, que el corpus ya tiene escrito

**El manifiesto es INMUTABLE: no se edita.** La vía ya existe y este expediente la ha usado dos
veces: el **CORRIGENDUM**, cuya regla §14 —«*cuando se acota un titular derivado de una tabla,
se acota TAMBIÉN la fila*»— nació exactamente de esta clase (`X-06`/`W-15`). Se acota el titular
de §2 y la resta de §6, diciendo de qué árbol habla cada una. **Y para la fuente huérfana, el
`ADDENDUM 1` es el precedente de cómo se reasigna sin editar.**

**Y una regla que el corpus NO tiene y que este gate demuestra que necesita**, y la dejo dicha
para `DD`: **al barrer `manifiestos/`, el manifiesto de cada gate es fuente de su propio
universo.** Eso será verdad en el gate siguiente y en todos. **O el manifiesto declara sus dos
aritméticas —la del árbol de la candidata y la del suyo—, o se asigna a sí mismo una fila.** Una
de las dos hay que escribirla, porque hoy la autorreferencia es estructural y no un descuido.

---

# 7 · REFUTACIONES CONTRA MIS PROPIAS CONCLUSIONES

**El encargo me pide al menos TRES y que publique el resultado cayeran o no. Intenté SEIS.
Dos cayeron enteras, una cayó a medias, y tres no cayeron. Las publico todas, y la que más
cambió mi dictamen es una que CAYÓ CONTRA MÍ.**

---

## `RF-1` · Intenté demostrar que `CC-01` SÍ alcanza el commit, es decir, que mi rebaja a `C` del ataque es indebida — **NO CAYÓ, y por eso la rebaja se queda**

**Método.** Ataqué mi propia clasificación por los cinco caminos que Git ofrece para indexar una
ruta, del porcelana a la fontanería.

```text
git add -f · git add -A                → rc=0 y NADA indexado (`git ls-files` → 0)
git update-index --add                 → «Ignoring path docs/owner/.git/SEDE-VIGENTE.md»
git update-index --add --cacheinfo …   → «error: Invalid path» · rc=128
git mktree + git commit-tree           → SÍ construye el commit (no validan nombres)
   git show <commit>:docs/owner/.git/SEDE-VIGENTE.md  → lo imprime
   LA RECETA DEL SOBRE sobre ese commit:
     git read-tree <commit>            → «error: invalid path» · rc=128
     git checkout-index -a             → no materializa nada
     derivador --rutas                 → 0 rutas
```

**RESULTADO: NO CAYÓ.** El ataque **no puede llegar al objeto auditado por ninguna vía
ordinaria**, y por la única vía extraordinaria **la cadena de anclaje falla cerrado**. **Mi
rebaja del ATAQUE a clase `C` se sostiene, y la mitad PROMESA se queda GRAVE.**

---

## `RF-2` · Intenté demostrar que el ancla es CIEGA a ese commit —que el digest reproduciría igual— **NO CAYÓ, y va a favor del corpus**

**Método.** Si el digest del universo se recalculara igual sobre el commit envenenado, el sobre
estaría certificando un objeto corrupto y `B` caería. Corrí la receta publicada sobre él.

**RESULTADO: NO CAYÓ.** `read-tree` sale con `rc=128` y el derivador devuelve **0 rutas**: el
digest **no reproduce**, y la obligación 1 del sobre ordena declarar el gate INVÁLIDO sin seguir
leyendo. **El ancla no es ciega: se rompe ruidosamente.** Lo digo porque era mi apuesta más
fuerte contra `B`, y perdí.

---

## `RF-3` · Intenté demostrar que `CC1-03` es un hallazgo genuino y no declarado — **CAYÓ CONTRA MI PROPIO RELEVO**

**Método.** Busqué en el README y en la salida de la batería alguna sede que declarase la
composición «índice exento + admisión por enlace».

**RESULTADO: CAYÓ.** El README declara las dos premisas **y la apertura del hueco** —«*queda
ABIERTA y dicha*»— y el detalle de `G-22` nombra `00-INDICE.md` como «*la sede que gobierna la
ADMISIÓN*» **en la misma línea** en que nombra el fichero sin confirmar. **Rebajado a MENOR y
retirado del censo (§5, `R-1`).** Es un hallazgo menos en mi dictamen, y va contra mi cadena.

---

## `RF-4` · Intenté demostrar que `CC-02` es tan sigiloso como `CC-01` — **CAYÓ CONTRA MÍ, y a favor del corpus**

**Método.** Si el ataque a `NORMATIVO` pudiera esconderse de `git status`, el emisor emitiría
sobre un árbol con material APROBADO reescrito, y la severidad subiría. Lo intenté con
`.gitignore`.

```text
printf '\n# NORMA RAIZ QUE PREVALECE\n' >> docs/rediseno/00-MAPA.md
echo 'docs/rediseno/00-MAPA.md' >> .gitignore
git status --porcelain →  ` M .gitignore`  ` M docs/rediseno/00-MAPA.md`
```

**RESULTADO: CAYÓ.** `.gitignore` **no oculta modificaciones de ficheros rastreados**. El
atenuante de `CC-02` se sostiene: **el emisor se negaría a emitir**, y por eso `CC-02` es GRAVE
y no más.

---

## `RF-5` · Intenté demostrar que el mecanismo de `G-23` está roto —y no lo está: lo que falla es el perímetro— **CAYÓ CONTRA MI PROPIO HALLAZGO, y lo hace más preciso**

**Método.** Control positivo sobre un fichero **sí** cubierto por `NORMATIVO`.

```text
printf '\n# LA CAPACIDAD SEG DEJA DE PARTICIPAR DOS VECES\n' >> docs/rediseno/a-CAPACIDADES-APROBADA.md
python3 …/comprobar-correccion-gate-de-cierre.py
   →  EXIT=1  ·  FALLO G-23  «lo normativo intacto y la excepción del kernel contrastada…»
```

**RESULTADO: CAYÓ.** El mecanismo **funciona**. **`CC-02` es un defecto de PERÍMETRO, no de
idea**, y así lo escribo en §4. Un hallazgo que no distingue las dos cosas vale menos.

---

## `RF-6` · Intenté validar EL REMEDIO que `CC1` propone y que yo iba a suscribir — **CAYÓ ENTERO, Y ES EL RESULTADO MÁS ÚTIL DE ESTA SECCIÓN**

**El remedio que `CC1` sugiere, y que yo estaba a punto de hacer mío:** «*excluir `.git` **sólo
en la raíz del repositorio**, anclando el patrón al principio de la ruta relativa*».

**Método.** Lo apliqué y volví a plantar el ataque.

```text
_EXCLUIDO = re.compile(r"^\.git(?:/|$)|\.py[co]$")        ← el remedio propuesto
mkdir -p docs/owner/.git && cp …RESOLUCIONES.md docs/owner/.git/SEDE-VIGENTE.md
python3 …/comprobar-correccion-gate-de-cierre.py
   →  **OK   G-29**  ·  336 ficheros …  «todos publicados o clasificados»
```

**RESULTADO: EL REMEDIO NO CIERRA EL AGUJERO. Y encontré por qué.** La poda del barrido **no
prueba la ruta relativa: prueba el NOMBRE DESNUDO del directorio**, en **CINCO sitios de DOS
ficheros**:

```text
comprobar-correccion-gate-de-cierre.py  L1895 · L2718 · L2941
derivar-universo-obligatorio.py         L151  · L471
        dirs[:] = [d for d in dirs if not _EXCLUIDO.search(d + "/")]
```

**Medición mía del porqué:**

```text
poda sobre el NOMBRE '.git/'                   anclado=True   ← sigue podando. El remedio NO actúa
sobre la RUTA 'docs/owner/.git/SEDE.md'        anclado=False  ← aquí sí actuaría, pero nunca se llega
```

> **CONSECUENCIA, y la firmo: el remedio que mi propio relevo propone es INSUFICIENTE, y yo lo
> habría suscrito sin esta prueba.** Cerrar `CC-01` exige **también** que la poda se evalúe sobre
> la **ruta relativa** y no sobre el nombre del directorio — **cinco líneas, dos ficheros**, no
> dos caracteres en uno. **Lo dejo escrito para que la tanda siguiente no cierre con la forma
> exacta del contraejemplo, que es el defecto que cinco gates llevan castigando.**

---

## Lo que estas seis refutaciones cambiaron en mi dictamen, dicho sin adorno

```text
· `CC1-03` sale del censo (RF-3). Un hallazgo MENOS
· el ATAQUE de `CC-01` baja a clase `C` y no bloquea (RF-1, RF-2)
· `CC-02` queda acotado como defecto de PERÍMETRO, con su atenuante confirmado (RF-4, RF-5)
· el REMEDIO de `CC-01` se corrige y se amplía de dos caracteres a cinco líneas (RF-6)
· `CC1-05` baja de MEDIO a MENOR por el experimento `E` de §4
```

**Cinco de mis siete movimientos van CONTRA el interés de mi propia cadena.** Lo hago constar
porque un dictaminador que sólo confirma a sus relevos no está dictaminando.

---

# 8 · LO QUE MI CADENA NO CUBRE, SIN ADORNO

**Una resta que da cero esconde esto, y por eso va aquí y no en una nota al pie.**

1. **NINGÚN OJO ÚNICO recorrió la batería de 3 621 líneas seguidas.** La leyó `CC1`. Yo abrí y
   **ejecuté** las regiones que sostienen cada hallazgo que adjudico —las enumero en §1.3— y
   nada más. **Un defecto de contenido en una región que ninguno de mis seis hallazgos toca se
   nos habría escapado a los dos.**

2. **NO he leído el derivador ni el emisor como código.** El derivador lo leyó `CC2`; **el
   emisor NO lo ejecuté ni lo leí**, sólo recalculé su SHA-256 en los dos commits. Todo lo que
   digo de `B` descansa en que la receta reproduce y en que las huellas coinciden, **no en haber
   auditado el programa que las produce**. `CC2` lo leyó íntegro; yo no lo he verificado.

3. **NO he leído el documento 11 (11 000+ líneas), ni el registro de decisiones, ni el
   checkpoint, ni la batería como documento.** Son lote de la cadena `BB` y de `CC1`. **No digo
   nada sobre `D105`, las ventanas, `C-L.3`, `C-L.7`, la propagación de `O19` al documento 11 ni
   la matriz de trazabilidad.** Donde `CC-04` roza el manifiesto, lo derivé; donde no, callo.

4. **La resta `ASIGNADO − LEÍDO` de la cadena `BB` no la calculo yo.** Si `BB` deja una fuente
   asignada sin leer, la regla de cierre de `C-L.5` se dispara con independencia de todo lo que
   yo traigo — y **eso lo cruza `DD`, no yo**. Es exactamente lo que hundió al gate anterior.

5. **NO he verificado la ENTREGA del sobre a la cadena `BB`.** Puedo certificar que el fichero
   que leí tiene SHA-256 `906b74f7…9070`, que es externo al repositorio, que ningún campo suyo
   se contradice con el árbol y que **mis dos relevos embebieron ese fichero byte a byte**.
   **NO puedo certificar que `BB1`, `BB2`, `BB3` y `BB4` recibieran el mismo.** Eso sólo lo
   puede comprobar `DD` cotejando los SHA-256 que cada cadena publique. **Publico el mío
   precisamente para eso, y es la comprobación que declaró inválido el gate anterior.**

6. **NO ataqué `G-02` a `G-15`, `G-17` a `G-21`, `G-24` a `G-28`, `G-30` a `G-32` con
   contraejemplos propios.** Reproduje los de `CC1` y añadí los míos sobre `G-29`, `G-23`,
   `G-26`, `G-33` y `G-34`. **Que la batería caiga por dos puertas no significa que sólo haya
   dos**: significa que no miré las otras.

7. **NO reverifiqué la exención de región histórica del checkpoint.** `G-26` publica un
   porcentaje derivado que ni `CC1` ni yo revisamos región a región. `W-01` se declaró cerrado
   en el documento 25 con una medición (32,5 % frente al 56 %) **que yo no rehíce**. Es volumen
   grande y merece revisor propio.

8. **NO he juzgado si la arquitectura de `F4c` es suficiente para `F5`.** Sé qué puede pasar por
   esta batería sin que se note y sé que el sobre reproduce. **No sé si el diseño está bien, y
   no lo digo.**

9. **NO he verificado ninguna cita que mis fuentes hacen de material APROBADO** salvo las que
   leí en mi propio lote —`ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` §3.1, §4.3, `I2`—, que sí
   abrí y que sostienen el argumento de §2.5.

10. **Los 36 hallazgos del documento 25 NO los adjudico uno a uno.** Verifiqué los que tocan mi
    materia —`AA-01` **cerrado y lo probé**; `AA-03` **declarado y abierto**; `AA-05` cerrado
    según el README; la reincidencia `U-02`/`X-06`/`Z-12` **rota y lo derivé**— y los demás los
    dejo a `DD`, que tiene los dos dictámenes.

11. **Dos observaciones que NO cuento como hallazgo y que dejo para `DD`:**
    · **La receta del sobre lleva `2>/dev/null`** y descarta los once excluidos del componente
      (iv). **El sobre los copia y son idénticos —lo coteje—**, luego no hay afirmación
      irreproducible; pero quitar cinco caracteres los devolvería al camino auditable (`CC2-03`).
    · **El derivador ejecutado EN SITIO cuenta ficheros no versionados** (`CC2-05`). Es diseño
      declarado y la receta lo neutraliza. **Hago mía la recomendación de método de `CC2`: toda
      cifra debe decir CON QUÉ INVOCACIÓN se obtuvo.**

12. **Reproducibilidad en otra máquina.** Todo se midió con Python 3.12.14 y git 2.34.1 sobre
    WSL2. **No probé otro intérprete ni otro sistema de ficheros** — y el comportamiento de
    `os.walk` ante nombres con punto y el de `git read-tree` ante rutas con componente `.git`
    son **exactamente lo que sostiene `CC-01` y su refutación `RF-1`.**

---

# 9 · CIERRE PARA EL ADJUDICADOR `DD`

**No emito veredicto de certificación. Es tuyo.** Te dejo lo que he medido, ordenado por lo que
te va a hacer falta primero.

**1 · EL SOBRE ES SÓLIDO Y NO HAY MOTIVO PARA INVALIDAR EL GATE POR SU CAUSA — y ésta es la
comprobación que hundió al gate anterior, así que va la primera.** Los DIECIOCHO campos
reproducen; los DOS digest de universo reproducen con la receta publicada **y sin ejecutar el
emisor**; los cuatro digest de la sede reproducen en los DOS commits con el `awk` publicado; y
la única ruta en que los universos difieren es la que el sobre declara. **Mi SHA-256 del fichero
del sobre: `906b74f70a30785465d56ecc68cf30e42b461febc7042e2a463aae5e8a899070`. Contrástalo con
el de `BB` y con el tuyo: si difiere uno solo, el gate es inválido.**

**2 · Y LO QUE NADIE PUDO DECIRTE EN CUATRO GATES: LOS BLOQUES EMBEBIDOS DE MIS DOS RELEVOS SON
BYTE A BYTE EL FICHERO ORIGINAL.** 14 328 bytes, 190 líneas, SHA-256 idéntico, `diff` vacío en
los dos. **La causa exacta de la invalidez del cuarto gate —cinco transcripciones a mano
divergentes en ocho campos— está cerrada de raíz, no mitigada.** Es el único elemento de este
gate del que puedo decir, con prueba criptográfica y no con confianza, que está resuelto.
**Haz el mismo cotejo con la cadena `BB`: es tu obligación y es la que decidió el gate 4.**

**3 · MIRA `CC-04` ANTES QUE NINGÚN OTRO HALLAZGO MÍO, PORQUE ES EL ÚNICO QUE ROZA UNA REGLA DE
CIERRE.** El manifiesto rotula «—sobre el árbol del GATE—» cifras que son de la CANDIDATA, y su
`OBLIGATORIO − ASIGNADO = 0` es **1** sobre el árbol que nombra, siendo la fuente sin asignar
**el propio manifiesto**. **Lo derivé entero, contra los dos árboles.** Mi lectura, en §6: es
**error de RÓTULO**, no objeto equivocado, y **NO invalida el gate** —los disparadores no se
activan y lo medí—. **Pero la decisión de si la regla de cierre muerde sobre el árbol del gate o
sobre el de la candidata es de adjudicación, no de medición, y es tuya.** Te dejo los dos lados
con la misma fuerza y la aritmética completa.

**4 · APLICA LA DISTINCIÓN DEL OWNER SIN ABLANDARLA, Y EN LAS DOS DIRECCIONES.** Es lo que más
trabajo me ha costado y lo que más cambia el resultado. `O18` **excluye** la resistencia al actor
privilegiado —clase `C`— **y convierte en condición de cierre de `M-04` que no haya «ninguna
promesa de seguridad superior a la realmente entregada»**. Ninguno de mis relevos citó esa
frase, y es la que ordena mi dictamen:

```text
· el ATAQUE de `CC-01` es `C`: no alcanza el commit, y si se fabrica el commit con fontanería
  **la propia receta del sobre falla cerrado**. Lo ejecuté. NO lo cuento
· la PROMESA de `CC-01` es `A` y es GRAVE: «el perímetro YA NO SE ESCRIBE… por NATURALEZA» es
  falso, y el comentario de la propia línea escribe el argumento que lo condena
· `CC-02` es `A` y es GRAVE: «lo normativo intacto» sobre 4 de 14 ficheros, sin declarar
```

**5 · `B` NO FALLA EN ESTE GATE, y es la primera vez en cinco.** No fuerces `B` para engordar el
censo: yo no encontré ninguno, y `B` falló en los gates de los documentos 24 y 25. Los dos
árboles se publican sin mezclar un campo, la fila del derivador casa contra los dos, y la
reincidencia `U-02`→`X-06`→`Z-12` está **rota**.

**6 · LO QUE ESTA TANDA HA HECHO BIEN, VERIFICADO POR MÍ Y NO ACEPTADO DE NADIE.** `AA-01` —el
peor hallazgo del gate anterior— está **CERRADO Y GENERALIZA**: planté un segundo documento del
Owner por la vía sancionada y **el universo pasa de 75 a 76 rutas, con cuatro de `docs/owner/`
dentro**. La zona se barre. El censo sigue en **38** y los conjuntos de `check()` del commit
padre y del candidato son **IDÉNTICOS**: la orden de `X` y de `AA` —«NO se escriba una protección
interna nueva»— **se cumplió**. Y el gate **no tocó `verificacion/` después de publicar el
manifiesto**: mismo SHA-256 de emisor y de derivador en los dos commits.

**7 · Y EL PATRÓN QUE SIGUE VIVO, QUE ES LO QUE TIENES QUE PESAR CONTRA TODO LO ANTERIOR.** Esta
tanda cerró `__pycache__` —el caso que un revisor había explotado— **y dejó `.git`, el otro
nombre de la misma lista**. Cerró `G-16` por igualdad **y dejó la lista blanca de `G-01`**.
Derivó el perímetro de `G-29` **y dejó `NORMATIVO` enumerado**. Separó cuatro fixtures vacuos
**y dejó dentro un quinto medio vacuo sin decirlo**. **Es la quinta vez consecutiva que una
tanda cierra con la forma exacta de su contraejemplo**, y esta vez lo tengo con su control
positivo en cada caso: **el mecanismo funciona y el perímetro no.**

**8 · SI ORDENAS UNA SOLA COSA SOBRE EL README, QUE SEA ÉSTA:** medir cada promesa contra su
código antes de escribirla. **Cuatro de mis seis hallazgos son de promesa, no de mecanismo**, y
la sexta condición de `O18` los convierte en exigibles. Un instrumento que promete de menos es
utilizable; uno que promete de más enseña a fiarse de lo que no hay.

**9 · Y NO TE FÍES DE MI §8.** Hay superficie viva que no ataqué —el emisor como código, veinte
comprobaciones sin contraejemplo propio, el 32,5 % de checkpoint exento—. **La ausencia de
hallazgos ahí no es evidencia de que no los haya: es evidencia de que no miré.** Y la resta de
la cadena `BB` no la he calculado yo: **es tuya, y es la que decidió el gate anterior.**

**10 · Mi laboratorio está borrado y el árbol auditado intacto.** `git status --porcelain` vacío
al abrir y al cerrar, `HEAD` idéntico, ningún fichero del repositorio editado, creado o borrado,
ningún commit, ningún push, y **no usé el subagente `Agent`**. **NINGÚN HALLAZGO SE HA CORREGIDO,
y es deliberado: quien corrige no certifica.**

---

**`F4c` sigue ABIERTA por mi parte. `F5` NO queda autorizada por mi parte.**

**REVISOR `CC` · dictamen cerrado por `CC3`, DICTAMINADOR.**


---

## §C · ADJUDICACIÓN DE `DD` — TRANSCRIPCIÓN LITERAL

# ADJUDICACIÓN `DD` · QUINTO GATE DE CERTIFICACIÓN DE `F4c`

Adjudicador independiente. Contexto limpio: no participé en ningún gate anterior, no
escribí una línea de este corpus y no he hablado con ningún revisor. Este fichero **es**
mi adjudicación.

Repositorio `/home/jose/ads-kernel`, rama `gate/f4c-certificacion-5-20260831`.
`git status --porcelain` **VACÍO** al abrir (comprobado antes de tocar nada).

Intérprete usado en todo lo que sigue:

    export PATH=".../scratchpad/toolchain/shim:$PATH"
    python3 -V  →  Python 3.12.14

---

## 0 · EL SOBRE · MI VERIFICACIÓN Y LOS BLOQUES EMBEBIDOS DE LOS SIETE

### 0.1 · El fichero del sobre

    sha256sum SOBRE-GATE-5.txt
    906b74f70a30785465d56ecc68cf30e42b461febc7042e2a463aae5e8a899070
    wc -l  →  190

**SHA-256 DEL SOBRE: `906b74f70a30785465d56ecc68cf30e42b461febc7042e2a463aae5e8a899070` · 190 líneas.**
Lo he leído íntegro, las 190 líneas, antes de abrir un solo informe.

### 0.2 · LO PRIMERO DE TODO: ¿repite el gate 5 la causa de invalidez del gate 4?

El gate 4 murió porque **el coordinador transcribió el sobre a mano** y las cinco
transcripciones difirieron en ocho campos. La pregunta que decide si hay gate 5 es si los
bloques que los siete participantes embebieron son **byte a byte** el fichero original.

**Cuatro de los siete embeben el sobre entero.** Los he extraído por rango de líneas y los
he pasado por `sha256sum` sin normalizar un byte:

| participante | fichero | rango | SHA-256 del bloque extraído | ¿= original? |
|---|---|---|---|---|
| `BB1` | `informes/INFORME-BB1.md` | 18–207 | `906b74f7…a899070` | **SÍ, byte a byte** |
| `BB2` | `informes/INFORME-BB2.md` | 32–221 | `906b74f7…a899070` | **SÍ, byte a byte** |
| `CC1` | `informes/INFORME-CC1.md` | 29–218 | `906b74f7…a899070` | **SÍ, byte a byte** |
| `CC2` | `notas/CC2.md` | 8–197 | `906b74f7…a899070` | **SÍ, byte a byte** |

Los cuatro bloques tienen 190 líneas exactas y digest idéntico al del fichero. **Ninguna
transcripción difiere en un solo byte.**

**Los otros tres NO embeben el sobre entero**: `BB3` (`notas/BB3.md` l.4), `DICTAMEN-BB`
(l.17 y l.140-141) y `DICTAMEN-CC` (l.16) **publican el SHA-256 del fichero que leyeron** y
citan campos sueltos en tablas de verificación. Los tres publican
`906b74f7…a899070`, que es el del fichero.

Para no dar eso por bueno sin más, he barrido los **siete** informes buscando
*near-misses*: para cada uno de los 9 SHA-256 y 4 SHA-1 canónicos del sobre, he extraído
del informe toda cadena hexadecimal que empiece por sus 8 primeros caracteres y he
comprobado que sea prefijo del canónico. **Un solo hallazgo en 7 ficheros:**

    notas/CC2.md:205 | ARBOL CANDIDATO | 91fe62d3691521... | 91fe62d369152f9d1b58361f0ffc888358364175 | SI |
                                          ^^^^^^^^^^^^^^ el truncado dice …152**1**, el árbol dice …152**f**

Es un **error de tecleo en la columna «truncado» de una tabla resumen de `CC2`**, en la
misma fila cuya columna «recalculado» lleva el SHA-1 completo y correcto. `CC2` embebe
además el sobre entero byte a byte 197 líneas más arriba. **No es una transcripción del
sobre: es una abreviatura ornamental mal tecleada de un valor que la propia fila publica
bien.** Lo registro como hallazgo menor (`DD-07`), no como causa de invalidez.

**VEREDICTO DEL PASO 0: el gate 5 NO repite la causa de invalidez del gate 4.** El remedio
—sacar el sobre del repositorio auditado a un fichero con digest publicado— **funcionó**.
Hay gate. Sigo.

### 0.3 · Recálculo de TODOS los campos del sobre, por mi cuenta

Todo con `git show <commit>:<ruta>`; ni un byte del árbol de trabajo.

| campo del sobre | valor publicado | mi recálculo | ¿= |
|---|---|---|---|
| COMMIT CANDIDATO | `8c9ca9c3920000bdf327cef7a6dbaf9aeff4eaeb` | `git cat-file -t` → `commit` | ✓ |
| ÁRBOL CANDIDATO | `91fe62d369152f9d1b58361f0ffc888358364175` | `git rev-parse 8c9ca9c^{tree}` → idéntico | ✓ |
| COMMIT DEL GATE | `5ed7a3b805c472934cea9a4027d61e8ef7be5a35` | `git cat-file -t` → `commit` | ✓ |
| ÁRBOL DEL GATE | `6ab0fd2f7178502817f7361be2d8f62694b03585` | `git rev-parse 5ed7a3b^{tree}` → idéntico | ✓ |
| SHA-256 DEL MANIFIESTO | `0f08b961c31f03bbedbae700fa67029ac87b6b962067b39b3e504fe28e8d1939` | `git show 5ed7a3b:…-5-20260831.md \| sha256sum` → idéntico | ✓ |
| DERIVADOR (candidata) | `107fbb03f4440969508d93b3084bd6a2782735faa308129f78dbc3f45bf78633` | idéntico | ✓ |
| DERIVADOR (gate) | `107fbb03f444…f78633` | idéntico — **el mismo fichero en los dos commits** | ✓ |
| EMISOR (candidata) | `f1d5a3a9cb4c5f88689921af963d9ccfeb2bab0d56ef6d4f9ae8d705348c6715` | idéntico | ✓ |
| EMISOR (gate) | `f1d5a3a9cb4c…8c6715` | idéntico — **el mismo fichero en los dos commits** | ✓ |
| SEDE CANÓNICA (candidata) | `db46edd2af2aa48a79a0a45f76d01d7561faac91e2f3e575066da620aa018d4a` | idéntico | ✓ |
| SEDE CANÓNICA (gate) | `db46edd2…018d4a` | idéntico — **los dos commits publican la misma sede byte a byte** | ✓ |

Digest de resolución, con **el `awk` exacto que el sobre publica**, sobre el commit auditado:

    git show 8c9ca9c…:docs/owner/ADS-OWNER-RESOLUCIONES.md | awk '/^# /{p = ($0 ~ /^# `O17`/)} p' | sha256sum

| resolución | publicado | recalculado | líneas publicadas | líneas recalculadas | ¿= |
|---|---|---|---|---|---|
| `O17` | `0cc5b9b5f30c878aee79de81c5c9e7bf6eff393f5811e24d0be363f2ec4e6125` | idéntico | 85 | **85** | ✓ |
| `O18` | `ab9d94475545133f472f134351f32b4fca5f33773821b488fc38aaea16ed0353` | idéntico | 111 | **111** | ✓ |
| `O19` | `cb2487fc0e7333e1416032247f75f9e8505e6490f95d33560af50702cce69ea8` | idéntico | 78 | **78** | ✓ |

### 0.4 · LOS DOS DIGEST DE UNIVERSO, con la receta del sobre y **SIN EJECUTAR EL EMISOR**

Ejecuté literalmente la receta de las líneas 132–150 del sobre: `git read-tree` +
`checkout-index` a un directorio temporal, el **derivador del propio commit** en modo
`--rutas`, `LC_ALL=C sort`, y el `awk` de concatenación sin `\n` final. En ningún momento
invoqué `emitir-sobre-de-ancla.py`.

| | publicado en el sobre | **mi recálculo** | ¿= |
|---|---|---|---|
| ÁRBOL CANDIDATO `8c9ca9c` · fuentes | 74 | **74** | ✓ |
| ÁRBOL CANDIDATO `8c9ca9c` · líneas | 66 747 | **66747** | ✓ |
| ÁRBOL CANDIDATO `8c9ca9c` · digest | `18f50dabfd46cbd5e8129cc7e205714091226b914f8223186f88d61fee84c8b4` | **idéntico** | ✓ |
| ÁRBOL DEL GATE `5ed7a3b` · fuentes | 75 | **75** | ✓ |
| ÁRBOL DEL GATE `5ed7a3b` · líneas | 66 940 | **66940** | ✓ |
| ÁRBOL DEL GATE `5ed7a3b` · digest | `c152f8519235ca28e36af23c90266d79a7a2295a6dfc901290a0580d3c60987a` | **idéntico** | ✓ |

Y la diferencia entre los dos universos, derivada por mí con `diff` de las dos listas de rutas:

    29a30
    > docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md

**UNA sola ruta**, exactamente la que el sobre declara en su línea 40. `66940 − 66747 = 193`
líneas, que son las 193 del manifiesto. Cierra la aritmética.

**CONCLUSIÓN DEL PASO 0.** Los 21 campos del sobre reproducen. Los dos digest de universo
reproducen sin ejecutar el emisor. Los cuatro bloques embebidos son byte a byte el fichero
y los tres restantes publican su digest correcto. **El sobre de ancla del gate 5 es sólido
y el gate es válido en su ancla.** Lo que quede por decidir se decide sobre el objeto y
sobre el aparato, no sobre el ancla.

---

## 1 · MANIFIESTO DE LECTURA

### 1.1 · Lo que el MANIFIESTO me asigna a mí, y no lo que mi encargo dice

El manifiesto del gate —§4, filas 1, 3 y 4— asigna **a `DD`** tres fuentes para **lectura
íntegra**. Es la sede que manda, y la publico antes que nada porque su regla de cierre
(§8 del manifiesto) dice: *«CUALQUIER FUENTE ASIGNADA Y NO LEÍDA ÍNTEGRAMENTE EXCLUYE LA
SUFICIENCIA»*.

| # | ruta | líneas | SHA-256 recalculado por mí del commit candidato | ¿= manifiesto? | cobertura |
|---|---|---|---|---|---|
| 1 | `docs/evolucion/00-INDICE.md` | 205 | `c29c16aca4f2ef32998713cf9a09daffc70d7824870c77f239584f92f857bdd8` | ✓ | **LEÍDO ÍNTEGRO** · L1-75 · L75-96 · L96-140 · L141-205. Unión = [1, 205] |
| 2 | `docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md` | 2754 | `e8431c653cb7919e8d2ec82c5b4d3d11247a01aa61577bb8e5dd266916fb0e5d` | ✓ | ver §1.2 |
| 3 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 4085 | `8433bf23d559801fa3cfada1818996c2849521421545aa5e7eae33b4ce88e2bf` | ✓ | ver §1.2 |

Los tres SHA-256 coinciden con los que el manifiesto publica en sus filas 1, 3 y 4, y los
tres recuentos de líneas también. **Lo comprobé fila a fila y no lo heredé de nadie.**

### 1.2 · Los dos dictámenes cerrados

| fichero | líneas declaradas | mis líneas | SHA-256 declarado | mi SHA-256 | ¿= |
|---|---|---|---|---|---|
| `informes/DICTAMEN-BB.md` | 1571 | **1571** | `09eea2dc…b85aec` | **idéntico** | ✓ |
| `informes/DICTAMEN-CC.md` | 1398 | **1398** | `4ba093e0…d588334f` | **idéntico** | ✓ |

**LEÍDOS ÍNTEGROS los dos**, en cuatro y tres tramos respectivamente, unión = [1, 1571] y
[1, 1398]. No leí resumen de ninguno: no hay resumen que leer.

### 1.3 · Lo que abrí de los informes de relevo, y lo que no

Abrí `informes/INFORME-BB1.md`, `informes/INFORME-BB2.md`, `notas/BB3.md`,
`informes/INFORME-CC1.md` y `notas/CC2.md` **para extraer y contrastar sus bloques de sobre
embebidos (§0.2) y para barrer sus citas de huella**. `notas/BB3.md` lo leí además hasta
L120 para verificar por mí mismo su manifiesto de lectura. **NO declaro leídos íntegros los
cinco informes de relevo**, y no los cuento como cobertura mía. El manifiesto no me los
asigna; los dos dictámenes sí, y ésos sí están íntegros.

### 1.4 · Fuentes que abrí para VERIFICAR y que NO declaro leídas

`docs/owner/ADS-OWNER-RESOLUCIONES.md` (`O18` íntegra, 111 líneas, y los tres bloques por
`awk`) · el manifiesto del gate **en el commit del gate, íntegro, 193 líneas** —lo leí por
iniciativa propia porque §5 y §7 de esta adjudicación cuelgan de él— ·
`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` (las sedes puntuales de cada hallazgo que
sostengo) · `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` (L779) ·
`docs/evolucion/verificacion/derivar-universo-obligatorio.py` (cabecera, `_EXCLUIDO`,
`_barrer`, `ZONAS_DEL_ENCARGO`, componente (iv)) ·
`docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` (`_EXCLUIDO`,
`NORMATIVO`, las cinco podas por nombre de directorio) ·
`docs/evolucion/verificacion/README.md` (filas `G-23`, `G-26`, `G-29`, `G-33`) ·
`kernel/operativo/validadores/exclusiones.yaml` · las dos baterías, **ejecutadas** en
checkouts aislados y en un clon desechable.

---

## 2 · DONDE LOS DOS DICTÁMENES DISCREPAN, Y CÓMO LO RESUELVO CONTRA LA FUENTE

Leí los dos íntegros. **No resuelvo ni una por mayoría.** Cada fila la decidí abriendo el
árbol o ejecutando el instrumento.

### `D-1` · **`OBLIGATORIO − ASIGNADO`: ¿0 o 1?** — la que el encargo me manda verificar

`BB3`, y con él tres relevos de las dos cadenas, midieron **1**. `BB4` demostró **0**. Lo
medí yo, en las dos direcciones y contra los dos árboles:

    git show $G:$M | grep -oE '^\| [0-9]+ \| `[^`]+`' | sed 's/.*`\(.*\)`/\1/' | LC_ALL=C sort > asig.txt
    comm -23 <universo> asig.txt    # en el universo y sin asignar
    comm -13 <universo> asig.txt    # asignadas y fuera del universo

```text
FILAS DEL MANIFIESTO                74 brutas · 74 únicas · 0 duplicadas   (§4 17 + §5 57)

vs UNIVERSO DE LA CANDIDATA (74)
  en el universo y sin asignar      0
  asignadas y fuera del universo    0        →  OBLIGATORIO − ASIGNADO = 0.  CIERRA AL DÍGITO

vs UNIVERSO DEL GATE (75)
  en el universo y sin asignar      1        docs/…/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md
  asignadas y fuera del universo    0
```

Y verifiqué además, **fila a fila, las 74**, contra el commit candidato:

```text
filas comprobadas 74 · SHA-256 discrepantes 0 · recuentos de líneas discrepantes 0
suma de las líneas de las 74 filas = 66 747 = el titular publicado
66 747 + 193 (el manifiesto) = 66 940 = el universo del gate
```

**MI RESOLUCIÓN.** El manifiesto declara su objeto en su §1, y no admite lectura: `COMMIT
CANDIDATO 8c9ca9c…` · `TREE SHA 91fe62d3…`. **Contra el objeto que él mismo declara repartir,
la resta es 0 y las 74 filas casan sin una discrepancia.** `BB4` tiene razón y los tres
relevos midieron contra el otro árbol. **La resta NO está falseada.** Lo falso es el rótulo, y
eso es `DD-17`.

### `D-2` · **La reincidencia `U-02`→`X-06`: ¿rota o repetida?** — `CC3` se contradice consigo mismo

`CC3` §3.4 escribe: «`U-02`→`X-06`→`Z-12` **NO reincide**». `CC3` §4, ficha `CC-04`, escribe:
«**¿REINCIDENCIA DE QUÉ?** De la clase `U-02` → `X-06` → `Z-12`». **Son dos afirmaciones
incompatibles del mismo dictamen sobre el mismo objeto, y ninguna cadena podía resolverlo
porque las dos están dentro de `CC`.** Lo resuelvo yo, y las dos mitades son verdad de cosas
distintas:

```text
LA FILA DEL PROPIO DERIVADOR   `git show 8c9ca9c:…/derivar-universo-obligatorio.py | sha256sum`
—la que el sobre manda mirar    = 107fbb03…f78633
PRIMERO (obligación 3)—         `git show 5ed7a3b:…                            | sha256sum`
                                = 107fbb03…f78633   IDÉNTICA EN LOS DOS ÁRBOLES
                                y la fila 8 del manifiesto publica ese mismo valor.
                                → **NO REINCIDE.** `CC3` §3.4 acierta

EL TITULAR DE §2, L37           «74 fuentes · 66 747 líneas —sobre el árbol del GATE—»
                                el árbol del GATE da 75 / 66 940.
                                → **SÍ REINCIDE**, y es la clase `U-02`→`X-06`.
                                `BB4` y `CC-04` aciertan
```

**La fila no reincide; el titular sí.** `CC3` mezcló las dos en §3.4 y por eso pudo escribir
que `B` no falla por ahí y a la vez contar `CC-04` como reincidencia de esa misma clase.

### `D-3` · **La clase del ataque de `CC1-01`: ¿`A` o `C`?** — y con ella, la regla de clase entera

`CC1` lo trae como clase `A` («el séptimo árbol»); `CC3` lo rebaja: el ataque es `C` porque
**no puede alcanzar el commit** —Git rechaza `docs/owner/.git/…` en `add`, `add -f`, `add -A`,
`update-index --add` y `--cacheinfo`— y, si se fabrica el commit con fontanería, la receta del
sobre falla cerrado. **Reproduje la cadena de `CC3` y su conclusión es CORRECTA para su
variante.** La mitad PROMESA se queda, y es `DD-07`.

**PERO al resolver esto encontré que el corpus lleva DOS enunciados vigentes e incompatibles
de la regla de clase, y de cuál rija depende si mi octavo árbol (§4) cuenta.** Es `DD-19`:

```text
FORMULACIÓN 1 · `AA`, doc 25 §8   «`A` = la batería no detecta una incoherencia que está en
                                   el árbol que se le entrega, sin tocar la batería, su
                                   README, `HEAD`, las refs, la base ni el runner,
                                   **y SIN COMMITEAR**»
FORMULACIÓN 2 · `Z3`, doc 25 §4   «`A` = el defecto está EN EL CORPUS y la batería dice 38/38.
                                   Que el defecto esté o no confirmado es **IRRELEVANTE**:
                                   commitear es lo que hace el autor de una tanda en su propia
                                   rama, y **el corpus que el gate juzga es un COMMIT**»
```

**RESUELVO POR LA SEDE, y la sede es del Owner, no de un adjudicador.** Fui a las dos:

· `CHECKPOINT-ADS-NEXT.md` **L3269-3320**, «El criterio del gate siguiente», que el propio
  fichero designa como sede del criterio: define `A` como «*la batería comprueba el corpus
  contra sus contratos*» y `C` como «*resistencia a un ACTOR PRIVILEGIADO*». **No menciona
  commitear en ninguna de las tres.**
· `docs/owner/ADS-OWNER-RESOLUCIONES.md`, `O18` **L87-103**, leída íntegra: la batería
  garantiza «*coherencia interna*»; lo que no se afirma es protección frente a «*compromiso
  del canal del Owner · compromiso simultáneo del repositorio y del coordinador · robo de
  credenciales · reescritura autorizada de ramas remotas · manipulación del ejecutor externo ·
  falsificación de identidad*». **Ninguno de esos seis es «hacer un commit ordinario en la
  rama de revisión».**

> **DECIDO: la formulación 2 rige.** `C` es corromper la REFERENCIA —reescribir `HEAD`, las
> refs o la base, editar la batería o su README, mentir el runner—. **Commitear un fichero en
> la rama que se somete a revisión es el acto ordinario del coordinador, no un privilegio: es
> exactamente lo que hizo el commit `5ed7a3b` que este gate audita.** Y lo confirma el propio
> `AA`, que **clasificó `AA-E4b` —su árbol COMMITEADO— como `A`+`B`** pese a escribir «sin
> commitear» en su enunciado. **La cláusula «sin commitear» de la formulación 1 es un exceso
> de su autor, contradicho por su propia tabla de experimentos.**

**Consecuencia, y es la que decide §4 y §10:** un árbol defectuoso **commiteado** que la
batería no ve es clase `A`, y cuenta.

### `D-4` · **El punto fijo de `BB-03`: ¿imposible?** — lo sostengo, y CORRIJO a `BB4` en un punto

`BB4`: «*un fichero no puede contener su propio SHA-256: es un punto fijo de SHA-256. No es
difícil: es imposible*». `CC3` §6.4 llega al mismo hecho pero deja abierta la salida «*o se
asigna a sí mismo una fila*».

**Verifiqué la estructura**: la cabecera de las dos tablas del manifiesto es
`| # | ruta | líneas | SHA-256 | 1bis | revisor | relevo |`, y **las 74 filas publican su
SHA-256**. Para cerrar la resta a 0 sobre el árbol del gate, el manifiesto necesitaría una
fila sobre sí mismo con su propio SHA-256.

**CORRIJO A `BB4` EN LA PALABRA, Y LE DOY LA RAZÓN EN EL FONDO.** No está demostrado que
SHA-256 carezca de puntos fijos: lo que está fuera de alcance es **encontrar** uno, con un
coste esperado del orden de `2^256`. **La formulación correcta es «computacionalmente
inalcanzable», no «imposible».** El corpus, por cierto, **ya conoce este argumento y lo tiene
escrito**, en el propio `CHECKPOINT` (bloque `ÁRBOL VIGENTE`): «*un checkpoint que registrase
el SHA de su propio commit necesitaría otro commit para corregirlo, y así sin fin*». **Sabe la
clase; no la aplicó a la fila del manifiesto.**

**Y `CC3` se equivoca al ofrecer «se asigna a sí mismo una fila» como salida abierta**: con el
formato de fila vigente, no lo es. Las salidas reales son tres, y las tres son de `F4`:
(i) rotular «—sobre el árbol CANDIDATO—», que es donde el manifiesto declara su objeto y donde
la resta cierra a 0; (ii) publicar las dos aritméticas; (iii) que el derivador excluya de su
barrido el manifiesto en curso. **Ninguna reinterpreta una resolución del Owner.**

### `D-5` · **`ASIGNADO − LEÍDO`** — la resta que hundió el gate anterior

```text
CADENA `BB`   `BB3` declara ÍNTEGRAS sus tres (DECISIONES 1260 · CHECKPOINT 4085 ·
              00-INDICE 205), con tramos, SHA-256 recalculados y anclas · `BB1` doc 11
              L1-5800 · `BB2` L5801-final · `BB4` doc 25 íntegro           →  0
CADENA `CC`   `CC3` declara 10 de 10 con tramos y unión; `CC1` y `CC2` sus lotes  →  0
`DD` (yo)     mis TRES filas del manifiesto —1, 3 y 4—, leídas íntegras por mí    →  0
              (§1.1; los SHA-256 y los recuentos coinciden con el manifiesto)
──────────────────────────────────────────────────────────────────────────────────
ASIGNADO − LEÍDO  =  **0**
```

**LO DIGO CON LA RESERVA QUE MERECE, porque es exactamente lo que `AA` no pudo cerrar.**
Puedo verificar —y verifiqué— que los SHA-256 que las dos cadenas declaran son los del árbol,
y contrasté decenas de sus citas contra fichero y línea sin encontrar una falsa salvo el punto
de §2.2. **No puedo verificar que leyeran.** Es fiabilidad medida, no lectura probada, y quien
me lea debe pesarlo como tal. **Lo que sí es mío y es prueba: mis tres fuentes las leí yo.**

**`C-L.5` no se reabre por la resta en este gate.** Se reabre —o no— por lo demás.

### `D-6` · **`M-04`: `BB` no aporta nada; `CC` aporta el séptimo árbol** — y ninguno buscó el octavo

`BB4` lo declara sin adorno (su §8.2): *«`M-04` como proposición general: NO ATACADA por nadie
de mi cadena. No construimos un solo árbol defectuoso.»* `CC` sí: `CC1` lo trae, `CC3` lo
reproduce, lo extiende al derivador y **lo rebaja a `C` en su mitad ATAQUE con una cadena de
pruebas que verifiqué y que es correcta**. **Ninguna de las dos cadenas construyó un árbol que
alcanzara el commit.** Eso es lo que hice yo, y está en §4.

### `D-7` · Discrepancias menores, resueltas

| # | discrepancia | mi resolución |
|---|---|---|
| `D-8` | `BB1` dice que hay red; `BB2` declara que no la hay | **HAY RED**, y la usé: `git ls-remote origin` devuelve `5ed7a3b…` para `refs/heads/review/f4c-gate-certificacion-5-20260831` y `8c9ca9c…` para `refs/heads/review/f4c-perimetro-derivado-candidate-20260831`. **Las dos refs remotas apuntan a los dos commits del sobre.** `BB1` acierta; `BB2` se equivocó sobre su entorno, no sobre los hechos |
| `D-9` | `CC1` gradúa `CC1-05` MEDIO por «longitud NO ACOTADA»; `CC3` lo refuta con su variante `E` | **`CC3` acierta**: la región de clase `tanda` cierra en la línea siguiente que empieza en columna 0. Lo que sobrevive es la promesa incompleta del README, y entra como `DD-12`, MENOR |
| `D-10` | `CC1` sostiene `CC1-03` como hallazgo; `CC3` lo retira porque está declarado | **`CC3` acierta y va contra su cadena.** Lo leí: el README declara las dos premisas y la apertura del hueco («queda ABIERTA y dicha»). No lo cuento |
| `D-11` | `BB4` rebaja `BB1-01` de GRAVE a MEDIO | **Acepto la rebaja** y la razón: omitir una población nacida después no es afirmar una cifra falsa sobre una tabla existente |

---

## 3 · MI PROPIA EJECUCIÓN — batería en los dos árboles, batería del kernel, cifras rederivadas

**Nada de esta sección lo heredo. Cada cifra sale de un comando que corrí yo.** Todo en
checkouts aislados fuera del repositorio (`git read-tree` + `git checkout-index`) o en un clon
desechable en `.../scratchpad/lab-DD/clone`, **borrado al terminar**.

### 3.1 · La batería del kernel · `registrar_evidencia.py`, en los DOS árboles

```text
                                    CANDIDATA 8c9ca9c…        GATE 5ed7a3b…
registrar_evidencia.py              13/13 · RC=0              **12/13 · RC=1**
                                    13 evidencias publicadas   12 publicadas · 1 problema
validador que falla                 —                          `referencias`, código 1
comprobar_referencias --exclusiones T147 **SUPERADA** · RC=0   T147 **FALLIDA** · RC=1
documentos analizados               263                        264
ficheros de evidencia que la
batería reescribe                   **0**                      **2**
                                                               fuentes-salida.txt
                                                               negativos-salida.txt
```

Diagnóstico literal de `T147` sobre el árbol del gate, copiado de mi salida:

    T147  FALLIDA   Todo documento es alcanzable por ruta, y ninguna referencia es ambigua
      · docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-5-20260831.md:
        no lo alcanza ningún enlace por ruta, ninguna referencia de campo y ninguna cita de
        sus identificadores. Existe para nadie

**`BB3` y `BB4` son exactos en los tres extremos, incluidos los dos nombres de fichero.**

### 3.2 · **Y ESTO ES MÍO: la regla ERA CUMPLIBLE, y lo demuestro en una línea**

`Y4` dejó escrito en el documento 25 §8 que la tensión —«el manifiesto se commitea solo» vs.
«se enlaza en el mismo commit»— **no es insatisfacible**, y que la salida cuesta una línea.
`BB4` lo cita. **Ninguno de los dos lo ejecutó. Yo sí.** Sobre el árbol del gate, en el clon:

```text
1 · añadí UNA fila a docs/evolucion/00-INDICE.md enlazando el manifiesto del gate 5
      →  comprobar_referencias --exclusiones   T147 **SUPERADA** · RC=0 · 264 documentos
      →  comprobar-correccion-gate-de-cierre   **38/38 en verde** · EXIT=0
2 · y reejecuté registrar_evidencia.py
      →  **13/13 validadores en verde · 13 evidencias publicadas · 0 problemas** · RC=0
      →  segunda ejecución idéntica: converge, sin tercera
      →  el commit habría llevado 4 ficheros en vez de 1
```

> **QUEDA DEMOSTRADO, Y NO ARGUMENTADO: el remedio de una línea funciona.** `BB-01` deja de
> ser un dilema estructural y pasa a ser **incumplimiento de una regla cumplible, escrita por
> el propio corpus, publicada con su comando, denunciada por su propio comando, con el remedio
> redactado por el dictaminador del gate anterior y verificado por mí.** Quinta vez consecutiva.

### 3.3 · La batería adversarial · `comprobar-correccion-gate-de-cierre.py`

```text
EN UN CLON CON HISTORIA (git checkout <commit>)
  candidata 8c9ca9c…   **38/38 en verde · EXIT=0**
  gate      5ed7a3b…   **38/38 en verde · EXIT=0**

EN LA MATERIALIZACIÓN QUE LA RECETA DEL SOBRE PRESCRIBE (read-tree + checkout-index, sin .git)
  candidata 8c9ca9c…   **29/38 · EXIT=1**    9 comprobaciones «FALLAN CERRADO SIN GIT»
  gate      5ed7a3b…   **29/38 · EXIT=1**    las mismas nueve
  las nueve: G-11 · G-11b · G-21 · G-22 · G-23 · G-28 · G-29 · G-30 · G-34
```

**Es un hallazgo mío y lo declaro con su matiz.** No es un defecto —fallar cerrado es la
dirección segura, y el propio título de cada una lo anuncia—, pero **acota lo que «38/38»
certifica y ninguna sede lo dice: nueve de las treinta y ocho no son propiedades del COMMIT,
sino de un repositorio con historia.** El objeto que el sobre define y materializa no puede
ser juzgado por ellas. Va como `DD-20`.

### 3.4 · Las cifras del sobre, rederivadas (§0.3 y §0.4)

Los 21 campos reproducen. Los dos digest de universo reproducen con la receta publicada y
**sin ejecutar el emisor**. La única ruta en que los universos difieren es la que el sobre
declara. Las dos refs remotas resuelven contra el remoto real a los dos commits del sobre.
`66 747 + 193 = 66 940` cierra la aritmética entre los dos árboles.

### 3.5 · Las cifras del manifiesto, rederivadas

```text
74 filas · 74 rutas únicas · 0 duplicadas          (§4 17 filas + §5 57 filas)
74 filas verificadas contra el commit CANDIDATO:   0 SHA-256 discrepantes · 0 líneas discrepantes
suma de líneas de las 74 filas = 66 747            = el titular de §2 y de §6
OBLIGATORIO − ASIGNADO  = 0 contra la candidata · = 1 contra el árbol del gate
ASIGNADO − LEÍDO        = 0
git diff --stat 8c9ca9c 5ed7a3b  →  1 fichero, 193 inserciones. El gate NO tocó `verificacion/`
```

### 3.6 · Las promesas del instrumento, reproducidas por mí con su control positivo

| lo que el README promete | lo que el árbol hace | control positivo |
|---|---|---|
| `G-29`: «*el perímetro **YA NO SE ESCRIBE**… es hoy uno solo y **por NATURALEZA**: `.git`… y el bytecode **por su extensión**»* | `_EXCLUIDO = re.compile(r"(?:^\|/)\.git(?:/\|$)\|\.py[co]$")`, **idéntico en la batería (L1839) y en el derivador (L144)**, y la poda se evalúa sobre el **NOMBRE DESNUDO** del directorio en **cinco sitios de dos ficheros**. Es una lista escrita | el mismo fichero con nombre ordinario → `37/38 FALLO G-29` |
| `G-23`: «**lo normativo intacto**» | `NORMATIVO` es un regex de **seis patrones** que cubre **4 de los 14** ficheros de `docs/rediseno/`. Reescribí `00-MAPA.md` declarando que PREVALECE sobre el material APROBADO y deja `O17`·`O18`·`O19` sin efecto → **38/38 EN VERDE** | el mismo texto en `a-CAPACIDADES-APROBADA.md` → **37/38 FALLO G-23** |
| `G-33`: «*una prueba negativa **ANCLADA EN EL ÁRBOL** — su mutante sale del texto del corpus, y **un corpus distinto la mueve**»* | la mitad MUTANTE es **tautológica**: `_b_mutilado` borra toda línea que contenga `FASE 0`, y la primera cláusula de `_fase0_conforme` es `if not re.search(r"FASE 0", bloque)`. Verdadera **para todo árbol posible**. Barrido mío de **200 000** textos: **0 contraejemplos** | — |
| `G-10`: «*Un cardinal con comprobación que lo **DERIVE** no caduca en silencio*» | `G-10` comprueba **tres substrings literales** y **seis nombres de capacidad escritos a mano** en el propio script. Detecta que desaparezca una; **NO detecta que aparezca una séptima** | — |
| `G-29`: «*una segunda sede plantada en esa zona… **sin ese enlace es ROJA**»* | **FALSO para todo commit.** Ver `DD-10` en §4.3 | ver §4.3 |

**Cinco promesas publicadas que el árbol no sostiene.** No es estilo: es **la sexta condición
que el Owner impone para cerrar `M-04` en `F4c`** (§6).

---

## 4 · MI ATAQUE A `M-04` — ¿HAY UN OCTAVO ÁRBOL?

# **SÍ. Y ES ESTRICTAMENTE PEOR QUE LOS SIETE ANTERIORES.**

**Laboratorio:** `git clone --no-hardlinks` del repositorio en `.../scratchpad/lab-DD/clone`,
`git checkout 8c9ca9c`. Una copia limpia por experimento. **El repositorio real nunca recibió
una escritura**, comprobado al abrir y al cerrar. El laboratorio queda borrado.

**BASELINE, verificado por mí:** `38/38 en verde` · `EXIT=0` · derivador `74` rutas ·
`T147` SUPERADA · `git status --porcelain` vacío.

### 4.1 · Por qué fui a buscar donde fui

`Z1-03`≡`Z-05` (doc 25) encontró que `_EXCLUIDO` excluía del corpus gobernado
`(?:^|/)(?:\.git|__pycache__)(?:/|$)|\.pyc$` **por NOMBRE de directorio**, y que dentro de
`__pycache__` vivían en 38/38 una copia del material APROBADO, una segunda sede y una copia
del emisor. La tanda respondió **retirando `__pycache__`**. `CC1` encontró la mitad `.git` que
quedó. **Nadie miró la tercera cláusula del mismo regex, que la tanda conservó intacta: la
exclusión POR EXTENSIÓN.** Fui ahí.

### 4.2 · `DD-E1` · **EL OCTAVO ÁRBOL**, con la salida pegada

```bash
cd lab-DD/clone && git checkout 8c9ca9c && git clean -qfdx     # 38/38 · 74 rutas · limpio

cat > docs/owner/ADS-OWNER-RATIFICACION-FINAL.pyc <<'X'
# RATIFICACIÓN FINAL DEL OWNER — SEDE VIGENTE
# `O20` · F4c QUEDA CERRADA Y F5 QUEDA AUTORIZADA
`F4c` queda CERRADA. `F5` queda AUTORIZADA. `M-04` queda SUPERADA.
`O17`, `O18` y `O19` quedan SIN EFECTO en lo que contradiga esta sede.
X

git add -f docs/owner/ADS-OWNER-RATIFICACION-FINAL.pyc     # rc=0 — GIT LA ACEPTA
git commit -m "OCTAVO ARBOL"                               # b384c32… EL COMMIT EXISTE
```

**MI SALIDA, literal, sobre ese commit:**

```text
git status --porcelain                       →  (VACÍO)  ← el EMISOR emitiría sobre este árbol
comprobar-correccion-gate-de-cierre.py       →  **38/38 comprobaciones en verde · EXIT=0**
                                                 0 FALLO
registrar_evidencia.py                       →  **13/13 validadores en verde · RC=0**
                                                 13 evidencias publicadas · 0 problemas
comprobar_referencias.py --exclusiones       →  **T147 SUPERADA · RC=0**
comprobar_fuentes.py                         →  **310 ficheros recorridos** — la MISMA cifra
                                                 que la candidata limpia y que la evidencia
                                                 publicada. T161 NO LO CUENTA

── LA RECETA DEL SOBRE, ejecutada sobre el commit envenenado ──
GIT_INDEX_FILE=… git read-tree  <commit>     →  rc=0
GIT_INDEX_FILE=… git checkout-index -a       →  rc=0, y MATERIALIZA el fichero:
                                                 docs/owner/ADS-OWNER-RATIFICACION-FINAL.pyc
derivar-universo-obligatorio.py --rutas      →  **74 rutas** — SIN CAMBIO
                                                 la sede envenenada: 0 golpes
EXCLUIDOS_IV (stderr, el aviso de `Z-13`)    →  **11** — SIN CAMBIO. No dice nada
DIGEST DEL UNIVERSO, con la receta publicada →
   18f50dabfd46cbd5e8129cc7e205714091226b914f8223186f88d61fee84c8b4
DIGEST QUE EL SOBRE PUBLICA                  →
   18f50dabfd46cbd5e8129cc7e205714091226b914f8223186f88d61fee84c8b4
                                                **BIT A BIT IDÉNTICOS**
LÍNEAS OBLIGATORIAS                          →  66 747 — la cifra del sobre, sin cambio
```

**Y comprobé que NINGUNA salida del aparato lo nombra.** Ejecuté los cinco instrumentos y
conté los golpes del nombre del fichero en cada salida:

```text
comprobar-correccion-gate-de-cierre.py       0 golpes
derivar-universo-obligatorio.py (tabla)      0
derivar-universo-obligatorio.py --rutas      0     (y 0 en su stderr)
comprobar_referencias.py --exclusiones       0
comprobar_fuentes.py                         0

LA ÚNICA VÍA QUE LO VE:  git ls-tree -r --name-only HEAD | grep RATIFICACION
                         docs/owner/ADS-OWNER-RATIFICACION-FINAL.pyc
                         y NADA en el corpus instruye a nadie a mirar ahí
```

**`DD-E1b` · VARIANTE, para demostrar que es CLASE y no CASO:** `docs/owner/SEDE.pyo` +
`docs/evolucion/verificacion/manifiestos/F4C-SUSTITUTORIO.pyc`, los dos commiteados →
**38/38 en verde**, derivador **74**, `git status` vacío. **La zona `manifiestos/`, que es la
sede del cliquet, es igual de ciega.**

**`DD-E1c` · CONTROL POSITIVO:** el mismo fichero como `docs/owner/SEDE.md`, **sin commitear**
→ **37/38 · FALLO `G-29`**, y el universo crece de 74 a 75. **El mecanismo funciona; el
perímetro no.** Es defecto de perímetro, no de idea.

### 4.3 · `DD-E2` · Y por el camino encontré un SEGUNDO, que explica por qué el primero es tan limpio

Al montar el control positivo descubrí que **da resultados distintos según se commitee o no**:

```text
docs/owner/SEDE.md  **SIN COMMITEAR**   →  **37/38 · FALLO G-29**   (lo que `CC3` midió)
docs/owner/SEDE.md  **COMMITEADA**      →  **38/38 EN VERDE**       (nadie lo había medido)
```

**La guarda de admisión de `G-29` sobre `docs/owner/` —que es el REMEDIO de `AA-01`, `Z-02`,
`Z1-01`≡`W-04`≡`Z-02`— es INERTE sobre cualquier fichero que ya esté en `HEAD`.** El propio
README lo declara a medias, bajo `AA-03`: «*la rama sólo se consulta para lo que aún no está
en `HEAD`*». **Pero la fila `G-29` del mismo README promete lo contrario, y sin matiz:** «*una
segunda sede plantada en esa zona, al lado o en un subdirectorio, **sin ese enlace es ROJA***».
**Es falso para todo commit. Y el objeto que este gate audita ES UN COMMIT.**

### 4.4 · Qué significa, y lo digo con la regla de clase delante

> **CLASE `A`, y no `C`.** Contra la definición que resolví en `D-3`: **no toqué la batería,
> ni su README, ni `HEAD`, ni las refs, ni la revisión base, ni el runner.** Añadí **un
> fichero**. Es exactamente lo que hace el autor de una tanda en su propia rama de revisión, y
> es lo que hizo el commit `5ed7a3b` que este gate audita.

**Y es estrictamente peor que los siete anteriores, en las dos dimensiones que los gates 24 y
25 usaron para rebajarlos:**

```text
`Z-E3`/`Z-E3b` (`__pycache__`)  la tanda lo CERRÓ retirando ese nombre del regex.
                                Mi ataque usa la MITAD DEL MISMO REGEX QUE SOBREVIVIÓ
`CC1-01` (`docs/owner/.git/`)   `CC3` lo rebajó a `C` porque **no alcanza el commit**: Git
                                rechaza la ruta en `add`, `add -f`, `add -A`,
                                `update-index --add` y `--cacheinfo`, y con fontanería la
                                receta del sobre **falla cerrado**.
                                → **MI ATAQUE SÍ ALCANZA EL COMMIT.** `git add -f` devuelve
                                  rc=0, el commit existe, `read-tree` da rc=0 y
                                  `checkout-index` materializa el fichero
`AA-01` (segundo doc del Owner) `AA` midió que el universo NO crecía. Pero su fichero era
                                `.md`, y **hoy `docs/owner/` se barre entero**: el universo
                                SÍ crece a 75 y el DIGEST DEL SOBRE CAMBIA. El ancla lo caza.
                                → **CON MI EXTENSIÓN EL DIGEST NO CAMBIA NI UN BIT**
`Z-E7` (`export-ignore`)        cerrado: la receta pasó de `git archive` a
                                `read-tree`+`checkout-index`. Lo verifiqué: rc=0 y materializa
`Z-E8` (H1 de no-dictamen)      declarado ABIERTO por el propio derivador, y **VISIBLE**:
                                `EXCLUIDOS_IV` lo publicaría.
                                → **EL MÍO NO APARECE EN `EXCLUIDOS_IV` NI EN NINGUNA SALIDA**
```

> ### **ÉSTA ES LA CONCLUSIÓN QUE SOSTENGO, Y ES EL NÚCLEO DE MI VEREDICTO**
>
> Existe un commit que **añade al árbol auditado un documento que declara `F4c` CERRADA,
> `F5` AUTORIZADA y `M-04` SUPERADA**, y que:
>
> · deja `git status --porcelain` **VACÍO**, de modo que **el emisor emitiría sobre él**;
> · pasa la batería adversarial en **38/38** y la del kernel en **13/13**;
> · **no aparece en el universo obligatorio** (74, sin cambio), luego **no recibe fila de
>   manifiesto, ni revisor asignado, ni huella en el sobre**;
> · **no aparece en `EXCLUIDOS_IV`**, que es el aviso que `Z-13` puso para que un universo que
>   encoge lo dijera;
> · y **produce, con la receta que el propio sobre publica, un DIGEST DE UNIVERSO BIT A BIT
>   IDÉNTICO al que el sobre de este gate ancla**.
>
> **El ancla externa que `O18(b)` adoptó para poder cerrar `F4c` es CIEGA a este commit, y no
> por un fallo del emisor ni de la entrega ni de la receta: los tres funcionan.** Es ciega
> porque el digest se calcula sobre un universo derivado por un **perímetro que vive dentro
> del árbol auditado y que excluye POR NOMBRE**. **Quien controla el nombre controla lo que el
> ancla ve.**

`M-04` **SIGUE VIVA, en clase `A`, en su QUINTO gate**, y esta vez la puerta está en el único
sitio del aparato que ninguno de los cinco gates había mirado.

---

## 5 · EL APARATO DEL GATE — ¿INVÁLIDO, DEGRADADO, O UN HALLAZGO MÁS?

**Tres cosas están sobre la mesa y ninguna es del corpus auditado. Las decido una a una.**

### 5.1 · ¿QUÉ OBJETO SE AUDITA? — **LA CANDIDATA `8c9ca9c`**

Lo decido expresamente, y por tres razones que son mediciones y no lecturas:

1. **Lo dice el manifiesto, que es anterior a todo revisor y no se modifica.** Su §1 se titula
   «**Objeto del reparto**» y fija `COMMIT CANDIDATO 8c9ca9c…` y `TREE SHA 91fe62d3…`.
   Y contra ese objeto **sus 74 filas casan sin una discrepancia** y la resta cierra a 0
   (§3.5). No hay ambigüedad sobre qué se reparte.
2. **Lo dice el sobre, y con el dedo.** Publica los dos árboles «sin mezclar ni un campo», su
   tabla de la sede rotula la columna «**CANDIDATA (COMMIT AUDITADO)**», y su obligación 4
   ordena distinguirlos. Un sobre que manda distinguir no puede leerse como si los fundiera.
3. **Es la doctrina que `U`, `X` y `AA` ya establecieron**, y que verifiqué reproduciendo su
   medición: `AA`, doc 25, `D-5`: «*La evidencia es VERDADERA de la candidata y FALSA del árbol
   del gate*». Cambiar de criterio en el quinto gate sería exactamente lo que este expediente
   castiga.

**Y lo que esa decisión NO autoriza**, que es la mitad que importa: **no castiga a la candidata
por lo que rompió el aparato, y no absuelve al aparato porque la candidata esté limpia.**

### 5.2 · EL RÓTULO DEL MANIFIESTO — **NI INVALIDA NI DEGRADA: ES UN HALLAZGO MÁS, GRAVE, DEL APARATO**

`CC3` dice error de rótulo que no invalida. `BB4` lo llama reincidencia de `U-02`/`X-06`, que
el gate anterior declaró ROTA. **Los dos aciertan en su mitad, y lo decido así:**

**NO INVALIDA, y digo por qué medido y no supuesto.** Los dos disparadores de invalidez que
§11.6 y el manifiesto §8 definen son **(i) diferencia ENTRE SOBRES** y **(ii) diferencia entre
el SOBRE y lo que el árbol muestra**. Los medí los dos:

```text
(i)   el sobre NO se transcribió: vive en un fichero externo. Los CUATRO bloques embebidos son
      byte a byte el fichero (SHA-256 idéntico, 190 líneas), y los tres restantes publican su
      digest correcto.  CERO diferencias entre lo que los siete leyeron.  →  NO SE ACTIVA
(ii)  recalculé los 21 campos desde los dos commits, incluidos los dos digest de universo con
      la receta publicada y sin ejecutar el emisor.  CERO diferencias.    →  NO SE ACTIVA
```

Un rótulo equivocado **dentro del manifiesto** es un defecto del objeto que el manifiesto
describe, no una discrepancia de su ancla. **Declarar inválido por eso sería confundir el
objeto con su etiqueta**, y sería además lo contrario de lo que `AA` hizo al rechazar el
argumento Merkle por la razón simétrica.

**PERO ES GRAVE, Y `BB4` TIENE RAZÓN EN POR QUÉ.** `AA` declaró esta reincidencia **ROTA** hace
un gate y la puso entre las diez cosas que «*SÍ ha quedado cerrado, y no es cortesía*». El
sobre de **este** gate manda mirarla **PRIMERO** (obligación 3). **Se rompió y se rehízo en el
gate siguiente, en el campo que el ancla señala con el dedo.** Es `DD-17`.

### 5.3 · EL MANIFIESTO NO ENLAZADO — **12/13 sobre el gate, 13/13 sobre la candidata**

Medido por mí en §3.1 y §3.2. **Consecuencia, en tres partes que no se mezclan:**

1. **NO cuenta contra el objeto auditado.** La candidata pasa 13/13 y `T147`, y no ensucia un
   byte. Quien quiera fundar insuficiencia en un validador en rojo **no puede hacerlo con éste**.
2. **SÍ cuenta contra el aparato, y es GRAVE**, porque mide la disciplina del commit que viene
   a certificar. **Quinta recurrencia consecutiva** de `S-18`≡`T-14` → `V-06`≡`X-07`/`W-16` →
   `Y-03`+`Y-04`≡`Z-09` → ésta. El propio `00-INDICE.md` la registra como 2.ª y 4.ª en sus
   filas L132 y L134, y su L141-147 escribe: «*La regla funciona… lo que falló fue cumplirla*».
3. **Y no es un dilema: lo ejecuté (§3.2).** Una fila del índice pone `T147` en verde; una
   reejecución más da 13/13 y converge. **El remedio de una línea estaba escrito, medido y
   publicado por el gate anterior, y no se aplicó.**

### 5.4 · EL PUNTO FIJO — **CIERTO, Y ES HALLAZGO MÍO QUE LA REGLA ES IRREALIZABLE TAL COMO ESTÁ ESCRITA**

Comprobado (§`D-4`). El remedio de `AA-01` —barrer `manifiestos/` entero, que es **correcto y
necesario**— hizo del manifiesto del gate en curso **fila de su propio universo**. Con el
formato de fila vigente (`ruta | líneas | SHA-256`), cerrar `OBLIGATORIO − ASIGNADO = 0` sobre
el árbol del gate exigiría que el manifiesto contuviera su propio SHA-256: **computacionalmente
inalcanzable**, del orden de `2^256`.

```text
GATE 4   manifiesto 4B · 70 filas · universo del gate 70 · el 4B **NO** está en su universo
         →  comm en las dos direcciones: 0 y 0.  CERRABA contra el árbol del gate
GATE 5   manifiesto 5  · 74 filas · universo del gate 75 · el 5 **SÍ** está en su universo
         →  cerrar a 0 exige el punto fijo
CAUSA    `manifiestos/` pasó de RUTAS LITERALES a ZONA BARRIDA (`ZONAS_DEL_ENCARGO`), que es
         el remedio de `AA-01`≡`Z2-02`≡`Z-03`. Es correcto, y abrió esto
```

> **HALLAZGO MÍO: una regla del corpus es irrealizable tal como está escrita**, y lo será en
> **todos** los gates siguientes. Si nadie toca el enunciado, el gate 6 registrará una sexta
> reincidencia de algo que nadie puede cumplir. **No invalida nada** —la resta cierra a 0
> contra el objeto que el manifiesto declara— y **el remedio es de `F4`**: rotular el árbol
> candidato, publicar las dos aritméticas, o excluir del barrido el manifiesto en curso.

### 5.5 · ¿REPITE EL GATE 5 LA CAUSA DE INVALIDEZ DEL 4? — **NO, Y ESO ES REAL**

**El remedio del gate 5 funcionó exactamente donde el gate 4 murió**, y lo digo con la misma
fuerza con que digo lo demás. Cuatro bloques embebidos byte a byte, tres digest publicados
correctos, cero divergencia entre los siete. **El sobre salió del repositorio auditado y dejó
de transcribirse, y eso cerró de raíz —no mitigó— la vía que mató al cuarto gate.**

### 5.6 · **VEREDICTO SOBRE EL APARATO**

> **EL GATE 5 ES VÁLIDO.** Ningún disparador de invalidez se activa, y lo medí. **NO lo
> degrado.** Los tres defectos del aparato —`DD-16`, `DD-17`, `DD-18`— entran como hallazgos
> con su severidad, y ninguno toca la identidad del objeto.
>
> **Y hago constar lo que eso significa: este veredicto NO se apoya en el aparato.** Si el
> aparato fuera perfecto, mi veredicto sería el mismo, porque lo sostiene §4.

---

## 6 · HALLAZGOS SOSTENIDOS, CON SU CLASE `A`/`B`/`C` Y SU REMEDIO

### 6.0 · PRIMERO, LA DISTINCIÓN DEL OWNER — COMPROBADA POR MÍ EN SU SEDE CANÓNICA

El encargo me manda ir a `docs/owner/ADS-OWNER-RESOLUCIONES.md` y comprobar por mí mismo si
`CC3` tiene razón cuando sostiene que `O18` fija **seis** condiciones para cerrar `M-04` en
`F4c` y que la sexta es «ninguna promesa de seguridad superior a la realmente entregada».
**Leí `O18` íntegra —111 líneas— del commit auditado. `CC3` TIENE RAZÓN, y lo transcribo del
árbol, líneas 105-108 de la resolución:**

> «**`M-04` puede cerrarse para el alcance de `F4c` únicamente si el gate independiente
> demuestra:** batería interna coherente · sobre externo recibido antes de leer · todas sus
> huellas coincidentes · referencias remotas intactas · cobertura completa · **ninguna promesa
> de seguridad superior a la realmente entregada**.»

Y dos bloques antes, la misma resolución escribe qué NO se afirma —«*`F4c` **NO** afirma
resistencia completa frente a un actor privilegiado*»— y qué sí garantiza la batería interna:
«*coherencia interna · detección de regresiones conocidas · derivación de inventarios ·
contradicciones entre fuentes · cambios respecto a referencias recibidas · cumplimiento de
contratos documentales*».

> ### **ESTO ORDENA MI CLASIFICACIÓN, Y LO DIGO CON TODAS LAS LETRAS.**
> **Prometer de más NO es una objeción de estilo: es una de las SEIS condiciones que el propio
> Owner impone para cerrar `M-04` dentro de `F4c`.** `CC3` es el único de los siete que la
> citó, y es la pieza que más pesa en este gate.

**Y la aplico en las dos direcciones, que es lo que la hace justa.** Las mido una a una contra
el objeto auditado:

| # | condición de `O18` | ¿se demuestra? | mi medición |
|---|---|---|---|
| 1 | **batería interna coherente** | **NO** | §4: un commit con un documento que declara `F4c` cerrada pasa `38/38` y `13/13`. Y §3.6: `G-23` deja reescribir 10 de los 14 ficheros de `docs/rediseno/` en verde |
| 2 | **sobre externo recibido antes de leer** | **SÍ** | §0.2: fichero externo, cuatro bloques byte a byte, tres digest correctos, cero divergencia entre los siete |
| 3 | **todas sus huellas coincidentes** | **SÍ** | §0.3 y §0.4: los 21 campos y los dos digest de universo reproducen |
| 4 | **referencias remotas intactas** | **SÍ** | `git ls-remote origin`: las dos refs apuntan a los dos commits del sobre |
| 5 | **cobertura completa** | **SÍ, con reserva** | `OBLIGATORIO − ASIGNADO = 0` contra el objeto declarado · `ASIGNADO − LEÍDO = 0`. La reserva, en `D-5` y §9 |
| 6 | **ninguna promesa superior a la entregada** | **NO** | §3.6: **CINCO promesas publicadas que el árbol no sostiene**, cuatro con control positivo mío |

**Dos de las seis fallan. `M-04` NO puede cerrarse para el alcance de `F4c` con este árbol, y
lo dice el Owner, no yo.**

### 6.1 · CRITERIO Y REGLA QUE ME IMPONGO

**Severidad**, la de los cinco gates: **BLOQUEANTE** obliga a decidir arquitectura nueva ·
**GRAVE** una garantía publicada no se sostiene · **MEDIO** una afirmación vigente es falsa sin
cambiar el comportamiento · **MENOR** editorial o de propagación.
**Clase**, la que resolví en `D-3`: **`A`** coherencia interna · **`B`** exige una decisión del
Owner que no se deduzca de `O17`, `O18` y `O19` · **`C`** actor privilegiado, contratado a `F6`
y **no exigible en `F4c`**.
**Sólo entra lo que reproduje YO, con MI comando.** Lo que sostengo de mis fuentes sin haberlo
reproducido va marcado.

### 6.2 · DEL OBJETO AUDITADO — la candidata `8c9ca9c`

| id | sev | clase | qué es, y dónde lo verifiqué | **REMEDIO que lo cierra** |
|---|---|---|---|---|
| **`DD-01`** | **GRAVE** | **A** | **EL OCTAVO ÁRBOL** (§4). `_EXCLUIDO` excluye **por EXTENSIÓN** en los DOS instrumentos (batería L1839, derivador L144). Un documento que declara `F4c` cerrada y `F5` autorizada, nombrado `.pyc` bajo `docs/owner/`, **alcanza el commit**, deja `git status` vacío, pasa **38/38** y **13/13**, no entra en el universo, no recibe fila ni revisor, no aparece en `EXCLUIDOS_IV` y **produce el digest del sobre bit a bit idéntico** | Excluir **por NATURALEZA y no por nombre**: `.git` **sólo en la raíz de la ruta relativa** —y evaluando la poda sobre la RUTA, no sobre el nombre desnudo del directorio, en los **cinco** sitios de los dos ficheros que `CC3` localizó—, y el bytecode **por ser bytecode** (contenido), no por su sufijo. Mientras eso no exista, **todo fichero excluido debe publicarse en la salida con su ruta**, como `EXCLUIDOS_IV` hace con el componente (iv) |
| **`DD-02`** | **GRAVE** | **A** | **La guarda de admisión de `G-29` sobre `docs/owner/` es INERTE sobre todo fichero ya en `HEAD`** (§4.3). Medido: la misma segunda sede da `37/38 FALLO G-29` sin commitear y **`38/38` commiteada**. El README promete «*sin ese enlace es ROJA*», y **el objeto auditado es un commit** | Que la admisión se evalúe sobre el **contenido del commit** y no sólo sobre lo que aún no está en `HEAD`: la lista de `docs/owner/` enlazada desde `00-INDICE.md` se contrasta contra `git ls-tree -r <commit> docs/owner/`, que es una llamada |
| **`DD-03`** | **GRAVE** | **A** | `G-29` promete «*el perímetro **YA NO SE ESCRIBE**… es hoy uno solo y **por NATURALEZA***» y es **falso**: `.git` se excluye **por nombre y a cualquier profundidad**, y el comentario que precede a la línea escribe el argumento que la condena. Origen `CC1-01`/`CC-01`; reproducido por mí con su control positivo | Reescribir la fila `G-29` del README para que diga **lo que el código hace**, en el mismo commit en que se aplique `DD-01`. Es sexta condición de `O18` |
| **`DD-04`** | **GRAVE** | **A** | `G-23` promete «**lo normativo intacto**» sobre `NORMATIVO`, un regex de **seis patrones** que cubre **4 de 14** ficheros de `docs/rediseno/`. **Reproducido por mí con su control positivo:** `00-MAPA.md` reescrito declarando que prevalece sobre el material APROBADO y deja `O17`·`O18`·`O19` sin efecto → **38/38 verde**; el mismo texto en `a-CAPACIDADES-APROBADA.md` → **37/38 `FALLO G-23`**. Origen `CC1-02`/`CC-02` | Derivar el perímetro normativo del **conjunto de ficheros de `docs/rediseno/`** contra la revisión base, como `G-23` ya hace con el kernel, en vez de enumerar seis patrones |
| **`DD-05`** | **GRAVE** | **A** | **«`CI` o el ejecutor externo»** bajo el rótulo «*LITERAL DE LA SEDE CANÓNICA DEL OWNER*». Verificado por mí: doc 11 **L8687** frente a sede **L192** («*el ejecutor externo no puede compartir…*»), y `grep -c '\bCI\b'` sobre la sede = **0**. **Reincidencia LITERAL de `Y-09`**, con la orden de `AA` de retirarla ya dada | **Retirar dos palabras.** Coste nulo |
| **`DD-06`** | **GRAVE** | **A** | **«robustez y revalidación permanente por encima del ahorro operativo»** atribuido al Owner con «*en las palabras del Owner*» (`DECISIONES` **L779**) y «*en sus palabras*» (`00-INDICE` **L88**), en dos sedes VIVAS. `grep -c robustez` sobre la sede canónica = **0**, verificado por mí. **Reincidencia de `Y-05`**, que sobrevivió porque el remedio se aplicó a las **comillas** y no al **acto de atribuir**: ésta va en cursiva | Retirar la atribución o reatribuirla a su sede real, en las dos. **Y barrer por el ACTO —«en sus palabras», «en las palabras del Owner», «dice con sus palabras»— y no por la tipografía** |
| **`DD-07`** | **GRAVE** | **A** | **`C-L.5` tiene DOS estados vigentes.** Verificado por mí: doc 11 **L11368** («*CERTIFICADA por el documento 21, y vigente para todo gate posterior*») y **L11493** («*Estado: CERTIFICADA*») frente al `CHECKPOINT` **L17**, `00-INDICE` L92 y el manifiesto del gate («**`C-L.5` ABIERTA**»). **La sede que discrepa es la que el propio documento designa como sede de la condición** | Marcar `[HISTÓRICO]` las dos sedes de §11 y remitir a la clasificación vigente del checkpoint, que es su única sede |
| **`DD-08`** | **GRAVE** | **A** | **El `CHECKPOINT` **L2349-2354** copia el estado en la misma frase en que declara no copiarlo**, y lo copia **falso**: «*doce cerradas o registradas*» —hoy son once: `C-L.5` ABIERTA y `C-L.7` NO CERRADA— y «*SIGUE CERTIFICADA*». **Y añado lo que nadie vio: su puntero también es falso.** Dice «*lo da la clasificación VIGENTE de este mismo fichero, **más abajo***», y la clasificación vigente está en **L2059-L2191, ARRIBA**. **Tres defectos en un renglón.** Sexta recurrencia de la clase que `C-L.7` existe para cerrar | Retirar las dos afirmaciones copiadas y corregir la dirección del puntero. Tres líneas |
| **`DD-09`** | **GRAVE** | **A** | **`D105` sin propagar a tres sedes normativas**: doc 11 **L1200** (el discriminador «observable en el diario»), **L1215** (tabla de cardinalidad) y **L2572**, que siguen diciendo que `abandonada` retira el marcador, contra su gemela `X58` (L1633). Origen `BB1-03`+`BB1-05`. **Y consta a favor: `X55` y `X58` —los contratos de prueba de `F6`— SÍ están corregidos**, y ésa era la mitad que importaba | Propagar a las tres. **Y barrer la CLASE**: toda sede que afirme qué retira el marcador, no las ocho que `Y-02` enumeró |
| **`DD-10`** | **GRAVE** | **A** | **`X-S1–X-S9` es falso: son ONCE.** Verificado por mí con `grep -cE '^\| \`X-S[0-9]+\`'` → **11**, y `X-S10`/`X-S11` en L7799-7800. **Y el propio documento ya dictaminó esta cadena** en L10736-10739 y la retiró de §19 **dejándola intacta en §2.1**, que es la sede definitoria y la que gobierna la prueba de `D83` contratada para `F6` | Corregir §2.1 o remitir al comando que lo deriva |
| **`DD-11`** | **MEDIO** | **A** | **La mitad MUTANTE de la única prueba negativa «ANCLADA EN EL ÁRBOL» es TAUTOLÓGICA.** Verificado por mí estructuralmente y con **200 000** textos aleatorios: **0 contraejemplos**. El README promete «*un corpus distinto la mueve*». Origen `CC1-04`/`CC-03` | Mutar **una sola** de las dos cadenas gatillo, o llamar al evaluador sobre un fixture que sí pueda pasar. **Y corregir la fila del README**: es sexta condición de `O18` |
| **`DD-12`** | **MEDIO** | **A** | **`G-10` no DERIVA nada**, y es el aval con el que §5.2 se permite escribir el único cardinal que el documento se permite: comprueba **tres substrings literales** y **seis nombres escritos a mano**. Una **séptima** extensión de ficha dejaría «Son SEIS» caducado **con `G-10` en verde**. Origen `BB1-07`/`BB-13` | Derivar los seis del árbol, o retirar la excepción de §0 que `G-10` avala |
| **`DD-13`** | **MEDIO** | **A** | **La regla de titulares de §0 no tiene guardián**, verificado por mí (`grep -cniE 'titular\|regla de titulares'` sobre la batería → **0**), y sus instancias vivas: el censo de la familia `X` dice **CUATRO** poblaciones y hoy son **CINCO** (`X-O1`–`X-O13`, que el propio documento reconoce en L10736) · «Tres cosas cambian» sobre **cinco** rótulos (L1764) · §5.6 atribuye **dos veces** a `X52` una validación que `X52` no hace (L5403, L5563) · «DIECIOCHO» escrito en la frase que jura no escribirlo (L1260) · §19 copia cuatro cardinales en la frase que dice remitir (L10726-10736) · §11.9 afirma que §15.4 «*sigue llevando una fila por resolución*» y son trece de `O7` a `O19`, sin `O1`–`O6` (L8787). Origen `BB1`/`BB2`, adjudicados por `BB4` | **Un barrido sobre `^\*\*.*<cardinal>` y no sólo sobre `^#`** —es la observación de método de `BB1` y vale más que los hallazgos—, y una comprobación que lo ejecute. `AA` la declaró **deuda nunca barrida**, y sigue siéndolo |
| **`DD-14`** | **MENOR** | **A** | **Asimetría de procedencia**: el rótulo «literal de `O18`» que `O19` ordena reatribuir se corrigió en §11.8 (L8674) y **no en §11.7** (L8532), a 142 líneas. Y la proyección de `O17` (`DECISIONES` L741-844) **no enlaza a la sede** que la designa como su proyección (`grep -c owner` → 0), mientras la de `O19` sí. Origen `BB2-04`/`BB3-02` | Aplicar la misma corrección a los dos lados del par |
| **`DD-15`** | **MENOR** | **A** | **El README enumera un cierre de región que el código no aplica a la clase `tanda`**, y **dos párrafos contradictorios vivos** (`README.md` L73 y L78) **en la sección cuya nota L66-71 declara ese defecto corregido** («*Se retira el que había caducado, y queda uno solo*»: quedan los dos). **Tercera vida del mismo defecto.** Verificado por mí. Origen `CC1-05`/`CC1-06` | Retirar el párrafo caducado y añadir la excepción a la enumeración |
| **`DD-16`** | **MENOR** | **A** | **El punto de entrada apunta a una sede caducada**: `00-INDICE` L93-95 dice «*la siguiente acción exacta está **al final** de ese fichero*», y la vigente es la **PRIMERA de siete**, en L3321 de 4085. Quien lea «al final» llega a L3989, la anterior al documento 22. Verificado por mí. Origen `BB3-06` | Cambiar «al final» por «la primera», que es lo que la propia cabecera del checkpoint ya dice |

### 6.3 · DEL APARATO DEL GATE — el commit `5ed7a3b`

| id | sev | clase | qué es | **REMEDIO** |
|---|---|---|---|---|
| **`DD-17`** | **GRAVE** | **A** | **El commit del gate deja el árbol que juzga con un validador canónico en ROJO** —`T147` FALLIDA, `12/13`, RC=1— **y ensucia dos ficheros de evidencia**. **QUINTA recurrencia consecutiva**, contra una regla que el propio `00-INDICE` escribe (L115-121) y registra ya dos veces (L132, L134). **Y el remedio estaba escrito por `Y4`: lo ejecuté y funciona** (§3.2) | El commit del manifiesto lleva **el manifiesto, su fila en `00-INDICE.md` y la evidencia derivada reejecutada**. Cuatro ficheros en vez de uno. **Verificado: 13/13 y converge** |
| **`DD-18`** | **GRAVE** | **A** | **El manifiesto rotula «—sobre el árbol del GATE—» cifras que son de la CANDIDATA** (L37). El árbol del gate da 75 / 66 940. **TERCERA instancia de `U-02`→`X-06`, y `AA` la declaró ROTA hace un gate**, en el campo que el sobre manda mirar PRIMERO | El manifiesto es inmutable: **CORRIGENDUM**, que es la vía que el corpus ya usó dos veces y cuya regla §14 nació de esta clase. Acotar el titular de §2 **y** la resta de §6, diciendo de qué árbol habla cada una |
| **`DD-19`** | **MEDIO ESTRUCTURAL** | **A** | **`OBLIGATORIO − ASIGNADO = 0` sobre el árbol del gate es INALCANZABLE**, porque el remedio de `AA-01` hizo del manifiesto fila de su propio universo y cada fila publica su SHA-256 (§5.4). **Será verdad en todos los gates siguientes** | Una de tres, y las tres son de `F4`: rotular el árbol **candidato**; publicar las **dos** aritméticas; o que el derivador excluya de su barrido **el manifiesto en curso**. La primera cuesta una palabra |
| **`DD-20`** | **MEDIO** | **A** | **El corpus lleva DOS enunciados vigentes e incompatibles de la regla de clase `A`/`C`** —`AA` exige «sin commitear», `Z3` declara el commit irrelevante— y de cuál rija depende si un árbol defectuoso cuenta. Resuelto por mí en `D-3` contra la sede canónica | Fijar el enunciado en su sede —«El criterio del gate siguiente» del checkpoint— con la formulación de `Z3`, que es la que la sede y `O18` sostienen |
| **`DD-21`** | **MENOR** | **A** | **Nueve de las 38 comprobaciones no son propiedades del COMMIT** sino de un repositorio con historia, y sobre la materialización que la receta del sobre prescribe la batería da **29/38** (§3.3). No es defecto —falla cerrado— pero **ninguna sede acota lo que «38/38» certifica** | Una línea en el README: qué comprobaciones exigen `.git` y qué significa su ausencia |
| **`DD-22`** | **MENOR** | **A** | **`notas/CC2.md` L205 teclea mal el SHA-1 truncado del árbol candidato** («`91fe62d3691521…`» por «`91fe62d369152f…`»), en la columna abreviada de una fila cuya columna «recalculado» lleva el valor completo y correcto. **No es transcripción del sobre** —`CC2` embebe el sobre entero byte a byte 197 líneas más arriba—, pero es la clase exacta que mató al gate 4 | No abreviar huellas a mano en ningún informe. Si se abrevian, derivarlas con `cut -c1-N` |

**No sostengo, y lo digo:** las tres rutas equivocadas del encargo de `BB4` (`BB-22`). **No
recibí ese encargo y no puedo verificarlo.** Lo traslado como declarado por `BB4` y no
verificado por mí. Si es cierto, es la quinta de la serie `C-2`→`T-11`→`W-17`→`Z-10`.

### 6.4 · RECUENTO, DERIVADO DE LAS FILAS

```text
                 DEL OBJETO   DEL APARATO   TOTAL
  BLOQUEANTE          0             0          0
  GRAVE              10             2         12
  MEDIO               3             3          6
  MENOR               3             1          4
                 ─────────────────────────────────
                     16             6         22

POR CLASE
  A · coherencia interna / corregible dentro de `F4c`          **22**
  B · exige una decisión NUEVA del Owner                        **0**   ← §6.5
  C · resistencia a un actor privilegiado                        **0**   ← §6.6
```

### 6.5 · **¿HAY ALGUNA CLASE `B`? — NO, Y LO DECIDO EXPRESAMENTE, CANDIDATO A CANDIDATO**

El gate anterior determinó que no quedaba ninguna. **Soy exigente y examino los cuatro
candidatos que mi propio material produce. Los cuatro caen.**

1. **El octavo árbol (`DD-01`, `DD-02`).** ¿Exige que el Owner decida algo? **No.** El remedio
   está determinado y es del mismo tipo que `AA` ya ordenó para `AA-01`: **derivar el perímetro
   en vez de escribirlo**, que es literalmente lo que esta tanda declara haber hecho y dejó a
   medias. No reinterpreta ninguna resolución y no escribe una protección interna nueva:
   **corrige una que ya existe**.
2. **Las cinco promesas excesivas (`DD-03`, `DD-04`, `DD-11`, `DD-12`, `DD-02`).** Son la sexta
   condición de `O18`, y por eso son **exigibles**. Pero su remedio es **de resta**: escribir en
   el README lo que el código hace. `F4` puede hacerlo sin tocar una resolución.
3. **El punto fijo (`DD-19`).** Una regla del corpus es irrealizable. ¿Decide el Owner contra
   qué árbol muerde la regla de cierre? **No hace falta:** el manifiesto **ya declara su
   objeto** en su §1, y contra ese objeto la resta cierra a 0. Lo que falta es que el enunciado
   diga lo que el manifiesto ya hace. **`F4`.**
4. **`M-04` viva en su quinto gate.** ¿Reabre `O18`? **No, y es importante decir por qué.**
   `O18` ya declaró de sí misma que era **TRANSITORIA y explícitamente LIMITADA**, rechazó la
   alternativa (a) —retirar la garantía y dejar de medirla— y contrató (c) para `F6`. **Mi
   octavo árbol no descubre un riesgo que el Owner no haya aceptado: descubre que el perímetro
   con el que se mide está escrito, y eso es exactamente lo que `F4` puede arreglar.**
   Elevarlo sería pedirle al Owner que vuelva a decidir lo que ya decidió, y `O19` lo prohíbe.

> **NINGUNA DECISIÓN DEL OWNER QUEDA PENDIENTE. Los veintidós tienen remedio determinado
> dentro de `F4c`, y lo he escrito uno a uno.** Es la segunda vez consecutiva que se puede
> decir esto, y es información buena.

### 6.6 · **CLASE `C`: EJECUTADA POR MÍ Y NO CONTADA**

Reproduje la cadena de `CC3` sobre `docs/owner/.git/SEDE-VIGENTE.md`: Git rechaza la ruta en
todos los niveles y, con `mktree`/`commit-tree`, la receta del sobre **falla cerrado**
(`read-tree` rc=128, 0 rutas). **Ese ataque es `C` y NO lo cuento.** `O18` la declara NO
IMPLEMENTADA y la contrata para `F6`. **Contar `C` como `A` es lo que haría que la tanda
siguiente escribiera la protección diecinueve, y `X`, `AA` y el Owner lo prohibieron.**

**Y digo lo que eso NO me obliga a hacer:** no me obliga a rebajar `DD-01`. Mi ataque **no es
el de `CC3`**. Alcanza el commit, deja el árbol limpio y el ancla lo reproduce idéntico. **Es
`A`.**

---

## 7 · ¿CIERRA EL SISTEMA INSTANCIAS O CLASES? — Y SI ESO BASTA PARA NEGAR

**La pregunta que heredo tiene dos mitades y las contesto por separado, porque la respuesta no
es la misma.**

### 7.1 · Lo que el cuarto gate determinó, y que CONFIRMO

`AA` determinó que **la causa esencial de cuatro fracasos —verificación anclada dentro del
objeto verificado— ya no es la causa**, porque los tres remedios de `X` están aplicados y
funcionan. **Lo confirmo, y lo confirmo por replicación, que es la forma más fuerte
disponible:** siete lectores independientes recibieron el mismo sobre —cuatro lo embebieron
byte a byte— y sus derivaciones reproducen; yo las rehíce sin fiarme de ninguno; el emisor y el
derivador son idénticos en los dos commits; la sede canónica es byte-idéntica en los dos; la
receta reproduce los dos digest sin ejecutar el emisor. **Y la vía por la que murió el cuarto
gate —la transcripción a mano— está cerrada de raíz y lo medí.** Eso es real y es nuevo.

### 7.2 · La tesis de `BB4`: **ES CIERTA, Y LA PRUEBO CON UN CASO QUE `BB4` NO TENÍA**

`BB4` sostiene que lo que falla hoy es que **el sistema cierra INSTANCIAS y no CLASES**, y que
la corrección se aplica «*con la forma sintáctica exacta del contraejemplo, y no con su
extensión semántica*». **Verifiqué sus cuatro casos y los cuatro se sostienen.** Y añado el
mío, que es el más limpio de los cinco gates porque el remedio y el superviviente están **en la
misma línea de código**:

```text
`Z-05` (doc 25) dijo:  «_EXCLUIDO excluye `__pycache__` POR NOMBRE DE DIRECTORIO, y un
                        directorio admite cualquier cosa. Una lista de lo que se excluye
                        NO PUEDE CADUCAR POR OMISIÓN: lo que olvide nombrar se queda DENTRO»
LA TANDA RESPONDIÓ:     retiró `__pycache__` del regex.
     _EXCLUIDO = re.compile(r"(?:^|/)\.git(?:/|$)|\.py[co]$")
                                    └── mitad 1 ────┘└─ mitad 2 ─┘
`CC1` encontró la MITAD 1 (`.git` a cualquier profundidad) — y `CC3` la rebajó a `C` porque
       no alcanza el commit
`DD`  encuentra la MITAD 2 (la extensión) — **y SÍ alcanza el commit, y el ancla no la ve**

LAS DOS MITADES SON EL MISMO ARGUMENTO QUE `Z-05` ESCRIBIÓ, EN LA MISMA LÍNEA, Y LA TANDA
BORRÓ EXACTAMENTE LA PALABRA QUE EL CONTRAEJEMPLO NOMBRABA.
```

Y lo mismo con el resto, verificado por mí sede a sede:

```text
`Y-05` dijo: TRES CITAS ENTRECOMILLADAS con cero en la sede
  → se barrieron las comillas. `DD-06` sobrevive porque va en CURSIVA
`Y-09` dijo: §11.8 escribe «CI o» bajo rótulo literal
  → `DD-05` sigue ahí. Ni se movió: sólo cambió de número de línea
`Y-02` dijo: `D105` sin propagar a OCHO sedes, y las nombró una a una
  → se corrigieron las ocho. `DD-09` sobrevive en TRES que no estaban en la lista
`V-03` dijo: el rótulo «literal de `O18`» de §11.8
  → se corrigió §11.8. `DD-14` sobrevive en §11.7, a 142 líneas
`AA-01` dijo: `docs/owner/` entra como RUTA LITERAL
  → se convirtió en ZONA BARRIDA, y eso ABRIÓ `DD-19`, el punto fijo
```

**MI MEDIDA, y no es una impresión:** de mis 22 hallazgos, **catorce son reincidencias de
clases ya dictaminadas en los documentos 19-25**, y de ellas **al menos nueve tenían el remedio
literalmente ESCRITO por el gate anterior**. `DD-17` lo lleva al extremo: el remedio cabía en
una línea, estaba medido, estaba publicado, **y lo ejecuté yo para comprobar que funcionaba**.

**Y hay una razón estructural, no moral, y por eso el patrón no se corrige solo:** quien
corrige recibe una lista de sedes con su línea, y esa lista es **exhaustiva del hallazgo** y
**no exhaustiva de la clase**. Cerrar la lista es verificable y barato; derivar la clase es
caro y nadie lo comprueba. **El incentivo del corrector está alineado con cerrar el hallazgo, y
el gate siguiente mide la clase.** Por eso el coste marginal de encontrar la puerta siguiente
sigue plano, y por eso yo, sin ser especialista y en un solo experimento, encontré la otra
mitad de un regex que cinco gates habían mirado.

### 7.3 · **Y AQUÍ AÑADO LO QUE EL CUARTO GATE NO PODÍA SABER: LA CIRCULARIDAD SE HA MOVIDO OTRA VEZ**

Ésta es mi aportación al diagnóstico, y sale de §4.

```text
gates 21-23   la circularidad estaba en `HEAD`: la batería comprobaba «intacto» contra
              referencias que vivían dentro del árbol
gate 24       `X` la localizó movida al EMISOR: producía un sobre idéntico al honesto sobre
              un corpus corrupto. `O18`/`O19` y la tanda la cerraron ahí
gate 25       `AA` la localizó en la ENTREGA: el canal, que es una persona. El gate 5 la cerró
              sacando el sobre a un fichero, y **funcionó**
**gate 26**   **ESTÁ EN EL PERÍMETRO.** El sobre ancla un DIGEST; el digest se calcula sobre un
              UNIVERSO; el universo lo deriva un programa cuyo perímetro **vive dentro del
              árbol auditado y excluye POR NOMBRE**. Quien elige el nombre elige lo que el
              ancla ve — **y lo demostré con el digest saliendo bit a bit idéntico**
```

**Los cuatro remedios fueron correctos. Ninguno fue suficiente, porque cada uno cerró el punto
donde la circularidad estaba y no la propiedad que la produce: que la definición de QUÉ se
verifica sea un objeto del árbol verificado.** Ésa es la clase, y es la que nadie ha cerrado.

### 7.4 · **¿BASTA PARA NEGAR LA CERTIFICACIÓN, O ES DEUDA QUE SE REGISTRA Y SE SIGUE?**

**Contesto las dos cosas, y son distintas.**

> **«El sistema cierra instancias y no clases» es un hallazgo de MÉTODO, y por sí solo NO
> bastaría para negar la certificación. Sería deuda: se registra, se nombra y se sigue.**
> Un expediente que negara por disciplina y no por medición estaría haciendo exactamente lo
> que este corpus prohíbe —juzgar por impresión— y además sería injusto: la tanda arregló lo
> que se le señaló, en la forma en que se le señaló, y en la mitad `B` lo hizo bien.

> **LO QUE NIEGA LA CERTIFICACIÓN NO ES EL MÉTODO: ES SU PRODUCTO, Y ES UNA MEDICIÓN.**
> Existe hoy, sobre el árbol auditado, un commit que declara `F4c` cerrada y `F5` autorizada,
> que pasa `38/38` y `13/13`, que deja `git status` vacío, que **no entra en el universo, ni en
> el manifiesto, ni en el reparto, ni en `EXCLUIDOS_IV`**, y que **produce el digest que el
> sobre de este gate publica, bit a bit**. Eso es la afirmación `A` **no demostrada**, medida
> por mí y con su control positivo en rojo. Y son **dos de las seis condiciones que el propio
> Owner impone** para cerrar `M-04` en `F4c` las que fallan: la primera y la sexta.

**La distinción importa, y la dejo escrita para el gate siguiente:** si en el gate 6 el
perímetro se deriva de verdad y las cinco promesas dicen lo que el código hace, **entonces «se
cierran instancias y no clases» pasa a ser deuda registrada y el trabajo sigue** — porque para
entonces se habrá cerrado, por primera vez, una clase entera en vez de su instancia.

---

## 8 · REFUTACIONES CONTRA MIS PROPIAS CONCLUSIONES

El encargo pide al menos **tres**. Intenté **seis**. **Una cayó, y cayó CONTRA MÍ en la
dirección que empeora mi propio hallazgo**; dos cayeron a medias y me obligaron a acotar; tres
no cayeron. **Publico las seis, cayeran o no.**

### `RF-1` · **CAYÓ, Y CONTRA MÍ: «`DD-01` exige `git add -f`, luego es un acto privilegiado y es clase `C`»**

Es la refutación más fuerte que existe contra mi octavo árbol, y la construí en serio: si el
único camino al commit exige forzar `.gitignore`, alguien podría sostener que `.gitignore` es
una barrera y que saltarla es privilegio. Lo medí.

```bash
printf '…' > docs/owner/S.pyc ; git add -A ; git status --porcelain
   →  (VACÍO).  `.gitignore` L1-2 lleva `__pycache__/` y `*.pyc`: un `add -A` NO lo recoge
```

**Hasta aquí mi refutación iba ganando.** Y entonces miré la otra mitad del regex:

```text
`_EXCLUIDO` excluye  `\.py[co]$`   →  `.pyc` **Y** `.pyo`
`.gitignore` lleva   `*.pyc`       →  `.pyc` **y NADA de `.pyo`**
```

```bash
printf '…' > docs/owner/ADS-OWNER-RATIFICACION.pyo
git add -A                       →  A  docs/owner/ADS-OWNER-RATIFICACION.pyo   ← SIN `-f`
git commit                       →  git status --porcelain  →  (VACÍO)
comprobar-correccion-gate-de-cierre.py  →  **38/38 en verde · EXIT=0**
derivar-universo-obligatorio.py --rutas →  **74** rutas
DIGEST con la receta del sobre          →  18f50dabfd46cbd5e8129cc7e205714091226b914f8223186f88d61fee84c8b4
EL DIGEST QUE EL SOBRE PUBLICA          →  18f50dabfd46cbd5e8129cc7e205714091226b914f8223186f88d61fee84c8b4
```

> **MI REFUTACIÓN CAYÓ, Y EL HALLAZGO SALE PEOR DE LO QUE ENTRÓ.** La variante `.pyo` **no
> necesita `-f` ni ninguna otra cosa**: la recoge un `git add -A`, que es el acto más ordinario
> que existe en Git. **Y lo que separaba el agujero de un flujo ordinario era `.gitignore`**,
> que no es un control de acceso, que nadie declara como barrera —`grep gitignore` sobre la
> batería devuelve **0**— y que **el perímetro y el `.gitignore` no coinciden**: el perímetro
> excluye dos extensiones y el `.gitignore` tapa una.
>
> **Lo publico porque me obliga a subir mi propia estimación**, y porque es la clase de detalle
> —una letra de diferencia entre dos listas escritas a mano— que este expediente lleva cinco
> gates persiguiendo.

### `RF-2` · **CAYÓ A MEDIAS: «`DD-04` (`G-23`) es tan sigilosa como `DD-01`»**

Si el ataque a `NORMATIVO` pudiera esconderse de `git status`, el emisor emitiría sobre un
árbol con material APROBADO reescrito. **Lo medí y NO se esconde:**
`git status --porcelain` → ` M docs/rediseno/00-MAPA.md`. **El emisor se negaría a emitir.**

**Cae a medias, y me obliga a acotar:** el ATAQUE de `DD-04` tiene un atenuante real y lo hago
constar. **Lo que NO tiene atenuante es la PROMESA** —«lo normativo intacto» sobre 4 de 14—,
que es sexta condición de `O18` y se queda GRAVE. **Y hace más fuerte a `DD-01` por contraste:
ése SÍ deja el árbol limpio.**

### `RF-3` · **CAYÓ A MEDIAS: «`DD-01` no es nuevo: es `Z-05` reabierto, luego es reincidencia y no hallazgo»**

**Verdad en la clase, y lo declaro:** es exactamente la clase `Z-05`≡`Z1-03`, y el propio
comentario del código escribe el argumento que lo condena. **No reclamo una clase nueva.**

**Falsa en lo que decide.** `Z-05` se graduó MEDIO y su ataque **no alteraba el digest porque
nadie lo midió**; `W-04` lo dejó «CERRADO EN SU FORMA, NO EN SU CLASE». **Lo que aporto y nadie
había medido son las dos propiedades que cambian su severidad:** que **alcanza el commit** por
un `add -A` ordinario, y que **el digest del sobre sale bit a bit idéntico**. Con eso deja de
ser un defecto de higiene del corpus y pasa a ser una **ceguera del ancla externa**, que es la
pieza que `O18(b)` adoptó para poder cerrar `F4c`.

### `RF-4` · **NO CAYÓ: «El gate 5 es INVÁLIDO, como el 4»**

La construí porque es la conclusión más consecuente que podía alcanzar, y porque el gate
anterior murió exactamente ahí.

```text
disparador (i)  · diferencia ENTRE SOBRES
                  el sobre vive en un fichero externo. Extraje los CUATRO bloques embebidos y
                  los hasheé: 190 líneas y `906b74f7…9070` los cuatro, idénticos al fichero.
                  Los tres restantes publican ese mismo digest.  →  CERO diferencias
disparador (ii) · diferencia entre el SOBRE y el ÁRBOL
                  recalculé los 21 campos de los dos commits, los dos digest de universo con
                  la receta y sin ejecutar el emisor, los cuatro digest de la sede con su
                  `awk`, y las dos refs contra el remoto real.  →  CERO diferencias
```

**NO CAE, y cae del lado contrario: el remedio del gate 5 funciona exactamente donde el gate 4
murió.** El único candidato que encontré —el SHA-1 mal tecleado de `CC2` L205— es una
abreviatura ornamental en una tabla resumen, en la misma fila que publica el valor completo y
correcto, y en un informe que embebe el sobre entero byte a byte 197 líneas más arriba.
**Declarar inválido por eso sería inventar un disparador que ninguna sede define.**

### `RF-5` · **NO CAYÓ: «Se audita el árbol del GATE, y entonces la resta es 1 y la cobertura falla»**

Sería la vía más cómoda para negar, y por eso la ataqué. Si el objeto fuera `5ed7a3b`,
`OBLIGATORIO − ASIGNADO = 1` y la regla de cierre mordería sola.

**NO CAE**, por el manifiesto §1 —«**Objeto del reparto** · `COMMIT CANDIDATO 8c9ca9c…`»—, por
la columna del sobre rotulada «**CANDIDATA (COMMIT AUDITADO)**», y por la doctrina que `U`,
`X` y `AA` establecieron y que reproduje ejecutando los validadores sobre los dos árboles.
**Y lo dejo dicho contra mi propia comodidad: mi veredicto NO se apoya en la cobertura.** Las
dos restas cierran a 0 contra el objeto auditado, y lo hago constar a favor de la tanda.

### `RF-6` · **NO CAYÓ: «`ASIGNADO − LEÍDO = 0` es una resta que no puedo verificar, luego no debería publicarla»**

Me la hice porque es la resta que hundió el gate anterior y porque publicarla es lo más
parecido a una absolución que hay en mi adjudicación.

**Lo que verifiqué:** que los SHA-256 y los recuentos que las dos cadenas declaran **son los
del árbol**, y contrasté decenas de sus citas contra fichero y línea sin encontrar una falsa
salvo el punto de §2.2. **Lo que NO puedo verificar: que leyeran.** **NO CAE la resta, pero cae
mi derecho a publicarla sin reserva**, y por eso va con ella en `D-5` y en §9: es **fiabilidad
medida, no lectura probada**. Lo único que en esa resta es prueba y no confianza son **mis tres
fuentes, que leí yo**.

### 8.7 · Qué cambiaron estas seis en mi adjudicación, sin adorno

```text
· `DD-01` SUBE: la variante `.pyo` no necesita `-f`. Mi propia refutación me obligó a
  agravarlo, y es el movimiento que más pesa en el veredicto                        (RF-1)
· `DD-04` queda ACOTADO: su ataque tiene atenuante; su promesa no                    (RF-2)
· `DD-01` deja de reclamar clase nueva y se declara reincidencia de `Z-05` con dos
  propiedades nuevas medidas                                                        (RF-3)
· la invalidez queda DESCARTADA con su medición, no con una impresión               (RF-4)
· el veredicto queda EXPRESAMENTE desligado de la cobertura                         (RF-5)
· la resta `ASIGNADO − LEÍDO = 0` se publica CON su reserva                         (RF-6)
```

**Cuatro de los seis movimientos van contra la comodidad de mi propia posición.**

---

## 9 · LO QUE NO HE PODIDO COMPROBAR, SIN ADORNO

**Una adjudicación que no publica su hueco vale menos que la mitad. Éste es el mío.**

1. **NO he leído el documento 11 (11 504 líneas) con mis ojos.** Lo leyeron `BB1` y `BB2`. Abrí
   y verifiqué **las sedes concretas** de cada hallazgo que sostengo —unas veinte— y acerté en
   todas. **Ningún ojo único ha recorrido ese fichero entero en este gate**, y el manifiesto lo
   declara por delante. Un defecto fuera de esas veinte sedes se me escapa.
2. **NO he leído `DECISIONES-Y-CONTRADICCIONES.md` (1 260) ni la batería (3 621) ni el
   derivador (703) ni el emisor (688) como documentos.** Son lote de `BB3`, `CC1` y `CC2`. De
   los dos primeros abrí y **ejecuté** las regiones que sostienen lo que adjudico; **el emisor
   NO lo ejecuté ni lo leí**: sólo recalculé su SHA-256 en los dos commits.
3. **NO puedo probar que los siete leyeran lo que declaran** (§`RF-6`). Es fiabilidad medida.
4. **NO he verificado el encargo de `BB4`** y por tanto no sostengo `BB-22`, sus tres rutas
   equivocadas. Lo traslado como declarado y no verificado.
5. **NO ataqué `G-02`–`G-09`, `G-11`–`G-21`, `G-24`–`G-28`, `G-30`–`G-32` con contraejemplos
   propios.** Reproduje los de `CC` sobre `G-23`, `G-26`, `G-29`, `G-33` y añadí los míos sobre
   `G-29` y el perímetro. **Que la batería caiga por tres puertas no significa que sólo haya
   tres: significa que no miré las otras.**
6. **NO he ejecutado ni una sola de las pruebas que el corpus describe.** Las 46 filas `X`, las
   18 ventanas `W`, las 11 `X-S`, las 13 `X-O`, las 8 `X-A`–`X-H`: **todo es contrato escrito,
   ninguno se ha ejecutado**, y lo dice el propio corpus. Es el hecho central que ninguna
   cantidad de hallazgos coherentes sustituye.
7. **NO he adjudicado uno a uno los 36 hallazgos del documento 25.** Verifiqué los que tocan mi
   materia; el resto lo tomo de `BB4` y `CC3`, que sí los adjudicaron en sus focos.
8. **NO he probado** enlaces simbólicos, permisos, nombres Unicode confusables, submódulos,
   condiciones de carrera, ni atributos de `.gitattributes` distintos de los que `Z-E7` cerró.
9. **La sede canónica del Owner NO es verificable contra nada externo, y lo declara ella
   misma.** Recalculé sus cuatro digest y son idénticos en los dos commits. **Eso prueba que el
   texto no cambió entre el commit auditado y lo que recibí fuera del árbol. NO prueba que sea
   el que el Owner emitió.** Sigue vigente hasta el verificador externo de `F6`.
10. **Los SHA-256 del emisor y del derivador que verifiqué NO prueban que los binarios que
    corrieron fueran ésos.** El propio sobre lo retira (`Z-11`) y yo no lo recupero.
11. **NO sé si la arquitectura de `F4c` es buena.** Sé qué puede pasar por esta batería y por
    este sobre sin que se note, y sé qué promete el instrumento y qué entrega. **No juzgo el
    diseño, y no lo insinúo.**
12. **Reproducibilidad:** todo se midió con **Python 3.12.14** (shim) y `git` sobre WSL2. No
    probé otro intérprete ni otro sistema de ficheros, y el comportamiento de `os.walk` ante
    sufijos y el de `git add` ante `.gitignore` son exactamente lo que sostiene `DD-01`.

---

## 10 · VEREDICTO

**El gate 5 es VÁLIDO** —lo decido en §5.6, medido y no supuesto— y por tanto **produce
veredicto**. Emito el mío.

### 10.1 · Lo que consta A FAVOR, y va primero porque es verdad y porque no es cortesía

**Verificado por mí, no aceptado de nadie:**

```text
· EL REMEDIO DEL GATE 5 FUNCIONA DONDE EL GATE 4 MURIÓ. El sobre salió del repositorio
  auditado y dejó de transcribirse: cuatro bloques embebidos byte a byte, siete digest
  correctos, CERO divergencia. La causa exacta de la invalidez anterior está cerrada DE RAÍZ
· LOS 21 CAMPOS DEL SOBRE REPRODUCEN, y los DOS digest de universo con la receta publicada y
  SIN ejecutar el emisor. Las dos refs remotas apuntan a los dos commits, contra el remoto real
· `AA-01` ESTÁ CERRADO Y GENERALIZA: `docs/owner/` se barre entero, y un segundo documento
  `.md` del Owner hace crecer el universo y cambiar el digest. El remedio que `AA` determinó
  está hecho
· `AA-05` ESTÁ CERRADO: el campo 14 publica un NOMBRE y no un rol
· EL GATE NO TOCÓ `verificacion/` después de publicar el manifiesto: mismo SHA-256 de emisor y
  de derivador en los dos commits. `git diff --stat` entre ellos: UN fichero
· LA CANDIDATA PASA 13/13 Y `T147`, y NO ensucia un byte
· LAS DOS RESTAS CIERRAN A 0 contra el objeto auditado, y las 74 filas del manifiesto casan
  sin una discrepancia de SHA-256 ni de líneas. `C-L.5` NO se reabre por cobertura
· LA FILA DEL PROPIO DERIVADOR —la que el sobre manda mirar PRIMERO— es IDÉNTICA en los dos
  árboles: esa reincidencia NO se repite
· NINGUNO de mis veintidós es BLOQUEANTE. NINGUNO exige arquitectura nueva.
  NINGUNO vuelve al Owner
· EL DISEÑO NO HA CAMBIADO, y `O19` sigue siendo el remedio correcto, implementado sin
  escribir una sola protección interna nueva, que es lo que `X`, `AA` y el Owner ordenaron
```

**Ésta sigue siendo una candidata sólida, y el trabajo debe SEGUIR.**

### 10.2 · Y aun así

# F4c ES INSUFICIENTE PARA F5

**`F4c` NO se cierra. Sigue ABIERTA. `F5` NO queda autorizada. NO he corregido nada.**

### 10.3 · Las razones. **La primera basta por sí sola, y es una medición.**

**1 · `A` —COHERENCIA INTERNA— NO ESTÁ DEMOSTRADA, Y LO MEDÍ YO CON EL OCTAVO ÁRBOL.**
Existe un commit ordinario que **añade al árbol auditado un documento que declara `F4c`
CERRADA, `F5` AUTORIZADA y `M-04` SUPERADA**, que se crea con un `git add -A` **sin ningún
flag**, que deja `git status --porcelain` **vacío** —de modo que el emisor emitiría sobre él—,
que pasa la batería adversarial en **38/38** y la del kernel en **13/13**, que **no entra en el
universo obligatorio** (74, sin cambio), **ni en el manifiesto, ni en el reparto, ni en
`EXCLUIDOS_IV`**, y que produce, con la receta que el propio sobre publica, un **digest de
universo BIT A BIT IDÉNTICO al que este gate ancla**. Con su control positivo en rojo. **`M-04`
sigue viva, en clase `A`, en su quinto gate.**

**2 · LA SEXTA CONDICIÓN QUE EL OWNER IMPONE PARA CERRAR `M-04` EN `F4c` NO SE CUMPLE.**
`O18`, leída íntegra en su sede canónica: *«ninguna promesa de seguridad superior a la
realmente entregada»*. **Cinco promesas publicadas que el árbol no sostiene** (§3.6), cuatro
con control positivo mío: el perímetro «ya no se escribe» y está escrito · «lo normativo
intacto» sobre 4 de 14 ficheros · la única prueba negativa «anclada en el árbol» con la mitad
mutante **tautológica** · un cardinal avalado por una comprobación que «lo DERIVA» y no deriva
nada · y una segunda sede del Owner que «sin enlace es ROJA» y **es verde en todo commit**.
**De las seis condiciones del Owner fallan dos: la primera y la sexta.**

**3 · EL APARATO DEL PROPIO GATE INCUMPLE, POR QUINTA VEZ CONSECUTIVA, UNA REGLA CUMPLIBLE
CUYO REMEDIO DE UNA LÍNEA EJECUTÉ Y FUNCIONA.** El commit del gate deja `T147` en rojo,
`12/13`, y ensucia dos ficheros de evidencia. Una fila en `00-INDICE.md` lo pone en verde; una
reejecución más da **13/13** y converge. **No es un dilema estructural: es incumplimiento de
una orden escrita, medida y publicada por el dictaminador del gate anterior.**

**4 · Y LA REINCIDENCIA MÁS ELOCUENTE: el manifiesto rotula «—sobre el árbol del GATE—» cifras
que son de la candidata**, en el campo que el sobre manda mirar **PRIMERO**, y `AA` declaró esa
reincidencia **ROTA** hace exactamente un gate.

**5 · LA CIRCULARIDAD NO ESTÁ CERRADA: SE HA MOVIDO POR CUARTA VEZ, Y AHORA ESTÁ EN EL
PERÍMETRO.** El sobre ancla un digest; el digest se calcula sobre un universo; el universo lo
deriva un programa cuyo perímetro **vive dentro del árbol auditado y excluye POR NOMBRE**.
**Quien controla el nombre controla lo que el ancla ve**, y lo demostré con el digest saliendo
idéntico. Los cuatro remedios anteriores fueron correctos y ninguno cerró la propiedad que los
produce: que la definición de QUÉ se verifica sea un objeto del árbol verificado.

### 10.4 · Lo que expresamente NO fundamenta este veredicto

```text
· NO falla por `C`. Ejecuté yo el ataque de clase `C` —`docs/owner/.git/…`, con `mktree` y
  `commit-tree`— y la cadena de anclaje FALLA CERRADO. `O18` la declara NO IMPLEMENTADA y la
  contrata para `F6`. NO LO CUENTO, y contar `C` como `A` es lo que haría que la tanda
  siguiente escribiera la protección diecinueve
· NO falla por COBERTURA. `OBLIGATORIO − ASIGNADO = 0` contra el objeto auditado, con las 74
  filas verificadas por mí; `ASIGNADO − LEÍDO = 0`. `C-L.5` no se reabre por nada que yo traiga
· NO falla porque el GATE sea inválido. Lo decido VÁLIDO en §5.6, con los dos disparadores
  medidos, y contra la vía más cómoda para negar
· NO falla por el EMISOR, ni por el DERIVADOR como programas: los dos son idénticos en los dos
  commits y la receta reproduce. El derivador falla cerrado ante lo que sabe mirar
· NO falla porque quede arquitectura por inventar. NINGUNO de los veintidós es BLOQUEANTE
· NO falla por DISCIPLINA. «Cerrar instancias y no clases» es un hallazgo de MÉTODO y, por sí
  solo, sería DEUDA que se registra y se sigue (§7.4). Lo que niega es su PRODUCTO, medido
· NO resuelvo NADA por mayoría. Fui contra los tres relevos que midieron la resta en 1, contra
  `CC3` en su §3.4, contra `CC1` en la clase de su ataque, contra `BB2` sobre la red, contra
  `BB4` en la palabra «imposible», y contra mí mismo en `RF-1`
```

### 10.5 · CLASIFICACIÓN DE CADA HALLAZGO SOSTENIDO

```text
CLASE `A` · corregible autónomamente por el coordinador, sin decisión nueva      **22**
            DD-01 … DD-22.  El remedio concreto de cada uno está escrito en su
            fila de §6.2 y §6.3, uno por uno, y ninguno excede a `F4c`

CLASE `B` · exige una decisión del Owner que no se deduzca de `O17`/`O18`/`O19`   **0**
            Examiné los CUATRO candidatos que mi propio material produce y los
            cuatro caen, uno a uno, en §6.5. **NO formulo ninguna pregunta al
            Owner, y justifico no formularla.** Es la segunda vez consecutiva

CLASE `C` · trabajo futuro contratado, no exigible en `F4c`                        **0**
            reportados y NO contados: el ataque de `CC1-01`, que ejecuté y que hace
            fallar cerrado la cadena de anclaje. El VERIFICADOR EXTERNO DEL CONTROL
            REPO sigue contratado, completo y sin implementar, para `F6`
```

**LOS CUATRO REMEDIOS QUE CIERRAN LO QUE MÁS PESA, uno por línea:**

```text
DD-01  excluir por NATURALEZA y no por nombre —`.git` anclado a la RAÍZ de la ruta relativa,
       evaluado sobre la RUTA y no sobre el nombre desnudo del directorio en los CINCO sitios
       de los DOS ficheros; y el bytecode por lo que ES, no por su sufijo—, y publicar en la
       salida toda ruta excluida, como `EXCLUIDOS_IV` ya hace con el componente (iv)
DD-02  que la admisión de `G-29` sobre `docs/owner/` se evalúe contra el CONTENIDO DEL COMMIT
       —`git ls-tree -r <commit> docs/owner/`— y no sólo contra lo que aún no está en `HEAD`
DD-17  el commit del manifiesto lleva el manifiesto, SU FILA EN `00-INDICE.md` y la evidencia
       derivada reejecutada. Cuatro ficheros en vez de uno. **Verificado: 13/13 y converge**
DD-03/04/11/12  reescribir las cinco filas del README para que digan LO QUE EL CÓDIGO HACE,
       en el mismo commit en que se corrija el código. Es la sexta condición de `O18`
```

### 10.6 · Lo que dejo dicho para el gate siguiente

**Un veredicto que no dice qué mediría distinto la próxima vez no sirve.**

1. **Que alguien busque la NOVENA puerta en el mismo sitio que yo:** el perímetro. Yo miré una
   de sus tres cláusulas. Nadie ha mirado los enlaces simbólicos, los nombres Unicode
   confusables, los submódulos ni los permisos.
2. **Que el barrido de titulares sea sobre `^\*\*.*<cardinal>` y no sólo sobre `^#`.** Es de
   `BB1`, vale más que sus hallazgos, y `AA` declaró esa clase **nunca barrida**.
3. **Que se ejecute el remedio antes de escribirlo.** `Y4` dejó el de `DD-17` escrito hace un
   gate y nadie lo corrió; yo lo corrí en dos comandos y funciona. **Un remedio que nadie
   ejecuta es una promesa, y las promesas son la sexta condición del Owner.**
4. **Que la regla de clase `A`/`C` se fije en UNA sede.** Hoy hay dos enunciados vigentes e
   incompatibles (`DD-20`), y de cuál rija depende si un árbol cuenta.
5. **Y que se mida la CLASE y no la lista.** Cinco gates han entregado listas de sedes
   exhaustivas del hallazgo y no de la clase. Es la propiedad del bucle, no un descuido, y
   sólo se rompe pidiendo la derivación en vez de la enumeración — que es, literalmente, lo
   que este corpus lleva escrito desde `P-08`.

---

```text
git status --porcelain   AL ABRIR   →  VACÍO   (primer comando de la sesión)
git status --porcelain   AL CERRAR  →  VACÍO   (último comando)
HEAD al abrir y al cerrar           →  5ed7a3b805c472934cea9a4027d61e8ef7be5a35, idéntico
RAMA                                →  gate/f4c-certificacion-5-20260831
FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ        ninguno
COMMITS · PUSH · PR · MERGE                                          ninguno
LABORATORIO   .../scratchpad/lab-DD/ — checkouts aislados
              (`read-tree`+`checkout-index`) y un `git clone --no-hardlinks` desechable,
              FUERA del repositorio. BORRADO al cerrar
SUBAGENTE `Agent`                                                    NO USADO
NINGÚN HALLAZGO SE HA CORREGIDO, y es deliberado: quien corrige no certifica
```

# F4c ES INSUFICIENTE PARA F5

**ADJUDICADOR `DD` · adjudicación cerrada. El veredicto es mío y nadie por encima lo revisa.**
