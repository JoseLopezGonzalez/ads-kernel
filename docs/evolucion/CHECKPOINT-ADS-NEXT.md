# CHECKPOINT — ADS NEXT

> Registro persistente y reanudable de la iniciativa. Formato de
> [`a.10`](../rediseno/a-CAPACIDADES-APROBADA.md), copiable desde
> [`plantillas/CHECKPOINT.md`](../../kernel/operativo/plantillas/CHECKPOINT.md).
> **Basta decir «Continúa»**: la siguiente acción exacta está al final, en la **PRIMERA**
> sección titulada **«Siguiente acción exacta»**. Las que le siguen van rotuladas
> **HISTÓRICA**, conservan el texto anterior a cada gate y **no describen el estado vigente**.
> **Cuántas versiones históricas hay NO se escribe aquí** —esta cabecera ya caducó una vez por
> decir «la que le sigue» cuando ya eran dos—: se deriva con
> `grep -c '^## Siguiente acci[óo]n exacta' docs/evolucion/CHECKPOINT-ADS-NEXT.md`, menos la
> vigente, que es siempre la primera.

> **Estado de la fase, en una línea:**
> **El CUARTO GATE DE CERTIFICACIÓN devolvió `INSUFICIENTE PARA F5` y, además, EL PROPIO
> ADJUDICADOR LO DECLARÓ INVÁLIDO. `F4c` sigue ABIERTA y `F5` sigue NO AUTORIZADA. Y
> `C-L.5` pasa de CERTIFICADA a ABIERTA, por primera vez en cuatro gates.**
>
> Está en
> [`25-CUARTO-GATE-DE-CERTIFICACION-F4C.md`](25-CUARTO-GATE-DE-CERTIFICACION-F4C.md), con los
> tres dictámenes íntegros.
>
> **POR QUÉ ES INVÁLIDO, Y LA CULPA ES DEL COORDINADOR.** `O18` adoptó el SOBRE DE ANCLA como
> raíz de confianza externa y `O19` le añadió la huella de la sede canónica. **El emisor lo
> produjo bien**: `AA` verificó que todos sus campos reproducen byte a byte. **Lo que falló
> fue la ENTREGA**: el coordinador transcribió el sobre A MANO en cada encargo, y las cinco
> transcripciones **difieren en OCHO campos** —entre ellos el SHA-256 del derivador, que el
> propio Owner ordena entregar en la sede canónica—. La obligación del adjudicador
> **pre-rechaza con sus palabras exactas** la defensa que los dos dictaminadores ensayaron, y
> `AA` resolvió **contra los dos**.
>
> ```text
> 36 HALLAZGOS DISTINTOS    0 bloqueantes · 12 graves · 13 medios · 11 menores
> CLASIFICACIÓN             A · coherencia interna      23
>                           B · identidad               5      A+B  8
>                           C · actor privilegiado       0
>                           DECISIÓN DEL OWNER           0   ← no hay ninguna pendiente
> COBERTURA                 OBLIGATORIO − ASIGNADO = ∅ · **ASIGNADO − LEÍDO = 1**
>                           la regla de cierre excluye la suficiencia POR SÍ SOLA
> ```
>
> **LA CAUSA RAÍZ, y por primera vez hay una buena mitad.** `AA` dictamina que **NO es la
> misma causa que en los gates 21, 22, 23 y 24**: aquéllos fallaron porque la verificación
> estaba anclada dentro del objeto verificado, y **éste no** — los tres remedios del documento
> 24 **están aplicados y funcionan**, verificados uno a uno, y la sede real, el emisor y el
> derivador están protegidos. **Lo que falla es la ENTREGA, no la producción**, que es la
> mitad que nadie había podido medir hasta que el mecanismo existió.
> **Sí es la misma causa en el MÉTODO**: el perímetro se cerró y el `basename` se abrió **en
> el commit del propio remedio de `O19`**, quinta vez consecutiva.
>
> **`AA` dictamina que EL TRABAJO DEBE SEGUIR**, y expresamente **sin escribir una protección
> interna nueva**: «lo que falta es de resta y de disciplina». **No hay ninguna decisión
> pendiente del Owner**: los treinta y seis tienen remedio determinado dentro de `F4c`.
>
> **Y lo que SÍ quedó cerrado:** los tres remedios del documento 24 · los 54 agotamientos
> pasando las dos reglas · la reincidencia `U-02`/`X-06` **ROTA** —70 filas, cero
> discrepancias— · la **SEDE CANÓNICA cumple**, con `O1`–`O16` no reconstruidos, el diseño
> intacto en siete cotejos y **cero amplificación** en la proyección · `X-01` CERRADO Y
> GENERALIZA · y la exención histórica del checkpoint baja del 56 % al 32,5 %.

> **[ESTADO ANTERIOR · antes del CUARTO GATE DE CERTIFICACIÓN, documento 25]**

> **El Owner ha RATIFICADO el texto amplio de `O18` y ha ordenado una SEDE CANÓNICA para sus
> resoluciones: es `O19`. `F4c` sigue ABIERTA y `F5` sigue NO AUTORIZADA.**
>
> Su texto íntegro vive en
> [`docs/owner/ADS-OWNER-RESOLUCIONES.md`](../owner/ADS-OWNER-RESOLUCIONES.md), que es
> **la SEDE CANÓNICA**, y **no se copia aquí**. Desde `O19`, la sección 2 de
> [`DECISIONES-Y-CONTRADICCIONES.md`](../rediseno/DECISIONES-Y-CONTRADICCIONES.md) es una
> **PROYECCIÓN DERIVADA** de esa sede, y **una paráfrasis nunca puede ampliar el texto
> canónico**.
>
> ```text
> QUÉ RATIFICA        el texto AMPLIO de `O18`. Las condiciones omitidas y el reparto
>                     PERTENECÍAN a la resolución original: «la omisión está en la
>                     transcripción del coordinador, no en mi resolución original»
> QUÉ REVISA          la PROYECCIÓN INCOMPLETA de `O18` — NO su contenido y NO su diseño.
>                     `O18` no vuelve a someterse a elección
> QUÉ TRASLADA        la AUTORIDAD CANÓNICA, de la paráfrasis del coordinador a
>                     `docs/owner/`. La entrada corta de `O18` se conserva, sin editar,
>                     como REGISTRO HISTÓRICO de una transcripción incompleta
> QUÉ NO AUTORIZA     iniciar `F5`. Tampoco `F6` ni PesquerApp
> ```
>
> **Lo que esta tanda hace, y no es más que eso.** El sobre de ancla publica la sede —ruta,
> SHA-256 **leído del commit auditado**, identificadores DERIVADOS de ella y digest del texto
> canónico de cada resolución, cada uno con la receta que lo reproduce— y **se niega a emitir
> si la sede no está en el commit auditado, si falta un identificador exigido o si un digest
> no se deriva**. El inventario de integridad **que ya existía** se extiende a `docs/owner/`,
> y el registro ENLAZA a la sede sin ampliarla. **Ninguna protección interna nueva**, que es
> lo que el adjudicador del documento 24 ordenó expresamente.
>
> **Lo que NO cambia, y se dice.** `O19` corrige la PROCEDENCIA y la AUTORIDAD, **no el
> diseño**. Ningún hallazgo se declara SUPERADO, `M-04` no se cierra, y la limitación que
> `O18` declara de sí misma **sigue VIGENTE**: la sede traslada la autoridad, pero **no la
> hace mecánicamente verificable contra una fuente externa al sistema**. Eso es el
> verificador externo real de `F6`, y `O19` tampoco lo adelanta.

> **[ESTADO ANTERIOR · antes de la resolución `O19` del Owner. Se conserva ENTERO y NO
> describe el estado vigente.]**

> **Estado de la fase, en una línea:**
> **El TERCER GATE DE CERTIFICACIÓN devolvió `INSUFICIENTE PARA F5` sobre la candidata
> `21f1ccb`, y el gate es VÁLIDO. `F4c` sigue ABIERTA y `F5` sigue NO AUTORIZADA.**
>
> Está en
> [`24-TERCER-GATE-DE-CERTIFICACION-F4C.md`](24-TERCER-GATE-DE-CERTIFICACION-F4C.md), con los
> tres dictámenes íntegros. **Es el primer gate que recibe su ancla por un canal EXTERNO al
> repositorio**, como `O18` ordena.
>
> ```text
> 43 HALLAZGOS DISTINTOS    0 bloqueantes · 15 graves · 16 medios · 12 menores
> CLASIFICACIÓN de `O18`    A · coherencia interna          27   NO SE SOSTIENE
>                           B · identidad de la candidata   12   NO DEMOSTRADA
>                           C · actor privilegiado           0   correctamente declarada
>                           DECISIÓN DEL OWNER               4   ratificación de `O18`
> ```
>
> **`C-L.5` CERTIFICADA por CUARTA vez consecutiva**: las dos restas son ∅, las 67 filas del
> manifiesto no tienen una discrepancia y los **54 agotamientos** pasan las dos reglas uno a
> uno. **El gate NO falla por cobertura**, y el adjudicador lo dice expresamente.
>
> **Falla por `A` y por `B`. Y expresamente NO por `C`:** el Owner resolvió su fase, el
> contrato del verificador externo está completo, y el adjudicador **no encontró ni una sede
> que presente `(b)` como `(c)`**. Los dos hallazgos de clase `C` siguen vivos y **no se
> cuentan**.
>
> **LA RAÍZ, dicha en dos mitades, porque las dos son ciertas:**
>
> ```text
> LA MALA    es la misma causa de los gates 21, 22 y 23, y esta vez es PEOR, porque éste era
>            el gate que venía a curarla. `O18` es correcta —cambia la raíz de confianza en
>            vez de añadir otra comprobación interna—, pero su implementación puso la nueva
>            raíz DENTRO del mismo repositorio: con tres líneas de puerta trasera y sin
>            commitear, el emisor produce un sobre IDÉNTICO al honesto sobre un corpus
>            corrupto, y la batería da 38/38.
>            La circularidad no se cerró: se MOVIÓ, de `HEAD` a `emitir-sobre-de-ancla.py`
>
> LA BUENA   `O18` NO está refutada. Describe un CANAL, y ese canal SÍ es externo: el sobre
>            llegó a los ocho dentro del encargo, no leyéndolo del árbol, y los dos revisores
>            recibieron el mismo. **Lo externo es la ENTREGA. Lo interno es la PRODUCCIÓN.**
>            Es la distinción que ningún gate anterior podía aportar
> ```
>
> **Por eso el adjudicador recomienda que el trabajo SIGA**, y distingue esta situación de la
> del gate anterior: aquél pidió parar porque nadie había preguntado al Owner. Hoy se ha
> preguntado, la respuesta existe y **es la palanca correcta**. Lo que falla es la palanca, y
> el remedio está determinado en tres puntos. **Y ordena expresamente que NO se escriba una
> decimonovena protección interna.**
>
> **Lo único que vuelve al Owner es una RATIFICACIÓN**, no una elección: `O18` registra UNA
> condición previa para el verificador externo y seis sedes escriben TRES. La pregunta, con
> sus tres alternativas, está en §13 de la adjudicación de `X`, dentro del documento 24.
>
> **Y algo que `F4` sí puede hacer diga lo que diga el Owner:** `O17` declara su propia
> inverificabilidad con todas las letras y **`O18` no lo declara**. Esa declaración debe
> escribirse.

> **[ESTADO ANTERIOR · antes del TERCER GATE DE CERTIFICACIÓN, documento 24]**

> **EL OWNER HA RESUELTO LA ÚNICA CLASE `B` DEL SEGUNDO GATE DE CERTIFICACIÓN —la que NO era
> un hallazgo, sino LA RAÍZ—. Su respuesta es `O18`, del 2026-08-30, es una RESOLUCIÓN
> ESCALONADA, y con ella esa clase `B` queda RESUELTA y YA NO BLOQUEA. Esta tanda la está
> PROPAGANDO como `D108`, declarada DERIVADA. `F4c` sigue ABIERTA y `F5` sigue NO AUTORIZADA,
> porque APLICAR NO ES CERTIFICAR.**
>
> `O18` está registrada íntegra —con sus tres alternativas conservadas literalmente— en §2 de
> [`DECISIONES-Y-CONTRADICCIONES.md`](../rediseno/DECISIONES-Y-CONTRADICCIONES.md), y su
> propagación es **`D108`**, en §1 de ese mismo fichero. **Ninguna de las dos se reescribe ni
> se copia aquí: se leen allí, que es su sede.** `O1`–`O18` y `D1`–`D108` conservan su texto
> resolutivo; lo que reciben son punteros.
>
> **QUÉ ELIGIÓ EL OWNER, Y EN QUÉ ORDEN. La resolución es ESCALONADA: no eligió una de tres,
> dispuso las tres.**
>
> ```text
> (a) DECLARAR EL LÍMITE Y DEJAR      RECHAZADA EXPRESAMENTE. El Owner no retira la garantía
>     DE MEDIRLO                      ni acepta como solución que una alteración deliberada
>                                     sea indetectable
>
> (b) SOBRE DE ANCLA · raíz           ADOPTADA PARA CERRAR `F4c`, y declarada TRANSITORIA y
>     documental EXTERNA al árbol     EXPLÍCITAMENTE LIMITADA. Se entrega a cada revisor,
>     auditado                        dentro de su encargo, por un canal externo al
>                                     repositorio y ANTES de que empiece a leer
>
> (c) VERIFICADOR EXTERNO REAL        OBLIGATORIA EN `F6`, y CONDICIÓN PREVIA a la adopción
>                                     permanente de PesquerApp, a declarar ADS operativo y a
>                                     certificar adaptadores
> ```
>
> **POR QUÉ EN ESE ORDEN, Y NO EXIGIENDO (c) YA.** Exigir la infraestructura de (c) dentro de
> `F4c` produce un **bloqueo circular** que el Owner declara inaceptable: `F4c` bloquea `F5`,
> `F5` precede a `F6`, `F6` construiría el verificador, y `F4c` seguiría abierta esperando a
> que `F6` lo construyese. La cadena, escrita literal, está en `O18`.
>
> **QUÉ AÑADE EL SOBRE.** Una referencia que el árbol **no puede redefinir unilateralmente
> durante el gate**, la detección de que el árbol auditado no sea el encargado, y la detección
> de que el manifiesto se sustituyera después del reparto. El sobre **no sustituye** el
> manifiesto previo, ni los manifiestos de lectura, ni las dos restas, ni la revisión
> independiente, ni la adjudicación contra las fuentes: **es su raíz documental externa**.
>
> **QUÉ NO PROTEGE EL SOBRE, Y SE DICE. No se le atribuye más de lo que hace:**
>
> ```text
> compromiso del canal del Owner            robo de credenciales
> compromiso simultáneo del repositorio     reescritura autorizada de ramas remotas
>   y del coordinador                       manipulación del ejecutor externo
>                                           falsificación de identidad
>
> ESOS RIESGOS PERTENECEN AL VERIFICADOR EXTERNO DE `F6`, y siguen ABIERTOS hasta que exista
> ```
>
> **`M-04` NO SE DECLARA SUPERADA, y no puede declararlo esta tanda.** `O18` le da raíz de
> confianza a un mecanismo que no la tenía y fija la fase de cada garantía; no vuelve falsa la
> proposición «se puede construir un árbol defectuoso que pase la batería en verde». Quien
> puede decir si sigue habiendo uno es **un gate independiente con revisores que no hayan
> aplicado esta tanda**, y ese gate todavía no existe. **Ningún hallazgo del documento 23 se
> declara SUPERADO aquí.**
>
> **QUÉ NO AUTORIZA `O18`. No autoriza iniciar `F5`, ni `F6`, ni PesquerApp.** No cierra `F4c`
> por sí misma —eso lo hace un gate independiente—, no levanta ninguna condición `C-L` abierta
> y no deroga ninguna presión vigente. El criterio con el que ese gate tendrá que juzgar —las
> TRES afirmaciones `A`, `B` y `C`— tiene sede propia en **«El criterio del gate siguiente»**,
> justo antes de «Siguiente acción exacta».

> **[ESTADO ANTERIOR · antes de la resolución `O18` del Owner. Se conserva ENTERO para
> trazabilidad y NO describe el estado vigente: declara la clase `B` PENDIENTE DEL OWNER y
> manda parar a esperarla, y hoy está RESUELTA.]**

> **Estado de la fase, en una línea:**
> **El SEGUNDO GATE INDEPENDIENTE DE CERTIFICACIÓN devolvió `INSUFICIENTE PARA F5` sobre la
> candidata `e316396`. `F4c` sigue ABIERTA y `F5` sigue NO AUTORIZADA. Y esta vez el gate trae
> algo que ningún gate anterior había traído: LA RAÍZ, y una decisión que sólo puede tomar el
> Owner.**
>
> Está en
> [`23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md`](23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md), con los
> tres dictámenes íntegros. Lo emitieron **ocho agentes de contexto limpio** —revisor `S` como
> cadena `S1`–`S4`, revisor `T` como `T1`·`T2`·`T3`, en paralelo y sin verse, y el adjudicador
> `U`—, ninguno de los cuales participó en ningún gate anterior. **Ningún hallazgo se corrigió
> en esa pasada, y es deliberado.**
>
> ```text
> 49 HALLAZGOS DISTINTOS    0 bloqueantes · 17 graves · 19 medios · 13 menores
> CLASIFICACIÓN             A · corregible en F4c sin decidir arquitectura     48
>                           B · DECISIÓN EXCLUSIVA DEL OWNER                    1   ← LA RAÍZ
>                           C · trabajo futuro ya contratado                     0
> ```
>
> **LA RAÍZ, y por qué el trabajo se detiene aquí en vez de abrir una cuarta ronda.**
> `M-04` —«se puede construir un árbol defectuoso que pase la batería en verde»— ha fallado
> **tres gates consecutivos**. La tanda anterior respondió con QUINCE protecciones sistémicas;
> el adjudicador las midió una a una: **tres generalizan, tres son parciales y nueve siguen
> cerrando sólo su perímetro**, y **el coste marginal de encontrar la puerta siguiente no está
> subiendo**. Entonces encontró la causa, escrita en **§11.4 de este mismo corpus** y nunca
> llevada al Owner por ningún gate:
>
> ```text
> EL SUELO QUE QUEDA    si el runner miente, nada dentro del repositorio lo detecta.
> ABIERTO, Y SE DICE    Cerrarlo exige un verificador EXTERNO al repositorio, y eso NO se
>                       resuelve aquí. Se declara en vez de taparlo con una capa más de
>                       comprobación interna, que sólo movería la circularidad de sitio.
> ```
>
> **`M-04` no es satisfacible desde dentro de F4.** La batería vive dentro del repositorio que
> audita y decide si algo está «intacto» contra referencias que también viven ahí: `HEAD`, la
> revisión base, `kernel/.upstream-hash` y su propio README. **Quien puede escribir el
> repositorio puede escribir la referencia, y puede amputar la batería.** Tres gates han fallado
> contra un criterio que el corpus **había probado inalcanzable y dejado abierto**.
> **La pregunta al Owner, con sus tres alternativas y el coste de cada una, está en §13 de la
> adjudicación de `U`, dentro del documento 23.** El adjudicador recomienda expresamente cerrar
> los 48 de clase A y **NO escribir una decimosexta protección**.
>
> **ESTADO DE ESA CLASE `B`, HOY: PENDIENTE DEL OWNER, Y NADIE MÁS PUEDE MOVERLA.** No está
> resuelta, no está diferida y no tiene valor por defecto. `G21` de `KERNEL.md` L690 —«un
> sistema no puede definir sin conflicto de interés los criterios que aprueban su propia
> existencia»— es exactamente este caso, y por eso **F4 no elige ninguna de las tres y lo
> dice**. Mientras no haya respuesta, **`M-04` seguirá fallando el gate siguiente igual que
> ha fallado los tres anteriores**, y cerrar los 48 de clase `A` no lo cambia.
>
> **Las otras razones del veredicto**, todas de clase A: la **FASE 0** que `O17` ordena **no es
> ejecutable** —su ENTRADA exige el identificador de una iniciativa que su propio GATE prohíbe
> abrir, y su SALIDA se escribe donde `estado/` aún no existe—; la **Operativa** sigue con un
> eslabón sin productor que nadie declara en la migración; y **§18 excede a `O17`** dando a
> `SEG` una vía que la misma tabla niega dos filas más abajo.
>
> **Y lo que SÍ quedó cerrado.** **`C-L.5` CERTIFICADA por tercera vez consecutiva**, sobre
> universo derivado, con `OBLIGATORIO − ASIGNADO = ∅`, `ASIGNADO − LEÍDO = ∅` y los **52
> agotamientos** pasando las dos reglas. **`R-04` CERRADO CON MECANISMO** tras dos gates sin
> lograrlo. La propagación de `O17` es, en palabras del dictamen de `S`, **«la más disciplinada
> del expediente»**: 9 de las 12 reglas sin reserva, sede única y cuatro invocaciones
> byte-idénticas. **`D107` NO excede a `O17`.** `PN-17` y `PN-18` **registran sin elegir**.
> `D1`–`D106` y `O1`–`O16` intactas, y el material APROBADO protegido por refutación.

> **[ESTADO ANTERIOR · antes del SEGUNDO GATE DE CERTIFICACIÓN, documento 23]**

