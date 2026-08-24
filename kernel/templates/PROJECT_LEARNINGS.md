# PROJECT LEARNINGS

Qué funciona y qué no **en el producto y su ingeniería**, según el uso real.
Dueño: capacidad **Evidence & Learning** (G52).

> No es un registro de actividad (→ `JOURNAL.md`), ni de decisiones (→ `decisions/`), ni de investigación (→ `research/`), ni un backlog. Aquí sólo va lo que **cambia el criterio** para la próxima vez.

**Techo de entradas vigentes: 40.** Al superarlo, curación obligatoria antes de añadir más (G52).

**Antes de abrir un ADR, tomar una decisión Significant o empezar en un módulo con entradas vigentes: consultar este fichero y dejar constancia.** Si no hay nada relevante, decirlo explícitamente.

---

## Vigentes

<!--
LRN-000 · [categoría]
Observación:   qué pasó, una frase
Evidencia:     dónde, cuándo, cómo lo sabemos
Confianza:     anécdota | patrón | medido
Implicación:   qué hacer o no hacer la próxima vez
Afecta a:      ADR-00X · módulo · decisión abierta · supuesto del PROFILE
Estado:        vigente
-->

*(vacío — las primeras entradas llegarán del primer Plan de Validación y de los spikes)*

---

## Ejemplos de lo que SÍ va aquí

Ilustrativos, para calibrar. Bórralos cuando haya entradas reales.

```text
LRN-001 · [producto]
Observación:   Confirmar reps con dos toques rompe el ritmo entre series.
Evidencia:     Plan de Validación VP-003, sesión del 12/09, 4 ejercicios de 6.
Confianza:     patrón (2ª vez, ya apareció en VP-001)
Implicación:   Toda interacción durante la serie tiene presupuesto de 1 toque.
               Si necesita dos, se rediseña o se automatiza.
Afecta a:      P04.2 · módulo app-wear/set-flow
Estado:        vigente
```

```text
LRN-002 · [arquitectura]
Observación:   Reconstruir el estado desde el log tarda demasiado si no hay snapshot.
Evidencia:     SPIKE-04, medición en dispositivo real.
Confianza:     medido
Implicación:   Snapshot cada N eventos. No confiar en reproducción completa.
Afecta a:      P16 · ADR-004
Estado:        promovido a ADR-006
```

```text
LRN-003 · [proceso]
Observación:   Probamos generar el catálogo de ejercicios con LLM y salió inconsistente
               en equipamiento y grupos musculares; costó más revisarlo que escribirlo.
Evidencia:     TASK-058, descartado.
Confianza:     anécdota
Implicación:   No reintentar sin un esquema de validación previo. Si alguien lo propone
               de nuevo dentro de seis meses, que lea esto antes.
Afecta a:      P09
Estado:        vigente
```

**El tercero es el tipo de entrada que más se pierde y más valor tiene:** lo que se intentó y no funcionó. Sin él, dentro de medio año alguien lo reintenta con entusiasmo.

## Ejemplos de lo que NO va aquí

| No es aprendizaje | Es | Dónde va |
|---|---|---|
| "El botón de guardar estaba mal alineado" | un bug | se arregla |
| "Decidimos usar ULID" | una decisión | ADR |
| "Hoy terminé el módulo de sync" | actividad | JOURNAL |
| "Habría que refactorizar el detector" | trabajo pendiente | tarea |
| "El login va lento" | síntoma sin implicación | investigar, y **luego** registrar la implicación |

---

## Archivo

Entradas `promovido` y `superado`. **No se consultan**; se conservan por trazabilidad.

*(vacío)*
