# SECCIÓN (a) v3 — CAPACIDADES, EQUIPOS, PAQUETES Y ESTADO

Rediseño del kernel ADS. Reescritura tras las 10 correcciones del Owner sobre v2.
Estado: **pendiente de aprobación**. No pasar a la sección (b) sin ella.

---

## a.0 — Tres niveles

```text
CATÁLOGO DE CAPACIDADES     qué sabe hacer una organización ADS
(kernel · fijo · reusable)  14 capacidades. No es un recorrido.
          │  materialización — sólo donde hay trabajo real
          ▼
EQUIPOS VIVOS               capacidad + tablero + cola + memoria + agentes
(proyecto · variable)       se materializan y se retiran
          │  composición — una por cada item, según su naturaleza
          ▼
RUTAS Y PAQUETES            grafo de valor: qué capacidades se activan, en qué
(item · única)              orden, en paralelo o no, y POR QUÉ NO las demás
```

**Regla de categoría** (deroga "sombreros, no saltos"): no existe *la* cadena.
Existe un catálogo y un enrutador que compone una ruta por item. Saltarse una
capacidad no es un defecto; **no dejar escrito por qué se saltó, sí**. La traza la
escribe el enrutador una vez, no cada capacidad saltada.

---

## a.1 — Ficha de una capacidad · doce campos

```text
MISIÓN          una frase: qué falta si esto no existe
CAPA DE VALOR   qué añade al item que no traía al entrar
ENTRADA         qué acepta y en qué estado mínimo
SALIDA          qué deja escrito cuando añade su capa
GATE            lista COMPROBABLE para que un paquete cambie de estado y salga de
                su custodia. No es un juicio: es una lista. Si hiciera falta
                juicio, ese juicio es otra capacidad activada, no una aprobación
                oculta.
RESULTADOS      cuáles de los cuatro (a.2) puede emitir, y con qué autoridad
MEMORIA PROPIA  su fuente de verdad persistente
TABLERO         su vista de estado, derivada y legible sin herramienta (a.9)
MÉTODO          procedimiento interno; puede tener subcircuitos propios
CHECKPOINT      en qué punto de su método se quedó en cada paquete que tiene a
                medias, persistido para que un agente nuevo lo retome (a.10)
AUTORIDAD       qué decide sola · qué escala · sobre qué tiene veto
OWNER           en qué nivel de los tres de a.8, con qué criterio escrito
```

Sin los doce es una etiqueta y el kernel **DEBE** rechazarla.

---

## a.2 — Los cuatro resultados

Cuando una capacidad termina con un **paquete** emite exactamente uno:

| | resultado | qué es |
|---|---|---|
| 1 | **CAPA AÑADIDA** | añadió su capa. El **gate** decide si el paquete puede cambiar de estado. Capa y gate son distintos: la capa es lo producido, el gate la condición de entrega. |
| 2 | **DEVOLUCIÓN** | una capa anterior es insuficiente. Vuelve a la capacidad concreta nombrando qué falta. Sujeta a los frenos de a.7. |
| 3 | **BLOQUEO** | depende de algo que aún no existe. **DEBE** nombrar qué lo desbloquearía. |
| 4 | **CANCELACIÓN** | este paquete o item no merece seguir fabricándose: el problema se disolvió · el anclaje reveló que ya está resuelto · la relación coste/valor se invirtió · lo sustituye otro item. PRD y DSP cancelan solas items de naturaleza interna; **toda cancelación de algo que el Owner pidió explícitamente se propone y la decide él**. Siempre con motivo escrito; nunca se borra. |

**APARCADO no es un resultado.** Es ortogonal: lo declara el Owner (o DSP por
instrucción suya). Conserva custodia y todas las capas intactas.

> **REGLA DURA:** el sistema **NO DEBE** proponer desaparcar, cerrar ni "limpiar" un
> item aparcado por antigüedad. Un item puede quedar aparcado indefinidamente. Es un
> resultado normal del sistema, no una anomalía.

---

## a.3 — El catálogo · 14 capacidades

### Estaciones — toman custodia de paquetes y añaden capa

**PRD · PRODUCTO** — *intención y criterio de éxito*
Para quién, qué cambia, qué queda fuera, qué haría que esto fuera un fracaso aunque
funcione, relación con la definición de éxito del Owner (K0.13). En un GAP: aquí el
hueco pasa de "falta algo" a resultado definido con criterio de terminado — es el
procedimiento estándar de gaps que hoy no existe. Se activa sólo si el item afecta
al producto. Autoridad: alcance rutinario sola; escala alcance relevante y prioridad
estratégica. Cancela items internos.

**DIS · DISEÑO** — *forma*
Dos niveles simultáneos y ambos exigibles: funcional/experiencia (flujo, estados,
información, densidad, accesibilidad, fluidez percibida) y estética/dirección de arte
(identidad, carácter, capacidad de sorprender). Condición de entrada: consultar la
memoria de diseño. Salida obligatoria: memoria actualizada con lo decidido **y con lo
descartado y su porqué**. Métodos internos propios: **DIS/Fundación · DIS/Reconstrucción
· DIS/Evolución**. Veto sobre soluciones técnicas que degraden la forma sin agotar
alternativas.

