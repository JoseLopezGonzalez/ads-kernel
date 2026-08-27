# TERCERA REVISIÓN INDEPENDIENTE DE F4C

> **Nota de transcripción — la escribe el agente principal, NO el revisor.**
>
> ```text
> QUIÉN EMITE EL JUICIO   un REVISOR INDEPENDIENTE con CONTEXTO LIMPIO, encargado
>                         expresamente para esta pasada. No escribió F4, no aplicó ninguna de
>                         sus correcciones —ni la primera crítica, ni la segunda, ni la
>                         devolución técnica previa, ni ninguna de las SEIS comprobaciones
>                         técnicas posteriores—, y no participó en ninguna decisión `D16`–`D63`
>                         ni en `O7`–`O15`. Su única entrada fue el árbol del repositorio.
>
> QUIÉN TRANSCRIBE        el agente principal, que SÍ aplicó las correcciones anteriores y por
>                         tanto NO puede certificar su propio trabajo. Su papel aquí es
>                         copiar el juicio LITERALMENTE. **No ha suavizado, reinterpretado ni
>                         corregido ningún hallazgo**, y no ha tocado
>                         `11-ARQUITECTURA-INTEGRADA.md` en esta pasada.
>
> QUÉ SE HA RETIRADO      del texto recibido, sólo el sufijo técnico del arnés de ejecución
>                         —identificador del agente y contador de uso—, que no forma parte
>                         del juicio. Ni una palabra del juicio se ha alterado.
>
> SOBRE QUÉ ÁRBOL         HEAD `df059297057bc8cd432b748d82e63837c80d5139`, rama
>                         `redesign/kernel-2.0`, árbol limpio. El commit revisado es el
>                         ÚLTIMO de la cadena de correcciones, y NO estaba publicado en el
>                         remoto en el momento de la revisión.
>
> QUÉ ES ESTE DOCUMENTO   la TERCERA REVISIÓN INDEPENDIENTE que `F4c` exigía como su única
>                         puerta. Su veredicto es **INSUFICIENTE PARA F5**, y por tanto
>                         **`F4c` NO se cierra**: sigue ABIERTA.
>
> QUÉ NO SE HA HECHO      NINGÚN hallazgo se ha corregido en esta pasada. Corregirlos sería
>                         volver a que quien recibe sea quien aplica, que es exactamente el
>                         defecto que estas revisiones encadenadas existen para no repetir.
> ```

---

## 1 · Identidad y procedencia del revisor

Soy un agente con **contexto limpio**. No escribí F4, no escribí ninguna de sus correcciones, no apliqué la primera crítica, ni la segunda, ni la devolución técnica previa, ni ninguna de las seis comprobaciones técnicas posteriores. No he participado en ninguna decisión `D16`–`D63` ni en la redacción de `O7`–`O15`. Mi única entrada ha sido el árbol del repositorio.

```text
REPOSITORIO   /home/jose/ads-kernel
RAMA          redesign/kernel-2.0
HEAD          df059297057bc8cd432b748d82e63837c80d5139
              «docs(f4c): la lapida, la identidad tipada y los tres niveles de garantia»
              verificado con `git log -1`; árbol limpio
FECHA         2026-08-27
MODO          SÓLO LECTURA. No he modificado ningún fichero, no he hecho commits y no he
              ejecutado ninguna escritura de git
```

**Qué NO soy.** No soy una certificación. No he ejecutado ni una sola de las pruebas que F4 escribe: ninguna de las cuarenta y dos filas de `§2.6.7`, ninguna de las nueve `R1`–`R9`, ninguna de las ocho `X-A`–`X-H`, ninguno de los once escenarios `NP-*`, ninguno de los doce escenarios de `§14`. Tampoco soy un revisor del producto: no he visto PesquerApp. Y no soy la autoridad que aprueba las presiones normativas: eso es del Owner, en F5.

**Qué he tratado como objeto y no como fuente.** Los ficheros `12-`, `13-`, `14-`, `CHECKPOINT-ADS-NEXT.md`, `00-INDICE.md` y los mensajes de commit son **objeto de revisión**. No he aceptado ninguna afirmación suya como verdad. Cada cita que F4 hace de `(a)`, `(b)`, `E1`, `E2`, `K-1`, `C1`–`C7`, las fichas de capacidad, los procesos, los esquemas o los validadores la he abierto contra el fichero original. Cada recuento lo he derivado yo con `grep`, `awk`, `wc` y Python sobre el fichero, y sólo después lo he comparado con el declarado.

---

## 2 · Corpus realmente leído

### Leído íntegro

| fichero | líneas |
|---|---|
| `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` | 6316 — el entregable bajo revisión, leído entero por tramos de 230–340 líneas |
| `docs/evolucion/14-DEVOLUCION-TECNICA-PREVIA-F4C.md` | 325 |
| `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` | 230 |
| `docs/evolucion/00-INDICE.md` | 92 |
| `kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md` | 250 (tabla de propiedad y gates, íntegros) |
| `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` | secciones 1–3 íntegras |

### Leído en parte, con los tramos nombrados

