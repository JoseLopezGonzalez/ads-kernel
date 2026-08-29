# CHECKPOINT — ADS NEXT

> Registro persistente y reanudable de la iniciativa. Formato de
> [`a.10`](../rediseno/a-CAPACIDADES-APROBADA.md), copiable desde
> [`plantillas/CHECKPOINT.md`](../../kernel/operativo/plantillas/CHECKPOINT.md).
> **Basta decir «Continúa»**: la siguiente acción exacta está al final.

> **Estado de la fase, en una línea:**
> **El GATE DEFINITIVO INDEPENDIENTE devolvió INSUFICIENTE PARA F5 sobre `r4`=`0ea0451`, y
> sus TRECE condiciones de cierre están APLICADAS — NO CERTIFICADAS. `F4c` sigue ABIERTA y
> `F5` NO queda autorizada: falta un gate independiente NUEVO sobre el resultado corregido.**
>
> Lo emitió un **adjudicador `L`** con contexto limpio sobre los dictámenes cerrados de dos
> revisores independientes, `J` y `K`, que trabajaron en paralelo sin verse. `L` verificó
> cada afirmación material contra su fichero y su línea, **sin resolver por mayoría**, y
> **rechazó** `J-09`, la base externa de `K-03` y su propio agravamiento de `K-11`. Está en
> [`19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md`](19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md).
>
> **SEIS razones independientes, y cualquiera bastaría:** cobertura incompleta —~8 700 líneas
> de fuentes centrales que **ningún** revisor abrió—; **un BLOQUEANTE** (`J-01`:
> `revision_base` sostiene la condición 5 de arranque, el ancla de la restauración y la
> alcanzabilidad de `abandonada`, y **no estaba declarado en §3.6 ni en ninguna capa**);
> **SEIS GRAVES** (`J-02`, `K-01`, `K-02`, `K-03`, `K-06`, `L-02`); un contrato F6 que aún
> exigía decidir arquitectura; una contradicción con `G20`–`G23` sin presión F5; y un
> checkpoint no vigente.
>
> **La cifra es SEIS y está derivada de las filas adjudicadas por `L`.** El texto literal del
> documento 19 dice «cinco graves» y **enumera seis identificadores**: su dictamen se
> conserva intacto y la corrección va en un **corrigendum externo** del propio documento 19.
> Derivado: **25 hallazgos planteados · 1 RECHAZADO (`J-09`) · 24 consolidados —
> BLOQUEANTE 1 · GRAVE 6 · MEDIO 10 · MENOR 7**.
>
> **Ningún hallazgo se corrigió DURANTE el gate**, y era deliberado. Lo que vino después
> **no es «todo corregido»**, y decirlo así sería presentar un registro como una
> implementación. Las trece condiciones quedan en **cuatro estados distintos**, y sólo el
> primero significa que el trabajo esté hecho:
>
> ```text
> CORREGIDAS EN F4c        `C-L.1` `C-L.3` `C-L.4` `C-L.6` `C-L.7` `C-L.8` `C-L.9` `C-L.11`
>   ocho                   y los cinco residuos de `C-L.13`. El cambio está ESCRITO en su
>                          sede y es comprobable hoy
>
> REGISTRADAS PARA F5      `C-L.2` · `PN-15`: `G20`–`G23` PRESIONADAS, y **la decisión sigue
>   dos                    sin tomar** — es del Owner, y F4 no puede tomarla
>                          `C-L.12` · los dos restos de (b), como checklist verificable
>                          **Registrar NO es corregir**: el texto de (b) sigue como estaba
>
> CONTRATADAS PARA F6      `C-L.10` —censo `AFIRMACIONES` derivado, `T152` sobre toda sede
>   dos                    que publique versión— y `J-11` —la guardia de intérprete—.
>                          **Contratar NO es implementar**: no existe ni una línea de código
>                          de las tres, y `T151` y `T152` siguen pasando en verde sobre las
>                          sedes que el corpus desmiente
>
> ABIERTA POR COBERTURA    `C-L.5`. **No la cierra esta tanda ni puede cerrarla**: aplicar
>   una                    correcciones no es leer lo que no se leyó. Sólo la cierra el gate
>                          siguiente, con revisores de contexto limpio y lectura real
> ```
>
> **Aplicar no es certificar**, y **registrar o contratar no es corregir**.
>
> **Y consta:** los tres coinciden en que es la candidata más sólida de la cadena. Las diez
> filas FALLIDAS del gate anterior están cerradas, verificadas una a una. **Nada de lo que
> impedía el paso exigía inventar arquitectura: el bloqueante eran cinco líneas en §3.6, y
> están escritas.**

> **El GATE FINAL INDEPENDIENTE devolvió INSUFICIENTE PARA F5, y su NIVEL 0 —la cobertura que
> faltaba— está CERRADO. F4c sigue ABIERTA, y F5 NO queda autorizada.**
>
> El nivel 0 lo cerraron **otros tres agentes con contexto limpio** —revisores `D` y `E` en
> paralelo, adjudicador `F`— leyendo **las diecinueve fuentes obligatorias** que ningún
> revisor del gate había abierto: **8 310 líneas**. Está en
> [`17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md`](17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md).
> **Ningún hallazgo se retiró ni se rebajó, y ninguna severidad se movió.**
>
> Lo emitió un **adjudicador C** con contexto limpio sobre los dictámenes cerrados de **dos
> revisores independientes**, A y B, que trabajaron en paralelo sin verse. C verificó los
> **33 hallazgos uno a uno contra su fichero y su línea**, **sin resolver por mayoría**, y
> rechazó piezas de cinco de ellos. Está en
> [`16-GATE-FINAL-INDEPENDIENTE-F4C.md`](16-GATE-FINAL-INDEPENDIENTE-F4C.md).
>
> **DOS razones independientes, y cualquiera bastaría:** la cobertura del corpus obligatorio
> quedó **incompleta —dieciocho fuentes sin abrir por ninguno de los dos—**, y hay **CUATRO
> BLOQUEANTES y SEIS GRAVES confirmados**. **Ningún hallazgo se ha corregido**: hacerlo en la
> misma pasada volvería a que quien recibe sea quien aplica.
>
> La emitió un revisor con contexto limpio que **no escribió F4 ni aplicó ninguna de sus
> correcciones**, sobre el árbol `df05929`: **DOS BLOQUEANTES, ocho GRAVES, cinco MEDIOS y
> siete MENORES**, más quince hallazgos que intentó y **no pudo reproducir**. Está en
> [`15-TERCERA-REVISION-INDEPENDIENTE-F4C.md`](15-TERCERA-REVISION-INDEPENDIENTE-F4C.md).
> **Ninguno de sus hallazgos se ha corregido**: corregirlos en la misma pasada volvería a
> hacer que quien recibe sea quien aplica.
>
> Y por una **corrección técnica posterior** sobre el protocolo transaccional, que encontró
> **dos bloqueantes más** en el texto que las correcciones anteriores escribieron. Tampoco es
> la tercera revisión, y tampoco certifica nada.
>
> Y por una **SEGUNDA corrección técnica**, que encontró **tres GRAVES más** —garantías
> atribuidas a un esquema que no puede comprobarlas, `W12a` contra la clasificación por
> hashes, y siete valores de `tipo` sin contrato— **en el texto que la corrección anterior
> escribió**. Tampoco es la tercera revisión, y tampoco certifica nada.
>
> Y por una **TERCERA COMPROBACIÓN TÉCNICA acotada**, que encontró **dos defectos más** en el
> texto que la segunda escribió: el recuento de fases mezclaba `tipo` con `fase`, y la
> «reemisión» admitía un `confirmada → confirmada` que §2.8 ya prohibía. Es el **CUARTO**
> encadenamiento consecutivo en el que una pasada encuentra defectos de la anterior. Tampoco
> es la tercera revisión, y tampoco certifica nada.
>
> Y por una **CUARTA COMPROBACIÓN TÉCNICA acotada**, que encontró **dos defectos más** en el
> texto que la tercera escribió: una cardinalidad que **ninguna transacción podía cumplir**, y
> una frontera de recursión **falsa** que clasificaba mal `sellado`. **Quinto** encadenamiento
> consecutivo. Tampoco es la tercera revisión, y tampoco certifica nada.
>
> Y por una **QUINTA COMPROBACIÓN TÉCNICA de un solo punto**, que encontró que un único campo
> `iteracion` numeraba **observaciones e intentos a la vez** y valía 4 bajo un máximo de 3.
> **Sexto** encadenamiento consecutivo. Tampoco es la tercera revisión, y tampoco certifica
> nada.
>
> Y por una **SEXTA COMPROBACIÓN TÉCNICA** sobre la semántica de sellado y retirada de
> cuerpo: la lápida conservaba un `id` que **ya no podía recalcularse**, la huella se
> presentaba como prueba de contenido, y la regla de bloqueo hacía **inalcanzable la propia
> retirada**. **Séptimo** encadenamiento consecutivo. Tampoco es la tercera revisión, y
> tampoco certifica nada.
>
> La segunda revisión la emitió un revisor con contexto limpio que **no escribió F4 ni aplicó
> la primera crítica**, y su veredicto fue de **INSUFICIENCIA**: dos hallazgos BLOQUEANTES,
> siete GRAVES y catorce nuevos. **Dos de ellos eran defectos que la PRIMERA corrección
> introdujo o no vio.** Las correcciones las APLICÓ el autor material de F4. **Aplicar una
> crítica no prueba que esté bien resuelta**, y por eso `F4c` **no se declara cerrada aquí**.