**ARQ · ARQUITECTURA** — *encaje y plan técnico*
Cómo entra en lo que ya hay; radio de impacto **medido**, no estimado; contratos que
cambian; alternativas con coste; ADR cuando proceda; descomposición en paquetes con
orden y dependencias. También diagnóstico en rutas de defecto. Devuelve a DIS sólo
trayendo alternativas de forma, nunca sólo la negativa.

**CON · CONSTRUCCIÓN** — *la implementación y sus tests*
**No redecide capas anteriores.** Si descubre que una está mal, devuelve. Implementar
sobre una capa que sabe mal es el fallo característico de esta estación. Sin autoridad
sobre forma ni intención.

**VER · VERIFICACIÓN** — *dosier de evidencia*
No emite un sí/no: produce un artefacto que viaja hacia adelante. Revisión independiente
de quien construyó (**G13 deja de ser proporcional al riesgo y pasa a ser estructura por
defecto de esta capacidad**), tests, regresión incluida la visual, seguridad cuando
aplica, presupuestos, y evidencia juzgable por un humano: capturas, grabaciones,
comparativas, estados extremos (vacío, error, carga, mínimo, máximo). Veto sobre entrega
mientras haya evidencia en rojo. Coaprueba patrones técnicos junto a la capacidad
competente (a.8).

**ENT · ENTREGA Y OPERACIÓN** — *realidad operativa*
El cambio existe fuera del entorno de desarrollo y se ha **observado** comportarse.
Integración de ramas y paquetes, migraciones, despliegue (preview/staging/dispositivo),
smoke tests, publicación (materia reservada al Owner, G05), observación de logs y
métricas durante una ventana declarada, rollback, y confirmación de funcionamiento en
el entorno real.

> **Por qué estación y no parte de PLT:** PLT *construye y posee* la maquinaria (CI,
> entornos, observabilidad) — backlog propio, sin custodia. ENT *opera* esa maquinaria
> sobre un paquete concreto y sí toma custodia. Fundirlas mete en una sola cola el
> trabajo de infraestructura y el trabajo por item, y uno de los dos siempre pierde.

**Rollback autónomo — con límites.** ENT revierte por decisión propia, sin consultar,
si y sólo si se cumplen los cinco:

```text
[ ] existe procedimiento de reversión previamente probado
[ ] la reversión es segura en el estado actual
[ ] no destruye datos
[ ] responde a una señal roja definida de antemano
[ ] deja evento y evidencia
```

Si el rollback es **destructivo**, **irreversible**, **obliga a elegir entre pérdida de
datos e indisponibilidad**, o **no está probado**: ENT **contiene el daño y escala**. No
tiene autoridad ilimitada por llamarse rollback.

**USO · USO REAL** — *validación en condiciones reales*
No equivale a "el Owner". La evidencia de uso real puede proceder de: **el Owner · un
usuario real distinto del Owner · un operador · un dispositivo físico · telemetría ·
logs · observación de comportamiento · un plan de validación humana (G36)**. El Owner
interviene **sólo cuando el resultado requiere su autoridad o su juicio** (a.8). Cuando
la fuente es humana, hereda G36 íntegro: cola priorizada, plan único, orden por coste
de set-up, estado preparado de antemano.

**APR · APRENDIZAJE** — *criterio*
Convierte el recorrido en cambio de criterio: ledgers (G52), promoción de aprendizaje a
regla, memoria de diseño y memorias de equipo actualizadas, candidatos a UPSTREAM
(K0.12), ajuste de la composición por defecto si el recorrido reveló una ruta mal
definida, e items nuevos nacidos del uso real, que entrega a DSP.
**Resultado legítimo y frecuente: `sin aprendizaje promovible`.** APR no es una ceremonia
de cierre; una entrada forzada contamina el ledger con falsa autoridad (G52).

### Servicios — se consultan sin tomar custodia del paquete que consultan

| | capacidad | nota |
|---|---|---|
| **INV** | Investigación y evidencia | spikes contra entorno real, freshness (G22+G33). Puede declarar que una decisión **no puede tomarse todavía** |
| **DOM** | Dominio y datos | modelo, vocabulario, contratos, reversibilidad de esquemas. **Veto** sobre lo que rompa el modelo o la recuperabilidad |
| **SEG** | Seguridad y privacidad | G27 + G28 + cumplimiento declarado. **Veto duro**, no negociable |
| **PLT** | Plataforma | build, CI, entornos, tooling, observabilidad, aislamiento multiagente. Cola y backlog propios |

Un servicio **PUEDE** tomar custodia de un paquete propio cuando su trabajo es
sustantivo y duradero (un spike, una migración de contratos). En ese caso se comporta
como estación para ese paquete, checkpoint incluido.

### Sistema — trabajan sobre la fábrica

**SIS · INGENIERÍA DEL SISTEMA**
Dueña del sistema operativo: memoria persistida, **el dispatcher como software**,
plantillas, catálogo de capacidades, composiciones por defecto, prueba de conformidad
de una organización instalada (a.12), enrutamiento de modelos, rendimiento de equipos,
revisión de plantilla y regla de retirada (G52).
**Función Coherencia Documental:** valida estructura, frescura, enlaces y coherencia del
corpus. **No escribe contenido por nadie** — cuando encuentra un documento huérfano o
caduco crea un item y lo enruta a quien posee esa capa.
*Va en SIS y no en APR porque el sujeto de APR es el* criterio*, mientras que estructura,
frescura y enlaces son propiedades de los* artefactos *— misma naturaleza que plantillas,
tableros y dispatcher, y comprobación mayoritariamente automatizable.*

