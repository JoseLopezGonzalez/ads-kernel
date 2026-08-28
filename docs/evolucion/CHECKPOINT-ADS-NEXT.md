# CHECKPOINT — ADS NEXT

> Registro persistente y reanudable de la iniciativa. Formato de
> [`a.10`](../rediseno/a-CAPACIDADES-APROBADA.md), copiable desde
> [`plantillas/CHECKPOINT.md`](../../kernel/operativo/plantillas/CHECKPOINT.md).
> **Basta decir «Continúa»**: la siguiente acción exacta está al final.

> **Estado de la fase, en una línea:**
> **La TERCERA REVISIÓN INDEPENDIENTE devolvió INSUFICIENTE PARA F5, y sus hallazgos
> reproducibles están CORREGIDOS en una tanda integrada. F4c sigue ABIERTA: quien corrigió es
> quien recibió, y eso no la cierra.**
>
> Sólo la cerraría un veredicto de SUFICIENCIA emitido por un revisor independiente **sobre
> este resultado corregido**. Ese veredicto no existe, y esta pasada **no lo pide**.
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
CHECKPOINT — ADS-NEXT/10 · SIS/evolucion
actualizado: 2026-08-27
metodo:      SIS/Evolucion · TERCERA REVISIÓN INDEPENDIENTE EMITIDA · VEREDICTO
             INSUFICIENTE PARA F5 · F4c ABIERTA
based_on:    docs/evolucion/09-SINTESIS.md@56ea196 + su addendum
             docs/evolucion/10-CRITICA-INDEPENDIENTE-F3.md@56ea196
             docs/evolucion/11-ARQUITECTURA-INTEGRADA.md   corregida
             docs/evolucion/12-CRITICA-INDEPENDIENTE-F4.md
             docs/evolucion/13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md
             docs/evolucion/14-DEVOLUCION-TECNICA-PREVIA-F4C.md
             docs/evolucion/15-TERCERA-REVISION-INDEPENDIENTE-F4C.md   VEREDICTO,
                                                             corregido por D64–D68
             docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md   O7–O14 · O15 · O16 · D16–D22 ·
                                                             D23–D33 · D34–D45 · D46–D51 ·
                                                             D52–D54 · D55–D57 · D58–D59 ·
                                                             D60–D61 · D62 · D63 · D64–D68 ·
                                                             D69–D70
             kernel/VERSION@2.0.0-alpha.9 · kernel/KERNEL.md@1.5.0
freshness:   vigente
last_meaningful_event: la SEGUNDA revisión independiente devuelve F4 con veredicto de
             INSUFICIENCIA —dos BLOQUEANTES, siete GRAVES y catorce hallazgos nuevos— y sus
             correcciones quedan aplicadas (2026-08-27)
procedencia_de_la_critica: los hallazgos y el veredicto de las críticas de F3 y de las DOS
             de F4 los EMITIÓ un revisor independiente que no las escribió. La SEGUNDA de F4
             la emitió además un revisor que TAMPOCO aplicó la primera. Los ficheros que los
             recogen los TRANSCRIBIÓ Y APLICÓ el autor material de esas fases. Aplicar una
             crítica NO equivale a autocertificarse, y NO prueba que esté bien resuelta.
             LA PRUEBA DE QUE ESTO IMPORTA: dos de los hallazgos de la segunda devolución son
             defectos que la PRIMERA CORRECCIÓN introdujo o no vio
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
pregunta_pendiente: ninguna. Las DIEZ presiones normativas vigentes son materia de F5,
             no preguntas
siguiente:   CUARTA REVISIÓN INDEPENDIENTE sobre el resultado corregido, por quien NO
             escribió F4 ni aplicó NINGUNA de sus tandas. Los 22 hallazgos reproducibles
             están corregidos, y eso NO los da por bien resueltos: quien corrigió es quien
             recibió. F5 NO arranca sin un veredicto de SUFICIENCIA