> **El GATE INDEPENDIENTE DE CERTIFICACIÓN devolvió `INSUFICIENTE PARA F5` sobre la candidata
> `4d231ee`. EL OWNER YA RESPONDIÓ la única decisión de clase `B`: es `O17`, eligió la
> alternativa (b), y con eso la clase `B` queda RESUELTA y YA NO BLOQUEA. Esta tanda está
> APLICANDO `O17` —propagada como `D107`— y los 68 hallazgos de clase `A`. `F4c` sigue
> ABIERTA y `F5` sigue NO AUTORIZADA, porque APLICAR NO ES CERTIFICAR.**
>
> **LA DECISIÓN DEL OWNER, Y POR QUÉ ELIGIÓ LO QUE ELIGIÓ.** La pregunta era el **nivel
> ESTRUCTURAL y su productor**, y `R` le presentó tres alternativas con su coste. Eligió la
> **(b): que cada macrocircuito produzca su certificación Estructural AL ARRANCAR, como
> precondición propia de esa ejecución.** Su motivo, en sus palabras: **robustez y
> revalidación permanente por encima del ahorro operativo** — «*No elijo la alternativa
> barata de certificarlo sólo durante la instalación. Quiero que instalación, adopción,
> migración y actualización comprueben la estructura vigente antes de continuar. La prioridad
> es una base sólida y permanente, aunque suponga más comprobaciones y consumo de
> recursos.*» Descartó la **(a)** —producirlo sólo en la instalación— porque un producto ya
> instalado **no revalidaría** su Estructural al cambiar el kernel; y descartó la **(c)**
> —degradarlo a precondición no certificada— porque obliga a reescribir §9.2 y **cambia el
> contenido de `O12`**, que es resolución suya.
>
> Está registrada íntegra, con sus **DOCE reglas obligatorias** y su reparto —`SIS`
> propietario y productor · `VER` dosier · `PLT` maquinaria · `SEG` bloqueo—, en
> [`DECISIONES-Y-CONTRADICCIONES.md`](../rediseno/DECISIONES-Y-CONTRADICCIONES.md) §2, y su
> propagación es **`D107`**, declarada **DERIVADA**: sede nueva **§9.6 ·
> `gate:sistema-conforme`**, **FASE 0** en los cuatro macrocircuitos §8.1–§8.4, filas en §18,
> tabla adversarial `X-S1`–`X-S9`, y los bloques que faltaban en §15.8 para `D96`–`D107`.
> **`O1`–`O16` y `D1`–`D106` conservan su texto, y nada se renumera.**
>
> **QUÉ NO HACE `O17`.** No autoriza iniciar `F5`, ni `F6`, ni la adopción de PesquerApp. No
> levanta ninguna condición `C-L` abierta, no cierra `F4c` y no deroga ninguna presión
> vigente. Fija QUÉ tiene que producirse y QUIÉN lo produce; **construirlo es trabajo de las
> fases siguientes**.
>
> **QUÉ QUEDA, EXACTO.** Terminar de aplicar los 68 de clase `A`, **publicar el árbol vigente
> como candidata nueva** y **encargar OTRO GATE INDEPENDIENTE** sobre ella, con revisores de
> contexto limpio que no sean quien aplicó esta tanda. **Ningún hallazgo de esta tanda se
> declara SUPERADO**: sólo puede declararlo ese gate.
>
> **EL VEREDICTO QUE ABRIÓ TODO ESTO**, y que sigue siendo el vigente sobre `F4c`, está en
> [`22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md`](22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md),
> con los tres dictámenes transcritos íntegros. Lo emitieron **diez agentes con contexto
> limpio** —revisor `P` como cadena `P1`–`P4`, revisor `Q` como cadena `Q1`·`Q2`·`Q3`·`Q5`·`Q4`,
> en paralelo y sin verse, y el adjudicador `R`—. Ninguno escribió F4, aplicó `D16`–`D106`, es
> autor de ninguna corrección ni fue revisor `A`–`R`. **Ningún hallazgo se corrigió en esa
> pasada, y es deliberado.**
>
> ```text
> 69 HALLAZGOS DISTINTOS    0 bloqueantes · 8 graves · 34 medios · 27 menores
>                           27 de `P` · 42 de `Q` · 3 propios de `R` · menos 3 solapes
>
> CLASIFICACIÓN             A · corregible en F4c sin decidir arquitectura      68
>                           B · DECISIÓN EXCLUSIVA DEL OWNER                     1   ← BLOQUEA
>                           C · trabajo futuro ya contratado                     0
>
> LOS 24 DEL DOCUMENTO 21   20 SUPERADOS · 4 NO SUPERADOS: `P-06` `Q-04` `Q-05` `R-04`
> ```
>
> **LA QUE FUE LA ÚNICA DECISIÓN QUE BLOQUEABA — HOY RESUELTA POR `O17`: el nivel ESTRUCTURAL
> y su productor.** §9.2 fija la cadena `estructural ◀── operativo ◀── integrado ◀── completo`
> y una regla dura: «un nivel no se declara por argumento ni por haber pasado el anterior».
> Cuando el gate emitió su veredicto, `gate:sistema-conforme` **tenía una sola aparición en
> todo el documento 11, y era su propia definición**: ninguna fase de ninguno de los cuatro
> macrocircuitos lo producía, con lo que **`O12` no era satisfacible por ningún recorrido**.
> **La pregunta exacta, con sus tres alternativas y el coste de cada una, está en §13 de la
> adjudicación de `R`, dentro del documento 22; la RESPUESTA está en `O17`, y F4 no la
> eligió: la eligió el Owner.** Con la (b) elegida, `O12` **pasa a ser satisfacible desde
> CUALQUIER entrada**, y el coste —un gate más en los cuatro recorridos, que encarece
> migración y actualización— **el Owner lo acepta expresamente**.
>
> **Por qué INSUFICIENTE, en seis razones y ninguna es la cobertura:**
>
> ```text
> 1  `M-04` sigue FALLIDA y HOY ES MÁS ANCHA. `R` construyó y ejecutó OCHO árboles
>    defectuosos que pasan la batería 30/30 EN VERDE. El peor es suyo: volteó los veredictos
>    de los documentos 19, 20 y 21 a `SUFICIENTE PARA F5` y la batería no se enteró, porque
>    su rango inmutable dice `1[5-8]`
> 2  las CINCO correcciones de la batería funcionan en el PERÍMETRO EXACTO de su
>    contraejemplo y en ninguna otra parte. `G-26` se desactiva escribiendo «regresión» en la
>    línea, y con eso se reinstala el único GRAVE del gate anterior
> 3  `R-04` NO está superado: está AGRAVADO. El punto 7 de §2.6.9 es byte-idéntico a
>    `7764cca`, y la fila de `W17` afirma que reparte algo que no reparte
> 4  DOS GRAVES nuevos sobre garantías publicadas de material APROBADO: el nivel ESTRUCTURAL
>    sin productor —el B de arriba— y `reconciliacion_pendiente` sin productor, que deja
>    `T22` de (a) insatisfacible sin que ninguna presión lo registre
> 5  la regla del ordinal NO EJECUTA: §15.8 no tiene bloque para `D96`–`D106`, y
>    `00-INDICE` se contradice dentro de una sola tabla
> 6  la razón de método: la mayoría de los 69 los introdujo o los dejó pasar esta misma
>    tanda, y cuatro son la reinstalación de defectos ya adjudicados
> ```
>
> **Esas seis razones son la TRANSCRIPCIÓN del veredicto, y describen el árbol que el gate
> juzgó — no el de hoy.** La razón 5, por ejemplo, se apoyaba en que §15.8 no tenía bloque para
> `D96`–`D106`: esta tanda los ha escrito, y con `D107` la regla del ordinal vuelve a ejecutar.
> **Eso NO declara superada la razón 5 ni ninguna otra**: quien aplica no certifica, y sólo un
> gate independiente posterior puede declararlo. Se transcriben sin retocar porque un veredicto
> publicado no se edita.
>
> **Y lo que SÍ quedó cerrado, porque también es información.** **`C-L.5` sigue CERTIFICADA**,
> por segunda vez consecutiva y **ahora sobre un universo DERIVADO**: `P-08` está cerrado de
> verdad —el comando existe, se publicó en un commit propio antes que el manifiesto, y `R`
> recalculó las dos restas, **`OBLIGATORIO − ASIGNADO = ∅` y `ASIGNADO − LEÍDO = ∅`**—.
> **VEINTE de los veinticuatro** hallazgos del documento 21 están genuinamente superados,
> **el único GRAVE de aquel gate entre ellos**. Las **cinco vías nombradas** de la batería
> están cerradas con control positivo. **`Q-14` y `C-L.3`, cerrados.** Los **22** hallazgos
> del documento 15 y los documentos **10, 12, 13 y 14** —leídos íntegros por primera vez en
> el expediente— **no producen ni un hallazgo vivo**. `D1`–`D106` y `O1`–`O16` intactas.
>
> **El coordinador del gate se equivocó y lo dice.** Su manifiesto agotó 21 fuentes con una
> cita del documento 20 que no nombra ninguna ruta. Lo encontró su propio relevo `Q3` antes de
> cualquier adjudicación. El manifiesto **no se editó** —`1bis` lo declara inmutable—: se
> publicó el `ADDENDUM 1`, se creó el relevo `Q5` después de commitearlo, y `Q5` leyó las 21.
> `R` juzgó esa conducta expresamente y la declaró correcta, con tres reproches.

> **[ESTADO ANTERIOR · antes del GATE DE CERTIFICACIÓN, documento 22]**

> **Los 24 hallazgos del GATE INDEPENDIENTE DE CIERRE CON MANIFIESTOS están APLICADOS — NO
> CERTIFICADOS. `F4c` sigue ABIERTA y `F5` sigue NO AUTORIZADA.**
>
> **`C-L.5` quedó CERTIFICADA por ese gate, y sigue certificada.** Es la única de las trece
> condiciones que un adjudicador independiente ha certificado, y **certificar la cobertura no
> cierra `F4c`**: el mismo gate falló por otras dos de sus siete condiciones.
>
> **Cómo quedan los 24, y por qué ninguno dice SUPERADO:**
>
> ```text
> APLICADOS, NO CERTIFICADOS   24   los veinticuatro ids distintos, uno por fila de la
>                                   matriz de trazabilidad de este fichero
>   GRAVE        1   P-05≡Q-08 — la sección «Siguiente acción exacta», reescrita entera
>   MEDIO       12   P-01≡Q-13 P-02≡Q-06 P-04 P-06 Q-01 Q-02 Q-04 Q-05 Q-07 Q-14 R-02 R-03
>   MENOR       11   P-03 P-07 P-08 Q-03 Q-09 Q-10 Q-11 Q-12 Q-15 R-01 R-04
>   BLOQUEANTE   0
>
> M-04, APARTE Y FALLIDA            sus cuatro refutaciones nombradas estaban cerradas, pero
>                                   su PROPOSICIÓN —«se puede construir un árbol defectuoso
>                                   que pase 30/30 en verde»— seguía siendo verdadera. Esta
>                                   tanda añade protección contra Q-01, Q-04 y Q-05. Eso NO
>                                   la declara superada: sólo un gate posterior puede
> ```
>
> **Qué se corrigió, por causa.** La batería dejó de derivar con expresiones regulares sobre
> prosa y pasa a leer **indentación y escalares de bloque** (`Q-05`); el ancla se normaliza
> como el resto del algoritmo (`Q-02`); la **procedencia** —propietaria, obligatoria,
> condicional— se conserva y el **reparto por vía** se publica y se contrasta (`Q-03`,
> `Q-10`); `G-11b` **falla cerrado** (`Q-01`); el conjunto vigilado se **deriva de las
> fichas** (`Q-09`); y `G-23` compara el **conjunto de ficheros del kernel contra la revisión
> base** y exige que el catálogo de procesos ocupe **una sola sede**, con lo que el árbol que
> daba 30/30 en verde con una copia del catálogo y un contrato autodeclarado contradictorio
> **hoy falla con responsable y causa** (`Q-04`).
> `D105` se propaga a las sedes que no lo habían recibido: `X54` cubre las **dieciocho**
> ventanas y nombra `W17` (`P-01`), la capa B escribe la referencia en su dirección vigente
> (`P-02`), `§2.6.9` fija **quién dice qué** (`R-03`), `W17` deja de atribuirse un tramo que
> es de `W8` (`R-04`) y las tres sedes que justificaban su idempotencia «por contenido»
> —razonamiento que `§2.8` había retirado— dicen hoy dónde vive de verdad (`R-01`).
>
> **`PN-16` es la única presión que esta tanda añade**, y sale de `P-07`: la grafía canónica
> de `<CAP>:revisión` vive en (b) L836, que es **material APROBADO**, y F4 no puede elegirla.
> Con ella, las presiones vigentes derivadas de §16 pasan a **CATORCE**, y `PN-16` es la
> **única** presión nueva. `PN-1`–`PN-14` conservan su texto. **De `PN-15` cambió UNA sola
> cosa, y hay que decirlo con precisión**: su párrafo de evidencia, que era falso —declaraba
> «cero apariciones» de `G20`/`G21`/`G23` en el documento 11, donde las hay— y que `P-06`
> obligó a acotar al material **APROBADO**, que es el único que puede derogarlas: **(a) una
> aparición pertinente, (b) cero, `E2` cero**. Todos los demás campos de `PN-15` —lo que
> presiona, su texto vigente, la materia mínima, el alcance, lo que bloquea, la condición de
> reversión, el propietario, la prueba posterior y el origen— **permanecen intactos**.
>
> **NO se ha añadido `D107` y no se ha reescrito ninguna decisión**: el gate declaró que
> ninguno de los 24 exigía decidir arquitectura, y **ninguno lo exigió**. `D1`–`D106` y
> `O1`–`O16` siguen intactas; los documentos 15–21 y los manifiestos del gate, sin tocar.
>
> **Quien ha aplicado esto no puede certificarlo.** El paso siguiente es publicar el árbol
> vigente como candidata y encargar **otro gate independiente**, con revisores nuevos que no
> hayan aplicado esta tanda, que publique de nuevo el manifiesto previo de ASIGNACIÓN —ahora
> con la regla `1bis` de `C-L.5`: de qué sede sale el universo obligatorio y con qué comando
> auditable— y los manifiestos de LECTURA.

> **[ESTADO ANTERIOR · el veredicto del GATE DE CIERRE CON MANIFIESTOS, documento 21]**
> **El GATE INDEPENDIENTE DE CIERRE CON MANIFIESTOS VERIFICABLES devolvió INSUFICIENTE PARA
> F5 sobre la candidata `7764cca`, y NO por cobertura. `F4c` sigue ABIERTA, `F5` NO queda
> autorizada, y NINGÚN hallazgo se ha corregido en esta pasada.**
>
> Está en
> [`21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md`](21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md).
> Lo emitió un **adjudicador `R`** con contexto limpio sobre los dictámenes **ya cerrados**
> de dos revisores independientes, `P` y `Q`, que trabajaron en paralelo sin verse. Ninguno
> de los tres escribió F4, aplicó `D16`–`D106`, es autor de las correcciones ni fue revisor
> `A`–`O`.
>
> **`C-L.5` QUEDA CERTIFICADA, Y ES LA PRIMERA VEZ.** Es lo que `D106` contrató y lo que el
> gate anterior declaró NO CERTIFICABLE (`O-04`):
>
> ```text
> MANIFIESTO PREVIO DE ASIGNACIÓN   commiteado SOLO, ANTES de que existiera ningún revisor
>                                   18cbfb5 · 140 líneas · 1 fichero · 140 inserciones
>                                   SHA-256 c843b0c341183859b7f0f07db78cc67eade7ef98c4a96a…
>                                   43 fuentes · 59 asignaciones · 31 888 líneas
>                                   `P` verificó con `git log` que es anterior al reparto
>
> MANIFIESTOS DE LECTURA            uno por revisor, dentro de su dictamen, con SHA-256
>                                   recalculado y DOS anclas de regiones separadas por fuente
>
>                    ASIGNADAS   LEÍDAS ÍNTEGRAS   PARCIALES   NO ABIERTAS   A − L
>   REVISOR P            20            20              0            0          ∅
>   REVISOR Q            31            31              0            0          ∅
>   ADJUDICADOR R         9             9              0            0          ∅
>
> `R` NO se quedó en las suyas: recalculó `wc -l` y `sha256sum` de las CUARENTA Y TRES filas
> del manifiesto contra el árbol. 43 de 43 coinciden. 0 ficheros ausentes.
> `R`: «No la presumo en ninguna de las dos direcciones: la calculé.»
> ```
>
> **Y aun así, INSUFICIENTE. Fallan DOS de las siete condiciones, y ninguna es la cobertura:**
>
> ```text
> 1  asignadas − leídas = ∅                                          SE CUMPLE
> 2  C-L.5 certificada                                               SE CUMPLE · 1ª vez
> 3  D104–D106 superan el intento adversarial                        NO SE CUMPLE
> 4  los cuatro bloqueantes del gate anterior superados              SE CUMPLE
> 5  ningún pendiente de F5/F6 exige inventar arquitectura           SE CUMPLE
> 6  ninguna contradicción material vigente sin registrar            NO SE CUMPLE
> 7  la batería no ofrece falsos verdes en R1–R4                     SE CUMPLE
> ```
>
> **La 3 falla por `D104`, y NO por su arquitectura**, que resistió: las cuatro vías operan,
> la propietaria hace **fallar** `G-15`, el discriminante es estructural, las cuatro
> combinaciones de `AUD` se derivan, `DIR` entra sin excepción escrita y no hay décimo par.
> Lo que falla son **dos de sus cuatro pilares declarados**, falsados contra el árbol y **en
> verde los dos**: el pilar (ii) —«los campos de prosa NO se leen»— es falso del troceado
> real, que es un `re.findall` sobre un segmento de texto y no un parseo YAML (`Q-05`); y el
> pilar (iv) —el ancla de posición— **no normaliza**, contra la declaración del propio `D104`
> de que la normalización «ES TODA LA INFERENCIA QUE HAY» (`Q-02`).
>
> **La 6 falla por SIETE contradicciones materiales vigentes y sin registrar**, y **tres son
> la segunda o tercera recurrencia de la misma frase**: `X54` dice diecisiete donde se
> derivan dieciocho ventanas y ninguna fila adversarial alcanza `W17` (`P-01`≡`Q-13`) · la
> capa B conserva el verbo que `D105` invirtió, y §2.6.9 la invoca por su nombre para una
> regla que ella no escribe (`P-02`≡`Q-06` + `R-03`) · este fichero cuenta en L1142 las nueve
> ventanas `RC-1`–`RC-9` que L1641 declara retiradas (`P-04`) · **la sección «Siguiente acción
> exacta» —la que la cabecera designa como punto de entrada— lleva dos tandas de retraso, sin
> marca de histórica, con CINCO afirmaciones falsas a la vez, y una de ellas reproduce `M-06`
> en la misma tanda que lo declara corregido** (`P-05`≡`Q-08` + `R-02`) · el bloque de
> evidencia de `PN-15` se autofalsifica (`P-06`) · §16 L7887 cerraba su rango en «`PN-14`»
> cuando ya existía `PN-15`, omitiendo justo la que va al Owner (`Q-07`) · y `C-L.3` se
> describe aquí con la regla
> de `D103` que `M-01` refutó, sin que `D104` aparezca en ninguna de sus seis sedes (`Q-14`).
>
> **24 hallazgos distintos —`P` 8 · `Q` 15 · `R` 4 propios · 3 solapes—:
> BLOQUEANTE 0 · GRAVE 1 · MEDIO 12 · MENOR 11.** Ninguno exige decidir arquitectura, y `R`
> los tasa uno a uno: una palabra, un verbo, cinco caracteres en un `if`, marcar un bloque
> como histórico.
>
> **`R` no resolvió por mayoría, y lo demuestra rechazando.** **RECHAZÓ la primera razón de
> veredicto de `P`** —`P-03`, la tesis de que `D105` deja el terminal inconstruible—: abrió
> las cinco sedes y **cuatro de las cinco afirmaciones son falsas**. `predecesor =
> id(abandonada)` está en TRES sedes de §2.6.9, la regla de unicidad que `P` daba por ausente
> está escrita en L4406, **dos arranques no pueden emitir dos `deriva` porque el paso 0
> comprueba la existencia por `abandonada_id` ANTES de emitir**, y `predecesor` es campo común
> a todo evento. Y declaró **FALSA la premisa de hecho de `P-08`**: el documento 15 **sí** se
> leyó íntegro, por `N`, en el gate anterior. De ahí una resolución de criterio que queda
> fijada: **una lectura íntegra hecha en un gate anterior SATISFACE `C-0.1`; no hay que
> rehacerla.**
>
> **Cómo quedan los 21 hallazgos del gate de cobertura, adjudicados por `R`:**
>
> ```text
> SUPERADOS            17   M-01 M-02 M-03 M-05 M-06 M-07 M-08 M-10 M-11 M-12
>                           N-01 N-02 N-05 · O-01 O-02 O-03 O-04
>                           **Los cuatro bloqueantes anteriores —M-01 M-02 M-03 N-01— entre
>                           ellos**, verificados uno a uno y con mecanismo, no con prosa
> FALLIDO               1   M-04. Sus cuatro refutaciones nombradas están cerradas —`R` las
>                           reprodujo—, pero M-04 es la PROPOSICIÓN «se puede construir un
>                           árbol defectuoso que pase 30/30 en verde», y sigue siendo cierta:
>                           con una copia íntegra del catálogo de procesos y un contrato que
>                           declara por escrito contradecir a C4, la batería da 30/30 EN VERDE
> REGISTRADOS PARA F5   2   M-09 · N-03
> CONTRATADO PARA F6    1   N-04
>                          ──
>                          21
> ```
>
> **Las cuatro refutaciones prescritas fallan las cuatro**, reproducidas por `R` en copias de
> `/tmp`: `R1` 28/30 · `R2` 29/30 · `R3` 29/30 · `R4` 26/30, y en `R2` y `R3` **falla la
> comprobación responsable SOLA**. Lo que la condición 7 no cubre son **tres falsos verdes
> nuevos**: `Q-01` —`G-11b` declara intactas las ochenta y seis filas con tres reescritas y es
> el único dependiente de Git que no falla cerrado—, `Q-04` y `Q-05`.
>
> **Y consta, porque no es cortesía:** `D105` **resistió el ataque más duro que se le hizo** y
> `R` la llama «la mejor decisión que este expediente ha producido» · `D106` supera su intento
> y la prueba de `PN-15` **falla hoy**, como debe · `Q` derivó `<CAP>:revision` **a ciegas
> antes de leer lo publicado y coincidió exactamente** —cinco procesos, nueve pares, ningún
> décimo—, intentó refutar `D104` por nueve caminos y concluyó «la cuarta formulación es la
> buena» · `git diff --numstat 652ab8e..HEAD` sobre el registro da **169 inserciones y CERO
> supresiones**: `D1`–`D103` conservan su texto y `O1`–`O16` están intactas · los documentos
> 15–20 sin tocar · `P` y `Q` **publicaron sus derrotas**, y `R` deja escrito que eso es lo que
> le permitió reconstruir por qué la séptima de `P` tampoco se sostiene.
>
> `R`: «Ésta es, con distancia, la candidata más sólida que este corpus ha producido. No falla
> por concepción, no falla por cobertura y no falla por lo que decidió. Falla, otra vez, en la
> mitad de los sitios donde sus decisiones tenían que llegar — y esta vez la mitad que falta
> incluye la página que un agente lee cuando escribe «Continúa».»
>
> **NINGÚN HALLAZGO SE HA CORREGIDO, Y ES DELIBERADO.** Eso incluye los que caen sobre este
> mismo fichero —`P-04`, `P-05`≡`Q-08`, `R-02`, `Q-14`—: **la sección «Siguiente acción
> exacta» del final NO se ha tocado, y sigue diciendo lo que el gate le reprocha.** Corregirla
> en esta misma pasada sería, otra vez, que quien recibe sea quien aplica. El coordinador de
> este gate sólo ha transcrito y registrado: **no emite suficiencia.**

