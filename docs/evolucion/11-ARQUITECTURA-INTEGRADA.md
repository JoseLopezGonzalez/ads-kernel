# F4 — ARQUITECTURA INTEGRADA

Fase **F4** del [plan](04-PLAN-DE-INVESTIGACION.md) y trabajo **23.5** de la
[directiva](ADS-NEXT-OWNER-BRIEF.md). Un solo sistema, no una colección de subsistemas
unidos por documentación — que es lo que el 23.5 rechaza con esas palabras.

> **Esto es diseño, no construcción.** Nada de lo que sigue está implementado, probado ni
> ejecutado. La distinción entre contrato definido, implementación, prueba ejecutada, prueba
> superada y uso real es la disciplina central de este repositorio, y esta fase produce
> **sólo la primera**.
>
> **F4 no está certificada.** La escribe quien la propone, y el plan exige crítica
> independiente antes de F5. Este documento no es esa crítica y no la sustituye.

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
7. Se añaden **cuatro tipos nuevos** al sistema y ni uno más: `iniciativa`, `adaptador`,
   `cobertura` y `evento`. Todo lo demás se compone con lo que ya existe.

**Qué no se ha decidido, y por qué.**

```text
LA CUARTA CAPA           sigue deferida. Hace falta un proyecto independiente que minar.
EL PILOTO                sigue sin ejecutarse. Nada de aquí está demostrado en un producto.
LAS ENMIENDAS            este diseño presiona material aprobado en cinco puntos. Se enumeran
                         y NO se redactan: eso es F5, y su puerta es el Owner.
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
| estado global de un item y su ruta | `estado/items/<ID>/` | `DSP` | runtime |
| capa depositada por una capacidad | el paquete, en `estado/items/<ID>/paq/` | la capacidad con custodia | esa capacidad |
| prioridad y aparcado | zona de órdenes del tablero | **Owner** | runtime |
| qué pasó y por qué | `estado/eventos/` | nadie lo edita: se emite | runtime |
| agrupación de items con sentido común | `estado/iniciativas/<ID>/` | quien la abre | runtime |
| nivel de calidad de una parte del producto | `estado/cobertura/` | `SIS` el contrato, la capacidad de la dimensión el juicio | runtime |
| combinación de revisiones probada junta | `integration-set` | `ENT` | `ENT` |
| gobierno documental de un documento | bloque `ads:memoria` **dentro** del documento | la capacidad que lo posee | esa capacidad |
| qué lee y escribe cada entorno agentic | `adaptador` en el control repo | `PLT` | `PLT` |
| conocimiento externo vendorizado | manifiesto de vendorizado | `SIS` | `PLT` |
| entradas de cada validador | `validadores.yaml` | `SIS` | `SIS` |
| tableros, dosieres, vistas, índices | **nadie**: se regeneran | — | runtime |

**Regla que cierra la matriz:** una fila con autoridad «nadie» es derivada, y **editarla no es
una escritura canónica**. Una fila con autoridad Owner puede recibir bytes del Owner, y eso
**es una orden**, no una mutación — es `a.9` literal.

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
                └── cobertura (sujeto × dimensión) ──▶ campañas = INICIATIVA §3
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
| **D** | **canónico en ficheros + diario de eventos + manifiesto de transacción + derivados** | **sí** | **sí** | sí | **sí** | excelente | medio |

**Por qué se descarta B.** Rompe `R1`, que no es una preferencia estética: es el requisito que
el Owner puso y que `E2.1` reafirmó al precisar *cuál* repositorio contiene esos ficheros. Un
estado en SQLite obliga a un informe intermedio para leerlo, que es exactamente lo que `R1`
prohíbe. **Se conserva una función para SQLite**: como **índice compilado no canónico** en el
plano operacional, regenerable y no versionado (§2.7). Ahí no gobierna nada y acelera lecturas.

**Por qué se descarta C.** Cumple `R3` de forma elegante y rompe `R1` de la forma más cara:
para saber en qué estado está un paquete habría que reproyectar el log. Además crece sin
límite y convierte cada lectura en un cómputo, lo que choca con §12.

**Por qué no basta A.** Es la disposición candidata que `a.9` ya esbozó, y `a.9` la deja
abierta precisamente por `R3`: *«Git no convierte una secuencia de escrituras en una
transacción: si el proceso muere a mitad, el estado queda parcialmente aplicado»*.

**Decisión: D.** Es A más las dos piezas mínimas que le faltan, y cada una resuelve un
requisito distinto que hoy nadie cubre.

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
│  ├─ tx/<TX-ID>.md          manifiestos de transición EN VUELO. Vacío en reposo
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
DURABLE Y VERSIONADO     todo `estado/`, la especialización, la distribución instalada,
                         los adaptadores y sus proyecciones. Sobrevive a la máquina.

OPERACIONAL Y NO VERSIONADO   `.ads/run/`. Lock, cachés e índices compilados. Se borra
                         entero sin perder nada: se reconstruye desde lo durable. Si
                         borrarlo perdiera algo, ese algo estaba en el sitio equivocado.
```