**DSP · DESPACHO**
Implementación **software/runtime primero** (el dispatcher), propiedad de SIS. Un
supervisor —agente o el Owner— interviene sólo en excepciones: paquete estancado,
contradicción de estado, ruta a recomponer, conflicto que el runtime no debe resolver
solo. Cuatro funciones:

- **Encuadre** — id, enunciado de una línea de lo que de verdad se pide, naturaleza, y
  **dosier de anclaje**: qué sistemas/módulos/agentes ya implementados tocan esto · qué
  decisiones previas lo gobiernan · qué aprendizajes aplican · si duplica un item abierto
  · **qué no existe todavía y se creía que sí**. Se apoya en el **índice de lo existente**,
  memoria propia de DSP.
- **Enrutamiento** — compone la ruta, crea los paquetes, asigna propietario global,
  escribe la traza (a.6).
- **Estado** — reconstruye al abrir, contrasta lo declarado contra la realidad del repo,
  resuelve inconsistencias, regenera las vistas derivadas. **Responde a "Continúa".**
- **Supervisión** — detecta estancados, aplica los frenos de a.7, escala.

Autoridad: total sobre el **orden** y la **ruta**. **Ninguna sobre el contenido de
ninguna capa.** Cancela items internos duplicados.

**DSP puede sintetizar.** Estado ejecutivo, riesgos, qué necesita atención, qué ha
cambiado, qué puede seguir solo: son salidas legítimas y necesarias. Condiciones, todas
obligatorias:

```text
[ ] toda afirmación deriva del estado persistido
[ ] enlaza los items y paquetes de los que deriva
[ ] no mantiene información que no esté en los ficheros
[ ] el Owner puede comprobarla leyendo los ficheros
[ ] NUNCA presenta una síntesis divergente como nueva fuente de verdad
```

---

## a.4 — Materialización y retirada

El kernel define **capacidades**. El proyecto materializa **equipos**.

- **Materializar** = darle tablero, cola, memoria viva y agentes declarados.
- **Señal de materialización:** el enrutador necesita activar una capacidad que no tiene
  equipo. Esa necesidad *es* el disparador. No se materializa "por si acaso".
- **Retirada:** equipo cuyo tablero no ha tenido movimiento durante dos auditorías es
  candidato a desmaterializarse (regla de retirada, G52).
  **Su memoria persiste. Las memorias no mueren; los equipos sí.**
- **DSP y SIS se materializan siempre.** Sin ellas no hay sistema operativo.

El kernel proporciona el **criterio** de materialización. **NO DEBE** decidir sin
auditoría que un proyecto concreto carece de dominio complejo, de superficie de diseño
o de cualquier otra materia: eso se determina en el encuadre del proyecto, no aquí.

---

## a.5 — Propiedad global y custodia de paquetes

v2 decía "un item está en custodia de exactamente una estación" y a la vez permitía
paralelismo. Era contradictorio. Se separan dos niveles distintos:

```text
NIVEL 1 · PROPIEDAD GLOBAL DEL ITEM
  Un único equipo responde de extremo a extremo por el avance general y por la
  integración de resultados. No es quien más trabaja: es quien responde.

NIVEL 2 · CUSTODIA DEL PAQUETE
  Cada paquete tiene exactamente un equipo responsable vigente.
  Varios paquetes del mismo item PUEDEN estar simultáneamente en equipos distintos.
```

### Propietario global

- **Regla de asignación:** es la capacidad **cuya capa define el resultado del item**.
  DSP lo asigna al encuadrar, desde la composición por defecto del tipo, y queda escrito.
- Siempre es una **estación**, nunca un servicio. Para items de tipo `SIS`, es SIS.
- **Puede cambiar** durante el recorrido, sólo por decisión de DSP y con traza (un `DEF`
  que resulta ser un `GAP` traslada la propiedad de ARQ a PRD).
- **NO DEBE** declarar el item cerrado porque su parte terminó. Cierra cuando todos los
  paquetes tienen gate cumplido o resultado declarado.
- **No tiene autoridad sobre las capas de otros.** Si dos capas son incompatibles, abre
  un desacuerdo; **no arbitra**.
- La asignación concreta por tipo de proceso se cierra en la sección (b).

### El paquete

```text
PAQUETE  <ITEM-ID>/<nn>
  capacidad responsable   una y sólo una, vigente
  objetivo                qué debe quedar hecho
  contexto mínimo         ENLACES a fuentes, nunca copias
  escribe                 qué fuentes de verdad va a modificar     ← declarado al crearse
  depende de              qué decisiones y qué otros paquetes
  nivel de calidad exigido
  capa · gate · estado · checkpoint    propios
  v                       versión, incrementa en cada escritura canónica
```

### Cómo se crean paquetes paralelos

1. DSP crea los paquetes al **componer o recomponer** la ruta.
2. Cualquier capacidad **PUEDE pedir** la creación de paquetes hijos —típicamente ARQ al
   descomponer—; DSP los crea y los ancla al grafo. La capacidad no los crea por su
   cuenta: si lo hiciera, el grafo dejaría de ser reconstruible.