```text
CHECKPOINT — ADS-NEXT/12 · SIS/evolucion
actualizado: 2026-08-29
metodo:      SIS/Evolucion · TANDA DE CORRECCIÓN DEL GATE DEFINITIVO APLICADA · D96–D102 ·
             y CORRECCIÓN TÉCNICA ACOTADA sobre ella · D103 · las TRECE condiciones C-L en
             CUATRO estados: 8 CORREGIDAS EN F4c · 2 REGISTRADAS PARA F5 · 2 CONTRATADAS
             PARA F6 · 1 ABIERTA POR COBERTURA (C-L.5) · APLICADA, NO CERTIFICADA ·
             F4c ABIERTA · F5 NO AUTORIZADA
metodo_anterior: SIS/Evolucion · GATE DEFINITIVO INDEPENDIENTE EJECUTADO SOBRE r4=0ea0451 ·
             VEREDICTO INSUFICIENTE PARA F5 · F4c ABIERTA · F5 NO AUTORIZADA
based_on:    docs/evolucion/09-SINTESIS.md@56ea196 + su addendum
             docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md@56ea196
             docs/evolucion/11-ARQUITECTURA-INTEGRADA.md   corregida
             docs/evolucion/12-CRITICA-INDEPENDIENTE-F4.md
             docs/evolucion/13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md
             docs/evolucion/14-DEVOLUCION-TECNICA-PREVIA-F4C.md
             docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md   VEREDICTO,
                                                             corregido por D64–D68
             docs/evolucion/16-GATE-FINAL-INDEPENDIENTE-F4C.md    A · B · C ·
                                                             VEREDICTO FINAL
             docs/evolucion/17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md   D · E · F ·
                                                             NIVEL 0 CERRADO
             docs/evolucion/18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md
             docs/evolucion/19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md   J · K · L ·
                                                             VEREDICTO INSUFICIENTE
             docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md   O7–O14 · O15 · O16 · D16–D22 ·
                                                             D23–D33 · D34–D45 · D46–D51 ·
                                                             D52–D54 · D55–D57 · D58–D59 ·
                                                             D60–D61 · D62 · D63 · D64–D68 ·
                                                             D69–D70 · D71–D95 · D96–D102 ·
                                                             D103
             kernel/VERSION@2.0.0-alpha.9 · kernel/KERNEL.md@1.5.0
rama_de_trabajo: fix/f4c-post-gate-definitivo-20260829, creada en 652ab8e —el commit del
             gate definitivo, publicado en review/f4c-gate-definitivo-20260829—. Sin
             upstream. El SHA del árbol vigente se DERIVA de Git y no se escribe aquí:
             `git rev-parse HEAD` sobre esa rama, y su base con
             `git rev-parse 652ab8e011c3ae567592e7f12add9f69880f6a5b`
freshness:   vigente. La cabecera separa ESTADO HISTÓRICO de ESTADO VIGENTE: lo dicho bajo
             Python 3.10 —9/13, T158 fallida, cobertura 291 frente a 293, nada publicado—
             queda marcado HISTÓRICO y SUPERADO, y no se borra
last_meaningful_event: CORRECCIÓN TÉCNICA ACOTADA sobre la candidata publicada, y es D103.
             D98 había retirado el barrido léxico de su CRITERIO y lo reintroducía en su
             ALGORITMO —marcaba una participación como condicionante buscando «ANTES de
             construir» en TEXTO LIBRE—, y publicaba «seis procesos, diez pares exigidos»,
             cardinalidad que ningún árbol puede satisfacer. Derivado de campos
             ESTRUCTURADOS, el catálogo da CINCO procesos y NUEVE pares, con (DEP, SEG) por
             la obligatoria; y proceso:AUD NO tiene cardinalidad estática: su propietario es
             DERIVADO por item, luego cada item exige DOM:revision, SEG:revision o NINGUNA —
             cero o un par, NUNCA los dos—. D103 separa los dos niveles y no los suma.
             G-15 pasaba en VERDE sobre las dos cosas porque buscaba palabras en vez de
             derivar: ahora EJECUTA la derivación, contrasta la proyección con lo derivado
             sin escribir el nueve en la prueba, y corre tres fixtures de item AUD.
             D98 NO se reescribe. Y el checkpoint deja de decir «todos corregidos»: las
             trece condiciones quedan en CUATRO estados separados (2026-08-29)
last_meaningful_event_anterior: se APLICA la TANDA DE CORRECCIÓN del gate definitivo. D96–D102, todas
             revisoras y ninguna reescribe D1–D95. PN-15 registra que G20–G23 de KERNEL.md
             están PRESIONADAS y pendientes de F5, NO derogadas. O16 gana procedencia real
             —fecha, formulación presentada y respuesta literal del Owner— sin crear O17.
             X62 da a §6.7 fila propia. Doce de las trece condiciones C-L quedan cerradas o
             registradas; C-L.5, la COBERTURA, sigue ABIERTA y sólo la cierra un gate nuevo
             mediante lectura real. **APLICADA NO ES CERTIFICADA**: F4c sigue ABIERTA y F5
             sigue NO autorizada (2026-08-29)
last_meaningful_event_anterior: el GATE DEFINITIVO INDEPENDIENTE —J y K en paralelo, adjudicados
             por L con contexto limpio— devuelve INSUFICIENTE PARA F5 sobre r4=0ea0451, por
             SEIS razones independientes. NINGÚN hallazgo se corrigió en esa pasada, y eso
             INCLUYÓ los que caen sobre este mismo fichero: K-01, J-10 y L-01 señalaban
             recuentos y bloques caducados aquí dentro, y se dejaron INTACTOS a propósito —
             corregirlos durante el gate sería volver a que quien recibe sea quien aplica
             (2026-08-29)
last_meaningful_event_anterior: se publican DOS snapshots —r2@1b588ac, con la tanda y el arreglo de
             N158g; y r3@65cab54, con la batería ya PORTABLE, G-23 comprobando la excepción
             exacta en vez de afirmar «kernel intacto», y G-24 leyendo de verdad—. El árbol
             VIGENTE es posterior a ambos, y su SHA se deriva de Git, no se escribe aquí.
             Validación con Python 3.11.16, confirmada de forma independiente: 13/13, 57/57,
             67 detectadas y 0 NO detectadas, T158 SUPERADA y T161 = 293 (2026-08-29)
last_meaningful_event_anterior: la SEGUNDA revisión independiente devuelve F4 con veredicto de
             INSUFICIENCIA —dos BLOQUEANTES, siete GRAVES y catorce hallazgos nuevos— y sus
             correcciones quedan aplicadas (2026-08-27)
procedencia_de_la_critica: los hallazgos y el veredicto de las críticas de F3 y de las DOS
             de F4 los EMITIÓ un revisor independiente que no las escribió. La SEGUNDA de F4
             la emitió además un revisor que TAMPOCO aplicó la primera. Los ficheros que los
             recogen los TRANSCRIBIÓ Y APLICÓ el autor material de esas fases. Aplicar una
             crítica NO equivale a autocertificarse, y NO prueba que esté bien resuelta.
             LA PRUEBA DE QUE ESTO IMPORTA: dos de los hallazgos de la segunda devolución son
             defectos que la PRIMERA CORRECCIÓN introdujo o no vio
cerrado_en_el_NIVEL_0_DEL_GATE:
  # NO es una corrección: es la COBERTURA que faltaba. Tres agentes con contexto limpio —D y E
  # en paralelo, F adjudicando— leen las DIECINUEVE fuentes obligatorias que nadie abrió.
  # NINGÚN hallazgo corregido, retirado ni rebajado. NINGUNA severidad movida.
  · COBERTURA · requisito 0.1 SATISFECHO. Diecinueve fuentes, 8 310 líneas, leídas ÍNTEGRAS
    por dos revisores independientes, con cita de su primera y última sección sustantiva y con
    `C5-HANDOFF.md` leído ANTES de pronunciarse sobre B-2. Se cubrieron DIECINUEVE porque el
    requisito dice «dieciocho» y su propia enumeración lista diecinueve. De todas las citas
    que F abrió, UNA SOLA no estaba donde su dictamen la ponía, y su hallazgo sobrevive con la
    referencia corregida
  · LA PREGUNTA DEL GATE, CONTESTADA EN NEGATIVO · **`C5` NO RESUELVE `B-2`**, y la razón es
    ESTRUCTURAL, no accidental: el sujeto de un handoff son DOS CAPACIDADES —`handoff.yaml`
    no admite proceso ni fase—, y SIETE de las diecisiete instancias anclan su `cuando` al
    criterio `C-<CAP>` que el proceso debe declarar. El handoff se dispara PORQUE la capacidad
    ya está en la ruta; no es lo que la mete. La sospecha de C —«nadie miró ahí»— queda
    cerrada y NO debe reabrirse
  · Y AGRAVA `B-2` EN VEZ DE ALIVIARLO · `SIS` y `PLT` —el propietario global y el ejecutor de
    tres de los cuatro macrocircuitos— NO aparecen en ninguna de las diecisiete instancias, ni
    siquiera dentro de la ruta que proceso:SIS sí declara: existe `con-a-ver`, no existe
    `sis-a-con`. Y F corrige a C: el matiz sobre `SEG` NO se sostiene —sólo entra por C-SEG o
    por item DEP, y en proceso:SIS no ocurre ninguna—, luego el hueco cubre CINCO capacidades
    y no cuatro: ENC, PRD, ARQ, DIS y SEG. La única salida plausible es DOM
  · LA DISCREPANCIA MATERIAL, RESUELTA · D abrió `00-CIRCUITOS.md` —fuera de las diecinueve, y
    lo declaró porque REFUTA SU PROPIO HALLAZGO— y encontró que dice que un par sin handoff
    declarado «no está prohibido», contra el «Todo handoff se declara» de C5 L36. F resuelve A
    FAVOR DE D con tres pruebas convergentes: C5 se autolimita dos líneas después («define la
    forma, no las instancias»); el MAPA DE FUENTE ÚNICA del kernel asigna «entregas entre
    capacidades» a circuitos/; y NINGÚN validador comprueba cobertura. Consecuencia: la
    ausencia de instancias NO es defecto de conformidad. F declara que éste es el punto más
    débil de su adjudicación: no hay regla escrita de precedencia entre contratos/ y el mapa
  · DOCE HALLAZGOS NUEVOS · F-01 a F-12, tras fundir tres duplicados, reformular dos a la baja
    y rechazar una extensión. CUATRO medios y OCHO menores. Ninguno bloqueante, ninguno grave.
    Uno es defecto de F4 (F-03), tres preexistentes del kernel, uno propagado por F4, uno
    presión normativa, uno implementación ausente y cuatro editoriales
  · EL RECUENTO, FIJADO CONTANDO IDENTIFICADORES · son **32 hallazgos adjudicados** —4
    bloqueantes, 6 graves, **16** medios, 6 menores—, **31 distintos** tras la unificación
    A11≡M-8. **La cifra de 29 es ERRÓNEA**: C contó A5 y A13 como si estuvieran DENTRO de
    trece, cuando SE SUMAN a catorce. Con los doce nuevos: **44 abiertos, 43 distintos**
  · SEIS HALLAZGOS CAMBIAN DE ALCANCE, NINGUNO DE SEVERIDAD · B-1, B-2, G-4, M-5, M-6 y M-9.
    Y dos ganan prueba independiente: G-1 en `handoffs-generales.md` L107 —«siempre en items
    DEP antes de construir»— y G-2 en la ausencia del único camino de entrada a VER
  · TRES HALLAZGOS PROTEGIDOS CONTRA UNA SALIDA FALSA · G-1, M-3 y M-4 NO pueden cerrarse
    invocando autoridad del Owner: la norma APROBADA no menciona la actualización de ADS
    instalado —grep vacío sobre 3 343 líneas—, y eso vive sólo en el documento de IDEAS
    PENDIENTES, que dice de sí mismo que no autoriza a implementar
  · DÓNDE ESTÁ EL TRABAJO, CORREGIDO · el remedio de B-2 **no está en §8 en absoluto**: toca
    `01-PROCESOS.md` (los condicionales), `esquemas/proceso.yaml` (el vocabulario del campo) y
    `circuitos/` (el checkpoint que falta). «§18 hace parecer que el trabajo está donde no
    está», y quien empiece por ahí perderá la tanda
  · NIVEL 0 CERRADO, LAGUNA DE CORPUS NO · son dos cosas distintas y el doc 16 las mezcló.
    Siguen sin abrir: packs/ más allá de cabeceras (24 ficheros), quince de los diecinueve
    esquemas, C4/C6/C7 completos, (a)/(b)/E1/E2 completos, los roles y métodos de las quince
    capacidades, los validadores línea a línea, test_workspace.py, y §11 y §14
  · LA TANDA DE CORRECCIÓN NO EXIGE NINGUNA DECISIÓN NUEVA DEL OWNER PARA EMPEZAR. Sólo tres
    puntos abrirían consulta, y los tres son ELECTIVOS: G-3 si se elige reinterpretar O12,
    F-09 si se elige elevar a norma un principio que el Owner declaró provisional, y m-3 si
    alguien quisiera convertir en defecto lo que se dejó declarado como juicio no asumido
devuelto_por_el_GATE_FINAL_INDEPENDIENTE:
  # NO es una lista de resueltos: es lo que el gate DEVUELVE SIN RESOLVER. Tres agentes con
  # contexto limpio —A, B y C—, ninguno autor de F4. VEREDICTO: INSUFICIENTE PARA F5.
  # NINGÚN hallazgo se ha corregido en la pasada que lo registra.
  · COBERTURA · el encargo exige que entre A y B se cubra ÍNTEGRO el corpus obligatorio de
    121 ficheros. NO se cubrió: DIECIOCHO fuentes obligatorias quedaron sin abrir por ninguno
    —los dos ficheros de handoffs, los SEIS de diseno/, CUATRO de los siete contratos
    transversales (C1, C2, C3, C5), los DOS de docs/owner/ y CUATRO de entrada/—. **Basta
    para bloquear por sí solo**, y el riesgo no es formal: C5-HANDOFF.md es donde podría
    vivir el vehículo que el bloqueante B-2 no encontró, y nadie miró ahí
  · BLOQUEANTES CONFIRMADOS · CUATRO:
      A1  el contrato de `evento` en §3.6 NO puede representar el `deriva` que hace emitible
          `abandonada`: TRES sedes declaran el enum de `causa` y DOS son incompatibles. Un
          esquema derivado de §3.6 rechaza el único registro que hace emitible el segundo
          terminal, y con él la corrección entera de D64
      A2  el predicado «transacción abierta» sigue siendo «sin `derivada`» en §2.9 y §7.4.
          Una transacción cerrada por `abandonada` no tiene `derivada`, luego §2.9 RECONSTRUYE
          su marcador y el control repo deja de commitear para todo el producto,
          indefinidamente. Es el modo de fallo de B1, reinstaurado
      B-1 §8.2 y §18 asignan procesos INCOMPATIBLES a las mismas fases de la adopción: §8.2
          apoya DOM, SEG y DIS/Reconstruccion en los condicionales de proceso:AUD, y §18
          asigna proceso:INV, cuyos condicionales son otros. Y ambas tablas listan AUD y DEU
          como capacidades, que la nota al pie de §18 prohíbe expresamente
      B-2 los participantes declarados de los cuatro macrocircuitos NO tienen vehículo en los
          condicionales del proceso que D67 les asigna. Es el hueco que D67 existía para
          cerrar, y F6 tendría que tomar la decisión arquitectónica que D67 dice haber tomado
  · GRAVES CONFIRMADOS · SEIS: A3 (§7.4 declara retirado el ramal de reversión que D69
    exige) · A4 (D64–D68 y la tercera revisión NO constan en §15.8 ni en la cabecera) ·
    G-1 (U5b sin SEG ni CON: obligación con autoridad_de_retirada «nadie», y U6 es
    inalcanzable) · G-2 (A8 y M6–M7 con propietario ARQ ausente de participantes, y sin CON) ·
    G-3 (N7 = O12 sin producir dos de sus tres términos) · G-4 (las doce áreas documentales
    sin identificador declarado, y el único ejemplo usa la mitad que D68 retira)
  · MEDIOS CONFIRMADOS · TRECE, incluidos A5 y A13 que C RECLASIFICÓ desde otra severidad
  · MENORES · SEIS, uno con su inferencia rechazada y uno declarado juicio y no defecto
  · LO QUE C RECHAZÓ · piezas de CINCO hallazgos: la inferencia de m-4, la mecánica concreta
    de M-7, una generalización de B-2 —DOM y SEG sí tienen vía de consulta abierta—, una
    referencia de línea de A9, y m-3 como defecto. Y declaró que A14 NO es defecto de F4:
    es el entorno con Python 3.10 contra un tooling que exige 3.11
  · UN DEFECTO QUE NINGÚN REVISOR VIO, confirmado por C: §2.6.9 L1458 sigue afirmando
    «ninguna de las dos rutas revierte nada», tercera sede que contradice a D69
  · SIN DISCREPANCIAS MATERIALES IRRESOLUBLES entre A y B: todas las aparentes se resolvieron
    demostrando que miraban sedes distintas. Esa cláusula del encargo NO se disparó
  · EL DIAGNÓSTICO DE C · el patrón es uno solo y alcanza a los dos ejes: decisiones bien
    tomadas y APLICADAS A LA MITAD DE LOS SITIOS QUE LAS INVOCAN. D67 asignó procesos sin
    comprobar sus condicionales; D68 corrigió el recuento obligatorio y reprodujo el fallo en
    el condicional. **Ninguno de los diez hallazgos de nivel 1 y 2 exige una decisión
    arquitectónica nueva del Owner**: todos se cierran propagando decisiones ya tomadas bien
    en otra sede
  · CONDICIÓN PARA F5 · C la deja en CINCO niveles, del 0 al 4, hallazgo a hallazgo, en la
    sección 10 del documento 16. Nivel 0: cubrir las dieciocho fuentes, con C5-HANDOFF.md
    ANTES de cerrar B-2
corregido_en_la_CORRECCION_PREVIA_AL_GATE:
  # Comprobación adversarial de SÓLO LECTURA sobre la tanda anterior, y su corrección. Sus
  # SEIS defectos eran TODOS propios de esa tanda: ninguno estaba en el juicio de la tercera
  # revisión. Es la novena vez que la corrección introduce el defecto siguiente.
  · 1 · D69 · ESTADO ESTABLE frente a ESPECULATIVO. Estable es el último commit aceptado de
    la rama canónica: verdad publicable y NUNCA con una transacción parcialmente aplicada.
    Especulativo son las escrituras posteriores a `preparada`: NADIE LAS HA VISTO, no entran
    en ningún commit ordinario, y revertirlas no destruye trabajo de nadie. Arrancar exige
    worktree limpio, HEAD conocido, sin solape, INTENCIÓN CAUSAL PUBLICADA, revisión base,
    hashes previos y capacidad comprobada de restaurar
  · 2 · D69 · `abandonada` ES REVERSIÓN LOCAL VERIFICADA, no «cerrar dejando lo aplicado».
    Inalcanzable hasta CAPTURAR la divergencia, DETENER, RESTAURAR todos los canónicos a la
    revisión base —incluidos los que ya alcanzaron su posterior—, VERIFICAR byte a byte, y
    sólo entonces CERRAR. El commit lleva LA BASE CONSISTENTE MÁS EL INCIDENTE y NINGÚN
    `hash_posterior_esperado`. Si no se puede preservar o verificar, la transacción PERMANECE
    ABIERTA y no se publica nada. Con esto `abandonada` es la rama REVERTIR de b.14, y no hay
    tercer desenlace. «Roll-forward only» deja de ser absoluto: lo PUBLICADO nunca se revierte
    automáticamente; lo ESPECULATIVO sí, y su contenido anterior está en la revisión base
  · 3 · D70 · RECUPERACIÓN EN TRES NIVELES, y se retira la promesa de reanudación
    distribuida: A misma máquina y disco → EXACTA · B otra máquina con la tx CERRADA Y
    PUBLICADA → completa desde Git, incidente incluido · C otra máquina con la tx ABIERTA →
    NO HAY reanudación exacta: se REINICIA desde la intención publicada, y se pierde lo que
    sólo existiera en la máquina perdida. Limitación declarada y NO presentada como capacidad
    de PesquerApp
  · 4 · D69 · LA COPIA DIVERGENTE sólo existe localmente mientras la tx está abierta; se
    preserva ANTES de restaurar; el commit del incidente debe incluirla o incluir un
    artefacto durable autorizado; y si SEG bloquea su publicación, la tx NO puede declararse
    abandonada hasta que exista forma autorizada de preservar lo necesario
  · 5 · D70 · PARALELISMO ACOTADO: un único ejecutor por clon/worktree, ninguna segunda
    transacción canónica concurrente, otras máquinas serializadas por CAS Git, y el
    paralelismo por varios worktrees declarado CAPACIDAD FUTURA
  · 6 · D70 · R1 NO DESCARTA EL WORKTREE TRANSACCIONAL. R1 exige ficheros de texto legibles
    sin informe intermedio, no que estén en el worktree principal. Se descarta por COSTE Y
    DUPLICACIÓN de mecanismos, y la comparación gana cuarentena y reinicio desde intención
  · PN-7 REFORMULADA: b.14 tiene sólo COMPLETAR o REVERTIR, y `abandonada` es la segunda
  · PN-11 GANA SEDE por O16: autoridad en (g), contrato derivado C8 en F6, C7 intacto
  · RECUENTO CORREGIDO: DIEZ presiones vigentes. El corpus decía 8, 10 y 11 a la vez
  · D69, D70 y O16 registradas. D16–D68 y O1–O15 conservan su texto. O15 INTACTA
corregido_en_la_TANDA_INTEGRADA:
  # Corrección CONJUNTA de los hallazgos reproducibles de la tercera revisión. Los 22 se
  # reprodujeron mecánicamente contra el corpus vigente ANTES de tocar nada. El juicio, en
  # 15-TERCERA-REVISION-INDEPENDIENTE-F4C.md, NO se modifica: es histórico e inmutable.
  · B1 + G2 + M5 · D64 · LA RUTA DE CONFLICTO SE COLAPSA. No se le añade una salida a un
    mecanismo desproporcionado: se retira el mecanismo y se conserva la capacidad. Se van
    `reconciliacion-preparada`, `reconciliada`, los contadores `intento` e
    `intentos_consumidos`, la bandera `agotado` y las nueve ventanas R1–R9. Quedan CINCO
    fases, SEIS transiciones y DOS terminales, y TODO terminal retira el marcador.
    `conflicto` tiene DOS salidas: la divergencia cesa y se completa, o la autoridad emite
    `abandonada`, que cierra sin completar y emite un `deriva` que conserva el bloqueo
    ACOTADO a los items nombrados. La reparación es una transacción NUEVA que al cerrar lo
    resuelve. Comparación de proporcionalidad hecha garantía a garantía: NO se pierde
    ninguna. Los TRES mecanismos de reintento quedan separados —CAS del canal de órdenes de
    a.9, recuperación multiarchivo sin contador, resolución de divergencia externa sin
    tope—, y ninguno reutiliza el contador de otro. Contención declarada: alcance,
    solapamiento por intersección de rutas, checkpoint publicable y reanudación desde otra
    máquina. Siete secuencias completas, y ningún estado alcanzable sin salida
  · B2 + M1 · D65 · GOBIERNO GIT DEL CONTROL REPO, escrito. Tabla de propiedad completa;
    `main` es la rama canónica y NO recibe G29 —E2.4 la conserva por source—; PR y merge no
    se usan para el estado; la unidad de aislamiento es la transacción y no la rama;
    publicación por actualización optimista contra la revisión conocida, con rechazo
    non-fast-forward a `fallo`; `--force` prohibido salvo procedimiento extraordinario del
    Owner. Cuatro alternativas comparadas y elegida la mínima: DIARIO para recuperar, GIT
    para publicar, sin dos mecanismos para el mismo estado. La «política de publicación»
    pasa a ser `adaptador.publicacion_control_repo`, y NINGUNA política autoriza publicar
    una recuperación. Registrada PN-11: la sede normativa no existe, y C7 NO se toca
  · G1 + G3 · D66 · Los cinco conceptos de a.9 se citan como a.9 los escribe, y CONCEPTO no
    es CAMPO: cuatro son campos, el PROPIETARIO DEL CAMPO se DERIVA de §1.3, y
    `actor_atribuido` se conserva declarado aparte con su motivo. `fallo` recibe semántica
    CERRADA, con enum de operación y `tx_afectada` como REFERENCIA: X15 y X28 vuelven a ser
    satisfacibles
  · G4 + G5 + G6 + G7 · D67 · Los cuatro macrocircuitos, mapeados a b.16 con el propietario
    global QUE b.16 FIJA, sin crear ningún proceso. §8.3 gana LEE, ESCRIBE, autoridad,
    ejecutor y el gobierno de su retirada destructiva con cuatro condiciones. §8.4 gana
    ESTADO, con la instantánea de U3 declarada durable y versionada. N0 crea el item real
    SIS-001
  · G8 · D68 · Las doce áreas se alinean LITERALMENTE con §5.18: se restituye «mapa
    documental» y «arquitectura» vuelve a ser UNA. Taxonomía en tres clases. Registrada
    PN-12: el área 1 se satisface DERIVADA, con la misma vara de PN-6 y PN-10
  · M2 · M3 · M4 · corregidos. m1 a m7 · corregidos, incluidas las DOS frases vigentes que
    volvían a prometer append-only físico absoluto contra D63
  · CONTRASTE con las fuentes que la revisión no leyó íntegras: detectó un defecto PROPIO de
    esta tanda —el propietario global de A8, M6, N6 y A9 estaba elegido y no derivado de
    b.16— y quedó corregido en su commit
  · DIEZ presiones normativas vigentes. Ninguna renumerada. **Corregido**: el titular decía
    ONCE sobre una lista de DIEZ filas — PN-1, PN-2, PN-3, PN-6, PN-7, PN-8, PN-9, PN-10,
    PN-11 y PN-12—, con PN-4 retirada y PN-5 fusionada en PN-3
  · D64–D68 registradas. D16–D63 y O1–O15 conservan su texto. O15 INTACTA
devuelto_por_la_TERCERA_REVISION_INDEPENDIENTE:
  # Lo que la revisión independiente DEVOLVIÓ. Se conserva como registro de lo que encontró.
  # Emitida por un revisor con contexto limpio sobre df05929. VEREDICTO: INSUFICIENTE PARA F5.
  # NINGÚN hallazgo se ha corregido en la pasada que la registra.
  · B1 · BLOQUEANTE. EL CONFLICTO AGOTADO ES UN INTERBLOQUEO TERMINAL SIN SALIDA. Desde
    `conflicto(observacion: 4, agotado: true)` no existe ninguna transición admisible: no hay
    `reconciliacion-preparada` —predecesora prohibida—, no hay `derivada` —predecesoras
    `confirmada`/`reconciliada`, ambas 0 en esa ruta—, `abortada` está retirada, `deriva` no
    aplica y una transacción nueva la bloquea el marcador. Y como ninguna fase salvo
    `derivada` retira el marcador, el control repo NO VUELVE A COMMITEAR NUNCA, para todo el
    producto, por un solo conflicto agotado sobre un solo fichero
  · B2 · BLOQUEANTE. EL GOBIERNO GIT DEL CONTROL REPO NO EXISTE, y F4 lo rellena por
    inferencia sobre una regla que `E2.4` acota expresamente a las FUENTES. No se declara qué
    rama recibe las escrituras del runtime, con `main` protegida
  · G1 · GRAVE. «Los cinco conceptos de a.9» están MAL CITADOS, y son la lista de campos
    obligatoria de todo evento
  · G2 · GRAVE, de PROPORCIONALIDAD. Dos mecanismos para el mismo estado de disco: la ruta de
    reconciliación puede ser complejidad no justificada —tres fases, dos contadores, una
    bandera, nueve ventanas y cinco filas adversariales—. La carga de la prueba es de F4
  · G3 · GRAVE. El contrato de `fallo` no puede representar lo que cuatro pasajes normativos
    y dos pruebas le exigen
  · G4 · GRAVE. §8.3 migración no declara qué LEE ni qué ESCRIBE, y su único paso destructivo
    escribe en las fuentes sin gobierno
  · G5 · GRAVE. §8.4 actualización no declara su ESTADO persistido
  · G6 · GRAVE. Tres de los cuatro macrocircuitos no dicen a qué proceso de `b.16` pertenecen
    sus items
  · G7 · GRAVE. `N0` crea un paquete que pertenece a una iniciativa, y §3.3.0 acaba de
    declarar que eso no existe
  · G8 · GRAVE. Las doce áreas de §4.3 NO son las doce del §5.18 que `O8` resuelve
  · M1–M5 · MEDIOS. Sede normativa invocada y no definida · referencias colgantes a `X32`–
    `X34` y `X42` · §15.7 declara `C6` REUTILIZADO mientras §6.7 le añade una excepción ·
    retirar un adaptador borra ficheros en repositorios ajenos sin gobierno · el tope de
    reintentos invoca el precedente de `a.9` invirtiendo su cláusula de terminación
  · m1–m7 · MENORES. El más importante: DOS FRASES VIGENTES vuelven a prometer el append-only
    físico absoluto que `D63` retira
  · NO REPRODUCIDOS · quince, y el revisor los registra con su motivo: cardinalidades,
    cuarto intento, transiciones desde `derivada`, exclusión `confirmada`/`reconciliada`,
    cobertura de ventanas, tabla adversarial, partición de la matriz, `Q0`–`Q9` total y
    disjunta, promesas vivas sobre la lápida, contrato de identidad, `P-08`, los ONCE puntos
    de la adopción, `O13`, los dos relojes documentales, y todos los recuentos del árbol
  · LAS OCHO PRESIONES NORMATIVAS DE ENTONCES quedan CONFIRMADAS como bien identificadas
    —hoy son DIEZ, con PN-11 y PN-12—, con fuente y
    contradicción verificadas una a una. FALTA UNA: la de `G8` sobre `O8`. Y hay una
    candidata que depende de cómo se resuelva `B2`
  · O15 VERIFICADA FIEL: los seis puntos del Owner están literales, incluido que NO autoriza
    iniciar la adopción. Pero el revisor concluye que PesquerApp NO PUEDE recibir hoy una
    adopción permanente y completa, por `B2`, `B1`, `G7`, `G6` y `G4`
resuelto_en_la_SEXTA_COMPROBACION_TECNICA:
  # Comprobación ACOTADA sobre la semántica de sellado y retirada de cuerpo. NO es la tercera
  # revisión independiente, y NO certifica F4c. SÉPTIMO encadenamiento consecutivo.
  · 1 · CONTRADICCIÓN DE IDENTIDAD. El contrato decía `id = EV-H(evento MENOS id)` Y que la
    lápida conserva el mismo `id`. Consecuencia no escrita: tras retirar, el `id` YA NO puede
    recalcularse desde el fichero, la identidad por contenido deja de ser verificable por la
    regla ordinaria, y conservar id + huella NO equivale a conservar el contenido. Se TIPA la
    excepción: A evento íntegro → se recalcula y debe coincidir · B lápida → NO se recalcula,
    se valida su estructura y su vínculo con el sellado (id_original, hash_cuerpo_original,
    fase, tx, posición); con el cuerpo original delante se recalculan huella e identidad y
    deben coincidir; SIN él no hay verificación completa de la preimagen
  · 2 · TRES NIVELES DE GARANTÍA, antes mezclados:
      NIVEL 1 CONTINUIDAD ESTRUCTURAL   ids y `predecesor` permiten recorrer el orden. NO
                                        verifica el contenido retirado
      NIVEL 2 CONSISTENCIA DEL          sellado y lápida llevan el MISMO compromiso, y se
              COMPROMISO                demuestra que el repositorio lo conservó y registró
                                        la retirada. Una huella aislada NO demuestra cuál era
                                        el contenido ni que se poseyera
      NIVEL 3 VERIFICACIÓN COMPLETA     EXIGE el cuerpo original. Se recalculan cuerpo, huella
                                        e identidad. El cuerpo viene de una revisión Git
                                        exacta o de un archivo externo autorizado
    RETIRADAS las cuatro afirmaciones que prometían de más: «la huella demuestra que el cuerpo
    existió» · «demuestra cuál era» · «se recompone la cadena» cuando sólo se comprueban
    referencias · «sigue siendo verificable» sin decir que hace falta el cuerpo
  · 3 · FUENTE DE RECUPERACIÓN EXIGIDA ANTES DE RETIRAR: evento y sellado confirmados en una
    revisión Git durable o archivo externo autorizado · la lápida lleva LOCALIZADOR
    verificable —revision, ruta o blob, hash_esperado—, no sólo una huella · se ha COMPROBADO
    que el cuerpo se recupera de ahí · la evidencia queda registrada. Si la fuente
    desaparece: niveles 1 y 2 siguen, el 3 NO, y el sistema REFLEJA la degradación. NO se
    afirma que Git conserve eternamente: se declara la dependencia de retención de historia
    o de archivo externo
  · 4 · APPEND-ONLY, DICHO CON PRECISIÓN. Sustituir un cuerpo SÍ edita físicamente un fichero
    existente, luego el diario FÍSICO no es estrictamente append-only. Regla real: eventos y
    cabeceras lógicas INMUTABLES · se añaden eventos nuevos · UNA única mutación física
    autorizada y transaccional, la lápida · cualquier otra prohibida. Se retira «sustituir no
    es editar». Y el efecto real: reduce el CORPUS y el CONTEXTO del checkout, NO elimina el
    cuerpo de la historia Git ni reduce necesariamente el tamaño del repositorio. Liberar
    objetos históricos sería otra operación, con otro gobierno, y NO queda autorizada
  · 5 · LA RETIRADA VUELVE A SER ALCANZABLE. «No puede retirarse un evento al que apunte
    cualquier evento VIVO» la hacía imposible: cada evento apunta al anterior por
    `predecesor`. Se distingue REFERENCIA ESTRUCTURAL —nombra el id, y el id se conserva: NO
    bloquea— de DEPENDENCIA SEMÁNTICA VIVA —necesita LEER el cuerpo: SÍ bloquea—. En la duda,
    bloquea. El SELLADO actúa de ancla y checkpoint: conserva id, fase, tx, posición, huella
    y la cabeza de la cadena, y con eso el recorrido estructural no toca ningún cuerpo
  · 6 · `retirada-de-cuerpo` DETALLADA en once puntos, sin crear un segundo evento que
    duplique su `confirmada`: fichero que modifica · contenido exacto de la lápida ·
    identidad original conservada · localizador · relación con el sellado · hash_previo del
    evento íntegro · hash_posterior_esperado de la lápida · prueba de recuperación PREVIA ·
    autoridad y motivo · registro por las fases de su propia transacción · y por qué esas
    fases no abren recursivamente otra transacción
  · X-A a X-H añadidas como comprobaciones de la retirada. NO son filas de la tabla
    adversarial, que SIGUE en 42 filas y 42 ids `X<nn>`
  · SIN CAMBIO: `sellado` no transaccional y direccionado por contenido · `retirada-de-cuerpo`
    transaccional · matriz 9 tipos / 6 fases / 40 válidas / 23 prohibidas · cardinalidades y
    contadores de conflicto · ninguna transición nueva · §3.8 · O15 INTACTA
  · Corregido además el cierre Markdown defectuoso junto a la excepción en §3.6
  · D63 registrada
resuelto_en_la_QUINTA_COMPROBACION_TECNICA:
  # Comprobación de UN SOLO PUNTO sobre D60. NO es la tercera revisión independiente, y NO
  # certifica F4c. Su hallazgo está en texto que la comprobación ANTERIOR escribió: SEXTO
  # encadenamiento consecutivo.
  · UN CAMPO NUMERABA DOS COSAS. `iteracion` contaba a la vez observaciones e intentos, y de
    ahí salieron seis afirmaciones incompatibles: empieza en 1 · la comparten conflicto(i) y
    rec-prep(i) · incrementa al abrir conflicto · el máximo es 3 · la ruta agotada acaba en
    conflicto(4) · y ese cuarto «no es una cuarta iteración». Un campo que vale 4 bajo un
    máximo de 3 son DOS contadores con un solo nombre
  · VIGENTE, DOS CONCEPTOS Y DOS CONTADORES:
      OBSERVACIÓN DE CONFLICTO   cada divergencia REAL que debe quedar registrada
      INTENTO DE RECONCILIACIÓN  cada decisión durable que se intenta aplicar
    `conflicto`  → `observacion` 1..4 · `intentos_consumidos` 0..3, con
                   intentos_consumidos = observacion − 1 · `agotado: true` SÓLO en la cuarta,
                   y con él NO admite ninguna `reconciliacion-preparada`
    `rec-prep`   → `intento` 1..3 · `resuelve` = id del `conflicto` que atiende.
                   NUNCA existe un `intento: 4`
    MAX_CAS_RETRIES = 3 limita INTENTOS, NO OBSERVACIONES. La cuarta observación registra el
    FRACASO DEL TERCER INTENTO y no se silencia
  · SECUENCIA  C1(obs1,cons0) → RP1(int1) → C2(obs2,cons1) → RP2(int2) → C3(obs3,cons2) →
               RP3(int3) → C4(obs4,cons3,agotado) · NO EXISTE RP4
  · TOTALES SIN CAMBIO: normal 3 · conflicto exitoso 5, 7 o 9 · agotamiento 8
  · EL PREDICADO `reconciliacion_pendiente` NO cambia y sigue siendo VERDADERO al agotarse:
    agotar no resuelve nada. Lo que cambia es quién desbloquea — con agotado, SÓLO el Owner
  · `retirada-de-cuerpo` COMPROBADA como ÚNICA excepción autorizada a «un evento nunca se
    edita»: cabecera e identidad conservadas · hash original verificable en el sellado Y en la
    lápida · lápida con autoridad y motivo · cualquier otra edición prohibida. Y se dice lo
    que NO es cierto: el cuerpo original NO se recupera desde el sellado — el sellado guarda
    la HUELLA, no el cuerpo, y si lo guardara retirarlo no liberaría nada. Recuperarlo exige
    una fuente EXTERNA, la historia de Git mientras el commit sobreviva
  · O15 INTACTA. Sin tipos nuevos, §3.8 sin cambios
  · D62 registrada. Tabla adversarial: SIGUE en 42 filas — X58 se ajusta en su sitio
resuelto_en_la_CUARTA_COMPROBACION_TECNICA:
  # Comprobación ESTRICTAMENTE ACOTADA sobre D58–D59. NO es la tercera revisión independiente,
  # y NO certifica F4c. Sus DOS hallazgos están en texto que la comprobación ANTERIOR
  # escribió: QUINTO encadenamiento consecutivo.
  · 1 · CARDINALIDAD INSATISFACIBLE. Se decía «`preparada`, `confirmada`, `reconciliada` y
    `derivada` exactamente una vez por tx», y NINGUNA transacción real puede cumplirlo: la
    ruta normal no tiene `reconciliada`, la de conflicto no tiene `confirmada`, y una agotada
    no tiene `derivada`. Vigente, CONDICIONAL A LA RUTA:
      RUTA NORMAL CERRADA        preparada 1 · confirmada 1 · conflicto 0 · rec-prep 0 ·
                                 reconciliada 0 · derivada 1        → 3 eventos
      CONFLICTO CERRADA          preparada 1 · confirmada 0 · conflicto = rec-prep = k∈{1,2,3}
                                 reconciliada 1 · derivada 1        → 3+2k = 5, 7 o 9
      CONFLICTO AGOTADA/ABIERTA  preparada 1 · confirmada 0 · conflicto 4 · rec-prep 3 ·
                                 reconciliada 0 · derivada 0        → 8 eventos, marcador
                                 ABIERTO, bloqueada y escalada al Owner
    `confirmada` y `reconciliada` son MUTUAMENTE EXCLUYENTES. Invariante que distingue cierre
    de agotamiento: #conflicto = #rec-prep si cerró, #conflicto = #rec-prep + 1 si agotó
  · 2 · EL CONTADOR `iteracion`, CERRADO.
    [REVISADO por D62: era UN campo numerando DOS conceptos, y valía 4 bajo un máximo de 3.
     Se separa en `observacion` 1..4 sobre `conflicto` e `intento` 1..3 sobre
     `reconciliacion-preparada`. Ver el bloque de la quinta comprobación técnica]
    Empieza en 1 —nunca 0—; lo comparten `conflicto(i)`
    y su `reconciliacion-preparada(i)`; incrementa SÓLO al abrir un `conflicto` nuevo.
    MAX_ITERACIONES = 3: el TERCER `conflicto` SÍ recibe decisión. El CUARTO `conflicto` se
    emite —la clasificación de §2.6.4 lo produce y un hecho observado no se calla— y es el
    MARCADOR DE PARADA: sin decisión, escalado, transacción abierta. Máximos exactos: CUATRO
    `conflicto` y TRES `reconciliacion-preparada`. Alineados autómata, contrato, R9, X58 y
    validador semántico
  · 3 · LA FRONTERA DE RECURSIÓN ERA FALSA. Se decía a la vez que `sellado` sólo AÑADE, que la
    frontera es AÑADIR frente a MODIFICAR, y que `sellado` exige tx SIEMPRE: las tres no
    caben juntas. Vigente, UN solo criterio: una escritura canónica exige `tx` si y sólo si
    toca MÁS DE UN FICHERO o SUSTITUYE CONTENIDO PREVIO. No la exige la que sea UN SOLO
    FICHERO, NUEVO Y DIRECCIONADO POR SU CONTENIDO — ahí el nombre es la verificación
  · 4 · `sellado` PASA A NO TRANSACCIONAL. Comprobado contra §2.9: no edita ni borra eventos
    —retirar un cuerpo es acto SEPARADO—, no escribe índices —derivados— y no toca el item
    —cerrarlo es un `transicion`—. Añade UN fichero `SL-<huella>` que nunca se reemplaza.
    `retirada-de-cuerpo` SÍ es transaccional: sustituye el cuerpo por su lápida, que conserva
    id, fase, tx, huella, autoridad y motivo. Cero recursión POR EL CRITERIO GENERAL
  · 5 · MARCADO DE ÓRDENES, CLASIFICADO. Marcar `- [x]` o `- [!]` SÍ es una escritura durable
    que modifica físicamente el tablero; NO es mutación del estado canónico gobernada por la
    transacción general; se rige por el CAS propio de a.9 sobre hash de contenido con
    MAX_CAS_RETRIES = 3. Aplicar la orden al estado canónico SÍ usa tx y fases
  · 6 · RECUENTO RECALCULADO, no arrastrado. Regímenes: 5 SIEMPRE transaccionales
    (transicion · integracion · certificacion · migracion · retirada-de-cuerpo) · 1
    CONDICIONAL (orden) · 3 SIEMPRE NO transaccionales (sellado · deriva · fallo).
    9 tipos · 6 fases · 7 estados del campo · 40 válidas · 23 prohibidas · 63 de espacio
  · O15 INTACTA. §3.8 no cambia: `sellado` sigue siendo un valor del enum, cambia su régimen
  · D60–D61 registradas. Tabla adversarial: SIGUE en 42 filas — X58 corrige su escenario en
    su sitio para que coincida con su resultado
resuelto_en_la_TERCERA_COMPROBACION_TECNICA:
  # Comprobación técnica ACOTADA sobre D55–D57. NO es la tercera revisión independiente, y NO
  # certifica F4c. Sus DOS hallazgos están en texto que la corrección ANTERIOR escribió: es el
  # CUARTO encadenamiento consecutivo.
  · 1 · RECUENTO DE FASES MEZCLANDO EJES. Se decía «las ocho formas» y luego «7 × 6 + 2 = 44»,
    metiendo `deriva` y `fallo` —que son valores de `tipo`— en el eje `fase`. Vigente: NUEVE
    valores de `tipo` · SEIS fases transaccionales · SIETE estados del campo `fase` contando
    su AUSENCIA · 45 combinaciones válidas y 18 prohibidas sobre un espacio de 63
  · 2 · `confirmada → confirmada` NO EXISTE. La «reemisión» de D56 —un evento NUEVO con la
    misma fase— contradecía §2.8 punto 5, que ya declaraba NO-OPERACIÓN emitir una fase que ya
    existe. Vigente: CASO A, `confirmada` no durable → se emite UNA vez (W5, W13); CASO B, ya
    durable → se reaplican los canónicos desde `preparada` y NO se emite ninguna fase nueva,
    siguiendo con derivados y `derivada`. Restaurar un fichero de evento perdido es
    RESTAURACIÓN IDEMPOTENTE del MISMO evento —mismo id, cuerpo y predecesor—, no una emisión.
    `preparada`, `confirmada`, `reconciliada` y `derivada`: EXACTAMENTE UNA por tx. Sólo
    `conflicto` y `reconciliacion-preparada` son repetibles, con `iteracion` y tope de tres
    [REVISADO por D60: «las cuatro exactamente una vez» es INSATISFACIBLE. La cardinalidad es
     CONDICIONAL A LA RUTA, y `confirmada` y `reconciliada` son mutuamente excluyentes. Ver el
     bloque de la cuarta comprobación técnica]
  · 3 · MATRIZ MÍNIMA, DEMOSTRADA TIPO A TIPO. `orden` es CONDICIONAL: a.9 da consumos que NO
    aplican y NO modifican el estado canónico —base inexistente tras rebase, agotamiento de
    MAX_CAS_RETRIES—. Los otros SEIS son siempre transaccionales; `deriva` y `fallo`, nunca.
    Y se declara CERO RECURSIÓN: escribir los eventos del propio diario NO abre otra
    transacción — la frontera es AÑADIR frente a MODIFICAR, y por eso `sellado` y
    `retirada-de-cuerpo` sí la necesitan
    [REVISADO por D61: esa frontera era FALSA — con ella `sellado`, que sólo añade, NO
     exigiría la tx que aquí se le impone. La frontera real es UN FICHERO frente a VARIOS y
     NUEVO frente a SUSTITUIR CONTENIDO, y con ella `sellado` pasa a NO TRANSACCIONAL. El
     recuento 45 se recalcula a 40. Ver el bloque de la cuarta comprobación técnica]
  · O15 NO SE TOCA. Sólo se corrigen recuentos y referencias derivadas
  · D58–D59 registradas. Tabla adversarial: SIGUE en 42 filas — X21 gana la comprobación
    explícita de que no existe `confirmada → confirmada`, en su sitio
resuelto_en_la_SEGUNDA_CORRECCION_TECNICA:
  # Segunda corrección técnica sobre el protocolo transaccional. NO es la tercera revisión
  # independiente, y NO certifica F4c. Sus TRES hallazgos están en texto que la corrección
  # técnica ANTERIOR escribió: es el TERCER encadenamiento consecutivo.
  · H1 · GRAVE. GARANTÍAS ATRIBUIDAS A QUIEN NO PUEDE COMPROBARLAS. §3.6 declaraba cuatro
    reglas «que un esquema derivado debe hacer cumplir», y TRES son incomprobables por un
    esquema estructural: recorrer los demás eventos de un `tx`, contar iteraciones y observar
    el orden real de fsync y rename. Se separan TRES CAPAS con dueño — A esquema estructural
    del evento · B validador semántico del diario · C runtime y pruebas de caída — y cada
    regla queda asignada a la capa capaz de comprobarla. Es D55, y revisa D54
  · H2 · GRAVE. W12a CONTRADECÍA LA CLASIFICACIÓN POR HASHES. Mandaba `conflicto` ante un
    canónico revertido a su `hash_previo`, que es la caja NO APLICADO de §2.6.4 y lo que W3 y
    W4 completan hacia delante: el mismo disco recibía dos clasificaciones incompatibles, y
    la que ganaba escalaba a una persona un resultado DETERMINISTA. La clasificación pasa a
    hacerse contra la ÚLTIMA FASE DURABLE —`preparada`, o `reconciliacion-preparada` para las
    rutas que reconcilió—, con base válida y resultado permitido explícitos. Un canónico
    revertido bajo transacción abierta SE REAPLICA; si `confirmada` era durable SE REEMITE
    tras reaplicar, y reemitir una fase NO es una transición.
    [REVISADO por D58: NO se reemite. El evento `confirmada` ya existe, y §2.8 punto 5 ya
     declaraba NO-OPERACIÓN emitir una fase que ya está. `confirmada → confirmada` NO EXISTE] `conflicto` exige transacción
    abierta Y divergencia real; el marcador huérfano o clonado es `fallo` de publicación, y
    lo divergente sin transacción es `deriva`. Es D56
  · H3 · GRAVE. SIETE TIPOS SIN CONTRATO. El enum de `tipo` tiene NUEVE valores y el contrato
    condicional cubría sólo el eje `fase`; «las ocho formas de evento» contaba filas del eje
    equivocado. Se declara la matriz: los SIETE tipos que escriben estado canónico llevan
    `fase` y `tx` OBLIGATORIOS y son ortogonales a las seis fases; `deriva` y `fallo` los
    tienen PROHIBIDOS. Cada tipo declara su sujeto. Formas válidas: 7 × 6 + 2 = 44. NO se crea
    ni se fusiona ningún tipo, y el recuento de §3.8 no cambia. Es D57
    [REVISADO por D59: `orden` es CONDICIONAL, no siempre transaccional, y el recuento se
     separa por ejes — 9 tipos · 6 fases · 7 estados del campo · 45 válidas · 18 prohibidas.
     El cartesiano 7 × 6 + 2 se retira: no estaba demostrado tipo a tipo]
  · C4 · RESTOS VIGENTES. `preparada` deja de ser «la única entrada que necesita la
    recuperación» —lo es en la ruta normal—; la cardinalidad de una transacción se declara
    VARIABLE (3 normal · 3+2k en conflicto · 6 si escala sin cerrar · más reemisiones);
    `conflicto` deja de decir que sólo avanza a `reconciliada`; y «absorbente» pasa a
    «ABIERTO Y BLOQUEANTE», con la definición de por qué no es absorbente. El término
    anterior se conserva en D35, en las devoluciones y en este checkpoint como HISTORIA
  · NO REPRODUCIDOS · dos restos señalados no existen en el árbol publicado, y se dice: `X28`
    aparece UNA vez —42 filas de datos y 42 ids únicos, y la fila 43 es el separador de
    Markdown— y «Un fichero que no existe» también aparece UNA vez
  · D55–D57 registradas, y O15. Tabla adversarial: SIGUE en 42 filas — X05, X15, X26 y X28
    se corrigen EN SU SITIO, sin añadir ni retirar ninguna
resuelto_en_la_CORRECCION_TECNICA_POSTERIOR:
  # Corrección técnica sobre el protocolo transaccional. NO es la tercera revisión
  # independiente, y NO certifica F4c. Sus tres hallazgos están en texto que las
  # correcciones ANTERIORES escribieron.
  · 1 · BLOQUEANTE. LA RECONCILIACIÓN NO ERA RECUPERABLE. `reconciliada` declaraba la
    decisión Y la daba por aplicada: una caída entre decidir y emitir dejaba el diario sin la
    decisión, sin su mecanismo y sin el resultado esperado — y el `preparada` original NO
    sirve de respaldo, porque la decisión puede ser «conservar lo divergente» o «un tercer
    contenido». Se añade `reconciliacion-preparada`, la intención durable ANTES de tocar
    nada, con siete campos. **SEIS fases, no cinco**: el número se recalcula, no es cuota.
    Nueve ventanas R1–R9 y tope de TRES iteraciones, con el precedente de MAX_CAS_RETRIES
  · 2 · BLOQUEANTE. TRANSICIÓN POSTERIOR AL TERMINAL. La integridad post-terminal emitía
    `conflicto` sobre una transacción con `derivada` durable, y ninguna transición sale del
    terminal. Se separa por IDENTIDAD: `conflicto` es fase de una transacción ABIERTA; lo
    descubierto tras el cierre es un evento `deriva`, sin fase y sin tx propio, que la
    REFERENCIA sin reabrirla. Reparar exige una transacción NUEVA con su intención durable, y
    nada se restaura desde Git automáticamente. W12 se parte en W12a y W12b
  · 3 · GRAVE. El tipo `evento` no representaba el protocolo narrado. Contrato CONDICIONAL
    por fase para las ocho formas de evento: obligatorios, prohibidos, predecesora admitida,
    hash que gobierna y condición para emitir la siguiente. Más cuatro reglas que un esquema
    derivado debe hacer cumplir. Y los `fsync` obligatorios se extienden a la ruta de conflicto
    [REVISADO por D57: «las ocho formas» no era el recuento de formas de evento — el enum de
     `tipo` tiene NUEVE valores y siete quedaban sin contrato. Y por D55: tres de las cuatro
     reglas NO las puede comprobar un esquema.
     REVISADO OTRA VEZ por D59: tampoco era «el eje FASE» — las fases son SEIS, y `deriva` y
     `fallo` son valores de `tipo`. Ver el bloque de la tercera comprobación técnica]
  · CONSISTENCIA · el marcador deja de llamarse «tercera categoría» en §2.6.6 · W11 deja de
    hablar de «su bandera» · X47 comprueba la PROYECCIÓN NORMATIVA VIGENTE y declara sus
    excepciones históricas una a una, en vez de afirmar que todo el corpus tiene una sola
    enumeración cuando conserva historia a propósito
  · D52–D54 registradas. Tabla adversarial 37 → 42 filas (X54–X58), más las nueve R1–R9
resuelto_en_la_DEVOLUCION_TECNICA_PREVIA:
  # Auditoría externa de Codex sobre el ÁRBOL REMOTO REAL (7ebdd8a). NO es un veredicto de
  # suficiencia: es revisión TÉCNICA. Tres de sus bloqueantes están en texto que las DOS
  # correcciones anteriores escribieron.
  · 1 · BLOQUEANTE. UN SOLO AUTÓMATA: dos rutas —normal
    `preparada→confirmada→derivada`, de conflicto con su ciclo propio— y `derivada` como
    ÚNICO cierre terminal, con tabla de transiciones admitidas. Había CINCO formulaciones
    incompatibles del mismo autómata. `abortada` rechazada por el esquema.
    [REVISADO por D52: el número de fases pasó de cinco a SEIS al hacer recuperable la
    reconciliación. Ver el bloque de la corrección técnica posterior]
  · 2 · BLOQUEANTE. `tx_abierta` RETIRADO de los canónicos: rompía el
    `hash_posterior_esperado` que la propia transacción declara, y exigía una segunda
    escritura multiarchivo que ningún paso describía. La detectabilidad no toca un byte
  · 3 · BLOQUEANTE. `reconciliacion_pendiente` pasa a PREDICADO DERIVADO. Antes exigía abrir
    una transacción para registrar el estado que impide abrir transacciones, contra su X08
  · 4 · `reconciliada` deja de ser terminal: aplica la decisión, declara hashes finales que
    SUSTITUYEN al esperado, y cierra por `derivada` tras regenerar los derivados
  · 5 · integridad post-terminal con ventana de commit definida, hash tras reconciliar,
    comparación real contra HEAD, y DERIVA NO TRANSACCIONAL que se reporta y NO se restaura
  · 6 · el marcador es OPERACIONAL con excepción de ruta declarada. Dos categorías, no tres
  · 7 · §3.6, §3.4, §5.6 y §9.2 alineados: `auditor` y `verificador_de_correccion`,
    `resolucion_del_control_repo` añadido de verdad, y la celda registra sólo desviación
  · 8 · §9.1 y §9.5 proyectan las CINCO pruebas de `nivel-certificacion:integrado`
  · 9 · DOS huellas y un artefacto que las contiene, no tres (D47 revisa D31)
  · 10 · reparto de dominio: certificación SÓLO en `nivel-certificacion`
  · 11 · restos editoriales; DOS de los cinco señalados NO se reproducen, y se dice
  · D46–D51 registradas. Tabla adversarial 30 → 37 filas (X47–X53)
resuelto_en_la_SEGUNDA_devolucion_de_f4:
  · E · BLOQUEANTE. `fsync` DE DIRECTORIO obligatorio también para los canónicos, y en el
    orden correcto: temporal → fsync(temporal) → rename → fsync(directorio). F4c lo exigía
    para los dos eventos y NO para los ficheros que SON el estado, cometiendo el error que su
    propia garantía 3 nombraba como «el error clásico». El fallo era SILENCIOSO: con
    `confirmada` durable nadie volvía a comparar hashes. Nace la COMPROBACIÓN DE INTEGRIDAD
    POST-TERMINAL, sin la cual todo lo demás depende de que la implementación no falle
  · B · BLOQUEANTE. `conflicto` deja de ser TERMINAL: es ABIERTO Y ABSORBENTE, emite la
    bandera que b.4 P0 consume, conserva copia íntegra de lo divergente, declara autoridad y
    alcance de bloqueo, y sólo lo cierra `fase: reconciliada`. VERIFICADO POR BARRIDO:
    `reconciliacion-pendiente` aparecía cuatro veces en el documento y NINGUNA dentro de §2,
    luego el protocolo nunca emitía el único estado del que depende b.4 P0
  · A · GRAVE. Regla de lectura para TODO lector, marcador CON CONTENIDO, y `tx_abierta` en
    la cabecera de cada canónico afectado. Lo que se garantiza es DETECTABILIDAD, no
    aislamiento, y R3 se cualifica en §2.2 en vez de decir «sí» a secas
  · C · GRAVE. Contrato de identidad completo: representación canónica independiente del
    formato, campos excluidos con `identidad_v`, `tx` e `id` definidos, regla de reintento.
    Y la consecuencia declarada: REEMITIR NO ES IDEMPOTENTE POR ID — la idempotencia vive en
    `tx`. La frase contraria se RETIRA
  · D · `abortada` se retira: era formalmente definida y OPERACIONALMENTE INALCANZABLE
  · F · el marcador se excluye de Git. F4c violaba su propio criterio de §2.4
  · H · GRAVE. Se REGISTRA el defecto de C7: su gate dice «una o más fuentes» y E2.6 dice
    «varias sources». Con el texto vigente NINGÚN producto de un repositorio cierra un solo
    item. NO es presión normativa: es defecto de DERIVADO con prescripción cerrada, y su
    ejecución es F6. C7 NO se edita en esta pasada. §15.7 deja de decir «REUTILIZADO»
  · I · GRAVE. El puntero: lista de componentes derivada de SOURCES.toml, resolución como
    campo del adaptador con normalización de remoto y cuarto desenlace, §6.4 gana la
    comprobación que §6.7 remitía y no existía, y TODA escritura de puntero pasa a ser source
    change gobernado por C7 — U5 se parte en U5a/U5b, y N2 y A5 dejan de escribir en fuentes
  · K · GRAVE. El push deja de ser automático: el commit local es recuperación, el push es
    PUBLICACIÓN. Y se DECLARA que el gobierno Git del control repo NO EXISTE en C7 ni en
    ninguna parte — §7.6 dejaba de ser cierta para las dos operaciones que automatizaba
  · N-1 · GRAVE. Nace `contrato-de-aspecto`: se invocaba TRES veces como sede normativa y no
    existía. Mismo modo de fallo que el manifiesto de transacción, reproducido y no
    detectado. Recuento 24 → 25
  · N-6 · GRAVE. Los predicados de obligación se definen a nivel de INICIATIVA: Q9 no era
    computable y ninguna iniciativa con obligaciones podía cerrar jamás
  · J · el documento gobernado tiene ciclo PROPIO de cuatro valores. Se deja de atribuir a
    b.3 un vocabulario que b.3 no contiene
  · G · la premisa del Owner queda REFUTADA por el revisor y se transcribe así. Los cinco
    residuos reales sí se corrigen, incluida la condición para reintentar M6
  · y N-2 · N-3 · N-4 · N-5 · N-7 · N-8 · N-9 · N-10 · N-11 · N-12 · N-13 · N-14
  · PN-7 a PN-10 registradas. Ocho presiones vigentes. Ninguna redactada
resuelto_en_la_PRIMERA_devolucion_de_f4:
  · A · EL PROTOCOLO TRANSACCIONAL, reescrito para ser EJECUTABLE. El manifiesto de
    transacción se pliega en `evento` como una `fase`: una transacción es una secuencia de
    eventos INMUTABLES con `tx` común, y ya no hay fichero que se reescriba ni que se borre.
    Hash POSTERIOR esperado por fichero — el dato que faltaba—, tres cajas de clasificación
    en recuperación, ONCE ventanas de caída, SEIS garantías de durabilidad separadas con sus
    tres puntos de `fsync` obligatorio, semántica completa del sellado, e ids DIRECCIONADOS
    POR CONTENIDO. Se RETIRA la afirmación falsa de que dos emisores concurrentes no
    colisionan jamás. Tabla adversarial de DIECISIETE filas, para convertirse en pruebas F6
  · B · `cobertura.dimension` se parte en `sujeto` · `aspecto` con namespace tipado ·
    `responsables` · `criterio`. Una capacidad deja de sustituir a las dimensiones de las
    que responde: accesibilidad y responsive de una pantalla ya son dos celdas. Rendimiento,
    resiliencia y cadena de suministro dejan de estar sin dueño, asignadas a capacidades que
    YA EXISTEN. Tres celdas completas sobre el mismo contrato
  · C · la matriz de fuentes de verdad, rehecha: prioridad y aparcado en `02-control.md`, la
    zona ÓRDENES como CANAL DE COMANDOS, y el tablero deja de declararse derivado entero
  · D · el estado de iniciativa pasa a FUNCIÓN TOTAL con precedencia Q0–Q9, con su totalidad
    demostrada sobre los diez estados de b.4. No se persiste en ningún canónico
  · E · `memoria` SE GENERALIZA, y se dice. `ultima_verificacion_real` queda en UNA sola
    fuente. `capa` pasa a condicional y nace `plano`, sin fabricar la cuarta capa
  · F · `adaptador.nivel` desaparece como campo: el nivel alcanzado es DERIVADO y caduca.
    §6.7 resuelve el descubrimiento con control repo y fuentes hermanos, sin copiar la
    organización ADS y sin depender de nada no versionado
  · G · migración con secuencia única M5 certifica · M6 retira · M7 verifica. Rollback con
    remoto separado de lo local y SIN eliminación remota automática. Certificación Integrada
    con aplicabilidad para 0, 1 y N fuentes. Actualización con compatibilidad y rollback DEL
    ESTADO, y punto de no retorno declarado en U3
  · H · P-08 con DOS huellas —semántica y de entorno— y clave de caché por CONTENIDO, nunca
    el SHA de Git. El artefacto de salida las CONTIENE; no es una tercera huella (D47). La
    raíz de confianza, declarada sin circularidad, y el suelo que queda abierto, dicho
  · I · D23–D33 registradas, cada una diciendo qué decisión anterior revisa. D16–D22
    CONSERVAN SU TEXTO. Tipos RECALCULADOS: cuatro de estado, uno de clase, y el manifiesto
    de transacción deja de serlo. Presiones revisadas: PN-4 retirada, PN-5 fusionada en
    PN-3, PN-6 nueva. CUATRO vigentes, sin renumerar ninguna
resuelto_en_la_entrega_de_f4:
  # HISTORIA. Es lo que F4 resolvió AL ENTREGARSE. Lo marcado [CORREGIDO] lo revisó la
  # devolución independiente, y su forma vigente está en el bloque de arriba.
  · LA PRIMERA DECISIÓN, que H2 ordenaba primero: DISPOSICIÓN FÍSICA DEL ESTADO.
    Ficheros canónicos + DIARIO DE EVENTOS append-only + derivados deterministas. SQLite
    canónico y event sourcing puro comparados y DESCARTADOS por romper «el estado ES los
    ficheros, legibles sin informe intermedio»; sólo ficheros, descartado por no cumplir
    la atomicidad que a.9 exige. SQLite queda como índice compilado NO canónico, en el
    plano operacional
    [CORREGIDO] la entrega contaba además un MANIFIESTO DE TRANSACCIÓN como pieza aparte.
    D23 lo pliega en `evento` como una `fase`
  · el diario ES el JOURNAL que a.11 dejó PENDIENTE. Cierra G26
  · DURABLE frente a OPERACIONAL: `estado/` versionado · `.ads/run/` no versionado y
    reconstruible. El criterio, en una pregunta: ¿sobrevive a un clon nuevo?
  · [CORREGIDO] la entrega decía «CUATRO TIPOS NUEVOS Y NI UNO MÁS», que era una CUOTA
    fijada antes de aplicar la prueba. El recuento se CALCULA: cuatro tipos de estado, un
    esquema de clase, y el manifiesto de transacción deja de ser tipo. §3.8
  · CI-1 aplicado: el sujeto auditable es referencia tipada (clase, ancla, ruta), con el
    componente de C6 como ANCLA. SOURCES.toml no se toca
  · CI-2 resuelto por COMPOSICIÓN: `memoria` gobierna, `cobertura` da vigencia
    [CORREGIDO] la composición era real y la generalización de `memoria` también, y sólo
    se contaba una. D27 sustituye a D20 y declara las dos. «Cero campos duplicados» no era
    cierto: `ultima_verificacion_real` estaba en los dos sitios, y ahora está en uno
  · CI-5 aplicado: cuatro macrocircuitos con disparador, fases, gates, rollback,
    reanudación y certificación PROPIOS. El motor es común; las rutas no se aplanan
    [CORREGIDO] dos de los cuatro declaraban secuencias imposibles. D32 y D33
  · CI-6 aplicado: adaptador en cuatro piezas — definición canónica, proyecciones donde
    cada proveedor las DESCUBRE, huella con validador de deriva, y prueba de humo
    [CORREGIDO] `adaptador.nivel` era una segunda verdad, y «donde cada proveedor las
    descubre» no resolvía el caso de control repo y fuentes hermanos. D28 y §6.7
  · P-08 con solución general diseñada: entradas declaradas por validador, huella de
    entradas en la evidencia, y las cuatro preguntas separadas — integridad, procedencia,
    éxito y VIGENCIA
    [CORREGIDO] la caché se claveaba por revisión de Git y era ciega al árbol sucio. D31
  · doce escenarios extremo a extremo recorridos. NINGUNO EJECUTADO
  · D16–D22 registradas con su alternativa descartada. D23–D33 las revisan sin
    reescribirlas
owner_captado: "Autoriza aplicar la crítica independiente de F4 y corregir su
             arquitectura. NO autoriza F5 ni F6" (2026-08-27)
             + RESOLUCIÓN POSTERIOR O15: "PesquerApp será la primera adopción REAL,
             PERMANENTE y completa de ADS; su repositorio global ADS nace como repositorio
             de control DEFINITIVO. NO autoriza iniciar la adopción" (2026-08-27)
             + RESOLUCIÓN POSTERIOR O16 (2026-08-29). Se le presentó esta formulación,
             REDACTADA POR EL SISTEMA: "El gobierno Git del repositorio global de control
             de ADS tendrá su autoridad normativa en la sección (g); F6 derivará de ella un
             contrato independiente C8; C7 seguirá gobernando únicamente los repositorios
             fuente del producto." Respuesta LITERAL del Owner: "ok, confirmamos".
             El párrafo largo NO es cita suya: lo literal es la confirmación, y lo que
             confirma es la formulación presentada. NO autoriza iniciar F5, no autoriza
             redactar (g) y no autoriza crear C8. Registrado por L-02, que demostró que O16
             era la ÚNICA de las dieciséis resoluciones sin fecha, sin cita y sin entrada
             aquí — y es la que da sede a PN-11, nacida del BLOQUEANTE B2
pregunta_pendiente: ninguna. Las TRECE presiones normativas vigentes —derivadas de las
             cabeceras `## \`PN-` de §16: QUINCE menos PN-4 RETIRADA y PN-5 FUSIONADA— son
             materia de F5, no preguntas. PN-15 es la que esta tanda añade, por K-06