**El criterio, en una pregunta:** ¿sobrevive esto a `rm -rf` y a un clon nuevo? Si tiene que
sobrevivir, es durable y va a Git. Si no, es operacional. Un dato que no sobreviva y que nadie
pueda recalcular **es un defecto de diseño**, no una categoría.

## 2.5 · Instantáneas frente a eventos, y qué es cada cosa

Las dos, con papeles que no se solapan:

```text
FICHEROS CANÓNICOS   son el ESTADO. Responden «¿cómo está esto ahora?» sin cómputo.
                     Es lo que R1 exige y lo que un humano abre.

EVENTOS              son el CAMBIO. Responden «¿por qué está así, quién lo ordenó, sobre
                     qué base y quién lo aplicó?». Es G26, y es lo que a.11 dejó pendiente.
                     NO se reproyectan para leer el estado: el estado ya está escrito.

MANIFIESTO DE TX     es la INTENCIÓN EN VUELO. Responde «¿quedó algo a medias?».
                     En reposo, `estado/tx/` está VACÍO. Un fichero ahí es una señal.
```

**Ninguno de los tres duplica a los otros**, y por eso conviven sin violar `I5`: el estado no
guarda su historia, la historia no guarda el estado, y el manifiesto no guarda ninguno de los
dos — guarda lo que se iba a hacer.

**Relación con `G26`.** El diario **es** el `JOURNAL` que `a.11` dejó pendiente, y cubre lo
cuatro cosas que allí se enumeran como no cubiertas por los tableros: secuencia de eventos,
contexto transversal de sesión, por qué cambió el estado, y operaciones fallidas y
recuperación tras escritura parcial. Que esto **resuelva** `G26` es una decisión normativa y
está declarada como presión para F5 en §16.

## 2.6 · Atomicidad, escritura parcial y recuperación

El mecanismo que `a.9` deja abierto, cerrado aquí:

```text
UNA TRANSICIÓN MULTIARCHIVO

1  EMITIR EVENTO      se crea `estado/eventos/<EV-ID>.md` con: qué se va a cambiar, quién lo
                      ordenó, sobre qué base (hash de las entradas), quién lo aplica.
                      Crear un fichero nuevo es atómico por `rename`: o existe entero o no
                      existe. NUNCA se reescribe un evento.

2  ABRIR MANIFIESTO   `estado/tx/<TX-ID>.md` declara: el evento, la lista exacta de ficheros
                      a tocar, y el hash previo de cada uno.

3  APLICAR            cada fichero se escribe por `escribir temporal + rename`, en el orden
                      declarado. Un `rename` dentro del mismo sistema de ficheros es atómico:
                      ningún fichero queda a medias, aunque el conjunto sí pueda.

4  CERRAR             el manifiesto se marca aplicado y se borra.

5  REGENERAR          los derivados afectados, con `source_revision` sobre los canónicos.

AL ARRANCAR, y en el paso 2 de `Continúa`:

  · `estado/tx/` vacío            → nada que hacer
  · manifiesto con evento aplicado a todos sus ficheros  → se cierra. Idempotente por id
  · manifiesto con ficheros sin aplicar → se COMPLETA aplicando lo que falta, porque el
                                          evento declara el resultado exacto
  · manifiesto cuyo hash previo ya no casa → NO se aplica. Se marca `tx-conflicto` y se
                                          escala. Nunca se inventa estado (R3, b.14.3)
```

**Idempotencia.** Aplicar un evento dos veces por id es una no-operación: es la misma regla
que `a.9` ya fijó para las órdenes del Owner, extendida a toda transición. Lo que `a.9`
declaraba expresamente **no** cubierto —*«las transiciones multiarchivo producidas por
agentes, paquetes, rutas e integración no están cubiertas por el protocolo del tablero»*—
queda cubierto aquí, y por el mismo mecanismo.

## 2.7 · Concurrencia y locks

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

EL DIARIO                  no necesita lock: un evento es un fichero nuevo con id único.
                           Dos emisores concurrentes no colisionan jamás.
```

**Latido y hora de pared.** El lock lleva hora, y eso es correcto: **no es un artefacto
derivado**. `R4` prohíbe la hora de pared en los derivados, no en el plano operacional. Un
lock cuyo dueño murió se detecta por latido vencido y se reclama registrando el evento.

## 2.8 · Identidad, versionado y migración de esquema

```text
ITEM        <TIPO>-<nnn>            FEA-021         estable, del PRODUCTO (E2.5)
PAQUETE     <ITEM>/<nn>             FEA-021/02
INICIATIVA  INI-<nnn>
EVENTO      EV-<nnnnnn>             monotónico, nunca reutilizado
TX          TX-<nnnnnn>
COBERTURA   <clase>:<ancla>/<ruta>  pantalla:web/checkout
INTEGRACIÓN IS-<nnn>                ya normado por `integration-set`

VERSIÓN DE REGISTRO   cada fichero canónico lleva `v`, que incrementa el ejecutor de
                      mutación. Es la base del CAS y de `based_on`.

VERSIÓN DE ESQUEMA    cada fichero canónico lleva `esquema_estado: N`. Una migración es un
                      item `SIS` con su migrador, su prueba y su rollback, y emite evento.
                      Leer un fichero con esquema mayor que el soportado es un ERROR
                      EXPLÍCITO, nunca una interpretación optimista.
