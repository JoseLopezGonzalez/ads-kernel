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
BLOQUE 1   circuito Owner → item (paso 1)          TERMINADO, pendiente revisión
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

**Bloque 1 — paso 1 completo**

- Taxonomía de nueve clases de entrada — `entrada/01-TAXONOMIA.md`
- Circuito de catorce estaciones con sus caminos de vuelta — `entrada/02-CIRCUITO.md`
- Catorce formas de conversación, con árbol de decisión ordenado — `entrada/03-FORMAS.md`
- Escala de incertidumbre, tabla de confirmación, umbral y margen de anclaje
- Seis escenarios completos, incluido el de referencia — `entrada/05-ESCENARIOS.md`
- Capacidad `ENC` con tres roles, seis métodos, tres prompts y tres composiciones
- Política de agentes y modelos, neutral de proveedor, con 21 perfiles — `contratos/C2`
- Plantilla de encuadre rellenable — `plantillas/ENCUADRE.md`
- T75–T85 definidas

## En revisión

Bloque 1 — revisión adversarial independiente pendiente de lanzar.

## Decisiones pendientes del Owner

Agrupadas en `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` §2 — **ninguna bloquea**.
La única con contenido normativo es **C1** (¿`ENC` es capacidad propia o función de `DSP`?).

## Pruebas

```text
T01-T74   contrato-definido, salvo tres parciales en validador-implementado
T75-T85   contrato-definido (11). Ninguna ejecutada: seis exigen juicio humano o
          guion manual sobre un proyecto real, y una exige runtime.
ads_lint  EJECUTADO y en verde sobre 74 bloques canónicos
```

## Siguiente acción exacta

> Escribir `kernel/operativo/contratos/C1-EQUIPO-ROL-AGENTE-METODO.md` (paso 2.1),
> `C3-METODO-EJECUTABLE.md` (paso 2.3) y `C4-MATERIALIZACION.md` (paso 2.4). `C2`
> —agentes y modelos— ya está escrito.