3. Dos paquetes se despachan en paralelo si y sólo si **sus conjuntos `escribe` son
   disjuntos**. Si no lo son, DSP los secuencia y el segundo queda `bloqueado` con
   `desbloquea: <paquete>`. Esto instrumenta G17 en vez de dejarlo a criterio.

### Cómo vuelven los resultados y quién integra

Al cumplir su gate, el paquete deposita su capa y notifica al **propietario global**, que
integra y responde por la coherencia del conjunto.

### Qué ocurre si dos paquetes son incompatibles

| tipo de conflicto | detección | resolución |
|---|---|---|
| **De fuente** — mismos ficheros o misma fuente de verdad | al despachar, por `escribe` disjunto; si aparece en marcha, al integrar | DSP secuencia. El segundo paquete se recompone sobre el resultado del primero. Nunca merge silencioso de decisiones. |
| **De decisión** — dos capas incompatibles (DIS decidió X, DOM impone Y) | al integrar, por el propietario global | El propietario **no decide en silencio**: abre un desacuerdo con las dos posturas escritas. Si una capacidad tiene **veto** en esa materia (SEG, DOM), su veto manda y el otro paquete se recompone. Si no hay veto: escala a DSP si es problema de ruta (debieron secuenciarse), al Owner si es desacuerdo de fondo. |

> Nadie declara completado el proceso global porque terminó su parte. Los desacuerdos se
> registran y escalan según autoridad; **nunca se resuelven en silencio**.

---

## a.6 — Composición de rutas

**Gramática:** `A → B` secuencia · `A ∥ B` paralelo · `A ⇄ B` revisión cruzada ·
`A ⊳ B` A desbloquea B · `[A si X]` condicional con la condición escrita.

### Traza obligatoria — sustituye a "sombreros, no saltos"

```text
RUTA   compuesta: <fecha> por DSP · tipo: DEF · propietario global: ARQ
activadas:   ARQ(diagnóstico) → CON → VER → ENT
no activadas:
  PRD — no altera alcance ni criterio de éxito: corrige comportamiento ya
        especificado en FEA-009
  DIS — sin superficie de interfaz: el fallo es de cálculo en capa de dominio
  USO — sin fuente de uso real aplicable; la evidencia de VER basta
recomposiciones: <fecha> ARQ pidió añadir PRD — el "bug" era un gap de alcance
```

**Activar de más deja traza igual que activar de menos.** Una ruta que activa una
capacidad que no cambió nada es señal del modo de fallo (b) de a.7. Cualquier capacidad
puede pedir a DSP recomponer la ruta dejando el motivo — esto sustituye al "escalado
automático" de G34 en forma trazable.

### Composiciones — ILUSTRATIVAS, NO APROBADAS

> Sirven **sólo** para demostrar que el catálogo soporta rutas distintas entre sí.
> **No se consolidan aquí. Se cierran en la sección (b).**

```text
FEA  PRD → [DIS si hay superficie o experiencia afectada] → ARQ → CON → VER → ENT
         → [USO si hay fuente de uso real aplicable] → APR
GAP  PRD → [DIS] → ARQ → CON → VER → ENT → [USO] → APR
DEF  [ARQ si el diagnóstico no es evidente] → CON → VER → ENT → [USO] → [APR]
INC  ENT(contención) → ARQ(diagnóstico) → CON → VER → ENT → APR (obligatorio)
INV  INV → [PRD o ARQ según destino] → APR
DEU  ARQ → CON → VER → ENT → APR
DEP  SEG ∥ PLT (condiciones) ⊳ CON → VER → ENT
AUD  INV ∥ DOM ∥ SEG ∥ DIS/Reconstrucción → [PRD si hay decisión de producto] → APR
DIR  PRD ∥ DIS → ARQ(radio de impacto) → OWNER → CON → VER → ENT → USO → APR
SIS  SIS → CON → VER → ENT(activación segura del runtime) → APR
```

Correcciones pendientes de aplicar al cerrarlas en (b), ya registradas:
DIS no se activa en toda feature · USO no es obligatorio en toda feature · APR puede
emitir `sin aprendizaje promovible` · DOM y SEG aportan **condiciones antes de construir**
y revisan después, no reciben la primera noticia en paralelo con CON · ARQ no es
obligatoria para todo bug trivial · una auditoría no tiene por qué terminar en PRD · los
cambios de SIS que modifican el runtime necesitan entrega y activación segura.

---

## a.7 — Los frenos: dos modos de fallo simétricos (sustituye a K0.9)

K0.9 declaraba un único modo de fallo y con él justificaba todos los timeboxes y
presupuestos. Se sustituye por dos, ambos vigilados, ninguno subordinado al otro.

### Modo (a) — FRAGMENTACIÓN SIN SISTEMA · *el problema real hoy*

Muchos agentes, documentos y circuitos descoordinados; trabajo que duplica lo ya
implementado; memoria perdida entre sesiones; el Owner reexplicando contexto.
**Señales:** items que al anclarse resultan duplicados · la misma decisión tomada dos
veces con resultado distinto · el Owner reescribiendo cómo guiar la conversación.
**Mecanismos:** Encuadre obligatorio con dosier de anclaje · índice de lo existente ·
escritor único por fichero (a.9) · vistas derivadas legibles.

