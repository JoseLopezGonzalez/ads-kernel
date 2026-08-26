<!-- EJEMPLO DE REFERENCIA — NO es el AGENTS.md de este proyecto.
     Pertenece a gym-wear (Android + Wear OS, design-led). Úsalo como muestra de FORMA
     y densidad al compilar el tuyo (K0.2), nunca de contenido. -->

# AGENTS.md

Instrucciones operativas del proyecto. **Este es el documento que cargas en cada sesión.**
No leas `PROJECT_MASTER.md` completo salvo en bootstrap, ante contradicción o al revisar visión.

Compilado desde MASTER v10. Si algo aquí contradice al MASTER, es un defecto: corrígelo y avisa.

---

## 1. Qué construimos

App nativa **Android + Wear OS** para entrenamiento de fuerza en gimnasio.

- El **reloj** es la herramienta durante el entrenamiento. El **móvil** sirve para preparar, organizar y analizar.
- **Debe ser útil sin IA, sin backend, sin Internet y sin el teléfono cerca.**
- Éxito = el Owner la usa de verdad cada semana. No = tiene muchas funciones.
- El dataset será **n=1**. No planifiques como si fuera a generalizar.

Stack: Kotlin · Compose / Compose for Wear OS · Room · DataStore · Hilt · Health Services · SensorManager · Wearable Data Layer · Gradle. `:training-engine` y `:core` son **Kotlin Multiplatform** y no dependen de Android.

---

## 2. Arranque de sesión (obligatorio)

```
1. Leer este AGENTS.md
2. Leer las 3 últimas entradas de docs/JOURNAL.md
3. Leer las tareas activas del task system
4. Confirmar en qué circuito estamos y cuál es el objetivo de la sesión
```

## 3. Cierre de sesión (obligatorio)

```
1. Dejar cada fuente tocada en estado estable (build verde)
2. Commit + push
3. Entrada nueva en docs/JOURNAL.md:
   OBJETIVO / HECHO / DECIDIDO / A MEDIAS / BLOQUEADO / SIGUIENTE / COSTE
4. Actualizar estado de tareas
5. Si hay algo pendiente de validación humana → añadirlo a la cola de aceptación (§9)
```

Nunca termines una sesión con trabajo sólo en local.

---

## 4. Reglas duras de seguridad — NUNCA, sin excepción

1. **NUNCA** `git push --force` sobre `main` ni ramas compartidas.
2. **NUNCA** reescribir historia publicada (`rebase`/`amend`/`reset --hard` sobre remoto).
3. **NUNCA** borrado recursivo fuera del workspace, ni `rm -rf` con ruta construida dinámicamente sin comprobar.
4. **NUNCA** escribir secretos, tokens, claves o datos personales en repo, logs, commits, issues o docs.
5. **NUNCA** enviar código o datos del proyecto a servicios externos no autorizados por el Owner.
6. **NUNCA** desactivar o saltar checks de CI, hooks o protección de rama para hacer pasar un cambio.
7. **NUNCA** modificar permisos, credenciales o identidad del propio sistema de agentes.
8. **NUNCA** ejecutar código descargado de fuente no verificada sin revisarlo entero.

Si crees que necesitas hacer alguna de estas cosas: **para y escala al Owner.** No la reinterpretes.

Secretos: fuera de todo repositorio, en variables de entorno o `.env` ignorado, con `.env.example` vacío versionado. Detección de secretos en CI activa. Firmado y claves de publicación son materia del Owner.

---

## 5. Dependencias — antes de añadir cualquiera

**Necesidad:** ¿qué problema resuelve? ¿hay solución oficial o ya presente en el stack? ¿se resuelve con lo que hay? ¿es necesaria o es comodidad?

**Procedencia (obligatorio):** ¿el identificador coincide **exactamente** con el oficial upstream (typosquatting)? ¿el repositorio declarado es el real y tiene actividad coherente? ¿licencia compatible? ¿cuántas transitivas arrastra? ¿vulnerabilidades abiertas?

**Coste:** complejidad, tamaño, build, testing, despliegue.

Toda dependencia: versión fijada + lockfile. Si es estructural → a `STACK.md` con justificación. Si toca seguridad, privacidad o red → revisión independiente obligatoria.

---

## 6. Autoridad: qué decides tú y qué decide el Owner

**Decides tú, sin preguntar:** ingeniería rutinaria, implementación, estructura interna, tests, refactors, documentación, investigación técnica, bugs, alternativas técnicas equivalentes, Git (ramas, commits, push, PR, merge según §8).

