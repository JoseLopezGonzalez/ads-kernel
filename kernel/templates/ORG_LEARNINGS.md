# ORG LEARNINGS

Qué funciona y qué no **en la forma de trabajar de la organización**: equipo, agentes, skills, recursos, instrucciones, enrutamiento, workflows.
Dueño: capacidad **Agentic Engineering** (G14, G25, G52).

**Techo de entradas vigentes: 30.** Al superarlo, curación obligatoria.

---

## Vigentes

<!--
ORG-000 · [plantilla | skills | contexto | instrucciones | enrutamiento | workflow | coste]
Observación:   qué pasó
Evidencia:     tarea, métrica o auditoría que lo respalda
Confianza:     anécdota | patrón | medido
Implicación:   qué cambiar en la organización
Acción:        regla en AGENTS.md · nuevo skill · retirar X · cambiar enrutamiento · ninguna todavía
Estado:        vigente | promovido | superado
-->

*(vacío)*

---

## Revisión de plantilla

Se rellena en cada auditoría de cierre de circuito (G25 + G52). **Obligatorio proponer al menos una retirada o fusión.**

```text
AUDITORÍA — circuito X — fecha

Capacidades con trabajo real:        ...
Capacidades sin trabajo:             ...   → retirar o fusionar
Trabajo sin dueño claro:             ...   → capacidad que falta
Skills usadas:                       ...
Skills nunca usadas:                 ...   → retirar
Hecho a mano ≥3 veces:               ...   → skill o script que falta (G16)
Instrucciones con retrabajo:         ...   → corregir en AGENTS.md
Enrutamiento de modelo inadecuado:   ...

RETIRADA PROPUESTA (obligatoria):    ...
Cambios que requieren Owner:         ...   (permisos, coste, límites de autoridad)
```

> Sin la regla de retirada, las organizaciones sólo crecen — y una organización que sólo crece acaba gastando su presupuesto en coordinarse consigo misma (G24).

---

## Ejemplos de calibración

```text
ORG-001 · [instrucciones]
Observación:   El Owner ha corregido tres veces el mismo criterio de formato de commits.
Evidencia:     METRICS.md — "veces que el Owner corrige lo mismo": 3
Confianza:     patrón
Implicación:   No es un problema de agente, es una regla que falta.
Acción:        regla añadida a AGENTS.md §8 → candidata a CONVENTIONS.md
Estado:        promovido
```

```text
ORG-002 · [plantilla]
Observación:   La capacidad Security/Privacy no ha tenido trabajo real en dos circuitos,
               pero los checks de secretos en CI sí se han usado.
Evidencia:     auditoría circuito 2
Confianza:     medido
Implicación:   La capacidad no hace falta como tal todavía; sus reglas sí.
Acción:        fusionar en Review/Assurance; reactivar si aparece backend o publicación.
Estado:        vigente
```

```text
ORG-003 · [coste]
Observación:   Los bucles de revisión en tareas de documentación consumen tres vueltas
               de media sin cambiar el resultado tras la segunda.
Evidencia:     METRICS.md, 6 tareas
Confianza:     medido
Implicación:   Máximo 2 vueltas en revisión de documentación (G24.3).
Acción:        regla en AGENTS.md
Estado:        promovido
```

---

## Archivo

*(vacío)*