| fichero | qué leí |
|---|---|
| `docs/rediseno/a-CAPACIDADES-APROBADA.md` | índice completo; `a.9` íntegra (627–925), `a.11` íntegra, `a.3`/`a.5`/`a.10` por encabezados |
| `docs/rediseno/b-RECORRIDO-APROBADA.md` | índice completo; `b.3`, `b.4`, `b.14`, `b.15`, `b.15.1`, `b.16` íntegras |
| `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` | índice completo; `O7`–`O14` y `O15` íntegras (238–330); `D32`, `D38`, `D46` verificadas por línea |
| `kernel/KERNEL.md` | `G03`, `G05`, `G13`, `G26`, `G28`, `G29` por localización directa; el resto por índice |
| `docs/evolucion/CHECKPOINT-ADS-NEXT.md` | cabecera y bloques `resuelto_en_*` (1–400) |
| `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` | índice completo (31 secciones); §5.18, §5.19, §5.23, §5.24, §20.8, §26.5 íntegras |
| `docs/evolucion/ADS-NEXT-OWNER-BRIEF.md` | estructura completa (26 apartados verificados por conteo) |
| `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` | estructura completa; §4.3, §14, §15, §16 íntegras |
| `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | sólo por localización de términos |
| `kernel/operativo/contratos/C6-…` | catorce principios, tres conceptos, «Entrada por ADS», «Alcance mínimo» |
| `kernel/operativo/capacidades/*/CAPACIDAD.md` | las quince **enumeradas y contadas**; sólo `ENT/CAPACIDAD.md` leída íntegra; las demás por localización dirigida |
| `kernel/operativo/recorrido/01-PROCESOS.md` | los diez procesos enumerados; sólo `AUD` leído íntegro |
| `kernel/operativo/esquemas/` | los 19 contados; `memoria.yaml` e `integration-set.yaml` inspeccionados por campo |
| `kernel/operativo/validadores/validadores.yaml` | clasificado entero por tipo mediante script; bloque `vigencia:` leído íntegro |
| `kernel/operativo/plantillas/SOURCES.toml` | no abierto; el modelo se verificó contra `C6` y el documento del Owner |

### Lo que NO he podido cubrir

- `12-CRITICA-INDEPENDIENTE-F4.md` y `13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md` **no** los he leído íntegros. Los usé sólo para localizar hallazgos concretos que F4 cita. **No audito la corrección de esas dos críticas.**
- Las catorce fichas de capacidad distintas de `ENT` y los nueve procesos distintos de `AUD` no están leídos línea a línea.
- `kernel/operativo/pruebas/`, `kernel/operativo/circuitos/`, `kernel/operativo/diseno/`, `kernel/operativo/entrada/`, `packs/` y `tooling/` quedan fuera: F4 no los modifica y no dependía de ellos ninguna comprobación que hiciera.
- `reglas.yaml` y `exclusiones.yaml` sólo por existencia y ubicación.

---

## 3 · Método

Todo recuento de este informe está **derivado por máquina sobre el fichero**, nunca copiado del documento.

```text
CONTEO DE FILAS Y IDS      grep -cE '^\| `X[0-9]+`' · grep -oE … | sort -n | uniq
                           sobre §2.6.7 y §2.6.5 acotadas por sed -n '<ini>,<fin>p'
COBERTURA DE VENTANAS      extracción de W* y R* de la tabla de proyección de §2.6.9 y
                           comparación de conjuntos contra las tablas de origen
CARDINALIDADES             derivación manual de las cuatro secuencias (3 · 3+2k · 8) y
                           comprobación de 1+k+k+1+1 = 3+2k y 1+4+3 = 8
MATRIZ TIPO × FASE         recomputación de 9 × 7 = 63, 5×6+7+1+1+1 = 40, 5+6+6+6 = 23,
                           y de la partición 40 + 23 = 63
ESQUEMAS Y VALIDADORES     ls kernel/operativo/esquemas/*.yaml | wc -l  → 19
                           script Python que clasifica validadores.yaml por `tipo`
                           → 13 validador · 2 generador · 3 biblioteca
CAPACIDADES Y PROCESOS     ls kernel/operativo/capacidades | wc -l → 15
                           grep '^## `' 01-PROCESOS.md → 10
APARTADOS DE LA DIRECTIVA  grep -c '^# [0-9]' ADS-NEXT-OWNER-BRIEF.md → 26,
                           contra las filas de la tabla de §15.2 → 32 filas, 22 apartados
REFERENCIAS COLGANTES      conjunto de `X<nn>` citados en todo el documento, menos el
                           conjunto de ids definidos en la tabla de §2.6.7
VERIFICACIÓN DE CITAS      cada cita de (a)/(b)/E2/C6/C7/KERNEL abierta con sed -n en su
                           fichero original y comparada palabra a palabra
ALCANZABILIDAD             derivación a mano del grafo de transiciones admitidas de §2.6.1
                           cruzado con las «predecesoras admitidas» de §3.6 y las
                           cardinalidades de §2.6.4
```

---

## 4 · Comprobaciones independientes: derivado frente a declarado

| # | qué declara F4 | qué obtengo yo | veredicto |
|---|---|---|---|
| 1 | «cuarenta y dos filas físicas y cuarenta y dos identificadores únicos» (§2.6.7) | 42 filas, 42 ids únicos, hueco declarado en `X24` | **CUADRA** |
| 2 | «las **diecisiete**» ventanas de §2.6.5 | 17 filas: `W1`–`W11`, `W12a`, `W12b`, `W13`–`W16` | **CUADRA** |
| 3 | nueve ventanas `R1`–`R9` | 9 | **CUADRA** |
| 4 | la tabla de proyección de §2.6.9 cubre todas las ventanas | cubre las 17 `W` y las 9 `R`, sin huecos ni repeticiones | **CUADRA** |
| 5 | seis fases; `derivada` único terminal; ninguna sale de `derivada` | 6 fases; 8 transiciones admitidas; `derivada` sin sucesor | **CUADRA en el grafo**, pero ver `B1` |
| 6 | cardinalidad ruta normal = 3 | 1+1+1 = 3 | **CUADRA** |
| 7 | ruta de conflicto cerrada = `3 + 2k`, k∈{1,2,3} → 5·7·9 | 1+k+k+1+1 = 3+2k → 5, 7, 9 | **CUADRA** |
| 8 | ruta agotada y abierta = 8 | 1 + 4 + 3 = 8 | **CUADRA** |
| 9 | `observacion` ∈ 1..4 · `intento` ∈ 1..3 · `intentos_consumidos` = `observacion` − 1 · no existe `intento: 4` | consistente en §2.6.1, §2.6.4, §2.6.9, §3.6 A y §3.6 B | **CUADRA** |
| 10 | `confirmada` y `reconciliada` mutuamente excluyentes | 1/0 normal, 0/1 conflicto cerrado, 0/0 agotada | **CUADRA** |
| 11 | invariante `#observaciones = #intentos` (cerrada) / `+1` (agotada) | verificado sobre las cuatro secuencias | **CUADRA** |
| 12 | `tipo` = 9 valores | 9 | **CUADRA** |
| 13 | espacio bruto 63 · válidas 40 · prohibidas 23 · partición cierra | 9×7=63; 30+7+3=40; 5+6+6+6=23; 40+23=63 | **CUADRA** |
| 14 | 19 esquemas vigentes + 4 tipos + 2 de clase = 25 | `ls esquemas/*.yaml` → 19; suma 25 | **CUADRA** |
| 15 | trece validadores y dos generadores | 13 `tipo: validador`, 2 `tipo: generador` | **CUADRA** |
| 16 | quince capacidades · diez procesos | 15 directorios con `CAPACIDAD.md`; 10 bloques `ads:proceso` | **CUADRA** |
| 17 | los 29 candidatos repartidos en §15.6 | 29 ids, todos distintos, sin solapes | **CUADRA** |
| 18 | `estado_iniciativa` `Q0`–`Q9` es **total y disjunta** | derivada de cero contra los diez estados de `b.4`: todo caso cae en exactamente una rama; el vacío en `Q4` | **CUADRA** |
| 19 | los diez estados globales de `b.4` quedan cubiertos | los diez, verificados uno a uno contra `b.4` | **CUADRA** |
| 20 | «las doce áreas de `O8`» | 12 elementos, pero **no son los doce del §5.18** que `O8` resuelve | **NO CUADRA** → `G8` |
| 21 | «los cinco conceptos de `a.9`» | `a.9` L675–679 y `00-OBLIGACIONES-Y-CIERRE.md` L41 dan otros cinco | **NO CUADRA** → `G1` |
| 22 | «Los **veintiséis** apartados de la directiva» (§15.2) | la tabla tiene 32 filas y traza **22** de los 26 apartados | **NO CUADRA** → `m3` |
| 23 | «El resultado son **cuatro vigentes**, una retirada y una fusionada» sobre «las cinco de la entrega anterior» (§16) | 4+1+1 = 6 ≠ 5; y §16 cierra con «VIGENTES · OCHO» | **NO CUADRA** → `m2` |
| 24 | los `X<nn>` citados existen en la tabla | `X32`, `X33`, `X34` y `X42` citados y **no definidos** | **NO CUADRA** → `M2` |
| 25 | §8.0: cada macrocircuito declara «lecturas y escrituras» y «estados persistidos» | §8.3 sin `LEE`/`ESCRIBE`; §8.4 sin `ESTADO` | **NO CUADRA** → `G4`, `G5` |
| 26 | `C7` `aplica_a: "una o más fuentes"` frente a `E2.6` «varias sources» | verificado literal en `C7` L170 y `E2.6` | **CUADRA**: el diagnóstico de F4 es correcto |
| 27 | `b.3` dice `vigente \| sustituida \| invalidada` | verificado literal | **CUADRA**: la corrección de F4 es correcta |
| 28 | `b.16` fila `AUD` no incluye `VER` | verificado en `b.16` y en `proceso:AUD` | **CUADRA**: `PN-8` es legítima |
| 29 | `a.11` no deroga ni ajusta `G03` | verificado: `G03` no aparece en `a.11` | **CUADRA**: `PN-3` es legítima |
| 30 | `O15` = adopción real, permanente, completa; repo definitivo; no MVP; base completa; mejoras por migración versionada; no autoriza la adopción | los **seis** puntos presentes y literales en `DECISIONES-Y-CONTRADICCIONES.md` L267–322 | **CUADRA** |

---

## 5 · Hallazgos

### BLOQUEANTES

---

#### `B1` · El conflicto agotado es un interbloqueo terminal sin salida, y congela todo el commit del control repo — **BLOQUEANTE**

**Cita, `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`:**

> L542: «`reconciliacion-preparada` | `conflicto` | … Con `observacion: 4` lleva `agotado: true` y **no admite ninguna `reconciliacion-preparada`**: para y escala»
> L557: «**Ninguna fase salvo `derivada` retira el marcador.**»
> L1497: «AGOTADO (observación 4) **sólo el OWNER**, y con una decisión nueva. El sistema NO prepara un cuarto intento, y `reconciliacion_pendiente` sigue siendo verdadero hasta que esa decisión llegue.»
> L1214: «**ADS nunca hace commit de un árbol con una transacción abierta.** El commit se hace entre transacciones.»
> L1334 (`X58`): «se **detiene y se escala al Owner**, y la transacción queda ABIERTA con su marcador»

**Por qué es un defecto.** Derivé el grafo de transiciones alcanzables desde `conflicto(observacion: 4, agotado: true)` cruzando la tabla de §2.6.1 con las «predecesoras admitidas» de §3.6 y las cardinalidades de §2.6.4. **No existe ninguna transición admisible**, y todas las vías de escape están cerradas explícitamente:

```text
1  hacia `reconciliacion-preparada`  PROHIBIDA. §3.6 L3209 fija su predecesora admitida en
                                     «`conflicto` **sin `agotado: true`**», y §3.6 L3285
                                     manda al validador semántico rechazar toda
                                     `reconciliacion-preparada` cuyo `resuelve` apunte a un
                                     `conflicto` con `agotado: true`
2  hacia `derivada`                  IMPOSIBLE. §3.6 L3212 admite como predecesoras sólo
                                     `confirmada` o `reconciliada`, y la tabla de §2.6.4
                                     (L848–858) fija ambas en **0** para la ruta agotada
3  hacia `abortada`                  NO EXISTE. §2.6.1 L564: retirada y rechazada por el
                                     esquema. Su justificación —«entre el punto de
                                     compromiso y el primer fichero el único resultado es
                                     completar»— fue escrita cuando este estado no existía
4  hacia `deriva`                    NO APLICA. §2.6.11 sólo admite `posterior-al-cierre`
                                     (exige `derivada` durable) y `sin-transaccion` (exige
                                     que no haya transacción). Aquí hay transacción y no
                                     está cerrada
5  una transacción NUEVA de reparación  BLOQUEADA. §2.6.9 L1513: «mutar los items durante un
                                     conflicto — que exigiría una transacción, que está
                                     bloqueada por el marcador». `X08` (L1300): el segundo
                                     ejecutor «**no arranca**: `R5` es un lock, no un consejo»
6  borrar el marcador a mano         INÚTIL. §2.9 lo reconstruye desde el diario como «una
                                     transacción **sin evento `derivada`**», y `W14`/`X14`
                                     mandan recrearlo
```

Las consecuencias no son teóricas y se encadenan mecánicamente:

- El marcador **nunca** se retira (L557), luego por L1214 **el control repo no vuelve a commitear nunca**, para todo el producto. Con ello caen las garantías 4, 5 y 6 de §2.6.6 —commit local, push, reconstrucción desde un clon nuevo— de forma permanente y global, por un solo conflicto agotado sobre un solo fichero.
- `reconciliacion_pendiente` permanece verdadero (L1489), luego `b.4` `P0` deja los items afectados en `reconciliacion-pendiente` para siempre, `§3.3.1` `Q0` deja la iniciativa igual, y `§7.4` `Continúa` paso 2 —«¿hay `reconciliacion_pendiente`? → resolverla antes de nada»— no puede pasar de ahí.
- La regla de lectura de §2.6.8 declara esas rutas **NO FIABLES** de forma permanente.
- §2.6.1 L487 afirma que «una vez [`preparada`] es durable, la transacción SE COMPLETA por una de las dos rutas, y no se revierte». En este estado no se completa ni se revierte: la afirmación es falsa para un estado que el propio contrato produce.

La decisión del Owner que L1497 exige **no tiene forma representable**: no hay `fase` que pueda llevarla, no hay `tipo` de evento que la aloje, y el único mecanismo de reparación que F4 define (§2.6.11: transacción nueva con `hash_previo` = `hash_observado`) está bloqueado por el marcador de la propia transacción que se quiere reparar.

Es, además, **exactamente el modo de fallo que `D32` y `D45` existieron para eliminar** —«bloqueaba **para siempre**», «`Q9` devolvía `bloqueada` **para siempre**»— reproducido en el texto más reciente (`D60`, `D62`) y no detectado. Y `X58` lo canoniza como resultado *exigido*, de modo que el contrato de prueba consagra el interbloqueo en vez de detectarlo.

**Qué exigiría cerrarlo.** Una salida declarada y representable del estado agotado, con las cuatro cosas que todo lo demás de §2.6 tiene: qué acto la produce, qué registro la lleva, qué autoridad la firma y cómo se retira el marcador. Las dos formas mínimas que veo son (i) admitir una transición `conflicto(agotado) → <acto del Owner> → derivada` con su propio registro, o (ii) admitir el abandono explícito de la transacción —el `abortada` que `D38` retiró bajo una justificación que ya no cubre el espacio de estados— seguido de una transacción nueva de reparación. Cualquiera de las dos es una **decisión arquitectónica nueva**, y por tanto no puede diferirse a F6.

---

#### `B2` · El gobierno Git del repositorio de control no existe, y F4 lo rellena por inferencia sobre una regla que `E2.4` acota a las fuentes — **BLOQUEANTE**

**Citas:**

> `11-ARQUITECTURA-INTEGRADA.md` L1781–1789: «LUEGO EL GOBIERNO GIT DEL CONTROL REPO NO EXISTE — es un HUECO DECLARADO POR OMISIÓN en toda la arquitectura.» · «**Se declara aquí como hueco, y no se rellena por inferencia.**»
> `11-ARQUITECTURA-INTEGRADA.md` L1767–1768: «3 LA RAMA SE DECLARA, y no se adivina. `main` del control repo PROTEGIDA por defecto, coherente con `G29` conservada por `E2.4`.»
> `docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md` L151: «Su modelo de rama principal protegida … **se conserva íntegro y se aplica POR SOURCE**.»
> `11-ARQUITECTURA-INTEGRADA.md` L5254: «ramas, worktrees, aislamiento | `C7`, conservando `G29` **por fuente**»
> `11-ARQUITECTURA-INTEGRADA.md` L1763: «EL PUSH NO ES AUTOMÁTICO. Pasa a `esperando-owner`, o a la política de publicación que el producto declare.»

**Por qué es un defecto.** Verifiqué la tabla de propiedad de `C7` línea a línea (L80–92): sus once filas gobiernan **materializar fuente, rama, commit, push, PR, revisión, merge, convergencia, release, rollback y retirada de rama abandonada**, todas *de las fuentes*. Ninguna alcanza al control repo. F4 lo diagnostica correctamente. Pero acto seguido:

1. **Se rellena por inferencia lo que dos párrafos antes prometió no rellenar.** La regla 3 invoca `G29` para el control repo, y `E2.4` —la enmienda aprobada que revisa `G29`— la acota expresamente a las fuentes, hasta el punto de rematar: *«El estado del producto **no vive en ninguna rama**: se calcula en el control repo»*. El propio F4 lo escribe correctamente en L5254 y lo contradice en L1768.
2. **La regla 3 no declara nada.** Dice «LA RAMA SE DECLARA, y no se adivina» y a continuación declara únicamente que `main` está protegida. Con `main` protegida, sin rama de trabajo declarada, sin PR, sin autoridad de merge y sin política de publicación, **no existe ningún camino por el que un commit de `estado/` llegue jamás a `main`**.
3. **La alternativa nombrada no existe.** «La política de publicación que el producto declare» aparece **una sola vez en todo el corpus** (comprobado con `grep -rn` sobre `docs/` y `kernel/`): sin esquema, sin sede canónica, sin autoridad, sin fila en la matriz de §1.3 y fuera del recuento de §3.8. Es exactamente el modo de fallo que `D43` corrigió cuando `contrato-de-aspecto` se invocaba tres veces como sede normativa y no existía.

Lo que se cae con ello no es periférico:

- §2.6.6 garantías **5** (push remoto: «sobrevive a la pérdida de la máquina entera») y **6** (reconstrucción desde un clon nuevo) quedan sin mecanismo.
- §2.9 declara que el estado canónico tras una pérdida se reconstruye **desde Git**; sin publicación gobernada, sólo hay commits locales.
- §2.9 exige, como condición previa a toda `retirada-de-cuerpo`, que evento y sellado estén «confirmados en una **REVISIÓN GIT DURABLE del repositorio de control**». Sin publicación gobernada, la condición 1 de la fuente de recuperación es inalcanzable, y con ella toda la operación de lápida.
- `O15` exige que el control repo de PesquerApp **nazca definitivo y permanente**. Una instalación permanente cuyo estado no puede publicarse de forma gobernada no es permanente: es local.

**Qué exigiría cerrarlo.** La tabla de propiedad del control repo que §2.6.10 nombra y no escribe: quién pide, ejecuta, bloquea y verifica su rama, commit, push y PR, con qué evidencia; qué rama recibe las escrituras del runtime dado que `main` está protegida; y qué es, con esquema y sede, la «política de publicación». **Nada de eso está determinado por `(a)`, `(b)`, `E1`, `E2`, `C6` ni `C7`** —`E2.4` cierra explícitamente la vía de derivarlo de `G29`—, luego F6 no puede rellenarlo sin tomar una decisión arquitectónica nueva. Por el criterio del propio encargo, «queda para F6» no es aceptable aquí.

---

### GRAVES

---

#### `G1` · «Los cinco conceptos de `a.9`» están mal citados, y son la lista de campos obligatoria de todo evento — **GRAVE**

**Citas:**

> `11-ARQUITECTURA-INTEGRADA.md` L632–633: «6 PROCEDENCIA los cinco conceptos de `a.9` sin confundirlos: ordenante, autoridad, escritor del comando, ejecutor y **actor atribuido**.»
> `11-ARQUITECTURA-INTEGRADA.md` L2864–2865: «`ordenante · autoridad · escritor_del_comando · ejecutor · actor_atribuido` — los CINCO conceptos de a.9, sin confundirlos»
> `docs/rediseno/a-CAPACIDADES-APROBADA.md` L673–679: «Cinco conceptos que **NO DEBEN** confundirse — ni en el kernel ni en ninguna prueba de conformidad: **PROPIETARIO DEL CAMPO · AUTORIDAD · ORDENANTE · ESCRITOR DEL COMANDO · EJECUTOR DE MUTACIÓN**»
> `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md` L41: «Los cinco conceptos de a.9 —**propietario del campo**, autoridad, ordenante, escritor del comando y ejecutor de mutación— aplican aquí sin excepción»

**Por qué es un defecto.** F4 sustituye `propietario del campo` por `actor atribuido` —que en `a.9` pertenece a **otra** lista, la de cuatro elementos de L662–665— y presenta el resultado como los cinco de `a.9` «sin confundirlos», que es literalmente lo que `a.9` advierte que no debe hacerse. No es una imprecisión de redacción: esa lista es **el conjunto de campos comunes obligatorios de todo evento** (§3.6), lo invoca seis veces (L632, L1177, L1322, L1592, L1733, L2399) y `X39` y la regla 1 de §2.6.10 lo convierten en condición de validación —«la ausencia de cualquiera de los cinco es un FALLO DEL VALIDADOR, no un silencio»—. F6 construiría el esquema de `evento` con un conjunto de campos que ni `a.9` ni el propio corpus operativo respaldan.

Y es **el mismo modo de fallo que el hallazgo `J` corrigió** en esta misma pasada —«F4c tomaba la palabra de un sujeto y la pegaba al ciclo de otro»—, reproducido en otra sección y no detectado.

**Qué exigiría cerrarlo.** O bien alinear la lista con `a.9` y con `00-OBLIGACIONES-Y-CIERRE.md`, o bien declarar explícitamente que el evento lleva `actor_atribuido` **además** de los cinco, con su motivo, y dejar de llamar «los cinco conceptos de `a.9`» a un conjunto distinto.

---

#### `G2` · Dos mecanismos para el mismo estado de disco: la ruta de reconciliación es complejidad no justificada — **GRAVE (defecto arquitectónico de proporcionalidad)**

**Citas:**

> L1201–1204: «Un canónico que revirtió bajo una `derivada` durable es **indistinguible, desde el estado**, de uno que alguien tocó — y las dos cosas exigen lo mismo: parar y escalar.»
> L1867–1872 (§2.6.11): «REQUIERE UNA OPERACIÓN RECUPERABLE, con su INTENCIÓN DURABLE PREVIA — es decir, su propio `preparada`, con `hash_previo` = el `hash_observado` que la deriva registró … Es una transacción **NUEVA**, con `tx` nuevo.»
> L1598 (punto 5 de `reconciliacion-preparada`): «`hash_final` por fichero. Es el que gobierna a partir de aquí, y **SUSTITUYE** al `hash_posterior_esperado`.»

**Por qué es un defecto.** F4 resuelve **el mismo problema dos veces, con dos maquinarias de coste muy distinto**:

- Divergencia descubierta con la transacción **cerrada**, o sin transacción → evento `deriva`, se escala, y la reparación es **una transacción nueva** con `hash_previo = hash_observado`. Coste: un tipo de evento sin fase y ninguna maquinaria adicional.
- Divergencia descubierta con la transacción **abierta** → un subautómata completo: tres de las seis fases (`conflicto`, `reconciliacion-preparada`, `reconciliada`), dos contadores (`observacion` 1..4, `intentos_consumidos` 0..3) más `intento` 1..3, la bandera `agotado`, el campo `resuelve`, un presupuesto de reintentos, nueve ventanas `R1`–`R9`, cinco filas adversariales `X54`–`X58`, y una parte sustancial de las reglas del validador semántico del diario.

El único argumento que F4 ofrece para la asimetría es que con la transacción abierta «SÍ existe una intención durable que declara a qué resultado hay que llegar y con qué mecanismo, luego el resultado es determinista y se completa» (L1207–1210). **Ese argumento no se sostiene para los ficheros divergentes**, que son los únicos que entran en la ruta: el punto 5 de `reconciliacion-preparada` declara que su `hash_final` **sustituye** al `hash_posterior_esperado`. Es decir, la intención original se descarta y una autoridad decide una nueva. Exactamente lo mismo que hace la reparación de una `deriva` — con la diferencia de que aquélla lo hace con una transacción nueva y cero maquinaria adicional.

Además, la ruta de reconciliación es la que produce `B1`. La alternativa más simple —`conflicto` bloquea, se escala, la reparación es una transacción nueva— **conserva todas las garantías profesionales que F4 declara**: nada se sobrescribe, se conserva copia íntegra de lo divergente, decide una autoridad nombrada, hay intención durable previa, roll-forward only, y ningún trabajo se destruye sin registro. Y elimina de raíz el interbloqueo, porque una transacción abandonada explícitamente libera su marcador.

No afirmo que la ruta larga sea incorrecta; afirmo que **F4 no demuestra qué capacidad se perdería sin ella**, y que su §3.1 y el §26.5 del documento de pendientes —«no se fusionan conceptos realmente distintos sólo para reducir el recuento», pero tampoco se duplican mecanismos para el mismo sujeto— exigen esa demostración. Es el mismo criterio con el que §2.5 plegó el manifiesto de transacción dentro de `evento`, aplicado con una vara distinta.

**Qué exigiría cerrarlo.** O una demostración explícita, mecanismo a mecanismo, de qué garantía profesional se pierde si la divergencia bajo transacción abierta se trata como la divergencia posterior al cierre; o la simplificación.

---

#### `G3` · El contrato de `fallo` no puede representar lo que cuatro pasajes normativos y dos pruebas le exigen — **GRAVE**

**Citas:**

> L3213 (contrato por fase): «`fallo` | **ninguna: NO tiene `tx` ni `fase`** | `operacion` · `diagnostico` · `intentos` | `fase` · `afecta` | — | ninguna»
> L3162: «`deriva` o `fallo` CON `fase` o CON `tx` → ESQUEMA ESTRUCTURAL»
> L1083 (garantía 6): «se emite un evento **`fallo`** de publicación, **nombrando `tx` y commit**, y se escala»
> L1225–1229: «MARCADOR EN UN ÁRBOL CLONADO → Evento **`fallo`**, con `operacion: publicacion`, **el `tx` y el commit culpable nombrados**»
> L1307 (`X15`) y L1319 (`X28`): «nombrando `tx` y commit»
> L1036 (`W16`): «evento `fallo` **con las referencias nombradas**»

**Por qué es un defecto.** El campo `tx` está **prohibido** en `fallo` y su ausencia la hace cumplir el esquema estructural. Sus campos obligatorios son tres y ninguno puede alojar un `tx`, un commit ni un conjunto de referencias Git. `deriva` sí recibió un campo dedicado (`tx_afectada`) precisamente para referenciar una transacción sin pertenecer a ella; **a `fallo` no se le dio el equivalente**, pese a que cuatro pasajes normativos y dos filas adversariales le exigen nombrar un `tx`. `X15` y `X28`, tal como están escritas, **no son satisfacibles** contra el contrato vigente.

Es el mismo modo de fallo que `D54` corrigió para el contrato genérico —«no podía representar el `hash_observado` de un conflicto, ni la copia de lo divergente»— reproducido para `fallo` y no detectado por `D57`/`D59`, que se ocuparon de los ejes y no del contenido de esta fila.

**Qué exigiría cerrarlo.** Dar a `fallo` los campos de referencia que sus usos normativos exigen —`tx_afectada`, `commit`, `referencias[]`— con la misma disciplina con que se los dio `deriva`, o retirar de garantía 6, §2.6.4 paso 1, `W16`, `X15` y `X28` la exigencia de nombrarlos.

---

#### `G4` · El macrocircuito de migración no declara qué lee ni qué escribe, y su único paso destructivo escribe en las fuentes sin gobierno — **GRAVE**

**Citas:**

> L4525–4527 (§8.0): «PROPIO disparador · precondiciones · fases · participantes · **lecturas y escrituras** · estados persistidos · evidencias · gates · certificación · rollback · reanudación · condición de cierre.»
> L4719–4744 (§8.3): el bloque contiene `DISPARADOR`, `PRECONDICIONES`, `FASES`, `PARTICIPANTES`, `DIFERENCIA CON A`, `ESTADO`, `EVIDENCIA`, `GATES`, `CERTIFICACIÓN`, `ROLLBACK`, `REANUDACIÓN`, `CIERRE`. **No contiene `LEE` ni `ESCRIBE`.**
> L4728: «M6 RETIRAR del **repositorio técnico** kernel, packs y organización»
> L4813: «M6 revertir es RESTAURAR lo retirado desde la historia del **repositorio técnico**»

**Por qué es un defecto.** Comprobé los cuatro bloques campo a campo. §8.1 y §8.2 declaran `LEE` y `ESCRIBE` con precisión —y ambos fueron **corregidos** por el hallazgo `I.3` para acotar cuándo se escribe en las fuentes: «las fuentes sólo desde N6», «NADA en las fuentes hasta A8»—. §8.3 no declara ninguno de los dos, y es **el único macrocircuito cuyo paso `M6` es destructivo sobre los repositorios del producto**. Tres consecuencias:

- No hay declaración de alcance de escritura para el circuito que borra kernel, packs y organización de repositorios ajenos.
- `M6` no invoca `C7` en ningún punto (verificado con `grep` sobre las 110 líneas de §8.3): sin paquete, sin `escribe_fuentes`, sin custodia, sin checkpoint, sin rama, sin PR, sin CI. Es **exactamente** lo que el hallazgo `I.3` corrigió para `U5b`, `N2` y `A5`, y que aquí no se aplicó.
- «El **repositorio técnico**», en singular, contra `C6` `N4` (0..N fuentes) y contra `E2.0`, cuya formulación singular está declarada RETIRADA. Con N fuentes, `M6` y su rollback necesitan tratamiento por fuente e `INTEGRACIÓN PARCIAL`, igual que `U5b` y `A8` los recibieron. §8.3 no lo tiene. Es también la reproducción del hallazgo `I.1`, corregido para el puntero y no aquí.

**Qué exigiría cerrarlo.** `LEE` y `ESCRIBE` declarados en §8.3 con el mismo grado que §8.1 y §8.2; `M6` como conjunto de source changes gobernados por `C7`, con gate, evidencia y rollback **por fuente**, y el estado `INTEGRACIÓN PARCIAL` mientras no converjan todas.

---

#### `G5` · El macrocircuito de actualización no declara su estado persistido — **GRAVE**

**Cita:** L4828–4861 (§8.4). El bloque contiene `DISPARADOR`, `PRINCIPIO`, `PRECONDICIONES`, `FASES`, `PARTICIPANTES`, `LEE`, `ESCRIBE`, `EVIDENCIA`, `GATES`, `CERTIFICACIÓN`, `ROLLBACK`, `REANUDACIÓN`, `CIERRE`. **No contiene `ESTADO`**, que §8.0 L4526 declara propio de cada macrocircuito.

**Por qué es un defecto.** `U` es el circuito con más superficie de estado en juego: `U2` compara `esquema_estado`, `U3` puede exigir una instantánea versionada del estado previo, `U4` puede ejecutar una migración de esquema y `U5b` genera un estado `INTEGRACIÓN PARCIAL` por fuente. Nada de eso tiene sede declarada. `REANUDACIÓN` («por el evento `preparada` de la tx si U4 se interrumpe») cubre sólo `U4`; `U0`–`U3`, `U5b` y `U6` quedan sin soporte durable declarado, que es exactamente el defecto que `D30` corrigió para la instalación al mover `estado/` a `N0`. Y la instantánea de `U3` —alternativa admitida al migrador inverso— no tiene ni ubicación ni plano ni ciclo: si es durable y versionada, contradice que `estado/` sea la única sede; si es operacional, no sobrevive al rollback que justifica su existencia.

**Qué exigiría cerrarlo.** Declarar el `ESTADO` de `U` con el mismo grado que `N` y `A`: qué nace, dónde, desde qué fase, y dónde vive la instantánea de `U3` con su plano.

---

#### `G6` · Tres de los cuatro macrocircuitos no dicen a qué proceso de `b.16` pertenecen sus items — **GRAVE**

**Citas:**

> L4523–4528 (§8.0): «COMÚN el motor: ENC → DSP → **ruta desde b.16** → C4 … **Ningún macrocircuito crea un tipo de proceso nuevo.**» · «FORMA cada uno es una INICIATIVA con **su plantilla de ruta**. No un proceso.»
> `docs/rediseno/b-RECORRIDO-APROBADA.md` §b.1: regla de proceso único — un item tiene exactamente un proceso.
> `b.16`: «Las capacidades marcadas OBLIGATORIAS definen las **obligaciones** del proceso».

**Por qué es un defecto.** La ruta, las obligaciones, el propietario global y los gates de cada item se **derivan del proceso** (`b.16`). §8.2 nombra el suyo para dos fases —«A2/A3 `AUD` con INV produciendo la capa» (L4646)—. **§8.1, §8.3 y §8.4 no nombran ninguno**: sus filas `PARTICIPANTES` enumeran capacidades (`PLT`, `SIS`, `VER`, `ENC`, `PRD`…), que no es lo mismo. Y §8.0 cierra la salida fácil al prohibir crear un proceso nuevo, y al declarar que el macrocircuito «no es un proceso».

Resultado: F6 no puede componer la ruta de `N0`–`N7`, `M0`–`M7` ni `U0`–`U6` sin **elegir** entre los diez procesos canónicos, y esa elección determina obligaciones, propietario global y gates. Es una decisión arquitectónica que F4 no toma y que no se deriva mecánicamente de nada. Lo agrava que §8.0 hable de «su plantilla de ruta» sin que exista tal artefacto en el corpus: no es un tipo, no está en §3.8, no tiene esquema y no aparece en la matriz de §1.3.

**Qué exigiría cerrarlo.** Para cada macrocircuito, la correspondencia fase → item → proceso de `b.16`, o la declaración explícita de que la «plantilla de ruta» es un artefacto nuevo, con la prueba de §3.1 aplicada y su entrada en el recuento.

---

#### `G7` · `N0` crea un paquete que pertenece a una iniciativa, y `§3.3.0` acaba de declarar que eso no existe — **GRAVE**

**Citas:**

> L4576 (§8.1): «└─ `items/INI-001-paq/`  el paquete en curso, con su CHECKPOINT»
> L2569–2572 (§3.3.0, `D45`): «`b.1` fija que un paquete pertenece a un ITEM. **Una iniciativa no tiene paquetes ni capas: sólo `items` como referencias**»
> L2544 (§3.3): «`items` referencias. NUNCA copia su estado»
> L327–331 (§2.3): «`estado/items/<ITEM-ID>/` … `paq/<nn>-<CAP>.md`»
> L1949–1951 (§2.8): «ITEM `<TIPO>-<nnn>` FEA-021» · «INICIATIVA `INI-<nnn>`»

**Por qué es un defecto.** `estado/items/INI-001-paq/` viola tres contratos a la vez:

1. Usa un identificador de **iniciativa** (`INI-001`) como identificador de **item**, contra la nomenclatura de §2.8.
2. No es una ruta válida bajo §2.3: los paquetes viven en `<ITEM-ID>/paq/<nn>-<CAP>.md`, no en un directorio `<ID>-paq`.
3. Asigna un paquete a una iniciativa, que es precisamente lo que `D45` —la corrección del hallazgo `N-6`, la que hizo computable `Q9`— declaró imposible catorce páginas antes.

Y no es un detalle de ilustración: es el soporte sobre el que descansa `D30`. Toda la justificación de mover `estado/` a `N0` es que la instalación pueda reanudarse «SIN el chat y SIN el Owner»; §8.1 `REANUDACIÓN` dice «por checkpoint desde N0» y §8.2 «por el dosier de la iniciativa más el checkpoint del paquete en curso». Si ese paquete no puede existir, la reanudación de las fases tempranas de instalación y adopción vuelve a apoyarse en nada — que es lo que el apartado 19 de la directiva prohíbe. Adicionalmente, `§3.3.1` `Q4` («conjunto de items VACÍO → `abierta-sin-items` … es el primer instante de toda iniciativa») describe un arranque que `N0` contradice.

**Qué exigiría cerrarlo.** O declarar el item real que `N0` crea, con su id tipado, su proceso (ver `G6`) y su relación de referencia desde `INI-001`; o declarar dónde vive el checkpoint de una iniciativa sin paquetes, lo que exigiría revisar `D45`.

---

#### `G8` · Las doce áreas de `§4.3` no son las doce del `§5.18` que `O8` resuelve — **GRAVE**

**Citas:**

> `11-ARQUITECTURA-INTEGRADA.md` L3634–3637: «identidad y dirección de producto · baseline funcional · dominio y glosario · **arquitectura actual · dirección arquitectónica** · tecnologías y entorno de desarrollo · dirección de ingeniería · calidad y pruebas · seguridad y riesgos · despliegue, entornos y operación · decisiones · dirección de evolución y gaps»
> `docs/evolucion/ADS-PENDIENTES-…md` L775–786: «1. **mapa documental**; 2. identidad y dirección de producto; … 5. **arquitectura actual y dirección arquitectónica**; …»
> `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` L255 (`O8`): «**las doce áreas semánticas del §5.18**, obligatorias como MATERIA y no como ficheros»

**Por qué es un defecto.** Comparé los dos conjuntos elemento a elemento. F4 **elimina «mapa documental»** —el punto 1 del núcleo obligatorio— y **parte «arquitectura actual y dirección arquitectónica» en dos**. El número doce se conserva; el conjunto no. `grep -n "mapa documental"` sobre todo el repositorio devuelve **una sola aparición**, en `§5.18`: F4 no lo menciona en ningún sitio, ni para conservarlo, ni para retirarlo, ni para declararlo derivado.

`O8` es una resolución del Owner y remite a `§5.18` por número. Cambiar qué contiene esa lista es reinterpretar una resolución suya — que es exactamente el criterio por el que F4 registró `PN-6` («reinterpretar la precondición de una resolución suya es materia suya, no del autor de F4 — aunque la corrección sea obviamente necesaria, y precisamente por serlo») y `PN-10` («un tratamiento asimétrico de las resoluciones del Owner es el defecto»). Aquí la misma vara no se aplicó: **es una presión normativa omitida**.

La consecuencia es material: cada área es un `aspecto:documental/<area>` con su `contrato-de-aspecto:documental/<area>` (§5.7), luego F6 construiría doce contratos para las áreas equivocadas, y el mapa documental —lo que `§5.23` necesita para «detectar documentos ausentes, duplicados, sin responsable»— quedaría sin sede, sin responsable y sin caducidad.

**Qué exigiría cerrarlo.** O alinear la lista con `§5.18`, o declarar explícitamente la sustitución con su motivo y registrarla como presión normativa sobre `O8`, diciendo qué ocupa el lugar del mapa documental —presumiblemente el inventario derivado de §5.1, que habría que declarar como tal.

---

### MEDIOS

---

#### `M1` · «La política de publicación que el producto declare» es una sede normativa invocada y no definida — **MEDIO**

**Cita:** L1763. `grep -rn "política de publicación" docs/ kernel/` devuelve **una única aparición**, ésta.

**Por qué es un defecto.** Es el modo de fallo exacto que `D43` corrigió: invocar una sede normativa que no existe —sin esquema, sin fichero, sin autoridad, sin ciclo, sin la prueba de §3.1 y fuera del recuento de §3.8—. No es bloqueante por sí solo porque la rama primaria (`esperando-owner`) sí está definida, pero deja a F6 una alternativa normativa sin contenido. Contribuye a `B2`.

**Qué exigiría cerrarlo.** Definirla —tipo o campo, sede, autoridad, ciclo— o retirar la alternativa y dejar `esperando-owner` como única vía.

---

#### `M2` · Referencias colgantes a pruebas que no existen: `X42` y `X32`–`X34` — **MEDIO**

**Citas:**

> L3979: «y **`X42`** la comprueba validando las tres celdas contra el esquema sin campos libres»
> L4373: «**Pruebas adversariales `X32`–`X34`.** Adopción hasta `A7` inclusive: …»
> L1349 (§2.6.7): «la tabla empieza en `X01`, **salta `X24`** con su motivo declarado abajo»

**Por qué es un defecto.** El conjunto de ids definidos en la tabla de §2.6.7 es `{X01..X23, X25..X28, X37..X39, X47..X58}`. `X32`, `X33`, `X34` y `X42` **no están definidos en ninguna parte** del documento. Además, la nota de L1349 declara un único hueco (`X24`) cuando los huecos reales son dieciséis (`X24`, `X29`–`X36`, `X40`–`X46`), lo que apunta a filas retiradas o renumeradas sin actualizar las referencias. F4 afirma que `X42` «comprueba» la tesis del §5.6 y que `X32`–`X34` demuestran que la adopción no toca las fuentes antes de `A8`: son afirmaciones de verificación respaldadas por contratos de prueba inexistentes, en un documento cuya disciplina central es que «escribir el contrato de una prueba no es la prueba».

**Qué exigiría cerrarlo.** Definir las cuatro filas o reasignar las referencias a filas existentes, y corregir la nota de huecos.

---

#### `M3` · `§15.7` declara `C6` REUTILIZADO mientras `§6.7` le añade una excepción nombrada a su frontera — **MEDIO**

**Citas:**

> L5766: «| `C6` producto, fuentes y workspace | **REUTILIZADO**. §5.1 se apoya en su componente sin deformarlo |» — y §15.1 define REUTILIZADA como «entra sin cambio»
> L4344–4349: «1 EXCEPCIÓN DECLARADA A LA FRONTERA DE `C6` — El puntero está en la fuente por una necesidad real de descubrimiento, y **NO porque la frontera de `C6` lo permita**.»
> L4331–4333: «`C6` RESPONDÍA QUE NO A SU PROPIA FRONTERA: el puntero NO deja de ser cierto si cambia el código de al lado …, luego por la regla de `C6` **su sitio sería el control repo**»

**Por qué es un defecto.** Es literalmente el hallazgo `H` reproducido sobre otro contrato: allí `§15.7` decía «`C7` REUTILIZADO» mientras el diseño lo contradecía, y F4 lo corrigió. Aquí `§15.7` sigue diciendo «`C6` REUTILIZADO» mientras `§6.7` reconoce que su frontera responde lo contrario y le impone una excepción, más obligaciones nuevas (`puntero_en_fuente` y `resolucion_del_control_repo` en todo adaptador, escrituras en fuentes en `N6`, `A8` y `U5b`). `C6` es material derivado, luego esto no es presión normativa; pero su registro en §15.7 es falso, que es exactamente lo que `H` exigía corregir.

**Qué exigiría cerrarlo.** Cambiar la fila de `C6` en `§15.7` a la clase que le corresponde, con la excepción nombrada y su prescripción para F6, igual que se hizo con `C7`.

---

#### `M4` · Retirar un adaptador borra ficheros en repositorios ajenos sin ningún gobierno — **MEDIO**

**Citas:**

> L4213–4214 (§6.6): «5 el adaptador viejo puede convivir o retirarse. **Retirarlo borra su proyección**, nunca el estado»
> L4351–4355 (§6.7 regla 2): «**TODA ESCRITURA DE PUNTERO ES UN SOURCE CHANGE GOBERNADO POR `C7`** … paquete con `escribe_fuentes`, custodia de `PLT`, checkpoint, rama, commit, push, PR y CI por fuente.»

**Por qué es un defecto.** Borrar es escribir. El puntero es una proyección que vive **dentro de los repositorios del producto**. Escribirlo exige `C7`, gate, evidencia por fuente e Integration Set (`U5b`), y sólo puede ocurrir en `N6` o `A8` con autorización del Owner. Retirarlo, según §6.6, no exige nada: ni gate, ni autorización, ni rollback por fuente, ni `INTEGRACIÓN PARCIAL` si la retirada converge en unas fuentes y no en otras. La asimetría deja la operación destructiva menos gobernada que la constructiva, en repositorios que no son de ADS.

**Qué exigiría cerrarlo.** Someter la retirada del puntero al mismo régimen que su propagación, con su gate, su autorización y su rollback por fuente.

---

#### `M5` · El tope de reintentos invoca el precedente de `a.9` invirtiendo su cláusula de terminación — **MEDIO**

**Citas:**

> L1660–1662: «Es el **precedente numérico que `a.9` ya fijó** para el CAS del tablero —`MAX_CAS_RETRIES = 3`— aplicado aquí: un reintento sin tope es un livelock, y **el corpus ya lo resolvió una vez**.»
> L1655–1658: «no admite ninguna `reconciliacion-preparada`: se detiene, se escala al OWNER y **NO se vuelve a intentar sin su decisión**»
> `docs/rediseno/a-CAPACIDADES-APROBADA.md` L787–793: «Si los tres fallan … DSP: 1. deja TODAS las órdenes sin consumir · 2. NO modifica el estado canónico · 3. registra `reconciliacion_pendiente` · 4. informa del conflicto y DEJA DE GIRAR · **5. reintenta en un ciclo posterior o cuando cese la escritura concurrente**»

**Por qué es un defecto.** El precedente de `a.9` tiene **cinco** pasos y el quinto es una salida: el reintento posterior. F4 toma el número y **suprime la salida**, sustituyéndola por una prohibición contractual —«el contrato no lo admite y el validador lo rechaza» (L905)—. Presentar eso como «el precedente que el corpus ya resolvió una vez» es una cita que invierte lo citado, y es precisamente la supresión que produce `B1`.

**Qué exigiría cerrarlo.** O conservar la salida del precedente —reintento en un ciclo posterior, con su registro—, o declarar explícitamente que se aparta de `a.9` en ese punto y con qué motivo, y proveer la salida alternativa que `B1` exige.

---

### MENORES

| id | cita | por qué |
|---|---|---|
| `m1` | L345: «`<EV-ID>.md` **APPEND ONLY. Nadie los edita**: se emiten» · L2459: «el CONTRATO —**append only**, id único, **nunca se edita**— no cambia» | Dos frases **vigentes**, no marcadas como históricas, que vuelven a prometer el append-only físico absoluto que `D63` retira: §2.9 L2294 declara que «el diario **FÍSICO no es estrictamente append-only**» y que la lápida «SÍ EDITA FÍSICAMENTE UN FICHERO EXISTENTE» bajo `estado/eventos/`. Cerrarlo: reescribir ambas con la excepción tipada. |
| `m2` | L5926: «El resultado son **cuatro vigentes**, una retirada y una fusionada» sobre «las cinco de la entrega anterior» (L5923) | 4+1+1 = 6 ≠ 5. De `PN-1`–`PN-5` resultan tres vigentes, una retirada y una fusionada. Además contradice el cierre de §16 (L6159: «VIGENTES · OCHO») y §19 («`PN-6` a `PN-10` nuevas»). No cambia implementación. |
| `m3` | L5652: «## 15.2 · Los **veintiséis** apartados de la directiva» | La tabla tiene 32 filas y traza los apartados 2–23: **22 de los 26**. Sin fila: 1, 24, 25 y 26 — y `§24` («Reglas para interpretar esta directiva») sí se usa, citada como «regla 6 de la directiva» en §10.2 y «regla 16.1» en §7.1. |
| `m4` | L6288–6291: «NADA ESTÁ PROBADO los doce escenarios de §14, las CUARENTA Y DOS filas …, las NUEVE ventanas `R1`–`R9` … y los ONCE escenarios negativos de §11.5» | El censo de lo no probado omite las **ocho** comprobaciones `X-A`–`X-H` de §2.9, que la propia §2.9 declara «contrato de prueba igual que aquéllas» y «ninguna se ha ejecutado». |
| `m5` | L1770–1772: «`E2.7` y §2.11 **admiten expresamente** dos máquinas sobre el mismo control repo» | `E2.7` (verificada íntegra) no menciona máquinas: enumera «runtime distribuido · locks multi-agente · scheduler · colas …». La lectura es defendible; «expresamente» no lo es. |
| `m6` | L1338–1347 (`X47`): «Las excepciones son **exactamente ésas**» | `CHECKPOINT-ADS-NEXT.md` (L326, L365) cita `abortada` y no figura en la lista declarada exhaustiva. Son citas históricas, no un enum, luego el riesgo es nulo; la exhaustividad declarada, no. |
| `m7` | L1690: «Mismo disco, misma clasificación — **las diecisiete ventanas** contra UNA sola función» | La tabla que sigue proyecta 17 `W` **y** 9 `R` = 26 ventanas. El título subcuenta lo que la tabla hace bien. |

---

## 6 · Hallazgos que intenté y NO pude reproducir

Esta lista es parte del entregable: registra lo que sospeché y lo que la comprobación mecánica desmintió.

| qué sospeché | qué encontré | por qué lo descarto |
|---|---|---|
| Que las cardinalidades `3 / 3+2k / 8` no cerraran | Derivé las cuatro secuencias a mano: 3, 5, 7, 9 y 8. Todas cuadran con la tabla, con las secuencias de L935–981 y con el invariante `#observaciones = #intentos (+1)` | **No reproducido.** El recuento es correcto |
| Que hubiera un cuarto intento alcanzable | `intento` ∈ 1..3 en el esquema (capa A), y el validador del diario (capa B) prohíbe toda `reconciliacion-preparada` que resuelva un `conflicto` agotado | **No reproducido.** Cerrado en dos capas |
| Que alguna transición saliera de `derivada` | El grafo no la tiene; §3.6 lo asigna al validador semántico con el argumento correcto (exige recorrer el `tx`); `X57` lo comprueba | **No reproducido** |
| Que `confirmada` y `reconciliada` pudieran coexistir | Excluidas por ruta en §2.6.4 y reafirmadas en la capa B | **No reproducido** |
| Que faltara una ventana de caída | Proyecté las 17 `W` y las 9 `R` sobre la tabla de §2.6.9: cobertura completa, sin huecos ni duplicados | **No reproducido** |
| Que la tabla adversarial tuviera filas repetidas o el recuento fallara | 42 filas, 42 ids únicos | **No reproducido**, coincide con lo declarado |
| Que la matriz `tipo × fase` no particionara | 63 = 40 + 23, recomputado desde la tabla de nueve filas | **No reproducido** |
| Que `estado_iniciativa` `Q0`–`Q9` tuviera huecos o solapes | La derivé de cero contra los diez estados de `b.4`: total, y funcional por precedencia. El caso vacío cae en `Q4`; con bandera y sin items, en `Q2`/`Q3`, coherentemente | **No reproducido.** Es correcta |
| Que `D63` hubiera dejado promesas vivas sobre la lápida | Barrí «huella», «recomputable», «verificable», «eterna», «cadena». Los tres niveles están separados con rigor y las cuatro frases retiradas no reaparecen en texto normativo. Sólo sobreviven los dos restos de `m1`, que son sobre append-only, no sobre la lápida | **No reproducido** salvo `m1` |
| Que el contrato de identidad (§2.8) fuera circular o irreproducible | Representación canónica, exclusión de `id`, definición de `tx` sin definiendum circular, `identidad_v`, y la excepción tipada de la lápida con sus dos algoritmos disjuntos y distinguibles sin abrir otro fichero. Coherente | **No reproducido** |
| Que `§11` (`P-08`) tuviera un hueco de circularidad no declarado | Las dos huellas, la clave de caché por contenido y `NP-1`–`NP-11` son coherentes, y §11.4 declara honestamente el suelo abierto («si el runner miente, nada dentro del repositorio lo detecta») | **No reproducido** |
| Que la cobertura de la adopción (§8.2) dejara fuera alguno de los once puntos exigidos | Comprobé los once: repositorios (A1), código (A2/A3 y `LEE`), agentes/skills/instrucciones (INVENTARIO), documentación técnica/producto/UX-UI/despliegue/entornos (A6 e INVENTARIO), sistema de diseño (A6), trabajo abierto/gaps/ideas (A7), retirada controlada (A8 + RETIRADA SEGURA), trazabilidad conservada («el origen NUNCA desaparece»), reanudación entre chats (A0 + dosier), gate «puede empezar a programarse» (A10 = `O12`). **Los once están** | **No reproducido** |
| Que `O13` estuviera contradicho por §6.5 | §6.5 dice «Claude Code · Codex primer OBJETIVO … **NO CERTIFICADOS**» y «NINGÚN ADAPTADOR EXISTE HOY … el nivel alcanzado de todos es `desconocido`». Coincide literalmente con `O13` | **No reproducido** |
| Que `§4.2` duplicara `memoria.estado` con `cobertura.estado` | Están separados con la disciplina de los dos relojes, y el cruce de coherencia (incluida la fila `refutada` × `verificado` = INCOHERENTE) es correcto | **No reproducido** |
| Que el número de esquemas, capacidades, procesos, validadores o candidatos estuviera inflado | 19 / 15 / 10 / 13+2 / 29, todos verificados por conteo sobre el árbol | **No reproducido** |
| Que `O15` se desviara del mandato del Owner | Los seis puntos exigidos están presentes y literales; el punto 9 dice expresamente «**NO autoriza iniciar la adopción**» | **No reproducido.** `O15` es fiel |

---

## 7 · Limitaciones de esta revisión

```text
1  NO HE EJECUTADO NADA. Ni una prueba, ni un validador, ni el runtime — que no existe.
   Todo lo que digo sobre comportamiento es derivación sobre el texto, no observación.

2  DOS FICHEROS DEL CORPUS OBLIGATORIO quedan leídos en parte: `12-` y `13-`. Los usé para
   localizar hallazgos citados, no para auditar su corrección. Si alguno de aquellos
   hallazgos era erróneo, no lo detectaría.

3  CATORCE DE LAS QUINCE FICHAS de capacidad y NUEVE DE LOS DIEZ procesos están leídos por
   localización dirigida, no línea a línea. Una contradicción entre F4 y el interior de una
   ficha que yo no consulté podría habérseme escapado.

4  NO HE AUDITADO `pruebas/`, `packs/`, `tooling/`, `circuitos/`, `diseno/` ni `entrada/`.

5  NO JUZGO SI LA ARQUITECTURA FUNCIONARÁ. Nadie puede: la columna de uso real está vacía y
   F4 lo dice. Juzgo si es suficiente para que F5 redacte enmiendas y F6 construya.

6  MI LECTURA DE PROPORCIONALIDAD (`G2`) es un juicio arquitectónico, no un hecho mecánico.
   Lo señalo como tal: la carga de la prueba que reclamo es que F4 demuestre qué se pierde
   sin la ruta larga, no que yo demuestre que no se pierde nada.
```

---

## 8 · Veredicto

# **INSUFICIENTE PARA F5**

---

## 9 · Condiciones exactas para F5

El veredicto es de insuficiencia por **dos BLOQUEANTES y ocho GRAVES**, y cualquiera de los dos bloqueantes bastaría por sí solo. Además, cinco de los MEDIOS obligarían a F6 a tomar decisiones que F4 no toma. Éstas son las condiciones, ordenadas por lo que desbloquean.

### A · Obligatorias antes de que F4c pueda volver a revisarse

```text
C1  `B1` · SALIDA DEL CONFLICTO AGOTADO
    Declarar el acto, el registro, la autoridad y la retirada del marcador que sacan a una
    transacción de `conflicto(agotado: true)`. Sin ella, un solo conflicto agotado congela
    para siempre el commit del control repo, el despacho de sus items y `Continúa`.
    Revisar en consecuencia la justificación de `D38` para retirar `abortada`, que ya no
    cubre el espacio de estados, y corregir `X58`, que hoy exige el interbloqueo como
    resultado.

C2  `B2` · GOBIERNO GIT DEL CONTROL REPO
    Escribir la tabla de propiedad que §2.6.10 nombra: quién pide, ejecuta, bloquea y
    verifica rama, commit, push y PR del control repo, con qué evidencia. Declarar QUÉ RAMA
    recibe las escrituras del runtime, dado que la regla 3 protege `main` y no declara otra.
    Retirar la invocación de `G29` para el control repo o registrar la presión normativa
    correspondiente: `E2.4` acota `G29` a las fuentes con todas las letras.

C3  `G1` · LOS CINCO CONCEPTOS DE `a.9`
    Alinear la lista con `a.9` L675–679 y con `00-OBLIGACIONES-Y-CIERRE.md` L41, o declarar
    la desviación con su motivo. Hoy el esquema obligatorio de todo evento se construiría
    sobre un conjunto que su fuente no respalda.

C4  `G3` · CONTRATO DE `fallo`
    Dar a `fallo` los campos de referencia que garantía 6, §2.6.4 paso 1, `W16`, `X15` y
    `X28` le exigen, o retirar de esos cinco sitios la exigencia de nombrar `tx` y commit.

C5  `G4` · `G5` · `G6` · LOS MACROCIRCUITOS
    §8.3 gana `LEE` y `ESCRIBE`, y `M6` pasa a source changes gobernados por `C7`, por
    fuente, con gate, evidencia y rollback por fuente e `INTEGRACIÓN PARCIAL`.
    §8.4 gana `ESTADO`, incluida la sede y el plano de la instantánea de `U3`.
    Los cuatro declaran a qué proceso de `b.16` pertenecen sus items, o «plantilla de ruta»
    pasa la prueba de §3.1 y entra en el recuento.

C6  `G7` · EL SOPORTE DURABLE DE `N0`
    Declarar el item real que `N0` crea, con id tipado y proceso, y su referencia desde
    `INI-001`; o declarar dónde vive el checkpoint de una iniciativa sin paquetes, lo que
    exige revisar `D45`.

C7  `G8` · LAS DOCE ÁREAS
    Alinear §4.3 con las doce del §5.18 que `O8` resuelve, o registrar la sustitución como
    PRESIÓN NORMATIVA sobre `O8` —con la misma vara que `PN-6` y `PN-10`— diciendo qué
    ocupa el lugar del mapa documental.
```

### B · Obligatorias antes de que F6 empiece

```text
C8   `G2` · Demostrar, mecanismo a mecanismo, qué garantía profesional se pierde si la
     divergencia bajo transacción abierta se trata como la posterior al cierre —`deriva` más
     transacción nueva de reparación—. Si no se pierde ninguna, retirar la ruta larga: son
     tres fases, dos contadores, una bandera, nueve ventanas y cinco filas adversariales.
C9   `M1` · Definir la «política de publicación» o retirar la alternativa.
C10  `M2` · Definir `X32`–`X34` y `X42`, o reasignar sus referencias, y corregir la nota de
     huecos de §2.6.7.
C11  `M3` · Corregir la fila de `C6` en §15.7, como ya se hizo con `C7`.
C12  `M4` · Someter la retirada del puntero al régimen de §6.7 regla 2.
C13  `M5` · Restaurar la salida del precedente de `a.9`, o declarar el apartamiento.
```

### C · Editoriales, no bloqueantes por separado

`m1` a `m7`. Ninguno cambia implementación. `m1` es el más importante de los siete: dos frases vigentes vuelven a prometer el append-only físico absoluto que `D63` retira, y esa promesa es justo la que la sexta comprobación técnica existió para eliminar.

### D · Lo que NO exijo, y lo digo para que nadie lo lleve al Owner

```text
LAS OCHO PRESIONES NORMATIVAS `PN-1`, `PN-2`, `PN-3`, `PN-6`, `PN-7`, `PN-8`, `PN-9` y
`PN-10` están correctamente identificadas. Abrí las ocho fuentes y verifiqué las citas una a
una: `a.9`/`a.11` para PN-1, `b.15.1` y la taxonomía para PN-2, `G03` y su ausencia en `a.11`
para PN-3, `O12` para PN-6, `b.14` paso 2 literal para PN-7, la fila AUD de `b.16` y
`proceso:AUD` para PN-8, los dos predicados de `b.3` para PN-9, y `O11` para PN-10. Las ocho
tienen fuente exacta, contradicción exacta, alcance, qué bloquean y una materia mínima
suficientemente determinada para que F5 la redacte. `PN-4` está bien retirada y `PN-5` bien
fusionada, con sus motivos escritos y reinstaurables.

LA ÚNICA PRESIÓN QUE FALTA es la de `G8` sobre `O8`. Y hay un candidato a segunda, que
depende de cómo se resuelva `C2`: si el gobierno Git del control repo acaba exigiendo tocar
`G29` más allá de lo que `E2.4` ya revisó, eso sería presión normativa y no relleno de F6.

EL DEFECTO DE `C7` (§9.5) está bien clasificado: es material derivado de `E2.6`, su
prescripción está cerrada y su sitio es F6. Verifiqué `C7` L170 y `E2.6` literalmente.

LAS LIMITACIONES ABIERTAS DE §2.11 —tamaño de sellado, formato del diario, lock distribuido,
orden total entre máquinas, umbral de retirada de cuerpos— están acotadas y son no
bloqueantes para una adopción de un solo Owner y una sola máquina, que es el caso de `O15`.
```

---

## 10 · Nota final sobre `O15` y PesquerApp

`O15` está registrada con fidelidad: los seis puntos que el Owner decidió están todos, literales, en `DECISIONES-Y-CONTRADICCIONES.md` L267–322, incluido el noveno —«**NO autoriza iniciar la adopción**»—. No hay desviación que señalar.

Pero la pregunta que el veredicto tiene que responder no es si `O15` está bien transcrita, sino si **PesquerApp puede recibir hoy una adopción permanente y completa** con esta arquitectura. No puede, y por razones que no son de estilo:

- Su control repo nacería sin gobierno Git declarado, con `main` protegida y sin rama de trabajo declarada, y su estado no podría publicarse de forma gobernada (`B2`). Un repositorio de control **definitivo** cuyo estado sólo vive en local no es definitivo.
- Un solo conflicto agotado sobre un solo fichero congelaría permanentemente todo commit de ese repositorio, sin salida representable (`B1`). En una instalación que por decisión del Owner **no se rehace**, un estado sin salida no es un incidente: es el fin de la instalación.
- Las fases `A0`–`A2` no tendrían soporte durable válido (`G7`) y sus items no tendrían proceso asignado (`G6`), justo en el tramo que `O15` declara «el hilo entre chats».
- Y si más adelante hubiera que migrar esa instalación permanente —la vía que `O15` punto 6 declara **la única** para incorporar mejoras—, el macrocircuito de migración no declara qué escribe ni gobierna su único paso destructivo sobre los repositorios del producto (`G4`).

`F4c` es un documento notablemente más riguroso que lo que sus siete encadenamientos de corrección sugieren: sus recuentos cuadran, su función de estado de iniciativa es total y disjunta, su matriz `tipo × fase` particiona, su contrato de identidad es reproducible y sus ocho presiones normativas están bien fundadas y listas para redactarse. Pero la cadena de correcciones ha vuelto a hacer lo que hizo las seis veces anteriores: **el texto más reciente introdujo el defecto más grave.** `D60` y `D62` cerraron el contador y abrieron el interbloqueo; `D63` corrigió la lápida y dejó vivas dos promesas de append-only; y el hueco que `D41` declaró honestamente en el gobierno Git del control repo se rellenó, tres reglas más abajo, por la misma inferencia que la declaración prometía no hacer.

`F4c` sigue **ABIERTA**.