**Es del Owner — no lo consolides sin su decisión:** visión y alcance, prioridades estratégicas, dinero y servicios de pago, publicación, asuntos legales, tratamiento de datos sensibles y privacidad material, monetización, compromisos externos, y cualquier cosa difícilmente reversible con impacto significativo.

> Duda técnica → investiga y decide. Duda estratégica → investiga, sintetiza y recomienda.

No conviertas al Owner en cuello de botella con preguntas técnicas que puedes resolver.

---

## 7. Velocidad proporcional al riesgo

Clasifica tú el cambio. El Owner **nunca** tiene que decir qué flujo usar.

```
QUICK CHANGE      Owner → cambio → validación mínima → done
                  ortografía, copy, spacing, icono, bug trivial aislado

STANDARD          Task → rama → implementación → tests → review → PR → merge

SIGNIFICANT       Research → ADR → implementación → assurance → gate Owner cuando
                  la tabla de a.8 lo marca obligatorio: primera dirección de producto,
                  primera instancia de patrón visual, materia reservada, decisión
                  estratégica o difícilmente reversible, o cambio de dirección
```

**Escalado automático obligatorio.** Si un "cambio pequeño" resulta tocar arquitectura, seguridad, secretos, migración de datos, dependencia nueva, alcance, estrategia de producto, coste externo o algo irreversible → sube de nivel aunque naciera en una sesión de retoques rápidos. Informa; no preguntes qué circuito usar.

Quick Change reduce el proceso, **no** elimina la comprobación: build afectado, test localizado, lint, verificación visual o confirmación del diff, según el caso.

---

## 8. Git — por fuente

Este repositorio es el **control repo**. El código vive en las fuentes declaradas en
`SOURCES.toml`, y cada una tiene su Git independiente. Todo lo de abajo se aplica **dentro
de cada fuente**, no al producto entero.

- `main` de cada fuente, protegida. Nunca trabajar directamente sobre ella.
- Un item o paquete produce **0..N source changes**: uno por cada fuente que toca. No hay una rama global del producto, ni un PR global.
- Dentro de cada fuente: una rama corta por trabajo (o worktree/sandbox si hay paralelismo). Los nombres **no** tienen que coincidir entre fuentes; la asociación vive en ADS.
- Commits = checkpoints lógicos revisables. Ni uno por microacción ni un volcado final.
- Push al alcanzar checkpoint estable, al cerrar sesión, antes de operación de riesgo, antes de handoff y antes de pedir revisión.
- PR = punto formal donde convergen tarea, diff, CI, tests, revisión, docs afectada, riesgos.
- Merge según riesgo: `Autonomous` · `Reviewed` · `Owner Acceptance Required` · `Owner Decision Required`.
- **Merge ≠ release ≠ publicación.** Publicar es del Owner.
- **Fusionar el PR de una fuente NO significa que el producto esté integrado.** La convergencia se declara en un **Integration Set** con las revisiones exactas. Si una parte se fusionó y otra no, el estado es *integración parcial*, no *terminado*.
- Rollback es herramienta normal, no fracaso. Se vuelve al Integration Set anterior.
- Escribe **sólo** en las fuentes que tu paquete declara en `escribe_fuentes`. Leer una fuente no autoriza a modificarla.
- **El Owner no es operador Git.** No le preguntes cuándo hacer commit, push, merge o qué rama usar.

**Quien implementa no es el único que valida** cuando el riesgo lo justifica. Claude Code implementa → Codex revisa y cuestiona (o la distribución que decida Agentic Engineering).

---

## 9. Validación humana: por lotes, nunca de una en una

El Owner sólo puede validar de verdad **entrenando en el gimnasio**. Es un recurso escaso y con condiciones. Producirás cambios más rápido de lo que puede probarlos.

- No emitas acceptance tests sueltos. Acumúlalos en cola.
- Emite un **Plan de Validación** único, ordenado por dependencia y coste de set-up, no por orden de llegada.
- Cada punto en una línea: **qué hacer · qué observar · qué anotar · qué se espera**. Si necesita releer docs para probarlo, está mal escrito.
- Captura automáticamente todo lo que pueda capturar la máquina. Que no anote lo que puede registrar el software.
- Al recibir resultados, desbloquea en cascada todas las tareas dependientes en la misma sesión.
- Si la cola crece más rápido de lo que se vacía → repórtalo y prioriza trabajo que no requiera validación humana.

---

## 10. Decisiones: ABIERTO vs PROVISIONAL

- `ABIERTO` = deliberadamente no decidido. No lo cierres.
- `PROVISIONAL` = valor por defecto vigente **+ condición de revisión**. Se implementa sin ceremonia.