> **[ESTADO ANTERIOR · GATE DE COBERTURA Y CIERRE, documento 20]**
> **El GATE INDEPENDIENTE DE COBERTURA Y CIERRE devolvió INSUFICIENTE PARA F5 sobre
> `r2`=`c3d6465`, y sus 21 hallazgos están APLICADOS — NO CERTIFICADOS. `F4c` sigue
> ABIERTA y `F5` NO queda autorizada.**
>
> **Cómo quedan los 21, en los cuatro estados que no se mezclan:**
>
> ```text
> CORREGIDOS EN F4c            17   M-01 M-02 M-03 M-04 M-05 M-06 M-07 M-08 M-10 M-11
>                                   M-12 · N-01 N-02 N-05 · O-01 O-02 O-03
> REGISTRADOS PARA F5           2   M-09 (grafía `revisión`/`revision`) · N-03 (marcas de
>                                   `E1`). Los dos caen en material APROBADO que F4c no
>                                   puede editar, y van a la checklist `E5-3` y `E5-4`
> CONTRATADO PARA F6            1   N-04 (los perfiles de agente, que ningún censo cuenta).
>                                   **La cifra vigente queda reanclada a 21 aquí; DERIVARLA
>                                   es F6, y encaja en `C-L.10`. Cero líneas escritas**
> ABIERTO PARA EL SIGUIENTE     1   O-04. El contrato de los DOS manifiestos —asignación y
> GATE                              lectura— queda preparado, y **`C-L.5` NO se declara
>                                   cerrada**: la cierra el gate que los publique
>                                  ──
>                                  21
> ```
>
> **Registrar no es corregir. Contratar no es implementar. Y aplicar no es certificar:**
> quien ha escrito `D104` es el mismo que escribió `D98` y `D103`, las dos que este gate
> acaba de declarar insuficientes.
>
> Lo emitió un **adjudicador `O`** con contexto limpio sobre los dictámenes cerrados de dos
> revisores independientes, `M` y `N`, que trabajaron en paralelo sin verse. Está en
> [`20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md`](20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md).
>
> **LA COBERTURA SE CERRÓ, Y ES LA PRIMERA VEZ.** Las cuatro fuentes que `C-L.5` nombra
> —`ADS-PENDIENTES` con sus BLOQUES B y C, y los documentos 16, 17 y 18: 8 735 líneas— se
> leyeron **ÍNTEGRAS por los tres, de forma independiente**. `N` cerró además las catorce
> fuentes y las quince fichas que tres gates dejaron sin abrir, **incluido el documento 15**,
> y contestó las dos preguntas que el adjudicador `I` declaró irresolubles. **Los BLOQUES B y
> C CONFIRMAN a F4; `b.3` y `b.5` NO refutan `I-08`.** Esas vías de escape quedan cerradas.
>
> **Y aun así, INSUFICIENTE. SEIS razones, cualquiera bastaría:** `C-L.3` **no cerrada** por
> TRES causas independientes —la vía propietaria no implementada (`O-01`), la vía condicional
> perdida en `proceso:AUD` (`M-01`), y la posición «tras `VER`» exigida en el único proceso
> que no tiene `VER`, con `proceso:DIR` excluido sin motivo derivable (`N-01`)—; **un defecto
> arquitectónico NUEVO que hace INEMITIBLE el terminal `abandonada`** —`id(abandonada)`
> depende de `id(deriva)` y viceversa, y ninguna sede lo resuelve (`M-02`)—; **una laguna de
> durabilidad con fallo silencioso** que deja el diario permanentemente inválido (`M-03` +
> `O-03`); **la batería REFUTADA** —dos árboles defectuosos distintos pasan **30/30 en verde**,
> uno con el contraejemplo exacto que `G-15` dice detectar (`M-04`)—; **tres sedes vigentes
> que el árbol desmiente** (`M-05`, `M-06`, `M-07`); y la regla de cierre de `C-L.5` no
> certificable (`O-04`).
>
> **21 hallazgos consolidados, CERO rechazados: GRAVE 5 · MEDIO 6 · MENOR 10.** Derivado de
> las filas adjudicadas. **NINGUNO se ha corregido**, y eso incluye los que caen sobre este
> mismo fichero y sobre la batería.
>
> **Y consta:** `D96`–`D103` **no reescribieron ni una línea** —121 inserciones, cero
> supresiones, verificado con `git`—; `D67` idéntica byte a byte; los documentos 15–18
> intactos; la aritmética resiste entera; la **cardinalidad de `D103` es correcta** y acertó
> en lo más difícil, negarse a publicar un décimo par fijo; **ninguna de las trece condiciones
> está mal clasificada**; y `J-11` y `C-L.10` declaran cero implementación **y la tienen de
> verdad**. `O`: «no falla por concepción; falla porque una decisión bien tomada llega a la
> mitad de los sitios que la invocan».
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
> implementación. Las trece condiciones quedan en **CINCO estados primarios mutuamente
> excluyentes**, y sólo el primero significa que el trabajo esté hecho. **Cada id
> `C-L.1`–`C-L.13` recibe EXACTAMENTE UN estado, y ningún subhallazgo cuenta como
> condición:**
>
> ```text
> CORREGIDAS EN F4c        `C-L.1` `C-L.3` `C-L.4` `C-L.6` `C-L.7` `C-L.8` `C-L.9` `C-L.11`
>   ocho                   El cambio está ESCRITO en su sede y es comprobable hoy
>
> REGISTRADAS PARA F5      `C-L.2` · `PN-15`: `G20`–`G23` PRESIONADAS, y **la decisión sigue
>   dos                    sin tomar** — es del Owner, y F4 no puede tomarla
>                          `C-L.12` · los dos restos de (b), como checklist verificable
>                          **Registrar NO es corregir**: el texto de (b) sigue como estaba
>
> CONTRATADA PARA F6       `C-L.10` — censo `AFIRMACIONES` derivado y `T152` sobre toda sede
>   una                    que publique versión. **Contratar NO es implementar**: no existe
>                          ni una línea de código, y `T151` y `T152` siguen pasando en verde
>                          sobre las sedes que el corpus desmiente
>
> MIXTA, SATISFECHA POR    `C-L.13`. Es la única con estado COMPUESTO, y por eso se declara
> DESGLOSE                 aparte en vez de repartir sus piezas entre los demás estados.
>   una                    Sus SEIS componentes, como ATRIBUTOS SECUNDARIOS que **NO cuentan
>                          como condiciones**:
>                            `K-05` `K-09` `K-10` `K-08` `L-03`   CORREGIDOS AHORA
>                            `J-11`                               CONTRATO COMPLETO PARA F6,
>                                                                 NO IMPLEMENTADO
>
> ABIERTA POR COBERTURA    `C-L.5`. **No la cierra esta tanda ni puede cerrarla**: aplicar
>   una                    correcciones no es leer lo que no se leyó. Sólo la cierra el gate
>                          siguiente, con revisores de contexto limpio y lectura real
>
> SUMA                     8 + 2 + 1 + 1 + 1 = 13, y son los TRECE ids distintos
> ```
>
> **Aplicar no es certificar**, y **registrar o contratar no es corregir**.
>
> **Corregido aquí un doble conteo.** La clasificación anterior declaraba cuatro estados y
> sumaba trece, **pero sumaba trece por accidente**: contaba `J-11` como si fuera una
> condición —y no lo es: es uno de los seis componentes de `C-L.13`— mientras atribuía los
> otros cinco componentes a «CORREGIDAS EN F4c» sin ser ids `C-L`. El resultado era **doce
> ids `C-L` asignados más un subhallazgo**, con **`C-L.13` sin estado primario propio**.
> Mezclar condición y subhallazgo en un mismo recuento es la clase de defecto que la matriz
> de los 43 ya cerró una vez con la regla de **un estado primario por hallazgo**; aquí se
> aplica la misma regla a las condiciones de cierre.
>
> **Y consta:** los tres coinciden en que es la candidata más sólida de la cadena. Las diez
> filas FALLIDAS del gate anterior están cerradas, verificadas una a una. **Nada de lo que
> impedía el paso exigía inventar arquitectura: el bloqueante eran cinco líneas en §3.6, y
> están escritas.**

> **[ESTADO ANTERIOR · el GATE FINAL INDEPENDIENTE, documento 16, y su COMPLEMENTO DE
> COBERTURA, documento 17 — y la cadena de devoluciones que los precede. HISTÓRICO: se
> conserva para trazabilidad y NO describe el estado vigente. Le faltaba esta marca, que los
> dos bloques anteriores sí llevaban; corregido por `Q-38` del documento 22.]**
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
actualizado: 2026-08-31
regla_de_reanclaje: ESTE BLOQUE ES EL ESTADO REANUDABLE y va SIN rótulo histórico: describe el
             árbol VIGENTE. Fue a la vez el defecto X-04 del documento 24 —GRAVE— y la CUARTA
             recurrencia consecutiva de la clase «el checkpoint no reancla»: K-01/J-10/L-01 ·
             P-05≡Q-08/R-02 · S-17≡S3-05 · X-04. Iba DOS eventos atrasado bajo
             `actualizado: 2026-08-30`, nombrando O17 y el documento 22 como vigentes cuando
             ya existían el documento 23, O18, D108 y el documento 24.
             LA GARANTÍA GENERAL, escrita AQUÍ DENTRO para que no dependa de que alguien se
             acuerde, y en la forma que S-16 y S-17 ya establecieron para este fichero:
               1  NADA QUE OTRA SEDE PUEDA DERIVAR SE COPIA DENTRO DE ESTE BLOQUE. Ni
                  recuentos de hallazgos, ni severidades, ni clasificación A/B/C, ni número
                  del último documento, ni rama, ni base: se REMITE a su sede, o se DERIVA
                  con el comando que la deriva. Copiar es lo que caduca
               2  EL ÚLTIMO GATE Y SU DOCUMENTO NO SE ESCRIBEN A MANO. Se derivan con
                       ls docs/evolucion/[0-9][0-9]-*.md | sort | tail -1
                  y su VEREDICTO y su RECUENTO viven EN ESE documento, que es inmutable y es
                  su única sede
               3  LA ÚLTIMA RESOLUCIÓN DEL OWNER Y LA ÚLTIMA DECISIÓN TAMPOCO. Se derivan con
                       grep -o '^### `O[0-9]*`' docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md | tail -1
                       grep -o '^| D[0-9]* |' docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md | tail -1
               4  TODO EVENTO NUEVO —un gate devuelto, una resolución del Owner, una tanda
                  aplicada— REANCLA `metodo`, `last_meaningful_event` y `based_on` EN EL MISMO
                  COMMIT QUE LO REGISTRA. Un evento escrito en la cabecera de este fichero y
                  no aquí es EXACTAMENTE el defecto de X-04, y no cuenta como registrado
               5  LO ANTERIOR NO SE BORRA: baja a `metodo_anterior` y a
                  `last_meaningful_event_anterior`, que es donde vive lo histórico
               6  NINGÚN HALLAZGO SE DECLARA SUPERADO POR ESTE REANCLAJE. Reanclar no es
                  certificar, y sólo un gate independiente posterior puede cerrar X-04
metodo:      SIS/Evolucion · CUARTO GATE DE CERTIFICACIÓN DEVUELTO —VEREDICTO INSUFICIENTE
             PARA F5, y **EL GATE DECLARADO INVÁLIDO POR SU PROPIO ADJUDICADOR**— y TANDA DE
             APLICACIÓN DE SUS HALLAZGOS EN CURSO. Es el PRIMER gate inválido del expediente,
             y lo produce el COORDINADOR: transcribió el SOBRE DE ANCLA a mano en el encargo
             de cada relevo y las transcripciones NO fueron idénticas. El emisor emitió bien;
             falló la ENTREGA, que ocurre FUERA del árbol.
             El documento es el que deriva la regla 2 de `regla_de_reanclaje`. El recuento de
             hallazgos, sus severidades y la clasificación A/B/C NO SE COPIAN AQUÍ: su sede es
             el propio documento, en la adjudicación de AA.
             LO QUE ESTA TANDA APLICA, y no es más que esto: se ANOTA de verdad en la entrada
             de O18 la resolución que la proyección de O19 decía haber anotado y no anotó; se
             propaga D105 a las sedes vivas que seguían diciendo que `abandonada` RETIRA el
             marcador —incluidas dos filas que son CONTRATO DE PRUEBA de F6—; los titulares
             numéricos que su propia enumeración desmentía pasan a REMITIR o a DERIVARSE, y la
             regla de titulares de §0 declara que NO tiene guardián; se corrigen las
             afirmaciones sobre el propio árbol que el gate falsó, incluidas TRES citas
             entrecomilladas atribuidas al Owner que la sede canónica no contiene; y el punto
             de entrada recupera la remisión al campo de la excepción del kernel de este mismo
             fichero, que G-23 exige y que la reescritura de O19 había perdido.
             NINGUNA COMPROBACIÓN NUEVA Y NINGUNA PROTECCIÓN INTERNA NUEVA: el adjudicador AA
             lo ordenó expresamente —«lo que falta es de resta y de disciplina»—, y es la
             misma orden que dejó el adjudicador X y que el Owner ratificó.
             LO QUE NO CAMBIA: ningún hallazgo se declara SUPERADO, M-04 no se cierra, C-L.7
             sigue NO CERRADA, **C-L.5 pasa de CERTIFICADA a ABIERTA** por ASIGNADO − LEÍDO =
             1, y no hay NINGUNA decisión pendiente del Owner: los treinta y seis hallazgos
             tienen remedio determinado dentro de F4c.
             APLICADA, NO CERTIFICADA · F4c ABIERTA · F5 NO AUTORIZADA
metodo_anterior: SIS/Evolucion · RESOLUCIÓN O19 DEL OWNER RECIBIDA —RATIFICACIÓN DEL TEXTO AMPLIO
             DE O18 Y CREACIÓN DE SU SEDE CANÓNICA EN docs/owner/— y TANDA DE APLICACIÓN EN
             CURSO. O19 revisa la PROYECCIÓN INCOMPLETA de O18, NO su contenido ni su diseño, y
             traslada la AUTORIDAD CANÓNICA de la paráfrasis del coordinador a docs/owner/: el
             registro de decisiones queda declarado PROYECCIÓN DERIVADA, y una paráfrasis nunca
             puede ampliar el texto canónico.
             EL TEXTO NO SE COPIA AQUÍ —regla 1 de regla_de_reanclaje—: su sede es
             docs/owner/ADS-OWNER-RESOLUCIONES.md, y qué resoluciones publica se deriva con
                 grep -o '^# `O[0-9]*`' docs/owner/ADS-OWNER-RESOLUCIONES.md
             LO QUE LA TANDA APLICA, y no es más que esto: el SOBRE DE ANCLA publica la ruta de
             la sede, su SHA-256 LEÍDO DEL COMMIT AUDITADO, los identificadores DERIVADOS de
             ella, el digest del texto canónico de cada resolución con su receta reproducible,
             la relación «O19 revisa la proyección incompleta de O18» y la declaración externa
             de ratificación, y FALLA CERRADO si la sede falta, si falta un identificador
             exigido o si un digest no se deriva; el INVENTARIO DE INTEGRIDAD QUE YA EXISTÍA se
             extiende a docs/owner/, con el mismo id, el mismo doble contraste y el perímetro
             derivado del árbol; la ampliación de esa zona se CLASIFICA con la regla de enlace
             desde 00-INDICE.md que el propio índice escribió; y la proyección tiene que
             ENLAZAR a la sede sin AMPLIAR su texto en ninguna valla.
             NINGUNA COMPROBACIÓN NUEVA Y NINGUNA PROTECCIÓN INTERNA NUEVA: el censo no se
             mueve —su sede es la tabla del README de verificacion/, y G-34 lo contrasta—, y
             tanto el adjudicador del documento 24 como el Owner lo prohibieron expresamente.
             LO QUE NO CAMBIA: O19 corrige PROCEDENCIA y AUTORIDAD, no DISEÑO. Ningún hallazgo
             se declara SUPERADO, M-04 no se cierra, C-L.7 sigue NO CERRADA, y la limitación
             que O18 declara de sí misma SIGUE VIGENTE — la sede traslada la autoridad y NO la
             hace mecánicamente verificable contra una fuente externa al sistema, que es el
             verificador externo real de F6.
             RATIFICADA, NO CERTIFICADA · F4c ABIERTA · F5 NO AUTORIZADA
metodo_anterior: SIS/Evolucion · TERCER GATE DE CERTIFICACIÓN DEVUELTO —gate VÁLIDO, VEREDICTO
             INSUFICIENTE PARA F5 sobre la candidata 21f1ccb— y TANDA DE CORRECCIÓN DE SUS
             HALLAZGOS EN APLICACIÓN. Es el PRIMER gate que recibe su ancla por un canal
             EXTERNO al repositorio, como O18 ordena, y el sobre se entregó a cada revisor
             dentro de su encargo antes de leer.
             El documento es el que deriva la regla 2 de `regla_de_reanclaje`. El recuento de
             hallazgos, sus severidades y la clasificación A/B/C NO SE COPIAN AQUÍ: su sede es
             §12 y §13 de la adjudicación de X, dentro de ese documento.
             Falla por A —coherencia interna— y por B —identidad de la candidata—, y
             EXPRESAMENTE NO por cobertura y NO por C: C-L.5 queda CERTIFICADA por CUARTA vez
             consecutiva y las dos restas son ∅.
             LA RAÍZ es la misma de los gates 21, 22 y 23 y esta vez es PEOR, porque éste era
             el gate que venía a curarla: O18 es correcta —cambia la raíz de confianza en vez
             de añadir otra comprobación interna— pero su implementación puso la nueva raíz
             DENTRO del mismo árbol. La circularidad no se cerró: se MOVIÓ, de HEAD a
             `emitir-sobre-de-ancla.py`. O18 NO está refutada: lo externo es la ENTREGA, lo
             interno es la PRODUCCIÓN. Y queda ordenado EXPRESAMENTE que NO se escriba una
             decimonovena protección interna.
             LO ÚNICO QUE VUELVE AL OWNER es una RATIFICACIÓN, no una elección: O18 registra
             UNA condición previa y seis sedes escriben TRES. La disputa queda REGISTRADA Y NO
             RESUELTA dentro de la propia entrada de O18 —con sus tres hechos, la corroboración
             de `bcee159` y la anomalía de forma frente a O17—, la propagación NO se recorta y
             O18 NO se completa, porque ninguna de las dos vías es ejecutable por F4 (G21).
             La pregunta exacta está en §13 de la adjudicación de X.
             Y LO QUE F4 SÍ HACE diga lo que diga el Owner: O18 recibe la declaración de
             INVERIFICABILIDAD que O17 ya tenía — X-02, cerrado en su sede.
             C-L.7 pasa de CERRADA a NO CERRADA por X-04, y este bloque es el reanclaje.
             APLICADA, NO CERTIFICADA · F4c ABIERTA · F5 NO AUTORIZADA
metodo_anterior: SIS/Evolucion · RESOLUCIÓN O18 DEL OWNER RECIBIDA Y PROPAGADA COMO D108,
             DERIVADA y no elegida por F4 —SOBRE DE ANCLA como requisito de todo gate de F4c,
             y CONTRATO DEL VERIFICADOR EXTERNO DEL CONTROL REPO registrado para F6 sin
             implementar—, y TANDA DE CORRECCIÓN DEL SEGUNDO GATE DE CERTIFICACIÓN
             (documento 23) APLICADA. La clase B de ese gate —LA RAÍZ— queda RESUELTA y YA NO
             BLOQUEA. O1–O17 y D1–D107 conservan su texto resolutivo · APLICADA, NO CERTIFICADA
metodo_anterior: SIS/Evolucion · SEGUNDO GATE DE CERTIFICACIÓN EJECUTADO SOBRE e316396 —ocho
             agentes de contexto limpio: cadena S1–S4, cadena T1·T2·T3 en paralelo y sin
             verse, adjudicador U— · VEREDICTO INSUFICIENTE PARA F5 · su ÚNICA clase B era LA
             RAÍZ y se elevó al Owner, que la respondió con O18 · documento 23
metodo_anterior: SIS/Evolucion · RESOLUCIÓN O17 DEL OWNER RECIBIDA Y EN PROPAGACIÓN, y TANDA
             DE CORRECCIÓN DEL GATE DE CERTIFICACIÓN (documento 22) EN APLICACIÓN.
             El Owner eligió la alternativa (b): el nivel ESTRUCTURAL lo produce CADA
             MACROCIRCUITO AL ARRANCAR, como precondición propia. Motivo suyo: robustez y
             revalidación permanente por encima del ahorro operativo. La clase B queda
             RESUELTA y YA NO BLOQUEA · propagación D107, DERIVADA y no elegida por F4:
             §9.6 gate:sistema-conforme · FASE 0 en §8.1–§8.4 · filas en §18 · X-S1–X-S9 ·
             bloques de §15.8 para D96–D107 · PN-17 y PN-18 nuevas · se aplican los 68
             hallazgos de clase A · O1–O16 y D1–D106 intactas, nada renumerado ·
             APLICADA, NO CERTIFICADA · F4c ABIERTA · F5 NO AUTORIZADA
metodo_anterior: SIS/Evolucion · GATE INDEPENDIENTE DE CERTIFICACIÓN CON UNIVERSO DERIVADO
             EJECUTADO SOBRE 4d231ee · diez agentes de contexto limpio, cadenas P y Q en
             paralelo sin verse y adjudicador R · VEREDICTO INSUFICIENTE PARA F5 ·
             69 hallazgos: A 68 · B 1 · C 0
metodo_anterior: SIS/Evolucion · TANDA DE CORRECCIÓN DEL GATE DE CIERRE CON MANIFIESTOS
             APLICADA · 24 hallazgos del documento 21 · SIN añadir ninguna D ·
             APLICADA, NO CERTIFICADA
metodo_anterior: SIS/Evolucion · TANDA DE CORRECCIÓN DEL GATE DE COBERTURA APLICADA ·
             D104 D105 D106 · los 21 hallazgos en CUATRO estados: 17 CORREGIDOS EN F4c ·
             2 REGISTRADOS PARA F5 · 1 CONTRATADO PARA F6 · 1 ABIERTO PARA EL SIGUIENTE
             GATE (O-04) · W17 nueva · APLICADA, NO CERTIFICADA · C-L.5 sigue ABIERTA ·
             F4c ABIERTA · F5 NO AUTORIZADA
metodo_anterior: SIS/Evolucion · GATE INDEPENDIENTE DE COBERTURA Y CIERRE EJECUTADO SOBRE
             r2=c3d6465 · M y N en paralelo, adjudica O · VEREDICTO INSUFICIENTE PARA F5
metodo_anterior: SIS/Evolucion · TANDA DE CORRECCIÓN DEL GATE DEFINITIVO APLICADA · D96–D102 ·
             y CORRECCIÓN TÉCNICA ACOTADA sobre ella · D103 · APLICADA, NO CERTIFICADA
metodo_anterior: SIS/Evolucion · GATE DEFINITIVO INDEPENDIENTE EJECUTADO SOBRE r4=0ea0451 ·
             VEREDICTO INSUFICIENTE PARA F5 · F4c ABIERTA · F5 NO AUTORIZADA
based_on:    LA SEDE CANÓNICA DE LAS RESOLUCIONES DEL OWNER —docs/owner/ADS-OWNER-RESOLUCIONES.md,
             creada por O19— ES FUENTE DE AUTORIDAD, y NO se deriva de la lista de abajo: esa
             lista enumera documentos numerados de docs/evolucion/, y la sede no es uno. Su
             contenido no se copia aquí; se remite. Es APPEND-ONLY, el índice la enlaza y el
             inventario de inmutables la custodia. Desde O19, toda sede derivada que cite una
             resolución del Owner cita DE AHÍ, y no de una paráfrasis.
             LA LISTA DE DOCUMENTOS NUMERADOS NO ES SEDE Y ES DERIVABLE — regla 2 de
             `regla_de_reanclaje`: `ls docs/evolucion/[0-9][0-9]-*.md | sort`. Son INMUTABLES,
             y el VEREDICTO y el RECUENTO de cada gate viven EN CADA DOCUMENTO, no aquí. La
             enumeración de abajo se conserva por comodidad de lectura; las anotaciones que
             COPIAN recuentos son ANTERIORES a esa regla y se conservan sin ampliarse, y las
             entradas nuevas REMITEN en vez de copiar.
             docs/evolucion/09-SINTESIS.md@56ea196 + su addendum
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
             docs/evolucion/20-GATE-INDEPENDIENTE-DE-COBERTURA-Y-CIERRE-F4C.md
                                                             M · N · O · VEREDICTO
                                                             INSUFICIENTE · cobertura cerrada
             docs/evolucion/21-GATE-INDEPENDIENTE-DE-CIERRE-F4C.md   P · Q · R ·
                                                             VEREDICTO INSUFICIENTE ·
                                                             C-L.5 CERTIFICADA
             docs/evolucion/22-GATE-INDEPENDIENTE-DE-CERTIFICACION-F4C.md
                                                             cadenas P1–P4 y Q1·Q2·Q3·Q5·Q4,
                                                             adjudica R · VEREDICTO
                                                             INSUFICIENTE · universo derivado ·
                                                             69 hallazgos, A 68 · B 1 · C 0
             docs/evolucion/23-SEGUNDO-GATE-DE-CERTIFICACION-F4C.md
                                                             cadenas S1–S4 y T1·T2·T3,
                                                             adjudica U · VEREDICTO
                                                             INSUFICIENTE · su única clase B
                                                             es LA RAÍZ, y es la que O18
                                                             responde · recuento EN EL PROPIO
                                                             DOCUMENTO
             docs/evolucion/24-TERCER-GATE-DE-CERTIFICACION-F4C.md
                                                             dictámenes V y W, adjudica X ·
                                                             gate VÁLIDO · VEREDICTO
                                                             INSUFICIENTE · PRIMER gate con
                                                             SOBRE DE ANCLA entregado por
                                                             canal externo · C-L.5 CERTIFICADA
                                                             por cuarta vez · recuento y
                                                             clasificación A/B/C EN EL PROPIO
                                                             DOCUMENTO, §12 y §13 de X · y la
                                                             RATIFICACIÓN de O18 que queda
                                                             PENDIENTE DEL OWNER, en su §13
             docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md
                                                             dictámenes Y y Z, adjudica AA ·
                                                             **GATE INVÁLIDO** · VEREDICTO
                                                             INSUFICIENTE · C-L.5 pasa a
                                                             ABIERTA · recuento, severidades
                                                             y clasificación A/B/C EN EL
                                                             PROPIO DOCUMENTO: aquí se REMITE
                                                             y no se copia, por la regla 1
             docs/evolucion/verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md
                                                             errores de hecho señalados SIN
                                                             tocar los dictámenes
             docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md   O18 · D108, y en la entrada
                                                             de O18: su declaración de
                                                             INVERIFICABILIDAD (X-02) y la
                                                             DISPUTA REGISTRADA Y NO RESUELTA
                                                             sobre el alcance de (c)
             docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md   O17 · D107
             docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md   D104 · D105 · D106
             docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md   O7–O14 · O15 · O16 · D16–D22 ·
                                                             D23–D33 · D34–D45 · D46–D51 ·
                                                             D52–D54 · D55–D57 · D58–D59 ·
                                                             D60–D61 · D62 · D63 · D64–D68 ·
                                                             D69–D70 · D71–D95 · D96–D102 ·
                                                             D103
             kernel/VERSION@2.0.0-alpha.9 · kernel/KERNEL.md@1.5.0