```

## 2.9 · Qué se reconstruye, y desde dónde

**La pregunta honesta no es «¿se puede reconstruir todo?» sino «¿desde dónde, y con qué
garantía?».**

| artefacto | se reconstruye desde | garantía |
|---|---|---|
| tableros, vistas, dosieres, índices | los canónicos | **total y determinista**. `T03` lo comprueba |
| `.ads/run/` entero | los canónicos | total |
| un derivado divergente | los canónicos | total, y `Continúa` paso 2 lo regenera |
| una transición interrumpida | manifiesto de tx + evento | total: se completa o se marca conflicto |
| el estado canónico tras una pérdida | Git | total: es su historia |
| el estado canónico **sin Git** | eventos sellados + eventos posteriores | **parcial y declarada**: sólo desde el último sellado. Antes del primero, no |
| el contenido de otra fuente | su repositorio, por la revisión referenciada | total mientras la fuente exista. ADS **no lo copia** (`R6`) |

**Sellado y compactación.** Al cerrar un item, sus eventos se compactan en un fichero sellado
que incluye el estado final de ese item. Eso acota el crecimiento del diario y **es lo que
hace real la reconstrucción sin Git**: sellado más eventos posteriores. Sin sellado, el diario
crece sin límite y la reconstrucción exige el primer evento de la historia.

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
| **`evento`** | **TIPO NUEVO** | `G26` está declarado PENDIENTE en `a.11` justamente porque no existe. Es el diario de §2 |
| **sujeto auditable** | **REFERENCIA TIPADA, no tipo** | se identifica con `(clase, ancla, ruta)` y se **declara dentro de la celda de cobertura**. Crear un tipo para el sujeto obligaría a un registro paralelo de pantallas, flujos y formularios que nadie mantendría, y a deformar `SOURCES.toml` — que es lo que `CI-1` prohíbe |
| **matriz sujeto × dimensión** | **VISTA DERIVADA** | es la proyección de las celdas de cobertura. Persistirla sería una segunda verdad |
| **finding** | **NO ES UN TIPO** | un finding clasificado **es un item**: la tabla del §20.8 mapea uno a uno sobre los diez procesos de `b.16`. Antes de clasificarse vive en la evidencia del `AUD` que lo produjo |
| **causa raíz** | **CAMPO, no tipo** | agrupa items ya existentes. Es una referencia común, no un sujeto |
| **campaña de corrección** | **ES UNA `iniciativa`** | varios items, un sentido común, un gate de cierre. Exactamente lo que la iniciativa es |
| **excepción aceptada** | **ESTADO DE `cobertura`** | con responsable, motivo y caducidad, que la celda ya necesita |
| **contrato documental** | **COMPOSICIÓN** | `ads:memoria` + `cobertura`. Ver §4 |
| **instalación / certificación** | **COMPOSICIÓN** | `cobertura` con `clase: instalacion` + un `gate` por nivel + `DICTAMEN` como dosier. Ver §9 |
| **política de recurrencia** | **DECISIÓN REGISTRADA** | vive donde viven las decisiones, y sus parámetros como campos de `cobertura` |
| **integración multi-fuente** | **REUTILIZA `integration-set`** | ya existe y ya normado |
| **procedencia de conocimiento externo** | **MANIFIESTO NUEVO, no tipo** | misma clase que `SOURCES.toml`: un lockfile que consume tooling, con su contrato. `K0.11` y `huella.py` ya hacen esto **con el propio kernel**; `CAND-027` lo hace con conocimiento ajeno |
| **entradas de validadores (`P-08`)** | **EXTENSIÓN** | un bloque `entradas:` en `validadores.yaml`, junto al `vigencia:` que ya existe |

**Cuatro tipos nuevos y ni uno más.** El recuento importa: el §26.5 y `3.7` del brief existen
para impedir que un diseño se pague en tipos.

## 3.3 · `iniciativa` — qué declara

```text
id                INI-<nnn>
intencion         la pregunta o el resultado global. UNA, no una lista de tareas
alcance           qué entra
fuera_de_alcance  qué NO entra. Sin esto, una iniciativa crece hasta ser el proyecto
apertura          quién la abrió y por qué señal
items             referencias. NUNCA copia su estado
gate_de_cierre    ref a un gate
riesgos · decisiones · contratos_previstos    referencias
estado            DERIVADO de sus items. Ver abajo
```

**Su estado es derivado, y esto es una decisión.** `b.4` define el estado global como función
total sobre los paquetes de un item. Dar a la iniciativa un estado editable crearía una
segunda verdad sobre lo mismo, que es `I5`. Por tanto:

```text
abierta        tiene items vivos
esperando      todos sus items vivos están esperando algo
bloqueada      todos sus items vivos están bloqueados
lista-cierre   todos sus items están cerrados o cancelados
cerrada        además, su gate de cierre está cumplido
```

Sólo `cerrada` exige un acto: cumplir el gate. Los demás se calculan.

**Umbral de activación.** `CI` reduce las nueve señales del §16 a una, porque las otras ocho
la aproximan: **su cierre no puede explicarse con un solo item**. Un bug, una dependencia
rutinaria o una feature localizada siguen usando item y paquetes.

**Prohibición.** Una iniciativa **no anida** en otra. Anidar convierte el estado derivado en
un cálculo sobre un árbol de profundidad arbitraria, y con él la vista del Owner. Si un
trabajo necesita árbol, es un cambio de dirección y su sitio es `DIR`.

**El dosier es derivado.** Índice y memoria, no copia: `I5` y el §15 del documento de
pendientes coinciden. Se genera desde la iniciativa, sus items, sus decisiones y su evidencia.
Un dosier que alguien mantiene a mano es una segunda verdad que envejece.

## 3.4 · `adaptador` — qué declara

Detallado en §6. Su contrato mínimo:

```text
id · entorno · nivel                soportado | compatible | generico | desconocido
lee                                 qué ficheros del control repo consume
proyecta                            qué ficheros GENERA, y dónde los descubre ese entorno
escribe_permitido                   qué puede modificar, con las excepciones NOMBRADAS
comandos                            qué escribe el Owner y qué activa
capacidades_del_entorno             subagentes · skills · límites de contexto · permisos
degradacion                         qué se pierde y cómo, función por función
prueba_de_humo                      ref al escenario que lo certifica
huella                              de la definición de la que deriva cada proyección
```

## 3.5 · `cobertura` — qué declara

```text
sujeto      clase   componente | modulo | pantalla | flujo | formulario | patron |
                    api | integracion | entidad | migracion | entorno | pipeline |
                    despliegue | documento | agente | skill | adaptador | instalacion
            ancla   el COMPONENTE de C6 del que cuelga, o `transversal`
            ruta    dentro del ancla
