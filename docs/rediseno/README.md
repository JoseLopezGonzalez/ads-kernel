# Rediseño del kernel ADS — de constitución interpretable a sistema operativo

Trabajo fundacional en curso. **Nada de `kernel/` ni `packs/` se ha modificado
todavía**: hasta que las secciones estén aprobadas, aquí sólo hay propuesta.

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

## El mínimo operable está cerrado

Con (a) y (b) aprobadas, el kernel tiene lo necesario para **usarse**. El siguiente
trabajo **no** es seguir diseñando (c) a (i) en abstracto: es **probar este mínimo en un
proyecto real** —gym-wear o PesquerApp— y desarrollar las piezas siguientes como **items
`SIS` surgidos de esa utilización**.

Es la aplicación a nosotros mismos del freno de racha SIS (a.7): seguir construyendo el
kernel entero antes de usarlo es exactamente el modo de fallo (b) —autorreferencia sin
producto— que el propio kernel existe para frenar.

Conformidad acumulada: **T01-T24** de (a) · **T26-T74** de (b) · `T25` abierta hasta (g).

## Regla de proceso

Una sección cada vez, con aprobación explícita del Owner antes de pasar a la
siguiente. Sin timebox: es trabajo fundacional, no un circuito de producto.

**Al cerrar la sección (b)**, el kernel tiene lo mínimo operable. A partir de ahí el
trabajo vuelve a los proyectos reales y las secciones (c) en adelante se diseñan como
items SIS normales dentro de un proyecto, no como bloque previo a arrancar nada.
