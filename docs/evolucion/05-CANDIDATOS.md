# INVENTARIO DE CANDIDATOS — minería de proyectos reales

Trabajo **23.3** de la [directiva](ADS-NEXT-OWNER-BRIEF.md). Un candidato es conocimiento
extraído de un proyecto real que **podría** mejorar ADS. Extraído no significa aceptado.

Campos, protocolo de las ocho lentes y reglas de clasificación:
[`04-PLAN-DE-INVESTIGACION.md`](04-PLAN-DE-INVESTIGACION.md).

## Proyectos minados

| proyecto | ruta | qué es | lentes | fecha |
|---|---|---|---|---|
| PesquerApp · frontend | `~/projects/lapesquerapp-frontend` | Next.js · ERP multi-tenant del sector pesquero | L1–L8 | 2026-08-26 |
| PesquerApp · backend | `~/projects/lapesquerapp-backend` | Laravel 10 · API `/api/v2` del mismo producto | L1–L8 | 2026-08-26 |

**Los dos repositorios son un solo producto.** Eso limita lo que esta pasada puede
concluir, y está dicho abajo en «Lo que esta minería NO puede responder».

## La escala del material encontrado

Todo lo de esta tabla se contó sobre el árbol, no se estimó.

```text
INSTRUCCIÓN PERSISTENTE   AGENTS.md · CLAUDE.md ×2 · 18 reglas de Cursor · 9 ficheros de
                          instrucciones de Copilot · .claude/ con agentes, comandos,
                          skills, reglas y herramientas
SKILLS                    37 en el frontend · 4 en el backend · duplicadas entre
                          .agents/skills/ y .claude/skills/
AGENTES DECLARADOS        18 en el frontend · 3 en el backend
GAP                       115 cerrados · 2 abiertos · plantilla con secciones por rol
SESIONES DE TRABAJO       17 carpetas .ai_work_context/<TIMESTAMP>/ con seis subniveles
MEMORIA DE PROYECTO       32 entradas PL-NNN con categoría y confianza
LOG DE EVOLUCIÓN          47 entradas con rating antes y después
GIT                       1839 + 2433 commits · 67 PR · 58 ramas remotas, 10 sin fusionar
```

## Respuesta a las dos preguntas que bloqueaban la arquitectura

### Q3 — qué es una skill · **RESPONDIDA**

El proyecto ya resolvió esto, y su respuesta es más limpia que la pregunta.

```text
docs/agent-system/workflows/gap-workflow.md    EL CONTENIDO. Neutral. 45 líneas de
                                               procedimiento: estados, flujo, obligaciones
                                               y prohibiciones de cada paso.

.agents/skills/lapesquerapp-gap-auditor/       EL DISPARADOR. 31 líneas. Declara cuándo
  SKILL.md                                     se activa —«audita GAP-NNN», «revisa la
                                               implementación»—, qué leer antes, y remite
                                               al workflow neutral.
```

**Conclusión con evidencia: una skill no es un tipo nuevo de contenido. Es el disparador
específico de un proveedor sobre un método que ya existe.** En vocabulario ADS: el
`metodo` es el workflow neutral, y la skill es la pieza de adaptador que lo activa con las
palabras que ese entorno reconoce.

Con una excepción que no encaja ahí: `skills-lock.json` registra una skill **de terceros**
—la de `shadcn/ui`— con su origen, su ruta y su hash. Eso no es un disparador: es
conocimiento externo vendorizado, con procedencia y control de integridad. Es la misma
figura que `kernel/.upstream-hash`, aplicada a conocimiento ajeno.

### Q1 — conocimiento nuestro que ningún pack explica · **INDICIOS, NO CONCLUSIÓN**

Hay indicio fuerte: `.ai_standards/` —el sistema de memoria de trabajo en tres capas— está
en **los dos repositorios**, que son de clase técnica distinta (Next.js y Laravel). Ningún
pack de clase explicaría algo que vale para los dos. Y los cinco ficheros **han divergido
entre copias**: el `README.md` del repositorio de frontend sigue titulándose *«Estándares
IA – PesquerApp Backend»*.

**Y el indicio no basta.** Los dos repositorios son un solo producto, con un solo Owner y
una sola historia. Que algo se repita entre ellos demuestra que se copió, no que sea
reutilizable entre proyectos independientes. **Q1 exige un segundo proyecto sin relación
con éste.** Hasta entonces, la cuarta capa de **X1** sigue sin justificación concluyente, y
proponerla ahora sería exactamente lo que la directiva prohíbe en su regla 3.

