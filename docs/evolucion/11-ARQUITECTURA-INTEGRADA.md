# F4 — ARQUITECTURA INTEGRADA

Fase **F4** del [plan](04-PLAN-DE-INVESTIGACION.md) y trabajo **23.5** de la
[directiva](ADS-NEXT-OWNER-BRIEF.md). Un solo sistema, no una colección de subsistemas
unidos por documentación — que es lo que el 23.5 rechaza con esas palabras.

> **Esto es diseño, no construcción.** Nada de lo que sigue está implementado, probado ni
> ejecutado. La distinción entre contrato definido, implementación, prueba ejecutada, prueba
> superada y uso real es la disciplina central de este repositorio, y esta fase produce
> **sólo la primera**.
>
> **F4 no está certificada, y este texto ha sido CORREGIDO DOS VECES.**
>
> ```text
> PRIMERA DEVOLUCIÓN    nueve bloques de hallazgos, en
>                       12-CRITICA-INDEPENDIENTE-F4.md. Correcciones: D23–D33
> SEGUNDA DEVOLUCIÓN    veredicto de INSUFICIENCIA por un revisor con contexto limpio que
>                       no escribió F4 NI aplicó la primera crítica: DOS hallazgos
>                       BLOQUEANTES, siete GRAVES y catorce nuevos, en
>                       13-SEGUNDA-CRITICA-INDEPENDIENTE-F4.md. Correcciones: D34–D45
> DEVOLUCIÓN TÉCNICA    auditoría externa sobre el ÁRBOL REMOTO REAL: TRES BLOQUEANTES, dos
> PREVIA                GRAVES, cuatro MEDIOS y dos MENORES, en
>                       14-DEVOLUCION-TECNICA-PREVIA-F4C.md. Correcciones: D46–D51.
>                       NO es un veredicto de suficiencia: es revisión técnica
> CORRECCIÓN TÉCNICA    sobre el protocolo transaccional: DOS BLOQUEANTES más —la
> POSTERIOR             reconciliación no era recuperable, y la integridad post-terminal
>                       salía del terminal— y un GRAVE. Correcciones: D52–D54.
>                       Tampoco es la tercera revisión, y tampoco certifica nada
> SEXTA COMPROBACIÓN    sobre la semántica de sellado y retirada de cuerpo: la lápida
> TÉCNICA               conservaba un `id` que ya no podía recalcularse, la huella se
>                       presentaba como prueba de contenido, y «cualquier evento vivo» hacía
>                       inalcanzable la retirada. Corrección: D63. TAMPOCO es la tercera
>                       revisión, y TAMPOCO certifica nada
> QUINTA COMPROBACIÓN   de un solo punto, sobre `D60`: un único campo `iteracion` numeraba
> TÉCNICA               OBSERVACIONES e INTENTOS a la vez, y valía 4 bajo un máximo de 3. Se
>                       separan los dos contadores. Corrección: D62. TAMPOCO es la tercera
>                       revisión, y TAMPOCO certifica nada
> CUARTA COMPROBACIÓN   acotada, sobre `D58`–`D59`: la cardinalidad «exactamente una vez»
> TÉCNICA               era insatisfacible por ruta, y la frontera de recursión era falsa y
>                       clasificaba mal `sellado`. Correcciones: D60–D61. TAMPOCO es la
>                       tercera revisión, y TAMPOCO certifica nada
> TERCERA COMPROBACIÓN  acotada, sobre `D55`–`D57`: el recuento de fases mezclaba ejes, la
> TÉCNICA               «reemisión» admitía un `confirmada → confirmada` que §2.8 ya
>                       prohibía, y la matriz era un cartesiano sin demostrar. Correcciones:
>                       D58–D59. TAMPOCO es la tercera revisión, y TAMPOCO certifica nada
> SEGUNDA CORRECCIÓN    TRES GRAVES sobre el texto que la corrección anterior escribió:
> TÉCNICA               garantías atribuidas a un esquema que no puede comprobarlas, `W12a`
>                       contra la clasificación por hashes de §2.6.4, y siete valores de
>                       `tipo` sin contrato. Más los restos vigentes de §2.6.
>                       Correcciones: D55–D57. TAMPOCO es la tercera revisión, y TAMPOCO
>                       certifica nada
> ```
>
> **Dos de los hallazgos de la segunda devolución son defectos que la PRIMERA CORRECCIÓN
> introdujo o no vio, los TRES de la segunda corrección técnica están en el texto que la
> corrección técnica ANTERIOR escribió, los DOS de la tercera comprobación están en el
> texto que la segunda escribió, los DOS de la cuarta están en el texto que la tercera
> escribió, el de la quinta está en el texto que la cuarta escribió, y el de la sexta está
> en el texto que la quinta escribió.** Es el SÉPTIMO encadenamiento consecutivo, y es la
> razón por la que las revisiones se encadenan en vez de darse por buenas. **Quien aplicó
> todas es quien las recibió**, luego ninguna prueba nada: `F4c` sigue **ABIERTA**,
> pendiente de una **tercera revisión independiente**.

---

# 0 · Resumen ejecutivo

Para el Owner, sin vocabulario interno.

**Qué se ha decidido, en siete frases.**

1. **El estado del proyecto vive en ficheros de texto dentro del repositorio de control**, se
   lee sin ninguna herramienta y se versiona con Git. No hay base de datos que gobierne: si
   apareciera, sería una copia, y las copias divergen.
2. Junto a esos ficheros hay un **diario de lo que pasó** —quién ordenó qué, sobre qué base y
   quién lo aplicó— que además permite terminar o deshacer una escritura interrumpida. Es lo
   que hace que una caída a mitad no deje el sistema inventando estado.
3. **Cada entorno de IA —Claude Code, Codex, Cursor, Gemini— recibe ficheros generados**, no
   escritos a mano. Se generan desde una única definición y llevan una huella que delata si
   alguien los editó. Hoy **ninguno está certificado**; certificar exige una prueba real.
4. Un trabajo grande se llama **iniciativa** y agrupa varios items sin sustituirlos. Su
   dosier no es un documento que alguien mantiene: se calcula.
5. **La calidad de cada parte del producto se registra y caduca.** El sistema puede decir qué
   nunca se revisó, qué venció y qué está corregido pero sin verificar. Puede detectar y
   proponer por su cuenta; **abrir trabajo** exige la política que el Owner ya autorizó, y esa
   política es revocable.
6. **Instalar, adoptar, migrar y actualizar son cuatro recorridos distintos** que comparten
   maquinaria y no se mezclan: cada uno tiene su disparador, sus fases, su gate, su rollback y
   su certificación.
7. Se añaden **cuatro tipos de estado** —`iniciativa`, `adaptador`, `cobertura` y
   `evento`— y **dos esquemas de clase**: `nivel-certificacion` y `contrato-de-aspecto`. El
   número **se calcula** aplicando la prueba materia a materia (§3.8); no se fija de
   antemano, y por eso ha cambiado dos veces. Todo lo demás se compone con lo que ya existe.

**Qué no se ha decidido, y por qué.**

```text
LA CUARTA CAPA           sigue deferida. Hace falta un proyecto independiente que minar.
EL PILOTO                sigue sin ejecutarse. Nada de aquí está demostrado en un producto.
LAS ENMIENDAS            este diseño presiona material aprobado en OCHO puntos, tras dos
                         devoluciones independientes. Se enumeran y NO se redactan: eso es
                         F5, y su puerta es el Owner.
```

**Qué cuesta.** El diseño elige, en cada punto donde había alternativa, la forma que se puede
leer sin herramienta y reconstruir desde Git. Eso encarece la velocidad de lectura de máquina
y abarata la recuperación, la auditoría y el cambio de proveedor. Es la contrapartida
deliberada, y está argumentada en §2.

---

# 1 · El modelo integrado

## 1.1 · Topología global

```text
                         ┌───────────────────────────────────┐
        OWNER  ─────────▶│  ENC · encuadre                   │  intención → entrada
                         └───────────────┬───────────────────┘
                                         │ encuadre listo
                         ┌───────────────▼───────────────────┐
                         │  DSP · despacho                   │  item · ruta · paquete
                         └───────────────┬───────────────────┘
                                         │ materializa (C4)
     ┌───────────────────────────────────▼────────────────────────────────────┐
     │  CAPACIDADES  PRD DIS ARQ DOM CON VER ENT USO INV SEG PLT APR SIS       │
     └───────────────────────────────────┬────────────────────────────────────┘
                                         │ escribe capas y source changes
                                         │
   ══════════════════ WORKSPACE DEL PRODUCTO (no es un repositorio) ══════════════════
     ┌──────────────────────────────┐   ┌──────────┐ ┌──────────┐ ┌──────────┐
     │  ads/   REPOSITORIO DE       │   │ frontend │ │ backend  │ │  mobile  │
     │         CONTROL              │   │  .git    │ │  .git    │ │  .git    │
     │  ┌────────────────────────┐  │   └────┬─────┘ └────┬─────┘ └────┬─────┘
     │  │ DISTRIBUCIÓN instalada │  │        │            │            │
     │  │  kernel · packs        │  │        └────────────┴────────────┘
     │  │  blueprint · esquemas  │  │                     │
     │  ├────────────────────────┤  │            source changes (C7)
     │  │ ESPECIALIZACIÓN        │  │                     │
     │  │  PROFILE · PROJECT     │  │              ┌──────▼───────┐
     │  │  SOURCES.toml          │◀─┼──────────────│ INTEGRATION  │
     │  │  overrides · skills    │  │              │     SET      │
     │  ├────────────────────────┤  │              └──────────────┘
     │  │ ESTADO DURABLE         │  │
     │  │  items · paquetes      │  │   ┌────────────────────────────────┐
     │  │  iniciativas · eventos │  │   │ PROYECCIONES generadas          │
     │  │  cobertura · memoria   │  │──▶│  AGENTS.md · CLAUDE.md          │
     │  ├────────────────────────┤  │   │  .cursor/ · reglas Gemini …     │
     │  │ DERIVADOS              │  │   │  con huella y aviso de generado │
     │  │  vistas · tableros     │  │   └────────────────────────────────┘
     │  │  dosieres · índices    │  │
     │  └────────────────────────┘  │   ┌────────────────────────────────┐
     │                              │   │ .ads/run/  OPERACIONAL          │
     │                              │   │  lock · caché · índice compilado│
     └──────────────────────────────┘   │  NO versionado, reconstruible   │
                                        └────────────────────────────────┘
```

## 1.2 · Los cinco planos, y por qué son cinco

Ésta es la separación que resuelve `CI-3`/`X8` sin crear una cuarta capa de conocimiento.

| plano | qué contiene | quién lo versiona | ciclo |
|---|---|---|---|
| **DISTRIBUCIÓN** | kernel, packs, esquemas, contratos, plantillas, blueprint, validadores | `ads-kernel`, por release | cambia al actualizar ADS |
| **ESPECIALIZACIÓN** | `PROFILE`, `PROJECT`, `SOURCES.toml`, overrides, skills y agentes propios del producto | el control repo del producto | cambia al conocer o cambiar el producto |
| **ESTADO DURABLE** | items, paquetes, iniciativas, eventos, cobertura, memoria, integration sets | el control repo del producto | cambia con cada trabajo |
| **PROYECCIÓN** | los ficheros que cada entorno agentic descubre | el control repo, **generados** | se recompila |
| **OPERACIONAL** | lock, cachés, índices compilados, información de proceso | **nadie**: no se versiona | efímero, reconstruible |

> **Estos cinco planos NO son `K-1`.** `K-1` clasifica **conocimiento** —¿esto sería cierto
> en otro proyecto, en otro de la misma clase, o sólo aquí?—. Éstos clasifican **ciclo de
> vida** —¿qué viaja con el release, qué se rellena, qué se genera, qué cambia al trabajar,
> qué no se guarda?—. Confundirlos fabricaría la cuarta capa por la puerta de atrás, y `X1`
> sigue deferida.

## 1.3 · Matriz de fuentes de verdad

**Un artefacto, un lugar canónico.** Todo lo demás lo enlaza. Es `I5` y la regla de fuente
única del [índice operativo](../../kernel/operativo/00-INDICE.md), aplicada a la arquitectura
entera.

| verdad | fuente única | autoridad | ejecutor de mutación |
|---|---|---|---|
| catálogo de capacidades, roles, métodos, gates | `kernel/operativo/` de la distribución instalada | `SIS` (upstream) | release de ADS |
| qué packs y extensiones tiene el producto | `PROJECT.md` | `SIS` | `SIS` |
| identidad, éxito, riesgos y decisiones fuertes del producto | `PROFILE.md` | Owner | `ENC` transcribe, Owner aprueba |
| qué repositorios y componentes forman el producto | `SOURCES.toml` | Owner | `PLT` |
| encuadre de un item | `estado/items/<ID>/00-encuadre.md` | `DSP` | runtime |
| ruta y traza de un item | `estado/items/<ID>/01-ruta.md` | `DSP` | runtime |
| **prioridad y aparcado de un item** | **`estado/items/<ID>/02-control.md`** | **Owner** | **runtime** |
| estado global, capas y desacuerdos | `estado/items/<ID>/03-integracion.md` | el propietario global | runtime |
| capa depositada por una capacidad | el paquete, en `estado/items/<ID>/paq/` | la capacidad con custodia | esa capacidad |
| **órdenes del Owner pendientes de consumo** | **zona `ÓRDENES` del tablero** | **Owner** | **ninguno: no hay mutación hasta consumirla** |
| qué pasó y por qué | `estado/eventos/` | nadie lo edita: se emite | runtime |
| agrupación de items con sentido común | `estado/iniciativas/<ID>/00-iniciativa.md` | quien la abre | runtime |
| nivel de calidad de una parte del producto | `estado/cobertura/` | `SIS` el contrato, la capacidad **responsable del aspecto** el juicio | runtime |
| combinación de revisiones probada junta | `integration-set` | `ENT` | `ENT` |
| gobierno documental de un documento | bloque `ads:memoria` **dentro** del documento | la capacidad que lo posee | esa capacidad |
| qué lee y escribe cada entorno agentic | `adaptador` en el control repo | `PLT` | `PLT` |
| conocimiento externo vendorizado | manifiesto de vendorizado | `SIS` | `PLT` |
| entradas de cada validador | `validadores.yaml` | `SIS` | `SIS` |
| zona `COLA` de un tablero, dosieres, vistas, índices | **nadie**: se regeneran | — | runtime |
| estado de una iniciativa | **nadie**: se calcula desde sus items (§3.3.1) | — | runtime |
| nivel alcanzado por un adaptador | **nadie**: se deriva de sus celdas de certificación (§6.5) | — | runtime |

**Tres reglas cierran la matriz. Dos son `a.9` literal; la tercera se deriva de `a.7`.**

```text
1  UNA FILA CON AUTORIDAD «NADIE» ES DERIVADA, y editarla no es una escritura canónica.
   El remedio ante una divergencia es REGENERAR, nunca sincronizar.

2  UNA ORDEN NO ES ESTADO. La zona ÓRDENES del tablero es un CANAL DE COMANDOS. Una orden
   PENDIENTE `- [ ]`, una en CONFLICTO `- [!]` o una que espera confirmación `- [?]` NO
   son todavía estado del item: `a.9` dice expresamente que ni se aplican ni se borran. El
   campo canónico de prioridad y aparcado es `02-control.md`, y sólo cambia cuando el
   protocolo de consumo de `a.9` aplica la orden y emite su evento.

3  EL RUNTIME ES EL ÚNICO EJECUTOR DE LA MUTACIÓN CANÓNICA. El Owner PUEDE escribir bytes
   en el tablero, y eso es la EMISIÓN DE UNA ORDEN, no una mutación. Así `I2` se mantiene
   aunque el Owner tenga las manos en el fichero.
```

> **Por qué el tablero aparece partido en dos filas.** `a.9` le da **dos zonas y dos
> escritores por diseño**. Declarar el tablero entero derivado —como hacía F4 entregada—
> autorizaría a regenerar encima de una orden no consumida, que es justo lo que `a.9`
> prohíbe con todas las letras: *«DSP nunca borra una orden no consumida»*.

## 1.4 · Cómo encajan los subsistemas

```text
INSTALACIÓN ─┐
ADOPCIÓN ────┤                 ┌── crean y especializan ──▶ ESPECIALIZACIÓN
MIGRACIÓN ───┼── §8, cuatro ───┤
ACTUALIZACIÓN┘   recorridos    └── se cierran con ────────▶ CERTIFICACIÓN §9
                 distintos                                        │
                                                                  ▼
   OWNER ──▶ ENC ──▶ DSP ──▶ CAPACIDADES ──▶ capas ──▶ INTEGRATION SET ──▶ release
               │       │           │                          │
               │       │           └── source changes ────────┘  §10
               │       │
               │       └── compone rutas · aplica frenos · regenera derivados   §7
               │
               └── clasifica findings, órdenes y trabajo histórico
                                   ▲
                                   │
        AUDITORÍA CONTINUA §5 ─────┘   detecta y propone; abre dentro de política O7
                │
                └── cobertura (sujeto × aspecto) ──▶ campañas = INICIATIVA §3
                                   │
                                   ▼
                            APRENDIZAJE §13 ──▶ release de ADS ──▶ ACTUALIZACIÓN
```

**Todo lo anterior se apoya en una sola pieza**, y por eso se decide primero.

---

# 2 · Disposición física del estado — la primera decisión

`H2` y el checkpoint la ordenan primero porque la certificación operativa, la iniciativa y la
matriz de cobertura se apoyan las tres en ella. Construirlas antes fabricaría tres almacenes
paralelos, que es el modo de fallo (a) de `a.7`.

## 2.1 · Qué tiene que cumplir, antes de mirar ninguna tecnología

Requisitos, con su fuente. No son preferencias:

```text
R1  el estado operativo ES los ficheros del repositorio ADS de control, legibles
    directamente, sin informe intermedio                          E2.1 sobre a.9
R2  I1 propiedad inequívoca · I2 escritura controlada por zona · I3 fragmentable por
    unidad de custodia · I4 vistas derivadas deterministas y legibles sin herramienta ·
    I5 sin duplicidad editable · I6 concurrencia y recuperación VERIFICABLES     a.9
R3  toda transición multiarchivo DEBE ser recuperable e idempotente; el runtime DEBE
    detectar una operación incompleta y terminarla o revertirla SIN INVENTAR ESTADO   a.9
R4  un artefacto derivado NO contiene hora de pared, duración, número de ejecución ni
    identidad de proceso. `source_revision` hashea sólo ficheros canónicos            a.9
R5  un solo ejecutor de mutaciones canónicas                                          a.9
R6  el estado global referencia revisiones de otras fuentes; NUNCA copia su contenido  E2.1
R7  `Continúa` reconstruye desde el estado canónico, sin conversación y sin el Owner   b.14
R8  G26/JOURNAL sigue PENDIENTE: los tableros no son secuencia de eventos, ni contexto
    transversal, ni por qué cambió el estado, ni operaciones fallidas, ni recuperación
    tras escritura parcial                                                      a.11
```

**`R8` es la pieza que falta y que nadie ha decidido.** `a.11` dice, con estas palabras, que
el runtime *«probablemente necesite un event log que PUEDA sustituirlo»* y que eso se decide
al diseñar memoria, eventos y recuperación — no por inferencia. Aquí se decide.

## 2.2 · Alternativas comparadas

| | forma | `R1` legible sin herramienta | `R3` atomicidad y recuperación | `R4` determinismo | `R7` reconstrucción | Git y diff | coste |
|---|---|---|---|---|---|---|---|
| **A** | sólo ficheros canónicos | **sí** | **no**: Git no convierte N escrituras en transacción; una caída deja estado parcial y nada lo detecta | sí | parcial: no sabe si una transición quedó a medias | excelente | bajo |
| **B** | SQLite como estado canónico | **no**: binario, ilegible sin herramienta, ilegible en un diff | sí, transacciones reales | sí | sí | **malo**: un blob que conflictúa entero | medio |
| **C** | event sourcing puro: sólo el log es canónico | **no**: leer el estado exige reproyectar | sí | sí | sí | bueno | alto: toda lectura es una proyección |
| **D** | **canónico en ficheros + diario de eventos con transacciones + derivados** | **sí** | **parcial, y cualificado**: recuperabilidad, idempotencia y **detectabilidad** de la ventana. La atomicidad lógica multiarchivo **NO se afirma** (§2.6.8) | sí | **sí** | excelente | medio |

**Por qué se descarta B.** Rompe `R1`, que no es una preferencia estética: es el requisito que
el Owner puso y que `E2.1` reafirmó al precisar *cuál* repositorio contiene esos ficheros. Un
estado en SQLite obliga a un informe intermedio para leerlo, que es exactamente lo que `R1`
prohíbe. **Se conserva una función para SQLite**: como **índice compilado no canónico** en el
plano operacional, regenerable y no versionado (§2.7). Ahí no gobierna nada y acelera lecturas.

> **Cualificado por la segunda devolución independiente (hallazgo `A`).** La casilla de `R3`
> para la opción D decía «sí» sin matiz. Lo que D ofrece es lo que `a.9` pide con esas
> palabras —*«recuperable e idempotente»*— más la detectabilidad de §2.6.8. **No ofrece
> aislamiento de lecturas**, y decir «sí» a secas invitaba a leerlo como si lo ofreciera.

**Por qué se descarta C.** Cumple `R3` de forma elegante y rompe `R1` de la forma más cara:
para saber en qué estado está un paquete habría que reproyectar el log. Además crece sin
límite y convierte cada lectura en un cómputo, lo que choca con §12.

**Por qué no basta A.** Es la disposición candidata que `a.9` ya esbozó, y `a.9` la deja
abierta precisamente por `R3`: *«Git no convierte una secuencia de escrituras en una
transacción: si el proceso muere a mitad, el estado queda parcialmente aplicado»*.

**Decisión: D.** Es A más **una** pieza mínima que le falta: un diario de eventos que además
sostiene las transiciones multiarchivo mediante fases. F4 entregada contaba **dos** piezas
—diario y manifiesto de transacción— y la segunda no pasaba la prueba de tipo nuevo. Se
pliega en la primera en §2.5, y el recuento se corrige aquí en vez de arrastrarse.

## 2.3 · La disposición

```text
ads/                                    el repositorio ADS de control
├─ PROFILE.md · PROJECT.md · SOURCES.toml        ESPECIALIZACIÓN
├─ kernel/ · packs/                              DISTRIBUCIÓN instalada
├─ estado/                                       ESTADO DURABLE · versionado en Git
│  ├─ items/<ITEM-ID>/
│  │  ├─ 00-encuadre.md      autoridad DSP
│  │  ├─ 01-ruta.md          autoridad DSP
│  │  ├─ 02-control.md       autoridad OWNER          prioridad · aparcado
│  │  ├─ 03-integracion.md   autoridad PROPIETARIO GLOBAL
│  │  ├─ paq/<nn>-<CAP>.md   autoridad LA CAPACIDAD CON CUSTODIA
│  │  │                      incluye checkpoint, source changes y declaración de acoplamiento
│  │  └─ vista.md            DERIVADO
│  ├─ iniciativas/<INI-ID>/
│  │  ├─ 00-iniciativa.md    autoridad de quien la abre
│  │  └─ dosier.md           DERIVADO
│  ├─ cobertura/<clase>/<sujeto>.md    autoridad SIS el contrato · la capacidad el juicio
│  ├─ integracion/<IS-ID>.md           autoridad ENT
│  ├─ eventos/
│  │  ├─ <EV-ID>.md          APPEND ONLY. Nadie los edita: se emiten
│  │  ├─ sellados/<seg>.md   compactación de items cerrados
│  │  └─ INDICE.md           DERIVADO
│  ├─ tx/<TX-ID>.abierta    MARCADOR de transacción EN VUELO, con el `tx` y LA LISTA DE
│  │                        RUTAS AFECTADAS (§2.6.8). Vacío en reposo, reconstruible desde
│  │                        el diario, y EXCLUIDO DE GIT: vive en el árbol durable y NO
│  │                        viaja (§2.6.6)
│  ├─ tableros/<CAP>.md      ÓRDENES (Owner) + COLA (DERIVADO)
│  └─ memoria/…              memoria de capacidad y ledgers
├─ adaptadores/<entorno>/    definición canónica neutral, no la proyección
├─ AGENTS.md · CLAUDE.md · .cursor/…   PROYECCIONES GENERADAS, con huella
└─ .ads/run/                 OPERACIONAL · NO versionado
   ├─ lock                   un solo ejecutor de mutaciones (R5)
   ├─ indice.sqlite          índice compilado, reconstruible, no canónico
   └─ cache/                 análisis vigente por huella
```

## 2.4 · Durable frente a operacional, y qué vive en Git

```text
DURABLE Y VERSIONADO     `estado/` SALVO la excepción de ruta declarada abajo, la
                         especialización, la distribución instalada, los adaptadores y sus
                         proyecciones. Sobrevive a la máquina.

OPERACIONAL Y NO VERSIONADO   `.ads/run/` — lock, cachés e índices compilados — Y los
                         marcadores de transacción de `estado/tx/`, por la excepción de
                         abajo. Se borra entero sin perder nada: se reconstruye desde lo
                         durable. Si borrarlo perdiera algo, ese algo estaba en el sitio
                         equivocado.
```

### La excepción de ruta, declarada — y son DOS categorías, no tres

> **Corregido por la devolución técnica previa (hallazgo `6`).** El texto anterior decía
> «DURABLE Y VERSIONADO: **todo** `estado/`», y `D40` colocaba el marcador en `estado/tx/`
> declarándolo **no versionado**, reconstruible y *«vive en el árbol durable y no viaja»*.
> Eso es una **tercera categoría informal** entre durable y operacional, y el modelo sólo
> tiene dos. Se resuelve clasificando, no inventando.

```text
QUÉ ES EL MARCADOR       **OPERACIONAL.** Su `plano` es `operacional`, y responde «no» a la
                         pregunta de §2.4: no tiene que sobrevivir a un clon nuevo, porque
                         se reconstruye desde el diario (§2.9).

POR QUÉ ESTÁ BAJO        por DESCUBRIBILIDAD, y sólo por eso: la regla de lectura de §2.6.8
`estado/` Y NO BAJO      obliga a comprobarlo ANTES de leer el estado, y un aviso de «esto no
`.ads/run/`              es fiable» que vive en un directorio que el lector no tiene por qué
                         mirar no es un aviso. Es una EXCEPCIÓN DE RUTA, no de naturaleza.

QUÉ DEJA DE SER CIERTO   «todo `estado/` es durable y versionado». Se corrige arriba en vez
                         de sostenerse con una nota al pie.

CÓMO QUEDA ALINEADO      `.gitignore` del control repo excluye `estado/tx/` · la
                         reconstrucción desde el diario está en §2.9 · un clon nuevo NO
                         contiene marcadores, y si los contiene es evidencia diagnóstica de
                         un defecto del runtime (§2.6.6, garantía 6) · `X27` lo comprueba
                         recorriendo la historia entera.
```

**El criterio, en una pregunta:** ¿sobrevive esto a `rm -rf` y a un clon nuevo? Si tiene que
sobrevivir, es durable y va a Git. Si no, es operacional — **y dónde esté colocado no cambia
la respuesta**, que es lo que la excepción de arriba hace explícito. Un dato que no sobreviva y que nadie
pueda recalcular **es un defecto de diseño**, no una categoría.

## 2.5 · Instantáneas, eventos y transacciones — qué es cada cosa

Dos artefactos, con papeles que no se solapan:

```text
FICHEROS CANÓNICOS   son el ESTADO. Responden «¿cómo está esto ahora?» sin cómputo.
                     Es lo que R1 exige y lo que un humano abre.

EVENTOS              son el CAMBIO. Responden «¿por qué está así, quién lo ordenó, sobre
                     qué base y quién lo aplicó?». Es G26, y es lo que a.11 dejó pendiente.
                     NO se reproyectan para leer el estado: el estado ya está escrito.
```

**No hay un tercer artefacto, y esto es una corrección.** F4 entregada declaraba un
**manifiesto de transacción** con identidad propia, ciclo propio —se abría, se marcaba y se
borraba— y contenido propio. Eso es un tipo, y estaba fuera de la cuenta de tipos sin haber
pasado la prueba del §3.1. Se le aplica ahora, y no la pasa:

```text
PASO 4 DE LA PRUEBA    ¿tiene sujeto propio, autoridad propia y ciclo propio que ningún
                       existente puede alojar sin mentir?

SUJETO      el mismo que el evento: una transición del estado canónico.       NO es propio
AUTORIDAD   la misma: el ejecutor único de mutaciones (R5).                   NO es propia
CICLO       parecía propio —cambiaba de fase— y ahí estaba el error de diseño: un
            artefacto que CAMBIA obliga a reescribirlo, y reescribir en el registro que
            debe sobrevivir a una caída es exactamente lo que no se puede hacer.

VEREDICTO   COMPONER. Una transacción es una SECUENCIA DE EVENTOS INMUTABLES que comparten
            un identificador `tx` y se distinguen por su campo `fase`. Ningún fichero
            cambia de estado: cada fase es un fichero NUEVO.
```

**Qué se gana al plegarlo, y se comprueba propiedad a propiedad:**

| propiedad que tenía el manifiesto | cómo sobrevive dentro de `evento` |
|---|---|
| declarar la intención antes de tocar nada | evento con `fase: preparada` |
| declarar la lista exacta de ficheros y su hash previo | campo `afecta`, con `hash_previo` por fichero |
| señalar «hay algo en vuelo» | una transacción **sin evento `derivada`**, que es el único terminal (§2.6.1). `estado/tx/<TX-ID>.abierta` la acelera y **lleva el `tx` y las rutas afectadas**, para que la regla de lectura de §2.6.8 sea ejercible sin recorrer el diario. Se reconstruye si se pierde |
| decir si la transición se aplicó | evento con `fase: confirmada` |
| poder cerrarse y desaparecer | **no sobrevive, y es lo correcto**: borrarlo era el defecto. §3.6 dejaba a `evento.tx` apuntando a un artefacto borrado |

**Ninguna propiedad se pierde, y una se retira a propósito.** El estado no guarda su
historia, y la historia no se reescribe nunca — que es lo que hace que el diario sea una
historia y no un estado más.

## 2.6 · El protocolo transaccional

Lo que `a.9` deja expresamente abierto, cerrado aquí de forma **ejecutable**: una
recuperación real tiene que poder llevarse a cabo con los datos que estos registros escriben,
y nada más.

### 2.6.1 · El autómata de fases — seis fases, dos rutas, un solo cierre

> **Corregido dos veces.** La devolución técnica previa unificó cinco formulaciones
> incompatibles en un solo autómata de cinco fases (`D46`). Una corrección técnica posterior
> encontró que **la ruta de conflicto no era recuperable**: `reconciliada` declaraba la
> decisión y a la vez la daba por aplicada, luego una caída entre decidir y emitir dejaba el
> diario **sin la decisión, sin su mecanismo y sin el resultado esperado** — y el `preparada`
> original no sirve, porque la decisión puede ser «conservar lo divergente» o «un tercer
> contenido». **Se añade la fase que faltaba.** Es `D52`.
>
> **El número de fases no es una cuota.** Fue cuatro, luego cinco, y ahora seis, porque cada
> vez se recalculó contra lo que el protocolo tiene que garantizar. Una cuota es lo que hizo
> que `D38` dijera «cuatro registros, no cinco» sin contar `reconciliada`.

```text
RUTA NORMAL         preparada ─────────────────▶ confirmada ──▶ derivada
                                                                    ▲
RUTA DE CONFLICTO   preparada ──▶ conflicto ──▶ reconciliacion-preparada ──▶ reconciliada ──┘

`derivada` es el ÚNICO cierre terminal de las DOS rutas.
NINGUNA transición sale de `derivada`.
```

**La simetría es el argumento.** La ruta de conflicto es **el mismo par intención/hecho** que
la ruta normal, aplicado a la decisión de resolución: `preparada` es a `confirmada` lo que
`reconciliacion-preparada` es a `reconciliada`. Ninguna de las dos escribe un canónico antes
de que su intención sea durable.

**Las seis fases, y qué significa cada una:**

```text
preparada                 INTENCIÓN PREPARADA. Declara a qué resultado exacto va a llegar
                          cada fichero. NO afirma que haya ocurrido nada. Es el PUNTO DE
                          COMPROMISO de la ruta normal: una vez es durable, la transacción
                          SE COMPLETA por una de las dos rutas, y no se revierte.
                          NO ES TERMINAL.

confirmada                CANÓNICOS COHERENTES POR LA RUTA NORMAL. Todos los ficheros
                          declarados alcanzaron su `hash_posterior_esperado`. Desde este
                          registro un lector puede creerse el contenido de esos ficheros —si
                          además respeta la regla de lectura de §2.6.8.
                          NO ES TERMINAL: faltan los derivados.

conflicto                 ABIERTO Y BLOQUEANTE. Un fichero no casa ni con la base válida ni
                          con el resultado permitido de su intención vigente: alguien de
                          fuera lo tocó (§2.6.4). NO admite `confirmada`. Registra la copia
                          íntegra de lo divergente. Bloquea el despacho sobre los items
                          afectados hasta que una autoridad decide.
                          NO ES TERMINAL. Ver §2.6.9.
                          **Corregido** (hallazgo `C4`): se le llamaba «absorbente», y no lo
                          es — tiene salida hacia `reconciliacion-preparada` y puede volver
                          a recibir un reintento. Un estado absorbente es el que no se
                          abandona nunca, y éste se abandona en cuanto la decisión es
                          durable. Lo que sí hace es BLOQUEAR mientras dura.

reconciliacion-preparada  INTENCIÓN DE RECONCILIACIÓN PREPARADA. Declara la decisión, su
                          autoridad, la base observada por fichero, cómo se produce el
                          resultado, el hash final esperado y el orden total —**todo ello
                          ANTES de tocar ningún canónico**—. Es el PUNTO DE COMPROMISO de la
                          ruta de conflicto.
                          NO ES TERMINAL. Ver §2.6.9.

reconciliada              DECISIÓN APLICADA DE FORMA DURABLE. Todos los ficheros que la
                          reconciliación tocó alcanzaron su `hash_final`.
                          NO ES TERMINAL: faltan los derivados.

derivada                  ÚNICO CIERRE TERMINAL. Los derivados afectados se regeneraron.
                          Sólo entonces se retira el marcador. Cierra las dos rutas.
```

**Las transiciones admitidas, y ninguna más:**

| desde | hacia | condición |
|---|---|---|
| — | `preparada` | el resultado se calculó y cada hash posterior es alcanzable desde su previo |
| `preparada` | `confirmada` | los N ficheros casan con su `hash_posterior_esperado` |
| `preparada` | `conflicto` | **algún** fichero es divergente (§2.6.4) |
| `confirmada` | `derivada` | los derivados afectados se regeneraron |
| `conflicto` | `reconciliacion-preparada` | la autoridad decidió, y su decisión es durable **antes de tocar nada** |
| `reconciliacion-preparada` | `reconciliada` | los ficheros de la decisión casan con su `hash_final` |
| `reconciliacion-preparada` | `conflicto` | un fichero **volvió a divergir** durante la aplicación. El nuevo `conflicto` incrementa `observacion` y `intentos_consumidos`. Con `observacion: 4` lleva `agotado: true` y **no admite ninguna `reconciliacion-preparada`**: para y escala (§2.6.4, §2.6.9) |
| `reconciliada` | `derivada` | los derivados afectados se regeneraron **sobre el estado reconciliado** |

```text
DE `derivada` NO SALE     ninguna. Es terminal, y quien lo hace cumplir es el VALIDADOR
NINGUNA                   SEMÁNTICO DEL DIARIO —no el esquema del evento—: rechazar un
                          evento con `tx` de una transacción que ya tiene `derivada` exige
                          MIRAR LOS DEMÁS EVENTOS de ese `tx`, y un esquema estructural
                          sólo ve el evento que valida (§3.6, reparto de capas).
                          Lo que se descubre DESPUÉS del cierre NO es una fase de esa
                          transacción: es un evento `tipo: deriva`, con identidad propia y
                          sin `fase`. Ver §2.6.11.

Y TAMPOCO SALE            de `confirmada` a `preparada` · de `conflicto` a `derivada` sin
NINGUNA OTRA              pasar por la reconciliación · de `reconciliacion-preparada` a
                          `derivada` sin `reconciliada`. **Ninguna fase salvo `derivada`
                          retira el marcador.**
```

**Qué se retira, y por qué se dice en vez de borrarse.**

```text
`fase: abortada`   RETIRADA, y RECHAZADA POR EL ESQUEMA. Un evento con esa fase es inválido.

                   Su ventana de alcanzabilidad era `[preparada durable, primer fichero
                   tocado)`, que es EXACTAMENTE el dominio de `W3` — y `W3` manda COMPLETAR.
                   Antes de que `preparada` sea durable no hay registro que pueda llevar esa
                   fase: `W2` dice «se borra el temporal. La transacción no existió».

                   NO HAY ABORTO, y la razón es positiva: entre el punto de compromiso y el
                   primer fichero, el único resultado es completar (`W3`); antes del punto de
                   compromiso no hay transacción que abortar (`W2`).

                   Es `D38`; `D46` la revisó para decir que quedaban CINCO fases y no cuatro,
                   y `D52` la revisa otra vez: son SEIS.
```

**Regla de lectura del diario, y es la que impide que la historia mienta:** un evento
**nunca** narra en futuro. `preparada` dice «preparada», y `reconciliacion-preparada` dice
«preparada» también. Ningún lector —humano o máquina— puede leer una intención como un hecho,
porque **la fase está dentro del propio registro** y no en su ausencia.

### 2.6.2 · Qué datos permiten reproducir el resultado

> **Corregido por la segunda corrección técnica (hallazgo `C4`).** Este párrafo decía que
> `preparada` *«es la única entrada que necesita la recuperación»*, y dejó de ser cierto en
> cuanto `D52` hizo recuperable la ruta de conflicto: una reconciliación se recupera desde
> **`reconciliacion-preparada`**, que declara la base observada y el `hash_final` que
> SUSTITUYE al esperado. La regla vigente es la de §2.6.4: **la recuperación se hace contra
> la INTENCIÓN DURABLE VIGENTE de cada ruta**, que son dos y no una.

En la **ruta normal**, el evento `preparada` es la única entrada que necesita la recuperación
—en la de conflicto se le añade `reconciliacion-preparada`, con sus siete campos (§2.6.9)—, y
lleva **seis cosas y no menos**:

```text
1  IDENTIDAD DE LA          `tx: TX-<huella>`. La comparten TODOS los eventos de esa
   TRANSACCIÓN              transacción y nadie más. **La cardinalidad es VARIABLE**, y lo
                            único fijo es que comparten `tx`:
                              · TRES en la ruta normal — `preparada`, `confirmada`,
                                `derivada`
                              · `3 + 2k` en la de conflicto que CIERRA, con `k` ∈ {1,2,3}
                                iteraciones: CINCO, SIETE o NUEVE (§2.6.4)
                              · OCHO en la que AGOTA el tope y queda abierta: `preparada`,
                                CUATRO `conflicto` —cuatro OBSERVACIONES, la cuarta con
                                `agotado: true`— y TRES `reconciliacion-preparada` —tres
                                INTENTOS, que es lo que el tope limita—
                              · y NADA MÁS. Recuperar no añade eventos: una fase de hecho
                                no se duplica, y restaurar un evento perdido devuelve el
                                MISMO evento, no uno nuevo (§2.6.4)
                            **Corregido**: decía «cuatro en la de conflicto», que era la
                            cuenta anterior a `D52` y nunca contempló los reintentos.

2  HASH PREVIO              por fichero. Qué había antes.

3  HASH POSTERIOR           por fichero. A qué exactamente hay que llegar. ESTE ES EL DATO
   ESPERADO                 QUE FALTABA: sin él, «no casa con el previo» es ambiguo entre
                            «ya aplicado» y «lo tocó otro», y los dos casos exigen lo
                            contrario.

4  CÓMO SE PRODUCE EL       una de tres formas, declarada: `contenido` —el texto completo
   RESULTADO                preparado—, `parche` —diff aplicable— u `operacion` —una
                            operación DETERMINISTA sobre el contenido previo—. En las tres,
                            aplicarla al hash previo tiene que dar el hash posterior, y eso
                            se comprueba antes de escribir nada.

5  ORDEN EXACTO             `orden: <n>` por fichero, total dentro de la transacción. La
                            recuperación aplica en el mismo orden, y por eso converge al
                            mismo resultado que una ejecución sin interrupción (T17).

6  PROCEDENCIA              los cinco conceptos de `a.9` sin confundirlos: ordenante,
                            autoridad, escritor del comando, ejecutor y actor atribuido.
```

**Por qué el contenido preparado va dentro del evento y no en un fichero aparte.** Porque
sólo hay una dirección de recuperación. Una vez el evento `preparada` es durable, **la
transacción se completa hacia delante**: no se deshace, porque deshacer exigiría conservar
también el contenido anterior y duplicaría el estado. Es un registro de rehacer, no de
deshacer, y esa elección se declara aquí en vez de quedar implícita.

### 2.6.3 · La secuencia, con sus puntos de sincronización

```text
1  PREPARAR       se calcula el resultado completo, se comprueba que cada hash posterior
                  es alcanzable desde su hash previo, y se escribe el evento `preparada`
                  por `escribir temporal + fsync + rename + fsync del directorio`.
                  NADA CANÓNICO SE HA TOCADO TODAVÍA.

                  ─── PUNTO DE COMPROMISO ─── a partir de aquí se completa hacia delante

2  MARCAR         se crea `estado/tx/<TX-ID>.abierta`, **con el `tx` y la lista de rutas
                  afectadas** (§2.6.8). Es un acelerador, no una verdad: si falta, el
                  arranque recorre el diario. **Corregido** (hallazgo `7`): decía «marcador
                  sin contenido», contra §2.6.8, que le da contenido para que la regla de
                  lectura sea ejercible sin recorrer el diario.

3  APLICAR        cada fichero canónico, en el `orden` declarado, con esta secuencia
                  EXACTA y en este orden:
                      escribir temporal → fsync(temporal) → rename → fsync(DIRECTORIO)
                  Un `rename` en el mismo sistema de ficheros es atómico: ningún fichero
                  queda a medias, aunque el CONJUNTO sí pueda. La atomicidad NO es la
                  durabilidad: sin el `fsync` del DIRECTORIO, el `rename` puede perderse
                  entero aunque el contenido esté en disco (§2.6.6, garantía 3).
                  Los directorios afectados pueden ser VARIOS —`estado/items/<ID>/`,
                  `estado/items/<ID>/paq/`, `estado/cobertura/<clase>/`…— y se sincronizan
                  TODOS los que reciban una entrada nueva o modificada. Un solo `fsync` de
                  `estado/` NO basta.
                  OPTIMIZACIÓN PERMITIDA Y NOMBRADA: agrupar los `fsync` de directorio por
                  directorio distinto, una sola vez al final del paso 3. Se nombra para que
                  nadie «optimice» quitando el que hace falta.

4  CONFIRMAR      evento `confirmada`, con `fsync + rename + fsync del directorio`.
                  ─── EL CAMBIO ES VERDAD DESDE ESTE RENAME ───

5  REGENERAR      los derivados afectados, con `source_revision` sobre los canónicos.
                  Sin `fsync`: un derivado perdido se recalcula.

6  CERRAR         evento `derivada`. Se borra el marcador `.abierta`.

7  PUBLICAR       el commit de Git es un paso SEPARADO, fuera de la transacción, y sólo
                  ocurre con `estado/tx/` sin marcadores abiertos. Ver 2.6.6.
```

### 2.6.4 · Cómo clasifica cada fichero durante la recuperación

> **Corregido por la segunda corrección técnica (hallazgo `H2`, GRAVE).** Las tres cajas
> estaban bien y **`W12a` no las respetaba**: mandaba emitir `conflicto` ante un canónico
> revertido a su `hash_previo`, que es exactamente la PRIMERA caja —NO APLICADO— y que `W3`
> y `W4` mandan completar hacia delante. El mismo estado observable recibía **dos
> clasificaciones incompatibles** según por qué ventana se entrara, y la que ganaba escalaba
> a una persona un resultado que sigue siendo **determinista**. Es `D56`.

**La clasificación se hace contra la ÚLTIMA FASE DURABLE que gobierna esa ruta**, no contra
el síntoma ni contra la ventana por la que se llegó. Primero se resuelve **qué intención
gobierna**, y sólo después se compara:

```text
INTENCIÓN VIGENTE     la última intención durable que declara esa ruta:
DE UNA RUTA             · `reconciliacion-preparada`, si la hay para esa ruta
                        · `preparada`, si no la hay
                      Es la misma regla que §2.6.6 usa para elegir el hash que gobierna, y
                      no dos reglas parecidas.

BASE VÁLIDA           `hash_previo`      si gobierna `preparada`
                      `hash_observado`   si gobierna `reconciliacion-preparada`

RESULTADO PERMITIDO   `hash_posterior_esperado`   si gobierna `preparada`
                      `hash_final`                si gobierna `reconciliacion-preparada`
```

**Y entonces, las tres cajas — que siguen siendo tres:**

```text
CASA CON LA BASE VÁLIDA      NO APLICADO      → aplicar, en el `orden` declarado. Es
                                                IDEMPOTENTE: reaplicar sobre la base no
                                                destruye nada, porque la base es
                                                exactamente lo que la intención durable ya
                                                se comprometió a sustituir
CASA CON EL RESULTADO        YA APLICADO      → saltar. Idempotente por hash, no por
PERMITIDO                                       confianza en un contador
NO CASA CON NINGUNO          DIVERGENTE       → CONFLICTO. Se escala. NUNCA se
                                                sobrescribe: el contenido que hay
                                                es de alguien, y aplicar encima
                                                destruiría trabajo sin registro
```

**Un fichero que no existe** se trata como caso declarado, no como excepción: si el evento
declara `hash_previo: ausente`, no existir es «no aplicado»; si declara un hash concreto, no
existir es **divergente**.

#### La función de clasificación, completa — y es UNA

Antes de las tres cajas hay dos preguntas que deciden **si hay transacción**, y sin ellas
`conflicto` se emite donde no hay transacción que pueda tenerlo como fase:

```text
0  ¿LA TRANSACCIÓN QUE DECLARA ESA RUTA TIENE `derivada` DURABLE?
     SÍ → NO HAY FASE POSIBLE. Ninguna transición sale del terminal (§2.6.1).
          · casa con el resultado que gobernaba  → nada que hacer
          · no casa                              → evento `deriva`, `causa:
                                                   posterior-al-cierre` (§2.6.11) · W12b

1  ¿EXISTE UNA TRANSACCIÓN ABIERTA —`preparada` durable y SIN `derivada`— QUE DECLARE
   ESA RUTA, EN ESTA INSTALACIÓN?
     NO → NO HAY TRANSACCIÓN, luego NO PUEDE HABER `conflicto`: sería una fase de algo
          que no existe.
          · casa con `HEAD`     → nada que hacer
          · no casa con `HEAD`  → evento `deriva`, `causa: sin-transaccion`
          · y si además hay un MARCADOR sin su transacción, o el marcador llegó en un
            árbol publicado, eso es un DEFECTO DE PUBLICACIÓN: evento `fallo`, nunca
            `conflicto` (§2.6.6)

2  INTENCIÓN VIGENTE, BASE VÁLIDA y RESULTADO PERMITIDO, como arriba.

3  LAS TRES CAJAS. Y `conflicto` sale de la tercera Y SÓLO DE ELLA.
```

**Las dos consecuencias que esto fija, y que antes se contradecían:**

```text
UN CANÓNICO REVERTIDO      casa con la BASE de su intención vigente → NO APLICADO → se
BAJO UNA TRANSACCIÓN       REAPLICA en el `orden` declarado, de forma idempotente. NO es
ABIERTA                    `conflicto`, porque `conflicto` exige que NO case con NINGUNO
                           de los dos hashes. El resultado es DETERMINISTA y no necesita
                           que nadie decida. Es `W12a`.

SI `confirmada` YA ERA      se REAPLICA igual, y **NO se emite ninguna fase nueva**: el
DURABLE Y UN CANÓNICO      evento `confirmada` YA EXISTE. La recuperación se hace desde
SE PERDIÓ POR              `preparada`, que declara el `hash_posterior_esperado` y el
DURABILIDAD                mecanismo —`contenido`, `parche` u `operacion`— con el que
                           reproducirlo; después se sigue con los derivados y con
                           `derivada`. No hace falta ninguna entrada nueva, no se pide
                           ninguna decisión humana y **no existe `confirmada →
                           confirmada`**.
```

#### Emitir y RESTAURAR no son lo mismo — y no existe `confirmada → confirmada`

> **Corregido por la tercera comprobación técnica (`D58`, que revisa `D56`).** La redacción
> anterior llamó «reemisión» a *«un evento NUEVO, con `id` propio, mismo `tx` y MISMA
> `fase`»*, y eso **contradice §2.8 punto 5**, que ya decía lo contrario: *«ANTES DE
> REEMITIR, el ejecutor busca en el diario un evento con el MISMO `tx` y la MISMA `fase`. Si
> existe, la operación es una NO-OPERACIÓN»*. Admitir un segundo `confirmada` habría creado
> una secuencia `confirmada → confirmada` que el autómata de §2.6.1 no tiene y que ninguna
> transición admite.

**Los dos casos, separados por si el hecho llegó a ser durable:**

```text
CASO A · `confirmada` NO       la última fase durable es `preparada`. Se completan los
LLEGÓ A SER DURABLE            ficheros que falten, y cuando los N casan con su
                               `hash_posterior_esperado` se emite `confirmada`
                               **UNA SOLA VEZ**. Es una EMISIÓN, y es la primera.
                               Cubre `W5` —nunca se llegó a escribir— y `W13` —se escribió
                               un temporal que nunca fue durable, luego el evento NO EXISTE—.

CASO B · `confirmada` YA ES    **el evento YA EXISTE, y no se añade otro.** La recuperación:
DURABLE                          1  reaplica los canónicos perdidos desde `preparada`, que
                                    declara el `hash_posterior_esperado` y el mecanismo
                                    —`contenido` | `parche` | `operacion`— con el que
                                    reproducirlos. Es DETERMINISTA
                                 2  NO emite ninguna fase nueva
                                 3  continúa con los derivados y con `derivada`
                               Cubre `W12a` con `confirmada` durable, y `X26`.
```

**Y el tercer caso, que es de almacenamiento y no de protocolo:**

```text
SI EL FICHERO DEL EVENTO       es una RESTAURACIÓN IDEMPOTENTE DEL MISMO EVENTO, no una
DURABLE SE PERDIÓ              emisión. El evento está direccionado por contenido (§2.8): se
FÍSICAMENTE                    vuelve a materializar el MISMO `id`, con el MISMO cuerpo y el
                               MISMO `predecesor`.
                                 · NO nace un evento nuevo
                                 · NO cambia la cadena `predecesor`
                                 · NO cambia el `tx`
                                 · el diario NO crece
                               Restaurar un fichero perdido y emitir un evento son
                               operaciones distintas, y confundirlas es lo que producía el
                               `confirmada → confirmada`.
```

#### La cardinalidad de cada fase es CONDICIONAL A LA RUTA, y a si la transacción cerró

> **Corregido por la cuarta comprobación técnica (`D60`, que revisa `D58`).** La redacción
> anterior decía que *«`preparada`, `confirmada`, `reconciliada` y `derivada` aparecen
> exactamente una vez por `tx`»*, y **eso es imposible en cualquier transacción real**: la
> ruta normal tiene `confirmada` y **no** `reconciliada`, la de conflicto tiene
> `reconciliada` y **no** `confirmada`, y una transacción que agotó los reintentos **no tiene
> `derivada` todavía**. Un invariante que ninguna transacción puede cumplir no es
> comprobable. Se sustituye por **invariantes condicionales por ruta y por cierre**.

**Primero, qué determina la ruta**, y es observable en el diario sin ambigüedad:

```text
RUTA NORMAL        #`conflicto` = 0.  Y entonces #`confirmada` = 1 y #`reconciliada` = 0
RUTA DE CONFLICTO  #`conflicto` ≥ 1.  Y entonces #`confirmada` = 0 y #`reconciliada` ∈ {0,1}
CERRADA            #`derivada` = 1 · el marcador se retiró
ABIERTA            #`derivada` = 0 · el marcador sigue vivo
```

**`confirmada` y `reconciliada` son MUTUAMENTE EXCLUYENTES.** Ninguna transacción tiene las
dos, y ninguna transacción cerrada tiene cero: cada ruta cierra con la suya.

**Los tres estados terminales o bloqueantes, con su cardinalidad exacta:**

| fase | RUTA NORMAL cerrada | RUTA DE CONFLICTO cerrada | RUTA DE CONFLICTO agotada y ABIERTA |
|---|---|---|---|
| `preparada` | **exactamente 1** | **exactamente 1** | **exactamente 1** |
| `confirmada` | **exactamente 1** | **0** | **0** |
| `conflicto` | **0** | `k` ∈ {1, 2, 3} **observaciones** | **exactamente 4 observaciones** |
| `reconciliacion-preparada` | **0** | `k` **intentos**, el MISMO número | **exactamente 3 intentos** |
| `reconciliada` | **0** | **exactamente 1** | **0** |
| `derivada` | **exactamente 1** | **exactamente 1** | **0** |
| total de eventos | **3** | **3 + 2k** → 5 · 7 · 9 | **8** |
| marcador | retirado | retirado | **ABIERTO** |
| estado | cerrado | cerrado | **BLOQUEADO y ESCALADO AL OWNER** |

```text
EL INVARIANTE QUE LAS       CERRADA POR CONFLICTO   #observaciones = #intentos
DISTINGUE SIN MIRAR         AGOTADA Y ABIERTA       #observaciones = #intentos + 1
NADA MÁS                                            y ese `+1` es el `conflicto` con
                                                    `agotado: true`, que registra el fracaso
                                                    del tercer intento y no tiene pareja
```

#### DOS contadores, porque son DOS conceptos — observación e intento

> **Corregido por la quinta comprobación técnica (`D62`, que revisa `D60`).** `D60` usó **un
> solo campo** `iteracion` para numerar dos cosas distintas, y con ello afirmó a la vez que el
> contador llega a **4** y que el tope es **3**, rematándolo con que *«`conflicto(4)` no es
> una cuarta iteración»*. **Un campo que vale 4 bajo un máximo de 3 no es un contador: es dos
> contadores con un solo nombre.** Se separan, y la contradicción desaparece sin cambiar ni
> un total de eventos.

```text
OBSERVACIÓN DE          cada DIVERGENCIA REAL que se detecta y que DEBE quedar registrada.
CONFLICTO               Es un HECHO OBSERVADO, y §2.6.4 lo produce siempre que un fichero no
                        casa ni con la base ni con el resultado. **No se silencia nunca.**

INTENTO DE              cada DECISIÓN DURABLE que se prepara para aplicar. Es un ACTO DE
RECONCILIACIÓN          AUTORIDAD, y es lo que consume presupuesto.

Y LA REGLA QUE LOS      **`MAX_CAS_RETRIES = 3` limita INTENTOS, no OBSERVACIONES.** Un tope
SEPARA                  sobre lo observado sería un tope sobre la realidad, no sobre el
                        trabajo — y obligaría a callar la divergencia que agota el último
                        intento, que es exactamente lo que §2.6.4 prohíbe.
```

**Los dos campos, cada uno en su fase:**

```text
`conflicto` LLEVA       `observacion`           1..4   qué divergencia es ésta
                        `intentos_consumidos`   0..3   cuántas decisiones se prepararon ANTES
                        `agotado`               true ÚNICAMENTE en la CUARTA observación
                        más los hashes y la copia íntegra de lo divergente (§2.6.9)

                        La relación entre los dos es fija y comprobable:
                            `intentos_consumidos` = `observacion` − 1

                        Con `agotado: true` el evento **NO admite ninguna
                        `reconciliacion-preparada` posterior**. Es lo que convierte la parada
                        en una propiedad del registro, y no en una promesa del runtime.

`reconciliacion-        `intento`               1..3   qué intento es éste
preparada` LLEVA        `resuelve`              el `id` del evento `conflicto` que resuelve
                        más la decisión y su resultado durable (los siete campos de §2.6.9)

                        **NUNCA existe un `intento: 4`.** No es que no se emita: es que el
                        contrato no lo admite y el validador lo rechaza.
```

```text
LA CORRESPONDENCIA      `reconciliacion-preparada(intento: n)` resuelve el `conflicto` con
                        `observacion: n`. Los dos números coinciden mientras el intento
                        existe — y la cuarta observación es precisamente la que ya no tiene
                        pareja.

QUÉ REGISTRA LA         **el FRACASO DEL TERCER INTENTO.** No es un intento más: es la prueba
CUARTA OBSERVACIÓN      observada de que el tercero no funcionó. Sin ella el diario diría que
                        se intentó tres veces y callaría cómo acabó la tercera.

DÓNDE EMPIEZA CADA      `observacion` en **1** —la primera colisión—; `intentos_consumidos`
CONTADOR                en **0** en esa primera colisión; `intento` en **1**. Ninguno empieza
                        en cero salvo `intentos_consumidos`, que cuenta hacia atrás lo ya
                        gastado y por eso empieza vacío.

MÁXIMOS EXACTOS         OBSERVACIONES  `conflicto`                   **4**
                        INTENTOS       `reconciliacion-preparada`    **3**
```

**Las secuencias completas, para que no haya que deducirlas:**

```text
ÉXITO INMEDIATO          preparada → confirmada → derivada
(ruta normal)            3 eventos

ÉXITO SIN NUEVAS         preparada
DIVERGENCIAS               → C  observacion 1 · intentos_consumidos 0
(k = 1)                    → RP intento 1
                           → reconciliada → derivada
                         5 eventos

ÉXITO TRAS 1 NUEVA       preparada
DIVERGENCIA                → C  observacion 1 · intentos_consumidos 0
(k = 2)                    → RP intento 1
                           → C  observacion 2 · intentos_consumidos 1
                           → RP intento 2
                           → reconciliada → derivada
                         7 eventos

ÉXITO TRAS 2 NUEVAS      preparada
DIVERGENCIAS               → C  observacion 1 · intentos_consumidos 0
(k = 3)                    → RP intento 1
                           → C  observacion 2 · intentos_consumidos 1
                           → RP intento 2
                           → C  observacion 3 · intentos_consumidos 2
                           → RP intento 3
                           → reconciliada → derivada
                         9 eventos

AGOTAMIENTO              preparada
(3 nuevas divergencias)    → C  observacion 1 · intentos_consumidos 0
                           → RP intento 1
                           → C  observacion 2 · intentos_consumidos 1
                           → RP intento 2
                           → C  observacion 3 · intentos_consumidos 2
                           → RP intento 3
                           → C  observacion 4 · intentos_consumidos 3 · agotado: true
                             ← PARADA. NO EXISTE RP4
                         8 eventos · marcador ABIERTO · escalado al Owner

                         `C` = `conflicto` · `RP` = `reconciliacion-preparada`
                         En las cuatro, `intentos_consumidos` = `observacion` − 1
```

**Qué fases pueden repetirse dentro de un `tx`, y cuáles no.** No es una excepción tolerada:
es parte del contrato, y el validador semántico del diario (§3.6, capa B) lo comprueba:

```text
COMO MUCHO UNA VEZ     `preparada`     exactamente 1 SIEMPRE —el `tx` ES su huella (§2.8):
POR `tx`, Y CUÁNTAS                    dos serían dos `tx`
EXACTAMENTE LO DICE    `confirmada`    1 en la ruta normal · 0 en la de conflicto
LA TABLA DE ARRIBA     `reconciliada`  0 en la ruta normal · 1 en la de conflicto CERRADA
                       `derivada`      1 si cerró · 0 si sigue abierta
                       Una SEGUNDA aparición de cualquiera de éstas es un DEFECTO, no una
                       reemisión. **`confirmada → confirmada` no existe.**

REPETIBLES, Y          `conflicto`                  discriminado por `observacion`, máx. 4
DECLARADAS COMO TAL    `reconciliacion-preparada`   discriminada por `intento`, máx. 3.
                       Cada una lleva SU contador, y no comparten uno.
                       Es la ÚNICA repetición que el contrato define, y la define en
                       positivo con su discriminador y su tope. Sin discriminador no hay
                       fase repetible.

LA REGLA, EN UNA       una fase de HECHO —`confirmada`, `reconciliada`, `derivada`— no puede
FRASE                  duplicarse NUNCA, y su presencia o ausencia la fija LA RUTA. Una fase
                       de INTENCIÓN sólo se repite si el contrato la declara repetible y le
                       da un discriminador. No hay más casos.
```

**Cómo se ejerce en el momento de escribir**, que es §2.8 punto 5 sin cambiar una coma: antes
de emitir, el ejecutor busca en el diario un evento con el **mismo `tx`** y la **misma
`fase`**; si existe, la operación es una **NO-OPERACIÓN**. Esa regla, que ya estaba escrita,
es exactamente lo que impide el segundo `confirmada` — y lo que la redacción anterior había
dejado de respetar.

### 2.6.5 · Todas las ventanas de caída

Se enumeran las **diecisiete** de la ruta normal y del ciclo de vida de la transacción. Las
**nueve de la reconciliación** viven en §2.6.9, junto al mecanismo que recuperan. Una ventana
que no está en ninguna de las dos tablas es un defecto de esa tabla — y las dos devoluciones
posteriores ejercieron esa invitación: la segunda añadió cinco, y la corrección técnica
posterior partió `W12` en dos, porque el mismo síntoma exige registros distintos según la
transacción esté abierta o cerrada (§2.6.11).

| # | la caída ocurre… | qué se observa al arrancar | qué se hace |
|---|---|---|---|
| W1 | antes de preparar | nada: ni evento ni marcador | nada que hacer. La transacción no existió |
| W2 | escribiendo el temporal de `preparada` | un temporal huérfano, sin evento | se borra el temporal. La transacción no existió |
| W3 | después de `preparada`, antes de tocar nada | evento `preparada`, todos los ficheros en previo | **se completa**: aplicar del primero al último |
| W4 | tras aplicar unos ficheros y no otros | mezcla de previos y posteriores | **se completa**: aplicar sólo los que casan con previo, en orden |
| W5 | tras aplicar todos, antes de `confirmada` | todos en posterior, sin `confirmada` | se emite `confirmada` y se sigue. No se reescribe nada |
| W6 | justo después de `confirmada` | `confirmada` presente, derivados sin regenerar | se regeneran los derivados y se emite `derivada` |
| W7 | durante la regeneración de derivados | derivados divergentes de su `source_revision` | se regeneran ENTEROS. Un derivado es reemplazable por definición |
| W8 | tras `derivada`, antes de borrar el marcador | transacción CERRADA con marcador abierto | se borra el marcador. Idempotente. **`derivada` es el único terminal**, luego «cerrada» y «terminal» vuelven a coincidir (§2.6.1) |
| W9 | antes del commit de Git | árbol coherente, Git por detrás | se hace el commit LOCAL. Es recuperación: protege el árbol y no publica (§2.6.10) |
| W10 | después del commit, antes del push | commit local sin publicar | **NO se empuja automáticamente.** El push es publicación, no recuperación: pasa a la política de §2.6.10 |
| W11 | en cualquier punto, con la transacción abierta y un fichero VERDADERAMENTE divergente | un fichero que no casa **ni con la base válida ni con el resultado permitido** de su intención vigente (§2.6.4) | **`conflicto`** —y las dos condiciones son necesarias: transacción abierta Y divergencia real—, con la copia íntegra de lo divergente. El predicado `reconciliacion_pendiente` **se deriva** de él (§2.6.9): no hay bandera que escribir. No se completa y no se revierte |
| **W12a** | caída de MÁQUINA tras el `rename` de un canónico, sin `fsync` de su directorio, con la transacción **TODAVÍA ABIERTA** —sin `derivada`— | uno o más canónicos revertidos a su hash previo | **NO es `conflicto`.** Casan con la BASE VÁLIDA de su intención vigente, luego son **NO APLICADO** y se **REAPLICAN** en el `orden` declarado, de forma idempotente (§2.6.4) — que es lo mismo que mandan `W3` y `W4` ante el mismo disco. Si `confirmada` ya era durable, **no se emite ninguna fase nueva**: el evento ya existe, se sigue con los derivados y con `derivada`, y **no hay `confirmada → confirmada`** (§2.6.4). Sólo hay `conflicto` si algún fichero no casa **ni con la base ni con el resultado**. **Corregido** (hallazgo `H2`) |
| **W12b** | lo mismo, con la transacción **YA CERRADA** —`derivada` durable— | ídem | **NO es `conflicto`**, y por el paso 0 de §2.6.4: `derivada` es terminal y ninguna transición sale de él. Se emite un evento **`deriva`** con `causa: posterior-al-cierre` (§2.6.11), que referencia la transacción sin reabrirla. Es el fallo silencioso del hallazgo `E`, y el hallazgo `2` corrige a dónde va |
| **W13** | **escribiendo el temporal de `confirmada`** | temporal huérfano, con todos los canónicos ya en posterior | **se emite `confirmada`, y es su PRIMERA emisión durable**: un temporal huérfano NO es un evento, luego `confirmada` no existe todavía (caso A de §2.6.4). NO se descarta la transacción: a diferencia de `W2`, aquí los canónicos YA están aplicados |
| **W14** | **creando el marcador (paso 2)** | `preparada` durable, marcador ausente o vacío | benigno: `W3` lo cubre por resultado. Se recrea el marcador desde el diario (§2.9) |
| **W15** | **el push es rechazado porque el remoto avanzó** | commit local, remoto divergente | evento `fallo`, tope de tres por §7.3, y se escala. **NUNCA `--force`** (§2.6.10) |
| **W16** | **el push se completa parcialmente** | unas referencias publicadas y otras no | evento `fallo` con las referencias nombradas. El estado local no cambia: el push no es una mutación canónica |

**Qué se completa, qué se revierte y qué se escala**, dicho en una frase cada uno:

```text
SE COMPLETA   toda transacción cuyo evento `preparada` es durable y ninguno de sus ficheros
              es divergente. W3 a W9, más W13 y W14.
SE REVIERTE   sólo lo que nunca llegó a comprometerse: un temporal huérfano de `preparada`
              (W2). No existe «deshacer» después del punto de compromiso, y por eso no se
              promete. W13 NO es una reversión: es la PRIMERA emisión durable de una
              `confirmada` que nunca llegó a existir.
SE ESCALA     todo lo VERDADERAMENTE divergente (W11), la deriva posterior al cierre que la
              integridad post-terminal destapa (W12b), el fallo de publicación (W15, W16),
              y todo lo que exija decidir. `b.14.3` y `R3`: DSP para y escala, NUNCA
              inventa estado.
              W12a NO ESTÁ AQUÍ, y es la corrección del hallazgo `H2`: un canónico revertido
              bajo una transacción abierta casa con su base válida, luego SE COMPLETA. Se
              REPORTA —el runtime nombra la ruta y el hash observado, porque una pérdida de
              durabilidad es un defecto que hay que ver— pero no se escala una decisión que
              es determinista.
```

### 2.6.6 · Seis garantías distintas que no son la misma

`a.9` habla de atomicidad y F4 entregada la usó como si fuera durabilidad. No lo es.

```text
1  ATOMICIDAD DE `rename`      un fichero nunca se lee a medias: o el contenido viejo o el
                               nuevo. NO garantiza que el nuevo sobreviva a un corte.

2  DURABILIDAD FRENTE A        basta con que el `rename` haya retornado: el contenido está
   CAÍDA DE PROCESO            en la caché del sistema y cualquier otro proceso lo ve. NO
                               exige `fsync`.

3  DURABILIDAD FRENTE A        exige `fsync` DEL FICHERO y `fsync` DEL DIRECTORIO. Sin el
   CAÍDA DE MÁQUINA            segundo, el `rename` puede perderse aunque el contenido esté
                               en disco. Es el error clásico, y aquí se nombra.

4  COMMIT LOCAL                el estado es recuperable desde `.git` aunque el árbol se
                               destruya. NO sobrevive a la pérdida del disco.

5  PUSH REMOTO                 sobrevive a la pérdida de la máquina entera.

6  RECONSTRUCCIÓN DESDE        sólo ve lo que se empujó. Y por la regla de Git de abajo,
   UN CLON NUEVO               un árbol publicado NUNCA contiene marcadores. Si un clon ve
                               uno, es EVIDENCIA DIAGNÓSTICA de un defecto del runtime que
                               publicó un árbol incoherente: se emite un evento **`fallo`**
                               de publicación, nombrando `tx` y commit, y se escala.
                               **NO se emite `conflicto`** —el clon no tiene ninguna
                               transacción abierta propia, y `conflicto` es una FASE de una
                               transacción (hallazgo `H2`)—.
                               **El marcador NUNCA es fuente para un clon.**
```

**Dónde es obligatorio `fsync`, y dónde deliberadamente no:**

```text
OBLIGATORIO   LAS DOS INTENCIONES, y por el mismo motivo:
              (1) el evento `preparada` y SU DIRECTORIO, ANTES de tocar ningún canónico
              (2) el evento `reconciliacion-preparada` y SU DIRECTORIO, ANTES de tocar
                  ningún canónico. Es el punto de compromiso de la ruta de conflicto, y sin
                  su durabilidad la reconciliación no es recuperable (hallazgo `1`, §2.6.9)

              CADA ESCRITURA CANÓNICA, venga de la ruta que venga:
              (3) cada fichero canónico escrito **Y SU DIRECTORIO**, ANTES de emitir
                  `confirmada` o `reconciliada` — y en el orden del paso 3 de §2.6.3:
                  `fsync(temporal)` ANTES del `rename`, `fsync(directorio)` DESPUÉS

              LOS DOS HECHOS:
              (4) el evento `confirmada` y SU DIRECTORIO
              (5) el evento `reconciliada` y SU DIRECTORIO
NO EXIGIDO    los derivados, el marcador y el evento `derivada`: los tres se reconstruyen
              desde lo canónico, y pagar `fsync` por ellos encarece cada transacción sin
              comprar ninguna garantía
```

> **Corregido dos veces.** La corrección técnica posterior extendió la lista a la ruta de
> conflicto: sólo nombraba `preparada`, y sin `fsync` de `reconciliacion-preparada` la
> reconciliación no sobrevive a una caída de máquina (hallazgo `1`).
>
> **Y antes, por la segunda devolución independiente (hallazgo `E`, BLOQUEANTE).** F4c exigía
> *«cada fichero canónico escrito, ANTES de emitir `confirmada`»* —**sin el directorio**— y §2.6.3 decía *«`fsync` del fichero antes del paso 4»*, es decir **después
> del `rename`**. Los dos son el mismo error, en el eje del alcance y en el del tiempo, y es
> **exactamente el que la garantía 3 acababa de nombrar como «el error clásico»**, cometido en
> el punto donde más importa: los ficheros que **son** el estado.
>
> **Y el fallo resultante era SILENCIOSO**, que es lo que lo hacía bloqueante. La recuperación
> clasifica ficheros en las tres cajas de §2.6.4 **sólo cuando encuentra una transacción sin
> evento terminal**. Si `confirmada` sobrevivió —y sobrevive: lleva sus dos `fsync`— la
> transacción es terminal, `W6` sólo regenera derivados y **nadie vuelve a comparar los hashes
> de los canónicos**. El diario afirmaba un cambio que el disco no tenía, y no había un solo
> mecanismo que lo desmintiera. **Ninguna de las diecisiete filas de §2.6.7 lo detectaba**:
> `X01`–`X03` matan el proceso, no la máquina, y ninguna cortaba la corriente. Es `D36`.

### Comprobación de integridad post-terminal

Los cuatro puntos anteriores dependen de que la implementación no tenga defectos. **Ésta es la
comprobación que convierte un fallo silencioso en un fallo detectado**, y sin ella lo demás es
una promesa:

> **Corregida por la devolución técnica previa (hallazgo `5`, GRAVE).** Decía «toda
> transacción cuyo evento terminal sea `confirmada` o `derivada`» —y `confirmada` **no es
> terminal**—, no contemplaba los hashes finales de una reconciliación, y usaba «respaldado
> por Git» como si equivaliera a «el fichero actual es correcto». **No equivale**: un commit
> demuestra qué se guardó, no qué hay hoy en el árbol de trabajo.

```text
QUÉ ES UNA VENTANA   el conjunto de transacciones cuyo evento `derivada` NO está incluido
DE COMMIT            todavía en ningún commit de Git. Se delimita por el último commit que
                     registró un árbol sin marcadores abiertos — que por la regla de Git de
                     §2.6.6 es el único que ADS produce.

QUÉ TRANSACCIONES    TODAS las de la ventana, ABIERTAS Y CERRADAS. Las abiertas, porque su
SE COMPRUEBAN        recuperación depende de ello; las cerradas, porque su `derivada` afirma
                     un resultado que el disco puede haber dejado de sostener. Lo que cambia
                     entre unas y otras no es SI se comprueban, sino DÓNDE se registra el
                     fallo: `conflicto` en las abiertas, `deriva` en las cerradas.

QUÉ HASH SE USA      · ruta normal:      el `hash_posterior_esperado` de `preparada`
                     · ruta de conflicto: el `hash_final` que declara
                       `reconciliacion-preparada`, que SUSTITUYE al anterior para los
                       ficheros que la reconciliación tocó (§2.6.9). Lo declara la INTENCIÓN,
                       no el hecho: por eso está disponible aunque la caída ocurra antes de
                       `reconciliada`

CÓMO SE VERIFICA     comparando el árbol de trabajo contra `HEAD` **para las rutas canónicas
QUE LOS CANÓNICOS    de `estado/`**, no para el repositorio entero. Es una comparación
COINCIDEN CON HEAD   explícita, no una suposición: «respaldado por Git» describe la historia,
                     no el disco de ahora.

ÁRBOL DIVERGENTE     es un evento `deriva` con `causa: sin-transaccion` (§2.6.11): alguien
SIN TRANSACCIÓN      editó un canónico fuera del protocolo. NO es un conflicto —no hay
ABIERTA              transacción que reconciliar— y no tiene `preparada` con el que
                     compararlo; el hash esperado es el de `HEAD`.
                       · se REPORTA, nombrando ruta, hash observado y hash en `HEAD`
                       · NO se completa, NO se revierte y NO se restaura sola
                       · se ESCALA, como toda inconsistencia irresoluble sin decidir (b.14.3)

CUÁNDO SE RESTAURA   NUNCA de forma automática. Restaurar desde Git DESTRUYE el contenido
DESDE GIT, Y CON     que hay en el árbol, y ese contenido es de alguien —es el mismo
QUÉ AUTORIDAD        argumento de §2.6.4—. La restauración es **decisión del Owner**, y deja
                     su evento con los cinco conceptos de `a.9`.

QUÉ HACE SI NO CASA  DEPENDE DE SI LA TRANSACCIÓN SIGUE ABIERTA, y la distinción es de
                     identidad, no de grado (§2.6.11):

                       TRANSACCIÓN ABIERTA    —sin `derivada`— se CLASIFICA por §2.6.4
                       (W12a)                 contra su intención vigente, y NO se salta a
                                              `conflicto`:
                                                · casa con la BASE     → NO APLICADO → se
                                                  REAPLICA. Si `confirmada` era durable NO
                                                  se emite ninguna fase nueva: se sigue con
                                                  los derivados y con `derivada`
                                                · casa con el RESULTADO → nada que hacer
                                                · no casa con ninguno  → **entonces sí**
                                                  `conflicto`, una FASE suya, y con él el
                                                  predicado `reconciliacion_pendiente` de
                                                  §2.6.9, sin escribir en ningún item
                                              **Corregido** por el hallazgo `H2`: antes
                                              mandaba `conflicto` para el primer caso, que
                                              es el que `W3` y `W4` completan

                       TRANSACCIÓN CERRADA    —`derivada` durable— **NO** es `conflicto`:
                       (W12b)                 ninguna transición sale del terminal. Es un
                                              evento `deriva` con `causa:
                                              posterior-al-cierre`, que la REFERENCIA sin
                                              reabrirla

                     Un canónico que revirtió bajo una `derivada` durable es indistinguible,
                     desde el estado, de uno que alguien tocó — y las dos cosas exigen lo
                     mismo: parar y escalar. Lo que cambia es DÓNDE se registra.
                     BAJO UNA TRANSACCIÓN ABIERTA no ocurre lo mismo, y ésa es la asimetría
                     que el hallazgo `H2` corrige: allí SÍ existe una intención durable que
                     declara a qué resultado hay que llegar y con qué mecanismo, luego el
                     resultado es determinista y se completa. Después del cierre esa
                     intención ya se consumió, y no queda nada que completar
```

**La regla de Git, que cierra W9 y W10:** **ADS nunca hace commit de un árbol con una
transacción abierta.** El commit se hace entre transacciones. Por tanto un árbol publicado
**nunca contiene una transacción a medias**, y un clon nuevo nunca tiene que completar una
transacción que no preparó. Si un clon encuentra un marcador `.abierta`, es que se empujó
un árbol incoherente: eso es un **defecto del runtime**, y se registra como tal.

**Qué se emite exactamente ante un marcador que no debería existir**, corregido por el
hallazgo `H2` — porque `conflicto` exige **una transacción abierta válida Y un fichero
verdaderamente divergente**, y aquí no hay ni lo uno ni, necesariamente, lo otro:

```text
MARCADOR EN UN ÁRBOL      DEFECTO DE PUBLICACIÓN. Evento **`fallo`**, con `operacion:
CLONADO                   publicacion`, el `tx` y el commit culpable nombrados. El clon NO
                          completa la transacción ajena, NO emite ninguna fase con ese
                          `tx` —no es suyo— y NO borra el marcador en silencio.

MARCADOR HUÉRFANO         el marcador nombra un `tx` que el diario no tiene. Evento
—SIN SU `preparada`       **`fallo`** con el mismo diagnóstico: es un defecto de escritura
EN EL DIARIO—             o de publicación, no un conflicto. Reconstruir desde el diario
                          (§2.9) da CERO transacciones abiertas, y el marcador se retira
                          registrando por qué.

CANÓNICO DIVERGENTE       evento **`deriva`** con `causa: sin-transaccion` (§2.6.11). No
SIN TRANSACCIÓN           hay `preparada` contra la que comparar; el hash esperado es el de
ABIERTA                   `HEAD`.

`conflicto`               SÓLO con transacción abierta válida EN ESTA INSTALACIÓN y un
                          fichero que no casa ni con la base ni con el resultado de su
                          intención vigente. Fuera de eso, emitirlo sería **inventar una
                          transición**, que es lo que `b.14.3` prohíbe con otras palabras.
```

> **Corregido por la segunda devolución independiente (hallazgo `F`).** La garantía 6 decía
> *«los marcadores `.abierta` sí, porque están versionados»*, enunciando como **propiedad
> normal del sistema** un estado que la regla de Git, dos párrafos después, declara
> **imposible salvo por defecto del runtime**. Si el commit sólo ocurre entre transacciones,
> el marcador **nace y muere entre dos commits** y por construcción nunca entra en un árbol
> publicado. `X15` ya trataba el caso como evidencia diagnóstica, que es la lectura correcta;
> la garantía 6 lo trataba como **fuente**, que es la incorrecta.
>
> **Y hay un segundo defecto, más incómodo.** Aplicando el criterio de §2.4 al propio
> marcador —*¿sobrevive a un clon nuevo?*— la respuesta es **no**: §2.9 lo declara
> reconstruible y «un acelerador, no una verdad». Por el criterio del propio documento **es
> operacional**. F4c lo colocaba en `estado/tx/`, dentro de lo que §1.2 y §2.4 declaran
> «DURABLE Y VERSIONADO: todo `estado/`». El documento violaba su propio criterio de
> clasificación en la única pieza a la que ese criterio debería aplicarse sin discusión.

**Dónde vive el marcador, resuelto.** Se conserva en `estado/tx/` **y se excluye de Git**:

```text
POR QUÉ NO SE MUEVE A     porque el hallazgo `A` exige que sea LEGIBLE SIN HERRAMIENTA junto
`.ads/run/`               al estado que califica. Un aviso de «esto no es fiable» que vive en
                          un directorio operacional que el lector no tiene por qué mirar no
                          es un aviso.

CÓMO SE IMPIDE QUE        exclusión explícita en `.gitignore` del control repo. **Es
VIAJE                     OPERACIONAL** —§2.4 y `D50`— y está bajo `estado/` por una
                          EXCEPCIÓN DE RUTA declarada, no por su naturaleza. No hay tercera
                          categoría: hay dos, y una excepción de ubicación con su motivo.

QUÉ SIGUE SIENDO CIERTO   se reconstruye desde el diario (§2.9), luego borrarlo no pierde
                          nada, y sigue sin ganar identidad propia: §3.1 paso 4 sigue dando
                          COMPONER.

QUÉ LLEGA A GIT, EN       NADA de `estado/tx/`. Declarado en positivo, y `X27` lo comprueba
POSITIVO                  recorriendo la historia entera.
```

### 2.6.7 · Tabla adversarial de recuperación

**Convertible en pruebas de F6 sin traducción.** Cada fila declara qué se prepara, dónde se
interrumpe, qué debe observarse y qué diagnóstico exacto debe emitirse. **Trece filas se
añadieron tras la segunda devolución independiente**, que encontró que ninguna de las
diecisiete originales detectaba una caída de máquina. Una fila que
termine con una traza cuenta como **NO detectada**, que es la disciplina que `N158*` ya
impuso al arnés de negativos.

| | escenario adversarial | resultado exigido |
|---|---|---|
| `X01` | matar el proceso entre `preparada` y el primer fichero | converge al mismo estado que una ejecución sin interrupción (T17) |
| `X02` | matar el proceso entre el fichero 2 y el 3 de cinco | los cinco quedan en posterior, en el orden declarado |
| `X03` | matar el proceso entre el último fichero y `confirmada` | se emite `confirmada`; ningún fichero se reescribe |
| `X04` | ejecutar la recuperación DOS VECES seguidas | la segunda es una no-operación. Idempotencia por hash |
| `X05` | modificar a mano un fichero de la transacción entre `preparada` y la recuperación, **a un contenido que no es ni su base ni su resultado** | `conflicto` con el fichero NOMBRADO: hay transacción abierta y divergencia real, que son las DOS condiciones. No se sobrescribe |
| `X06` | borrar un fichero cuyo `hash_previo` no es `ausente`, **con su transacción abierta** | `conflicto`: no existir es DIVERGENTE cuando el evento declara un hash concreto (§2.6.4), y hay transacción abierta. No se recrea desde el hash |
| `X07` | corromper un evento `preparada` a medio escribir | se identifica como temporal huérfano y se descarta. La transacción no existió |
| `X08` | dos ejecutores preparan transacciones que tocan el mismo fichero | el segundo encuentra el marcador `.abierta` y **no arranca**: `R5` es un lock, no un consejo |
| `X09` | dos ejecutores en máquinas distintas emiten eventos a la vez | ids distintos por contenido. La cadena BIFURCA, y la bifurcación se DETECTA. No se resuelve sola |
| `X10` | matar el proceso durante la regeneración de derivados | derivados regenerados enteros; ningún canónico tocado |
| `X11` | editar a mano un derivado y arrancar | se regenera encima. Un derivado no es una fuente (I5) |
| `X12` | matar el proceso entre `confirmada` y el commit de Git | se hace el commit. El estado ya era verdad |
| `X13` | perder `.ads/run/` entero | se reconstruye. Ninguna transacción se pierde: el diario es durable |
| `X14` | borrar el marcador `.abierta` de una transacción en vuelo | el arranque la encuentra recorriendo el diario. El marcador es un acelerador |
| `X15` | clonar de nuevo un remoto empujado en medio de una transacción | evento **`fallo`** de publicación, nombrando `tx` y commit, y escalado. **NUNCA `conflicto`**: el clon no tiene transacción abierta propia, y una fase de una transacción ajena no se emite. Nunca se completa una transacción ajena |
| `X16` | una operación declarada `operacion` que NO es determinista | el hash posterior no casa al prepararla → la transacción **no llega a preparar** |
| `X17` | un evento sellado al que apunta un evento vivo | el sellado **no lo retira**. Ver §2.9 |
| `X18` | suspender el ejecutor con `SIGSTOP` entre el fichero 3 y el 4, y leer los cinco desde fuera | el lector declara «transacción abierta; estas cinco rutas no son fiables», **nombrando las cinco y sin recorrer el diario** (§2.6.8) |
| `X19` | aplicar 2 de 5, modificar el 4 externamente, recuperar, **reiniciar y ejecutar `Continúa`** | `Continúa` se detiene en `reconciliacion-pendiente` nombrando items y fichero divergente, **antes** de regenerar derivados y **antes** de seleccionar trabajo. Borrar el marcador a mano y repetir: diagnóstico idéntico |
| `X20` | dar la misma entrada a **dos implementaciones independientes** del serializador, con claves invertidas, `\r\n` y un mapa anidado | ambas producen **el mismo `tx` y el mismo `id`** (§2.8) |
| `X21` | preparar, matar antes del `rename`, reintentar; y después forzar una recuperación con `confirmada` YA durable | existe **un solo `tx`** en el diario, aunque los `id` difieran; **ninguna secuencia contiene `confirmada → confirmada`**; y restaurar un evento durable perdido devuelve el **mismo `id`, el mismo cuerpo y el mismo `predecesor`**, sin que el diario crezca |
| `X22` | cambiar el formato de presentación del diario sin cambiar el contenido | **ningún identificador cambia**. Si cambian, §2.11 y §2.8 son incompatibles |
| `X23` | recorrer todos los caminos del protocolo buscando `fase: abortada` | **ninguno la produce**, y el **esquema estructural** **rechaza** un evento con esa fase: es un valor fuera del enum, y eso se ve en el evento aislado |
| `X25` | **corte de alimentación forzado** tras el `rename` de `confirmada` | los cinco canónicos casan con su `hash_posterior_esperado`. Es la caída de MÁQUINA, que `X01`–`X03` no cubrían |
| `X26` | inyectar la reversión de dos canónicos con `confirmada` presente y **sin `derivada`** | el arranque **lo detecta y nombra los dos ficheros** en vez de regenerar derivados encima, los clasifica como **NO APLICADO** —casan con su `hash_previo`— y los **REAPLICA** desde `preparada` y **NO emite ninguna fase nueva** —`confirmada` ya existe—, siguiendo con los derivados y con `derivada`. **No emite `conflicto`, no duplica `confirmada` y no pide ninguna decisión**: el resultado es determinista |
| `X27` | recorrer la historia entera del control repo tras N transacciones | **ningún commit** contiene un fichero bajo `estado/tx/` |
| `X28` | fabricar a mano un commit con marcador abierto, publicarlo y clonar | el clon emite **`fallo`** de publicación, **escala como defecto del runtime** y **no completa nada**, nombrando `tx` y commit culpable. **No emite `conflicto` ni ninguna otra fase** |
| `X37` | interrumpir una transacción, avanzar el remoto desde otro clon, arrancar la recuperación | se completa, el commit local se hace, el push **no se fuerza**, se emite `fallo` con el diagnóstico «el remoto avanzó» y se escala |
| `X38` | recuperación con la `main` del control repo protegida | la recuperación **no intenta** empujar sobre ella |
| `X39` | commit y push de recuperación | dejan evento con **los cinco conceptos de `a.9`** completos; la ausencia de cualquiera es un fallo del validador, no un silencio |
| `X47` | resolver la **proyección normativa VIGENTE** del enum de `evento.fase` aplicando la cadena de sustituciones `D38 → D46 → D52`, y compararla con §2.6.1 y §3.6 | **coinciden**, y un evento con `fase: abortada` es **rechazado por el esquema estructural**, que para un enum basta. La prueba NO recorre el corpus entero buscando una sola enumeración: los registros de decisión y los documentos de crítica **conservan deliberadamente los enums sustituidos**, y esa historia es lo que hace auditable la cadena. Las excepciones son exactamente ésas, y están declaradas abajo |
| `X48` | aplicar una transacción completa y comparar cada canónico con su `hash_posterior_esperado` | casan **byte a byte**. Ningún mecanismo de detección —marcador, regla de lectura o diario— modifica el contenido canónico |
| `X49` | provocar un conflicto y evaluar `b.4` P0 sobre los items afectados | devuelve `reconciliacion-pendiente` **sin que se haya escrito un byte en ningún `03-integracion.md`** y sin que exista un segundo marcador |
| `X50` | reconciliar un conflicto de cinco ficheros | los derivados se regeneran **antes** de `derivada`, el marcador sobrevive hasta `derivada`, y los canónicos casan con los `hash_final` de `reconciliada` |
| `X51` | editar un canónico fuera del protocolo, sin transacción abierta, y arrancar | se declara **deriva no transaccional**, nombrando ruta, hash observado y hash en `HEAD`. NO se completa, NO se revierte y NO se restaura sola |
| `X52` | comparar el censo de pruebas de §9.1, §9.5 y `nivel-certificacion` para cada nivel | los tres conjuntos son **idénticos**. Una diferencia de censo es un fallo |
| `X53` | buscar un `contrato-de-aspecto` de familia `certificacion`, y campos de certificación declarados dos veces | **no existe ninguno**, y ningún campo de certificación tiene dos sedes normativas |
| `X54` | matar la máquina en cada una de las nueve ventanas `R1`–`R9` de la reconciliación | en `R1` y `R2` la decisión se pierde y el conflicto sigue abierto, **sin un solo canónico tocado**; de `R3` a `R9` la reconciliación **converge al mismo resultado** que una ejecución sin interrupción |
| `X55` | comprobar que **ninguna escritura de reconciliación precede a su intención durable** | para todo canónico tocado por una reconciliación, el `fsync` de `reconciliacion-preparada` y de su directorio **retornó antes** del primer `rename` |
| `X56` | revertir un canónico de una transacción con `derivada` durable, y arrancar | se emite un evento **`deriva`** con `causa: posterior-al-cierre`. **NO** se emite ninguna fase, la transacción cerrada **no gana ningún evento nuevo con su `tx`**, y nada se restaura solo |
| `X57` | recorrer el diario buscando cualquier evento con `fase` cuya transacción ya tenga `derivada` | **no existe ninguno**, y el **validador semántico del diario** lo rechaza —la comprobación es de `tx`, no de evento aislado (§3.6)—. Ninguna transición sale del terminal |
| `X58` | provocar que un fichero diverja y **vuelva a divergir TRES veces más** durante la reconciliación | el diario queda con **CUATRO observaciones y TRES intentos**: los `conflicto` llevan `observacion` 1..4 con `intentos_consumidos` = `observacion` − 1, el cuarto lleva **`agotado: true`**, y las `reconciliacion-preparada` llevan `intento` 1..3. **NO existe ningún `intento: 4`**, se **detiene y se escala al Owner**, y la transacción queda ABIERTA con su marcador |

> **Las excepciones históricas de `X47`, declaradas una a una.** Estos textos conservan
> deliberadamente enumeraciones sustituidas, y `X47` **no los cuenta como incumplimiento**:
>
> ```text
> DECISIONES-Y-CONTRADICCIONES.md   `D23` y `D38` citan el enum de cuatro fases con
>                                   `abortada`. Es el registro de lo que se decidió, y
>                                   `D46` y `D52` lo revisan sin reescribirlo
> 12-CRITICA-INDEPENDIENTE-F4.md    la primera crítica, con el enum de su momento
> 13-SEGUNDA-CRITICA-INDEPENDIENTE  el hallazgo `D` cita `abortada` para pedir su retirada
> 14-DEVOLUCION-TECNICA-PREVIA-F4C  el hallazgo `1` cita las cinco formulaciones que
>                                   encontró, incluida la que conservaba `abortada`
> §2.6.1 y §15.8 de este documento  las notas de corrección citan lo que sustituyen
> ```
>
> **La regla, en una frase:** la proyección normativa vigente es UNA; las citas históricas y
> adversariales son MUCHAS, y eliminarlas destruiría la trazabilidad que estos documentos
> existen para dar. `X47` comprueba la primera y declara las segundas.

> **Cuarenta y dos filas físicas y cuarenta y dos identificadores únicos**, comprobado por
> conteo sobre el fichero y no por memoria: la tabla empieza en `X01`, salta `X24` con su
> motivo declarado abajo, y **ninguna fila se repite**. La segunda corrección técnica revisó
> `X05`, `X15`, `X26` y `X28` **en su sitio**, sin añadir ninguna fila y sin retirar ninguna.
>
> **Y dos restos señalados que NO se reproducen, dicho porque corregir lo que no existe sería
> peor que no corregirlo** —es la misma disciplina del hallazgo `11` de la devolución
> técnica previa:
>
> ```text
> «dos filas idénticas X28»      NO REPRODUCIDO. `X28` aparece UNA sola vez en el fichero, y
>                                el conteo da 42 filas de datos con 42 ids distintos. Lo que
>                                puede haber inducido el recuento a 43 es la fila SEPARADORA
>                                del Markdown, que no es un escenario
> «"Un fichero que no existe"    NO REPRODUCIDO. Un barrido literal sobre todo `docs/`
>  dos veces en §2.6.4»          devuelve UNA sola aparición
> ```
>
> **Ninguna se ha ejecutado.** Cuarenta y dos filas escritas es el contrato de lo que F6 debe
> demostrar, y **no es su demostración**. Trece son de la segunda devolución independiente,
> siete de la devolución técnica previa (`X47`–`X53`) y **cinco de la corrección técnica
> posterior** (`X54`–`X58`). `X24` no existe porque su hallazgo —`D`— se resolvió retirando
> el estado en vez de darle un disparador. **Y las nueve ventanas `R1`–`R9` de §2.6.9 son
> contrato de prueba igual que éstas**, aunque vivan junto al mecanismo que recuperan.


### 2.6.8 · La regla de lectura — lo que se garantiza es DETECTABILIDAD, no aislamiento

> **Añadida por la segunda devolución independiente (hallazgo `A`, GRAVE).** F4c escribía
> *«desde este registro, y no antes, un lector del estado puede creerse lo que lee»* y no
> tenía **ninguna regla dirigida a ningún lector**. Era una descripción del estado del diario,
> no una barrera. La única entidad que comprobaba era el runtime, en `Continúa` paso 2 — y
> `R1` existe precisamente para que haya lectores que no son el runtime.

**La ventana existe y es observable.** Entre el primer `rename` del paso 3 y el `confirmada`
del paso 4, los ficheros canónicos contienen una **mezcla** de estado previo y posterior. No
se elimina: se **declara**, se **detecta** y se **dice**.

```text
LO QUE NO SE OFRECE     AISLAMIENTO DE LECTURAS. Ningún lector obtiene una vista consistente
                        de un instante anterior. Eso exigiría versiones múltiples de cada
                        canónico, y con ello un almacén que `R1` no admite.

LO QUE SÍ SE OFRECE     DETECTABILIDAD DE LA VENTANA. Ningún lector puede leer una mezcla
                        SIN SABER que la está leyendo.
```

**La regla, del mismo rango que la de escritura y dirigida a TODO lector** —humano, agente o
herramienta, sea o no el runtime:

```text
1  ANTES DE LEER EL ESTADO CANÓNICO, se comprueba `estado/tx/`.
2  SI HAY ALGÚN MARCADOR, la lectura de los ficheros que esa transacción declara es
   **NO FIABLE**, y quien lee DEBE declararlo. No es una recomendación de prudencia: una
   lectura silenciosa de una ventana abierta es un defecto de quien lee.
3  LOS DEMÁS FICHEROS se leen con normalidad. Una transacción abierta no invalida el estado
   entero: invalida exactamente las rutas que declara.
```

**Tres cosas cambian para que la regla sea ejecutable sin herramienta**, que es lo que `R1`
exige:

```text
EL MARCADOR LLEVA        `estado/tx/<TX-ID>.abierta` deja de estar «sin contenido» y declara
CONTENIDO                el `tx` y LA LISTA DE RUTAS AFECTADAS. F4c obligaba a recorrer
                         `estado/eventos/` para saber QUÉ ficheros estaban en vuelo — es
                         decir, a REPROYECTAR EL DIARIO para saber si podía creerse el
                         estado, que es exactamente el coste con el que §2.2 descarta la
                         alternativa C. F4 pagaba el coste de C sin haber elegido C.
                         Sigue siendo RECONSTRUIBLE desde el diario, luego no gana identidad
                         propia y el paso 4 de §3.1 sigue dando COMPONER.

EL DIARIO ES LA FUENTE   el marcador acelera; el diario RECONSTRUYE. Si el marcador falta,
DE RECONSTRUCCIÓN        el evento `preparada` de la transacción declara las mismas rutas, y
                         §2.9 lo dice: una transacción sin evento `derivada`.

NADA SE ESCRIBE EN EL    **corregido por la devolución técnica previa (hallazgo `2`,
CONTENIDO CANÓNICO       BLOQUEANTE).** El texto anterior exigía escribir `tx_abierta:
                         TX-<id>` EN LA CABECERA de cada canónico afectado y retirarlo al
                         confirmar. Rompía seis cosas a la vez:

                           1  el contenido con `tx_abierta` NO CASA con el
                              `hash_posterior_esperado` que `preparada` declara
                           2  retirarlo exige una SEGUNDA escritura de todos los ficheros
                           3  esa retirada es, ella misma, otra TRANSICIÓN MULTIARCHIVO
                           4  el paso APLICAR describe UNA escritura, no dos
                           5  CONFIRMAR emite un evento y NO retira cabeceras
                           6  «lo escribe al preparar» contradice que PREPARAR no toca
                              ningún canónico

                         **La detectabilidad NO exige contaminar el contenido canónico.** Se
                         sostiene sobre las tres piezas de arriba —regla de lectura,
                         marcador con contenido y diario—, y ninguna toca un solo byte de un
                         fichero canónico. Es `D48`.

`R3` SE CUALIFICA        §2.2 marcaba la opción D con «`R3` atomicidad y recuperación: sí».
EN §2.2                  **La atomicidad lógica multiarchivo NO se afirma.** Se afirma
                         RECUPERABILIDAD, IDEMPOTENCIA y DETECTABILIDAD, que es lo que `a.9`
                         pide con esas palabras: «recuperable e idempotente».
```

**Qué NO cambia, y estaba bien.** `b.14 Continúa` **sí** estaba cubierto y sigue estándolo:
§7.4 comprueba las transacciones abiertas y los pasos 1–4 son deterministas. La reanudación
**no** reanuda desde estado parcial, y esa mitad de la objeción no procedía.

### 2.6.9 · `conflicto` y `reconciliada` — sin transacción recursiva, y con regeneración

> **Corregido por la devolución técnica previa (hallazgos `3` y `4`, BLOQUEANTE y GRAVE).**
> El texto anterior tenía dos defectos que se anulaban entre sí:
>
> ```text
> RECURSIÓN IMPOSIBLE   decía que al escribir `conflicto` la transacción marca
>                       `reconciliacion_pendiente` en cada `03-integracion.md` «DENTRO DE UNA
>                       TRANSACCIÓN PROPIA». Pero la transacción original SIGUE ABIERTA y su
>                       marcador bloquea: `X08` dice que un segundo ejecutor «encuentra el
>                       marcador y NO ARRANCA: R5 es un lock, no un consejo». **El protocolo
>                       necesitaba abrir otra transacción para registrar el estado que
>                       impide abrir otra transacción.**
>
> CIERRE PREMATURO      declaraba `reconciliada` «terminal», y a la vez su decisión puede
>                       conservar lo divergente, aplicar lo preparado o elegir un tercer
>                       contenido — cualquiera de las cuales CAMBIA los canónicos. Los
>                       derivados estaban bloqueados durante el conflicto, y **nadie los
>                       regeneraba nunca**.
> ```

#### `reconciliacion_pendiente` es un PREDICADO DERIVADO, no una bandera que se escribe

```text
reconciliacion_pendiente(item) ≡
    existe una transacción con evento `conflicto` SIN evento `reconciliada` NI `derivada`,
    cuyo evento `conflicto` NOMBRA ese item
```

**El predicado NO distingue si el bucle se agotó, y es deliberado.** Un `conflicto` con
`agotado: true` sigue siendo un `conflicto` sin `reconciliada` ni `derivada`, luego el
predicado sigue siendo verdadero y el item sigue bloqueado — que es lo correcto: agotar los
intentos **no resuelve nada**. Lo que sí cambia es **quién puede desbloquearlo**:

```text
SIN AGOTAR            la autoridad del conflicto prepara el siguiente intento, dentro de los
(observaciones 1–3)   tres. El sistema sigue solo.

AGOTADO               **sólo el OWNER**, y con una decisión nueva. El sistema NO prepara un
(observación 4)       cuarto intento, y `reconciliacion_pendiente` sigue siendo verdadero
                      hasta que esa decisión llegue. Un predicado que se volviera falso al
                      agotarse desbloquearía el despacho justo cuando menos debe.
```

```text
POR QUÉ FUNCIONA        el evento `conflicto` YA CONOCE los items y las rutas afectadas: los
                        declara al emitirse. No hace falta escribir nada en ningún item para
                        saber que están afectados.

QUIÉN LO CONSUME        `b.4` P0 y §3.3.1 `Q0`, directamente. Ninguno de los dos necesita una
                        bandera persistida: necesitan un PREDICADO, y aquí lo tienen.

QUÉ SE EVITA            mutar los items durante un conflicto — que exigiría una transacción,
                        que está bloqueada por el marcador de la transacción en conflicto.
                        **Cero transacciones recursivas.**

COSTE                   recorrer los eventos `conflicto` sin terminal. Son los que el
                        marcador ya señala, luego el coste es el de leer los marcadores
                        abiertos y sus eventos: acotado y pequeño.

SI ALGUIEN QUISIERA     tendría que declarar una EXCEPCIÓN TRANSACCIONAL COMPLETA que no
PERSISTIR LA BANDERA    colisione con el bloqueo — quién la concede, sobre qué ficheros, con
                        qué garantías y cómo se recupera. «Dentro de una transacción propia»
                        NO es esa declaración, y por eso no se conserva.
```

#### `conflicto` — abierto y bloqueante, que NO es absorbente

```text
NO ES TERMINAL         no admite `confirmada` ni `derivada`. Sólo avanza a
                       `reconciliacion-preparada`, que es el punto de compromiso de esta
                       ruta; `reconciliada` viene DESPUÉS y nunca directamente desde aquí.
                       **Corregido** (hallazgo `C4`): decía «sólo avanza a `reconciliada`»,
                       que era el autómata anterior a `D52` y saltaba la única fase que hace
                       recuperable la reconciliación.

EL MARCADOR NO SE      mientras la transacción no llegue a `derivada`. `W8` sólo retira el
BORRA                  marcador de una transacción CERRADA, y `conflicto` y `reconciliada`
                       no lo están.

QUÉ BLOQUEA            todo despacho sobre los items afectados, y toda regeneración de
                       derivados que dependan de sus canónicos. No bloquea el resto del
                       producto: el conflicto tiene alcance, y su evento lo declara.

QUIÉN LO RESUELVE      el PROPIETARIO GLOBAL del item, si el conflicto afecta a uno solo.
                       El OWNER, si atraviesa varios items. «Se escala» no nombraba
                       autoridad, y el resto del corpus siempre la nombra —`a.5` en el veto,
                       `b.15.1` en los desbloqueadores, `C7` en cada operación Git.

CÓMO SE CONSERVA LO    el evento `conflicto` registra, POR FICHERO DIVERGENTE, su HASH ACTUAL
DIVERGENTE             OBSERVADO y una COPIA ÍNTEGRA en el cuerpo del evento —§2.6.2 ya
                       admite `contenido` dentro del evento: es el mismo mecanismo—. Sin
                       esto, quien resolviera podría destruir ese contenido sin que quedara
                       constancia de qué había.

QUÉ DECLARA ADEMÁS     los ITEMS y las RUTAS afectados. Es lo que hace derivable el predicado
                       de arriba sin escribir en ningún item.
```

> **Por qué el término cambia, y qué se conserva.** `D35` y las devoluciones que lo
> registraron dicen **«abierto y absorbente»**, y ese texto **no se reescribe**: es el
> registro de lo que se decidió. Pero la palabra describe mal lo vigente. **Absorbente** es,
> en un autómata, el estado del que no sale ninguna transición — y de `conflicto` sale una
> (`reconciliacion-preparada`), y además puede volver a entrarse en él hasta tres veces. Lo
> que el término quería decir es que `conflicto` **no se resuelve solo y detiene el
> despacho**, y eso es **abierto y bloqueante**. La norma vigente usa ese término; la
> historia conserva el anterior.

#### `reconciliacion-preparada` — la intención durable, ANTES de tocar nada

> **Añadida por la corrección técnica posterior (hallazgo `1`, BLOQUEANTE).** El texto
> anterior hacía que `reconciliada` declarase la decisión **y** la diera por aplicada. Tres
> ventanas quedaban sin cubrir, y en las tres el diario **no contenía la decisión**:
>
> ```text
> caída después de decidir y antes del primer fichero   → la decisión se pierde entera
> caída tras modificar algunos de los N ficheros        → estado mezclado, y nada declara
>                                                         a qué resultado había que llegar
> caída tras modificarlos todos, antes de `reconciliada` → indistinguible del anterior
> ```
>
> Y el `preparada` original **no sirve como respaldo**: declara el `hash_posterior_esperado`
> de la transacción, no la decisión de la reconciliación, que puede ser **conservar lo
> divergente** o **un tercer contenido**. Es el mismo defecto que `preparada` existe para
> cerrar en la ruta normal, sin cerrar en la de conflicto.

**Lleva SIETE cosas, y todas ANTES de escribir un solo byte canónico:**

```text
1  LA DECISIÓN, FICHERO A       conservar lo divergente · aplicar lo preparado · un tercer
   FICHERO                      contenido decidido. Explícita por ruta, no global.

2  LA AUTORIDAD QUE LA TOMÓ     el propietario global del item, o el Owner si el conflicto
                                atraviesa varios (abajo). Con los cinco conceptos de `a.9`.

3  BASE OBSERVADA POR FICHERO   `hash_observado` — lo que HAY en disco en el momento de
                                decidir. NO es el `hash_previo` de `preparada`: el fichero
                                divergente ya no está en ninguno de los dos hashes de la
                                transacción original, y ése es justo el motivo del conflicto.

4  CÓMO SE PRODUCE EL           una de `contenido` | `parche` | `operacion`, reproducible.
   RESULTADO                    Aplicarla a la base observada tiene que dar el hash final, y
                                eso se comprueba ANTES de escribir nada.

5  HASH FINAL ESPERADO          `hash_final` por fichero. Es el que gobierna a partir de aquí,
   POR FICHERO                  y SUSTITUYE al `hash_posterior_esperado` para esos ficheros.

6  ORDEN TOTAL DE APLICACIÓN    `orden` por fichero, total dentro de la reconciliación. La
                                recuperación aplica en el mismo orden, y por eso converge.

7  DERIVADOS AFECTADOS          los que dependen del estado reconciliado y habrá que
                                regenerar antes de `derivada`.
```

**Y dos campos más de contabilidad**, que `D62` separa de los siete de contenido:

```text
`intento`     1..3. Qué intento es éste. **NUNCA 4**: el contrato no lo admite.
`resuelve`    el `id` del evento `conflicto` que esta decisión resuelve — el de
              `observacion` igual a este `intento`.
```

**Se escribe con la misma disciplina de durabilidad que `preparada`**: `fsync` del evento y
de su directorio **antes** de tocar ningún canónico (§2.6.6). Es el **punto de compromiso de
la ruta de conflicto**: desde que es durable, la reconciliación se completa hacia delante.

#### `reconciliada` — la decisión ya está aplicada

```text
QUÉ AFIRMA        todos los ficheros que la decisión declara alcanzaron su `hash_final`.
                  Nada más: no declara la decisión —ya está en `reconciliacion-preparada`— y
                  no declara los derivados regenerados.
NO ES TERMINAL    el cierre es `derivada`, que regenera los derivados declarados en el punto
                  7 y sólo entonces retira el marcador.
POR QUÉ NO CIERRA porque la decisión PUEDE cambiar los canónicos respecto a lo que declaraba
AQUÍ              `preparada`, y los derivados llevan bloqueados toda la duración del
                  conflicto. Cerrar aquí dejaría derivados que describen un estado que ya no
                  existe — el defecto que `W7` y `X11` existen para impedir.
```

#### Clasificación y recuperación durante la reconciliación

**Las mismas tres cajas de §2.6.4, contra los hashes de la reconciliación:**

```text
CASA CON `hash_observado`   NO APLICADO         → aplicar
CASA CON `hash_final`       YA APLICADO         → saltar. Idempotente por hash
NO CASA CON NINGUNO         DIVERGENTE OTRA VEZ → vuelve a `conflicto`, con una base
                                                  observada NUEVA. NO se sobrescribe
```

```text
EL BUCLE TIENE TOPE   **`MAX_CAS_RETRIES = 3` limita INTENTOS, NO OBSERVACIONES** (§2.6.4).
                      Se prepara decisión para `intento` 1, 2 y 3 — **la tercera observación
                      SÍ recibe su intento, y es el último**. Si tras el `intento: 3` un
                      fichero vuelve a divergir, se emite un `conflicto` con
                      **`observacion: 4`, `intentos_consumidos: 3` y `agotado: true`**, que
                      **no admite ninguna `reconciliacion-preparada`**: se detiene, se escala
                      al OWNER y NO se vuelve a intentar sin su decisión. Esa cuarta
                      observación **registra el fracaso del tercer intento**, y por eso no se
                      silencia. Máximos exactos: **CUATRO observaciones y TRES intentos**.
                      Es el precedente numérico que `a.9` ya fijó para el CAS del tablero
                      —`MAX_CAS_RETRIES = 3`— aplicado aquí: un reintento sin tope es un
                      livelock, y el corpus ya lo resolvió una vez.
```

#### Las ventanas de caída de la reconciliación

| # | la caída ocurre… | qué queda durable | qué se hace |
|---|---|---|---|
| **R1** | tras decidir, antes de escribir el temporal de `reconciliacion-preparada` | el `conflicto`, y nada de la decisión | la decisión **se pierde y se vuelve a tomar**. El conflicto sigue abierto, que es su estado correcto. **Nada se ha tocado** |
| **R2** | escribiendo el temporal de `reconciliacion-preparada` | un temporal huérfano | se borra el temporal. La reconciliación no existió; el conflicto sigue abierto |
| **R3** | tras `reconciliacion-preparada`, antes de tocar nada | la decisión ENTERA | **se completa**: aplicar del primero al último, en el `orden` declarado |
| **R4** | tras aplicar unos ficheros y no otros | la decisión, y una mezcla en disco | **se completa**: aplicar sólo los que casan con `hash_observado`, en orden |
| **R5** | tras aplicar todos, antes de `reconciliada` | la decisión, y todos en `hash_final` | se emite `reconciliada`. No se reescribe nada |
| **R6** | justo después de `reconciliada` | la aplicación completa | se regeneran los derivados del punto 7 y se emite `derivada` |
| **R7** | durante la regeneración posterior a la reconciliación | derivados a medias | se regeneran ENTEROS y se emite `derivada` |
| **R8** | tras `derivada`, antes de borrar el marcador | transacción cerrada | se borra el marcador. Idempotente |
| **R9** | en cualquier punto, con un fichero que ya no casa ni con `hash_observado` ni con `hash_final` | la decisión | vuelve a `conflicto` con base nueva, `observacion` incrementada e `intentos_consumidos` = `observacion` − 1. Con `observacion` 2 o 3 se prepara un intento nuevo; con `observacion: 4` lleva `agotado: true` y **no se prepara ninguno**: para, escala y la transacción queda abierta (§2.6.4) |

**Una segunda ejecución converge al mismo resultado en las nueve**, porque la decisión es
durable desde `R3` y la clasificación por hash es idempotente. Es `T17` aplicado a la ruta de
conflicto, que era exactamente lo que no se podía afirmar antes.

#### Mismo disco, misma clasificación — las diecisiete ventanas contra UNA sola función

> **Añadido por la segunda corrección técnica (hallazgo `H2`).** Una tabla de ventanas es una
> lista de casos, y una lista de casos **puede contradecirse consigo misma sin que se note**:
> es exactamente lo que le pasó a `W12a` frente a `W3` y `W4`. La comprobación que lo impide
> es proyectar TODAS las ventanas sobre la función de clasificación de §2.6.4 y verificar que
> **ninguna ventana clasifica, y todas se limitan a describir por dónde se entró**.

```text
LA REGLA        una ventana NO decide. Decide la función de §2.6.4, sobre el disco. La
                ventana sólo dice qué se observa al arrancar. Dos ventanas con el mismo
                disco tienen, por construcción, el mismo desenlace.
```

| estado observable de una ruta | qué dice la función de §2.6.4 | ventanas que llegan a ese estado |
|---|---|---|
| sin `preparada` durable | no hay transacción: nada, o `deriva` `sin-transaccion` | `W1` · `W2` · `R2` |
| `preparada` durable · fichero en la BASE | NO APLICADO → aplicar | `W3` · `W4` (los que faltan) · **`W12a`** |
| `preparada` durable · fichero en el RESULTADO | YA APLICADO → saltar | `W4` (los hechos) · `W5` · `W6` · `W13` · `W14` |
| `preparada` durable · fichero en NINGUNO | DIVERGENTE → `conflicto` | `W11` · `X05` · `X06` |
| `conflicto` sin `reconciliacion-preparada` durable | el conflicto sigue abierto; **nada se toca** | `R1` · `R2` |
| `reconciliacion-preparada` durable · fichero en `hash_observado` | NO APLICADO → aplicar | `R3` · `R4` (los que faltan) |
| `reconciliacion-preparada` durable · fichero en `hash_final` | YA APLICADO → saltar | `R4` (los hechos) · `R5` · `R6` |
| `reconciliacion-preparada` durable · fichero en NINGUNO | DIVERGENTE → `conflicto`, base nueva, tope de tres | `R9` |
| `derivada` durable · fichero fuera del resultado que gobernaba | **`deriva`** `posterior-al-cierre`. Ninguna fase | **`W12b`** |
| derivados divergentes, canónicos intactos | regenerar enteros. No es una caja: un derivado no es fuente | `W7` · `R7` · `X10` · `X11` |
| transacción cerrada con marcador vivo | borrar el marcador. Idempotente | `W8` · `R8` |
| árbol coherente, Git por detrás | commit local sí, push no | `W9` · `W10` · `W15` · `W16` |
| marcador sin transacción propia, o llegado en un clon | **`fallo`** de publicación. Nunca `conflicto` | `X15` · `X28` |

**Las tres invariantes que esta tabla hace comprobables**, y que `X59` no necesita porque se
leen aquí —la tabla adversarial se queda en **cuarenta y dos filas**:

```text
1  NINGÚN `conflicto` SIN LAS DOS CONDICIONES: transacción abierta en esta instalación Y
   fichero que no casa ni con la base ni con el resultado. Cuatro filas lo producen, y las
   cuatro cumplen las dos.

2  NINGUNA TRANSICIÓN SALE DE `derivada`. La única fila con `derivada` durable produce un
   evento `deriva`, que no lleva `fase` ni `tx` propio.

3  MISMO ESTADO OBSERVABLE, MISMA CLASIFICACIÓN. `W12a` y `W3` comparten fila, que es lo
   que antes no ocurría; `W12a` y `W12b` están en filas distintas porque el disco NO es el
   mismo: en una hay una intención durable pendiente y en la otra ya se consumió.
```

### 2.6.10 · Commit y push en recuperación — y el hueco que esto destapa

> **Corregido por la segunda devolución independiente (hallazgo `K`, GRAVE).** F4c escribía
> en `W9` y `W10`, en voz impersonal, *«se hace el commit»* y *«se hace el push»*: sin
> ordenante, sin autoridad, sin ejecutor atribuido — **ninguno de los cinco conceptos de
> `a.9`** que §3.6 obliga a registrar en toda mutación. Sin política de rama, pese a que
> `G29` protege `main` por defecto. Sin ramal de fallo. Y sin encaje real con `C7`.

**La distinción que faltaba, y lo cambia todo:**

```text
`W9` COMMIT LOCAL     ES RECUPERACIÓN. Protege el árbol frente a su pérdida —garantía 4 de
                      §2.6.6— y NO publica nada. Va sin preguntar, como el resto de la
                      recuperación.

`W10` PUSH            NO ES RECUPERACIÓN: ES PUBLICACIÓN. Sube a infraestructura del Owner,
                      hace el trabajo visible a todo clon, y es irreversible en el sentido
                      que §8.1 ya declara con todas las letras: «un rollback NO reescribe
                      historia publicada: reescribirla rompería todo clon existente, y ADS
                      no lo hace». **NO se ejecuta por el mero hecho de arrancar.**
```

> **La asimetría que F4c no argumentaba.** Es escrupuloso con la publicación cuando habla de
> instalación y de rollback —§8.1 prohíbe la eliminación remota automática y reserva la
> decisión al Owner— y la ejecutaba sin preguntar cuando hablaba de recuperación. Las dos
> son la misma operación sobre la misma infraestructura.

**Lo que rige, y son cinco reglas:**

```text
1  EL COMMIT LOCAL SE HACE, y emite su evento con los CINCO conceptos de `a.9`:
   ordenante · autoridad · escritor_del_comando · ejecutor · actor_atribuido. La ausencia de
   cualquiera de los cinco es un FALLO DEL VALIDADOR, no un silencio.

2  EL PUSH NO ES AUTOMÁTICO. Pasa a `esperando-owner`, o a la política de publicación que el
   producto declare. Una recuperación que publica sin decirlo convierte un incidente local en
   un hecho remoto.

3  LA RAMA SE DECLARA, y no se adivina. `main` del control repo PROTEGIDA por defecto,
   coherente con `G29` conservada por `E2.4`.

4  PUSH RECHAZADO POR REMOTO AVANZADO → evento `fallo`, tope de TRES reintentos por §7.3, y
   se escala. **NUNCA `--force`.** Regla dura, heredada literalmente de §8.1:
   **ADS no reescribe historia publicada del control repo.**

5  «EL REMOTO ESTABA ATRASADO, NO ROTO» era un SUPUESTO, no una comprobación. `E2.7` y §2.11
   admiten expresamente dos máquinas sobre el mismo control repo, y en ese caso el remoto
   PUEDE haber avanzado. Se comprueba; no se supone.
```

### El hueco que esto destapa, y que no se tapa con una remisión

§7.6 afirma que *«`C7` declara quién pide, ejecuta, bloquea y verifica cada una»*. **Es falsa
exactamente para las dos operaciones que `W9` y `W10` automatizaban**, y el motivo es
estructural:

```text
LA TABLA DE PROPIEDAD DE `C7`   gobierna las operaciones Git DE LAS FUENTES: rama, commit,
                                push, PR, revisión, merge y CI, capacidad a capacidad.

NINGUNA DE SUS FILAS CUBRE      y `W9`/`W10` son commits y pushes DEL CONTROL REPO, porque es
EL REPOSITORIO DE CONTROL       ahí donde vive `estado/`.

LUEGO EL GOBIERNO GIT DEL       es un HUECO DECLARADO POR OMISIÓN en toda la arquitectura.
CONTROL REPO NO EXISTE          F4c lo tapaba con una remisión que no resuelve.
```

**Se declara aquí como hueco, y no se rellena por inferencia.** Rellenarlo es escribir la
tabla de propiedad del control repo —quién pide, ejecuta, bloquea y verifica su commit, su
push, su rama y su PR, con qué evidencia—, y su sitio es la reconstrucción de `C7` que §10.2
registra. Mientras no exista:

```text
§7.6 SE CORRIGE   deja de afirmar que `C7` cubre TODAS las operaciones. Cubre las de las
                  FUENTES, y el control repo está pendiente
LO QUE SE PUEDE   la recuperación local completa, el commit local con su evento, y el push
HACER HOY         SUSPENDIDO a decisión, que es el comportamiento seguro
```


### 2.6.11 · `deriva` — lo que se descubre DESPUÉS del cierre no es una fase

> **Añadida por la corrección técnica posterior (hallazgo `2`, BLOQUEANTE).** §2.6.6 y `W12`
> decían que un canónico revertido bajo una transacción durable *«emite `conflicto`»*, y
> `conflicto` es una **fase de la transacción**. Con `derivada` como único terminal, eso es
> **una transición que sale del terminal** — que la tabla de §2.6.1 declara defecto. El
> protocolo se contradecía en el punto donde detecta corrupción silenciosa. Es `D53`.

**La distinción que faltaba, y es de identidad, no de grado:**

```text
CONFLICTO      se descubre MIENTRAS la transacción sigue abierta —sin `derivada`—. Es una
               FASE suya, tiene su `tx`, y la transacción lo resuelve por su ruta de
               conflicto. El estado incoherente es SUYO y lo arregla ella.

DERIVA         se descubre DESPUÉS de que la transacción cerró, o SIN ninguna transacción de
               por medio. **NO es una fase de nada**: la transacción terminó, y una historia
               append-only no se reabre. Es un evento NUEVO con identidad propia.
```

**El evento `deriva`:**

```text
tipo             deriva
fase             — NINGUNA. No pertenece al autómata de §2.6.1 y no lleva `tx` propio
tx_afectada      la transacción CERRADA cuyo resultado ya no se sostiene, si la hay.
                 Es una REFERENCIA, no una pertenencia: no la reabre, no la modifica y no
                 añade ninguna fase a su historia
causa            `posterior-al-cierre`   el fichero casaba y ya no casa, con `derivada`
                                         durable. Corrupción silenciosa (garantía 3 de
                                         §2.6.6)
                 `sin-transaccion`       nadie preparó nada: alguien editó un canónico
                                         fuera del protocolo
afecta           por fichero: `ruta` · `hash_esperado` —el que gobierna según la transacción
                 cerrada, o el de `HEAD` si no hay transacción— · `hash_observado`
items            los items cuyos canónicos están afectados
autoridad        quién debe decidir la reparación
```

**Qué hace, y sobre todo qué NO hace:**

```text
SE REPORTA       nombrando ruta, hash esperado y hash observado, por fichero.
SE ESCALA        a la autoridad declarada. Es `b.14.3`: DSP para y escala.
BLOQUEA          el despacho sobre los items afectados, igual que un conflicto — el estado
                 no es fiable, y el motivo de no serlo no cambia esa consecuencia.

NO REABRE        la transacción cerrada. Su historia es inmutable, y `derivada` fue su
                 último acto.
NO AÑADE FASE    a nada. Que `deriva` no lleve `fase` ni `tx` lo rechaza el ESQUEMA
                 ESTRUCTURAL, porque es coherencia interna del propio evento. Que ningún
                 evento con `fase` pertenezca a un `tx` que ya tiene `derivada` lo rechaza
                 el VALIDADOR SEMÁNTICO DEL DIARIO, porque exige recorrer ese `tx`
                 entero (§3.6).
NO RESTAURA      desde Git, ni desde ningún sitio, **automáticamente**. El contenido que hay
                 en disco es de alguien, y sobrescribirlo sin decisión es destruir trabajo
                 sin registro — el mismo argumento de §2.6.4.
NO REPARA        por su cuenta.
```

**Y si hay que reparar, la reparación es una transacción nueva:**

```text
REQUIERE UNA OPERACIÓN RECUPERABLE, con su INTENCIÓN DURABLE PREVIA — es decir, su propio
`preparada`, con `hash_previo` = el `hash_observado` que la deriva registró, y
`hash_posterior_esperado` = lo que la autoridad decida.

NO es una fase de la transacción vieja. Es una transacción NUEVA, con `tx` nuevo, que
REFERENCIA el evento `deriva` que la motivó. Con eso la reparación tiene las mismas
garantías que cualquier otra escritura canónica, y ninguna excepción.
```

> **Por qué no basta con «restaurar desde Git».** Un commit demuestra qué se guardó, no qué
> hay hoy en el árbol. Restaurar sobrescribe lo observado, que puede ser trabajo de alguien o
> la única copia de un contenido que nadie más tiene. La restauración es **una decisión del
> Owner** y, cuando se ejecuta, **es una transacción de reparación como cualquier otra**.

## 2.7 · Concurrencia, locks e identidad sin colisión

```text
POR DISEÑO NO COLISIONAN   paquetes en unidades de custodia distintas (I3). Es el caso
                           normal y no necesita lock.

UN SOLO EJECUTOR           las mutaciones canónicas las aplica un único ejecutor (R5).
DE MUTACIONES              `.ads/run/lock` con identidad del proceso y latido. Vive en el
                           plano operacional a propósito: un lock versionado en Git sería
                           un lock que viaja a otra máquina, que es peor que no tenerlo.

DOS AGENTES, UN PAQUETE    prohibido por custodia única. Es un defecto de despacho, no un
                           conflicto que fusionar (a.5).

EL TABLERO                 dos escritores físicos por diseño: Owner en ÓRDENES, runtime en
                           COLA. Protocolo de a.9 con CAS sobre hash de contenido y tope de
                           tres reintentos. NO se toca.
```

**Latido y hora de pared.** El lock lleva hora, y eso es correcto: **no es un artefacto
derivado**. `R4` prohíbe la hora de pared en los derivados, no en el plano operacional. Un
lock cuyo dueño murió se detecta por latido vencido y se reclama registrando el evento.

### Identidad de los eventos — corrección

F4 entregada afirmaba que *«el diario no necesita lock: un evento es un fichero nuevo con id
único. Dos emisores concurrentes no colisionan jamás»*, con ids `EV-<nnnnnn>` **monotónicos**.
**Las dos afirmaciones son falsas y se retiran.** Un id monotónico se calcula leyendo el
mayor existente y sumando uno; dos emisores que lo hacen a la vez eligen el mismo número.
Que el fichero sea nuevo no genera su nombre.

```text
LA ELECCIÓN, DECLARADA     de las dos vías admisibles —serializar la generación bajo el
                           ejecutor único, o usar ids NO MONOTÓNICOS resistentes a
                           colisión— se elige la SEGUNDA.

FORMA                      `EV-<huella del contenido del evento>`. Direccionado por
                           contenido.

POR QUÉ LA SEGUNDA         · no depende de un lock que sólo existe en una máquina, y `R5`
                             es un requisito del runtime local, no del producto
                           · la idempotencia se ejerce sobre `tx` con la regla de
                             reintento de §2.8 — NO sobre el nombre del fichero.
                             F4c afirmaba aquí que «emitir dos veces el MISMO evento produce
                             el MISMO fichero»: es falso bajo `predecesor` distinto, y se
                             RETIRA (hallazgo `C`)
                           · sobrevive a dos máquinas sobre el mismo control repo, que es
                             el caso que `E2.7` dejó abierto

QUÉ SE PIERDE, Y SE DICE   el orden NO se lee del nombre. Se recupera de dos campos:
                             `orden`       total DENTRO de una transacción
                             `predecesor`  el evento que este emisor observó como último.
                                           Forma una cadena verificable
                           EL ORDEN TOTAL ENTRE MÁQUINAS NO SE AFIRMA. Dos emisores
                           concurrentes BIFURCAN la cadena; la bifurcación se detecta al
                           verificarla, y resolverla es runtime distribuido — abierto en
                           `E2.7` y en §2.11.
```

## 2.8 · Identidad, versionado y migración de esquema

```text
ITEM        <TIPO>-<nnn>            FEA-021         estable, del PRODUCTO (E2.5)
PAQUETE     <ITEM>/<nn>             FEA-021/02
INICIATIVA  INI-<nnn>
EVENTO      EV-<huella>             direccionado por contenido, NO monotónico (§2.7)
TRANSACCIÓN TX-<huella>             comparte forma con el evento. NO es un artefacto: es el
                                    identificador que agrupa los eventos de una transacción
COBERTURA   <clase>:<ancla>/<ruta>  pantalla:web/checkout
INTEGRACIÓN IS-<nnn>                ya normado por `integration-set`

VERSIÓN DE REGISTRO   cada fichero canónico lleva `v`, que incrementa el ejecutor de
                      mutación. Es la base del CAS y de `based_on`.

VERSIÓN DE ESQUEMA    cada fichero canónico lleva `esquema_estado: N`. Una migración es un
                      item `SIS` con su migrador, su prueba y su rollback, y emite evento.
                      Leer un fichero con esquema mayor que el soportado es un ERROR
                      EXPLÍCITO, nunca una interpretación optimista.
```


### El contrato de identidad — sin circularidad y reproducible

> **Añadido por la segunda devolución independiente (hallazgo `C`, GRAVE).** F4c decía
> `id: EV-<huella del contenido>` en una lista de campos **cuyo primer campo es `id`**, y
> `TX-<huella>` con la glosa «comparte forma con el evento» — que dice **cómo se ve**, no
> **qué se hashea**. Sin serialización canónica, dos implementaciones producen
> identificadores distintos para la misma entrada. Como estaba escrito, **no era
> implementable**. Es `D37`.

**1 · Representación canónica.** Normativa e **independiente del formato de presentación**.
Se publica en F6 como pseudocódigo, no como prosa, y su contrato es:

```text
claves            ordenadas lexicográficamente, en todo mapa y a toda profundidad
listas            en su orden declarado, que es significativo y no se reordena
escalares         codificación fijada; sin representaciones alternativas del mismo valor
texto             UTF-8, normalización NFC
saltos de línea   `\n` como ÚNICO terminador. `\r\n` se normaliza antes de hashear
rutas             relativas a la raíz del control repo, con `/`, sin `./` ni `..`
espacios          sin espacios finales de línea ni al final del documento
```

**2 · Campos incluidos y excluidos.** La lista es **cerrada**:

```text
`id`              EXCLUIDO por construcción. Es lo que se está calculando: incluirlo es la
                  circularidad que F4c no resolvía
`tx`              EXCLUIDO del cómputo del propio `tx`; INCLUIDO en el de cada evento
todo lo demás     INCLUIDO
UN CAMPO NUEVO    obliga a versionar el algoritmo: `identidad_v: N`, junto a
                  `esquema_estado`. Sin versión, añadir un campo cambia en silencio todos
                  los identificadores futuros y ninguno de los pasados
```

**3 · `tx`, definido.**

```text
tx = TX-H( representación canónica del cuerpo de `preparada`
           MENOS los campos `id`, `tx` y `predecesor` )
```

```text
POR QUÉ ASÍ   depende SÓLO de la intención declarada —`afecta`, `orden`, hashes,
              procedencia—, luego es reproducible por dos implementaciones, NO depende del
              punto de la cadena en que se emita, y SOBREVIVE A UNA REEMISIÓN. F4c no tenía
              definiendum: un `tx` no tiene contenido propio —§2.5 lo declara— luego no
              había nada de lo que sacar su huella
```

**4 · `evento.id`, definido — y la consecuencia, declarada.**

```text
id = EV-H( representación canónica del evento MENOS `id` )
```

```text
`predecesor` VA INCLUIDO      es parte de la historia, y dos eventos con el mismo cuerpo en
                              puntos distintos de la cadena NO son el mismo evento

Y POR TANTO, DICHO SIN        **REEMITIR NO ES IDEMPOTENTE POR `id`.** Tras una caída, el
RODEOS                        diario ha crecido y el `predecesor` es otro, luego el id es
                              otro. F4c afirmaba que «emitir dos veces el MISMO evento
                              produce el MISMO fichero: la idempotencia deja de necesitar un
                              registro aparte». **Eso sólo es cierto bajo un `predecesor`
                              idéntico**, condición que la recuperación no garantiza. La
                              frase se RETIRA.

DÓNDE VIVE LA IDEMPOTENCIA    sobre `tx`, no sobre `id`. Y se ejerce con una regla, no con
                              un nombre de fichero.
```

**4bis · La EXCEPCIÓN TIPADA: un evento con el cuerpo retirado.**

> **Añadida por la sexta comprobación técnica (`D63`, que revisa `D37` y `D61`).** El
> contrato decía `id = EV-H(evento MENOS id)` y, a la vez, que `retirada-de-cuerpo`
> **sustituye el cuerpo por una lápida conservando el mismo `id`**. Las dos cosas juntas
> tienen una consecuencia que no estaba escrita:
>
> ```text
> 1  después de retirar el cuerpo, el `id` original YA NO PUEDE RECALCULARSE desde el
>    fichero actual: la preimagen que lo produjo ya no está allí
> 2  la identidad DIRECCIONADA POR CONTENIDO deja de ser verificable por la REGLA
>    ORDINARIA. Aplicarla a la lápida da OTRO valor, no el `id` declarado
> 3  conservar el `id` y una huella **NO equivale a conservar el contenido original**, y
>    tratarlo como si lo fuera es la afirmación que `D63` retira
> ```
>
> No se corrige debilitando la regla de identidad: se corrige **tipando la excepción**, para
> que esquema y validador sepan cuál de los dos algoritmos aplicar.

**Los dos casos, y son disjuntos y distinguibles sin ambigüedad:**

```text
A · EVENTO ÍNTEGRO         · se recalcula su representación canónica
                           · se deriva su `id` con `EV-H(evento MENOS id)`
                           · el resultado DEBE coincidir con su nombre y con la identidad
                             declarada. Si no coincide, es un defecto

B · EVENTO CON CUERPO      · **NO se intenta recalcular el `id` desde la lápida.** Aplicar
    RETIRADO                 la fórmula ordinaria a una lápida es un ERROR DEL VALIDADOR,
    (lápida)                  no un fallo del evento
                           · se valida la ESTRUCTURA de la lápida (§2.9)
                           · se valida que SELLADO y LÁPIDA vinculen exactamente lo mismo:
                                 `id_original` · `hash_cuerpo_original` · `fase` · `tx` ·
                                 posición en la cadena
                           · SI se aporta el cuerpo original: se recalculan su huella y su
                             identidad, y **deben coincidir** con lo que lápida y sellado
                             declaran
                           · SIN el cuerpo original **no existe verificación completa de su
                             preimagen**, y el sistema debe decirlo en vez de callarlo
```

```text
CÓMO SE DISTINGUEN     el propio evento lo declara: una lápida lleva `cuerpo_retirado: true`
                       y el bloque de lápida de §2.9. El esquema estructural lo ve sin salir
                       del fichero, y por eso puede elegir el algoritmo correcto ANTES de
                       intentar nada.

QUÉ NO SE DEBILITA     la regla de identidad de los eventos íntegros. Sigue siendo
                       `EV-H(evento MENOS id)`, sin excepciones, y `X20` y `X22` la
                       comprueban igual que antes.
```

**5 · Regla de reintento.** Es lo que F4c le pedía al nombre del fichero y el nombre del
fichero no puede dar:

```text
ANTES DE REEMITIR, el ejecutor busca en el diario un evento con el MISMO `tx` y la MISMA
`fase`. Si existe, la operación es una NO-OPERACIÓN.
```

> **Qué significa exactamente «reemitir» aquí, precisado por `D58`.** Es el INTENTO de
> volver a emitir tras una caída, no un permiso para tener dos eventos de la misma fase. La
> regla de arriba lo convierte en **no-operación** cuando la fase ya existe, y de ahí que
> **`confirmada → confirmada` no exista** (§2.6.4). Las únicas fases que pueden aparecer más
> de una vez en un `tx` son `conflicto` y `reconciliacion-preparada`, y no por reemisión sino
> porque el contrato las declara **repetibles**, cada una con SU discriminador: `observacion`
> para `conflicto` —hasta 4— e `intento` para `reconciliacion-preparada` —hasta 3— (§2.6.4). Y
> **restaurar** un fichero de evento perdido no es reemitir: devuelve el MISMO `id`, con el
> mismo cuerpo y el mismo `predecesor`, luego no cae bajo esta regla y no hace crecer el
> diario.

**Y una incompatibilidad declarada, que hay que resolver antes de construir.** §2.11 admite
que el formato del diario **puede cambiar** de Markdown a «un formato de línea» sin que cambie
el contrato. Pero si la identidad es la huella del contenido, **cambiar el formato cambiaría
todos los identificadores** y `predecesor` dejaría de resolver. La representación canónica de
arriba es lo que lo resuelve —es independiente de la presentación—, y `X22` es la prueba que
lo comprueba. Sin esa independencia, §2.8 y §2.11 son incompatibles.

**Los identificadores de item y de iniciativa siguen siendo legibles y correlativos** —son
del producto y los lee el Owner—, y su generación sí se serializa bajo el ejecutor único.
La diferencia con los eventos es deliberada: un `FEA-021` se pronuncia en una conversación;
un evento no.

## 2.9 · Qué se reconstruye, desde dónde, y qué significa sellar

**La pregunta honesta no es «¿se puede reconstruir todo?» sino «¿desde dónde, y con qué
garantía?».**

| artefacto | se reconstruye desde | garantía |
|---|---|---|
| tableros, vistas, dosieres, índices | los canónicos | **total y determinista**. `T03` lo comprueba |
| `.ads/run/` entero | los canónicos | total |
| un derivado divergente | los canónicos | total, y `Continúa` paso 2 lo regenera |
| el marcador `estado/tx/<TX>.abierta` | el diario: una transacción **sin evento `derivada`** | total. Es un acelerador, no una verdad. Con `derivada` como único terminal (§2.6.1), la condición es UNA |
| una transición interrumpida | el evento `preparada` de su `tx` | total si ningún fichero es divergente; si lo es, `conflicto` declarado |
| el estado canónico tras una pérdida | Git | total: es su historia |
| el estado canónico **sin Git** | eventos sellados + eventos posteriores | **parcial y declarada**: sólo desde el último sellado. Antes del primero, no |
| el contenido de otra fuente | su repositorio, por la revisión referenciada | total mientras la fuente exista. ADS **no lo copia** (`R6`) |

### Semántica del sellado

Al cerrar un item, sus eventos se **compactan** en un fichero sellado. Qué significa eso,
con las cuatro preguntas respondidas:

```text
QUÉ CONSERVA EL SELLADO   · el ESTADO FINAL de los items que sella. Es lo que hace real la
                            reconstrucción sin Git
                          · por cada evento sellado: su `id`, su `fase`, su `tx`, su
                            POSICIÓN y la HUELLA de su contenido. La LISTA ORDENADA, no un
                            resumen. **La huella, no el cuerpo**
                          · la cabeza de la cadena `predecesor` al sellar
                          · qué eventos quedan REFERENCIADOS desde fuera del sellado

QUÉ PUEDE RETIRARSE       únicamente el CUERPO de un evento sellado: su texto largo. Nunca
                          su id, su huella ni su posición. Retirar un cuerpo es un acto
                          AUTORIZADO Y REGISTRADO —emite su propio evento—, no una limpieza
                          automática por antigüedad. Y exige una FUENTE DE RECUPERACIÓN
                          COMPROBADA de antemano (abajo).

QUÉ NO PUEDE RETIRARSE    · un evento con una DEPENDENCIA SEMÁNTICA VIVA: alguien que
   NUNCA                    necesita LEER SU CUERPO, no sólo nombrarlo (abajo). Una
                            referencia ESTRUCTURAL por `predecesor` **no** bloquea
                          · el evento terminal de cualquier transacción
                          · el estado final de un item, que es el contenido del sellado
                          · cualquier evento cuya fuente de recuperación no esté comprobada

QUÉ SE VERIFICA, Y CON    **TRES NIVELES DISTINTOS, y no son el mismo.** Están abajo, uno a
QUÉ ALCANCE               uno. Recorrer los ids conservados comprueba ORDEN Y REFERENCIAS,
                          no CONTENIDO; y una huella sola no dice cuál era el cuerpo.

QUÉ ES EXACTAMENTE        sellar **AÑADE**: escribe un fichero de sellado nuevo y emite el
APPEND-ONLY, Y QUÉ NO     evento que lo registra. Retirar un cuerpo, en cambio, **SÍ EDITA
                          FÍSICAMENTE UN FICHERO EXISTENTE**. La formulación correcta está
                          abajo, y ya no dice «sustituir no es editar».
```

#### Los TRES NIVELES de garantía, que el texto anterior mezclaba

> **Corregido por la sexta comprobación técnica (`D63`).** §2.9 decía que *«un cuerpo
> retirado sigue siendo verificable: su huella está en el sellado, y por eso se puede
> demostrar que se conocía y que se retiró a propósito»*, y que *«recomputar la cadena
> `predecesor`»* verificaba integridad y orden. **Las dos frases prometen de más.** Una
> huella es un COMPROMISO CRIPTOGRÁFICO: sin la preimagen no demuestra qué contenido había
> ni que se poseyera; y recorrer referencias comprueba el orden, no el contenido. Se separan
> en tres niveles, cada uno con lo que sí garantiza y lo que no.

```text
NIVEL 1 · CONTINUIDAD     QUÉ DA   los `id` conservados y los enlaces `predecesor` permiten
ESTRUCTURAL                        RECORRER EL ORDEN DECLARADO y comprobar que ninguna
                                   referencia apunta a algo que no existe, hasta el ancla
                                   que el sellado declara.
                          QUÉ NO   **no verifica NADA del contenido retirado.** Un orden
                          DA       correcto sobre cuerpos ausentes sigue siendo un orden
                                   correcto sobre cuerpos ausentes.
                          SOBREVIVE a la retirada, y sobrevive a que la fuente externa
                                   desaparezca.

NIVEL 2 · CONSISTENCIA    QUÉ DA   sellado y lápida contienen EL MISMO COMPROMISO
DEL COMPROMISO                     CRIPTOGRÁFICO —`hash_cuerpo_original`—, junto con el
                                   mismo `id_original`, `fase`, `tx` y posición. Se puede
                                   demostrar que **el repositorio conservó ese compromiso y
                                   registró la retirada**, con su autoridad y su motivo.
                          QUÉ NO   **una huella aislada no demuestra por sí sola cuál era el
                          DA       contenido, ni que alguien lo poseyera.** Demuestra que
                                   DOS SITIOS DEL REPOSITORIO dicen lo mismo — que es
                                   consistencia interna, no prueba de preimagen.
                          SOBREVIVE a la retirada, y sobrevive a que la fuente externa
                                   desaparezca.

NIVEL 3 · VERIFICACIÓN    QUÉ DA   con el CUERPO ORIGINAL delante: se recalcula el cuerpo,
COMPLETA                           su huella y su identidad, y las tres deben coincidir con
                                   lo que lápida y sellado declaran. Es la única que cierra
                                   la preimagen.
                          QUÉ      **EXIGE DISPONER DEL CUERPO ORIGINAL.** Puede proceder de
                          EXIGE    una revisión Git EXACTA o de otro archivo durable
                                   autorizado (abajo).
                          NO SOBREVIVE a que la fuente de recuperación desaparezca. Y
                                   cuando eso ocurre, **el sistema lo declara**: los niveles
                                   1 y 2 siguen, el 3 no, y no se sigue afirmando integridad
                                   histórica completa.
```

```text
LA FRASE QUE SE RETIRA    «la huella demuestra que el cuerpo existió» · «la huella demuestra
                          cuál era» · «se recompone la cadena» cuando sólo se comprueban
                          referencias · «el contenido sigue siendo verificable» sin decir
                          que el cuerpo original tiene que estar disponible.
                          Ninguna de las cuatro se usa ya en la norma vigente.
```

#### La FUENTE DE RECUPERACIÓN, exigida antes de retirar

**La retirada sólo puede autorizarse si, ANTES de sustituir el cuerpo, se cumplen las
cuatro:**

```text
1  EL EVENTO ORIGINAL Y SU     confirmados en una REVISIÓN GIT DURABLE del repositorio de
   SELLADO ESTÁN DURABLES      control, o en un ARCHIVO EXTERNO AUTORIZADO. Sin esto no hay
                               de dónde recuperar, y la retirada es una pérdida.

2  LA LÁPIDA LLEVA UN          y no sólo una huella. Tres campos, y los tres:
   LOCALIZADOR VERIFICABLE       · `revision`  el commit exacto, o el identificador del
                                              archivo externo autorizado
                                 · `ruta`      la ruta o el `blob` dentro de esa revisión
                                 · `hash_esperado`  el del cuerpo que debe salir de ahí

3  SE HA COMPROBADO QUE EL     no «se supone que se puede»: se RECUPERA, se calcula su
   CUERPO SE RECUPERA DE       huella y se compara. Una recuperación no ensayada no es una
   ESE LOCALIZADOR             garantía, es una expectativa.

4  LA EVIDENCIA DE ESA         queda REGISTRADA, y la lápida la referencia. Es lo que
   COMPROBACIÓN SE REGISTRA    permite auditar después que la condición 3 se cumplió de
                               verdad y no se declaró de palabra.
```

**Y si la fuente externa deja de estar disponible**, que es un caso que hay que nombrar
porque ocurre:

```text
SIGUEN VÁLIDOS      el NIVEL 1 —continuidad estructural— y el NIVEL 2 —consistencia del
                    compromiso—. No dependen de nada externo.

DEJAN DE ESTAR      la RECUPERACIÓN del cuerpo y la VERIFICACIÓN COMPLETA (nivel 3).
GARANTIZADOS

QUÉ DEBE HACER      **REFLEJAR LA DEGRADACIÓN**, y dejar de afirmar integridad histórica
EL SISTEMA          completa para ese evento. Un sistema que sigue diciendo «verificado»
                    cuando ya no puede verificar es peor que uno que no verifica.

LO QUE NO SE        **que Git garantice conservación eterna.** No la garantiza: depende de
AFIRMA              la POLÍTICA DE RETENCIÓN DE HISTORIA del alojamiento, de que nadie
                    reescriba o pode esa historia, y de que el remoto siga existiendo. La
                    dependencia se DECLARA —retención de historia, o archivo externo— en vez
                    de suponerse.
```

#### `append-only`, dicho con precisión física

> **Corregido por `D63`.** El texto anterior decía que *«retirar un cuerpo tampoco edita el
> evento: lo sustituye por su lápida»*. **Sustituir un cuerpo SÍ edita físicamente un fichero
> existente**, y llamarlo de otra manera no cambia lo que hace el sistema de ficheros.

```text
LO QUE ES INMUTABLE       los EVENTOS y sus CABECERAS LÓGICAS: `id`, `fase`, `tx`,
                          `predecesor`, posición y procedencia. Nada de eso cambia nunca.

CÓMO CRECE EL DIARIO      AÑADIENDO eventos nuevos. Es la operación normal, y la única que
                          el protocolo usa para narrar.

LA ÚNICA MUTACIÓN         **sustituir el CUERPO de un evento SELLADO por su LÁPIDA.** Una,
FÍSICA AUTORIZADA         y transaccional (§3.6): es la única escritura de ADS que reemplaza
                          contenido ya escrito bajo `estado/`.

CUALQUIER OTRA            PROHIBIDA. No hay una segunda excepción.
MODIFICACIÓN

Y POR TANTO, DICHO SIN    **el diario FÍSICO no es estrictamente append-only.** Lo es su
RODEOS                    semántica —eventos y cabeceras inmutables, historia que no se
                          reescribe— con UNA excepción física, tipada, autorizada,
                          transaccional y registrada. Decir «append-only» a secas era
                          cómodo y no era cierto.
```

**Qué reduce de verdad esta operación, y qué no:**

```text
SÍ REDUCE       el CORPUS y el CONTEXTO del checkout vigente: lo que un agente o una persona
                tiene que leer, y lo que ocupa el árbol de trabajo. Ése es su objeto.

NO ELIMINA      el cuerpo de la HISTORIA DE GIT. El commit que lo contenía sigue
                conteniéndolo, y por eso mismo la fuente de recuperación funciona.

NO REDUCE       necesariamente el TAMAÑO DEL REPOSITORIO: los objetos históricos siguen
                ahí. Un clon completo los sigue trayendo.

LIBERAR ESOS    sería OTRA OPERACIÓN, con OTRO GOBIERNO —reescribir o podar historia
OBJETOS         publicada—, y **no queda autorizada aquí**. Mezclarla con la retirada de
                cuerpo destruiría además la fuente de recuperación que la retirada exige.
```

#### Qué referencia BLOQUEA la retirada, y qué referencia NO

> **Corregido por `D63`.** La regla decía *«un evento al que apunta cualquier evento VIVO»*.
> Como **cada evento apunta al anterior por `predecesor`**, esa regla haría **inalcanzable la
> propia operación**: casi todo evento sellado tiene un sucesor que lo nombra. Se distingue
> por el TIPO de referencia.

```text
REFERENCIA         alguien NOMBRA el `id`, y le basta con el `id`: el enlace `predecesor`,
ESTRUCTURAL        la lista ordenada del sellado, un `resuelve`, un `tx_afectada`.
NO BLOQUEA         El `id` SE CONSERVA en la lápida, luego la referencia sigue resolviendo y
                   el orden sigue recorriéndose. **Por sí sola no impide retirar.**

DEPENDENCIA        alguien necesita LEER EL CUERPO para hacer su trabajo: una reparación que
SEMÁNTICA VIVA     tiene que reproducir el `contenido` o el `parche` declarado, una
BLOQUEA            reconciliación abierta que se apoya en la copia de lo divergente, una
                   transacción sin terminal que declara ese cuerpo como su mecanismo, un
                   dictamen en curso que lo cita como evidencia.
                   **Mientras exista, la retirada se rechaza.**

CÓMO SE DISTINGUEN el evento que refiere DECLARA cuál de las dos hace. Una referencia que no
                   dice que necesita el cuerpo se trata como ESTRUCTURAL; una que lo
                   necesita lo dice, y por eso bloquea. En la duda, BLOQUEA.

EL SELLADO ES EL   porque conserva `id`, `fase`, `tx`, posición y huella de cada evento
ANCLA              sellado, y la CABEZA DE LA CADENA al sellar. Con eso, el recorrido
                   estructural no necesita ningún cuerpo: se apoya en el sellado como
                   CHECKPOINT y sigue desde ahí.

CÓMO SE RECORRE    · por los `id` conservados y la lista ordenada del sellado, hasta el
LA CADENA TRAS       ancla. Eso es NIVEL 1, y no toca ningún cuerpo
LA RETIRADA        · lo que se verifica ASÍ: orden, referencias y que nada apunte al vacío
                   · lo que EXIGE recuperar los cuerpos originales: cualquier afirmación
                     sobre QUÉ decía un evento, y toda verificación de NIVEL 3
```

#### `retirada-de-cuerpo` — el contrato completo, punto por punto

**Sigue siendo TRANSACCIONAL** por el criterio de §3.6 —sustituye contenido previo—, y estos
son sus once puntos:

```text
1  FICHERO QUE MODIFICA      el del EVENTO SELLADO cuyo cuerpo se retira, en su ruta actual
                             bajo `estado/eventos/`. UNO, y ninguno más.

2  CONTENIDO EXACTO DE       `cuerpo_retirado: true`   la marca que tipa la excepción (§2.8)
   LA LÁPIDA                 `id_original`             el `id` del evento íntegro
                             `fase` · `tx` · `posicion`  la cabecera lógica, intacta
                             `predecesor`              intacto: la cadena sigue resolviendo
                             `hash_cuerpo_original`    el compromiso criptográfico
                             `localizador`             `revision` · `ruta` · `hash_esperado`
                             `prueba_de_recuperacion`  referencia a la evidencia registrada
                             `autoridad` · `motivo`    quién lo decidió y por qué
                             `sellado_ref`             el sellado que lo ancla

3  IDENTIDAD ORIGINAL        `id_original`, `fase`, `tx` y `posicion`. El `id` NO cambia y
   QUE CONSERVA              NO se recalcula desde la lápida: es la excepción tipada de
                             §2.8, punto 4bis.

4  LOCALIZADOR DEL CUERPO    `revision` —commit exacto o archivo externo autorizado—, `ruta`
   ORIGINAL                  o blob dentro de ella, y `hash_esperado`. Los tres, o no hay
                             localizador.

5  RELACIÓN CON EL SELLADO   la lápida y el sellado deben vincular EXACTAMENTE lo mismo:
                             `id_original`, `hash_cuerpo_original`, `fase`, `tx` y posición.
                             Una discrepancia entre los dos es un fallo de verificación
                             (`X-D`), no una tolerancia.

6  `hash_previo`             la huella del EVENTO ÍNTEGRO tal como está en disco antes de
                             tocarlo. Es lo que hace clasificable la recuperación por §2.6.4.

7  `hash_posterior_          la huella de la LÁPIDA completa. Con los dos, una caída a mitad
   esperado`                 cae en una de las tres cajas y se completa o se escala: la
                             retirada es recuperable como cualquier otra escritura canónica.

8  PRUEBA DE RECUPERACIÓN    OBLIGATORIA Y PREVIA. Se recupera el cuerpo desde el
   PREVIA                    localizador, se calcula su huella y se compara con
                             `hash_cuerpo_original`. Sin esta prueba **la retirada se
                             rechaza** (`X-G`). No se ensaya después: después ya no hay
                             cuerpo que recuperar si falla.

9  AUTORIDAD Y MOTIVO        ambos obligatorios, con los cinco conceptos de `a.9`. Retirar
                             no es una limpieza automática por antigüedad, y sin autoridad
                             declarada no es un acto: es una pérdida.

10 CÓMO SE REGISTRA          por LAS FASES DE SU PROPIA TRANSACCIÓN, con
   LA RETIRADA               `tipo: retirada-de-cuerpo`. Su `confirmada` **ES** el registro
                             del hecho. **NO se crea un segundo evento que la duplique**:
                             sería una segunda verdad sobre el mismo hecho.

11 POR QUÉ ESAS FASES        porque son ficheros NUEVOS, uno cada una, direccionados por su
   NO ABREN OTRA             contenido — y por el criterio de §3.6 eso **no exige `tx`**. La
   TRANSACCIÓN               recursión se corta por el criterio general, no por una
                             excepción escrita para el diario: escribir el `preparada` de
                             una retirada no abre otra transacción para registrar que se
                             escribió ese `preparada`.
```

#### `X-A`–`X-H` · las ocho comprobaciones de la retirada

**No son filas de la tabla adversarial de §2.6.7**, que sigue en **cuarenta y dos filas y
cuarenta y dos identificadores `X<nn>`**. Éstas verifican la semántica de lápida e identidad,
llevan letra en vez de número, y son contrato de prueba igual que aquéllas.

| | escenario | resultado exigido |
|---|---|---|
| `X-A` | lápida y sellado coinciden, y **el cuerpo original NO está disponible** | **NIVEL 1 válido** —orden y referencias se recorren hasta el ancla— · **NIVEL 2 válido** —el compromiso coincide en los dos sitios— · **NIVEL 3 NO alcanzable**: identidad y contenido originales **no se verifican completamente**, y el sistema lo DECLARA en vez de afirmar integridad histórica completa |
| `X-B` | se recupera el cuerpo desde el `localizador` declarado | su huella casa con `hash_cuerpo_original`, `EV-H(evento MENOS id)` sobre el cuerpo recuperado reproduce el `id_original`, y la **verificación completa se supera** |
| `X-C` | se aporta un cuerpo INCORRECTO | **verificación FALLIDA**, nombrando qué no casa: la huella, el `id` recomputado, o los dos. No se acepta «se parece» |
| `X-D` | sellado y lápida declaran `hash_cuerpo_original` o `id_original` DISTINTOS | **verificación FALLIDA.** Es inconsistencia interna del repositorio, y se escala: ninguno de los dos puede darse por bueno |
| `X-E` | un evento posterior mantiene **sólo una referencia estructural** `predecesor` al evento que se quiere retirar | la retirada **PUEDE autorizarse** si se cumplen las demás condiciones. El `id` se conserva en la lápida, la referencia sigue resolviendo y el orden sigue recorriéndose |
| `X-F` | existe una **dependencia semántica viva** que necesita leer el cuerpo —una reparación que debe reproducir su `contenido`, una reconciliación abierta apoyada en su copia de lo divergente— | **retirada BLOQUEADA**, nombrando quién depende y por qué. En la duda sobre el tipo de referencia, bloquea |
| `X-G` | se intenta retirar **antes de sellar**, o **sin prueba de recuperación comprobada** | **retirada BLOQUEADA** en los dos casos. Sin sellado no hay ancla; sin prueba de recuperación la retirada es una pérdida disfrazada de operación |
| `X-H` | pasar el validador sobre un evento con lápida | **NO aplica la fórmula ordinaria de identidad al contenido de la lápida.** Detecta `cuerpo_retirado: true`, cambia al algoritmo B de §2.8 punto 4bis, y valida estructura y vínculo con el sellado. Aplicar `EV-H` a la lápida y reportar «id no coincide» es un **defecto del validador** |

> **Ninguna se ha ejecutado**, como las cuarenta y dos de §2.6.7 y las nueve `R1`–`R9`.
> Escribir el contrato de una prueba no es la prueba.

**Sin sellado, el diario crece sin límite y la reconstrucción exige el primer evento de la
historia.** Con él, la garantía es explícita y acotada: **sellado más eventos posteriores**.

## 2.10 · Relación con varias fuentes Git

```text
EL ESTADO DEL PRODUCTO NO VIVE EN NINGUNA RAMA. Se calcula en el control repo.   C7

Un paquete que escribe en `frontend` y `backend` registra sus source changes EN SU
CHECKPOINT (E2.3), con rama, commit, push, PR y CI por fuente. El control repo guarda
REFERENCIAS —id de fuente y SHA—, nunca contenido.

Un `integration-set` es la única afirmación de que una combinación exacta se probó junta.
No es un commit multi-repositorio, y ADS no finge uno (E2.6).
```

## 2.11 · Lo que esta decisión deja abierto

```text
TAMAÑO DE SELLADO        cada cuántos items o eventos se compacta. Es un parámetro, y el
                         valor sale del piloto, no de una preferencia escrita hoy.
FORMATO DEL DIARIO       bloque canónico `ads:evento` en Markdown. Si el piloto demuestra
                         que el volumen lo hace impracticable, la alternativa es un
                         formato de línea; el CONTRATO —append only, id único, nunca se
                         edita— no cambia.
LOCK DISTRIBUIDO         dos máquinas sobre el mismo control repo se serializan por Git,
                         no por el lock. Ese caso queda declarado y sin resolver: es
                         runtime distribuido, y E2.7 ya lo dejó expresamente abierto.
ORDEN TOTAL ENTRE         la cadena `predecesor` da orden total DENTRO de una transacción y
MÁQUINAS                  orden parcial entre emisores concurrentes. La bifurcación se
                          DETECTA (§2.7); RESOLVERLA no se decide aquí, y es el mismo caso
                          distribuido de la línea anterior.
RETIRADA DE CUERPOS       cuándo se autoriza retirar el cuerpo de un evento sellado, y con
SELLADOS                  qué política. §2.9 fija que es un acto autorizado y registrado, y
                          NO fija el umbral: sale del piloto.
```

---

# 3 · Tipos y contratos

## 3.1 · La prueba que tiene que pasar un tipo nuevo

El §26.5 del documento de pendientes lo exige, y `D11` ya lo aplicó una vez al rechazar
`source` y `component` como tipos *«porque duplicarían `SOURCES.toml`»*:

```text
1  ¿lo expresa un tipo existente sin deformarlo?          → REUTILIZAR
2  ¿lo expresa la COMBINACIÓN de dos existentes?          → COMPONER
3  ¿le falta un campo a un tipo existente?                → EXTENDER
4  ¿tiene sujeto propio, autoridad propia y ciclo propio
   que ningún existente puede alojar sin mentir?          → TIPO NUEVO
```

## 3.2 · El veredicto, materia a materia

| materia | veredicto | por qué |
|---|---|---|
| **`iniciativa`** | **TIPO NUEVO** | ningún artefacto agrupa items. Un item tiene exactamente un proceso (`b.1`) y no puede contener otros; un paquete pertenece a un item. Falta un sujeto con identidad, alcance, gate propio y varios items dentro. `O11` le da nombre |
| **`adaptador`** | **TIPO NUEVO** | `C2` lo nombra —*«los nombres de marca sólo aparecen en el adaptador del proyecto»*— y no existe en ninguna otra parte: no es uno de los tipos canónicos, ninguna capacidad lo posee, ningún gate lo comprueba, ninguna ruta lo produce. Es `P-01`, y siete candidatos convergen en él |
| **`cobertura`** | **TIPO NUEVO** | nada persiste el nivel de calidad de una parte del producto ni su caducidad. Los tres registros existentes tienen otro sujeto: los ledgers registran qué se aprendió, el journal qué pasó, las decisiones qué se decidió. Es `P-03` |
| **`evento`** | **TIPO NUEVO** | `G26` está declarado PENDIENTE en `a.11` justamente porque no existe. Es el diario de §2, y **absorbe la transacción multiarchivo** como una `fase` suya |
| **manifiesto de transacción** | **NO ES UN TIPO** | mismo sujeto y misma autoridad que `evento`. Su «ciclo propio» era que cambiaba de fase, y reescribir el registro que debe sobrevivir a una caída era el defecto, no la propiedad. Se compone: una transacción es una secuencia de eventos inmutables con `tx` común. Ver §2.5 |
| **sujeto auditable** | **REFERENCIA TIPADA, no tipo** | se identifica con `(clase, ancla, ruta)` y se **declara dentro de la celda de cobertura**. Crear un tipo para el sujeto obligaría a un registro paralelo de pantallas, flujos y formularios que nadie mantendría, y a deformar `SOURCES.toml` — que es lo que `CI-1` prohíbe |
| **matriz sujeto × aspecto** | **VISTA DERIVADA** | es la proyección de las celdas de cobertura. Persistirla sería una segunda verdad |
| **finding** | **NO ES UN TIPO** | un finding clasificado por `ENC` a través de las nueve clases de entrada **o bien** produce un item de uno de los diez procesos de `b.16`, **o bien** no produce trabajo: se vincula a uno existente, o se corrige documentalmente. **Ninguna de las dos salidas exige un tipo nuevo**, y el §20.8 nombra las dos. Antes de clasificarse vive en la evidencia del `AUD` que lo produjo. **Corregido** (hallazgo `N-8`): F4c decía que §20.8 «mapea uno a uno sobre los diez procesos», y no lo hace — `SEG` no es un proceso, dos filas no producen item, tres procesos no aparecen y una fila es ambigua entre dos. El veredicto aguanta; el argumento con que se sostenía, no |
| **causa raíz** | **CAMPO, no tipo** | agrupa items ya existentes. Es una referencia común, no un sujeto |
| **campaña de corrección** | **ES UNA `iniciativa`** | varios items, un sentido común, un gate de cierre. Exactamente lo que la iniciativa es |
| **excepción aceptada** | **ESTADO DE `cobertura`** | con responsable, motivo y caducidad, que la celda ya necesita |
| **contrato documental** | **COMPOSICIÓN CON `memoria` GENERALIZADA** | `ads:memoria` —gobierno— + `cobertura` —vigencia—. `memoria` **se generaliza** para admitir cualquier documento gobernado, y eso se declara en vez de hacerse en silencio. Ver §4 |
| **estado de una `iniciativa`** | **VISTA DERIVADA** | función total sobre el estado global de sus items, que `b.4` ya calcula. Persistirlo en un canónico editable sería una segunda verdad. Ver §3.3.1 |
| **instalación / certificación** | **COMPOSICIÓN, más un esquema de CLASE** | el ESTADO es `cobertura` con `clase: instalacion` y `aspecto:certificacion/<nivel>`. La NORMA del nivel —pruebas, propietario, crítico, jerarquía, invalidación— no cabe en la celda ni en `gate`: es `nivel-certificacion`, esquema de clase con el precedente de `nivel-novedad`. Ver §9.2 |
| **política de recurrencia** | **DECISIÓN REGISTRADA** | vive donde viven las decisiones, y sus parámetros como campos de `cobertura` |
| **aspecto de calidad** | **REFERENCIA TIPADA, no tipo** | `aspecto:<familia>/<nombre>`. No es una capacidad —una capacidad responde de VARIOS aspectos— ni un fichero. Ver §3.5 y §5.2 |
| **integración multi-fuente** | **REUTILIZA `integration-set`** | ya existe y ya normado |
| **procedencia de conocimiento externo** | **MANIFIESTO NUEVO, no tipo** | misma clase que `SOURCES.toml`: un lockfile que consume tooling, con su contrato. `K0.11` y `huella.py` ya hacen esto **con el propio kernel**; `CAND-027` lo hace con conocimiento ajeno |
| **entradas de validadores (`P-08`)** | **EXTENSIÓN** | un bloque `entradas:` en `validadores.yaml`, junto al `vigencia:` que ya existe |

**El recuento se CALCULA, no se fija de antemano.** F4 entregada abría con «cuatro tipos
nuevos y ni uno más», y esa frase era una **cuota escrita antes de aplicar la prueba**: el
manifiesto de transacción quedó fuera de la cuenta sin pasarla. El §26.5 y el `3.7` del brief
existen para impedir que un diseño se pague en tipos, no para fijar un número por adelantado.
El recuento final está en §3.8, después de los veredictos, que es su sitio.

## 3.3 · `iniciativa` — qué declara

```text
id                INI-<nnn>
intencion         la pregunta o el resultado global. UNA, no una lista de tareas
alcance           qué entra
fuera_de_alcance  qué NO entra. Sin esto, una iniciativa crece hasta ser el proyecto
apertura          quién la abrió y por qué señal
items             referencias. NUNCA copia su estado
obligaciones      lo que la iniciativa DEBE dejar producido, más allá de que sus items
                  cierren. **CONSUME** los predicados de `b.3`; NO los reutiliza. Ver abajo
gate_de_cierre    ref a un gate
riesgos · decisiones · contratos_previstos    referencias
banderas          `aparcada` · `cancelada`, autoridad del Owner. Su PROPAGACIÓN a los items
                  está declarada abajo, y no es mecánica
```

**Su estado NO es un campo.** `b.4` define el estado global como función total sobre los
paquetes de un item. Dar a la iniciativa un estado editable crearía una segunda verdad sobre
lo mismo, que es `I5`.

### 3.3.0 · Los dos predicados de obligación, definidos a nivel de iniciativa

> **Corregido por la segunda devolución independiente (hallazgo `N-6`, GRAVE).** F4c decía
> «misma forma que las obligaciones de proceso de `b.3`», y los dos predicados de `b.3` están
> definidos sobre objetos que **una iniciativa no tiene**:
>
> ```text
> obligación_satisfecha   exige una CAPA VIGENTE. Las capas las depositan las capacidades en
>                         PAQUETES, y `b.1` fija que un paquete pertenece a un ITEM. Una
>                         iniciativa no tiene paquetes ni capas: sólo `items` como referencias
> obligación_retirada     exige una RECOMPOSICIÓN APROBADA, que es `b.9`, definida sobre la
>                         RUTA DE UN ITEM. Una iniciativa no tiene ruta
> ```
>
> **Consecuencia mecánica:** toda obligación de iniciativa era huérfana desde que se escribía,
> y `Q9` devolvía `bloqueada` **para siempre**. Una iniciativa con obligaciones **nunca podía
> cerrar**. Es el mismo bloqueo perpetuo que `D32` corrigió para la Integrada, en otro sitio y
> sin detectar — y hacía que la función «total» de §3.3.1 **no fuera computable en su última
> rama**.

```text
obligación_de_iniciativa_satisfecha(o) ≡
    existe una CAPA VIGENTE **de alguno de sus items** enlazada EXPLÍCITAMENTE a `o`

    La iniciativa NO produce capas: las CITA. Con eso la satisfacción se apoya en `b.3` sin
    deformarla, y el enlace explícito impide que una capa cualquiera se lea como cumplimiento
    de una obligación que nadie conectó con ella.

obligación_de_iniciativa_retirada(o) ≡
    una DECISIÓN REGISTRADA de quien abrió la iniciativa —o del OWNER, según la materia—
    declara que dejó de ser necesaria, IDENTIFICA LA AUTORIDAD y EXPLICA CÓMO AFECTA al
    resultado perseguido

    Es el equivalente de la recomposición aprobada de `b.9`, sin inventar una ruta de
    iniciativa. Conserva los tres requisitos que `b.3` exige de una retirada.
```

**Se registra como CONSUMO, no como reutilización** — que es exactamente lo que `D29` hizo,
correctamente, con `b.4`, y lo que el argumento de la retirada de `PN-4` establece. Que la
definición pertenezca a (g) y no redefina `b.3` es lo que **`PN-9` pide a F5 que confirme**, y
no se da por hecho aquí.

### 3.3.1 · La función de estado, total y disjunta

F4 entregada listaba cinco estados con definiciones que se solapaban —«abierta: tiene items
vivos» y «bloqueada: todos sus items vivos están bloqueados» son ciertas a la vez— y dejaba
sin cubrir la iniciativa sin items, las mezclas, las cancelaciones y las obligaciones
huérfanas. Se sustituye por una función con **precedencia mecánica**, con la misma forma que
`b.4`, porque consume su resultado.

```text
estado_iniciativa(INI) → (estado, motivo)

Dominio: el estado global de cada item de la iniciativa, YA CALCULADO por b.4, más las
banderas de la propia iniciativa y el veredicto de su gate de cierre.

VIVO = estado_global(item) ∉ { cerrado, cancelado }
```

**Precedencia. Se evalúa en orden y gana la primera que se cumple.**

```text
Q0   ∃ item en `reconciliacion-pendiente`              → reconciliacion-pendiente
     Mientras sea cierto, ningún otro cálculo es fiable. Va PRIMERO, igual que b.4 P0.

Q1   bandera `cancelada`  Y  ∃ item VIVO               → cancelando
Q2   bandera `cancelada`  Y  ningún item vivo          → cancelada
Q3   bandera `aparcada`                                → aparcada
     El bloqueo de sus items SE SIGUE REPORTANDO: aparcar oculta el trabajo, no la
     información. Es b.4 P3 aplicado aquí.

Q4   conjunto de items VACÍO                           → abierta-sin-items
     Existe, tiene intención y alcance, y todavía no ha producido ningún item. NO es un
     error: es el primer instante de toda iniciativa.

Q5   ∃ item `en desacuerdo`                            → en-desacuerdo
     Hay algo que RESOLVER, y domina sobre lo que sólo hay que esperar (b.4 P4).

Q6   ∃ item `activo`                                   → activa
     Basta uno. Los bloqueos y esperas de los demás se reportan, no cambian el veredicto.

Q7   ∃ item `bloqueado`                                → bloqueada
     motivo: el trabajo real es CREAR EL DESBLOQUEADOR (b.15.1)

Q8   ∃ item VIVO — `en espera` · `aparcado` · `encuadrado` · `cancelando`  → esperando
     motivo: el de la espera dominante, con su clase

Q9   TODOS los items terminales (`cerrado` | `cancelado`):

       ∃ obligación de la INICIATIVA ni satisfecha ni retirada    → bloqueada
                                       motivo: obligación de iniciativa sin reemplazo
       gate_de_cierre NO cumplido                                 → lista-cierre
       gate_de_cierre cumplido                                    → cerrada
```

**Totalidad, demostrada y no afirmada.** Los diez estados globales de `b.4` quedan cubiertos:
`reconciliacion-pendiente` por Q0 · `cancelando` **de ITEM** por Q8 y `cancelado` **de ITEM**
por Q9 —`Q1` y `Q2` se disparan por la BANDERA DE LA INICIATIVA, no por el estado de un item,
y la glosa anterior los mezclaba— · `aparcado` por Q8 · `en desacuerdo` por Q5 · `activo` por
Q6 · `bloqueado` por Q7 · `en espera` y `encuadrado` por Q8 · `cerrado` por Q9. El conjunto vacío, por Q4. **No existe combinación
sin resultado, y ninguna produce dos**, porque gana la primera que se cumple.

**Los casos frontera, resueltos:**

| combinación | resultado |
|---|---|
| items activos junto a bloqueados y esperando | `activa` (Q6). El bloqueo se reporta |
| todos los vivos bloqueados | `bloqueada` (Q7). Ya no colisiona con «abierta» |
| algunos cerrados, otros esperando | `esperando` (Q8) |
| todos terminales, obligación de iniciativa huérfana | **`bloqueada` (Q9). NUNCA `cerrada`** — cerrar todos los items ni produce la obligación ni la retira |
| todos terminales, gate pendiente | `lista-cierre` (Q9). Es un estado ESTABLE: puede durar |
| todos cancelados sin bandera de iniciativa | Q9: si no hay obligación viva y el gate lo admite, `cerrada`; el informe dirá que se cerró por cancelación |
| cancelada con items aún vivos | **`cancelando` (Q1), nunca `cancelada`** |
| aparcada con un item en desacuerdo | `aparcada` (Q3), y el desacuerdo se reporta |

**Sólo `cerrada` exige un acto**: cumplir el gate. Las demás se calculan.

### 3.3.1.1 · Qué hacen las banderas con los items — la propagación, declarada

> **Corregido por la segunda devolución independiente (hallazgo `N-7`).** F4c definía qué
> **muestra** la iniciativa cuando lleva bandera y no definía qué **le pasa a sus items**. Las
> dos consecuencias eran:
>
> ```text
> `aparcada` ERA COSMÉTICA   los items seguían `activo`, `b.12` los seguía seleccionando y
>                            `Continúa` los seguía despachando. El Owner aparcaba una
>                            iniciativa y el sistema seguía trabajando en ella
> `cancelando` NO TENÍA      `Q1` da `cancelando` mientras haya un item VIVO, y nada cancelaba
> SALIDA                     esos items — por `b.4` P1 un item entra en `cancelando` por SU
>                            PROPIA bandera. `Q2` era inalcanzable salvo acción manual
> ```

**La propagación es una PROPUESTA, no una ejecución.** §5.4 ya declara que *«cancelar es
autoridad semántica»*, y `b.15` fija cómo se presenta lo que espera al Owner:

```text
AL MARCAR LA INICIATIVA   el sistema PROPONE la misma bandera para todos sus items VIVOS,
`aparcada` o `cancelada`  agrupados en UN LOTE (`G36`, `b.15` paso 2). No la aplica.

EL OWNER RESUELVE EL      item a item o en bloque. Cada aplicación es una orden por `a.9`,
LOTE                      con su evento y su atribución.

HASTA QUE LO RESUELVA     la iniciativa muestra su bandera y **sus items siguen su curso**.
                          La vista lo dice con todas las letras: «aparcada, con N items
                          todavía activos, pendientes de tu decisión». No sabe menos que el
                          estado, que es lo que §7.5 exige.

CONDICIÓN DE TERMINACIÓN  `Q1` (`cancelando`) termina cuando el Owner ha resuelto el lote y
DE `Q1`                   ningún item queda vivo. Si el Owner decide NO cancelar algún item,
                          la bandera de la iniciativa se retira: no se puede cancelar una
                          iniciativa cuyos items siguen vivos por decisión suya.
```

### 3.3.2 · Dónde vive el estado derivado

```text
NO SE PERSISTE EN UN     `00-iniciativa.md` es canónico y editable. Escribir allí el estado
FICHERO CANÓNICO         derivado crearía la segunda verdad que la propia decisión evita.

VIVE EN `dosier.md`      que es DERIVADO ENTERO, con su `source_revision` sobre los
                         canónicos de los que deriva: la iniciativa y sus items.

SI ALGUNA VEZ TUVIERA    sería en una ZONA REGENERABLE Y NO EDITABLE, delimitada y con su
QUE APARECER EN UN       `source_revision`, con la misma disciplina de dos zonas que `a.9`
CANÓNICO                 aplica al tablero. Hoy NO hace falta, y por tanto se omite y se
                         calcula.
```

**Prohibición.** Una iniciativa **no anida** en otra. Anidar convierte el estado derivado en
un cálculo sobre un árbol de profundidad arbitraria, y con él la vista del Owner. Si un
trabajo necesita árbol, es un cambio de dirección y su sitio es `DIR`.

**Umbral de activación.** `CI` reduce las nueve señales del §16 a una, porque las otras ocho
la aproximan: **su cierre no puede explicarse con un solo item**. Un bug, una dependencia
rutinaria o una feature localizada siguen usando item y paquetes.

**El dosier es derivado.** Índice y memoria, no copia: `I5` y el §15 del documento de
pendientes coinciden. Se genera desde la iniciativa, sus items, sus decisiones y su
evidencia. Un dosier que alguien mantiene a mano es una segunda verdad que envejece.

## 3.4 · `adaptador` — qué declara

Detallado en §6. Su contrato mínimo:

```text
id · entorno
compatibilidad_declarada            lo que el adaptador AFIRMA soportar. EDITABLE. Es una
                                    declaración de intención, y NO un logro
capacidades_del_entorno             subagentes · skills · límites de contexto · permisos.
                                    EDITABLE. Es una observación del entorno
lee                                 qué ficheros del control repo consume
proyecta                            qué ficheros GENERA, y dónde los descubre ese entorno
puntero_en_fuente                   el único fichero que proyecta DENTRO de una fuente, y
                                    qué declara. Ver §6.7
resolucion_del_control_repo         CÓMO localiza el control repo desde una fuente. Ver §6.7
                                      estrategia                `hermanos-del-workspace`
                                      profundidad_maxima        de ascenso desde el
                                                                directorio abierto
                                      normalizacion_del_remoto   sin credenciales · con y sin
                                                                `.git` · `ssh` y `https`
                                                                tratados como EQUIVALENTES
                                      desenlaces                para 0, 1 y ≥2 coincidencias,
                                                                más «no se pudo comprobar»
                                    **Añadido** (hallazgo `7`): §6.7 afirmaba que este campo
                                    se había añadido aquí, y no estaba. Sin él, un adaptador
                                    conforme podía omitir la resolución entera y seguir
                                    validando contra su tipo
escribe_permitido                   qué puede modificar, con las excepciones NOMBRADAS
comandos                            qué escribe el Owner y qué activa
degradacion                         qué se pierde y cómo, función por función
prueba_de_humo                      ref al escenario que lo certifica
huella                              de la definición de la que deriva cada proyección
```

**`nivel` NO es un campo, y esto es una corrección.** F4 entregada declaraba
`nivel: soportado | compatible | generico | desconocido` como campo editable del adaptador, y
a la vez §6.5 hacía de `soportado` una conclusión derivada de una prueba de humo ejecutada y
una certificación Integrada. Lo mismo escrito y derivado a la vez es la segunda verdad que
`I5` prohíbe, y además un campo editable **no caduca** mientras una certificación sí. El
nivel alcanzado se lee ahora en un solo sitio: §6.5.

## 3.5 · `cobertura` — qué declara

```text
sujeto      clase   componente | modulo | pantalla | flujo | formulario | patron |
                    api | integracion | entidad | migracion | entorno | pipeline |
                    despliegue | documento | agente | skill | adaptador | instalacion
            ancla   el COMPONENTE de C6 del que cuelga, o `transversal`
            ruta    dentro del ancla

aspecto     REFERENCIA TIPADA CON NAMESPACE. Qué propiedad del sujeto se juzga:
              aspecto:calidad/<nombre>          accesibilidad · responsive · rendimiento ·
                                               resiliencia · seguridad · dependencias …
              aspecto:documental/<area>         las doce áreas de O8 (§4.3)
              aspecto:certificacion/<nivel>     estructural · operativo · integrado ·
                                               completo (§9)
            Las tres familias tienen CONTRATO DISTINTO y se validan por separado.

responsables  la DESVIACIÓN respecto al reparto por defecto, cuando la hay, con su motivo.
              El reparto POR DEFECTO lo declara el `contrato-de-aspecto` (§5.7), que es
              norma y viaja con el release. Una capacidad NO es un aspecto: responde de él
              **Corregido** (hallazgo `N-1`): F4c declaraba `responsables` como campo de la
              celda Y como contenido del contrato del aspecto — dos sedes editables para la
              misma verdad, que es el defecto que la primera crítica corrigió en
              `ultima_verificacion_real` y que aquí se había reintroducido

criterio      ref al criterio concreto contra el que se juzga, y **resuelve siempre a un
              artefacto que existe**:
                `rubrica:<id>`                        ya existe en el corpus
                `contrato-de-aspecto:<familia>/<n>`   §5.7
                `nivel-certificacion:<nivel>`         §9.2
              Sin criterio, `verificado` no significa nada — y un criterio que no resuelve
              tampoco significa nada, que era el caso de `contrato:documental/O8`

evaluacion_de_pruebas   por cada prueba que el criterio enumera:
              prueba                        id de la prueba en la norma de clase
              aplicabilidad                 obligatoria | condicional | no-aplicable
              motivo_no_aplicable           obligatorio si `no-aplicable`
              evidencia_de_inaplicabilidad  obligatoria si `no-aplicable`
              resultado                     pendiente | pasa | falla | no-aplica
              **Añadido** (hallazgo `N-2`): la `aplicabilidad` de la celda es del par
              `(sujeto, aspecto)`, y `D32` y `PN-6` exigen evaluarla PRUEBA A PRUEBA. F4c
              metía esa evaluación «dentro del criterio», que es una norma de CLASE
              compartida por todas las instalaciones — y `SOURCES.toml@<SHA>` es un dato de
              ESTE producto y ESTA revisión. Es la forma que `integration-set.verificacion`
              ya usa en el corpus, con su `resultado: no-aplica` incluido

aplicabilidad   obligatoria | condicional | no-aplicable
motivo_no_aplicable   obligatorio cuando `no-aplicable`. El §5.18 lo exige: una evaluación
                      registrada, nunca una ausencia
evidencia_de_inaplicabilidad   obligatoria cuando `no-aplicable`. Un motivo sin evidencia
                      es una opinión, y una prueba no aplicable NO puede bloquear para
                      siempre ni desaparecer en silencio (§9.5)

estado      no-auditado | planificado | en-curso | parcial | findings-abiertos |
            corregido-sin-verificar | verificado | excepcion-aceptada | obsoleto | vencido

verificacion  ultima_real            no la última edición del fichero
              revisiones_examinadas  por fuente, el SHA. Es lo que hace la celda
                                     contrastable
              auditor                quién produjo el JUICIO de la celda, y qué
                                     independencia declara
              verificador_de_correccion  quién verificó la CORRECCIÓN, cuando el estado lo
                                     exige. Puede estar vacío: una celda `findings-abiertos`
                                     todavía no tiene nada que verificar
              **Corregido** (hallazgo `N-11`): F4c tenía un solo campo `verificador` que
              significaba el auditor en §5.6 y el verificador de la corrección en §5.3 — el
              mismo campo con dos sentidos en dos secciones, que es lo que §5.6 promete que
              no ocurre. Se parte, con la misma disciplina con que `D25` partió `dimension`
evidencia · findings   referencias a items
caducidad · triggers   qué la vence y qué la reabre
responsable_de_corregir
```

**`corregido` y `verificado` son estados distintos**, y ésa es la razón de que la lista sea
larga: fundirlos permitiría cerrar sin verificación independiente, que es `G13`.

**Por qué `aspecto` no puede ser «la capacidad que lo posee».** F4 entregada escribía
`dimension: ref a capacidad · la dimensión es la capacidad que la posee`, y con eso
**auditar la accesibilidad de una pantalla y auditar su responsive eran la misma celda**:
`DIS` posee las dos. No podían registrarse por separado, ni vencer por separado, ni tener
verificadores distintos. Y las doce áreas documentales y los cuatro niveles de certificación
—que no son capacidades— entraban en ese mismo campo sin namespace. Tres universos en un
campo sin tipo es una colisión semántica, no una economía.

## 3.6 · `evento` — qué declara, qué exige cada TIPO y qué exige cada FASE

### Campos comunes a todo evento

```text
id            EV-<huella del contenido>. Direccionado por contenido, NO monotónico (§2.7)
tipo          orden | transicion | integracion | certificacion | migracion | sellado |
              retirada-de-cuerpo | deriva | fallo. NUEVE valores, y la matriz de abajo dice
              cuáles llevan `fase` y cuáles la tienen PROHIBIDA
fase          preparada | confirmada | conflicto | reconciliacion-preparada | reconciliada |
              derivada | — (sin transacción). El autómata, en §2.6.1. **`fase` y `tipo` son
              DOS EJES**, y el valor `—` sólo lo toman `deriva` y `fallo`.
              `abortada` NO existe: un evento con esa fase es RECHAZADO por el ESQUEMA
              ESTRUCTURAL — es un valor fuera del enum, y eso se ve sin salir del evento
tx            TX-<huella>, cuando el evento forma parte de una transacción multiarchivo.
              Lo comparten todos los eventos de esa transacción y nadie más
orden         posición dentro de su transacción. Total dentro de ella
predecesor    el evento que este emisor observó como último. Forma la cadena verificable
ordenante · autoridad · escritor_del_comando · ejecutor · actor_atribuido
              los CINCO conceptos de a.9, sin confundirlos
base          hash de las entradas sobre las que se decidió
```

### Las DOS dimensiones, y la matriz que las cruza

> **Añadido por la segunda corrección técnica (hallazgo `H3`, GRAVE).** El contrato de
> abajo cubre el eje `fase` —seis fases más `deriva` y `fallo`, ocho filas— y se resumía
> como *«las ocho formas de evento»*. Pero el enum de `tipo` tiene **NUEVE** valores, y
> **siete de ellos quedaban sin contrato**: nada decía si un `sellado` lleva `fase`, si un
> `fallo` puede llevar `tx`, ni qué declara un `certificacion` además de su fase. Declarar
> «ocho formas» con formas válidas sin contrato es un recuento que no cierra. Es `D57`.
>
> **Y `D57` se quedó a medias, que es lo que `D59` corrige.** Contó **ocho filas de una
> tabla como si fueran ocho valores del eje `fase`** —`deriva` y `fallo` son valores de
> `tipo`—, y dio por obligatoria la transacción de `orden` **sin demostrarla tipo a tipo**.
> Las fases son **SEIS**; los estados del campo, **SIETE** contando su ausencia; y `orden` es
> **condicional**. `D57` conserva su texto.

**Son dos ejes, y no se sustituyen:**

```text
`tipo`    QUÉ ACONTECIÓ. El significado del acontecimiento: qué parte del producto cambia,
          quién tiene autoridad sobre ella y qué sujeto nombra el evento.

`fase`    CÓMO PARTICIPA EN UNA TRANSACCIÓN. Si el acontecimiento incluye al menos una
          ESCRITURA CANÓNICA, participa —y entonces `fase` y `tx` son OBLIGATORIOS—.
          Si no escribe nada canónico, no participa, y los dos están PROHIBIDOS.
```

**La regla, en una frase:** un evento lleva `fase` y `tx` **si y sólo si** el acontecimiento
que narra incluye una escritura canónica. Es la misma frontera que la regla 4 de abajo: lo
que exige intención durable previa es exactamente lo que exige fase.

**La prueba, tipo a tipo — y la matriz sale de ella, no al revés.**

> **Corregido por la tercera comprobación técnica (`D59`, que revisa `D57`).** La primera
> redacción afirmó *«siete tipos escriben estado canónico y llevan `fase` y `tx`
> obligatorios»* y derivó de ahí un **producto cartesiano** —`7 × 6 + 2 = 44`— **sin
> demostrarlo tipo a tipo**. Al demostrarlo, `orden` resulta **CONDICIONAL**: `a.9` describe
> consumos que **no aplican la orden y no modifican el estado canónico**, y un evento que no
> escribe nada canónico no tiene nada que proteger con una transacción. La matriz correcta es
> la **mínima que representa el sistema**, no el cartesiano máximo — y el recuento se
> **deriva** de ella en vez de encabezarla.

| `tipo` | sujeto | qué HECHO representa | ¿escribe canónicos además del propio evento? | ¿uno o varios ficheros? | ¿necesita `tx`? | ¿puede existir SIN `fase`? | ejemplo dentro de ADS |
|---|---|---|---|---|---|---|---|
| `orden` | la orden del Owner, y el item al que apunta | el **consumo** de una orden del canal `ÓRDENES` | **DEPENDE**: sí cuando la aplica al estado canónico; **no** cuando el consumo termina sin aplicarla — y en los dos casos se **marca la línea**, que es otra cosa (abajo) | varios cuando aplica | **DEPENDE** | **SÍ**, y sólo entonces | aplicar «sube la prioridad de `FEA-021`» escribe `02-control.md` → CON fase. Una orden cuya base ya no existe tras un rebase se marca `- [!]` y **no se aplica** (`a.9`) → SIN fase |
| `transicion` | un item | el item cambia de estado o avanza por su ruta | **sí** | varios: `01-ruta.md`, `03-integracion.md` y lo que la ruta toque | **sí, siempre** | **no** | `FEA-021` pasa de `en-ruta` a `integrado` |
| `integracion` | un item y la capa depositada | una capacidad deposita o integra su capa | **sí** | varios: el paquete en `paq/` y `03-integracion.md` | **sí, siempre** | **no** | `DIS` deposita su capa de diseño en `FEA-021/02` |
| `certificacion` | la celda `(sujeto, aspecto)` | una celda **alcanza, conserva o pierde** un nivel | **sí** | uno o varios de `estado/cobertura/` | **sí, siempre** | **no** | `pantalla:web/checkout` alcanza `aspecto:calidad/accesibilidad` |
| `migracion` | la instalación | el estado migra de una versión de esquema a otra | **sí** | **muchos**, y ése es su caso peor | **sí, siempre** | **no** | `esquema_estado: 3 → 4` sobre todos los items |
| `sellado` | los eventos de un item que se compactan | se **AÑADE** un fichero de sellado; ningún evento se edita ni se borra (§2.9) | **sí**: el fichero de sellado, que es la única fuente de reconstrucción sin Git | **uno, NUEVO y direccionado por su contenido** | **NO** — cae del lado que no la exige (abajo) | **SÍ, y es obligatorio** | al cerrar `FEA-021`, sus eventos se compactan en `SL-<huella>` |
| `retirada-de-cuerpo` | el evento sellado cuyo cuerpo se retira | el cuerpo se sustituye por su **lápida**, conservando id, huella y motivo | **sí**, y es la ÚNICA operación que **modifica** algo ya escrito bajo `estado/` | uno | **sí, siempre** | **no** | retirar el cuerpo largo de un evento sellado, con autoridad y motivo |
| `deriva` | el canónico que dejó de sostener lo que el diario afirma | **REPORTA**. No repara, no restaura y no completa (§2.6.11) | **no**: sólo se escribe a sí mismo | — | **no** | **SIEMPRE, y es obligatorio** | un canónico revertido bajo una `derivada` durable |
| `fallo` | una operación **no canónica** | **REPORTA** que esa operación falló. No repara | **no** | — | **no** | **SIEMPRE, y es obligatorio** | el push es rechazado porque el remoto avanzó (`W15`) |

**Los cuatro casos que la prueba obligó a separar, dichos uno a uno:**

```text
`orden`                REGISTRAR NO ES APLICAR. `a.9` da dos consumos que NO mutan: una
CONDICIONAL            orden cuya base ya no existe tras un rebase «se marca `- [!]` y NO SE
                       APLICA», y el agotamiento de `MAX_CAS_RETRIES`, donde DSP «deja TODAS
                       las órdenes sin consumir» y «NO modifica el estado canónico». En los
                       dos hay un HECHO que el Owner tiene que poder ver —por qué su orden no
                       se aplicó— y NINGUNA escritura canónica que proteger.
                       LA CONDICIÓN, EXACTA: `fase` y `tx` si y sólo si el consumo produce al
                       menos una escritura canónica. No hay tercera opción y no es a gusto
                       del emisor.
                       Y MARCAR LA LÍNEA, DICHO CON PRECISIÓN — porque «no escribe» sería
                       falso: marcar `- [ ]` → `- [x]` o `- [!]` **SÍ es una escritura
                       durable, y modifica físicamente el tablero**. Lo que NO es, es una
                       MUTACIÓN DEL ESTADO CANÓNICO gobernada por la transacción general:
                         · la zona `ÓRDENES` no tiene ejecutor de mutación canónica (§1.3),
                           y su campo canónico correspondiente es `02-control.md`
                         · se rige por el **protocolo CAS propio de `a.9`** —compare-and-swap
                           sobre HASH DE CONTENIDO, nunca `mtime`, con `MAX_CAS_RETRIES = 3`
                           y parada obligatoria—, que es un protocolo DISTINTO del de §2.6
                         · `a.9` declara la propia línea de orden «el registro write-ahead»,
                           y por eso el marcado converge sin `preparada`: al reiniciar, DSP
                           encuentra cada orden en el estado en que quedó y **no inventa
                           estado**
                       APLICAR LA ORDEN AL ESTADO CANÓNICO **SÍ usa `tx` y fases**. Son dos
                       escrituras con dos protocolos, y confundirlas es lo que haría creer
                       que el tablero se toca sin registro.

`sellado`              SELLAR AÑADE, NO REESCRIBE (§2.9): un fichero nuevo, direccionado por
NO TRANSACCIONAL,      su contenido, y ningún evento editado ni borrado. Por el criterio de
SIN AUTORREFERENCIA    la frontera —abajo— eso **NO exige `tx`**, y `sellado` es un evento
                       SIN `fase`. La regla que cierra la autorreferencia sigue en pie y
                       ahora es más simple: **un `sellado` NUNCA se incluye a sí mismo en su
                       alcance**, y §2.9 ya prohíbe retirar un evento vivo o el terminal de
                       cualquier transacción.

`retirada-de-cuerpo`   NO HAY DOS EVENTOS. El evento que REGISTRA la retirada **es** una fase
ES LA TRANSACCIÓN      de la transacción que la EJECUTA: su `preparada` declara `hash_previo`
                       = el evento íntegro y `hash_posterior_esperado` = la lápida, y su
                       `confirmada` ES el registro del hecho. Un segundo evento «que registra»
                       sería una segunda verdad sobre el mismo hecho. Y **sí exige `tx`**,
                       porque SUSTITUYE contenido previo — que es lo que lo separa de
                       `sellado` aunque los dos toquen el diario y escriban un solo fichero.

`certificacion`        EL JUICIO lo emite la capacidad responsable del aspecto (§1.3); su
JUICIO Y ESCRITURA     SEDE CANÓNICA es la celda de cobertura, y el evento narra esa
                       escritura. No son dos artefactos: el juicio no vive en el evento y el
                       evento no lo sustituye. Una reverificación que confirma el mismo nivel
                       TAMBIÉN escribe —`ultima_verificacion_real`—, luego también lleva fase.

`integracion` NO ES    el evento `integracion` narra el depósito de una CAPA en el estado de
`integration-set`      un item. El `integration-set` es OTRO artefacto: identidad propia
                       `IS-<nnn>`, ya normado antes de esta fase, con `ENT` como autoridad Y
                       como ejecutor (§1.3), y es la afirmación de que una combinación de
                       revisiones se probó junta (§10). **No es una fase de `integracion` y
                       este enum no lo nombra.**

`deriva` y `fallo`     INFORMATIVOS. No reparan, no restauran y no completan. Reparar exige
                       una transacción NUEVA (§2.6.11), y por eso no llevan fase: no hay
                       ninguna escritura canónica suya que proteger.
```

#### La frontera que exige una `tx`, y por qué NO es «añadir frente a modificar»

> **Corregido por la cuarta comprobación técnica (`D61`, que revisa `D59`).** La redacción
> anterior afirmaba **tres cosas que no pueden ser ciertas a la vez**: que `sellado` *«sólo
> AÑADE un fichero»*, que la frontera que evita la recursión es *«AÑADIR frente a
> MODIFICAR»*, y que `sellado` exige `tx` **siempre**. Si la frontera fuera añadir/modificar,
> `sellado` caería del lado de **no exigirla**, exactamente igual que añadir un `preparada`.
> La frontera era falsa, y estaba tapando que `sellado` estaba mal clasificado.

**La frontera real, y es UN solo criterio aplicado a todo por igual:**

```text
UNA ESCRITURA CANÓNICA EXIGE `tx` SI Y SÓLO SI la recuperación NO PUEDE DECIDIR QUÉ HACER
mirando el fichero y su nombre. Eso ocurre cuando se cumple AL MENOS UNA de dos:

  1  TOCA MÁS DE UN FICHERO CANÓNICO
     el CONJUNTO puede quedar incoherente aunque cada `rename` sea atómico, y para
     completarlo hace falta la lista, el `orden` y los hashes. Es `a.9` literal: «Git no
     convierte una secuencia de escrituras en una transacción».

  2  SUSTITUYE CONTENIDO PREVIO
     la recuperación necesita `hash_previo` y `hash_posterior_esperado` para distinguir
     «no aplicado» de «lo tocó otro» (§2.6.4). Sin esos dos hashes, las tres cajas no se
     pueden formar y sobrescribir destruiría trabajo sin registro.

NO EXIGE `tx` la escritura que sea LAS DOS COSAS A LA VEZ: **UN SOLO FICHERO, NUEVO Y
DIRECCIONADO POR SU CONTENIDO**. Ahí el NOMBRE ES LA VERIFICACIÓN:
     · está y su contenido casa con su nombre  → hecho, nada que completar
     · no está, o es un temporal huérfano      → no ocurrió, y se borra el temporal (`W2`)
No hay estado anterior que conservar, no hay partner que quede a medias, y no hay nada
que declarar por adelantado para poder rehacerlo.
```

**Aplicado a las cinco cosas que ADS escribe bajo `estado/`** —y «estar bajo `estado/`» no
es el criterio, porque el diario también está allí:

| qué se escribe | ¿varios ficheros? | ¿sustituye contenido? | ¿exige `tx`? |
|---|---|---|---|
| un item, una celda de cobertura, una iniciativa | **sí**, casi siempre | **sí** | **SÍ** |
| un **evento** del diario (`preparada`, `confirmada`, `derivada`…) | no: uno | no: es nuevo, y su nombre es su huella (§2.8) | **NO** |
| un **fichero de sellado** | no: uno | no: `sellar AÑADE` (§2.9), y nada se reemplaza | **NO** |
| la **lápida** de un cuerpo retirado | no: uno | **SÍ**: reemplaza el cuerpo de un fichero que ya existe | **SÍ** |
| un derivado | — | — | **no**: no es canónico. Se regenera entero (`W7`) |

#### `sellado` — la decisión, y por qué cambia

**Se comprueba una a una lo que `sellado` hace, contra §2.9:**

```text
¿SÓLO AÑADE UN FICHERO?   SÍ. §2.9: «sellar AÑADE: escribe un fichero de sellado nuevo y
                          emite el evento que lo registra. NINGÚN evento se edita».

¿MODIFICA O ELIMINA       NO. Los eventos sellados **siguen donde estaban**. Lo único que
EVENTOS EXISTENTES?       puede retirarse es un CUERPO, y eso es `retirada-de-cuerpo`: un
                          acto SEPARADO, autorizado y registrado, que §2.9 declara «no una
                          limpieza automática por antigüedad».

¿ACTUALIZA ÍNDICES O      NO. Los índices, tableros, vistas y dosieres son DERIVADOS (§1.3):
ESTADO DEL ITEM?          se regeneran, y editarlos no es una escritura canónica. Y el
                          «estado final del item» que el sellado conserva va DENTRO del
                          fichero de sellado — no se escribe en el item. Cerrar el item es
                          un `transicion`, que es otro evento y otra transacción.

¿UNA ESCRITURA DURABLE    **UNA.** Un solo fichero, con la disciplina de §2.6.3
O UNA MUTACIÓN            —`temporal → fsync → rename → fsync(directorio)`—, que es la
MULTIARCHIVO?             disciplina de DURABILIDAD y no la de transacción.
```

**Conclusión: `sellado` NO es transaccional.** No lleva `fase` ni `tx`, exactamente por el
mismo criterio por el que no lo lleva añadir un `preparada` — y sostener lo contrario exigía
la frontera falsa que `D61` retira. Con dos condiciones que se declaran aquí porque el
criterio las necesita:

```text
EL FICHERO DE SELLADO SE   `SL-<huella>`, como el evento y por el mismo motivo (§2.8): su
DIRECCIONA POR CONTENIDO   nombre es su verificación. Sin esto, el criterio no se cumple y
                           `sellado` volvería a exigir `tx`.

NUNCA SE REEMPLAZA         un sellado posterior del mismo item produce un fichero NUEVO. El
                           anterior no se toca, y cuál es el vigente **se deriva** —cada
                           sellado declara la cabeza de la cadena `predecesor` al sellar
                           (§2.9)—, no se escribe en ningún índice. Reemplazarlo sería
                           «sustituir contenido previo», y entonces sí exigiría `tx`.
```

#### `retirada-de-cuerpo` — qué modifica, y por qué NO hay recursión

```text
QUÉ FICHERO EXISTENTE     el del EVENTO SELLADO cuyo cuerpo se retira. Es la ÚNICA
MODIFICA                  operación de ADS que sustituye contenido ya escrito bajo
                          `estado/`, y por eso es la única que cae del lado 2 de la
                          frontera siendo un solo fichero.

QUÉ PARTE DEL DIARIO      **NO es «la historia no se reescribe»**: esta operación EDITA
SIGUE SIENDO INMUTABLE    físicamente un fichero existente, y el diario FÍSICO no es
                          estrictamente append-only (§2.9, `D63`). Lo inmutable son los
                          EVENTOS y sus CABECERAS LÓGICAS: la lápida conserva `id_original`,
                          `fase`, `tx`, `posicion` y `predecesor`, luego la cadena sigue
                          RESOLVIENDO y el ORDEN sigue recorriéndose. Eso es el NIVEL 1 de
                          §2.9, y **no verifica ningún contenido**.
                          EL PRECIO, DICHO: el `id` deja de ser recomputable desde el
                          fichero, y por eso §2.8 punto 4bis TIPA la excepción — sobre una
                          lápida NO se aplica la fórmula ordinaria de identidad.
                          Y LO QUE LA HUELLA NO DA: es un COMPROMISO, no una prueba de
                          contenido. Que esté en la lápida Y en el sellado demuestra que el
                          repositorio CONSERVÓ ESE COMPROMISO y registró la retirada —NIVEL
                          2—, no cuál era el cuerpo. Afirmar lo segundo exige tener el
                          cuerpo original delante: es el NIVEL 3, y depende del
                          `localizador` comprobado antes de retirar.
                          QUÉ BLOQUEA LA RETIRADA: una DEPENDENCIA SEMÁNTICA VIVA —alguien
                          que necesita LEER el cuerpo—, el evento terminal de cualquier
                          transacción, y la falta de fuente de recuperación comprobada. Una
                          referencia ESTRUCTURAL por `predecesor` **no** bloquea: si lo
                          hiciera, la operación sería inalcanzable (§2.9).

QUÉ EVENTO NUEVO          **ninguno aparte**. Las fases de su PROPIA transacción llevan
REGISTRA LA RETIRADA      `tipo: retirada-de-cuerpo`, y su `confirmada` ES el registro del
                          hecho. Un segundo evento «que lo registra» sería una segunda
                          verdad sobre el mismo hecho.

POR QUÉ NO HAY            porque esas fases son ficheros NUEVOS, uno cada una, direccionados
RECURSIÓN                 por su contenido: caen del lado que NO exige `tx`. La recursión se
                          corta **por el criterio general**, no por una excepción escrita
                          para el diario. Escribir un `preparada` no abre otra transacción
                          para registrar que se escribió un `preparada`, y lo mismo vale
                          para el `preparada` de una retirada de cuerpo.
```

**Y por eso `sellado` y `retirada-de-cuerpo` acaban en lados distintos**, que es lo que la
frontera falsa impedía ver: los dos tocan el diario, los dos escriben un solo fichero, y sólo
uno **sustituye contenido previo**.

**El recuento, DERIVADO de la tabla y separado por ejes.** No es una métrica de calidad ni un
titular: es la consecuencia de las nueve filas de arriba.

```text
VALORES DE `tipo`               9   orden · transicion · integracion · certificacion ·
                                    migracion · sellado · retirada-de-cuerpo · deriva · fallo

FASES TRANSACCIONALES           6   preparada · confirmada · conflicto ·
                                    reconciliacion-preparada · reconciliada · derivada
                                    `deriva` y `fallo` NO SON FASES: son valores de `tipo`

ESTADOS DEL CAMPO `fase`        7   las SEIS fases, más la AUSENCIA del campo. La ausencia no
                                    es un séptimo valor del enum: es que el campo no está

ESPACIO BRUTO                  63   9 × 7, y la mayor parte NO es válida

LOS TRES REGÍMENES             SIEMPRE TRANSACCIONAL      5   transicion · integracion ·
                                                              certificacion · migracion ·
                                                              retirada-de-cuerpo
                               CONDICIONAL                1   orden
                               SIEMPRE NO TRANSACCIONAL   3   sellado · deriva · fallo

COMBINACIONES VÁLIDAS          40   5 tipos SIEMPRE transaccionales × 6 fases  = 30
                                    `orden`, CONDICIONAL: 6 con fase + 1 sin   =  7
                                    `sellado` sin fase                         =  1
                                    `deriva` sin fase                          =  1
                                    `fallo` sin fase                           =  1

COMBINACIONES PROHIBIDAS       23   los 5 siempre transaccionales SIN fase      =  5
                                    `sellado` con cualquiera de las 6 fases     =  6
                                    `deriva` con cualquiera de las 6 fases      =  6
                                    `fallo` con cualquiera de las 6 fases       =  6
                                    40 + 23 = 63, y la partición cierra
```

> **Lo que se retira, dicho en positivo.** «Las ocho formas de evento» contaba **mezclando
> ejes** —metía `deriva` y `fallo` en el eje `fase`—; «`7 × 6 + 2 = 44`» daba por obligatoria
> una transacción para `orden` sin demostrarlo; y «`45`» seguía dando por transaccional un
> `sellado` que sólo añade un fichero. **Las fases son SEIS**, `deriva`, `fallo` y `sellado`
> son valores de `tipo` **sin** fase, y `orden` es condicional. El recuento vigente es **40 ·
> 23 · 63**, y se **deriva** de la tabla de arriba: no se conserva ninguno por arrastre.

**Combinaciones prohibidas, y quién las rechaza** (capas de §3.6, más abajo):

```text
`deriva` o `fallo` CON `fase` o CON `tx`          ESQUEMA ESTRUCTURAL. Es coherencia
                                                  interna: `tipo` y `fase` viven en el
                                                  MISMO evento
CUALQUIERA DE LOS CINCO SIEMPRE                   ESQUEMA ESTRUCTURAL, por lo mismo
TRANSACCIONALES SIN `fase` O SIN `tx`
`sellado` CON `fase` O CON `tx`                   ESQUEMA ESTRUCTURAL: `sellado` es una
                                                  escritura única de un fichero nuevo
                                                  direccionado por contenido, y no la
                                                  exige
UN `orden` CON `fase` QUE NO DECLARE NINGUNA      ESQUEMA ESTRUCTURAL: si lleva fase, su
ESCRITURA CANÓNICA, O SIN `fase` DECLARANDO       `preparada` declara `afecta[]`, y si no
UNA                                               la lleva no puede declarar ninguna
`fase: abortada`, con cualquier `tipo`            ESQUEMA ESTRUCTURAL: fuera del enum
`tx_afectada` sin `causa: posterior-al-cierre`    ESQUEMA ESTRUCTURAL
UN EVENTO CON `fase` CUYO `tx` YA TIENE           VALIDADOR SEMÁNTICO DEL DIARIO: exige
`derivada`                                        recorrer los demás eventos de ese `tx`
UN `intento: 4`, O UNA `observacion` MAYOR        VALIDADOR SEMÁNTICO DEL DIARIO: exige
QUE 4, O UNA `reconciliacion-preparada` QUE       contar los `conflicto` de ese `tx` y
RESUELVA UN `conflicto` CON `agotado: true`       seguir sus referencias
```

**No se crea ningún tipo, y no se fusiona ninguno.** La prueba de §3.1 **no llega a
plantearse**: los nueve valores son valores de un **enum** dentro del tipo `evento`, no tipos
candidatos con sujeto, autoridad y ciclo propios. El recuento de §3.8 **no cambia**.

### El contrato condicional, fase a fase

> **Qué cubre esta tabla, y qué NO.** Sus **seis primeras filas son las seis FASES**. Las
> dos últimas —`deriva` y `fallo`— **no son fases**: son los dos valores de `tipo` que nunca
> la llevan, y están aquí porque sin ellos el contrato del evento quedaría incompleto. **La
> tabla tiene ocho filas y el eje `fase` tiene seis valores**, y confundir las dos cosas es
> lo que `D59` corrige. Un evento válido cumple **su fila de tipo** en la prueba de arriba
> **y**, si lleva fase, su fila de fase aquí.

> **Añadido por la corrección técnica posterior (hallazgo `3`, GRAVE).** El contrato anterior
> declaraba un `afecta` genérico —`hash_previo` · `hash_posterior_esperado`— y un `resultado`
> descrito sólo para `preparada` y `confirmada`. **No podía representar** el `hash_observado`
> de un conflicto, ni la copia de lo divergente, ni la decisión de una reconciliación, ni su
> `hash_final`, ni los derivados pendientes. Un esquema derivado de ese contrato aceptaría un
> `conflicto` sin copia de lo divergente y una reconciliación sin resultado reproducible —y
> §2.6 declara que las dos cosas son defectos—. Es `D54`.

| fase | predecesora admitida | campos OBLIGATORIOS | campos PROHIBIDOS | hash que gobierna | condición para emitir la siguiente |
|---|---|---|---|---|---|
| `preparada` | ninguna: abre la transacción | `afecta[]` con `ruta`·`hash_previo`·`hash_posterior_esperado`·`orden`· una de `contenido`\|`parche`\|`operacion` · los cinco de `a.9` · `base` | `resultado` · `hash_observado` · `hash_final` · `decision` | `hash_posterior_esperado` | los N ficheros casan con su hash posterior → `confirmada`; alguno diverge → `conflicto` |
| `confirmada` | `preparada` | `resultado` · `derivados_pendientes[]` | `decision` · `hash_final` · `hash_observado` | `hash_posterior_esperado` | los derivados de `derivados_pendientes` se regeneraron → `derivada` |
| `conflicto` | `preparada` o `reconciliacion-preparada` | `divergentes[]` con `ruta`·`hash_observado`· **`contenido` íntegro de lo divergente** · `items[]` · `rutas[]` · `autoridad` que debe resolver · `observacion` ∈ 1..4 · `intentos_consumidos` ∈ 0..3 · `agotado` **sólo `true` con `observacion: 4`** | `resultado` · `hash_final` · `decision` | ninguno: declara lo observado, no lo esperado | la autoridad decide y su decisión es durable → `reconciliacion-preparada` con `intento` = `observacion`, **para las observaciones 1, 2 y 3**; con `agotado: true` **no admite ninguna**: se detiene, se escala y la transacción queda abierta (§2.6.4) |
| `reconciliacion-preparada` | `conflicto` **sin `agotado: true`** | `decision[]` con `ruta`·`hash_observado`·`hash_final`·`orden`· una de `contenido`\|`parche`\|`operacion` · `autoridad` que decidió · `derivados_pendientes[]` · `intento` ∈ 1..3 · `resuelve` = `id` del `conflicto` que resuelve | `resultado` · `agotado` · `observacion` | `hash_final`, que **sustituye** al `hash_posterior_esperado` para esas rutas | los ficheros de `decision` casan con su `hash_final` → `reconciliada`; alguno vuelve a divergir → `conflicto` |
| `reconciliada` | `reconciliacion-preparada` | `resultado` · `derivados_pendientes[]` | `decision` · `hash_posterior_esperado` para las rutas reconciliadas | `hash_final` | los derivados de `derivados_pendientes` se regeneraron → `derivada` |
| `derivada` | `confirmada` o `reconciliada` | `derivados_regenerados[]` con su `source_revision` | `afecta` · `decision` · `divergentes` | el que gobernara su ruta | **ninguna. Es terminal**. Que no exista ningún evento posterior con ese `tx` lo comprueba el **validador semántico del diario**, no el esquema |
| `deriva` | **ninguna: NO tiene `tx` ni `fase`** | `causa` ∈ {`posterior-al-cierre`,`sin-transaccion`} · `afecta[]` con `ruta`·`hash_esperado`·`hash_observado` · `items[]` · `autoridad` · `tx_afectada` sólo si `causa: posterior-al-cierre` | `fase` · `tx` · `decision` · `resultado` | ninguno: **reporta**, no repara | ninguna. La reparación es una transacción NUEVA (§2.6.11) |
| `fallo` | **ninguna: NO tiene `tx` ni `fase`** | `operacion` · `diagnostico` · `intentos` | `fase` · `afecta` | — | ninguna |

### Las cuatro reglas, y QUIÉN puede hacer cumplir cada una — tres capas

> **Corregido por la segunda corrección técnica (hallazgo `H1`, GRAVE).** Las cuatro reglas
> se enunciaban como *«reglas que un esquema derivado debe hacer cumplir»*, y **tres de las
> cuatro son incomprobables por un esquema**. Un esquema estructural valida **un evento
> aislado**: no abre los demás ficheros del diario, no reconstruye el autómata y no observa
> el orden real de `fsync` y `rename` en el disco. Atribuirle esas garantías no las
> proporciona: las deja **sin dueño**, que es la forma en la que un contrato falla en
> silencio. Es `D55`, y revisa `D54`.

**Las tres capas, y qué puede comprobar cada una.** Ninguna promete lo de otra:

```text
A · ESQUEMA ESTRUCTURAL      valida UN evento aislado, sin abrir ningún otro fichero.
    DEL EVENTO               Se ejecuta al escribir el evento, antes de publicarlo.

B · VALIDADOR SEMÁNTICO      valida el DIARIO: recorre todos los eventos de un `tx` —y, para
    DEL DIARIO               lo que lo exige, del diario entero—. Se ejecuta al arrancar, al
                             recuperar y en cada auditoría de integridad.

C · RUNTIME Y PRUEBAS        garantiza o DEMUESTRA lo FÍSICO: el orden real de las llamadas
    DE CAÍDA                 al sistema, la durabilidad, los locks y la comparación contra
                             el disco. No hay validación de texto que lo sustituya: se
                             prueba matando el proceso y cortando la corriente.
```

#### A · Qué comprueba el ESQUEMA ESTRUCTURAL del evento

```text
· campos OBLIGATORIOS y PROHIBIDOS de la fila que le corresponde en la tabla de arriba
· ENUMS: `tipo`, `fase`, `causa`, `decision[].tipo`. `abortada` cae aquí: está fuera del enum
· TIPOS de cada campo, y su cardinalidad
· FORMA de los hashes —algoritmo declarado y longitud—, del `id`, del `tx` y del `orden`
· EXCLUSIÓN ENTRE PAYLOADS: exactamente uno de `contenido` | `parche` | `operacion` por ruta
· COHERENCIA INTERNA del propio evento: que `tipo` y `fase` sean una combinación admitida
  por la matriz de §3.6; que `deriva` y `fallo` no lleven `fase` ni `tx`; que un `conflicto`
  lleve `divergentes[].contenido`; que una `reconciliacion-preparada` lleve `decision[]` con
  su `hash_final`; que `tx_afectada` sólo aparezca con `causa: posterior-al-cierre`
· UNICIDAD DE `ruta` dentro del array del propio evento, y `orden` total dentro de él
· QUÉ ALGORITMO DE IDENTIDAD APLICAR, antes de aplicarlo: si el evento lleva
  `cuerpo_retirado: true` es una LÁPIDA, y **NO se le aplica `EV-H(evento MENOS id)`** —la
  preimagen ya no está—; se valida su estructura (§2.9). Sobre un evento íntegro sí se aplica
  y debe reproducir su `id`. Confundirlos es el defecto que `X-H` comprueba (§2.8, 4bis)
· LOS DOS CONTADORES DE LA RUTA DE CONFLICTO, en lo que se ve sin salir del evento:
  `observacion` ∈ 1..4 · `intentos_consumidos` ∈ 0..3 · `intentos_consumidos` = `observacion`
  − 1 · `agotado: true` **sólo** con `observacion: 4` · `intento` ∈ 1..3, y **`intento: 4` no
  existe**. Lo que NO ve: si esa `observacion` es realmente la siguiente de su `tx` — eso es
  del validador del diario
```

**Lo que NO puede**, y por eso no se le pide: nada que exija otro fichero, otro evento, otro
momento o el disco.

#### B · Qué comprueba el VALIDADOR SEMÁNTICO DEL DIARIO

Recorriendo **todos los eventos**, y por eso ninguna de estas comprobaciones cabe en A:

```text
· IDENTIDAD Y UNICIDAD DE `tx`: que el `tx` se calcule como declara §2.8 y que no haya dos
  transacciones distintas compartiéndolo
· PREDECESOR: que la cadena `predecesor` cierre, y que una BIFURCACIÓN se DETECTE (`X09`)
· TRANSICIONES ADMITIDAS: que el par (fase anterior, fase nueva) esté en la tabla de §2.6.1
· CONTINUIDAD DE HASHES entre fases: que el `hash_final` de una `reconciliacion-preparada`
  gobierne desde ahí, y que `derivada` cierre sobre el hash que gobernaba cada ruta
· NINGUNA FASE POSTERIOR A `derivada` en ese `tx`. **Ésta es la regla 1**, y es de diario
· OBSERVACIONES E INTENTOS, que son DOS cuentas: `observacion` empieza en 1, es consecutiva y
  no pasa de **4**; `intento` empieza en 1, es consecutivo y no pasa de **3**; en cada
  `conflicto` se cumple `intentos_consumidos` = `observacion` − 1; `agotado: true` aparece
  **sólo** con `observacion: 4`; toda `reconciliacion-preparada` tiene `intento` = la
  `observacion` del `conflicto` que su campo `resuelve` referencia; y **no existe ninguna
  `reconciliacion-preparada` cuyo `resuelve` apunte a un `conflicto` con `agotado: true`**.
  **El cuarto reintento no lo ve un esquema**: exige contar los `conflicto` de ese `tx`
· TERMINALIDAD: exactamente un `derivada` por transacción cerrada, y ninguno en las abiertas
· CORRESPONDENCIA ENTRE INTENCIÓN Y HECHO: que todo `confirmada` tenga su `preparada`, toda
  `reconciliada` su `reconciliacion-preparada`, y que las rutas y hashes coincidan
· CARDINALIDAD DE CADA FASE, **CONDICIONAL A LA RUTA** (§2.6.4): `preparada` exactamente 1
  siempre; `confirmada` y `reconciliada` **mutuamente excluyentes** —1 y 0 en la ruta normal,
  0 y 1 en la de conflicto cerrada, 0 y 0 en la agotada—; `derivada` 1 si cerró y 0 si sigue
  abierta. **Ninguna secuencia contiene `confirmada → confirmada`.** Sólo `conflicto` y
  `reconciliacion-preparada` se repiten, con `observacion` e `intento` como discriminadores
  respectivos y máximos **4 observaciones** y **3 intentos**
· LÁPIDA Y SELLADO, VINCULADOS: para todo evento con `cuerpo_retirado: true`, el sellado que
  lo ancla declara el MISMO `id_original`, `hash_cuerpo_original`, `fase`, `tx` y posición.
  Una discrepancia es un fallo (`X-A`–`X-D`), y comprobarla exige abrir DOS ficheros: por eso
  es de esta capa y no del esquema
· QUÉ NIVEL DE GARANTÍA SE ALCANZA, declarado y no supuesto: con lápida y sin cuerpo original
  disponible, NIVEL 1 y NIVEL 2 sí, **NIVEL 3 no** — y el validador lo REPORTA en vez de
  afirmar integridad histórica completa (§2.9)
· LA IDENTIDAD DE LA RUTA: #observaciones = #intentos en una transacción de conflicto
  CERRADA, y #observaciones = #intentos + 1 en una AGOTADA — y en la agotada ese `+1` es
  siempre el `conflicto` con `agotado: true`
· EMISIÓN FRENTE A RESTAURACIÓN: restaurar un evento durable perdido devuelve el MISMO `id`,
  el MISMO cuerpo y el MISMO `predecesor`. Un `id` nuevo con el mismo `tx` y la misma fase de
  HECHO es un defecto, no una reemisión
· CONSISTENCIA DEL AUTÓMATA COMPLETO: que la secuencia de fases de cada `tx` sea un camino
  admitido de §2.6.1, y no una colección de eventos que por separado validan
```

#### C · Qué garantizan o DEMUESTRAN el RUNTIME y las PRUEBAS DE CAÍDA

Nada de esto es observable en el texto de un evento, y por eso **la regla 4 vive aquí**:

```text
· ORDEN EFECTIVO DE ESCRITURA: `temporal → fsync(temporal) → rename → fsync(directorio)`
· `fsync` DEL EVENTO Y DE SU DIRECTORIO ANTES DEL PRIMER CANÓNICO. **Ésta es la regla 4**:
  «ninguna escritura canónica sin intención durable previa» es una afirmación sobre el
  ORDEN REAL DE DOS LLAMADAS AL SISTEMA, y ningún esquema puede observarla
· LOCKS: que `R5` sea un lock y no un consejo, y que el segundo ejecutor no arranque
· COMPARACIÓN CONTRA EL DISCO: la clasificación de §2.6.4 y la integridad post-terminal
  comparan CONTENIDO REAL, no lo que el diario afirma
· ROLL-FORWARD IDEMPOTENTE: que dos recuperaciones seguidas converjan al mismo estado
· QUE NINGUNA ESCRITURA CANÓNICA OCURRA SIN INTENCIÓN DURABLE PREVIA — se DEMUESTRA con
  `X55` y con las ventanas de caída, no se declara
```

**Las cuatro reglas, reasignadas a la capa que puede comprobarlas:**

| # | la regla | capa | por qué no puede estar en otra |
|---|---|---|---|
| 1 | ningún evento con `fase` cuya transacción ya tenga `derivada` | **B** | exige recorrer los demás eventos de ese `tx` |
| 2 | ningún `conflicto` sin `divergentes[].contenido` | **A** | es coherencia interna del propio evento |
| 3 | ninguna `reconciliacion-preparada` sin `decision[]` reproducible y su `hash_final` | **A** la presencia y la forma · **B** que su base observada case con lo que el `conflicto` anterior registró | la presencia es del evento; la correspondencia con el conflicto es del diario |
| 4 | ninguna escritura canónica sin intención durable previa | **C**, y sólo C | es una propiedad del ORDEN FÍSICO de las escrituras. Ni A ni B ven el disco |

> **La regla que resume el reparto:** **no se le atribuye a JSON/YAML Schema ninguna
> propiedad histórica o física que no pueda observar.** Un esquema que «rechaza» un cuarto
> reintento, una transición no admitida o una escritura sin intención durable previa está
> prometiendo lo que no comprueba — y una promesa así es peor que no tenerla, porque nadie
> construye después el mecanismo que sí lo haría.

**Un evento no se edita para corregirlo, y nunca narra en futuro.** Corregir un evento se
hace emitiendo otro que lo rectifica y lo enlaza — **nunca** reescribiendo el que ya está.

> **La ÚNICA excepción autorizada, y está acotada: `retirada-de-cuerpo`.** El contrato
> completo, con sus once puntos y sus ocho comprobaciones `X-A`–`X-H`, vive en §2.9. Aquí
> queda lo que esta sección tiene que decir:
>
> ```text
> QUÉ SE PUEDE TOCAR      SÓLO el CUERPO —el texto largo— de un evento YA SELLADO, y sólo
>                         con su fuente de recuperación COMPROBADA de antemano. Nunca un
>                         evento con dependencia semántica viva, ni el terminal de una
>                         transacción.
>
> ES UNA EDICIÓN FÍSICA   y se dice: sustituir un cuerpo **SÍ edita un fichero existente**.
> REAL                    El diario FÍSICO no es estrictamente append-only. Lo inmutable son
>                         los eventos y sus CABECERAS LÓGICAS; ésta es la ÚNICA mutación
>                         física autorizada, tipada, transaccional y registrada (§2.9).
>
> CABECERA E IDENTIDAD    SE CONSERVAN: `id_original`, `fase`, `tx`, `posicion` y
>                         `predecesor`. La cadena sigue resolviendo, y el recorrido
>                         estructural no necesita ningún cuerpo.
>
> LA IDENTIDAD NO SE      **es la excepción tipada de §2.8 punto 4bis.** Sobre una lápida NO
> RECALCULA               se aplica `EV-H(evento MENOS id)`: la preimagen ya no está. Hacerlo
>                         es un defecto del validador, no un fallo del evento (`X-H`).
>
> QUÉ GARANTIZA CADA      NIVEL 1 continuidad estructural · NIVEL 2 consistencia del
> NIVEL                   compromiso · NIVEL 3 verificación completa, que **exige el cuerpo
>                         original** desde el `localizador` declarado. Sin él, los niveles 1
>                         y 2 siguen y el 3 NO, y el sistema lo declara (§2.9).
>
> LO QUE NO SE AFIRMA     que la huella demuestre que el cuerpo existió, ni cuál era. Una
>                         huella es un COMPROMISO: sin preimagen no prueba contenido. Y no
>                         se afirma que Git conserve eternamente: la dependencia de retención
>                         de historia, o de archivo externo, queda declarada.
>
> CUALQUIER OTRA EDICIÓN  SIGUE PROHIBIDA. No hay una segunda excepción, y añadir una
>                         exigiría pasar la misma prueba: qué se toca, qué se conserva, cómo
>                         se verifica, con qué autoridad y con qué registro.
> ```

**Y la segunda mitad de la regla:** una intención se registra con una fase que dice
«preparada», y hay dos. Las dos juntas son lo que hace que el diario sea una historia y no
una lista de deseos.

## 3.7 · Extensiones, sin tipo nuevo

```text
memoria.yaml          + `estado` — ciclo NORMATIVO PROPIO del documento, de CUATRO valores.
                      NO es estado de verificación: ése es de la celda. Ver §4.2
                      **Corregido** (hallazgo `J`): F4c escribía `vigente | sustituida |
                      retirada` y lo atribuía a `b.3`. `b.3` dice
                      `vigente | sustituida | INVALIDADA`, y `retirada` en `b.3` es un
                      predicado sobre OBLIGACIONES, no sobre capas
                      + `plano` OBLIGATORIO — uno de los cinco planos de §1.2
                      `capa` pasa a CONDICIONAL: sólo la declara conocimiento que viaja
                      con un release
                      y su sujeto SE GENERALIZA de «sección del corpus de un equipo» a
                      «documento gobernado». Es una GENERALIZACIÓN, y se dice. Ver §4
                      NO recibe `ultima_verificacion_real`: ésa vive sólo en `cobertura`
validadores.yaml      + `entradas:` — resuelve P-08. Ver §11
paquete               ya tiene `lee_fuentes` y `escribe_fuentes` por E2.2, y aloja los
                      source changes por E2.3. No necesita nada más
checkpoint            sin cambios. E2.3 ya le dio forma multi-fuente
```

## 3.8 · El recuento final, calculado

```text
TIPOS CANÓNICOS DE ESTADO NUEVOS · CUATRO
    iniciativa · adaptador · cobertura · evento
    Los cuatro pasan el paso 4 de §3.1: sujeto propio, autoridad propia y ciclo propio.

LO QUE DEJA DE SER TIPO · UNO
    el manifiesto de transacción. Se pliega en `evento` como una `fase`, y §2.5 comprueba
    propiedad a propiedad que no se pierde ninguna.

ESQUEMAS DE CLASE NUEVOS · DOS, Y NINGUNO ES TIPO DE ESTADO
    `nivel-certificacion`. Aloja pruebas, propietario, crítico, jerarquía e invalidación de
    cada nivel. Es NORMA, no estado. Su precedente exacto está en el corpus:
    `esquemas/nivel-novedad.yaml`. Ver §9.2.
    `contrato-de-aspecto`. Aloja el reparto de responsables POR DEFECTO, el criterio, las
    pruebas, la caducidad y los triggers de una FAMILIA de aspectos. Misma clase de
    artefacto, mismo precedente. **Añadido por la segunda devolución independiente**: F4c
    lo invocaba TRES VECES como sede normativa y no lo definía, ni lo contaba. Ver §5.7.

ESQUEMAS AMPLIADOS · DOS
    `memoria` (generalizado, §4) · `validadores` (bloque `entradas:`, §11)

TOTAL   19 esquemas vigentes + 4 tipos de estado + 2 de clase = **25**
```

> **El recuento se recalcula, y por eso cambia.** Pasó de «cuatro y ni uno más» a 24 en la
> primera devolución, y de 24 a 25 en la segunda. Un recuento que se calcula **se mueve
> cuando aparece algo que no se había contado**; uno que se fija de antemano, no. Esa
> diferencia es exactamente lo que §3.1 existe para proteger.

**Por qué `nivel-certificacion` no cabe en `gate`.** Un gate declara comprobaciones,
evidencia y consecuencia al fallar. Un nivel declara además **qué nivel presupone** y **qué
lo invalida**. Añadir esos dos campos a `gate` se los daría a todos los gates del sistema
para que sólo los usara la certificación, que es la definición de deformar un tipo — el paso
1 de §3.1 leído al revés.

---

# 4 · Contrato documental

Resuelve `CI-2`, que degradó `H5` de conclusión a candidato.

## 4.1 · Las tres vías, comparadas

| | vía | cubre las doce áreas | duplica campos | coste | riesgo |
|---|---|---|---|---|---|
| 1 | **generalizar `memoria`** | tras añadir campos | no | bajo | convierte un tipo con sujeto claro —la memoria de un equipo— en un cajón con dos sujetos |
| 2 | **metadata documental especializada** | sí | **sí**: `capacidad`, `autoridad`, `fichero`, `caducidad` y `se_actualiza_cuando` volverían a declararse | medio | dos tipos que dicen lo mismo sobre el mismo fichero |
| 3 | **composición** `memoria` + `cobertura` | sí | no | bajo | exige que las dos piezas existan, y `cobertura` se construye igualmente por §5 |

**Decisión: vía 3 sobre una `memoria` GENERALIZADA — y las dos mitades se dicen.**

> **Corrección de F4 entregada.** El documento anterior eligió la vía 3 y a la vez, en §3.7,
> amplió la descripción de `memoria` *«de sección del corpus de un equipo a documento
> gobernante en general»*. **Eso es la vía 1**, comparada y declarada descartada doce líneas
> antes. La composición era real, y la generalización también: se hacía **en silencio** y se
> describía como si no ocurriera. Aquí se declara. Es `D27`, que **sustituye** a `D20`.

```text
LO QUE SE COMPONE      dos preguntas con dueños distintos, y ninguna de las dos duplica a
                       la otra:
                         ¿QUIÉN RESPONDE DE ESTE DOCUMENTO Y CUÁNDO SE TOCA?
                              → `ads:memoria`, DENTRO del documento
                         ¿ESTO SIGUE SIENDO CIERTO, Y CUÁNDO SE COMPROBÓ?
                              → `cobertura`, con el documento como SUJETO y su área como
                                `aspecto:documental/<area>`

LO QUE SE GENERALIZA   el SUJETO de `memoria`: de «una sección del corpus persistente de un
                       equipo» a «cualquier documento gobernado». Un documento gobernante
                       ES un sujeto auditable, y la lista del Owner lo dice: «documentos»
                       está entre lo que hay que auditar.

POR QUÉ LA VÍA 1 SOLA  porque `memoria` sin `cobertura` no puede responder la segunda
NO BASTABA             pregunta sin absorber vigencia, evidencia, revisiones examinadas y
                       findings — y ahí sí se convertiría en el cajón que el riesgo de la
                       vía 1 describe. Generalizar el SUJETO no es lo mismo que absorber
                       el SEGUNDO SUJETO, y la diferencia es exactamente §4.2.
```

### El campo `capa`, resuelto sin fabricar una cuarta capa

`memoria.capa` es hoy un enum obligatorio de tres valores: `kernel`, `pack`, `profile`. Son
las tres capas de `K-1`, que clasifican **conocimiento**. Un documento cuyo sujeto es la
arquitectura **real de este producto** no es ninguno de los tres, y el tipo generalizado no
validaría. Añadir un cuarto valor fabricaría `X1` por la puerta de atrás, y `X1` sigue
deferida.

```text
`capa`   K-1, tres valores, pasa a CONDICIONAL. La declara únicamente un documento que sea
         CONOCIMIENTO QUE VIAJA CON UN RELEASE. Si el documento no lo es, el campo NO
         APLICA, y eso se registra como no aplicable, no como ausencia.

`plano`  NUEVO Y OBLIGATORIO. Uno de los cinco planos de §1.2: `distribucion` ·
         `especializacion` · `estado` · `proyeccion` · `operacional`. Todo documento tiene
         plano, porque todo documento tiene ciclo de vida.
```

**Y por qué esto no cruza la línea de `X1`.** §1.2 ya separó las dos clasificaciones: `K-1`
clasifica conocimiento y los cinco planos clasifican ciclo de vida. `plano` es la segunda, no
una cuarta capa de la primera. Un documento del producto tiene `plano: especializacion` y
**no tiene `capa`** — que es precisamente lo que hay que poder decir.

## 4.2 · Cómo se reparte cada exigencia

**Una sola fuente por exigencia.** F4 entregada colocaba `ultima_verificacion_real` en
`memoria.yaml` (§3.7) **y** en `cobertura` (§4.2), y proclamaba «cero campos duplicados» tres
líneas después de la tabla que los duplicaba. Se corrige: vive **sólo en `cobertura`**.

| exigencia del §5.19 / §5.23 | dónde vive | ya existe |
|---|---|---|
| fuente canónica | `memoria.fichero` | **sí** |
| autoridad | `memoria.autoridad` | **sí** |
| responsable / capacidad | `memoria.capacidad` | **sí** |
| qué materia cubre | `memoria.contiene` | **sí** |
| triggers de actualización | `memoria.se_actualiza_cuando` | **sí** |
| consumidor operativo | `memoria.se_consulta_en` | **sí** |
| plano de ciclo de vida | `memoria.plano` | **extensión** |
| capa de conocimiento, cuando aplica | `memoria.capa`, condicional | **sí**, con su obligatoriedad corregida |
| **caducidad NORMATIVA del documento** | `memoria.caducidad` | **sí** |
| ciclo normativo del documento | `memoria.estado` | **extensión** |
| qué significa que el documento esté VACÍO | `memoria.vacio_significa` | **sí** |
| que un ASPECTO no aplique a este documento | `cobertura.motivo_no_aplicable` + su evidencia | tipo nuevo |
| **vigencia de la última verificación** | `cobertura.caducidad` | tipo nuevo |
| **última verificación real** | `cobertura.verificacion.ultima_real` | tipo nuevo |
| procedencia: fuentes, entornos y **revisiones examinadas** | `cobertura.verificacion.revisiones_examinadas` | tipo nuevo |
| evidencia | `cobertura.evidencia` | tipo nuevo |
| gaps y contradicciones | `cobertura.findings` → items | tipo nuevo + existente |
| relaciones con decisiones, items y dosieres | referencias desde ambos | **sí** |
| aplicabilidad obligatoria/condicional/no aplicable | `cobertura.aplicabilidad` | tipo nuevo |

### Los dos relojes, que no son el mismo

**Un documento vigente con una verificación caducada es el caso NORMAL**, y F4 entregada no
podía representarlo porque llamaba «caducidad» a las dos cosas.

```text
`memoria.caducidad`     NORMATIVA. Cuándo el DOCUMENTO deja de ser exigible o debe
                        reescribirse. Es propiedad del documento, y la fija su autoridad.
                        Ejemplo: «caduca cuando cambie la dirección arquitectónica».

`cobertura.caducidad`   VIGENCIA DE UNA VERIFICACIÓN. Cuándo el juicio «esto sigue siendo
                        cierto» deja de valer. Es propiedad de la CELDA, y su valor por
                        defecto lo fija el `contrato-de-aspecto` de su familia (§5.7).
                        Ejemplo: «caduca a los seis meses, o antes si cambia una de las
                        revisiones examinadas».
```

| documento | verificación | qué significa |
|---|---|---|
| vigente | vigente | el caso bueno: se cree lo que dice |
| vigente | caducada | **el caso normal y el más frecuente**: el documento sigue siendo exigible, y nadie ha comprobado últimamente que sea cierto. La celda pasa a `vencido` y el sistema lo REPORTA |
| caducado | vigente | el documento debe reescribirse aunque su última comprobación fuese buena: lo que verificó ya no es lo que se exige |
| caducado | caducada | reescribir y volver a verificar. Es el peor caso, y es visible |

### El ciclo del documento gobernado — propio, y de cuatro valores

> **Corregido por la segunda devolución independiente (hallazgo `J`).** F4c escribía
> `vigente | sustituida | retirada` y lo atribuía a `b.3` **dos veces**, en §3.7 y aquí.
> **`b.3` dice `vigente | sustituida | INVALIDADA`.** Y no era un desliz de nombre:
> **`retirada` sí existe en `b.3`, aplicado a otro sujeto** — `obligación_retirada`, sobre
> OBLIGACIONES, no sobre capas. `b.3` advierte con estas palabras: *«Producir lo que una
> obligación exigía y decidir que ya no forma parte del alcance son resultados DISTINTOS. Si
> se llaman igual, el sistema puede informar de que entregó algo que en realidad se
> eliminó.»* F4c tomaba la palabra de un sujeto y la pegaba al ciclo de otro, que es la
> confusión concreta contra la que `b.3` avisa.

**Y un documento gobernado NO reutiliza la vigencia de `b.3`, por dos razones.** Los tres
valores de `b.3` describen *si un resultado puede sostener integración y cierre*; un documento
normativo no sostiene ni integra: **obliga**. Y un documento **retirado del corpus** y uno
**cuyo contenido se declara falso** son cosas distintas, y las dos ocurren.

```text
vigente      exigible, y su contenido se cree salvo que su celda diga otra cosa

sustituida   exigible en su ámbito residual, con ENLACE OBLIGATORIO al documento que lo
             reemplaza. Es el único valor que conserva la forma de `b.3`, y ahí la analogía
             puede citarse COMO ANALOGÍA

derogada     deja de ser exigible por decisión de su autoridad, SIN REEMPLAZO.
             Es el caso que F4c no podía escribir con ningún valor válido

refutada     su contenido resultó FALSO. Distinta de `derogada`, porque obliga a revisar
             todo lo que se apoyó en ella. Es la que corresponde a la intuición de
             `invalidada` en `b.3`, sin tomarle prestado el nombre
```

**El cruce con `cobertura.estado`, extendido a los cuatro:**

| documento | celda `verificado` | qué significa |
|---|---|---|
| `vigente` | coherente | el caso bueno |
| `sustituida` | coherente | era cierto, y ya no se usa. Su ámbito residual sigue enlazado |
| `derogada` | coherente | era cierto cuando se comprobó, y ya no obliga |
| `refutada` | **INCOHERENTE** | un documento cuyo contenido resultó falso no puede tener una celda que afirme que se verificó y salió bien. La validación cruzada **lo rechaza** |

### Las tres duplicaciones que se eliminan

```text
`ultima_verificacion_real`   ESTABA EN LOS DOS. Se retira de `memoria`. Sólo `cobertura`.

`vacio_significa` FRENTE A   dejan de solaparse porque responden preguntas distintas:
`motivo_no_aplicable`          `vacio_significa`      el documento EXISTE y está vacío.
                                                      ¿Eso qué quiere decir?
                               `motivo_no_aplicable`  este ASPECTO no aplica a este SUJETO.
                                                      ¿Por qué, y con qué evidencia?

`memoria.estado` FRENTE A    `memoria.estado` es el CICLO NORMATIVO PROPIO del documento.
`cobertura.estado`           NO es estado de verificación. `cobertura.estado` es el estado
                             del JUICIO sobre él. Un documento `sustituida` con celda
                             `verificado` es coherente y se lee sin ambigüedad: era cierto,
                             y ya no se usa.
```

**Cero campos duplicados**, ahora sí: es la condición que `CI-2` conserva de `H5`, y la que
descarta la vía 2.

## 4.3 · Las doce áreas de `O8`, sin doce ficheros

Las doce áreas son **aspectos de la familia documental**, y un aspecto no es un fichero.
Cada una es un `aspecto:documental/<area>` con su namespace propio, distinto del de los
aspectos de calidad y del de los niveles de certificación — que es la corrección de §3.5.

```text
identidad y dirección de producto · baseline funcional · dominio y glosario ·
arquitectura actual · dirección arquitectónica · tecnologías y entorno de desarrollo ·
dirección de ingeniería · calidad y pruebas · seguridad y riesgos ·
despliegue, entornos y operación · decisiones · dirección de evolución y gaps

COMPACTACIÓN     un documento declara VARIAS áreas en su bloque `memoria.contiene`. En un
                 producto pequeño, tres documentos pueden cubrir las doce.
PROFUNDIDAD      la exige `cobertura.aplicabilidad` por área, derivada de tamaño,
                 naturaleza y riesgo declarados en `PROFILE`.
RESPONSABLE      cada área declara su reparto POR DEFECTO en su
                 `contrato-de-aspecto:documental/<area>` (§5.7), y NO se infiere de la
                 capacidad: `SIS` responde de conformidad documental, y del CONTENIDO de un
                 área responde la capacidad de esa materia. La celda declara sólo la
                 desviación, con motivo.
CONDICIONALES    UX e investigación, dirección visual, sistema de diseño, datos,
                 integraciones, cumplimiento, observabilidad, continuidad,
                 internacionalización. Se activan por aplicabilidad.
NO APLICABLE     con motivo registrado. Una ausencia silenciosa es un fallo del gate.
```

**Y la comprobación, que `CI-4` corrigió:** la reanudación por un agente sin contexto y los
gates **comprueban** el mínimo; no lo definen. Un producto puede reanudarse y seguir sin tener
resuelto su dominio o su seguridad, y por eso las doce áreas son obligatorias como **materia**
aunque la reanudación funcione.

---

# 5 · Sistema de auditoría y mejora continua

Autorizado por `O7`, con el sujeto que `CI-1` corrigió.

## 5.1 · El sujeto auditable

`CI-1` cerró que el componente de `C6` es **ancla**, no sujeto único. La referencia tipada:

```text
sujeto = (clase, ancla, ruta)

ANCLA          un componente declarado en SOURCES.toml, o `transversal`
CLASE          qué es, y de ella sale qué ASPECTOS le aplican y con qué obligatoriedad
RUTA           dentro del ancla; para un transversal, su identificador global

componente:web              ancla, la raíz
pantalla:web/checkout       subordinado
formulario:web/checkout/pago
api:backend/pedidos
entidad:backend/Pedido
migracion:backend/2026_08_add_tenant
pipeline:transversal/release
patron:transversal/tabla-operativa      atraviesa componentes
documento:transversal/arquitectura
adaptador:transversal/claude-code
```

**`SOURCES.toml` no se toca.** Sigue declarando fuentes y componentes, y nada más. El sujeto
lo declara la celda, y el inventario se **deriva** de las celdas más lo que ya declara
superficie: componentes del manifiesto, documentos con bloque `memoria`, adaptadores, skills
vendorizadas y contratos declarados por los paquetes.

**Límite declarado.** Una pantalla o un flujo que nadie ha declarado nunca **no aparece en el
inventario**. El sistema puede decir qué no ha auditado de lo que conoce; **no puede afirmar
que conoce todo el producto**. Cerrar ese hueco exige descubrimiento sobre el código, y eso
es la adopción (§8.2) y el piloto, no una propiedad del registro.

## 5.2 · Aspectos y capacidades — que no son lo mismo

`H4` sobrevive a la corrección de `CI-1` en su mitad útil: **la capacidad es quien responde
del juicio**. Lo que no sobrevive es la otra mitad, que F4 entregada escribió como
*«la dimensión es la capacidad que la posee»*.

> **Por qué no se sostiene.** `DIS` responde de UI, UX, diseño visual, sistema de diseño,
> responsive y accesibilidad. Con la capacidad como dimensión, **auditar la accesibilidad de
> una pantalla y auditar su responsive son la misma celda**: no se pueden registrar por
> separado, ni vencer por separado, ni tener verificadores distintos, ni abrir findings
> distintos. Una capacidad **no sustituye a las dimensiones de las que responde**.

```text
ASPECTO        QUÉ propiedad del sujeto se juzga.   `aspecto:calidad/accesibilidad`
CAPACIDAD      QUIÉN responde de ese juicio.        `DIS`
CRITERIO       CONTRA QUÉ se juzga.                 una rúbrica, un gate, un nivel
```

**Una capacidad responde de varios aspectos. Un aspecto puede tener varios responsables**,
y en ese caso uno se declara `lider` — porque «dos responsables» sin líder es «ninguno».

### El reparto, aspecto a aspecto

| aspecto | responsables | líder | qué aporta |
|---|---|---|---|
| `calidad/producto` | `PRD` | `PRD` | criterio de éxito y alcance |
| `calidad/ui` · `calidad/ux` · `calidad/diseno-visual` · `calidad/sistema-de-diseno` · `calidad/responsive` · `calidad/accesibilidad` | `DIS` | `DIS` | rúbricas y `05-FIDELIDAD`. **Seis aspectos, una capacidad** |
| `calidad/arquitectura` · `calidad/integraciones` · `calidad/acoplamiento` · `calidad/deuda` | `ARQ` | `ARQ` | radio de impacto |
| `calidad/dominio` · `calidad/reglas` · `calidad/datos` | `DOM` | `DOM` | invariantes y migraciones |
| `calidad/seguridad` · `calidad/privacidad` · `calidad/cumplimiento` | `SEG` | `SEG` | veto con evidencia |
| `calidad/pruebas` · `calidad/regresion` · `calidad/evidencia` | `VER` | `VER` | dictamen independiente |
| `calidad/ci-cd` · `calidad/despliegue` · `calidad/observabilidad` | `ENT` | `ENT` | entrega observada |
| `calidad/tecnologias` · `calidad/entorno` | `PLT` | `PLT` | maquinaria disponible |
| `calidad/conformidad-ads` | `SIS` | `SIS` | contrato y coherencia |
| `calidad/uso-real` | `USO` | `USO` | comportamiento observado |
| **`calidad/rendimiento`** | **`ARQ` · `ENT`** | **`ENT`** | `ARQ` responde del coste de DISEÑO —algoritmos, contratos, radio—; `ENT` responde del rendimiento OBSERVADO en un entorno real, que es el que decide |
| **`calidad/resiliencia`** | **`ENT` · `ARQ`** | **`ENT`** | `ENT` ya declara **recuperación** entre su materia; `ARQ` responde de la resiliencia estructural — degradación, contratos, aislamiento de fallos |
| **`calidad/dependencias`** | **`PLT` · `SEG`** | **`PLT`** | `PLT` es el propietario global del proceso `DEP` de `b.16`; `SEG` participa con **veto**, porque `b.16` ya declara `SEG:condiciones ⊳ CON` OBLIGATORIO en `DEP` por `G28` |
| `documental/<area>` | ver §4.3 | según el área | las doce áreas de `O8` |
| `certificacion/<nivel>` | ver §9.2 | `SIS` o `PLT` según el nivel | los cuatro niveles |

### Las dos dimensiones huérfanas, asignadas

F4 entregada declaró **rendimiento y resiliencia** y **dependencias y cadena de suministro**
*«sin propietario evidente»* y las aparcó. Una arquitectura que se llama **integrada** no
puede terminar con dos materias sin responsable: la honestidad es decir **quién responde**, o
**qué norma hay que enmendar para que alguien pueda responder**. Aquí se resuelve lo primero.

```text
POR QUÉ SE PUEDEN         las cuatro capacidades implicadas EXISTEN y la materia YA está en
ASIGNAR SIN ENMENDAR      su alcance declarado:
NADA                        `ENT`   `b.16` le da la entrega y la operación, e incluye
                                    RECUPERACIÓN entre su materia
                            `ARQ`   contratos, estructura y radio de impacto
                            `PLT`   propietario global de `DEP` en `b.16`
                            `SEG`   `C-SEG` nombra expresamente «dependencias externas»,
                                    y `G28` hace su consulta OBLIGATORIA antes de construir

QUÉ TRABAJO GENERA        una EXTENSIÓN DE FICHA en F6, nombrada fichero a fichero:
                            `capacidades/ENT/`   añadir rendimiento observado y resiliencia
                                                 a su materia declarada
                            `capacidades/ARQ/`   añadir coste de diseño y resiliencia
                                                 estructural
                            `capacidades/PLT/`   añadir cadena de suministro como aspecto,
                                                 no sólo como proceso
                            `capacidades/SEG/`   declarar su veto sobre `calidad/dependencias`
                                                 con los seis campos del contrato de veto de
                                                 `a.5`

QUÉ NO GENERA             presión normativa. Ninguna de las cuatro fichas es (a), (b), `E1`,
                          `E2`, `K-1` ni `C4`. Extender una ficha de capacidad con materia
                          que ya está en su alcance es trabajo de F6.

EL LÍMITE, DECLARADO      si al redactar la extensión F5 o F6 encontrasen que el alcance de
                          una de las cuatro NO estira hasta el aspecto, entonces SÍ nacería
                          una presión, y se registraría ese día. Hoy no la hay, y afirmar
                          que la habrá sería tan poco riguroso como aparcar las dos materias.
```

## 5.3 · El ciclo, y quién hace cada paso

```text
INVENTARIO          derivado. No crea trabajo. AUTOMÁTICO
      ↓
COBERTURA           celdas con su estado y su caducidad. AUTOMÁTICO
      ↓
DETECCIÓN           qué nunca se auditó · qué venció · qué invalidó un cambio.
                    Es una VISTA DERIVADA: no crea trabajo. AUTOMÁTICO
      ↓
APERTURA            crea un item AUD. SÓLO dentro de la política O7. Si no hay política
                    vigente, el sistema PROPONE y espera
      ↓
AUDITORÍA           proceso `AUD`, con la capacidad RESPONSABLE DEL ASPECTO produciendo
                    la capa. Si hay varias, la declarada `lider` (§5.2)
      ↓
FINDINGS            en la evidencia del AUD. Todavía no son trabajo
      ↓
CLASIFICACIÓN       `ENC`, con las nueve clases de entrada y los diez procesos de b.16
      ↓
CAUSAS RAÍZ         agrupación por campo común. Veinte inputs con alturas distintas NO son
                    veinte items si la causa es un componente
      ↓
CAMPAÑA             una `iniciativa` con su gate
      ↓
CORRECCIÓN          `CON`, con el nivel de autorización de §5.5
      ↓
VERIFICACIÓN        `VER` independiente. `corregido` != `verificado`
      ↓
PREVENCIÓN          `APR/Promocion` + `gate:aprendizaje-fundado`, que ya exige dos
                    ocurrencias o un incidente
      ↓
REAUDITORÍA         la celda vuelve a `vencido` por su trigger
```

## 5.4 · La política de `O7`, y qué la limita

```text
AUTOMÁTICO SIN CREAR TRABAJO    inventariar · calcular cobertura · detectar · proponer
DENTRO DE LA POLÍTICA           abrir items AUD por evento, riesgo, recurrencia y caducidad
FUERA DE LA POLÍTICA            todo lo demás: se propone y espera

LA POLÍTICA ES UNA DECISIÓN REGISTRADA, y declara:
    alcance          qué clases de sujeto y qué aspectos, por familia
    prioridad        con qué prioridad nacen los items que abre
    presupuesto      cuántos items abiertos simultáneos admite
    umbrales         qué caducidad y qué señales disparan
    revocación       cómo se apaga, y qué pasa con lo ya abierto

REVOCABLE. Al revocarse, el sistema vuelve a proponer y esperar. Lo ya abierto no se
cancela solo: pasa a decisión del Owner, porque cancelar es autoridad semántica.
```

## 5.5 · Autonomía de corrección por riesgo

| nivel | autorización | quién verifica |
|---|---|---|
| mecánico y local, sin cambio funcional | dentro de campaña preautorizada | `VER` independiente |
| corrección local con cambio de comportamiento acotado | campaña + gate de su capa | `VER` independiente |
| refactorización transversal | plan y radio de impacto de `ARQ` | `VER` + `ARQ` |
| cambio de UX, producto o arquitectura | dirección aprobada. `a.8` nivel obligatorio | la capacidad con autoridad |
| seguridad, datos o comportamiento crítico | gate especializado, y `SEG` con veto | `SEG` · `VER` · Owner |

**Ninguna fila levanta un gate existente.** La política decide **si se abre el trabajo**, no
con qué rigor se cierra.

## 5.6 · Tres celdas completas, sobre el mismo contrato

La prueba de que la separación de §3.5 funciona no es el argumento: es que **tres sujetos
que no se parecen en nada caben en el mismo contrato sin campos vacíos de conveniencia y sin
campos que signifiquen cosas distintas en cada uno**.

### Ejemplo 1 · una pantalla auditada en accesibilidad

```text
sujeto        clase: pantalla · ancla: web · ruta: checkout
              → pantalla:web/checkout
aspecto       aspecto:calidad/accesibilidad
responsables  [DIS]                                        lider: DIS
criterio      rubrica:accesibilidad-web                    la rúbrica, no una nota
aplicabilidad obligatoria
estado        findings-abiertos
verificacion
  ultima_real            2026-07-14
  revisiones_examinadas  frontend@9c1e4a7
  auditor                VER, que no construyó la pantalla
  verificador_de_correccion  vacío: el estado es `findings-abiertos`, y todavía no hay
                             corrección que verificar
evidencia     [DIC-0041]                                   el dictamen
findings      [DEF-118, DEF-119]                           items, no anotaciones (§3.2)
caducidad     6 meses, o antes si cambia `frontend` bajo `src/checkout/`
triggers      cambio en la revisión examinada · cambio de la rúbrica · incidente de uso
responsable_de_corregir  CON
```

**Y su celda hermana, que antes no podía existir:**

```text
sujeto        pantalla:web/checkout                        EL MISMO SUJETO
aspecto       aspecto:calidad/responsive                   OTRO ASPECTO
responsables  [DIS]                                        LA MISMA CAPACIDAD
estado        verificado
caducidad     12 meses
```

> Con `dimension: ref a capacidad`, estas dos celdas eran **una sola** y no podían tener
> estados ni caducidades distintas. Ésa era la colisión, y éste es su remedio.

### Ejemplo 2 · un documento evaluado en una familia documental

```text
sujeto        clase: documento · ancla: transversal · ruta: arquitectura-actual
              → documento:transversal/arquitectura-actual
aspecto       aspecto:documental/arquitectura-actual       una de las doce áreas de O8
responsables  [ARQ, SIS]                                   lider: ARQ
              ARQ responde del CONTENIDO; SIS de la conformidad del contrato documental
criterio      contrato-de-aspecto:documental/arquitectura-actual        §5.7
aplicabilidad obligatoria
estado        vencido
verificacion
  ultima_real            2026-02-03
  revisiones_examinadas  backend@4d0c118 · frontend@9c1e4a7
  auditor                VER
  verificador_de_correccion  vacío: el estado es `vencido`
evidencia     [DIC-0027]
findings      []
caducidad     vence cuando cambia cualquiera de las revisiones examinadas.  YA VENCIÓ
triggers      cambio en una revisión examinada · cambio de dirección arquitectónica
responsable_de_corregir  ARQ
```

**Lo que el bloque `ads:memoria` del propio documento dice, y que la celda NO repite:**

```text
memoria.fichero              docs/arquitectura/ACTUAL.md
memoria.autoridad            ARQ
memoria.capacidad            ARQ
memoria.plano                especializacion                 nuevo, §4.1
memoria.capa                 NO APLICA: no es conocimiento que viaje con un release
memoria.contiene             [arquitectura-actual, dominio-y-glosario]   DOS áreas, §4.3
memoria.se_actualiza_cuando  [cambia un contrato entre componentes, entra una fuente nueva]
memoria.caducidad            NORMATIVA: caduca si cambia la dirección arquitectónica
memoria.estado               vigente
memoria.vacio_significa      «no se ha reconstruido la arquitectura todavía»
```

**Documento `vigente`, verificación `vencido`.** Es el caso normal de §4.2, y ahora se puede
escribir: el documento sigue siendo exigible, y nadie ha comprobado últimamente que sea
cierto.

### Ejemplo 3 · una instalación evaluada para un nivel de certificación

```text
sujeto        clase: instalacion · ancla: transversal · ruta: pesquerapp
              → instalacion:transversal/pesquerapp
aspecto       aspecto:certificacion/integrado
responsables  [PLT, VER]                                   lider: PLT
criterio      nivel-certificacion:integrado                LA NORMA, en el kernel (§9.2)
aplicabilidad obligatoria
estado        verificado
verificacion
  ultima_real            2026-08-11
  revisiones_examinadas  frontend@9c1e4a7 · backend@4d0c118
  auditor                VER independiente, que NO participó en la instalación
  verificador_de_correccion  VER independiente. El estado es `verificado`, luego este campo
                             es OBLIGATORIO (§3.5)
evidencia     [DIC-0033]                                   dosier + salidas de las pruebas
findings      []
caducidad     no vence por tiempo: vence por TRIGGER
triggers      cambia SOURCES.toml · cambia CI o permisos · cambia un entorno ·
              SE AÑADE UNA FUENTE
responsable_de_corregir  PLT
```

**Y la celda del nivel que no aplica, que ahora se puede escribir sin bloquear nada:**

```text
sujeto        instalacion:transversal/producto-de-un-repo
aspecto       aspecto:certificacion/integrado
aplicabilidad obligatoria
estado        verificado
evaluacion_de_pruebas
              - prueba                        multi-fuente-verificado-como-conjunto
                aplicabilidad                 no-aplicable
                motivo_no_aplicable           el producto declara UNA sola fuente; con una
                                              fuente no hay conjunto que converger (E2.6)
                evidencia_de_inaplicabilidad  SOURCES.toml@a71f3c2 declara 1 fuente
                resultado                     no-aplica
              - prueba                        workspace-check-sobre-fuentes-reales
                aplicabilidad                 obligatoria
                resultado                     pasa
```

**Los tres caben en el mismo contrato.** Ninguno necesita un campo que los otros dos dejen
vacío por conveniencia, y ningún campo significa una cosa en uno y otra en otro. Eso es lo
que el campo único `dimension` no podía sostener.

> **Y la tercera celda NO cabía hasta ahora (hallazgo `N-2`).** F4c colocaba la evaluación de
> inaplicabilidad «DENTRO del criterio», que es una norma de CLASE compartida por todas las
> instalaciones — y `SOURCES.toml@a71f3c2` es un dato de ESTE producto y ESTA revisión. El
> ejemplo 3b era un **contraejemplo de la tesis que este apartado dice demostrar**. Con
> `evaluacion_de_pruebas` (§3.5) la tesis vuelve a ser cierta, y `X42` la comprueba validando
> las tres celdas contra el esquema sin campos libres.

> **Ninguna de las tres celdas existe.** Son ejemplos del contrato, no registros de un
> producto real. `cobertura` no está construida.

## 5.7 · `contrato-de-aspecto` — la norma que F4c invocaba y no definía

> **Añadido por la segunda devolución independiente (hallazgo `N-1`, GRAVE).** F4c invocaba
> «el contrato del aspecto» **tres veces** como sede normativa —fijaba la caducidad de las
> celdas (§4.2), declaraba los responsables de cada área documental (§4.3), y se referenciaba
> desde `criterio` como `contrato:documental/O8` (§5.6)— **y no existía**: sin esquema, sin
> fichero, sin autoridad, sin ciclo, sin la prueba del §3.1, y **fuera del recuento de §3.8**
> — en un apartado que abre presumiendo de que *«el recuento se CALCULA, no se fija de
> antemano»*.
>
> **Es el mismo modo de fallo que la primera crítica encontró con el manifiesto de
> transacción**, reproducido en otra sección y no detectado al corregir. Se le aplica ahora
> la prueba, por escrito, exactamente como se hizo con aquél.

### La prueba de §3.1, aplicada

```text
1 ¿lo expresa un tipo existente sin deformarlo?
     `cobertura` es la CELDA: un sujeto evaluado. El contrato es la NORMA de una familia de
     aspectos, compartida por todas las instalaciones. Meterlo en la celda obligaría a
     repetirlo en cada producto y permitiría que dos discreparan sobre qué exige un área.
     → NO

2 ¿lo expresa la COMBINACIÓN de dos existentes?
     `rubrica` + `gate` cubren el CRITERIO y las COMPROBACIONES, y no cubren el reparto de
     responsables por defecto, la caducidad por defecto ni los triggers de familia. → NO

3 ¿le falta un campo a un tipo existente?
     añadir `responsables_por_defecto`, `caducidad_por_defecto` y `triggers` a `gate` se los
     daría a TODOS los gates del sistema para que sólo los usara la cobertura. Es el paso 1
     leído al revés. → NO

4 ¿tiene sujeto propio, autoridad propia y ciclo propio?
     SUJETO      una FAMILIA DE ASPECTOS, no un sujeto auditado
     AUTORIDAD   `SIS` para la conformidad del contrato; la capacidad de la materia para su
                 contenido
     CICLO       viaja con el release, como `nivel-certificacion`
     → SÍ

VEREDICTO   ESQUEMA DE CLASE. Es la misma clase de artefacto que `nivel-certificacion` y que
            el `nivel-novedad.yaml` que ya existe en el corpus. NO es un tipo de estado, y
            por eso no entra en la cuenta de tipos canónicos — pero SÍ en la de esquemas.
            El recuento de §3.8 pasa de 24 a **25**.
```

### Qué declara

```text
id                       contrato-de-aspecto:<familia>/<nombre>
familia                  calidad | documental. **NO `certificacion`**: ver abajo
responsables_por_defecto 1..N capacidades, con una `lider`. Es la NORMA; la celda declara
                         sólo la DESVIACIÓN, con motivo (§3.5)
criterio_por_defecto     la rúbrica, el gate o la norma contra la que se juzga
pruebas                  la lista que la celda evalúa una a una en `evaluacion_de_pruebas`
caducidad_por_defecto    la que la celda hereda si no declara otra
triggers                 qué vence y qué reabre, a nivel de familia
aplicabilidad_por_defecto  y las condiciones que la modifican
evidencia_minima         sin qué no se puede declarar `verificado`
```

### La duplicación de `responsables`, resuelta con la disciplina de los dos relojes

```text
EL CONTRATO DECLARA   el reparto POR DEFECTO. Es norma, y viaja con el release.
LA CELDA DECLARA      la DESVIACIÓN, si la hay, con su motivo. Es estado, y es del producto.
UNA FUENTE POR        no dos sedes editables para lo mismo. Es exactamente el remedio que
PREGUNTA              §4.2 aplicó a `memoria.caducidad` frente a `cobertura.caducidad`.
```

### El reparto con `nivel-certificacion`, para que no haya dos normas editables

> **Corregido por la devolución técnica previa (hallazgo `10`).** `contrato-de-aspecto`
> declaraba `familia: calidad | documental | certificacion`, y `nivel-certificacion` ya
> declaraba para certificación pruebas, propietario, crítico, jerarquía, invalidación y
> criterio. **Dos normas editables para el mismo aspecto**, que es exactamente el defecto que
> `D43` existía para cerrar en otro sitio.

```text
`contrato-de-aspecto`   cubre EXCLUSIVAMENTE las familias `calidad` y `documental`
`nivel-certificacion`   cubre EXCLUSIVAMENTE la familia `certificacion`, y es la ÚNICA sede
                        de sus pruebas, responsables, crítico, jerarquía, invalidación y
                        criterio
NINGÚN CAMPO DE         está declarado en los dos. No hay especialización ni composición
CERTIFICACIÓN           entre ambos esquemas: hay REPARTO DE DOMINIO, que es más simple y no
                        deja campos que puedan discrepar
```

**Y las tres familias resuelven ahora a algo que existe**, que era la otra mitad del hallazgo:
`aspecto:calidad/accesibilidad` → `contrato-de-aspecto:calidad/accesibilidad`;
`aspecto:documental/arquitectura-actual` → `contrato-de-aspecto:documental/arquitectura-actual`;
`aspecto:certificacion/integrado` → `nivel-certificacion:integrado`, que es su norma propia
por §9.2. **Ninguna referencia de `criterio` queda sin resolver.**

---

# 6 · Arquitectura de adaptadores

Las cuatro piezas que `CI-6` separó, diseñadas por separado.

## 6.1 · Pieza 1 · Definición canónica neutral

```text
DÓNDE      ads/adaptadores/<entorno>/
QUÉ ES     la FUENTE. Es lo único de las cuatro que se edita a mano.
CONTIENE   el bloque `ads:adaptador` de §3.4, y nada de contenido de kernel: lo enlaza
QUIÉN      PLT la mantiene; SIS comprueba su conformidad
```

**Qué no contiene.** Conocimiento. Un adaptador **traduce**; si empieza a contener reglas de
trabajo, se convierte en una segunda copia del kernel y reproduce `CAND-016` — la memoria
espejada que divergió 23 contra 32 entradas.

## 6.2 · Pieza 2 · Proyecciones generadas

```text
DÓNDE      donde CADA PROVEEDOR las descubre. No lo elige ADS: lo impone el entorno.
           AGENTS.md · CLAUDE.md · .cursor/rules/ · .github/instructions/ · lo que venga
CÓMO       se COMPILAN desde: definición canónica + kernel instalado + packs + PROFILE +
           SOURCES.toml + overrides
QUÉ LLEVA  versión de ADS · versión del adaptador · revisión de la especialización ·
           origen canónico · aviso de fichero generado · HUELLA
REGLA      I5: derivadas, NO editables. Editar una proyección no es configurar: es
           fabricar deriva
```

**El precedente existe y funciona.** `CAND-008` —registro derivado, regenerable, no editable—
es el patrón, y `registro_pruebas.py` y `comprobar_recuentos.py --generar` lo implementan para
el propio corpus. [`compile-agents.sh`](../../tooling/compile-agents.sh) es su primer intento
fuera del corpus: hoy inventaría las fuentes y emite un encargo, y **no genera**. Es el punto
de partida, no el resultado.

## 6.3 · Pieza 3 · Huella y validador de deriva

```text
QUÉ DETECTA    una proyección editada a mano · una proyección obsoleta respecto a su
               fuente · dos proyecciones que dicen cosas distintas sobre lo mismo
CÓMO           huella de las entradas de la compilación, escrita en la proyección.
               Recompilar y comparar es determinista
CIERRA         P-06, que F2 registró con DOS ocurrencias medidas: la memoria espejada
               divergió 23 contra 32, y cuatro skills duplicadas divergieron las cuatro
               — la segunda DESPUÉS de detectar y documentar la primera
```

**Personalización local frente a generación.** Una particularidad persistente se edita en la
**definición canónica o en overrides** y se recompila. Nunca en la proyección. Una proyección
con huella rota es un fallo de conformidad, y el remedio es **recompilar**, no sincronizar —
que es el corolario que `CAND-016` dejó escrito: *un adaptador apunta, nunca copia*.

## 6.4 · Pieza 4 · Prueba de humo en sesión nueva

```text
QUÉ COMPRUEBA   lo que no puede comprobarse leyendo ficheros: que el agente ARRANCA
CÓMO            sesión nueva · las skills declaradas están visibles · prompts secos que
                NO deben modificar nada · comprobación de que el árbol quedó limpio ·
                **SESIÓN NUEVA ABIERTA SOBRE UNA FUENTE: el entorno lee el puntero,
                localiza el control repo hermano y opera con él como contexto principal**,
                con sus cuatro desenlaces como resultados EXIGIDOS y distintos —lo
                encuentra · no lo encuentra · no se pudo comprobar · encuentra dos—
                **Añadida** (hallazgo `I.2`): §6.7 remitía a esta prueba como la que mide si
                un entorno honra el puntero, y esta prueba no contenía NINGUNA comprobación
                que abriera el entorno sobre una fuente. Era una remisión que no llegaba a
                ninguna parte, y F4 declaraba medido por ella algo que no medía
ES              el nivel OPERATIVO de la certificación (§9), y `CAND-012` con un caso
                negativo real detrás: una skill añadida no aparecía hasta reiniciar la
                sesión, y nadie lo sabía
```

## 6.5 · Nivel alcanzado — derivado, nunca escrito

F4 entregada tenía **dos verdades sobre lo mismo**: `adaptador.nivel` era un campo editable
del bloque `ads:adaptador` (§3.4) y a la vez `soportado` era una conclusión que exigía prueba
de humo ejecutada y certificación Integrada. Editable y derivado a la vez es la segunda
verdad que `I5` prohíbe — y además un campo editable **no caduca** mientras una certificación
sí. Se separan tres cosas que no son la misma.

```text
COMPATIBILIDAD DECLARADA    lo que el adaptador AFIRMA soportar. CAMPO EDITABLE del
                            adaptador. Es una declaración de INTENCIÓN, y no autoriza a
                            afirmar nada sobre el entorno real.

CAPACIDADES DEL ENTORNO     lo que el entorno OFRECE técnicamente: subagentes, skills,
                            límites de contexto, permisos. CAMPO EDITABLE. Es una
                            OBSERVACIÓN, y puede quedarse obsoleta: se reobserva.

NIVEL ALCANZADO Y VIGENTE   NO ES UN CAMPO. Se DERIVA de las celdas de cobertura cuyo
                            sujeto es `adaptador:transversal/<entorno>` y cuyo aspecto es
                            `aspecto:certificacion/<nivel>`. Sale de EVIDENCIA, y CADUCA
                            por los triggers de §9.3 como cualquier otra celda.
```

| nivel alcanzado | qué autoriza a afirmar | qué celdas lo sostienen |
|---|---|---|
| **soportado** | el entorno ejecuta ADS con sus garantías | `certificacion/operativo` **verificado** y **vigente**, con la prueba de humo EJECUTADA como evidencia, más `certificacion/integrado` verificado y vigente |
| **compatible** | hay proyección y funciona lo esencial | `certificacion/estructural` verificado: existe adaptador, existe proyección y su huella casa. Sin prueba de humo ejecutada |
| **genérico** | recibe el contrato y las instrucciones universales | ninguna celda específica. Es el fallback obligatorio, y es `CAND-011`, ya construido en un proyecto real |
| **desconocido** | nada | ninguna celda, o todas `no-auditado` |

```text
LA REGLA, EN UNA FRASE    un adaptador NO PUEDE DECLARARSE `soportado`. Puede DECLARAR que
                          aspira a serlo —`compatibilidad_declarada`— y el sistema LEE su
                          nivel alcanzado de las celdas. Las dos frases se distinguen en el
                          texto, y por eso ya no se confunden en el registro.

QUÉ PASA AL INVALIDARSE   §9.3 dice que cambiar un adaptador, el arranque o la disposición
                          del estado invalida el nivel Operativo. Con el campo editable, un
                          adaptador seguía diciendo `soportado` después de eso. Con el nivel
                          derivado, la celda pasa a `vencido` y el nivel alcanzado BAJA solo,
                          sin que nadie tenga que acordarse de editar nada.
```

**Estado hoy, sin adornos:**

```text
Claude Code · Codex     primer OBJETIVO de soporte y certificación.  NO CERTIFICADOS
Cursor · Gemini         compatible o genérico hasta pasar su prueba de humo
cualquier otro          genérico, por el fallback obligatorio
NINGÚN ADAPTADOR EXISTE HOY, luego NINGUNA CELDA EXISTE y el nivel alcanzado de todos es
`desconocido`. O13 fija el objetivo; fijar el objetivo no es alcanzarlo.
```

## 6.6 · Cambio de proveedor

```text
1  se añade o activa el adaptador del entorno nuevo
2  se compila su proyección
3  prueba de humo en sesión nueva
4  el estado, la memoria, los items y los checkpoints NO SE TOCAN: son neutrales por
   diseño, y ésa es la propiedad que K0.8 y T92 protegen
5  el adaptador viejo puede convivir o retirarse. Retirarlo borra su proyección, nunca
   el estado
```

**Fronteras de escritura entre entornos.** Cuando dos entornos trabajan sobre el mismo
producto, cada adaptador declara `escribe_permitido` con sus **excepciones nombradas una a
una y con su motivo** — que es `CAND-014`, extensión de `I2` de zonas dentro de un artefacto a
zonas del repositorio entre dos ejecutores.

## 6.7 · Cómo descubre cada entorno su proyección, con el control repo y las fuentes hermanos

`C6` fija la topología: el control repo y las fuentes son **hermanos** dentro del workspace,
y **prohíbe** clonar las fuentes dentro del control repo. F4 entregada decía que las
proyecciones van *«donde CADA PROVEEDOR las descubre»* y no dijo qué ocurre cuando el agente
se abre sobre `frontend/` en vez de sobre `ads/`: allí no hay nada de ADS que descubrir.

**Las dos salidas fáciles están prohibidas, y por eso no se toman:**

```text
COPIAR LA ORGANIZACIÓN ADS   lo prohíbe `C6`: PROFILE, PROJECT, estado, items, rutas,
A CADA FUENTE                paquetes, memoria y contratos NO pueden vivir en una fuente.
                             Copiarlos crearía una organización ADS por repositorio que
                             después habría que sincronizar — el modo de fallo (a) de `a.7`
                             a escala de producto, y el `CAND-016` medido: 23 contra 32.

UN FICHERO NO VERSIONADO     no sobrevive a un clon nuevo, y `C6` `N9` dice que la identidad
                             de una fuente no depende de su ruta local. Un descubrimiento
                             que depende de `.ads/run/` o de una variable de entorno se
                             rompe en la nube, en otra máquina y en el segundo clon.
```

### La solución, en cuatro reglas

```text
1  LA ENTRADA CANÓNICA ES EL CONTROL REPO
   `C6` «Entrada por ADS» ya lo fija: se abre `ads/`, y desde ahí ADS determina componentes,
   fuentes y contexto mínimo. Un entorno abierto DIRECTAMENTE sobre una fuente es TRABAJO
   FUERA DE ADS, y `C6` es explícito: no se impide, y **ADS no finge** que pasó por sus
   gates. Ésta es la vía normal, y cubre la mayoría de los casos.

2  PARA LA PARTE INEVITABLE, UN ÚNICO FICHERO PUNTERO
   Algunos entornos sólo pueden abrirse sobre el repositorio que contiene el código. Para
   ésos, y sólo para ésos, el adaptador proyecta DENTRO de la fuente **un fichero y nada
   más**, declarado en su campo `puntero_en_fuente`:
       VERSIONADO      va al repositorio de la fuente, luego sobrevive a un clon nuevo
       GENERADO        se compila como cualquier otra proyección, y no se edita a mano
       CON HUELLA      §6.3 lo cubre igual que a las demás: editado a mano es deriva
       CON AVISO       dice que es generado y por quién

3  QUÉ CONTIENE, Y QUÉ TIENE PROHIBIDO CONTENER
   CONTIENE     la IDENTIDAD REMOTA CANÓNICA del control repo · la LISTA COMPLETA de los
                componentes que esta fuente materializa · la versión del adaptador · el
                aviso de generado
                **Corregido** (hallazgo `I.1`): F4c decía «el id del componente», en
                singular, y `C6` `N7` declara que «componente y fuente NO tienen cardinalidad
                1:1 obligatoria», con el caso MONOREPO explícito —`web → repo app, ruta
                apps/web` y `api → repo app, ruta apps/api`—. El campo singular reintroducía
                por la puerta de atrás la equivalencia que `C6` retira en su primer párrafo
                sobre los tres conceptos, y que `E2.0` declara formulación RETIRADA.
                La lista se DERIVA de `SOURCES.toml`, no se escribe: un componente nuevo
                obliga a recompilar el puntero
   NO CONTIENE  reglas de trabajo · memoria · estado · items · decisiones · contratos ·
                catálogo · prompts. NADA de conocimiento. Si lo llevara, sería la
                organización ADS copiada, y volveríamos a lo que `C6` prohíbe.
   TAMAÑO       es un puntero. Si crece, es que alguien está copiando el kernel otra vez, y
                el validador de deriva de §6.3 es quien lo detecta.

4  SE RESUELVE POR IDENTIDAD, NO POR RUTA — Y LA LÓGICA ES DEL ADAPTADOR, DECLARADA
   El puntero NO declara `../ads`. Declara el REMOTO CANÓNICO, que es lo que `C6` `N9`
   define como identidad. **La lógica de resolución vive en el ADAPTADOR y es un campo de su
   contrato**, `resolucion_del_control_repo` (§3.4), no una frase de prosa:
       estrategia            `hermanos-del-workspace`
       profundidad máxima    de ascenso desde el directorio abierto
       normalización del     sin credenciales · con y sin `.git` · `ssh` y `https` tratados
       remoto comparado      como EQUIVALENTES. Sin decirlo, dos formas del mismo remoto no
                             casan, y el descubrimiento falla por una diferencia de escritura
       desenlaces            para 0, 1 y ≥2 coincidencias
   **Corregido** (hallazgo `I.2`): F4c dejaba esta lógica como prosa sin campo en §3.4, luego
   un adaptador conforme podía **omitirla por completo** y seguir validando contra su tipo.
   Con el campo, «el puntero no contiene instrucciones» pasa a ser cierto Y comprobable: los
   datos están en el puntero, la lógica en el adaptador.
       LO ENCUENTRA         trabaja con el control repo como contexto principal
       NO LO ENCUENTRA      lo DICE, con el remoto que buscaba, y NO ADIVINA. Se comporta
                            como una fuente ausente: bloquea sólo lo que la requiere, que
                            es la regla de alcance mínimo de `C6`
       NO SE PUDO           diagnóstico DISTINTO del anterior, y es el que F4c no tenía. La
       COMPROBAR            regla 4 asume permiso para ejecutar `git` en directorios
                            hermanos, y `C6` dice que los permisos los aporta el entorno. Un
                            entorno con acceso restringido al directorio abierto NO PUEDE
                            ejercerla, y eso no es «ausencia»: es «impedimento». Confundir
                            dos causas bajo un mismo diagnóstico es el defecto que §11.2
                            corrige en `P-08`, y aquí se reintroducía
       ENCUENTRA DOS        ERROR explícito. Dos control repos para el mismo producto es
                            exactamente el defecto que el puntero existe para no crear
```


### El puntero escribe en repositorios técnicos, y eso hay que gobernarlo

> **Corregido por la segunda devolución independiente (hallazgo `I.3`, GRAVE).** El puntero
> **es una proyección** —regla 2, literal— y `U5` recompila proyecciones. Luego **`U5` escribe
> en las fuentes**, y §8.4 declaraba que `U` escribe «la distribución instalada y las
> proyecciones» **sin decir que algunas viven en repositorios ajenos al control repo**, y sin
> una sola precondición, gate, evidencia ni rollback por fuente. La contradicción no era sólo
> con `U0`–`U6`: era **con §8.1 y §8.2, dentro del propio F4**.
>
> ```text
> §8.1 SE AUTOCONTRADECÍA    los adaptadores se eligen en N2 y sus proyecciones se compilan
>                            antes de N6; pero ESCRIBE dice «las fuentes sólo desde N6»
> §8.2 SE AUTOCONTRADECÍA    la adopción declara modo NO DESTRUCTIVO y «ESCRIBE NADA en las
> DE FORMA MÁS SERIA         fuentes hasta A8». La especialización —adaptadores incluidos— es
>                            A5. Un adaptador con puntero obligaba a commitear en un producto
>                            ajeno con historia, TRES FASES antes de que existiera
>                            autorización de escritura. La adopción de un producto ajeno
>                            empezaba haciendo un commit en su repositorio
> `C6` RESPONDÍA QUE NO      a su propia pregunta frontera: el puntero NO deja de ser cierto
> A SU PROPIA FRONTERA       si cambia el código de al lado —depende del control repo—, luego
>                            por la regla de `C6` su sitio sería el control repo
> `C7` LO GOBIERNA Y NADIE   un puntero recompilado por `PLT` durante U5 no tenía item, ni
> LO INVOCABA                paquete, ni custodia, ni checkpoint, ni rama, ni PR — y `main`
>                            está protegida, luego ni siquiera podía empujarse
> ```

**Seis reglas, y ninguna copia conocimiento de ADS a las fuentes:**

```text
1  EXCEPCIÓN DECLARADA A LA FRONTERA DE `C6`
   El puntero está en la fuente por una necesidad real de descubrimiento, y NO porque la
   frontera de `C6` lo permita. Se declara como EXCEPCIÓN NOMBRADA, con su motivo escrito.
   Una excepción declarada es aceptable; una excepción silenciosa reproduce el modo de fallo
   (a) de `a.7` por goteo.

2  TODA ESCRITURA DE PUNTERO ES UN SOURCE CHANGE GOBERNADO POR `C7`
   Se materializa como un PAQUETE con `escribe_fuentes: [<fuente>]`, custodia de `PLT`,
   checkpoint, rama, commit, push, PR y CI por fuente. **No hace falta inventar nada: hace
   falta USARLO.** Lo que `C7` ya norma para cualquier otra escritura vale aquí.

3  `U5` SE PARTE EN DOS
   U5a  recompila las proyecciones DEL CONTROL REPO — lo que §8.4 ya cubría
   U5b  PROPAGA los punteros a las fuentes, con su propio gate, su evidencia POR FUENTE, y
        su INTEGRATION SET cuando hay más de una — que es el caso normal, y donde el defecto
        de `C7` de §9.5 deja de ser teórico

4  ROLLBACK DECLARADO PARA `U5b`
   Por fuente, y con estado INTEGRACIÓN PARCIAL mientras no converjan todas. Un puntero es
   pequeño; la coordinación multi-fuente no lo es. Sin esto, un producto puede quedarse con
   punteros de dos versiones distintas y ninguna pieza del sistema saberlo.

5  `N2` Y `A5` NO ESCRIBEN PUNTEROS
   INSTALACIÓN  el puntero se propaga en **N6**, que es cuando §8.1 autoriza escribir en las
                fuentes. N2 elige el adaptador y compila lo del control repo; nada más
   ADOPCIÓN     el puntero se propaga en **A8**, que es cuando el Owner autoriza, y sólo lo
                que autorice. A0–A7 no tocan el producto, y eso vuelve a ser cierto

6  LÍMITE DE §6.3, DECLARADO
   la deriva de un puntero **sólo es detectable si su fuente está materializada**. Con una
   fuente ausente, el validador LO DICE y no asume nada — que es la regla de `NP-9` aplicada
   aquí, y lo que impide que «huella correcta» se lea como «puntero al día».
```

**Pruebas adversariales `X32`–`X34`.** Adopción hasta `A7` inclusive: `git status` y `git log`
en cada fuente no muestran **ni un solo commit ni un fichero nuevo** de ADS · actualización en
tres fuentes con `main` protegida: la propagación produce tres PR, un Integration Set, y
estado `INTEGRACIÓN PARCIAL` hasta que las tres se fusionan · fusionar dos de tres y comprobar
que el sistema **lo dice**, en vez de declarar la actualización cerrada.

**Límite declarado, y es el que importa.** Que un entorno concreto **honre** el puntero —que
lo lea, que abra el directorio hermano y que trabaje con él— **no lo puede afirmar el
diseño**. Es precisamente lo que mide la **prueba de humo** de §6.4, y hasta que se ejecute,
el nivel alcanzado de ese adaptador es `desconocido`. Un entorno que no pueda honrarlo
degrada a `genérico`, y su `degradacion` declara qué se pierde, función por función.

---

# 7 · Runtime y dispatcher

## 7.1 · Qué es el runtime, y qué no

```text
ES        el EJECUTOR de contratos que ya existen: compone rutas por b.16, materializa por
          C4, aplica los frenos de a.7, calcula el estado global por b.4, consume órdenes
          por a.9 y regenera derivados.

NO ES     una fuente de verdad. Todo lo que decide queda escrito en el estado canónico
          ANTES de que valga. Si el runtime muere, el estado sigue siendo el estado.

REGLA     16.1 de la directiva: «siempre que sea viable, el runtime debe EJECUTAR O VALIDAR
          contratos existentes en lugar de duplicar su semántica en código independiente».
          Un comportamiento del runtime que no corresponda a una regla escrita es un
          defecto, no una feature.
```

## 7.2 · El ciclo

```text
ENTRADA DEL OWNER
   │ expresión literal, conservada siempre con fecha y canal (taxonomía de entrada, regla 1)
   ▼
ENC  clasifica en una de las nueve clases · ancla contra lo existente · produce ENCUADRE
   │ Sólo tres clases crean trabajo. Las demás se registran y esperan (regla 2)
   ▼
DSP  crea el item · determina el PROCESO por el resultado perseguido (b.1) · compone la
   │ ruta desde b.16 con su traza de activadas y NO activadas con motivo (T05)
   ▼
DSP  crea paquetes con su declaración de acoplamiento, incluidas `lee_fuentes` y
   │ `escribe_fuentes` (E2.2), prefiriendo el ALCANCE MÍNIMO coherente
   ▼
DSP  comprueba la condición COMPUESTA de paralelismo (a.5, seis condiciones). Si falla
   │ cualquiera, secuencia. `escribe` disjunto NUNCA basta por sí solo
   ▼
C4   materializa el equipo: composición por orden, roles, agentes por C2, combinación,
   │ límites de execution_slots, y escribe qué quedó fuera y por qué
   ▼
LA CAPACIDAD trabaja · escribe checkpoint tras cada avance semántico · produce su capa ·
   │ registra sus source changes por fuente
   ▼
GATE de su capa · handoff por C5 · o DEVOLUCIÓN con su evidencia obligatoria
   ▼
DSP  recompone si hace falta (b.9), aplica frenos, recalcula estado global (b.4)
   ▼
ENT  declara convergencia con un INTEGRATION SET cuando hubo varias fuentes (E2.6)
   ▼
gate:cierre-de-item — todas las obligaciones RESUELTAS: satisfechas o retiradas (b.3)
```

## 7.3 · Fallos, reintentos, bloqueo y pausa

```text
FALLO DE UNA HERRAMIENTA      se registra como evento `fallo`. No cambia estado canónico
REINTENTO                     sólo para operaciones idempotentes, y con tope. Un reintento
                              sin tope es un livelock, y a.9 ya fijó el precedente: tres
BLOQUEADO                     GENERA TRABAJO: crear el desbloqueador. Dentro del alcance
                              autorizado, DSP lo crea y despacha sin preguntar (b.15.1)
ESPERANDO-DEPENDENCIA         se resuelve solo. NO genera trabajo. Si deja de ser viable,
                              DEBE convertirse en bloqueo: no puede quedar muerta (b.8)
PAUSA POR PRESUPUESTO         completar unidad segura · verificar · persistir · dejar la
                              siguiente acción exacta · NO declarar terminación (§12)
CAÍDA A MITAD                 evento `preparada` de la tx: completar, o `conflicto` si
                              algún fichero es divergente (§2.6)
INCONSISTENCIA IRRESOLUBLE    DSP para y escala. NUNCA inventa estado (b.14.3)
```

## 7.4 · `Continúa`

Los siete pasos de `b.14` se conservan, **con una desviación declarada en el paso 2** y
varias comprobaciones añadidas.

> **Corregido por la segunda devolución independiente (hallazgo `N-9`).** F4c decía que los
> siete pasos «se conservan enteros» y que sólo se añadía «qué mira el paso 2». **No es
> exacto: se cambia su disposición.** Donde (b) escribe *«completar o REVERTIR (a.9)»*, esta
> arquitectura escribe *«completar o marcar conflicto»*, y §2.6 **elimina el ramal de
> reversión por completo**.
>
> La decisión de *roll-forward only* es buena y está argumentada en §2.6.2, y satisface la
> disyunción de `a.9` —«terminarla **o** revertirla»—. Lo que no era aceptable es hacerlo
> **declarando que el texto de (b) se conserva entero**. La desviación queda registrada como
> presión normativa `PN-7` en §16, y no se resuelve aquí.

```text
2 VERIFICAR   · ¿existen los artefactos que los paquetes dicen haber producido?
              · ¿hay transacciones sin evento `derivada`?  → completar, o marcar conflicto
              · ¿hay deriva NO transaccional respecto a `HEAD`? → reportar y escalar (§2.6.6)
              · ¿hay `reconciliacion_pendiente`?           → resolverla antes de nada
              · ¿hay derivados divergentes de su source_revision?  → regenerar
              · ¿hay proyecciones con huella rota?         → recompilar (§6.3)
              · ¿siguen viables todas las `esperando-dependencia`? (b.8)
              · ¿hay celdas de cobertura vencidas?         → sólo REPORTAR, no abrir
```

Los pasos 1 a 4 siguen siendo deterministas y sin Owner. El paso 5 sigue siendo obligatorio y
breve. **`Continúa` no significa «haz todo lo pendiente»**.

## 7.5 · Atención del Owner y vistas ejecutivas

```text
LOS TRES NIVELES de a.8 no cambian: obligatorio · opcional acumulada · ninguna
EL LOTE           lo que espera al Owner se presenta agrupado y ordenado por coste de
                  set-up (G36 y b.15)
LA VISTA          es DERIVADA del estado canónico, no un informe redactado. Es G08 ya
                  ajustado en a.11, y hasta ahora no tenía estado del que derivarse
RESPONDE          qué se está construyendo · qué está bloqueado · qué espera decisión
                  suya · qué cambió · qué riesgos aparecieron · qué se aprendió
NO RESPONDE       nada que no esté en el estado. Una vista que sabe más que el estado es
                  una segunda verdad
```

## 7.6 · Relación con Git y con los adaptadores

```text
CON GIT           el runtime no inventa operaciones: C7 declara quién pide, ejecuta,
                  bloquea y verifica cada una DE LAS FUENTES. El runtime las ORQUESTA y
                  registra su evidencia en el checkpoint del paquete.
                  **EL CONTROL REPO NO ESTÁ CUBIERTO**: ninguna fila de la tabla de
                  propiedad de C7 lo alcanza, y §2.6.10 declara ese hueco en vez de
                  taparlo con esta remisión, que es lo que F4c hacía
CON ADAPTADORES   el runtime no conoce ninguna marca. Entrega al agente el control repo y
                  las rutas de las fuentes necesarias; CÓMO se le entregan es del
                  adaptador. Es C6 literal, y T92 lo comprueba
```

---

# 8 · Los cuatro macrocircuitos

`H1` sostiene que comparten motor de composición. `CI-5` añade la condición que impide leerlo
mal: **compartir motor no aplana las rutas**. Cada uno declara lo suyo.

## 8.0 · Lo común, y lo propio

```text
COMÚN     el motor: ENC → DSP → ruta desde b.16 → C4 → capacidades → gate → estado.
          Ningún macrocircuito crea un tipo de proceso nuevo.
PROPIO    disparador · precondiciones · fases · participantes · lecturas y escrituras ·
          estados persistidos · evidencias · gates · certificación · rollback ·
          reanudación · condición de cierre.
FORMA     cada uno es una INICIATIVA con su plantilla de ruta. No un proceso.
```

## 8.1 · Instalación en proyecto nuevo

```text
DISPARADOR      el Owner quiere gobernar un producto que todavía no existe
PRECONDICIONES  hay un sitio donde crear el workspace · hay remoto para el control repo
FASES           N0 crear y publicar control repo y workspace, CON EL SOPORTE DURABLE
                   MÍNIMO DE `estado/` y la iniciativa de instalación ya escrita
                N1 elaborar y aprobar PROFILE
                N2 elegir topología de fuentes, packs, extensiones y adaptadores
                N3 C0: especializar y verificar la organización YA MATERIALIZADA
                N4 certificar instalación y reanudación
                N5 discovery de producto, dominio y diseño
                N6 engineering bootstrap con evidencia real
                N7 gate «listo para construir»
PARTICIPANTES   Owner · PLT (N0,N2,N6) · ENC+PRD (N1,N5) · SIS (N3) · VER (N4,N7) ·
                ARQ DOM DIS SEG según discovery
LEE             la distribución instalada
ESCRIBE         control repo entero; las fuentes sólo desde N6 — **incluidos los punteros
                de adaptador**, que N2 NO escribe aunque elija el adaptador (§6.7)
ESTADO          `estado/` nace en **N0**, con su soporte durable mínimo. Ver abajo
EVIDENCIA       `workspace check` · prueba de humo por adaptador · checkpoint recuperado
GATES           N4 certificación Operativa · N7 = O12
CERTIFICACIÓN   Operativa en N4 · Integrada en N7, con la aplicabilidad de §9.5: en N7 el
                producto tiene LAS FUENTES QUE N2 DECLARÓ, y la columna que rige es la de
                ese número. Si son 0, hay pruebas que no le aplican
                **Corregido** (hallazgo `N-5`): F4c decía «una instalación nueva tiene CERO
                fuentes», y es falso en N7 — que es donde se invoca
ROLLBACK        ver «Rollback, con el remoto separado de lo local», abajo
REANUDACIÓN     **por checkpoint desde N0**. Ningún tramo del recorrido depende del chat
CIERRE          N7 superado y el primer item de producto despachable
```

**Lo que cambia respecto a hoy.** `C0` deja de redactar la organización y pasa a
**especializar y verificar** una que la distribución ya trae. Es `O9` y el §4.11 del documento
de pendientes: el agente no crea ADS durante C0.

### `estado/` nace en N0, y no en N3

F4 entregada declaraba *«`estado/` nace en N3. La iniciativa de instalación nace en N0»* y
*«REANUDACIÓN por checkpoint desde N3; antes, repitiendo el paso»*. **Las dos frases juntas
dicen que entre N0 y N3 la iniciativa no está persistida**: vive en la conversación. Eso es
exactamente lo que el apartado 19 de la directiva prohíbe, y lo que `b.14` no puede reanudar.

```text
QUÉ SE CREA EN N0,        estado/
Y ES EL MÍNIMO              ├─ iniciativas/INI-001/00-iniciativa.md   la instalación misma
                            ├─ eventos/                               el diario, desde el
                            │                                         primer acto
                            └─ items/INI-001-paq/                     el paquete en curso,
                                                                      con su CHECKPOINT

QUÉ NO SE CREA EN N0      cobertura, integración, tableros de capacidades que no se han
                          materializado, y todo lo que no tenga contenido todavía. Un
                          directorio vacío no es soporte durable: es ruido.

POR QUÉ ES BARATO         son tres ficheros. El coste de crearlos es menor que el de
                          explicar por qué un recorrido de siete fases no se puede reanudar
                          en sus tres primeras.

QUÉ HACE N3 AHORA        lo que `O9` ya decía que hace: ESPECIALIZAR Y VERIFICAR la
                          organización que la distribución trae materializada. Deja de
                          «crear `estado/`», que era lo que lo ponía en contradicción con N0.

QUÉ SE GANA               «Continúa» funciona desde el primer minuto de una instalación. El
                          recorrido se reanuda desde N0 SIN el chat y SIN el Owner, que es
                          `R7` y `b.14` aplicados también a la instalación — y no sólo al
                          trabajo de producto.
```

### Rollback, con el remoto separado de lo local

F4 entregada decía *«N0–N2 se deshacen borrando el workspace: no hay producto que dañar»*.
Pero N0 **publica** el control repo. Borrar lo local no revierte lo publicado.

```text
LOCAL          borrar el workspace deshace lo local, y NADA MÁS.

REMOTO         un control repo YA PUBLICADO sigue existiendo, con su historia y con
               cualquier clon que alguien haya hecho. NO se revierte borrando el local.

COMMITS        permanecen. Un rollback de instalación NO reescribe historia publicada:
               reescribirla rompería todo clon existente, y ADS no lo hace.

AUTORIDAD      **NINGUNA ELIMINACIÓN REMOTA AUTOMÁTICA.** Borrar o archivar un remoto es una
               operación destructiva sobre infraestructura del Owner. ADS **propone** —
               archivar · marcar abandonado · conservar como histórico · eliminar — y la
               eliminación la ejecuta **el Owner**, a mano.

LO QUE ADS SÍ  emite el evento de abandono y lo escribe en el control repo, para que un clon
HACE SOLO      posterior no lea una instalación abandonada como una instalación viva. Es
               barato, es reversible y no destruye nada.

ANTES DE N0    no hay nada que revertir: no se ha publicado.
```

## 8.2 · Adopción profunda de un producto existente

El más largo, y el que `CI-5` protege de ser aplanado contra la instalación.

```text
DISPARADOR      el Owner quiere gobernar un producto CON HISTORIA
PRECONDICIONES  acceso de lectura a todas sus fuentes · modo NO DESTRUCTIVO declarado
FASES           A0  apertura, perímetro y modo no destructivo
                A1  topología: control repo, fuentes, identidad, remotos y permisos
                A2  INVENTARIO
                A3  BASELINE con evidencia
                A4  conocimiento: verdad global, verdad acoplada, duplicados, obsoletos
                A5  especialización: PROFILE, PROJECT, packs, adaptadores, overrides
                A6  reconstrucción: producto, arquitectura, dominio, datos, UI/UX,
                    sistema de diseño, seguridad y operación REALES
                A7  trabajo vivo: issues, TODO, ramas, ideas, deuda, auditorías
                A8  limpieza: retirar copias organizativas y verdades paralelas
                A9  certificación
                A10 preparación y gate
PARTICIPANTES   A2/A3 `AUD` con INV produciendo la capa · A6 activa DOM, SEG,
                DIS/Reconstruccion y PRD, que son LOS CONDICIONALES QUE `proceso:AUD` YA
                DECLARA · A7 ENC · A8 DEU con PLT · A9 SIS+PLT+VER, y SEG si hay superficie
LEE             TODO: código, docs, historial Git, ramas, PR, CI, entornos, despliegues,
                agentes, skills, prompts, reglas, workflows, backlog, incidentes
ESCRIBE         NADA en las fuentes hasta A8, y en A8 sólo lo que el Owner autorice —
                **incluidos los punteros de adaptador**, que A5 NO escribe aunque
                especialice el adaptador. Sin esta corrección, la adopción de un producto
                ajeno empezaba haciendo un commit en su repositorio (§6.7)
ESTADO          la iniciativa de adopción nace en A0 y es el hilo entre chats
EVIDENCIA       inventario con procedencia · baseline aprobado · mapa de conservación
GATES           A3 baseline aprobado por el Owner · A8 autorización de retirada ·
                A10 = O12
CERTIFICACIÓN   Integrada en A9
ROLLBACK        A0–A7 no tocan el producto. Revertir NO es «borrar el control repo»: el
                control repo de A1 está PUBLICADO, y se le aplica el mismo reparto que a la
                instalación —local, remoto, commits y autoridad del Owner— descrito en §8.1.
                A8 exige rollback POR FUENTE y commits revisables por fuente
REANUDACIÓN     por el dosier de la iniciativa más el checkpoint del paquete en curso
CIERRE          A10 superado, y el producto entra en SU macrofase real — que puede ser
                C2, C3 o C4. ADS no finge que empieza de cero
```

> **`O15` · la primera adopción es PERMANENTE, y eso cambia qué es el control repo de A1.**
> El Owner resolvió, después de `O14`, que **PesquerApp es la primera adopción REAL,
> PERMANENTE y COMPLETA de ADS**, y que su control repo **nace definitivo**. El recorrido no
> cambia una fase; lo que cambia es su lectura en tres puntos:
>
> ```text
> A1 CREA UNA INSTALACIÓN   el control repo de la adopción no es un montaje que se tira al
> DEFINITIVA                terminar. Los clones y worktrees aislados protegen LAS FUENTES y
>                           las ramas productivas —que es lo que `O14` pedía—, y NO hacen
>                           desechable el repositorio de control.
>
> QUÉ ENTRA ANTES DE A0     la BASE COMPLETA ACORDADA, no un MVP reducido. Lo que sólo se
>                           puede demostrar contra un producto real se completa DURANTE la
>                           adopción, y es lo que la columna de uso real existe para llenar.
>
> CÓMO ENTRA UN DEFECTO     por §8.3 —migración— o §8.4 —actualización—, sobre la instalación
> DESCUBIERTO EN LA         permanente. Reconstruir o sustituir el control repo exigiría
> ADOPCIÓN                  migración explícita, autoridad y evidencia, y **nunca es el
>                           procedimiento normal**. El `ROLLBACK` de arriba ya lo decía para
>                           el caso puntual: revertir no es «borrar el control repo».
> ```
>
> **Esto no autoriza iniciar la adopción**, y no levanta ninguna de las condiciones de `O14`.

### Lo que la adopción tiene que cubrir de verdad

```text
INVENTARIO          repositorios · código · arquitectura · tecnología · dominio · datos ·
                    integraciones · entornos · despliegue · operación · Git e historial ·
                    agentes · skills · prompts · reglas · workflows · documentación ·
                    UI/UX y sistema de diseño de facto · tareas, ideas, gaps y auditorías

CICATRICES          `Q10` dio el criterio operable, y es de esta fase: NO SE SUSTITUYE LO
                    QUE TIENE CICATRIZ ESCRITA — un mecanismo cuyo motivo está en su propio
                    comentario y sigue siendo cierto. Es la lente `L7` del protocolo de
                    minería, aplicada aquí. `CAND-012`, `CAND-014` y `CAND-024` son los
                    ejemplos medidos, y ADS adoptó tres de los cuatro

CONVERSIÓN          ningún issue, TODO o nota se convierte mecánicamente en item. Pasa por
                    las nueve clases de entrada. El origen NUNCA desaparece

RETIRADA SEGURA     importar o referenciar → validar → retirar. Nunca al revés. Con
                    rollback, evidencia de sustituto canónico, y comprobación de build,
                    pruebas, CI, despliegue y comportamiento agentic tras cada retirada

DOCUMENTACIÓN       la frontera es la pregunta que `C6` ya tiene escrita: ¿esto deja de ser
                    cierto si cambia el código de al lado? Si sí, vive con el código
```

## 8.3 · Migración desde una versión anterior de ADS

```text
DISPARADOR      existe un producto con ADS instalado en disposición antigua
PRECONDICIONES  se conoce la versión instalada · el árbol está limpio
FASES           M0 identificar versión instalada y disposición
                M1 crear control repo separado y declarar las fuentes
                M2 migrar PROFILE, PROJECT, decisiones, memoria y documentación global
                M3 migrar ESTADO PERSISTIDO, con su esquema
                M4 sustituir mecanismos retirados y resolver overrides y forks locales
                M5 CERTIFICAR lo nuevo, con lo viejo TODAVÍA EN PIE
                M6 RETIRAR del repositorio técnico kernel, packs y organización
                M7 VERIFICAR que nada dependía de lo retirado
PARTICIPANTES   PLT · SIS · VER · Owner en M6
DIFERENCIA      lo que la separa de la adopción: aquí **ya hay estado ADS**. No se
CON A           reconstruye una realidad: se TRADUCE una que ya estaba escrita. Los items
                y paquetes en curso tienen que seguir en curso al otro lado
ESTADO          M3 es el paso peligroso: migración de esquema con su migrador y su prueba
EVIDENCIA       equivalencia antes/después de items, paquetes y checkpoints · dictamen de
                M5 · salidas de build, pruebas, CI y despliegue en M7
GATES           M3 no cierra sin equivalencia demostrada · M5 certificación Integrada del
                control repo nuevo · M6 exige autorización EXPLÍCITA del Owner · M7 no
                cierra sin las cuatro salidas verdes
CERTIFICACIÓN   Integrada en M5, ANTES de retirar nada. Revalidada en M7
ROLLBACK        ver «El orden, y por qué certificar y verificar son dos pasos», abajo
REANUDACIÓN     por checkpoint. M3 es idempotente por diseño (§2.6)
CIERRE          M7 superado y el producto operando sobre el control repo nuevo
```

### El orden, y por qué certificar y verificar son dos pasos

F4 entregada declaraba **dos secuencias incompatibles**: la lista de fases ponía `M5 retirar`
antes de `M6 validar y certificar`, y el rollback afirmaba que *«M5 es el único destructivo,
y va DESPUÉS de M6 en el orden real de seguridad»*. Un lector no podía saber cuál ejecutar, y
una de las dos retira material antes de certificar su sustituto. Se fija **una sola**:

```text
M5 CERTIFICAR    ¿funciona lo nuevo?   Se responde con lo VIEJO TODAVÍA EN PIE, que es lo
                 que hace la respuesta barata: si falla, no se ha destruido nada.

M6 RETIRAR       único paso destructivo. Exige autorización explícita del Owner, y sigue la
                 disciplina de RETIRADA SEGURA de §8.2: importar o referenciar → validar →
                 retirar. Nunca al revés.

M7 VERIFICAR     ¿dependía algo de lo retirado?   Es una pregunta DISTINTA, y sólo se puede
                 responder DESPUÉS de retirar: build, pruebas, CI, despliegue y
                 comportamiento agentic, los cinco, sin lo retirado.

LAS DOS SON      M5 no puede responder a M7 —lo viejo sigue ahí y tapa cualquier
NECESARIAS       dependencia oculta—, y M7 no puede sustituir a M5 —llega tarde—. Fundirlas
                 es lo que producía la contradicción.
```

**Rollback, por tramos:**

```text
M0–M5   revertir es ABANDONAR el control repo nuevo. Nada del producto se ha tocado, y se
        le aplica el reparto local/remoto/autoridad de §8.1.
M6      revertir es RESTAURAR lo retirado desde la historia del repositorio técnico. Es un
        `revert`, no una resurrección: el contenido está en Git y por eso M6 puede hacerse.
        Retirar algo que NO estuviera en la historia sería irreversible, y M6 lo prohíbe.
M7      si M7 falla, se revierte M6 y se vuelve a M4. Ver «El alcance de M5, y qué pasa si
        M7 falla», abajo.
```

### El alcance de M5, y qué pasa si M7 falla

> **Corregido por la segunda devolución independiente (hallazgo `G`).** El revisor **refuta
> la premisa** de que el contrato afirmara sin matiz que el sustituto funciona por sí solo:
> §8.3 dice literalmente lo contrario, y `D33` es sólida en su núcleo. **Lo que sí eran reales
> son cinco residuos**, y el mayor era la frase *«la certificación de M5 NO se pierde»*, que
> chocaba con *«Revalidada en M7»* — si fueran la misma afirmación, revalidar no tendría
> sentido.

```text
QUÉ ACREDITA M5           «lo nuevo funciona EN COEXISTENCIA». Nada más, y es mucho: si
                          falla, no se ha destruido nada.

QUÉ PASA AL EJECUTAR M6   M6 CAMBIA la configuración certificada. Por §9.3 —«cambia el
                          entorno»— la celda de `certificacion/integrado` pasa a `vencido`,
                          y con ella BAJA el nivel alcanzado. Es el mismo mecanismo que §6.5
                          celebra para el adaptador —«baja solo, sin que nadie tenga que
                          acordarse de editar nada»—, y F4c lo suspendía aquí sin decir por
                          qué. **`O12` deja de estar satisfecho hasta M7.**

ALCANCE RESIDUAL, COMO    la celda de M5 conserva su evidencia y su `verificacion.ultima_real`
CAMPO Y NO COMO PROSA     y queda en `parcial`, con
                          `motivo: certificado en coexistencia; pendiente de verificación
                          independiente tras la retirada`. El vocabulario de `cobertura` ya
                          lo expresa; F4c no lo usaba.

RESTAURAR M6 OBLIGA A     «revertir es RESTAURAR lo retirado desde la historia» devuelve
REVALIDAR                 FICHEROS. NO devuelve CI, permisos, entornos ni el árbol exacto — y
                          §9.3 dice que cambiar CI o permisos invalida Integrado. Tras el
                          revert **se reejecutan las pruebas de M5** antes de volver a M4.
                          Un revert no es una máquina del tiempo.

LA DEPENDENCIA OCULTA     no es «un item nuevo» sin tipo. Pasa por `ENC` y por las nueve
TIENE PROCESO             clases de entrada, como cualquier finding (§5.3). Los tres destinos
                          plausibles son `DEF` —comportamiento incorrecto—, `DEU`
                          —acoplamiento— y `DEP` —dependencia externa—, y **lo decide `ENC`**,
                          no este apartado.

CONDICIÓN PARA            M6 SÓLO se reintenta cuando el item de la dependencia oculta está
REINTENTAR M6             `cerrado`, su capa `vigente`, y M5 ha sido REEJECUTADA sobre el
                          árbol resultante. **Sin esta condición el tramo admitía un bucle
                          M6→M7→M6 indefinido**, y era el hueco más importante de los cinco.
```

## 8.4 · Actualización de ADS en un proyecto instalado

```text
DISPARADOR      existe una versión de ADS posterior a la instalada. `kernel-status.sh` y
                `.upstream-hash` ya detectan la divergencia: es la mitad que existe
PRINCIPIO       DETECTAR AUTOMÁTICAMENTE, ACTUALIZAR CONSCIENTEMENTE
PRECONDICIONES  árbol limpio · sin transiciones en vuelo · certificación vigente
FASES           U0 detectar versión candidata
                U1 comparar: qué añade, cambia, retira y migra
                U2 impacto EN ESTE PRODUCTO: overrides, personalizaciones, adaptadores,
                   esquemas de estado, trabajo en curso
                U3 plan de migración, con su rollback
                U4 aplicar
                U5a recompilar proyecciones DEL CONTROL REPO
                U5b propagar los PUNTEROS a las fuentes, como source changes gobernados
                    por C7, con gate, evidencia por fuente e Integration Set si hay más
                    de una. Ver §6.7
                U6 certificar
PARTICIPANTES   SIS · PLT · VER · Owner si hay incompatibilidad o retirada
LEE             la distribución nueva y la instalada
ESCRIBE         la distribución instalada y las proyecciones DEL CONTROL REPO en U5a; y
                LAS FUENTES en U5b, sólo el fichero puntero y bajo `C7`. **No el estado**,
                salvo migración de esquema declarada en U3
                **Corregido** (hallazgo `I.3`): F4c decía «la distribución instalada y las
                proyecciones» sin declarar que algunas proyecciones viven en repositorios
                ajenos al control repo
EVIDENCIA       la vista comprensible del cambio que el §14.2 del brief pide
GATES           U3 aprobado antes de U4 · U6 certificación
CERTIFICACIÓN   el nivel que tuviera antes, revalidado. Una actualización que baja el
                nivel alcanzado es un fallo, no un resultado
ROLLBACK        ver «Compatibilidad y rollback DEL ESTADO», abajo. NO basta con volver la
                distribución atrás. Y U5b tiene el SUYO, POR FUENTE, con estado INTEGRACIÓN
                PARCIAL mientras no converjan todas (§6.7)
REANUDACIÓN     por el evento `preparada` de la tx si U4 se interrumpe
CIERRE          U6 superado y la versión instalada es la candidata
```

### Compatibilidad y rollback DEL ESTADO, no sólo de la distribución

F4 entregada decía *«ROLLBACK: volver a la versión anterior CON SU ESTADO»*. Si U4 ejecutó
una migración de esquema, **el estado quedó en el esquema nuevo** y devolver la distribución
atrás produce lo que §2.8 declara ERROR EXPLÍCITO: leer un fichero con `esquema_estado` mayor
que el soportado. El rollback declarado **no era ejecutable**.

```text
COMPATIBILIDAD — LA DECIDE U2, Y ES UNA COMPARACIÓN, NO UN JUICIO

  U2 lee el `esquema_estado` de los canónicos instalados y el que exige la candidata.

  IGUALES              no hay migración. U4 NO TOCA `estado/`, y el rollback es trivial.

  CANDIDATA MAYOR      migración HACIA DELANTE. U3 NO SE APRUEBA sin una de estas dos:
                         · un MIGRADOR INVERSO con su prueba de equivalencia, o
                         · una INSTANTÁNEA del estado previa a U4, versionada
                       Sin ninguna de las dos, la actualización es irreversible, y una
                       actualización irreversible no es una actualización: es una migración,
                       y su sitio es §8.3.

  CANDIDATA MENOR      la distribución candidata NO SOPORTA el estado instalado. NO se
                       aplica. Es un downgrade de esquema, y §2.8 ya fija que leer un
                       esquema mayor que el soportado es error explícito, nunca una
                       interpretación optimista. Se escala al Owner.

ROLLBACK DEL ESTADO

  SIN MIGRACIÓN        volver a la distribución anterior. `estado/` no se tocó, y la
                       certificación previa vuelve a ser la vigente.

  CON MIGRACIÓN        volver la distribución atrás NO BASTA. El rollback:
                         1  ejecuta el MIGRADOR INVERSO, o restaura la INSTANTÁNEA de U3
                         2  VERIFICA equivalencia con el mismo rigor que el gate de M3:
                            items, paquetes y checkpoints, antes y después
                         3  emite su evento, como cualquier transición (§2.6)
                       Si la verificación de equivalencia falla, se PARA Y SE ESCALA. No se
                       deja el estado a medio revertir: eso es `reconciliacion-pendiente`, y
                       `b.4` P0 ya dice que ningún otro cálculo es fiable mientras dure.

  PUNTO DE NO RETORNO  se declara EN U3, por escrito, antes de aprobar: desde qué paso el
                       rollback deja de ser automático y pasa a ser decisión del Owner. Un
                       recorrido cuyo punto de no retorno no está escrito no tiene rollback:
                       tiene una esperanza.
```

**Por qué no se funden `M` y `U`.** Comparten fases con el mismo nombre y no el mismo riesgo:
`M` traduce una disposición entera y toca el estado por definición; `U` cambia la distribución
y **procura no tocar el estado**. Fundirlas obligaría a que cada actualización rutinaria
cargara con el aparato de una migración estructural.

---

# 9 · Certificación

## 9.1 · Los cuatro niveles

| nivel | **afirma** | **NO afirma** | pruebas | propietario | crítico | evidencia |
|---|---|---|---|---|---|---|
| **Estructural** | los ficheros, contratos y referencias existen y son coherentes | que el sistema arranque | los validadores del manifiesto + `gate:sistema-conforme` | `SIS` | el propio validador | evidencia publicada |
| **Operativo** | una sesión nueva arranca, interpreta el proyecto y persiste y recupera un checkpoint | que las fuentes, CI y permisos funcionen | prueba de humo por adaptador · `ENC` recibe una expresión mínima · se crea y persiste un item mínimo · `Continúa` reanuda sin pedir resumen | `SIS` | **`VER`, que no participó en la instalación** | dosier `DICTAMEN` |
| **Integrado** | fuentes, herramientas, CI, permisos y adaptadores funcionan en el entorno real | que el runtime despache, concurra y recupere | las **cinco** de `nivel-certificacion:integrado`: `workspace check` sobre fuentes reales · comandos del producto · CI ejecutable · trabajo multi-fuente verificado como conjunto · `integration-set` producido | `PLT` | `VER` independiente, con `SEG` si hay superficie sensible | dosier + salidas |
| **Completo** | runtime, despacho, reanudación, concurrencia, integración y recuperación están demostrados | que el producto sea bueno | los escenarios de §14 ejecutados sobre un producto real | `SIS` | `VER` independiente | dosier + evidencia ejecutada |

**La lista de pruebas de cada nivel vive UNA SOLA VEZ, en su `nivel-certificacion`** (§9.2).
Esta tabla y la de §9.5 son **proyecciones** de ella, y no censos independientes.

> **Corregido por la devolución técnica previa (hallazgo `8`).** Esta tabla enumeraba
> **cuatro** pruebas de Integrado y §9.5 enumeraba **cinco**, porque añadía `integration-set
> producido`. El documento afirmaba que ambas eran proyecciones de una única lista **y no
> proyectaban el mismo censo**. Ahora las dos proyectan las cinco.
>
> **CRITERIO DE CONSISTENCIA, convertible en prueba por F6:** para cada nivel, el conjunto de
> pruebas de §9.1 y el de §9.5 deben ser **idénticos** al de su `nivel-certificacion`, y
> ninguna de las dos proyecciones puede fusionar dos pruebas en una fila sin declararlo. Una
> diferencia de censo es un fallo, no una simplificación editorial. Es `X52`.

> **Corregido por la segunda devolución independiente (hallazgo `N-4`).** F4c enumeraba
> **cuatro** pruebas para el nivel Integrado en esta tabla y **siete** en §9.5. *«Un "resumen
> legible" que omite tres de siete pruebas no es un resumen: es una segunda lista»* — y `PN-6`
> fija que «Integrada» significa «todas las pruebas APLICABLES superadas», de las cuales había
> **dos censos distintos en el mismo documento**.
>
> **Y dos de las tres añadidas eran de rango Estructural** —«manifiesto válido y coherente» y
> «adaptadores con su proyección y su huella»—, que §9.1 asigna al nivel Estructural y que
> §9.2 declara **presupuesto** por Integrado. Repetirlas creaba dos sitios donde la misma
> comprobación puede pasar y fallar. **Vuelven a Estructural, que es su sitio.**
>
> **La consecuencia con 0 fuentes era una afirmación falsa**, y por eso importa: si las únicas
> pruebas aplicables de Integrado eran esas dos de rango estructural, una celda
> `certificacion/integrado: verificado` autorizaba a afirmar que *«fuentes, herramientas, CI,
> permisos y adaptadores funcionan en el entorno real»* **sin haber comprobado ninguna de las
> cinco cosas**. §9.5 lo mitigaba con «el dosier lo dice», y `O12` no lee el dosier: **lee el
> nivel**. De ahí la regla dura de abajo.

**REGLA DURA AÑADIDA, en `nivel-certificacion`:** un nivel **NO se alcanza si TODAS sus
pruebas propias resultan no aplicables**. Es la condición que impide certificar sobre el
vacío, y no existía.

## 9.2 · Cómo se representa — estado en la celda, norma en la clase

**El ESTADO sigue siendo `cobertura`**, y en eso `D21` acierta: mismo sujeto, mismo ciclo,
misma caducidad y los mismos triggers de invalidación que cualquier otra celda. **Lo que
`D21` no vio es que un nivel es además una NORMA**, y una norma no cabe en la celda del
sujeto que evalúa.

> **La prueba de tipos, reaplicada.** Un nivel de certificación necesita declarar **qué
> pruebas exige, quién es su propietario, quién puede ser su crítico, qué nivel presupone y
> qué lo invalida**. Meter eso en la celda obligaría a repetir las cinco cosas en cada
> instalación del mundo, y a que dos instalaciones pudieran discrepar sobre qué exige
> «Integrado». Eso **no es representar la certificación: es deformar `cobertura`**.

```text
LA CELDA GUARDA ESTADO — una por nivel y por sujeto, con el contrato de §3.5 sin cambios

  sujeto        instalacion:transversal/<producto>
                o adaptador:transversal/<entorno>, o cualquier otro sujeto certificable
  aspecto       aspecto:certificacion/<nivel>          namespace propio, §3.5
  criterio      nivel-certificacion:<nivel>            ref a la NORMA, abajo
  responsables  SÓLO LA DESVIACIÓN respecto al reparto que la norma del nivel declara, con
                su motivo. §3.5 fija que el reparto por defecto se HEREDA y la celda registra
                únicamente lo que se aparta de él
  aplicabilidad obligatoria | condicional | no-aplicable      + motivo + evidencia (§9.5)
  estado        EL ENUM COMPLETO de §3.5, sin recortes. **Corregido** (hallazgo `N-3`):
                F4c listaba SIETE valores y declaraba «con el contrato de §3.5 sin cambios»,
                cuando §3.5 tiene DIEZ. Los tres que faltaban no eran inocuos:
                `findings-abiertos` y `corregido-sin-verificar` son EXACTAMENTE los dos que
                §3.5 justifica por `G13`, y son los dos estados en los que una certificación
                pasa la mayor parte de su vida útil. No hay razón para que la certificación
                pierda la distinción que `G13` impone al resto
  verificacion  ultima_real · revisiones_examinadas · `auditor` y su independencia ·
                `verificador_de_correccion` cuando el estado es `corregido-sin-verificar` o
                `verificado`
  evidencia     el dosier
  caducidad · triggers

LA CLASE GUARDA NORMA — `nivel-certificacion`, esquema de CLASE, una vez en el kernel

  id            nivel-certificacion:<nivel>
  afirma        qué autoriza a afirmar
  no_afirma     qué NO autoriza a afirmar. Es la mitad que impide leerlo de más
  pruebas       la lista, cada una con su `aplicabilidad` y su condición (§9.5)
  propietario   qué capacidad responde del nivel
  critico       qué capacidad lo verifica, y qué INDEPENDENCIA se le exige
  presupone     el nivel que hay que tener alcanzado y VIGENTE antes de éste. Es la
                JERARQUÍA, y es lo que no cabía ni en la celda ni en `gate`
  invalida_por  los triggers de clase, que la celda hereda (§9.3)
```

**Por qué no es un `gate`, y por qué no es un tipo de estado.**

```text
NO ES UN `gate`         un gate declara comprobaciones, evidencia y consecuencia al fallar.
                        No declara `presupone` ni `invalida_por`. Añadírselos daría a todos
                        los gates del sistema dos campos que sólo usaría la certificación,
                        que es deformar un tipo — el paso 1 de §3.1 leído al revés.
                        Cada nivel SÍ USA gates: son parte de su lista de `pruebas`.

NO ES UN TIPO DE        no tiene instancia por producto: hay CUATRO niveles, los mismos en
ESTADO                  toda instalación de ADS, y viajan con el release. Es norma, no
                        estado, y por eso no entra en la cuenta de §3.8 como tipo canónico.

SU PRECEDENTE EXISTE    `esquemas/nivel-novedad.yaml` es exactamente la misma clase de cosa:
                        una escala normativa declarada una vez, referenciada desde donde se
                        aplica. Se sigue ese patrón en vez de inventar otro.
```

### La jerarquía, y qué significa «alcanzado»

```text
estructural  ◀── operativo  ◀── integrado  ◀── completo
             presupone      presupone      presupone

NIVEL ALCANZADO   el mayor nivel cuya celda está `verificado` Y VIGENTE, **y** cuyos niveles
                  presupuestos están todos `verificado` y vigentes.

ES DERIVADO       no se escribe en ninguna parte. Se calcula recorriendo las celdas, igual
                  que el estado de una iniciativa (§3.3.2). Escribirlo sería una segunda
                  verdad, y es el mismo defecto que `adaptador.nivel` (§6.5).

CONSECUENCIA      si `operativo` vence, el nivel alcanzado BAJA a `estructural` aunque la
                  celda de `integrado` siga diciendo `verificado`. Eso es lo correcto: un
                  integrado que se apoya en un operativo vencido no está sostenido, y con
                  un campo editable nadie se habría enterado.

REGLA DURA        un nivel **no se declara por argumento ni por haber pasado el anterior**.
                  Pasar el anterior es NECESARIO y no suficiente. Es la disciplina de
                  [`08-EVIDENCIA-MULTIREPO.md`](08-EVIDENCIA-MULTIREPO.md).
```

## 9.3 · Qué invalida un nivel

```text
ESTRUCTURAL   cambia el corpus instalado · cambia un esquema · falla un validador
OPERATIVO     cambia un adaptador · cambia el arranque · cambia la disposición del estado
INTEGRADO     cambia SOURCES.toml · cambia CI o permisos · cambia un entorno · se añade
              una fuente
COMPLETO      todo lo anterior, más cualquier cambio de runtime
```

**Un cierre de Circuito 0, de adopción, de migración o de actualización relevante dispara la
certificación.** También la dispara una auditoría que detecte deriva entre fuentes de verdad.

## 9.4 · `O12`, exactamente

```text
EMPEZAR A PROGRAMAR   Integrada  +  baseline aprobado  +  ningún desconocido crítico sin
                      clasificar. Las tres, no dos.
DECLARAR TERMINADA    Completa. Y la Completa exige runtime, que no existe.
Y CERTIFICADA
```

**Consecuencia honesta:** hasta que exista runtime, **ninguna instalación ni adopción puede
declararse terminada y plenamente certificada**. Puede empezar a programar, que es lo que
`O12` resuelve.

## 9.5 · Aplicabilidad: una prueba que no aplica no puede bloquear para siempre

F4 entregada exigía para el nivel Integrado *«trabajo multi-fuente mínimo verificado como
conjunto»*, sin condición. `C6` `N4` dice que un producto tiene **0..N fuentes**, y `O12`
exige Integrada para empezar a programar. Las tres frases juntas **bloquean para siempre a
todo producto de un solo repositorio**, por una prueba que no puede satisfacer nunca — y a
toda instalación recién hecha, que tiene cero.

### La aplicabilidad, por número de fuentes declaradas en `SOURCES.toml`

| pruebas del nivel Integrado | 0 fuentes | 1 fuente | N ≥ 2 fuentes |
|---|---|---|---|
| `workspace check` sobre fuentes reales | **no aplica**: no hay fuentes que comprobar | obligatoria | obligatoria |
| comandos del producto ejecutables | **no aplica**: no hay producto todavía | obligatoria | obligatoria |
| CI ejecutable | **no aplica** | obligatoria | obligatoria |
| trabajo multi-fuente verificado como conjunto | **no aplica** | **no aplica**: con una fuente no hay conjunto que converger (`E2.6`) | **obligatoria** |
| `integration-set` producido | **no aplica** | **no aplica**: `E2.6` exige convergencia ENTRE fuentes, y con una no hay divergencia | **obligatoria** |
| ~~manifiesto válido y coherente~~ | — | — | — |
| ~~adaptadores con su proyección y su huella~~ | — | — | — |

> **Las dos filas tachadas se RETIRAN de Integrado** (hallazgo `N-4`): son comprobaciones de
> rango **Estructural**, y §9.2 declara que Integrado **presupone** Estructural. No
> desaparecen del sistema: se exigen donde siempre debieron, y dejan de poder pasar y fallar
> en dos sitios. Se dejan tachadas y no borradas para que se vea qué se movió.

```text
0 FUENTES   un producto que NO HA DECLARADO NINGUNA FUENTE en `SOURCES.toml`. Ocurre
            cuando un ADS Project gobierna un producto que todavía no tiene repositorio de
            código: una fase de dirección, de investigación o de diseño previa al primer
            commit. Integrada se alcanza con lo que SÍ aplica — sujeta a la regla dura de
            §9.1: un nivel no se alcanza si TODAS sus pruebas propias resultan no aplicables.
            **Corregido** (hallazgo `N-5`): F4c decía «una instalación recién hecha, antes de
            N6», y eso es falso en el punto donde se invoca. La aplicabilidad se calcula
            sobre las fuentes DECLARADAS, y `SOURCES.toml` se rellena en **N2**; la Integrada
            se certifica en **N7**, después de N2 y de N6. En N7 el producto tiene, por
            construcción, las fuentes que N2 declaró. El caso de 0 fuentes EXISTE, y no es
            «toda instalación nueva».

1 FUENTE    un producto de un solo repositorio. Es la mayoría de los productos del mundo, y
            F4 entregada lo dejaba fuera del sistema sin darse cuenta.

N ≥ 2       el caso para el que se escribió `E2`, y donde la prueba multi-fuente es
            OBLIGATORIA sin excepción.
```

### Qué exige registrar una prueba no aplicable

**No se omite, y no bloquea.** Se EVALÚA, y la evaluación se escribe. Es el §5.18 aplicado
aquí, y usa los campos que `cobertura` ya tiene (§3.5):

```text
aplicabilidad                 no-aplicable
motivo_no_aplicable           OBLIGATORIO. En lenguaje comprobable, no «no procede»
evidencia_de_inaplicabilidad  OBLIGATORIA. El dato que lo demuestra: `SOURCES.toml@<SHA>`
                              declara N fuentes. Un motivo sin evidencia es una opinión, y
                              una opinión no cierra un nivel de certificación

UNA AUSENCIA SILENCIOSA ES UN FALLO DEL GATE. Que la prueba no aplique se dice; que nadie la
mirara, no se puede decir de ninguna manera que se parezca a lo anterior.
```

### Y la aplicabilidad se REEVALÚA, porque cambia

```text
§9.3 ya declara que «se añade una fuente» invalida el nivel Integrado. Ahora eso tiene
consecuencia real y no sólo formal:

  1 FUENTE → 2 FUENTES    la prueba multi-fuente PASA A APLICAR. La celda de `integrado`
                          vence, y su `aplicabilidad` se recalcula. El producto NO conserva
                          una Integrada obtenida cuando la prueba no le aplicaba.
  2 FUENTES → 1 FUENTE    la prueba deja de aplicar, y eso TAMPOCO se hereda en silencio:
                          la celda vence igual y se reevalúa con la nueva aplicabilidad.

LA APLICABILIDAD ES PARTE DEL VEREDICTO, no una nota al margen. Dos celdas `verificado` con
aplicabilidades distintas NO afirman lo mismo, y el dosier lo dice.
```

> **Esto reinterpreta la precondición de `O12`**, que es una resolución del Owner. Por eso
> queda registrado como presión normativa `PN-6` en §16, y **no se da por aprobado aquí**.

### El defecto de `C7`, que esto destapa — y que hay que registrar hoy

> **Encontrado por la segunda devolución independiente (hallazgo `H`, GRAVE).** F4c leía bien
> su fuente y mal el contrato derivado, y **declaraba a la vez que ese contrato entraba sin
> cambio**. Las tres afirmaciones no pueden ser ciertas juntas.

```text
LO QUE DICE `E2.6`      «Un item con paquetes que escribieron en VARIAS SOURCES no cierra
(APROBADO)              mientras su convergencia no esté declarada y evidenciada en un
                        INTEGRATION SET»

LO QUE DICE `C7` HOY    `gate:convergencia-de-fuentes`
(DERIVADO)              `aplica_a: "todo item cuyos paquetes escribieron en UNA O MÁS
                        fuentes"`, con la comprobación `existe-integration-set`

LO QUE DICE `F4` §9.5   el Integration Set NO APLICA con una sola fuente

LO QUE DECÍA `F4` §15.7 `C7` · REUTILIZADO — es decir, «entra sin cambio», por §15.1
```

**La consecuencia, y es peor que la que `D32` corrigió.** Producto de un solo repositorio.
`FEA-021`, un paquete, escribe en su única fuente. Al cerrar, el validador evalúa `aplica_a`
→ **verdadero**; `existe-integration-set` → no hay ninguno, porque §9.5 declaró que no aplica;
el `fallo` de `C7` dice *«El item no cierra»*. **Un producto de un repositorio no puede cerrar
ni un solo item.** `D32` bloqueaba la certificación inicial; **esto bloquea cada cierre de
item, para siempre.**

**Y NO es una presión normativa. Es un defecto de material DERIVADO:**

```text
`C7` DERIVA DE `E2`     lo declara en su propia cabecera. Su corrección está COMPLETAMENTE
                        DETERMINADA por `E2.6` y NO requiere decisión del Owner ni enmienda
                        de material aprobado.
LA TRAZABILIDAD         `E2.6` (aprobado, dice «varias») → `C7` `gate:convergencia-de-fuentes`
                        (derivado, dice «una o más», INCORRECTO) → `F4` §9.5 (lee bien la
                        fuente y mal el derivado)
SU SITIO ES F6          con prescripción CERRADA. Lo que F4 debe hacer HOY es REGISTRARLO,
                        porque §15.7 afirmaba lo contrario.
```

**La prescripción, cerrada:**

```text
1  `aplica_a`      pasa a "todo item cuyos paquetes escribieron en MÁS DE UNA fuente".
                   Es la traducción literal de «varias sources»
2  CON UNA FUENTE  no queda hueco: `b.10` sigue exigiendo obligaciones resueltas y capas
   ESCRITA         vigentes; el gate de la capa de cada paquete sigue exigiendo su CI; y `C7`
                   sigue gobernando rama, commit, push, PR y merge POR FUENTE. La evidencia
                   es su SOURCE CHANGE en el checkpoint, no un Integration Set
3  ¿UN INTEGRATION SET DE UNA FUENTE ES OPCIONAL, O SIRVE PARA OTRA COSA?
                   Sirve para otra cosa: `C7` exige que responda «¿qué combinación hay que
                   restaurar si se revierte el producto?», y `restaura_a` es OBLIGATORIO en
                   `integration-set.yaml`. Con una fuente esa pregunta sigue teniendo sentido
                   y sigue sin tener otro sitio donde vivir. Y el esquema ya admite
                   `resultado: no-aplica`, luego es expresable HOY sin cambiarlo.
                   → OPCIONAL COMO GATE, RECOMENDADO COMO ANCLA DE RESTAURACIÓN, y
                     explícitamente NO exigido para cerrar
4  QUÉ MÁS SE TOCA en `C7`: el `aplica_a`, y la comprobación `sin-integracion-parcial`, que
                   con una fuente es vacuamente cierta.
                   en `F4`: §15.7 (hecho), §10.2 (hecho) y esta nota.
                   en las pruebas: `T159`–`T170` deben incluir el caso de UNA fuente
5  QUÉ NO SE HACE  NO se edita `C7` en esta pasada: es `kernel/operativo/`, y esta devolución
   AQUÍ            no autoriza a tocarlo. Queda registrado, con su prescripción y su
                   trazabilidad, y su ejecución es F6
```

---

# 10 · Git y multi-repositorio

`C6` y `C7` ya lo gobiernan. Lo que esta arquitectura añade es **dónde queda cada cosa** y qué
falta.

## 10.1 · La cadena, sin inventar un commit multi-repositorio

```text
ITEM / PAQUETE
   │  declara `lee_fuentes` y `escribe_fuentes` (E2.2), con el alcance mínimo coherente
   ▼
0..N SOURCE CHANGES        uno por fuente tocada. Viven en el CHECKPOINT (E2.3)
   │  rama · commit · push · PR · CI, independientes por fuente. Los nombres de rama NO
   │  tienen que coincidir: la asociación vive en ADS (C7)
   ▼
INTEGRATION SET            la única afirmación de que una combinación EXACTA se probó junta
   │  `commit` con patrón de SHA, nunca una rama: una rama se mueve y el conjunto deja de
   │  ser exacto
   ▼
CIERRE DEL ITEM            no cierra con una fuente sin integrar. Si una se fusionó y otra
                           no, el estado es INTEGRACIÓN PARCIAL, no `cerrado` (E2.6)
```

## 10.2 · Reparto, y qué cubre cada pieza

| materia | dónde está resuelto | qué falta |
|---|---|---|
| ramas, worktrees, aislamiento | `C7`, conservando `G29` **por fuente** | ejecución |
| commits, push, PR, revisión, CI | `C7`, tabla de propiedad operación a operación | ejecución |
| conflictos | `a.5`: físicos los secuencia DSP, semánticos abren desacuerdo | ejecución |
| integración lógica multi-fuente | `integration-set` | ejecución |
| releases, hotfixes, rollback | `G29` conservado + `restaura_a` del integration set | ejecución |
| trazabilidad item/paquete ↔ revisiones | source changes en el checkpoint | ejecución |
| **trazabilidad iniciativa ↔ revisiones** | **derivada** de sus items | tipo `iniciativa` |
| reanudación parcial | checkpoint con `sources:` por fuente (E2.3) | ejecución |
| permisos y credenciales | las aporta el entorno; el manifiesto **nunca** los lleva | — |
| trabajo fuera de ADS | `C6`: no se impide y **ADS no finge** que pasó por sus gates | — |
| **ramas abandonadas** | **nada** | `CAND-026` lo midió: diez sin fusionar y nada que las mire. Exige runtime |
| **Integration Set con UNA sola fuente** | **`C7` lo exige y `E2.6` no** | defecto de material DERIVADO con prescripción cerrada (§9.5). Con el texto vigente de `C7`, ningún producto de un repositorio cierra un item. NO es presión normativa. F6 |
| **gobierno Git del CONTROL REPO** | **nada: ninguna fila de `C7` lo alcanza** | `C7` gobierna las operaciones de las FUENTES. El commit y el push del control repo —donde vive `estado/`— no tienen tabla de propiedad. Declarado en §2.6.10, y su relleno es F6 |
| **`T161` no ve una formulación retirada partida por un salto de línea** | **su recorrido es por líneas** | encontrado POR ACCIDENTE al aplicar la corrección de `I.1`. No es un falso negativo grave hoy, y sí es un hueco del recorrido. F6 |
| Git de las fuentes ↔ Git de `ads-kernel` | regla 6 de la directiva: materias distintas | — |

## 10.3 · Lo que no se hace

```text
NO se inventa un commit multi-repositorio. Git no lo ofrece y ADS no lo finge.
NO se exige la misma convención de nombres de rama en todas las fuentes.
NO se copia contenido de una fuente al control repo: se referencia su revisión.
NO se declara integrado un producto porque un PR se fusionara.
```

---

# 11 · `P-08` — vigencia general de la evidencia

Hoy la vigencia está garantizada para `T161` y **para nada más**. Ésta es la solución general,
diseñada y **no implementada**.

## 11.1 · Las cuatro preguntas, que hoy se confunden

```text
INTEGRIDAD    ¿el artefacto es el que se publicó, sin editar?      huella · ya existe
PROCEDENCIA   ¿de quién es, qué orden lo produjo, con qué código?  T158 · ya existe
ÉXITO         ¿su salida respalda el éxito que afirma?             T158 · ya existe
VIGENCIA      ¿sigue describiendo el corpus y las entradas que
              validó?                                              sólo T161
```

Las tres primeras se responden igual aunque la evidencia envejezca. Ésa es exactamente la
razón por la que una evidencia intacta y caducada pasó por válida.

## 11.2 · Dos huellas separadas, y un artefacto que las lleva

F4 entregada describía **una** huella, calculada sobre *«rutas, extensiones y exclusiones»*
del corpus. Con eso, cambiar un helper importado cambiaba trece veredictos y **ninguna
huella**. Se separan tres cosas.

```text
HUELLA SEMÁNTICA      lo que, si cambia, CAMBIA EL VEREDICTO. Seis entradas:

  1  CORPUS                      el CONTENIDO de cada fichero de las entradas declaradas.
                                 No su `mtime`, no su ruta absoluta, no su orden en disco.
  2  IMPLEMENTACIÓN DEL          el fichero del propio validador
     VALIDADOR
  3  IMPORTS COMPARTIDOS         el CIERRE TRANSITIVO de los módulos DEL REPOSITORIO que
                                 importa, CALCULADO recorriendo los imports — nunca una
                                 lista escrita a mano, que es lo que envejece
  4  MANIFIESTO Y                `validadores.yaml`, `reglas.yaml`, `exclusiones.yaml`. Una
     CONFIGURACIÓN               exclusión nueva cambia lo que el validador mira
  5  ARGUMENTOS                  con los que se invocó. `--exclusiones` y sin él no son la
                                 misma ejecución, y hoy producen la misma evidencia
  6  ENTRADAS DECLARADAS         el bloque `entradas:` mismo: rutas, extensiones y
                                 exclusiones, de forma determinista

HUELLA DE ENTORNO     lo que, si cambia, PUEDE cambiar el veredicto sin que cambie nada
                      semántico. DOS entradas, y ninguna más:

  1  VERSIÓN MAYOR.MENOR         del intérprete
     DEL INTÉRPRETE
  2  VERSIÓN DE CADA             biblioteca de terceros que el validador importa
     DEPENDENCIA EXTERNA

  NI hostname · NI usuario · NI rutas absolutas · NI hora · NI número de ejecución.
  Eso rompería `R4`, que prohíbe la volatilidad ajena a las entradas.

ARTEFACTO DE SALIDA   la evidencia publicada. Lleva LAS DOS HUELLAS EN CAMPOS SEPARADOS, y
                      no las mezcla en una sola. Separarlas es lo que permite decir «el
                      veredicto sigue valiendo, pero se obtuvo con otro intérprete» — que es
                      un diagnóstico distinto de «el corpus cambió».
```

### El mecanismo, en cuatro pasos

```text
1  CADA VALIDADOR DECLARA SUS ENTRADAS
   bloque `entradas:` en `validadores.yaml`, junto al `vigencia:` que ya existe.
   Una entrada es un conjunto de ficheros descrito de forma determinista: rutas,
   extensiones y exclusiones. NO una lista escrita a mano que envejece.

2  LA EVIDENCIA LLEVA AMBAS HUELLAS
   `registrar_evidencia.py` las calcula al publicar y las escribe en la cabecera, en dos
   campos. Deterministas, y sin hora de pared.

3  T158 RECALCULA Y COMPARA, Y DISTINGUE DOS DIAGNÓSTICOS
   huella semántica distinta   → CADUCADA. El veredicto ya no describe lo que validó
   huella de entorno distinta  → CADUCADA POR ENTORNO. Mensaje propio: lo que cambió no es
                                 el corpus, y el remedio es el mismo — REGENERAR, nunca
                                 editar — pero el diagnóstico no miente sobre la causa

4  LO QUE NO CAMBIA
   · el runner sigue SIN sobrescribir evidencia válida cuando una ejecución falla.
     Esa negativa protege la evidencia buena, y es lo que destapó el defecto
   · publicación atómica
   · determinismo: sin timestamps, rutas temporales ni duraciones
```

## 11.3 · La caché, y por qué su clave no puede ser el SHA de Git

F4 entregada decía que la huella *«se CACHEA en `.ads/run/cache/` por revisión de Git»`*.

> **Un árbol sucio tiene el mismo `HEAD` y contenido distinto.** Con la revisión de Git como
> clave, la caché sirve un veredicto calculado sobre OTRO contenido. `P-08` existe porque una
> evidencia intacta y caducada pasó por válida; esa caché reproducía el mismo defecto por
> otro camino. Y en el trabajo normal —editar y comprobar— el árbol sucio es el caso
> **permanente**, no el raro: la caché habría estado mintiendo casi siempre.

```text
LA CLAVE       clave = H( huella_semántica ‖ huella_de_entorno )
               Se calcula sobre el CONTENIDO de las entradas, que es cierto con árbol limpio
               y con árbol sucio por igual.

EL SHA DE GIT  se conserva en la evidencia como DATO INFORMATIVO —sirve para localizar el
               commit y para leer la historia— y NO PARTICIPA EN LA CLAVE. Es contexto, no
               identidad.

UN ACIERTO DE  significa: mismas entradas semánticas, mismo entorno, mismo veredicto. Nada
CACHÉ          más, y nada menos.

UNA CLAVE      no existe. La clave es el hash de la concatenación de las dos huellas
PARCIAL        COMPLETAS: no hay forma de acertar con la mitad. Servir por coincidencia
               parcial es el escenario negativo `NP-6`.

DÓNDE VIVE     `.ads/run/cache/`, plano OPERACIONAL. Borrarla entera no pierde nada: se
               recalcula. Si perdiera algo, estaría en el sitio equivocado (§2.4).
```

**Coste, y cómo se acota.** Recalcular la huella semántica de trece validadores exige leer un
conjunto acotado de ficheros y el cierre de imports, que es pequeño. En un árbol sin cambios
la comprobación es un acierto de caché. **Declarado:** si el coste resulta inaceptable en el
piloto, la alternativa es comprobar vigencia sólo en el runner y no en cada invocación
suelta. **El contrato no cambia; cambia cuándo se ejecuta.**

## 11.4 · La raíz de confianza — reducida a un punto declarado, no eliminada

§11.2 de F4 entregada decía que `T158` está exento de comprobarse a sí mismo y que **un
componente exento no puede declarar vigencia**. Es correcto, y dejaba la pregunta sin
responder: **entonces quién comprueba la vigencia de la evidencia de `T158`.**

```text
NO LA DECLARA `T158`      comprobaría su evidencia contra sí mismo. Eso es la circularidad,
                          y no se resuelve escribiéndola con más cuidado.

LA REDUCE EL RUNNER       `registrar_evidencia.py` RECALCULA SIEMPRE la evidencia de `T158`
A UN PUNTO                y NUNCA la lee de caché. No decide si vale: la vuelve a producir.
                          Recalcular es más barato que razonar sobre si vale.
                          **Corregido** (hallazgo `N-10`): F4c decía que esto «elimina la
                          circularidad de raíz en vez de administrarla», y eso contradecía
                          su propia conclusión cuatro líneas más abajo. La circularidad
                          **se REDUCE A UN ÚNICO PUNTO DECLARADO** —el runner—, que es
                          cierto, es defendible y es lo que la sección concluye.

EL RUNNER NO ES UN        no publica evidencia sobre sí mismo, no se cachea y no aparece en
VALIDADOR, Y AUN ASÍ      la matriz de vigencia. Su corrección la comprueban las PRUEBAS
LA CIRCULARIDAD SE        NEGATIVAS `N158*`, que ya rechazan la traza como detección — pero
DESPLAZA, NO DESAPARECE   **la evidencia de `negativos` LA PUBLICA EL RUNNER**. «La
                          corrección del runner la comprueban unas pruebas cuya evidencia
                          publica el runner» es circularidad desplazada un paso. Se dice.

EL ORDEN IMPORTA          `comprobar_evidencia.py` va EL ÚLTIMO, como ya va hoy, para no
                          enmascarar el motivo de otras mutaciones.

Y UN HUECO DE ALCANCE,    §11 gobierna la vigencia de los TRECE VALIDADORES y no dice nada de
DECLARADO                 los DOS GENERADORES —`registro_pruebas.py` y
                          `comprobar_recuentos.py --generar`—, cuyos artefactos derivados
                          padecen EXACTAMENTE el defecto que `P-08` existe para cerrar: una
                          cifra que describe un corpus que ya no existe. Un artefacto
                          generado debe llevar su huella semántica igual que una evidencia,
                          y `NP-11` lo comprueba. **Es un defecto vivo de este repositorio**,
                          y su prueba está en su propio historial: hay commits cuyo único
                          contenido es reanclar una cifra al corpus que creció.

EL SUELO QUE QUEDA        **si el runner miente, nada dentro del repositorio lo detecta.**
ABIERTO, Y SE DICE        Cerrarlo exige un verificador EXTERNO al repositorio, y eso NO se
                          resuelve aquí. Se declara en vez de taparlo con una capa más de
                          comprobación interna, que sólo movería la circularidad de sitio.
```

## 11.5 · Los escenarios negativos que exige

**Cada uno comprueba EL DIAGNÓSTICO, no sólo que el proceso terminara con código distinto de
cero.** Y una **traza cuenta como NO DETECTADA**: un validador que revienta no es un
validador que detecta. Es la disciplina que `N158i`–`N158o` ya impusieron al arnés.

| | escenario | qué debe ocurrir |
|---|---|---|
| `NP-1` | **mismo `HEAD`, un fichero de las entradas modificado en el árbol** | huella semántica distinta → **CADUCADA**, nombrando el fichero. Es el escenario que la clave por SHA de Git no detectaba |
| `NP-2` | cambio en un **helper importado** por el validador, sin tocar el corpus | el cierre transitivo de imports cambia → **CADUCADA**, nombrando el módulo |
| `NP-3` | el mismo validador invocado **con otros argumentos** | huella semántica distinta → **CADUCADA**, nombrando el argumento |
| `NP-4` | **cambio de versión** del intérprete o de una dependencia | huella de entorno distinta → **CADUCADA POR ENTORNO**, con diagnóstico PROPIO, distinto del de `NP-1` |
| `NP-5` | **caché existente con entradas distintas** de las de la invocación | fallo de caché → se recalcula. NUNCA se sirve la entrada vieja |
| `NP-6` | caché cuya clave **coincide parcialmente** | no existe acierto parcial: la clave es el hash de ambas huellas completas |
| `NP-7` | **la evidencia de `T158` está caducada** | el runner la RECALCULA, no la lee de caché. Si aun así no casa, FALLO explícito, no silencio |
| `NP-8` | una **entrada declarada que ya no existe** | fallo explicativo, nombrando la ruta que falta |
| `NP-9` | un validador **sin `entradas:` declaradas** | fallo: no se puede comprobar su vigencia, **y eso se dice**. No se asume vigente |
| `NP-10` | una huella calculada de forma **no determinista** | dos ejecuciones seguidas difieren → fallo. Es `T03` aplicado a la propia huella |
| `NP-11` | un **artefacto GENERADO** desincronizado del corpus que describe | se detecta **y se nombra**. Los dos generadores llevan huella semántica igual que las trece evidencias (hallazgo `N-10`) |

**Y las nueve que ya existen para `vigencia`** siguen en pie, sin cambio.

---

# 12 · Eficiencia sin mediocridad

Propiedad arquitectónica, no una fase posterior de optimización.

## 12.1 · El suelo, que no se negocia

```text
LA CALIDAD POR DEFECTO ES PRODUCCIÓN PROFESIONAL. El presupuesto alarga el calendario;
NO rebaja el gate.

Y en buena parte YA ESTÁ ESCRITO:
  `esquemas/rubrica.yaml`     existe «para no reducir el juicio a una nota»
  `plantillas/DICTAMEN.md`    prohíbe el término medio, que es como se cuela la
                              aprobación complaciente
  `03-ESCALA-DE-NOVEDAD`      «N0 no significa trabajo barato, acabado inferior ni
                              verificación reducida»
  `CON/Experimental`          «construir para saber, no para entregar», con el criterio
                              de descarte declarado ANTES de la primera línea
```

**Lo que falta es extenderlo fuera de diseño**, y ése es trabajo de F6.

## 12.2 · Contexto mínimo suficiente, y ampliable

```text
CATÁLOGO COMPLETO DISPONIBLE en el control repo
        ↓
RUTA + ITEM + PAQUETE ACTUAL
        ↓
CONTEXTO MÍNIMO SUFICIENTE   `C6` ya tiene la mitad: necesidad → componentes afectados →
                             fuentes necesarias → lee/escribe → contexto mínimo.
                             Lo que falta es la mitad DENTRO del control repo: qué
                             métodos, documentos y decisiones se cargan
        ↓
AMPLIACIÓN POR NECESIDAD     el agente amplía cuando detecta incertidumbre.
                             CONTEXTO SELECTIVO NO ES CONTEXTO INSUFICIENTE
```

**Herencia declarada:** `K0.2` —«no leer el kernel, compilar menos de 400 líneas»— quedó
sustituido por procedimientos por estación, y `compile-agents.sh` todavía lo cita. La mitad
que falta es su sucesor.

## 12.3 · Los mecanismos, y qué los limita

| mecanismo | qué ahorra | qué NO puede hacer |
|---|---|---|
| lectura incremental por huella | releer lo que no cambió | sustituir la lectura cuando la decisión es crítica |
| índices y vistas derivadas | recorrer el corpus | ser fuente de verdad |
| caché invalidable por huella de entradas | recomputar análisis vigente | sobrevivir a un cambio de sus entradas, ni al de su entorno (§11.3) |
| selección de modelo por dificultad | modelo fuerte donde hay juicio | usar un modelo insuficiente para cumplir presupuesto |
| reutilización de métodos y skills probadas | rehacer lo resuelto | adoptar sin procedencia |
| skills de terceros con procedencia y hash | reconstruir conocimiento ajeno | entrar sin licencia, origen, integridad y regla de retirada |
| fan-out limitado con integrador declarado | ceremonia sin decisión | existir sin integrador: `C4` lo prohíbe |
| presupuesto como ritmo | trabajo mediocre por prisa | recortar diseño, pruebas o documentación |

## 12.4 · Coste por resultado verificado

```text
LA UNIDAD NO ES «tokens para generar código». Es RECURSOS HASTA UN RESULTADO ACEPTADO,
INTEGRADO Y VERIFICADO, e incluye replanificación, retrabajo, defectos escapados y la
intervención que exigió al Owner.

Un modelo fuerte que resuelve bien un problema complejo puede ser MÁS eficiente que varios
económicos cuyo resultado exige rehacer el trabajo.

MEDICIÓN ADICIONAL, y es la que nadie hace: EL COSTE DE REANUDAR. Es lo que paga el
checkpoint, y sin medirlo el checkpoint parece puro gasto.
```

## 12.5 · Pausa por presupuesto

Los seis pasos del §26.16 **ya son `a.10` y `b.14`**: completar unidad segura, verificar,
persistir estado y evidencia, dejar la siguiente acción exacta, pausar sin declarar
terminación, continuar cuando haya recursos. Lo único nuevo es el **límite** y su **alerta**,
que es contenido de `G24` — un hueco ya declarado en
[`03-INVARIANTES.md`](03-INVARIANTES.md) con dueño asignado.

---

# 13 · Aprendizaje y actualización

## 13.1 · El circuito completo

```text
PRODUCTO
   │ uso real · incidente · auditoría · fricción
   ▼
EVIDENCIA          en el item que la produjo, con su procedencia
   ▼
AUD / APR          `gate:aprendizaje-fundado` ya exige DOS OCURRENCIAS O UN INCIDENTE
   ▼
CLASIFICACIÓN      test de contaminación `K0.10`:
   │                 ¿cierto en otro proyecto de otra clase?   → KERNEL
   │                 ¿en otro de la misma clase?               → PACK
   │                 ¿sólo aquí?                               → PROFILE
   │                 ¿cierto en NUESTROS proyectos y no en los de otro?  → X1, DEFERIDO
   ▼
DESTINO            kernel · pack · tooling · adaptador · blueprint · proyecto · DESCARTE
   ▼
ITEM SIS           en `ads-kernel`, con su justificación de producto enlazada
   ▼
RELEASE DE ADS     con su entrada de changelog y su huella reanclada
   ▼
ACTUALIZACIÓN      §8.4, consciente, con impacto, plan, rollback y certificación
   ▼
PROYECTOS INSTALADOS
```

## 13.2 · Lo que este circuito conserva y lo que le falta

```text
CONSERVA    procedencia obligatoria · umbral de aprendizaje fundado · el test de
            contaminación intacto · el freno de racha SIS · X1 y P-05 DEFERIDOS

LE FALTA    los destinos que el §12 del brief enumera y que hoy NO EXISTEN como destino
            posible: blueprint, adaptador y tooling. Los tres existen ya en esta
            arquitectura, y por eso el circuito puede completarse en F6

NO HACE     subir todo. Un aprendizaje puede terminar en el propio proyecto, o
            descartarse. `G52` ya fija techo de entradas vigentes y curación obligatoria
```

## 13.3 · Conocimiento externo

```text
`P-02` se resuelve extendiendo lo que YA funciona con lo propio: `K0.11` y `huella.py`
gobiernan el kernel vendorizado con hash de referencia y detección de fork.

Un manifiesto de vendorizado declara, por pieza externa:
    origen · tipo de origen · versión · hash · licencia · precedencia · actualización ·
    retirada · diferencias frente a las reglas del proyecto

Y para las herramientas de contexto —Caveman o equivalentes— los nueve campos del §26.7 son
los mismos: problema que resuelve, compatibilidad, coste, precisión, procedencia,
privacidad, frescura, impacto medido y degradación si deja de estar disponible.

CUÁLES SE ADOPTAN LO DECIDE INVESTIGACIÓN, no esta fase. Un `INV` con su banco de pruebas.
```

---

# 14 · Escenarios extremo a extremo

**Ninguno se ha ejecutado.** Son recorridos arquitectónicos, y sirven para una sola cosa:
demostrar que las piezas encajan sin contradecirse. El piloto sigue pendiente.

| | escenario | fuentes que se leen | estado que cambia | quién escribe | gate | evidencia | cómo se recupera |
|---|---|---|---|---|---|---|---|
| 1 | **proyecto nuevo** | distribución instalada | `estado/` nace · item de instalación | `PLT` · `SIS` · runtime | N4 Operativa, N7 = `O12` | `workspace check` · prueba de humo · checkpoint recuperado | repetir el paso; antes de N3 no hay estado que perder |
| 2 | **adopción de PesquerApp** | los dos repositorios enteros, sólo lectura | iniciativa A0 · inventario · baseline · cobertura inicial | `INV` la capa, `SIS` consumidor | A3 baseline, A8 retirada, A10 = `O12` | inventario con procedencia · dictamen de `VER` | dosier de la iniciativa + checkpoint del paquete |
| 3 | **migración desde ADS anterior** | control repo antiguo y fuentes | estado **traducido**, con esquema nuevo | `PLT` · `SIS` | M3 equivalencia, M5 autorización | equivalencia antes/después de items y checkpoints | el evento `preparada` de la tx; M3 es idempotente |
| 4 | **actualización de ADS** | distribución candidata e instalada | distribución instalada · proyecciones | `SIS` · `PLT` | U3 plan aprobado, U6 certificación | vista comprensible del cambio | rollback a la versión anterior con su estado |
| 5 | **feature amplia por iniciativa** | componentes afectados y sus fuentes | iniciativa + N items + paquetes | las capacidades con custodia | gate de cierre de la iniciativa | capas, source changes e integration set | dosier derivado + checkpoints |
| 6 | **auditoría recurrente → campaña** | los sujetos de las celdas vencidas | cobertura · items `AUD` · iniciativa campaña | runtime dentro de `O7` · `ENC` clasifica | gate de cada `AUD` + cierre de campaña | dictámenes · findings con causa raíz | la celda y su estado; nada se pierde |
| 7 | **reanudación tras chat agotado** | estado canónico completo | ninguno hasta despachar | runtime | — | el reporte breve de `b.14` paso 5 | es el escenario: `Continúa` |
| 8 | **caída durante escritura** | `estado/eventos/` y los marcadores de `estado/tx/` | se completa o se marca conflicto | runtime | — | los eventos de la transacción | §2.6, sin inventar estado |
| 9 | **dos fuentes y cierre** | `frontend` y `backend` | paquetes con source changes · integration set | capacidades con custodia · `ENT` | `gate:convergencia-de-fuentes` | el integration set, con SHA por fuente | checkpoint con `sources:` |
| 10 | **de Claude Code a Codex** | definición canónica del adaptador | proyecciones nuevas · cobertura de instalación | `PLT` | prueba de humo | salida de la prueba en sesión nueva | el estado no se toca: es neutral por diseño |
| 11 | **evidencia caducada** | entradas declaradas del validador | ninguno: se regenera evidencia | el runner | `T158` | la huella que no casa | regenerar, nunca editar |
| 12 | **aprendizaje promovido** | evidencia del item de origen | ledger · item `SIS` en `ads-kernel` | `APR` · `SIS` | `gate:aprendizaje-fundado` | dos ocurrencias o un incidente | el ledger conserva la procedencia |

**Lo que los doce demuestran juntos**: que ningún escenario necesita un almacén nuevo, un
proceso nuevo ni una capa nueva. Los cuatro tipos de estado de §3 aparecen, y el esquema de
clase de §9.2; nada más.

**Lo que NO demuestran**: que funcionen. Para eso hace falta el piloto de `O14`.

---

# 15 · Trazabilidad y decisiones

## 15.1 · Clasificación usada

```text
REUTILIZADA    entra sin cambio
AMPLIADA       se le añaden campos o alcance, sin romper lo anterior
NUEVA          tipo, artefacto o mecanismo que no existía
DERIVADA       se calcula; no se guarda ni se edita
DEFERIDA       la evidencia disponible no permite decidir
RECHAZADA      no entra, con motivo
PRESIÓN F5     exige enmienda de material aprobado antes de construirse
```

## 15.2 · Los veintiséis apartados de la directiva

| § | materia | dónde queda | clase |
|---|---|---|---|
| 2 | intención → trabajo persistente | §2 estado durable + §7 runtime | NUEVA |
| 3.1 | el Owner no es scheduler | §7.5 + `a.8` | REUTILIZADA |
| 3.2 | organización independiente del agente | `C1` · `C2` · §6.6 | REUTILIZADA |
| 3.3 | productor y crítico independientes | §9 crítico por nivel | AMPLIADA |
| 3.4 | evidencia antes que afirmación | §9 + §11 | AMPLIADA |
| 3.5 | fuente única de verdad | §1.3 matriz | AMPLIADA |
| 3.6 | persistencia y recuperación | §2 | NUEVA |
| 3.7 | el sistema no crece sin control | §3.1 prueba de tipo nuevo | REUTILIZADA |
| 4.1 | reglas universales | `kernel/operativo/` | REUTILIZADA |
| 4.2 | conocimiento por clase | packs | REUTILIZADA |
| 4.3 | conocimiento nuestro reutilizable | `X1` | **DEFERIDA** |
| 4.4 | conocimiento del proyecto | §1.2 especialización | AMPLIADA |
| 5 | minería | `X4`: es un `AUD` | REUTILIZADA |
| 6 | adopción | §8.2 | NUEVA |
| 7 | proyecto nuevo instalable | §8.1 | NUEVA |
| 8 | gobierno Git del producto | §10 · `C6` · `C7` | REUTILIZADA |
| 8.3 | Git como memoria operativa | §10.2: ramas abandonadas siguen sin cubrir | **PARCIAL** |
| 9 | neutralidad con adaptadores | §6 | NUEVA |
| 10 | skills y agentes de primera clase | §6 la skill es contenido de adaptador | AMPLIADA |
| 11 | base tecnológica y defaults | `X1` | **DEFERIDA** |
| 12 | aprendizaje proyecto → ADS | §13 | AMPLIADA |
| 13 | documentación de lo aprendido | §4 + §13 | NUEVA |
| 14 | actualización ADS → proyectos | §8.4 | NUEVA |
| 15 | instalable como sistema | §8.1 + §9 | NUEVA |
| 16 | runtime real | §7 | NUEVA · **PRESIÓN F5** |
| 17 | circuito formal de PROFILE | §8.1 N1 · §8.2 A5 | NUEVA |
| 18 | ADS se evoluciona con ADS | §13, y esta iniciativa es su primer intento | AMPLIADA |
| 19 | no depender de un chat | §2 + §7.4 | NUEVA |
| 20 | estado ejecutivo | §7.5, vista derivada | NUEVA |
| 21 | criterios de realidad | §9 + §11 | REUTILIZADA |
| 22 | compatibilidad y migración | §8.3 · §8.4 · §2.8 | NUEVA |
| 23 | trabajo previo | F0–F3, entregado | REUTILIZADA |

## 15.3 · `H1`–`H6` y `CI-1`–`CI-6`

| | conclusión | qué hace F4 con ella |
|---|---|---|
| `H1` | los macrocircuitos son una composición | §8: motor común, cuatro recorridos con lo suyo |
| `H2` | el estado es el cuello de botella | §2, decidido primero |
| `H3` | el adaptador es proyección compilada | §6, en cuatro piezas |
| `H4` | el sujeto de `P-03` | §5.1, corregido por `CI-1`: ancla, no sujeto único |
| `H5` | contrato documental | §4, resuelto por composición |
| `H6` | máxima documentación contra mínima complejidad | §4.3, resuelto por `O8` |
| `CI-1` | sujeto auditable con subordinados y transversales | §5.1 referencia tipada, sin tipo nuevo |
| `CI-2` | `H5` es candidato, no conclusión | §4.1, vía 3 elegida y comparada |
| `CI-3` | `X8` cerrada por lectura | §1.2 cinco planos, sin cuarta capa |
| `CI-4` | doce áreas semánticas | §4.3 |
| `CI-5` | no aplanar rutas | §8.0 y §8.4 |
| `CI-6` | cuatro piezas del adaptador | §6.1–§6.4 |

## 15.4 · `O7`–`O14` y `P-01`–`P-08`

| | dónde queda | clase |
|---|---|---|
| `O7` política de auditoría | §5.4 | NUEVA · **PRESIÓN F5** |
| `O8` mínimo documental | §4.3 | NUEVA |
| `O9` catálogo, no equipo | §1.2 | REUTILIZADA |
| `O10` `docs/owner/` | ya aplicado | REUTILIZADA |
| `O11` `iniciativa` | §3.3 | NUEVA |
| `O12` gate de arranque | §9.4 | NUEVA |
| `O13` matriz agentic | §6.5 | NUEVA |
| `O14` piloto PesquerApp | §14 escenario 2 · §8.2 | DEFERIDA a F6 |
| `O15` la adopción de PesquerApp es PERMANENTE | §8.2 · §18 · §19 | NUEVA · revisa `O14` · DEFERIDA a F6 |
| `P-01` adaptador sin contrato | §6 | NUEVA |
| `P-02` conocimiento externo | §13.3 | AMPLIADA |
| `P-03` calidad por área | §5 | NUEVA |
| `P-04` gobierno Git | §10 | REUTILIZADA · falta ejecución |
| `P-05` capa entre PACK y PROFILE | — | **DEFERIDA** |
| `P-06` deriva núcleo/adaptadores | §6.3 | NUEVA |
| `P-07` material en voz del Owner | ya aplicado | REUTILIZADA |
| `P-08` vigencia de la evidencia | §11 | NUEVA |

## 15.5 · `X1`–`X8`

| | estado tras F4 |
|---|---|
| `X1` cuarta capa | **DEFERIDA**. §1.2 separa ciclo de vida de conocimiento y no la cruza |
| `X2` runtime contra `G03` | la parte de persistencia procede (§2, §7). La parte desatendida la abre `O7` → **PRESIÓN F5** |
| `X3` neutralidad y adaptadores | **RESUELTA** en §6 |
| `X4` minería como proceso | **RESUELTA**: es un `AUD` |
| `X5` documento en voz del Owner | **RESUELTA** por `O10` |
| `X6` auditoría autónoma | **RESUELTA** por `O7` → **PRESIÓN F5** |
| `X7` mínimo documental | **RESUELTA** por `O8` |
| `X8` organización preestructurada | **RESUELTA** por lectura de `a.4`, `E1` y `C4` |

## 15.6 · Los 29 candidatos

| destino | candidatos | dónde |
|---|---|---|
| contrato de adaptador | `009` `010` `011` `012` `013` `014` `023` | §6 |
| estado persistido | `001` `004` `007` `008` | §2 |
| calidad por área | `019` `021` | §5 |
| conocimiento externo | `015` `027` | §13.3 |
| deriva | `016` `028` | §6.3 |
| gobierno Git | `025` `026` | §10 |
| pack `web-app` | `022` `024` | F6, sin dependencias |
| confirmación sin cambio | `002` `003` `005` `020` | — |
| contenido de plantilla | `017` `018` | §4 |
| no sube | `006` | — |
| deferido | `029` | `X1` |

## 15.7 · `C1`–`C7`, y los criterios que siguen sin demostrar

| contrato | efecto de F4 |
|---|---|
| `C1` rol y equipo | REUTILIZADO |
| `C2` agentes y modelos | AMPLIADO: §12.3 añade escalado ante incertidumbre y registro del modelo |
| `C3` método ejecutable | REUTILIZADO |
| `C4` materialización | REUTILIZADO. `X8` se resolvió leyéndolo |
| `C5` handoff | REUTILIZADO |
| `C6` producto, fuentes y workspace | REUTILIZADO. §5.1 se apoya en su componente sin deformarlo |
| `C7` gobierno Git | **REUTILIZADO CON UNA CORRECCIÓN PENDIENTE, NOMBRADA.** Su `gate:convergencia-de-fuentes` dice `aplica_a: "una o más fuentes"` y `E2.6` —su fuente aprobada— dice «varias sources». Con el texto vigente, ningún producto de un repositorio cierra un solo item. Es un defecto de DERIVADO con prescripción cerrada (§9.5); NO es presión normativa; su ejecución es F6. **Y el control repo no está cubierto por su tabla de propiedad** (§2.6.10) |

```text
T169 · T170       siguen en contrato-definido. Exigen runtime y dos repos reales
CA-10 · CA-11     siguen dependiendo de runtime
§100              comprobada la condición necesaria; el DESCUBRIMIENTO exige piloto
NINGUNO SUBE DE ESTADO POR ESTAR DISEÑADO.
```

## 15.8 · Decisiones técnicas de esta fase

Se registran en la serie existente, en
[`DECISIONES-Y-CONTRADICCIONES.md`](../rediseno/DECISIONES-Y-CONTRADICCIONES.md), como
`D16`–`D22`. Aquí su resumen y la alternativa descartada:

| | decisión | alternativa descartada | por qué |
|---|---|---|---|
| `D16` | estado canónico en ficheros + diario + manifiesto de tx | SQLite canónico · event sourcing puro · sólo ficheros | los dos primeros rompen «el estado ES los ficheros, legibles sin informe intermedio»; el tercero no cumple la atomicidad que `a.9` exige |
| `D17` | el diario **es** el `JOURNAL` de `G26` | un `JOURNAL` aparte del event log | dos registros de lo mismo es la duplicidad que `I5` prohíbe |
| `D18` | cuatro tipos nuevos: `iniciativa`, `adaptador`, `cobertura`, `evento` | un tipo por materia | la prueba de §3.1, aplicada materia a materia |
| `D19` | el sujeto auditable es referencia tipada, no tipo | tipo `sujeto-auditable` · declararlo en `SOURCES.toml` | el primero exige un registro paralelo que nadie mantendría; el segundo deforma un manifiesto que es fuente única de otra cosa (`D11`) |
| `D20` | contrato documental por composición `memoria` + `cobertura` | generalizar `memoria` · metadata especializada | la primera convierte un tipo con sujeto claro en un cajón; la segunda duplica cinco campos |
| `D21` | la certificación es `cobertura` con `clase: instalacion` | tipo `certificacion` | tiene el mismo sujeto, el mismo ciclo y la misma caducidad |
| `D22` | el estado de una `iniciativa` es derivado y no anida | estado editable · anidación | un estado editable sobre lo mismo es segunda verdad (`I5`); la anidación convierte la vista del Owner en un cálculo sobre un árbol arbitrario |

### `D23`–`D33` · las decisiones de la devolución independiente

**`D16`–`D22` NO se reescriben.** Están tomadas y son historia. Lo que las corrige son
decisiones **posteriores**, que declaran qué queda revisado, por qué y cómo se revierte — la
misma vía por la que `O7`–`O14` entraron sin tocar `O1`–`O6`. Su registro canónico es el
mismo fichero; aquí queda su resumen y qué revisa cada una.

| | decisión | qué revisa | por qué |
|---|---|---|---|
| `D23` | el manifiesto de transacción **deja de ser un artefacto propio**: una transacción es una secuencia de eventos inmutables con `tx` común y campo `fase` | **`D16`** | un artefacto que cambia de fase hay que reescribirlo, y reescribir el registro que debe sobrevivir a una caída era el defecto. Además dejaba a `evento.tx` apuntando a algo borrado (§2.5) |
| `D24` | los ids de evento son **direccionados por contenido y no monotónicos** | **`D16`** y §2.8 | un id monotónico se calcula leyendo el mayor y sumando uno: dos emisores concurrentes eligen el mismo. La afirmación «no colisionan jamás» era falsa (§2.7) |
| `D25` | `cobertura` se parte en **`sujeto` · `aspecto` · `responsables` · `criterio`** | **`D18`**, en la forma de `cobertura` | un campo `dimension` que era «la capacidad que la posee» fundía accesibilidad y responsive en una celda, y metía las doce áreas y los cuatro niveles en el mismo campo sin namespace (§3.5) |
| `D26` | la certificación **sigue siendo `cobertura`** para el ESTADO, **y exige** un esquema de clase `nivel-certificacion` para la NORMA | **`D21`**, confirmada en su conclusión y corregida en su fundamento | pruebas, propietario, crítico, **jerarquía** e invalidación son de la clase, no del sujeto evaluado. En la celda se repetirían en cada instalación y podrían discrepar (§9.2) |
| `D27` | **`memoria` se generaliza**, y se declara. `capa` pasa a condicional y nace `plano` | **SUSTITUYE a `D20`** | `D20` decía «composición sin generalización» y §3.7 generalizaba `memoria` en silencio. Se hacían las dos cosas y sólo se contaba una (§4.1) |
| `D28` | `adaptador.nivel` **desaparece**: compatibilidad declarada · capacidades del entorno · **nivel alcanzado, derivado** | **`D18`**, en la forma de `adaptador` | editable y derivado a la vez es segunda verdad, y un campo editable no caduca mientras una certificación sí (§6.5) |
| `D29` | el estado de iniciativa es **función total con precedencia `Q0`–`Q9`**, y **no se persiste** en ningún canónico | **`D22`**, confirmada y completada | los cinco estados anteriores se solapaban y dejaban huecos, y `D22` no decía DÓNDE aparecía el estado derivado (§3.3.1) |
| `D30` | **`estado/` nace en N0**, con su soporte durable mínimo | §8.1 | una iniciativa que nace en N0 con soporte desde N3 vive en el chat entre medias, y el apartado 19 de la directiva lo prohíbe |
| `D31` | la clave de caché de `P-08` es **el contenido**, con tres huellas separadas. **Nunca el SHA de Git** | §11.3 | un árbol sucio tiene el mismo `HEAD` y contenido distinto, y en el trabajo normal ése es el caso permanente |
| `D32` | la **aplicabilidad de la certificación Integrada** depende del número de fuentes | §9.1 | `C6` `N4` admite 0..N fuentes, y la prueba multi-fuente bloqueaba para siempre a todo producto de un repositorio. Genera `PN-6` |
| `D33` | secuencia de migración **M5 certifica · M6 retira · M7 verifica** | §8.3 | la lista de fases y el rollback declaraban órdenes incompatibles, y una de las dos retiraba antes de certificar |

### `D34`–`D45` · las decisiones de la SEGUNDA devolución independiente

Un revisor con contexto limpio, que **no escribió F4 y no aplicó la primera crítica**, emitió
un veredicto de **INSUFICIENCIA**. `D16`–`D33` conservan su texto; éstas los revisan.

| | decisión | qué revisa | por qué |
|---|---|---|---|
| `D34` | `fsync` de DIRECTORIO obligatorio también para los canónicos, y en el orden correcto | `D16` · `D23` | **BLOQUEANTE**: F4c cometía, en los ficheros que **son** el estado, el error que su propia garantía 3 nombraba como «el error clásico» — y el fallo era SILENCIOSO |
| `D35` | `conflicto` deja de ser terminal: abierto, absorbente, y emite `reconciliacion_pendiente` | `D23` | **BLOQUEANTE**: el protocolo nunca emitía el único estado del que depende `b.4` P0, luego una colisión producía un repositorio que el sistema declaraba sano |
| `D36` | comprobación de integridad post-terminal | `D23` | sin ella, `D34` depende de que la implementación no tenga defectos |
| `D37` | contrato de identidad completo, y la idempotencia vive en `tx`, no en `id` | `D24` | `D24` eligió ids por contenido y no dijo **qué** contenido: circular, sin serialización canónica, y con una idempotencia que `predecesor` hacía falsa |
| `D38` | `abortada` se retira. Cuatro registros, no cinco | `D23` | era formalmente definida y **operacionalmente inalcanzable** |
| `D39` | regla de lectura, marcador con contenido, `tx_abierta` en cabecera. **Detectabilidad, no aislamiento** | `D16` · `D23` | no había ninguna regla dirigida a ningún lector, y el marcador vacío obligaba a reproyectar el diario — el coste con que §2.2 descarta el event sourcing puro |
| `D40` | el marcador se excluye de Git | `D23` | la garantía 6 enunciaba como normal un estado que la regla de commit declara imposible, y F4c violaba su propio criterio de §2.4 |
| `D41` | el push deja de ser automático, y se declara que el gobierno Git del control repo **no existe** | `D16` | «se hace el push» convertía una recuperación local en publicación remota, sin autoridad, sin rama y sin ramal de fallo |
| `D42` | `evaluacion_de_pruebas` en `cobertura`, y `verificador` se parte en dos | `D25` · `D32` | la inaplicabilidad se evalúa prueba a prueba y no cabía en una norma de clase; y un campo significaba dos cosas en dos secciones |
| `D43` | nace `contrato-de-aspecto`. Recuento **24 → 25** | `D25` · `D26` | se invocaba TRES veces como sede normativa y no existía. Mismo modo de fallo que el manifiesto de transacción, reproducido y no detectado |
| `D44` | el documento gobernado tiene ciclo propio de cuatro valores | **sustituye parte de `D27`** | `b.3` dice `invalidada`, no `retirada`, y un documento derogado sin reemplazo no podía escribirse con ningún valor válido |
| `D45` | los predicados de obligación se definen a nivel de iniciativa | `D29` | `Q9` no era computable: toda obligación de iniciativa era huérfana desde que se escribía, y ninguna iniciativa con obligaciones podía cerrar |

### `D46`–`D51` · las decisiones de la devolución técnica previa

Una **auditoría externa sobre el árbol remoto real** —no un informe— devolvió once hallazgos.
**No certifica `F4c`**: es revisión técnica previa. `D16`–`D45` conservan su texto.

| | decisión | qué revisa | por qué |
|---|---|---|---|
| `D46` | cinco fases, dos rutas, y `derivada` como único terminal | `D38` · `D23` · `D35` | **BLOQUEANTE**: había cinco formulaciones incompatibles del mismo autómata, y hacer terminal a `confirmada` dejaba los derivados sin regenerar |
| `D47` | dos huellas y un artefacto que las contiene, no tres huellas | `D31` | el artefacto no es una huella. Lo detectó `N-13` y sobrevivió en los resúmenes vigentes |
| `D48` | la detectabilidad no escribe nada en el contenido canónico | `D39` | **BLOQUEANTE**: `tx_abierta` rompía el `hash_posterior_esperado` que la propia transacción declara |
| `D49` | `reconciliacion_pendiente` es predicado derivado, no bandera | `D35` | **BLOQUEANTE**: exigía abrir una transacción para registrar lo que impide abrir transacciones |
| `D50` | el marcador es operacional, con excepción de ruta declarada | `D40` | creaba una tercera categoría informal que §2.4 no tiene |
| `D51` | reparto de dominio: certificación sólo en `nivel-certificacion` | `D43` · `D26` | dos normas editables para el mismo aspecto |

### `D52`–`D54` · las decisiones de la corrección técnica posterior

Posterior a la devolución técnica previa y **anterior a la tercera revisión independiente**.
Dos de sus tres hallazgos son BLOQUEANTES, y los tres están en texto que las correcciones
anteriores escribieron. `D16`–`D51` conservan su texto.

| | decisión | qué revisa | por qué |
|---|---|---|---|
| `D52` | **seis fases**: la ruta de conflicto gana `reconciliacion-preparada`, su intención durable previa | `D46` · `D35` | **BLOQUEANTE**: la reconciliación no era recuperable — una caída entre decidir y emitir dejaba el diario sin la decisión |
| `D53` | lo descubierto tras el cierre es un evento `deriva`, no una fase | `D34` · `D46` | **BLOQUEANTE**: la integridad post-terminal emitía `conflicto` sobre una transacción terminal, saliendo del terminal |
| `D54` | contrato **condicional por fase** para `evento` | `D23` | el contrato genérico no podía representar lo divergente, la decisión ni el `hash_final` |

### `D55`–`D57` · las decisiones de la SEGUNDA corrección técnica

Posterior a `D52`–`D54` y **anterior a la tercera revisión independiente**. Sus tres
hallazgos están en texto que la corrección técnica ANTERIOR escribió — el tercer
encadenamiento consecutivo. `D16`–`D54` conservan su texto.

| | decisión | qué revisa | por qué |
|---|---|---|---|
| `D55` | las garantías se reparten en **tres capas**: esquema estructural del evento, validador semántico del diario, y runtime con pruebas de caída | `D54` · `D46` · `D23` | **GRAVE**: tres de las cuatro reglas de `D54` son incomprobables por un esquema, que valida un evento aislado. Atribuírselas las dejaba sin dueño |
| `D56` | la recuperación clasifica contra la **última fase durable**, y `conflicto` exige transacción abierta **y** divergencia real | `D34` · `D36` · `D35` · `D53` | **GRAVE**: `W12a` mandaba `conflicto` donde §2.6.4, `W3` y `W4` mandan completar. Y la regla del clon emitía `conflicto` sin transacción abierta alguna |
| `D57` | `tipo` y `fase` son **dos ejes**, con matriz declarada: siete tipos transaccionales × seis fases, más `deriva` y `fallo` sin fase | `D54` · `D23` | **GRAVE**: «las ocho formas de evento» contaba el eje `fase`, y siete de los nueve valores de `tipo` quedaban sin contrato |

### `D58`–`D59` · las decisiones de la TERCERA comprobación técnica

Comprobación acotada sobre `D55`–`D57`. **Cuarto encadenamiento consecutivo**: sus dos
hallazgos están en texto que la corrección anterior escribió. `D16`–`D57` conservan su texto.

| | decisión | qué revisa | por qué |
|---|---|---|---|
| `D58` | emitir y **restaurar** son distintos, y **`confirmada → confirmada` no existe**; cardinalidad de cada fase declarada por `tx` | `D56` · `D37` | «reemisión como evento nuevo» contradecía §2.8 punto 5, que ya la declaraba NO-OPERACIÓN, y creaba una secuencia que el autómata no tiene |
| `D59` | recuento **separado por ejes** —9 tipos · 6 fases · 7 estados del campo— y matriz **mínima** demostrada tipo a tipo, con `orden` **condicional** | `D57` · `D54` | `D57` contó filas de tabla como valores de `fase` y derivó un cartesiano sin demostrarlo; `a.9` da consumos de orden que no mutan nada |

### `D60`–`D61` · las decisiones de la CUARTA comprobación técnica

Comprobación acotada sobre `D58`–`D59`. **Quinto encadenamiento consecutivo**. `D16`–`D59`
conservan su texto.

| | decisión | qué revisa | por qué |
|---|---|---|---|
| `D60` | la cardinalidad de cada fase es **condicional a la ruta y al cierre**, y el contador `iteracion` queda cerrado: empieza en 1, el tercer `conflicto` recibe decisión, y el cuarto es el **marcador de parada** | `D58` | «las cuatro exactamente una vez» era **insatisfacible**: ninguna transacción tiene `confirmada` Y `reconciliada`, y una agotada no tiene `derivada` |
| `D61` | la frontera que exige `tx` es **un fichero frente a varios, y nuevo frente a sustituir contenido**; **`sellado` NO es transaccional** y `retirada-de-cuerpo` sí | `D59` · `D57` | «añadir frente a modificar» era falsa: con ella `sellado`, que sólo añade, no exigiría la `tx` que `D59` le imponía |

### `D62` · la decisión de la QUINTA comprobación técnica

Comprobación de un solo punto sobre `D60`. **Sexto encadenamiento consecutivo.** `D16`–`D61`
conservan su texto.

| | decisión | qué revisa | por qué |
|---|---|---|---|
| `D62` | **observación e intento son dos contadores**: `conflicto` lleva `observacion` 1..4, `intentos_consumidos` 0..3 y `agotado`; `reconciliacion-preparada` lleva `intento` 1..3 y `resuelve`. El tope limita **intentos**, no observaciones | `D60` | un solo campo `iteracion` valía 4 bajo un máximo de 3, y con él seis afirmaciones incompatibles a la vez |

### `D63` · la decisión de la SEXTA comprobación técnica

Comprobación acotada sobre la semántica de sellado y retirada de cuerpo. **Séptimo
encadenamiento consecutivo.** `D16`–`D62` conservan su texto.

| | decisión | qué revisa | por qué |
|---|---|---|---|
| `D63` | la **lápida es excepción tipada** al algoritmo de identidad · **tres niveles** de garantía · **fuente de recuperación** comprobada antes de retirar · el diario **físico no es estrictamente append-only** · sólo una **dependencia semántica viva** bloquea la retirada | `D37` · `D61` | tras retirar, el `id` no se recalcula desde el fichero; la huella no prueba contenido; y «cualquier evento vivo» hacía inalcanzable la propia operación |

**Y `O15`**, resolución posterior del Owner que revisa `O14` sin reescribirlo: la adopción de
PesquerApp es la **primera adopción real, permanente y completa** de ADS. Vive en el registro
de decisiones, y su lectura arquitectónica en §8.2, §18 y §19. **`D58`–`D63` no la tocan**:
sólo corrigen recuentos, cardinalidades, fronteras, contadores y la semántica de sellado.



---

# 16 · Presiones normativas para F5

**Aquí no se redacta ninguna enmienda.** Se enumera exactamente qué presiona qué, y qué queda
bloqueado hasta que el Owner apruebe.

**Las cinco de la entrega anterior se han revisado una a una**, no arrastrado. Cada bloque
declara su `ESTADO TRAS LA DEVOLUCIÓN`, y los identificadores **no se renumeran**: `PN-4`
sigue llamándose `PN-4` aunque esté retirada, porque renumerar rompería la trazabilidad de lo
que ya se llevó al Owner. El resultado son **cuatro vigentes**, una retirada y una fusionada.

## `PN-1` · La sección (g) no existe, y esta fase la escribe

```text
QUÉ PRESIONA        (a) a.9, que delega la disposición física a la sección (g), y a.11,
                    que declara G26/JOURNAL PENDIENTE «hasta diseñar memoria, eventos y
                    recuperación en la sección (g), no ahora por inferencia»
TEXTO VIGENTE       «La disposición física concreta —cuántos ficheros, cómo se fragmentan,
                    transacciones, event log y recuperación— pertenece a la sección (g)»
POR QUÉ NO BASTA    §2 decide exactamente esas cinco cosas. Es materia de (g), y (g) es
UN DERIVADO         normativa del mismo grado que (a) y (b): un derivado no puede
                    autoconcederse la autoridad que su fuente reservó a otra sección
MATERIA MÍNIMA      aprobar §2 como sección (g), o como enmienda que la sustituya
SE PUEDE CONSTRUIR  nada del estado durable. Es el primero del orden de construcción, y
                    está bloqueado hasta esta aprobación
BLOQUEA             §2 · §3 `evento` · §5 cobertura · §7 runtime · §9 nivel Operativo
ESTADO TRAS LA      VIGENTE Y AMPLIADA. §2 decide ahora, además de las cinco materias de
DEVOLUCIÓN          (g), cuatro cosas más que la entrega anterior no cerraba: el escalonado
                    de `fsync` y sus tres puntos obligatorios, la regla de que ADS nunca
                    hace commit con una transacción abierta, la semántica completa del
                    sellado, y el esquema de identidad direccionado por contenido. Sigue
                    siendo LA ÚNICA que bloquea todo el estado durable.
```

## `PN-2` · `O7` crea trabajo por una vía que (b) no contempla

```text
QUÉ PRESIONA        (b) b.15.1 y la regla 2 de la taxonomía de entrada: el trabajo nace de
                    una entrada del Owner o de un desbloqueador DENTRO DEL ALCANCE YA
                    AUTORIZADO. Una política de recurrencia es una TERCERA vía
TEXTO VIGENTE       «ninguna clase de entrada crea trabajo por sí misma salvo las tres que
                    lo declaran» · «DSP crea y despacha dentro del alcance ya autorizado»
POR QUÉ NO BASTA    la taxonomía es derivada y podría ampliarse; b.15.1 no
UN DERIVADO
MATERIA MÍNIMA      reconocer la política de recurrencia aprobada como fuente de trabajo,
                    con su alcance, su presupuesto y su revocación. El Owner YA decidió la
                    sustancia en O7; falta la vía
SE PUEDE CONSTRUIR  todo el sistema de §5 salvo la APERTURA automática: inventario,
                    cobertura, detección y propuesta no crean trabajo y no presionan nada
BLOQUEA             sólo el paso APERTURA de §5.3
ESTADO TRAS LA      VIGENTE, SIN CAMBIO. Ninguna corrección la toca.
DEVOLUCIÓN
```

## `PN-3` · `G03` y la ejecución desatendida

```text
QUÉ PRESIONA        KERNEL.md 1.3.0 G03, constitucional y congelada; a.11 declara qué
                    reglas suyas quedan derogadas, sustituidas o ajustadas
TEXTO VIGENTE       la autonomía temporal no es requisito inicial y no debe introducirse
                    esa complejidad
POR QUÉ NO BASTA    a.11 es la única lista que deroga o ajusta reglas de 1.3.0, y vive en
UN DERIVADO         (a)
MATERIA MÍNIMA      una fila en a.11 que ajuste G03 al alcance exacto que O7 autoriza,
                    conservando el resto
SE PUEDE CONSTRUIR  persistencia, checkpoint, reanudación y vistas: el mapa ya estableció
                    que NO son autonomía temporal
BLOQUEA             lo mismo que PN-2, y por otro camino. Y ADEMÁS, por absorción de PN-5,
                    el nivel COMPLETO de §9: afirma «concurrencia y recuperación
                    demostradas», y la concurrencia real de varios agentes trabajando solos
                    cae bajo G03. Con ello bloquea «instalación terminada y plenamente
                    certificada» de O12
ESTADO TRAS LA      VIGENTE, y ABSORBE a PN-5. La materia mínima es la misma para las dos
DEVOLUCIÓN          —una fila en a.11 que ajuste G03—, y mantenerlas separadas hacía contar
                    dos veces la misma enmienda ante el Owner
```

## `PN-4` · RETIRADA · la `iniciativa` sobre el estado global de (b)

```text
QUÉ PRESIONABA      (b) b.4, que define el estado global como función total sobre los
                    paquetes de UN item. Un lector de b.4 podía leer la iniciativa como un
                    SEGUNDO estado global, y esa lectura había que cerrarla

TEXTO VIGENTE       la función de estado global tiene por dominio los paquetes del item

POR QUÉ SE RETIRA   `D29` cierra la lectura en el propio texto, y por dos vías a la vez:
                      1  el DOMINIO de la función de iniciativa NO son paquetes: es el
                         estado global de sus items, YA CALCULADO POR b.4. La consume, no
                         la redefine ni la extiende
                      2  NO SE PERSISTE. §3.3.2 fija que no se escribe en ningún canónico y
                         vive sólo en el dosier derivado. Sin registro editable no hay
                         segunda verdad que un lector pueda confundir con la de b.4
                      Y su vocabulario es DISTINTO —`abierta-sin-items`, `lista-cierre`—,
                      de modo que ningún estado de iniciativa se parece a uno de b.4

QUÉ SE PIERDE AL    la frase aclaratoria en b.4 que la entrega anterior sugería. F5 PUEDE
RETIRARLA           reinstaurarla si el Owner prefiere que b.4 lo diga con todas las letras
                    en vez de que lo diga (g). El motivo de la retirada queda escrito
                    precisamente para que esa decisión sea SUYA y no una omisión

ESTADO TRAS LA      RETIRADA. Ya se declaraba «MATERIA MÍNIMA: posiblemente ninguna», y la
DEVOLUCIÓN          corrección la convierte en ninguna.
```

## `PN-5` · FUSIONADA en `PN-3` · la certificación Completa frente a `G03`

```text
QUÉ PRESIONABA      el nivel Completo de §9 afirma «concurrencia y recuperación
                    demostradas», y la concurrencia real de varios agentes trabajando solos
                    cae bajo G03

POR QUÉ SE FUSIONA  su MATERIA MÍNIMA es idéntica a la de PN-3 —una fila en a.11 que ajuste
                    G03—, y el propio texto de la entrega anterior ya lo decía: «no es una
                    presión independiente: es su consecuencia». Contarla aparte hacía
                    presentar al Owner dos presiones donde hay una enmienda

DÓNDE VIVE AHORA    en PN-3, como su consecuencia NOMBRADA, con lo que bloquea escrito allí

ESTADO TRAS LA      FUSIONADA. No desaparece: se lee en PN-3.
DEVOLUCIÓN
```

## `PN-6` · NUEVA · la aplicabilidad de la Integrada reinterpreta `O12`

```text
QUÉ PRESIONA        `O12`, resolución del Owner del 2026-08-27: «empezar a programar exige
                    Integrada + baseline aprobado + ningún desconocido crítico sin
                    clasificar. Las tres, no dos»

TEXTO VIGENTE       «la certificación Integrada permite empezar a programar»

QUÉ HA CAMBIADO     `D32` declara que la prueba multi-fuente NO APLICA a productos de 0 y de
                    1 fuente, y que una prueba no aplicable se registra con motivo y
                    evidencia y NO bloquea (§9.5). Sin esa corrección, `C6` `N4` —que admite
                    0..N fuentes— y `O12` juntos bloqueaban para siempre a todo producto de
                    un solo repositorio, que es la mayoría

POR QUÉ NO BASTA    porque cambia QUÉ SIGNIFICA «Integrada» para una clase entera de
UN DERIVADO         productos, y `O12` es una decisión del Owner sobre cuándo se puede
                    empezar a programar. Reinterpretar la precondición de una resolución
                    suya es materia suya, no del autor de F4 — aunque la corrección sea
                    obviamente necesaria, y precisamente por serlo

MATERIA MÍNIMA      confirmar que «Integrada» significa «todas las pruebas APLICABLES
                    superadas, con la inaplicabilidad de las demás registrada con motivo y
                    evidencia», y no «las siete pruebas superadas». Es una frase

SE PUEDE CONSTRUIR  todo §9, incluida la tabla de aplicabilidad: es diseño, y no depende de
                    la confirmación. Lo que depende de ella es DECLARAR Integrada a un
                    producto de 0 o 1 fuente

BLOQUEA             sólo esa declaración, y con ella el arranque de programación de un
                    producto de un solo repositorio
```

## `PN-7` · NUEVA · `b.14` paso 2 dice «completar o revertir»

```text
QUÉ PRESIONA        (b) b.14, paso 2: «¿hay transiciones multiarchivo incompletas? →
                    completar o REVERTIR (a.9)»
TEXTO VIGENTE       el de arriba, literal
QUÉ HA CAMBIADO     §2.6 elige ROLL-FORWARD ONLY y retira el ramal de reversión por
                    completo. §2.6.2 lo argumenta: deshacer exigiría conservar el contenido
                    anterior y duplicaría el estado
POR QUÉ NO BASTA    la disyunción de `a.9` —«terminarla O revertirla»— admite elegir una de
UN DERIVADO         las dos, y la elección es buena. Pero `b.14` ENUMERA las dos, y §7.4
                    afirmaba conservar sus siete pasos enteros mientras cambiaba uno
MATERIA MÍNIMA      una frase en b.14: «completar, o marcar conflicto y escalar»
SE PUEDE CONSTRUIR  todo §2.6. La desviación está declarada en §7.4 y no espera a nadie
BLOQUEA             nada que no bloquee ya PN-1. Es coherencia, no capacidad
ORIGEN              hallazgo `N-9` de la segunda devolución independiente
```

## `PN-8` · NUEVA · `VER` no está en la ruta `AUD` de `b.16`

```text
QUÉ PRESIONA        (b) b.16, fila AUD: obligatorias = INV. `VER` no figura, ni siquiera
                    como condicional
TEXTO VIGENTE       «AUD auditoría de proyecto existente | derivado del encargo | INV |
                    DOM C-DOM · SEG C-SEG · DIS/Reconstrucción C-DIS · PRD sólo si…»
QUÉ HA CAMBIADO     §5.3 declara «VERIFICACIÓN · `VER` independiente», y las tres celdas de
                    §5.6 citan un DICTAMEN de `VER` como evidencia. **Ninguna ruta de b.16
                    produce ese dictamen en una auditoría**
POR QUÉ NO BASTA    b.16 es (b), y la ruta AUD está aprobada con `INV` como única obligatoria
UN DERIVADO
MATERIA MÍNIMA      o bien añadir `VER` como condicional de `AUD`, o bien que F4 deje de
                    exigir dictamen de `VER` en la celda auditada y NOMBRE otro productor.
                    Son dos salidas, y elegir es del Owner
SE PUEDE CONSTRUIR  el inventario, la cobertura, la detección y la propuesta. Lo que espera
                    es que una celda alcance `verificado` CON EVIDENCIA
BLOQUEA             exactamente eso
ORIGEN              hallazgo `N-11` de la segunda devolución independiente
```

## `PN-9` · NUEVA · las obligaciones de iniciativa y los predicados de `b.3`

```text
QUÉ PRESIONA        (b) b.3, cuyas definiciones de `obligación_satisfecha` y
                    `obligación_retirada` se apoyan en CAPA VIGENTE y RECOMPOSICIÓN
                    APROBADA — objetos que una iniciativa no tiene
TEXTO VIGENTE       «obligación_satisfecha(o) ≡ existe una CAPA VIGENTE que produce el
                    resultado exigido…» · «obligación_retirada(o) ≡ una RECOMPOSICIÓN
                    APROBADA declara que la obligación dejó de ser necesaria…»
QUÉ HA CAMBIADO     §3.3.0 define los dos predicados A NIVEL DE INICIATIVA, consumiendo b.3
                    sin redefinirla: la iniciativa CITA capas de sus items en vez de
                    producirlas, y su retirada es una decisión registrada en vez de una
                    recomposición de ruta
MATERIA MÍNIMA      **probablemente NINGUNA.** Es exactamente la vía por la que `PN-4` se
                    retiró: consumir el resultado de (b) no redefine su dominio. Pero
                    `PN-4` se retiró tras COMPROBARLO, y aquí F5 debe CONFIRMARLO, no darlo
                    por hecho. Se registra para que la confirmación exista
SE PUEDE CONSTRUIR  la iniciativa entera. La función Q0–Q9 ya es computable con §3.3.0
BLOQUEA             nada, salvo que F5 decida que sí toca b.3
ORIGEN              hallazgo `N-6` de la segunda devolución independiente
```

## `PN-10` · NUEVA · `O11` dice «estado durable» de la iniciativa

```text
QUÉ PRESIONA        `O11`, resolución del Owner del 2026-08-27: «`iniciativa`. Tipo o
                    artefacto canónico de coordinación, con identidad, ESTADO DURABLE,
                    alcance, gates y dosier vivo derivado»
QUÉ HA CAMBIADO     §3.3 dice «su estado NO es un campo» y `D29` que «no se persiste en
                    ningún fichero canónico»
LA LECTURA BENIGNA  «estado durable» significa que la iniciativa ES estado durable —frente a
                    vivir en el chat—, no que su ESTADO CALCULADO se persista. Es defendible
                    y probablemente correcta
POR QUÉ SE REGISTRA **por simetría con `PN-6`.** F4c registró PN-6 precisamente porque
IGUAL               reinterpretar la precondición de una resolución del Owner «es materia
                    suya, no del autor de F4 — aunque la corrección sea obviamente
                    necesaria, y precisamente por serlo». La misma vara vale aquí. Un
                    tratamiento asimétrico de las resoluciones del Owner es el defecto
MATERIA MÍNIMA      una frase que fije cuál de las dos lecturas rige
SE PUEDE CONSTRUIR  todo §3.3
BLOQUEA             nada. Es coherencia de método
ORIGEN              hallazgo `N-14` de la segunda devolución independiente
```

**Resumen para el Owner, tras revisar las cinco de la entrega anterior:**

```text
VIGENTES · OCHO
  PN-1   la sección (g). LA ÚNICA QUE BLOQUEA TODO EL ESTADO DURABLE, y ahora decide más
  PN-2   la política de auditoría como tercera vía de creación de trabajo
  PN-3   G03 y la ejecución desatendida. Misma pregunta que PN-2 por otro camino, y
         absorbe lo que era PN-5
  PN-6   qué significa «Integrada» para un producto de 0 o 1 fuente
  PN-7   b.14 paso 2 dice «completar o revertir», y §2.6 sólo completa        NUEVA
  PN-8   VER no está en la ruta AUD, y §5.6 exige su dictamen                 NUEVA
  PN-9   los predicados de obligación de b.3 a nivel de iniciativa. Probablemente
         NINGUNA materia, y F5 debe confirmarlo                               NUEVA
  PN-10  O11 dice «estado durable» y F4 deriva el estado. Simetría con PN-6   NUEVA

RETIRADA · UNA
  PN-4   con su motivo escrito, y reinstaurable por F5 si el Owner lo prefiere

FUSIONADA · UNA
  PN-5   dentro de PN-3, porque su enmienda es la misma

CUATRO SON UNA FRASE       PN-6, PN-7, PN-9 y PN-10. Y tres de ellas se registran
CADA UNA                   PRECISAMENTE PORQUE parecen obvias: PN-6 fijó esa vara, y
                           aplicarla de forma desigual sería el defecto

NO SE RENUMERA NINGUNA. Renumerar rompería la trazabilidad de lo que ya se llevó al Owner.
```

> **Lo que NO es presión normativa, y se dice para que nadie lo lleve al Owner.** El defecto
> de `C7` (§9.5) es material **derivado** de `E2`: su corrección está completamente
> determinada por `E2.6`, no requiere decisión del Owner, y su sitio es F6. Y las cuatro
> extensiones de ficha de §5.2 tampoco lo son: extender una ficha con materia que ya está en
> su alcance es trabajo de F6.

---

# 17 · Migración desde el ADS actual

| pieza actual | qué le pasa |
|---|---|
| (a), (b), `E1`, `E2` | **intactas**. F4 no las toca, y sus presiones están en §16 |
| `K-1` tres capas | **intacta**. §1.2 clasifica ciclo de vida, no conocimiento |
| `C1`–`C7` | **intactos**. `C2` se amplía en F6 |
| quince capacidades, roles, métodos, prompts | **intactos**. Son los RESPONSABLES de los aspectos de §5.2, no los aspectos. `+4` extensiones de ficha: `ENT`, `ARQ`, `PLT` y `SEG` |
| diez procesos de `b.16` | **intactos**. Ningún macrocircuito crea uno nuevo |
| diecinueve esquemas | **+4 de estado**: `iniciativa`, `adaptador`, `cobertura`, `evento`. **+2 de clase**: `nivel-certificacion` y `contrato-de-aspecto`, con el precedente de `nivel-novedad`. `memoria` y `validadores.yaml` se amplían. **Total 25** (§3.8) |
| packs | **intactos**, `+2` piezas en `web-app` (`CAND-022`, `CAND-024`) |
| trece validadores | **intactos**, `+entradas:` por `P-08` |
| `plantillas/CHECKPOINT.md` | **intacta**: `E2.3` ya le dio forma multi-fuente |
| `tooling/workspace.py` | **intacto** |
| `tooling/compile-agents.sh` | **sustituido** por el compilador de §6.2. Hoy no compila |
| `START_HERE.md` rutas A y B | **sustituidas** por §8.1 y §8.2, que son sus versiones con estado y gates |
| `docs/evolucion/` | **temporal**. Se retira tras F6, y no antes: F5 y F6 necesitan su trazabilidad |

**Convivencia sin dos verdades.** Regla de orden: una pieza nueva **no entra hasta que la que
sustituye deja de ser consultada**, y mientras convivan, la vieja se marca como sustituida con
enlace a la nueva — que es `b.3`, capa `sustituida`, aplicado al corpus. Lo que **no** se hace
es mantener las dos vivas y sincronizarlas.

**Rollback.** Cada pieza de F6 entra en su propio release con su huella reanclada; volver
atrás es volver a un release. Es lo que ya se hace, y funciona.

---

# 18 · Orden de construcción para F6

**Grafo de dependencias, no items.** Crear items es F6.

```text
        ┌──────────────────────────────────────────────────────────┐
        │  0 · ENTRADAS DE VALIDADORES  (P-08, §11)                │
        │     independiente · barato · PROTEGE TODO LO DEMÁS       │
        └──────────────────────────────────────────────────────────┘
                    (puede ir en paralelo con todo lo de abajo)

  1 · DISPOSICIÓN FÍSICA DEL ESTADO  §2        ── BLOQUEADA por PN-1 ──
        │   evento con fases de transacción · derivados deterministas
        ├──────────────┬───────────────┬──────────────────┐
        ▼              ▼               ▼                  ▼
  3 · INICIATIVA   4 · CERTIFICACIÓN   6 · SUJETO       7 · RUNTIME
      Y DOSIER §3.3     §9                AUDITABLE          §7
        │              │                  Y COBERTURA        │
        │              │                  §5                 │
        │              │                  │  apertura        │
        │              │                  │  BLOQUEADA       │
        │              │                  │  por PN-2/PN-3   │
        │              │                  │                  │
        └──────────────┴──────────────────┴──────────────────┤
                                                             ▼
                                                    8 · PRIMERA ADOPCIÓN
                                                       REAL  O14 · O15
                                                       PesquerApp
                                                       PERMANENTE, no un
                                                       montaje desechable

  2 · CONTRATO DE ADAPTADOR Y VALIDADOR DE DERIVA  §6
        independiente del estado ── alimenta 4 (nivel Operativo) y 7
        incluye el PUNTERO EN FUENTE de §6.7, que es proyección, no estado

  4b · `nivel-certificacion`  §9.2   esquema de CLASE, no de estado
        NO depende de 1: es norma que viaja con el release, y puede escribirse mientras
        PN-1 espera. Lo que depende de 1 son las CELDAS que lo referencian

  5 · PIEZAS DE PACK  CAND-022 · CAND-024
        independientes de todo. Pueden ir en cualquier momento
```

**Lo que cambia respecto al orden propuesto, y por qué:**

```text
SE AÑADE UN PASO 0    las entradas declaradas de validadores (P-08) no dependen de nada,
                      son baratas y protegen la evidencia de todo lo que se construya
                      después. Construirlas al final significaría producir seis meses de
                      evidencia sin garantía de vigencia
SE CONFIRMA EL RESTO  1 estado · 2 adaptadores · 3 iniciativa · 4 certificación · 5 pack ·
                      6 cobertura · 7 runtime · 8 primera adopción real
EL PASO 8 NO ES UN    `O15`: la adopción de PesquerApp es PERMANENTE y COMPLETA, y su
ENSAYO                control repo nace definitivo. Por eso el paso 8 exige la BASE COMPLETA
                      ACORDADA de los pasos 0 a 7, y no un MVP: lo que se instale allí se
                      queda, y sólo se cambia por migración versionada
2 NO DEPENDE DE 1     el adaptador se compila desde la especialización, no desde el estado.
                      Puede avanzar mientras PN-1 espera aprobación
5 NO DEPENDE DE NADA  y por eso es lo que puede entregarse primero si hace falta demostrar
                      avance mientras F5 resuelve
```

---

# 19 · Límites de esta fase

```text
NADA ESTÁ CONSTRUIDO      ni una línea de kernel, runtime, tooling, esquema, adaptador,
                          plantilla, pack ni validador. F4 no lo autoriza
NADA ESTÁ PROBADO         los doce escenarios de §14, las CUARENTA Y DOS filas de la tabla
                          adversarial de §2.6.7, las NUEVE ventanas `R1`–`R9` de §2.6.9 y
                          los ONCE escenarios negativos de §11.5
                          están ESCRITOS. Ninguno se ha ejecutado. Escribir el contrato de
                          una prueba no es la prueba
LA PRIMERA ADOPCIÓN       la columna de uso real está vacía desde F0, y esta fase no la
REAL SIGUE PENDIENTE      llena. `O15` fija que esa adopción —PesquerApp— será REAL,
                          PERMANENTE y COMPLETA, con su control repo definitivo, y que
                          exige la base completa acordada antes de empezar. **`O15` no la
                          autoriza ni la programa**: dice qué será cuando ocurra
NINGÚN ADAPTADOR EXISTE   y por tanto ninguno está certificado
X1 Y P-05 SIGUEN          ninguna decisión de aquí cruza la línea del blueprint
DEFERIDAS
OCHO PRESIONES            §16, tras DOS devoluciones independientes: PN-4 retirada, PN-5
NORMATIVAS VIGENTES       fusionada en PN-3, y PN-6 a PN-10 nuevas. Sólo PN-1 bloquea todo
                          el estado durable, y F5 es su puerta
F4 NO ESTÁ CERTIFICADA    la escribe quien la propone. DOS críticas independientes y UNA
                          devolución técnica la han devuelto; la segunda emitió veredicto de
                          INSUFICIENCIA, y la técnica encontró TRES BLOQUEANTES MÁS en el
                          texto que las dos correcciones anteriores escribieron. Todo está
                          aplicado, y LO APLICÓ QUIEN LO RECIBIÓ: `F4c` sigue ABIERTA,
                          pendiente de una TERCERA REVISIÓN INDEPENDIENTE, que la devolución
                          técnica NO sustituye
```

**La distancia que queda**, dicha como la dijo el baseline: ADS sigue siendo un corpus
verificado contra sí mismo y **cero veces contra la realidad**. Esta arquitectura dice cómo
cerrar esa distancia. No la cierra.