rama_de_trabajo: NO SE ESCRIBE AQUÍ, Y ES DELIBERADO. Este campo nombró durante tres tandas
             la rama y la base de una tanda ya cerrada, dentro de un bloque `freshness:
             vigente` — es Q-35 del documento 22, y es la tercera vez que caduca. La rama
             en curso y su base se DERIVAN de Git, que es su única sede:
               `git branch --show-current`
               `git rev-parse HEAD`
               `git merge-base HEAD origin/main`
             CUÁL ES LA RAMA DE ESTA TANDA TAMPOCO SE ESCRIBE: la dan los tres comandos de
             arriba, y sólo ellos.
             **[HISTÓRICO · este renglón nombraba «la rama de propagación de O17 y de la
             clase A del documento 22» y la candidata 4d231ee de
             review/f4c-post-gate-manifiestos-candidate-20260830. Eran ciertos cuando se
             escribieron y describen tandas ya cerradas; se conservan marcados.]**
             Los SNAPSHOTS PUBLICADOS sí se nombran cuando hacen falta, porque no describen
             el árbol vigente: la candidata del CUARTO gate es dc9be3f, en
             review/f4c-o19-sede-canonica-candidate-20260830.
freshness:   vigente. La cabecera separa ESTADO HISTÓRICO de ESTADO VIGENTE: lo dicho bajo
             Python 3.10 —9/13, T158 fallida, cobertura 291 frente a 293, nada publicado—
             queda marcado HISTÓRICO y SUPERADO, y no se borra
last_meaningful_event: EL CUARTO GATE DE CERTIFICACIÓN DEVUELVE INSUFICIENTE PARA F5 **Y SU
             PROPIO ADJUDICADOR LO DECLARA INVÁLIDO**, sobre la candidata dc9be3f. Es el
             PRIMER gate inválido del expediente y **la causa es el COORDINADOR**: las cinco
             transcripciones del SOBRE DE ANCLA a los encargos difieren en ocho campos —entre
             ellos el SHA-256 del DERIVADOR, que la SEDE CANÓNICA ordena entregar—, y la
             obligación del adjudicador pre-rechaza con sus palabras exactas la defensa que
             los dos dictaminadores ensayaron.
             Su documento es docs/evolucion/25-CUARTO-GATE-DE-CERTIFICACION-F4C.md, y es el
             que deriva la regla 2 de `regla_de_reanclaje`; su recuento, sus severidades y su
             clasificación A/B/C NO se copian aquí y viven en la adjudicación de AA.
             LA BUENA NOTICIA, y ningún gate anterior podía darla: **NO es la misma causa raíz
             en lo esencial.** Los gates 21–24 fallaron porque la verificación estaba anclada
             DENTRO del objeto verificado; éste no. Los TRES remedios que el adjudicador X
             dejó determinados están APLICADOS y FUNCIONAN, verificados por AA. Lo que falla
             es la mitad que nadie había podido medir: la ENTREGA, no la producción, y ocurre
             fuera del árbol, donde no hay defensa mecánica posible.
             LA MALA, y es la que duele: **SÍ es la misma causa en el MÉTODO.** El perímetro
             escrito se cerró y el `basename` se abrió EN EL COMMIT DEL PROPIO REMEDIO de O19.
             Es la quinta vez consecutiva que una tanda introduce, al corregir, la puerta que
             el gate siguiente encuentra.
             COBERTURA: ASIGNADO − LEÍDO = 1 —DECISIONES-Y-CONTRADICCIONES.md—, la regla de
             cierre excluye la suficiencia por sí sola, y **C-L.5 pasa de CERTIFICADA a
             ABIERTA por primera vez en cuatro gates**. Los 54 agotamientos pasan las dos
             reglas. La reincidencia U-02/X-06 está ROTA.
             NO HAY NINGUNA DECISIÓN PENDIENTE DEL OWNER: los treinta y seis hallazgos tienen
             remedio determinado dentro de F4c, y AA ordena que el trabajo SIGA y que **NO se
             escriba una protección interna nueva**.
             APLICAR NO ES CERTIFICAR: esta tanda aplica y no cierra nada; F4c sigue ABIERTA y
             F5 sigue NO AUTORIZADA (2026-08-31)
last_meaningful_event_anterior: EL OWNER RESPONDE LA RATIFICACIÓN que el TERCER GATE DE CERTIFICACIÓN
             le elevó como la única decisión que le tocaba a él, y su respuesta es O19: RATIFICA
             EL TEXTO AMPLIO DE O18 Y ORDENA DARLE SEDE CANÓNICA EN docs/owner/. Sus palabras:
             «la omisión está en la transcripción del coordinador, no en mi resolución
             original».
             O19 REVISA LA PROYECCIÓN INCOMPLETA de O18, no su contenido ni su diseño; la
             entrada corta de O18 se CONSERVA sin editar como registro histórico de esa
             transcripción; y la DISPUTA REGISTRADA Y NO RESUELTA que aquella entrada declaraba
             queda RESUELTA por O19 sin tocar su texto. Las condiciones omitidas y el reparto
             PERTENECÍAN a la resolución original, y lo que seis sedes rotulaban «literal de
             O18» pasa a ser literal DE LA SEDE CANÓNICA.
             NACE docs/owner/ADS-OWNER-RESOLUCIONES.md, APPEND-ONLY, con el texto íntegro de
             O17, de O18 —versión amplia ratificada— y de O19. O1-O16 NO se reconstruyen ahí y
             conservan su registro histórico, por orden expresa del Owner en esta misma
             ratificación: no se inventa lo que no consta.
             LO QUE ESTA TANDA REGISTRA EN EL APARATO: el sobre de ancla ancla la sede y no se
             emite sin ella; el inventario de inmutables alcanza docs/owner/; el registro
             ENLAZA a la sede y no la amplía; y el índice enlaza la sede EN EL MISMO COMMIT QUE
             LA CREA. Sin escribir una protección interna nueva, que es lo que el Owner y el
             adjudicador prohibieron.
             RATIFICAR NO ES CERTIFICAR y APLICAR NO ES CERTIFICAR: ningún hallazgo se declara
             SUPERADO, F4c sigue ABIERTA y F5 sigue NO AUTORIZADA, y O19 lo dice con todas las
             letras (2026-08-30)
last_meaningful_event_anterior: EL TERCER GATE DE CERTIFICACIÓN DEVUELVE INSUFICIENTE PARA F5 sobre
             la candidata 21f1ccb, y el gate es VÁLIDO. Su documento es el que deriva la regla
             2 de `regla_de_reanclaje`; su recuento, sus severidades y su clasificación A/B/C
             NO se copian aquí y viven en §12 y §13 de la adjudicación de X.
             Es el PRIMER gate cuyo ancla llega por un canal EXTERNO al repositorio, como O18
             ordena, y esa parte FUNCIONÓ: el sobre se entregó dentro del encargo, idéntico a
             los dos revisores, antes de leer, y es reconstruible. Lo que falla es la
             PRODUCCIÓN del sobre, no su ENTREGA: el emisor vive dentro del árbol que ancla,
             lee del directorio de trabajo y no comprueba `git status`, y con eso produce un
             sobre idéntico al honesto sobre un corpus corrupto sin commitear nada. La
             circularidad no se cerró: se MOVIÓ. O18 NO queda refutada, y el adjudicador
             recomienda que el trabajo SIGA y que NO se escriba una decimonovena protección
             interna.
             NO falla por cobertura: C-L.5 queda CERTIFICADA por CUARTA vez consecutiva, las
             dos restas son ∅ y los agotamientos pasan las dos reglas. Y NO falla por C.
             LO QUE ESTA TANDA HACE EN EL REGISTRO, sin resolver lo que no le toca: O18 recibe
             la declaración de INVERIFICABILIDAD que O17 ya tenía (X-02, GRAVE) y que el
             adjudicador declara ejecutable por F4 diga lo que diga el Owner; la DISPUTA sobre
             el alcance de la condición previa de O18(c) queda REGISTRADA Y NO RESUELTA en la
             propia entrada de O18 —UNA condición en su sede frente a TRES en seis sedes, la
             corroboración contemporánea del mensaje de `bcee159`, la anomalía de forma frente
             a O17 cuyo reparto nace en `8e70d94`, y la inexistencia de sede del Owner en su
             propia mano—, SIN recortar la propagación y SIN completar O18, porque ninguna de
             las dos vías es ejecutable por F4 (G21 de KERNEL.md); el preámbulo de D107 deja de
             decir «texto ÍNTEGRO» y dice «texto RESOLUTIVO», con la reconciliación de lo que
             de verdad se editó —celda de D97 en `8c3afe7` y celda de D92 en `78ec1cc`, un
             puntero y una corrección de cita, ninguna resolución tocada—; y este bloque de
             estado se REANCLA, con la regla que lo obliga a reanclarse escrita dentro.
             C-L.7 pasa de CERRADA a NO CERRADA. LA RATIFICACIÓN DE O18 QUEDA PENDIENTE DEL
             OWNER. APLICADA NO ES CERTIFICADA: F4c sigue ABIERTA y F5 sigue NO AUTORIZADA
             (2026-08-30)
last_meaningful_event_anterior: EL OWNER RESPONDE la única decisión de clase B del documento
             23 —LA RAÍZ, la que ningún gate anterior había llevado a nadie—, y su respuesta se
             registra como O18, RESOLUCIÓN ESCALONADA: RECHAZA expresamente (a) —retirar la
             garantía—, ADOPTA (b) —ancla documental externa, declarada TRANSITORIA y
             explícitamente limitada— para cerrar F4c, y hace (c) —verificador externo real—
             OBLIGATORIA EN F6. Con ella esa clase B queda RESUELTA y YA NO BLOQUEA. Se propaga
             como D108, DERIVADA y no elegida por F4: el SOBRE DE ANCLA pasa a ser requisito de
             todo gate de F4c, con sus obligaciones para coordinador, revisores y adjudicador, y
             el CONTRATO DEL VERIFICADOR EXTERNO DEL CONTROL REPO queda registrado para F6, sin
             una línea implementada. Se aplican los hallazgos de clase A del documento 23.
             O1–O17 y D1–D107 conservan su texto resolutivo; nada se renumera; NINGÚN hallazgo
             se declara SUPERADO. APLICADA NO ES CERTIFICADA (2026-08-30)
last_meaningful_event_anterior: el SEGUNDO GATE DE CERTIFICACIÓN —ocho agentes de contexto
             limpio sobre e316396, cadenas S y T en paralelo y sin verse, adjudica U— devuelve
             INSUFICIENTE PARA F5, y trae algo que ningún gate anterior había traído: LA RAÍZ.
             M-04 no es satisfacible desde dentro de F4, como §11.4 del documento 11 ya había
             declarado, y la pregunta con sus tres alternativas se eleva al Owner en §13 de la
             adjudicación de U. Ningún hallazgo se corrigió en esa pasada, y fue deliberado
             (2026-08-30)
last_meaningful_event_anterior: EL OWNER RESPONDE la única decisión de clase B del documento 22, y su
             respuesta se registra como O17. Elige la alternativa (b): el nivel ESTRUCTURAL
             lo produce CADA MACROCIRCUITO AL ARRANCAR, como precondición propia de esa
             ejecución. Su motivo, en sus palabras, es robustez y revalidación permanente
             por encima del ahorro operativo: descarta (a) porque un producto ya instalado
             no revalidaría su Estructural al cambiar el kernel, y descarta (c) porque
             obliga a reescribir §9.2 y CAMBIA el contenido de O12, que es resolución suya.
             O17 fija DOCE reglas obligatorias y el reparto SIS/VER/PLT/SEG. Con ella, O12
             pasa a ser SATISFACIBLE desde cualquier entrada, y el coste —un gate más en
             los cuatro recorridos— el Owner lo acepta expresamente.
             Se propaga como D107, DERIVADA y NO elegida por F4: §9.6 gate:sistema-conforme
             con productor, sujeto, evidencia, vigencia y condición de invalidación · FASE 0
             en §8.1, §8.2, §8.3 y §8.4 · filas en §18 · X-S1–X-S9 · y los bloques de §15.8
             que faltaban para D96–D107, con lo que la regla del ordinal vuelve a ejecutar.
             PN-17 y PN-18 se registran como presiones nuevas. Se aplican los 68 hallazgos
             de clase A del documento 22, agrupados POR CAUSA. Se publica el
             CORRIGENDUM-DICTAMENES-INMUTABLES.md, que señala errores de hecho de dictámenes
             y manifiestos SIN tocarlos, y el índice gana la sede desde la que se enlaza todo
             lo que C-L.5 obliga a publicar, que era la laguna estructural de T147.
             O1–O16 y D1–D106 conservan su texto; nada se renumera; NINGÚN hallazgo se
             declara SUPERADO. **APLICADA NO ES CERTIFICADA**: F4c sigue ABIERTA y F5 sigue
             NO AUTORIZADA (2026-08-30)
last_meaningful_event_anterior: el GATE INDEPENDIENTE DE CERTIFICACIÓN CON UNIVERSO DERIVADO
             —diez agentes de contexto limpio sobre 4d231ee— devuelve INSUFICIENTE PARA F5
             por SEIS razones y NO por cobertura. 69 hallazgos: A 68 · B 1 · C 0. C-L.5
             sigue CERTIFICADA. Ningún hallazgo se corrigió en esa pasada, y fue
             deliberado (2026-08-30)
last_meaningful_event_anterior: se APLICA la TANDA DE CORRECCIÓN del gate de cobertura. D104, D105 y
             D106, todas revisoras; D1–D103 conservan su texto y O1–O16 quedan intactas,
             con O16 ganando sólo un ADDENDUM DE CRONOLOGÍA que fija desde cuándo está
             respaldada, sin reescribirla y sin inventar ninguna cita.
             D104 · la derivación de <CAP>:revision pasa a CUATRO VÍAS TIPADAS con un
             discriminante ESTRUCTURAL —pertenencia al conjunto de las quince, no búsqueda
             de la palabra «DERIVADO» en un campo {tipo: texto}— y un ANCLA que ya no
             presupone VER. La cifra se deriva y sigue dando cinco procesos y nueve pares.
             D105 · la referencia entre abandonada y su deriva se INVIERTE: el que llega
             después nombra al que ya existe, con lo que el segundo terminal vuelve a ser
             emitible. El deriva gana fsync de fichero y directorio, el marcador de
             transacción se MANTIENE hasta que es durable, el arranque COMPLETA el deriva
             ausente de forma idempotente, y nace la ventana W17. El recuento pasa a
             DIECIOCHO y se deriva de las filas.
             D106 · la prueba de PN-15 deja de ser una disyunción que su propia decisión
             satisfacía; C-L.5 pasa a exigir DOS manifiestos publicados, de ASIGNACIÓN y de
             LECTURA; y O16 gana su addendum de cronología.
             LA BATERÍA, REFUTADA POR EL GATE, queda corregida: las cuatro refutaciones se
             demostraron ANTES y DESPUÉS, y las cuatro fallan ahora con diagnóstico.
             Los 21 hallazgos quedan en CUATRO estados: 17 CORREGIDOS EN F4c, 2 REGISTRADOS
             PARA F5, 1 CONTRATADO PARA F6, 1 ABIERTO PARA EL SIGUIENTE GATE.
             **APLICADA NO ES CERTIFICADA**, y C-L.5 sigue ABIERTA (2026-08-29)
last_meaningful_event_anterior: el GATE INDEPENDIENTE DE COBERTURA Y CIERRE —M y N en paralelo,
             adjudicados por O con contexto limpio— devuelve INSUFICIENTE PARA F5 sobre
             r2=c3d6465. Es la PRIMERA pasada que lee ÍNTEGRAS las cuatro fuentes que C-L.5
             nombra, y las lee POR TRIPLICADO; N cierra además las catorce fuentes y las
             quince fichas que tres gates dejaron sin abrir, incluido el documento 15, y
             contesta las dos preguntas que el adjudicador I declaró irresolubles: los
             BLOQUES B y C CONFIRMAN a F4, y b.3 y b.5 NO refutan I-08.
             Y aun con la cobertura cerrada en su núcleo, el gate falla POR EL FONDO:
             C-L.3 no cerrada por TRES causas independientes; un defecto arquitectónico
             NUEVO que hace INEMITIBLE el terminal `abandonada`; una laguna de durabilidad
             con fallo silencioso que deja el diario irreparable; la batería REFUTADA —dos
             árboles defectuosos pasan 30/30 en verde—; tres sedes vigentes que el árbol
             desmiente; y la regla de cierre de C-L.5 no certificable.
             21 hallazgos consolidados, CERO rechazados: GRAVE 5 · MEDIO 6 · MENOR 10.
             NINGUNO SE HA CORREGIDO, y eso incluye los que caen sobre este mismo fichero
             (M-06) y sobre la batería (M-04, M-11, M-12, O-01, O-02): corregirlos durante
             el gate volvería a hacer que quien recibe sea quien aplica (2026-08-29)