### Modo (b) — AUTORREFERENCIA SIN PRODUCTO · *el riesgo simétrico de construir esto*

El sistema dedica más esfuerzo a organizarse a sí mismo que a producir resultados.
**Señales:** rutas que activan capacidades que no cambiaron nada · devoluciones
repetidas · capacidades materializadas sin cola.

**FRENO 1 — LÍMITE DE DEVOLUCIONES = 2**

```text
2 devoluciones entre el mismo par de capacidades sobre el mismo paquete.
  1ª  información: la capa estaba incompleta
  2ª  desacuerdo:  no se han puesto de acuerdo en qué falta
  3ª  NO SE EJECUTA. El paquete no rebota otra vez.

DSP lo detiene y escala CON LAS DOS POSTURAS ENFRENTADAS ESCRITAS: qué sostiene
cada capacidad y por qué. A DSP si es problema de ruta; al Owner si es de fondo.
PROHIBIDO: una tercera revisión muda, o que una capacidad ceda en silencio.
```

**FRENO 2 — DETECCIÓN DE CICLOS MULTIPARTE**
El freno no puede evitarse porque el rebote atraviese tres equipos en vez de dos. El
runtime **DEBE** detectar ciclos de ruta repetidos con más de dos capacidades
(`DIS → ARQ → CON → DIS`, `ARQ → DOM → PRD → ARQ`) y aplicarles el mismo tratamiento:
detención y escalado con las posturas escritas.
*El algoritmo concreto no se cierra aquí; la obligación de detectarlos, sí.*

**FRENO 3 — LÍMITE DE RACHA SIS = 2**

```text
No se despachan más de 2 items de tipo SIS completados consecutivamente
SI existe al menos un item de producto listo para avanzar.
El tercero no se despacha hasta que avance al menos un item de producto.

EXCEPCIONES:
  · instrucción explícita del Owner
  · incidente del propio sistema
  · trabajo SIS que desbloquea directamente el item de producto listo

NO APLICA mientras el objetivo explícito del proyecto sea construir o migrar el
propio kernel/runtime.

OBLIGACIÓN: cada item SIS DEBE enlazar el problema real, la fricción o la
capacidad de producto que justifica su existencia.
```

*Se usa racha y no proporción porque un item puede durar cinco minutos y otro semanas:
una proporción simple de items no mide esfuerzo.*

---

## a.8 — Intervención del Owner: tres niveles con criterio escrito

| nivel | cuándo |
|---|---|
| **Obligatorio** | primera dirección de **producto** · primera instancia de un patrón **visual, artístico o de interacción** · primera decisión dentro de un **área reservada** (G05) · decisión **estratégica** o **difícilmente reversible** · **cambio de dirección** (G51) |
| **Opcional / acumulada** | el item extiende un `owner_approved_pattern` → cola de validación por lotes (G36); **no detiene el item** |
| **Ninguna** | extiende un `capability_approved_pattern` o un `provisional_pattern` vigente · mantenimiento · bugs internos · trabajo rutinario dentro de la autoridad delegada |

> **Los patrones técnicos dentro de la autoridad delegada NO requieren al Owner.** Los
> aprueba la capacidad competente junto a **VER**, dejando evidencia y ADR cuando
> corresponda. El primer uso de una migración, un refactor, una estrategia de test o un
> patrón de código **no** es materia del Owner.

### Cuatro clases de patrón

```text
owner_approved_pattern        aprobado por el Owner. Sólo en materias de su juicio:
                              producto, forma visual/artística/interacción, reservadas.
capability_approved_pattern   aprobado por la capacidad competente + VER, con evidencia
                              y ADR cuando corresponda. Patrones técnicos delegados.
provisional_pattern           vigente con condición de revisión declarada (K0.5).
                              Se usa sin ceremonia; se reabre al cumplirse la condición.
expired_or_superseded         ya no extiende nada. Un item que lo invoque vuelve al
                              tratamiento completo según materia.
```

Cada patrón declara:

```text
PATRÓN: <nombre>
Clase:      owner_approved | capability_approved | provisional | expired_or_superseded
Aprobado:   <fecha> · por <quién> · en <item/AT/ADR>
Alcance:    a qué se aplica y a qué NO
Criterios comprobables: <lista>
Caduca:     condición que lo reabre
```

### Test de "extiende un patrón aprobado"

```text
Un item extiende un patrón si y sólo si:
 (1) existe una entrada VIGENTE (no expired_or_superseded) cuyo alcance lo cubre, Y
 (2) el item cumple TODOS sus criterios comprobables, Y
 (3) no introduce ningún elemento fuera del alcance declarado.

El NIVEL DE OWNER que corresponde lo determina la CLASE del patrón, no el hecho de
extenderlo. Si falla cualquiera de las tres condiciones, el nivel se determina por
MATERIA según la tabla de arriba — no automáticamente "obligatorio".
```

Los patrones de forma viven en la memoria de diseño; los técnicos en `CONVENTIONS.md`.

---

## a.9 — Estado persistido: propiedad de campos y concurrencia

Requisito del Owner: **el estado operativo ES los ficheros del repo**, legibles
directamente, sin informe intermedio.