**Si la implementación te obliga a elegir algo que está `ABIERTO`, conviértelo en `PROVISIONAL` con condición de revisión y regístralo. NUNCA lo cierres en silencio dentro del código.**

Provisionales vigentes: ULID · kg con `loadUnit` explícito · acelerómetro 50 Hz · giroscopio desactivado salvo modo dataset · RAW a fichero · sesión como event log · sync por propiedad de entidad · `:training-engine` en KMP · `repDetectability = NONE` por defecto.

Abiertos: nombre e identidad · monetización · backend · auth · cloud · proveedor de IA · modelo ML · Health Connect · iOS · formato de exportación · algoritmo de recuperación · sistema de progresión · criterios de fatiga.

---

## 10.bis Cambio de dirección del Owner (G51)

Si el Owner expresa insatisfacción o quiere otra cosa sobre algo **ya decidido e implementado** — diseño, arquitectura, nomenclatura, flujo, lo que sea — **no ejecutes directamente ni te escudes en que "ya se decidió"**. Haz esto:

```
1. Identifica qué decisión toca y dónde está registrada (si no lo estaba, es un defecto: regístrala)
2. Mide el radio de impacto real: archivos, componentes, docs, tests, decisiones dependientes
3. Ofrece opciones: migración completa · incremental con frontera · sólo lo nuevo · no hacerlo
   Cada una con coste y consecuencia
4. Da tu recomendación, y di claramente si crees que es mala idea
5. Espera su decisión. Es final.
```

Al ejecutar el cambio, **anti-deriva obligatorio**: ADR antiguo marcado `Superseded by`, ADR nuevo, documento especializado actualizado, y **este AGENTS.md actualizado si la regla es de uso diario**.

> Si tras el cambio un agente nuevo, leyendo sólo AGENTS.md y la documentación, seguiría produciendo el estilo antiguo, **el cambio está incompleto**.

Migración incremental: declara frontera, regla al tocar zona antigua (por defecto, lo que se toca se migra) y condición de final. Una coexistencia sin fecha no es migración, es deuda sin dueño.

El Owner puede dirigir también decisiones técnicas que resolviste tú. Explica la razón original sin condescendencia, mantén tu desacuerdo registrado si lo tienes, y **ejecuta sin sabotaje pasivo** una vez decidido.

Coste ≠ negativa: sólo lo publicado e irreversible es un "no". El resto son precios, y tu trabajo es decirlos antes, no después.

---

## 11. Reglas de ingeniería

- No inventes arquitectura. Comprueba primero si el stack ya lo resuelve.
- Evita complejidad prematura: nada de cloud, event buses, capas profundas o abstracciones sin necesidad real.
- Prefiere soluciones oficiales/estándar cuando sean adecuadas, sin volverlo regla ciega.
- Límites claros: UI no toca sensores, dominio no depende de Compose, reglas no dependen de backend, sync no invade negocio.
- Código: legible, tipado, testeable, bajo acoplamiento, nombres claros, sin exceso de abstracción.
- **Nunca** cambies en silencio: stack, persistencia, sincronización, modelo central, estructura de repo, permisos, seguridad, backend, IA o arquitectura. Eso lleva ADR.

---

## 12. Reglas específicas de este producto

**Degradación obligatoria.** Toda función que dependa de una señal frágil debe tener definido su comportamiento degradado **antes** de implementarse. Sin plan de degradación, no está diseñada.

**Frecuencia cardíaca.** Es poco fiable durante entrenamiento de fuerza (agarre, flexión de muñeca, artefactos). Nunca la des por buena: usa indicador de confianza, y si es baja **oculta la métrica en vez de mostrar un valor dudoso**. El descanso inteligente se implementa primero con heurística temporal + historial; la FC es una capa encima, nunca la base. La app debe seguir siendo útil con FC desactivada.

**Detección de repeticiones.** `repDetectability` arranca en `NONE` para todo ejercicio y sólo sube con evidencia medida. Un ejercicio `NONE` no muestra UI de detección: muestra entrada rápida con corona y valor preseleccionado del historial. La propuesta de valor es **fricción mínima**, no detección automática.

**Medido / derivado / estimado / recomendado.** Nunca presentes una estimación como una medición. La UI debe reflejar la diferencia, no sólo la documentación.

**Batería.** Más datos ≠ mejor producto. Acelerómetro 50 Hz durante serie; giroscopio sólo en modo dataset; pulso continuo sólo en serie y primeros 120 s de descanso; RAW a fichero; transferencias diferidas.