last_meaningful_event_anterior: CORRECCIÓN TÉCNICA ACOTADA sobre la candidata publicada, y es D103.
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
  · RECUENTO CORREGIDO ENTONCES a «DIEZ presiones vigentes». El corpus decía 8, 10 y 11
    a la vez. [CIFRA DE AQUEL MOMENTO: el censo vigente lo deriva §16 del documento 11]
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
  · «DIEZ presiones normativas vigentes» ENTONCES. Ninguna renumerada. **Corregido**: el
    titular decía
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
  · LAS «OCHO PRESIONES NORMATIVAS» DE ENTONCES quedan CONFIRMADAS como bien identificadas
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
  · PN-7 a PN-10 registradas. «Ocho presiones vigentes» ENTONCES. Ninguna redactada
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
owner_captado: LA AUTORIDAD CANÓNICA DE LO QUE EL OWNER HA RESUELTO NO ES ESTE CAMPO, Y DESDE
             O19 NO ES NINGUNA PARÁFRASIS DEL COORDINADOR: es
             docs/owner/ADS-OWNER-RESOLUCIONES.md, donde viven O17, O18 —texto amplio
             RATIFICADO— y O19 con su texto íntegro. Este campo NO los transcribe: remite.
             LO QUE ESTE CAMPO CONSERVA DE O15 Y O16 ES TRANSCRIPCIÓN DEL COORDINADOR, se
             declara como tal y NO ES AUTORIDAD CANÓNICA. No se borra ni se reescribe: el Owner
             ordenó expresamente que O1-O16 NO se reconstruyan en la sede y conserven su
             registro histórico hasta que exista una ratificación expresa o una fuente primaria
             verificable. Y es exactamente la clase de defecto que O19 corrige: una resolución
             que sólo constaba porque el coordinador la transcribía, sin nada contra lo que
             contrastarla.
             O17, O18 Y O19 NO SE TRANSCRIBEN AQUÍ. Su sede es la canónica; su proyección, la
             sección 2 de docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md, que ENLAZA a ella.
             NINGUNA de las tres autoriza iniciar F5, F6 ni PesquerApp.
             [TRANSCRIPCIÓN DEL COORDINADOR · NO ES SEDE CANÓNICA · se conserva sin editar]
             "Autoriza aplicar la crítica independiente de F4 y corregir su
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
pregunta_pendiente: NINGUNA. La última que había —la RATIFICACIÓN que el TERCER GATE DE
             CERTIFICACIÓN elevó, y que no era una elección de diseño— la RESPONDIÓ el Owner, y
             es O19: ratifica el texto amplio de O18 y ordena su sede canónica. LA RATIFICACIÓN
             QUEDA CERRADA y O18 no vuelve a someterse a elección. Antes de ella, la clase B del
             documento 22 —el nivel ESTRUCTURAL y su productor— la respondió O17 con la
             alternativa (b). Ninguna de las dos bloquea ya, y NINGUNA autoriza iniciar F5.
             Su texto no se copia aquí: la sede es docs/owner/ADS-OWNER-RESOLUCIONES.md.
             Las presiones normativas vigentes son materia de F5, no preguntas, y SU CENSO
             NO SE ESCRIBE AQUÍ. Este campo publicó una cifra a mano tres tandas seguidas y
             las tres caducaron —Q-12 y Q-13 del documento 22—, así que REMITE: la única
             sede que publica el total es §16 del documento 11, y se deriva con
               grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
                 | grep -vc 'RETIRADA\|FUSIONADA'
             que es cabeceras `## `PN-` menos las marcadas RETIRADA o FUSIONADA.
             QUÉ TANDA AÑADIÓ CADA UNA TAMPOCO SE ESCRIBE AQUÍ: se DERIVA de git, una a una,
                 git log --oneline -S'## `PN-<n>`' -- docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
             Ninguna anterior se renumera.
             **[HISTÓRICO · lo que este campo afirmaba, y era falso cuando el CUARTO GATE lo
             leyó]** *«Las que ESTA tanda añade son PN-17 y PN-18»*. El barrido de arriba lo
             desmiente: PN-17 y PN-18 nacen en la tanda de O17 y PN-19 en la de O18, y la
             tanda que escribió la frase no añadió ninguna. Es `Y-10` del documento 25,
             MEDIO, clase A, y es la clase `X-04` otra vez: dos eventos de retraso **en el
             renglón que presumía de remitir en vez de copiar**. La frase no se sustituye por
             otra cifra: se retira el hecho copiado y se pone el comando que lo deriva.
siguiente:   NO SE ESCRIBE AQUÍ, Y ES DELIBERADO — regla 1 de `regla_de_reanclaje`. Este
             campo copiaba lo que la sección **«Siguiente acción exacta»** de este mismo
             fichero deriva, y por eso caducó con la tanda de O17/D107: nombraba el documento
             22 cuando ya existían el 23, O18, D108 y el 24. Su sede única es la PRIMERA
             sección titulada «Siguiente acción exacta», que se localiza con
                 grep -n '^## Siguiente acci[óo]n exacta' docs/evolucion/CHECKPOINT-ADS-NEXT.md | head -1
             y las que le siguen van rotuladas HISTÓRICA. Lo único que este campo afirma, y
             que no caduca: **APLICADA NO ES CERTIFICADA**, y REGISTRAR o CONTRATAR no es
             CORREGIR. F4c sigue ABIERTA y F5 sigue NO AUTORIZADA. La RATIFICACIÓN de O18
             YA NO ESTÁ PENDIENTE: la dio el Owner en O19, y RATIFICAR TAMPOCO ES CERTIFICAR —
             O19 revisa la PROYECCIÓN, no el contenido, y no autoriza iniciar F5.
             **[HISTÓRICO · lo que este campo copiaba en la tanda de O17/D107. Se conserva y
             NO describe el estado vigente.]**
             PUBLICAR UNA CANDIDATA NUEVA y someterla a OTRO GATE INDEPENDIENTE, con
             revisores de contexto limpio que NO sean quien aplicó esta tanda — y **que
             publique los DOS manifiestos que D106 exige**: el de ASIGNACIÓN antes de
             repartir y el de LECTURA por revisor, ENLAZADOS desde 00-INDICE.md en el mismo
             commit que los crea, que es la regla que cierra la laguna de T147.
             Sin los dos manifiestos, su adjudicador tendrá que declarar la regla de cierre
             de C-L.5 NO CERTIFICABLE, como hizo O.
             Antes de eso: O17 está RECIBIDA y en propagación (D107), y los 68 hallazgos de
             clase A del documento 22 se están aplicando.

             **[HISTÓRICO · el estado que dejó la tanda de D96–D103. La clasificación
             VIGENTE está más abajo, tras el gate del documento 21.]**
             CÓMO QUEDABA CADA CONDICIÓN ENTONCES, en CINCO estados primarios MUTUAMENTE
             EXCLUYENTES. Un estado por id, los trece ids exactamente una vez, y NINGÚN
             subhallazgo contado como condición:
               CORREGIDAS EN F4c     8   C-L.1 C-L.3 C-L.4 C-L.6 C-L.7 C-L.8 C-L.9 C-L.11
               REGISTRADAS PARA F5   2   C-L.2 (PN-15, decide el Owner) · C-L.12
               CONTRATADA PARA F6    1   C-L.10 — CERO líneas de código escritas
               MIXTA POR DESGLOSE    1   C-L.13 — sus SEIS componentes son atributos
                                         SECUNDARIOS y no cuentan como condiciones:
                                         K-05 K-09 K-10 K-08 L-03 corregidos ahora ·
                                         J-11 contratado para F6, NO implementado
               ABIERTA POR COBERTURA 1   C-L.5
                                    ──
                                    13   = los trece ids distintos, sin doble conteo
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
                      o NINGUNA según su propietario derivado — «cero o un par, nunca dos».
                      **[HISTÓRICO] Esa última regla de D103 está DEROGADA por D104**, que
                      M-01 obligó a rehacer: un item de AUD puede exigir NINGUNO, DOM, SEG
                      **o LOS DOS**, según su propietario efectivo y sus condicionales
                      activas. Son CUATRO combinaciones, no dos.
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
               C-L.10 CONTRATADA PARA F6 · única en este estado. D102: tres contratos —censo
                      AFIRMACIONES derivado, T152 sobre toda sede que publique versión, y la
                      guardia de intérprete con exit 2— y ocho casos de regresión.
                      **CERO líneas implementadas.** T151 y T152 siguen pasando en verde
                      sobre las sedes que el corpus desmiente. Contratar NO es implementar
               C-L.11 CERRADA · D101: §6.7 recibe fila propia X62. X51 conserva su escenario
               C-L.12 REGISTRADA PARA F5 · los dos restos de (b) —«(P7)» donde aplica P9 en
                      L358, y la numeración 1,2,5,3,4 de L462–472— quedan como checklist
                      verificable, con ruta, ubicación, corrección exacta y prueba. Sin PN
                      nueva: el contenido no cambia. **El texto de (b) sigue como estaba**
               C-L.13 MIXTA, SATISFECHA POR DESGLOSE · es la ÚNICA con estado compuesto,
                      y sus seis componentes son atributos SECUNDARIOS que no cuentan como
                      condiciones: K-05, K-09, K-10, K-08 y L-03 CORREGIDOS ahora; J-11
                      CONTRATO COMPLETO PARA F6 en D102, NO implementado

             F5 NO arranca sin un veredicto explícito de SUFICIENCIA.

             ESTADO TRAS EL GATE INDEPENDIENTE DE COBERTURA Y CIERRE (documento 20), que
             adjudica las trece una a una y NO corrige ninguna:
               CERRADAS                              7   C-L.1 C-L.6 C-L.7 C-L.8 C-L.9
                                                         C-L.11 C-L.13
               REGISTRADAS PARA F5                   2   C-L.2 (con M-05 en su cuerpo) · C-L.12
               CONTRATADA PARA F6                    1   C-L.10 — cero líneas, verificado
               CERRADA EN LA FORMA, NO EN EL FONDO   1   C-L.4  (M-07: las fechas no cuadran)
               NO CERRADA                            1   C-L.3  ← una de las cinco que bloquean
               ABIERTA                               1   C-L.5  (núcleo satisfecho; regla de
                                                         cierre no certificable, O-04)
                                                    ──
                                                    13   cada id exactamente una vez

             CÓMO QUEDA CADA CONDICIÓN — **CLASIFICACIÓN VIGENTE**, tras el GATE
             INDEPENDIENTE DE CIERRE CON MANIFIESTOS (documento 21), las tandas que lo
             siguen, **la ACTUALIZACIÓN que impuso el TERCER GATE DE CERTIFICACIÓN
             (documento 24) sobre C-L.7** y **la que impone el CUARTO (documento 25) sobre
             C-L.5**. Los estados primarios son los que ROTULA el bloque de abajo, uno por
             renglón, y el titular NO los cuenta: son MUTUAMENTE EXCLUYENTES, con un estado
             por id, los trece ids exactamente una vez, y NINGÚN subhallazgo contado como
             condición:
               CORREGIDAS EN F4c     7   C-L.1 C-L.3 C-L.4 C-L.6 C-L.8 C-L.9 C-L.11
               NO CERRADA            1   C-L.7 — la MUEVE aquí el documento 24, por X-04
               REGISTRADAS PARA F5   2   C-L.2 (PN-15, decide el Owner) · C-L.12
               CONTRATADA PARA F6    1   C-L.10 — CERO líneas de código escritas
               MIXTA POR DESGLOSE    1   C-L.13 — sus SEIS componentes son atributos
                                         SECUNDARIOS y no cuentan como condiciones:
                                         K-05 K-09 K-10 K-08 L-03 corregidos ·
                                         J-11 contratado para F6, NO implementado
               ABIERTA               1   C-L.5 — la REABRE el CUARTO GATE DE CERTIFICACIÓN,
                                         documento 25, por ASIGNADO − LEÍDO = 1
                                    ──
                                    13   = los trece ids distintos, sin doble conteo
               **[HISTÓRICO · hasta el documento 24 esta clasificación contaba OCHO
               CORREGIDAS EN F4c, con C-L.7 entre ellas, y CINCO estados. El texto anterior
               NO se borra: queda dicho aquí que era eso, y por qué dejó de serlo.]**
               **[HISTÓRICO · hasta el documento 25, C-L.5 figuraba como «CERTIFICADA POR
               COBERTURA · 1 · la CERTIFICÓ el adjudicador R del documento 21, y el
               documento 24 la CERTIFICA por cuarta vez consecutiva». Dejó de serlo por la
               resta del CUARTO gate, y el renglón anterior no se borra: queda dicho aquí.]**

             LAS TRECE FILAS DE DETALLE, que son la sede canónica de esta clasificación:
               C-L.1  CERRADA · D96: revision_base OBLIGATORIO en §3.6 y participante en tx
               C-L.2  REGISTRADA PARA F5 · D97 crea PN-15. La decisión sigue SIN TOMAR: es
                      del Owner. Registrar NO es corregir
               C-L.3  CERRADA · **por D104, y NO por D103**, que M-01 refutó. La regla
                      vigente: un item de proceso:AUD exige NINGUNO, DOM, SEG **o LOS DOS**,
                      según su propietario efectivo y sus condicionales activas — CUATRO
                      combinaciones, y las cuatro se derivan. El catálogo estático da CINCO
                      procesos y NUEVE pares, con (DEP, SEG) por la obligatoria, y el
                      reparto por vía se publica y se contrasta (Q-03). D104 aparece ahora en
                      TODAS las sedes vigentes de esta condición, que es lo que Q-14 pidió
               C-L.4  CERRADA · D106 (iii): O16 gana su ADDENDUM DE CRONOLOGÍA, con las dos
                      fechas verificadas en git log por el adjudicador R
               C-L.5  ABIERTA · **la REABRE el CUARTO GATE DE CERTIFICACIÓN, documento 25,
                      y es la PRIMERA VEZ EN CUATRO GATES que deja de estar certificada.**
                      La causa es la RESTA, y no un hallazgo: `ASIGNADO − LEÍDO = 1` en el
                      lote del revisor `Y` —`docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`,
                      1 196 líneas, sin manifiesto de lectura íntegra—, y la propia regla de
                      cierre de esta condición dice que *«cualquier fuente ASIGNADA pero NO
                      LEÍDA impide la suficiencia, con independencia de los hallazgos»*. El
                      dictaminador lo declaró **contra su propia cadena** antes de que nadie
                      se lo señalara, y el adjudicador AA lo confirmó: §8 del manifiesto
                      EXCLUYE la suficiencia por sí solo.
                      **NADA se declara SUPERADO ni CERRADO por registrarlo aquí**, y esta
                      tanda NO la cierra: sólo la vuelve a certificar un gate independiente
                      con la resta a ∅ y manifiesto de lectura por revisor.
                      **[HISTÓRICO] Su estado anterior era CERTIFICADA** —por el gate del
                      documento 21, con manifiesto previo de ASIGNACIÓN commiteado antes de
                      existir ningún revisor, sus manifiestos de LECTURA y la resta a ∅, y
                      renovada por los documentos 22, 23 y 24—; deja de estarlo aquí.
                      **Certificar la cobertura no cerraba F4c ni autorizaba F5, y perderla
                      tampoco cierra nada: sólo impide certificar.**
                      CONSECUENCIA DECLARADA **SIN COPIAR SU RESULTADO, que es lo que
                      `AA-02` castigó**: la declaración no escribe si la batería está en
                      rojo — publica el comando que lo decide, y así no puede caducar ni ser
                      falsa en el commit que la escribe.
                          grep -c '"ABIERTA"' \
                            docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py
                          python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py | grep G-16
                      **MIENTRAS el primero devuelva 0, `G-16` dará ROJO sobre esta
                      clasificación, y ese rojo es VERDADERO**: dice que el vocabulario de
                      estados primarios del instrumento no conoce «ABIERTA» y sigue
                      describiendo la clasificación anterior, la que este gate falsó.
                      El remedio —«ABIERTA» en `_ESTADOS_CL` y en `_CANON`— vive en
                      `docs/evolucion/verificacion/`, **que este registro NO escribe**; en
                      cuanto ese fichero lo incorpore, el primer comando deja de dar 0 y el
                      segundo se pone en verde **sin que haya que tocar este renglón**.
                      **No se escribe «CERTIFICADA» aquí para poner la batería en verde**:
                      eso sería el mutante que `Q-06` cerró
               C-L.6  CERRADA · las CINCO salidas del gate de M7 en §8.3
               C-L.7  NO CERRADA · **la MUEVE aquí el TERCER GATE DE CERTIFICACIÓN,
                      documento 24, hallazgo X-04, GRAVE, y es la CUARTA RECURRENCIA
                      CONSECUTIVA de la clase** (K-01/J-10/L-01 · P-05≡Q-08/R-02 ·
                      S-17≡S3-05 · X-04). El enunciado —«el checkpoint reancla su estado en
                      cada tanda»— quedó FALSADO sobre el árbol que ese gate juzgó: el
                      BLOQUE DE ESTADO ESTRUCTURADO de este fichero, el del formato de a.10,
                      iba DOS eventos atrasado —sin el documento 23, sin O18, sin D108, y
                      luego tampoco el documento 24— NO estaba dentro de ningún [HISTÓRICO]
                      ni [ESTADO ANTERIOR], y llevaba `actualizado: 2026-08-30`.
                      **[HISTÓRICO] Su estado anterior era CERRADA**, y lo estuvo desde la
                      tanda de D96–D103; deja de estarlo aquí.
                      QUÉ SE HA HECHO EN ESTA TANDA: el bloque queda REANCLADO —metodo,
                      metodo_anterior, based_on, last_meaningful_event y siguiente— y
                      recibe un campo nuevo, `regla_de_reanclaje`, que escribe DENTRO del
                      propio bloque la garantía general de la clase: nada que otra sede
                      pueda derivar se copia aquí, el último documento y la última
                      resolución se DERIVAN con su comando, y todo evento nuevo reancla el
                      bloque EN EL MISMO COMMIT que lo registra.
                      **NO se declara SUPERADO**: reanclar no es certificar, y sólo un gate
                      independiente posterior puede cerrar X-04 y devolver C-L.7 a CERRADA.
                      **[HISTÓRICO · CONSECUENCIA DECLARADA que era FALSA EN EL COMMIT QUE
                      LA ESCRIBIÓ. Se conserva marcada, no se borra, y es `AA-02` del
                      documento 25, GRAVE.]** Este renglón decía: *«el evaluador `G-16` de
                      la batería tiene escritos CINCO estados primarios y NO conoce «NO
                      CERRADA», de modo que mientras no lo aprenda saldrá en ROJO sobre esta
                      clasificación. Ese rojo es VERDADERO … El remedio es de dos líneas
                      —`NO CERRADA` en `_ESTADOS_CL` y en `_CANON`— y vive en
                      `docs/evolucion/verificacion/`, que este registro NO escribe.»*
                      **EL MISMO COMMIT que escribió eso —`5343260`— aplicó el remedio a la
                      batería**, y el adjudicador lo midió con
                      `git log --oneline -S` sobre los dos ficheros. Y lo peor: **TRES
                      revisores citaron la frase como prueba de honradez y ninguno ejecutó
                      `G-16`.** Una afirmación rancia redactada en forma de autocrítica
                      cobró crédito de tres revisores independientes.
                      **LO QUE ES VERDAD HOY, ejecutado sobre este árbol y no supuesto:**
                      `_ESTADOS_CL` de la batería **YA contiene «NO CERRADA»**, su `_CANON`
                      también, y `G-16` pasa en VERDE sobre el estado NO CERRADA de esta
                      condición. Lo que hoy la pone en rojo es OTRA cosa, y es la fila de
                      `C-L.5`: el vocabulario no conoce «ABIERTA». Ahí está declarado, con
                      su medición.
                      **No se escribe «CERRADA» aquí para poner la batería en verde**: eso
                      sería exactamente el mutante que `Q-06` cerró
               C-L.8  CERRADA · el hash_previo de la reparación, unificado para las tres causas
               C-L.9  CERRADA · X62 da fila propia a §6.7, y G-26 deriva los recuentos
               C-L.10 CONTRATADA PARA F6 · censo AFIRMACIONES derivado y T152 sobre toda sede
                      que publique versión, más el CONTRATO 1bis de los perfiles (N-04).
                      Contratar NO es implementar: CERO líneas escritas
               C-L.11 CERRADA · fila adversarial propia para §6.7
               C-L.12 REGISTRADA PARA F5 · los dos restos de (b), como checklist E5.
                      **Y uno de ellos deja de ser sólo checklist**: E5-3 se eleva a PN-16
                      por P-07, porque puede exigir que F5 enmiende (b). Registrar NO es
                      corregir: el texto de (b) sigue como estaba
               C-L.13 MIXTA · K-05 K-09 K-10 K-08 L-03 corregidos · J-11 CONTRATADO PARA F6
                      y NO implementado
             FIN DE LA CLASIFICACIÓN VIGENTE

             LO QUE EL GATE DEJA ABIERTO, sin corregir y por orden expresa:
               M-01 M-02 M-03 M-04 N-01                    GRAVES · cuatro bloquean el paso
               M-05 M-06 M-07 N-02 O-01 O-03                MEDIOS
               M-08 M-09 M-10 M-11 M-12 N-03 N-04 N-05      MENORES
               O-02 O-04

             Y consta que el gate NO falla por cobertura: O lo dice expresamente —«habría
             fallado igual con C-L.5 cerrada»—. Falla por el fondo.
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
    corresponde, y por eso este bloque ya no dice «DIEZ presiones» ni se detiene en D63.
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
  · **[HISTÓRICO · el censo del momento de esa tanda]** TRECE PRESIONES NORMATIVAS
    VIGENTES —PN-1, PN-2, PN-3, PN-6 a PN-15—. El total se
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
    no escritas a mano; X62 la añade esta tanda por J-03—, las **18** ventanas de caída
    `W1`–`W17` de §2.6.5 —también derivadas de sus filas—, las **8** comprobaciones `X-A`–
    `X-H`, los 11 escenarios negativos de §11.5 y los 12 escenarios de §14 están ESCRITOS.
    Ninguno ejecutado.
    **Corregido por `P-04`**: esta línea contaba «las 9 ventanas `RC-1`–`RC-9` de §2.6.9»,
    que `D64` RETIRÓ y que `D83` renombró precisamente para sacarlas del inventario — la
    corrección que este mismo fichero declara aplicada en `M-8`, quinientas líneas más abajo.
    Contarlas era inflar el inventario con algo inexistente, que es lo que `11-ARQ` dice con
    todas las letras. Y omitía las ocho `X-A`–`X-H` que el documento 11 sí cuenta
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
                             cerradas o registradas—. C-L.5, la COBERTURA, quedó
                             CERTIFICADA por el gate del documento 21 y SIGUE CERTIFICADA
                             tras el del 22, ahora sobre universo derivado; el estado de
                             cada C-L NO se copia aquí, sino que lo da la clasificación
                             VIGENTE de este mismo fichero, más abajo.
                             **APLICADAS NO ES CERTIFICADAS.**
                             8ª  GATE INDEPENDIENTE DE CIERRE CON MANIFIESTOS VERIFICABLES
                                 (P·Q, adjudica R) — **INSUFICIENTE PARA F5** sobre
                                 7764cca. 24 hallazgos: BLOQUEANTE 0 · GRAVE 1 · MEDIO 12 ·
                                 MENOR 11. **C-L.5 CERTIFICADA por primera vez.**
                                 documento 21 · su tanda de corrección NO añadió ninguna `D`
                             9ª  GATE INDEPENDIENTE DE CERTIFICACIÓN CON UNIVERSO DERIVADO
                                 (cadenas P1–P4 y Q1·Q2·Q3·Q5·Q4, adjudica R) —
                                 **INSUFICIENTE PARA F5** sobre 4d231ee, por SEIS razones y
                                 NO por cobertura. **69 hallazgos: BLOQUEANTE 0 · GRAVE 8 ·
                                 MEDIO 34 · MENOR 27**, clasificados **A 68 · B 1 · C 0** ·
                                 documento 22
                                 SU CLASE B —el nivel ESTRUCTURAL y su productor— la
                                 RESOLVIÓ EL OWNER: es **O17**, alternativa (b), y su
                                 propagación es **D107**. Los 68 de clase A se están
                                 aplicando. **NINGUNO se declara SUPERADO.**
                             10ª SEGUNDO GATE INDEPENDIENTE DE CERTIFICACIÓN (cadenas
                                 `S1`–`S4` y `T1`·`T2`·`T3`, adjudica `U`) —
                                 **INSUFICIENTE PARA F5** · documento 23. El reparto por
                                 severidad y por clase NO se copia aquí: lo publican §12 y
                                 §13 de la adjudicación de `U`, que es su sede.
                                 SU CLASE B —LA RAÍZ DE CONFIANZA DE LA VERIFICACIÓN, que
                                 no era un hallazgo— la RESOLVIÓ EL OWNER: es **O18**,
                                 ESCALONADA —(a) rechazada · (b) sobre de ancla para cerrar
                                 F4c · (c) verificador externo obligatorio en F6—, y su
                                 propagación es **D108**. Los de clase A se están
                                 aplicando. **NINGUNO se declara SUPERADO, y M-04 tampoco.**
                             CUÁNTAS PASADAS SON NO SE ESCRIBE AQUÍ: se DERIVA de los
                             ficheros `1?-*.md` y `2?-*.md` de este directorio y de las
                             filas de 00-INDICE.md. Esta proyección enumeraba hasta la 7ª
                             mientras el árbol iba por la 9ª — es Q-16 del documento 22, y
                             por eso la enumeración remite en vez de pretender ser el censo.
                             DOS de los hallazgos de la 2ª devolución, TRES de la 3ª, LOS
                             TRES de la segunda corrección técnica, y K-02 del gate
                             definitivo —cuya causa es D75, una corrección anterior— son
                             defectos que las correcciones ANTERIORES introdujeron o no
                             vieron.
                             SIGUE ABIERTA: sólo la cierra un veredicto explícito de
                             SUFICIENCIA emitido por revisores independientes de contexto
                             limpio sobre el resultado corregido, y que NO sean quien lo
                             aplicó. Ese veredicto NO existe
F5  ENMIENDAS                las presiones normativas vigentes que §16 del documento 11
                             deriva —cabeceras `## `PN-` menos las marcadas RETIRADA o
                             FUSIONADA—, enumeradas y sin redactar. **El total NO se copia
                             aquí**: §16 es su única sede, y se obtiene con
                               grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
                                 | grep -vc 'RETIRADA\|FUSIONADA'
                             **NO INICIADA, y NO AUTORIZADA**
F6  DESCOMPOSICIÓN Y EJECUCIÓN  NO INICIADA, y NO AUTORIZADA — y ya tiene un CONTRATO
                             OBLIGATORIO esperándola: el **VERIFICADOR EXTERNO DEL CONTROL
                             REPO** que `O18` impone y que `D108`(v) registra COMPLETO y
                             SIN IMPLEMENTAR, con propietario, ejecutor, autoridad, fase,
                             pruebas y condición de cierre. Es **CONDICIÓN PREVIA** a la
                             adopción permanente de PesquerApp, a declarar ADS operativo y
                             a certificar adaptadores. **`O18` lo contrata; no autoriza
                             construirlo hoy ni iniciar F6**
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
python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py
```

> **DOS CONDICIONES QUE HAY QUE CUMPLIR PARA QUE ESAS DOS LÍNEAS SEAN VERDAD**, y las dos las
> levantó `P-27`≡`Q-08` del documento 22, que encontró el árbol en **12/13** con `T147` en rojo
> y `git status` sucio mientras esta misma sección afirmaba lo contrario, sin marca.
>
> 1. **La evidencia derivada se republica en el MISMO commit que cambia el corpus.** Añadir o
>    quitar un documento mueve los recuentos que `fuentes-salida.txt` y `negativos-salida.txt`
>    publican, y hasta que el runner vuelve a correr el árbol queda sucio. No es un defecto del
>    runner: es la disciplina de un derivado.
> 2. **Todo documento que `C-L.5` obliga a publicar se ENLAZA desde `00-INDICE.md` en el mismo
>    commit que lo crea.** `T147` exige que ningún documento exista para nadie, y `C-L.5` exige
>    que cada gate publique su manifiesto de asignación y sus manifiestos de lectura. Sin la
>    regla, **cada gate rompía `T147` una vez más**: es una laguna estructural, no una errata.
>    La sede desde la que se enlazan es la sección *«Lo que cada gate tiene que publicar, y
>    desde dónde se enlaza»* de [`00-INDICE.md`](00-INDICE.md), y **no se arregla con
>    `exclusiones.yaml`**: una exclusión apaga la comprobación en vez de cumplirla.
>
> **Y consta la atribución, porque sin ella el dato engaña**: los huérfanos que dispararon el
> hallazgo los introdujo el aparato del propio gate, no la tanda que juzgaba. `R` no resolvió a
> quién se imputa, y este fichero tampoco lo resuelve: registra la laguna y la cierra.
>
> El aparato de verificación —batería, manifiestos, addenda y el
> [`CORRIGENDUM-DICTAMENES-INMUTABLES.md`](verificacion/CORRIGENDUM-DICTAMENES-INMUTABLES.md),
> que señala errores de hecho de dictámenes ya publicados **sin tocarlos**— está enumerado en
> esa misma sección del índice.

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
> `PRESIONES` decía ONCE cuando el derivado ya daba más. **Los dos bloques quedan marcados, y
> ninguno se borra.** Y desde `Q-12` del documento 22, este bloque **ya no publica el total**:
> lo REMITE a §16 del documento 11, porque una cifra copiada envejece sola y ésta envejeció
> tres veces.
>
> **CIFRAS VIGENTES, DERIVADAS de la tabla de abajo y no copiadas de ningún resumen:**
>
> ```text
> ESTADO PRIMARIO      31 CORREGIDO_EN_F4 · 2 PRESION_LISTA_PARA_F5 —B-2 y F-01— ·
> DE LOS 43            2 CONTRATO_COMPLETO_PARA_F6 —M-5 y M-6— · 7 EXTERNO_CON_PROPIETARIO
>                      —F-02 F-04 F-06 F-07 F-08 F-10 F-11— · 1 HISTORICO_NO_APLICABLE —m-3—
>                      = 43. Adjudicadas por `L`: 42 SUPERADAS · 0 FALLIDAS · 1 NO APLICABLE
>
> PRESIONES VIGENTES   **el total NO se escribe aquí. Se REMITE**, y la sede es §16 del
>                      documento 11 — cabeceras `## \`PN-` menos las marcadas RETIRADA o
>                      FUSIONADA. Este campo publicó a mano ONCE, luego TRECE, y las dos
>                      caducaron; que caducara bajo el rótulo «CIFRAS VIGENTES, DERIVADAS»
>                      es lo que `Q-12` del documento 22 reprocha. Se deriva con
>                        grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
>                          | grep -vc 'RETIRADA\|FUSIONADA'
>                      `PN-17` y `PN-18` son las que añade esta tanda, por `P-07` y `P-08`
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
  **[HISTÓRICO · lo que aquella tanda validó, con sus cifras de entonces]**
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

PRESIONES           **[HISTÓRICO · el censo del momento de esa tanda]** DOCE vigentes:
                    `PN-1`, `PN-2`, `PN-3`, `PN-6` a `PN-14`. `PN-4` retirada, `PN-5`
                    fusionada en `PN-3`. Sin renumerar. El total se DERIVA
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