## Resumen por destino

| destino | candidatos |
|---|---|
| kernel universal | CAND-001 · 002 · 003 · 004 · 005 · 008 · 011 · 012 · 014 · 015 · 017 · 018 · 019 · 020 · 021 · 025 |
| pack de clase | CAND-022 · 024 |
| capa por decidir (X1) | CAND-029 |
| adaptador de proveedor | CAND-009 · 010 · 013 · 023 |
| tooling | CAND-027 |
| conocimiento de ese proyecto | CAND-006 |
| evidencia negativa · no se incorpora | CAND-016 · 026 · 028 |

**Ninguno está incorporado.** Todos quedan en `decision: investigar` o
`decision: incorporar` **propuesta**, y ninguna propuesta entra al kernel sin pasar por
síntesis, crítica independiente y —donde toque material aprobado— enmienda.

---

## Fichas

### Estado, memoria y sesión

**CAND-001 · Estructura persistente de sesión de trabajo**
`origen` frontend · `.ai_work_context/<TIMESTAMP>/` · `lente` L1, L8
`problema` el trabajo de una sesión se perdía al cerrarla, y el Owner reexplicaba contexto
`mecanismo` seis subniveles numerados por sesión: `00_working/` (activo, se borra al
cerrar), `01_analysis/`, `02_planning/`, `03_execution/`, `04_logs/`, `05_outputs/`
(entregables). `00_working/` contiene cuatro ficheros fijos: `active_task.md`,
`context_stack.md`, `decisions_pending.md`, `session_notes.md`
`evidencia` 17 sesiones reales, 129 ficheros versionados en git
`aplicabilidad` universal
`solapamiento` `a.9` deja abierta la disposición física del estado; esto es una disposición
física que funcionó. `a.10` checkpoint se parece a `active_task.md` + `context_stack.md`
`contradiccion` ninguna. **Complementa** un hueco declarado
`destino` kernel · `decision` **investigar** — es material directo para la disposición
física del estado, y llega con uso real detrás
`motivo` es lo más cercano a un runtime de estado que existe en el material minado

**CAND-002 · Tres capas de memoria con ciclo de vida escrito**
`origen` ambos repos · `.ai_standards/AGENT_MEMORY_SYSTEM.md` · `lente` L1
`problema` mezclar lo temporal con lo permanente hacía que ninguna de las dos sobreviviera
`mecanismo` corto plazo (sesión, se borra), medio plazo (evoluciona durante la tarea, se
entrega), largo plazo (permanente, se consulta y no se modifica durante la ejecución). Doce
pasos de ciclo de vida, del arranque a la consolidación
`evidencia` presente en los dos repositorios; es el documento que el Owner adjunta al chat
`aplicabilidad` universal
`solapamiento` ADS tiene `memoria` como tipo canónico y doce secciones; **no tiene ciclo de
vida ni regla de borrado**
`contradiccion` ninguna
`destino` kernel · `decision` **investigar**

**CAND-003 · Protocolo de decisión crítica frente a automática**
`origen` ambos repos · `AGENT_MEMORY_SYSTEM.md` · `lente` L1, L8
`problema` el agente paraba a preguntar lo que podía decidir, y decidía lo que debía preguntar
`mecanismo` dos listas cerradas. Automáticas: análisis técnico, código que sigue un
estándar establecido, validación contra reglas documentadas. Críticas: ambigüedad,
conflicto entre requisitos, contexto de negocio no documentado, implicaciones de seguridad,
elección entre opciones válidas con contrapartidas. Lo crítico se escribe en
`decisions_pending.md` y **se pregunta**
`evidencia` `decisions_pending.md` existe en cinco de las sesiones examinadas
`aplicabilidad` universal
`solapamiento` `a.8` fija tres niveles de intervención del Owner con criterio escrito. Esto
es la misma idea **desde el lado del agente**, y con lista cerrada
`contradiccion` ninguna
`destino` kernel · `decision` **investigar** — la lista cerrada es más operable que un criterio

