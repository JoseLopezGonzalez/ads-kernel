# Rediseño del kernel ADS — de constitución interpretable a sistema operativo

Trabajo fundacional. Las secciones **(a)** y **(b)** están aprobadas, y sobre ellas se ha
construido el contenido operativo de [`kernel/operativo/`](../../kernel/operativo/00-INDICE.md).
Lo que aquí vive es la **especificación normativa** y su historia: qué se aprobó, qué se
enmendó después y con qué autoridad.

## Principio gobernante

Un work item no se aprueba o rechaza en una pasada: **se fabrica**. Atraviesa
capacidades especializadas y cada una **añade su capa de valor**, no valida.
Implementación es casi la última parada. Lo aprendido del uso real **reentra** por el
principio del ciclo. **Calidad sólida, profesional y autónoma es la disposición por
defecto**, no "la combinación más barata que mantenga la calidad necesaria".

## Estado de las secciones

| | sección | estado |
|---|---|---|
| — | [Mapa del kernel 1.3.0 frente al principio gobernante](00-MAPA.md) | entregado |
| a | [Capacidades, equipos, paquetes y estado](a-CAPACIDADES-APROBADA.md) | **APROBADA** 2026-08-25 |
| b | [Recorrido, estados y composición de procesos](b-RECORRIDO-APROBADA.md) | **APROBADA** 2026-08-25 |
| E1 | [Enmienda a (a): `ENC` como decimoquinta capacidad base](a-ENMIENDA-E1-ENC.md) | **APROBADA** 2026-08-26 |
| c | Formato del handoff entre capacidades | no iniciada |
| d | Puntos de interacción con el Owner | no iniciada |
| e | La pregunta de la vía rápida | no iniciada |
| f | Diseño como área diferencial y tensión de presupuesto | no iniciada |
| g | Sistema operativo persistente: memoria, eventos, dispatcher, "Continúa" | no iniciada |
| h | Qué pasa con G24, G34, G53 y el resto de reglas en conflicto | no iniciada |
| i | Impacto en packs y PROFILE_TEMPLATE | no iniciada |

Versiones rechazadas conservadas para trazabilidad:
[v1](a-EQUIPOS-v1-RECHAZADA.md) · [v2](a-EQUIPOS-v2-RECHAZADA.md) · [v3](a-EQUIPOS-v3-SUPERADA.md).

Pendientes que (a) dejó abiertos y (b) cierra: lista formal de estados, transiciones,
recorrido y composición de procesos. **Siguen abiertos por diseño**: disposición física
del estado, atomicidad multiarchivo, event log y `T25` → (g).

## Qué existe y qué no

**Existe una especificación mínima aprobada para construir el kernel. No existe todavía
un kernel.**

```text
SÍ existe    (a) y (b) aprobadas: catálogo de capacidades, custodia, concurrencia,
             frenos, recorrido, estados, transiciones y composición de procesos
NO existe    runtime · dispatcher · estado persistido · tableros · checkpoints
             kernel/ y packs/ siguen INTACTOS en la versión 1.3.0
```

`T01-T24` y `T26-T74` son **contratos de conformidad definidos**, no pruebas ejecutadas.
Ninguna ha corrido nunca, porque no hay nada contra lo que correrlas. `T25` queda además
explícitamente abierta hasta (g). **Nada de esto autoriza a afirmar que el sistema
funciona.** Eso requerirá runtime y evidencia ejecutable.

## Estado de la construcción del kernel operativo

Sobre (a) y (b) aprobadas se ha construido el **contenido operativo** que el runtime
consumirá: [`kernel/operativo/`](../../kernel/operativo/00-INDICE.md).

| | |
|---|---|
| registro reanudable de la iniciativa | [`CHECKPOINT-OPERATIVO.md`](CHECKPOINT-OPERATIVO.md) |
| decisiones, decisiones del Owner y contradicciones | [`DECISIONES-Y-CONTRADICCIONES.md`](DECISIONES-Y-CONTRADICCIONES.md) |
| revisión adversarial del propio equipo, con su límite declarado | [`REVISION-ADVERSARIAL.md`](REVISION-ADVERSARIAL.md) |
| **auditoría independiente** — 33 hallazgos sobre el corpus integrado | [`AUDITORIA-INDEPENDIENTE-LOCAL.md`](AUDITORIA-INDEPENDIENTE-LOCAL.md) |
| **correcciones** derivadas de esa auditoría, con su matriz | [`CORRECCIONES-POST-AUDITORIA.md`](CORRECCIONES-POST-AUDITORIA.md) |
| estado real de cada prueba | [`pruebas/REGISTRO.md`](../../kernel/operativo/pruebas/REGISTRO.md) |

**Sigue sin existir un runtime.** Lo construido es lo que ese runtime ejecutará.

## Siguiente trabajo

**No** es seguir diseñando (c) a (i) en abstracto. Es **usar esta especificación en un
proyecto real** —gym-wear o PesquerApp— y desarrollar las piezas siguientes como **items
`SIS` surgidos de esa utilización**.

Es la aplicación a nosotros mismos del freno de racha SIS (a.7): seguir especificando el
kernel entero antes de construir nada es exactamente el modo de fallo (b) —autorreferencia
sin producto— que la propia especificación existe para frenar.

## Regla de proceso

Una sección cada vez, con aprobación explícita del Owner antes de pasar a la
siguiente. Sin timebox: es trabajo fundacional, no un circuito de producto.

**Al cerrar la sección (b)** queda una especificación mínima aprobada, no un kernel
funcionando. A partir de ahí el trabajo vuelve a los proyectos reales y las secciones (c)
en adelante se diseñan como items SIS normales dentro de un proyecto, no como bloque
previo a arrancar nada.