dimension   ref a capacidad · la dimensión es la capacidad que la posee (§5.2)
aplicabilidad   obligatoria | condicional | no-aplicable
motivo_no_aplicable   obligatorio cuando `no-aplicable`. El §5.18 lo exige: una evaluación
                      registrada, nunca una ausencia
estado      no-auditado | planificado | en-curso | parcial | findings-abiertos |
            corregido-sin-verificar | verificado | excepcion-aceptada | obsoleto | vencido
ultima_revision_real  no la última edición
revisiones_examinadas  por fuente, el SHA. Es lo que hace la celda contrastable
evidencia · findings   referencias a items
caducidad · triggers   qué la vence y qué la reabre
responsable · verificador
```

**`corregido` y `verificado` son estados distintos**, y ésa es la razón de que la lista sea
larga: fundirlos permitiría cerrar sin verificación independiente, que es `G13`.

## 3.6 · `evento` — qué declara

```text
id            EV-<nnnnnn>
tipo          orden | transicion | integracion | certificacion | migracion | fallo
ordenante · autoridad · ejecutor        los cinco conceptos de a.9, sin confundirlos
base          hash de las entradas sobre las que se decidió
afecta        lista de ficheros canónicos y su versión previa
resultado     qué queda escrito
tx            ref al manifiesto, cuando forma parte de una transición multiarchivo
```

**Un evento nunca se edita.** Corregir un evento se hace emitiendo otro que lo rectifica y lo
enlaza. Es lo que hace que el diario sea una historia y no un estado más.

## 3.7 · Extensiones, sin tipo nuevo

```text
memoria.yaml          + `estado` y + `ultima_verificacion_real`, y su descripción se
                      amplía de «sección del corpus de un equipo» a documento gobernante
                      en general. Ver §4
validadores.yaml      + `entradas:` — resuelve P-08. Ver §11
paquete               ya tiene `lee_fuentes` y `escribe_fuentes` por E2.2, y aloja los
                      source changes por E2.3. No necesita nada más
checkpoint            sin cambios. E2.3 ya le dio forma multi-fuente
```

---

# 4 · Contrato documental

Resuelve `CI-2`, que degradó `H5` de conclusión a candidato.

## 4.1 · Las tres vías, comparadas

| | vía | cubre las doce áreas | duplica campos | coste | riesgo |
|---|---|---|---|---|---|
| 1 | **generalizar `memoria`** | tras añadir seis campos | no | bajo | convierte un tipo con sujeto claro —la memoria de un equipo— en un cajón con dos sujetos |
| 2 | **metadata documental especializada** | sí | **sí**: `capacidad`, `autoridad`, `fichero`, `caducidad` y `se_actualiza_cuando` volverían a declararse | medio | dos tipos que dicen lo mismo sobre el mismo fichero |
| 3 | **composición** `memoria` + `cobertura` | sí | no | bajo | exige que las dos piezas existan, y `cobertura` se construye igualmente por §5 |

**Decisión: vía 3.** Y no por eliminación: porque **un documento gobernante es un sujeto
auditable**, y la lista del Owner lo dice —«documentos» está entre lo que hay que auditar—.
Las dos preguntas que el §5.19 y el §5.23 mezclan son en realidad dos, con dueños distintos:

```text
¿QUIÉN RESPONDE DE ESTE DOCUMENTO Y CUÁNDO SE TOCA?   → `ads:memoria`, dentro del documento
¿ESTO SIGUE SIENDO CIERTO, Y CUÁNDO SE COMPROBÓ?      → `cobertura`, con el documento como
                                                        sujeto y su área como dimensión