**CAND-017 · Ledger de aprendizaje con confianza medida por repetición**
`origen` frontend · `.claude/project-learnings.md` · `lente` L5, L7
`problema` los mismos errores volvían cada pocas sesiones
`mecanismo` entradas `PL-NNN` que nunca se reutilizan, con fecha, fuente (qué agente o qué
corrección la disparó), categoría (`AUDIT_RULE` · `CODEBASE_PATTERN` · `ANTI_PATTERN` ·
`CORRECTION`), **confianza** (`HIGH` = encontrado en tres o más sitios o confirmado por el
Owner; `MEDIUM` = una vez), la regla, dónde se encontró y su seguimiento
`evidencia` 32 entradas
`aplicabilidad` universal
`solapamiento` **corregido en F2 (C-2):** `ORG_LEARNINGS` y `PROJECT_LEARNINGS` **sí** tienen juego completo de campos, incluida `Confianza` en tres grados, y `gate:aprendizaje-fundado` ya exige dos ocurrencias o un incidente. Lo único no cubierto es la lista vinculante de lectores
`contradiccion` ninguna
`destino` kernel · `decision` **incorporar** propuesta. El campo de confianza atado a un
recuento de apariciones convierte «lo aprendido» en algo con umbral, y `G52` ya pide una
regla de retirada que hoy no tiene señal que la dispare

**CAND-018 · Un solo escritor para la memoria, declarado en el propio fichero**
`origen` frontend · cabecera de `project-learnings.md` · `lente` L1
`mecanismo` *«This file is maintained exclusively by the system-learner agent»*, seguido de
la lista **vinculante** de los trece agentes que deben leerlo antes de trabajar
`evidencia` la lista cita agentes que existen en `.claude/agents/`
`aplicabilidad` universal
`solapamiento` `I1` y `I2` de `a.9` exigen exactamente esto: autoridad identificada y
ejecutor único de mutación
`contradiccion` ninguna. Es `I1`/`I2` implementado sin haber leído `a.9`
`destino` kernel · `decision` **incorporar** propuesta — la mitad que ADS no tiene es la
**lista de lectores obligatorios**, que hace comprobable que la memoria se usa

### El circuito GAP

**CAND-004 · El GAP como artefacto único con una sección por rol**
`origen` frontend · `.claude/gaps/_template.md` · `lente` L5, L8
`problema` el contrato de un cambio, su implementación y su auditoría vivían en tres sitios
`mecanismo` un fichero por GAP con tres zonas de escritura: **contrato** (contexto,
solución acordada, criterios de aceptación, **lista exacta de archivos** que el
implementador no puede exceder sin avisar, restricciones), **implementación** (rellena el
implementador: archivos creados y modificados, decisiones tomadas, desviaciones del plan) y
**auditoría** (rellena el auditor: veredicto, puntuación, checklist, observaciones para el
Owner, estado real del código)
`evidencia` 115 GAP cerrados
`aplicabilidad` universal
`solapamiento` es a la vez el `item`, el `paquete` y el `DICTAMEN` de ADS, en un fichero
`contradiccion` **corregido en F2 (C-3):** ninguna, ni aparente. `a.9` ya resuelve el caso
para el tablero, con zonas de autoridad distinta, canal de órdenes, evento antes de mutar y
compare-and-swap. Lo que falta es aplicarlo al paquete
`destino` kernel · `decision` **investigar** — el hallazgo fuerte es que las tres zonas
juntas hacen imposible auditar sin ver el contrato

**CAND-005 · Descubrimiento → implementación → auditoría, con roles separados**
`origen` frontend · `docs/agent-system/workflows/gap-workflow.md` · `lente` L8
`mecanismo` tres roles con prohibiciones explícitas. Descubrimiento: pregunta hasta que el
alcance esté claro y **nunca escribe código de producción**. Implementación: trabaja sólo
sobre los archivos listados. Auditoría: **no modifica código de producción**, no aprueba
criterios incumplidos, y deja los rechazados en curso con las correcciones exactas
`evidencia` 115 ciclos completos
`aplicabilidad` universal
`solapamiento` es `G13` —creación no es validación— y la estructura por defecto de la cadena
`contradiccion` ninguna
`destino` kernel · `decision` **incorporar** como confirmación empírica de `G13`
`motivo` no añade contrato: **prueba uno**. Es la primera evidencia de proyecto real de que
la separación productor/crítico se sostiene en producción

