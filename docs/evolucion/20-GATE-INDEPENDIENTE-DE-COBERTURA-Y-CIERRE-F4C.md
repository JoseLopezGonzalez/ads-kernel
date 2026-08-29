# GATE INDEPENDIENTE DE COBERTURA Y CIERRE DE F4c

> **Veredicto, en una línea:**
> # INSUFICIENTE PARA F5
>
> **`F4c` NO se cierra. Sigue ABIERTA. `F5` NO queda autorizada.**

## 1 · Identidad y procedencia

```text
CANDIDATA JUZGADA   review/f4c-post-gate-candidate-20260829-r2
COMMIT              c3d6465a519855095ad6fd2a6a168ec72ef5ed7a
ÁRBOL               db26b4d1898b17ce66f89ea3bb25f817c7c1d6c3
                    verificado con `git ls-remote` ANTES de empezar
RAMA DEL GATE       gate/f4c-cobertura-final-20260829, creada en ese commit exacto,
                    sin upstream

REVISOR M           arquitectura, protocolo transaccional, estado, decisiones, material
                    aprobado, KERNEL.md y los contratos C1, C5, C6, C7
REVISOR N           capacidades, procesos, diseño, entrada, contratos C2/C3/C4, las
                    enmiendas E1 y E2, y el documento 15
ADJUDICADOR O       recibe ambos dictámenes YA CERRADOS y emite el veredicto único

INDEPENDENCIA       los tres son agentes NUEVOS con contexto limpio. Ninguno escribió F4,
                    ninguno aplicó D16–D103, ninguno es autor de las correcciones
                    post-gate y ninguno es revisor A–L de las pasadas anteriores.
                    M y N trabajaron EN PARALELO y no se vieron.
                    O NO resolvió por mayoría: verificó cada afirmación material contra
                    su fichero y su línea, RECHAZÓ lo que no se sostuvo, corrigió dos
                    citas de N y añadió cuatro hallazgos propios.

EL COORDINADOR      repartió el corpus, generó los manifiestos con SHA-256, derivó cifras
                    de contraste ANTES de ver ningún dictamen, comprobó por su cuenta las
                    afirmaciones más consecuentes, transcribió y validó.
                    NO emitió suficiencia y NO corrigió ningún hallazgo.
                    Es el autor material de las tandas anteriores, y por eso su juicio no
                    cuenta aquí.
```

**Una corrección del adjudicador al coordinador, y va por delante.** El encargo del gate daba
`c3d6465a…` como «árbol». Eso es el **commit**; el árbol es
`db26b4d1898b17ce66f89ea3bb25f817c7c1d6c3`. `O` lo abre su dictamen corrigiéndolo, y añade:
«Es exactamente la clase de identificador derivado y escrito a mano que este expediente lleva
doce tandas persiguiendo, y aparece en el encargo del gate que viene a cerrarlo.» **Tiene
razón, y consta.**

**Qué comprobó el coordinador por su cuenta, antes de transcribir nada.** Derivó las cifras de
contraste sin abrir ningún dictamen; después verificó contra fichero y línea `M-01`, `M-02`,
`M-05`, `M-06`, `M-07`, `M-08`, `M-11`, `N-01` —incluidos sus tres fixtures—, `N-02`, `N-03`,
`N-04`, `N-05`, `O-01`, `O-02`, `O-03` y `O-04`; y **reprodujo en un clon de `/tmp`, ya
borrado, la refutación 2 de `M-04`**: la batería da **30/30 en verde** sobre un árbol que
publica a la vez «CINCO procesos · NUEVE pares» y «SEIS procesos · DIEZ pares», que es el
contraejemplo exacto que `G-15` declara detectar. **Todos se sostienen.**

## 2 · Cobertura mínima obligatoria, y qué se leyó de verdad

```text
BLOQUE COMÚN · leído ÍNTEGRO por M, por N y por O, de forma independiente

  docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md   2163
     BLOQUE B (§8–§12, certificación por niveles)   LEÍDO ÍNTEGRO por los tres
     BLOQUE C (§13–§17, iniciativa y dosier vivo)   LEÍDO ÍNTEGRO por los tres
  docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md                1257
  docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md       1650
  docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md            3665
                                                                  ─────
                                                                   8735 × 3 lectores
```

**Es la primera vez en el expediente que estas cuatro fuentes se leen íntegras.** Tres gates
consecutivos —el final, el de cierre y el definitivo— declararon no haberlas abierto, y el
adjudicador `I` del documento 18 dejó dos preguntas expresamente sin resolver porque dependían
de ellas. **Las dos quedan contestadas en esta pasada** (§7).

```text
LOTE DE M · 26 411 líneas          LOTE DE N · 14 534 líneas
  11-ARQUITECTURA-INTEGRADA   9058   01-PROCESOS.md                564
  19-GATE-DEFINITIVO          1152   LAS QUINCE FICHAS           1829   ← íntegras
  CHECKPOINT-ADS-NEXT         1898   15-TERCERA-REVISION           651   ← nadie la abrió
  DECISIONES-Y-CONTRADICC.     677   diseno/00 01 02 04 05        1095
  (a) a-CAPACIDADES           1132   C2 · C3 · C4                  859
  (b) b-RECORRIDO             1288   entrada/00 · 02 · 04          360
  KERNEL.md                   1590   E1 · E2                       441
  C1 · C5 · C6 · C7            862   + el bloque común            8735
  + el bloque común           8735
```

**Los dos lotes son complementarios, y eso importa más que su suma.** `M` no podía encontrar
`N-01` porque no leyó `esquemas/proceso.yaml` ni las fichas; `N` no podía encontrar `M-02` ni
`M-03` porque §2 del documento 11 era el lote de `M`. **Cada mitad del corpus produjo un
defecto GRAVE que la otra mitad no podía ver**, y `O` lo señala como la medida real de la
cobertura.

**Qué sigue sin abrir**, derivado de las declaraciones de los tres:

```text
capacidades/<COD>/roles/ · metodos/ · prompts/ · composicion.md   ~150 ficheros
packs/ más allá de cabeceras · tooling/ · pruebas/
dieciocho de los diecinueve esquemas .yaml
circuitos/ · recorrido/00-OBLIGACIONES-Y-CIERRE.md · entrada/01, 03, 05
docs/owner/ · el BRIEF · los documentos 12, 13 y 14
```

## 3 · Manifiestos de lectura

Los SHA-256 y los recuentos de líneas los calculó **cada revisor por su cuenta** con
`sha256sum` y `wc -l`, y coinciden con los que el coordinador generó antes de repartir.

### 3.1 · Bloque común — verificado por los tres