```

## 4.2 · Cómo se reparte cada exigencia

| exigencia del §5.19 / §5.23 | dónde vive | ya existe |
|---|---|---|
| fuente canónica | `memoria.fichero` | **sí** |
| autoridad | `memoria.autoridad` | **sí** |
| responsable / capacidad | `memoria.capacidad` | **sí** |
| qué materia cubre | `memoria.contiene` | **sí** |
| triggers de actualización | `memoria.se_actualiza_cuando` | **sí** |
| consumidor operativo | `memoria.se_consulta_en` | **sí** |
| caducidad | `memoria.caducidad` | **sí** |
| `no aplicable` con motivo | `memoria.vacio_significa` **y** `cobertura.motivo_no_aplicable` | **sí** el primero |
| estado del documento | `memoria.estado` | **extensión** |
| última verificación real | `cobertura.ultima_revision_real` | tipo nuevo |
| procedencia: fuentes, entornos y **revisiones examinadas** | `cobertura.revisiones_examinadas` | tipo nuevo |
| evidencia | `cobertura.evidencia` | tipo nuevo |
| gaps y contradicciones | `cobertura.findings` → items | tipo nuevo + existente |
| relaciones con decisiones, items y dosieres | referencias desde ambos | **sí** |
| aplicabilidad obligatoria/condicional/no aplicable | `cobertura.aplicabilidad` | tipo nuevo |

**Cero campos duplicados.** Es la condición que `CI-2` conserva de `H5`, y la que descarta la
vía 2.

## 4.3 · Las doce áreas de `O8`, sin doce ficheros

Las doce áreas son **dimensiones**, y una dimensión no es un fichero:

```text
identidad y dirección de producto · baseline funcional · dominio y glosario ·
arquitectura actual · dirección arquitectónica · tecnologías y entorno de desarrollo ·
dirección de ingeniería · calidad y pruebas · seguridad y riesgos ·
despliegue, entornos y operación · decisiones · dirección de evolución y gaps

COMPACTACIÓN     un documento declara VARIAS áreas en su bloque `memoria.contiene`. En un
                 producto pequeño, tres documentos pueden cubrir las doce.
PROFUNDIDAD      la exige `cobertura.aplicabilidad` por área, derivada de tamaño,
                 naturaleza y riesgo declarados en `PROFILE`.
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
CLASE          qué es, y de ella salen las dimensiones que le aplican
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

## 5.2 · Las dimensiones son las capacidades

`H4` sobrevive a la corrección de `CI-1` en su mitad más útil:

| dimensión | capacidad | qué aporta |
|---|---|---|
| producto y funcionalidad | `PRD` | criterio de éxito y alcance |
| UI, UX, diseño visual, sistema de diseño, responsive, accesibilidad | `DIS` | rúbricas y `05-FIDELIDAD` |
| arquitectura, integraciones, acoplamiento, deuda | `ARQ` | radio de impacto |
| dominio, reglas y datos | `DOM` | invariantes y migraciones |
| seguridad, privacidad, cumplimiento | `SEG` | veto con evidencia |
| pruebas, regresión, evidencia | `VER` | dictamen independiente |
| CI/CD, despliegue, observabilidad, recuperación | `ENT` | entrega observada |
| tecnologías, herramientas, entorno | `PLT` | maquinaria disponible |
| documentación y conformidad ADS | `SIS` | contrato y coherencia |
| uso real | `USO` | comportamiento observado |

**Dos dimensiones sin propietario evidente, y se dicen:** **rendimiento y resiliencia**, que
hoy reparten `ARQ` y `ENT` sin que ninguna lo declare; y **dependencias y cadena de
suministro**, que hoy es el proceso `DEP` y no una dimensión. Asignarlas es materia de F5 o de
una extensión de ficha, y **no se decide aquí por comodidad**.

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
AUDITORÍA           proceso `AUD`, con la capacidad de la dimensión produciendo la capa
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
    alcance          qué clases de sujeto y qué dimensiones
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
                NO deben modificar nada · comprobación de que el árbol quedó limpio
ES              el nivel OPERATIVO de la certificación (§9), y `CAND-012` con un caso
                negativo real detrás: una skill añadida no aparecía hasta reiniciar la
                sesión, y nadie lo sabía