falta_para_cerrar_la_capa:
  · F4c ESTÁ ABIERTA. Hubo un veredicto INDEPENDIENTE Y EXPLÍCITO de INSUFICIENCIA —dos
    BLOQUEANTES y ocho GRAVES—, sus hallazgos reproducibles están corregidos, y **eso no la
    cierra**: sólo la cierra un veredicto de SUFICIENCIA sobre el resultado corregido,
    emitido por quien no lo escribió. Ese veredicto no existe.
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
  · DIEZ PRESIONES NORMATIVAS VIGENTES —PN-1, PN-2, PN-3, PN-6 a PN-12; PN-4 retirada y
    PN-5 fusionada—. PN-1 —la sección (g)— BLOQUEA todo el estado
    durable, y ahora decide MÁS: fsync, regla de commit, sellado, identidad y regla de
    lectura. PN-2 y PN-3 son la misma y sólo bloquean que el sistema abra auditorías solo.
    PN-6 reinterpreta O12. PN-7 (b.14 dice «completar o revertir»), PN-8 (VER no está en la
    ruta AUD), PN-9 (predicados de obligación de b.3 — probablemente ninguna materia, y F5
    debe CONFIRMARLO) y PN-10 (O11 dice «estado durable») son NUEVAS. PN-4 RETIRADA y PN-5
    FUSIONADA en PN-3. Ninguna renumerada, y ninguna redactada
  · NADA CONSTRUIDO: ni kernel, ni runtime, ni tooling, ni esquemas, ni adaptadores, ni
    plantillas, ni packs, ni validadores, ni migraciones. Las correcciones son DISEÑO
    CORREGIDO, no diseño implementado
  · NADA PROBADO: las 42 filas de la tabla adversarial de §2.6.7, las 9 ventanas R1–R9 de
    §2.6.9, los 11 escenarios
    negativos de §11.5 y los 12 escenarios de §14 están ESCRITOS. Ninguno ejecutado
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
F4c CRÍTICA INDEPENDIENTE    TRES devoluciones, EMITIDAS por revisores y auditores que no
                             escribieron F4, TRANSCRITAS y APLICADAS por su autor material.
                             1ª  nueve bloques · 12-CRITICA-INDEPENDIENTE-F4.md · D23–D33
                             2ª  VEREDICTO DE INSUFICIENCIA por un revisor que TAMPOCO
                                 aplicó la primera: 2 BLOQUEANTES, 7 GRAVES, 14 nuevos ·
                                 13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md · D34–D45
                             3ª  DEVOLUCIÓN TÉCNICA PREVIA — auditoría externa de Codex
                                 sobre el ÁRBOL REMOTO REAL: 3 BLOQUEANTES, 2 GRAVES, 4
                                 MEDIOS, 2 MENORES · 14-DEVOLUCION-TECNICA-PREVIA-F4C.md ·
                                 D46–D51. NO es veredicto de suficiencia
                             Y TRES PASADAS TÉCNICAS posteriores, ninguna de ellas la
                             tercera revisión: la 1ª con dos BLOQUEANTES y un GRAVE
                             (`D52`–`D54`), la 2ª con tres GRAVES (`D55`–`D57`) sobre el
                             texto que la 1ª escribió, y una 3ª comprobación acotada
                             (`D58`–`D59`) sobre el texto de la 2ª y una 4ª (`D60`–`D61`)
                             sobre el texto de la 3ª, una 5ª (`D62`) sobre el de la 4ª y
                             una 6ª (`D63`) sobre la semántica de sellado.
                             DOS de los hallazgos de la 2ª devolución, TRES de la 3ª y LOS
                             TRES de la segunda corrección técnica son defectos que las
                             correcciones ANTERIORES introdujeron o no vieron.
                             ABIERTA: sólo la cierra un veredicto explícito de SUFICIENCIA
                             emitido por un revisor independiente sobre el resultado
                             corregido. Ese veredicto NO existe
F5  ENMIENDAS                DIEZ presiones normativas vigentes, enumeradas y sin redactar.
                             NO INICIADA
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

## Siguiente acción exacta

```text
0  LA TERCERA REVISIÓN         se emitió con veredicto INSUFICIENTE, y sus 22 hallazgos
   INDEPENDIENTE, YA          reproducibles están CORREGIDOS en una tanda integrada
   CORREGIDA                  (`D64`–`D68`, `PN-11`, `PN-12`). Lo siguiente es una CUARTA
                              revisión independiente SOBRE ESTE RESULTADO, por quien no
                              escribió F4 ni aplicó ninguna tanda. Que estén corregidos no
                              prueba que estén bien resueltos: es la octava vez que quien
                              recibe es quien aplica.

1  POR QUÉ NO SE CORRIGIÓ      por quien NO escribió F4 y NO aplicó NINGUNA de las dos
   EN LA MISMA PASADA          tandas de correcciones. La segunda devolución demostró por
                               qué esto no es ceremonia: DOS de sus hallazgos BLOQUEANTES
                               eran defectos que la PRIMERA CORRECCIÓN introdujo o no vio.
                               Sin un veredicto explícito de SUFICIENCIA, F4c no cierra y
                               F5 no arranca.

2  QUÉ MIRAR PRIMERO           §2.6 otra vez, y con el mismo método que funcionó: coger la
                               tabla adversarial de §2.6.7 —ahora TREINTA filas— e intentar
                               ejecutar cada una CONTRA EL TEXTO. Las dos que destaparon los
                               bloqueantes fueron X25 (caída de MÁQUINA, que ninguna fila
                               cubría) y X19 (Continúa tras un conflicto). Buscar la
                               siguiente ventana que la tabla no tiene.

3  QUÉ MIRAR DESPUÉS           las atribuciones. La segunda devolución encontró CINCO citas
                               falsas —b.3 dos veces, b.14, §20.8 y «a.9 literal»—
                               verificándolas una a una contra el fichero original. Ése es
                               el método: no leer lo que F4 dice que dice un contrato, sino
                               abrir el contrato.

4  QUÉ LLEVAR AL OWNER         las DIEZ presiones de §16. PN-1 bloquea todo el estado
                               durable. Cuatro son UNA FRASE cada una, y tres de ellas se
                               registran precisamente porque parecen obvias.

5  QUÉ VIGILAR                 la tentación de leer «corregido dos veces» como «ya está
                               bien». Dos devoluciones salen de F4 con CERO líneas
                               construidas, CERO escenarios ejecutados y CERO comprobaciones
                               independientes de las correcciones aplicadas.

6  DÓNDE PARAR                 antes de redactar una enmienda, y antes de tocar C7. Lo
                               primero es F5 y su puerta es el Owner; lo segundo es F6 y su
                               prescripción ya está escrita.
```

