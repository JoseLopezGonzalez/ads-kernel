# CHECKPOINT — construcción del kernel operativo

> Registro persistente de esta iniciativa. **Se actualiza antes de cada commit**, no al
> final. Basta decir «Continúa» en un chat nuevo: la siguiente acción exacta está abajo.

```text
iniciativa   contenido operativo del kernel 2.0 — pasos 1 a 6
rama         claude/kernel-operativo-equipos-roles-s4dzfq
base         (a) y (b) APROBADAS · no se modifican
alcance      contratos, esquemas, plantillas, roles, prompts, métodos, circuitos,
             criterios, checkpoints, gates, validadores, pruebas y packs
fuera        runtime · dispatcher · gym-wear · pack ERP · secciones (c)-(i) abstractas
```

## Bloque actual

```text
BLOQUE 0   esquemas, validadores e índice          TERMINADO
BLOQUE 1   circuito Owner → item (paso 1)          NO INICIADO
BLOQUE 2   contrato equipo/rol/agente/método       NO INICIADO
BLOQUE 3   sistema de excelencia de Diseño         NO INICIADO
BLOQUE 4   equipo de Diseño materializado          NO INICIADO
BLOQUE 5   demás capacidades                       NO INICIADO
BLOQUE 6   packs web-app · mobile-app · wear-os    NO INICIADO
```

## Terminado

- Lenguaje canónico y sus diecisiete esquemas — `kernel/operativo/esquemas/`
- Validador estructural `ads_lint.py` y sus reglas — **ejecutado, en verde**
- Generador determinista del registro de pruebas — `registro_pruebas.py`
- Índice y regla de fuente única — `kernel/operativo/00-INDICE.md`
- Registro honesto de estado de pruebas — `kernel/operativo/pruebas/REGISTRO.md`
- Decisiones, decisiones del Owner y contradicciones — `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`
- Packs 1.3.0 retirados a `packs/legacy-1.3.0/` con su carta de retirada

## En revisión

Nada. El bloque 0 no tiene revisión adversarial propia: se revisa al usarlo en el bloque 1.

## Decisiones pendientes del Owner

Agrupadas en `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` §2 — **ninguna bloquea**.
La única con contenido normativo es **C1** (¿`ENC` es capacidad propia o función de `DSP`?).

## Pruebas

```text
T01-T74   contrato-definido, salvo tres parciales en validador-implementado
T75+      ninguna todavía
```

## Siguiente acción exacta

> Escribir `kernel/operativo/entrada/01-TAXONOMIA.md` con los nueve bloques `ads:entrada`
> del paso 1.1 (expresión original, interpretación, observación, nota, idea inmadura,
> candidato a trabajo, orden sobre item existente, decisión, item formal), y a
> continuación la ficha `ads:capacidad` de `ENC`.