v2 decía "la ficha es la fuente de verdad" **y** "el tablero es una proyección editable
que DSP propaga". Entre edición y reconciliación existían dos valores posibles y no
estaba definido cuál ganaba. Eso no es fuente única. Se rediseña por **propiedad de
campos con escritor único**.

### Regla fundacional

> **Cada fichero canónico tiene exactamente un escritor.** No hay campos con dos dueños.
> Todo lo demás es derivado y regenerable.

### Disposición

```text
estado/
├─ items/<ITEM-ID>/
│  ├─ 00-encuadre.md      escritor: DSP      id · enunciado · naturaleza · dosier de anclaje
│  ├─ 01-ruta.md          escritor: DSP      ruta · traza · grafo de paquetes · propietario global
│  ├─ 02-control.md       escritor: OWNER    prioridad · aparcado · motivo · reactivador
│  ├─ 03-integracion.md   escritor: PROPIETARIO GLOBAL   estado global · capas integradas · desacuerdos
│  ├─ paq/<nn>-<CAP>.md   escritor: LA CAPACIDAD CON CUSTODIA   objetivo · escribe · depende ·
│  │                                          capa · gate · estado · checkpoint · v
│  └─ vista.md            DERIVADO por DSP   el item entero en un solo fichero legible
└─ tableros/<CAP>.md      DERIVADO por DSP   la cola de ese equipo
```

**Derivado no significa efímero.** `vista.md` y los tableros son ficheros reales,
versionados en git, legibles sin herramienta. Lo que significa es: **un solo escritor
(DSP) y regeneración determinista** — mismo estado canónico ⇒ fichero byte-idéntico. Eso
hace que los diffs de git sean informativos y que la detección de comandos sea fiable.

### Cuatro clases de campo

| clase | escritor único | dónde | ejemplos |
|---|---|---|---|
| **Canónico global del item** | DSP | `00-`, `01-` | id, enunciado, naturaleza, anclaje, ruta, traza, grafo, propietario global |
| **Canónico del paquete** | la capacidad con custodia | `paq/<nn>-<CAP>.md` | objetivo, `escribe`, `depende de`, capa, gate, estado, checkpoint, `v` |
| **Control directo del Owner** | el Owner (DSP transcribe el comando) | `02-control.md` | prioridad, aparcado + motivo + reactivador |
| **Derivado** | DSP, por regeneración determinista | `vista.md`, `tableros/` | todo el tablero, estado ejecutivo, colas |

### El tablero como canal de órdenes, no como estado editable

El tablero **no** es editable como estado. Es editable como **canal de comandos**. DSP es
su único escritor, así que **cualquier diferencia entre el fichero en disco y el que DSP
regeneraría es, por construcción, una orden del Owner**. Pipeline:

```text
1 DETECTAR   diff( tablero en disco , tablero que DSP generaría ) ≠ ∅
2 VALIDAR    ¿el campo tocado es de control del Owner (prio, aparcado)?
             NO → comando malformado. NO se aplica y NO se sobrescribe en silencio:
                  DSP anota el rechazo en 03-integracion.md y marca la fila.
3 VERSIÓN    la fila lleva `v` del paquete que proyecta. ¿Sigue siendo la actual?
             NO → CONFLICTO. DSP no elige: escribe los dos valores y deja el item
                  en `esperando-owner`.
4 EVENTO     la orden válida se convierte en evento
5 APLICAR    el evento se aplica a 02-control.md (fuente canónica)
6 REGENERAR  DSP regenera tablero y vista de forma determinista
7 ATÓMICO    escritura temp+rename. Si el mtime cambió entre lectura y escritura,
             el ciclo se repite.
```

*Dónde se persiste la secuencia de eventos se decide en la sección (g), junto con
memoria y recuperación. Aquí sólo se define el pipeline, no su almacenamiento.*

### Prueba de concurrencia — resuelta por construcción

> Dos agentes actualizan simultáneamente dos items diferentes del mismo equipo mientras
> DSP reconcilia y el Owner aparca uno. El sistema no pierde cambios ni requiere
> coordinación manual.

```text
agente A  → estado/items/FEA-021/paq/02-DIS.md     fichero distinto
agente B  → estado/items/GAP-014/paq/01-DIS.md     fichero distinto
Owner     → estado/items/GAP-014/02-control.md     fichero distinto
DSP       → estado/tableros/DIS.md                  único escritor, regeneración atómica
```

Cuatro escritores, cuatro ficheros disjuntos. **Ninguna escritura pisa a otra.** DSP
regenera después y el tablero refleja los cuatro cambios. No hace falta bloqueo ni
coordinación manual.

Los dos casos residuales, nombrados y resueltos:
1. **Dos agentes sobre el mismo paquete** — prohibido por la regla de custodia única. Si
   ocurre, es un defecto del despacho, no un conflicto a fusionar.
2. **Dos instancias de DSP** — el runtime **DEBE** garantizar un solo escritor de
   derivados (lock o proceso único). Es requisito del runtime, se implementa en (g).

### El tablero

