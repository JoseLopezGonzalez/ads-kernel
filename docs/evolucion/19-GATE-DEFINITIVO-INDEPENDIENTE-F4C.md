# GATE DEFINITIVO INDEPENDIENTE DE F4c

> **Veredicto, en una línea:**
> # INSUFICIENTE PARA F5
>
> **`F4c` sigue ABIERTA. `F5` NO queda autorizada.**

## 1 · Identidad y procedencia

```text
BASE INMUTABLE      review/f4c-candidate-20260828-r4
                    0ea04514f1f6d7f99b1bade980b349771b7f3194
                    verificado con `git ls-remote` ANTES de empezar
RAMA DEL GATE       gate/f4c-definitivo-20260829, creada en ese SHA exacto, sin upstream

REVISOR J           arquitectura, estado, protocolo, recuperación, concurrencia, Git,
                    fuentes de verdad, tipos, proporcionalidad y recursos
REVISOR K           capacidades, procesos, composición, handoffs, macrocircuitos,
                    documentación, adopción, PesquerApp, presiones F5 y contratos F6
ADJUDICADOR L       recibe ambos dictámenes YA CERRADOS y emite el veredicto único

INDEPENDENCIA       los tres son agentes NUEVOS con contexto limpio. Ninguno escribió F4,
                    ninguno aplicó D1–D95, y ninguno es revisor A–I de los gates
                    anteriores. J y K trabajaron EN PARALELO y no se vieron.
                    L NO resolvió por mayoría: verificó cada afirmación material contra su
                    fichero y su línea, y RECHAZÓ lo que no se sostuvo.

EL COORDINADOR      sólo coordinó, derivó cifras de contraste, transcribió y validó.
                    NO emitió suficiencia y NO corrigió ningún hallazgo.
                    Es el autor material de tandas anteriores, y por eso su juicio no
                    cuenta aquí.
```

**Qué hizo el coordinador, y qué no.** Verificó el SHA remoto antes de empezar; derivó el inventario de Git; repartió el corpus garantizando cobertura asignada del 100 %; generó los manifiestos con líneas y SHA-256; derivó cifras de contraste **sin copiarlas del checkpoint**; comprobó por su cuenta las afirmaciones más consecuentes de J, de K y de L; y transcribió los tres dictámenes. **No juzgó.**

**Una comprobación del coordinador que corrigió a un revisor.** J declaró 45 filas adversariales y el coordinador derivaba 53. Resuelto contra la fuente: **J tiene razón** — el patrón del coordinador mezclaba tres tablas distintas (45 en §2.6.7, más 8 `X1`–`X8` y 8 `X-A`–`X-H` en otras). Se deja escrito porque el error era del coordinador.

## 2 · Inventario y cobertura

Derivado de `git ls-files`, no copiado de ningún gate anterior.

```text
FICHEROS VERSIONADOS                318

LECTURA SEMÁNTICA OBLIGATORIA       286
EVIDENCIA DERIVADA                   15   pruebas/evidencia/ y los dos *-generado.md
HISTÓRICO INMUTABLE                  12   packs/legacy-1.3.0, a-EQUIPOS-v1/v2/v3,
                                          auditorías y correcciones cerradas
NO APLICABLE                          5   .gitignore, .upstream-hash, VERSION, fixtures

REPARTO
  fuentes centrales, AMBOS            15   24 700 líneas
  lote propio de J                    83   20 346 líneas
  lote propio de K                   193   30 200 líneas
  UNIÓN                              286   = 286 obligatorios · 0 sin asignar
```

**La cobertura ASIGNADA fue del 100 %. La cobertura LEÍDA no.** Los tres declararon lectura parcial, contra su propio interés, y L lo convirtió en la primera razón del veredicto. El detalle está en sus dictámenes y en §7 de la adjudicación.

---

## 3 · Dictamen literal del REVISOR J

> Transcrito **sin suavizar y sin resumir cambiando el sentido**. Lo emitió J; el
> coordinador sólo lo transcribe.


**Ámbito:** arquitectura, estado, protocolo transaccional, recuperación, concurrencia, Git, fuentes de verdad, tipos, proporcionalidad y recursos.
**Árbol:** `0ea04514f1f6d7f99b1bade980b349771b7f3194`, rama `gate/f4c-definitivo-20260829`, árbol limpio verificado con `git status --porcelain` (vacío) antes y después de mi trabajo. **Modo: SÓLO LECTURA.** No he modificado ni un fichero, no he hecho commits. Ejecuté validadores; ninguno mutó el árbol (comprobado: `git status` sigue vacío).

#### 1 · EVALUACIÓN PROPIA PROVISIONAL

*Escrita y guardada ANTES de abrir 12, 13, 14, 15, 16, 17, 18 y la matriz de los 43.*

> **Impresión general.** El protocolo transaccional de §2 es, con diferencia, la pieza mejor construida. Distingue con precisión atomicidad, durabilidad de proceso, durabilidad de máquina, commit local, push y clon nuevo; nombra el error clásico del `fsync` de directorio; separa estado ESTABLE de ESPECULATIVO; y declara lo que NO ofrece (aislamiento de lecturas, reanudación exacta distribuida). El autómata de cinco fases es cerrado y sin estado sin salida. La honestidad es alta y sistemática.
>
> **Hallazgos propios provisionales:**
> 1. GRAVE — `tx` es huella de la intención y EXCLUYE `predecesor`. Una reparación posterior a `abandonada` con intención idéntica produce EL MISMO `tx`. La regla de reintento la convierte en NO-OPERACIÓN y la capa B la rechaza por posterior a terminal. El `deriva` no puede resolverse por su camino natural.
> 2. MEDIO — dos formulaciones incompatibles del `hash_previo` de la transacción de reparación: §2.6.9 «lo que hay en la base restaurada» vs §2.6.11 «el `hash_observado` que la deriva registró».
> 3. MEDIO — §6.7 reasigna su comprobación adversarial a `X51`, cuya fila cubre otro escenario.
> 4. MEDIO — los validadores de recuento y versión se apoyan en censos ESCRITOS A MANO; su cobertura no deriva. Instancias vivas: «veintiocho campos» (29), «KERNEL.md versión 1.3.0» (1.5.0).
> 5. MENOR — 45 filas adversariales declaradas en §2.6.7 y 42 en §2.9 y en §19.
> 6. MENOR — «Ninguna lo redeclara» no es literal: §2.5 y §2.9 reenuncian la condición inline.
> 7. MENOR — (b) L358 cita «(P7)» donde aplica P9; (b) L468 numera 1,2,5,3,4.
> 8. MENOR — checkpoint: `actualizado: 2026-08-28` con `last_meaningful_event` 2026-08-29.
> 9. MEDIO/portabilidad — en Python 3.10 fallan 3/13 validadores y 54/57 tests de workspace.
>
> **Veredicto provisional:** SUFICIENTE PARA F5 con reservas, condicionado a resolver los hallazgos 1 y 2 antes de aprobar §2 como (g).

**Qué cambió después de leer 15–18 y de seguir investigando:**

- El hallazgo 1 **se profundizó y cambió de causa**. Al buscar qué campo podría distinguir dos intenciones idénticas encontré `revision_base` — y descubrí que **no está declarado en §3.6**. Eso convierte el hallazgo 1 en consecuencia de un defecto mayor y anterior, que es ahora mi hallazgo principal `J-01`.
- Mi veredicto provisional era **erróneo en su forma**: no había contabilizado honestamente mi propia cobertura. Al hacerlo, cambia.

#### 2 · EVIDENCIA DE LECTURA

##### 2.1 · Leído ÍNTEGRO

`kernel/KERNEL.md` (1590) · `a-CAPACIDADES-APROBADA.md` (1132) · `b-RECORRIDO-APROBADA.md` (1288, falta ~5 líneas de b.15 paso 4) · `a-ENMIENDA-E1-ENC.md` (211) · `a-ENMIENDA-E2-MULTIREPO.md` (230) · `kernel/operativo/00-INDICE.md` (139) · `contratos/00-INDICE.md` (29) · `C1` (161) · `C3` (150) · `C4` (170) · `C5` (115) · `C6` (336) · `C7` (250) · `docs/evolucion/00-INDICE.md` (105) · `07-DECISION-MULTIREPO.md` (150) · `08-EVIDENCIA-MULTIREPO.md` (96) · `15-TERCERA-REVISION-INDEPENDIENTE-F4C.md` (651) · `kernel/VERSIONES.md` (74) · `verificacion/README.md` (102) · `plantillas/SOURCES.toml` (91) · `plantillas/INTEGRATION-SET.md` (65) · `plantillas/CHECKPOINT.md` (67) · 16 esquemas (~500) · `comprobar_recuentos.py` (227) · `comprobar_versiones.py` (125) · `tooling/workspace.py` (814, parcial por mapa de funciones).

##### 2.2 · `11-ARQUITECTURA-INTEGRADA.md` — leído POR TRAMOS, **NO íntegro**

ÍNTEGRO: 1–3600 · 5247–5570 · 5564–5835 · 6680–7239 · 7239–7420 y 7595–8437. Casi íntegro: 3600–4340.

**NO LEÍDO (~2 300 líneas):** §4 contrato documental (4330–4618) · §5 auditoría (4618–5102) · §6.1–§6.6 adaptadores (5102–5247) · §8.1–§8.4 cuerpos de los macrocircuitos (5835–6517) · §9.1–§9.4 certificación (6517–6680) · §13 aprendizaje (7149–7211) · §14 escenarios (7211–7239) · §15.8 detalle de `D34`–`D86` (7420–7595).

##### 2.3 · HONESTIDAD BRUTAL — lo que NO leí íntegro, y era mío

**De las quince fuentes centrales, leí íntegras nueve. NO leí íntegras seis:**

- `11-ARQUITECTURA-INTEGRADA.md` — ~2 300 de 8 437 líneas sin abrir.
- `16-GATE-FINAL-INDEPENDIENTE-F4C.md` (1 257) — **sólo barridos dirigidos**.
- `17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` (1 650) — **sólo barridos dirigidos**. No leí la matriz de los 43 fila a fila.
- `18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` (3 665) — leí ~450 líneas. **No leí los dictámenes de `G` y `H` completos, ni §5.4–§5.11, ni §6, ni §7, ni la tabla completa de las 43 filas.**
- `CHECKPOINT-ADS-NEXT.md` (1 626) — leí ~250 líneas.
- `ADS-PENDIENTES…md` (2 163) — **sólo §5.18–§5.19**.
- `DECISIONES-Y-CONTRADICCIONES.md` (556) — leí `D87`–`D95`, `O15`, `O16` e índice. **`D16`–`D86` no línea a línea.**

**De los 83 ficheros de mi lote propio (20 346 líneas) leí íntegros o casi íntegros unos 25.** No abrí, o abrí sólo por barrido: `C2` (539) · `06-CONTRASTE.md` (488) · docs 12, 13, 14 (sólo estructura) · `README.md` · `docs/owner/ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` (3 343) · `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` (597) · `BOOTSTRAP_PROMPT.md` · `PROFILE_TEMPLATE.md` · `PROJECT_TEMPLATE.md` · `KERNEL_CHANGELOG.md` (parcial) · plantillas ENCUADRE/CIERRE/DEVOLUCION/DICTAMEN · **los siete ficheros de `pruebas/`** (~1 500) · esquemas `veto` `pack` `encuadre` (parciales) · `exclusiones.yaml` `reglas.yaml` · **once de los trece validadores** · los tres `.sh` de tooling · **`test_workspace.py` (973) — lo EJECUTÉ, no lo leí** · **la batería (477) — la EJECUTÉ tres veces, no la leí línea a línea**.

**Estimación honesta: leí en torno al 40 % de mi lote propio y en torno al 70 % de las fuentes centrales.**

**Consecuencia, que asumo:** por la regla del encargo, **mi cobertura sola ya determina el veredicto**, con independencia de los hallazgos. Lo digo antes de dar el veredicto para que no parezca una excusa posterior.

##### 2.4 · Ejecución real (sólo lectura)

```text
batería                → 30/30, exit 0, desde la raíz y desde /tmp por ruta absoluta
registrar_evidencia.py → 10/13 en verde, 3 problemas
comprobar_contratos    → 18 superadas · 0 fallidas
comprobar_recuentos    → T151 SUPERADA
comprobar_evidencia    → T158 SUPERADA
comprobar_negativos    → 67 detectadas · 0 NO detectadas
comprobar_fuentes      → T159 FALLIDA · T160 T161 SUPERADAS
comprobar_arranque     → T171 SUPERADA · T148 FALLIDA
test_workspace.py      → Ran 57 · FAILED (49 fallos, 5 errores)
python3 --version      → 3.10.12
git status --porcelain → vacío, antes y después
```

**Las 54 fallas y las 3 de validadores tienen una sola causa: `tomllib` no existe en 3.10.** Está declarado en `08-EVIDENCIA-MULTIREPO.md` y en §19 como `A14`, con propietario `PLT` y fase F6. **La declaración es exacta y honesta.**

#### 3 · RESPUESTAS 1–20

**1 · fuente de verdad única:** SÍ, con una excepción que no cierra. `revision_base` no tiene sede. Ver `J-01`.
**2 · durable/operacional:** SÍ. Dos categorías y dos excepciones de RUTA declaradas. Verificado y correcto.
**3 · `abierta(tx)` una semántica:** SÍ. Declarado una vez en §2.6.1; nueve sedes citantes derivadas por mí.
**4 · estados no terminales con salida:** SÍ. Derivé el grafo: no hay nodo no terminal sin sucesor. `B1` realmente cerrado.
**5 · terminales retiran marcadores:** SÍ, los dos. Laguna menor: `J-09`.
**6 · restauración sin publicar mezclas:** SÍ, y muy bien hecho. Pero descansa sobre `revision_base` — `J-01`.
**7 · pérdida de máquina declarada:** SÍ, ejemplarmente. «REINICIO SEGURO, no reanudación, y no se llama de otra manera».
**8 · sellado/retirada/identidad:** SÍ. «el diario FÍSICO no es estrictamente append-only», dicho sin adornos.
**9 · lápida con garantías honestas:** SÍ, de lo mejor del documento. Tres niveles separados.
**10 · hashes/predecesores/idempotencia implementables:** NO del todo. `J-01` y `J-02`.
**11 · gobierno Git del control repo suficiente:** SÍ. §2.6.10 escribe la tabla que `C7` no tiene; `O16` le da sede.
**12 · `C7` acotado a las fuentes:** SÍ, y su único defecto está bien clasificado como derivado con prescripción cerrada.
**13 · multi-repo 0/1/N:** SÍ. Verificado contra `C6` N4, la plantilla, `workspace.py` y §9.5.
**14 · `P-08` suficiente para F6:** SÍ. Dos huellas, cierre transitivo calculado, suelo abierto dicho.
**15 · proporcionalidad:** PROPORCIONAL, y demostrado en vez de afirmado. `D64` retiró maquinaria.
**16 · optimización de contexto:** SÍ en el diseño, con coste declarado.
**17 · base profesional, no MVP:** SÍ. `O15` y §18 lo fijan; §19 no disimula.
**18 · decisiones sin atribuir:** NO, salvo `J-01`: la sede de `revision_base` no está atribuida porque nadie advirtió que falta.
**19 · `D87`–`D95` correctas:** SÍ, verificado uno a uno en su sede. `D67` restaurada byte a byte. Ninguna reescribe `D1`–`D86`.
**20 · batería/runner/checkpoint:** batería PORTABLE (30/30 en dos ubicaciones); runner reproducible en comportamiento, 10/13 en 3.10; checkpoint vigente con dos restos (`J-10`).

#### 4 · HALLAZGOS

##### `J-01` · **GRAVE** · `revision_base` sostiene la mitad del protocolo y no está declarado en el contrato de evento

`11`:604, 608, 1655, 1798, 1808, 1817, 1867, 2391, 2555, 5482, 5520 — **y ninguna en §3.6 (3589–4270)**.

> `11:604` — «`5 REVISIÓN BASE DECLARADA  `revision_base` en `preparada`: el `HEAD` del punto 2`»
> `11:2391` — «`abandonada` es INALCANZABLE hasta haber RESTAURADO todas sus rutas a `revision_base` y haberlo **verificado byte a byte**»
> §3.6, fila `preparada` y campos comunes: **`revision_base` no aparece.**

`revision_base` es condición 5 de arranque, ancla exacta de la restauración, lo que hace `abandonada` alcanzable, y el sostén de «`main` nunca contiene estado parcial» y de la rama REVERTIR de `PN-7`. **Un esquema derivado literalmente de §3.6 acepta un `preparada` sin él.** Es la clase exacta de `A1`, que el gate final graduó BLOQUEANTE. Lo introdujo `D69` sin propagarlo a §3.6. El adjudicador `I` examinó `D69`, citó `revision_base` cinco veces y verificó la fila correcta — sin advertir la ausencia.