```

## 6.5 · Matriz de soporte

| nivel | qué autoriza a afirmar | qué exige |
|---|---|---|
| **soportado** | el entorno ejecuta ADS con sus garantías | adaptador + prueba de humo **ejecutada** + certificación Integrada |
| **compatible** | hay proyección y funciona lo esencial | adaptador + proyección, sin prueba de humo ejecutada |
| **genérico** | recibe el contrato y las instrucciones universales | ninguna pieza específica. Es `CAND-011`, ya construido en un proyecto real |
| **desconocido** | nada | — |

**Estado hoy, sin adornos:**

```text
Claude Code · Codex     primer OBJETIVO de soporte y certificación.  NO CERTIFICADOS
Cursor · Gemini         compatible o genérico hasta pasar su prueba de humo
cualquier otro          genérico, por el fallback obligatorio
NINGÚN ADAPTADOR EXISTE HOY. O13 fija el objetivo; fijar el objetivo no es alcanzarlo.
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
CAÍDA A MITAD                 manifiesto de tx: completar o marcar conflicto (§2.6)
INCONSISTENCIA IRRESOLUBLE    DSP para y escala. NUNCA inventa estado (b.14.3)
```

## 7.4 · `Continúa`

Los siete pasos de `b.14` se conservan enteros. Lo que esta arquitectura les añade es **qué
mira el paso 2**, que hoy no tiene dónde mirar:

```text
2 VERIFICAR   · ¿existen los artefactos que los paquetes dicen haber producido?
              · ¿hay manifiestos en `estado/tx/`?          → completar o marcar conflicto
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
                  bloquea y verifica cada una. El runtime las ORQUESTA y registra su
                  evidencia en el checkpoint del paquete
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
FASES           N0 crear y publicar control repo y workspace
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
ESCRIBE         control repo entero; las fuentes sólo desde N6
ESTADO          `estado/` nace en N3. La iniciativa de instalación nace en N0
EVIDENCIA       `workspace check` · prueba de humo por adaptador · checkpoint recuperado
GATES           N4 certificación Operativa · N7 = O12
CERTIFICACIÓN   Operativa en N4 · Integrada en N7
ROLLBACK        N0–N2 se deshacen borrando el workspace: no hay producto que dañar
REANUDACIÓN     por checkpoint desde N3; antes, repitiendo el paso, que es barato
CIERRE          N7 superado y el primer item de producto despachable
```

**Lo que cambia respecto a hoy.** `C0` deja de redactar la organización y pasa a
**especializar y verificar** una que la distribución ya trae. Es `O9` y el §4.11 del documento
de pendientes: el agente no crea ADS durante C0.

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
ESCRIBE         NADA en las fuentes hasta A8, y en A8 sólo lo que el Owner autorice
ESTADO          la iniciativa de adopción nace en A0 y es el hilo entre chats
EVIDENCIA       inventario con procedencia · baseline aprobado · mapa de conservación
GATES           A3 baseline aprobado por el Owner · A8 autorización de retirada ·
                A10 = O12
CERTIFICACIÓN   Integrada en A9
ROLLBACK        A0–A7 no tocan el producto: revertir es borrar el control repo.
                A8 exige rollback POR FUENTE y commits revisables por fuente
REANUDACIÓN     por el dosier de la iniciativa más el checkpoint del paquete en curso
CIERRE          A10 superado, y el producto entra en SU macrofase real — que puede ser
                C2, C3 o C4. ADS no finge que empieza de cero
```

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
                M5 retirar del repositorio técnico kernel, packs y organización
                M6 validar y certificar
PARTICIPANTES   PLT · SIS · VER · Owner en M5
DIFERENCIA      lo que la separa de la adopción: aquí **ya hay estado ADS**. No se
CON A           reconstruye una realidad: se TRADUCE una que ya estaba escrita. Los items
                y paquetes en curso tienen que seguir en curso al otro lado
ESTADO          M3 es el paso peligroso: migración de esquema con su migrador y su prueba
EVIDENCIA       equivalencia antes/después de items, paquetes y checkpoints
GATES           M3 no cierra sin equivalencia demostrada · M5 exige autorización del Owner
CERTIFICACIÓN   Integrada en M6
ROLLBACK        M5 es el único destructivo, y va después de M6 en el orden real de
                seguridad: no se retira nada hasta que lo nuevo esté certificado
REANUDACIÓN     por checkpoint. M3 es idempotente por diseño (§2.6)
CIERRE          M6 superado y el producto operando sobre el control repo nuevo
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
                U5 recompilar proyecciones de adaptadores
                U6 certificar
PARTICIPANTES   SIS · PLT · VER · Owner si hay incompatibilidad o retirada
LEE             la distribución nueva y la instalada
ESCRIBE         la distribución instalada y las proyecciones. **No el estado**, salvo
                migración de esquema declarada en U3
EVIDENCIA       la vista comprensible del cambio que el §14.2 del brief pide
GATES           U3 aprobado antes de U4 · U6 certificación
CERTIFICACIÓN   el nivel que tuviera antes, revalidado. Una actualización que baja el
                nivel alcanzado es un fallo, no un resultado
ROLLBACK        volver a la versión anterior con su estado. Por eso U4 emite eventos
REANUDACIÓN     por manifiesto de tx si U4 se interrumpe
CIERRE          U6 superado y la versión instalada es la candidata
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
| **Integrado** | fuentes, herramientas, CI, permisos y adaptadores funcionan en el entorno real | que el runtime despache, concurra y recupere | `workspace check` sobre fuentes reales · comandos del producto · CI ejecutable · trabajo multi-fuente mínimo verificado como conjunto | `PLT` | `VER` independiente, con `SEG` si hay superficie sensible | dosier + salidas |
| **Completo** | runtime, despacho, reanudación, concurrencia, integración y recuperación están demostrados | que el producto sea bueno | los escenarios de §14 ejecutados sobre un producto real | `SIS` | `VER` independiente | dosier + evidencia ejecutada |