**CAND-006 · Checklist de auditoría con las prohibiciones del proyecto**
`origen` frontend · sección de auditoría del template · `lente` L4, L7
`mecanismo` nueve comprobaciones, todas cicatrices: sin `fetch()` directo, sin hardcode de
tenant, sin ficheros `.js` nuevos, sin `any` sin justificación, hooks gigantes intactos sin
permiso, `entitiesConfig.js` intacto sin permiso
`aplicabilidad` de ese proyecto
`solapamiento` es el contenido de un `gate`, no su forma
`destino` conocimiento de ese proyecto · `decision` **descartar** para el kernel.
`motivo` **la forma sí importa**: un gate cuyas comprobaciones nacen de errores ya
cometidos. Eso ya lo hace ADS al exigir infracción deliberada por prueba

**CAND-007 · Estado del GAP como directorio**
`origen` frontend · `open/` · `in-progress/` · `closed/` · `lente` L8
`mecanismo` mover el fichero es cambiar de estado. El estado se ve con `ls`
`aplicabilidad` universal · `solapamiento` `b.2` estados de paquete
`destino` kernel · `decision` **investigar** — es una disposición física candidata para
`a.9`, legible sin herramienta como pide `I4`

**CAND-008 · Registro derivado, regenerable, no editable**
`origen` frontend · `scripts/build-gaps-registry.mjs` · `lente` L2
`mecanismo` regenera `gaps-registry.md` desde el frontmatter YAML de cada GAP
`aplicabilidad` universal
`solapamiento` `I4` vistas completas derivadas · `I5` lo derivado no es editable
`contradiccion` ninguna · `destino` kernel · `decision` **incorporar** propuesta
`motivo` ADS exige vistas derivadas y no tiene ni una sola implementada fuera de sus
propios validadores

### Neutralidad de proveedor — el hallazgo mayor

**CAND-009 · Núcleo neutral con adaptadores por herramienta**
`origen` frontend · `docs/agent-system/` · `lente` L1
`problema` el mismo conocimiento reescrito para Claude, Codex, Cursor y Copilot
`mecanismo` una carpeta declarada **tool-neutral** con `rules/`, `workflows/`, `agents/`,
`commands/`, `memory/`. Cada herramienta la consume por su propio adaptador:
`.agents/skills/` para Codex, `.cursor/rules/` para Cursor, `.github/instructions/` para
Copilot, `.claude/**` para Claude Code
`evidencia` siete workflows y siete ficheros de reglas neutrales, consumidos por cuatro
adaptadores. Su README declara el principio: *«Keep tool-specific behavior in adapters»*
`aplicabilidad` universal
`solapamiento` **responde a la contradicción X3**: dónde vive un adaptador. Aquí vive junto
al proyecto, y el núcleo neutral es el que se comparte
`contradiccion` ninguna con `K0.8`: **lo cumple**, sacando la marca fuera del contenido
`destino` adaptador · `decision` **incorporar** propuesta
`motivo` es la arquitectura del apartado 9 de la directiva, construida a mano, en
producción, y con la degradación y la verificación ya resueltas — ver CAND-011 y CAND-012

**CAND-010 · Mapa explícito de qué consume cada herramienta**
`origen` frontend · `docs/agent-system/adapters.md` · `lente` L1
`mecanismo` una sección por herramienta con la lista exacta de ficheros que lee, y las
diferencias declaradas: *«These files cannot behave like Codex skills, but they expose the
same source of truth»*
`aplicabilidad` universal · `destino` adaptador · `decision` **incorporar** propuesta
`motivo` es la ficha de capacidad de un adaptador: qué lee, qué puede y qué no

**CAND-011 · Entrada mínima para la herramienta sin adaptador**
`origen` frontend · `docs/agent-system/generic-agent-quickstart.md` · `lente` L1
`aplicabilidad` universal
`solapamiento` es el 9.3 de la directiva —degradación explícita— resuelto
`destino` kernel · `decision` **incorporar** propuesta
`motivo` sin esto, «neutral» significa «no funciona en lo que no previmos»

**CAND-012 · Prueba de humo del adaptador en sesión nueva**
`origen` frontend · `docs/agent-system/smoke-tests.md` · `lente` L4
`problema` una skill añadida no aparecía hasta reiniciar la sesión, y nadie lo sabía
`mecanismo` por herramienta: la lista de skills que deben estar visibles, prompts secos que
**no deben modificar código**, y el comportamiento esperado de cada uno. Termina con una
comprobación de seguridad: `git diff --name-only | rg '^\.claude/'` debe salir vacío
`aplicabilidad` universal
`solapamiento` es el 15.2 de la directiva —la instalación debe ser verificable— resuelto
`contradiccion` ninguna
`destino` kernel · `decision` **incorporar** propuesta
`motivo` ADS tiene definición verificable de «el kernel es íntegro» y ninguna de «el agente
puede arrancar el sistema». Esto es esa prueba, y con un caso negativo real detrás