siguiente:   OTRO GATE INDEPENDIENTE, con revisores de contexto limpio que NO sean quien
             aplicó esta tanda. La TANDA DE CORRECCIÓN DEL GATE DEFINITIVO está APLICADA,
             y después una CORRECCIÓN TÉCNICA ACOTADA (D103) sobre ella.
             **APLICADA NO ES CERTIFICADA**, y REGISTRAR o CONTRATAR no es CORREGIR.

             CÓMO QUEDA CADA CONDICIÓN, en CUATRO estados que no se mezclan:
               CORREGIDAS EN F4c     8   C-L.1 C-L.3 C-L.4 C-L.6 C-L.7 C-L.8 C-L.9 C-L.11
                                         + los cinco residuos de C-L.13
               REGISTRADAS PARA F5   2   C-L.2 (PN-15, decide el Owner) · C-L.12
               CONTRATADAS PARA F6   2   C-L.10 · J-11 — CERO líneas de código escritas
               ABIERTA POR COBERTURA 1   C-L.5
               C-L.1  CERRADA · D96: `revision_base` OBLIGATORIO de `preparada` en §3.6,
                      registrable en `conflicto` y `abandonada`, y ENTRA en el cómputo de
                      `tx`. Cierra J-01 (BLOQUEANTE) y J-02 a la vez, sin nonce ni timestamp
               C-L.2  REGISTRADA PARA F5 · D97 crea PN-15: G20–G23 PRESIONADAS y pendientes
                      de F5, NO derogadas por F4, con fila propia para kernel/KERNEL.md en
                      §17. **La decisión sigue SIN TOMAR**: es del Owner, y F4 no puede
                      tomarla. Registrar NO es corregir
               C-L.3  CERRADA · D98 reformuló la regla de D92 sobre PARTICIPACIÓN, y
                      **D103 la corrigió después**: D98 retiraba el barrido léxico del
                      criterio y lo reintroducía en su algoritmo —marcaba «condicionante»
                      buscando «ANTES de construir» en texto libre—, y publicaba «seis
                      procesos, diez pares», cardinalidad que ningún árbol puede satisfacer.
                      D103 deriva SÓLO de campos estructurados —`capacidad`,
                      `capacidad_productora`, `propietario_global`— y separa DOS NIVELES:
                      CATÁLOGO ESTÁTICO = 5 procesos y 9 pares, con (DEP, SEG) por la
                      obligatoria; y POR ITEM para AUD, que exige DOM:revision, SEG:revision
                      o NINGUNA según su propietario derivado — cero o un par, nunca dos.
                      Contrato F6 completo, y G-15 pasa a EJECUTAR la derivación
               C-L.4  CERRADA · procedencia de O16 registrada con fecha, formulación
                      presentada y respuesta literal del Owner. No se creó O17
               C-L.5  ABIERTA, Y NO LA CIERRA ESTA TANDA · es condición del gate siguiente,
                      escrita al final de §19 con sus requisitos exactos: lectura ÍNTEGRA de
                      ADS-PENDIENTES con sus BLOQUES B y C y de los documentos 16, 17 y 18;
                      manifiesto con ruta, líneas, SHA-256 y primera y última sección
                      sustantiva; declaración de cobertura REALMENTE LEÍDA; cualquier fuente
                      asignada y no leída impide la suficiencia; y el adjudicador no corrige
                      los hallazgos que encuentre
               C-L.6  CERRADA · D99: las CINCO salidas verdes de M7, alineadas en las tres
                      sedes de §8.3
               C-L.7  CERRADA · este fichero. Estado de las fases, pregunta_pendiente,
                      RESULTADO de la matriz, presiones y siguiente acción, reescritos
               C-L.8  CERRADA · D100: el `hash_previo` de la reparación es el
                      `hash_observado` del `deriva`, PARA LAS TRES CAUSAS. El ancla de la
                      restauración es `revision_base`, y es un dato distinto
               C-L.9  CERRADA · 42→46 derivado en las seis sedes, reconciliación de externos
                      corregida a 9 = 7 + F-01 + F-05, y G-26 ampliada a cuatro
                      comprobaciones sin ninguna cifra constante
               C-L.10 CONTRATADA PARA F6 · D102: tres contratos completos —censo
                      AFIRMACIONES derivado, T152 sobre toda sede que publique versión, y la
                      guardia de intérprete con exit 2— y ocho casos de regresión.
                      **CERO líneas implementadas.** T151 y T152 siguen pasando en verde
                      sobre las sedes que el corpus desmiente. Contratar NO es implementar
               C-L.11 CERRADA · D101: §6.7 recibe fila propia X62. X51 conserva su escenario
               C-L.12 REGISTRADA PARA F5 · los dos restos de (b) —«(P7)» donde aplica P9 en
                      L358, y la numeración 1,2,5,3,4 de L462–472— quedan como checklist
                      verificable, con ruta, ubicación, corrección exacta y prueba. Sin PN
                      nueva: el contenido no cambia. **El texto de (b) sigue como estaba**
               C-L.13 CERRADA los cinco primeros —K-05, K-09, K-10, K-08, L-03—; J-11
                      CONTRATADO PARA F6 en D102, sin implementar

             F5 NO arranca sin un veredicto explícito de SUFICIENCIA.
