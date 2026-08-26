# ADS — Autonomous Development System

Estructura reutilizable para desarrollar proyectos con una organización autónoma de agentes de IA bajo gobierno humano.

Esto **no** es una plantilla de código. Es la constitución operativa de la organización que escribe el código.

## Dónde está lo que hace funcionar esto

```text
kernel/operativo/     EL CONTENIDO OPERATIVO. Quince capacidades con sus roles, métodos,
                      prompts, gates y composiciones. Es lo que un equipo ejecuta.
                      → empieza por kernel/operativo/00-INDICE.md

docs/rediseno/        LA ESPECIFICACIÓN NORMATIVA aprobada: (a) capacidades, equipos,
                      paquetes y estado · (b) recorrido, estados y composición.

packs/                web-app · mobile-app · wear-os, y cómo se componen entre sí.

kernel/KERNEL.md      la constitución en prosa de la versión 1.3.0. Sigue siendo el
                      documento de arranque mientras no exista el runtime.
```

**Si eres un agente que llega por primera vez**, el camino es:
[`kernel/operativo/00-INDICE.md`](kernel/operativo/00-INDICE.md) → tu capacidad →
tu rol → su prompt. No hace falta leer nada más.

## Las tres capas

```text
KERNEL    cómo trabaja la organización        idéntico en todos los proyectos
PACK      saber hacer de una CLASE            reusable entre proyectos del mismo tipo
PROFILE   qué se construye AQUÍ               único por proyecto
                    ↓
                AGENTS.md    ← compilado; lo que el agente lee cada sesión
```

La capa intermedia es la que hace que esto escale de verdad. Hay conocimiento que no es universal pero tampoco es de un solo proyecto: toda web app necesita presupuestos de rendimiento y estrategia de migraciones; toda app móvil necesita perfil de capacidades, política de batería y degradación por permisos. Sin los packs, eso se reescribe en cada proyecto o contamina el kernel.

## Contenido

```text
kernel/
├── KERNEL.md              constitución reusable  (1.0.0)
├── PROFILE_TEMPLATE.md    plantilla a rellenar para un proyecto nuevo
├── templates/             ledgers de aprendizaje (G52)
├── KERNEL_CHANGELOG.md
└── VERSION

packs/
├── pack-mobile-native.md  apps móviles y wearables
├── pack-web-app.md        aplicaciones web
└── pack-design-led.md     productos donde el diseño ES el diferenciador

tooling/
├── new-project.sh         crea el esqueleto de un proyecto nuevo
├── compile-agents.sh      prepara la recompilación de AGENTS.md
└── kernel-status.sh       detecta forks silenciosos del kernel

PROJECT.md                 binder: qué kernel, qué packs, qué profile
PROFILE.md                 este proyecto (gym-wear)
AGENTS.md                  compilado
docs/UPSTREAM.md           candidatos a promover a kernel o pack
```

## Empezar un proyecto nuevo

**→ Lee `START_HERE.md`.** Contiene el procedimiento completo: requisitos, rutas para proyecto nuevo / proyecto existente / prueba rápida, qué esperar en cada paso, qué decir como Owner durante el proyecto y qué hacer cuando algo va mal.

Versión corta:

```bash
./tooling/new-project.sh mi-web-app web-app
cd ../mi-web-app
# rellenar PROFILE.md (a mano o por conversación con el agente)
# pegar BOOTSTRAP_PROMPT.md en el agente principal
```

## Las tres reglas que sostienen la reutilización

**1. El kernel vendorizado no se edita.**
Cada proyecto lleva una copia congelada. Si necesitas otro comportamiento, la vía es un **override declarado** en el PROFILE, no editar la copia. `kernel-status.sh` detecta la divergencia. Un kernel editado localmente es un fork silencioso y la reutilización desaparece.

**2. Ante cada regla, preguntar de qué capa es.**
¿Sería igual de cierta en un proyecto de otra clase? → KERNEL. ¿En otro proyecto de la misma clase? → PACK. ¿Sólo aquí? → PROFILE.
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
| `kernel/KERNEL.md` | 1.3.0, conviviendo | ningún proyecto todavía |
| runtime y dispatcher | **no existen** | — |

**Nada de esto ha pasado por un proyecto real.** El estado honesto de cada prueba está en
[`kernel/operativo/pruebas/REGISTRO.md`](kernel/operativo/pruebas/REGISTRO.md): la mayoría
son contratos definidos, y sólo las estructurales están ejecutadas y superadas. La primera
versión de un kernel siempre está equivocada en algún punto; el bucle de upstream existe
precisamente para eso.
