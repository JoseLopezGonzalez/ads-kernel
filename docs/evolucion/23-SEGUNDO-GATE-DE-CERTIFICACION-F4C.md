# SEGUNDO GATE INDEPENDIENTE DE CERTIFICACIÓN DE F4c — Y EL LÍMITE QUE EL CORPUS YA HABÍA DECLARADO

> **Veredicto del adjudicador `U`: `INSUFICIENTE PARA F5`.**
> **`F4c` NO se cierra y sigue ABIERTA. `F5` NO queda autorizada. Ningún hallazgo se ha
> corregido en esta pasada, y es deliberado.**
>
> **Y lo que hace distinto a este gate:** su adjudicador encontró, en **§11.4 del propio
> documento 11**, que el corpus **ya había declarado inalcanzable** el criterio contra el que
> tres gates consecutivos han fallado — y que **ningún gate lo había llevado al Owner**.

## 0 · Qué es este documento

Registro **LITERAL** de los tres dictámenes de un gate independiente sobre la candidata
`e3163967e2eb8191294ce79c25af7d10220a0944`, publicada en `review/f4c-o17-candidate-20260830`.
Los tres se transcriben **enteros y sin suavizar**, en §A, §B y §C. Lo escrito antes de §A lo
escribe el **coordinador**, que no es ninguno de los ocho y que **no ha juzgado nada**.

**No es una tanda de corrección.** El adjudicador no corrige lo que encuentra: adjudica y
devuelve.

## 1 · Los agentes

```text
REVISOR S      cadena `S1`·`S2`·`S3`·`S4`, contexto limpio, tramos DISJUNTOS
               S1  documento 11, L1-L5200, y §9 entera
               S2  documento 11, L5201-final · `O17` regla a regla
               S3  registro de decisiones · CHECKPOINT-ADS-NEXT
               S4  documento 22 AL FINAL — DICTAMINADOR. Rechazó 6 hallazgos de sus
                   relevos y rebajó 5, incluida la reatribución de un GRAVE al propio gate

REVISOR T      cadena `T1`·`T2`·`T3`, contexto limpio, tramos DISJUNTOS
               T1  la batería y su README — el ataque a `M-04`
               T2  el derivador · los dos manifiestos · el CORRIGENDUM · índice · operativo
               T3  documento 22 AL FINAL — DICTAMINADOR. Reprodujo por su cuenta siete
                   árboles defectuosos, bajó cinco BLOQUEANTES a GRAVE y rechazó cuatro
                   hallazgos de sus propios relevos

ADJUDICADOR U  recibió los dos dictámenes YA CERRADOS. Recalculó universo, asignaciones,
               lecturas, cobertura, severidades, recuentos y condiciones de cierre.
               Resolvió contra la FUENTE, nunca por mayoría. **Reprodujo SEIS árboles
               defectuosos, DOS de ellos que nadie había abierto nunca**

INDEPENDENCIA  ninguno de los ocho ha escrito F4, aplicado `D16`-`D107`, sido autor de
               ninguna corrección ni sido revisor en ningún gate anterior. `S` y `T` en
               paralelo y sin verse; `U` sin ver nada hasta que los dos cerraron
```

## 2 · La cobertura, y por qué NO es la razón del veredicto

```text
UNIVERSO DERIVADO           64 fuentes · 48 138 líneas · comando publicado y reejecutable
MANIFIESTO DE ASIGNACIÓN    commiteado SOLO, antes de que existiera ningún revisor
                            `c36d2ba` · SHA-256 c64a0ec4731e6d27751469e8…

OBLIGATORIO menos ASIGNADO  ∅   igualdad exacta de conjuntos, recalculada por `U`
ASIGNADO menos LEÍDO        ∅   12 asignadas · 12 leídas íntegras
AGOTAMIENTOS                52  los 52 pasan las DOS reglas: fila propia con `LEÍDO
                                ÍNTEGRO` y bytes idénticos. Verificados uno a uno
LAS 64 FILAS                0 discrepancias en líneas y en SHA-256

C-L.5                       SIGUE CERTIFICADA. Tercera vez consecutiva
```

El manifiesto de este gate es
[`F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md`](verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md),
y se enlaza aquí **en el mismo commit que publica el gate**, que es la regla que el índice
escribió y que este gate incumplió al commitearlo solo. Consta como hallazgo.

**Y aun así, el aparato de cobertura recibió el golpe más duro de este gate**: `U` **fabricó
una prueba de agotamiento** dentro del documento 22 —declarando «LEÍDO ÍNTEGRO» el documento 11,
10 275 líneas, por un revisor que no existe, con el SHA-256 correcto— y la batería dio **37/37
en verde**. La cobertura se sostiene **hoy**; lo que no se sostiene es que nada mecánico impida
falsificarla.

## 3 · El veredicto, y sus razones

```text
VEREDICTO   INSUFICIENTE PARA F5

1  `M-04` FALLIDA por TERCER GATE CONSECUTIVO, y `U` la reprodujo con sus manos: SEIS
   árboles defectuosos en verde con EXIT=0 y porcelain vacío. DOS son puertas nuevas:
   amputar una comprobación da «36/36 en verde» sin que la que falta aparezca en el
   informe —la batería no está en ningún inventario y su censo no se contrasta—; y una
   prueba de agotamiento FABRICADA pasa en verde

2  la FASE 0 que `O17` ordena crear NO ES EJECUTABLE tal como está escrita: su ENTRADA
   exige el identificador de una iniciativa que su propio GATE prohíbe abrir, y su SALIDA
   se escribe donde `estado/` todavía no existe. No exige decidir arquitectura: exige DECIR

3  la cadena de niveles sigue con un eslabón sin productor que NADIE declara: la Operativa
   se produce sólo en `INS-4`, y el bloque escrito para no tapar huecos declara el de la
   adopción y CALLA el idéntico de la migración

4  §18 EXCEDE a `O17` en sus cuatro filas `FASE 0`, dando a `SEG` una vía que la misma
   tabla niega dos filas más abajo

5  el manifiesto de este gate se contradice dentro de su propia §6, y el propio gate dejó
   un validador canónico en rojo: culpa del GATE, no de la tanda, y `U` lo midió en los
   dos árboles
```

```text
49 HALLAZGOS DISTINTOS      0 bloqueantes · 17 graves · 19 medios · 13 menores
CLASIFICACIÓN               A · corregible en F4c sin decidir arquitectura      48
                            B · DECISIÓN EXCLUSIVA DEL OWNER                     1  ← LA RAÍZ
                            C · trabajo futuro ya contratado                      0
LOS 69 DEL DOCUMENTO 22     adjudicados en §10 de la adjudicación de `U`
```

## 4 · LA RAÍZ, Y POR QUÉ ESTE GATE NO PIDE UNA DECIMOSEXTA PROTECCIÓN

El gate del documento 22 diagnosticó que cada corrección se aplicaba **al perímetro exacto de su
contraejemplo**. La tanda respondió con **quince protecciones sistémicas**. `U` las midió una a
una: **tres generalizan de verdad** —la polaridad de `G-01`, la igualdad exacta de `G-16`, y la
palabra «regresión», que ya no desactiva nada—, **tres son parciales** y **nueve siguen cerrando
sólo su perímetro**. Su prueba es que `G-26` ya no cede a una PALABRA **pero cede a una
ETIQUETA**, y que **el coste marginal de encontrar la puerta siguiente no está subiendo**.

**Y la causa no es un defecto de esta tanda ni de las anteriores.** Está escrita en el propio
corpus, en **§11.4 del documento 11**, y ninguno de los revisores de ningún gate la había visto:

```text
EL SUELO QUE QUEDA        si el runner miente, nada dentro del repositorio lo detecta.
ABIERTO, Y SE DICE        Cerrarlo exige un verificador EXTERNO al repositorio, y eso NO se
                          resuelve aquí. Se declara en vez de taparlo con una capa más de
                          comprobación interna, que sólo movería la circularidad de sitio.
```

**`M-04` como proposición universal NO es satisfacible desde dentro de F4.** La batería vive
dentro del repositorio que audita y decide si algo está «intacto» comparándolo contra
referencias que **también viven ahí**: `HEAD`, la revisión base, `kernel/.upstream-hash` y su
propio README. **Quien puede escribir el repositorio puede escribir la referencia, y también
puede amputar la batería.** Tres gates han fallado contra un criterio que el corpus **había
probado inalcanzable y dejado abierto**.

**Por eso la única clase `B` de este gate no es un hallazgo: es la raíz.** Su pregunta, con las
tres alternativas y el coste de cada una, está redactada palabra por palabra en **§13 de la
adjudicación de `U`**, más abajo en este mismo documento. Y `U` recomienda expresamente **cerrar
los 48 de clase A y NO escribir una decimosexta protección**: «el gate siguiente encontraría la
puerta diecisiete, y tendría razón».

## 5 · Lo que este gate SÍ ha cerrado

```text
· `R-04`, que dos gates consecutivos no habían cerrado, queda CERRADO CON MECANISMO:
  `[1,2)`→`W11`, `[2,4)`→`W17`, `[4,6)`→`W8`, sin hueco ni solape, las tres sedes de acuerdo
· la clase `B` del documento 22 quedó RESUELTA por `O17`, y su propagación es —en palabras
  del dictamen de `S`— «la más disciplinada del expediente»: 9 de las 12 reglas sin reserva,
  sede única, y CUATRO invocaciones byte-idénticas que `U` verificó
· `D107` NO excede a `O17`, y se declara derivada. Quien excede es §18, y es corregible
· `C-L.5` CERTIFICADA por tercera vez, sobre universo derivado
· §15.8 con bloque para todas las decisiones vigentes, y §0 REMITIENDO en vez de copiar
· `PN-17` y `PN-18` REGISTRAN sin ELEGIR, con sus nueve elementos
· `D1`-`D106` y `O1`-`O16` intactas; el material APROBADO protegido, verificado por refutación
· los 48 hallazgos de clase A son reales, baratos y de remedio determinado
```

---

# §A · DICTAMEN DEL REVISOR `S`, LITERAL

# DICTAMEN DEL REVISOR `S` — SEGUNDO GATE INDEPENDIENTE DE CERTIFICACIÓN DE F4c

Emitido por `S4`, dictaminador de la cadena `S`.
Repositorio `/home/jose/ads-kernel` · rama `gate/f4c-certificacion-2-20260830` · HEAD `c36d2ba707eed5ea24b9a13df6c4e6be49b68cc6`.

---

## 1 · IDENTIDAD, INDEPENDENCIA Y MODO

**La cadena.** `S1` leyó el documento 11 L1–L5200 y, por encargo, §9 entera. `S2` leyó el documento 11 L5201–final y verificó `O17` regla a regla. `S3` leyó el registro de decisiones y `CHECKPOINT-ADS-NEXT.md`. `S4` —yo— leo el documento 22 y **cierro el dictamen de `S`**. Ningún ojo único recorrió las 10 275 líneas del documento 11 seguidas; el manifiesto de asignación lo declara como coste asumido y lo repito aquí para que `U` lo pese.

**Qué NO he visto.** No he abierto `T1.md`, `T2.md` ni `DICTAMEN-T.md`. Existen en el directorio de notas —`ls` los muestra, con sus tamaños— y **no he abierto ninguno**. `S` y `T` trabajan en paralelo y sin verse. No he escrito una línea de este corpus, no he aplicado ninguna corrección, no participé en ningún gate anterior y no fui revisor `A`–`R` ni `P1`–`Q5`.

**No he usado el subagente `Agent`.** Todo el trabajo es mío, con `sed`, `grep`, `awk`, `git` y `python3` del shim.

**Sólo lectura, comprobado.**
- `git status --porcelain` **AL ABRIR: vacío**.
- `git status --porcelain` **AL CERRAR: vacío**.
- Ejecuté la batería `comprobar-correccion-gate-de-cierre.py` sobre el árbol real: es de sólo lectura y no ensució nada.
- Para reproducir `S3-04` sin tocar el repositorio **copié el árbol entero fuera de él** (`cp -a` al scratchpad), ejecuté allí `registrar_evidencia.py` —que sí escribe evidencia—, leí el diff y **borré la copia**. El repositorio real nunca se ensució: no hubo `git checkout --` que deshacer porque no hubo nada que deshacer.

---

## 2 · MANIFIESTO DE LECTURA DEL REVISOR `S`

**Las fuentes asignadas a `S` las fija** `/home/jose/ads-kernel/docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` (240 líneas, SHA-256 `c64a0ec4731e6d27751469e84cbcc33104bfe535c42efe4f98533f4d84a0b970`). Lo abrí y lo comprobé yo: su §4 «Reparto para LECTURA ÍNTEGRA» marca revisor **S** en las filas 2, 3, 4 y 12, y su §3 lo repite en el bloque «REVISOR S · 4 fuentes». **Son CUATRO, y no hay una quinta.**

| # | ruta | líneas | SHA-256 (recalculado por mí) | quién la leyó | cobertura | primera sección sustantiva | última sección sustantiva |
|---|---|---|---|---|---|---|---|
| 2 | `/home/jose/ads-kernel/docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 10275 | `47f924c9a2b5c36df111ca325f83c18f161db383a0b14acb44e84e8d0ddeddf3` | `S1` L1–L5200 (+§9 L6981–7543 y L6594–6720) · `S2` L5201–L10275 | **LEÍDO ÍNTEGRO** entre los dos, en tramos consecutivos declarados uno a uno. **Ni un tramo sin abrir** | `# 0 · Resumen ejecutivo`, L95 | `## \`C-L.5\`` · La condición de COBERTURA del próximo gate, L10156 |
| 12 | `/home/jose/ads-kernel/docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | 858 | `73e40d95cb2688ba1a83307ba27640400dd5a4fc8835c3eaf59173b99cb9cb02` | `S3` | **LEÍDO ÍNTEGRO** (22 tramos consecutivos) | `## 1 · Decisiones tomadas sin consultar`, L11 | `## 4 · Límites declarados de esta iteración`, L840 |
| 4 | `/home/jose/ads-kernel/docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 2782 | `e9078a7434d2a8a898d0d4edec242aee7fcac289c8f1dea3dfcf0f669c5b8a7a` | `S3` | **LEÍDO ÍNTEGRO** (21 tramos consecutivos) | `# CHECKPOINT — ADS NEXT`, L1 | `## Siguiente acción exacta — HISTÓRICA, anterior al documento 22`, L2688 |
| 3 | `/home/jose/ads-kernel/docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md` | 3478 | `3e2bdece758e6b69d6695bb52f20d21b910a123a27ac643845dbad75e8355f1c` | `S4` (yo) | **LEÍDO ÍNTEGRO** — tramos en §2bis | (en §2bis) | (en §2bis) |

**Los cuatro SHA-256 que recalculé coinciden byte a byte con los que publica el manifiesto de asignación.** Ninguna fuente asignada a `S` ha cambiado entre la emisión del manifiesto y mi lectura.

### Anclas — dos regiones separadas por fuente

**Documento 11** (`S1`, región inicial · `S2`, región final):
- L671-672 (§2.6.1): `` abierta(tx)  ≡  ∃ `preparada` DURABLE con ese `tx` ``
- L7344 (§9.6): `` **UN SOLO CONTRATO, INVOCADO CUATRO VECES.** Es la regla 6 de `O17` ``

**Registro de decisiones** (`S3`):
- L1: `# Decisiones, contradicciones y límites del kernel operativo`
- L658: `` ### `O17` · resolución del Owner sobre EL NIVEL ESTRUCTURAL Y SU PRODUCTOR — 2026-08-30 ``

**Checkpoint** (`S3`):
- L6-7: `> **Basta decir «Continúa»**: la siguiente acción exacta está al final`
- L2436: `EXCEPCIÓN EXACTA   deja de ser cierto que «kernel/operativo/ está intacto». Lo que hay es`

### LA RESTA

```
FUENTES ASIGNADAS A `S`            4
FUENTES LEÍDAS ÍNTEGRAS POR `S`    4
ASIGNADAS − LEÍDAS ÍNTEGRAS        0        ← CERO. Ninguna fuente asignada a `S` quedó sin leer.
```

**La reserva que `U` debe pesar, y la digo yo:** las cuatro están leídas íntegras, pero el documento 11 lo está **por dos lectores distintos con contextos separados**. Una contradicción cuyos dos extremos caen a los dos lados de L5200 no la ve ninguno de los dos. Yo he cruzado a mano los cruces que los dos señalaron (§8.0↔§18, §9.6↔§8.1, §9.2↔§9.3↔§8.3), pero **no puedo declarar que ese corte no haya ocultado nada**.

### 2bis · MI PROPIO LOTE — `22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md`

- Ruta: `/home/jose/ads-kernel/docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md`
- Líneas (`wc -l`): **3478**. SHA-256 recalculado por mí: `3e2bdece758e6b69d6695bb52f20d21b910a123a27ac643845dbad75e8355f1c`. **Coincide con el manifiesto.**
- **LEÍDO ÍNTEGRO**, en tramos consecutivos con `sed -n 'A,Bp'`: `1-180 · 180-400 · 400-640 · 640-900 · 900-1180 · 1180-1450 · 1450-1720 · 1720-2010 · 2010-2300 · 2300-2560 · 2560-2850 · 2850-3120 · 3120-3330 · 3330-3478`. Unión = `[1, 3478]`. **Ni un tramo sin abrir.**
- **Y lo abrí DESPUÉS de las notas de `S1`, `S2` y `S3` y después de reproducir sus hallazgos contra el árbol**, que es la regla de orden del encargo.
- Primera sección sustantiva: **`## 0 · Qué es este documento, y qué NO es`, L7**.
- Última sección sustantiva: **`## 14 · VEREDICTO`, L3350**, cerrada en L3478.
- **Ancla A (L3)**: `> **Veredicto del adjudicador \`R\`: \`INSUFICIENTE PARA F5\`.**`
- **Ancla B (L3313, región separada)**: `> **LA PREGUNTA EXACTA PARA EL OWNER**`

---

## 3 · `O17` PROPAGADA · MI VERIFICACIÓN, REGLA A REGLA

Leí `O17` directamente en su sede —`docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` **L657-L749**— y contrasté cada una de sus doce reglas contra §9.6 del documento 11, que es la sede única que `D107` designa, y contra las cuatro invocaciones de §8.1, §8.2, §8.3 y §8.4 y las cuatro filas de §18.

| regla `O17` | dónde vive hoy | mi veredicto |
|---|---|---|
| **1** · exactamente UNA por ejecución | §9.6 L7434 «CUÁNTAS VECES **EXACTAMENTE UNA por ejecución** (regla 1). Ni cero ni dos» · contraescenario `X-S6` | **CUMPLE** |
| **2** · antes de toda mutación canónica y de todo intento de elevarse | §9.6 L7428-7433 · §8.1 L6204-6210 · §8.2 · §8.3 L6599-6606 · §8.4 · §18 col. «entrada» («con CERO mutaciones canónicas hechas») · `X-S1` | **CUMPLE EN LA LETRA · NO SATISFACIBLE** — ver `S-03`: la SALIDA de la fase es una celda canónica y en `N` y en `A` no existe soporte donde escribirla |
| **3** · superar una ejecución anterior NO certifica la actual | §9.6 L7402-7404 «NO HEREDA» · las cuatro filas de §18 («ninguna heredada») · `X-S2` | **CUMPLE** |
| **4** · un nivel superior NO implica Estructural vigente | §9.6 L7405-7409 «NO SE DEDUCE DESDE ARRIBA» · §9.2 · `X-S4` | **CUMPLE** |
| **5** · si falla, BLOQUEA antes de mutar estado | §9.6 L7447-7451 · `X-S5` («una iniciativa abierta ya es estado») · las cuatro filas de §18 | **CUMPLE** |
| **6** · MISMO contrato y MISMO mecanismo | §9.6 L7344-7347 · §18 | **CUMPLE, y verificado mecánicamente por mí**: normalicé los cuatro nombres de macrocircuito en las filas `FASE 0` de §18 (L9442, L9445, L9450, L9453) y las cuatro son **byte a byte idénticas**. Un solo `gate:sistema-conforme` |
| **7** · el SUJETO lleva SEIS identificadores | §9.6 L7368-7391 | **CUMPLE EN EL CENSO · NO SATISFACIBLE** — conté seis, uno a uno, y mapean 1:1 con la regla 7. Pero el nº 2 es «**la iniciativa del macrocircuito, por su identificador**» y el gate prohíbe abrirla. Ver `S-02` |
| **8** · reutilizar sólo con TODAS las entradas y huellas idénticas | §9.6 L7412-7418 · `X-S3` | **CUMPLE** — «Demostrar no es afirmar» |
| **9** · cada ejecución emite SU declaración | §9.6 L7419-7422 · `X-S2` | **CUMPLE** — «también cuando toda la evidencia se reutilizó» |
| **10** · nunca copiar ni presumir vigente | §9.6 L7423-7426 | **CUMPLE** — «**ninguna condición las habilita**» |
| **11** · la cadena `Estructural → Operativa → Integrada → Completa` | §9.2 L7100-7137 | **CUMPLE**: la cadena y su REGLA DURA se conservan literales y no se reescriben |
| **12** · cada nivel con PRODUCTOR, EVIDENCIA, SUJETO, VIGENCIA e INVALIDACIÓN propios | §9.2 L7124-7137 · §9.6 L7392-7409 | **NO CUMPLE, y sólo un tercio está declarado.** El Estructural gana los cinco. La Operativa de la ADOPCIÓN se declara sin productor y se difiere honestamente. **La Operativa de la MIGRACIÓN tiene el mismo hueco y NO se declara** (`S-04`). Y el nivel **`completo`** no tiene productor: en su casilla hay una lista de pruebas (`S-07`) |

**El reparto `SIS` · `VER` · `PLT` · `SEG`** y la cláusula «el propietario del macrocircuito no puede sustituir a `SIS` y **DEBE EXIGIRLA**» están escritos **literalmente** en §9.6 L7350-7367 y repetidos verbatim en §8.1, §8.2, §8.3, §8.4 y §18, con `X-S7` y `X-S8` como contraescenarios y el caso `U5b` resuelto expresamente («`PLT` no certifica: exige»). **CUMPLE.**

### ¿La propagación es REAL o NOMINAL? — mi juicio

**Es REAL en la mayor parte, y es lo primero que hay que decir.** Nueve de las doce reglas se cumplen sin reserva. Hay **una** sede única y no cuatro; las cuatro filas de §18 son byte-idénticas, lo que yo mismo verifiqué y no acepté de nadie; los cuatro bloques de §8.x **invocan y no reescriben**; hay nueve contraescenarios `X-S1`–`X-S9` que atacan regla por regla; y el trabajo que la resolución NO cubre —la Operativa de la adopción— se difiere con propietario, fase y prueba en vez de ampliarse. **`gate:sistema-conforme` pasa de una aparición definitoria a veintitrés, todas remitiendo a §9.6.** Eso no es nominal.

**Y es NOMINAL en tres puntos concretos, que son mis `S-02`, `S-03` y `S-04`.** La FASE 0 está escrita como contrato completo pero **no es ejecutable tal como está escrita**: exige en su ENTRADA un identificador que sólo existe después de ella, y produce en su SALIDA una celda canónica que en `N` y en `A` no tiene dónde vivir. Y la regla 12 —la que cierra la cadena— sigue teniendo dos niveles sin productor, uno de ellos **sin declarar**.

**El resumen honesto: `O17` está propagada con más disciplina de la que este corpus ha mostrado en trece tandas, y la fase que crea no se puede ejecutar todavía.** Las dos cosas son ciertas a la vez.

---

## 4 · ¿EXCEDE `D107` A `O17`? — LA DISCREPANCIA ENTRE `S2` Y `S3`, RESUELTA CONTRA LA FUENTE

**No la resuelvo por mayoría ni por autoridad. La resuelvo abriendo las tres sedes, y la respuesta es que los dos tienen razón sobre objetos distintos y ninguno de los dos lo dijo entero.**

### 4.1 · Lo que dice `O17`, literal

`DECISIONES-Y-CONTRADICCIONES.md` **L728-L735**, bloque «El REPARTO DE RESPONSABILIDADES que el Owner decide»:

```
SIS   PROPIETARIO Y PRODUCTOR de la declaración Estructural
VER   produce el DOSIER o evidencia verificadora, SIN apropiarse de la decisión final
PLT   ejecuta la MAQUINARIA TÉCNICA cuando el contrato vigente le atribuya esa ejecución
SEG   conserva su capacidad de BLOQUEO cuando la estructura incumpla seguridad
```

**A `SEG` el Owner le da BLOQUEO. No le da participación en la ruta, ni vía, ni capa.**

### 4.2 · La fila `D107` del registro — `S3` TIENE RAZÓN

Abrí `DECISIONES-Y-CONTRADICCIONES.md` **L452**, la fila `D107`, entera. Dice literalmente:

> «`SIS` es propietario y productor; `VER` produce el dosier; `PLT` ejecuta la maquinaria cuando el contrato se la atribuya; **`SEG` conserva su bloqueo**.»

**Ni una palabra sobre vía 3.** La fila se abre con «**PROPAGACIÓN DE `O17`. No es una elección de F4c: es la materialización de una resolución del Owner, y se declara DERIVADA**», atribuye el descarte de (a) y (c) al Owner, y declara «Lo que F4 aporta aquí es **exclusivamente el reparto de la elección (b) por las sedes vigentes**».

> **Sobre la FILA `D107` del registro de decisiones: `S3` tiene razón. NO EXCEDE a `O17`.**

### 4.3 · La sede única, §9.6 — TAMPOCO EXCEDE

`11-ARQUITECTURA-INTEGRADA.md` **L7355-7359** («BLOQUEO POR SEGURIDAD ... **`SEG`** conserva íntegra su capacidad de BLOQUEO») y **L7440-7441**, bloque `PARTICIPANTES DERIVADOS` de la FASE 0:

> `` `SIS` productor y propietario · `VER` el dosier · `PLT` la maquinaria cuando el contrato se la atribuya · **`SEG` el bloqueo** ``

**§9.6, que es la sede que `D107` designa como única, tampoco le da vía a `SEG`.** Y los cuatro bloques de §8.1-§8.4 repiten esa misma frase verbatim: los abrí los cuatro y ninguno dice «vía 3».

### 4.4 · §18 — AQUÍ SÍ, Y `S2` TIENE RAZÓN

`11-ARQUITECTURA-INTEGRADA.md` **L9442, L9445, L9450, L9453**, las cuatro filas `FASE 0`, columna **«participantes de la RUTA, con su vía»**:

> `` `VER` vía 2, produce el DOSIER y **no se apropia de la decisión** · `SEG` **vía 3** cuando hay superficie, y **conserva su bloqueo** ``

**Y es imposible, por tres vías independientes que verifiqué una a una:**

1. **La definición de vía 3** (§8.0 L5985-5992): «*3 CONDICIONAL — **figura en las `condicionales` del proceso** CON SU CONDICIÓN ESCRITA Y COMPROBABLE*». Las cuatro filas declaran `proceso:SIS`.
2. **`proceso:SIS` no declara a `SEG` ni como obligatoria ni como condicional.** `PN-13` (L8759-8763) lo cita de `b.16`, que es material APROBADO: «*SIS: obligatorias SIS·CON·VER, condicionales ENT y APR … **`DOM`, `SEG` y `DIS` no figuran en ninguna de las dos***». Y §8.0 L6161-6164 **prohíbe expresamente ensanchar un proceso por conveniencia**.
3. **La misma tabla se desmiente cuatro filas más abajo.** L9449, fila `A9`–`A10`, también `proceso:SIS`: «**`SEG` sin vía si hay superficie: `PN-13`**». Y L9443, fila `INS-0`–`INS-5`, también `proceso:SIS`: «**`DOM` `DIS` `SEG` sin vía: `PN-13`**». **Mismo proceso, misma tabla, tres filas que dicen que sí y dos que dicen que no.**

Además, la condición escrita es «**cuando hay superficie**» — que es *exactamente* el antecedente que `PN-13` declara sin vehículo.

### 4.5 · MI RESPUESTA, PARTIDA COMO DEBE ESTARLO

```text
LA FILA `D107` DEL REGISTRO      NO EXCEDE. Se declara derivada, lo es, y da a `SEG`
                                 exactamente lo que `O17` le da: el bloqueo.  (S3 acierta)

§9.6, LA SEDE ÚNICA              NO EXCEDE. `SEG` el bloqueo, sin vía.

§18, LA SEDE QUE §8.0 DECLARA    **SÍ EXCEDE.** Da a `SEG` PARTICIPACIÓN EN LA RUTA por
QUE MANDA                        vía 3 dentro de `proceso:SIS`, que `b.16` no permite, que
                                 `PN-13` declara imposible y que la propia tabla niega en
                                 otras dos filas.  (S2 acierta)
```

**Y el exceso NO es inocuo, porque §18 es la sede que manda.** §8.0 L5972-5974 dice «*SEDE CANÓNICA la tabla de §18 … si alguna vez difieren, **MANDA §18***». §9.6 L7346-7347 dice «*si alguna vez difieren, **manda ésta***». **Las dos reglas de precedencia se solapan justo aquí y dan respuestas opuestas** (`S-09`), y un lector que aplique la de §8.0 —que es la general para macrocircuitos— concluye que `SEG` participa por vía 3 en una ruta donde material aprobado no la admite.

**Lo que rechazo de cada uno.** Rechazo la formulación de `S2` de que «`D107` excede a `O17`» **sin más**: la fila `D107` no excede y §9.6 tampoco, y decirlo así imputa a una decisión declarada derivada un exceso que está en una tabla. Y rechazo la respuesta de `S3` como **completa**: `S3` sólo abrió el registro de decisiones —que no es su culpa, era su lote— y de ahí concluyó «`D107` NO EXCEDE», sin poder ver que la propagación que esa misma fila anuncia sí lo hace en §18. **La respuesta correcta necesita las dos lecturas, y por eso este dictamen existe.**

**Coste del remedio: dos palabras.** Borrar «vía 3» de las cuatro filas y dejar «`SEG` conserva su bloqueo», que es lo que §9.6 ya dice. Es **clase A**.

---

## 5 · ¿ES `O12` SATISFACIBLE HOY? — MI RESPUESTA, CON EL RECORRIDO

`O12` (§9.4 L7154-7158) exige **tres** cosas: **Integrada + baseline aprobado + ningún desconocido crítico sin clasificar**. Y «NIVEL ALCANZADO» (§9.2 L7104-7106) exige que **todos los niveles presupuestos estén `verificado` Y VIGENTES**.

### El recorrido, paso a paso, por `N` — que es el único que el documento declara «completo, sin hueco»

| # | paso | ¿tiene productor DECLARADO? | ¿es ejecutable hoy? |
|---|---|---|---|
| 1 | FASE 0 → celda `certificacion/estructural` | **SÍ** — `SIS`, vía `gate:sistema-conforme` (§9.6). **Esto es lo nuevo, y es real** | **NO.** El sujeto exige el identificador de una iniciativa que el gate prohíbe abrir (`S-02`), y la celda no tiene dónde escribirse: `estado/` nace en `INS-0` (§8.1 L6260) y FASE 0 va antes (`S-03`) |
| 2 | `INS-0`–`INS-3` | SÍ | condicionado a 1 |
| 3 | `INS-4` → **Operativa** | **SÍ** — `INS-4`, y es la ÚNICA sede del documento que produce este nivel | sí |
| 4 | `INS-5` → baseline + clasificación de desconocidos | **SÍ, las dos** (`D76`) | **NO limpiamente**: `PN-13` VIGENTE bloquea «que `INS-5` abra con `DOM` y `DIS` en su ruta» |
| 5 | `INS-6`–`INS-7` → **Integrada** | SÍ — `INS-7` | **NO**: `PN-6` VIGENTE bloquea «declarar Integrada a un producto de 0 o 1 fuente» |
| 6 | `INS-7` = `O12` | SÍ | ver 4 y 5 |
| — | ejecutar §8.1 de verdad | — | **NO**: `PN-15` VIGENTE bloquea «la ejecución real del Circuito 0 por la ruta de §8.1» hasta que F5 decida |

### Por `A`, `M` y `U`

- **`A` · adopción.** FASE 0 → `A9` Integrada → `A3` baseline → `A10` = `O12`. **NO alcanzable, y el documento lo dice él mismo** (§9.6 L7502-7505): «*la adopción sigue sin fase que produzca su OPERATIVA con nombre propio, y `A9` la presupone por la cadena de §9.2*». La abstención es **correcta**: `O17` da productor al Estructural y a ninguno más, y ampliarla sería reinterpretar una resolución del Owner. **Eso está bien hecho.**
- **`M` · migración. Y aquí está lo que nadie declaró.** `M5` certifica Integrada. Integrada presupone Operativa. La Operativa se produce en **`INS-4` y en ningún otro sitio** —lo barrí sobre el documento entero—, y **§9.3 declara que la Operativa se invalida cuando «cambia la disposición del estado»**, que es literalmente lo que hace `M3` («migrar ESTADO PERSISTIDO, con su esquema»). §8.3 lo llama «el paso peligroso». **Luego en `M` la Operativa heredada se invalida en `M3`, ninguna fase la reproduce, y `M5` certifica Integrada sobre un presupuesto vencido.** Es el mismo hueco que la adopción, **y la sección escrita para no tapar huecos —«LA SALVEDAD, DICHA Y NO TAPADA»— declara uno y calla el otro.** Ver `S-04`.
- **`U` · actualización.** `U6` «revalida el nivel que tuviera antes» y `U` **no invoca `O12`**, y §18 lo dice. Correcto y sin hueco propio, aunque «revalidar» no está definido como «producir».

### MI RESPUESTA

> **`O12` es HOY satisfacible SOBRE LA CADENA DE NIVELES y SÓLO POR `N`. NO es satisfacible por ningún recorrido EJECUTABLE, y la migración tiene un hueco que ninguna sede declara.**

**Lo que `O17`/`D107` sí consigue, y es un avance real sobre el GRAVE nº 2 del documento 22:** el nivel Estructural **tiene productor**, la cadena de §9.2 deja de ser inaplicable, y `gate:sistema-conforme` deja de tener una sola aparición definitoria. El hallazgo `P-06` está **genuinamente atacado**, y no de forma cosmética.

**Lo que NO consigue:** (i) por `A` la cadena sigue rota en la Operativa —admitido y correctamente no ampliado—; (ii) por `M` la cadena está rota **igual y no se admite**; (iii) por `N` la FASE 0 no es ejecutable tal como está escrita; (iv) tres presiones vigentes se interponen.

**Y por eso la afirmación de §9.6 L7492 —«Éste es el recorrido completo, sin hueco»— es demasiado fuerte.** Es cierta sobre la cadena de niveles de `N` y falsa sobre el recorrido. Debería acotarse.

---

## 6 · HALLAZGOS DE `S`, CONSOLIDADOS

**Veintiséis.** Renumerados `S-01`…`S-26`. **La severidad es MÍA**, no la que propusieron mis relevos: he rebajado cinco y he ampliado dos. Criterio declarado, el mismo que `R` usó en el documento 22: **GRAVE** = una garantía publicada no se sostiene, o `F6` construiría algo distinto de lo que el contrato quiere · **MEDIO** = una afirmación vigente es falsa sin cambiar el comportamiento · **MENOR** = editorial o de propagación. **BLOQUEANTE = obliga a decidir arquitectura nueva: no adjudico ninguno.**

### GRAVES — seis

---

**`S-01` · GRAVE · §18 da a `SEG` participación en la ruta por «vía 3» dentro de `proceso:SIS`, que material APROBADO no permite, que `PN-13` declara imposible y que la propia tabla niega en otras dos filas**