falta_para_cerrar_la_capa:
  · F4c ESTÁ ABIERTA. El GATE DEFINITIVO INDEPENDIENTE devolvió **INSUFICIENTE PARA F5**,
    adjudicado por L sobre los dictámenes cerrados de J y K, y **sus correcciones están
    ahora APLICADAS — NO CERTIFICADAS**. Veinticinco hallazgos planteados, uno RECHAZADO
    (J-09) y **VEINTICUATRO consolidados**, derivados fila a fila de la adjudicación:
    **BLOQUEANTE 1 · GRAVE 6 · MEDIO 10 · MENOR 7**. Las seis razones del veredicto fueron
    cobertura incompleta, el BLOQUEANTE J-01, los SEIS graves, un contrato F6 que aún exigía
    decidir arquitectura (K-02), la contradicción con G20–G23 sin presión F5 (K-06) y un
    checkpoint no vigente. **F5 SIGUE NO AUTORIZADA**: aplicar una corrección no es superarla,
    y hace falta un gate independiente nuevo sobre el resultado corregido.
  · ERRATA DEL PROPIO GATE, CORREGIDA FUERA DE SU TEXTO LITERAL: el documento 19 dice
    «cinco graves» y enumera SEIS identificadores —J-02, K-01, K-02, K-03, K-06, L-02—.
    El texto de L **se conserva intacto** y la corrección va en un corrigendum externo del
    propio documento 19. La cifra vigente, DERIVADA de las filas adjudicadas, es **SEIS**.
  · LOS TRES HALLAZGOS QUE CAÍAN SOBRE ESTE FICHERO —K-01, J-10, L-01— **se dejaron
    intactos DURANTE el gate**, deliberadamente, porque corregirlos allí habría vuelto a
    hacer que quien recibe sea quien aplica. **Se corrigen en esta tanda**, que es la que
    corresponde, y por eso este bloque ya no dice DIEZ presiones ni se detiene en D63.
  · LA COBERTURA SIGUE SIENDO UNA CONDICIÓN ABIERTA (C-L.5), y **esta tanda no la cierra ni
    puede cerrarla**: aplicar correcciones no es leer lo que no se leyó, y quien aplica no
    certifica su propia cobertura. Tres gates consecutivos han declarado lectura parcial del
    mismo material —ADS-PENDIENTES bloques B y C, y los documentos 16, 17 y 18—. Mientras
    nadie los abra, ningún gate puede certificar que no contengan algo que refute o agrave lo
    escrito, y **L lo demostró con dos ejemplos en direcciones opuestas**: §12 reforzó K-06, y
    la cabecera L3–L6 le obligó a tumbar la base externa de K-03 y a retirar su propio
    agravamiento de K-11. **Sólo la cierra el gate siguiente, mediante lectura real.**
  · NO SE HA INICIADO F5, ni F6, ni PesquerApp. Ninguna enmienda normativa está redactada,
    C8 no existe y C7 no se ha tocado.

  · F4c ESTÁ ABIERTA, y ahora con el GATE FINAL INDEPENDIENTE ejecutado y devuelto:
    **INSUFICIENTE PARA F5**, por adjudicación de un tercer agente sobre dos dictámenes
    independientes. CUATRO BLOQUEANTES, SEIS GRAVES y una COBERTURA DE CORPUS INCOMPLETA,
    cada una bastante por sí sola. **F5 NO queda autorizada.** Antes: un veredicto de
    insuficiencia de la tercera revisión, dos devoluciones independientes y CINCO
    comprobaciones técnicas.
    Antes: dos devoluciones independientes, la segunda con veredicto explícito de
    INSUFICIENCIA, y CUATRO comprobaciones técnicas más. Las correcciones de todas las aplicó
    QUIEN LAS RECIBIÓ, y eso no prueba que estén bien resueltas. LA EVIDENCIA DE QUE EL
    ENCADENAMIENTO IMPORTA: dos de los hallazgos BLOQUEANTES de la segunda son defectos que
    la PRIMERA CORRECCIÓN introdujo o no vio, los TRES de la segunda corrección técnica están
    en texto que la corrección técnica ANTERIOR escribió, los DOS de la tercera comprobación
    están en texto que la SEGUNDA escribió, y los DOS de la CUARTA están en texto que la
    TERCERA escribió, y el de la QUINTA está en texto que la CUARTA escribió. SEIS pasadas
    encadenadas —siete con la sexta comprobación técnica—, y cada una encontró defectos de
    la anterior. NINGUNA crítica se declara superada. F4c sólo se cierra con un veredicto explícito de SUFICIENCIA emitido por un revisor
    independiente sobre el resultado corregido
  · TRECE PRESIONES NORMATIVAS VIGENTES —PN-1, PN-2, PN-3, PN-6 a PN-15—. El total se
    DERIVA de las cabeceras `## \`PN-` de §16: QUINCE menos PN-4 RETIRADA y PN-5 FUSIONADA
    en PN-3. Ninguna renumerada, y ninguna redactada. PN-1 —la sección (g)— BLOQUEA todo el
    estado durable, y decide además fsync, regla de commit, sellado, identidad y regla de
    lectura. PN-2 y PN-3 son la misma pregunta por dos caminos. PN-6 reinterpreta O12.
    PN-7 (b.14 dice «completar o revertir»), PN-8 (VER no está en la ruta AUD), PN-9
    (predicados de obligación de b.3 — probablemente ninguna materia, y F5 debe
    CONFIRMARLO), PN-10 (O11 dice «estado durable»), PN-11 (gobierno Git del control repo,
    con sede en O16 y su procedencia ya registrada), PN-12 (mapa documental de O8),
    PN-13 (proceso:SIS y proceso:INV sin vía para DOM, SEG ni DIS) y PN-14
    (DIS/Reconstruccion en material aprobado). **PN-15 la añade esta tanda** por K-06:
    G20–G23 de KERNEL.md 1.5.0 están PRESIONADAS y pendientes de F5, **NO derogadas por
    F4**, y hasta que F5 decida regla a regla SIGUEN VIGENTES
  · NADA CONSTRUIDO: ni kernel, ni runtime, ni tooling, ni esquemas, ni adaptadores, ni
    plantillas, ni packs, ni validadores, ni migraciones. Las correcciones son DISEÑO
    CORREGIDO, no diseño implementado
  · NADA PROBADO: las **46** filas de la tabla adversarial de §2.6.7 —derivadas por conteo,
    no escritas a mano; X62 la añade esta tanda por J-03—, las 9 ventanas RC-1–RC-9 de
    §2.6.9, los 11 escenarios negativos de §11.5 y los 12 escenarios de §14 están ESCRITOS.
    Ninguno ejecutado
  · DEFECTO DE C7 REGISTRADO Y NO CORREGIDO: su gate exige Integration Set con UNA sola
    fuente y E2.6 exige «varias». Prescripción CERRADA, trazabilidad a E2.6, ejecución F6.
    NO es presión normativa. C7 no se ha tocado
  · EL GOBIERNO GIT DEL CONTROL REPO NO EXISTE: ninguna fila de la tabla de propiedad de C7
    lo alcanza. Declarado en §2.6.10, y su relleno es F6
  · la PRIMERA ADOPCIÓN REAL sigue seleccionada y NO ejecutada. La columna de uso real,
    vacía. **O15** (resolución posterior del Owner, que revisa O14 sin reescribirlo):
    PesquerApp será la primera adopción REAL, PERMANENTE y COMPLETA de ADS; su control repo
    ADS nace DEFINITIVO y no se crea para tirarlo; los clones y worktrees aislados protegen
    LAS FUENTES y las ramas productivas, no convierten el control repo en desechable; exige
    la BASE COMPLETA ACORDADA antes de empezar, no un MVP; lo que sólo se demuestra contra un
    producto real se completa DURANTE la adopción; los defectos entran por MIGRACIÓN y
    evolución versionada; reconstruir o sustituir el control repo exigiría migración
    explícita, autoridad y evidencia, y nunca es el procedimiento normal; «piloto», donde el
    término se conserve, significa PRIMERA ADOPCIÓN REAL y caso inicial de certificación.
    **O15 NO autoriza iniciar la adopción**
  · ningún adaptador existe, y por tanto ninguno está certificado
  · X1 y P-05 siguen deferidas. Ninguna decisión de F4 cruza esa línea, y D27 resuelve
    `capa` precisamente para no cruzarla
  · el SUELO DE P-08: si el runner miente, nada dentro del repositorio lo detecta.
    Declarado en §11.4, no resuelto
  · ORDEN TOTAL ENTRE MÁQUINAS: la cadena de eventos da orden total por transacción y
    parcial entre emisores concurrentes. La bifurcación se DETECTA; resolverla es runtime
    distribuido, y E2.7 ya lo dejó abierto
  · leer el manifiesto exige Python 3.11 o superior
