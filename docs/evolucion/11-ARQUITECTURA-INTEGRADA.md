# F4 — ARQUITECTURA INTEGRADA

Fase **F4** del [plan](04-PLAN-DE-INVESTIGACION.md) y trabajo **23.5** de la
[directiva](ADS-NEXT-OWNER-BRIEF.md). Un solo sistema, no una colección de subsistemas
unidos por documentación — que es lo que el 23.5 rechaza con esas palabras.

> **Esto es diseño, no construcción.** Nada de lo que sigue está implementado, probado ni
> ejecutado. La distinción entre contrato definido, implementación, prueba ejecutada, prueba
> superada y uso real es la disciplina central de este repositorio, y esta fase produce
> **sólo la primera**.
>
> **F4 no está certificada, y este texto ha sido CORREGIDO MUCHAS VECES: exactamente TANTAS
> COMO BLOQUES DE CORRECCIÓN TIENE §15.8, y ésa es la única sede que lo dice.** El recuento
> **se DERIVA de las cabeceras `###` de §15.8** —hoy diecisiete, de `D23`–`D33` a `D107`— y
> **este párrafo NO las enumera**: remite. **Corregido por `I-19`**, que encontró aquí NUEVE
> con una aposición que enumeraba diez. **Y corregido otra vez por `P-03` del documento 22**,
> que encontró DOCE con la enumeración copiada entera y **§15.8 sin bloque para `D96`–`D107`
> —once decisiones vigentes—**: la sede de la que la cifra decía derivarse estaba incompleta
> en dos tandas, luego la cifra no derivaba de nada. Ahora §15.8 tiene su bloque por tanda y
> **abrirlo es parte de escribir la tanda**. Un recuento que se declara derivado se deriva, o
> se retira la afirmación de que deriva; **y una enumeración copiada envejece sola, mientras
> una remisión no**. «Dos veces» era la cifra de hace quince correcciones.
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
> todas es quien las recibió**, luego ninguna prueba nada.
>
> ```text
> TERCERA REVISIÓN      **YA EMITIDA**, por un revisor con contexto limpio que no escribió F4
> INDEPENDIENTE         ni aplicó ninguna corrección: DOS BLOQUEANTES, ocho GRAVES, cinco
>                       MEDIOS y siete MENORES, en 15-TERCERA-REVISION-INDEPENDIENTE-F4C.md.
>                       Veredicto: INSUFICIENTE PARA F5. Correcciones: D64–D68
> GATE FINAL            TRES agentes con contexto limpio —dos revisores y un adjudicador—:
> INDEPENDIENTE         33 hallazgos verificados uno a uno contra su fichero y su línea, en
>                       16-GATE-FINAL-INDEPENDIENTE-F4C.md. Veredicto: INSUFICIENTE PARA F5
> COMPLEMENTO DE        las diecinueve fuentes obligatorias que nadie había abierto, leídas
> COBERTURA · NIVEL 0   íntegras por otros tres agentes: `C5` NO resuelve `B-2`, doce
>                       hallazgos nuevos y el recuento fijado en 44 abiertos / 43 distintos,
>                       en 17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md
> ESTA TANDA            corrección integrada de los 43. Correcciones: D71 en adelante
> ```
>
> **`F4c` sigue ABIERTA**, y el veredicto vigente sigue siendo **INSUFICIENTE PARA F5**: lo
> aplicado aquí lo aplicó quien lo recibió, y eso no certifica nada. La tercera revisión
> **ya no está pendiente**; lo que está pendiente es un juicio independiente sobre ESTA
> tanda.

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
LAS ENMIENDAS            este diseño presiona material aprobado en **los puntos que §16
                         enumera y que sólo §16 cuenta** —el cardinal NO se escribe aquí, por
                         la regla de titulares de abajo—, tras
                         dos devoluciones independientes, una tercera revisión, el gate final
                         con su complemento de cobertura, el GATE DE CIERRE INDEPENDIENTE, el
                         GATE DEFINITIVO INDEPENDIENTE y el GATE INDEPENDIENTE DE
                         CERTIFICACIÓN. **La cifra NO se escribe aquí ni se enumera aquí: se
                         DERIVA del barrido de las cabeceras `## \`PN-` de §16, menos las
                         marcadas RETIRADA o FUSIONADA, y §16 es la ÚNICA sede que la
                         publica.** Este párrafo REMITE a ella y no la copia — **corregido
                         por `P-04` del documento 22**, que encontró aquí el titular CATORCE
                         junto a una cadena que decía derivarlo y terminaba en TRECE
                         omitiendo `PN-16`. Una cadena copiada caduca sola; una remisión no.
                         Se enumeran y NO se redactan: eso es F5, y su puerta es el Owner.
```

### La regla que cierra los titulares caducados, y vale para TODO este documento

**No es una regla nueva: el corpus ya se la había aplicado dos veces en local.** §2.6.6, cuando
`P-09` la pilló, escribió «*y el remate deja de ser un cardinal: «todos ellos», para que añadir
una pieza no vuelva a dejar una cifra caduca detrás*»; y §3.6 escribió «*el recuento se
**deriva** de ella en vez de encabezarla*». **Se extiende aquí a todo titular sobre
enumeración, sin excepción, porque el titular numérico que su propia lista desmiente es el
defecto más repetido del expediente y cada tanda ha vuelto a producirlo — incluida la que
introdujo la FASE 0.**

```text
LA REGLA          **ningún titular, rótulo, remate ni frase introductoria de este documento
                  escribe el CARDINAL de la enumeración que lo sigue o que lo precede.** O
                  REMITE —«las secuencias de abajo», «todos ellos», «las que la enumeración
                  nombra fichero a fichero»— o DERIVA, diciendo de dónde y con qué barrido.
                  **Nunca copia un número junto a la lista que ese número describe**

POR QUÉ           una cifra escrita junto a su enumeración **caduca en silencio**: quien añade
                  el elemento no está obligado a pasar por la frase que lo cuenta, y el
                  documento pasa a afirmar dos cosas incompatibles a dos líneas de distancia.
                  Una remisión no caduca nunca; una derivación se mueve sola con su fuente

QUÉ SÍ PUEDE      · un cardinal cuya enumeración NO está al lado y que se publica **con el
LLEVAR CARDINAL     comando que lo deriva**, en la sede única que lo publica —así está §16—
                  · un cardinal que **una comprobación de la batería contrasta** contra la
                    enumeración y contra sus otras sedes, y que da ROJO si alguna regresa —así
                    están las extensiones de ficha de §5.2, §16 y §17, por `G-10`—. Lo que la
                    regla persigue no es el número: es el número **que nadie está obligado a
                    volver a mirar**
                  · un cardinal **HISTÓRICO** dentro de una nota de corrección: es registro de
                    lo que se vio entonces, va marcado, y **no se reescribe**
                  · un cardinal que es parte del CONTENIDO normado y no un recuento de la
                    lista —«más de dos items `SIS` consecutivos» es el umbral de `a.7`, no un
                    titular sobre una enumeración

CÓMO SE COMPRUEBA **contrato de prueba para F6, y NO se ha ejecutado**, como todas las de este
                  documento: por cada titular que contenga un cardinal, o la enumeración
                  adyacente tiene exactamente ese número de elementos, o el titular remite.
                  Escribir el contrato de una prueba no es la prueba

QUÉ NO ES         no es «prohibir los números». Es **prohibir que un número y su enumeración
                  vivan en dos sitios que nadie está obligado a sincronizar**
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
| **mapa documental: qué documentos existen, qué área cubre cada uno, quién responde y cuál es su vigencia** | **nadie**: se REGENERA desde los bloques `ads:memoria` y las celdas de `cobertura` de familia documental (§4.3) | — | runtime |
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

> **Dos espacios de nombres colisionados, deshechos por el gate final independiente (`M-8`
> ≡ `A11`, y `F-03`; es `D83`).** El corpus tenía **`R<n>` dos veces** —los ocho requisitos de
> aquí y las nueve ventanas de reconciliación de §2.6.9— y **`N<n>` tres veces**: los catorce
> principios de `C6`, los cinco niveles de `diseno/03-ESCALA-DE-NOVEDAD.md` y las ocho fases
> de instalación de §8.1. Un lector que encontrara `R1` o `N4` no podía saber a cuál se
> refería, y §19 llegó a contar como pendientes nueve ventanas que `D64` ya había retirado.
>
> ```text
> R1–R8    SE QUEDAN aquí. Son los requisitos, y son la referencia más citada del documento
> RC-1–RC-9 las ventanas de reconciliación, RETIRADAS por `D64`. Renombradas para que su
>          mención histórica no colisione con lo vigente
> N1–N14   SE QUEDAN en `C6`. Es un contrato, y esta fase no toca contratos
> N0–N4    SE QUEDAN en la escala de novedad. Es kernel canónico y anterior
> INS-0…INS-7  las fases de instalación de §8.1, RENOMBRADAS. Eran el espacio más nuevo de
>          los tres, y el único que esta fase puede renombrar sin tocar norma ni kernel
> ```
>
> **La prueba es UNA y cubre los dos**: ningún identificador de la forma `<PREFIJO><n>` se
> usa con dos significados distintos en el corpus. F6 la construye una vez.

**LA FAMILIA `X`, QUE EL CENSO DE `D83` NO ALCANZÓ — declarada aquí, y no tapada.** `D83`
censó `R<n>` y `N<n>`. **El prefijo `X` lo usan hoy CUATRO poblaciones de este documento**, y
se nombran para que nadie tenga que descubrirlo:

```text
X1–X8       las INCÓGNITAS de §0. Sin relleno de ceros
X01–X62     las filas de la TABLA ADVERSARIAL de §2.6.7. Con relleno de DOS dígitos
X-A–X-H     las filas adversariales de §2.9. Con guion y letra
X-S1–X-S9   las filas adversariales de la FASE 0, §9.6. Con guion, letra y número
```

**El invariante de `D83` NO está literalmente violado, y eso se dice antes que nada:** `X1` y
`X01` son **cadenas distintas**, el relleno se aplica de forma consistente y no hay ni una
cita ambigua en el documento. **Lo que sí queda, y es lo que se declara:** las dos primeras
poblaciones se separan **sólo por un cero de relleno**, y la prueba que `D83` contrata para F6
—«ningún identificador de la forma `<PREFIJO><n>`…»— **falla o pasa según normalice o no el
relleno**, cosa que su enunciado no fija. **La condición, escrita para que la prueba no dependa
de una interpretación:** *la comparación es entre CADENAS LITERALES, sin normalizar ceros a la
izquierda ni separadores; y ninguna población nueva de prefijo `X` puede introducirse sin
añadir su renglón a la lista de arriba.* Renombrar cualquiera de las cuatro **no se hace aquí**:
`X01`–`X62` y `X-A`–`X-H` son contratos de prueba ya citados por número desde otras sedes, y
moverlos rompería citas vivas por un riesgo que hoy no se ha materializado.

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
│  │  ├─ <EV-ID>.md          SE EMITEN, NO SE EDITAN. Con UNA excepción física
│  │  │                       autorizada: la lápida de `retirada-de-cuerpo` (§2.9)
│  │  ├─ sellados/<seg>.md   compactación de items cerrados
│  │  └─ INDICE.md           DERIVADO
│  ├─ tx/<TX-ID>.abierta    MARCADOR de transacción EN VUELO, con el `tx` y LA LISTA DE
│  │                        RUTAS AFECTADAS (§2.6.8). Vacío en reposo, reconstruible desde
│  │                        el diario, y EXCLUIDO DE GIT: vive en el árbol durable y NO
│  │                        viaja (§2.6.6)
│  ├─ deriva/<ID>.abierta   MARCADOR de `deriva` SIN REPARAR, con el `id` del evento, las
│  │                        RUTAS y los ITEMS que bloquea, y su causa (§2.6.8). Misma
│  │                        naturaleza y misma disciplina que el anterior: OPERACIONAL, por
│  │                        la SEGUNDA excepción de ruta de §2.4, reconstruible desde el
│  │                        diario (§2.9) y EXCLUIDO DE GIT
│  ├─ tableros/<CAP>.md      ÓRDENES (Owner) + COLA (DERIVADO)
│  └─ memoria/…              memoria de capacidad y ledgers
├─ adaptadores/<entorno>/    definición canónica neutral, no la proyección
├─ AGENTS.md · CLAUDE.md · .cursor/…   PROYECCIONES GENERADAS, con huella
└─ .ads/run/                 OPERACIONAL · NO versionado
   ├─ lock                   un solo ejecutor de mutaciones (R5)
   ├─ indice.sqlite          índice compilado, reconstruible, no canónico
   ├─ cache/                 análisis vigente por huella
   └─ quarantine/<TX>/       CUARENTENA TEMPORAL de contenido divergente, cuando el Owner la
                             autoriza para poder abandonar (§2.6.9, **secuencia** `4b`, cuyo desenlace es el 4). LOCAL,
                             ignorada por Git, NO canónica y NO fuente de verdad. Se crea
                             ANTES de restaurar, se verifica por hash, y se elimina SÓLO
                             después del terminal, de su verificación y del commit del
                             incidente
```

## 2.4 · Durable frente a operacional, y qué vive en Git

```text
DURABLE Y VERSIONADO     `estado/` SALVO las DOS excepciones de ruta declaradas abajo, la
                         especialización, la distribución instalada, los adaptadores y sus
                         proyecciones. Sobrevive a la máquina.

OPERACIONAL Y NO VERSIONADO   `.ads/run/` — lock, cachés, índices compilados y la
                         CUARENTENA de `.ads/run/quarantine/<TX>/` (§2.6.9) — Y los
                         marcadores de `estado/tx/` y de `estado/deriva/`, por las DOS
                         excepciones de abajo. Se borra entero sin perder nada: se
                         reconstruye desde lo durable. Si borrarlo perdiera algo, ese algo
                         estaba en el sitio equivocado — y por eso la cuarentena **no se
                         borra hasta después del terminal, de su verificación y del commit
                         del incidente** (§2.6.9), que es cuando deja de haber algo que
                         perder.
```

### Las DOS excepciones de ruta, declaradas — y siguen siendo DOS categorías, no tres

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

CÓMO QUEDA ALINEADO      `.gitignore` del control repo excluye `estado/tx/` **y
                         `estado/deriva/`** · la reconstrucción desde el diario está en §2.9,
                         con una fila para cada uno · un clon nuevo NO contiene marcadores, y
                         si los contiene es evidencia diagnóstica de un defecto del runtime
                         (§2.6.6, garantía 6) · `X27` y `X59` lo comprueban recorriendo la
                         historia entera.
```

### La SEGUNDA excepción de ruta · `estado/deriva/<ID>.abierta`

> **Completada por el gate de cierre independiente (`I-02`, GRAVE; es `D88`).** `D78` creó el
> marcador de `deriva` e invocó «la excepción de ruta de §2.4» — que nombraba **sólo**
> `estado/tx/` y por tanto **no lo cubría**. Por el criterio vigente el marcador viajaba a
> Git, y un caché versionado que nadie regenera con sede declarada **es** una segunda fuente
> de verdad, que es lo que `I5` prohíbe. El defecto era de propagación, no de concepción: se
> completa aquí, con las mismas cinco piezas que sostienen al marcador de transacción.

```text
QUÉ ES                   **OPERACIONAL**, exactamente igual que el marcador de transacción.
                         Su `plano` es `operacional`, y responde «no» a la pregunta de §2.4:
                         no tiene que sobrevivir a un clon nuevo, porque se reconstruye desde
                         el diario por `bloqueado_por_deriva(item)` (§2.6.9).

POR QUÉ ESTÁ BAJO        por el MISMO motivo, y sólo por ése: la regla de lectura de §2.6.8
`estado/` Y NO BAJO      obliga a consultarlo ANTES de leer el estado, y un aviso de «esto no
`.ads/run/`              es fiable» que vive donde el lector no tiene por qué mirar no es un
                         aviso. Es EXCEPCIÓN DE RUTA, no de naturaleza.

CÓMO SE IMPIDE QUE       exclusión explícita en `.gitignore` del control repo, junto a
VIAJE                    `estado/tx/`. `X59` lo comprueba recorriendo la historia entera.

DESDE DÓNDE SE           desde el diario, y §2.9 tiene su fila: los `deriva` que satisfacen
RECONSTRUYE              `bloqueado_por_deriva(item)`. Total y determinista.

QUÉ NO GANA              **ni identidad ni autoridad propias.** No es fuente de verdad de
                         nada: la verdad es el evento `deriva` del diario, y §1.3 no le da
                         fila porque §2.4 lo clasifica — igual que a `estado/tx/`. El paso 4
                         de §3.1 sigue dando COMPONER.
```

**El criterio, en una pregunta:** ¿sobrevive esto a `rm -rf` y a un clon nuevo? Si tiene que
sobrevivir, es durable y va a Git. Si no, es operacional — **y dónde esté colocado no cambia
la respuesta**, que es lo que las dos excepciones de arriba hacen explícito. Un dato que no sobreviva y que nadie
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
| señalar «hay algo en vuelo» | una transacción que satisface **`abierta(tx)`**, el predicado único de §2.6.1 —hay `preparada` durable y no hay ninguno de los DOS terminales—. `estado/tx/<TX-ID>.abierta` la acelera y **lleva el `tx` y las rutas afectadas**, para que la regla de lectura de §2.6.8 sea ejercible sin recorrer el diario. Se reconstruye si se pierde |
| decir si la transición se aplicó | evento con `fase: confirmada` |
| poder cerrarse y desaparecer | **no sobrevive, y es lo correcto**: borrarlo era el defecto. §3.6 dejaba a `evento.tx` apuntando a un artefacto borrado |

**Ninguna propiedad se pierde, y una se retira a propósito.** El estado no guarda su
historia, y la historia no se reescribe nunca — que es lo que hace que el diario sea una
historia y no un estado más.

## 2.6 · El protocolo transaccional

Lo que `a.9` deja expresamente abierto, cerrado aquí de forma **ejecutable**: una
recuperación real tiene que poder llevarse a cabo con los datos que estos registros escriben,
y nada más.

### 2.6.0 · Estado ESTABLE y estado ESPECULATIVO, y qué exige arrancar

> **Añadida por la comprobación adversarial previa al gate (`D69`).** El protocolo hablaba de
> «estado canónico» sin distinguir **lo publicado** de **lo escrito y aún no publicado**, y de
> esa confusión salían dos afirmaciones falsas: que un conjunto parcialmente aplicado era
> consistente porque cada `rename` es atómico, y que revertirlo destruiría trabajo de alguien.
> **Ninguna escritura de una transacción abierta ha sido publicada nunca**, y eso cambia lo
> que se puede hacer con ella.

```text
ESTADO ESTABLE       el ÚLTIMO COMMIT ACEPTADO de la rama canónica del control repo.
                       · es la VERDAD PUBLICABLE y lo único reconstruible desde otro clon
                       · **NUNCA contiene una transacción parcialmente aplicada**
                       · es la REVISIÓN BASE contra la que se clasifica y se restaura

ESTADO ESPECULATIVO  los cambios del worktree producidos DESPUÉS de `preparada` y ANTES del
                     terminal.
                       · pueden ser un CONJUNTO PARCIAL de ficheros completamente
                         reemplazados por `rename`. **Cada fichero está entero; el CONJUNTO
                         no es consistente**, y la atomicidad del `rename` individual no lo
                         hace consistente — decirlo era el defecto
                       · NO son verdad publicada
                       · sólo se recuperan EXACTAMENTE desde el mismo disco mientras no se
                         publiquen
                       · **no pueden entrar en ningún commit ordinario**
                       · y por eso REVERTIRLOS es local y no destruye trabajo de nadie: nadie
                         los ha visto nunca
```

**Qué exige ARRANCAR una transacción.** Las siete, y si falta una **la transacción no
empieza**:

```text
1  WORKTREE LIMPIO              sin cambios sin confirmar en `estado/`. Un worktree sucio
                                hace indistinguible lo especulativo de lo ajeno, y con ello
                                imposible restaurar contra la base
2  `HEAD` CONOCIDO              el commit exacto sobre el que se trabaja, registrado
3  NINGUNA TRANSACCIÓN          por intersección de rutas (§2.6.9). Con solape, no arranca
   ABIERTA INCOMPATIBLE
4  INTENCIÓN CAUSAL YA          el item u orden que la motiva, **commiteada y PUBLICADA**
   PERSISTIDA Y PUBLICADA       antes de tocar nada (§2.6.10). Es lo que permite reiniciar
                                desde otra máquina
5  REVISIÓN BASE DECLARADA      `revision_base` en `preparada`: el `HEAD` del punto 2
6  HASHES PREVIOS DE TODOS      el `hash_previo` por ruta, que ya exigía §2.6.2
   LOS FICHEROS AFECTADOS
7  CAPACIDAD DE RESTAURARLOS    comprobada, no supuesta: las N rutas existen en
   DESDE ESA REVISIÓN           `revision_base` con el hash declarado, o se declaran
                                `ausente`. Sin esto, `abandonada` sería inalcanzable
```

### 2.6.1 · El autómata de fases — cinco fases, dos rutas, dos cierres

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

> **CORREGIDO POR LA TERCERA REVISIÓN INDEPENDIENTE (`B1`, `G2` y `M5`; es `D64`).** El
> autómata de seis fases tenía un **estado alcanzable sin salida**: desde
> `conflicto(observacion: 4, agotado: true)` no existía ninguna transición admisible, el
> marcador no se retiraba nunca, y por la regla de commit de §2.6.6 **el control repo no
> volvía a commitear jamás, para todo el producto**, por un solo conflicto agotado sobre un
> solo fichero. Y la revisión encontró además que la ruta larga resolvía **con tres fases,
> tres contadores y una bandera** el mismo problema que §2.6.11 resuelve con **un evento sin
> fase y una transacción nueva**, sin que F4 demostrara qué capacidad se perdía sin ella.
>
> **La ruta de conflicto se COLAPSA.** No se le añade una salida a un mecanismo
> desproporcionado: se retira el mecanismo y se conserva la capacidad. Qué se retira, y qué
> ocupa su lugar, en §2.6.9.

```text
RUTA NORMAL       preparada ──────────────────────────▶ confirmada ──▶ derivada
                       │                                     ▲
RUTA DE           └──▶ conflicto ─── cesa la divergencia ────┘
CONFLICTO                  │
                           └──── la autoridad abandona ────▶ abandonada

DOS cierres terminales:  `derivada`   la transacción se completó
                         `abandonada` la transacción se cerró SIN completarse
NINGUNA transición sale de un terminal.
```

> **`abierta(tx)` · el predicado, declarado UNA VEZ y aquí.**
>
> **Corregido por el gate final independiente (`A2`, BLOQUEANTE; es `D71`).** Siete sedes
> decidían «si esta transacción sigue abierta» y **ninguna citaba a otra**: unas decían «sin
> evento `derivada`», y tres de ellas añadían que `derivada` es **el único terminal** —que
> `D64` había dejado de ser cierto al hacer `abandonada` terminal—. Una transacción
> `abandonada` satisfacía «sin `derivada`», luego **el marcador nunca se retiraba, la regla de
> lectura de §2.6.8 la seguía declarando en vuelo y la regla de commit de §2.6.10 seguía
> bloqueando el control repo**. El defecto no era la redacción: era que el predicado **no
> tenía sede**.

```text
abierta(tx)  ≡  ∃ `preparada` DURABLE con ese `tx`
                ∧  ¬∃ evento con ese `tx` y `fase` ∈ { `derivada`, `abandonada` }

cerrada(tx)  ≡  ¬abierta(tx) ∧ ∃ `preparada` durable   — y CERRADA ≡ TERMINAL, por los DOS

QUIÉN LO EVALÚA   el VALIDADOR SEMÁNTICO DEL DIARIO (§3.6, capa B): exige recorrer los demás
                  eventos de ese `tx`, luego NO es comprobable por el esquema estructural.
                  `estado/tx/<TX>.abierta` lo ACELERA y no lo define: es un caché
                  reconstruible, y §2.9 declara desde dónde

DÓNDE SE CITA     **NUEVE sedes vigentes, fuera de aquí**, y el censo se DERIVA con un
                  barrido del identificador, no se escribe de memoria:
                    §2.5      la tabla de plegado del manifiesto
                    §2.6.4    el paso 1 de la clasificación
                    §2.6.5    `W8`
                    §2.6.6    la comprobación de integridad post-terminal
                    §2.6.8    el diario como fuente de reconstrucción
                    §2.6.11   la distinción entre `conflicto` y `deriva`
                    §2.9      la fila de reconstrucción del marcador
                    §3.6      la capa B, que es quien lo EVALÚA
                    §7.4      el paso 2 de `Continúa`
                  **Las NUEVE REMITEN aquí. Ninguna lo redeclara.**
                  **Corregido por el gate de cierre (`I-09`; es `D89`).** El censo anterior
                  decía SIETE y nombraba §2.6.4 y §2.6.9 —que no lo citaban— omitiendo §2.6.5
                  y §2.6.11 —que sí—; y su «ninguna lo redeclara» era falso, porque §2.6.4
                  redeclaraba con la formulación retirada. Ahora §2.6.4 remite, §3.6 entra en
                  el censo por ser la capa evaluadora, y §2.6.9 sale porque **no lo cita**:
                  usa el predicado a través de §2.6.4 y de la regla de commit
```

**Las CINCO fases, y qué significa cada una:**

```text
preparada                 INTENCIÓN PREPARADA. Declara a qué resultado exacto va a llegar
                          cada fichero. NO afirma que haya ocurrido nada. Es el PUNTO DE
                          COMPROMISO: una vez es durable, la transacción SE CIERRA por uno de
                          los dos terminales, y **nunca se revierte en silencio**.
                          NO ES TERMINAL.

confirmada                CANÓNICOS COHERENTES. Todos los ficheros declarados alcanzaron su
                          `hash_posterior_esperado`. Desde este registro un lector puede
                          creerse el contenido de esos ficheros —si además respeta la regla
                          de lectura de §2.6.8.
                          NO ES TERMINAL: faltan los derivados.

conflicto                 OBSERVACIÓN DE DIVERGENCIA, ABIERTA Y BLOQUEANTE. Un fichero no
                          casa ni con su `hash_previo` ni con su `hash_posterior_esperado`:
                          alguien de fuera lo tocó (§2.6.4). Registra la copia íntegra de lo
                          divergente, los items, las rutas y la autoridad que debe decidir.
                          **Bloquea el despacho de los items que NOMBRA, y nada más.**
                          NO ES TERMINAL, y **tiene DOS salidas**: si la divergencia cesa, la
                          transacción se completa; si no, la autoridad la abandona. Ver
                          §2.6.9.

abandonada                CIERRE TERMINAL SIN COMPLETAR. La autoridad declara que esta
                          transacción no va a alcanzar su resultado, registra el estado
                          observado de TODAS sus rutas, y **retira el marcador**. No
                          revierte nada: lo aplicado sigue aplicado, y lo divergente sigue
                          divergente. Emite además el evento `deriva` que mantiene
                          bloqueados los items hasta que una transacción de reparación los
                          devuelva a un estado coherente. Ver §2.6.9.

derivada                  CIERRE TERMINAL COMPLETO. Los derivados afectados se regeneraron.
                          Sólo entonces se retira el marcador.
```

**Las transiciones admitidas, y ninguna más:**

| desde | hacia | condición |
|---|---|---|
| — | `preparada` | el resultado se calculó y cada hash posterior es alcanzable desde su previo |
| `preparada` | `confirmada` | los N ficheros casan con su `hash_posterior_esperado` |
| `preparada` | `conflicto` | **algún** fichero es divergente (§2.6.4) |
| `conflicto` | `confirmada` | **la divergencia cesó**: en una pasada posterior los N ficheros vuelven a casar con base o resultado, y el roll-forward los lleva a su `hash_posterior_esperado`. Es la salida que `a.9` ya prevé para su CAS —«reintenta en un ciclo posterior o cuando cese la escritura concurrente»— y que `M5` señaló suprimida |
| `conflicto` | `abandonada` | **la autoridad decide abandonar**, con su decisión durable. Es la salida que `B1` exigía y que no existía |
| `confirmada` | `derivada` | los derivados afectados se regeneraron |

```text
DE UN TERMINAL NO SALE    ninguna, y los terminales son DOS: `derivada` y `abandonada`.
NINGUNA                   Quien lo hace cumplir es el VALIDADOR SEMÁNTICO DEL DIARIO —no el
                          esquema del evento—: rechazar un evento con `tx` de una transacción
                          que ya tiene un terminal exige MIRAR LOS DEMÁS EVENTOS de ese `tx`,
                          y un esquema estructural sólo ve el evento que valida (§3.6).
                          Lo que se descubre DESPUÉS del cierre NO es una fase de esa
                          transacción: es un evento `tipo: deriva`, con identidad propia y
                          sin `fase`. Ver §2.6.11.

Y TAMPOCO SALE            de `confirmada` a `preparada` · de `conflicto` a `derivada` sin
NINGUNA OTRA              pasar por `confirmada` · de `preparada` a `abandonada` sin pasar
                          por `conflicto`, porque sin divergencia observada no hay nada que
                          abandonar: `W3` manda completar.
                          **Ninguna fase salvo un TERMINAL retira el marcador**, y por eso
                          ya no existe ningún estado que lo retenga para siempre.
```

**Qué se retira, y por qué se dice en vez de borrarse.**

```text
`fase: abortada`   RETIRADA, y sustituida por `abandonada`, que NO es la misma cosa.

                   `abortada` se retiró en `D38` con este argumento: «entre el punto de
                   compromiso y el primer fichero, el único resultado es completar (`W3`);
                   antes del punto de compromiso no hay transacción que abortar (`W2`)».
                   **Ese argumento sigue siendo cierto para la ruta normal, y NO cubría el
                   caso de una divergencia externa**, que `D35` introdujo después. `B1` lo
                   señaló: la justificación «fue escrita cuando este estado no existía».

                   `abandonada` NO es un aborto: no revierte nada, no deshace ninguna
                   escritura, registra el estado observado de todas las rutas y deja el
                   bloqueo vivo en un `deriva`. Es un CIERRE, no una marcha atrás.

                   Es `D38`; `D46` la revisó a cinco fases, `D52` a seis, y `D64` la revisa
                   otra vez: son CINCO, y el número sigue sin ser una cuota.

`reconciliacion-   RETIRADAS, con `reconciliada`. Su trabajo —una autoridad decide, se
preparada` y       declara la intención antes de tocar nada, se aplica y se regeneran los
`reconciliada`     derivados— lo hace ahora una TRANSACCIÓN NUEVA de reparación, que es
                   exactamente el mismo par intención/hecho con `preparada`/`confirmada` y
                   sin ninguna maquinaria propia. Es `D64`, y revisa `D35`, `D46` y `D52`
                   sin reescribirlos. Ver la comparación en §2.6.9.

`observacion` ·    `observacion` SE CONSERVA, sin tope: numera cada estado divergente
`intentos_         DISTINTO observado, y ya no compite con ningún contador de intentos.
consumidos` ·      `intentos_consumidos`, `intento` y `agotado` **se retiran**: no había
`intento` ·        intentos automáticos que contar, y su tope era el que producía `B1`.
`agotado`
```

**Regla de lectura del diario, y es la que impide que la historia mienta:** un evento
**nunca** narra en futuro. `preparada` dice «preparada», y una transacción de reparación
tiene la suya, que dice lo mismo de su propio resultado. Ningún lector —humano o máquina— puede leer una intención como un hecho,
porque **la fase está dentro del propio registro** y no en su ausencia.

### 2.6.2 · Qué datos permiten reproducir el resultado

> **Corregido dos veces.** La segunda corrección técnica lo condicionó a la ruta, porque
> `D52` había hecho recuperable la reconciliación con una segunda intención durable. **`D64`
> retira esa segunda intención**: con la ruta de conflicto colapsada, `preparada` vuelve a ser
> **la única entrada que necesita la recuperación**, y lo es en las dos salidas — completar
> hacia delante usa su `hash_posterior_esperado`, y una transacción de reparación tiene su
> propia `preparada`.

El evento `preparada` es **la única entrada que necesita la recuperación**, y lleva **seis
cosas y no menos**:

```text
1  IDENTIDAD DE LA          `tx: TX-<huella>`. La comparten TODOS los eventos de esa
   TRANSACCIÓN              transacción y nadie más. **La cardinalidad es VARIABLE**, y lo
                            único fijo es que comparten `tx` y que TODA transacción con
                            `preparada` durable acaba en EXACTAMENTE UN terminal:
                              · TRES si completa sin conflicto — `preparada`, `confirmada`,
                                `derivada`
                              · `3 + k` si completa tras `k` observaciones de divergencia
                              · `2 + k` si la autoridad la abandona: `preparada`, `k`
                                `conflicto` y `abandonada` (§2.6.4)
                              · y NADA MÁS. Recuperar no añade eventos: una fase de hecho
                                no se duplica, y restaurar un evento perdido devuelve el
                                MISMO evento, no uno nuevo (§2.6.4)
                            **Corregido** por `D64`: la cuenta anterior contaba fases que ya
                            no existen y una ruta agotada que no tenía salida.

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

6  PROCEDENCIA              los CINCO CONCEPTOS de `a.9` **citados como `a.9` los escribe**
                            —propietario del campo · autoridad · ordenante · escritor del
                            comando · ejecutor de mutación—, más `actor_atribuido`, que
                            pertenece a OTRA lista de `a.9`. Qué se persiste como campo y qué
                            se DERIVA está separado en §3.6.
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

**La clasificación se hace contra la INTENCIÓN DURABLE de la transacción**, no contra el
síntoma ni contra la ventana por la que se llegó. Con `D64` esa intención es **UNA**:

```text
INTENCIÓN VIGENTE     `preparada`, y no hay otra. `D52` había añadido una segunda
DE UNA RUTA           —`reconciliacion-preparada`— y `D64` la retira con la ruta larga.
                      Una transacción, una intención, un `hash_posterior_esperado`.

BASE VÁLIDA           `hash_previo`

RESULTADO PERMITIDO   `hash_posterior_esperado`

Y SI HAY QUE LLEGAR   eso NO es esta transacción: es una transacción NUEVA de reparación,
A OTRO RESULTADO      con su propia `preparada` y su propio `hash_posterior_esperado`
                      (§2.6.9). La intención de una transacción no se sustituye a mitad.
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
0  ¿LA TRANSACCIÓN QUE DECLARA ESA RUTA TIENE UN TERMINAL DURABLE —`derivada` o
   `abandonada`—?
     SÍ, `derivada`    → NO HAY FASE POSIBLE. Ninguna transición sale de un terminal (§2.6.1).
          · casa con el resultado que gobernaba  → nada que hacer
          · no casa                              → evento `deriva`, `causa:
                                                   posterior-al-cierre` (§2.6.11) · W12b
     SÍ, `abandonada`  → **ninguna FASE es posible** —el terminal no admite transiciones— pero
          **hay que comprobar que su `deriva` existe** (`D105`, cierra `M-03` y `O-03`):
            · existe un `deriva` con `abandonada_id` = ese `abandonada`
                              → nada que hacer. **NO se emite otro**: el que existe se
                                conserva hasta que la reparación lo resuelve
            · NO existe       → **se COMPLETA, y es idempotente** · `W17`. El `abandonada`
                                durable lleva `estado_observado[]` de TODAS las rutas,
                                `autoridad`, `motivo` y `revision_base`: **el cuerpo del
                                `deriva` es una FUNCIÓN de él**, luego dos arranques
                                construyen el MISMO cuerpo. Se emite, se hacen sus dos
                                `fsync`, se crea su marcador, y **sólo entonces** se retira
                                el marcador de transacción.
                                **DÓNDE VIVE LA IDEMPOTENCIA DE `W17`, dicho sin rodeos**
                                (`R-01`): en **esta guarda de existencia por `abandonada_id`**
                                y en la regla de unicidad de la capa B, **no** en que el `id`
                                del evento coincida. §2.8 RETIRÓ expresamente el razonamiento
                                por contenido —«REEMITIR NO ES IDEMPOTENTE POR `id`»,
                                porque `predecesor` va en el `id` y la recuperación no lo
                                garantiza—, y este párrafo se apoyaba en él para una
                                propiedad que la guarda ya asegura. **Dos arranques no pueden
                                emitir dos `deriva` porque el segundo lo encuentra**, con
                                cualquier `predecesor`
          **Esto sustituye la prohibición anterior**, que decía «no se emite un `deriva` por
          arranque» mientras §3.6 y la capa B exigían que existiera. Las dos cosas no podían
          ser ciertas a la vez, y el resultado era un diario permanentemente inválido por su
          propio validador sin ruta de reparación declarada — que es `O-03`. **La prohibición
          se conserva donde sí valía: no se INVENTAN derivas nuevas por arranque; se COMPLETA
          el que un `abandonada` durable ya exige**

1  ¿EXISTE UNA TRANSACCIÓN QUE SATISFAGA **`abierta(tx)`** —el predicado de §2.6.1, y no
   otro— Y QUE DECLARE ESA RUTA, EN ESTA INSTALACIÓN?
   **Corregido por el gate de cierre (`I-09`; es `D89`)**: decía «`preparada` durable y SIN
   `derivada`», que es la formulación que `D71` retiró y que el paso 0 hacía inocua sólo por
   accidente. Aquí se REMITE, como hacen las demás sedes.
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

#### La cardinalidad de cada fase es CONDICIONAL A LA RUTA, y a cómo cerró

> **Corregida por `D60` y REHECHA por `D64`.** `D58` decía que cuatro fases aparecían
> «exactamente una vez», y eso era insatisfacible por ruta. `D60` lo condicionó a la ruta;
> `D64` colapsa la ruta de conflicto, y con ella desaparecen `reconciliacion-preparada`,
> `reconciliada` y la ruta agotada — que era la que no tenía salida (`B1`).

**Primero, qué determina la ruta y el cierre**, y es observable en el diario:

```text
SIN CONFLICTO   #`conflicto` = 0
CON CONFLICTO   #`conflicto` ≥ 1 — y NO es otra ruta: es la misma, con una observación de
                divergencia por medio
CERRADA         existe un TERMINAL: `derivada` o `abandonada`, y nunca los dos
COMPLETADA      el terminal es `derivada`   · marcador retirado · nada bloqueado
ABANDONADA      el terminal es `abandonada` · marcador retirado · queda un `deriva`
ABIERTA         no hay terminal · el marcador sigue vivo
```

**`derivada` y `abandonada` son MUTUAMENTE EXCLUYENTES.** Ninguna transacción tiene las dos, y
ninguna transacción cerrada tiene cero.

| fase | completada sin conflicto | completada tras conflicto | abandonada |
|---|---|---|---|
| `preparada` | **exactamente 1** | **exactamente 1** | **exactamente 1** |
| `conflicto` | **0** | `k` ≥ 1 observaciones | `k` ≥ 1 observaciones |
| `confirmada` | **exactamente 1** | **exactamente 1** | **0** |
| `abandonada` | **0** | **0** | **exactamente 1** |
| `derivada` | **exactamente 1** | **exactamente 1** | **0** |
| total de eventos | **3** | **3 + k** | **2 + k** |
| marcador | retirado | retirado | **retirado** |
| bloqueo que queda | ninguno | ninguno | un `deriva` sobre los items nombrados |

```text
EL INVARIANTE QUE CIERRA   toda transacción con `preparada` durable acaba en EXACTAMENTE UN
EL ESPACIO DE ESTADOS      terminal, y todo terminal retira el marcador. **No existe ninguna
                           combinación de cardinalidades sin salida**, que es lo que `B1`
                           encontró y `D64` elimina en su raíz.

`k` NO TIENE TOPE          y no lo necesita: cada `conflicto` registra un estado divergente
                           DISTINTO observado, producido por el mundo y no por un reintento
                           del sistema. Volver a observar lo mismo es una NO-OPERACIÓN
                           (§2.8). No hay livelock porque no hay bucle: el sistema bloquea y
                           espera, y la autoridad siempre puede abandonar (§2.6.9).
```

**Qué fases pueden repetirse dentro de un `tx`, y cuáles no:**

```text
EXACTAMENTE UNA VEZ    `preparada`    siempre — el `tx` ES su huella (§2.8)
CUANDO LA RUTA LA      `confirmada`   1 si completó · 0 si se abandonó
TIENE                  `abandonada`   1 si se abandonó · 0 si completó
                       `derivada`     1 si completó · 0 si se abandonó
                       Una SEGUNDA aparición de cualquiera de éstas es un DEFECTO.
                       **`confirmada → confirmada` no existe.**

REPETIBLE, Y           `conflicto`, discriminado por `observacion`, monotónica desde 1 y SIN
DECLARADO COMO TAL     TOPE. Es la ÚNICA fase repetible, y sólo se emite cuando el conjunto
                       de hashes observados CAMBIA.

LA REGLA, EN UNA       una fase de HECHO —`confirmada`, `abandonada`, `derivada`— no se
FRASE                  duplica NUNCA, y su presencia la fija cómo cerró la transacción. Una
                       fase de OBSERVACIÓN se repite si observa algo distinto, y lo declara
                       con su discriminador.
```


### 2.6.5 · Todas las ventanas de caída

Se enumeran las **DIECIOCHO**, y el recuento **se deriva de las filas de la tabla, no se
escribe**: las nueve `RC-1`–`RC-9` de la reconciliación se retiran con la ruta larga (`D64`),
porque el mecanismo que recuperaban ya no existe. Una ventana que no esté en esta tabla es un
defecto de esa tabla — y las devoluciones posteriores han ejercido esa invitación tres veces:
la segunda añadió cinco, la corrección técnica posterior partió `W12` en dos, y el **gate de
cobertura obligó a añadir `W17`**.

> **CORREGIDA la justificación de exhaustividad, y es `D105`.** Este párrafo decía que las
> ventanas eran todas porque «**la única escritura que un abandono produce es un evento del
> diario**». Eso era cierto antes de `D78` y `D88`, y **dejó de serlo sin que nadie lo
> propagara**: el paso E de §2.6.9 produce hoy **dos eventos, un marcador nuevo, la retirada
> de otro y el borrado de la cuarentena**. Cinco efectos, no uno. Sobre esa premisa falsa
> faltaba la ventana entre el `abandonada` durable y el `deriva` durable, que es `M-03`.
> **La justificación se retira y se sustituye por la tabla misma: la exhaustividad la sostiene
> el recorrido del protocolo, no una frase sobre él.**

| # | la caída ocurre… | qué se observa al arrancar | qué se hace |
|---|---|---|---|
| W1 | antes de preparar | nada: ni evento ni marcador | nada que hacer. La transacción no existió |
| W2 | escribiendo el temporal de `preparada` | un temporal huérfano, sin evento | se borra el temporal. La transacción no existió |
| W3 | después de `preparada`, antes de tocar nada | evento `preparada`, todos los ficheros en previo | **se completa**: aplicar del primero al último |
| W4 | tras aplicar unos ficheros y no otros | mezcla de previos y posteriores | **se completa**: aplicar sólo los que casan con previo, en orden |
| W5 | tras aplicar todos, antes de `confirmada` | todos en posterior, sin `confirmada` | se emite `confirmada` y se sigue. No se reescribe nada |
| W6 | justo después de `confirmada` | `confirmada` presente, derivados sin regenerar | se regeneran los derivados y se emite `derivada` |
| W7 | durante la regeneración de derivados | derivados divergentes de su `source_revision` | se regeneran ENTEROS. Un derivado es reemplazable por definición |
| W8 | tras `derivada`, antes de borrar el marcador | transacción CERRADA con marcador abierto | se borra el marcador. Idempotente. **`abierta(tx)` deja de cumplirse** en cuanto es durable cualquiera de los DOS terminales. **Pero la RETIRADA del marcador no es simétrica** (`D105`): tras `derivada` se retira sin más; tras `abandonada` se retira **sólo cuando el `deriva` es DURABLE y su marcador existe** (§2.6.9 paso E), porque hasta entonces retirarlo dejaría el commit desbloqueado y el bloqueo de los items perdido. **Y `W8` cubre los DOS tramos posteriores al `deriva` durable —`[paso 4, paso 5)` y `[paso 5, paso 6)`—**: crea el marcador del `deriva` si falta —reconstruible desde el diario (§2.9), y por eso no lleva `fsync`, que es la fila `X60`— y **sólo entonces** retira el de transacción, todo idempotente. **Si el `deriva` NO es durable todavía, la ventana es `W17`; si no hay `abandonada` durable, es `W11`.** **Corregido por `P-01`**: esta celda mandaba a `W17` todo lo anterior a que «el `deriva` **y su marcador**» fueran durables, y con ello reclamaba para `W17` el tramo `[4, 5)` que la propia fila de `W17` expulsa por su condición de detección. **Las tres sedes dicen ahora lo mismo, y el punto 7 de §2.6.9 es la que manda** |
| W9 | antes del commit de Git | árbol coherente, Git por detrás | se hace el commit LOCAL. Es recuperación: protege el árbol y no publica (§2.6.10) |
| W10 | después del commit, antes del push | commit local sin publicar | **NO se empuja automáticamente.** El push es publicación, no recuperación: pasa a la política de §2.6.10 |
| W11 | en cualquier punto, con la transacción abierta y un fichero VERDADERAMENTE divergente | un fichero que no casa **ni con su `hash_previo` ni con su `hash_posterior_esperado`** (§2.6.4) | **`conflicto`** —y las dos condiciones son necesarias: transacción abierta Y divergencia real—, con la copia íntegra de lo divergente. El predicado `reconciliacion_pendiente` **se deriva** de él (§2.6.9): no hay bandera que escribir. No se completa y no se revierte, y tiene **dos salidas**: si la divergencia cesa se completa hacia delante, y si no, la autoridad **abandona** y el marcador se retira |
| **W12a** | caída de MÁQUINA tras el `rename` de un canónico, sin `fsync` de su directorio, con la transacción **TODAVÍA ABIERTA** —sin `derivada`— | uno o más canónicos revertidos a su hash previo | **NO es `conflicto`.** Casan con la BASE VÁLIDA de su intención vigente, luego son **NO APLICADO** y se **REAPLICAN** en el `orden` declarado, de forma idempotente (§2.6.4) — que es lo mismo que mandan `W3` y `W4` ante el mismo disco. Si `confirmada` ya era durable, **no se emite ninguna fase nueva**: el evento ya existe, se sigue con los derivados y con `derivada`, y **no hay `confirmada → confirmada`** (§2.6.4). Sólo hay `conflicto` si algún fichero no casa **ni con la base ni con el resultado**. **Corregido** (hallazgo `H2`) |
| **W12b** | lo mismo, con la transacción **YA CERRADA** —`derivada` durable— | ídem | **NO es `conflicto`**, y por el paso 0 de §2.6.4: `derivada` es terminal y ninguna transición sale de él. Se emite un evento **`deriva`** con `causa: posterior-al-cierre` (§2.6.11), que referencia la transacción sin reabrirla. Es el fallo silencioso del hallazgo `E`, y el hallazgo `2` corrige a dónde va |
| **W13** | **escribiendo el temporal de `confirmada`** | temporal huérfano, con todos los canónicos ya en posterior | **se emite `confirmada`, y es su PRIMERA emisión durable**: un temporal huérfano NO es un evento, luego `confirmada` no existe todavía (caso A de §2.6.4). NO se descarta la transacción: a diferencia de `W2`, aquí los canónicos YA están aplicados |
| **W14** | **creando el marcador (paso 2)** | `preparada` durable, marcador ausente o vacío | benigno: `W3` lo cubre por resultado. Se recrea el marcador desde el diario (§2.9) |
| **W15** | **el push es rechazado porque el remoto avanzó** | commit local, remoto divergente | evento `fallo`, tope de tres por §7.3, y se escala. **NUNCA `--force`** (§2.6.10) |
| **W16** | **el push se completa parcialmente** | unas referencias publicadas y otras no | evento `fallo` con las referencias nombradas. El estado local no cambia: el push no es una mutación canónica |
| **W17** | **`abandonada` DURABLE y `deriva` AUSENTE o todavía no durable** — el tramo **`[paso 2, paso 4)`** de §2.6.9, y **sólo** ése: si NO hay `abandonada` durable la transacción sigue abierta y es `W11`, que cubre `[paso 1, paso 2)`; si el `deriva` YA es durable, con su marcador o el de transacción aún sin resolver, **la cubre `W8`** con §2.9 y la fila `X60`. **El punto 7 de §2.6.9 reparte exactamente así, y esta fila no afirma nada que aquella sede no escriba.** **Corregido por `P-01` y `P-02`** (`R-04` **no** quedó cerrado con la tanda anterior): esta fila decía «entre el `abandonada` durable y el `deriva` durable» y atribuía al punto 7 un reparto que el punto 7 no hacía, mientras el punto 7 le asignaba `[1, 2)` y dejaba `[4, 5)` sin dueño | terminal `abandonada` presente **sin ningún `deriva` que lo referencie por `abandonada_id`**, y el marcador de transacción **todavía puesto** | **se COMPLETA, y es idempotente** (paso 0 de §2.6.4): el arranque comprueba **si ya existe un `deriva` con ese `abandonada_id` ANTES de emitir**, y ahí vive la idempotencia — no en la igualdad del `id`, que §2.8 retiró como prueba (`R-01`). El cuerpo del `deriva` es una función del `abandonada` durable —que lleva `estado_observado[]` de todas las rutas, `autoridad`, `motivo` y `revision_base`—, luego los dos arranques construyen el mismo cuerpo. Se emite, se hacen sus dos `fsync`, se crea su marcador, y **sólo entonces** se retira el marcador de transacción. **Añadida por `D105`** (`M-03`, `O-03`): el `abandonada` llevaba `fsync` obligatorio y el `deriva` no, el marcador se retiraba antes de que el `deriva` fuera durable, el arranque tenía PROHIBIDO emitirlo y la capa B exigía que existiera. El resultado era un bloqueo perdido en silencio y un diario permanentemente inválido sin ruta de reparación |

**Qué se completa, qué se revierte y qué se escala**, dicho en una frase cada uno:

```text
SE COMPLETA   toda transacción cuyo evento `preparada` es durable y ninguno de sus ficheros
              es divergente. W3 a W9, más W13 y W14. **Y `W17`**, que no completa una
              transacción sino su CIERRE: emite el `deriva` que el `abandonada` durable ya
              exige, de forma idempotente (`D105`).
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
OBLIGATORIO   LA INTENCIÓN — y con `D64` es UNA, no dos:
              (1) el evento `preparada` y SU DIRECTORIO, ANTES de tocar ningún canónico.
                  Una transacción de reparación tiene la suya, con la misma exigencia

              CADA ESCRITURA CANÓNICA:
              (2) cada fichero canónico escrito **Y SU DIRECTORIO**, ANTES de emitir
                  `confirmada` — y en el orden del paso 3 de §2.6.3:
                  `fsync(temporal)` ANTES del `rename`, `fsync(directorio)` DESPUÉS

              LOS DOS CIERRES QUE AFIRMAN ALGO SOBRE EL DISCO:
              (3) el evento `confirmada` y SU DIRECTORIO
              (4) el evento `abandonada` y SU DIRECTORIO — porque es el terminal que decide
                  cerrar, y perderlo dejaría el bloqueo global vivo sin registro de que se
                  decidió cerrarlo

              **Y LA PIEZA QUE CONSERVA EL BLOQUEO** — añadida por `D105`, y era la laguna
              de `M-03`:
              (5) **el evento `deriva` con `causa: abandono-de-transaccion` Y SU DIRECTORIO**,
                  ANTES de retirar el marcador de transacción. Es lo único que conserva el
                  bloqueo de los items cuando la transacción se cierra sin resultado:
                  perderlo deja el commit desbloqueado y los items libres **sin que nadie lo
                  sepa**. El `abandonada` llevaba `fsync` y el `deriva` no, y entre los dos
                  cabía una caída de máquina sin ventana que la cubriera
NO EXIGIDO    los derivados, el marcador de transacción, **el marcador del `deriva`**, el
              evento `derivada` y el evento `conflicto`:
              **todos ellos** se reconstruyen desde lo canónico o desde la comparación de
              hashes, y pagar `fsync` por ellos encarece cada transacción sin comprar ninguna
              garantía. **Corregido por `D64`**: la lista nombraba dos intenciones y dos
              hechos de una ruta que ya no existe.
              **Y corregido por `P-09` del documento 22**: `D105` creó el marcador del
              `deriva` y **no lo clasificó en ninguna de las dos listas de esta sede**, que es
              LA que reparte `fsync`, mientras la lista se cerraba con «los cuatro»,
              enumeración cerrada que dejaba fuera un quinto. Va a NO EXIGIDO **con su razón
              escrita**: §2.9 le da fila propia de reconstrucción —«los eventos `deriva` para
              los que `bloqueado_por_deriva(item)` sigue siendo verdadero — total y
              determinista»— y la fila adversarial `X60` la comprueba. **Y el remate deja de
              ser un cardinal**: «todos ellos», para que añadir una pieza no vuelva a dejar
              una cifra caduca detrás.
              **CRITERIO GENERAL, que es lo que evita la próxima recurrencia:** *toda pieza
              nueva del protocolo entra en UNA de estas dos listas en el mismo acto que la
              crea. No estar en ninguna no es «no exigido»: es una laguna.* Es `M-03` leído
              como regla en vez de como incidente
```

> **Corregido tres veces.** `D64` la devuelve a una sola intención al colapsar la ruta de
> conflicto, y añade `abandonada` porque es el evento que retira el marcador. Antes, la
> corrección técnica posterior la había extendido a `reconciliacion-preparada`, que ya no
> existe.
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

**Todos los puntos OBLIGATORIOS de arriba** —los que la lista enumera, sin cardinal delante—
dependen de que la implementación no tenga defectos. **Ésta es la
comprobación que convierte un fallo silencioso en un fallo detectado**, y sin ella lo demás es
una promesa:

> **Corregida por la devolución técnica previa (hallazgo `5`, GRAVE).** Decía «toda
> transacción cuyo evento terminal sea `confirmada` o `derivada`» —y `confirmada` **no es
> terminal**—, no contemplaba los hashes finales de una reconciliación, y usaba «respaldado
> por Git» como si equivaliera a «el fichero actual es correcto». **No equivale**: un commit
> demuestra qué se guardó, no qué hay hoy en el árbol de trabajo.

```text
QUÉ ES UNA VENTANA   el conjunto de transacciones **cuyo TERMINAL —`derivada` o
DE COMMIT            `abandonada`— NO está incluido todavía en ningún commit de Git**, más
                     las que siguen abiertas. Se delimita por el último commit que registró
                     un árbol sin marcadores abiertos — que por la regla de Git de §2.6.6 es
                     el único que ADS produce.
                     **Corregido por `I-17`**: la definía sólo sobre `derivada`, y una
                     transacción cerrada por `abandonada` no tiene ni tendrá ninguno, luego
                     **nunca salía de la ventana** y la comprobación la recorría
                     indefinidamente. Era otro residuo de partición binaria sobre `derivada`.

QUÉ TRANSACCIONES    TODAS las de la ventana, ABIERTAS Y CERRADAS. Las abiertas, porque su
SE COMPRUEBAN        recuperación depende de ello; las cerradas por `derivada`, porque
                     afirman un resultado que el disco puede haber dejado de sostener. Lo que
                     cambia entre unas y otras no es SI se comprueban, sino DÓNDE se registra
                     el fallo: `conflicto` en las abiertas, `deriva` en las cerradas por
                     `derivada`. Las cerradas por `abandonada` no afirman ningún resultado:
                     su `deriva` ya declara lo observado, y no se vuelve a emitir.

QUÉ HASH SE USA      el `hash_posterior_esperado` de `preparada`, **y no hay otro**: con
                     `D64` una transacción tiene una sola intención. Si el resultado que hay
                     que alcanzar es otro, eso es una transacción NUEVA con su propia
                     `preparada` (§2.6.9), y entonces gobierna la suya

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
                     su evento con **los cinco CAMPOS de procedencia** de §3.6 — no «los
                     cinco conceptos de `a.9`», que incluyen uno derivado.

QUÉ HACE SI NO CASA  DEPENDE DE SI LA TRANSACCIÓN SIGUE ABIERTA, y la distinción es de
                     identidad, no de grado (§2.6.11):

                       TRANSACCIÓN ABIERTA    —`abierta(tx)`, §2.6.1— se CLASIFICA por §2.6.4
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

QUÉ LLEGA A GIT, EN       NADA de `estado/tx/`, **NADA de `estado/deriva/` y NADA de
POSITIVO                  `.ads/run/`, incluida su `quarantine/`**. Declarado en positivo, y
                          lo comprueban `X27` y `X59` recorriendo la historia entera.
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
| `X39` | commit y push de recuperación | dejan evento con **los cinco CAMPOS de procedencia** de §3.6 completos —lo comprobable; el `propietario del campo` se DERIVA de §1.3 y no se persiste—; la ausencia de cualquiera es un fallo del validador, no un silencio |
| `X47` | resolver la **proyección normativa VIGENTE** del enum de `evento.fase` aplicando la cadena de sustituciones `D38 → D46 → D52`, y compararla con §2.6.1 y §3.6 | **coinciden**, y un evento con `fase: abortada` es **rechazado por el esquema estructural**, que para un enum basta. La prueba NO recorre el corpus entero buscando una sola enumeración: los registros de decisión y los documentos de crítica **conservan deliberadamente los enums sustituidos**, y esa historia es lo que hace auditable la cadena. Las excepciones son exactamente ésas, y están declaradas abajo |
| `X48` | aplicar una transacción completa y comparar cada canónico con su `hash_posterior_esperado` | casan **byte a byte**. Ningún mecanismo de detección —marcador, regla de lectura o diario— modifica el contenido canónico |
| `X49` | provocar un conflicto y evaluar `b.4` P0 sobre los items afectados | devuelve `reconciliacion-pendiente` **sin que se haya escrito un byte en ningún `03-integracion.md`** y sin que exista un segundo marcador |
| `X50` | abandonar una transacción de cinco ficheros y repararla con otra | la reparación regenera sus derivados **antes** de su `derivada`, su marcador sobrevive hasta ella, sus canónicos casan con SU `hash_posterior_esperado`, y al cerrar **resuelve el `deriva`** que el abandono emitió |
| `X51` | editar un canónico fuera del protocolo, sin transacción abierta, y arrancar | se declara **deriva no transaccional**, nombrando ruta, hash observado y hash en `HEAD`. NO se completa, NO se revierte y NO se restaura sola |
| `X52` | comparar el censo de pruebas de §9.1, §9.5 y `nivel-certificacion` para cada nivel | los tres conjuntos son **idénticos**. Una diferencia de censo es un fallo |
| `X53` | buscar un `contrato-de-aspecto` de familia `certificacion`, y campos de certificación declarados dos veces | **no existe ninguno**, y ningún campo de certificación tiene dos sedes normativas |
| `X54` | matar la máquina en cada una de las **DIECIOCHO** ventanas de §2.6.5 —`W1`–`W11`, `W12a`, `W12b`, `W13`–`W16` y **`W17`**— con un `conflicto` vivo. **`W17` incluida expresamente** (`P-01`≡`Q-13`): esta fila decía «las diecisiete», que era el censo anterior a `D105`, y dejaba fuera del único escenario que las barre todas justamente la ventana que `D105` creó para cerrar `M-03` y `O-03`. El número no vuelve a caducar solo: `G-26` deriva las filas `W` de la tabla y exige que esta fila las cubra y nombre `W17` | el `conflicto` sobrevive o se reconstruye desde el diario, **ningún canónico se toca**, y la transacción sigue teniendo sus DOS salidas disponibles tras el arranque |
| `X55` | abandonar una transacción en conflicto y comprobar el estado resultante | `abandonada` es durable, **el marcador se retira**, el control repo **vuelve a commitear**, y un evento `deriva` con `causa: abandono-de-transaccion` mantiene bloqueados **sólo** los items que nombra |
| `X56` | revertir un canónico de una transacción con `derivada` durable, y arrancar | se emite un evento **`deriva`** con `causa: posterior-al-cierre`. **NO** se emite ninguna fase, la transacción cerrada **no gana ningún evento nuevo con su `tx`**, y nada se restaura solo |
| `X57` | recorrer el diario buscando cualquier evento con `fase` cuya transacción ya tenga `derivada` | **no existe ninguno**, y el **validador semántico del diario** lo rechaza —la comprobación es de `tx`, no de evento aislado (§3.6)—. Ninguna transición sale del terminal |
| `X58` | recorrer el grafo de fases buscando un estado no terminal sin sucesor admisible | **no existe ninguno**: `preparada` sale a dos, `conflicto` sale a dos, `confirmada` sale a uno, y `derivada` y `abandonada` son terminales que **retiran el marcador**. **Y la retención acotada de la secuencia `4b` —desenlace 4, `TODAVÍA BLOQUEADA`— termina por ACTO DE AUTORIDAD del Owner** —cuarentena o declaración de irrecuperable (§2.6.9)—, no por construcción: el grafo no la cierra sola, y decirlo es la corrección de `A9`. Lo que se comprueba aquí es el grafo; que exista autoridad que pueda cerrarla se comprueba en §2.6.9 |
| `X59` | recorrer la historia entera del control repo tras N transacciones y N `deriva` | **ningún commit** contiene un fichero bajo `estado/deriva/` ni bajo `.ads/run/`, incluida `quarantine/`. Es `X27` para la SEGUNDA excepción de ruta de §2.4 |
| `X60` | emitir un `deriva`, borrar a mano `estado/deriva/<ID>.abierta` y arrancar | el arranque lo **reconstruye desde el diario** por `bloqueado_por_deriva(item)` (§2.9), con las mismas rutas e items. Y un lector que aplique §2.6.8 **no recorre `estado/eventos/`**: consulta los dos marcadores. El marcador es un acelerador, igual que el de transacción |
| `X61` | abandonar con cuarentena autorizada, y comprobar su ciclo | `.ads/run/quarantine/<TX>/` existe **antes** de restaurar y su contenido **casa por hash** con lo registrado en el `conflicto`; **sigue existiendo** tras `abandonada` y tras la verificación; y **sólo deja de existir después del commit del incidente**. Ningún commit la contiene. Si `SEG` bloquea la publicación y el Owner acepta la pérdida, el incidente conserva **hash, clasificación, autoridad, motivo y alcance**, y el contenido prohibido **no se publica** |
| `X62` | **adopción hasta `A7` inclusive sobre tres fuentes reales**: recorrer `A0`–`A7` completo y después ejecutar `git status --porcelain` y `git log` en CADA fuente, **incluida la comprobación de que NO se ha escrito ningún puntero de adaptador** | **ni un solo commit, ni un fichero nuevo, ni una línea modificada de ADS en ninguna de las tres** — el inventario, el baseline y la cobertura inicial de `A0`–`A7` son LECTURA, y el estado que producen vive en el control repo. **El puntero de adaptador NO es excepción**: `A8` es el primer tramo que escribe en las fuentes, y un puntero escrito antes es un fallo, no un preparativo. Cubre además, en la misma corrida, la propagación a tres fuentes con `main` protegida —tres PR, un Integration Set y estado `INTEGRACIÓN PARCIAL`— y el caso de fusionar dos de tres, donde el sistema **lo dice** en vez de declarar la actualización cerrada |

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
> **Y la lista de arriba NO es exhaustiva**, corregido por `m6`: `CHECKPOINT-ADS-NEXT.md`
> también cita `abortada` en sus bloques históricos, y lo hará cualquier registro futuro que
> narre esta cadena. La regla no es un censo de ficheros: es que la PROYECCIÓN NORMATIVA
> VIGENTE sea una, y que toda otra aparición esté en texto marcado como histórico.
>
> **La regla, en una frase:** la proyección normativa vigente es UNA; las citas históricas y
> adversariales son MUCHAS, y eliminarlas destruiría la trazabilidad que estos documentos
> existen para dar. `X47` comprueba la primera y declara las segundas.

> **Cuarenta y seis filas físicas y cuarenta y seis identificadores únicos**, comprobado
> por conteo sobre el fichero y no por memoria: la tabla empieza en `X01` y **tiene huecos de
> numeración** —`X24`, `X29`–`X36` y `X40`–`X46`—, de filas retiradas o renumeradas en las
> sucesivas correcciones. `X59`, `X60` y `X61` las añadió la tanda del gate de cierre para
> las tres piezas que `I-01` e `I-02` completaron: la exclusión de Git del segundo marcador,
> su reconstrucción, y el ciclo de la cuarentena operacional. **`X62` la añade esta tanda**,
> por `J-03`: la comprobación propia de §6.7, que estaba reasignada a `X51` —una fila
> existente pero ajena—. `X24` es el único con motivo declarado abajo; los demás son huecos
> y **ninguna referencia del documento apunta a ellos**, corregido por `M2`, que encontró
> `X32`–`X34` y `X42` citados sin existir. **Ninguna fila se repite**. La segunda corrección técnica revisó
> `X05`, `X15`, `X26` y `X28` **en su sitio**, sin añadir ninguna fila y sin retirar ninguna.
>
> **Y dos restos señalados que NO se reproducen, dicho porque corregir lo que no existe sería
> peor que no corregirlo** —es la misma disciplina del hallazgo `11` de la devolución
> técnica previa:
>
> ```text
> «dos filas idénticas X28»      NO REPRODUCIDO. `X28` aparece UNA sola vez en el fichero, y
>                                el conteo da **46 filas de datos con 46 ids distintos** —la
>                                cifra vigente, derivada; cuando esta comprobación se hizo el
>                                conjunto tenía 42 y la cifra no se reancló al crecer:
>                                corregido por `J-07`—. Lo que pudo inducir un recuento de
>                                más es la fila SEPARADORA del Markdown, que no es un
>                                escenario
> «"Un fichero que no existe"    NO REPRODUCIDO. Un barrido literal sobre todo `docs/`
>  dos veces en §2.6.4»          devuelve UNA sola aparición
> ```
>
> **Ninguna se ha ejecutado.** Cuarenta y seis filas escritas es el contrato de lo que F6
> debe demostrar, y **no es su demostración**. Trece son de la segunda devolución
> independiente, siete de la devolución técnica previa (`X47`–`X53`), **cinco de la
> corrección técnica posterior** (`X54`–`X58`), **tres de la corrección del gate de cierre**
> (`X59`–`X61`) y **una de la corrección del gate definitivo** (`X62`). `X24` no existe porque su hallazgo —`D`— se resolvió retirando
> el estado en vez de darle un disparador. **Las nueve ventanas `RC-1`–`RC-9` se retiran con
> la ruta de reconciliación** (`D64`): ya no hay un segundo mecanismo que recuperar.


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

> **Corregida por el gate de cierre independiente (`I-02`; es `D88`).** La norma decía
> «se comprueban DOS cosas: los marcadores de `estado/tx/` y **los eventos `deriva` SIN
> REPARAR del diario**», y con ella **la regla que el lector ejecuta seguía mandando recorrer
> `estado/eventos/` entero** — que es exactamente el coste con el que §2.2 descarta la
> alternativa C, y exactamente lo que `D78` añadió el marcador para evitar. `D78` escribió la
> explicación debajo y no cambió la norma de arriba: el marcador existía y nadie estaba
> obligado a usarlo. **La norma pasa a consultar los DOS marcadores**, y el diario vuelve a
> ser lo que §2.9 dice que es: la fuente de RECONSTRUCCIÓN, no la de lectura ordinaria.

```text
1  ANTES DE LEER EL ESTADO CANÓNICO, se consultan LOS DOS MARCADORES, y **sólo ellos**:
   `estado/tx/` y `estado/deriva/`. Son dos listados de directorio. **NO se recorre
   `estado/eventos/`**: el diario es la fuente de RECONSTRUCCIÓN de los marcadores (§2.9),
   no la que un lector ordinario reproyecta para saber si puede creerse el estado.
2  SI HAY ALGÚN MARCADOR DE `estado/tx/`, la lectura de los ficheros que esa transacción
   declara es **NO FIABLE**, y quien lee DEBE declararlo. No es una recomendación de
   prudencia: una lectura silenciosa de una ventana abierta es un defecto de quien lee.
2bis SI HAY ALGÚN MARCADOR DE `estado/deriva/`, las rutas que NOMBRA son igualmente **NO
   FIABLES**, y por el mismo motivo. **Añadido por `D64`** —al retirar el marcador de
   transacción, un abandono traslada el bloqueo al `deriva`— y **hecho ejercible por `D78` y
   `D88`**: el marcador lleva el `id`, las rutas y los items, luego el paso se resuelve
   leyendo el marcador y no evaluando `bloqueado_por_deriva(item)` sobre el diario entero.
   Cubre también el hueco que ya existía para `deriva` `posterior-al-cierre` y
   `sin-transaccion`, que bloqueaban el despacho sin que ningún lector estuviera obligado a
   mirarlos.
3  LOS DEMÁS FICHEROS se leen con normalidad. Ni una transacción abierta ni un `deriva`
   invalidan el estado entero: invalidan exactamente las rutas que declaran.
4  SI UN MARCADOR FALTA, no se inventa: el arranque lo RECONSTRUYE desde el diario (§2.9),
   y ésa es la única lectura que lo recorre. Un lector que encuentre `estado/` sin haber
   arrancado el runtime lee lo que los marcadores digan, y declara esa condición.
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

EL `deriva` SIN REPARAR  **añadido por el gate final independiente (`A8`, MEDIO; es
TIENE SU PROPIO          `D78`).** El paso `2bis` obliga a TODO lector a mirar los `deriva`
MARCADOR                 sin reparar antes de creerse el estado — y encontrarlos exigía
                         recorrer `estado/eventos/` entero y evaluar
                         `bloqueado_por_deriva(item)` sobre cada uno. **Es exactamente el
                         coste que el párrafo de arriba acaba de rechazar para el marcador de
                         transacción**, y por el mismo `R1`. La regla era ejercible por el
                         runtime y no por un lector humano, luego no era la regla que §2.6.8
                         declara.
                         `estado/deriva/<ID-DEL-DERIVA>.abierta` declara el `id` del evento,
                         **las rutas y los items que bloquea**, y su causa. **Lo crea el paso
                         E de §2.6.9** —en el mismo acto que el evento— y **lo retira la
                         TRANSACCIÓN CERRADA que lo resuelve**, cuando su `derivada` lo
                         referencia en `resuelve_deriva`, con la misma disciplina con la que
                         un terminal retira el marcador de transacción.
                         **No gana identidad ni autoridad propias, y NUNCA es fuente de
                         verdad**: la verdad es el evento `deriva` del diario. Es
                         RECONSTRUIBLE desde él por `bloqueado_por_deriva(item)`, vive fuera
                         de Git por la **SEGUNDA excepción de ruta de §2.4** —que ahora lo
                         nombra—, tiene su fila de reconstrucción en §2.9, su declaración de
                         `.gitignore` y su fila adversarial `X59`, y el paso 4 de §3.1 sigue
                         dando COMPONER. Es un caché legible, **con las mismas cinco piezas
                         de disciplina** que el otro, que es lo que `A8` exigía.

EL DIARIO ES LA FUENTE   el marcador acelera; el diario RECONSTRUYE. Si el marcador falta,
DE RECONSTRUCCIÓN        el evento `preparada` de la transacción declara las mismas rutas, y
                         §2.9 lo dice: las que satisfacen `abierta(tx)` (§2.6.1).

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

### 2.6.9 · `conflicto` — una observación bloqueante con DOS salidas

> **Sección REESCRITA por la tercera revisión independiente (`B1`, `G2`, `M5`; es `D64`).**
> Lo que había aquí —`reconciliacion-preparada`, `reconciliada`, tres contadores y nueve
> ventanas `RC-1`–`RC-9`— se retira. El texto de `D35`, `D46` y `D52` se conserva en el registro
> de decisiones; lo que sigue es la norma vigente.

#### La comparación de proporcionalidad, hecha y no supuesta

`G2` reclamó una demostración: **qué garantía profesional se pierde** si la divergencia bajo
transacción abierta se trata como la divergencia posterior al cierre. Se hizo, garantía a
garantía, y **no se pierde ninguna**:

| garantía que la ruta larga daba | ¿la conserva la ruta corta? | cómo |
|---|---|---|
| nada se sobrescribe sin decisión | **sí** | `conflicto` no toca ningún fichero divergente, y la reparación es una transacción nueva con su propia intención durable |
| se conserva copia íntegra de lo divergente | **sí** | `conflicto` la registra, exactamente igual que antes |
| decide una autoridad NOMBRADA | **sí** | `conflicto` la declara, y `abandonada` registra quién decidió |
| intención durable antes de cualquier escritura | **sí** | el `preparada` de la transacción de reparación, que es el mismo mecanismo |
| decisión por fichero: conservar lo divergente, aplicar lo preparado, o un tercer contenido | **sí** | es el `afecta[]` de esa `preparada`, con `hash_previo` = lo observado |
| orden total de aplicación | **sí** | el `orden` de esa `preparada` |
| derivados regenerados antes de cerrar | **sí** | la `derivada` de esa transacción |
| roll-forward only sobre lo PUBLICADO, sin deshacer | **sí** | ninguna de las dos rutas revierte estado publicado. **`abandonada` sí restaura las escrituras ESPECULATIVAS LOCALES** a `revision_base`, y lo verifica byte a byte (`D69`, §2.6.9): eso no es deshacer historia, es descartar lo que nunca se publicó |
| el bloqueo persiste hasta que se repara | **sí, y mejor acotado** | pasa del marcador —que bloqueaba el commit de TODO el producto— al `deriva`, que bloquea los items que nombra |

**Qué se pierde, dicho en positivo:** tres fases del enum, tres contadores, una bandera, el
campo `resuelve`, nueve ventanas de caída, cinco filas adversariales, una parte sustancial de
las reglas del validador semántico — y el único estado alcanzable sin salida que el autómata
tenía. **Lo que ninguna de esas piezas compraba era una capacidad.**

```text
POR QUÉ LA ASIMETRÍA      la ruta larga se justificaba en que «con la transacción abierta SÍ
NO SE SOSTENÍA            existe una intención durable que declara a qué resultado hay que
                          llegar, luego el resultado es determinista». Pero para los ficheros
                          DIVERGENTES —los únicos que entran en esa ruta— la propia
                          `reconciliacion-preparada` declaraba un `hash_final` que
                          **SUSTITUÍA** al esperado: la intención original se descartaba y una
                          autoridad decidía otra. Eso es exactamente lo que hace la
                          reparación de una `deriva`, con una transacción nueva y cero
                          maquinaria adicional. Es el mismo criterio con el que §2.5 plegó el
                          manifiesto de transacción dentro de `evento`, aplicado ahora con la
                          misma vara.
```

#### LOS TRES MECANISMOS DE REINTENTO, que no son el mismo y ya no comparten contador

> **Corregido por `M5`.** La ruta larga tomaba `MAX_CAS_RETRIES = 3` de `a.9` y **suprimía su
> quinto paso**, que es precisamente una salida. Presentar eso como «el precedente que el
> corpus ya resolvió una vez» invertía lo citado. Cada mecanismo recupera aquí su nombre, su
> contador, su salida y su autoridad, y **ninguno reutiliza el contador de otro**.

```text
A · CAS DEL CANAL DE       DÓNDE   `a.9`, consumo de órdenes del tablero. NO es de §2.6
    ÓRDENES                CUENTA  `MAX_CAS_RETRIES = 3` por ciclo de reconciliación
                           SALIDA  deja las órdenes sin consumir · NO modifica el estado
                                   canónico · registra reconciliación pendiente · deja de
                                   girar · **reintenta en un ciclo posterior o cuando cese
                                   la escritura concurrente**
                           QUIÉN   `DSP`, sin intervención humana
                           NO SE REUTILIZA AQUÍ, y ésta es la corrección de `M5`.

B · RECUPERACIÓN DE UNA    DÓNDE   §2.6.4. Es roll-forward por clasificación de hashes
    TRANSACCIÓN            CUENTA  **NINGÚN CONTADOR.** Es idempotente por hash, no por
    MULTIARCHIVO                   intentos: repetirla no consume presupuesto ni cambia nada
                           SALIDA  converge sola en cuanto los ficheros casan
                           QUIÉN   el runtime, sin autoridad humana
                           No hay livelock que acotar: no hay bucle.

C · RESOLUCIÓN DE UNA      DÓNDE   esta sección. Es la divergencia NO determinista: alguien
    DIVERGENCIA EXTERNA            de fuera tocó un canónico
                           CUENTA  `observacion`, monotónica y **SIN TOPE**. No cuenta
                                   intentos: cuenta ESTADOS DIVERGENTES DISTINTOS
                                   observados, que los produce el mundo y no el sistema
                           SALIDA  DOS: la divergencia cesa y la transacción se completa, o
                                   la autoridad la abandona
                           QUIÉN   el propietario global del item, o el Owner si atraviesa
                                   varios
                           No hay tope porque no hay reintento automático que acotar: el
                           sistema NO gira, bloquea y espera.
```

#### `reconciliacion_pendiente` sigue siendo un PREDICADO DERIVADO

```text
reconciliacion_pendiente(item) ≡
    existe una transacción con evento `conflicto` SIN terminal —ni `derivada` ni
    `abandonada`—, cuyo evento `conflicto` NOMBRA ese item
    O BIEN existe un evento `deriva` SIN reparar que nombra ese item
```

```text
POR QUÉ FUNCIONA        el evento `conflicto` YA CONOCE los items y las rutas afectadas: los
                        declara al emitirse. No hace falta escribir nada en ningún item.

QUÉ CAMBIA CON `D64`    la segunda rama. Antes, agotar el bucle dejaba el predicado
                        verdadero **sin ninguna forma de volverlo falso** (`B1`). Ahora el
                        abandono cierra la transacción —y con ella la primera rama— y traslada
                        el bloqueo a un `deriva`, que **sí tiene forma de cerrarse**: la
                        transacción de reparación.

QUIÉN LO CONSUME        `b.4` P0 y §3.3.1 `Q0`, directamente, sin bandera persistida.

CERO TRANSACCIONES      no se muta ningún item para registrar el bloqueo, y por tanto no hace
RECURSIVAS              falta abrir una transacción para registrar lo que impide abrirlas.
                        Es `D49`, y sigue en pie.
```

#### `conflicto` — qué declara, y qué bloquea EXACTAMENTE

```text
QUÉ REGISTRA           por FICHERO DIVERGENTE: su `hash_observado` y una COPIA ÍNTEGRA de lo
                       divergente en el cuerpo del evento. Sin ella, quien resolviera podría
                       destruir ese contenido sin que quedara constancia.
                       Y además: los ITEMS y las RUTAS afectados, y la AUTORIDAD que debe
                       decidir.

`observacion`          monotónica desde 1, SIN TOPE. Un `conflicto` nuevo se emite **sólo si
                       el conjunto de hashes observados CAMBIA**; volver a observar lo mismo
                       es una NO-OPERACIÓN por la regla de reintento de §2.8. Así el diario
                       no crece por mirar dos veces, y sí registra cada estado distinto por
                       el que pasó el fichero.

QUÉ BLOQUEA            **los items que el evento NOMBRA, y sólo ésos**, más toda regeneración
                       de derivados que dependa de sus canónicos. Ver la contención abajo.

QUIÉN RESUELVE         el PROPIETARIO GLOBAL del item, si el conflicto afecta a uno solo.
                       El OWNER, si atraviesa varios items.
```

#### LAS DOS SALIDAS, completas

**Salida 1 · LA DIVERGENCIA CESA.** No exige decisión de nadie:

```text
CUÁNDO         en una pasada posterior de recuperación, los N ficheros vuelven a casar con su
               `hash_previo` o con su `hash_posterior_esperado` — porque quien los tocó los
               devolvió, o porque su edición coincidía con el resultado esperado.
CÓMO           §2.6.4 los clasifica y completa hacia delante, en el `orden` declarado.
QUÉ SE EMITE   `confirmada`. La transacción sigue por la ruta normal hasta `derivada`.
IDEMPOTENCIA   por hash. Repetir la pasada no cambia nada, y el `conflicto` anterior se
               conserva como lo que fue: la observación de que aquello ocurrió.
QUIÉN          el runtime, sin autoridad humana. Es la salida que `a.9` prevé para su CAS y
               que la ruta larga había suprimido (`M5`).
```

**Salida 2 · LA AUTORIDAD ABANDONA — y abandonar es RESTAURAR, no «cerrar dejando lo
aplicado».**

> **Redefinida por la comprobación adversarial previa al gate (`D69`).** La redacción anterior
> hacía que `abandonada` retirase el marcador **dejando el conjunto parcial en el worktree**,
> y con el marcador retirado ese conjunto era **publicable**. «El item queda bloqueado» no lo
> salvaba: el bloqueo es sobre el despacho, no sobre el commit, y el commit era exactamente
> lo que el marcador impedía. Un conjunto parcial no es consistente porque cada `rename` sea
> atómico. **`abandonada` pasa a exigir la restauración verificada contra la revisión base**,
> y con ello se convierte en la rama **REVERTIR** de `b.14`.

**El procedimiento, y `abandonada` es INALCANZABLE hasta completarlo entero:**

```text
A · CAPTURAR      · conservar, ANTES de tocar nada, la copia ÍNTEGRA de toda divergencia
                    necesaria — el cuerpo del `conflicto` ya la lleva
                  · cuando el worktree tenga que restaurarse encima y el Owner lo haya
                    autorizado, copiar además lo divergente a **`.ads/run/quarantine/<TX>/`**
                    y **verificarlo POR HASH** contra lo registrado en el `conflicto`. La
                    cuarentena es OPERACIONAL y TEMPORAL: su contrato está abajo
                  · registrar rutas, hashes observados, autoridad, causa y `revision_base`
                  · asegurar que esa copia formará parte del INCIDENTE que se publicará
                  · **si no puede conservarse, NO SE PUEDE ABANDONAR**: la transacción
                    permanece abierta (cuarto desenlace, abajo)

B · DETENER       · impedir nuevas escrituras sobre las rutas afectadas
                  · las operaciones no solapadas siguen **sólo si su mecanismo de commit no
                    incorpora por accidente las rutas especulativas**. Con un worktree único
                    eso significa: **no commitean nada mientras haya especulativo vivo**

C · RESTAURAR     · restaurar TODOS los canónicos afectados desde la `revision_base` EXACTA
                  · **incluidos los que ya alcanzaron su `hash_posterior_esperado`**, no sólo
                    los divergentes
                  · es restauración LOCAL de estado ESPECULATIVO: **no revierte nada
                    publicado**, porque nada de esta transacción llegó a publicarse (§2.6.0)
                  · **NUNCA se restaura automáticamente contenido YA PUBLICADO.** Esa
                    prohibición de §2.6.6 sigue entera y no la toca `D69`

D · VERIFICAR     · comparar **BYTE A BYTE** cada fichero restaurado con su contenido en
                    `revision_base`
                  · comprobar que no quedan rutas NUEVAS huérfanas creadas por la transacción
                  · comprobar que el conjunto canónico vuelve a ser el de la base, entero
                  · **si una escritura concurrente impide verificarlo, `abandonada` NO puede
                    emitirse** y la transacción permanece abierta

E · CERRAR        sólo entonces, y **en este orden, que ahora es EXACTO y DURABLE paso a
                  paso** (`D105`):
                  1 · emitir `abandonada`, con la evidencia de la verificación de D.
                      **NO lleva `deriva_emitida`: ese campo queda PROHIBIDO en esta fase**
                  2 · `fsync` del fichero de `abandonada` **y de su directorio**
                  3 · emitir el `deriva` con `causa: abandono-de-transaccion`, que **REFERENCIA
                      UNILATERALMENTE** al `abandonada` por su campo `abandonada_id`, y a la
                      transacción por `tx_afectada`
                  4 · **`fsync` del fichero del `deriva` Y DE SU DIRECTORIO** — obligatorio
                      desde `D105`, y era la laguna de `M-03`
                  5 · **crear su marcador `estado/deriva/<ID>.abierta`** con las rutas y los
                      items que el `deriva` nombra (§2.6.8)
                  6 · **sólo ahora, y no antes, retirar el marcador de transacción de
                      `estado/tx/`.** Mientras el paso 4 no sea durable, el marcador se
                      MANTIENE: es lo que impide que el commit avance dejando el bloqueo
                      perdido

                  **Por qué el `abandonada` ya no nombra a su `deriva`.** Lo nombraba, y era
                  circular: `id(abandonada)` incluía `deriva_emitida` = `id(deriva)`, y
                  `id(deriva)` incluye su `predecesor`, que es el `abandonada`. Ninguna sede
                  lo resolvía, y el segundo terminal del protocolo **no se podía emitir**. Es
                  `M-02`, y lo cierra `D105` invirtiendo la referencia: **el que llega
                  después nombra al que ya existe**
```

**Las tres alternativas, comparadas antes de elegir** (`D105`, cierra `M-02`):

| alternativa | ¿identidad construible? | ¿cadena verificable? | ¿bloqueo persistente? | veredicto |
|---|---|---|---|---|
| **A · `abandonada` conoce el `id` del `deriva`** —lo que había— | **NO.** `id(abandonada)` necesita `id(deriva)`, que necesita `predecesor` = `id(abandonada)`. Circular | sí, por puntero directo | sí | **DESCARTADA.** Es el defecto. Sólo funcionaría emitiendo el `deriva` ANTES, y entonces su `predecesor` no sería el terminal que lo motiva |
| **B · el `deriva` referencia unilateralmente al `abandonada`** | **SÍ.** El `abandonada` se calcula y se hace durable primero; el `deriva` nace después y nombra un `id` que ya existe | sí, **recorriendo** el diario en busca del `deriva` que apunta. Es lo que la capa B ya hace para otras reglas | sí: el bloqueo vive en el `deriva` y en su marcador | **ELEGIDA.** Es la mínima: **no añade ningún evento, ningún tipo y ningún campo al `abandonada`** — sólo mueve una referencia de sitio y le da `fsync` |
| **C · una intención o identidad separada previa** —un tercer evento que reserve el par de ids— | sí | sí | sí | **DESCARTADA.** Crea un evento más en el camino crítico del único desenlace que revierte, y con él una ventana de caída más y una regla de validación más. **Compra lo mismo que B a un coste mayor**, y `D64` ya retiró maquinaria por este motivo exacto |

**Los ocho puntos que quedan definidos**, y ninguno queda a criterio de F6:

```text
1 ORDEN EXACTO        abandonada → fsync(fichero) → fsync(directorio) → deriva →
                      fsync(fichero) → fsync(directorio) → marcador del deriva →
                      retirada del marcador de transacción. Seis pasos, en este orden

2 CAMPOS              `abandonada`  OBLIGA `estado_observado[]` de TODAS las rutas ·
                      `autoridad` · `motivo` · `revision_base`
                                    PROHÍBE `deriva_emitida` · `resultado` ·
                      `derivados_regenerados` · `decision`
                      `deriva`      OBLIGA `causa: abandono-de-transaccion` · `afecta[]` ·
                      `items[]` · `autoridad` · `tx_afectada` · **`abandonada_id`**
                                    PROHÍBE `fase` · `tx` · `decision` · `resultado`

3 QUIÉN REFERENCIA    **el `deriva` al `abandonada`, y nunca al revés.** El que llega después
  A QUIÉN             nombra al que ya existe y ya es durable

4 CÓMO SE CALCULA     `id(abandonada) = EV-H(su cuerpo MENOS `id`)`, y su cuerpo **ya no
  CADA `id`           contiene ninguna referencia hacia adelante**
                      `id(deriva) = EV-H(su cuerpo MENOS `id`)`, con `predecesor` =
                      `id(abandonada)` y `abandonada_id` = `id(abandonada)`, los dos
                      calculables porque ese evento existe

5 EL MARCADOR         el de TRANSACCIÓN se MANTIENE hasta que **el `deriva` es DURABLE
                      —paso 4— y su propio marcador EXISTE** —paso 5—. El del `deriva` se
                      crea en el paso 5.
                      **Precisado por `P-09`**: esta sede decía «y su propio marcador son
                      durables», y §2.6.6 **no concede `fsync` al marcador del `deriva`**:
                      lo clasifica como NO EXIGIDO porque §2.9 lo reconstruye. «Durable»
                      significa en §2.6.6 `fsync` de fichero y de directorio, y usarlo aquí
                      exigía una garantía que la sede que reparte `fsync` no da. Lo exigible
                      es que **exista**, y que su ausencia se repare desde el diario

6 CUÁNDO SE PUEDE     **sólo después del paso 6.** Mientras el marcador de transacción esté
  HACER COMMIT        puesto, el commit está bloqueado (§2.6.10): es exactamente lo que
                      impide publicar un cierre cuyo bloqueo no es durable

7 CÓMO RECUPERA EL    **el arranque no adivina CUÁNDO se cayó: CLASIFICA POR LO QUE OBSERVA**,
  ARRANQUE            que es lo único durable. **Reescrito por `P-01` y `P-02` del documento
                      22 —los dos GRAVES—**, que demostraron que este punto era byte a byte
                      el de `7764cca`: repartía por TRAMOS DE TIEMPO, dejaba `[paso 4,
                      paso 5)` **sin dueño** y metía `[paso 1, paso 2)` en `W17`, donde el
                      `abandonada` puede no ser durable. **`D105` no se reescribe: se propaga
                      bien.** El reparto, y es el mismo que escriben la fila de `W17` y la de
                      `W8`:
                        · **NO hay `abandonada` durable** —no se emitió, o se perdió por no
                          haber pasado el paso 2— → la transacción **SIGUE ABIERTA**: es
                          `W11` y sus dos salidas. **Cubre todo `[paso 1, paso 2)`**, porque
                          hasta el `fsync` del paso 2 ese evento puede no existir, y la
                          garantía 3 de §2.6.6 lo dice con esas palabras
                        · **hay `abandonada` durable y NO hay `deriva` durable** → **`W17`**:
                          se completa el `deriva`, con sus dos `fsync`, su marcador y, sólo
                          entonces, la retirada del marcador de transacción. Idempotente por
                          el paso 0 de §2.6.4. Es **`[paso 2, paso 4)`**
                        · **hay `abandonada` y `deriva` durables, y el marcador de
                          transacción TODAVÍA PUESTO** → **`W8`**: crea el marcador del
                          `deriva` si falta —reconstruible desde el diario (§2.9) y por la
                          fila `X60`, y por eso no lleva `fsync`— y **sólo entonces** retira
                          el de transacción. Idempotente. Es **`[paso 4, paso 6)`, LOS DOS
                          TRAMOS**, y ahí vive el `[4, 5)` que antes no reclamaba nadie
                        · **marcador de transacción ya retirado** → nada que hacer
                      **Este punto, la fila de `W17` y la fila de `W8` dicen LO MISMO, y
                      ninguna cita a otra como fuente de un reparto que esa otra no escriba**
                      — que era el defecto exacto de `P-01`

8 `abandonada` DURABLE **se COMPLETA.** El cuerpo del `deriva` es una FUNCIÓN del
  Y `deriva` AUSENTE   `abandonada`, luego los dos arranques construyen el mismo cuerpo; y
                       **emitirlo dos veces es imposible porque el paso 0 comprueba antes si
                       ya existe un `deriva` con ese `abandonada_id`**. Ahí vive la
                       idempotencia, y **no** en la igualdad del `id`: §2.8 retiró ese
                       razonamiento —`predecesor` entra en el `id` y la recuperación no lo
                       garantiza— y esta sede se apoyaba en él (`R-01`). **No es un estado
                       ilegal ni irreparable: es la ventana `W17`**, y el paso 0 de §2.6.4
                       la resuelve

EL VALIDADOR Y LAS    describen el MISMO protocolo, y eso es comprobable. **Quién dice qué,
VENTANAS, ALINEADOS   para que no vuelva a haber dos direcciones** (`R-03`):
                        · **§3.6 FIJA LA FORMA**: `deriva` lleva `abandonada_id`;
                          `abandonada` tiene PROHIBIDO `deriva_emitida`. Es la sede del
                          contrato del evento, y nadie más la redefine
                        · **la capa B la VALIDA y remite**: exige «exactamente un `deriva`
                          que referencie por `abandonada_id`» —lo dicen su LISTA de reglas y
                          la tabla de las cuatro, con el mismo verbo—, y no inventa otra
                          dirección
                        · **§2.6.5 describe la caída** que lo deja ausente, que es `W17`
                        · **el paso 0 de §2.6.4 dice cómo se completa**, y comprueba la
                          existencia por `abandonada_id` ANTES de emitir
                      Antes, la capa B exigía que existiera y el paso 0 prohibía emitirlo:
                      **las dos afirmaciones no podían ser ciertas a la vez**, y esa
                      contradicción era `O-03`. Después, esta sede invocaba «la capa B» por
                      su nombre para una regla que su lista **no escribía** —vivía sólo en la
                      tabla de las cuatro—, y era `R-03`
```

> **Bloque reanclado por `P-23` del documento 22.** Estas dos viñetas son **la COLA del paso
> `F` del procedimiento de abandono**, cuya cabeza está más arriba en esta misma §2.6.9.
> Entre una y otra se insertaron la nota de `M-02`, la tabla de alternativas y los ocho
> puntos de `D105`, y quedaron a 83 líneas de su frase introductoria: sin rótulo, sin sujeto
> y con la sangría de los pasos de `E`, de modo que quien leyera el paso `E` como lista
> cerrada de seis pasos **no implementaba el orden que §2.3 y esta misma sección declaran
> crítico**. No se mueven de sitio —moverlas rompería las referencias a esta región—: se les
> devuelve la cabeza que les falta.

**LA COLA DEL PROCEDIMIENTO DE ABANDONO — qué queda por hacer DESPUÉS de cerrar la
transacción**, y el orden **no** es negociable:

```text
CUANDO LA TRANSACCIÓN YA ESTÁ CERRADA Y SU MARCADOR RETIRADO (paso 6 de `E`), y sólo
entonces:
                  · permitir el COMMIT DEL INCIDENTE
                  · y **sólo después**, eliminar `.ads/run/quarantine/<TX>/` si se creó
```

**Qué contiene exactamente el commit del incidente**, y es lo que cierra el defecto:

```text
LLEVA    · el estado canónico RESTAURADO A LA BASE — idéntico, byte a byte, al del commit
           anterior en todas las rutas de la transacción
         · el evento `preparada`
         · los eventos `conflicto`, con la EVIDENCIA DE LA DIVERGENCIA en su cuerpo
         · el evento `abandonada`, con su verificación
         · el evento `deriva`

NO LLEVA **ningún FICHERO CANÓNICO en su `hash_posterior_esperado`**. Ni uno: todos han
         vuelto a la base, y por eso el conjunto publicable es la BASE CONSISTENTE MÁS EL
         INCIDENTE, nunca la mezcla parcial.
         **El evento `preparada` SÍ conserva los suyos**, y debe conservarlos: es historia,
         está en `estado/eventos/`, y sin él no se sabría a qué resultado se iba ni desde qué
         base. Confundir «ningún fichero está en su hash posterior» con «ningún hash posterior
         se conserva» borraría la intención que hace auditable el abandono.
```

**Y por eso `abandonada` ES la rama «revertir» de `b.14`**, no un tercer desenlace. La
disyunción de `a.9` y `b.14` —«completar o revertir»— queda satisfecha por las dos ramas
reales del autómata, y `PN-7` se reformula en consecuencia (§16).

```text
QUÉ SE RETIRA DE     la afirmación de «ROLL-FORWARD ONLY» **como absoluto**. Era cierta para
«ROLL-FORWARD ONLY»  el estado PUBLICADO y se aplicaba también al ESPECULATIVO, que nadie ha
                     visto. Vigente:
                       · el estado PUBLICADO nunca se revierte automáticamente. Restaurarlo
                         es decisión del Owner y una transacción de reparación (§2.6.6)
                       · el estado ESPECULATIVO **sí se revierte**, y es la única forma de
                         abandonar sin publicar una mezcla
                     El argumento de §2.6.2 —«deshacer exigiría conservar el contenido
                     anterior»— sigue en pie y ahora tiene respuesta: el contenido anterior
                     **está en la `revision_base`**, que Git ya conserva. No se duplica nada.
```

#### Los CUATRO desenlaces materiales, y ninguno más

```text
1 · COMPLETADA            intención durable → aplicación completa → verificación →
                          `confirmada` → `derivada`
                          COMMIT PUBLICABLE. Marcador retirado. Nada bloqueado

2 · CONFLICTO QUE CESA    → `conflicto` → nueva clasificación → aplicación completa →
                          `confirmada` → `derivada`
                          COMMIT PUBLICABLE. Marcador retirado. Nada bloqueado

3 · ABANDONADA            → `conflicto` → captura de la divergencia → restauración local
                          completa → verificación byte a byte contra la base →
                          `abandonada` → `deriva`
                          COMMIT DE INCIDENTE SOBRE BASE CONSISTENTE. Marcador retirado.
                          Los items del `deriva`, bloqueados hasta su reparación

4 · TODAVÍA BLOQUEADA     no puede completar, y **no puede preservar la divergencia o
                          restaurar la base**
                          PERMANECE ABIERTA · marcador VIVO · **NO HAY COMMIT** · exige
                          intervención EN LA MISMA MÁQUINA
                          No es un estado sin salida: sus salidas son las tres de arriba, y
                          lo que falta es una condición material, no una transición

NINGÚN TERMINAL DEJA ESTADO ESPECULATIVO DENTRO DEL CONJUNTO PUBLICABLE. Los desenlaces 1 y
2 lo convierten en estable; el 3 lo restaura a la base; el 4 no publica.

QUÉ ES `4b`, Y POR QUÉ NO ES UN QUINTO DESENLACE — **añadido por `P-16` del documento 22**
  `4b` es el rótulo de una **SECUENCIA** —`4b · ABANDONO IMPOSIBLE`, más abajo en esta misma
  §2.6.9—, **no de un desenlace**. Su desenlace ES el **4 · TODAVÍA BLOQUEADA**, y por eso
  conserva el marcador vivo y no publica. Seis sedes de este documento la citaban como
  «desenlace `4b`» —incluida `X58`, que es contrato de prueba que F6 debe construir, y la
  fila de reconstrucción de §2.9—, y quien viniera aquí a resolver `4b` **no lo encontraba**:
  es el espacio de identificadores con dos significados que `D83` declara cerrado.
  **La regla, y vale para todo el documento:** *los desenlaces se numeran `1`–`4` y no hay
  ninguno más; las SECUENCIAS llevan letra tras el número y viven en su propio bloque.*
  **[HISTÓRICO] El cardinal «Seis sedes» es lo que se contó entonces y no se reescribe.**
  **CÓMO SE COMPRUEBA HOY, que es lo que faltaba:** el barrido **no publica cardinal** — la
  condición es *`grep -n 'desenlace .4b.'` sobre este documento devuelve SÓLO líneas que estén
  dentro de una nota de corrección o de un registro de decisión*, y toda mención VIVA dice
  «secuencia `4b`». Un cardinal escrito aquí volvería a caducar el día que se añada una sede;
  la condición, no. Y `D79` —«el desenlace `4b` lo cierra un ACTO DE
  AUTORIDAD del Owner»— **no se reescribe**: es registro de decisión, y lo que cierra la
  autoridad es la retención de esa secuencia dentro del desenlace 4
```

#### El predicado que mantiene el bloqueo, y cómo se cierra

```text
bloqueado_por_deriva(item) ≡
    existe un evento `deriva` que NOMBRA ese item y para el que NO existe ningún evento
    `derivada` cuyo campo `resuelve_deriva` apunte a él

CÓMO SE CIERRA     una TRANSACCIÓN DE REPARACIÓN, con `tx` nuevo, cuyo `preparada` declara
                   por ruta **`hash_previo` = el `hash_observado` que el evento `deriva`
                   registró para esa ruta** —**para las TRES causas**, sin excepción— y
                   `hash_posterior_esperado` = lo que la autoridad decida, y cuya `derivada`
                   lleva **`resuelve_deriva` = el `id` de ese `deriva`**.
                   **`revision_base` de la reparación es la revisión PUBLICADA que ya
                   contiene el incidente cerrado**, no la anterior a él: por eso su `tx` es
                   distinto del de la transacción abandonada (§2.8, `D96`).
                   **Y el ancla de la restauración NO es `hash_previo`**: es
                   `revision_base`, que es un dato DISTINTO y con nombre distinto. Confundir
                   los dos era lo que producía las dos formulaciones incompatibles que el
                   gate definitivo señaló (`J-04`; es `D100`).
                   Al cerrar, el predicado se vuelve falso, **se retira
                   `estado/deriva/<ID>.abierta`** —lo retira la transacción CERRADA que lo
                   resuelve, en el mismo acto que su `derivada`, igual que un terminal retira
                   el marcador de transacción— y los items se desbloquean.

POR QUÉ ESTO NO    porque el `deriva` tiene una forma explícita y comprobable de terminar, y
REPRODUCE `B1`     el estado sobre el que trabaja la reparación es la BASE CONSISTENTE, no
                   una mezcla. `reconciliacion_pendiente` de §2.6.9 consume este predicado
                   en su segunda rama.
```

#### CONTENCIÓN — un conflicto no congela el producto

> **Corregido por `B1`.** El bloqueo vivía en el marcador de la transacción, y la regla de
> commit de §2.6.6 convierte cualquier marcador abierto en un bloqueo **global**: ADS no
> commitea el control repo con una transacción abierta. Un conflicto de un fichero paraba el
> producto entero. El alcance pasa a estar declarado y acotado.

```text
ALCANCE EXACTO DEL       las RUTAS que el `conflicto` —o el `deriva` posterior— NOMBRA, y los
BLOQUEO                  ITEMS a los que esas rutas pertenecen. Nada más.

QUÉ SE BLOQUEA           · el despacho de trabajo sobre esos items
                         · toda transacción nueva que declare ALGUNA de esas rutas
                         · la regeneración de derivados que dependan de esos canónicos
                         · la lectura fiable de esas rutas (§2.6.8)

QUÉ PUEDE CONTINUAR      **con la honestidad de lo que un worktree único sostiene**, que es
                         menos de lo que la redacción anterior prometía:
                           · **UN ÚNICO EJECUTOR DE MUTACIÓN por clon/worktree** (`R5`), y
                             **ninguna segunda transacción canónica concurrente en el mismo
                             worktree**. El paralelismo de escrituras aisladas mediante
                             varios worktrees es **capacidad futura, no garantía actual**
                           · otros agentes pueden continuar ANÁLISIS o trabajo que **no
                             escriba en este control repo**
                           · otras máquinas pueden trabajar desde la MISMA BASE, y su
                             publicación **se serializa por el CAS de Git** (§2.6.10): un
                             rechazo non-fast-forward obliga a releer y recalcular, y
                             **nunca a forzar**
                           · **DESPUÉS de publicar un incidente abandonado**, los items no
                             cubiertos por el `deriva` continúan con normalidad, y los
                             cubiertos quedan bloqueados hasta su reparación
                           · el commit del control repo, en cuanto no queda ningún marcador
                             abierto **y no hay estado especulativo vivo**. Un `deriva` sin
                             reparar NO impide commitear: impide despachar los items que
                             nombra

CÓMO SE DETECTA EL       por INTERSECCIÓN DE CONJUNTOS DE RUTAS, comparando el `afecta[]` de
SOLAPAMIENTO             la `preparada` que quiere abrirse contra la unión de rutas de todos
                         los `conflicto` sin terminal y todos los `deriva` sin reparar.
                         Es la misma comparación que `R5` ya hacía con el marcador, aplicada
                         a rutas en vez de a «hay o no hay marcador»:
                           · marcador de OTRA transacción con rutas solapadas → NO ARRANCA
                           · marcador de otra transacción SIN solape           → arranca
                         `X08` sigue siendo cierto para el caso que describe —dos ejecutores
                         que tocan EL MISMO fichero— y deja de bloquear a los que no.

CÓMO SE PUBLICA EL       **NO se publica mientras la transacción está abierta**, y decir lo
CHECKPOINT DE            contrario era el defecto. Un `conflicto` pertenece por definición a
CONFLICTO                una transacción abierta, y la regla de commit prohíbe commitear con
                         marcador abierto: **es imposible que llegue al servidor antes de que
                         la transacción cierre**. Lo que se publica es el COMMIT DE INCIDENTE
                         de la salida 2, con la transacción ya cerrada, la base restaurada y
                         `preparada`, `conflicto`, evidencia, `abandonada` y `deriva` dentro.

CÓMO SE PRESERVA LO      la copia íntegra vive en el cuerpo del `conflicto`, que **mientras la
DIVERGENTE, Y HASTA      transacción está abierta SÓLO EXISTE LOCALMENTE**. Sus garantías,
DÓNDE                    dichas sin adornos:
                           · para abandonar, se PRESERVA ANTES de restaurar (paso A)
                           · el commit del incidente **debe incluirla**, o incluir un
                             artefacto durable autorizado que permita recuperarla
                           · **hasta que ese commit se publica, NO hay garantía frente a la
                             pérdida total de la máquina**
                           · después de publicarse, otra máquina puede continuar desde ella

SI LO DIVERGENTE NO      **`SEG` bloquea su publicación** —secretos, material no publicable—.
ES PUBLICABLE            Entonces se conserva únicamente una REFERENCIA SEGURA o la evidencia
                         que `SEG` permita, y **la transacción NO puede declararse abandonada
                         hasta que exista una forma autorizada de preservar lo necesario**.
                         Sin preservación autorizada, el desenlace es el cuarto: sigue
                         abierta.
```

#### RECUPERACIÓN — tres garantías, y ninguna promete más de lo que hay

> **Corregido por la comprobación adversarial previa al gate (`D70`).** El texto afirmaba que
> otra máquina reanuda «clonando o actualizando el control repo», y **eso es imposible para
> una transacción abierta**: sus eventos no están commiteados —la regla de commit lo impide—,
> el marcador no viaja (`D50`) y las escrituras especulativas tampoco. Se sustituye por los
> tres niveles reales.

```text
NINGÚN TERMINAL DEJA     **todo terminal retira el marcador**: `derivada` al regenerar los
EL MARCADOR ABIERTO      derivados, `abandonada` tras verificar la restauración. Y el
                         **la** secuencia `4b` no es terminal: por eso conserva el marcador
                         vivo, y
                         por eso no publica.
```

```text
A · MISMA MÁQUINA,       recuperación **EXACTA**, desde diario, marcador y worktree.
    MISMO DISCO            · puede CONTINUAR, RESTAURAR o ABANDONAR
                           · conserva la copia divergente local
                         Es la garantía fuerte, y la única que hay para lo abierto.

B · OTRA MÁQUINA,        recuperación **COMPLETA desde Git**.
    TRANSACCIÓN YA         · si completó, el estado está publicado y no hay nada que hacer
    CERRADA Y PUBLICADA    · si se abandonó, recibe el INCIDENTE ENTERO: base restaurada,
                             `preparada`, `conflicto`, divergencia conservada, `abandonada`
                             y `deriva`
                           · **puede iniciar la reparación** sin haber estado allí

C · OTRA MÁQUINA,        **NO EXISTE REANUDACIÓN EXACTA.**
    TRANSACCIÓN ABIERTA    · diario, marcador, copia divergente y escrituras especulativas
    NO PUBLICADA             **no están en el servidor**
                           · se REINICIA desde la última INTENCIÓN PUBLICADA y la revisión
                             base estable
                           · **se pierde toda observación que sólo existiera en la máquina
                             desaparecida**, incluida la copia de lo divergente
                           · esto es **REINICIO SEGURO, no reanudación**, y no se llama de
                             otra manera
```

```text
LIMITACIÓN ACEPTADA,     · la pérdida total de la máquina durante una transacción abierta
DECLARADA Y NO             **puede perder evidencia no publicada**
DISIMULADA               · soportar reanudación exacta distribuida exigiría publicar un
                           checkpoint AISLADO: rama o worktree transaccional, worktree
                           remoto, o un almacén durable aparte
                         · **esa capacidad NO se declara construida ni incluida** en la
                           arquitectura vigente
                         · **no se presenta como capacidad de PesquerApp** hasta que exista

QUÉ GARANTÍA SE          **la reanudación exacta distribuida de una transacción abierta.** Es
SACRIFICA, DICHO EN      el precio de un worktree único con publicación sólo de estados
UNA LÍNEA                terminales consistentes, y se paga a sabiendas.
```

#### Las secuencias completas, una por rótulo del bloque de abajo, y ninguna termina sin salida

```text
1 · ÉXITO NORMAL              preparada → confirmada → derivada
                              3 eventos · marcador retirado · nada bloqueado

2 · CONFLICTO QUE SE          preparada → conflicto(obs 1) → confirmada → derivada
    RESUELVE SOLO             4 eventos. La divergencia cesó y `W3`/`W4` completaron.
                              Ningún humano intervino

3 · CONFLICTO CON VARIAS      preparada → conflicto(1) → conflicto(2) → … → confirmada
    OBSERVACIONES                       → derivada
                              3 + k eventos, k = observaciones DISTINTAS. Sin tope, porque
                              cada `conflicto` registra un estado del mundo, no un intento

4 · ABANDONO AUTORIZADO       preparada → conflicto(1) → [capturar · restaurar · verificar]
                                        → abandonada → deriva
                              3 eventos de fase más el `deriva` · marcador RETIRADO · los
                              canónicos RESTAURADOS a la base y verificados byte a byte ·
                              COMMIT DE INCIDENTE sobre base consistente · un `deriva`
                              mantiene bloqueados los items nombrados

4b · ABANDONO IMPOSIBLE       preparada → conflicto(1) → [no se puede preservar la
                              divergencia, o no se puede verificar la restauración]
                              la transacción PERMANECE ABIERTA · marcador VIVO · NO HAY
                              COMMIT · exige intervención en la MISMA MÁQUINA
                              **LO CIERRA UN ACTO DE AUTORIDAD DEL OWNER, y son dos**
                              (`A9`; es `D79`, revisado por `D87` en el plano de la
                              cuarentena):
                                (i)  AUTORIZAR LA CUARENTENA — copiar lo divergente fuera del
                                     worktree, a **`.ads/run/quarantine/<TX>/`**, con su hash
                                     registrado en el `conflicto`. Con eso la preservación
                                     deja de ser imposible y el desenlace 4 se vuelve
                                     alcanzable por el camino normal. Es OPERACIONAL, LOCAL y
                                     TEMPORAL: su contrato completo está abajo
                                (ii) DECLARAR IRRECUPERABLE el estado especulativo local y
                                     ordenar el cierre: `abandonada` registra el
                                     `estado_observado[]` de TODAS las rutas TAL COMO ESTÁN
                                     —con `clasificacion: divergente` donde lo estén—, el
                                     `deriva` conserva el bloqueo sobre los items nombrados,
                                     y el commit de incidente **NO incluye las rutas
                                     divergentes**, que quedan fuera del conjunto publicable
                              Ninguna de las dos es automática, ninguna la toma el runtime, y
                              las dos dejan evento con su autoridad. Lo que NO existe es un
                              4b que se cierre solo

5 · REPARACIÓN POSTERIOR      TX-2: preparada → confirmada → derivada
                              3 eventos, transacción NUEVA e independiente. Al cerrar,
                              resuelve el `deriva` y desbloquea los items

6 · NUEVA DIVERGENCIA         TX-2: preparada → conflicto(1) → …
    DURANTE LA REPARACIÓN     con SUS dos salidas. Sin anidamiento y sin recursión: TX-1
                              ya está cerrada y no participa

7 · TRABAJO INDEPENDIENTE     TX-3 sobre rutas que NO se solapan: preparada → confirmada
    MIENTRAS HAY CONFLICTO             → derivada
                              arranca, avanza y cierra con normalidad, con TX-1 en
                              conflicto. Es la contención en un caso concreto
```

#### LA CUARENTENA del acto (i) — operacional, local y temporal

> **Corregido por el gate de cierre independiente (`I-01`, GRAVE; es `D87`, que revisa `D79`
> sin reescribirla).** `D79` colocó la cuarentena en **`estado/cuarentena/<TX>/`**, y esa ruta
> no tenía plano en §1.2 ni en §2.4, ni fila en §1.3, ni entrada en el árbol de §2.3, ni
> declaración de `.gitignore`, ni fila de reconstrucción en §2.9, ni ciclo —nadie decía cuándo
> se vacía—, ni fila adversarial. Por el criterio vigente de §2.4 quedaba **durable y
> versionada**, y entonces el acto (i) **publicaba en `main` exactamente el material que
> existe para preservar cuando `SEG` prohíbe publicarlo**. Y §2.6.10 descarta la alternativa
> D precisamente porque «crea una tercera ubicación con su ciclo y su plano, que §2.4 no
> tiene» — objeción que se aplicaba palabra por palabra a la ruta nueva.
>
> **Se resuelve sin crear una tercera fuente de verdad**: la ruta `estado/cuarentena/<TX>/`
> queda **RETIRADA de la arquitectura vigente**, y la preservación temporal vive donde ya
> existe un plano para ella.

```text
DÓNDE VIVE            **`.ads/run/quarantine/<TX>/`**, dentro del plano OPERACIONAL que §1.2
                      y §2.4 ya declaran. NO es una ubicación nueva de estado: es un
                      directorio más de `.ads/run/`, con el mismo `plano`, el mismo ciclo y
                      la misma exclusión de Git que el lock, la caché y el índice compilado.

QUÉ ES, Y QUÉ NO ES   · OPERACIONAL · LOCAL · **NO CANÓNICA** · ignorada por Git
                      · **NO es fuente de verdad de nada.** La verdad de lo divergente es la
                        copia íntegra que el `conflicto` lleva en su cuerpo (§3.6); la
                        cuarentena es el soporte físico que hace esa preservación posible
                        cuando el worktree tiene que restaurarse encima
                      · **NO gana identidad ni autoridad propias**, y §1.3 no le da fila
                      · **NO se usa como garantía de reanudación distribuida**: no viaja, y
                        la garantía `C` de arriba sigue siendo REINICIO SEGURO, no reanudación

CUÁNDO SE CREA        **ANTES de restaurar**, dentro del paso A del procedimiento —conservar
                      la divergencia antes de tocar nada—. Restaurar sin haberla creado y
                      verificado es exactamente lo que el paso A prohíbe.

CÓMO SE VERIFICA      **POR HASH.** El hash de cada fichero puesto en cuarentena se registra
                      en el `conflicto`, y se recalcula sobre la copia antes de continuar. Si
                      no casa, la preservación NO se ha logrado y **se permanece en la
                      SECUENCIA `4b`**, cuyo desenlace es el **4 · TODAVÍA BLOQUEADA**: la
                      transacción permanece abierta. **Convertido aquí**, que era una de las
                      dos sedes vivas que el barrido de `P-16` no alcanzó.

CUÁNDO SE ELIMINA     **SÓLO después de las TRES**, y en este orden:
                        1 el terminal es durable —`abandonada`, con su `deriva`—
                        2 la verificación del paso D está hecha y registrada
                        3 el COMMIT DEL INCIDENTE está hecho, y lleva la divergencia dentro
                      Antes de las tres, borrarla destruiría la única copia de un contenido
                      que todavía no está publicado. Después, no queda nada que perder: es
                      el criterio de §2.4 aplicado a su ciclo.

SI EL CONTENIDO NO    es el caso que `SEG` gobierna, y no cambia con la ruta nueva:
SE PUEDE CONSERVAR      · **`SEG` BLOQUEA LA PUBLICACIÓN** — secretos, material no publicable
O NO SE PUEDE             (arriba, «SI LO DIVERGENTE NO ES PUBLICABLE»)
PUBLICAR                · **el Owner PUEDE ACEPTAR EXPRESAMENTE LA PÉRDIDA DE LA PREIMAGEN**,
                          y esa aceptación es un acto suyo, registrado con su autoridad, su
                          motivo, su alcance y su fecha. Nadie la toma por él
                        · el INCIDENTE conserva, en todo caso, **hash · clasificación ·
                          autoridad · motivo · alcance** de lo que no se conservó
                        · y **NUNCA se publica el contenido prohibido**: la aceptación de la
                          pérdida es la alternativa a publicarlo, no una vía para publicarlo

QUÉ LIMITACIÓN SE     la misma que ya estaba aceptada y declarada, y **no mejora**: perder la
MANTIENE              máquina durante una transacción abierta **puede perder evidencia
                      operacional no publicada**, y la cuarentena es operacional. Sube la
                      probabilidad de poder abandonar; **no** convierte lo local en durable.
```

**Y con eso la alternativa D de §2.6.10 sigue descartada, sin contradicción.** Lo que aquélla
descarta es la cuarentena **como mecanismo general de aislamiento del estado especulativo**,
que exigiría una ubicación de ESTADO con su ciclo y su plano propios. Esto es otra cosa: una
**preservación puntual, bajo autoridad, en el plano operacional que ya existe**, y que se
vacía en cuanto el incidente está publicado. **La objeción de la tabla de alternativas de
esta misma §2.6.9 —la que descarta preservar lo divergente en una ubicación nueva porque
«crea una tercera ubicación»—** deja de aplicarse porque ya no se crea ninguna.
**Corregido por `P-24` del documento 22**: esta frase citaba «L2103», un número de línea
absoluto que el propio documento había desplazado —la cita vive hoy 346 líneas más abajo—, y
la sustitución NO es otro número: **es una referencia a la SEDE, que no caduca**. La regla,
para todo el documento: *una autorreferencia se hace por sección y por lo que la sede DICE,
nunca por número de línea; un número de línea sólo vale para citar OTRO fichero, y con su
revisión.*

```text
NINGÚN ESTADO ALCANZABLE   se comprueba sobre el grafo de cinco fases: `preparada` sale a dos
QUEDA SIN SALIDA           sitios; `conflicto` sale a dos; `confirmada` sale a uno;
                           `derivada` y `abandonada` son terminales POR DEFINICIÓN y retiran
                           el marcador. **No hay ningún nodo no terminal sin sucesor
                           admisible.**
                           La secuencia `4b` NO es una excepción del GRAFO: sus salidas son
                           las mismas y lo que falta es una CONDICIÓN MATERIAL —preservar o
                           restaurar—, no una transición. Y mientras falta, **el marcador
                           sigue vivo y no se publica nada**, que es el comportamiento seguro.
                           **Pero el bloqueo no lo levanta el autómata: lo levanta el
                           OWNER**, por uno de los dos actos declarados arriba. Decir «ningún
                           estado queda sin salida» sin nombrar esa autoridad prometía una
                           terminación por construcción que el diseño no da.
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
1  EL COMMIT LOCAL SE HACE, y emite su evento con **los CINCO CAMPOS DE PROCEDENCIA** de
   §3.6 —`ordenante` · `autoridad` · `escritor_del_comando` · `ejecutor` ·
   `actor_atribuido`—, **no «los cinco conceptos de `a.9`»**: el quinto concepto de `a.9` es
   el **PROPIETARIO DEL CAMPO**, que **se DERIVA** de §1.3 y no se persiste, y
   `actor_atribuido` pertenece a **otra** lista de `a.9`. La ausencia de cualquiera de los
   cinco campos es un FALLO DEL VALIDADOR, no un silencio.
   **Corregido por el gate de cierre (`A7`, FALLIDA).** Ésta era **la única sede que el gate
   final nombró y la única que no se tocó**: era byte a byte idéntica al texto base, y **la
   secuencia `4b` de §2.6.9, en su acto (i)**, la hace condición de validación — que es
   literalmente el sentido de su condición de cierre. **Corregido por `P-24`**: decía «L2226»,
   número de línea absoluto ya desplazado, y se sustituye por la sede, que no caduca.
   El documento ya lo escribía bien en las otras cinco sedes: `X39`, §2.6.6, §2.9 punto 9,
   §3.6 fila `preparada` y §3.6 el bloque de PROCEDENCIA. Es `D66` propagado, y `D95` lo
   registra.

2  EL PUSH NO ES AUTOMÁTICO. Pasa a `esperando-owner`, o a la política declarada en
   `adaptador.publicacion_control_repo` (abajo) — y **ninguna política autoriza publicar una
   RECUPERACIÓN**. Una recuperación que publica sin decirlo convierte un incidente local en
   un hecho remoto.

3  LA RAMA SE DECLARA, y no se adivina: **`main` del control repo**, que NO recibe la
   protección `G29` de las fuentes. `E2.4` conserva `G29` **por source**, y el control repo
   no es una source. **Corregido por `B2`**: invocarla aquí rellenaba por inferencia lo que
   dos párrafos antes se prometía no rellenar, y dejaba el estado sin camino a publicarse.
   Lo que protege esta rama es otra cosa: **el CAS de Git** —una actualización de referencia
   sólo avanza desde la revisión conocida, y un `push` non-fast-forward se rechaza—, commits
   sólo entre transacciones
   y push bajo autoridad (abajo).

4  PUSH RECHAZADO POR REMOTO AVANZADO → evento `fallo`, tope de TRES reintentos por §7.3, y
   se escala. **NUNCA `--force`.** Regla dura, heredada literalmente de §8.1:
   **ADS no reescribe historia publicada del control repo.**

5  «EL REMOTO ESTABA ATRASADO, NO ROTO» era un SUPUESTO, no una comprobación. `E2.7` y §2.11
   dejan ABIERTO el runtime distribuido —`E2.7` enumera «runtime distribuido · locks
   multi-agente · scheduler · colas», **sin nombrar máquinas**—, luego dos máquinas sobre el
   mismo control repo son un caso POSIBLE y no gobernado. **Corregido por `m5`**: decir que
   `E2.7` lo admite «expresamente» le atribuía una palabra que no tiene. En ese caso el
   remoto
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

**Ya no se declara como hueco: se escribe.** La tercera revisión independiente (`B2`)
encontró que el texto anterior prometía no rellenarlo por inferencia y, tres reglas más
abajo, lo rellenaba invocando `G29` para el control repo — cuando `E2.4` conserva `G29`
**por source**, con todas las letras. Y que sin gobierno declarado, `main` protegida y sin
rama de trabajo, **ningún commit de `estado/` podía llegar jamás a publicarse**, con lo que
caían las garantías 5 y 6 de §2.6.6, la reconstrucción sin árbol de §2.9, la condición previa
de toda `retirada-de-cuerpo` y la permanencia que `O15` exige. Es `D65`.

### El gobierno Git del REPOSITORIO DE CONTROL

#### Primero, qué papel juega Git aquí — y las cuatro alternativas, comparadas

| | alternativa | qué aporta | qué cuesta | veredicto |
|---|---|---|---|---|
| **A** | **worktree único** sobre la rama canónica | visibilidad directa del estado en vuelo; ningún merge; un solo mecanismo de recuperación | **no aísla el conjunto parcial**, y por eso exige que `abandonada` restaure (§2.6.9); no da reanudación exacta desde otra máquina | **ELEGIDA**, con las dos compensaciones de abajo |
| **B** | **staging/índice temporal** + commit atómico | atomicidad de la publicación | no ayuda a los lectores durante la ventana —el estado canónico ES el árbol de trabajo— y no aporta nada que el diario no dé ya para recuperar | descartada: coste sin garantía nueva |
| **C** | **worktree o rama transaccional** | aísla el conjunto parcial; permite publicar un checkpoint aislado y **reanudación exacta distribuida**; permite paralelismo real | **duplica el mecanismo de recuperación** —Git y diario compiten—; obliga a merge y convergencia; sube la complejidad del runtime y del gobierno de ramas | descartada **por coste y duplicación**, no por ilegibilidad. Es la que habría que construir para la reanudación distribuida |
| **D** | **cuarentena** fuera del estado canónico | aísla lo especulativo sin ramas | crea una tercera ubicación con su ciclo y su plano, que §2.4 no tiene; y lo que aísla es justo lo que `R1` quiere ver | descartada: reintroduce la tercera categoría que `D50` eliminó |
| **E** | **reinicio desde la intención publicada**, sin conservar estado en vuelo | mínima; ninguna maquinaria | pierde toda observación local | **ADOPTADA COMO GARANTÍA `C`** de recuperación (§2.6.9): no sustituye a A, la complementa cuando la máquina se pierde |

> **`R1` NO descarta el worktree transaccional, y decirlo era una inferencia falsa.** `R1`
> —`E2.1` sobre `a.9`— exige que *«el estado operativo ES los ficheros del repositorio ADS de
> control, legibles directamente, sin informe intermedio»*. Exige **ficheros de texto sin
> informe intermedio**; **no exige que estén en el worktree principal ni en la rama activa**.
> Un worktree o una rama contienen ficheros de texto directamente legibles y no introducen
> ninguna base de datos. La razón real del descarte es **coste y duplicación de mecanismos**,
> y así queda escrita.

**Lo ELEGIDO, con lo que cuesta dicho al lado:**

```text
SE ELIGE          · WORKTREE ÚNICO
                  · INTENCIÓN PUBLICADA ANTES de mutar (§2.6.0, y abajo)
                  · recuperación EXACTA sólo en el mismo disco
                  · RESTAURACIÓN LOCAL VERIFICADA al abandonar (§2.6.9)
                  · REINICIO SEGURO desde la intención publicada en otra máquina
                  · publicación **sólo de estados terminales consistentes**

SE SACRIFICA      la **REANUDACIÓN EXACTA DISTRIBUIDA de una transacción abierta**. Se paga a
                  sabiendas, se declara en §2.6.9 y **no se presenta como capacidad**.
```

```text
LA REGLA QUE CIERRA LA    **la recuperación es del DIARIO; la publicación es de GIT.** No hay
DUPLICACIÓN               dos mecanismos para el mismo estado de recuperación —y ésta es la
                          razón por la que `C` se descarta, no `R1`:
                            · CANÓNICO   el diario y los ficheros de `estado/`
                            · DERIVADO   la historia de Git, que los conserva y los mueve
                                         entre máquinas
                            · OPERACIONAL el marcador, reconstruible desde el diario (`D50`)
                          Git NO decide qué se recupera ni cómo: sólo dónde sobrevive.
```

#### La tabla de propiedad del control repo, que `C7` no cubre

| operación | quién la PIDE | quién la EJECUTA | quién puede BLOQUEARLA | quién VERIFICA | evidencia |
|---|---|---|---|---|---|
| crear el control repo | `PLT` en `INS-1`/`A1` | `PLT` | Owner | `VER` en el gate del circuito | commit inicial + evento `migracion`/`transicion` |
| **commit** de `estado/` | el runtime, al cerrar transacciones | el runtime (ejecutor único, `R5`) | un marcador abierto lo impide por §2.6.6 | el propio validador de integridad | commit + los eventos que incluye |
| **push** | el runtime lo PROPONE | **nadie automáticamente** | el Owner, por defecto | `VER` si la política lo exige | evento `fallo` si se rechaza; evento de publicación si se autoriza |
| **rama de trabajo** | no existe: el runtime escribe en la rama canónica | — | — | — | — |
| **PR / merge** | **no se usan para el estado** (abajo) | — | — | — | — |
| CI | `PLT` la configura | el proveedor | `PLT` | `VER` | informe de CI referenciado |
| rollback de publicación | Owner | `PLT` | Owner | `VER` | commit de reversión, **nunca** reescritura |
| retirada de rama abandonada | `PLT` | `PLT` | Owner | — | evento con su motivo |

#### Las decisiones que la tabla presupone, dichas una a una

```text
RAMA CANÓNICA          **`main` del control repo**, y es la ÚNICA que contiene estado
                       publicado. Su significado es INEQUÍVOCO y distinto del de las
                       fuentes: en una source, `main` es código revisado; aquí es **estado
                       emitido por el ejecutor único**.

PROTECCIÓN DE LA RAMA  **NO se le aplica `G29`**, y esto corrige la inferencia que `B2`
                       señaló: `E2.4` conserva `G29` **por source**, y el control repo no es
                       una source. Aplicarle la protección de una rama de código a una rama
                       de estado bloquearía toda escritura del runtime, que es lo que hacía
                       el texto anterior sin advertirlo.
                       Lo que SÍ la protege es otra cosa: **el CAS de Git**, que serializa
                       `main` entre máquinas sin acuerdo previo —y NO «un único escritor»,
                       que es una regla LOCAL por worktree (`R5`) y no dice nada de dos
                       máquinas empujando a la vez (`A12`; es `D84`)—,
                       **commits sólo entre transacciones** (§2.6.6) y **push bajo
                       autoridad**.

UNIDAD AISLADA DE      **la transacción, no la rama.** El aislamiento lo da el marcador y la
TRABAJO                regla de solapamiento de rutas (§2.6.9), no un worktree: el estado
                       tiene que ser legible en el árbol mientras se trabaja (`R1`).
                       Worktrees y ramas se usan **en las fuentes**, gobernados por `C7`, y
                       para aislar la ADOPCIÓN de un producto (`O15`) — no para aislar
                       transacciones del control repo.

PR Y MERGE             **no se usan para el estado.** Un PR es una puerta de revisión humana
                       sobre contenido escrito por humanos; `estado/` lo emite el ejecutor
                       único y ya pasó por los gates de su ruta. Exigir PR duplicaría el
                       gate y dejaría el estado sin publicar mientras nadie lo abre.
                       SÍ se usan para lo que sí es material revisable del control repo
                       —`PROFILE.md`, `PROJECT.md`, `SOURCES.toml`, adaptadores—, y ahí el
                       proponente es una capacidad y el aprobador el Owner.

AUTORIDAD DE           **el Owner por defecto**, y ADS **nunca publica una recuperación**
PUBLICACIÓN            por su cuenta. Un incidente local no se convierte en un hecho remoto
                       sin que alguien lo decida. La alternativa —publicación automática
                       bajo una política— existe y está definida abajo.

MAIN NUNCA CONTIENE    **porque los DOS terminales dejan el árbol consistente ANTES de que
ESTADO PARCIAL         exista commit**, y no por la inferencia «sin marcador ⇒ cerrada»:
                       `derivada` cierra sobre canónicos que ya alcanzaron su
                       `hash_posterior_esperado`, y `abandonada` es INALCANZABLE hasta haber
                       RESTAURADO todas sus rutas a `revision_base` y haberlo **verificado
                       byte a byte** (§2.6.9, pasos C y D). La secuencia `4b` no publica.
                       **Corregido por `I-10`**: el argumento anterior —«sin marcador toda
                       transacción está cerrada, luego `main` no contiene estado parcial»— es
                       **exactamente la inferencia que `D69` refutó**, porque antes de `D69`
                       una transacción cerrada sin restaurar dejaba el conjunto parcial
                       **publicable**. La conclusión sigue siendo cierta; lo que fallaba era
                       su razón, y la razón real es la restauración verificada.
                       Y un abandono **no deja «estado mixto» en las rutas canónicas
                       publicadas**: en la ruta normal todas quedan clasificadas `previo`. El
                       enum `{previo, posterior, divergente}` de `estado_observado[]` (§3.6)
                       sólo alcanza `posterior` y `divergente` en el **acto (ii) del
                       secuencia `4b`**, donde el Owner declara irrecuperable lo especulativo
                       y el commit de incidente **EXCLUYE** las rutas divergentes. Decirlo
                       importa: sin ello F6 construiría el validador sobre un enum cuya
                       alcanzabilidad depende de un caso que el contrato no nombraba.
```

#### Concurrencia entre máquinas, y actualización optimista

```text
CONTRA QUÉ REVISIÓN    el runtime registra el `HEAD` del control repo que leyó al arrancar —
SE TRABAJA             la REVISIÓN CONOCIDA— y la lleva en el evento de publicación.

ANTES DE PUBLICAR      `fetch` y comprobación de que la publicación es **fast-forward** sobre
                       la revisión conocida. Es un compare-and-swap sobre revisión, el mismo
                       patrón que `a.9` usa sobre hash de contenido — **y con su contador
                       propio**, que no es el de `a.9` ni el de §2.6.9.

SI EL REMOTO AVANZÓ    **rechazo non-fast-forward**: evento `fallo` con `operacion: push`,
                       la revisión conocida, la revisión remota y el diagnóstico; tope de
                       tres reintentos por §7.3; y se escala. El estado LOCAL no cambia: un
                       push rechazado no es una mutación canónica (`W15`, `W16`).

CÓMO CONVERGEN DOS     por el diario: los eventos son inmutables y direccionados por
MÁQUINAS               contenido, luego una fusión de historias produce la UNIÓN de eventos y
                       la bifurcación se DETECTA (`X09`). Resolverla es runtime distribuido,
                       que `E2.7` y §2.11 dejan abierto — y el comportamiento seguro
                       entretanto es que la segunda máquina **no publique** y escale.

`--force`              **PROHIBIDO.** Sin excepción automática. Sólo un PROCEDIMIENTO
                       EXTRAORDINARIO DEL OWNER, con decisión registrada, motivo, alcance y
                       evidencia previa de que la historia que se descarta está respaldada.
                       Ninguna recuperación, ningún reintento y ninguna política lo autorizan.

RELACIÓN CON LOS       ninguna directa: un `integration-set` afirma que una combinación de
INTEGRATION SETS       revisiones DE LAS FUENTES se probó junta (`ENT`, §10). El control repo
                       **referencia** esas revisiones y no participa en el set. Publicar el
                       control repo no exige un set, y producir un set no exige publicar.
```

#### La INTENCIÓN PUBLICADA PREVIA, y qué no es

> **Añadida por `D69`.** Es lo que hace que un clon nuevo pueda **reiniciar** el trabajo sin
> depender del chat ni de la máquina perdida, y la condición 4 de §2.6.0 la exige antes de
> mutar nada.

```text
QUÉ ES            el registro, YA COMMITEADO Y EMPUJADO, de que este trabajo debe hacerse.
                  Lleva SIETE cosas:
                    1 ITEM U ORDEN CAUSAL      qué lo motiva, con su id
                    2 REVISIÓN BASE            el `HEAD` sobre el que se va a trabajar
                    3 ALCANCE                  las rutas e items que se van a tocar
                    4 AUTORIDAD                quién puede decidirlo (§1.3)
                    5 OPERACIÓN SOLICITADA     qué se pide hacer, no cómo
                    6 IDENTIFICADOR ESTABLE    para que el reinicio la reconozca
                    7 EVIDENCIA DE SU COMMIT   el commit y el push que la publicaron
                      Y SU PUSH

CUÁNDO SE          **el runtime NO INICIA la transacción** hasta comprobar que esta intención
COMPRUEBA          está en el ÚLTIMO ESTADO ACEPTADO del control repo. No basta con que esté
                   commiteada: tiene que estar PUBLICADA.

QUÉ NO ES          **publicar la INTENCIÓN no es publicar la TRANSACCIÓN ABIERTA.** La
                   intención dice QUÉ hay que hacer y sobre qué base; la transacción abierta
                   —su `preparada`, su marcador, sus escrituras especulativas— **no se
                   publica nunca** (§2.6.9). Confundirlas sería volver a prometer reanudación
                   distribuida.

PARA QUÉ SIRVE     para la garantía `C`: una máquina nueva lee la intención publicada y la
                   revisión base, y **reinicia** el trabajo desde ahí. Sin ella, un clon
                   nuevo no sabría siquiera que ese trabajo existía.
```

#### La POLÍTICA DE PUBLICACIÓN, definida — o retirada

> **Corregido por `M1`.** El texto anterior ofrecía «la política de publicación que el
> producto declare» como alternativa a `esperando-owner`, y esa sede **no existía en ninguna
> parte del corpus**: sin esquema, sin fichero, sin autoridad, sin ciclo y fuera del recuento
> de §3.8. Es el modo de fallo que `D43` corrigió para `contrato-de-aspecto`.

**No se crea un tipo nuevo.** La política es un **campo del `adaptador` del control repo**,
que ya es el artefacto donde vive la configuración de plataforma del producto (§6):

```text
DÓNDE VIVE        `adaptador.publicacion_control_repo`, en el control repo. NO es un tipo
                  nuevo, y §3.8 no cambia.

QUÉ VALORES       `esperando-owner`   POR DEFECTO. Todo push lo autoriza el Owner
                  `automatica`        el runtime publica al cerrar, sin preguntar
                  `programada`        el runtime publica en la ventana declarada

QUÉ DECLARA       autoridad que la aprobó · fecha · alcance · condición de revocación. Es
ADEMÁS            una decisión revocable, como la política de auditoría de `O7`.

QUÉ NO PUEDE      **ninguna política autoriza publicar una RECUPERACIÓN.** Un push que sigue
HACER NUNCA       a una recuperación pasa siempre por el Owner, sea cual sea el valor. Y
                  ninguna autoriza `--force`.

SI NO ESTÁ        vale `esperando-owner`. La ausencia nunca significa «publica».
DECLARADA
```

#### Qué queda para F5, y se registra como presión normativa

**Este gobierno NO está en `(a)`, `(b)`, `E1`, `E2`, `C6` ni `C7`**, y `E2.4` cierra
expresamente la vía de derivarlo de `G29`. Escribirlo aquí lo hace implementable, pero su
**sede normativa definitiva no existe**: `C7` gobierna las fuentes, y extenderlo al control
repo es material del Owner. Queda registrado como **`PN-11`** en §16, y **`C7` no se toca en
esta pasada**.

### 2.6.11 · `deriva` — lo que se descubre DESPUÉS del cierre no es una fase

> **Añadida por la corrección técnica posterior (hallazgo `2`, BLOQUEANTE).** §2.6.6 y `W12`
> decían que un canónico revertido bajo una transacción durable *«emite `conflicto`»*, y
> `conflicto` es una **fase de la transacción**. Con `derivada` como único terminal —**como
> lo era ENTONCES**; `D64` hizo terminal también a `abandonada`, y `D71` fijó el predicado—, eso es
> **una transición que sale del terminal** — que la tabla de §2.6.1 declara defecto. El
> protocolo se contradecía en el punto donde detecta corrupción silenciosa. Es `D53`.

**La distinción que faltaba, y es de identidad, no de grado:**

```text
CONFLICTO      se descubre MIENTRAS la transacción sigue abierta —`abierta(tx)`, §2.6.1—. Es una
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
tx_afectada      la transacción CERRADA cuyo resultado ya no se sostiene, o la ABANDONADA
                 cuyas rutas quedaron mixtas, si la hay.
                 Es una REFERENCIA, no una pertenencia: no la reabre, no la modifica y no
                 añade ninguna fase a su historia
causa            **EL ENUM LO DECLARA §3.6, Y ES SU ÚNICA SEDE.** Son TRES valores. Lo que
                 sigue es su GLOSA —qué significa cada uno—, no una segunda declaración: si
                 alguna vez difieren, manda §3.6. Es `D72`, que cierra `A1`.

                 `posterior-al-cierre`   el fichero casaba y ya no casa, con `derivada`
                                         durable. Corrupción silenciosa (garantía 3 de
                                         §2.6.6). LLEVA `tx_afectada`
                 `sin-transaccion`       nadie preparó nada: alguien editó un canónico
                                         fuera del protocolo. **NO lleva `tx_afectada`**:
                                         no hay ninguna a la que referirse
                 `abandono-de-           **añadida por `D64`.** Una autoridad cerró la
                 transaccion`            transacción con `abandonada` sin completarla. **Sus
                                         rutas canónicas quedaron RESTAURADAS a
                                         `revision_base` y verificadas byte a byte** —`D69`
                                         hace `abandonada` inalcanzable sin eso—, y lo que
                                         queda declarado es el `estado_observado[]` de todas
                                         ellas: `previo` en la ruta normal, y `posterior` o
                                         `divergente` **sólo** en el acto (ii) de la
                                         **SECUENCIA** `4b` —convertido aquí; era la otra sede
                                         viva que el barrido de `P-16` no alcanzó—, cuyas
                                         rutas divergentes el commit de incidente
                                         excluye. **Corregido por `I-10`**: decía «quedaron en
                                         un estado mixto declarado», que es la semántica
                                         anterior a `D69`. Lo emite el propio acto de
                                         abandono, en el mismo instante, y es lo que conserva
                                         el bloqueo cuando el marcador se retira (§2.6.9).
                                         LLEVA `tx_afectada`
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

```text
CUÁNDO SE RESUELVE UN    cuando una transacción de reparación CIERRA por `derivada` y sus
`deriva`                 rutas alcanzan el `hash_posterior_esperado` que esa reparación
                         declaró. Sólo entonces deja de bloquear y deja de hacer NO FIABLES
                         sus rutas (§2.6.8). **Un `deriva` no se retira: se resuelve**, y el
                         evento que lo resuelve lo REFERENCIA.

POR QUÉ ESTO CIERRA      porque el bloqueo pasa a tener una forma explícita de terminar. Es
`B1`                     la diferencia con el estado agotado que `D64` retira: aquél no
                         tenía ninguna.
```

**Y si hay que reparar, la reparación es una transacción nueva:**

```text
REQUIERE UNA OPERACIÓN RECUPERABLE, con su INTENCIÓN DURABLE PREVIA — es decir, su propio
`preparada`, con `hash_previo` = el `hash_observado` que la deriva registró —**ÚNICA
FORMULACIÓN, y vale para las TRES causas del enum**: `posterior-al-cierre`,
`sin-transaccion` y `abandono-de-transaccion`—, `revision_base` = la revisión publicada que
ya contiene el incidente cerrado, y `hash_posterior_esperado` = lo que la autoridad decida.

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
              procedencia, `base` y **`revision_base`**—, luego es reproducible por dos
              implementaciones, NO depende del punto de la cadena en que se emita, y
              SOBREVIVE A UNA REEMISIÓN. F4c no tenía definiendum: un `tx` no tiene
              contenido propio —§2.5 lo declara— luego no había nada de lo que sacar su
              huella

QUÉ ENTRA,    entra **todo el cuerpo de `preparada` menos `id`, `tx` y `predecesor`**, y
DICHO SIN     `revision_base` es parte de ese cuerpo desde `D96`, luego **entra**. Se dice
AMBIGÜEDAD    expresamente porque de ello depende que una reparación posterior no colisione
              con la transacción que repara
```

**Y por qué una REPARACIÓN posterior no colisiona con la transacción ABANDONADA** —cerrado
por el gate definitivo independiente (`J-02`, GRAVE; es `D96`):

```text
EL PROBLEMA   tras un abandono, `C · RESTAURAR` devuelve todas las rutas a `revision_base`.
QUE HABÍA     La reparación natural declara el MISMO `afecta[]`, los MISMOS hashes, el
              MISMO `orden` y la MISMA procedencia. Con `id` y `predecesor` excluidos del
              cómputo, su `tx` era EL MISMO: la regla de reintento la volvía NO-OPERACIÓN,
              la capa B la rechazaba por posterior a un terminal, y `bloqueado_por_deriva`
              no se cerraba por su camino natural

POR QUÉ AHORA 1 · la transacción original parte de la revisión ANTERIOR al incidente
NO OCURRE     2 · el incidente cerrado —`abandonada` y su `deriva`— SE PUBLICA, y publicarlo
              produce una revisión NUEVA
              3 · la reparación parte de ESA nueva revisión publicada
              4 · luego su `revision_base` es DISTINTO, y con él su `tx`

              No hay nada que añadir al evento para conseguirlo: el dato ya era necesario
              por §2.5, §2.6.9 y §2.6.11, y lo único que faltaba era declararlo en §3.6 y
              decir que entra aquí

QUÉ NO SE     **ni nonce, ni timestamp, ni aleatoriedad.** Un `tx` que dependiera de
INTRODUCE     cualquiera de las tres dejaría de ser reproducible por dos implementaciones,
              que es exactamente la propiedad por la que se definió así

QUÉ SE        la IDEMPOTENCIA de una misma intención sobre la MISMA base. Dos emisiones de
CONSERVA      la misma intención desde el mismo `revision_base` siguen computando el mismo
              `tx`, y la regla de reintento las sigue colapsando en una. Lo que se rompe es
              sólo la falsa igualdad entre dos intenciones que parten de revisiones
              distintas — que no son la misma transacción y nunca debieron compartir `tx`
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
> de una vez en un `tx` es `conflicto`, y no por reemisión sino porque el contrato la declara
> **repetible** con `observacion` como discriminador y sin tope (§2.6.4). Y
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
| el marcador `estado/tx/<TX>.abierta` | el diario: las transacciones que satisfacen **`abierta(tx)`** (§2.6.1) | total. Es un acelerador, no una verdad. La condición es UNA, y es el predicado: `preparada` durable sin ninguno de los DOS terminales |
| el marcador `estado/deriva/<ID>.abierta` | el diario: los eventos `deriva` para los que **`bloqueado_por_deriva(item)`** sigue siendo verdadero (§2.6.9) — es decir, sin ninguna `derivada` que los referencie en `resuelve_deriva` | total y determinista. Es un acelerador, no una verdad, exactamente igual que el anterior. `D88` le da esta fila, que `D78` no le había dado |
| `.ads/run/quarantine/<TX>/` | **NO SE RECONSTRUYE.** Es preservación temporal de contenido que sólo existía localmente (§2.6.9) | **ninguna, y se declara**: si se pierde antes del commit del incidente, lo divergente se pierde con ella, y la secuencia vuelve a ser la `4b` —desenlace 4—. Es la limitación aceptada de §2.6.9, y la cuarentena no la levanta |
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
BLOQUEA            transacción sin terminal que declara ese cuerpo como su mecanismo, un
                   dictamen en curso que lo cita como evidencia, **o un `deriva` sin reparar
                   que se apoya en la copia de lo divergente de su `conflicto`**.
                   **Mientras exista, la retirada se rechaza.**
                   **Corregido por `P-25` del documento 22.** Este disparador decía «una
                   **reconciliación abierta** que se apoya en la copia de lo divergente», y
                   **`D64` retiró esa ruta**: `reconciliacion-preparada` y `reconciliada` no
                   existen, y `X47` exige que toda mención de lo retirado esté marcada.
                   `[HISTÓRICO]` — *«una reconciliación abierta que se apoya en la copia de
                   lo divergente»*, redacción anterior a `D64`, conservada aquí como lo que
                   fue y **no vigente**. El disparador vigente es el `deriva` sin reparar,
                   que es la pieza que heredó ese papel

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

9  AUTORIDAD Y MOTIVO        ambos obligatorios, con los cinco CAMPOS de procedencia de
                             §3.6 — no los cinco conceptos, que incluyen uno derivado. Retirar
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

**No son filas de la tabla adversarial de §2.6.7**, que queda en **cuarenta y seis filas y
cuarenta y seis identificadores `X<nn>`**, tras las tres que `I-01` e `I-02` obligaron a
añadir y la que `J-03` obliga a añadir ahora (`X62`). Éstas verifican la semántica de lápida e identidad,
llevan letra en vez de número, y son contrato de prueba igual que aquéllas.

| | escenario | resultado exigido |
|---|---|---|
| `X-A` | lápida y sellado coinciden, y **el cuerpo original NO está disponible** | **NIVEL 1 válido** —orden y referencias se recorren hasta el ancla— · **NIVEL 2 válido** —el compromiso coincide en los dos sitios— · **NIVEL 3 NO alcanzable**: identidad y contenido originales **no se verifican completamente**, y el sistema lo DECLARA en vez de afirmar integridad histórica completa |
| `X-B` | se recupera el cuerpo desde el `localizador` declarado | su huella casa con `hash_cuerpo_original`, `EV-H(evento MENOS id)` sobre el cuerpo recuperado reproduce el `id_original`, y la **verificación completa se supera** |
| `X-C` | se aporta un cuerpo INCORRECTO | **verificación FALLIDA**, nombrando qué no casa: la huella, el `id` recomputado, o los dos. No se acepta «se parece» |
| `X-D` | sellado y lápida declaran `hash_cuerpo_original` o `id_original` DISTINTOS | **verificación FALLIDA.** Es inconsistencia interna del repositorio, y se escala: ninguno de los dos puede darse por bueno |
| `X-E` | un evento posterior mantiene **sólo una referencia estructural** `predecesor` al evento que se quiere retirar | la retirada **PUEDE autorizarse** si se cumplen las demás condiciones. El `id` se conserva en la lápida, la referencia sigue resolviendo y el orden sigue recorriéndose |
| `X-F` | existe una **dependencia semántica viva** que necesita leer el cuerpo —una reparación que debe reproducir su `contenido`, **un `deriva` sin reparar apoyado en la copia de lo divergente de su `conflicto`**— · **`[HISTÓRICO]`** decía «una reconciliación abierta apoyada en su copia de lo divergente», y `D64` retiró esa ruta: corregido por `P-25`, y esta fila es contrato de prueba que F6 debe construir, luego enumeraba un disparador inalcanzable | **retirada BLOQUEADA**, nombrando quién depende y por qué. En la duda sobre el tipo de referencia, bloquea |
| `X-G` | se intenta retirar **antes de sellar**, o **sin prueba de recuperación comprobada** | **retirada BLOQUEADA** en los dos casos. Sin sellado no hay ancla; sin prueba de recuperación la retirada es una pérdida disfrazada de operación |
| `X-H` | pasar el validador sobre un evento con lápida | **NO aplica la fórmula ordinaria de identidad al contenido de la lápida.** Detecta `cuerpo_retirado: true`, cambia al algoritmo B de §2.8 punto 4bis, y valida estructura y vínculo con el sellado. Aplicar `EV-H` a la lápida y reportar «id no coincide» es un **defecto del validador** |

> **Ninguna se ha ejecutado**, como las cuarenta y seis de §2.6.7. Las nueve `RC-1`–`RC-9`
> **ya no existen**: `D64` las retiró con la ruta de reconciliación, y contarlas entre lo
> escrito y no ejecutado era contar dos veces algo que ya no está.
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
                         formato de línea; el CONTRATO —se añaden y no se editan, con la
                         única excepción de la lápida (§2.9); id único; nunca se
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
fase          preparada | confirmada | conflicto | abandonada | derivada | — (sin
              transacción). El autómata, en §2.6.1. **`fase` y `tipo` son DOS EJES**, y
              **QUIÉN toma el valor `—` lo dice LA MATRIZ DE ABAJO, columna «¿puede existir
              SIN `fase`?», que es su sede: esta línea REMITE a ella y no la enumera aparte**
              —regla de titulares de §0—. Enumerarla aquí es lo que hacía que un esquema
              derivado LITERALMENTE de esta línea **rechazase un `orden` sin `fase`**, que es
              el caso que `D59` declaró legítimo y que la matriz declara «SÍ, y sólo
              entonces»; y es la misma clase que `J-01`/`D96`, invertida. Lo que sí se dice
              aquí, porque es la forma de la regla y no su censo: `sellado`, `deriva` y
              `fallo` lo toman **SIEMPRE**; `orden` lo toma **CUANDO Y SÓLO CUANDO** su
              consumo no produce ninguna escritura canónica; los demás **nunca**.
              `reconciliacion-preparada` y `reconciliada` NO existen: `D64` las retira.
              `abortada` NO existe: un evento con esa fase es RECHAZADO por el ESQUEMA
              ESTRUCTURAL — es un valor fuera del enum, y eso se ve sin salir del evento
tx            TX-<huella>, cuando el evento forma parte de una transacción multiarchivo.
              Lo comparten todos los eventos de esa transacción y nadie más
orden         posición dentro de su transacción. Total dentro de ella
predecesor    el evento que este emisor observó como último. Forma la cadena verificable
ordenante · autoridad · escritor_del_comando · ejecutor · actor_atribuido
              ver el bloque de PROCEDENCIA de abajo. **NO son «los cinco conceptos de a.9»
              a secas**: `a.9` los enumera como PROPIETARIO DEL CAMPO · AUTORIDAD ·
              ORDENANTE · ESCRITOR DEL COMANDO · EJECUTOR DE MUTACIÓN, y `actor_atribuido`
              pertenece a otra lista suya. No todos son campos: uno se DERIVA
base          hash de las entradas sobre las que se decidió
revision_base la REVISIÓN PUBLICADA Y CONSISTENTE desde la que parte la transacción: el
              `HEAD` del punto 2 de la condición de arranque 5 (§2.5). **OBLIGATORIO en
              `preparada`**; se registra o se referencia de forma comprobable en
              `conflicto` y en `abandonada`. **NO es `base`**: `base` es la huella de las
              ENTRADAS sobre las que se decidió —qué se leyó para decidir—, y
              `revision_base` es el PUNTO DEL HISTORIAL contra el que se restaura y se
              verifica byte a byte. Un mismo `revision_base` admite muchas `base`
              distintas, y una misma `base` puede evaluarse desde dos revisiones. **Entra
              en el cómputo de `tx`** (§2.8). Es `D96`
```

> **Añadido por el gate definitivo independiente (`J-01`, BLOQUEANTE; es `D96`).**
> `revision_base` era **condición 5 de arranque** (§2.5), **ancla exacta de la
> restauración** (§2.6.9), **lo que hace alcanzable `abandonada`** —«INALCANZABLE hasta
> haber RESTAURADO todas sus rutas a `revision_base` y haberlo verificado byte a byte»— y
> el sostén de «`main` nunca contiene estado parcial» y de la rama REVERTIR de `PN-7`. Y
> **no aparecía ni una vez en §3.6**, que es el contrato del evento: un esquema derivado
> literalmente de esta sección **aceptaba un `preparada` sin él**. Lo introdujo `D69` sin
> propagarlo aquí. Es la clase exacta de `A1` —un esquema derivado de §3.6 que no casa con
> lo que §2 exige—, invertida: allí RECHAZABA lo que debía aceptar, aquí ACEPTABA lo que
> debía rechazar.

### La PROCEDENCIA: qué es concepto, qué es campo y qué se deriva

> **Corregido por la tercera revisión independiente (`G1`; es `D66`).** F4 llamaba «los cinco
> conceptos de `a.9`» a un conjunto que **sustituía `propietario del campo` por
> `actor_atribuido`** —que en `a.9` pertenece a otra lista, la de cuatro elementos— y lo
> presentaba como los cinco «sin confundirlos», que es literalmente lo que `a.9` advierte que
> no debe hacerse. Verificado contra `a.9` y contra
> `kernel/operativo/recorrido/00-OBLIGACIONES-Y-CIERRE.md`, que lo cita igual. No era una
> imprecisión de redacción: esa lista era **el conjunto de campos obligatorios de todo
> evento**, y F6 habría construido el esquema sobre un conjunto que su fuente no respalda.

**Los CINCO CONCEPTOS, citados como `a.9` los escribe:**

```text
PROPIETARIO DEL CAMPO   de qué parte del estado forma parte
AUTORIDAD               quién tiene derecho a decidir su valor
ORDENANTE               quién emitió esta orden concreta
ESCRITOR DEL COMANDO    quién escribió físicamente el texto de la orden
EJECUTOR DE MUTACIÓN    quién aplicó el cambio al estado canónico
```

**Y la distinción que faltaba: concepto no es campo.** `a.9` exige que los cinco **se puedan
atribuir sin confundirse**; no exige que los cinco se persistan en cada evento:

| concepto | ¿se persiste en el evento? | por qué |
|---|---|---|
| **propietario del campo** | **NO: SE DERIVA** | es la fila de la matriz de fuentes de verdad (§1.3) a la que pertenece cada ruta de `afecta[]`. Persistirlo sería una segunda verdad editable sobre lo que §1.3 ya fija, y `I5` lo prohíbe |
| **autoridad** | **SÍ**, campo `autoridad` | puede desviarse de la que §1.3 declara por defecto, y esa desviación hay que registrarla |
| **ordenante** | **SÍ**, campo `ordenante` | no es derivable de nada: es quién pidió ESTA mutación |
| **escritor del comando** | **SÍ**, campo `escritor_del_comando` | idem, y es lo que distingue al Owner que escribe de la capacidad que transcribe |
| **ejecutor de mutación** | **SÍ**, campo `ejecutor` | `R5` lo hace único hoy, y persistirlo es lo que permite auditar que lo fue |

```text
Y ADEMÁS, DECLARADO       `actor_atribuido`, campo OBLIGATORIO. **NO es uno de los cinco**:
APARTE Y CON SU MOTIVO    pertenece a la otra lista de `a.9` —«a quién se imputa el cambio»—
                          y se conserva porque «quién lo aplicó» y «a quién se le imputa»
                          pueden diferir, que es justo lo que esa lista existe para separar.
                          Llamarlo «uno de los cinco» era la cita falsa que `G1` señaló.

CINCO CAMPOS, Y UN        `ordenante` · `autoridad` · `escritor_del_comando` · `ejecutor` ·
DERIVADO                  `actor_atribuido` son CAMPOS. **Propietario del campo se DERIVA**
                          de §1.3, y por eso el evento no lo lleva.

QUÉ COMPRUEBA `X39`       que los CINCO CAMPOS estén presentes, y que el propietario del
                          campo sea DERIVABLE para toda ruta de `afecta[]`. La ausencia de
                          cualquiera de los cinco campos es un fallo del validador; que una
                          ruta no tenga fila en §1.3 es un fallo de la matriz, y se reporta
                          como tal.

QUÉ SÓLO EXISTE PARA      `escritor_del_comando` puede COINCIDIR con `ordenante` fuera del
LAS ÓRDENES DEL TABLERO   canal de órdenes, y entonces se registra igual: coincidir no es lo
                          mismo que no existir, y por eso no se omite.

NADA SE DUPLICA, Y LA     el propietario del campo NO se copia en el evento, luego no hay dos
TRAZABILIDAD NO BAJA      sedes editables para lo mismo. Se DERIVA de una fuente única en vez
                          de repetirse en cada uno de los miles de eventos del diario.
```

### Las DOS dimensiones, y la matriz que las cruza

> **Añadido por la segunda corrección técnica (hallazgo `H3`, GRAVE).** El contrato de
> abajo cubre el eje `fase` —**cinco** fases más `deriva` y `fallo`, **siete** filas— y se resumía
> como *«las ocho formas de evento»*. Pero el enum de `tipo` tiene **NUEVE** valores, y
> **siete de ellos quedaban sin contrato**: nada decía si un `sellado` lleva `fase`, si un
> `fallo` puede llevar `tx`, ni qué declara un `certificacion` además de su fase. Declarar
> «ocho formas» con formas válidas sin contrato es un recuento que no cierra. Es `D57`.
>
> **Y `D57` se quedó a medias, que es lo que `D59` corrige.** Contó **las filas de una tabla
> como si fueran valores del eje `fase`** —`deriva` y `fallo` son valores de `tipo`—, y dio
> por obligatoria la transacción de `orden` **sin demostrarla tipo a tipo**. `orden` es
> **condicional**. `D57` y `D59` conservan su texto.
>
> **Y los tres recuentos se recalculan una vez más, porque `D64` movió el sustrato** (`A6`;
> es `D85`). `D59` fijó «seis fases, siete estados, ocho filas» cuando el autómata tenía
> seis fases; `D64` colapsó la ruta de conflicto y lo dejó en **cinco**, y los tres números
> se quedaron atrás. Derivados del enum vigente:
>
> ```text
> FASES                    5   preparada · confirmada · conflicto · abandonada · derivada
> ESTADOS DEL CAMPO        6   las cinco, más la AUSENCIA del campo
> FILAS DE LA TABLA        7   las cinco fases, más `deriva` y `fallo`, que NO son fases
> ```

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
| `fallo` | la OPERACIÓN NO CANÓNICA que falló, declarada en `sujeto` y `operacion` | **REPORTA** que esa operación falló, con su causa, su estado observado, si es recuperable y qué autoridad hace falta. **No repara** | **no**: sólo se escribe a sí mismo | — | **no** | **SIEMPRE, y es obligatorio** | el push es rechazado porque el remoto avanzó (`W15`), con `tx_afectada` y `referencias[]` |

**Los casos que la prueba obligó a separar, dichos uno a uno — todos los que el bloque de abajo
rotula, y el cardinal no se escribe:**

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

FASES TRANSACCIONALES           5   preparada · confirmada · conflicto ·
                                    abandonada · derivada
                                    `deriva` y `fallo` NO SON FASES: son valores de `tipo`

ESTADOS DEL CAMPO `fase`        6   las CINCO fases, más la AUSENCIA del campo. La ausencia
                                    no es un sexto valor del enum: es que el campo no está

ESPACIO BRUTO                  54   9 × 6, y la mayor parte NO es válida

LOS TRES REGÍMENES             SIEMPRE TRANSACCIONAL      5   transicion · integracion ·
                                                              certificacion · migracion ·
                                                              retirada-de-cuerpo
                               CONDICIONAL                1   orden
                               SIEMPRE NO TRANSACCIONAL   3   sellado · deriva · fallo

COMBINACIONES VÁLIDAS          34   5 tipos SIEMPRE transaccionales × 5 fases  = 25
                                    `orden`, CONDICIONAL: 5 con fase + 1 sin   =  6
                                    `sellado` sin fase                         =  1
                                    `deriva` sin fase                          =  1
                                    `fallo` sin fase                           =  1

COMBINACIONES PROHIBIDAS       20   los 5 siempre transaccionales SIN fase      =  5
                                    `sellado` con cualquiera de las 5 fases     =  5
                                    `deriva` con cualquiera de las 5 fases      =  5
                                    `fallo` con cualquiera de las 5 fases       =  5
                                    34 + 20 = 54, y la partición cierra
```

> **Lo que se retira, dicho en positivo.** «Las ocho formas de evento» contaba **mezclando
> ejes** —metía `deriva` y `fallo` en el eje `fase`—; «`7 × 6 + 2 = 44`» daba por obligatoria
> una transacción para `orden` sin demostrarlo; y «`45`» seguía dando por transaccional un
> `sellado` que sólo añade un fichero. Y `D64` retira dos fases con la ruta de conflicto.
> **Las fases son CINCO**, `deriva`, `fallo` y `sellado` son valores de `tipo` **sin** fase, y
> `orden` es condicional. El recuento vigente es **34 · 20 · 54**, y se **deriva** de la tabla
> de arriba: no se conserva ninguno por arrastre.

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
`tx_afectada` CON `causa: sin-transaccion`, o SU     ESQUEMA ESTRUCTURAL: el enum de tres
AUSENCIA con las otras DOS causas                 valores y su condicional viven en §3.6
UN EVENTO CON `fase` CUYO `tx` YA TIENE           VALIDADOR SEMÁNTICO DEL DIARIO: exige
`derivada`                                        recorrer los demás eventos de ese `tx`
DOS `conflicto` CONSECUTIVOS CON EL MISMO         VALIDADOR SEMÁNTICO DEL DIARIO: exige
CONJUNTO DE HASHES OBSERVADOS · UNA               comparar los `conflicto` de ese `tx`
`observacion` NO CONSECUTIVA · UN `abandonada`    entre sí, y RECORRER el diario buscando
AL QUE NINGÚN `deriva` REFERENCIA POR              el `deriva` que apunta al `abandonada`
`abandonada_id`                                    (`D105`: la referencia va del `deriva` al
                                                   `abandonada`, no al revés)
```

**No se crea ningún tipo, y no se fusiona ninguno.** La prueba de §3.1 **no llega a
plantearse**: los nueve valores son valores de un **enum** dentro del tipo `evento`, no tipos
candidatos con sujeto, autoridad y ciclo propios. El recuento de §3.8 **no cambia**.

### El contrato condicional, fase a fase

> **Qué cubre esta tabla, y qué NO.** Sus **cinco primeras filas son las cinco FASES**. Las
> dos últimas —`deriva` y `fallo`— **no son fases**: son los dos valores de `tipo` que nunca
> la llevan, y están aquí porque sin ellos el contrato del evento quedaría incompleto. **La
> tabla tiene SIETE filas y el eje `fase` tiene CINCO valores**, y confundir las dos cosas es
> lo que `D59` corrige y `D85` recuenta tras `D64`. Un evento válido cumple **su fila de tipo** en la prueba de arriba
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
| `preparada` | ninguna: abre la transacción | `afecta[]` con `ruta`·`hash_previo`·`hash_posterior_esperado`·`orden`· una de `contenido`\|`parche`\|`operacion` · **los CINCO CAMPOS de procedencia** —`ordenante`·`autoridad`·`escritor_del_comando`·`ejecutor`·`actor_atribuido`—, **no «los cinco conceptos de `a.9`»**: el quinto concepto, `propietario del campo`, **se DERIVA** de §1.3 y no es campo · `base` · **`revision_base`** —la revisión publicada y consistente desde la que parte la transacción; su ausencia hace el evento INVÁLIDO, y es lo que hace verificable la restauración de §2.6.9 y alcanzable `abandonada` (`D96`)— | `resultado` · `hash_observado` · `hash_final` · `decision` | `hash_posterior_esperado` | los N ficheros casan con su hash posterior → `confirmada`; alguno diverge → `conflicto` |
| `confirmada` | `preparada` | `resultado` · `derivados_pendientes[]` | `decision` · `hash_final` · `hash_observado` | `hash_posterior_esperado` | los derivados de `derivados_pendientes` se regeneraron → `derivada` |
| `conflicto` | `preparada` o `conflicto` | `divergentes[]` con `ruta`·`hash_observado`· **`contenido` íntegro de lo divergente** · `items[]` · `rutas[]` · `autoridad` que debe resolver · `observacion` ≥ 1 · **`revision_base`, registrado o referenciado al `preparada` de su `tx`** (`D96`) | `resultado` · `decision` | ninguno: declara lo observado, no lo esperado | la divergencia CESA y los N ficheros vuelven a casar → `confirmada`; la autoridad decide cerrar → `abandonada`. **Siempre hay una de las dos** |
| `abandonada` | `conflicto` | `estado_observado[]` con `ruta`·`hash_observado`·`clasificacion` ∈ {previo, posterior, divergente} **para TODAS las rutas del `tx`** · `autoridad` que decidió · `motivo` · **`revision_base`, registrado o referenciado al `preparada` de su `tx`: es la revisión CONTRA LA QUE se verificó byte a byte la restauración, y sin ella la restauración no es comprobable** (`D96`) | `resultado` · `derivados_regenerados` · `decision` · **`deriva_emitida`, PROHIBIDO desde `D105`: era la referencia circular de `M-02`, y ahora el `deriva` referencia al `abandonada` y no al revés** | ninguno: la transacción no alcanza ningún resultado | **ninguna. Es TERMINAL.** El marcador de transacción **NO se retira aquí**: se retira cuando el `deriva` es DURABLE y su marcador EXISTE (§2.6.9 paso E) — **precisado por `P-09`**, que el marcador del `deriva` es NO EXIGIDO en §2.6.6 y se reconstruye desde el diario (§2.9, `X60`). El bloqueo pasa al `deriva` que la referencia por `abandonada_id` |
| `derivada` | `confirmada` | `derivados_regenerados[]` con su `source_revision` · `resuelve_deriva` sólo si esta transacción repara uno | `afecta` · `decision` · `divergentes` | el `hash_posterior_esperado` de su `preparada` | **ninguna. Es TERMINAL**, y retira el marcador. Que no exista ningún evento posterior con ese `tx` lo comprueba el **validador semántico del diario**, no el esquema |
| `deriva` | **ninguna: NO tiene `tx` ni `fase`** | **`causa`, ENUM CERRADO DE TRES VALORES y ÉSTA ES SU ÚNICA SEDE** ∈ {`posterior-al-cierre`,`sin-transaccion`,`abandono-de-transaccion`} · `afecta[]` con `ruta`·`hash_esperado`·`hash_observado` · `items[]` · `autoridad` · `tx_afectada` **obligatorio si `causa` ∈ {`posterior-al-cierre`,`abandono-de-transaccion`} y PROHIBIDO con `sin-transaccion`** · **`abandonada_id` = `id` del evento `abandonada` del que deriva, OBLIGATORIO con `causa: abandono-de-transaccion` y PROHIBIDO con las otras dos. Es la referencia UNILATERAL de `D105`: apunta a un evento que YA existe y es durable, luego su `id` es calculable** | `fase` · `tx` · `decision` · `resultado` | ninguno: **reporta**, no repara | ninguna. La reparación es una transacción NUEVA (§2.6.11) |
| `fallo` | **ninguna: NO tiene `tx` ni `fase`** | `sujeto` · `operacion` ∈ {`push`,`publicacion`,`arranque`,`ci`,`proyeccion`} · `causa` · `estado_observado` · `diagnostico` · `intentos` · `recuperable` ∈ {`si`,`no`,`requiere-decision`} · `autoridad_requerida` · `accion_siguiente` · `evidencia` · **`tx_afectada` como REFERENCIA, cuando la operación se refiere a una** · `referencias[]` con `commit`·`rama`·`remoto` cuando la operación es Git | `fase` · `tx` · `afecta` · `decision` | — | ninguna. **Es informativo y NO repara**: si hay que reparar, es una transacción nueva |

### `fallo` — una semántica CERRADA, no un contenedor genérico

> **Corregido por la tercera revisión independiente (`G3`; es `D66`).** El contrato de `fallo`
> tenía tres campos obligatorios y **prohibía `tx`**, mientras cuatro pasajes normativos y dos
> filas adversariales le exigían **nombrar un `tx` y un commit**: la garantía 6 de §2.6.6, el
> paso 1 de §2.6.4, `W16`, `X15` y `X28`. `X15` y `X28` **no eran satisfacibles** contra el
> contrato vigente. `deriva` había recibido `tx_afectada` justamente para referenciar una
> transacción sin pertenecer a ella; a `fallo` no se le dio el equivalente.

```text
SUJETO                 `sujeto`: qué operación concreta falló, nombrada. NO «algo salió mal»

OPERACIÓN              `operacion`, ENUM CERRADO: `push` · `publicacion` · `arranque` · `ci`
                       · `proyeccion`. Un valor fuera del enum es un evento inválido, y
                       añadir uno es una decisión, no una improvisación

FASE                   NINGUNA, y `tx` PROHIBIDO. `fallo` no pertenece a ninguna transacción

`tx` RELACIONADA       `tx_afectada`, **REFERENCIA y no pertenencia**, exactamente como en
                       `deriva`. Presente cuando la operación se refiere a una transacción:
                       el push que la publicaría, el marcador clonado que la delata

CAUSA Y ESTADO         `causa` y `estado_observado`: por qué falló y qué se vio. Para Git,
OBSERVADO              `referencias[]` con `commit`, `rama` y `remoto`

RECUPERABILIDAD        `recuperable` ∈ {`si`, `no`, `requiere-decision`}. Es lo que distingue
                       un reintento legítimo de un escalado

AUTORIDAD Y ACCIÓN     `autoridad_requerida` y `accion_siguiente`. Un fallo que no dice quién
SIGUIENTE              lo desbloquea ni qué sigue no es un registro: es un lamento

EVIDENCIA              `evidencia`: referencia al artefacto que lo demuestra —salida del
                       comando, informe de CI, diagnóstico del arranque—

TERMINALIDAD           `fallo` es TERMINAL en sí mismo: no encadena. Repetir el intento emite
                       OTRO `fallo`, con su `intentos` incrementado

RELACIÓN CON LOS       `conflicto`  divergencia DENTRO de una transacción abierta. Es fase
DEMÁS                  `deriva`     estado canónico que dejó de sostener el diario. Sin fase
                       `fallo`      una operación NO CANÓNICA que no se completó. Sin fase
                       Los tres REPORTAN y ninguno repara. Lo que los separa es QUÉ falló:
                       un fichero en vuelo, un fichero ya cerrado, o una operación que nunca
                       tocó el estado canónico. **Ninguno es contenedor de los otros.**
```

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
  por la matriz de §3.6; que `deriva`, `fallo` y `sellado` no lleven `fase` ni `tx`; que un
  `conflicto` lleve `divergentes[].contenido`; que una `abandonada` lleve `estado_observado[]`
  para TODAS las rutas, `autoridad` y `motivo` —**y NO `deriva_emitida`, que `D105` prohíbe
  en esta fase**—; que en `deriva` el `tx_afectada` aparezca con `causa: posterior-al-cierre`
  o `abandono-de-transaccion` y NO con `sin-transaccion`, y que **`abandonada_id` aparezca
  con `abandono-de-transaccion` y NO con las otras dos** —el enum de TRES valores lo declara §3.6, sede única—;
  y que un `fallo` con `operacion` ∈ {`push`,`publicacion`} lleve `referencias[]`
· UNICIDAD DE `ruta` dentro del array del propio evento, y `orden` total dentro de él
· QUÉ ALGORITMO DE IDENTIDAD APLICAR, antes de aplicarlo: si el evento lleva
  `cuerpo_retirado: true` es una LÁPIDA, y **NO se le aplica `EV-H(evento MENOS id)`** —la
  preimagen ya no está—; se valida su estructura (§2.9). Sobre un evento íntegro sí se aplica
  y debe reproducir su `id`. Confundirlos es el defecto que `X-H` comprueba (§2.8, 4bis)
· EL CONTADOR DE OBSERVACIÓN, en lo que se ve sin salir del evento: `observacion` ≥ 1 y
  entero. **No hay tope** que comprobar: `D64` retira los contadores de intentos con la ruta
  que los usaba. Lo que NO ve: si esa `observacion` es la siguiente de su `tx`, ni si los
  hashes observados cambiaron — eso es del validador del diario
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
· CONTINUIDAD DE HASHES entre fases: que `derivada` cierre sobre el `hash_posterior_esperado`
  que su `preparada` declaró, y que ninguna transacción sustituya su intención a mitad
· NINGUNA FASE POSTERIOR A UN TERMINAL en ese `tx` —`derivada` **o** `abandonada`—.
  **Ésta es la regla 1**, y es de diario
· **EL PREDICADO `abierta(tx)` SE EVALÚA AQUÍ, Y NO SE REDECLARA.** Su enunciado tiene UNA
  sede, §2.6.1, y esta capa lo EJERCE: ninguna regla de esta lista vuelve a escribir la
  condición con otras palabras. `D71` designó esta capa como evaluadora (§2.6.1); `D89`
  retira las dos reglas que la contradecían
· OBSERVACIONES: `observacion` empieza en 1, es consecutiva dentro de su `tx`, y cada
  `conflicto` declara un conjunto de hashes observados **DISTINTO** del anterior — repetir lo
  mismo es una NO-OPERACIÓN (§2.8). No hay tope que comprobar. **Esto no lo ve un esquema**:
  exige comparar los `conflicto` de ese `tx` entre sí
· TERMINALIDAD, sobre el ÚNICO PREDICADO de §2.6.1: toda transacción **cerrada** —esto es,
  `¬abierta(tx)` con `preparada` durable— tiene **exactamente UN terminal, y es `derivada` o
  `abandonada`**; toda transacción **abierta** no tiene ninguno. **Corregido por el gate de
  cierre (`I-03`; es `D89`)**: decía «exactamente un `derivada` por transacción cerrada», y
  una cerrada por `abandonada` tiene **cero** `derivada` — un validador construido de esa
  frase habría rechazado toda transacción abandonada. Era el residuo exacto de `A2` en la
  única capa que evalúa el predicado
· CORRESPONDENCIA ENTRE INTENCIÓN Y HECHO: que todo `confirmada` tenga su `preparada`, y
  todo `abandonada` su `conflicto`, y que las rutas y hashes coincidan
· CARDINALIDAD DE CADA FASE, **CONDICIONAL A CÓMO CERRÓ** (§2.6.4): `preparada` exactamente 1
  siempre; `derivada` y `abandonada` **mutuamente excluyentes**, y toda transacción cerrada
  tiene exactamente uno de los dos; `confirmada` 1 si completó y 0 si se abandonó. **Ninguna
  secuencia contiene `confirmada → confirmada`.** Sólo `conflicto` se repite, con
  `observacion` como discriminador y **sin tope**
· TODO ESTADO NO TERMINAL TIENE SUCESOR ADMISIBLE: ninguna transacción con `preparada` durable
  puede quedar sin terminal alcanzable. Es la comprobación que `B1` exigía, y vive aquí
  porque exige recorrer el `tx` entero
· TODO `abandonada` TIENE **EXACTAMENTE UN** `deriva` QUE LO REFERENCIA POR
  `abandonada_id`, y ese `deriva` existe en el diario y nombra las mismas rutas e items.
  **La referencia es UNILATERAL y va del `deriva` al `abandonada`** (`D105`): el `abandonada`
  **NO declara `deriva_emitida`** —está PROHIBIDO en §3.6—, y la forma del evento la fija
  §3.6, que es su sede; esta capa la VALIDA y no la redefine. La unicidad se comprueba por
  `abandonada_id` **antes de emitir**, en el paso 0 de §2.6.4.
  **Corregido por `P-02`≡`Q-06`**: esta regla conservaba el verbo anterior a `D105` —«TODO
  `abandonada` DECLARA SU `deriva`»— en la lista que `D89` acababa de barrer, mientras la
  tabla de las cuatro reglas y §3.6 ya decían lo contrario. Quien construyera la capa B desde
  esta lista implementaba el puntero desde el `abandonada`, que es exactamente lo que hacía
  inemitible el segundo terminal
· LÁPIDA Y SELLADO, VINCULADOS: para todo evento con `cuerpo_retirado: true`, el sellado que
  lo ancla declara el MISMO `id_original`, `hash_cuerpo_original`, `fase`, `tx` y posición.
  Una discrepancia es un fallo (`X-A`–`X-D`), y comprobarla exige abrir DOS ficheros: por eso
  es de esta capa y no del esquema
· QUÉ NIVEL DE GARANTÍA SE ALCANZA, declarado y no supuesto: con lápida y sin cuerpo original
  disponible, NIVEL 1 y NIVEL 2 sí, **NIVEL 3 no** — y el validador lo REPORTA en vez de
  afirmar integridad histórica completa (§2.9)
· LA IDENTIDAD DE LA RUTA: cada `conflicto` de un `tx` declara un conjunto de hashes
  observados DISTINTO del anterior, y su `observacion` es consecutiva desde 1. **No hay nada
  más que contar.** **Corregido por el gate de cierre (`I-03`; es `D89`)**: la regla decía
  «#observaciones = #intentos» y clasificaba una ruta «AGOTADA» con `agotado: true` — y `D64`
  retiró `intentos_consumidos`, `intento` y `agotado`, y con ellos la ruta agotada. Era una
  regla **inconstruible**: exigía contar un campo que el esquema no tiene y clasificar una
  ruta que el autómata no admite
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
| 3 | ninguna `abandonada` sin `estado_observado[]` de TODAS las rutas · y **ninguna `abandonada` sin EXACTAMENTE UN `deriva` que la referencie por `abandonada_id`** | **A** la presencia y la forma del `estado_observado[]` · **B** que exista uno y sólo un `deriva` con ese `abandonada_id`, y que nombre las mismas rutas | la presencia es del evento; la correspondencia se comprueba **recorriendo el diario en busca del `deriva` que apunta**, no siguiendo un puntero desde el `abandonada`. **Invertido por `D105`**: el sentido anterior exigía al `abandonada` un campo cuyo valor no podía existir cuando se calculaba su propio `id` |
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

> **Corregido por la tercera revisión independiente (`G8`; es `D68`).** F4 declaraba doce
> áreas y **no eran las doce del `§5.18`** que `O8` resuelve: **eliminaba «mapa documental»**
> —el punto 1 del núcleo obligatorio— y **partía «arquitectura actual y dirección
> arquitectónica» en dos**. El número doce se conservaba; el conjunto no. Y `grep` sobre todo
> el repositorio devolvía **una sola aparición** de «mapa documental», en `§5.18`: F4 no lo
> mencionaba ni para conservarlo, ni para retirarlo, ni para declararlo derivado. La
> consecuencia era material: cada área es un `contrato-de-aspecto:documental/<area>`, luego
> F6 habría construido doce contratos para las áreas equivocadas.

**LAS DOCE ÁREAS OBLIGATORIAS, alineadas literalmente con `§5.18`, CON SU IDENTIFICADOR:**

> **Añadidos los identificadores por el gate final independiente (`G-4`, GRAVE; es `D77`).**
> Las doce materias estaban enumeradas y **ninguna tenía identificador declarado**, mientras
> §5.7 afirma que cada una resuelve a un `contrato-de-aspecto:documental/<area>` y el único
> ejemplo existente usaba `arquitectura-actual` — la mitad partida que `D68` había retirado.
> F6 habría tenido que inventarse doce, y dos productos habrían inventado doce distintos.
>
> **No se crea ninguna sede nueva.** Los identificadores **se derivan del patrón que ya
> existe**: `esquemas/memoria.yaml` fija `id: {tipo: texto, patron: '^memoria:[a-z0-9-]+$'}`
> con `nombre`, `capacidad`, `autoridad`, `caducidad` y `vacio_significa`, y el corpus tiene
> **doce ejemplares trabajados** de ese patrón. El slug es el mismo: minúsculas, guiones, sin
> tildes. Lo único nuevo es el prefijo de familia, `documental/`, que §3.5 ya separó.

```text
 #  área de `§5.18`                              identificador de aspecto
 1  mapa documental                              aspecto:documental/mapa-documental
 2  identidad y dirección de producto            aspecto:documental/identidad-de-producto
 3  baseline funcional                           aspecto:documental/baseline-funcional
 4  dominio y glosario                           aspecto:documental/dominio-y-glosario
 5  arquitectura actual y dirección              aspecto:documental/arquitectura
    arquitectónica  ← UNA área, no dos           ← UN identificador, no dos
 6  tecnologías e instrucciones de desarrollo    aspecto:documental/tecnologias-y-desarrollo
 7  dirección de ingeniería                      aspecto:documental/direccion-de-ingenieria
 8  calidad y pruebas                            aspecto:documental/calidad-y-pruebas
 9  seguridad y riesgos                          aspecto:documental/seguridad-y-riesgos
10  despliegue, entornos y operación             aspecto:documental/despliegue-y-operacion
11  decisiones                                   aspecto:documental/decisiones
12  dirección de evolución y gaps documentales   aspecto:documental/evolucion-documental

CADA UNO RESUELVE A       `contrato-de-aspecto:documental/<area>` (§5.7), con el mismo
                          reparto de campos del patrón `ads:memoria`: responsable POR
                          DEFECTO, criterio, pruebas, caducidad y triggers. La celda declara
                          sólo la DESVIACIÓN, con motivo

Y LAS CONDICIONALES NO    las TRECE condicionales NO reciben identificador aquí. Dos de
LO RECIBEN AQUÍ           ellas —«dirección visual» y «sistema de diseño»— ya tienen sede
                          canónica en el sistema de diseño, y darles un
                          `contrato-de-aspecto` editable crearía la SEGUNDA SEDE que `I5`
                          prohíbe. Su contrato se DERIVA de la sede que ya las gobierna, y
                          F6 lo compila; no lo escribe a mano
```

```text
EL «MAPA DOCUMENTAL»,     es el área 1, y **es obligatoria**. Su materia: qué documentos
RESTITUIDO                existen, cuál cubre cada área, quién responde de cada uno y cuál
                          es su vigencia. Es lo que `§5.23` necesita para «detectar
                          documentos ausentes, duplicados o sin responsable».
                          **Y se declara DERIVADO**: se regenera desde los bloques
                          `ads:memoria` de los documentos gobernados y desde las celdas de
                          `cobertura` de familia documental, luego su fila en §1.3 tiene
                          autoridad «nadie: se regenera». Ser derivado NO lo saca del
                          mínimo: sigue siendo una de las doce materias exigibles, y su
                          ausencia —que no haya de dónde derivarlo— es un fallo del gate.

ARQUITECTURA, UNA         `§5.18` la enumera como UNA área. Partirla daba dos contratos de
SOLA ÁREA                 aspecto donde `O8` fija uno, con dos responsables y dos
                          caducidades para una materia que se decide junta.

COMPACTACIÓN     un documento declara VARIAS áreas en su bloque `memoria.contiene`. En un
                 producto pequeño, tres documentos pueden cubrir las doce.
PROFUNDIDAD      la exige `cobertura.aplicabilidad` por área, derivada de tamaño,
                 naturaleza y riesgo declarados en `PROFILE`.
RESPONSABLE      cada área declara su reparto POR DEFECTO en su
                 `contrato-de-aspecto:documental/<area>` (§5.7), y NO se infiere de la
                 capacidad: `SIS` responde de conformidad documental, y del CONTENIDO de un
                 área responde la capacidad de esa materia. La celda declara sólo la
                 desviación, con motivo.
CONDICIONALES    las **TRECE** que `§5.18` enumera, y son las suyas: UX e investigación,
                 dirección visual, sistema de diseño, arquitectura de datos detallada,
                 integraciones, cumplimiento regulatorio, modelo de amenazas avanzado,
                 observabilidad, continuidad, analítica, dispositivos,
                 internacionalización, gobierno de IA. Se activan por aplicabilidad.
AMPLIABLE        un producto puede declarar áreas propias, con su contrato de aspecto. Lo
                 que NO puede es quedarse por debajo de las doce obligatorias.
NO APLICABLE     con motivo registrado. Una ausencia silenciosa es un fallo del gate.
SIN DOCE         la taxonomía es de MATERIAS, no de ficheros: `O8` lo dice con esas
FICHEROS         palabras, y la compactación de arriba es lo que lo hace real.
```

**La taxonomía documental, en una tabla:**

| clase | cuántas | quién las fija | se pueden fusionar en un fichero | se pueden omitir |
|---|---|---|---|---|
| **obligatorias** | **12**, las de `§5.18` | `O8`, resolución del Owner | **sí** | **no**, y una ausencia silenciosa es fallo de gate |
| **condicionales** | **13**, las de `§5.18` | aplicabilidad declarada en `PROFILE` | sí | sí, con motivo registrado |
| **ampliaciones** | las que el producto declare | el producto, con su contrato de aspecto | sí | sí: son suyas |

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
| `calidad/ci-cd` · `calidad/despliegue` · `calidad/observabilidad` | `ENT` | `ENT` | entrega observada. **`m-3`, registrado y NO resuelto**: la misión de `PLT` nombra expresamente la observabilidad, y aquí sólo figura `ENT`. El hecho está confirmado; **convertirlo en defecto sería una preferencia de diseño**, y esta fase no la toma. Si el Owner o F6 quisieran a `PLT` como corresponsable, la vía es la misma que la de `calidad/rendimiento`: dos responsables y un `lider` |
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

QUÉ TRABAJO GENERA        una EXTENSIÓN DE FICHA en F6, nombrada fichero a fichero. **Son
                          SEIS**, no cuatro: las cuatro de las dos dimensiones huérfanas, más
                          `DSP` y `ENC` que el gate final añadió. **Este cardinal SÍ se
                          escribe, por la única razón que la regla de titulares de §0 admite:
                          `G-10` de la batería lo CONTRASTA contra las tres sedes —§5.2, §16 y
                          §17— y contra los seis nombres, y da ROJO si alguna regresa. Un
                          cardinal con comprobación que lo derive no caduca en silencio; sin
                          ella, el titular remite.** Son:
                            `capacidades/ENT/`   añadir rendimiento observado y resiliencia
                                                 a su materia declarada
                            `capacidades/ARQ/`   añadir coste de diseño y resiliencia
                                                 estructural
                            `capacidades/PLT/`   añadir cadena de suministro como aspecto,
                                                 no sólo como proceso
                            `capacidades/SEG/`   declarar su veto sobre `calidad/dependencias`
                                                 con los seis campos del contrato de veto de
                                                 `a.5`
                            `capacidades/DSP/`   **añadida por `M-5`**: autorizar la APERTURA
                                                 mecánica de items `AUD` dentro de una
                                                 política `O7` vigente. `C1` exige que la
                                                 ficha lo autorice antes de que ningún rol
                                                 pueda hacerlo
                            `capacidades/ENC/`   **añadida por `M-6`**: admitir como ENTRADA
                                                 un finding de auditoría, cuyo sujeto es una
                                                 celda de cobertura y no el Owner, y emitir
                                                 su encuadre sin pasar por el vivero

QUÉ NO GENERA             presión normativa, **y se dice ficha a ficha en vez de en bloque,
                          porque en bloque es como se quedaron dos sin declaración**:
                            `ENT` `ARQ` `PLT` `SEG`   **NO la generan.** Ninguna es (a), (b),
                                                      `E1`, `E2`, `K-1` ni `C4`, y la materia
                                                      ya está en su alcance declarado —lo
                                                      dice el bloque de arriba, capacidad a
                                                      capacidad—. Extender una ficha con
                                                      materia que ya está en su alcance es
                                                      trabajo de F6
                            `DSP`                     **NO la genera, y la razón se escribe:**
                                                      `C1` YA EXIGE que la ficha autorice la
                                                      apertura mecánica antes de que ningún
                                                      rol pueda hacerla, y §5.3 y §14 ya
                                                      norman esa apertura dentro de una
                                                      política `O7` vigente. Extender la ficha
                                                      **EJECUTA** `C1`, no lo enmienda. Lo que
                                                      F4 NO puede hacer es tocar `C1` ni la
                                                      ficha: las dos son kernel (§19)
                            `ENC`                     **NO SE DECLARA AQUÍ, Y ESO ES LO QUE SE
                                                      DECLARA.** Su extensión —admitir como
                                                      ENTRADA un finding de auditoría, cuyo
                                                      sujeto es una celda de cobertura y no el
                                                      Owner, y emitir su encuadre sin pasar
                                                      por el vivero— **cae del lado de `E1`**,
                                                      que es la enmienda de `ENC` y habla de
                                                      «trabajo real de entrada … una expresión
                                                      del Owner». Decidir si la extensión cabe
                                                      dentro del alcance de `E1` o lo estira
                                                      **exige leer `E1` COMO NORMA y
                                                      resolverlo, y esta sede no lo hace**:
                                                      queda abajo como trabajo futuro, con
                                                      propietario, fase y prueba. **Afirmar
                                                      que no hay presión sin haberlo
                                                      comprobado es exactamente el defecto que
                                                      esta corrección repara**

EL LÍMITE, DECLARADO      si al redactar la extensión F5 o F6 encontrasen que el alcance de
                          alguna de las fichas de arriba NO estira hasta el aspecto, entonces
                          SÍ nacería una presión, y se registraría ese día. Para `ENT`, `ARQ`,
                          `PLT`, `SEG` y `DSP` hoy no la hay, y afirmar que la habrá sería tan
                          poco riguroso como aparcar las dos materias. **Para `ENC` no se
                          afirma ni lo uno ni lo otro: se declara sin comprobar.**

TRABAJO FUTURO,           **`ENC` Y `E1`** · PROPIETARIO **el Owner** · FASE **F5** ·
CON PROPIETARIO,          contrastar la extensión de la ficha de `ENC` contra `E1` y decidir
FASE Y PRUEBA             si cabe en su alcance o lo estira. Si lo estira, nace una presión
                          normativa y se registra en §16 ese día. **F4 no lee `E1` como norma
                          ni la enmienda** (§19). PRUEBA POSTERIOR: que un finding de
                          auditoría entregado a `ENC` produzca un encuadre que supere
                          `gate:encuadre-listo` **sin `expresion_literal[]` del Owner**, o que
                          el gate lo rechace y quede escrito por qué. **FALLA HOY**
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
APERTURA            **`DSP`**, y sólo mecánicamente: crea un item `AUD` cuando la política
                    `O7` vigente lo determina, con la prioridad que ella fija. Si no hay
                    política vigente, PROPONE y espera. `DSP` **no decide** si auditar: la
                    política lo decidió, y `DSP` la aplica — que es la misma disciplina con
                    la que `b.15.1` le deja crear desbloqueadores «dentro del alcance ya
                    autorizado» y `b.7` le niega la autoridad semántica de cancelar.
                    **Y su ficha tiene que autorizarlo**: `C1` fija que la autoridad de un
                    rol es SUBCONJUNTO de la de su capacidad, luego nombrar a `DSP` aquí
                    exige una EXTENSIÓN DE FICHA en `capacidades/DSP/`, registrada abajo y
                    en §17. La mitad NORMATIVA —que una política de recurrencia sea fuente
                    de trabajo, tercera vía que `b.15.1` no contempla— **ya está registrada
                    como `PN-2`**, y no se resuelve aquí
      ↓
AUDITORÍA           proceso `AUD`, con la capacidad RESPONSABLE DEL ASPECTO como
                    PROPIETARIA GLOBAL derivada del encargo, e `INV` produciendo la capa
                    como su única obligatoria (§8.0, vía 1 y vía 2). Si hay varias
                    responsables, la declarada `lider` (§5.2)
      ↓
FINDINGS            en la evidencia del AUD. Todavía no son trabajo
      ↓
CLASIFICACIÓN       `ENC`, con las nueve clases de entrada y los diez procesos de `b.16`.
                    **Y con una décima clase, que hoy no existe** (`M-6`; es `D80`): todo el
                    aparato de entrada tiene UN SOLO SUJETO, el Owner —las nueve clases son
                    sobre su expresión, las catorce formas también, y `03-FORMAS` cierra su
                    algoritmo con «11 en otro caso → `forma:idea-inmadura`», que **manda al
                    vivero todo finding producido por un `AUD`**. Un hallazgo con evidencia,
                    sujeto y aspecto declarados no es una idea inmadura del Owner.
                    Lo que F6 tiene que construir, ya determinado y sin decidir nada:
                      CLASE      `entrada:finding-de-auditoria`, décima de la taxonomía
                      FORMA      `forma:finding`, decimoquinta de `03-FORMAS`
                      RAMA       una rama del algoritmo ANTES de la cláusula de cierre: si
                                 la entrada trae `sujeto`, `aspecto` y `evidencia` de una
                                 celda de cobertura, es un finding y NO cae en el vivero
                      SUJETO     no el Owner: la celda de cobertura que lo produjo
                      SALIDA     un encuadre `listo-para-dsp` con su proceso propuesto, o
                                 un descarte con motivo. Nunca una ficha de vivero
                    **Y la extensión de ficha de `capacidades/ENC/`** —cuyas cuatro entradas
                    declaradas están HOY ancladas al Owner— queda registrada abajo y en §17
      ↓
CAUSAS RAÍZ         agrupación por campo común. Veinte inputs con alturas distintas NO son
                    veinte items si la causa es un componente
      ↓
CAMPAÑA             la abre la **capacidad RESPONSABLE del aspecto** —la `lider` si hay
                    varias (§5.2)—, porque agrupar findings de su materia es juicio suyo y
                    no de `DSP`. Es una `iniciativa` de §3.3 con su gate. **`DSP` la compone
                    y la despacha**, y no decide su contenido (`b.5`, `b.7`).
                    **Y su ficha tiene que autorizarlo, igual que la de `DSP`** (`I-14`; es
                    `D91`): `C1` L118 fija que la autoridad de un rol es SIEMPRE subconjunto
                    de la de su capacidad, y **ninguna de las quince fichas menciona hoy
                    `iniciativa` ni `campaña`** —comprobado con un barrido sobre las quince—.
                    Abrir una iniciativa NO se da por implícito porque la capacidad responda
                    del aspecto: es una autoridad, y las autoridades se declaran.
                    **QUÉ TRABAJO GENERA, y es de F6**: una EXTENSIÓN DE FICHA por cada
                    capacidad que pueda ser LÍDER DE COBERTURA, autorizándole abrir una
                    `iniciativa` de campaña sobre los aspectos de los que responde.
                    **EL CONJUNTO NO SE ESCRIBE A MANO**: se DERIVA de los
                    `contrato-de-aspecto` (§5.7) —la capacidad `lider` de cada aspecto, o la
                    única responsable cuando hay una sola—, exactamente como el reparto por
                    defecto vive allí y no aquí. Escribirlo a mano crearía la segunda sede
                    editable que `I5` prohíbe, y quedaría desactualizado en cuanto un aspecto
                    cambiara de líder. Registrado en §17 y en §19
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

> **`responsables` NO APARECE EN NINGUNA DE LAS TRES CELDAS DE ABAJO, y es a propósito.**
> **Corregido por `P-20` del documento 22.** Las tres lo escribían —`[DIS]`, `[ARQ, SIS]`,
> `[PLT, VER]`—, y **los tres valores eran exactamente el reparto POR DEFECTO**, sin `motivo`.
> Contra el contrato que estas celdas existen para demostrar: §3.5 —«`responsables` **la
> DESVIACIÓN** respecto al reparto por defecto, **cuando la hay**, **con su motivo**»—, §5.7
> —«es la NORMA; la celda declara sólo la DESVIACIÓN, con motivo»— y §9.2 —«SÓLO LA
> DESVIACIÓN … con su motivo»—. Con el esquema tal como §3.5 lo define, **`X52` tendría que
> RECHAZAR las tres**, y §5.6 es precisamente la sección que existe para probar que el
> contrato funciona «sin campos vacíos de conveniencia».
>
> **LA REGLA, escrita una vez para que no haya que revisar celda a celda:** *un ejemplo de
> celda de este documento **no escribe `responsables` salvo que esté ilustrando una
> DESVIACIÓN, y entonces la escribe CON SU MOTIVO**. El reparto por defecto vive en el
> `contrato-de-aspecto` (§5.7) y en la norma del nivel (§9.2), y una celda que lo copie es una
> segunda verdad.*
>
> **`[HISTÓRICO]`** — lo que las tres celdas decían antes de esta corrección, conservado
> porque `X47` exige que lo retirado esté marcado y no borrado: ejemplo 1 y su hermana
> `responsables [DIS] lider: DIS`; ejemplo 2 `responsables [ARQ, SIS] lider: ARQ`, con la
> glosa «ARQ responde del CONTENIDO; SIS de la conformidad del contrato documental»; ejemplo
> 3 `responsables [PLT, VER] lider: PLT`. **Los tres coincidían con el defecto de su
> contrato**, y por eso ninguno debía llevar el campo. La glosa del ejemplo 2 **no se pierde**:
> es el reparto por defecto del `contrato-de-aspecto:documental/arquitectura`, y su sitio es
> §5.7, no la celda.

### Ejemplo 1 · una pantalla auditada en accesibilidad

```text
sujeto        clase: pantalla · ancla: web · ruta: checkout
              → pantalla:web/checkout
aspecto       aspecto:calidad/accesibilidad
              — SIN `responsables`: el reparto es el POR DEFECTO del contrato, y §3.5 sólo
                admite el campo para declarar una DESVIACIÓN con su motivo (`P-20`)
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
              — SIN `responsables`, por lo mismo: la capacidad responsable es la del reparto
                por defecto, y copiarla aquí sería una segunda verdad (`P-20`)
estado        verificado
caducidad     12 meses
```

> Con `dimension: ref a capacidad`, estas dos celdas eran **una sola** y no podían tener
> estados ni caducidades distintas. Ésa era la colisión, y éste es su remedio.

### Ejemplo 2 · un documento evaluado en una familia documental

```text
sujeto        clase: documento · ancla: transversal · ruta: arquitectura-actual
              → documento:transversal/arquitectura-actual
aspecto       aspecto:documental/arquitectura              el área 5 de `O8`, UNIFICADA
                                                          (§4.3). El SUJETO se llama
                                                          `arquitectura-actual` porque es la
                                                          RUTA de un documento; el ASPECTO
                                                          es el área. Dos espacios de
                                                          nombres distintos, y §3.5 los separa
              — SIN `responsables`: `[ARQ, SIS]` con `lider: ARQ` **ES** el reparto por
                defecto de este `contrato-de-aspecto`, y §5.7 lo declara allí. La celda sólo
                escribe la DESVIACIÓN, con motivo (`P-20`)
criterio      contrato-de-aspecto:documental/arquitectura               §5.7
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
memoria.contiene             [arquitectura, dominio-y-glosario]           DOS áreas, §4.3
                             — `arquitectura` es el área 5 UNIFICADA que `D68` restituyó,
                             no la mitad `arquitectura-actual` que retiró
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
              — SIN `responsables`: `[PLT, VER]` con `lider: PLT` es lo que la NORMA del
                nivel declara (§9.1 y §9.2), y §9.2 admite el campo **sólo** para la
                desviación, con motivo (`P-20`)
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
> `evaluacion_de_pruebas` (§3.5) la tesis vuelve a ser cierta, y **`X52`** la comprueba validando
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
`aspecto:documental/arquitectura` → `contrato-de-aspecto:documental/arquitectura` —el área 5
UNIFICADA, con el identificador que §4.3 declara—;
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
5  el adaptador viejo puede convivir o retirarse. **Retirar su proyección de una fuente es
   una ESCRITURA, y va por el mismo régimen que propagarla**: source change gobernado por
   `C7`, con paquete, `escribe_fuentes`, custodia de `PLT`, gate, autorización del Owner,
   rollback POR FUENTE e `INTEGRACIÓN PARCIAL` si converge en unas y no en otras (§6.7 regla
   2). **Corregido por `M4`**: la asimetría dejaba la operación DESTRUCTIVA menos gobernada
   que la constructiva, en repositorios que no son de ADS. Borrar la proyección nunca
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
> §8.1 SE AUTOCONTRADECÍA    los adaptadores se eligen en INS-2 y sus proyecciones se compilan
>                            antes de INS-6; pero ESCRIBE dice «las fuentes sólo desde INS-6»
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

5  `INS-2` Y `A5` NO ESCRIBEN PUNTEROS
   INSTALACIÓN  el puntero se propaga en **INS-6**, que es cuando §8.1 autoriza escribir en las
                fuentes. INS-2 elige el adaptador y compila lo del control repo; nada más
   ADOPCIÓN     el puntero se propaga en **A8**, que es cuando el Owner autoriza, y sólo lo
                que autorice. A0–A7 no tocan el producto, y eso vuelve a ser cierto

6  LÍMITE DE §6.3, DECLARADO
   la deriva de un puntero **sólo es detectable si su fuente está materializada**. Con una
   fuente ausente, el validador LO DICE y no asume nada — que es la regla de `NP-9` aplicada
   aquí, y lo que impide que «huella correcta» se lea como «puntero al día».
```

**Comprobación adversarial: `X62`, fila PROPIA.** Adopción hasta `A7` inclusive: `git status`
y `git log` en cada fuente no muestran **ni un solo commit ni un fichero nuevo** de ADS,
**incluidos los punteros de adaptador** · actualización en tres fuentes con `main` protegida:
la propagación produce tres PR, un Integration Set, y estado `INTEGRACIÓN PARCIAL` hasta que
las tres se fusionan · fusionar dos de tres y comprobar que el sistema **lo dice**, en vez de
declarar la actualización cerrada.

> **Corregido por el GATE DEFINITIVO INDEPENDIENTE (`J-03`, MEDIO; es `D101`).** Estas tres
> comprobaciones estaban **reasignadas a `X51`**, que cubre otro escenario: `X51` es «editar
> un canónico fuera del protocolo, sin transacción abierta, y arrancar → se declara deriva no
> transaccional», y no tiene nada que ver con que la adopción no escriba en las fuentes antes
> de `A8`. `M2` había señalado que `X32`–`X34` se citaban y **no existían en la tabla**, y el
> remedio de entonces las reasignó a una fila **existente pero ajena** — que es peor que la
> referencia rota, porque pasa desapercibida. **Se elige fila propia y no contrato de prueba
> F6** porque el escenario se expresa entero con el contrato de hoy —`git status`, `git log` y
> la ausencia de puntero, sobre tres fuentes— y **no exige ningún runtime que no exija ya
> cualquier otra de las cuarenta y seis**. `X51` conserva su escenario intacto.

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
CAÍDA A MITAD                 evento `preparada` de la tx: **COMPLETAR**, o `conflicto` si
                              algún fichero es divergente — y `conflicto` **no es un
                              desenlace: tiene DOS salidas**, completar si la divergencia
                              cesa, o **REVERTIR** lo especulativo local con `abandonada`
                              verificada byte a byte contra `revision_base` (§2.6.9).
                              **Corregido por `I-18`**: era la formulación que `A3` corrigió
                              en §7.4, sobreviviendo una sección más allá
INCONSISTENCIA IRRESOLUBLE    DSP para y escala. NUNCA inventa estado (b.14.3)
```

## 7.4 · `Continúa`

Los siete pasos de `b.14` se conservan, **con una desviación declarada en el paso 2** y
varias comprobaciones añadidas.

> **Corregido por la segunda devolución independiente (hallazgo `N-9`), y REESCRITO por el
> gate final independiente (`A3`, GRAVE; es `D73`).** F4c decía que los siete pasos «se
> conservan enteros». Después se corrigió a *«se cambia su disposición: donde (b) escribe
> «completar o REVERTIR», esta arquitectura escribe «completar o marcar conflicto», y §2.6
> elimina el ramal de reversión por completo»*. **Esa segunda formulación dejó de ser cierta
> con `D69`**, que dio a `abandonada` una restauración verificada de las escrituras
> ESPECULATIVAS LOCALES a la revisión base. `PN-7` ya recoge las DOS ramas en su cuerpo; el
> paso 2 y el resumen de §16 se habían quedado en la formulación vieja, y un lector tenía
> **dos contratos incompatibles** sobre el mismo paso.
>
> **Lo vigente, y es lo único vigente:** §2.6 tiene **las dos ramas de `a.9`** —completar y
> revertir—, y la reversión está ACOTADA a lo especulativo local. Lo publicado no se restaura
> nunca de forma automática (§2.6.0). Sigue siendo una desviación respecto de la LETRA de
> `b.14`, porque (b) no distingue publicado de especulativo, y por eso `PN-7` sigue vigente:
> lo que cambia es que ahora presiona por una PRECISIÓN, no por una rama ausente.

```text
2 VERIFICAR   · ¿existen los artefactos que los paquetes dicen haber producido?
              · ¿hay transacciones con `abierta(tx)` (§2.6.1)?  → LAS DOS RAMAS, y no hay
                una tercera:
                  COMPLETAR  todos los ficheros casan con su base o su resultado →
                             aplicar lo que falte en el `orden` declarado, `confirmada` si
                             no existía, regenerar derivados y `derivada`
                  MARCAR     algún fichero no casa NI con la base NI con el resultado →
                             `conflicto`, con la copia íntegra de lo divergente. Su salida
                             la decide la AUTORIDAD, y son dos: cesa la divergencia →
                             `confirmada`; la autoridad abandona → `abandonada`, que
                             RESTAURA lo especulativo local a `revision_base` y lo verifica
                             byte a byte antes de emitirse (§2.6.9)
                **Ninguna de las dos cierra dejando una mezcla parcial publicable.**
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
PROPIO    **CATORCE campos, y son catorce** —corregido por `I-21`, que encontró que el
          inventario decía doce y omitía dos: `proceso` y `handoffs`—:
            1 disparador · 2 precondiciones · 3 **proceso de cada tramo** · 4 participantes
            con su vía · 5 lecturas · 6 escrituras · 7 estados persistidos ·
            8 **handoffs** · 9 evidencias · 10 gates · 11 rollback · 12 reanudación ·
            13 certificación · 14 condición de cierre
FORMA     cada uno es una INICIATIVA con su plantilla de ruta. No un proceso.
```

> **Los dos campos que faltaban, y dónde quedan.** `proceso` estaba **implícito** en `N` —lo
> nombraba dentro de `PARTICIPANTES`— y explícito en los otros tres; ahora `N` lo rotula
> igual que ellos. Y `handoffs` **no existía en ninguno de los cuatro**: lo que viaja entre
> capacidades está declarado en el bloque «`SIS` y `PLT`, dicho aparte» de esta misma
> sección, pero no estaba repartido por macrocircuito. Cada bloque de §8.1–§8.4 gana ahora su
> fila `HANDOFFS`, que **remite** a ese bloque y a `circuitos/` sin duplicarlo: las
> instancias las crea F6 (`F-05`), y su ausencia hoy no bloquea la composición — sólo la
> entrega.

### La COMPOSICIÓN DE RUTA — sede canónica, y por qué NO hace falta un tipo nuevo

> **Añadida por el gate final independiente (`B-1` y `B-2`, BLOQUEANTES, con la conclusión
> del NIVEL 0 sobre `C5`; es `D74`).** Los cuatro macrocircuitos declaraban una lista de
> `PARTICIPANTES` y `D67` les asignó un proceso de `b.16`, **sin comprobar que el proceso
> asignado admitiera a esos participantes**. Trece de ellos no tenían por dónde entrar. El
> gate lo llamó «participantes sin vehículo», y el NIVEL 0 comprobó además que **`C5` no es
> ese vehículo**: un handoff ocurre ENTRE capacidades que YA están en la ruta —siete de sus
> diecisiete instancias disparan sobre el criterio `C-<CAP>` que el proceso declara—, luego
> `C5` **materializa** una entrega, no **compone** una ruta. Buscar el vehículo en `C5` era
> buscarlo un piso más arriba de donde vive.

**Dónde vive la composición, y es UNA sede.** No se crea ningún tipo canónico, y la prueba de
§3.1 no llega a plantearse, porque **la composición ya es expresable con lo que existe**:

```text
SEDE CANÓNICA          la tabla de §18, «Los cuatro macrocircuitos, mapeados a los procesos
                       de b.16», fase a fase. Los bloques de §8.1–§8.4 son su LECTURA
                       narrativa: si alguna vez difieren, MANDA §18.
                       **JERARQUÍA CON §9.6, la misma frase que allí, para que se lea desde
                       las dos puntas:** §18 manda sobre el **MAPEO** —qué fase, qué proceso
                       de `b.16`, qué participantes y por qué vía, qué entra y qué sale de
                       cada tramo—; **§9.6 manda sobre el CONTENIDO DEL CONTRATO
                       `gate:sistema-conforme`** —qué afirma, quién lo produce, qué exige su
                       entrada, dónde se persiste su salida, qué lo bloquea y qué lo cierra—.
                       Lo que no es contrato es mapeo, y no hay tercera cosa. Sin esta
                       jerarquía las dos reglas de desempate se solapaban sobre la FASE 0

QUÉ ES LA COMPOSICIÓN  un CONJUNTO DE ITEMS ENLAZADOS, agrupados por una `iniciativa` —tipo
                       que §3.3 ya declara—. NO es un artefacto nuevo, no tiene esquema
                       propio y no entra en el recuento de §3.8

POR QUÉ NO PUEDE SER   porque `b.1` fija la REGLA DE PROCESO ÚNICO: «un item tiene
UN SOLO ITEM           EXACTAMENTE UN proceso en cada momento». Una fase que necesita
                       capacidades de dos rutas necesita DOS ITEMS, no un proceso nuevo
```

**Cómo entra una capacidad en la ruta. Son CUATRO vías, y no hay una quinta:**

```text
1 PROPIETARIA GLOBAL   la capacidad cuya capa DEFINE el resultado del item. La fija `b.16`
                       por proceso, y en `AUD` y `DIR` se DERIVA del encargo — nunca se
                       asigna a mano (`01-PROCESOS.md` L419)

2 OBLIGATORIA          figura en las `obligatorias` del proceso del item. Entra SIEMPRE, y
                       su obligación tiene que quedar SATISFECHA para cerrar (`b.3`, `b.10`)

3 CONDICIONAL          figura en las `condicionales` del proceso CON SU CONDICIÓN ESCRITA Y
                       COMPROBABLE del vocabulario de `b.16` —`C-DIS`, `C-ARQ`, `C-DOM`,
                       `C-SEG`, `C-ENT`, `C-USO`, `C-APR`— o con una condición propia
                       redactada. **Una condición vaga está PROHIBIDA** —`b.16` lo dice con
                       su propia fórmula, que este documento no repite porque el validador de
                       vocabulario la rechaza—, y lo no activado deja motivo (`a.6`)

4 ITEM PROPIO ENLAZADO la capacidad NO cabe en el proceso de la fase, y entra con SU PROPIO
                       ITEM, bajo el proceso que sí la declara, enlazado al item líder de la
                       fase. Es la regla que `b.16` ya escribe DOS VECES: «varias
                       conclusiones INDEPENDIENTES con propietarios distintos → se divide en
                       items AUD ENLAZADOS, uno por conclusión», y lo mismo para `DIR`
```

**Y hay TRES formas de estar presente que NO son participar en la ruta**, y confundirlas con
la vía 3 es lo que produjo la lista de participantes sin vehículo. **Corregido por el gate de
cierre (`I-20`)**: el texto decía DOS y los macrocircuitos usaban tres — el registro de `D74`
sí las declaraba las tres.

```text
EJECUTOR      ejecuta el trabajo sin responder de la conclusión. `a.5` los separa
              expresamente. **Quién ejecuta qué en Git lo fija `C7`, operación a operación**,
              y el reparto está abajo. `PLT` es ejecutor donde `C7` lo dice —materializar una
              fuente y retirar una rama abandonada—, y **no es participante de la ruta por
              hacerlo**

AUTORIDAD     autoriza o cierra un gate. El **Owner** en `A8`, `M6` y en toda decisión de
              retirada, y la autoridad de retirada que cada obligación nombra. Autorizar no
              es depositar capa

ENCUADRE      `ENC` produce el encuadre ANTES de que haya ruta, y `b.16` no la declara en
              ningún proceso. Encuadrar no es depositar capa, y por eso `ENC` no figura entre
              los participantes de ninguna fase
```

#### QUIÉN EJECUTA CADA OPERACIÓN GIT — el reparto es de `C7`, y se cita, no se reescribe

> **Corregido por el gate de cierre independiente (`I-04`, GRAVE; es `D90`).** Este párrafo
> decía que **`PLT` bajo `C7` custodia «cada source change —rama, commit, push, PR y CI POR
> FUENTE»**, y `C7:83-86` da esas cuatro operaciones a **la capacidad con custodia, ella
> misma**. De las siete operaciones que se le atribuían, `C7` le da **dos**. Y no era sólo
> divergencia con el contrato: **F4 se desmentía a sí misma** —§1.3 asigna el
> `integration-set` a `ENT` como autoridad y ejecutor, §7.2 escribe «`ENT` declara
> convergencia con un INTEGRATION SET» y §7.6 remite a `C7` «de las fuentes»—. La fila
> `EJECUTOR` existía ya en §8.3; **esta tanda la generalizó a §8.0, §8.1, §8.2, §8.4 y a §18,
> y la promovió a dispositivo de cierre de un BLOQUEANTE**, que es lo que lo hacía grave.

**El reparto vigente, literal contra `C7:82-92`, y sin repetir la tabla que `C7` ya tiene:**

```text
MATERIALIZAR UNA FUENTE   la solicita `DSP` al despachar · **la ejecuta `PLT`** · la verifica
                          `gate:workspace-conforme`                              `C7:82`

CREAR RAMA O WORKTREE     la solicita y **la ejecuta LA CAPACIDAD CON CUSTODIA, ella misma**
COMMIT · PUSH · ABRIR PR  `PLT` puede bloquear si el aislamiento no basta   `C7:83`–`C7:86`
                          En los tramos de §8 que escriben en fuentes esa capacidad es
                          **`CON`**, obligatoria por `cambio-construido` en `proceso:SIS`,
                          `proceso:DEU` y `proceso:DEP`

`SEG` PUEDE BLOQUEAR      **el push, ante secreto detectado**                        `C7:85`
                          Y en `U5b` además participa por vía 2, con `G28` haciéndola
                          irretirable — que es otra cosa y no se confunde con ésta

MERGE Y CONVERGENCIA      **`ENT` las solicita y las ejecuta.** `declarar convergencia` pasa
                          por `gate:convergencia-de-fuentes` y produce el Integration Set
                                                                        `C7:88`–`C7:89`
CI                        **verifica CADA FUENTE**, y es quien verifica push y PR. No la
                          ejecuta ninguna capacidad de la ruta

RETIRAR RAMA ABANDONADA   la solicita y la ejecuta **`PLT`**, y la capacidad con custodia
                          puede bloquearla si la reclama                             `C7:92`

EL OWNER                  conserva su autoridad **donde `C7` la exige**: materia reservada en
                          el merge, el release, y el rollback irreversible. Y en §8, además,
                          la autorización de retirada POR FUENTE de `A8` y `M6`
```

```text
QUÉ NO CAMBIA CON ESTO    **`PLT` NO se convierte en participante de la ruta** por ejecutar la
                          materialización: sigue siendo EJECUTOR, con su propio gate
                          (`gate:workspace-conforme`) y fuera de las cuatro vías. Lo que
                          cambia es el ALCANCE que se le atribuía, no su naturaleza.
                          En `U5b` `PLT` **sí** participa, pero por la **vía 1** —es la
                          propietaria global de `proceso:DEP`—, no por ser ejecutor.

QUÉ RESIDUO DEJA EN       `PN-13` conserva ÚNICAMENTE lo que de verdad le quedaba: la
`B-2`                     composición de **`INS-5`** y de **`A9`**, donde `proceso:SIS` y
                          `proceso:INV` no dan vía a `DOM`, `SEG` ni `DIS`. **La mitad `PLT`
                          del bloqueante se cierra aquí, contra `C7`, y no era materia del
                          Owner**: `C7:80-92` ya decía quién.
```

**Cómo se materializan los handoffs DESPUÉS, y por qué es después.** Una vez la ruta está
compuesta, la entrega concreta entre dos capacidades que ya están en ella se declara en
`kernel/operativo/circuitos/` con la forma de `C5`. De sus **once campos obligatorios** —`id`,
`de`, `a`, `cuando`, `entrega`, `comprueba_al_recibir`, `rechaza_si`, `devolucion`,
`evidencia_de_devolucion`, `owner` y `checkpoint`, según `esquemas/handoff.yaml`—, los que
esta sección necesita nombrar son **seis**: `id`, `de`, `a`, `cuando`, `checkpoint` y
`comprueba_al_recibir`. **Es un SUBCONJUNTO declarado, no la lista completa** —corregido por
`I-22`—: los otros cinco los exige el esquema igual, y su sede es `C5`, no ésta.
**El orden importa y no es reversible**: sin
composición no hay entre quiénes; con composición, el handoff sólo añade QUÉ viaja y CUÁNDO.
`00-CIRCUITOS.md` lo dice con todas las letras —los circuitos son la sede de las entregas
entre capacidades—, y ésa es la fuente que manda cuando `C5` parece decir otra cosa.

**Cuántos ITEMS compone cada macrocircuito, y cómo le afecta el FRENO 3 de `a.7`.**

> **Declarado por el gate final independiente (`M-7`, MEDIO; es `D82`).** `a.7` FRENO 3 impide
> despachar más de **dos items `SIS` completados consecutivamente** si hay un item de producto
> listo. Los cuatro macrocircuitos son mayoritariamente `proceso:SIS` y **dos de ellos —`A` y
> `U`— componen más de dos items líderes**, y §8 no decía ni cuántos ni cómo interactúan con
> el freno. El tercer item de `A` se habría detenido sin que nadie hubiera previsto por qué.
> **[HISTÓRICO] Corregido por `I-25`**: la premisa citada decía «más de dos items **cada
> uno**», y la derivación de entonces daba **N 2** y **M 2**. La derivación manda; la premisa
> se ajusta a ella. **Aquellas cifras son de antes de `D107`, no se reescriben, y el bloque de
> abajo ya no las copia: se re-deriva de §18 con la `FASE 0` dentro de la racha.**

```text
CUÁNTOS ITEMS      los ITEMS LÍDERES son las FILAS de la tabla de §18 —una por tramo de fases
COMPONE CADA UNO   con proceso propio—, más los ITEMS ENLAZADOS que la vía 4 exija.
                   **El recuento se DERIVA de §18 y NO SE ESCRIBE AQUÍ**, que es lo que esta
                   misma casilla ya prometía y lo que copiar el cardinal incumplía. Lo que sí
                   se escribe es la **SECUENCIA DE PROCESOS**, porque es lo único que el
                   FRENO 3 necesita y porque se lee fila a fila de §18 en su orden:
                     N   `SIS` `SIS` `SIS`
                     A   `SIS` `SIS` `AUD` `DEU` `SIS`
                     M   `SIS` `SIS` `DEU`
                     U   `SIS` `SIS` `SIS` `DEP` `SIS`
                   **Cada uno empieza por su `FASE 0`, que §18 declara `proceso:SIS` con
                   estado persistido propio** —`O17` vía `D107`, no elección de F4—. En `A`,
                   el tramo `AUD` NO es un item: son varios `AUD` enlazados, **uno por
                   conclusión** — ocho sólo en `A6`. Si §18 cambia, esta secuencia cambia con
                   ella, y **no queda ningún cardinal escrito aparte que pueda caducar en
                   silencio**

FRENO 3, CIRCUITO  **RE-DERIVADO sobre la secuencia de arriba, CON la `FASE 0` dentro de la
A CIRCUITO         racha.** El FRENO 3 de `a.7` exige **más de dos items `SIS` COMPLETADOS
                   CONSECUTIVAMENTE**, y su antecedente es que **haya un item de producto
                   listo**. Las dos condiciones, no una.
                   · **`N` · instalación** — racha `SIS` máxima **TRES** (`FASE 0` · `INS-0`–
                     `INS-5` · `INS-6`–`INS-7`), pero el **antecedente es FALSO**: no existe
                     ningún item de producto listo, porque el producto no tiene items en ADS
                     hasta `INS-7`. **El freno no llega a evaluarse.** No es excepción
                   · **`A` · adopción** — racha `SIS` máxima **DOS** (`FASE 0` · `A0`–`A1`),
                     y ahí `AUD` rompe: el freno cuenta rachas de items **`SIS`**. **Nunca
                     alcanza el tercero consecutivo**, y además el antecedente es falso hasta
                     `A10`, que es su puerta
                   · **`M` · migración** — racha `SIS` máxima **DOS** (`FASE 0` · `M0`–`M5`),
                     y `M6`–`M7` es `DEU`. **Nunca alcanza el tercero consecutivo**
                   · **`U` · actualización — AQUÍ SÍ LLEGA A EVALUARSE, Y SE DICE.** La racha
                     es `FASE 0` · `U0`–`U4` · `U5a`: **TRES `SIS` consecutivos** antes de que
                     `DEP` rompa en `U5b`, y tres es «más de dos». Y `U` es **el único de los
                     cuatro donde el antecedente es plausiblemente VERDADERO**, porque corre
                     sobre un producto ya instalado y operando. **Luego la conclusión anterior
                     —«`U` tiene dos», y con ella «ninguno de los cuatro necesita excepción del
                     Owner»— DEJA DE ESTAR DERIVADA para `U`**, y lo que la caducó fue meter
                     la `FASE 0` en la racha, que es `O17` vía `D107` y no una elección de F4.
                     **Lo que sostiene hoy a `U` es la cláusula LITERAL de excepción de `a.7`**
                     —«NO APLICA mientras el objetivo explícito del proyecto sea construir o
                     migrar el propio kernel/runtime»—, que en `U` es literalmente el caso:
                     `U` actualiza el propio ADS. **Para `U`, y SÓLO para `U`, esa cláusula
                     pasa de OBSERVACIÓN a FUNDAMENTO**, porque la cuenta propia ya no cierra.
                     **Si el Owner no la considerase aplicable a una actualización, `U`
                     necesitaría excepción del Owner — y eso NO se decide aquí**: queda
                     registrado en §9.6 como trabajo futuro, con propietario, fase y prueba.
                     `U` además declara `bloqueo` en §8.4: ninguna otra actualización arranca
                   **[HISTÓRICO]** la redacción anterior decía «`M` tiene uno y `U` tiene dos»
                   y dejaba la cláusula de `a.7` «como observación, no como fundamento»
                   (`K-08`): era cierto ANTES de que `D107` añadiera la `FASE 0` a cada racha,
                   y **no se reescribe**.
                   **`N`, `A` y `M` no necesitan excepción del Owner, y la cuenta propia lo
                   demuestra tramo a tramo. `U` sí depende hoy de la cláusula literal de
                   `a.7`, y por eso está registrado.** Lo que hacía falta era comprobarlo y
                   decirlo — también, y sobre todo, cuando el resultado cambia

QUÉ PASA SI CAMBIA si un producto adoptado tuviera items ADS listos DURANTE su adopción
                   —caso que hoy no existe porque `A10` es su puerta—, el freno pasaría a
                   evaluarse y la salida sería la tercera excepción de `a.7`: «trabajo SIS
                   que desbloquea directamente el item de producto listo», que es exactamente
                   lo que una adopción es. Queda dicho para que nadie lo redescubra
```

**Cómo se COMPRUEBA que la composición está completa.** Es mecánico, y F6 lo construye como
validador; aquí queda declarado el contrato:

```text
GATE DE COMPOSICIÓN    ninguna fase de ningún macrocircuito abre hasta que, para CADA
                       capacidad que la fase declara, consta UNA de las cuatro vías, con su
                       proceso y —si es la 3— su condición nombrada

ENTRADA Y SALIDA       para cada capacidad de la ruta: la ENTRADA es su vía (1–4); la SALIDA
                       es la capa que deposita, con su criterio de satisfacción. Una
                       capacidad sin salida declarada es una capacidad que no tenía por qué
                       estar

EVIDENCIA              la tabla de §18 resuelta fase a fase, con la vía de cada capacidad, y
                       el enlace de cada item propio a su item líder

ERROR CUANDO FALTA     `composicion-incompleta`: la fase NO abre, DSP para y escala
UNA CONEXIÓN           nombrando la capacidad y la fase (`b.14.3`). **No se inventa un
                       handoff para tapar una capacidad sin vía**, y no se ensancha un
                       proceso por conveniencia: ensanchar `b.16` es normativo, y su sitio
                       es una presión, no esta arquitectura

QUIÉN CONSUME LA       `DSP`, que compone y despacha; y el `gate` de la fase, que no cierra
COMPOSICIÓN            sin las obligaciones satisfechas (`b.10`)
```

> **`SIS` y `PLT`, dicho aparte porque el NIVEL 0 los aisló.** Ninguna de las diecisiete
> instancias de handoff declaradas en `circuitos/` nombra a `SIS` ni a `PLT` — ni como
> emisor ni como receptor—, y los cuatro macrocircuitos son mayoritariamente `proceso:SIS`
> con `PLT` como ejecutor. **No es un defecto de composición**: `SIS` entra por la vía 1
> —es la propietaria global de `proceso:SIS`— y `PLT` no entra por ninguna porque **es
> ejecutor, no participante**. Lo que sí falta es material y queda declarado aquí para que
> F6 lo materialice sin decidir nada:
>
> ```text
> QUÉ VIAJA DE SIS A PLT    la SOLICITUD DE MATERIALIZACIÓN de las fuentes del alcance, que
>                           es lo que `C7:82` le da a `PLT`. **No el source change entero**:
>                           rama, commit, push y PR los hace la capacidad con custodia
>                           (`C7:83`–`C7:86`). **Corregido por `I-04`**
> QUÉ VIAJA DE SIS A CON    el SOURCE CHANGE: paquete con `escribe_fuentes`, y con él la
>                           custodia de rama, commit, push, PR y CI POR FUENTE bajo `C7`. Es
>                           lo que §8.3 `M6`, §8.2 `A8` y §8.4 `U5b` describen
> QUÉ VIAJA DE SIS A VER    el dosier de certificación: celdas, evidencia y nivel propuesto
> QUÉ VIAJA DE CON A ENT    el resultado POR FUENTE. **`ENT` declara la convergencia y emite
>                           el Integration Set** (`C7:88`–`C7:89`), y es quien sostiene el
>                           estado `INTEGRACIÓN PARCIAL` mientras no converjan todas —§1.3
>                           L224, §7.2 y `C7` coinciden—. **Corregido por `I-04`**: esta
>                           entrega salía de `PLT`, y la convergencia nunca fue suya
> QUÉ VIAJA DE ENT A VER    la convergencia declarada, con su Integration Set, para el gate
> DÓNDE SE DECLARAN         `kernel/operativo/circuitos/`, en F6. Son instancias, no norma:
>                           no requieren decisión del Owner, y su ausencia hoy NO bloquea la
>                           composición, sólo la entrega
> ```

## 8.1 · Instalación en proyecto nuevo

```text
DISPARADOR      el Owner quiere gobernar un producto que todavía no existe
PRECONDICIONES  hay un sitio donde crear el workspace · hay remoto para el control repo ·
                **FASE 0 superada**: certificación Estructural DE ESTA EJECUCIÓN, verificada
                y vigente (§9.6). **Derivado de `O17` vía `D107`; no lo elige F4**
FASES           **FASE 0 · CERTIFICACIÓN ESTRUCTURAL** — precondición PROPIA de esta
                   ejecución, ANTERIOR a toda mutación canónica y a todo intento de
                   elevarse. Invoca **el contrato compartido `gate:sistema-conforme`** de
                   §9.6, que es el MISMO que invocan §8.2, §8.3 y §8.4. Si falla, la
                   instalación se BLOQUEA antes de mutar estado
                INS-0 crear y publicar control repo y workspace, CON EL SOPORTE DURABLE
                   MÍNIMO DE `estado/` y la iniciativa de instalación ya escrita
                INS-1 elaborar y aprobar PROFILE
                INS-2 elegir topología de fuentes, packs, extensiones y adaptadores
                INS-3 C0: especializar y verificar la organización YA MATERIALIZADA
                INS-4 certificar instalación y reanudación
                INS-5 discovery de producto, dominio y diseño
                INS-6 engineering bootstrap con evidencia real
                INS-7 gate «listo para construir»
PROCESO         `INS-0`–`INS-5` y `INS-6`–`INS-7` son los DOS tramos, y **los dos son
DE CADA TRAMO   `proceso:SIS`** — «cambiar la propia fábrica», que es literalmente lo que una
                instalación hace. §18 tiene la tabla, y manda. **Rotulado por `I-21`**: era
                el único de los cuatro que lo dejaba implícito dentro de `PARTICIPANTES`
PARTICIPANTES   **con su VÍA de entrada (§8.0), porque una lista sin vía no es una ruta**
                  **FASE 0** · participantes y reparto en §9.6, que es la sede ÚNICA y
                         la misma para los cuatro: `SIS` productor y propietario de la
                         declaración · `VER` el dosier verificador, sin apropiarse de la
                         decisión · `PLT` la maquinaria técnica cuando el contrato vigente
                         se la atribuya · `SEG` su bloqueo por seguridad. **El propietario
                         de este macrocircuito no puede sustituir a `SIS`, y DEBE exigir la
                         certificación antes de continuar** (`O17` vía `D107`)
                  `SIS`  vía 1 · propietaria global de `proceso:SIS`, todas las fases
                  `CON`  vía 2 · obligatoria `cambio-construido`
                  `VER`  vía 2 · obligatoria `evidencia-suficiente`. Cierra `INS-4` y `INS-7`
                  `ENT`  vía 3 · «el cambio modifica el runtime», en `INS-6`
                  `APR`  vía 3 · `C-APR`
                  `PRD` y `ARQ`  vía 4 · items `proceso:INV` ENLAZADOS para el discovery de
                         `INS-1` y `INS-5`, por sus condicionales «el destino declarado es una
                         decisión de producto» y «…una decisión técnica»
                  `DOM`, `DIS` y `SEG`  **SIN VÍA en `proceso:INV`. Es `PN-13`**, y hasta
                         que F5 la resuelva su discovery se encarga como items `proceso:AUD`
                         SÓLO si el objeto ya existe — que en una instalación NUEVA no es el
                         caso. §8.0 prohíbe inventarles un handoff
EJECUTOR        **el reparto es de `C7`, y §8.0 lo cita operación a operación.**
                  `PLT`  en `INS-0`, `INS-2` y `INS-6`: MATERIALIZA las fuentes (`C7:82`) y
                         retira ramas abandonadas (`C7:92`). Custodia workspace, adaptadores
                         y la maquinaria. **Ejecuta, no deposita capa** (`a.5`)
                  `CON`  rama, commit, push y PR de cada source change de `INS-6` — es la
                         capacidad CON CUSTODIA por su obligatoria `cambio-construido`, y
                         `C7:83`–`C7:86` se los da a ella misma
                  `SEG`  puede BLOQUEAR el push ante secreto detectado (`C7:85`)
                  `ENT`  merge y declaración de convergencia (`C7:88`–`C7:89`)
                  CI     verifica cada fuente
                **Corregido por `I-04`**: decía «`PLT` … cada source change», que `C7:83-86`
                desmiente
ENCUADRE        `ENC` encuadra `INS-1` y `INS-5` ANTES de que haya ruta. No es participante de
                ninguna: `b.16` no la declara en ningún proceso, y es correcto (§8.0)
AUTORIDAD       el **Owner**: decisión de instalar, y los gates `INS-4` y `INS-7`
LEE             la distribución instalada
ESCRIBE         control repo entero; las fuentes sólo desde INS-6 — **incluidos los punteros
                de adaptador**, que INS-2 NO escribe aunque elija el adaptador (§6.7)
ESTADO          `estado/` nace en **INS-0**, con su soporte durable mínimo. Ver abajo
HANDOFFS        de `SIS` a `PLT` la SOLICITUD DE MATERIALIZACIÓN · de `SIS` a `CON` el source
                change de `INS-6` con su custodia · de `CON` a `ENT` el resultado por fuente ·
                de `ENT` a `VER` la convergencia declarada. **Su QUÉ está en §8.0; las
                INSTANCIAS las crea F6 en `circuitos/`** (`F-05`), y su ausencia hoy no
                bloquea la composición
EVIDENCIA       **el dosier de FASE 0 que `VER` produce, con la huella de su sujeto (§9.6)** ·
                `workspace check` · prueba de humo por adaptador · checkpoint recuperado
GATES           **FASE 0 `gate:sistema-conforme`, antes de INS-0 y de cualquier mutación
                canónica (§9.6)** · INS-4 certificación Operativa · **INS-5 baseline aprobado
                por el Owner** · INS-7 = O12, con sus TRES condiciones y su productor nombrado
CERTIFICACIÓN   **Estructural en FASE 0**, propia de ESTA ejecución y NO heredada de ninguna
                anterior (§9.6) · Operativa en INS-4 · Integrada en INS-7, con la aplicabilidad de §9.5: en INS-7 el
                producto tiene LAS FUENTES QUE INS-2 DECLARÓ, y la columna que rige es la de
                ese número. Si son 0, hay pruebas que no le aplican
                **Corregido** (hallazgo `N-5`): F4c decía «una instalación nueva tiene CERO
                fuentes», y es falso en INS-7 — que es donde se invoca
ROLLBACK        ver «Rollback, con el remoto separado de lo local», abajo
REANUDACIÓN     **por el checkpoint del paquete de `SIS-001`, desde INS-0**. Ningún tramo del
                recorrido depende del chat
CIERRE          INS-7 superado y el primer item de producto despachable
```

> **Quién produce las TRES condiciones de `O12`, que `INS-7` invoca (`G-3`, GRAVE; es `D76`).**
> §9.4 fija que empezar a programar exige **Integrada + baseline aprobado + ningún
> desconocido crítico sin clasificar — las tres, no dos**. §8.1 declaraba `INS-7 = O12` y
> **ninguna fase producía las dos últimas**: el gate era invocable pero no satisfacible.
>
> ```text
> INTEGRADA                    `INS-7`, con la aplicabilidad de §9.5. Ya estaba
> BASELINE APROBADO            **`INS-5`**, y lo aprueba el **Owner** — exactamente como `A3`
>                              en la adopción. La simetría no es estética: `INS-5` es la única
>                              fase de `N` que produce conocimiento de producto, y el
>                              baseline funcional es el área 3 de la taxonomía documental
> DESCONOCIDOS CRÍTICOS        **`INS-5` también**, y su clasificación es un ENTREGABLE
> SIN CLASIFICAR               declarado suyo, no un residuo: cada desconocido queda
>                              clasificado como resuelto, acotado con su portador, o
>                              deferido con su motivo. Un desconocido sin clasificar es lo
>                              que `O12` prohíbe, y por eso su ausencia se comprueba en `INS-7`
>                              y no se descubre al construir
> ```
>
> **No reinterpreta `O12` y no necesita presión normativa**: `O12` decía qué hace falta, y lo
> que faltaba era el productor. La alternativa —dejarlo abierto y registrarlo como `PN`—
> llevaría al Owner una pregunta que su propia resolución de adopción ya responde en `A3`.

**Lo que cambia respecto a hoy.** `C0` deja de redactar la organización y pasa a
**especializar y verificar** una que la distribución ya trae. Es `O9` y el §4.11 del documento
de pendientes: el agente no crea ADS durante C0.

### `estado/` nace en INS-0, y no en INS-3

F4 entregada declaraba *«`estado/` nace en INS-3. La iniciativa de instalación nace en INS-0»* y
*«REANUDACIÓN por checkpoint desde INS-3; antes, repitiendo el paso»*. **Las dos frases juntas
dicen que entre INS-0 y INS-3 la iniciativa no está persistida**: vive en la conversación. Eso es
exactamente lo que el apartado 19 de la directiva prohíbe, y lo que `b.14` no puede reanudar.

```text
QUÉ SE CREA EN INS-0,        estado/
Y ES EL MÍNIMO              ├─ iniciativas/INI-001/00-iniciativa.md   la instalación misma
                            ├─ eventos/                               el diario, desde el
                            │                                         primer acto
                            └─ items/SIS-001/                         el ITEM de instalación
                                 ├─ 00-encuadre.md · 01-ruta.md · 02-control.md
                                 └─ paq/01-SIS.md                     el paquete en curso,
                                                                      con su CHECKPOINT

                          **Corregido por la tercera revisión independiente (`G7`).** Decía
                          `items/INI-001-paq/`, y eso violaba tres contratos a la vez: usaba
                          un id de INICIATIVA como id de ITEM contra §2.8, no era una ruta
                          válida bajo §2.3 —los paquetes viven en `<ITEM-ID>/paq/`— y
                          asignaba un paquete a una iniciativa, que `D45` había declarado
                          imposible catorce páginas antes: «una iniciativa no tiene paquetes
                          ni capas: sólo `items` como referencias».

EL ITEM REAL QUE `INS-0`     **`SIS-001`**, item de `proceso:SIS` —«cambiar la propia fábrica»,
CREA                      que es literalmente lo que una instalación hace (§8.0)—. Su
                          propietario global es `SIS`. `INI-001` lo REFERENCIA, y nada más:
                          no copia su estado, que es lo que §3.3 exige.
                          Con ello `Q4` deja de contradecirse: la iniciativa **no** nace con
                          el conjunto de items vacío, nace con uno.

QUÉ NO SE CREA EN INS-0      cobertura, integración, tableros de capacidades que no se han
                          materializado, y todo lo que no tenga contenido todavía. Un
                          directorio vacío no es soporte durable: es ruido.

POR QUÉ ES BARATO         son cinco ficheros pequeños. El coste de crearlos es menor que el
                          de explicar por qué un recorrido de siete fases no se puede
                          reanudar en sus tres primeras.

QUÉ HACE INS-3 AHORA        lo que `O9` ya decía que hace: ESPECIALIZAR Y VERIFICAR la
                          organización que la distribución trae materializada. Deja de
                          «crear `estado/`», que era lo que lo ponía en contradicción con INS-0.

QUÉ SE GANA               «Continúa» funciona desde el primer minuto de una instalación. El
                          recorrido se reanuda desde INS-0 SIN el chat y SIN el Owner, que es
                          `R7` y `b.14` aplicados también a la instalación — y no sólo al
                          trabajo de producto.
```

### Rollback, con el remoto separado de lo local

F4 entregada decía *«INS-0–INS-2 se deshacen borrando el workspace: no hay producto que dañar»*.
Pero INS-0 **publica** el control repo. Borrar lo local no revierte lo publicado.

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

ANTES DE INS-0    no hay nada que revertir: no se ha publicado.
```

## 8.2 · Adopción profunda de un producto existente

El más largo, y el que `CI-5` protege de ser aplanado contra la instalación.

```text
DISPARADOR      el Owner quiere gobernar un producto CON HISTORIA
PRECONDICIONES  acceso de lectura a todas sus fuentes · modo NO DESTRUCTIVO declarado ·
                **FASE 0 superada**: certificación Estructural DE ESTA EJECUCIÓN, verificada
                y vigente (§9.6). **Derivado de `O17` vía `D107`; no lo elige F4**
FASES           **FASE 0 · CERTIFICACIÓN ESTRUCTURAL** — precondición PROPIA de esta
                    ejecución, ANTERIOR a toda mutación canónica y a todo intento de
                    elevarse. Invoca **el MISMO contrato compartido `gate:sistema-conforme`**
                    de §9.6. Si falla, la adopción se BLOQUEA antes de mutar estado
                A0  apertura, perímetro y modo no destructivo
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
PROCESO         `A0`–`A1` y `A9`–`A10` son `proceso:SIS`. **`A2`–`A7` es `proceso:AUD`**,
DE CADA TRAMO   y `A8` es `proceso:DEU`. §18 tiene la tabla, y manda
PARTICIPANTES   **con su VÍA de entrada (§8.0)**
                  **FASE 0** · participantes y reparto en §9.6, que es la sede ÚNICA y
                         la misma para los cuatro: `SIS` productor y propietario de la
                         declaración · `VER` el dosier verificador, sin apropiarse de la
                         decisión · `PLT` la maquinaria técnica cuando el contrato vigente
                         se la atribuya · `SEG` su bloqueo por seguridad. **El propietario
                         de este macrocircuito no puede sustituir a `SIS`, y DEBE exigir la
                         certificación antes de continuar** (`O17` vía `D107`)
                `A0`–`A1` · `proceso:SIS`
                  `SIS` vía 1 · `CON` y `VER` vía 2
                `A2`–`A7` · `proceso:AUD`, y **NO es un item: son VARIOS ENLAZADOS**, uno
                por conclusión independiente, que es lo que `b.16` manda para `AUD` cuando
                hay «varias conclusiones INDEPENDIENTES con propietarios distintos»
                  propietario global  **DERIVADO por item**, nunca asignado a mano
                                      (`01-PROCESOS.md` L419): la capacidad responsable de
                                      LA CONCLUSIÓN de ese item. `A6` reconstruye producto,
                                      arquitectura, dominio, datos, UI/UX, sistema de
                                      diseño, seguridad y operación REALES — ocho
                                      conclusiones, con `PRD`, `ARQ`, `DOM`, `DIS`, `SEG` y
                                      `ENT` como propietarias de la suya. **Ésa es su vía 1**
                  `INV`  vía 2 · única obligatoria de `AUD`: produce la evidencia de CADA
                         item. Es la capacidad que EJECUTA la auditoría sin responder de la
                         conclusión, y `b.16` lo dice con esas palabras
                  `DOM` `C-DOM` · `SEG` `C-SEG` · `DIS` `C-DIS` · `PRD` «produce una
                         decisión de producto» · `APR` `C-APR`  vía 3, en los items donde no
                         son propietarias
EJECUTOR        **el reparto es de `C7`** (§8.0). En `A8`:
                  `PLT`  MATERIALIZA las fuentes (`C7:82`) y retira ramas abandonadas
                         (`C7:92`). **No es participante de la ruta de `A8`**, y por eso no
                         figura arriba (`a.5`)
                  `CON`  rama, commit, push y PR POR FUENTE — capacidad CON CUSTODIA por su
                         obligatoria `cambio-construido` (`C7:83`–`C7:86`)
                  `SEG`  puede BLOQUEAR el push ante secreto detectado (`C7:85`)
                  `ENT`  merge y convergencia, con su Integration Set (`C7:88`–`C7:89`)
                  CI     verifica cada fuente
                **Corregido por `I-04`**
ENCUADRE        `ENC` encuadra `A7` —trabajo vivo— antes de que haya ruta. No es
                participante (§8.0). Su extensión de ficha para clasificar findings del
                sistema está en §5.2 y §17
AUTORIDAD       el **Owner**: gate `A3` del baseline, autorización de retirada de `A8` POR
                FUENTE, y `A10`
`A8` · `proceso:DEU`
                  `ARQ` vía 1 · propietaria global, obligatoria `plan-tecnico` con radio de
                        impacto MEDIDO
                  `CON` vía 2 · obligatoria **`cambio-construido`**, cuya `capacidad_productora`
                        es `CON` en `01-PROCESOS.md`. Sin ella `A8` no cierra
                  `VER` vía 2 · obligatoria `evidencia-suficiente`
                  `DOM:condiciones` `SEG:condiciones` `ENT` `USO` `APR` vía 3
`A9`–`A10` · `proceso:SIS`
                  `SIS` vía 1 · `CON` y `VER` vía 2
                  `SEG` **SIN VÍA en `proceso:SIS` cuando hay superficie. Es `PN-13`.** Hasta
                        que F5 la resuelva, su dictamen entra como item `proceso:AUD`
                        enlazado, con `SEG` de propietaria global derivada
LEE             TODO: código, docs, historial Git, ramas, PR, CI, entornos, despliegues,
                agentes, skills, prompts, reglas, workflows, backlog, incidentes
ESCRIBE         NADA en las fuentes hasta A8, y en A8 sólo lo que el Owner autorice —
                **incluidos los punteros de adaptador**, que A5 NO escribe aunque
                especialice el adaptador. Sin esta corrección, la adopción de un producto
                ajeno empezaba haciendo un commit en su repositorio (§6.7)
ESTADO          la iniciativa de adopción nace en A0 y es el hilo entre chats
HANDOFFS        entre los items `AUD` enlazados de `A2`–`A7` y su consumidor · de `SIS` a
                `PLT` la solicitud de materialización · de `SIS` a `CON` el source change de
                `A8` · de `CON` a `ENT` el resultado por fuente · de `ENT` a `VER` la
                convergencia. **Su QUÉ está en §8.0; las INSTANCIAS las crea F6**
EVIDENCIA       **el dosier de FASE 0 que `VER` produce, con la huella de su sujeto (§9.6)** ·
                inventario con procedencia · baseline aprobado · mapa de conservación
GATES           **FASE 0 `gate:sistema-conforme`, antes de A0 y de cualquier mutación
                canónica (§9.6)** · A3 baseline aprobado por el Owner, contra las CATORCE
                preguntas del §6.2 de la directiva, que son su contrato (abajo) · A8
                autorización de retirada · A10 = O12
CERTIFICACIÓN   **Estructural en FASE 0**, propia de ESTA ejecución y NO heredada (§9.6) ·
                Integrada en A9
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
>
> **Nota al pie, que NO toca la resolución** (`m-1`): `O15` se escribió cuando el recuento
> derivado de presiones normativas vigentes era **ocho**. **Hoy son MÁS, y esta nota no dice
> cuántas: la cifra vigente es SIEMPRE la que §16 deriva de sus cabeceras, y §16 es la única
> sede que la publica.** La que `O15` cita queda como la que era el día en que el Owner
> resolvió —su texto no se reescribe—. **Corregido por `P-21` del documento 22**: esta nota
> decía «Hoy son TRECE» y enumeraba hasta `PN-15` cuando ya existía `PN-16`. Se retira la
> cifra en vez de reescribirla, porque escrita aquí vuelve a caducar con la próxima presión —
> y ya ha caducado dos veces.

### El contenido del BASELINE de `A3`, que es el §6.2 de la directiva y no otra cosa

> **Declarado por el gate final independiente (`M-9`, MEDIO; es `D81`).** `A3` era «BASELINE
> con evidencia» y su gate «baseline aprobado por el Owner», **sin decir de qué**. El §6.2 de
> la directiva enumera catorce preguntas que el baseline debe responder «con evidencia
> razonable», y §15.2 trazaba el apartado 6 entero en una sola fila —lo que hacía invisible
> que 6.2 tenía contenido exigible—. F6 habría inventado el contenido de un gate que el Owner
> aprueba.

**Las CATORCE preguntas del §6.2 son el contrato de `A3`, literalmente y sin reordenar:**

```text
 1 qué existe realmente                    8 qué decisiones están implementadas y nunca
 2 qué está terminado                        se documentaron
 3 qué está parcialmente implementado      9 qué elementos se contradicen
 4 qué está pendiente                     10 qué trabajo pendiente existe
 5 qué está roto                          11 qué elementos son duplicados
 6 qué está desplegado                    12 qué riesgos y restricciones existen
 7 qué decisiones gobiernan actualmente   13 qué conocimiento local debe conservarse
   el proyecto                            14 qué especialización necesita el proyecto
```

**Y se responden OBSERVANDO, no interpretando**, con el patrón que el corpus ya usa: las
cinco variables de `diseno/03-ESCALA-DE-NOVEDAD.md` se evalúan «mirando el producto —el
control repo y sus fuentes—, no interpretando», y cada una declara qué cuenta como verdadera.
El baseline hereda esa disciplina:

```text
CADA RESPUESTA LLEVA      su EVIDENCIA —ruta, revisión y qué se observó—, y su GRADO: OBSERVADO
                          (se vio), DERIVADO (se calculó de algo observado) o DECLARADO (lo
                          dijo alguien, y consta quién)
NINGUNA ES «SE SUPONE»    una pregunta sin respuesta se responde «no se pudo determinar», con
                          el motivo. El gate `A3` admite esa respuesta; lo que NO admite es
                          el silencio
QUIÉN LAS PRODUCE         los items `AUD` enlazados de `A2`–`A3`, cada uno con su propietaria
                          derivada (§18). La pregunta 14 la produce `SIS`, que responde de la
                          especialización
QUIÉN LO APRUEBA          el **Owner**, y su aprobación es el gate. Sin ella `A4` no abre
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
PRECONDICIONES  se conoce la versión instalada · el árbol está limpio ·
                **FASE 0 superada**: certificación Estructural DE ESTA EJECUCIÓN, verificada
                y vigente (§9.6). **Derivado de `O17` vía `D107`; no lo elige F4**
FASES           **FASE 0 · CERTIFICACIÓN ESTRUCTURAL** — precondición PROPIA de esta
                   ejecución, ANTERIOR a toda mutación canónica y a todo intento de
                   elevarse. Invoca **el MISMO contrato compartido `gate:sistema-conforme`**
                   de §9.6. Si falla, la migración se BLOQUEA antes de mutar estado — y
                   antes, por tanto, de tocar nada de las fuentes
                M0 identificar versión instalada y disposición
                M1 crear control repo separado y declarar las fuentes
                M2 migrar PROFILE, PROJECT, decisiones, memoria y documentación global
                M3 migrar ESTADO PERSISTIDO, con su esquema
                M4 sustituir mecanismos retirados y resolver overrides y forks locales
                M5 CERTIFICAR lo nuevo, con lo viejo TODAVÍA EN PIE
                M6 RETIRAR de CADA FUENTE AUTORIZADA kernel, packs y organización — no
                   «del repositorio técnico» en singular, que es la formulación que `E2.0`
                   declara RETIRADA
                M7 VERIFICAR que nada dependía de lo retirado
PROCESO         `M0`–`M5` es **`proceso:SIS`** y `M6`–`M7` es **`proceso:DEU`**. §18 tiene la
DE CADA TRAMO   tabla, y manda
PARTICIPANTES   **con su VÍA de entrada (§8.0)**
                  **FASE 0** · participantes y reparto en §9.6, que es la sede ÚNICA y
                         la misma para los cuatro: `SIS` productor y propietario de la
                         declaración · `VER` el dosier verificador, sin apropiarse de la
                         decisión · `PLT` la maquinaria técnica cuando el contrato vigente
                         se la atribuya · `SEG` su bloqueo por seguridad. **El propietario
                         de este macrocircuito no puede sustituir a `SIS`, y DEBE exigir la
                         certificación antes de continuar** (`O17` vía `D107`)
                `M0`–`M5` · `proceso:SIS`
                  `SIS` vía 1 · `CON` vía 2 (`cambio-construido`) · `VER` vía 2
                  `ENT` vía 3 · «el cambio modifica el runtime»
                `M6`–`M7` · `proceso:DEU`
                  `ARQ` vía 1 · propietaria global. Su obligatoria `plan-tecnico` —el radio
                        de impacto MEDIDO de la retirada— **es entrada de `M5`**: sin ella
                        `M5` no puede certificar lo que `M6` va a retirar. Es la vía por la
                        que `ARQ` participa en la migración, y §18 la nombra
                  `CON` vía 2 · obligatoria **`cambio-construido`**, `capacidad_productora`
                        `CON`. Es quien ejecuta la sustitución de mecanismos de `M4`
                  `VER` vía 2 · obligatoria `evidencia-suficiente`, y verifica `M7`
                  `DOM:condiciones` `SEG:condiciones` `ENT` `USO` `APR` vía 3
LEE             la instalación ANTERIOR entera: `estado/` con su `esquema_estado`, el
                catálogo instalado, `PROFILE.md`, `PROJECT.md`, `SOURCES.toml`, los
                adaptadores, y la organización heredada de CADA fuente.
                **Añadido por `G4`**: §8.3 no declaraba `LEE` ni `ESCRIBE`, y era el único
                macrocircuito con un paso DESTRUCTIVO sobre los repositorios del producto
ESCRIBE         · en el CONTROL REPO desde `M0`: la iniciativa, el estado migrado y sus
                  eventos. Escritura canónica, por §2.6
                · en LAS FUENTES **sólo en `M6`**, y sólo lo que el Owner autorice. `M6` es
                  un conjunto de SOURCE CHANGES gobernados por `C7`: paquete con
                  `escribe_fuentes`, custodia de `PLT`, checkpoint, rama, commit, push, PR y
                  CI **POR FUENTE**
                · NADA en las fuentes antes de `M6`. `M0`–`M5` son de sólo lectura sobre ellas
AUTORIDAD       `SIS` propone · el **OWNER** autoriza `M6`, y su autorización es **POR
                FUENTE**, nombrándola · `VER` verifica `M7`
EJECUTOR        el runtime para el control repo. Para las fuentes, **el reparto es de `C7`**
                (§8.0): `PLT` MATERIALIZA (`C7:82`) y retira ramas abandonadas (`C7:92`);
                `CON` —capacidad CON CUSTODIA por `cambio-construido`— hace rama, commit,
                push y PR POR FUENTE (`C7:83`–`C7:86`); `SEG` puede bloquear el push
                (`C7:85`); `ENT` hace merge y declara convergencia (`C7:88`–`C7:89`); y CI
                verifica cada fuente.
                **Corregido por `I-04`**: ésta era la fila HEREDADA que decía «`PLT` para
                cada source change», y de la que esta tanda generalizó el error a las otras
                cuatro sedes y a §18
GOBIERNO DE LA  **ninguna retirada es automática.** `M6` sólo se ejecuta sobre una fuente si
RETIRADA        se cumplen las CUATRO: `M5` certificó la instalación nueva · el Owner
DESTRUCTIVA     autorizó ESA fuente por su nombre · existe EVIDENCIA de que lo retirado vive
                en la historia de esa fuente · y su rollback por fuente está declarado.
                Falta cualquiera y **la retirada no se ejecuta**, aunque las demás fuentes ya
                hayan convergido. Mientras no converjan todas, el estado es
                **INTEGRACIÓN PARCIAL**
CONDICIÓN PARA  que el artefacto heredado esté SUSTITUIDO **y CERTIFICADO**, no sólo
ELIMINAR        sustituido. Sin sustituto certificado se CONSERVA, y su conservación se
                registra con su motivo
QUÉ SE CONSERVA la HISTORIA y el TRABAJO ABIERTO del producto: issues, TODO, ramas vivas,
SIEMPRE         ideas y deuda registrada. `M6` retira kernel, packs y organización DE ADS;
                **nunca material del producto**
DIFERENCIA      lo que la separa de la adopción: aquí **ya hay estado ADS**. No se
CON A           reconstruye una realidad: se TRADUCE una que ya estaba escrita. Los items
                y paquetes en curso tienen que seguir en curso al otro lado
ESTADO          la iniciativa de migración nace en `M0` · el estado migrado y su
                `esquema_estado` · el evento `migracion` por paso aplicado · el estado
                `INTEGRACIÓN PARCIAL` por fuente mientras `M6` no converja.
                M3 es el paso peligroso: migración de esquema con su migrador y su prueba
HANDOFFS        de `ARQ` a `M5` el `plan-tecnico` con el radio MEDIDO —que es ENTRADA de
                `M5`— · de `SIS` a `PLT` la solicitud de materialización · de `SIS` a `CON`
                los source changes de `M6` · de `CON` a `ENT` el resultado por fuente · de
                `ENT` a `VER` la convergencia para `M7`. **Su QUÉ está en §8.0; las
                INSTANCIAS las crea F6**
EVIDENCIA       **el dosier de FASE 0 que `VER` produce, con la huella de su sujeto (§9.6)** ·
                equivalencia antes/después de items, paquetes y checkpoints · dictamen de
                M5 · salidas de build, pruebas, CI, despliegue y COMPORTAMIENTO AGENTIC en
                M7 — **las CINCO**
GATES           **FASE 0 `gate:sistema-conforme`, antes de M0 y de cualquier mutación
                canónica (§9.6)** ·
                M3 no cierra sin equivalencia demostrada · M5 certificación Integrada del
                control repo nuevo · M6 exige autorización EXPLÍCITA del Owner · **M7 no
                cierra sin las CINCO salidas verdes: build, pruebas, CI, despliegue y
                comportamiento agentic**
CERTIFICACIÓN   **Estructural en FASE 0**, propia de ESTA ejecución y NO heredada de la
                instalación que se migra (§9.6) · Integrada en M5, ANTES de retirar nada.
                Revalidada en M7
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

POR QUÉ LA       **`M6` retira de cada fuente el kernel, los packs y la organización de ADS.**
QUINTA NO ES     Build, pruebas, CI y despliegue pasarían IGUALMENTE en una fuente a la que
OPTATIVA         le han quitado su organización ADS: son verdes sobre el producto, no sobre
                 lo retirado. **La única de las cinco que interroga precisamente lo que `M6`
                 retira es el comportamiento agentic**, y por eso es la que el gate no puede
                 omitir. Es `D99`.
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
                **PROVISIONAL, y con su procedencia** (`F-09`): lo escribe así
                `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` **§3, L79** —donde está el
                calificativo «principio PROVISIONAL»; su §15, L589, lleva el principio SIN el
                calificativo, y citar §15 era impreciso (`I-23`)—, que es **documento de
                trabajo del Owner**, no norma aprobada — y lo llama expresamente «principio
                PROVISIONAL». `grep` sobre las 3 343 líneas de la arquitectura multirrepo
                APROBADA no devuelve ningún mandato sobre la actualización de ADS: **`U` no
                tiene norma aprobada que lo gobierne**. Citarlo sin el calificativo lo
                convertía en norma por transcripción. Que esa ausencia se eleve a materia
                normativa es electivo, y por eso NO se registra como presión: el principio se
                usa, marcado como lo que es
PRECONDICIONES  árbol limpio · sin transiciones en vuelo · certificación vigente ·
                **FASE 0 superada**: certificación Estructural DE ESTA EJECUCIÓN, verificada
                y vigente (§9.6). **Y «certificación vigente» a secas NO la satisface**: la
                regla 4 de `O17` prohíbe deducir Estructural de un nivel superior.
                **Derivado de `O17` vía `D107`; no lo elige F4**
FASES           **FASE 0 · CERTIFICACIÓN ESTRUCTURAL** — precondición PROPIA de esta
                   ejecución, ANTERIOR a toda mutación canónica y a todo intento de
                   elevarse. Invoca **el MISMO contrato compartido `gate:sistema-conforme`**
                   de §9.6. Si falla, la actualización se BLOQUEA antes de mutar estado
                U0 detectar versión candidata
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
PROCESO         `U0`–`U5a` es **`proceso:SIS`**, `U5b` es **`proceso:DEP`** —la única fase de
DE CADA TRAMO   los cuatro macrocircuitos donde hay una dependencia externa de verdad— y `U6`
                vuelve a ser **`proceso:SIS`**. §18 tiene la tabla, y manda
PARTICIPANTES   **con su VÍA de entrada (§8.0)**
                  **FASE 0** · participantes y reparto en §9.6, que es la sede ÚNICA y
                         la misma para los cuatro: `SIS` productor y propietario de la
                         declaración · `VER` el dosier verificador, sin apropiarse de la
                         decisión · `PLT` la maquinaria técnica cuando el contrato vigente
                         se la atribuya · `SEG` su bloqueo por seguridad. **El propietario
                         de este macrocircuito no puede sustituir a `SIS`, y DEBE exigir la
                         certificación antes de continuar** (`O17` vía `D107`)
                `U0`–`U5a` · `proceso:SIS`
                  `SIS` vía 1 · `CON` vía 2 · `VER` vía 2 · `ENT` vía 3 si toca el runtime
                `U5b` · `proceso:DEP` — **y por eso `SEG` y `CON` son OBLIGATORIAS aquí**
                  `PLT` vía 1 · propietaria global de `proceso:DEP`
                  `SEG` vía 2 · obligatoria `condiciones-de-seguridad`, **la capa de SEG
                        ANTES de construir**. Su `autoridad_de_retirada` es *«nadie: `G28` lo
                        hace obligatorio en este proceso y no se retira»*. No es una elección
                  `CON` vía 2 · obligatoria `cambio-construido`
                  `VER` vía 2 · obligatoria `evidencia-suficiente`
                  `DOM:condiciones` `C-DOM` · `ARQ` «el cambio de versión altera contratos» ·
                        `ENT` `C-ENT`  vía 3
                `U6` · `proceso:SIS` · `VER` vía 2
EJECUTOR        **el reparto es de `C7`** (§8.0). En `U5b`, POR FUENTE:
                  `PLT`  MATERIALIZA las fuentes (`C7:82`) y retira ramas abandonadas
                         (`C7:92`). Aquí `PLT` además **participa por la vía 1** —es la
                         propietaria global de `proceso:DEP`—, que es cosa distinta de ser
                         ejecutor y no se confunde con ella
                  `CON`  rama, commit, push y PR — capacidad CON CUSTODIA por su obligatoria
                         `cambio-construido` (`C7:83`–`C7:86`)
                  `SEG`  puede BLOQUEAR el push ante secreto detectado (`C7:85`), además de
                         participar por vía 2 con `G28` haciéndola irretirable
                  `ENT`  merge y convergencia, con Integration Set si hay más de una fuente
                         (`C7:88`–`C7:89`)
                  CI     verifica cada fuente
                **Corregido por `I-04`**
AUTORIDAD       el **Owner** si hay incompatibilidad o retirada, y en el punto de no retorno
                de `U3`
LEE             la distribución nueva y la instalada
ESCRIBE         la distribución instalada y las proyecciones DEL CONTROL REPO en U5a; y
                LAS FUENTES en U5b, sólo el fichero puntero y bajo `C7`. **No el estado**,
                salvo migración de esquema declarada en U3
                **Corregido** (hallazgo `I.3`): F4c decía «la distribución instalada y las
                proyecciones» sin declarar que algunas proyecciones viven en repositorios
                ajenos al control repo
ESTADO          **añadido por `G5`.** §8.4 no lo declaraba, y `U` es el circuito con más
                superficie de estado en juego. Lo que nace, dónde y desde qué fase:
                  · `version_anterior` y `version_objetivo` — en la iniciativa de `U0`
                  · `migraciones_aplicables[]` con su orden — resuelto en `U2`
                  · `punto_de_no_retorno` — `U3`, y queda registrado con su fecha y autoridad
                  · `instantanea_previa` — DURABLE y VERSIONADA, en
                    `estado/instantaneas/<version>/`, plano DURABLE. Es la alternativa
                    admitida al migrador inverso, y por eso **no puede ser operacional**: si
                    no sobreviviera a un clon nuevo no serviría para el rollback que la
                    justifica. `G5` señaló que no tenía ni ubicación ni plano ni ciclo
                  · `progreso_por_pasos` — qué paso de `U0`–`U6` se completó, en la
                    iniciativa, para que la reanudación no dependa del chat
                  · `INTEGRACIÓN PARCIAL` por fuente en `U5b`, hasta que todas convergen
                  · `bloqueo` — mientras `U` está en vuelo, ninguna otra actualización
                    arranca, y se declara con el mismo mecanismo de solapamiento de §2.6.9
HANDOFFS        de `SIS` a `PLT` la solicitud de materialización · de `PLT` a `CON` el
                paquete de `U5b` con su `escribe_fuentes` · de `SEG` a `CON` las condiciones
                ANTES de construir · de `CON` a `ENT` el resultado por fuente · de `ENT` a
                `VER` la convergencia para `U6`. **Su QUÉ está en §8.0; las INSTANCIAS las
                crea F6**
EVIDENCIA       **el dosier de FASE 0 que `VER` produce, con la huella de su sujeto (§9.6)** ·
                la vista comprensible del cambio que el §14.2 del brief pide
GATES           **FASE 0 `gate:sistema-conforme`, antes de U0 y de cualquier mutación
                canónica (§9.6)** · U3 aprobado antes de U4 · U6 certificación
CERTIFICACIÓN   **Estructural en FASE 0**, propia de ESTA ejecución y NO heredada de la
                versión instalada (§9.6) · y después, el nivel que tuviera antes, revalidado. Una actualización que baja el
                nivel alcanzado es un fallo, no un resultado
ROLLBACK        ver «Compatibilidad y rollback DEL ESTADO», abajo. NO basta con volver la
                distribución atrás. Y U5b tiene el SUYO, POR FUENTE, con estado INTEGRACIÓN
                PARCIAL mientras no converjan todas (§6.7)
REANUDACIÓN     **desde el ESTADO, nunca desde el chat.** `U0`–`U3` por el
                `progreso_por_pasos` de la iniciativa; `U4` por el evento `preparada` de su
                transacción; `U5b` por el estado `INTEGRACIÓN PARCIAL` de cada fuente; `U6`
                por las celdas de certificación. Una actualización interrumpida se retoma
                **en otra sesión y en otra máquina**, que es lo que `D30` exige y `G5`
                encontró sin soporte declarado
CIERRE          U6 superado y la versión instalada es la candidata
```

> **Y una segunda sede del Owner, registrada por `N-05`.** El mismo principio aparece en
> `docs/evolucion/ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` **L914–916**, §7, con la
> **misma frase literal** y bajo el rótulo «**Principio aceptado**». La afirmación de arriba
> —«lo escribe así»— es exacta para la fuente que cita e **incompleta para el corpus**.
> **Qué relación hay entre los dos rótulos, dicho sin tocar ninguno de los dos documentos:**
> los dos son **material de trabajo del Owner y ninguno es normativo** —`ADS-PENDIENTES`
> L3–L6 se autodeclara «no es todavía especificación normativa»—, luego **ninguno de los dos
> calificativos tiene fuerza de norma**, y la diferencia entre ellos no cambia ninguna
> obligación. Lo que decide el estatus del principio no es el adjetivo que uno u otro
> documento le ponga, sino **si existe norma APROBADA que lo imponga — y no existe**:
> `grep` sobre las 3 343 líneas de `ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` no devuelve
> mandato sobre actualizar ADS instalado. **Por eso `F-09` sigue siendo correcta en su
> sustancia** —§8.4 clasifica el principio como PROVISIONAL y no registra presión—, y lo
> único que faltaba era decir que el Owner lo ha escrito dos veces con dos adjetivos
> distintos. **Queda dicho. No se modifica ninguno de los dos documentos del Owner.**

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

**Y `gate:sistema-conforme` —la prueba del nivel Estructural— tiene desde hoy PRODUCTOR,
SUJETO, EVIDENCIA, VIGENCIA y CONDICIÓN DE INVALIDACIÓN, en §9.6.** Esta fila deja de ser su
única aparición en el documento. **Derivado de `O17` vía `D107`, y no elegido por F4.**

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

PRODUCTOR DE CADA **la cadena de arriba y su REGLA DURA se conservan ÍNTEGRAS.** Lo que se
NIVEL, Y EL DEL   añade —**derivado de `O17` vía `D107`, y no elegido por F4**— es que
ESTRUCTURAL       **el nivel Estructural TIENE PRODUCTOR**, que es lo que le faltaba y lo que
                  hacía inaplicable la regla dura:
                    estructural  **la FASE 0 de CADA UNO de los cuatro macrocircuitos**, con
                                 `SIS` como productor y propietario de la declaración,
                                 invocando el contrato compartido `gate:sistema-conforme`.
                                 **Su contrato entero está en §9.6**, que es su sede única
                    operativo    `INS-4`
                    integrado    `A9` · `M5` · `INS-7` · revalidado en `M7` y en `U6`
                    completo     **SIN PRODUCTOR DECLARADO, y se dice en vez de taparlo.** Lo
                                 que esta casilla contenía —«los escenarios de §14 ejecutados
                                 sobre un producto real»— es EVIDENCIA, no una fase que lo
                                 produzca, y la regla 12 de `O17` exige PRODUCTOR propio a
                                 cada nivel. `O17` da productor al Estructural **y a ningún
                                 otro**, luego resolverlo aquí sería ampliar una resolución
                                 del Owner: **no se amplía**, y queda como trabajo futuro con
                                 propietario, fase y prueba en §9.6. Que §9.4 declare el nivel
                                 HOY inalcanzable explica que no se ALCANCE, no que no tenga
                                 productor DECLARADO
                  **Cada nivel conserva PRODUCTOR, EVIDENCIA, SUJETO, VIGENCIA y CONDICIÓN DE
                  INVALIDACIÓN propios** —regla 12 de `O17`—, y **un nivel superior NO implica
                  por sí mismo que Estructural siga vigente** —regla 4—: es lo que «NIVEL
                  ALCANZADO» ya dice arriba, y `O17` lo hace explícito para que nadie lo
                  deduzca al revés
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

> **`O12` ES HOY SATISFACIBLE, y por qué recorrido. Derivado de `O17` vía `D107`.** Hasta
> `O17`, no lo era **por ningún recorrido**: «NIVEL ALCANZADO» (§9.2) exige que todos los
> niveles presupuestos estén `verificado` y vigentes, Integrado presupone Operativo y
> Operativo presupone Estructural, **y ninguna fase de ninguno de los cuatro macrocircuitos
> producía el Estructural** — `gate:sistema-conforme` tenía una sola aparición en todo este
> documento y era su propia definición. Es el GRAVE nº 2 del documento 22 (`P-06`).
> **Con la FASE 0 de §9.6, cada ejecución produce su Estructural**, y el recorrido completo
> queda escrito en §9.6, bajo «LO QUE ESTO HACE SATISFACIBLE». **Lo que sigue sin productor
> nombrado —la Operativa de la adopción— queda registrado allí como trabajo futuro con
> propietario, fase y prueba, y NO se resuelve aquí: `O17` da productor al nivel Estructural
> y a ninguno más, y ampliarla sería reinterpretarla.**

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
            INS-6», y eso es falso en el punto donde se invoca. La aplicabilidad se calcula
            sobre las fuentes DECLARADAS, y `SOURCES.toml` se rellena en **INS-2**; la Integrada
            se certifica en **INS-7**, después de INS-2 y de INS-6. En INS-7 el producto tiene, por
            construcción, las fuentes que INS-2 declaró. El caso de 0 fuentes EXISTE, y no es
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


## 9.6 · `gate:sistema-conforme` — el contrato del nivel Estructural y su FASE 0

> **TODO LO DE ESTA SECCIÓN ES DERIVADO DE `O17`, VÍA `D107`. Nada de ello lo eligió F4.**
> La pregunta la formuló el GATE INDEPENDIENTE DE CERTIFICACIÓN —documento 22— como su única
> clase `B`, con tres alternativas redactadas palabra por palabra. **El Owner eligió la (b)**
> —que lo produzca cada macrocircuito al arrancar, como precondición propia— y **aceptó
> expresamente su coste**: un gate más en los cuatro recorridos, y migración y actualización
> más caras. `O17` está íntegra en `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md` §2, y su
> propagación es `D107`, §1. **Lo único que F4 aporta aquí es el reparto de la elección (b)
> por las sedes vigentes**, y por eso esta sección se declara derivada y no decidida.
>
> **El vacío que cierra** —`P-06` del documento 22, GRAVE nº 2—: `gate:sistema-conforme`
> tenía **una sola aparición en todo el documento 11, y era su propia definición** en §9.1.
> Ninguna fase de §8.1, §8.2, §8.3 ni §8.4 lo producía ni lo invocaba. Sin celda de
> Estructural `verificado` y vigente, la definición de «NIVEL ALCANZADO» de §9.2 impedía
> elevar nada, **y `O12` no era satisfacible por ningún recorrido**. **La cadena de §9.2 y su
> REGLA DURA no se reescriben**: se conservan enteras, y dejan de ser inaplicables.

**UN SOLO CONTRATO, INVOCADO CUATRO VECES.** Es la regla 6 de `O17`: los cuatro macrocircuitos
invocan **el MISMO contrato y el MISMO mecanismo compartido**, y **no se crean cuatro
implementaciones divergentes**. Ésta es su sede única: §8.1, §8.2, §8.3 y §8.4 **la invocan y
no la reescriben**, y §18 la mapea fase a fase.

**JERARQUÍA CON §8.0, declarada aquí porque había DOS reglas de desempate solapadas y de
sentido contrario.** §8.0 dice «SEDE CANÓNICA la tabla de §18 … si alguna vez difieren, MANDA
§18»; esta sede decía «si alguna vez difieren, manda ésta». Las dos se solapaban justo sobre la
FASE 0. **Se jerarquizan así, y el reparto no deja zona muerta: §18 manda sobre el MAPEO —qué
fase, qué proceso de `b.16`, qué participantes y por qué vía, qué entra y qué sale de cada
tramo—; ESTA SEDE manda sobre el CONTENIDO DEL CONTRATO `gate:sistema-conforme` —qué afirma,
quién lo produce, qué exige su entrada, dónde se persiste su salida, qué lo bloquea y qué lo
cierra—. Lo que no es contrato es mapeo, y no hay tercera cosa.** Y la primera divergencia real
que el solapamiento produjo —la vía de `SEG` en las cuatro filas `FASE 0` de §18— se resuelve
por esta jerarquía **a favor de esta sede**, porque la vía de participación de una capacidad en
el contrato compartido es contenido del contrato y no mapeo de tramos. §8.0 lleva la misma
frase, para que la jerarquía se lea desde las dos puntas.

```text
CONTRATO           `gate:sistema-conforme`
QUÉ AFIRMA         lo que §9.1 ya atribuye al nivel Estructural: los ficheros, contratos y
                   referencias existen y son coherentes. **NO afirma que el sistema arranque**
PRODUCTOR Y        **`SIS`.** Emite la declaración Estructural y responde de ella. §9.1 ya le
PROPIETARIO        daba el nivel; lo que faltaba era la fase que lo produce
DOSIER Y           **`VER`**, que produce el dosier o evidencia verificadora **SIN apropiarse
EVIDENCIA          de la decisión final**: verifica, y no certifica
MAQUINARIA         **`PLT`**, que ejecuta la maquinaria técnica **cuando el contrato vigente
TÉCNICA            se la atribuya** — no por defecto, y nunca en lugar de `SIS`
BLOQUEO POR        **`SEG`** conserva íntegra su capacidad de BLOQUEO cuando la estructura
SEGURIDAD          incumpla seguridad. Su veto no lo levanta ninguna de las otras tres, ni el
                   propietario del macrocircuito
EL PROPIETARIO DE  **NO puede sustituir a `SIS`** en la certificación, y **DEBE EXIGIRLA**
CADA MACROCIRCUITO antes de continuar. En `N`, `A`, `M` y los tramos `SIS` de `U` ese
                   propietario ES `SIS` por otra vía —la vía 1 del proceso—, y **eso no lo
                   dispensa de nada**: certifica como productor de esta sección, con su
                   sujeto, su evidencia y su huella, no por ser el dueño del recorrido. En
                   `U5b` el propietario global es `PLT`, y **`PLT` no certifica: exige**
```

### El SUJETO — los SEIS identificadores de la regla 7, y son un MÍNIMO

```text
1 PRODUCTO O          qué se certifica: `instalacion:transversal/<producto>` o el sujeto
  INSTALACIÓN         certificable que corresponda (§9.2)
2 EJECUCIÓN DEL       **CUÁL** de las ejecuciones, **por el identificador de la EJECUCIÓN y
  MACROCIRCUITO       NO por el de la iniciativa** — que durante la FASE 0 todavía no existe y
                      NO PUEDE existir: la regla 5 y `X-S5` fijan que «una iniciativa abierta
                      ya es estado». Es lo que hace que la certificación sea de ESTA ejecución
                      y no de otra, y sin él las reglas 1, 3 y 9 no son evaluables.
                      **DÓNDE NACE — dicho aquí porque sin decirlo la fase NO ES EJECUTABLE, y
                      derivado de `O17` vía `D107`, no elegido por F4:** lo ACUÑA la propia
                      FASE 0, y es la **HUELLA de su disparador junto con los otros cinco
                      identificadores de este sujeto**. Direccionado por CONTENIDO y no
                      monotónico, como todo identificador de este documento (§2.7): **no
                      consume contador, no abre iniciativa, no escribe canónico** — luego no
                      muta estado y la regla 2 se conserva entera. No es de la forma
                      `<PREFIJO><n>` y por eso no entra en el censo de espacios de nombres de
                      `D83`. La iniciativa, cuando la abren `INS-0`, `A0`, `M0` o `U0`, **lo
                      ADOPTA por referencia y no lo re-acuña**; y si el disparador cambia, la
                      huella cambia, que es exactamente lo que la regla 8 quiere
3 REVISIÓN DEL        qué kernel se comprueba, por su revisión
  KERNEL
4 REVISIÓN DE         qué esquemas y qué contratos APLICABLES, por su revisión. No «los del
  SCHEMAS Y           kernel» en bloque: los aplicables a ESTE sujeto
  CONTRATOS
5 CONFIGURACIÓN Y     `PROFILE`, `PROJECT`, `SOURCES.toml`, packs, adaptadores y overrides
  FUENTES             relevantes, cada uno por su revisión
  RELEVANTES
6 HUELLA DE LA        la huella del conjunto de evidencia. **Es el campo que decide la
  EVIDENCIA           reutilización de abajo**: sin él, reutilizar es presumir

MÍNIMO, NO CENSO      la regla 7 dice «como mínimo». Un sujeto puede llevar más
                      identificadores; **no puede llevar menos**, y omitir uno es un fallo
                      del gate, no una simplificación
```

### VIGENCIA e INVALIDACIÓN

```text
VIGENCIA          una declaración Estructural es vigente mientras (i) su celda esté
                  `verificado`, (ii) no haya vencido por caducidad y (iii) **ninguno de los
                  SEIS identificadores de su sujeto haya cambiado**
INVALIDACIÓN      los triggers de §9.3 para Estructural —cambia el corpus instalado · cambia
                  un esquema · falla un validador— **MÁS el cambio de cualquiera de los
                  seis**. §9.3 no se reescribe: se le añade que el sujeto es parte de lo que
                  se compara, y los tres triggers que ya tenía son casos suyos
NO HEREDA         **regla 3:** superar una ejecución anterior NO certifica la actual. Una
                  declaración pertenece a la ejecución que la produjo, y a ninguna otra
NO SE DEDUCE      **regla 4:** un nivel superior verificado NO implica por sí mismo que
DESDE ARRIBA      Estructural siga vigente. §9.2 ya lo dice con «NIVEL ALCANZADO»; aquí queda
                  explícito, porque era exactamente la deducción que `U` hacía al pedir sólo
                  «certificación vigente»
```

### REUTILIZACIÓN DE EVIDENCIA — reglas 8, 9 y 10, y las tres a la vez

```text
QUÉ SE PUEDE       la EVIDENCIA MATERIAL anterior —salidas de los validadores, dosier de
REUTILIZAR         `VER`— **ÚNICAMENTE si se DEMUESTRA que TODAS sus entradas y TODAS sus
                   huellas siguen IDÉNTICAS** (regla 8). Demostrar no es afirmar: se compara
                   huella a huella contra los seis identificadores del sujeto
QUÉ EMITE CADA     **SU PROPIA declaración Estructural, vinculada a ESA ejecución** (regla 9),
EJECUCIÓN          también cuando toda la evidencia se reutilizó. Reutilizar evidencia y
                   emitir declaración son cosas DISTINTAS: lo primero es un ahorro de
                   ejecución, lo segundo es la certificación
QUÉ NO SE PUEDE    **copiar una certificación anterior**, y **presumirla vigente**. Las dos
HACER NUNCA        están prohibidas por la regla 10, y **ninguna condición las habilita**: ni
                   que las huellas coincidan, ni que el nivel superior siga verde
SI UNA SOLA        no hay reutilización: la evidencia se REPRODUCE. Una huella distinta es
HUELLA DIFIERE     una entrada distinta, y una entrada distinta es otro sujeto
```

### La FASE 0, IGUAL EN LOS CUATRO — entrada, salida, gate y cierre

```text
CUÁNDO             **ANTES de cualquier mutación canónica del macrocircuito** y **ANTES de
                   todo intento de elevarse** a Operativa, Integrada o Completa (regla 2).
                   En `N` va antes de `INS-0` —que ya publica—, en `A` antes de `A0`, en `M`
                   antes de `M0` y en `U` antes de `U0`
CUÁNTAS VECES      **EXACTAMENTE UNA por ejecución** (regla 1). Ni cero ni dos
ENTRADA            el disparador del macrocircuito, con CERO mutaciones hechas · el SUJETO de
                   los seis identificadores, resuelto · la evidencia anterior con sus
                   huellas, si la hay y sólo para el contraste de la regla 8
PARTICIPANTES      `SIS` productor y propietario · `VER` el dosier · `PLT` la maquinaria
DERIVADOS          cuando el contrato se la atribuya · `SEG` el bloqueo. **`ENC` no
                   participa**: la FASE 0 es anterior a que haya ruta, y §8.0 ya fija que
                   encuadrar no es depositar capa
SALIDA             **la declaración Estructural DE ESTA EJECUCIÓN**, con su sujeto, su
                   evidencia, su huella y su vigencia · la celda
                   `aspecto:certificacion/estructural` del sujeto, con el contrato de §3.5 y
                   con `responsables` **sólo si hay desviación del reparto por defecto, y con
                   su motivo**
DÓNDE SE PERSISTE  **Dicho aquí porque sin decirlo la fase NO ES EJECUTABLE, e IGUAL EN LOS
LA SALIDA          CUATRO** — derivado de `O17` vía `D107`, y no elegido por F4. `estado/`
                   nace en `INS-0` (§8.1, `D30`), y su equivalente en `A0`, `M0` y `U0`: la
                   FASE 0 es ANTERIOR a los cuatro, luego **no puede escribir en `estado/`, y
                   no escribe**. Escribe en el **SOPORTE DURABLE DE LA FASE 0**: soporte
                   propio, anterior al `estado/` del macrocircuito, que contiene **la
                   declaración, su dosier y su celda, y NADA del macrocircuito**. Y entonces:
                     · la PRIMERA fase que crea `estado/` —`INS-0`, `A0`, `M0`, `U0`—
                       **INCORPORA** la declaración a `estado/cobertura/` (§2.4) como su
                       primer acto, **sin reemitirla y sin volver a certificar**. Incorporar
                       NO es certificar: si la huella incorporada no es idéntica a la emitida
                       es OTRO sujeto, y la regla 8 lo rechaza
                     · **la celda existe desde la FASE 0.** Lo que cambia al entrar en
                       `INS-0`/`A0`/`M0`/`U0` es DÓNDE reside, no quién la produjo ni cuándo
                     · si el gate BLOQUEA, **no hay nada que incorporar y nada que deshacer**:
                       el soporte de la FASE 0 no es estado canónico del macrocircuito, y ésa
                       es la razón exacta de que la regla 2 siga siendo cierta con la salida
                       ya escrita. La frontera no es «no escribir nada»: es **no escribir
                       nada DEL MACROCIRCUITO**
                   **Materializar este soporte es kernel, y F4 no toca `kernel/`**: queda
                   abajo como trabajo futuro, con propietario, fase y prueba
QUÉ PASA SI EL     **la FASE 0 NO SE REANUDA: se REPITE ENTERA.** No tiene mutación canónica
CHAT SE AGOTA      que preservar, y tanto su identificador de ejecución como su declaración
DENTRO DE ELLA     son derivados por contenido: repetirla sobre el mismo disparador produce
                   **la MISMA** declaración, no una segunda, con lo que la regla 1 —«ni cero
                   ni dos»— se conserva. Por eso «REANUDACIÓN … desde `INS-0`» de §8.1 sigue
                   siendo cierta y **no se contradice con esta fase**
GATE               `gate:sistema-conforme`. **Si FALLA, el macrocircuito se BLOQUEA ANTES DE
                   MUTAR ESTADO** (regla 5): no se abre la iniciativa, **no se escribe ningún
                   canónico DEL MACROCIRCUITO** —ni `estado/`, ni item, ni celda suya— y no se
                   toca ninguna fuente. Bloquear después de abrir la iniciativa YA es haber
                   mutado estado. **La declaración propia de la FASE 0 no es una excepción a
                   esto: vive en su soporte propio, arriba, y por eso un bloqueo no deja nada
                   que deshacer**
CONDICIÓN DE       la declaración emitida, y su celda `verificado` y vigente para ESTA
CIERRE DE FASE 0   ejecución. **Sin ella la fase siguiente no abre**, y ningún nivel superior
                   es alcanzable por la definición de §9.2
QUÉ NO HACE        no sustituye a `INS-3`, que especializa y verifica la organización ya
FASE 0             materializada; no sustituye a `A0`, que fija perímetro y modo no
                   destructivo; y **no certifica ningún nivel superior**
```

### Tabla adversarial de la FASE 0

**No son filas de la tabla adversarial de §2.6.7**, que sigue en **cuarenta y seis filas y
cuarenta y seis identificadores `X<nn>`**, ni de las **OCHO** `X-A`–`X-H` de §2.9. Llevan
familia propia, `X-S`, y son contrato de prueba igual que aquéllas: cada una declara qué se
prepara, qué se intenta y qué resultado es exigible. **Ninguna se ha ejecutado**, como las
demás. Escribir el contrato de una prueba no es la prueba.

| | escenario adversarial | resultado exigido |
|---|---|---|
| `X-S1` | ejecutar un macrocircuito **OMITIENDO la FASE 0** y mutar estado canónico | **FALLA**, nombrando el macrocircuito y la mutación intentada. La certificación Estructural es PRECONDICIÓN, no un paso recomendado: sin ella la primera mutación está prohibida (regla 2 de `O17`) |
| `X-S2` | presentar como Estructural de esta ejecución una **certificación de una ejecución anterior, copiada** | **FALLA.** La regla 10 prohíbe copiar una certificación anterior y prohíbe presumirla vigente. Se exige la declaración propia de ESTA ejecución (regla 9), aunque toda la evidencia material se haya reutilizado |
| `X-S3` | **reutilizar evidencia con UNA SOLA HUELLA DISTINTA** en cualquiera de los identificadores de su sujeto —los de la regla 7, enumerados arriba— | **FALLA**, nombrando el identificador que difiere. La regla 8 exige que TODAS las entradas y huellas sigan idénticas: **una basta para invalidar la reutilización**, y entonces la evidencia se reproduce |
| `X-S4` | **elevarse a Operativa, Integrada o Completa sin Estructural vigente DE ESA EJECUCIÓN** | **FALLA** por la definición de «NIVEL ALCANZADO» de §9.2, y el gate lo dice con esas palabras. Un nivel superior ya `verificado` **NO** vale como prueba de que Estructural siga vigente (regla 4) |
| `X-S5` | la FASE 0 **falla** y el macrocircuito continúa hasta abrir su iniciativa | **FALLA.** La regla 5 exige BLOQUEAR **antes** de mutar estado, y **una iniciativa abierta ya es estado**: es la frontera exacta, no «antes de tocar las fuentes» |
| `X-S6` | emitir **DOS** declaraciones Estructurales en una misma ejecución | **FALLA.** La regla 1 fija exactamente una por ejecución: dos son dos verdades sobre el mismo hecho, que es lo que §2.9 y §3.3 prohíben en todo el documento |
| `X-S7` | el propietario del macrocircuito **emite él mismo** la declaración en vez de `SIS`, o **continúa sin exigirla** | **FALLA en los DOS casos.** No puede sustituir a `SIS` y debe exigirla: son las dos mitades del mismo reparto, y satisfacer una no dispensa de la otra |
| `X-S8` | `SEG` bloquea por incumplimiento de seguridad de la estructura y la FASE 0 se declara superada igualmente | **FALLA.** El veto de `SEG` no lo levantan `SIS`, `VER`, `PLT` ni el propietario del macrocircuito |
| `X-S9` | emitir la declaración con un SUJETO al que le falta uno de los identificadores obligatorios de la regla 7 | **FALLA**, nombrando el que falta. La regla 7 es un mínimo, y omitir la huella de la evidencia convierte cualquier reutilización posterior en una presunción |
| `X-S10` | la FASE 0 **abre la iniciativa** —o consume un contador de iniciativa— para poder resolver el identificador nº 2 de su sujeto | **FALLA**, y es la prueba de que el identificador de la EJECUCIÓN no es el de la iniciativa. El identificador nº 2 lo ACUÑA la FASE 0 por HUELLA de su disparador y de los otros cinco: **sin abrir nada y sin consumir contador**. Abrirla es mutar estado (regla 2, `X-S5`) |
| `X-S11` | la FASE 0 **escribe su celda dentro de `estado/`** —o el macrocircuito abre `INS-0`/`A0`/`M0`/`U0` **sin INCORPORAR** la declaración ya emitida, o la incorpora con **otra huella** | **FALLA en los TRES casos.** `estado/` nace después de la FASE 0: escribir ahí antes es imposible y pretenderlo oculta que la fase no tenía soporte. No incorporarla deja el nivel Estructural sin sede canónica. Incorporarla con otra huella es OTRO sujeto, y la regla 8 lo rechaza |

### LO QUE ESTO HACE SATISFACIBLE — `O12`, y por qué recorrido

```text
`O12` EXIGE        Integrada + baseline aprobado + ningún desconocido crítico sin clasificar
                   (§9.4). Las tres, no dos
POR QUÉ NO ERA     porque «NIVEL ALCANZADO» exige que **los niveles presupuestos estén todos
SATISFACIBLE       `verificado` y vigentes**; Integrado presupone Operativo, Operativo
                   presupone Estructural, **y Estructural no lo producía nadie**. Ninguno de
                   los cuatro recorridos podía elevarse, y `O12` era invocable y no
                   alcanzable — el mismo modo de fallo que `G-3`/`D76` cerró un piso más abajo
POR QUÉ LO ES HOY  porque **cada ejecución produce su Estructural en FASE 0**. El recorrido,
                   entero y por macrocircuito:
                     `N`  FASE 0 Estructural → `INS-4` Operativa → `INS-7` Integrada.
                          `INS-5` produce el BASELINE, que aprueba el Owner, y la
                          CLASIFICACIÓN DE DESCONOCIDOS CRÍTICOS como entregable propio.
                          `INS-7` = `O12`, con las tres condiciones y **un productor cada
                          una** (§8.1). **Éste es el recorrido completo, sin hueco**
                     `A`  FASE 0 Estructural → `A9` Integrada → `A3` el baseline aprobado
                          por el Owner → `A10` = `O12`. **Con la salvedad de abajo**
                     `M`  FASE 0 Estructural → `M5` Integrada con lo viejo TODAVÍA EN PIE →
                          `M7` revalidada tras retirar. `M` no arranca programación.
                          **Con la salvedad de abajo, que es la MISMA que la de `A`**
                     `U`  FASE 0 Estructural → `U6` revalida el nivel que tuviera antes. `U`
                          **no invoca `O12`** y §18 lo dice: una actualización no arranca
                          programación
LAS SALVEDADES,    **enumeradas aquí, TODAS las que hay; el cardinal no se escribe** —regla de
DICHAS Y NO        §0 sobre titulares de enumeración—. Son las de la cadena de niveles, no las
TAPADAS            de la FASE 0:
                     · **ADOPCIÓN.** `A` sigue sin fase que produzca su OPERATIVA con nombre
                       propio, y `A9` la presupone por la cadena de §9.2
                     · **MIGRACIÓN — EL MISMO HUECO, Y SE DICE CON LAS MISMAS LETRAS.** `M3`
                       migra el ESTADO PERSISTIDO «con su esquema» (§8.3), y §9.3 declara que
                       «cambia la disposición del estado» INVALIDA el nivel Operativo. La
                       única Operativa que un producto migrado traía es la que produjo `INS-4`
                       en su instalación original, y **`M3` la vence**. **Ninguna fase
                       `M0`–`M7` la reproduce** y §8.3 no la nombra: su fila CERTIFICACIÓN va
                       de Estructural en FASE 0 a Integrada en `M5` sin pasar por ella. Luego
                       **`M5` certifica Integrada sobre un presupuesto VENCIDO**, que es el
                       modo de fallo que §9.2 describe en «CONSECUENCIA» y el que `O17` cerró
                       un piso más abajo. **Declararlo es para lo que esta sede existe;
                       callarlo mientras se declaraba el de `A`, cuatro líneas más arriba, era
                       el defecto — y el lector infería que los otros recorridos estaban
                       completos**
                     · **`N` y `U` NO lo tienen, y consta, porque una enumeración de huecos
                       que sólo nombra los rotos no dice nada del resto:** `INS-4` produce la
                       Operativa de `N` con nombre propio, y `U6` REVALIDA el nivel VIGENTE
                       sin invocar `O12` —§18 lo dice—, luego `U` no arrastra el hueco de
                       ningún otro
                   **`O17` da productor al nivel Estructural y a NINGÚN otro**, luego resolver
                   cualquiera de los dos huecos aquí sería ampliar una resolución del Owner.
                   **No se amplía.** Quedan registrados abajo como trabajo futuro, con
                   propietario, fase y prueba
```

### Trabajo futuro que esta sede NO puede hacer, con propietario, fase y prueba

```text
MATERIALIZAR EL      PROPIETARIO **`SIS`** · FASE **F6** · el contrato `gate:sistema-conforme`
CONTRATO EN EL       vive hoy sólo en este documento: `kernel/` no lo declara con productor,
KERNEL               sujeto, vigencia ni invalidación, y **F4 no toca `kernel/`** — lo dice
                     §19 y lo repite §8.0. PRUEBA POSTERIOR: un barrido que exija que
                     `gate:sistema-conforme` esté declarado en el kernel con **los seis
                     identificadores de sujeto**, su productor, su vigencia y su condición de
                     invalidación, y que **FALLA HOY, y tiene que fallar**

EL PRODUCTOR DE LA   PROPIETARIO **el Owner** · FASE **F5** · `O17` resuelve el productor del
OPERATIVA EN LA      nivel Estructural **y de ninguno más**; `A9` certifica Integrada y su
ADOPCIÓN             Operativa presupuesta no la produce ninguna fase de §8.2. **No se
                     resuelve aquí ni se registra como presión nueva**: el hueco lo levantó
                     `P-06` del documento 22 dentro de la misma clase `B` que el Owner acaba
                     de responder, y ampliar su respuesta sería reinterpretarla. PRUEBA
                     POSTERIOR: que `A9` no pueda cerrar sin una celda
                     `aspecto:certificacion/operativo` `verificado` y vigente **de esa misma
                     ejecución**. **FALLA HOY**

EL SOPORTE DURABLE   PROPIETARIO **`SIS`** · FASE **F6** · el bloque «DÓNDE SE PERSISTE LA
DE LA FASE 0,        SALIDA» de arriba dice QUÉ es y QUÉ contiene, y ésa era la pieza que
MATERIALIZADO EN     faltaba para que la fase fuese ejecutable. **Materializarlo —su ruta, su
EL KERNEL            formato y el acto de INCORPORACIÓN que ejecutan `INS-0`, `A0`, `M0` y
                     `U0`— es kernel, y §19 prohíbe a F4 tocar `kernel/`.** PRUEBA POSTERIOR:
                     ejecutar una FASE 0 que BLOQUEA y exigir que **no exista ni un byte bajo
                     `estado/`** al terminar; y ejecutar una que SUPERA y exigir que la celda
                     `aspecto:certificacion/estructural` aparezca en `estado/cobertura/` con
                     **la huella idéntica** a la emitida antes de `INS-0`. **FALLA HOY, y
                     tiene que fallar**

EL PRODUCTOR DE LA   PROPIETARIO **el Owner** · FASE **F5** · el hueco es el MISMO que el de la
OPERATIVA EN LA      adopción y está declarado arriba con las mismas letras: `M3` invalida la
MIGRACIÓN            Operativa heredada por el trigger literal de §9.3 y ninguna fase
                     `M0`–`M7` la reproduce, con lo que `M5` certifica Integrada sobre un
                     presupuesto vencido. **No se resuelve aquí ni se registra como presión
                     nueva**, por la misma razón que en la adopción: `O17` resuelve el
                     productor del Estructural y de ningún otro. PRUEBA POSTERIOR: que `M5` no
                     pueda cerrar sin una celda `aspecto:certificacion/operativo` `verificado`
                     y vigente **posterior a `M3` y de esa misma ejecución**. **FALLA HOY**

EL PRODUCTOR DEL     PROPIETARIO **el Owner** · FASE **F5** · §9.2 deja la casilla del nivel
NIVEL `completo`     `completo` sin fase que lo produzca, y la regla 12 de `O17` exige
                     PRODUCTOR propio a cada nivel. Lo que hay hoy en esa casilla es
                     EVIDENCIA —los escenarios de §14—, no un productor. Es la misma clase que
                     los dos huecos de arriba y se resuelve por la misma puerta.
                     PRUEBA POSTERIOR: que ninguna celda pueda alcanzar `completo` sin una
                     fase nombrada que la produzca, con su sujeto, su evidencia, su vigencia y
                     su condición de invalidación. **FALLA HOY**

`U` Y EL FRENO 3     PROPIETARIO **el Owner** · FASE **F5** · con la `FASE 0` dentro de la
DE `a.7`             racha, `U` presenta TRES items `SIS` consecutivos y el FRENO 3 **sí llega
                     a evaluarse** (§8.0, re-derivado). Lo que sostiene hoy a `U` es la
                     cláusula LITERAL de excepción de `a.7`, no la cuenta propia. **Si el
                     Owner no considerase que una actualización de ADS es «construir o migrar
                     el propio kernel/runtime», `U` necesitaría excepción del Owner — y eso no
                     se decide aquí.** PRUEBA POSTERIOR: un barrido que derive de §18 la racha
                     `SIS` máxima de cada macrocircuito y **falle si alguna supera dos sin una
                     excepción escrita con su fundamento**

AÑADIR EL SUJETO A   PROPIETARIO **`SIS`** · FASE **F6** · §9.3 enumera los triggers de
LOS TRIGGERS DE      invalidación por nivel y no menciona el sujeto, que esta sección añade
`nivel-certificacion` para Estructural. La NORMA vive en el esquema de clase
                     `nivel-certificacion` (§9.2), que es kernel. PRUEBA POSTERIOR: que un
                     cambio en cualquiera de los seis identificadores **venza** la celda
                     Estructural del sujeto sin que nadie tenga que acordarse de editarla,
                     que es el mismo mecanismo que §6.5 celebra para el adaptador
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
| 1 | **proyecto nuevo** | distribución instalada | **`estado/` nace en `INS-0`**, con `INI-001` y el item real `SIS-001` | `SIS` propietaria global · `CON` y `VER` · `PLT` materializa (`C7:82`) · runtime | **`FASE 0` `gate:sistema-conforme`, ANTES de toda mutación canónica (§9.6; `O17` vía `D107`)** · `INS-4` Operativa · **`INS-5` baseline aprobado por el Owner** · `INS-7` = `O12` | `workspace check` · prueba de humo · checkpoint recuperado | **por el checkpoint del paquete de `SIS-001`, desde `INS-0`.** Ningún tramo depende del chat. **La `FASE 0` no se reanuda: se REPITE ENTERA y produce la MISMA declaración, porque no muta nada y su identificador es derivado por contenido (§9.6)** |
| 2 | **adopción de PesquerApp** | los dos repositorios enteros, sólo lectura | iniciativa A0 · inventario · baseline · cobertura inicial | `INV` la capa, `SIS` consumidor | **`FASE 0` `gate:sistema-conforme`, ANTES de toda mutación canónica (§9.6; `O17` vía `D107`)** · A3 baseline, A8 retirada, A10 = `O12`. **`A9` presupone una Operativa que ninguna fase de `A` produce: salvedad declarada en §9.6** | inventario con procedencia · dictamen de `VER` | dosier de la iniciativa + checkpoint del paquete |
| 3 | **migración desde ADS anterior** | control repo antiguo y fuentes | estado **traducido**, con esquema nuevo | `SIS` · `ARQ` en `M6`–`M7` · `CON` con custodia de cada source change · `PLT` materializa (`C7:82`) | **`FASE 0` `gate:sistema-conforme`, ANTES de toda mutación canónica (§9.6; `O17` vía `D107`)** · M3 equivalencia · M5 certificación Integrada · **`M6` autorización EXPLÍCITA del Owner** · M7 las cinco salidas verdes. **`M3` invalida la Operativa heredada (§9.3) y ninguna fase `M` la reproduce: salvedad declarada en §9.6** | equivalencia antes/después de items y checkpoints | el evento `preparada` de la tx; M3 es idempotente |
| 4 | **actualización de ADS** | distribución candidata e instalada | distribución instalada · proyecciones | `SIS` · `PLT` propietaria global de `U5b` · `CON` con custodia del puntero · `ENT` declara convergencia | **`FASE 0` `gate:sistema-conforme`, ANTES de toda mutación canónica (§9.6; `O17` vía `D107`)** · U3 plan aprobado, U6 certificación (**revalida el nivel vigente; `U` no invoca `O12`**) | vista comprensible del cambio | rollback a la versión anterior con su estado |
| 5 | **feature amplia por iniciativa** | componentes afectados y sus fuentes | iniciativa + N items + paquetes | las capacidades con custodia | gate de cierre de la iniciativa | capas, source changes e integration set | dosier derivado + checkpoints |
| 6 | **auditoría recurrente → campaña** | los sujetos de las celdas vencidas | cobertura · items `AUD` · iniciativa campaña | **`DSP` abre los items `AUD` dentro de la política `O7` vigente** (§5.3) · la capacidad RESPONSABLE del aspecto —la `lider` si hay varias— abre la campaña · `ENC` clasifica los findings · runtime | gate de cada `AUD` + cierre de campaña | dictámenes · findings con causa raíz | la celda y su estado; nada se pierde |
| 7 | **reanudación tras chat agotado** | estado canónico completo | ninguno hasta despachar | runtime | — | el reporte breve de `b.14` paso 5 | es el escenario: `Continúa` |
| 8 | **caída durante escritura** | `estado/eventos/` y los marcadores de `estado/tx/` y `estado/deriva/` | **se COMPLETA, o se marca `conflicto` — que NO es un desenlace: tiene DOS salidas, completar si la divergencia cesa o REVERTIR lo especulativo local con `abandonada` verificada byte a byte** (§2.6.9) | runtime | — | los eventos de la transacción | §2.6, sin inventar estado |
| 9 | **dos fuentes y cierre** | `frontend` y `backend` | paquetes con source changes · integration set | capacidades con custodia · `ENT` | `gate:convergencia-de-fuentes` | el integration set, con SHA por fuente | checkpoint con `sources:` |
| 10 | **de Claude Code a Codex** | definición canónica del adaptador | proyecciones nuevas · cobertura de instalación | `PLT` | prueba de humo | salida de la prueba en sesión nueva | el estado no se toca: es neutral por diseño |
| 11 | **evidencia caducada** | entradas declaradas del validador | ninguno: se regenera evidencia | el runner | `T158` | la huella que no casa | regenerar, nunca editar |
| 12 | **aprendizaje promovido** | evidencia del item de origen | ledger · item `SIS` en `ads-kernel` | `APR` · `SIS` | `gate:aprendizaje-fundado` | dos ocurrencias o un incidente | el ledger conserva la procedencia |

**Lo que los escenarios de arriba demuestran juntos** —todos ellos; el cardinal no se escribe—: que ningún escenario necesita un almacén nuevo, un
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

## 15.2 · Los apartados de la directiva que esta fase traza

> **Corregido por `m3`.** El título decía «los veintiséis apartados» y la tabla traza **22 de
> los 26**: la recorren del 2 al 23. Sin fila quedan el 1, el 24, el 25 y el 26 — y el §24,
> «Reglas para interpretar esta directiva», **sí se usa**, citado en §10.2 y en §7.1. Trazar
> 22 es correcto; llamarlos veintiséis, no.

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
| 6 | adopción — **desglosado**, porque trazarlo en bloque ocultaba que `6.2` es exigible | §8.2 | NUEVA |
| 6.1 | fuentes que deben poder analizarse | §8.2 `LEE` · `A2` inventario | NUEVA |
| 6.2 | **las catorce preguntas del baseline** | §8.2, contrato de `A3` y de su gate | NUEVA |
| 6.3 | conversión del trabajo existente | §8.2 `A7` trabajo vivo | NUEVA |
| 6.4 | creación del PROFILE y especialización | §8.2 `A5` | NUEVA |
| 6.5 | el proyecto trae base sólida propia | §8.2 `A6` reconstrucción, y `A8` no retira material del producto | NUEVA |
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
| 17 | circuito formal de PROFILE | §8.1 INS-1 · §8.2 A5 | NUEVA |
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

## 15.4 · Las resoluciones del Owner y `P-01`–`P-08` — **dónde queda cada una**

> **Corregido por `P-26` del documento 22.** Esta cabecera publicaba el rango `O7`–`O14`
> mientras la tabla llegaba a `O15`, y **`O16` no tenía fila** — en la tabla cuyo objeto es
> declarar «dónde queda cada resolución del Owner». **La cabecera deja de llevar rango**: un
> rango escrito a mano en el título de una tabla que crece caduca en cuanto crece, y ya lo
> hizo. **La regla: esta tabla contiene UNA FILA POR RESOLUCIÓN del Owner, derivada de las
> cabeceras `### \`O` de la sección 2 de
> [`DECISIONES-Y-CONTRADICCIONES.md`](../rediseno/DECISIONES-Y-CONTRADICCIONES.md), y no
> declara ningún total en su título.** Una resolución sin fila aquí es el defecto.

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
| `O16` la sede del gobierno Git del control repo | §16 `PN-11` · §10 | NUEVA · **PRESIÓN F5** · con el ADDENDUM DE CRONOLOGÍA de `D106`(iii). **Fila añadida por `P-26`** |
| `O17` el nivel ESTRUCTURAL y su productor | **§9.6** · §9.2 · §9.4 · §8.1 · §8.2 · §8.3 · §8.4 · §18 | NUEVA · **hace satisfacible `O12`** · propagada por `D107`, **derivada y no elegida por F4** |
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
| `C5` handoff | **REUTILIZADO CON EXCEPCIÓN NOMBRADA**, con la misma disciplina que `C6` y `C7`, y no menos (`F-05`; es `D86`). `C5` L36 dice que **todo handoff entre capacidades se declara con su forma**, y `circuitos/00-CIRCUITOS.md` L238 dice que **los circuitos declarados son los que hoy existen, no todos los posibles**. Las dos frases no pueden ser ciertas a la vez. **MANDA `00-CIRCUITOS`**, por el mapa de fuente única de `kernel/operativo/00-INDICE.md`, que asigna «entregas entre capacidades» a `circuitos/` — y el NIVEL 0 del gate lo adjudicó así. Luego `C5` L36 se lee **acotada a la FORMA**: cuando un handoff se declara, se declara así; no obliga a que exista uno por cada par. La consecuencia material —`SIS` y `PLT` no aparecen en ninguna de las diecisiete instancias— **no es un defecto de composición de ruta** (§8.0) y su remedio es crear instancias en `circuitos/`, que es F6. **Y no es presión normativa**: `C5` es material DERIVADO, prescripción cerrada, ejecución F6 |
| `C6` producto, fuentes y workspace | **REUTILIZADO CON EXCEPCIÓN NOMBRADA**, y su defecto REGISTRADO —igual que se hizo con `C7`—. §5.1 se apoya en su componente sin deformarlo, pero §6.7 declara una **excepción a su frontera**: el puntero vive en la fuente por una necesidad de descubrimiento, y NO porque la frontera de `C6` lo permita — que respondería «su sitio es el control repo». `C6` es material DERIVADO, luego **no es presión normativa**: prescripción cerrada, ejecución F6. **Corregido por `M3`** |
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

> **LAS DOS REGLAS DE ESTA SEDE, escritas una vez.** **Añadidas por `P-03` del documento 22**,
> que encontró §0 declarando derivar de aquí un recuento que aquí ya no se sostenía: **once
> decisiones vigentes no tenían bloque**, y la sede de la que la cifra decía derivarse estaba
> incompleta en dos tandas enteras.
>
> 1. **EL TEXTO AUTORITATIVO DE TODA DECISIÓN ES EL REGISTRO**, no esta sección. Aquí vive
>    **una tanda por bloque**, con el gate que la devolvió y el tramo que abarca; el contenido
>    de cada `D` **se remite** y no se copia, porque una copia envejece sola y ya lo hizo.
> 2. **EL RECUENTO DE CORRECCIONES SE DERIVA DE LOS BLOQUES `###` DE ESTA SECCIÓN**, contados
>    tal como están, y **§0 REMITE aquí en vez de enumerarlos**. Toda tanda nueva **abre su
>    bloque en el mismo acto en que escribe sus decisiones**: no abrirlo es lo que rompió la
>    derivación dos veces.

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
| `D30` | **`estado/` nace en INS-0**, con su soporte durable mínimo | §8.1 | una iniciativa que nace en INS-0 con soporte desde INS-3 vive en el chat entre medias, y el apartado 19 de la directiva lo prohíbe |
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

### `D64`–`D68` · las decisiones de la TERCERA REVISIÓN INDEPENDIENTE

Veredicto de **INSUFICIENCIA** emitido por un revisor con contexto limpio que **no escribió
F4 ni aplicó ninguna de sus correcciones**: dos BLOQUEANTES, ocho GRAVES, cinco MEDIOS y
siete MENORES, más quince que intentó y no pudo reproducir. Su juicio se conserva íntegro e
inmutable en `15-TERCERA-REVISION-INDEPENDIENTE-F4C.md`. `D16`–`D63` conservan su texto.
**Y `D67` conserva el suyo**: la tanda del gate final lo reescribió, y `D87`–`D93` lo
restauran al de `7e99388`, llevando su corrección a `D89` (`I-16`).

| | decisión | qué revisa | por qué |
|---|---|---|---|
| `D64` | la **ruta de conflicto se COLAPSA**: cinco fases, seis transiciones, **DOS terminales**, y todo terminal retira el marcador. `conflicto` es observación bloqueante con dos salidas, y `abandonada` emite un `deriva` que conserva el bloqueo acotado | `D35` · `D46` · `D52` · `D60` · `D62` | **BLOQUEANTE**: `conflicto(observacion: 4, agotado: true)` no tenía transición admisible, el marcador no se retiraba y el control repo no volvía a commitear **para todo el producto** |
| `D65` | el **gobierno Git del control repo** se escribe: tabla de propiedad, `main` canónica sin `G29`, publicación optimista, `--force` prohibido salvo procedimiento del Owner, y `adaptador.publicacion_control_repo` como sede real de la política | `D41` | **BLOQUEANTE**: el texto prometía no rellenar el hueco por inferencia y lo rellenaba tres reglas después invocando `G29`, que `E2.4` acota a las fuentes. Ningún commit de `estado/` podía publicarse |
| `D66` | `a.9` se cita como `a.9` lo escribe —**concepto no es campo**—, y `fallo` recibe **semántica CERRADA** con `tx_afectada` como REFERENCIA | `D23` · `D54` | **GRAVE**: F4 sustituía «propietario del campo» por `actor_atribuido` y lo presentaba como los cinco de `a.9`; y `X15` y `X28` no eran satisfacibles contra el contrato de `fallo` |
| `D67` | los cuatro macrocircuitos se **MAPEAN a los procesos de `b.16`**, con propietario global tomado y no elegido; §8.3 gana `LEE`, `ESCRIBE`, `AUTORIDAD`, `EJECUTOR` y el gobierno de su retirada; §8.4 gana `ESTADO` | `D30` · `D32` · `D33` · `D45` | **GRAVE**: tres de los cuatro no nombraban proceso, y del proceso se derivan ruta, obligaciones, propietario y gates — F6 habría tenido que elegir |
| `D68` | la **taxonomía documental se alinea literalmente con las doce áreas del `§5.18`**: se restituye «mapa documental» y «arquitectura» vuelve a ser UNA. El área 1 se declara DERIVADA, y esa precisión es `PN-12` | `D26` · `D43` | **GRAVE**: las doce de F4 no eran las doce de `O8` — conservaban el número y no el conjunto, luego F6 habría construido doce contratos para las áreas equivocadas |

> **`D67` y `D68` fueron REVISADAS por la tanda del gate final.** `D67` en la columna de
> participantes y en el proceso de `A2`–`A7` (`D74`, `D75`); `D68` en los identificadores de
> las doce áreas (`D77`). Sus textos se conservan.

### `D69`–`D70` · las decisiones de la corrección previa al gate

Comprobación adversarial de sólo lectura sobre la tanda anterior. Sus seis defectos eran
**todos propios de esa tanda**, ninguno estaba en el juicio de la tercera revisión.
`D16`–`D68` conservan su texto.

| | decisión | qué revisa | por qué |
|---|---|---|---|
| `D69` | estado **ESTABLE** frente a **ESPECULATIVO**, y `abandonada` como **reversión local verificada** contra la revisión base | `D64` · `D16` · `D23` | `abandonada` retiraba el marcador dejando el conjunto parcial **publicable**, y un conjunto parcial no es consistente porque cada `rename` sea atómico |
| `D70` | recuperación en **TRES niveles** —exacta local, completa remota si cerró, **reinicio** si sigue abierta—, y la comparación de alternativas corregida: **`R1` no descarta el worktree** | `D65` · `D64` | «otra máquina reanuda clonando el control repo» es imposible con la regla de commit vigente, y el descarte del worktree invocaba `R1` sin fundamento |

### `D71`–`D86` · las decisiones de la TANDA INTEGRADA del GATE FINAL

El **GATE FINAL INDEPENDIENTE** —tres agentes con contexto limpio, 33 hallazgos verificados
uno a uno contra su fichero y su línea— y su **COMPLEMENTO DE COBERTURA** —otros tres agentes,
las diecinueve fuentes obligatorias leídas íntegras— dejaron **44 hallazgos abiertos, 43
distintos**. Los dos juicios se conservan íntegros e inmutables en los documentos 16 y 17.

> **`D16`–`D70` conservan su texto — y esta declaración es cierta desde `D87`, no lo era
> antes.** El gate de cierre encontró que esta misma tanda **reescribió `D67`** en el commit
> que declaraba lo contrario, en tres sedes a la vez (`I-16`). `D87`–`D93` **restauran `D67`
> al texto exacto de `7e99388`** y llevan su corrección a `D89`, que es una decisión revisora.
> La disciplina que este bloque enuncia vuelve a ser verificable con un `diff`.

| | decisión | qué revisa | por qué |
|---|---|---|---|
| `D71` | **`abierta(tx)`** es un predicado único, nombrado y con sede: §2.6.1. Las siete sedes remiten | `D46` · `D64` | **BLOQUEANTE** `A2`: tres sedes seguían diciendo «único terminal», luego una `abandonada` satisfacía «sin `derivada`» y el marcador no se retiraba nunca |
| `D72` | **`deriva.causa`** es enum cerrado de TRES valores con UNA sede, §3.6, y `tx_afectada` condicional a la causa | `D53` · `D64` | **BLOQUEANTE** `A1`: §3.6 declaraba dos valores, luego un esquema derivado de ella habría rechazado el `deriva` que `abandonada` obliga a emitir |
| `D73` | **§7.4 paso 2 recoge LAS DOS RAMAS** de `a.9` con el predicado de `D71`, y el resumen de §16 se alinea con el cuerpo de `PN-7` | `D69` | **GRAVE** `A3`: «§2.6 elimina el ramal de reversión por completo» dejó de ser cierto con `D69` y sobrevivía en dos sedes vigentes |
| `D74` | la **COMPOSICIÓN DE RUTA** gana sede canónica en §8.0: items enlazados, **cuatro vías** de entrada, ejecutor y autoridad separados de la ruta, gate de composición y error `composicion-incompleta`. **`C5` no es el vehículo** | `D67` | **BLOQUEANTE** `B-2`: trece participantes declarados no tenían por dónde entrar en el proceso que `D67` les asignó, sobre **cinco** capacidades |
| `D75` | **`A2`–`A7` es `proceso:AUD`** en items enlazados uno por conclusión, con propietario DERIVADO por item; §18 reescrita con la vía de cada capacidad; `SEG` y `CON` obligatorias en `U5b`; `U6` revalida el nivel vigente | `D67` | **BLOQUEANTE** `B-1`, y con él `G-1`, `G-2`, `M-3` y `m-4`: §8.2 y §18 asignaban procesos incompatibles a las mismas fases |
| `D76` | **`INS-5` produce el baseline y la clasificación de desconocidos críticos**, y el Owner lo aprueba — simetría exacta con `A3` | `D67` en los gates de `N` | **GRAVE** `G-3`: `INS-7 = O12` invocaba tres condiciones y ninguna fase producía dos de ellas: el gate era invocable y no satisfacible |
| `D77` | las **doce áreas documentales reciben identificador** `aspecto:documental/<area>`, derivado del patrón `ads:memoria` que ya existe. Las TRECE condicionales NO lo reciben: dos ya tienen sede canónica, y darles contrato editable crearía la segunda sede que `I5` prohíbe | `D68` | **GRAVE** `G-4`: §5.7 afirmaba que cada área resuelve a un contrato de aspecto, ninguna tenía identificador, y el único ejemplo usaba la mitad partida que `D68` retiró |
| `D78` | un **`deriva` sin reparar lleva su propio marcador legible**, `estado/deriva/<ID>.abierta`, con las rutas y los items que bloquea | `D64` | **MEDIO** `A8`: el paso `2bis` obligaba a todo lector a mirarlos, y encontrarlos exigía recorrer el diario entero — el coste que `R1` rechaza |
| `D79` | el desenlace **`4b` lo cierra un ACTO DE AUTORIDAD del Owner**: cuarentena, o declaración de irrecuperable con cierre por `abandonada` | `D69` · `X58` | **MEDIO** `A9`: `4b` retenía el marcador para siempre sin autoridad que pudiera cerrarlo, mientras `X58` afirmaba lo contrario |
| `D80` | un **finding del sistema tiene clase, forma y rama propias**, y su sujeto es la celda de cobertura, no el Owner | `D67` | **MEDIO** `M-6`: la cláusula de cierre de `03-FORMAS` mandaba al vivero todo finding de un `AUD` |
| `D81` | el **contenido del BASELINE de `A3` es el §6.2 de la directiva**, sus catorce preguntas con evidencia y grado; §15.2 desglosa el apartado 6 | `D67` · `m3` | **MEDIO** `M-9`: `A3` era «baseline con evidencia» sin decir de qué, y F6 habría inventado el contenido de un gate del Owner |
| `D82` | cada macrocircuito declara **cuántos items compone y cómo le afecta el FRENO 3** de `a.7`. Ninguno necesita excepción | `D67` | **MEDIO** `M-7`: el tercer item `SIS` de `N` se habría detenido sin que nadie hubiera previsto por qué |
| `D83` | los **dos espacios de nombres colisionados** se deshacen con UNA prueba: `RC-1`–`RC-9` para las ventanas retiradas, `INS-0`…`INS-7` para las fases de instalación | `D64` · `D67` | **MEDIO** `M-8` ≡ `A11` y `F-03`: `R<n>` estaba dos veces y `N<n>` **tres**, y §19 contaba nueve ventanas que `D64` retiró |
| `D84` | lo que protege la rama canónica es **el CAS de Git**, no «un único escritor», que es una regla LOCAL por worktree | `D65` | **MENOR** `A12`: se mezclaba una garantía distribuida con una regla local para justificar no aplicar `G29` |
| `D85` | los tres recuentos del eje `fase`, **recalculados tras `D64`**: cinco fases, seis estados, siete filas | `D59` | **MEDIO** `A6`: el documento decía «seis fases» en cuatro sedes y «cinco» en otras tres |
| `D86` | **`C5` con excepción nombrada** en §15.7, y `00-CIRCUITOS` manda sobre `C5` L36 por el mapa de fuente única | — | **MENOR** `F-05`: §15.7 aplicaba a `C6` y `C7` una disciplina que a `C5` no, con una tensión del mismo tipo |

**Y `O16`**, resolución posterior del Owner que da sede a `PN-11`: autoridad normativa en la
sección `(g)`, contrato derivado `C8` en F6, y `C7` limitado a las sources. **No autoriza
iniciar F5.** **Su procedencia quedó registrada por `L-02`** en el registro de decisiones:
fecha **2026-08-29**, la formulación que se le presentó —redactada por el sistema— y su
respuesta literal, «ok, confirmamos». El párrafo presentado **no es cita del Owner**; lo
literal suyo es la confirmación, y así consta.

**Y `O15`**, resolución posterior del Owner que revisa `O14` sin reescribirlo: la adopción de
PesquerApp es la **primera adopción real, permanente y completa** de ADS. Vive en el registro
de decisiones, y su lectura arquitectónica en §8.2, §18 y §19. **`D58`–`D63` no la tocan**:
sólo corrigen recuentos, cardinalidades, fronteras, contadores y la semántica de sellado.



### `D87`–`D95` · las decisiones de la CORRECCIÓN DEL GATE DE CIERRE

El **GATE DE CIERRE INDEPENDIENTE** —dos revisores con contexto limpio en paralelo y un
adjudicador sobre los dos dictámenes ya cerrados— devolvió **INSUFICIENTE PARA F5** por dos
razones independientes: la **cobertura** —catorce fuentes obligatorias sin lectura
sustantiva, el documento 15 entre ellas— y el **fondo** —diez de las 43 filas FALLIDAS, con
28 hallazgos consolidados de los que SEIS los introdujo o los perpetuó la propia
corrección—. Su juicio se conserva íntegro e inmutable en
`18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md`. `D1`–`D86` conservan su texto, **y `D67` se
RESTAURA al que tenía en `7e99388`**: la tanda anterior la reescribió en el mismo commit en
que declaraba que `D16`–`D70` no se reescriben (`I-16`), y la corrección que llevaba vive
ahora en `D89`, que es una decisión revisora.

| | decisión | qué revisa | por qué |
|---|---|---|---|
| `D87` | `estado/cuarentena/<TX>/` **RETIRADA**. La cuarentena temporal vive en **`.ads/run/quarantine/<TX>/`**: operacional, local, ignorada por Git y no canónica. Se crea antes de restaurar, se verifica por hash, y se elimina sólo tras el terminal, su verificación y el commit del incidente. `SEG` bloquea la publicación; el Owner puede aceptar expresamente la pérdida de la preimagen; el incidente conserva hash, clasificación, autoridad, motivo y alcance; el contenido prohibido no se publica nunca | `D79`, en el plano de la cuarentena. **`D79` no se reescribe** | **GRAVE** `I-01`: la ruta no tenía plano, ni fila, ni ciclo, ni prueba, y por §2.4 quedaba versionada — el acto (i) publicaba lo que existe para preservar cuando `SEG` prohíbe publicarlo |
| `D88` | el marcador de `deriva` gana **las cinco piezas**: segunda excepción de ruta en §2.4, fila en §2.3, `.gitignore`, fila de reconstrucción en §2.9 y filas adversariales. Lo crea el paso E de §2.6.9 y lo retira la transacción cerrada que lo resuelve. **La NORMA de §2.6.8 consulta los DOS marcadores**, no el diario | `D78` y `D64` | **GRAVE** `I-02`: la excepción invocada no lo cubría, luego viajaba a Git; y la regla que el lector ejecuta seguía mandando recorrer `estado/eventos/` |
| `D89` | la **capa B** pierde las dos reglas que `D64` retiró; §2.6.4 **remite** en vez de redeclarar; el censo de sedes se deriva y son **NUEVE**; y se recoge aquí la corrección que la reescritura de `D67` llevaba —`A2`–`A7` es `proceso:AUD`, propagar a las fuentes es `proceso:DEP`— | `D71`, `D64` y `D67` en su resumen | **GRAVE** `I-03` y **MEDIO** `I-09`: la capa que EVALÚA el predicado conservaba la afirmación exacta que causó `A2` |
| `D90` | **quién ejecuta cada operación Git lo fija `C7`**, y §8 lo cita: `PLT` materializa y retira ramas; la capacidad con custodia hace rama, commit, push y PR; `SEG` bloquea el push; `ENT` hace merge y declara convergencia; CI verifica cada fuente; el Owner conserva su autoridad. `PN-13` conserva sólo el residuo de `INS-5` y `A9` | `D74`, en el dispositivo `EJECUTOR` | **GRAVE** `I-04`: de las siete operaciones atribuidas a `PLT`, `C7` le da dos — y §1.3, §7.2 y §7.6 ya decían lo contrario |
| `D91` | abrir una `iniciativa` de campaña **no es implícito**: extensión de ficha para F6, con el conjunto **derivado de los `contrato-de-aspecto`** | `D80` y el remedio de `M-5` | **MEDIO** `I-14`: `C1` L118 es taxativa y ninguna de las quince fichas menciona `iniciativa` |
| `D92` | `<CAP>:revision` tras `VER` se registra como **contrato completo para F6**, en todos los procesos donde el condicional existe. F4 no toca `01-PROCESOS.md` | nada anterior | **GRAVE** `I-08`: (b) lo exige dos veces y hay **cero instancias** en el kernel, justo en los tres tramos que escriben en las fuentes |
| `D93` | **`F-01` se reclasifica** a presión lista para F5, y nace **`PN-14`**: `DIS/Reconstruccion` está en `b.16` L895 y `a.6` L495, material APROBADO | `D67` en la sede del remedio | `F-01` FALLIDA: el remedio, como estaba escrito, cambiaba el derivado dejando la fuente |
| `D94` | las condicionales de `§5.18` son **TRECE**, contadas una a una. `D68` y `D77` dicen CATORCE y **no se reescriben**: la corrección vive aquí | `D68` y `D77` en su recuento | **MEDIO** `I-15`: `M-1` era exactamente «catorce frente a trece», y la cuarta sede —escrita de cero en la misma tanda— reintrodujo la cifra en el registro de trazabilidad |
| `D95` | la regla 1 de §2.6.10 usa **«los cinco CAMPOS de procedencia»** de §3.6, como las otras cinco sedes. Es `D66` propagado | `D66` en su propagación | **MEDIO** `A7`, FALLIDA: era la ÚNICA sede que el gate nombró y la única que no se tocó, byte a byte idéntica al texto base, y **es** condición de validación |

> **El espacio de nombres `INS-0`…`INS-7`, y su excepción histórica declarada (`I-12`).** La
> proyección **NORMATIVA VIGENTE** de las fases de instalación es **`INS-0`…`INS-7`**, y su
> sede es §8.1 y la tabla de §18. `D83` la fijó, y la prueba que declara —«ningún
> identificador `<PREFIJO><n>` se usa con dos significados distintos»— se comprueba **sobre
> el corpus vigente**, no sobre el registro de decisiones.
>
> **`D32`, `D67`, `D76` y `D82` conservan `N<n>` en su texto, y es deliberado.** El registro
> es historia: dice qué se decidió y con qué palabras se decidió, y `D16`–`D86` no se
> reescriben — que es exactamente la disciplina que `I-16` demostró rota y que `D87`–`D93`
> restauran. Reescribirlos para uniformar la nomenclatura destruiría la trazabilidad que este
> fichero existe para dar, y sería el mismo gesto que produjo `I-16`.
>
> **La regla, en una frase, y es la misma que `X47` aplica al enum de `fase`:** la proyección
> normativa vigente es UNA —`INS-0`…`INS-7`—, y las citas históricas son MUCHAS y están
> marcadas como tales. Lo que la prueba de `D83` comprueba es la primera. `C6` `N1`–`N14` y
> la escala de novedad `N0`–`N4` siguen intactos y siguen siendo los suyos.

### `D96`–`D102` · las decisiones de la CORRECCIÓN DEL GATE DEFINITIVO INDEPENDIENTE

El **GATE DEFINITIVO INDEPENDIENTE** —dos revisores con contexto limpio, `J` y `K`, en
paralelo y sin verse, y un adjudicador `L` sobre los dos dictámenes ya cerrados— devolvió
**INSUFICIENTE PARA F5** por **seis** razones independientes: cobertura incompleta, un
BLOQUEANTE arquitectónico, seis GRAVES abiertos, un contrato F6 que aún exigía decidir
arquitectura, una contradicción con `G20`–`G23` sin presión F5, y un checkpoint no vigente.
Su juicio se conserva íntegro e inmutable en
[`19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md`](19-GATE-DEFINITIVO-INDEPENDIENTE-F4C.md).
**El texto de `D96`–`D102` vive en el registro y NO se copia aquí** (regla 1 de arriba): allí
está cada decisión con lo que revisa y su alternativa descartada. `D1`–`D95` conservan su
texto.

### `D103` · la decisión de la CORRECCIÓN TÉCNICA sobre la derivación de `<CAP>:revision`

Corrección técnica acotada sobre el algoritmo que `D98` había reformulado: retiró del
ALGORITMO el barrido léxico que su propio criterio ya había retirado, y corrigió una
cardinalidad insatisfacible. **`D98` no se reescribe.** Su texto vive en el registro.

### `D104`–`D106` · las decisiones de la CORRECCIÓN DEL GATE DE COBERTURA Y CIERRE

El **GATE INDEPENDIENTE DE COBERTURA Y CIERRE** y el **GATE INDEPENDIENTE DE CIERRE CON
MANIFIESTOS VERIFICABLES** —documentos 20 y 21— devolvieron **INSUFICIENTE PARA F5**.
`D104` sustituye entero el algoritmo de derivación de `<CAP>:revision` por cuatro defectos
concurrentes; `D105` fija el orden EXACTO y DURABLE del cierre por abandono —los seis pasos
del paso `E` de §2.6.9, la ventana `W17` y el `fsync` del `deriva`—; `D106` recoge tres
correcciones documentales que cambian lo que alguien tiene que hacer. **`D103` no se
reescribe.** Sus textos viven en el registro.

### `D107` · la propagación de `O17` — DERIVADA de una resolución del Owner, NO elegida por F4

El **GATE INDEPENDIENTE DE CERTIFICACIÓN** —documento 22— devolvió **INSUFICIENTE PARA F5**
con 69 hallazgos, de los que **uno solo** era decisión exclusiva del Owner: **el nivel
Estructural y su productor**. El Owner resolvió, y su resolución es **`O17`**, íntegra en la
sección 2 del registro. `D107` es **su propagación, y se declara DERIVADA**: los cuatro
macrocircuitos ganan una **FASE 0 de CERTIFICACIÓN ESTRUCTURAL** como precondición propia, y
`gate:sistema-conforme` gana productor, sujeto, evidencia, vigencia y condición de
invalidación. **La sede de todo ello es §9.6**, y §8.1–§8.4, §9.2, §9.4 y §18 la invocan.
**Lo único que F4 aporta es el reparto de la alternativa (b) por las sedes vigentes**: las
alternativas (a) y (c) **las descartó el Owner**, no F4. `D1`–`D106` y `O1`–`O16` conservan
íntegro su texto, y **nada se renumera**.

---

# 16 · Presiones normativas para F5

**Aquí no se redacta ninguna enmienda.** Se enumera exactamente qué presiona qué, y qué queda
bloqueado hasta que el Owner apruebe.

**Las cinco de la entrega anterior se han revisado una a una**, no arrastrado. Cada bloque
declara su `ESTADO TRAS LA DEVOLUCIÓN`, y los identificadores **no se renumeran**: `PN-4`
sigue llamándose `PN-4` aunque esté retirada, porque renumerar rompería la trazabilidad de lo
que ya se llevó al Owner. De aquellas cinco resultan **TRES vigentes** —`PN-1`, `PN-2`,
`PN-3`—, una retirada (`PN-4`) y una fusionada (`PN-5`): 3 + 1 + 1 = 5, y la cuenta cierra.
**Corregido por `m2`**: decía «cuatro vigentes, una retirada y una fusionada» sobre cinco, que
suma seis. Las demás vigentes —**`PN-6` a `PN-18`**— son posteriores, y el total está abajo.
**Corregido por `I-11`**: decía «`PN-6` a `PN-12`», que con las tres primeras suma DIEZ
mientras el total decía ONCE, y omitía precisamente `PN-13`, la que va al Owner.
**Corregido otra vez por `Q-07`**: decía «`PN-6` a `PN-14`» cuando ya existía `PN-15`, y
volvía a omitir justo la que va al Owner. Es la TERCERA vez que esta frase caduca, y por eso
`G-26` deja de mirar sólo numerales sueltos y **deriva también los RANGOS**: un `PN-a` a
`PN-b` vivo tiene que terminar en la última cabecera vigente y contener tantas como el censo.
**Y CUARTA vez, con `PN-17` y `PN-18`** (`P-07` y `P-08` del documento 22): decía «`PN-6` a
`PN-16`». **La garantía, escrita una vez y para siempre, y es la que hay que leer antes que
cualquier cifra de este documento:** *ningún rango ni ningún total de presiones de este
fichero se escribe a mano. **TODOS se DERIVAN del barrido de las cabeceras `## \`PN-`**, y el
extremo superior de todo rango vivo es **la ÚLTIMA cabecera vigente, sea cual sea**.* Una
cifra que aquí aparezca y no coincida con ese barrido **es el defecto, no el barrido**.

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
QUÉ HA CAMBIADO     **REFORMULADO por `D69`.** §2.6 tenía sólo ROLL-FORWARD y ahí la
                    disyunción quedaba coja. Ahora tiene **LAS DOS RAMAS**, y ninguna deja
                    una mezcla parcial:
                      COMPLETAR   `confirmada` → `derivada`, con todos los ficheros en su
                                  `hash_posterior_esperado`
                      REVERTIR    `abandonada`, que **restaura las escrituras ESPECULATIVAS
                                  LOCALES a la revisión base y lo verifica byte a byte**
                                  antes de poder emitirse (§2.6.9)
                    Y en los dos casos el incidente se registra y se publica DESPUÉS de
                    recuperar la consistencia. **NUNCA se cierra dejando una mezcla parcial**,
                    y **no hay un tercer desenlace normativo**
QUÉ QUEDA POR       que `b.14` y `a.9` hablan de revertir sin distinguir estado PUBLICADO de
DECIDIR             estado ESPECULATIVO. §2.6.0 hace esa distinción, y sólo revierte lo
                    segundo: lo publicado nunca se restaura automáticamente
MATERIA MÍNIMA      una frase en b.14 que confirme la lectura: «completar, o revertir las
                    escrituras especulativas a su revisión base, registrar el incidente y
                    escalar» — sin autorizar la reversión de estado ya publicado
SE PUEDE CONSTRUIR  todo §2.6. La lectura está declarada y no espera a nadie
BLOQUEA             nada que no bloquee ya PN-1. Es coherencia, no capacidad
ORIGEN              hallazgo `N-9` de la segunda devolución independiente, REFORMULADA por la
                    comprobación adversarial previa al gate
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

## `PN-11` · NUEVA · el gobierno Git del CONTROL REPO no tiene sede normativa

```text
QUÉ PRESIONA        `C7`, contrato derivado que gobierna las operaciones Git **de las
                    fuentes**, y `E2.4`, que conserva `G29` **por source** con todas las
                    letras
QUÉ FALTA           **ninguna norma gobierna el Git del REPOSITORIO DE CONTROL**: ni su rama
                    canónica, ni su protección, ni la autoridad de su push, ni su
                    concurrencia entre máquinas, ni el procedimiento extraordinario de
                    `--force`. §2.6.10 lo escribe para que sea implementable, pero lo escribe
                    la ARQUITECTURA, no una norma
POR QUÉ NO ES SÓLO  porque `E2.4` **cierra expresamente** la vía de derivarlo de `G29`, y
DEFECTO DE F6       porque la tabla de propiedad de `C7` no tiene ninguna fila que alcance al
                    control repo. F6 no puede rellenarlo sin tomar una decisión normativa
                    NUEVA, y eso es materia del Owner
SEDE, YA RESUELTA   **`O16`**, resolución posterior del Owner: la AUTORIDAD NORMATIVA vive en
POR EL OWNER        la futura sección `(g)` —que `PN-1` ya exige crear, luego no se añade una
                    norma nueva—, y F6 deriva de ella un contrato independiente **`C8`** que
                    gobierna ÚNICAMENTE el control repo. **`C7` permanece limitado a las
                    sources.** `C8` no copia la tabla de `C7`: el sujeto es distinto y hay que
                    aplicarle la prueba.
                    **Procedencia de `O16`, registrada por `L-02`:** 2026-08-29, formulación
                    presentada por el sistema y respuesta literal del Owner «ok,
                    confirmamos». Está en el registro de decisiones y en `owner_captado`.
                    Antes de eso, `O16` era **la única resolución del Owner sin fecha, sin
                    cita y sin entrada en `owner_captado`** — y es la que cierra la sede de
                    esta presión, nacida del BLOQUEANTE `B2`.
                    **El TOTAL de resoluciones del Owner no se escribe aquí**: se deriva de
                    las cabeceras `### \`O` de la sección 2 de
                    `docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`, y §15.4 lo traza.
                    **Corregido por la propagación de `O17`** (`D107`): esta línea decía
                    «dieciséis», y la cifra caducó el día en que el Owner resolvió una más
MATERIA MÍNIMA      un apartado en `(g)` con la tabla de propiedad del control repo. **F5 la
                    redacta; F6 materializa y valida `C8`.** Ninguna se redacta aquí
BLOQUEA             la publicación gobernada del estado, y con ella las garantías 5 y 6 de
                    §2.6.6, la reconstrucción sin árbol de §2.9, la condición previa de toda
                    `retirada-de-cuerpo` y la permanencia que `O15` exige
LO QUE NO BLOQUEA   la recuperación local, el commit local y todo lo que no salga de la
                    máquina. El comportamiento seguro entretanto está declarado en §2.6.10
ORIGEN              hallazgo `B2` de la TERCERA REVISIÓN INDEPENDIENTE
CONDICIÓN DE        si el Owner prefiere que `C7` no crezca, la reversión es declarar el
REVERSIÓN           control repo fuera del gobierno Git normativo y dejar §2.6.10 como
                    prescripción de arquitectura — a costa de que su cumplimiento no sea
                    verificable por ningún contrato
```

## `PN-12` · NUEVA · el «mapa documental» de `O8` como área DERIVADA

```text
QUÉ PRESIONA        `O8`, resolución del Owner del 2026-08-27: «las doce áreas semánticas del
                    §5.18, obligatorias como MATERIA y no como ficheros»
QUÉ HACE F4         restituye las doce **literalmente** como `§5.18` las enumera —`G8` había
                    encontrado que F4 eliminaba «mapa documental» y partía «arquitectura» en
                    dos— y, al restituir la primera, la declara **DERIVADA**: se regenera
                    desde los bloques `ads:memoria` y las celdas de cobertura documental
POR QUÉ SE REGISTRA porque `O8` dice «obligatorias como MATERIA», y declarar que UNA de esas
IGUAL               materias no se escribe sino que se DERIVA es una precisión sobre su
                    resolución. Puede ser obviamente correcta —un mapa escrito a mano
                    envejece, que es el defecto que `§5.23` existe para detectar— y por eso
                    mismo se registra: es **la misma vara de `PN-6` y `PN-10`**, y un
                    tratamiento asimétrico de las resoluciones del Owner es el defecto
MATERIA MÍNIMA      una frase que confirme que el área 1 se satisface con un mapa DERIVADO, o
                    que exija uno escrito y mantenido
BLOQUEA             nada hoy. Con la lectura derivada, F6 puede construir los doce contratos
                    de aspecto sin esperar
ALCANCE             sólo el área 1. Las otras once no se tocan, y su alineación con `§5.18`
                    no es presión: es la corrección de una cita
CONDICIÓN DE        si el Owner exige un mapa escrito, el área 1 pasa a tener responsable y
REVERSIÓN           caducidad propios, y su fila en §1.3 deja de tener autoridad «nadie»
ORIGEN              hallazgo `G8` de la TERCERA REVISIÓN INDEPENDIENTE, que la nombró como
                    «la presión normativa omitida»
```

## `PN-13` · NUEVA · `proceso:SIS` y `proceso:INV` no admiten `DOM`, `SEG` ni `DIS`

```text
QUÉ PRESIONA        (b) b.16, filas SIS e INV. SIS: obligatorias SIS·CON·VER, condicionales
                    ENT y APR. INV: obligatoria INV, condicionales CON:experimental, PRD,
                    ARQ y APR. **`DOM`, `SEG` y `DIS` no figuran en ninguna de las dos**, ni
                    como obligatorias ni como condicionales
TEXTO VIGENTE       «SIS evolución del sistema | SIS | SIS · CON · VER | ENT obligatorio si
                    modifica el runtime · APR C-APR» y «INV investigación | INV | INV |
                    CON:experimental… · PRD o ARQ según destino declarado · APR C-APR»
QUÉ HACE F4         §8.1 declara `INS-5` «discovery de producto, dominio y diseño» ANTES del
                    gate `INS-7` «listo para construir», y §8.0 exige que toda capacidad de la
                    ruta entre por una de sus cuatro vías. `DOM` y `DIS` no entran por
                    ninguna: el modelo de dominio y el sistema de diseño de un producto
                    NUEVO se establecen en `INS-5`, y sus items sólo pueden ser `SIS` o `INV`.
                    `AUD` sí las declara, pero `AUD` exige «un objeto YA EXISTENTE», que en
                    una instalación nueva no hay
POR QUÉ NO CABE EN  no es `PN-8` —aquélla es `VER` ausente de la ruta `AUD`, otra fila, otra
LAS DIEZ            capacidad y otro remedio—. No es `PN-2` ni `PN-3`, que preguntan QUIÉN
                    puede CREAR trabajo, no por dónde entra una capacidad en un trabajo que
                    ya existe. No es `PN-6`, `PN-10` ni `PN-12`, que interpretan
                    resoluciones del Owner. **Es la única que toca la derivación de rutas de
                    b.16 por el lado de las capacidades ausentes en SIS e INV**
POR QUÉ NO BASTA    porque §8.0 prohíbe expresamente ensanchar un proceso por conveniencia:
UN DERIVADO         `b.16` es (b), y añadir un condicional a una ruta aprobada es normativo.
                    La alternativa —inventar un handoff que traiga a `DOM` sin que esté en
                    la ruta— la cierra el NIVEL 0 del gate: `C5` materializa entregas entre
                    capacidades que YA participan, y no compone rutas
MATERIA MÍNIMA      añadir `DOM:condiciones C-DOM`, `SEG:condiciones C-SEG` y `DIS C-DIS`
                    como CONDICIONALES de `proceso:SIS`, y `DOM`, `SEG` y `DIS` como
                    condicionales de `proceso:INV`. **O bien** declarar que el discovery de
                    dominio y diseño de un producto nuevo no pertenece a `INS-5` y nombrar
                    dónde pertenece. Son dos salidas, y elegir es del Owner
ALCANCE             `INS-5` y `A9` de §8, **y nada más**. NO alcanza a `A2`–`A7`, que es
                    `proceso:AUD` y sí hace participar a `DOM`, `SEG` y `DIS` como
                    condicionales; ni a `A8`, `M6`–`M7` ni `U5b`, que son `proceso:DEU` y
                    `proceso:DEP` y **también hacen participar a las dos, aunque por VÍAS
                    DISTINTAS**: `DEU` declara `DOM:condiciones` y `SEG:condiciones` como
                    condicionales, mientras `DEP` declara `DOM:condiciones` como condicional
                    y **`SEG` como OBLIGATORIA** —el item `condiciones-de-seguridad`, con
                    `capacidad_productora: "SEG"`, que `G28` hace irretirable—. **Corregido
                    por `L-03`**: el texto anterior atribuía `SEG:condiciones` a `DEP`, que
                    es precisamente la conflación de vías que rompía `D92` (`K-02`, cerrada
                    por `D98`). La conclusión no cambia —el alcance sigue sin llegar a
                    `U5b`—; el motivo escrito sí. **Corregido por `I-26`**: la frase quedaba
                    cortada a media línea, en la única presión que esta tanda añadía y que va
                    al Owner. **Y la mitad `PLT` del bloqueante `B-2` ya NO está aquí**: se
                    cierra contra `C7:80-92` en §8.0 (`I-04`), y nunca fue materia del Owner
SE PUEDE CONSTRUIR  todo lo demás de §8, y las cuatro composiciones completas salvo esas dos
                    celdas. `INS-0`–`INS-4`, `INS-6`, `INS-7` y los tres macrocircuitos restantes no
                    esperan a nadie
BLOQUEA             que `INS-5` abra con `DOM` y `DIS` en su ruta, y que `A9` incorpore el
                    dictamen de `SEG` sin pasar por un item `AUD` enlazado
CONDICIÓN DE        si el Owner prefiere no tocar `b.16`, la reversión es declarar que `INS-5`
REVERSIÓN           produce ÚNICAMENTE conocimiento —items `INV` con destino `PRD` o `ARQ`—
                    y que dominio y diseño se depositan después, en los items de producto
                    donde `C-DOM` y `C-DIS` ya son condicionales. A costa de que el gate
                    `INS-7` «listo para construir» se supere sin modelo de dominio
ORIGEN              hallazgo `B-2` del GATE FINAL INDEPENDIENTE, residuo que NO se cierra
                    propagando ninguna decisión ya tomada. Es el ÚNICO de los cuarenta y
                    cuatro que lo exige
```

## `PN-14` · NUEVA · `DIS/Reconstruccion` está en material APROBADO, no sólo en el kernel

> **Registrada por el gate de cierre independiente (`F-01`, reclasificado; es `D93`).**
> `F-01` estaba clasificado como EXTERNO de F6: sustituir `DIS/Reconstruccion` por `DIS` en
> `01-PROCESOS.md` y en `00-CIRCUITOS.md`. **La sede estaba incompleta**: la misma cadena
> aparece en material **APROBADO** que §17 declara intocable por F4 **y por F6**. Ejecutado
> tal como estaba escrito, el kernel diría `DIS` y su fuente normativa seguiría diciendo
> `DIS/Reconstrucción`: se corregiría el derivado y se dejaría la fuente, que es exactamente
> el modo de fallo que §15.7 registra para `C7`. Y entonces la verificación mecánica «contra
> la fuente» que el checkpoint invoca como motivo del remedio **seguiría fallando**.

```text
QUÉ PRESIONA        (b) `b.16` L895 · `docs/rediseno/b-RECORRIDO-APROBADA.md`
                    (a) `a.6` L495 · `docs/rediseno/a-CAPACIDADES-APROBADA.md`
                    Los dos son material APROBADO, y §17 los declara «intactas. F4 no las
                    toca» — y F6 tampoco puede tocarlos

TEXTO VIGENTE       `b.16` L895: «`DIS/Reconstrucción `C-DIS``»
                    `a.6` L495: «`AUD  INV ∥ DOM ∥ SEG ∥ DIS/Reconstrucción`»

QUÉ ES EL DEFECTO   `DIS/Reconstruccion` **no es una capacidad ni un participante
                    asignable**: es uno de los SEIS MÉTODOS de `DIS`
                    (`capacidades/DIS/CAPACIDAD.md`), y **cuál se ejecuta lo calcula la
                    ESCALA DE NOVEDAD, no lo elige la ruta** —`diseno/03-ESCALA-DE-NOVEDAD.md`
                    L251–261 fija que todo paquete de `DIS` declara su `nivel_de_novedad` y
                    que `gate:excelencia-visual` lo comprueba—. Nombrar el método en la ruta
                    **PREDETERMINA** lo que la escala prohíbe predeterminar

POR QUÉ NO BASTA    porque el conjunto de participantes es IDÉNTICO bajo las dos lecturas
UN DERIVADO         —`DIS/Reconstruccion` denota `DIS` operando por uno de sus métodos, y la
                    condición es `C-DIS` en las dos—, luego la composición de `A2`–`A7` que
                    §8.0 y §18 declaran es correcta y **la arquitectura no queda inválida**.
                    Lo que no se puede hacer por derivado es corregir (a) y (b): son
                    normativos, y `F-01` tal como estaba escrito **no era ejecutable** para
                    su fin declarado

MATERIA MÍNIMA      sustituir, en los DOS puntos aprobados, `DIS/Reconstruccion` por la
                    capacidad **`DIS`** con su condición **`C-DIS`**, y declarar
                    expresamente que **el método concreto lo calcula la escala de novedad**,
                    no la ruta. **Aquí no se redacta ninguna enmienda**, como en las trece
                    anteriores

ALCANCE             `b.16` fila `AUD` y `a.6` composición ilustrativa. NO alcanza a §8.2 ni
                    a §18, que ya dicen `DIS` `C-DIS`; ni a la ficha de `DIS`, donde
                    `DIS/Reconstruccion` es correcto porque **allí sí es un método**

SE PUEDE CONSTRUIR  todo lo demás. La composición de `A2`–`A7` es correcta hoy bajo las dos
                    lecturas, y `INS-5` no depende de esto

BLOQUEA             que la composición de `A2`–`A7` sea **verificable mecánicamente contra la
                    fuente**. Mientras (a), (b) y el kernel no digan lo mismo, la
                    comprobación cruzada que `F-02` habilita no puede pasar

DESPUÉS DE F5       **F6** actualiza `kernel/operativo/recorrido/01-PROCESOS.md` L434 y
                    `kernel/operativo/circuitos/00-CIRCUITOS.md` L166, que es el trabajo que
                    `F-01` ya tenía registrado. El orden importa: primero la fuente, después
                    el derivado — al revés es el modo de fallo de `C7`

CONDICIÓN DE        si el Owner prefiere no tocar (a) ni (b), la reversión es declarar
REVERSIÓN           expresamente que `DIS/Reconstruccion` y `DIS` **designan al mismo
                    participante**, y que lo que F6 corrige es la forma del derivado. Es una
                    salida legítima y más barata; elegir es del Owner

ORIGEN              hallazgo `F-01` del GATE FINAL, reclasificado por el GATE DE CIERRE
                    INDEPENDIENTE: su remedio, tal como estaba escrito, no alcanzaba su fin
```

## `PN-15` · NUEVA · `KERNEL.md` `G20`–`G23` y el gate del Circuito 0, presionados por §8

> **Registrado por el GATE DEFINITIVO INDEPENDIENTE (`K-06`, GRAVE; es `D97`).** §8 sustituye
> la ruta de arranque cuyo gate de salida la constitución declara **no negociable por el
> sistema**, por un gate distinto **definido por el propio sistema** — y ni `a.11` lo deroga
> ni §16 lo registraba. `PN-3` demuestra que presionar UNA regla de `KERNEL.md` exige una
> `PN`; aquí son cuatro. **Esta presión NO deroga nada y NO redacta ninguna enmienda: fija
> que la decisión es de F5 y que hasta entonces `G20`–`G23` SIGUEN VIGENTES.**

```text
QUÉ PRESIONA        `kernel/KERNEL.md` 1.5.0 · `G20` (Macrocircuitos) · `G21` (Gates entre
                    circuitos) · `G22` (gate fijo del Circuito 0) · `G23` (Product Baseline)
                    Es material APROBADO. F4 no lo toca, y F6 tampoco puede tocarlo

TEXTO VIGENTE       `KERNEL.md`:690 (`G21`) — «El gate de salida del Circuito 0 lo fija este
                    documento y NO es negociable por el sistema (G22), porque un sistema no
                    puede definir sin conflicto de interés los criterios que aprueban su
                    propia existencia»
                    `KERNEL.md`:687 — «C0 →[gate fijo, ver G22]→ C1 →[gate]→ C2 →[gate]→
                    C3 →[baseline, ver G23]→ C4»
                    `KERNEL.md`:694–712 (`G22`) — timebox de 3 sesiones del Owner o 2
                    semanas · parada obligatoria con `Owner Decision` · DIEZ entregables
                    obligatorios nombrados uno a uno · cuatro prohibiciones
                    `START_HERE.md`:141–147 — ruta A: «Lanzar el Circuito 0… termina cuando
                    existen los 10 entregables de G22, dentro del timebox»

QUÉ ES EL DEFECTO   §17 declara «`START_HERE.md` rutas A y B → **sustituidas** por §8.1 y
                    §8.2», y §8.1 define `INS-0`…`INS-7` con `INS-3` = «C0: especializar y
                    verificar la organización YA MATERIALIZADA» y gates `INS-4` / `INS-7`.
                    **BARRIDO DERIVADO, y acotado a lo que puede DEROGAR** (`P-06`): en
                    el material APROBADO —(a), (b) y `E2`— las cuatro reglas aparecen
                    **(a) 1 · (b) 0 · E2 0**, y esa única aparición de (a) es una cita de
                    apoyo en la ficha de `INV`, **no una fila derogatoria de `a.11`**.
                    Lo que se prueba es esto y sólo esto: **el material aprobado no contiene
                    ninguna derogación válida de `G20`–`G23`**.
                    **Esta sede decía «cero apariciones en el documento 11», y era falsa**:
                    el documento 11 las nombra muchas veces, y la mayoría de esas
                    apariciones las introdujo ESTE MISMO bloque al registrar la presión. Son
                    apariciones DOCUMENTALES —explican la presión— y contarlas probaría sólo
                    que la presión está escrita. `G-13` deriva el censo del material
                    aprobado y lo contrasta contra estas tres cifras.
                    `a.11` —«la ÚNICA lista que deroga o ajusta reglas», según `PN-3`— **no
                    nombra ninguna de las cuatro** en ninguna de sus cinco filas, y `E2.4`
                    demuestra la regla de lectura: `G29` figuraba entre las que SOBREVIVEN
                    intactas y hubo que ENMENDAR (a) para reclasificarla. **Lo no nombrado
                    sobrevive.** Y §17 **no tenía fila para `kernel/KERNEL.md`**

POR QUÉ NO BASTA    porque el conflicto no es de forma: `G22` fija un gate CON CONTENIDO
UN DERIVADO         —timebox, diez entregables, cuatro prohibiciones— y §8.1 fija otro
                    distinto SIN ellos. No hay lectura bajo la cual los dos sean el mismo
                    gate. Y `G21` declara expresamente que quien lo fija es la constitución
                    y **no el sistema**, luego F4 no puede resolverlo por su cuenta sin
                    incurrir justo en el conflicto de interés que esa regla nombra

MATERIA MÍNIMA      que F5 decida, regla a regla y de forma EXPRESA, qué se CONSERVA, qué se
                    AJUSTA y qué se SUSTITUYE de `G20`, `G21`, `G22` y `G23` frente al
                    Circuito 0 de §8.1, y lo registre en `a.11` —que es material APROBADO y
                    por eso exige enmienda, como `PN-3` para `G03`—. **Aquí no se redacta
                    ninguna enmienda**, como en las catorce anteriores.
                    Cuatro preguntas concretas, y ninguna la puede contestar F4:
                      1 · ¿el gate de salida del Circuito 0 sigue siendo el de `G22`, o pasa
                          a ser `INS-4`/`INS-7`? Si pasa, ¿quién lo fija, dado que `G21`
                          dice que no puede fijarlo el sistema?
                      2 · ¿el timebox de 3 sesiones o 2 semanas sobrevive, se ajusta o se
                          retira?
                      3 · ¿los DIEZ entregables obligatorios de `G22` sobreviven, y cómo se
                          corresponden con las salidas de `INS-0`…`INS-7`?
                      4 · ¿`G20` y `G23` —macrocircuitos y Product Baseline— quedan
                          intactos, ajustados o sustituidos por §8?

ALCANCE             `G20`, `G21`, `G22` y `G23` de `KERNEL.md` 1.5.0, y la fila de `a.11`
                    que haya que añadir. NO alcanza al resto del kernel, ni a §8, que
                    describe lo que F4 diseñó y no pretende derogar nada

SE PUEDE CONSTRUIR  todo §8 **como diseño**. Lo que NO se puede es instalar por §8.1 dando
                    por derogado el gate de `G22`: **hasta que F5 decida, `G20`–`G23` SIGUEN
                    VIGENTES**, y una instalación real tiene que satisfacer las dos cosas o
                    esperar a la enmienda

BLOQUEA             la ejecución real del Circuito 0 por la ruta de §8.1 sin resolver antes
                    qué le pasa a `G22`. **No bloquea F6 en lo que no toca el arranque**

DESPUÉS DE F5       **F6** actualiza `START_HERE.md` y el resto de derivados. El orden
                    importa: primero la fuente —`a.11` y la enmienda—, después el derivado.
                    Al revés es el modo de fallo que §15.7 registra para `C7`

CONDICIÓN DE        si el Owner decide que `G20`–`G23` se conservan intactas, la reversión
REVERSIÓN           es que **§8.1 se subordine a `G22`**: el Circuito 0 mantiene su timebox,
                    sus diez entregables y sus cuatro prohibiciones, y `INS-0`…`INS-7` pasa
                    a ser la instrumentación de ese gate y no su sustituto. Es una salida
                    legítima y no exige rediseñar §8; elegir es del Owner

PROPIETARIO         el **Owner**, porque es material aprobado y porque `G21` reserva
                    expresamente esta decisión a la constitución y no al sistema.
                    Redacta **F5**; materializa **F6**

PRUEBA POSTERIOR    **CORREGIDA por `M-05`.** La formulación anterior era una DISYUNCIÓN
                    —una fila en `a.11` **o** una fila en §17— y afirmaba que pasar en verde
                    hoy sería imposible «porque no existe ninguna de las dos». **La fila de
                    §17 la escribió `D97`, en el mismo commit que esta presión**, y con ella
                    el segundo disyunto quedaba satisfecho para las cuatro reglas: la prueba
                    pasaba en verde el día que nacía. El propio cuerpo de esta presión lo
                    dice en pasado —«§17 **no tenía** fila para `kernel/KERNEL.md`»— y aun
                    así declaraba su prueba infalible.
                    **La disyunción se retira. La prueba exige UNA sola cosa:**
                      · para cada una de `G20`, `G21`, `G22` y `G23`, **una fila en `a.11`**
                        —o en la enmienda que F5 escriba sobre `a.11`— **que la nombre y
                        declare su disposición**: derogada, sustituida, ajustada, conservada
                        o pendiente con plazo.
                    **La fila de §17 NO la satisface, y no puede satisfacerla**: §17 es la
                    tabla de trazabilidad de F4, y lo que registra es que la presión existe.
                    **Registrar una presión no es resolverla.** `a.11` es material APROBADO y
                    sólo F5 puede escribir en él, luego **esta prueba sólo pasa cuando F5 haya
                    tomado y materializado la decisión normativa real**, que es lo que una
                    prueba posterior debe medir.
                    **Hoy FALLA, y tiene que fallar**: `grep 'G2[0-3]'` sobre (a) devuelve una
                    sola línea, y es la ficha de `INV`, no una fila derogatoria.
                    Propietario `SIS`, fase F6 —la comprobación—; la decisión, F5

ORIGEN              hallazgo `K-06` del GATE DEFINITIVO INDEPENDIENTE, agravado a GRAVE por
                    el adjudicador `L` y elevado por él a una de las seis razones del
                    veredicto INSUFICIENTE PARA F5
```

## `PN-16` · NUEVA · la grafía canónica de `<CAP>:revisión` vive en material APROBADO

> **Registrada por `P-07` del GATE INDEPENDIENTE DE CIERRE CON MANIFIESTOS.** El bloque `E5`
> justificaba no crear presión con «aquí **no hay norma presionada** … lo que hay es una cita
> mal puesta y una lista mal numerada». Eso es exacto para `E5-1` y `E5-2`. **No lo es para
> `E5-3`**, cuya propia fila dice «si es la sin tilde, **F5 enmienda (b)**» y se declara
> «hermano exacto de `F-01`/`PN-14`, que SÍ se registró como presión». El único de los cuatro
> que puede exigir enmendar material aprobado era el único que no llegaba al Owner.
> **Esta presión NO elige la grafía y NO redacta ninguna enmienda: registra que hay que
> elegir, y que la elección es del Owner.**

```text
QUÉ PRESIONA        `docs/rediseno/b-RECORRIDO-APROBADA.md` · `b.16` **L836**, la ÚNICA
                    aparición normativa de la variante. Es material APROBADO: F4 no lo toca
                    y F6 tampoco puede tocarlo

TEXTO VIGENTE       (b) L836 — «`<CAP>:**revisión**`  tras VER  revisan lo construido»,
                    **con tilde**

QUÉ ES EL DEFECTO   todo el aparato derivado de F4 escribe la variante **sin tilde**:
                    §19, `D92`, `D98`, `D103`, `D104`, la prueba prescrita, el mensaje de
                    error `composicion-incompleta` y el vocabulario de `F-02` en `E-3`.
                    **Dos grafías para el mismo identificador normativo, y ninguna sede dice
                    cuál manda.** Es la misma clase que `F-01`: una discrepancia entre fuente
                    APROBADA y derivado, que no se cierra corrigiendo sólo el derivado

POR QUÉ NO BASTA    porque si la canónica es la de (b), lo que hay que corregir es todo el
UN DERIVADO         derivado de F4 —trabajo de F6—; y si es la sin tilde, **hay que enmendar
                    (b)**, que sólo F5 puede hacer. **Las dos salidas son incompatibles y
                    F4 no puede elegir entre ellas**: elegir sería decidir sobre material
                    aprobado sin el Owner

MATERIA MÍNIMA      que F5 declare **cuál de las dos grafías es la CANÓNICA** para el
                    identificador de la segunda participación, y en consecuencia si se
                    enmienda (b) o se alinea el derivado

ALCANCE             `b.16` L836 y todas las sedes derivadas que nombran la variante. **No
                    alcanza a ninguna otra regla**: no cambia qué exige la participación, ni
                    su ancla, ni su cardinalidad — sólo cómo se escribe su nombre

SE PUEDE CONSTRUIR  todo `<CAP>:revision` **como contrato** (§19 y `D104`), que es lo que
                    está escrito. Lo que NO se puede es materializar el identificador en el
                    kernel eligiendo una grafía por cuenta propia

BLOQUEA             la materialización de F6, que tendría que escribir el identificador; y
                    la comprobación de grafía única, que hoy no puede exigir nada

DESPUÉS DE F5       **F6** alinea la sede que quede desalineada, y la comprobación pasa a
                    exigir UNA sola grafía en todo el corpus vigente

CONDICIÓN DE        si el Owner decide que manda la grafía de (b), esta presión se cierra sin
REVERSIÓN           enmendar (b): se corrige el derivado, y `PN-16` queda RESUELTA en vez de
                    retirada

PROPIETARIO         el **Owner**, porque (b) es material aprobado

PRUEBA POSTERIOR    un barrido que exija **UNA sola grafía** para la variante en todo el
                    corpus vigente, con las citas históricas marcadas como tales. **FALLA
                    HOY, y tiene que fallar**: hoy conviven las dos y nadie ha dicho cuál
                    manda. Sólo pasa cuando F5 haya decidido y F6 haya alineado

ORIGEN              hallazgo `M-09` del GATE DE COBERTURA —registrado para F5 y llevado a la
                    checklist `E5-3`— y hallazgo `P-07` del GATE INDEPENDIENTE DE CIERRE CON
                    MANIFIESTOS, que demostró que la justificación del bloque `E5` no cubre
                    esa fila
```

## `PN-17` · NUEVA · `reconciliacion_pendiente` del canal de órdenes no tiene productor, y `T22` no es satisfacible

> **Registrada por `P-07` del GATE INDEPENDIENTE DE CERTIFICACIÓN —documento 22, GRAVE.**
> Reproducida contra las cinco sedes antes de escribirla. **Esta presión NO elige la solución
> normativa y NO redacta ninguna enmienda: registra que hay que elegir, y que la elección es
> del Owner** — porque el identificador y su semántica de ESCRITURA los fija material
> APROBADO, `a.9` y `T22`, que F4 no toca y F6 tampoco puede tocar.

```text
FUENTES             `docs/rediseno/a-CAPACIDADES-APROBADA.md` **L793–797** (`a.9`, el
ENFRENTADAS         mecanismo CAS) y **L1109–1111** (`T22`, prueba de conformidad APROBADA)
                    · `docs/rediseno/b-RECORRIDO-APROBADA.md` **L614–615** (`b.12`, freno 4)
                    · este documento, §2.6.11 **el mecanismo `A`** contra §2.6.9 **el
                    predicado derivado**, veintiséis líneas más abajo

TEXTO VIGENTE       (a) `T22` — «Tres fallos CAS consecutivos detienen el ciclo, dejan las
                    órdenes intactas y **registran `reconciliacion_pendiente`**. No existe un
                    cuarto giro automático»
                    (a) `a.9` — el agotamiento «1. deja TODAS las órdenes sin consumir ·
                    **2. NO modifica el estado canónico** · 3. registra
                    `reconciliacion_pendiente`»
                    (b) `b.12` paso 4 — «FRENOS · racha SIS · devoluciones agotadas · ciclo
                    detectado · recomposiciones sin avance · **`reconciliacion_pendiente`
                    (a.9)** → si hay, se atiende ANTES de despachar»
                    §2.6.9 de este documento, la definición vigente y ÚNICA del predicado —
                    «`reconciliacion_pendiente(item) ≡` existe una transacción con evento
                    `conflicto` SIN terminal … **O BIEN** existe un evento `deriva` SIN
                    reparar que nombra ese item»

QUÉ ES EL DEFECTO   el predicado tiene **exactamente DOS disyuntos, y los dos son sobre el
                    DIARIO DE TRANSACCIONES**. El agotamiento de `MAX_CAS_RETRIES` **no emite
                    ningún evento de diario**: el propio §2.6.11 lo declara «NO es de §2.6» y
                    manda «NO modifica el estado canónico». Luego, tras tres fallos CAS, el
                    predicado es **FALSO**. Consecuencia mecánica y triple: **`T22` no es
                    satisfacible por esta arquitectura**, **el freno 4 de `b.12` nunca
                    dispara** para este caso, y **`reconciliacion_pendiente` no tiene
                    PRODUCTOR** por la vía que (a) le manda tener uno. Y `b.4` `P0` no lo
                    salva: está acotado a «transición multiarchivo incompleta», que es
                    precisamente lo que este caso NO es
                    **Agrava** que §2.6.11 escribe «registra reconciliación pendiente» en la
                    SALIDA del mecanismo `A`, veintiséis líneas antes de que §2.6.9 titule
                    que el predicado **se DERIVA** y que «no hay bandera que escribir»

POR QUÉ NO BASTA    porque las salidas posibles son INCOMPATIBLES entre sí y **cada una toca
UN DERIVADO         una sede distinta**: (i) dar al agotamiento CAS un tercer disyunto en el
                    predicado obliga a que algo durable lo sostenga, y `a.9` prohíbe
                    expresamente modificar el estado canónico; (ii) admitir una bandera
                    persistida reabre exactamente lo que `D49` cerró —«exigía abrir una
                    transacción para registrar lo que impide abrir transacciones»—; (iii)
                    acotar `T22` a otra semántica de «registrar» **enmienda material
                    APROBADO**. **F4 no puede elegir entre ellas**: elegir sería decidir
                    sobre (a) sin el Owner

MATERIA MÍNIMA      que F5 declare **qué significa «registra `reconciliacion_pendiente`» en
                    `a.9` y en `T22` cuando se agota `MAX_CAS_RETRIES`**, y en consecuencia
                    quién es su productor: si un tercer disyunto del predicado derivado, si
                    un registro que no es estado canónico, o si `T22` se enmienda

ALCANCE             `a.9` L793–797, `T22` L1109–1111, el freno 4 de `b.12` y las sedes
                    derivadas que citan el predicado. **No alcanza a la definición de §2.6.9
                    para el resto de sus casos**: las dos ramas del diario siguen siendo
                    correctas para `conflicto` y para `deriva`, y `D49` sigue en pie

SE PUEDE CONSTRUIR  todo lo demás de §2.6.9 y de §2.6.11, que está escrito y no depende de
                    esta elección. Lo que NO se puede es **materializar un productor para el
                    caso CAS eligiendo por cuenta propia** cuál de las tres salidas es la
                    buena

BLOQUEA             **la conformidad con `T22`**, que hoy no es satisfacible por ninguna ruta
REALMENTE           de esta arquitectura, y **el freno 4 de `b.12` para el caso del canal de
                    órdenes**: sin productor, el despacho no se detiene ante un agotamiento
                    CAS. Bloquea también cualquier prueba de F6 que pretenda verificar `T22`
                    en verde

QUÉ NO BLOQUEA      **no bloquea `§2.6` ni el diario de transacciones**: `conflicto` y
                    `deriva` siguen produciendo el predicado por sus dos ramas, y `b.4` `P0`
                    sigue disparando para la transición multiarchivo incompleta. **No bloquea
                    el mecanismo CAS**, que sigue deteniendo el ciclo y dejando las órdenes
                    intactas — lo que no hace es dejar rastro que el predicado vea. **No
                    bloquea `PN-1`** ni depende de ella

CONDICIÓN DE        si el Owner decide que «registrar» en `a.9` significa exactamente lo que
REVERSIÓN           §2.6.9 ya deriva —y que el caso CAS queda fuera del predicado a
                    propósito—, esta presión se cierra **sin enmendar (a)**: lo que se corrige
                    es la redacción de la SALIDA del mecanismo `A` en §2.6.11, que es
                    derivado, y `PN-17` queda RESUELTA en vez de retirada

PROPIETARIO         el **Owner**, porque (a) —`a.9` y `T22`— es material aprobado

FASE                **F5** decide · **F6** materializa el productor que se decida y construye
                    la prueba

PRUEBA POSTERIOR    ejecutar `T22` tal como (a) la escribe: agotar `MAX_CAS_RETRIES` y exigir
                    que `reconciliacion_pendiente` sea **VERDADERO** para el item afectado y
                    que el freno 4 de `b.12` **detenga el despacho**. **FALLA HOY, y tiene
                    que fallar**: con el predicado vigente el resultado es FALSO. Sólo pasa
                    cuando F5 haya decidido y F6 haya materializado el productor

ORIGEN              hallazgo `P3-02` de la cadena `P`, elevado y graduado GRAVE por `P` como
                    `P-07` del documento 22, y clasificado por el adjudicador `R` en su
                    clase `A` —«una PN nueva para `reconciliacion_pendiente`/`T22`»—:
                    **registrar es F4, elegir es F5**
```

## `PN-18` · NUEVA · `VER:decisión` frente a `VER:decision`: la grafía YA materializada, con DOS variantes dentro del kernel construido

> **Registrada por `P-08` del GATE INDEPENDIENTE DE CERTIFICACIÓN —documento 22, GRAVE.**
> `PN-16` se acota literalmente a «la grafía canónica de `<CAP>:revisión`» y a `b.16` L836.
> Esa variante **no tiene ni una sola instancia construida**, mientras la que **YA está
> materializada** —`VER:decisión`— convive en el kernel **con las DOS grafías a la vez**. Se
> registró la presión por el caso hipotético y se dejó pasar el real, que además ya es
> incoherente consigo mismo. **`PN-16` no se reescribe, no se renumera y no se retira**: ésta
> es una presión distinta sobre un identificador distinto, y las dos van al Owner.
>
> **Esta presión NO elige la grafía y NO redacta ninguna enmienda.**

```text
FUENTES             `docs/rediseno/b-RECORRIDO-APROBADA.md` — **DOCE apariciones de
ENFRENTADAS         `VER:decisión`, todas CON TILDE, y CERO sin tilde**
                    contra el kernel construido, que usa **LAS DOS**:
                      CON TILDE   `kernel/operativo/recorrido/01-PROCESOS.md` — **3**
                      SIN TILDE   `kernel/operativo/capacidades/VER/` (`CAPACIDAD.md`,
                                  `composicion.md`, `metodos/Decision.md`, `roles/decision.md`),
                                  `kernel/operativo/circuitos/00-CIRCUITOS.md`,
                                  `kernel/operativo/pruebas/` y `packs/wear-os/composicion.md`
                                  — **14**
                    **LOS RECUENTOS SE DERIVAN, no se escriben**: son el resultado de
                    `grep -c 'VER:decisión' docs/rediseno/b-RECORRIDO-APROBADA.md`,
                    `grep -rn 'VER:decisión' kernel/ | wc -l` y
                    `grep -rn 'VER:decision' kernel/ packs/ | wc -l` sobre el árbol de hoy.
                    Si el árbol se mueve, se vuelven a derivar

TEXTO VIGENTE       (b) escribe `VER:**decisión**` en sus doce apariciones normativas, todas
                    con tilde. **Es material APROBADO: F4 no lo toca y F6 tampoco**

QUÉ ES EL DEFECTO   **el mismo identificador normativo con DOS grafías DENTRO DEL MISMO
                    KERNEL CONSTRUIDO**, y ninguna sede dice cuál manda. No es una
                    discrepancia fuente/derivado como `PN-16`: es una discrepancia **dentro
                    del derivado**, que además discrepa de la fuente en catorce de sus
                    diecisiete apariciones. Un barrido de grafía única falla hoy contra el
                    kernel sin necesidad de mirar (b)

POR QUÉ NO LA       porque `PN-16` está acotada **por su propio texto** a `<CAP>:revisión` y a
CUBRE `PN-16`       `b.16` L836, y `<CAP>:revisión` tiene **CERO instancias construidas** en
                    `kernel/` — verificado con `grep -rn ':revisión' kernel/` y
                    `grep -rn ':revision' kernel/`, que devuelven **cero las dos**. Ampliar
                    `PN-16` para que la cubra sería reescribir una presión ya llevada al
                    Owner, que es exactamente lo que §16 prohíbe hacer

MATERIA MÍNIMA      que F5 declare **cuál de las dos grafías es la CANÓNICA** para
                    `VER:decisión`, y en consecuencia si se enmienda (b) o se alinea el
                    kernel construido

ALCANCE             las doce apariciones de (b) y las diecisiete del kernel y los packs. **No
                    alcanza a ninguna otra regla**: no cambia qué es la decisión de `VER`, ni
                    quién la produce, ni su posición en el recorrido — sólo cómo se escribe
                    su nombre

SE PUEDE CONSTRUIR  nada nuevo hace falta: el identificador YA está construido. Lo que **no**
                    se puede es alinear las diecisiete apariciones eligiendo una grafía por
                    cuenta propia, porque la canónica vive en (b)

BLOQUEA             **la comprobación de grafía única sobre el corpus vigente**, que hoy no
REALMENTE           puede exigir nada, y **cualquier resolución automática de
                    `VER:decision(¿?)` por igualdad de cadena**: un contraste por igualdad
                    falla contra tres sedes o contra catorce, según cuál se tome por buena.
                    Bloquea también la alineación de F6, que tendría que elegir

QUÉ NO BLOQUEA      **no bloquea el recorrido**: las dos grafías resuelven hoy a la misma
                    participación para cualquier lector humano, y ninguna ruta queda sin
                    vehículo por esto. **No bloquea `PN-16`**, que sigue vigente y separada.
                    **No bloquea F6 en lo demás**: sólo en el acto de escribir el nombre

CONDICIÓN DE        si el Owner decide que manda la grafía de (b) —con tilde—, esta presión
REVERSIÓN           se cierra **sin enmendar (b)**: se alinean las catorce apariciones sin
                    tilde del kernel y de los packs, y `PN-18` queda RESUELTA en vez de
                    retirada. La simétrica también vale, y entonces sí enmienda (b)

PROPIETARIO         el **Owner**, porque (b) es material aprobado

FASE                **F5** decide · **F6** alinea el kernel construido

PRUEBA POSTERIOR    un barrido que exija **UNA SOLA GRAFÍA** de `VER:decisión` en todo el
                    corpus vigente —(b), `kernel/` y `packs/`—, con las citas históricas
                    marcadas como tales. **FALLA HOY, y tiene que fallar**: hoy conviven las
                    dos DENTRO del kernel, y nadie ha dicho cuál manda. Sólo pasa cuando F5
                    haya decidido y F6 haya alineado

ORIGEN              hallazgo `P3-03` de la cadena `P`, elevado y graduado GRAVE por `P` como
                    `P-08` del documento 22, y clasificado por el adjudicador `R` en su
                    clase `A` —«otra [PN] … para `VER:decisión` frente a `VER:decision`, que
                    ya conviven dentro del kernel construido»
```

**Resumen para el Owner, tras revisar las cinco de la entrega anterior:**

```text
VIGENTES · DIECISÉIS
  PN-1   la sección (g). LA ÚNICA QUE BLOQUEA TODO EL ESTADO DURABLE, y ahora decide más
  PN-2   la política de auditoría como tercera vía de creación de trabajo
  PN-3   G03 y la ejecución desatendida. Misma pregunta que PN-2 por otro camino, y
         absorbe lo que era PN-5
  PN-6   qué significa «Integrada» para un producto de 0 o 1 fuente
  PN-7   b.14 paso 2 dice «completar o revertir». §2.6 tiene LAS DOS RAMAS, y
         lo que presiona es la PRECISIÓN: (b) no distingue estado PUBLICADO de
         estado ESPECULATIVO, y sólo el segundo se revierte                    NUEVA
  PN-8   VER no está en la ruta AUD, y §5.6 exige su dictamen                 NUEVA
  PN-9   los predicados de obligación de b.3 a nivel de iniciativa. Probablemente
         NINGUNA materia, y F5 debe confirmarlo                               NUEVA
  PN-10  O11 dice «estado durable» y F4 deriva el estado. Simetría con PN-6   NUEVA
  PN-11  el gobierno Git del CONTROL REPO no tiene sede normativa: C7 gobierna
         las fuentes y E2.4 cierra la vía de G29. BLOQUEA la publicación        NUEVA
  PN-12  el «mapa documental» de O8 se satisface DERIVADO. Misma vara que
         PN-6 y PN-10. No bloquea                                              NUEVA
  PN-13  b.16 no da a proceso:SIS ni a proceso:INV ninguna vía para DOM, SEG
         ni DIS, y INS-5 las necesita antes del gate «listo para construir»        NUEVA
  PN-14  `DIS/Reconstruccion` —un MÉTODO, no una capacidad— está en b.16 L895 y
         en a.6 L495, que son material APROBADO. Corregir sólo el kernel
         cambiaría el derivado dejando la fuente, que es el modo de fallo que
         §15.7 registra para C7. Sale de reclasificar `F-01`                      NUEVA
  PN-15  KERNEL.md 1.5.0 G20–G23: §8 sustituye la ruta cuyo gate de salida G21
         declara NO NEGOCIABLE POR EL SISTEMA, y ni a.11 lo deroga ni §17 tenía
         fila para KERNEL.md. Hasta que F5 decida, las cuatro SIGUEN VIGENTES.
         Sale de K-06
  PN-16  la GRAFÍA CANÓNICA de <CAP>:revisión. (b) L836 la escribe CON TILDE y
         todo el derivado de F4 SIN TILDE. Si manda (b), corrige F6; si manda la
         sin tilde, F5 ENMIENDA (b). F4 no elige. Sale de P-07                    NUEVA
  PN-17  `reconciliacion_pendiente` del canal de órdenes NO TIENE PRODUCTOR: el
         agotamiento de MAX_CAS_RETRIES declara que NO modifica el estado canónico
         y el predicado de §2.6.9 sólo mira el diario, luego T22 —prueba de
         conformidad APROBADA— no es satisfacible y el freno 4 de b.12 nunca
         dispara. Sale de P-07 del doc 22                                            NUEVA
  PN-18  la GRAFÍA de `VER:decisión`, que YA ESTÁ CONSTRUIDA y convive con DOS
         variantes DENTRO del kernel: 12 con tilde en (b), 3 con tilde y 14 sin
         tilde en kernel/ y packs/. PN-16 no la cubre: se acota a <CAP>:revisión,
         que tiene CERO instancias. Sale de P-08 del doc 22                          NUEVA

RETIRADA · UNA
  PN-4   con su motivo escrito, y reinstaurable por F5 si el Owner lo prefiere

FUSIONADA · UNA
  PN-5   dentro de PN-3, porque su enmienda es la misma

CUATRO SON UNA FRASE       PN-6, PN-7, PN-9 y PN-10. Y tres de ellas se registran
CADA UNA                   PRECISAMENTE PORQUE parecen obvias: PN-6 fijó esa vara, y
                           aplicarla de forma desigual sería el defecto

EL TOTAL SE DERIVA         un barrido de las cabeceras `## \`PN-` da DIECIOCHO; menos PN-4
                           RETIRADA y PN-5 FUSIONADA, quedan DIECISÉIS. No se escribe a mano,
                           y por eso se mueve cuando aparece una nueva — y acaba de moverse
                           con `PN-17` y `PN-18`.
                           **Y ES LA ÚNICA SEDE QUE PUEDE PUBLICARLO.** Toda otra sede de
                           este documento que necesite el total o el rango **REMITE aquí**
                           en vez de copiarlo: una lista copiada envejece sola, una remisión
                           no. Es la garantía que la cabecera de §16 declara, y la razón de
                           que §0, §8.2 y §19 hayan caducado ya

NO SE RENUMERA NINGUNA. Renumerar rompería la trazabilidad de lo que ya se llevó al Owner.
```

> **Lo que NO es presión normativa, y se dice para que nadie lo lleve al Owner.** El defecto
> de `C7` (§9.5) es material **derivado** de `E2`: su corrección está completamente
> determinada por `E2.6`, no requiere decisión del Owner, y su sitio es F6. Y las **SEIS**
> extensiones de ficha de §5.2 —`ENT`, `ARQ`, `PLT`, `SEG`, `DSP` y `ENC`— tampoco lo son:
> extender una ficha con materia que ya está en su alcance es trabajo de F6.
> **Corregido por `I-06`**: decía «cuatro», que era el recuento anterior a `M-5` y `M-6`.

---

# 17 · Migración desde el ADS actual

| pieza actual | qué le pasa |
|---|---|
| (a), (b), `E1`, `E2` | **intactas**. F4 no las toca, y sus presiones están en §16 |
| `K-1` tres capas | **intacta**. §1.2 clasifica ciclo de vida, no conocimiento |
| `C1`–`C7` | **NO todos intactos, y esta columna es la lista de trabajo de F6, luego se lee como exhaustiva.** `C2` se amplía en F6. **`C7` se reutiliza CON UNA CORRECCIÓN PENDIENTE, NOMBRADA**: su `gate:convergencia-de-fuentes` dice `aplica_a: "una o más fuentes"` y `E2.6` dice «varias sources», con lo que **con el texto vigente ningún producto de un repositorio cierra un solo item** — §15.7 y §9.5 lo declaran, §9.5 lleva la prescripción cerrada, y el contrato **sigue diciendo «una o más»**. **`C5` y `C6` se reutilizan CON EXCEPCIÓN NOMBRADA** (§15.7, §9.5). **Corregido por `P-14` del documento 22**, que reprodujo el `aplica_a` contra el contrato mismo. **La lista de qué le pasa a cada contrato NO se copia aquí: la sede que la deriva es §15.7, y esta fila REMITE a ella** — una lista copiada en la lista de trabajo de F6 envejece sola |
| quince capacidades, roles, métodos, prompts | **intactos**. Son los RESPONSABLES de los aspectos de §5.2, no los aspectos. **`+6` extensiones de ficha**: `ENT`, `ARQ`, `PLT`, `SEG`, **`DSP`** (`M-5` · abrir items `AUD` dentro de una política `O7` vigente) y **`ENC`** (`M-6` · admitir un finding de auditoría como entrada, con la celda de cobertura por sujeto). **Corregido por `I-06`**: decía `+4`, y era la mitad literal del cierre de `M-6` —«añadir `capacidades/ENC/` a §5.2 **y a §17**»— que no se había hecho. §5.2, §16 y §17 dicen ahora la misma cifra. **Y las fichas de las capacidades LÍDERES de cobertura se extienden también** —no es un `+1` condicional: `D91` ya lo decidió y fija que **el conjunto se DERIVA de los `contrato-de-aspecto`, no se escribe a mano**, luego es un conjunto derivado ya resuelto y no un incremento pendiente de una condición. Corregido por `K-10` |
| diez procesos de `b.16` | **el NÚMERO es intacto: siguen siendo DIEZ y ningún macrocircuito crea uno nuevo. Los PROCESOS no lo son.** §19 (`D104`) contrata que **F6 instancie nueve pares `<CAP>:revision` repartidos en CINCO de los diez**, con su error `composicion-incompleta`, y que edite `kernel/operativo/recorrido/01-PROCESOS.md`. **La distinción es la misma que la fila vecina hace con las quince capacidades** —«intactos … **`+6` extensiones de ficha**»—, y esta fila no la hacía: **corregido por `P-15` del documento 22**. **El reparto exacto no se copia aquí: lo deriva §19**, que es su sede, y a ella remite esta fila |
| diecinueve esquemas | **+4 de estado**: `iniciativa`, `adaptador`, `cobertura`, `evento`. **+2 de clase**: `nivel-certificacion` y `contrato-de-aspecto`, con el precedente de `nivel-novedad`. `memoria` y `validadores.yaml` se amplían. **Total 25** (§3.8) |
| packs | **intactos**, `+2` piezas en `web-app` (`CAND-022`, `CAND-024`) |
| trece validadores | **intactos**, `+entradas:` por `P-08` |
| `plantillas/CHECKPOINT.md` | **intacta**: `E2.3` ya le dio forma multi-fuente |
| `tooling/workspace.py` | **intacto** |
| `tooling/compile-agents.sh` | **sustituido** por el compilador de §6.2. Hoy no compila |
| `kernel/KERNEL.md` `G20`–`G23` | **PRESIONADAS y pendientes de F5. NO derogadas por F4, y NO sustituidas por §8.** `G21` declara que el gate de salida del Circuito 0 lo fija la constitución y **no es negociable por el sistema**; `G22` fija su timebox, sus diez entregables y sus cuatro prohibiciones. `a.11` —«la única lista que deroga o ajusta reglas», `PN-3`— **no las nombra**, y `E2.4` demuestra que lo no nombrado sobrevive. **Hasta que F5 decida regla a regla, las cuatro SIGUEN VIGENTES**, y §8.1 no las deroga: es un diseño que las presiona. La decisión y su enmienda son `PN-15` (`D97`), registrada por `K-06` |
| `START_HERE.md` rutas A y B | **sustituidas** por §8.1 y §8.2, que son sus versiones con estado y gates — **con la reserva de `PN-15`**: la ruta A termina hoy «cuando existen los 10 entregables de `G22`, dentro del timebox», y esa condición pertenece a `KERNEL.md`, no a `START_HERE.md`. Mientras `PN-15` no se resuelva, la sustitución alcanza a la ruta como TEXTO DE ENTRADA y **no** al gate constitucional que invoca |
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

### Los cuatro macrocircuitos, mapeados a los procesos de `b.16`

> **Añadido por la tercera revisión independiente (`G6`; es `D67`).** §8.0 prohíbe crear un
> proceso nuevo y declara que cada macrocircuito «es una INICIATIVA con su plantilla de
> ruta». Pero la ruta, las obligaciones, el propietario global y los gates de cada item **se
> derivan del proceso** (`b.16`), y tres de los cuatro no nombraban ninguno: F6 habría tenido
> que ELEGIR, y esa elección determina obligaciones y autoridad. Se declara aquí, y **no se
> crea ningún proceso**: los diez de `b.16` bastan.

> **Reescrita por el gate final independiente (`B-1`, `B-2`, `G-1`, `G-2`, `M-3`, `m-4` y
> `F-01`; es `D75`).** La versión anterior tenía cuatro defectos que se apoyaban entre sí:
> ponía nombres de PROCESO —`AUD`, `DEU`— en la columna de PARTICIPANTES, que sólo admite
> CAPACIDADES; asignaba a `A2`–`A7` un proceso que §8.2 desmentía; listaba participantes que
> el proceso asignado **no admite por ninguna vía**; y confundía ejecutores y autoridades con
> participantes. **Ahora cada capacidad lleva su vía de §8.0**, y las quince capacidades son
> `APR ARQ CON DIS DOM DSP ENC ENT INV PLT PRD SEG SIS USO VER` — ni `AUD` ni `DEU` ni `DEP`
> están entre ellas.

| macrocircuito | fase | proceso `b.16` | propietario global | participantes de la RUTA, con su vía | ejecutor y autoridad | entrada | salida | gate | estado persistido |
|---|---|---|---|---|---|---|---|---|---|
| **N · instalación** | **`FASE 0`** · CERTIFICACIÓN ESTRUCTURAL | `proceso:SIS` | **`SIS`** (vía 1), **productor y propietario de la declaración** (`O17` vía `D107`) | `VER` vía 2, produce el DOSIER y **no se apropia de la decisión** · **`SEG` sin vía: `PN-13`** — y **conserva su bloqueo**, que es lo ÚNICO que `O17` le da y lo único que §9.6 recoge. Corregido contra §9.6 por la jerarquía de precedencia declarada allí | ejecutor `PLT` cuando el contrato vigente le atribuya la maquinaria técnica · autoridad `SIS`, con el veto de `SEG` · **el propietario de `N` no puede sustituir a `SIS`, y DEBE exigirla** | el disparador de `N`, **con CERO mutaciones canónicas hechas**, y el SUJETO de los seis identificadores de §9.6 resuelto | **la declaración Estructural de ESTA ejecución**, con su sujeto, su evidencia y su huella. Una por ejecución, y ninguna heredada | **`gate:sistema-conforme` (§9.6)** — el MISMO contrato para los cuatro. Si falla, **BLOQUEA antes de mutar estado** | celda `aspecto:certificacion/estructural` del sujeto, con su vigencia y su condición de invalidación, **en el SOPORTE DURABLE DE LA FASE 0 —anterior al `estado/` del macrocircuito—, que la primera fase que crea `estado/` INCORPORA sin reemitirla (§9.6)** |
| | `INS-0`–`INS-5` | `proceso:SIS` | **`SIS`** (vía 1) | `CON` `VER` vía 2 · `APR` `C-APR` vía 3 · `PRD` `ARQ` vía 4, items `INV` enlazados de discovery · **`DOM` `DIS` `SEG` sin vía: `PN-13`** | ejecutor `PLT` MATERIALIZA (`C7:82`) · autoridad Owner | decisión del Owner de instalar | control repo, topología, especialización y adaptadores · **el BASELINE de producto, dominio y diseño de `INS-5`** · **la CLASIFICACIÓN DE DESCONOCIDOS CRÍTICOS**, cada uno resuelto, acotado con su portador o deferido con su motivo | `INS-4` certificación Operativa · **`INS-5` BASELINE APROBADO POR EL OWNER** —la misma disposición que `A3` en la adopción— | `estado/` e `INI-001` desde `INS-0`, sobre el item `SIS-001` |
| | `INS-6`–`INS-7` | `proceso:SIS` | **`SIS`** (vía 1) | `CON` `VER` vía 2 · `ENT` vía 3, «modifica el runtime» | `PLT` MATERIALIZA (`C7:82`) · **`CON` con custodia hace rama, commit, push y PR** del puntero (`C7:83`–`C7:86`) · `SEG` puede bloquear el push · `ENT` merge y convergencia (`C7:88`–`C7:89`) · autoridad Owner | **especialización aprobada Y baseline de `INS-5` aprobado por el Owner** | punteros propagados y nivel Integrada | `INS-7` = `O12`, **con sus TRES condiciones y el productor de cada una**: Integrada la produce `INS-7` con la aplicabilidad de §9.5 · el BASELINE APROBADO lo produce `INS-5` y lo aprueba el Owner · la CLASIFICACIÓN DE DESCONOCIDOS CRÍTICOS la produce `INS-5` como entregable propio. Ninguna queda sin productor identificable | evidencia + celdas de cobertura |
| **A · adopción** | **`FASE 0`** · CERTIFICACIÓN ESTRUCTURAL | `proceso:SIS` | **`SIS`** (vía 1), **productor y propietario de la declaración** (`O17` vía `D107`) | `VER` vía 2, produce el DOSIER y **no se apropia de la decisión** · **`SEG` sin vía: `PN-13`** — y **conserva su bloqueo**, que es lo ÚNICO que `O17` le da y lo único que §9.6 recoge. Corregido contra §9.6 por la jerarquía de precedencia declarada allí | ejecutor `PLT` cuando el contrato vigente le atribuya la maquinaria técnica · autoridad `SIS`, con el veto de `SEG` · **el propietario de `A` no puede sustituir a `SIS`, y DEBE exigirla** | el disparador de `A`, **con CERO mutaciones canónicas hechas**, y el SUJETO de los seis identificadores de §9.6 resuelto | **la declaración Estructural de ESTA ejecución**, con su sujeto, su evidencia y su huella. Una por ejecución, y ninguna heredada | **`gate:sistema-conforme` (§9.6)** — el MISMO contrato para los cuatro. Si falla, **BLOQUEA antes de mutar estado** | celda `aspecto:certificacion/estructural` del sujeto, con su vigencia y su condición de invalidación, **en el SOPORTE DURABLE DE LA FASE 0 —anterior al `estado/` del macrocircuito—, que la primera fase que crea `estado/` INCORPORA sin reemitirla (§9.6)** |
| | `A0`–`A1` | `proceso:SIS` | **`SIS`** (vía 1) | `CON` `VER` vía 2 | ejecutor `PLT` MATERIALIZA (`C7:82`) · autoridad Owner | el Owner quiere gobernar un producto con historia | perímetro y topología | modo no destructivo declarado | iniciativa + `estado/` |
| | `A2`–`A7` | **`proceso:AUD`**, en items ENLAZADOS, **uno por conclusión** | **DERIVADO por item** del encargo (`b.16`): la capacidad responsable de esa conclusión — `PRD`, `ARQ`, `DOM`, `DIS`, `SEG` y `ENT` en las ocho de `A6`. **NUNCA a mano** | `INV` vía 2, única obligatoria, ejecuta y no responde de la conclusión · `DOM` `C-DOM` · `SEG` `C-SEG` · `DIS` `C-DIS` · `PRD` «produce una decisión de producto» · `APR` `C-APR`, vía 3 | encuadre `ENC` (previo a la ruta) · autoridad Owner en `A3` | acceso de lectura a las fuentes | inventario, baseline, producto reconstruido y trabajo vivo | `A3` baseline aprobado por el Owner | capas por item, con procedencia |
| | `A8` | `proceso:DEU` | **`ARQ`** (vía 1) | `CON` vía 2 (`cambio-construido`) · `VER` vía 2 · `DOM:condiciones` `SEG:condiciones` `ENT` `USO` `APR` vía 3 | `PLT` MATERIALIZA (`C7:82`) · **`CON` con custodia hace rama, commit, push y PR** (`C7:83`–`C7:86`) · `SEG` puede bloquear el push · `ENT` merge y convergencia (`C7:88`–`C7:89`) · autoridad Owner, POR FUENTE | autorización de retirada | copias organizativas y verdades paralelas retiradas | `A8` autorizado por el Owner | source changes por fuente |
| | `A9`–`A10` | `proceso:SIS` | **`SIS`** (vía 1) | `CON` `VER` vía 2 · **`SEG` sin vía si hay superficie: `PN-13`**, y entretanto item `AUD` enlazado con `SEG` de propietaria derivada | ejecutor `PLT` MATERIALIZA (`C7:82`) · autoridad Owner | limpieza cerrada | nivel Integrada | `A10` = `O12` | celdas de certificación |
| **M · migración** | **`FASE 0`** · CERTIFICACIÓN ESTRUCTURAL | `proceso:SIS` | **`SIS`** (vía 1), **productor y propietario de la declaración** (`O17` vía `D107`) | `VER` vía 2, produce el DOSIER y **no se apropia de la decisión** · **`SEG` sin vía: `PN-13`** — y **conserva su bloqueo**, que es lo ÚNICO que `O17` le da y lo único que §9.6 recoge. Corregido contra §9.6 por la jerarquía de precedencia declarada allí | ejecutor `PLT` cuando el contrato vigente le atribuya la maquinaria técnica · autoridad `SIS`, con el veto de `SEG` · **el propietario de `M` no puede sustituir a `SIS`, y DEBE exigirla** | el disparador de `M`, **con CERO mutaciones canónicas hechas**, y el SUJETO de los seis identificadores de §9.6 resuelto | **la declaración Estructural de ESTA ejecución**, con su sujeto, su evidencia y su huella. Una por ejecución, y ninguna heredada | **`gate:sistema-conforme` (§9.6)** — el MISMO contrato para los cuatro. Si falla, **BLOQUEA antes de mutar estado** | celda `aspecto:certificacion/estructural` del sujeto, con su vigencia y su condición de invalidación, **en el SOPORTE DURABLE DE LA FASE 0 —anterior al `estado/` del macrocircuito—, que la primera fase que crea `estado/` INCORPORA sin reemitirla (§9.6)** |
| | `M0`–`M5` | `proceso:SIS` | **`SIS`** (vía 1) | `CON` `VER` vía 2 · `ENT` vía 3 | ejecutor `PLT` MATERIALIZA (`C7:82`) · autoridad Owner | existe una instalación de una versión anterior | estado migrado, verificado y certificado | `M3` equivalencia · `M5` Integrada | `estado/` migrado + evento `migracion` |
| | `M6`–`M7` | `proceso:DEU` | **`ARQ`** (vía 1) — su `plan-tecnico` es ENTRADA de `M5` | `CON` vía 2 (`cambio-construido`) · `VER` vía 2, y verifica `M7` · `DOM:condiciones` `SEG:condiciones` `ENT` `USO` `APR` vía 3 | `PLT` MATERIALIZA (`C7:82`) · **`CON` con custodia hace rama, commit, push y PR** (`C7:83`–`C7:86`) · `SEG` puede bloquear el push · `ENT` merge y convergencia (`C7:88`–`C7:89`) · autoridad Owner, POR FUENTE | `M5` certificado y autorización POR FUENTE | heredado retirado y verificado | `M6` autorizado · `M7` verificado | source changes + `INTEGRACIÓN PARCIAL` |
| **U · actualización** | **`FASE 0`** · CERTIFICACIÓN ESTRUCTURAL | `proceso:SIS` | **`SIS`** (vía 1), **productor y propietario de la declaración** (`O17` vía `D107`) | `VER` vía 2, produce el DOSIER y **no se apropia de la decisión** · **`SEG` sin vía: `PN-13`** — y **conserva su bloqueo**, que es lo ÚNICO que `O17` le da y lo único que §9.6 recoge. Corregido contra §9.6 por la jerarquía de precedencia declarada allí | ejecutor `PLT` cuando el contrato vigente le atribuya la maquinaria técnica · autoridad `SIS`, con el veto de `SEG` · **el propietario de `U` no puede sustituir a `SIS`, y DEBE exigirla** | el disparador de `U`, **con CERO mutaciones canónicas hechas**, y el SUJETO de los seis identificadores de §9.6 resuelto | **la declaración Estructural de ESTA ejecución**, con su sujeto, su evidencia y su huella. Una por ejecución, y ninguna heredada | **`gate:sistema-conforme` (§9.6)** — el MISMO contrato para los cuatro. Si falla, **BLOQUEA antes de mutar estado** | celda `aspecto:certificacion/estructural` del sujeto, con su vigencia y su condición de invalidación, **en el SOPORTE DURABLE DE LA FASE 0 —anterior al `estado/` del macrocircuito—, que la primera fase que crea `estado/` INCORPORA sin reemitirla (§9.6)** |
| | `U0`–`U4` | `proceso:SIS` | **`SIS`** (vía 1) | `CON` `VER` vía 2 · `ENT` vía 3 | ejecutor `PLT` MATERIALIZA (`C7:82`) · autoridad Owner en `U3` | hay una versión nueva de ADS | compatibilidad decidida y migración aplicada | `U3` punto de no retorno | instantánea de `U3` + progreso por pasos |
| | **`U5a`** | `proceso:SIS` | **`SIS`** (vía 1) | `CON` `VER` vía 2 | ejecutor el runtime del control repo | migración aplicada | proyecciones del control repo recompiladas | ninguno propio: cae en `U6` | huella de proyección (§6.3) |
| | **`U5b`** | `proceso:DEP` | **`PLT`** (vía 1) | **`SEG` vía 2** (`condiciones-de-seguridad`, ANTES de construir; `G28` la hace irretirable) · **`CON` vía 2** (`cambio-construido`) · `VER` vía 2 · `DOM:condiciones` `ARQ` `ENT` vía 3 | `PLT` MATERIALIZA (`C7:82`) y participa por **vía 1** · **`CON` con custodia hace rama, commit, push y PR** (`C7:83`–`C7:86`) · `SEG` puede bloquear el push · `ENT` merge y convergencia (`C7:88`–`C7:89`) · autoridad Owner si hay retirada | `U5a` cerrado | punteros propagados a cada fuente | gate por fuente, con Integration Set si hay más de una | `INTEGRACIÓN PARCIAL` por fuente |
| | **`U6`** | `proceso:SIS` | **`SIS`** (vía 1) | `VER` vía 2 | autoridad Owner si la revalidación baja el nivel | `U5b` convergido | ADS actualizado y recertificado | **revalidación del nivel VIGENTE**, no `O12`: una actualización no arranca programación, y `O12` gobierna ese arranque. Bajar de nivel es un fallo, no un resultado | celdas de certificación |

> **Los propietarios globales NO se eligen: los fija `b.16`.** `proceso:SIS` → `SIS`,
> `proceso:INV` → `INV`, `proceso:DEU` → **`ARQ`** y `proceso:DEP` → `PLT`, verificados uno a
> uno contra `01-PROCESOS.md`. **`proceso:AUD` es el único que NO lo fija**: lo DERIVA del
> encargo, y `01-PROCESOS.md` L419 prohíbe expresamente asignarlo a mano. Por eso `A2`–`A7`
> no tiene UN propietario: tiene uno POR ITEM, y son varios items porque son varias
> conclusiones independientes. `DEU` y `DEP` son **procesos**, no capacidades: las quince son
> `APR ARQ CON DIS DOM DSP ENC ENT INV PLT PRD SEG SIS USO VER`, y confundir el nombre de un
> proceso con el de una capacidad es el mismo modo de fallo que `G1` corrigió con `a.9`.

```text
POR QUÉ NINGUNO ES        porque ninguno cambia la fábrica de forma que los diez procesos no
UN PROCESO NUEVO          puedan representar, y sus INTENCIONES lo dicen literalmente:
                            · instalar, migrar, actualizar y certificar son `proceso:SIS`,
                              «cambiar la propia fábrica: memoria, plantillas, catálogo,
                              composiciones o runtime»
                            · inventariar y reconstruir un producto con historia es
                              `proceso:AUD`, «producir una CONCLUSIÓN sobre un objeto ya
                              existente, para que alguien decida con ella». `INV` es su
                              única obligatoria, no su proceso: ejecuta la auditoría sin
                              responder de la conclusión (`a.5`)
                            · retirar lo heredado es `proceso:DEU`, «reducir riesgo interno o
                              coste de cambio, sin introducir capacidad de producto»
                            · y `proceso:DEP` —«incorporar, actualizar o retirar una
                              DEPENDENCIA EXTERNA»— aparece sólo donde de verdad hay una:
                              `U5b`, cuando la versión nueva de ADS entra en cada fuente
                          La prueba de §3.1 no llega a plantearse.

QUÉ ES ENTONCES «SU       una COMPOSICIÓN declarada de items de esos procesos, no un
PLANTILLA DE RUTA»        artefacto. **No es un tipo**, no entra en §3.8 y no tiene esquema:
                          es esta tabla. Llamarla «plantilla» sugería un artefacto que no
                          existe, y `G6` lo señaló.

QUÉ NO SE APLANA          que compartan motor NO borra sus diferencias: cada uno conserva su
                          disparador, sus precondiciones, sus gates, su rollback, su
                          reanudación y su cierre, que es lo que `CI-5` protege.
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
NADA ESTÁ PROBADO         los doce escenarios de §14, las CUARENTA Y SEIS filas de la tabla
                          adversarial de §2.6.7, los ONCE escenarios negativos de §11.5, las
                          OCHO comprobaciones `X-A`–`X-H` de §2.9 y **las NUEVE
                          `X-S1`–`X-S9` de la FASE 0 de §9.6**, que esta tanda añade con la
                          propagación de `O17` (`D107`). **Las nueve ventanas de
                          reconciliación NO se cuentan: `D64` las retiró**, y §2.6.9 lo
                          dice — contarlas era inflar el inventario con algo inexistente.
                          **Cada familia lleva su cifra en SU sede y aquí se remite**:
                          §2.6.7 sigue en cuarenta y seis y no se toca, §2.9 en ocho, y §9.6
                          es la sede de la familia `X-S`
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
LAS PRESIONES             **§16, y su total NO se copia aquí: se DERIVA allí de las cabeceras
NORMATIVAS VIGENTES       `## \`PN-`, menos las marcadas RETIRADA o FUSIONADA, y §16 es la
                          ÚNICA sede que lo publica.** Tras DOS devoluciones independientes,
                          la TERCERA REVISIÓN, el GATE FINAL, el GATE DE CIERRE, el GATE
                          DEFINITIVO, el GATE DE COBERTURA, el GATE DE CIERRE CON MANIFIESTOS
                          y el GATE INDEPENDIENTE DE CERTIFICACIÓN: `PN-4` retirada, `PN-5`
                          fusionada en `PN-3`, y `PN-6` a `PN-18` nuevas.
                          `PN-1` bloquea todo el estado durable, y F5 es su puerta.
                          **Las DOS que esta tanda añade son `PN-17` y `PN-18`**, y salen de
                          `P-07` y `P-08` del documento 22: `reconciliacion_pendiente` del
                          canal de órdenes sin productor —con `T22` no satisfacible— y la
                          grafía de `VER:decisión`, que ya está construida con DOS variantes
                          dentro del kernel. Las dos viven en material APROBADO, y F4 no
                          puede elegir por el Owner en ninguna de las dos.
                          **Corregido por `P-04`**: este bloque llevaba el titular CATORCE y
                          el rango `PN-6`–`PN-16` escritos a mano
F4 NO ESTÁ CERTIFICADA    la escribe quien la propone. TRES críticas independientes, una
                          devolución técnica, un GATE FINAL con tres agentes y su
                          COMPLEMENTO DE COBERTURA la han devuelto. La TERCERA REVISIÓN
                          INDEPENDIENTE **ya se emitió** —veredicto INSUFICIENTE PARA F5— y
                          el gate lo **confirmó** por dos razones independientes. Todo está
                          aplicado, y LO APLICÓ QUIEN LO RECIBIÓ: `F4c` sigue ABIERTA, y lo
                          que queda pendiente es un juicio independiente sobre la tanda que
                          cierra los 43 hallazgos, no la tercera revisión
```

## Lo que esta fase NO puede corregir, con su propietario y su fase

**SIETE de los cuarenta y tres hallazgos del gate tienen su sede FUERA de F4** —en el kernel,
en `docs/owner/` o en el propio documento del gate—, y esta fase **no los toca**: modificar
kernel, esquemas, contratos o pruebas es F6, y modificar material en voz del Owner es suyo.
Se registran aquí con propietario y fase para que nadie los dé por cerrados, **y no se
cuentan como «F4 corregida»**.

> **Eran OCHO, y ahora son SIETE.** `F-01` deja de ser externo: el gate de cierre demostró
> que su sede alcanza a `b.16` L895 y a `a.6` L495 —material APROBADO— y que su remedio, tal
> como estaba escrito, **no era ejecutable** para su fin declarado. Pasa a
> `PRESION_LISTA_PARA_F5` con `PN-14`, y **conserva su trabajo de F6** —el kernel—, que se
> ejecuta DESPUÉS. Sigue figurando en la tabla de abajo porque su mitad de F6 vive aquí.

> **La tabla tiene NUEVE filas y los externos son SIETE, y no es un descuadre** —corregido
> por `K-04`, que demostró que la reconciliación anterior decía «los externos son OCHO» seis
> líneas después de declarar que `F-01` había dejado de serlo, y así contaba a `F-01` en los
> dos lados—. **Las dos filas que NO son externas:**
>
> - **`F-01`**, que acaba de dejar de serlo en el párrafo anterior: pasa a
>   `PRESION_LISTA_PARA_F5` con `PN-14`, y figura abajo porque **conserva su trabajo de F6**.
> - **`F-05`**, que **nunca lo fue**: sus tres condiciones de cierre se cumplen en esta fase
>   —§15.7 registra la excepción de `C5`, y §8.0 declara qué checkpoint viaja—, y lo que
>   aparece abajo es el residuo OPTATIVO que `00-CIRCUITOS` L238 desactiva expresamente.
>   Figura aquí porque su trabajo residual vive en `circuitos/`. Su estado primario es
>   `CORREGIDO_EN_F4`.
>
> **La aritmética, entera: 9 filas = 7 externos + `F-01` + `F-05`.** Los siete
> `EXTERNO_CON_PROPIETARIO` de la matriz son `F-02`, `F-04`, `F-06`, `F-07`, `F-08`, `F-10` y
> `F-11`, y coinciden con el estado primario que la matriz de cierre les asigna.

| hallazgo | qué hay que hacer | dónde | propietario | fase | ¿bloquea la implementabilidad de F4? |
|---|---|---|---|---|---|
| `F-01` | **RECLASIFICADO por el gate de cierre.** Ya NO es un externo de F6: la cadena `DIS/Reconstruccion` está también en **`b.16` L895 y `a.6` L495**, que son material APROBADO e intocable por F4 **y por F6**. Corregir sólo el kernel cambiaría el derivado dejando la fuente. La presión es **`PN-14`** (§16), y **F5 es su puerta**; después, **F6** actualiza `01-PROCESOS.md` L434 y `00-CIRCUITOS.md` L166 | (a) `a.6` · (b) `b.16` → **F5** · después `recorrido/01-PROCESOS.md` · `circuitos/00-CIRCUITOS.md` → F6 | el **Owner** para (a) y (b) · `SIS` para el kernel | **F5 y F6** | **SÍ, parcialmente.** §8.2 y §18 ya dicen `DIS` `C-DIS`; (a), (b) y el kernel siguen diciendo `DIS/Reconstruccion`. Mientras difieran, la composición de `A2`–`A7` **no es verificable mecánicamente** contra la fuente. **No invalida la arquitectura**: el conjunto de participantes es idéntico bajo las dos lecturas |
| `F-02` | **el vocabulario ya está escrito, y F6 no tiene que decidirlo.** Lo fijó `E-3` del documento 17, que es corpus inmutable, y esta tanda lo RECOGE aquí porque §19 no lo llevaba (`I-13`): (1) la **capacidad base** es una de las QUINCE, y sólo una de las quince; (2) admite un **sufijo `:<variante>` OPCIONAL y TIPADO**, con la variante declarada —`DOM:condiciones`, `SEG:condiciones`, `SEG:revision`, `CON:experimental`, `ARQ:diagnostico`—, que es la notación que la propia F4 usa en §8.2, §8.3, §8.4 y §18; (3) **`/` NO es válido para variantes** — es lo que hoy admite un MÉTODO donde va una capacidad, y es la raíz de `F-01`/`PN-14`; (4) **`capacidad_productora` usa la MISMA referencia** y el mismo vocabulario; (5) **`OWNER` NO es una capacidad**: se separa como AUTORIDAD, en su propio campo, porque las quince no lo incluyen. Con eso, tipar `capacidad` y `capacidad_productora` como `ref_a: capacidad` **deja de invalidar la notación de la propia F4** | `esquemas/proceso.yaml` — el cambio exacto de esquema: `ref_a: capacidad` con sufijo `:` opcional tipado, y un campo de autoridad separado para `OWNER` · y en `recorrido/01-PROCESOS.md`, sustituir `DIS/Reconstruccion` (tras `PN-14`) y mover `OWNER` a autoridad. **F4 NO modifica el esquema** | `SIS` | **F6** | no hoy. Es la RAÍZ de `B-1` y de `F-01`: sin tipar, nada impide que vuelva a entrar un método donde va una capacidad |
| `F-04` | `grado_inicial: alta` en el escenario, conservando `grado: media`, y que `T75` compruebe la coincidencia con el grado del paso 5 | `entrada/05-ESCENARIOS.md` · su prueba `T75` | `ENC` con `SIS` | **F6** | no |
| `F-05` (i) | crear en `circuitos/` las instancias de handoff que faltan, empezando por las de `SIS`, `PLT` y `VER`. **El QUÉ viaja ya está declarado** en §8.0; lo que falta es el bloque | `circuitos/` | `SIS` | **F6** | no. §8.0 declara el contenido, y la composición de ruta no depende de la instancia |
| `F-06` | anclar el `cuando` de `dis-a-ver` a una estación del ciclo de calidad, y que la entrega nombre de qué pasada procede el dictamen | `circuitos/DIS-handoffs.md` | `DIS` | **F6** | no. Es ambigüedad, no contradicción: el gate de diseño no cierra hasta la segunda pasada, y bajo esa lectura los nueve ejes tienen nivel |
| `F-07` | campo declarado `autoridad: aprobada \| trabajo` en cada fichero de `docs/owner/`, comprobado por el validador que ya recorre el directorio. Hoy la distinción está sólo en prosa | `docs/owner/*` · `validadores/exclusiones.yaml` | `SIS`, con el **Owner** para el valor | **F6** | no |
| `F-08` | nota de vigencia o de sustitución que reconcilie el «NO IMPLEMENTAR SIN DISEÑO PREVIO» de `IDEAS` §15 con lo que `C6`, `C7` y §10 **ya implementan**. Un campo `autoridad:` no retira esa frase: son remedios distintos | `docs/owner/ADS-IDEAS-PENDIENTES-MULTIREPO.md` | el **Owner**: es su documento | **F5** | no |
| `F-10` | la cabecera deja de afirmar «catorce bloques, **uno por clase de expresión**»: hay catorce formas y **nueve** clases, y la aposición es falsa. La cifra 14 es correcta | `entrada/03-FORMAS.md` | `ENC` | **F6** | no |
| `F-11` | la cabecera enumera las pruebas que el fichero contiene de verdad —`T75`–`T80` y `T154`–`T157`—, no «`T75` a `T84`»: `T81`–`T85` viven en otro fichero, que existe | `entrada/05-ESCENARIOS.md` | `SIS` | **F6** | no |

### Correcciones EDITORIALES obligatorias de F5 sobre material APROBADO

> **Registrado por el GATE DEFINITIVO INDEPENDIENTE (`J-08`, MENOR; sin decisión nueva).**
> Dos restos en (b) que **no cambian ninguna norma ni ninguna composición**: son una cita
> equivocada y una numeración desordenada. **No son cambio arquitectónico y no se registran
> como presión normativa**, precisamente porque el contenido no cambia — crear una `PN` para
> esto sería inflar el censo que F5 lleva al Owner. Se registran aquí como **checklist
> verificable de F5**, que es la fase con autoridad para editar material aprobado.

| # | ruta | ubicación | texto vigente | corrección exacta | prueba posterior |
|---|---|---|---|---|---|
| `E5-1` | `docs/rediseno/b-RECORRIDO-APROBADA.md` | **L358**, en la nota «Toda devolución obliga a DSP a crear o reabrir el paquete de corrección» | «deja al item en `en espera` **(P7)**» | «deja al item en `en espera` **(P9)**» | `b`:217–218 fija `P7 → activo` con motivo «pendiente de promoción», y `b`:221–222 fija `P9 → en espera` para `esperando-*`, `devuelto` y `propuesto` con dependencias abiertas. **`devuelto` es exactamente `P9`**, y `b`:255 ya lo usa bien. La prueba: que toda cita de un predicado `Pn` en (b) case con el predicado que ese número define |
| `E5-2` | `docs/rediseno/b-RECORRIDO-APROBADA.md` | **L462–472**, lista de reglas de recomposición | la numeración va **1, 2, 5, 3, 4** | renumerar a **1, 2, 3, 4, 5** conservando el texto de cada regla **sin tocar una palabra**, y comprobando que ninguna otra sede cita esas reglas por su número | que la secuencia de una lista numerada de (b) sea estrictamente creciente. Antes de renumerar, un barrido de «regla 3 de b.» y equivalentes que confirme que ninguna referencia externa se rompe |
| `E5-3` | `docs/rediseno/b-RECORRIDO-APROBADA.md` | **L836**, la única aparición normativa de la variante | (b) escribe **`<CAP>:revisión`, con tilde**; todo el aparato de F4 —§19, `D92`, `D98`, `D103`, `D104`—, la prueba prescrita y el mensaje de error escriben **`revision`, sin tilde**, y `E-3` la lista sin tilde en el vocabulario de `F-02` | **declarar cuál es la grafía CANÓNICA** y alinear la otra sede. Si la canónica es la de (b), F6 corrige el derivado; si es la sin tilde, F5 enmienda (b). **F4 no elige: sólo registra que las dos existen y que nadie ha dicho cuál manda** | un barrido que exija UNA sola grafía para la variante en todo el corpus vigente, con las citas históricas marcadas como tales. Hermano exacto de `F-01`/`PN-14`, que sí se registró como presión sobre la misma clase de discrepancia entre fuente aprobada y derivado. Registrado por `M-09`, y **elevado a presión `PN-16` por `P-07`**: la justificación del bloque `E5` —«no hay norma presionada»— no cubría esta fila, y era el único de los cuatro restos que puede exigir que F5 enmiende (b) |
| `E5-4` | `docs/rediseno/a-ENMIENDA-E1-ENC.md` y `docs/rediseno/a-CAPACIDADES-APROBADA.md` | `E1` **L196–197**, y en (a) **L269** y **L276** | `E1.4` declara «**siete** MARCAS DE REMISIÓN `[E1]` … cinco recuentos y dos párrafos», y en (a) hay **SEIS** —L26, L89, L219, L226, L261 y L285, y una de ellas es de confirmación, no de sustitución—. **Dos recuentos de «las 14» quedan sin marcar**: L269 «Las **14** son el catálogo base» y L276. La cifra se repite en `CORRECCIONES-POST-AUDITORIA.md` L53 y L218 | reanclar la cifra de `E1.4` a lo que (a) lleva realmente, y **marcar los dos recuentos sin marca** — o declarar por qué no los lleva. **No cambia ninguna norma**: `E1.0` sustituye los recuentos con independencia de las marcas. Lo que falla es la TRAZABILIDAD, en el apartado cuya única función es darla | que el número de marcas `[E1]` que `E1.4` declara **coincida con las que (a) lleva**, derivado por barrido y no escrito. Y que ningún recuento de capacidades en (a) quede sin marca. Registrado por `N-03` |

**Qué NO se hace aquí, y por qué. Y para cuál de las cuatro filas vale ese porqué**
(`P-07`). F4 **no edita (b)** en ninguna de las cuatro: §17 la declara intacta y esta fase no
toca material aprobado. Lo que **no** vale para las cuatro es el motivo de no crear presión:

```text
E5-1 y E5-2   NO se crea `PN`, y el motivo se sostiene: **no hay norma presionada**. `P7` y
              `P9` siguen significando lo que siempre significaron, y las cinco reglas de
              recomposición dicen lo mismo en cualquier orden. Lo que hay es una cita mal
              puesta y una lista mal numerada, en un fichero que sólo F5 puede tocar

E5-4          NO se crea `PN`: lo que falla es la TRAZABILIDAD de un recuento, y `E1.0`
              sustituye los recuentos con independencia de las marcas. Registrado por `N-03`

E5-3          **SÍ se crea presión, y es `PN-16`.** Su propia fila decía «si es la sin tilde,
              **F5 enmienda (b)**» y se declaraba «hermano exacto de `F-01`/`PN-14`, que SÍ
              se registró como presión». Una fila que puede exigir enmendar material APROBADO
              **tiene norma presionada por definición**, y cubrirla con el motivo de las
              erratas dejaba fuera del Owner al único de los cuatro que le corresponde.
              **F4 sigue sin elegir la grafía**: `PN-16` registra que hay que elegir
```

---

### `DOM` y `SEG` participan DOS veces, y ningún proceso instancia la segunda

> **Registrado por el gate de cierre independiente (`I-08`, GRAVE; es `D92`).** `b.16`
> L834–836 declara que **`DOM` y `SEG` participan dos veces**: `<CAP>:condiciones ⊳ CON`
> aporta RESTRICCIONES **antes** de construir, y **`<CAP>:revision` tras `VER` REVISA LO
> CONSTRUIDO**. `a.6` **L502–503** lo dice para las dos mitades —**corregido por `M-08`**: `D92` y este párrafo citaban `L504–505`, que dice otra cosa; la frase «`DOM` y `SEG` aportan condiciones antes de construir y revisan después» está en L502–503, y `D98` ya la citaba bien. Las dos citas convivían a veintiséis líneas—. Un barrido sobre
> `kernel/operativo/` devuelve **cero instancias de `:revision`**: los diez procesos
> instancian sólo `:condiciones`. F4 compone `A8`, `M6`–`M7` y `U5b` con
> `DOM:condiciones` y `SEG:condiciones` y nada más — **y son los tres tramos que escriben en
> las fuentes del producto**. El `GATE DE COMPOSICIÓN` de §8.0 comprueba contra los
> condicionales declarados, no contra `b.16`, luego daría por completa una composición a la
> que le falta una participación que (b) exige.
>
> **NO es una decisión nueva del Owner, y no se registra como presión.** `b.16` ya lo exige
> con esas palabras: lo que falta es INSTANCIARLO en el kernel derivado, que es trabajo de F6
> exactamente como `F-01` y `F-02`. **F4 no toca `01-PROCESOS.md`**, y por eso lo que sigue
> es la edición exacta, su propietario y su prueba.

> **REFORMULADO por el GATE DEFINITIVO INDEPENDIENTE (`K-02`, GRAVE; es `D98`).** La regla
> que `D92` entregaba a F6 derivaba el conjunto con **un barrido léxico de la cadena
> `:condiciones`**. Ese barrido es correcto en su cuenta —cuatro `DOM:condiciones` y cuatro
> `SEG:condiciones`— **y no alcanza al tramo que `D92` señala como el más expuesto**:
> `proceso:DEP` hace participar a `SEG` por la OBLIGATORIA `condiciones-de-seguridad`
> (`capacidad_productora: "SEG"`, `autoridad_de_retirada: nadie`), luego la cadena
> `SEG:condiciones` **no aparece en `DEP`** y el barrido no la ve. Y `U5b` **es**
> `proceso:DEP`, uno de los tres tramos que `D92` nombra. `proceso:AUD` queda igualmente
> fuera: hace participar a `DOM` y a `SEG` con la notación **sin tipar**. La prueba prescrita
> reproducía el punto ciego: pasaría en verde sobre un árbol sin `SEG:revision` en `DEP`.
> **Y su causa es una corrección anterior:** `D75` cerró `G-1` moviendo `SEG` a obligatorias
> en `DEP`, eliminando sin verlo la cadena de la que `D92` dependería después.
>
> **La norma aprobada está escrita sobre el HECHO, no sobre la notación:** `a.6` L502–503 —
> «**`DOM` y `SEG` aportan condiciones antes de construir y revisan después**»— y `b.16`
> L834–836 lo repite. La regla se reformula en consecuencia. **El barrido léxico de
> `:condiciones` queda RETIRADO como criterio de derivación.**

> **CORREGIDO OTRA VEZ, y es `D103`. `D98` no se reescribe.** La reformulación de `D98`
> retiraba el barrido léxico en su criterio —«participación por cualquier vía»— **y lo
> reintroducía en su algoritmo**: el paso 3 marcaba una participación como condicionante
> buscando en TEXTO LIBRE expresiones como «ANTES de construir». `D103` lo retiró del
> algoritmo y corrigió una cardinalidad insatisfacible que contaba `proceso:AUD` como si
> aportara un par fijo.

> **Y CORREGIDO UNA TERCERA VEZ, y es `D104`. `D103` no se reescribe.** El GATE INDEPENDIENTE
> DE COBERTURA Y CIERRE demostró que `D103` seguía fallando por **cuatro defectos
> concurrentes**, y que la corrección alcanzaba, otra vez, a la mitad de los sitios:
>
> - **`O-01`.** El criterio nombra **cuatro** vías y el algoritmo derivaba **dos**: la
>   **participación PROPIETARIA no estaba implementada en ningún nivel**. Demostrado con
>   fixture: un `propietario_global: "DOM"` en `proceso:SIS` pasaba en verde sin emitir par.
> - **`M-01`.** La **participación CONDICIONAL se perdía en `proceso:AUD`**, que declara `DOM`
>   y `SEG` como condicionales —`b.16` L895 lo confirma en material APROBADO— y que `D98`
>   había nombrado expresamente como hueco a cerrar. El nivel A lo excluía entero; el nivel B
>   sólo miraba el propietario del item. **Ningún nivel las evaluaba.**
> - **`N-02`.** El nivel A se declaraba derivado «de campos ESTRUCTURADOS» y uno de los tres
>   —`propietario_global`— es `{tipo: texto}` en `esquemas/proceso.yaml` L23, y en **tres de
>   los diez procesos** contiene una frase. **El barrido léxico no se había retirado: había
>   migrado de `capa_exigida` a `propietario_global`**, y la partición entre los dos niveles
>   se decidía buscando la palabra «DERIVADO».
> - **`N-01`.** El nivel B exigía la revisión «posterior a `VER`» en `proceso:AUD`, que
>   **junto a `proceso:INV` es uno de los dos únicos que NO declaran `VER`**; y excluía
>   `proceso:DIR` —que **sí** tiene `VER` y **también** deriva su propietario— con una
>   afirmación no derivable. **Los dos tratamientos estaban invertidos respecto del ancla que
>   la norma usa.**
>
> **`D104` sustituye el algoritmo entero.** Deriva sobre campos estructurados y sobre
> pertenencia a conjuntos, **sin buscar una sola palabra en texto libre**, cubre las cuatro
> vías, y define un ancla de posición aplicable a cualquier ruta real. La cifra estática **no
> se escribe: se deriva, y sigue dando el mismo conjunto que antes de la corrección** — que
> es la comprobación de que la corrección no rompió lo que ya funcionaba. **La cifra se
> publica UNA sola vez, en `SALIDA ESPERADA`, y `G-15` comprueba que sea única**: una segunda
> proyección en el mismo bloque es el contraejemplo de `M-04`, y la comprobación la suspende.

```text
LAS CUATRO VÍAS,     una participación de `DOM` o `SEG` en un proceso existe por UNA de estas
TIPADAS Y            cuatro vías, y **las cuatro cuentan**. La vía se determina por el CAMPO
EXHAUSTIVAS          en que aparece y por la FORMA del valor, nunca por su prosa:

  1 · PROPIETARIA    `propietario_global` resuelve a `DOM` o a `SEG`
  2 · OBLIGATORIA    `obligatorias[].capacidad_productora` resuelve a `DOM` o a `SEG`
  3 · CONDICIONAL    `condicionales[].capacidad` es la capacidad BASE DESNUDA: `DOM`, `SEG`
  4 · ITEM PROPIO    `condicionales[].capacidad` u `obligatorias[].capacidad_productora` es
      ENLAZADO       una REFERENCIA TIPADA `<CAP>:<aspecto>` o `<CAP>/<metodo>` cuya base
      TIPADO         resuelve a `DOM` o a `SEG` — hoy, `DOM:condiciones` y `SEG:condiciones`

NORMALIZACIÓN        la capacidad BASE de un valor es el segmento anterior al primer `:` y al
—Y ES TODA LA        primer `/`, con los espacios recortados. Sobre esa base se aplica **una
INFERENCIA QUE       sola prueba: pertenencia al conjunto de las QUINCE**, derivado de los
HAY**                directorios de `kernel/operativo/capacidades/`. **No se analiza ninguna
                     otra cosa.** `capa_exigida`, `condicion`, `criterio_de_satisfaccion` y
                     `autoridad_de_retirada` **NO se leen**

EL DISCRIMINANTE     un proceso tiene **PROPIETARIO ESTÁTICO** si y sólo si su
ESTÁTICO/DINÁMICO,   `propietario_global`, recortado, **es exactamente uno de los QUINCE
Y ES ESTRUCTURAL     identificadores** —igualdad de cadena contra un conjunto derivado del
                     árbol, no búsqueda de subcadena—. En cualquier otro caso es
                     **DERIVADO POR ITEM**. No se busca la palabra «DERIVADO» ni ninguna otra:
                     un propietario que no es un identificador es, por construcción, una
                     expresión que sólo se resuelve con el encargo delante.
                     Derivado hoy: ESTÁTICOS `FEA` `GAP` `INC` `INV` `DEU` `DEP` `SIS`
                                   POR ITEM  `DEF` `AUD` `DIR`
                     **`DEF` y `DIR` entran por la misma regla que `AUD`, sin excepción
                     escrita para ninguno.** Ésa es la razón derivable que `N-01` pedía

EL ANCLA DE          la revisión se coloca **después de la participación obligatoria de `VER`
POSICIÓN, APLICABLE  si el proceso la declara; y si NO la declara, después de su ÚLTIMA
A CUALQUIER RUTA     participación obligatoria**. Dos ramas, las dos derivables del propio
REAL                 bloque, y ninguna presupone que `VER` exista.
                     Derivado hoy: `FEA` `GAP` `DEF` `INC` `DEU` `DEP` `DIR` `SIS` → tras `VER`
                                   `AUD` → tras su ÚNICA obligatoria, `conclusion-fundada`,
                                           **que produce la capacidad `INV`**
                                   `INV` → tras su ÚNICA obligatoria, `evidencia-producida`,
                                           **que produce también `INV`**
                     **Corregido por `Q-11`**: esta sede decía «`INV` `AUD` → tras su única
                     obligatoria, `conclusion-fundada` de `INV`», y atribuía a los dos
                     procesos el MISMO item. `conclusion-fundada` es la obligatoria de `AUD`;
                     la de `INV` es `evidencia-producida`. Los dos anclan en la capacidad
                     `INV` y **en items distintos**, y `G-15` contrasta hoy el ancla publicada
                     contra la derivada, proceso a proceso.
                     **Ya no se exige `VER` donde no hay `VER`.** Que `AUD` carezca de `VER`
                     es un hecho de `b.16` registrado como `PN-8`, y esta regla lo respeta en
                     vez de tropezar con él: **la revisión de `AUD` va tras la conclusión que
                     `INV` produce, que es lo que hay que revisar en ese proceso**
```

```text
DATOS DE ENTRADA     `kernel/operativo/recorrido/01-PROCESOS.md`, sus bloques
DEL DERIVADO         ```yaml ads:proceso```: los campos `propietario_global`,
                     `obligatorias[].capacidad_productora`, `obligatorias[].id` —para el orden
                     del ancla— y `condicionales[].capacidad`.
                     Y el conjunto de las QUINCE, derivado de los directorios de
                     `kernel/operativo/capacidades/`.
                     **Y NADA MÁS.** Ninguna lista escrita a mano, ningún campo de prosa

ALGORITMO DE         1 · derivar el conjunto de las QUINCE de los directorios
DERIVACIÓN           2 · parsear los bloques `ads:proceso`
                     3 · por proceso, clasificar el propietario: ESTÁTICO si
                         `propietario_global` ∈ QUINCE por igualdad; si no, POR ITEM
                     4 · por proceso, derivar el ANCLA: la obligatoria de `VER` si existe;
                         si no, la última obligatoria declarada
                     5 · **CATÁLOGO ESTÁTICO** — para cada proceso de propietario ESTÁTICO,
                         emitir un par `(proceso, capacidad, vía)` por cada participación de
                         `DOM` o `SEG` hallada por las vías 1, 2, 3 y 4
                     6 · **REGLA POR ITEM** — para cada proceso de propietario POR ITEM, NO
                         emitir par estático. Emitir la regla que se evalúa con el item
                         delante, definida abajo
                     7 · para cada par exigido, EXIGIR la participación `<CAP>:revision`
                         posterior al ANCLA del paso 4
                     8 · HEREDAR de la participación de origen: activación, obligatoriedad y
                         `autoridad_de_retirada`

LA REGLA POR ITEM,   con el item delante se resuelven **DOS** cosas, y las dos suman:
Y CÓMO INTERVIENEN     a · el PROPIETARIO EFECTIVO del item (vía 1). Si resuelve a `DOM` o a
LOS CONDICIONALES        `SEG`, ese par se exige
                       b · los CONDICIONALES DE `DOM` Y `SEG` que el item ACTIVA (vías 3 y 4).
                         Cada condicional activado exige su par
                     **EL CONJUNTO EXIGIDO ES LA UNIÓN DE LOS DOS.**
                     Para `proceso:AUD`, que declara `DOM` y `SEG` como condicionales
                     desnudos con `C-DOM` y `C-SEG`: un item puede exigir `∅`, `{DOM}`,
                     `{SEG}` **o `{DOM, SEG}`**, según su propietario y qué condicionales
                     active. **`D103` decía «cero o un par, NUNCA los dos»: eso era cierto
                     mirando sólo el propietario, y deja de serlo al contar los
                     condicionales que `b.16` L895 declara.** Es la corrección de `M-01`,
                     y es `D104`
                     Para `proceso:DIR`, cuyos condicionales no incluyen `DOM` ni `SEG`: sólo
                     puede exigir par por la vía 1, si su propietario efectivo resuelve a una
                     de las dos. **No «pasa vacío» por declaración: pasa vacío o no según su
                     item, y eso se deriva.**
                     Para `proceso:DEF`, cuyo propietario resuelve por texto a `ARQ` o `CON` y
                     cuyos condicionales no incluyen `DOM` ni `SEG`: **hoy nunca exige par**,
                     y eso también se deriva en vez de declararse

SALIDA ESPERADA      **DOS salidas, y NO se suman en un total** (`D104`):
                       A · el conjunto ESTÁTICO del catálogo, con la vía de cada par y su
                           ancla, y para cada uno si está PRESENTE o AUSENTE. **La cifra se
                           deriva y no se escribe aquí**; ejecutada hoy sobre el árbol da
                           **CINCO procesos y NUEVE pares, los NUEVE AUSENTES** —hay cero
                           instancias de `:revision` en todo `kernel/operativo/`—, con
                           `(DEP, SEG)` por la vía 2 y los otros ocho por la vía 4

                           **REPARTO POR VÍA, y `G-15` lo contrasta vía a vía** (`Q-03`):
                           **vía 1 · 0 pares · vía 2 · 1 par · vía 3 · 0 pares · vía 4 ·
                           8 pares**. Un total de nueve admite repartos que significan cosas
                           distintas —mover los condicionales de `FEA` de la forma tipada a
                           la desnuda deja el nueve intacto y cambia el contrato—, luego
                           **publicar sólo el total no basta**

                           **EL CONJUNTO VIGILADO SE DERIVA, y no se escribe** (`Q-09`):
                           son las capacidades cuya FICHA declara la doble participación de
                           `b.16` — hoy `DOM` y `SEG`, cada una en su propio
                           `CAPACIDAD.md`. Si `b.16` se la diera a una tercera o se la
                           quitara a una de las dos, el catálogo se movería solo; una lista
                           escrita aquí seguiría en verde sobre un catálogo que ya no es el
                           suyo. `G-15` contrasta el conjunto que usa contra lo que declaran
                           las quince fichas

                           **LA VÍA Y LA PROCEDENCIA DE CADA PAR SON DERIVABLES, y las dos
                           se conservan** (`Q-10`): la vía dice CÓMO se declaró la
                           participación —1, 2, 3 o 4— y la procedencia dice DE DÓNDE
                           —propietaria, `obligatorias` o `condicionales`—. **No son lo
                           mismo desde que la vía 4 puede venir de las dos secciones**: una
                           participación de `obligatorias` se exige SIEMPRE, también tipada;
                           una de `condicionales`, sólo con su condición activa

                           **REPARTO POR PROCEDENCIA, PUBLICADO — y `G-15` lo contrasta
                           procedencia a procedencia** (`Q-28`): **propietaria · 0 pares ·
                           `obligatorias` · 1 par —`(DEP, SEG)`— · `condicionales` · 8
                           pares**. **Se conservaba en la derivación y no se publicaba en
                           ninguna sede**, con lo que era el único de los tres desgloses que
                           **no se contrastaba contra nada**: `G-15` publicaba el reparto por
                           VÍA y nadie el de procedencia. Es exactamente el defecto que
                           `M-04` describe —una magnitud derivada sin proyección única contra
                           la que compararse—, y por eso esta sede la publica **una sola vez**,
                           aquí, como las otras dos. **La cifra se DERIVA; si el árbol se
                           mueve, se mueve con él, y `G-15` falla si esta proyección no es la
                           suya**

                           **ANCLA DERIVADA HOY, proceso a proceso** —y `G-15` la contrasta
                           contra el catálogo, que es lo que `Q-11` pidió—:
                           `AUD → INV` · `DEF → VER` · `DEP → VER` · `DEU → VER` ·
                           `DIR → VER` · `FEA → VER` · `GAP → VER` · `INC → VER` ·
                           `INV → INV` · `SIS → VER`
                       B · por cada item de un proceso de propietario POR ITEM, el conjunto
                           exigido por la unión de propietario efectivo y condicionales
                           activados. **No se agrega al total de A**

CASOS POSITIVOS      VÍA 1 · un proceso con `propietario_global: "DOM"` exige `DOM:revision`
                     VÍA 2 · `DEP` con `SEG:revision` obligatoria e irretirable tras `VER`
                     VÍA 3 · item `AUD` que activa `C-DOM` exige `DOM:revision` tras
                             `conclusion-fundada`
                     VÍA 4 · `DEU` con `DOM:revision` y `SEG:revision` condicionales tras `VER`
                     `AUD` propietario `DOM` sin condicionales activos → `{DOM}`
                     `AUD` propietario `SEG` sin condicionales activos → `{SEG}`
                     `AUD` propietario `PRD` con `C-DOM` y `C-SEG` activos → **`{DOM, SEG}`**
                     `AUD` propietario `PRD` sin condicionales activos → **`∅`**
                     `DIR` propietario `DOM` → `{DOM}` · `DIR` propietario `ARQ` → `∅`
                     `INV` `SIS` `DEF` sin participación de `DOM` ni `SEG` → PASAN VACÍOS

CONTRAEJEMPLOS       · una participación PROPIETARIA de `DOM` o `SEG` que no emita par → FALLA.
                       **Es el contraejemplo de `O-01`, y hoy la comprobación lo suspende**
                     · `DEP` sin `SEG:revision`, con `SEG` sólo en `obligatorias` → FALLA
                     · un item `AUD` con `C-DOM` activo y sin `DOM:revision` → FALLA.
                       **Es el contraejemplo de `M-01`**
                     · exigir a un item `AUD` la revisión «tras `VER`» → FALLA: `AUD` no
                       declara `VER`, y el ancla correcta es su última obligatoria (`N-01`)
                     · declarar que `DIR` pasa vacío SIN resolver su item → FALLA (`N-01`)
                     · clasificar un proceso como estático o dinámico por una palabra de su
                       `propietario_global` → FALLA: el discriminante es la pertenencia al
                       conjunto de las quince (`N-02`)
                     · una proyección que publique un total fijo distinto del derivado → FALLA
                     · una segunda proyección contradictoria en el mismo bloque → FALLA
                     · un proceso con `<CAP>:revision` colocado ANTES de su ancla → FALLA
                     · un proceso con `SEG:revision` RETIRABLE en `DEP` → FALLA

ERROR                **`composicion-incompleta`**, con el proceso, la capacidad, **la vía por
                     la que participa —1, 2, 3 o 4—**, el NIVEL —catálogo o item—, el ANCLA
                     derivada y la participación que falta. **No es un aviso: impide el cierre
                     del gate de composición**

PRUEBA QUE FALLARÍA  sobre el árbol de HOY, la prueba tiene que devolver **FALLIDA nombrando
SI FALTA `SEG` EN    `proceso:DEP` → `SEG:revision` AUSENTE**, y tiene que seguir fallando si
`DEP`                alguien añade `SEG:revision` a los otros cuatro procesos del catálogo y
                     no a `DEP`. Una prueba que hoy pase en verde está mal construida por
                     definición

QUÉ TIENE QUE        un fixture por VÍA, uno por cada combinación de un proceso de
DEMOSTRAR LA         propietario POR ITEM, y uno por cada modo de fallo cerrado, **y `G-15`
COMPROBACIÓN         los ejecuta en cada corrida**: propietaria · obligatoria desnuda ·
                     condicional desnuda · item enlazado tipado · discriminante estructural ·
                     ancla ante una referencia tipada `VER:dosier` · prosa con aspecto de
                     campo · obligatoria tipada de vía 4 · `AUD` con sus cinco casos · `DIR`
                     con propietario vigilado y con propietario ajeno · negativo de `DEP` ·
                     conjunto vigilado derivado de las fichas.
                     **CENSO DE FIXTURES, contrastado contra los que se ejecutan y no
                     escrito a mano: 20 fixtures** (`Q-12`, y `Q-10` lo subió a veinte al
                     retirar el fixture tautológico y poner tres reales en su lugar). La sede
                     decía «cinco» junto a una enumeración de seis grupos, con tres procesos
                     dinámicos en el árbol: la cifra no describía nada de lo que la batería
                     corre. Ahora `G-15` **cuenta los fixtures que ejecuta y falla si esta
                     cifra no es la suya**, nombrando sede, responsable y remedio. Esta cifra
                     vive aquí porque un documento no puede contarlos, pero **no puede
                     caducar en silencio**: la única forma de que envejezca es en ROJO

DÓNDE, EXACTAMENTE   `kernel/operativo/recorrido/01-PROCESOS.md`. Y en
                     `kernel/operativo/circuitos/`, la instancia de handoff que materializa
                     la entrega de vuelta

PROPIETARIO          `SIS`, que es quien posee `recorrido/` y `circuitos/` por el mapa de
                     fuente única del índice operativo

FASE                 **F6.** `D104` fija las cuatro vías, la normalización, el discriminante
                     estructural, el ancla de posición, el algoritmo paso a paso, la regla
                     por item, las dos salidas, los casos, los contraejemplos y el error.
                     **F6 MATERIALIZA; no elige la forma.**
                     **Y esto NO se autocertifica.** La premisa se rompió con `K-02`, volvió a
                     romperse con `D98`, volvió a romperse con `D103`, y `D104` es el cuarto
                     intento. **Que esta vez alcance sólo lo puede decir un gate independiente
                     que no sea quien lo escribió.** Aquí queda APLICADO, no certificado

Y EL GATE DE         el `GATE DE COMPOSICIÓN` de §8.0 pasa a comprobar contra `b.16` **por
COMPOSICIÓN          participación efectiva en cualquiera de las cuatro vías**, no contra los
                     condicionales declarados ni contra la cadena `:condiciones`

QUÉ NO SE HACE AQUÍ  F4 **no edita `01-PROCESOS.md`**: tocarlo es F6, y esta fase no toca
                     kernel. Lo que se cierra aquí es que la ausencia quede REGISTRADA con
                     propietario, fase, edición exacta, algoritmo y prueba, en vez de
                     descubrirse cuando F6 componga `A8`, `M6`–`M7` o `U5b` sin la revisión
```

### Los censos escritos a mano, derivados — el contrato F6 que cierra nueve hallazgos

> **Registrado por el GATE DEFINITIVO INDEPENDIENTE (`J-05` + `J-06` + `K-07`, y es `D102`).**
> Los tres revisores, sin verse, aislaron la MISMA causa raíz desde mitades opuestas del
> corpus, y `L` la cuantificó: **`A6`, `A10`, `M-1`, `m-1`, `F-10`, `E-10`, `K-01`, `K-03`,
> `K-04`, `K-10`, `J-07` y `L-01` son la misma clase** — cifras y censos escritos a mano cuya
> cobertura no deriva de nada. El corpus **ya sabe cómo se arregla**: `comprobar_fuentes.py`
> lo escribe con estas palabras — «nunca una lista escrita a mano, que es lo que envejece» —
> **y no se lo había aplicado a sí mismo**. Es, según `L`, la corrección más barata del
> entregable. **Aquí NO se implementa nada: se deja el contrato completo.**

```text
QUÉ FALLA HOY, Y     · `comprobar_recuentos.py` L107–156: `AFIRMACIONES` es un CENSO ESCRITO
DÓNDE, VERIFICADO      A MANO de dónde vive cada cifra. Cubre `C1` y NO cubre
                       `contratos/00-INDICE.md`:7 ni `pruebas/T086-T092-contratos.md`:14, que
                       siguen diciendo «veintiocho campos» donde `esquemas/rol.yaml` tiene
                       **29** y `C1`:37 ya dice «veintinueve». **`T151` sale SUPERADA** con
                       dos sedes vigentes afirmando lo que el corpus desmiente
                     · `comprobar_versiones.py` L87: `T152` recorre **sólo `README.md` y
                       `START_HERE.md`**. Por eso pasa en verde mientras
                       `kernel/operativo/00-INDICE.md`:132,134 declara `KERNEL.md` «1.3.0»
                       y `KERNEL.md`:4 dice **1.5.0**

--- CONTRATO 1 · DERIVAR EL CENSO `AFIRMACIONES` ---

ENTRADAS             el árbol de ficheros versionados, y **para cada cifra publicada, la
                     FUENTE de la que deriva** declarada como una regla `(patrón de sede,
                     derivación)` — no una lista de rutas. Ejemplos de derivación:
                     «obligatorios de `esquemas/rol.yaml`» · «cabeceras `## \`PN-` de §16
                     menos las RETIRADAS y FUSIONADAS» · «filas `| \`X<nn>\` |` de §2.6.7»

ALGORITMO            1 · barrer TODO el corpus buscando afirmaciones numéricas sobre objetos
                         censables, en dígitos **y en letra** —«veintiocho», «DOCE»—
                     2 · para cada una, resolver su derivación y calcular el valor real
                     3 · comparar, y reportar cada divergencia con ruta, línea, valor escrito
                         y valor derivado
                     **La cobertura de sedes NO se enumera: se descubre barriendo.** Una sede
                     nueva queda cubierta el día que nace, sin tocar el validador

SALIDA               lista de `(ruta, línea, cifra escrita, cifra derivada)` divergentes.
                     Vacía = `T151` SUPERADA

PROPIETARIO          `PLT`, que posee el tooling de validación

FASE                 **F6**

CONDICIÓN DE CIERRE  que `AFIRMACIONES` **deje de existir como lista literal** y que la
                     cobertura del validador sea derivada. Mientras exista la lista, la
                     condición NO está cerrada, aunque `T151` salga verde

PRUEBA POSITIVA      sobre el árbol de hoy, el validador tiene que **FALLAR** nombrando
                     `contratos/00-INDICE.md`:7 y `pruebas/T086-T092-contratos.md`:14 con
                     «escrito 28 · derivado 29». Un validador que hoy pase en verde está mal
                     construido

PRUEBA NEGATIVA      introducir en un fichero NUEVO —que ninguna lista podría contener— una
                     afirmación falsa sobre un objeto censable, y comprobar que la detecta
                     **sin haber tocado el validador**. Es la prueba de que la cobertura
                     deriva y no se enumera

--- CONTRATO 1bis · LOS PERFILES DE AGENTE, QUE NADIE CENSA (`N-04`) ---

REANCLAJE, AQUÍ     `kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md` declara
Y EN SEDE VIGENTE   **VEINTIÚN** bloques `ads:perfil-agente`. Derivado por conteo sobre el
                    fichero —`grep -c '^id: perfil:'`— hoy y sobre `7c7856c`, que es el árbol
                    sobre el que se escribió el documento 17.
                    **El documento 17 publica DOS cifras distintas para el mismo objeto**: su
                    tabla del revisor `D` dice **22** y la del revisor `E` dice **21**, y su
                    adjudicador declaró el requisito `0.1` SATISFECHO sin detectarlo. **El
                    documento 17 es HISTÓRICO e INMUTABLE y no se corrige**: lo que se
                    reancla es la cifra VIGENTE, y queda aquí. **Son 21.**

POR QUÉ NADIE LO    `RECUENTOS-generado.md` **no cuenta los perfiles de agente**, pese a
DETECTÓ             contar roles, métodos, prompts, composiciones, gates, rúbricas, vetos,
                    formas, niveles de novedad y clases de entrada — todos ellos bloques
                    tipados como éste. Ninguna comprobación mecánica podía cazarlo

ENTRADA · ALGORITMO los bloques ```yaml ads:perfil-agente``` de `C2`, contados por barrido.
· SALIDA            Salida: la cifra, publicada en `RECUENTOS-generado.md` junto a las demás

PROPIETARIO `PLT` · FASE **F6** · **encaja dentro de `C-L.10`**, y su coste es una línea:
`perfiles_de_agente: n("perfil-agente")`

CONDICIÓN DE CIERRE que la cifra deje de existir sólo en prosa. **Prueba**: introducir un
                    perfil nuevo en `C2` y comprobar que el recuento se mueve solo

--- CONTRATO 2 · AMPLIAR `T152` A TODA SEDE QUE PUBLIQUE VERSIÓN ---

ENTRADAS             **toda sede que publique una versión**, descubierta por barrido: hoy,
                     como mínimo, `README.md`, `START_HERE.md`,
                     `kernel/operativo/00-INDICE.md`, los títulos de `a.11`, `O2`, `PN-3` y
                     `kernel/VERSIONES.md`. **La lista anterior es un EJEMPLO de lo que el
                     barrido encuentra hoy, no la definición del alcance**

ALGORITMO            1 · barrer el corpus buscando patrones de versión —`X.Y.Z`— y el objeto
                         del que se predican
                     2 · resolver la versión vigente de ese objeto en `kernel/VERSIONES.md`,
                         que es su sede única (regla 5: prohibido declarar versiones fuera de
                         su tabla)
                     3 · comparar y reportar

SALIDA               lista de sedes cuya versión publicada NO casa con `VERSIONES.md`

PROPIETARIO          `PLT`.   FASE **F6**

REMEDIOS DISTINTOS   no todas las sedes se corrigen igual, y el validador lo REPORTA sin
POR SEDE             decidirlo: `kernel/operativo/00-INDICE.md` es F6 · el título de `a.11`
                     es **material APROBADO, luego F5** · `O2` pide **nota, no reescritura**,
                     porque es resolución del Owner

CONDICIÓN DE CIERRE  que ninguna sede VIVA publique una versión o un recuento obsoleto, y que
                     el alcance de `T152` sea derivado

PRUEBA POSITIVA      hoy tiene que FALLAR nombrando `kernel/operativo/00-INDICE.md`:132,134
                     con «escrito 1.3.0 · vigente 1.5.0»

PRUEBA NEGATIVA      crear una sede nueva con una versión falsa y comprobar que la detecta sin
                     modificar el validador

--- CONTRATO 3 · LA GUARDIA DE VERSIÓN DE INTÉRPRETE (`J-11`) ---

> **Y se dice sin rodeos:** evidencia en verde generada bajo Python 3.11 **NO demuestra que
> el runner sea ejecutable bajo 3.10**. Bajo 3.10.12, `registrar_evidencia.py` da **10/13 con
> exit 1**, `T148` y `T159` salen FALLIDAS y la suite de workspace falla — causa única,
> `tomllib` no existe antes de 3.11. Y los tres validadores que fallan **dejan intacta la
> evidencia anterior**, por lo que `comprobar_evidencia.py` (`T158`) sale **SUPERADA en un
> entorno donde nada se reprodujo**. Eso es lo que la guardia impide.

ENTRADAS             `sys.version_info` y el `python_requires` declarado del tooling

UBICACIÓN            el **punto de entrada del runner**, `registrar_evidencia.py`, ANTES de
                     invocar ningún validador; y el mismo prólogo en los tres validadores que
                     importan `tomllib`, para que ejecutarlos sueltos no eluda la guardia

MENSAJE              nombrar la versión exigida, la encontrada y la causa:
                     `ADS exige Python >= 3.11 (tomllib). Encontrado 3.10.12. La evidencia NO
                     se regenera y la anterior NO se da por válida.`

EXIT CODE            **2** — reservado a «no se pudo ejecutar», distinto del **1** de «se
                     ejecutó y falló». La distinción importa: hoy los dos casos son
                     indistinguibles desde fuera

PRUEBAS              positiva: bajo 3.11+, la guardia no dispara y el runner da 13/13
                     negativa: bajo 3.10, la guardia dispara con exit 2, **no se reescribe
                     ninguna evidencia**, y `T158` **NO** puede salir SUPERADA sobre evidencia
                     que no se ha regenerado en esta corrida

PROPIETARIO          `PLT`.   FASE **F6**, y ya tenía sede: es `A14`

--- CASOS DE REGRESIÓN OBLIGATORIOS DE LOS TRES CONTRATOS ---

                     Cada uno de estos defectos, YA CORREGIDO en su sede, tiene que volver a
                     ser DETECTADO por el validador derivado si alguien lo reintroduce:
                       `J-05`  «veintiocho campos» con 29 obligatorios en `rol.yaml`
                       `J-06`  `00-INDICE.md` diciendo `KERNEL.md` 1.3.0 siendo 1.5.0
                       `J-07`  «cuarenta y dos» filas adversariales habiendo 46
                       `K-01`  el checkpoint diciendo DIEZ presiones habiendo trece
                       `K-04`  «los externos son OCHO» con siete en la matriz
                       `K-07`  `a.11`, `O2` y `PN-3` anclados a una versión que no existe
                       `K-10`  §17 presentando como condicional lo que `D91` deriva
                       `K-11`  un censo de sedes que omite una sede viva
                     **Ocho casos, y ninguno se cierra escribiéndolo en una lista: se cierran
                     haciendo que la cobertura del validador derive.**

QUÉ NO SE HACE AQUÍ  **F4 no implementa ninguno de los tres.** No se toca
                     `comprobar_recuentos.py`, ni `comprobar_versiones.py`, ni
                     `registrar_evidencia.py`. Lo que se cierra aquí es el contrato: entradas,
                     algoritmo, salida, propietario, fase, condición de cierre y sus pruebas
                     positiva y negativa
```

**Y dos más, que no son defectos de F4 y se dicen para que nadie los busque aquí:**

```text
`A14`   `python_requires ≥ 3.11` declarado en el tooling y comprobado ANTES de correr, para
        que `T148`/`T159` no suban a la capa de certificación como defecto del producto. Es
        una LIMITACIÓN ACEPTADA con procedencia aprobada —la arquitectura multirrepo la
        declara—, no un defecto de esta fase. Propietario `PLT`, fase **F6**

`F-12`  las cifras derivadas del propio GATE: su tabla tiene 32 hallazgos adjudicados y 16
        medios, y su prosa dice 29 y 13; su §7 dice «dieciocho fuentes» y su requisito 0.1
        enumera diecinueve. **Los documentos 15, 16 y 17 son HISTÓRICOS e INMUTABLES y no se
        corrigen**: lo que se reancla son sus PROYECCIONES VIGENTES, en el índice de
        `docs/evolucion/` y en el checkpoint. Propietario: esta tanda. **Hecho**

`m-3`   `calidad/observabilidad` se asigna sólo a `ENT` y la misión de `PLT` la nombra. **El
        hecho está confirmado; el juicio NO se asume**: convertirlo en defecto es una
        preferencia de diseño, y el adjudicador tampoco la tomó. Registrado en §5.2, sin
        remedio exigible
```

**La distancia que queda**, dicha como la dijo el baseline: ADS sigue siendo un corpus
verificado contra sí mismo y **cero veces contra la realidad**. Esta arquitectura dice cómo
cerrar esa distancia. No la cierra.

---

## `C-L.5` · La condición de COBERTURA del próximo gate — **CERTIFICADA por el documento 21**, y vigente para todo gate posterior

> **Registrada por el GATE DEFINITIVO INDEPENDIENTE (`C-L.5`, una de las cinco que bloquean
> el paso a F5).** El gate definitivo dio `INSUFICIENTE PARA F5` por **seis razones
> independientes**, y la primera fue la cobertura: **~8 700 líneas de fuentes centrales
> obligatorias que NINGÚN revisor abrió**. `L` no lo trató como formalismo — sondeó la región
> muerta y produjo **dos cambios de adjudicación en direcciones opuestas**: `ADS-PENDIENTES`
> §12 reforzó `K-06`, y su cabecera L3–L6 le obligó a **corregir la base externa de `K-03` y
> a retirar su propio agravamiento de `K-11`**. Las líneas que nadie abrió no eran relleno.

> **ESTADO ÚNICO, y está abajo. Corregido por `P-22` ≡ `Q-37` del documento 22.** Esta
> sección llevaba **dos estados dentro de sí misma**: su cabecera y su primer párrafo decían
> «**abierta, y no la cierra esta tanda**», y sesenta líneas después el cierre declaraba
> «**CERTIFICADA**». **El estado vigente de `C-L.5` es UNO y es el del cierre**, y la cabecera
> lo dice ahora — que es además lo que se proyecta al índice. Lo anterior queda marcado como
> histórico y **no se borra**, que es lo que `X47` exige.
>
> **`[HISTÓRICO]` — el estado que esta sección declaraba mientras se escribía, y que un gate
> POSTERIOR superó:** *«La condición de COBERTURA del próximo gate — abierta, y no la cierra
> esta tanda. **Esta tanda NO cierra `C-L.5`, y no puede cerrarla.** Aplicar las correcciones
> no es leer lo que no se leyó, y quien las aplica no puede certificar su propia cobertura.»*
> **Era verdad SOBRE LA TANDA** —la tanda no la cerró—, y dejó de describir el estado de la
> condición en cuanto el documento 21 la certificó. **Certificarla no la deroga**: el
> requisito de abajo **sigue vigente para todo gate posterior**, y eso también lo dice el
> cierre.

Queda escrita aquí como **condición permanente de todo gate siguiente**, con sus requisitos
exactos:

```text
QUIÉN                revisores NUEVOS con contexto limpio. **El autor de esa lectura tiene
                     que ser distinto de quien aplicó ESTA tanda de corrección.** Ésa es la
                     razón por la que doce tandas se han encadenado, y no se rompe sola

QUÉ HAY QUE LEER     ÍNTEGRO, no asignado:
ÍNTEGRO                · `ADS-PENDIENTES-DE-IMPLEMENTACION-Y-DISCUSION.md` COMPLETO,
                         **incluidos el BLOQUE B (§8–§12, certificación por niveles) y el
                         BLOQUE C (§13–§17, iniciativa y dosier vivo)** — las fuentes de
                         `P4`, `P9` y `P10`, que ningún revisor contrastó
                       · `16-GATE-FINAL-INDEPENDIENTE-F4C.md` COMPLETO
                       · `17-COMPLEMENTO-DE-COBERTURA-DEL-GATE-F4C.md` COMPLETO
                       · `18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md` COMPLETO

DOS MANIFIESTOS,     **corregido por `O-04`.** La regla de cierre de abajo dice «cualquier
Y NO UNO             fuente **ASIGNADA** pero NO LEÍDA impide la suficiencia», y para
                     evaluarla hace falta saber **qué se asignó** — dato que ningún dictamen
                     entregaba. Los tres revisores del gate de cobertura declararon con
                     honestidad qué leyeron y qué no, y **ninguno declaró qué se le había
                     asignado**, con lo que su propio adjudicador no pudo certificar la
                     cláusula más dura de esta condición. Desde ahora son **DOS documentos
                     separados, y los dos se PUBLICAN**:

  1 · MANIFIESTO DE   lo emite **el coordinador ANTES de repartir**, y se publica tal cual.
      ASIGNACIÓN      Por cada fuente: **ruta · líneas · SHA-256 · a qué revisor se asigna**.
                      Y el total, derivado: fuentes obligatorias, asignadas y sin asignar.
                      **Es inmutable una vez repartido**: si hace falta reasignar, se publica
                      un manifiesto nuevo con su motivo, no se edita el anterior

  1bis · DE DÓNDE     **corregido por `P-08`.** El manifiesto anterior declaró «FUENTES SIN
     SALE «FUENTE     ASIGNAR **0**» sobre un universo **ELEGIDO**, no derivado: la regla
     OBLIGATORIA»     decía «el total, derivado» y no decía **de qué sede**, con lo que el
                      cero era verdadero por construcción — se cumplía escogiendo sólo lo que
                      ya se había asignado. **Son DOS restas distintas y las dos hay que
                      publicarlas**:

                        · `OBLIGATORIO − ASIGNADO`  el universo obligatorio es la UNIÓN, sin
                          quitar nada, de: (i) las cuatro fuentes que nombra el apartado
                          «QUÉ HAY QUE LEER ÍNTEGRO» de arriba; (ii) las **catorce fuentes y
                          quince fichas** de la condición `C-0.1` del documento 18; (iii) el
                          documento 11, el registro de decisiones y el checkpoint; (iv) todo
                          dictamen de gate anterior aún no leído íntegro por nadie; y (v) el
                          objeto que el gate juzgue —batería, kernel o lo que sea— según su
                          encargo. **El manifiesto publica la REGLA y el COMANDO auditable
                          con que la materializa**, de modo que cualquiera pueda reejecutarlo
                          y obtener el mismo universo
                        · `ASIGNADO − LEÍDO`  la de siempre, y la que EXCLUYE la suficiencia

                      **Una lectura íntegra CERTIFICADA en un gate anterior sigue siendo
                      evidencia válida** y no se declara ausente: agota la parte de `C-0.1`
                      que cubrió, y el manifiesto la cita con el gate y la línea donde consta.
                      Es la resolución que el adjudicador `R` fijó al rechazar la premisa de
                      hecho de `P-08`: **`C-0.1` es condición de ESTADO DEL CORPUS —«fuentes
                      que nadie abrió»— y se agota cuando alguien independiente las abre**,
                      no una obligación de releer 31 517 líneas por pasada

  2 · MANIFIESTO DE   lo emite **cada revisor DESPUÉS de leer**, dentro de su dictamen. Por
      LECTURA         cada fuente que se le asignó: **ruta · líneas · SHA-256 recalculado por
                      él · `LEÍDO ÍNTEGRO` o los tramos exactos que NO abrió · primera y
                      última sección sustantiva · dos anclas de regiones separadas**

  CÓMO SE EVALÚA      el adjudicador cruza los dos: **asignado menos leído = pendiente**. Si
  LA REGLA DE         ese conjunto no está vacío, la suficiencia queda excluida, y ahora la
  CIERRE              exclusión **se puede comprobar** en vez de presumirse en una u otra
                      dirección. Sin los dos manifiestos, el adjudicador **debe declarar la
                      regla NO CERTIFICABLE**, que es exactamente lo que `O` hizo

DECLARACIÓN DE       cada revisor declara, contra su propio interés, **qué leyó íntegro y qué
COBERTURA REAL       no**. `J`, `K` y `L` lo hicieron y por eso el veredicto es utilizable

REGLA DE CIERRE      **cualquier fuente ASIGNADA pero NO LEÍDA impide la suficiencia**, con
                     independencia de los hallazgos. Cobertura asignada del 100 % NO es
                     cobertura leída, y `sin_cubrir.txt` vacío sólo dice que todo fichero
                     tenía un lector

EL ADJUDICADOR       **no corrige los hallazgos que encuentre.** Adjudica y devuelve. Corregir
                     en la misma pasada vuelve a hacer que quien recibe sea quien aplica
```

**Estado: CERTIFICADA por el GATE INDEPENDIENTE DE CIERRE CON MANIFIESTOS VERIFICABLES**
—documento 21—, y es la primera vez. El manifiesto previo de asignación se commiteó **solo y
antes de que existiera ningún revisor**; los tres publicaron su manifiesto de lectura; y el
adjudicador `R` recalculó las **43 filas** del manifiesto contra el árbol —43 de 43
coincidiendo en líneas y en SHA-256— y **calculó la resta en vez de presumirla**:
`asignado − leído = ∅` en `P` (20/20), en `Q` (31/31) y en él mismo (9/9). Los tres declararon
expresamente que su veredicto **NO se funda en la cobertura**.

**Que esta condición esté certificada no cierra `F4c` ni autoriza `F5`**: el mismo gate
devolvió `INSUFICIENTE PARA F5` por otras dos condiciones. Y el requisito de arriba **sigue
vigente para todo gate posterior**, con el añadido de `1bis`: lo que se corrige aquí es la
regla, no el manifiesto ya emitido, que es inmutable.