VALIDACIÓN
CANÓNICA           **[HISTÓRICO · el resultado de AQUELLA tanda, con Python 3.11.16, y
                   repetido entonces de forma independiente. `T161` cuenta ficheros del
                   corpus y SE MUEVE cada vez que se publica un documento, luego esta cifra
                   caduca sola. El estado de HOY no se copia: se obtiene ejecutando
                   `python3 kernel/operativo/validadores/registrar_evidencia.py`, que es su
                   única sede. Corregido por la causa que `Q-14` y `Q-16` del documento 22
                   levantaron: un bloque histórico presentado como vigente.]**
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
DEL KERNEL         un conjunto NOMBRADO y COMPLETO. **Derivado de Git, no escrito:**
                   `git diff --name-only 05f71b7..HEAD -- kernel/` devuelve **SEIS ficheros**,
                   y se clasifican así:

                     TRES FICHEROS DIRECTOS, no derivados:
                       kernel/operativo/validadores/comprobar_negativos.py   codigo, en 1b588ac
                       kernel/operativo/entrada/02-CIRCUITO.md               enlace colgante de
                                                                            K-09, en d868bcb
                       kernel/.upstream-hash                                 huella reanclada

                     TRES FICHEROS DE EVIDENCIA DERIVADA, que publica el runner:
                       kernel/operativo/pruebas/evidencia/fuentes-salida.txt
                       kernel/operativo/pruebas/evidencia/negativos-salida.txt
                       kernel/operativo/pruebas/evidencia/referencias-salida.txt

                     TOTAL 6 = 3 directos + 3 de evidencia derivada

                   **CORREGIDO OTRA VEZ, por la verificación previa a publicación.** La
                   formulación anterior decía «**CUATRO rutas más la evidencia derivada**» y
                   enumeraba cuatro entradas **de las cuales la cuarta ERA la evidencia**
                   (`pruebas/evidencia/*`): contaba lo derivado dentro de las cuatro **y otra
                   vez fuera**, y llamaba «ruta» a una categoría junto a tres ficheros. Antes
                   de eso decía «y sólo ésta» sobre una lista de TRES que omitía
                   `entrada/02-CIRCUITO.md`. **Ahora no hay categorías en el recuento: hay
                   seis ficheros, enumerados uno a uno, y la cifra la deriva `G-23`.**

                   Lo normativo —(a), (b), `E1`, `E2`, `C4`, `C7`— sigue intacto, y del kernel
                   operativo lo único SUSTANTIVO tocado es el enlace de
                   `entrada/02-CIRCUITO.md`. `G-23` autoriza los tres directos fichero a
                   fichero —`COD_AUTORIZADO`, `DOC_AUTORIZADO` y `HUELLA`— y **contrasta esta
                   lista contra lo que Git deriva**, para que no vuelva a envejecer.

BATERÍA PROPIA     tenía dos defectos que ESTA tanda cierra: calculaba mal la raíz y caía a
                   una ruta codificada de una máquina —luego en cualquier otro clon o
                   worktree comprobaba el repositorio del autor, no el que tenía delante—, y
                   `G-23` afirmaba «kernel intacto», que dejó de ser cierto en `1b588ac`.
                   Corregidos: raíz derivada de `__file__`, `G-23` con la excepción exacta y
                   `G-24` leyendo de verdad las catorce fuentes y las quince fichas por
                   nombre. **En verde desde la raíz, desde otro cwd y desde un worktree
                   arbitrario.**
                   CUÁNTAS COMPROBACIONES SON **NO SE ESCRIBE AQUÍ**, por la misma razón por
                   la que no se escriben los SHA ni la excepción del kernel: se DERIVA, y su
                   única sede es la batería misma, que lo imprime en su última línea —
                     python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py \
                       | tail -1
                   —, y su censo de identificadores se deriva de su README con
                     grep -o 'G-[0-9]\+[a-z]*' docs/evolucion/verificacion/README.md \
                       | sort -u | wc -l
                   [ESTADO ANTERIOR · esta línea decía **30/30**. Era cierta cuando se
                    escribió; las QUINCE protecciones sistémicas de la tanda de `O17`
                    llevaron la batería a 37 comprobaciones y nadie reancló la cifra, que se
                    quedó **bajo el rótulo ESTADO VIGENTE afirmando en presente algo falso**.
                    Es `S-16`≡`S3-06` del documento 23. No se sustituye 30 por 37: se retira
                    el número y se remite al comando, que es lo que este bloque ya hace con
                    el árbol vigente y con la excepción del kernel.]

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
[`verificacion/README.md`](verificacion/README.md), con el detalle de sus comprobaciones
—**cuántas son no se copia aquí**: las deriva el propio README con
``grep -o 'G-[0-9]\+[a-z]*' docs/evolucion/verificacion/README.md | sort -u | wc -l`` y la
batería las publica al ejecutarse; decía «treinta» cuando ya eran más, y es `S-16` del
documento 23— y de sus tres límites declarados: **no ejecuta nada del protocolo** —no hay
runtime, ni esquema de `evento`, ni un fichero bajo `estado/`—, **no sustituye al gate** —no
juzga suficiencia para F5— y **no cubre el corpus por lectura**: comprueba que las catorce
fuentes y las quince fichas existen, no que alguien las haya leído. Que un gate posterior las
LEA sigue siendo su condición mínima, y ninguna comprobación mecánica la sustituye.


## Matriz de trazabilidad · los 24 hallazgos del documento 21

> **Una fila por hallazgo DISTINTO, sin duplicar los tres solapes** —`P-01`≡`Q-13`,
> `P-02`≡`Q-06`, `P-05`≡`Q-08`—. La severidad es la **ADJUDICADA por `R`**, no la que
> propuso el revisor: `R` regraduó cuatro. **Ninguno se declara SUPERADO**: corregido por
> quien lo recibió no es superado por revisión independiente, y sólo un gate posterior con
> revisores que no hayan aplicado esta tanda puede decirlo.

| # | hallazgo | severidad adjudicada | reproducción | causa | fichero y sede corregidos | comprobación que impide la regresión | estado |
|---|---|---|---|---|---|---|---|
| 1 | `P-01≡Q-13` | **MEDIO** | sí · `X54` decía «las diecisiete ventanas» y la tabla de §2.6.5 deriva DIECIOCHO filas; `grep` sobre las 46 filas `X` devuelve CERO menciones de `W17` | un censo escrito a mano dentro de la única fila que dice barrerlas todas | `11-ARQ` §2.6.7, fila `X54` | `G-26.e` deriva las filas `W` y exige que la fila que las barre las cubra Y nombre la última. Las dos ramas disparan sobre su mutación | **APLICADA, NO CERTIFICADA** |
| 2 | `P-02≡Q-06` | **MEDIO** | sí · `11-ARQ:4360` decía «TODO `abandonada` DECLARA SU `deriva`» | el verbo anterior a `D105` no se propagó a la lista de la capa B, mientras §3.6 y la tabla de las cuatro reglas ya decían lo contrario | `11-ARQ` capa B, regla de correspondencia | la regla escribe hoy la referencia UNILATERAL por `abandonada_id` y remite a §3.6 como sede de la forma; `G-05` y `G-06` siguen cubriendo la capa | **APLICADA, NO CERTIFICADA** |
| 3 | `P-03` | **MENOR** | sí · abrí las cinco sedes que `P` cita | **TESIS RECHAZADA por el adjudicador `R`**: cuatro de sus cinco afirmaciones son falsas. No hay circularidad que corregir y `D105` no se altera | ninguna — se registra el rechazo | el residuo real que sobrevive se cierra en `R-01`, y su fila lo dice | **APLICADA, NO CERTIFICADA** |
| 4 | `P-04` | **MEDIO** | sí · el inventario contaba «las 9 ventanas `RC-1`–`RC-9`» que `D64` retiró y `D83` renombró para sacarlas | censo a mano, contradicho por la sede que declara la retirada quinientas líneas más abajo en este mismo fichero | `CHECKPOINT`, inventario NADA PROBADO | las cifras se derivan de las filas `W` y de las ocho `X-A`–`X-H` que el documento 11 sí cuenta | **APLICADA, NO CERTIFICADA** |
| 5 | `P-05≡Q-08` | **GRAVE** | sí · CINCO afirmaciones falsas a la vez, sin marca de histórica, en la sede que la cabecera designa como punto de entrada | la sección no se reancló en dos tandas, y su cifra de presiones iba al Owner | `CHECKPOINT`, «Siguiente acción exacta» **reescrita entera** | `G-26.c1` barre ahora también el checkpoint —la sede que va al Owner— y `G-23` exige que el punto de entrada REMITA en vez de copiar | **APLICADA, NO CERTIFICADA** |
| 6 | `P-06` | **MEDIO** | sí · el bloque declaraba «cero apariciones» de `G20`/`G21`/`G23` en el documento 11, donde hay 13 · 11 · 14 | la evidencia se destruía al registrarla: la mayoría de esas apariciones las introdujo el propio bloque | `11-ARQ` §16, bloque de evidencia de `PN-15` | `G-13` deriva el barrido sobre (a), (b) y `E2` —el material que puede DEROGAR— y lo contrasta contra las tres cifras publicadas | **APLICADA, NO CERTIFICADA** |
| 7 | `P-07` | **MENOR** | sí · el bloque `E5` cubría `E5-3` con «aquí no hay norma presionada» | `E5-3` puede exigir que **F5 enmiende (b)**, luego tiene norma presionada por definición | `11-ARQ` §19 bloque `E5`, y **`PN-16` NUEVA** en §16 | `G-13` deriva el censo —CATORCE— y `G-26.f` exige que todo rango vivo termine en la última vigente | **APLICADA, NO CERTIFICADA** |
| 8 | `P-08` | **MENOR** | sí · el manifiesto declaraba «FUENTES SIN ASIGNAR 0» sobre un universo ELEGIDO | `D106` pedía «el total, derivado» sin fijar **de qué sede** sale «obligatoria» | `11-ARQ` `C-L.5`, apartado `1bis` | la regla vigente exige publicar el universo, su REGLA y el COMANDO auditable, y separa `obligatorio − asignado` de `asignado − leído`. Lo comprueba el gate siguiente | **APLICADA, NO CERTIFICADA** |
| 9 | `Q-01` | **MEDIO** | sí · sin `.git` y con `D12`, `D40` y `D80` reescritas, `G-11b` decía «ninguna difiere» | la única comprobación dependiente de Git que no fallaba cerrado | batería, `G-11b` | la propia `G-11b`, que hoy falla con «GIT NO RESPONDE». Refutación reejecutada: falla | **APLICADA, NO CERTIFICADA** |
| 10 | `Q-02` | **MEDIO** | sí · `capacidad_productora: "VER:dosier"` en `INC` movía el ancla y `G-15` seguía verde | el ancla se comparaba en CRUDO mientras el resto del algoritmo normaliza a la capacidad base | batería, `_analizar` | fixture «ancla ante `VER:dosier`», que dispara si se deshace la normalización | **APLICADA, NO CERTIFICADA** |
| 11 | `Q-03` | **MENOR** | sí · mover `DOM`/`SEG` de `FEA` de la vía 4 a la vía 3 dejaba el total en nueve y `G-15` en verde | sólo se contrastaba el TOTAL, y un total admite repartos que significan cosas distintas | batería `_derivar` y `11-ARQ` §19 `SALIDA ESPERADA` | el REPARTO POR VÍA se publica y `G-15` lo contrasta vía a vía | **APLICADA, NO CERTIFICADA** |
| 12 | `Q-04` | **MEDIO** | sí · con `01-PROCESOS-BIS.md` y `C8-SEGUNDA-SEDE.md` bajo `kernel/`, la batería daba **30/30 EN VERDE** | `git diff --name-only` no ve ficheros nuevos sin rastrear | batería, `G-23` | el CONJUNTO de ficheros del kernel se compara contra la revisión base, y el catálogo de procesos debe ocupar UNA sede bajo `kernel/`. La refutación falla hoy nombrando las dos causas | **APLICADA, NO CERTIFICADA** |
| 13 | `Q-05` | **MEDIO** | sí · `capacidad_productora` inyectada en la prosa de un `criterio_de_satisfaccion` daba `FEA part = [('DOM',2),('DOM',4),('SEG',4)]` | el troceado era un `re.findall` sobre un segmento de texto, no un parseo | batería, `_campos` y `_analizar` | lector por INDENTACIÓN y ESCALARES: la prosa no participa, y el fallo NOMBRA el campo que la contiene. Fixture propio | **APLICADA, NO CERTIFICADA** |
| 14 | `Q-07` | **MEDIO** | sí · §16 L7887 cerraba su rango en `PN-14` con `PN-15` ya viva. TERCERA recurrencia de la misma frase | un RANGO no es un numeral, y las dos correcciones anteriores corrigieron el numeral | `11-ARQ` §16 y las sedes vivas del censo | `G-26.f` deriva la última vigente y exige que todo rango VIVO termine en ella | **APLICADA, NO CERTIFICADA** |
| 15 | `Q-09` | **MENOR** | sí · `_VIGILADAS = ("DOM", "SEG")` era un literal | censo escrito a mano dentro de la comprobación cuyo objeto es esa disciplina | batería, `_derivar_vigiladas` | el conjunto se deriva de las fichas de capacidad; retirar la declaración de una ficha hace fallar `G-15` | **APLICADA, NO CERTIFICADA** |
| 16 | `Q-10` | **MENOR** | sí · `_exige_item` usaba `via in (3, 4)` sin conservar la sección de origen | la vía por sí sola no dice si una participación es obligatoria o condicional desde que la vía 4 puede venir de las dos secciones | batería, `_analizar` y `_exige_item` | la PROCEDENCIA se conserva, y un fixture exige que una obligatoria tipada se exija SIEMPRE | **APLICADA, NO CERTIFICADA** |
| 17 | `Q-11` | **MENOR** | sí · la sede atribuía `conclusion-fundada` a `proceso:INV`, cuya única obligatoria es `evidencia-producida` | una sola frase daba el mismo item a dos procesos | `11-ARQ` §19, `EL ANCLA DE POSICIÓN` | las anclas se publican proceso a proceso y `G-15` las contrasta contra el catálogo derivado | **APLICADA, NO CERTIFICADA** |
| 18 | `Q-12` | **MENOR** | sí · «cinco fixtures» junto a una enumeración de SEIS grupos, con TRES procesos dinámicos | cifra manual que no describía lo que la batería ejecuta | `11-ARQ` §19, `QUÉ TIENE QUE DEMOSTRAR` | el censo se deriva de los fixtures ejecutados —17— y `G-15` falla si la sede publica otro | **APLICADA, NO CERTIFICADA** |
| 19 | `Q-14` | **MEDIO** | sí · `C-L.3` figuraba CERRADA por la regla de `D103` que `M-01` refutó **y** NO CERRADA, y `D104` no aparecía en ninguna de sus seis sedes | el contraste de detalle leía la PRIMERA fila `C-L.n` del fichero, que estaba en un bloque histórico | `CHECKPOINT`, **clasificación vigente** delimitada y con sus trece filas de detalle | `G-16` se acota al bloque vigente y exige que `C-L.3` nombre `D104` y no conserve «cero o un par, nunca dos» | **APLICADA, NO CERTIFICADA** |
| 20 | `Q-15` | **MENOR** | sí · `ancho` se calculaba en cada corrida y no la leía nadie; y la capa B decía «toda todo `abandonada`» | código muerto y una errata de concordancia | batería, informe · `11-ARQ` capa B | `ast` sobre el fichero: cero variables asignadas y nunca leídas | **APLICADA, NO CERTIFICADA** |
| 21 | `R-01` | **MENOR** | sí · TRES sedes justificaban la idempotencia de `W17` «por contenido» | se apoyaban en el razonamiento que §2.8 RETIRÓ expresamente —`predecesor` entra en el `id`— | `11-ARQ` §2.6.4 paso 0, fila `W17` y §2.6.9 punto 8 | las tres dicen hoy dónde vive la idempotencia: la guarda de existencia por `abandonada_id` y la regla de unicidad de la capa B | **APLICADA, NO CERTIFICADA** |
| 22 | `R-02` | **MEDIO** | sí · la sección de entrada enumeraba TRES ficheros del kernel donde la sede derivada enumera SEIS | `M-06` reproducido en la misma tanda que lo declaraba corregido: una lista copiada en vez de una remisión | `CHECKPOINT`, «Siguiente acción exacta» | `G-23` prohíbe que esa sección copie rutas del kernel y exige que remita a `EXCEPCIÓN EXACTA DEL KERNEL` | **APLICADA, NO CERTIFICADA** |
| 23 | `R-03` | **MEDIO** | sí · §2.6.9 invocaba «la capa B» por su nombre para una regla que su lista no escribía | la regla vivía en la tabla de las cuatro, 46 líneas más abajo, y la lista decía lo contrario | `11-ARQ` §2.6.9, `EL VALIDADOR Y LAS VENTANAS` | queda escrito quién FIJA la forma (§3.6), quién la VALIDA (capa B), quién describe la caída (§2.6.5) y quién la completa (paso 0) | **APLICADA, NO CERTIFICADA** |
| 24 | `R-04` | **MENOR** | sí · `W17` se atribuía «—o entre el `deriva` y su marcador—», tramo que su propia condición de detección excluye | el reparto estaba bien en el punto 7 de §2.6.9 y mal en la fila | `11-ARQ` §2.6.5, fila `W17` | la fila remite hoy a `W8`, §2.9 y `X60` para ese tramo, y `G-26.e` mantiene el censo alineado | **APLICADA, NO CERTIFICADA** |

```text
RECUENTO DERIVADO DE LAS FILAS DE ARRIBA, no copiado
  BLOQUEANTE   0
  GRAVE        1   P-05≡Q-08
  MEDIO       12   P-01≡Q-13 · P-02≡Q-06 · P-04 · P-06 · Q-01 · Q-02 · Q-04 · Q-05 ·
                   Q-07 · Q-14 · R-02 · R-03
  MENOR       11   P-03 · P-07 · P-08 · Q-03 · Q-09 · Q-10 · Q-11 · Q-12 · Q-15 ·
                   R-01 · R-04
              ──
              24   los veinticuatro ids distintos, cada uno EXACTAMENTE UNA VEZ
```

**`M-04` no es una de las veinticuatro, y se describe aparte porque su estado es preciso.**
Sus CUATRO refutaciones nombradas estaban cerradas —`R` las reprodujo una a una: `R1` 28/30,
`R2` 29/30, `R3` 29/30, `R4` 26/30—, pero `M-04` es la **proposición** «se puede construir un
árbol defectuoso que pase 30/30 en verde», y esa proposición **seguía siendo verdadera**:
`Q-04` la demostró. Esta tanda **añade protección contra `Q-04`** —el conjunto de ficheros
del kernel y la unicidad del catálogo, derivados del árbol— y contra `Q-01` y `Q-05`.
**Eso no la declara superada.** La proposición es universal y una tanda sólo puede cerrar los
contraejemplos que conoce: **sólo un gate posterior, con revisores que no hayan aplicado esto,
puede decir si sigue habiendo un árbol defectuoso en verde.** `M-04` queda FALLIDA.

## El criterio del gate siguiente · las TRES afirmaciones que hay que distinguir

> **Está escrito aquí, y no dentro del encargo de un gate concreto, porque es lo que decide
> si `F4c` puede cerrarse.** Tres gates consecutivos fallaron por la misma causa, y la causa
> era que una sola pregunta —«¿está intacto?»— mezclaba tres afirmaciones con evidencia
> distinta y con **FASE distinta**. `O18` las separa y le pone fase a cada una. **El mecanismo
> del sobre no se reproduce aquí**: sus campos, el deber del revisor y el del adjudicador son
> `D108` en §1 de
> [`DECISIONES-Y-CONTRADICCIONES.md`](../rediseno/DECISIONES-Y-CONTRADICCIONES.md), y la
> resolución que lo ordena es `O18`, en §2 de ese mismo fichero.

```text
A · COHERENCIA INTERNA          la batería comprueba el corpus contra sus contratos
                                DEMOSTRABLE HOY — es lo que la batería hace, y su censo de
                                comprobaciones no se copia aquí: lo publica ella misma

B · IDENTIDAD DE LA CANDIDATA   el sobre demuestra que se analizó EXACTAMENTE el commit, el
                                árbol, el manifiesto y el universo ENCARGADOS
                                DEMOSTRABLE HOY por la alternativa (b) de `O18`, y sólo si
                                el sobre se entregó por canal EXTERNO al repositorio ANTES
                                de que el revisor empezara a leer

C · RESISTENCIA A UN ACTOR      NO IMPLEMENTADA. Contrato OBLIGATORIO de `F6`, y CONDICIÓN
    PRIVILEGIADO                PREVIA a PesquerApp. Se declara como LÍMITE; no se presenta
                                como capacidad existente


`F4c` PUEDE CONSIDERARSE SUFICIENTE SI, Y SÓLO SI:

   A   está DEMOSTRADA
   B   está DEMOSTRADA
   C   está DECLARADA como límite · CONTRATADA COMPLETAMENTE · ASIGNADA a `F6` ·
       ESTABLECIDA como condición previa a PesquerApp · y NO presentada como capacidad
       existente

Suficiente NO es cerrada: quien cierra `F4c` es el veredicto explícito de ese gate, y
NINGÚN hallazgo se declara SUPERADO antes de que lo emita.


LAS DOS ADVERTENCIAS, Y SON DEL OWNER:

   1   el gate **NO puede volver a exigir `C` como implementación YA CONSTRUIDA dentro de
       `F4c`**. `O18` resuelve expresamente su FASE, y exigirla aquí reinstala el bloqueo
       circular que esa resolución existe para evitar: `F4c` bloquea `F5`, `F5` precede a
       `F6`, y `F6` es quien construye el verificador

   2   el gate **NO puede dar por satisfecha `B` sólo porque el repositorio AFIRME que el
       sobre existió**. Los revisores tienen que registrar lo RECIBIDO EXTERNAMENTE, y
       registrarlo ANTES de leer: un sobre reconstruido a posteriori desde el árbol vuelve
       a anclar la verificación en el árbol, que es exactamente lo que `O18` cierra
```

## Siguiente acción exacta