**Regla dura:** un nivel **no se declara por argumento ni por haber pasado el anterior**. Es
la disciplina de [`08-EVIDENCIA-MULTIREPO.md`](08-EVIDENCIA-MULTIREPO.md) aplicada a una
instalación.

## 9.2 · Cómo se representa

**No es un tipo nuevo.** Es `cobertura` con `clase: instalacion`, una celda por nivel:

```text
sujeto        instalacion:transversal/<producto>
dimension     el nivel
estado        no-auditado | verificado | vencido | obsoleto
caducidad     qué lo vence
triggers      qué lo INVALIDA
evidencia     el dosier
verificador   quién, y que no participó en la instalación
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

## 11.2 · El mecanismo

```text
1  CADA VALIDADOR DECLARA SUS ENTRADAS
   bloque `entradas:` en `validadores.yaml`, junto al `vigencia:` que ya existe.
   Una entrada es un conjunto de ficheros descrito de forma determinista: rutas,
   extensiones y exclusiones. NO una lista escrita a mano que envejece.

2  LA EVIDENCIA LLEVA LA HUELLA DE SUS ENTRADAS
   `registrar_evidencia.py` la calcula al publicar y la escribe en la cabecera. Es
   determinista y no lleva hora de pared.

3  T158 RECALCULA Y COMPARA
   huella distinta → la evidencia está CADUCADA. Mensaje explícito, y el remedio es
   REGENERAR, nunca editar.

4  LO QUE NO CAMBIA
   · el runner sigue SIN sobrescribir evidencia válida cuando una ejecución falla.
     Esa negativa protege la evidencia buena, y es lo que destapó el defecto
   · publicación atómica
   · determinismo: sin timestamps, rutas temporales ni duraciones
   · T158 sigue exento de comprobarse a sí mismo, y un componente exento NO puede
     declarar vigencia: comprobaría su evidencia contra sí mismo
```

## 11.3 · Coste, y cómo se acota

```text
COSTE       recalcular la huella de las entradas de trece validadores en cada comprobación
ACOTADO POR una huella se calcula leyendo metadatos y contenido de un conjunto acotado, y
            se CACHEA en `.ads/run/cache/` por revisión de Git. En un árbol limpio y sin
            cambios, la comprobación es una lectura de caché
DECLARADO   si el coste resulta inaceptable en el piloto, la alternativa es comprobar
            vigencia sólo en el runner y no en cada invocación suelta. El CONTRATO no
            cambia; cambia cuándo se ejecuta
```

## 11.4 · Pruebas negativas que exige

```text
· una entrada declarada que ya no existe                  → fallo explicativo
· una evidencia con huella de entradas que no casa        → CADUCADA
· un validador sin `entradas:` declaradas                 → fallo: no se puede comprobar
                                                            su vigencia, y eso se dice
· una huella calculada de forma no determinista           → dos ejecuciones difieren
· y las nueve que ya existen para `vigencia`

CADA UNA COMPRUEBA EL DIAGNÓSTICO, no sólo que el proceso terminara con código distinto de
cero. Y una TRAZA se cuenta como NO DETECTADA: un validador que revienta no es un
validador que detecta.
```

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
| caché invalidable por revisión | recomputar análisis vigente | sobrevivir a un cambio de sus entradas |
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
| 3 | **migración desde ADS anterior** | control repo antiguo y fuentes | estado **traducido**, con esquema nuevo | `PLT` · `SIS` | M3 equivalencia, M5 autorización | equivalencia antes/después de items y checkpoints | manifiesto de tx; M3 es idempotente |
| 4 | **actualización de ADS** | distribución candidata e instalada | distribución instalada · proyecciones | `SIS` · `PLT` | U3 plan aprobado, U6 certificación | vista comprensible del cambio | rollback a la versión anterior con su estado |
| 5 | **feature amplia por iniciativa** | componentes afectados y sus fuentes | iniciativa + N items + paquetes | las capacidades con custodia | gate de cierre de la iniciativa | capas, source changes e integration set | dosier derivado + checkpoints |
| 6 | **auditoría recurrente → campaña** | los sujetos de las celdas vencidas | cobertura · items `AUD` · iniciativa campaña | runtime dentro de `O7` · `ENC` clasifica | gate de cada `AUD` + cierre de campaña | dictámenes · findings con causa raíz | la celda y su estado; nada se pierde |
| 7 | **reanudación tras chat agotado** | estado canónico completo | ninguno hasta despachar | runtime | — | el reporte breve de `b.14` paso 5 | es el escenario: `Continúa` |
| 8 | **caída durante escritura** | `estado/tx/` y `estado/eventos/` | se completa o se marca conflicto | runtime | — | evento y manifiesto | §2.6, sin inventar estado |
| 9 | **dos fuentes y cierre** | `frontend` y `backend` | paquetes con source changes · integration set | capacidades con custodia · `ENT` | `gate:convergencia-de-fuentes` | el integration set, con SHA por fuente | checkpoint con `sources:` |
| 10 | **de Claude Code a Codex** | definición canónica del adaptador | proyecciones nuevas · cobertura de instalación | `PLT` | prueba de humo | salida de la prueba en sesión nueva | el estado no se toca: es neutral por diseño |
| 11 | **evidencia caducada** | entradas declaradas del validador | ninguno: se regenera evidencia | el runner | `T158` | la huella que no casa | regenerar, nunca editar |
| 12 | **aprendizaje promovido** | evidencia del item de origen | ledger · item `SIS` en `ads-kernel` | `APR` · `SIS` | `gate:aprendizaje-fundado` | dos ocurrencias o un incidente | el ledger conserva la procedencia |

**Lo que los doce demuestran juntos**: que ningún escenario necesita un almacén nuevo, un
proceso nuevo ni una capa nueva. Los cuatro tipos de §3 aparecen; nada más.

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
| `O14` piloto PesquerApp | §14 escenario 2 | DEFERIDA a F6 |
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
| `C7` gobierno Git | REUTILIZADO |

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

---

# 16 · Presiones normativas para F5

**Aquí no se redacta ninguna enmienda.** Se enumera exactamente qué presiona qué, y qué queda
bloqueado hasta que el Owner apruebe.

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
BLOQUEA             lo mismo que PN-2, y por otro camino
```