**¿Bloquea F5? SÍ.** `PN-1` propone aprobar §2 como (g). **La corrección son cinco líneas y no hay nada que decidir.**

##### `J-02` · **GRAVE** · el `tx` de una reparación de intención idéntica colisiona con el de la transacción abandonada

`11`:2749-2752, 4180-4183, 1905, 2613, 4137.

Tras un abandono, la restauración deja todas las rutas en `previo`. La reparación natural declara el mismo `afecta[]`, hashes, orden y procedencia; `predecesor` e `id` están excluidos del cómputo. **Su `tx` es el mismo** → la regla de reintento la vuelve NO-OPERACIÓN, y la capa B la rechaza por posterior a terminal. `bloqueado_por_deriva(item)` nunca se vuelve falso por ese camino. Es la clase de `B1` desplazada al contrato de identidad.

**Causalmente unido a `J-01`:** el único campo que distinguiría las dos intenciones es `revision_base`. **Declararlo y decir que entra en el cómputo de `tx` cierra los dos a la vez.**

##### `J-03` · **MEDIO** · §6.7 reasigna su comprobación adversarial a `X51`, cuya fila cubre otro escenario

`11`:5400-5406 frente a `11`:1437. `X51` verifica una deriva no transaccional; nada que ver con que la adopción no escriba en las fuentes antes de `A8`. `M2` señaló referencias inexistentes; el remedio las reasignó a una fila **existente pero ajena**. No bloquea F5.

##### `J-04` · **MEDIO** · dos formulaciones distintas del `hash_previo` de la reparación

`11`:1906 («lo que hay en la base restaurada») frente a `11`:2610 («el `hash_observado` que la deriva registró»). Coinciden sólo para `abandono-de-transaccion`. La formulación general correcta es la de §2.6.11. No bloquea F5, pero cae dentro de §2, que es lo que (g) aprobará.

##### `J-05` · **MEDIO** · los validadores de recuento se apoyan en un censo ESCRITO A MANO

`comprobar_recuentos.py`:107-156 · instancias vivas: `contratos/00-INDICE.md`:7 y `T086-T092-contratos.md`:14 dicen «veintiocho campos»; `esquemas/rol.yaml` tiene **29**. `T151` sale SUPERADA mientras dos sedes vigentes afirman una cifra que el corpus desmiente. Es lo que el propio corpus condena en `comprobar_fuentes.py`: «nunca una lista escrita a mano, que es lo que envejece». No bloquea F5.

##### `J-06` · **MENOR** · `kernel/operativo/00-INDICE.md`:134 declara `KERNEL.md` «versión 1.3.0»; es 1.5.0

`T152` sale SUPERADA porque sólo recorre `README.md` y `START_HERE.md`. Misma causa que `J-05`. No bloquea.

##### `J-07` · **MEDIO** · tres recuentos declarados en 42 cuando el conteo da 45

`11`:1475 correcto (45), frente a `11`:1491, `11`:3173 y `11`:8298 (§19). **Es una regresión de esta tanda:** `c63df21` cambió unas y dejó otras, editando la línea 3173 dieciséis líneas por debajo de donde acababa de escribir cuarenta y cinco. Es la clase que `I-19` cerró en esta misma tanda. Cae en §19, donde un gate lee qué está probado. `G-26` no lo ve: compara `filas == ids`, no `prosa == derivado`. No bloquea F5, pero es el **undécimo** eslabón de «la corrección introduce el defecto».

##### `J-08` · **MENOR** · dos restos editoriales en (b), material APROBADO

`b`:358 cita «(P7)» donde aplica `P9`; `b`:468 numera 1,2,5,3,4. Su sede es material APROBADO, luego su remedio es **F5**, y hoy no está registrado.

##### `J-09` · **MENOR** · no se nombra la salida «aceptar lo divergente» para cerrar un `deriva`

##### `J-10` · **MENOR** · la cabecera del checkpoint va una tanda por detrás de su cuerpo

Línea de estado nombra el GATE FINAL sin mencionar el GATE DE CIERRE; `actualizado: 2026-08-28` con `last_meaningful_event` de 2026-08-29. `a.10` regla 3: «un checkpoint desactualizado es un defecto del sistema, no una omisión menor».

##### `J-11` · **MEDIO** · la guardia de versión de intérprete que §19 declara no existe

En 3.10 el runner da 10/13 y la suite 54 fallos, **y la evidencia publicada sigue afirmando 13/13 y pasando `T158`** — el defecto que `P-08` diseña para cerrar con la huella de entorno, todavía no construida. Es F6.

#### 5 · REEVALUACIÓN DE LOS HALLAZGOS PREVIOS

**CONFIRMO cerrados, verificados uno a uno:** `B1` (retirando maquinaria, no parcheándola) · `B2` (§2.6.10 + `O16` + `PN-11`; verifiqué que ninguna fila de `C7`:80-92 alcanza al control repo) · `G1` · `G2` (la tabla garantía a garantía es la carga de la prueba que pedía) · `G3` · `A1` · `A2` · `I-01` (sin crear tercera fuente de verdad) · `I-02` (la NORMA cambió, no sólo su explicación) · `I-04` · `I-16` (`D67` restaurada byte a byte) · `M-8`/`A11`.

**RECHAZO o matizo:** `M2` cerrado sólo a medias (`J-03`) · `m4` corregido pero el censo sigue incorrecto por otra vía (`J-07`) · `I-09` cerrado en lo material, no en su literalidad · **doc 18 §5.3 «`D69` CORRECTO» — lo rechazo parcialmente: no alcanzó a comprobar que `revision_base` tuviera sede en §3.6** · doc 18 §5.2 «`X51` CORRECTO» correcto sólo para lo que verificó · doc 15 «§2.8 NO REPRODUCIDO»: buscó circularidad e irreproducibilidad, **no colisión entre transacciones distintas**.

**Lo que NO exijo:** el defecto de `C7` está bien clasificado como derivado, no es presión normativa · la excepción de `C6` en §15.7 es correcta · las doce presiones están bien fundadas, abrí las fuentes de nueve de ellas · `PN-4` bien retirada, `PN-5` bien fusionada · las limitaciones de §2.11 no bloquean el caso de `O15`.

#### 6 · PROPORCIONALIDAD Y COSTE

Proporcional, y esta tanda lo demuestra: `D64` retiró maquinaria; `D87` retiró la ruta en vez de darle plano; `D74` resolvió sin crear tipo. El recuento de tipos se calcula y se ha movido tres veces.

**Dónde el coste sí es alto, y se dice:** once tandas, tres revisiones, dos gates y un complemento. `J-07` muestra que el ciclo sigue produciendo defectos. **La corrección más barata no es más revisión: es derivar los censos escritos a mano** (`J-05`, `J-06`, `J-07` comparten causa). El corpus ya sabe cómo se arregla y no se lo ha aplicado a sí mismo.

#### 7 · LÍMITES

1. No he ejecutado nada del protocolo: no hay runtime. Todo es derivación sobre texto.
2. **Mi cobertura es incompleta** (~40 % de mi lote, ~70 % de las centrales), detallada en §2.3.
3. No adjudico §4, §5, §6.1–§6.6, §8.1–§8.4, §9.1–§9.4, §13 ni §14 del documento 11.
4. `J-01` depende de que `revision_base` y `base` sean campos distintos, que sostengo porque `11:1798` los trata como tales. Si se demostrara lo contrario, `J-01` bajaría a MEDIO y `J-02` quedaría cerrado.
5. `J-02` asume que la procedencia de una reparación puede ser idéntica a la original.
6. Los recuentos los derivé con `grep`, `awk`, `wc` y Python, y sólo después los comparé.
7. No juzgo si esto funcionará: la columna de uso real está vacía.
8. No pude adjudicar si las catorce fuentes que el gate anterior declaró sin leer refutan algo: yo tampoco las he leído todas.

#### 8 · RECOMENDACIÓN DE VEREDICTO

##### INSUFICIENTE PARA F5

**Falla por dos razones independientes, cualquiera bastaría.**

1. **MI COBERTURA NO CUMPLE.** ~40 % de mi lote propio y ~70 % de las centrales. Sobre esta muestra no puedo certificar que no haya algo que refute o agrave lo escrito.
2. **UN GRAVE DE FONDO, Y ES DE CONTRATO.** `J-01`: `revision_base` no está declarado en §3.6 ni en ninguna capa. `J-02` es su consecuencia sobre la identidad de `tx`. Es la clase de `A1`, que este mismo gate graduó BLOQUEANTE.

**Por qué bloquea F5:** `PN-1` propone aprobar §2 como (g). Aprobarla consagraría un contrato de evento que no puede representar el dato del que dependen su segundo terminal y su garantía de no publicar mezclas parciales. F6 tendría que **decidir su forma**, que es lo que el criterio de suficiencia excluye.

**Y por qué no es una condena de la arquitectura.** Es la candidata más sólida de la cadena: los dos BLOQUEANTES de la tercera revisión realmente cerrados, uno retirando maquinaria; los ocho GRAVES del gate de cierre cerrados en su sede, verificados uno a uno; `D87`–`D95` todas revisoras y `D67` restaurada byte a byte; batería portable y honesta sobre lo que no comprueba; doce presiones listas para que F5 redacte sin inventar arquitectura; externos con fichero, propietario, fase y condición de cierre; y limitaciones declaradas sin presentarse como demostradas.

**Condiciones de cierre:**

- `C-J.1` — `J-01`+`J-02`: declarar `revision_base` obligatorio de `preparada` en §3.6, registrable en `conflicto` y `abandonada`, y decir si participa en el cómputo de `tx`. **CINCO LÍNEAS. ES LA ÚNICA CONDICIÓN QUE BLOQUEA.**
- `C-J.2` — `J-04`: una frase, el `hash_previo` de la reparación es el `hash_observado` del `deriva`, para las tres causas.
- `C-J.3` — `J-03`: fila adversarial propia para §6.7, o registro como contrato de prueba F6.
- `C-J.4` — `J-07`: derivar las tres cifras, o retirar la afirmación de que derivan. Extender `G-26`.
- `C-J.5` — `J-05`/`J-06`: derivar el censo de `AFIRMACIONES` y el alcance de `T152`. F6.
- `C-J.6` — `J-08`: registrar los dos restos de (b) como material de F5.
- `C-J.7` — COBERTURA: un revisor con contexto limpio que lea íntegro lo que J no leyó.

**Advertencia final.** `J-07` es la undécima vez consecutiva que una tanda introduce un defecto de su propia clase declarada. Tres hallazgos —`J-05`, `J-06`, `J-07`— comparten una causa: **censos escritos a mano cuya cobertura no deriva de nada**. Mientras siga así, cada tanda dejará una cifra atrás y cada gate la encontrará.

---

## 4 · Dictamen literal del REVISOR K

> Transcrito **sin suavizar y sin resumir cambiando el sentido**. Lo emitió K; el
> coordinador sólo lo transcribe.


**Ámbito:** capacidades, procesos, composición, handoffs, macrocircuitos, documentación, adopción, PesquerApp, presiones F5 y contratos F6.
**Árbol:** `0ea04514f1f6d7f99b1bade980b349771b7f3194`, rama `gate/f4c-definitivo-20260829`. **Sólo lectura.** No he modificado ningún fichero, no he hecho commit y no he corregido nada.
**Integridad del corpus:** verifiqué las 208 entradas de `manif_central.tsv` y `manif_K.tsv` — líneas y SHA-256 — antes de leer nada. Coinciden todas. Ninguna cita de este dictamen procede de un fichero no verificado.

#### 1 · EVALUACIÓN PROPIA PROVISIONAL

*(Escrita antes de abrir los documentos 15–18.)*

> La arquitectura de mi lote es coherente, completa en lo esencial y proporcionada. Las quince fichas tienen los doce campos de `a.1` (comprobado mecánicamente, 15/15). Los cuatro macrocircuitos declaran sus catorce campos. Los diez procesos tienen propietario derivado, obligatorias y condicionales comprobables. `C5` se autolimita correctamente a la forma. Los diecisiete handoffs son instancias, no composiciones. La distribución preestructurada reduce trabajo de instalación sin cerrar contenido de producto. Las doce áreas obligatorias y las trece condicionales casan con `§5.18`.
>
> Provisionalmente: **SUFICIENTE PARA F5**, con once hallazgos, ninguno bloqueante.

**Qué cambió tras leer 15–18.** Dos de mis once hallazgos provisionales cayeron al verificarlos. Y uno de los que sobrevivió —el de `<CAP>:revision`— se agravó al leer `D92`: no es una omisión, es una **regla de derivación que no puede alcanzar el caso que ella misma señala como el más expuesto**. Eso, sumado a mi cobertura incompleta del corpus central, invierte mi conclusión provisional.

#### 2 · EVIDENCIA DE LECTURA

##### Leído íntegro

(a) 1132 · (b) 1288 · E1 211 · E2 230 · `DECISIONES-Y-CONTRADICCIONES.md` 556 · `11-ARQUITECTURA-INTEGRADA.md` 8437 · `KERNEL.md` 1590 · `kernel/operativo/00-INDICE.md` 139 · `docs/evolucion/00-INDICE.md` 105 · las 15 `CAPACIDAD.md` · las 15 `composicion.md` · 36 contratos de rol · 35 métodos · 35 prompts · `circuitos/00-CIRCUITOS.md` 240 · `DIS-handoffs.md` 247 · `handoffs-generales.md` 245 · `recorrido/00-OBLIGACIONES-Y-CIERRE.md` · `01-PROCESOS.md` 564 · `diseno/00`–`05` · `entrada/00`–`05` · packs (18) · `kernel/templates/` (3) · docs 01,02,03,04,05,09,10 · `ADS-NEXT-OWNER-BRIEF.md` 1341 · `PROMPT-ARRANQUE` · `START_HERE.md` · `docs/rediseno/README.md`.

##### Leído en parte

`CHECKPOINT-ADS-NEXT.md` (1626): cabecera L1–26 · `## Estado de las fases` L830–871 íntegra · tandas 9ª y 10ª L1172–1450 · matriz L1196–1300 · `Siguiente acción exacta`. **No leí L27–829 ni L872–1171.**
`15-…` (651): §1–§5 íntegras + todos los encabezados. **No leí §5 desde `G6`, ni §6–§10.**
`16-…` (1257): encabezados · hallazgos por título · cobertura de B · L1143. **No leí los tres dictámenes íntegros.**
`17-…` (1650): encabezados · `E-1`–`E-10` por título · `E-4` íntegro · tabla L1294–1310 · matriz L1415–1425. **No leí los dictámenes de D y E íntegros.**
`18-…` (3665): encabezados · `M-3` íntegro · externos L2069–2074 · matriz L2733–2740 · inventario L144–209. **No leí los dictámenes de G y H, ni la adjudicación de I.**

##### DECLARACIÓN DE COBERTURA INCOMPLETA — sin adorno

**No leí íntegro `ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md`, que es fuente central obligatoria.** De sus 2163 líneas abrí el índice, `§4.5`–`§4.11`, `§5.5`–`§5.6`, `§5.9`–`§5.13`, `§5.18`–`§5.19`, `§5.24`, `§6` y `§7`. **No abrí `§1`–`§3`, `§4.1`–`§4.4`, `§5.1`–`§5.4`, `§5.7`–`§5.8`, `§5.14`–`§5.17`, `§5.20`–`§5.23`, ni el BLOQUE B (§8–§12, certificación), ni el BLOQUE C (§13–§15, iniciativa y dosier vivo), ni nada a partir de §16.** Unas 1750 líneas sin leer, que incluyen la fuente del Owner para la **certificación por niveles** (P4, P10) y para la **iniciativa como unidad viva** (P9). **Mis respuestas a P9 y P10 no están contrastadas contra la directiva que las origina.**

**No leí íntegros los documentos 15, 16, 17 y 18** (~6000 líneas sin abrir). **No audito la corrección de esas cuatro pasadas.**

**Consecuencia, que asumo:** el encargo dice que la cobertura incompleta obliga a veredicto INSUFICIENTE. Mi cobertura del corpus central es incompleta. Eso, por sí solo y con independencia de mis hallazgos, determina mi veredicto.

#### 3 · RESPUESTAS 1–25 (resumen fiel)