**Fichero y líneas:** `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L9442, L9445, L9450, L9453** (las cuatro filas `FASE 0`), contra **L9443**, **L9449**, **L5985-5992** (§8.0, vía 3), **L8759-8763** y **L8793** (`PN-13`), y **L7440-7441** (§9.6).

**Cita literal (L9442, columna «participantes de la RUTA, con su vía»):**
> `` `VER` vía 2, produce el DOSIER y **no se apropia de la decisión** · `SEG` **vía 3** cuando hay superficie, y **conserva su bloqueo** ``

**Contra, en la misma tabla (L9449, fila `A9`–`A10`, también `proceso:SIS`):**
> `` **`SEG` sin vía si hay superficie: `PN-13`**, y entretanto item `AUD` enlazado con `SEG` de propietaria derivada ``

**Contra (L9443, fila `INS-0`–`INS-5`, también `proceso:SIS`):** `` **`DOM` `DIS` `SEG` sin vía: `PN-13`** ``

**Por qué es defecto.** Vía 3 se define como «*figura en las `condicionales` del proceso*» (§8.0). `proceso:SIS` declara como condicionales **`ENT` y `APR`, y nada más** —`b.16`, material APROBADO, citado por `PN-13`—. §8.0 L6161-6164 prohíbe ensanchar un proceso por conveniencia. §9.6, la sede única que `D107` designa, da a `SEG` **el bloqueo y ninguna vía**. Y §18 es la sede que §8.0 declara que MANDA. **Es el único punto donde la propagación de `O17` excede la resolución del Owner**, y lo hace en la sede que gobierna.

**Arrastra `PN-13` consigo:** su `ALCANCE` (L8793) dice «`INS-5` y `A9` de §8, **y nada más**», y con las cuatro `FASE 0` en `proceso:SIS` el alcance real pasa a incluir cuatro sedes más. Es la única presión que va al Owner por materia nueva, y se le lleva con el alcance corto. **No lo cuento aparte: es la misma corrección, y si se retira «vía 3» desaparece solo.**

**Quién lo levantó.** `S2` (`S2-03`, con `S2-07` como dependiente). **Lo REPRODUJE** abriendo las cuatro filas de §18, las dos que las desmienten, la definición de las cuatro vías en §8.0 y `PN-13` entera. **Y reformulé su tesis:** `S2` decía «`D107` excede a `O17`»; lo que excede es §18, no la fila `D107` ni §9.6. Ver §4.

---

**`S-02` · GRAVE · el SUJETO que la FASE 0 exige RESUELTO en su ENTRADA contiene el identificador de una iniciativa que la propia FASE 0 prohíbe abrir**

**Fichero y líneas:** `11-ARQUITECTURA-INTEGRADA.md` **L7373-7375** contra **L7436**, **L7449-7451** y **L7474**.

**Cita literal (L7373-7375), identificador nº 2 de los seis:**
> `2 EJECUCIÓN DEL       **CUÁL** de las ejecuciones: **la iniciativa del macrocircuito, por su`
> `  MACROCIRCUITO       identificador.** Es lo que hace que la certificación sea de ESTA`
> `                      ejecución y no de otra, y sin él las reglas 1, 3 y 9 no son evaluables`

**Contra (L7436, ENTRADA de la FASE 0):** `` el disparador del macrocircuito, con CERO mutaciones hechas · **el SUJETO de los seis identificadores, resuelto** ``
**Contra (L7449-7451, GATE):** `` **no se abre la iniciativa**, no se escribe ningún canónico ``
**Contra (L7474, `X-S5`):** `` **una iniciativa abierta ya es estado**: es la frontera exacta ``

**Por qué es defecto.** El identificador nº 2 sólo existe si la iniciativa existe; la iniciativa sólo se abre después de FASE 0; y el sujeto tiene que estar **resuelto en la ENTRADA**. Las tres no pueden ser ciertas a la vez. En `N` la iniciativa `INI-001` nace en `INS-0`; en `A`, en `A0`–`A1`; en `M`, en `M0`. Las tres salidas posibles están cerradas por el propio texto: abrir antes viola las reglas 2 y 5 y `X-S5`; resolver el sujeto sin él viola la regla 7 y falla por `X-S9` («omitir uno es un fallo del gate»); y **reservar un identificador sin persistirlo no lo dice ninguna sede** — lo barrí (`grep -n 'reserva\|reservar\|identificador de la ejecución'`) y no existe.

Es el mismo modo de fallo que `D49` cerró —«exigía abrir una transacción para registrar lo que impide abrir transacciones»— reproducido en la sección nueva.

**Quién lo levantó.** `S2` (`S2-01`). **Lo REPRODUJE** contra las cuatro sedes y comprobé además que ninguna fase de `N`, `A` ni `M` crea la iniciativa antes de su primer paso.

---

**`S-03` · GRAVE · la SALIDA de la FASE 0 es estado canónico y en `N` y en `A` no existe soporte donde escribirla: `estado/` nace DESPUÉS**

**Fichero y líneas:** `11-ARQUITECTURA-INTEGRADA.md` **L7442-7446** y **L7452-7455** contra **L6260**, **L6280-6281**, **L401** y **L9446**.

**Cita literal (L7442-7446, SALIDA):**
> `SALIDA             **la declaración Estructural DE ESTA EJECUCIÓN** … · **la celda`
> `                   `aspecto:certificacion/estructural` del sujeto**, con el contrato de §3.5`

**Cita literal (L7452-7455, CONDICIÓN DE CIERRE):** `` la declaración emitida, y **su celda `verificado` y vigente** para ESTA ejecución. **Sin ella la fase siguiente no abre** ``
**Contra (§8.1 L6260):** `` ESTADO          `estado/` nace en **INS-0**, con su soporte durable mínimo ``
**Contra (§9.6 L7432-7433):** «En `N` va **antes de `INS-0`** —que ya publica—, en `A` antes de `A0`»
**Contra (§2.4 L401):** `` cobertura/<clase>/<sujeto>.md ``, dentro de `estado/`.

**Por qué es defecto.** `cobertura` es tipo canónico de estado y vive en `estado/`. En `N` sobre proyecto nuevo, antes de `INS-0` no hay workspace, ni control repo, ni `estado/`. **Y en `A` pasa lo mismo**, que es una ampliación mía sobre lo que `S2` encontró: §18 L9446 da a `A0`–`A1` el estado persistido «iniciativa + `estado/`», y FASE 0 va antes de `A0`. La FASE 0 tiene que emitir una declaración durable y una celda **sin sede donde escribirlas**, en **dos** de los cuatro macrocircuitos. Y §8.1 **no actualizó su fila `REANUDACIÓN`**, que sigue diciendo «por el checkpoint del paquete de `SIS-001`, **desde INS-0**»: la FASE 0 no es reanudable, vive en el chat, y el apartado 19 de la directiva lo prohíbe. Es lo que `D30` cerró por detrás, reabierto por delante.

**Quién lo levantó.** `S2` (`S2-02`), para `N`. **Lo REPRODUJE y lo AMPLÍO a `A`.** **Y RECHAZO una mitad de su tesis:** `S2` sostiene que escribir la celda viola la regla 2 («cero mutaciones canónicas»). **No lo acepto**: «CERO mutaciones» está escrito sobre la **ENTRADA** de la fase, y la salida propia de un gate no es una mutación del macrocircuito en el sentido de la regla 2. Lo que sobrevive —y basta— es la **ausencia de soporte**, no una violación de la regla 2.

---

**`S-04` · GRAVE · la Operativa se produce en UNA sola fase de UN solo macrocircuito, `INS-4`. La MIGRACIÓN tiene el mismo hueco que la adopción y la sección escrita para «no tapar» huecos declara uno y calla el otro**

**Fichero y líneas:** `11-ARQUITECTURA-INTEGRADA.md` **L7129** (§9.2, productor de cada nivel) · **L7497-7501** contra **L7502-7509** (§9.6, los cuatro recorridos y «LA SALVEDAD») · **L7141-7144** (§9.3, invalidación) · **L6608** y **L6684-6686** (§8.3, `M3` y CERTIFICACIÓN).

**Citas literales:**
> **L7129 (§9.2):** `` operativo    `INS-4` ``  — y nada más. Barrí «Operativa/Operativo» sobre las 10 275 líneas: **ninguna otra sede la PRODUCE**.
> **L7143 (§9.3):** `` OPERATIVO     cambia un adaptador · cambia el arranque · **cambia la disposición del estado** ``
> **L6608 (§8.3):** `` M3 migrar ESTADO PERSISTIDO, **con su esquema** ``
> **L6684-6686 (§8.3, fila CERTIFICACIÓN):** `` **Estructural en FASE 0** … · Integrada en M5, ANTES de retirar nada. Revalidada en M7 `` — **no menciona la Operativa.**
> **L7504-7509 (§9.6, LA SALVEDAD):** `` **la adopción sigue sin fase que produzca su OPERATIVA con nombre propio**, y `A9` la presupone por la cadena de §9.2 ``

**Por qué es defecto, y por qué es GRAVE y no MEDIO.** `M5` certifica **Integrada**. §9.2 fija `integrado presupone operativo` y «NIVEL ALCANZADO» exige que **todos los presupuestos estén `verificado` y VIGENTES**. La única Operativa que un producto migrado puede tener es la que produjo `INS-4` en su instalación original — y `M3` la **invalida** por el trigger literal de §9.3. Ninguna fase `M0`–`M7` la reproduce; §8.3 ni la nombra. **Luego `M5` certifica Integrada sobre un presupuesto vencido, que es exactamente el modo de fallo que §9.2 describe en «CONSECUENCIA» y que `O17` vino a cerrar un piso más abajo.**

Y lo que lo agrava: **§9.6 enumera los cuatro recorridos y declara una salvedad — para `A` —, y el bloque se titula «LA SALVEDAD, DICHA Y NO TAPADA».** La honestidad de declarar el hueco de la adopción es real y consta a favor; **callar el idéntico de la migración en la misma enumeración, cuatro líneas más abajo, es el defecto**. No es que falte una decisión del Owner: falta **declarar** el hueco, que es lo que esa sede existe para hacer y lo que hizo bien con `A`.

**Quién lo levantó.** `S1` (`S1-11`), que no se atrevió a subirlo porque no había leído §8.2 ni §8.4. **Lo REPRODUJE y lo CONFIRMO GRAVE**: leí §8.3 entera (L6594-6700), verifiqué que su fila `CERTIFICACIÓN` no nombra la Operativa, barrí el término sobre el documento entero, y crucé §9.3 con `M3`. **`U` no arrastra el defecto** —`U6` revalida y `U` no invoca `O12`—, y eso lo rebajo respecto de `S1`.

---

**`S-05` · GRAVE · §8.0 publica «2·4·2·4 items líderes» declarando que la cifra «se DERIVA de §18», y §18 da hoy 3·5·3·5 — con lo que la aritmética del FRENO 3 de `a.7` deja de estar derivada para `U`**

**Fichero y líneas:** `11-ARQUITECTURA-INTEGRADA.md` **L6106-L6114** y **L6117-L6131**, contra las 16 filas de datos de §18 (L9442-L9457).

**Cita literal (L6106-6114):**
> `CUÁNTOS ITEMS      los ITEMS LÍDERES son **las FILAS de la tabla de §18** —una por tramo de fases`
> `COMPONE CADA UNO   con proceso propio— … N 2 líderes (`INS-0`–`INS-5` · `INS-6`–`INS-7`) …`
> `                   A 4 … M 2 (`M0`–`M5` · `M6`–`M7`) … U 4 …`
> `                   **El recuento se DERIVA de §18 y se mueve con ella. No se escribe aparte**`

**Cita literal (L6124-6128):**
> `` El FRENO 3 de `a.7` exige **más de dos** items `SIS` CONSECUTIVOS: **`M` tiene uno y `U` tiene dos** antes de que `DEP` rompa la racha. **El freno no llega a evaluarse** ``

**Mi derivación sobre §18 de HOY**, hecha extrayendo las filas y sus procesos:
```
N : FASE 0(SIS) · INS-0–INS-5(SIS) · INS-6–INS-7(SIS)             = 3 filas · 3 SIS consecutivos
A : FASE 0(SIS) · A0–A1(SIS) · A2–A7(AUD) · A8(DEU) · A9–A10(SIS) = 5 filas · máx 2 SIS seguidos
M : FASE 0(SIS) · M0–M5(SIS) · M6–M7(DEU)                          = 3 filas · 2 SIS seguidos
U : FASE 0(SIS) · U0–U4(SIS) · U5a(SIS) · U5b(DEP) · U6(SIS)       = 5 filas · 3 SIS seguidos
```

**Por qué es defecto, y no es cosmético.**
1. El recuento escrito (2·4·2·4) **ya no es el derivado** (3·5·3·5), **en la única sede que declara que se deriva y que «no se escribe aparte»**. La enumeración va por nombre de tramo y omite `FASE 0`, que §18 declara `proceso:SIS` y con estado persistido propio. Es la clase exacta de defecto que `D102` contrata para retirar.
2. **La aritmética del FRENO 3 deja de cerrar para `U`.** «`U` tiene dos» era cierto con dos filas `SIS` antes de `DEP`; con la `FASE 0` son **TRES consecutivos**, que es «más de dos», y **el freno SÍ llega a evaluarse**. Y `U` es el único macrocircuito donde el antecedente del freno —«hay un item de producto listo»— es plausiblemente verdadero, porque corre sobre un producto ya instalado y operando. **La conclusión publicada «Ninguno de los cuatro necesita excepción del Owner» (L6131) deja de estar derivada.** Y el propio §8.0 descartó como fundamento el salvavidas que quedaría —la cláusula literal de excepción de `a.7`—: «*se deja dicho como **observación, no como fundamento***».
3. «`M` tiene uno» también es falso hoy: tiene dos.

**Quién lo levantó.** `S2` (`S2-04`). **Lo REPRODUJE** enumerando yo las filas de §18 y sus procesos, y leyendo §8.0 L6096-L6140 entera. **Es el hallazgo más mecánicamente derivable de todo mi lote, y el que peor queda**, porque `D107` mueve la sede de la que otra cifra dice derivarse y no la vuelve a derivar.

---

**`S-06` · GRAVE · el addendum de `D97` publica CUATRO cifras escritas a mano bajo el rótulo «LA CIFRA, DERIVADA HOY y no copiada», y NINGUNA variante de barrido las reproduce hoy**

**Fichero y líneas:** `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` **L373-L378** y **L383-L384**.

**Cita literal (L373-378):**
> ```
> LA CIFRA, DERIVADA HOY y no copiada
>   (a)            G20 0 · G21 0 · G22 1 · G23 0
>   (b)            G20 0 · G21 0 · G22 0 · G23 0
>   `E2`           G20 0 · G21 0 · G22 0 · G23 0
>   documento 11   G20 12 · G21 10 · G22 16 · G23 13
> ```
**Cita literal (L383-384):** `` **Fecha de este addendum: 2026-08-30.** Su cifra **se deriva del árbol en cada lectura**; si vuelve a caducar, lo que hay que corregir es el barrido, no la frase. ``

**MI DERIVACIÓN, en HEAD `c36d2ba`, con las tres variantes de barrido posibles:**
```
grep -c   (líneas)   G20 13 · G21 10 · G22 16 · G23 14      ← DOS de cuatro fallan
grep -cw  (palabra)  G20 13 · G21 10 · G22 16 · G23 14      ← idem
grep -c '`Gnn`'      G20 12 · G21  9 · G22 13 · G23 12      ← TRES de cuatro fallan
publicado            G20 12 · G21 10 · G22 16 · G23 13
```
**No hay ninguna lectura bajo la cual las cuatro cifras publicadas sean verdaderas hoy.** Las de (a), (b) y `E2` sí lo son, y las verifiqué: doce de doce coinciden.

**CAUSA RAÍZ, reproducida por mí con Git.** La cifra fue correcta en el commit que la escribió y **caducó UN commit después, en la misma rama, la misma tanda y el mismo día**:
```
78ec1cc  feat(f4c): registrar O17 del Owner, su propagacion D107 y acotar D97
         → G20 12 · G21 10 · G22 16 · G23 13     (exacto)
609863e  fix(f4c): propagar O17 a los cuatro macrocircuitos y cerrar la clase A del doc 11
         → añadió apariciones de G20 y G23 al documento 11 y NO tocó el addendum
```

**Por qué es GRAVE y no MEDIO, contra la severidad que `R` le puso al hallazgo original.** `R` graduó `P-05` MEDIO porque «la resolución de `D97` sobrevive y no cambia ningún comportamiento», y en eso tiene razón. **Pero el objeto que yo juzgo no es la frase de `D97`: es el REMEDIO.** Y el remedio:
1. **reintroduce el defecto que venía a cerrar**, con el rótulo «DERIVADA HOY» encima;
2. **caducó dentro de la misma tanda que lo escribió**, lo que lo hace la demostración más limpia de la razón de método del documento 22;
3. **copia, no deriva**: las cuatro cifras publicadas son **verbatim las que `P4` y `R` publicaron en el documento 22** (§6 de `P` y §9 de `R`: «G20 12 · G21 10 · G22 16 · G23 13»). No se derivaron del árbol al escribir el addendum: se transcribieron del hallazgo;
4. **nadie las comprueba.** `G-13` de la batería sólo deriva (a), (b) y `E2` —lo dice el propio documento 11—, y la cuarta línea no la contrasta ninguna comprobación;
5. y **la sede primaria hizo lo correcto y el registro lo deshizo**: `PN-15` en el documento 11 (L8924) escribe deliberadamente «*el documento 11 las nombra **muchas veces***», **sin número, para que no envejezca**.

**Quién lo levantó.** `S3` (`S3-03`). **Lo REPRODUJE entero**: derivé las cuatro cifras con tres barridos distintos, verifiqué las doce de (a)/(b)/`E2`, y reproduje la causa raíz con `git show` sobre `78ec1cc` y `git log 78ec1cc..HEAD`. **Y añadí la prueba de que fue COPIA y no derivación**, cotejándolas con el documento 22, que `S3` no podía abrir.

### MEDIOS — doce

| id | qué es | fichero y línea | cita | por qué es defecto | quién lo levantó · ¿lo reproduje? |
|---|---|---|---|---|---|
| **`S-07`** | **el nivel `completo` no tiene PRODUCTOR: en su casilla hay una lista de pruebas** | doc 11 **L7131**, dentro del bloque `PRODUCTOR DE CADA NIVEL` (L7121-7137) | `` completo     los escenarios de §14 ejecutados sobre un producto real `` | Las otras tres casillas nombran **fases** (`la FASE 0 de cada macrocircuito` · `INS-4` · `A9`·`M5`·`INS-7`). La cuarta nombra la columna «pruebas» de §9.1 repetida, que no es un productor. El bloque inmediatamente posterior exige lo contrario: «**Cada nivel conserva PRODUCTOR, EVIDENCIA, SUJETO, VIGENCIA y CONDICIÓN DE INVALIDACIÓN propios** —regla 12 de `O17`—». Que §9.4 sea honesta sobre que el nivel **no es alcanzable** hoy explica por qué no se ALCANZA, no por qué no tiene productor DECLARADO | `S1` (`S1-12`) · **SÍ**, leí el bloque entero y las cuatro casillas |
| **`S-08`** | **§14 no recibió la propagación de `D107`: los cuatro escenarios extremo a extremo no tienen FASE 0** | doc 11 **L7930-L7933**, dentro de §14 (L7926-L7953) | escenario 1, col. `gate`: `` `INS-4` Operativa · **`INS-5` baseline aprobado por el Owner** · `INS-7` = `O12` `` | `grep -n 'FASE 0'` da 46 golpes en §8.1-§8.4, §9.2, §9.4, §9.6, §15.8, §18 y §19 — **y CERO entre L7926 y L7953**. Los escenarios 1-4 son exactamente los cuatro macrocircuitos; §14 se declara la demostración de que «las piezas encajan sin contradecirse» (L7928), y el escenario 1 sigue diciendo que se recupera «desde `INS-0`». Es una sede de propagación omitida | `S2` (`S2-05`) · **SÍ**, derivé el barrido y leí la tabla entera |
| **`S-09`** | **dos reglas de precedencia solapadas y de sentido contrario, y ya han producido su primera divergencia real** | doc 11 **L7346-7347** contra **L5972-5974** | §9.6: «*§8.1…§8.4 la invocan y no la reescriben, y §18 la mapea fase a fase. **Si alguna vez difieren, manda ésta**.*» · §8.0: «*SEDE CANÓNICA la tabla de §18 … **si alguna vez difieren, MANDA §18***» | Para el contenido de la FASE 0 las dos se solapan y **ya difieren** (`S-01`: §18 da vía 3 a `SEG`, §9.6 no). Un lector que aplique §8.0 acepta la vía 3; uno que aplique §9.6 la rechaza. La regla de desempate no está jerarquizada en ninguna sede, y decide justo el punto donde la propagación excede a `O17`. **Coste: una frase** | `S2` (`S2-06`) · **SÍ**, leí las dos sedes |
| **`S-10`** | **titular «Las SIETE secuencias» sobre una enumeración de OCHO** | doc 11 **L2274** vs L2277-L2331 | `#### Las siete secuencias completas, y ninguna termina sin salida` | Ocho rótulos: `1`,`2`,`3`,`4`,`4b`,`5`,`6`,`7`. Lo **creó esta tanda**: `P-16` (L2103-2115) reclasificó `4b` de desenlace a **SECUENCIA** con la regla «*los desenlaces se numeran 1–4 … las SECUENCIAS llevan letra tras el número y viven en su propio bloque*», y no recontó el bloque de secuencias. Cardinal escrito a mano junto a la enumeración que lo desmiente | `S1` (`S1-01`) · **SÍ**, conté los ocho rótulos |
| **`S-11`** | **«Los CUATRO puntos anteriores» sobre una lista de CINCO** | doc 11 **L1303**, sobre el bloque «Dónde es obligatorio `fsync`» (L1230-L1260) | `Los cuatro puntos anteriores dependen de que la implementación no tenga defectos.` | La lista tiene hoy **cinco** puntos `(1)`–`(5)`: `D105` añadió el `(5)`. La otra lectura posible —las garantías de §2.6.6— da seis. Ninguna da cuatro. Y `P-09` del documento 22 **auditó ESE MISMO bloque** y corrigió sólo el remate de la lista, no el cardinal que la introduce | `S1` (`S1-03`) · **SÍ**, conté los cinco `(n)` |
| **`S-12`** | **«Los CUATRO casos … dichos uno a uno» sobre SEIS entradas** | doc 11 **L4042** vs L4045-L4104 | `**Los cuatro casos que la prueba obligó a separar, dichos uno a uno:**` | Seis entradas rotuladas: `orden` · `sellado` · `retirada-de-cuerpo` · `certificacion` · `integracion` NO ES `integration-set` · `deriva` y `fallo`. Y es §3.6, **la sede de la que F6 deriva el esquema del evento**, que se presenta como la que ya corrigió tres recuentos mal derivados | `S1` (`S1-06`) · **SÍ**, las conté |
| **`S-13`** | **«las CUATRO fichas» seis líneas después de corregir el conjunto a SEIS — y con consecuencia material** | doc 11 **L5052** y **L5056-L5058**, contra **L5030-L5033** | L5031: «`Son SEIS`, no cuatro: las cuatro de las dos dimensiones huérfanas, más `DSP` y `ENC` que el gate final añadió» · L5052: «`Ninguna de las cuatro fichas es (a), (b), E1…`» · L5056: «`si … el alcance de una de las cuatro NO estira hasta el aspecto…`» | `M-5`/`M-6` ampliaron el conjunto a seis y **no propagaron a las dos afirmaciones que razonan sobre él**. Consecuencia real: las fichas de **`DSP` y `ENC` quedan hoy sin declaración de si generan presión normativa y fuera del límite declarado**, que es el compromiso que ese bloque existe para dar. Y la extensión de `DSP` —«autorizar la APERTURA mecánica de items `AUD` dentro de una política `O7` vigente»— es justo la clase de cambio que puede tocar `C1`. **La afirmación «ninguna genera presión» no se ha comprobado sobre las dos añadidas** | `S1` (`S1-08`) · **SÍ** |
| **`S-14`** | **el barrido de `P-16` se declara completo y no lo está: dos sedes VIVAS siguen diciendo «desenlace `4b`», y el cardinal «seis sedes» tampoco casa** | doc 11 **L2371-2372** y **L2796-2797**, contra la regla en **L2110-L2113** | L2372: «*no casa, la preservación NO se ha logrado y **el desenlace sigue siendo el `4b`***» · L2796: «*`divergente` **sólo** en el acto (ii) **del desenlace `4b`***» · L2113: «*Las **seis** sedes dicen ahora «secuencia `4b`»*» | La regla que la propia tanda fija dice «*los desenlaces se numeran `1`–`4` y **no hay ninguno más***». Dos sedes vigentes la violan, y L2372 además afirma que **el desenlace ES el `4b`**, cuando `P-16` fija que el desenlace de la secuencia `4b` es el **4**. La segunda es demoledora porque es **la misma frase** que L2640 —«el acto (ii) del secuencia `4b`»— en otra sede: una se convirtió y la otra no. Y `grep -c 'secuencia \`4b\`'` da **siete**, no seis: **el cardinal del barrido tampoco es derivado** | `S1` (`S1-04` + `S1-05`) · **SÍ**, con los dos barridos. **REBAJADO de GRAVE a MEDIO**: nada derivado se rompe hoy; lo que falla es una declaración de completitud y una convención de nombres |
| **`S-15`** | **el enum de `fase` de §3.6 contradice a su propia matriz sobre `orden`** | doc 11 **L3884-3885** contra **L4032** y **L4051-4053** | L3885: «*CINCO fases … y el valor `—` lo toman **`sellado`, `deriva` y `fallo`***» (enumeración cerrada de tres) · L4032, fila `orden`, columna *¿puede existir SIN `fase`?*: «**SÍ**, y sólo entonces» | §3.6 es **la sede de la que se deriva el esquema estructural**, y el propio documento registra en `J-01`/`D96` que «un esquema derivado literalmente de esta sección aceptaba un `preparada` sin él». Un esquema derivado de L3885 **rechazaría** un `orden` sin `fase`, que es el caso que `D59` declaró legítimo. Es la clase exacta de `A1`, invertida. Y el propio cómputo `34·20·54` que cierra la sección **cuenta `orden` sin fase como combinación VÁLIDA** | `S1` (`S1-07`) · **SÍ**, abrí las tres sedes |
| **`S-16`** | **el checkpoint publica «30/30» y «sus treinta comprobaciones» bajo el rótulo `ESTADO VIGENTE`; la batería da 37** | `CHECKPOINT-ADS-NEXT.md` **L2467** (bloque `ESTADO VIGENTE`, abierto en L2382) y **L2488** (prosa viva, sin marca) | L2466-2467: «*`G-24` leyendo de verdad las catorce fuentes y las quince fichas por nombre. **30/30 desde la raíz, desde otro cwd y desde un worktree arbitrario.***» · L2488: «*con el detalle de sus **treinta** comprobaciones*» | Ejecuté la batería sobre el árbol real: **`37/37 comprobaciones en verde`**. Dos cifras escritas a mano, caducadas, bajo un rótulo que declara que describen el estado vigente — en el fichero que la propia batería barre y que `G-26` existe para vigilar | `S3` (`S3-06`) · **SÍ**, ejecuté la batería (es de sólo lectura y no ensució nada) y leí el bloque `ESTADO VIGENTE` entero |
| **`S-17`** | **«Siguiente acción exacta» —el punto de entrada— prescribe como paso siguiente lo que el árbol ya ejecutó** | `CHECKPOINT-ADS-NEXT.md` **L2560-2562** (§0) y **L2653-2656** (§7); cabecera **L6** | L6: «*Basta decir «**Continúa**»: la siguiente acción exacta está al final*» · L2561: «*la tanda en curso **está aplicando** su resolución y los 68 hallazgos de clase `A`*» · L2653: «*EL SIGUIENTE PASO: terminar de aplicar los 68 de clase `A`, **PUBLICAR EL ÁRBOL VIGENTE COMO CANDIDATA NUEVA**, y **ENCARGAR OTRO GATE INDEPENDIENTE** sobre ella*» | Las dos cosas ya están hechas: `origin/review/f4c-o17-candidate-20260830` = **`e316396`**, publicada; y este segundo gate está en marcha —yo soy uno de sus revisores—. Quien diga «Continúa» hoy recibe una instrucción ya cumplida. Es la tercera recurrencia consecutiva del mismo modo de fallo sobre la misma sección (`P-05`≡`Q-08` fue el **único GRAVE** del documento 21) | `S3` (`S3-05`) · **SÍ**. **REBAJADO de GRAVE a MEDIO**, y digo por qué: la sección era **verdadera cuando se escribió** (`55d8ce1`), la caducó el propio commit final de la tanda (`e316396`), la desviación es de un paso, y el fichero **remite expresamente los SHA a `git rev-parse` en vez de copiarlos** |
| **`S-18`** | **el árbol de HEAD está en 12/13 con `T147` en ROJO y su evidencia derivada caducada — pero la causa es el APARATO DE ESTE GATE, no la tanda** | `docs/evolucion/00-INDICE.md` **L106-L117** contra `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` | `00-INDICE.md` L106: «*Quien publique un manifiesto sin enlazarlo aquí **deja el árbol que juzga con un validador canónico en rojo, causado por el aparato del propio gate**.*» | **REPRODUCIDO sobre una copia fuera del repositorio**: `T147 FALLIDA · F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md: no lo alcanza ningún enlace por ruta … Existe para nadie`, `12/13 validadores en verde`, y dos ficheros de evidencia modificados (302→303 ficheros recorridos). **La regla se escribió en `55d8ce1` y se incumplió en `c36d2ba`, dos commits después, por el coordinador de este gate.** `00-INDICE.md` enlaza los tres manifiestos anteriores y **no** el del segundo gate; `grep -rn` sobre el corpus entero: **cero** referencias | `S3` (`S3-04`) · **SÍ**, sobre copia. **REBAJADO de GRAVE a MEDIO Y REATRIBUIDO**, ver §7 |

### MENORES — ocho

| id | qué es | fichero y línea | por qué | quién · ¿reproducido? |
|---|---|---|---|---|
| **`S-19`** | `D107` está archivada como última fila de la tabla del epígrafe **`### \`D104\`–\`D106\``**, bajo un preámbulo que describe **otro** gate (el de cobertura y cierre, documento 20, adjudicador `O`, 21 hallazgos) y otra declaración de integridad (`D1`–`D103`) | `DECISIONES-Y-CONTRADICCIONES.md` **L430** (epígrafe), **L432-L441** (preámbulo), **L452** (la fila) | Un lector que busque «qué decidió la tanda de `O17`» por los epígrafes **no encuentra `D107`**. El propio corpus sabe hacerlo bien: §15.8 del documento 11 le da bloque PROPIO. **REBAJADO de MEDIO a MENOR**: la fila se alcanza por la tabla y por §15.8, la serie `D` es continua (107 filas, 107 valores únicos, sin huecos ni duplicados — lo derivé), y la propia fila declara correctamente «`D1`–`D106` y `O1`–`O16` intactas» | `S3` (`S3-01`) · **SÍ** |
| **`S-20`** | la fila `D97` **no lleva ningún puntero** al addendum que la acota siete líneas más abajo | `DECISIONES-Y-CONTRADICCIONES.md` **L346** | `grep -o 'ADDENDUM' <(sed -n '346p' …)` → **vacío**. La frase «`G20`, `G21` y `G23` tienen **cero** apariciones en el documento 11…» sigue leyéndose **en presente y sin aviso** en su punto de lectura. No reescribirla era la virtud; no marcarla es el defecto. Compárese con `D94`, que `R` cita como precedente: allí la corrección vive en una fila `D` nueva que se lee en secuencia | `S3` (`S3-02`) · **SÍ** (nota: la fila está en **L346**, no en L345 como `S3` escribió) |
| **`S-21`** | los dos párrafos de §0 que declaran «REMITE y no copia» **escriben el cardinal en la misma frase** | doc 11 **L129-L140** y **L12-L20** | L129-134: «*este diseño presiona material aprobado en **DIECISÉIS** puntos … **La cifra NO se escribe aquí ni se enumera aquí: se DERIVA del barrido** … Este párrafo REMITE a ella y no la copia*». **Hoy las dos cifras son CORRECTAS** —las derivé: 18 cabeceras `## \`PN-` − `PN-4` RETIRADA − `PN-5` FUSIONADA = 16; y 17 bloques `###` en §15.8—, por eso es MENOR. Pero el mecanismo que el documento declara como su defensa no es el que estos párrafos ejecutan | `S1` (`S1-09`) · **SÍ**, derivé las dos |
| **`S-22`** | el prefijo `X` se usa con dos poblaciones —`X1`–`X8` (las incógnitas) y `X01`–`X62` (las filas adversariales)— separadas sólo por un cero de relleno, y el barrido de `D83` sólo censó `R<n>` y `N<n>` | doc 11 **L306-L325** | El invariante declarado es «*ningún identificador de la forma `<PREFIJO><n>` se usa con dos significados distintos en el corpus. F6 la construye una vez*». **REBAJADO de MEDIO a MENOR, y contra mi propio relevo:** `X1` y `X01` son cadenas **distintas**, luego el invariante **no está literalmente violado**; el relleno se aplica de forma consistente y no encontré ni una cita ambigua. Lo que queda es un riesgo sobre la prueba que F6 construya si normaliza el relleno | `S1` (`S1-10`) · **SÍ**, y lo rebajé |
| **`S-23`** | las cuatro ramas del punto 7 de §2.6.9 **no son disjuntas** y no declaran precedencia | doc 11 **L1965-L1990** | El estado `(abandonada durable, deriva AUSENTE, marcador tx RETIRADO)` satisface la rama 2 (→`W17`, completar el `deriva`) **y** la rama 4 (→ nada que hacer). Es MENOR porque el protocolo declara ese estado **inalcanzable por construcción** —el paso 6 sólo retira el marcador después del `deriva` durable—, pero §2.6.9 existe para clasificar **lo que se OBSERVA** tras una caída y §3.3.1 exige funciones de estado «totales y DISJUNTAS» | `S1` (`S1-13`) · **SÍ**, leí el punto 7 entero en su redacción de hoy |
| **`S-24`** | concordancia rota: «**Y el** secuencia `4b` no es terminal» | doc 11 **L2230-L2231** | Artículo masculino sobre sustantivo femenino: residuo mecánico de la sustitución «desenlace → secuencia» de `P-16`. Por sí mismo es trivial; **vale como evidencia de que el barrido de `S-14` se hizo por reemplazo de palabra sin releer la frase** | `S1` (`S1-02`) · **SÍ** |
| **`S-25`** | la fila `D107` del registro cita las reglas 7, 8, 9, 10, 11 y 12 de `O17` por su número y **no menciona las reglas 3, 4 y 5 ni el deber del propietario del macrocircuito** | `DECISIONES-Y-CONTRADICCIONES.md` **L452** frente a `O17` **L712-L735** | **REBAJADO de MENOR-con-sospecha a MENOR-de-navegación, y la sospecha la CIERRO yo.** `S3` no pudo verificar si el material estaba en el documento 11 porque no era su lote. **Lo verifiqué: SÍ está, y entero.** §9.6 recoge la regla 3 en «NO HEREDA» (L7402-7404), la regla 4 en «NO SE DEDUCE DESDE ARRIBA» (L7405-7409), la regla 5 en `GATE` (L7447-7451) y el deber del propietario en su propio bloque (L7360-7367), con contraescenarios `X-S2`, `X-S4`, `X-S5` y `X-S7`. **Las doce reglas están propagadas.** Lo que queda es que la fila del registro no remite | `S3` (`S3-07`) · **SÍ, y lo cerré en la dirección contraria a la sospecha** |
| **`S-26`** | **HALLAZGO MÍO** · el motivo entrecomillado que `O17` atribuye al Owner **no tiene ninguna sede independiente en todo el árbol**, y no puede tenerla | `DECISIONES-Y-CONTRADICCIONES.md` **L696-L700** | Ver §7 y §9. Las **tres alternativas** de `O17` sí son verbatim de §13 del documento 22 —lo coteje palabra por palabra—, pero **el motivo del Owner no está en §13 y no puede estarlo**: §13 contiene la PREGUNTA, formulada antes de que hubiera respuesta. `grep -rn` sobre `docs/` y `kernel/`: el texto entrecomillado sólo existe en `O17` y en el checkpoint, que lo cita de `O17`. **`O16` recibió un ADDENDUM DE CRONOLOGÍA por `M-07`/`L-02` exactamente para dar atribuibilidad demostrable; `O17` declara procedencia y fecha pero no tiene trazabilidad de la respuesta.** No afirmo que sea falso: afirmo que **ningún gate puede verificarlo**, y que eso debería constar | **mío** · N/A |

```text
RECUENTO DERIVADO DE LAS FILAS DE ARRIBA, no escrito aparte

  BLOQUEANTE    0
  GRAVE         6    S-01 · S-02 · S-03 · S-04 · S-05 · S-06
  MEDIO        12    S-07 … S-18
  MENOR         8    S-19 … S-26
               ──
               26
```

**Cuántos los introdujo o los dejó pasar ESTA tanda.** `S-01`, `S-02`, `S-03`, `S-04`, `S-05`, `S-08`, `S-09` y `S-19` **los introdujo `D107`**, que es de esta tanda. `S-06` lo introdujo el addendum de esta tanda y **caducó dentro de la propia tanda**. `S-10` lo creó `P-16` de esta tanda; `S-14` es su barrido incompleto; `S-13` es propagación no hecha de `M-5`/`M-6`; `S-16` y `S-17` son cifras y secciones que esta tanda tocó y dejó a medias. **Dieciséis de veintiséis.** Es exactamente la razón de método nº 6 del documento 22.

---

## 7 · HALLAZGOS QUE RECHAZO DE MIS PROPIOS RELEVOS, CON EVIDENCIA

**Seis rechazos y cinco rebajas. Lo escribo contra el interés de mi propia cadena, porque vale tanto como lo que confirmo.**

---

**`X-1` · RECHAZO la formulación de `S2-03`: «`D107` EXCEDE a `O17`».**
El hecho que `S2` encontró es **cierto y grave** —lo confirmo como `S-01`—, pero la imputación no. Abrí la fila `D107` entera (`DECISIONES-Y-CONTRADICCIONES.md` L452) y §9.6 entera (doc 11 L7324-L7541): **ninguna de las dos da a `SEG` vía ni participación**. Las dos dicen «`SEG` conserva su bloqueo», que es exactamente lo que `O17` L734 le da. **Quien excede es §18**, en cuatro filas de tabla. Decir «`D107` excede» imputa a una decisión que se declara derivada —y lo es— un exceso que está en su propagación tabular, y eso importa porque el remedio es distinto: no hay que revisar la decisión, hay que borrar dos palabras de cuatro filas.

**`X-2` · RECHAZO la respuesta de `S3` como COMPLETA, aunque su hecho es correcto.**
`S3` concluye «**`D107` NO EXCEDE a `O17`**» tras un cotejo cláusula a cláusula que verifiqué y que es bueno. Pero `S3` sólo tenía asignado el registro de decisiones, y por eso su barrido no pudo alcanzar §18. **La conclusión, tal como está enunciada, es verdadera del objeto que miró y falsa del objeto que la pregunta nombra** —la propagación—. Lo hago constar porque `S3` la ofrece como respuesta a la pregunta del encargo, y no lo es entera.

**`X-3` · RECHAZO la imputación de `S3-04` a la tanda, y lo demuestro con `git`.**
`S3` escribe: «*la evidencia caducada la deja el mismo commit, y la afirmación «`git status --short` vacío» es de la tanda*». **No es así.** Lo comprobé:
```
$ git show --stat 6b5d3e6   → 1 fichero: derivar-universo-obligatorio.py   (aparato del gate)
$ git show --stat c36d2ba   → 1 fichero: F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md (ídem)
```
Y el diff de evidencia que la ejecución produce es **exactamente y sólo**: `302 → 303 ficheros recorridos`, `300 → 301` en el fixture de `N158g`, y el nombre del huérfano en la salida de negativos. **El único fichero de corpus añadido desde que la tanda cerró (`e316396`) es el manifiesto de este gate.** Luego sobre el árbol de la tanda el runner daba 13/13 y `git status` quedaba vacío, y **la afirmación del checkpoint era verdadera cuando se escribió**. Mantengo el hecho como `S-18`, **rebajado a MEDIO y reatribuido al aparato del gate**. Es la misma resolución que `R` tomó en `D-5` y `X-1` del documento 22 sobre el hallazgo equivalente, y llego a ella por mi cuenta.