```text
0  DÓNDE ESTAMOS               el CUARTO GATE DE CERTIFICACIÓN ha devuelto **INSUFICIENTE
                               PARA F5** y su propio adjudicador lo ha declarado
                               **INVÁLIDO**. Su documento, su recuento y su clasificación
                               NO se copian aquí: el documento se deriva con
                               `ls docs/evolucion/[0-9][0-9]-*.md | sort | tail -1`, y el
                               recuento vive dentro de él. Los SHA vigentes, con
                               `git rev-parse HEAD` y `git ls-remote`.

1  POR QUÉ ES INVÁLIDO,        porque **el COORDINADOR transcribió el SOBRE DE ANCLA a mano**
   EN UNA LÍNEA                en el encargo de cada relevo y las transcripciones NO fueron
                               idénticas. El emisor emitió bien y el objeto no está en duda:
                               **lo que falló fue la ENTREGA**, que ocurre FUERA del árbol y
                               no tiene defensa mecánica posible. Es la primera vez que este
                               expediente produce un gate inválido.

2  LO QUE ESTA TANDA HA HECHO  aplicar los hallazgos DOCUMENTALES, y nada más: la entrada de
                               `O18` recibe la NOTA DE ALCANCE que `O19` decía haber anotado
                               y no anotó —sin editar su texto resolutivo—; `D105` queda
                               propagado a las sedes vivas que aún decían que `abandonada`
                               RETIRA el marcador, **incluidas las dos filas adversariales
                               que son CONTRATO DE PRUEBA de `F6` y que una implementación
                               con el defecto `M-03` PASABA**; los titulares numéricos que su
                               propia enumeración desmentía pasan a REMITIR o a DERIVARSE, y
                               la regla de titulares de §0 **declara que no tiene guardián**;
                               las afirmaciones sobre el propio árbol que el gate falsó se
                               corrigen o se marcan como históricas; y **tres citas
                               entrecomilladas atribuidas al Owner** vuelven a su sede real
                               —la PREGUNTA del coordinador—, con una de ellas retirada.

3  LO QUE NO SE HA HECHO,      **no se ha escrito ni una protección interna nueva**: el
   Y ES DELIBERADO             adjudicador `AA` lo ordenó expresamente —«lo que falta es de
                               resta y de disciplina»—, y el censo de comprobaciones no se
                               mueve. No se declara SUPERADO ningún hallazgo, no se cierra
                               `M-04`, no se edita la SEDE CANÓNICA —es append-only— ni el
                               texto resolutivo de ninguna `O` ni de ninguna `D`, y no se
                               sustituye un número por otro donde se podía remitir.

4  QUÉ VUELVE AL OWNER         **NADA.** `AA` declara expresamente que NO hay ninguna
                               decisión del Owner pendiente: los treinta y seis hallazgos
                               tienen remedio determinado dentro de `F4c`.

5  QUÉ VIENE AHORA             publicar candidata y encargar otro gate independiente con
                               revisores de contexto limpio que NO sean quien aplicó esta
                               tanda. Y esta vez **el sobre se entrega ÍNTEGRO Y CAMPO A
                               CAMPO IDÉNTICO a los cinco relevos** —el SHA-256 del derivador
                               incluido, que lo ordena la SEDE CANÓNICA y no sólo §11.6—,
                               con los DOS manifiestos que `D106` exige ENLAZADOS desde
                               `00-INDICE.md` en el mismo commit que los crea.

6  LO QUE SIGUE ABIERTO        `M-04` **NO se declara superada**. `C-L.7` sigue **NO
                               CERRADA**. **`C-L.5` pasa de CERTIFICADA a ABIERTA**, por
                               `ASIGNADO − LEÍDO = 1`, y por sí sola excluye la suficiencia.
                               Y la limitación que `O18` declara de sí misma sigue VIGENTE:
                               la sede canónica traslada la AUTORIDAD y **no la hace
                               mecánicamente verificable contra una fuente externa al
                               sistema**. Eso es el verificador externo de `F6`.

7  ESTADO, SIN ADORNO          `F4c` sigue **ABIERTA**. `F5` sigue **NO AUTORIZADA**. No se
                               ha iniciado F5, ni F6, ni PesquerApp. No se ha hecho merge en
                               `redesign/kernel-2.0`. **APLICAR NO ES CERTIFICAR**, y un
                               gate INVÁLIDO no certifica nada en ninguna dirección.

8  DÓNDE PARAR                 antes de dar por cerrado lo que sólo un gate independiente
                               puede cerrar. Y sigue vigente parar antes de redactar `(g)`,
                               antes de crear `C8`, antes de tocar `C7` o el kernel
                               operativo SUSTANTIVO, y antes de iniciar PesquerApp.

9  QUÉ DEL KERNEL ESTÁ         **NO SE ENUMERA AQUÍ, Y ES LA REGLA.** La lista exacta de lo
   TOCADO, Y DÓNDE MIRARLO     que el kernel tiene tocado —y sólo eso— vive en el campo
                               **EXCEPCIÓN EXACTA DEL KERNEL** de este mismo fichero, que es
                               su sede derivada, y `G-23` la contrasta contra el árbol.
                               Esta sección **REMITE y no copia ninguna ruta**: copiarlas es
                               `M-06`, y su reincidencia es `R-02`.
                               **Recuperado por `Y3-09`**: esta remisión estaba en las
                               CUATRO versiones históricas de más abajo, se perdió al
                               reescribir la sección entera para `O19`, y nadie lo vio
                               porque `G-23` barre desde el PRIMER rótulo «Siguiente acción
                               exacta» **hasta el final del fichero**: las versiones
                               históricas la satisfacían en lugar de la vigente.
```

> **La regla de redacción de esta sección, que NO es histórica y se conserva:** nada que otra
> sede pueda derivar se copia aquí. Los SHA, los censos, el recuento de la batería y el
> ordinal de la tanda se derivan con su comando. **Cuántas veces ha caducado esta sección no
> se escribe: se DERIVA**, y es una por cada versión rotulada HISTÓRICA de más abajo —
> `grep -c '^## Siguiente acci[óo]n exacta — HISTÓRICA' docs/evolucion/CHECKPOINT-ADS-NEXT.md`—.
> Escribir el cardinal aquí sería el defecto que la regla de titulares de §0 del documento 11
> persigue, en la misma sección que existe para no volver a copiar nada.

> **[HISTÓRICA · «Siguiente acción exacta» anterior al CUARTO GATE DE CERTIFICACIÓN. Se
> conserva para trazabilidad y NO describe el estado vigente.]**

## Siguiente acción exacta — HISTÓRICA, anterior al documento 25

```text
0  DÓNDE ESTAMOS               el Owner ha resuelto la RATIFICACIÓN que el TERCER GATE DE
                               CERTIFICACIÓN le elevó como su única decisión suya. Es
                               `O19`, y su texto íntegro está en la SEDE CANÓNICA
                               `docs/owner/ADS-OWNER-RESOLUCIONES.md`. El último documento
                               numerado y los SHA vigentes NO se copian aquí: se derivan
                               con `ls docs/evolucion/[0-9][0-9]-*.md | sort | tail -1`,
                               `git rev-parse HEAD` y `git ls-remote`.

1  QUÉ RESOLVIÓ, EN UNA LÍNEA  RATIFICA el texto amplio de `O18` y le da SEDE CANÓNICA en
                               `docs/owner/`. Revisa la PROYECCIÓN incompleta, **no el
                               contenido ni el diseño**, y la autoridad deja de ser la
                               paráfrasis del coordinador. La sede es su única sede.

2  LO QUE ESTA TANDA HA HECHO  el sobre de ancla ancla la sede: ruta, SHA-256 del COMMIT
                               AUDITADO, identificadores DERIVADOS de ella, digest del texto
                               canónico de cada resolución con su receta, la relación entre
                               `O18` y `O19`, y la declaración externa de ratificación.
                               **Sin la sede no hay sobre.** Y el inventario de inmutables
                               que ya existía alcanza ahora `docs/owner/`, con la misma
                               comprobación y el mismo perímetro derivado del árbol.

3  LO QUE NO SE HA HECHO,      no se declara SUPERADO ningún hallazgo, no se cierra `M-04`,
   Y ES DELIBERADO             no se edita la entrada corta de `O18` —es el registro
                               histórico de la transcripción incompleta y borrarla sería
                               reescribir la historia— y **no se escribe ni una protección
                               interna nueva**: el remedio del Owner es una sede EXTERNA a
                               la paráfrasis, no una comprobación más dentro del árbol.

4  QUÉ VUELVE AL OWNER         NADA. La ratificación queda CERRADA por él mismo: versión
                               amplia, condiciones obligatorias y reparto, y `O18` no vuelve
                               a someterse a elección.

5  QUÉ VIENE AHORA             publicar candidata y encargar otro gate independiente con
                               revisores de contexto limpio que NO sean quien aplicó esta
                               tanda. Cada uno recibe FUERA del árbol el SHA de la sede del
                               Owner junto al resto del sobre, y **comprueba la receta sin
                               ejecutar el emisor**. Y los DOS manifiestos que `D106` exige,
                               ENLAZADOS desde `00-INDICE.md` en el mismo commit que los
                               crea, que es la regla que dos gates han castigado incumplir.

6  LO QUE SIGUE ABIERTO        `M-04` **NO se declara superada**. `C-L.7` sigue **NO
                               CERRADA**. Y la limitación que `O18` declara de sí misma
                               sigue VIGENTE: la sede canónica traslada la AUTORIDAD y **no
                               la hace mecánicamente verificable contra una fuente externa
                               al sistema**. Eso es el verificador externo de `F6`.

7  ESTADO, SIN ADORNO          `F4c` sigue **ABIERTA**. `F5` sigue **NO AUTORIZADA**, y
                               `O19` lo dice con todas las letras. No se ha iniciado F5, ni
                               F6, ni PesquerApp. No se ha hecho merge en
                               `redesign/kernel-2.0`. **RATIFICAR no es CERTIFICAR.**

8  DÓNDE PARAR                 antes de dar por cerrado lo que sólo un gate independiente
                               puede cerrar. Y sigue vigente parar antes de redactar `(g)`,
                               antes de crear `C8`, antes de tocar `C7` o el kernel
                               operativo SUSTANTIVO, y antes de iniciar PesquerApp.
```

> **La regla de redacción de esta sección, que NO es histórica y se conserva:** nada que otra
> sede pueda derivar se copia aquí. Los SHA, los censos, el recuento de la batería y el
> ordinal de la tanda se derivan con su comando. Esta sección ha caducado cuatro veces por
> copiar lo que otra sede ya decía.

> **[HISTÓRICA · «Siguiente acción exacta» anterior a la resolución `O19` del Owner. Se
> conserva para trazabilidad y NO describe el estado vigente.]**

## Siguiente acción exacta — HISTÓRICA, anterior a `O19`

```text
0  DÓNDE ESTAMOS               el TERCER GATE DE CERTIFICACIÓN devolvió `INSUFICIENTE PARA
                               F5` sobre la candidata `21f1ccb`, y **el gate es VÁLIDO**.
                               Su documento es el **24** y está publicado. Los SHA vigentes
                               se derivan con `git rev-parse HEAD` y `git ls-remote`: no se
                               copian aquí, y ésa es la regla de esta sección.

1  QUÉ DIJO, EN UNA LÍNEA      falla por `A` —coherencia interna— y por `B` —identidad de la
                               candidata—, y **expresamente NO por `C`**. `C-L.5` queda
                               CERTIFICADA por cuarta vez consecutiva: **no falla por
                               cobertura**, y el adjudicador lo dice con todas las letras.

2  LO QUE ESTA TANDA HA HECHO  reparar el mecanismo que el gate rompió, sin añadir ninguna
                               comprobación nueva —el censo sigue en el número que la sede
                               declara y `G-34` lo contrasta—. El emisor del sobre lee del
                               COMMIT y no del árbol de trabajo, **se niega a emitir con el
                               árbol sucio**, publica LOS DOS ÁRBOLES con las rutas en que
                               difieren, y su receta reproduce los digest byte a byte. El
                               emisor y el derivador entran en el inventario de integridad.
                               `O18` recibe su **declaración de INVERIFICABILIDAD**, que es
                               lo único de la disputa que `F4` sí puede hacer.

3  LO QUE NO SE HA HECHO,      **la disputa sobre el texto de `O18` NO se ha resuelto**, y
   Y ES DELIBERADO             es deliberado: ni se recortó la propagación ni se completó la
                               resolución. Está REGISTRADA dentro de `O18` con sus cuatro
                               hechos, y **la ratificación es del Owner**. `G21` de
                               `KERNEL.md` L690: un sistema no puede definir sin conflicto
                               de interés los criterios que aprueban su propia existencia.

4  LO ÚNICO QUE VUELVE         una **RATIFICACIÓN**, no una elección. `O18` registra UNA
   AL OWNER                    condición previa para el verificador externo y seis sedes
                               escriben TRES. La pregunta, con sus tres alternativas y el
                               coste de cada una, está redactada palabra por palabra en
                               **§13 de la adjudicación de `X`**, dentro del documento 24.

5  QUÉ VIENE DESPUÉS DE        publicar candidata y encargar otro gate independiente con
   LA RESPUESTA                revisores nuevos, que reciban el sobre —ya reparado— antes de
                               leer. Y **NO escribir una protección interna más**: el
                               adjudicador lo ordena, y su razón es que el gate siguiente
                               encontraría la puerta que venga detrás y tendría razón.

6  LO QUE SIGUE ABIERTO        `M-04` **NO se declara superada**: sólo un gate independiente
                               puede hacerlo, y lleva cuatro sin poder. `C-L.7` pasa a **NO
                               CERRADA** por el hallazgo `X-04`. Los hallazgos de clase `C`
                               siguen vivos, declarados y contratados para `F6`.

7  ESTADO, SIN ADORNO          `F4c` sigue **ABIERTA**. `F5` sigue **NO AUTORIZADA**. No se
                               ha iniciado F5, ni F6, ni PesquerApp. No se ha hecho merge en
                               `redesign/kernel-2.0`. **Aplicar no es certificar.**

8  DÓNDE PARAR                 antes de elegir por el Owner en el punto 4. Y sigue vigente
                               parar antes de redactar `(g)`, antes de crear `C8`, antes de
                               tocar `C7` o el kernel operativo SUSTANTIVO, y antes de
                               iniciar PesquerApp.
```

> **[HISTÓRICA · «Siguiente acción exacta» anterior al documento 24. Se conserva para
> trazabilidad y NO describe el estado vigente.]**

## Siguiente acción exacta — HISTÓRICA, anterior al documento 24

> **POR QUÉ ESTA SECCIÓN ESTÁ ESCRITA ASÍ, y es una garantía HEREDADA, no un adorno.** Ha
> caducado **tres veces consecutivas** —`K-01`/`J-10`/`L-01` en el gate del documento 19;
> `P-05`≡`Q-08`, el único GRAVE de aquel gate, y `R-02` en el del documento 21; y
> `S-17`≡`S3-05` en el del documento 23—, siempre por la misma causa: **copiaba lo que otra
> sede deriva**. La regla que la tanda anterior le escribió **sigue vigente y se respeta**:
> **nada que otra sede pueda derivar se copia dentro de ella.** Remiten, y no se escriben:
> los SHA (a `git rev-parse` y `git ls-remote`) · el recuento de comprobaciones de la batería
> (a la batería) · el censo de presiones vigentes (a §16 del documento 11, con su comando) ·
> la excepción del kernel (al campo **EXCEPCIÓN EXACTA DEL KERNEL** de este mismo fichero) ·
> el ordinal de la tanda (a las cabeceras `###` de §15.8 del documento 11) · el reparto por
> severidad de los hallazgos (a §12 y §13 de la adjudicación de `U`, dentro del documento 23)
> · el texto de `O18` y los campos del sobre (a §2 y §1 de
> [`DECISIONES-Y-CONTRADICCIONES.md`](../rediseno/DECISIONES-Y-CONTRADICCIONES.md)) · lo que
> el sobre NO protege (a la cabecera de este mismo fichero, y a `O18`) · el criterio `A`/`B`/`C`
> del gate siguiente (a «El criterio del gate siguiente», justo encima) · y la lista de
> manifiestos publicados (a la tabla de `00-INDICE.md`). Lo que quede escrito aquí es lo que
> **no tiene otra sede**: qué pasó, qué se está haciendo y dónde hay que parar.

```text
0  DÓNDE ESTAMOS, EXACTO         **el Owner ya respondió.** La única clase `B` del SEGUNDO
                                 GATE INDEPENDIENTE DE CERTIFICACIÓN —documento 23— no era
                                 un hallazgo: era LA RAÍZ. Su respuesta es **`O18`**, del
                                 2026-08-30, y está **REGISTRADA** en §2 de
                                 `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`; su
                                 propagación es **`D108`**, en §1 del mismo fichero,
                                 declarada DERIVADA. **La clase `B` queda RESUELTA y YA NO
                                 BLOQUEA.**
                                 **Los SHA no se copian aquí**: se derivan con
                                   git rev-parse HEAD
                                   git ls-remote origin
                                 [ESTADO ANTERIOR · la versión de esta sección que ahora va
                                  rotulada HISTÓRICA mandaba PARAR y esperar respuesta del
                                  Owner, y no encargar ningún gate hasta tenerla. **La
                                  respuesta llegó**: ese paso está cumplido y esa condición
                                  de parada queda levantada.]

1  QUÉ RESOLVIÓ `O18`            una **RESOLUCIÓN ESCALONADA**, y sus tres partes son
                                 inseparables: **(a) RECHAZADA EXPRESAMENTE** —no se retira
                                 la garantía ni se acepta que una alteración deliberada sea
                                 indetectable—; **(b) ADOPTADA PARA CERRAR `F4c`**, el
                                 SOBRE DE ANCLA, transitoria y explícitamente limitada;
                                 **(c) OBLIGATORIA EN `F6`**, el verificador externo real.
                                 El motivo del orden es el **bloqueo circular** que el Owner
                                 no acepta. **El texto no se copia aquí**: es `O18`.

2  QUÉ ES REQUISITO DESDE HOY    **el SOBRE DE ANCLA es requisito de TODO gate de `F4c`**, y
                                 no de uno solo. El coordinador lo emite y lo entrega dentro
                                 del encargo de cada revisor, **por un canal externo al
                                 repositorio y ANTES de que lea**; el revisor lo transcribe,
                                 lo comprueba contra el remoto y **falla CERRADO ante
                                 cualquier diferencia**; el adjudicador contrasta los sobres
                                 y **declara INVÁLIDO el gate** si difieren, sin aceptar uno
                                 reconstruido a posteriori ni cambiado después de crear
                                 revisores. **Los campos del sobre y los tres deberes no se
                                 copian aquí**: son `D108`, apartados (i), (ii) y (iii).
                                 **El sobre NO sustituye** el manifiesto previo, ni los
                                 manifiestos de lectura, ni las dos restas, ni la revisión
                                 independiente, ni la adjudicación contra las fuentes.

3  QUÉ QUEDA CONTRATADO PARA     el **VERIFICADOR EXTERNO DEL CONTROL REPO**, registrado
   `F6`, Y NO PARA HOY           COMPLETO y **SIN IMPLEMENTAR** en `D108`(v), con
                                 propietario, ejecutor, autoridad, fase, pruebas y condición
                                 de cierre. Es **CONDICIÓN PREVIA a PesquerApp**: su
                                 adopción permanente no puede iniciarse mientras esa
                                 sustitución no exista y esté probada.
                                 **`O18` lo contrata; NO autoriza construirlo hoy ni
                                 iniciar `F6`.**

4  QUÉ SE ESTÁ HACIENDO AHORA    propagar `O18` como `D108` por las sedes vigentes, y cerrar
                                 los hallazgos de clase `A` del documento 23, agrupados POR
                                 CAUSA y no por línea. **El reparto por severidad y por
                                 clase no se copia aquí**: §12 y §13 de la adjudicación de
                                 `U`. **Y expresamente NO se escribe una protección
                                 sistémica más**: el adjudicador midió las de la tanda
                                 anterior y sólo tres generalizan. `O18` no añade otra
                                 comprobación interna —eso movería la circularidad de
                                 sitio—: **cambia la raíz de confianza**, que es lo que
                                 §11.4 del documento 11 decía que hacía falta.

5  EL PASO SIGUIENTE, EXACTO     (i)   **publicar el árbol vigente como candidata nueva**;
                                 (ii)  **encargar OTRO GATE INDEPENDIENTE** sobre ella, con
                                       revisores de contexto limpio que no sean quien aplicó
                                       esta tanda **y que RECIBAN EL SOBRE DE ANCLA, por
                                       canal externo, ANTES de empezar a leer**;
                                 (iii) que ese gate juzgue con **las TRES afirmaciones `A`,
                                       `B` y `C`** — su sede es «El criterio del gate
                                       siguiente», la sección inmediatamente anterior a
                                       ésta, y **no se reproduce aquí**.
                                 El «parar y esperar al Owner» del paso anterior **está
                                 levantado**, porque la respuesta ya existe y está registrada.

6  QUÉ LLEVAR AL OWNER           las presiones normativas vigentes de §16 — **el total NO se
                                 copia aquí**: se deriva con
                                   grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
                                     | grep -vc 'RETIRADA\|FUSIONADA'
                                 Registrar es F4; elegir es F5. **Ninguna decisión nueva de
                                 clase `B` queda pendiente hoy**: la que había es `O18`, y
                                 está respondida.

7  EL KERNEL SUSTANTIVO          no se ha tocado, y la excepción **no se reproduce aquí**:
                                 vive en el campo `EXCEPCIÓN EXACTA DEL KERNEL` de este
                                 mismo fichero, derivada de Git y contrastada por `G-23`.
                                 **Se remite, no se copia**: una lista copiada envejece sola.

8  LO QUE EL PRÓXIMO GATE        dos cosas, y ninguna es opcional:
   TIENE QUE CUMPLIR SIN         (i)  **el sobre**, en los términos del paso 2 y de `D108`,
   EXCUSA                             con la advertencia 2 del criterio: `B` no se da por
                                      satisfecha porque el repositorio afirme que el sobre
                                      existió;
                                 (ii) **la regla de publicación**: todo documento que
                                      `C-L.5` obligue a publicar —manifiesto de asignación,
                                      manifiestos de lectura, addenda y corrigenda— **se
                                      enlaza desde la tabla de `00-INDICE.md` en el MISMO
                                      commit que lo crea**. No vale añadirlo a
                                      `exclusiones.yaml`: una exclusión APAGA `T147` en vez
                                      de cumplirlo. La regla, la tabla y el comando que
                                      deriva los huérfanos están en `00-INDICE.md`, bajo
                                      «Lo que cada gate tiene que publicar, y desde dónde se
                                      enlaza».

9  ESTADO, SIN ADORNO            **`F4c` sigue ABIERTA. `F5` sigue NO AUTORIZADA.** `O18`
                                 resuelve una decisión que sólo el Owner podía tomar; no
                                 cierra `F4c`, no autoriza `F5`, no autoriza `F6`, no
                                 autoriza PesquerApp, no levanta ninguna condición `C-L` y
                                 no deroga ninguna presión vigente. Ninguna enmienda
                                 normativa está redactada, `C8` no existe y `C7` no se ha
                                 tocado. **No se ha hecho merge en `redesign/kernel-2.0`.**
                                 **APLICAR NO ES CERTIFICAR**, y esta tanda la aplica quien
                                 la recibió: **NINGÚN hallazgo del documento 23 se declara
                                 SUPERADO**, **`M-04` NO se declara superada**, y sólo un
                                 gate independiente posterior podría declararlo.

10 LO QUE EL SOBRE NO PROTEGE    hay seis riesgos que la alternativa (b) **NO cubre**, y
                                 están enumerados uno a uno en la cabecera de este fichero y
                                 en `O18`. **No se reproducen aquí**, y tampoco se disimulan:
                                 pertenecen al **verificador externo de `F6`** y siguen
                                 ABIERTOS hasta que exista. Presentar el sobre como si los
                                 cerrara es exactamente la afirmación que `O18` prohíbe.

11 DÓNDE PARAR                   antes de redactar `(g)`, antes de crear `C8`, antes de
                                 tocar `C7` o el kernel operativo SUSTANTIVO, antes de
                                 iniciar `F5`, antes de iniciar `F6` —el verificador externo
                                 está CONTRATADO, no autorizado— y antes de iniciar
                                 PesquerApp. `O15` dice qué será la adopción cuando ocurra,
                                 no que ocurra ahora; `O17` dice qué se certificará al
                                 arrancar cada macrocircuito, no que se construya hoy; y
                                 `O18` dice con qué raíz se verifica y quién cierra la clase
                                 que queda, no que `F4c` esté cerrada.
```

> **[HISTÓRICO · «Siguiente acción exacta» anterior a la resolución `O18` del Owner. Se
> conserva ENTERA para trazabilidad y NO describe el estado vigente: su paso 4 declara que el
> trabajo PARA y espera al Owner, su paso 5 manda LLEVARLE la clase `B`, y su paso 9 manda no
> encargar ningún gate hasta que responda. **El Owner ya respondió: es `O18`.**]**

## Siguiente acción exacta — HISTÓRICA, anterior a `O18`

> **POR QUÉ ESTA SECCIÓN ESTÁ ESCRITA ASÍ, y es una garantía y no un adorno.** Ha caducado
> **tres veces consecutivas**: `K-01`/`J-10`/`L-01` en el gate del documento 19; `P-05`≡`Q-08`
> —el único GRAVE de aquel gate— y `R-02` en el del documento 21; y `S-17`≡`S3-05` en el del
> documento 23. Siempre por la misma causa: **copiaba lo que otra sede deriva**.
> Regla de esta sección, desde aquí:
> **nada que otra sede pueda derivar se copia dentro de ella.** Remiten, y no se escriben:
> los SHA (a `git rev-parse` y `git ls-remote`) · el recuento de comprobaciones de la batería
> (a la batería) · el censo de presiones vigentes (a §16 del documento 11, con su comando) ·
> la excepción del kernel (al campo **EXCEPCIÓN EXACTA DEL KERNEL** de este mismo fichero) ·
> el ordinal de la tanda (a las cabeceras `###` de §15.8 del documento 11) · el reparto por
> severidad de los hallazgos (a §12 y §13 de la adjudicación de `U`, dentro del documento 23)
> · y la lista de manifiestos publicados (a la tabla de `00-INDICE.md`). Lo que quede escrito
> aquí es lo que **no tiene otra sede**: qué pasó, qué se está haciendo y dónde hay que parar.

