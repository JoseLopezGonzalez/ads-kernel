# PLAN DE INVESTIGACIÓN — qué hay que saber antes de cerrar arquitectura

La directiva prohíbe cerrar el diseño antes de la minería (23.3) y la síntesis (23.4). Este
plan dice **qué preguntas decide la evidencia**, **cómo se obtiene** y **en qué orden**.

## Las preguntas que la evidencia debe responder

Cada una está abierta porque cerrarla hoy sería inventar. Cada una lleva **qué decide** y
**qué la respondería**.

| | pregunta | decide | la responde |
|---|---|---|---|
| Q1 | ¿existe conocimiento válido en varios proyectos nuestros que ningún pack explica? | si la cuarta capa de **X1** existe | decisiones repetidas en dos o más proyectos, sin relación con su clase |
| Q2 | ¿de qué está hecho ese conocimiento? | la forma de la capa, y su nombre | el reparto real de los candidatos: stack, patrones de UI, testing, despliegue, convenciones |
| Q3 | ¿qué es una skill, medida por lo que ya existe? | si `skill` es tipo canónico nuevo, método existente o herramienta | las skills reales de los proyectos: cuáles se usaron, cuáles se abandonaron |
| Q4 | ¿qué patrones de trabajo se repiten sin haber sido formalizados? | qué métodos y circuitos faltan en el kernel | instrucciones repetidas, mecanismos creados para evitar un error recurrente |
| Q5 | ¿cómo se gobierna Git hoy, de hecho, en los proyectos del Owner? | el contrato del apartado 8, entero | ramas, PR, revisión, releases, hotfixes y lo que falló |
| Q6 | ¿qué pierde cada entorno agentic respecto a los demás? | qué degrada un adaptador y qué no puede degradar | instrucciones y configuraciones reales de Claude Code, Codex y Cursor en esos proyectos |
| Q7 | ¿qué se rompió por pérdida de contexto entre sesiones? | los requisitos reales de estado, memoria y reanudación | retrabajo, decisiones tomadas dos veces, contexto reexplicado |
| Q8 | ¿qué mecanismos de revisión redujeron retrabajo de verdad? | qué gates merecen ser obligatorios | evidencia de uso, no opinión sobre su utilidad |
| Q9 | ¿qué representa la minería dentro de `b.16`? | si hace falta un proceso canónico nuevo — **X4** | el trabajo, una vez hecho una vez |
| Q10 | ¿qué tiene ya cada proyecto que ADS **no** debe sustituir? | el contrato del apartado 6.5 | soluciones locales mejores que el default de ADS |

**Q1 y Q3 son las que bloquean la arquitectura.** Sin ellas, el diseño de capas y el de
skills serían preferencias, no conclusiones.

**Estado tras la minería y el contraste** —PesquerApp, registrado en
[`05-CANDIDATOS.md`](05-CANDIDATOS.md) y [`06-CONTRASTE.md`](06-CONTRASTE.md)—:

```text
Q3   RESPONDIDA     una skill es el disparador específico de un proveedor sobre un método
                    que ya existe. El contenido vive en el workflow neutral.
Q1   NO RESPONDIDA  ni en positivo ni en negativo. NO existe evidencia independiente
     · DEFERIDA     suficiente para demostrar si hace falta una capa entre PACK y PROFILE.
                    El Owner retiró gym-wear el 2026-08-26 por fuente contaminada: nació
                    de una versión primitiva de ADS. PesquerApp es la única fuente externa
                    madura de esta fase, y sus dos repositorios son un solo producto.
                    Registrada como problema P-05. NO se diseña ninguna capa.
Q3bis ABIERTA       una skill de TERCEROS —shadcn, con origen y hash en skills-lock.json—
                    no es un disparador: es conocimiento ajeno vendorizado, y ADS no tiene
                    posición para él en su precedencia. Registrada como problema P-02.
Q4 Q6 Q7 Q8         respondidas en el contraste, dentro de los veredictos por candidato.
Q5                  respondida, y corrigió el mapa: G29 gobierna más de lo que F0 dijo.
                    Registrada como problema P-04.
Q9 Q10              abiertas. Entran en la síntesis.
```

