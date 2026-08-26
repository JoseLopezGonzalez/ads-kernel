# ADS — Autonomous Development System

Estructura reutilizable para desarrollar proyectos con una organización autónoma de agentes de IA bajo gobierno humano.

Esto **no** es una plantilla de código. Es la constitución operativa de la organización que escribe el código.

## Dónde está lo que hace funcionar esto

```text
kernel/operativo/     EL CONTENIDO OPERATIVO. Quince capacidades con sus roles, métodos,
                      prompts, gates y composiciones. Es lo que un equipo ejecuta.
                      → empieza por kernel/operativo/00-INDICE.md

docs/rediseno/        LA ESPECIFICACIÓN NORMATIVA aprobada: (a) capacidades, equipos,
                      paquetes y estado · (b) recorrido, estados y composición · y sus
                      enmiendas E1 y E2.

packs/                web-app · mobile-app · wear-os, y cómo se componen entre sí.

kernel/KERNEL.md      la constitución en prosa de la línea 1.4. Sigue siendo el
                      documento de arranque mientras no exista el runtime.
```

**Si eres un agente que llega por primera vez**, el camino es:
[`kernel/operativo/00-INDICE.md`](kernel/operativo/00-INDICE.md) → tu capacidad →
tu rol → su prompt. No hace falta leer nada más.

## Un producto no es un repositorio

Un ADS Project gobierna un **producto**, y el producto puede estar repartido entre varios
repositorios Git independientes:

```text
mi-producto/                el WORKSPACE. NO es un repositorio Git.
├── ads/                    el repositorio de CONTROL: kernel, packs, PROFILE, estado,
│   └── SOURCES.toml        items, decisiones, contratos... y la composición del producto
├── frontend/               una FUENTE. Su Git, su CI, su despliegue, independientes.
└── backend/                otra FUENTE.
```

El código **no** vive en el repositorio de ADS, y ADS **no** se copia dentro de los
repositorios de código. Un producto de un solo repositorio es el caso particular de tener
una sola fuente, no un modelo distinto. Contrato:
[`C6`](kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md) · gobierno Git:
[`C7`](kernel/operativo/contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md).

## Las tres capas

```text
KERNEL    cómo trabaja la organización        idéntico en todos los proyectos
PACK      saber hacer de una CLASE            reusable entre proyectos del mismo tipo
PROFILE   qué se construye AQUÍ               único por PRODUCTO, nunca por repositorio
                    ↓
                AGENTS.md    ← compilado; lo que el agente lee cada sesión
```

La capa intermedia es la que hace que esto escale de verdad. Hay conocimiento que no es universal pero tampoco es de un solo proyecto: toda web app necesita presupuestos de rendimiento y estrategia de migraciones; toda app móvil necesita perfil de capacidades, política de batería y degradación por permisos. Sin los packs, eso se reescribe en cada proyecto o contamina el kernel.

## Contenido

| | qué es |
|---|---|
| [`kernel/operativo/`](kernel/operativo/00-INDICE.md) | **el contenido operativo**: quince capacidades con sus roles, métodos, prompts, gates, circuitos y validadores |
| [`kernel/KERNEL.md`](kernel/KERNEL.md) | la constitución en prosa de la línea 1.4, que sigue arrancando proyectos mientras el runtime no exista |
| [`kernel/PROFILE_TEMPLATE.md`](kernel/PROFILE_TEMPLATE.md) | plantilla del PROFILE, a rellenar para un proyecto nuevo |
| [`kernel/PROJECT_TEMPLATE.md`](kernel/PROJECT_TEMPLATE.md) | plantilla del binder: qué kernel, qué packs, qué overrides |
| [`kernel/BOOTSTRAP_PROMPT.md`](kernel/BOOTSTRAP_PROMPT.md) | el texto que se pega en el agente principal para arrancar |
| [`kernel/templates/`](kernel/templates/) | [ledgers de aprendizaje](kernel/templates/ORG_LEARNINGS.md) (G52) y un [AGENTS.md de ejemplo](kernel/templates/AGENTS_EXAMPLE.md) |
| [`kernel/VERSIONES.md`](kernel/VERSIONES.md) | **la política de versiones**: cuatro cosas distintas se versionan aquí y no se mezclan |
| [`kernel/KERNEL_CHANGELOG.md`](kernel/KERNEL_CHANGELOG.md) · [`kernel/VERSION`](kernel/VERSION) | la versión del release y su historia |
| [`packs/`](packs/00-QUE-ES-UN-PACK.md) | `web-app` · `mobile-app` · `wear-os`, y [cómo se componen](packs/COMPOSICION.md) |
| [`docs/rediseno/`](docs/rediseno/README.md) | la especificación normativa (a) y (b), sus enmiendas, y las auditorías |
| [`docs/evolucion/`](docs/evolucion/00-INDICE.md) | **ADS NEXT**: la directiva del Owner para la siguiente evolución, el baseline comprobado del sistema y el plan de investigación que precede a cualquier arquitectura nueva |
| `tooling/` | `new-project.sh` crea el ADS Project · `workspace.py` comprueba y materializa las fuentes · `kernel-status.sh` detecta forks silenciosos · `compile-agents.sh` prepara la recompilación de AGENTS.md |

