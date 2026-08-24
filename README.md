# ADS — Autonomous Development System

Estructura reutilizable para desarrollar proyectos con una organización autónoma de agentes de IA bajo gobierno humano.

Esto **no** es una plantilla de código. Es la constitución operativa de la organización que escribe el código.

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
./tooling/new-project.sh mi-web-app pack-web-app,pack-design-led
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

| Artefacto | Versión | Validado en |
|---|---|---|
| kernel | 1.3.0 | ningún proyecto todavía |
| pack-mobile-native | 1.1.0 | ningún proyecto todavía |
| pack-web-app | 1.1.0 | ningún proyecto todavía |
| pack-design-led | 1.0.0 | ningún proyecto todavía |

Ninguna de estas piezas ha pasado aún por un proyecto real. La primera versión de un kernel siempre está equivocada en algún punto; el bucle de upstream existe precisamente para eso. Tras el primer circuito de `gym-wear` habrá candidatos reales que promover.