**Estado tras la síntesis** —[`09-SINTESIS.md`](09-SINTESIS.md)—:

```text
Q9   RESPONDIDA     la minería es un `AUD` con `SIS` como consumidor declarado. No hace
                    falta un proceso nuevo: la correspondencia es campo a campo con el
                    bloque `ads:proceso` de AUD, y la minería ya se ejecutó una vez, así
                    que no hay que suponer qué forma tendría. El esquema `candidato` se
                    APLAZA, con su condición escrita: se justifica cuando la minería
                    ocurra por segunda vez sobre una fuente independiente — la misma
                    condición que reabre P-05.
Q10  RESPONDIDA     no con una lista, con una señal: lo que no se sustituye es lo que
                    tiene CICATRIZ ESCRITA, un mecanismo cuyo motivo está en su propio
                    comentario y sigue siendo cierto. CAND-012, CAND-014 y CAND-024 lo
                    demuestran, y la comprobación es que ADS adoptó tres de los cuatro.
                    Es el criterio operable que le faltaba al 6.5 del brief.
```

## Qué necesita el sistema del Owner

**Ya no bloquea nada.** La minería está cerrada con la única fuente que el Owner considera
válida.

```text
ENTREGADO      PesquerApp, frontend y backend, minados el 2026-08-26.
RETIRADO       gym-wear, el 2026-08-26, por decisión del Owner: nació de una versión
               primitiva de ADS y su evidencia estaría contaminada.
CONSECUENCIA   Q1 queda sin respuesta posible con el material disponible, y X1 queda
               DEFERIDA — no bloqueada. Ver P-05 en 06-CONTRASTE.md.
FUTURO         se reabre si aparece un proyecto independiente y maduro. No antes.
```

## Protocolo de minería

Un proyecto se recorre por **ocho lentes**, no por su árbol de directorios. Buscar carpetas
llamadas `skills` es el modo de fallo que la directiva señala en su 5.2.

```text
L1  INSTRUCCIÓN PERSISTENTE   AGENTS.md · CLAUDE.md · reglas de Cursor · Codex · prompts
                              guardados · subagentes · skills declaradas
L2  AUTOMATISMO               scripts · hooks · Makefile · CI/CD · workflows · linters ·
                              generadores · cualquier cosa creada porque algo fallaba
L3  GOBIERNO GIT              ramas vivas y muertas · worktrees · convención de commits ·
                              PR y su revisión · tags · releases · hotfixes · rollbacks
L4  VERIFICACIÓN              tests y su cobertura real · auditorías · revisión visual ·
                              lo que se comprueba a mano y nadie automatizó
L5  CONOCIMIENTO              ADR · documentación de arquitectura · journals · backlog ·
                              TODO · issues · decisiones implementadas y nunca escritas
L6  TECNOLOGÍA                stack · librerías · patrones de UI · datos y migraciones ·
                              despliegue · observabilidad · autenticación
L7  CICATRICES                lo más valioso. Mecanismos que existen para evitar un error
                              concreto que ya ocurrió. Se reconocen por su comentario:
                              «no hagas X porque...»
L8  SISTEMA IMPLÍCITO         secuencias repetidas de trabajo que nadie llamó proceso.
                              Se detectan por repetición, no por nombre
```

Por cada lente se recoge **lo que hay** y **cuántas veces se usó**. Una skill escrita y
nunca invocada es un hallazgo distinto de una skill invocada cien veces.

## Ficha de candidato

Los campos son los que la directiva pide en su 5.4. **No es un bloque canónico**: hoy no
existe un esquema `candidato`, y crear un tipo canónico es materia de la síntesis, no de una
comodidad de registro. Se escribe como tabla en
[`05-CANDIDATOS.md`](05-CANDIDATOS.md), un candidato por fila de detalle.

**La síntesis lo resolvió, y lo aplazó.** La ficha es la evidencia de la obligación
`conclusion-fundada` del `AUD` que representa la minería, y una tabla la sostiene. El esquema
canónico se justifica cuando la minería ocurra por segunda vez sobre una fuente
independiente — la misma condición que reabre `P-05`. Ver [`09-SINTESIS.md`](09-SINTESIS.md).