## `PN-4` · La `iniciativa` sobre el estado global de (b)

```text
QUÉ PRESIONA        (b) b.4, que define el estado global como función total sobre los
                    paquetes de UN item
TEXTO VIGENTE       la función de estado global tiene por dominio los paquetes del item
POR QUÉ NO BASTA    la iniciativa agrupa VARIOS items. §3.3 lo resuelve haciendo su estado
UN DERIVADO         DERIVADO de los items, precisamente para no tocar b.4
MATERIA MÍNIMA      **posiblemente ninguna.** Si el estado derivado se acepta como vista,
                    b.4 no cambia. Se registra porque un lector de b.4 puede leer la
                    iniciativa como un segundo estado global, y esa lectura hay que
                    cerrarla explícitamente
SE PUEDE CONSTRUIR  la iniciativa entera, con su estado derivado
BLOQUEA             nada, salvo que F5 decida que sí toca b.4
```

## `PN-5` · La certificación Completa exige lo que `G03` limita

```text
QUÉ PRESIONA        el nivel Completo de §9 afirma «concurrencia y recuperación
                    demostradas», y la concurrencia real de varios agentes trabajando
                    solos cae bajo G03
TEXTO VIGENTE       el mismo de PN-3
MATERIA MÍNIMA      la misma de PN-3. No es una presión independiente: es su consecuencia
SE PUEDE CONSTRUIR  los niveles Estructural, Operativo e Integrado
BLOQUEA             sólo el nivel Completo, y con él «instalación terminada y plenamente
                    certificada» de O12
```

**Resumen para el Owner:** de las cinco, **una bloquea de verdad** —`PN-1`, la sección (g)—;
**dos son la misma** —`PN-2` y `PN-3`, y sólo bloquean que el sistema abra auditorías solo—;
`PN-4` probablemente no exija nada; `PN-5` es consecuencia de `PN-3`.

---

# 17 · Migración desde el ADS actual

| pieza actual | qué le pasa |
|---|---|
| (a), (b), `E1`, `E2` | **intactas**. F4 no las toca, y sus presiones están en §16 |
| `K-1` tres capas | **intacta**. §1.2 clasifica ciclo de vida, no conocimiento |
| `C1`–`C7` | **intactos**. `C2` se amplía en F6 |
| quince capacidades, roles, métodos, prompts | **intactos**, y son las dimensiones de §5.2 |
| diez procesos de `b.16` | **intactos**. Ningún macrocircuito crea uno nuevo |
| diecinueve esquemas | **+4**: `iniciativa`, `adaptador`, `cobertura`, `evento`. `memoria` y `validadores.yaml` se amplían |
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
        │   evento · manifiesto de tx · derivados deterministas
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
                                                    8 · PILOTO  O14
                                                       PesquerApp

  2 · CONTRATO DE ADAPTADOR Y VALIDADOR DE DERIVA  §6
        independiente del estado ── alimenta 4 (nivel Operativo) y 7

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
                      6 cobertura · 7 runtime · 8 piloto
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
NADA ESTÁ PROBADO         los doce escenarios de §14 son recorridos arquitectónicos.
                          Ninguno se ha ejecutado
EL PILOTO SIGUE PENDIENTE la columna de uso real está vacía desde F0, y esta fase no la
                          llena
NINGÚN ADAPTADOR EXISTE   y por tanto ninguno está certificado
X1 Y P-05 SIGUEN          ninguna decisión de aquí cruza la línea del blueprint
DEFERIDAS
CINCO PRESIONES           §16. Una bloquea de verdad, y F5 es su puerta
NORMATIVAS
F4 NO ESTÁ CERTIFICADA    la escribe quien la propone. El plan exige crítica independiente
                          por quien no la escribió, y este documento no es esa crítica
```

**La distancia que queda**, dicha como la dijo el baseline: ADS sigue siendo un corpus
verificado contra sí mismo y **cero veces contra la realidad**. Esta arquitectura dice cómo
cerrar esa distancia. No la cierra.