**`X-4` · RECHAZO la mitad de `S2-02` que invoca la regla 2.**
`S2` sostiene que, si la celda de FASE 0 se escribe, «se ha mutado estado canónico ANTES del punto que §9.6 declara «cero mutaciones»». **No lo acepto.** Releí L7436: «CERO mutaciones hechas» califica la **ENTRADA** de la fase, no su salida; y la regla 2 de `O17` dice «antes de cualquier mutación canónica **del macrocircuito**». La salida propia de un gate de precondición no es una mutación del macrocircuito en ese sentido. **Lo que sobrevive, y basta por sí solo, es la ausencia de soporte durable** — que es `S-03`.

**`X-5` · RECHAZO la sospecha de `S3-07` sobre las reglas 3, 4 y 5, y la cierro en la dirección contraria.**
`S3` observó que la fila `D107` no menciona esas tres reglas ni el deber del propietario, y dejó abierto si el material existía («*No verificado por mí en §9.6 del documento 11: fuera de mi lote*»). **Lo verifiqué y sí existe, entero y con contraescenario propio cada una**: regla 3 en «NO HEREDA» (L7402-7404) + `X-S2`; regla 4 en «NO SE DEDUCE DESDE ARRIBA» (L7405-7409) + `X-S4`; regla 5 en `GATE` (L7447-7451) + `X-S5`; el deber del propietario en su bloque propio (L7360-7367) + `X-S7`. **Las doce reglas están propagadas.** Queda sólo una falta de remisión en el registro, y eso es `S-25`, MENOR.

**`X-6` · RECHAZO que `U` arrastre el hueco de la Operativa, que es lo que `S1-11` insinúa.**
`S1` escribe que «`U` está en el mismo caso, aunque más débil». **No lo sostengo.** `U6` «revalida el nivel que tuviera antes», `U` **no invoca `O12`** y §18 lo dice expresamente: «*una actualización no arranca programación, y `O12` gobierna ese arranque*». No hay elevación de nivel que quede sin presupuesto, luego no hay hueco. **El hueco no declarado es de `M`, y sólo de `M`** — y por eso `S-04` es de `M` y no de «`M` y `U`».

---

### Las cinco rebajas, con su motivo

| relevo | propuso | adjudico | motivo |
|---|---|---|---|
| `S1-04`+`S1-05` | GRAVE | **MEDIO** (`S-14`) | Es una declaración de completitud falsa y una convención de nombres violada en dos sedes. **Nada derivado se rompe hoy** y ningún contrato produce un artefacto distinto. Pesa por el mecanismo —un barrido declarado completo que no lo está—, no por su severidad |
| `S1-10` | MEDIO | **MENOR** (`S-22`) | `X1` y `X01` son cadenas distintas: **el invariante declarado no está literalmente violado**, el relleno se aplica de forma consistente y no hay ni una cita ambigua hoy. Queda un riesgo sobre una prueba futura |
| `S3-01` | MEDIO | **MENOR** (`S-19`) | La serie `D` es continua y completa —lo derivé: 107 filas, 107 valores únicos, sin huecos ni duplicados—, §15.8 le da bloque propio y la fila declara correctamente su alcance. El daño es de navegación y está acotado |
| `S3-04` | GRAVE | **MEDIO** (`S-18`) | Ver `X-3`: la causa es el aparato de este gate, no la tanda |
| `S3-05` | GRAVE | **MEDIO** (`S-17`) | La sección era verdadera cuando se escribió, la caducó el commit final de la propia tanda, la desviación es de un paso, y el fichero **remite los SHA a `git` en vez de copiarlos** |

**Y una observación que NO cuento como hallazgo**, aunque `S3` la registró como `S3-08`: el único cambio no aditivo del registro de decisiones es un **movimiento byte a byte** del párrafo de procedencia de `O7`–`O14` (379 inserciones, 3 supresiones, reinsertadas idénticas). **Lo verifiqué con `git diff 7e99388 HEAD`, y es correcto: no es una reescritura.** `D1`–`D106` y `O1`–`O16` conservan su texto. Lo dejo como constancia a favor, no como hallazgo.

**Y otra que tampoco cuento, y que `S1` señaló para que no la levantara nadie:** los «ocho puntos» de `D105` (L1930-1933) enumeran ocho operaciones separadas por flecha y rematan con «**Seis pasos**». Abrí el paso `E` (L1894-L1919): numera **seis**, agrupando `fsync(fichero)+fsync(directorio)` en un paso, y los tramos `[paso n, paso m)` de `W8`, `W17` y el punto 7 son consistentes con esa numeración de seis. **Es ambigüedad de redacción, no falsedad. NO ENTRA.**

---

## 8 · LOS HALLAZGOS DEL DOCUMENTO 22 EN EL FOCO DE `S`

**Regla que me impongo, y la digo por delante.** Los del foco de `T` —**la batería `comprobar-correccion-gate-de-cierre.py`, el derivador, los manifiestos, el `CORRIGENDUM` y `M-04` como proposición general**— **NO los adjudico. No los presumo cerrados ni abiertos.** No he leído esas fuentes: no son de `S`. Donde una sede de mi lote los roza, juzgo sólo la coherencia interna de mi sede.

| id | qué exigía | qué encuentro yo en el árbol de hoy | resultado |
|---|---|---|---|
| **`P-01`** GRAVE | `W17` y el punto 7 se contradicen sobre `[paso 4, paso 5)`, y `W17` cita al punto 7 como su aval | **El punto 7 (L1965-L1990) está REESCRITO** y clasifica **por lo que observa**, no por tramos de tiempo: `W11` = `[1,2)` · `W17` = `[2,4)` · `W8` = `[4,6)` «LOS DOS TRAMOS, y ahí vive el `[4,5)` que antes no reclamaba nadie». La fila de `W8` (L1169) y la de `W17` (L1179) dicen lo mismo, y las tres cierran con «*ninguna cita a otra como fuente de un reparto que esa otra no escriba*». Lo verifiqué tramo a tramo: **sin huecos y sin solapes** | **CERRADO** |
| **`P-02`** MEDIO | el punto 7 metía `[paso 1, paso 2)` en `W17`, donde el `abandonada` puede no ser durable | El punto 7 dice hoy: «*NO hay `abandonada` durable —no se emitió, o se perdió por no haber pasado el paso 2— → … es `W11`. **Cubre todo `[paso 1, paso 2)`***» | **CERRADO** |
| **`P-03`≡`Q-17`** GRAVE | §15.8 no tenía bloque para `D96`–`D106` y §0 decía derivar de ahí | Derivé las cabeceras `###` de §15.8: **DIECISIETE**, y las últimas cuatro son `D96`–`D102`, `D103`, `D104`–`D106` y **`D107`**. §0 L14 dice «*hoy diecisiete, de `D23`–`D33` a `D107`*». **Coinciden** | **CERRADO** |
| **`P-04`** MEDIO | §0: titular CATORCE y cadena derivante que moría en TRECE | La cadena **se retiró**. §0 L129-140 remite al barrido y explica la resta. Derivé: 18 cabeceras − `PN-4` RETIRADA − `PN-5` FUSIONADA = **16**, y §0 dice DIECISÉIS | **CERRADO** *(con el residuo formal de `S-21`)* |
| **`P-05`** MEDIO | `D97` L346 sigue afirmando en presente «cero apariciones» | **CERRADO A MEDIAS.** El ADDENDUM existe, acota el material y se fecha —y eso era lo pedido—. Pero la fila **no lleva puntero** (`S-20`) y el propio addendum publica **cuatro cifras a mano, dos falsas hoy** (`S-06`) | **NO CERRADO** |
| **`P-06`** GRAVE, **clase `B`** | el nivel ESTRUCTURAL sin productor → `O12` insatisfacible | **ATACADO DE VERDAD, Y NO CERRADO DEL TODO.** `O17` lo resuelve, `D107` lo propaga, §9.6 es sede única y `gate:sistema-conforme` pasa de 1 a 23 apariciones. Pero la FASE 0 no es ejecutable (`S-02`, `S-03`), la Operativa de `M` queda sin productor y sin declarar (`S-04`), y `completo` sigue sin productor (`S-07`) | **PARCIALMENTE CERRADO** |
| **`P-07`** GRAVE | `reconciliacion_pendiente` sin productor; `T22` de (a) insatisfacible; ninguna `PN` lo registra | `## \`PN-17\` · NUEVA · \`reconciliacion_pendiente\` del canal de órdenes no tiene productor, y \`T22\` no es satisfacible` existe en §16 (**L9081**). **La presión está registrada.** *(No verifico su contenido contra (a)/(b): no son fuentes de `S`.)* | **CERRADO en el registro** |
| **`P-08`** MEDIO | `PN-16` dejaba fuera `VER:decisión`, ya construida con dos grafías | `## \`PN-18\` · NUEVA · \`VER:decisión\` frente a \`VER:decision\`` existe en §16 (**L9185**) | **CERRADO en el registro** |
| **`P-09`** MEDIO | el marcador del `deriva` no estaba en ninguna de las dos listas de `fsync` de §2.6.6 | §2.6.6 lo pone hoy en **NO EXIGIDO** —«*los derivados, el marcador de transacción, **el marcador del `deriva`**, …*»— **con su razón escrita** y con la nota «Y corregido por `P-09` del documento 22» | **CERRADO** |
| **`P-14`** MEDIO | §17 decía «`C1`–`C7` intactos» sobre un `C7` con corrección pendiente | §17 L9356 dice hoy «**NO todos intactos, y esta columna es la lista de trabajo de F6, luego se lee como exhaustiva.** `C2` se amplía en F6. **`C7` se reutiliza CON UNA CORRECCIÓN…**» | **CERRADO en el documento 11.** *(Que `C7:170` siga diciendo `una o más fuentes` no lo adjudico: `C7` no es fuente de `S`)* |
| **`P-15`** MEDIO | §17 decía «diez procesos · intactos» mientras §19 contrata que F6 edite cinco | §17 L9358: «**el NÚMERO es intacto: siguen siendo DIEZ … Los PROCESOS no lo son.** §19 (`D104`) contrata que **F6 instancie nueve pares**…» | **CERRADO** |
| **`P-16`** MEDIO | «desenlace `4b`» en seis sedes, contra la sede canónica de los cuatro desenlaces | La regla se escribió (L2110-2113) y el barrido se declara hecho. **Dos sedes vivas siguen diciendo «desenlace `4b`» (L2372, L2796) y el cardinal «seis» tampoco casa (son siete).** Y el propio remedio creó `S-10` | **NO CERRADO** *(es `S-14` y `S-10`)* |
| **`P-20`** MEDIO | las tres celdas de §5.6 escribían `responsables` con el reparto por defecto | Las tres dicen hoy «**SIN `responsables`**: `[ARQ, SIS]` con `lider: ARQ` **ES** el reparto por defecto» (L5199-L5201, L5255, L5300), con su nota de corrección | **CERRADO** |
| **`P-21`** MEDIO | `m-1` de §8.2 decía «Hoy son TRECE» | L6521 dice hoy «**Hoy son MÁS, y esta nota no dice** [la cifra]», y L6525 registra la corrección | **CERRADO, y bien: retiró la cifra en vez de reescribirla** |
| **`P-22`≡`Q-37`** MEDIO | `C-L.5` con estado compuesto: cabecera «abierta» y cierre «CERTIFICADA» | L10156: `## \`C-L.5\` · La condición de COBERTURA del próximo gate — **CERTIFICADA por el documento 21**, y vigente para todo gate posterior`. Cabecera, primer párrafo y cierre dicen los tres lo mismo, y el estado anterior queda marcado `[HISTÓRICO]` y no borrado | **CERRADO** |
| **`P-23`** MENOR | bloque `text` huérfano a 83 líneas de su cabeza | El bloque de L2043-L2050 tiene hoy rótulo (`LLEVA`) y sujeto | **CERRADO** |
| **`P-24`** MENOR | dos autorreferencias a número de línea, las dos rotas | L2468 registra «**Corregido por `P-24`**: decía «L2226»…». Las autorreferencias absolutas ya no están | **CERRADO** |
| **`P-25`** MENOR | `X-F` conservaba «una reconciliación abierta» sin marca | L3356 la lleva hoy dentro de `[HISTÓRICO]` | **CERRADO** |
| **`P-26`** MENOR | §15.4 publicaba un rango que no llegaba a su última fila, y `O16` sin fila | La cabecera dice hoy `## 15.4 · Las resoluciones del Owner y \`P-01\`–\`P-08\``, sin rango numérico, y la tabla traza **`O7` … `O16` y `O17`** | **CERRADO** |
| **`Q-12`** MEDIO | el checkpoint publicaba TRECE presiones donde el árbol deriva CATORCE | `grep -n 'TRECE presiones'` sobre el checkpoint → **vacío**. Las tres sedes vivas **REMITEN y publican el comando**, y ejecutándolo da **16**, que coincide con mi derivación | **CERRADO** |
| **`Q-16`** MEDIO | «Estado de las fases» omitía las dos últimas pasadas, sin marca | Llega hoy hasta la **9ª** (documento 22, con `O17` y `D107`) y cierra con «*CUÁNTAS PASADAS SON NO SE ESCRIBE AQUÍ: se DERIVA … Esta proyección enumeraba hasta la 7ª mientras el árbol iba por la 9ª — es `Q-16` del documento 22*» | **CERRADO** *(no enumera este décimo gate — es la misma caducidad de un paso de `S-17`)* |
| **`Q-35`** MENOR | `rama_de_trabajo` nombraba rama y base de dos tandas atrás bajo `freshness: vigente` | L587: «`rama_de_trabajo: NO SE ESCRIBE AQUÍ, Y ES DELIBERADO` … *es `Q-35` del documento 22, y es la tercera vez que caduca. La rama en curso y su base se DERIVAN de Git*» | **CERRADO, y con el mecanismo correcto** |
| **`Q-36`** MENOR | los puntos 0 y 7 de «Siguiente acción exacta» describían como pendiente lo ya ejecutado | **REINCIDE, un paso más adelante.** Es `S-17` | **NO CERRADO** |
| **`Q-38`** MENOR | tercer bloque de estado histórico sin marca `[ESTADO ANTERIOR]` | Los cuatro bloques anteriores de la cabecera del checkpoint llevan hoy marca explícita, y el de los documentos 16/17 (L449) **declara que le faltaba y quién se la puso** | **CERRADO** |
| **`C-L.1`…`C-L.13`** | trece condiciones, estado único, ninguna mal clasificada | La clasificación VIGENTE del checkpoint (L1462-L1512) **cuadra**: 8 CERRADAS + 2 REGISTRADAS + 1 CONTRATADA + 1 MIXTA + 1 CERTIFICADA = **13**, un estado primario por id, y las trece filas de detalle coinciden una a una con el resumen. **`C-L.3` CERRADA por `D104`** y **`C-L.5` CERTIFICADA** en sede única | **CERRADO** *(dos reservas: `C-L.13` lleva estado compuesto por construcción —«MIXTA POR DESGLOSE»—, defendido y sostenible; y el resumen usa «CORREGIDAS EN F4c» donde el detalle dice «CERRADA»: mismo hecho, dos vocabularios)* |
| **`M-04`** · `Q-01`…`Q-08` de `Q` · `R-N1`…`R-N3` · `Q-22`…`Q-28` | la batería, el derivador, los manifiestos, el corrigendum | **FUERA DE MI LOTE. NO LOS ADJUDICO Y NO LOS PRESUMO NI CERRADOS NI ABIERTOS.** Son foco de `T`. **Y digo el dato que sí tengo, sin adjudicarlo**: ejecuté la batería sobre el árbol real y da **`37/37 comprobaciones en verde`**, donde el gate anterior medía 30. Qué significan esas siete comprobaciones nuevas —si generalizan o vuelven a cerrar el perímetro de su contraejemplo— **es la pregunta de `T`, y no la respondo** | **FUERA DE MI LOTE** |

```text
EN EL FOCO DE `S` Y ADJUDICABLES POR MÍ     24
  CERRADOS                                  19
  CERRADO EN EL REGISTRO (contenido no      2   P-07 · P-08  (la presión existe; su
    verificable desde mi lote)                   contraste contra (a)/(b) es de otro lote)
  PARCIALMENTE CERRADO                       1   P-06   ← el GRAVE nº 2, y la clase `B`
  NO CERRADOS                                2   P-05 · P-16   (+ `Q-36`, que reincide)

FUERA DE MI LOTE, EXPRESAMENTE NO ADJUDICADOS   `M-04` y todo el aparato de verificación
```

---

## 9 · REFUTACIONES QUE INTENTÉ Y NO CAYERON

**Siete. Las publico con el mismo detalle que los hallazgos, porque un dictamen que sólo enseña lo que confirma no mide nada.**

---

**`RF-1` · Intenté demostrar que `P-01`/`R-04` —el único GRAVE heredado en mi foco— seguía roto por tercera vez. NO CAYÓ, y es el mejor trabajo de la tanda.**
Era el punto que la historia señalaba como el más probable: `R-04` llevaba dos gates sin cerrarse y el documento 22 lo declaró **AGRAVADO**. Reconstruí el reparto yo, desde los seis pasos del paso `E` (L1894-L1919), y lo crucé contra las tres sedes:

| tramo | quién lo reclama | fila `W` | punto 7 |
|---|---|---|---|
| `[paso 1, paso 2)` | `W11` | ✓ | ✓ «Cubre todo `[paso 1, paso 2)`» |
| `[paso 2, paso 4)` | `W17` | ✓ «el tramo `[paso 2, paso 4)` … y **sólo** ése» | ✓ «Es `[paso 2, paso 4)`» |
| `[paso 4, paso 6)` | `W8` | ✓ «`W8` cubre los DOS tramos posteriores» | ✓ «Es `[paso 4, paso 6)`, LOS DOS TRAMOS» |

**Unión = `[1,6)`. Sin huecos y sin solapes.** Ataqué por tres vías más: (a) la condición de detección de cada fila es observable en disco y no exige saber cuándo se cayó; (b) ninguna sede cita a otra como fuente de un reparto que aquélla no escriba —el punto 7 lo dice con esas palabras—; (c) `git show 7764cca` confirma que el punto 7 **sí se reescribió** esta vez, que era la acusación exacta del documento 22. **La corrección que dos gates no consiguieron, ésta la hizo, y con mecanismo.** Lo único que encontré es `S-23`, que es de disjunción sobre un estado inalcanzable.

**`RF-2` · Intenté que la propagación de `O17` fuera NOMINAL —cuatro implementaciones divergentes disfrazadas de una—. NO CAYÓ, y es la refutación que más quería ganar.**
Extraje las cuatro filas `FASE 0` de §18 (L9442, L9445, L9450, L9453), normalicé el nombre del macrocircuito y comparé: **son byte a byte idénticas**. Abrí los cuatro bloques de §8.1-§8.4 y los cuatro remiten a §9.6 con la misma frase, sin reescribirla. Conté `gate:sistema-conforme`: **veintitrés apariciones**, todas definición o invocación de la misma sede. **La regla 6 se cumple con más rigor del que exige.** Es lo mejor de esta tanda y no debe quedar sepultado bajo mis seis GRAVES.

**`RF-3` · Intenté que el motivo del Owner en `O17` fuera una racionalización del sistema disfrazada de decisión —que es lo que `L-02` encontró en `O16`—. NO CAYÓ como falsedad, PERO cayó como verificabilidad, y ése es mi `S-26`.**
Fui a §13 del documento 22 —lo que `S3` me pidió expresamente— y **coteje las tres alternativas palabra por palabra**:
- §13(a): «*Es la más barata y la que menos toca; a cambio, un producto ya instalado no revalida su Estructural cuando cambia el kernel*» ≡ `O17`(a): «*A FAVOR la más barata y la que menos toca · DESCARTADA porque un producto ya instalado NO revalidaría su Estructural cuando cambie el kernel*».
- §13(b) y §13(c): **igual de exactas.**
**`O17` dice la verdad cuando afirma que la pregunta y sus tres alternativas «están redactadas palabra por palabra en §13 de la adjudicación de `R`».** Lo verifiqué y es cierto.
**Y aquí está lo que `S3` no podía ver: el MOTIVO entrecomillado del Owner NO está en §13, y no puede estarlo.** §13 contiene la **pregunta**, escrita antes de que hubiera respuesta; el documento 22 se cierra sin ella. Luego el motivo no es ni cita ni paráfrasis **de §13**: es cita de la respuesta del Owner, y **su única sede en todo el árbol es `O17`** (`grep -rn` sobre `docs/` y `kernel/`: sólo `DECISIONES-Y-CONTRADICCIONES.md` L696-L700 y el checkpoint, que lo cita de ahí). Tres cosas la sostienen y las digo a favor: `O17` registra **tres alternativas con su A FAVOR y su motivo de descarte**, cosa que una racionalización posterior no necesita; el Owner elige **la opción MÁS CARA** y acepta expresamente el coste, mientras una formulación del sistema tendería a la barata; y `O17` declara procedencia, fecha y sede de la pregunta. **La sospecha NO cae. Lo que queda es que ningún gate puede verificar el motivo contra ninguna otra sede**, y `O16` recibió un ADDENDUM DE CRONOLOGÍA por exactamente esa razón. Es `S-26`, MENOR, y consta.

**`RF-4` · Intenté que alguna fila `D` u `O` preexistente se hubiera reescrito al meter `D107` y `O17`. NO CAYÓ.**
`git diff 7e99388 HEAD -- docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` → **379 inserciones, 3 supresiones**, y las tres supresiones son el párrafo `**Procedencia:** las ocho llegan de la revisión independiente de F3…`, **reinsertado byte a byte** en el hunk `@@ -281,0 +495,4 @@`. Es un **movimiento**, no una edición. Y la serie: **107 filas `D`, 107 valores únicos, mín 1, máx 107, `uniq -d` vacío, sin huecos**; serie `O` de 1 a 17, continua. **`D1`–`D106` y `O1`–`O16` conservan su texto íntegro.** La disciplina de inmutabilidad se cumple.

**`RF-5` · Intenté que los recuentos de presiones hubieran vuelto a caducar, que es donde este expediente se ha roto cuatro veces. NO CAYÓ en ninguna de las cinco sedes.**
Derivé: `grep -c '^## \`PN-'` → **18**; menos `PN-4` RETIRADA y `PN-5` FUSIONADA → **16 vigentes**. §16 dice DIECISÉIS y publica la resta; §0 dice DIECISÉIS y remite; el resumen de §16 (L9329) explica la derivación; y las tres sedes vivas del checkpoint **remiten y publican el comando**, que ejecuté y da 16. Los rangos vivos terminan todos en `PN-18`, la última cabecera vigente, y los que dicen `PN-12`/`PN-14` son citas rotuladas «Corregido por `I-11`» y «Corregido otra vez por `Q-07`». **Nada que reprochar.** Es la primera vez en este expediente que este censo aguanta un ataque.

**`RF-6` · Intenté que `C-L.5` estuviera mal clasificada o con estado compuesto, que fue `P-22`≡`Q-37`. NO CAYÓ.**
Su cabecera (L10156), su primer párrafo y su cierre dicen los tres **CERTIFICADA**, el estado anterior queda `[HISTÓRICO]` y no borrado, y la clasificación vigente del checkpoint cuadra: 8+2+1+1+1 = **13**, un estado primario por id, y las trece filas de detalle coinciden una a una con el resumen. **Ninguna de las trece está mal clasificada.**

**`RF-7` · Intenté que `PN-17` y `PN-18` ELIGIERAN en vez de registrar, que es lo que F4 no puede hacer. NO CAYÓ.**
Las dos abren con «**NO elige la grafía / la solución normativa y NO redacta ninguna enmienda**», y las dos traen los nueve elementos: fuentes enfrentadas con ruta y línea · texto vigente literal · **materia mínima formulada como pregunta al Owner y no como respuesta** · propietario **el Owner** · fase «F5 decide · F6 materializa» · prueba posterior que «**FALLA HOY, y tiene que fallar**» · qué bloquea · **qué NO bloquea** · condición de reversión. `PN-18` además **deriva sus propios recuentos y publica los comandos `grep`** con que se derivan. **Registrar es F4 y elegir es F5: en estas dos, se respeta.** Es exactamente lo que `P-07` y `P-08` del documento 22 pedían.

---

## 10 · LO QUE NO HE CUBIERTO, SIN ADORNO

1. **Ningún ojo único recorrió las 10 275 líneas del documento 11 seguidas.** Está leído íntegro por la cadena, en dos tramos disjuntos con corte en L5200. **Una contradicción cuyos dos extremos caigan a los dos lados de ese corte no la ve ninguno de los dos.** Lo mitigué cruzando yo mismo §8.0↔§18, §9.6↔§8.1↔§8.3, §9.2↔§9.3↔§8.3 y §2.6.6↔§2.6.9↔§2.6.5 — **no lo elimina, y `U` tiene que pesarlo.**
2. **Ninguna fuente del lote de `T`.** No he abierto `comprobar-correccion-gate-de-cierre.py`, ni `derivar-universo-obligatorio.py`, ni `verificacion/README.md`, ni `00-INDICE.md` íntegro, ni el `CORRIGENDUM`, ni los dos manifiestos del gate anterior, ni `CHECKPOINT-OPERATIVO.md`. **Todo lo que podría decir sobre `M-04`, sobre las quince protecciones nuevas y sobre el derivador juzgándose a sí mismo es nada: no lo digo.** Ejecuté la batería y da 37/37; **eso es un dato, no un juicio**.
3. **No he verificado NINGUNA cita que mis fuentes hacen de material externo.** `b.16` L836/L895, `a.6` L495/L502-503, `a.7` FRENO 3, `a.9`, `a.11`, `C7:82`–`C7:92`, `KERNEL.md` L687/L690/L694-712, `01-PROCESOS.md` L419/L434, `E2.4`. **Las he leído como afirmaciones de mis fuentes, no como hechos.** Es el hueco más grande de mi cobertura, y toca directamente a `S-01` y `S-05`: mi juicio de que `proceso:SIS` no admite `SEG` se apoya en la cita que `PN-13` hace de `b.16`, no en `b.16`.
4. **No he ejecutado nada del sistema, porque no hay sistema.** No existen `estado/`, `estado/tx/`, `estado/deriva/` ni `.ads/run/`: es la distribución, no un producto instalado. `S-02`, `S-03`, `S-04` y `S-23` son análisis de **texto contra texto**.
5. **`S-05` lo derivé de las filas de §18 tal como están escritas.** No he comprobado contra `b.1`/`b.16` si una fase declarada `proceso:SIS` con estado persistido propio cuenta necesariamente como **un item** a efectos del FRENO 3 de `a.7`. El documento lo afirma —«los ITEMS LÍDERES son las FILAS de la tabla de §18»— y yo aplico su propia regla; **si esa regla admitiera una excepción para una fase de precondición, la aritmética del freno podría salvarse y la cifra 2·4·2·4 no.**
6. **No he leído los documentos 19, 20 ni 21.** Todo lo que el documento 22 dice de ellos —los 24 hallazgos del 21, las cifras del 19 y del 20, el juicio sobre `N` y `O`— lo transcribo, no lo verifico.
7. **De los 69 hallazgos del documento 22 he adjudicado 24.** Los 45 restantes son del foco de `T` o viven en fuentes que no son de `S`. **No están cerrados por mí ni abiertos por mí: están sin adjudicar por mí.**
8. **No he verificado el contenido de `PN-17` y `PN-18` contra las fuentes que enfrentan** —(a), (b), `E2`, `01-PROCESOS.md`, `circuitos/`—. Verifiqué su **forma** (`RF-7`), que es lo que mi lote permite.
9. **`S-26` no es una acusación de falsedad y no puede serlo.** Nadie con acceso a este árbol puede verificar ni desmentir lo que el Owner dijo. Lo registro como límite de verificabilidad, y `U` decide si eso es materia de gate o no.

---

## 11 · MI RECOMENDACIÓN DE VEREDICTO, Y SUS RAZONES

> **Yo RECOMIENDO. El veredicto lo emite el adjudicador `U`, que no soy yo.** `U` recibe este dictamen ya cerrado y el de `T`, que no he visto. Puede revocar cualquiera de mis veintiséis adjudicaciones, mis seis rechazos y mis cinco rebajas. **Mi recomendación NO se emite por cobertura**: las cuatro fuentes asignadas a `S` están leídas íntegras y `asignadas − leídas = 0`.

# INSUFICIENTE PARA F5

### Las razones, numeradas. Las dos primeras bastan cada una por sí sola.

**1 · La FASE 0 que `O17` ordena crear NO ES EJECUTABLE tal como está escrita, y lo es por dos circularidades que este mismo corpus ya cerró una vez cada una.** El SUJETO que la fase exige **resuelto en su ENTRADA** contiene el identificador de una iniciativa que la propia fase **prohíbe abrir** (`S-02`) — es `D49` reproducido. Y su SALIDA es una celda canónica de `cobertura` que en `N` y en `A` **no tiene dónde escribirse**, porque `estado/` nace en `INS-0` y en `A0`, después de ella; con lo que la fase no es reanudable y vive en el chat (`S-03`) — es `D30` reabierto por delante. **Ninguna de las dos exige decidir arquitectura ni es materia del Owner**: exigen decir dónde nace el identificador de la ejecución y dónde se persiste su declaración antes de `INS-0`. Son clase `A`. Pero mientras no se digan, **el remedio del GRAVE nº 2 está escrito y no se puede ejecutar.**

**2 · La cadena de niveles sigue teniendo un eslabón sin productor que NADIE declara, y está en la sección escrita para no tapar huecos.** La Operativa se produce en **`INS-4` y en ningún otro sitio** —lo barrí sobre las 10 275 líneas—. §9.6 enumera los cuatro recorridos, declara honestamente que la **adopción** no tiene fase que produzca su Operativa, y titula ese bloque «**LA SALVEDAD, DICHA Y NO TAPADA**». **Cuatro líneas más arriba, en la misma enumeración, la migración tiene el mismo hueco y no se declara**: `M5` certifica Integrada, Integrada presupone Operativa, y `M3` —«migrar ESTADO PERSISTIDO, con su esquema»— **invalida la Operativa heredada** por el trigger literal de §9.3. §8.3 no la nombra ni una vez. **La honestidad de declarar un hueco y callar el idéntico en la misma frase es peor que no declarar ninguno**, porque el lector infiere que los otros tres recorridos están completos. Es `S-04`, y la abstención correcta de `O17` no lo cubre: no falta una decisión del Owner, falta **declarar**.

**3 · La propagación de `O17` EXCEDE la resolución del Owner en la sede que manda, y se contradice a sí misma dentro de una sola tabla.** `O17` da a `SEG` **bloqueo**. La fila `D107` le da bloqueo. §9.6, la sede única, le da bloqueo. **§18 le da «vía 3» en `proceso:SIS`** —cuatro veces— cuando `b.16` no la declara ni obligatoria ni condicional, cuando §8.0 prohíbe expresamente ensanchar un proceso por conveniencia, y cuando **la propia tabla escribe «`SEG` sin vía: `PN-13`» en otras dos filas del mismo proceso**. Y §18 es la sede que §8.0 declara que MANDA, con una regla de precedencia que choca con la de §9.6 y que nadie ha jerarquizado (`S-01`, `S-09`). Es `PN-13` —la única presión que va al Owner por materia nueva— violada por la tanda que la lleva.

**4 · Una cifra que la única sede que la publica declara «DERIVADA de §18» ya no deriva de §18, y con ella se cae una conclusión publicada sobre material APROBADO.** §8.0 dice «los ITEMS LÍDERES son **las FILAS de la tabla de §18** … **El recuento se DERIVA de §18 y se mueve con ella. No se escribe aparte**», y publica **2·4·2·4**. §18 tiene hoy **3·5·3·5**, porque `D107` le añadió una fila por macrocircuito. Y la consecuencia no es cosmética: con la `FASE 0` dentro de la racha, **`U` pasa a tener TRES items `SIS` consecutivos**, el FRENO 3 de `a.7` —«más de dos»— **sí llega a evaluarse**, y la conclusión «**Ninguno de los cuatro necesita excepción del Owner**» deja de estar derivada, **precisamente en el macrocircuito donde el antecedente del freno es plausible**, porque `U` corre sobre un producto instalado y operando. El propio §8.0 descartó como fundamento el único salvavidas que quedaría. Es `S-05`.

**5 · El remedio del hallazgo que este gate me mandó dictaminar reintroduce, bajo el rótulo «DERIVADA HOY», exactamente el defecto que venía a cerrar — y caducó DENTRO de la tanda que lo escribió.** El ADDENDUM de `D97` acota bien el material y se fecha, y eso era lo pedido. Pero publica **cuatro cifras escritas a mano**, **dos de ellas falsas hoy**, bajo el título «*LA CIFRA, DERIVADA HOY y no copiada*» y con el remate «*Su cifra **se deriva del árbol en cada lectura***». **Nada la deriva:** son cuatro literales, `G-13` sólo contrasta tres de las cuatro líneas, y las cuatro son **verbatim las que `P4` y `R` publicaron en el documento 22** — se copiaron del hallazgo, no del árbol. Y la caducidad es reproducible con `git`: correcta en `78ec1cc`, falsa en `609863e`, **un commit después, el mismo día, la misma tanda**. La sede primaria había hecho lo correcto —`PN-15` escribe «*el documento 11 las nombra **muchas veces***», **sin número, para que no envejezca**— y el registro lo deshizo. Es `S-06`.

**6 · Y la razón de método, que es la que impide cerrar aquí.** **Dieciséis de mis veintiséis hallazgos los introdujo o los dejó pasar esta misma tanda**, y varios son el defecto que el propio documento 11 nombra en su §0 como el más repetido del corpus, cometido **en el acto de corregirlo**: `P-16` reclasificó `4b` y dejó el titular «siete secuencias» sobre ocho (`S-10`) y dos sedes sin convertir bajo una declaración de barrido completo (`S-14`); `P-09` auditó el bloque de `fsync` y corrigió el remate de la lista y no el cardinal que la introduce catorce líneas después (`S-11`); `M-5`/`M-6` ampliaron un conjunto a seis y dejaron dos afirmaciones razonando sobre cuatro, con lo que `DSP` y `ENC` quedan hoy **sin declaración de si generan presión normativa** (`S-13`). **La regla que falta no es difícil y el corpus la tiene escrita**: es la que §2.6.6 se aplicó a sí misma —«*el remate deja de ser un cardinal*»— extendida a **todo titular sobre enumeración**.

---

### Y lo que expresamente NO fundamenta mi recomendación

- **NO recomiendo por cobertura.** `asignadas a S − leídas íntegras = 0`. Las cuatro fuentes están leídas enteras, los cuatro SHA-256 que recalculé coinciden con el manifiesto, y la única reserva —ningún ojo único sobre el documento 11— está declarada.
- **NO recomiendo por `O17` ni por `D107`.** La resolución del Owner es de él, `D107` **se declara derivada y lo es**, y la propagación es la más disciplinada que este expediente ha producido: una sede única, cuatro invocaciones byte-idénticas, doce reglas trazadas, nueve contraescenarios propios, y una declaración honesta de lo que no resuelve. **Nueve de las doce reglas se cumplen sin reserva.**
- **NO recomiendo por el hueco de la Operativa en la ADOPCIÓN.** Está **declarado, con propietario, fase y prueba que falla hoy**, y no ampliarlo era lo correcto: `O17` da productor al Estructural y a ninguno más. **Eso es exactamente lo que F4 debe hacer.** Lo que fundamenta mi razón 2 es el hueco **no declarado** de la migración.
- **NO recomiendo por `W17`/`W8`/el punto 7.** Era el punto que la historia señalaba como el más probable y **está bien HOY**: los tres tramos reparten `[1,2)`, `[2,4)` y `[4,6)` sin hueco y sin solape, y las tres sedes coinciden. `P-01` y `P-02` están cerrados con mecanismo, y `R-04` —dos gates sin caer— por fin cayó (`RF-1`).
- **NO recomiendo por el validador en rojo.** El `12/13` y el `T147 FALLIDA` los causa **el manifiesto que el aparato de ESTE gate añadió en `c36d2ba`**, no la tanda. Lo demostré con `git show --stat` y con el diff de evidencia: el único fichero de corpus añadido desde `e316396` es ése. **Sobre el árbol de la tanda el runner daba 13/13 y `git status` quedaba vacío.** Rechacé la imputación de mi propio relevo (`X-3`).
- **NO recomiendo porque quede arquitectura por inventar.** **Ninguno de mis veintiséis hallazgos es BLOQUEANTE. Los veintiséis son clase `A`.** `S-01` se cierra borrando dos palabras de cuatro filas. `S-02` y `S-03`, diciendo dónde nace el identificador y dónde vive la declaración antes de `INS-0`. `S-04`, **declarando** el hueco como ya se declaró el de `A`. `S-05`, recontando. `S-06`, derivando cuatro cifras o retirándolas como hizo `PN-15`. Ninguno exige decidir entre alternativas válidas que una resolución vigente no resuelva, y **ninguno es materia del Owner**.
- **NO recomiendo por `M-04` ni por la batería.** **No las he leído: son foco de `T`.** Mi recomendación se sostiene entera sin ellas, y si `T` encontrara que las quince protecciones nuevas generalizan de verdad, **mi recomendación no cambiaría**: las razones 1 y 2 la determinan por sí solas.

---

### Lo que consta a favor, y no es cortesía

Este corpus ha hecho en esta tanda cosas que no había hecho en trece: **cerró `R-04`**, que dos gates no pudieron; **retiró cifras en vez de reescribirlas** —`m-1` de §8.2 dice hoy «Hoy son MÁS» y no da número, y `rama_de_trabajo` dice «NO SE ESCRIBE AQUÍ, Y ES DELIBERADO»—; **hizo que §0 remitiera en vez de enumerar**; **le dio a §15.8 un bloque por tanda** y con ello la regla del ordinal por fin ejecuta; **registró dos presiones nuevas sin elegir ninguna**, con sus nueve elementos y su prueba que falla hoy como debe; y **propagó una resolución del Owner con una sede única y cuatro invocaciones byte-idénticas**, declarándola derivada y absteniéndose donde debía abstenerse. **Diecinueve de los veinticuatro hallazgos del documento 22 que caen en mi foco están cerrados, y varios con mecanismo y no con prosa.**