```text
[HISTÓRICO · todo lo que sigue hasta el final de esta sección es el texto ANTERIOR a la
 resolución `O18` del Owner. Describe la clase `B` como ABIERTA y PENDIENTE, y manda parar
 a esperarla: hoy está RESUELTA y el trabajo ha seguido. NO describe el estado vigente, que
 está en «Siguiente acción exacta», arriba. Su regla de redacción —nada que otra sede pueda
 derivar se copia dentro de ella— NO es histórica: sigue vigente y la sección de arriba la
 hereda.]

0  DÓNDE ESTAMOS, EXACTO         el **SEGUNDO GATE INDEPENDIENTE DE CERTIFICACIÓN** ya corrió
                                 y **su veredicto ya está publicado**: `INSUFICIENTE PARA F5`,
                                 en el documento 23. Corrió sobre la candidata que la tanda
                                 anterior publicó —rama `review/f4c-o17-candidate-20260830`—
                                 y el veredicto vive en la rama
                                 `review/f4c-gate-certificacion-2-20260830`.
                                 Ocho agentes de contexto limpio: revisor `S` como cadena
                                 `S1`–`S4`, revisor `T` como `T1`·`T2`·`T3` en paralelo y sin
                                 verse, y el adjudicador `U`. **Ninguno participó en ningún
                                 gate anterior**, y **ningún hallazgo se corrigió en esa
                                 pasada**: es deliberado, porque quien recibe no aplica.
                                 **Los SHA no se copian aquí**: se derivan con
                                   git rev-parse HEAD
                                   git ls-remote origin
                                 [ESTADO ANTERIOR · el paso 7 de la versión de esta sección
                                  que ahora va rotulada HISTÓRICA mandaba «publicar la
                                  candidata nueva y encargar otro gate». **Las dos cosas
                                  están hechas**: la candidata se publicó y el gate emitió su
                                  veredicto. Quien dijera «Continúa» recibía una instrucción
                                  ya cumplida — `S-17` del documento 23, y la TERCERA
                                  recurrencia consecutiva sobre esta misma sección.]

1  QUÉ DEVOLVIÓ, SIN ADORNO      **INSUFICIENTE PARA F5**, con **49 hallazgos distintos**.
                                 El reparto por severidad y por clase **no se copia aquí**:
                                 lo publica el bloque de cabecera de este fichero y, como
                                 sede primaria, §12 y §13 de la adjudicación de `U` dentro
                                 del documento 23. Lo único que hace falta para actuar:
                                 **48 de los 49 son de clase `A`** —remedio determinado, sin
                                 decidir arquitectura— **y se están cerrando en la tanda en
                                 curso**, agrupados POR CAUSA y no por línea.
                                 **Y consta lo que quedó cerrado**: `C-L.5` CERTIFICADA por
                                 tercera vez consecutiva sobre universo derivado, y `R-04`
                                 CERRADO CON MECANISMO tras dos gates sin lograrlo.

2  LA ÚNICA CLASE `B`,           **NO es un hallazgo: es LA RAÍZ, y está ABIERTA.** `M-04`
   Y ES LA RAÍZ                  —«se puede construir un árbol defectuoso que pase la batería
                                 en verde»— **no es satisfacible desde dentro de F4**. La
                                 batería vive dentro del repositorio que audita y decide si
                                 algo está intacto contra referencias que también viven ahí:
                                 quien puede escribir el repositorio puede escribir la
                                 referencia, y puede amputar la batería.
                                 **No lo dice primero el gate: lo declaró el propio corpus en
                                 §11.4 del documento 11** —«si el runner miente, nada dentro
                                 del repositorio lo detecta; cerrarlo exige un verificador
                                 EXTERNO al repositorio, y eso NO se resuelve aquí»—, y
                                 **ningún gate lo había llevado al Owner**.
                                 **LA PREGUNTA AL OWNER, con sus TRES alternativas y el coste
                                 de cada una, está redactada palabra por palabra en §13 de la
                                 adjudicación de `U`, dentro del documento 23.** No se copia
                                 aquí: se lee allí, que es su sede.

3  QUÉ SE ESTÁ HACIENDO AHORA    cerrar los **48 de clase `A`**, agrupados POR CAUSA:
                                 propagación de decisiones ya tomadas en el documento 11 ·
                                 batería, validadores y derivador · documentación, recuentos
                                 y trazabilidad. El agrupamiento por remedio lo publica §13
                                 de la adjudicación de `U`; **no se reproduce aquí**.
                                 **Y expresamente NO se escribe una decimosexta protección
                                 sistémica**: el adjudicador midió las quince de la tanda
                                 anterior y sólo tres generalizan. Añadir una más movería la
                                 circularidad de sitio, que es lo que §11.4 predijo.

4  DÓNDE SE DETIENE EL TRABAJO   **aquí, y no se abre una cuarta ronda.** Tres gates
                                 consecutivos han fallado por la MISMA causa, y esa causa es
                                 una decisión que F4 tiene prohibido tomar: `G21` de
                                 `KERNEL.md` L690 dice que un sistema no puede definir sin
                                 conflicto de interés los criterios que aprueban su propia
                                 existencia. **Después de cerrar los 48 de clase `A`, el
                                 trabajo PARA y espera respuesta del Owner.** Encargar un
                                 cuarto gate antes de esa respuesta es gastar ocho agentes
                                 para volver a leer el mismo veredicto.

5  QUÉ LLEVAR AL OWNER           dos cosas, y en este orden:
                                 (i) **LA CLASE `B`**: la pregunta de §13 de la adjudicación
                                     de `U`, con sus tres alternativas —declarar el límite y
                                     dejar de medirlo · dar un ancla fuera del árbol dentro
                                     de lo que F4 alcanza · un verificador externo de verdad—
                                     y el coste de cada una. **F4 no elige, y lo dice.**
                                 (ii) las presiones normativas vigentes de §16 — **el total
                                     NO se copia aquí**: se deriva con
                                       grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
                                         | grep -vc 'RETIRADA\|FUSIONADA'
                                     Registrar es F4; elegir es F5.

6  EL KERNEL SUSTANTIVO          no se ha tocado, y la excepción **no se reproduce aquí**:
                                 vive en el campo `EXCEPCIÓN EXACTA DEL KERNEL` de este mismo
                                 fichero, derivada de Git y contrastada por `G-23`.
                                 **Se remite, no se copia**: una lista copiada envejece sola.

7  LO QUE EL PRÓXIMO GATE        **la regla que este corpus escribió y que el segundo gate
   TIENE QUE CUMPLIR SIN         incumplió**: todo documento que `C-L.5` obligue a publicar
   EXCUSA                        —manifiesto de asignación, manifiestos de lectura, addenda y
                                 corrigenda— **se enlaza desde la tabla de `00-INDICE.md` en
                                 el MISMO commit que lo crea**. No vale añadirlo a
                                 `exclusiones.yaml`: una exclusión APAGA `T147` en vez de
                                 cumplirlo. La regla y la tabla están en `00-INDICE.md`, bajo
                                 «Lo que cada gate tiene que publicar, y desde dónde se
                                 enlaza», con el comando que deriva los huérfanos.

8  ESTADO, SIN ADORNO            **`F4c` sigue ABIERTA. `F5` sigue NO AUTORIZADA.** El
                                 segundo gate no cierra `F4c`, no autoriza `F5`, no levanta
                                 ninguna condición `C-L` y no deroga ninguna presión vigente.
                                 Ninguna enmienda normativa está redactada, `C8` no existe y
                                 `C7` no se ha tocado. **No se ha hecho merge en
                                 `redesign/kernel-2.0`.** **APLICAR NO ES CERTIFICAR**, y
                                 esta tanda la aplica quien la recibió: **NINGÚN hallazgo del
                                 documento 23 se declara SUPERADO**, y sólo un gate
                                 independiente posterior podría declararlo.

9  DÓNDE PARAR                   después de cerrar los 48 de clase `A` y **antes** de
                                 encargar ningún gate nuevo, mientras la clase `B` siga sin
                                 respuesta del Owner. Sigue vigente además parar antes de
                                 redactar `(g)`, antes de crear `C8`, antes de tocar `C7` o
                                 el kernel operativo SUSTANTIVO, y antes de iniciar
                                 PesquerApp. `O15` dice qué será la adopción cuando ocurra,
                                 no que ocurra ahora; `O17` dice qué se certificará al
                                 arrancar cada macrocircuito, no que se construya hoy.
```

> **[HISTÓRICO · «Siguiente acción exacta» anterior al SEGUNDO GATE DE CERTIFICACIÓN,
> documento 23. Se conserva ENTERA para trazabilidad y NO describe el estado vigente: su
> paso 7 manda publicar una candidata que YA está publicada y encargar un gate que YA emitió
> su veredicto. Es `S-17` del documento 23.]**

## Siguiente acción exacta — HISTÓRICA, anterior al documento 23

```text
[HISTÓRICO · todo lo que sigue hasta el final de esta sección es el texto ANTERIOR al
 SEGUNDO GATE DE CERTIFICACIÓN del documento 23. Sus cifras son las de aquel momento y
 varias han caducado —los 68 de clase `A` son los del documento 22, no los 48 de hoy—;
 NO describe el estado vigente, que está en «Siguiente acción exacta», arriba.]

0  DÓNDE ESTAMOS, EXACTO         la candidata `4d231ee` está publicada en
                                 `review/f4c-post-gate-manifiestos-candidate-20260830`.
                                 Sobre ella se ejecutó el **GATE INDEPENDIENTE DE
                                 CERTIFICACIÓN CON UNIVERSO DERIVADO** —diez agentes de
                                 contexto limpio: cadenas `P1`–`P4` y `Q1`·`Q2`·`Q3`·`Q5`·`Q4`
                                 en paralelo sin verse, y el adjudicador `R`—, y su documento
                                 es el 22.
                                 **Su veredicto fue INSUFICIENTE PARA F5, y NO por cobertura.**
                                 **EL OWNER YA RESPONDIÓ**, y la tanda en curso está aplicando
                                 su resolución y los 68 hallazgos de clase `A`.
                                 Los SHA del árbol vigente se derivan con `git rev-parse HEAD`
                                 y `git ls-remote`. Los que aparecen escritos son snapshots
                                 históricos publicados, y por eso se nombran.

1  LA DECISIÓN DE CLASE B        **RESUELTA. YA NO BLOQUEA.** De los 69 hallazgos, 68 eran
   YA NO BLOQUEA                 clase `A` —remedio determinado, sin decidir arquitectura— y
                                 UNO era clase `B`, decisión exclusiva del Owner. **Cero de
                                 clase `C`.** El trabajo se paró ahí, se agrupó la pregunta y
                                 se preguntó, que es la regla. **El Owner contestó el
                                 2026-08-30**, y su respuesta está registrada como **`O17`**
                                 en §2 de `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`.

2  QUÉ ELIGIÓ EL OWNER,          la pregunta era el **nivel ESTRUCTURAL y su productor**.
   Y POR QUÉ                     Eligió la **alternativa (b): que cada macrocircuito produzca
                                 su certificación Estructural AL ARRANCAR, como precondición
                                 propia de esa ejecución.**
                                 **Su motivo, en sus palabras: ROBUSTEZ Y REVALIDACIÓN
                                 PERMANENTE POR ENCIMA DEL AHORRO OPERATIVO.** «No elijo la
                                 alternativa barata de certificarlo sólo durante la
                                 instalación. Quiero que instalación, adopción, migración y
                                 actualización comprueben la estructura vigente antes de
                                 continuar. La prioridad es una base sólida y permanente,
                                 aunque suponga más comprobaciones y consumo de recursos.»
                                 DESCARTA (a) —certificarlo sólo en la instalación— porque un
                                 producto ya instalado NO revalidaría su Estructural al
                                 cambiar el kernel. DESCARTA (c) —degradarlo a precondición
                                 no certificada— porque obliga a reescribir §9.2 y **cambia
                                 el contenido de `O12`**, que es resolución suya.
                                 **ACEPTA EXPRESAMENTE EL COSTE**: un gate más en los cuatro
                                 recorridos, y migración y actualización más caras.
                                 Con la (b), **`O12` pasa a ser satisfacible desde CUALQUIER
                                 entrada**, que era el GRAVE nº 2 del documento 22.

3  QUÉ SE ESTÁ APLICANDO         **`D107`**, la propagación de `O17`, declarada **DERIVADA**
                                 y no elegida por F4: sede nueva **§9.6 ·
                                 `gate:sistema-conforme`** con productor, sujeto, evidencia,
                                 vigencia y condición de invalidación · **FASE 0 de
                                 CERTIFICACIÓN ESTRUCTURAL** en los cuatro macrocircuitos
                                 §8.1–§8.4 · filas en §18 · tabla adversarial `X-S1`–`X-S9` ·
                                 y los bloques de §15.8 que faltaban para `D96`–`D107`.
                                 **`PN-17` y `PN-18`** se registran como presiones nuevas.
                                 Y los **68 de clase `A`**, agrupados POR CAUSA y no por
                                 línea, con las protecciones sistémicas que `R` nombra:
                                 extender el rango inmutable de `G-22` a los documentos 19,
                                 20, 21 y a los manifiestos; evaluar el bloque histórico
                                 sobre la OCURRENCIA y no sobre la línea; contrastar `G-16`
                                 por igualdad de estado y no por prefijo; exigir polaridad en
                                 `G-01`; extender la comparación de CONJUNTOS más allá de
                                 `kernel/`; y fijar la excepción del kernel por CONTENIDO y
                                 no sólo por ruta.
                                 **Ninguna de las seis es una sustitución manual más: las
                                 seis son la generalización de un perímetro que no
                                 generalizaba.**

4  EL ORDINAL DE ESTA TANDA      **no se escribe aquí, y es deliberado.** Una versión anterior
                                 decía «ésta es la décima» dos tandas después de serlo. El
                                 número de correcciones del documento 11 tiene **UNA sede**:
                                 las cabeceras `###` de §15.8 de ese documento, y se deriva
                                 con
                                   awk '/^## 15\.8 /{f=1;next} f&&/^## /{exit} \
                                        f&&/^### /{n++} END{print n}' \
                                       docs/evolucion/11-ARQUITECTURA-INTEGRADA.md
                                 `00-INDICE.md` **no es un segundo recuento del mismo
                                 universo**: registra UNA FILA por tanda desde el gate final,
                                 y su cuenta difiere de la de §15.8 exactamente en las tandas
                                 que **no añadieron ninguna decisión `D`** —hoy, la del
                                 documento 21—. Decirlo así es lo que hace que la regla
                                 EJECUTE: es `Q-17`≡`P-03` del documento 22, que la encontró
                                 declarándose derivada de dos sedes que daban cifras distintas.

5  QUÉ LLEVAR AL OWNER           las presiones normativas vigentes de §16 — **el total NO se
                                 copia aquí**: se deriva con
                                   grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md \
                                     | grep -vc 'RETIRADA\|FUSIONADA'
                                 con `PN-1` bloqueando todo el estado durable, y `PN-17` y
                                 `PN-18` como las que esta tanda añade:
                                 `reconciliacion_pendiente` sin productor, que deja `T22` de
                                 (a) insatisfacible, y la grafía `VER:decisión` frente a
                                 `VER:decision`, que **ya convive en dos variantes dentro del
                                 kernel construido**.
                                 Registrar es F4; elegir es F5.

6  EL KERNEL SUSTANTIVO          no se ha tocado, y la excepción **no se reproduce aquí**: vive
                                 en el campo `EXCEPCIÓN EXACTA DEL KERNEL` de este mismo
                                 fichero, derivada de Git y contrastada por `G-23`.
                                 **Se remite, no se copia**: una lista copiada envejece sola.

7  EL SIGUIENTE PASO             **terminar de aplicar los 68 de clase `A`, PUBLICAR EL ÁRBOL
                                 VIGENTE COMO CANDIDATA NUEVA, y ENCARGAR OTRO GATE
                                 INDEPENDIENTE sobre ella.** Sus revisores tienen que ser
                                 nuevos, con contexto limpio, y **ninguno puede haber aplicado
                                 esta tanda**. Ese gate deberá publicar otra vez el manifiesto
                                 previo de ASIGNACIÓN —con la regla `1bis` de `C-L.5`: de qué
                                 sede sale el universo obligatorio y con qué comando
                                 auditable— y los manifiestos de LECTURA, **y ENLAZARLOS desde
                                 `00-INDICE.md` en el mismo commit que los cree**: sin ese
                                 enlace rompe `T147`, que es la laguna que `P-27`≡`Q-08`
                                 levantó y que esta tanda cierra con una regla escrita.

8  ESTADO, SIN ADORNO            **`F4c` sigue ABIERTA. `F5` sigue NO AUTORIZADA.** `O17`
                                 **no autoriza iniciar F5**, ni F6, ni la adopción de
                                 PesquerApp; no levanta ninguna condición `C-L`, no cierra
                                 `F4c` y no deroga ninguna presión vigente. Ninguna enmienda
                                 normativa está redactada, `C8` no existe y `C7` no se ha
                                 tocado. **No se ha hecho merge en `redesign/kernel-2.0`.**
                                 **APLICAR NO ES CERTIFICAR**, y esta tanda la aplica quien
                                 la recibió: **NINGÚN hallazgo del documento 22 se declara
                                 SUPERADO**, y sólo un gate independiente posterior puede
                                 declararlo.

9  DÓNDE PARAR                   después de aplicar y publicar la candidata, y **antes** de
                                 dar por cerrada `F4c`. También sigue vigente parar antes de
                                 redactar `(g)`, antes de crear `C8`, antes de tocar `C7` o el
                                 kernel operativo SUSTANTIVO, y antes de iniciar PesquerApp.
                                 `O15` dice qué será la adopción cuando ocurra, no que ocurra
                                 ahora; `O17` dice qué se certificará al arrancar cada
                                 macrocircuito, no que se construya hoy.
```

> **[HISTÓRICO · «Siguiente acción exacta» anterior al GATE DE CERTIFICACIÓN, documento 22.
> Se conserva para trazabilidad y NO describe el estado vigente.]**

## Siguiente acción exacta — HISTÓRICA, anterior al documento 22

```text
[HISTÓRICO · todo lo que sigue hasta el final de esta sección es el texto ANTERIOR al
 GATE DE CERTIFICACIÓN del documento 22 y a la resolución `O17` del Owner. Sus cifras
 son las de aquel momento y varias han caducado; NO describe el estado vigente, que
 está en «Siguiente acción exacta», arriba. Se conserva para trazabilidad.]

0  DÓNDE ESTAMOS, EXACTO         la candidata `7764cca` **está publicada** en
                                 `review/f4c-post-gate-cobertura-candidate-20260829`.
                                 Sobre ella se ejecutó el **GATE INDEPENDIENTE DE CIERRE CON
                                 MANIFIESTOS VERIFICABLES** —revisores `P` y `Q` en paralelo
                                 sin verse, adjudicador `R`—, **publicado** en
                                 `review/f4c-gate-cierre-manifiestos-20260829` = `f2c4348`,
                                 y su documento es el 21.
                                 **Su veredicto fue INSUFICIENTE PARA F5, y NO por cobertura.**
                                 Nada de esto está por encargar: está hecho, y consta.

1  QUÉ CERTIFICÓ ESE GATE        **`C-L.5`, la COBERTURA, por primera vez en el expediente.**
                                 Manifiesto previo de ASIGNACIÓN commiteado SOLO y antes de
                                 que existiera ningún revisor; tres manifiestos de LECTURA; y
                                 la resta CALCULADA en vez de presumida:
                                 `asignado − leído = ∅` en los tres. `R` recalculó las 43
                                 filas contra el árbol y las 43 coinciden.
                                 **Certificar la cobertura NO cierra `F4c` y NO autoriza `F5`.**

2  POR QUÉ FALLÓ AUN ASÍ         por DOS de las siete condiciones, y ninguna es la cobertura:
                                 · la 3 — dos de los cuatro pilares declarados de `D104` son
                                   falsables contra el árbol, y las dos falsaciones pasaban
                                   EN VERDE (`Q-02`, `Q-05`)
                                 · la 6 — SIETE contradicciones materiales vigentes sin
                                   registrar, tres de ellas segunda o tercera recurrencia de
                                   la misma frase, **y una era esta misma sección**

3  QUÉ HA HECHO ESTA TANDA       ha corregido los **24 hallazgos distintos** del documento 21
                                 —`BLOQUEANTE 0 · GRAVE 1 · MEDIO 12 · MENOR 11`—, cada uno
                                 reproducido antes de tocarlo. La matriz de trazabilidad, con
                                 una fila por hallazgo, está más arriba en este fichero.
                                 **NINGUNO se declara SUPERADO**: corregido por quien lo
                                 recibió no es superado por revisión independiente.
                                 **Y esta sección se reescribió entera**, porque `P-05`≡`Q-08`
                                 y `R-02` la encontraron con CINCO afirmaciones falsas a la
                                 vez, sin marca de histórica, siendo el punto de entrada que
                                 la cabecera de este fichero designa.

4  EL ORDINAL DE ESTA TANDA      **no se escribe aquí, y es deliberado.** La versión anterior
                                 decía «ésta es la décima» dos tandas después de serlo. El
                                 número de tandas se DERIVA de los bloques de §15.8 del
                                 documento 11 y de las filas de `00-INDICE.md`, que es donde
                                 se registran, y de ninguna otra parte.

   [HISTÓRICO · las cifras de este paso son las de aquel momento y han caducado; el censo
    vigente lo deriva §16 del documento 11 con el comando que la sección vigente publica]
5  QUÉ LLEVAR AL OWNER           las **CATORCE** presiones de §16 —el recuento se DERIVA de
                                 las cabeceras `## \`PN-`, y `G-26` lo contrasta también
                                 contra ESTE fichero desde `P-05`—, con `PN-1` bloqueando
                                 todo el estado durable y **`PN-16` como la única que esta
                                 tanda añade**: la grafía canónica de `<CAP>:revisión` vive
                                 en (b) L836, que es material APROBADO, y **F4 no puede
                                 elegirla**. Sale de `P-07`.
                                 **Y `F-08`, que es trabajo de F5 y NO es presión normativa**:
                                 su registro vive en §19 y en la matriz, con
                                 `requiere F5 · sí · sin PN`.

6  EL KERNEL SUSTANTIVO          **no se ha tocado**, y la excepción **no se reproduce aquí**:
                                 vive en el campo `EXCEPCIÓN EXACTA DEL KERNEL` de este mismo
                                 fichero, **derivada de Git y contrastada por `G-23`**. Son
                                 SEIS ficheros = TRES directos + TRES de evidencia derivada.
                                 Esta sección enumeraba TRES y omitía los otros, reproduciendo
                                 `M-06` en la misma tanda que lo declaraba corregido (`R-02`).
                                 **Se remite, no se copia**: una lista copiada envejece sola.

7  EL SIGUIENTE PASO             **publicar el árbol vigente como candidata nueva, y encargar
                                 otro GATE INDEPENDIENTE sobre ella.** Sus revisores tienen
                                 que ser nuevos, con contexto limpio, y **ninguno puede haber
                                 aplicado esta tanda**. El gate deberá publicar otra vez el
                                 manifiesto previo de ASIGNACIÓN —ahora con la regla de
                                 `1bis` de `C-L.5`: de qué sede sale el universo obligatorio,
                                 y el comando auditable con que se obtiene— y los manifiestos
                                 de LECTURA.
                                 Los SHA de este árbol se derivan con `git rev-parse HEAD` y
                                 `git ls-remote`. Los que aparecen escritos arriba —`7764cca`
                                 y `f2c4348`— son **snapshots históricos publicados**, y por
                                 eso se nombran: no describen el árbol vigente.

8  ESTADO, SIN ADORNO            **las correcciones de esta tanda están APLICADAS, NO
                                 CERTIFICADAS.** `F4c` sigue **ABIERTA**. `F5` sigue **NO
                                 AUTORIZADA**. No se ha iniciado F5, ni F6, ni PesquerApp.
                                 Ninguna enmienda normativa está redactada, `C8` no existe y
                                 `C7` no se ha tocado. **No se ha hecho merge en
                                 `redesign/kernel-2.0`.**

9  DÓNDE PARAR                   antes de redactar `(g)`, antes de crear `C8`, antes de tocar
                                 `C7` o el kernel operativo SUSTANTIVO, y antes de iniciar
                                 PesquerApp.
                                 `O15` dice qué será cuando ocurra, no que ocurra ahora.
```