**P1** casi: las cuatro vías de `D74` y el GATE DE COMPOSICIÓN; residuos en `PN-13`. Pero el gate comprueba contra los condicionales declarados, no contra `b.16` → K-02.
**P2** sí. Diez propietarios, tres derivados con regla; ejecutor/autoridad anclados a `C7` L80–92, verificado fila a fila; los cuatro vetos con sus seis campos, 4/4.
**P3** sí, y es ejemplar. `C5` define la forma, no las instancias. 17 instancias reales.
**P4** sí, los catorce campos en los cuatro. **Pero el contenido de dos es incorrecto:** K-03 y K-05.
**P5** sí en sustancia. Reserva: nadie reconcilia esto con el gate fijo de `G22` (K-06).
**P6** sí. `A0`–`A10`, con la disciplina de RETIRADA SEGURA fiel a `§5.6`.
**P7** sí, con dos defectos en `M`: K-03 y K-05.
**P8** sí, íntegramente. Los nueve puntos de `O15` literales; la cifra reanclada por nota al pie sin tocar la resolución.
**P9** sí, con la reserva de cobertura. `Q4` deja de contradecirse.
**P10** sí en la forma, misma reserva. Su autonomía real está bloqueada por `PN-2` y `PN-3`, y así se declara.
**P11** sí. Doce obligatorias verificadas una a una en L775–786; trece condicionales en L788–790. Diseño y datos son condicionales **por decisión del Owner**, no por omisión de F4.
**P12** sí. Proyecciones con huella; el puntero es proyección, no estado.
**P13** sí, y fiel a `§4.8`: «prepara los recipientes… sin inventarla».
**P14** sí. Sólo las doce reciben `aspecto:documental/<area>`.
**P15** sí. Las seis; el «+1 si `I-14`» no es indeterminación porque `D91` deriva el conjunto. Presentación floja (K-10).
**P16** **NO.** Es K-02.
**P17** sí. `PN-13` acotada por `D90`; `PN-14` con la sustitución en material aprobado y `F-02` dejando el vocabulario escrito.
**P18** **no del todo.** Falta el registro de la presión de `§8` sobre `G20`–`G23` (K-06).
**P19** todos menos uno: `D92` tiene propietario, fase, edición y prueba — y su regla y su prueba comparten el punto ciego.
**P20** sí, los siete con fichero, propietario, fase y condición. `F-04` sigue en `media` y **está bien que siga**.
**P21** sí, y con buen criterio. Sólo omite una tercera sede (K-11).
**P22** sí hasta donde verifiqué. Sospeché de `m-1`, **me equivoqué y lo retiro**. El recuento 31·2·2·7·1 = 43 cierra. Pero la matriz vive en un documento con el bloque de estado caducado (K-01).
**P23** sí. Ni `PN-1` obliga a inventar. Única laguna: el censo (K-06).
**P24** **NO, en un punto.** `D92` obliga a F6 a decidir si una obligatoria que aporta condiciones cuenta como `<CAP>:condiciones` a efectos de `b.16`. Es K-02.
**P25** sí. La asimetría de `DIS` está declarada como deuda en `A-30`. La repetición de prompts es excepción declarada. Es la parte más sólida de mi lote.

#### 4 · HALLAZGOS

##### `K-01` — El bloque de estado del checkpoint está caducado dos tandas, y dice DIEZ presiones donde hay DOCE — **GRAVE**

`CHECKPOINT-ADS-NEXT.md:867`, dentro de `## Estado de las fases` (L830).

> `F5  ENMIENDAS   DIEZ presiones normativas vigentes, enumeradas y sin redactar. NO INICIADA`

Su fila `F4` enumera las pasadas **hasta `D63`** y no menciona la tercera revisión, ni el gate final, ni el complemento, ni el gate de cierre, ni `D64`–`D95`. La 10ª tanda del mismo fichero dice **DOCE vigentes** (L1430) y su punto 5 dice «las **DOCE** presiones de §16» (L1606).

No cabe «no se reescribe historia»: esa regla protege el registro `D`/`O` y las resoluciones del Owner —y por eso `m-1` se cerró con nota al pie, correctamente—, no un bloque cuyo cometido es declarar el estado presente. La cabecera superior sí está mantenida.

**Consecuencia.** Quien reancla desde el checkpoint recibe un censo que omite `PN-13` y `PN-14`: la que bloquea componer `INS-5` y `A9`, y la que corrige material aprobado en `a.6` L495 y `b.16` L895. **No bloquea F5. Falsea su punto de partida.**

##### `K-02` — La regla que `D92` entrega a F6 para derivar `<CAP>:revision` no puede alcanzar `proceso:DEP`, y su propia prueba comparte el punto ciego — **GRAVE**

`11-ARQ:8387-8392` · `01-PROCESOS.md:369-373` · `a-CAPACIDADES-APROBADA.md:501`.

`D92` prescribe derivar el conjunto con **un barrido de `:condiciones`**. El barrido es correcto en su cuenta (4 `DOM:condiciones` + 4 `SEG:condiciones`). **Pero `proceso:DEP` hace participar a `SEG` por otra vía:**

> ```
>   - id: condiciones-de-seguridad
>     capa_exigida: la capa de SEG/Dependencia ANTES de construir
>     capacidad_productora: "SEG"
> ```

Es una **obligatoria**, no un condicional. La cadena `SEG:condiciones` no aparece en `DEP`, luego el barrido no la ve. Y la norma aprobada está escrita sobre el hecho, no sobre la notación: `a.6:501` — «**DOM y SEG aportan condiciones antes de construir y revisan después**».

**Tres razones encadenadas:** (1) `U5b` **es** `proceso:DEP`, y `D92` nombra a `U5b` entre los tres tramos donde la ausencia importa — «y son los tres tramos que escriben en las fuentes del producto». La regla no llega al tramo que ella misma señala. (2) La prueba que `D92` prescribe reproduce el punto ciego: pasaría en verde sobre un árbol sin `SEG:revision` en `DEP`. (3) **Lo introdujo una corrección anterior:** `D75` cerró `G-1` moviendo `SEG` a `obligatorias`, eliminando la cadena de la que `D92` dependería después.

**No bloquea F5. Bloquea la premisa de que F6 construye sin decidir arquitectura** (P24).

##### `K-03` — El gate del único paso destructivo exige CUATRO salidas donde su propia sección, y la directiva del Owner, exigen CINCO — **GRAVE**

`11-ARQ:6271` · `6273-6274` · `6296-6298`.

> `GATES` — «`M7` no cierra sin las **cuatro salidas verdes**»
> `EVIDENCIA` — «salidas de **build, pruebas, CI y despliegue** en `M7`»
> `M7 VERIFICAR` — «build, pruebas, CI, despliegue y **comportamiento agentic, los cinco**»

Y `ADS-PENDIENTES §5.6`: «Comprobar build, pruebas, CI, despliegue y **comportamiento agentic** tras cada retirada.»

**`M6` retira de cada fuente kernel, packs y organización de ADS.** Build, pruebas, CI y despliegue pasarían igualmente en una fuente a la que le han quitado su organización ADS: **la única de las cinco que interroga lo que `M6` retira es precisamente la que el gate omite.** No bloquea F5; deja el único paso destructivo con un gate que no cubre su propio riesgo.

##### `K-04` — La nota que reconcilia el recuento de externos afirma la cifra que el párrafo anterior retira — **MEDIO**

`11-ARQ:8332` («SIETE»), `8338` («Eran OCHO, y ahora son SIETE»), `8344` («la tabla tiene NUEVE filas y los externos son OCHO»). Derivado: 7 externos + 2 no externos = 9. La nota reconcilia 9 = 8 + 1, contando `F-01` entre los externos seis líneas después de declarar que dejó de serlo.

##### `K-05` — El escenario 3 de `§14` sitúa en `M5` la autorización que `D33` fijó en `M6` — **MEDIO**

`11-ARQ:7221` contra `6273` y `7422`. Bajo el orden anterior a `D33` era correcto; `D33` corrigió `§8.3` y la fila de `§14` conservó la asignación vieja. **Es la reaparición exacta de `M-3`** del gate de cierre, en la fila inmediatamente siguiente de la misma tabla.

##### `K-06` — `§8` sustituye cuatro reglas vigentes de `KERNEL.md` y ninguna presión lo registra — **MEDIO**

`G20`, `G21`, `G23`: cero apariciones en `11-ARQ`, (a), (b) y `E2`. `G22` una sola, como cita de apoyo. `a.11` es una lista donde **lo no nombrado sobrevive** —confirmado por `E2.4`, que tuvo que reclasificar `G29`—. Y `G22` dice de sí misma: «**NO es negociable por el sistema**». `§17` registra que las rutas A y B de `START_HERE` quedan sustituidas y **no tiene fila para `KERNEL.md`**. `PN-3` demuestra que presionar una regla de `KERNEL.md` exige una `PN`; aquí hay cuatro sin registro.

##### `K-07` — Tres sedes anclan la derogación a una versión que no existe, y el validador no mira esos ficheros — **MEDIO**

`KERNEL.md:4` dice 1.5.0; `a.11`, `O2`, `kernel/operativo/00-INDICE.md` y `PN-3` dicen 1.3.0. `comprobar_versiones.py` (`T152`) sólo recorre `README.md` y `START_HERE.md`, luego pasa en verde. Remedios distintos por sede: `00-INDICE` es F6; el título de `a.11` es material aprobado (F5); `O2` pide nota, no reescritura.

##### `K-08` — `§8.0` invoca la excepción de `a.7` donde su propia aritmética bastaba — **MENOR**
##### `K-09` — Enlace colgante: `entrada/02-CIRCUITO.md:54` cita `04-CONFIRMACION.md`, que no existe — **MENOR**
##### `K-10` — `§17` presenta como incremento condicional una cantidad que `D91` deriva — **MENOR**
##### `K-11` — El censo de sedes del principio de actualización omite `ADS-PENDIENTES §7` — **MENOR**

#### 5 · REEVALUACIÓN DE LOS HALLAZGOS PREVIOS

**Confirmados y bien resueltos:** `G4`/`G5` (doc 15) · `B-2` (doc 16, con `D74`+`D90`, verificada la tabla de `C7` fila a fila) · `M-1` (conté trece condicionales) · `G-4`/`D68` (conté doce áreas) · `M-9`/`D81` (conté catorce preguntas) · `E-3`/`F-01`/`F-02`/`PN-14` (verificada la cadena en las cuatro sedes) · `E-1` (colisión cerrada con `INS-0`…`INS-7`) · `M-3` (corregido en el escenario 1 — **y su clase reaparece en el 3: K-05**) · `M-4` (cerrado en sustancia por `D91`).

**Hallazgos previos que siguen presentes, y está bien:** `F-04`, `F-10`, `F-11` — registrados como `EXTERNO_CON_PROPIETARIO` con los cuatro atributos.

**Un hallazgo mío, RETIRADO tras verificarlo — y lo declaro porque casi lo escribo como bloqueante.** Sostuve que `m-1` era una falsa declaración de corrección. **Me equivoqué.** La nota existe, literal, en `11-ARQ:6120-6125`, y el remedio elegido es el correcto: `O15` es resolución del Owner y no se reescribe. Mi error fue inferir que «nota al pie de `O15`» significaba «nota dentro del fichero del registro». Lo dejo escrito porque **un gate que sólo publica los aciertos de su revisor no es una medida** — y porque este mismo mecanismo, aplicado a `K-01`, es lo que **no** defiende al bloque de estado del checkpoint: un bloque de estado existe para reescribirse.

**Ninguno de mis once hallazgos aparece en los documentos 15, 16, 17 ni 18.** Derivado por barrido: cero coincidencias.

#### 6 · PROPORCIONALIDAD

No es ornamental. Quince capacidades con doce campos, diez procesos, diecisiete handoffs y tres packs es proporcionado, y la disciplina de fuente única está aplicada con constancia real.

Tres observaciones de coste: (1) la repetición de los ~35 prompts es la mayor duplicación, declarada como excepción con motivo, pero es deuda que crecerá; (2) la asimetría de `DIS` (11 roles frente a 1–3) está en `A-30`, y **`SEG` merece atención**: única con veto duro, obligatoria e irretirable en `DEP`, y un solo rol; (3) **el patrón de censo divergente es sistémico**: `A6`, `A10`, `M-1`, `m-1`, `F-10`, `E-10`, y mis `K-01`, `K-03`, `K-04` son la séptima, octava y novena. **Cuando un defecto reaparece nueve veces no es descuido: es que las cifras se escriben a mano donde deberían derivarse.**

Lo desproporcionado no está en mi lote: `§2` ocupa ~2900 líneas y diez tandas para un runtime que no existe. No lo juzgo —es ámbito de J— pero afecta al equilibrio del entregable.

#### 7 · LÍMITES

1. No leí íntegro `ADS-PENDIENTES` (~1750 de 2163 líneas). **P9 y P10 no contrastadas contra su directiva de origen.**
2. No leí íntegros los documentos 15–18 (~6000 líneas). **No audito la corrección de esas cuatro pasadas.**
3. **No ejecuté ninguna prueba.** Ninguna fila adversarial, ningún `NP-*`, ningún escenario de `§14`, ningún validador.
4. No he visto PesquerApp. P8 juzga el texto de `O15`, no la adopción.
5. No juzgo `§2`, `§3` en su disposición física, ni los validadores: ámbito de J.
6. Abrí ocho ficheros fuera de mi lote sólo donde una afirmación de mi ámbito dependía de ellos.
7. No he visto el dictamen de J ni he intentado cubrir su mitad.
8. `K-06` depende de leer `a.11` como «lo no nombrado sobrevive», apoyado en `E2.4`. Si existiera regla contraria en material que no leí, `K-06` caería.

#### 8 · RECOMENDACIÓN DE VEREDICTO

##### INSUFICIENTE PARA F5

**Por dos motivos independientes, y cualquiera bastaría.**

**Primero, y decisivo por regla del encargo: mi cobertura del corpus central es incompleta.** No leí íntegro `ADS-PENDIENTES` ni los documentos 15–18, todos fuentes obligatorias. Ocultarlo sería el peor defecto posible en un gate. No lo oculto.

**Segundo: tres hallazgos GRAVES verificados, no registrados por ninguna de las nueve pasadas anteriores, dos de ellos arquitectónicos.** `K-02` rompe la premisa de que F6 construye sin decidir arquitectura, y su causa es una corrección anterior (`D75`) que desactivó sin verlo la cadena de la que la posterior dependía. `K-03` deja el único paso destructivo con un gate que omite la única comprobación que interroga lo que ese paso retira. `K-01` deja caducado el bloque cuya función es reanclar a un agente sin contexto.

**Lo que NO fundamenta este veredicto:** no declaro insuficiencia porque falte runtime, piloto, adaptadores certificados o PesquerApp. Todo eso son **limitaciones correctamente declaradas**, y el corpus es escrupuloso en no presentarlas como demostradas. Esa disciplina es de las mejores cosas de este entregable.

**Y lo que quiero que conste.** En mi ámbito la arquitectura es **buena**: las cuatro vías de `D74` resuelven de raíz un problema real; `C5` se autolimita con nitidez poco común; la separación ejecutor/autoridad anclada a `C7` es verificable; las doce y trece áreas son fieles a la directiva, incluida la decisión del Owner de dejar diseño y datos como condicionales; los siete externos tienen los cuatro atributos; y la distribución preestructurada cumple `§4.8`.

**Ninguno de mis once hallazgos exige inventar arquitectura para cerrarse.** Los tres graves tienen remedio acotado. Pero son graves, están sin resolver, y el criterio que se me dio es explícito en que eso impide el paso.

---

## 5 · Adjudicación literal del ADJUDICADOR L

> Transcrita **íntegra**. Incluye la adjudicación de las 43 filas de la matriz, de los
> veintidós hallazgos nuevos, de las decisiones, las cifras que L derivó por su cuenta,
> las discrepancias y su resolución, y el veredicto.


##### DICTAMEN DEL ADJUDICADOR L — GATE DEFINITIVO INDEPENDIENTE DE `F4c`

Árbol `0ea04514f1f6d7f99b1bade980b349771b7f3194`, rama `gate/f4c-definitivo-20260829`. `git status --porcelain` vacío antes y después. **No he modificado ningún fichero, no he hecho commit y no he corregido nada.** Ejecuté validadores y baterías; el árbol siguió limpio.

---

#### 1 · PROCEDENCIA Y MÉTODO

No escribí F4. No apliqué ninguna decisión `D1`–`D95` ni ninguna resolución `O1`–`O16`. No soy `J` ni `K` ni ninguno de los revisores anteriores. Recibí dos dictámenes cerrados y las cifras del coordinador **como contraste, no como fuente**.

**Integridad verificada por mí antes de leer nada.** Las 15 entradas de `manif_central.tsv`, las 83 de `manif_J.tsv` y las 193 de `manif_K.tsv` — líneas y SHA-256 — coinciden todas con el árbol. Ninguna cita de este dictamen procede de un fichero no verificado.

##### Lo que verifiqué yo mismo, contra el fichero y la línea