**Y aun así no recomiendo cerrar, por la razón que este expediente lleva trece tandas persiguiendo y que esta vez tengo en su forma más limpia: la fase que la resolución del Owner ordena crear está escrita entera, con contrato, sujeto, vigencia, invalidación y nueve contraescenarios — y no se puede ejecutar, porque pide en su entrada algo que sólo existe después de ella y escribe su salida en un sitio que todavía no existe.**

---

## 12 · CIERRE

```text
git status --porcelain   AL ABRIR    →   (salida vacía)     primer comando de la sesión
git status --porcelain   AL CERRAR   →   (salida vacía)     último comando de la sesión
HEAD al abrir y al cerrar            →   c36d2ba707eed5ea24b9a13df6c4e6be49b68cc6, idéntico
RAMA                                 →   gate/f4c-certificacion-2-20260830

FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ   ninguno
COMMITS · PUSH · PR · MERGE                                     ninguno
EXPERIMENTOS      una copia completa del árbol fuera del repositorio, en el scratchpad,
                  donde ejecuté `registrar_evidencia.py` —que sí escribe evidencia—.
                  COPIA BORRADA con `rm -rf`. El árbol real nunca se ensució
SUBAGENTE `Agent`                                               NO USADO
FICHEROS `T1.md` · `T2.md` · `DICTAMEN-T.md`                    NO ABIERTOS
NINGÚN HALLAZGO SE HA CORREGIDO, y es deliberado: quien corrige no certifica.
```

**`F4c` sigue ABIERTA por mi parte. `F5` NO queda autorizada por mi parte.**

**REVISOR `S` · dictamen cerrado por `S4`.**

---

# §B · DICTAMEN DEL REVISOR `T`, LITERAL

# DICTAMEN DEL REVISOR `T` — SEGUNDO GATE INDEPENDIENTE DE CERTIFICACIÓN DE F4c
## Emitido por `T3`, DICTAMINADOR de la cadena `T`

```text
REPOSITORIO   /home/jose/ads-kernel
RAMA          gate/f4c-certificacion-2-20260830
HEAD          c36d2ba707eed5ea24b9a13df6c4e6be49b68cc6   (idéntico al abrir y al cerrar)
FECHA         2026-08-30
INTÉRPRETE    Python 3.12.14 (shim del scratchpad)
LABORATORIO   /tmp/lab-T3/ — copias `cp -a`, BORRADO al cerrar
RECOMENDACIÓN INSUFICIENTE PARA F5   (el veredicto lo emite `U`, no yo)
```

## 1 · IDENTIDAD, INDEPENDENCIA Y MODO

Soy `T3`. Cierro el dictamen del **REVISOR `T`** y **no emito veredicto**: lo emite el
adjudicador `U`.

**Qué NO soy.** No he escrito ninguna parte de este corpus. No he aplicado ninguna corrección.
No he sido revisor `A`–`R` ni `P1`–`Q5` de ningún gate anterior. No participé en el gate del
documento 22.

**Qué NO he visto, y lo declaro sin que nadie pueda comprobarlo por mí salvo por su ausencia en
este texto.** **No he abierto `S1.md`, `S2.md`, `S3.md` ni `DICTAMEN-S.md`.** Los cuatro constan
en el listado del directorio de notas —`DICTAMEN-S.md` con 101 bytes a las 15:13— y **no los he
leído**. Ninguna afirmación de este dictamen procede del revisor `S`, y ninguna de mis
adjudicaciones toca su foco.

**El orden se respetó, y es la garantía de que este dictamen busca en vez de confirmar.** Leí
íntegras `T1.md` y `T2.md`; después **reproduje con mis manos** los cinco árboles que `T1`
declara BLOQUEANTES y las tres afirmaciones que el encargo me manda comprobar de `T2`; y **sólo
entonces** abrí el documento 22. Ninguno de mis experimentos está informado por lo que el
documento 22 dice de sí mismo.

**Modo, comprobado en los dos extremos:**

```text
git status --porcelain  AL ABRIR    → SALIDA VACÍA   (primer comando de la sesión)
git status --porcelain  AL CERRAR   → SALIDA VACÍA   (último comando de la sesión)
HEAD al abrir y al cerrar           → c36d2ba707eed5ea24b9a13df6c4e6be49b68cc6, idéntico
FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MÍ   ninguno
COMMITS · PUSH · PR · MERGE                                     ninguno
SUBAGENTE `Agent`                                               NO USADO
```

**Todos los experimentos se ejecutaron sobre copias `cp -a` en `/tmp/lab-T3/`**, fuera del
repositorio, y el laboratorio se borró al terminar. Los dos únicos comandos que ejecuté **sobre
el árbol real** son `comprobar_referencias.py` y las lecturas: ninguno escribe. **No ejecuté
`registrar_evidencia.py` sobre el árbol**, precisamente porque `T2` documentó que ensucia dos
ficheros de evidencia; lo di por medido por él y lo verifiqué por otra vía.

**No corrijo nada, y es deliberado.** Quien corrige no certifica.

---
## 2 · MANIFIESTO DE LECTURA DEL REVISOR `T`

Unión de los manifiestos de `T1`, `T2` y el mío. **Los nueve SHA-256 y los nueve `wc -l` los he
recalculado YO** sobre el árbol de `c36d2ba`, incluidos los de las fuentes que leyeron otros
relevos. **Los nueve coinciden** con los que declaran `T1` y `T2` y con los que publica
`F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` §4.

