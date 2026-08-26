# KERNEL CHANGELOG

Formato: semver (K0.11). MAJOR cambia el contrato con el PROFILE o el sentido de una regla DEBE.

## 2.0.0-alpha.2 — correcciones de la auditoría independiente

Resuelve los 33 hallazgos de una auditoría independiente, ejecutada por un lector que no
escribió el material. El informe y la matriz de resolución viven en el repositorio del
kernel, en `docs/rediseno/AUDITORIA-INDEPENDIENTE-LOCAL.md` y
`docs/rediseno/CORRECCIONES-POST-AUDITORIA.md`. **No viajan con el kernel instalado**: son
historia del kernel, no especificación que su corpus enlace.

**Normativo.** Enmienda **E1** a la sección (a), aprobada por el Owner: `ENC` es la
decimoquinta capacidad base, con su frontera con `DSP` y con materialización **bajo
demanda** — los equipos permanentemente activos siguen siendo dos.

**Lo que faltaba y ahora existe:**

- `recorrido/` — obligaciones del proceso, `gate:cierre-de-item` con las cinco condiciones
  de b.10, y los diez procesos de b.16 en forma canónica
- `DSP/supervision` — la cuarta función de DSP, que ejecuta los cuatro frenos
- `esquemas/nivel-novedad.yaml` — la escala de novedad con condiciones **formales**, que
  vuelve alcanzable el nivel N3
- `propiedades_medibles` en los packs — lo que hace computable la precedencia P1
- `validadores/huella.py` — la integridad cubre ahora a los validadores y al tooling
- `validadores/comprobar_negativos.py` — **cada prueba nueva falla cuando debe fallar**

**Lo que se corrigió y era falso:**

- el comando de arranque documentado terminaba con código 3
- un proyecto recién creado tenía once enlaces rotos: no se le enviaba la especificación
  normativa que su propio corpus enlaza
- `T131` estaba en `prueba-superada` afirmando un comportamiento que su validador no
  ejecutaba; `T134` pasaba por coincidencia de nombre de fichero
- `DIS` y `DOM` se arbitraban un veto que a.5 reserva al Owner
- `DSP/estado` **decidía** cancelaciones, que b.7 le niega
- once recuentos en prosa que ya no coinciden con nada porque **se derivan**: los comprueba
  `comprobar_recuentos.py`

**El corpus, contado desde el corpus** (`pruebas/RECUENTOS-generado.md`):

```text
15 capacidades · 42 roles · 35 métodos · 36 prompts · 29 gates
38 composiciones · 16 handoffs · 10 procesos · 18 esquemas
12 validadores · 73 escenarios de conformidad
```

## 2.0.0-alpha.1 — contenido operativo sobre la especificación aprobada

> **Las cifras de esta entrada eran incorrectas** y se corrigen aquí sin reescribir su
> historia: eran dieciséis esquemas y no diecisiete, treinta y cuatro métodos y no treinta
> y cinco, veintinueve campos de rol y no veintiocho. Fue el hallazgo A-24, y desde
> `2.0.0-alpha.2` ninguna cifra del corpus se escribe a mano.

**No es un kernel funcionando: es el contenido que el runtime consumirá.** El runtime y el
dispatcher siguen sin existir, por decisión del Owner.

Añade `kernel/operativo/`, con:

- lenguaje canónico de doble lectura y diecisiete esquemas
- quince capacidades con ficha de doce campos, gate propio y contrato de veto donde procede
- 41 roles con los 28 campos del contrato común, y sus prompts operativos
- 35 métodos ejecutables, todos con condición de salida por paso y prueba de reanudación
- los cinco contratos transversales C1 a C5
- el sistema de excelencia de Diseño: dos gates independientes, dos rúbricas, memoria de
  doce secciones, escala de novedad y procedimiento de fidelidad
- el circuito completo de la puerta de entrada, con catorce formas de conversación
- tres validadores ejecutables y 61 escenarios de conformidad con su estado REAL

Deroga: `pack-design-led` como pack — la excelencia visual pasa al kernel.
Retira a `packs/legacy-1.3.0/` los tres packs de la versión anterior.

Las secciones (a) y (b) aprobadas NO se han modificado. Las contradicciones encontradas
están registradas en `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`.

## 1.3.0 — 2026-08-24

MINOR: nueva regla compatible. **Adopción recomendada para cualquier proyecto con un diferenciador cualitativo.**

- **G53 — Ejes de prioridad: riesgo y valor diferencial.** El kernel graduaba el proceso
  sólo por riesgo (G34), con una consecuencia grave: los cambios visuales, de interacción
  y de redacción son casi siempre de bajo riesgo, así que un sistema gobernado sólo por
  riesgo los trata como Quick Change, les da validación mínima y los resuelve por el
  camino más barato que exige G24. Si el diferenciador del producto es el diseño, la
  organización optimiza con precisión hacia la mediocridad.
- Nuevo campo obligatorio del contrato K0: `premium_areas` (1-3 máximo; más requiere
  justificación explícita del Owner, porque si todo es premium nada lo es).