| ruta | líneas | SHA-256 |
|---|---|---|
| `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | 2163 | `a88609167dbbea2818b7f2e68cbd4c6fc704cb7e2245ee0a2c873052486fd159` |
| `docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md` | 1257 | `8243034f286160cc89330af95b49f558af0dd16d1b36a37ccbdf02f74a79d185` |
| `docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` | 1650 | `18f876d4cd47a2f7cfde15594f98696cfacf750607cd23811dd40ffb36d6c29c` |
| `docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` | 3665 | `1e71366b10d2293802db435de14953771ebd8fc13b426acedd7c0efe21cdb496` |

**Anclas de `O`, de regiones separadas, para demostrar el recorrido:**

- `ADS-PENDIENTES` L988 — «No debe declararse un nivel superior por argumento ni porque pase el nivel anterior.» · L2119–2120 — «Qué mínimo documental exacto permite superar «ahora puedes empezar a programar»…»
- Doc 16 L215 — «el control repo **deja de commitear para todo el producto, indefinidamente**.» · L1156 — «Faltan, sin ambigüedad y por nombre: los dos ficheros de handoffs, los seis de `diseno/`…»
- Doc 17 L174 — «Eso **contradice literalmente** `C5` L36-37.» · L1240 — «**Resolución: manda `00-CIRCUITOS.md` L238.** … **D tiene razón contra E**.»
- Doc 18 L2466 — «`<CAP>:revisión` | `b.16:834-836` + `grep -rn` sobre `kernel/` | **cero instancias**.» · L3546–3548 — «NO HE RESUELTO `I-08` CONTRA `b.3` NI `b.5`, que nadie abrió… **la refutación posible vive donde no he mirado**.»

### 3.2 · Lotes propios

`M` y `N` registran en sus dictámenes, fichero a fichero, ruta, SHA-256, líneas, la marca
`LEÍDO ÍNTEGRO`, primera y última sección sustantiva, dos anclas de regiones separadas y qué
aporta cada fuente. Están transcritos íntegros en §4 y §5.

---

## 4 · Dictamen literal del REVISOR M

> Transcrito **sin suavizar y sin resumir cambiando el sentido**. Lo emitió `M`; el
> coordinador sólo lo transcribe.


**Ámbito:** arquitectura, protocolo transaccional, estado, decisiones, material aprobado, `KERNEL.md`, contratos `C1`, `C5`, `C6`, `C7`.
**Árbol:** `db26b4d1898b17ce66f89ea3bb25f817c7c1d6c3`, commit `c3d6465a…`, rama `gate/f4c-cobertura-final-20260829`. **Modo sólo lectura, comprobado:** `git status --porcelain` vacío al abrir y al cerrar; `HEAD` y el objeto `tree` idénticos en los dos extremos. Los quince SHA-256 del corpus obligatorio son idénticos al inicio y al final. Los experimentos de refutación se hicieron **íntegramente en `/tmp`**, sobre clones y copias, y el directorio se borró al terminar.

**Límite de entorno declarado.** El intérprete disponible es **Python 3.10.12**. La batería canónica del kernel exige 3.11+ y publica evidencia derivada: **no la he ejecutado**, porque habría podido ensuciar el árbol. Es la reproducción exacta de `A14`, y consta como límite mío, no como hallazgo contra F4.

#### 1 · Evaluación propia provisional, y qué cambió

Escribí una evaluación provisional **antes** de abrir el bloque común y los documentos 15–19. Juzgué correctos a priori: la aritmética de §3.6, las diecisiete ventanas de §2.6.5, las cuarenta y seis filas adversariales, el recuento de presiones, la honestidad de la procedencia de `O16` y la forma de `PN-15`. Llevé siete sospechas a verificación.

| | qué creía | qué encontré |
|---|---|---|
| `S1` | sospecha | **CONFIRMADA.** Es `M-02`, GRAVE. La circularidad existe y ninguna sede la resuelve |
| `S2` | sospecha | **CONFIRMADA Y AGRAVADA.** Además de la laguna de `fsync`, la justificación de exhaustividad de las diecisiete ventanas quedó **invalidada por `D88`** y nadie lo propagó |
| `S3` | sospecha | **CONFIRMADA**, MENOR: `X58` está en L1451, entre `X61` y `X62` |
| `S4` | pendiente | **Derivé el catálogo yo mismo.** Coincide con «CINCO procesos · NUEVE pares» — y al derivarlo encontré `M-01`, GRAVE, que es un defecto distinto y mayor |
| `S5` | pendiente | **REFUTADA LA BATERÍA.** Dos árboles defectuosos distintos pasan **30/30 en verde**. Es `M-04` |
| `S6` | **ME EQUIVOQUÉ** | Sospeché que la entrada `owner_captado` de `O16` no existiera. **Existe**, en `CHECKPOINT` L866–875, con fecha, formulación presentada y cita literal. Lo escribo porque un dictamen que sólo publica sus aciertos no es una medida |
| `S7` | sospecha | **REFUTADA A FAVOR DEL CORPUS.** `git diff` sobre el registro devuelve **121 inserciones y CERO borrados**. `D1`–`D95` y `O1`–`O16` intactas |

Lo que **no** cambió: mi impresión de que el rasgo más fuerte de este corpus es su honestidad sobre lo que no está hecho. Lo que cambió del todo es mi expectativa sobre la batería: entré esperando encontrarla sólida y salgo habiéndola refutado dos veces.

#### 2 · Declaración de cobertura, sin adornos

**He leído íntegramente las QUINCE fuentes que se me asignaron** —las cuatro del bloque común, con los BLOQUES B y C, y las once de mi lote—. Son **26 411 líneas**, recorridas por tramos consecutivos que cubren todas sus líneas.

**Y ahora lo que no he leído, que es lo que importa decir.** No he leído el documento 15; ni `diseno/00`–`05`, `C2`, `C3`, `C4`, `entrada/00`/`02`/`04`, `E1`, `E2`; ni las quince fichas de capacidad. No estaban en mi lote. No he ejecutado la batería canónica del kernel.

**Consecuencia que declaro antes de cualquier veredicto:** mi cobertura satisface `C-L.5` tal como `L` la escribió, **pero NO satisface la condición mínima más amplia que el propio checkpoint declara**. Sobre lo que se me encargó, la cobertura está completa y demostrada. Sobre lo que el corpus se exige a sí mismo, no lo está — y el encargo no me dio esas fuentes. Lo digo aquí, y no después del veredicto.

#### 3 · HALLAZGOS

##### `M-01` · **GRAVE** · La derivación de `<CAP>:revision` pierde la participación condicional de `DOM` y `SEG` en `proceso:AUD`, que `D98` había nombrado expresamente

Criterio, `11`:8679–8683:
> «si `DOM` o `SEG` PARTICIPAN en un proceso por **CUALQUIER VÍA** —propietaria, obligatoria, **condicional**, o item enlazado con `capacidad_productora` tipada— … ENTONCES ese proceso necesita su `<CAP>:revision` correspondiente DESPUÉS de `VER`.»

Algoritmo, `11`:8754:
> «3 · **NIVEL A** — para cada proceso con `propietario_global` **FIJADO**, emitir un par `(proceso, capacidad)` por cada participación estructurada de `DOM` o `SEG`.»

Lo que `D98` había declarado, `11`:8647–8648:
> «`proceso:AUD` queda igualmente fuera: hace participar a `DOM` y a `SEG` con la notación **sin tipar**.»

`proceso:AUD` declara `condicionales: DOM` y `condicionales: SEG`, y `b.16` L895 lo confirma en material APROBADO. Por el criterio, esas dos participaciones exigen revisión tras `VER`. Por el algoritmo no la exigen **en ningún nivel**: el nivel A excluye `AUD` entero por tener propietario DERIVADO, y el nivel B mira sólo el propietario efectivo del item, no los condicionales. **Un item `AUD` con propietario `PRD` que active `C-DOM` y `C-SEG` sale conforme sin ninguna `:revision`.** F6 no puede materializar esto sin **decidir** cuál de las dos lecturas vale — que es exactamente lo que `K-02` cerró y lo que el contrato promete que no volverá a pasar («F6 MATERIALIZA; no elige la forma»).

Y su causa es la misma clase que ya se registró dos veces: `D98` corrigió `D92` y reintrodujo el barrido léxico en su algoritmo; `D103` corrigió `D98` y perdió el caso que `D98` había nombrado.

**¿Bloquea F5? Sí.** `C-L.3` es una de las cinco condiciones que bloquean, y esto la deja sin cerrar.

##### `M-02` · **GRAVE** · Circularidad de identidad entre `abandonada` y su `deriva`: el segundo terminal del protocolo no tiene representación construible

§2.6.9 paso E, `11`:1830–1833:
> «E · CERRAR   sólo entonces, y **en este orden**: · emitir `abandonada`, con la evidencia de la verificación de D · emitir el `deriva` que conserva el bloqueo»

§3.6, `11`:4102 — campo **OBLIGATORIO** de `abandonada`:
> «`deriva_emitida` = `id` del `deriva` que conserva el bloqueo»

§2.8, `11`:2810 y 2815:
> «`id = EV-H( representación canónica del evento MENOS `id` )`» · «`predecesor` **VA INCLUIDO** — es parte de la historia»

§3.6, `11`:3662:
> «`predecesor`  el evento que este emisor observó como último.»

`id(abandonada)` incluye `deriva_emitida`, que es `id(deriva)`. El `deriva` se emite después, luego su `predecesor` es el `abandonada`, luego `id(deriva)` incluye `id(abandonada)`. **La dependencia es circular y no la resuelve ninguna sede**: la busqué en §2.6.9, §2.6.11, §2.8, §3.6 y en la tabla de validadores de la capa B, y no está.

Las tres salidas que existen son las tres una decisión arquitectónica: invertir el orden del paso E, sacar `deriva_emitida` del cómputo de `id`, o referenciar el `deriva` por su `tx` en vez de por su `id`. La tercera rompería la comprobación B de la fila 3 de la tabla de validadores (L4291), que exige seguir la referencia. **Ninguna la ha tomado nadie.**

Es exactamente la clase que el propio §2.8 dice haber cerrado, `11`:2746:
> «`id`  EXCLUIDO por construcción. Es lo que se está calculando: **incluirlo es la circularidad que F4c no resolvía**»

La consecuencia material: `abandonada` es uno de los **dos terminales** del autómata y el único desenlace que revierte sin publicar mezcla parcial. Como está especificado, **no se puede emitir**.

**¿Bloquea F5? Sí.** Es un defecto arquitectónico de §2, que es lo que `PN-1` propone aprobar como sección (g), y del mismo calibre que `J-01`.

##### `M-03` · **GRAVE** · El `deriva` que conserva el bloqueo no exige `fsync`, el arranque prohíbe reemitirlo, y la tabla de diecisiete ventanas se declara exhaustiva sobre una justificación que `D88` invalidó

§2.6.6, `11`:1207–1213:
> «(4) el evento `abandonada` y SU DIRECTORIO … **NO EXIGIDO**  los derivados, **el marcador**, el evento `derivada` y el evento `conflicto`»

§2.6.4 paso 0, `11`:956–958:
> «El `deriva` … YA declara el estado observado de todas sus rutas … **No se emite un `deriva` por arranque: el que existe se conserva** hasta que la reparación lo resuelve»

§2.6.5, `11`:1112–1114:
> «Se enumeran las **diecisiete**, y **son todas** … **la única escritura que un abandono produce es un evento del diario**, cubierto por la disciplina de §2.6.3»

Son tres piezas que juntas dejan un fallo silencioso:

1. El evento `deriva` **no está en ninguna de las dos listas**: ni entre los cuatro `fsync` obligatorios, ni entre los cuatro excusados —esa lista nombra `derivada`, que es una fase distinta—. Su marcador `estado/deriva/<ID>.abierta`, que `D88` creó, sí está entre los NO EXIGIDOS.
2. Una caída de máquina entre el `abandonada` durable y el `deriva` deja el marcador de transacción retirado, el commit desbloqueado y **el bloqueo de los items perdido**.
3. El arranque no lo repara: el paso 0 dice literalmente que no se emite un `deriva` por arranque porque «el que existe se conserva» — y no existe.

Y **no hay ventana que cubra esa secuencia**. La justificación de por qué no hace falta —«la única escritura que un abandono produce es un evento del diario»— era cierta antes de `D78`/`D88` y dejó de serlo después: el paso E produce hoy dos eventos, un marcador nuevo, la retirada de otro y el borrado de la cuarentena. **Nadie propagó `D88` hasta aquí.** Es el mismo modo de fallo que `D34` cerró como BLOQUEANTE para los canónicos: silencioso y en el eje de la durabilidad.

**¿Bloquea F5? Sí.**

##### `M-04` · **GRAVE** · La batería de verificación se refuta: dos árboles defectuosos distintos pasan 30/30 en verde

**Refutación 1 · `G-15` no implementa la vía PROPIETARIA que su criterio declara.** `_participaciones()` lee **sólo** `condicionales[].capacidad` y `obligatorias[].capacidad_productora`. **No lee `propietario_global` para el nivel A**, pese a que el contrato lo declara como uno de sus tres campos de entrada y a que el criterio nombra la vía «propietaria» en primer lugar. Fixture: `propietario_global: "SIS"` → `"DOM"` en `proceso:SIS`. `G-15` **no vio nada**. Lo detuvo `G-23`, que sólo dice «el kernel cambió» — y `G-23` desaparecerá por diseño en cuanto F6 edite `01-PROCESOS.md`, que es exactamente lo que este contrato manda hacer.

**Refutación 2 · `G-15` compara sólo la PRIMERA proyección del bloque · 30/30 EN VERDE.** `re.search` toma la **primera** coincidencia y no comprueba que sea única. Inserté en el mismo bloque §19 una segunda proyección contradictoria: «Resumen operativo para F6: **SEIS procesos · DIEZ pares**, contando `AUD` como par fijo.» Es literalmente el contraejemplo que `G-15` declara detectar y la cardinalidad insatisfacible que `D103` existe para retirar. Resultado: **30/30 comprobaciones en verde**. **Sí puedo construir un árbol defectuoso que pase en verde.**

**Refutación 3 · `G-16` no contrasta la clasificación contra nada · 30/30 EN VERDE.** Moví `C-L.12` de «REGISTRADAS PARA F5 2» a «CORREGIDAS EN F4c 9» y ajusté los dos contadores: **30/30 en verde**. El árbol resultante declara `C-L.12` **corregida en F4c** catorce líneas antes de que su propia línea de detalle diga «`C-L.12` REGISTRADA PARA F5», y contradice al documento 19. La batería no ve ninguna de las dos cosas.

**Refutación 4 · sin `git`, tres comprobaciones pasan vacuamente.** Copié el árbol **sin `.git`**, mutilé `a-CAPACIDADES-APROBADA.md`, añadí a `18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` la línea «EL GATE 18 SE DECLARA SUPERADO» y modifiqué `C7`. Resultado: **29/30**, con `G-21` «ninguna difiere», `G-22` «intactos» y `G-23` «intacto salvo…». En un árbol distribuido como tarball o `git archive` —la forma en que este corpus viajaría a un revisor externo—, **la batería declara intacto lo destruido**.

Añado dos debilidades estructurales: `_COMPONENTES_CL13` es una **lista literal escrita a mano** de los seis componentes —el censo enumerado que `D102` condena, dentro de la comprobación que verifica que no haya censos enumerados—; y la detección de estados compuestos sobre las 43 filas es **código muerto** (`M-11`).

**Qué concluyo, y qué no.** No concluyo que la batería sea inútil: `G-11`, `G-11b`, `G-13`, `G-20`, `G-24`, `G-25`, `G-26` y `G-27` derivan de verdad y son buenas. Concluyo que **las dos comprobaciones sobre las que descansan las afirmaciones centrales de esta tanda son refutables**, y que su 30/30 no puede usarse como evidencia de que `C-L.3` está cerrada ni de que la clasificación de las trece condiciones es correcta.

##### `M-05` · **MEDIO** · La prueba posterior de `PN-15` afirma que sería imposible pasar en verde hoy, y hoy pasaría en verde — satisfecha por la fila que la propia `D97` añadió

`11`:8285–8290:
> «PRUEBA POSTERIOR  una comprobación mecánica que … exija **o** una fila en `a.11` que la nombre … **o** una fila en §17 para `kernel/KERNEL.md` que declare qué le pasa. **Falla en verde hoy sería imposible: hoy no existe ninguna de las dos para ninguna de las cuatro.**»

`11`:8370:
> «| `kernel/KERNEL.md` `G20`–`G23` | **PRESIONADAS y pendientes de F5. NO derogadas por F4, y NO sustituidas por §8.** … La decisión y su enmienda son `PN-15` (`D97`) |»

`D97` añadió esa fila. La prueba prescrita es una disyunción, y esa fila satisface el segundo disyunto para las cuatro reglas a la vez. **La prueba pasaría en verde hoy**, y el texto afirma lo contrario en la misma sección, ochenta líneas más arriba. Es la misma clase de defecto que `K-02`, y es autoinfligido: la satisface la corrección que la acompaña.

##### `M-06` · **MEDIO** · La «EXCEPCIÓN EXACTA DEL KERNEL» del checkpoint dice «y sólo ésta» y nombra tres ficheros; son cuatro

`CHECKPOINT`:1782–1786:
> «deja de ser cierto que «`kernel/operativo/` está intacto». Lo que hay es una excepción NOMBRADA, **y sólo ésta**: `comprobar_negativos.py` · `kernel/.upstream-hash` · `kernel/operativo/pruebas/evidencia/*`»

Derivado del árbol, `git diff --name-only 05f71b7 | grep '^kernel/'` incluye además **`kernel/operativo/entrada/02-CIRCUITO.md`**, que es kernel operativo **sustantivo** y se modificó en `d868bcb` para cerrar `K-09`. **La batería sí lo nombra** —`DOC_AUTORIZADO`, con su motivo—, luego la sede que se corrigió fue el código y no el checkpoint, que es la sede que un agente sin contexto lee. El checkpoint dice «y sólo ésta» y es falso desde `d868bcb`. Es exactamente el defecto de `L-01` reproducido por la tanda que venía a cerrarlo, y en el párrafo que existe para no repetirlo.

##### `M-07` · **MEDIO** · La procedencia de `O16` fecha la consulta al Owner un día después de que la resolución entrara en el registro

```text
git log --reverse -S'| O16 |' → a713590  2026-08-28
git log -1 --date=short d868bcb → d868bcb  2026-08-29
la procedencia declara FECHA 2026-08-29
```

La fila `| O16 |` existe en el registro desde el **28**. La procedencia añadida el **29** dice que ese día se le presentó al Owner la formulación y que ese día respondió. **El corpus registró como resolución del Owner, durante al menos un día, algo que —según su propio registro de procedencia— el Owner todavía no había confirmado.** `L-02` no era que la decisión fuera falsa; era que el corpus no podía demostrar que el Owner la tomara. La procedencia demuestra que la tomó, y demuestra a la vez que se registró antes. Ninguna de las dos sedes reconcilia las fechas.

Digo con precisión lo que **no** afirmo: no afirmo que el Owner no confirmara, ni que la cita sea falsa. Afirmo que la fecha registrada y el historial no cuadran.

##### `M-08` · **MENOR** · La cita a `a.6` L504–505 es incorrecta, y convive con la cita correcta

La frase «DOM y SEG aportan **condiciones antes de construir** y revisan después» está en `a-CAPACIDADES-APROBADA.md` **L502–503**. `a.6` L504–505 dice otra cosa. `D92` y `11`:8627 citan **L504–505**; `D98` y `11`:8653 citan **L502–503**. Las dos citas del mismo documento están a veintiséis líneas una de otra.

##### `M-09` · **MENOR** · La grafía de la variante no está reconciliada: (b) escribe `revisión`, F4 escribe `revision`

(b) L836: «`<CAP>:revisión`      tras VER  revisan lo construido.» Todo el aparato de F4 escribe `<CAP>:revision` sin tilde, y la prueba prescrita busca `:revision`. La fuente APROBADA lleva tilde. Nadie declara cuál es la grafía canónica. Es hermano de `F-01`, que sí se registró como presión.

##### `M-10` · **MENOR** · `X58` está fuera de orden en la tabla de §2.6.7

`11`:1451, entre `X61` (L1450) y `X62` (L1452). El recuento de cuarenta y seis filas y cuarenta y seis identificadores es correcto —lo derivé yo—, pero una fila fuera de secuencia invita al error que `M2` ya produjo con `X32`–`X34`.

##### `M-11` · **MENOR** · La comprobación de «ningún estado compuesto» de `G-16` es código muerto

```python
filas = re.findall(r"^\| `([A-Za-z0-9-]+)` \| (BLOQUEANTE|GRAVE|MEDIO|MENOR) \| \*\*`([A-Z_0-9]+)`\*\* \|(.*)$", ...)
comp = [f[0] for f in filas if " y " in f[2] or "+" in f[2]]
```

El grupo 3 está restringido a `[A-Z_0-9]+`, luego **nunca puede contener `" y "` ni `"+"`**. La comprobación que existe para impedir el doble conteo que produjo el `34·2·1·8·1 = 46` **no puede disparar jamás**.

##### `M-12` · **MENOR** · `G-21`, `G-22` y `G-23` pasan vacuamente si `git` no responde

`subprocess.run(...)` sin comprobar `returncode`. La batería ya aprendió esta lección una vez y lo documenta: «una comprobación que sólo mira commits no protege el árbol que se le pone delante». Cerró la mitad y dejó abierta la simétrica: **un `git` que falla se interpreta como «nada cambió»**.

##### `M-13` · Sospecha propia REFUTADA, y consta

Sospeché que la entrada `owner_captado` que `PN-11` invoca para `O16` podía no existir. **Me equivoqué.** Está en `CHECKPOINT` L866–875, completa, con fecha, formulación presentada, cita literal y el descargo de que el párrafo largo no es del Owner.

```text
RECUENTO DERIVADO DE LAS FILAS, no escrito a mano
BLOQUEANTE   0
GRAVE        4   M-01 · M-02 · M-03 · M-04
MEDIO        3   M-05 · M-06 · M-07
MENOR        5   M-08 · M-09 · M-10 · M-11 · M-12
            ───
            12   consolidados · más M-13, sospecha refutada, que no es hallazgo
BLOQUEAN F5  3   M-01 · M-02 · M-03
```

#### 4 · Adjudicación de las trece condiciones por `M`

`C-L.1` **CERRADA** · `C-L.2` **CERRADA** · `C-L.3` **NO CERRADA** (`M-01`) · `C-L.4` **CERRADA EN LA FORMA, NO EN EL FONDO** (`M-07`) · `C-L.5` **CERRADA por su parte para lo que la condición dice**, abierta para el mínimo más amplio del checkpoint · `C-L.6` **CERRADA** · `C-L.7` **CERRADA**, con `M-06` como defecto nuevo del mismo fichero · `C-L.8` **CERRADA** · `C-L.9` **CERRADA** (46/46 derivado por él) · `C-L.10` **CONTRATADA PARA F6**, correctamente clasificada, cero líneas verificado · `C-L.11` **CERRADA** · `C-L.12` **CERRADA** · `C-L.13` **CERRADA, clasificación CORRECTA, sin doble conteo**.

> **Ninguna de las trece está mal clasificada.** Ese punto lo concedo entero: la clasificación del checkpoint es correcta, conservadora donde duda, y sin doble conteo. Lo que falla no es cómo se clasificó, sino que **una de las cinco que bloquean no está cerrada**.

#### 5 · Proporcionalidad

**Ninguno de mis doce hallazgos exige rediseñar arquitectura.** `M-01` son ~12 líneas más la corrección de `G-15`. `M-02` son cinco líneas, **pero es una decisión, y por eso no la tomo yo**. `M-03` es una fila en la lista de `fsync`, una ventana nueva y reescribir una justificación. `M-04` son dos comprobaciones reescritas. `M-05` a `M-12`, una línea cada uno.

**Y en la otra dirección, que también hay que decir.** No he contado como insuficiencia la ausencia de runtime, piloto, adaptadores certificados ni adopción de PesquerApp. Están declaradas con propietario y fase, y **están bien declaradas**. Verifiqué media docena en su sede. Eso es exactamente lo que F4 debe entregar, y lo entrega.

#### 6 · RECOMENDACIÓN DE VEREDICTO

##### INSUFICIENTE PARA F5

1. **`C-L.3` NO está cerrada.** `M-01`.
2. **Defecto arquitectónico nuevo en §2 que hace inemitible uno de los dos terminales.** `M-02`.
3. **Laguna de durabilidad con fallo silencioso en la única ruta de reversión.** `M-03`.
4. **La única garantía mecánica está refutada.** `M-04`, `M-11`, `M-12`.
5. **Tres sedes vigentes publican afirmaciones que el árbol contradice**, las tres introducidas o sobrevividas en la tanda que venía a cerrar esa misma clase de defecto. `M-05`, `M-06`, `M-07`.
6. **La cobertura no está cerrada en su totalidad.**

**Y lo que consta a favor.** `D96`–`D103` **no reescribieron ni una línea** de `D1`–`D95` ni de `O1`–`O16`: 121 inserciones, cero borrados, verificado con `git`. Diez de las trece condiciones están cerradas donde dicen estarlo. Ninguna está mal clasificada. La procedencia de `O16` es, en lo que atribuye, de una honestidad poco frecuente. `PN-15` está bien construida y su negativa a decidir es la correcta. `J-11` está declarado como no implementado y **lo está de verdad**. Mi propia sospecha sobre `owner_captado` era falsa y lo he escrito. **Ésta es, con distancia, la candidata más sólida que este corpus describe haber producido — y sigue sin ser suficiente**, porque tres de las razones son defectos arquitectónicos abiertos en §2 y §19, y ninguno existía antes de la tanda que venía a cerrar los anteriores.

---

## 5 · Dictamen literal del REVISOR N

> Transcrito **sin suavizar y sin resumir cambiando el sentido**. Lo emitió `N`; el
> coordinador sólo lo transcribe.

**Ámbito:** capacidades, procesos, diseño, entrada, contratos `C2`/`C3`/`C4`, enmiendas `E1` y `E2`, y el documento 15.
**Árbol:** `db26b4d1898b17ce66f89ea3bb25f817c7c1d6c3`, commit `c3d6465a…`. **Modo sólo lectura, comprobado:** `git status --porcelain` vacío al abrir y al cerrar, tras ejecutar `comprobar_recuentos.py` y la batería. Mis únicas escrituras fueron en el scratchpad, fuera del árbol.

**Los cuatro hashes del bloque común coinciden byte a byte con los declarados**, y verifico los dos totales: bloque común **8 735** líneas y lote propio **5 799**, ambos exactos por `wc -l`. *(El desglose del encargo dice «1 729 en total» para las quince fichas; los quince recuentos individuales que enumera son todos correctos y suman **1 829**. El total del lote, 5 799, está calculado con 1 829 y es el correcto. Es una errata aritmética del propio encargo, sin consecuencia.)*

#### 1 · Evaluación propia provisional, y qué cambió

Guardé una evaluación provisional **antes** de abrir los documentos 15–18 y `ADS-PENDIENTES`. Su núcleo: **derivación propia de `<CAP>:revision` hecha a ciegas — nueve pares en cinco procesos**, `FEA(DOM,SEG)`, `GAP(DOM,SEG)`, `INC(SEG)`, `DEU(DOM,SEG)`, `DEP(DOM` condicional`, SEG` por la obligatoria`)`. **Coincidía exactamente con lo publicado.**

Qué cambió después de leer el bloque común:

1. **`P3` se transformó en el hallazgo principal y subió de MEDIO a GRAVE.** La lectura de `b.3` y `b.5` —que el adjudicador `I` declaró expresamente no haber abierto como única refutación posible de `I-08`— no refuta nada; y al derivar qué procesos declaran `VER` descubrí que **`proceso:AUD` no tiene `VER`**, lo que convierte el Nivel B en insatisfacible por posición, no sólo por objeto.
2. **`P2` ganó una tercera sede**: §8.0 del documento 11, L5711–5712, dice «en **`AUD` y `DIR`** se DERIVA del encargo — nunca se asigna a mano». Son tres sedes concordantes contra §19.
3. **`P1` se reformuló a la baja** en su consecuencia: el resultado de hoy (9/5) es correcto, y el defecto es de robustez futura.
4. **`P4` se corrigió a la baja:** mi primer `grep` era demasiado estrecho y me hizo creer que (a) no llevaba ninguna marca. Lleva seis.
5. **Aparecieron dos hallazgos nuevos** que la lectura del bloque común hizo visibles (`N-04`, `N-05`).
6. **Tres sospechas más se cayeron al verificarlas.**

#### 2 · Declaración de cobertura

**Leído íntegro, sin excepción:** las cuatro fuentes del bloque común (**8 735 líneas**) y las diecisiete entradas de mi lote propio (**5 799**), incluidas **las quince fichas de capacidad completas** y **`ADS-PENDIENTES` entero, con los BLOQUES B y C**. Total: **14 534 líneas**. Método: `cat -n` y `sed` por tramos consecutivos que cubren todas las líneas, sin saltos. **No he sustituido lectura por `grep` en ninguno de los veintiún ficheros obligatorios.**

**Lo que NO he cubierto, sin adorno:** `11-ARQUITECTURA-INTEGRADA.md` **no está leído íntegro**; no he leído `C1`, `C5`, `C6`, `C7`, `circuitos/`, `entrada/01`/`03`/`05`, `diseno/03`, `packs/`, `tooling/`, `pruebas/`, ni dieciocho de los diecinueve esquemas; no he leído los ~150 ficheros de `roles/`, `metodos/`, `prompts/` y `composicion.md` —comprobé mecánicamente que existen y se corresponden uno a uno con lo que cada ficha declara, **pero eso no es lectura**—; no he leído (a) ni (b) íntegros, salvo `b.3` y `b.5` completas. **Nada de esto está construido**, y todos mis hallazgos son sobre texto.

**Lo que mi cobertura sí cierra:** las **catorce fuentes** del `C-0.1` del documento 18 —incluido **el documento 15**— y el `C-0.2` —**las quince fichas íntegras**—, más `ADS-PENDIENTES` completo con sus BLOQUES B y C. Es exactamente lo que el adjudicador `I` declaró que no podía resolver y lo que `C-L.5` exige.

#### 3 · HALLAZGOS

##### `N-01` · **GRAVE** · El NIVEL B prescribe, para `proceso:AUD`, una participación cuya posición declarada no existe en ese proceso; y deja fuera `proceso:DIR`, que es donde sí existiría

`11`:8763–8764, paso 5 del algoritmo:
> «para cada par exigido, EXIGIR la participación `<CAP>:revision` **posterior a `VER`** en el mismo proceso»

`11`:8803–8804, contraejemplos:
> «un proceso con `<CAP>:revision` colocado ANTES de `VER` → FALLA: **la posición es parte del contrato, no un detalle**»

`b-RECORRIDO-APROBADA.md` L836:
> «`<CAP>:revisión` **tras VER** revisan lo construido.»

`01-PROCESOS.md` L420–427, `proceso:AUD`, `obligatorias` completas: una sola, `conclusion-fundada`, `capacidad_productora: "INV"`. **No hay `VER`.**

**Derivación mecánica propia** de qué procesos declaran `VER`:

```text
FEA SÍ · GAP SÍ · DEF SÍ · INC SÍ · DEU SÍ · DEP SÍ · DIR SÍ · SIS SÍ
INV NO · AUD NO          ← los dos únicos sin VER
```

En tres pasos que no admiten lectura alternativa: `<CAP>:revision` está definido **por su posición, tras `VER`**, y §19 convierte esa posición en contraejemplo de fallo; **`proceso:AUD` no declara `VER`**, y no es un olvido de F4 sino un hecho de `b.16` registrado como **`PN-8`**, presión viva que va al Owner en F5; luego el NIVEL B, aplicado a un item `AUD` cuyo propietario resuelva a `DOM` o `SEG`, **exige una participación que no tiene dónde colocarse**. **§19 no lo dice en ninguna línea** — lo comprobé barriendo `VER` en las 250 líneas del apartado.

**Y el error simétrico.** `proceso:DIR` **sí** tiene `VER` (obligatoria `decision-verificada`, `capacidad_productora: "VER"`) **y** propietario derivado —«la capacidad PROPIETARIA de la decisión que se sustituye»—, que puede resolver a `DOM` o a `SEG`. **§19 lo excluye de los dos niveles** y lo declara estáticamente vacío: `11`:8781–8782, «`INV`, `DIR`, `SIS`, `DEF` sin participación de `DOM` ni de `SEG` → **PASAN VACÍOS**». Esa afirmación no es derivable. **Los dos tratamientos están exactamente invertidos respecto del ancla que la norma usa.**

**Causa, verificada.** El discriminante entre NIVEL A y NIVEL B es, en el texto y en la implementación (`if "DERIVADO" in pg.group(1).upper()`), **la presencia de la palabra «DERIVADO» en un campo de prosa libre**. Demostrado con dos fixtures sobre el árbol real:

```text
árbol real                                 9 pares · 5 procesos · dinámicos {AUD}
AUD reformulado sin «DERIVADO»,
mismo significado                         11 pares · 6 procesos · dinámicos {}
DIR reformulado con «DERIVADO»,
mismo significado                          9 pares ·             dinámicos {AUD, DIR}
```

Es la misma clase de defecto que `K-02` demostró y que `D98`→`D103` declara retirada. El barrido léxico no volvió a `capa_exigida` ni a `condicion` —eso es cierto y lo verifiqué—: **migró a `propietario_global`**, que §19 presenta como campo estructurado y que en tres de los diez procesos es prosa libre.

**Por qué es GRAVE y no BLOQUEANTE.** El NIVEL A —los nueve pares— **es correcto y lo reproduje independientemente**. El error no cambia ninguna cifra del árbol de hoy. Pero el contrato se entrega a F6 con la afirmación de que no queda nada por decidir, y quedan dos cosas: qué revisa una `DOM:revision` en un proceso sin `VER` y sin `CON`, y si `DIR` está dentro o fuera.

**¿Bloquea F5? Sí.** No por su tamaño, sino porque **esconde una decisión arquitectónica todavía abierta bajo una declaración de que no la hay**, y es la tercera vez que la misma cláusula se corrige y la tercera vez que el remedio no alcanza.

**Qué lo cerraría** — cualquiera de las tres, y ninguna exige decidir arquitectura nueva:
1. **Retirar el NIVEL B** y declarar que `AUD` y `DIR` pasan vacíos **por la misma razón**, que existe y está escrita: ninguno de los dos activa `CON`, luego no hay «lo construido» que revisar. El contrato queda en un solo nivel y **derivable sin mirar prosa**.
2. **Conservar el NIVEL B** condicionando su aplicabilidad en `AUD` a la resolución de `PN-8`, y **añadir `DIR`**.
3. **Sustituir el discriminante léxico** por uno estructural.

##### `N-02` · **MEDIO** · El NIVEL A se declara derivado «de campos ESTRUCTURADOS», y uno de los tres no lo es en tres de los diez procesos

`11`:8737–8740: «**SÓLO campos ESTRUCTURADOS**, tres y nada más: `condicionales[].capacidad` · `obligatorias[].capacidad_productora` · **`propietario_global`, resuelto para el item**».

`esquemas/proceso.yaml` L23: `propietario_global: {tipo: texto, min: 3}` — **texto libre**. Y tres de los diez lo llevan en prosa: `DEF` L154, `AUD` L419, `DIR` L458.

Llamar «estructurado» a un campo `tipo: texto` que en tres de diez casos contiene una frase condicional es lo que permite que el clasificador de `N-01` tenga que leer prosa. **No es un hallazgo nuevo en su raíz** —es `F-02`—, pero `F-02` **no incluye `propietario_global`** en su remedio, y es el campo del que depende la partición.

##### `N-03` · **MENOR** · `E1.4` declara siete marcas de remisión en (a) y hay seis, tres de los cinco recuentos quedan sin marcar, y la cifra se repite en dos sedes más

`E1` L196–197: «**siete** MARCAS DE REMISIÓN `[E1]` insertadas en línea … **cinco recuentos y dos párrafos**». `grep -o '\[E1[^]]*\]'` sobre (a) devuelve **seis**. Recuentos de «14» sin marca: **dos** —L269 «Las **14** son el **catálogo base**» y L276—.

`E1.4` **es** el mecanismo por el que la enmienda alcanza a un lector de (a). Un lector que llegue a L269 o L276 lee «las 14» sin ninguna señal de que el catálogo está enmendado a quince. **No cambia ninguna norma**, pero es una cifra derivada escrita a mano y falsa, **en el apartado cuya función es la trazabilidad**, y repetida en `CORRECCIONES-POST-AUDITORIA.md` L53 y L218. Es la décima ocurrencia de la clase que el expediente lleva nueve tandas persiguiendo.

**Dónde va.** (a) y `E1` son material **APROBADO**. Su sitio es **la checklist de F5**, junto a `E5-1` y `E5-2`. **No está en ella:** la checklist (`11`:8608–8611) sólo lleva las dos filas de (b).

##### `N-04` · **MENOR** · El documento 17 publica dos cifras contradictorias sobre el mismo objeto de mi lote, y nada las contrasta

Doc 17, evidencia del revisor `D`, fila `C2`: «**22** bloques `ads:perfil-agente`». Doc 17, evidencia del revisor `E` y su método: «**21**». `grep -c '^id: perfil:'` sobre `C2` → **21**, en `HEAD` **y** en `7c7856c`, que es el árbol sobre el que se escribió el documento 17. Los enumeré uno a uno. **Son 21.**

`C2` es una de las catorce fuentes que nadie había abierto, y el documento 17 es **el documento que declara haberla cerrado**. Los dos revisores que la leyeron publican cifras distintas, y **el adjudicador `F` no lo detectó**. Nada mecánico lo habría atrapado: **`RECUENTOS-generado.md` no cuenta los perfiles de agente**, pese a contar composiciones, gates, rúbricas, vetos, formas, niveles y clases. Verifiqué: las veinte cifras que sí publica cuadran todas; ésta no existe. Cierre: una línea, y encaja en `C-L.10`.

##### `N-05` · **MENOR** · El calificativo del principio de `U` difiere entre los dos documentos de trabajo del Owner, y `F-09` se resolvió contrastando sólo uno

`ADS-PENDIENTES` L914–916 (§7): «**Principio aceptado:** > **Detectar automáticamente; actualizar conscientemente.**» `11`:6470–6474 cita `IDEAS` §3 L79, «donde está el calificativo **principio PROVISIONAL**». `F-09` se resolvió por comparación con **un** documento; **existe un segundo**, en `docs/evolucion/`, que llama al mismo principio «aceptado». Los dos son no normativos, así que **ninguna norma cambia**; pero la afirmación «lo escribe así» es exacta para la fuente que cita e incompleta para el corpus. **La sustancia de `F-09` sigue siendo cierta**, y lo verifiqué.

#### 4 · Hallazgos que intenté y NO pude reproducir

> Los publico porque un dictamen que sólo enseña sus aciertos no es una medida.

| qué sospeché | qué encontré | resultado |
|---|---|---|
| Un **método huérfano** en `SEG`: dos métodos y un solo rol | `SEG/composicion.md` L27–37 asigna `SEG/condiciones` a ese método. **Un rol ejecuta los dos** | **NO REPRODUCIDO** |
| Que `E1` **no pusiera ninguna marca** en (a) | Usan `[E1 → 15]`, `[E1: quince]`, `[E1 confirma: …]`. **Son seis**, no cero. Mi patrón era estrecho | **CORREGIDO.** Sobrevive reducido en `N-03` |
| Que `C3` descuadrara: 17 elementos y 19 campos | `C3` L11–13 lo explica: la tabla lista 17 porque incluye `modo`, subcampo de `pasos`, y no los tres de identidad. **Cuadra** | **NO REPRODUCIDO** |
| **Enlaces rotos** en mi lote | Barrí todos los enlaces relativos `.md` y `.yaml` de los veintiún ficheros: **cero rotos** | **NO REPRODUCIDO** |
| **`roles: 42`** inflado: sólo 36 ficheros de rol | El generador cuenta **bloques `ads:rol`**, y **`packs/` aporta 6**. 36+6 = **42**. `T151` **SUPERADA** | **NO REPRODUCIDO** |
| §26.22–§26.26 de `ADS-PENDIENTES` **sin registrar** | Lo resolvió **F3**: `09-SINTESIS.md` L714–716, «ACEPTADA el principio · RECHAZADO el fichero nuevo», «FUSIONADA», «ACEPTADA». `exclusiones.yaml` L113 lo cita | **NO REPRODUCIDO** |
| Que F4 **contradijera al Owner** sobre quién abre una campaña | `11`:4872–4875 parte la materia con argumento: la **abre** la capacidad responsable, y **«`DSP` la compone y la despacha»**. Conserva lo que §20.14 pide | **NO REPRODUCIDO. F4 tiene razón** |

#### 5 · Verificaciones mecánicas que salen limpias

| comprobación | resultado |
|---|---|
| las quince fichas ↔ ficheros de `roles/`, `metodos/`, `prompts/` | **coinciden una a una**, sin sobrantes ni ausencias |
| los 21 perfiles de `C2` ↔ los `perfil_agente` de los 42 roles | **los 21 usados; ninguno referido que no exista** |
| orden de las 10 composiciones de `DIS` ↔ ejemplo de `C4` | **idéntico** |
| 12 bloques `ads:memoria` ↔ 12 ficheros ↔ «doce secciones» | **12 = 12 = 12** |
| `RECUENTOS-generado.md`, veinte cifras derivadas por mí | **veinte de veinte cuadran** |
| enlaces internos de todo mi lote | **cero rotos** |
| `T151` ejecutado | **SUPERADA**, árbol limpio después |

#### 6 · Lo que aporta mi lote y nadie más tenía

**BLOQUES B y C de `ADS-PENDIENTES`: los dos CONFIRMAN. Ninguno contradice. Ninguno agrava.** Es la conclusión más importante de mi lectura, porque tres gates declararon no haberlos abierto.

**BLOQUE B (certificación por niveles) → confirma §9 de F4, casi literalmente.** Los cuatro niveles coinciden; las definiciones de «Integrado» y «Completo» son **verbatim**; la REGLA DURA de §988 —«no se declara un nivel superior por argumento ni porque pase el anterior»— está en §9.2 **y F4 la endurece** con `NIVEL ALCANZADO` derivado; los cinco participantes de §11 aparecen; y §1000–1001 —«SIS no puede ser el único productor y único crítico de su propia instalación»— queda **cumplido**: tres de los cuatro niveles tienen a `VER` independiente como crítico y el nivel Integrado tiene a `PLT` de propietario.

**BLOQUE C (iniciativa y dosier vivo) → confirma §3.3, y F4 no toma ninguna decisión que fuera del Owner.** Recorrí las **doce decisiones pendientes** de §17 una a una contra §3.3: **once resueltas con fuente citada** —el nombre lo decide `O11`, resolución del Owner con fecha; el dosier derivado coincide con §15; el umbral reduce las nueve señales a una **citando el §16 por número**—, y **la única que F4 decide por su cuenta —prohibir la anidación— está argumentada** y es legítima porque el documento se autodeclara no normativo.

**`b.3` y `b.5` leídas íntegras: la refutación de `I-08` NO EXISTE.** El adjudicador `I` dejó escrito: «la refutación posible vive donde no he mirado. **Si apareciera, `I-08` caería**». `b.3` (L101–176) y `b.5` (L272–304) no mencionan `<CAP>:revisión` en ninguna línea; un barrido de `revisi` sobre (b) devuelve **una sola aparición normativa**, L836, sin calificativo de ilustratividad. Y `b.3` L131–133 **refuerza** `I-08`. **`I-08` no cae. Queda cerrada esa vía de escape.**

**Las fichas de `DOM` y `SEG` declaran la segunda participación como salida propia** —`DOM` L14–15, L17, L51; `SEG` L13–15, L22, L51— **y los diez procesos instancian cero.** Confirma `I-08` desde una sede que el gate del documento 18 no leyó.

**`PN-13` verificada de forma independiente:** `proceso:SIS` declara exactamente dos condicionales y `proceso:INV` cuatro, **sin `DOM`, `SEG` ni `DIS`**. La presión es un hecho, no una opinión.

**`G-24` no cierra la cobertura**, y el corpus lo declara bien: `verificacion/README.md` L97–101 dice «**ninguna comprobación mecánica la sustituye**». Lo consigno porque el rótulo «se LEEN» admite leerse como que la cobertura queda cerrada, **y no queda: la cierra una lectura**, y por eso existe este dictamen.

#### 7 · Adjudicación de `N`, sólo lo que toca su lote

**`C-L.3` PARCIALMENTE CERRADA** — NIVEL A cerrado y bien, NIVEL B abierto · **`C-L.5` CERRADA por su parte**, cerrando las catorce fuentes de `C-0.1`, las quince fichas de `C-0.2` y el documento 15 · **`C-L.12` CERRADA** · **`C-L.13`·`K-09` CERRADA** · **`K-10` CERRADA** · **`L-03` CERRADA** · **clasificación MIXTA CORRECTA, sin doble conteo**. Las nueve restantes **fuera de su lote: no las adjudica**.

#### 8 · RECOMENDACIÓN DE VEREDICTO

##### INSUFICIENTE PARA F5

1. **`N-01`, GRAVE.** El contrato se entrega a F6 declarando que «F6 MATERIALIZA; no elige la forma», y **la premisa vuelve a estar rota en la misma cláusula**.
2. **`N-02`, MEDIO, que es la causa mecánica del anterior.** El barrido léxico **migró de `capa_exigida` a `propietario_global`**. Tercera reaparición de la misma clase en la misma cláusula.
3. **`C-L.3` no está cerrada.** Su NIVEL A sí, y lo confirmo con derivación independiente. Su NIVEL B no. **Una condición de cierre no se satisface a medias.**
4. **La regla general de cobertura del gate sigue sin cumplirse.** Cierro `C-L.5` por mi parte y contesto las dos preguntas que `I` declaró irresolubles. Pero **`11-ARQUITECTURA-INTEGRADA.md` sigue sin lectura íntegra por nadie, yo incluido**.
5. **Y una razón que es del método.** Los tres remedios sucesivos de la misma cláusula han fallado cada uno por la misma causa, la inferencia sobre texto libre, sólo que en un campo distinto cada vez. **Cerrar aquí sería premiar el patrón.**

> **Si alguien graduara `N-01` como MEDIO en vez de GRAVE, mi veredicto no cambiaría, porque `C-L.5` lo determina por otra vía.**

**Y lo que quiero que se lea junto al veredicto.** Nada de lo que exijo requiere una decisión nueva del Owner. `N-01` tiene tres salidas escritas y **la más barata reduce el contrato**. Los cuatro hallazgos restantes suman menos de una página. Y lo que leí de mi lote —las quince fichas, el sistema de diseño, la puerta de entrada, los tres contratos y las dos enmiendas— **es material profesional, internamente coherente en las veinte cifras que derivé**, con sus límites declarados con propietario y fase, y **no contradice ni agrava nada de lo corregido**. Los BLOQUES B y C que tres gates no abrieron **confirman** a F4, y `b.3` y `b.5` **no refutan** `I-08`: esas dos vías de escape quedan cerradas y nadie tiene que volver a mirar ahí.

---

## 6 · Adjudicación literal del ADJUDICADOR O

> Transcrita **íntegra**. Incluye la adjudicación de los diecisiete hallazgos de `M` y `N`,
> sus cuatro hallazgos propios, las cifras que derivó, las cinco discrepancias y su
> resolución, la adjudicación de las trece condiciones y el veredicto.

**Modo.** `git status --porcelain` vacío ANTES y DESPUÉS. Ni un fichero modificado, ni un commit, ni una escritura de git. Todas las reproducciones en el scratchpad, fuera del repo.

**Qué NO soy.** No escribí F4, ni `F4b`, ni `F4c`. No apliqué `D16`–`D103`. No soy autor de ninguna corrección post-gate. No fui revisor `A`–`N`. Recibí los dictámenes ya cerrados; ninguno vio el del otro. **No he corregido nada. Adjudico y devuelvo.**

#### 1 · Qué verifiqué yo mismo y qué acepté sin verificar

**Verificado por mí, contra fichero y línea o mecánicamente:** estado del repositorio y del rango · SHA-256 y líneas de las cuatro fuentes · `D1`–`D103` serie continua · `O1`–`O16` · el diff del registro · `D67` idéntica a `7e99388` · documentos 15–18 intactos desde `0ea0451` · las quince cabeceras `PN` y las trece vigentes · las 46 filas y 46 ids de §2.6.7 y el desorden de `X58` · las 43 filas de la matriz y sus cinco estados · quince capacidades, diez procesos, diecinueve esquemas, cero instancias de `:revision` · **la derivación completa de `<CAP>:revision`, a mano y mecánicamente** · el texto íntegro del algoritmo de §19 · `esquemas/proceso.yaml` · `a.6` L495/L502–503/L504–505 · `b.16` L832–836 · **los cuatro eslabones de la circularidad de `M-02` y la ausencia de sede que la resuelva** · la lista de `fsync`, las diecisiete ventanas y el paso 0 · `PN-15` íntegra y la fila de §17 · el bloque «excepción exacta del kernel» contra `git diff` · las fechas de `O16` · la batería en el árbol real y **sus cuatro refutaciones reproducidas** · las seis marcas `[E1]` · los 21 perfiles de `C2` · el único `:revisi` normativo de (b) · `J-11` con cero líneas · `AFIRMACIONES` todavía a mano.

**Aceptado sin verificación independiente, y lo digo:** `C-L.6` y `C-L.8` · las correcciones de `K-05`, `K-10`, `K-08` y `L-03` · diecinueve de los veinte recuentos que `N` deriva · la correspondencia de las quince fichas con `roles/`/`metodos/`/`prompts/` · los cero enlaces rotos · `D91` · la reproducción de `A14` por `M`. **Donde escribo «verificado», lo abrí. Donde no, lo digo.**

**Lo que no juzgo, por instrucción y porque está bien declarado:** runtime, piloto, adaptadores certificados y adopción de PesquerApp. **Comprobé que están bien declarados** y **no los uso como motivo de insuficiencia**.

#### 2 · Cifras que derivé

```text
DECISIONES        D1–D103, serie continua, sin huecos ni repeticiones      103
RESOLUCIONES      O1–O16, sin huecos                                        16
PRESIONES         15 cabeceras · PN-4 RETIRADA · PN-5 FUSIONADA → 13 vigentes
TABLA ADVERSARIAL 46 filas / 46 ids, con `X58` fuera de orden entre `X61` y `X62`
MATRIZ DE LOS 43  43 filas / 43 ids · 31 · 2 · 2 · 7 · 1 = 43
                  por severidad: BLOQUEANTE 4 · GRAVE 6 · MEDIO 20 · MENOR 13 = 43
GATE DEFINITIVO   1 + 6 + 10 + 7 = 24 consolidados + 1 rechazado = 25
CORPUS            capacidades 15 · procesos 10 · esquemas 19
                  instancias `:revision` en kernel/operativo/  =  0
REGISTRO          diff 652ab8e..HEAD sobre DECISIONES: 121 inserciones · 0 SUPRESIONES
                  → ninguna fila D1–D95 reescrita; O1–O16 intactas
                  D67 idéntica byte a byte a la de 7e99388
INMUTABLES        documentos 15, 16, 17 y 18: sin cambios desde 0ea0451
BATERÍA           30/30 en verde sobre el árbol real
```

**Mi derivación de `<CAP>:revision`:**

```text
proceso  propietario_global        DOM              SEG
FEA      PRD       (fijado)        condicional      condicional
GAP      PRD       (fijado)        condicional      condicional
DEF      ARQ/CON   (fijado, prosa) —                —
INC      ENT       (fijado)        —                condicional
INV      INV       (fijado)        —                —
DEU      ARQ       (fijado)        condicional      condicional
DEP      PLT       (fijado)        condicional      OBLIGATORIA
AUD      DERIVADO  (L419)          condicional C-DOM  condicional C-SEG
DIR      DERIVADO  (L458)          —                —
SIS      SIS       (fijado)        —                —

NIVEL A · CINCO procesos · NUEVE pares · (DEP,SEG) por la obligatoria
NIVEL B · AUD, resuelto por item. DIR también lo es y §19 NO lo trata así
```

**Coincide exactamente** con la proyección publicada, con la salida de `G-15` y con la derivación del coordinador. **La cardinalidad publicada es correcta. Lo que no lo es, es la regla que la produce.**

#### 3 · Adjudicación de los hallazgos de `M`

**`M-01` · CONFIRMADO · GRAVE · defecto arquitectónico de F4c.** Verificado en las cuatro sedes que `M` cita y en una quinta que añado. El criterio nombra **cuatro** vías; el paso 3 excluye `AUD` entero; el paso 4 **no mira los condicionales** —verificado en el código: `_exige_por_item(propietario)` no abre el bloque del proceso—; `AUD` sí declara `DOM` y `SEG` como condicionales con `C-DOM` y `C-SEG`, confirmado en material APROBADO por `b` L895; y `D98` lo había nombrado. **Consecuencia:** el contrato **no dice** si un item `AUD` con propietario `PRD` que active `C-DOM` y `C-SEG` debe llevar revisión. Si es correcto que no, la razón sería la segunda mitad del criterio, que `D103` prohíbe evaluar por análisis de texto y que NIVEL A ignora. **F6 tendría que decidirlo.** Confirmo también que `C-L.3` queda sin cerrar por esta vía: su condición literal exige operar «cualquiera que sea su vía», y no lo hace.

**`M-02` · CONFIRMADO ÍNTEGRO · GRAVE · defecto arquitectónico de F4c.** Es el hallazgo más grave del expediente, y verifiqué sus cuatro eslabones uno a uno: el orden del paso E (`abandonada` va primero); `deriva_emitida` en la celda de **campos OBLIGATORIOS**, no condicional; `predecesor` incluido en el `id` y definido como el último evento observado; y la circularidad que resulta. **Ninguna sede la resuelve:** `grep -n 'circularidad\|circular'` devuelve seis líneas —dos sobre la circularidad del `id` consigo mismo, que §2.8 sí cierra, tres sobre `T158` y una sobre `D37`—. **Ninguna toca ésta.** Y §2.8 dice del caso que sí cerró: «incluirlo es **la circularidad que F4c no resolvía**». `abandonada` es uno de los dos terminales y el único que revierte sin publicar mezcla parcial; toda la línea `D64`→`D69`→`D73`→`D79` descansa en él. **Como está especificado, no se puede emitir.** Las tres salidas son tres decisiones, y la tercera choca con la comprobación B de la fila 3, que exige resolver `deriva_emitida` a un evento concreto. **F6 no puede materializar §2.6.9 sin decidir arquitectura.**

**`M-03` · CONFIRMADO · GRAVE · defecto arquitectónico de F4c.** Verificados literalmente la lista de `fsync` —el evento `deriva` no está en ninguna de las dos—, la prohibición de reemitir del paso 0, y la justificación de exhaustividad, **que es falsa hoy**: tras `D78`/`D88` el paso E produce **cinco efectos, no uno**. Recorrí `W1`–`W16`: **ninguna cubre la caída entre el `abandonada` durable y el `deriva`**.

**`M-04` · CONFIRMADO · GRAVE.** **Reproduje las cuatro refutaciones yo mismo, sobre copias del árbol. El repositorio no se tocó.** Refutación 1: leí `_participaciones()` —lee dos campos y nada más— y `_derivar_catalogo()` —usa `propietario_global` **sólo** para ramificar—; fixture `proceso:SIS` con propietario `DOM` → **`G-15` en verde**, sin par nuevo; `29/30`. Refutación 2: `re.search` toma la primera coincidencia y **no comprueba unicidad**; inyecté la segunda proyección → **`30/30` en verde**, con `G-15` marcada OK, sobre **el contraejemplo exacto que el propio contrato declara que la prueba tiene que suspender**. Refutación 3: moví `C-L.12` de estado ajustando contadores → **`30/30` en verde**, mientras el checkpoint declara `C-L.12` corregida en L888 y **REGISTRADA PARA F5 en L941**, catorce líneas más abajo, contradiciendo al documento 19. `G-16` comprueba la coherencia interna del bloque y **nunca contrasta contra el detalle ni contra la fuente**. Refutación 4: reproducida **exactamente como `M` la describe, cifra incluida: 29/30**. Y confirmo su añadido: `_COMPONENTES_CL13` es una lista literal escrita a mano dentro de la comprobación cuyo objeto es la disciplina que `D102` contrata para retirar los censos enumerados.

**`M-05` · CONFIRMADO · MEDIO · autoinfligido.** Comprobé el primer disyunto: `grep 'G2[0-3]'` sobre (a) devuelve una línea, y es la ficha de `INV`, no una fila derogatoria. Correctamente ausente. **Agravo respecto de `M`, y es mío:** no es una cifra arrastrada de otra tanda — **la fila de §17 la escribe `D97`, la misma decisión que escribe `PN-15`, en el mismo commit** — y el propio cuerpo de `PN-15` lo dice en pasado: «Y §17 **no tenía fila para `kernel/KERNEL.md`**». El documento sabe que la fila existe ahora y aun así declara su prueba infalible en verde. **Es una contradicción dentro de una sola decisión.**

**`M-06` · CONFIRMADO · MEDIO.** Derivado por mí: son **cuatro rutas distintas de kernel más la evidencia derivada, no tres**, y la cuarta es kernel operativo **sustantivo**, nombrada en `DOC_AUTORIZADO` de la batería. **Se corrigió el código y no el checkpoint**, que es la sede que lee un agente sin contexto.

**`M-07` · CONFIRMADO · MEDIO.** Derivado con `git log -S`. Verifiqué las dos sedes y **ninguna reconcilia las fechas**. Adopto la precisión de `M` sin rebajarla: **no afirmo que el Owner no confirmara ni que la cita sea falsa.** La resolución existe y ahora es atribuible; lo que no está es la reconciliación.

**`M-08` · CONFIRMADO · MENOR.** Conté sobre el fichero: la frase está en **L502–503**; **L504–505 dice otra cosa**. El documento 18 la cita en L504-505 y `D92`/§19 heredaron la cita; `D98` y §19 L8653 citan la correcta. **Dos citas de la misma frase, a veintiséis líneas, conviviendo.**

**`M-09` · CONFIRMADO · MENOR.** `grep -n ':revisi'` sobre (b) devuelve **una sola línea**, L836, **con tilde**. Todo el aparato de F4, la prueba prescrita y la salida de error escriben `revision` **sin tilde**. Hermano exacto de `F-01`, que sí se registró como presión.

**`M-10` · CONFIRMADO · MENOR.** Derivé el orden: `… X57 X59 X60 X61 **X58** X62`.

**`M-11` · CONFIRMADO · MENOR.** Un valor capturado por `[A-Z_0-9]+` **no puede contener espacio ni `+`**. Código muerto: nunca puede disparar.

**`M-12` · CONFIRMADO · MENOR.** Reproducido, con la cifra exacta.

**`M-13` · CONFIRMACIÓN DE SU REFUTACIÓN.** La entrada existe y la abrí: `CHECKPOINT` L866–875, completa. **Lo publica pese a no serle favorable, y eso es un dato del gate.**

#### 4 · Adjudicación de los hallazgos de `N`

**`N-01` · CONFIRMADO EN SUS DOS MITADES · GRAVE · defecto arquitectónico de F4c.**
*Mitad A:* derivación mía sobre los diez procesos — declaran `VER` ocho; **`INV` y `AUD` son los dos únicos que NO**. `proceso:AUD` tiene **una sola obligatoria**, `capacidad_productora: "INV"`. El NIVEL B, que existe **exclusivamente para `AUD`**, exige una participación **que no tiene dónde colocarse**, y tenerla dependería de `PN-8`. **§19 no lo dice en ninguna línea. Lo busqué.**
*Mitad B:* `proceso:DIR` **sí tiene `VER`** —obligatoria `decision-verificada`, «nadie: un DIR no cierra sin `VER:decisión`»— y su propietario **también es derivado**. **Dos sedes lo confirman, y las abrí las dos:** `esquemas/proceso.yaml` L22 —«en **DIR y AUD** el propietario se DERIVA»— y §8.0 L5711–5712. **§19 lo excluye de los dos niveles** colocándolo entre los casos positivos de NIVEL A, y la afirmación **no es derivable** del propio algoritmo.
**Confirmo la severidad GRAVE**, y registro su precisión: si alguien la graduara MEDIO, su veredicto no cambiaría. **El mío tampoco.**
**Corrijo una imprecisión de `N`**: cita `a.6` L504–505 en su mitad B; la frase está en **L502–503**. El hallazgo sobrevive intacto.

**`N-02` · CONFIRMADO · MEDIO.** `esquemas/proceso.yaml` L23 verificado en el fichero: **texto libre**. Tres de los diez lo llevan en prosa, y los abrí. `F-02` tipa `capacidad` y `capacidad_productora` y **no incluye `propietario_global`**. **Es la causa mecánica de `N-01` y de la mitad de `M-01`: la partición entre los dos niveles se decide sobre una cadena de texto libre no tipada.**

**`N-03` · CONFIRMADO · MENOR.** Conté las marcas yo mismo: **SEIS** (L26, L89, L219, L226, L261, L285; L16 y L18 son cabecera y tabla, no marcas). `E1` L196 declara **siete**. Confirmo los dos recuentos sin marcar, L269 y L276, y la repetición en `CORRECCIONES-POST-AUDITORIA.md` L53 y L218, verificadas por número de línea exacto. **Y confirmo la observación que la hace pertinente**, porque la abrí: la checklist de F5 lleva **exactamente dos filas**, ambas de (b). **(a) y `E1` no están en ella, siendo material APROBADO igual que (b).**

**`N-04` · CONFIRMADO EN EL HECHO, CON LA CITA CORREGIDA · MENOR.** Conté: **21**. El documento 17 dice 22 **en L116, no en L60**, que es la fila del inventario. **Corrijo la referencia; el hecho es exacto.** `RECUENTOS-generado.md` **no cuenta los perfiles**: `grep 'perfil'` devuelve vacío. Encaja en `C-L.10`.

**`N-05` · CONFIRMADO · MENOR.** Abrí las dos sedes: `IDEAS` L79 «**Principio provisional:**» y `ADS-PENDIENTES` L914 «**Principio aceptado:**», con la **misma frase literal**. Ninguna norma cambia. **La sustancia de `F-09` sigue siendo cierta.**

**Las verificaciones de `N` que confirmo por mi cuenta.** `grep -n 'revisi'` sobre (b) devuelve cuatro líneas y **una sola aparición normativa, L836, sin calificativo de ilustratividad**. El adjudicador `I` dejó escrito que «si apareciera, `I-08` caería». **No aparece. `I-08` no cae.** `PN-13` es un hecho, derivado por mí. Los BLOQUES B y C confirman a F4: sondeé cuatro puntos y **no encontré nada que contradiga o agrave las correcciones aplicadas**.

#### 5 · Mis propios hallazgos

**`O-01` · MEDIO · la vía PROPIETARIA no está implementada en ningún nivel.** `M` lo encontró como refutación de la batería; **lo elevo a defecto del contrato**. DATOS DE ENTRADA nombra `propietario_global` con el calificativo «resuelto para el item», que lo ata a NIVEL B; el paso 3 emite «un par por cada participación estructurada» sin decir si un `propietario_global: "DOM"` fijado lo es; y **la prueba prescrita resuelve la ambigüedad en negativo**, demostrado con fixture en verde. Hoy ningún proceso tiene `DOM` o `SEG` como propietario fijado, luego el hueco es **latente**. Pero **el criterio nombra cuatro vías, el aparato deriva dos, y el contrato no dice cuál de las dos lecturas manda.**

**`O-02` · MENOR · el mensaje de éxito de `G-16` es él mismo un censo escrito a mano.** En mi reproducción de la refutación 3, `G-16` imprimió, **marcada OK**: «condiciones 13/13 con estado único, **8+2+1+1+1 = 13**» — mientras el bloque que acababa de validar declaraba 9+1+1+1+1. La cadena está codificada literalmente y **no se deriva**. Junto con `_COMPONENTES_CL13`, son **dos censos escritos a mano dentro de la comprobación cuyo objeto es esa disciplina**, y uno sobrevive intacto a la mutación que la comprobación no detecta.

**`O-03` · MEDIO · la laguna de `M-03` deja además el diario permanentemente inválido.** `M` se detiene en «el bloqueo se pierde». Añado la segunda consecuencia, verificada: tras esa caída, el `abandonada` **durable** conserva su `deriva_emitida` obligatorio apuntando a un evento que **no existe** y que el arranque **tiene prohibido emitir**. La capa B, fila 3, exige «que ese `deriva` **exista**». Luego el diario queda **permanentemente no conforme por su propio validador, sin ruta de reparación declarada**. La laguna no es sólo de bloqueo perdido: es de **corpus irreparable**.

**`O-04` · MENOR · `C-L.5` contiene una condición que su propio adjudicador no puede verificar.** Su regla de cierre —«cualquier fuente ASIGNADA pero NO LEÍDA impide la suficiencia»— exige el **manifiesto de asignación** de cada revisor. Los dictámenes declaran, con honestidad, qué leyeron y qué no, **pero ninguno declara qué se le asignó**. Sin eso, la regla no es comprobable por el adjudicador que `C-L.5` designa.

#### 6 · Discrepancias entre `M` y `N`, resueltas contra la fuente

| # | discrepancia | resolución |
|---|---|---|
| **D-1** | **`C-L.3`: ¿NO CERRADA (`M`) o PARCIALMENTE CERRADA (`N`)?** | **Los dos aciertan en la mitad que miraron.** La **aritmética** de NIVEL A es correcta —la derivé a mano y mecánicamente—, y en eso `N` tiene razón. Pero NIVEL A **no está cerrado normativamente**: no implementa la vía propietaria que su propio criterio nombra en primer lugar (`O-01`, demostrado con fixture). **`C-L.3` queda NO CERRADA, y con TRES causas independientes**: `O-01`, `M-01` y `N-01` |
| **D-2** | **La cobertura de `11-ARQUITECTURA-INTEGRADA.md`.** `N` funda su quinta razón en que nadie lo leyó íntegro | **Resuelvo contra `N`.** `M` lo declara en su lote **con lectura íntegra de sus 9058 líneas**, y su total declarado sólo cuadra incluyéndolo. `N` no podía saberlo: trabajaron a ciegas. **La quinta razón de `N` cae sobre la unión.** Su veredicto no depende de ella sola, y las otras cuatro se sostienen |
| **D-3** | **La severidad del defecto de `AUD`.** `M` lo formula como pérdida de la vía condicional; `N` como posición inexigible más exclusión de `DIR` | **Son DOS defectos distintos en la misma cláusula, no uno graduado dos veces.** El de `M` responde *qué pares se exigen*; el de `N`, *dónde va la participación y a qué procesos alcanza la regla*. **Ninguno absorbe al otro**, y los confirmo por separado. **Que dos revisores ciegos encontraran defectos distintos en la misma cláusula, tras tres remedios sucesivos sobre ella, es el dato más elocuente del expediente** |
| **D-4** | **Lotes complementarios** | **Sin conflicto: se complementan.** `M` no encontró `N-01` porque no leyó `esquemas/proceso.yaml` ni las fichas; `N` no encontró `M-02` ni `M-03` porque §2 era el lote de `M`. **Cada mitad del corpus produjo un defecto grave que la otra mitad no podía ver, y eso mide la cobertura mejor que cualquier declaración** |
| **D-5** | **Citas a corregir** | `N` cita `a.6` L504–505 (es L502–503) y sitúa el «22» en L60 (es L116). **Corrijo las dos referencias; los dos hechos sobreviven** |

**No hay ninguna discrepancia material irresoluble entre `M` y `N`.** Todas se resuelven abriendo la fuente.

#### 7 · ¿Contradice o agrava alguna fuente leída las correcciones aplicadas?

- **`ADS-PENDIENTES`, BLOQUES B y C: CONFIRMAN.** Los cuatro niveles, la REGLA DURA de §988, los cinco participantes de §11 y las doce decisiones pendientes de §17 están recogidos. La única que F4 decide por su cuenta —prohibir la anidación— está argumentada en `D22` y es legítima porque el documento se autodeclara no normativo.
- **Documentos 16, 17 y 18: no contradicen.** La condición `C-0.1` del documento 18 **queda cubierta por el lote de `N`**; la `C-0.2` también: `N` declara las quince fichas íntegras.
- **Una sola tensión, y la registro:** el documento 18 dejaba abierta la posibilidad de que `b.3` o `b.5` refutaran `I-08`. **`N` la cerró en negativo y lo verifiqué.** Eso **agrava** —confirma `I-08` sin escape—, no absuelve.

**No encontré en las cuatro fuentes obligatorias nada que contradiga las correcciones aplicadas.** Lo que encontré las agrava por otra vía: **`M-05`, `M-06` y `M-07` son defectos de las propias sedes que la corrección escribió**, y no estaban registrados en ninguna parte del corpus hasta que `M` los abrió.

#### 8 · Cobertura: `C-L.5`

| requisito | estado |
|---|---|
| **QUIÉN** · revisores nuevos, contexto limpio, distintos de quien aplicó | **CUMPLE** |
| **QUÉ HAY QUE LEER ÍNTEGRO** · las cuatro fuentes | **CUMPLE, y por triplicado.** Las 8 735 líneas leídas íntegras por `M`, por `N` y por mí, de forma independiente |
| **MANIFIESTO DE LECTURA** | **CUMPLE** |
| **DECLARACIÓN DE COBERTURA REAL**, contra el propio interés | **CUMPLE.** `M` publica una sospecha propia refutada; `N`, siete |
| **REGLA DE CIERRE** · cualquier fuente **asignada** y no leída impide la suficiencia | **NO CERTIFICABLE POR MÍ** (`O-04`). No recibí los manifiestos de asignación. **No sustituyo una lectura ausente por una presunción en ninguna de las dos direcciones** |
| **EL ADJUDICADOR NO CORRIGE** | **CUMPLE** |

**La unión de los dos lotes cierra la laguna que el documento 18 dejó abierta**: las catorce fuentes sin lectura sustantiva de su `C-0.1` y las trece fichas de su `C-0.2` quedan cubiertas.

**Mi conclusión.** El **núcleo** de `C-L.5` está satisfecho, y por tres lectores independientes. Su **regla de cierre** no puedo certificarla. **`C-L.5` queda ABIERTA en forma.** Y lo digo con precisión porque importa: **no es la razón por la que este gate falla. El gate falla por el fondo, y habría fallado igual con `C-L.5` cerrada.**

#### 9 · Proporcionalidad, y el patrón

Doce tandas encadenadas. Esta tanda repite el patrón, y lo verifiqué caso a caso: **`M-05` lo introduce `D97` contra sí misma, en el mismo commit**; `M-06` es el checkpoint quedándose atrás del código que la misma tanda corrigió; y `C-L.3` es la **tercera** reformulación de la misma cláusula, fallando las tres por la misma causa.

**Y hay una asimetría que conviene nombrar.** La corrección `D103` es, en su aritmética, **correcta y verificable**: derivé sus cinco procesos y nueve pares a mano y mecánicamente, y coinciden. **`D103` acertó al separar los dos niveles y al negarse a publicar un décimo par fijo.** El defecto no está en lo que decidió, sino, otra vez, **en la mitad de los sitios donde su decisión tenía que alcanzar**.

#### 10 · Límites de esta adjudicación

1. **No he leído el corpus obligatorio íntegro.** Leí íntegras las cuatro fuentes que `C-L.5` nombra y verifiqué por sondeo dirigido todo lo demás.
2. **Nada de esto está construido.** `M-02`, `M-03` y `O-03` son sobre TEXTO. **Un contrato contradictorio no es un sistema roto: es un sistema que no se puede construir sin decidir cuál de las dos frases vale.**
3. **Mi punto más débil es la severidad, no el hecho.** Los hechos están todos abiertos en su fichero y su línea, o reproducidos. **Si alguien graduara `M-01` o `N-01` como MEDIO, el veredicto NO cambiaría:** `M-02` y `C-L.3` lo determinan por otra vía.
4. **Acepté sin verificar** `C-L.6`, `C-L.8` y diecinueve de los veinte recuentos de `N`. Si alguno fuera falso, caerían esas conclusiones; **el veredicto no**.
5. **`M-02` depende de una lectura, y la declaro.** Lo que **NO** admite lectura es que `deriva_emitida` es obligatorio y que `predecesor` va incluido en el `id`.
6. **No reproduje la batería en todas sus variantes.** El repositorio no se tocó.
7. **No recibí los manifiestos de asignación**, y es lo que me impide certificar la regla de cierre de `C-L.5`.

---

## 7 · Estado individual de `C-L.1`–`C-L.13`, adjudicado por `O`

Cada una exactamente una vez, con estado y motivo verificado en su sede.

| # | estado | motivo, con la sede |
|---|---|---|
| **`C-L.1`** | **CERRADA** | `revision_base` es campo **OBLIGATORIO** de `preparada` (§3.6 L4100, «su ausencia hace el evento INVÁLIDO»), registrable en `conflicto` (L4101) y en `abandonada` (L4102), y **entra en el cómputo de `tx`** por §2.8 L2759. **Verificado por `O`.** Cierra `J-01` y `J-02` a la vez, sin nonce ni timestamp |
| **`C-L.2`** | **REGISTRADA PARA F5**, con un defecto en su cuerpo | `PN-15` existe, nombra las cuatro reglas, las declara **PRESIONADAS y VIGENTES**, deja la decisión al Owner, **no redacta ninguna enmienda** y da su condición de reversión. Es trabajo normativo legítimo de F5. **Pero su campo PRUEBA POSTERIOR es falso hoy** (`M-05`) |
| **`C-L.3`** | **NO CERRADA** | La regla **no opera sobre «cualquier vía»**, que es literalmente lo que la condición exige. **Tres causas independientes, las tres verificadas:** `O-01` (vía propietaria no implementada, con fixture en verde), `M-01` (vía condicional perdida en `AUD`), `N-01` (posición inexigible en el único proceso donde el NIVEL B se aplica, y exclusión no derivable de `DIR`) |
| **`C-L.4`** | **CERRADA EN LA FORMA, NO EN EL FONDO** | Los tres extremos existen y `O` los abrió: fecha, cita literal y entrada en `owner_captado`. No se creó `O17` ni se reescribió `O16`, que es la disciplina correcta. **El fondo no cierra** (`M-07`): la fila entró el 2026-08-28 y la procedencia fecha la consulta el 2026-08-29, sin reconciliación en ninguna de las dos sedes |
| **`C-L.5`** | **ABIERTA** | Su núcleo está satisfecho —las cuatro fuentes leídas íntegras por tres revisores limpios que no aplicaron nada— y su **regla de cierre no es certificable** (`O-04`). **No es la razón por la que este gate falla** |
| **`C-L.6`** | **CERRADA** | Declarada por `D99`. **Aceptada sin verificación independiente** por `O` |
| **`C-L.7`** | **CERRADA**, con un defecto nuevo de la misma sede | El bloque de estado está reescrito. **Pero `M-06` es un defecto nuevo del mismo fichero**, en un bloque contiguo. Es `L-01` reproducido por la tanda que venía a cerrarlo |
| **`C-L.8`** | **CERRADA** | Declarada por `D100`. **Aceptada sin verificación independiente** |
| **`C-L.9`** | **CERRADA** | **Verificada por `O`**: 46 filas / 46 ids, y la prosa dice «cuarenta y seis». Derivada y publicada coinciden |
| **`C-L.10`** | **CONTRATADA PARA F6**, correctamente clasificada | **Verificada por `O`, y hay cero líneas de código**: `AFIRMACIONES` sigue siendo la lista literal, no existe derivación, y `T152` conserva su alcance anterior. **Contratar no es implementar, y el corpus lo dice** |
| **`C-L.11`** | **CERRADA** | **Verificada por `O`**: `X62` existe y el recuento se sostiene con él dentro |
| **`C-L.12`** | **REGISTRADA PARA F5** | **Verificada por `O`**: dos filas `E5-1` y `E5-2` con corrección exacta y prueba posterior. F4 no edita (b) y no crea `PN`, con el motivo escrito. **Registrar no es corregir, y se dice** |
| **`C-L.13`** | **MIXTA, SATISFECHA POR DESGLOSE — clasificación CORRECTA, sin doble conteo** | **Verificado por `O`**: los seis componentes **no son filas de la matriz** ni ids `C-L`, y la matriz sigue dando 43/43. `J-11` consta CONTRATADO y NO IMPLEMENTADO, y **lo está de verdad**: `grep 'python_requires\|sys.version_info'` sobre `tooling/` y `validadores/` devuelve **vacío** |

```text
CERRADAS                             7   C-L.1 C-L.6 C-L.7 C-L.8 C-L.9 C-L.11 C-L.13
REGISTRADAS PARA F5                  2   C-L.2 C-L.12
CONTRATADA PARA F6                   1   C-L.10
CERRADA EN LA FORMA, NO EN EL FONDO  1   C-L.4
NO CERRADA                           1   C-L.3        ← una de las cinco que bloquean
ABIERTA                              1   C-L.5
                                    ──
                                    13   los trece ids, cada uno exactamente una vez
```

**Ninguna condición mal clasificada.** `M`, `N` y `O` coinciden, y `O` lo verificó donde pudo.

## 8 · Recuento derivado de los hallazgos

Derivado de las filas adjudicadas por `O`, no copiado de ninguna prosa.

```text
PLANTEADOS      21     M-01…M-12 (12) · N-01…N-05 (5) · O-01…O-04 (4)
RECHAZADOS       0     ninguno. O confirmó los diecisiete de M y N, y añadió cuatro
CONSOLIDADOS    21

BLOQUEANTE       0
GRAVE            5     M-01 · M-02 · M-03 · M-04 · N-01
MEDIO            6     M-05 · M-06 · M-07 · N-02 · O-01 · O-03
MENOR           10     M-08 M-09 M-10 M-11 M-12 · N-03 N-04 N-05 · O-02 O-04
                ──
                21

BLOQUEAN EL PASO A F5   4     M-01 · M-02 · M-03 · N-01
REGRADUADOS             2     N-01 confirmado en sus DOS mitades como un solo GRAVE;
                              O-01 elevado de refutación de batería a defecto de contrato
CITAS CORREGIDAS POR O  2     N cita a.6 L504–505 (es L502–503) y el «22» en L60 (es L116)
SOSPECHAS REFUTADAS     8     M-13 (una) · N (siete), todas publicadas por sus autores
```

**No hay ningún hallazgo rechazado, y eso es inusual en este expediente.** `O` verificó los diecisiete de `M` y `N` contra fichero y línea y los confirmó todos, corrigiendo dos referencias sin que los hechos cayeran. Lo que sí rechazó fue **una razón de veredicto**: la quinta de `N`, que caía sobre la unión de los dos lotes (`D-2`).

## 9 · Veredicto

# INSUFICIENTE PARA F5

**`F4c` NO se cierra. Sigue ABIERTA. `F5` NO queda autorizada.**

Emitido por el adjudicador `O` tras leer íntegras las cuatro fuentes que `C-L.5` nombra,
verificar cada afirmación material contra su fichero y su línea, reproducir por su cuenta las
cuatro refutaciones de la batería, resolver las cinco discrepancias contra la fuente y añadir
cuatro hallazgos propios. **Sin resolver por mayoría.**

**Seis razones, cada una suficiente por sí sola:**

1. **`C-L.3` NO está cerrada**, por tres causas independientes: la vía propietaria no está implementada en ningún nivel (`O-01`), la vía condicional se pierde en `proceso:AUD` (`M-01`), y la posición exigida no existe en el único proceso donde el NIVEL B se aplica mientras `proceso:DIR` queda excluido con una afirmación no derivable (`N-01`). **Es la tercera reformulación de la misma cláusula, y la tercera que falla por la misma causa.**
2. **Existe un defecto arquitectónico nuevo que hace inemitible un terminal** (`M-02`). Sus tres salidas son tres decisiones. **F6 no puede materializar §2.6.9 sin inventar arquitectura.**
3. **Existe una laguna de durabilidad con fallo silencioso, y deja el corpus irreparable** (`M-03` + `O-03`).
4. **La única garantía mecánica del entregable está refutada**, y el adjudicador la refutó él mismo: **dos árboles defectuosos distintos pasan 30/30 en verde** (`M-04`).
5. **Tres sedes vigentes afirman cosas que el árbol desmiente, y ninguna estaba registrada** (`M-05`, `M-06`, `M-07`). **La condición «ninguna contradicción material sin registrar» no se cumple.**
6. **`C-L.5` no queda satisfecha** en su regla de cierre (`O-04`). **Y este gate no falla por cobertura: habría fallado igual con `C-L.5` cerrada.**

**Lo que expresamente NO fundamenta el veredicto.** Ninguna de las seis razones es la ausencia
de runtime, de piloto, de adaptadores certificados o de adopción de PesquerApp. Los tres
revisores comprobaron que están declaradas, con propietario y fase, y que `J-11` y `C-L.10`
declaran cero implementación **y la tienen de verdad**. **La implementación no ejecutada,
correctamente declarada, no es motivo de insuficiencia y no se ha contado.**

## 10 · Qué consta a favor, y no es cortesía

- **`D96`–`D103` no reescribieron ni una línea del registro.** `git diff --numstat 652ab8e..HEAD` sobre `DECISIONES-Y-CONTRADICCIONES.md`: **121 inserciones y CERO supresiones**. `D1`–`D95` intactas, `O1`–`O16` intactas, `D67` **idéntica byte a byte** a la de `7e99388`, documentos 15–18 sin tocar. **`O` lo subraya: «es la primera vez en el expediente que la disciplina de inmutabilidad se cumple sin excepción».**
- **La aritmética resiste.** `D1`–`D103` sin huecos · `O1`–`O16` · trece presiones de quince cabeceras · **46 filas / 46 ids** · **43 filas / 43 ids** con la partición 31·2·2·7·1 cerrando en 43 · quince capacidades · diez procesos · diecinueve esquemas. **Todas cuadran**, derivadas por `O` sin fiarse de ningún titular.
- **La cardinalidad de `D103` es correcta, y era la cifra que más veces había fallado.** Cinco procesos, nueve pares, `(DEP,SEG)` por la obligatoria, `AUD` dinámico por item. **`D103` acertó en lo más difícil: negarse a publicar un décimo par fijo y separar los dos niveles en vez de sumarlos.**
- **Diez de las trece condiciones están donde dicen, y ninguna está mal clasificada.** `C-L.13` es MIXTA de verdad, **sin doble conteo**, verificado contra la matriz.
- **`J-11` y `C-L.10` se declaran contratados y no implementados, y lo están de verdad.** **Contratar no es implementar, registrar no es corregir, y el corpus lo dice en las dos.**
- **La procedencia de `O16` es de una honestidad poco frecuente en lo que atribuye.** Distingue el párrafo del sistema de las dos palabras del Owner, declara qué alcanza la confirmación, y **no crea `O17` ni reescribe la resolución**. Su defecto es de fecha, no de atribución.
- **`PN-15` está bien construida y su negativa a decidir es correcta.** `G21` reserva esa decisión a la constitución y no al sistema.
- **`I-08` no cae, y ahora se sabe.** `N` cerró en negativo la única vía de escape que el gate anterior dejó abierta, y `O` lo verificó.
- **Los BLOQUES B y C confirman a F4.** La lectura que faltaba —la que motivó `C-L.5`— **no absuelve pero tampoco agrava**.
- **Los tres revisores publicaron sus propios errores.** `M` una sospecha refutada; `N` siete; `O` corrigió dos citas de `N` sin que los hechos cayeran, y corrigió al coordinador el identificador del árbol.

> **`O`, literalmente:** «Ésta sigue siendo, con distancia, la candidata más sólida que este
> corpus ha producido. Y por eso mismo importa decir dónde falla: **no falla por concepción.
> Falla, por duodécima vez, porque una decisión bien tomada llega a la mitad de los sitios que
> la invocan** — y esta vez lo hace en la cláusula que tres tandas seguidas han intentado
> cerrar, y en el terminal del que depende toda la línea de corrección de `D64`.»

## 11 · Ningún hallazgo se ha corregido

**Ninguno de los veintiún hallazgos de este gate se ha corregido aquí, y es deliberado.** El
encargo lo prohíbe expresamente mientras el gate está en curso, y corregirlos en la misma
pasada volvería a hacer que quien recibe sea quien aplica — que es la razón por la que doce
tandas se han encadenado.

**Y eso incluye los que caen sobre ficheros que este gate sí podía tocar**: `M-06` señala un
recuento caducado en el checkpoint, y **se deja intacto**; `M-04`, `M-11`, `M-12`, `O-01` y
`O-02` señalan defectos de la batería de verificación, y **no se toca ni una línea de ella**.

Los únicos ficheros que esta pasada modifica son **este documento**, el índice de
`docs/evolucion/`, el checkpoint —para registrar el veredicto, no para corregir hallazgos— y
la evidencia derivada que el runner regenere.

```text
ÁRBOL AL CERRAR   git status --porcelain  →  vacío en los tres revisores
COMMIT JUZGADO    c3d6465a519855095ad6fd2a6a168ec72ef5ed7a
ÁRBOL JUZGADO     db26b4d1898b17ce66f89ea3bb25f817c7c1d6c3
RAMA              gate/f4c-cobertura-final-20260829, sin upstream
```

**`F4c` sigue ABIERTA. `F5` NO queda autorizada. `C-L.5` sigue pendiente.**