```text
id             CAND-nnn
candidato      qué es, en una línea
origen         proyecto y ruta exacta dentro de él
lente          L1..L8
problema       qué problema resolvía ALLÍ
mecanismo      cómo funciona, sin adornos
evidencia      pruebas de uso: frecuencia, commits, incidentes que evitó
                 · SIN EVIDENCIA es un valor legítimo, y cambia la decisión
aplicabilidad  universal | por clase | nuestra | por proveedor | de ese proyecto
solapamiento   con qué pieza de ADS choca o coincide, por identificador
contradiccion  qué regla aprobada contradice, o «ninguna»
destino        kernel | pack | capa por decidir (X1) | skill | tooling | adaptador |
               conocimiento de ese proyecto | descarte
decision       incorporar | fusionar | adaptar | investigar | descartar | ABIERTA
motivo         por qué esa decisión, con la evidencia enlazada
```

**Regla dura:** un candidato con `destino` sin `evidencia` no puede pasar de
`decision: investigar`. La directiva lo dice de otra forma en su regla 4: extraer, comparar,
criticar y clasificar — nunca copiar.

## Orden de trabajo, y sus puertas

```text
F0  BASELINE Y MAPA          HECHO — 01, 02, 03 y este plan
      ↓ puerta: nada más entra hasta que el Owner entregue las rutas

F1  MINERÍA                  un proyecto cada vez, ocho lentes, fichas con procedencia
      ↓ puerta: el inventario existe y cada ficha tiene origen comprobable   CERRADA

F2  CONTRASTE                cada candidato contra ADS: solapamiento y contradicción
      ↓ puerta ORIGINAL: Q1 y Q3 con respuesta. Q3 la tiene; Q1 NO PUEDE TENERLA con
        el material disponible, y la puerta se sustituye por su registro como P-05

F3  SÍNTESIS                 ADS actual + directiva + candidatos + evidencia   ENTREGADA
      ↓ puerta SUPERADA: X1 deferida con su línea escrita · X2 resuelta por lectura, con
        su parte de Owner acotada a una pregunta · X3 resuelta: el adaptador es una
        proyección compilada, no una capa · X4 resuelta: la minería es AUD · X5 resuelta
        en su forma, y su ubicación es del Owner. Y tres contradicciones NUEVAS
        registradas sin resolver: X6, X7 y X8

F4  ARQUITECTURA INTEGRADA   una sola propuesta que explique todos los subsistemas juntos
      ↓ puerta: CRÍTICA INDEPENDIENTE, por quien no la escribió

F5  ENMIENDAS                lo que toque (a), (b) o K-1 va al Owner por separado
      ↓ puerta: aprobación explícita

F6  DESCOMPOSICIÓN           items SIS trazables, y ejecución incremental
```

**F4 no la certifica quien la escribe.** La iteración anterior ya dejó el precedente: una
auditoría independiente encontró treinta y tres hallazgos, dos de ellos en pruebas que
figuraban como superadas sin comprobar lo que su nombre afirmaba.

## Minería y piloto: cuál va primero

El [checkpoint anterior](../rediseno/CHECKPOINT-OPERATIVO.md) fijaba como siguiente acción
el piloto: instalar ADS en un proyecto y hacer pasar por él una frase del Owner. La
directiva ordena minar esos mismos proyectos. **La minería va primero, y no por preferencia:**

```text
1  La minería LEE. El piloto ESCRIBE. Leer un proyecto antes de instalarle nada no tiene
   coste de reversión; instalarlo antes de haberlo leído sí.

2  El apartado 6.5 exige reconocer lo que el proyecto ya hace bien ANTES de gobernarlo.
   Instalar primero es exactamente el error que ese apartado prohíbe.

3  El piloto sigue siendo lo único que convierte una prueba de `contrato-definido` a
   `prueba-ejecutada`. No se cancela: se ejecuta con lo aprendido, sobre el proyecto que
   la minería demuestre más adecuado.
```