- **G24 se invierte dentro de las áreas premium**: modelo más capaz, techo de iteraciones
  alto, y "la calidad más alta alcanzable" en lugar de "la combinación más sencilla".
- **Prohibido Quick Change dentro de un área premium**, por bajo que sea su riesgo técnico.
- Iteración obligatoria (≥2 direcciones) y evidencia visible como criterio de validación.
- Prioridad alta en la cola de aceptación humana (G36): la organización puede verificar
  que algo funciona, no que algo es bueno cuando "bueno" es el diferenciador.
- Contrapartida obligatoria: fuera de las áreas premium se busca lo suficientemente
  bueno y barato.

Pack nuevo publicado en paralelo: **`pack-design-led` 1.0.0** — para productos cuya razón
de existir es cómo se sienten al usarlos. Referencias analizadas en vez de aspiración
vaga, criterios comprobables, sistema de movimiento, listón de rechazo, regresión visual,
enrutamiento de modelo y orden de construcción.

## 1.2.0 — 2026-08-24

MINOR: nueva capacidad y nuevo mecanismo, compatibles. Adopción recomendada.

- **G52 — Aprendizaje del sistema: los dos ledgers.** El kernel registraba decisiones,
  estado, investigación y métricas, pero no lo más volátil y valioso: **qué ha funcionado
  y qué no**. Ahora hay dos ledgers con sujetos separados:
  `docs/agentic/ORG_LEARNINGS.md` (cómo trabajamos, dueño Agentic Engineering) y
  `docs/PROJECT_LEARNINGS.md` (qué construimos, dueño Evidence & Learning).
- **Nueva capacidad `Evidence & Learning`** en G11. No es plantilla permanente: se activa
  en momentos definidos. Su criterio de éxito no es el número de entradas, sino que una
  decisión no repita un error ya registrado.
- **Recuperación obligatoria**: consultar el ledger, y dejar constancia, antes de un ADR,
  una decisión Significant, trabajo en un módulo con entradas vigentes, un Owner Decision,
  un cambio de dirección (G51) o un spike sobre algo ya investigado.
- **Escalera de promoción** que enlaza con K0.12: observación → patrón → regla local →
  PACK → KERNEL. Una regla vale más que cien aprendizajes.
- **Anti-hinchazón**: techo de entradas vigentes, archivo de promovidas y superadas,
  retirada de anécdotas que no reaparecen.
- **Revisión de plantilla y regla de retirada** (refuerza G14/G25): toda auditoría DEBE
  proponer al menos un elemento a retirar o fusionar. Sin ella la organización sólo crece.
- G22: los dos ledgers pasan a ser entregable del gate del Circuito 0.
- G25: la retro de tarea incorpora una línea de aprendizaje (0 o 1, cero es legítimo).
- Plantillas incorporadas en `kernel/templates/`.

## 1.1.0 — 2026-08-24

MINOR: nueva regla compatible. Adopción recomendada.

- **G51 — Cambio de dirección: reabrir una decisión ya tomada.** El kernel 1.0.0 cubría
  cómo se toman, registran y revalidan decisiones, pero no el caso más frecuente en la
  práctica: el Owner ve el producto funcionando y quiere otra cosa. Ahora es un flujo de
  primera clase, con identificación de la decisión, radio de impacto, opciones con coste,
  desacuerdo explícito permitido, y **regla anti-deriva** obligatoria.
- G10 reconoce explícitamente la intención de cambio de dirección.
- G41: un ADR puede ser superado en cualquier momento; el antiguo se marca `Superseded by`.
- `BOOTSTRAP_PROMPT.md` y `PROJECT_TEMPLATE.md` incorporados al kernel.

Packs actualizados en paralelo (no forman parte del versionado del kernel):
`pack-web-app` 1.1.0 (W13 — sistema de diseño y resistencia al cambio),
`pack-mobile-native` 1.1.0 (M14 — equivalente).

## 1.0.0 — 2026-08-24

Primera versión extraída del MASTER v10 del proyecto `gym-wear`.

- Separación física en tres capas: KERNEL / PACK / PROFILE (K-1).
- Contrato KERNEL↔PROFILE con 10 apartados obligatorios (K0).
- Regla de pertenencia por capa y test de contaminación (K0.10).
- Versionado semántico y vendorización; prohibición de editar el kernel local (K0.11).
- Bucle de upstream con `docs/UPSTREAM.md` y reglas de promoción (K0.12).
- Definición de éxito del Owner obligatoria en todo PROFILE (K0.13).
- Procedimiento de arranque de proyecto nuevo (K0.14).
- Política de spikes generalizada: "entorno real de ejecución" en lugar de "hardware" (G22).
- Packs iniciales publicados aparte: `pack-mobile-native` 1.0.0, `pack-web-app` 1.0.0.

### Candidatos pendientes de promoción

Ninguno todavía. El bucle K0.12 se activa al cerrar el primer circuito de `gym-wear`.