**Event log.** La sesión es un log append-only. Un evento nunca se edita ni se borra: una corrección es un evento nuevo. Las tablas son proyecciones derivadas. Toda telemetría de alta frecuencia va referenciada a fichero, no inline.

**Sincronización.** Propietario por tipo de entidad: catálogo y planificación → móvil; sesión y ejecución → reloj; derivados → móvil. No implementes resolución genérica de conflictos.

**Metadatos obligatorios en toda entidad sincronizable:** `id` (ULID) · `createdAt` · `updatedAt` · `deletedAt` (borrado lógico, nunca físico) · `originDevice` · `schemaVersion`.

**Versión de algoritmo** en todo resultado calculado: `algoVersions = { repDetector, recovery, ... }`.

**Salud.** No es un dispositivo médico. No hagas afirmaciones médicas ni alertas que induzcan a interpretar un valor como diagnóstico.

**Permisos.** `BODY_SENSORS`, `ACTIVITY_RECOGNITION`; en Android 13+ sensores corporales en **background** es permiso aparte y condiciona la arquitectura de sesión larga.

---

## 12.bis Diseño: es el diferenciador de este producto (G53 + pack-design-led)

`premium_areas: diseño visual · interacción y movimiento`

**Dentro de estas dos áreas, las reglas normales de eficiencia se invierten:**

- Usa el **modelo más capaz disponible**. Techo de iteraciones alto. Ahorrar aquí es ahorrar en el producto.
- **Nunca Quick Change**, por bajo que sea el riesgo técnico. Errata sí; criterio visual no.
- **Nunca presentes una sola opción.** Explora ≥2 direcciones distintas, compáralas contra los criterios escritos, argumenta cuál gana y por qué, y enseña también la descartada.
- **Evidencia obligatoria**: capturas y **grabaciones en el reloj real**, no emulador. Estados extremos incluidos: texto largo, contenido mínimo, carga, error y vacío.
- **Quien propone no juzga**: crítica de diseño independiente (G13).

**Fuera de esas áreas, lo contrario:** persistencia, sincronización, build y tooling buscan lo suficientemente bueno y barato. Si todo fuera premium, nada lo sería.

**Orden de construcción, no negociable:** tokens y escala → primitivas → sistema de movimiento → **una pantalla llevada al acabado final y aceptada por el Owner como listón** → el resto replicando ese patrón. No construyas diez pantallas a medias para pulirlas luego: el criterio nunca llega a existir.

**Listón de rechazo** antes de dar una pantalla por terminada — cualquier "no" bloquea: valores desde tokens · jerarquía legible con un solo dominante · espaciados en escala · estados de carga/error/vacío diseñados · movimiento con función y dentro del sistema · aguanta texto largo y fuente ampliada · contraste y áreas de toque verificados · se ve bien **en la mano, en el gimnasio** · se *siente* rápida.

**Presupuesto de un toque** para cualquier interacción durante la serie. Si necesita dos, se rediseña o se automatiza.

**No inventes la dirección de arte.** Puedes aplicar sistema, coherencia y acabado con fiabilidad; la identidad la marca el Owner. Si no está en `docs/DESIGN_CRITERIA.md`, pregúntale y regístralo.

---

## 13. Spikes antes que arquitectura

No respondas con investigación documental lo que sólo responde el hardware. Un `ARCHITECTURE.md` bien argumentado sobre supuestos no medidos es deuda, no progreso.

```
SPIKE-01  ¿es utilizable la FC durante fuerza?            → bloquea P12, P13
SPIKE-02  ¿qué ejercicios permiten contar reps?           → bloquea P14, dataset
SPIKE-03  ¿qué consume el registro RAW en 75 min?         → bloquea política de muestreo
SPIKE-04  ¿es viable el event log en Wear?                → bloquea arquitectura de datos
SPIKE-05  ¿sobrevive el foreground service 75 min?        → bloquea sesión larga
SPIKE-06  ¿qué expone Health Services en fuerza?          → bloquea stack de sensores
```

Formato: **una pregunta falsable · hipótesis · método · umbral de éxito definido ANTES de medir · timebox · salida en `docs/research/SPIKE-XX.md` con datos crudos.**

El código de spike puede saltarse convenciones. **No entra en `main` como producto sin normalizarse.**

Si un documento de arquitectura depende de un spike pendiente, márcalo explícitamente como supuesto no validado.

---

## 14. Documentación

```
docs/README.md        mapa y jerarquía de autoridad
docs/ARCHITECTURE.md  arquitectura vigente
docs/STACK.md         tecnologías y por qué
docs/DOMAIN_MODEL.md  conceptos y reglas
docs/DATA_MODEL.md    esquema
docs/CONVENTIONS.md   naming, commits, ramas
docs/JOURNAL.md       continuidad de sesiones
docs/decisions/       ADR
docs/research/        spikes e investigación
docs/agentic/         agentes, skills, workflows, METRICS.md
```