Un proyecto creado con `new-project.sh` recibe además `SOURCES.toml` (la composición del
producto, que arranca vacía), `PROJECT.md` (binder), `PROFILE.md` (qué se construye aquí),
`docs/UPSTREAM.md` (candidatos a promover) y una copia congelada del kernel, de los packs
pedidos y de la especificación normativa.

## Empezar un proyecto nuevo

**→ Lee `START_HERE.md`.** Contiene el procedimiento completo: requisitos, rutas para proyecto nuevo / proyecto existente / prueba rápida, qué esperar en cada paso, qué decir como Owner durante el proyecto y qué hacer cuando algo va mal.

Versión corta:

```bash
./tooling/new-project.sh mi-producto web-app
cd ../mi-producto/ads
# declarar los repositorios de código en SOURCES.toml, si ya existen
python3 tooling/workspace.py check && python3 tooling/workspace.py init
# rellenar PROFILE.md (a mano o por conversación con el agente)
# pegar BOOTSTRAP_PROMPT.md en el agente principal
```

## Las tres reglas que sostienen la reutilización

**1. El kernel vendorizado no se edita.**
Cada proyecto lleva una copia congelada. Si necesitas otro comportamiento, la vía es un **override declarado** en el PROFILE, no editar la copia. `kernel-status.sh` detecta la divergencia sobre `kernel/`, `packs/` y `tooling/`, e incluye **los validadores en Python**: sin ellos, editar `ads_lint.py` para relajar una regla sería un fork invisible. Lo que entra en la huella se ve con `python3 kernel/operativo/validadores/huella.py --listar`, y que la detección funcione lo comprueba la prueba T150 con tres infracciones deliberadas.

**2. Ante cada regla, preguntar de qué capa es.**
¿Sería igual de cierta en un proyecto de otra clase? → KERNEL. ¿En otro proyecto de la misma clase? → PACK. ¿Sólo aquí? → PROFILE. Y las tres viven **una sola vez**, en el repositorio de control: nunca copiadas dentro de un repositorio de código.
Test de contaminación: si al sustituir mentalmente el proyecto por *"una CLI de facturación en Rust"* una regla del kernel deja de tener sentido, está en la capa equivocada.

**3. Lo que se aprende vuelve arriba.**
`docs/UPSTREAM.md` acumula candidatos. Una regla que el Owner ha tenido que repetir en dos proyectos distintos es candidata automática. Se promueve al kernel cuando ha demostrado valor en dos proyectos, o al pack si sólo vale para su clase.

> **Un kernel que nunca cambia no es estable: está abandonado. Un kernel que cambia con cada proyecto no es reusable: es un fork.**

## Estado actual

| Artefacto | Estado | Validado en |
|---|---|---|
| secciones (a) y (b) | **aprobadas** por el Owner | especificación, no runtime |
| `kernel/operativo/` | contenido operativo construido | ningún proyecto todavía |
| `packs/web-app` · `mobile-app` · `wear-os` | 1.0.0 | ningún proyecto todavía |
| `kernel/KERNEL.md` | 1.4.0, conviviendo con la línea 2.0 por [política declarada](kernel/VERSIONES.md) | ningún proyecto todavía |
| runtime y dispatcher | **no existen** | — |

**Nada de esto ha pasado por un proyecto real.** El estado honesto de cada prueba está en
[`kernel/operativo/pruebas/REGISTRO.md`](kernel/operativo/pruebas/REGISTRO.md): la mayoría
son contratos definidos, y sólo las estructurales están ejecutadas y superadas. La primera
versión de un kernel siempre está equivocada en algún punto; el bucle de upstream existe
precisamente para eso.

Lo que sí ha pasado es una **auditoría independiente**, ejecutada por un lector que no
escribió el material: [`AUDITORIA-INDEPENDIENTE-LOCAL.md`](docs/rediseno/AUDITORIA-INDEPENDIENTE-LOCAL.md),
33 hallazgos, y sus [correcciones](docs/rediseno/CORRECCIONES-POST-AUDITORIA.md). Dos de
las once pruebas que entonces figuraban como superadas **no comprobaban lo que su nombre
afirmaba**. Por eso cada prueba nueva lleva ahora su infracción deliberada: un validador
que sólo se ha visto pasar no está verificado.