```markdown
# TABLERO — DIS · Diseño
> DERIVADO de estado/items/. Regeneración determinista por DSP.
> Editar aquí prio o aparcado es una orden; el resto se rechaza (a.9).
> generado: 2026-08-25T19:04

| paquete | estado | prio | actúa | espera desde | necesita para avanzar | v |
|---|---|---|---|---|---|---|
| [GAP-014/01](../items/GAP-014/paq/01-DIS.md) | aparcado | normal | owner | 2026-08-19 | aparcado por: atención en FEA-021 · reactiva: "retoma el gap" | 7 |
| [FEA-021/02](../items/FEA-021/paq/02-DIS.md) | en curso | urgente | dis/critico | 2026-08-25 | 2ª dirección explorada y comparada | 3 |
| [FEA-009/04](../items/FEA-009/paq/04-DIS.md) | bloqueado | normal | inv | 2026-08-22 | bloqueo: latencia real sin medir · desbloquea: SPIKE-03 | 2 |
| [DEF-102](../items/DEF-102/paq/03-CON.md) | consulta | normal | dis | 2026-08-24 | opinión sobre estado vacío · custodia: CON | 5 |
```

Reglas de forma para que sea parseable sin ambigüedad: orden de columnas fijo · sin `|`
en el contenido (usar `·`) · vacío = `—` · fechas ISO · prefijo tipado en `necesita`:
`bloqueo: … · desbloquea: …` / `aparcado por: … · reactiva: …` / `custodia: <CAP>` / sin
prefijo = lo que falta para cerrar la capa. Lo que no quepa en una línea vive en el
paquete.

### Estados y prioridad

```text
propuesto · en curso · consulta · esperando-owner · bloqueado · aparcado ·
devuelto · cancelado · cerrado

BLOQUEADO  no puede avanzar: depende de algo que aún no existe
APARCADO   SÍ podría avanzar; el Owner ha decidido centrar la atención en otra cosa.
           Decisión de prioridad, no imposibilidad. Conserva custodia y capas.

Un item aparcado o bloqueado NO consume capacidad ni frena a ningún otro.
Transiciones completas → sección (b).
```

```text
PRIORIDAD  urgente · normal · fondo          por defecto: normal
`normal` significa "avanza a su ritmo", NO "cuanto antes".
REGLA DURA: el sistema NO DEBE marcar `urgente` por su cuenta. Sólo el Owner.
Se cambia en lenguaje natural o editando el tablero (pipeline de arriba).
```

### Concurrencia: es el modo normal

Paquetes en custodia de equipos distintos avanzan de forma independiente por defecto.
Sólo se serializa cuando sus conjuntos `escribe` se solapan o hay dependencia declarada
(a.5). Lanzar un gap y después un feature debe dejar ambos progresando.

---

## a.10 — CHECKPOINT

El tablero resuelve **dónde** está un paquete. No resuelve **en qué punto del método
interno** se quedó el equipo con él.

> **CHECKPOINT ≠ APARCADO.** Aparcado es prioridad. Checkpoint es posición dentro del
> método propio del equipo — existe igual si el paquete está activo, aparcado, bloqueado
> o en cola.

### Cuándo se actualiza

**Después de cada avance semántico significativo, no sólo al cambiar de paso.** Un paso
conversacional puede durar diez mensajes con varias respuestas importantes del Owner en
medio; escribir sólo al cerrar el paso pierde casi todo si el chat se corta.

Obligatorio actualizarlo:

```text
[ ] después de cada respuesta del Owner que cambie el entendimiento
[ ] al consolidar o descartar una alternativa
[ ] antes de formular la siguiente pregunta importante
[ ] antes de iniciar una operación larga
[ ] al cambiar de fase del método
[ ] antes de transferir, devolver, bloquear o aparcar
```

> **Orden de escritura:** cuando sea posible, **persistir primero lo comprendido y la
> siguiente acción, y formular la pregunta después.** Si el corte llega justo tras la
> pregunta, lo comprendido ya está a salvo.

### Formato — vive en el fichero del paquete

```text
CHECKPOINT — FEA-021/02 · DIS
actualizado: 2026-08-25T18:40
método:      DIS/Evolución · paso 2 de 5 (COMPARAR)
based_on:    docs/design/MEMORIA.md@v12 · patrón "tabla operativa"@2026-07-30 ·
             ADR-014@v2 · FEA-021/01(PRD)@v4
freshness:   vigente
last_meaningful_event:  respuesta del Owner 2026-08-25T18:36
resuelto:    · dirección A (densidad alta) descartada — no aguanta el texto largo
               del nombre de lote
             · paleta: se reutiliza el patrón "tabla operativa"
owner_captado: "prefiero perder densidad antes que truncar nombres" (2026-08-25T18:36)
pregunta_pendiente: ¿la fila expandible sustituye al detalle o convive con él?
siguiente:   explorar la 2ª dirección (detalle lateral) y compararla contra D3
falta_para_cerrar_la_capa:
             · 2ª dirección explorada · comparación escrita · memoria de diseño actualizada
```

Campos obligatorios: `based_on` (fuentes **y versiones** de las que depende) ·
`freshness` (`vigente` · `requiere revalidación` · `obsoleto`) · `last_meaningful_event`
· decisión o respuesta del Owner captada · pregunta exacta pendiente · siguiente acción
exacta.

Reglas:

1. **No es una transcripción.** Enlaces, no copias. Un checkpoint que crece con cada
   turno es un log, y los logs no se releen.