**CAND-013 · Mapa de comandos por herramienta**
`origen` frontend · `AGENTS.md` y `docs/agent-system/commands/` · `lente` L1
`mecanismo` tabla de doce filas que traduce la orden que el Owner escribe al workflow que
la ejecuta, incluyendo frases en lenguaje natural: *«crea un GAP»*, *«recuerda esto»*
`aplicabilidad` universal
`solapamiento` `b.13` órdenes en lenguaje natural
`destino` adaptador · `decision` **investigar**

**CAND-014 · Frontera de escritura entre adaptadores, con excepciones nombradas**
`origen` frontend · `AGENTS.md` y `docs/agent-system/rules/memory.md` · `lente` L1, L7
`problema` dos ecosistemas escribiendo sobre los mismos ficheros
`mecanismo` `.claude/**` es de sólo lectura para Codex, con **tres excepciones nombradas
una por una** —los GAP activos, el aparcadero de ideas y el fichero de memoria— cada una
con su motivo. La de memoria dice por qué existe: *«to avoid re-introducing the same
drift»*
`aplicabilidad` universal
`solapamiento` `I2` propiedad de escritura por zona
`destino` kernel · `decision` **incorporar** propuesta
`motivo` `I2` habla de zonas dentro de un artefacto; esto extiende la misma idea a zonas
del repositorio entre dos ejecutores, que es el caso de la concurrencia real

**CAND-015 · Precedencia declarada entre conocimiento genérico y del proyecto**
`origen` frontend · `AGENTS.md` §Rule precedence · `lente` L1
`mecanismo` *«When a generic skill conflicts with La PesquerApp-specific documentation,
follow La PesquerApp documentation»*, seguido de tres ejemplos concretos del conflicto real
—formularios, llamadas a API, reglas de interfaz—
`aplicabilidad` universal
`solapamiento` la precedencia de capas de ADS, y `P1` de la composición de packs
`contradiccion` ninguna
`destino` kernel · `decision` **incorporar** propuesta — con los ejemplos, que son lo que
hace la regla aplicable

### Calidad y evolución

**CAND-019 · Workflow de evolución con puntuación antes y después**
`origen` backend · `.claude/agents/evolution-workflow.md` · `lente` L4, L8
`problema` los bloques se daban por terminados sin criterio comparable
`mecanismo` siete pasos, de `STEP 0a` a `STEP 5`. Escala de 1 a 10 con descripción por
tramo. `STEP 1` puntúa **antes**, justificando componente a componente. `STEP 2` describe
los cambios sin código y **espera aprobación explícita del Owner**. `STEP 4` puntúa
**después** y ejecuta los tests. Un bloque no se cierra por debajo de 9, salvo bloqueo de
negocio explícito
`evidencia` 47 entradas en el log de evolución, con la tabla de bloques y su estado
`aplicabilidad` universal
`solapamiento` `rubrica` es tipo canónico en ADS, y sólo hay dos rúbricas, ambas de diseño
`contradiccion` ninguna
`destino` kernel · `decision` **investigar**
`motivo` la puntuación antes/después sobre la misma escala es una medida de avance
material, que `b.9` define formalmente y nadie ha medido nunca

**CAND-020 · El déficit declarado con su siguiente acción**
`origen` backend · `Gap to 10/10` en la plantilla del log · `lente` L8
`mecanismo` cerrar por debajo del objetivo obliga a escribir qué falta y cuál es la
siguiente acción concreta
`aplicabilidad` universal
`solapamiento` `b.3` obligaciones del proceso y obligación huérfana; `plantillas/CIERRE.md`
separa lo entregado de lo retirado
`destino` kernel · `decision` **incorporar** propuesta
`motivo` ADS impide cerrar con una obligación huérfana. Esto permite cerrar **declarando**
el hueco, que es lo que un proyecto real necesita para no bloquearse