- **`11-ARQUITECTURA-INTEGRADA.md`**: §3.6 completa (3589–4270); §19 completa (8293–8437); §17 completa; §9 (6517–6690); §14 (7211–7239); §15.2 y §15.8 (cabeceras y filas `D`); §16 (cabeceras + `PN-3`, `PN-13`, `PN-14` íntegras); §18 (tabla completa, extraída y derivada); §8.0 (5564–5600, 5736–5800), §8.1, §8.2 (6115–6130), §8.3 (6265–6300), §8.4 (6361–6400); §6.7 (5395–5412); y de §2: 290, 546–620, 650–690, 725–745, 900–1000, 1110–1160, 1233, 1288–1300, 1390–1510, 1538–1560, 1602, 1677–1720, 1790–1830, 1896–1935, 2193–2260, 2385–2440, 2524–2625, 2740–2845, 2857–2880, 4130–4230.
- **`kernel/KERNEL.md`** §G20–G23 (640–760). **`kernel/VERSIONES.md`** íntegro. **`a-CAPACIDADES-APROBADA.md`** a.6, a.10, a.11, a.12. **`b-RECORRIDO-APROBADA.md`** L207–260, 353–362, 462–474, 830–840. **`START_HERE.md`** rutas A/B por barrido dirigido.
- **`ADS-PENDIENTES`**: cabecera y §1, §5.6, §5.18, §7, §8–§12 íntegras, y **todas** las cabeceras. **`ADS-NEXT-OWNER-BRIEF`** §6.2.
- **`CHECKPOINT-ADS-NEXT.md`**: L1–30, 70–115, 240–270, 735–760, 828–875, 1172–1330, 1398–1450.
- **`DECISIONES-Y-CONTRADICCIONES.md`**: `D87`–`D95`, `O15` íntegra, `O16` íntegra, y el **diff completo** contra `7e99388` y contra `3614e75`.
- **`18-GATE-DE-CIERRE`**: §5.1–§5.2 (matriz de las 43, extraída y recontada por mí), L435–470, L878–890, L1225, L2143.
- **Kernel derivado**: `recorrido/01-PROCESOS.md` parseado programáticamente (los diez procesos, obligatorias y condicionales); `esquemas/rol.yaml`; `validadores/comprobar_recuentos.py` (bloque `AFIRMACIONES`); `comprobar_versiones.py` L87; `contratos/C1`, `contratos/00-INDICE.md`, `pruebas/T086-T092`.
- **Ejecución real, sólo lectura**: `registrar_evidencia.py` → **10/13, exit 1**, en Python **3.10.12**; `comprobar_fuentes` → `T159` FALLIDA; `comprobar_arranque` → `T148` FALLIDA, `T171` SUPERADA; `comprobar_evidencia` → `T158` SUPERADA; `comprobar_recuentos` → `T151` SUPERADA; `comprobar_versiones` → `T152` SUPERADA; batería del gate de cierre → **30/30 desde la raíz y 30/30 desde `/tmp` por ruta absoluta**. `git status --porcelain` vacío después de todo.

##### Lo que acepté sin verificar por mí mismo — lo digo

- Los recuentos de `K` sobre su lote: 15 fichas × 12 campos, 17 instancias de handoff, 36 contratos de rol, 35 métodos, 35 prompts. **No los re-derivé.**
- La verificación fila a fila de `C7:80-92` que hicieron `J` y `K`. **No la repetí.**
- El desglose de `J` de la suite `test_workspace.py` (49 fallos + 5 errores). Confirmé el fallo y su causa (`tomllib`), no el desglose.
- El grafo completo del autómata de cinco fases de `J`. Verifiqué las reglas terminales y que los dos terminales retiran marcador; no re-derivé el grafo entero.
- **No abrí los documentos 15 y 17.** Del 16 sólo hice barridos dirigidos. Del 18 leí ~200 líneas más las tablas.

**Mi propia cobertura es incompleta, y lo declaro antes del veredicto para que no parezca excusa posterior.**

---

#### 2 · ADJUDICACIÓN DE LA MATRIZ — LAS 43 FILAS

**Localización.** La única tabla física de las 43 vive en `CHECKPOINT-ADS-NEXT.md` L1213–1299, bajo el bloque de la NOVENA tanda; §19 del documento 11 lleva la mitad externa (nueve filas, L8353–8361) y el documento 18 §5.2 lleva la adjudicación anterior de `I`. **La extraje y la reconté yo mismo**: 43 filas, 43 ids distintos (`uniq -d` vacío), un estado primario por fila.

**Método de adjudicación.** Verifiqué contra la fuente **las diez filas que el documento 18 declaró FALLIDAS** —son las que la décima tanda tenía que cerrar— y **re-derivé mecánicamente** todas las filas cuya condición es un recuento. Del resto acepto la verificación de `I` más la batería que yo mismo ejecuté en dos ubicaciones.