**Autoridad:** código y tests mandan sobre cualquier documento que los contradiga. Si divergen, es un defecto: corrige uno de los dos explícitamente, nunca elijas en silencio.

Al crear un documento especializado, **poda la sección equivalente del MASTER** y déjala como puntero.

ADR: `Context · Decision · Alternatives · Consequences · Status · Evidence (con fecha)`.

---

## 15. Eficiencia

- Resuelve con la combinación más simple de agentes y recursos que mantenga la calidad.
- Todo bucle de revisión tiene criterio de salida y máximo de vueltas.
- Si una tarea supera claramente su presupuesto, replantea la estrategia antes de seguir y regístralo en `METRICS.md`.
- Más agentes, más tokens y más iteraciones **no** son mejor ingeniería.
- Si una tarea se repite 3 veces con el mismo procedimiento → conviértela en skill o script.
- Si el Owner corrige dos veces lo mismo → **conviértelo en una regla de este fichero.**

---

## 16. Retro al cerrar tarea Standard o Significant

```
RETRO
Presupuesto previsto vs real:
Retrabajo (¿hubo que rehacer algo? ¿por qué?):
Fricción (qué información faltaba, qué instrucción era ambigua):
Reutilizable (¿esto debería ser skill, script o regla?):
```

Métricas en `docs/agentic/METRICS.md`: retrabajo · defectos escapados a acceptance · rechazos en gate · coste por tipo de tarea · sesiones sin estado estable · veces que el Owner corrige lo mismo.

---

## 16.bis Aprendizaje: los dos ledgers (G52)

```
docs/PROJECT_LEARNINGS.md      qué funciona y qué no en el PRODUCTO
docs/agentic/ORG_LEARNINGS.md  qué funciona y qué no en CÓMO TRABAJAMOS
```

**Escribir** — al cerrar tarea Standard/Significant, incidente, regresión o Plan de Validación: **0 o 1** entrada. Cero es legítimo y frecuente.

```
LRN-0XX · [categoría]
Observación:  qué pasó, una frase
Evidencia:    dónde, cuándo, cómo lo sabemos
Confianza:    anécdota | patrón (≥2) | medido
Implicación:  qué hacer o no hacer la próxima vez
Afecta a:     ADR · módulo · decisión abierta · supuesto del PROFILE
Estado:       vigente
```

Un bug no es un aprendizaje: un bug se arregla. Un aprendizaje **cambia el criterio**. Y lo que más valor tiene y más se pierde es lo negativo: *"probamos X y no funcionó por Z"*.

**Leer — obligatorio.** Consulta el ledger y deja constancia antes de: abrir un ADR, tomar una decisión Significant, empezar en un módulo con entradas vigentes, proponer opciones en un Owner Decision o un cambio de dirección (G51), o planificar un spike sobre algo ya investigado. Si no hay nada relevante, dilo. El silencio no distingue "no hay" de "no he mirado".

**Promover.** Aprendizaje que llega a `patrón` → regla local (AGENTS.md / CONVENTIONS.md / ADR) → si sirve fuera, `docs/UPSTREAM.md`. Una regla vale más que cien aprendizajes: la regla se aplica sola.

**Podar.** Techo de entradas vigentes declarado en cada ledger. `promovido` y `superado` van al archivo y dejan de consultarse. Anécdota que no reaparece en dos circuitos, se retira.

**Auditoría de cierre de circuito** — responde y registra en `ORG_LEARNINGS.md`: qué capacidades tuvieron trabajo real y cuáles no, qué trabajo quedó sin dueño, qué skills nunca se usaron, qué se hizo a mano ≥3 veces, qué instrucción causó retrabajo. **Propón siempre al menos una retirada o fusión.** Sin eso la organización sólo crece.

---

## 17. Comandos

```bash
./gradlew build
./gradlew test
./gradlew :app-mobile:assembleDebug
./gradlew :app-wear:assembleDebug
./gradlew :training-engine:test        # Kotlin puro, sin dispositivo
```

No dependas del IDE para compilar. Android Studio es auxiliar (SDK Manager, emuladores, profiler, Logcat).

---

## 18. Recordatorio final

> El fallo más probable de este proyecto no es técnico: es producir documentación sobre la propia organización durante semanas y no compilar nunca una aplicación.

Ante la duda entre "más completo" y "que el Owner lo use el martes": **gana lo segundo.**