2. `siguiente` es **una acción concreta**. "Seguir con el diseño" no es válido.
3. Un checkpoint desactualizado —siguió trabajando y no lo escribió— es **un defecto del
   sistema**, no una omisión menor.
4. Escribirlo es parte del **gate de suspensión**, no del de terminación.

### Al reanudar

El agente **DEBE** comprobar si las fuentes de `based_on` cambiaron de versión.
**Revalida sólo la parte afectada.** No reinicia el método desde cero ni continúa sobre
supuestos obsoletos. Si algo cambió, marca `freshness: requiere revalidación` y dice qué
parte concreta va a revalidar.

### Obligatoriedad

> **CHECKPOINT es obligatorio para cualquier paquete cuyo trabajo pueda interrumpirse
> después de haber producido progreso significativo — sea estación o servicio.**

Una operación verdaderamente atómica **PUEDE** declarar `checkpoint: not_required` con
motivo escrito. Una consulta de INV, DOM o SEG que dure varias sesiones **sí** necesita
checkpoint aunque sea servicio.

### Sin duplicar

La columna `necesita para avanzar` del tablero es la **proyección en una línea** del
campo `siguiente`, generada por DSP. El checkpoint completo vive sólo en el paquete.
*"Retoma el item X con [equipo]"*, en lenguaje natural, es una entrada de la función
**Estado** de DSP: localiza el paquete, carga el checkpoint, comprueba `based_on`,
devuelve el control a esa capacidad en su paso.

---

## a.11 — Efecto sobre el kernel 1.3.0

| | |
|---|---|
| **Derogadas** | `G11` (13 cajas de capacidades) → a.1–a.4 · `G12` (orquestación sin tecnología) → DSP + SIS + sección (g) · `K0.9` (modo de fallo único) → a.7 |
| **Sustituidas** | `G14` → SIS |
| **Ajustadas** | `G13` deja de ser proporcional al riesgo: estructura por defecto de VER · `G34` escalado automático → recomposición de ruta trazada · `G52` regla de retirada → se aplica a capacidades materializadas · `G17` deja de ser criterio y pasa a instrumentarse por `escribe` disjunto · **`G08` se ajusta: el estado ejecutivo es una vista derivada del estado canónico, no un informe redactado** · `G32` se concreta en a.9 |
| **PENDIENTES, no derogadas** | **`G26` / JOURNAL** — los tableros son estado vigente, no secuencia de eventos, contexto transversal de sesión, por qué cambió el estado, operaciones fallidas ni recuperación tras escritura parcial. El runtime probablemente necesite un event log que **pueda** sustituirlo, pero eso se decide al diseñar memoria, eventos y recuperación en la sección (g), no ahora por inferencia. |
| **Previstas** | `G24` · `G34` vía rápida · `G53` → secciones (e), (f), (h) |

**Nota sobre (e):** una errata es un `DEF` con ruta corta, compuesta por el mismo
enrutador y con la misma traza. No es un carril aparte. **No se da por cerrado**: se
confirma en la sección (e).

---

## a.12 — Pruebas de conformidad derivables de esta sección

Una organización instalada cumple la sección (a) si SIS puede ejecutar y aprobar:

```text
T01 REANUDACIÓN      Chat nuevo, agente que no vio la conversación: "retoma X con Y".
                     Continúa desde el punto exacto, sin pedir resumen al Owner.
T02 CONCURRENCIA     Dos agentes en dos items del mismo equipo + DSP reconciliando +
                     Owner aparcando uno. Cero cambios perdidos, cero coordinación manual.
T03 DETERMINISMO     Mismo estado canónico ⇒ tablero y vista byte-idénticos.
T04 ESCRITOR ÚNICO   Ningún fichero canónico declara dos escritores.
T05 TRAZA DE RUTA    Todo item tiene `activadas` y `no activadas` con motivo escrito.
T06 FRENO PAR        La 3ª devolución entre el mismo par no se ejecuta, y existe el
                     registro con las dos posturas enfrentadas.
T07 FRENO CICLO      Un rebote repetido de 3+ capacidades se detecta y se detiene.
T08 RACHA SIS        El 3er item SIS consecutivo no se despacha si hay item de producto
                     listo, salvo excepción declarada. Todo item SIS enlaza su
                     justificación de producto.
T09 CHECKPOINT       Ningún paquete suspendido sin checkpoint, o con `not_required` sin
                     motivo. Todo checkpoint tiene `based_on` con versiones.
T10 APARCADO         Ningún item aparcado cerrado, desaparcado ni "limpiado" por
                     antigüedad.
T11 SÍNTESIS         Toda afirmación de una vista derivada enlaza su origen y es
                     comprobable leyendo los ficheros canónicos.
T12 SIN EQUIPOS VACÍOS  Ningún equipo materializado sin cola durante dos auditorías.
T13 PATRONES         Todo patrón vigente declara clase, alcance, criterios comprobables
                     y condición de caducidad.
T14 ROLLBACK         Todo rollback autónomo ejecutado cumplía los cinco requisitos y
                     dejó evento y evidencia.
T15 CONFLICTO        Ningún conflicto de decisión entre paquetes resuelto sin desacuerdo
                     registrado con las dos posturas.
```