```

> **Qué está demostrado y qué no**, criterio a criterio y con el artefacto que lo sostiene:
> [`08-EVIDENCIA-MULTIREPO.md`](08-EVIDENCIA-MULTIREPO.md). Ningún criterio se cuenta como
> verificado por estar escrito.


## Estado de las fases

```text
F0  BASELINE Y MAPA          ENTREGADA
F1  MINERÍA                  CERRADA — PesquerApp. gym-wear RETIRADO por el Owner
F2  CONTRASTE                ENTREGADA
M   MANDATO MULTI-REPO       EJECUTADO — interrumpió F3 por orden del Owner
F3  SÍNTESIS                 ENTREGADA — 09-SINTESIS.md. Puerta X1..X5 superada
F3c PUERTA CORRECTIVA        CERRADA y después CORREGIDA — crítica independiente aplicada,
                             O7–O14 registradas, T158 corregido en dos pasadas, y los cuatro
                             defectos que la revisión encontró en la propia puerta resueltos.
                             10-CRITICA-INDEPENDIENTE-F3.md · release 2.0.0-alpha.9
F4  ARQUITECTURA INTEGRADA   ENTREGADA, NO CERTIFICADA, y después CORREGIDA por
                             devolución independiente — 11-ARQUITECTURA-INTEGRADA.md
F4c CRÍTICA INDEPENDIENTE    ABIERTA. La cadena completa, EMITIDA por revisores y auditores
                             que no escribieron F4, TRANSCRITA y APLICADA por su autor
                             material — **y aplicar no es superar**.
                             1ª  nueve bloques · 12-CRITICA-INDEPENDIENTE-F4.md · D23–D33
                             2ª  VEREDICTO DE INSUFICIENCIA por un revisor que TAMPOCO
                                 aplicó la primera: 2 BLOQUEANTES, 7 GRAVES, 14 nuevos ·
                                 13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md · D34–D45
                             3ª  DEVOLUCIÓN TÉCNICA PREVIA — auditoría externa de Codex
                                 sobre el ÁRBOL REMOTO REAL: 3 BLOQUEANTES, 2 GRAVES, 4
                                 MEDIOS, 2 MENORES · 14-DEVOLUCION-TECNICA-PREVIA-F4C.md ·
                                 D46–D51. NO es veredicto de suficiencia
                             SEIS PASADAS TÉCNICAS encadenadas, ninguna de ellas la tercera
                             revisión: D52–D54, D55–D57, D58–D59, D60–D61, D62 y D63. Cada
                             una sobre el texto que escribió la anterior
                             4ª  TERCERA REVISIÓN INDEPENDIENTE — VEREDICTO DE
                                 INSUFICIENCIA · 15-TERCERA-REVISION-INDEPENDIENTE-F4C.md ·
                                 D64–D70
                             5ª  GATE FINAL INDEPENDIENTE (A·B·C) + su COMPLEMENTO DE
                                 COBERTURA — INSUFICIENTE PARA F5: 4 BLOQUEANTES, 6 GRAVES
                                 y cobertura incompleta · documentos 16 y 17 · D71–D86
                             6ª  GATE DE CIERRE INDEPENDIENTE (G·H, adjudica I) —
                                 INSUFICIENTE PARA F5: cobertura incompleta y DIEZ de las
                                 43 filas FALLIDAS · documento 18 · D87–D95
                             7ª  GATE DEFINITIVO INDEPENDIENTE (J·K, adjudica L) —
                                 **INSUFICIENTE PARA F5** sobre r4=0ea0451, por SEIS razones
                                 independientes. 25 hallazgos planteados, J-09 RECHAZADO,
                                 **24 consolidados: BLOQUEANTE 1 · GRAVE 6 · MEDIO 10 ·
                                 MENOR 7**, derivado de las filas adjudicadas ·
                                 19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md · **D96–D102**
                             SUS TRECE CONDICIONES C-L.1–C-L.13 están APLICADAS —doce
                             cerradas o registradas—, salvo C-L.5, la COBERTURA, que sólo
                             puede cerrar el gate siguiente mediante lectura real.
                             **APLICADAS NO ES CERTIFICADAS.**
                             DOS de los hallazgos de la 2ª devolución, TRES de la 3ª, LOS
                             TRES de la segunda corrección técnica, y K-02 del gate
                             definitivo —cuya causa es D75, una corrección anterior— son
                             defectos que las correcciones ANTERIORES introdujeron o no
                             vieron.
                             SIGUE ABIERTA: sólo la cierra un veredicto explícito de
                             SUFICIENCIA emitido por revisores independientes de contexto
                             limpio sobre el resultado corregido, y que NO sean quien lo
                             aplicó. Ese veredicto NO existe
F5  ENMIENDAS                TRECE presiones normativas vigentes —derivadas de §16: quince
                             cabeceras menos PN-4 retirada y PN-5 fusionada—, enumeradas y
                             sin redactar. **NO INICIADA, y NO AUTORIZADA**
F6  DESCOMPOSICIÓN Y EJECUCIÓN  no iniciada
```

## Lo que cambió en el repositorio

```text
F0
docs/evolucion/00-INDICE.md               nuevo — punto de entrada de la iniciativa
docs/evolucion/01-BASELINE-ADS.md         nuevo — 23.1
docs/evolucion/02-MAPA-DIRECTIVA.md       nuevo — 23.2
docs/evolucion/03-INVARIANTES.md          nuevo — lo que no se toca en silencio
docs/evolucion/04-PLAN-DE-INVESTIGACION.md nuevo — preguntas, protocolo y fases
validadores/exclusiones.yaml              los dos documentos del Owner, exentos de
                                          vocabulario con su motivo escrito
kernel/VERSION · KERNEL_CHANGELOG.md ·    release 2.0.0-alpha.3 con su entrada, y la
kernel/VERSIONES.md · .upstream-hash      huella reanclada sobre el cambio
README.md                                 enlaza la iniciativa

F1
docs/evolucion/05-CANDIDATOS.md           29 candidatos con procedencia y evidencia

F2
docs/evolucion/06-CONTRASTE.md            29 veredictos · 6 problemas arquitectónicos
docs/evolucion/01-BASELINE-ADS.md         corrección C-1 — gobierno Git
docs/evolucion/02-MAPA-DIRECTIVA.md       corrección C-1 — el apartado 8 pasa a PARCIAL
docs/evolucion/05-CANDIDATOS.md           correcciones C-2 y C-3
docs/evolucion/03-INVARIANTES.md          regla 6 — ninguna capa nueva sin evidencia
docs/evolucion/04-PLAN-DE-INVESTIGACION.md estado de las diez preguntas
docs/evolucion/07-DECISION-MULTIREPO.md   la contradicción, y su resolución por el Owner

MANDATO MULTI-REPOSITORIO
docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md  enmienda a (a) y (b)
kernel/operativo/contratos/C6 · C7        los dos contratos nuevos
kernel/operativo/esquemas/integration-set.yaml
kernel/operativo/plantillas/SOURCES.toml · INTEGRATION-SET.md
kernel/operativo/pruebas/T159-T170-multirepo.md
kernel/operativo/validadores/comprobar_fuentes.py
tooling/workspace.py · tooling/tests/test_workspace.py
kernel/KERNEL.md 1.4.0 · README · START_HERE · BOOTSTRAP · PROJECT · PROFILE
capacidades DSP · ENT · PLT · SIS · ARQ · DOM · ENC · VER · SEG · C2
release 2.0.0-alpha.5

PASADA CORRECTIVA DE F2
tooling/workspace.py                      los ocho bloqueantes, cada uno con su prueba
tooling/tests/test_workspace.py           29 → 57 pruebas: batería adversarial,
                                          reconstrucción de cuatro fuentes y red cerrada