**CAND-021 · Log de evolución con formato de entrada fijo**
`origen` backend · `docs/audits/laravel-evolution-log.md` · `lente` L5
`mecanismo` una entrada por bloque y fecha: puntuación antes y después, prioridad,
complejidad, estado, cambios, tests con cobertura, y el déficit pendiente
`evidencia` 47 entradas, 1740 líneas, mantenido durante meses
`aplicabilidad` universal
`solapamiento` el apartado 13 de la directiva —documentación estructurada de lo
aprendido— que ADS tiene **ausente**
`destino` kernel · `decision` **investigar**

### Herramientas y automatismo

**CAND-022 · Captura de pares esqueleto/cargado para revisión de fidelidad**
`origen` frontend · `.claude/tools/capture-skeleton-pair.ts` y sus tres hermanos · `lente` L2, L4
`problema` el crítico visual no podía comparar el estado de carga con el estado real
`mecanismo` Playwright headless que **retiene todas las respuestas de API** hasta capturar
el esqueleto, las libera y captura el estado cargado. Las dos imágenes salen de la misma
navegación, de modo que la estructura del DOM es comparable fotograma a fotograma. Depende
de `auth-setup.ts`, que guarda la sesión. Se ejecuta con `npx -p`, sin añadir dependencias
`evidencia` 316 líneas de herramienta, con dos agentes que la consumen
`aplicabilidad` por clase — interfaz web
`solapamiento` `DIS/RevisionDeFidelidad` y `05-FIDELIDAD` describen el procedimiento y
**no tienen herramienta**
`destino` pack `web-app` · `decision` **investigar**
`motivo` es la primera evidencia de que la revisión de fidelidad de ADS es ejecutable

**CAND-023 · Permisos del agente declarados en el repositorio**
`origen` frontend · `.claude/settings.json` · `lente` L1, L2
`mecanismo` lista de órdenes permitidas sin preguntar, y de rutas escribibles
`aplicabilidad` por proveedor · `destino` adaptador · `decision` **investigar**
`motivo` el apartado 9.2 de la directiva nombra los permisos como materia de adaptador, y
esto es un ejemplo mínimo y real

**CAND-024 · Ganchos de git con degradación declarada**
`origen` frontend · `.husky/pre-push` · `lente` L2, L7
`mecanismo` comprueba tipos y lint antes de empujar, y **se salta la comprobación con aviso
si no hay `node_modules`**, porque en entornos de nube las dependencias las gestiona otro
`evidencia` el comentario del script nombra el caso que lo provocó
`aplicabilidad` por clase
`destino` pack `web-app` · `decision` **investigar**
`motivo` la degradación explícita del 9.3 aplicada a un gancho, no a un adaptador

**CAND-027 · Skill de terceros con procedencia y hash**
`origen` frontend · `skills-lock.json` · `lente` L1
`mecanismo` por cada skill externa: origen, tipo de origen, ruta y hash calculado
`aplicabilidad` universal
`solapamiento` `K0.11` vendorizado y `kernel/.upstream-hash` hacen esto con el kernel
`destino` tooling · `decision` **investigar**
`motivo` ADS controla la integridad de lo suyo y no tiene forma de vendorizar conocimiento
ajeno con su procedencia

### Git

**CAND-025 · Rama por trabajo de agente, integración por PR**
`origen` frontend · historia de git · `lente` L3
`mecanismo` cada trabajo de agente abre su rama con prefijo del proveedor —`claude/<tema>`,
`codex/<tema>`— y entra por Pull Request. `main` no recibe empujes directos de agente
`evidencia` 67 PR · 58 ramas remotas · 48 fusionadas
`aplicabilidad` universal
`solapamiento` `G29` dice que el Owner no es operador de git y no dice quién sí
`contradiccion` ninguna
`destino` kernel · `decision` **investigar**
`motivo` es el aislamiento del apartado 8 de la directiva, resuelto con la herramienta más
simple que existe, y con doce meses de uso

### El indicio de la cuarta capa