Leyenda: **F5**/**F6** = exige esa fase · **EXT** = externo · **BLOQ** = bloquea realmente.

| # | id | sev | estado primario | condición de cierre (fuente) | F5 | F6 | EXT | BLOQ | **mi adjudicación** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `A1` | BLOQ | CORREGIDO_EN_F4 | enum de `deriva.causa` de TRES valores con sede única — `11`:3806 (`§3.6`), `§2.6.11` L2331 se autodeclara glosa | no | no | no | **no** | **SUPERADA** — verificado en las tres sedes |
| 2 | `A2` | BLOQ | CORREGIDO_EN_F4 | `abierta(tx)` con UNA sede (`§2.6.1` L663–666) y NUEVE sedes que remiten | no | no | no | **no** | **SUPERADA** — derivé el censo: las nueve sedes son exactamente §2.5, §2.6.4, §2.6.5, §2.6.6, §2.6.8, §2.6.11, §2.9, §3.6, §7.4. Y `11`:4153–4156 ya dice «exactamente UN terminal, y es `derivada` **o** `abandonada`» |
| 3 | `A3` | GRAVE | CORREGIDO_EN_F4 | §7.4 paso 2 con las dos ramas; §16 alineado con `PN-7` | no | no | no | no | **SUPERADA** |
| 4 | `A4` | GRAVE | CORREGIDO_EN_F4 | el recuento de correcciones DERIVA de §15.8 | no | no | no | no | **SUPERADA** — derivé §15.8: **13 bloques** (`D23`…`D87`–`D95`). La cabecera L12 enumera doce y nombra la decimotercera. Cierra |
| 5 | `A5` | MEDIO | CORREGIDO_EN_F4 | sujeto corregido a FICHEROS canónicos, L1735–1741 | no | no | no | no | **SUPERADA** |
| 6 | `A6` | MEDIO | CORREGIDO_EN_F4 | 5 fases · 6 estados · 7 filas | no | no | no | no | **SUPERADA** — derivé: enum `fase` = 5; tabla de contrato condicional = 7 filas (`preparada` `confirmada` `conflicto` `abandonada` `derivada` `deriva` `fallo`); estados del campo = 6 con la ausencia |
| 7 | `A7` | MEDIO | CORREGIDO_EN_F4 | «los cinco CAMPOS» en las SEIS sedes, incluida la regla 1 de §2.6.10 | no | no | no | no | **SUPERADA** — `11`:2224–2226 ya dice «los CINCO CAMPOS DE PROCEDENCIA… no “los cinco conceptos de `a.9`”». La única aparición restante de «cinco conceptos» (L2198) es la descripción histórica del defecto `K` |
| 8 | `A8` | MEDIO | CORREGIDO_EN_F4 | marcador de `deriva` con las CINCO piezas de disciplina | no | no | no | no | **SUPERADA** — verifiqué las cinco: clasificación §2.4 (L472), `.gitignore` (L464), fila de reconstrucción §2.9 (L2868), `X59` (L1447), y la norma de lectura L1541 que ya **no** manda recorrer `estado/eventos/` |
| 9 | `A9` | MEDIO | CORREGIDO_EN_F4 | dos actos de autoridad cierran `4b`; `X58` reformulado | no | no | no | no | **SUPERADA** |
| 10 | `A10` | MEDIO | CORREGIDO_EN_F4 | «ONCE puntos de presión, derivados de §16» | no | no | no | no | **SUPERADA en su regla, con reserva de cifra.** Derivé §16: **14 cabeceras `## \`PN-`, `PN-4` RETIRADA, `PN-5` FUSIONADA → DOCE vigentes.** La condición publicada en la matriz **sigue diciendo ONCE**. La derivación funciona; el número escrito en la fila está caducado (ver `L-01`) |
| 11 | `A12` | MENOR | CORREGIDO_EN_F4 | el CAS de Git, no «un único escritor» | no | no | no | no | **SUPERADA** |
| 12 | `A13` | MEDIO | CORREGIDO_EN_F4 | fila `preparada` de §3.6 con los cinco CAMPOS | no | no | no | no | **SUPERADA** en su literalidad — **pero esa misma fila es la sede de `J-01`**: lleva los cinco campos y NO lleva `revision_base` |
| 13 | `B-1` | BLOQ | CORREGIDO_EN_F4 | `A2`–`A7` es `proceso:AUD`, propietario derivado | no | no | no | no | **SUPERADA** — verificado contra `01-PROCESOS.md` L413–440 |
| 14 | `B-2` | BLOQ | PRESION_LISTA_PARA_F5 | `PN-13` + `D90` cierra la mitad `PLT` contra `C7:80-92` | **sí** (`PN-13`) | **sí** | no | **sí, acotado a `INS-5` y `A9`** | **SUPERADA** — `PN-13` está completa: qué presiona, texto vigente, materia mínima con **dos salidas nombradas**, alcance, condición de reversión y origen. F5 puede redactar sin inventar. *(Reserva: su párrafo ALCANCE contiene un error de hecho — ver `L-03`)* |
| 15 | `G-1` | GRAVE | CORREGIDO_EN_F4 | `SEG` y `CON` obligatorias de `proceso:DEP` en `U5b` | no | no | no | no | **SUPERADA** — derivé `DEP`: obligatorias `SEG`, `CON`, `VER`. **Y es la corrección que causa `K-02`** |
| 16 | `G-2` | GRAVE | CORREGIDO_EN_F4 | `ARQ` por el `plan-tecnico` de su item `DEU` | no | no | no | no | **SUPERADA** |
| 17 | `G-3` | GRAVE | CORREGIDO_EN_F4 | el gate de `INS-5` **en §18**, sede canónica | no | no | no | no | **SUPERADA** — `11`:8223 columna gate: «especialización aprobada **Y baseline de `INS-5` aprobado por el Owner**» |
| 18 | `G-4` | GRAVE | CORREGIDO_EN_F4 | doce identificadores derivados del patrón `ads:memoria` | no | no | no | no | **SUPERADA** — conté las doce áreas de `ADS-PENDIENTES` §5.18 L775–786: son doce, numeradas |
| 19 | `M-1` | MEDIO | CORREGIDO_EN_F4 | TRECE condicionales, en las tres sedes | no | no | no | no | **SUPERADA** — las conté una a una en L788–790: **trece** |
| 20 | `M-2` | MEDIO | CORREGIDO_EN_F4 | fila del mapa documental, autoridad «nadie: se regenera» | no | no | no | no | **SUPERADA** |
| 21 | `M-3` | MEDIO | CORREGIDO_EN_F4 | `U6` revalida el nivel vigente, no es `O12` | no | no | no | no | **SUPERADA** — `11`:8233. **Y su clase reaparece en el escenario 3 de §14: `K-05`** |
| 22 | `M-4` | MEDIO | CORREGIDO_EN_F4 | resumen corregido: `AUD` y `DEP` | no | no | no | no | **SUPERADA** |
| 23 | `M-5` | MEDIO | CONTRATO_COMPLETO_PARA_F6 | actor de las DOS mitades + extensión de ficha en §5.2 **y §17** | no | **sí** | no | no | **SUPERADA** — §5.2 L4713 «Son **SEIS**, no cuatro»; §17 L8138 «**`+6`**»; §16 L8125 las seis. Las tres sedes coinciden |
| 24 | `M-6` | MEDIO | CONTRATO_COMPLETO_PARA_F6 | `capacidades/ENC/` en §5.2 **y en §17** | no | **sí** | no | no | **SUPERADA** — ídem |
| 25 | `M-7` | MEDIO | CORREGIDO_EN_F4 | items por macrocircuito y FRENO 3 | no | no | no | no | **SUPERADA** — derivé de §18: N 2, A 4, M 2, U 4. *(Reserva menor: `K-08`)* |
| 26 | `M-8` (≡`A11`) | MEDIO | CORREGIDO_EN_F4 | `RC-1`–`RC-9` renombradas y fuera del inventario de §19 | no | no | no | no | **SUPERADA** |
| 27 | `M-9` | MEDIO | CORREGIDO_EN_F4 | el §6.2 de la directiva es el contrato de `A3` | no | no | no | no | **SUPERADA** — conté las preguntas del `OWNER-BRIEF` L435–450: **catorce** |
| 28 | `m-1` | MENOR | CORREGIDO_EN_F4 | reanclar la cifra SIN tocar la resolución | no | no | no | no | **SUPERADA** — la nota al pie existe literal en `11`:6121–6125 y dice DOCE. **`K` sostuvo lo contrario, se retractó, y la retractación es correcta** |
| 29 | `m-2` | MENOR | CORREGIDO_EN_F4 | la nota de procedencia precede a `O16` | no | no | no | no | **SUPERADA** — `DECISIONES`:355–360 |
| 30 | `m-3` | MENOR | HISTORICO_NO_APLICABLE | hecho confirmado, juicio NO asumido | no | no | no | no | **NO APLICABLE, con causa demostrada** — correctamente registrado como preferencia de diseño sin remedio exigible |
| 31 | `m-4` | MENOR | CORREGIDO_EN_F4 | `U5a` y `U5b` rotuladas en §18 | no | no | no | no | **SUPERADA** — `11`:8231–8232 |
| 32 | `F-01` | MEDIO | PRESION_LISTA_PARA_F5 | la cadena está también en `b.16` L895 y `a.6` L495, material APROBADO → `PN-14` | **sí** (`PN-14`) | **sí**, después | **ya no** | no | **SUPERADA** — verifiqué las dos sedes aprobadas. `PN-14` está completa y no obliga a inventar |
| 33 | `F-02` | MEDIO | EXTERNO_CON_PROPIETARIO | el vocabulario escrito en §19 (cinco puntos) | no | **sí** (`SIS`) | **sí** | no | **SUPERADA** — §19 L8354 fija los cinco puntos. **Reserva mía**: `proceso:AUD` sigue escribiendo `DOM`, `SEG`, `DIS/Reconstruccion` **sin sufijo tipado**, y ésa es la notación que `F-02` existe para tipar |
| 34 | `F-03` | MEDIO | CORREGIDO_EN_F4 | `INS-0`…`INS-7` | no | no | no | no | **SUPERADA** |
| 35 | `F-04` | MEDIO | EXTERNO_CON_PROPIETARIO | `grado_inicial: alta` + `T75` | no | **sí** (`ENC`+`SIS`) | **sí** | no | **SUPERADA como externo** — fichero, propietario, fase y condición presentes |
| 36 | `F-05` | MENOR | CORREGIDO_EN_F4 | §15.7 registra la excepción de `C5`; §8.0 declara qué viaja | no | (residual) | **no** | no | **SUPERADA** — y §19 explica por qué la novena fila no es externa |
| 37 | `F-06` | MENOR | EXTERNO_CON_PROPIETARIO | anclar el `cuando` de `dis-a-ver` | no | **sí** (`DIS`) | **sí** | no | **SUPERADA como externo** |
| 38 | `F-07` | MENOR | EXTERNO_CON_PROPIETARIO | campo `autoridad:` en `docs/owner/` | no | **sí** (`SIS`+Owner) | **sí** | no | **SUPERADA como externo** |
| 39 | `F-08` | MENOR | EXTERNO_CON_PROPIETARIO | nota de vigencia en `IDEAS §15` | **sí, sin PN** | no | **sí** (el Owner) | no | **SUPERADA como externo** |
| 40 | `F-09` | MENOR | CORREGIDO_EN_F4 | «provisional» conservado y procedencia citada | no | no | no | no | **SUPERADA.** Comprobé lo que `K-11` alega: `ADS-PENDIENTES` §7 L914–916 llama al principio «**Principio aceptado**» y el censo de §8.4 lo omite. **Pero ese documento se autodeclara en su L3–L6 «documento vivo de trabajo con el Owner… No es todavía especificación normativa».** La clasificación de §8.4 como PROVISIONAL es correcta; la omisión es de censo, no de estatus |
| 41 | `F-10` | MENOR | EXTERNO_CON_PROPIETARIO | la cabecera de `03-FORMAS` deja de afirmar «uno por clase» | no | **sí** (`ENC`) | **sí** | no | **SUPERADA como externo** |
| 42 | `F-11` | MENOR | EXTERNO_CON_PROPIETARIO | la cabecera de `05-ESCENARIOS` enumera lo que contiene | no | **sí** (`SIS`) | **sí** | no | **SUPERADA como externo** |
| 43 | `F-12` | MENOR | CORREGIDO_EN_F4 | 15, 16 y 17 inmutables; se reanclan sus proyecciones | no | no | no | no | **SUPERADA** |

**Recuento de mi adjudicación: 42 SUPERADAS · 0 FALLIDAS · 1 NO APLICABLE = 43.**

**Las diez filas que el documento 18 declaró FALLIDAS —`A2`, `A4`, `A7`, `A8`, `B-2`, `G-3`, `M-5`, `M-6`, `F-01`, `F-02`— están cerradas, y lo verifiqué una a una contra su sede.** Esa es la afirmación más fuerte que puedo hacer a favor de esta candidata, y la hago sin reservas.

**Y es exactamente lo que no cierra `F4c`.** Lo dice la propia matriz en su última línea (`CHECKPOINT` L1321): «que las 43 filas estén cerradas NO cierra `F4c`». Los defectos que impiden el paso **no están entre los 43**: son nuevos, y están en el apartado siguiente.

---

#### 3 · ADJUDICACIÓN DE LOS HALLAZGOS NUEVOS

##### Los once de `J`

**`J-01` · CONFIRMADO · severidad adjudicada por mí: BLOQUEANTE** *(J proponía GRAVE — lo subo)*

`revision_base` aparece **once veces** en el documento 11 —L604, 608, 1655, 1798, 1808, 1817, 1867, 2391, 2555, 5482, 5520— y **ninguna dentro de §3.6 (3589–4270)**. Lo verifiqué con `grep -n` sobre el fichero entero y leyendo la fila `preparada` completa:

> `11`:4024 — campos OBLIGATORIOS de `preparada`: «`afecta[]` con `ruta`·`hash_previo`·`hash_posterior_esperado`·`orden`· una de `contenido`|`parche`|`operacion` · los CINCO CAMPOS de procedencia … · `base`». **No hay `revision_base`.**
> `11`:604 — «5 REVISIÓN BASE DECLARADA · `revision_base` **en `preparada`**: el `HEAD` del punto 2»
> `11`:611 — «7 CAPACIDAD DE RESTAURARLOS DESDE ESA REVISIÓN … **Sin esto, `abandonada` sería inalcanzable**»
> `11`:2391 — «`abandonada` es INALCANZABLE hasta haber RESTAURADO todas sus rutas a `revision_base` y haberlo **verificado byte a byte**»

Comprobé además que `base` **no** es el mismo campo: §3.6 lo define como «hash de las entradas sobre las que se decidió», y el documento entero contiene **una sola** aparición entrecomillada de `` `base` `` — la de la fila `preparada`. Ninguna sede los equipara.

**Por qué BLOQUEANTE y no GRAVE.** El propio corpus fijó el listón. El documento 18, L448, cierra `A1` con estas palabras: *«El defecto BLOQUEANTE de `A1` —que el esquema derivado literalmente de §3.6 rechazaba el `deriva` que hace emitible `abandonada`— está cerrado.»* `J-01` es **el mismo defecto, sobre el mismo terminal, en la misma sección, invertido**: un esquema derivado literalmente de §3.6 **acepta** un `preparada` sin el campo del que dependen la restauración exacta, la alcanzabilidad de `abandonada` y la garantía de que «`main` nunca contiene estado parcial». Graduarlo por debajo de `A1` sería aplicar dos varas.

**Bloquea F5**: `PN-1` propone aprobar §2 como sección (g). Aprobarla consagraría un contrato de evento que no puede representar ese dato, y F6 tendría que **decidir su forma** — lo que el criterio de suficiencia excluye. La corrección son cinco líneas y no hay nada que decidir.

**`J-02` · CONFIRMADO · GRAVE**

Verificado en las cuatro sedes:
- `11`:2741–2742 — `tx = TX-H(cuerpo de \`preparada\` MENOS \`id\`, \`tx\` y \`predecesor\`)`.
- `11`:2830–2832 — «ANTES DE REEMITIR, el ejecutor busca un evento con el MISMO `tx` y la MISMA `fase`. Si existe, **la operación es una NO-OPERACIÓN**.»
- `11`:4136 — capa B: «que no haya **dos transacciones distintas compartiéndolo**».
- `11`:4140 — capa B: «NINGUNA FASE POSTERIOR A UN TERMINAL en ese `tx`».

Una reparación con intención declarada idéntica —mismos `afecta[]`, hashes, `orden` y procedencia, que es el caso natural tras un abandono, porque C·RESTAURAR devuelve todas las rutas a `revision_base`— **computa el mismo `tx`**. Entonces la regla de reintento la vuelve no-operación, la capa B la rechaza por posterior a terminal, y `bloqueado_por_deriva(item)` no se cierra por su camino natural. Es la clase de `B1` desplazada al contrato de identidad. **Causalmente unido a `J-01`**: el único campo que distingue las dos intenciones es `revision_base`, y declararlo y decir si entra en el cómputo de `tx` cierra los dos a la vez.

**`J-03` · CONFIRMADO · MEDIO**

`11`:5400–5405 reasigna la comprobación adversarial de §6.7 a `X51`. `11`:1440 dice qué es `X51`: «editar un canónico fuera del protocolo, sin transacción abierta, y arrancar → se declara deriva no transaccional». Nada que ver con las tres comprobaciones de §6.7 (que la adopción hasta `A7` no escriba en las fuentes; propagación a tres fuentes con `main` protegida; fusionar dos de tres). `M2` señaló referencias inexistentes (`X32`–`X34`) y **el remedio las reasignó a una fila existente pero ajena**. No bloquea F5.

**`J-04` · CONFIRMADO · MEDIO**

Dos formulaciones incompatibles del `hash_previo` de la transacción de reparación:
> `11`:1906 (§2.6.9) — «`hash_previo` = **lo que hay en la base restaurada**»
> `11`:2609 (§2.6.11) — «`hash_previo` = **el `hash_observado` que la deriva registró**»

Coinciden sólo para `causa: abandono-de-transaccion`. Para `sin-transaccion` y `posterior-al-cierre` no hay base restaurada, y divergen. La formulación general correcta es la de §2.6.11. Cae dentro de §2, que es lo que `PN-1` propone aprobar como (g).

**`J-05` · CONFIRMADO · MEDIO**

`comprobar_recuentos.py` L107–156: `AFIRMACIONES` es un **censo escrito a mano** de dónde vive cada cifra. Cubre `C1-EQUIPO-ROL-AGENTE-METODO.md` y **no** cubre `contratos/00-INDICE.md`:7 ni `pruebas/T086-T092-contratos.md`:14, que siguen diciendo «veintiocho campos». Derivé `esquemas/rol.yaml`: **29 obligatorios**. `C1`:37 ya dice «veintinueve». Ejecuté `T151` → **SUPERADA**, con dos sedes vigentes afirmando una cifra que el corpus desmiente. Es lo que el propio corpus condena en `comprobar_fuentes.py`: «nunca una lista escrita a mano, que es lo que envejece».

**`J-06` · CONFIRMADO · MENOR** *(mismo defecto que `K-07`)*

`kernel/operativo/00-INDICE.md`:132,134 declara `KERNEL.md` «versión 1.3.0»; `KERNEL.md`:4 dice **1.5.0**, y `VERSIONES.md` fija esa línea histórica en 1.5.0 con su motivo. `comprobar_versiones.py` L87 sólo recorre `README.md` y `START_HERE.md`; ejecuté `T152` → **SUPERADA**.

**`J-07` · CONFIRMADO · MEDIO**

Conté yo mismo las filas de la tabla adversarial de §2.6.7 (L1395–1506): **45 filas físicas, 45 ids distintos** — `X01`–`X23`, `X25`–`X28`, `X37`–`X39`, `X47`–`X61`. La batería que ejecuté lo confirma (`G-26`: «45 filas / 45 ids»). Frente a eso:
- `11`:1475 dice **45** — correcto.
- `11`:1491 dice «el conteo da **42** filas de datos con 42 ids distintos».
- `11`:3173 dice «como las **cuarenta y dos** de §2.6.7» — **dieciséis líneas después de que L3157 escribiera «cuarenta y cinco»**.
- `11`:8298 (**§19**, el sitio donde un gate lee qué está probado) dice «las **CUARENTA Y DOS** filas de la tabla adversarial de §2.6.7».

`G-26` no lo detecta porque compara `filas == ids`, no `prosa == derivado`.

**`J-08` · CONFIRMADO · MENOR**

`b`:358 — «deja al item en `en espera` **(P7)**». Pero `b`:217–218 fija `P7 → activo` y `b`:221–222 fija `P9 → en espera`; `b`:255 lo usa correctamente. La cita es errónea.
`b`:462–472 — la numeración va **1, 2, 5, 3, 4**.
Su sede es material APROBADO, luego su remedio es **F5**, y hoy no está registrado en ninguna `PN` ni en §19.

**`J-09` · RECHAZADO**

`J` afirma que no se nombra la salida «aceptar lo divergente» para cerrar un `deriva`, y **no aporta cita**. Contra la fuente: las dos sedes que gobiernan la reparación —`11`:1907 y `11`:2611— dicen ambas «`hash_posterior_esperado` = **lo que la autoridad decida**». Aceptar lo divergente es un valor que la autoridad puede elegir, y el mecanismo está declarado sin ambigüedad. No nombrarlo es preferencia editorial, no laguna. **Lo rechazo.**

**`J-10` · CONFIRMADO · MEDIO** *(J proponía MENOR — lo subo, y lo amplío)*

Verificado y **peor de lo que `J` describe**:
- `CHECKPOINT`:75 — `actualizado: 2026-08-28`, mientras `last_meaningful_event` (L100–105) registra hechos de **2026-08-29**.
- `CHECKPOINT`:76–77 — `metodo:` dice «GATE FINAL EJECUTADO · NIVEL 0 CERRADO», sin mencionar el GATE DE CIERRE, que sí figura en `based_on`.
- `CHECKPOINT`:8–10 — «Estado de la fase, en una línea» nombra sólo el GATE FINAL.

`a.10` regla 3 (`a`:986): «Un checkpoint desactualizado —siguió trabajando y no lo escribió— es **un defecto del sistema**, no una omisión menor.»

**`J-11` · CONFIRMADO · MEDIO**

Reproducido por mí en Python **3.10.12**: `registrar_evidencia.py` → **10/13, exit 1**; `T159` y `T148` FALLIDAS; la suite de workspace falla. Causa única: `tomllib` no existe antes de 3.11. Los tres validadores que fallan **dejan intacta la evidencia anterior**, y por eso `comprobar_evidencia.py` (`T158`) sale **SUPERADA** en un entorno donde nada se reprodujo. No hay guardia de versión de intérprete.

**Matiz que corrijo a `J`**: el checkpoint L104 **sí declara** «Validación con Python 3.11.16», y `A14` registra `python_requires ≥ 3.11` con propietario `PLT` y fase F6. La limitación está declarada con honestidad. Lo que falta es la guardia, que es F6 y es la huella de entorno que `P-08` diseña. **No es «una batería que sólo pasa en el entorno del autor»**: la batería propia del gate da **30/30 desde la raíz y desde `/tmp`**, y lo verifiqué.

##### Los once de `K`

**`K-01` · CONFIRMADO · GRAVE** *(y agravado por mí)*

`K` cita `CHECKPOINT`:867. Encontré **tres sedes vivas más**:
- L867 — «`F5 ENMIENDAS` **DIEZ** presiones normativas vigentes».
- **L747** — `pregunta_pendiente: ninguna. Las **DIEZ** presiones normativas vigentes son materia de F5` — **campo de metadatos vivo**, contiguo a `owner_captado` y a `siguiente:`, ambos actualizados en el último commit.
- **L1186–1188** — el bloque `RESULTADO` que **introduce la matriz** declara `31 · **1** · 2 · **8** · 1 = 43`; la tabla que empieza 27 líneas después da `31 · **2** · 2 · **7** · 1`. Lo derivé yo.
- **L1190** — `PRESIONES: **ONCE** vigentes: PN-1, PN-2, PN-3, PN-6 a PN-13`.
- La fila `F4c` (L842–866) enumera las pasadas **hasta `D63`** y no menciona la tercera revisión, ni el gate final, ni el complemento, ni el gate de cierre, ni `D64`–`D95`.

Derivé la cifra correcta: **catorce cabeceras `## \`PN-`, menos `PN-4` RETIRADA y `PN-5` FUSIONADA → DOCE**, que es lo que dicen §19 L8310, `CHECKPOINT`:1430 y `CHECKPOINT`:1606. **Quien reancla desde el checkpoint recibe un censo que omite `PN-13` y `PN-14`** — la que bloquea componer `INS-5` y `A9`, y la que corrige material aprobado.

**`K-02` · CONFIRMADO · GRAVE** *(y agravado por mí)*

Parseé `01-PROCESOS.md` programáticamente. La derivación:

| proceso | `SEG` participa | notación |
|---|---|---|
| FEA, GAP, INC, DEU | condicional | `SEG:condiciones` — **cuatro instancias, exactamente las que `D92` cuenta** |
| **DEP** | **obligatoria** `condiciones-de-seguridad` (L370–373), `capacidad_productora: "SEG"` | **`SEG:condiciones` NO aparece.** Sus condicionales son `DOM:condiciones`, `ARQ`, `ENT` |
| **AUD** | condicional | **`SEG` a secas, sin sufijo tipado** (L432) |

`D92` prescribe (`11`:8418): «El conjunto se DERIVA con **un barrido de `:condiciones`** sobre el fichero, no se escribe a mano: hoy son las cuatro instancias de `SEG:condiciones` y las cuatro de `DOM:condiciones`». **Ese barrido no alcanza a `DEP` ni a `AUD`.** Y `11`:6390 dice «`U5b` es **`proceso:DEP`**», mientras `D92` nombra a `U5b` entre «**los tres tramos que escriben en las fuentes del producto**». La regla no llega al tramo que ella misma señala como el más expuesto, y la prueba que prescribe reproduce el punto ciego. Verifiqué también que hay **cero** instancias de `:revision` en todo `kernel/operativo/`.

La norma aprobada está escrita sobre el hecho, no sobre la notación: `a`:502–503 — «**DOM y SEG aportan condiciones antes de construir y revisan después**»; `b`:834–836 lo repite.

**Y su causa es una corrección anterior**: `D75` cerró `G-1` moviendo `SEG` a obligatorias en `DEP` —fila 15 de esta misma matriz, que adjudico SUPERADA— eliminando la cadena de la que `D92` dependería después.

**`K-03` · CONFIRMADO · GRAVE, con su base corregida**

Las cuatro sedes, verificadas:
> `11`:6186 (§8.2, RETIRADA SEGURA) — «pruebas, CI, despliegue y **comportamiento agentic** tras cada retirada»
> `11`:6271 (EVIDENCIA) — «salidas de build, pruebas, CI y despliegue en `M7`» — **cuatro**
> `11`:6274 (**GATES**) — «`M7` no cierra sin **las cuatro salidas verdes**»
> `11`:6298 (`M7 VERIFICAR`) — «build, pruebas, CI, despliegue y **comportamiento agentic, los cinco**»

`M6` es el **único paso destructivo** y retira de cada fuente kernel, packs y organización de ADS. Build, pruebas, CI y despliegue pasarían igual en una fuente a la que le han quitado su organización ADS: **la única de las cinco que interroga lo que `M6` retira es precisamente la que el gate omite.**

**Corrijo la base que `K` le dio.** `K` la ancla en «la directiva del Owner, `ADS-PENDIENTES` §5.6». Comprobé la cabecera de ese documento (L3–L6): *«documento vivo de trabajo con el Owner… **No es todavía especificación normativa**»*. La cita existe (L513) pero no es norma. **El hallazgo sobrevive entero como contradicción INTERNA del documento 11**: cuatro y cinco, en la misma sección, sobre el gate vinculante del único paso destructivo. Severidad GRAVE mantenida; **no** activa la regla de «contradicción contra fuente normativa».

**`K-04` · CONFIRMADO · MEDIO**

Las tres líneas, verificadas y contadas por mí:
> `11`:8332 — «**SIETE** de los cuarenta y tres hallazgos … tienen su sede FUERA de F4»
> `11`:8338 — «**Eran OCHO, y ahora son SIETE.** `F-01` deja de ser externo»
> `11`:8344 — «**La tabla tiene NUEVE filas y los externos son OCHO**, y no es un descuadre»

Conté la tabla: **nueve filas** (`F-01`, `F-02`, `F-04`, `F-05`, `F-06`, `F-07`, `F-08`, `F-10`, `F-11`). Y derivé de la matriz: **siete** `EXTERNO_CON_PROPIETARIO`. La reconciliación de L8344 sólo cierra contando `F-01` entre los externos, **seis líneas después de declarar que dejó de serlo**. El descuadre correcto es 9 = 7 externos + `F-01` (ya no externo) + `F-05` (nunca externo).

**`K-05` · CONFIRMADO · MEDIO**

`11`:7221, §14 escenario 3 «migración desde ADS anterior», columna gate: «M3 equivalencia, **M5 autorización**». Contra:
> `11`:6273 — «**`M6` exige autorización EXPLÍCITA del Owner**»
> `11`:7422 — `D33`: «secuencia de migración **M5 certifica · M6 retira · M7 verifica**»

Bajo el orden anterior a `D33` era correcto; `D33` corrigió §8.3 y la fila de §14 conservó la asignación vieja. Es la reaparición exacta de `M-3` del gate de cierre —fila 21 de esta matriz, que adjudico SUPERADA por haberse corregido en el escenario 1— en el escenario 3 de la misma tabla.

**`K-06` · CONFIRMADO · GRAVE** *(K proponía MEDIO — lo subo, y es de los decisivos)*

Derivé el censo: `G20`, `G21` y `G23` tienen **cero** apariciones en el documento 11, en (a), en (b) y en `E2`; `G22` tiene **una**, como cita de apoyo. `a.11` (`a`:1016–1025) lista `G11`, `G12`, `K0.9`, `G14`, `G13`, `G34`, `G52`, `G17`, `G08`, `G32`, `G26`, `G24`, `G53` — **`G20`–`G23` no aparecen en ninguna de sus cinco filas**. `PN-3` (`11`:7704) declara que «a.11 es **la única lista** que deroga o ajusta reglas de 1.3.0». Y `E2.4` demuestra la regla de lectura: `G29` «figuraba entre las reglas que **SOBREVIVEN** intactas» y hubo que **enmendar** (a) para reclasificarla. **Lo no nombrado sobrevive.**

Ahora el conflicto, que verifiqué línea a línea:
- `KERNEL.md`:688 (`G21`) — «**El gate de salida del Circuito 0 lo fija este documento y NO es negociable por el sistema** (G22), porque un sistema no puede definir sin conflicto de interés los criterios que aprueban su propia existencia.»
- `KERNEL.md`:694–712 (`G22`) — timebox de **3 sesiones del Owner o 2 semanas**, parada obligatoria con `Owner Decision`, **diez entregables obligatorios** nombrados uno a uno, y cuatro prohibiciones.
- `START_HERE.md`:141–147 — ruta A «Lanzar el Circuito 0… termina cuando existen **los 10 entregables de G22, dentro del timebox**».
- `11`:8146 (**§17**) — «`START_HERE.md` **rutas A y B** → **sustituidas** por §8.1 y §8.2».
- `11`:5833–5850 (§8.1) — `INS-0`…`INS-7`, con `INS-3` = «C0: especializar y verificar la organización YA MATERIALIZADA» y gates `INS-4` / `INS-7`.
- `grep` sobre el documento 11: **cero** apariciones de «timebox», «presupuesto máximo», «Owner Decision» o «entregables obligatorios».
- **§17 no tiene fila para `kernel/KERNEL.md`.**

Es decir: F4 sustituye la ruta cuyo gate de salida la constitución declara **no negociable por el sistema**, por un gate distinto **definido por el propio sistema**, redefine el contenido de C0, retira el timebox, los diez entregables y las cuatro prohibiciones — y **no lo registra ni como derogación en `a.11` ni como presión en §16**. `PN-3` demuestra que presionar **una** regla de `KERNEL.md` exige una `PN`; aquí hay cuatro sin registro.

Sondeé además la región de `ADS-PENDIENTES` que ninguno de los dos revisores abrió, y la refuerza: §12 L1005 exige ejecutar el gate de certificación «**al cerrar Circuito 0**», y `11`:6664 lo recoge. **El corpus sigue operando con «Circuito 0» como concepto vivo mientras su gate constitucional queda desplazado en silencio.**

**`K-07` · CONFIRMADO · MEDIO**

`KERNEL.md`:4 = **1.5.0**. Frente a ello: `a.11` título «Efecto sobre el kernel **1.3.0**»; `O2` «Convivencia de `KERNEL.md` **1.3.0**»; `kernel/operativo/00-INDICE.md`:132,134; `PN-3` `11`:7700 «QUÉ PRESIONA `KERNEL.md` **1.3.0** `G03`». `VERSIONES.md` regla 1 exige que cada punto de entrada cite la versión de la cosa de la que habla, y regla 5 prohíbe declarar versiones fuera de su tabla. `T152` pasa en verde porque sólo recorre dos ficheros. Remedios distintos por sede, como `K` dice: `00-INDICE` es F6; el título de `a.11` es material aprobado (F5); `O2` pide nota, no reescritura.

**`K-08` · CONFIRMADO · MENOR**

Derivé de §18 el proceso de cada tramo: `M` = `M0`–`M5` **SIS** + `M6`–`M7` **DEU**; `U` = `U0`–`U4` **SIS** + `U5a` **SIS** + `U5b` **DEP** + `U6` **SIS**. El FRENO 3 de `a.7` exige **más de dos** items `SIS` consecutivos: `M` tiene uno y `U` tiene dos antes de que `DEP` rompa la racha. **La aritmética propia de §8.0 bastaba**, e invocar además la cláusula literal de excepción de `a.7` (`11`:5765–5767) es redundante. No es contradicción; es una dependencia innecesaria.

**`K-09` · CONFIRMADO · MENOR**

`kernel/operativo/entrada/02-CIRCUITO.md`:54 cita `04-CONFIRMACION.md`. El directorio contiene `04-INCERTIDUMBRE-Y-CONFIRMACION.md`. Enlace colgante, verificado con `ls`.

**`K-10` · CONFIRMADO · MENOR**

`11`:8138 presenta «`+1` más **si** `I-14` obliga a extender las fichas de las capacidades líderes de cobertura». Pero `D91` (`DECISIONES`:292) ya lo decidió y fija que **el conjunto se DERIVA de los `contrato-de-aspecto`, no se escribe a mano** — luego no es un incremento condicional de uno, sino un conjunto derivado ya resuelto. Defecto de presentación.

**`K-11` · CONFIRMADO · MENOR** *(mantengo la severidad de `K`; **retiro** el agravamiento que yo mismo consideré)*

El censo del principio «DETECTAR AUTOMÁTICAMENTE, ACTUALIZAR CONSCIENTEMENTE» (`11`:6366–6377) cita `ADS-IDEAS-PENDIENTES-MULTIREPO.md` §3 L79 y §15 L589, y **omite `ADS-PENDIENTES` §7 L914–916**, donde el mismo principio aparece bajo el rótulo «**Principio aceptado**». Lo verifiqué.

**Pero comprobé el estatus de ese documento antes de darle peso**, y eso cambia la consecuencia: `ADS-PENDIENTES` L3–L6 se autodeclara «documento vivo de trabajo con el Owner… **No es todavía especificación normativa ni autoriza a implementar automáticamente sus propuestas**». Luego la clasificación de §8.4 —principio PROVISIONAL, sin norma aprobada que gobierne `U`, y por eso sin presión registrada— **es correcta**, y `F-09` sigue SUPERADA. La omisión es de completitud del censo. **MENOR.**

##### Los tres que aporto yo

**`L-01` · El bloque que INTRODUCE la matriz viva declara la distribución anterior · MEDIO**

`CHECKPOINT`:1186–1191, veintisiete líneas por encima de la tabla que introduce, declara `RESULTADO **31 · 1 · 2 · 8 · 1** = 43`, `DECISIONES **D71–D86**` y `PRESIONES **ONCE** vigentes`. La tabla que le sigue da, derivado por mí, `31 · 2 · 2 · 7 · 1` y cita `PN-14`. Y la fila `A10` de esa misma tabla conserva como condición de cierre «**ONCE** puntos de presión, derivados de §16». Un bloque histórico contiene una tabla viva, sin marca que distinga una cosa de otra. Es la misma clase de `K-01` y suma a la misma conclusión.

**`L-02` · `O16` se presenta como resolución del Owner sin ninguna procedencia registrada · GRAVE**

`DECISIONES`:360 la rotula «`O16` · **resolución POSTERIOR del Owner** — la sede del gobierno Git del control repo», y §16 `PN-11` (`11`:7908) la invoca como «SEDE, YA RESUELTA — `O16`, resolución posterior del Owner».

Busqué su procedencia en todo el corpus:
- `O7`–`O14` la tienen: `DECISIONES`:355–357, «las ocho llegan de la revisión independiente de F3 y de la respuesta del Owner a ella, **el 2026-08-27**».
- `O15` la tiene: cita **verbatim** con fecha en `CHECKPOINT`:743–746, campo `owner_captado`.
- **`O16` no tiene ninguna.** Ni fecha, ni cita, ni entrada en `owner_captado`. El único rastro es la línea de bitácora `CHECKPOINT`:259 («PN-11 GANA SEDE por O16») y el cuerpo del commit `a713590`, que tampoco registra intervención del Owner.

No afirmo que la decisión esté inventada: **afirmo que el corpus no puede demostrar que el Owner la tomara**, mientras demuestra exactamente eso para las quince restantes, con su propia disciplina y en el mismo fichero. `O16` es lo que da sede a `PN-11`, que nació del BLOQUEANTE `B2` de la tercera revisión. Es precisamente la pregunta 18 de `J` («decisiones sin atribuir»), y ni `J` ni `K` lo vieron.

**`L-03` · El ALCANCE de `PN-13` afirma de `proceso:DEP` algo que el kernel desmiente · MENOR**

`11`:7989–7991: «…ni a `A8`, `M6`–`M7` ni `U5b`, que son `proceso:DEU` y `proceso:DEP` y **también las declaran —`DOM:condiciones` y `SEG:condiciones`**, con `G28` haciendo irretirable a `SEG` en `DEP`—». Derivado del kernel: `DEP` declara `DOM:condiciones` como condicional, **pero `SEG` como obligatoria, no como `SEG:condiciones`**. La conclusión de `PN-13` (que su alcance no llega a `U5b`) es correcta; el motivo escrito, no. Es la **misma conflación de vías que rompe `D92`**, dentro de una presión que va al Owner.

---

#### 4 · ADJUDICACIÓN DE LAS DECISIONES

**Integridad verificada mecánicamente.** Diff de `DECISIONES-Y-CONTRADICCIONES.md` contra `3614e75` (el árbol previo a la décima tanda), restringido a filas `D` y `O`: **la única fila preexistente modificada es `D67`, y `D87`–`D95` son adiciones. Ninguna otra `D` ni ninguna `O` se reescribió.** Diff de la fila `D67` contra `7e99388`: **idéntica byte a byte**. `O1`–`O16` intactas.

| decisión | qué decide | ¿revisora sin reescribir? | ¿sede verificada? | ¿F5 o F6 tendría que decidir algo? | adjudicación |
|---|---|---|---|---|---|
| `D87` | retira `estado/cuarentena/` y la lleva a `.ads/run/quarantine/` | sí, revisa `D79` | §2.6.9 L1794–1800; §2.9 L2870 declara que **no se reconstruye**, con su límite | no | **CORRECTA.** Retira, no parchea |
| `D88` | las cinco piezas de disciplina del marcador de `deriva` | sí, completa `D78` | verifiqué las cinco: §2.4 L472, `.gitignore` L464, §2.9 L2868, `X59` L1447, norma de lectura L1541 | no | **CORRECTA** |
| `D89` | capa B pierde las dos reglas que `D64` retiró; censo de `abierta(tx)` = nueve | sí, revisa `D71`/`D64`/`D67` | derivé las nueve sedes; `11`:4153 ya dice «UN terminal, `derivada` **o** `abandonada`» | no | **CORRECTA** |
| `D90` | el reparto Git lo fija `C7`; §8 lo **cita** | sí | §8.0 y §18 citan `C7:82`–`C7:92` operación a operación | no | **CORRECTA.** Cierra la mitad `PLT` de `B-2` sin duplicar `C7` |
| `D91` | autoridad para abrir campañas, **derivada** de los aspectos | sí, revisa `D80` | `DECISIONES`:292; prohíbe la lista escrita a mano por `I5` | no | **CORRECTA** *(su proyección en §17 es floja: `K-10`)* |
| `D92` | `<CAP>:revision` como contrato completo para F6 | sí | §19 L8380–8425: edición exacta, propietario `SIS`, fase F6, prueba prescrita | **SÍ** | **INCOMPLETA.** Su regla de derivación no alcanza `proceso:DEP` —donde `SEG` es obligatoria— ni `proceso:AUD` —notación sin tipar—, y su prueba comparte el punto ciego. F6 tendría que **decidir** si `U5b` lleva `SEG:revision` y cómo expresarla. Es `K-02` |
| `D93` | `F-01` reclasificado; nace `PN-14` | sí | `PN-14` §16 L8011–8060, completa | no | **CORRECTA** |
| `D94` | trece condicionales de §5.18, derivadas | sí; `D68` y `D77` conservan su texto | las conté una a una: **trece** | no | **CORRECTA** |
| `D95` | la regla 1 de §2.6.10 usa «los CINCO CAMPOS» | sí, propaga `D66` | `11`:2224–2226 | no | **CORRECTA** |

| resolución/presión | adjudicación |
|---|---|
| **`PN-13`** | **COMPLETA Y LISTA PARA F5.** Qué presiona, texto vigente, por qué no cabe en las diez, por qué no basta un derivado, **materia mínima con dos salidas nombradas**, alcance, se puede construir, bloquea, condición de reversión, origen. F5 redacta sin inventar arquitectura. **Reserva `L-03`** en el párrafo ALCANCE |
| **`PN-14`** | **COMPLETA Y LISTA PARA F5.** Las dos sedes aprobadas verificadas (`b`:895, `a`:495); explica por qué el remedio anterior no era ejecutable; materia mínima precisa; alcance acotado correctamente |
| **`O15`** | **CORRECTA E INTACTA.** Los nueve puntos verificados en `DECISIONES`:402–443. Su cifra caducada («ocho presiones») está reanclada por **nota al pie** en `11`:6121–6125, que dice DOCE **sin tocar la resolución** — el remedio correcto para material del Owner, y `K` hizo bien en retractarse de su sospecha. Procedencia registrada con cita verbatim y fecha en `owner_captado` |
| **`O16`** | **SIN PROCEDENCIA REGISTRABLE.** Su contenido es coherente y no duplica `C7` (los seis puntos son limpios: autoridad en (g), `C8` derivado, `C7` intacto, no se copia la tabla, F5 redacta y F6 materializa, no autoriza iniciar F5). **Pero es la única de las dieciséis resoluciones del Owner sin fecha, sin cita y sin entrada en `owner_captado`, y es la que cierra la sede de `PN-11`.** Ver `L-02` |

---

#### 5 · CIFRAS DERIVADAS POR MÍ

Ninguna copiada del checkpoint ni del fichero de contraste. Método: `grep -n`, `awk`, `sed -n`, `wc`, `comm` y parseo en Python sobre el árbol `0ea0451`.

**Matriz de los 43**
```
filas                       43        ids distintos 43 (uniq -d vacío)
CORREGIDO_EN_F4             31
PRESION_LISTA_PARA_F5        2        B-2 · F-01
CONTRATO_COMPLETO_PARA_F6    2        M-5 · M-6
EXTERNO_CON_PROPIETARIO      7        F-02 F-04 F-06 F-07 F-08 F-10 F-11
HISTORICO_NO_APLICABLE       1        m-3
                          ────
                            43        = el 31·2·2·7·1 declarado. COINCIDE

severidad     BLOQUEANTE 4 · GRAVE 6 · MEDIO 20 · MENOR 13 distintos (14 filas, A11≡M-8)
arquitectura corregida       35 sí · 8 no (los 7 externos puros + m-3)
requieren F5                  3        B-2 (PN-13) · F-01 (PN-14) · F-08 (sin PN)
requieren F6                 11        B-2 M-5 M-6 F-01 F-02 F-04 F-05 F-06 F-07 F-10 F-11
bloquean F5                   0
bloquean F6                   1        B-2, acotado a INS-5 y A9
mi adjudicación              42 SUPERADAS · 0 FALLIDAS · 1 NO APLICABLE
```

**Presiones normativas**
```
bloques ## `PN- en §16      14        PN-1 … PN-14
PN-4  RETIRADA               −1
PN-5  FUSIONADA en PN-3      −1
VIGENTES                     12        ← §19, CHECKPOINT:1430 y :1606 coinciden
                                        ← CHECKPOINT:747, :867 y :1190 dicen DIEZ / ONCE
```

**Eventos, fases y protocolo**
```
tipos (enum §3.6)             9        orden transicion integracion certificacion migracion
                                        sellado retirada-de-cuerpo deriva fallo
fases (enum §3.6)             5        preparada confirmada conflicto abandonada derivada
estados del campo             6        las cinco + la AUSENCIA
filas del contrato condicional 7       las cinco fases + deriva + fallo
transiciones (tabla §2.6.1)   5
ventanas de caída W          17        W1–W11 (11) + W12a W12b W13 W14 W15 W16 (6)
filas adversariales §2.6.7   45 físicas · 45 ids distintos
                                        ← §19 L8298, L1491 y L3173 dicen CUARENTA Y DOS
comprobaciones X-A…X-H        8
escenarios negativos NP      11
escenarios extremo a extremo §14  12
```

**Estructura organizativa**
```
capacidades                  15        directorios en kernel/operativo/capacidades/
procesos de b.16             10        FEA GAP DEF INC INV DEU DEP AUD DIR SIS
macrocircuitos §8.1–§8.4      4        con 14/14 campos cada uno, comprobado etiqueta a etiqueta
items líderes                 N 2 · A 4 · M 2 · U 4
SEG:condiciones (condicional) 4        FEA GAP INC DEU     ← DEP NO, es obligatoria
DOM:condiciones (condicional) 4        FEA GAP DEU DEP
instancias de :revision       0        en todo kernel/operativo/
esquemas .yaml existentes    19        · total declarado §3.8: 19 + 4 estado + 2 clase = 25
campos obligatorios de rol.yaml  29    ← dos sedes vivas siguen diciendo «veintiocho»
áreas documentales obligatorias 12 · condicionales 13 · preguntas del baseline 14
```

**Registro y volumen**
```
decisiones D                 95        sin huecos
resoluciones O               16        sin huecos, pero O16 sin procedencia (L-02)
documento 11                 8437 líneas · §2 ocupa 2928 = 34,7 %
corpus del gate              318 ficheros · J 20 346 líneas · K 30 200 · centrales 24 700
```

**Ejecución, Python 3.10.12**
```
registrar_evidencia.py       10/13 en verde, exit 1 · 3 problemas
T159 FALLIDA · T148 FALLIDA · T171 T151 T152 T158 SUPERADAS
batería del gate de cierre   30/30 desde la raíz · 30/30 desde /tmp por ruta absoluta
causa única de los fallos    tomllib no existe antes de 3.11 → declarado como A14 (PLT, F6)
git status --porcelain       vacío, antes y después
```

**Dos cifras del fichero de contraste del coordinador son incorrectas, y por eso es contraste y no fuente:** «PN vigentes declaradas: 14» —son **12**— y «filas adversariales X únicas: 53», que conflaciona el espacio `X01`–`X61` de §2.6.7 con el espacio `X1`–`X8` de §15.5 y con los huecos de numeración citados en las notas. En §2.6.7 son **45**.

---

#### 6 · DISCREPANCIAS `J`/`K` Y SU RESOLUCIÓN

| # | discrepancia | resolución contra la fuente |
|---|---|---|
| 1 | **Severidad del checkpoint**: `J-10` MENOR frente a `K-01` GRAVE | **A favor de `K`, y más.** Encontré cinco sedes vivas caducadas (L747, L867, L1186, L1190, y la fila `F4c` que se detiene en `D63`), más las dos de `J`. `a.10` regla 3 lo tipifica como defecto del sistema. **GRAVE** |
| 2 | **Proporcionalidad de §2**: `J` (Q15) dice PROPORCIONAL y demostrado; `K` (§6) dice «lo desproporcionado no está en mi lote: §2 ocupa ~2900 líneas y diez tandas para un runtime que no existe», y **declina juzgarlo** | **Resuelta sin conflicto.** Medí §2: **2 928 líneas, 34,7 % del documento** — el dato de `K` es exacto. Pero `K` excluye el juicio por reparto y `J` leyó §2 íntegra. **Prevalece `J` donde `J` leyó**: la proporcionalidad está demostrada, no afirmada (`D64` retiró maquinaria, `D87` retiró la ruta en vez de darle plano, `D74` resolvió sin crear tipo) |
| 3 | **Honestidad de las limitaciones**: `J-11` reprocha que la evidencia publicada afirme 13/13 mientras el entorno da 10/13; `K` sostiene que el corpus es escrupuloso en no presentar limitaciones como demostradas | **Las dos son ciertas y no se contradicen.** El checkpoint L104 **declara** «Validación con Python 3.11.16» y `A14` registra el requisito con propietario y fase — `K` tiene razón. Y no existe guardia, y `T158` sale verde sobre evidencia rancia — `J` tiene razón. Es F6, y está declarado |
| 4 | **Los externos**: `J` (Q20, §5) los da por bien clasificados con sus cuatro atributos; `K-04` demuestra que la nota de reconciliación de §19 se contradice a seis líneas | **Ambas correctas, sobre objetos distintos.** Verifiqué las nueve filas: **cada una** tiene fichero, propietario, fase y condición de cierre — `J` acierta. El **agregado** de §19 L8344 no cierra — `K` acierta. `J` leyó §19 y no lo vio; es un dato sobre la calidad de su cobertura, no una discrepancia |
| 5 | **Censos escritos a mano**: `J-05`/`J-06`/`J-07` y `K-01`/`K-03`/`K-04`/`K-07`/`K-10` | **Convergentes, no discrepantes.** Los dos, sin verse, aíslan la misma causa raíz desde mitades opuestas del corpus. Lo confirmo: **nueve instancias vivas** de la misma clase |
| 6 | **Base de `K-03`** | **La corrijo yo.** `K` la ancla en «la directiva del Owner». `ADS-PENDIENTES` se autodeclara no normativo (L3–L6). El hallazgo sobrevive entero como contradicción interna del documento 11; su base externa, no |
| 7 | **Agravamiento de `K-11`** | **Lo retiro tras verificarlo.** Consideré subirlo a MEDIO por reabrir `F-09`; comprobar el estatus de `ADS-PENDIENTES` lo desactiva. **MENOR, como `K` lo graduó** |
| 8 | **Veredicto** | Ninguna. Los dos recomiendan INSUFICIENTE, por razones distintas y no solapadas |

**Ninguna discrepancia material quedó sin resolver contra la fuente.**

---

#### 7 · COBERTURA

**No.** La unión `J ∪ K` **no** cubrió el inventario obligatorio, y el hecho de que `sin_cubrir.txt` esté vacío sólo dice que todo fichero tenía asignado un lector — no que se leyera.

Lo que la unión deja **sin abrir por nadie**, según las declaraciones de ambos, que acepto porque son contra su propio interés:

```
ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md   ~1 700 de 2 163 líneas
   incluido el BLOQUE B íntegro (§8–§12, certificación por niveles) y el BLOQUE C
   (§13–§15, iniciativa y dosier vivo) — las fuentes de P4, P9 y P10
16-GATE-FINAL-INDEPENDIENTE-F4C.md                 1 257 líneas, sólo barridos
17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md        1 650 líneas, sólo barridos
18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md            ~3 200 de 3 665 líneas
CHECKPOINT-ADS-NEXT.md                            ~900 líneas (L27–829, L872–1171)
                                                  ─────────
                                                  ~8 700 líneas de fuentes CENTRALES
```

Y del documento 11, `J` declara no adjudicar §4, §5, §6.1–§6.6, §8.1–§8.4, §9.1–§9.4, §13 y §14. `K` sí leyó el documento 11 íntegro, y eso salva esa parte.

**La consecuencia, y no es formal.** Sondeé la región muerta y **produjo resultado inmediato**: `ADS-PENDIENTES` §8–§12 me dio la confirmación de que doc 11 §9 es fiel a la propuesta de certificación por niveles, y §12 me dio el «al cerrar Circuito 0» que refuerza `K-06`. Y su cabecera L3–L6 me obligó a **corregir la base de `K-03` y a retirar mi propio agravamiento de `K-11`**. Es decir: las líneas que nadie abrió no son relleno — **contienen material que cambia adjudicaciones en las dos direcciones**. Una de ellas confirmó un hallazgo y otra tumbó una inferencia.

Ese es exactamente el argumento por el que la cobertura incompleta determina el veredicto: **sobre esta muestra nadie puede certificar que no haya algo que refute o agrave lo escrito**, y yo acabo de demostrar, con dos ejemplos, que lo hay.

**Y mi propia cobertura tampoco cumple.** No abrí los documentos 15 ni 17, y del 16 sólo hice barridos. Verifiqué exhaustivamente lo que los dos dictámenes afirman, más tres regiones que ninguno tocó, pero no leí el corpus entero. **Lo declaro como parte del veredicto, no como atenuante.**

---

#### 8 · PROPORCIONALIDAD Y COSTE

**La arquitectura es proporcional, y esta tanda lo demuestra en vez de afirmarlo.** `D64` retiró maquinaria en lugar de añadirle una salida. `D87` retiró la ruta de cuarentena de `estado/` en vez de darle plano. `D74` resolvió la composición **sin crear un tipo**. El recuento de esquemas se calcula (`19 + 4 + 2 = 25`) y se ha movido tres veces al moverse el sustrato. Quince capacidades con doce campos, diez procesos, cuatro macrocircuitos con catorce campos cada uno y diecisiete instancias de handoff **no es ornamental** para el problema declarado.

**Dónde el coste es alto, y se dice.** Once tandas, tres revisiones independientes, dos gates, un complemento y una devolución técnica. §2 ocupa 2 928 líneas —el 34,7 % del entregable— para un runtime que no existe; lo mido y lo digo, aunque `J`, que lo leyó íntegro, sostiene que la densidad está justificada por el problema, y no tengo base para contradecirle.

**La corrección más barata no es más revisión.** Nueve de los veintidós hallazgos nuevos comparten **una sola causa**: censos escritos a mano cuya cobertura no deriva de nada. `J-05` (`AFIRMACIONES`), `J-06` y `K-07` (versión), `J-07` (42 vs 45), `K-01` y `L-01` (checkpoint), `K-04` (7 vs 8), `K-10` y `K-11` (censos de sede). El corpus **ya sabe cómo se arregla** —`comprobar_fuentes.py` lo escribe: «nunca una lista escrita a mano, que es lo que envejece»— y **no se lo ha aplicado a sí mismo**. Mientras `AFIRMACIONES` sea un censo manual y `comprobar_versiones` recorra dos ficheros, cada tanda dejará una cifra atrás y cada gate la encontrará.

**Una observación sobre el ciclo.** `J-07` es la undécima vez consecutiva que una tanda introduce un defecto de su propia clase declarada. Y `K-02` es peor que eso: **una corrección anterior (`D75`, que cerró `G-1` y que yo adjudico SUPERADA) desactivó, sin que nadie lo viera, la cadena de la que dependería una corrección posterior (`D92`)**. Eso no se arregla con otra pasada del mismo autor.

---

#### 9 · LÍMITES POSTERIORES

Lo que queda para runtime, piloto y PesquerApp, y **si está bien declarado**:

| límite | dónde se declara | ¿bien declarado? |
|---|---|---|
| **Nada está construido** | §19 L8296 | **Sí.** «ni una línea de kernel, runtime, tooling, esquema, adaptador, plantilla, pack ni validador» |
| **Nada está probado** | §19 L8297–8305 | **Sí en su disciplina** —«Escribir el contrato de una prueba no es la prueba»— **con la cifra mal**: dice 42 filas adversariales donde hay 45 (`J-07`) |
| **No hay runtime** | §9.4 L6675 | **Sí, y ejemplarmente.** «hasta que exista runtime, **ninguna instalación ni adopción puede declararse terminada y plenamente certificada**» |
| **Ningún adaptador certificado** | §19 L8307; §6.7 L5407–5411 | **Sí.** «hasta que se ejecute [la prueba de humo], el nivel alcanzado de ese adaptador es `desconocido`» |
| **El piloto sigue pendiente** | §14 L7213–7214, L7236 | **Sí.** «Ninguno se ha ejecutado… **Lo que NO demuestran**: que funcionen. Para eso hace falta el piloto de `O14`» |
| **PesquerApp no adoptada** | `O15` punto 9; §19 L8308–8310 | **Sí, y es de lo mejor del entregable.** «`O15` **no la autoriza ni la programa**: dice qué será cuando ocurra» |
| **Reanudación distribuida** | §2, `D70` | **Sí.** «REINICIO SEGURO, no reanudación, **y no se llama de otra manera**» |
| **La cuarentena no se reconstruye** | §2.9 L2871 | **Sí.** «si se pierde antes del commit del incidente, lo divergente se pierde con ella» |
| **`X1` y `P-05` deferidas** | §19 L8306 | **Sí** |
| **`python_requires ≥ 3.11`** | §19 `A14`, `08-EVIDENCIA-MULTIREPO` | **Sí**, con propietario `PLT` y fase F6. Lo que falta es la guardia (`J-11`), que es F6 |
| **La distancia real** | §19, última línea | **Sí, y sin adornos.** «ADS sigue siendo un corpus verificado contra sí mismo y **cero veces contra la realidad**. Esta arquitectura dice cómo cerrar esa distancia. **No la cierra.**» |

**Conclusión de este apartado: las limitaciones que exigen runtime, piloto o PesquerApp están declaradas, con su propietario y su fase, y NO se presentan como demostradas.** Esa disciplina es real y la reconozco expresamente. **Nada de esto fundamenta mi veredicto.**

---

#### 10 · VEREDICTO

##### INSUFICIENTE PARA F5

Emitido tras verificar cada afirmación material contra su fichero y su línea, sin resolver por mayoría ni por deferencia, y rechazando lo que no se sostuvo (`J-09`, y la base externa de `K-03`, y mi propio agravamiento de `K-11`).

**Falla por seis razones independientes. Cualquiera de ellas bastaría.**

**1 · COBERTURA INCOMPLETA.** ~8 700 líneas de fuentes centrales obligatorias que **ningún revisor abrió** —incluidos los BLOQUES B y C de `ADS-PENDIENTES` y ~6 100 líneas de los documentos 16, 17 y 18—. Y mi propia cobertura tampoco cumple. Sondeé la región muerta y produjo dos cambios de adjudicación en direcciones opuestas: no es relleno.

**2 · UN BLOQUEANTE ARQUITECTÓNICO ABIERTO.** `J-01`: `revision_base` es condición 5 de arranque, ancla exacta de la restauración, lo que hace `abandonada` alcanzable y el sostén de «`main` nunca contiene estado parcial» — y **no está declarado en §3.6 ni en ninguna capa**. Es la clase exacta de `A1`, que este mismo corpus graduó BLOQUEANTE con estas palabras: «el esquema derivado literalmente de §3.6…». `PN-1` propone aprobar §2 como (g), y aprobarla consagraría un contrato de evento que no puede representar ese dato.

**3 · GRAVES ARQUITECTÓNICOS ABIERTOS.** `J-02` (colisión de `tx` en la reparación), `K-02` (`D92`), `K-03` (el gate de `M7`), `K-06` (`G20`–`G23`), `K-01` (checkpoint) y `L-02` (`O16`).

**4 · UN CONTRATO F6 QUE TODAVÍA EXIGE DECIDIR ARQUITECTURA.** `K-02`: `D92` entrega a F6 una regla de derivación —barrido de `:condiciones`— que **no puede alcanzar `proceso:DEP`**, donde `SEG` participa como obligatoria, ni `proceso:AUD`, cuya notación no está tipada; y `U5b` **es** `proceso:DEP`, uno de los tres tramos que `D92` nombra como los que escriben en las fuentes del producto. La prueba que `D92` prescribe pasaría en verde sobre un árbol sin `SEG:revision` en `DEP`. F6 tendría que decidir la forma.

**5 · CONTRADICCIÓN ENTRE FUENTE NORMATIVA Y ARQUITECTURA SIN PRESIÓN F5.** `K-06`: `KERNEL.md` 1.5.0 `G21` declara que **el gate de salida del Circuito 0 lo fija la constitución y NO es negociable por el sistema**; `G22` fija su timebox, sus diez entregables y sus cuatro prohibiciones; `a.11` —«la única lista que deroga o ajusta reglas de 1.3.0», según `PN-3`— **no nombra `G20`, `G21`, `G22` ni `G23`**, y `E2.4` demuestra que lo no nombrado sobrevive. §17 declara la ruta A de `START_HERE` «sustituida por §8.1», y §8.1 define un gate distinto, sin timebox, sin los diez entregables y con un C0 redefinido. **§17 no tiene fila para `KERNEL.md`.** Cuatro reglas constitucionales presionadas y ninguna registrada.

**6 · CHECKPOINT NO VIGENTE.** `K-01` + `J-10` + `L-01`. Cinco sedes vivas caducadas, entre ellas el campo `pregunta_pendiente`, el bloque `Estado de las fases` y el `RESULTADO` que introduce la matriz. `a.10` regla 3 lo tipifica: «es **un defecto del sistema**, no una omisión menor». Y su función es reanclar a un agente sin contexto: quien lo haga hoy recibe un censo que omite `PN-13` y `PN-14`.

**Lo que expresamente NO fundamenta este veredicto.** No declaro insuficiencia porque F5 no esté escrita, ni porque F6 no esté implementada, ni porque no exista runtime, ni porque el piloto no se haya ejecutado, ni porque PesquerApp no esté adoptada, ni porque los escenarios no sean todavía pruebas ejecutables, ni porque tres validadores exijan Python 3.11. Todo eso está **correctamente declarado**, con propietario y fase, y el corpus es escrupuloso en no presentarlo como demostrado.

---

##### Condiciones de cierre exactas

Ordenadas por lo que realmente bloquea.

**Bloquean el paso a F5:**

- **`C-L.1` — `J-01` + `J-02`.** Declarar `revision_base` como campo **OBLIGATORIO de `preparada`** en §3.6, registrable en `conflicto` y en `abandonada`, y **decir expresamente si entra en el cómputo de `tx`** de §2.8. Cinco líneas. Cierra los dos hallazgos a la vez y no hay nada que decidir.
- **`C-L.2` — `K-06`.** Resolver `G20`–`G23`: o una fila en `a.11` que las derogue, sustituya o ajuste —lo que es material APROBADO y por tanto **una `PN` nueva**, como `PN-3` para `G03`—, o una fila en §17 para `kernel/KERNEL.md` que declare qué le pasa. **No es electivo**: `G21` dice de su gate que no es negociable por el sistema, y F4 lo ha negociado.
- **`C-L.3` — `K-02`.** Reformular la regla de derivación de `D92` para que opere sobre **la participación de `DOM`/`SEG` cualquiera que sea su vía** —obligatoria, condicional o tipada—, y no sobre la cadena `:condiciones`. Extender su prueba prescrita en el mismo sentido. Mientras no se haga, F6 no puede construir `U5b` sin decidir.
- **`C-L.4` — `L-02`.** Registrar la procedencia de `O16` con la misma disciplina que `O7`–`O14` y `O15`: fecha, cita y entrada en `owner_captado`. **O retirarla y devolver `PN-11` a la lista de presiones sin sede.** Una resolución del Owner que el corpus no puede atribuir no puede cerrar una presión nacida de un BLOQUEANTE.
- **`C-L.5` — COBERTURA.** Un gate con revisores de contexto limpio que lean **íntegro** lo que nadie abrió: `ADS-PENDIENTES` completo —BLOQUES B y C incluidos— y los documentos 16, 17 y 18 completos. Y **que no lo aplique quien lo reciba**: ésa es la razón por la que once tandas se han encadenado.

**No bloquean F5, pero deben quedar cerradas o registradas:**

- **`C-L.6` — `K-03`.** Que la línea `GATES` de §8.3 diga **cinco salidas verdes**, o que §8.2 L6186 y `M7 VERIFICAR` L6298 digan cuatro. Hoy el gate vinculante del único paso destructivo omite la única comprobación que interroga lo que ese paso retira.
- **`C-L.7` — `K-01` + `J-10` + `L-01`.** Reescribir el bloque `Estado de las fases`, el campo `pregunta_pendiente`, la fecha `actualizado`, la línea de estado y el `RESULTADO` que introduce la matriz. Un bloque de estado existe para reescribirse; la regla de no reescribir historia protege el registro `D`/`O` y las resoluciones del Owner, no esto.
- **`C-L.8` — `J-04`.** Una frase: el `hash_previo` de la reparación es el `hash_observado` que el `deriva` registró, **para las tres causas**. Cae dentro de §2, que es lo que (g) aprobará.
- **`C-L.9` — `J-07` + `K-04`.** Derivar o retirar: las tres cifras de 42 (§19 L8298, L1491, L3173) frente a las 45 reales, y la reconciliación de externos de §19 L8344 (9 = 7 + `F-01` + `F-05`, no 8 + 1). Extender `G-26` para que compare **prosa contra derivado**, no sólo filas contra ids.
- **`C-L.10` — `J-05` + `J-06` + `K-07`.** Derivar el censo `AFIRMACIONES` y ampliar el alcance de `T152` más allá de `README.md` y `START_HERE.md`. Es F6, y es **la corrección más barata del entregable**: cierra de una vez nueve hallazgos de nueve tandas distintas.
- **`C-L.11` — `J-03`.** Fila adversarial propia para §6.7, o registro explícito como contrato de prueba para F6. `X51` cubre otro escenario.
- **`C-L.12` — `J-08`.** Registrar como material de F5 los dos restos de (b): la cita «(P7)» de `b`:358 donde aplica `P9`, y la numeración 1,2,5,3,4 de `b`:468.
- **`C-L.13` — `K-05`, `K-09`, `K-10`, `K-08`, `L-03`, `J-11`.** El escenario 3 de §14 (`M5` → `M6`); el enlace colgante de `entrada/02-CIRCUITO.md`:54; la presentación de §17 sobre `D91`; la invocación redundante de la excepción de `a.7` en §8.0; el párrafo ALCANCE de `PN-13`; y la guardia de versión de intérprete, que es F6 y ya tiene propietario en `A14`.

---

##### Y lo que quiero que conste, porque un gate que sólo publica lo que falla tampoco es una medida

**Ésta es, con diferencia, la candidata más sólida de la cadena, y lo digo tras haberla verificado y no tras haberla leído.**

Las diez filas que el gate anterior declaró FALLIDAS **están cerradas, y comprobé las diez contra su sede**. Los cuatro BLOQUEANTES de la tanda anterior están cerrados por su causa, uno de ellos **retirando maquinaria en vez de parchearla**. `D67` está restaurada **byte a byte**, y lo verifiqué con `git show` y `diff`. `D87`–`D95` son todas revisoras y **ninguna reescribe una decisión anterior**, lo que comprobé con un diff completo del registro. La batería propia da **30/30 desde dos ubicaciones distintas** y su README declara, sin que nadie se lo exigiera, que la escribió quien aplicó la corrección y que por eso no certifica nada. Las doce presiones están listas para que F5 redacte sin inventar arquitectura, y las dos nuevas —`PN-13` y `PN-14`— son de las mejor construidas del corpus: materia mínima, alcance, condición de reversión y origen. Los siete externos tienen fichero, propietario, fase y condición de cierre, uno a uno. El protocolo transaccional de §2 distingue con precisión poco común atomicidad, durabilidad de proceso y de máquina, commit local, push y clon nuevo; nombra el error del `fsync` de directorio; y **declara lo que NO ofrece**. `C5` se autolimita con nitidez. Las doce y trece áreas son fieles a la directiva, incluida la decisión del Owner de dejar diseño y datos como condicionales.

**Nada de lo que impide el paso exige inventar arquitectura para cerrarse.** El bloqueante son cinco líneas en §3.6. Los cinco graves tienen remedio acotado y nombrado. La cobertura exige una lectura, no un rediseño.

Pero son un bloqueante y cinco graves, están sin resolver, la cobertura del corpus obligatorio está incompleta, el checkpoint no está vigente y una resolución del Owner no es atribuible. **El criterio que se me dio es explícito en que cualquiera de esas cosas impide el paso.**

`F4c` sigue **ABIERTA**. **F5 NO queda autorizada.**
---

## 8 · Hallazgos nuevos, discrepancias y resolución

Están dentro de la adjudicación de `L`, §3 y §6, transcritas arriba. `L` confirmó, rechazó y regraduó los veintidós hallazgos nuevos de `J` y `K`, añadió tres propios —`L-01`, `L-02`, `L-03`— y **rechazó `J-09`, la base externa de `K-03` y su propio agravamiento de `K-11`**.

## 9 · Proporcionalidad y coste

Los tres coinciden en que la arquitectura **no es ornamental**, y los tres lo argumentan desde piezas concretas: `D64` retiró maquinaria en vez de parchearla, `D87` retiró una ruta en vez de darle plano, `D74` resolvió sin crear un tipo, y el recuento de tipos se calcula y por eso se ha movido tres veces.

Y los tres señalan la misma causa sistémica del goteo de defectos: **hay censos escritos a mano donde deberían derivarse**. `K` lo cuantifica: `A6`, `A10`, `M-1`, `m-1`, `F-10`, `E-10` y sus tres propios son la séptima, octava y novena ocurrencia. `L` lo convierte en la condición de cierre más barata del entregable —`C-L.10`—, que cierra de una vez nueve hallazgos de nueve tandas distintas.

## 10 · Límites posteriores

Lo que **no** fundamenta este veredicto, dicho por los tres para que nadie lo lleve al Owner como si lo fuera:

```text
NO ES DEFECTO DE F4c    que F5 no esté escrita · que F6 no esté implementada · que no
                        exista runtime · que el piloto no se haya ejecutado · que
                        PesquerApp no esté adoptada · que los escenarios no sean todavía
                        pruebas ejecutables · que tres validadores exijan Python 3.11

POR QUÉ                 todo eso está CORRECTAMENTE DECLARADO, con propietario y fase, y
                        el corpus es escrupuloso en NO presentarlo como demostrado.
                        `L` lo dice tras verificarlo: «§9 dice que hoy no hay adaptador
                        certificado, `O13` fija un objetivo y no lo da por alcanzado, y el
                        registro de pruebas es honesto».
```

## 11 · Veredicto

# INSUFICIENTE PARA F5

**`F4c` sigue ABIERTA. `F5` NO queda autorizada.**

Emitido por el adjudicador `L` tras verificar cada afirmación material contra su fichero y su línea, sin resolver por mayoría y rechazando lo que no se sostuvo. Falla por **seis razones independientes**, cualquiera de las cuales bastaría: cobertura incompleta · un bloqueante arquitectónico abierto (`J-01`) · **SEIS** graves arquitectónicos abiertos —ver el corrigendum de §12— · un contrato F6 que todavía exige decidir arquitectura (`K-02`) · una contradicción con material normativo sin presión F5 (`K-06`) · y un checkpoint no vigente.

**Ningún hallazgo se ha corregido en esta pasada.** Corregirlos aquí volvería a hacer que quien recibe sea quien aplica, que es la razón por la que once tandas se han encadenado.

**Y consta, porque un gate que sólo publica lo que falla tampoco es una medida:** los tres revisores coinciden en que ésta es, con diferencia, la candidata más sólida de la cadena. Las diez filas que el gate anterior declaró FALLIDAS están cerradas, verificadas una a una contra su sede. `D67` está restaurada byte a byte. `D87`–`D95` son todas revisoras y ninguna reescribe una decisión anterior. La batería da 30/30 desde dos ubicaciones y declara por sí misma que no certifica nada. **Nada de lo que impide el paso exige inventar arquitectura para cerrarse:** el bloqueante son cinco líneas en §3.6.

---

## 12 · CORRIGENDUM · recuentos derivados, y una errata del propio gate

> **Añadido por la TANDA DE CORRECCIÓN posterior, FUERA de toda transcripción.** Los
> dictámenes literales de `J`, `K` y `L` de §3, §4 y §5 **no se han tocado**: conservan cada
> palabra, incluida la que este apartado corrige. Un gate se conserva como se emitió; lo que
> se reancla es la cifra vigente, y se hace aquí, donde se ve que es una corrección y de
> quién.

### 12.1 · La errata: «cinco graves» junto a SEIS identificadores

El dictamen de `L` dice, en dos sedes de su texto literal —§5.10, «Y lo que quiero que
conste»— «**los cinco graves**» y «**un bloqueante y cinco graves**». Y en su razón 3 del
veredicto enumera:

```text
J-02 · K-02 · K-03 · K-06 · K-01 · L-02        →  SEIS identificadores
```

**Son seis, no cinco.** El error es de recuento en la prosa, no de adjudicación: las seis
filas están adjudicadas GRAVE una a una en §5.3, y ninguna de las seis está en duda.

### 12.2 · Las severidades, DERIVADAS de las filas adjudicadas

Ningún total de este bloque se copia de la prosa de nadie. Se deriva recorriendo las filas de
adjudicación de `L` en §5.3 y leyendo la severidad que cada una lleva escrita:

```text
J-01  BLOQUEANTE   (L lo SUBE desde el GRAVE que J proponía)
J-02  GRAVE          K-01  GRAVE   (L lo sube desde MENOR de J-10 y lo agrava)
J-03  MEDIO          K-02  GRAVE   (agravado por L)
J-04  MEDIO          K-03  GRAVE   (mantenido, con su base externa CORREGIDA por L)
J-05  MEDIO          K-04  MEDIO
J-06  MENOR          K-05  MEDIO
J-07  MEDIO          K-06  GRAVE   (L lo SUBE desde el MEDIO que K proponía)
J-08  MENOR          K-07  MEDIO
J-09  RECHAZADO      K-08  MENOR         L-01  MEDIO
J-10  MEDIO          K-09  MENOR         L-02  GRAVE
J-11  MEDIO          K-10  MENOR         L-03  MENOR
                     K-11  MENOR   (L RETIRA su propio agravamiento)

PLANTEADOS                     25     11 de J · 11 de K · 3 de L
RECHAZADOS                      1     J-09
CONSOLIDADOS                   24     = 25 − 1

BLOQUEANTE                      1     J-01
GRAVE                           6     J-02 · K-01 · K-02 · K-03 · K-06 · L-02
MEDIO                          10     J-03 J-04 J-05 J-07 J-10 J-11 K-04 K-05 K-07 L-01
MENOR                           7     J-06 J-08 K-08 K-09 K-10 K-11 L-03
                             ────
                               24     COINCIDE con los consolidados
```

### 12.3 · Tres cosas distintas que no hay que confundir

```text
HALLAZGOS CONSOLIDADOS      24. Todo lo que sobrevivió a la adjudicación, con
                            independencia de si bloquea

HALLAZGOS QUE EL VEREDICTO   5. `J-01` (BLOQUEANTE), y los graves `J-02`, `K-02`, `K-06` y
USA COMO BLOQUEANTES DEL     `L-02`. Son exactamente los que sostienen `C-L.1`–`C-L.4`.
PASO                         **`K-01` y `K-03` son GRAVES y NO bloquean**: sus condiciones
                             —`C-L.7` y `C-L.6`— están en el grupo que `L` titula «no
                             bloquean F5, pero deben quedar cerradas o registradas».
                             Ser GRAVE y bloquear el paso no son lo mismo, y `L` las separa
                             **La sexta razón que bloquea NO es un hallazgo: es la
                             COBERTURA** (`C-L.5`)

CONDICIONES DE CIERRE       13. `C-L.1`–`C-L.13`. **Cinco bloquean** —`C-L.1` a `C-L.5`— y
                            **ocho no** —`C-L.6` a `C-L.13`—. No hay correspondencia uno a
                            uno con los hallazgos: `C-L.1` cierra dos (`J-01`+`J-02`),
                            `C-L.7` cierra tres (`K-01`+`J-10`+`L-01`), `C-L.13` cierra seis
```

### 12.4 · Dónde se ha propagado la cifra derivada

`SEIS GRAVES` queda escrito en las **sedes de estado vigentes** —la línea de estado y
`falta_para_cerrar_la_capa` del checkpoint, y la fila del índice de `docs/evolucion/`—, y
`CINCO GRAVES` **se conserva intacto donde `L` lo escribió**. La regla es la misma que la
nota al pie de `O15`, y la misma que este corpus aplica a los enums sustituidos: **la
proyección vigente es una, las citas históricas son muchas, y están marcadas como tales.**

### 12.5 · Un residuo de transcripción, retirado

La transcripción del dictamen de `L` arrastraba, pegadas a su última línea, cuatro líneas de
**metadatos de la herramienta** que lo ejecutó —un identificador de agente y un bloque
`<usage>` con contadores de tokens, llamadas y milisegundos—. **No eran texto de `L`**: eran
exhaust del arnés, adheridos al transcribir. **Se retiran**, y con ello la última línea del
dictamen vuelve a ser exactamente la que `L` escribió: «`F4c` sigue ABIERTA. F5 NO queda
autorizada.» Retirarlos **restituye** la literalidad en vez de alterarla, y consta aquí
porque el defecto lo introdujo el coordinador al transcribir, no el adjudicador al juzgar.

### 12.6 · Y qué NO cambia este corrigendum

**El veredicto no cambia, y no podía cambiar.** `INSUFICIENTE PARA F5` se sostiene sobre
**seis razones independientes, cualquiera de las cuales bastaría**, y la primera —la
cobertura— no depende de ningún recuento. Que los graves sean seis y no cinco **agrava** el
cuadro; no lo alivia. Ninguna adjudicación de `L` se toca, ningún hallazgo se reclasifica y
ninguna de las trece condiciones de cierre se retira.