tooling/new-project.sh                    el control repo nace en la rama que documenta
kernel/operativo/validadores/
  comprobar_fuentes.py                    T161 deja de ser tres literales
  comprobar_arranque.py                   T168 ampliada · T171 nueva
  comprobar_negativos.py                  N161–N161g · N171 · N171b
kernel/operativo/pruebas/fixtures/formulaciones-retiradas.yaml
kernel/KERNEL.md 1.5.0                    K0.6 · K0.8 · G04 · G12 · C0 · G26 · G27 ·
                                          G38 · G39 · G46 · G48
capacidades ARQ · ENC · DSP · SEG · CON · contratos C2 · C5 · C6 · 00-INDICE
docs/evolucion/08-EVIDENCIA-MULTIREPO.md  qué está demostrado y qué no
START_HERE.md                             cinco preguntas, y el checklist decía cuatro
kernel/VERSION · KERNEL_CHANGELOG.md ·    release 2.0.0-alpha.6 con su entrada, y la
kernel/VERSIONES.md · .upstream-hash      huella reanclada sobre el cambio

F3 SÍNTESIS
docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md
                                          entra como MATERIAL TEMPORAL de evolución, en su
                                          propio commit y sin copiarse en ningún otro
                                          fichero. Release 2.0.0-alpha.7
kernel/operativo/validadores/exclusiones.yaml
                                          quinta exención de vocabulario para un documento
                                          en voz del Owner. La medida de P-07
docs/evolucion/09-SINTESIS.md             nuevo — el entregable de F3
docs/evolucion/00-INDICE.md               23.4 entregada · el documento nuevo enlazado · y
                                          dos cifras que se habían quedado atrás
docs/evolucion/04-PLAN-DE-INVESTIGACION.md Q9 y Q10 respondidas · puerta de F3 superada ·
                                          la ficha de candidato registra su aplazamiento

PUERTA CORRECTIVA PRE-F4
docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md  nueva — la crítica, sus seis hallazgos, las
                                          ocho resoluciones y el defecto de T158
docs/evolucion/09-SINTESIS.md             addendum + marca en cada sección revisada. El
                                          texto original se conserva íntegro
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  O7–O14, sin reescribir O1–O6
kernel/operativo/validadores/
  comprobar_evidencia.py                  contrato de vigencia: falla cerrado, sin
                                          circularidad, y va el último para no enmascarar
                                          el motivo de otras mutaciones
  comprobar_fuentes.py                    corpus_recorrido() y ficheros_recorridos():
                                          definición ÚNICA del recorrido de T161
  comprobar_negativos.py                  N158g y N158h
  validadores.yaml                        bloque `vigencia` de `fuentes`
  exclusiones.yaml                        clasificación POR UBICACIÓN: docs/owner/
kernel/operativo/pruebas/T136-T152-post-auditoria.md  qué no veía T158, y su alcance
docs/owner/                               nuevo — los dos documentos multi-repo del Owner,
                                          movidos con git mv y sus referencias al día
kernel/VERSION · KERNEL_CHANGELOG.md ·    release 2.0.0-alpha.8 — HISTÓRICO. Fue el estado
kernel/VERSIONES.md · .upstream-hash      final de esta pasada, y NO es la base vigente:
                                          la corrección de abajo lo sustituye

CORRECCIÓN DE LA PUERTA — cuatro defectos que la revisión independiente encontró en ella
docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md  procedencia: quién EMITE la crítica y quién
                                          ESCRIBIÓ el fichero dejan de confundirse
docs/evolucion/09-SINTESIS.md             O13 deja de dar por certificado lo que no lo está ·
                                          la vía de autoridad pasa de C4 a a.4
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  O9 y O13 corregidas en su registro canónico
kernel/operativo/validadores/
  comprobar_evidencia.py                  validación TIPADA del contrato `vigencia`, sin
                                          `except Exception`
  comprobar_negativos.py                  N158i–N158o · el arnés exige el diagnóstico
                                          esperado y rechaza la traza como detección
kernel/operativo/pruebas/T136-T152-post-auditoria.md  el manifiesto inválido se rechaza con
                                          un fallo, nunca con una traza
kernel/VERSION · KERNEL_CHANGELOG.md ·    release 2.0.0-alpha.9 — ESTADO VIGENTE, con su
kernel/VERSIONES.md · .upstream-hash      entrada y la huella reanclada sobre el cambio

F4 ARQUITECTURA INTEGRADA
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md  nueva — el entregable de F4
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  D16–D22, sin reescribir D1–D15 ni O1–O14
docs/evolucion/00-INDICE.md               23.5 entregada
NADA de kernel/operativo/, packs/ ni tooling/ ha cambiado en F4. Ninguna enmienda.

F4c DEVOLUCIÓN INDEPENDIENTE — nueve bloques de hallazgos, aplicados
docs/evolucion/12-CRITICA-INDEPENDIENTE-F4.md  nueva — la crítica, su procedencia, los
                                          nueve bloques y qué se corrigió en cada uno
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md  §1.3 matriz de fuentes de verdad · §2.5–§2.9
                                          protocolo transaccional reescrito · §3.2–§3.8
                                          tipos, contratos y recuento · §4.1–§4.3 contrato
                                          documental · §5.2 aspectos y §5.6 tres celdas ·
                                          §6.5 nivel derivado y §6.7 puntero en fuente ·
                                          §8.1–§8.4 los cuatro recorridos · §9.2 y §9.5
                                          certificación · §11.2–§11.5 P-08 · §15.8 · §16
                                          presiones · §17 · §18 · §19
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  D23–D33, SIN reescribir D1–D22 ni O1–O14
docs/evolucion/00-INDICE.md               la crítica de F4, enlazada
NADA de kernel/operativo/, packs/ ni tooling/ ha cambiado en F4c, salvo la evidencia
DERIVADA que el runner republica. Ninguna enmienda. (a), (b), E1, E2, K-1 y C4 intactos.

(a), (b) y E1 siguen ÍNTEGRAS y sin reescribir: E2 las enmienda por sustitución
explícita, que es la única vía que admite la regla 1 de 03-INVARIANTES.
Los documentos del Owner tampoco se han tocado: el de pendientes entra literal.
NADA se ha escrito en los proyectos minados.
NADA de kernel/operativo/, packs/ ni docs/rediseno/ ha cambiado en F3.
```

### Una cifra mal escrita en un mensaje de commit, corregida aquí

El commit `d78a3df` —«N158g reancla su cifra con los dos documentos nuevos»— dice que el
corpus pasa «de 285 a 287» y la cifra citada «de 283 a 285». **Los valores reales son 286 y
284**: sólo entró UN documento nuevo en ese punto, no dos. El historial no se reescribe, así
que la corrección vive aquí, que es donde se buscan las cifras vigentes. Y el recuento sigue
derivándose, no escribiéndose:

```bash
grep -o "[0-9]* ficheros recorridos" kernel/operativo/pruebas/evidencia/fuentes-salida.txt
grep -o "documentos analizados: [0-9]*" kernel/operativo/pruebas/evidencia/referencias-salida.txt
```

### El recuento de commits se deriva, no se escribe

Esta sección llegó a decir «MANDATO MULTI-REPOSITORIO — tres commits» y se quedó
desactualizada en el commit siguiente, que es el mismo defecto que
[`CORRECCIONES-POST-AUDITORIA`](../rediseno/CORRECCIONES-POST-AUDITORIA.md) ya había
corregido para la entrega anterior. Lo que se fija es el punto de partida y el comando:

```bash
git rev-list --count 910d1d3..HEAD     # cuántos commits desde el cierre de F2
git log --oneline 910d1d3..HEAD        # cuáles son
```

```text
910d1d3   último commit de F2 (contraste)
5         commits de la implementación multi-repo: a4475a2 · fd741e8 · a8e2273 ·
          06a93ba · a224c36. NO tres, y NO seis
entre     a224c36 y 4cf9b8d, la pasada correctiva de F2
después   43c627f entra el documento de pendientes; a partir de ahí, F3
7e450cf   F3 síntesis · f59d9eb su evidencia derivada
8b6727a   primer cierre de la puerta correctiva — release 2.0.0-alpha.8, HISTÓRICO
8403d23   corrección de la puerta tras la revisión del SHA remoto — release
          2.0.0-alpha.9, ESTADO VIGENTE
```

Escribir el total a mano aquí lo dejaría mal en la siguiente confirmación. **El historial
no se reescribe**: la cifra se corrige contándola, no rehaciendo los commits.

## Cómo se comprueba que esto sigue en pie

```bash
python3 kernel/operativo/validadores/registrar_evidencia.py   # exige Python 3.11+
git status --short          # vacío: los generados son deterministas
```

**Verde no basta.** Los ocho bloqueantes de `workspace.py` —escape por enlace simbólico,
fuentes dentro del control repo, repositorios anidados, `init` mutando con el manifiesto
roto, secretos en la salida, SSH confundido con credenciales, normalización que igualaba
repositorios distintos y tipos de TOML que reventaban— convivieron con los trece
validadores en verde y con veintinueve pruebas pasando. Lo que cerró cada uno fue una
prueba ADVERSARIAL que falla contra el código anterior, no el color del resumen.

## Lo que cambió en el repositorio · segunda devolución

```text
F4c SEGUNDA DEVOLUCIÓN INDEPENDIENTE
docs/evolucion/13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md  nueva — el juicio, su procedencia,
                                          los once candidatos adjudicados, catorce hallazgos
                                          nuevos, siete rechazados y el veredicto de
                                          suficiencia
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md  §2.2 R3 cualificada · §2.3 · §2.5 · §2.6.1
                                          cuatro registros · §2.6.3 secuencia de fsync ·
                                          §2.6.5 once→dieciséis ventanas · §2.6.6 fsync y
                                          comprobación post-terminal · §2.6.7 diecisiete→
                                          treinta filas · §2.6.8 regla de lectura NUEVA ·
                                          §2.6.9 conflicto NUEVA · §2.6.10 Git NUEVA · §2.7 ·
                                          §2.8 contrato de identidad · §2.9 · §3.2 · §3.3 ·
                                          §3.3.0 NUEVA · §3.3.1 · §3.3.1.1 NUEVA · §3.5 ·
                                          §3.7 · §3.8 recuento 24→25 · §4.2 · §4.3 · §5.6 ·
                                          §5.7 NUEVA · §6.4 · §6.7 · §7.4 · §7.6 · §8.1 ·
                                          §8.2 · §8.3 · §8.4 · §9.1 · §9.2 · §9.5 · §10.2 ·
                                          §11.2 · §11.4 · §11.5 · §15.7 · §15.8 · §16 ·
                                          §17 · §19
docs/evolucion/12-CRITICA-INDEPENDIENTE-F4.md  se CONSERVA tal como se escribió, con un
                                          aviso de que la segunda revisión ya se hizo y
                                          encontró defectos en SUS correcciones. Sus dos
                                          erratas —§5.7 por §5.6, y «SEIS» por diez—
                                          corregidas donde se escribieron
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  D34–D45, SIN reescribir D1–D33 ni O1–O14
docs/evolucion/00-INDICE.md               la segunda crítica, enlazada
NADA de kernel/operativo/, packs/ ni tooling/ ha cambiado, salvo la evidencia DERIVADA que
el runner republica. (a), (b), E1, E2, K-1 y C4 intactos. **C7 TAMPOCO se ha tocado**: su
defecto queda REGISTRADO con prescripción cerrada, y su ejecución es F6.
```

## Lo que cambió en el repositorio · segunda corrección técnica

```text
F4c SEGUNDA CORRECCIÓN TÉCNICA — tres GRAVES, los restos vigentes de §2.6, y O15
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md  cabecera · §2.6.1 fases y transiciones ·
                                          §2.6.2 entradas de recuperación y cardinalidad ·
                                          §2.6.4 REESCRITA: intención vigente, función de
                                          clasificación completa y reemisión · §2.6.5 W11,
                                          W12a, W12b y el resumen de escalado · §2.6.6
                                          garantía 6, regla de Git y qué se emite ante un
                                          marcador que no debería existir · §2.6.7 X05,
                                          X15, X26, X28 y el recuento declarado · §2.6.9
                                          conflicto, término y coherencia W×R NUEVA ·
                                          §2.6.11 · §3.6 matriz tipo × fase NUEVA y
                                          reparto en tres capas · §8.2 O15 · §15.4 · §15.8
                                          D55–D57 · §18 · §19
docs/evolucion/14-DEVOLUCION-TECNICA-PREVIA-F4C.md  DOS addenda nuevos y el veredicto
                                          reanclado. Su texto se CONSERVA entero
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  D55–D57 y O15, SIN reescribir D1–D54 ni
                                          O1–O14
docs/evolucion/CHECKPOINT-ADS-NEXT.md     este bloque, el estado de la fase y O15

F4c TERCERA COMPROBACIÓN TÉCNICA — recuento por ejes, emisión frente a restauración, matriz
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md  cabecera · §2.6.2 cardinalidad · §2.6.4 emisión
                                          y restauración idempotente, con la cardinalidad de
                                          cada fase por `tx` · §2.6.5 W12a y W13 · §2.6.6 ·
                                          §2.6.7 X21 y X26 · §2.8 qué significa «reemitir» ·
                                          §3.6 prueba tipo a tipo, cero recursión del diario
                                          y recuento derivado · §15.8 D58–D59
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  D58–D59, SIN reescribir D1–D57 ni O1–O15
docs/evolucion/CHECKPOINT-ADS-NEXT.md     su bloque y las marcas [REVISADO] sobre D56 y D57

F4c CUARTA COMPROBACIÓN TÉCNICA — cardinalidad por ruta, tope de iteración y frontera real
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md  cabecera · §2.6.1 la transición de reintento ·
                                          §2.6.2 cardinalidad · §2.6.4 cardinalidad
                                          CONDICIONAL por ruta, contador `iteracion` y las
                                          cinco secuencias completas · §2.6.9 el tope · R9 ·
                                          §2.6.7 X58 · §3.6 frontera real de la `tx`,
                                          `sellado` NO transaccional, marcado de órdenes y
                                          recuento 40 · 23 · 63 · §15.8 D60–D61
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  D60–D61, SIN reescribir D1–D59 ni O1–O15
docs/evolucion/CHECKPOINT-ADS-NEXT.md     su bloque

F4c QUINTA COMPROBACIÓN TÉCNICA — observación e intento, dos contadores
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md  cabecera · §2.6.1 la transición de reintento ·
                                          §2.6.2 · §2.6.4 los DOS contadores y las cinco
                                          secuencias con sus valores · §2.6.9 el tope, los
                                          dos campos de contabilidad, el predicado y R9 ·
                                          §2.6.7 X58 · §3.6 esquema, contrato de `conflicto`
                                          y de `reconciliacion-preparada`, validador, y
                                          `retirada-de-cuerpo` como única excepción ·
                                          §15.8 D62
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  D62, SIN reescribir D1–D61 ni O1–O15
docs/evolucion/CHECKPOINT-ADS-NEXT.md     su bloque y la marca [REVISADO] sobre D60

F4c SEXTA COMPROBACIÓN TÉCNICA — lápida, identidad, tres niveles y retirada alcanzable
docs/evolucion/11-ARQUITECTURA-INTEGRADA.md  cabecera · §2.8 punto 4bis, la excepción tipada
                                          al algoritmo de identidad · §2.9 semántica del
                                          sellado reescrita, TRES NIVELES, fuente de
                                          recuperación, append-only con precisión física,
                                          qué referencia bloquea, contrato de
                                          `retirada-de-cuerpo` en once puntos y tabla
                                          `X-A`–`X-H` · §3.6 bloque de la excepción alineado,
                                          cierre Markdown corregido y validador con el
                                          algoritmo de identidad por tipo · §15.8 D63
docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md  D63, SIN reescribir D1–D62 ni O1–O15
docs/evolucion/CHECKPOINT-ADS-NEXT.md     su bloque
O15 INTACTA. §3.8 sin cambios. (a), (b), E1, E2, K-1, C4 y C7 intactos. Ningún documento
numerado nuevo.
O15 NO SE TOCA. (a), (b), E1, E2, K-1, C4 y C7 intactos. Ningún documento numerado nuevo.
NADA de kernel/operativo/, packs/ ni tooling/ ha cambiado, salvo la evidencia DERIVADA que
el runner republica. (a), (b), E1, E2, K-1, C4 y C7 intactos. NINGÚN documento `15-*` nuevo:
la corrección se registra por ADDENDUM sobre los documentos existentes.
```

## TANDA INTEGRADA DE CORRECCIÓN DEL GATE FINAL — cerrada, sin publicar

```text
QUÉ ES              la corrección de los 43 hallazgos distintos que el GATE FINAL
                    INDEPENDIENTE (documento 16) y su COMPLEMENTO DE COBERTURA (documento
                    17) dejaron abiertos: 4 BLOQUEANTES, 6 GRAVES, 20 MEDIOS y 14 MENORES,
                    44 filas y 43 distintos porque `A11` está absorbido en `M-8`.
                    El inventario NO se copió a mano: se DERIVÓ de los identificadores de la
                    tabla del documento 17 y se comprobó contra las cuatro cifras del encargo.

QUÉ NO ES           un veredicto. **Lo aplicó quien lo recibió**, por novena vez, y eso no
                    certifica nada. `F4c` sigue **ABIERTA** y el veredicto vigente sigue
                    siendo **INSUFICIENTE PARA F5**.

RESULTADO           **[HISTÓRICO · lo que esta tanda dejó]** `31 CORREGIDO_EN_F4 · 1
DE ESTA TANDA       PRESION_LISTA_PARA_F5 · 2 CONTRATO_COMPLETO_PARA_F6 · 8
                    EXTERNO_CON_PROPIETARIO · 1 HISTORICO_NO_APLICABLE = 43`. Un estado
                    primario por hallazgo, los cinco mutuamente excluyentes.

DECISIONES          `D71`–`D86`. `D16`–`D70` conservan su texto. `O15` y `O16` intactas.
PRESIONES           **[HISTÓRICO]** ONCE vigentes en el momento de esta tanda: `PN-1`,
                    `PN-2`, `PN-3`, `PN-6` a `PN-13`. `PN-4` retirada, `PN-5` fusionada en
                    `PN-3`. Sin renumerar. **`PN-13` es la única que esta tanda añadió**:
                    `proceso:SIS` y `proceso:INV` no dan vía a `DOM`, `SEG` ni `DIS`, y
                    `INS-5` las necesita antes de su gate.

RENOMBRADOS         `R1`–`R9` (ventanas de reconciliación, retiradas por `D64`) → `RC-1`–`RC-9`
                    `N0`–`N7` (fases de instalación) → `INS-0`…`INS-7`
                    `C6` `N1`–`N14` y la escala de novedad `N0`–`N4` NO se tocan.