**CAND-029 · Un sistema de trabajo propio, copiado entre repositorios de clase distinta**
`origen` ambos repos · `.ai_standards/` y `.cursor/rules/agent-memory-protocol.mdc` · `lente` L1, L7
`problema` el método de trabajo con agentes valía para los dos repositorios, y no había
dónde ponerlo salvo dentro de cada uno
`mecanismo` cinco ficheros —el sistema de memoria, el protocolo para el chat, la coletilla
que se pega al final de un prompt, la guía rápida y su índice— copiados a los dos
repositorios y referenciados desde las reglas de Cursor de ambos
`evidencia` presentes en un Next.js y en un Laravel. **Los cinco han divergido entre
copias**, y el índice del repositorio de frontend sigue titulándose *«Estándares IA –
PesquerApp Backend»*
`aplicabilidad` **por decidir**. Su contenido parece universal —memoria, decisiones,
ciclo de sesión—, y su forma de propagarse es la de conocimiento propio sin capa
`solapamiento` parte de su contenido está desglosado en CAND-002 y CAND-003 como candidato
de kernel. Lo que aquí se registra no es el contenido: es **el patrón de propagación**
`contradiccion` presiona sobre `K-1` — es la contradicción **X1**
`destino` capa por decidir (X1) · `decision` **investigar**
`motivo` es el indicio de Q1, y su límite: los dos repositorios son un producto. Que algo
se copie entre ellos demuestra que se copió. **La conclusión exige un proyecto
independiente**, y por eso este candidato no se resuelve en esta pasada

### Evidencia negativa — no se incorpora, se aprende

**CAND-016 · La memoria espejada divergió, 23 entradas contra 32**
`origen` frontend · `docs/agent-system/rules/memory.md` · `lente` L7
`qué pasó` la memoria de proyecto se copió a la carpeta neutral para que Codex la leyera.
Las dos copias divergieron —*«23 vs 32 entries, never reconciled»*— porque nada las
sincronizaba. La corrección fue **declarar una sola canónica y dejar la otra como puntero**
`por qué importa` es la regla de fuente única de ADS, verificada por su violación. Y la
violación se cometió **para** dar servicio a un segundo adaptador: el motivo por el que un
espejo parece razonable es exactamente el que lo hace fallar
`destino` no se incorpora · `decision` **descartar**
`motivo` refuerza `T147` y la regla de fuente única, y añade el corolario que faltaba: un
adaptador **apunta**, nunca copia

**CAND-028 · Las skills duplicadas también divergieron**
`origen` frontend · `.agents/skills/` frente a `.claude/skills/` · `lente` L7
`qué pasó` cuatro skills existen en ambas carpetas con el mismo nombre. **Las cuatro
difieren.** Y la skill de auditoría de GAP sigue remitiendo a la memoria espejada que
CAND-016 declaró puntero
`por qué importa` es CAND-016 otra vez, en otro material, sin que nadie lo detectara. **La
deriva entre adaptadores no es un descuido: es el comportamiento por defecto cuando no hay
un validador que la vea**
`destino` no se incorpora · `decision` **descartar** como contenido; **retener** como
requisito: un núcleo neutral con adaptadores necesita un validador de referencias, o
repetirá esto

**CAND-026 · Diez ramas abandonadas sin mecanismo que las vea**
`origen` frontend · git · `lente` L3
`qué pasó` de 58 ramas remotas, 10 no están fusionadas en `main`. Tres son trabajo de
agente; siete son ramas de corrección y funcionalidad. Nada dice si contienen trabajo vivo
`por qué importa` el 8.3 de la directiva pregunta literalmente *«¿qué trabajo quedó
abandonado sin integrar?»*. Aquí la respuesta existe y nadie la tiene
`destino` no se incorpora · `decision` **descartar** como candidato; **retener** como
requisito medible del gobierno de git

---

## Lo que esta minería NO puede responder

```text
Q1 CONCLUYENTE       los dos repositorios son un producto. Que algo se repita entre
                     ellos demuestra copia, no reutilización. Hace falta un proyecto
                     independiente — gym-wear es el candidato inmediato.

FRECUENCIA DE USO    se ha contado lo que existe y lo que se fusionó. Cuántas veces se
                     invocó realmente cada skill no está en el repositorio: viviría en
                     los historiales de sesión de cada herramienta.

QUÉ FRACASÓ          las skills retiradas no dejan rastro. El material sólo conserva lo
                     vigente, y el apartado 5.3 de la directiva pide expresamente
                     «skills que resultaron inútiles».

COSTE                no hay forma de medir desde el repositorio cuánto retrabajo evitó
                     cada mecanismo. La única señal indirecta es que los mecanismos con
                     cicatriz escrita —CAND-012, CAND-014, CAND-024— nombran el error
                     que los provocó.
```