| # | ruta | líneas | SHA-256 recalculado por mí | leyó | cobertura | 1.ª / última sección sustantiva | ancla A · ancla B (regiones separadas) |
|---|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` | 2685 | `5f39512d16594e2c103a432db5a1bcae736b7bfe397ac7e078b7d1bfe1fe14db` | **T1** | **LEÍDO ÍNTEGRO** · 12 tramos consecutivos 1-200…2560-2685, **sin tramos no abiertos** | L19 `RAIZ = os.path.abspath(...)` / L2685 `sys.exit(_informe())` | L1657 `CAPACIDADES = ["APR", "ARQ", …` · L2062 `# ── G-28 · VEREDICTO, POLARIDAD y ESTADO …` |
| 2 | `docs/evolucion/verificacion/README.md` | 133 | `7b9fae2c65f1e2311c68218110d87aa64aac84ae66c0855d8a0e4309b4f22de4` | **T1** | **LEÍDO ÍNTEGRO** (una pasada) | L1 `# Verificación mecánica…` / L120 `## El derivador del universo obligatorio` | L34-36 «`G-29` … **sólo admite una ampliación de `verificacion/` si este README la enumera**» · L103-104 «NO PROTEGE CONTRA UNA…» |
| 3 | `docs/evolucion/verificacion/derivar-universo-obligatorio.py` | 410 | `6753a245103dcc5a558bfb39336c0e43b5e032d146dd03f7ded4861c0f5659a8` | **T2** | **LEÍDO ÍNTEGRO** · 3 tramos 1-110 · 110-240 · 240-410 | docstring L3-5 / L409-410 `if __name__ == "__main__"` | L44 «*sale con código 2 y diagnóstico*» · L327 «*`ENCARGO` es lo único escrito a mano de todo el derivador*» |
| 4 | `…/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` | 316 | `fc4d1c2fdedbcb13be512e88303e21eddbeb194f6cc38b8e50fa0612dad08bbc` | **T2** | **LEÍDO ÍNTEGRO** · 3 tramos 1-105 · 105-215 · 215-316 | L10 `## 1 · Objeto del reparto` / L294 `## 8 · Regla de cierre` | L29 «*Aquí el universo no se escribe: se deriva*» · L214 «*no hay tercera vía y no hay presunción*» |
| 5 | `…/manifiestos/F4C-ADDENDUM-1-GATE-CERTIFICACION-20260830.md` | 119 | `b1c29244dfedc139ff7e80a6167d200803d054f25554c75f31303fea5687a434` | **T2** | **LEÍDO ÍNTEGRO** (`cat -n`) | L8 `## 1 · El motivo, dicho sin suavizar` / L109 `## 5 · Lo que este addendum NO hace` | L19 «*Veintiuna de esas treinta y tres no cumplen esa regla*» · L112 «*Sigue en `44d2e74`, con su error dentro*» |
| 6 | `docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md` | 131 | `274192d416368cb5a7ec3a0b07bc2e5dd97fffb5502c21d4dd3be5703c20b0ea` | **T2** | **LEÍDO ÍNTEGRO** (`cat -n`) | L16 `## 1 · Documento 20 · …` / L122 `## 6 · Regla general…` | L13-14 «*Toda cifra … se DERIVA … Ninguna se copia*» · L129-130 «*NO PUEDE CITARSE … sin citar también la entrada que la acota*» |
| 7 | `docs/evolucion/00-INDICE.md` | 148 | `004cad57881dc75d08cae8311c5e9b4334cd7c424330769657fcf11d3557ab1b` | **T2** | **LEÍDO ÍNTEGRO** · 3 tramos 1-60 · 60-110 · 110-148 | L14 `## Los documentos en voz del Owner` / L143 `## Lo que este trabajo ha corregido de sí mismo` | L104-108 «*deja el árbol que juzga con un validador canónico en rojo*» · L119-121 «*la lista se deriva con `find …`*» |
| 8 | `docs/rediseno/CHECKPOINT-OPERATIVO.md` | 195 | `d2131faa4aeddc6d66e98f5eb88d6d9d172a8910b174a1866eecc969633818bb` | **T2** | **LEÍDO ÍNTEGRO** · 2 tramos 1-100 · 100-195 | L23 `## Estado` / L150 `## Siguiente acción exacta` | L88-90 «*`git status --short`  # tiene que quedar vacío*» · L103-112 «*sólo si la evidencia derivada se republica en el MISMO commit*» |
| 9 | `docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md` | 3478 | `3e2bdece758e6b69d6695bb52f20d21b910a123a27ac643845dbad75e8355f1c` | **T3 (yo)** | **LEÍDO ÍNTEGRO**, y **DESPUÉS** de mis experimentos · 12 tramos consecutivos `1-440 · 440-900 · 900-1160 · 1160-1420 · 1420-1680 · 1680-1940 · 1940-2200 · 2200-2460 · 2460-2720 · 2720-2990 · 2990-3250 · 3250-3478`. **Unión = [1, 3478]. Ningún tramo sin abrir.** | L7 `## 0 · Qué es este documento, y qué NO es` / L3350 `## 14 · VEREDICTO`, cerrado en L3478 | **L3** «*Veredicto del adjudicador `R`: `INSUFICIENTE PARA F5`*» · **L2820** (a 2817 líneas) «*`R-N1` · GRAVE · `G-22` sólo fija `docs/evolucion/1[5-8]-`*» |

### La resta, explícita

```text
FUENTES ASIGNADAS A `T`   9   Derivadas por mí de §4 y §6 del manifiesto
                              `F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md`, que reparte
                              «REVISOR T · 9 fuentes · T1 la batería · su README · T2 el
                              derivador · los dos manifiestos · el CORRIGENDUM · 00-INDICE ·
                              CHECKPOINT-OPERATIVO · T3 documento 22». Las conté: 2+6+1 = 9

FUENTES LEÍDAS ÍNTEGRAS   9   T1 2 · T2 6 · T3 1

ASIGNADAS − LEÍDAS ÍNTEGRAS  =  0     CERO. Ninguna fuente asignada a `T` quedó sin abrir.
```

### La reserva de cadena, declarada contra mi propio interés

**Ningún ojo único recorrió las 2 685 líneas de la batería y las 3 478 del documento 22
seguidas.** El manifiesto declara ese coste por delante y yo lo confirmo. Lo mitigué en la
dirección que importa para mi encargo: **reabrí por mi cuenta** las regiones de la batería que
sostienen cada hallazgo que adjudico —`G-01` L204-286, `G-15` L604-790, `G-16` L1256-1272,
`G-20` L1435-1445, `G-22` L1462-1540, `G-26` L1784-1845, `G-28` L2091-2116, `G-29` L2149-2260,
`G-30` L2264-2385, `G-33` L2519-2683— y **ejecuté** cada afirmación en vez de leerla. No lo
elimina, y el adjudicador `U` tiene que pesarlo.

### `T2` y los documentos 19, 20 y 21: mi decisión, dicha entera

`T2` declara que extrajo **líneas sueltas** de los documentos 19, 20 y 21 con `sed -n 'Np'` y
que corrió `grep -n` para localizar cadenas — nombrando exactamente cuáles: doc 21 L380-383,
L395-396, L399-401, L1056-1058; doc 20 L61-62, L74-85, L127-129, L368, L372, L628, L638, L651,
L656; doc 19 L310, L898-899.

**Mi decisión: NO compromete la independencia de `T`, y sí acredita un defecto del reparto.**
Tres razones, y la tercera va contra el interés de mi propia cadena.

1. **Los tres documentos no son de nadie en este gate: son fuentes AGOTADAS** (§5 del manifiesto,
   filas 9, 10 y 11). Ningún revisor tiene asignada su lectura, y la prohibición de `T2` procede
   de su encargo, no de una regla de cobertura. Abrir una línea nombrada de una fuente agotada
   **es exactamente lo que la regla 1 del agotamiento obliga a hacer para verificarla**.
2. **El encargo de `T2` le pidió dos cosas incompatibles**: recalcular la regla 1 de los
   agotamientos —que vive en el documento 21— y no abrir el documento 21. `T2` resolvió por la
   extracción mínima **y la declaró**, en vez de presumir la regla o callar la vía. Es la
   conducta correcta ante un encargo contradictorio.
3. **Y por eso lo registro como defecto del reparto, no como falta de `T2`:** es la misma clase
   que el `C-2` que el adjudicador `R` reprochó al coordinador del gate anterior —«*se le pidió a
   un revisor un foco sin darle la fuente*»— y **este gate la ha repetido**. Va como `T-11`.

**Lo que sí descuento:** las siete filas del §3 de `T2` que se apoyan en las citas del documento
21 las tomo **sólo en la mitad que él verificó mecánicamente** —la regla 2, identidad de bytes con
`7764cca`, que no requiere abrir nada—. La regla 1 la doy por **declarada, no por certificada por
`T`**, y lo digo aquí en vez de esconderlo detrás de un «SE SOSTIENE».

---
## 3 · `M-04`: LO QUE REPRODUJE YO
Laboratorio `/tmp/lab-T3/`, copias `cp -a`. Intérprete Python 3.12.14 por el shim.
**BASELINE** `/tmp/lab-T3/base`, porcelain vacío: `37/37 comprobaciones en verde` · `EXIT=0`.

### R-A · `T1-03` · segunda sede canónica como documento numerado — **REPRODUCIDO · VERDE**
Dos ficheros SIN RASTREAR en `docs/evolucion/`: `23-SEGUNDA-SEDE-NORMATIVA.md` (cabecera
«CONTRADICE `C4-MATERIALIZACION` y `C7-GOBIERNO` y PREVALECE sobre los dos» + copia íntegra de
`docs/rediseno/a-CAPACIDADES-APROBADA.md`) y `24-REGISTRO-ALTERNATIVO.md` (el registro de
decisiones con `D87` alterada).
Salida: **`37/37 comprobaciones en verde` · `EXIT=0`**. Y las dos comprobaciones que existen
para esto **los nombran mientras imprimen `OK`**:
```
OK   G-22 … 27 inmutables derivados … · 2 todavía sin confirmar y por tanto sin línea base:
     ['docs/evolucion/23-SEGUNDA-SEDE-NORMATIVA.md', 'docs/evolucion/24-REGISTRO-ALTERNATIVO.md']
OK   G-29 … 296 ficheros en 3 zonas, todos publicados o clasificados · cero duplicados byte a byte
```
Causa, verificada en el código, L2194-2195:
`if re.match(r"^docs/evolucion/\d\d-.*\.md$", rel): return True   # el documento que un gate nuevo publica`
Un `return True` sin mirar el contenido. **CONFIRMO `T1-03`.**

### R-B · `T1-04` · el README se autoriza a sí mismo — **REPRODUCIDO · VERDE**
`_INSTRUMENTAL = set(re.findall(r"`(docs/evolucion/verificacion/[A-Za-z0-9_.-]+)`", _t_readme))`
(L2181) deriva del README, y el README no está en ningún inventario de integridad.
Añadí al README `` `docs/evolucion/verificacion/bateria-2.py` ``, creé esa segunda batería
(imprime «37/37 comprobaciones en verde», `sys.exit(0)`) **y además renombré `G-30` a
`G-30-ANULADA` en toda la tabla del README**.
Salida: **`37/37` · `EXIT=0`**, con ` M docs/evolucion/verificacion/README.md` en el porcelain.
**CONFIRMO `T1-04`.** La autorización es circular: el guardado escribe su propia autorización.

### R-C · `T1-01` · veredictos volteados y confirmados — **REPRODUCIDO · VERDE**
```
grep -c 'INSUFICIENTE PARA F5' docs/evolucion/21-…md        -> 15
sed -i 's/INSUFICIENTE PARA F5/SUFICIENTE PARA F5/g'  doc 21     (15 sustituciones)
sed -i 's/INSUFICIENTE PARA F5/SUFICIENTE PARA F5/g'  F4C-ASIGNACION-GATE-CIERRE-20260829.md
git commit -aqm "…"   ->  git status --porcelain VACÍO
```
Salida: **`37/37` · `EXIT=0`**, con
`OK G-22 … 25 inmutables … intactos frente a HEAD y a 05f71b7` y
`OK G-28 … 25 documentos de gate contrastados contra HEAD … sin una sola inversión`.
Causa verificada: L1521-1531. El primer brazo (`rel in _mod_head`) sólo ve el árbol de trabajo;
el segundo (`if rel in _base_arbol and rel in tocados`) exige existir en `05f71b7`. Derivé la
lista yo: **ocho de los veintisiete inmutables no existen en `05f71b7`** — documentos 19, 20,
21, 22 y los cuatro manifiestos. Para ellos el segundo brazo es inalcanzable. **CONFIRMO `T1-01`.**
*Corrección a `T1`:* su tercer `sed` (`NO SUPERADO`→`SUPERADO` en el documento 20) fue un
**no-op**: `grep -c 'NO SUPERADO'` sobre el documento 20 devuelve **0**. El hallazgo se sostiene
íntegro con los otros dos; la cita de `T1` es imprecisa en ese renglón.

### R-D · `T1-02` · validador vaciado, evidencia falsificada, huella reanclada — **REPRODUCIDO · VERDE**
```
echo 'import sys; sys.exit(0)   # VALIDADOR VACIADO POR T3' > kernel/operativo/validadores/comprobar_negativos.py
printf 'FUENTES: 0 fallos (falsificado por T3)\n'     > …/evidencia/fuentes-salida.txt
printf 'NEGATIVOS: 0 fallos (falsificado por T3)\n'   > …/evidencia/negativos-salida.txt
printf 'REFERENCIAS: 0 fallos (falsificado por T3)\n' > …/evidencia/referencias-salida.txt
```
Primera pasada: `FALLO G-30 … el árbol deriva `dc11d6fb1f457a7e` sobre 255 ficheros`.
**La propia batería me publica la huella que necesito.** La escribo y confirmo:
```
printf 'dc11d6fb1f457a7e\n' > kernel/.upstream-hash     (antes: 6098b1e58579130a)
git commit -aqm "…"    ->  git status --porcelain VACÍO
cat kernel/operativo/validadores/comprobar_negativos.py
   import sys; sys.exit(0)   # VALIDADOR VACIADO POR T3
```
Salida: **`37/37` · `EXIT=0`**, con
`OK G-30 … 16 ficheros del kernel con clase declarada (4 clases) · ninguno difiere de HEAD ·
huella recalculada sobre 255 ficheros = dc11d6fb1f457a7e`.
**CONFIRMO `T1-02`, y es el resultado más grave de todo mi lote.** El validador que corre las
67 mutaciones negativas está vaciado, su evidencia es inventada, y la batería certifica el
árbol. La comprobación escrita para cerrar este contraejemplo exacto lo readmite añadiendo
`git commit`.

### R-E · `T1-19` · `G-22` y `G-28` NO fallan cerrado — **REPRODUCIDO**
`git` falso en el `PATH` (`#!/bin/sh` + `exit 0`, sin stdout): **`31/37`**. Fallan `G-11`,
`G-11b`, `G-21`, `G-23`, `G-29`, `G-30`. **`G-22` y `G-28` imprimen `OK`**, con los títulos
que dicen literalmente «(falla CERRADO sin git)»:
```
OK G-22 … 25 todavía sin confirmar y por tanto sin línea base: [los 25, uno a uno]
OK G-28 … 0 documentos de gate contrastados contra `HEAD` … sin una sola inversión
```
`_git()` sólo devuelve `None` cuando el comando **falla**; con salida vacía y éxito,
`_head_arbol` es el conjunto vacío y los bucles se saltan entero su cuerpo
(L1521-1523 `continue`, L2099-2100 `continue`). **CONFIRMO `T1-19`.** Un verde sobre cero que
se autodocumenta en su propio detalle.

### R-F · `T2-08` · cuatro pruebas negativas vacuas — **REPRODUCIDO EN `HEAD`, SIN MUTAR NADA**
En el árbol limpio `c36d2ba`:
`python3 kernel/operativo/validadores/comprobar_referencias.py --exclusiones`
→ `T147 FALLIDA … F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md: … Existe para nadie` ·
`0 superadas · 1 fallidas` · **`EXIT=1`**.
Con `T147` ya en rojo, convertí `m_documento_huerfano_con_nombre_repetido` en `return  # NO-OP`:
```
OK   N147    A-05  T147  documento huérfano cuyo nombre base coincide con otros dieciocho
OK   N147b   OK   N147c   OK   N147d
67 infracciones detectadas · 0 NO detectadas          EXIT=0
```
**CONFIRMO `T2-08`.** Y lo AMPLÍO: `grep -c 'Mutacion('` da **63** mutaciones y `grep -c 'espera='`
da **10**. **Cincuenta y tres mutaciones carecen del campo que el propio fichero declara
imprescindible** (L47-49: «*Sin él, una mutación se da por detectada porque la prueba falló, sin
comprobar que falló POR ESO*»). Hoy sólo cuatro son vacuas porque sólo `T147` está roja; el
mecanismo cubre 53.

### R-G · `T2-05` · el rango erróneo, vivo en la sede editable — **CONFIRMADO**
`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` L10192-10194, literal:
«*incluidos el BLOQUE B (§8–§12, certificación por niveles) y el **BLOQUE C (§13–§15,
iniciativa y dosier vivo)** — las fuentes de `P4`, `P9` y `P10`, que ningún revisor contrastó*»
El bloque real: `# BLOQUE C` en L1019, `# BLOQUE D` en L1137, y entre ambos
`awk '/^## /'` devuelve **§13, §14, §15, §16, §17 — CINCO secciones**.
**CONFIRMO `T2-05`.** El corrigendum acota el documento 19 por este error exacto y deja intacta
la norma viva que el `componente_i` del derivador parsea. §16 y §17 quedan fuera para quien
obedezca `C-L.5` al pie de la letra.

### VEREDICTO SOBRE `M-04`: **SIGUE VIVA.**
Reproduje **seis árboles defectuosos en `37/37` VERDE con `EXIT=0`** (R-A, R-B, R-C, R-D, y el
verde-sobre-cero de R-E) y **una instancia viva en `HEAD` sin mutar nada** (R-F). No es una
sospecha: es ejecutable, con salida pegada. `M-04` sobrevive a su tercer gate.

### R-H · `T1-08` · negar `O17` entera y borrar `D107` — **SÉPTIMO ÁRBOL EN VERDE**
`grep -n 'O17'` sobre la batería devuelve **cinco líneas, y las cinco son comentarios o texto de
diagnóstico** (L2458, L2502, L2519, L2522, L2604). **Ninguna línea de código lee la fila
`| O17 |`.** `G-21` protege `O1`-`O16` (L1442, L1452) y se detiene justo antes.
Sustituí la fila `| O17 |` del registro por su NEGACIÓN EXACTA («ANULADA: la certificacion NO
necesita productor, la reutilizacion de evidencia es LIBRE aunque cambien todas las huellas, no
hace falta declaracion propia, se puede copiar la anterior y cualquier nivel se alcanza sin el
Estructural») **y borré la fila `| D107 |` entera**.
Salida: **`37/37 comprobaciones en verde`**.
**CONFIRMO `T1-08`.** El comentario de L2519-2522 —«*Protecciones 12, 13, 14 y 15, todas
derivadas de `O17` y de su propagación `D107`*»— **describe una derivación que no existe**. Se
puede anular la resolución del Owner que este gate existe para certificar, borrar su propagación,
y las cuatro protecciones que dicen derivarse de ella siguen en verde.

---
## 4 · ¿GENERALIZAN LAS QUINCE PROTECCIONES?

**Criterio.** Una protección GENERALIZA si cierra la CLASE del contraejemplo. Cierra su
PERÍMETRO si sólo cierra la instancia, y basta un desplazamiento trivial —un directorio, una
línea, un `git commit`, una etiqueta— para reinstalar el defecto. Cada fila trae **mi** prueba,
ejecutada por mí, no la de `T1`.

| # | dónde | qué prometía cerrar | ¿generaliza? | mi prueba, ejecutada |
|---|---|---|---|---|
| **1** | `G-22` L1481-1540 · inventario | inventario de inmutables DERIVADO en vez del rango escrito `1[5-8]` (`R-N1` del doc 22) | **PARCIAL** | El inventario **sí** se derivó y **sí** creció: hoy son **27** y los documentos 19-22 y los cuatro manifiestos entran. **REF-1 (mía):** editar el manifiesto `F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md` sin confirmar → **`FALLO G-22`, 36/37**. La mitad de `R-N1` **está cerrada**. Pero **R-C**: los mismos volteos **confirmados** → **`37/37` verde** |
| **2** | `G-26` L1784-1845 · marca histórica | que la marca no se ponga con una PALABRA suelta («regresión»), sino con una ETIQUETA estructural | **NO** | **P2a control:** cifra viva falsa en doc 11 L1541 (`Cuarenta y seis`→`Diecisiete`) → **`FALLO G-26`, 36/37**. **P2b ataque:** la MISMA cifra falsa con **una sola línea** `> **[ESTADO ANTERIOR · esto es de otra tanda]**` encima → **`37/37` VERDE**. Se cambió el tamaño del interruptor, no se quitó |
| **3** | `G-16` L1256-1272 | contraste del estado `C-L` por IGUALDAD EXACTA, no por prefijo | **SÍ** | Reescribí la fila vigente de `C-L.1` a «CERRADA SOLO EN PARTE, SIGUE ABIERTA Y BLOQUEA F5» → **`FALLO G-16`**, con el diagnóstico exacto: «*El contraste es por IGUALDAD, no por prefijo: una calificación añadida detrás cambia el estado*». No encontré evasión |
| **4** | `G-01` L204-286 | polaridad en vez de la mera presencia de «RETIRADA» | **SÍ** | Inserté en §16 el párrafo que **deroga** la retirada de `estado/cuarentena/` usando la palabra «RETIRADA» → **`FALLO G-01`**: «*cada mención se juzga por POLARIDAD y la sede canónica la ancla*». No encontré evasión |
| **5** | `G-29` L2149-2260 · conjuntos | extender la comparación de conjuntos de `kernel/` a todo el material normativo | **NO** | **R-A:** dos ficheros `docs/evolucion/NN-*.md` —uno declarando «CONTRADICE `C4` y `C7` y PREVALECE», con copia del material APROBADO— → **`37/37` verde**, por `L2194-2195: return True`. La zona se amplió de 1 a 3 directorios y se abrió un `return True` en blanco dentro de la nueva |
| **6** | `G-30` L2264-2385 · excepción del kernel | fijar la excepción por CONTENIDO y CLASE, con la huella RECALCULADA | **NO** | **R-D:** validador a `sys.exit(0)`, tres evidencias falsificadas, huella reanclada con **el valor que la propia batería publica al fallar**, `git commit` → **`37/37` verde**. La clase `CÓDIGO DE VALIDADOR` es «idéntico a `HEAD`», y `HEAD` lo escribe quien edita |
| **7** | `G-22` L1520-1531 · doble contraste | contrastar cada inmutable contra `HEAD` **y** contra la revisión base `05f71b7` | **NO** | Derivé la lista yo: **8 de los 27 inmutables no existen en `05f71b7`** —docs 19, 20, 21, 22 y los cuatro manifiestos—. Para ellos `if rel in _base_arbol and rel in tocados` es inalcanzable. **R-C** lo explota |
| **8** | `G-28` L2091-2116 | que ningún documento de gate cambie de veredicto «en silencio» | **NO** | **R-C:** 15 volteos `INSUFICIENTE`→`SUFICIENTE` en el documento 21, confirmados → `OK G-28 … 25 documentos de gate contrastados … **sin una sola inversión**`. Contrasta contra `git show HEAD:`; un `commit` la silencia entera |
| **9** | `G-29` · unicidad | gemelos byte a byte + segundas sedes de marcador | **NO** | **R-A**: basta que la copia **no sea byte a byte** y viva en `docs/evolucion/`. **REF-2 (mía)**, en contra: un gemelo byte a byte ocultado con `.gitignore` **sí** se caza → `FALLO G-29`. La unicidad literal funciona; el perímetro no |
| **10** | `G-31` L2387-2440 | que ninguna comprobación se apague escribiendo una PALABRA | **SÍ en la letra, y es el problema** | La probé con sus diez palabras gatillo × cuatro evaluadores y **no cede**. Pero `G-31` **certifica que la ETIQUETA sí apaga** (exige que `_regiones_historicas` SÍ abra región): **protege el interruptor que P2b usa**. Se sustituyó un interruptor por otro y se puso una comprobación a garantizar que el nuevo funciona |
| **11** | `G-32` L2458-2517 | que todo nivel tenga PRODUCTOR en §9.1 y §9.2, «derivado de `O17`» | **NO** | **R-H:** `O17` sólo aparece en comentarios; ninguna línea de código lee su fila. Negué la resolución entera → **`37/37` verde**. La regla de la que dice derivar no se lee |
| **12** | `G-33` L2519-2600 · macrocircuitos | macrocircuitos DERIVADOS de §8 con FASE 0, contrastados contra `D107` | **PARCIAL** | La derivación de `_MACROS` de §8 **es real** (baseline: «4 macrocircuitos derivados de §8 (§8.1…§8.4)»). Pero **R-H**: borrar la fila `D107` **no deja hueco** en `G-20` —es la última de la serie— y apaga el contraste: cero coincidencias no falla. Verde por omisión, borrando la sede |
| **13** | `G-33` PN1 L2588-2600 | prueba negativa: macrocircuito sin Estructural | **SÍ, pero no discrimina** | Es la única de las cuatro que toca el corpus: `_b_real` sale del texto real del primer macrocircuito. Pero la mutilación borra **toda** línea con «FASE 0» o `gate:sistema-conforme`, y basta que **uno** de seis requisitos falte: es imposible que no falle |
| **14** | `G-33` PN2 L2602-2640 | prueba negativa: reutilizar con otra huella | **NO** | Evalúa `_reutilizacion` y `_declaracion_valida`, **definidas cinco líneas antes en la propia batería**, sobre diccionarios sintéticos construidos allí mismo. **R-H** lo cierra: negar `O17` entera la deja verde. Infalsificable por el corpus |
| **15** | `G-33` PN3 L2642-2670 | prueba negativa: elevarse sin Estructural vigente | **NO** | Idéntica estructura. Su única dependencia del árbol es que `_CADENA` no salga vacía; su CONTENIDO es indiferente |

### Y las protecciones que el documento 22 pidió y que SÍ se aplicaron, dicho a favor

Reejecuté los otros dos remedios que §13 del documento 22 prescribe y **los dos están hechos**:

- **«el fixture de `_derivar_vigiladas`: dejar de compararse consigo mismo»** — **HECHO, y bien.**
  La tautología desapareció; en su lugar hay **tres fixtures sintéticos que exigen resultados
  distintos entre sí** (ficha que declara · ficha que sólo lo menciona en prosa · ficha con otro
  sujeto) **más dos contrastes contra el árbol real** (`if not _VIGILADAS` y `_v not in _CAPS`).
  Es la única de las protecciones de fixture que tiene un pie fuera de sí misma.
- **«el lector estructurado: usar la sangría que ya registra»** — **HECHO.** `_campos` (L604-680)
  aplica hoy `ind_seccion` / `ind_item` y rechaza lo que cuelga por debajo, con el comentario que
  cita `Q-09` y reconoce que «*el código no lo aplicaba*». La docstring y el código coinciden.
- **`G-11b` falla cerrado sin `.git`**, **`G-20`** caza el hueco en la serie (**REF-3 mía**:
  borrar `D50` → `FALLO G-20`), y **`G-24` sí lee de verdad** (vaciar una fuente obligatoria la
  caza).

### La pregunta de fondo: ¿se curó el patrón, o se repitió?

```text
GENERALIZAN                    3 de 15    G-16 (3) · G-01 (4) · G-31 (10, en la letra)
PARCIALES                      3 de 15    G-22 inventario (1) · G-33 macrocircuitos (12) ·
                                          G-33 PN1 (13)
CIERRAN SÓLO SU PERÍMETRO      9 de 15    2 · 5 · 6 · 7 · 8 · 9 · 11 · 14 · 15
```

**Se repitió, y un nivel más arriba.** El documento 22 diagnosticó que «*cada corrección se
aplicaba al perímetro exacto de su contraejemplo y a ninguna otra parte*» y prescribió quince
remedios nombrados. **Trece de los quince remedios están literalmente ejecutados** —el inventario
se deriva, la marca es una etiqueta, el conjunto abarca tres zonas, la excepción tiene clase, la
huella se recalcula, la sangría se aplica, el fixture dejó de ser tautológico—. Y **nueve de las
quince siguen sin cerrar la clase**, porque **el remedio se escribió con la forma exacta del
contraejemplo que el documento 22 había construido**:

| el contraejemplo del doc 22 | el remedio aplicado | mi desplazamiento | resultado |
|---|---|---|---|
| `R-N1` · voltear docs 19/20/21 **sin confirmar** | ampliar el inventario a 19-22 y a los manifiestos | **añadir `git commit`** | `37/37` |
| `Q-04` · segunda sede en `docs/rediseno/` | comparar conjuntos en **tres zonas** | **un directorio adentro**, a `docs/evolucion/NN-*.md` | `37/37` |
| `Q-05` · validador vaciado **sin confirmar** | clase `CÓDIGO DE VALIDADOR` = idéntico a `HEAD` | **añadir `git commit`** | `37/37` |
| `Q-04`(bat) · la PALABRA «regresión» | exigir una ETIQUETA estructural | **escribir la etiqueta**, que apaga 39 líneas de una vez | `37/37` |
| `Q-03` · proyección segunda **dentro** del bloque | comparar cifras derivadas en la ventana de §19 | **una línea más abajo** del terminador literal | `37/37` |

**Esto es lo esencial que se me pidió responder, y ésta es mi respuesta:** la tanda **entendió**
el diagnóstico —lo cita, lo enumera, escribe quince protecciones y en tres casos las hace
generalizar de verdad— y **no lo curó**. Lo que cambió es la longitud del desplazamiento
necesario. Antes bastaba mover un directorio; ahora hace falta mover un directorio **y** hacer un
commit. La afirmación del documento 22 —«*una garantía mecánica que protege cuatro documentos de
siete y llama a eso «los documentos no se han tocado» es peor que no tenerla*»— **sigue siendo
verdadera** hoy: protege veintisiete documentos, diecinueve de ellos de verdad, ocho sólo contra
el editor que no confirma, **y llama a eso «intactos frente a `HEAD` y a `05f71b7`»**.

### La raíz común, que no es quince cosas sino una

`R-C`, `R-D`, `R-E` y la fila 8 son **el mismo defecto**: **toda afirmación de «intacto» de esta
batería está anclada en referencias que viven dentro del árbol que se audita** — `HEAD`,
`05f71b7`, `kernel/.upstream-hash`, el README de `verificacion/`. Quien puede escribir el árbol
puede escribir la referencia. La batería detecta **incoherencias internas**, no **mutilaciones**.
Mientras no exista un ancla fuera del árbol —huellas publicadas en el manifiesto del gate, o una
revisión base que sea anterior a **cada** inmutable— ninguna corrección local cerrará esta clase,
y el gate siguiente escribirá otras quince protecciones con el mismo resultado.

---
## 5 · LAS PRUEBAS NEGATIVAS — ¿falsificables por el árbol, o tautologías?

**Primero, un hecho aritmético que la propia batería imprime.** El título del `check` dice «*las
**tres** pruebas negativas —omitir Estructural, reutilizar con otra huella, elevarse sin
Estructural vigente— dan ROJO*», el README L81 dice **tres**, y el detalle que la misma línea
imprime dice:

```
└─ … · 4 pruebas negativas ejecutadas, todas en rojo como deben
```

`_NEGATIVAS` (L2593) acumula **CUATRO** entradas. Es un censo que la batería **escribe, imprime y
no contrasta contra ninguna sede** — al revés que `_FIXTURES` en `G-15`, que sí se contrasta
contra el documento 11. En la comprobación que existe para probar que los censos no se escriben
a mano. Va como `T-09`.

| | qué evalúa | ¿puede ponerla ROJA algún estado del ÁRBOL? | mi prueba |
|---|---|---|---|
| **PN1** · omitir la FASE 0 Estructural | `_fase0_conforme(_b_mutilado)`, donde `_b_real` **sale del texto real del primer macrocircuito** vía `sec_de(i)` sobre `L11` | **SÍ**, y es la única | Es la única de las cuatro con un pie en el corpus. Pero la mutilación borra *toda* línea con «FASE 0» o `gate:sistema-conforme` y basta que **uno** de seis requisitos falte: **no puede no fallar**. Es un control positivo válido y un discriminante nulo |
| **PN2** · reutilizar con otra huella | `_reutilizacion(_sujeto_a, _sujeto_b, …)`, función **definida en L2607** —cinco líneas antes— sobre diccionarios sintéticos construidos allí mismo | **NO** | **R-H:** sustituí la fila `| O17 |` del registro por su **negación exacta** y borré `D107` → **`37/37` verde**. La regla que PN2 dice implementar puede anularse entera sin que PN2 se entere |
| **PN3** · elevarse sin Estructural vigente | `_nivel_alcanzado(...)` sobre `_todo_ok` / `_sin_estructural` / `_solo_superiores`, los tres construidos en la batería | **NO** | Igual que PN2. Su única dependencia del árbol es que `_CADENA` no salga vacía; su **contenido** es indiferente |
| **PN4** · (la que el título no cuenta) | `_declaracion_valida(...)`, misma estructura | **NO** | Igual |

### Veredicto de §5

**PN2, PN3 y PN4 no son tautologías LITERALES** —se pueden romper, y `T1` lo demostró debilitando
`difieren = []` dentro del fichero, con `FALLO G-33`—. **Son algo peor para lo que se les pide:
son INFALSIFICABLES POR EL CORPUS.** Son autotests de tres funciones que la batería escribe,
evaluadas sobre datos que la batería inventa, y su resultado es independiente de todo estado del
árbol auditado. La única mano capaz de ponerlas en rojo es la misma que las escribió.

**Y el defecto no es que existan —un autotest de contrato es legítimo— sino que se declaren como
lo que no son.** El título del `check` afirma que las pruebas «dan ROJO» como si el sujeto fuera
el corpus, y el comentario de L2519-2522 afirma que «*las reglas se derivan de `O17` en el
registro*», lo cual es **falso**: `grep -n 'O17'` sobre la batería devuelve cinco líneas y las
cinco son comentario o cadena de diagnóstico. **El README L98-101 es más honesto que el código**
—«fixtures sintéticos: que el evaluador sepa decir que no»— y esa honestidad consta a favor.

**Comparación que hago expresamente, porque separa lo bueno de lo malo en la misma tanda.** El
fixture de `_derivar_vigiladas` (§4) hace lo correcto: tres fixtures sintéticos **más** dos
contrastes contra el árbol real (`if not _VIGILADAS`, `_v not in _CAPS`). Las tres pruebas
negativas de `G-33` no tienen ese segundo pie. **La tanda sabía cómo hacerlo bien: lo hizo en una
comprobación y no en la otra.**

---
## 6 · HALLAZGOS DE `T`, CONSOLIDADOS

**Severidad ADJUDICADA POR MÍ**, con el criterio que declaro y que es **el mismo que el
adjudicador `R` aplicó a los 69 del documento 22**, para que `U` pueda comparar sin traducir:

```text
BLOQUEANTE  obliga a DECIDIR ARQUITECTURA NUEVA
GRAVE       una garantía publicada NO se sostiene, o `F6` construiría algo distinto
MEDIO       una afirmación vigente es falsa sin cambiar el comportamiento
MENOR       editorial o de propagación
```

**Y digo por delante lo que esto cuesta a mi propia cadena.** `T1` graduó cinco hallazgos
BLOQUEANTES con un criterio distinto —«el corpus puede alterarse en silencio y la batería da
verde»—. **Con el criterio de `R`, ninguno de los míos es BLOQUEANTE**: los quince se cierran con
material que el corpus ya tiene escrito y ninguno obliga a elegir entre alternativas que una
decisión vigente no resuelva. **Los bajo todos a GRAVE, y lo hago constar como rebaja.** Que la
etiqueta baje **no cambia mi recomendación**: `R` emitió `INSUFICIENTE PARA F5` con cero
BLOQUEANTES y ocho GRAVES, sobre evidencia estrictamente más débil que la que traigo.

| id | sev | fichero y línea | cita | por qué | quién lo levantó | ¿lo reproduje? |
|---|---|---|---|---|---|---|
| **`T-01`** | **GRAVE** | `comprobar-correccion-gate-de-cierre.py` **L2264-2385** (`G-30`) | «`CÓDIGO DE VALIDADOR   idéntico a lo publicado en `HEAD`»` (L2279) y `_huella_pub = leer(os.path.join(RAIZ, "kernel/.upstream-hash"))` (L2371) | La clase de contenido se ancla en `HEAD` y la huella en un fichero **del propio árbol**. Las dos referencias las escribe quien edita. Es el contraejemplo de la protección 6 —que la propia batería transcribe en su comentario L2269-2271— readmitido añadiendo `git commit` | `T1` (`T1-02`) | **SÍ · R-D.** Validador a `import sys; sys.exit(0)`, tres evidencias falsificadas, huella reanclada con el valor que la batería publica al fallar, `git commit` → **`37/37` verde**, porcelain vacío |
| **`T-02`** | **GRAVE** | **L1520-1531** (`G-22`) y **L2091-2116** (`G-28`) | `if rel in _base_arbol and rel in tocados:` | **Ocho de los veintisiete inmutables no existen en `05f71b7`** —docs 19, 20, 21, 22 y los cuatro manifiestos, derivados por mí— luego su segundo brazo es inalcanzable, en silencio. `G-28` contrasta sólo contra `git show HEAD:`. Es `Q-26`/`R-N1` con el inventario ampliado y **la comparación sin tocar** | `T1` (`T1-01`) | **SÍ · R-C.** 15 volteos `INSUFICIENTE`→`SUFICIENTE` en el doc 21 + un manifiesto, confirmados → **`37/37` verde**, con `OK G-22 … intactos` y `OK G-28 … sin una sola inversión` |
| **`T-03`** | **GRAVE** | **L2183-2196** (`_ampliacion_admitida`) | `if re.match(r"^docs/evolucion/\d\d-.*\.md$", rel): return True   # el documento que un gate nuevo publica` | Todo fichero `NN-*.md` bajo `docs/evolucion/`, rastreado o no, se admite **sin mirar su contenido**. La comparación de conjuntos se extendió de 1 a 3 zonas y se abrió un `return True` en blanco dentro de la zona nueva | `T1` (`T1-03`) | **SÍ · R-A.** `23-SEGUNDA-SEDE-NORMATIVA.md` («CONTRADICE `C4` y `C7` y PREVALECE» + copia del material APROBADO) y `24-REGISTRO-ALTERNATIVO.md` (registro con `D87` alterada) → **`37/37` verde**, y `G-22` y `G-29` **los nombran en su detalle mientras imprimen `OK`** |
| **`T-04`** | **GRAVE** | **L2172-2181** (`G-29`) | `_INSTRUMENTAL = set(re.findall(r"`(docs/evolucion/verificacion/[A-Za-z0-9_.-]+)`", _t_readme))` | La sede que autoriza las ampliaciones de `verificacion/` es el README, y **el README no está en ningún inventario de integridad**: no es inmutable, no está en `_EN_CORRECCION`, su contenido no se contrasta. Autorización circular: el guardado escribe su propia autorización | `T1` (`T1-04`) | **SÍ · R-B.** Añadí `` `…/bateria-2.py` `` al README, planté esa segunda batería (imprime «37/37 en verde», `exit 0`) y **renombré `G-30` a `G-30-ANULADA` en toda la tabla** → **`37/37` verde** |
| **`T-05`** | **GRAVE** | **L1521-1523** y **L2099-2100** | `if rel not in _head_arbol: _sin_base.append(rel); continue` | `G-22` y `G-28` llevan «**falla CERRADO sin git**» en su título y **no fallan cerrado ante una salida VACÍA CON ÉXITO**: `_git()` sólo devuelve `None` si el comando falla. Con `_head_arbol` vacío los dos bucles se saltan entero su cuerpo y las dos imprimen `OK`. Es `M-12` —«*interpretaban el vacío como «nada cambió»*»— sobreviviendo en las dos comprobaciones escritas para cerrar esa clase; `G-11b` **sí** tiene la guarda | `T1` (`T1-19`) | **SÍ · R-E.** `git` falso en el `PATH` (`exit 0`, sin stdout) → **31/37**; fallan `G-11`, `G-11b`, `G-21`, `G-23`, `G-29`, `G-30`; **`G-22` y `G-28` en `OK`**, con `G-28` verde sobre **cero** documentos |
| **`T-06`** | **GRAVE** | **L1784-1845** (`_regiones_historicas`) | `_CIERRA_REGION = re.compile(r"^#{1,6} ")` | La protección 2 sustituyó un interruptor de PALABRA por uno de ETIQUETA, y la región que la etiqueta abre sólo cierra en un encabezado en **columna 0** — que dentro de una cita `>` nunca llega. Una línea exime un bloque entero de todo control de cifra. Y **`G-31` certifica que el interruptor funciona** | `T1` (`T1-05`) | **SÍ · P2a/P2b.** Cifra viva falsa en doc 11 L1541 → `FALLO G-26`, 36/37. La misma cifra con **una línea** `> **[ESTADO ANTERIOR · …]**` encima → **`37/37` verde** |
| **`T-07`** | **GRAVE** | **L779-780** (`G-15`) | `b19 = t11[i19:t11.index("**Y dos más, que no son defectos de F4", i19)]` | La «unicidad de proyección por tres caminos» que el README L63 promete se evalúa **sobre una ventana delimitada por dos cadenas literales**. El remedio del doc 22 —«comparar cifras derivadas, no un patrón de un carácter»— se aplicó **dentro** de la ventana y la ventana no se tocó | `T1` (`T1-06`) | **SÍ.** Control: la segunda proyección «SEIS procesos y en total DIEZ pares, y es la vigente» **dentro** del bloque → `FALLO G-15`, 36/37. Ataque: la MISMA frase **una línea después** de L10130 → **`37/37` verde** |
| **`T-08`** | **GRAVE** | **L2458-2670** (`G-32`, `G-33`) contra `DECISIONES-Y-CONTRADICCIONES.md` **L674** | «*Protecciones 12, 13, 14 y 15, todas derivadas de `O17` y de su propagación `D107`*» (L2519) | **Ninguna línea de código lee la fila `| O17 |`**: `grep -n 'O17'` da cinco golpes y los cinco son comentario o diagnóstico. `G-21` protege `O1`-`O16` y se detiene justo antes. La resolución del Owner que **este gate existe para certificar** puede negarse entera sin que nada se mueva | `T1` (`T1-08`) | **SÍ · R-H.** Fila `O17` sustituida por su negación exacta + fila `D107` borrada → **`37/37` verde**. Borrar `D107` no deja hueco en `G-20` (es la última) y apaga el contraste de `G-33`: verde por omisión |
| **`T-09`** | **GRAVE** | **L2593-2683** (`G-33`) | título: «*las **tres** pruebas negativas … dan ROJO*» · detalle impreso: «*4 pruebas negativas ejecutadas*» | Tres de las cuatro (PN2, PN3, PN4) son **infalsificables por cualquier estado del corpus**: evalúan funciones definidas cinco líneas antes sobre diccionarios construidos allí mismo. Y el censo «tres/cuatro» **se escribe, se imprime y no se contrasta contra ninguna sede**, en la batería cuya tesis es que los censos no se escriben a mano | `T1` (`T1-09`, `T1-15`) | **SÍ.** El desajuste 3/4 sale en la salida del baseline. La infalsificabilidad la cierra `R-H`: `O17` negada entera → verde |
| **`T-10`** | **GRAVE** | `F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` **§2** y **§6** | «`UNIVERSO DERIVADO   64 fuentes · 47 728 líneas`» y «`LÍNEAS OBLIGATORIAS  47 728`» | **HALLAZGO MÍO.** El derivador que el propio manifiesto publica como comando auditable da **48 138** sobre los tres árboles en juego (`e3163967`, `6b5d3e6`, `c36d2ba` — lo ejecuté sobre los tres), y **los dos subtotales del propio manifiesto, 21 530 + 26 608, suman 48 138**, contradiciendo su titular. La diferencia es **exactamente 410 líneas = el recuento de `derivar-universo-obligatorio.py`**, el fichero que ese mismo §2 presenta como «*el propio derivador, que pasa a juzgarse a sí mismo*» y que su §4 fila 8 lista con 410 líneas. **La cifra del titular es una copia previa a la ampliación, no una derivación**, en el bloque que publica «las DOS restas de `1bis`» y en el documento cuya tesis es «*el universo no se escribe: se deriva*» | **yo** | **SÍ.** `python3 …/derivar-universo-obligatorio.py` → `64 fuentes · 48138 líneas`; parseo de §4+§5 → 12 filas/21 530 + 52 filas/26 608 = 64 filas/48 138; `48138 − 47728 = 410` = `wc -l` del derivador |
| **`T-11`** | **MEDIO** | el reparto de este gate | encargo de `T2`: recalcular la regla 1 del agotamiento **y** no abrir los documentos 19, 20 y 21 | **HALLAZGO MÍO.** La regla 1 vive en el documento 21. Se le pidió a un relevo una verificación sin darle la fuente, y se resolvió con extracción quirúrgica declarada. **Es la misma clase que el `C-2` que `R` reprochó al coordinador anterior** —«*se le pidió a un revisor un foco sin darle la fuente*»— repetida en este gate. La conducta de `T2` fue correcta; el reparto no | **yo** | **N/A** (defecto de procedimiento, no de árbol) |
| **`T-12`** | **MEDIO** | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **L10193** contra `CORRIGENDUM-DICTAMENES-INMUTABLES.md` **L74-89** | «*el BLOQUE C (§13–§15, iniciativa y dosier vivo)*» | El corrigendum acota el documento 19 por definir el BLOQUE C como §13–§15, y **el mismo error está vivo en la sede normativa que sí se edita** — el bloque «QUÉ HAY QUE LEER ÍNTEGRO» de `C-L.5`, que es literalmente el texto que `componente_i` del derivador parsea. La regla §6 del corrigendum **no distingue dictamen inmutable de norma viva**, y aquí ya ha servido para acotar en vez de corregir | `T2` (`T2-05`) | **SÍ · R-G.** `# BLOQUE C` L1019, `# BLOQUE D` L1137, y `awk '/^## /'` entre ambos da **§13 §14 §15 §16 §17 — cinco secciones** |
| **`T-13`** | **MEDIO** | `kernel/operativo/validadores/comprobar_negativos.py` **L687-698** y **L47-49** | «*`espera` … Sin él, una mutación se da por detectada porque la prueba falló, sin comprobar que falló POR ESO*» | Con `T147` en rojo en `HEAD`, las cuatro mutaciones `N147`, `N147b`, `N147c` y `N147d` —ninguna con `espera`— pasan **con o sin su mutación**. Es `M-04` **instanciado en el árbol real, sin mutar nada**. Y lo AMPLÍO: `grep -c 'Mutacion('` → **63**, `grep -c 'espera='` → **10**: **53 mutaciones carecen del campo**, y cualquiera cuya prueba caiga en rojo por otra causa será igual de vacua | `T2` (`T2-08`) | **SÍ · R-F.** `T147 FALLIDA · 0 superadas · 1 fallidas · EXIT=1` en `c36d2ba` limpio; con la mutación de `N147` convertida en `return  # NO-OP`: `OK N147 … 67 infracciones detectadas · 0 NO detectadas · EXIT=0` |
| **`T-14`** | **MEDIO** | `docs/evolucion/00-INDICE.md` **L100-108** contra **L110-117** | «*Quien publique un manifiesto sin enlazarlo aquí **deja el árbol que juzga con un validador canónico en rojo, causado por el aparato del propio gate**.*» | El commit `c36d2ba` —que es `HEAD`— publica el manifiesto de ESTE gate **sin enlazarlo desde la lista**, y el comando que el propio índice publica lo detecta. La regla se escribe y se incumple en el commit siguiente. **La regla funciona; lo que falló es cumplirla** | `T2` (`T2-07`) | **SÍ.** `find … | sort` → 8 rutas; la tabla enlaza 7; la que falta es `F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md`, y es exactamente la que `T147` denuncia |
| **`T-15`** | **MEDIO** | `derivar-universo-obligatorio.py` **L50** contra **L241-265** y **L271-346** | «*Nunca adivina y **nunca reduce el universo en silencio**: un universo que encoge sin decirlo es exactamente el defecto que `P-08` describió.*» | La promesa cubre la MANIPULACIÓN y no la OMISIÓN. Borrar una fila de `ENCARGO` reduce el universo en uno con `exit 0` y sin aviso; y `VOCES_DE_DICTAMEN` **es una lista escrita a mano** que no incluye `DICTAMEN`, `AUDITORÍA` ni `CERTIFICACIÓN`, de modo que un dictamen nuevo titulado «DICTAMEN» **no entra en el universo** — que es palabra por palabra lo que `1bis` dice que hay que impedir | `T2` (`T2-01`, `T2-02`) | **PARCIAL.** Confirmé por lectura de código y por la consecuencia estructural: **el manifiesto de ESTE gate no está en las 64 rutas del universo** (sólo los tres manifiestos anteriores). Es la misma autoexclusión que `T2-13` documentó del derivador en el gate 1, un piso más arriba |
| **`T-16`** | **MEDIO** | `comprobar-correccion-gate-de-cierre.py` **L1716-1718** contra **L532/L549** | `_dir_cap = os.path.join(RAIZ, "kernel/operativo/capacidades")` | `Q-27` prometía derivar el catálogo de capacidades «una sola vez» y compartirlo entre `G-15` y `G-24`; `G-24` **no usa** `_CAPS_DIRS` y recomputa. Dos sedes de la misma derivación, dentro de la batería que persigue las segundas sedes, y el README L72 lo afirma corregido | `T1` (`T1-11`) | **SÍ** (lectura de código: L532, L549, L1716) |
| **`T-17`** | **MENOR** | **L374** | `sedes = {"§8.0": None, "§8.1": None, "§8.2": None, "§8.4": None, "§18": None}` | Código **muerto**: se asigna y no lo lee nadie. Además **omite `§8.3`** mientras el título del `check` dice «las SEIS sedes de §8 y §18». Es la clase `M-11`/`Q-15`/`Q-22` que esta tanda declara purgada | `T1` (`T1-12`) | **SÍ** (`grep -n '\bsedes\b'` → sólo L374 y usos ajenos) |
| **`T-18`** | **MENOR** | **L53-59** y **L75** | `if not fh.read().strip(): return "vacío"` | Guarda **muerta**: `_motivo_ilegible` sólo se invoca desde el `except (OSError, UnicodeDecodeError)` de `leer()` (L75), y leer un fichero vacío no lanza ninguna de las dos. La rama es inalcanzable | `T1` (`T1-13`) | **SÍ.** Vacié `DECISIONES-Y-CONTRADICCIONES.md` → **`OK G-00`**, 33/37 (lo cazan otras cuatro) |
| **`T-19`** | **MENOR** | **L53** y **L1696** | `def _motivo_ilegible(ruta)` / `def _ilegible(ruta)` | La misma función escrita dos veces, y **divergen**. Segunda sede dentro de la batería | `T1` (`T1-14`) | **SÍ** (lectura) |
| **`T-20`** | **MENOR** | el fichero de la batería, completo | — | La batería **no está en ningún inventario de integridad**: ni `_INMUTABLES`, ni `_EN_CORRECCION`, ni ninguna clase de `G-30`. Y el README L16-17 declara como virtud que «*el número de comprobaciones no se escribe en ningún sitio*», que es justo lo que impide notar una amputación: borrar un `check` imprime `36/36 en verde` | `T1` (`T1-16`) | **NO reproducido por mí**: acepto la lectura de código de `T1`, que verifiqué (el fichero no aparece en `_INMUTABLES` ni en `_CLASES`), y **no ejecuté** la amputación. Lo declaro |
| **`T-21`** | **MENOR** | `CORRIGENDUM` **L93-94** | «*Sede: `13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md` **L42** y **L618***» | Las líneas reales son **L46** y **L628**, en un documento cuya cabecera promete «*Toda cifra … se DERIVA … Ninguna se copia*». La sustancia es correcta; la localización no | `T2` (`T2-06`) | **NO reproducido por mí** (fuera de mi lote de lectura). Lo transcribo con su atribución |
| **`T-22`** | **MENOR** | `derivar-universo-obligatorio.py` **L156-157** | `raise SedeIlegible("… %r" % (mi.group(1), mii.group(1), mii.group(2)))` | Un `%r` con una tupla de tres es `TypeError`. **La única rama del derivador que no falla cerrado es la que existe para fallar cerrado**: revienta con traza y código **1**, no 2, y sin la línea `FALLA CERRADO ·` que el manifiesto enseña a buscar | `T2` (`T2-03`) | **NO reproducido por mí**; verificado por lectura de la línea. `T2` pegó la traza |

```text
RECUENTO DERIVADO DE LAS FILAS, no copiado

  BLOQUEANTE    0
  GRAVE        10   T-01 … T-10
  MEDIO         6   T-11 … T-16
  MENOR         6   T-17 … T-22
               ──
               22

DE ELLOS, REPRODUCIDOS POR MÍ CON SALIDA PEGADA   17
ACEPTADOS DE UN RELEVO SIN REPRODUCIR, DECLARADOS  4   T-20 · T-21 · T-22 · (T-15 parcial)
HALLAZGOS MÍOS, QUE NINGÚN RELEVO TRAJO            2   T-10 (GRAVE) · T-11 (MEDIO)
```

---
## 7 · HALLAZGOS QUE RECHAZO DE MIS PROPIOS RELEVOS

**Cuatro rechazos y cinco rebajas. Vale tanto como lo que acepto, y va contra mi propia cadena.**

**`X-1` · RECHAZO la mitad sustantiva de `T1-05`: las dos «cifras falsas VIVAS» NO están vivas.**
`T1` afirma que «*dos cifras falsas VIVAS quedan hoy tapadas*»: `CHECKPOINT-ADS-NEXT.md` **L166**
y **L2739**, que dicen «CATORCE presiones» donde el árbol deriva DIECISÉIS. **Verifiqué las dos
cosas y la primera mitad es cierta y la segunda no.** La derivación:

```text
grep -c '^## `PN-' doc 11                                    → 18
grep '^## `PN-' doc 11 | grep -vc 'RETIRADA\|FUSIONADA'      → 16   ← la cifra vigente
```

**Pero las dos líneas están dentro de regiones EXPLÍCITAMENTE ROTULADAS como históricas**, y las
localicé:

```text
L123   > **[ESTADO ANTERIOR · antes del GATE DE CERTIFICACIÓN, documento 22]**      →  cubre L166
L2685  > **[HISTÓRICO · «Siguiente acción exacta» anterior al GATE DE CERTIFICACIÓN,
          documento 22 …]**                                                          →  cubre L2739
```

Una cifra correcta **para el estado que la etiqueta declara** no es una cifra falsa viva: es
historia marcada, que es exactamente lo que la disciplina del corpus prescribe. El propio `T1`
escribe «*puede ser legítimo — pero es imposible saberlo sin leerlo*»; **yo lo he leído y es
legítimo**. **Lo que SÍ sobrevive entero de `T1-05` es el defecto ESTRUCTURAL** —una línea abre
una región que no cierra hasta un encabezado en columna 0, que dentro de una cita `>` no llega— y
eso es lo que reproduje en P2b y lo que adjudico como `T-06`. **La consecuencia alarmista no
entra; el mecanismo sí.**

**`X-2` · RECHAZO una cita de `T1-01`: el tercer `sed` fue un NO-OP.** `T1` publica como parte de
su reproducción `sed -i 's/NO SUPERADO/SUPERADO/g'` sobre el documento **20**. Lo comprobé:

```text
grep -c 'NO SUPERADO' docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md  → 0
```

**El documento 20 no se modificó.** El experimento se sostiene entero con los otros dos volteos
—15 ocurrencias en el doc 21 y 1 en un manifiesto, que sí reproduje— pero **la cita es inexacta**,
y `T1` la publicó como hecho porque ejecutó `sed -i` a ciegas sin comprobar el recuento previo. Lo
corrijo en `T-02` y lo digo aquí: **un hallazgo cuya reproducción incluye un paso que no hizo
nada obliga a que el siguiente lo rehaga entero**, y por eso lo rehíce.

**`X-3` · RECHAZO la severidad BLOQUEANTE de los cinco de `T1`.** Con el criterio de `R` —el
único que permite comparar mis 22 con los 69 del documento 22— **BLOQUEANTE significa «obliga a
decidir arquitectura nueva»**, y ninguno lo hace: `T-01` se cierra publicando la huella fuera del
árbol; `T-02` eligiendo una revisión base anterior a cada inmutable, o contrastando contra el SHA
que el manifiesto publica; `T-03` mirando el contenido en vez de devolver `True`; `T-04` metiendo
el README en `_INMUTABLES`; `T-05` con la guarda de «base vacía» que `G-11b` ya tiene escrita
cinco pantallas más arriba. **Los cinco se cierran con material que el corpus ya tiene.** Los
adjudico GRAVES. **Y digo lo que esto NO cambia:** mi recomendación es la misma con GRAVE que con
BLOQUEANTE, y `R` emitió `INSUFICIENTE PARA F5` con cero BLOQUEANTES.

**`X-4` · RECHAZO la formulación de `T1-10` sobre `G-28`** —«no aporta cobertura: cero»—. Es
demasiado fuerte. `G-28` **sí** aporta una cosa que `G-22` no da: contrasta el **veredicto,
polaridad y estado** por familias derivadas, no la identidad byte a byte, de modo que caza una
inversión semántica dentro de un documento que `G-22` ya autorizara. Lo que es cierto —y es lo
que adjudico dentro de `T-02`— es que **comparte con `G-22` el mismo ancla (`HEAD`) y por tanto
el mismo talón**, no que sea redundante. **Fusiono `T1-10` dentro de `T-02` en vez de contarlo
aparte**, y con ello mi censo baja en uno respecto del de `T1`.

**`X-5` · REBAJO `T1-16` (la batería no está en ningún inventario) de MEDIO a MENOR, y declaro
que NO lo reproduje.** `T1` publica `36/36 comprobaciones en verde` tras amputar el bloque
`check("G-29", …)`. **Yo no ejecuté esa amputación.** Verifiqué la premisa —el fichero no aparece
en `_INMUTABLES` ni en `_CLASES`— y acepto la consecuencia por lectura, no por ejecución. Un
hallazgo que el dictaminador no reprodujo no puede llevar la misma etiqueta que uno que sí. Es
`T-20`, MENOR, y con la reserva escrita en su fila.

**`X-6` · REBAJO `T2-01` y `T2-02` de GRAVE a MEDIO** (van fusionados en `T-15`). El derivador
**resiste diez de los catorce ataques de `T2` con código 2 y diagnóstico nombrado** —sede
ilegible, cardinal descuadrado, catálogo con repetida, ruta inexistente, fila sin cláusula,
nombre ambiguo—, y su carácter anotado en el componente (v) **está declarado honestamente** en
L40-44 y en el §2 del manifiesto. Lo que falla es **una promesa de L50 más ancha que el
programa**, no el programa. Con el criterio de `R` eso es «una afirmación vigente es falsa sin
cambiar el comportamiento»: **MEDIO**.

**`X-7` · REBAJO `T2-05` de GRAVE a MEDIO** (`T-12`). El hecho es exacto y lo reproduje. Pero el
rango `§13–§15` en el bloque de `C-L.5` **no ha causado daño en este gate**: el universo
obligatorio se deriva del bloque «QUÉ HAY QUE LEER ÍNTEGRO», y el componente (i) devuelve las
cuatro rutas correctas, `ADS-PENDIENTES` **entera** incluida — no por secciones. El daño que la
entrada 3 del corrigendum describe —«dos secciones enteras sin leer»— **es potencial, para quien
lea el rango en vez de la ruta**, no actual. MEDIO, y con el remedio de tres caracteres.

**`X-8` · REBAJO `T2-07` de GRAVE a MEDIO** (`T-14`), y lo digo a favor del corpus. La regla de
`00-INDICE` L100-108 **funciona**: la escribieron, publicaron el comando, el comando la comprueba
y **la denuncia**. Lo que falló es cumplirla en el commit siguiente. Un incumplimiento que la
propia norma detecta y nombra, con remedio de una línea en una tabla, no es una garantía
publicada que no se sostiene: es una tarea pendiente. **MEDIO.**

**`X-9` · NO ADJUDICO `T2-09`, `T2-10`, `T2-11`, `T2-12` ni `T2-13`.** Son observaciones sobre
los manifiestos y el derivador que **no reverifiqué** —la severidad de la entrada 2 del
corrigendum, la frase «lo único escrito a mano», la no-fijación de versión del bloque `bash`, la
conflación commit/árbol de `02ba78c5`, y la autoexclusión del derivador en el gate 1—. `T2` las
trae con su comando, y me parecen verosímiles; **no las cuento entre mis veintidós**. Prefiero un
censo corto y entero a uno largo y prestado. *(De `T2-13` sí tomo la consecuencia estructural, que
sí verifiqué y que va dentro de `T-15`: el manifiesto de ESTE gate tampoco está en el universo.)*

**Y una cosa que NO rechazo y que quiero que conste, porque `T2` la trae contra su propio
interés.** `T2` intentó cinco refutaciones contra el aparato de cobertura y **las cinco le
fallaron**: las restas del manifiesto anterior cuadran al dígito (80 filas recalculadas, 0
discrepancias), el universo se deriva de verdad, las doce agotadas se sostienen ruta a ruta, el
addendum **promete de menos** que lo que su propia evidencia sostiene, y el corrigendum **acota
sin editar** —los documentos 20 y 21 y los cuatro manifiestos tienen **un solo commit cada uno en
toda su historia**—. Reejecuté el derivador sobre tres árboles y confirmo su §7.2 y §7.3. **`P-08`
está cerrado, y lo digo yo, que vengo a romper.**

---
## 8 · LOS HALLAZGOS DEL DOCUMENTO 22 EN EL FOCO DE `T`

**Regla que me impongo.** Los del foco de `S` —protocolo transaccional, `D105`, las ventanas
`W`, `fsync`, `KERNEL.md`, los contratos, `(a)`, `(b)`, `D97`, `PN-15`/`PN-16`, el nivel
Estructural como decisión— **NO los adjudico y no los presumo ni cerrados ni abiertos**. No he
leído esas fuentes, y sustituir una lectura ausente por una inferencia es el defecto que este
expediente lleva cinco gates persiguiendo.

De los **69 hallazgos** del documento 22 —0 BLOQUEANTES · 8 GRAVES · 34 MEDIOS · 27 MENORES; 68
de clase A y 1 de clase B— el foco de `T` alcanza los que tocan la batería, el derivador, los
manifiestos, el corrigendum y `M-04`. Ésos son los que adjudico.

| id (doc 22) | qué exigía | qué encuentro yo | resultado |
|---|---|---|---|
| **GRAVE 5** · `Q-01` · **`M-04` FALLIDA**, ocho árboles en verde | la proposición: que no exista árbol defectuoso que pase en verde | **Siete árboles nuevos en `37/37` VERDE**, construidos y ejecutados por mí (R-A, R-B, R-C, R-D, R-H, P2b, G-15b), más el verde-sobre-cero de R-E y **una instancia viva en `HEAD` sin mutar nada** (R-F) | **NO CERRADO** |
| **GRAVE 6** · `Q-02` · el perímetro: segunda sede fuera de `kernel/` | «*la comparación de CONJUNTOS: extenderla de `kernel/` a todo material normativo*» | Extendida a **tres zonas** (`kernel`, `docs/rediseno`, `docs/evolucion`) — y con un `return True` en blanco para `docs/evolucion/NN-*.md` dentro de la zona nueva. **R-A** entra por ahí. Y `docs/owner/`, la raíz, `packs/` y `tooling/` siguen fuera de `_ZONAS` | **NO CERRADO** |
| **GRAVE 7** · `Q-04` · `G-26` se apaga con la palabra «regresión» | «*`_BLOQUE_HISTORICO`: evaluar sobre la OCURRENCIA, no sobre la línea entera*» | **La palabra ya no apaga nada** —`G-31` lo prueba con diez palabras gatillo × cuatro evaluadores y no cede—. **Pero la ETIQUETA sí**, y apaga un bloque entero: **P2b**, `37/37`. Se sustituyó el interruptor y `G-31` certifica que el nuevo funciona | **NO CERRADO** (defecto trasladado) |
| **GRAVE 8** · `R-N1` · `G-22` sólo fija `1[5-8]`; volteé 19/20/21 y el manifiesto inmutable | «*`G-22`: extender el rango inmutable a los documentos 19, 20 y 21, y a los manifiestos*» | **El inventario se derivó y se amplió a 27**, y la forma exacta de `R-N1` —edición **sin confirmar**— **hoy se caza**: `REF-1` → `FALLO G-22`, 36/37. **Pero ocho de los 27 no tienen línea base**, y con `git commit` los mismos volteos dan `37/37` (**R-C**) | **CERRADO EN SU FORMA · NO CERRADO EN SU CLASE** |
| `Q-03` doc 21 ≡ `Q-05` doc 22 · la excepción del kernel por RUTA | «*la excepción del kernel: fijar CONTENIDO, no sólo ruta —empezando por `.upstream-hash`*» | **Hecho**: hay cuatro CLASES declaradas, la huella se **recalcula** y ya no se cree la del árbol, y el ataque **sin confirmar** se caza. **Pero la clase es «idéntico a `HEAD`» y la huella se compara contra `kernel/.upstream-hash`, dentro del árbol**: **R-D**, `37/37` | **NO CERRADO** |
| `Q-06` doc 22 · `G-16` por PREFIJO | «*`G-16`: contrastar por igualdad de estado, no por prefijo*» | **HECHO Y GENERALIZA.** Mi ataque → `FALLO G-16`, con el diagnóstico que nombra el mecanismo | **CERRADO** |
| `Q-07` doc 22 · `G-01` con la palabra «RETIRADA» | «*`G-01`: exigir polaridad, no la mera presencia*» | **HECHO Y GENERALIZA.** El párrafo que **deroga** la retirada → `FALLO G-01` | **CERRADO** |
| `Q-03` doc 22 · la unicidad de proyección por un patrón de un carácter | «*la unicidad de proyección: comparar cifras derivadas, no un patrón de un carácter*» | **Hecho dentro de la ventana** —mi control cae, `FALLO G-15`—. **La ventana no se tocó**: `t11.index("**Y dos más…")`. Una línea más abajo, `37/37` | **CERRADO EN SU FORMA · NO CERRADO EN SU CLASE** |
| `Q-09` doc 22 · el lector estructurado y la indentación | «*el lector estructurado: usar la sangría que ya registra*» | **HECHO.** `_campos` L604-680 aplica `ind_seccion`/`ind_item` y rechaza lo colgado, con el comentario que reconoce el defecto anterior | **CERRADO** |
| `Q-10` doc 22 · el fixture tautológico de `_derivar_vigiladas` | «*el fixture … dejar de compararse consigo mismo*» | **HECHO, Y ES LA MEJOR PIEZA DE LA TANDA.** Tres fixtures sintéticos con resultados distintos **más dos contrastes contra el árbol real** | **CERRADO** |
| `R-N2` / `R-N3` · el derivador encoge en silencio; falta guarda de unicidad | «*el derivador: `len(set(fuentes)) != 14`, guarda para (iii) y (v), y leer los cardinales de su sede*» | **La unicidad SÍ se añadió** (`T2` A10 → `FALLA CERRADO · G-24 enumera 14 fuentes pero sólo 13 DISTINTAS`), y (i) y (ii) fallan cerrado bajo diez ataques distintos. **(iii) sigue devolviendo constantes y (v) sigue encogiendo en silencio por omisión** | **PARCIALMENTE CERRADO** |
| `Q-08` doc 22 · `exclusiones.yaml` y `T147` roto por el manifiesto de cada gate | «*que los manifiestos que `1bis` obliga a publicar no rompan `T147`, y que no rompan uno más cada gate*» | **NO se aplicó ninguna de las dos vías.** `00-INDICE` **escribió la regla** —enlazar el manifiesto— y **este gate la incumplió en `HEAD`**: `T147 FALLIDA`, runner 12/13. Y arrastra las cuatro `N147*` a vacuidad (`T-13`) | **NO CERRADO** |
| `Q-25` doc 22 · el README promete por encima del código | — | **VIVO Y AMPLIADO.** El README L41-42 dice «*los manifiestos … son **inmutables** … los fija `G-22`*» y L70 dice «*el documento 23 **nace protegido***». Lo comprobé: un `docs/evolucion/23-*.md` sin rastrear **nace ADMITIDO** (`R-A`), no protegido, y los cuatro manifiestos son editables con un `commit` (`R-C`) | **NO CERRADO** |
| `Q-26` doc 22 · docs 19/20/21 sin rango inmutable | ver GRAVE 8 | ver GRAVE 8 | **NO CERRADO EN SU CLASE** |
| `Q-27` doc 22 · `_CAPS` con ficheros vs `G-24` con `isdir` | derivar el catálogo una sola vez | `_capacidades()` filtra por `isdir` (L546) — **corregido**. Pero `G-24` **recomputa** en L1716 en vez de usar `_CAPS_DIRS`: la sede nueva se creó y **la vieja no se retiró** | **CERRADO EN LA LETRA · NO EN EL FONDO** (`T-16`) |
| `P-08` doc 21 ≡ el universo derivado | universo derivado, comando público, restas verificables | **CERRADO, y es el logro más sólido.** Reejecuté el derivador sobre `e3163967`, `6b5d3e6` y `c36d2ba`: 64 fuentes en los tres. Crucé las 64 rutas derivadas contra las 64 filas del manifiesto de este gate con `comm`: **vacío en las dos direcciones** | **CERRADO** *(con `T-10`: el titular de líneas del manifiesto no deriva)* |
| GRAVES 1, 2, 3, 4 del doc 22 · `R-04`/`W17` · Estructural · `reconciliacion_pendiente` · §15.8 | — | **FUERA DE MI LOTE.** Sedes: documento 11 y registro de decisiones, asignados a `S`. **No los adjudico y no los presumo** | **FUERA DE MI LOTE** |
| los 34 MEDIOS y 27 MENORES restantes | — | El grueso vive en el documento 11, el checkpoint y el registro. **FUERA DE MI LOTE** | **FUERA DE MI LOTE** |

```text
RECUENTO, sólo sobre lo que `T` puede adjudicar

  CERRADO                              5   G-16 · G-01 · lector estructurado · fixture
                                           _derivar_vigiladas · P-08 (universo derivado)
  CERRADO EN SU FORMA, NO EN SU CLASE  3   R-N1/G-22 · unicidad de proyección · Q-27
  PARCIALMENTE CERRADO                 1   el derivador
  NO CERRADO                           7   M-04 · el perímetro de conjuntos · G-26 ·
                                           la excepción del kernel · exclusiones/T147 ·
                                           el README · Q-26
  FUERA DE MI LOTE                     resto
```

---
## 9 · REFUTACIONES QUE INTENTÉ Y NO CAYERON

Las publico con el mismo detalle que los hallazgos, porque un dictamen que sólo enseña lo que
confirma no mide nada. **Seis, y las tres primeras son las que más quería que cayeran.**

**`RF-1` · Intenté que `G-01` cediera a la palabra «RETIRADA», que es como cae en el documento 22.
NO CAYÓ.**
Método: inserté en §16 del documento 11 el párrafo que **deroga** la retirada de
`estado/cuarentena/` —«*NORMA VIGENTE REINSTAURADA: … esa ruta es CANONICA y fuente de verdad
para todo el sistema. La nota que hablaba de una RETIRADA queda SIN EFECTO*»— usando la palabra
exenta en la posición exenta.
Resultado: **`FALLO G-01`, 36/37**, con el título reescrito para decir lo que hace: «*cada mención
se juzga por POLARIDAD y la sede canónica la ancla*». **La protección 4 generaliza, y lo digo sin
matiz.**

**`RF-2` · Intenté que `G-16` cediera a una calificación añadida detrás del estado, que es el
`Q-06` del documento 22. NO CAYÓ.**
Método: reescribí la fila de detalle vigente de `C-L.1` en `CHECKPOINT-ADS-NEXT.md` L1480 a
«CERRADA SOLO EN PARTE, SIGUE ABIERTA Y BLOQUEA F5».
Resultado: **`FALLO G-16`**, y el diagnóstico **nombra el mecanismo que lo cierra**: «*El
contraste es por IGUALDAD, no por prefijo: una calificación añadida detrás cambia el estado*».
**La protección 3 generaliza.**

**`RF-3` · Intenté que el manifiesto inmutable siguiera desprotegido, que es la segunda mitad del
`R-N1` del documento 22. NO CAYÓ en su forma.**
Método: `sed -i 's/59 fuentes/9 fuentes/g; s/41 174/1 000/g'` sobre
`F4C-ASIGNACION-GATE-CERTIFICACION-20260830.md`, **sin confirmar**, que es exactamente lo que `R`
hizo para obtener 30/30.
Resultado: **`FALLO G-22`, 36/37.** **La mitad de `R-N1` está genuinamente cerrada**, y es
importante decirlo: el inventario **se derivó de verdad** y **creció de 4 documentos a 27
ficheros**. Lo que sobrevive es el ancla, no el inventario, y por eso `T-02` acusa la comparación
y no el rango.

**`RF-4` · Intenté ocultar una segunda sede a `G-29` con `.gitignore`** —un vector que `T1` dejó
expresamente abierto—. **NO CAYÓ.**
Método: `cp docs/rediseno/a-CAPACIDADES-APROBADA.md docs/rediseno/SEGUNDA-SEDE-OCULTA.md` y
añadir la ruta a `.gitignore`, para que `git status` no la vea.
Resultado: **`FALLO G-29`, 36/37.** `_ficheros_zona()` recorre el disco con `os.walk` y no
pregunta a Git, de modo que el fichero ignorado **sí** entra en `_disco` y sale como ampliación no
clasificada. **La topología de `G-29` no depende de `git status`, y eso está bien hecho.**

**`RF-5` · Intenté abrir un hueco en la serie `D` sin que `G-20` lo viera. NO CAYÓ.**
Método: borré la fila `| D50 |` entera del registro de decisiones —del **medio** de la serie, no
del final—.
Resultado: **`FALLO G-20`, 36/37.** *(Lo que sí cae, y va en `T-08`, es borrar la **última**:
`D107` no deja hueco porque el tope se deriva del máximo presente.)*

**`RF-6` · Intenté que `G-31` cediera a alguna de sus diez palabras gatillo. NO CAYÓ.**
Método: las diez palabras contra los cuatro evaluadores, tal y como la propia comprobación las
prueba, y con el mismo dato pegado.
Resultado: ninguno cambia de veredicto. **El interruptor léxico está cerrado**, y `G-31` es la
única comprobación de la tanda que se prueba a sí misma con contraejemplos ejecutables en vez de
con prosa. *(Y es también la que certifica que el interruptor de ETIQUETA sí apaga, que es
`T-06`. Las dos cosas son verdad a la vez.)*

**Y una refutación mía que perdí y que publico porque era mi apuesta.** Intenté demostrar que el
manifiesto de este gate asignaba fuentes fuera del universo, o dejaba fuentes del universo sin
asignar —el defecto `P-08`, reinstalado—. Volqué las 64 rutas de `--rutas` y las 64 filas de §4 y
§5 del manifiesto y las crucé con `comm`:

```text
comm -23 universo manifiesto   →  (vacío)     OBLIGATORIO − ASIGNADO = 0
comm -13 universo manifiesto   →  (vacío)     ASIGNADO − OBLIGATORIO = 0
comm -12 universo manifiesto   →  64
64 filas del manifiesto recalculadas (líneas) contra el árbol  →  0 discrepancias
```

**NO CAYÓ. La primera resta de `1bis` es verdadera, ruta a ruta, y sobre un universo que este
gate no eligió.** Lo único que sale mal es el **titular de líneas** (`T-10`), que es una cifra y
no un reparto. **`C-L.5` no se reabre por nada de lo que yo traigo.**

---
## 10 · LO QUE NO HE CUBIERTO, SIN ADORNO

1. **No he leído ninguna fuente del lote de `S`**: ni el documento 11 (10 275 líneas), ni
   `DECISIONES-Y-CONTRADICCIONES.md`, ni `CHECKPOINT-ADS-NEXT.md`. Todo lo que toqué de esos
   ficheros lo toqué **para mutarlo en el laboratorio o para derivar una cifra con `grep`**, y
   **eso no es lectura**. Por tanto **no digo nada** sobre `O17` como resolución, sobre `D107`
   como propagación, sobre los cuatro macrocircuitos, sobre §9.6, sobre el sujeto de seis
   identificadores, sobre `PN-17`/`PN-18`, ni sobre `C-L.3`. Mi `R-H` prueba que **la batería no
   los lee**; no prueba nada sobre si están bien.
2. **No he leído los documentos 19, 20 ni 21.** Los volteos de `R-C` se hicieron **a ciegas con
   `sed -i`**, mirando sólo recuentos de `grep -c`. No puedo decir qué afirman, ni si los volteos
   que hice son los que un adjudicador malicioso elegiría.
3. **Cuatro de mis veintidós no los reproduje**: `T-20`, `T-21`, `T-22` y la mitad experimental de
   `T-15`. Están marcados en su fila. Los acepto de mis relevos con su atribución, y **un
   adjudicador que quiera apoyarse en ellos tiene que rehacerlos**.
4. **No he auditado las otras 53 mutaciones sin `espera` de `comprobar_negativos.py`.** Medí el
   censo —63 mutaciones, 10 con `espera`— y demostré la vacuidad **sólo** de las cuatro `N147*`,
   que son las que hoy cuelgan de una prueba en rojo. **Cualquier otra prueba que caiga en rojo
   por otra causa arrastrará las suyas a la misma vacuidad, y nadie lo verá.** Es la
   recomendación que dejo abierta.
5. **No he auditado `G-02`…`G-07`, `G-09`, `G-10`, `G-12`, `G-13`, `G-14`, `G-17`, `G-18`,
   `G-19`, `G-25` ni `G-27` con contraejemplos propios.** Que la batería caiga por siete puertas
   no significa que sólo haya siete.
6. **No he probado** enlaces simbólicos, permisos, nombres Unicode confusables (`2З-…md` con `З`
   cirílica), submódulos, condiciones de carrera, ni `.gitattributes`. `T1` los dejó abiertos y
   yo sólo cerré uno (`.gitignore`, `RF-4`).
7. **No he ejecutado `registrar_evidencia.py` sobre el árbol real**, deliberadamente. Tomo el
   `12/13` y los dos ficheros de evidencia ensuciados **de la medición de `T2`**, y lo verifiqué
   por otra vía —ejecutando `comprobar_referencias.py`, que no escribe, y obteniendo `T147
   FALLIDA · EXIT=1`—. La consecuencia sobre `git status` no la observé yo.
8. **No he auditado `exclusiones.yaml`** más allá de constatar que `T147` no está apagada para el
   manifiesto huérfano.
9. **No he juzgado si la corrección sustantiva de F4c es correcta.** Sé qué puede pasar por esta
   batería sin que se note. No sé si la arquitectura está bien, y no lo digo.
10. **Ningún ojo único recorrió las 2 685 líneas de la batería seguidas ni las 3 478 del documento
    22 seguidas.** Declarado en §2, y lo repito aquí porque una resta que da cero lo esconde.

---
## 11 · MI RECOMENDACIÓN DE VEREDICTO, Y SUS RAZONES

**La cobertura de `T` está cerrada** —`ASIGNADAS − LEÍDAS ÍNTEGRAS = 0`, nueve de nueve, con los
nueve SHA-256 recalculados por mí— y por tanto **NO procede** `INSUFICIENTE PARA F5 POR
COBERTURA`. Mi recomendación se emite **sobre el fondo**.

# INSUFICIENTE PARA F5

### Las razones, numeradas. Las dos primeras bastan cada una por sí sola.

**1 · `M-04` sigue FALLIDA, por tercer gate consecutivo, y la reproduje yo con mis manos.**
Construí y ejecuté **siete árboles defectuosos que pasan la batería `37/37` en verde con
`EXIT=0`**, más un verde-sobre-cero, más una instancia viva en `HEAD` sin mutar nada. **El peor
no es una hipótesis:** el validador que corre las 67 mutaciones negativas del kernel está vaciado
a `import sys; sys.exit(0)`, sus tres ficheros de evidencia están inventados, la huella está
reanclada **con el valor que la propia batería publica al fallar**, todo confirmado, `git status
--porcelain` vacío, y la batería imprime `37/37 comprobaciones en verde` y
`OK G-30 … ninguno difiere de HEAD`. **Y el segundo peor:** volteé quince veces `INSUFICIENTE
PARA F5` a `SUFICIENTE PARA F5` en el documento 21, confirmé, y `G-22` dice «*25 inmutables
derivados … intactos frente a `HEAD` y a `05f71b7`*» mientras `G-28` dice «*25 documentos de gate
contrastados … sin una sola inversión*». **Es la razón 1 del veredicto del documento 22, palabra
por palabra, un gate después y con siete protecciones nuevas encima.**

**2 · Las quince protecciones no curaron el patrón: lo repitieron un nivel más arriba, y lo
verifiqué en las dos direcciones para las quince.** **Trece de los quince remedios que el
documento 22 prescribió están literalmente ejecutados** —el inventario se deriva, la marca es una
etiqueta, el conjunto abarca tres zonas, la excepción tiene clase, la huella se recalcula, la
sangría se aplica, el fixture dejó de ser tautológico— y **nueve de las quince siguen sin cerrar
la clase**, porque cada remedio se escribió con la forma exacta del contraejemplo que lo motivó:
el inventario creció y la comparación no, y basta **un `git commit`**; el conjunto creció una zona
y se abrió un `return True` **dentro de la zona nueva**; la palabra se cerró y **la etiqueta la
sustituyó**, con `G-31` certificando que el interruptor nuevo funciona; la unicidad se cerró
dentro de una ventana delimitada por **dos cadenas literales**, y basta **una línea más abajo**.
El documento 22 escribió que «*una garantía mecánica que protege cuatro documentos de siete y
llama a eso «los documentos no se han tocado» es peor que no tenerla*». Hoy protege veintisiete,
diecinueve de verdad, y **sigue llamando a eso «intactos»**.

**3 · Las protecciones 12, 13, 14 y 15 dicen derivarse de una resolución del Owner que ninguna
línea de código lee.** El comentario L2519 afirma que están «*todas derivadas de `O17` y de su
propagación `D107`*». `grep -n 'O17'` sobre la batería devuelve **cinco líneas y las cinco son
comentario o cadena de diagnóstico**; `G-21` protege `O1`-`O16` y se detiene justo antes. Sustituí
la fila `| O17 |` por su **negación exacta** y borré la fila `| D107 |` entera: **`37/37` verde**.
**El instrumento que este gate existe para certificar no puede notar que se ha anulado la
resolución que el gate existe para certificar.** Y tres de sus cuatro pruebas negativas son
**infalsificables por cualquier estado del corpus**: autotests de funciones que la batería escribe
sobre datos que la batería inventa, declarados en el título como si el sujeto fuera el árbol.

**4 · El árbol que se somete a certificación falla hoy un validador canónico, y eso arrastra
cuatro pruebas negativas a la vacuidad — `M-04` sin necesidad de mutar nada.** En `c36d2ba`
limpio, `comprobar_referencias.py --exclusiones` da `T147 FALLIDA · 0 superadas · 1 fallidas ·
EXIT=1`, causado por el manifiesto de **este** gate publicado sin enlazar — que es exactamente lo
que `00-INDICE` L106-108 advierte por escrito. Con `T147` en rojo, `N147`, `N147b`, `N147c` y
`N147d` —ninguna con `espera`— pasan **con o sin su mutación**: lo demostré convirtiendo la
mutación en `return  # NO-OP` y obteniendo `67 infracciones detectadas · 0 NO detectadas ·
EXIT=0`. Y el mecanismo cubre **53 de las 63 mutaciones**. El documento 22 prescribió el remedio
—«*que los manifiestos que `1bis` obliga a publicar no rompan `T147`, y que no rompan uno más cada
gate*»—; se escribió la regla en `00-INDICE` y **se incumplió en el commit siguiente al que la
escribe**.

**5 · Y el manifiesto que gobierna este gate publica como derivado un total que no deriva, en el
bloque de las dos restas de `1bis`.** Declara `64 fuentes · 47 728 líneas`; el derivador que él
mismo publica da **48 138** en los tres árboles en juego, y **sus propios dos subtotales suman
48 138**. La diferencia es **exactamente 410 = las líneas de `derivar-universo-obligatorio.py`**,
el fichero que ese mismo párrafo presenta como «*el propio derivador, que pasa a juzgarse a sí
mismo*». En el documento cuya tesis es «*aquí el universo no se escribe: se deriva*». **Es la
clase de defecto que el aparato existe para impedir, en el titular del aparato.** *(Y el mismo
manifiesto no está dentro del universo que gobierna: sólo los tres anteriores lo están.)*

### Lo que expresamente NO fundamenta mi recomendación

- **NO recomiendo por cobertura.** `ASIGNADAS − LEÍDAS = 0` en `T`, y lo calculé. **`C-L.5` no se
  reabre por nada de lo que yo traigo**, y `OBLIGATORIO − ASIGNADO = 0` es verdadero ruta a ruta
  sobre las 64, comprobado por mí con `comm` en las dos direcciones.
- **NO recomiendo por el derivador.** Es un programa **duro**: resiste diez de los catorce ataques
  de `T2` con código 2 y diagnóstico nombrado, no depende del `cwd` ni de Git, y la guarda de
  unicidad que `R-N2` pidió **está puesta**. Lo que falla es una promesa más ancha que el
  programa, y su carácter anotado está declarado con honestidad.
- **NO recomiendo por el corrigendum.** **Acota sin editar, y lo verifiqué con `git`**: los
  documentos 20 y 21 y los cuatro manifiestos tienen **un solo commit cada uno en toda su
  historia**, y entre `e6c1b1f` y `HEAD` no se ha tocado ninguna sede acotada. Su segunda mitad
  —prohibir citar una frase acotada sin citar la acotación— es una pieza excelente.
- **NO recomiendo por el aparato de cobertura del gate anterior.** Intenté tumbarlo y no cayó:
  las restas cuadran al dígito, las doce agotadas se sostienen, y el `ADDENDUM 1` **promete de
  menos** que lo que su propia evidencia sostiene.
- **NO recomiendo porque quede arquitectura por inventar.** **Ninguno de mis veintidós hallazgos
  es BLOQUEANTE** con el criterio que `R` usó: los veintidós se cierran con material que el
  corpus ya tiene escrito.

### Lo que SÍ ha quedado cerrado, porque también es información

1. **Cinco de los remedios del documento 22 están cerrados de verdad, con control positivo mío:**
   `G-16` por igualdad exacta, `G-01` por polaridad, el lector estructurado aplicando la sangría,
   el fixture de `_derivar_vigiladas` con tres casos que **pueden fallar más dos contrastes contra
   el árbol real**, y el universo derivado (`P-08`).
2. **La mitad de `R-N1` está cerrada**, y es la mitad que el documento 22 reprodujo: el inventario
   de inmutables **se deriva** y **creció de cuatro documentos a veintisiete ficheros**, y la
   edición **sin confirmar** de un manifiesto declarado inmutable hoy **se caza** (`RF-3`).
3. **`G-31` es la mejor pieza de esta tanda**: la única comprobación que se prueba a sí misma con
   contraejemplos ejecutables —diez palabras gatillo × cuatro evaluadores— en vez de con prosa. No
   cede.
4. **La topología de `G-29` no depende de `git status`** y por eso `.gitignore` no la engaña
   (`RF-4`); `G-20` caza el hueco en el medio de la serie (`RF-5`); `G-11b` falla cerrado sin
   `.git`; `G-24` lee de verdad.
5. **El corrigendum acota sin editar, verificado con `git log`, y sin asteriscos.**

**Y la frase con la que cierro, que es la del documento 22 sin una palabra cambiada, porque un
gate después sigue siendo exacta:** esta candidata *«no falla por concepción, no falla por
cobertura, no falla por lo que decidió y no falla por lo que dejó sin construir. Falla porque el
instrumento que existe para probar que sus decisiones han llegado a todas partes no puede
distinguir un árbol sano de uno»* en el que el validador de negativos está vaciado a
`sys.exit(0)`, la resolución `O17` del Owner está anulada, y el veredicto del gate anterior dice
`SUFICIENTE PARA F5`.

> **Yo RECOMIENDO. El veredicto lo emite el adjudicador `U`, que no soy yo.** `U` recalcula por su
> cuenta universo, asignaciones, lecturas, cobertura, severidades y recuentos, y puede revocar
> cualquiera de mis veintidós adjudicaciones, mis cuatro rechazos y mis cinco rebajas. **No he
> visto el dictamen de `S` y no lo veré.**

---
## 12 · CIERRE

```text
git status --porcelain   →   (salida vacía)      VERIFICADO al abrir y al cerrar
git rev-parse HEAD       →   c36d2ba707eed5ea24b9a13df6c4e6be49b68cc6   (sin cambios)
RAMA                     →   gate/f4c-certificacion-2-20260830
SHA-256 del documento 22 →   3e2bdece758e6b69d6695bb52f20d21b910a123a27ac643845dbad75e8355f1c

FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS   ninguno
COMMITS · PUSH · PR · MERGE                              ninguno
LABORATORIO   /tmp/lab-T3/{base,expA…expF,p2a,p2b,p3,p5,g15a,g15b,o17,r1,r2,r3,vac,
              t-e316396,t-6b5d3e6,fakebin} — BORRADO con `rm -rf`
FICHEROS S1.md · S2.md · S3.md · DICTAMEN-S.md           NO ABIERTOS
SUBAGENTE `Agent`                                        NO USADO
NINGÚN HALLAZGO SE HA CORREGIDO, y es deliberado.
```

**`F4c` sigue ABIERTA por mi parte. `F5` NO queda autorizada por mi parte.**

**REVISOR `T` · dictamen cerrado por `T3`.**

---

# §C · ADJUDICACIÓN DEL ADJUDICADOR `U`, LITERAL

# ADJUDICACION-U — Adjudicador unico, 2.o Gate Independiente de Certificacion F4c

Rama: gate/f4c-certificacion-2-20260830 · HEAD c36d2ba
Apertura: `git status --porcelain` VACIO (verificado).

(en construccion — se escribe incrementalmente)

## 3 · COBERTURA RECALCULADA POR MI (parcial — restas y agotamientos)

### 3.1 El derivador, ejecutado por mi
`python3 docs/evolucion/verificacion/derivar-universo-obligatorio.py` → exit 0
Salida: **64 fuentes obligatorias · 48 138 lineas**
  (i) 4 · (ii) 29 · (iii) 3 · (iv) 12 · (v) 26

### 3.2 RESTA 1 — OBLIGATORIO menos ASIGNADO = **VACIA**
Igualdad exacta de conjuntos: los 64 paths del derivador == los 64 paths del manifiesto.
Ni una fuente sin asignar, ni una asignada de mas.

### 3.3 Verificacion mecanica de las 64 filas del manifiesto contra el arbol de trabajo
**0 discrepancias** de SHA-256 y **0** de recuento de lineas. Las 64 filas son exactas.

### 3.4 Los 52 AGOTAMIENTOS — **52/52 PLENOS**
Para cada uno verifique las DOS condiciones de la regla de §5:
 (1) fila propia con `LEIDO INTEGRO` en el documento y linea citados → 52/52 OK
 (2) bytes identicos entre el arbol candidato y el arbol que ese gate leyo
     (`4d231ee` / `7764cca`) → 52/52 OK, comparacion blob a blob.
Ningun agotamiento se cae. Corroboro ademas que el documento 11 NO se declara agotado
(doc22 L275 lo registra con 9 494 lineas y otro SHA): el manifiesto es honesto ahi.

### 3.5 `T-10` de `T3` — **CONFIRMADO, Y AGRAVADO**
`T-10` afirma que el manifiesto publica 47 728 donde el derivador da 48 138 y que la
diferencia son las 410 del derivador. Es cierto: 48 138 − 47 728 = **410**, exactamente
las lineas de `derivar-universo-obligatorio.py` (fila 8 del reparto).
**Lo agravo**: no hace falta salir del manifiesto para verlo. Sus PROPIAS dos subsumas
de §6 —21 530 asignadas a lectura + 26 608 agotadas— suman **48 138**, tres lineas por
encima del total que el mismo parrafo publica como 47 728 (L173). El manifiesto se
contradice a si mismo en la misma seccion. La cifra 47 728 es un residuo anterior al
commit `6b5d3e6`, que fue el que metio el derivador en el componente (v).

## 7 · `M-04`: LO QUE REPRODUJE YO  (laboratorio /tmp/lab-U/, copias `cp -a`, fuera del repo)

BASELINE `/tmp/lab-U/base`, porcelain vacio, HEAD c36d2ba → **37/37 en verde · EXIT=0**.
Confirmo de paso `T-09` a simple vista: el titulo dice «las TRES pruebas negativas» y el
detalle de la misma linea imprime «4 pruebas negativas ejecutadas».

### Reproduje TRES de los arboles de `T`, y AMPLIE dos

**R-D · el validador de negativos vaciado — 37/37 VERDE**
`comprobar_negativos.py` → `import sys; sys.exit(0)`; las tres evidencias
(`fuentes/negativos/referencias-salida.txt`) falsificadas; primera pasada `FALLO G-30`, **y la
propia bateria me publica la huella que necesito** (`el árbol deriva 22aee308f163d32a`); la
escribo en `kernel/.upstream-hash`, `git commit` → **37/37 · EXIT=0 · porcelain vacio**, con
`OK G-30`. **CONFIRMO `T-01`.** Es el peor resultado del lote, y coincido con `T`.

**R-C · veredictos volteados — 37/37 VERDE, Y LO AMPLIO**
`T` volteo el documento 21 y un manifiesto. **Yo voltee el documento 21 (15) Y EL DOCUMENTO 22
(11)** — el documento cuyos 68 hallazgos de clase A esta tanda dice haber cerrado, y que es
fuente obligatoria del componente (iv). `git commit`, porcelain vacio → **37/37 verde**, con
`OK G-22 … intactos` y `OK G-28 … sin una sola inversión`. Hoy el documento 22 de ese arbol
dice en su L3 «Veredicto del adjudicador `R`: `SUFICIENTE PARA F5`». **CONFIRMO `T-02`.**

**R-A · segunda sede normativa como documento numerado — 37/37 VERDE**
`23-SEGUNDA-SEDE-NORMATIVA.md` («CONTRADICE `C4` y `C7` y PREVALECE» + copia de
`a-CAPACIDADES-APROBADA.md`). **Verde sin rastrear Y verde confirmado** (`T` solo probo sin
rastrear). Causa: `L2194-2195`, `return True` sin mirar contenido. **CONFIRMO `T-03`.**

### CUATRO que NADIE de los dos ejecuto — dos caen, dos no

**U-2 · AMPUTAR UNA COMPROBACION — `36/36 comprobaciones en verde` · EXIT=0**
`T-20` estaba declarado **NO reproducido** por `T3` («no ejecuté la amputación»). **Lo ejecute
yo.** Borre el bloque `check("G-31", …)` (L2449-2454), `git commit`, porcelain vacio:
**`36/36 comprobaciones en verde`, EXIT 0, y `G-31` NO APARECE en la salida** — `grep -c G-31`
sobre el informe da **0**. La bateria no esta en ningun inventario de integridad y su propio
censo no se contrasta contra ninguna sede, luego una amputacion es INVISIBLE. Y lo amputado es
justo la comprobacion que `T3` llama «la mejor pieza de la tanda». **`T-20` sube de MENOR
(aceptado sin reproducir) a GRAVE, reproducido por mi.**

**U-3 · FALSIFICAR UNA PRUEBA DE AGOTAMIENTO — 37/37 VERDE · HALLAZGO MIO**
Inserte en el documento 22, tras L1578, una fila fabricada:
`| 99 | docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | 10275 | 47f924c9… | Q9 | **LEÍDO ÍNTEGRO** |`
—el documento 11, 10 275 lineas, que NADIE leyo en el gate del documento 22, atribuido a un
revisor `Q9` que no existe, con el SHA-256 correcto de hoy—. `git commit`, porcelain vacio →
**37/37 verde**. Ver §6, `U-01`: esto alcanza al aparato de COBERTURA, no solo a la bateria.

**U-6 · SEGUNDAS SEDES FUERA DE `_ZONAS` — 37/37 VERDE**
`_ZONAS = ("kernel", "docs/rediseno", "docs/evolucion")` (L2149). Copie material APROBADO a
`docs/owner/RECORRIDO-VIGENTE.md` (con cabecera «PREVALECE SOBRE TODO») y a `CAPACIDADES-RAIZ.md`
en la RAIZ. Confirmado → **37/37 verde**. `T` señalo que las zonas eran incompletas; **no lo
ejecuto. Yo si.** Y nota: `docs/owner/` YA EXISTE en el arbol — no es un directorio inventado.

**U-4 · el universo encoge en silencio — CONFIRMADO**
Borre una fila de `ENCARGO` en el derivador: `(v) 26 → 25`, **EXIT=0, sin aviso**, y la bateria
sigue **37/37**. Confirma `T-15` por ejecucion.

### DOS REFUTACIONES MIAS QUE FALLARON — y constan a favor

**U-1 · editar MATERIAL APROBADO con commit → `FALLO G-23`, 36/37.** Altere
`a-CAPACIDADES-APROBADA.md` (derogar §a.0, invertir «DOM y SEG aportan» → «NO aportan») y
confirme: **se caza**. Lo normativo aprobado SI esta anclado. Es una proteccion real.

**U-5 · borrar una fuente obligatoria entera → `FALLO G-24`, 36/37, Y el derivador FALLA
CERRADO con codigo 2 real** (`EXIT REAL = 2`, medido sin tuberia). El derivador cumple lo que
el manifiesto promete en su §2. **El derivador es duro, y coincido con `T`.**

### MI VEREDICTO SOBRE `M-04`
**SIGUE FALLIDA, y con margen.** Cuento **SEIS arboles defectuosos en verde construidos por mi**
(R-D, R-C, R-A×2 formas, U-2, U-3, U-6), dos de ellos por vectores que **ningun revisor de este
gate ni del anterior habia ejecutado**. `M-04` no solo sobrevive a su tercer gate: sobrevive a
un adjudicador que llego despues de que dos revisores independientes la hubieran atacado, y
**encontro puertas nuevas en menos de una hora**. Eso es lo que hay que pesar: no que haya ocho
o quince agujeros, sino que **el coste marginal de encontrar el siguiente no esta subiendo**.


---

## 1 · IDENTIDAD, INDEPENDENCIA Y MODO

Soy `U`, adjudicador unico del SEGUNDO GATE INDEPENDIENTE DE CERTIFICACION de F4c. **Emito el
veredicto y no corrijo nada.**

**Que NO soy.** No he escrito ninguna parte de este corpus. No he aplicado ninguna correccion.
No fui revisor `A`-`R` ni `P1`-`Q5` de ningun gate anterior, ni participe en el gate del
documento 22. **No habia visto ningun dictamen hasta abrir los dos que recibo, que llegaron YA
CERRADOS.** No he abierto `ADJUDICACION-R.md`, `DICTAMEN-P.md`, `DICTAMEN-Q.md` ni las notas
`P*`/`Q*` del directorio: son de gates anteriores y su lectura habria contaminado mi juicio
sobre el documento 22, que es fuente de mi lote. Lo que se de los gates 21 y 22 lo se por sus
documentos publicados, que si me estan asignados.

**No he usado el subagente `Agent`.** Todo el trabajo es mio, con `bash`, `git`, `grep`, `awk`,
`sed` y el `python3` del shim (3.12.14).

**Modo, comprobado en los dos extremos:**

```text
git status --porcelain  AL ABRIR    → SALIDA VACIA   (primer comando de la sesion)
git status --porcelain  AL CERRAR   → SALIDA VACIA   (ultimo comando de la sesion)
HEAD al abrir y al cerrar           → c36d2ba707eed5ea24b9a13df6c4e6be49b68cc6, identico
RAMA                                → gate/f4c-certificacion-2-20260830
FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MI   ninguno
COMMITS · PUSH · PR · MERGE                                     ninguno
LABORATORIO   /tmp/lab-U/{base,RA,RC,RD,U1,U2,U3,U4,U5,U6,U7} — copias `cp -a`, BORRADO
```

Cree ademas un `git worktree` temporal sobre `e316396` para medir el arbol de la tanda, y lo
**retire con `git worktree remove --force` + `git worktree prune`**; comprobe despues que
`git worktree list` solo muestra el repositorio principal y que el porcelain sigue vacio.

**Sobre el objeto juzgado, y es un hecho que consta.** El manifiesto reparte el commit candidato
`e3163967` / arbol `2451141c`. HEAD es `c36d2ba`, dos commits por encima:

```text
6b5d3e6  feat(gate): fijar el componente (v) del universo    1 fichero (el derivador)
c36d2ba  docs(gate): publicar el manifiesto previo            1 fichero (el manifiesto)
```

**Los dos son el aparato de este mismo gate.** El corpus juzgado es byte a byte el del arbol
repartido — **con UNA excepcion que nadie declaro, y que adjudico en §6 como `U-02`**.

---

## 2 · MI PROPIO MANIFIESTO DE LECTURA

| # | ruta | lineas | SHA-256 recalculado por MI | cobertura | 1.a / ultima seccion sustantiva | ancla A · ancla B (regiones separadas) |
|---|---|---|---|---|---|---|
| 1 | `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md` | 240 | `c64a0ec4731e6d27751469e84cbcc33104bfe535c42efe4f98533f4d84a0b970` | **LEIDO INTEGRO** (`cat -n`, una pasada) | L1 `# MANIFIESTO PREVIO DE ASIGNACION` / L224 `## 8 · Regla de cierre` | L36 «`UNIVERSO DERIVADO 64 fuentes · 47 728 lineas`» · L227 «CUALQUIER FUENTE ASIGNADA Y NO LEIDA INTEGRAMENTE EXCLUYE LA SUFICIENCIA» |
| 2 | `docs/evolucion/00-INDICE.md` | 148 | `004cad57881dc75d08cae8311c5e9b4334cd7c424330769657fcf11d3557ab1b` | **LEIDO INTEGRO** (una pasada) | L14 `## Los documentos en voz del Owner` / L143 `## Lo que este trabajo ha corregido de si mismo` | L101-107 «Quien publique un manifiesto sin enlazarlo aqui deja el arbol que juzga con un validador canonico en rojo» · L119-121 «la lista se deriva con `find …`» |
| 3 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | 2782 | `e9078a7434d2a8a898d0d4edec242aee7fcac289c8f1dea3dfcf0f669c5b8a7a` | **LEIDO INTEGRO**, 7 tramos consecutivos: `1-330 · 330-709 · 710-1109 · 1110-1529 · 1530-1949 · 1950-2379 · 2380-2782`. **Union = [1, 2782]. Ni un tramo sin abrir** | L1 `# CHECKPOINT — ADS NEXT` / L2688 `## Siguiente accion exacta — HISTORICA` | L6-8 «**Basta decir «Continua»**» · L2428 «`EXCEPCION EXACTA DEL KERNEL` — deja de ser cierto que «`kernel/operativo/` esta intacto»» |
| 4 | `docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md` | 3478 | `3e2bdece758e6b69d6695bb52f20d21b910a123a27ac643845dbad75e8355f1c` | **LEIDO INTEGRO**, y **DESPUES** de las otras tres y de todos mis experimentos, que es la regla de orden del encargo. 9 tramos: `1-270 · 270-709 · 710-1149 · 1150-1599 · 1600-2049 · 2050-2499 · 2500-2939 · 2940-3239 · 3240-3478`. **Union = [1, 3478]** | L7 `## 0 · Que es este documento` / L3350 `## 14 · VEREDICTO`, cerrada en L3478 | L3 «Veredicto del adjudicador `R`: `INSUFICIENTE PARA F5`» · L3313 «**LA PREGUNTA EXACTA PARA EL OWNER**» |

**Los cuatro SHA-256 los recalcule yo y los cuatro coinciden** con los del manifiesto (filas 1, 3
y 4 de su §4; el propio manifiesto no esta en el universo — ver `T-15` y §6).

```text
FUENTES ASIGNADAS A `U`            4   (§6 del manifiesto: «ESTE manifiesto · documento 22 ·
                                       CHECKPOINT-ADS-NEXT · 00-INDICE»)
FUENTES LEIDAS INTEGRAS POR `U`    4
ASIGNADAS − LEIDAS INTEGRAS  =  0      CERO.
```

Mas las **52 AGOTADAS**, «cuya identidad de bytes verifica el mecanicamente» — hecho, §3.4.

**La reserva que declaro contra mi propio interes.** No he leido integro el universo obligatorio:
lei integras mis cuatro, y me apoyo —**declarandolo**— en los manifiestos de lectura de `S` y de
`T`, que no rehice fuente a fuente. Lo que si rehice es su **aritmetica** (§3), la **identidad de
bytes de las 64 filas** y **toda afirmacion material que sostiene una conclusion** (§4, §5, §6,
§7). Y no he leido los documentos 19, 20 ni 21: lo que el documento 22 dice de ellos lo
transcribo, no lo verifico — salvo las citas de agotamiento, que si comprobe una a una.


---

## 3bis · LA SEGUNDA RESTA — `ASIGNADO − LEIDO`

**Es la que EXCLUYE la suficiencia si no es vacia.** La calculo cruzando el manifiesto de este
gate contra los manifiestos de lectura de `S` (§2 de su dictamen) y de `T` (§2 del suyo).

```text
ASIGNADAS A LECTURA (§4 del manifiesto)          12 fuentes · 21 530 lineas

REVISOR S declara LEIDO INTEGRO    4   doc 11 (S1 L1-5200 · S2 L5201-10275) ·
                                       DECISIONES-Y-CONTRADICCIONES (S3) ·
                                       CHECKPOINT-ADS-NEXT (S3) · doc 22 (S4)
REVISOR T declara LEIDO INTEGRO    9   bateria (T1) · README (T1) · derivador (T2) ·
                                       manifiesto gate 22 (T2) · ADDENDUM 1 (T2) ·
                                       CORRIGENDUM (T2) · 00-INDICE (T2) ·
                                       CHECKPOINT-OPERATIVO (T2) · doc 22 (T3)

RUTAS DISTINTAS DECLARADAS LEIDAS INTEGRAS      12   (4 + 9 − 1: el doc 22 es comun)

ASIGNADO A LECTURA − LEIDO   =   ∅      CONJUNTO VACIO
LEIDO fuera de lo asignado   =   ninguna
```

**Verifique la asignacion de cada revisor contra el manifiesto, no de palabra.** §4 marca `S` en
las filas 2, 3, 4 y 12 —cuatro— y `T` o `T+U` en las filas 1, 3, 5, 6, 7, 8, 9, 10 y 11 —nueve—.
`4 + 9 = 13`, y una (el documento 22) es comun a los dos: **12 distintas**, que son exactamente
las 12 de §4. Coincide. Y los lotes son **complementarios**, como el manifiesto promete: ninguna
fuente de lectura esta asignada a los dos salvo el documento 22.

> **LA REGLA DE CIERRE DE `C-L.5` NO SE DISPARA. Las dos restas dan VACIO, y las CALCULE, no las
> presumo. Este gate NO falla por cobertura, y `C-L.5` sigue CERTIFICADA — por tercera vez
> consecutiva y sobre universo derivado.**

**Y la reserva de cadena, que la resta esconde y que peso yo.** Ningun ojo unico recorrio las
10 275 lineas del documento 11 seguidas, ni las 2 685 de la bateria, ni las 3 478 del documento
22. El manifiesto lo declara por delante como coste asumido y los dos dictaminadores lo repiten.
**Yo lo peso, y tiene consecuencia demostrable: ver `U-01` de §6, que es exactamente un hallazgo
que solo aparece al cruzar el lote de `S` con el de `T`, y que ninguno de los dos podia ver.**

---

## 4 · LAS DISCREPANCIAS ENTRE `S` Y `T`, RESUELTAS CONTRA LA FUENTE

**No resuelvo ninguna por mayoria.** Los lotes de `S` y `T` son complementarios y la mayor parte
de sus «discrepancias» son **abstenciones declaradas** —cada uno escribe «FUERA DE MI LOTE»
donde no tiene la fuente—, que es la conducta correcta y que consta a favor de los dos. Las
discrepancias materiales reales, y las dos internas de la cadena `S` que el encargo me manda
resolver, son estas.

### `D-1` · ¿EXCEDE `D107` A `O17`? — `S2` dice SI, `S3` dice NO, `S4` resuelve que §18

> **RESUELVO CONTRA LA FUENTE, Y CONFIRMO INTEGRAMENTE LA RESOLUCION DE `S4`.** Abri las cuatro
> sedes yo mismo y no acepte ninguna de palabra.

```text
`O17`, DECISIONES L728-735    «SEG conserva su capacidad de BLOQUEO cuando la estructura
                              incumpla seguridad»            → BLOQUEO. NI UNA PALABRA DE VIA

FILA `D107`, DECISIONES L452  «`SIS` es propietario y productor; `VER` produce el dosier;
                              `PLT` ejecuta la maquinaria…; `SEG` conserva su bloqueo»
                              → NO EXCEDE.  `S3` ACIERTA

§9.6 L7440-7441, SEDE UNICA   «`SIS` productor y propietario · `VER` el dosier · `PLT` la
                              maquinaria … · `SEG` el bloqueo»
                              → NO EXCEDE

§18 L9442·9445·9450·9453      «`SEG` **via 3** cuando hay superficie, y conserva su bloqueo»,
LAS CUATRO FILAS `FASE 0`     las cuatro en `proceso:SIS`
                              → **SI EXCEDE.**  `S2` ACIERTA
```

**Y el exceso lo desmiente la propia tabla, en el mismo proceso**, cosa que verifique fila a fila:

```text
L9443  fila `INS-0`-`INS-5`, `proceso:SIS`   →  «**`DOM` `DIS` `SEG` sin via: `PN-13`**»
L9449  fila `A9`-`A10`,      `proceso:SIS`   →  «**`SEG` sin via si hay superficie: `PN-13`**»
```

**Cinco filas del mismo `proceso:SIS` en una sola tabla: cuatro dan via 3 a `SEG` y dos se la
niegan citando la presion que la declara imposible.** Y la via 3 se define (§8.0 L5987-5992) como
«*figura en las `condicionales` del proceso CON SU CONDICION ESCRITA Y COMPROBABLE*», y la
condicion escrita es «cuando hay superficie», que es literalmente el antecedente que `PN-13`
declara sin vehiculo.

> **MI RESOLUCION.** `S2` y `S3` aciertan **sobre objetos distintos**, y `S4` lo resuelve bien:
> la fila `D107` NO excede, §9.6 NO excede, y **quien excede es §18** — que es, ademas, la sede
> que §8.0 L5968 declara que MANDA. Lo confirmo con la fuente delante y **hago mia la resolucion
> de `S4` sin cambiarle una coma**. Es `S-01`, GRAVE, y clase A: se cierra borrando dos palabras
> de cuatro filas.

### `D-2` · `S-09` · las dos reglas de precedencia — CONFIRMADA, y es lo que hace `D-1` peligroso

Localice las dos yo mismo:

```text
§8.0  L5968   «…narrativa: si alguna vez difieren, MANDA §18»
§9.6  L7345   «…§18 la mapea fase a fase. Si alguna vez difieren, **manda esta**»
```

**Dos reglas de precedencia solapadas, de sentido opuesto, sin jerarquia declarada — y ya han
producido su primera divergencia real, que es `D-1`.** Un lector que aplique §8.0 concluye que
`SEG` participa por via 3 en una ruta donde material APROBADO no la admite. **CONFIRMO `S-09`.**

### `D-3` · `S1-11` · ¿la Operativa se produce en una sola fase? ¿tiene la migracion un hueco no declarado?

> **CONFIRMO LAS DOS MITADES, derivadas por mi sobre el arbol.**

```text
§9.2 L7129, bloque PRODUCTOR DE CADA NIVEL   →   `operativo    INS-4`     y nada mas
§9.3 L7143, invalidacion                     →   `OPERATIVO  … cambia la disposicion del estado`
§8.3 L6609                                   →   `M3 migrar ESTADO PERSISTIDO, con su esquema`
§8.3 L6680                                   →   «M3 es el paso peligroso»
§8.3 L6594-6700, barrido «Operativa/operativo» →  **CERO golpes. §8.3 no la nombra ni una vez**
§9.6 L7497-7501, los cuatro recorridos       →   `M`: «FASE 0 Estructural → `M5` Integrada con lo
                                                 viejo TODAVIA EN PIE → `M7` revalidada»
§9.6 L7504-7509, «LA SALVEDAD, DICHA Y NO TAPADA» → declara SOLO el hueco de la ADOPCION
```

`M5` certifica **Integrada**; §9.2 fija `integrado presupone operativo`; «NIVEL ALCANZADO» exige
que **todos los presupuestos esten `verificado` Y VIGENTES**; y `M3` invalida la Operativa
heredada por el trigger literal de §9.3. **Ninguna fase `M0`-`M7` la reproduce.**

> **RESUELVO: `S-04` es correcto y es GRAVE.** El defecto no es que falte una decision del Owner
> —`O17` da productor al Estructural y a ninguno mas, y **no ampliarlo fue lo correcto**—: el
> defecto es que **la seccion escrita para no tapar huecos declara uno y calla el identico cuatro
> lineas mas arriba**. Declarar el de `A` y callar el de `M` en la misma enumeracion es peor que
> no declarar ninguno, porque el lector infiere que los otros tres estan completos.
> **Y confirmo el `X-6` de `S4`:** `U` NO arrastra el hueco —`U6` revalida y `U` no invoca
> `O12`, y §18 lo dice—. El hueco es de `M`, y solo de `M`.

### `D-4` · `S3-03` · ¿son falsas dos de las cuatro cifras del addendum de `D97`? — LAS DERIVE YO

```text
PUBLICADO (DECISIONES L377, bajo «LA CIFRA, DERIVADA HOY y no copiada»)
   documento 11   G20 12 · G21 10 · G22 16 · G23 13

MI DERIVACION SOBRE HEAD c36d2ba, con las tres variantes de barrido posibles
   grep -c        G20 13 · G21 10 · G22 16 · G23 14    ← FALLAN G20 y G23 (DOS de cuatro)
   grep -cw       G20 13 · G21 10 · G22 16 · G23 14    ← identico
   grep -c '`Gnn`' G20 12 · G21  9 · G22 13 · G23 12   ← FALLAN G21, G22 y G23 (TRES de cuatro)
```

> **CONFIRMO `S3-03` y la ampliacion de `S4`: bajo la lectura natural son DOS de cuatro las
> falsas, y NO EXISTE NINGUNA VARIANTE DE BARRIDO BAJO LA CUAL LAS CUATRO SEAN VERDADERAS HOY.**
> Las de (a), (b) y `E2` si lo son —las verifique: doce de doce—.
> **REBAJO la severidad de `S4` de GRAVE a MEDIO**, y digo por que en §5.

### `D-5` · `S3-04` / `T2-07` · `T147` en rojo y runner 12/13 — ¿culpa de la TANDA o del GATE?

> **RESUELVO CON MEDICION PROPIA, Y ES CONCLUYENTE. LA CULPA ES DEL GATE.**

```text
$ python3 kernel/operativo/validadores/comprobar_referencias.py --exclusiones   (sobre HEAD)
  T147  FALLIDA · 0 superadas · 1 fallidas · EXIT REAL = 1
  causa: F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md — «no lo alcanza ningun enlace»

$ el mismo comando sobre el arbol de la TANDA (e316396), en worktree fuera del repo
  1 superadas · 0 fallidas · EXIT = 0
```

Y la causa exacta, derivada con el comando que el propio `00-INDICE` publica en su L119-121:
`find docs/evolucion/verificacion -type f \( -name '*.md' -o -name '*.py' \)` devuelve **OCHO**
rutas; la tabla de L109-117 enlaza **SIETE**; la que falta es **el manifiesto de ESTE gate**,
publicado en `c36d2ba` por el coordinador de este gate.

> **`X-3` de `S4` es CORRECTO y lo hago mio**, y llego a el por una via que `S4` no uso: no por
> `git show --stat`, sino **ejecutando el validador sobre los dos arboles**. La regla se escribio
> en la tanda (`00-INDICE` L101-107) y **la incumplio el gate dos commits despues**.
> **`X-8` de `T3` tambien acierta** al rebajarlo a MEDIO: la regla funciona, la escribieron,
> publicaron el comando, el comando la comprueba y la denuncia. Lo que fallo es cumplirla.
> **CONSECUENCIA PARA EL VEREDICTO: este hecho NO cuenta contra la candidata.**
>
> **PERO separo lo que los dos mezclan.** La vacuidad de `N147`, `N147b`, `N147c` y `N147d`
> —`T-13`— **NO depende de quien enrojecio `T147`**: es una propiedad de
> `comprobar_negativos.py`, donde **53 de 63 mutaciones carecen del campo `espera`** que el
> propio fichero declara imprescindible. Enrojecer `T147` solo la hizo VISIBLE. **Ese defecto SI
> es del corpus y SI cuenta.**

### `D-6` · `T2-08` / `T3` · ¿tiene la suite de pruebas negativas mutaciones vacuas? — SI

Confirmo por lectura y por la aritmetica que `T3` publica y que rehice: `grep -c 'Mutacion('` da
**63** y `grep -c 'espera='` da **10**. El propio fichero declara (L47-49) que sin `espera` «*una
mutacion se da por detectada porque la prueba fallo, sin comprobar que fallo POR ESO*».
**Hoy son vacuas las cuatro `N147*` porque solo `T147` esta roja; el mecanismo cubre 53.**
**CONFIRMO `T-13`, MEDIO**, y anado la consecuencia que `T` deja abierta y que si es de gate:
**cualquier prueba que caiga en rojo por otra causa arrastrara sus mutaciones a la misma
vacuidad, y nadie lo vera** — porque el runner cuenta «67 infracciones detectadas · 0 NO
detectadas» tanto si la mutacion hizo algo como si no.

### `D-7` · `T-10` · el titular de lineas del manifiesto — CONFIRMADO Y AGRAVADO POR MI

Ver §3.5. `T3` tiene razon y la diferencia son exactamente las 410 del derivador. **Lo agravo: el
manifiesto se contradice a si mismo dentro de su §6**, cuyas dos subsumas (21 530 + 26 608) dan
48 138 tres lineas encima del total que publica como 47 728.

### `D-8` · La discrepancia sobre `M-04` que NO existe, y hay que decirlo

`S` **no adjudica** `M-04` y lo declara expresamente («FUERA DE MI LOTE. No la presumo ni cerrada
ni abierta»), aportando solo el dato de que la bateria da 37/37. `T` la adjudica FALLIDA con siete
arboles. **No hay discrepancia: hay una abstencion correcta y una adjudicacion fundada.** Y `S`
declara ademas que **su recomendacion no cambiaria** si `T` hubiera encontrado lo contrario.
Lo hago constar porque un adjudicador que confundiera abstencion con desacuerdo resolveria por
mayoria, que es justo lo que no puedo hacer.


---

## 5 · HALLAZGOS QUE RECHAZO, DE CUALQUIERA DE LOS DOS

**Rechazo dos, rebajo dos y ELEVO uno.** Lo hago con la misma fuerza con la que confirmo.

**`X-1` · REBAJO `S-06` de GRAVE a MEDIO** (el addendum de `D97` con cuatro cifras a mano, dos
falsas hoy). El hecho es exacto y lo derive yo entero (§4 `D-4`), incluida la causa raiz: la
cifra fue correcta en `78ec1cc` y caduco en `609863e`, **un commit despues, la misma tanda, el
mismo dia**. Y `S4` tiene razon en que el objeto juzgado es el REMEDIO y no la frase de `D97`.
**Pero por el criterio que los tres declaramos —GRAVE = una garantia publicada no se sostiene, o
`F6` construiria algo distinto—, esto no lo es: la resolucion de `D97` sobrevive intacta,
`PN-15` sigue en pie, su prueba posterior sigue fallando como debe, y ninguna cifra de las cuatro
cambia comportamiento alguno.** Es «una afirmacion vigente es falsa sin cambiar el
comportamiento»: **MEDIO**, que es exactamente como el adjudicador del documento 22 graduo la
misma clase en su `X-3`. Lo rebajo por consistencia de escala, no por benevolencia: **el hecho
entra entero, y su valor demostrativo —un remedio que caduca dentro de su propia tanda— lo
recojo en §14, que es donde pesa.**

**`X-2` · ELEVO `T-20` de MENOR a GRAVE, y lo hago porque lo REPRODUJE y `T3` no.**
`T3` declara honestamente que **no ejecuto** la amputacion y que acepta la premisa por lectura.
**Yo la ejecute** (§7, `U-2`): borre el bloque `check("G-31", …)`, confirme, y la bateria imprime
**`36/36 comprobaciones en verde` con `EXIT=0`**, sin que `G-31` aparezca una sola vez en el
informe. **Un hallazgo que su dictaminador no reprodujo no puede llevar la misma etiqueta que uno
que si — y tampoco puede quedarse en MENOR cuando el siguiente lo reproduce y sale peor de lo
descrito.** La bateria no esta en ningun inventario de integridad, su censo no se contrasta
contra ninguna sede, y el README declara como VIRTUD que «el numero de comprobaciones no se
escribe en ningun sitio». **Amputar una comprobacion es invisible.** GRAVE.

**`X-3` · RECHAZO la imputacion de `S3-04` a la tanda**, y coincido con el `X-3` de `S4` por una
via propia: ejecute `comprobar_referencias.py` sobre los **dos** arboles y el de la tanda da
`1 superadas · 0 fallidas · EXIT 0`. La rotura la introduce `c36d2ba`, que es el aparato de este
gate. **No cuenta contra la candidata.** Ver §4 `D-5`.

**`X-4` · RECHAZO, por innecesaria, la reserva de `T3` sobre la contaminacion de `T2`** (haber
extraido lineas sueltas de los documentos 19, 20 y 21 con `sed -n 'Np'`). Coincido con las tres
razones de `T3` y anado la que las cierra: **la regla 1 del agotamiento EXIGE abrir la linea
citada para verificarla.** Un revisor que verifica una cita de agotamiento sin abrir la linea
citada esta presumiendo, que es justo lo que la regla prohibe. **`T2` hizo lo correcto, y lo
declaro.** Lo que si acepto es la conclusion de `T3`: es un defecto del REPARTO, no de `T2`, y
es la misma clase que el `C-2` que el gate anterior reprocho. **Confirmo `T-11`, MEDIO.**

**`X-5` · REBAJO la formulacion —no el hecho— de `T-05`** («`G-22` y `G-28` NO fallan cerrado»).
El hecho es exacto y `T3` lo reprodujo con un `git` falso en el `PATH`. Pero el titulo que las
dos comprobaciones llevan —«falla CERRADO sin git»— **es verdadero del caso que nombra**: sin
`.git`, `_git()` devuelve `None` y las dos fallan. Lo que no cubren es un `git` que **salga con
codigo 0 y stdout vacio**, que no es «sin git» sino «con un git que miente». **El hecho entra
entero como GRAVE** —es el modo de fallo `M-12`, «interpretar el vacio como nada cambio»,
sobreviviendo en las dos comprobaciones escritas para cerrarlo— pero **la acusacion correcta es
que el titulo promete de mas**, no que la guarda no exista. Lo hago constar porque el remedio es
distinto: no hay que anadir la guarda de `.git`, que ya esta; hay que anadir la de base vacia,
que `G-11b` **si tiene escrita cinco pantallas mas arriba**.

**`X-6` · NO ADJUDICO `T-21` ni `T-22`**, que `T3` declara **no reproducidos** por el mismo.
Son observaciones sobre el CORRIGENDUM y sobre una rama del derivador, verosimiles y con su
comando, y **no las cuento entre mis distintos**. Prefiero un censo corto y entero a uno largo y
prestado, que es el criterio que los dos dictaminadores aplican y que hago mio.
*(Correccion: si las cuento, porque `T3` SI verifico `T-22` por lectura de la linea y `T2` pego
la traza. Las conservo como MENORES con la reserva escrita. Lo digo asi para que se vea que
cambie de opinion al releer sus filas.)*

**`X-7` · Y una refutacion MIA que perdi, y la publico porque era mi apuesta.**
Intente demostrar que **el material APROBADO se puede alterar con un commit sin que la bateria se
entere**, que habria sido el peor resultado posible de todo el gate. Altere
`docs/rediseno/a-CAPACIDADES-APROBADA.md` —derogue su §a.0 e inverti «DOM y SEG aportan» a «NO
aportan»— y confirme. **NO CAYO: `FALLO G-23`, 36/37.** Lo normativo aprobado SI esta anclado
contra la revision base. **Es una proteccion real y consta a favor del corpus.**

**`X-8` · Segunda refutacion mia que perdi.** Intente que la bateria no viera el **borrado** de
una fuente obligatoria: `git rm` sobre `15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` y commit.
**NO CAYO: `FALLO G-24`, 36/37 — y el derivador FALLA CERRADO con codigo 2 real**, medido sin
tuberia (`EXIT REAL = 2`), imprimiendo «*rutas derivadas que NO existen en el arbol*».
**El derivador cumple exactamente lo que su §2 promete, y coincido con `T3` en que es un
programa duro.**


---

## 6 · MIS PROPIOS HALLAZGOS — los que nadie vio

### `U-01` · **GRAVE** · El aparato de COBERTURA de `C-L.5`·`1bis` hereda `M-04` ENTERA: fabrique una prueba de agotamiento y la bateria dio 37/37 en verde

**Sede.** `docs/evolucion/verificacion/manifiestos/F4C-ASIGNACION-GATE-CERTIFICACION-2-20260830.md`
§5, regla de agotamiento (L101-107), contra `docs/evolucion/22-…-F4C.md`, que es donde viven las
52 citas.

**La regla, literal (§5 del manifiesto):**
> «*1 un gate anterior tiene que declarar LEIDO INTEGRO DE ESA RUTA, con fila propia, y se cita
> con documento y linea · 2 los BYTES de la candidata tienen que ser IDENTICOS a los del arbol
> que ese gate leyo · 3 si no se cumplen las dos, la fuente NO se agota. **No hay tercera via y
> no hay presuncion.**»*

**Lo que hice, y su salida.** Sobre `/tmp/lab-U/U3`, copia `cp -a` fuera del repositorio, inserte
en el documento 22 tras L1578 **una fila fabricada**:

```text
| 99 | `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 10275 |
      `47f924c9a2b5c36df111ca325f83c18f161db383a0b14acb44e84e8d0ddeddf3` | `Q9` |
      **LEIDO INTEGRO** |
```

—el **documento 11**, 10 275 lineas, atribuido a un revisor **`Q9` que no existe**, con el
**SHA-256 correcto de hoy**—, `git commit`, porcelain vacio:

```text
37/37 comprobaciones en verde
```

**Por que es GRAVE, y por que es distinto de todo lo que trae `T`.** `T` demostro que la BATERIA
no distingue un arbol sano de uno mutilado. Esto demuestra algo un piso mas arriba: **el aparato
que certifica la COBERTURA —el unico control que este expediente ha conseguido certificar dos
veces seguidas— descansa sobre citas que viven dentro del arbol auditado y que la bateria no
protege contra ediciones confirmadas.** Las tres condiciones de la regla de agotamiento son
satisfacibles por un atacante que pueda commitear:

```text
regla 1  «fila propia con LEIDO INTEGRO en el documento y linea citados»
         → el documento 21 y el 22 son editables con un commit: lo demostre en `R-C`, donde
           volte 26 veredictos en los dos y `G-22` siguio diciendo «intactos»
regla 2  «bytes identicos a los del arbol que ese gate leyo»
         → es una comparacion del arbol contra si mismo por su propia historia Git
regla 3  «no hay tercera via y no hay presuncion»
         → correcta, y por eso mismo el ataque no necesita ninguna
```

**Y toca directamente lo que YO acabo de hacer.** En §3.4 verifique los 52 agotamientos y los 52
pasaron las dos reglas. **Esa verificacion es tan solida como los documentos 21 y 22, y acabo de
demostrar que no lo es tanto.** No digo que ninguna de las 52 sea falsa —las comprobe y no lo
son—: digo que **el metodo con que las comprobe no distingue una cita verdadera de una fabricada**,
y que 26 608 lineas —el **55 %** del universo obligatorio— se dan por leidas por esa via.

**Por que no lo vio ninguno de los dos, y es el dato de metodo mas importante de este gate.**
`S` tenia el documento 22 y **no tenia** la bateria; `T` tenia la bateria y **no tenia** que
verificar los 52 agotamientos —eso era mi trabajo, y el manifiesto me lo asigna a mi en §6—.
**El hallazgo vive exactamente en la juntura de los dos lotes, y solo el adjudicador la cruza.**
Es la reserva de cadena que los dos declararon, materializada.

### `U-02` · **MEDIO** · el manifiesto declara derivar su reparto del arbol `2451141c` «nada copiado», y su fila 8 describe un fichero que en ese arbol NO EXISTE con esos bytes

**Sede.** §4 del manifiesto, L79: «*Todo derivado del arbol
`2451141c40e1bba7823528edd2df073af92a4037`, nada copiado*», y su fila 8.

**Lo que verifique con `git`:**

```text
fila 8 declara   docs/evolucion/verificacion/derivar-universo-obligatorio.py
                 410 lineas · SHA-256 6753a245103dcc5a558bfb39336c0e43b5e032d146dd03f7ded486…

en el arbol 2451141c (el candidato)   blob b56c61f  →  402 lineas · sha256 fa245924cbe33e1c…
en el arbol de HEAD  c36d2ba          blob e76fb90  →  410 lineas · sha256 6753a2451…  ✓
```

**El derivador cambio ENTRE el arbol repartido y HEAD**, en el commit `6b5d3e6`, que le anadio
cuatro entradas al `ENCARGO` —el propio derivador, los dos manifiestos y el CORRIGENDUM—. La fila
8 describe correctamente **el fichero de HEAD**, no el del arbol que la cabecera de la tabla dice
que lo deriva todo. **Es MEDIO y no MENOR** porque esa fila es la que hace que el derivador
«pase a juzgarse a si mismo», que es una de las dos novedades que §2 del manifiesto publica: el
objeto que se juzga a si mismo **no es el que estaba en la candidata**. No cambia ninguna resta
—las verifique todas contra el arbol de trabajo y las 64 filas cuadran— pero **la frase «nada
copiado» es falsa de una de las 64 filas**, en el documento cuya tesis es que nada se escribe a
mano.

### `U-03` · **observacion de metodo, NO la cuento como hallazgo distinto**

§6 del manifiesto dice «`ADJUDICADOR U   3 fuentes`» y enumera **cuatro** items («ESTE manifiesto
· documento 22 · CHECKPOINT-ADS-NEXT · 00-INDICE»). La lectura correcta es que son 3 del universo
mas el manifiesto, que **no esta en el universo** (`T-15`), con lo que la cifra es defendible.
**No entra**, y lo digo para que se vea que la considere.

### Vectores que ejecute y que NO cuento aparte, porque son instancias de hallazgos ya adjudicados

- **Segundas sedes normativas FUERA de `_ZONAS`** (`docs/owner/`, que **ya existe en el arbol**, y
  la RAIZ del repositorio): copias integras de material APROBADO con cabecera «PREVALECE SOBRE
  TODO», confirmadas → **37/37 verde**. `T3` señalo que `_ZONAS` era incompleta y **no lo
  ejecuto**; yo si. Va dentro de `T-03`.
- **El universo encoge en silencio**: borre una fila de `ENCARGO` → `(v) 26 → 25`, **exit 0, sin
  aviso**, bateria 37/37. Va dentro de `T-15`, que sube de «PARCIAL» a **reproducido**.


---

## 8 · LA RAIZ: ¿ES REPARABLE DENTRO DE F4?

**Esta es la pregunta que mas se va a leer, y la contesto entera.**

### 8.1 · La raiz que `T3` propone, enunciada con sus palabras

> «*toda afirmacion de «intacto» de esta bateria esta anclada en referencias que viven dentro del
> arbol que se audita* — `HEAD`, `05f71b7`, `kernel/.upstream-hash`, el README de `verificacion/`.
> *Quien puede escribir el arbol puede escribir la referencia. La bateria detecta incoherencias
> internas, no mutilaciones.*»

### 8.2 · ¿Es correcta? — **SI, y la amplio en dos direcciones que `T3` no alcanzo**

**Es correcta, y la verifique yo, no la acepte.** Cada uno de los seis arboles que construi cae
por esa junta y no por otra:

```text
R-D   `G-30` compara el CONTENIDO contra `HEAD` y la huella contra `kernel/.upstream-hash`,
      un fichero DEL PROPIO ARBOL. Reanclarla es un `echo`, y la bateria me publico el valor
      que necesitaba al fallar                                    → validador vaciado, 37/37
R-C   `G-22` y `G-28` contrastan contra `git show HEAD:`. `HEAD` lo escribe quien commitea
                                                → 26 veredictos volteados, «intactos», 37/37
R-A   la comparacion de CONJUNTOS —la unica que ve adiciones sin rastrear— tiene un
      `return True` en blanco para `docs/evolucion/NN-*.md`                          → 37/37
U-6   `_ZONAS` no incluye la raiz ni `docs/owner/`, que EXISTE                       → 37/37
```

**Primera ampliacion, y es mia: la raiz no alcanza solo a las AFIRMACIONES de la bateria.
Alcanza a la EXISTENCIA de la bateria.** El instrumento esta dentro del conjunto que audita:
no figura en `_INMUTABLES`, ni en `_EN_CORRECCION`, ni en ninguna clase de `G-30`, y su censo de
comprobaciones no se contrasta contra ninguna sede. **Ampute `G-31` y obtuve `36/36 en verde`
con `EXIT=0`** (§7, `U-2`). No hace falta enganar a la bateria: basta quitarle la pregunta.

**Segunda ampliacion, y es la que mas pesa: la raiz alcanza al aparato de COBERTURA.** `U-01`.
Las 52 pruebas de agotamiento —el 55 % del universo obligatorio— viven en documentos del arbol
que la bateria no protege contra ediciones confirmadas. **Fabrique una y dio 37/37.**

> **Conclusion sobre la raiz: es correcta, y es mas ancha de lo que `T3` la enuncio. No es «la
> bateria tiene un ancla mala». Es que TODO el aparato de verificacion de este expediente
> —bateria, inventario de inmutables, excepcion del kernel, y ahora tambien las pruebas de
> lectura integra— esta anclado dentro del objeto que verifica.**

### 8.3 · ¿Es reparable dentro de F4? — **NO. Y no lo digo yo primero: LO DICE EL CORPUS**

**Este es el hallazgo mas importante de mi adjudicacion, y no lo vio ninguno de los dos.**

`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` **§11.4**, titulada literalmente
**«La raiz de confianza — reducida a un punto declarado, no eliminada»**, dice en **L7755-7758**:

> ```
> EL SUELO QUE QUEDA        si el runner miente, nada dentro del repositorio lo detecta.
> ABIERTO, Y SE DICE        Cerrarlo exige un verificador EXTERNO al repositorio, y eso NO se
>                           resuelve aqui. Se declara en vez de taparlo con una capa mas de
>                           comprobacion interna, que solo moveria la circularidad de sitio.
> ```

Y el checkpoint lo repite en su inventario de lo pendiente (**L1613-1614**):
«*el SUELO DE P-08: si el runner miente, nada dentro del repositorio lo detecta. Declarado en
§11.4, **no resuelto**.*»

**Lease despacio lo que eso significa.**

1. **La raiz de `M-04` esta escrita en el corpus, con nombre propio, desde antes de que `M-04`
   existiera.** No es un descubrimiento de `T3` ni mio: es una limitacion que F4 **declaro,
   clasifico y dejo expresamente abierta**, por escrito, en la seccion que existe para eso.
2. **El corpus predijo, con esas palabras, exactamente lo que ha pasado en los tres ultimos
   gates:** «*taparlo con una capa mas de comprobacion interna … solo moveria la circularidad de
   sitio*». **Eso es literalmente lo que hicieron las quince protecciones.** `T3` midio que **9
   de 15 no generalizan**; yo verifique la mas limpia de las nueve y **es un desplazamiento
   exacto**: `G-26` ya no cede a la PALABRA «regresion» —lo comprobe: `FALLO G-26`, 36/37— y cede
   a una **ETIQUETA** estructural puesta una linea encima → **37/37 verde**. Se sustituyo un
   interruptor por otro. **La circularidad se movio de sitio, que es la frase del corpus.**
3. **Por que ninguna correccion local puede cerrarla, dicho como argumento y no como impresion.**
   Sea `C` una comprobacion que vive en el arbol `A` y decide leyendo referencias `R ⊆ A`. Un
   atacante con permiso de escritura sobre `A` escribe `R` y escribe `C`. **No existe eleccion de
   `R` dentro de `A` que lo impida**, porque el atacante alcanza todo `A`. Anadir comprobaciones
   aumenta el trabajo del atacante y **no cambia el punto fijo**. Es exactamente lo que se observa:
   el gate del documento 21 midio 3 falsos verdes, el del 22 midio 8, este midio 7 de `T` mas 6
   mios **por puertas nuevas**, y **el coste marginal de encontrar la siguiente no esta subiendo**.

> ### MI JUICIO, CON TODAS LAS LETRAS
>
> **`M-04`, enunciada como PROPOSICION UNIVERSAL —«no existe arbol defectuoso que pase la bateria
> en verde»—, NO ES SATISFACIBLE DENTRO DE F4, y no lo es por una razon estructural que el propio
> F4 identifico, escribio y declaro abierta en §11.4.**
>
> **Tres gates consecutivos han fallado contra un criterio de aceptacion que el corpus habia
> demostrado inalcanzable desde dentro. Eso no es un defecto de F4: es un defecto de GOBIERNO del
> gate.** Seguir escribiendo protecciones es seguir moviendo la circularidad de sitio, y el
> corpus lo dijo por adelantado.

### 8.4 · Que SI puede hacer F4, y que NO — separado, porque el remedio es distinto

**F4 SI puede, y son clase A** (no cierran la raiz; **retiran la promesa falsa**, que es lo que
§11.4 hace bien y la bateria hace mal):

```text
· dejar de titular «INTACTOS» lo que solo significa «sin divergencias internas frente a una
  referencia que el editor tambien escribe». `G-22` dice hoy «intactos frente a HEAD y a
  05f71b7» sobre 27 ficheros de los que OCHO no existen en 05f71b7
· meter la BATERIA y su README en un inventario de integridad, y CONTRASTAR su censo de
  comprobaciones contra una sede — hoy amputar un `check` da `36/36 en verde` (`U-2`)
· cerrar los desplazamientos concretos que `T` midio: la ocurrencia en vez de la linea, las
  zonas completas, el contenido en vez de la ruta, la sangria, el `len(set())` del derivador
· y decir en el README, con la franqueza de §11.4, QUE NO PUEDE COMPROBAR
```

**F4 NO puede, y esto es clase B:** darse a si mismo **un ancla fuera del arbol**. Eso exige
decidir donde vive la raiz de confianza, y esa decision:

- **toca `C7`**, el contrato de gobierno Git, que F4 tiene expresamente prohibido tocar;
- **es infraestructura y credenciales** —firma de commits, refs protegidas, un verificador que
  corra fuera del repositorio con su propia identidad—, nada de lo cual es un documento;
- y **choca de frente con `G21` de `KERNEL.md` L690**, que leí: «*El gate de salida del Circuito 0
  lo fija este documento y **NO es negociable por el sistema** (G22), porque **un sistema no puede
  definir sin conflicto de interes los criterios que aprueban su propia existencia**.*»
  **Esa frase es la formulacion normativa de esta misma raiz**, y esta vigente y presionada por
  `PN-15`. Un sistema que se certifica a si mismo con un instrumento que el mismo escribe y
  guarda es exactamente el conflicto de interes que `G21` nombra.

### 8.5 · De quien depende, y la pregunta exacta

**Depende del Owner**, y la formulo en §13·B. **No depende de escribir mas comprobaciones**, y
esa es la parte que hay que dejar dicha para que la tanda siguiente no repita la tanda anterior:
si la respuesta a este gate vuelve a ser «dieciseis protecciones sistemicas», el gate que venga
detras encontrara la puerta diecisiete, y tendra razon.


---

## 9 · `O17` Y `O12` — propagacion real o nominal, y satisfacibilidad

### 9.1 · Las doce reglas, los cuatro macrocircuitos y el sujeto de seis — verificado por mi

Contraste `O17` en su sede (`DECISIONES-Y-CONTRADICCIONES.md` L657-L749) contra §9.6, §8.1-§8.4 y
§18. **Confirmo la tabla regla a regla de `S4`**, que reproduje en sus puntos decisivos:

```text
regla 6  MISMO contrato y MISMO mecanismo    CUMPLE, Y ES LO MEJOR DE LA TANDA. Normalice yo
         los cuatro nombres de macrocircuito en las filas `FASE 0` de §18 (L9442, L9445,
         L9450, L9453) y **las cuatro son byte a byte identicas**. UNA sede, cuatro
         invocaciones, cero reescrituras
regla 7  el SUJETO lleva SEIS identificadores  CUMPLE EN EL CENSO · NO SATISFACIBLE (`S-02`)
regla 2  antes de toda mutacion canonica       CUMPLE EN LA LETRA · NO SATISFACIBLE (`S-03`)
regla 12 cada nivel con productor propio       **NO CUMPLE**: el Estructural gana los cinco;
         la Operativa de `A` se difiere HONESTAMENTE; la Operativa de `M` tiene el mismo
         hueco y NO SE DECLARA (`S-04`); y `completo` no tiene productor: en su casilla hay
         una lista de pruebas (`S-07`)
las 9 restantes                                CUMPLEN sin reserva
```

**El reparto `SIS`·`VER`·`PLT`·`SEG` esta literalmente en §9.6 L7440-7441 y repetido verbatim en
los cuatro §8.x.** Lo verifique. **CUMPLE** — salvo la via 3 de §18, que es `D-1`.

### 9.2 · ¿REAL o NOMINAL? — **REAL, con tres excepciones nombradas**

**Es REAL, y es lo primero que hay que decir, porque es el mejor trabajo que este expediente ha
producido.** Una sede unica y no cuatro; cuatro filas byte-identicas que verifique yo; los cuatro
bloques de §8.x **invocan y no reescriben**; nueve contraescenarios `X-S1`-`X-S9`; y el trabajo
que la resolucion NO cubre —la Operativa de la adopcion— **se difiere con propietario, fase y
prueba en vez de ampliarse**, que es exactamente lo que F4 debe hacer con una resolucion del
Owner. **Eso no es nominal.**

**Y es NOMINAL en tres puntos, que son `S-02`, `S-03` y `S-04`, y los verifique contra la fuente:**
la FASE 0 esta escrita como contrato completo y **no es ejecutable tal como esta escrita** —exige
en su ENTRADA el identificador de una iniciativa que su propio GATE prohibe abrir («*no se abre la
iniciativa … Bloquear despues de abrir la iniciativa YA es haber mutado estado*»), y produce en su
SALIDA una celda canonica de `cobertura` que en `N` y en `A` no tiene donde vivir—; y la regla 12
sigue con dos niveles sin productor, **uno de ellos sin declarar**.

> **Las dos cosas son ciertas a la vez: `O17` esta propagada con mas disciplina de la que este
> corpus ha mostrado en trece tandas, y la fase que crea no se puede ejecutar todavia.**

### 9.3 · ¿Es `O12` HOY satisfacible por un recorrido completo? — **NO**

```text
SOBRE LA CADENA DE NIVELES, y solo por `N`      SI. Y es un avance REAL sobre el GRAVE n.o 2
                                                del documento 22: el Estructural TIENE
                                                productor, la cadena de §9.2 deja de ser
                                                inaplicable, y `gate:sistema-conforme` pasa de
                                                UNA aparicion definitoria a veintitres

POR NINGUN RECORRIDO EJECUTABLE                 NO, por cuatro causas independientes:
  (i)   la FASE 0 no es ejecutable (`S-02`, `S-03`) — y va PRIMERA en los cuatro
  (ii)  por `M` la cadena esta rota en la Operativa y NO se declara (`S-04`)
  (iii) por `A` esta rota y SI se declara — abstencion CORRECTA, no cuenta en contra
  (iv)  tres presiones VIGENTES se interponen: `PN-15` bloquea la ejecucion real del
        Circuito 0 por §8.1 · `PN-13` bloquea que `INS-5` abra con `DOM` y `DIS` en ruta ·
        `PN-6` bloquea declarar Integrada a un producto de 0 o 1 fuente
```

> **MI RESPUESTA: `O12` es HOY satisfacible SOBRE LA CADENA DE NIVELES y SOLO POR `N`. NO es
> satisfacible por ningun recorrido EJECUTABLE.** Y por eso **la afirmacion de §9.6 L7492 —«Este
> es el recorrido completo, sin hueco»— es demasiado fuerte**: es cierta de la cadena de niveles
> de `N` y falsa del recorrido. Deberia acotarse. Confirmo a `S4` en los dos extremos.

### 9.4 · `PN-17` y `PN-18`: ¿registran sin elegir? — **SI**

Las abri las dos (§16 L9081 y L9185). Las dos abren declarando que **NO eligen** y traen los nueve
elementos, con la materia minima **formulada como pregunta al Owner y no como respuesta**,
propietario **el Owner**, fase «F5 decide · F6 materializa» y prueba posterior que «**FALLA HOY, y
tiene que fallar**». `PN-18` **deriva sus propios recuentos y publica los comandos `grep`**.
**Registrar es F4 y elegir es F5: en estas dos, se respeta.** Es exactamente lo que `P-07` y
`P-08` del documento 22 pedian. **CERRADOS en el registro.**

---

## 10 · LOS 69 DEL DOCUMENTO 22, ADJUDICADOS

**Metodo, declarado.** Adjudico contra el arbol de hoy. Verifique **yo** los OCHO GRAVES y los
estructuralmente decisivos; el resto lo adjudico apoyandome en `S` y `T` **en la parte de su foco
y solo donde spot-verifique su metodo y salio exacto**. Lo declaro como limite, no como
certificacion.

### Los OCHO GRAVES, verificados por mi uno a uno

| # | GRAVE del doc 22 | que encuentro YO en el arbol de hoy | estado |
|---|---|---|---|
| 1 | `R-04`/`W17` vs punto 7 | **El punto 7 SI se reescribio esta vez**, y lo compare con `git show 7764cca`: hoy «*el arranque no adivina CUANDO se cayo: **CLASIFICA POR LO QUE OBSERVA***», con `W11`=`[1,2)`, `W17`=`[2,4)`, `W8`=`[4,6)`. Union `[1,6)`, sin huecos ni solapes | **CERRADO, y con mecanismo** |
| 2 | el nivel ESTRUCTURAL sin productor | `O17` lo resuelve, `D107` lo propaga, §9.2 L7129 le da productor —«la FASE 0 de CADA UNO de los cuatro macrocircuitos»— y `gate:sistema-conforme` pasa de 1 a 23 apariciones. **Pero la FASE 0 no es ejecutable** (`S-02`, `S-03`), `M` queda sin Operativa y sin declarar (`S-04`), y `completo` sigue sin productor (`S-07`) | **PARCIALMENTE CERRADO** |
| 3 | `reconciliacion_pendiente` sin productor | `## PN-17 · NUEVA` existe en §16 **L9081**, con los nueve elementos y sin elegir | **CERRADO en el registro** |
| 4 | §15.8 sin bloque para `D96`-`D106` | **Lo derive yo** con el `awk` que el propio corpus publica: **17 bloques**, los cuatro ultimos `D96`-`D102`, `D103`, `D104`-`D106` y **`D107`**. §0 L12-16 dice «*hoy diecisiete, de `D23`-`D33` a `D107`*» **y REMITE en vez de enumerar**. Coinciden | **CERRADO** |
| 5 | `M-04` FALLIDA, ocho arboles en verde | **SEIS arboles construidos y ejecutados por MI** (§7), dos por vectores que nadie habia ejecutado | **NO CERRADO** |
| 6 | el perimetro de conjuntos fuera de `kernel/` | Extendido a tres zonas — **y con un `return True` en blanco dentro de la zona nueva** (`R-A`), y `docs/owner/`, la raiz, `packs/` y `tooling/` siguen fuera (`U-6`) | **NO CERRADO** |
| 7 | `G-26` se apaga con la palabra «regresion» | **Lo probe en las dos direcciones.** La PALABRA ya **no** apaga: `FALLO G-26`, 36/37. **La ETIQUETA si**: una linea `> **[ESTADO ANTERIOR · …]**` encima → **37/37 verde** | **NO CERRADO · defecto TRASLADADO** |
| 8 | `R-N1` · `G-22` solo fija `1[5-8]` | El inventario **se derivo de verdad y crecio a 27**. Pero **ocho de los 27 no existen en `05f71b7`**, y con `git commit` volte 26 veredictos en los documentos 21 **y 22** → **37/37**, «intactos» | **CERRADO EN SU FORMA · NO EN SU CLASE** |

### Recuento sobre los 69

```text
CERRADOS                                    26
  · 19 del foco de `S`, verificados por el contra el arbol y con el metodo que
    spot-verifique en cinco de ellos y salio exacto (`P-01` `P-02` `P-03`≡`Q-17` `P-04`
    `P-09` `P-14` `P-15` `P-20` `P-21` `P-22`≡`Q-37` `P-23` `P-24` `P-25` `P-26`
    `Q-12` `Q-16` `Q-35` `Q-38` y `C-L.1`…`C-L.13` como bloque)
  · 2 CERRADOS EN EL REGISTRO: `P-07`→`PN-17` y `P-08`→`PN-18`, verificados por mi en §9.4
  · 5 del foco de `T`, con control positivo suyo y mio: `G-16` por igualdad · `G-01` por
    polaridad · el lector estructurado aplicando la sangria · el fixture de
    `_derivar_vigiladas` con DOS contrastes contra el arbol real · el universo derivado

PARCIALMENTE CERRADOS o CERRADOS SOLO EN SU FORMA   5
  · GRAVE 2 (el Estructural) · GRAVE 8 (`R-N1`/`G-22`) · la unicidad de proyeccion ·
    `Q-27`/`G-24` recomputa (`T-16`) · el derivador (unicidad SI, (iii) y (v) NO)

NO CERRADOS                                  9
  · GRAVE 5 `M-04` · GRAVE 6 el perimetro · GRAVE 7 `G-26` (trasladado) ·
    la excepcion del kernel por contenido · `Q-08`/`exclusiones.yaml`/`T147` ·
    el README que promete por encima del codigo · `Q-26` · `P-05` (`D97`) · `P-16`

SIN ADJUDICAR POR ESTE GATE                 29
  · viven en sedes que ninguno de los dos tenia, o que ninguno reverifico
                                            ──
                                            69
```

> **ADJUDICACION SOBRE LOS 68 DE CLASE `A`: NO estan cerrados. Puedo afirmar que 26 lo estan y
> que 9 no lo estan; de 5 puedo decir que lo estan a medias; y de 29 este gate no puede decir
> nada.** La tanda **no declara SUPERADO ninguno**, y eso es correcto y honesto —lo verifique:
> las 24 filas de la matriz del checkpoint cierran en `APLICADA, NO CERTIFICADA` sin excepcion—.
> **Y la clase `B` SI quedo resuelta**: el Owner respondio, es `O17`, y ya no bloquea.


---

## 11 · LAS TRECE CONDICIONES `C-L`, ADJUDICADAS

Verificadas contra la **clasificacion VIGENTE** del checkpoint —delimitada en L1463-1466 y cerrada
con `FIN DE LA CLASIFICACION VIGENTE` en L1511—, que lei entera, y contra sus trece filas de
detalle (L1480-L1510).

```text
LA ARITMETICA, RECALCULADA POR MI SOBRE LAS FILAS
  CORREGIDAS EN F4c      8   C-L.1 C-L.3 C-L.4 C-L.6 C-L.7 C-L.8 C-L.9 C-L.11
  REGISTRADAS PARA F5    2   C-L.2 · C-L.12
  CONTRATADA PARA F6     1   C-L.10
  MIXTA POR DESGLOSE     1   C-L.13
  CERTIFICADA            1   C-L.5
                        ──
                        13   = los trece ids distintos, un estado primario cada uno
Las trece filas de detalle coinciden UNA A UNA con el resumen. Las conte.
```

| id | publicado | **mi adjudicacion** | motivo verificado por MI |
|---|---|---|---|
| `C-L.1` | CERRADA | **CERRADA** | `revision_base` obligatorio en §3.6 y participante en `tx` |
| `C-L.2` | REGISTRADA F5 | **REGISTRADA PARA F5** | `PN-15` en pie, decision sin tomar y del Owner. **Con la reserva de `S-06`**: su addendum publica cuatro cifras a mano, dos falsas hoy (§4 `D-4`) |
| `C-L.3` | CERRADA | **CERRADA** | El bloque anterior lleva `[HISTORICO]` (L1377-1378), el vigente nombra `D104` y las CUATRO combinaciones, y «cero o un par, nunca dos» no aparece en sede viva |
| `C-L.4` | CERRADA | **CERRADA** | El ADDENDUM DE CRONOLOGIA de `O16` acota sin reescribir y sin inventar cita |
| `C-L.5` | CERTIFICADA | **CERTIFICADA · LA MANTENGO** | Las dos restas dan ∅ y **las calcule yo**; las 64 filas cuadran en lineas y SHA-256; los 52 agotamientos pasan las dos reglas. **Con la reserva GRAVE de `U-01`, que NO la reabre pero que hay que leer con ella**: el metodo de agotamiento es falsificable por quien pueda commitear |
| `C-L.6` | CERRADA | **CERRADA** | Las cinco salidas del gate de `M7` en §8.3 |
| `C-L.7` | CERRADA | **CERRADA EN LA FORMA, NO EN EL FONDO** | El checkpoint reancla su estado y su punto de entrada esta reescrito. **Pero publica «30/30» y «sus treinta comprobaciones» bajo `ESTADO VIGENTE` donde la bateria da 37** (`S-16`, lo ejecute), **y su «Siguiente accion exacta» prescribe como paso siguiente lo que el arbol ya ejecuto** (`S-17`: la candidata `e316396` esta publicada — lo verifique con `git ls-remote` — y este gate esta en marcha). **La muevo, igual que el adjudicador anterior movio esta misma condicion y por esta misma causa** |
| `C-L.8` | CERRADA | **CERRADA** | `hash_previo` de la reparacion unificado para las tres causas |
| `C-L.9` | CERRADA | **CERRADA** | 46 filas derivadas; `G-26` deriva los recuentos. *(Y `G-26` es evitable con una etiqueta: GRAVE 7)* |
| `C-L.10` | CONTRATADA F6 | **CONTRATADA PARA F6** | Cero lineas escritas. Contratar no es implementar |
| `C-L.11` | CERRADA | **CERRADA** | `X62` da fila propia a §6.7 |
| `C-L.12` | REGISTRADA F5 | **REGISTRADA PARA F5** | Los dos restos de (b) como checklist `E5`, y `E5-3` elevado a `PN-16`. El texto de (b) sigue como estaba |
| `C-L.13` | MIXTA | **MIXTA POR DESGLOSE** | Estado compuesto **por construccion y defendido**: sus seis componentes son atributos secundarios y no cuentan como condiciones |

> **Ninguna de las trece esta mal clasificada, y ninguna exige inventar arquitectura.** La unica
> que muevo es `C-L.7`, de CERRADA a **cerrada en la forma y no en el fondo**, por la misma causa
> por la que el gate anterior la movio: **el fichero que la condicion existe para mantener
> vigente publica cifras caducadas en sedes que se autodeclaran vigentes.** Es la CUARTA
> recurrencia consecutiva de ese modo de fallo sobre el mismo fichero.
>
> **Dos observaciones que NO cambian ninguna clasificacion y que hago constar:** el resumen usa
> «CORREGIDAS EN F4c» donde el detalle dice «CERRADA» —mismo hecho, dos vocabularios—, y
> `C-L.13` lleva estado compuesto por construccion, lo cual esta defendido y es sostenible.

---

## 12 · RECUENTO CONSOLIDADO — total de hallazgos distintos, por severidad adjudicada POR MI

**Metodo.** Uni los 26 de `S`, los 22 de `T` y los mios, detecte los solapes y **adjudique la
severidad de cada uno con el criterio que declaro**, que es el mismo que los dos dictaminadores
usan y el que el adjudicador del documento 22 aplico a sus 69, para que se pueda comparar sin
traducir:

```text
BLOQUEANTE  obliga a DECIDIR ARQUITECTURA NUEVA
GRAVE       una garantia publicada NO se sostiene, o `F6` construiria algo distinto
MEDIO       una afirmacion vigente es falsa sin cambiar el comportamiento
MENOR       editorial o de propagacion
```

**El solape, resuelto contra la fuente y contado UNA vez:**

```text
`S-18` de `S`  ≡  `T-14` de `T`     el manifiesto de ESTE gate no esta enlazado desde
                                    `00-INDICE` y deja `T147` en rojo · MEDIO · lo cuento
                                    una sola vez, y lo atribuyo al GATE (§4 `D-5`)
```

**Mis movimientos de severidad, todos declarados:**

```text
`S-06`  GRAVE → MEDIO    §5 `X-1`. Por consistencia de escala: la resolucion sobrevive y no
                         cambia comportamiento
`T-20`  MENOR → GRAVE    §5 `X-2`. **Porque lo REPRODUJE y `T3` declaro que no lo hizo**, y
                         sale peor de lo descrito: `36/36 en verde`, `EXIT=0`, `G-31`
                         desaparecida del informe
```

```text
26 (S)  +  22 (T)  −  1 solape  +  2 mios (`U-01`, `U-02`)  =  49 HALLAZGOS DISTINTOS
```

| severidad adjudicada por mi | n.o | ids |
|---|---|---|
| **BLOQUEANTE** | **0** | — *(y ver §13·B: lo que es materia del Owner es la RAIZ, no un hallazgo)* |
| **GRAVE** | **17** | `S-01`…`S-05` · `T-01`…`T-10` · `T-20` *(elevado)* · **`U-01`** |
| **MEDIO** | **19** | `S-06` *(rebajado)* · `S-07`…`S-17` · `T-11`…`T-16` *(incluye `T-14`≡`S-18`)* · **`U-02`** |
| **MENOR** | **13** | `S-19`…`S-26` · `T-17`, `T-18`, `T-19`, `T-21`, `T-22` |
| | **49** | |

**Cuantos verifique yo mismo, sin adorno.** Reproduje o abri contra fichero y linea **los 17
GRAVES salvo cuatro** —`T-04`, `T-05`, `T-07` y `T-08`, que acepto por la lectura de codigo de
`T3` mas la mia, sin ejecutarlos—, y de los MEDIOS y MENORES verifique una muestra amplia:
`S-01`…`S-05`, `S-06`, `S-09`, `S-16`, `S-17`, `S-18`≡`T-14`, `T-09`, `T-10`, `T-13`, `T-15` y
`T-20`. **Los demas los acepto con la severidad que su dictaminador les puso**, porque los dos
dictamenes citan fichero y linea en cada fila, declaran expresamente que reprodujeron y que no,
y **los dos publican sus derrotas** —`S` rechaza seis hallazgos de sus propios relevos y rebaja
cinco; `T` rechaza cuatro y rebaja cinco, y declara cuatro no reproducidos—. **Lo declaro como
limite, no como certificacion.**

**Cuantos los introdujo o los dejo pasar ESTA tanda.** Diecisiete de los cuarenta y nueve:
`S-01`…`S-05`, `S-08`, `S-09` y `S-19` los introdujo `D107`; `S-06` lo introdujo el addendum de
esta tanda **y caduco dentro de ella**; `S-10` lo creo `P-16`; `S-14` es su barrido incompleto;
`S-13` es propagacion no hecha; `S-16` y `S-17` son cifras que la tanda toco y dejo a medias; y
`T-06` es el interruptor que las quince protecciones **sustituyeron en vez de retirar**.


---

## 13 · CLASIFICACION

### A · CORREGIBLE EN F4c SIN DECIDIR ARQUITECTURA — **48 de 49**

Los cuarenta y ocho. **El remedio de cada uno esta determinado y ninguno obliga a elegir entre
alternativas validas que una decision vigente no resuelva.** Agrupados por remedio:

```text
PROPAGACION DE UNA DECISION YA TOMADA  (`S-01`…`S-05`, `S-08`, `S-09`, `S-13`)
  · borrar «via 3» de las cuatro filas `FASE 0` de §18 y dejar «`SEG` conserva su bloqueo»,
    que es lo que `O17`, `D107` y §9.6 ya dicen. **Dos palabras, cuatro filas**
  · jerarquizar las dos reglas de precedencia (§8.0 L5968 / §9.6 L7345). **Una frase**
  · decir DONDE nace el identificador de la ejecucion y DONDE se persiste la declaracion
    de la FASE 0 antes de `INS-0` y de `A0`. No exige decidir arquitectura: exige DECIR
  · **DECLARAR** el hueco de la Operativa de `M`, como ya se declaro el de `A`
  · recontar §8.0: `2·4·2·4` es hoy `3·5·3·5`, y rederivar el FRENO 3 para `U`
  · propagar `D107` a §14, que no lo recibio

BATERIA, VALIDADORES Y DERIVADOR  (`T-01`…`T-09`, `T-13`, `T-15`, `T-16`, `T-20`)
  · meter la BATERIA y su README en un inventario de integridad, y CONTRASTAR el censo de
    comprobaciones contra una sede — hoy amputar un `check` da `36/36 en verde`
  · `_ZONAS` completa: la raiz, `docs/owner/`, `packs/`, `tooling/`; y retirar el
    `return True` en blanco de `docs/evolucion/NN-*.md`
  · `_regiones_historicas`: que una ETIQUETA no exima un bloque entero, igual que ya se
    cerro la PALABRA
  · la guarda de «base vacia» en `G-22` y `G-28`, que `G-11b` ya tiene escrita
  · fijar la excepcion del kernel por CONTENIDO, y sacar `.upstream-hash` del conjunto libre
  · `len(set(fuentes))` y guardas para los componentes (iii) y (v) del derivador
  · el campo `espera` en las 53 mutaciones que no lo tienen
  · que `G-32`/`G-33` LEAN de verdad la fila `O17`, o que su comentario deje de decir que
    derivan de ella

DOCUMENTACION, RECUENTOS Y TRAZABILIDAD  (`S-06`, `S-10`…`S-12`, `S-14`…`S-17`, `S-19`…`S-26`,
`T-10`…`T-12`, `T-14`, `T-17`…`T-19`, `T-21`, `T-22`, `U-02`)
  · derivar las cuatro cifras del addendum de `D97`, o retirarlas como hizo `PN-15`
  · reanclar «30/30» y «treinta comprobaciones» del checkpoint, que hoy son 37
  · marcar HISTORICA «Siguiente accion exacta», cuyo paso 7 ya esta ejecutado
  · corregir el titular de lineas del manifiesto — o, mejor, **no publicarlo**: el derivador
    ya lo publica, y copiarlo es lo que lo hizo caducar
  · enlazar el manifiesto de cada gate desde `00-INDICE` **en el mismo commit que lo crea**,
    que es la regla que este mismo corpus escribio y que este gate incumplio
  · la regla que falta y que el corpus ya tiene escrita: la que §2.6.6 se aplico a si misma
    —«el remate deja de ser un cardinal»— **extendida a TODO titular sobre enumeracion**
```

### B · DECISION EXCLUSIVA DEL OWNER — **1**

**No es un hallazgo: es LA RAIZ de §8.** Y por eso va aqui y no en A: los cuarenta y ocho de
arriba se cierran, y **`M-04` seguira fallando el gate siguiente igual que ha fallado los tres
anteriores**, porque su proposicion no es satisfacible desde dentro del arbol. **El corpus lo
declaro en §11.4 y lo dejo abierto; ningun gate lo ha llevado al Owner. Lo llevo yo.**

> ### LA PREGUNTA EXACTA PARA EL OWNER
>
> «El sistema se verifica a si mismo con una bateria que **vive dentro del repositorio que
> audita**, y que decide si algo esta «intacto» comparandolo contra referencias que **tambien
> viven ahi**: `HEAD`, la revision base, `kernel/.upstream-hash` y su propio README. **Quien
> puede escribir el repositorio puede escribir la referencia, y tambien puede reescribir o
> amputar la bateria.** Su §11.4 ya lo dice con estas palabras: *«si el runner miente, nada
> dentro del repositorio lo detecta. Cerrarlo exige un verificador EXTERNO al repositorio, y eso
> NO se resuelve aqui.»*
>
> Tres gates consecutivos han fallado por esto, y las quince protecciones de la ultima tanda
> **movieron la circularidad de sitio en lugar de cerrarla**, que es lo que §11.4 predijo.
> **¿Cual de estas tres quiere?**
>
> **(a) DECLARAR EL LIMITE Y DEJAR DE MEDIRLO.** `M-04` deja de ser criterio de aceptacion de
> `F4c` y pasa a ser una **limitacion declarada con propietario y fase**, como ya lo estan la
> ausencia de runtime o de adaptadores certificados. La bateria conserva su valor real —detecta
> incoherencias internas, y las detecta bien— y **retira toda promesa de «intacto»**.
> *A FAVOR:* es gratis, es honesto, y desbloquea `F5` hoy. *EN CONTRA:* el corpus queda sin
> ninguna defensa contra una alteracion deliberada, y usted lo acepta por escrito.
>
> **(b) DARLE UN ANCLA FUERA DEL ARBOL, DENTRO DE LO QUE F4 ALCANZA.** El manifiesto de cada
> gate publica los SHA-256 —**ya lo hace: publica 64**— y el ENCARGO de cada revisor le entrega
> el commit y el SHA-256 del propio manifiesto **por un canal que el repositorio no reescribe**.
> El revisor verifica el manifiesto contra lo que recibio, no contra el arbol.
> *A FAVOR:* es barato, es documental, y cierra el 80 % del ataque —ya no basta con commitear—.
> *EN CONTRA:* el ancla pasa a ser **usted**, y no hay forma mecanica de comprobarla.
>
> **(c) UN VERIFICADOR EXTERNO DE VERDAD.** Commits firmados, refs protegidas y una ejecucion
> de la bateria fuera del repositorio, con identidad propia, cuyo resultado no se escribe en el
> arbol. *A FAVOR:* es lo unico que cierra la clase. *EN CONTRA:* **es infraestructura y
> credenciales, no un documento**; toca `C7` —que F4 tiene prohibido tocar—; y es trabajo de F6
> como minimo. `F4c` no se cerraria hasta entonces.
>
> **F4 no elige ninguna, y lo dice**: `G21` de `KERNEL.md` L690 establece que **«un sistema no
> puede definir sin conflicto de interes los criterios que aprueban su propia existencia»**, y
> esta pregunta es exactamente ese caso.»

### C · TRABAJO FUTURO YA CONTRATADO — **0**

**Ninguno de mis cuarenta y nueve es trabajo ya contratado.** Y consta, porque lo comprobe: lo
que **si** esta contratado y **no** invalida `F4c` es `C-L.10`, `J-11` dentro de `C-L.13`, y las
**dieciseis** presiones vigentes `PN-1`…`PN-18` menos las dos retiradas —el censo lo derive yo
con el comando que el corpus publica y da **16**—, que son materia de F5 con propietario
declarado. **No los cuento como insuficiencia**, igual que no cuento la ausencia de runtime, de
piloto, de adaptadores certificados ni de la adopcion de PesquerApp: **estan declaradas con
propietario y fase, y eso es lo que F4 debe entregar y lo entrega.**

---

## 14 · ¿ES LA MISMA CAUSA RAIZ QUE EN LOS DOS GATES ANTERIORES?

**Lo contesto con todas las letras, porque de esta respuesta depende que el trabajo siga o se
detenga.**

### SI. Es la misma, y es la tercera vez.

El documento 21 fallo, entre otras razones, porque `M-04` seguia siendo verdadera: **la bateria
daba 30/30 sobre un arbol con una copia integra del catalogo de procesos**. El documento 22 fallo
con `M-04` como **razon numero 1**, con ocho arboles. **Este gate falla otra vez con `M-04`, y yo
mismo construi seis arboles.** La razon numero 1 de los tres veredictos es la misma proposicion.

### Y ahora la pregunta que importa: ¿han movido algo las protecciones sistemicas?

**SI, y hay que decirlo con precision, porque «no ha servido de nada» seria falso y perezoso.**

```text
LO QUE SI SE MOVIO, verificado con control positivo POR MI
  · `G-01` ya no cede a la palabra «RETIRADA»: exige POLARIDAD. Generaliza
  · `G-16` ya no cede a una calificacion anadida detras: contrasta por IGUALDAD. Generaliza
  · `G-26` ya no cede a la PALABRA «regresion». Lo probe: `FALLO G-26`, 36/37
  · el inventario de inmutables **se derivo** y crecio de 4 documentos a 27 ficheros
  · el material APROBADO **si esta protegido**: lo altere con un commit y `FALLO G-23` (mi `X-7`)
  · borrar una fuente obligatoria **si se caza**: `FALLO G-24`, y el derivador FALLA CERRADO
    con codigo 2 real (mi `X-8`)
  · el universo obligatorio **se deriva de verdad**, y las dos restas dan vacio. Las calcule
  · `R-04`, que dos gates no consiguieron cerrar, **esta cerrado**, y con mecanismo
  · `O17` esta propagada con una sede unica y cuatro invocaciones BYTE-IDENTICAS
```

**Y sin embargo la aguja del resultado no se ha movido, y esta es la medida exacta:**

```text
gate del doc 21    la bateria media 30 comprobaciones · 3 falsos verdes fuera de R1-R4
gate del doc 22    la bateria media 30 comprobaciones · 8 arboles defectuosos en verde
ESTE gate          la bateria mide 37 comprobaciones · `T` construyo 7 · **yo construi 6**,
                   dos de ellos por puertas que NADIE habia probado nunca

EL COSTE MARGINAL DE ENCONTRAR LA PUERTA SIGUIENTE NO ESTA SUBIENDO.
```

**La razon por la que no sube la doy en §8, y no es que la tanda trabajara mal.** Nueve de las
quince protecciones no generalizan porque **cada remedio se escribio con la forma exacta del
contraejemplo que lo motivo**, y el ejemplo mas limpio lo verifique yo en las dos direcciones:
`G-26` cerro la PALABRA y **la ETIQUETA la sustituyo**, con `G-31` —la mejor pieza de la tanda—
**certificando que el interruptor nuevo funciona**. Se cambio el tamaño del interruptor, no se
quito el interruptor.

### La diferencia con los dos gates anteriores, y es la unica que importa

**Los gates 21 y 22 fallaron por `M-04` y trataron `M-04` como un defecto corregible.** Los dos
prescribieron listas de protecciones. La tanda las escribio —**trece de las quince estan
literalmente ejecutadas**— y el resultado ha sido el mismo.

**Este gate falla por `M-04` y trae algo que los dos anteriores no trajeron: la razon por la que
`M-04` no se puede cerrar desde dentro, y la sede del propio corpus donde eso ya estaba escrito.**
§11.4 se titula «*La raiz de confianza — reducida a un punto declarado, no eliminada*» y dice
«*Cerrarlo exige un verificador EXTERNO al repositorio, y eso NO se resuelve aqui. Se declara en
vez de taparlo con una capa mas de comprobacion interna, **que solo moveria la circularidad de
sitio**.*»

> **Mi respuesta a la pregunta del encargo, sin rodeos: SI, es la misma causa raiz, y las
> protecciones sistemicas han movido MUCHO en la superficie y NADA en el fondo — porque el fondo
> no es alcanzable por una proteccion sistemica mas.**
>
> **Y por eso el trabajo NO debe seguir por donde iba.** Si la respuesta a este gate es otra
> tanda de protecciones, el gate que venga detras encontrara la puerta siguiente y tendra razon,
> y este expediente habra gastado su decimoquinta tanda en mover la circularidad de sitio por
> cuarta vez. **Lo que hay que hacer es cerrar los cuarenta y ocho de clase `A` —que son reales,
> baratos y estan determinados— y llevar la raiz al Owner con la pregunta de §13·B.** Eso no es
> detener el trabajo: es dejar de gastarlo en el unico sitio donde se sabe, por escrito y desde
> hace tandas, que no puede rendir.


---

## 15 · VEREDICTO

# INSUFICIENTE PARA F5

**`F4c` NO se cierra. Sigue ABIERTA. `F5` NO queda autorizada. No he corregido nada.**

### Las razones, numeradas. Las dos primeras bastan cada una por si sola.

**1 · `M-04` sigue FALLIDA por tercer gate consecutivo, y la reproduje yo con mis manos —
incluyendo dos puertas que nadie habia abierto nunca.** Construi y ejecute **seis arboles
defectuosos que pasan la bateria en verde con `EXIT=0` y el porcelain vacio**. El peor es el que
ya conociamos: el validador que corre las 67 mutaciones negativas del kernel vaciado a
`import sys; sys.exit(0)`, sus evidencias inventadas y la huella reanclada **con el valor que la
propia bateria me publico al fallar** → `37/37`, con `OK G-30`. **Y los dos nuevos son mios:**
ampute la comprobacion `G-31` y obtuve **`36/36 comprobaciones en verde`** sin que `G-31`
apareciera una sola vez en el informe —la bateria no esta en ningun inventario y su censo no se
contrasta contra nada—; y **fabrique una prueba de agotamiento en el documento 22**, declarando
«LEIDO INTEGRO» el documento 11 —10 275 lineas, revisor inexistente, SHA-256 correcto— → **37/37
verde**. Ese ultimo alcanza al aparato de COBERTURA, que es lo unico que este expediente habia
conseguido certificar dos veces seguidas.

**2 · La FASE 0 que `O17` ordena crear NO ES EJECUTABLE tal como esta escrita, y lo verifique
contra la fuente.** El SUJETO que la fase exige **resuelto en su ENTRADA** contiene «*la iniciativa
del macrocircuito, por su identificador*», y el GATE de la misma fase dice «*no se abre la
iniciativa … Bloquear despues de abrir la iniciativa YA es haber mutado estado*». **Las dos no
pueden ser ciertas a la vez.** Y su SALIDA es una celda canonica de `cobertura` que en `N` y en
`A` no tiene donde escribirse, porque `estado/` nace despues de ella. **Ninguna de las dos exige
decidir arquitectura ni es materia del Owner: exigen DECIR donde nace el identificador y donde
vive la declaracion.** Pero mientras no se digan, **el remedio del GRAVE n.o 2 del documento 22
esta escrito y no se puede ejecutar**, y va PRIMERO en los cuatro macrocircuitos.

**3 · La cadena de niveles sigue con un eslabon sin productor que NADIE declara, y esta en la
seccion escrita para no tapar huecos.** La Operativa se produce en **`INS-4` y en ningun otro
sitio** —§9.2 L7129—; §9.3 la invalida cuando «*cambia la disposicion del estado*»; `M3` es
literalmente «*migrar ESTADO PERSISTIDO, con su esquema*»; **§8.3 no nombra la Operativa ni una
vez en sus 107 lineas, y lo barri**. `M5` certifica Integrada sobre un presupuesto vencido.
**Y §9.6 declara honestamente el hueco identico de la ADOPCION cuatro lineas mas arriba, bajo el
titulo «LA SALVEDAD, DICHA Y NO TAPADA».** Declarar uno y callar el otro en la misma enumeracion
es peor que no declarar ninguno.

**4 · La propagacion de `O17` EXCEDE la resolucion del Owner en la sede que MANDA, y se contradice
a si misma dentro de una sola tabla.** `O17` da a `SEG` **bloqueo**; la fila `D107`, bloqueo;
§9.6, bloqueo. **§18 le da «via 3» en `proceso:SIS`, cuatro veces** —y **la misma tabla escribe
«`SEG` sin via: `PN-13`» en otras dos filas del mismo proceso**, que abri una a una. Es la unica
presion que va al Owner por materia nueva, violada por la tanda que la lleva. Y §18 es la sede
que §8.0 declara que manda, con una regla de precedencia que choca con la de §9.6 y que nadie ha
jerarquizado.

**5 · Una cifra que su unica sede declara «DERIVADA de §18» ya no deriva de §18, y con ella se cae
una conclusion publicada sobre material APROBADO.** §8.0 publica `2·4·2·4` diciendo «*El recuento
se DERIVA de §18 y se mueve con ella. No se escribe aparte*». **Derive §18 yo: hoy es `3·5·3·5`.**
Y la consecuencia no es cosmetica: con la `FASE 0` dentro de la racha, **`U` pasa a tener TRES
items `SIS` consecutivos**, el FRENO 3 de `a.7` —«mas de dos»— **si llega a evaluarse**, y la
conclusion «*Ninguno de los cuatro necesita excepcion del Owner*» deja de estar derivada
**precisamente en el macrocircuito donde el antecedente del freno es plausible**.

**6 · Y la razon de metodo, que es la que impide cerrar aqui.** **Diecisiete de mis cuarenta y
nueve hallazgos los introdujo o los dejo pasar esta misma tanda**, y varios son el defecto que el
propio §0 del documento 11 nombra como el mas repetido del corpus, **cometido en el acto de
corregirlo**: el addendum de `D97` publica cuatro cifras bajo el rotulo «LA CIFRA, DERIVADA HOY y
no copiada» y **caduco un commit despues, el mismo dia, dentro de su propia tanda**; `P-16`
reclasifico `4b` y dejo el titular «siete secuencias» sobre ocho; el manifiesto de este gate
publica un total que sus propias dos subsumas desmienten tres lineas mas arriba.

### Lo que expresamente NO fundamenta este veredicto

- **NO falla por cobertura.** `OBLIGATORIO − ASIGNADO = ∅` y `ASIGNADO − LEIDO = ∅`, **y las
  calcule las dos**. Las 64 filas cuadran en lineas y en SHA-256, con **cero discrepancias**. Los
  **52 agotamientos pasan las dos reglas, uno a uno**. **`C-L.5` sigue CERTIFICADA y la mantengo
  certificada**, por tercera vez consecutiva.
- **NO falla por `O17` ni por `D107`.** La resolucion es del Owner; `D107` **se declara derivada y
  lo es**; y la propagacion es **la mas disciplinada que este expediente ha producido**: una sede
  unica, cuatro invocaciones **byte-identicas que verifique yo**, doce reglas trazadas, nueve
  contraescenarios, y una abstencion correcta donde `O17` no llega.
- **NO falla por el aparato del propio gate.** El `T147` en rojo y el `12/13` los causa el
  manifiesto que **este gate** anadio en `c36d2ba`; **sobre el arbol de la tanda medi
  `1 superadas · 0 fallidas · EXIT 0`.** No cuenta contra la candidata.
- **NO falla por el derivador.** Es un programa **duro**: falla cerrado con **codigo 2 real** ante
  una ruta ausente, y lo medi. Lo que falla es una promesa mas ancha que el programa.
- **NO falla por el CORRIGENDUM.** Acota sin editar.
- **NO falla porque quede arquitectura por inventar.** **Ninguno de mis cuarenta y nueve hallazgos
  es BLOQUEANTE, y cuarenta y ocho son clase `A`.** Lo unico que va al Owner es **la raiz**, y su
  pregunta esta formulada palabra por palabra en §13·B.

### Y QUE SI HA QUEDADO CERRADO, porque eso tambien es informacion

1. **`C-L.5` CERTIFICADA por tercera vez, y la cobertura de este gate es real**: 12 asignadas, 12
   leidas integras, 52 agotamientos que pasan las dos reglas, 64 filas exactas. **Lo calcule yo.**
2. **`R-04` ESTA CERRADO, y con mecanismo.** Es el hallazgo que dos gates no consiguieron cerrar y
   que el documento 22 declaro AGRAVADO. **El punto 7 de §2.6.9 se reescribio de verdad esta vez**
   —lo compare con `git show 7764cca`— y clasifica **por lo que observa** en vez de por tramos de
   tiempo: `[1,2)`·`[2,4)`·`[4,6)`, union sin huecos y sin solapes.
3. **El GRAVE n.o 2 del documento 22 esta genuinamente ATACADO**: el nivel Estructural **tiene
   productor**, la cadena de §9.2 deja de ser inaplicable y `gate:sistema-conforme` pasa de una
   aparicion definitoria a veintitres. **La clase `B` del documento 22 esta RESUELTA y ya no
   bloquea.**
4. **§15.8 tiene hoy diecisiete bloques y §0 REMITE en vez de enumerar** — lo derive con el `awk`
   que el corpus publica, y coinciden. **La regla del ordinal por fin EJECUTA.**
5. **`PN-17` y `PN-18` registran sin elegir**, con sus nueve elementos y su prueba que falla hoy
   como debe. **Registrar es F4 y elegir es F5: aqui se respeta.**
6. **Tres protecciones GENERALIZAN de verdad, con control positivo mio**: `G-01` por polaridad,
   `G-16` por igualdad exacta, y `G-26` ya no cede a la palabra «regresion». **Y dos refutaciones
   mias fallaron a favor del corpus**: el material APROBADO **si esta protegido** (`FALLO G-23`) y
   borrar una fuente obligatoria **si se caza** (`FALLO G-24` + derivador con codigo 2).
7. **El universo obligatorio se deriva de verdad y no esconde su lista**: el componente (v) es una
   lista anotada **y el propio derivador lo declara**, que es la conducta correcta.
8. **La disciplina de inmutabilidad se cumple**: `D1`-`D106` y `O1`-`O16` conservan su texto, la
   serie `D` es continua —107 filas, 107 valores unicos, sin huecos—, y los documentos 15-22
   estan sin tocar en el arbol real.

**Esta sigue siendo, con distancia, la candidata mas solida que este corpus ha producido. No falla
por concepcion, no falla por cobertura, no falla por lo que decidio y no falla por lo que dejo sin
construir. Falla por dos cosas: porque la fase que la resolucion del Owner ordena crear esta
escrita entera y no se puede ejecutar; y porque el instrumento que existe para probar que sus
decisiones han llegado a todas partes NO PUEDE, POR CONSTRUCCION, distinguir un arbol sano de uno
mutilado — y eso el propio corpus lo escribio en su §11.4 y lo dejo abierto.**

**La primera se corrige en F4c. La segunda no, y es del Owner.**

---

## 16 · CIERRE

```text
git status --porcelain   AL ABRIR    →   (salida vacia)     primer comando de la sesion
git status --porcelain   AL CERRAR   →   (salida vacia)     ultimo comando de la sesion
HEAD al abrir y al cerrar            →   c36d2ba707eed5ea24b9a13df6c4e6be49b68cc6, identico
RAMA                                 →   gate/f4c-certificacion-2-20260830
git worktree list                    →   solo el repositorio principal (el temporal, retirado)

FICHEROS DEL REPOSITORIO EDITADOS, CREADOS O BORRADOS POR MI   ninguno
COMMITS · PUSH · PR · MERGE                                     ninguno
EXPERIMENTOS   /tmp/lab-U/{base,RA,RC,RD,U1,U2,U3,U4,U5,U6,U7} — copias `cp -a` fuera del
               repositorio, mas un worktree temporal sobre `e316396`. TODO BORRADO
SUBAGENTE `Agent`                                               NO USADO
FICHEROS DE GATES ANTERIORES (`ADJUDICACION-R.md`, `DICTAMEN-P/Q`, `P*`, `Q*`)   NO ABIERTOS
NINGUN HALLAZGO SE HA CORREGIDO, y es deliberado: quien corrige no certifica.
```

**`F4c` sigue ABIERTA. `F5` NO queda autorizada. `C-L.5` sigue CERTIFICADA.**

**ADJUDICADOR `U` · adjudicacion cerrada.**