```

> **Dónde acaba lo histórico y dónde empieza lo vigente** — corregido por `L-01`, MEDIO. El
> bloque de arriba es el **registro de la tanda del gate final** y sus cifras son **las de
> aquel momento**; la tabla de abajo es **VIVA** y ha seguido corrigiéndose en las tandas
> posteriores. Que un bloque histórico introdujera una tabla viva **sin marca que
> distinguiera una cosa de otra** es lo que `L-01` señaló: `RESULTADO` decía `31 · 1 · 2 · 8
> · 1` mientras la tabla, veintisiete líneas más abajo, daba `31 · 2 · 2 · 7 · 1`; y
> `PRESIONES` decía ONCE donde hoy son TRECE. **Los dos bloques quedan marcados, y ninguno
> se borra.**
>
> **CIFRAS VIGENTES, DERIVADAS de la tabla de abajo y no copiadas de ningún resumen:**
>
> ```text
> ESTADO PRIMARIO      31 CORREGIDO_EN_F4 · 2 PRESION_LISTA_PARA_F5 —B-2 y F-01— ·
> DE LOS 43            2 CONTRATO_COMPLETO_PARA_F6 —M-5 y M-6— · 7 EXTERNO_CON_PROPIETARIO
>                      —F-02 F-04 F-06 F-07 F-08 F-10 F-11— · 1 HISTORICO_NO_APLICABLE —m-3—
>                      = 43. Adjudicadas por `L`: 42 SUPERADAS · 0 FALLIDAS · 1 NO APLICABLE
>
> PRESIONES VIGENTES   TRECE. Derivado: quince cabeceras `## \`PN-` en §16, menos `PN-4`
>                      RETIRADA y `PN-5` FUSIONADA. `PN-15` la añade la tanda del gate
>                      definitivo, por `K-06`
>
> HALLAZGOS DEL GATE   25 planteados · 1 RECHAZADO (`J-09`) · **24 consolidados**:
> DEFINITIVO           BLOQUEANTE 1 · GRAVE 6 · MEDIO 10 · MENOR 7. Derivado de las filas
>                      adjudicadas por `L`, no de ningún total escrito
>
> FILAS ADVERSARIALES  46 filas físicas · 46 ids únicos en §2.6.7. `X62` la añade la tanda
>                      del gate definitivo, por `J-03`
> ```
>
> **Las condiciones de cierre que aparezcan en las filas de abajo citando cifras de su
> momento** —por ejemplo, «once puntos de presión» en la fila `A10`— **son el texto con que
> aquella fila se cerró**, y no se reescriben: la cifra vigente es siempre la derivada de
> arriba. Es la misma disciplina que la nota al pie de `O15`.

### Matriz de cierre de los 43 hallazgos distintos

> **RECONCILIADA.** La primera versión de esta tabla declaraba `34 · 2 · 1 · 8 · 1`, que
> **suma 46 y no 43**. El defecto era de método, no de contenido: `B-2`, `M-5` y `M-6`
> llevaban un estado compuesto —«corregido **y** contrato para F6», «corregido **y** presión
> para F5»— y el resumen contó **las dos mitades de cada uno**, una dentro de los 34 y otra
> como categoría propia. Tres hallazgos contados dos veces, 43 + 3 = 46. Ahora **cada
> hallazgo tiene EXACTAMENTE UN estado primario**, los cinco son mutuamente excluyentes, y lo
> demás son **atributos secundarios que NO entran en el total**.

| id | severidad | estado primario | decisión o sede | arquitectura corregida | requiere F5 | requiere F6 | bloquea F5 | bloquea F6 | cómo se cierra |
|---|---|---|---|---|---|---|---|---|---|
| `A1` | BLOQUEANTE | **`CORREGIDO_EN_F4`** | D72 | sí | no | no | no | no | enum de TRES valores con UNA sede, §3.6; §2.6.11 remite |
| `A2` | BLOQUEANTE | **`CORREGIDO_EN_F4`** | D71 · D89 | sí | no | no | no | no | predicado `abierta(tx)` en §2.6.1; **NUEVE** sedes vigentes y todas remiten —§2.6.4 dejó de redeclarar—, y la capa B pierde la regla de terminalidad sobre `derivada` que era el residuo exacto de `A2` |
| `B-1` | BLOQUEANTE | **`CORREGIDO_EN_F4`** | D75 | sí | no | no | no | no | `A2`–`A7` es `proceso:AUD` en items enlazados, propietario derivado por item |
| `B-2` | BLOQUEANTE | **`PRESION_LISTA_PARA_F5`** | D74 · D90 · PN-13 | sí | PN-13 | componer INS-5 y A9 tras PN-13 | no | sí · acotado a INS-5 y A9 | §8.0 declara la sede de composición y las cuatro vías, y **`D90` cierra la mitad `PLT` contra `C7:80-92`** —nunca fue materia del Owner: el contrato ya decía quién—. El residuo que queda es SÓLO `DOM`/`SEG`/`DIS` en `SIS` e `INV`, y ése sí es del Owner |
| `G-1` | GRAVE | **`CORREGIDO_EN_F4`** | D75 | sí | no | no | no | no | `SEG` y `CON` obligatorias de `proceso:DEP` en `U5b`; `G28` las hace irretirables |
| `G-2` | GRAVE | **`CORREGIDO_EN_F4`** | D75 | sí | no | no | no | no | `ARQ` por el `plan-tecnico` de su item `DEU`; `cambio-construido` producido por `CON` |
| `G-3` | GRAVE | **`CORREGIDO_EN_F4`** | D76 | sí | no | no | no | no | `INS-5` produce baseline y clasificación; el Owner lo aprueba — **y el gate y la salida están en §18**, que §8.0 declara sede canónica y que antes no los llevaba |
| `G-4` | GRAVE | **`CORREGIDO_EN_F4`** | D77 | sí | no | no | no | no | doce identificadores derivados del patrón `ads:memoria` |
| `A3` | GRAVE | **`CORREGIDO_EN_F4`** | D73 | sí | no | no | no | no | §7.4 paso 2 con las dos ramas; resumen de §16 alineado con `PN-7` |
| `A4` | GRAVE | **`CORREGIDO_EN_F4`** | §15.8 + cabecera | sí | no | no | no | no | bloques `D64`–`D68`, `D71`–`D86` y `D87`–`D95`; la tercera revisión ya no consta pendiente; **y la cifra se DERIVA** de los bloques de §15.8 —son doce, y ésta es la decimotercera— en vez de declararse derivada sin serlo (`I-19`) |
| `A5` | MEDIO | **`CORREGIDO_EN_F4`** | §2.6.9 | sí | no | no | no | no | sujeto corregido: ningún FICHERO en su hash posterior; el evento sí lo conserva |
| `A6` | MEDIO | **`CORREGIDO_EN_F4`** | D85 | sí | no | no | no | no | 5 fases · 6 estados · 7 filas, recalculados tras `D64` |
| `A7` | MEDIO | **`CORREGIDO_EN_F4`** | §3.6 · D95 | sí | no | no | no | no | «los cinco CAMPOS de procedencia» **en las SEIS sedes**, incluida la regla 1 de §2.6.10 — la única que el gate nombró y la única que no se había tocado |
| `A8` | MEDIO | **`CORREGIDO_EN_F4`** | D78 · D88 | sí | no | no | no | no | `estado/deriva/<ID>.abierta`, legible sin herramienta **y sujeto a las CINCO piezas de disciplina del marcador de transacción** —§2.4, §2.3, `.gitignore`, §2.9 y fila adversarial—, creado en el paso E y retirado por la transacción que lo resuelve. **Y la NORMA de §2.6.8 consulta los marcadores**, no el diario |
| `A9` | MEDIO | **`CORREGIDO_EN_F4`** | D79 · D87 | sí | no | no | no | no | dos actos de autoridad del Owner cierran `4b`; `X58` reformulado. **Y la cuarentena del acto (i) tiene plano**: `.ads/run/quarantine/<TX>/`, operacional, con su ciclo y su prueba |
| `A10` | MEDIO | **`CORREGIDO_EN_F4`** | §1 · §16 · §19 | sí | no | no | no | no | ONCE puntos de presión, derivados de §16 |
| `A12` | MENOR | **`CORREGIDO_EN_F4`** | D84 | sí | no | no | no | no | el CAS de Git, no «un único escritor» |
| `A13` | MEDIO | **`CORREGIDO_EN_F4`** | §3.6 | sí | no | no | no | no | fila `preparada` de §3.6 con los cinco CAMPOS |
| `M-1` | MEDIO | **`CORREGIDO_EN_F4`** | §4.3 | sí | no | no | no | no | TRECE condicionales, en las tres sedes |
| `M-2` | MEDIO | **`CORREGIDO_EN_F4`** | §1.3 | sí | no | no | no | no | fila del mapa documental, autoridad «nadie: se regenera» |
| `M-3` | MEDIO | **`CORREGIDO_EN_F4`** | D75 | sí | no | no | no | no | `U6` revalida el nivel vigente; no es `O12` |
| `M-4` | MEDIO | **`CORREGIDO_EN_F4`** | registro de `D67` | sí | no | no | no | no | resumen corregido: `proceso:AUD`, y propagar a las fuentes es `proceso:DEP` |
| `M-5` | MEDIO | **`CONTRATO_COMPLETO_PARA_F6`** | §5.3 + §5.2 + D91 | sí | no | extensión de ficha `capacidades/DSP/` **y de las capacidades LÍDERES DE COBERTURA**, con el conjunto derivado de los `contrato-de-aspecto` | no | no | F4 nombra el actor de las DOS mitades —`DSP` en APERTURA, la capacidad líder en CAMPAÑA— y declara que `C1` exige que la ficha lo autorice **en ambas**. **`DSP` y `ENC` están ya en §17**, que es la sede que F6 lee |
| `M-6` | MEDIO | **`CONTRATO_COMPLETO_PARA_F6`** | D80 | sí | no | clase, forma y rama en `entrada/` + ficha `capacidades/ENC/` | no | no | F4 determina clase, forma, rama, sujeto y salida; construirlas en `entrada/` es de F6. **`capacidades/ENC/` está ahora en §5.2 Y en §17**, que era la mitad literal de su condición de cierre |
| `M-7` | MEDIO | **`CORREGIDO_EN_F4`** | D82 | sí | no | no | no | no | items por macrocircuito y FRENO 3 circuito a circuito |
| `M-8` | MEDIO | **`CORREGIDO_EN_F4`** | D83 | sí | no | no | no | no | `RC-1`–`RC-9` renombradas y retiradas del inventario de §19 |
| `M-9` | MEDIO | **`CORREGIDO_EN_F4`** | D81 | sí | no | no | no | no | el §6.2 de la directiva es el contrato de `A3`; §15.2 desglosado |
| `m-1` | MENOR | **`CORREGIDO_EN_F4`** | nota al pie de `O15` | sí | no | no | no | no | reancla la cifra SIN tocar la resolución |
| `m-2` | MENOR | **`CORREGIDO_EN_F4`** | §2 del registro | sí | no | no | no | no | la nota de procedencia precede a la sección de `O16` |
| `m-3` | MENOR | **`HISTORICO_NO_APLICABLE`** | §5.2 | no | no | no | no | no | hecho confirmado, juicio NO asumido: es preferencia de diseño |
| `m-4` | MENOR | **`CORREGIDO_EN_F4`** | D75 | sí | no | no | no | no | `U5a` y `U5b` rotuladas en §18 |
| `F-01` | MEDIO | **`PRESION_LISTA_PARA_F5`** | D93 · PN-14 | sí | **PN-14** | `01-PROCESOS.md` L434 · `00-CIRCUITOS.md` L166, DESPUÉS de F5 | no | no | la cadena está también en `b.16` L895 y `a.6` L495, material APROBADO: corregir sólo el kernel cambiaría el derivado dejando la fuente. `PN-14` lleva la sustitución a (a) y (b); F6 ejecuta después |
| `F-02` | MEDIO | **`EXTERNO_CON_PROPIETARIO`** | `SIS` · F6 | no | no | `esquemas/proceso.yaml`: `ref_a: capacidad` con sufijo `:` opcional tipado, y `OWNER` movido a un campo de AUTORIDAD | no | no | **el vocabulario ya está escrito y §19 lo recoge** (`I-13`): capacidad base de las quince · sufijo `:<variante>` opcional y tipado · `/` NO válido · `capacidad_productora` con la misma referencia · `OWNER` no es capacidad. F6 no decide nada |
| `F-03` | MEDIO | **`CORREGIDO_EN_F4`** | D83 | sí | no | no | no | no | fases de instalación renombradas a `INS-0`…`INS-7` |
| `F-04` | MEDIO | **`EXTERNO_CON_PROPIETARIO`** | `ENC` con `SIS` · F6 | no | no | `05-ESCENARIOS.md` L181 y su prueba `T75` | no | no | `grado_inicial: alta` y su comprobación en `T75` |
| `F-05` | MENOR | **`CORREGIDO_EN_F4`** | D86 | sí | no | instancias en `circuitos/` — OPTATIVO, `00-CIRCUITOS` L238 lo desactiva | no | no | §15.7 registra la excepción de `C5`; **§8.0 declara QUÉ VIAJA** —el source change, el dosier de certificación, el resultado por fuente y la convergencia—, que es cosa distinta del campo `checkpoint:` de esos handoffs (`I-24`: la columna decía «qué checkpoint viaja», y §19 lo dice bien). Las tres condiciones de cierre, cumplidas |
| `F-06` | MENOR | **`EXTERNO_CON_PROPIETARIO`** | `DIS` · F6 | no | no | `circuitos/DIS-handoffs.md` L137 | no | no | anclar el `cuando` de `dis-a-ver` a una estación del ciclo |
| `F-07` | MENOR | **`EXTERNO_CON_PROPIETARIO`** | `SIS` con el Owner · F6 | no | no | `docs/owner/*` + `exclusiones.yaml` | no | no | campo `autoridad:` en `docs/owner/`, comprobado por validador |
| `F-08` | MENOR | **`EXTERNO_CON_PROPIETARIO`** | el Owner · F5 | no | sí · sin PN | no | no | no | nota de vigencia sobre la materialización multirrepo |
| `F-09` | MENOR | **`CORREGIDO_EN_F4`** | §8.4 | sí | no | no | no | no | «provisional» conservado y procedencia citada |
| `F-10` | MENOR | **`EXTERNO_CON_PROPIETARIO`** | `ENC` · F6 | no | no | `entrada/03-FORMAS.md` L3 | no | no | la cabecera de `03-FORMAS` deja de afirmar «uno por clase» |
| `F-11` | MENOR | **`EXTERNO_CON_PROPIETARIO`** | `SIS` · F6 | no | no | `entrada/05-ESCENARIOS.md` L5 | no | no | la cabecera de `05-ESCENARIOS` enumera lo que contiene |
| `F-12` | MENOR | **`CORREGIDO_EN_F4`** | índice y checkpoint | sí | no | no | no | no | los documentos 15, 16 y 17 son inmutables; se reanclan sus proyecciones |

```text
RECUENTO DERIVADO DE LAS 43 FILAS, no al revés — RECALCULADO tras la corrección del gate
de cierre. Ninguna de estas cifras se ha copiado: todas salen de extraer los
identificadores, la severidad y el estado primario de la tabla de arriba y contarlos.

  CORREGIDO_EN_F4             31   la corrección está escrita y no queda nada por decidir
  PRESION_LISTA_PARA_F5        2   `B-2` (`PN-13`) y **`F-01` (`PN-14`)**. Las dos tienen su
                                   arquitectura corregida; lo que queda es una enmienda que
                                   sólo el Owner puede aprobar
  CONTRATO_COMPLETO_PARA_F6    2   `M-5` y `M-6`. F4 corrigió la ambigüedad y dejó el
                                   contrato determinado; el elemento sólo se construye en F6
  EXTERNO_CON_PROPIETARIO      7   su sede está fuera de F4: kernel, `docs/owner/` o el
                                   propio documento del gate. Con propietario y fase en §19.
                                   **Eran OCHO: `F-01` deja de serlo**
  HISTORICO_NO_APLICABLE       1   `m-3`: el hecho está confirmado y el juicio NO se asume
                              ───
  TOTAL                       43   suma exacta de los cinco estados

  UN ESTADO PRIMARIO POR ID, y los cinco mutuamente excluyentes. 43 ids DISTINTOS.
  A11 no aparece: absorbido en `M-8`, sin condición de cierre propia
  A14 no aparece: el gate lo declaró AJENO a F4 — limitación aceptada con procedencia

QUÉ SE MOVIÓ EN ESTA TANDA, Y POR QUÉ

  `F-01`   EXTERNO_CON_PROPIETARIO → **PRESION_LISTA_PARA_F5**. Su remedio, como estaba
           escrito, no alcanzaba `b.16` L895 ni `a.6` L495 —material APROBADO—, luego
           cambiaba el derivado dejando la fuente. Es `PN-14` y `D93`.
           **Conserva `requiere_f6`**: el kernel se corrige DESPUÉS de F5, no en su lugar
  `B-2`    sigue siendo PRESION_LISTA_PARA_F5 por `PN-13`, y **su parte arquitectónica queda
           corregida**: `D90` cierra la mitad `PLT` contra `C7:80-92`, que nunca fue materia
           del Owner. El residuo es sólo `DOM`/`SEG`/`DIS` en `SIS` e `INV`
  `M-5` `M-6`  conservan CONTRATO_COMPLETO_PARA_F6, y ahora su contrato está **también en
           §17**, que es la sede que F6 lee y la mitad literal del cierre de `M-6`
  `A2` `A4` `A7` `A8` `G-3` `F-02`  eran las otras seis FALLIDAS del gate de cierre.
           Conservan su estado primario y **su condición de cierre pasa a cumplirse**:
           `D89`, `I-19`, `D95`, `D88`, §18 e `I-13` respectivamente

POR SEVERIDAD ORIGINAL, Y QUÉ FUE DE CADA GRUPO — derivado por cruce, no escrito

  BLOQUEANTE   4 filas ·  4 distintos   3 CORREGIDO_EN_F4 · 1 PRESION_LISTA_PARA_F5 (`B-2`)
  GRAVE        6 filas ·  6 distintos   6 CORREGIDO_EN_F4
  MEDIO       20 filas · 20 distintos  15 CORREGIDO_EN_F4 · 2 CONTRATO_COMPLETO_PARA_F6
                                        1 PRESION_LISTA_PARA_F5 (`F-01`)
                                        2 EXTERNO_CON_PROPIETARIO
  MENOR       14 filas · 13 distintos   7 CORREGIDO_EN_F4 · 5 EXTERNO_CON_PROPIETARIO
                                        1 HISTORICO_NO_APLICABLE  (`A11` absorbido en `M-8`)
              ── filas 44 · distintos 43

ATRIBUTOS SECUNDARIOS, QUE NO ENTRAN EN NINGÚN TOTAL

  arquitectura corregida    35 sí · 8 no. Los ocho «no» son los EXTERNOS puros y `m-3`
  requieren F5               3   `B-2` (`PN-13`) · **`F-01` (`PN-14`)** · `F-08` (documento
                                 del Owner, sin `PN`). **Sube por `PN-14`**
  requieren F6              11   `B-2` `M-5` `M-6` **`F-01`** `F-02` `F-04` `F-05` `F-06`
                                 `F-07` `F-10` `F-11`. **`F-01` NO sale**: su trabajo de
                                 kernel sigue existiendo, y se ejecuta DESPUÉS de F5
  bloquean F5                0   lo que impide F5 es el VEREDICTO del gate, no un hallazgo
  bloquean F6                1   `B-2`, y ACOTADO: sólo la composición de `INS-5` y de `A9`

REQUERIR TRABAJO FUTURO NO ES «F4 NO RESOLVIÓ SU ARQUITECTURA». `B-2`, `F-01`, `M-5` y `M-6`
tienen su arquitectura escrita y cerrada; lo que queda de ellos son dos aprobaciones del
Owner y tres construcciones, no una decisión de diseño pendiente.

Y LO QUE ESTA MATRIZ NO DICE, Y HAY QUE DECIR: **que las 43 filas estén cerradas NO cierra
`F4c`.** Esta tanda la aplicó quien la recibió, por décima vez. El veredicto vigente sigue
siendo el del gate de cierre, y lo que hace falta es un juicio independiente sobre ESTA
tanda — con la cobertura que al anterior le faltó.
```

### Lo que la tanda comprobó mecánicamente

> **Y lo que el gate de cierre demostró de esta lista, que es lo que importa.** Cuatro de
> estas treinta comprobaciones **estaban en verde y no debían estarlo**, y son exactamente
> las que la corrección siguiente tuvo que rehacer: «UN predicado `abierta(tx)`» —el censo
> era falso en dos de siete entradas y §2.6.4 lo redeclaraba (`I-09`)—, «vía declarada para
> cada participante» —`b.16` da a `DOM` y a `SEG` una segunda participación que ningún
> proceso instancia (`I-08`)—, «los cuatro macrocircuitos con sus **doce** campos» —el
> encargo pedía CATORCE, y faltaban `proceso` y `handoffs` (`I-21`)— y «once presiones
> derivadas de sus cabeceras», que era cierta entonces y no lo es ahora. **Una comprobación
> mecánica que se declara en verde sin ejecutarse es peor que no tenerla**, y por eso la
> batería de la tanda siguiente se ejecuta y se publica.

```text
30 COMPROBACIONES, 30 EN VERDE — declaradas por la NOVENA tanda, y CUATRO de ellas
refutadas después por el GATE DE CIERRE. Se conservan como lo que fueron
  cinco estados alcanzables · dos terminales y sólo dos · ningún no terminal sin sucesor ·
  restauración verificada byte a byte ANTES de `abandonada` · ninguna mezcla parcial
  publicable · la intención histórica íntegra · recuperación local y reinicio remoto
  diferenciados · gobierno Git con sede y contrato · UN predicado `abierta(tx)` · quince
  capacidades · diez procesos derivados de `01-PROCESOS.md` · los cuatro macrocircuitos con
  sus doce campos · vía declarada para cada participante · doce identificadores documentales
  distintos · once presiones derivadas de sus cabeceras · `D1`–`D86` sin hueco · vallas
  balanceadas · cero párrafos duplicados · cero contradicciones vigentes conocidas
```

## GATE DE CIERRE INDEPENDIENTE — emitido, y NO superado

```text
QUÉ ES              la verificación independiente de si la arquitectura vigente es SUFICIENTE
                    PARA F5, sobre el rango `7e99388…0a4b3a0` y la resolución declarada de los
                    43 hallazgos. TRES agentes con contexto limpio: `G` y `H` en paralelo sin
                    verse, e `I` sobre los dos dictámenes ya cerrados. `I` no resolvió por
                    mayoría: corrigió a `G` en `A2`, a `H` en `A10` y `F-08`, reubicó cuatro
                    citas y rechazó un hallazgo entero.

VEREDICTO           **INSUFICIENTE PARA F5.** `F4c` NO se cierra y sigue ABIERTA.

POR QUÉ · RAZÓN 1   LA COBERTURA NO CUMPLE. CATORCE fuentes obligatorias —3 420 líneas, el
                    10,9 % del corpus— sin lectura sustantiva. DIEZ son de las diecinueve que
                    el PRIMER gate ya omitió. Y el **documento 15** —la tercera revisión
                    independiente, donde vive la causa original de `D64`–`D68`— estaba
                    asignado a los DOS revisores y **no lo abrió ninguno**.

POR QUÉ · RAZÓN 2   DIEZ de las 43 filas son FALLIDAS: `A2` `A4` `A7` `A8` `B-2` `G-3` `M-5`
                    `M-6` `F-01` `F-02`. Dos de severidad BLOQUEANTE original y dos GRAVES.

HALLAZGOS           **28 consolidados**: 0 BLOQ · 8 GRAVES · 8 MEDIOS · 12 MENORES.
                    **SEIS los introdujo o los perpetuó la propia tanda de corrección.**
                    UNO rechazado. DOS son del propio adjudicador.

LO ÚNICO QUE EXIGE  el plano de `estado/cuarentena/<TX>/`, que `D79` autorizó y §2.6.10
DECIDIR DISEÑO      descarta once líneas después. Son cinco líneas. Todo lo demás se cierra
                    propagando material que el corpus ya tiene escrito.

QUÉ NO SE TOCÓ      NADA. Ningún hallazgo corregido, `11-ARQUITECTURA-INTEGRADA.md` intacto,
                    `D1`–`D86` y `O1`–`O16` intactas, documentos 15, 16 y 17 inmutables.
```

### Matriz de las 43, adjudicada por `I`

```text
SUPERADAS        32
FALLIDAS         10   A2 · A4 · A7 · A8 · B-2 · G-3 · M-5 · M-6 · F-01 · F-02
NO APLICABLE      1   m-3, con causa demostrada
                 ──
                 43   La derivación de `I` desde el checkpoint CONFIRMA la cifra publicada:
                      43 ids distintos, un estado primario cada uno, 31·1·2·8·1 = 43
```

## TANDA INTEGRADA DE CORRECCIÓN DEL GATE DE CIERRE — cerrada, sin publicar

```text
QUÉ ES              la corrección de los 28 hallazgos consolidados `I-01`–`I-28` del GATE DE
                    CIERRE INDEPENDIENTE (documento 18), más la fila `A7` —una de las DIEZ
                    FALLIDAS, que no lleva número `I-nn` porque es fila de la matriz y no
                    hallazgo nuevo—. Es la **DÉCIMA** tanda de corrección de `F4c`.

QUÉ NO ES           un veredicto. **Lo aplicó quien lo recibió**, por décima vez, y eso no
                    certifica nada. `F4c` sigue **ABIERTA** y el veredicto vigente sigue
                    siendo **INSUFICIENTE PARA F5**.

QUÉ NO SE HA HECHO  no se ha encargado otro gate · no se ha iniciado F5 ni F6 · no se ha
                    iniciado PesquerApp · **no se ha redactado ninguna enmienda normativa** ·
                    (a), (b), `E1`, `E2`, `K-1`, `C4` y `C7` **intactos** · los documentos
                    15, 16, 17 y 18 **intactos** · `D1`–`D86` conservan su texto, con la
                    ÚNICA excepción de restaurar `D67` al de `7e99388` · `O1`–`O16` intactas
                    · **NADA de `kernel/operativo/`, `packs/` ni `tooling/`** cambia, salvo
                    la evidencia DERIVADA que el runner republica.

DECISIONES          **`D87`–`D95`**, todas revisoras. Ninguna reescribe una anterior.
                      D87  la cuarentena OPERACIONAL, que revisa `D79`
                      D88  las cinco piezas del marcador de `deriva`, que completan `D78`
                      D89  la capa B, el censo de `abierta(tx)`, y el resumen de procesos
                           que la reescritura de `D67` llevaba
                      D90  el reparto Git de `C7`, citado y no reescrito
                      D91  la autoridad para abrir campañas, DERIVADA de los aspectos
                      D92  `<CAP>:revision` como contrato completo para F6
                      D93  `F-01` reclasificado, y `PN-14`
                      D94  las TRECE condicionales de `§5.18`
                      D95  los cinco CAMPOS de procedencia en la sexta sede

PRESIONES           **DOCE vigentes**: `PN-1`, `PN-2`, `PN-3`, `PN-6` a `PN-14`. `PN-4`
                    retirada, `PN-5` fusionada en `PN-3`. Sin renumerar. El total se DERIVA
                    de las cabeceras `## \`PN-` menos las dos marcadas.
                    **`PN-14` es la única que esta tanda añade**, y sale de reclasificar
                    `F-01`: `DIS/Reconstruccion` está en `b.16` L895 y `a.6` L495, que son
                    material APROBADO. **No se redacta su enmienda.**

QUÉ CAMBIA EN LA    `F-01` pasa de EXTERNO a PRESIÓN F5 · los externos bajan de OCHO a SIETE ·
MATRIZ DE LOS 43    `requiere_f5` sube de 2 a 3 · `requiere_f6` conserva `F-01` · `B-2` sigue
                    siendo presión F5 por `PN-13` **con su parte arquitectónica corregida** ·
                    `M-5` y `M-6` conservan CONTRATO_COMPLETO_PARA_F6.
                    **43 ids distintos, un estado primario cada uno, ningún estado compuesto,
                    y el total DERIVADO de las filas.**

VERIFICACIÓN        una batería propia de **TREINTA comprobaciones que DERIVAN su
MECÁNICA PROPIA     resultado del árbol**, no de lo que el texto afirma de sí mismo.
                    **No es un gate y no certifica nada**: la escribió quien aplicó la
                    corrección. Lo que hace es volver REFUTABLE cada afirmación de la tanda.
                    Es la lección de la tanda anterior, cuyas «30 comprobaciones, 30 en
                    verde» incluían CUATRO que no debían estarlo y ninguna se había ejecutado.
                    Vive en `docs/evolucion/verificacion/`, y su alcance y sus límites están
                    declarados abajo.

LÍMITE DEL ENTORNO  **[HISTÓRICO · SUPERADO, ver ESTADO VIGENTE abajo]** la batería canónica
[HISTÓRICO]         se ejecutó con **Python 3.10.12**, que era lo único disponible en aquella
                    máquina —no había 3.11+ instalable sin `sudo`—. `comprobar_arranque`
                    (`T148`), `comprobar_fuentes` (`T159`) y las pruebas de `workspace`
                    fallaban por `tomllib`, que exige **3.11+**. **Es `A14`**, que el gate
                    final declaró AJENO a F4, con propietario `PLT` y fase F6. **No se tocó
                    el tooling para sortearlo.** Resultado de entonces: **9/13**.

Y UNA CONSECUENCIA  **[HISTÓRICO · SUPERADO]** `comprobar_evidencia` (`T158`) quedaba
DE ESE LÍMITE       FALLIDA, y **no era un defecto de contenido**: la evidencia publicada de
[HISTÓRICO]         `comprobar_fuentes` declaraba **291 ficheros** y el corpus vigente daba
                    **293**. La cifra la publica `T161`, que SUPERABA por sí sola; lo que
                    impedía republicarla es que `comprobar_fuentes` salía con código 1 **por
                    `T159`**, y `registrar_evidencia` —correctamente— no publica una ejecución
                    que falla. Se anticipó que **en una máquina con Python 3.11+ una sola
                    ejecución la reconciliaría**. Así fue.

════════════════════ ESTADO VIGENTE ════════════════════

SNAPSHOTS          publicados y PRESERVADOS. Son fotografías de un momento, no «la
PUBLICADOS         candidata actual»:
                     r2 · 1b588acafb5acf68b11fcc9f544de9fc7e8fddb2
                          publicación de la tanda y arreglo de `N158g`
                     r3 · 65cab5415e002f5dc5f66dbab5b6ae5f3f77bebd
                          portabilidad de la batería, `G-23`, `G-24` y vigencia del
                          checkpoint
                   Deja de ser cierto que «nada está publicado». Y **`r2` NO es la candidata
                   vigente**: su árbol no contiene las correcciones que `r3` incorpora.

ÁRBOL VIGENTE      **el árbol que contiene ESTE checkpoint**, que incorpora las correcciones
                   posteriores a los snapshots de arriba.
                   Su SHA y su rama remota **NO se escriben aquí**: se DERIVAN de Git, y
                   escribirlos crearía una segunda fuente de verdad que además envejece a
                   cada commit —y un checkpoint que registrase el SHA de su propio commit
                   necesitaría otro commit para corregirlo, y así sin fin.
                   Antes del gate se comprueban con:
                     git rev-parse HEAD
                     git ls-remote origin

VALIDACIÓN         ejecutada con **Python 3.11.16**, y **repetida después de forma
CANÓNICA           independiente con el mismo resultado**:
                     13/13 validadores
                     57/57 pruebas de workspace
                     67 infracciones detectadas · 0 NO detectadas
                     `T158` SUPERADA · `T159` SUPERADA · `T148` SUPERADA
                     `T161` = **293 ficheros recorridos**
                   Lo que el bloque histórico anticipaba se cumplió: una sola ejecución
                   reconcilió la cobertura, y con ella `T158`.

DETERMINISMO       `N158g` derivaba su fixture de la cifra PUBLICADA, luego dependía del
DE `N158g`         orden del manifiesto —`negativos` corre antes que `fuentes`— y dos
                   ejecuciones seguidas no coincidían byte a byte. Corregido en `1b588ac`:
                   la cifra se deriva del **corpus vigente** por la definición canónica
                   `comprobar_fuentes.ficheros_recorridos`. **Demostrado partiendo de
                   evidencia inicialmente caducada**: la primera ejecución ya converge y la
                   segunda es idéntica, sin tercera.

EXCEPCIÓN EXACTA   deja de ser cierto que «`kernel/operativo/` está intacto». Lo que hay es
DEL KERNEL         una excepción NOMBRADA, y sólo ésta:
                     kernel/operativo/validadores/comprobar_negativos.py   código
                     kernel/.upstream-hash                                 huella reanclada
                     kernel/operativo/pruebas/evidencia/*                  derivada
                   Lo normativo —(a), (b), `E1`, `E2`, `C4`, `C7`— y el kernel operativo
                   SUSTANTIVO siguen intactos. `G-23` lo comprueba así, fichero a fichero,
                   sin exclusiones amplias.

BATERÍA PROPIA     tenía dos defectos que ESTA tanda cierra: calculaba mal la raíz y caía a
                   una ruta codificada de una máquina —luego en cualquier otro clon o
                   worktree comprobaba el repositorio del autor, no el que tenía delante—, y
                   `G-23` afirmaba «kernel intacto», que dejó de ser cierto en `1b588ac`.
                   Corregidos: raíz derivada de `__file__`, `G-23` con la excepción exacta y
                   `G-24` leyendo de verdad las catorce fuentes y las quince fichas por
                   nombre. **30/30 desde la raíz, desde otro cwd y desde un worktree
                   arbitrario.**

QUÉ PASA CON LOS   los hallazgos `I-01`–`I-28` y la fila `A7` tienen sus **correcciones
HALLAZGOS DEL      arquitectónicas APLICADAS**, en la tanda anterior. La corrección posterior
GATE               —`N158g`, portabilidad de la batería, `G-23`, `G-24` y este checkpoint—
                   **NO modifica ninguna de esas decisiones arquitectónicas**: toca
                   auditabilidad y vigencia, y nada más.
                   **Aplicar las correcciones NO las certifica.** Las aplicó quien las
                   recibió, y eso es lo que un gate independiente existe para juzgar.

LO QUE NO CAMBIA   **`F4c` sigue ABIERTA hasta el gate independiente, y `F5` sigue NO
                   AUTORIZADA.**

EL SIGUIENTE PASO  un **gate independiente sobre la candidata corregida**, con contexto
                   limpio. **No otra corrección aplicada por el mismo autor**: quien recibe
                   no puede seguir siendo quien aplica.

```

**La batería de esta tanda, y lo que NO comprueba.** Vive en
[`verificacion/README.md`](verificacion/README.md), con el detalle de sus treinta
comprobaciones y de sus tres límites declarados: **no ejecuta nada del protocolo** —no hay
runtime, ni esquema de `evento`, ni un fichero bajo `estado/`—, **no sustituye al gate** —no
juzga suficiencia para F5— y **no cubre el corpus por lectura**: comprueba que las catorce
fuentes y las quince fichas existen, no que alguien las haya leído. Que un gate posterior las
LEA sigue siendo su condición mínima, y ninguna comprobación mecánica la sustituye.

## Siguiente acción exacta

```text
0  UN GATE INDEPENDIENTE SOBRE   **NO lo encarga esta tanda, y no está encargado.** La
   ESTA DÉCIMA TANDA              corrección la ha aplicado quien la recibió, otra vez, y eso
                                  no certifica nada. Lo que hace falta es un juicio
                                  independiente sobre ESTA tanda, y su condición mínima es la
                                  que al anterior le faltó: **cubrir las CATORCE fuentes
                                  obligatorias que nadie abrió** —empezando por
                                  `15-TERCERA-REVISION-INDEPENDIENTE-F4C.md`, asignada a los
                                  dos revisores y leída por ninguno; después las DIEZ de las
                                  diecinueve que el primer gate ya omitió: `diseno/00` `01`
                                  `02` `04` `05`, `C2`, `C3`, `entrada/00` `02` `04`; más
                                  `C4`, `E1` y `E2` íntegro— y **leer íntegras las TRECE
                                  fichas de capacidad** que se cubrieron por `grep`, o
                                  declarar por qué la cobertura por atributos basta.
                                  **Sin esto no hay gate, hay una muestra.**

1  QUÉ HA CORREGIDO ESTA          los 28 hallazgos `I-01`–`I-28`, más `A7`. Las ocho GRAVES,
   TANDA, Y CONTRA QUÉ            por el orden en que el adjudicador las puso: `I-03` la capa
                                  B —cierra `A2`—; `I-04` el EJECUTOR contra `C7:80-92`
                                  —cierra la mitad `PLT` de `B-2`—; `I-07` el gate de `INS-5`
                                  en §18 —cierra `G-3`—; `I-06` `DSP` y `ENC` en §17 —cierra
                                  `M-5` y `M-6`—; `I-05` §14; `I-01` la cuarentena; `I-02` el
                                  marcador de `deriva`; `I-08` la revisión de `DOM`/`SEG`.
                                  La ÚNICA decisión de diseño que el gate identificó —el
                                  plano de la cuarentena— se tomó en `D87`: **no crea una
                                  tercera ubicación**, la retira y usa el plano operacional
                                  que ya existe.

2  QUÉ VIGILAR                    lo mismo que el gate anterior mandó vigilar, y con más
                                  motivo: **que la undécima tanda NO la aplique quien la
                                  reciba sin un gate posterior**. Ésta es la décima, y las
                                  dos veces que alguien ha mirado ha aparecido algo que la
                                  corrección introdujo — SEIS de los veintiocho del gate de
                                  cierre eran de esa clase, y esta tanda ha tocado cinco
                                  sedes más de §8 y toda la capa B.

3  QUÉ NO SE HA HECHO, Y NO       no se ha encargado el gate independiente · no se ha
   DEBE HACERSE SIN DECIDIRLO     iniciado F5, F6 ni PesquerApp · no se ha redactado ninguna
                                  enmienda de `b.16`, de (a) ni de (b) · no se ha tocado
                                  `C7` · **no se ha hecho merge en `redesign/kernel-2.0`**.

   Y LO QUE SÍ SE HA HECHO,       **hay candidatas PUBLICADAS y preservadas** —`r2` y `r3`—,
   PARA QUE NO SE LEA DE MENOS    luego «nada se ha publicado» ya NO es cierto.
                                  **El kernel operativo SUSTANTIVO no se ha tocado**, y la
                                  excepción es exacta y se nombra:
                                    kernel/operativo/validadores/comprobar_negativos.py
                                    kernel/.upstream-hash
                                    kernel/operativo/pruebas/evidencia/*
                                  Decir «no se ha tocado nada de `kernel/operativo/`» sería
                                  falso desde `1b588ac`.

5  QUÉ LLEVAR AL OWNER            las **DOCE** presiones de §16, con `PN-1` bloqueando todo el
                                  estado durable y **`PN-14` como la única que esta tanda
                                  añade**. `I-26` está corregido: el campo ALCANCE de `PN-13`
                                  ya no está truncado.
                                  **Y `F-08`, que es trabajo de F5 y NO es presión normativa**
                                  —`IDEAS` se declara a sí mismo «no es una especificación
                                  cerrada»—: su registro vive en §19 y en la matriz, con
                                  `requiere F5 · sí · sin PN`. **Corregido por `I-28`**: este
                                  punto decía «las ONCE presiones de §16» y un Owner que
                                  siguiera sólo esta línea no habría visto `F-08`.

4  EL SIGUIENTE PASO              **el GATE INDEPENDIENTE sobre el ÁRBOL VIGENTE** —no sobre
                                  `r2`, cuyo árbol es anterior a las correcciones de
                                  portabilidad—. Su SHA se deriva con `git rev-parse HEAD` y
                                  `git ls-remote`, no de una cifra escrita aquí.

6  DÓNDE PARAR                    antes de redactar `(g)`, antes de crear `C8`, antes de tocar
                                  `C7` o el kernel operativo SUSTANTIVO, y antes de iniciar
                                  PesquerApp.
                                  `O15` dice qué será cuando ocurra, no que ocurra ahora.
```
